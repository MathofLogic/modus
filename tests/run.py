#!/usr/bin/env python3
"""
tests/run.py — the gate for /modus.
==========================================================================
Green means: all checks pass; the named findings are present and say
what the README says; the engine enforces its riders; the claims
ledger is covered; verify.py exits 0; the manifest replays; the demo
runs; the analysis document's check references all exist.
"""
import json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from modus import CHECKS, replay, PAID
from modus.core import run_claim
from modus.carriers import CARRIERS, sweep, inverter_battery
from modus.claims import ALL, SECTIONS
from modus import engine as E

failures = []


def gate(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" — {detail}" if detail else ""))
    if not ok:
        failures.append(name)


print("\n== 1. every check passes ==")
bad = []
for n, f in sorted(CHECKS.items()):
    try:
        ok, _, ev = f()
    except Exception as e:
        ok, ev = False, str(e)
    if not ok:
        bad.append((n, ev[:60]))
gate(f"all {len(CHECKS)} checks", not bad, str(bad))

print("\n== 2. the findings say what the README says ==")
gate("detachment dies exactly at glut designation (LP, L3+, FOUR) and "
     "nowhere else",
     {n for n in CARRIERS if sweep(n)[0] is not None}
     == {"LP", "L3+", "FOUR"})
bat = inverter_battery("POST4")
gate("POST4: MT valid + trigger fails precision AND completeness",
     sweep("POST4")[1] is None and not bat["precision"]
     and not bat["completeness"])
gate("LP and L3+ share exact witnesses (1/2,0) and (1,1/2)",
     sweep("LP") == sweep("L3+"))

print("\n== 3. the engine enforces its riders ==")
try:
    E.detach(E.mint("x", "FORCED"),
             E.certify("y", "z", "FORCED"))
    gate("equivocation refused", False)
except E.EquivocationError:
    gate("equivocation refused", True)
t = E.detach(E.mint("a", "EMPIRICAL", riders={"r1"}),
             E.certify("a", "b", "STIPULATED", riders={"r2"}))
gate("weakest link + rider union",
     t.tier == "STIPULATED" and t.riders == frozenset({"r1", "r2"}))
gate("clean detachment is FORCED-and-rider-free only",
     E.mint("m", "FORCED").clean() and not t.clean()
     and not E.mint("m2", "FORCED", riders={"r"}).clean())

print("\n== 4. ledger coverage and accounting ==")
naked = [c for c in ALL if not c.get("check") and not c.get("cite")]
gate("every ledger claim has a check or a citation", not naked)
missing = [c["check"] for c in ALL
           if c.get("check") and c["check"] not in CHECKS]
gate("every referenced check exists", not missing, str(missing))
results = [run_claim(c) for c in ALL]
paid = sum(1 for r in results if r["tier"] in PAID and r["ok"])
gate("document paid fraction > 50%", paid / len(results) > 0.5,
     f"{paid}/{len(results)} = {100 * paid / len(results):.1f}%")
unused = set(CHECKS) - {c.get("check") for c in ALL}
gate("every check is cited by the ledger", not unused, str(unused))

print("\n== 5. verify.py, manifest, demo ==")
p = subprocess.run([sys.executable, str(ROOT / "verify.py")],
                   capture_output=True, text=True)
gate("verify.py exits 0", p.returncode == 0)
gate("prints the paid fraction", "DOCUMENT PAID FRACTION" in p.stdout)
man = json.loads((ROOT / "manifests" / "modus_manifest.json").read_text())
gate("manifest replays intact", replay(man), f"{len(man)} seals")
d = subprocess.run([sys.executable, str(ROOT / "demos" / "pipeline.py")],
                   capture_output=True, text=True)
gate("demo runs and routes to the riders",
     d.returncode == 0 and "primary suspect(s): rider:" in d.stdout
     and "classical MT recovered" in d.stdout)

print("\n== 6. ANALYSIS.md references resolve ==")
txt = (ROOT / "ANALYSIS.md").read_text()
refs = set(re.findall(r"\[FORCED — `([a-z0-9_]+)`", txt)) \
     | set(re.findall(r"\[EMPIRICAL — `([a-z0-9_]+)`", txt))
dangling = [r for r in refs if r not in CHECKS]
gate("every check tag in the document names a real check",
     not dangling, str(dangling))

print()
if failures:
    print(f"GATE: RED — {failures}")
    sys.exit(1)
print(f"GATE: GREEN — {len(CHECKS)} checks, {paid}/{len(results)} "
      f"ledger claims paid ({100 * paid / len(results):.1f}%), engine "
      "riders enforced, manifest sealed and replayed.")
