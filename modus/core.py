"""modus.core — tiers, check registry, hash-chain seals.
Same conventions as the sibling MathofLogic repos."""
from __future__ import annotations
import hashlib, json

TIERS = ("FORCED", "EMPIRICAL", "CONDITIONAL", "STIPULATED",
         "PRESUMED", "OPEN", "UNPAID")
PAID = ("FORCED", "EMPIRICAL", "CONDITIONAL")

CHECKS = {}


def check(name):
    def deco(fn):
        if name in CHECKS:
            raise KeyError(f"duplicate check id: {name}")
        CHECKS[name] = fn
        return fn
    return deco


def weakest(*tiers):
    """Weakest-link composition: the largest index on the ladder wins."""
    return max(tiers, key=TIERS.index)


def run_claim(claim):
    cid = claim.get("check")
    if cid is None:
        return {"claim": claim["claim"], "check": None, "ok": None,
                "tier": claim.get("tier", "PRESUMED"),
                "evidence": claim.get("cite", "no citation")}
    fn = CHECKS.get(cid)
    if fn is None:
        return {"claim": claim["claim"], "check": cid, "ok": False,
                "tier": "UNPAID", "evidence": f"check {cid!r} not found"}
    try:
        ok, tier, ev = fn()
    except Exception as e:
        ok, tier, ev = False, "UNPAID", f"crashed: {type(e).__name__}: {e}"
    return {"claim": claim["claim"], "check": cid, "ok": bool(ok),
            "tier": tier, "evidence": str(ev)[:220]}


def seal(body, chain):
    prev = chain[-1]["sha"] if chain else "GENESIS"
    sha = hashlib.sha256((prev + json.dumps(body, sort_keys=True))
                         .encode()).hexdigest()[:16]
    chain.append({**body, "sha_prev": prev, "sha": sha})
    return chain[-1]


def replay(chain):
    prev = "GENESIS"
    for g in chain:
        body = {k: v for k, v in g.items() if k not in ("sha", "sha_prev")}
        want = hashlib.sha256((prev + json.dumps(body, sort_keys=True))
                              .encode()).hexdigest()[:16]
        if g["sha_prev"] != prev or g["sha"] != want:
            return False
        prev = g["sha"]
    return True
