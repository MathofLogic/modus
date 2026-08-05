#!/usr/bin/env python3
"""
demos/pipeline.py — one inference, run twice.
==========================================================================
First the classical way (tokens bare, riders invisible, blame
pre-addressed), then with the meter running (modus.engine). Same
premises, same failure — different invoices.

The story: a thermal-management pipeline. A sensor reads 92C, the spec
says 90C is 'overheating', firmware is supposed to throttle when
overheating. The throttle does not engage. Who gets refuted?
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from modus import engine as E

print("\n== the classical run ==")
print("  A:      'core is overheating'                (true)")
print("  A -> B: 'overheating -> throttle engages'    (true)")
print("  MP:     B. 'throttle engages'                (detached, clean)")
print("  ...observation: throttle did NOT engage.")
print("  MT:     therefore NOT-A: 'core is not overheating'.")
print("  The 92C reading is now formally overruled by two 'true' "
      "premises.\n  Nothing on the page says which premise was minted "
      "from a spec revision.\n")

print("== the metered run ==")
reading = E.mint("sensor reads 92C", "EMPIRICAL",
                 evidence="calibrated 2026-06 rig, +/-0.5C")
classify = E.certify("sensor reads 92C", "core is overheating",
                     "CONDITIONAL", degree=0.98,
                     riders={"threshold=90C per spec rev3"},
                     evidence="margin 2C ~ 4 sigma of sensor noise")
behave = E.certify("core is overheating", "throttle engages",
                   "CONDITIONAL", degree=0.99,
                   riders={"firmware 2.1 behavior"},
                   evidence="bench-tested on firmware 2.1")

hot = E.detach(reading, classify)
throttle = E.detach(hot, behave)

print(f"  minted:   {reading.claim!r}  [{reading.tier}]")
print(f"  detach 1: {hot.claim!r}  [{hot.tier}] degree>="
      f"{hot.degree:.2f}  riders={sorted(hot.riders)}")
print(f"  detach 2: {throttle.claim!r}  [{throttle.tier}] degree>="
      f"{throttle.degree:.2f}")
print(f"            riders={sorted(throttle.riders)}")
print(f"            clean (classical) detachment available? "
      f"{throttle.clean()} — riders are conserved, not dropped\n")

not_b = E.mint("throttle did NOT engage", "EMPIRICAL",
               evidence="observed on the bench, twice")
print(str(E.route_refutation(behave, hot, not_b)))
print("\n  The 92C reading and the arithmetic keep their tiers. The "
      "refutation lands on\n  the STIPULATED riders first — the spec "
      "revision and the firmware assumption —\n  which is where "
      "post-mortems find these bugs anyway. The engine just sends\n"
      "  the invoice to that address on the first pass.\n")

print("== and the degenerate case, for honesty ==")
a = E.mint("A", "FORCED")
c = E.certify("A", "B", "FORCED")
print(str(E.route_refutation(c, a, E.mint("not B", "FORCED"))))
print()
