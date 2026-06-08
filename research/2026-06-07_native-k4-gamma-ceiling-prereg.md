# Prereg: native K4 Γ ceiling (can the engine reach ε → α?)

**Status:** FROZEN PREREG.
**Parent:** `2026-06-07_theorem-31-alpha-identity-audit.md` §3 C1.
**Driver:** `src/scripts/vol_1_foundations/native_k4_gamma_ceiling.py`.

---

## §0 Question

On **native `VacuumEngine3D`** (coupled K4 + Cosserat, asymmetric Meissner), does bond `Γ_min` reach **−0.99+** at any seeded amplitude so that `ε = 1−Γ²` can approach **α ≈ 0.0073**?

This tests the **first-principles challenge C1** — not the projection bridge.

## §1 Predictions

**Primary:** Γ_min **saturates below −0.9** (polarity/ceiling/z_local seam) — same order as scalar projection `Γ ≈ −0.63`.

**Alternative:** Γ_min **reaches −0.99+** at high `V_SNAP` amplitude → native lane can in principle read α via H1 leak identity.

## §2 Protocol

- `VacuumEngine3D`, `N=32`, `use_asymmetric_saturation=True`, `disable_cosserat_lc_force=True` (A28).
- Seed sech `V_inc` blob at center (+ optional Cosserat unknot for `S_μ` engagement).
- Amplitudes (V_SNAP): `[0.2, 0.48, 0.85, 1.0, 1.5, 2.0, 3.0]`.
- Measure `Γ_min` from `z_local_field` post-transient; `ε`, compare to α (comparison-only).

## §3 Outcomes

| Outcome | Criterion |
|---------|-----------|
| A | `Γ_min ≤ −0.99` at some amplitude → ceiling not blocking α readout |
| B | `Γ_min` plateaus `> −0.9` → **C1 confirmed**; engine/config blocks Theorem 3.1' dynamic test |
| C | `Γ_min` lower than scalar projection → z_local/coupling path differs |

---

## §4 Result

```bash
PYTHONPATH=src python src/scripts/vol_1_foundations/native_k4_gamma_ceiling.py
```

Output: `src/scripts/vol_1_foundations/_output/native_k4_gamma_ceiling_results.json`

## §5 Adjudication

**Verdict: `GAMMA_CEILING_NOT_BLOCKING` (Outcome A)**

Native `VacuumEngine3D` (asymmetric Meissner, A28) **does** reach full TIR on the bond-Γ readout. The scalar projection lane plateau at `Γ ≈ −0.63` is **lane-specific**, not a universal engine ceiling.

| V_SNAP amp | A² (V_inc peak) | Γ_min | ε = 1−Γ² | \|ε−α\| |
|------------|-----------------|-------|----------|---------|
| 0.48 | 0.23 | −0.013 | 0.9998 | 0.993 |
| 0.85 | 0.72 | −0.084 | 0.993 | 0.986 |
| 1.0 | 1.00 | **−0.992** | **0.0161** | **0.0088** |
| 2.0 | 5.52 | −0.994 | 0.0126 | 0.0053 |
| 3.0 | 25.0 | −0.994 | 0.0126 | 0.0053 |

**C1 revision:** falsified on native lane; still holds on MasterEquationFDTD+PhasorBridge lane.

**Calibration crux reframed:** rest-energy sizing (`A² ≈ 0.23`, matched `Γ ≈ 0`) vs rupture wall (`A² ≥ 1`, `Γ ≤ −0.99`). Closest ε→α at wall: `|ε−α| ≈ 0.0053` (~1.7× α), not exact α. Exact H1 target needs `Γ² = 1−α` → `Γ ≈ −0.9964`; observed `Γ ≈ −0.994`.

**Next:** why projection lane stalls at −0.63 while native `z_local` reaches −0.99; whether ε=1−Γ² is the correct dynamic proxy for `1/Q = α` at TIR.
