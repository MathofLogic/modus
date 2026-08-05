"""
pl_witness — witness counting for law engines.

THE DEFECT
A law computed as a bare boolean cannot distinguish "held in every case"
from "the guard never engaged". Measured: a carrier with an EMPTY
designated set scores as well as strong Kleene, because four of the five
guarded laws pass with their guard inert.

Only laws quantified over the VALUE SPACE are immune. Laws quantified,
directly or through a guard, over the DESIGNATED SET are all vulnerable.

THE REPAIR
Report, alongside each verdict, the number of cases in which the law COULD
have failed. Zero witnesses is coverage zero, which the tier rule already
grades UNPAID. Nothing new is invented.

NOT AN ADMISSION GATE. No carrier is refused. Pricing alone restores the
discrimination; a gate built from how classical logic behaves would refuse
real logics, which is a second defect and not a repair.
"""
GUARDED = {"LNC", "LEM", "NoGlut", "MP", "MT"}


def witnesses(V, NEG, AND, OR, D):
    """Cases in which each guarded law could have failed."""
    Ds, n = set(D), len(V)
    disc = bool(Ds) and Ds != set(V)
    return {
        "LNC":    n if Ds else 0,
        "LEM":    n if disc else 0,
        "NoGlut": sum(1 for a in V if a in Ds),
        "MP":     sum(1 for a in V for b in V
                      if a in Ds and OR(NEG(a), b) in Ds),
        "DN":     n,
    }


def grade(verdict, w):
    """Zero witnesses is never a pass."""
    return "UNPAID" if w == 0 else ("FORCED-on-cut" if verdict else "REFUTED")


def unpaid_count(laws, wits):
    """How many laws passed without being tested."""
    return sum(1 for k, v in laws.items()
               if k in wits and grade(v, wits[k]) == "UNPAID")


def distinguishes(V, NEG, AND, OR, sound_D, degenerate_Ds):
    """The canary. A sound carrier must report zero UNPAID; every
    degenerate one must report at least one."""
    def laws(D):
        Ds = set(D)
        return {
            "LNC": all(AND(a, NEG(a)) not in Ds for a in V),
            "LEM": all(OR(a, NEG(a)) in Ds for a in V),
            "NoGlut": not any(a in Ds and NEG(a) in Ds for a in V),
            "MP": all(not (a in Ds and OR(NEG(a), b) in Ds) or b in Ds
                      for a in V for b in V),
            "DN": all(NEG(NEG(a)) == a for a in V),
        }
    if unpaid_count(laws(sound_D), witnesses(V, NEG, AND, OR, sound_D)) != 0:
        return False, "a sound carrier reports UNPAID laws"
    for D in degenerate_Ds:
        if unpaid_count(laws(D), witnesses(V, NEG, AND, OR, D)) == 0:
            return False, f"degenerate carrier D={D or 'empty'} reports none"
    return True, ""
