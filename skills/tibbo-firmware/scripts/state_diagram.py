#!/usr/bin/env python3
"""State diagram (SVG) for firmware built as a state machine.

  python3 state_diagram.py fsm.json out.svg

fsm.json:
{
  "title": "Автополив — конечный автомат (тик 0,5 с)",
  "states": [
    {"id": "START", "note": "набор 8 замеров", "outputs": "насос выкл · LED B-~", "kind": "init"},
    {"id": "IDLE",  "note": "ждём сухость",    "outputs": "насос выкл"},
    {"id": "FAULT", "note": "насос заблокирован", "kind": "fault"}
  ],
  "transitions": [
    {"from": "START", "to": "IDLE", "label": "8 исправных замеров"},
    {"from": "*", "to": "FAULT", "label": "датчик вне диапазона"}      // "*" = из любого состояния
  ],
  "layout": "row"            // row (default): main states left→right, fault/error states below
}
kind: "init" (blue), "normal" (default, green), "active" (orange, e.g. an output is on), "fault" (red).
"""
import json, sys, math


def utf8_stdio():
    """Print UTF-8 whatever the console code page is (Windows cp1251/cp1252, pipes in Git Bash)."""
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

COL = {"init": ("#E8F1FD", "#2F6FD0"), "normal": ("#E8F6EE", "#1B8A5A"), "active": ("#FFF2E0", "#D9822B"),
       "fault": ("#FDECEC", "#C62828")}
W_BOX, H_BOX, GAP_X = 210, 92, 160


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(fsm):
    states = fsm["states"]
    main = [s for s in states if s.get("kind") != "fault"]
    faults = [s for s in states if s.get("kind") == "fault"]
    pos = {}
    x0, y_main, y_fault = 40, 230, 230 + H_BOX + 170
    for i, s in enumerate(main):
        pos[s["id"]] = (x0 + i * (W_BOX + GAP_X), y_main)
    width = x0 * 2 + len(main) * W_BOX + (len(main) - 1) * GAP_X
    for i, s in enumerate(faults):
        fx = width / 2 - (len(faults) * (W_BOX + GAP_X) - GAP_X) / 2 + i * (W_BOX + GAP_X)
        pos[s["id"]] = (fx, y_fault)
    H = (y_fault + H_BOX + 60) if faults else (y_main + H_BOX + 150)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {H}" font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif">',
         f'<rect width="{width}" height="{H}" fill="#FFFFFF"/>',
         '<defs>' + "".join(
             f'<marker id="m{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
             for k, c in (("n", "#555"), ("f", "#C62828"))) + '</defs>',
         f'<text x="{x0}" y="44" font-size="22" font-weight="800" fill="#222">{esc(fsm.get("title", "Конечный автомат"))}</text>']
    order = {s["id"]: i for i, s in enumerate(main)}
    pair_count = {}
    labels = []
    for t in fsm["transitions"]:
        srcs = [s["id"] for s in main] if t["from"] == "*" else [t["from"]]
        if t["from"] == "*":
            # one fan-in arrow from the main row's centre instead of N arrows
            tx, ty = pos[t["to"]]
            cx = width / 2
            o.append(f'<path d="M{cx},{y_main + H_BOX + 18} L{tx + W_BOX / 2},{ty - 4}" fill="none" stroke="#C62828" stroke-width="2.2" stroke-dasharray="7 5" marker-end="url(#mf)"/>')
            o.append(f'<line x1="{x0 + W_BOX / 2}" x2="{pos[main[-1]["id"]][0] + W_BOX / 2}" y1="{y_main + H_BOX + 18}" y2="{y_main + H_BOX + 18}" stroke="#C62828" stroke-width="2.2" stroke-dasharray="7 5"/>')
            for s in main:
                sx = pos[s["id"]][0] + W_BOX / 2
                o.append(f'<line x1="{sx}" x2="{sx}" y1="{y_main + H_BOX}" y2="{y_main + H_BOX + 18}" stroke="#C62828" stroke-width="2.2" stroke-dasharray="4 4"/>')
            labels.append((cx + 12, (y_main + H_BOX + 18 + ty) / 2, "любое → " + t["label"], "#C62828", "start"))
            continue
        a, b = t["from"], t["to"]
        (ax, ay), (bx, by) = pos[a], pos[b]
        fault = b in [f["id"] for f in faults]
        col = "#C62828" if fault else "#555"
        mk = "mf" if fault else "mn"
        key = tuple(sorted((a, b)))
        n = pair_count.get(key, 0)
        pair_count[key] = n + 1
        if a == b:
            o.append(f'<path d="M{ax + W_BOX * 0.3},{ay} C{ax + W_BOX * 0.3},{ay - 70} {ax + W_BOX * 0.7},{ay - 70} {ax + W_BOX * 0.7},{ay}" fill="none" stroke="{col}" stroke-width="2" marker-end="url(#{mk})"/>')
            labels.append((ax + W_BOX / 2, ay - 62, t["label"], col, "middle"))
            continue
        if a in order and b in order:
            fwd = order[b] > order[a]
            adjacent = abs(order[b] - order[a]) == 1
            if fwd and adjacent and n == 0:
                y = ay + H_BOX * 0.42
                o.append(f'<path d="M{ax + W_BOX},{y} L{bx},{y}" stroke="{col}" stroke-width="2" fill="none" marker-end="url(#{mk})"/>')
                labels.append(((ax + W_BOX + bx) / 2, y - 10, t["label"], col, "middle"))
            else:
                # arcs above the row (backward / long jumps)
                lift = 50 + 48 * abs(order[b] - order[a]) + 22 * n
                sx, ex = ax + W_BOX / 2, bx + W_BOX / 2
                if fwd:
                    sx, ex = ax + W_BOX * 0.62, bx + W_BOX * 0.38
                else:
                    sx, ex = ax + W_BOX * 0.38, bx + W_BOX * 0.62
                o.append(f'<path d="M{sx},{ay} C{sx},{ay - lift} {ex},{ay - lift} {ex},{ay}" stroke="{col}" stroke-width="2" fill="none" marker-end="url(#{mk})"/>')
                labels.append(((sx + ex) / 2, ay - lift * 0.75 - 4, t["label"], col, "middle"))
        else:
            # to/from fault row
            if fault:
                sx, sy, ex, ey = ax + W_BOX / 2, ay + H_BOX, bx + W_BOX * 0.3, by
            else:
                sx, sy, ex, ey = ax + W_BOX * 0.7, ay, bx + W_BOX / 2, by + H_BOX
            o.append(f'<path d="M{sx},{sy} C{sx},{(sy + ey) / 2} {ex},{(sy + ey) / 2} {ex},{ey}" stroke="{col}" stroke-width="2" fill="none" marker-end="url(#{mk})"/>')
            labels.append(((sx + ex) / 2 + 8, (sy + ey) / 2, t["label"], col, "start"))
    for s in states:
        x, y = pos[s["id"]]
        fill, stroke = COL.get(s.get("kind", "normal"), COL["normal"])
        o.append(f'<rect x="{x}" y="{y}" width="{W_BOX}" height="{H_BOX}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
        o.append(f'<text x="{x + W_BOX / 2}" y="{y + 30}" font-size="17" font-weight="800" fill="{stroke}" text-anchor="middle">{esc(s["id"])}</text>')
        if s.get("note"):
            o.append(f'<text x="{x + W_BOX / 2}" y="{y + 54}" font-size="12.5" fill="#333" text-anchor="middle">{esc(s["note"][:34])}</text>')
        if s.get("outputs"):
            o.append(f'<text x="{x + W_BOX / 2}" y="{y + 76}" font-size="11.5" fill="#666" text-anchor="middle">{esc(s["outputs"][:36])}</text>')
    for lx, ly, text, col, anchor in labels:
        w = len(text) * 6.4 + 10
        bx = lx - w / 2 if anchor == "middle" else lx - 4
        o.append(f'<rect x="{bx:.0f}" y="{ly - 13:.0f}" width="{w:.0f}" height="18" rx="4" fill="#fff" opacity="0.92"/>')
        o.append(f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="12" fill="{col}" text-anchor="{anchor}">{esc(text)}</text>')
    o.append("</svg>")
    return "\n".join(o)


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    txt = open(sys.argv[1], encoding="utf-8").read()
    import re
    txt = re.sub(r"//[^\n]*", "", txt)
    open(sys.argv[2], "w", encoding="utf-8").write(render(json.loads(txt)))


if __name__ == "__main__":
    utf8_stdio()
    main()
