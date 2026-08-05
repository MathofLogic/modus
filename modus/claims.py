"""
modus.claims — the ledger for ANALYSIS.md.
==========================================================================
Every load-bearing claim in the analysis document, as a record: either
it names a check (run by verify.py on every build) or it carries a
citation and its honest tier. verify.py computes the DOCUMENT'S OWN
PAID FRACTION from this ledger — the analysis is subject to the same
accounting it performs on the two rules.
"""

SECTIONS = [
 ("Mechanics of detachment", [
  dict(claim="MP/MT validity across nine carriers: survives CL2, K3, "
             "L3, G3, WK3, POST4; dies in LP, L3+, FOUR",
       check="sweep_nine_carriers"),
  dict(claim="Designating the glut — not the choice of conditional — "
             "kills detachment: LP and L3+ share witnesses exactly",
       check="glut_kills_detachment"),
  dict(claim="The gap protects detachment: K3 and WK3 keep both rules",
       check="gap_protects_detachment"),
  dict(claim="MP is residuation read back: T(a, a->b) = min(a,b) for "
             "Lukasiewicz, exactly; inequalities for Godel and product",
       check="residuation_identity"),
  dict(claim="Under BHK, MP is function application with a step count",
       cite="Curry-Howard; PAID in carriersets "
            "lambda_church_rosser_bounded (Church 2+2 -> 4 by counted "
            "beta steps); inherited here"),
  dict(claim="MP is the sole rule of motion of Hilbert systems",
       cite="Frege 1879; Hilbert & Ackermann 1928"),
 ]),
 ("Mechanics of the inverter", [
  dict(claim="MT is composition into the absurdity sink; it survives "
             "the loss of classical negation while the MP/MT mirror "
             "does not (mirror drops to 1/2 at (1,1/2))",
       check="mirror_asymmetry_3chain"),
  dict(claim="Inverter fitness is a four-test battery separate from "
             "schema validity, decided for all nine negations",
       check="inverter_battery_table"),
  dict(claim="POST4: MT schema-valid yet meaningless — the trigger "
             "never arms on genuine falsity and arms on 2/3",
       check="post4_valid_but_meaningless"),
  dict(claim="MT's trigger is a theta policy: in K3 an unverified "
             "prediction refutes nothing; only measured falsity arms it",
       check="k3_trigger_policy"),
 ]),
 ("Quantitative regime", [
  dict(claim="Each graded detachment leaks 1 - degree(certificate); "
             "1000 steps at 99.9%% guarantee exactly 0 — the sorites "
             "is the leak compounding", check="leak_bound_sorites"),
  dict(claim="Bivalence relocates the leak into the tokenization step "
             "rather than removing it",
       cite="corollary of leak_bound_sorites plus the Boundary Law "
            "(PAID in carriersets boundary_law_scaling, slope ~2 "
            "measured); inherited here"),
  dict(claim="Probability prices the rules asymmetrically: bounded "
             "lift for MP (0.667), total refutation for MT (0.000) "
             "from a degree-1 conditional", check="probability_asymmetry"),
  dict(claim="Popper's falsificationist asymmetry, as a framing of "
             "that arithmetic", cite="Popper 1934"),
 ]),
 ("Reification and the riders", [
  dict(claim="The rule reified as a premise never detaches: 5 rounds, "
             "7 premises, no B — G is not V", check="tortoise_regress"),
  dict(claim="Attribution of the regress", cite="Carroll 1895"),
  dict(claim="The atomic sentence is already a recorded gradient "
             "output (function/argument replacing subject/predicate)",
       cite="Frege 1879, 1892"),
  dict(claim="Predicate minting has a measured price diverging at the "
             "boundary", cite="the Boundary Law, carriersets "
            "boundary_law_scaling (EMPIRICAL there)", tier="CONDITIONAL"),
  dict(claim="What ~B refutes is the conjunction of A with the riders "
             "(underdetermination)", cite="Duhem 1906; Quine 1951"),
 ]),
 ("The truth presumption", [
  dict(claim="Truth reified as an object (das Wahre) is a formal "
             "design decision, not a metaphor", cite="Frege 1892"),
  dict(claim="Cut elimination pays off every deferred detachment; the "
             "payoff can be non-elementary",
       cite="Gentzen 1935; Statman 1978"),
  dict(claim="Tarskian truth is relational; fixing the intended model "
             "and deleting the parameter is the intrinsic-truth move; "
             "the parameter is unrecoverable from tokens",
       cite="Tarski 1936; Godel 1930; Skolem 1920 — satisfaction "
            "executed in carriersets tarski_satisfaction_finite"),
  dict(claim="LP's loss of detachment is the priced cost of "
             "paraconsistency", cite="Priest 1979 — independently "
            "re-derived by glut_kills_detachment"),
 ]),
 ("The engine (inference with the meter running)", [
  dict(claim="Tier composes by weakest link through detach()",
       check="engine_weakest_link"),
  dict(claim="Riders are conserved through detachment; clean "
             "detachment is a FORCED-and-rider-free privilege",
       check="engine_rider_conservation"),
  dict(claim="Rider 1 (token identity) is enforced at the type level: "
             "equivocation raises", check="engine_refuses_equivocation"),
  dict(claim="The engine's chained degrees match the Lukasiewicz "
             "bound: the sorites meter runs inside detach()",
       check="engine_leak_accounting"),
  dict(claim="MT routes refutation weakest-tier-first and recovers "
             "classical MT as the all-FORCED degenerate case",
       check="engine_routing_weakest_first"),
  dict(claim="Weakest-tier-first is the right default routing policy",
       tier="STIPULATED",
       cite="declared, not derived — explicit where the classical "
            "default (always blame the antecedent) is implicit"),
 ]),
]

ALL = [c for _, cs in SECTIONS for c in cs]
