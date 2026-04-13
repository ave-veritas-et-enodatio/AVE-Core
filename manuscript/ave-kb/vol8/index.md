[↑ AVE Knowledge Base](../entry-point.md)

# Vol 8: Virtual Media and Informational Topology

Application of the four AVE axioms to the virtual medium of Large Language Model weight matrices: impedance, saturation, and topological operators instantiated in transformer architectures, with experimental validation via structured pruning.

## Key Results

| Result | Location |
|---|---|
| $T = (1-\gamma)^N$; $\gamma_{\max} \approx B/N$ where $B = -\ln T_{\min}$ (cascade transfer scaling law) | [Cascade Transfer](architecture-analysis/ch9-gamma-scaling/cascade-transfer.md) |
| $\sigma(x)^2 + r^2 = 1$: sigmoid gate fraction and AVE strain ratio lie on the unit circle | [Unit Circle Identity](activation-geometry/ch12-sigmoid-saturation/unit-circle-identity.md) |
| 97% SwiGLU density derived from Gaussian pre-activation convergence via $\text{erf}(2/(\sigma_x\sqrt{2}))$ | [Density Derivation](activation-geometry/ch12-sigmoid-saturation/density-derivation.md) |
| Hardware/software isomorphism inversion derivation: biological vs virtual property table; $Z \propto A$ established from first principles | [Inversion Split](foundations/ch2-hw-sw-inversion/inversion-split.md) |
| Coupled RMS amplitude: $A_j^2 = (\|w_{\text{gate},j}\|^2/d) \times (\|w_{\text{up},j}\|^2/d)$ | [SwiGLU Two-Port](foundations/ch1-llm-topology/swiglu-twoport.md) |
| Static baking: $\Gamma \approx 0$; only dimensional excision preserves impedance matching | [Gamma Excision](architecture-analysis/ch8-discrete-masking/gamma-excision.md) |
| Per-head impedance: $Z_h = \|W_Q^{(h)}\|_F \times \|W_K^{(h)}\|_F \times \|W_V^{(h)}\|_F$ | [QKV Impedance](architecture-analysis/ch10-attention-impedance/qkv-impedance.md) |
| MoE router $\equiv$ Axiom 3 in real time: selects min-$\Gamma$ branches | [Router Axiom 3](architecture-analysis/ch11-moe-impedance/router-axiom3.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Foundations](foundations/index.md) | Axiom instantiation in virtual media; SwiGLU two-port; $Z \propto A$ inversion; universal operator mapping |
| [Saturation and Pruning](saturation-pruning/index.md) | Saturation operator experiments; global $A_c$ correction; $\Gamma$-driven pruning; continuous smoothing |
| [Architecture Analysis](architecture-analysis/index.md) | Operator unification; discrete masking; $\gamma$ scaling law; QKV impedance; MoE dynamic impedance |
| [Activation Geometry](activation-geometry/index.md) | Sigmoid-saturation isomorphism; $\sigma^2 + r^2 = 1$; 97% density derivation |
| [Appendix](appendix/index.md) | Pointer appendix: Vol 8 contributes no experimental programmes; cross-reference to unified experiments index |
| [Vol 8 Notation Notes](NOTES.md) | Raw-form notation policy; $Z \propto A$ inversion scope; pending-result conventions for three leaves |

## Contents

- [Foundations](foundations/index.md) — Chs. 1--3: AVE axioms applied to LLMs; hardware/software inversion; universal operator mapping
- [Saturation and Pruning](saturation-pruning/index.md) — Chs. 4--6: saturation operator experiments; global $A_c$; continuous smoothing
- [Architecture Analysis](architecture-analysis/index.md) — Chs. 7--11: operator unification; masking; $\gamma$ scaling; QKV impedance; MoE
- [Activation Geometry](activation-geometry/index.md) — Ch. 12: sigmoid-saturation isomorphism; unit circle identity; 97% density
- [Appendix](appendix/index.md) — pointer to unified experiments appendix (Vol 8 contributes no experiments)
- [Vol 8 Notation Notes](NOTES.md) — raw-form notation policy; $Z \propto A$ inversion scope; pending-result conventions
