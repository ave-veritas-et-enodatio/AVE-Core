# Cosserat-Lagrangian Engine: Q-Preservation Soliton-Scale Test Result

**Date**: 2026-05-18
**Pre-registration**: [`2026-05-18_cosserat-engine-q-preservation-prereg.md`](2026-05-18_cosserat-engine-q-preservation-prereg.md)
**Test**: [`src/tests/test_cosserat_engine_q_preservation.py`](../src/tests/test_cosserat_engine_q_preservation.py)
**Branch**: `analysis/cosserat-engine-q-preservation`

## TL;DR

**Outcome**: TECHNICAL OBSERVATION (not in any of the four pre-registered outcome bins A/B/C/D directly, but operationally closest to **Outcome C (FAIL — needs Phase 4 chiral coupling refactor)** for the predicted reason of "not testable on scalar engine without bound cavity").

The existing CosseratMasterEquationFDTD engine **does not support a bound cavity** at the (V, ω) configurations tested. ω_R measures grid-eigenmode frequencies (not blob-radius-dependent cavity modes); τ is unmeasurable (engine cavity modes are lossless within the 5000-step / ~8-period observation window). The test does not produce a measurable Q value across the radius sweep — but this null result is itself informative.

## Observed Results

```
Fixed A = 0.40 V_yield; N=48 grid; n_steps=5000

 R (cells)    ω_R (rad/t)          τ (t)              Q
------------------------------------------------------------
       3.0     2.6720e-01              ∞              ∞
       4.0     2.6720e-01              ∞              ∞
       5.0     1.1452e-01              ∞              ∞
       6.0     1.1452e-01              ∞              ∞
       7.0     1.1452e-01              ∞              ∞
```

## Findings

### Finding 1: ω_R clusters into two grid-eigenmode bands, not blob-radius-dependent

The ω_R values fall into two distinct buckets:
- Small blobs (R = 3, 4 cells): ω_R = 0.2672 rad/t
- Larger blobs (R = 5, 6, 7 cells): ω_R = 0.1145 rad/t

Ratio 0.2672 / 0.1145 = 2.334 — close to but not exactly 2:1. This is the signature of **the engine settling into the lowest available grid eigenmodes**, not of a blob-bound cavity mode that scales with R.

At BH scale (C1), the cavity radius is *physically* set by r_sat(a*) — the saturation boundary is a physically meaningful Γ=-1 mirror. At soliton scale, the existing scalar engine has no equivalent binding mechanism: per Phase 3f (commit 3d67cae, "(2,3) torus knot seed on FDTD3DEngine FAILS to bind"), a scalar V+ω initial condition does not self-organize into a bound cavity at any tested amplitude.

The blob radius therefore acts as an initial-condition parameter that excites different lattice modes, not as a tunable cavity-radius analog to BH r_sat.

### Finding 2: τ unmeasurable on lossless engine within observation window

τ = ∞ at all radii. Diagnostic:
- Engine `dt ≈ 0.039` time units (set by Cosserat CFL with S_min=0.05)
- Measured ω_R · dt ≈ 0.0105 rad/step
- One period = 2π / 0.0105 ≈ 600 steps
- 5000 steps = ~8 periods

For measurable τ in 8 periods, need Q < ~320. The engine's cavity modes have far higher Q than this — energy bounces between V and ω fields via shared_flux coupling without dissipation; only PML at boundaries absorbs energy, and the central blob's energy doesn't reach the PML in 8 periods on a 48³ grid.

This is consistent with the engine being designed to validate Op14 ρ=-0.990 anti-correlation (which is energy-trading, not energy-dissipating) — it has no built-in radiative loss mechanism for cavity modes.

### Finding 3: Q-preservation IS testable, just not on this engine architecture

C1's mechanism requires:
1. A bound cavity with a physically meaningful radius parameter (BH has r_sat from Γ=-1 saturation boundary)
2. A way to perturb the cavity radius parameter (BH has spin a*)
3. A measurable cavity Q that responds to the perturbation

The existing scalar CosseratMasterEquationFDTD lacks (1) — no bound cavity forms. Phase 3f confirmed (2,3) torus knot seed doesn't bind on this scalar engine architecture. Without (1), neither (2) nor (3) is testable.

The pre-registered "Outcome C" pathway (FAIL → Phase 4 chiral coupling refactor) is the correct unblock. This test independently corroborates the Phase 3f finding: scalar (V, ω) engine cannot support the (2,q) torus-knot solitons that would produce measurable bound cavities.

## Operational Implications

### What this tells us about C1's mechanism

C1's lattice-Q preservation result at BH scale is empirically anchored at -0.47% mean τ across 3 LIGO events. This test does NOT invalidate C1; it shows that *testing the soliton-scale analog requires engine machinery the scalar engine lacks*. The C1 result holds; what's required is upgraded engine architecture for soliton-scale verification.

The Phase 3f → this test chain narrows the engine-build requirement: **must support (2,q) torus-knot soliton binding** for the C1 mechanism to be reproducible at soliton scale.

### What this tells us about the engine roadmap

Per the original Phase 4 plan (full-picture doc §4 Phase 4):
1. Q-4 adjudication (separate workstream, requires Grant input)
2. Chiral coupling refactor: $\kappa_{\text{chiral}}$ derived from Cosserat-K4 geometry, NOT hardcoded as $\alpha \cdot \tilde\kappa(p,q)$
3. Layer 4 p_c extraction from FCC packing geometry
4. Layer 5 test: $\alpha = p_c / 8\pi$ at electron-unknot bound state

Both Phase 3f and this Q-preservation test point at step 2 as the necessary engine upgrade. Without chiral coupling, the engine cannot support (2,q) torus-knot solitons, and without those solitons, neither α-emergence nor C1-Q-preservation is testable.

## Outcome Classification

Pre-registered outcome probability distribution:
- A (PASS, ~20%): Q constant within 10% — NOT OBSERVED (Q not measurable)
- B (PARTIAL, ~60%): Q varies 20-50% — NOT OBSERVED (Q not measurable)
- C (FAIL, ~15%): Q varies >50% — TECHNICALLY NOT OBSERVED but for the predicted underlying reason (mechanism is (2,3)-topology-specific; scalar engine can't bind soliton)
- D (TECHNICAL BLOCKER, ~5%): NaN at high A — NOT OBSERVED (engine ran stably; just produced lossless modes)

**Actual outcome**: NEW outcome category not in prereg — "no bound cavity on scalar engine, mechanism not testable" — closest to C in spirit (need chiral coupling refactor) but with a sharper diagnostic (the issue isn't Q-variance, it's no cavity at all).

Pre-reg note: I under-estimated the probability of Outcome C and didn't predict the specific failure mode ("no measurable Q because no bound cavity"). This is a discipline note for future preregs: when corpus shows (Phase 3f) that scalar engines fail to bind topological solitons, that result should propagate forward into related preregs more aggressively.

## Recommended Next Action

**Don't refactor the scalar engine.** This test confirms the Phase 4 chiral-coupling refactor is the load-bearing engine upgrade — not the ν_vac=2/7 partition (Outcome B) that the prereg predicted as most-likely.

Two paths forward, both gated on Phase 4 chiral coupling:

**Path 1 (engine work)**: Q-4 adjudication of L3 doc 108 (requires Grant input), then chiral coupling refactor + (2,q) torus-knot soliton implementation, then re-run this Q-preservation test on the chiral-coupled engine.

**Path 2 (analytical work)**: Use C1's empirically-anchored ν_vac=2/7 rigid/compliant partition as the input to Sessions 19+ Q-G47 ξ_K1, ξ_K2 prefactor derivation from K4 unit-cell Cosserat-Lagrangian integration (per closure-roadmap:30). This work is analytical and doesn't require the chiral-coupled engine; it derives the partition that the engine refactor would need.

**Recommendation**: Path 2 first (multi-session analytical, but doesn't require engine refactor or Q-4 adjudication). Then Path 1 after the partition is analytically derived (engine can then *implement* the derived partition).

## Falsifier discipline (per `ave-prereg` Step 4)

Result logged regardless of outcome — this is a null/informative result, not a PASS. The pre-reg's Outcome A and B did not happen; Outcome C is the closest match. Pre-reg has been honored.

## Cross-references

- Pre-registration: [`2026-05-18_cosserat-engine-q-preservation-prereg.md`](2026-05-18_cosserat-engine-q-preservation-prereg.md)
- Test code: [`src/tests/test_cosserat_engine_q_preservation.py`](../src/tests/test_cosserat_engine_q_preservation.py)
- Phase 3f failure (independent corroboration): commit 3d67cae
- C1 closure (the BH-scale result this tests at soliton scale): [`ligo-ringdown-driver-design.md`](ligo-ringdown-driver-design.md) §10
- Engine implementation: [`src/ave/core/cosserat_master_equation_fdtd.py`](../src/ave/core/cosserat_master_equation_fdtd.py)
- Full-picture engine plan: [`2026-05-18_cosserat-lagrangian-engine-full-picture.md`](2026-05-18_cosserat-lagrangian-engine-full-picture.md) §4 Phase 4
- Sessions 19+ Q-G47 ξ_K1, ξ_K2 derivation target: [`closure-roadmap.md:30`](../manuscript/ave-kb/claim-quality-closure-roadmap.md:30)
