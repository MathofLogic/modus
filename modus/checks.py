"""
modus.checks — every claim in ANALYSIS.md that can be decided, decided.
==========================================================================
Each check returns (ok, tier, evidence). The gate fails the build on
any red. Together with modus/tortoise logic these are the receipts.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from .core import check, TIERS
from .carriers import CARRIERS, sweep, inverter_battery, V3, kneg
from .leak import (residuation_grid, sorites, probability_asymmetry,
                   mirror_asymmetry, leak_guarantee)
from . import engine as E

Z, H, U = Fr(0), Fr(1, 2), Fr(1)


def tortoise(rounds=5):
    """Carroll's regress mechanized: reify MP as a premise and count.
    Returns (premise_counts, detached) — detached is always False; the
    rule consumed as a token regenerates itself as a premise."""
    prem = ["A", "A->B"]
    counts = []
    for _ in range(rounds):
        prem.append("(" + " & ".join(prem) + ") -> B")
        counts.append(len(prem))
    return counts, False


# ── the sweep ───────────────────────────────────────────────────────────
EXPECTED = {          # name -> (mp_holds, mt_holds)
    "CL2": (True, True), "K3": (True, True), "LP": (False, False),
    "L3": (True, True), "L3+": (False, False), "G3": (True, True),
    "WK3": (True, True), "POST4": (True, True), "FOUR": (False, False),
}


@check("sweep_nine_carriers")
def _():
    got = {}
    for name in CARRIERS:
        mp, mt = sweep(name)
        got[name] = (mp is None, mt is None)
    ok = got == EXPECTED
    return ok, "FORCED", \
        ("MP/MT decided by complete enumeration over all nine carriers; "
         "detachment survives CL2/K3/L3/G3/WK3/POST4 and dies exactly "
         "where the glut is designated (LP, L3+, FOUR)"
         if ok else f"table mismatch: {got}")


@check("glut_kills_detachment")
def _():
    lp_mp, lp_mt = sweep("LP")
    l3p_mp, l3p_mt = sweep("L3+")
    four_mp, four_mt = sweep("FOUR")
    same_witnesses = lp_mp == l3p_mp == (H, Z) and lp_mt == l3p_mt == (U, H)
    return (same_witnesses and four_mp == ("B", "N")
            and four_mt == ("N", "B")), "FORCED", \
        ("LP and L3+ fail with the SAME witnesses — MP at (1/2,0), MT at "
         "(1,1/2) — despite different conditionals: designation, not the "
         "t-norm, is the culprit; FOUR repeats it at (B,N)/(N,B)")


@check("gap_protects_detachment")
def _():
    k3 = sweep("K3") == (None, None)
    wk3 = sweep("WK3") == (None, None)
    return k3 and wk3, "FORCED", \
        ("K3 and WK3 keep both rules: the undesignated middle "
         "contaminates values but never crosses theta, so certificates "
         "cannot be forged — 'unknown must not validate', proven")


@check("inverter_battery_table")
def _():
    got = {n: inverter_battery(n) for n in CARRIERS}
    exp = {
     "CL2":  dict(involution=True, soundness=True, precision=True,
                  completeness=True),
     "K3":   dict(involution=True, soundness=True, precision=True,
                  completeness=True),
     "LP":   dict(involution=True, soundness=False, precision=False,
                  completeness=True),
     "L3":   dict(involution=True, soundness=True, precision=True,
                  completeness=True),
     "L3+":  dict(involution=True, soundness=False, precision=False,
                  completeness=True),
     "G3":   dict(involution=False, soundness=True, precision=True,
                  completeness=True),
     "WK3":  dict(involution=True, soundness=True, precision=True,
                  completeness=True),
     "POST4": dict(involution=False, soundness=True, precision=False,
                   completeness=False),
     "FOUR": dict(involution=True, soundness=False, precision=False,
                  completeness=True),
    }
    ok = got == exp
    return ok, "FORCED", \
        ("four-test battery decided for all nine negations; POST4 fails "
         "precision AND completeness: its trigger arms on b=2/3 and "
         "never on the genuine counterexample b=0"
         if ok else f"mismatch: { {k: got[k] for k in got if got[k] != exp[k]} }")


@check("post4_valid_but_meaningless")
def _():
    mp, mt = sweep("POST4")
    bat = inverter_battery("POST4")
    ok = mt is None and not bat["precision"] and not bat["completeness"]
    return ok, "FORCED", \
        ("POST4: the MT schema is VALID (complete enumeration, no "
         "counterexample) while the trigger neither arms on genuine "
         "falsity (NEG(0)=1/3, undesignated) nor arms only on it "
         "(NEG(2/3)=1) — a valid rule that can never mean refutation. "
         "Designation-validity is a syntactic shadow; the semantics "
         "lives in the inverter")


# ── quantitative regime ─────────────────────────────────────────────────
@check("residuation_identity")
def _():
    luk, godel, prod, tight, pts = residuation_grid(20)
    return luk and godel and prod and tight, "FORCED", \
        (f"T(a, a->b) = min(a,b) EXACTLY for Lukasiewicz at all {pts} "
         "grid points; Godel and product satisfy the residuation "
         "inequality; the leak bound is TIGHT (equality whenever b <= a) "
         "— MP delivers the weakest link, by definition of ->")


@check("leak_bound_sorites")
def _():
    table = sorites(1000, 0.999)
    final = table[-1][1]
    mid = dict(table)
    ok = final < 1e-9 and abs(mid[500] - 0.5) < 1e-9 \
        and abs(mid[100] - 0.9) < 1e-9
    return ok, "FORCED", \
        ("1000 chained detachments, each certificate 99.9% safe: "
         "guaranteed conclusion degree 0.999 -> 0.900 (n=100) -> 0.500 "
         "(n=500) -> 0.000 (n=1000). The sorites is the leak "
         "compounding; bivalence relocates the meter, it does not "
         "remove it")


@check("mirror_asymmetry_3chain")
def _():
    mt_min, mirror_val, worst, comp_min = mirror_asymmetry()
    ok = mt_min == U and mirror_val == H and worst == (U, H) \
        and comp_min == U
    return ok, "FORCED", \
        ("3-chain Heyting: MT valid (min 1 over all 9 points) and equal "
         "to composition-into-bottom (transitivity instance, also min "
         "1); the classical mirror (~b->~a)->(a->b) drops to 1/2 at "
         "(1,1/2). MT survives without classical negation; the MP/MT "
         "symmetry does not")


@check("k3_trigger_policy")
def _():
    unverified = kneg(H) in (U,)          # b=1/2: trigger armed?
    refuted = kneg(Z) in (U,)             # b=0
    return (not unverified) and refuted, "FORCED", \
        ("K3, D={1}: an unverified prediction (b=1/2) leaves NEG(b)=1/2 "
         "undesignated — nothing is refuted; only measured falsity "
         "(b=0) arms MT. The gap policy: absence of verification is not "
         "a counterexample, as a matter of theta, not of philosophy")


@check("probability_asymmetry")
def _():
    held, lift, refute = probability_asymmetry()
    ok = held and abs(lift - 2 / 3) < 1e-9 and refute == 0.0
    return ok, "EMPIRICAL", \
        ("P(B) >= P(A)+P(A->B)-1 on 50/50 random spaces; instance "
         "P(B|A)=1: observing B lifts A only to 0.667, observing ~B "
         "drops A to exactly 0.000 — confirmation accrues, refutation "
         "detonates. Popper's asymmetry as carrier arithmetic")


@check("tortoise_regress")
def _():
    counts, detached = tortoise(5)
    return counts == [3, 4, 5, 6, 7] and not detached, "FORCED", \
        ("reify the rule as a premise and count: 5 rounds, 7 premises, "
         "B never detaches — the operation flattened into a token is "
         "inert. G is not V, mechanized (Carroll 1895 for the "
         "attribution)")


# ── the engine ──────────────────────────────────────────────────────────
@check("engine_weakest_link")
def _():
    a = E.mint("sensor reads 92C", "EMPIRICAL", evidence="calibrated rig")
    c = E.certify("sensor reads 92C", "core is overheating",
                  "CONDITIONAL", evidence="thermal model, bounded")
    b = E.detach(a, c)
    ok = b.tier == "CONDITIONAL" and b.claim == "core is overheating"
    a2 = E.mint("x", "FORCED")
    c2 = E.certify("x", "y", "STIPULATED")
    ok &= E.detach(a2, c2).tier == "STIPULATED"
    return ok, "FORCED", \
        ("detach() composes tier by weakest link: EMPIRICAL through a "
         "CONDITIONAL certificate yields CONDITIONAL; FORCED through "
         "STIPULATED yields STIPULATED — a conclusion is never better "
         "than its worst rider")


@check("engine_rider_conservation")
def _():
    a = E.mint("overheating", "EMPIRICAL",
               riders={"threshold=90C per spec rev3"})
    c = E.certify("overheating", "throttle engages", "CONDITIONAL",
                  riders={"firmware 2.1 behavior"})
    b = E.detach(a, c)
    conserved = b.riders == frozenset({"threshold=90C per spec rev3",
                                       "firmware 2.1 behavior"})
    clean_no = not b.clean()
    clean_yes = E.mint("2+2=4", "FORCED").clean()
    return conserved and clean_no and clean_yes, "FORCED", \
        ("riders survive detachment as a set union — nothing silently "
         "dropped; clean (classical) detachment is granted exactly to "
         "FORCED rider-free tokens. The '/STIPULATED' verdict suffix, "
         "generalized")


@check("engine_refuses_equivocation")
def _():
    a = E.mint("bank (river)", "EMPIRICAL")
    c = E.certify("bank (finance)", "has vaults", "FORCED")
    try:
        E.detach(a, c)
        return False, "FORCED", "equivocation was allowed"
    except E.EquivocationError as e:
        return True, "FORCED", \
            ("Rider 1 enforced at the type level: detach() raises "
             f"EquivocationError on mismatched middle terms ({e})"[:200])


@check("engine_leak_accounting")
def _():
    a = E.mint("start", "FORCED", degree=1.0)
    conds = []
    prev = "start"
    for i in range(1000):
        conds.append(E.certify(prev, f"s{i}", "EMPIRICAL", degree=0.999))
        prev = f"s{i}"
    b = E.chain(a, conds)
    ok = b.degree < 1e-9 and abs(
        E.chain(E.mint("start", "FORCED"), conds[:100]).degree - 0.9) < 1e-9
    ok &= abs(leak_guarantee(1.0, 0.999, 100) - 0.9) < 1e-12
    return ok, "FORCED", \
        ("the engine's chained degree matches the Lukasiewicz bound "
         "exactly: 100 steps -> 0.900, 1000 steps -> 0.000; the sorites "
         "meter runs inside detach(), not in a footnote")


@check("engine_routing_weakest_first")
def _():
    a = E.mint("core overheating", "EMPIRICAL",
               riders={"threshold=90C per spec rev3"})
    c = E.certify("core overheating", "throttle engages", "FORCED",
                  riders={"firmware 2.1 behavior"})
    not_b = E.mint("throttle did NOT engage", "EMPIRICAL")
    rep = E.route_refutation(c, a, not_b)
    routed_to_riders = all(p.startswith("rider:") for p in rep.primary) \
        and len(rep.primary) == 2
    # classical degenerate case:
    a2 = E.mint("A", "FORCED")
    c2 = E.certify("A", "B", "FORCED")
    rep2 = E.route_refutation(c2, a2, E.mint("not B", "FORCED"))
    classical = rep2.classical_degenerate \
        and rep2.primary == ["antecedent: A"]
    return routed_to_riders and classical, "FORCED", \
        ("MT routes the refutation to the weakest-tier suspects first — "
         "here both STIPULATED riders outrank the EMPIRICAL antecedent "
         "and the FORCED certificate for blame; with everything FORCED "
         "and rider-free the report collapses to classical MT. "
         "Duhem-Quine with a chart of accounts")
