---
name: appblocks
description: Use when working with Tibbo AppBlocks (app.appblocks.io, AppBlocks Cloud) - reading, explaining, reviewing, changing or generating an AppBlocks project (exported JSON), visualising its logic and Tibbit hardware, using the AppBlocks Cloud API (projects, devices, OTA, workflows), or working in the AppBlocks editor in the browser.
---

# Tibbo AppBlocks: проекты, логика, железо, облако

AppBlocks — визуальный конструктор прошивок Tibbo: проект = плата + Tibbit/периферия + сервисы (features) +
логика из блоков. Из проекта генерируется прошивка: **`runtime: tios`** — Tibbo BASIC для TiOS (TPP2, TPP3, DS1101,
DS1102, EM510), **`zephyr`** — Zephyr C (сотни плат и TPP2/TPP3), `micropython`. AppBlocks Cloud — устройства,
OTA, переменные/таблицы/команды, облачные workflow, дашборды, HTTP API.
Ручной код на Tibbo BASIC — скилл tibbo-firmware; им же проверяй железо и код, сгенерированный для `tios`.

| Файл | Когда открывать |
|---|---|
| `references/editor.md` | Как устроен редактор и проект: шаги Hardware/Features/Application, Import/Export, Run/Debug/Release, runtime, **правила потоков** (поток с события, нет циклов, параметры видны только следующему блоку, ASYNC теряет параметры), переменные, плагины, частые ошибки. **Читать перед объяснением, ревью или проектированием логики.** |
| `references/format.md` | Формат экспорта JSON: верх, группы feature, узлы, связи, `{{$…}}`, правила правки. **Читать перед любой правкой JSON.** |
| `references/catalog.md` | Порты и поля узлов, полный список типов блоков, поля Tibbit, структуры Modbus/LUIS. |
| `references/generated-code.md` | Что генерирует AppBlocks для `tios`: файлы TIDE-проекта, переменные → процедуры `var_X_*`, маркеры вставки кода, замеченные особенности. |
| `references/catalog-examples.md` | Порты, поля и сокеты, собранные из **78 проектов appblocks.io** (59 типов узлов, 28 Tibbit). Основной справочник портов. |
| `references/api.md` | AppBlocks Cloud API: авторизация, проекты (код, сборка, версии, OTA, бандлы), устройства, группы, workspaces, workflow, дашборды. |
| `scripts/ab_tool.py` | Офлайн-разбор проекта: `summary`, `check`, `flow` (схема логики SVG), `tps` (железо → tps_check), `nodes`, `ids`. |
| `scripts/ab_api.py` | Клиент API: `me`, `projects`, `project <id> --out`, `versions`, `workspaces`, `devices`, `device`, `get`, `code`, `examples`/`example <имя>` (с запасным путём через appblocks.io), запись — только `create`/`update … --yes`. |
| `tests/run.sh` | Офлайн-тесты инструментов на примерах (и мост в tps_check, если tibbo-firmware лежит рядом). |
| `examples/*.json` | 6 проектов Tibbo: Modbus-шлюз с LCD на 4×RS485 и Modbus→MQTT (`ModbusMQTTGateway`, он же пример modbusmqtt; zephyr, GitHub), sprinkler5, accesscontrol6, hydroponics (TPP3), water_level_control_cloud (с appblocks.io, в т.ч. tios). |

Железо проверяет `tps_check.py` из скилла tibbo-firmware (найди Glob `**/tibbo-firmware/scripts/tps_check.py`): он же
рисует плату в стиле редактора AppBlocks (сокеты с номерами линий, SERn(k)/INTn(k), Tibbit, PoE, +5V, бюджет питания).

## 1. Откуда взять проект
1. **API** (лучший путь): `ab_api.py projects` → `ab_api.py project <id> --out p.json`. Ключ `abk_…` из Settings →
   API Keys в веб-приложении; передаётся `x-api-key`. Первым делом `ab_api.py me` (аккаунт и скоупы read/write).
2. **Экспорт**: в редакторе кнопка **Export** скачивает `.json`; пользователь прикладывает файл.
3. **Браузер** (§5) — смотреть проект в редакторе под входом пользователя.
4. **Примеры**: `https://appblocks.io/projects/<имя>.json`, где имя — последний сегмент страниц
   `appblocks.io/tutorials/*` и `appblocks.io/examples/*` (78 проектов: sprinkler1–6, accesscontrol1–6, modbusgateway,
   modbusmqtt, tbt22, hydroponics, http-server-tls…). `GET /api/projects/examples` в октябре 2026 отвечал 500.

**Сеть.** В облачной песочнице хосты AppBlocks доступны только после того, как пользователь добавит `api.appblocks.io`
и `appblocks.io` в разрешённые (claude.ai → Settings → Capabilities; в Team/Enterprise — администратор); до этого прокси
отвечает 403. Проверка: `ab_api.py me`. Если сеть закрыта: скрипт на подключённом компьютере пользователя, браузер или
файл экспорта. Документацию appblocks.io читай WebFetch (карта: `https://appblocks.io/sitemap.xml`).

**Ключ.** Только из окружения (`APPBLOCKS_API_KEY` или файл `APPBLOCKS_API_KEY_FILE` с правами 600, удалить после).
Не печатать, не сохранять в файлы, память, артефакты. У устройства поле `key` (MQTT) тоже не показывать.

## 2. Разбор и ревью
```
python3 scripts/ab_tool.py summary p.json        # плата, Tibbit, сервисы, переменные, таблицы, цепочки событий
python3 scripts/ab_tool.py check   p.json        # битые связи и ссылки, дубли ID, конфликты сокетов
python3 scripts/ab_tool.py flow    p.json flow.svg
python3 scripts/ab_tool.py tps     p.json --vin 24 --out cfg.json && python3 <tps_check.py> check cfg.json --svg board.svg
python3 scripts/ab_api.py code p.json --outdir gen   # что сгенерирует AppBlocks (для tios — Tibbo BASIC)
```
- Напряжение питания в проекте не хранится (только `POWERADAPTER`) — спроси или прими 24 В и напиши допущение.
- Ответ: что делает устройство (по цепочкам, человеческим языком) → картинки платы и логики → проблемы → что проверить.
- Ревью логики по правилам editor.md §4: поток без события (не попадёт в прошивку), параметр предыдущего блока после
  ASYNC-блока или через блок (пусто), рекурсия On Variable Changed, циклы через команды без условия выхода,
  `modbus_timeout`/`tbl_record_not_found` никуда не ведут, длинные потоки на tios, таблицы с большим MAXRECORDS,
  пароли открытым текстом (MQTT_PASSWORD, PASSWORD, WPW) вместо настроек, выключенные feature, нужные узлам.
- Ревью железа — `tps_check.py` (предупреждения AppBlocks про -SDWN, ±15 В, serial-сокеты, питание он повторяет).

## 3. Правка и генерация
Порядок: format.md §4 → правка **копии** экспорта скриптом Python (не строками вручную) → `check` = 0 ошибок →
`tps_check` для железа → `flow` для картинки → отдать файл (импорт кнопкой **Import**) или, с согласия, через API.
- Новые ID: `ab_tool.py ids N`. Порты и поля — из catalog-examples.md (78 проектов), catalog.md или из такого же узла в проектах пользователя.
- Логику строй по правилам потоков: каждое действие достижимо из события; значения между потоками — через переменные;
  повторы — таймеры/On Time Period/команды; после ASYNC — только переменные.
- Tibbit: сначала подбор и проверка раскладки/питания (tibbo-firmware), затем `tibbit_NN` с SOCKET и полями по образцу.
- **Проект на основе примера**: меняешь данные (настройки STG, команды, таблицы) — **оставляй ID тех, что переиспользуешь,
  а ненужные удаляй вместе со всеми ссылками на них**, включая панели (`web_dashboard`, `luis`, `ds_man`, `lcd_menu`, `cgg`:
  пункты настроек, кнопки-команды, таблицы консоли). Никогда не пересоздавай элемент с новым ID, не заменив старый
  ID по всему файлу. Так появились 9 из 11 ошибок первого СКУД-проекта (format.md §4 п.8).
- **Update Interval** (`global_vars.INTERVAL`) — не меньше 1 с. Короткие сигналы — на линию прерывания (editor.md §7а).
- `ab_tool.py check` = 0 ошибок обязателен перед записью; `ab_api.py code` без ошибок **не** означает, что Problems пуст.
- После создания/обновления проекта через API попроси пользователя открыть его и прислать вкладку Problems;
  каждую новую ошибку оттуда добавляй в `check` и в эти правила.

## 4. Запись в облако — только с подтверждением
Без вопросов: GET (чтение), `code` (генерация кода ничего не меняет в аккаунте).
С явным «да» пользователя на **конкретный** вызов (покажи метод, путь, что изменится): создание/изменение/удаление
проектов и версий, запись переменных и таблиц устройств, команды устройствам, **OTA-прошивка** устройств и групп,
workflow (создаются выключенными; включение — отдельное подтверждение), workspaces (DELETE удаляет всё).
`ab_api.py create|update … --yes` — флаг ставь только после подтверждения.

## 5. Редактор в браузере
Браузер, выбранный пользователем (встроенный в приложение Claude или Chrome), под его входом. Сначала читай.
Run/Deploy Release, OTA, сохранение, удаление — только после подтверждения. Пароли и ключи в поля не вводи.
Устройство в Debug-режиме останавливается без связи с редактором — не оставляй его в Debug на объекте.
Карта экранов — editor.md §1–2; если интерфейс отличается, сообщи пользователю и предложи обновить скилл.

## 6. Визуализация
- **Плата**: `tps_check.py --svg` — вид как в AppBlocks. **Логика**: `ab_tool.py flow` — группы панелями, узлы
  по позициям редактора, цвет по роли (события синие, логика фиолетовые, данные зелёные, связь красные, индикация
  оранжевые), подписи портов, при наведении — аргументы. **Текстом**: цепочки из `summary`.
- Показывай SVG инлайн, если можно, иначе файлом (PNG через cairosvg). Не перерисовывай вручную в другом стиле.
