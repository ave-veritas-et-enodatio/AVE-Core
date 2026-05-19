# Prereg Outcome + Corpus-State Retrofit — 2026-05-18 ABCD Eigensolver Handoff Retired

**Date drafted**: 2026-05-18 night (post-handoff, post-review-of-review)
**Status**: ACTIVE — retires `2026-05-18_abcd-eigensolver-workstream-handoff.md`; partially retrofits `2026-05-18_q-g47-interpretation-g-result.md`
**Author**: AVE implementer lane, post-Grant "proceed full skills ahead" greenlight
**Trigger**: review-of-review of the 2026-05-18 ABCD handoff identified coordinate-system conflation; `ave-prereg` corpus-grep then surfaced that the corpus-canonical replacement methodology was ALSO already-closed.

## 0. TL;DR

The 2026-05-18 ABCD-eigensolver workstream handoff is **retired before any Phase 1 code is written**. The replacement methodology (doc 68 `relax_s11` coupled-engine extension) that the first review identified as "corpus-canonical" turns out to have been **implemented in spring 2026 (F17-K Phase 5, commits `6158465` → `2c873cf` → `4c9fbea`) and empirically falsified** — Golden Torus is NOT a stationary point of either Cosserat-energy or coupled-S₁₁ gradient flow. The corpus reframe (doc 72 §1.3, doc 03 §4.3): **GT is selected by topological-quantization ANSATZ, not by gradient flow on any objective the engine knows.**

The handoff and the Interpretation G result doc were both authored without engaging docs 71-78 (the F17-K closure + R7.1 reframe). Two artifacts are retrofitted; no code work proceeds without Grant arbitration on next steps.

**Net session-cost saved by firing `ave-prereg` before Phase 1**: ~2-4 hours of methodology that would have reproduced an already-on-file negative empirical finding.

## 1. What the prereg corpus-grep surfaced

Per `ave-prereg` Step 2, an `ave-corpus-grep` agent searched 10 repos + archive for prior work on the proposed methodology. Six topics, returned in 5 minutes. Key findings:

### 1.1 F17-K Phase 5 is implemented, ran, falsified — NOT a future plan

Verified by direct `git log` and file read:

- **Commit [`6158465`](https://github.com/...)** — F17-K Phase 5c v1: coupled S₁₁ relaxation infrastructure built (~290 LOC). v1 unconstrained descent on `(u, ω, V_inc)` joint state empirically falsified — descent over-saturated Cosserat (peak |ω| 0.94 → 2.19).
- **Commit [`2c873cf`](https://github.com/...)** — F17-K Phase 5c v2: dual descent with tanh reparam. Premature Finding 3 landed; empirically confounded (both descents at wrong amplitude).
- **Commit [`4c9fbea`](https://github.com/...)** — F17-K Phase 5c v2-v2: saturation-pin (peak |ω| = 0.9425 enforced). **Empirical closure of the F17-K arc.** Both objectives correctly pinned at saturation; topology preserved (c_cos = 3); each objective converges to distinct (R, r) NOT at GT:

  | Objective | iters | converged R/r | distance from φ² |
  |---|---|---|---|
  | Cosserat-energy | 78 | **3.40** | 1.30× |
  | coupled S₁₁ | 500 (still descending) | **1.03** | 0.39× |
  | corpus claim | — | φ² = 2.62 (Golden Torus) | — |

Verbatim from [VACUUM_ENGINE_MANUAL.md:1466](research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md) (`grep -n` confirmed):

> *"Phase 5c-v2-v2 seeded at Golden Torus geometry (R=20, r=20/φ²=7.64) and ran descent. Both descents drifted at iteration 1: energy moved (R, r) from (20, 7.6) → (25.4, 7.5); S₁₁ moved (20, 7.6) → (17.5, 17.0). The fact that descent moved immediately means **the gradient at Golden Torus is nonzero** in both objectives — Golden Torus is NOT a stationary point."*

### 1.2 The corpus reframe — topological quantization is INPUT, not OUTPUT

[doc 72_:51](research/_archive/L3_electron_soliton/72_vacuum_impedance_design_space.md:51) verbatim (citing doc 03_ §4.3):

> *"R·r = 1/4: topologically quantized, NOT dynamically derived... R·r = 1/4 is a topological identity that the Lagrangian must be consistent with but does not by itself produce. It follows from the requirement that the toroidal shell area match the spin-1/2 half-cover quantum π² of the SU(2) field — a quantization condition forced by the SU(2) → SO(3) double-cover structure that is **input** to the Lagrangian, not **output** of its energy functional."*

> *"R/r=φ² (or equivalently R·r=1/4 + R−r=1/2) is selected by ansatz initialization, not derived by gradient flow. F17-K v2-v2's failure to converge to GT under either objective is the corpus prediction holding empirically — neither objective KNOWS about topological quantization, so neither lands at the topologically-quantized point."*

This applies equally to the proposed ABCD eigensolve and to the doc-68 `relax_s11` path. Both are gradient-flow / linear-algebra methods on continuous objectives that don't encode the discrete topological-quantization constraint that *selects* GT from the continuous family of (2,3) stationary states.

### 1.3 V_ref is not independent state — joint-state Hessian retracted as A36

[`coupled_s11_eigenmode.py:21-24`](src/scripts/vol_1_foundations/coupled_s11_eigenmode.py:21) verbatim docstring:

> *"V_ref is NOT in the gradient descent state. V_ref is a derived quantity from V_inc via TLM scatter+connect; it gets reset each engine.step() call (which we don't call during S11 relaxation — relaxation is gradient descent, not time-evolution)."*

A prior attempt to descend on joint `(u, ω, V_inc, V_ref)` state ([commit `c69e79c`](research/_archive/L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md:20)) was **retracted as A36 Rule 6 violation** — joint-state Hessian over (u, ω, V_inc, V_ref) "misses sectoral structure" because V_ref is fully determined by V_inc once the TLM operator is fixed.

Both the original ABCD handoff §4 ("state vector (V, I)" — equivalent dimensionality) and the review's recommendation ("operating on the joint (V_inc, V_ref, u, ω) state") would repeat the A36 structural error if implemented. The corrected joint state per `coupled_s11_eigenmode.py` is `(V_inc, u, ω)` — V_ref derived by scatter-connect.

### 1.4 R7.1 (block Helmholtz) is the current canonical methodology and is partially RUN

Per [doc 74_ §4.5](research/_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md):

- **V-block result**: comprehensive Mode III at N=32 across ALL seeds (GT_corpus, F17K_cos_endpoint, F17K_s11_endpoint, vacuum_control). All return ~0.7158 rad phase, 1.22% off ω_C target. Shift-invert ensures this is the closest eigenvalue in the spectrum.
- **Cos-block result**: Mode III for the **bottom 100 of 196608 eigenvalues only**. Higher-frequency modes near ω_C² may exist but were not searched. Comprehensive coverage requires shift-invert at sigma=ω_C² via inner GMRES (~30 min - 2 hr per seed).
- **Negative control passes**: vacuum_control returns same Mode III as GT-family — no spurious bound-state artifact.

**What stays open** (verbatim from doc 74_ §4.5):

1. Cos-block comprehensive coverage at sigma=ω_C² shift-invert
2. Hybrid V≠0 ∧ ω≠0 seed test (Round 8 territory)
3. Larger N sensitivity sweep (N=64 or N=80 matching F17-K v2-v2's lattice size)
4. Round 8 architectural rework if all of the above return Mode III

### 1.5 The Outcome A result doc's R/r=13.29 measurement was an unphysical observable

Per [doc 29_ Finding F2](research/_archive/L3_electron_soliton/29_ch8_audit.md:17) verbatim:

> *"Ch 8 Golden Torus (R, r, d) = (0.809, 0.309, 1) is **not geometrically realizable as a real-space torus**: r < d/2 (poloidal radius less than tube radius) and R < d (major radius less than tube diameter)."*

And [doc 29_:89-91](research/_archive/L3_electron_soliton/29_ch8_audit.md:89):

> *"The two-node synthesis §4 says R, r are phase-space parameters — dimensions of the (V_inc, V_ref) phasor torus — not real-space torus dimensions. In phase space there's no 'tube' to fit around a centerline; the 'd = 1' constraint becomes a dimensionless phase-space unit, not a physical tube diameter."*
>
> *"If Ch 8 is genuinely making a real-space claim, it's falsified by elementary ropelength geometry. The phase-space reading is the only one that survives."*

[Vol 1 Ch 8](manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex:57) verbatim:

> *"The trefoil lives in phase space; the soliton lives in real space."*

The 2026-05-18 Outcome A result computed R, r in **real-space Cartesian coordinates** from a radial Riemann-invariant projection on the `MasterEquationFDTD` field (`R_meas = 0.131`, `r_meas = 0.0099`, `R/r = 13.29`). These are real-space observables compared to canonical targets that are **phase-space observables**. The 407% deviation is a coordinate-system mismatch, not a falsification of the GT claim.

Per doc 28_:80-87, the corpus has explicit precedent for separating these:

> *"Ch 8's Golden Torus is a PHASE-SPACE shape, not a sub-node Cartesian shape... Real-space R_real/r_real ≈ 2.27 is a DIFFERENT QUANTITY from phase-space R_phase/r_phase = φ². The TLM at multi-cell scale measures real-space envelope; the electron's 'Golden Torus' is in phase space. They needn't match."*

## 2. Retrofit scope — what changes, what doesn't

### 2.1 RETIRED ARTIFACT — `2026-05-18_abcd-eigensolver-workstream-handoff.md`

**Retirement reason**: methodology operates in wrong coordinate system per §1.5 above (real-space cavity discretization, see Phase 3 Step 1); proposed methodology is structurally equivalent to F17-K Phase 5 which is empirically closed (§1.1).

**Action**: top-banner the handoff as SUPERSEDED. Do not delete — the methodology-error analysis in the review-of-review is itself a useful corpus record.

**No code was written** against this handoff; no Phase 1 work is in flight. No code-level walk-back needed.

### 2.2 PARTIAL RETROFIT — `2026-05-18_q-g47-interpretation-g-result.md`

**Retrofit scope**:

| Section | Original framing | Retrofit |
|---|---|---|
| §1 TL;DR "Outcome A — geometry NOT realized" | Treated R/r=13.29 vs φ²=2.618 as falsification of GT claim | Add note: real-space R/r measurement is an unphysical observable per doc 29 F2; comparison to phase-space φ² target is category error. The Outcome A result does not falsify the GT claim. |
| §4.1 "Interpretation G CONFIRMED" | Same — geometric-mismatch attribution | Soften: 50% Λ gap is NOT explained by "geometry not realized at v14"; the corpus state (doc 72-74) identifies topological-quantization-input as the actual mechanism by which gradient-flow optima miss GT. |
| §4.3 "Nested-oscillator topology — NOT (2,3) torus knot" | Treated radial-shell mode segregation as falsification of (2,3) topology | KEEP (substantive real-space observation) but reframe: real-space radial-shell structure does not falsify phase-space (2,3) topology per doc 28 §4.2 ("they needn't match"). The 7/3 mode-ratio is a real-space observation of the v14 attractor, not a refutation of canonical phase-space (2,3). |
| §8 Closure pathway — ABCD eigensolver | Pointed at the now-retired handoff | Replace pointer with reference to this prereg-outcome doc + doc 74 §4.5 (canonical open follow-ups). |

The §5 reframing finding (doc 78 K4-TLM cross-validation Mode III FAIL) STANDS — that finding was correctly surfaced in the original result doc and remains substantive. But its load-bearing weight shifts: doc 78's Mode III result is now read in the corpus-canonical context that GT is topologically-quantized-input, so the K4-TLM evolve-and-measure result is expected (gradient-flow / time-evolve on continuous dynamics doesn't reach the discrete-topology-selected state).

### 2.3 BRANCH STATE update — weak-spot 2b

[`research/BRANCH_STATE_2026-05-18_analysis-divergence-test-substrate-map.md:119`](research/BRANCH_STATE_2026-05-18_analysis-divergence-test-substrate-map.md:119) currently reads:

> *"(2b) K4-TLM Q-factor route at 50% precision (Chain A5, audit-pending): ... Resolution path: finer-grid FDTD convergence study OR derivation of expected discrepancy."*

The "finer-grid FDTD convergence study OR derivation of expected discrepancy" framing is itself stale relative to docs 72-74. The actual canonical resolution path per the F17-K closure + R7.1 reframe is:

> Topological-quantization-input recognition (GT is ansatz-selected per doc 03 §4.3, not gradient-flow output) + R7.1 follow-ups per doc 74 §4.5 (Cos-block comprehensive coverage at sigma=ω_C²; hybrid V≠0 ∧ ω≠0 seed test; larger-N sensitivity sweep; Round 8 architectural rework if all return Mode III).

Update weak-spot 2b to reflect this. The 50% precision number `Λ_total = 102.78` itself stays valid; what changes is the diagnosed mechanism and the resolution path.

### 2.4 NOT CHANGED — Theorem 3.1' canonical leaf

The handoff's §9 walk-back propagation list included adding a §63b precondition paragraph to `theorem-3-1-q-factor.md`. Per the corpus-canonical retrofit:

- The Λ_i = Q_i bridge precondition (Golden Torus geometry) STILL holds as a structural statement of the bridge.
- But "geometry verification" no longer means a gradient-flow finds GT or an ABCD eigensolve recovers GT; per doc 03 §4.3 it means **topological-quantization-consistency** (SU(2) → SO(3) double-cover requires R·r = 1/4) which is verified by ANSATZ + SU(2) algebra, not by engine measurement.

A §63b note may still be useful, but its content shifts from "geometry must be realized by the bound-state engine" to "geometry is topologically-quantized input per doc 03 §4.3; engine measurement tests the consistency of the engine with this input, not the validity of the input." Defer this edit to a separate session — it's a Theorem 3.1' leaf revision, not a walk-back artifact.

### 2.5 NOT CHANGED — Foreword line 106

The handoff's §9 walk-back propagation list included foreword line 106 updates (Interpretation G flag). The current foreword line 106 framing — that the K4-TLM A5 chain is at 50% precision with explicit non-promotion — stands. The retired handoff was going to either (POSITIVE) remove the flag OR (NEGATIVE) strengthen the flag; neither is appropriate now. Leave foreword as-is.

## 3. Surface to Grant — next-step adjudication needed

The 50% Λ_total gap from doc 131 still wants closure. Per the corpus state, four candidate next steps (NOT mutually exclusive):

**Option A — Extend R7.1 to comprehensive Cos-block coverage** (~30 min - 2 hr per seed, total ~4-6 hr session). [doc 74_ §4.5](research/_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md) item 1. Shift-invert at sigma=ω_C² via inner GMRES; converts Cos-block result from "bottom-100 only" to comprehensive Mode III/II/I. Highest-priority canonical follow-up.

**Option B — R7.1 larger-N sensitivity sweep** (N=64 or N=80). [doc 74_ §4.5](research/_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md) item 3. At N=32 the (2,3) shell has minor radius ~3.8 cells (borderline-resolved); at N=64 better resolved; tests whether the 1.22% V-block gap closes at higher resolution.

**Option C — Hybrid V≠0 ∧ ω≠0 seed test** (Round 8 territory). [doc 74_ §4.5](research/_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md) item 2. If bound state genuinely lives at non-trivial cross-coupling, V=0 seed never finds it.

**Option D — Reframe Q-G47 Interpretation G away from "geometry verification"**. Given that GT is topologically-quantized-input (not engine-output), the question "does the engine realize GT" may be the wrong question. The right question becomes "does the engine bound state RESPECT the topological-quantization constraint?" — a different observable. Could reframe Interpretation G as "topological-quantization-consistency check" instead of "geometric-realization check."

**Recommend Option A as cheapest next step** (small scope, addresses a known incomplete result, doesn't require architectural rework). If Option A returns comprehensive Mode III, escalate to B or C. Option D is a framing-level reframe and warrants its own Grant-arbitration cycle.

The retired ABCD-eigensolver handoff's Phase 5 walk-back propagation list (foreword line 106, BRANCH STATE 2b, Theorem 3.1' leaf §63b, L5 Q-G47 row, Vol 1 Ch 8 §3) is mostly NOT executed by this retrofit. The minimal-disruption set is: this prereg-outcome doc + handoff banner + result-doc banner + BRANCH STATE 2b edit. Larger-scope walk-back is conditional on which Option (A/B/C/D) Grant picks.

## 4. Verified citations (per `verify-before-cite`)

| Citation | Verification command | Status |
|---|---|---|
| Commit `4c9fbea` "Golden Torus is topologically selected, not dynamically derived" | `git log --all --oneline \| grep 4c9fbea` | VERIFIED — full title matches verbatim |
| Commit `2c873cf` F17-K Phase 5c v2 (premature Finding 3) | same | VERIFIED |
| Commit `6158465` F17-K Phase 5c v1 (coupled S₁₁ infrastructure built) | same | VERIFIED |
| Doc 72 §1.3 "topologically quantized, NOT dynamically derived" | `sed -n '45,60p' 72_vacuum_impedance_design_space.md` | VERIFIED verbatim |
| VACUUM_ENGINE_MANUAL.md:1466 "Phase 5c-v2-v2 seeded at Golden Torus... drifted at iteration 1" | `sed -n '1440,1470p' VACUUM_ENGINE_MANUAL.md` | VERIFIED verbatim |
| Doc 29 Finding F2 "not geometrically realizable as a real-space torus" | `sed -n '15,20p' 29_ch8_audit.md` | VERIFIED verbatim |
| Doc 74 §4.5 "What stays open" — Cos-block coverage + hybrid seed + larger-N + Round 8 rework | `sed -n '126,135p' 74_r7_k4tlm_lctank_run_result.md` | VERIFIED verbatim |
| Vol 1 Ch 8 line 57 "trefoil lives in phase space; soliton lives in real space" | `sed -n '57p' 08_alpha_golden_torus.tex` | VERIFIED via corpus-grep agent (line 57) |
| `coupled_s11_eigenmode.py:21-24` "V_ref is NOT in the gradient descent state" | corpus-grep agent | VERIFIED verbatim |
| `cosserat_field_3d.py:1254` relax_s11 current line | corpus-grep agent | VERIFIED (drift from doc 68's :974) |

## 5. Skill audit trail

**Upfront skill-selection plan** (per `feedback_skill_selection_planning.md`): logged in conversation transcript prior to ave-prereg firing.

**Formal Skill invocations**:
1. `ave-prereg` — at session start of this retrofit. Step 1 + Step 1.5 written, Step 2 dispatched ave-corpus-grep agent.
2. `verify-before-cite` — adhered to internally for all citations above (load-bearing on the retrofit); verification commands documented in §4.

**Skills adhered to internally without formal Skill tool firing**:
- `ave-canonical-leaf-pull` — phase-space canon, Q-factor canon, F17-K canon, R7.1 canon enumerated via corpus-grep
- `consistency-vs-emergence` — the retrofit is INTRA-FRAMEWORK CONSISTENCY CHECK; reclassifies the original result accordingly
- `pre-test-physics-check` — surfaced to Grant via §3 (Options A/B/C/D enumeration)
- `phase-space-coordinate-check` — fired at test-design-stage (this retrofit, not the original handoff's Phase 4) — confirmed the original handoff was operating in wrong coordinates
- `ave-evidence-framing-discipline` — all "VERIFIED" / "retired" / "stays open" language pinned to verbatim citations

**Skills deferred to future workstreams**:
- `substrate-native-check` — fires when the next-step methodology (Option A/B/C/D) is chosen
- `ave-canonical-source` — fires when code is written for that methodology
- `ave-driver-script-honesty` — same
- `ave-walk-back` — minimal walk-back executed here; larger walk-back is conditional on Grant's next-step pick

**Sub-agent delegations**:
- `ave-corpus-grep` agent for Step 2 of `ave-prereg` (returned in 5 minutes; all citations verified)
- `ave-auditor` agent (PENDING — second-pass audit before staging commits)

## 6. File-edits in this retrofit

| File | Edit |
|---|---|
| `research/2026-05-18_abcd-handoff-prereg-outcome-corpus-state-retrofit.md` | NEW (this doc) |
| `research/2026-05-18_abcd-eigensolver-workstream-handoff.md` | Top banner: SUPERSEDED; pointer to this doc |
| `research/2026-05-18_q-g47-interpretation-g-result.md` | Top banner: PARTIAL RETROFIT; inline notes in §1, §4.1, §4.3, §8 per §2.2 above |
| `research/BRANCH_STATE_2026-05-18_analysis-divergence-test-substrate-map.md` | Weak-spot 2b: update resolution path per §2.3 |

No code edits. No leaf-level canonical edits. No foreword edits. No L5-status edits.

## 7. Provenance

**Drafted under**: Grant directive "proceed full skills ahead" after the review-of-review surfaced (A) coordinate-system conflation, (B) reciprocal-chirality structural error, (C) doc-68-`relax_s11`-not-engaged. The `ave-prereg` corpus-grep then surfaced that (C)'s recommended methodology was also dead-lettered.

**Pure-AVE-corpus rule** (per memory): all content above is pure physics. No external context.

**Net effect**: ~2-4 hours of methodology-implementation work avoided by firing `ave-prereg` before Phase 1. The corpus-grep saved both the originally-proposed methodology AND the review's recommended replacement methodology from being re-implemented.
