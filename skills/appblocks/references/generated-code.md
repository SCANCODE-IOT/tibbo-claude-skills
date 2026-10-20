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

## Что замечено (проверяй при ревью)
- Генератор **не останавливает** проект с #13 без #12: код инициализирует АЦП, но без ±15 В он будет читать мусор.
  Железо проверяй `tps_check.py`, а не полагайся на сборку.
- Комментарий «Set the timezone to UTC-12:00» стоит при `APP_TIMEZONE="0"` — комментарий шаблонный, верь значению.
- Debug-сборка (`debug=on`, `_dbg_` в имени); релиз — Run › Deploy Release Version / Download Release Binary (.tpc).
- Задача сборки (`/api/tasks`) живёт 3 минуты; для просмотра кода сборка не нужна — хватает `/api/projects/code`.
