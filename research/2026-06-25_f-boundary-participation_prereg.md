# Open D — forward f_b boundary participation for δ_strain magnitude

**Date:** 2026-06-25  
**Status:** FROZEN prereg  
**Parent:** `research/2026-06-25_delta-strain-session-synthesis.md` §8

## Question

Can a **geometry-only** boundary participation fraction `f_b` combine with forward coupling `η_ε = f_b · 8π α_cold³` to predict `δ_strain ≈ 2.2×10⁻⁶` **without** importing CODATA `δ_strain` or `α_obs` on the forward path?

## Physical model

Environmental asymmetric load (E hot / B frozen) couples only through **exterior-facing boundary DOFs** of the electron's Γ=-1 Nyquist-scale flux tube. Interior + frozen B DOFs do not participate.

```
η_ε     = f_b · 8π α_cold³        (coupling kernel — α_cold only)
δ_pred  = η_ε / 2                 (leading asymmetric ε shift → α⁻¹)
```

Compare `δ_pred` to `DELTA_STRAIN` **post-solve only**.

## Forward f_b candidates (geometry / DOF counting only)

| ID | Definition | Substrate rationale |
|---|---|---|
| G1 | `3/6` | E-mode fraction of Cosserat DOFs (δ-strain leaf) |
| G2 | `(3/6)×(1/2)` | E modes × exterior-facing half of boundary |
| G3 | `1/2` | Shared-bond / two-cell boundary ownership |
| G4 | `R·r = 1/4` | Golden Torus Nyquist identification |
| G5 | `4/π²` | Tube cross-section / Nyquist face area ratio scale |
| G6 | `1/(2φ)` | Golden ratio from torus minor radius |
| G7 | `φ−1 = 1/φ` | Inverse golden ratio |
| G8 | `(3/6)×(1−1/(2π))` | E fraction × tube-circumference correction |
| G9 | `(ℓ_node/r_sec)²` capped at 1 | Secondary-link sphere, `r_sec=1.187 ℓ_node` |
| G10 | `2/z₀` | Bond-pair vs amorphous coord, `z₀=51.25` |
| G11 | `1/2` screened variance | Two-node complete projector (comparison only — phase space) |

## Controls

| ID | Purpose |
|---|---|
| I0 | `f_req = δ_target/(4πα_cold³)` — **tautology** |
| I1 | `f_b = α_cold` — uses α inside f_b (circular) |
| I2 | `η = BE` FT-1 — negative control |

## Verdict gates

- **CHORD:** any G* within **10%** of target without I0 identity
- **PARTIAL:** within **50%** (OOM bracket)
- **CLOSED-NEGATIVE:** all forward G* miss by >50% or only I0 hits

## Discipline

`ave-driver-script-honesty`, `substrate-native-check`, `consistency-vs-emergence`
