# Что генерирует AppBlocks (runtime `tios`)

Проверено на проекте пользователя (TPP2W(G2), #13 в S9, #17 в S7, #10+#18, DHCP) через `POST /api/projects/code`
(`ab_api.py code p.json --outdir gen`). Результат — **обычный проект TIDE на Tibbo BASIC**, его можно открыть в TIDE,
собрать и проверять скиллом tibbo-firmware.

## Файлы
| Файл | Что внутри |
|---|---|
| `project.tpr` | `name=<проект>_dbg___<версия>`, `platform=TPP2W(G2)`, `debug=on`, `src_lib_ver=0_00`, список файлов |
| `global.tbh` | `#define` (INTERFACE_SWITCHING, SUPPORTS_TLS, DHCP_*, TBT_CLK_SOURCE…), `const` (FIRMWARE_VERSION, APP_ID = id проекта, линии Tibbit: `T13_S9_CLK=PL_IO_NUM_32`), include библиотек, `declare` переменных и процедур |
| `main.tbs` | `'****BOARD_CONFIG****'` (комментарий: какой Tibbit в каком сокете), `dim` переменных, `on_sys_init` → `boot()`, обработчики событий TiOS |
| `boot.tbs` | `sub boot()`: часовой пояс, `sys.onsystimerperiod=1`, сторожевой таймер, сеть (статический IP или `dhcp_start`), инициализация Tibbit (`tbt13_init(...)`, `tbt_pic_gra_init(...)`), `pat.play("B-B-B-")` |
| `device.tbs` | Интерфейсы и сокеты, колбэки библиотек (`callback_dhcp_ok`…), для каждой переменной — `var_<имя>_update / _update_completed / _set` |
| `libraries/…` | Копии библиотек Tibbo: time, datetime, sock, utils, dhcp, super_i2c, ssi, pic, tibbits/tbtNN |
| `cody.json` | Служебный файл ассистента (пустой) |

## Как устроено
- **Переменные** → глобальные `dim` + три процедуры. Аппаратные опрашиваются в `on_sys_timer` по `var_poll_timer`
  (период из Update Interval, по умолчанию 1000 мс): `var_X_update()` читает железо → `var_X_update_completed(value)`
  записывает и при изменении печатает `VAR> X changed…` (если `VARIABLES_DEBUG_PRINT`). `var_X_set(value)` — запись из логики.
- **Блоки** превращаются в код, вставленный в эти процедуры и обработчики. Поток On Variable Changed → в `'****var_X_changed****'`.
- **Маркеры вставки** `'****имя****'` — те же «Code Location» для своих плагинов: `GLOBAL_DEFINES`, `GLOBAL_CONSTS`,
  `GLOBAL_FILES`, `GLOBAL_INCLUDES`, `GLOBAL_DECLARATIONS`, `GLOBAL_DIMS`, `BOOT_DIMS`, `boot`, `boot_complete`,
  `EVENTS`, `on_sys_timer`, `var_poll_timer_elapsed`, `on_sock_data_arrival`, `on_net_link_change`,
  `callback_net_disconnected`, `interface_set`, `services_start`, `services_stop`, `callback_system_error`,
  `callback_dhcp_ok|failure|pre_clear_ip|pre_buffrq|buff_released`, `DEVICE_TBS_DIMS`, `DEVICE_TBS`,
  на каждую переменную `var_<X>_update|update_completed|updated|set|changed`, `var_poll_timer_<X>_elapsed`.
- Линии Tibbit в коде совпадают с `tps_check.py board <плата>` (S9 TPP2: A=32, B=33; S7: 15_TX3, 14_RX3, 3, 19_INT3).

## Блоки и настройки, проверенные генерацией (октябрь 2026)
Метки: **[генерация]** - проверено кодом от `POST /api/projects/code` (22.10.2026, TPP3W(G2) и TPP2W(G2), tios);
**[не проверено]** - ни импорт в редактор (Problems), ни компиляция в TIDE, ни железо не проверялись.
`ab_api.py code` работает без API-ключа [генерация].

- **Digital Line Set** (`node_digital_line_set`) [генерация]: `LINE_NUMBER="48", VALUE="0"` -> `io.lineset("48", "0")` - оба
  значения в кавычках. При `LINE_NUMBER="PL_IO_NUM_48"` будет `io.lineset("PL_IO_NUM_48", "0")`: строка неявно
  переводится в число (`val`) и даёт 0, то есть запись, скорее всего, уйдёт на линию 0 [не проверено в TIDE]. Как TIDE
  принимает `"48"` в аргументе типа `pl_io_num`, тоже [не проверено]. Блок **не генерирует `io.enabled`**: на линии,
  которую не сделал выходом фреймворк или Tibbit проекта, запись не подействует (tibbo-firmware SKILL.md §2).
  `ab_tool.py check`: ошибка, если `LINE_NUMBER` не число и не `{{$…}}`; предупреждение для линий вне 46-48 на TPP.
- **IF Condition** (`node_comparison`) [генерация]: аргумент `operator` уходит в Tibbo BASIC как есть: `"=="` -> `if a == b then`,
  `"<>"` -> `if a <> b then`. Редактор знает `=`, `<>`, `<`, `<=`, `>`, `>=` (для zephyr/micropython сам переводит `=` в `==`,
  `<>` в `!=`). `==` и `!=` для tios - ошибка `check` (компиляция в TIDE [не проверена]).
- **Custom Function** (`node_math_compound`) [генерация]: CODE становится телом `function <FUNCNAME>() as string` в device.tbs,
  объявление - в global.tbh, вызов - в месте блока. Внутри доступны процедуры фреймворка, например
  `signal_strength_set(&h1F)` [компиляция не проверена].
- **On Time Period** (`node_time_interval`) [генерация]: `sys.onsystimerperiod=1` (10 мс), в boot -
  `timer = INTERVAL*1000/sys.onsystimerperiod/10`, срабатывание при `count > timer`, то есть раз в N+1 тиков:
  0,5 с -> 51 тик = 0,51 с (+2 %), 5 с -> 5,01 с. Для точных интервалов учитывай.
- **`general.LEDPAT`** [генерация на 4gswitchover, water_level_control_cloud, wifiswitchover, tbt22]: при `"1"` в boot() добавляется
  `pat.play("R-R-~",PL_PAT_CANINT)` (мигание красным) перед `sys.halt` на трёх ошибках инициализации библиотеки Settings
  (stg_start, stg_check_all, stg_restore_multiple). В проекте без этих вызовов (tbt22) LEDPAT код не меняет. Стартовый
  `pat.play("B-B-B-",PL_PAT_CANINT)` в конце boot() есть при любом LEDPAT; свой `pat.play` из логики его перебивает.
- **Шкала уровня сигнала (5 синих LED) на TPP2/TPP3** [генерация на TPP3W(G2) и TPP2W(G2)]: global.tbh -
  `#define SIGNAL_STRENGTH_INDICATION 1`, `declare sub signal_strength_set(strength as byte)`,
  `declare sub signal_strength_indication_init()`; boot.tbs - `signal_strength_indication_init()` (линии `PL_IO_NUM_46/47/48` =
  reset/clock/data становятся выходами) и `signal_strength_set(0)` (шкала гаснет); device.tbs - `signal_strength_set`: 5 тактов
  по линии 47, данные на 48 активным LOW, биты 0..4 = LED 1..5. Вариант `SIGNAL_STRENGTH_INDICATION=2` - линии
  `PL_IO_NUM_19_SB1…23_SB5` (DS110x). Во время работы фреймворк вызывает `signal_strength_set(0)` только под
  `#IF CELLULAR_AVAILABLE`. Рецепт управления шкалой - editor.md §8.

## Что замечено (проверяй при ревью)
- Генератор **не останавливает** проект с #13 без #12: код инициализирует АЦП, но без ±15 В он будет читать мусор.
  Железо проверяй `tps_check.py`, а не полагайся на сборку.
- Комментарий «Set the timezone to UTC-12:00» стоит при `APP_TIMEZONE="0"` — комментарий шаблонный, верь значению.
- Debug-сборка (`debug=on`, `_dbg_` в имени); релиз — Run › Deploy Release Version / Download Release Binary (.tpc).
- Задача сборки (`/api/tasks`) живёт 3 минуты; для просмотра кода сборка не нужна — хватает `/api/projects/code`.
