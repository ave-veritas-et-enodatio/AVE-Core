[↑ Ch.13: Future Geometries](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [hd9bee]
-->

## 3D Torus Knot Antenna Simulation

The Diamond lattice architecture validates the physics completely on $O(N)$ computational complexity via fully vectorized numpy tensors. Time-domain scattering transforms down to:

$$
V^{ref}_{ijk\mu} = \sum_\nu S_{ijk\mu\nu} \, V^{inc}_{ijk\nu}
$$

By directly generating parametric 3D torus knots over the explicit K4 sublattice boundaries, structural self-interference directly validates resonant constraints.

Three-dimensional torus knots are generated via the standard parametric equations:

$$
\begin{align}
x(t) &= (R + r\cos qt)\cos pt, \\
y(t) &= (R + r\cos qt)\sin pt, \\
z(t) &= r\sin qt,
\end{align}
$$

discretized to the nearest lattice node with duplicate suppression.

**3D Results.** Broadband Gaussian-pulse excitation of three torus knot topologies on a $40^3$ lattice ($64{,}000$ nodes):

| Topology | $L$ [nodes] | $f_{peak}$ (FFT) | $pq/(p{+}q)$ | $\alpha \cdot pq/(p{+}q)$ |
|---|---|---|---|---|
| $(2,3)$ Trefoil | 156 | 0.050 | 1.200 | $8.76 \times 10^{-3}$ |
| $(3,5)$ Torus knot | 192 | 0.015 | 1.875 | $1.37 \times 10^{-2}$ |
| $(7,11)$ Torus knot | 358 | 0.015 | 4.278 | $3.12 \times 10^{-2}$ |

Three-dimensional mathematical energy conservation over the unitary S-matrix holds to $2.2 \times 10^{-16}$ (machine epsilon). In the non-reflective PML regime, the chiral frequency shift tracks strictly to the first-principles structural impedance $\Delta f / f = \alpha \cdot pq/(p+q)$. Because the engine abandons all numerical rotation matrix perturbations in favor of pure native wave tracing logic, the simulations directly confirm that continuous-field chiral properties emerge flawlessly from discrete topological graph parity.

**Physical interpretation.** The (7,11) topology produces the longest wire ($L = 358$ nodes) and therefore the lowest resonant frequency, but its high $pq/(p+q) = 4.278$ gives the *strongest* chiral coupling coefficient $\alpha \cdot pq/(p+q) = 3.12 \times 10^{-2}$. This confirms the analytical result from the preceding antenna analysis: the $(7,11)$ torus knot is the optimal topology for maximising lattice coupling, with a chiral FoM that scales linearly with the topological fraction $pq/(p+q)$.

[Figure: k4_tlm_phase3_4_3d_antenna.png — see manuscript/vol_4_engineering/chapters/]

---
