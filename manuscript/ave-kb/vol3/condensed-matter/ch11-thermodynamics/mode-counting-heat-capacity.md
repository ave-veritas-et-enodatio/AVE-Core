[↑ Ch.11: Thermodynamics and The Arrow of Time](../index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: uu6dl5 -->

---

## Mode Counting and Heat Capacity

### The 7-Mode Compliance Manifold

The Poisson ratio of the vacuum lattice, $\nu_{vac} = 2/7$, reveals the internal structure of each lattice node. The denominator $n = 7$ counts the **independent compliance modes per node**:

1. 3 translational degrees of freedom (displacement along $x$, $y$, $z$)
2. 3 rotational degrees of freedom (torsion about $x$, $y$, $z$)
3. 1 volumetric degree of freedom (radial breathing / compression)

The numerator $d = 2$ counts the transverse (shear) modes---the two polarisation states of a transverse electromagnetic wave. The ratio $\nu = d/n = 2/7$ is therefore the fraction of total compliance that responds to transverse shear, exactly as in classical elasticity theory.

### The Effective Degrees of Freedom ($g_*$)

The K4 unit cell of the SRS lattice (the chiral rod packing that defines the vacuum) contains $N_{K4} = 4$ nodes. In three dimensions, the total mode count is:

> **[Resultbox]** *The Effective Degrees of Freedom ($g_*$)*
>
> $$g_* = \frac{n^3}{N_{K4}} = \frac{7^3}{4} = \frac{343}{4} = 85.75$$

This is the lattice-derived effective number of relativistic degrees of freedom---the AVE replacement for the Standard Model's $g_{*,SM} = 106.75$, which is obtained by exhaustively counting all known particle species. The lattice derivation yields $g_*$ from pure geometry without reference to a particle catalog.

### Equipartition and Heat Capacity

By the classical equipartition theorem, each independent mode of the lattice at thermal equilibrium carries energy $\frac{1}{2} k_B T$. The total thermal energy density stored in the vacuum lattice at temperature $T$ is therefore:

> **[Resultbox]** *Vacuum Thermal Energy Density*
>
> $$u_{thermal} = \frac{1}{2} g_* \frac{k_B T}{\ell_{node}^3} = \frac{1}{2} \cdot \frac{343}{4} \cdot \frac{k_B T}{\ell_{node}^3}$$

The volumetric heat capacity of the vacuum lattice (at constant volume) follows immediately:

> **[Resultbox]** *Vacuum Volumetric Heat Capacity*
>
> $$c_v = \frac{\partial u_{thermal}}{\partial T} = \frac{g_*}{2} \cdot \frac{k_B}{\ell_{node}^3} \approx 42.875 \cdot \frac{k_B}{\ell_{node}^3}$$

This is the Dulong-Petit limit for the vacuum lattice as an elastic solid: a fixed heat capacity per unit cell, independent of temperature, valid at temperatures well above the lattice Debye temperature. At cosmological temperatures approaching the thermal mass of the lightest topological excitation ($T \sim m_e c^2 / k_B \approx 5.93 \times 10^9 \;\text{K}$), modes begin to freeze out and the heat capacity falls---exactly as in standard Debye theory for crystalline solids.

---
