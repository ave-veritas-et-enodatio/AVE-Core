[↑ Ch.11 MoE Impedance](../index.md)
<!-- leaf: verbatim -->

# From Static to Dynamic Impedance

The preceding chapters analyzed dense transformer architectures, where every neuron and every attention head participates in every forward pass. The impedance of the network is *static*: the weight matrices are frozen, and the same computational graph executes for every input token.

Mixture of Experts (MoE) architectures introduce a fundamentally different paradigm: *dynamic impedance selection*. Each MoE layer contains $N_{\text{expert}}$ parallel expert sub-networks, but only $K$ of them activate per token (typically $K = 2$ or $K = 4$). A learned router selects which experts to activate based on the input.
