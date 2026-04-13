# Atomic Ionization Energy Solver — Dedicated Tracker

> **Branch:** `feature/hybrid-ie-solver`
> **Status:** Active development — SIR mode-weighted correction implemented
> **Last Updated:** 2026-04-07

## Architecture Summary

The solver has TWO complementary formalisms:

| Formalism | Code | Valid for | Base energy |
|-----------|------|-----------|-------------|
| **ABCD cascade** | `radial_eigenvalue.py` | s-block (l=0): Li, Be, Na | Non-hydrogenic (graded CDF potential) |
| **MCL cavity** | `coupled_resonator.py` | p-block (l≥1): B–Ne, Al–Ar | Z_eff² Ry / n² (Gauss screening exact) |

**Critical findings:**
1. **(2026-04-06):** The s-orbital eigenvalue is intrinsically non-hydrogenic. No formula Z_eff²Ry/n² captures it. The ABCD cascade through the graded CDF is the ONLY axiom-compliant architecture for s-block.
2. **(2026-04-07):** The atom is a **Stepped Impedance Resonator (SIR)**. The ODE eigenvalue includes phase from ALL impedance sections, but MCL loading only operates in the valence bulk. The SIR mode-weighted correction `_sir_mode_weighted_base()` separates these.

## Current Results

### ABCD cascade + SIR MCL (ionization_energy_e2k) — Period 2

| Z | Element | Calc (eV) | Exp (eV) | Error | Notes |
|---|---------|-----------|----------|-------|-------|
| 1 | H | 13.606 | 13.598 | +0.06% | Exact hydrogenic |
| 2 | **He** | **24.370** | 24.587 | **−0.88%** | ✅ Coupled resonator mode splitting |
| 3 | **Li** | **5.786** | 5.391 | **+7.3%** | ⚠️ s-block, SIR not applied |
| 4 | **Be** | **8.664** | 9.322 | **−7.1%** | ⚠️ Coupled resonator |
| 5 | B | **8.053** | 8.298 | **−3.0%** | ✅ **SIR (was +1.8%)** |
| 6 | C | **11.384** | 11.260 | **+1.1%** | ✅ **SIR (was +5.8%)** |
| 7 | N | **14.435** | 14.534 | **−0.7%** | ✅ **SIR (was +3.6%)** |
| 8 | O | **13.599** | 13.618 | **−0.1%** | ✅ **SIR (was +3.9%)** |
| 9 | F | **17.182** | 17.422 | **−1.4%** | ✅ **SIR (was +2.3%)** |
| 10 | Ne | **21.789** | 21.564 | **+1.0%** | ✅ **SIR (was +4.5%)** |
| 11 | **Na** | **5.885** | 5.139 | **+14.5%** | ⚠️ s-block, SIR not applied |
| 12 | **Mg** | **7.913** | 7.646 | **+3.5%** | ⚠️ Coupled resonator + n=2 CDF |

**Period 2 mean |error|: 1.2%** (was 3.3%, 2.7× improvement)

### Period 3 — SIR Overcorrection ❌

| Z | Element | Calc (eV) | Exp (eV) | Error | Diagnosis |
|---|---------|-----------|----------|-------|-----------|
| 13 | Al | **3.579** | 5.986 | **−40.2%** | SIR too aggressive: n=2 CDF broad |
| 14 | Si | **5.060** | 8.151 | **−37.9%** | Same |

**Root cause:** For period 3 atoms (shells = [(1,2), (2,8)]), the n=2 inner
shell CDF is much broader than the 1s CDF. The 3p mode's probability
density overlaps the n=2 transition zone, dragging Z_eff_mode far below
Z_eff_gauss. The SIR correction overcorrects.

### MCL cavity (ionization_energy_cavity) — p-block only (unchanged)

| Z | Element | Calc (eV) | Exp (eV) | Error | Notes |
|---|---------|-----------|----------|-------|-------|
| 5 | B | 8.052 | 8.298 | −2.96% | ✅ Best p-block solver |
| 6 | C | 11.384 | 11.260 | +1.10% | ✅ |
| 7 | N | 14.435 | 14.534 | −0.68% | ✅ |
| 8 | O | 13.599 | 13.618 | −0.14% | ✅ |
| 9 | F | 17.182 | 17.422 | −1.38% | ✅ |
| 10 | Ne | 21.789 | 21.564 | +1.04% | ✅ |

## Changes Made (2026-04-07)

### New: SIR Mode-Weighted Correction

Added `_sir_mode_weighted_base()` to `radial_eigenvalue.py`. This function:
1. Extracts ψ(r) at the Phase A eigenvalue
2. Normalizes by charge conservation (Axiom 2)
3. Computes Z_eff_mode = ⟨Z_net(r)⟩_ψ (mode-weighted effective charge)
4. Returns Z_eff_mode² Ry / n² as the MCL base energy

Axiom chain: Axiom 1 (mode profile) → Axiom 2 (Gauss normalize) → Axiom 3 (least reflected action → mode amplitude determines loading).

Phase B (MCL) and Phase C (pairing) now use E_mcl_base instead of E_base
for the p-block path. The s-block path (coupled resonator) still uses E_base.

### Terminology: E_eigen_J Rename

Renamed `Z_resonance_J` → `E_eigen_J` (24 occurrences) to avoid confusion
with impedance Z and charge Z. The variable is the soliton eigenvalue energy.

## Eliminated Hypotheses (2026-04-07)

| # | Hypothesis | Test | Result |
|---|-----------|------|--------|
| 1 | Cross-shell stub loading | Analytical derivation | ~0.3%, too small |
| 2 | CDF Z_shell self-screening (Z→Z−0.5) | Direction test | Wrong direction |
| 3 | Nonlinear vacuum effects (Axiom 4) | Regime I strain | Negligible (A ≈ α) |
| 4 | ODE r_min in Regime II zone | r_min sensitivity | Δ < 0.002 eV for l≥1 |
| 5 | ΔE_penetration additive correction | Direct test | +15–36%, way too much |
| 6 | Phase B (MCL) formula wrong | Proportionality proof | IE/E_base identical to 4 d.p. |

## Key Discovery: Hopf Half-Screening Identity

∫₀^∞ F(r) ρ(r) dr = 1/2

For any CDF F with PDF ρ. Two identical Hopf-linked solitons on the same
mode screen exactly half each other's charge on average. Topological invariant.

## Axiom Compliance Audit (2026-04-06, updated 2026-04-07)

### Resolved ✅

1. **Centrifugal term l(l+1)/r²**: Angular Helmholtz eigenvalue. Native to Axiom 1.
2. **p:0.5 weight**: Crossing factor (1+cos90°)/2. Axiom 1 torus geometry.
3. **n_s_eff=1.5 for He/Be → REPLACED** by coupled resonator mode splitting.
4. **Pairing penalty (4α, 6α)**: Crossing scattering, NOT orbital expansion.
5. **SIR correction**: Phase B operates on mode-weighted Z_eff, not ODE eigenvalue.

### Flagged ⚠️

6. **s:1.0 weight**: Null hypothesis — no explicit derivation.
7. **d:0.0, f:0.0 weights**: Phenomenological, no axiom chain.
8. **Period 3 SIR overcorrection**: Need outermost-shell-only formulation.
9. **s-block error (Li +7.3%, Na +14.5%)**: Unsolved, separate from SIR.

### Resolved engineering work ✅

10. **Multi-shell CDF cascade**: Implemented (2026-04-07). Na: −46% → +14.5%.

## Next Steps

1. **Near-term:** Fix period 3 SIR overcorrection (outermost-shell-only option)
2. **Near-term:** Diagnose s-block error separately from SIR
3. **Long-term:** Unified ABCD+MCL (full vector control approach)
4. **Long-term:** KB formalism reconciliation (3 incompatible formalisms)
