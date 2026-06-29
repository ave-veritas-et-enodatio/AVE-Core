# Result — Open B: forward δ_strain from EMT percolation (adversarial)

**Canonical session state:** [`2026-06-25_delta-strain-session-synthesis.md`](2026-06-25_delta-strain-session-synthesis.md)

**Date:** 2026-06-25 · **Status:** CLOSED-NEGATIVE
**Prereg:** [`2026-06-25_openB-delta-strain-percolation_prereg-v4.md`](2026-06-25_openB-delta-strain-percolation_prereg-v4.md)
**Driver:** [`src/scripts/verify/alpha_variational_strain_projection.py`](../src/scripts/verify/alpha_variational_strain_projection.py)
**JSON:** [`alpha_variational_strain_projection_results.json`](../src/scripts/verify/alpha_variational_strain_projection_results.json)

---

## Verdict: **CLOSED-NEGATIVE** (percolation does not forward-derive δ_strain magnitude)

Forward routes B1–B2 miss target `δ_strain ≈ 2.22×10⁻⁶` by **~4–5 orders of magnitude** even with rigidity-margin geometry (56.7% above `p_G`). No independent `δu` / participation driver exists in corpus beyond closed-negative FT-1 thermal chain.

---

## What survived adversarial audit

| Finding | Survives? |
|---|---|
| Cold ideal 2.22 ppm above CODATA — gap **is** δ_strain scale | YES |
| `1 − p_cold/p_obs ≈ δ_strain` (packing readout identity) | YES — **tautology**, not derivation |
| `z₀ ≈ 51.25` from `p_cold`, K/G = 2 at operating packing | YES |
| `u ≈ 0.187`, `r_secondary ≈ 1.187 ℓ_node` at `p_cold` | YES numerically |
| z=52 K/G crossing (+1.38%) | **CONFIRMED wrong target** |
| Percolation sensitivity → δ_strain magnitude | **FAIL** |
| EMT route AVE-distinct | **FAIL** (generic network physics) |
| Cold Golden Torus value substrate-selected | **FAIL** (value echo on R·r=¼) |
| `p = 8πα` as double prediction | **FAIL** (consistency identity) |

---

## Forward route results

| Route | δ_strain_pred | vs target |
|---|---|---|
| B0 identity (`1 − p_cold/p_obs`) | 2.223×10⁻⁶ | exact — **tautology** |
| B1 dilution × thermal δu | 5.6×10⁻¹¹ | **−4.6 dex** |
| B2 percolation β=1 × f_part | 1.2×10⁻¹⁰ | **−4.3 dex** |
| B3 half-participation invert | requires 4.4×10⁻⁶ Δp/p | **tautology** |
| B4 d(K/G)/du | no α bridge | inconclusive |

FT-1 reference: thermal BE η_ε ~ 10⁻³⁸ (**−31 dex** vs target) — still the hardest negative control.

---

## Adversarial lessons (assumptions challenged)

1. **ppm coincidence ≠ causation.** Matching δ_strain to packing shift proves α **is** the packing readout (`p/(8π)`), not that percolation **derived** the ppm.

2. **Percolation without δu driver is empty.** Sensitivity `d ln α⁻¹ / d ln u ≈ 0.47` is real, but multiplying by thermal `δu/u ~ 10⁻¹⁰` gives ~10⁻¹⁰ — not 10⁻⁶. Open B needs a **non-thermal** participation fluctuation the corpus does not supply.

3. **Don't relabel FT-1 as percolation.** Node-participation dilution is a different *story* from BE occupation; without a new driver it repeats the same OOM failure dressed in EMT language.

4. **K/G sensitivity ≠ α selector.** B4 shows d(K/G)/du ≠ 0 at `p_cold` — the operating point is not an K/G extremum. Trace-reversal is a **form lock**, not a variational crossing.

5. **Honest chain stands:** α value = cold LC Q (form chord, value echo) + δ_strain (magnitude **definitional** until a substrate forward driver closes).

---

## Discipline checklist

- [x] substrate-native: Born-Huang + FTG EMT, Golden Torus cold, shared-B-node geometry
- [x] adversarial audit explicit (8 challenges)
- [x] FT-1 negative control cited
- [x] no CODATA on forward path
- [x] ave-evidence-framing: CLOSED-NEGATIVE, not softened
