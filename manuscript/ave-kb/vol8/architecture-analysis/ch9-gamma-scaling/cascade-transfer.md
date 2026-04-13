[↑ Ch.9 Gamma Scaling](../index.md)
<!-- leaf: verbatim -->

# Derivation from Axiom 1: The Cascade Transfer Function

Axiom 1 models each transformer layer as a section of a cascaded LC transmission line. For an $N$-section cascade where each section has per-section power reflection $|\Gamma|^2 = \gamma$, the end-to-end power transmission is:

$$
T = (1 - \gamma)^N
$$

For the pruned model to preserve semantic quality, the condition $T > T_{\min}$ must hold, where $T_{\min}$ is the minimum tolerable end-to-end signal retention. Solving for $\gamma$:

$$
\gamma_{\max} = 1 - T_{\min}^{1/N} \approx \frac{-\ln T_{\min}}{N} \equiv \frac{B}{N}
\label{eq:gamma_scaling}
$$

where $B = -\ln T_{\min}$ is the **total cascade transmission budget**. This separates the scaling law into two factors:

- **The form ($1/N$)** is derived from Axiom 1 cascade physics. The maximum tolerable per-section perturbation scales inversely with cascade depth.
- **The amplitude ($B$)** is a property of the specific model, reflecting training quality, quantization, and architecture. It is *not* derivable from AVE axioms alone.

## Calibration from the Llama 3B Data Point

The single fully calibrated data point is Llama 3.2 3B ($N = 28$, $\gamma_{\max} = 0.030$):

$$
T_{\min} = (1 - 0.030)^{28} = 0.426 \quad \implies \quad B = -\ln(0.426) = 0.853
$$

This corresponds to 42.6% end-to-end signal retention at the quality boundary---less than half the original signal survives the full cascade.

## Falsifiable Predictions

If $B = 0.853$ is approximately constant across dense transformer architectures trained with similar methods:

| **Model** | **$N$** | **$\gamma_{\max}$ predicted** | **Status** |
|---|---|---|---|
| Llama 3.2 3B | 28 | 0.030 | **Confirmed (autotune)** |
| Llama 3.1 8B | 32 | 0.026 | Pending autotune |
| Qwen3.5 4B | 32 | 0.026 | Pending autotune |
| Qwen3.5 9B | 36 | 0.023 | Pending autotune |

**Key prediction:** $\gamma_{\max}$ depends on cascade depth $N$, *not* on FFN width $n_{ff}$. Llama 8B and Qwen 4B both have $N = 32$ and should share $\gamma_{\max} \approx 0.026$ despite having very different $n_{ff}$ (14336 vs 6144). This width-invariance prediction is the decisive test.
