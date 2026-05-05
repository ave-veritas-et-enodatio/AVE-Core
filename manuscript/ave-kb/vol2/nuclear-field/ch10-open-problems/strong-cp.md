[↑ Ch. 10: Three Open Problems from Lattice Topology](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [gfs4j8]
-->

## The Strong CP Problem

### The Problem

The QCD Lagrangian contains a CP-violating term:

$$
\mathcal{L}_\theta = \frac{\theta\, g^2}{32\pi^2}\, F^a_{\mu\nu} \tilde{F}^{a,\mu\nu}
$$

Any $\theta \ne 0$ gives the neutron an electric dipole moment $d_n \propto \theta$. The experimental bound $|d_n| < 10^{-26}$ e$\cdot$cm implies $|\theta| < 10^{-10}$.

**Why is $\theta$ so small?** Standard QCD allows any $\theta \in [0, 2\pi)$. The Peccei-Quinn solution posits a new symmetry and predicts the axion --- a particle not yet observed.

### AVE Resolution: Topological Quantization

**Theorem (Strong CP):** On the AVE lattice, the vacuum angle $\theta = 0$ exactly. No axion is needed.

**Proof.**

1. The AVE vacuum is the *unique* ground state with $\mathbf{E}_n = \mathbf{B}_n = 0$ for all lattice nodes $n$. This state has zero topological charge: $Q_{top} = 0$.
2. The vacuum angle $\theta$ parameterizes superpositions of topologically distinct vacua. In QCD, these are the $|\nu\rangle$ states related by large gauge transformations.
3. In AVE, the gauge structure emerges from $(2,q)$ torus knots (Section [Section Removed]). Each torus knot has quantized phase winding $\Phi = q\pi$.
4. A transition between topologically distinct vacua requires creating a topological defect, which costs energy $E \ge \Delta > 0$ (the mass gap).
5. Therefore, the vacuum cannot tunnel between $\theta$-sectors: the barrier is the mass gap itself. The ground state is $|\theta = 0\rangle$ with probability 1. $\square$

### Comparison with Peccei-Quinn

| **Feature** | **Peccei-Quinn** | **AVE** |
|---|---|---|
| Mechanism | New U(1)$_{PQ}$ symmetry | Unique vacuum topology |
| New particle | Axion (unobserved) | None |
| $\theta$ | Dynamically relaxed to 0 | Exactly 0 (ground state) |
| Free parameters | $f_a$ (axion scale) | Zero |

---
