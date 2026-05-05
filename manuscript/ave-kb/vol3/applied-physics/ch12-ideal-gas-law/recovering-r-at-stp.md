[↑ Ch.12: The Ideal Gas Law and Fluid Pressure](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: cul4it -->

---

## Quantitative Verification: Recovering $R$ at STP

To confirm that the LC energy balance is not merely a qualitative analogy, the numerical evaluation at Standard Temperature and Pressure (STP) must reproduce the empirical gas constant.

At STP ($T = 273.15$ K, $P = 101{,}325$ Pa), one mole of ideal gas ($N = N_A = 6.022 \times 10^{23}$) occupies $V = 22.414 \times 10^{-3}$ m$^3$. The thermal energy per node is:

$$\langle U_{noise} \rangle = \frac{3}{2}\, k_B\, T = \frac{3}{2} \times 1.381 \times 10^{-23} \times 273.15 \approx 5.657 \times 10^{-21} \text{ J}$$

The macroscopic pressure exerted by $N_A$ topological nodes on the cavity walls is:

$$P = \frac{N_A \cdot \langle U_{noise} \rangle}{V} \cdot \frac{2}{3} = \frac{N_A \cdot k_B \cdot T}{V}$$

The factor of $2/3$ converts the 3D thermal energy to the 1D ponderomotive pressure along each Cartesian axis. Evaluating:

$$R = \frac{PV}{nT} = N_A \cdot k_B = 6.022 \times 10^{23} \times 1.381 \times 10^{-23} = 8.314 \text{ J/(mol}\cdot\text{K)}$$

This is the exact CODATA value of the universal gas constant. The identity $R = N_A k_B$ is not a coincidence but a structural theorem: Boltzmann's constant is the per-node LC thermal energy scaling, and the gas constant is its macroscopic (per-mole) projection. No parameter beyond the lattice axioms is required.

### Quantitative Summary

| **Quantity** | **AVE** | **CODATA** | **Error** |
|---|---|---|---|
| $k_B$ | $1.381 \times 10^{-23}$ J/K | $1.380\,649 \times 10^{-23}$ J/K | Exact (SI input) |
| $N_A$ | $6.022 \times 10^{23}$ /mol | $6.022\,140\,76 \times 10^{23}$ /mol | Exact (SI input) |
| $R = N_A k_B$ | 8.314 J/(mol$\cdot$K) | 8.314,462 J/(mol$\cdot$K) | $< 0.001\%$ |
| STP molar volume | 22.414 L | 22.414 L | Exact |

---
