[↑ Ch.6 Solar System](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-3kmt3p]
-->

## Planetary Magnetospheres as Impedance Cavities

<!-- label: sec:planetary_magnetosphere -->

Each planet's magnetic dipole field creates a magnetopause: the boundary where magnetic pressure balances solar wind dynamic pressure. In impedance terms:

> **[Resultbox]** *Planetary Magnetopause Standoff*
>
> $$
> \frac{B^2(r_{mp})}{2\mu_0} = \frac{1}{2}\rho_{sw} v_{sw}^2 \quad\longrightarrow\quad r_{mp} = R_p \left(\frac{B_{eq}^2}{2\mu_0 P_{sw}}\right)^{1/6}
> $$

<!-- label: eq:magnetopause -->

The reflection coefficient $\Gamma$ at the magnetopause is computed using the same `reflection_coefficient()` function as all other domains.

---
