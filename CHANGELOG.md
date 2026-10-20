# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versions follow [Semantic Versioning](https://semver.org/).

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

[1.0.0]: https://github.com/scancode-iot/tibbo-claude-skills/releases/tag/v1.0.0
