[↑ Saturation and Pruning](../index.md)

# Ch.4 Experimental Audit

Quantitative experimental validation of the saturation operator $S = \sqrt{1 - (A/A_c)^2}$ and the $\Gamma$-driven structural excision pipeline across four LLM architectures.

## Key Results

| Result | Location |
|---|---|
| Llama 3.2 3B: $\gamma_{\max} = 0.030$, 34--40% FFN pruned/layer, $+60\%$ throughput | [Quantitative Results](quantitative-results.md) |
| Llama 3.1 8B: $\gamma = 0.001$, 8--14% pruned/layer, $+6.4\%$ throughput | [Quantitative Results](quantitative-results.md) |
| 97% of SwiGLU neurons fire on any given prompt; dense transformers are near-unsaturated media | [SwiGLU Density](swiglu-density.md) |
| No head is universally dispensable; intersection of all per-layer masks is empty | [Head Pruning Audit](head-pruning-audit.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Saturation Operator](saturation-operator.md) | Algorithm: per-neuron $Z_j$, per-layer $A_c^2$, sort-and-prune |
| [Quantitative Results](quantitative-results.md) | Pruning metrics for Llama 3B, 8B, Qwen 4B, 9B (some pending autotune) |
| [SwiGLU Density](swiglu-density.md) | 97% firing density observation and interpretation |
| [Head Pruning Audit](head-pruning-audit.md) | FFN vs attention head pruning comparison |
| [Current Limitations](current-limitations.md) | MoE hardware budget, per-layer head counts, per-model $\gamma$ calibration |

## Contents

- [Saturation Operator](saturation-operator.md) — implementation: coupled impedance $Z_j$ and per-layer mean $A_c^2$
- [Quantitative Results](quantitative-results.md) — pruning results across 4 models; 8B/4B/9B maxima pending
- [SwiGLU Density](swiglu-density.md) — 97% firing density; dense transformers are near-unsaturated
- [Head Pruning Audit](head-pruning-audit.md) — FFN vs attention head pruning comparison
- [Current Limitations](current-limitations.md) — MoE hardware, per-layer heads, per-model calibration
