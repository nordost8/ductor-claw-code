# Ductor Claw Code — setup (Telegram bot + cheap DeepSeek)

This repo is **Ductor with a `claw` provider**. It talks to the **Claw Code** CLI (open source), not to Anthropic’s proprietary `claude` CLI, so you can use **cheap DeepSeek** and other OpenAI-compatible backends your Claw build supports.

## Suggested GitHub repository name

Use something like **`ductor-claw-code`** (clear: Ductor + Claw).

## Prerequisites

1. **Claw CLI on `PATH`** — build from the companion fork (recommended name: **`claw-code-cheap-deepseek`**). See that repo’s **`SETUP.md`**.
2. **Python 3.11+**
3. A **Telegram bot token** and your numeric **user id** (for `allowed_user_ids`).

## Install

```bash
git clone https://github.com/YOUR_USER/ductor-claw-code.git
cd ductor-claw-code
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

Confirm Claw is visible:

```bash
which claw
claw --version
```

## Configuration

Create `~/.ductor/config/config.json` (or set `DUCTOR_HOME` and put `config/config.json` there). Minimal example for **cheap DeepSeek**:

```json
{
  "provider": "claw",
  "model": "deepseek-chat",
  "telegram_token": "PASTE_BOT_TOKEN",
  "allowed_user_ids": [YOUR_TELEGRAM_USER_ID],
  "interagent_port": 8799
}
```

For the heavier reasoning model use `"model": "deepseek-reasoner"`.

To **lock the bot to reasoning only** (no `deepseek-chat`, no `@ds-chat`, `/model` wizard shows a single button), add:

```json
"model": "deepseek-reasoner",
"claw_models": ["deepseek-reasoner"]
```

### Switching chat vs reasoning in Telegram

- **`/model`** → choose **CLAW** → buttons **DEEPSEEK-CHAT** / **DEEPSEEK-REASONER**, or  
- Text commands (aliases are expanded to canonical ids):  
  **`/model deepseek-reasoner`**, **`/model reasoner`**, **`/model r1`**, **`/model ds-reasoner`**  
- Leading directives on the next message: **`@deepseek-reasoner`**, **`@reasoner`**, **`@r1`** (same keys as in `/model`).

Secrets go in **`$DUCTOR_HOME/.env`** (default `~/.ductor/.env`). At minimum for DeepSeek:

```bash
DEEPSEEK_API_KEY=sk-your-key-here
```

Do not commit `.env`.

## Run

```bash
source .venv/bin/activate
python -m ductor_bot
```

Or use your own systemd service / `pipx` layout; the important part is **`claw` on `PATH`** and **`.env` + `config.json`** as above.

## Companion repository

- **Claw (cheap DeepSeek)** — publish as **`claw-code-cheap-deepseek`** (see its `SETUP.md`).

## Syncing from upstream Ductor

See **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)** (Ductor + when to adjust for **Claw** updates).

```bash
./scripts/sync-upstream.sh
git merge upstream/main
```

Record in **`CHANGELOG_FORK.md`**.

## GitHub publish

See **`GITHUB_SETUP.md`**.
