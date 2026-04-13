[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol5 as sec:z_topo_table -->

# Tier 2: Complex Topological Impedance $Z_{topo}$

Each amino acid maps to a complex impedance $Z_i = R_i + jX_i$ where:

- $R_i$ encodes the sidechain's hydrophobic volume (resistive coupling to vacuum)
- $X_i$ encodes the sidechain's charge reactance, scaled by the backbone $Q$-factor:

> **[Resultbox]** *Topological Charge Reactance*
>
> $$X_i = \begin{cases} -R_i / Q & \text{negative charge (capacitive): D, E} \\ +R_i / Q & \text{positive charge (inductive): K, R} \\ \pm R_i / 2Q & \text{polar uncharged: S, T, C, Y, N, Q, H} \\ 0 & \text{hydrophobic: A, V, I, L, M, F, W, P, G} \end{cases}$$

The $Q$-factor scaling ensures that resistive (hydrophobic) coupling dominates at $\sim 85\%$, with reactive (electrostatic) coupling as a $\sim 15\%$ perturbation. This ratio is *derived* from the backbone's amide-V resonance width.

| **AA** | $R$ | $X$ | $|Z|$ | **Type** |
|---|---|---|---|---|
| G | 0.304 | 0.000 | 0.30 | Hydrophobic (minimal stub) |
| A | 0.568 | 0.000 | 0.57 | Hydrophobic |
| V | 0.605 | 0.000 | 0.61 | Hydrophobic |
| I | 0.610 | 0.000 | 0.61 | Hydrophobic |
| L | 0.610 | 0.000 | 0.61 | Hydrophobic |
| P | 0.632 | 0.000 | 0.63 | Hydrophobic (cyclic) |
| K | 0.639 | $+0.091$ | 0.65 | Positive charge |
| M | 0.723 | 0.000 | 0.72 | Hydrophobic |
| T | 0.713 | $+0.051$ | 0.71 | Polar uncharged |
| R | 0.740 | $+0.106$ | 0.75 | Positive charge |
| S | 0.764 | $+0.055$ | 0.77 | Polar uncharged |
| Q | 0.782 | $+0.056$ | 0.78 | Polar uncharged |
| F | 0.786 | 0.000 | 0.79 | Hydrophobic |
| C | 0.824 | $-0.059$ | 0.83 | Polar uncharged |
| Y | 0.833 | $-0.060$ | 0.84 | Polar uncharged |
| N | 0.840 | $+0.060$ | 0.84 | Polar uncharged |
| E | 0.849 | $-0.121$ | 0.86 | Negative charge |
| H | 0.862 | $+0.062$ | 0.86 | Polar (half-protonated) |
| W | 0.895 | 0.000 | 0.89 | Hydrophobic |
| D | 0.949 | $-0.136$ | 0.96 | Negative charge |

*Ab initio complex $Z_{topo}$. $R = \sqrt{L_R/C_R}/\sqrt{L_\text{bb}/C_\text{bb}}$; all values in $[0.30, 0.96]$.*

---
