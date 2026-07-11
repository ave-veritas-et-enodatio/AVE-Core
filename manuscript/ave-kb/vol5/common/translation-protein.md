[↑ Vol 5 Translation Tables](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-r6uef4]
-->

---

## Table: Protein Folding Terminology Translation (tab:trans_protein)

Protein folding terminology: structural biology $\leftrightarrow$ transmission line / circuit theory $\leftrightarrow$ AVE derivation.

| **Biology** | **Electrical Engineering** | **AVE Derivation** |
|---|---|---|
| Amino acid backbone | Cascaded transmission line | $L$-$C$ ladder from bond stiffness |
| Sidechain R-group | Shunt stub impedance | $Z_R(\omega)$ at backbone junction |
| Helix propensity $P_\alpha$ | Impedance match ($Z_R \gg Z_0$) | Low $Z_{topo}$: stub invisible |
| Sheet / coil tendency | Impedance mismatch ($Z_R \sim Z_0$) | High $Z_{topo}$: destructive interference |
| Ramachandran map | Smith chart | Allowed $\Gamma$ trajectories |
| Steric clash | Short-circuit reflection ($\Gamma = -1$) | $d < r_A + r_B$ (Pauli exclusion) |
| H-bond ($i \to i{+}4$) | Series resonant coupling | $L$-$C$ energy transfer at $\omega_0$ |
| Inter-strand H-bond | Coupled microstrip lines | Mutual $L$/$C$ at $d_\beta = 4.7$ Å |
| Hydrophobic effect | Impedance mismatch with termination | $h_i \cdot h_j$ coupling (water $\varepsilon_r \approx 80$) |
| Native fold | Matched load (zero reflection) | Global $U_{\text{total}}$ minimum |
| Levinthal's paradox | Why doesn't the line ring forever? | Deterministic $Z$-driven gradient |
| Disulfide bond | Topological short-circuit | Non-local $Z$-match creates loop |
| Salt bridge (Glu--Lys) | Conjugate impedance match | $\operatorname{Re}(Z_i \cdot Z_j^*) > 0$ |
| Solvent (water) | Chassis ground (parasitic shunt) | $Y_{\text{solv}} = \text{exposure}_i / Z_{\text{H}_2\text{O}}$ |
| L-amino acid chirality | Non-reciprocal waveguide | $\beta_{\text{eff}} = \beta_0 - \delta_\chi \tanh(\chi/\chi_0)$ |
| $\alpha$-helix | Helical slow-wave structure | Right-handed coiled delay line |
| $\beta$-sheet | Coupled stripline array | Antiparallel microstrip pair |

> **Reconciliation note (collapse-batch T19, drift-grade).** The "Conjugate impedance match" label on the **salt bridge** (`:28` above) is attached to a *different* residue pair by `vol5/common/translation-protein-solver.md:20-21` (there the **hydrophobic core** is the conjugate-impedance match and the salt bridge is "Reactive LC resonance"). The solver ground truth `common/solver-toolchain.md:477` uses **one** Conjugate-Matching term, $Y_{shunt}\propto \operatorname{Re}(Z_iZ_j^*)/d_{ij}^2$, for **both** salt bridges and hydrophobic pairs. **FLAG, not asserted** — the two-terms-vs-one question depends on the live `dc_analysis()` internals, which are not visible from this checkout.

---
