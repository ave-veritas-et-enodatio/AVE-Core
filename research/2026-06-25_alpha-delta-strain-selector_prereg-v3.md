# PRE-REG v3 — α via cold ideal + δ_strain (NOT K/G crossing)

**Date frozen:** 2026-06-25 · **Supersedes v1/v2 functional targets**
**Driver:** `src/scripts/verify/alpha_variational_strain_projection.py`

**Grant correction (2026-06-25):** The operating point for α's **value** is not the K/G=2 crossing at `z₀=52`. It is:

```
α⁻¹_obs  =  α⁻¹_cold × (1 − δ_strain)
α⁻¹_cold =  4π³ + π² + π          (Golden Torus, T→0)
δ_strain ≈  2.225×10⁻⁶            (vacuum strain at T_CMB — the selector to CODATA)
p_c      =  8π α                    (packing readout; cold and obs differ at δ_strain scale)
```

The **1.38% gap** at `z₀=52` K/G=2 crossing is a **wrong convention** (z=52 vs true z≈51.25 from `p_c = 8πα_cold`). It is **not** δ_strain (which is ~2 ppm).

---

## Frozen routes (v3)

### D1 — Cold ideal (geometry only, α-free)

`α⁻¹_cold = 4π³ + π² + π` from Golden Torus multipole (R·r=1/4, d=1). No `constants.py`.

### D2 — Packing + z₀ at cold ideal

`p_cold = 8π/α⁻¹_cold`. Invert FTG-EMT `p*(z₀)=p_cold` → `z₀ ≈ 51.25`. Verify `K/G(p_cold, z₀) = 2`.

### D3 — δ_strain bridge (forward attempt)

Predict `δ_strain` from substrate packing sensitivity at `p_cold` (Open B: EMT-percolation / node-participation dilution). Compare to CODATA-residual target **post-solve only**.

### D4 — Observed α readout

`α⁻¹_pred = α⁻¹_cold × (1 − δ_strain_pred)`. CHORD if within tolerance.

**Legacy B2/A1 (K/G crossing at z=52):** retained as **negative control** — shows 1.38% failure mode when wrong target is used.

---

## Outcome map

| Outcome | Condition |
|---|---|
| **CHORD** | D4 within δ_strain tolerance |
| **PARTIAL** | D1 cold within ~3 ppm of CODATA (confirms δ_strain is the only gap) |
| **ECHO** | D3 requires CODATA δ_strain input on verdict path |
| **NEGATIVE-CONTROL** | z=52 crossing 1.38% off — documents wrong-target failure |

## Expected stance

D1 lands ~2.2 ppm above CODATA (needs δ_strain). D3 forward δ_strain is **Open B** — expect ECHO unless percolation route works.
