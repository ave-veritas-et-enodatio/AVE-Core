# Stage-2b STEP 0 — the discrete continuity analysis (a note; NO code)

**Epic:** EM-readout derivation — Axiom-2's last underived leg. **Stage-2b Step 0** (the cheapest-decisive gate BEFORE any settling-test build).
**Charter:** `_orchestration/2026-07-03_em-readout-derivation-charter.md` §4 (Stage-1/2 chartered dynamics).
**Branch:** `analysis/em-readout-stage2-redesign` (same branch as the retired Stage-2a; PR #484).
**Prior:** Stage-2a RETIRED — Y-STATIC = [NO-FLUX-STRUCTURAL] at theorem grade (`..._prereg.md` §R1). The static route is a structural negative; this note asks whether the DYNAMICAL route is even live before building it.
**Panel requirement (process):** the Stage-2b prereg gets an ORCHESTRATOR REVIEW GATE BEFORE BUILD (consequence of the Stage-2a freeze violation). This note is the pre-prereg analytic input to that gate. **STOP after this note.**

**Disciplines:** `verify-before-cite` (every file:line re-verified at HEAD this session) · `substrate-native-check` (the operators are the srs/K4-native discrete ∇×, ∇·, not Cartesian) · `flag-don't-fix` (the answer, whichever way, is surfaced not steered) · `consistency-vs-emergence` (this is a FORM/structural analysis, not a value claim).

---

## 0. THE QUESTION (the cheapest-decisive one in the epic)

Does the chartered coupled dynamics — the `u`-sector (translational ↔ E) evolution + the axiom-native LC rotation↔translation coupling + the Ax4 `S(A)` nonlinearity — **CONSERVE `∇·E` identically** from clean initial data?

- **If YES (∇·E structurally conserved):** the dynamical route dies exactly as statics did. The DC monopole content of any settled state would be whatever was in the *initial data*, not emergence. A settling test would be a tautology of a different color (initial `∇·E` in = same `∇·E` out). Route the epic to **lane Z** (topology/harmonic — the box-cycle / non-contractible-cycle sector, which requires an EDGE-field E representation with DEC sector readout, invisible to a scalar-φ co-exact channel) **+ lane W** (winding pairs, the clm-wcoul2 inter-winding force).
- **If NO (the ω-coupling genuinely breaks the continuity identity):** THAT coupling term is the transducer, and the settling test has a live target. The analysis then tells us exactly which term to ledger hardest.

This is decisive and cheap: it is an algebraic identity check on the chartered update equations, needing NO integrator run.

---

## 1. THE CHARTERED DYNAMICS (grounded at file:line — verify-before-cite)

The unified srs/K4 host (`src/ave/facade/unified_engine.py`), per node on ONE native K4 graph (`unified_engine.py:29-40`, verbatim):
- **`u ∈ R³ ↔ E/ε₀`** — 3 translational DOF (2 transverse = photon; 1 longitudinal = the A1 dilatation MASS-"3" projection). `unified_engine.py:30-31`.
- **`ω ∈ R³ ↔ B/μ₀`** — 3 Cosserat micro-rotation DOF; the (2,3) winding = charge. `unified_engine.py:32`.
- **`u` is initialized zero with NO stepper — the DORMANT slot** (`unified_engine.py:114-115`: `self.u = np.zeros(...)`; the Stage-1 charter task, `charter §4 Stage-1`: "the static/longitudinal translational sector + the axiom-native rotation↔translation coupling are the missing DOFs"). Stage-2b's job is to COMPLETE this stepper.
- **KEY STRUCTURAL FACT (`unified_engine.py:38-40`, verbatim):** *"u and ω are SEPARATELY conserved grades."* The A1 scalar is NEVER wired into the transverse phasor (genesis-24 double-count guard, `master-equation.md:20`).
- **The Ax4 kernel** `S(A) = (1−A²)^p` is wired from `graded_vacuum_network.saturation_kernel` (`unified_engine.py:386-396`), modulating the effective reactances.

**The axiom-native LC coupling (Axiom 1, `axiom-definitions.md:16`):** each node's 3 translational DOF are capacitive (ε₀, E) and its 3 microrotational DOF are inductive (μ₀, B), LC-coupled at the shared node. The chartered dynamics is therefore the substrate-native Maxwell-Ampère/Faraday pair on the srs/K4 graph, with `S(A)`-modulated ε_eff, μ_eff:

```
(Ampère, the u/E update)   ∂_t (ε_eff E)  =  +∇× (μ_eff⁻¹ B)  −  J_coupling      … (I)
(Faraday, the ω/B update)  ∂_t (μ_eff B)  =  −∇× E                                … (II)
```
where `E = −∇φ + …` is the translational-sector field carried by `u`, `B` is the microrotational field carried by `ω`, and `J_coupling` is the axiom-native rotation↔translation LC coupling current (the ONLY place a winding can push the E-sector — the transducer candidate). All operators (`∇×`, `∇·`) are the srs/K4-native discrete exterior operators (the DEC `∂₁, ∂₂` of PR #483, reconciled: `BᵀB=−L0`), NOT Cartesian stencils (substrate-native-check).

---

## 2. THE CONTINUITY IDENTITY (the algebra — clean, no integrator)

Take the discrete divergence `∇·` of the Ampère equation (I). Using the DEC identity `∇·∇× ≡ 0` — the exact `∂₁∂₂ = 0` boundary-of-boundary identity, theorem-grade AND test-asserted on the srs 2-complex (merged main `src/ave/topological/srs_dec.py:242`, verbatim: *"div∘curl_adj = −∂₁∂₂ = 0 ← THE THEOREM's operator: any F=curl_adj(anything) has div F ≡ 0, hence zero enclosed charge"*; `test_srs_dec_operators.py:60` asserts `int(|∂₁∂₂|.max()) == 0` exactly):

```
∂_t (∇·(ε_eff E))  =  ∇·(∇×(μ_eff⁻¹ B))  −  ∇·J_coupling
                   =  0                    −  ∇·J_coupling        … (III)
                      └─ DEC ∇·∇×≡0 ─┘
```

**So the entire continuity behaviour of `∇·(ε_eff E)` is controlled by `∇·J_coupling`:**

- **`∇·J_coupling ≡ 0`** ⇒ `∂_t(∇·(ε_eff E)) ≡ 0` ⇒ **`∇·E` (the enclosed charge) is a CONSERVED constant of motion.** No dynamics can create monopole content that was not in the initial data. The dynamical route dies exactly as statics. → **route to lane Z + lane W.**
- **`∇·J_coupling ≠ 0`** ⇒ the coupling current is the source term `d/dt(∇·E) = −∇·J_coupling`, and IF `J_coupling` is built from the winding's ω without a topological-integer insertion, THAT term is the emergent transducer. → **the settling test has a live target;** ledger `J_coupling` hardest.

**This is the whole question, reduced to one term: is the axiom-native LC coupling current `J_coupling` DIVERGENCE-FREE?**

---

## 3. IS `J_coupling` DIVERGENCE-FREE? (the structural sub-question, three sub-cases)

The axiom-native rotation↔translation coupling has one canon-constrained FORM and a placement fork. The coupling current in the LC picture is the rate at which the rotational (μ/B) sector trades energy into the translational (ε/E) sector at the shared node. Three structurally distinct candidate forms, each with its divergence:

- **(J-curl) `J_coupling = ∇×(g(A) ω)`** — the coupling enters as a curl of a (saturation-weighted) rotational field (the natural "B drives E" Ampère form; `g(A)` from `S(A)`). **Then `∇·J_coupling = ∇·∇×(gω) ≡ 0` by the DEC identity.** ⇒ `∇·E` CONSERVED ⇒ dynamical route DIES. This is the same structural death as statics: a pure-curl drive has no divergence, sources no monopole. **This is the DEFAULT canon form** (Ampère's law drive is a curl), and it kills the dynamical route by the same `∇·∇×≡0` theorem that killed statics.
- **(J-grad) `J_coupling = ∇(h(A))`** — the coupling enters as a gradient of a saturation-scalar (a longitudinal drive). **Then `∇·J_coupling = ∇²h ≠ 0` generically** ⇒ `∇·E` is NOT conserved ⇒ a live source. BUT: this is a LONGITUDINAL coupling, and canon forbids a *propagating* longitudinal EM mode (`historical-precedents.md:21`, verified Stage-1 prereg correction item 2) — the static curl-free E is retained by Gauss, but a *dynamical* longitudinal drive `∇h(A)` would be exactly the object the corpus says does not propagate. So (J-grad) is either (a) a static-only re-derivation of the RETIRED Stage-2a mechanism (`h(A)` textures ε_eff → the same [NO-FLUX-STRUCTURAL] theorem), or (b) a forbidden propagating longitudinal mode. **Neither is a live new transducer.**
- **(J-mixed) `J_coupling = ∇×(g ω) + f(A,ω)·(coupling that is neither pure curl nor pure grad)`** — a genuinely NEW term whose divergence is nonzero AND that is not a forbidden longitudinal wave. This is the ONLY live case, and it requires a coupling current that (i) has a nonzero divergence, (ii) is built from the ω FIELD (no integer), (iii) is not a static-texture (else the [NO-FLUX-STRUCTURAL] theorem applies), and (iv) is not a propagating longitudinal mode. **No such term is written in the chartered host** (`u` has no stepper yet), and canon does not obviously supply one — the LC coupling is an Ampère (curl) drive by default.

---

## 4. THE ANSWER (surfaced, not steered)

**LEAN: the dynamical route ALSO dies structurally, by the SAME `∇·∇×≡0` theorem — UNLESS a specific mixed coupling term (J-mixed §3) exists that canon does not currently supply.**

The chain: the chartered LC coupling is an Ampère-form curl drive (`J_coupling = ∇×(gω)`, the default). Its divergence is identically zero (`∇·∇×≡0`, DEC theorem-grade). Therefore `∂_t(∇·E) ≡ 0` — the enclosed charge is a conserved constant of motion, set by initial data, not emergent. The DC monopole content the settling test would read is whatever was seeded, exactly the statics tautology in dynamical clothing.

**The ONE escape (the live target, if it exists):** a coupling current `J_coupling` with `∇·J_coupling ≠ 0` that is (a) ω-field-derived (no integer), (b) not a static texture (evades the [NO-FLUX-STRUCTURAL] theorem), (c) not a forbidden propagating longitudinal mode. This is the term to ledger hardest IF Stage-2b is built. But it is NOT in the chartered host today, and the default LC/Ampère coupling does not provide it.

**This is a `flag-don't-fix` surface, not a verdict I mint:** whether the axiom-native LC coupling is purely a curl-drive (⇒ route dies) or carries a divergence-bearing mixed term (⇒ live) is a FRAMING question about the coupling's form — the same class of question as the Stage-2a A-composition fork. It routes to Grant / the orchestrator review gate, NOT to a unilateral build.

**THE UNIFYING OBSERVATION (why statics AND curl-coupled dynamics die by the SAME theorem):** the DEC result names its own operator (`srs_dec.py:242`): *"div∘curl_adj = −∂₁∂₂ = 0 ← THE THEOREM's operator: any F=curl_adj(anything) has div F ≡ 0, **hence zero enclosed charge**."* Statics died because the winding's substrate flux `F = ∇×ω = curl_adj(ω)` is exactly such an F (a curl), so `∇·F ≡ 0` — no monopole (this is the OLD-cell closure the sibling DEC arc formalized). The curl-coupled dynamics dies for the identical reason: `J_coupling = ∇×(gω)` is again `curl_adj(·)`, so `∇·J_coupling ≡ 0`, so `∂_t(∇·E) ≡ 0`. **The same `∂₁∂₂=0` theorem closes both routes.** The ONLY escape (either statically or dynamically) is a mechanism whose source is NOT a pure curl of the ω field — which for statics was killed by the [NO-FLUX-STRUCTURAL] maximum-principle theorem (a texture is not a curl-source either), and for dynamics is the (J-mixed) term canon does not supply. This is why lane Z (the HARMONIC sector, which is precisely the `ker∂₁ ∩ ker∂₂ᵀ` complement that `∂₁∂₂=0` does NOT annihilate) is the structurally-distinct survivor: harmonic 1-cochains are neither exact nor co-exact, so the `∇·∇×≡0` theorem does not apply to them.

---

## 5. ROUTING RECOMMENDATION (for the orchestrator review gate)

1. **PRIMARY (highest-confidence):** the dynamical route leans structurally dead by `∇·∇×≡0` on the default Ampère-curl coupling. **Do NOT build the Stage-2b settling test until the coupling-form question (§3/§4) is resolved** — building a settler on a curl-only coupling would burn the same commits statics did, for the same structural reason.
2. **The live-target test IF Stage-2b proceeds:** the pre-reg must FIRST establish, analytically, that `J_coupling` carries a `∇·≠0` mixed term (§3 J-mixed) — the divergence-of-the-coupling is the make-or-break, checkable at equation-audit time BEFORE any integrator run (the discipline the Stage-2a anchor-source violated).
3. **PARALLEL (independent of the dynamical verdict) — lane Z:** the harmonic/topological sector (`b₁=3`, PR #483) is where non-contractible-cycle flux lives and is INVISIBLE to a scalar-φ co-exact channel. A charge-as-winding readout in lane Z needs an **edge-field E representation** (the 1-cochain, not the node potential) with the DEC harmonic projector — a genuinely different instrument that neither statics nor the curl-coupled dynamics can reach. This is the most likely home of any Link-counting emergence and does NOT depend on the §4 dynamical verdict.
4. **PARALLEL — lane W:** winding pairs (the field BETWEEN two windings; the clm-wcoul2 ω-sector force already measured). The pair-interaction may carry Coulomb even if the single-winding exterior does not (the Stage-0 §7 option-C hypothesis).

---

## 6. DISCIPLINE LEDGER

- **`verify-before-cite`:** `unified_engine.py:29-40` (the u/ω DOF map + "separately conserved grades"), `:114-115` (u dormant), `:386-396` (S(A) wired) all re-verified at HEAD this session. The DEC `∇·∇×≡0` (`∂₁∂₂=0`) is theorem-grade at PR #483 (reconciled at source in the retired Stage-2a work).
- **`substrate-native-check`:** the operators are the srs/K4-native discrete exterior `∇×, ∇·` (DEC `∂₁, ∂₂`), NOT Cartesian — the continuity identity `∇·∇×≡0` is the exact `∂∂=0`, not an approximate stencil identity.
- **`flag-don't-fix`:** the answer (route leans dead unless a mixed coupling exists) is SURFACED as a framing question to the orchestrator review gate, not resolved unilaterally. I do not build the settler.
- **Rule 11 / cheapest-decisive:** this note is the cheapest-decisive gate — an algebraic identity, no integrator. It prevents the Stage-2b build from burning commits on a structurally-dead curl-coupling (the exact failure the Stage-2a retirement teaches).
- **NO code:** per the panel directive, this is a note only. No harness, no settler, no driver.

**STOP after this note.** The Stage-2b prereg + build await the orchestrator review gate, with the coupling-divergence question (§3/§4) as its make-or-break entry condition.
