[↑ Axioms and Lattice](../index.md)
<!-- claim-quality (subtree): 219e8j, 3kzmt9, 5xon03, 9s9apq, dfaiwj -->

# Ch.1: The Four Fundamental Axioms and Network Architecture

The four fundamental axioms define the vacuum as an electromagnetic LC resonant network ($\mathcal{M}_A$) with a topo-kinematic charge-length isomorphism, an effective hardware action principle, and non-linear dielectric saturation bounded by the fine-structure constant. Three emergent hardware constraints ($\ell_{node}$, $\alpha$, $G$) are shown to be derivable from topology, reducing the framework to zero free parameters.

## Key Results

| Result | Statement |
|---|---|
| Topological Conversion Constant | $\xi_{topo} \equiv e / \ell_{node}$ [C/m] |
| Macroscopic Hardware Action | $\mathcal{L}_{node} = \frac{1}{2}\epsilon_0 \lvert\partial_t \mathbf{A}_n\rvert^2 - \frac{1}{2\mu_0} \lvert\nabla \times \mathbf{A}_n\rvert^2$ |
| Non-Linear Dielectric Saturation | $C_{eff}(\Delta\phi) = C_0 / \sqrt{1 - (\Delta\phi/\alpha)^2}$ |
| True Gravitational Coupling | $G_{true} = \hbar c / m_e^2$ |
| True Planck Length | $\ell_{P,true} = \sqrt{\hbar G_{true}/c^3} \equiv \hbar/(m_e c) = \ell_{node}$ |
| Trace-Reversal Packing Fraction | $p^* = (10z_0 - 12)/(z_0(z_0+2)) = 8\pi\alpha$ |
| Edge Strain Update | $I_{new} = I_{old} + (\Delta t / L)(V_A - V_B)$ |
| Node Displacement Update | $V_{new} = V_{old} + (\Delta t / C)(\sum I_{in} - \sum I_{out})$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Calibration and Cutoff Scales](./calibration-cutoff-scales.md) | Three canonical hardware scales: $\ell_{node}$, $\alpha$, $G$ (all derived from first principles; $\alpha$ closure in Ch.8 Golden Torus) |
| [Axiom Definitions](./axiom-definitions.md) | The four fundamental axioms with resultboxes for $\xi_{topo}$, $\mathcal{L}_{node}$, $C_{eff}$ |
| [LC Condensate Vacuum](./lc-condensate-vacuum.md) | Planck scale artifact, true gravitational coupling, vacuum porosity ratio |
| [Zero-Parameter Universe](./zero-parameter-universe.md) | Deriving $\alpha$ via Golden Torus S₁₁-min (Ch.8), $G$ via thermodynamic equilibrium, $\ell_{node}$ via scale invariance |
| [Kirchhoff Network Method](./kirchhoff-network-method.md) | Discrete Kirchhoff solver, edge/node update equations, master constants pipeline |
| [Lattice Structure (stub)](./lattice-structure.md) | Redirect to Kirchhoff network method |
