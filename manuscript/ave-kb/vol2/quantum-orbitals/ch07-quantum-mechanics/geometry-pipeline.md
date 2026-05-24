[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-oltvwy]
-->

## Complete Geometry-to-Solver Pipeline

Given any element with nuclear charge $Z$ and electron configuration $[n_i, l_i, m_{l,i}]_{i=1}^{N}$, the complete mapping to the Mutual Cavity Loading IE solver is:

**Stage A: Per-Electron Geometry.** For each electron $i$ with quantum numbers $(n_i, l_i, m_{l,i})$:

$$
\begin{align}
\text{Ring radius:} \quad R_i &= \frac{a_0 n_i^2}{Z} \\
\text{Orbital frequency:} \quad \omega_i &= \frac{Z^2 \alpha^2 m_e c^2}{\hbar\, n_i^3} \\
\text{Self-inductance:} \quad L_i &= \mu_0 R_i \left[\ln\!\left(\frac{8 R_i}{l_{\text{node}}}\right) - 2\right] \\
\text{Char.\ impedance:} \quad Z_{LC,i} &= \omega_i L_i
\end{align}
$$

All computed at bare nuclear charge $Z$. No $Z_{\text{eff}}$, no screening.

**Stage B: Pair Classification.** For each pair of electrons $(i, j)$, the coupling type is determined purely by their geometric relationship:

| Configuration | Same $n$? | Link Type | Crossings | Topology Factor |
|---|---|---|---|---|
| Same shell, same $m_l$ | Yes | Hopf ($2_1^2$) | 2 (parallel) | $1 - p_c/2$ |
| Same shell, diff. $m_l$ | Yes | Orthogonal | 2 ($90^\circ$) | $(1 - p_c/2) / 2$ |
| Different shells | No | None (concentric) | 0 | $1$ |

**Stage C: Coupling Admittance (from Universal Operators).**

At atomic scales, $r \sim a_0 \gg l_{\text{node}} = d_{\text{sat}}$. The strain amplitude is $A = d_{\text{sat}}/r \approx \alpha/(2\pi) \approx 10^{-3}$ — deep in Regime I (linear). Op4 reduces to pure Coulomb:

$$
U(r) = -\frac{K}{r}\,(T^2 - \Gamma^2) \xrightarrow[\Gamma \to 0]{A \ll 1} -\frac{K}{r}
$$

*Type 1: Same-shell Hopf link (Op4 + Op2).* Two flux rings on the same orbit form a Hopf link. At antipodal separation $r = 2R_i$:

$$
k_{\text{Hopf}} = \frac{2}{Z}\left(1 - \frac{p_c}{2}\right), \qquad y_{\text{Hopf}} = \frac{k_{\text{Hopf}}}{Z_{LC,i}}
$$

*Type 2: Same-shell orthogonal (Op4 + Op2, $90^\circ$).* Two flux rings in different $m_l$ orbitals:

$$
k_\perp = k_{\text{Hopf}} \times \frac{1}{\sqrt{2}}, \qquad y_\perp = \frac{k_\perp}{Z_{LC,i}}
$$

*Type 3: Cross-shell concentric rings (Op4 only, no Op2).* The orbit-averaged Op4 potential between two charges on concentric circular orbits:

$$
\langle V_{ab} \rangle = \frac{2\alpha\hbar c}{\pi R_b}\, K\!\left(\frac{R_a}{R_b}\right)
$$

where $K(m)$ is the complete elliptic integral of the first kind. The coupling coefficient:

$$
k_{\text{cross}} = \frac{\langle V_{ab} \rangle}{\sqrt{E_{0,a} \times E_{0,b}}}
$$

**Stage D: Y-Matrix Assembly (Axiom 1, Kirchhoff).** Each electron is a node on the LC lattice. KCL at node $i$:

$$
Y_{ii} = \frac{1}{Z_{LC,i}} + \sum_{j \neq i} y_{ij} \qquad Y_{ij} = -y_{ij}
$$

This is Kirchhoff's current law on the discrete LC lattice (Axiom 1), with Op4 providing the pairwise admittances. No wavefunctions, no Hamiltonian matrix.

**Stage E: Hierarchical Mode Analysis.** The energy extraction follows a two-level hierarchy: **(E1)** resolve same-shell coupling within each shell, then **(E2)** resolve cross-shell coupling between the composite shell oscillators.

---
