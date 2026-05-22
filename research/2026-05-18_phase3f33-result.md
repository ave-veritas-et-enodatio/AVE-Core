# Phase 3f.3.3 Result: TECHNICAL BLOCKER on Engine CFL Stability

**Date**: 2026-05-18
**Test**: [src/tests/test_fdtd3d_negative_pressure_freeze_in.py](../src/tests/test_fdtd3d_negative_pressure_freeze_in.py)
**Status**: TECHNICAL BLOCKER per pre-reg Outcome E
**Pre-reg**: [2026-05-18_phase3f33-negative-pressure-stretch-freeze-in-prereg.md](2026-05-18_phase3f33-negative-pressure-stretch-freeze-in-prereg.md)

## TL;DR

Phase 3f.3.3 stretch-driven freeze-in test blocked at NUMERICAL level: FDTD3DEngine produces NaN when V_yield is decreased mid-run with full-lattice smooth-noise initial conditions in the full Born-Infeld nonlinear regime. Tested at amplitudes 0.05 and 0.3 × V_yield/dx; all NaN.

This is the THIRD numerical-stability blocker in the topology verification program:
- Phase 3f.3.1: random per-cell noise → high spatial frequencies destabilize
- Phase 3f.3.3 (this): full-lattice smooth noise + varying V_yield → CFL violation when V_yield drops

Pattern confirmed: **FDTD3DEngine has stability limits for test architectures involving (a) full-lattice noise or (b) time-varying V_yield in nonlinear regime**. Each works individually (Phase 3a-d, 3e, 3f all PASS with smooth deterministic seeds at constant V_yield), but the combinations needed for freeze-in tests don't.

## Diagnosis

The numerical instability mechanism with time-varying V_yield:
1. Engine.dt is computed at __init__ based on V_yield_0 (the initial value)
2. As V_yield(t) drops, the substrate's effective saturation engagement increases
3. c_eff² = c_0²/S(V) where S(V) = √(1 - (E·dx/V_yield)²)
4. As V_yield drops, more cells have (E·dx/V_yield)² closer to 1 → S → 0 → c_eff² diverges
5. The CFL stability condition dt ≤ dx/(c_eff · √3) is violated
6. Updates produce out-of-bounds values → NaN propagates

This is a fundamental CFL issue. The engine's dt would need to be RESCHEDULED as V_yield drops, OR a different test architecture used.

## Pattern across 3 freeze-in attempts

| Phase | Mechanism | Architecture | Result | Why blocked |
|---|---|---|---|---|
| 3f.1 | (2,3) knot seed | Equilibrium substrate | FAIL (physics) | Seed too simple; needs Beltrami pair |
| 3f.3.1 | Stochastic noise | Constant V_yield | TECHNICAL | Random per-cell directions = high spatial freq |
| 3f.3.3 | Stretch-driven | Smooth noise + varying V_yield | TECHNICAL | V_yield drop → CFL violation |

The engine excellently handles:
- Single deterministic Gaussian seed in nonlinear regime (Phase 3e photon)
- Knot-tangent vector seed in nonlinear regime (Phase 3f, partial)
- Plane-wave packet with proper Beltrami pairing (Phase 3d E=pc)
- Cavity ringing in linear regime (Phase 3b ρ=-0.99)

The engine does NOT cleanly handle:
- Lattice-wide stochastic noise (any seed)
- Time-varying V_yield in nonlinear regime
- High-spatial-frequency content with Born-Infeld saturation

## What this tells us about the framework

**The substrate-physics predictions stand** — none of Phase 1-3d results are challenged. F·c scaling, E=pc, ρ(E²,B²)=-0.99, wake formation, photon-like dispersion, EE-photonics translation: ALL validated.

**The bound-state and freeze-in tests are gated on engine refinement**. Three iterations have not produced bound-state formation in vector Maxwell + Born-Infeld FDTD. This could mean:
- The engine needs CFL-aware dt rescheduling
- The engine needs different boundary conditions for high-frequency content (CPML instead of Mur ABC)
- The bound-state tests need fundamentally different test architecture
- The substrate physics is incomplete on Maxwell + Born-Infeld alone (needs Cosserat coupling)

## Proposed engine refinements for future Phase 3f.3.x or Phase 4

1. **CFL-aware adaptive dt**: when V_yield changes, recompute dt to maintain stability
2. **CPML boundaries**: use convolutional PML instead of Mur ABCs to absorb high-frequency content cleanly
3. **Sub-cell smoothing**: apply low-pass filter periodically during evolution to suppress numerical noise accumulation
4. **Sparse-seed test architectures**: avoid full-lattice noise; use single or few isolated localized seeds

These are not trivial engine modifications. Cumulative effort: ~3-5 sessions of engine work BEFORE next freeze-in test attempt is feasible.

## What's still pending

**Open Phase 3 sub-questions** (gated on engine refinement):
- Does substrate freeze in topologies under stretch? (Phase 3f.3.x)
- Does electron-like bound state form from proper Beltrami seed? (Phase 3f.2)
- Pair production threshold at V_snap? (Phase 3g)
- Photon-electron Compton scattering? (Phase 3h)

**Cosmological observable predictions** (independent of engine):
- Cosmic-F·c statistical survey: testable with published Lyα data; no engine required
- Dark energy = residual substrate tension: testable with cosmological data
- Particle mass from cosmic stretch history: testable analytically

## Recommended pivot

Given that 3 of 3 freeze-in test attempts have hit engine-stability blockers, the most productive next move is NOT to keep iterating on this test. Better options:

**Option A: Engine refinement workstream** (~3-5 sessions)
- Add CFL-aware adaptive dt
- Add CPML boundaries
- Add sub-cell smoothing
- Then return to Phase 3f.3.x with stable engine

**Option B: Cosmic-F·c statistical survey** (testable without engine)
- Use published cosmic-web Lyα observations
- Test AVE F·c prediction vs ΛCDM at statistical scale
- No paywall issues, no engine needed

**Option C: AVE-Umbrella .ip-graph.yaml setup** (admin)
- Lock in REPO-ARCH bidirectional pointer architecture
- Makes IP-divide machine-checkable
- 1 session of admin work

**Option D: Phase 4 per-private-repo upstream pointers** (admin)
- Complete the bidirectional architecture
- 1 session per repo

**Default recommendation**: Option B (cosmic-F·c statistical survey). High-leverage substrate-physics validation that doesn't depend on engine refinement.

## Discipline lesson reinforced

Three iterations of freeze-in test (3f.3.1, 3f.3.3, plus the related Phase 3f.1 attempt) hit different blockers:
- 3f.1: physics-level seed insufficiency
- 3f.3.1: high-frequency noise instability  
- 3f.3.3: time-varying V_yield CFL violation

The pre-reg discipline's TECHNICAL/IMPLEMENTATION outcome category (added at Phase 3f.3 result doc) is doing its job — exposing engine boundaries that were not visible from physics-side reasoning. Without it, these iterations would each look like physics failures rather than engine boundaries.

**Generalized lesson**: when 2+ test iterations in the same workstream hit different engine-stability blockers, the pattern indicates the engine architecture has fundamental limits for that test type. Engine refinement (or test architecture redesign) is the load-bearing next step, not more test iterations.

## Status

- ✅ Phase 3f.3.3 implementation complete
- ❌ Test BLOCKED on engine CFL stability with varying V_yield
- ✅ Test marked @pytest.mark.xfail with clear technical reason
- ✅ Engine refinement scope documented for future work
- ✅ Phase 3 substrate-physics validations (Phase 3a-d, 3e, 3f) unchanged
- ⏳ Phase 3 bound-state validation gated on engine refinement
- ⏳ Pivot decision pending: Options A/B/C/D above

## Cross-references

- Phase 3f.3 prereg (cooling framing): [2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md](2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md)
- Phase 3f.3 first attempt result (random noise blocker): [2026-05-18_phase3f3-first-attempt-result.md](2026-05-18_phase3f3-first-attempt-result.md)
- Phase 3f.3.3 prereg (stretch-driven): [2026-05-18_phase3f33-negative-pressure-stretch-freeze-in-prereg.md](2026-05-18_phase3f33-negative-pressure-stretch-freeze-in-prereg.md)
- Phase 3f first attempt (knot seed FAIL): [2026-05-18_phase3f-electron-torus-knot-first-attempt.md](2026-05-18_phase3f-electron-torus-knot-first-attempt.md)
- Topology verification program: [2026-05-18_fundamental-topology-verification-program.md](2026-05-18_fundamental-topology-verification-program.md)
- Engine: [src/ave/core/fdtd_3d.py](../src/ave/core/fdtd_3d.py)
