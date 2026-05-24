# C5-CMB-AXIS Shamir 2022 Cross-Catalog Validation — Result

**Date:** 2026-05-19
**Branch:** `analysis/c5-shamir-2022-cross-catalog` off `analysis/integration` at `588e069`
**Driver:** [`src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation.py`](../src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation.py)
**Result JSON:** [`src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation_results.json`](../src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation_results.json)
**Pre-registration:** [`research/2026-05-19_c5-shamir-2022-cross-catalog-prereg.md`](2026-05-19_c5-shamir-2022-cross-catalog-prereg.md)
**Briefing:** [`_orchestration/c5-shamir-2022-cross-catalog.md`](../_orchestration/c5-shamir-2022-cross-catalog.md)
**Predecessors:**
- E1b: [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md) (CMB axis (60.28, 50.48), sigma=0.92)
- E1b-prime: [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md) (sigma_Hubble 30 -> 24, Marginal-D)
- E1c SDSS DR17: [`research/2026-05-19_c5-sdss-spin-orientation-result.md`](2026-05-19_c5-sdss-spin-orientation-result.md) (LSS axis (129, 79), sigma=6.83, Marginal-D)
- C5 GZ-DECaLS scoping: [`research/2026-05-19_c5-gz-decals-spin-orientation-scoping.md`](2026-05-19_c5-gz-decals-spin-orientation-scoping.md) (Outcome E — chirality observable absent)

---

## 0. TL;DR

**Outcome: A (CATALOG-AGREE) — within 1 sigma_combined — BUT with E2 sub-finding (catalog-access blocker) flagging reduced cross-catalog cross-validation depth, AND a methodology-systematic surface at the SDSS imaging level.**

Paper-quoted-axis comparison of Shamir 2022 DESI Legacy Survey (~1.287M spirals, Ganalyzer algorithmic chirality on DECaLS DR8 + BASS + MzLS imaging) against the AVE C5 SDSS DR17 axis (l=129.0, b=79.0, sigma=6.83 via Longo cos-gamma estimator on Galaxy Zoo 1 + SDSS DR7). Shamir 2022's catalog is NOT publicly redistributed — data-availability statement is "upon reasonable request" only — so this session executes a **paper-quoted-axis comparison** using Shamir's published Table 3, not a live-fire catalog re-fit.

**Primary finding (Shamir DESI Legacy vs AVE SDSS DR17):**
- Shamir DESI axis (galactic): **(l = 242.10, b = -46.91)** (equivalently canonical-axis (62.10, +46.91))
- Sigma_Shamir from asymmetric 1sigma (RA, Dec) box -> galactic 68% containment: **42.57 deg**
- Sigma_combined with SDSS DR17 (sigma=6.83): **43.12 deg**
- **Separation: 39.83 deg = 0.92 sigma_combined**
- **OUTCOME: A (CATALOG-AGREE within 1 sigma_combined)**

**Striking sub-finding (Shamir DESI vs CMB axis-of-evil):**
- Separation: **3.77 deg = 0.09 sigma_combined**
- Shamir 2022's DESI Legacy axis lands *on* the Planck PR3 SMICA CMB axis-of-evil direction within Shamir's wide sigma. The absolute alignment 3.77 deg is small even in absolute terms (much smaller than sigma_Shamir = 42.57 deg; small in absolute terms regardless of sigma).

**Methodology-systematic surface (Shamir SDSS vs AVE SDSS DR17):**
- Same broad input galaxies (SDSS-class spirals), different methodology + classifier.
- Shamir SDSS axis (galactic): (l = 150.75, b = +5.78), sigma = 23.83 deg
- AVE SDSS DR17 axis: (l = 129.00, b = +79.02), sigma = 6.83 deg
- **Separation: 74.04 deg = 2.99 sigma_combined**
- Verdict: **METHODOLOGY-SYSTEMATIC SURFACE** — Ganalyzer (algorithmic, regression on radial intensity peaks) and Longo cos-gamma on GZ1 (crowdsourced ±1 vote) report axes ~3sigma apart on the same SDSS-class input.

**Outcome strength caveat (per prereg sec 4.2 tie-breaker):** sigma_Shamir > 35 -> the A label is WEAK. The cross-catalog separation precision is bottlenecked by Shamir's wide 1sigma box, not by AVE SDSS DR17. The 1sigma-box-max / 68%-containment ratio is 1.76 for DESI; the box is non-circular. The outcome is "consistent-with-the-prediction but not informative-as-cross-validation" in the precision-asymmetric regime.

**Cascade:**
- C5 row: A (Outcome strength = weak) — cross-catalog cross-validation does NOT decisively resolve the SDSS DR17 result's Marginal-D / CMB-LSS = 5.33sigma exclusion (E1c finding). Two paths agree within Shamir's wide sigma.
- D4-A034 cosmic-row Observable 3 (LSS spin direction): the Shamir DESI direction (galactic 242, -47, or equivalently canonical 62, +47) is in fact RIGHT ON the CMB axis-of-evil direction (60.28, 50.48). The 5.33sigma exclusion of CMB-vs-LSS alignment FROM E1c IS NOT seen in Shamir 2022 — Shamir's DESI axis IS at the CMB axis. This is a substantive methodology-dependent result.
- The methodology-systematic surface (Shamir SDSS row vs AVE SDSS DR17 at 2.99sigma) IS the load-bearing finding: same-data, different-methodology gives ~3sigma different axes. Either Lintott GZ1 + Longo cos-gamma OR Shamir Ganalyzer is methodology-biased in axis direction.
- E1c (Route 3 framework-commitment activation): stays DEFERRED. The cross-catalog test would have been decisive IF Shamir's sigma had been narrow enough to reach decisive A or C; in the wide-sigma regime the outcome is consistency without sharp discrimination.

**Anomaly surfaced (per flag-don't-fix):**
- Brief cites Shamir 2022 as MNRAS **516:2204**; actual reference is MNRAS **516(2):2281-2291**. Page-number transcription error in brief drafting. Surfaced for auditor lane.

---

## 1. Methodology summary (per prereg sec 3)

### 1.1 Data source

- **Source paper**: Shamir, L., 2022, "Analysis of spin directions of galaxies in the DESI Legacy Survey", MNRAS 516(2):2281-2291, DOI 10.1093/mnras/stac2372.
- **Catalog availability**: per the Shamir 2022 Data Availability Statement, the annotated catalog is provided "upon reasonable request" — NOT publicly redistributed. Surveyed (Phase 0): MNRAS supplementary materials (no data files), Zenodo (no deposit), author's institutional page (`assym_72k/` SDSS only, not DESI), GitHub (no `lshamir/desi_legacy` repo). See `data/shamir_2022/README.md` for detailed access audit.
- **Paper-quoted axes (Table 3)** used in this analysis:

| Data set | RA (deg) | Dec (deg) | sigma | RA 1sigma range | Dec 1sigma range | Galactic (l, b) |
|---|---|---|---|---|---|---|
| DESI Legacy Survey | 63 | -39 | 8.8 | -2 to 118 | 6 to -90 | (242.10, -46.91) |
| DECam | 57 | -10 | 4.7 | 22 to 92 | -39 to 56 | (199.19, -45.09) |
| SDSS | 69 | 56 | 4.6 | 19 to 107 | 25 to 77 | (150.75, 5.78) |
| Pan_STARRS | 47 | -1 | 1.9 | 4 to 117 | -73 to 40 | (180.12, -48.11) |

### 1.2 Sigma_Shamir derivation (per prereg sec 3.2)

The paper-quoted 1sigma uncertainty is an **asymmetric box in (RA, Dec)**, not a symmetric Gaussian-like sigma. Per the pre-registered procedure:
1. Uniform-sample (200 x 200 = 40000 points) the (RA, Dec) 1sigma box.
2. Convert each sample to galactic (l, b) via astropy `SkyCoord` ICRS->galactic.
3. Compute the undirected great-circle separation from the box-center (in galactic coords).
4. Take the 68% containment radius as sigma_galactic.

For DESI Legacy row:
- Equatorial 1sigma box: RA in [-2, +118], Dec in [-90, +6] (clipped to valid Dec range).
- Box center (galactic): (242.10, -46.91)
- **sigma_galactic 68% containment: 42.57 deg**
- sigma_galactic max-radius: 74.88 deg
- sigma_galactic median radius: 36.75 deg
- 1sigma-box-max / 68%-containment ratio: 1.76 (box is non-circular)

### 1.3 Cross-catalog separation + significance

For each pair of axes:
- Compute undirected angular separation (axis-line convention: (l, b) and (l+180, -b) equivalent).
- Compute sigma_combined = sqrt(sigma_A^2 + sigma_B^2).
- Separation in sigma_combined = separation / sigma_combined.

Adjudication per brief's outcome table:
- A (CATALOG-AGREE): separation < 1 sigma_combined
- C (CATALOG-DISAGREE): separation > 2 sigma_combined
- D (CATALOG-MARGINAL): 1 ≤ sep/sigma_combined ≤ 2
- E (CATALOG-METHODOLOGY): handled separately (E1 incomparability or E2 access-blocker)

### 1.4 Forward-prediction discipline (per `ave-driver-script-honesty` four-discriminator check)

All four discriminators PASS — see prereg sec 3.4 + driver `main()` upfront check:
1. Shamir's axis depends on AVE SDSS DR17 result? NO (Shamir published 2022-09; AVE C5 SDSS DR17 ran 2026-05-19; ~3.7 year publication-date independence).
2. Shamir's Q-cuts adjustable post-fit? NO (paper-pinned single published analysis pipeline).
3. Separation metric being minimized? NO (direct calculation, not optimization objective).
4. Result depends on choice of comparison axis? NO (both inputs are fixed prior to the comparison).

The cross-catalog comparison is a true forward-prediction validation, not a fit-to-target. **Trivially achieved precisely because Shamir's analysis preceded ours by 3.7 years — Shamir could not have tuned to match our SDSS DR17 axis.**

### 1.5 Constants used (per `ave-canonical-source`)

- `C_0` imported from `ave.core.constants` for stylistic consistency with the SDSS DR17 driver; not numerically used (pure angular-geometry test).
- No other canonical constants are load-bearing.

---

## 2. Numerical results

### 2.1 Primary adjudication (Shamir DESI Legacy vs AVE SDSS DR17)

| Metric | Value |
|---|---|
| AVE SDSS DR17 axis (l, b) | (129.00, 79.02) |
| AVE SDSS DR17 sigma | 6.83 deg |
| Shamir DESI Legacy axis (equatorial) | (RA=63, Dec=-39) |
| Shamir DESI Legacy axis (galactic) | (l=242.10, b=-46.91) |
| Shamir DESI Legacy axis (canonical 0 <= l < 180) | (l=62.10, b=+46.91) |
| Sigma_Shamir (68% containment radius in galactic) | **42.57 deg** |
| Sigma_Shamir max-radius | 74.88 deg |
| Sigma_Shamir median radius | 36.75 deg |
| Sigma_combined | **43.12 deg** |
| Separation (undirected axis) | **39.83 deg** |
| **Separation in sigma_combined** | **0.92 sigma** |
| **Decisive within 1 sigma?** | **YES (Outcome A)** |
| Decisive against (>2 sigma)? | NO |

### 2.2 Striking sub-finding: Shamir DESI vs CMB axis-of-evil

| Metric | Value |
|---|---|
| Shamir DESI Legacy axis (galactic) | (l=242.10, b=-46.91) |
| CMB axis-of-evil (Planck PR3 SMICA, E1b) | (l=60.28, b=50.48) |
| Sigma_CMB | 0.92 deg |
| Sigma_Shamir | 42.57 deg |
| Sigma_combined | 42.58 deg |
| **Separation (undirected)** | **3.77 deg** |
| Separation in sigma_combined | 0.09 sigma |

The Shamir DESI Legacy axis lies *very close* to the CMB axis-of-evil — only 3.77 deg apart. This is consistent with the framework's Observable 1 (CMB axis) and Observable 3 (LSS spin direction) being projections of the same `\hat{Omega}_freeze` direction.

**However, the AVE C5 SDSS DR17 axis at (129, 79) is 36.75 deg from the CMB axis-of-evil (Marginal-D outcome with 5.33sigma exclusion from CMB axis, per E1c).** Two LSS-spin axis re-fits using different methodologies on different imaging give DIFFERENT axes:
- AVE (Longo cos-gamma + GZ1 on SDSS DR7): axis 36.75 deg from CMB.
- Shamir 2022 (Ganalyzer + DESI Legacy): axis 3.77 deg from CMB.

**This is a methodology-systematic effect at the level of the LSS-axis-vs-CMB-axis cross-observable comparison.** The "same axis" interpretation per `omega-freeze-cosmic-grain-cascade.md:52` Observable 3 cascade prediction is supported BY Shamir's analysis and CONTRADICTED BY ours. Which methodology carries the systematic? The E1c result doc surfaces several candidates (GZ1 Hayes+2017 winding bias, the Lintott voting interface handedness asymmetry, sample-size noise on Longo's cos-gamma estimator). Shamir's Ganalyzer is purported to be parity-symmetric by construction.

### 2.3 Methodology-systematic probe (Shamir SDSS vs AVE SDSS DR17)

Same input galaxy population (SDSS-class spirals), DIFFERENT methodology + classifier:

| Metric | Value |
|---|---|
| AVE SDSS DR17 (GZ1 crowdsourced + Longo cos-gamma) | (l=129.00, b=79.02), sigma=6.83 |
| Shamir SDSS (Ganalyzer + SDSS DR8) | (l=150.75, b=5.78), sigma=23.83 |
| Sigma_combined | 24.79 deg |
| **Separation** | **74.04 deg** |
| **Separation in sigma_combined** | **2.99 sigma** |
| **Verdict** | **METHODOLOGY-SYSTEMATIC SURFACE** |

Two cosmological-axis re-fits of the SDSS-class galaxy population using two different methodologies disagree at ~3sigma. This is the structural finding that explains the Shamir-DESI-vs-AVE-SDSS-DR17 disagreement in direction (39.83 deg apart) AND the Shamir-DESI-vs-CMB-axis agreement (3.77 deg apart). The methodology difference DOMINATES the axis direction at SDSS precision.

### 2.4 Cross-survey comparisons (Shamir Table 3 other rows vs AVE SDSS DR17)

| Survey | Shamir axis galactic | Shamir sigma | Separation vs AVE SDSS DR17 | Outcome |
|---|---|---|---|---|
| DESI Legacy Survey | (242.10, -46.91) | 42.57 | 39.83 = 0.92 sigma | **A** |
| DECam | (199.19, -45.09) | 41.51 | 49.49 = 1.18 sigma | D |
| SDSS | (150.75, 5.78) | 23.83 | 74.04 = 2.99 sigma | **C** |
| Pan_STARRS | (180.12, -48.11) | 56.28 | 49.38 = 0.87 sigma | A |

**Cross-pipeline structure**: Shamir's DESI / DECam / Pan_STARRS axes are mutually consistent within their wide sigmas (centered ~(190, -47)) but Shamir's SDSS row is the outlier at (150, +6). The DECam and DESI are sub-analyses of the same DESI Legacy imaging at different focal-plane subsets — naturally consistent. Pan_STARRS is a different telescope at different wavelengths but Shamir's method puts its axis on the Pan_STARRS sky at (180, -48), close to the DESI center. Shamir's SDSS row, on the other hand, lands at (150, +6) — much closer to the celestial equator. This is consistent with the Pan_STARRS / DESI / DECam being predominantly southern-sky imaging and SDSS being predominantly northern-sky — the LSS dipole "lands where the survey's sky coverage allows it to be found".

### 2.5 Sub-finding: Shamir survey-coverage bias

The Shamir 2022 cross-survey axes all cluster near the survey-coverage center-of-density:
- DESI Legacy + DECam + Pan_STARRS: southern-sky imaging -> axes at galactic latitude ~-45 to -50.
- SDSS: northern-sky imaging -> axis at galactic latitude +6 (much closer to the SDSS-coverage center).

**Hypothesis (sub-finding for orchestration)**: Shamir's Ganalyzer is sensitive to a residual survey-coverage bias that the cos-gamma estimator's monopole-vs-dipole orthogonality is supposed to suppress. The dipole search MUST land somewhere on the sky, and if the data covers only one hemisphere, the maximum-significance direction tends to localize within (or anti-podal to) the covered hemisphere. This is a known SDSS / Pan_STARRS systematic discussed in Iye+2021 and (separately) Shamir's own work on Cosmic Principle anomalies.

The AVE SDSS DR17 estimator's randomization-null test (10000 random ±1 sign assignments) gave z = 29.8sigma significance for the (129, 79) axis — controlling for the SDSS-coverage anisotropy. The AVE axis is in the NORTHERN polar cap (b=79), well above the SDSS DR17 footprint center, which IS unusual for a survey-coverage-bias scenario. Shamir's SDSS axis at (150, +6) — also in the SDSS coverage — is more consistent with a coverage-localized "find the dipole within the data" behavior.

This sub-finding is a methodology-question, not an adjudication-changing finding. Orchestration / Grant decides whether to investigate further (e.g., by re-running the AVE driver with SDSS-coverage-matched random nulls).

---

## 3. Adjudication (per prereg sec 4)

**Pre-registered table:**

| Outcome | Criterion | This session |
|---|---|---|
| A (CATALOG-AGREE) | Shamir DESI vs SDSS DR17 separation within 1 sigma_combined | **MET — 39.83 = 0.92 sigma** |
| C (CATALOG-DISAGREE) | Separation > 2 sigma_combined | not met |
| D (CATALOG-MARGINAL) | 1 ≤ sep/sigma ≤ 2 | not met |
| E (CATALOG-METHODOLOGY) | Catalogs incomparable | E2 sub-finding active (catalog-access blocker; see sec 4.2 below) |

**Headline: Outcome A — CATALOG-AGREE.**

### 3.1 Outcome strength qualifier (per prereg sec 4.2 tie-breakers)

- **sigma_Shamir > 35 deg** -> precision-asymmetric regime: outcome label is **WEAK** because the cross-catalog separation precision is bottlenecked by Shamir's wide 1sigma box. The narrow AVE SDSS DR17 sigma (6.83 deg) is irrelevant to whether the comparison clears 1sigma_combined; sigma_combined ~ 43 deg is dominated by Shamir.
- 1sigma-box-max separation (74.88 deg) -> the box-corner samples reach ~75 deg from box-center; even an axis that lands 75 deg from Shamir's reported axis would be within Shamir's 1sigma uncertainty box. The cross-catalog separation must be quite large to clear Shamir's 1sigma criterion.
- All four pipeline tie-breakers met: pipeline didn't crash; outcome label is per primary pipeline (DESI Legacy); sub-survey rows logged as separate adjudications; methodology-probe (SDSS row) logged as sub-finding.

**Substantive content of the A label** (per Class E framing, prereg sec 3.7):
- The two cross-catalog re-fits are CONSISTENT with each other at the precision available. They do NOT contradict each other.
- BUT the consistency is at low informational depth: Shamir's wide sigma means almost any reasonable axis would also be Outcome A.
- The MORE LOAD-BEARING finding is the methodology-systematic surface (Shamir SDSS vs AVE SDSS DR17 at 2.99 sigma) — same data, different methods, ~3 sigma different axes.

### 3.2 E2 (catalog-access) sub-finding

Per prereg sec 4.1, the brief's Outcome E primary surface is decomposed into:
- E1 (incompatibility) — not triggered (Shamir's chirality convention matches GZ1; chirality observable is present).
- E2 (access blocker) — **ACTIVE**: Shamir 2022 per-galaxy CW/CCW classifications are not publicly redistributed.

**The E2 sub-finding does NOT change the primary outcome label A.** It DOES flag that the cross-catalog cross-validation depth is reduced — we trust Shamir's published axis without independent re-fit, Q-cuts variation, bootstrap diagnostics, or randomization-null. The primary outcome rests on a paper-quoted-axis comparison; full re-fit independence (which the brief's Phase 3 anticipated) is not achieved in this session's scope.

Resolution paths surfaced for orchestration (not executed this session):
1. **Author email contact** for catalog access (Shamir's data-availability statement says "upon reasonable request"; this would unblock a live-fire re-fit session).
2. **Live-fire Ganalyzer reproduction** on DECaLS imaging (multi-month effort; reproduces Shamir's algorithm from public methodology + does an independent classification).
3. **Retarget to McAdam & Shamir 2023** (Advances in Astronomy, "Reanalysis of the spin direction distribution of Galaxy Zoo SDSS spiral galaxies") if that catalog is publicly redistributed — would test the SDSS-imaging methodology systematic from a third angle.

### 3.3 Class E framing (per `consistency-vs-emergence` v1.1)

This is the same observable (LSS spin direction = Observable 3 of the Ω_freeze cascade) measured via two independent catalog+methodology paths. This is a **consistency check** — not an emergence-class test.

**Result-doc framing per Class E discipline:** the headline is "two catalog/methodology paths consistently report the LSS spin axis within 1 sigma joint uncertainty" — NOT "AVE prediction confirmed" or "consistency check passed at high precision". The framework's "same axis" prediction is supported (paths agree within their joint uncertainty); the precision of that support is sigma_combined ~ 43 deg, dominated by Shamir's wide sigma_Shamir.

Headline-by-comparison:
- E1c primary headline: "LSS spin axis vs CMB axis-of-evil = 36.75 deg = 5.33 sigma from zero — alignment EXCLUDED at 3 sigma."
- E1c (via Shamir's DESI axis) sub-headline: "Shamir 2022 DESI axis vs CMB axis-of-evil = 3.77 deg — well within sigma. Same observable (LSS spin direction) reported via different methodology gives different cross-observable significance against CMB."

This Class E classification is the LOAD-BEARING framework consequence:
- IF the framework's "same axis" prediction is right AND the two methodologies are unbiased, both methodologies should give the same axis -> the methodology-systematic at 2.99 sigma indicates one (or both) carries a directional bias.
- The cross-catalog validation (this session) IS consistent with the prediction (Outcome A), but at reduced informational depth.

---

## 4. Anomalies surfaced (per `flag-don't-fix`)

### 4.1 Brief citation typo (Shamir 2022 page range)

**Observation**: brief cites Shamir 2022 as "MNRAS 516:2204". Actual reference per author's institutional publication page + MNRAS DOI 10.1093/mnras/stac2372 is **MNRAS 516(2):2281-2291**. Page-number transcription error in brief drafting.

**Impact**: minor — the brief's intent was clear from context (Shamir 2022, DESI Legacy chirality, Ganalyzer). All citation links + DOI in this result doc and the data/shamir_2022/README.md point to the correct paper.

**Action**: surfaced for auditor lane. Suggested correction in `_orchestration/c5-shamir-2022-cross-catalog.md` line 3 + line 13 from "MNRAS 516:2204" to "MNRAS 516(2):2281-2291".

### 4.2 Shamir 2022 catalog access blocker

**Observation**: the per-galaxy CW/CCW classifications underlying Shamir's analysis are not in any public data archive. Data-availability statement reads "upon reasonable request" with corresponding-author contact.

**Impact**: structural — Phase 1 of the brief (catalog ingest with MD5 verification) cannot complete via public download. Phase 3 (live-fire driver) cannot run on Shamir's classifications.

**Adaptation**: pivoted to paper-quoted-axis comparison. Headline outcome (A) uses Shamir's Table 3; cross-catalog cross-validation depth is reduced as documented in sec 3.2 E2.

**Action**: surfaced for orchestration adjudication. Three resolution paths in sec 3.2 above.

### 4.3 Methodology-systematic surface at SDSS level

**Observation**: Shamir's SDSS row (Ganalyzer + SDSS DR8) reports LSS axis at (l=150.75, b=5.78), sigma=23.83. AVE SDSS DR17 (Longo cos-gamma + GZ1 + SDSS DR7) reports axis at (l=129, b=79), sigma=6.83. Separation 74.04 = 2.99 sigma_combined.

**Impact**: cross-methodology disagreement at ~3sigma on the same broad input galaxy population. The "LSS spin axis" observable is methodology-dependent at this level.

**Mechanism candidates**:
1. **GZ1 Hayes+2017 winding bias** (already noted in E1c result sec 4.2): the per-galaxy clockwise/anticlockwise vote asymmetry is ~3% in GZ1. The dipole search is in principle orthogonal to this monopole; could be 2nd-order coupling effects?
2. **Shamir Ganalyzer survey-coverage interaction**: hypothesis in sec 2.5 above. The cross-pipeline axis structure in Shamir Table 3 (3 out of 4 surveys cluster near (190, -47)) is suggestive.
3. **Sample-size noise on Longo cos-gamma**: the 63k AVE GZ1 subset is smaller than Shamir's ~170k SDSS DR8. But the random-null z=29.8sigma indicates the AVE result is well above statistical noise.
4. **Different sky coverage**: AVE's GZ1 footprint is SDSS DR7; Shamir's SDSS row is DR8 (covers DR7 + LSST extension). Marginal sky-coverage differences could matter for an axis near b=+79 (north galactic pole) vs an axis near b=+6 (galactic disk).

**Action**: surfaced as sub-finding for orchestration. NOT silently resolved. The cross-methodology question deserves either (a) a Shamir-DR8-on-GZ1-coverage controlled re-analysis, or (b) Grant adjudication on whether the Longo cos-gamma OR the Ganalyzer is methodology-preferred (e.g., based on parity-symmetry-by-construction arguments).

### 4.4 Shamir DESI vs CMB axis: 3.77 deg agreement

**Observation**: Shamir 2022 DESI Legacy axis (galactic 242, -47) lands within 3.77 deg of the CMB axis-of-evil (galactic 60, 50). The 3.77 deg is small in absolute terms — much smaller than the Planck σ_CMB = 0.92 deg combined with Shamir's σ ~ 42.

**Impact**: SUPPORTIVE of the framework's "same axis" prediction (per `omega-freeze-cosmic-grain-cascade.md:52` Observable 1 = Observable 3). HOWEVER:
- This support is at low precision (Shamir's sigma is wide).
- It CONTRADICTS our own SDSS DR17 finding (CMB-LSS = 5.33 sigma from zero per E1c).
- Either Shamir's methodology is correct (and AVE's SDSS DR17 result carries a directional methodology bias) OR AVE's result is correct (and Shamir's wide sigma masks a methodology systematic AT the central direction).

**Action**: NOT framed as "AVE prediction confirmed" (per Class E discipline + sec 3.3 framing). Framed as "Shamir 2022 supports the framework's same-axis prediction at low precision; AVE SDSS DR17 contradicts it at high precision". Orchestration / Grant adjudicates the cross-methodology question.

---

## 5. ave-discrimination-check (conditional on Outcome A)

Per prereg sec 6 conditional, fires `ave-discrimination-check` when Outcome A is reached.

### 5.1 SM-counterfactual

**Standard Model + ΛCDM prediction for cosmic galaxy-spin-axis dipole**: isotropic at large scales (per the cosmological principle). No preferred direction. Any reproducible 1sigma agreement between two cosmic-axis observables in the same direction is a NOVELTY for ΛCDM.

**This session's Outcome A** (Shamir DESI vs AVE SDSS DR17 within 1 sigma_combined): consistent with both:
- The framework's "same axis" prediction (Observables 1 and 3 of the Ω_freeze cascade), AND
- The null hypothesis of methodology-determined-but-wide-sigma cross-catalog noise (Shamir's wide sigma of 42.57 deg is so wide that almost any axis-pair would be within 1 sigma).

The Outcome A label does NOT discriminate the framework from null at the precision available.

**Sub-finding cross-observable** (Shamir DESI 3.77 deg from CMB): IF this were the load-bearing direction (i.e., Shamir's wide sigma is the right characterization of methodology uncertainty), it WOULD discriminate the framework from null. The framework predicts CMB-LSS within sigma; null predicts random direction. 3.77 / 42.58 = 0.09 sigma_combined — consistent with same-direction. But the precision-asymmetry between sigma_CMB=0.92 and sigma_Shamir=42.57 means this "same direction" statement is dominated by Shamir's wide sigma.

### 5.2 Interpretive alternatives

The Outcome A result is consistent with:

1. **AVE framework as written**: Observables 1 and 3 of the Ω_freeze cascade project to the same `\hat{Omega}_freeze` axis; both Shamir's and AVE's analyses sample this direction with methodology-specific noise/bias.

2. **Parity-violating inflationary cosmology (e.g., Alexander+, Cai+, Kim+, Naselsky+)**: a leptogenesis-class scenario produces a global parity asymmetry in the cosmic spin direction. ΛCDM-compatible if the parity violation enters at high-energy inflationary scale; not framework-distinct from AVE without an a priori predicted direction.

3. **Survey-coverage-systematic with cosmic-noise null**: Shamir's wide sigma reflects the underlying cosmic isotropy (no preferred direction at survey scales). The 3.77 deg "alignment" with CMB axis IS coincidence within Shamir's 42.57 deg sigma. Null hypothesis preserved.

4. **Coherent observational systematic (CMB axis + LSS axis both biased to same direction by a shared instrumental/foreground effect)**: less plausible given CMB and SDSS use entirely different instruments + sky bands + observational physics.

**Discrimination verdict**: Outcome A is consistent with both AVE-distinct (option 1, 2) and null (option 3). The 1sigma agreement does NOT decisively select between them given Shamir's wide sigma.

This is the "AVE-distinct framing requires more precision than Outcome A provides" conclusion. The framing in sec 0 TL;DR says "CATALOG-AGREE — BUT outcome strength is weak (precision-asymmetric)". The framework-strength language is NOT "AVE prediction confirmed" or "consistency-check passed decisively" — it is "cross-catalog cross-validation consistent at the precision available".

---

## 6. Cascade implications

### 6.1 C5 row update

`manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428, 514, 554, 907 + Mermaid chart at 907:
- Status: Marginal-D held + cross-catalog sub-finding: Shamir 2022 DESI Legacy axis at (l=242, b=-47), sigma~42.5 deg from asymmetric 1sigma box, separation from AVE SDSS DR17 = 39.83 deg = 0.92 sigma_combined -> Outcome A (CATALOG-AGREE, weak precision).
- Sub-finding: Shamir DESI vs CMB axis-of-evil = 3.77 deg (close to "same axis" prediction at LOW precision).
- Sub-finding: methodology-systematic surface at SDSS level (Shamir SDSS row vs AVE SDSS DR17 at 2.99 sigma).
- E2 sub-finding: catalog-access blocker (Shamir's catalog not publicly redistributed) — paper-quoted comparison only.

### 6.2 Closure-roadmap entry

New entry in `manuscript/ave-kb/claim-quality-closure-roadmap.md` documenting:
- The cross-catalog validation outcome (Outcome A weak).
- The methodology-systematic surface (3 sigma at SDSS level).
- The catalog-access blocker (E2 sub-finding).
- The Shamir-DESI-vs-CMB-axis alignment within Shamir's wide sigma (3.77 deg).

### 6.3 Ω_freeze 8-observable cascade

`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:52` currently reads (per the SDSS DR17 result update):

> | 3 | LSS spin direction | Same axis | SDSS galaxy spin axes (~1-2σ preferred direction, contested)

The "contested" qualifier IS now further substantiated: the cross-catalog test shows methodology-dependence at ~3sigma. The SAME observable, measured by two methodologies, lands at axes 39.83 deg apart. The framework's "same axis" prediction is consistent with Shamir's methodology and contradicted by AVE's SDSS DR17 methodology — the contestedness is NOT resolved by this session.

Walk-back propagation NOT applied this session (consistent with E1c's framing: Marginal-D + sub-finding stay surfaced, propagation requires Grant adjudication on threshold-policy + methodology-bias direction).

### 6.4 E1c (Route 3 framework-commitment activation)

Stays DEFERRED. The cross-catalog Outcome A is at low informational depth (precision-asymmetric), so it does not clear the un-defer trigger (3sigma-decisive A or C with both axes at comparable precision). The methodology-systematic surface (3 sigma) raises the QUESTION of which methodology dominates the substrate-physical interpretation; orchestration / Grant adjudicates before E1c can advance.

### 6.5 Next-session priorities

In priority order:

1. **Methodology-systematic adjudication** (highest priority, Grant decision): which methodology is preferred for the LSS spin-axis test? Ganalyzer (algorithmic, parity-symmetric-by-construction) OR Longo cos-gamma (crowdsourced ±1, monopole-orthogonal but small-sample-noise sensitive)? This is a plumber-physical question: which estimator's directional bias is smaller? The answer informs whether the AVE SDSS DR17 axis at (129, 79) OR Shamir's DESI axis at (242, -47) is the load-bearing measurement of `\hat{Omega}_freeze`'s LSS projection.

2. **Author email contact for Shamir 2022 catalog** (1-2 weeks roundtrip): unblock a future-session live-fire re-fit on Shamir's per-galaxy classifications. Would convert the current E2 sub-finding into a full A/C/D adjudication at comparable cross-catalog precision.

3. **Joint Pantheon+ + SDSS DR17 + Shamir-DESI constraint** (Option B from SDSS DR17 brief; 1-2 sessions): with three cosmic-axis observables, the consensus / disagreement structure becomes a 3D problem. Hubble flow (Pantheon+) at (129.76, -13.64) + AVE SDSS DR17 (129, 79) + Shamir DESI (242, -47) — joint analysis could surface which two-out-of-three pair-agree, identifying the most likely odd-one-out methodology systematic.

4. **McAdam & Shamir 2023 cross-comparison** (separate session if catalog publicly redistributed): "Reanalysis of the spin direction distribution of Galaxy Zoo SDSS spiral galaxies" — would test whether Shamir's methodology applied to GZ1 (the SAME data AVE uses) gives the same axis as AVE's Longo-cos-gamma, OR Shamir's Ganalyzer axis (which would prove the methodology is the dominant variable, not the catalog).

5. **Live-fire Ganalyzer reproduction** (multi-month effort): reproduces Shamir's algorithm on the DECaLS imaging from scratch. Highest cost, highest independence-of-implementation depth. Defer unless steps 1-4 do not resolve the methodology question.

---

## 7. Skill / discipline attestation

- **Pre-registration** [`research/2026-05-19_c5-shamir-2022-cross-catalog-prereg.md`](2026-05-19_c5-shamir-2022-cross-catalog-prereg.md): frozen 2026-05-19 BEFORE any comparison statistics computed; this result doc executes the pre-registered methodology.
- **Forward-prediction discipline** (ave-driver-script-honesty 4-discriminator): all four PASS — see sec 1.4 + driver main() upfront check.
- **Consistency-vs-emergence v1.1**: Class E classified per prereg sec 3.7; result-doc framing per Class E discipline applied at sec 0 TL;DR + sec 3.3 (no "AVE prediction confirmed" headline; framed as "cross-catalog cross-validation consistent at precision available").
- **Flag-don't-fix**: brief citation typo (sec 4.1) + catalog-access blocker (sec 4.2) + methodology-systematic surface (sec 4.3) + Shamir-DESI-vs-CMB 3.77 deg agreement (sec 4.4) all surfaced, NOT silently corrected.
- **Verify-before-cite v1.3**: trigger 1 (content) applied to Shamir 2022 paper text via MNRAS HTML + DOI verification; trigger 7c (cross-branch state) applied to worktree HEAD; trigger 8 (commit application) verified branch tip at `588e069`.
- **Empirical-driver discipline (Rule 10)**: driver ran end-to-end at first attempt with all pre-registered comparisons converging cleanly. No rationale-text bugs. JSON output 9.7 KB written successfully.
- **ave-discrimination-check** (conditional on Outcome A): applied at sec 5 — SM-counterfactual + interpretive-alternatives — discrimination verdict is "Outcome A consistent with both AVE-distinct and null at precision available; no decisive selection".
- **Class E result-doc framing**: sec 3.3 above.

---

## 8. Result-doc freeze attestation

**This result doc records the live-fire driver execution of 2026-05-19 against the frozen prereg.** Numerical values come directly from `c5_shamir_2022_spin_orientation_results.json` (9.7 KB written by `c5_shamir_2022_spin_orientation.py:main()`). Any subsequent re-runs that produce different numerical values require an explicit "RESULT-UPDATE" entry with both old and new values; per `ave-driver-script-honesty`, hypothesis-favorable post-hoc parameter adjustments are not permitted.

---

*End of result.*
