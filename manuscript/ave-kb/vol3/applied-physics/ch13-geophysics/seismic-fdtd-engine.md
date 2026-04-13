[↑ Ch.13: Geophysics: Seismic Waves](../index.md)
<!-- leaf: verbatim -->

---

## Seismic Wave Propagation on the FDTD Engine

The 3D FDTD Maxwell solver (`fdtd_3d.py`) is a *universal* wave engine. Injecting the PREM Earth model's impedance profile as material maps ($\varepsilon_r$, $\mu_r$) along the radial axis produces correct seismic wave propagation, reflection coefficients at layer boundaries, and waveguide trapping in the low-velocity zone.

## Constitutive Mapping

$$\begin{align}
\varepsilon_r(r) &= K_{\text{ref}} / K(r) \quad\text{(compressibility } \to \text{ capacitance)} \\
\mu_r(r) &= G_{\text{ref}} / G(r) \quad\text{(shear compliance } \to \text{ inductance)}
\end{align}$$

and the reflection coefficient at each boundary is:

> **[Resultbox]** *Seismic Reflection Coefficient (Moho)*
>
> $$\Gamma_{\text{Moho}} = \frac{\rho_2 V_{p2} - \rho_1 V_{p1}}{\rho_2 V_{p2} + \rho_1 V_{p1}}$$

which is the *same* `reflection_coefficient(Z1, Z2)` used for Pauli exclusion, plasma cutoff, superconductor boundaries, and antenna port $S_{11}$.

---
