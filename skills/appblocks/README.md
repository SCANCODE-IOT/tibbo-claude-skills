# appblocks

**English** · [Русский](README.ru.md) · [← All skills](../../README.md)

A Claude skill for **[Tibbo AppBlocks](https://appblocks.io)** - the visual firmware builder for Tibbo and Zephyr devices
and its cloud. Claude reads, explains, reviews, edits and generates AppBlocks projects, draws their logic and hardware,
and works with the AppBlocks Cloud API.

<img src="../../docs/images/appblocks-flow.svg" alt="AppBlocks logic flow" width="900" />

> Install together with [tibbo-firmware](../tibbo-firmware/): hardware checks and review of generated Tibbo BASIC code go through it.

## What it does

| Task | How the skill handles it |
|---|---|
| **Explain a project** | `ab_tool.py summary` - board, Tibbits, services, variables, tables and event chains, then a plain-language description of what the device does. |
| **Review logic** | Applies the AppBlocks flow rules: a flow must start from an event, parameters reach only the next block, ASYNC blocks drop parameters, `On Variable Changed` recursion, command loops without exit, unhandled `modbus_timeout` / `tbl_record_not_found`, passwords in plain text, disabled features that nodes need. |
| **Review hardware** | Converts the project's Tibbits to a TPS configuration (`ab_tool.py tps`) and runs `tps_check.py` from `tibbo-firmware` - sockets, lines, power budget, board picture. |
| **Edit or generate** | Edits a *copy* of the export with a script, never by hand; keeps IDs of reused elements and removes unused ones together with every reference (including dashboards, LUIS, LCD menus); new IDs from `ab_tool.py ids`; `check` must report 0 errors before the file is handed back for **Import**. |
| **Work with the cloud** | Lists projects and devices, downloads projects, generates firmware code, reads versions and workspaces. Any write - create/update projects, device variables, commands, **OTA**, workflows - happens only after your explicit "yes" to that exact call. |
| **Use the editor** | In your browser, under your sign-in, read-first; Run, Deploy, OTA, save and delete only after confirmation. |

Runtimes covered: **`tios`** (Tibbo BASIC for TPP2, TPP3, DS1101, DS1102, EM510), **`zephyr`** (Zephyr C), `micropython`.

## Contents

| Path | What is inside |
|---|---|
| `SKILL.md` | Instructions Claude follows: where to get the project, review, editing, cloud write rules, browser, visualisation. |
| `references/editor.md` | Editor structure (Hardware / Features / Application), Import/Export, Run/Debug/Release, runtimes, **flow rules**, variables, plugins, common mistakes. |
| `references/format.md` | The exported JSON format: top level, feature groups, nodes, links, `{{$…}}` references, editing rules. |
| `references/catalog.md` | Node types, ports and fields, Tibbit fields, Modbus and LUIS structures. |
| `references/catalog-examples.md` | Ports, fields and sockets collected from **78 appblocks.io projects** (59 node types, 28 Tibbits). |
| `references/generated-code.md` | What AppBlocks generates for `tios`: TIDE project files, `var_X_*` procedures, code insertion markers. |
| `references/api.md` | AppBlocks Cloud API: authentication, projects (code, build, versions, OTA, bundles), devices, groups, workspaces, workflows, dashboards. |
| `scripts/ab_tool.py` | Offline project tool (see below). |
| `scripts/ab_api.py` | Cloud API client (see below). |
| `examples/` | 6 Tibbo projects: Modbus gateway with LCD on 4×RS485 and Modbus→MQTT gateway (Zephyr), sprinkler, access control, hydroponics (TPP3), water level control with cloud. |
| `tests/run.sh` | Offline tests on the examples, including the bridge to `tps_check.py`. |

## Tools

Both scripts use only the Python standard library.

### `ab_tool.py` - offline, no account needed

```bash
python3 scripts/ab_tool.py summary project.json              # what is in the project
python3 scripts/ab_tool.py check   project.json              # broken links and references, duplicate IDs, socket conflicts (exit 1 on errors)
python3 scripts/ab_tool.py flow    project.json flow.svg     # logic diagram
python3 scripts/ab_tool.py tps     project.json --vin 24 --out cfg.json   # hardware → tps_check.py config
python3 scripts/ab_tool.py nodes   project.json              # node types and ports used
python3 scripts/ab_tool.py ids     5                         # new IDs in AppBlocks style
```

Full hardware check with the board picture:

```bash
python3 scripts/ab_tool.py tps project.json --vin 24 --out cfg.json
python3 ../tibbo-firmware/scripts/tps_check.py check cfg.json --svg board.svg
```

The supply voltage is not stored in an AppBlocks project; pass it with `--vin`. If you don't tell Claude the voltage, it assumes 24 V and says so in the answer.

### `ab_api.py` - AppBlocks Cloud

```bash
export APPBLOCKS_API_KEY=abk_...        # Settings → API Keys in the AppBlocks web app
python3 scripts/ab_api.py me                           # account and key scopes
python3 scripts/ab_api.py projects                     # list projects
python3 scripts/ab_api.py project <id> --out p.json    # download a project
python3 scripts/ab_api.py code p.json --outdir gen     # generated firmware sources
python3 scripts/ab_api.py devices                      # devices, connection, firmware
python3 scripts/ab_api.py example sprinkler5 --out p.json
```

| Command group | Commands | Changes your account? |
|---|---|---|
| Read | `me`, `projects`, `project`, `versions`, `examples`, `example`, `workspaces`, `devices`, `device`, `get` | No |
| Generate | `code` | No - sends the project to the code generator only |
| Write | `create … --yes`, `update … --yes` | **Yes** - Claude asks first, every time |

Security:

- The key is read **only** from `APPBLOCKS_API_KEY` or a file named in `APPBLOCKS_API_KEY_FILE` - never from the command line. Claude never prints it or saves it to files, memory or artifacts; the device MQTT `key` is hidden as well.
- In the claude.ai sandbox the network is closed by default: add `api.appblocks.io` and `appblocks.io` to allowed domains in **Settings → Capabilities** (on Team/Enterprise - ask your admin). Without that, use an exported `.json` file.

## Example prompts

```text
Here is my AppBlocks export. What does this device do? Draw the logic and the board.
```

```text
Check this project for problems before I deploy it to 30 controllers.
```

```text
Take the sprinkler5 example and make it 6 zones with a separate schedule table per zone.
```

```text
Show my AppBlocks devices that are offline and which firmware version they run.
```

## Limits

- The JSON format and node catalog were reconstructed from exported projects (October 2026). A new node type may be missing; Claude then copies the shape from a similar node in your projects and asks you to check the editor's **Problems** tab.
- `ab_api.py code` succeeding does not guarantee that the editor's Problems list is empty - the skill asks you to open the project and send any new errors, which are then added to `check`.
- A device left in **Debug** mode stops without a connection to the editor - the skill warns not to leave it that way on site.

## Tests

```bash
sh tests/run.sh
```

`check`, `summary`, `flow` and `tps` on every example, ID uniqueness, regressions for dashboard references and the
update interval, and the bridge to `tps_check.py` when `tibbo-firmware` sits next to this folder.
