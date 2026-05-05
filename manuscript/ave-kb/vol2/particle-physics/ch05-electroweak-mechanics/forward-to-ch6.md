[↑ Ch.5 — Electroweak Mechanics](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: jkpfd4 -->

## Electroweak Mechanics: Forward Reference

The complete quantitative derivations of the Weak Mixing Angle ($\sin^2\theta_W = 2/9$), the W and Z boson masses, the three-generation lepton spectrum, the neutrino mass hierarchy, and the Schwinger anomalous magnetic moment ($a_e = \alpha/2\pi$) are presented in full in [Ch.6 — Electroweak and Higgs](../ch06-electroweak-higgs/index.md). Those derivations build directly on the Cosserat micropolar mechanics and gauge structure established above.

## The Gauge Layer: From Topology to Symmetry

### U(1) Electromagnetism from the Lattice Plaquette

The physical continuous connection between adjacent nodes $i$ and $j$ is mathematically described by a unitary link variable $U_{ij} = e^{i\theta_{ij}}$, where $\theta_{ij}$ is the phase accumulated along the edge. The simplest gauge-invariant geometric quantity is the triangular plaquette---the product of link variables around a closed 3-node loop:

> **[Resultbox]** *Lattice Gauge Plaquette*
>
> $$
> U_P = U_{ij}U_{jk}U_{ki} = e^{i(\theta_{ij} + \theta_{jk} + \theta_{ki})}
> $$

The total phase around the plaquette is the discrete lattice curl of the gauge connection. For small phase gradients ($\theta_{ij} \approx A_\mu l_{node}$), the Taylor expansion of $U_P$ yields:

> **[Resultbox]** *Discrete Lattice Curl*
>
> $$
> \theta_{ij} + \theta_{jk} + \theta_{ki} = \oint \mathbf{A} \cdot d\mathbf{l} = \iint (\nabla \times \mathbf{A}) \cdot d\mathbf{S} = \iint \mathbf{B} \cdot d\mathbf{S} \equiv \Phi_P
> $$

The lattice action is constructed by summing over all plaquettes the deviation from unit phase:

> **[Resultbox]** *U(1) Lattice Action to Maxwell Limit*
>
> $$
> S_{lattice} = \sum_P \left(1 - \text{Re}\, U_P\right) = \sum_P \left(1 - \cos\Phi_P\right) \approx \sum_P \frac{1}{2}\Phi_P^2 \longrightarrow \int \frac{1}{4}F_{\mu\nu}F^{\mu\nu}\, d^4x
> $$

The continuum limit ($l_{node} \to 0$) recovers the Maxwell Lagrangian ($-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}$). **U(1) Electromagnetism** is therefore the enforcement of unitary topological continuity across the discrete graph---the standard Wilson formulation of lattice gauge theory, here derived from the physical structure of the $\mathcal{M}_A$ hardware.

### SU(3) Color Charge from the Borromean Linkage

The Borromean proton ($6^3_2$) consists of three topologically indistinguishable interlocked flux loops. Because no two loops are individually linked, the mathematical permutation symmetry of the three-loop system is the symmetric group $S_3$. This discrete symmetry classifies the allowed "color" states of the composite defect.

To parallel-transport the continuous phase field $\mathbf{A}$ smoothly across a tri-partite symmetric graph, the connection must locally respect $S_3$ permutation invariance while preserving the unitarity of phase transport. The smallest continuous Lie group whose discrete quotient contains $S_3$ as a subgroup of its Weyl group is $SU(3)$. Explicitly:

- The $S_3$ permutation group is the Weyl group of $SU(3)$.
- The three fundamental flux loops of the Borromean linkage transform under the fundamental representation (**3**) of $SU(3)$.
- The $\mathbb{Z}_3$ center of $SU(3)$ enforces the strict topological constraint that only color-singlet (**1**) composite states---where all three loops are linked---can propagate as free particles. This is confinement.

**SU(3) Color Charge** is derived as the effective field theory limit of a three-loop topological defect traversing a discrete condensate grid. The "colour" quantum number is the permutation label of which flux loop carries the dominant phase winding at any given lattice site.

---
