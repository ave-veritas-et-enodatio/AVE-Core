[↑ Architecture Analysis](../index.md)

# Ch.9 Gamma Scaling

The $\gamma$ scaling law: architecture-dependent pruning thresholds, the cascade transfer function $T = (1-\gamma)^N$, the transmission budget $B$, and the 97% density constraint derived from first principles.

## Key Results

| Result | Location |
|---|---|
| $T = (1-\gamma)^N$; $\gamma_{\max} \approx B/N$ where $B = -\ln T_{\min}$ | [Cascade Transfer](cascade-transfer.md) |
| Llama 3.2 3B: $\gamma_{\max} = 0.030$, $B = 0.853$, 42.6% end-to-end retention | [Cascade Transfer](cascade-transfer.md) |
| $\gamma_{\max}$ depends on cascade depth $N$, not FFN width $n_{ff}$ (width-invariance prediction) | [Cascade Transfer](cascade-transfer.md) |
| $B$ is a single-number summary of training quality | [Transmission Budget](transmission-budget.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Gamma Thresholds](gamma-thresholds.md) | Two tiers of $\gamma$: operating vs calibrated maximum; calibration gap |
| [Autotune Results](autotune-results.md) | Llama 3.2 3B binary search convergence (pending-autotune) |
| [Cascade Transfer](cascade-transfer.md) | $T = (1-\gamma)^N$ derivation; falsifiable predictions |
| [Transmission Budget](transmission-budget.md) | $B$ as training quality metric |
| [Density Constraint](density-constraint.md) | 97% SwiGLU density from $\sigma^2 + r^2 = 1$ |

## Contents

- [Architecture-Dependent Pruning Thresholds](gamma-thresholds.md) — two tiers of $\gamma$; calibration gap
- [Autotune Results: Llama 3.2 3B](autotune-results.md) — binary search convergence table
- [Cascade Transfer Function](cascade-transfer.md) — $T = (1-\gamma)^N$; $\gamma_{\max} \approx B/N$; falsifiable predictions
- [Transmission Budget](transmission-budget.md) — $B$ as emergent training quality metric
- [97% SwiGLU Density Constraint](density-constraint.md) — first-principles derivation via sigmoid-saturation identity
