[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol5 as sec:dual_formalism -->

# Dual-Formalism Architecture and the Op2 Crossing Correction

The atomic-scale radial eigenvalue problem required *two* complementary solver formalisms:

1. **ABCD cascade** (distributed TL) for the radial eigenvalue through a continuously screened potential.
2. **Y$\to$S network** (lumped LC) for the Hopf-link coupling correction between same-shell electron pairs.

Neither formalism alone captures the full physics of multi-electron atoms. The same duality appears at the protein scale, and identifying this structural isomorphism reveals a new topological correction (Op2 crossing penalty) that has not yet been incorporated into the folding engine.

<!-- cross-volume: ch:quantum_mechanics → Vol 2 atomic orbital solver (dangling — Anomaly A3) -->

## Atom $\leftrightarrow$ Protein Mapping

| **Operator / Feature** | **Atom** | **Protein** |
|---|---|---|
| **ABCD (distributed)** | Radial eigenvalue through screened potential $Z_{\rm net}(r)$ | 1D backbone $S_{11}$ cascade (this chapter) |
| **Y$\to$S (lumped)** | Hopf-link coupled resonator (P2) | Multi-path TL network (Ch. 5) |
| **Impedance profile** | $Z_{\rm net}(r) = Z - N_{\rm inner}$ (Gauss step) | $Z_{\rm topo}(i)$ = sidechain $\to Z(i)$ |
| **Op2 crossing** | $2s{\uparrow}$ through $1s{\uparrow}$: $\delta E = E \times P_C/4$ | Backbone loop crossing: $\delta E = E_{\rm bond} \times P_C/4$ |
| **Op3 reflection** | $\Gamma$ at shell boundary | $\Gamma$ at segment boundary |
| **Op5 cascade** | ABCD per radial section | ABCD per peptide unit |
| **Op6 eigenvalue** | $B_{\rm total}(E) = 0$ | $\lambda_{\min}(S^\dagger S) = 0$ |
| **Op9 steric** | Pauli exclusion at $r = 0$ | $C_\alpha$ steric reflection |

*Dual-formalism mapping between atom and protein scales. Every row is a universal operator, applied identically at both scales.*

The protein engine already uses *both* formalisms:

- The 1D ABCD cascade predicts secondary structure from wave propagation along the backbone.
- The 2D Y$\to$S network predicts tertiary structure from all-pairs coupling through H-bonds and contacts.

What is *missing* is the third component: the **Op2 topological crossing correction**, which penalises backbone self-crossings by a quantised, parameter-free energy cost.

> **[Resultbox]** *Dual-Formalism Architecture (Protein)*
>
> The protein folding engine uses two complementary solver formalisms:
>
> 1. **ABCD cascade** (distributed TL) for secondary structure from backbone wave propagation.
> 2. **Y$\to$S network** (lumped LC) for tertiary structure from all-pairs coupling.
>
> A third correction---the **Op2 topological crossing penalty** ($\delta E = c_{\min} \times 2\pi\alpha \times E_{\rm coupling}$)---penalises backbone knots by a quantised, parameter-free energy cost. This predicts that $\sim 99\%$ of natural proteins are unknotted, consistent with PDB statistics.

---
