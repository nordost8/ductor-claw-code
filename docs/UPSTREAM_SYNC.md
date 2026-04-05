# Upstream sync architecture (ductor-claw-code)

This repo has **one Git upstream** (Ductor) but **depends on another moving product** (Claw CLI). Plan updates on **two axes**.

## 1. Ductor (this repo’s `upstream`)

| Remote     | URL |
|-----------|-----|
| `upstream` | `https://github.com/PleasePrompto/ductor.git` |
| `origin`   | your `ductor-claw-code` |

**`main`** = PleasePrompto/ductor + **Claw provider patch** (Python only for this fork).

### Sync Ductor

```bash
git fetch upstream
git merge upstream/main
# or: git rebase upstream/main
```

### Patch surface (expect conflicts here)

| Files | Role |
|-------|------|
| `ductor_bot/cli/claw_provider.py` | **New** — usually no upstream conflict unless they add a file with same name |
| `ductor_bot/cli/factory.py`, `auth.py`, `service.py` | Factory / auth / `resolve_provider` |
| `ductor_bot/config.py` | `CLAW_MODELS`, `cli_parameters.claw`, `provider_for` |
| `ductor_bot/orchestrator/core.py`, `providers.py`, `selectors/model_selector.py` | Wiring + UI |
| `ductor_bot/messenger/telegram/app.py`, `welcome.py` | Directives / labels |
| `ductor_bot/text/response_format.py`, `workspace/rules_selector.py` | UX |

Take **upstream** for unrelated fixes; keep **Claw** branches in factory/service/config/orchestrator.

## 2. Claw Code (separate repo)

Your **`claw`** binary comes from **`claw-code-cheap-deepseek`**. When **that** repo rebases on main Claw:

- JSON output of `claw --output-format json prompt …` might change.
- Flags (`--dangerously-skip-permissions`, `--model`, …) might change.

If the CLI contract breaks, update **`ductor_bot/cli/claw_provider.py`** and re-test Telegram.

**Order of operations after big Claw releases:**

1. Sync **claw-code** fork → build `claw` → manual JSON smoke test.
2. Sync **ductor-claw-code** from Ductor upstream.
3. Run Ductor against new `claw`; adjust `claw_provider.py` if needed.

## Helper

```bash
./scripts/sync-upstream.sh
```

## Changelog

Record Ductor upstream SHA after each merge in **`CHANGELOG_FORK.md`** (root).

---

## Українською

**Два рівні оновлень:** (1) **Ductor** — `git fetch/merge upstream` у цьому репо; конфлікти переважно в перелічених Python-файлах. (2) **Claw** — окремий репо; після оновлення Claw перевір вихід JSON і за потреби поправ **`claw_provider.py`**.

Спочатку оновлюй **Claw**, збери бінарник, потім **Ductor**-форк. Деталі для репо Claw — у їхньому **`docs/UPSTREAM_SYNC.md`**.
