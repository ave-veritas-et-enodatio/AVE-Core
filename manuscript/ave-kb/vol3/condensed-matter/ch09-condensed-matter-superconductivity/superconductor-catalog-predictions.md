[↑ Ch.9: Condensed Matter and Superconductivity](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [qky559]
-->

---

## Superconductor Catalog: AVE Engine Predictions

The AVE superconductor engine (`ave.plasma.superconductor`) computes critical fields and London depths from first principles via the universal saturation operator $S(T/T_c) = \sqrt{1 - (T/T_c)^2}$.

| **Material** | **$T_c$ [K]** | **$B_{c0}$ [T]** | **$\lambda_L$ [nm]** | **Type** |
|---|---|---|---|---|
| Aluminium | 1.18 | 0.0105 | 12.5 | I |
| Lead | 7.19 | 0.0803 | 14.6 | I |
| Niobium | 9.25 | 0.206 | 22.5 | II |
| MgB$_2$ | 39.0 | 16.0 | 40.8 | II |
| YBCO | 92.0 | 100.0 | 118.8 | II |

The key identity is that the BCS critical field profile $B_c(T) = B_{c0}\sqrt{1-(T/T_c)^2}$ is *exactly* the Axiom 4 saturation factor $S(T/T_c)$. The Meissner effect is the magnetic-sector analog of plasma screening: a saturated $\mu_{eff} \to 0$ expels flux, just as a saturated $\epsilon_{eff} \to 0$ expels E-field in a plasma.

### Regime Classification

| **State** | **Regime** | **Physical Character** |
|---|---|---|
| Superconducting ($T < T_c$) | I (Linear) | Phase-locked inductors; $\mu_{eff} \to 0$ |
| Transition ($T \approx T_c$) | I--II boundary | Partial saturation; mixed state |
| Normal ($T > T_c$) | II (Yield) | Thermal disorder breaks phase lock |

---
