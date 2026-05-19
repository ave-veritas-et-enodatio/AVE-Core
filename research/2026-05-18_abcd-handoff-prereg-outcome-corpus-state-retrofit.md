# Prereg Outcome + Corpus-State Retrofit — 2026-05-18 ABCD Eigensolver Handoff Retired

> # ⚠️ v2 ADDENDUM 2026-05-19 — §3 Options STALE; see [v2 addendum at bottom](#v2-addendum-2026-05-19----3-options-retired-l3-branch-already-closed)
>
> §3 Options A/B/C/D of this doc were themselves stale relative to HEAD. Grant's "proceed with A" + a follow-up `ave-prereg` corpus-grep surfaced that:
> - **Option A** (Cos-block shift-invert at sigma=ω_C²): ALREADY DONE at `src/scripts/vol_1_foundations/r7_cos_block_shift_invert.py` — Mode III on all 4 seeds at 1.04-2.00% rel_diff
> - **Option B** (larger-N sweep): ALREADY DONE at `r7_cos_block_n64_topology.py` — Mode III + BULK mode (shell_fraction 1.5%)
> - **Options C/D** (hybrid V≠0 ∧ ω≠0 / reframe): ALREADY ADDRESSED by path α v1/v2/v3 → all Mode III; closed by [doc 79 v5.2](_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md) Three-Layer Convergent Refutation (2026-04-29)
> - **Grant adjudicated Framework Decision (ii)** per [doc 98](_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md) on 2026-04-30: mass spectrum / pair creation is the active track; L3 electron-modeling branch closed.
>
> This doc's body below remains accurate for the ABCD-handoff retirement (§1-§2 + §4) but §3 Options A-D are retired as stale. **Same failure mode as the original handoff**: citing static research-doc state ("doc 74 §4.5 What stays open") as if it were dynamic-current-state, when the corpus had closed those items in docs 75-99 over the subsequent ~3 weeks.
>
> Meta-pattern: this is the SECOND time in the same session that `ave-prereg` caught a methodology proposal as already-closed. The discipline is working. Skill-extension proposal in v2 addendum §M.
>
> ---

**Date drafted**: 2026-05-18 night (post-handoff, post-review-of-review)
**Status**: ⚠️ §3 SUPERSEDED by v2 addendum 2026-05-19; §1-§2 + §4 still accurate for ABCD-handoff retirement
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

---

# v2 Addendum 2026-05-19 — §3 Options Retired; L3 Branch Already Closed

**Status**: corrects this doc's §3 Options A/B/C/D framing. The body above retires the ABCD handoff correctly; the forward-looking §3 was itself stale.

## v2.0 — What happened

Grant said "proceed with A" (Option A from §3 above: Cos-block comprehensive shift-invert at sigma=ω_C²). Per discipline, `ave-prereg` fired before any code, dispatched `ave-corpus-grep`. The corpus-grep returned: **Option A is already done.** Plus B is also done. Plus C and D are addressed. Plus the entire L3 electron-modeling branch closed at [doc 79 v5.2](_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md) on 2026-04-29 with three-layer convergent refutation, and Grant adjudicated [Framework Decision (ii)](_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md) (mass spectrum / pair creation) on 2026-04-30.

The §3 Options came from citing [doc 74 §4.5 "What stays open"](_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md) as if it were current state. But doc 74 was written ~2026-04-26; over the subsequent ~3 weeks the corpus closed all four items via docs 75 → 99. This is the same failure mode the body of this retrofit doc was retiring for the ABCD handoff — citing a dated doc's "open" list without verifying current state.

## v2.1 — Verified current state (per `verify-before-cite` discipline)

### Option A — N=32 Cos-block shift-invert: DONE Mode III

[`src/scripts/vol_1_foundations/r7_cos_block_shift_invert.py`](src/scripts/vol_1_foundations/r7_cos_block_shift_invert.py) exists; [results JSON](src/scripts/vol_1_foundations/r7_cos_block_shift_invert_results.json) shows:
- sigma = 1.0 (ω_C² in natural units)
- N = 32
- Tolerance = α ≈ 0.00730
- All 4 seeds completed: GT_corpus (rel_diff 2.00%), F17K_cos_endpoint (1.04%), F17K_s11_endpoint (1.98%), vacuum_control (1.58%)
- `pass_seeds: []` — Mode III across all 4
- Per-seed wall time: 626-794s; per-seed gmres call count: 119-153

Reframes doc 74 §4.2's original "Cos-block Mode III for bottom-100 only" caveat: per [doc 74_:186](_archive/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md:186) verbatim, *"The earlier 71.85% rel_diff in SA-mode was an incomplete-coverage artifact... The actual gap is ~1-2%, not 72%."*

### Option B — N=64 sensitivity sweep: DONE Mode III + BULK

[`src/scripts/vol_1_foundations/r7_cos_block_n64_topology.py`](src/scripts/vol_1_foundations/r7_cos_block_n64_topology.py) exists; [results JSON](src/scripts/vol_1_foundations/r7_cos_block_n64_topology_results.json) shows:
- N = 64, R_anchor = 10.0, r_minor = 3.82 (Golden Torus)
- closest_eigenvalue = 1.0281; closest_rel_diff = 1.39%
- frequency_pass: false
- **shell_fraction = 0.0151** vs Mode-I threshold 0.8 — **BULK mode**, NOT (2,3) localized
- bulk_uniform_expectation = 0.00575
- verdict: *"MODE III — Cosserat sector also empty. No eigenvalue within α tolerance of ω_C². V-pressure AND ε-strain/κ-curvature both empty. Round 8 Φ_link sector becomes cleanest gap."*

Commits: `b5ecc89` ("Mode III at N=32 FALSIFIED as finite-N artifact; Mode I CANDIDATE at N=64 V-block GT_corpus") then `b8d97d9` ("topology check FALSIFIES Mode I candidate — N=64 V-block GT_corpus is BULK mode (shell fraction 1.13%, not (2,3) localized); third headline flip; Round 8 questions restored").

### Options C + D — addressed by path α v1/v2/v3 + doc 79 closure

Per [doc 79 v5.1](_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md) (2026-04-28) the cumulative empirical state is **10 pre-registered tests at engine-representable corpus GT, all Mode III**:

1. R7.1 V-block N=32 — Mode III
2. R7.1 V-block N=64 — Mode III
3. R7.1 Cos-block N=32 — Mode III (Option A above)
4. R7.1 Cos-block N=64 — Mode III (Option B above)
5. R7.2 G-13 pair injection — Mode III
6. Test B v2 8-port spatial 0.5·V_SNAP — Mode III
7. Test B v3 8-port spatial 0.85·V_SNAP — Mode III
8. Path α v1 (V_inc/V_ref bond-pair) — Mode III
9. Path α v2 (Φ_link/ω_axial bond-pair) — Mode III (Option C: hybrid V≠0 ∧ ω≠0 / Φ_link sector)
10. Path α v3 (3D-aligned ω-vector, 5 sampler views) — Mode III + **partial positive on chirality** (100% CCW consensus per view (c) Φ_link, |ω|)

Doc 79 v5.1 closes Mode III canonical across V_inc/V_ref + Φ_link sectors + auditor (δ) 3D-axis interpretation.

### v5.2 Three-Layer Convergent Refutation (2026-04-29)

Per [doc 79 v5.2 second addendum](_archive/L3_electron_soliton/79_l3_branch_closure_synthesis.md) lines 663-712:

| Layer | Test | Finding | Reference |
|---|---|---|---|
| 1. Substrate-geometric | Discrete Beltrami eigenvalue at chair-ring | λ_C = 2π·ℓ_node fits at non-integer wavenumber on 6-bond loop; Nyquist closure violated by 65% | doc 92 |
| 2. Engine-architectural | LC-coupled re-run + code-grep | A28 architectural choice suppresses V↔B direct coupling; Op14 z_local substitutes; Faraday-law BEMF not enforced | doc 94 §13 + doc 95 §4 |
| 3. Standard-physics-external | Far-field E and B characterization | Mode II partial (3/5) with Coulomb 1/r² AND dipole 1/r³ slope criteria FAILing; 1/r intermediate-regime decay; multipole content at engine noise floor | doc 95 |

Closure shape: *"corpus electron substrate is elsewhere (sub-ℓ_node FDTD per (i-b) original handoff, OR a different scale entirely)."*

### Grant Framework Decision (ii) — 2026-04-30

Per [doc 98_:5](_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md:5) verbatim: *"Per Grant's direction 2026-04-30: '(ii) works' — Framework Decision (ii) activated as next research track."*

Three-phase activation plan in doc 98 §3:
- Phase 1 (~1-2 days): baryon ladder extension beyond c=13
- Phase 2 (~1 week): W/Z/Higgs eigenvalue solver
- Phase 3 (~weeks): lepton/neutrino mass-spectrum solver + PMNS

Empirical anchors already in place per doc 98 §0:
- Proton mass: 0.002% accuracy via BARYON_LADDER + Faddeev-Skyrme
- Baryon ladder c=5,7,9,11,13: ±2.4% of PDG
- Atomic orbitals Z=1-10: ±5.5% (H at +0.06%, O at -0.14%)

## v2.2 — Action: retire §3 Options; surface actual state to Grant

**No code work to do.** The work this doc's §3 recommended is already done; the L3 electron-modeling branch is closed; the active track is Framework Decision (ii) per doc 98.

What's actually pending (per doc 79 v5.2 §711 + doc 98 §3 activation plan, ~2-3 weeks ago) — but Grant should confirm current state:

| Question | Doc-99 era state |
|---|---|
| Phase 1 baryon ladder extension (c=15, 17, …) | Status unverified — not searched this corpus-grep |
| Phase 2 W/Z/Higgs solver | Status unverified |
| Phase 3 lepton/neutrino solver | Status unverified |
| Q-G47 50% Λ_total gap (the original concern that started this whole chain) | Reframed by doc 79 v5.2 as "corpus electron substrate is elsewhere"; not a geometric-realization gap |

## v2.3 — Walk-back propagation needed

The 2026-05-18 BRANCH STATE doc + the (now-retired) ABCD handoff + my v1 retrofit doc all operated on a stale L3 picture. The corpus had moved 21+ docs forward (doc 74 → doc 99+) but the BRANCH STATE 2b paragraph still referenced doc 74-era resolution paths.

Files this v2 retrofit propagates to:

| File | Edit |
|---|---|
| this doc (§3 banner + v2 addendum) | DONE inline above |
| `research/BRANCH_STATE_2026-05-18_analysis-divergence-test-substrate-map.md` weak-spot 2b | Update to cite doc 79 v5.2 + doc 98 Grant adjudication instead of doc 74 §4.5 |

NOT changed:
- The original retired ABCD handoff — still correctly retired
- The 2026-05-18 result doc banner — still correctly retired
- Any leaf-canonical content — none touched

## v2.M — Meta-pattern: `verify-before-cite` failure axis on "what's open"

This is the SECOND time in the same session that `ave-prereg` caught a methodology proposal where the corpus-grep returned "already done":

1. **First time**: original ABCD handoff (commit `cbf3373`) proposed methodology equivalent to F17-K Phase 5; corpus had F17-K closed at commit `4c9fbea`. Caught by review-of-review + this doc's v1.
2. **Second time**: this doc's v1 §3 proposed Options A/B/C/D citing doc 74 §4.5 "What stays open"; corpus had closed all four via docs 75-99. Caught by this v2 addendum.

Both failures share the same axis: **citing a dated research doc's "open items" list as if it were dynamic-current-state**, when the corpus has subsequent docs closing those items.

`verify-before-cite` skill currently mandates verbatim-quote verification. It does NOT currently mandate **status-claim verification** — that "doc X says Y is open" requires checking whether Y is still open at HEAD (via git log on related code/docs since doc X's date), not just verifying the quote.

Proposed skill extension (queued, not landed here): `verify-before-cite` should add a step for citations of the form "X is open / X is pending / X is the next step / Y stays open" — these need TWO verifications: (1) the quote is verbatim, (2) the status is still current at HEAD. Without (2), the citation is verbatim-correct but load-bearingly-wrong.

This pattern is structural to AVE corpus citation work because research-doc state is dynamic (~1-3 days/doc cadence at active branches) and citations naturally form chains across docs that the agent treats as time-invariant.

## v2.N — Provenance

**Drafted under**: Grant directive "proceed with A" (Option A from §3). `ave-prereg` fired before any code; `ave-corpus-grep` agent returned the already-done finding within ~2 minutes.

**Verified citations** (per `verify-before-cite`):
- `r7_cos_block_shift_invert.py` file exists at HEAD; results JSON readable; all numerical claims verbatim from JSON read
- `r7_cos_block_n64_topology.py` file exists; results JSON readable; same
- Commits `b5ecc89`, `b8d97d9`, `88ec7c3`, `baadc33` exist via `git log --all --oneline`
- Doc 79 v5.1 + v5.2 text verified verbatim at quoted line ranges
- Doc 98 line 5 Grant directive verbatim verified

**Net effect**: ~2-4 hours of work avoided again. The skill-discipline pattern is robust under stale-state pressure.

**Pure-AVE-corpus rule** (per memory): pure physics throughout; no external context.
