[↑ Ch.4 Experimental Audit](../index.md)
<!-- leaf: verbatim -->
<!-- status: pending-autotune -->

# Quantitative Results

| **Model** | **$\gamma$** | **Calibration** | **FFN Pruned** | **Throughput $\Delta$** | **Quality** |
|---|---|---|---|---|---|
| Llama 3.2 3B (Q4_K_M) | 0.030 | autotune | 34--40%/layer | $+60\%$ | Correct |
| Llama 3.1 8B (Q4_K_M) | 0.001 | manual | 8--14%/layer | $+6.4\%$ | Correct |
| Qwen3.5 4B (Q4_K_M) | 0.0008 | manual | 5--10%/layer | $+4.1\%$ | Correct |
| Qwen3.5 9B (Q4_K_M) | 0.001 | manual | 6--12%/layer | $+5.8\%$ | Correct |

$\Gamma$-driven structural excision results. The Llama 3B $\gamma$ was calibrated to its maximum via `bench autotune`. The 8B, 4B, and 9B values are conservative operating points set by hand---their calibrated maxima are pending.

**Key observations:**

- The pruning fraction varies by layer depth, with early layers (passband) pruned least and deep layers (strain) pruned most. This gradient matches the expected impedance distribution of a deep transmission line.
- The $\gamma$ threshold is *not* universal---it is architecture-dependent and requires per-model calibration (Chapter 9).
- The Llama 3B autotune found $\gamma_{\max} = 0.030$, pruning 34--40% of FFN neurons with $+60\%$ throughput. The manually-set operating values for the larger models are likely far below their true maxima.
