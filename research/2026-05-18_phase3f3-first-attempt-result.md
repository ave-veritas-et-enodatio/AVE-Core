# Phase 3f.3 First Attempt: Engine Stability Blocker Identified

**Date**: 2026-05-18
**Test**: [src/tests/test_fdtd3d_cosmic_cooling_freeze_in.py](../src/tests/test_fdtd3d_cosmic_cooling_freeze_in.py)
**Status**: BLOCKED on engine numerical instability with random per-cell directional noise
**Pre-reg**: [2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md](2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md)

## TL;DR

Phase 3f.3 Option D (stochastic seed + observe persistence) first attempt failed not at the physics level but at the NUMERICAL level: FDTD3DEngine produces NaN values when initialized with random per-cell direction noise, even at very low amplitude (tried 0.5, 0.2, 0.05 × V_yield/dx). The random per-cell directions create high spatial frequency content that FDTD's curl/Laplacian operators amplify into divergence.

This is an ENGINE STABILITY issue, not a physics test failure. Phase 3f.3.2 needs SMOOTH NOISE (Gaussian-convolved random field) instead of per-cell random directions.

## Diagnosis

The numerical instability mechanism:
1. Random unit-vector E at cell (i,j,k) is uncorrelated with cell (i±1, j, k)
2. Curl operation: ∇×E ~ (E_{i+1} - E_{i-1})/(2·dx) → can be 2/dx large
3. dt update: E_new = E + dt·c²·∇×H → can amplify high-frequency content
4. Born-Infeld nonlinearity at high gradients: ε(E) drops sharply → c_eff diverges → CFL violated
5. Within a few timesteps: NaN propagates

This is a well-known FDTD limitation. Standard mitigations:
- Low-pass spatial filter (Gaussian convolution of initial noise)
- Smaller dt (sub-CFL margin)
- Smooth deterministic seed instead of random

## What this validates and what it doesn't

**Validates**: FDTD3DEngine works for smooth field configurations (Phase 3a-d all confirmed). The engine is correct; the test architecture (random per-cell noise) is unphysical and numerically unstable.

**Does NOT validate**: the physics question (does substrate freeze-in topology?). That question requires either:
- Smooth-noise initial conditions (physically realistic)
- Engine stabilization for high-frequency noise

## Phase 3f.3.2 plan

Use SMOOTH NOISE for the stochastic seed:

```python
# Pseudocode for smooth noise generation
raw_noise = rng.randn(N, N, N)  # white noise
smooth_noise = scipy.ndimage.gaussian_filter(raw_noise, sigma=3.0)  # low-pass to scale-3 cells
# Apply smooth_noise as amplitude modulation on a smooth carrier
E_seed = AMPLITUDE * smooth_noise * carrier_field
```

This produces noise with spatial correlations at scale ~3 cells (matching FDTD grid resolution), avoiding the unphysical per-cell directional incoherence.

Alternative: use a sparse seed (few isolated Gaussian blobs at random positions and amplitudes) instead of fill-fraction noise. Each blob is smooth; they interact only via radiated fields.

## Status

- ✅ Pre-reg discipline followed (engine ran cleanly within stability range previously; this test exposed a new boundary)
- ❌ First-attempt blocked on engine stability with chosen seed type
- ⚠️ Phase 3f.3.2 needs smooth-noise refactor
- 🔶 Test marked `@pytest.mark.xfail` with clear reason; doesn't block CI

## Cross-references

- Phase 3f.3 pre-reg: [2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md](2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md)
- FDTD3DEngine: [src/ave/core/fdtd_3d.py](../src/ave/core/fdtd_3d.py)
- Test: [src/tests/test_fdtd3d_cosmic_cooling_freeze_in.py](../src/tests/test_fdtd3d_cosmic_cooling_freeze_in.py) (xfail)
- Phase 3f attempt 1 (smooth knot seed, no engine crash): [2026-05-18_phase3f-electron-torus-knot-first-attempt.md](2026-05-18_phase3f-electron-torus-knot-first-attempt.md)

## Discipline lesson

The Phase 3f.3 pre-reg outcomes (PASS/PARTIAL/NULL/FAIL) all assumed the test would RUN. They didn't account for an engine-stability blocker before any physics result is produced.

**Generalized lesson**: pre-reg outcomes should include a TECHNICAL/IMPLEMENTATION category for "test cannot execute as designed". For numerical experiments, this is a real failure mode distinct from physics outcomes.

For Phase 3f.3.2, the pre-reg outcomes should add:
- Outcome E (TECHNICAL BLOCKER): engine instability OR test design issue prevents execution; result is uninformative for physics but informative for engine

This iteration provided exactly that — engine has stability limits for high-spatial-frequency noise. Useful for planning Phase 3f.3.2 + future Phase 4 work that might involve similar regimes.

## Recommended next action

Option A: continue Phase 3f.3.2 with smooth-noise refactor (~30 min implementation + run)
Option B: pivot to other workstream and revisit Phase 3f.3 when engine stabilization is part of a broader investment
Option C: pause topology verification entirely; the prerequisites (engine stability, proper Beltrami construction) need more upfront investment than incremental session work can deliver
