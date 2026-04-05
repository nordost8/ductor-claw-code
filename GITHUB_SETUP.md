# Підключення до GitHub

Зараз у цьому клоні:

- **`upstream`** → `https://github.com/PleasePrompto/ductor.git` (оригінальний Ductor)

Зроби **порожній репозиторій** на GitHub (наприклад `ductor-claw-code`), потім:

```bash
cd /home/nordost/Projects/ductor-claw-code
git remote add origin https://github.com/YOUR_USER/ductor-claw-code.git
git push -u origin main
```

Якщо `origin` уже існує з помилковою URL — `git remote set-url origin https://github.com/YOUR_USER/ductor-claw-code.git`.

Після першого `push` у налаштуваннях репозиторія на GitHub додай опис і посилання на форк **Claw Code**.
