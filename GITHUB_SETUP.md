# Publish on GitHub

## Suggested repository name

**`ductor-claw-code`** — Ductor fork with **Claw Code** + **cheap DeepSeek** support.

Full install steps: **[SETUP.md](SETUP.md)** (English + Українською).

## Remotes in this clone

- **`upstream`** → `https://github.com/PleasePrompto/ductor.git`

## First push

Create an **empty** repo on GitHub, then:

```bash
cd /path/to/ductor-claw-code
git remote add origin https://github.com/YOUR_USER/ductor-claw-code.git
git push -u origin main
```

If `origin` already exists with a wrong URL:

```bash
git remote set-url origin https://github.com/YOUR_USER/ductor-claw-code.git
git push -u origin main
```

Link the companion Claw fork in the repo description (suggested name: **`claw-code-cheap-deepseek`**).

---

## Публікація на GitHub (українською)

**Назва репо:** **`ductor-claw-code`**. Інструкція з установки — **[SETUP.md](SETUP.md)**.

У цьому клоні вже є **`upstream`** на оригінальний Ductor. Створюєш порожній репозиторій на GitHub, додаєш **`origin`** на свій URL і робиш **`git push -u origin main`**. У описі репозиторія вкажи посилання на **`claw-code-cheap-deepseek`**.
