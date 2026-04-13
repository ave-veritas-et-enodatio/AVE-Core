[↑ Ch.4 Experimental Audit](../index.md)
<!-- leaf: verbatim -->

# Attention Head Pruning

Extending the impedance framework to attention heads (Chapter 10) produced a complementary finding. Runtime head masking was validated at the quality level (correct output preserved), but structural head baking revealed that no head is universally dispensable (Section 10.5). The throughput contribution of head masking alone is negligible.

| **Approach** | **Throughput $\Delta$** | **Quality** | **Status** |
|---|---|---|---|
| FFN pruning only | $+6.4\%$ | Correct | Production ready |
| FFN + head runtime mask | $+6.4\%$ | Correct | No additional throughput |
| FFN + head structural bake | $+13\%$ | Degraded | Needs per-layer $n_{\text{heads}}$ |

FFN vs attention head pruning comparison on Llama 3.1 8B at $\gamma = 0.001$.
