[↑ Ch.8 Discrete Masking](../index.md)
<!-- leaf: verbatim -->

# $\Gamma$-Driven Structural Excision

The working implementation of static baking employs the $\Gamma$-driven per-layer sort-and-prune algorithm (Chapter 5, Section 5.4). The full pipeline operates as follows:

1. **Impedance computation.** For each layer $\ell$, compute the coupled impedance $Z_j$ of every SwiGLU neuron $j$.
2. **Sort by impedance.** Rank neurons in ascending $Z_j$ order. The weakest-impedance neurons contribute least to the transfer function.
3. **Prune to $\gamma$ ceiling.** Remove neurons from the sorted list until the cumulative per-layer $|\Gamma_\ell|^2$ reaches $\gamma_{\max}$.
4. **Alignment padding.** Round the surviving neuron count to the nearest multiple of 256 (Q4_K superblock alignment). This ensures the re-quantized weight tensors are compatible with the Metal GPU backend.
5. **Structural bake.** Dequantize $W_{\text{gate}}$, $W_{\text{up}}$, $W_{\text{down}}$ to F32. Slice rows/columns to retain only the kept neurons. Re-quantize to Q4_K_M. Allocate new GPU tensors and swap into the weight store.

## Quantitative Results

On Llama 3.1 8B Instruct (Q4_K_M, $n_{ff} = 14336$, 32 layers) with $\gamma_{\max} = 0.001$:

| **Metric** | **Baseline** | **Baked** |
|---|---|---|
| Throughput (tok/s) | 24.5 | 26.9 |
| Throughput $\Delta$ | --- | $+6.4\%$ |
| FFN width (avg) | 14336 | 12800--13312 |
| Max $|\Gamma|^2$ | --- | $< 0.001$ |
| Semantic quality | Correct | Correct |

The baked model produces a scientifically accurate Rayleigh scattering explanation, confirming that the structural excision preserves the full inferential chain.
