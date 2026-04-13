[↑ Ch.6 Universal Operators](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 as sec:universal_pairwise -->

## Section 6.4: The Universal Pairwise Potential

The pairwise interaction between two nodes at separation $r$ is constructed by composing Operators 1--3:

> **[Resultbox]** *Universal Pairwise Potential ($U$)*
>
> <!-- eq:universal_pairwise -->
>
> $$
> U(r) = -\frac{K}{r}\bigl(T^2 - \Gamma^2\bigr), \qquad
> \Gamma(r) = \frac{Z(r) - Z_0}{Z(r) + Z_0}, \qquad
> Z(r) = \frac{Z_0}{\bigl(1 - (d_{sat}/r)^2\bigr)^{1/4}}
> $$

The three regime behaviours emerge automatically:

| **Regime** | **$r$ range** | **$\Gamma$** | **Physics** |
|---|---|---|---|
| I (Linear) | $r \gg d_{sat}$ | $\approx 0$ | Coulomb / gravity |
| II (Nonlinear) | $r \sim d_{sat}$ | $0 < \Gamma < 1$ | Nuclear / H-bond |
| III (Saturated) | $r \leq d_{sat}$ | $\to 1$ | Pauli wall |

Code path: `universal_operators.universal_pairwise_energy(r, K, d_sat)`. A JIT-compiled variant (`universal_pairwise_energy_jax`) is provided for $O(N^2)$ pairwise cost functions where the energy matrix must be evaluated at every optimiser step. The JAX variant replaces runtime duck-typing dispatch with static branching to satisfy `@jit` tracing requirements; the numerical output is identical.

---
