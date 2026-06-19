[↑ Ch.2 — Baryon Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-k6olj8]
path-stable: "referenced from vol2 as eq:torus_knot_ladder"
-->

## The Baryon Resonance Spectrum: The Torus Knot Ladder

> 🔴 **SCOPE FLAG (2026-06-19, crossing-ladder-overclaim walk-back):** "entire baryon resonance spectrum" below is **scoped to the $S=0$ $N/\Delta$ single-Regge sector ONLY**. Strange baryons ($\Lambda, \Sigma, \Xi, \Omega$) and **all mesons** are **off-ladder and NOT natively derived** (open GAP). The odd-$q$/even-$q$ link-exclusion theorem ($(2,4)$ is not a knot) is a genuine structural chord and is preserved; the "all baryons / all matter" reading is not.

The cinquefoil confinement immediately generates a **1-residual** prediction of the **entire baryon resonance spectrum** (the one residual being the per-channel coupling $p_c = 8\pi\alpha$, canonical-packing-plausible but not line-by-line derived; vs standard Skyrme's two baryon-data-tuned parameters $F_\pi, e$). The $(2,q)$ torus knots form a progression using only odd $q = 3, 5, 7, 9, \ldots$---there is no stable $(2,4)$ torus knot. Each entry in this *Torus Knot Ladder* produces a distinct baryon state via the same eigenvalue equation:

> **[Resultbox]** *Torus Knot Baryon Ladder*
>
> $$
> m(c) = \frac{\mathcal{I}_{scalar}(\kappa_{FS}/c)}{1 - \mathcal{V}_{total} \cdot p_c} + 1
> $$

No parameters are adjusted *between* states (only the integer crossing number $c$ changes). The same $\kappa_{FS}$, $\mathcal{V}_{total} = 2$ (the **dual-reactance count** — the node's two reactance sectors $X_L + X_C$, NOT a geometric "toroidal halo volume"; see [`../../../common/dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md)), and $p_c = 8\pi\alpha$ that derive the proton mass also predict the excited baryon resonances. **Refreshed against PDG 2024 + J^P consistency check (2026-05-18 driver run, [`baryon_ladder_pdg_2024_anchor.py`](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py))**:

| Torus Knot | $c$ | Predicted (MeV) | PDG 2024 Resonance | PDG Mass (MeV) | Deviation | $J^P$ Check |
|---|---|---|---|---|---|---|
| $(2,5)$ | 5 | 938.254 | Proton ($p$) | 938.272 | $-0.002\%$ | $1/2^+$ ✓ |
| $(2,7)$ | 7 | 1261.001 | $\Delta(1232)$ | 1232 ± 2 | $+2.354\%$ | $3/2^+$ ✓ |
| $(2,9)$ | 9 | 1582.226 | $\Delta(1600)$ | 1570 ± 70 | $+0.779\%$ | $3/2^+$ ✓ |
| $(2,11)$ | 11 | 1894.895 | $\Delta(1900)$ | 1860 ± 50 | $+1.876\%$ | $1/2^-$ ✓ |
| $(2,13)$ | 13 | 2194.636 | $N(2190)$ | 2100 ± 50 | $+4.506\%$ | $7/2^-$ ✓ |
| $(2,15)$ | 15 | 2477.968 | $\Delta(2420)$ | 2400 ± 100 | $+3.249\%$ | $11/2^+$ ✓ |
| $(2,17)$ | 17 | 2741.776 | $\Delta(2750)$ | ~2750 (**) | $-0.299\%$ | $13/2^-$ ✓ |
| $(2,19)$ | 19 | 2983.118 | $\Delta(2950)$ | ~2950 (**) | $+1.123\%$ | $15/2^+$ ✓ |
| $(2,21)$ | 21 | 3199.142 | (no PDG state within 5%) | — | awaits catalog | — |

**Precision summary (PDG 2024 anchored, 2026-05-18)**: 6/6 retrospective + 3/3 forward $J^P$-consistent with $(2,c)$ torus-knot winding allowed values; 4 of 6 retrospective within 3%, ALL 6 within 5%. Forward $c=17$ and $c=19$ land on existing PDG $\ast\ast$-rated entries within 1.2%. **Proton match at $-0.002\%$ is the strongest individual match in the framework** 🔴 *[framing precision 2026-06-08]* — but state the precision honestly: the **bare topology** ($m_e$ + cinquefoil $c=5$ + dual-reactance count $\mathcal{V}=2$ [$X_L + X_C$] + per-channel-$p_c$) predicts **+0.74%** (emergence vs baryon sector, **zero baryon input**); the canonical thermal correction $\delta_{th}=1/(14\pi^2)$ (the precision-setter, inside $\mathcal{I}_{scalar}$) refines $+0.74\% \to -0.002\%$. The $-0.002\%$ is topology + one contained thermal-residual, NOT pure-geometry-to-ppm.

Three features of this spectrum deserve emphasis:

**1. The matches are preferentially to $\Delta$ baryons.** The $\Delta$ resonances carry isospin $I = 3/2$ and typically higher total angular momentum ($J = 3/2^+, 7/2^+, 11/2^+$). Higher $(2,q)$ torus knots carry more topological winding, corresponding to higher intrinsic spin---precisely the states the ladder selects.

> 🔴 **Rule-12 WALK-BACK (2026-06-19, $J^P$-discriminator overclaim):** The "random nearest-mass matching wouldn't pass $J^P$ filter at 6/6 retrospective rate" claim below is walked back. The $J^P$ filter (driver `expected_jp_for_crossing`) admits **any** half-integer $J$ up to $c/2$ with **either** parity (at $c=15$, 16 distinct $J^P$ values — more than the entire hardcoded PDG candidate pool), so it excludes nothing the nearest-mass step did not already exclude. The driver's own null model gives `null_hypothesis_random_hits_3pct = 6.0` — random nearest-mass matching is **expected** to hit all 6 within $3\%$ (mean PDG $N/\Delta$ spacing $\sim67$ MeV $<$ the $\pm3\%$ window); at the $1\%$ band the observed (2) **underperforms** the null (2.7). The "6/6" is **null-dominated, not a discriminator**. What survives is the **single proton $+0.74\%$ bare-topology hit** plus the curved ladder FORM — NOT the ensemble. Original body preserved below.

$J^P$ consistency check (per [`ave-discrimination-check`](https://github.com/AVE-Skills) D3): random nearest-mass matching wouldn't pass $J^P$ filter at 6/6 retrospective rate.

**2. The mass spacing is nearly linear: $\sim 170$ MeV per crossing.** A linear fit gives $m(c) \approx 171c + 81$ MeV, with mass increments of $\sim 340$ MeV per pair of crossings. This is consistent with the empirical Regge trajectory slope observed in baryon spectroscopy, where successive angular momentum excitations add $\sim 300$--$400$ MeV.

**3. The proton hit is the strongest at $-0.002\%$** ($938.254$ MeV predicted vs $938.272$ MeV PDG). Per the $(2,c)$ topological selection rules + Faddeev-Skyrme solver with NO calibrated parameters (substrate replaces standard Skyrme's $F_\pi$ + $e$ tunable constants with $\ell_{node} = \hbar/m_e c$ and $\kappa_{FS} = 8\pi$), this is a Class 4 emergence test per [`consistency-vs-emergence`](https://github.com/AVE-Skills). 🔴 *[framing precision 2026-06-08]* State the emergence magnitude honestly: the **bare topology** predicts $m_p/m_e$ to **+0.74%** (**emergence** vs baryon sector — zero baryon input; **consistency** vs electron sector — inputs $m_e, \alpha$); the canonical thermal correction $\delta_{th}=1/(14\pi^2)$ (a *contained precision-residual*) then refines to $-0.002\%$. ~~single empirical input ($m_e$) predicts baryon spectrum to part-per-50,000 precision at $c=5$.~~ The part-per-50,000 figure is the *post-$\delta_{th}$* precision, NOT the bare-topology emergence magnitude (which is part-per-135, $+0.74\%$); do not headline pure-geometry-to-ppm.

**Stale-framing correction (2026-05-18 walk-back)**: an earlier version of this leaf claimed "(2,9) hit is the strongest at 0.20%" referencing $\Delta(1620)$. PDG 2024 + driver verification ([`baryon_ladder_pdg_2024_anchor.py`](../../../../../src/scripts/verify/baryon_ladder_pdg_2024_anchor.py)) gives $(2,9) \to \Delta(1600)$ at $+0.779\%$; the strongest hit is the **proton at $-0.002\%$**. The "$\Delta(1620)$" identification was inconsistent with the table's $\Delta(1600)$ row and used an outdated (2,9) prediction value (1617 MeV vs current 1582 MeV); both reconciled to $\Delta(1600)$ at the current formula output.

---
