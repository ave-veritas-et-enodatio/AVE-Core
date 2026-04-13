[↑ App F: Universal Solver Toolchain](./index.md)
<!-- leaf: verbatim -->

## The Torus Knot Ladder

The $(2,q)$ torus knots with odd $q = 3, 5, 7, \ldots$ generate a family of topological solitons. Each member is characterised by its crossing number $c = q$, which sets both the confinement radius ($r_{\mathrm{opt}} = \kappa_{\mathrm{FS}}/c$) and the eigenvalue mode number ($\ell = c$).

Running the Faddeev-Skyrme solver with the Borromean 3D tensor correction for each crossing number yields a mass spectrum, a QNM (particle resonance), and a medium eigenvalue (exchange boson):

| $c$ | Knot | Mass [MeV] | QNM [MeV] | Medium [MeV] |
|---|---|---|---|---|
| 3 | Trefoil $(2,3)$ | 637 | 614 | 69.6 |
| 5 | Cinquefoil $(2,5)$ | 945 | 1519 | 141 |
| 7 | Septafoil $(2,7)$ | 1270 | 2859 | 229 |

**Validated: $c = 5$ (proton).** The proton mass (945 vs. 938 MeV, $+0.7\%$), the $N(1520)$ resonance (1519 vs. 1520 MeV, $-0.1\%$), and the charged pion (141 vs. 140 MeV, $+1.2\%$) all emerge from first principles with zero tuning.

**Predictions: $c = 3$ and $c = 7$.** The trefoil soliton at 637 MeV is *not* the electron (which is an unknot $0_1$, not a torus knot); it corresponds to a hypothetical light baryon or constituent diquark. The septafoil at 1270 MeV lies near the known strange baryons $\Sigma(1385)$ and $\Lambda(1405)$.

**Structure.** Each knot's three eigenvalues are derived from the same chain:

1. Faddeev-Skyrme solver $\to$ $I_{1\mathrm{D}}(c)$,
2. Borromean tensor correction $\to$ $I_{\mathrm{total}} = I_{1\mathrm{D}}/(1 - 2V\kappa_v) + 1$,
3. Mass: $m_c = I_{\mathrm{total}} \times m_e$,
4. QNM: $E_{\mathrm{QNM}} = c(1+\nu)\,\hbar c\,/\,D_c$ where $D_c = 4\hbar/(m_c c)$,
5. Medium: $E_{\mathrm{med}} = c(1+\nu)\,c^2\,\sqrt{m_e\,m_c}$.

---
