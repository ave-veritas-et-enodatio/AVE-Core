[↑ Ch.3 Quantum and Signal Dynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-yiyyi3]
-->

## Section 3.1: The Dielectric Lagrangian: Hardware Mechanics

Standard Quantum Field Theory (QFT) relies on a Lagrangian density ($\mathcal{L}$) describing fields as mathematical operators. In Applied Vacuum Engineering, the continuous quantum formalism is derived from the discrete finite-element signal dynamics of the $\mathcal{M}_A$ lattice.

The substitution of $\xi_{topo}$ converts the electromagnetic Lagrangian density into continuous mechanical stress ($\text{N/m}^2$), grounding Axiom 3 in bulk continuum mechanics. The total macroscopic energy density of the manifold is the sum of the energy stored in the capacitive edges (dielectric strain) and the inductive nodes (kinematic inertia). To construct a relativistically invariant action principle, the Lagrangian difference ($\mathcal{L} = \mathcal{T} - \mathcal{U}$) is evaluated.

The canonical field variable for evaluating transverse waves across a discrete graph is the **Magnetic Vector Potential** ($\mathbf{A}$), defining the magnetic flux linkage per unit length ($[\text{Wb/m}] = [\text{V}\cdot\text{s/m}]$). Because the generalized velocity of this coordinate is identically the electric field ($\mathbf{E} = -\partial_t \mathbf{A}$), the capacitive energy takes the role of kinetic energy ($\mathcal{T}$), and the inductive energy acts as potential energy ($\mathcal{U}$).

> **[Resultbox]** *Dielectric Lagrangian Density*
>
> $$
> \mathcal{L}_{AVE} = \frac{1}{2} \epsilon_0 \left| \frac{\partial \mathbf{A}}{\partial t} \right|^2 - \frac{1}{2\mu_0} |\nabla \times \mathbf{A}|^2
> $$

### Dimensional Proof: The Vector Potential as Mass Flow

Evaluating the SI dimensions of this continuous field confirms its mechanical identity. Applying the topological conversion constant ($\xi_{topo} \equiv e/\ell_{node}$ measured in $[\text{C/m}]$) to the canonical variable $\mathbf{A}$:

> **[Resultbox]** *Vector Potential Dimensions*
>
> $$
> [\mathbf{A}] = \left[ \frac{\text{V} \cdot \text{s}}{\text{m}} \right] = \left[ \frac{\text{J} \cdot \text{s}}{\text{C} \cdot \text{m}} \right] = \left[ \frac{\text{kg} \cdot \text{m}^2 \cdot \text{s}}{\text{s}^2 \cdot \text{C} \cdot \text{m}} \right] = \left[ \frac{\text{kg} \cdot \text{m}}{\text{s} \cdot \text{C}} \right]
> $$

By substituting the mathematically exact topological conversion $\text{C} \equiv \xi_{topo} \text{ m}$ derived in Chapter 2, the spatial metric evaluates to:

> **[Resultbox]** *Vector Potential as Mass Flow*
>
> $$
> [\mathbf{A}] = \left[ \frac{\text{kg} \cdot \text{m}}{\text{s} \cdot (\xi_{topo} \text{ m})} \right] = \mathbf{\xi_{topo}^{-1} \left[ \frac{\text{kg}}{\text{s}} \right]}
> $$

This establishes a fundamental dimensional equivalence: the magnetic vector potential ($\mathbf{A}$) is physically isomorphic to the continuous **Mass Flow Rate** (linear momentum density) of the vacuum lattice, scaled inversely by the topological dislocation constant. The time derivative therefore carries one extra factor of inverse time: $[\partial_t \mathbf{A}] = \xi_{topo}^{-1}\,[\text{kg/s}^2]$.

When evaluating the full kinetic energy density term using this mechanical substitution, and retrieving the exact capacitive compliance derivation from Chapter 2 ($\epsilon_{0}\equiv\xi_{topo}^2[\text{N}^{-1}]$), the topological scaling constants cancel:

> **[Resultbox]** *Kinetic Energy Density Dimensions*
>
> $$
> [\mathcal{L}_{kin}]=\frac{1}{2}\epsilon_{0}|\partial_{t}A|^{2}\Rightarrow(\xi_{topo}^{2}[\text{N}^{-1}])\left(\xi_{topo}^{-1}\frac{\text{kg}}{\text{s}^2}\right)^{2}=\left(\frac{\xi_{topo}^{2}}{\xi_{topo}^{2}}\right)\frac{\text{kg}^{2}}{\text{N}\cdot \text{s}^{4}}=\frac{\text{kg}^{2}}{(\text{kg}\cdot \text{m}/\text{s}^{2})\cdot \text{s}^{4}}\equiv\left[\frac{\text{N}}{\text{m}^{2}}\right]
> $$

Minimizing the quantum action is mathematically equivalent to minimizing the continuous inductive bulk stress (Pascals) of the $\mathcal{M}_{A}$ manifold.

---
