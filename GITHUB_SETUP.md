# Publish on GitHub

## Suggested repository name

**`ductor-claw-code`** — Ductor fork with **Claw Code** + **cheap DeepSeek** support.

Full install steps: **[SETUP.md](SETUP.md)**.

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

## Publish on GitHub (English)

**Repo name:** **`ductor-claw-code`**. For installation see **[SETUP.md](SETUP.md)**.

This clone already has **`upstream`** pointing at the original Ductor. Create an empty repo on GitHub, add **`origin`** to your URL, then run **`git push -u origin main`**. In the repo description, link the companion repo **`claw-code-cheap-deepseek`**.
