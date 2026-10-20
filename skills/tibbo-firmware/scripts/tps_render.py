"""Board-style SVG of a TPS configuration, drawn like Tibbo's own TPS configurator.

Green PCB, C-sockets at the board edge, M-sockets inside, Tibbits as coloured blocks with a black
label plate (big model number, name, line names with LED squares), connectors as orange blocks sticking
out of the edge. Empty sockets show their number in a circle and what the socket can do
(FULL / LINES A,B / LINE A ONLY / NO IO LINES, SERn(k), INTn(k), ADC, PoE).
Below the board: +5V power budget bar and the numbered list of findings; numbers are also
shown as badges on the board.

Layout source: TPP3(G2) picture from the Tibbo configurator. TPP2 uses the same arrangement scaled
down (bottom row S1–S7, top row S9–S11 next to RJ45, S13 = RF only) — check against the configurator.
"""

COL = 138          # width of one socket column
M_H = 283          # height of an M socket
C_H = 82           # height of a C socket
BOARD = "#17B884"
BOARD_LINE = "#5FD8AE"
CAT = {   # fill, darker stripe
    "power": ("#F2C230", "#C99A00"),
    "input": ("#8CC63F", "#5E9A18"),
    "output": ("#E2463F", "#A9231D"),
    "io": ("#2F8FE3", "#1C62A8"),
    "empty": ("#C3C6C8", "#8E9295"),
    "connector": ("#EE6A2C", "#B8461A"),
}


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def layout(board):
    """socket number -> (x, y, w, h, row) ; row 'top' or 'bottom'"""
    fam = board["family"]
    m = board["m_sockets"]
    n_bottom = 8 if fam == "TPP3" else 4
    bottom, top = m[:n_bottom], m[n_bottom:]
    x0 = 195
    y_top_c, y_top_m = 128, 128 + C_H + 2
    y_bot_m = y_top_m + M_H + 2
    y_bot_c = y_bot_m + M_H + 2
    pos = {}
    for i, s in enumerate(bottom):
        x = x0 + i * COL
        pos[s] = (x, y_bot_m, COL, M_H, "bottom")
        pos[s + 1] = (x, y_bot_c, COL, C_H, "bottom")
    # top row: right-aligned with the bottom row, numbers grow right-to-left
    right = x0 + n_bottom * COL
    for i, s in enumerate(top):
        x = right - (i + 1) * COL
        pos[s] = (x, y_top_m, COL, M_H, "top")
        pos[s + 1] = (x, y_top_c, COL, C_H, "top")
    rf = board.get("rf_socket")
    if rf:
        x = right - (len(top) + 1) * COL
        pos[rf] = (x, y_top_c, COL, C_H, "top")
    width = right + 70
    return pos, width, y_bot_c + C_H


def socket_caption(board, s):
    sk = board["sockets"].get(f"S{s}", {})
    if sk.get("type") != "M":
        return []
    n = len(sk.get("lines", {}))
    cap = ["FULL" if n == 4 else ("NO IO LINES" if n == 0 else
           ("LINE A ONLY" if n == 1 else "LINES " + ",".join(sk["lines"])))]
    feats = []
    if sk.get("uart") is not None:
        feats.append(f"SER{sk['uart'] + 1}({sk['uart']})")
    if sk.get("int") is not None:
        feats.append(f"INT{sk['int'] + 1}({sk['int']})")
    if sk.get("adc"):
        feats.append("ADC")
    if board.get("poe") and s == board["poe"]["m1"]:
        feats.append("PoE")
    if feats:
        cap.append(" ".join(feats))
    return cap


def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines[:3]


def pins(o, x, y, w, h, fill, dark):
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}"/>')
    n = max(3, int(w / 22))
    step = (w - 16) / n
    for i in range(n):
        px = x + 8 + i * step + step / 2 - 4
        o.append(f'<rect x="{px:.1f}" y="{y + 7}" width="8" height="11" fill="{dark}" opacity=".75"/>')
        o.append(f'<rect x="{px:.1f}" y="{y + h - 18}" width="8" height="11" fill="{dark}" opacity=".75"/>')


def cat_of(t):
    c = t["category"]
    if c == "connector" and t["kind"] in ("H", "M"):
        return "io"
    return c


def module(o, u, t, rect, row):
    x, y, w, h = rect
    fill, dark = CAT.get(cat_of(t), CAT["io"])
    pad = 5
    pins(o, x + pad, y + pad, w - 2 * pad, h - 2 * pad, fill, dark)
    px, py, pw, ph = x + 18, y + 30, w - 36, h - 60
    o.append(f'<path d="M{px + 14},{py} H{px + pw} V{py + ph} H{px} V{py + 14} Z" fill="#141414"/>')
    o.append(f'<path d="M{px},{py + 14} L{px + 14},{py} V{py + 14} Z" fill="{fill}"/>')
    # rotated text: bottom row reads bottom-to-top, top row top-to-bottom (as on Tibbo drawings)
    cx, cy = px + pw / 2, py + ph / 2
    rot = -90 if row == "bottom" else 90
    L = ph - 16          # text length available along the rotated axis
    o.append(f'<g transform="translate({cx:.1f},{cy:.1f}) rotate({rot})">')
    left = -L / 2
    big = 30 if w <= COL else 34
    # model number at the start
    o.append(f'<text x="{left:.1f}" y="{pw / 2 - 10:.1f}" fill="#fff" font-size="{big}" font-weight="800">#{esc(u["model"])}</text>')
    # name next to it
    lines = [l["id"] for l in t["lines"] if l["need"]]
    label_zone = (max(len(x) for x in lines) * 5.2 + 22) if lines else 0
    nx = left + 0.62 * big * (len(u["model"]) + 1) + 6
    avail = L / 2 - label_zone - nx - 4
    stacked = avail < 70          # not enough room after the number: put the name under it
    if stacked:
        nx = left
        avail = L - label_zone - 8
    name_lines = wrap(t["name"].upper(), max(8, int(avail / 6.6)))
    for i, ln in enumerate(name_lines):
        base = pw / 2 - (big + 12 if stacked else 12)
        o.append(f'<text x="{nx:.1f}" y="{base - (len(name_lines) - 1 - i) * 13:.1f}" fill="#fff" font-size="10.5" font-weight="600">{esc(ln)}</text>')
    # line labels with LED squares on the far side of the plate
    if lines:
        step = min(28, (pw - 20) / max(len(lines), 1))
        for i, ln in enumerate(lines):
            ly = -pw / 2 + 12 + i * step
            o.append(f'<rect x="{L / 2 - 10:.1f}" y="{ly:.1f}" width="10" height="10" fill="none" stroke="#fff" stroke-width="1.3"/>')
            o.append(f'<text x="{L / 2 - 14:.1f}" y="{ly + 9:.1f}" fill="#fff" font-size="8.5" text-anchor="end">{esc(ln)}</text>')
    o.append("</g>")


def connector(o, u, t, rect, row, label=True):
    x, y, w, h = rect
    fill, dark = CAT["connector"]
    ext = 42
    if row == "bottom":
        by, bh, stripe = y, h + ext, y + h + ext - 12
    else:
        by, bh, stripe = y - ext, h + ext, y - ext
    o.append(f'<rect x="{x + 2}" y="{by}" width="{w - 4}" height="{bh}" fill="{fill}"/>')
    o.append(f'<rect x="{x + 2}" y="{stripe}" width="{w - 4}" height="12" fill="{dark}"/>')
    if not label:
        return
    px, pw = x + 12, w - 24
    py = (y + 20) if row == "bottom" else (by + 22)
    ph = h - 4
    o.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="3" fill="#141414"/>')
    o.append(f'<text x="{px + pw - 8}" y="{py + 30}" fill="#fff" font-size="24" font-weight="800" text-anchor="end">#{esc(u["model"])}</text>')
    for i, ln in enumerate(wrap(t["name"].upper(), int(pw / 7.4))[:2]):
        o.append(f'<text x="{px + 8}" y="{py + 50 + i * 13}" fill="#fff" font-size="10.5" font-weight="600">{esc(ln)}</text>')


def line_map(board, u, t):
    """[(line id, socket, letter, PL_IO_NUM or None)] for lines the Tibbit uses."""
    m_socks = [s for s in u["sockets"] if board["sockets"].get(f"S{s}", {}).get("type") == "M"]
    out = []
    for i, ln in enumerate(t["lines"]):
        if not ln["need"] or i >= 4 * len(m_socks):
            continue
        s = m_socks[i // 4]
        letter = "ABCD"[i % 4]
        out.append((ln["id"], s, letter, board["sockets"][f"S{s}"]["lines"].get(letter)))
    return out


def unit_tip(board, u, t):
    lm = line_map(board, u, t)
    first = board["sockets"].get(f"S{u['sockets'][0]}", {})
    parts = [f"#{u['model']} {t['name']} ({t['form']})", "Сокеты: S" + ", S".join(map(str, u["sockets"]))]
    if "serial" in t["requires"] and first.get("uart") is not None:
        parts.append(f"ser.num = {first['uart']}")
    for lid, s, letter, pl in lm:
        parts.append(f"{lid}: S{s}.{letter} → {pl or 'нет линии'}")
    c = t["consumes_ma"]
    if c:
        parts.append("Потребление: " + ", ".join(f"{k} {v} мА" for k, v in c.items()))
    if t.get("supplies_ma"):
        parts.append("Выдаёт: " + ", ".join(f"{k} {v} мА" for k, v in t["supplies_ma"].items()))
    return "\n".join(parts)


def conn_rows(board, units, tib):
    rows = []
    for u in sorted(units, key=lambda v: v["start"]):
        t = tib[u["model"]]
        lm = line_map(board, u, t)
        first = board["sockets"].get(f"S{u['sockets'][0]}", {})
        ex = []
        if "serial" in t["requires"] and first.get("uart") is not None:
            ex.append(f"ser.num {first['uart']}")
        c5 = t["consumes_ma"].get("+5V")
        sup = t.get("supplies_ma", {})
        if sup:
            ex.append("даёт " + ", ".join(f"{k} {v}" for k, v in sup.items()) + " мА")
        elif c5:
            ex.append(f"{c5} мА")
        if t["kind"] == "C" and not lm:
            continue
        lines_txt = [f"{lid}→{(pl or 'нет').replace('PL_IO_NUM_', '')}" for lid, s, letter, pl in lm]
        ss = u["sockets"]
        label = f"S{ss[0]}–S{ss[-1]}" if len(ss) > 2 and ss == list(range(ss[0], ss[-1] + 1)) else "S" + "+S".join(map(str, ss))
        rows.append((label, u["model"], t["name"], lines_txt, " · ".join(ex), cat_of(t)))
    return rows


def badge(o, x, y, num, level):
    col = "#D0021B" if level == "error" else "#E8A100"
    o.append(f'<circle cx="{x}" cy="{y}" r="12" fill="{col}" stroke="#fff" stroke-width="2"/>')
    o.append(f'<text x="{x}" y="{y + 4.5}" fill="#fff" font-size="12.5" font-weight="800" text-anchor="middle">{num}</text>')


def render(res, board, rep, tib):
    pos, W, board_bottom = layout(board)
    fam = board["family"]
    units = res["units"]
    by_sock = {s: u for u in units for s in u["sockets"]}
    findings = [i for i in rep.items if i["level"] in ("error", "warning")]
    p = res["power"]
    H_board = board_bottom + 50
    ncol = max(2, int((W - 75) / 300))
    n_leg_rows = (len(p["consumers"]) + ncol - 1) // ncol
    table = conn_rows(board, units, tib)
    n_tab = sum(len(rw[3]) for rw in table)
    H = H_board + 190 + 20 * n_leg_rows + 24 * max(len(findings), 1) + (70 + 19 * n_tab if table else 0)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="60 80 {W - 40} {H - 80}" font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<rect width="{W + 20}" height="{H}" fill="#FFFFFF"/>']
    # PCB
    left_x = 75
    o.append(f'<rect x="{left_x}" y="128" width="{W - left_x}" height="{board_bottom - 128}" fill="{BOARD}"/>')
    o.append(f'<text transform="translate({W - 20},{(128 + board_bottom) / 2}) rotate(-90)" fill="#fff" font-size="26" font-weight="800" text-anchor="middle">{esc(res["board"])}</text>')
    # RJ45 / wireless area (left of the top row)
    top_left = min(v[0] for k, v in pos.items() if v[4] == "top")
    o.append(f'<rect x="205" y="92" width="122" height="162" fill="#1E9AD6"/><rect x="216" y="108" width="100" height="132" fill="#14324D"/>')
    o.append('<text x="266" y="180" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">RJ45</text>')
    on5 = bool(res.get("ext5v"))
    o.append(f'<rect x="132" y="92" width="64" height="64" fill="#14A57A" stroke="#fff" stroke-width="2"/>')
    o.append(f'<text x="164" y="110" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">+5V</text>')
    o.append(f'<rect x="155" y="116" width="18" height="18" fill="{"#fff" if on5 else "none"}" stroke="#fff" stroke-width="2"/>')
    o.append(f'<text x="164" y="150" fill="#fff" font-size="11" font-weight="700" text-anchor="middle">{"ON" if on5 else "OFF"}</text>')
    if board.get("poe"):
        jx, jy = top_left + 42, 222
        on_poe = str(res.get("poe_jumpers", "2-3")) == "1-2"
        o.append(f'<rect x="{jx}" y="{jy}" width="70" height="70" fill="none" stroke="#fff" stroke-width="2"/>')
        o.append(f'<rect x="{jx + (2 if on_poe else 36)}" y="{jy + 2}" width="32" height="66" fill="#2B2B2B"/>')
        o.append(f'<text transform="translate({jx + 23},{jy + 52}) rotate(-90)" fill="#fff" font-size="11" font-weight="700">PoE</text>')
        o.append(f'<text transform="translate({jx + 57},{jy + 54}) rotate(-90)" fill="#fff" font-size="11" font-weight="700">S{board["poe"]["m1"] + 1}</text>')
        o.append(f'<title>Перемычки у RJ45: {"1-2 (линии питания RJ45 → PoE-сокет)" if on_poe else "2-3 (обычный тайл)"}</title>')
    if top_left - left_x > 150 and not res.get("wifi"):
        o.append(f'<rect x="116" y="303" width="{top_left + 113 - 116}" height="150" fill="none" stroke="#fff" stroke-width="2"/>')
        o.append(f'<text x="{116 + (top_left + 113 - 116) / 2}" y="383" fill="#fff" font-size="14" font-weight="700" text-anchor="middle">WIRELESS</text>')
    if res.get("wifi") and top_left - left_x > 150:
        wx, wy, ww = 132, 318, top_left + 113 - 148
        o.append(f'<g><title>Wi-Fi add-on {esc(res["wifi"])}: +300 мА от +5 В</title>')
        o.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="120" rx="3" fill="{CAT["io"][0]}"/>')
        o.append(f'<path d="M{wx + 26},{wy + 14} H{wx + ww - 12} V{wy + 106} H{wx + 12} V{wy + 28} Z" fill="#141414"/>')
        o.append(f'<text x="{wx + 28}" y="{wy + 58}" fill="#fff" font-size="26" font-weight="800">{esc(res["wifi"])}</text>')
        o.append(f'<text x="{wx + 28}" y="{wy + 82}" fill="#fff" font-size="11" font-weight="600">WI-FI / BLUETOOTH ADD-ON</text></g>')
    # empty sockets
    for s, (x, y, w, h, row) in pos.items():
        if s in by_sock:
            continue
        o.append(f'<rect x="{x + 1}" y="{y}" width="{w - 2}" height="{h}" fill="none" stroke="{BOARD_LINE}" stroke-width="2"/>')
        dots_y = [y + h - 22] if h == C_H and row == "bottom" else ([y + 60] if h == C_H else [y + 20, y + h - 20])
        if s == board.get("rf_socket"):
            dots_y = []
        for dy in dots_y:
            for i in range(7):
                o.append(f'<circle cx="{x + 22 + i * 15.5}" cy="{dy}" r="2.6" fill="#0B3D2E"/>')
        cy = y + (25 if h == C_H and row == "top" else (h / 2 - 18 if h == M_H else 25))
        o.append(f'<circle cx="{x + w / 2}" cy="{cy}" r="16" fill="none" stroke="#fff" stroke-width="2"/>')
        o.append(f'<text x="{x + w / 2}" y="{cy + 4.5}" fill="#fff" font-size="12.5" font-weight="700" text-anchor="middle">S{s}</text>')
        cap = socket_caption(board, s)
        if s == board.get("rf_socket"):
            cap = []
            o.append(f'<text x="{x + w / 2}" y="{y + 64}" fill="#fff" font-size="10.5" font-weight="700" text-anchor="middle">ТОЛЬКО #37 (RF)</text>')
        for i, c in enumerate(cap):
            o.append(f'<text x="{x + w / 2}" y="{cy + 38 + i * 18}" fill="#fff" font-size="12.5" font-weight="700" text-anchor="middle">{esc(c)}</text>')
        sk = board["sockets"].get(f"S{s}", {})
        if sk.get("type") == "M" and sk.get("lines"):
            import re as _re
            order = "ABCD" if row == "bottom" else "DCBA"
            nums = [(_re.match(r"PL_IO_NUM_(\d+)", sk["lines"][L]).group(1) if L in sk["lines"] else "–") for L in order]
            ny = y + 42 if row == "bottom" else y + h - 42
            o.append(f'<text x="{x + w / 2}" y="{ny}" fill="#fff" font-size="11.5" font-weight="700" text-anchor="middle" word-spacing="6">{" ".join(nums)}</text>')
    # installed Tibbits
    findings_by_where = {}
    for i, f in enumerate(findings, 1):
        findings_by_where.setdefault(f["where"], []).append((i, f["level"]))
    for u in units:
        t = tib[u["model"]]
        socks = [s for s in u["sockets"] if s in pos]
        if not socks:
            continue
        xs = [pos[s][0] for s in socks]
        kind = t["kind"]
        row = pos[socks[0]][4]
        m_socks = [s for s in socks if pos[s][3] == M_H]
        c_socks = [s for s in socks if pos[s][3] == C_H]
        o.append(f'<g><title>{esc(unit_tip(board, u, t))}</title>')
        if m_socks:
            mx = min(pos[s][0] for s in m_socks); mw = max(pos[s][0] for s in m_socks) + COL - mx
            module(o, u, t, (mx, pos[m_socks[0]][1], mw, M_H), row)
        if c_socks:
            cx = min(pos[s][0] for s in c_socks); cw = max(pos[s][0] for s in c_socks) + COL - cx
            connector(o, u, t, (cx, pos[c_socks[0]][1], cw, C_H), row, label=(kind == "C"))
        o.append('</g>')
        bx = min(xs) + 14
        by = (pos[socks[0]][1] + 14) if kind != "C" or row == "bottom" else pos[socks[0]][1] - 30
        for k, (num, lvl) in enumerate(findings_by_where.get(f"S{u['start']}", [])):
            badge(o, bx + k * 27, by, num, lvl)
            if lvl == "error":
                x0 = min(xs); x1 = max(xs) + COL
                y0 = min(pos[s][1] for s in socks); y1 = max(pos[s][1] + pos[s][3] for s in socks)
                o.append(f'<rect x="{x0 + 2}" y="{y0 + 2}" width="{x1 - x0 - 4}" height="{y1 - y0 - 4}" fill="none" stroke="#D0021B" stroke-width="4" stroke-dasharray="10 5"/>')
    # connection table
    y = H_board + 20
    if table:
        o.append(f'<text x="{left_x}" y="{y}" font-size="18" font-weight="800" fill="#222">Подключение к CPU</text>')
        wide = W - left_x > 1100
        cols = [left_x, left_x + 100, left_x + 185, left_x + (480 if wide else 395), W - (150 if wide else 190)]
        heads = ["Сокет", "Tibbit", "Назначение", "Линии → PL_IO_NUM_*", "UART · +5 В"]
        y += 26
        for cx, hd in zip(cols, heads):
            o.append(f'<text x="{cx}" y="{y}" font-size="12" font-weight="700" fill="#666">{hd}</text>')
        y += 6
        o.append(f'<line x1="{left_x}" x2="{W}" y1="{y}" y2="{y}" stroke="#CCC"/>')
        maxch = int((cols[4] - cols[3] - 10) / 6.4)
        for k, (sock, model, name, lines_txt, extra, cat) in enumerate(table):
            wrapped = []
            cur = ""
            for part in lines_txt or ["—"]:
                if len(cur) + len(part) + 3 > maxch and cur:
                    wrapped.append(cur); cur = part
                else:
                    cur = (cur + " · " + part) if cur else part
            wrapped.append(cur)
            hrow = 19 * len(wrapped)
            if k % 2 == 0:
                o.append(f'<rect x="{left_x}" y="{y + 2}" width="{W - left_x}" height="{hrow + 4}" fill="#F6F7F8"/>')
            fill = CAT.get(cat, CAT["io"])[0]
            o.append(f'<rect x="{cols[1]}" y="{y + 7}" width="10" height="10" fill="{fill}"/>')
            o.append(f'<text x="{cols[0]}" y="{y + 17}" font-size="12.5" font-weight="700" fill="#222">{esc(sock)}</text>')
            o.append(f'<text x="{cols[1] + 16}" y="{y + 17}" font-size="12.5" font-weight="700" fill="#222">#{esc(model)}</text>')
            nmax = int((cols[3] - cols[2] - 12) / 6.3)
            o.append(f'<text x="{cols[2]}" y="{y + 17}" font-size="12" fill="#333">{esc(name if len(name) <= nmax else name[:nmax - 1] + "…")}</text>')
            for i, wl in enumerate(wrapped):
                o.append(f'<text x="{cols[3]}" y="{y + 17 + 19 * i}" font-size="11.5" fill="#333" font-family="Menlo,Consolas,monospace">{esc(wl)}</text>')
            o.append(f'<text x="{cols[4]}" y="{y + 17}" font-size="12" fill="#333">{esc(extra)}</text>')
            y += hrow + 6
        y += 40
    # power budget
    cap = p["capacity_5v_ma"]
    tot = p["total_5v_ma"]
    util = tot / cap if cap else None
    pwarn = any(f["where"] == "питание" for f in findings)
    col = "#D0021B" if (util is None or util > 1) else ("#C77C00" if pwarn or util > 0.8 else "#1B8A5A")
    head = f"Питание +5 В: потребление {tot} мА из {cap} мА" + (f" — загрузка {util:.0%}" if util is not None else " — источника нет")
    o.append(f'<text x="{left_x}" y="{y}" font-size="18" font-weight="800" fill="{col}">{esc(head)}</text>')
    bw = W - left_x
    scale = bw / max(cap, tot, 1)
    o.append(f'<rect x="{left_x}" y="{y + 12}" width="{bw}" height="34" fill="#F1F3F4"/>')
    if cap:
        o.append(f'<rect x="{left_x}" y="{y + 12}" width="{cap * scale:.1f}" height="34" fill="#E3F5EC" stroke="#1B8A5A" stroke-width="1.5"/>')
    xx = left_x
    pal = ["#5B6770", "#2F8FE3", "#8CC63F", "#E2463F", "#F2C230", "#9B59B6", "#16A3A3", "#EE6A2C"]
    for i, (n, v) in enumerate(p["consumers"]):
        w = v * scale
        o.append(f'<rect x="{xx:.1f}" y="{y + 16}" width="{max(w - 1, 0.5):.1f}" height="26" fill="{pal[i % len(pal)]}"><title>{esc(n)}: {v} мА</title></rect>')
        if w > 52:
            o.append(f'<text x="{xx + 5:.1f}" y="{y + 33}" fill="#fff" font-size="11" font-weight="600">{esc(n[:int(w / 6.3)])}</text>')
        xx += w
    colw = bw / ncol
    for i, (n, v) in enumerate(p["consumers"]):
        lx = left_x + (i % ncol) * colw
        ly = y + 68 + (i // ncol) * 20
        o.append(f'<rect x="{lx:.1f}" y="{ly - 10}" width="12" height="12" fill="{pal[i % len(pal)]}"/>')
        o.append(f'<text x="{lx + 18:.1f}" y="{ly}" font-size="12.5" fill="#333">{esc(n)} — {v} мА</text>')
    y += 68 + 20 * n_leg_rows
    src = "; ".join(f"{n} — {v} мА" for n, v in p["sources"]) or "нет"
    o.append(f'<text x="{left_x}" y="{y + 6}" font-size="13" fill="#333"><tspan font-weight="700">Источники:</tspan> {esc(src)}</text>')
    if p.get("rail_15v"):
        r = p["rail_15v"]
        o.append(f'<text x="{left_x}" y="{y + 26}" font-size="13" fill="#333"><tspan font-weight="700">±15 В:</tspan> +{r["plus_ma"]} / −{r["minus_ma"]} мА из {r["capacity_ma"]} мА</text>')
    # findings
    y += 40
    if findings:
        for i, f in enumerate(findings, 1):
            badge(o, left_x + 12, y + i * 24 - 5, i, f["level"])
            o.append(f'<text x="{left_x + 32}" y="{y + i * 24}" font-size="13" fill="#222"><tspan font-weight="700">{esc(f["where"])}:</tspan> {esc(f["msg"])}</text>')
    else:
        o.append(f'<text x="{left_x}" y="{y + 20}" font-size="14" font-weight="700" fill="#1B8A5A">Ошибок и предупреждений нет</text>')
    y_end = (y + 24 * len(findings) + 30) if findings else y + 40
    o[0] = o[0].replace(f'viewBox="60 80 {W - 40} {H - 80}"', f'viewBox="60 80 {W - 40} {y_end - 80:.0f}"')
    o.append("</svg>")
    return "\n".join(o)
