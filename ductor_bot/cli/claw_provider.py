"""Async wrapper around the Claw Code CLI (Rust claw binary)."""

from __future__ import annotations

import json
import logging
import re
from collections.abc import AsyncGenerator
from pathlib import Path
from shutil import which
from typing import TYPE_CHECKING

from ductor_bot.cli.base import (
    BaseCLI,
    CLIConfig,
    docker_wrap,
)
from ductor_bot.cli.executor import SubprocessSpec, run_oneshot_subprocess
from ductor_bot.cli.stream_events import AssistantTextDelta, ResultEvent, StreamEvent
from ductor_bot.cli.types import CLIResponse

if TYPE_CHECKING:
    from ductor_bot.cli.timeout_controller import TimeoutController

logger = logging.getLogger(__name__)


class ClawCodeCLI(BaseCLI):
    """Async wrapper around ``claw`` (Claw Code)."""

    def __init__(self, config: CLIConfig) -> None:
        self._config = config
        self._working_dir = Path(config.working_dir).resolve()
        self._cli = "claw" if config.docker_container else self._find_cli()
        logger.info("Claw CLI wrapper: cwd=%s, model=%s", self._working_dir, config.model)

    @staticmethod
    def _find_cli() -> str:
        path = which("claw")
        if not path:
            msg = "claw CLI not found on PATH. Install Claw Code and ensure `claw` is on PATH."
            raise FileNotFoundError(msg)
        return path

    def _compose_prompt(self, prompt: str) -> str:
        cfg = self._config
        parts: list[str] = []
        if cfg.system_prompt:
            parts.append(cfg.system_prompt)
        parts.append(prompt)
        if cfg.append_system_prompt:
            parts.append(cfg.append_system_prompt)
        return "\n\n".join(parts)

    def _build_command(
        self,
        full_prompt: str,
        resume_session: str | None = None,
        continue_session: bool = False,
    ) -> list[str]:
        cfg = self._config
        cmd: list[str] = [self._cli, "--output-format", "json"]

        if cfg.permission_mode == "bypassPermissions":
            cmd.append("--dangerously-skip-permissions")
        else:
            pm = _map_claw_permission_mode(cfg.permission_mode)
            if pm:
                cmd += ["--permission-mode", pm]

        if cfg.model:
            cmd += ["--model", cfg.model]

        if cfg.allowed_tools:
            cmd += ["--allowedTools", ",".join(cfg.allowed_tools)]
        if cfg.disallowed_tools:
            cmd += ["--disallowedTools", ",".join(cfg.disallowed_tools)]

        if resume_session or continue_session:
            logger.info(
                "Claw one-shot prompt ignores resume/continue (resume=%s continue=%s)",
                bool(resume_session),
                continue_session,
            )

        if cfg.cli_parameters:
            cmd.extend(cfg.cli_parameters)

        cmd.append("prompt")
        cmd.append(full_prompt)
        return cmd

    async def send(
        self,
        prompt: str,
        resume_session: str | None = None,
        continue_session: bool = False,
        timeout_seconds: float | None = None,
        timeout_controller: TimeoutController | None = None,
    ) -> CLIResponse:
        full = self._compose_prompt(prompt)
        cmd = self._build_command(full, resume_session, continue_session)
        exec_cmd, use_cwd = docker_wrap(cmd, self._config)
        _log_cmd(exec_cmd)
        return await run_oneshot_subprocess(
            config=self._config,
            spec=SubprocessSpec(exec_cmd, use_cwd, prompt, timeout_seconds, timeout_controller),
            parse_output=_parse_claw_stdout,
            provider_label="Claw",
        )

    async def send_streaming(
        self,
        prompt: str,
        resume_session: str | None = None,
        continue_session: bool = False,
        timeout_seconds: float | None = None,
        timeout_controller: TimeoutController | None = None,
    ) -> AsyncGenerator[StreamEvent, None]:
        """Claw has no stream-json; emulate streaming via chunked text + ResultEvent."""
        resp = await self.send(
            prompt,
            resume_session=resume_session,
            continue_session=continue_session,
            timeout_seconds=timeout_seconds,
            timeout_controller=timeout_controller,
        )
        text = resp.result or ""
        step = max(400, min(2000, len(text) // 15 or 400))
        for i in range(0, len(text), step):
            yield AssistantTextDelta(type="assistant", text=text[i : i + step])
        yield ResultEvent(
            type="result",
            result=text,
            is_error=resp.is_error,
            returncode=resp.returncode,
            duration_ms=resp.duration_ms,
            duration_api_ms=resp.duration_api_ms,
            total_cost_usd=resp.total_cost_usd,
            usage=resp.usage,
            model_usage=resp.model_usage,
            num_turns=resp.num_turns,
            session_id=resp.session_id,
        )


def _map_claw_permission_mode(mode: str) -> str | None:
    m = mode.strip().lower().replace("_", "-")
    if m in ("bypasspermissions", "bypass-permissions"):
        return None
    if m in ("readonly", "read-only"):
        return "read-only"
    if m in ("workspace-write", "workspacewrite"):
        return "workspace-write"
    if m in ("danger-full-access", "dangerfullaccess", "full-access"):
        return "danger-full-access"
    if m in ("default", ""):
        return None
    return mode


def _log_cmd(cmd: list[str]) -> None:
    safe = [(c[:80] + "...") if len(c) > 80 else c for c in cmd]
    logger.info("Claw cmd: %s", " ".join(safe))


def _parse_cost_usd(raw: str | None) -> float | None:
    if not raw or not isinstance(raw, str):
        return None
    m = re.search(r"[\d.]+", raw.replace(",", ""))
    if not m:
        return None
    try:
        return float(m.group(0))
    except ValueError:
        return None


def _parse_claw_stdout(stdout: bytes, stderr: bytes, returncode: int | None) -> CLIResponse:
    stderr_text = stderr.decode(errors="replace")[:4000] if stderr else ""
    if stderr_text and returncode not in (0, None):
        logger.warning("Claw stderr (exit=%s): %s", returncode, stderr_text[:500])

    raw = stdout.decode(errors="replace").strip()
    if not raw:
        return CLIResponse(
            result=stderr_text or "(empty output)",
            is_error=True,
            returncode=returncode,
            stderr=stderr_text,
        )

    if returncode not in (0, None):
        return CLIResponse(
            result=stderr_text or raw[:2000],
            is_error=True,
            returncode=returncode,
            stderr=stderr_text,
        )

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        logger.exception("Failed to parse Claw JSON: %s", raw[:500])
        return CLIResponse(result=raw, is_error=True, returncode=returncode, stderr=stderr_text)

    message = data.get("message", "")
    if not isinstance(message, str):
        message = str(message)
    usage = data.get("usage") if isinstance(data.get("usage"), dict) else {}
    cost = _parse_cost_usd(data.get("estimated_cost"))

    return CLIResponse(
        result=message,
        is_error=False,
        returncode=returncode,
        stderr=stderr_text,
        usage=usage,
        total_cost_usd=cost,
        num_turns=data.get("iterations"),
    )
