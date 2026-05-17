[↑ Ch.4 Continuum Electrodynamics](index.md)
<!-- leaf: verbatim -->

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

> **[Resultbox]** *1D String Tension Density (axial stiffness)*
>
> $$
> G_{string} = \frac{T_{EM}}{\ell_{node}} = \frac{m_e c^2}{\ell_{node}^2} \approx 5.49 \times 10^{11} \text{ Pa}
> $$

> **[Resultbox]** *Baseline 3D Vacuum Shear Modulus*
>
> $$
> G_{vac} = \rho_{bulk} \cdot c^2 \approx 7.12 \times 10^{23} \text{ Pa}
> $$
>
> Cross-check: $v_T = \sqrt{G_{vac}/\rho_{bulk}} = c$ (canonical transverse wave speed per [`photon-propagation-baseline.md:16`](photon-propagation-baseline.md), [`k4-port-irrep-decomposition.md:109`](../../operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md), [`de-broglie-standing-wave.md:236-240`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)).

**Correction note (2026-05-17 audit):** prior leaf revision conflated $G_{string}$ (1D axial stiffness, $T_{EM}/\ell_{node}$) with $G_{vac}$ (3D shear modulus, $\rho_{bulk} \cdot c^2$) and quoted "$G_{vac} \approx 5.48 \times 10^{24}$ Pa" — a 13-order-of-magnitude error. The correct quantities are now separated above per [`../../../vol2/appendices/app-f-solver-toolchain/derived-numerology.md:49-56`](../../../vol2/appendices/app-f-solver-toolchain/derived-numerology.md) which first identified the error. The 3D shear modulus $G_{vac}$ is what governs transverse-wave physics (photons, gravitational waves, bullet-cluster substrate-strain halos); the 1D string tension $G_{string}$ governs longitudinal/axial confinement physics.

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
