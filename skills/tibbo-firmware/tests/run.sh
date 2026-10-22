#!/bin/sh
# Regression: expected exit codes of tps_check.py on sample configs
cd "$(dirname "$0")/.." || exit 2
# python3 on Linux/macOS, python on Windows (Git Bash); override with PY=...
if [ -z "$PY" ]; then if python3 -c "" >/dev/null 2>&1; then PY=python3; else PY=python; fi; fi
fail=0
for pair in "autowater 0" "bad_poe_m2_in_s11 1" "gallery_tpp3 0" "gallery_tpp2 0" "good_tpp2 0" "adc_lte 0" "bad_24v 1" "bad_terminal 1"; do
  set -- $pair
  "$PY" scripts/tps_check.py check "tests/$1.json" >/dev/null; rc=$?
  if [ "$rc" != "$2" ]; then echo "FAIL $1: exit $rc, expected $2"; fail=1; else echo "ok   $1"; fi
done
T=$(mktemp -d)
"$PY" scripts/state_diagram.py tests/autowater.fsm.json "$T/fsm.svg" && grep -q "<svg" "$T/fsm.svg" && echo "ok   state_diagram" || { echo "FAIL state_diagram"; fail=1; }
"$PY" scripts/tps_check.py check tests/gallery_tpp3.json --svg "$T/b.svg" >/dev/null && grep -q "Подключение к CPU" "$T/b.svg" && echo "ok   board svg" || { echo "FAIL board svg"; fail=1; }
"$PY" scripts/tps_check.py board "TPP2W(G2)" | grep -q "PL_IO_NUM_9_TX0" && echo "ok   board cmd" || { echo "FAIL board cmd"; fail=1; }
"$PY" scripts/tps_check.py find rs485 | grep -q "#05" && echo "ok   find cmd" || { echo "FAIL find cmd"; fail=1; }
"$PY" scripts/tps_check.py tibbit 12 | grep -q '"model": "12"' && echo "ok   tibbit cmd" || { echo "FAIL tibbit cmd"; fail=1; }
out=$("$PY" scripts/tps_check.py check tests/editor_rules.json)
echo "$out" | grep -q "RF-разъём #37 в S13" && echo "$out" | grep -q "два #21 в S2 и S4" && echo "$out" | grep -q "#02 занимает два M-сокета" \
  && echo "ok   editor socket rules" || { echo "FAIL editor socket rules"; fail=1; }
# a cp1251 console (Windows) must not break the output: run without PYTHONUTF8
encfail=0
for cmd in "check tests/gallery_tpp3.json" "board TPP3W(G2)" "find реле" "tibbit 12"; do
  env -u PYTHONUTF8 PYTHONIOENCODING=cp1251 "$PY" scripts/tps_check.py $cmd >/dev/null 2>"$T/err" || { echo "FAIL cp1251 console: tps_check.py $cmd"; cat "$T/err"; encfail=1; }
done
[ "$encfail" = 0 ] && echo "ok   non-UTF-8 console" || fail=1
rm -rf "$T"
exit $fail
