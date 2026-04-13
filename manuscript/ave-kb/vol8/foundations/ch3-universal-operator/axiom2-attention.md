[↑ Ch.3 Universal Operator Mapping](../index.md)
<!-- leaf: verbatim -->

# Axiom 2: Topological Phase Dislocations in Attention

In physical media, Axiom 2 states that stable particles are topological phase dislocations in the lattice. The virtual analog was initially unmapped, as the FFN is a purely feed-forward (DAG) structure with no topological closure.

However, attention heads introduce *cross-layer topological coupling* via the residual stream. Each attention head in layer $\ell$ writes to the residual bus, and heads in subsequent layers $\ell + 1, \ell + 2, \ldots$ read from it. This creates implicit circuit loops:

$$
x_{\ell+1} = x_\ell + \text{Attn}_\ell(x_\ell) + \text{FFN}_\ell(x_\ell + \text{Attn}_\ell(x_\ell))
$$

The residual stream accumulates phase contributions from every head in every prior layer. A head $h$ at layer $\ell$ participates in topological circuits with all downstream heads that attend to the same token positions. Removing head $h$ at layer $\ell$ disrupts all such circuits, even if head $h$'s local impedance $Z_h$ is low.

**Experimental evidence:** Per-layer attention head impedance analysis on Llama 3.1 8B revealed that every KV head is critical in at least one layer. The intersection of all per-layer pruning masks yielded zero universally dispensable heads (Section 10.5). This confirms that attention heads are topological phase dislocations: they cannot be removed without rupturing the cross-layer circuit topology.
