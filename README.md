# Ductor Claw Code

**Telegram bot ([Ductor](https://github.com/PleasePrompto/ductor)) + open-source [Claw Code](https://github.com/instructkr/claw-code) CLI** — so you can drive the agent with **cheap [DeepSeek](https://www.deepseek.com/)** (and whatever else your `claw` build supports), not only Anthropic’s proprietary `claude` CLI.

This repo adds a **`claw` provider** to Ductor: subprocess calls to `claw --output-format json prompt …`, config `provider: "claw"`, models like `deepseek-chat` / `deepseek-reasoner`, auth via `DEEPSEEK_API_KEY` in `$DUCTOR_HOME/.env`, Telegram `/model` UI, rules, etc.

## Quick links

| Doc | Purpose |
|-----|---------|
| **[SETUP.md](SETUP.md)** | Install, `config.json`, `.env`, run the bot |
| **[FORK.md](FORK.md)** | What changed vs upstream Ductor |
| **[docs/UPSTREAM_SYNC.md](docs/UPSTREAM_SYNC.md)** | Merge Ductor + when Claw CLI changes |
| **[GITHUB_SETUP.md](GITHUB_SETUP.md)** | Remotes / first push |

**Companion repo (build `claw`):** [nordost8/claw-code-cheap-deepseek](https://github.com/nordost8/claw-code-cheap-deepseek)

## Upstream (vanilla Ductor)

All generic Ductor features, philosophy, Matrix, PyPI package name `ductor`, etc. are documented in the **original project**:

**[PleasePrompto/ductor — README (main)](https://github.com/PleasePrompto/ductor/blob/main/README.md)**

This fork tracks `upstream` = `https://github.com/PleasePrompto/ductor.git`. Sync: `./scripts/sync-upstream.sh` then merge/rebase.

## License

Same as upstream Ductor (see [LICENSE](LICENSE)).

---

## Українською

**Що це:** Ductor у Telegram + **Claw Code** замість лише офіційного Claude CLI → **дешевий DeepSeek** через `DEEPSEEK_API_KEY`.

**З чого почати:** [SETUP.md](SETUP.md). **Зібрати `claw`:** репо [claw-code-cheap-deepseek](https://github.com/nordost8/claw-code-cheap-deepseek).

**Оригінальний довгий опис Ductor** (усі фічі апстріму) — за посиланням вище на GitHub.
