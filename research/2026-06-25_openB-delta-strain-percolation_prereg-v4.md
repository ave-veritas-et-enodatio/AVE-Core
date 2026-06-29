# PRE-REG v4 — Open B: forward δ_strain from EMT percolation / node participation

**Date frozen:** 2026-06-25 · **Driver:** `src/scripts/verify/alpha_variational_strain_projection.py`

**Substrate chain (NOT K/G crossing search):**
```
Golden Torus → α⁻¹_cold = 4π³+π²+π
p_cold = 8π/α⁻¹_cold  →  z₀ ≈ 51.25  (EMT invert, NOT z=52)
δ_strain forward from node-participation / rigidity-percolation sensitivity
α⁻¹_obs = α⁻¹_cold × (1 − δ_strain_pred)
```

**α-hiding:** no `constants.py`, no CODATA α/δ on verdict path. Comparison post-solve only.

**Adversarial mandate:** each assumption gets an explicit CHALLENGE block in driver output.

## Forward routes (frozen)

| Route | Model | Verdict if |
|---|---|---|
| **B0** | Identity: δ_strain ≡ δp/p (since α=p/(8π)) | sets scale target only — NOT a derivation |
| **B1** | Born-Huang EMT: δα⁻¹/α⁻¹ = −(d ln p)/... from δu/u driver | needs independent δu — absent → FAIL |
| **B2** | Percolation exponent: G∝(p−p_G)^β, δG/G → δp via margin | β=1 mean-field; test amplification |
| **B3** | Participation: δ_strain = ½ δp/p at p_cold (η_ε analog) | tautology unless δp from substrate |
| **B4** | FTG-EMT d(K/G)/dp × bond-strain δu | same δu problem as B1 |

**Closed-negative control:** FT-1 thermal BE (η_ε ~ 10⁻³⁸) — must NOT be reused as δu driver.

## Outcome map

| Outcome | Condition |
|---|---|
| **CHORD** | forward δ_strain_pred within 2.225e-6 without CODATA on path |
| **PARTIAL** | correct OOM (within 10×) with substrate-native δu driver |
| **CLOSED-NEGATIVE** | all routes miss by >10 OOM OR tautological OR no independent δu |
| **TAUTOLOGY-FLAG** | B0/B3 match by definition, not derivation |

## Pre-registered adversarial challenges

1. **ppm coincidence:** δ_strain and δp/p match at 2.2 ppm — correlation or identity?
2. **p=8πα circularity:** is p_cold prediction or rearrangement of α_cold?
3. **Cold sum echo:** R·r=¼ not substrate-selected (Class B value echo)
4. **No δu driver:** cosmic T_CMB gives δu ~ 10⁻³⁸ via BE (FT-1) — percolation needs different driver
5. **Generic vs AVE-distinct:** EMT sensitivity is framework-neutral (any spring network)
6. **z=52 negative control:** still 1.38% off — documents wrong census convention
