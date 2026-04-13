[↑ Architecture Analysis](../index.md)

# Ch.8 Discrete Masking

Experimental proof that only dimensional excision (static baking) is valid for the software manifold: continuous masking and binary masking both fail via impedance mismatch, while static baking preserves $\Gamma \approx 0$. The neuroplasticity boundary distinguishes dynamic activation physics from static weight filter design.

## Key Results

| Result | Location |
|---|---|
| Continuous $S(r)$ masking: $|\Gamma|^2 > 0.83$ in top layers; catastrophic reflection | [Masking Failures](masking-failures.md) |
| Binary masking: 40% zero entries destabilize $W_{\text{down}}$ output distribution | [Masking Failures](masking-failures.md) |
| Static baking: $\Gamma \approx 0$; $+6.4\%$ throughput on 8B with preserved quality | [Gamma Excision](gamma-excision.md) |
| $Z_{\text{eff}} = Z_0/\sqrt{S(r)}$; peak $\approx 3600\,\Omega$ ($10\times$ baseline) at buckling | [Z_eff Telemetry](zeff-telemetry.md) |
| Frozen weights = static impedance; $S(r)$ applies to activations, not weights | [Neuroplasticity](neuroplasticity.md) |
| Software manifold $\implies$ excision (reshape) $\neq$ attenuation (mask) | [Neuroplasticity](neuroplasticity.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Masking Protocol](masking-protocol.md) | Motivation, experimental A/B protocol on Qwen 4B |
| [Z_eff Telemetry](zeff-telemetry.md) | Axiom 1 impedance telemetry; $10\times$ spike observation |
| [Masking Failures](masking-failures.md) | Why continuous and binary masking both fail |
| [Static Baking](static-baking.md) | Why simultaneous row/column removal preserves $\Gamma \approx 0$ |
| [Gamma Excision](gamma-excision.md) | Full pipeline: impedance compute, sort, prune, align, bake |
| [Neuroplasticity](neuroplasticity.md) | Category error; correct AVE mapping; static filter framework |

## Contents

- [Motivation and Experimental Protocol](masking-protocol.md) — continuous vs binary masking hypothesis; A/B test setup
- [Axiom 1 $Z_{eff}$ Telemetry](zeff-telemetry.md) — $10\times$ impedance spike at buckling threshold
- [Why Masking Fails](masking-failures.md) — continuous and binary failure analysis (grouped)
- [Why Static Baking Succeeds](static-baking.md) — dimensional excision preserves impedance ratio
- [$\Gamma$-Driven Structural Excision](gamma-excision.md) — full baking pipeline and quantitative results
- [The Neuroplasticity Boundary](neuroplasticity.md) — category error; static filter framework; ABCD cascade
