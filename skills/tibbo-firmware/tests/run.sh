#!/bin/sh
# Regression: expected exit codes of tps_check.py on sample configs
cd "$(dirname "$0")/.." || exit 2
fail=0
for pair in "autowater 0" "bad_poe_m2_in_s11 1" "gallery_tpp3 0" "gallery_tpp2 0" "good_tpp2 0" "adc_lte 0" "bad_24v 1" "bad_terminal 1"; do
  set -- $pair
  python3 scripts/tps_check.py check "tests/$1.json" >/dev/null; rc=$?
  if [ "$rc" != "$2" ]; then echo "FAIL $1: exit $rc, expected $2"; fail=1; else echo "ok   $1"; fi
done
T=$(mktemp -d)
python3 scripts/state_diagram.py tests/autowater.fsm.json "$T/fsm.svg" && grep -q "<svg" "$T/fsm.svg" && echo "ok   state_diagram" || { echo "FAIL state_diagram"; fail=1; }
python3 scripts/tps_check.py check tests/gallery_tpp3.json --svg "$T/b.svg" >/dev/null && grep -q "Подключение к CPU" "$T/b.svg" && echo "ok   board svg" || { echo "FAIL board svg"; fail=1; }
python3 scripts/tps_check.py board "TPP2W(G2)" | grep -q "PL_IO_NUM_9_TX0" && echo "ok   board cmd" || { echo "FAIL board cmd"; fail=1; }
python3 scripts/tps_check.py find rs485 | grep -q "#05" && echo "ok   find cmd" || { echo "FAIL find cmd"; fail=1; }
python3 scripts/tps_check.py tibbit 12 | grep -q '"model": "12"' && echo "ok   tibbit cmd" || { echo "FAIL tibbit cmd"; fail=1; }
rm -rf "$T"
exit $fail
