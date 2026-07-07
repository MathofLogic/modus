#!/usr/bin/env python3
"""
verify.py — /modus entry point.
==========================================================================
Prints the MP/MT sweep table, the inverter battery, the detachment-leak
meter, and then runs the CLAIMS LEDGER: every load-bearing claim of
ANALYSIS.md, checked live or cited honestly. The document's own paid
fraction is computed and sealed. Any failing check exits 1.
"""
import json, pathlib, sys, time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from modus.core import run_claim, seal, replay, PAID
from modus.carriers import CARRIERS, sweep, inverter_battery
from modus.leak import sorites
from modus.claims import SECTIONS


def main():
    t0 = time.time()
    print("\n  MODUS — detachment and refutation, priced")
    print("  MP and MT as designation-closure properties of (V, G, "
          "theta); every claim tiered.\n")

    print("  == the sweep " + "=" * 55)
    print(f"  {'carrier':<8} {'MP':<16} {'MT':<16} "
          f"{'inverter battery (inv/snd/prec/comp)'}")
    for name in CARRIERS:
        mp, mt = sweep(name)
        bat = inverter_battery(name)
        b = "".join("Y" if bat[k] else "." for k in
                    ("involution", "soundness", "precision",
                     "completeness"))
        pw = lambda w: "(" + ",".join(str(x) for x in w) + ")"
        f = lambda w: "holds" if w is None else f"FAILS {pw(w)}"
        note = ""
        if name == "POST4":
            note = "  <- valid, meaningless"
        print(f"  {name:<8} {f(mp):<16} {f(mt):<16} [{b}]{note}")

    print("\n  == the leak meter (each certificate 99.9%) " + "=" * 25)
    print("  " + "   ".join(f"n={k}: >={g:.3f}" for k, g in
                            sorites(1000, 0.999)))

    print("\n  == the claims ledger (ANALYSIS.md, priced) " + "=" * 25)
    chain, fails = [], []
    paid = total = 0
    for section, claims in SECTIONS:
        s_paid = 0
        results = [run_claim(c) for c in claims]
        for r in results:
            total += 1
            if r["ok"] is False:
                fails.append(r)
            if r["tier"] in PAID and r["ok"]:
                paid += 1
                s_paid += 1
        print(f"\n  -- {section}  [{s_paid}/{len(claims)} paid]")
        for r in results:
            flag = ("PASS" if r["ok"] else
                    "FAIL" if r["ok"] is False else "cite")
            print(f"   [{flag}][{r['tier'][:4]}] {r['claim'][:64]}")
        seal({"section": section, "claims": len(claims),
              "paid": s_paid}, chain)

    frac = 100 * paid / total
    body = {"claims": total, "paid": paid,
            "paid_fraction": round(frac, 1),
            "verdict": ("PASS" if not fails else "FAIL") + "/STIPULATED",
            "non_claims": [
                "NOT claimed: that classical logic is wrong — it is the "
                "correct carrier wherever the riders are enforced by "
                "construction, i.e. mathematics.",
                "NOT claimed: that MP fails 'in reality' — it fails in "
                "specifiable configurations, witnesses printed above.",
                "NOT claimed: that the philosophical attributions are "
                "settled — they are PRESUMED framings; the enumerations "
                "stand without them.",
                "NOT claimed: that weakest-tier-first routing is the "
                "unique correct blame assignment — it is a declared "
                "policy, explicit where the classical default is "
                "implicit."]}
    seal(body, chain)
    out = pathlib.Path(__file__).parent / "manifests"
    out.mkdir(exist_ok=True)
    (out / "modus_manifest.json").write_text(json.dumps(chain, indent=1))

    print("\n  " + "=" * 68)
    print(f"  DOCUMENT PAID FRACTION: {paid}/{total} claims "
          f"machine-decided here = {frac:.1f}%")
    print(f"  verdict {body['verdict']}   chain {len(chain)} sealed, "
          f"replay={'intact' if replay(chain) else 'BROKEN'}   "
          f"{time.time() - t0:.2f}s")
    for nc in body["non_claims"]:
        print(f"  {nc}")
    print()
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
