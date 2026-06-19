[↑ Ch.12: Falsifiable Predictions](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-to41c7]
-->

## The Torus Knot Ladder: Baryon Resonance Mass Predictions

> ↗ See also: [Vol 2 Ch 2 canonical anchor `torus-knot-ladder-baryons.md`](../../../vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) (refreshed against PDG 2024 + J^P 2026-05-18 per C8 PDG anchor merge `f4c9ffa`)
>
> ↗ See also: [Vol 4 alt anchor `baryon-mass-predictions.md`](baryon-mass-predictions.md) (convention realigned (2,3)→(2,5) for proton per FI-13 RESOLVED 2026-05-18)

> 🔴 **SCOPE FLAG (2026-06-19, crossing-ladder-overclaim walk-back):** This ladder is scoped to the **$S=0$ $N/\Delta$ single-Regge sector only**. Strange baryons ($\Lambda, \Sigma, \Xi, \Omega$) and **all mesons** are **off-ladder and NOT natively derived** (open GAP). Nothing on this page may be read as "all baryons" or "all matter".

The AVE framework's Torus Knot Ladder (Chapter 6, Section 6.4) generates a zero-parameter mass spectrum for **$S=0$ $N/\Delta$** baryon resonances using only the crossing number $c$ of the $(2,q)$ torus knots. The genuine chord here is **structural** and survives in full (see "What survives" below): the integer-ness of $c$, the odd-$q$/even-$q$ link-exclusion theorem, $(2,3)$ = smallest knot, the curved (non-linear-Regge) ladder FORM, and the single **proton $+0.74\%$ bare-topology hit**. The retrospective table reproduces the cataloged $N/\Delta$ masses to within $5\%$ (per C8-BARYON-LADDER PDG anchor driver [`baryon_ladder_pdg_2024_anchor.py`](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py), commit `55b3317` 2026-05-18); the c=17/c=19 rows are **postdictions** against pre-existing PDG entries, not forward predictions (see "Forward predictions" §, walked back 2026-06-19).

### Retrospective matches (PDG 2024 anchored, J^P-checked)

| $(2,q)$ | $c$ | Predicted (MeV) | PDG 2024 Resonance | PDG Mass (MeV) | Deviation | $J^P$ Check |
|---|---|---|---|---|---|---|
| $(2,5)$ | 5 | 938.254 | Proton ($p$) | 938.272 | $-0.002\%$ | $1/2^+$ ✓ |
| $(2,7)$ | 7 | 1261.001 | $\Delta(1232)$ | 1232 ± 2 | $+2.354\%$ | $3/2^+$ ✓ |
| $(2,9)$ | 9 | 1582.226 | $\Delta(1600)$ | 1570 ± 70 | $+0.779\%$ | $3/2^+$ ✓ |
| $(2,11)$ | 11 | 1894.895 | $\Delta(1900)$ | 1860 ± 50 | $+1.876\%$ | $1/2^-$ ✓ |
| $(2,13)$ | 13 | 2194.636 | $N(2190)$ | 2100 ± 50 | $+4.506\%$ | $7/2^-$ ✓ |
| $(2,15)$ | 15 | 2477.968 | $\Delta(2420)$ | 2400 ± 100 | $+3.249\%$ | $11/2^+$ ✓ |

> 🔴 **Rule-12 WALK-BACK (2026-06-19, methodology overclaim):** The "random nearest-mass matching cannot pass $J^P$ filter at 6/6 retrospective rate" claim below is **walked back as a discriminator overclaim**. The $J^P$ filter (driver `expected_jp_for_crossing`) admits **any** half-integer $J$ up to $c/2$ with **either** parity — at $c=15$ it allows 16 distinct $J^P$ values, more than the entire 8-state hardcoded PDG candidate pool. It therefore excludes nothing the nearest-mass step did not already exclude. The driver's **own** null model gives `null_hypothesis_random_hits_3pct = 6.0`: random nearest-mass matching is **expected** to hit all 6 within $3\%$, because mean PDG $N/\Delta$ spacing ($\sim67$ MeV) is smaller than the $\pm3\%$ window. At the $1\%$ band the observed count (2) **underperforms** the null expectation (2.7). So "6/6 beats chance" is **null-dominated, not a discriminator**. The surviving chord-side positive is the **single proton hit** ($+0.74\%$ bare-topology, closed to $\sim-0.002\%$ by one contained thermal residual $\delta_{th}=1/(14\pi^2)$) **plus the curved ladder FORM** — NOT the ensemble. Original body preserved below.

**Precision summary (PDG 2024 anchored, C8 PDG 2024 anchor commit `55b3317`)**: 6/6 retrospective $J^P$-consistent with $(2,c)$ torus-knot winding allowed values; **4 of 6 retrospective within 3%, ALL 6 within 5%**. **Proton match at $-0.002\%$ is the strongest individual match in the framework** (200× more precise than corpus's prior "+0.00%" precision-rounding framing). Set by 1 input (CODATA $m_e$) + 1 topological integer (cinquefoil $c=5$) + 1 halo invariant (Borromean $V=2$). Per `ave-discrimination-check` D3: random nearest-mass matching cannot pass $J^P$ filter at 6/6 retrospective rate.

### Forward predictions (PDG 2024 anchored)

> 🔴 **Rule-12 WALK-BACK (2026-06-19, "forward predictive spectrum CONFIRMED" overclaim):** The "**CONFIRMED**" headlines for $c=17$ and $c=19$ below are walked back. $\Delta(2750)$ and $\Delta(2950)$ are **pre-existing PDG-2024 catalog entries** hardcoded in the driver's own table (`baryon_ladder_pdg_2024_anchor.py`, `PDG_2024_BARYONS` list, entries lines 119–136 on HEAD). Matching a predicted mass to the nearest **already-cataloged** state is **postdiction (retrodiction), not forward prediction**. The only genuinely-open row is $c=21 \to 3199$ MeV, which currently **misses** the nearest cataloged state ($\Delta(2950)$) by $+8.4\%$ — failing its own $5\%$ gate. The row is kept; its epistemic status is relabeled. Original body preserved below.

**Restated honestly (2026-06-19):**

| $(2,q)$ | $c$ | Predicted Mass (MeV) | Epistemic status |
|---|---|---|---|
| $(2,17)$ | 17 | 2741.776 | **POSTDICTION**: nearest pre-cataloged PDG entry $\Delta(2750)$ at $-0.30\%$ (PDG $\ast\ast$; hardcoded in driver table) |
| $(2,19)$ | 19 | 2983.118 | **POSTDICTION**: nearest pre-cataloged PDG entry $\Delta(2950)$ at $+1.12\%$ (PDG $\ast\ast$; hardcoded in driver table) |
| $(2,21)$ | 21 | 3199.142 | **GENUINE FORWARD PREDICTION (currently MISSING)**: nearest cataloged state $\Delta(2950)$ off by $+8.4\%$, fails the $5\%$ gate; open search target above $\sim3000$ MeV |

Original (walked-back) framing preserved:

| $(2,q)$ | $c$ | Predicted Mass (MeV) | Status (PDG 2024) |
|---|---|---|---|
| $(2,17)$ | 17 | 2741.776 | **CONFIRMED**: $\Delta(2750)$ at $-0.30\%$ (PDG $\ast\ast$) |
| $(2,19)$ | 19 | 2983.118 | **CONFIRMED**: $\Delta(2950)$ at $+1.12\%$ (PDG $\ast\ast$) |
| $(2,21)$ | 21 | 3199.142 | Testable; no PDG entry within 5% yet (search target) |

### The Falsification Protocol

> 🔴 **Rule-12 WALK-BACK (2026-06-19):** Protocol items **2** ("forward predictions … land on existing PDG entries") and **4** ("$J^P$ discriminator … random nearest-mass matching cannot pass at 6/6 rate") restate the two overclaims walked back above. Item 2's $c=17/c=19$ "land on existing PDG entries" is **postdiction** against hardcoded catalog states (driver `PDG_2024_BARYONS` lines 119–136); only $c=21$ is a genuine forward test and it currently misses by $+8.4\%$. Item 4's "$J^P$ discriminator" excludes nothing (filter admits any $J\le c/2$, either parity) and the driver's own null hits 6/6 at $3\%$, so the 6/6 is null-dominated. Original body preserved below.

1. **Retrospective check**: 6/6 retrospective matches with PDG 2024 baryon table ($J^P$-consistent, all within 5%); proton at $-0.002\%$; reproducible via [`baryon_ladder_pdg_2024_anchor.py`](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py).
2. **Forward predictions**: $(2,17) \to \Delta(2750)$ at $-0.30\%$ and $(2,19) \to \Delta(2950)$ at $+1.12\%$ both land on existing PDG $\ast\ast$-rated entries; CLAS12 at Jefferson Lab and PANDA at FAIR upgrade of $\ast\ast \to \ast\ast\ast+$ would confirm. $(2,21) \to 3199$ MeV is the next search target.
3. **Mass spacing**: the ladder predicts an approximately linear mass increment of $\sim 170\,\text{MeV}$ per crossing ($m(c) \approx 171c + 81$ MeV linear fit), consistent with the empirical Regge slope.
4. **$J^P$ discriminator** (per ave-discrimination-check D3): all retrospective matches preserve $(2,c)$ torus-knot winding $\to J^P$ selection rule. Random nearest-mass matching cannot pass at 6/6 rate.

This prediction is unique to the AVE framework: no other model derives the baryon resonance spectrum from a single topological formula with **zero adjusted parameters + 1 electron-physics-provenanced empirical input (CODATA $m_e$) + 1 topological integer + 1 halo invariant**.

### Particle identification (per FI-13 RESOLVED 2026-05-18)

The $(2,q)$ torus-knot family is the canonical baryon-sector winding ladder per Foundation Item 13 (2,5)-namespace disambiguation resolved 2026-05-18:

- **Electron**: $0_1$ unknot (the simplest closed flux-tube loop); $(2,3)$ trefoil is the phase-space Clifford-torus winding pattern (per Vol 2 Ch 2 + Q-G19α canonical)
- **Proton**: $(2,5)$ cinquefoil per-loop winding on Borromean N=3 baryon (canonical via this leaf + Vol 2 Ch 2)
- **$\Delta$ baryons**: $(2,7) / (2,9) / (2,11) / (2,13) / (2,15)$ + forward predictions
- **Lepton family** (electron / muon / tau): stays at $(2,3)$ trefoil + climbs **Cosserat torsion ladder** (NOT (p,q) extension) — see [`q-g27-muon-cosserat-saliency.md`](../../../vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md) for muon canonical
- **Neutrino**: single-loop screw defect coupling to SAME $(2,5)$ resonance class as proton (RESONANCE LABEL, not topological-identity match)

The $(2,q)$ winding count is INTERNAL to each N-class: leptons stay at $(2,3)$ + climb Cosserat torsion; baryons climb $(2,q_{odd})$ per-loop winding on fixed Borromean 3-loop structure.

### Cross-references

- [Vol 2 canonical anchor](../../../vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md) — full Vol 2 derivation chain
- [Vol 4 alt anchor](baryon-mass-predictions.md) — convention-realigned alt presentation
- [C8-BARYON-LADDER matrix row](../../../common/divergence-test-substrate-map.md) — Matrix 1 Predictions row PROMOTED FULL CLOSURE
- [Driver `baryon_ladder_pdg_2024_anchor.py`](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py) + [results JSON](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor_results.json)
- Closure-roadmap §0.5 2026-05-18 C8 entry
- Foreword "Third positive load-bearing empirical confirmation at scale" line 115 (per 2026-05-18 promotion)

### Status (2026-05-20; framing corrected 2026-06-19)

**Structural chord PASS; ensemble/forward framing walked back (2026-06-19).** What stands at PDG 2024 anchor scale: the integer-$c$ ladder structure, the odd-$q$/even-$q$ link-exclusion ($(2,4)$ is not a knot), $(2,3)$ = smallest knot, the curved (non-linear-Regge) ladder FORM, and the **single proton $+0.74\%$ bare-topology hit** ($-0.002\%$ post one contained $\delta_{th}$) — the strongest individual empirical match in the framework. What was walked back (see the two Rule-12 banners above): the prior "**FULL PASS**" headline rested on a 6/6 "discriminator" that is null-dominated (driver `null_hypothesis_random_hits_3pct = 6.0`) and on $c=17/c=19$ "forward predictions" that are postdictions against hardcoded catalog entries. The matrix C8 row "PROMOTED FULL CLOSURE" label and the Foreword "Third positive load-bearing empirical confirmation at scale" line should be re-scoped to the proton-hit + structural chord, not the ensemble (flagged for the auditor lane to land; not edited here). Cross-scale corroboration via A1-HOPF chiral antenna ($(2,q)$ family at EE scale) and C3-MUON-DELTA Fermilab g-2 anchor ($(2,3)$+Cosserat lepton family) pending — see [`_orchestration/experimental/a1-hopf/exp-a1-hopf.md`](../../../../../_orchestration/experimental/a1-hopf/exp-a1-hopf.md) sub-epic for EE-scale corroboration plan.

---
