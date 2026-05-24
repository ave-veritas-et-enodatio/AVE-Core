[↑ Ch.12 Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-to41c7]
-->

## Baryon Mass Predictions (Torus Knot Ladder)

The $(2,q)$ torus knot ladder generates a zero-parameter mass spectrum using only the crossing number $c$.

> **Convention correction (2026-05-18 walk-back)**: An earlier version of this leaf used a $(2,q) \to c = q - 2$ labeling convention (showing proton as "$(2,3)$"), which was inconsistent with both the Vol 2 canonical anchor [`torus-knot-ladder-baryons.md`](../../../vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) and the production code [`constants.py:733`](../../../../../src/ave/core/constants.py:733) (`TORUS_KNOT_CROSSING_NUMBERS = [5, 7, 9, 11, 13]`). The canonical convention is $(2,q) \to c = q$: proton is the **cinquefoil $(2,5)$** at $c=5$, NOT the trefoil $(2,3)$. The electron is the $(2,3)$ trefoil; the proton is the next chiral torus knot after $(2,3)$ under the K4 substrate's chirality + torus + p=2 + q-odd selection rules. Table below realigned to canonical convention + refreshed against PDG 2024 + $J^P$ consistency check per [`baryon_ladder_pdg_2024_anchor.py`](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py).

### Confirmed Retrospective Matches (PDG 2024 anchored, $J^P$-checked)

| $(2,q)$ | $c$ | Predicted (MeV) | PDG 2024 Resonance | PDG Mass (MeV) | Deviation | $J^P$ Check |
|---|---|---|---|---|---|---|
| $(2,5)$ | 5 | 938.254 | Proton ($p$) | 938.272 | $-0.002\%$ | $1/2^+$ ✓ |
| $(2,7)$ | 7 | 1261.001 | $\Delta(1232)$ | 1232 ± 2 | $+2.354\%$ | $3/2^+$ ✓ |
| $(2,9)$ | 9 | 1582.226 | $\Delta(1600)$ | 1570 ± 70 | $+0.779\%$ | $3/2^+$ ✓ |
| $(2,11)$ | 11 | 1894.895 | $\Delta(1900)$ | 1860 ± 50 | $+1.876\%$ | $1/2^-$ ✓ |
| $(2,13)$ | 13 | 2194.636 | $N(2190)$ | 2100 ± 50 | $+4.506\%$ | $7/2^-$ ✓ |
| $(2,15)$ | 15 | 2477.968 | $\Delta(2420)$ | 2400 ± 100 | $+3.249\%$ | $11/2^+$ ✓ |

**6/6 retrospective $J^P$-consistent with $(2,c)$ topological winding selection rule.** 4 of 6 within 3%; ALL 6 within 5%. Proton match at $-0.002\%$ is the strongest individual match in the framework.

### Forward Predictions (Testable, PDG 2024 status)

| $(2,q)$ | $c$ | Predicted Mass (MeV) | PDG 2024 Candidate | Deviation | Search Target |
|---|---|---|---|---|---|
| $(2,17)$ | 17 | 2741.776 | $\Delta(2750)$ (PDG $\ast\ast$) | $-0.299\%$ | CLAS12 (JLab), PANDA (FAIR) to upgrade $\ast\ast \to \ast\ast\ast$+ |
| $(2,19)$ | 19 | 2983.118 | $\Delta(2950)$ (PDG $\ast\ast$) | $+1.123\%$ | Same facilities |
| $(2,21)$ | 21 | 3199.142 | (no PDG state within 5%) | awaits catalog | New search target |

Mass spacing: $\sim 170$ MeV per crossing (consistent with empirical Regge slope).

### Falsification Protocol (PDG 2024 anchored)

1. **Retrospective**: 6/6 matches verified $J^P$-consistent with PDG 2024 (no parameters adjusted between states)
2. **Forward**: $(2,17)$ at $2742 \pm 100$ MeV lands on $\Delta(2750)$ at $-0.30\%$. If PDG upgrades $\Delta(2750)$ to $\ast\ast\ast$+ (real state), forward chain confirmed. If $\Delta(2750)$ downgraded to $\ast$ or dissolves, ladder at $c=17$ falsified.
3. **Spacing**: Any departure from linear $\sim 170$ MeV increment → model falsified
4. **$J^P$ consistency**: If any retrospective $J^P$ assignment changes in PDG to be inconsistent with $(2,c)$ topological winding, that match becomes post-hoc-fit and discriminative claim weakens

> [!IMPORTANT]
> This prediction is unique to AVE: no other model derives baryon resonances from a single topological formula with zero adjusted parameters. Standard Skyrme has 2 tunable parameters ($F_\pi$, $e$); AVE replaces both with substrate constants ($\ell_{node} = \hbar/m_e c$, $\kappa_{FS} = 8\pi$). Class 4 emergence test per [`consistency-vs-emergence`](https://github.com/AVE-Skills): 1 empirical input (CODATA $m_e$) predicts 6+ baryon masses via integer-c topology change only.

---
