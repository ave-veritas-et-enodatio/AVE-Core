# Phase 3f: Electron Torus-Knot First-Attempt Result — FAIL Informative

**Date**: 2026-05-18
**Test**: [src/tests/test_fdtd3d_electron_torus_knot_seed.py](../src/tests/test_fdtd3d_electron_torus_knot_seed.py)
**Engine**: FDTD3DEngine (full-vector Maxwell with nonlinear ε(V), μ(H) per Axiom 4)
**Status**: FAIL on bound-state formation; INFORMATIVE about what's missing
**Pre-reg**: [2026-05-18_fundamental-topology-verification-program.md](2026-05-18_fundamental-topology-verification-program.md) Tier 1 #1

## TL;DR

First-attempt (2,3) torus knot seed on FDTD3DEngine produces a DISPERSING configuration that loses amplitude FASTER than a random-direction baseline. The simplified seed construction (E-only, knot-tangent-aligned, H=0 initial) is INSUFFICIENT for topology-driven binding.

Per pre-reg outcome: **FAIL — knot retention < random baseline**. But informative: identifies the simplified-seed-construction as the gap.

## Result

| Run | Seed peak |E| (initial) | Final peak |E| (after 500 timesteps) | Retention | Max strain ratio |
|---|---|---|---|---|
| (2,3) torus knot | 1.7 MV/m | 0.36 MV/m | **20.9%** | 0.22 |
| Random direction | 2.8 MV/m | 1.56 MV/m | **56.3%** | 0.56 |

**Knot retention is 2.7× WORSE than random**.

## Diagnosis

Multiple factors contribute to the FAIL:

### Factor 1: Simplified E-only seed; H=0 initial

The seed initializes ONLY E components tracing knot tangent direction; H field is zero. The Maxwell evolution then has to GENERATE H from curl(E) at each timestep, but the initial condition is not self-consistent.

For a proper Beltrami bound state, would need:
- E(r,0) tracing knot tangent
- H(r,0) self-consistent with E via Beltrami condition: B ∥ A (force-free), |E| = c|B|
- Phase relationship between E and H matching standing-wave eigenmode

The Beltrami-pair construction requires solving $\nabla \times \mathbf{B} = \lambda \mathbf{B}$ on the toroidal shell with proper boundary conditions. Standard EM literature (Marsh 1996, Yoshida 2018) provides recipes; not implemented in this first-attempt.

### Factor 2: Random baseline produces HIGHER per-component amplitudes than knot

Confound in test design:
- (2,3) knot: E_x = envelope × t_hat_x where |t_hat_x| ∈ [0, 1] (typically 0.3-0.7)
- Random baseline: E_x = envelope × random_unit (can be up to 1.0)

Random baseline produces larger SINGLE-COMPONENT amplitudes → engages saturation more (0.56 vs 0.22). The "better retention" of random is partially due to nonlinear saturation effects, NOT topology.

Better baseline construction would use matched-distribution comparison: same component-amplitude statistics as knot but topologically trivial.

### Factor 3: Amplitude too low for Γ=-1 boundary mechanism

Test used amplitude 0.5 × V_yield/dx (peak |E| ≈ 2 MV/m). The canonical Γ=-1 reflection at saturation requires amplitude approaching V_snap (11.7× higher than V_yield). At only 0.5 × V_yield/dx, the saturation kernel partially engages (max_strain 0.22) but the topological-mirror reflection mechanism doesn't activate.

Higher amplitude (0.85 × V_yield/dx) caused engine NaN blowup in earlier attempt. Needs:
- A_cap tuning
- Smaller dt
- OR a more stable seed configuration that doesn't trigger numerical instability

### Factor 4: Lattice resolution may be too coarse

N=48, dx=0.01 m, R=8 cells, r=3 cells. The toroidal shell is thin (3 cells thick) which may be undersampled relative to the (2,3) winding structure. For 3 windings around the minor radius (q=3), need at least 6-12 cells around minor circumference; with r=3, that's ~18-37 cells around — barely sufficient.

### Factor 5: Missing additional substrate physics

The topology-only-binding hypothesis assumes topology + Maxwell + Born-Infeld is sufficient. The FAIL suggests possibly missing:
- Cosserat coupling (microrotation DOF beyond just curl-coupled B)
- K=2G algebraic operating point coupling (mass-binding mechanism)
- Phase-space (V_inc, V_ref) phasor encoding (the (2,3) trefoil is in PHASE space per canonical spec, not real space)

The last point is potentially the critical issue: the canonical electron has the unknot in REAL space and (2,3) trefoil in PHASE space (V_inc, V_ref phasor trajectory). My seed put the (2,3) tangent in REAL space — possibly the wrong topology placement.

## Per pre-reg classification

Per pre-reg outcomes:
- ❌ Outcome A (PASS — knot rings at Compton frequency for 500+ steps): NOT achieved
- ❌ Outcome B (PARTIAL — some localization but disperses): NOT achieved (knot disperses FASTER than random)
- 🔴 Outcome C (NULL — identical to photon): NOT achieved (knot is WORSE than random)
- 🔴 Outcome D (FAIL): **THIS OUTCOME** — knot retention 21% << random 56%

Classification: **FAIL with multiple identified gap factors**.

## What this validates and what it doesn't

**What's still validated (unchanged)**:
- FDTD3DEngine runs cleanly with vector torus-knot seeds (smoke test PASS)
- Saturation kernel engages correctly (max_strain in [0, 1.0] range)
- No numerical blowup at 0.5 × V_yield/dx amplitude
- Phase 1-3d results (F·c scaling, ρ(E²,B²) = -0.99, wake propagation, E=pc) ALL stand

**What's NEWLY identified as needed for electron bound state**:
1. **Proper Beltrami (E, H) pair construction** — biggest gap; standard EM literature has solutions
2. **Phase-space topology encoding** — (2,3) trefoil should be in (V_inc, V_ref) phasor trajectory, not real-space tangent direction
3. **Higher amplitude with stability tuning** — to engage Γ=-1 reflection mechanism
4. **Possibly Cosserat or K=2G coupling** — substrate physics beyond plain Maxwell + Born-Infeld
5. **Higher lattice resolution** — to properly resolve the (2,3) winding structure

## Iteration plan: Phase 3f.2

Next attempt should:

1. **Implement Beltrami pair**: solve $\nabla \times \mathbf{B} = \lambda \mathbf{B}$ on toroidal shell for λ matching (p, q) winding. Construct E from B via $\mathbf{E} = c \cdot \hat{\mathbf{k}} \times \mathbf{B}$ or similar self-consistency.

2. **Implement phase-space (V_inc, V_ref) encoding**: at each toroidal-shell point, set INITIAL phasor trajectory to (2,3) winding. This means setting E and H with specific phase relationship that, when evolved, traces (2,3) trajectory in (V_inc, V_ref) phasor plane.

3. **Match baseline distribution**: use Hopf link (1,1) as comparison instead of random — same overall amplitude distribution and topology placement, but different (p,q) → predicts different binding behavior.

4. **Higher lattice resolution**: N=64 or 96; R=16, r=6 (cells); higher resolution per knot crossing.

5. **Lower amplitude initially**: 0.3 × V_yield/dx to avoid instability; if Beltrami construction is correct, the bound state should form even at moderate amplitude.

## Cross-references

- Pre-reg + scope: [2026-05-18_fundamental-topology-verification-program.md](2026-05-18_fundamental-topology-verification-program.md)
- Phase 3e photon precedent: [2026-05-18_phase3e-self-trapping-result.md](2026-05-18_phase3e-self-trapping-result.md)
- v14 Mode I (scalar engine precedent): [breathing-soliton-v14-mode-i.md](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/breathing-soliton-v14-mode-i.md)
- K4-TLM (2,3) ansatz reference: `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:33`
- Electron unknot canonical: [electron-unknot.md](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md)
- Engine: [src/ave/core/fdtd_3d.py](../src/ave/core/fdtd_3d.py)
- Test: [src/tests/test_fdtd3d_electron_torus_knot_seed.py](../src/tests/test_fdtd3d_electron_torus_knot_seed.py)

## Discipline lesson

First-attempt failed but informatively. The discipline of:
1. Pre-registration of outcomes
2. Comparison test (knot vs random)
3. Explicit gap diagnosis

…produces a clean diagnostic of WHAT'S MISSING for the next iteration. Without the comparison test, the result would be ambiguous; with it, we know the knot seed performs WORSE than random — a strong signal that the simplified seed construction is wrong.

**Generalized lesson**: bound-state verification on vector engines requires PROPER FIELD-CONFIGURATION CONSTRUCTION (Beltrami pairs, phase-space topology, etc.), not just direction-aligned amplitude. The seed-construction is the load-bearing step.

## Status

- ✅ First-attempt test built + run cleanly (no engine crash)
- ❌ Bound state NOT formed
- ✅ Gap factors identified
- ⏳ Phase 3f.2 (Beltrami pair construction) staged for next session
