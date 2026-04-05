# Ductor Claw Code (fork)

This repository is **[Ductor](https://github.com/PleasePrompto/ductor)** extended with a **`claw` provider** so the bot can drive **[Claw Code](https://github.com/instructkr/claw-code)** — an open-source coding agent CLI — instead of relying only on Anthropic’s proprietary `claude` CLI.

Upstream Ductor is tracked as remote **`upstream`**. This fork adds:

- `ductor_bot/cli/claw_provider.py` — subprocess integration (`claw --output-format json prompt …`)
- Config: `provider: "claw"`, `cli_parameters.claw`, models `deepseek-chat` / `deepseek-reasoner` → provider `claw`
- Auth: `claw` on `PATH` + API keys (process env or `$DUCTOR_HOME/.env`, e.g. `DEEPSEEK_API_KEY`)
- Telegram/UI: model selector, welcome line, rules (`CLAUDE.md` when Claw is authed), etc.

## Requirements

1. **Claw Code CLI** — build/install from your Claw fork (see companion repo). The `claw` binary must be on `PATH`.
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

## Syncing with upstream Ductor

```bash
git fetch upstream
git merge upstream/main
# resolve conflicts, test, then push to your origin
```

## Українською

Це **форк Ductor** із підтримкою **Claw Code**. Окремо потрібен репозиторій/збірка **Claw** (другий репо). Підключення дешевих моделей (наприклад **DeepSeek**) — через змінні в `~/.ductor/.env` і модель у `config.json`, згідно з можливостями твого бінарника `claw`.

Див. також **`GITHUB_SETUP.md`** — як прив’язати `origin` до твого GitHub.
