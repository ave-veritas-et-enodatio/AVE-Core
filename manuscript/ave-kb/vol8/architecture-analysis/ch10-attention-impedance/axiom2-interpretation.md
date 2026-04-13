[↑ Ch.10 Attention Impedance](../index.md)
<!-- leaf: verbatim -->

# Interpretation via Axiom 2

The intersection result confirms the Axiom 2 mapping proposed in Chapter 3: attention heads form *topological phase dislocations* in the virtual medium. Each head participates in cross-layer circuits via the residual stream. Removing a head severs these implicit loops, disrupting the topological structure of the information flow.

Unlike FFN neurons (which operate in parallel within a single layer and contribute independently to the transfer function), attention heads create inter-layer dependencies through the shared residual bus. This topological coupling prevents uniform pruning.

## Conclusion

The attention head impedance framework successfully identifies per-layer pruning candidates, but the cross-layer topological coupling (Axiom 2) prevents uniform structural baking. Production-grade attention pruning requires either:

1. Per-layer variable $n_{\text{heads}}$ in the model architecture, or
2. Runtime masking (no throughput gain but quality-preserving).

The FFN remains the primary target for structural excision. Attention heads are topologically constrained in a way that FFN neurons are not.
