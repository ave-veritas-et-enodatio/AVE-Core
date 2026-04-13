[↑ Ch.10 Attention Impedance](../index.md)
<!-- leaf: verbatim -->

# Grouped-Query Attention Constraint

Modern architectures employ Grouped-Query Attention (GQA), where multiple Query heads share a single Key-Value group. In Llama 3.1 8B, $n_{\text{heads}} = 32$ Q heads are grouped into $n_{\text{kv\_heads}} = 8$ KV groups (4 Q heads per KV group).

This creates a coupling constraint: pruning one KV group removes all 4 associated Q heads. The impedance must therefore be computed at the KV-group level:

$$
Z_{\text{group},g} = \left(\sum_{q \in g} \|W_Q^{(q)}\|_F\right) \times \|W_K^{(g)}\|_F \times \|W_V^{(g)}\|_F
$$

where the sum aggregates the Q-head norms within KV group $g$.
