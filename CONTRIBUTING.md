# Contributing

**English** · [Русский](#участие-в-проекте)

Thank you for helping improve the Tibbo skills.

## Reporting a problem

The most useful report shows what Claude got wrong on a real task:

- **Firmware:** platform (`TPP3W(G2)` etc.), the prompt, the wrong answer, and what TIDE or the device actually did (compiler message, behaviour).
- **Hardware:** the `cfg.json` you checked with `tps_check.py`, or the Tibbits per socket and the supply voltage.
- **AppBlocks:** the exported project (remove passwords and keys first) and the text of the editor's **Problems** tab.

Use the issue templates: *Wrong answer*, *Tool bug*, *Outdated data*.

## Changing the skills

1. Fork the repository and create a branch.
2. Edit the files under `skills/<name>/`. Keep `SKILL.md` short: details belong in `references/`.
3. When you fix a mistake, add a regression case to `tests/` so it does not come back
   (for example a configuration in `skills/tibbo-firmware/tests/` or a check in `skills/appblocks/tests/run.sh`).
4. Run the tests and build the packages:

   ```bash
   sh skills/tibbo-firmware/tests/run.sh
   sh skills/appblocks/tests/run.sh
   sh tools/package.sh
   ```

5. Add a line to `CHANGELOG.md` under *Unreleased* and open a pull request.

Rules for the content:

- API names, signatures and constants must come from Tibbo sources (github.com/tibbotech, docs.tibbo.com), never from memory.
- Scripts use the Python standard library only.
- Never commit API keys, passwords, device keys or customer data.

## Releasing (maintainers)

Update the version in `.claude-plugin/marketplace.json` and `CHANGELOG.md`, commit, then either
open **Actions → Release → Run workflow** and enter the version (for example `v1.1.0`), or push a tag:

```bash
git tag v1.1.0 && git push origin v1.1.0
```

The *Release* workflow runs the tests and attaches `tibbo-firmware.zip` and `appblocks.zip` to the release.

---

# Участие в проекте

Спасибо, что помогаете улучшать скиллы Tibbo.

## Как сообщить о проблеме

Самое полезное — показать, где Claude ошибся на реальной задаче:

- **Прошивка:** платформа (`TPP3W(G2)` и т.п.), запрос, неверный ответ и что на самом деле сказала TIDE или сделало устройство.
- **Железо:** `cfg.json`, проверенный `tps_check.py`, или Tibbit по сокетам и напряжение питания.
- **AppBlocks:** экспорт проекта (сначала уберите пароли и ключи) и текст вкладки **Problems** редактора.

Используйте шаблоны issue: *Wrong answer*, *Tool bug*, *Outdated data*.

## Как вносить изменения

1. Сделайте fork и создайте ветку.
2. Правьте файлы в `skills/<имя>/`. `SKILL.md` держите коротким, подробности — в `references/`.
3. Исправляя ошибку, добавьте регрессионный тест в `tests/`, чтобы она не вернулась.
4. Запустите тесты и сборку пакетов (команды выше).
5. Добавьте строку в `CHANGELOG.md` в раздел *Unreleased* и откройте pull request.

Правила для содержимого:

- Имена API, сигнатуры и константы — только из источников Tibbo (github.com/tibbotech, docs.tibbo.com), не по памяти.
- Скрипты используют только стандартную библиотеку Python.
- Никогда не коммитьте API-ключи, пароли, ключи устройств и данные заказчиков.

## Выпуск версии (для сопровождающих)

Обновите версию в `.claude-plugin/marketplace.json` и `CHANGELOG.md`, затем откройте **Actions → Release → Run workflow** и введите версию (например `v1.1.0`) или отправьте тег (см. команду выше):
workflow *Release* прогонит тесты и приложит к релизу `tibbo-firmware.zip` и `appblocks.zip`.
