#!/usr/bin/env python3
"""AppBlocks project (exported JSON) tool.

  python3 ab_tool.py summary  project.json            # what is in the project: board, Tibbits, services, data, flows
  python3 ab_tool.py check    project.json            # structural checks (links, references, IDs, sockets) -> exit 1 on errors
  python3 ab_tool.py tps      project.json [--vin 24] [--out cfg.json]  # hardware -> cfg for tibbo-firmware tps_check.py
  python3 ab_tool.py flow     project.json out.svg    # flow (logic) diagram from node_* positions, links and groups
  python3 ab_tool.py ids      [N]                     # new IDs in AppBlocks style
  python3 ab_tool.py nodes    project.json            # catalogue of node types/ports used in this project

The format is documented in references/format.md (derived from projects exported by AppBlocks).
"""
import json, re, sys, time, random, string, collections, os

REF = re.compile(r"\{\{\$([A-Za-z0-9_]+)\}\}")
NODE_PREFIX = "node_"
SERVICE_TOGGLES = ["net", "wifi", "dhcp", "dns", "sntp", "http", "httpserver", "mqtt", "cgg", "cell", "bt",
                   "modbus_master", "modbus_slave", "snmp_agent", "smtp_client", "web_dashboard", "luis", "lcd",
                   "lcd_graph", "tbl", "stg", "fd", "log", "ds_man", "mbedtls"]


def load(path):
    d = json.load(open(path, encoding="utf-8"))
    if isinstance(d, dict) and "data" in d and isinstance(d["data"], list) and d["data"]:
        d = d["data"][0]          # API envelope {count, data:[project]}
    if isinstance(d, dict) and "project" in d and "features" not in d:
        d = d["project"]          # example envelope
    if not isinstance(d, dict) or "features" not in d:
        raise SystemExit(f"{path}: not an AppBlocks project export (no 'features')")
    if isinstance(d.get("device"), dict):   # API form {platform, name}
        d["device"] = d["device"].get("platform") or d["device"].get("name")
    return d


def new_id(n=1):
    """AppBlocks-style id: Date.now() in base36 + random base36 tail (observed 16-20 chars)."""
    out = []
    for _ in range(n):
        ts = int(time.time() * 1000)
        b36 = ""
        while ts:
            ts, r = divmod(ts, 36)
            b36 = (string.digits + string.ascii_lowercase)[r] + b36
        tail = "".join(random.choice(string.digits + string.ascii_lowercase) for _ in range(10))
        out.append(b36 + tail)
        time.sleep(0.002)
    return out


def all_ids(obj, acc=None, parent=None):
    """Every nested {"id": kind, "settings": {"ID": ...}} -> {ID: (kind, settings)}."""
    if acc is None:
        acc = {}
    if isinstance(obj, dict):
        if "settings" in obj and isinstance(obj["settings"], dict) and "ID" in obj["settings"]:
            acc.setdefault(obj["settings"]["ID"], (obj.get("id"), obj["settings"]))
        for v in obj.values():
            all_ids(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            all_ids(v, acc)
    return acc


def label(f, ids):
    s = f["settings"]
    kind = f["id"]
    name = s.get("DISPLAY_NAME") or ""
    k = kind[len(NODE_PREFIX):] if kind.startswith(NODE_PREFIX) else kind
    extra = ""
    for key, src in (("VARIABLE", "VARNAME"), ("TIMER", "TIMER_NAME"), ("COMMAND", "NAME"), ("TABLE", "NAME"),
                     ("SOCKET", "NAME"), ("WIDGET", "NAME")):
        if s.get(key) and s[key] in ids:
            extra = ids[s[key]][1].get(src) or ""
    if kind == "node_modbus_write":
        extra = f"{s.get('PROTOCOL', '')} {s.get('FUNCTIONCODE', '')}"
    if kind == "node_comparison":
        a = {x["settings"]["TARGETPARAM"]: x["settings"]["ARGVALUE"] for x in s.get("ARGUMENTS", [])}
        extra = f"{a.get('operand1', '')} {a.get('operator', '')} {a.get('operand2', '')}"
    if kind == "node_time_delay":
        extra = f"{s.get('DURATION')} s"
    if kind == "node_network_changed":
        extra = f"type {s.get('NETWORK_TYPE')} event {s.get('NETWORK_EVENT')}"
    if kind == "node_socket_event":
        extra = (extra + " " + s.get("EVENT_TYPE", "")).strip()
    return (name or k), extra


def port_name(p, ids):
    x = ids.get(p)
    if x and x[0] == "node_switch_case":
        return f"case {x[1].get('VALUE')}"
    return p


def pretty_ref(text, ids):
    def rep(m):
        x = ids.get(m.group(1))
        if not x:
            return "{" + m.group(1) + "}"
        s = x[1]
        return "{" + (s.get("VARNAME") or s.get("SETTINGID") or s.get("NAME") or s.get("TIMER_NAME") or m.group(1)) + "}"
    return REF.sub(rep, str(text))


# ------------------------------------------------------------------ summary
def summary(d):
    F = d["features"]
    ids = all_ids(d)
    by = collections.defaultdict(list)
    for f in F:
        by[f["id"]].append(f["settings"])
    print(f"Проект: {d.get('name')}  (id {d.get('id')})")
    print(f"Плата: {d.get('device')}   runtime: {d.get('runtime')}   версия формата/проекта: {d.get('version')}")
    if d.get("description"):
        print("Описание:", d["description"][:300])
    bs = (by.get("boardsetting") or [{}])[0]
    if bs:
        print(f"Сборка: PoE={bs.get('POE')} 5VDIRECT={bs.get('5VDIRECT')} TPB={bs.get('TPB')} DIN={bs.get('DIN')} "
              f"адаптер={bs.get('POWERADAPTER')} ASM={bs.get('ASM')}")
    tib = sorted([s for k, v in by.items() if k.startswith("tibbit_") for s in v], key=lambda s: int(s.get("SOCKET") or 0))
    print("\nTibbit:")
    for s in tib:
        extra = {k: v for k, v in s.items() if k not in ("ID", "SOCKET", "TIBBIT", "PLATFORM", "GENERAL")}
        print(f"  S{s.get('SOCKET'):<3} #{s.get('TIBBIT'):<5} {json.dumps(extra, ensure_ascii=False) if extra else ''}")
    wm = by.get("wireless_module")
    if wm:
        print(f"  Wi-Fi модуль: {wm[0].get('MODULE')} (enabled={wm[0].get('ENABLED')})")
    print("\nСервисы (ENABLED=1):", ", ".join(k for k in SERVICE_TOGGLES if by.get(k) and str(by[k][0].get("ENABLED", "1")) == "1"))
    print("Выключены:", ", ".join(k for k in SERVICE_TOGGLES if by.get(k) and str(by[k][0].get("ENABLED", "1")) == "0"))
    net = (by.get("net") or [{}])[0]
    if net:
        print(f"Ethernet: DHCP={net.get('DHCP')} IP={net.get('IP')} NM={net.get('NM')} GW={net.get('GI')}")
    gv = (by.get("global_vars") or [{}])[0].get("VARS", [])
    print(f"\nПеременные ({len(gv)}): " + ", ".join(f"{v['settings']['VARNAME']}:{v['settings']['DATATYPE']}" for v in gv))
    tm = (by.get("timers") or [{}])[0].get("TIMERS", [])
    print(f"Таймеры ({len(tm)}): " + ", ".join(t["settings"]["TIMER_NAME"] for t in tm))
    cm = (by.get("commands") or [{}])[0].get("COMMANDS", [])
    print(f"Команды ({len(cm)}): " + ", ".join(c["settings"]["NAME"] for c in cm))
    st = (by.get("stg") or [{}])[0].get("SETTINGS", [])
    print(f"Настройки STG ({len(st)}): " + ", ".join(f"{x['settings']['SETTINGID']}={x['settings'].get('DEFAULT')}" for x in st))
    tb = (by.get("tbl") or [{}])[0].get("TABLES", [])
    for t in tb:
        s = t["settings"]
        print(f"Таблица {s['NAME']} (max {s.get('MAXRECORDS')}): " + ", ".join(f["settings"]["NAME"] for f in s.get("FIELDS", [])))
    cf = (by.get("custom_features") or [{}])[0].get("FEATURES", [])
    for c in cf:
        s = c["settings"]
        print(f"Custom feature «{s.get('NAME')}» ({s.get('TYPE')}, {s.get('RUNTIMES')}): блоков кода {len(s.get('CODE_BLOCKS', []))} → "
              + ", ".join(b["settings"].get("LOCATION", "") for b in s.get("CODE_BLOCKS", [])))
    nodes = [f for f in F if f["id"].startswith(NODE_PREFIX) and f["id"] not in ("node_link", "node_group")]
    links = [f["settings"] for f in F if f["id"] == "node_link"]
    groups = {f["settings"]["ID"]: f["settings"].get("DISPLAY_NAME") for f in F if f["id"] == "node_group"}
    print(f"\nЛогика: узлов {len(nodes)}, связей {len(links)}, групп {len(groups)}: {', '.join(groups.values())}")
    print("Типы узлов:", dict(collections.Counter(f["id"][5:] for f in nodes)))
    if d.get("featureFlags"):
        for fl in d["featureFlags"]:
            print(f"Флаг «{fl['name']}» ({'вкл' if fl.get('enabled') else 'выкл'}): управляет {len(d.get('featureFlagMap', {}).get(fl['id'], []))} элементами")
    # event chains
    print("\nЦепочки (от событий):")
    for line in chains(d, ids)[:40]:
        print("  " + line)


def chains(d, ids):
    F = d["features"]
    feats = {f["settings"]["ID"]: f for f in F if "ID" in f["settings"]}
    out = collections.defaultdict(list)
    has_in = set()
    for f in F:
        if f["id"] == "node_link":
            s = f["settings"]
            out[s["SOURCE_FEATURE"]].append((s["SOURCE_PORT"], s["TARGET_FEATURE"], s["TARGET_PORT"]))
            has_in.add(s["TARGET_FEATURE"])
    roots = [i for i in out if i not in has_in]
    lines = []

    def name(i):
        f = feats.get(i)
        if not f:
            return f"?{i}"
        a, b = label(f, ids)
        return a + (f"[{pretty_ref(b, ids)}]" if b else "")

    def walk(i, depth, seen, prefix):
        if depth > 12 or i in seen:
            lines.append(prefix + " …")
            return
        nexts = out.get(i, [])
        if not nexts:
            lines.append(prefix)
            return
        for sp, t, tp in nexts:
            walk(t, depth + 1, seen | {i}, f"{prefix} —{port_name(sp, ids)}→ {name(t)}")
    for r in roots:
        walk(r, 0, set(), name(r))
    return lines


# ------------------------------------------------------------------ check
# fields that hold the ID of another element anywhere in the project (services and panels included)
REF_KEYS = {"SETTINGID", "VARIABLE", "TIMER", "COMMAND", "TABLE", "LINKEDSETTING", "FEATURE", "INTLINE", "TIBBIT",
            "SOCKET", "SERIAL_PORT", "WIDGET", "GROUP", "SCREEN", "DEVICE", "SOURCE_FEATURE", "TARGET_FEATURE"}
IDLIKE = re.compile(r"^(?=.*[0-9])(?=.*[a-z])[0-9a-z]{14,24}$")
# panels whose items expose settings / commands / tables by ID
PANELS = ("web_dashboard", "luis", "ds_man", "lcd_menu", "cgg")


def deep_refs(obj, path, out):
    """Yield (path, key, value, kind) for every REF_KEYS field holding an ID-like value, at any depth."""
    if isinstance(obj, dict):
        kind = obj.get("id") if isinstance(obj.get("id"), str) else None
        st = obj.get("settings") if isinstance(obj.get("settings"), dict) else None
        if st is not None:
            for k, v in st.items():
                if k in REF_KEYS and isinstance(v, str) and IDLIKE.match(v):
                    out.append((path, k, v, kind, st))
        for k, v in obj.items():
            deep_refs(v, f"{path}/{kind or k}", out)
    elif isinstance(obj, list):
        for v in obj:
            deep_refs(v, path, out)
    return out


def check_panels_and_refs(d, ids, errs, warns):
    """Errors AppBlocks shows in Problems but node-level checks miss (found on a real import, Oct 2026)."""
    seen = set()
    for f in d["features"]:
        for path, k, v, kind, st in deep_refs(f, f["id"], []):
            if v not in ids and (path, k, v) not in seen:
                seen.add((path, k, v))
                errs.append(f"{path}: {k}={v} не найден (в редакторе: «Setting is not defined» / "
                             f"«Connected Setting is not set» / «Command is not set»)")
    for f in d["features"]:
        if f["id"] not in PANELS:
            continue
        st = f["settings"]
        if st.get("ENABLED", "1") != "1":
            continue
        used = collections.Counter()
        for g in st.get("GROUPS", []) or []:
            for it in g.get("settings", {}).get("SETTINGS", []) or []:
                sid = it.get("settings", {}).get("SETTINGID", "")
                if not sid:
                    errs.append(f"{f['id']}: пункт «{it['settings'].get('NAME', '')}» без настройки (Connected Setting is not set)")
                used[sid] += 1
        for sid, c in used.items():
            if sid and c > 1:
                errs.append(f"{f['id']}: настройка {sid} выведена {c} раз (Same setting cannot be exposed more than once)")
        for w in st.get("WIDGETS", []) or []:
            ws = w.get("settings", {})
            if w.get("id") == "button_widget" and not ws.get("VARIABLE"):
                errs.append(f"{f['id']}: кнопка «{ws.get('LABEL', '')}» без команды (Command is not set)")
    gv = next((f["settings"] for f in d["features"] if f["id"] == "global_vars"), None)
    if gv is not None:
        try:
            if float(gv.get("INTERVAL", "1")) < 1:
                errs.append(f"global_vars INTERVAL={gv['INTERVAL']}: редактор требует ≥ 1 с "
                            "(«Value for Update Interval (seconds) must be at least 1»)")
        except ValueError:
            errs.append(f"global_vars INTERVAL={gv.get('INTERVAL')!r} не число")


def check(d):
    F = d["features"]
    ids = all_ids(d)
    errs, warns = [], []
    top_ids = collections.Counter(f["settings"].get("ID") for f in F)
    for i, c in top_ids.items():
        if c > 1:
            errs.append(f"дублируется ID {i} ({c} раз)")
    feats = {f["settings"]["ID"]: f for f in F if f["settings"].get("ID")}
    port_out = collections.defaultdict(set)
    for f in F:
        if f["id"] == "node_link":
            s = f["settings"]
            for side in ("SOURCE", "TARGET"):
                fid = s.get(f"{side}_FEATURE")
                if fid not in feats:
                    errs.append(f"link {s['ID']}: {side.lower()} {fid} не существует")
            if s.get("SOURCE_FEATURE") == s.get("TARGET_FEATURE"):
                warns.append(f"link {s['ID']}: узел соединён сам с собой")
            src = feats.get(s.get("SOURCE_FEATURE"))
            if src and src["id"] == "node_switch":
                cases = {c["settings"]["ID"] for c in src["settings"].get("CASES", [])}
                if s["SOURCE_PORT"] not in cases and s["SOURCE_PORT"] not in ("default", "switch_default"):
                    warns.append(f"link {s['ID']}: у switch нет case {s['SOURCE_PORT']}")
    linked = set()
    for f in F:
        if f["id"] == "node_link":
            linked.add(f["settings"]["SOURCE_FEATURE"]); linked.add(f["settings"]["TARGET_FEATURE"])
    for f in F:
        k = f["id"]; s = f["settings"]
        if k.startswith(NODE_PREFIX) and k not in ("node_link", "node_group", "node_system", "node_label") and s["ID"] not in linked:
            warns.append(f"узел {k} {s['ID']} ни с чем не соединён")
        if k.startswith(NODE_PREFIX) and s.get("GROUP") and s["GROUP"] not in feats:
            errs.append(f"узел {k} {s['ID']}: группа {s['GROUP']} не существует")
        for key in ("VARIABLE", "TIMER", "COMMAND", "TABLE", "SOCKET", "WIDGET", "SERIAL_PORT"):
            if k.startswith(NODE_PREFIX) and s.get(key) and s[key] not in ids:
                errs.append(f"узел {k} {s['ID']}: {key}={s[key]} не найден")
    for f in F:
        if f["id"] == "linked_setting":
            s = f["settings"]
            if s.get("LINKEDSETTING") not in ids:
                errs.append(f"linked_setting {s['ID']}: настройка {s.get('LINKEDSETTING')} не найдена")
            if s.get("FEATURE") not in ids:
                errs.append(f"linked_setting {s['ID']}: feature {s.get('FEATURE')} не найдена")
    # references inside text values: unresolved ones are either event parameters or typos
    unresolved = collections.Counter()
    for m in REF.findall(json.dumps(d)):
        if m not in ids:
            unresolved[m] += 1
    if unresolved:
        warns.append("ссылки {{$…}} не на ID (это параметры события/записи или опечатка): " + ", ".join(f"{k}×{v}" for k, v in unresolved.most_common()))
    # sockets
    socks = collections.Counter()
    for f in F:
        if f["id"].startswith("tibbit_"):
            socks[f["settings"].get("SOCKET")] += 1
            if f["id"][7:] != f["settings"].get("TIBBIT"):
                errs.append(f"{f['id']}: TIBBIT={f['settings'].get('TIBBIT')} не совпадает с типом feature")
    for sck, c in socks.items():
        if c > 1:
            errs.append(f"в сокет S{sck} поставлено {c} Tibbit")
    check_panels_and_refs(d, ids, errs, warns)
    for fl in d.get("featureFlags", []):
        for x in d.get("featureFlagMap", {}).get(fl["id"], []):
            if x not in ids:
                errs.append(f"флаг «{fl['name']}»: элемент {x} не найден")
    for e in errs:
        print("[ОШИБКА]", e)
    for w in warns:
        print("[ВНИМАНИЕ]", w)
    print(f"Итог: ошибок {len(errs)}, предупреждений {len(warns)}")
    return 1 if errs else 0


# ------------------------------------------------------------------ tps bridge
def to_tps(d, vin=None):
    by = collections.defaultdict(list)
    for f in d["features"]:
        by[f["id"]].append(f["settings"])
    slots = {}
    for k, v in by.items():
        if k.startswith("tibbit_"):
            for s in v:
                slots[f"S{s['SOCKET']}"] = s["TIBBIT"]
    bs = (by.get("boardsetting") or [{}])[0]
    wm = (by.get("wireless_module") or [{}])[0]
    cfg = {"board": d.get("device"), "slots": slots, "power": {"vin": vin},
           "poe_jumpers": "1-2" if str(bs.get("POE")) == "1" else "2-3",
           "wifi": wm.get("MODULE") if str(wm.get("ENABLED", "0")) == "1" else None,
           "buzzer": True, "ambient_c": 40,
           "_source": f"AppBlocks project {d.get('name')} ({d.get('id')}); adapter {bs.get('POWERADAPTER')}; 5VDIRECT={bs.get('5VDIRECT')}"}
    supplies = {"09", "10", "23", "25", "33"}
    if str(bs.get("5VDIRECT")) == "1":
        cfg["power"]["ext5v_ma"] = 1000
    elif not (set(slots.values()) & supplies):
        cfg["power"]["ext5v_ma"] = 1000
        cfg["_assumption"] = ("в проекте нет Tibbit-источника и 5VDIRECT=0: принято внешнее стабилизированное 5 В / 1 А "
                              "на клеммы платы — уточни у пользователя")
    return cfg


# ------------------------------------------------------------------ flow diagram
KIND_COLOR = {
    "event": "#2F8FE3", "logic": "#9B59B6", "data": "#16A085", "io": "#E67E22", "comm": "#C0392B", "sys": "#5B6770",
}


def kind_of(k):
    k = k[5:]
    if k in ("system", "button", "button_released", "timer_completed", "command_triggered", "socket_event",
             "socket_data_arrival", "network_changed", "time_interval", "cron_event", "variable_changed", "keypad",
             "keypad_released", "interrupt", "wiegand", "mqtt_connected", "mqtt_sub", "modbus_response", "modbus_timeout",
             "ser_data_arrival", "sms_recv", "ir_received", "button_input_pressed", "button_input_released", "http_server_endpoint"):
        return "event"
    if k in ("comparison", "compound_condition", "switch", "time_delay"):
        return "logic"
    if k.startswith("table") or k.startswith("string") or k in ("variable_set", "datetime", "datetime_format", "settings_init",
                                                                  "arithmetic", "math_compound", "bitwise", "random", "num_round",
                                                                  "number_to_fixed", "json_get_string", "log_add"):
        return "data"
    if k in ("command_trigger",):
        return "event"
    if k in ("modbus_write", "mqtt_pub") or k.startswith("socket") or k.startswith("http"):
        return "comm"
    if k in ("beep", "pat", "debug", "lcd_text_widget") or k.startswith("lcd"):
        return "io"
    return "sys"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def flow_svg(d):
    F = d["features"]
    ids = all_ids(d)
    nodes = {f["settings"]["ID"]: f for f in F if f["id"].startswith(NODE_PREFIX) and f["id"] not in ("node_link", "node_group")}
    groups = {f["settings"]["ID"]: f["settings"] for f in F if f["id"] == "node_group"}
    links = [f["settings"] for f in F if f["id"] == "node_link"]
    NW, NH = 200, 64
    # positions: editor X/Y; nodes in a group are stored relative to the canvas too, groups are only labels
    by_group = collections.defaultdict(list)
    for i, n in nodes.items():
        by_group[n["settings"].get("GROUP") or ""].append(i)
    # lay groups out as separate panels so they never overlap (editor coordinates kept inside a panel)
    panels = []
    for g, members in sorted(by_group.items(), key=lambda kv: (kv[0] != "", groups.get(kv[0], {}).get("DISPLAY_NAME", ""))):
        xs = [nodes[i]["settings"].get("X", 0) for i in members]
        ys = [nodes[i]["settings"].get("Y", 0) for i in members]
        panels.append((g, members, min(xs), min(ys), max(xs) + NW - min(xs), max(ys) + NH - min(ys)))
    pos = {}
    y0 = 70
    W = 0
    for g, members, mx, my, w, h in panels:
        for i in members:
            s = nodes[i]["settings"]
            pos[i] = (40 + s.get("X", 0) - mx, y0 + 40 + s.get("Y", 0) - my)
        panels_rect = (20, y0, w + 40, h + 60)
        W = max(W, w + 80)
        nodes_panel = (g, panels_rect)
        y0 += h + 100
        pos[("panel", g)] = panels_rect
    H = y0 + 20
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#F7F8FA"/>',
         '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555"/></marker></defs>',
         f'<text x="20" y="40" font-size="22" font-weight="800" fill="#222">{esc(d.get("name"))} — логика AppBlocks ({len(nodes)} узлов, {len(links)} связей)</text>']
    for g, members, *_ in panels:
        x, y, w, h = pos[("panel", g)]
        title = groups.get(g, {}).get("DISPLAY_NAME") or ("без группы" if not g else g)
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="#D5D9DE"/>')
        o.append(f'<text x="{x + 14}" y="{y + 24}" font-size="15" font-weight="700" fill="#556">Группа: {esc(title)}</text>')
    for l in links:
        a, b = l["SOURCE_FEATURE"], l["TARGET_FEATURE"]
        if a not in pos or b not in pos:
            continue
        x1, y1 = pos[a][0] + NW, pos[a][1] + NH / 2
        x2, y2 = pos[b][0], pos[b][1] + NH / 2
        dx = max(40, abs(x2 - x1) / 2)
        o.append(f'<path d="M{x1},{y1} C{x1 + dx},{y1} {x2 - dx},{y2} {x2},{y2}" fill="none" stroke="#888" stroke-width="1.6" marker-end="url(#a)"/>')
        o.append(f'<text x="{x1 + 8 + (x2 - x1) * 0.12:.0f}" y="{y1 + (y2 - y1) * 0.22 - 5:.0f}" font-size="9.5" fill="#777">{esc(port_name(l["SOURCE_PORT"], ids)[:22])}</text>')
    for i, n in nodes.items():
        x, y = pos[i]
        title, extra = label(n, ids)
        col = KIND_COLOR[kind_of(n["id"])]
        args = n["settings"].get("ARGUMENTS", []) or []
        tip = "\n".join(f"{a['settings']['TARGETPARAM']} = {pretty_ref(a['settings']['ARGVALUE'], ids)}" for a in args)
        o.append(f'<g><title>{esc(n["id"])}\n{esc(tip)}</title>')
        o.append(f'<rect x="{x}" y="{y}" width="{NW}" height="{NH}" rx="8" fill="#fff" stroke="{col}" stroke-width="2"/>')
        o.append(f'<rect x="{x}" y="{y}" width="8" height="{NH}" rx="4" fill="{col}"/>')
        o.append(f'<text x="{x + 16}" y="{y + 22}" font-size="13" font-weight="700" fill="#222">{esc(title[:24])}</text>')
        if extra:
            o.append(f'<text x="{x + 16}" y="{y + 40}" font-size="11" fill="#444">{esc(pretty_ref(extra, ids)[:30])}</text>')
        if args:
            a0 = args[0]["settings"]
            o.append(f'<text x="{x + 16}" y="{y + 56}" font-size="10" fill="#777">{esc((a0["TARGETPARAM"] + "=" + pretty_ref(a0["ARGVALUE"], ids))[:32])}</text>')
        o.append("</g>")
    lx = W - 560
    for k, (name, col) in enumerate((("события", KIND_COLOR["event"]), ("логика", KIND_COLOR["logic"]), ("данные", KIND_COLOR["data"]),
                                     ("связь", KIND_COLOR["comm"]), ("индикация", KIND_COLOR["io"]), ("система", KIND_COLOR["sys"]))):
        o.append(f'<rect x="{lx + k * 92}" y="28" width="12" height="12" fill="{col}"/><text x="{lx + k * 92 + 17}" y="39" font-size="12" fill="#333">{name}</text>')
    o.append("</svg>")
    return "\n".join(o)


def nodes_catalog(d):
    F = d["features"]
    feats = {f["settings"]["ID"]: f for f in F if f["settings"].get("ID")}
    ports = collections.defaultdict(lambda: {"in": set(), "out": set()})
    for f in F:
        if f["id"] == "node_link":
            s = f["settings"]
            if s["SOURCE_FEATURE"] in feats:
                ports[feats[s["SOURCE_FEATURE"]]["id"]]["out"].add(s["SOURCE_PORT"])
            if s["TARGET_FEATURE"] in feats:
                ports[feats[s["TARGET_FEATURE"]]["id"]]["in"].add(s["TARGET_PORT"])
    for k in sorted({f["id"] for f in F if f["id"].startswith(NODE_PREFIX)}):
        print(f"{k:<28} in: {', '.join(sorted(ports[k]['in'])) or '—':<30} out: {', '.join(sorted(ports[k]['out'])) or '—'}")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    cmd = a[0]
    if cmd == "ids":
        print("\n".join(new_id(int(a[1]) if len(a) > 1 else 1))); return
    d = load(a[1])
    if cmd == "summary":
        summary(d)
    elif cmd == "check":
        sys.exit(check(d))
    elif cmd == "tps":
        vin = float(a[a.index("--vin") + 1]) if "--vin" in a else None
        txt = json.dumps(to_tps(d, vin), ensure_ascii=False, indent=1)
        if "--out" in a:
            open(a[a.index("--out") + 1], "w", encoding="utf-8").write(txt)
        else:
            print(txt)
    elif cmd == "flow":
        open(a[2], "w", encoding="utf-8").write(flow_svg(d))
    elif cmd == "nodes":
        nodes_catalog(d)
    else:
        print(__doc__); sys.exit(2)


if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("не хватает аргумента команды\n" + __doc__)
        sys.exit(2)
    except BrokenPipeError:
        pass
