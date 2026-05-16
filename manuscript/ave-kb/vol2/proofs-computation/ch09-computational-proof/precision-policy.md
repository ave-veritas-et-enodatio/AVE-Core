[↑ Ch. 9: Computational Proof and Anomaly Catalog](./index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-ak97cb]
-->

## Numerical Precision and Dimensional Coordination

The physics engine enforces a rigorous numerical precision policy to ensure that computational artefacts never masquerade as physical predictions.

### Floating-Point Arithmetic

All engine modules use IEEE 754 double precision (`float64`), providing approximately 15 significant decimal digits ($\varepsilon_{mach} \approx 2.2 \times 10^{-16}$). No single-precision (`float32`) arrays are used anywhere in the framework. This is critical because the AVE derivation chain spans 39 orders of magnitude: a constant computed at the lattice pitch ($l_{node} \sim 10^{-13}$ m) participates in predictions at the Hubble radius ($R_H \sim 10^{26}$ m), requiring at least 12 significant digits to remain unambiguous.

### Guard Constant Hierarchy

Three standardised guard constants prevent numerical singularities throughout the engine. All modules import these from `constants.py` rather than defining ad-hoc magic numbers:

| Constant | Value | Usage |
|---|---|---|
| `EPS_NUMERICAL` | $10^{-12}$ | Impedance ratios, reflection coefficients, normalisation denominators. Ensures $Z/(Z + \varepsilon) \approx 1$ within float64 precision. |
| `EPS_CLIP` | $10^{-15}$ | Saturation operator clip ceiling: $\sqrt{1 - x^2}$ with $x = 1 - \varepsilon$. Prevents $\sqrt{<0}$ while keeping $S(A_{yield}) \approx 0$ to float64 resolution. |
| `EPS_DIVZERO` | $10^{-30}$ | Hard division-by-zero floor for denominators that can reach exactly zero (DC impedance, $\tanh$ at origin). Sub-float64 so it never affects physical results. |

These constants are *dimensionless* ratios applied to already-normalised quantities. They carry no units and encode no physics.

### Dimensional Analysis Chain

Every derived constant in the engine is expressed algebraically from the three calibration inputs ($m_e$, $\alpha$, $G$) plus exact SI definitions ($c_0$, $\mu_0$, $\varepsilon_0$, $\hbar$, $e$). The dimensional algebra is as follows:

> **[Resultbox]** *Dimensional Traceability*
>
> $$
> \begin{align}
> \ell_{node} &= \hbar / (m_e c_0) \quad [\text{m}] \quad \text{(Input 1: spatial cutoff)} \\
> \alpha &= e^2 / (4\pi\varepsilon_0 \hbar c_0) \quad [\text{---}] \quad \text{(Input 2: dielectric bound)} \\
> G &= \hbar c_0 / (7 \xi_M m_e^2) \quad [\text{m}^3/\text{kg}\cdot\text{s}^2] \quad \text{(Input 3: Machian boundary)}
> \end{align}
> $$

Every subsequent constant (Bohr radius, Rydberg energy, string tension, snap voltage, yield field, proton mass, etc.) is an explicit algebraic combination of these three with no hidden fitting.

### Precision Budget

| Constant Class | Source | Relative Uncertainty |
|---|---|---|
| SI exact ($c_0$, $\mu_0$, $e$, $\hbar$, $k_B$) | 2019 SI redefinition | 0 (exact by definition) |
| $m_e$ (CODATA 2018) | Penning trap | $3.0 \times 10^{-10}$ |
| $\alpha$ (CODATA 2018) | Electron $g$-factor | $1.5 \times 10^{-10}$ |
| $G$ (CODATA 2018) | Torsion balance | $2.2 \times 10^{-5}$ |
| $m_p$ (CODATA 2018) | Penning trap | $3.1 \times 10^{-10}$ |

The gravitational constant $G$ is the least precise input at $2.2 \times 10^{-5}$ (22 ppm). This uncertainty propagates only into cosmological and gravitational predictions (MOND $a_0$, Machian hierarchy $\xi_M$). All electromagnetic, atomic, and molecular predictions are limited only by $m_e$ and $\alpha$ uncertainties below 1 ppb, which is far below the ODE solver tolerance and effectively exact.

---
