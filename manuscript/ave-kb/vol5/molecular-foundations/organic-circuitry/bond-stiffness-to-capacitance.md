[↑ Organic Circuitry](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [lm9b3j]
-->

---

## Bond Stiffness → Capacitance: $C = \xi^2 / k$

Chemical bonds define the structural tension between nuclei. In AVE terms, shared valence electrons create a zone of dielectric compliance ($\varepsilon_\text{eff}$). A covalent bond is therefore a **Capacitor** ($C$). Critically, tighter bonds have *less* compliance and thus *lower* absolute capacitance:

> **[Resultbox]** *Topological Capacitance of a Bond*
>
> $$
> C_\text{bond} \;=\; \frac{\xi^2_\text{topo}}{k_\text{bond}}
> \qquad [\text{Farads}]
> \label{eq:C_bond}
> $$

where $k_\text{bond}$ [N/m] is the stretching force constant. These values are conventionally obtained from infrared spectroscopy (Shimanouchi, 1972; NIST Chemistry WebBook), but the first-principles derivation demonstrates that they can be derived from first principles using only $\varepsilon_0$, $m_e$, $\hbar$, and $e$ — eliminating any dependence on spectroscopic measurement.

| **Bond** | $k$ **(N/m)** | **Source $\tilde{\nu}$ (cm$^{-1}$)** | **Capacitance (aF)** |
|---|---|---|---|
| C--H | 494 | $\sim$3000 | 348 |
| C--C | 354 | $\sim$1000 | 486 |
| C=C | 965 | $\sim$1650 | 178 |
| C--N | 461 | $\sim$1100 | 373 |
| C=O | 1170 | $\sim$1700 | 147 |
| C--O | 489 | $\sim$1100 | 352 |
| N--H | 641 | $\sim$3400 | 269 |
| O--H | 745 | $\sim$3650 | 231 |
| S--H | 390 | $\sim$2600 | 441 |
| C--S | 253 | $\sim$700 | 680 |

*Bond capacitances derived from $C = \xi^2 / k$. Force constants from NIST IR data.*

---
