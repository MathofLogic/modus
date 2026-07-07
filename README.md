# modus

**Modus ponens is not a law of thought — it is a designation-closure property of one configuration of (V, G, θ), decided here by complete enumeration across nine carriers; and modus tollens' validity is measurably independent of its *meaning*, which lives in the negation gradient and is tested by a four-check inverter battery. Then the repo builds the thing the analysis demands: a detachment engine with the meter running.**

```
$ python verify.py

  == the sweep ==================================================
  carrier  MP             MT             inverter (inv/snd/prec/comp)
  CL2      holds          holds          [YYYY]
  K3       holds          holds          [YYYY]
  LP       FAILS (1/2,0)  FAILS (1,1/2)  [Y..Y]
  L3+      FAILS (1/2,0)  FAILS (1,1/2)  [Y..Y]
  G3       holds          holds          [.YYY]
  POST4    holds          holds          [.Y..]  <- valid, meaningless
  FOUR     FAILS (B,N)    FAILS (N,B)    [Y..Y]

  n=100: >=0.900   n=500: >=0.500   n=1000: >=0.000
  DOCUMENT PAID FRACTION: 16/29 claims machine-decided = 55.2%
```

## The findings (measured, witnesses printed)

**Detachment dies exactly where the glut is designated, and nowhere else.** LP and Ł3⁺ lose MP and MT with the *identical witnesses* — (½,0) and (1,½) — despite running different conditionals; FOUR repeats it at (B,N)/(N,B). Designation, not the t-norm, is the culprit, and the gap (K3, WK3) provably protects: an undesignated middle contaminates values but never forges a certificate. [FORCED — `sweep_nine_carriers`, `glut_kills_detachment`, `gap_protects_detachment`]

**MP is residuation read back.** T(a, a→b) = min(a, b) for Łukasiewicz, *exactly*, at all 441 grid points — the conditional is minted to be precisely cashable, and detachment delivers the weakest link by definition. The bound is tight: equality whenever b ≤ a. [FORCED — `residuation_identity`]

**MT's validity and MT's meaning are independent axes.** The inverter battery (involution / trigger soundness / precision / completeness) is decided for all nine negations. POST4 is the exhibit: the MT schema is **valid** by complete enumeration while its trigger fails precision *and* completeness — it arms on b = 2/3 and never on the genuine counterexample b = 0. A valid rule that cannot, even once, mean refutation. [FORCED — `inverter_battery_table`, `post4_valid_but_meaningless`]

**The sorites is the detachment leak, compounding.** Each graded MP leaks 1−degree(certificate); 1000 chained steps at 99.9% guarantee exactly 0.000. Bivalence doesn't remove this meter — it relocates the bill into the unpriced tokenization step. [FORCED — `leak_bound_sorites`]

**MT survives the loss of classical negation; the MP/MT mirror does not.** On the 3-chain Heyting algebra MT is valid at all nine points and equals composition-into-⊥ (a transitivity instance); the classical mirror (¬b→¬a)→(a→b) drops to ½ at (1,½). The symmetry was purchased by involutive negation, not by inference. [FORCED — `mirror_asymmetry_3chain`]

**Confirmation accrues, refutation detonates.** With P(B|A)=1: observing B lifts A to 0.667; observing ¬B drops it to exactly 0.000. Popper's asymmetry as carrier arithmetic — and the reason the MathofLogic method needs full enumeration for "Forces" and one witness for "Breaks". [EMPIRICAL — `probability_asymmetry`]

**The rule is not a token.** Carroll's regress, mechanized: reify MP as a premise, five rounds, seven premises, B never detaches. G is not V. [FORCED — `tortoise_regress`]

## The engine

`modus/engine.py` is the constructive payload: MP and MT with the classical presentation's three unpriced riders put back on the instrument.

```python
from modus import engine as E

reading  = E.mint("sensor reads 92C", "EMPIRICAL")
classify = E.certify("sensor reads 92C", "core is overheating",
                     "CONDITIONAL", degree=0.98,
                     riders={"threshold=90C per spec rev3"})
hot = E.detach(reading, classify)   # tier: weakest link; riders: conserved;
                                    # degree: Lukasiewicz-metered;
                                    # equivocation: raises at the type level
E.route_refutation(...)             # MT as tier-routed auditing —
                                    # weakest suspect eats it first;
                                    # all-FORCED recovers classical MT
```

Rider 1 (token identity) is enforced — `detach()` raises `EquivocationError` on a mismatched middle term. Rider 2 (the threshold/degree) is metered — chained degrees match the Łukasiewicz bound exactly. Rider 3 (currency/context) is conserved — stipulations union through every detachment, and *clean* classical detachment is a privilege granted only to FORCED, rider-free tokens. Refutation routes weakest-tier-first (Duhem–Quine with a chart of accounts) and collapses to classical MT when everything is FORCED. [FORCED — the five `engine_*` checks] `demos/pipeline.py` runs one inference twice — classical and metered — and prints both invoices.

## The numbers

| | |
|---|---|
| Executable checks | **16**, suite ~0.2 s |
| Carriers swept | 9, MP and MT decided by complete enumeration |
| Inverter battery | 4 tests × 9 negations, all decided |
| ANALYSIS.md ledger | **29 claims, 16 machine-decided (55.2% paid)** — the rest PRESUMED with citations (Frege, Carroll, Popper, Duhem–Quine, Gentzen–Statman, Tarski, Priest) or STIPULATED (the routing policy, declared) |
| Manifest | 7 hash-chained seals, byte-replayable |

## Layout

```
ANALYSIS.md           the full analysis: mechanics, the reification of
                      subject-predicate process outputs, and what the
                      presumption of truth-as-intrinsic-discrete-
                      discoverable actually buys (spoiler: not
                      inference — inference at zero marginal cost)
verify.py             sweep + battery + leak meter + the claims ledger
                      pricing the document itself; sealed manifest
modus/carriers.py     nine configurations, the MP/MT decision
                      procedure, the inverter battery
modus/leak.py         residuation, the leak bound, the sorites,
                      the probabilistic asymmetry
modus/engine.py       the provenance-carrying detachment engine
modus/claims.py       the ledger: every ANALYSIS claim, checked or cited
demos/pipeline.py     the same inference, classical vs metered
tests/run.py          the gate
```

## Relation to the other MathofLogic repos

- **[/carriersets](../carriersets)** — the library this analysis walks through; kernel-parity on the LP and K3 signatures is checked there (`lp_signature`, `k3_signature`).
- **[/PL](../PL)** — the kernel whose 15-law vocabulary (MP included) the sweep speaks.
- **[/rigor](../rigor)** / **[/PL-Verify](../PL-Verify)** — the tier discipline and the verdict cap ("/STIPULATED") that `engine.py` generalizes into rider conservation.

## Run it

```bash
python verify.py          # everything, priced, sealed
python tests/run.py       # the gate
python demos/pipeline.py  # both invoices
```

No dependencies beyond the standard library.

## Non-claims

Not claimed: that classical logic is wrong — it is the correct carrier wherever the riders are enforced by construction, which is mathematics, and pricing them at zero there is accurate. Not claimed: that MP fails "in reality" — it fails in specifiable configurations with witnesses printed above. Not claimed: that the philosophical attributions are settled — they are PRESUMED framings, and the enumerations stand without them. Not claimed: that weakest-tier-first routing is the uniquely correct blame assignment — it is a declared policy, explicit where the classical default is implicit.

MIT license. Trust infrastructure should not be paywalled.
