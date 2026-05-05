[↑ Ch.15 Black Hole Orbitals](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [c6k5om]
-->

## Hawking Radiation as Spontaneous Emission

<!-- label: sec:hawking_emission -->

In atomic physics, an excited electron orbital emits photons (spectral lines) as it relaxes to a lower energy state. The black hole analogue follows directly from the Fluctuation-Dissipation Theorem (Chapter ch:thermodynamics).

As established in Section sec:fluctuation\_dissipation, thermal noise from the ambient vacuum lattice couples into any structure through its boundary. At the saturation boundary, the phase transition is not perfectly sharp---the lattice does not rupture instantaneously. The residual elastic coupling across the boundary transmits a vanishingly small fraction of the ambient Nyquist noise:

$$
P_{transmitted} \propto \left.\frac{\partial S}{\partial r}\right|_{r_{sat}} \cdot P_{incident}
$$

This is **Hawking radiation**---not quantum tunnelling, but the classical thermodynamic leakage of lattice noise through the imperfect phase boundary. The leakage rate is set by the gradient of the saturation factor $S(r)$ at $r_{sat}$.

The characteristic temperature of this emission is set by the impedance gradient at the horizon:

> **[Resultbox]** *Hawking Temperature as Impedance Noise*
>
> $$
> T_H = \frac{\hbar c^3}{8\pi G M k_B}
> $$

This is the Nyquist noise temperature of the vacuum lattice evaluated at the event horizon impedance boundary. The black hole's Hawking radiation is its **spontaneous emission spectrum**---the macroscopic analogue of an excited atom radiating spectral lines as it relaxes.

As the black hole radiates, its mass decreases, the impedance boundary tightens, and the emission temperature increases. This positive feedback loop drives the evaporation to completion---the macroscopic equivalent of an unstable excited orbital cascading down through the emission spectrum until the confinement structure itself dissolves.

---
