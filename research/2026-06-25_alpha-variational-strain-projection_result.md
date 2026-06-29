# Result — Open A v2: lattice-native strain-projection route to α's value

**Date:** 2026-06-25 · **Status:** COMPLETE (FORK-for-Grant + PARTIAL)
**Prereg v2:** [`2026-06-25_alpha-lattice-strain-projection_prereg-v2.md`](2026-06-25_alpha-lattice-strain-projection_prereg-v2.md)
**Prereg v1:** [`2026-06-25_alpha-variational-strain-projection_prereg.md`](2026-06-25_alpha-variational-strain-projection_prereg.md)
**Driver:** [`src/scripts/verify/alpha_variational_strain_projection.py`](../src/scripts/verify/alpha_variational_strain_projection.py)
**JSON artifact:** [`src/scripts/verify/alpha_variational_strain_projection_results.json`](../src/scripts/verify/alpha_variational_strain_projection_results.json)

> **Driver reconstruction note (2026-06-25 consolidation).** The original driver
> was lost from every tree/stash before preservation. The committed driver is a
> faithful reconstruction from this prereg/result chain; it **reproduces the
> Open-A table below to the reported precision** (B2 1/α=138.92 +1.38%, B1
> 1/α=129.96 K/G=1.83, DIAG 1/α=137.04, B4≡B2). The driver's signed `pct_err`
> reports B1 as −5.17% (pred below CODATA); the table's "+5.17%" is the same
> magnitude. CODATA `ALPHA`/`P_C` enter only as the post-solve DIAGNOSTIC; z₀=52
> and p_cauchy=0.3068 are the prereg-frozen α-free verdict-path inputs.

---

## Verdict: **FORK-for-Grant** + **PARTIAL** (unchanged classification; physics clarified)

| Route | Physical meaning | `u` | `p` | `K/G` | `s_grav` | `1/α_pred` | vs CODATA |
|---|---|---:|---:|---:|---:|---:|---:|
| **B2** K/G=2 constraint | trace-reversal gravity lock | 0.1925 | 0.1809 | 2.00 | 0.00897 | 138.92 | **+1.38%** |
| **B1** max `s_grav×adm` | unconstrained strain projection | 0.1663 | 0.1934 | 1.83 | 0.00867 | 129.96 | +5.17% |
| **B4** weighted `s_grav` | v1 A2 in lattice units | 0.1925 | 0.1809 | 2.00 | 0.00897 | 138.92 | +1.38% |
| **DIAG** CODATA packing | comparison only | 0.1871 | 0.1834 | 1.96 | 0.00893 | 137.04 | — |

**Key v2 finding:** B1 **≠** B2 (`|Δu| ≈ 0.026`). The **admissibility-weighted max** of local strain-projection amplitude (`s_grav × admissibility`) **lands at** a **denser** packing (`p ≈ 0.19`, `K/G ≈ 1.83`) — **not** the trace-reversal lock. Gravity-stable projection is a **constraint** (K/G=2), not the unconstrained optimum of `Π·γ`. (NOTE: the prereg-v2 expectation that B1 would land at the floppy/Cauchy edge toward `p_G` **did not occur**; the weighted max lands denser, not floppier.)

B4 still relabels B2 (variational with K/G proximity ≡ constraint crossing).

---

## Lattice-native chain (what the driver now tracks)

At dilution `u`, with `T_EM` normalized to 1:

1. **Packing:** `p(u) = p_cauchy/(1+u)³` — α readout `p/(8π)` only after solve
2. **Moduli:** FTG-EMT `K/G(p)` at `z₀=52` → `ν(p)`, shear modulus ratio
3. **Axial drive:** `ε_11 = 1/(E/G)` from unit 1D EM tension on primary bond
4. **Secondary shear:** `γ = (u/(1+u))·ε_11` — over-bracing engages secondary links
5. **Bulk projection:** `Π = (1−2ν)/3 = 1/(3K/G+1)` — equals **1/7 only at K/G=2**
6. **Local gravity channel:** `s_grav = Π·γ` — projected bulk strain amplitude before Machian ξ

**G (Newton)** = `c⁴/(7ξT_EM)` is **not** on the verdict path — ξ requires `α⁻²` in the horizon porosity integral (circular for α derivation).

---

## Load-bearing findings

### 1. K/G=2 is a constraint, not an unconstrained extremum

The **admissibility-weighted max** `s_grav×admissibility` (B1) **lands at** `K/G ≈ 1.83`, `p ≈ 0.19` — 5% off CODATA. The trace-reversal point has **higher raw** `s_grav` (0.00897 vs 0.00867) but sits at a different `(u,p)` because Π and γ trade off differently vs `K/G`.

**Physical read:** α is not "the packing that maximizes local strain projection." It is the packing where **bulk–shear lock** (`K=2G`) makes 1/7 isotropic projection valid for stable macroscopic gravity.

### 2. CODATA packing is near but not at K/G=2

Diagnostic: CODATA `p_c = 8πα` gives `K/G ≈ 1.96`, `u_codata ≈ 0.187` vs B2 crossing `u* ≈ 0.193`. The 1.38% α gap correlates with this ~3% offset in dilution geometry.

### 3. Variational relabel persists (B4 ≡ B2)

Adding K/G=2 proximity weight to `s_grav` (B4) recovers the same crossing as B2/A2. No new selection principle beyond the trace-reversal constraint.

### 4. Goldilocks without K/G still fails (A3)

Mid-band `(p−p_G)(p_cauchy−p)` → `K/G ≈ 1.66`, 13% off — confirms gravity-stable projection requires trace-reversal, not band midpoint.

---

## α-hiding audit

Unchanged from v1 — clean on verdict path. Circularity is structural: K/G=2 form is GR-imported; z₀=52 is path-count convention.

---

## Open-route status

| Open | Status |
|---|---|
| **A (variational / lattice-native)** | **CLOSED NEGATIVE** — B1 distinct from B2 but unphysical for gravity; B2/B4 relabel; PARTIAL 1.38% |
| **B (EMT-percolation δ_strain)** | **CLOSED-NEGATIVE** — see Open B result |
| **C (OCXO loaded-Q)** | **CONSISTENCY-REFRAME** — see synthesis §4 |

---

## Discipline checklist

- [x] ave-prereg v2 frozen before run
- [x] substrate-native-check: explicit T_EM→ε_11→γ→Π→s_grav chain
- [x] consistency-vs-emergence: Class D attempt → PARTIAL / FORK-for-Grant
- [x] ave-driver-script-honesty: forward solve; CODATA diagnostic separated
- [x] ave-evidence-framing-discipline: percentages from tool output
