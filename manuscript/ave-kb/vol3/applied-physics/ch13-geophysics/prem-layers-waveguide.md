[↑ Ch.13: Geophysics: Seismic Waves](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: zsqh87 -->

---

## PREM Layer Data and Numerical Evaluation

The major discontinuities of the Preliminary Reference Earth Model (PREM) and the corresponding seismic impedance computed by the AVE engine:

| **Boundary** | $\rho$ (kg/m$^3$) | $V_P$ (km/s) | $Z = \rho V_P$ (MPa$\cdot$s/m) | $|\Gamma|$ |
|---|---|---|---|---|
| Surface (crust) | 2,600 | 5.8 | 15.1 | --- |
| Moho (crust/mantle) | 3,380 | 8.1 | 27.4 | 0.29 |
| 670 km (upper/lower) | 3,990 | 10.3 | 41.1 | 0.20 |
| CMB (mantle/core) | 9,900 | 8.1 | 80.2 | 0.32 |
| ICB (outer/inner) | 12,760 | 11.0 | 140.4 | 0.27 |

Reflection coefficients are computed by the universal `reflection_coefficient(Z1, Z2)` function---identical to the function used for particle boundaries, plasma cutoffs, and antenna ports.

The Moho reflection coefficient evaluates numerically:

$$\Gamma_{\text{Moho}} = \frac{Z_{\text{mantle}} - Z_{\text{crust}}}{Z_{\text{mantle}} + Z_{\text{crust}}} = \frac{27.4 - 15.1}{27.4 + 15.1} = \frac{12.3}{42.5} \approx 0.29$$

This is the *same* algebraic formula that produces Pauli exclusion ($\Gamma = -1$) at the saturated particle boundary and gravitational stealth ($\Gamma = 0$) in a gravity well. The only difference is the input impedances.

## Waveguide Trapping in the Low-Velocity Zone

Between 80 and 220 km depth, the PREM model exhibits a pronounced low-velocity zone (LVZ) where partial melting reduces $V_S$ by $\sim 5\%$. This creates a seismic waveguide: energy injected into the LVZ undergoes total internal reflection at both boundaries where the impedance increases outward.

The trapping condition is:

$$\sin\theta_c = \frac{V_{LVZ}}{V_{surround}} \approx \frac{4.35}{4.65} \approx 0.936 \quad \Longrightarrow \quad \theta_c \approx 69^\circ$$

Seismic energy arriving at angles greater than $\theta_c$ is perfectly reflected back into the channel---structurally identical to optical fibre total internal reflection and the QCD flux-tube confinement derived in Volume IV. The universal impedance operator governs wave trapping from $10^{-15}$ m (nucleon) to $10^{6}$ m (planetary mantle).

---
