[↑ Proofs and Computation](../index.md)
<!-- claim-quality (subtree): ak97cb, oltvwy -->

# Ch. 9: Computational Proof and Anomaly Catalog

Chapter 9 establishes the computational universality of the AVE physics engine across 39 orders of magnitude, defines the numerical precision hierarchy that prevents floating-point artefacts from masquerading as physical predictions, and enforces complete independence from external theoretical frameworks.

## Key Results

| Result | Statement |
|---|---|
| Scale invariance verification | Same operator, same code, from $10^{-13}$ m to $10^{26}$ m — 13 domains verified with 0 free parameters |
| Guard constant hierarchy | $\texttt{EPS\_NUMERICAL} = 10^{-12}$, $\texttt{EPS\_CLIP} = 10^{-15}$, $\texttt{EPS\_DIVZERO} = 10^{-30}$ |
| Dimensional traceability | $\ell_{node} = \hbar/(m_e c_0)$ [m], $\alpha = e^2/(4\pi\varepsilon_0 \hbar c_0)$ [---], $G = \hbar c_0/(7\xi_M m_e^2)$ [m$^3$/kg$\cdot$s$^2$] |
| Precision budget | $G$ limits cosmological predictions at $2.2 \times 10^{-5}$; all electromagnetic/atomic predictions limited by $m_e$, $\alpha$ uncertainties below 1 ppb |
| Orbital scaling independence | $r_n \propto n^2$ from topological standing-wave resonance condition, not Schrodinger |
| Subshell impedance cascade | Multi-electron repulsion resolved via discrete geometric LC resonators — no $Z_{eff}$ fitting, no variational probability integrals |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Computational Graph](./computational-graph.md) | Scale invariance proof, verification summary across 13 domains |
| [Anomaly Catalog](./anomaly-catalog.md) | Tier 2–4 proposed experimental tests and anomalous phenomena |
| [Precision Policy](./precision-policy.md) | Floating-point arithmetic, guard constants, dimensional analysis chain, precision budget |
| [Methodological Contamination](./methodological-contamination.md) | Framework independence, orbital scaling derivation, saturation regime verification, subshell impedance cascade |

---
