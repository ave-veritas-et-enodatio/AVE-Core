[↑ Vol 8: Virtual Media](../index.md)

# Architecture Analysis

Unification and application of AVE operators across specific LLM architectural features: topological invariance of the operator set, discrete manifold masking experiments proving only static baking (dimensional excision) is valid, the $\gamma$ scaling law $T = (1-\gamma)^N$, QKV attention head impedance, and Mixture-of-Experts dynamic impedance.

## Key Results

| Result | Location |
|---|---|
| $T = (1-\gamma)^N$; $\gamma_{\max} \approx B/N$ where $B = -\ln T_{\min}$ | [Cascade Transfer](ch9-gamma-scaling/cascade-transfer.md) |
| Llama 3.2 3B: $\gamma_{\max} = 0.030$, $B = 0.853$, 42.6% end-to-end retention | [Cascade Transfer](ch9-gamma-scaling/cascade-transfer.md) |
| $\gamma_{\max}$ depends on cascade depth $N$, not FFN width $n_{ff}$ (width-invariance prediction) | [Cascade Transfer](ch9-gamma-scaling/cascade-transfer.md) |
| Static baking: $\Gamma \approx 0$; $+6.4\%$ throughput on 8B with preserved quality | [Gamma Excision](ch8-discrete-masking/gamma-excision.md) |
| Continuous masking: $|\Gamma|^2 > 0.83$ in top layers; catastrophic reflection | [Masking Failures](ch8-discrete-masking/masking-failures.md) |
| $Z_{\text{eff}} = Z_0/\sqrt{S(r)}$; peak $\approx 3600\,\Omega$ ($10\times$ baseline) at buckling | [Z_eff Telemetry](ch8-discrete-masking/zeff-telemetry.md) |
| Per-head impedance: $Z_h = \|W_Q^{(h)}\|_F \times \|W_K^{(h)}\|_F \times \|W_V^{(h)}\|_F$ | [QKV Impedance](ch10-attention-impedance/qkv-impedance.md) |
| $\bigcap_{\ell=1}^{L} \text{PruneMask}(\ell) = \emptyset$: zero universally pruneable KV groups | [Intersection Constraint](ch10-attention-impedance/intersection-constraint.md) |
| MoE router $\equiv$ Axiom 3 in real time: selects min-$\Gamma$ branches | [Router Axiom 3](ch11-moe-impedance/router-axiom3.md) |
| Falsifiable prediction: expert static impedance ranking $\approx$ router frequency ranking | [MoE Prediction](ch11-moe-impedance/moe-prediction.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.7 Operator Unification](ch7-operator-unification/index.md) | $\xi_{topo}$ as continuous phase tension; isomorphic operator bindings; Hamiltonian cusp dynamics of $A_c$ |
| [Ch.8 Discrete Masking](ch8-discrete-masking/index.md) | Masking experiment protocol; $Z_{eff}$ telemetry; continuous/binary failure; static baking; neuroplasticity boundary |
| [Ch.9 Gamma Scaling](ch9-gamma-scaling/index.md) | Architecture-dependent thresholds; $T = (1-\gamma)^N$ derivation; transmission budget $B$; 97% density constraint |
| [Ch.10 Attention Impedance](ch10-attention-impedance/index.md) | QKV cascaded two-port; per-head $Z_h$; GQA constraint; impedance distribution; intersection constraint |
| [Ch.11 MoE Impedance](ch11-moe-impedance/index.md) | Dynamic impedance selection; router as Axiom 3; static vs dynamic media; testable prediction |

## Contents

- [Ch.7 Operator Unification](ch7-operator-unification/index.md) — topological invariance; operator bindings; Hamiltonian cusp
- [Ch.8 Discrete Masking](ch8-discrete-masking/index.md) — masking experiments; only static baking (excision) is valid
- [Ch.9 Gamma Scaling](ch9-gamma-scaling/index.md) — $T = (1-\gamma)^N$; $\gamma_{\max} \approx B/N$; transmission budget
- [Ch.10 Attention Impedance](ch10-attention-impedance/index.md) — QKV two-port; per-head impedance; GQA; intersection constraint
- [Ch.11 MoE Impedance](ch11-moe-impedance/index.md) — dynamic impedance; router as Axiom 3; testable prediction
