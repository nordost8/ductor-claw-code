# Ductor Claw Code (fork)

**Setup guide (step by step, cheap DeepSeek): [SETUP.md](SETUP.md)**

This repository is **[Ductor](https://github.com/PleasePrompto/ductor)** extended with a **`claw` provider** so the bot can drive **[Claw Code](https://github.com/instructkr/claw-code)** — an open-source coding agent CLI — instead of relying only on Anthropic’s proprietary `claude` CLI.

**Companion repo (build `claw` for cheap DeepSeek):** publish it as **`claw-code-cheap-deepseek`** — its root **`SETUP.md`** has build + `DEEPSEEK_API_KEY` instructions.

Upstream Ductor is tracked as remote **`upstream`**. This fork adds:

- `ductor_bot/cli/claw_provider.py` — subprocess integration (`claw --output-format json prompt …`)
- Config: `provider: "claw"`, `cli_parameters.claw`, models `deepseek-chat` / `deepseek-reasoner` → provider `claw`
- Auth: `claw` on `PATH` + API keys (process env or `$DUCTOR_HOME/.env`, e.g. `DEEPSEEK_API_KEY`)
- Telegram/UI: model selector, welcome line, rules (`CLAUDE.md` when Claw is authed), etc.

## Requirements

1. **Claw Code CLI** — build/install from your fork (**suggested name: `claw-code-cheap-deepseek`**). The `claw` binary must be on `PATH`. See that repo’s root **`SETUP.md`** after you publish.
2. **Python 3.11+**, same as upstream Ductor.

## Quick start (Claw + DeepSeek)

```bash
git clone <YOUR_GITHUB>/ductor-claw-code.git
cd ductor-claw-code
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
mkdir -p ~/.ductor/config
# copy or edit ~/.ductor/config/config.json — minimal example:
```

```json
{
  "provider": "claw",
  "model": "deepseek-chat",
  "telegram_token": "YOUR_BOT_TOKEN",
  "allowed_user_ids": [YOUR_TELEGRAM_USER_ID]
}
```

```bash
# secrets (not committed): ~/.ductor/.env
echo 'DEEPSEEK_API_KEY=sk-...' >> ~/.ductor/.env
python -m ductor_bot
```

Use **`deepseek-reasoner`** in `model` if you want the reasoning variant. Other cheap models depend on what your **Claw** build exposes (OpenAI-compatible providers, etc.) — see the Claw repo docs.

## Syncing with upstream (Ductor + Claw)

**Ductor:** full branch model, file map, and **Claw CLI** dependency — **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)**.

Quick fetch:

```bash
./scripts/sync-upstream.sh
git merge upstream/main
```

Log merges in **`CHANGELOG_FORK.md`**. After upgrading **Claw** separately, re-test `claw --output-format json` against **`claw_provider.py`**.

## Українською

Це **форк Ductor** із підтримкою **Claw Code**. Окремо потрібен репозиторій/збірка **Claw** (другий репо). Підключення дешевих моделей (наприклад **DeepSeek**) — через змінні в `~/.ductor/.env` і модель у `config.json`, згідно з можливостями твого бінарника `claw`.

Повна інструкція: **`SETUP.md`**. GitHub: **`GITHUB_SETUP.md`**. Другий репо назви **`claw-code-cheap-deepseek`** (англійською на GitHub).
