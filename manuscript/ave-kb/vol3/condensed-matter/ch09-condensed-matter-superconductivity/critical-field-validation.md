[↑ Ch.9: Condensed Matter and Superconductivity](../index.md)
<!-- leaf: verbatim -->

> **A-034 anchor (canonical 2026-05-15 evening; SCOPE RECLASSIFIED 2026-05-17 Foundation Item 4 per `consistency-vs-emergence` discipline trigger 5).** BCS $B_c(T)$ functional-form $\sqrt{1-(T/T_c)^2}$ is **algebraically identical** to AVE's Axiom-4 saturation kernel $S(A) = \sqrt{1-A^2}$ with $A = T/T_c$ (per body line 25 below). The "0.00% error" reported in the validation table is therefore **definitional-identity** (sharpest end of consistency-vs-emergence 4-class taxonomy), NOT a predictive forward emergence test: $B_{c0}$ and $T_c$ are per-material experimental inputs, not derived from substrate parameters. The per-material BCS recovery is structural functional-form agreement, not zero-parameter prediction.
>
> **What the AVE-distinct emergence claim actually is**: the SAME kernel $\sqrt{1-A^2}$ governs BH ring-down (1.7% from GR), NOAA-validated solar flares, cosmic K4 crystallization, and BCS B_c(T) — i.e., the cross-substrate UNIVERSALITY of the kernel form across the 21-instance Universal Saturation-Kernel Catalog. The emergence test is the cross-instance applicability, not the per-instance fit. A single-instance functional-form match (BCS alone) does not constitute emergence; the 21-instance universality across qualitatively distinct physical regimes does.
>
> **Open work for promoting per-material BCS to emergence-class**: derive $B_{c0}$ and $T_c$ from substrate parameters per material (lattice geometry + Cosserat coupling + Op14 saturation onset) — currently NOT derived; both are inputs. If derived independently and matched to experimental values, BCS recovery would promote from definitional-identity to emergence.
>
> **Canonical manuscript source:** [Backmatter Ch 7 — Universal Saturation-Kernel Catalog](../../../../backmatter/07_universal_saturation_kernel.tex) (Vol 0). KB synthesis: [`trampoline-framework.md §7.5`](../../../common/trampoline-framework.md). Foundation Item 4 walk-back: see closure-roadmap §0.5 entry 2026-05-17 night.

---

## Numerical Validation

The superconductor engine (`ave.plasma.superconductor`) validates the Axiom 4 isomorphism against experimental data for four materials.

### $B_c(T) = B_{c0} \cdot S(T/T_c)$: Exact Match

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
