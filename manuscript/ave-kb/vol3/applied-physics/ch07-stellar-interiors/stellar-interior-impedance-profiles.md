[↑ Ch.7: Stellar Interiors and Neutrino Oscillation](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: o6kgkz -->

---

## Stellar Interiors as Impedance Profiles

A star is a self-gravitating plasma whose electron density $n_e(r)$ increases from the corona ($\sim10^{15}\;\text{m}^{-3}$) to the core ($\sim10^{32}\;\text{m}^{-3}$). Each radial shell has a local plasma frequency $\omega_p(r) = \sqrt{n_e e^2/m_e\varepsilon_0}$, creating a spherical impedance waveguide.

### Tachocline as Impedance Boundary: Step-by-Step $\Gamma$ Derivation

The tachocline ($r \approx 0.71\,R_\odot$) separates the rigid radiative zone from the convective envelope---exactly analogous to the Mohorovicic boundary in the Earth.

Using the universal operators:

1. **Constitutive mapping:** On the radiative side, $n_e \approx 4 \times 10^{30}$ m$^{-3}$; on the convective side, $n_e \approx 6 \times 10^{29}$ m$^{-3}$.
2. **Impedance computation:** $Z(r) = Z_0 / \sqrt{1 - (\omega_p/\omega)^2}$ via `impedance()`.
3. **Reflection coefficient:** $\Gamma = (Z_2 - Z_1)/(Z_2 + Z_1)$ via `reflection_coefficient()`.

The resulting $\Gamma \approx 0.82$ traps internal gravity waves and maintains the differential rotation profile. This is the *same* algebraic formula that produces Pauli exclusion ($\Gamma = -1$) at the particle boundary and Moho reflection ($\Gamma = 0.29$) inside the Earth.

### Helioseismology as Cavity Resonance

Solar p-modes are standing acoustic waves---transmission line resonances of the impedance cavity, the same physics as the protein backbone S$_{11}$ modes.

---
