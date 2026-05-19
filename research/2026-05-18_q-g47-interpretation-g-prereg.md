# Pre-Registration — Q-G47 K4-TLM A5 Interpretation G Geometry Verification

**Date**: 2026-05-18 night
**Target test**: K4-TLM A5 (α-derivation chain via Λ_total Q-factor decomposition) — Interpretation G closure pathway
**Per**: `research/2026-05-18_k4-tlm-a5-alternative-interpretations.md` §3.G + handoff queue Priority #1
**Skill discipline**: `ave-prereg` (Step 3 pre-reg); upstream skills fired: `pre-test-physics-check`, `substrate-native-check`, `ave-canonical-source`; downstream skills to fire: `ave-driver-script-honesty`, `consistency-vs-emergence`, `verify-before-cite`.

## 1. Derivation target (specific)

Measure the effective Clifford-torus phase-space coordinates $(R_{meas}, r_{meas})$ of the breathing-soliton bound state realized by `run_v14_canonical(R_seed=2.5)` in `src/scripts/verify/q_g47_path_d_full_cross_validation.py`. Route: decompose time-domain $V(x,y,z,t)$ at breathing extrema into $(V_{inc}, V_{ref})$ via radial Riemann-invariant projection $V_{inc} = (V + Z_0 I)/2$, $V_{ref} = (V - Z_0 I)/2$ (with $Z_0 = 1$ in natural units; $I$ from temporal/spatial gradients of $V$); fit Lissajous PCA on the $(V_{inc}, V_{ref})$ trajectory at energy-density peak sample points; report $R_{meas}$ (major axis), $r_{meas}$ (minor axis), $R \cdot r_{meas}$ (product). Compare to canonical Golden Torus targets `R_GOLDEN_TORUS = φ/2 ≈ 0.809`, `R_GOLDEN_TORUS_MINOR = (φ-1)/2 ≈ 0.309`, `RR_GOLDEN_TORUS = 1/4`.

## 2. Physical picture (5 mechanical bullets)

- K4-TLM bond = LC tank carrying counter-propagating $V_{inc}$ + $V_{ref}$; CANONICAL idealized form has the bond hit $\Gamma = -1$ TIR at saturation (hard wall).
- ACTUAL operating point at v14 canonical scope is **sub-saturation** ($A_{op} \approx 0.32$, not at TIR cavity — per `_archive/L3_electron_soliton/130_q_g47_path_d_engine_cross_validation_first_pass.md:55-60`). The breathing bound state is in continuum-EMT regime, NOT in the TIR-cavity regime where Theorem 3.1' bridge derives from.
- Clifford-torus picture (corpus-canonical per `_archive/L3_electron_soliton/68_phase_quadrature_methodology.md:62-71`): bound state's phase-space trajectory in $(V_{inc}, V_{ref})$ plane traces a Lissajous ellipse; major/minor axes in $\ell_{node}=1$ units ARE the Clifford-torus $(R, r)$ coordinates. **The corpus claim is in phase-space ℂ², NOT in Cartesian xyz** — A46 documents this is the load-bearing coordinate-system distinction.
- Golden Torus uniqueness: $R = \varphi/2$, $r = (\varphi-1)/2$ are the radii where Op21 multi-mode identity (per `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:99`) makes the geometric measures equal the mode counts, so $\Lambda_{vol} + \Lambda_{surf} + \Lambda_{line} = 137$ algebraically (Nyquist single-cell-per-natural-unit).
- Discrete observable: $(R_{meas}, r_{meas}, R\cdot r_{meas})$ extracted from PCA-on-Lissajous at breathing fundamental ($T_{breathing} \approx 32.27$ time units per `_archive/L3_electron_soliton/131_q_g47_path_d_full_two_engine_cross_validation_pass.md:50-66`).

## 3. Corpus state (from ave-prereg cross-repo grep)

**State**: PARTIAL — canonical pipeline exists but radial Riemann-invariant projection is NEW work.

**Prior work cited**:

| Class | Citation | Use |
|---|---|---|
| (a) closed | `src/ave/core/constants.py:140-149` (now lines 152-161 with new PHI block) — canonical Λ_i forms at Golden Torus | Reference targets |
| (a) closed | `constants.py:163` (new) — canonical `PHI, R_GOLDEN_TORUS, R_GOLDEN_TORUS_MINOR, RR_GOLDEN_TORUS` (added this prereg) | Import canonically |
| (a) closed | `src/scripts/vol_1_foundations/test_b_bond_scale_phasor.py:128-216` — `analyze_phasor_trajectory()` PCA+Lissajous pipeline | Reuse (don't reinvent) |
| (a) closed | `src/scripts/vol_1_foundations/phasor_discovery.py:17` — $V_{phys} = V_{inc} + V_{ref}, I_{phys} = V_{inc} - V_{ref}$ decomposition | Inverse projection formula |
| (a) closed | `src/scripts/vol_1_foundations/op21_multimode_derivation.py:11-17` — Op21 cell-count↔geometric-measure identity at Nyquist | Re-test harness at measured radii |
| (b) partial | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:63` — $\Lambda_i = Q_i$ bridge | Precondition source; geometry-verification is IMPLICIT in §49-63, not explicit |
| (a) closed | `_archive/L3_electron_soliton/68_phase_quadrature_methodology.md:62-71` — canonical phase-space framing | Corpus-canonical confirmation the (R, r) live in (V_inc, V_ref) phase-space |
| (a) closed | `_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md:1, 19` — PRIOR R_phase/r_phase fit | Read for persistence + chirality-noise caveats before trusting PCA |
| (a) closed | `_archive/L3_electron_soliton/131_q_g47_path_d_full_two_engine_cross_validation_pass.md:50-66` — v14 observables | $V_{peak}=0.2152$, FWHM=15.10, $T_{breathing}=32.27$ |
| (a) closed | `_archive/L3_electron_soliton/130_q_g47_path_d_engine_cross_validation_first_pass.md:55-60` — operating point | $A_{op}=0.32$ sub-saturation REFINEMENT |
| (b) partial | `src/tests/test_electron_tlm_eigenmode.py:39-40, 182-194` (xfail strict=True) | PRIOR geometry-verification harness FALSIFIED at K4-TLM sub-ℓ_node sampling; relevant risk for MasterEquationFDTD too |
| (c) ingredient | `src/ave/core/k4_tlm.py:196-197` — K4-TLM native V_inc/V_ref state | Different engine; NOT directly applicable to MasterEquationFDTD target |

## 4. Prediction (with outcome distribution)

Most-likely outcome distribution (subjective probabilities, $\sum = 1$):

| Outcome | Probability | Description | Interpretation |
|---|---|---|---|
| **A** | ~60% | $(R_{meas}, r_{meas})$ finite, far from Golden Torus (>30% deviation); $R \cdot r \neq 1/4$ | **Interpretation G confirmed**: geometry not realized; closure route requires seed change or added confinement physics (e.g., Cosserat coupling). 50% Λ-gap is dominantly geometric-mismatch. |
| **B** | ~20% | Lissajous fit degenerate (collapsed ellipse: $R \approx r$ or $r \to 0$) | **Sub-saturation regime mismatch**: at $A_{op}=0.32$, the (V_inc, V_ref) phasor structure may not be well-defined because the bond isn't in TIR-cavity regime. Closure route: drive engine into saturation regime first (push $A_{op}$ up to TIR boundary). |
| **C** | ~15% | $(R_{meas}, r_{meas}) \approx (\varphi/2, (\varphi-1)/2)$ within 10% | **Surprising positive**: Theorem 3.1' bridge holds despite sub-saturation operating point; 50% Λ-gap reduces to Interpretation F (UV running) or A/B/C from the §3 enumeration. Foreword line 106 framing tightens. |
| **D** | ~5% | Sub-ℓ_node sampling falsification triggers | MasterEquationFDTD resolution at $N=32, R_{seed}=2.5$ insufficient to resolve $R \approx 0.809 \ell_{node}$ scale; replicates `test_electron_tlm_eigenmode.py` xfail. Closure route: finer grid first, not interpretation verdict. |

**Bayesian weight justification**: A>B>C>D rests on three considerations:
(i) v14 operates sub-saturation per direct prior measurement (130:55-60) — pushes weight toward A or B, not C;
(ii) the Riemann-invariant projection IS valid for arbitrary continuum solutions (it's a coordinate change, not a regime-dependent operation) — pushes weight toward A (finite Lissajous) over B (degenerate);
(iii) the v14 N=32 grid has $R_{seed}=2.5$ which is ~3× larger than $R_{GOLDEN}=0.809$ — sampling-wise the larger seed should resolve the smaller golden radius IF it exists, so D is lower probability than the others.

## 5. Discriminating outcomes

Each outcome maps to a distinct downstream action — no outcome is non-informative:

- **A** → walk back foreword line 106 explicitly to flag Interpretation G; reframe BRANCH STATE weak-spot #2 (2b) per handoff sharpening; next test is Interpretation F (UV running) AFTER geometry forced (e.g., new seed parameters that drive convergence to Golden Torus) — multi-session
- **B** → next test runs the SAME observer at a higher $A_{op}$ seed (e.g., $A_{peak}=0.95$ instead of 0.85) to push into saturation regime, then re-measure (~30 min)
- **C** → foreword line 106 reframes from "50% Λ-gap is geometric" to "50% Λ-gap is UV running"; opens Interpretation F as the next priority test (1-2 hours, per A5 enumeration §149-153)
- **D** → next test runs at $N=64$ or $N=128$ (4-8× finer grid), then re-measures; computational cost ~8-16× higher (~1-2 hours runtime)

## 6. Falsifier (would invalidate framing)

If $(R_{meas}, r_{meas}) \approx (\varphi/2, (\varphi-1)/2)$ within 5% AND Λ-gap remains 50%, the framework's Theorem 3.1' precondition framing is wrong — geometry realization isn't the gap source, and Interpretation G is retired. The next test must search for the actual gap source (Interpretations A/B/C/F from §3).

If the PCA fit returns near-zero variance on BOTH axes (closed-curve at origin), the breathing bound state has no phase-space oscillation at all — the (V_inc, V_ref) decomposition may be a category error for MasterEquationFDTD entirely (i.e., post-hoc continuum→TLM projection is invalid). This would force reframing the whole Interpretation G pathway as inapplicable to this engine.

## 7. Open methodological questions (surface to Grant; making reasonable call per autonomous mode)

### Q1 — Post-hoc Riemann-invariant projection validity (substrate-native checkpoint 1 caveat)

The K4-TLM canonical $(V_{inc}, V_{ref})$ decomposition is NATIVE state of the K4-TLM engine (the lattice update IS scatter+connect on V_inc/V_ref). For MasterEquationFDTD (continuum/EMT, no native characteristic decomposition), computing $V_{inc} = (V + Z_0 I)/2$ from continuum $V$ + gradient-derived $I$ is a **post-hoc continuum-to-TLM mapping** that assumes the EMT solution is a coarse-grained limit of K4-TLM. This is an untested assumption.

**Reasonable call (autonomous mode)**: proceed with MasterEquationFDTD-only this round. If Outcome B (degenerate Lissajous) triggers, next step is K4-TLM cross-validation (where V_inc/V_ref ARE native state). Grant can redirect upfront if K4-TLM cross-validation should be primary.

### Q2 — Sub-ℓ_node sampling falsification risk (substrate-native checkpoint 4 + 7 inheritance)

Prior K4-TLM harness `test_electron_tlm_eigenmode.py` xfail at sub-ℓ_node sampling (electron tube radius $\ell_{node}/(2\pi) \approx 0.16$ cells; finite-grid resolution insufficient for $r = 0.309 \ell_{node}$). MasterEquationFDTD at $N=32, R_{seed}=2.5$ has ~3 lattice units per golden radius — likely OK but not certain. Outcome D captures this risk at ~5%.

**Reasonable call**: report sampling density alongside (R_meas, r_meas) so Outcome D is detectable; if triggered, escalate to $N=64$.

### Q3 — Local clock modulation (substrate-native checkpoint 5)

$A^2_{local} \approx 0.105$ at v14 operating point gives $\omega_{local} \approx 0.97 \omega_{global}$. Small but non-zero. The Lissajous fit assumes constant local-clock advancement during the sampling window; if sample points have differing $A^2_{local}$ (different shell radii), local phase advancement differs.

**Reasonable call**: sample at top-K=8 energy-density peaks (single-shell selection per A46 sampling discipline); report $A^2_{local}$ at sample points; document the local-clock spread in result.

### Q4 — Bond direction for Riemann-invariant projection

The K4-TLM has 4 ports per cell (4 bond directions). MasterEquationFDTD continuum form doesn't have bond direction natively. The radial Riemann-invariant projection picks ONE direction (radial outward from breathing center) as the characteristic axis. This is the natural choice for a spherical/toroidal bound state but is an implementation choice.

**Reasonable call**: use radial direction; report results for one direction in this round. If Outcome A or B, cross-validate by trying axial and tangential directions in followup.

## 8. Implementation plan summary

1. **Constants**: ADD `PHI`, `R_GOLDEN_TORUS`, `R_GOLDEN_TORUS_MINOR`, `RR_GOLDEN_TORUS` to `src/ave/core/constants.py` (DONE per ave-canonical-source skill).
2. **Observer**: add `golden_torus_geometry_check()` to `src/scripts/verify/q_g47_path_d_full_cross_validation.py` after `q_factor_decomposition()` call (line ~149). Three-stage pipeline: (i) Riemann-invariant projection on $V(x,y,z,t)$ at top-K energy-density peaks; (ii) reuse `analyze_phasor_trajectory()` pattern from `test_b_bond_scale_phasor.py:128-216` for PCA+Lissajous; (iii) compute deviation from canonical targets + classification by outcome A/B/C/D.
3. **Verification**: in-script canonical-source assertion block (no `verify_constants.py` exists in AVE-Core; bake assertions into observer startup per ave-canonical-source skill Step 4).
4. **Honesty audit**: fire `ave-driver-script-honesty` four-discriminator check on implementation.
5. **Run**: execute `run_v14_canonical(N=32, n_steps=5000, A_peak=0.85, R=2.5)` with new observer; capture $(R_{meas}, r_{meas}, R \cdot r_{meas})$ at top-K peak sample points + $A^2_{local}$.
6. **Classification**: fire `consistency-vs-emergence` to confirm this is a consistency check (verifies bound state realizes assumed coordinates that Theorem 3.1' presupposes); NOT an emergence test.
7. **Result doc**: log to `research/2026-05-18_q-g47-interpretation-g-result.md` per ave-prereg skill Step 5.
8. **Commit**: with audit trail citing all upstream + downstream skill applications.

## 9. Banked sharpenings (per handoff "Next-session sharpenings")

After this test lands, three banked items propagate:
- **foreword line 106**: flag Interpretation G outcome (one of A/B/C/D)
- **BRANCH STATE weak-spots #2 (2b)**: resolution path sharpens per outcome
- **Theorem 3.1' canonical leaf §49-63**: make geometry-verification precondition EXPLICIT (verify-before-cite skill confirms it's currently implicit; this leaf revision is a separate workstream from this test)

## 10. ADDENDUM (Grant intervention, 2026-05-18 night) — Chirality-induced multi-mode mechanism

**Grant plumber-physical question** surfaced after ave-driver-script-honesty audit but before measurement: *"the springs are asymmetrically applying torque to the nodes aren't they?"*

**Substantive implication**: The K4 lattice (Axiom 1) is **chiral Laves** — the 4 bonds at each node arrange with handedness, applying asymmetric torque to the node. This chiral coupling is the **mechanism** that turns pure radial breathing into multi-mode (2,3) torus knot structure:
- 2 = orbital winding (radial breathing mode)
- 3 = chiral precession (spin winding induced by asymmetric torque)
- Frequencies in ratio 2:3 (the Golden Torus / Clifford-torus signature)

**Engine limitation**: `MasterEquationFDTD` is a scalar EMT/continuum solver on a Cartesian grid — it has NO chiral structure, NO Cosserat torque coupling, NO K4 connectivity. The chirality-induced coupling mechanism is **absent from this engine**. Therefore:

- Outcome C (Golden Torus realized) from THIS engine collapses from ~15% to **essentially 0**. Positive C result from `MasterEquationFDTD` would be a measurement artifact, not physical realization.
- The realistic outcome space reduces to **A / B / D**, with **B (degenerate Lissajous from single-mode breathing) overwhelmingly likely**.
- Refined outcome distribution (post-Grant intervention): A ~30%, B ~60%, C ~0%, D ~5%, with ~5% reserved for unexpected.

**Test framing tightens**: this is NOT "does v14 realize Golden Torus geometry?" (that requires chirality the engine lacks). It IS:
- "Does v14 bound state exhibit single-mode breathing or multi-mode structure?" (answered by FFT discriminator)
- "How far is the projected (V_inc, V_ref) Lissajous from the Golden Torus targets?" (answered by Lissajous PCA)

**Closure pathway revises**: positive Interpretation G verification (Outcome C) requires running the same observer on **K4-TLM native engine** where chiral asymmetry IS in the substrate AND V_inc/V_ref ARE native scatter-connect state. Queued as follow-up workstream after this baseline measurement on `MasterEquationFDTD` lands.

**Result doc must document this explicitly**: the negative-by-engine-limitation outcome (B almost certainly) is INFORMATIVE — it bounds what `MasterEquationFDTD` can verify about geometry-precondition-bearing claims. The K4-TLM cross-validation becomes the load-bearing test, not this one.
