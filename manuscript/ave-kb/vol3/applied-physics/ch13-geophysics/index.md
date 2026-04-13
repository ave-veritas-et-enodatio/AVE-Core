[↑ Applied Physics](../index.md)

# Ch.13: Geophysics: Seismic Waves

Seismic wave propagation modelled on the universal 3D FDTD Maxwell engine by mapping PREM Earth model impedance profiles onto $\varepsilon_r$, $\mu_r$ material maps. The same `reflection_coefficient(Z1, Z2)` function used for particle boundaries, plasma cutoff, and antenna ports produces correct seismic reflection coefficients at all major Earth discontinuities.

## Key Results

| Result | Statement |
|---|---|
| Seismic Reflection Coefficient (Moho) | $\Gamma_{\text{Moho}} = (\rho_2 V_{p2} - \rho_1 V_{p1})/(\rho_2 V_{p2} + \rho_1 V_{p1}) \approx 0.29$ |
| Constitutive Mapping | $\varepsilon_r(r) = K_{\text{ref}}/K(r)$; $\mu_r(r) = G_{\text{ref}}/G(r)$ |
| LVZ Waveguide Critical Angle | $\theta_c \approx 69^\circ$; total internal reflection identical to optical fibre and QCD confinement |
| Planetary Magnetic Dipole (AC Motor) | $M_\oplus \approx 1.5 \times 10^{23}$ A$\cdot$m$^2$ from VCA Back-EMF (empirical: $8.0 \times 10^{22}$) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Resultbox: Seismic Reflection Coefficient (Moho)](./seismic-reflection-coefficient-moho.md) | $\Gamma_{\text{Moho}}$ formula |
| [Seismic FDTD Engine](./seismic-fdtd-engine.md) | Universal wave engine; constitutive mapping; PREM injection |
| [Constitutive Mapping](./constitutive-mapping.md) | Compressibility $\to$ capacitance; shear compliance $\to$ inductance |
| [PREM Layers and Waveguide Trapping](./prem-layers-waveguide.md) | PREM layer impedance table; Moho numerical evaluation; LVZ waveguide trapping |
| [Geodynamo VCA Back-EMF](./geodynamo-vca-back-emf.md) | Earth as AC induction motor rotor; Motional EMF; Venus/Mars falsifiability |

---
