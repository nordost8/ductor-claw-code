# Ductor Claw Code

## Example (Telegram)

**You:** Use the Docker sandbox with Pillow installed: draw the Ukrainian flag (blue and yellow horizontal stripes), save it as `flag_ua.png`, and send the image back here.

**Bot:** _(uses tools — e.g. Dockerfile/sandbox, `pip install pillow`, Python script, file read)_ — replies with a short summary and **attaches `flag_ua.png`**.

Illustrative only. What actually runs depends on your **Ductor** setup (Docker skills, allowed tools, workspace) and **`claw`** permission mode — but this is the kind of multi-step task the stack is built for.

---

**Telegram bot ([Ductor](https://github.com/PleasePrompto/ductor)) + open-source [Claw Code](https://github.com/instructkr/claw-code) CLI** — drive the agent with **cheap [DeepSeek](https://www.deepseek.com/)** (and other backends your `claw` build exposes), not only Anthropic’s `claude` CLI.

This fork adds a **`claw` provider**: `claw --output-format json prompt …`, `provider: "claw"`, models like `deepseek-chat` / `deepseek-reasoner`, `DEEPSEEK_API_KEY` in `$DUCTOR_HOME/.env`, `/model` in Telegram, rules, etc.

## Quick links

| Doc | Purpose |
|-----|---------|
| **[SETUP.md](SETUP.md)** | Install, `config.json`, `.env`, run the bot |
| **[FORK.md](FORK.md)** | What changed vs upstream Ductor |
| **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)** | Merge Ductor + when Claw CLI changes |
| **[GITHUB_SETUP.md](GITHUB_SETUP.md)** | Remotes / first push |

**Companion repo (build `claw`):** [nordost8/claw-code-cheap-deepseek](https://github.com/nordost8/claw-code-cheap-deepseek)

## Upstream (vanilla Ductor)

Full upstream feature list, Matrix, PyPI `ductor`, etc.:

**[PleasePrompto/ductor — README (main)](https://github.com/PleasePrompto/ductor/blob/main/README.md)**

This fork tracks `upstream` = `https://github.com/PleasePrompto/ductor.git`. Sync: `./scripts/sync-upstream.sh` then merge/rebase.

## License

Same as upstream Ductor (see [LICENSE](LICENSE)).
