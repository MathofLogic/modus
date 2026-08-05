"""
modus.engine — detachment with the meter running.
==========================================================================
The repo's product: MP and MT as they behave when the classical
presentation's three unpriced riders are put back on the instrument.

A Token is a minted claim: value plus tier plus riders (conserved
stipulations) plus provenance. A Conditional is a certificate between
named claims. The engine enforces:

  RIDER 1 (token identity)      detach() REFUSES equivocation — the
                                antecedent token must be the very claim
                                the certificate names.
  RIDER 2 (threshold / degree)  detachment composes degrees by the
                                Lukasiewicz guarantee a + c - 1: the
                                leak is metered, never hidden.
  RIDER 3 (currency)            certificates carry riders (contexts,
                                stipulations); detachment CONSERVES the
                                union — nothing is silently dropped.

Tier composes by weakest link. Clean detachment — value only,
provenance burned, the classical privilege — is granted exactly to
FORCED, rider-free tokens.

MT is route_refutation(): a failed prediction refutes the CONJUNCTION
of the antecedent with every rider, and the tier ladder is the routing
table — the refutation is routed to the weakest-tier suspect(s) first.
The classical rule is recovered as the degenerate case: all suspects
FORCED and rider-free routes the whole blast to the antecedent.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from .core import TIERS, weakest


class EquivocationError(TypeError):
    """Rider 1 violated: the antecedent token is not the claim the
    certificate names. Four-term fallacy, refused at the type level."""


@dataclass(frozen=True)
class Token:
    claim: str
    tier: str
    degree: float = 1.0
    riders: frozenset = frozenset()
    provenance: tuple = ()

    def clean(self):
        """The classical detachment privilege: may this token travel as
        a bare value?"""
        return self.tier == "FORCED" and not self.riders


@dataclass(frozen=True)
class Conditional:
    ante: str
    cons: str
    tier: str
    degree: float = 1.0
    riders: frozenset = frozenset()
    provenance: tuple = ()

    @property
    def claim(self):
        return f"({self.ante}) -> ({self.cons})"


def mint(claim, tier, degree=1.0, riders=(), evidence=""):
    if tier not in TIERS:
        raise ValueError(tier)
    return Token(claim, tier, float(degree), frozenset(riders),
                 (("mint", claim, tier, evidence),))


def certify(ante, cons, tier, degree=1.0, riders=(), evidence=""):
    if tier not in TIERS:
        raise ValueError(tier)
    return Conditional(ante, cons, tier, float(degree),
                       frozenset(riders),
                       (("certify", ante, cons, tier, evidence),))


def detach(a: Token, cond: Conditional) -> Token:
    """MP with the riders on the instrument."""
    if a.claim != cond.ante:
        raise EquivocationError(
            f"token identity rider violated: token is {a.claim!r}, "
            f"certificate expects {cond.ante!r}")
    return Token(
        claim=cond.cons,
        tier=weakest(a.tier, cond.tier),
        degree=max(0.0, a.degree + cond.degree - 1.0),
        riders=a.riders | cond.riders,
        provenance=a.provenance + cond.provenance
                   + (("MP", a.claim, cond.cons),))


def chain(a: Token, conds) -> Token:
    for c in conds:
        a = detach(a, c)
    return a


@dataclass
class RoutingReport:
    observation: str
    ledger: list                 # (suspect_name, tier, riders) weakest-first
    primary: list                # weakest-tier suspect names
    classical_degenerate: bool   # everything FORCED & rider-free

    def __str__(self):
        rows = "\n".join(f"    {n:<28} {t:<12} riders={sorted(r) or '-'}"
                         for n, t, r in self.ledger)
        head = (f"  REFUTATION ROUTED (observation: {self.observation})\n"
                f"{rows}\n  -> primary suspect(s): "
                f"{', '.join(self.primary)}")
        if self.classical_degenerate:
            head += ("\n  -> all suspects FORCED and rider-free: "
                     "classical MT recovered — the antecedent eats it")
        return head


def route_refutation(cond: Conditional, antecedent: Token,
                     not_b: Token) -> RoutingReport:
    """MT as tier-routed auditing. Suspects = the antecedent, the
    certificate itself, and every rider either carries (each rider is a
    STIPULATED suspect by construction). Weakest tier absorbs the blame
    first; Duhem-Quine with a chart of accounts."""
    suspects = [("antecedent: " + antecedent.claim, antecedent.tier,
                 antecedent.riders),
                ("certificate: " + cond.claim, cond.tier, cond.riders)]
    for r in sorted(antecedent.riders | cond.riders):
        suspects.append(("rider: " + r, "STIPULATED", frozenset()))
    ordered = sorted(suspects, key=lambda s: TIERS.index(s[1]),
                     reverse=True)                 # weakest first
    worst = ordered[0][1]
    primary = [n for n, t, _ in ordered if t == worst]
    degenerate = all(t == "FORCED" and not r for _, t, r in suspects)
    if degenerate:
        primary = ["antecedent: " + antecedent.claim]
    return RoutingReport(not_b.claim, ordered, primary, degenerate)
