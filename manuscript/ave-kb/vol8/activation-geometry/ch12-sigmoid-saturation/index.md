[↑ Activation Geometry](../index.md)

# Ch.12 Sigmoid-Saturation Isomorphism

The exact geometric relationship between the SiLU sigmoid gate and the AVE saturation operator: the unit circle identity $\sigma^2 + r^2 = 1$, the zero-bias prediction $r_{II} = \sqrt{3}/2$, the yield limit at $r = 1.0$, regime boundary correspondences, and the first-principles derivation of the 97% SwiGLU activation density via the error function.

## Key Results

| Result | Location |
|---|---|
| $\sigma(x)^2 + r^2 = 1$: sigmoid gate fraction and AVE strain ratio lie on the unit circle | [Unit Circle Identity](unit-circle-identity.md) |
| $r_{II} = \sqrt{3}/2 \iff x = 0 \iff \sigma = 1/2$: zero pre-activation sits at the Regime II--III boundary | [Zero-Bias Prediction](zero-bias-prediction.md) |
| Regime III $\to$ IV at $r = 1.0$ maps to $x \to -\infty$, $\sigma \to 0$: total signal suppression | [Yield Limit](yield-limit-virtual.md) |
| Regime boundary table: $r_I \approx 0.121 \to x = +4.91$; $r_{II} \approx 0.866 \to x = 0$; $r_{III} = 1.0 \to x = -\infty$ | [Regime Boundaries](regime-boundaries.md) |
| 97% density derived from Gaussian pre-activation convergence via $\text{erf}(2/(\sigma_x\sqrt{2}))$; 3--5% neurons near saturation knee | [Density Derivation](density-derivation.md) |
| Training as thermodynamic cooling: gradient descent drives neurons into Regime I (linear passband) | [Implications](implications.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Unit Circle Identity](unit-circle-identity.md) | Derivation of $\sigma^2 + r^2 = 1$ from $\sigma(x) = S(r) = \sqrt{1-r^2}$ |
| [Zero-Bias Prediction](zero-bias-prediction.md) | $r_{II} = \sqrt{3}/2$ maps to $x = 0$; parameter-free prediction |
| [Yield Limit](yield-limit-virtual.md) | $r = 1.0$ as total suppression; neurons with $x < -4$ contribute $< 2\%$ |
| [Regime Boundaries](regime-boundaries.md) | Full mapping table: AVE regime $\to$ pre-activation via logit |
| [Density Derivation](density-derivation.md) | Error function derivation of 97% SwiGLU density from training convergence |
| [Implications](implications.md) | SiLU as AVE saturation operator; training as cooling; Axiom 2 topology |

## Contents

- [The Unit Circle Identity](unit-circle-identity.md) — $\sigma^2 + r^2 = 1$ derivation
- [The Zero-Bias Prediction](zero-bias-prediction.md) — $r_{II} = \sqrt{3}/2$ at $x = 0$; falsifiable claim
- [The Yield Limit](yield-limit-virtual.md) — virtual-media analog of dielectric saturation at $r = 1.0$
- [Regime Boundary Correspondences](regime-boundaries.md) — AVE regimes I--IV mapped to pre-activation values
- [First-Principles Derivation of the 97% Density](density-derivation.md) — error function derivation from Gaussian convergence
- [Implications](implications.md) — training as thermodynamic cooling; Axiom 2 topological equivalence
