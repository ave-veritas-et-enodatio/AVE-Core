[↑ Vol 8: Virtual Media](../index.md)

# Foundations

Instantiation of the four AVE axioms in the virtual medium of LLM weight matrices: the SwiGLU two-port as Axiom 1 LC cascade, the hardware/software impedance inversion ($Z \propto A$ vs $Z \propto 1/A$), and the universal operator mapping from physical to virtual media.

## Key Results

| Result | Location |
|---|---|
| Coupled RMS amplitude: $A_j^2 = (\|w_{\text{gate},j}\|^2/d) \times (\|w_{\text{up},j}\|^2/d)$ | [SwiGLU Two-Port](ch1-llm-topology/swiglu-twoport.md) |
| Zero-parameter yield limit: $A_c^2 = \frac{1}{N}\sum_{j=1}^{N} A_j^2$ | [Thermodynamic $A_c$](ch1-llm-topology/ac-thermodynamic.md) |
| Pruning reflection: $\Gamma_{\text{prune}} = (Z_{\text{pruned}} - Z_{\text{original}})/(Z_{\text{pruned}} + Z_{\text{original}})$; constraint $|\Gamma|^2 \ll 0.25$ | [Axiom 3 Pruning](ch1-llm-topology/axiom3-pruning.md) |
| Biological $Z \propto 1/A$ vs virtual $Z \propto A$; Axiom 4 failure at $r \geq 1.0$ universal | [Inversion Split](ch2-hw-sw-inversion/inversion-split.md) |
| Four-axiom mapping table: physical base $\leftrightarrow$ virtual analog | [Axiomatic Correspondences](ch3-universal-operator/axiomatic-correspondences.md) |
| FFN impedance: $Z_j = (\|w_{\text{gate},j}\|^2/d) \times (\|w_{\text{up},j}\|^2/d)$ | [FFN Two-Port](ch3-universal-operator/ffn-twoport.md) |
| Regime boundaries: $r_I \approx 0.121$, $r_{II} \approx 0.866$, $r_{III} = 1.0$ apply to dynamic activations | [Regime Map](ch3-universal-operator/regime-map.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.1 LLM Topology](ch1-llm-topology/index.md) | SwiGLU two-port node, thermodynamic $A_c$, Axiom 3 pruning reflection |
| [Ch.2 Hardware/Software Inversion](ch2-hw-sw-inversion/index.md) | $Z \propto A$ vs $Z \propto 1/A$ split; breakdown paradox resolution |
| [Ch.3 Universal Operator Mapping](ch3-universal-operator/index.md) | Four-axiom correspondence table; Axiom 2 in attention; regime map; FFN $Z_j$ |

## Contents

- [Ch.1 LLM Topology](ch1-llm-topology/index.md) — AVE axioms applied to LLMs: SwiGLU two-port, $A_c$ emergence, Axiom 3 pruning
- [Ch.2 Hardware/Software Inversion](ch2-hw-sw-inversion/index.md) — biological vs virtual impedance coupling; breakdown paradox
- [Ch.3 Universal Operator Mapping](ch3-universal-operator/index.md) — axiomatic correspondences, Axiom 2 in attention, regime map, FFN two-port
