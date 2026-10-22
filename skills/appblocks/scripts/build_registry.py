#!/usr/bin/env python3
"""Build data/registry.json and references/blocks.md + references/features.md from a raw AppBlocks editor dump.

The raw dump is made in the browser on app.appblocks.io with scripts/extract_registry.js (see its header).
Usage:
    python3 scripts/build_registry.py appblocks_defs.json
Writes (relative to the skill folder):
    data/registry.json        compact machine-readable registry, used by ab_tool.py check / lookup
    references/blocks.md      all logic blocks by palette category: ports, parameters, settings
    references/features.md    features (services), nested items, LCD/dashboard widgets, peripherals, Tibbit settings
Standard library only.
"""
import json
import os
import re
import sys


def utf8_stdio():
    """Print UTF-8 whatever the console code page is (Windows cp1251/cp1252, pipes in Git Bash)."""
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
COMMON = {"ID", "DISPLAY_NAME", "FEATURE", "X", "Y", "INPUTS", "OUTPUTS", "GROUP", "ARGUMENTS"}
RUNTIMES = ("tios", "zephyr", "micropython")

# Ports that the editor adds at run time (getPortDeclaration / getOutputs) and the static dump does not show.
EXTRA_PORTS = {
    "node_table": {"out": {"tbl_record_found": ["row_index:word", "<поля таблицы>"], "tbl_record_not_found": []}},
    "node_table_lookup_v2": {"out": {"tbl_record_found": ["row_index:word", "<поля таблицы>"], "tbl_record_not_found": []}},
    "node_modbus_response": {"out": {"response": ["<параметры регистра>"]}},
}
# Blocks whose ports are defined by the project itself (custom code, groups, switch cases): ports are not checked.
DYNAMIC_PORTS = {"node_custom", "node_group", "node_group_input", "node_group_output", "node_switch", "node_math_compound"}


def parse_palette(src):
    if not src:
        return []
    js = re.sub(r'([{,])(name|nodes):', r'\1"\2":', src)
    return json.loads(js)


def port_list(ports):
    out = {}
    for p in ports or []:
        params = []
        for q in p.get("p") or []:
            if isinstance(q, str):
                params.append(q)
            else:
                params.append(f"{q.get('id') or q.get('n')}:{q.get('t')}" if q.get("t") else str(q.get("id") or q.get("n")))
        out[p["id"]] = params
    return out


def settings(sets, keep_common=False):
    out = {}
    for s in sets or []:
        if not keep_common and s["id"] in COMMON:
            continue
        r = {"t": s.get("t")}
        if s.get("n") and s.get("n") != s["id"]:
            r["name"] = s["n"]
        if s.get("refId"):
            r["ref"] = s["refId"]
        if s.get("default") not in (None, "", []):
            r["d"] = s["default"]
        if s.get("o"):
            r["o"] = [o["v"] if isinstance(o, dict) else o for o in s["o"]]
            names = {str(o["v"]): o.get("n") for o in s["o"] if isinstance(o, dict) and o.get("n") not in (None, o.get("v"))}
            if names:
                r["on"] = names
        for k in ("min", "max", "required", "readonly"):
            if s.get(k) not in (None, False, ""):
                r[k] = s[k]
        out[s["id"]] = r
    return out


def entry(e, kind):
    """Compact one registry entry; keeps per-runtime differences."""
    base = e.get("tios") or next((v for v in e.values() if v), None)
    if not base or "err" in base:
        return None
    r = {"name": base.get("name")}
    for k, short in (("linkedFeature", "feat"), ("isAsync", "async"), ("singleInstance", "single"), ("featureType", "type")):
        if base.get(k) not in (None, "", False):
            r[short] = base[k]
    for k in ("devices", "unsupportedDevices", "requirements", "capabilities"):
        v = base.get(k)
        if v:
            r[k] = v
    if "in" in base or "out" in base:
        r["in"] = port_list(base.get("in"))
        r["out"] = port_list(base.get("out"))
    r["set"] = settings(base.get("set"), keep_common=(kind != "nodes"))
    for rt in ("zephyr", "micropython"):
        if rt in e and e[rt] and "err" not in e[rt]:
            diff = {}
            if port_list(e[rt].get("in")) != r.get("in") and "in" in r:
                diff["in"] = port_list(e[rt].get("in"))
            if port_list(e[rt].get("out")) != r.get("out") and "out" in r:
                diff["out"] = port_list(e[rt].get("out"))
            s2 = settings(e[rt].get("set"), keep_common=(kind != "nodes"))
            if s2 != r["set"]:
                diff["set"] = s2
            if diff:
                r.setdefault("rt", {})[rt] = diff
    return r


def fmt_ports(d):
    if not d:
        return "-"
    return ", ".join(f"`{k}`" + (f"({', '.join(v)})" if v else "") for k, v in d.items())


def fmt_set(d, skip=()):
    parts = []
    for k, v in d.items():
        if k in skip or v.get("t") in ("hidden", "group"):
            continue
        s = f"`{k}`"
        if v.get("ref"):
            s += f"→{v['ref']}"
        elif v.get("t") and v["t"] not in ("string", "option"):
            s += f" {v['t']}"
        if v.get("o"):
            vals = []
            for o in v["o"][:24]:
                nm = (v.get("on") or {}).get(str(o))
                vals.append(f"{o}={nm}" if nm else str(o))
            s += " [" + "\\|".join(vals) + ("\\|…" if len(v["o"]) > 24 else "") + "]"
        if "d" in v and not isinstance(v["d"], (list, dict)) and str(v["d"]) != "" and not str(v["d"]).startswith(("[", "{")):
            s += f" ={str(v['d'])[:30]}"
        if v.get("min") is not None or v.get("max") is not None:
            s += f" ({v.get('min', '')}..{v.get('max', '')})"
        parts.append(s)
    return "; ".join(parts) or "-"


def esc(s):
    return str(s).replace("|", "\\|")


def main():
    raw = json.load(open(sys.argv[1], encoding="utf-8"))
    dump = raw["dump"]
    palette = parse_palette(raw.get("paletteSrc"))
    reg = {"source": "app.appblocks.io editor registry", "snapshot": raw.get("snapshot", "2026-10-22"), "palette": palette}
    for kind, items in dump.items():
        reg[kind] = {}
        for k, e in items.items():
            c = entry(e, kind)
            if c:
                reg[kind][k] = c
    cat = {}
    hidden = set()
    for c in palette:
        for n in c["nodes"]:
            if c["name"] == "Hidden":
                hidden.add(n)
            else:
                cat.setdefault(n, c["name"])
    for k, v in reg["nodes"].items():
        v["cat"] = cat.get(k, "Hidden")
        if k in EXTRA_PORTS:
            for side, ports in EXTRA_PORTS[k].items():
                v.setdefault(side, {}).update(ports)
        if k in DYNAMIC_PORTS:
            v["dynamic_ports"] = True
    os.makedirs(os.path.join(SKILL, "data"), exist_ok=True)
    with open(os.path.join(SKILL, "data", "registry.json"), "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, separators=(",", ":"), sort_keys=True)

    # ---------------- blocks.md
    n_vis = sum(1 for v in reg["nodes"].values() if v["cat"] != "Hidden")
    L = [f"# Блоки логики AppBlocks: порты, параметры, настройки",
         "",
         f"Снято из реестра редактора app.appblocks.io ({reg['snapshot']}): {len(reg['nodes'])} типов блоков, "
         f"из них {n_vis} в палитре и {len(reg['nodes']) - n_vis} скрытых (служебные и устаревшие, встречаются в старых проектах).",
         "Машинная версия - `data/registry.json` (её использует `ab_tool.py check` и `ab_tool.py lookup`). Пересборка: "
         "`scripts/extract_registry.js` в браузере на app.appblocks.io, затем `scripts/build_registry.py`.",
         "",
         "Как читать: **Входы/Выходы** - `portId` для `node_link` (SOURCE_PORT/TARGET_PORT) и параметры, которые порт передаёт "
         "следующему блоку (`{{$имя}}`) или принимает в ARGUMENTS (TARGETPARAM). **Настройки** - поля `settings` узла: "
         "`ID`→ref - ID элемента этого типа (variable, timer, tbl_table…), [варианты] - допустимые значения (`значение=подпись`), "
         "=… - значение по умолчанию. Общие поля (ID, DISPLAY_NAME, X, Y, GROUP, INPUTS, OUTPUTS, ARGUMENTS) не повторяются. "
         "**ASYNC** - после блока параметры предыдущих блоков недоступны (editor.md §4). "
         "Feature - сервис, который должен быть включён в проекте.",
         ""]
    order = [c["name"] for c in palette if c["name"] != "Hidden"] + ["Hidden"]
    for c in order:
        ids = [k for k, v in reg["nodes"].items() if v["cat"] == c]
        if c != "Hidden":
            pal = next(p["nodes"] for p in palette if p["name"] == c)
            ids = [k for k in dict.fromkeys(pal) if k in reg["nodes"]]
        if not ids:
            continue
        title = c if c != "Hidden" else "Скрытые и служебные (нет в палитре)"
        L += [f"## {title}", "", "| Блок | Название | Входы | Выходы | Настройки | Feature | Особенности |", "|---|---|---|---|---|---|---|"]
        for k in ids:
            v = reg["nodes"][k]
            notes = []
            if v.get("async"):
                notes.append("ASYNC")
            if v.get("devices"):
                notes.append("только " + ", ".join(v["devices"]))
            if v.get("unsupportedDevices"):
                notes.append("не для " + ", ".join(v["unsupportedDevices"]))
            if v.get("dynamic_ports"):
                notes.append("порты задаёт проект")
            for rt, diff in (v.get("rt") or {}).items():
                for side in ("in", "out"):
                    if side in diff:
                        notes.append(f"{rt}: {'входы' if side == 'in' else 'выходы'} {fmt_ports(diff[side])}")
            feat = v.get("feat", "")
            L.append(f"| `{k}` | {esc(v['name'])} | {fmt_ports(v.get('in'))} | {fmt_ports(v.get('out'))} | {fmt_set(v['set'])} | "
                     f"{'' if feat == 'general' else feat} | {'; '.join(notes)} |")
        L.append("")
    open(os.path.join(SKILL, "references", "blocks.md"), "w", encoding="utf-8").write("\n".join(L))

    # ---------------- features.md
    F = ["# Feature, сервисы, элементы, виджеты и периферия AppBlocks",
         "",
         f"Снято из реестра редактора app.appblocks.io ({reg['snapshot']}). Машинная версия - `data/registry.json`.",
         "Значения - как в экспорте JSON (`settings`). [варианты] - допустимые значения (`значение=подпись`), =… - по умолчанию, "
         "(min..max) - пределы, `ref` - ID элемента этого типа. Скрытые поля (hidden) редактор заполняет сам и здесь не показаны.",
         ""]
    sections = [("features", "Feature проекта (шаг Features)"), ("libraries", "Сервисы-библиотеки (stg, tbl, mqtt, modbus…)"),
                ("items", "Вложенные элементы (variable, timer, tbl_table, stg_setting, command…)"),
                ("tibbits", "Tibbit: поля feature `tibbit_NN`"), ("peripherals", "Периферия (GPIO, UART, датчики, дисплеи)"),
                ("widgets", "Виджеты LCD и веб-дашборда")]
    skip = {"ID", "SOCKET", "TIBBIT", "PLATFORM"}
    for kind, title in sections:
        items = reg.get(kind) or {}
        F += [f"## {title}", "", "| id | Название | Настройки | Особенности |", "|---|---|---|---|"]
        for k in sorted(items):
            v = items[k]
            notes = []
            if v.get("single") is False and kind in ("features", "libraries"):
                notes.append("несколько экземпляров")
            if v.get("devices"):
                notes.append("только " + ", ".join(map(str, v["devices"]))[:120])
            if v.get("unsupportedDevices"):
                notes.append("не для " + ", ".join(map(str, v["unsupportedDevices"]))[:120])
            if v.get("capabilities"):
                notes.append("даёт: " + ", ".join(map(str, v["capabilities"])))
            for rt, diff in (v.get("rt") or {}).items():
                notes.append(f"{rt}: свои настройки")
            F.append(f"| `{k}` | {esc(v['name'])} | {fmt_set(v['set'], skip)} | {'; '.join(notes)} |")
        F.append("")
    open(os.path.join(SKILL, "references", "features.md"), "w", encoding="utf-8").write("\n".join(F))
    print("registry:", {k: len(v) for k, v in reg.items() if isinstance(v, dict)},
          "blocks.md", sum(1 for _ in L), "lines; features.md", len(F), "lines")


if __name__ == "__main__":
    utf8_stdio()
    main()
