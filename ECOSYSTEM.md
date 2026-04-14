# Ecosystem

This repository is a fork of **Ductor** that adds a **`claw` provider** (it runs the `claw` CLI).

## Repositories

- **Telegram bot (this repo)**: `nordost8/ductor-claw-code`
- **Claw CLI fork (DeepSeek)**: `nordost8/claw-code-cheap-deepseek`
- **Upstream Claw Code**: `instructkr/claw-code`
- **Upstream Ductor**: `PleasePrompto/ductor`

## Typical setup

1. Install/build the `claw` binary (DeepSeek fork if you want `deepseek-*` models).
2. Configure Ductor to use provider `"claw"` and choose a model (`deepseek-chat` / `deepseek-reasoner`).
3. Run the Telegram bot.

