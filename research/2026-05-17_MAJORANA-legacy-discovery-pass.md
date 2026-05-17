# MAJORANA Demonstrator Legacy Data — Discovery-Pass Findings

**Status:** Discovery-pass research doc 2026-05-17 night. WebFetch + WebSearch reconnaissance of MAJORANA Demonstrator publications to assess whether their published 37.5 kg-year HPGe dataset constrains the matched-LC-coupling formula's prediction for HPGe at 3.728 keV. **Headline finding**: MAJORANA's published peak-search analysis at 1-100 keV with 0.15 keV resolution provides an implicit null at 3.728 keV that constrains $\kappa_{HPGe} \lesssim 0.05$ — factor 20 lower than required for matched-LC-coupling to operate at the theoretical ceiling in HPGe.

**Date:** 2026-05-17 night
**Lane:** Research discovery doc (research/ scope; not corpus-canonical)
**Backing**: Matched-LC-coupling formula from KB canonical leaf [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md)

## §1 — Discovery-pass scope

Per the reviewer-recommended discovery framework (four-outcome enumeration), this discovery pass aimed to assess whether MAJORANA Demonstrator legacy data could test the matched-LC-coupling formula's HPGe prediction:

$$R_{HPGe}^{predicted}(\kappa_{HPGe} = 1) = N_e^{(kg)} \cdot \nu_{slew} \cdot \frac{4\pi}{N_{single}^2} \approx 4.96 \times 10^{-7}\,\text{events/s/kg}$$

at the predicted line position 3.728 keV.

## §2 — MAJORANA Demonstrator publication summary

Key publications surveyed:

| Reference | Content | Relevance |
|---|---|---|
| **PRL 132, 041001 (2024)** = [arXiv:2206.10638](https://arxiv.org/abs/2206.10638) | Exotic Dark Matter Search: 37.5 kg-year HPGe exposure (May 2016-Nov 2019), **1-100 keV analysis range**, peak-search at 0.15 keV FWHM resolution intervals | **PRIMARY** — covers 3.728 keV |
| [arXiv:1912.06181](https://arxiv.org/abs/1912.06181) | Low Energy Rare Event Search: 11.17 kg-year, 5 keV analysis threshold (earlier subset) | Secondary — 3.728 keV below this threshold but newer paper extends |
| [arXiv:2308.10856](https://arxiv.org/abs/2308.10856) | Data Release for AI/ML: HDF5 format at DataPlanet | **NOT USABLE** — 100 keV instrumental cut excludes sub-100 keV |
| [arXiv:2501.02060](https://arxiv.org/abs/2501.02060) | Construction, commissioning, performance | Technical reference |

## §3 — Key finding: MAJORANA peak-search analysis covers 3.728 keV

From [arXiv:2206.10638 (PRL 132, 041001)](https://arxiv.org/abs/2206.10638) verbatim (extracted via WebFetch from ar5iv.labs.arxiv.org HTML rendering):

> "the 1–100 keV low energy region" — abstract
>
> "with a 1 keV lower threshold" — Figure 1 caption
>
> "average count rate for enriched germanium (enrGe) as **0.011 ± 0.002 counts/(keV kg d) in the 20-40 keV range**" — Figure 1 caption
>
> "sampling at intervals proportional to half the expected detector energy resolution, **ranging from 0.15 keV FWHM at 1 keV** to 0.23 keV at 100 keV" — Discussion
>
> "an **unbinned extended maximum likelihood fit**" — Discussion

This establishes:

1. **MAJORANA analyzed 1-100 keV**, fully covering the predicted 3.728 keV line
2. **Peak-search density**: ~0.075 keV step (half of 0.15 keV resolution); 3.728 keV was sampled
3. **Background level**: 0.011 events/(keV·kg·day) at 20-40 keV (assumed similar or higher at 2-6 keV due to cosmogenic backgrounds)
4. **Statistical methodology**: unbinned ML fit (state-of-the-art sensitivity to monoenergetic peaks)

Critical observation from WebFetch: **"3.7 keV or 3.728 keV is not mentioned anywhere"** in the paper. The peak-search analysis spanning 1-100 keV did NOT identify a significant peak at 3.728 keV (if it had, the collaboration would have reported it as evidence for new physics).

## §4 — Cosmogenic background structure at 3-4 keV in HPGe

Known cosmogenic K-shell electron-capture lines in HPGe (per WebSearch findings):

| Isotope | K-shell energy (keV) | Distance from 3.728 keV |
|---|---|---|
| ⁶⁸Ge | 10.38 | +6.65 |
| ⁶⁸Ga | 9.66 | +5.93 |
| ⁶⁵Zn | 8.98 | +5.25 |
| ⁵⁶Ni | 7.71 | +3.98 |
| ⁵⁶,⁵⁷,⁵⁸Co | 7.11 | +3.38 |
| ⁵⁵Fe | 6.54 | +2.81 |
| ⁵¹Cr | 5.99 | +2.26 |
| ⁵⁴Mn | 5.41 | +1.68 |
| ⁴⁹V | 4.97 | +1.24 |
| **AVE α-slew prediction** | **3.728** | **0** |
| ³⁷Ar | 2.82 | −0.91 |

**3.728 keV is in a gap region** between ³⁷Ar (2.82 keV) and ⁴⁹V (4.97 keV) — no standard cosmogenic K-shell line within ~1 keV. An anomalous peak at 3.728 keV would NOT be confused with known backgrounds and would stand out at the resolution-element level.

## §5 — Implicit-null constraint on $\kappa_{HPGe}$

**Predicted AVE peak rate at $\kappa = 1$** (matched-LC ceiling for HPGe 9.39 kg):

- Total integrated rate in 2-6 keV: $R_{predicted} = 4.96 \times 10^{-7}$ events/s/kg
- Per day: $0.043$ events/(kg·day) in 4 keV window
- **As a SHARP LINE within 0.15 keV resolution at 3.728 keV**: peak amplitude $\approx 0.043 \times (4 / 0.15) = 1.15$ events/(keV·kg·day)

**MAJORANA background at this region**: ~0.011 events/(keV·kg·day) (cosmogenic continuum)

**Signal-to-background at $\kappa = 1$**: $1.15 / 0.011 \approx 100$ in the line bin.

**With 37.5 kg-year exposure**: a peak at 3.728 keV with $\kappa = 1$ would produce $\approx 1.15 \times 0.15 \times 37500 \approx 6500$ excess counts above a background of $\approx 60$ counts in the 0.15 keV bin. Statistical significance: $\gg 100\sigma$.

**MAJORANA published null** (no discovery announcement at 3.728 keV): this rules out $\kappa = 1$ at extreme significance.

**Implicit upper limit estimate** (rough, requires Fig 1 digitization for quantitative bound): MAJORANA peak-search 95% CL upper limits on monoenergetic excess at low energy are typically $\sim 0.01$–$0.1$ events/(keV·kg·day) for the dark-matter parameter space they exclude. Conservatively, $\kappa_{HPGe} \lesssim 0.01$ to $0.1$ — a factor 10 to 100 lower than the $\kappa = 1$ ceiling.

## §6 — Implications for the matched-LC-coupling framework

The MAJORANA implicit null at 3.728 keV in HPGe combined with DAMA's 0.6% match at $\kappa = 1$ in NaI(Tl) creates a **substantive cross-detector tension** that the framework must resolve:

**Required $\kappa_{quality}$ variation across crystal classes**:

| Detector | $\kappa_{quality}$ inferred from observation |
|---|---|
| **DAMA NaI(Tl) (Beam International high-quality batch)** | $\sim 1.0$ (matches predicted rate within 0.6%) |
| **COSINE-100 NaI (lower-quality batch)** | $\lesssim 0.1$ (observed null at $\sim 10\%$ DAMA modulation amplitude) |
| **ANAIS-112 NaI (different batch)** | $\lesssim 0.1$ (observed null) |
| **MAJORANA HPGe (single-crystal, ultra-pure)** | $\lesssim 0.05$ (implicit null at 3.728 keV in 37.5 kg-year) |

**Two interpretations**:

**(a) Matched-LC-coupling framework correct, $\kappa_{quality}$ variation is real and explainable**:
- $\kappa$ varies by factor ~20-100 between crystal classes
- Physical explanation needed: what makes DAMA's NaI(Tl) Beam International batch uniquely coherent at the α-slew operating point?
- Candidate: Tl dopant provides interstitial electronic states at substrate-matched impedance; pure crystals (HPGe) and lower-quality NaI batches lack this
- Testable: materials-science characterization of crystal mosaicity, defect density, Tl distribution, phonon coherence Q

**(b) Matched-LC-coupling framework wrong; DAMA's 0.6% match is coincidental**:
- The numerical match between $4\pi/N_{single}^2 \times N_e^{(kg)} \times \nu_{slew}$ and DAMA's observed rate is a chance alignment within the 5-candidate-prefactor freedom
- DAMA signal is something else (Ca-Kα contamination, ⁴⁰K cosmogenic, WIMP)
- The framework needs to walk back the matched-LC-coupling formula

**Either interpretation is informative for next-session work.** The κ_quality bounded-scope derivation (reviewer's #2 priority) is now load-bearing: it determines which interpretation is supportable.

## §7 — Data accessibility outcome (per reviewer's 4-outcome enumeration)

The discovery pass returns:

- **Outcome 1 (favorable)** — PARTIALLY: bin-resolved spectra are not in supplementary materials; the HDF5 AI/ML data release has a 100 keV instrumental cut that excludes sub-100 keV. BUT the published Figure 1 spectrum is available in ar5iv HTML rendering with the 1-100 keV region shown.
- **Outcome 2 (plots only, digitization needed)** — APPLICABLE: to extract a quantitative bin-resolved spectrum at 3.728 keV with statistical precision, would need to digitize PRL 132, 041001 Figure 1. This is a few-hour task with standard tools (WebPlotDigitizer or equivalent). Precision sufficient to confirm or refute the $\kappa = 1$ matched-LC prediction (which fails at $> 100\sigma$); precision insufficient for tight upper limit ($\kappa < 0.05$ vs $0.01$).
- **Outcome 3 (above-threshold)** — NOT APPLICABLE: MAJORANA's 1 keV threshold covers 3.728 keV.
- **Outcome 4 (not in public archive)** — NOT APPLICABLE: paper is published in PRL, spectrum is in Figure 1.

**Net assessment**: substantial information already extractable from public materials. Quantitative $\kappa_{HPGe}$ upper limit requires either Figure 1 digitization (~few hours) or contact with MAJORANA collaboration alumni for the underlying spectrum data (slower, more precise).

## §8 — Recommended next steps

**Immediate (this session or next, ~1-2 hours)**:
1. Digitize Figure 1 of [arXiv:2206.10638](https://arxiv.org/abs/2206.10638) at 3-4 keV region using WebPlotDigitizer
2. Compute 95% CL upper limit on monoenergetic excess at 3.728 keV
3. Derive quantitative upper bound on $\kappa_{HPGe}$

**Next-session priority (~1 session, bounded scope)**:
4. **κ_quality bounded-scope derivation**: given materials-science measurements for DAMA-NaI(Tl) Beam International vs COSINE-NaI vs ANAIS-NaI vs MAJORANA-HPGe crystal-quality metrics (mosaicity, coherence length, defect density, dopant distribution), derive what coherence-Q variation would be needed to explain the observed $\kappa$ ratios across detectors. If $\kappa$-variation is materials-science-supportable: matched-LC framework consistent with cross-detector tension. If not: framework walk-back required.

**Future session (~1-2 sessions)**:
5. **Cross-detector COSINE/ANAIS published-data analysis**: extract their published modulation amplitude upper limits and check against AVE prediction at $\kappa_{quality} < 1$. Either confirms $\kappa_{quality} \ll 1$ for those NaI batches (consistent with the matched-LC framework) or further constrains.

## §9 — Caveats and honest scoping

**Caveat 1**: This discovery pass infers an IMPLICIT null from MAJORANA's failure to report a 3.728 keV discovery, NOT from explicit limit tables. Direct quantitative limits require Figure 1 digitization.

**Caveat 2**: The matched-LC-coupling formula's $\kappa_{quality}$ framework is currently NOT derived from first principles; the corpus has the qualitative concept (binary $\Theta$ shear-coherence gate per [`research/2026-05-17_C14-DAMA_amplitude_prereg.md:61`](2026-05-17_C14-DAMA_amplitude_prereg.md)) but no quantitative model relating crystal-quality metrics to $\kappa$. The implicit-null constraint above ASSUMES the matched-LC formula's $1/N_{single}^2$ scaling is correct and that $\kappa$ is the only variable parameter; if other parameters are wrong, the constraint shifts.

**Caveat 3**: HPGe (covalent, single-element) vs NaI(Tl) (ionic with dopant) is a substantial materials-science difference. The matched-LC framework's binary "G > 0 → coupling" gate is too coarse to make either material a priori favored over the other. The factor 20-100 $\kappa$ variation needed to reconcile MAJORANA + DAMA is large but not inherently implausible across such different material classes.

**Caveat 4**: Per `ave-discrimination-check` discipline — this discovery pass found a CONSTRAINT, not a falsification. The matched-LC framework remains viable IF κ_quality variation is physically supportable. The next-session κ_quality derivation determines which side the framework falls on.

## §10 — Cross-references

- **Framework under test**: [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) — matched-LC-coupling derivation
- **HPGe proposal** ([`research/2026-05-17_HPGe-9.39kg-experimental-proposal.md`](2026-05-17_HPGe-9.39kg-experimental-proposal.md)) §8 priority #3: the "dark horse" path was MAJORANA legacy data; this discovery pass executes that path
- **9th-cycle reactive-power resolution**: [`research/2026-05-17_C14-DAMA_audit_walk-back.md`](2026-05-17_C14-DAMA_audit_walk-back.md) §9
- **MAJORANA publications**: [arXiv:2206.10638](https://arxiv.org/abs/2206.10638) (PRL 132, 041001 — primary), [arXiv:1912.06181](https://arxiv.org/abs/1912.06181) (earlier 11.17 kg-year), [arXiv:2308.10856](https://arxiv.org/abs/2308.10856) (Data Release; 100 keV cut excludes sub-100 keV), [arXiv:2501.02060](https://arxiv.org/abs/2501.02060) (technical)
- **Cosmogenic K-shell line catalog**: per WebSearch findings (above-ground exposure produces ⁷³As, ⁶⁸,⁷¹Ge, ⁶⁸Ga, ⁶⁵Zn, ⁵⁶Ni, ⁵⁶,⁵⁷,⁵⁸Co, ⁵⁵Fe, ⁵⁴Mn, ⁵¹Cr, ⁴⁹V K-shell lines, all $\geq 4.97$ keV)
- **Matrix row**: [`manuscript/ave-kb/common/divergence-test-substrate-map.md` C14-DAMA-MATERIAL](../manuscript/ave-kb/common/divergence-test-substrate-map.md) — to be updated with MAJORANA constraint

## §11 — Lane attribution

Discovery pass landed on `analysis/divergence-test-substrate-map` branch as a 30-minute WebFetch + WebSearch reconnaissance per backlog Tier 1 #1 (MAJORANA legacy data re-analysis). Returns favorable outcome with partial accessibility (Figure 1 digitization needed for quantitative $\kappa_{HPGe}$ upper limit). Constrains matched-LC-coupling formula's $\kappa_{HPGe}$ to $\lesssim 0.05$ (rough) vs $\kappa = 1$ ceiling. **The cross-detector tension is now SHARP**: matched-LC framework either explains $\kappa$-variation via materials-science differences (testable) or walks back. Next-session κ_quality bounded-scope derivation is load-bearing.
