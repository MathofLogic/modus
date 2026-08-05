"""
modus.carriers — nine carrier configurations, the MP/MT decision
procedure, and the inverter battery.
==========================================================================
MP and MT are decided as designation-closure properties by COMPLETE
enumeration over each finite carrier:

  MP: a in D and IMP(a,b) in D  =>  b in D
  MT: IMP(a,b) in D and NEG(b) in D  =>  NEG(a) in D

Validity of the MT *schema* is a different property from MT *meaning
refutation*. The inverter battery separates them: four tests on the
negation gradient that measure whether "NEG(b) designated" actually
tracks "b failed". POST4 is the exhibit — MT schema-valid, inverter
broken twice over.
"""
from __future__ import annotations
from fractions import Fraction as Fr

Z, H, U = Fr(0), Fr(1, 2), Fr(1)
V3 = (Z, H, U)

kneg = lambda a: U - a
limp = lambda a, b: min(U, 1 - a + b)
gimp = lambda a, b: U if a <= b else b
gneg = lambda a: gimp(a, Z)


def _wk_or(a, b):
    return H if H in (a, b) else max(a, b)


P4 = tuple(Fr(k, 3) for k in range(4))
pneg = lambda a: P4[(P4.index(a) + 1) % 4]

Nn, Ff, Tt, Bb = "N", "F", "T", "B"
V4 = (Nn, Ff, Tt, Bb)
_trank = {Ff: 0, Nn: 1, Bb: 1, Tt: 2}
bneg = lambda a: {Nn: Nn, Ff: Tt, Tt: Ff, Bb: Bb}[a]


def bjoin(a, b):
    if Tt in (a, b):
        return Tt
    if a == b:
        return a
    if {a, b} == {Nn, Bb}:
        return Tt
    return a if _trank[a] > _trank[b] else b


# name -> (V, neg, IMP, D, bottom)
# `bottom` is the carrier's genuine-counterexample value: the thing an
# observation of outright failure returns.
CARRIERS = {
 "CL2":   ((Z, U), kneg, lambda a, b: max(kneg(a), b), (U,), Z),
 "K3":    (V3, kneg, lambda a, b: max(kneg(a), b), (U,), Z),
 "LP":    (V3, kneg, lambda a, b: max(kneg(a), b), (H, U), Z),
 "L3":    (V3, kneg, limp, (U,), Z),
 "L3+":   (V3, kneg, limp, (H, U), Z),
 "G3":    (V3, gneg, gimp, (U,), Z),
 "WK3":   (V3, kneg, lambda a, b: _wk_or(kneg(a), b), (U,), Z),
 "POST4": (P4, pneg, lambda a, b: max(pneg(a), b), (U,), Z),
 "FOUR":  (V4, bneg, lambda a, b: bjoin(bneg(a), b), (Tt, Bb), Ff),
}


def sweep(name):
    """Decide MP and MT for one carrier. Returns (mp_witness|None,
    mt_witness|None) — None means the rule HOLDS (no counterexample in
    the complete enumeration)."""
    V, neg, IMP, D, _ = CARRIERS[name]
    D = set(D)
    mp = mt = None
    for a in V:
        for b in V:
            if mp is None and a in D and IMP(a, b) in D and b not in D:
                mp = (a, b)
            if mt is None and IMP(a, b) in D and neg(b) in D \
               and neg(a) not in D:
                mt = (a, b)
    return mp, mt


def inverter_battery(name):
    """Four tests of whether the negation gradient is a fit MT-trigger.

    involution:   NEG(NEG(b)) = b everywhere — the mirror's price tag
    soundness:    NEG(b) in D  =>  b not in D — an armed trigger never
                  points at a designated value
    precision:    NEG(b) in D  =>  b = bottom — armed ONLY by the
                  genuine counterexample
    completeness: NEG(bottom) in D — the genuine counterexample DOES
                  arm it

    A carrier with valid MT but a failing battery has a schema without
    its meaning: the rule fires (or stays silent) for reasons unrelated
    to refutation."""
    V, neg, IMP, D, bottom = CARRIERS[name]
    D = set(D)
    return {
        "involution": all(neg(neg(b)) == b for b in V),
        "soundness": all(b not in D for b in V if neg(b) in D),
        "precision": all(b == bottom for b in V if neg(b) in D),
        "completeness": neg(bottom) in D,
    }
