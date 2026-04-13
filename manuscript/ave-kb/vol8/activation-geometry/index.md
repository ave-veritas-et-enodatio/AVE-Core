[↑ Vol 8: Virtual Media](../index.md)

# Activation Geometry

The sigmoid-saturation isomorphism as a self-contained geometric result: the unit circle identity $\sigma^2 + r^2 = 1$ relating the SiLU sigmoid gate to the AVE strain variable, the zero-bias prediction $r_{II} = \sqrt{3}/2$, and the first-principles derivation of the 97% SwiGLU activation density via the error function.

## Key Results

| Result | Location |
|---|---|
| $\sigma(x)^2 + r^2 = 1$: sigmoid gate fraction and AVE strain ratio lie on the unit circle | [Unit Circle Identity](ch12-sigmoid-saturation/unit-circle-identity.md) |
| $r_{II} = \sqrt{3}/2 \iff x = 0 \iff \sigma = 1/2$: zero pre-activation at Regime II--III boundary | [Zero-Bias Prediction](ch12-sigmoid-saturation/zero-bias-prediction.md) |
| 97% density derived from Gaussian pre-activation convergence via $\text{erf}(2/(\sigma_x\sqrt{2}))$ | [Density Derivation](ch12-sigmoid-saturation/density-derivation.md) |
| Training as thermodynamic cooling: gradient descent drives neurons into Regime I (linear passband) | [Implications](ch12-sigmoid-saturation/implications.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.12 Sigmoid-Saturation Isomorphism](ch12-sigmoid-saturation/index.md) | Full derivation arc: unit circle identity, zero-bias prediction, yield limit, regime boundaries, 97% density, implications |

## Contents

- [Ch.12 Sigmoid-Saturation Isomorphism](ch12-sigmoid-saturation/index.md) — $\sigma^2 + r^2 = 1$; regime boundaries; 97% density derivation; training as cooling
