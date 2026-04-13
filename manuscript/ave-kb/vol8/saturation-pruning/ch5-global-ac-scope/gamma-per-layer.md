[↑ Ch.5 Global $A_c$ Scope](../index.md)
<!-- leaf: verbatim -->

# Evolution to $\Gamma$-Driven Per-Layer Pruning

While the global $A_c$ resolved the per-layer vs global collapse paradox, it introduced a second-order problem: layers with uniformly high impedance (deep layers) were stripped of >60% of their neurons, exceeding acceptable reflection limits.

The resolution came from Axiom 3 directly: instead of imposing a fixed $r \ge 1.0$ threshold, the pruning criterion was reformulated as a per-layer reflection budget. For each layer $\ell$:

1. Sort neurons by ascending coupled impedance $Z_j$.
2. Starting from the weakest neuron, accumulate the cumulative reflection:

$$
|\Gamma_\ell|^2 = \left(\frac{ \sum_{j \in \text{kept}} Z_j - \sum_{j=1}^{N_\ell} Z_j }{ \sum_{j \in \text{kept}} Z_j + \sum_{j=1}^{N_\ell} Z_j }\right)^2
$$

3. Prune neurons until $|\Gamma_\ell|^2$ reaches the threshold $\gamma_{\max}$.

This formulation has two critical advantages:

- It is self-calibrating: layers with uniform impedance (low variance) are barely pruned, while layers with heavy-tailed distributions (high variance) lose their weakest neurons.
- The single parameter $\gamma_{\max}$ has a direct physical interpretation: the maximum reflected energy fraction tolerated per cascade section.

## Conclusion

The yield threshold evolved through three generations:

1. **Per-layer $A_c$**: collapsed all models (Chapter 5).
2. **Global $A_c$ with $r \ge 1.0$**: restored reasoning but over-pruned deep layers.
3. **$\Gamma$-driven per-layer sort-and-prune**: the axiomatically correct solution. Directly implements Axiom 3 (minimize $|S_{11}|^2$) per cascade section.

The $\Gamma$-driven formulation produced the first production-quality pruned inference, achieving $+6.4\%$ throughput on Llama 3.1 8B with preserved semantic accuracy (Chapter 4).
