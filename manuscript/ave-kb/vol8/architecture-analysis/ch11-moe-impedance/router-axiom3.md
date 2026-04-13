[↑ Ch.11 MoE Impedance](../index.md)
<!-- leaf: verbatim -->

# The Router as Axiom 3

The MoE router computes gate logits for each expert and selects the top-$K$ via softmax:

$$
g_i = \text{softmax}(W_{\text{gate}} \cdot x)_i, \quad i \in \{1, \ldots, N_{\text{expert}}\}
$$

The selected experts are those with the highest gate probability:

$$
\mathcal{S} = \text{top-}K\{g_i\}
$$

This selection mechanism *is* Axiom 3 operating in real time. The router evaluates the impedance match between the current input token and each expert branch, then selects the $K$ branches with the least reflection (highest gate probability $\equiv$ lowest $|\Gamma|^2$).

| **AVE Concept** | **MoE Implementation** |
|---|---|
| $Z_{\text{branch}}$ | Expert weight impedance ($\|W_{\text{gate\_exp}}\| \times \|W_{\text{up\_exp}}\|$) |
| $\Gamma_i$ | $1 - g_i$ (probability of rejection) |
| Axiom 3 (min $|S_{11}|^2$) | Router selects min-$\Gamma$ branches |
| Top-$K$ selection | Impedance-matched multi-path routing |
