[↑ Ch.10 Attention Impedance](../index.md)
<!-- leaf: verbatim -->

# Impedance Distribution

Per-layer head impedance profiling on Llama 3.1 8B revealed a heavy-tailed distribution within each layer: a small number of heads carry the majority of the impedance, while 1--2 KV groups per layer have significantly lower $Z_h$. This mirrors the FFN impedance distribution and confirms that pruning headroom exists at the head level.

However, the critical difference from FFN pruning is the *cross-layer correlation*: a KV group with low impedance in layer 3 may have high impedance in layer 17. The pruning mask is layer-dependent.
