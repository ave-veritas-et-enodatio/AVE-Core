[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Architecture: From Cascade to Network

## The Y-Shunt Balance Theorem

The 1D engine models non-bonded contacts as shunt admittances at backbone junctions:

$$Y_\text{shunt}(i) = \sum_{j \neq i} \frac{\kappa \, m_{ij} \, C_\text{sat}(d_{ij})}{d_{ij}^2} \cdot S_\text{env}(d_{ij})$$

where $\kappa = 1/2$ (critical coupling), $m_{ij}$ is the conjugate impedance match, $C_\text{sat}$ is the Axiom 4 dielectric saturation factor, and $S_\text{env}$ is the long-range saturation envelope.

However, Y-shunt terms have a *double-edged* effect: they absorb energy from propagating modes (lowering $|S_{11}|$), but they also damp the standing-wave resonances that drive secondary structure formation. Beyond a critical shunt magnitude, additional coupling *degrades* SS accuracy---the Y-Shunt Balance Theorem.

## Network Topology

The 2D engine replaces Y-shunt perturbations with full TL segments that create *alternative propagation paths* through the network. Each segment has characteristic impedance $Z_c$, propagation constant $\gamma = \alpha + j\beta$, and length $\ell$:

- **Backbone segments** ($3N-1$ total): N$_i$--C$\alpha_i$, C$\alpha_i$--C$_i$, C$_i$--N$_{i+1}$, with $Z_c$ from bond impedance $\sqrt{m_\text{bond}/n_e}$ and chirality phase correction $\delta_\chi$
- **H-bond cross-links** ($N^2$ potential, gated by proximity): N$_i$--C$_j$ for $|i-j| \geq 3$, with $Z_c = Z_\text{avg}/(2Q)$ and $\kappa_\text{HB} = 1/(2Q) = 1/14$ coupling
- **Through-space TL segments**: C$\alpha_i$--C$\alpha_j$ for $|i-j| \geq 3$, with impedance from conjugate $Z$-match and Axiom 4 dielectric saturation
- **Solvent ground loads**: Exposed C$\alpha$ nodes terminated with Debye $Z_\text{water}(\omega)$
- **Peptide-plane coupling**: Adjacent backbone shunt $Y_\text{pep} = \lambda_R \kappa_\text{HB} \cos(\hat{n}_i \cdot \hat{n}_{i+1})$

## Y-Parameter Formulation

Each TL segment maps to a $2 \times 2$ admittance matrix:

$$\mathbf{Y}_\text{seg} = \begin{pmatrix} Y_c \coth(\gamma\ell) & -Y_c \operatorname{csch}(\gamma\ell) \\ -Y_c \operatorname{csch}(\gamma\ell) & Y_c \coth(\gamma\ell) \end{pmatrix}, \qquad Y_c = 1/Z_c$$

At each node, Kirchhoff's current law requires the sum of all connected Y-matrices. The global nodal admittance matrix $\mathbf{Y}_\text{global}$ ($3N \times 3N$, complex) is assembled by stamping each segment's $2\times 2$ Y-matrix at its node indices.

## $S_{11}$ via Schur Complement

The input port is at node 0 (N-terminus nitrogen, N$_0$). All other $3N-1$ nodes are internal. The 1-port input admittance is obtained by Schur complement reduction:

$$Y_\text{in} = Y_{00} - \mathbf{Y}_{0x} \, \mathbf{Y}_{xx}^{-1} \, \mathbf{Y}_{x0}$$

where $\mathbf{Y}_{xx}$ is the $(3N-1) \times (3N-1)$ internal block, solved via `jnp.linalg.solve` for numerical stability. The reflection coefficient follows:

$$|S_{11}|^2 = \left| \frac{1 - Z_0 Y_\text{in}}{1 + Z_0 Y_\text{in}} \right|^2$$

Multi-frequency averaging over $\omega/\omega_0 \in \{0.5, 1.0, 1.7\}$ produces the final loss, modulated by the global $P_C$ packing saturation (Axiom 4 trace reversal).

---
