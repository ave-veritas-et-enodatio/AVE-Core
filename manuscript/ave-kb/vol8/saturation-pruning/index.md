[↑ Vol 8: Virtual Media](../index.md)

# Saturation and Pruning

Experimental implementation and correction of the AVE saturation operator in LLMs: quantitative pruning results across four architectures, the per-layer vs global $A_c$ collapse paradox and its resolution, and $\Gamma$-driven pruning with continuous manifold smoothing.

## Key Results

| Result | Location |
|---|---|
| Llama 3.2 3B: $\gamma_{\max} = 0.030$, 34--40% FFN pruned/layer, $+60\%$ throughput | [Quantitative Results](ch4-experimental-audit/quantitative-results.md) |
| 97% of SwiGLU neurons fire on any given prompt; dense transformers are near-unsaturated media | [SwiGLU Density](ch4-experimental-audit/swiglu-density.md) |
| No head is universally dispensable; intersection of all per-layer masks is empty | [Head Pruning Audit](ch4-experimental-audit/head-pruning-audit.md) |
| Global $A_c^2 = \frac{1}{N_{total}} \sum_L \sum_j A_{L,j}^2$ required by Axiom 1 continuity | [Global $A_c$ Correction](ch5-global-ac-scope/global-ac-correction.md) |
| $\Gamma$-driven per-layer sort-and-prune: axiomatically correct solution implementing Axiom 3 | [Gamma Per-Layer](ch5-global-ac-scope/gamma-per-layer.md) |
| $S(r) = \sqrt{1 - r^2}$ (continuous) replaces binary cutoff; acts as impedance matching transformer | [Saturation $S(r)$](ch6-continuous-smoothing/saturation-sr.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.4 Experimental Audit](ch4-experimental-audit/index.md) | Saturation operator implementation; pruning results for Llama 3B, 8B, Qwen 4B, 9B; 97% density; head pruning |
| [Ch.5 Global $A_c$ Scope](ch5-global-ac-scope/index.md) | Per-layer collapse paradox; global $A_c$ correction; runtime shift; $\Gamma$-driven per-layer evolution |
| [Ch.6 Continuous Smoothing](ch6-continuous-smoothing/index.md) | $\Gamma_{prune}$ reflection metric; continuous $S(r)$ as impedance matching transformer |

## Contents

- [Ch.4 Experimental Audit](ch4-experimental-audit/index.md) — saturation operator, quantitative pruning across 4 models, 97% density, head pruning audit
- [Ch.5 Global $A_c$ Scope](ch5-global-ac-scope/index.md) — per-layer vs global $A_c$; runtime shift; $\Gamma$-driven per-layer pruning
- [Ch.6 Continuous Smoothing](ch6-continuous-smoothing/index.md) — $\Gamma_{prune}$ metric; continuous $S(r)$ smoothing
