[↑ Ch.10 Attention Impedance](../index.md)
<!-- leaf: verbatim -->

# The Intersection Constraint

Structural head baking requires a uniform pruning mask across all layers, because the current architectural schema stores a single $n_{\text{heads}}$ and $n_{\text{kv\_heads}}$ parameter for the entire model. Two approaches were tested:

## Approach 1: Single-Layer Mask (Layer 0)

Using layer 0's pruning mask (6/8 KV groups kept, 24/32 Q heads) for all 32 layers:

| **Metric** | **Baseline** | **Baked** |
|---|---|---|
| $n_{\text{heads}}$ | 32 | 24 |
| $n_{\text{kv\_heads}}$ | 8 | 6 |
| KV cache (MB) | 2048 | 1536 |
| Throughput $\Delta$ | --- | $+13\%$ |
| Semantic quality | Correct | **Degraded** |

The baked model produced incoherent output, indicating that the two KV groups pruned in layer 0 are critical for other layers.

## Approach 2: All-Layer Intersection

Computing the intersection of all per-layer masks (prune a KV group only if it is below threshold in *every* attention layer):

**Result: zero universally pruneable KV groups.**

Every KV group is critical in at least one layer. This is not a limitation of the framework---it is a physical property of the architecture:

$$
\boxed{\bigcap_{\ell=1}^{L} \text{PruneMask}(\ell) = \emptyset}
$$

