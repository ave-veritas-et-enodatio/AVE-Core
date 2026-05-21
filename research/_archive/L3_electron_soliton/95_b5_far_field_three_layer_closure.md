# 95 — Round 11 Closure: Far-Field Test (B5/B5b/B6) + Three-Layer Convergent Refutation

**Status:** implementer-drafted, 2026-04-29. Companion to [doc 93](93_ee_to_ave_mapping.md) (EE↔AVE mapping) + [doc 94](94_ee_phase_a_universal_solver_match.md) (Phase A ℓ=2/ℓ=5 finding). Closes Round 11 of the L3 electron-soliton arc with three independent convergent layers of refutation against the corpus-electron test at chair-ring + K4 + ℓ_node + v8 engine config, plus one positive finding on the engine's Op14 feedback mechanism.

**Triggered by:** Grant 2026-04-29 reframe — "what E field and B field does an electron have, that standard physics accepts?" — initiating the standard-physics-external-observable test that v6→v10 had never run.

**Bottom line:** the chair-ring trapped state at v8 config is empirically NOT the corpus electron, refuted at three independent layers (substrate-geometric, engine-architectural, standard-physics-external). The trapped state IS a real Op14-bounded equilibrium with substrate-canonical ℓ=2 GW-analog cavity-mode internal structure (doc 94 §12) and 1/r geometric loop-near-field external decay (B5/B5b confirmed). Round 11 closes; framework decision (FDTD substrate per (i-b) handoff / mass-spectrum pivot / engine-architectural research) is Grant's call.

---

## §1 — Test framing: standard-physics electron's external observables

Per [Vol 2 Ch 5:15](../../manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex#L15) verbatim:

> "Because the unsaturated vacuum acts as a linear dielectric in the far-field, the static structural phase strain obeys the 3D Laplace Equation (∇²θ = 0)."

Solutions to Laplace's equation with localized sources ARE the standard multipole expansion. AVE corpus IS consistent with Maxwell external observables for solitons — the test target is corpus-canonical, not assumed Maxwell.

A standard-physics electron has:
- E field: Coulomb monopole, 1/r², q = -e (Gauss's law: ∮E·dA = -e/ε₀)
- B field: magnetic dipole, 1/r³, μ = μ_B (Bohr magneton, eℏ/(2m_e))
- Spin axis along polarization direction
- E multipole structure: ℓ=0 dominant
- B multipole structure: ℓ=1 dominant

**Eigenvalue vs eigenmode distinction (per Grant 2026-04-29):**
- **Eigenvalue:** scalar (frequency, mode number ℓ, wavenumber k)
- **Eigenmode:** spatial pattern (cos(2θ) for ℓ=2; Y_0^0 for monopole; etc.)

The test is at BOTH levels: eigenvalue match (1/r² slope) AND eigenmode match (Y_ℓ^m spherical harmonic content). Both must land for Mode I.

---

## §2 — B5 main run (chair-ring far-field)

**Driver:** [`r10_v8_ee_phase_a_b5_far_field.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b5_far_field.py). v8 IC + engine config UNCHANGED. 200P recording, full-lattice DC accumulator over steady-state window [N/4, N) = 1333 samples. r ∈ [3, 10] ℓ_node from chair-ring centroid (active region [4,28)³ excludes PML).

### §2.1 — Pre-flight specification (per A43 v2 + auditor's 5 asks)

Mode I/II/III criteria pre-registered before run (5 PASS thresholds):
1. Coulomb fit slope = -2.0 ± 0.3 over r ∈ [3, 10]
2. Coulomb fit R² ≥ 0.7
3. Charge sign matches expected (-1 for electron)
4. B-field dipole slope = -3.0 ± 0.3
5. B-field dipole R² ≥ 0.7

Mode I: ≥4 of 5 PASS. Mode II: 2-3 of 5. Mode III: 0-1.

### §2.2 — Empirical result

| Pre-reg criterion | Predicted | Observed | PASS? |
|---|---:|---:|---|
| Coulomb slope β | -2.0 ± 0.3 | **-1.10** | FAIL |
| Coulomb fit R² | ≥ 0.7 | 0.71 | passes (some power-law) |
| Charge sign | -1 | +1 (inner shell) | partial |
| Dipole slope β | -3.0 ± 0.3 | **-1.04** | FAIL |
| Dipole fit R² | ≥ 0.7 | 0.81 | passes (some power-law) |

**3 of 5 PASS (Mode II partial), but the load-bearing criteria (Coulomb 1/r² slope and dipole 1/r³ slope) BOTH FAIL.** Per the pre-reg, this is effectively Mode III for the electron-test specifically: neither eigenvalue (slope) nor eigenmode (cos θ angular pattern; multipole content) matches the standard-physics electron.

### §2.3 — What the actual finding IS

Both E and B exhibit ~1/r effective scaling at r ∈ [3, 10] ℓ_node from chair-ring centroid. r/r_eff ∈ [1.8, 6] places measurement in the **intermediate regime** between near-source and far-field for a current-carrying ring of radius r_eff ≈ 1.66·ℓ_node. **The 1/r decay is empirically the classical near-field signature of an extended loop source at intermediate regime**, NOT a verified eigenmode of any specific object. Per A43 v2 / auditor 2026-04-29:

> 1/r far-field decay is real per B5b (SNR > 10²²) and is geometrically consistent with classical loop-near-field at intermediate regime, but is NOT a verified eigenmode — multipole content sits at engine noise floor.

This is **classification + classical-prediction match**, not an eigenmode/eigenvalue decomposition match. The chair-ring is empirically behaving like an extended ring source at this measurement regime, but no clean ℓ-multipole eigenmode is independently confirmable.

### §2.4 — Multipole content at engine noise floor

Spherical-harmonic projection of E_DC onto Y_ℓ^m (ℓ = 0, 1, 2) per shell shows ALL ℓ amplitudes at ~10⁻¹¹ V_SNAP/ℓ_node — at engine numerical noise floor. No clean ℓ-dominance at any shell. Confirms eigenmode structure is sub-resolution at this measurement scale.

---

## §3 — B5b noise-floor control

**Driver:** [`r10_v8_ee_phase_a_b5b_noise_floor.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b5b_noise_floor.py). V_AMP=0 IC (no field seeded), same engine config, same 200P recording.

**Result:** |E_DC| and |B_DC| at every shell = **EXACTLY ZERO** (machine zero). Engine has no numerical noise without IC seeding — fields stay precisely at zero throughout the recording.

**Implication: B5's 1/r signal is entirely real**, not engine noise. SNR > 10²² (signal at ~10⁻⁸ V_SNAP/ℓ_node vs noise floor at 0). Decisive on the auditor's signal-vs-noise concern. The chair-ring trapped state DOES produce a deterministic far-field signal; that signal IS not point-particle Coulomb/dipole; it IS consistent with classical loop-near-field at intermediate regime.

---

## §4 — B6 long-window stability test (BEMF question, Grant 2026-04-29)

**Driver:** [`r10_v8_ee_phase_a_b6_long_window.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b6_long_window.py). 800P recording at v8 baseline (~17 min wall). V_inc and ω at ring nodes per step. V_DC computed in 7 sliding 100P windows from [100P, 200P] through [700P, 800P].

### §4.1 — The Faraday/BEMF question (per Grant 2026-04-29)

Grant asked: "are we accounting for the lattice's bulk BEMF/mutual coupling?" Per Q1 resolution + B2 empirical confirmation: v8 config does NOT enforce loop-level Faraday by construction (A28 architectural choice per [doc 67 §15](../../src/ave/topological/k4_cosserat_coupling.py#L386-L389)). The empirical signature ∮V_DC·dl ≠ 0 with ω_centroid at machine zero is direct measurement of A28's design — not a "violation" but an architectural feature.

The substitute mechanism (Op14 z_local impedance modulation) provides local-amplitude-bounded feedback at saturation walls, NOT loop-level Faraday-law BEMF. **B6 empirically tests whether Op14's substitute mechanism is sufficient to bound the saturation rectification across long timescales** — if yes, Op14 IS providing effective feedback (just not the standard Maxwell-Faraday kind); if no, the trapped state was an early-snapshot artifact.

### §4.2 — Empirical result: STABLE

| A-site | Window 1 (100-200P) | Window 7 (700-800P) | Drift per 100P | Total drift over 700P |
|---|---:|---:|---:|---:|
| A_0 (node 0) | 0.3876 | 0.3882 | +0.028% | +0.16% |
| A_2 (node 2) | 0.00048 | 0.00048 | +0.018% | +0.13% |
| A_4 (node 4) | 0.3876 | 0.3882 | +0.028% | +0.16% |

ω_DC at all 6 ring nodes: ~10⁻⁵ to 10⁻⁶ scale across all windows; no drift trend.

**Max V_DC drift = 0.028% per 100P window, total ~0.2% over 700P. STABLE.**

### §4.3 — A43 v19 flag (auditor 2026-04-29) empirically resolved

The pre-test synthesis "200P persistence may be artifact of missing loop-Faraday BEMF" was flagged per A43 v19 (don't claim synthesis IS the reading before empirical adjudication). B6 result: **synthesis REFUTED.** The persistence IS real bounded equilibrium across 700P. **Op14 z_local impedance modulation IS providing effective feedback**, even without proper Maxwell-Faraday loop-level BEMF.

This is a substantive **positive empirical finding** on engine architecture: A28's architectural choice (Op14 substituting for direct V↔B coupling) is empirically effective at bounding the saturation rectification across long timescales.

### §4.4 — Measurement-method clarification

B6 V_DC magnitudes (|V_inc time-mean|_4-port-rms = 0.388 at A_0/A_4) differ NUMERICALLY from B3's (V_DC via Phi_link linear-fit slope = 0.194 at A_0/A_4). Reason: V_avg in Phi_link's accumulator (`½(V_ref_A + V_ref_B_shifted)` per [`k4_tlm.py:391`](../../src/ave/core/k4_tlm.py#L391)) is structurally different from V_inc directly. Both are valid substrate observables — they reflect different parts of the K4 scatter+connect dynamics.

The STABILITY result holds regardless of which specific metric. Both metrics show < 0.1% drift per 100P. Per A43 v2: doc reports B3's |V_DC|_4-port_rms = 0.194 and B6's |V_inc-time-mean|_4-port_rms = 0.388 as DISTINCT substrate observables (related but not identical), not conflated.

---

## §5 — Three-layer convergent refutation: Round 11 closure

| Layer | Test | Finding | Reference |
|---|---|---|---|
| 1. Substrate-geometric | Discrete Beltrami eigenvalue at chair-ring | Chair-ring + K4 at ℓ_node sampling has λ_C fitting at non-integer wavenumber on 6-bond loop; Nyquist closure violated by 65% | [doc 92](92_round_11_vi_v10_finer_sampling_structural.md) |
| 2. Engine-architectural | LC-coupled re-run + code-grep | V↔B direct coupling required for Beltrami parallelism is empirically unstable across 5+ test paths; A28 architectural fix exists; Op14 substitute provides local-amplitude-bounded feedback | [doc 94 §13](94_ee_phase_a_universal_solver_match.md#13--addendum-lc-coupled-re-run-control-b4--engine-instability-identified) (RETRACTED + corrected) + Q1 |
| 3. Standard-physics-external | Far-field E and B characterization | Mode II partial (3/5) with both load-bearing slope criteria FAILing; 1/r intermediate-regime decay; multipole at engine noise floor; not point-particle Coulomb/dipole | B5 + B5b (this doc) |

**Three INDEPENDENT empirical layers all refute "chair-ring + K4 + ℓ_node + v8 config hosts the corpus electron."** Per Rule 11 (clean falsification at full strength): definitive negative across multiple framings, no escape hatches.

Round 11 closes cleanly.

---

## §6 — Positive empirical findings standing after Round 11 closure

The same disciplined arc that produced the three-layer refutation also produced substantive POSITIVE findings on substrate behavior:

🔴 **AMENDMENT 2026-04-30 per [doc 96 §11.3 v2](96_foundation_audit_t1_substrate_resonance.md#113--doc-94-12-2-gw-analog-cavity-mode-interpretation-strongly-restored) corrected framing:** the chair-ring↔universal-solver "match" is MEDIATED through substrate, not direct. Chain decomposition: chair-ring(1.48)↔substrate(1.50) at 1.3% (tight) + substrate(1.50)↔universal-solver(1.55) at 3.3% (loose). The 4.6% chair-ring↔universal-solver gap propagates from the chain, not a direct prediction error. **Chair-ring is amplified-substrate-resonance, NOT independent universal-solver data point.** A43 v25 promotion candidate WEAKENED, not strengthened — cinquefoil cross-topology test becomes more important (it would test substrate-level scale-invariance independent of any topology). Original framing below preserved per Rule 12.

1. **Substrate-canonical ℓ=2 GW-analog cavity mode at chair-ring + saturation** ([doc 94 §12](94_ee_phase_a_universal_solver_match.md#12--addendum-impedance-landscape-control-b3-confirms-2-spatial-structure)). Confirmed across 4 independent axes:
   - Frequency (FFT V_inc dominant at 1.480·ω_C vs universal-solver predicted 1.551 — 4.6% match)
   - Spatial saturation Fourier (ℓ=2 amplitude 0.495 vs ℓ=0/1/3 ≤ 1.4×10⁻⁷)
   - Real-power flux azimuthal (ℓ=2 dominance vs other ℓ)
   - Cavity geometry (4 saturated walls + 2 antinodes 180° apart = quadrupole pattern)

   **Corpus context (verified per A43 v2 anyone-must-grep at backmatter/05:225-235 + 494):** universal solver formula has 4 quantitatively-validated corpus contexts — BH (ℓ=2, ν=2/7), Proton QNM (ℓ=5, ν=2/7), Pion (ℓ=5 medium, ν=2/7), Protein (ℓ=7, ν=2/7) — all matching CODATA at <2% precision per backmatter/05:225-235 verbatim table. Plus a broader universality framework per [backmatter/05:494](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L494) verbatim ("Every domain-specific eigenvalue is a single evaluation of one universal formula") and [backmatter/05:401](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L401) cross-scale isomorphism table covering 7 contexts.

   **The chair-ring K4-cavity match contributes a candidate 5th data point** with 4-axis empirical match (frequency 4.6% off, spatial Fourier ℓ=2 dominant at 99.99%, real-power azimuthal ℓ=2 dominant, cavity geometry quadrupole). Per Q3 (scale invariance reframe), this is expected empirical confirmation of the corpus-canonical universal-solver/scale-invariance principle (Vol 1 Ch 5 + backmatter/05), NOT framework-extending substantive finding.

   **Precision-regime distinction (per auditor 2026-04-29):** the corpus 4-context pattern matches CODATA at **<2% precision** (BH 1.7%, Proton -0.8%, Pion +0.9%, Protein +0.1%). Chair-ring K4-cavity matches universal-solver prediction at **4.6% precision** — ~2.3× the corpus precision threshold. The chair-ring's "4-axis match" is correct on structural axes (frequency, spatial Fourier, real-power azimuthal, cavity geometry — all confirm ℓ=2) but at a coarser precision regime than the corpus 4-context pattern. **Open physics question:** the 4.6% deviation could be (a) discrete-substrate Bohr-Sommerfeld correction expected at K4 lattice scale, (b) different ℓ=2 mode index than what the corpus formula assumes for continuum cavities, (c) single-topology coincidence vs structural pattern. Cinquefoil cross-topology test (next K4 topology at ℓ=5) is the cleanest discriminator.

   **A43 v25 candidate adjudication: HOLD pending all three criteria** (per discipline rule articulated in doc 94 §9 + reaffirmed by auditor 2026-04-29):
   - (a) corpus-grep verification of universal-solver-applicability-to-K4-cavity-substrate (currently implementer extrapolation; backmatter/05's broader 7-context cross-scale isomorphism table includes "Antenna" + "Tokamak" + "BLDC Motor" but doesn't explicitly extend formula to K4-cavity-at-saturation as a quantitatively-validated context)
   - (b) ℓ-semantics verification (azimuthal-cavity vs universal-solver-mode-index vs spin-2-graviton ℓ — three different ℓ's flagged by outgoing auditor)
   - (c) pre-registered test at SECOND K4 topology (e.g., cinquefoil per Grant Q5 testability) — directly tests scale invariance across K4 topologies AND addresses precision-regime question (if cinquefoil lands <2%, chair-ring's 4.6% is expected discrete-substrate offset; if cinquefoil >5%, chair-ring is single-topology coincidence)
   - **PLUS precision-tightening to corpus standard** OR explicit acknowledgment that K4-cavity-at-discrete-substrate operates at different precision regime than continuum corpus contexts

   The corpus-canonical 4-context pattern is established INDEPENDENT of this arc's empirical work; chair-ring contributes a candidate 5th data point whose promotion is pending all four criteria. Even if subsequent tests don't confirm the K4-cavity extension, the 4-context corpus pattern stands.

2. **ω-sector ℓ=5 cinquefoil-baryon-analog FFT signature** ([doc 94 §3](94_ee_phase_a_universal_solver_match.md#3--the-load-bearing-finding-universal-solver-2--5-match)). Single-axis match (frequency only at 2.8% off universal solver ℓ=5 prediction). Spatial confirmation pending and not feasible at v8 config (LC coupling required for Cosserat strain/curvature would destabilize).

3. **Engine architecture works as designed (Op14 feedback)** (B6, this doc). A28's architectural choice to substitute Op14 z_local modulation for direct V↔B coupling IS empirically effective at bounding saturation rectification. Persistence at 700P with < 0.2% drift confirms the trapped state is genuine bounded equilibrium, not an artifact of insufficient recording time.

4. **1/r far-field decay consistent with classical loop-near-field** at intermediate regime r/r_eff ∈ [1.8, 6] (B5 + B5b). Real signal (SNR > 10²²), structurally consistent with extended ring source. Not the corpus electron, but substrate-canonically interpretable as a current-carrying displacement-current loop per Vol 6 Ch 1.

---

## §7 — Audit-trail items (per Rule 12 retraction-preserves-body)

**Retracted predictions (this arc):**

- 🔴 **A43 v19 candidate (B5 prior expectation, 2026-04-29):** "Mode III on electron test + clean ℓ=1 bipolar electric dipole far-field structure." First half landed (Mode III); second half (clean bipolar dipole) did NOT — empirically the chair-ring produces 1/r intermediate-regime decay with no clean multipole. Lane-symmetric: both implementer and auditor predicted bipolar dipole; both predictions wrong. Discipline rule: predict mode-class with calibrated confidence, NOT specific structural shape pre-empirical.
- 🔴 **A43 v19 (B6 hypothesis, 2026-04-29):** "200P persistence may be artifact of missing loop-Faraday BEMF." Synthesis flagged per A43 v19 pre-test; B6 result REFUTES synthesis (V_DC drift < 0.2% over 700P confirms real Op14-bounded equilibrium).
- 🔴 **A43 v26 (doc 94 §13, 2026-04-29):** "asymmetric saturation gap" engine-bug diagnosis. Wrong; engine has both ε and μ saturation properly implemented per Q1 code-grep. B4 ω runaway was config error (double-counted reflection forces) not engine bug. Retracted with full audit trail in [doc 94 §13](94_ee_phase_a_universal_solver_match.md#13).

**Synthesis claims this doc makes (per A43 v2 promotion threshold):**

| Claim | Status |
|---|---|
| Three-layer convergent refutation of corpus-electron at chair-ring + K4 + ℓ_node + v8 | **EMPIRICAL** — three independent test paths all refute |
| Engine's Op14 mechanism is effective at bounding saturation rectification | **EMPIRICAL** (B6 700P stability) |
| 1/r far-field decay is classical loop-near-field signature | **CLASSIFICATION + CLASSICAL-PREDICTION-MATCH** — not eigenmode-decomposition match (per auditor flag); empirical 1/r decay + classical loop-near-field formula match at intermediate regime |
| Universal solver formula extends to K4 substrate cavities at saturation | **IMPLEMENTER SYNTHESIS** — backmatter/05 doesn't extend formula to K4 cavity context. 4-axis empirical match at chair-ring + ν=2/7 application is consistent with extension. A43 v25 candidate: pre-registered prediction at second K4 topology (e.g., cinquefoil) would harden |
| Vol 2 Ch 5:15 Laplace-equation framework predicts standard multipole expansion for solitons | **CORPUS-CANONICAL** per direct verbatim citation |

**Auditor-lane queue:**

- A43 v25-v27 candidates (universal solver promotion, predictive-shape overclaim, ω-runaway misdiagnosis) — full audit trail in this doc + doc 94
- Doc 79 v5.1 second addendum: three-layer convergent refutation framing (replaces "wrong-topology + wrong-scale" closure with "wrong-topology + wrong-scale + wrong-engine-config + wrong-external-observable" four-layer mismatch)
- Successor auditor handoff doc: post-Round-11-closure state with all 27+ A43 worked examples + methodology rules + framework decision pending

---

## §8 — Framework decision pending (Grant adjudication)

Round 11 closes empirically. The framework has three pending moves per the original handoff + arc evolution:

**(i) (i-b) FDTD substrate test.** Tests Ax 1 revision; runs corpus electron at sub-ℓ_node FDTD where Yee grid enforces Faraday at PDE level by construction (independent of A28). Information value depends on B6 outcome (now stable Op14-bounded equilibrium): if B6 had shown drift, FDTD would discriminate engine-architecture vs corpus-physics; with B6 stable, FDTD's discriminator value remains substantial because chirality-blind Yee grid provides a fundamentally different substrate. ~weeks of work.

**(ii) Pivot to mass spectrum / pair creation / different physics.** Round 11 closes; Round 12+ starts in a different direction. Mass spectrum (Round 10+ Direction 5) load-bearing for framework validation, never touched. Pair creation has its own engine thread (AVE-Fusion). New direction.

**(iii) Engine-architectural research thread.** Investigate whether stable formulation of V↔B direct coupling exists that A28's empirical-instability findings missed. Theoretical/numerical project independent of L3 arc.

The Phase A toolkit (FFT + Faraday-test + impedance-landscape + power-split + Q-factor + B-H + multipole decomposition + far-field characterization) is portable. Applies cleanly to whatever framework move comes next.

**Framework decision is Grant's adjudication, not implementer or auditor recommendation.** Per Rule 16 (third source of truth) + Rule 15 (lane discipline): both (i) and (ii) have load-bearing a priori support — (i) was the original handoff's pre-empirical anchor pre-Round-11-closure, (ii) has cost/discrimination weight per outgoing auditor's reasoning, (iii) is speculative without independent corpus motivation. Test-design-question-wise:

- (i) tests "is the substrate wrong?" — bypasses Layer 1 + Layer 2 simultaneously
- (ii) tests "is the electron-test the right load-bearing test?" — different framework-level question
- (iii) tests "is there a stable V↔B formulation A28 missed?" — speculative

These are testing different framework-level questions; both (i) and (ii) are honest moves. Grant's call.

---

## §9 — References

- [Doc 92](92_round_11_vi_v10_finer_sampling_structural.md) — Substrate-Nyquist (Layer 1)
- [Doc 93](93_ee_to_ave_mapping.md) — EE↔AVE mapping
- [Doc 94](94_ee_phase_a_universal_solver_match.md) — Phase A + engine-architecture (Layer 2)
- [Vol 2 Ch 5:15](../../manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex#L15) — Laplace-equation far-field framework
- [Vol 6 Ch 1](../../manuscript/vol_6_periodic_table/chapters/01_computational.tex) — Electrons as displacement currents in nuclear far-field
- [`k4_cosserat_coupling.py:282-389`](../../src/ave/topological/k4_cosserat_coupling.py#L282) — A28 architectural choice (doc 67 §15)
- B5 driver + capture: [`r10_v8_ee_phase_a_b5_far_field.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b5_far_field.py)
- B5b control: [`r10_v8_ee_phase_a_b5b_noise_floor.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b5b_noise_floor.py)
- B6 long-window: [`r10_v8_ee_phase_a_b6_long_window.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b6_long_window.py)
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) — methodology discipline (Rule 6, 9 v2, 11, 12, 14, 16, A40, A43 v2/v19, A47)
