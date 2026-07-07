# Modus Ponens and Modus Tollens — a Propagation Logic Analysis

**Detachment is not a law of thought. It is a mechanical property of one configuration of (V, G, θ) — the property of a certificate format matched to its acceptance threshold — and the classical presentation hides both the machinery that makes it work and the invoice for the tokens it runs on.**

Every claim below is tiered. Claims tagged **FORCED** with a backticked check name were decided by complete enumeration or exact computation by that registered check in `modus/checks.py`, run on every build by `verify.py` (which also computes this document's own paid fraction from `modus/claims.py`); **[EMPIRICAL]** claims were measured with stated bounds; **[PRESUMED — source]** claims are inherited from the literature and priced at zero here; **[STIPULATED]** marks conventions this analysis declares. The mechanics come first, the reification and truth-presumption analysis second, because the second is only visible once the first is on the table.

---

## 1 · What the classical presentation says, and what it doesn't

The two rules as handed down:

> **MP**: from A and A→B, infer B.
> **MT**: from A→B and ¬B, infer ¬A.

Four-line truth tables verify both, the second is the first plus contraposition, and the matter is closed in a paragraph. What the paragraph does not say:

First, that MP is the *entire engine* of the oldest proof architecture. A Hilbert system has axiom schemata and exactly one rule of motion — MP. Every theorem of classical mathematics, in that presentation, is a straight-line chain of detachments. So MP is not one rule among many; it is *the* discharge operation, and everything else (the axioms) is pre-charged conditionals waiting to be cashed. Whatever MP costs, mathematics pays it at every step. [PRESUMED — Frege 1879; Hilbert & Ackermann 1928]

Second, that the four-line verification quantifies over *values* and says nothing about the *processes that minted them*. The soundness of MP is a conditional guarantee: **if** the tokens A, A→B are stable, self-identical across premises, and current, **then** designation propagates to B. The three "if"s are real, they each have their own failure threshold, and the classical presentation prices all three at zero. Sections 6–7 itemize that invoice.

Third, that MP and MT are presented as mirror images, and the mirror is a *purchased* symmetry — it is bought by a specific property of the negation gradient (involutivity) which in turn encodes a specific metaphysical posture (falsity as just truth-of-the-negation, equally real, equally intrinsic). Break the negation and the mirror breaks, while both rules can individually survive. The sweep in Section 4 shows exactly this happening.

## 2 · The PL restatement: what MP mechanically is

In Propagation Logic terms, a conditional A→B is a **stored gradient**: a certificate that designation, once present at A, can be transported to B. MP is the **discharge stroke** — the operation that cashes the certificate. Its partner, →-introduction (the deduction theorem), is the **compression stroke** that mints certificates from derivations. The two strokes are adjoint, and that adjunction is the deepest mechanical fact about MP:

> In any residuated structure, implication is *defined* as the residual of conjunction: a→b is the largest c such that a ∧ c ≤ b. Setting c = a→b gives **a ∧ (a→b) ≤ b immediately.** MP is not a rule *added* to such a system. It is the defining specification of the conditional, read back. The certificate is minted to be exactly cashable, and asking "why is MP valid?" in a residuated carrier gets the answer: because → was reverse-engineered from MP.

This is not only algebra. Enumerated on a 21×21 exact-rational grid, the residuation inequality T(a, a→b) ≤ b holds for all three fundamental t-norms, and for Łukasiewicz the inequality sharpens to an identity: **T(a, a→b) = min(a, b), exactly, at all 441 grid points** [FORCED — `residuation_identity`]. Detachment in the Łukasiewicz carrier delivers precisely the weaker of "how true the antecedent was" and "how true the consequent could be" — the weakest-link law, derived rather than decreed.

Under Curry–Howard the same fact wears its engineering openly: a BHK proof of A→B *is a function*, a proof of A *is an input*, and MP *is application* — an actual computation with an actual step count. The carriersets library ran this literally: Church-numeral 2+2 β-reduces to 4 in a counted number of steps. MP under the constructive reading is never free; it is exactly as expensive as the function it applies. [FORCED — carriersets `lambda_church_rosser_bounded`] The classical reading is the same machine with the step counter unplugged. Section 7 returns to who pays for the unplugging.

One consequence worth stating before the sweep: **MP fails precisely where the certificate format and the acceptance threshold were configured independently.** The material conditional ¬A∨B is a formula with the *shape* of a classical certificate. Transplant that shape into a carrier whose designated set it was not minted for — designate the glut — and the certificate becomes forgeable: it can be designated *by the antecedent's falsity-content* rather than by any genuine gradient to B. That is not a paradox. It is a configuration mismatch, and LP is its canonical CVE.

## 3 · What MT mechanically is

MT is standardly glossed as MP-through-a-mirror. The mechanically honest gloss is different: **MT is MP plus a round trip through the negation gradient**, and everything distinctive about MT is a property of that inverter.

Strip the costume off. Define ¬A as A→⊥ (implication into the absurdity sink) and MT becomes pure composition: from A→B and B→⊥, compose to A→⊥. No mirror, no inversion — just transitivity of stored gradients, pointed at ⊥. This is why MT is *intuitionistically valid* even though double-negation elimination is not: composition is constructive; mirror-inversion is not. Enumerated on the 3-chain Heyting algebra: the MT formula ((a→b) ∧ ¬b) → ¬a takes value 1 at all nine points, while its classical mirror (¬b→¬a) → (a→b) drops to ½ at (a,b) = (1, ½) [FORCED — `mirror_asymmetry_3chain`]. **MT survives the removal of classical negation; the MP/MT symmetry does not.** The symmetry was never about inference. It was about the value space having an involution — the formal shadow of the doctrine that falsity is as real, as intrinsic, and as symmetric as truth.

The quality ladder of inverters, read off the sweep in the next section: involutive negation (CL2, K3, LP, Ł3) buys full two-way contraposition wherever detachment itself survives; intuitionistic/Gödel negation (¬¬a ≥ a only) keeps MT as composition and breaks the mirror one-way; glut designation (LP, FOUR) kills MT together with MP because the certificate is forgeable in both directions; and cyclic negation (Post) produces the strangest outcome of all — **MT remains schema-valid while ceasing to mean refutation**. In Post-4, ¬b designated means "b was 2/3," the cyclic successor condition, not "b failed" [FORCED — `sweep_nine_carriers`, `post4_valid_but_meaningless`]. The rule passes the audit while the auditor's badge is fake. This is the cleanest available demonstration that designation-validity is a syntactic shadow: the *semantic role* of MT — routing a failure back to its source — is carried entirely by the negation gradient's fitness as an inverter, and validity of the schema neither requires nor certifies that fitness.

This repo formalizes that fitness as the **inverter battery** (`inverter_battery_table`): four decidable tests on the negation gradient. *Involution* (¬¬b = b — the mirror's price tag); *trigger soundness* (an armed trigger never points at a designated value); *trigger precision* (armed only by the genuine counterexample); *trigger completeness* (the genuine counterexample does arm it). Decided over all nine carriers [FORCED — `inverter_battery_table`]: CL2, K3, L3, WK3 pass all four; LP and FOUR fail soundness and precision (the glut arms the trigger while designated); G3 fails only involution (the mirror, not the meaning); and POST4 fails **precision and completeness both** — its trigger arms on b = 2/3 and *never* on b = 0 [FORCED — `post4_valid_but_meaningless`]. In POST4, MT is a valid rule that cannot, even once, mean refutation: the genuine counterexample is invisible to it. Schema validity and trigger fitness are fully independent axes, and the battery measures the second one.

## 4 · The carrier sweep — measured

MP as a designation-closure property (a ∈ D and IMP(a,b) ∈ D forces b ∈ D) and MT likewise (IMP(a,b) ∈ D and ¬b ∈ D forces ¬a ∈ D), decided by complete enumeration over each finite carrier [FORCED — `sweep_nine_carriers`]:

| Carrier (implication, designation) | MP | MT | Witness / note |
|---|---|---|---|
| CL2 — material, D={1} | holds | holds | the reference configuration |
| K3 — material, D={1} | holds | holds | the gap protects detachment |
| **LP — material, D={½,1}** | **fails** | **fails** | MP: (a,b)=(½,0); MT: (a,b)=(1,½) |
| Ł3 — Łukasiewicz IMP, D={1} | holds | holds | residuated certificate |
| **Ł3⁺ — Łukasiewicz IMP, D={½,1}** | **fails** | **fails** | same witnesses — designation, not the t-norm, is the culprit |
| G3 — residuum, D={1} (intuitionistic 3-chain) | holds | holds | MT as composition; mirror broken (block 4) |
| WK3 — weak material, D={1} | holds | holds | absorption never forges a certificate |
| POST4 — cyclic ¬, material, D={1} | holds | holds | *vacuously meaningful-free: ¬ is no inverter* |
| **FOUR — material, D={T,B}** | **fails** | **fails** | MP: (B,N); MT: (T,B) — the glut again |

Three structural readings of this table.

**The killer is designating the glut, not adding values.** K3 and LP share every table entry; they differ only in whether ½ licenses inference. K3 keeps both rules; LP loses both. Ł3 and Ł3⁺ repeat the experiment with a different (residuated!) conditional and get the same result — so it is not the material conditional's fault alone. The moment a value that is *simultaneously its own negation* becomes designated, every conditional touching it becomes designated-by-contamination, and detachment dies. LP's loss of MP is the famous, priced cost of paraconsistency [PRESUMED — Priest 1979; independently re-derived here and in the carriersets `lp_signature` check, kernel-parity confirmed]: you may keep contradictions as usable premises, or you may keep detachment. Not both. θ is where the choice is made, and PL's contribution is to display it *as* a θ-choice rather than as a mystery about inference.

**The gap is detachment's friend.** K3's undesignated middle never forges certificates — an unresolved computation contaminates *values* but never crosses the designation line, so anything that clears θ is genuinely classical-grade. This is the formal content of the engineering rule "unknown must not validate": strong Kleene is the configuration in which it provably doesn't.

**MT's trigger is a separate component from MT's validity.** In K3, MT is valid — but its trigger, ¬b ∈ D, arms only when b = 0, a full counterexample. An unverified prediction (b = ½) arms nothing: ¬½ = ½ ∉ D, nothing is refuted [FORCED — `k3_trigger_policy`]. The three-valued zoo is thus a menu of *policies for what a failed prediction means*: classical (every non-verification is a counterexample), gapped (only measured falsity refutes; absence of verification refutes nothing), glutted (even measured falsity may not refute, because the source might be contradictory and still designated). Choosing bivalence is choosing the first policy — and Section 7 argues that this choice is where the presumption of discoverable truth does its actual work.

## 5 · The quantitative regime: the leak, the sorites, and the asymmetry

Quantize V to {0,1} and detachment is lossless. Refuse to quantize and the Łukasiewicz bound puts a meter on it: from A at degree x and A→B at degree y, B is guaranteed only x + y − 1. **Each detachment leaks (1 − y)** — the certificate's shortfall from perfection — and the leaks add. Chained a thousand times with conditionals each at degree 0.999 ("each step is 99.9% safe"), the guaranteed degree of the conclusion is exactly zero [FORCED — `leak_bound_sorites`]:

```
n=   1: guaranteed >= 0.999      n= 500: guaranteed >= 0.500
n= 100: guaranteed >= 0.900      n=1000: guaranteed >= 0.000
```

This *is* the sorites paradox, mechanized: the heap argument is a long MP chain whose per-step conditionals are almost-but-not-quite degree 1, and the paradox is nothing but the accumulated leak arriving all at once because the classical carrier deleted the meter. Bivalence does not eliminate the leak. **It relocates the leak outside the calculus** — into the tokenization step where each "almost 1" was rounded to 1 before inference began — and MP's classical losslessness is purchased entirely by that relocation. The cost did not vanish; it moved to where the logic can't see it. That single sentence is, compressed, most of what this analysis has to say.

The probability carrier prices the two rules asymmetrically, and the asymmetry is arithmetic, not philosophy. The MP-direction bound P(B) ≥ P(A) + P(A→B) − 1 held on all fifty random probability spaces tried [FORCED — `probability_asymmetry`] — support propagates, bounded and gradual. But run the instance P(A)=0.5, P(B|A)=1, P(B|¬A)=0.5: observing B (the MP direction) lifts A only to 0.667, while observing ¬B (the MT direction) drops A to exactly 0.000 — **total refutation from a single datum**, because a degree-1 conditional makes ¬B and A jointly impossible [FORCED — `probability_asymmetry`]. Confirmation accrues; refutation detonates. Popper's asymmetry falls out of Bayes with no epistemology added [PRESUMED as the philosophical framing — Popper 1934; the arithmetic is FORCED above].

This asymmetry is not decoration — it is the reason the whole MathofLogic methodology has the shape it has. The mapping guide's step 4 (derive forced laws) is **MP-shaped**: establishing a law costs complete coverage of V, because support only accumulates. Step 5 (find failures) is **MT-shaped**: one witness suffices, because refutation is total. The carriersets library could decide every "Breaks" claim with a single printed witness and needed exhaustive enumeration for every "Forces" claim precisely because MT is cheap and MP is expensive, per unit of certainty delivered. The FORCED tier itself has two acquisition prices, and they are the two rules' prices.

## 6 · Reification: the subject–predicate freeze, and MP's three unpriced riders

Now the part of the machine the classical presentation keeps offstage. Before MP can run once, the world has been tokenized. "Socrates is mortal" is not a process; it is the *frozen output* of at least two processes, packaged by the subject–predicate form into a shippable receipt:

The **subject position** is the output of an *individuation* process — tracking, re-identification, the claim that this S is re-identifiable as the same S across contexts and premises. That process has an error rate and its own θ. The **predicate position** is the output of a *classification* process — a threshold laid across some graded, measured quantity. The Boundary Law prices exactly this act: telling two hypotheses apart across a gap costs D = 8σ²ln(1/δ)/gap² samples, diverging as the case approaches the threshold [EMPIRICAL — carriersets `boundary_law_scaling`, slope ≈ 2 measured]. And the **copula** — "is" — performs the third freeze: it detaches the timestamp, presenting the output as tenselessly available, a zero-decay stipulation.

Frege's own foundational move makes the first half of this explicit: subject–predicate is replaced by function–argument, so the atomic sentence P(s) is *already* the recorded output of a gradient evaluation — a G-application flattened to its value [PRESUMED — Frege 1879, 1892]. Propositional logic then forgets even that structure, keeping only the flattened token. What the flattening discards is **provenance**: which process minted this token, at what tolerance, at what tier, when. Classical inference is provenance-free *by design* — that is what makes it compositional and fast; a derived B is interchangeable with an axiomatic B, any B slots anywhere. For mathematics this is the right design, because re-derivation is always available at the original price. For empirical tokens it is a silent loan.

So MP's soundness, restated with the offstage machinery onstage, carries **three riders**:

**Rider 1 — token identity.** The A in the first premise and the A in the antecedent of the second must be the *same token*: the subject held, the middle term did not drift. The traditional name for this rider failing is *equivocation* (the four-term fallacy) — and notice that tradition classifies it as a fallacy of the arguer, not of the logic, which is precisely the invoice being mailed to a different address.

**Rider 2 — threshold stability.** The predicate's threshold did not move between minting and use; the margins that were rounded away stay rounded the same way. The traditional name for this rider failing under iteration is the *sorites* — Section 5's leak, arriving through the tokenization door instead of the inference door.

**Rider 3 — currency.** The conditional certificate has not expired: the regime that made A→B degree-1 still obtains. The traditional names here are *stale lemma*, *regime change*, the reference-class problem. Every empirical conditional is minted inside a context and shipped without one.

Classical validity is exactly the guarantee that holds *conditional on all three riders*, and the classical presentation prices the riders at zero — they live in the metatheory, off the invoice. The classical "fallacies" are not deviations from logic; **they are the riders' bills arriving**, and they arrive addressed to rhetoric because the logic declared itself not liable. PL's proposal is not to reject MP but to move the riders onto the instrument: a token travels with its tier, its minting evidence, and its stipulations, and detachment composes by weakest link. This is not speculative — it is what the sibling repositories already execute: `run_claim` returns (verdict, tier, evidence); composition takes the minimum tier; PL-Verify's CERTIFIED verdict is *capped at STIPULATED* because its probe-set rider is conserved through every detachment rather than silently dropped. A provenance-carrying MP is buildable, and cheap; the suite that proves it runs in two seconds.

MT under the rider analysis becomes the most interesting component in the machine. When ¬B arrives, what has actually been refuted is the **conjunction** of A with all three riders and with B's own measurement fidelity — the Duhem–Quine point [PRESUMED — Duhem 1906; Quine 1951]. Classical MT auto-routes the entire refutation to A, and it is licensed to do so only because the riders were booked at zero: a zero-priced premise cannot absorb blame. The tier ladder converts Duhem–Quine from a skeptical shrug into a **routing algorithm**: route the refutation to the lowest-tier link first. A FORCED arithmetic step never eats the blast; the STIPULATED probe set or the PRESUMED identity condition does. The Living Map's refusal semantics is this routing table running in production — a variant that fails the probes refutes *the variant's membership in the contract class*, never "optimization," never the arithmetic [FORCED — carriersets `program_variant_contract_gate`]. MT, tier-routed, is an auditor with a chart of accounts. MT, classically presented, is an auditor who has been told in advance whom to blame.

And then there is the tortoise. Lewis Carroll's regress [PRESUMED — Carroll 1895] is usually filed as a curiosity; under PL it is the load-bearing exhibit. The tortoise demands that the rule MP be written down as a premise before it may be used — that the **gradient be reified into a value**. Grant it, and the new premise needs the rule to be applied, which must be written down, which needs the rule... Block 7 mechanizes the futility: five rounds, seven premises, B never detaches [FORCED — `tortoise_regress`]. The moral is a type theorem: **G is not V.** Operations consume tokens; an operation flattened into a token is inert, and the machine that would consume it is the very thing that was flattened. Classical logic *already knows this* — it keeps MP in the metatheory precisely to stop the regress — which means classical logic already contains, implicitly and unpriced, the process/output distinction that PL makes explicit. The tortoise is the proof that the distinction was always there; PL's move is merely to stop hiding it in the room where the invoices can't be delivered.

## 7 · Truth as an intrinsic, discrete, discoverable primitive: what the presumption actually buys

The classical foundations bake in a three-part doctrine about truth: it is **intrinsic** (a property carried by the proposition-token itself, context-free), **discrete** (bivalent — the token holds one of exactly two values), and **discoverable** (the value pre-exists any evaluation; procedures reveal, they do not construct). Frege did not merely assume this — he *formalized* it, making sentences names of an object, das Wahre: truth reified not as metaphor but as a design decision of the Begriffsschrift's semantics [PRESUMED — Frege 1892]. The question a mechanics-first analysis can actually answer is: **which parts of the MP/MT machine does this doctrine power, and which parts run without it?**

What the presumption buys, component by component:

**Intrinsic → free storage and monotonicity.** If designation is a property of the token, then a designated token stays designated: no decay, no rent, no context to drift out of. Once ⊢B, always ⊢B. The entire nonmonotonic family — belief revision, default logic, the Bayesian carrier — is what inference looks like when designation is instead a *ledger state*: something maintained, at cost, against evidence flow. Landauer already priced the storage of a bit at kT·ln2 [FORCED as arithmetic — carriersets `landauer_and_h_theorem`]; the Boundary Law priced the *maintenance of the distinction* the bit records. Truth-as-intrinsic is the stipulation that both prices are zero — a fine stipulation for mathematics, where every token can be re-minted on demand at the original cost, and a false one for every empirical token, whose minting process ages.

**Discrete → lossless detachment.** Section 5 showed the counterfactual directly: in any graded carrier, MP leaks 1−y per step and sorites is the leak compounding. Bivalence makes MP lossless by rounding all margins away *before* the calculus starts — the meter is not removed, it is relocated to the unpriced tokenization step. The "discrete primitive" is therefore an engineering decision about *where the Boundary-Law bill is paid*: classical logic pays it all upfront, off the books, at minting time; graded logics amortize it, on the books, per inference. Neither escapes it.

**Intrinsic + discrete + symmetric → the MP/MT mirror.** Involutive negation — the value-space symmetry v ↦ 1−v — is the formal shadow of the realist doctrine that falsity is just the truth of the negation, an equally real, equally intrinsic value. Block 4 measured what happens when the doctrine is withdrawn: MT survives (as composition into ⊥), the *mirror* dies (the converse contraposition drops to ½). So the presumption is not what powers MT; it is what powers MT's *interchangeability* with MP.

**Discoverable → refutation-totality.** If every proposition has its value out there awaiting discovery, then a prediction that failed to verify has *thereby* been discovered false — every non-verification is a counterexample, and MT's trigger arms on absence. Withdraw discoverability and the gap opens: K3's policy, where b=½ arms nothing [FORCED — `k3_trigger_policy`], is exactly the policy that verification-transcendent truth forbids. The choice between "unverified" and "refuted" as readings of a failed prediction is the choice between constructed and discovered designation, made operational. Nothing in the MT schema decides it; θ decides it.

Now the other side of the ledger — **what survives the presumption's removal** — and this is the sharpest result available here. MP survives *entirely*. Under BHK it is function application; under residuation it is definitional; block 2's identity T(a, a→b) = min(a,b) needs no bivalence, no realism, no discovery. MT survives as composition toward ⊥ [FORCED — `mirror_asymmetry_3chain`]. What is lost is exactly and only the *free* versions: free storage, lossless detachment, the mirror, refutation-from-absence. **The presumption of truth as an intrinsic discrete discoverable primitive is not the license for inference. It is the license for inference at zero marginal cost.** The engine runs without the doctrine; the doctrine's whole function is to unplug the meter.

And the deferred meter is not hypothetical — proof theory found it and read it. In sequent calculus, MP generalizes to the cut rule: inference through a lemma, a certificate cashed mid-proof. Gentzen's Hauptsatz says every cut can be paid off — eliminated in favor of direct, subformula-transparent derivation — and Statman showed the payoff can be **non-elementary**: a tower of exponentials [PRESUMED — Gentzen 1935; Statman 1978; both filed at their honest tier in the carriersets proof-theory record, which sits at 0/4 paid on purpose]. Read as accounting: truth-as-primitive is the convention under which every cut clears instantly because the bank is presumed infinite; cut-elimination is what auditing the account actually costs; and the non-elementary blowup is the compound interest on centuries of zero-priced detachments. The invoice was real the whole time. It was deferred, not waived.

One more component of the doctrine deserves its line: Tarski made truth *relational* — a two-place affair between a sentence and a structure, computed compositionally (and computed here, live, in the carriersets `tarski_satisfaction_finite` check). The intrinsic-truth presumption is the act of fixing the intended model and then deleting the parameter, leaving a one-place "true." For MP itself this deletion is safe — MP is valid in every model, which is what "logical" means. But the *premises* were minted in a model, and shipping them into a model-uniform rule silently re-imports the deleted parameter as Rider 3, the currency rider. Compactness guarantees the parameter can never be recovered from the tokens: any theory with an infinite model has non-standard models agreeing on every token yet disagreeing about the structure [PRESUMED — Gödel 1930; Skolem 1920]. Provenance, once flattened, is gone.

## 8 · Engineering guidance: inference with the meter running

Everything above compresses into design rules, each of which the MathofLogic stack already implements somewhere — cited as existence proofs, not aspirations.

These rules are no longer only pointers into sibling repos: `modus/engine.py` implements them as a library, and the checks hold it to the analysis. `demos/pipeline.py` runs the same inference twice — classically and metered — and prints both invoices.

**Tier-weighted detachment.** MP composes by weakest link: the conclusion's tier is the minimum over {antecedent tier, certificate tier, the three riders' tiers} [FORCED — `engine_weakest_link`]. A conclusion is never better than its worst rider, and the worst rider is usually one the classical presentation didn't book. Rider 1 — token identity — is enforced at the type level: `detach()` raises `EquivocationError` on a mismatched middle term; the four-term fallacy is refused before it can propagate [FORCED — `engine_refuses_equivocation`].

**Detachment privileges by tier.** FORCED tokens may detach clean — they travel naked, because re-derivation at original price is guaranteed. STIPULATED tokens detach *with the stipulation conserved*: the rider set unions through every detachment, which is the "/STIPULATED" verdict suffix generalized [FORCED — `engine_rider_conservation`]. Full classical detachment — value only, provenance burned — is a privilege of the mathematical regime, where Rider 3 is enforced by the subject matter.

**Tier-routed MT.** On ¬B, route the refutation to the lowest-tier link of the failed conjunction, not automatically to A, and publish the routing table with the inference. `route_refutation()` does exactly this, and recovers classical MT as the degenerate case where every suspect is FORCED and rider-free [FORCED — `engine_routing_weakest_first`]. The Living Map's refusal semantics is the production precedent: probes refute contract-membership, never the arithmetic. The routing policy itself is STIPULATED — declared, where the classical default (always blame the antecedent) is implicit.

**Trigger policy as an explicit θ-choice.** Decide, per pipeline, what a failed prediction means: classical (absence refutes), gapped (only measured falsity refutes), glutted (nothing cheaply refutes). Block 5 is the three-line demonstration that this is a configuration setting, not a fact about logic — and that inheriting the classical setting silently is inheriting verification-transcendent realism silently.

**Leak budgets for chains.** In any graded or empirical regime, an MP chain of length n with certificates at degree 1−ε carries a guarantee of at most 1−nε [FORCED — `leak_bound_sorites`], and the engine meters it inside `detach()` itself — 100 chained steps at 0.999 land on exactly 0.900, a thousand on 0.000 [FORCED — `engine_leak_accounting`]. Budget n before building the chain. The discrete regime's exemption from this rule is real but must be *earned* at minting time — the Boundary Law's D = 8σ²ln(1/δ)/gap² per distinction — and a chain is only as certified as its most expensive unpaid distinction.

**Never reify the rule.** Gradients are not values; an inference engine that stores its own rules as ordinary premises stalls in Carroll's regress [FORCED — `tortoise_regress`]. Keep G and V typed apart; the metatheory is not a hiding place for costs but it is the correct home for operations.

## 9 · Non-claims

Printed here as the house style requires. **Not claimed:** that classical logic is wrong — it is the correct carrier wherever the three riders are enforced by construction, which is to say mathematics, and its zero-pricing of them there is not an omission but an accurate price. **Not claimed:** that MP "fails in reality" — it fails in specifiable configurations (glut-designating carriers), with witnesses printed, and holds in the rest of the sweep. **Not claimed:** that the philosophical attributions (Frege's reified True, Popper's asymmetry, Dummett's anti-realist reading of intuitionism, Duhem–Quine) are settled interpretations — they are PRESUMED-tier framings; the enumerations, identities, and measured numbers are the paid content of this document, and they stand independently of every framing draped over them. **Not claimed:** that the tier-routing rule for MT is the uniquely correct blame assignment — it is a declared policy (STIPULATED) with the virtue of being explicit where the classical default is implicit.

---

## Appendix A · Reproduction

```bash
python verify.py          # sweep table, inverter battery, leak meter,
                          # claims ledger with the document's paid
                          # fraction, sealed manifest; exit 1 on any red
python tests/run.py       # the gate
python demos/pipeline.py  # the same inference, classical vs metered
```

The sweep, battery, and witnesses print at the top of `verify.py`
output; every bracketed tag in this document names the check that
earned it. The ledger in `modus/claims.py` prices this document the
same way the carriersets library prices itself — the PRESUMED entries
(Frege, Carroll, Popper, Duhem–Quine, Gentzen–Statman, Tarski,
Priest, Gödel–Skolem) are inherited with citations and counted at
zero, and the printed paid fraction says exactly how much of this
analysis is bibliography.

## Appendix B · Cross-references into the MathofLogic stack

Kernel parity: LP's detachment failure matches `pl.py`'s 15-law
signature and carriersets' `lp_signature`; K3's clean detachment
matches its 14/15 lone-LEM signature (`k3_signature`, both readings
decided there). The BHK step-counting: carriersets
`lambda_church_rosser_bounded`. The distinction pricing: carriersets
`boundary_law_scaling`. The tier-routing production precedent:
carriersets `program_variant_contract_gate` and the PL-Verify verdict
cap. Relational truth, executed: carriersets
`tarski_satisfaction_finite`.
