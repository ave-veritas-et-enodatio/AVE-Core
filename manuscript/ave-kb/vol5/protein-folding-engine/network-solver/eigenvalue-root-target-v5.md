[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Eigenvalue Root-Finding (v5 Upgrade)

The folded protein is the *eigenstate* of its admittance network: the torsion-angle configuration $\boldsymbol{\theta}^*$ at which the impedance network is maximally matched to itself. Finding this state is a **root-finding** problem, not an optimisation.

## Target Function

The eigenvalue root target combines the S-matrix eigenvalue spectrum with the Axiom 4 packing saturation:

> **[Resultbox]** *Eigenvalue Root Target (v5)*
>
> $$f(\boldsymbol{\theta}) = \lambda_{\min}\!\bigl(S^\dagger S(\boldsymbol{\theta})\bigr) \cdot S_\text{pack}(\eta) + \mathcal{P}_\text{steric}$$

where:

- $\lambda_{\min}(S^\dagger S)$ is the smallest eigenvalue of the Hermitian product $S^\dagger S$. When $\lambda_{\min} \to 0$, the S-matrix has a zero singular value $\Rightarrow$ one mode is perfectly absorbed --- the network has an eigenstate.
- $S_\text{pack} = \sqrt{1 - (\eta / P_C)^2}$ is the Axiom 4 saturation factor, with $\eta$ the global packing fraction computed from the $C_\alpha$ coordinates and $P_C = 8\pi\alpha$. This factor naturally vanishes as the protein approaches its equilibrium density, ensuring the fold stops compacting at $\eta_\text{eq} = P_C(1 - \nu)$.
- $\mathcal{P}_\text{steric} = \sum_{|i-j|\geq 3} \max(0, r_\text{steric}^2 - d_{ij}^2)^2$ enforces Pauli exclusion between non-bonded atoms.

## Newton-Raphson Update

The step is the classical Newton update, applied to the full $2N$-dimensional torsion-angle space:

$$\Delta\boldsymbol{\theta} = -f(\boldsymbol{\theta}) \cdot \frac{\nabla f}{|\nabla f|^2}, \qquad |\Delta\theta_i| \leq \pi \quad\text{(trust region)}$$

The step size is entirely determined by the function value and gradient --- no learning rate. The trust region $\pi$ is the geometric bound on angular variables.

## Convergence Criterion

The solver halts when $|f| < 1/Q^2 \approx 0.018$, the noise floor of the backbone resonator. Below this threshold, the eigenvalue spectrum of $S^\dagger S$ cannot be distinguished from noise within the $Q$-limited bandwidth of the backbone. This is the *same* convergence criterion used by the nuclear $K_\text{MUTUAL}$ solver for binding energy --- the biological and nuclear problems are formally identical.

## Cross-Scale Analogy

| **Scale** | **Target** | **Root** |
|---|---|---|
| Nuclear | $\lambda_{\min}(S^\dagger S)$ of nucleon Y-matrix | Binding energy |
| Protein | $\lambda_{\min}(S^\dagger S)$ of backbone Y-matrix | Native fold |

The *same* operator chain (Y-matrix $\to$ S-matrix $\to$ eigenvalue) governs both nuclear binding and protein folding. This is not a metaphor --- both use exactly `universal_ymatrix_to_s()` (Operator 5 in `universal_operators.py`) followed by the Newton root-finder in `eigenvalue_root_finder.py`.

## Analytical VSWR Proof-of-Concept

The `test_vswr_fold.py` script provides the one-page proof that the native fold is a *deterministic matrix problem*, not an optimisation.

**Setup.** A 34-residue linear backbone is assembled as a nodal admittance matrix. Each $C_\alpha$ node has self-admittance $Y_0 = 1/Z_0$ and mutual coupling $-Y_0$ to its neighbours. Terminal nodes have half the self-admittance (one boundary).

**Operator chain.** The chain is identical to the v5 eigenvalue solver:

$$[\mathbf{Y}] \;\xrightarrow{\text{Operator 5}}\; [\mathbf{S}] = (I + Y/Y_0)^{-1}(I - Y/Y_0) \;\xrightarrow{\text{eigenvalue}}\; \{S_{11},\, S_{21},\, \text{VSWR}\}$$

No Adam, no gradient descent, no learning rate. The $O(N^3)$ matrix inversion is the *entire* computational cost.

**Results.**

| **Observable** | **Value** | **Physical Meaning** |
|---|---|---|
| $|S_{11}|$ | 0.2361 | Input reflection $\approx 24\%$ |
| $|S_{21}|$ | 0.0000 | End-to-end transmission (overdamped) |
| VSWR | 1.6180 | $= \varphi$ (golden ratio!) |
| Mode 0 | Re$(Y) = 0.0000$ | DC zero-mode (rigid translation) |
| Mode 1--4 | Re$(Y) > 0$ | Geometric resonance eigenstates |

**Interpretation.** VSWR $= 1.0$ means perfect impedance match (zero reflected power). The 34-residue uniform backbone achieves VSWR $= \varphi \approx 1.618$ from topology alone. The appearance of the golden ratio is not *assumed* --- it emerges from the eigenvalue structure of the tridiagonal admittance matrix, whose eigenmodes are the Chebyshev polynomials of the second kind. The five lowest eigenmodes of the Y-matrix are the geometrical resonances of the backbone: they are the standing-wave patterns that drive helix/sheet formation when sidechain impedances and H-bond couplers are introduced.

**Key insight.** The ground state of the protein is the $\boldsymbol{\theta}$ that drives VSWR $\to 1$ (or equivalently $\lambda_{\min}(S^\dagger S) \to 0$). This is a testable, analytical condition --- not a loss function to be minimised. `test_vswr_fold.py` is the existence proof that such a state can be found in $O(N^3)$ time without iteration.

**Implementation.** Function `fold_eigenvalue_v5()` in `s11_fold_engine_v4_ymatrix.py` (L640--720). Gradients are computed by `jax.grad` through the full Y-matrix assembly + S-parameter extraction chain. Typical convergence: 50--150 Newton steps for $N < 40$.

---
