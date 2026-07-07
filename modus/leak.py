"""
modus.leak — the quantitative regime of detachment.
==========================================================================
Residuation (MP as the definition of implication read back), the
per-step detachment leak in graded carriers, the sorites as compounded
leak, and the probabilistic MP/MT asymmetry.
"""
from __future__ import annotations
from fractions import Fraction as Fr
import random

Z, U = Fr(0), Fr(1)


def residuation_grid(n=20):
    """T(a, a->b) vs b for the three fundamental t-norms on an exact
    (n+1)x(n+1) rational grid. Lukasiewicz sharpens to the identity
    T(a, a->b) = min(a,b)."""
    grid = [Fr(i, n) for i in range(n + 1)]
    tl = lambda a, b: max(Z, a + b - 1)
    il = lambda a, b: min(U, 1 - a + b)
    ig = lambda a, b: U if a <= b else b
    ip = lambda a, b: U if a <= b else b / a
    luk_identity = all(tl(a, il(a, b)) == min(a, b)
                       for a in grid for b in grid)
    godel_ineq = all(min(a, ig(a, b)) <= b for a in grid for b in grid)
    prod_ineq = all(a * ip(a, b) <= b for a in grid for b in grid)
    # tightness: whenever b <= a the Lukasiewicz guarantee is EXACTLY b
    tight = all(tl(a, il(a, b)) == b for a in grid for b in grid if b <= a)
    return luk_identity, godel_ineq, prod_ineq, tight, (n + 1) ** 2


def leak_guarantee(a0, cond_degree, n):
    """Guaranteed degree of the conclusion after n chained detachments,
    each certificate at cond_degree: the compounded Lukasiewicz bound."""
    return max(0.0, a0 - n * (1 - cond_degree))


def sorites(n=1000, cond=0.999, a0=1.0):
    return [(k, leak_guarantee(a0, cond, k)) for k in (1, 10, 100, 500, n)]


def probability_asymmetry(trials=50, seed=20260707):
    """(1) the MP-direction bound P(B) >= P(A) + P(A->B) - 1 on random
    finite spaces; (2) the instance where MT detonates: P(B|A)=1 makes
    a single ~B a total refutation while B is only a bounded lift."""
    rng = random.Random(seed)
    bound_held = True
    for _ in range(trials):
        p = [rng.random() for _ in range(6)]
        s = sum(p)
        p = [x / s for x in p]
        A = [i < 3 for i in range(6)]
        B = [i % 2 == 0 for i in range(6)]
        PA = sum(x for x, a in zip(p, A) if a)
        PB = sum(x for x, b in zip(p, B) if b)
        Pmat = sum(x for x, a, b in zip(p, A, B) if (not a) or b)
        bound_held &= PB >= PA + Pmat - 1 - 1e-12
    PA0, PBgA, PBgnA = 0.5, 1.0, 0.5
    PB = PA0 * PBgA + (1 - PA0) * PBgnA
    lift = PA0 * PBgA / PB                        # P(A|B)  = 0.667
    refute = PA0 * (1 - PBgA) / (1 - PB)          # P(A|~B) = 0.000
    return bound_held, lift, refute


def mirror_asymmetry():
    """On the 3-chain Heyting algebra: MT ((a->b) AND ~b) -> ~a is
    valid (value 1 at all 9 points); the classical mirror
    (~b->~a) -> (a->b) is not — witness value and point returned."""
    from .carriers import V3, gimp, gneg
    mt_min = min(gimp(min(gimp(a, b), gneg(b)), gneg(a))
                 for a in V3 for b in V3)
    mirror = {(a, b): gimp(gimp(gneg(b), gneg(a)), gimp(a, b))
              for a in V3 for b in V3}
    worst = min(mirror, key=lambda k: mirror[k])
    # and MT's true form: composition into the absurdity sink —
    # transitivity ((a->b) AND (b->0)) -> (a->0), valid on the chain
    comp_min = min(gimp(min(gimp(a, b), gimp(b, Z)), gimp(a, Z))
                   for a in V3 for b in V3)
    return mt_min, mirror[worst], worst, comp_min
