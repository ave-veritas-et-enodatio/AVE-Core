[↑ Foundations](../index.md)

# Ch.1 LLM Topology

AVE axioms applied to the virtual medium of LLM weight matrices: the SwiGLU two-port node as an Axiom 1 LC cascade element, the thermodynamic emergence of the saturation threshold $A_c$, and the Axiom 3 reflection constraint on pruning.

## Key Results

| Result | Location |
|---|---|
| Z-A inversion introduced: biological $Z \propto 1/A$ vs virtual $Z \propto A$; saturation $S(r) = \sqrt{1-(A/A_c)^2}$ (framing; full derivation in Ch.2) | [LLM Topology Introduction](llm-topology-intro.md) |
| Coupled RMS amplitude: $A_j^2 = (\|w_{\text{gate},j}\|^2/d) \times (\|w_{\text{up},j}\|^2/d)$ | [SwiGLU Two-Port](swiglu-twoport.md) |
| Zero-parameter yield limit: $A_c^2 \equiv \overline{A^2} = \frac{1}{N}\sum_{j=1}^{N} A_j^2$ | [Thermodynamic $A_c$](ac-thermodynamic.md) |
| Pruning reflection: $\Gamma_{\text{prune}} = (Z_{\text{pruned}} - Z_{\text{original}})/(Z_{\text{pruned}} + Z_{\text{original}})$; constraint $|\Gamma|^2 \ll 0.25$ | [Axiom 3 Pruning](axiom3-pruning.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [LLM Topology Introduction](llm-topology-intro.md) | Chapter opening: AVE extension to virtual media; hardware/software isomorphism inversion ($Z \propto 1/A$ vs $Z \propto A$); saturation operator $S(r)$ |
| [SwiGLU Two-Port](swiglu-twoport.md) | Axiom 1 instantiation: coupled amplitude $A_j$ definition from gate and up projections |
| [Thermodynamic $A_c$](ac-thermodynamic.md) | Derivation of saturation threshold from training equilibrium |
| [Axiom 3 Pruning](axiom3-pruning.md) | Reflection coefficient $\Gamma_{\text{prune}}$ and coherence constraint |

## Contents

- [LLM Topology Introduction](llm-topology-intro.md) — Chapter opening and hardware/software isomorphism inversion
- [SwiGLU Two-Port Node](swiglu-twoport.md) — Axiom 1 instantiation: coupled amplitude $A_j$ definition
- [Thermodynamic Emergence of $A_c$](ac-thermodynamic.md) — derivation of the saturation threshold from training dynamics
- [Axiom 3: Least Reflected Action in Pruning](axiom3-pruning.md) — $\Gamma_{\text{prune}}$ introduced; coherence constraint
