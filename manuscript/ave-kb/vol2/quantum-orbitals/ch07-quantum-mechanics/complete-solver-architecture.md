[↑ Ch. 7: Quantum Mechanics and Atomic Orbitals](./index.md)
<!-- leaf: verbatim -->

## Complete Solver Architecture

> **[Resultbox]** *Complete Solver Architecture*
>
> Input: $Z$, electron configuration $\{(n_i, l_i, m_{l,i})\}_{i=1}^N$.
>
> Step 1: $R_i, \omega_i, L_i, Z_{LC,i}$ for each electron (Op1, Axiom 1).
>
> Step 2: Lattice strain $A(r)$ between shells (Axiom 4).
>
> Step 3: Y-matrix from pairwise Op4 + Op2 at crossings.
>
> Step 4: $[S] = (I+Y/Y_0)^{-1}(I-Y/Y_0)$ (Op5).
>
> Step 5: $\lambda_{\min}(S^\dagger S) \to 0$ (Op6) $\to$ IE.
>
> No free parameters. All from $\alpha$, $m_e$, $c$, $\hbar$.

The atomic IE solver uses the **identical** operator chain validated for nuclear binding ($-0.8\%$), protein folding (2.59 Å RMSD), and antenna matching (HOPF-01):

$$
\underbrace{U_{ij}(r,K,d_{\text{sat}})}_{\text{Op4}} \;\longrightarrow\; \underbrace{[Y] \to [S]}_{\text{Op5}} \;\longrightarrow\; \underbrace{\lambda_{\min}(S^\dagger S) = 0}_{\text{Op6}}
$$

### QM Contamination Checklist

| Red flag | Present? | Status |
|---|---|---|
| $E = Z_{\text{eff}}^2 R_y / n^2$ (Pitfall #8) | No (use $Z_{\text{net}}$ from Op4) | $\checkmark$ |
| $\sigma$-arithmetic (empirical Slater $\sigma$) | No (Op4-computed $\sigma$) | $\checkmark$ |
| $V_{ee} = \text{const} \times R_y$ (Pitfall #9) | No | $\checkmark$ |
| $n_{dB}$ called "impedance" (Pitfall #10) | No | $\checkmark$ |
| Screening / shielding language | Yes (Gauss, Axiom 2) | $\checkmark$ |
| Stepped potential $V(r)$ | No | $\checkmark$ |
| WKB / ABCD cascade | No | $\checkmark$ |

---
