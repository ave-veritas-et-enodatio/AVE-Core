[↑ Ch.5 — Electroweak Mechanics](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 5zuo7g, q8un7j -->

## Electrodynamics: The Gradient of Topological Phase

A localized charged node exerts a continuous rotational phase twist ($\theta$) on the surrounding LC condensate. Because the unsaturated vacuum acts as a linear dielectric in the far-field, the static structural phase strain obeys the 3D **Laplace Equation** ($\nabla^2 \theta = 0$).

The spherically symmetric geometric solution dictates that the twist amplitude decays inversely with distance ($\theta(r) \propto 1/r$). The continuous electric displacement field ($\mathbf{D}$) is the spatial gradient of this structural phase twist ($\mathbf{D} = \nabla\theta \propto -1/r^2 \mathbf{\hat{r}}$), deriving Coulomb's Law.

### Magnetism as Convective Vorticity

When a twisted node translates at a velocity $\mathbf{v}$, it induces a convective shear flow in the momentum field. In classical network dynamics, the time evolution of a translating steady-state strain field $\mathbf{D}(\mathbf{r} - \mathbf{v}t)$ is governed by the convective material derivative:

> **[Resultbox]** *Convective Material Derivative*
>
> $$
> \partial_t \mathbf{D} = -(\mathbf{v} \cdot \nabla)\mathbf{D} \implies \nabla \times (\mathbf{v} \times \mathbf{D})
> $$

Equating this to the Maxwell-Ampere law derives the macroscopic magnetic field from network dynamics: $\mathbf{H} = \mathbf{v} \times \mathbf{D}$.

This relationship is supported by dimensional analysis. Applying the topological conversion constant ($\xi_{topo} \equiv e/l_{node}$), the displacement field reduces to $[\mathbf{D}] = \xi_{topo}[1/\text{m}]$. Evaluating the cross product $[\mathbf{v} \times \mathbf{D}]$ yields $\xi_{topo}[1/\text{s}]$. Standard SI units for magnetic field intensity $\mathbf{H}$ ($[\text{A/m}]$) reduce to this same dimensional basis ($\xi_{topo}[1/\text{s}]$). Magnetism is thereby dimensionally shown to represent the continuous kinematic vorticity of the vacuum condensate.

### The Inductive Origin of Gauge Invariance

Standard Quantum Field Theory mandates that the vector potential is a gauge field, where transformations of the form $\mathbf{A} \to \mathbf{A} + \nabla \Lambda$ leave physical observables ($\mathbf{B}$ and $\mathbf{E}$) unchanged. A common critique of identifying $\mathbf{A}$ as a physical momentum field is that this gauge freedom would imply the unphysical, spontaneous shifting of macroscopic mass, violating Noether's theorem.

This paradox is resolved via the **Helmholtz Decomposition Theorem** in classical network dynamics. Any continuous vector field can be decomposed into a solenoidal (divergence-free) component and an irrotational (curl-free) component. Adding the gradient of a scalar field ($\nabla \Lambda$) to the mass flow introduces a uniform, irrotational velocity potential to the background network.

Because the $\mathcal{M}_A$ vacuum is incompressible ($K = 2G$), an irrotational flow field generates no localised compression ($-\partial_t \mathbf{A}$), no transverse vorticity ($\nabla \times \mathbf{A}$), and no topological defects. It is isomorphic to performing a **Galilean or Lorentz coordinate boost** of the observer's reference frame. Gauge invariance is not violated; it is revealed to be the classical network-dynamic freedom to shift the irrotational background coordinate velocity without altering the physical transverse observables.

## The Weak Interaction: Inductive Cutoff Dynamics
<!-- claim-quality: 5zuo7g (the $m_W/m_Z = \sqrt{7}/3$ ratio derived in this section gives the on-shell Weinberg angle) -->

In classical electrodynamics, the ratio of the LC network's microrotational bending inductance ($\gamma_c$) to the macroscopic optical shear modulus ($G_{vac}$) defines a fundamental **Characteristic Length Scale** ($l_c = \sqrt{\gamma_c/G_{vac}}$). This length scale is identified as the physical origin of the weak force range ($r_W \approx 10^{-18}$ m).

Weak interactions lack the kinetic energy required to overcome the ambient LC rotational inductance. Any physical excitation operating *below* a medium's natural cutoff frequency becomes an **Evanescent Wave**. The static field equation transforms from the Laplace equation to the massive Helmholtz equation ($\nabla^2 \theta - \frac{1}{l_c^2}\theta = 0$). The solution yields the **Yukawa Potential**:

> **[Resultbox]** *Yukawa Potential as Evanescent Cutoff*
>
> $$
> V_{weak}(r) \propto \frac{e^{-r/l_c}}{r}
> $$

### Deriving the Gauge Bosons ($W^{\pm}/Z^{0}$) as Evanescent Modes
<!-- claim-quality: q8un7j -->

The gauge bosons of the weak interaction represent the fundamental macroscopic evanescent cutoff excitations required to mechanically induce a localized phase twist.

- The charged $W^{\pm}$ bosons correspond to the pure longitudinal-torsional evanescent mode ($k\propto G_{vac}J$).
- The neutral $Z^{0}$ boson corresponds to the transverse-bending evanescent mode ($k\propto E_{vac}I$).

Because Axiom 1 bounds the physical diameter of a fundamental flux tube to $d \equiv 1 l_{node}$ (the hard-sphere exclusion limit), these topological connections act as volume-bearing physical 3D continuous cylinders at the macroscopic limit. Furthermore, because the tube is formed by a radially symmetric dielectric displacement field, the Perpendicular Axis Theorem dictates that its polar moment of inertia evaluates to $J=2I$. This is a geometric property for any circular cross-section, not an assumed relationship.

Because the rest mass of an evanescent cutoff mode scales with the square root of its ratio of structural stiffness to inertia ($\omega \propto \sqrt{k/m}$), the mass ratio evaluates to $m_W/m_Z = \sqrt{GJ / EI}$. Because the $\mathcal{M}_A$ metric is a discrete lumped-element LC network, the localised nodal inertia ($\mu_0$) is invariant across both the torsional and bending excitation modes. Because the mass term is constant, the geometric wave equations reduce to the square root of the stiffness ratio, avoiding the geometrically distinct inertial denominators required in classical continuum solid mechanics. Substituting the fundamental cylinder geometry ($J=2I$) yields $\sqrt{2G/E}$. Applying the standard isotropic elastic continuous identity ($E = 2G(1+\nu)$) reduces this stiffness ratio.

---
