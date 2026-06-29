# Open D — f_b boundary participation result

**Date:** 2026-06-25  
**Prereg:** `research/2026-06-25_f-boundary-participation_prereg.md`  
**Driver:** `src/scripts/verify/f_boundary_participation.py`  
**JSON:** `src/scripts/verify/f_boundary_participation_results.json`

## Verdict: **PARTIAL / OOM-BRACKET CLUSTER** (not CHORD)

Forward geometry routes **bracket** δ_strain ≈ 2.22×10⁻⁶ to within **~8–10%** but **do not close** without the tautological inversion f_b ≈ 0.455.

---

## Forward chain

```
η_ε     = f_b · 8π α_cold³
δ_pred  = η_ε / 2
```

Target (post-solve only): `DELTA_STRAIN = 2.223×10⁻⁶`

---

## Results table

| Route | f_b | δ_pred | vs target | Verdict |
|---|---:|---:|---:|---|
| **G8** E×(1−1/2π) | 0.420 | 2.053×10⁻⁶ | **0.92×** | best forward |
| **G1/G3/G12** E-half / shared bond / ½ direct | 0.500 | 2.442×10⁻⁶ | **1.10×** | near-hit cluster |
| G5 4/π² | 0.405 | 1.979×10⁻⁶ | 0.89× | partial |
| G2 exterior E (¼) | 0.250 | 1.221×10⁻⁶ | 0.55× | undershoot |
| G4 R·r | 0.250 | 1.221×10⁻⁶ | 0.55× | undershoot |
| G10 2/z₀ | 0.039 | 1.9×10⁻⁷ | 0.09× | closed-negative |
| **I0** inversion | 0.455 | 2.223×10⁻⁶ | 1.00× | **tautology** |
| I2 BE control | — | ~10⁻³⁷ | −31 dex | closed-negative |

---

## Adjudication

### What worked

1. **Half-participation cluster (f_b = ½):** Three independent substrate rationales (E-mode fraction, shared K4 bond, direct boundary-channel count) **converge** on f_b = ½ → δ_pred ≈ **2.44×10⁻⁶** (**+9.8%**). This is the same OOM bracket Open C L4 gave with f_b = 1 (2.2× high); geometry supplies the missing **~½** factor cleanly.

2. **G8 composite** (E fraction × tube circumference correction) lands at **−7.7%** — best single forward route, still not exact.

3. **Required f_b for exact match** = **0.455** (I0). Sits between G8 (0.420) and G1 (0.500) — a **narrow band**, not a discrete geometric identity.

### What failed

1. **No unique selector:** R·r = ¼ and exterior-E = ¼ both undershoot by ~45%; ½ overshoots by ~10%. Substrate does not **pick one** without importing δ.

2. **Tube cross-section** (unknot audit): `(ℓ_node/(2π))² / ℓ_node² = 1/(4π) ≈ 0.08` — wrong sector for ppm (would need surface not area).

3. **Two-node quadrature** (G11): f_b = ½ numerically but **wrong physics sector** — phase-space screened variance is 68×α, not boundary participation.

4. **Secondary link** (G9): overshoots 1.56× — wrong geometry for env-load aperture.

### Circularity audit

- f_b candidates use **no** CODATA α or δ_strain.
- Coupling kernel **8πα_cold³** is the Open C L4 bracket (α_cold only — acceptable per prereg).
- I0 hits exactly — confirms the **algebraic closure** is f_b ≈ 0.455, not derivable from listed geometry alone.

---

## Interpretation (Grant diode framing)

| Quantity | Role |
|---|---|
| α_cold | Datasheet ideal (cold Golden Torus LC Q) |
| f_b ≈ ½ | **~Half** of boundary channels participate in ambient E-load (hardware) |
| δ_strain ≈ 2 ppm | Residual calibration — **between** ½ bracket (+10%) and inverted 0.455 |

**Honest read:** Geometry **is consistent with δ_strain being O(α³) GIVEN an assumed α² boundary-coupling kernel (an underived ansatz)** and supplies **why the factor is ~½ not ~1**, but the last **~10%** (or f_b = 0.455 vs 0.500) is still **unclosed**. Promote as **bracket + calibrated input**, not independent chord.

> **Audit note (2026-06-25 propagation).** The "O(α³)" reading is NOT a forward
> derivation of the exponent: the `8π α_cold³` kernel is `8π α_cold · α_cold²`,
> where the `α_cold²` boundary-coupling factor is an **assumed ansatz** (Open C L4),
> not substrate-derived. Geometry supplies the leading `~½` participation factor on
> top of that ansatz; it does not explain why the boundary coupling scales as `α²`.
> The honest claim is consistency-given-ansatz, not derivation.

---

## Relation to Open C L4

Open C L4: η = 8πα³ → δ = 2.44×10⁻⁶ (2.2× target, f_b implicitly 1).

Open D: f_b ≈ ½ → δ = 2.44×10⁻⁶ at G1/G12 — **same number**, now with substrate label. The 2.2× discrepancy in L4 **is** the missing half-participation factor.

---

## Follow-up (only if pursued)

1. Engine-native bond-pair phasor extraction (two-node test §7 — K4-TLM time series, not Lissajous shadow).
2. Non-equilibrium rim injection (§8 item 3) as second-order correction inside the 8–10% band.
3. **Do not** promote f_b = 0.455 without a forward derivation — it is I0 tautology.
