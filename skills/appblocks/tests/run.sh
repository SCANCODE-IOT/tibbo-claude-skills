#!/bin/sh
# Offline regression for ab_tool.py on bundled example projects (no network, no key)
cd "$(dirname "$0")/.." || exit 2
fail=0; T=$(mktemp -d)
for f in examples/*.json; do
  python3 scripts/ab_tool.py check "$f" >/dev/null || { echo "FAIL check $f"; fail=1; }
  python3 scripts/ab_tool.py summary "$f" | grep -q "Плата:" || { echo "FAIL summary $f"; fail=1; }
  python3 scripts/ab_tool.py flow "$f" "$T/f.svg" && grep -q "<svg" "$T/f.svg" || { echo "FAIL flow $f"; fail=1; }
  python3 scripts/ab_tool.py tps "$f" --vin 24 --out "$T/c.json" && grep -q '"board"' "$T/c.json" || { echo "FAIL tps $f"; fail=1; }
done
[ "$fail" = 0 ] && echo "ok   ab_tool on $(ls examples/*.json | wc -l) examples"
n=$(python3 scripts/ab_tool.py ids 3 | sort -u | wc -l); [ "$n" = 3 ] && echo "ok   ids unique" || { echo "FAIL ids"; fail=1; }
# regression (Oct 2026): references inside Web Console and the Update Interval minimum must be caught
python3 - "$T" <<'PY' || fail=1
import json, sys, subprocess
T = sys.argv[1]
p = json.load(open("examples/accesscontrol6.json"))
for f in p["features"]:
    if f["id"] == "stg":
        f["settings"]["SETTINGS"] = [x for x in f["settings"]["SETTINGS"] if x["settings"]["SETTINGID"] != "lock_activation_duration"]
    if f["id"] == "commands":
        f["settings"]["COMMANDS"] = []
    if f["id"] == "global_vars":
        f["settings"]["INTERVAL"] = "0.1"
json.dump(p, open(T + "/bad.json", "w"))
out = subprocess.run(["python3", "scripts/ab_tool.py", "check", T + "/bad.json"], capture_output=True, text=True).stdout
need = ["SETTINGID=lh8ofi29e1ipb5hcn9n", "VARIABLE=lh8r5ppokuuzhvk8hbh", "INTERVAL=0.1"]
miss = [n for n in need if n not in out]
print("ok   panel/interval regression" if not miss else "FAIL panel/interval regression: " + ", ".join(miss))
sys.exit(1 if miss else 0)
PY
TPS=$(ls ../tibbo-firmware/scripts/tps_check.py 2>/dev/null)
if [ -n "$TPS" ]; then
  python3 scripts/ab_tool.py tps examples/ModbusMQTTGateway.json --vin 24 --out "$T/m.json"
  python3 "$TPS" check "$T/m.json" >/dev/null && echo "ok   bridge to tps_check" || { echo "FAIL bridge"; fail=1; }
fi
rm -rf "$T"; exit $fail
