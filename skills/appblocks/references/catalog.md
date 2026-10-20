# Каталог feature и узлов (из экспортов Tibbo: ModbusMQTTGateway, bp_modbus_gateway_lcd_v11)

Автоматически собрано из примеров. Встречаются не все типы AppBlocks — новые типы смотри в свежем экспорте пользователя.

## Узлы логики (`node_*`)

| Тип | Входы (TARGET_PORT) | Выходы (SOURCE_PORT) | ARGUMENTS (TARGETPARAM) | Свои поля |
|---|---|---|---|---|
| `node_beep` | beep.play | — | patternstring | CANINT, FREQ |
| `node_button` | — | on_button_pressed | — | — |
| `node_button_released` | — | on_button_released | — | — |
| `node_command_trigger` | command_trigger | — | data | COMMAND |
| `node_command_triggered` | — | on_command_triggered | — | COMMAND |
| `node_comparison` | comp | false_output, true_output | operand1, operand2, operator | — |
| `node_compound_condition` | cond | false_output, true_output | — | EXPRESSIONS, OPERATOR |
| `node_datetime` | timestamp_get | timestamp_now | — | — |
| `node_debug` | sys.debugprint | — | printstring | — |
| `node_group` | — | — | — | — |
| `node_lcd_text_widget` | lcd_print_text | — | text | VISIBLE, WIDGET |
| `node_modbus_write` | modbus_poll | modbus_response, modbus_timeout | — | DATA, DEVICE, DEVICEID, DEVICEIP, DEVICEPORT, ENDIAN, FUNCTIONCODE, LENGTH, PROTOCOL, REGISTER_ADDRESS, SERIAL_PORT, VARTYPE |
| `node_mqtt_pub` | mqtt_publish | done | publish_data, qos, retain, topic | — |
| `node_network_changed` | — | network_changed | — | NETWORK_EVENT, NETWORK_TYPE |
| `node_pat` | pat.play | — | patternstring | CANINT |
| `node_settings_init` | stg_init | done | — | — |
| `node_socket_data_arrival` | — | sock_data_arrival | — | SOCKET |
| `node_socket_event` | — | sock_connection_event | — | EVENT_TYPE, SOCKET |
| `node_switch` | switch_exec | <case ID> | — | CASES, VALUE |
| `node_system` | — | boot | — | — |
| `node_system_reboot` | sys.reboot | — | — | — |
| `node_table` | tbl_record_find | tbl_record_found, tbl_record_not_found | field_value, find_index | FIELD_NAME, OPERATOR, TABLE, WRAPAROUND |
| `node_table_insert` | tbl_add | — | NAME, TS, VALUE, timestamp, value | TABLE |
| `node_table_row_count` | tbl_count | tbl_count_result | — | TABLE |
| `node_table_update` | tbl_update | — | — | FIELDS, FIELD_NAME, OPERATOR, TABLE, VALUE |
| `node_time_delay` | delay_start | delay_elapsed | — | DURATION |
| `node_timer_completed` | — | timer_complete | — | TIMER |
| `node_timer_start` | timer_start | done | time | REPEAT, TIMER |
| `node_variable_set` | set_value | variable_set_done | value | VARIABLE |

## Остальные feature (аппаратура, сервисы, данные)

### `boardsetting`
Поля: 5VDIRECT, ASM, DIN, GPRSANTENNA, ID, NOTES, POE, POWERADAPTER, TPB, VPK, WIFIANTENNA

```json
{"ID": "mquecbkte5plbdjo9sl", "POE": "0", "5VDIRECT": "0", "WIFIANTENNA": "0", "GPRSANTENNA": "0", "TPB": "true", "VPK": "1", "DIN": "1", "POWERADAPTER": "apr-p0008", "ASM": "asm+rp", "NOTES": ""}
```

### `bt`
Поля: DEVICENAME, EMULATION, ENABLED, ID, RXBUF, TXBUF

```json
{"ID": "mrubrq7oy4s2mz0bcrt", "ENABLED": "0", "DEVICENAME": "MyBTDevice", "EMULATION": "PL_WLN_BT_EMULATION_MODE_MICROCHIP", "TXBUF": "1", "RXBUF": "1"}
```

### `cell`
Поля: CELL_APN, CELL_BAND_TYPE, CELL_LOG_LEVEL, CELL_MODE, CELL_PIN, CELL_PW, CELL_UN, CELL__DEBUG_PRINT, ENABLED, ID

```json
{"ID": "mrubrq7om0lm1x7reyj", "ENABLED": "0", "CELL_MODE": "CELL__PPP_MODE_ISENABLED", "CELL_APN": "", "CELL_UN": "myusername@realm", "CELL_PW": "", "CELL_PIN": "?", "CELL_BAND_TYPE": "1", "CELL__DEBUG_PRINT": "1", "CELL_LOG_LEVEL": "2"}
```

### `cgg`
Поля: ADVANCED, CONSOLE, CONSOLE_PREVIEW, DEBUG_PRINT, ENABLED, GENERAL, GROUPS, ID, INTERVAL, PASSWORD, SERVER, SERVER_PORT, SETTINGS, TABLES, TLS, USERNAME, WIDGETS, WIDGET_GROUPS

```json
{"ID": "mrubrq7pal0qeoxr0u8", "GENERAL": "", "SETTINGS": "", "CONSOLE": "", "ADVANCED": "", "ENABLED": "0", "SERVER": "192.168.1.201", "SERVER_PORT": "1883", "USERNAME": "", "PASSWORD": "", "DEBUG_PRINT": "0", "WIDGETS": [], "WIDGET_GROUPS": [{"id": "widget_group", "settings": {"ID": "mrubrq7pxwbce02prvo", "GROUPID": "group1", "NAME": "Group", "WIDGETS": []}}], "INTERVAL": "1", "TLS": "0", "GROUPS": [{"id": "luis_group", "settings": {"ID": "mrubrq7pau0c4r6v916", "GROUPID": "group1", "NAME": "General", "SETTINGS": []}}], "CONSOLE_PREVIEW": "cloud", "TABLES": []}
```

### `commands`
Поля: COMMANDS, ID

```json
{"ID": "mrubrq7km9e93bdx0sf", "COMMANDS": [{"id": "command", "settings": {"ID": "mruc4xydr4k64vqozom", "NAME": "POLL_NEXT", "DESCRIPTION": ""}}, {"id": "command", "settings": {"ID": "mrucs2e3hmen04majqr", "NAME": "STORE_VALUE", "DESCRIPTION": ""}}, {"id": "command", "settings": {"ID": "mrue5t3gwuenm9o1hm", "NAME": "POLL_END", "DESCRIPTION": ""}}, {"id": "command", "settings": {"ID": "mrzomxzmdo7hdqzw427", "NAME": "PUBLISH_NEXT", "DESCRIPTION": ""}}]}
```

### `cron`
Поля: ID, SCHEDULES

```json
{"ID": "mrubrq7j6psp7kuo3s6", "SCHEDULES": []}
```

### `custom_feature_id`
Поля: ENABLED, ID, MODBUS_TIMEOUT_MS, channels

```json
{"ENABLED": "1", "ID": "ms002ypf3b558il977r"}
```

### `custom_features`
Поля: FEATURES, ID

```json
{"ID": "mrubrq7xnn81nz3otvq", "FEATURES": [{"id": "custom_feature", "settings": {"ID": "mrzvp95zkzocplf5pjq", "NAME": "Feature", "FEATURE_ID": "custom_feature_id", "VERSION": "1.0.0", "RUNTIMES": "zephyr", "TYPE": "service", "REQUIREMENTS": "", "DEPENDENCIES": "", "CAPABILITIES": "", "SETTINGS": [], "CODE_BLOCKS": [{"id": "custom_feature_code_block", "settings": {"ID": "mrzvpd65axk75lzpcan", "GENERAL": "", "ADVANCED": "", "TYPE": "code", "RUNTIME": "zephyr", "NAME": "", "CODE_ID": "", "LOCATION": "PRJ_CONF_OVERRIDES", "CODE": "CONFIG_NET_BUF_RX_COUNT=24\nCONFIG_NET_BUF_TX_COUNT=36\nCONFIG_MAIN …
```

### `datasheet_pages`
Поля: ENABLED, ID, PAGES

```json
{"ID": "mojv7rzxr2j7tlfrwrn", "ENABLED": "1", "PAGES": "[{\"id\":\"dp_1777455674493\",\"title\":\"Features\",\"content\":\"> Tibbo Modbus Gateways route Modbus requests and replies between Modbus TCP, Modbus ASCII, and Modbus RTU masters and slaves. \\n \\n---\\n \\n## Networking\\n \\n- **100/10 Mb Ethernet port** (standard on all models)\\n- **Optional Wi-Fi port:**\\n  - WEP / WPA / WPA2 security support\\n  - Automatic failover to Wi-Fi when the Ethernet cable is unplugged\\n- **IP configuration:** Static IP or DHCP\\n---\\n \\n## Serial Ports\\n \\n### TPS2(G2)-based Gateways\\n- Up to ** …
```

### `datetime`
Поля: ID

```json
{"ID": "mquece9nfn3kvdkizho"}
```

### `dhcp`
Поля: ID

```json
{"ID": "mquece9n9swb69v12g"}
```

### `display_lib`
Поля: ID

```json
{"ID": "mql0uvylvulg18wxzp"}
```

### `dns`
Поля: DNS_DEBUG_PRINT, DNS_TIMEOUT, ENABLED, ID, SERVER1, SERVER2

```json
{"ID": "mrubrq7r3ge8ga8smn3", "ENABLED": "1", "SERVER1": "8.8.8.8", "SERVER2": "", "DNS_TIMEOUT": "5000", "DNS_DEBUG_PRINT": "0"}
```

### `ds_man`
Поля: ENABLED, GROUPS, ID

```json
{"ID": "mrubrq7xu2hhyy4utwf", "ENABLED": "0", "GROUPS": []}
```

### `fd`
Поля: ENABLED, FILES, ID, SECTORS

```json
{"ID": "mrubrt5tezlln38nbsv", "ENABLED": "1", "FILES": "32", "SECTORS": "100"}
```

### `filenum`
Поля: ID

```json
{"ID": "mrubrtjqr98nsxe2lsb"}
```

### `files`
Поля: FILES, ID

```json
{"ID": "mnwixtdp2i5oqz53d9g", "FILES": []}
```

### `flash_devices`
Поля: FLASH_DEVICES, ID

```json
{"ID": "mqueccssuznhrlmb4ap", "FLASH_DEVICES": [{"id": "flash_device", "settings": {"ID": "mrubri0k6lw5x4pzr9b", "NAME": "flash0", "BUILTIN": "1", "BUILTINID": "flash0", "LINKED_FEATURE": "", "FLASH_DEVICE_NAME": "flash0", "PARTITIONS": [{"id": "flash_partition", "settings": {"ID": "mrubri0kwbwn28dswk", "NAME": "boot_partition", "ADDRESS": "8200", "SIZE": "457728", "LABEL": "boot_partition", "MOUNT_POINT": ""}}]}}, {"id": "flash_device", "settings": {"ID": "mrubri0klfywzjonti", "NAME": "at45db081e", "BUILTIN": "1", "BUILTINID": "at45db081e", "LINKED_FEATURE": "", "FLASH_DEVICE_NAME": "at45db08 …
```

### `general`
Поля: DEVICE_NAME, FIRMWAREVERSION, ID, LATITUDE, LOGGING, LONGITUDE, TIMEZONE

```json
{"ID": "mquecbkttwt2hgq703", "DEVICE_NAME": "Device_Name_1", "FIRMWAREVERSION": "1.0.0", "TIMEZONE": "27", "LATITUDE": "0", "LONGITUDE": "0", "LOGGING": "sys.debugprint"}
```

### `global_vars`
Поля: AUTOVARS, DEBUG_PRINT, ID, INTERVAL, VARS

```json
{"ID": "mquecbktwgvfvpgurtd", "INTERVAL": "1", "DEBUG_PRINT": "0", "VARS": [{"id": "variable", "settings": {"ID": "mruc3avst0no8wlazw", "VARNAME": "current_poll_index", "DATATYPE": "float", "NAME": "", "FEATURE": "", "FEATURE_SETTING": "", "MINIMUM": "", "MAXIMUM": "", "DEFAULT": "0", "POLL_INTERVAL": ""}}, {"id": "variable", "settings": {"ID": "mruc4jrn7t8k59y0zmo", "VARNAME": "devices_total", "DATATYPE": "float", "NAME": "", "FEATURE": "", "FEATURE_SETTING": "", "MINIMUM": "", "MAXIMUM": "", "DEFAULT": "0", "POLL_INTERVAL": ""}}, {"id": "variable", "settings": {"ID": "mruc6oin6v7i8i6u8ee", " …
```

### `http`
Поля: DEBUG_PRINT, ENABLED, ID, MAX_REQUESTS

```json
{"ID": "mrubrq7qgx4eh0mu6el", "ENABLED": "0", "MAX_REQUESTS": "5", "DEBUG_PRINT": "0"}
```

### `httpserver`
Поля: ADVANCED, DEBUG_PRINT, ENABLED, ENDPOINTS, GENERAL, ID, PORT, RXBUF, SOCKETS, TLS_ENABLED, TXBUF, VARBUF

```json
{"ID": "mrubrq7qm4xcnjyt9s8", "GENERAL": "", "ADVANCED": "", "ENABLED": "1", "PORT": "80", "SOCKETS": "2", "TXBUF": "10", "RXBUF": "10", "VARBUF": "1", "ENDPOINTS": [], "DEBUG_PRINT": "0", "TLS_ENABLED": "0"}
```

### `lcd`
Поля: BACKCOLOR, ENABLED, FORECOLOR, GENERAL, GROUPS, ID, IMAGES, IMAGES_GROUP, LCD_SCREEN_WIDGET_COLUMNS, LCD_SCREEN_WIDGET_ROWS, LOGFONT, SCREENS, SETTINGS, WIDGETS

```json
{"ID": "mrubrq7uqk6oqszelbr", "GENERAL": "", "IMAGES_GROUP": "", "SETTINGS": "", "ENABLED": "0", "BACKCOLOR": "#000000", "FORECOLOR": "#ffffff", "LOGFONT": "LCD_SMALL_FONT", "WIDGETS": [], "SCREENS": [], "IMAGES": [], "LCD_SCREEN_WIDGET_COLUMNS": 320, "LCD_SCREEN_WIDGET_ROWS": 240, "GROUPS": [{"id": "luis_group", "settings": {"ID": "mrubrq7u7p7g8mggced", "GROUPID": "group2", "NAME": "General", "SETTINGS": []}}]}
```

### `lcd_graph`
Поля: ENABLED, FILL, HEIGHT, ID, MAXY, MINY, STARTX, STARTY, WIDTH

```json
{"ID": "mrubrq7vlwp02vzb4n", "ENABLED": "0", "MINY": "-100", "MAXY": "100", "STARTX": "0", "STARTY": 0, "WIDTH": 320, "HEIGHT": 240, "FILL": "#00ff00"}
```

### `linked_setting`
Поля: FEATURE, ID, LINKEDSETTING, SETTINGID

```json
{"ID": "mrubrskaax2o6rk7gxj", "SETTINGID": "BAUD", "LINKEDSETTING": "mrubrsjqjgez7pq729s", "FEATURE": "mrubrlt15u4ollyy4vs"}
```

### `log`
Поля: ENABLED, ID

```json
{"ID": "mrubrq7leok0mwos33i", "ENABLED": "1"}
```

### `luis`
Поля: BTENABLED, ENABLED, GROUPS, ID, PASSWORD, START_ENABLED, WEBENABLED

```json
{"ID": "mrubrq7wbczxfpnpxe9", "ENABLED": "0", "BTENABLED": "1", "WEBENABLED": "0", "START_ENABLED": "1", "PASSWORD": "", "GROUPS": []}
```

### `mbedtls`
Поля: CONFIGS, ENABLED, ID

```json
{"ID": "mrubrq7spks63m3sm2", "ENABLED": "1", "CONFIGS": "\nCONFIG_MBEDTLS_HEAP_SIZE=30000\nCONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN=4096                \n"}
```

### `modbus`
Поля: ID

```json
{"ID": "mruc8kyow8g1vgjgacj"}
```

### `modbus_master`
Поля: DEBUG_PRINT, FRAME_DELAY, ID, MAX_REQUESTS, MODBUSDEVICES, POLL_INTERVAL, TIMEOUT

```json
{"ID": "mrubrq7t0jv8nqk7bvd", "DEBUG_PRINT": "0", "TIMEOUT": "1000", "POLL_INTERVAL": "1000", "FRAME_DELAY": "2", "MAX_REQUESTS": "10", "MODBUSDEVICES": []}
```

### `modbus_slave`
Поля: DEBUG_PRINT, DEVICEID, ID, MODBUSTABLEITEMS, SLAVEPROTOCOL, SLAVE_SERIAL_PORT, SLAVE_TCP_PORT

```json
{"ID": "mrubrq7uvezopfuci", "DEBUG_PRINT": "0", "SLAVEPROTOCOL": "modbus_RTU", "DEVICEID": "1", "SLAVE_SERIAL_PORT": "", "SLAVE_TCP_PORT": "502", "MODBUSTABLEITEMS": []}
```

### `mqtt`
Поля: CERTIFICATE, CERTIFICATEFILE, CERTIFICATE_PATH, CLIENT_CERTIFICATE_PATH, ENABLED, GENERAL, ID, MQTT_APP_CLIENT_ID, MQTT_DEBUG_PRINT, MQTT_DESTINATION_PORT, MQTT_KEEPALIVE_INTERVAL, MQTT_NAME, MQTT_PASSWORD, MQTT_SERVER_HOST, MQTT_TLS, TOPICS

```json
{"ID": "mrubrq7paiw1hmfo1bm", "GENERAL": "", "CERTIFICATE": "", "ENABLED": "1", "MQTT_APP_CLIENT_ID": "Client_ID_1", "MQTT_NAME": "MQTT_Name_1", "MQTT_PASSWORD": "Password", "MQTT_SERVER_HOST": "1.0.0.1", "MQTT_DESTINATION_PORT": "1883", "MQTT_TLS": "0", "MQTT_KEEPALIVE_INTERVAL": "30", "MQTT_DEBUG_PRINT": "1", "CERTIFICATEFILE": "", "CERTIFICATE_PATH": "", "CLIENT_CERTIFICATE_PATH": "", "TOPICS": []}
```

### `mqtt_lib`
Поля: ID

```json
{"ID": "mrzo79kt29gl5doepyt"}
```

### `net`
Поля: DHCP, ENABLED, GI, ID, IP, NM

```json
{"ID": "mquecbkt7eahgszzc6g", "ENABLED": "1", "DHCP": "0", "IP": "192.168.1.40", "NM": "255.255.255.0", "GI": "1.0.0.1"}
```

### `peripheral_wiring`
Поля: CUSTOM_GROUPS, CUSTOM_SHAPES, ENABLED, ID, LAYOUT_DATA

```json
{"ID": "mquecdkhubfazo3zmsk", "ENABLED": "1", "LAYOUT_DATA": "[]", "CUSTOM_SHAPES": "[]", "CUSTOM_GROUPS": "[]"}
```

### `smtp_client`
Поля: ADVANCED, AUTH, AUTH_METHOD, ENABLED, FROM_ADDRESS, GENERAL, ID, LOG_LEVEL, PASSWORD, PORT, SECURITY, SERVER, TIMEOUT, USERNAME

```json
{"ID": "mrubrq7thy56poqyyzm", "GENERAL": "", "AUTH": "", "ADVANCED": "", "ENABLED": "0", "SERVER": "", "PORT": "465", "SECURITY": "tls", "FROM_ADDRESS": "", "AUTH_METHOD": "login", "USERNAME": "", "PASSWORD": "", "TIMEOUT": "10000", "LOG_LEVEL": "3"}
```

### `snmp_agent`
Поля: ADVANCED, ENABLED, GENERAL, ID, LOG_LEVEL, OBJECTS, OBJECT_CAPACITY, PORT, READ_COMMUNITY, SYSCONTACT, SYSDESCR, SYSLOCATION, SYSNAME, SYSOBJECTID, SYSTEM, USERS, V3, V3_ENABLED, WRITE_COMMUNITY

```json
{"ID": "mrubrq7sd9emcmt1ad", "GENERAL": "", "SYSTEM": "", "V3": "", "ADVANCED": "", "ENABLED": "0", "PORT": "161", "READ_COMMUNITY": "public", "WRITE_COMMUNITY": "private", "OBJECTS": [], "SYSDESCR": "Tibbo Device", "SYSOBJECTID": "1.3.6.1.4.1.20738", "SYSCONTACT": "", "SYSNAME": "", "SYSLOCATION": "", "V3_ENABLED": "0", "USERS": [], "OBJECT_CAPACITY": "16", "LOG_LEVEL": "4"}
```

### `sntp`
Поля: DEBUGPRINT, ENABLED, ID, SNTP_SERVER

```json
{"ID": "mrubrq7shyohrudx4gn", "ENABLED": "1", "DEBUGPRINT": "0", "SNTP_SERVER": "216.239.35.0"}
```

### `sock`
Поля: ID

```json
{"ID": "mquecebjkw6smsjwht"}
```

### `socket`
Поля: ID, SOCKETS

```json
{"ID": "mrubrq7r5r28mns1ko8", "SOCKETS": []}
```

### `stg`
Поля: ENABLED, ID, REDUNDANCY, SETTINGS, STG_DEBUG_PRINT, STG_MAX_NUM_SETTINGS, STG_MAX_SETTING_NAME_LEN, STG_MAX_SETTING_VALUE_LEN, STG_RAM_ARRAY_SIZE, STG_TIMESTAMP, STORAGE

```json
{"ID": "mrubrq7mnv87nufrvr9", "ENABLED": "1", "STG_DEBUG_PRINT": "0", "STORAGE": "FLASH", "STG_TIMESTAMP": "0", "REDUNDANCY": "0", "STG_MAX_NUM_SETTINGS": "0", "STG_RAM_ARRAY_SIZE": "0", "STG_MAX_SETTING_NAME_LEN": "0", "STG_MAX_SETTING_VALUE_LEN": "0", "SETTINGS": [{"id": "stg_setting", "settings": {"ID": "mrubrsjqjgez7pq729s", "GENERAL": "", "ADVANCED": "", "SETTINGID": "T05BAUD", "NAME": "Tibbit 05 Baud Rate", "STORAGE": "E", "SETTINGTYPE": "string", "DATATYPE": "S", "MIN": 0, "MAX": 8, "INITIALIZE": "A", "DEFAULT": "9600"}}, {"id": "stg_setting", "settings": {"ID": "mrubrvavla7vxt2vpsf", " …
```

### `stgcmd_lib`
Поля: ID

```json
{"ID": "mrubwb787ck2o5caqji"}
```

### `tbl`
Поля: ENABLED, ID, STORAGE_PATH, TABLES, TBL_DEBUG_PRINT, WEBENABLED

```json
{"ID": "mrubrq7n41jcwl4pn2p", "ENABLED": "0", "TBL_DEBUG_PRINT": "0", "WEBENABLED": "1", "TABLES": [{"id": "tbl_table", "settings": {"ID": "mrubsnak9lbxidrcn1i", "NAME": "DEVICES", "COMMENT": "Devices", "IN_MEMORY": "0", "MAXRECORDS": "30", "STRUCT": "T", "KEYFIELDS": "0", "FIELDS": [{"id": "tbl_field", "settings": {"ID": "mrubt09hwwl4vkwcd2", "NAME": "DEVICE_ID", "DISPLAY_NAME": "Device ID", "FIELDTYPE": "F", "P1": "1", "P2": "255", "DEFAULT": "1", "ENUMS": []}}, {"id": "tbl_field", "settings": {"ID": "mrubtax1savs6lbcks", "NAME": "ADDRESS", "DISPLAY_NAME": "Address", "FIELDTYPE": "F", "P1":  …
```

### `tibbit_05`
Поля: BAUD, BITS, FLOWCONTROL, ID, MODE, NAME, PARITY, PLATFORM, RXBUF, SOCKET, TIBBIT, TXBUF

```json
{"ID": "mrubrlt15u4ollyy4vs", "SOCKET": "1", "TIBBIT": "05", "PLATFORM": "", "NAME": "T05_S1", "MODE": "RS485", "BAUD": "9600", "FLOWCONTROL": "0", "PARITY": "0", "BITS": "1", "TXBUF": "1", "RXBUF": "1"}
```

### `tibbit_18`
Поля: ID, PLATFORM, SOCKET, TIBBIT

```json
{"ID": "mrugtw45o0mlklquzjo", "SOCKET": "12", "TIBBIT": "18", "PLATFORM": ""}
```

### `tibbit_20`
Поля: ID, PLATFORM, SOCKET, TIBBIT

```json
{"ID": "mrucxiznr3yjiuzxun", "SOCKET": "2", "TIBBIT": "20", "PLATFORM": ""}
```

### `tibbit_33`
Поля: GENERAL, ID, PF, PLATFORM, SOCKET, TIBBIT

```json
{"ID": "mrugtu4kfx0wgt59t05", "SOCKET": "11", "TIBBIT": "33", "PLATFORM": "", "GENERAL": "", "PF": "1"}
```

### `time`
Поля: ID

```json
{"ID": "mquecebjj4h4tkoi25d"}
```

### `timers`
Поля: DEBUG_PRINT, ID, TIMERS

```json
{"ID": "mrubrq7hry0t2aiqgr", "DEBUG_PRINT": "0", "TIMERS": [{"id": "timer", "settings": {"ID": "mruc2iri7ojenvex90l", "TIMER_NAME": "poll_timer", "DESCRIPTION": ""}}, {"id": "timer", "settings": {"ID": "mrzoit3t39wbjoi03dh", "TIMER_NAME": "mqtt_publish_timer", "DESCRIPTION": ""}}]}
```

### `web_dashboard`
Поля: ADVANCED, CONSOLE_PREVIEW, CUSTOM_PAGES, CUSTOM_PAGES_EDITOR, CUSTOM_PAGES_JSON, CUSTOM_PAGES_REFRESH_INTERVAL, DASHBOARD_TITLE, ENABLED, GENERAL, GROUPS, ID, INTERVAL, PASSWORD, SETTINGS, SETTINGSENABLED, TABLES, TABLESENABLED, USER, USER_PASSWORD, USER_REGULAR, WEB_ADMIN_WIDGET_COLUMNS, WEB_ADMIN_WIDGET_ROWS, WIDGETENABLED, WIDGETS, WIDGET_GROUPS

```json
{"ID": "mrubrq7w5smh555khek", "GENERAL": "", "SETTINGS": "", "ADVANCED": "", "CUSTOM_PAGES": "", "ENABLED": "1", "TABLESENABLED": "1", "SETTINGSENABLED": "1", "WIDGETENABLED": "1", "INTERVAL": "1", "DASHBOARD_TITLE": "Modbus MQTT Gateway", "GROUPS": [{"id": "luis_group", "settings": {"ID": "mrzocamz6onj42hdm", "GROUPID": "webgroup2", "NAME": "General", "SETTINGS": [{"id": "luis_item", "settings": {"ID": "mrztvxo8z2skfzmlmy", "SETTINGID": "mrztvq72hd8zzwdfusm", "NAME": "Web Admin Password", "CONTROL": "EDIT", "OPTIONS": [{"id": "luis_item_option", "settings": {"ID": "mrztvxo84a76ch5xj2j", "LABE …
```

### `wifi`
Поля: DHCP, ENABLED, GATEWAY, ID, IP, MODE, NETMASK, WAP, WPW, WSEC

```json
{"ID": "mmetanrjo36fh2hwva", "ENABLED": "1", "MODE": "station", "DHCP": "1", "IP": "1.0.0.1", "NETMASK": "255.255.255.0", "GATEWAY": "1.0.0.1", "WAP": "", "WSEC": "7", "WPW": ""}
```

### `wireless_module`
Поля: ENABLED, ID, MODULE

```json
{"ID": "mmetamp5gir6yhhok2c", "ENABLED": "1", "MODULE": "WA2000C"}
```

### `wln`
Поля: ID

```json
{"ID": "mmeoc4cujlmu9rhvlyg"}
```


## Дополнение: узлы и порты из проектов-примеров appblocks.io (sprinkler5, accesscontrol6, pwmlights2, bp01, scheduler, luis, 4gswitchover, wifiswitchover)

| Тип | Входы | Выходы | ARGUMENTS | Свои поля |
|---|---|---|---|---|
| `node_time_interval` (On Time Period) | — | timer_tick | — | INTERVAL (с) |
| `node_cron_event` (Scheduler) | — | cron_expired | — | SCHEDULE (ID записи `crontab` в `cron.SCHEDULES`: NAME, PATTERN из 6 полей `* * * * * *`) |
| `node_variable_changed` | — | variable_changed | — | VARIABLE |
| `node_keypad` / `node_keypad_released` | — | on_kp | — | BUTTON (`LCD_KEYPAD_1…4` или линия Tibbit, напр. `exit_button_line_kp`) |
| `node_interrupt` | — | on_io_int | — | INTLINE (ID Tibbit с линией INT) |
| `node_wiegand` | — | data_available | — | TIBBIT (ID tibbit_08), FORMAT (`hex`) |
| `node_math_compound` (Custom Function) | set_value | math_done | — | VARIABLE, FUNCNAME, CODE |
| `node_log_add` | add_to_log | — | — | PAIRS (ключ/значение: Event, ID…) |
| `node_debug` | sys.debugprint | done | printstring | — |
| `node_pat` / `node_beep` | pat.play / beep.play | done | patternstring | CANINT (`PL_PAT_CANINT`), FREQ (beep) |
| `node_lcd_text_widget` | lcd_print_text | done | text | WIDGET, VISIBLE |
| `node_label` | — | — | — | комментарий на холсте |

Полный список типов блоков (из карты документации; порты смотри в экспорте/документации блока
`https://appblocks.io/docs/blocks/<тип>/`): node_arithmetic, node_azure, node_azure_command, node_azure_telemetry,
node_beep, node_bitwise, node_button, node_button_input_pressed, node_button_input_released, node_button_released,
node_cgg_telemetry, node_command_trigger, node_command_triggered, node_comparison, node_compound_condition,
node_cron_event, node_datetime, node_datetime_format, node_debug, node_digital_line_set, node_forloop,
node_http, node_http_server_endpoint, node_http_server_response, node_interrupt, node_ir_received, node_ir_send,
node_json_get_string, node_keypad, node_keypad_released, node_label, node_lcd_graph_widget, node_lcd_graph_widget_clear,
node_lcd_image_widget, node_lcd_menu, node_lcd_set_screen, node_lcd_snapshot, node_lcd_text_widget, node_log_add,
node_luis, node_math_compound, node_modbus_response, node_modbus_slave_register, node_modbus_timeout, node_modbus_write,
node_mqtt_change, node_mqtt_connected, node_mqtt_pub, node_mqtt_sub, node_network_changed, node_num_round,
node_number_to_fixed, node_pat, node_play_sound, node_random, node_ser_data_arrival, node_ser_data_send,
node_settings_init, node_sms_recv, node_sms_send, node_smtp_send, node_snmp_get_value, node_snmp_object_set,
node_snmp_send_trap, node_snmp_set_value, node_socket, node_socket_connect, node_socket_data_arrival, node_socket_event,
node_stop_sound, node_string_index_of, node_string_pad, node_string_replace, node_string_substring, node_string_trim,
node_switch, node_system, node_system_reboot, node_table, node_table_clear, node_table_delete, node_table_insert,
node_table_lookup_v2, node_table_row_count, node_table_update, node_table_update_v2, node_tibbit_26_end,
node_tibbit_26_send, node_tibbit_26_start, node_time_delay, node_time_interval, node_timer_completed, node_timer_start,
node_timer_stop, node_upgrade_firmware, node_variable_changed, node_variable_set, node_wiegand.

## Дополнение: поля Tibbit в проектах
| Feature | Поля (кроме ID, SOCKET, TIBBIT, PLATFORM) |
|---|---|
| `tibbit_05`, `tibbit_01`, `tibbit_02` | NAME, MODE (`RS485`…), BAUD (`9600` или `PL_SER_BAUD_38400`), FLOWCONTROL, PARITY, BITS, TXBUF, RXBUF |
| `tibbit_08` | NAME, MODE (`PL_SER_MODE_WIEGAND`), TXBUF, RXBUF |
| `tibbit_00_1` | NAME, L1NAME…L4NAME (имена = переменные), L1MODE…L4MODE, INTEDGE (`INT_EDGE_LOW`) |
| `tibbit_03_1` | NAME, L1NAME, L2NAME (реле → Boolean-переменные) |
| `tibbit_16` | NAME, USESSI, PIC_CLOCK_SPEED, FREQUENCY, L1NAME…L3NAME |
| `tibbit_33` | PF ("1" — следить за -PF), GENERAL |
| `tibbit_10`, `tibbit_18`, `tibbit_20`, `tibbit_21`, `tibbit_45_2` | только сокет |
Типичная пара питания на TPP2 в примерах Tibbo: `tibbit_10` или `tibbit_33` в SOCKET 11 + `tibbit_18` в SOCKET 12.

## Дополнение: структуры списков
- `modbus_master.MODBUSDEVICES[]` → settings `ID, NAME, PROTOCOL, SERIAL_PORT (ID Tibbit), DEVICEID, DEVICEIP, DEVICEPORT, REGISTERS[]`;
  `REGISTERS[]` → `ID, ADDRESS, LENGTH, DATATYPE, VARTYPE, NAME` (регистры становятся переменными, `{{$<ID регистра>}}`).
- `luis.GROUPS[]` (`luis_group`: GROUPID, NAME, SETTINGS[] → `luis_item`: SETTINGID, NAME, CONTROL `STATIC|IPCTRL|EDIT…`, OPTIONS[], VALIDATION, STATUS).
- `general` в tios-проектах ещё: LEDPAT, INTERFACE_SWITCHING, DEFAULT_INTERFACE, BEEPFREQUENCY, TIME_FORMAT.
