# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versions follow [Semantic Versioning](https://semver.org/).

## [1.1.1] - 2026-10-22

Hotfix after user reports: scripts on Windows, and AppBlocks code generation facts checked against `POST /api/projects/code`.

### Fixed
- **Windows console encoding.** Every script (`ab_tool.py`, `ab_api.py`, `build_registry.py`, `tps_check.py`, `state_diagram.py`,
  `build_data.py`) now prints UTF-8 regardless of the console code page, so cp1251/cp1252 consoles no longer stop them with
  `UnicodeEncodeError` (for example `ab_tool.py lookup node_math_compound`). All files are opened with an explicit `encoding="utf-8"`.
- **`CERTIFICATE_VERIFY_FAILED` in `ab_api.py`.** HTTPS uses `SSL_CERT_FILE` / `SSL_CERT_DIR` if set, otherwise `truststore`
  (the OS store) or `certifi` when installed, otherwise Python's default. Verification is never disabled. A failed check now
  prints what to do on Windows instead of the sandbox hint; new `ab_api.py tls` shows the store in use and tests the connection.

### Added
- `ab_tool.py check`: error when Digital Line Set `LINE_NUMBER` is not a number (`PL_IO_NUM_48` is written into the code as a string);
  warning when the line is not made an output by the framework; error for comparison operators other than `=` `<>` `<` `<=` `>` `>=`
  on `tios` (`==` and `!=` go into Tibbo BASIC as is).
- `generated-code.md`: Digital Line Set, IF Condition, Custom Function, On Time Period (fires every N+1 ticks: 0.5 s is 0.51 s),
  `LEDPAT` (adds a red error pattern on Settings library init failures, no effect without Settings), the TPP signal strength bar
  driver (`signal_strength_set`). Each fact is marked: checked by generation, not checked in the editor, TIDE or on hardware.
- `editor.md` §8: driving the TPP signal strength bar from logic; `SKILL.md`: `tbt22` as a minimal base for a new tios project.
- tibbo-firmware `tios-api.md`: `pat.playlb` exists only on LTPP3(G2); on TiOS boards the bar is driven by the application.
- `ab_tool.one_id()`; `new_id()` docstring says it always returns a list.
- README and both `SKILL.md`: running the scripts on Windows.
- Tests run without `PYTHONUTF8` on a cp1251 console; CI on `windows-latest` (Python 3.12, 3.14) and an HTTPS check from Windows
  with `truststore` and `certifi`.

## [1.1.0] - 2026-10-22

Skills retrained on the AppBlocks editor itself (app.appblocks.io) and on the full docs.tibbo.com sources (2,325 pages, received from Tibbo on 2026-10-21).

### appblocks
- **Added** `references/blocks.md`: all 168 editor blocks (was 59 seen in examples) by palette category - ports with parameters, settings with allowed values and defaults, required feature, ASYNC; 45 hidden/legacy blocks listed separately.
- **Added** `references/features.md`: 30 features, 32 service libraries, 41 nested item types, 66 `tibbit_NN` field sets, 29 peripherals, 30 LCD / web console widgets.
- **Added** `data/registry.json` with `scripts/build_registry.py` and `scripts/extract_registry.js` (read-only browser extractor) to refresh it when AppBlocks changes.
- **Added** `ab_tool.py lookup <block|feature|word>`.
- **Changed** `ab_tool.py check` now also reports: unknown block type, link to a port the block does not have, setting value outside the allowed list, block whose feature is missing (or disabled), blocks no longer in the palette, blocks/features unavailable on the project's board. No false positives on the 78 appblocks.io projects and 5 real user projects.
- **Added** plugin format (`custom_feature`: settings, code blocks with `{{feature.settings.*}}` / `{{block.output}}`, variables) to `format.md` §5, based on the three marketplace plugins.
- **Added** to `editor.md`: how the editor validates Tibbit placement (§9), the editor's built-in AI assistant and text project view (§10), the plugin marketplace.
- **Changed** `SKILL.md`: new references, review rule for legacy blocks, how to refresh the registry.

### tibbo-firmware
- **Added** `references/docs-map.md`: topic → docs.tibbo.com page and its Russian translation on tibbo.ru/kb (objects, syscalls, libraries, platforms, TPS, all Tibbits, Monitor/Loader, Linux).
- **Changed** Tibbit catalog checked against 76 `tibbit_NN` pages: 84 Tibbits (added #47, #51, #56, all deprecated); #02 and #44 need an interrupt line for RTS/CTS; mating connectors for #09/#10/#16/#17/#23/#25/#33 per docs.
- **Fixed** #13/#14 own +5V consumption is 10/20 mA; the former 66/56 mA already included the #12 share, so the power budget counted it twice.
- **Changed** `tios-api.md`: defaults and notes from docs (watchdog, `sys.timercountms`, `net.gatewayip`, `stor.base`/`stor.size`, `wln.dhcp`/`autoconnect`, `kp.repeatdelay`, `ssi.baudrate` is writable, deprecated PPPoE and WS1102 properties).
- **Added** `platforms.md`: platform parameters table (16/32-bit, clock, RAM, EEPROM, UART FIFO, debugging, dual apps), docs vs .tph constant names, LTPP3(G2) line map.
- **Added** `project-and-libs.md` §9: facts for code and review - 16-bit arithmetic, `doevents` rules, VM exceptions in release builds, EEPROM/flash wear, Monitor/Loader and MD button, WM2000/WS1102 DCB and dual apps, DS110x port modes, LTPP3(G2).
- **Changed** `power.md`, `libraries.md`, `SKILL.md` (16-bit arithmetic, release exceptions, EEPROM service area is usually 28 bytes, not 8).
- **Added** `tps_check.py` rules from the AppBlocks editor: WA2000U needs RF connector #37; hints to use one #20 instead of #21 for double-width modules or two #21 in one tile.

### Repository
- Version 1.1.0 in the plugin catalog; counts updated in README files.

## [1.0.0] - 2026-10-20

First public release.

### tibbo-firmware
- TiOS API reference, 46 platforms with `PL_IO_NUM_*` mapping, Tibbo libraries, 81-Tibbit catalog (snapshot of October 2026).
- Writing, review checklist (34 items) and symptom-based debugging for Tibbo BASIC / Tibbo C.
- `tps_check.py`: TPS socket, line, UART/INT, connector, PoE and +5 V power budget checks; board SVG in the Tibbo configurator style; `find`, `board`, `tibbit` commands.
- `state_diagram.py`: state diagrams for firmware built as a state machine.

### appblocks
- AppBlocks editor, export format, node catalog (78 projects, 59 node types, 28 Tibbits), generated code and Cloud API references.
- `ab_tool.py`: `summary`, `check`, `flow`, `tps`, `nodes`, `ids`.
- `ab_api.py`: AppBlocks Cloud client; writes only with explicit confirmation.
- 6 example projects; AppBlocks Cloud device credentials removed from the published examples.

### Repository
- Claude Code plugin catalog (`/plugin marketplace add scancode-iot/tibbo-claude-skills`).
- Upload-ready packages for Claude apps and the API (`tools/package.sh`, attached to releases).
- Offline tests on every push.

[1.1.1]: https://github.com/scancode-iot/tibbo-claude-skills/releases/tag/v1.1.1
[1.1.0]: https://github.com/scancode-iot/tibbo-claude-skills/releases/tag/v1.1.0
[1.0.0]: https://github.com/scancode-iot/tibbo-claude-skills/releases/tag/v1.0.0
