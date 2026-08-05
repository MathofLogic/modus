#!/usr/bin/env python3
"""
mp_mt_verify.py — the receipts for the MP/MT Propagation Logic analysis.
Self-contained; deterministic; ~1s. Every FORCED/EMPIRICAL claim in the
analysis document points at a numbered block below.
"""
from fractions import Fraction as Fr
import itertools, math, random

Z, H, U = Fr(0), Fr(1, 2), Fr(1)
line = lambda s="": print(s)

# ======================================================================
# [1] MP / MT designation-validity across nine finite carriers
#     MP: a in D and IMP(a,b) in D  =>  b in D
#     MT: IMP(a,b) in D and NEG(b) in D  =>  NEG(a) in D
# ======================================================================
def sweep(name, V, neg, IMP, D):
    D = set(D)
    mp = mt = None
    for a in V:
        for b in V:
            if a in D and IMP(a, b) in D and b not in D and mp is None:
                mp = (a, b)
            if IMP(a, b) in D and neg(b) in D and neg(a) not in D \
               and mt is None:
                mt = (a, b)
    return mp, mt

mat = lambda neg, OR: (lambda a, b: OR(neg(a), b))
V3 = (Z, H, U)
kneg = lambda a: U - a
gimp = lambda a, b: U if a <= b else b
gneg = lambda a: gimp(a, Z)
limp = lambda a, b: min(U, 1 - a + b)

def wk(f):
    return lambda a, b: H if H in (a, b) else f(a, b)

# Post-4 cyclic negation
P4 = tuple(Fr(k, 3) for k in range(4))
pneg = lambda a: P4[(P4.index(a) + 1) % 4]

# Belnap FOUR
Nn, Ff, Tt, Bb = "N", "F", "T", "B"
V4 = (Nn, Ff, Tt, Bb)
trank = {Ff: 0, Nn: 1, Bb: 1, Tt: 2}
bneg = lambda a: {Nn: Nn, Ff: Tt, Tt: Ff, Bb: Bb}[a]
def bjoin(a, b):
    if Tt in (a, b): return Tt
    if a == b: return a
    if {a, b} == {Nn, Bb}: return Tt
    return a if trank[a] > trank[b] else b

CASES = [
 ("CL2   material, D={1}", (Z, U), kneg, mat(kneg, max), (U,)),
 ("K3    material, D={1}", V3, kneg, mat(kneg, max), (U,)),
 ("LP    material, D={1/2,1}", V3, kneg, mat(kneg, max), (H, U)),
 ("L3    Luk IMP,  D={1}", V3, kneg, limp, (U,)),
 ("L3+   Luk IMP,  D={1/2,1}", V3, kneg, limp, (H, U)),
 ("G3    residuum, D={1} (intuitionistic 3-chain)", V3, gneg, gimp, (U,)),
 ("WK3   weak material, D={1}", V3, kneg,
  (lambda a, b: wk(max)(kneg(a), b)), (U,)),
 ("POST4 cyclic neg, material, D={1}", P4, pneg,
  (lambda a, b: max(pneg(a), b)), (U,)),
 ("FOUR  material, D={T,B}", V4, bneg,
  (lambda a, b: bjoin(bneg(a), b)), (Tt, Bb)),
]

line("[1] MP/MT designation-validity, complete enumeration")
for name, V, neg, IMP, D in CASES:
    mp, mt = sweep(name, V, neg, IMP, D)
    line(f"  {name:<46} MP {'HOLDS ' if not mp else f'FAILS {mp}':<18} "
         f"MT {'HOLDS' if not mt else f'FAILS {mt}'}")

# ======================================================================
# [2] MP is residuation: T(a, a->b) = min(a,b) <= b for Lukasiewicz,
#     exactly, two-case algebra checked on a 21x21 exact grid; and the
#     residuation inequality for Godel and product t-norms.
# ======================================================================
line("\n[2] MP as residuation: T(a, a->b) <= b")
grid = [Fr(i, 20) for i in range(21)]
tl = lambda a, b: max(Z, a + b - 1)
ok_l = all(tl(a, limp(a, b)) == min(a, b) for a in grid for b in grid)
ok_g = all(min(a, gimp(a, b)) <= b for a in grid for b in grid)
pimp = lambda a, b: U if a <= b else b / a
ok_p = all(a * pimp(a, b) <= b for a in grid for b in grid)
line(f"  Lukasiewicz: T(a, a->b) EQUALS min(a,b) on all 441 grid points:"
     f" {ok_l}")
line(f"  Godel:   min(a, a->b) <= b everywhere: {ok_g}")
line(f"  Product: a * (a->b)  <= b everywhere: {ok_p}")

# ======================================================================
# [3] The leak bound and sorites: b >= a + (a->b) - 1 per detachment.
#     1000 chained MPs, each conditional at degree 0.999.
# ======================================================================
line("\n[3] detachment leak (Lukasiewicz): guarantee after n steps")
a0, c = 1.0, 0.999
for n in (1, 10, 100, 500, 1000):
    g = max(0.0, a0 - n * (1 - c))
    line(f"  n={n:>4}: each step 99.9% safe, guaranteed degree of "
         f"conclusion >= {g:.3f}")

# ======================================================================
# [4] Contraposition asymmetry on the 3-chain Heyting algebra:
#     MT ((a->b) AND ~b) -> ~a is valid; the mirror
#     (~b->~a) -> (a->b) is NOT.
# ======================================================================
line("\n[4] MT vs its mirror, intuitionistic 3-chain")
mt_vals = [gimp(min(gimp(a, b), gneg(b)), gneg(a)) for a in V3 for b in V3]
mirror = {(a, b): gimp(gimp(gneg(b), gneg(a)), gimp(a, b))
          for a in V3 for b in V3}
bad = min(mirror, key=lambda k: mirror[k])
line(f"  MT valid: min over all 9 points = {min(mt_vals)} (=1 means valid)")
line(f"  mirror (~b->~a)->(a->b): value {mirror[bad]} at (a,b)={bad}"
     f" — DNE is the missing part")

# ======================================================================
# [5] The gap policy: MT's trigger is NEG(b) designated. In K3 an
#     unverified prediction (b=1/2) never arms the trigger; only a
#     full counterexample (b=0) does. (MT itself is valid in K3 — [1].)
# ======================================================================
line("\n[5] K3 gap policy: when does MT's trigger NEG(b) in D arm?")
for b, label in ((H, "prediction unverified"), (Z, "prediction refuted")):
    armed = kneg(b) in (U,)
    line(f"  b={b} ({label}): NEG(b)={kneg(b)} -> trigger "
         f"{'ARMED — refutation may proceed' if armed else 'not armed — nothing is refuted'}")
line("  POST4 footnote: MT 'holds' there ([1]) but NEG(b) in D means "
     "b was 2/3 — the")
line("  cyclic negation is not an inverter, so the valid schema no "
     "longer means refutation.")

# ======================================================================
# [6] Probability carrier: MP-support is bounded and gradual;
#     MT-refutation from a degree-1 conditional is total.
# ======================================================================
line("\n[6] probability: the MP/MT asymmetry, 50 random spaces + instance")
rng = random.Random(20260707)
ok = True
for _ in range(50):
    p = [rng.random() for _ in range(6)]
    s = sum(p); p = [x / s for x in p]
    A = [i < 3 for i in range(6)]
    B = [i % 2 == 0 for i in range(6)]
    PA = sum(x for x, a in zip(p, A) if a)
    PB = sum(x for x, b in zip(p, B) if b)
    Pmat = sum(x for x, a, b in zip(p, A, B) if (not a) or b)  # P(~A or B)
    ok &= PB >= PA + Pmat - 1 - 1e-12
line(f"  P(B) >= P(A) + P(A->B) - 1 held on all 50 spaces: {ok}")
PA0, PBgA, PBgnA = 0.5, 1.0, 0.5
PB = PA0 * PBgA + (1 - PA0) * PBgnA
line(f"  instance P(A)=0.5, P(B|A)=1, P(B|~A)=0.5:")
line(f"    observe B  (MP direction): P(A|B)  = "
     f"{PA0 * PBgA / PB:.3f}   — bounded lift")
line(f"    observe ~B (MT direction): P(A|~B) = "
     f"{PA0 * (1 - PBgA) / (1 - PB):.3f}   — total refutation from one datum")

# ======================================================================
# [7] Carroll's regress, mechanized: reify MP as a premise and count
#     the premises needed before anything detaches. (It never does.)
# ======================================================================
line("\n[7] the tortoise: premises added by reifying the rule, 5 rounds")
prem = ["A", "A->B"]
for k in range(5):
    prem.append("(" + " & ".join(prem) + ") -> B")
    line(f"  round {k+1}: {len(prem)} premises, B still not detached")
line("  the rule consumed as a token regenerates itself as a premise: "
     "G is not V")
