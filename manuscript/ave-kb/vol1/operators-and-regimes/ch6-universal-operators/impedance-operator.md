[↑ Ch.6 Universal Operators](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 as sec:universal_impedance -->
<!-- claim-quality: gdd70j -->

## Section 6.1: The Universal Impedance Operator

The complete derivation chain spans 14 orders of magnitude in length scale (from the lattice pitch $\ell_{node} \approx 3.86 \times 10^{-13}$ m to the Hubble radius $R_H \approx 1.33 \times 10^{26}$ m). A persistent question is whether these scales are merely analogical---linked by suggestive but structurally unrelated mathematics---or whether the *same operator* acts at every scale.

This book proves the latter.

> **Theorem (Scale Invariance):**
> The characteristic impedance $Z = \sqrt{\mu/\varepsilon}$ is the single structural invariant of the AVE framework. No scale-specific modifications, fitting parameters, or domain-dependent redefinitions are required. Every physical phenomenon in the derivation chain reduces to boundary conditions on this single operator.

This claim is verified computationally: the physics engine implements *one* function (`scale_invariant.impedance(mu, eps)`) that is called by every domain module---from particle confinement through seismic wave propagation.

### Cross-Scale Constitutive Mapping

Every row uses the *same* code path: `impedance(mu, eps)`.

| **Scale** | **$\varepsilon$ analog** | **$\mu$ analog** | **$Z = \sqrt{\mu/\varepsilon}$** |
|---|---|---|---|
| Vacuum lattice | $\varepsilon_0$ | $\mu_0$ | $Z_0 = 376.73\;\Omega$ |
| Plasma | $\varepsilon_0(1 - \omega_p^2/\omega^2)$ | $\mu_0$ | $Z_0/\sqrt{1-\omega_p^2/\omega^2}$ |
| Seismic | Compressibility $1/K$ | Shear compliance $1/G$ | Acoustic impedance $\rho V$ |
| Gravitational | $\varepsilon_0 \cdot n(r)$ | $\mu_0 \cdot n(r)$ | $Z_0$ (invariant) |
| Protein backbone | Backbone permittivity | Residue inductance | Minimal $S_{11}$ mismatch (Folding) |
| Lattice Boltzmann Fluid | Energy Density $\rho \equiv \varepsilon_0$ | Viscous Resistance $\nu$ | Kinematic Shear Impedance |
| Galactic (saturation) | Lattice capacitance | Mutual inductance $\eta$ | Rotation velocity |
| Antenna (HOPF-01) | Wire-over-ground $C$ | Wire self-inductance $L$ | $Z_{wire} = \sqrt{L/C}$ |

---
