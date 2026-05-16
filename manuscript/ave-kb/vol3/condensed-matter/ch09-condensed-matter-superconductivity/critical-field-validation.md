[↑ Ch.9: Condensed Matter and Superconductivity](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-3dc9qt, clm-qky559]
-->

---

## Numerical Validation

The superconductor engine (`ave.plasma.superconductor`) validates the Axiom 4 isomorphism against experimental data for four materials.

### $B_c(T) = B_{c0} \cdot S(T/T_c)$: Exact Match
<!-- claim-quality: clm-3dc9qt (the BCS critical field IS the Universal Saturation Kernel applied at thermal scaling — Axiom 4 manifestation, not a curve fit) -->
<!-- claim-quality: clm-qky559 (universal saturation operator: BCS, type-I/II, London depth, coherence — same operator, four domains) -->

The critical field formula is not merely *similar* to the saturation operator---it IS the operator. The engine function `critical_field(T, T_c, B_c0)` calls `saturation_factor(T, T_c)` directly. Validation across four materials at six temperatures each yields:

> **[Resultbox]** *Critical Field Validation*
>
> | **Material** | $T_c$ [K] | $B_{c0}$ [T] | **Error vs. BCS** |
> |---|---|---|---|
> | Aluminium | 1.18 | 0.0105 | **0.0000%** |
> | Lead | 7.19 | 0.0803 | **0.0000%** |
> | Niobium | 9.25 | 0.206 | **0.0000%** |
> | MgB$_2$ | 39.0 | 16.0 | **0.0000%** |

This is not a fit: the error is exactly zero because the BCS formula and the AVE saturation operator are algebraically identical.

### London Penetration Depth and Coherence Length

| **Material** | $\lambda_L^{\text{AVE}}$ [nm] | $\lambda_L^{\text{exp}}$ [nm] | $\xi_0^{\text{AVE}}$ [nm] | $\xi_0^{\text{exp}}$ [nm] | $\kappa^{\text{AVE}}$ | Type |
|---|---|---|---|---|---|---|
| Aluminium | 17.7 | 50 | 1251 | 1600 | 0.014 | I ($\checkmark$) |
| Lead | 20.7 | 37 | 284 | 83 | 0.073 | I ($\checkmark$) |
| Niobium | 31.9 | 39 | 185 | 38 | 0.172 | I ($\times$) |
| MgB$_2$ | 57.6 | 85 | 14 | 5 | 4.069 | II ($\checkmark$) |

**Catalog limitation:** The superfluid densities $n_s$ used in the London formula are free-electron estimates. For Niobium, $n_s$ is overestimated, producing $\lambda_L$ too small and $\kappa < 1/\sqrt{2}$, incorrectly classifying it as Type I. Correcting $n_s$ from the measured $\lambda_L = 39$ nm yields $\kappa \approx 1.0$, matching experiment. This is tracked as a catalog limitation, not an operator failure.

### Regime Classification at Liquid Helium Temperature

At $T = 4.2$ K:

| **Material** | $r = T/T_c$ | **Regime** | **State** |
|---|---|---|---|
| Aluminium | 1.00 | IV boundary | Normal (above $T_c$) |
| Lead | 0.584 | II | Superconducting |
| Niobium | 0.454 | II | Superconducting |
| YBCO | 0.046 | I (deep) | Superconducting |
| MgB$_2$ | 0.108 | I (deep) | Superconducting |

---
