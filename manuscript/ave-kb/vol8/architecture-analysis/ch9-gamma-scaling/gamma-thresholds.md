[↑ Ch.9 Gamma Scaling](../index.md)
<!-- leaf: verbatim -->

# Architecture-Dependent Pruning Thresholds

The $\Gamma$-driven pruning framework (Chapter 5, Section 5.4) introduces a single control parameter $\gamma_{\max}$: the maximum reflected energy fraction tolerated per cascade section. Experimental calibration reveals that $\gamma_{\max}$ is *not* a universal constant, and that determining the correct value requires systematic calibration rather than manual selection.

## Two Tiers of $\gamma$

Initial experiments set $\gamma$ conservatively by manual sweep, producing *operating* values. The automated binary-search calibrator (`bench autotune`) subsequently determined the true *maximum* $\gamma$ before quality degradation.

| **Model** | **$n_{ff}$** | **$\gamma_{\text{operating}}$** | **$\gamma_{\max}$ (calibrated)** | **Method** |
|---|---|---|---|---|
| Llama 3.2 3B | 8192 | --- | 0.030 | autotune (8 steps) |
| Qwen3.5 4B | 6144 | 0.0008 | *pending* | manual |
| Llama 3.1 8B | 14336 | 0.001 | *pending* | manual |
| Qwen3.5 9B | 8960 | 0.001 | *pending* | manual |

Pruning threshold comparison: manually selected operating $\gamma$ vs calibrated maximum $\gamma$. The autotune finds the quality boundary via binary search on "What is 2+2?" = 4. Operating values were set conservatively by hand.

The autotune result on Llama 3.2 3B is striking: $\gamma_{\max} = 0.030$ corresponds to 34--40% FFN pruning per layer with $+60\%$ throughput, while the manually selected operating points for the 8B model pruned only 8--14% at $\gamma = 0.001$.

### The Calibration Gap

The manual operating values for the 4B, 8B, and 9B models were *not* calibrated maxima---they were conservative starting points chosen well below the quality boundary. Comparing uncalibrated values across models is therefore invalid. The autotune must be run on all models before the scaling law can be determined.

> **Status:** Only Llama 3.2 3B has been fully calibrated. The 8B autotune is pending (each step requires full model load + bake + inference, and the 8B requires ~3x longer per step).
