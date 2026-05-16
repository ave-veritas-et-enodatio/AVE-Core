[↑ Ch.4 Continuum Electrodynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-crbl60]
-->

## Section 4.2: Continuum Electrodynamics of the LC Condensate

### The Dimensionally Exact Mass Density ($\rho_{bulk}$)

Previous classical aether models failed because they incorrectly attempted to map vacuum mass density directly to the magnetic permeability constant ($\mu_0$), violating SI dimensional analysis ($[\text{H/m}] \neq [\text{kg/m}^3]$).

The baseline macroscopic bulk mass density ($\rho_{bulk}$) of the spatial vacuum network is defined as follows. The effective inductive mass of one discrete node is derived from the inductance-mass isomorphism. The permeability $\mu_0$ has dimensions of $[\text{H/m}]$. Under the topo-kinematic isomorphism ($[\Omega] = \xi_{topo}^{-2}[\text{kg/s}]$), inductance maps to mass via $L = \xi_{topo}^{-2} m$. Because the vacuum inductance per unit length is $\mu_0$, the mass of one node spanning $\ell_{node}$ is:

> **[Resultbox]** *Effective Inductive Node Mass*
>
> $$
> m_{node} = \xi_{topo}^2 \mu_0 \ell_{node}
> $$

> **[Resultbox]** *Longitudinal Tension Wave Velocity*
>
> $$
> v_{longitudinal} = \sqrt{\frac{K_{bulk}}{\rho_{node}}}
> $$

Dividing by the Voronoi geometric volume of a single spatial node ($V_{node} = p_c \ell_{node}^3$, from the packing fraction $p_c = 8\pi\alpha$ derived in Chapter 2):

> **[Resultbox]** *Macroscopic Bulk Mass Density*
>
> $$
> \rho_{bulk} = \frac{m_{node}}{V_{node}} = \frac{\xi_{topo}^2 \mu_0 \ell_{node}}{p_c \ell_{node}^3} = \frac{\xi_{topo}^2 \mu_0}{p_c \ell_{node}^2} \approx 7.92 \times 10^6 \text{ kg/m}^3
> $$

> **[Resultbox]** *Baseline Vacuum Shear Modulus*
>
> $$
> G_{vac} = \rho_{bulk} \cdot c^2 \approx 7.11 \times 10^{23} \text{ Pa}
> $$

This is the macroscopic 3D shear modulus of the $\mathcal{M}_A$ condensate — the elastic resistance to transverse spatial deformation. It must not be confused with the 1D **string tension modulus**

$$
G_{string} = \frac{T_{EM}}{\ell_{node}} = \frac{m_e c^2}{\ell_{node}^2} \approx 5.49 \times 10^{11}\;\text{N/m}
$$

which governs individual edge stiffness but is $\sim 10^{12}\times$ smaller than the collective continuum value. The Cauchy bulk modulus is fixed at $K_{vac} = 2G_{vac}$ (the Cauchy relation for the isotropic lattice).

### Deriving the Kinematic Mutual Inductance of the Universe ($\nu_{kin}$)

In classical kinetic network theory, the Kinematic Mutual Inductance ($\nu$) of a continuous network medium is defined as the product of its characteristic signal velocity ($v$) and its internal microscopic mean free path ($\lambda$), modulated by a dimensionless geometric momentum diffusion factor ($\kappa$): $\nu = \kappa v \lambda$.

For the $\mathcal{M}_{A}$ hardware lattice, the absolute internal signal velocity is $c$, and the topological mean free path is exactly the fundamental spatial lattice pitch $\ell_{node}$.

As established in Section 1.3.2, the geometric packing fraction ($p_c$) determines the structural porosity and transverse geometric scattering cross-section of the discrete graph (where $\alpha = p_c/8\pi$). Consequently, the macroscopic momentum diffusion across the lattice inherits this geometric scattering threshold ($\kappa \equiv \alpha$).

> **[Resultbox]** *Kinematic Network Mutual Inductance*
>
> $$
> \nu_{kin}=\alpha c \ell_{node}\approx8.45\times10^{-7}\text{ m}^{2}\text{/s}
> $$

This parameter-free derivation shows that the discrete vacuum condensate possesses a macroscopic kinematic network mutual inductance close to that of liquid water.

---
