# C5-CMB-AXIS Shamir 2022 Cross-Catalog Validation — Execution-Session Pre-Registration

**Date:** 2026-05-19
**Branch:** `analysis/c5-shamir-2022-cross-catalog` off `analysis/integration` at `588e069`
**Status:** EXECUTION-SESSION PRE-REGISTRATION. Frozen BEFORE comparison statistics are computed against headline outcome. Subordinate to the frozen 2026-05-15 A-034 methodology prereg at [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md).

**Briefing:** [`_orchestration/c5-shamir-2022-cross-catalog.md`](../_orchestration/c5-shamir-2022-cross-catalog.md) — retargets the GZ-DECaLS Outcome-E goal to Shamir 2022 (MNRAS 516(2):2281).

**Predecessors:**
- E1b session: [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md) — Outcome D; CMB axis at (l=60.28, b=50.48), sigma=0.92.
- E1b-prime session: [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md) — Outcome Marginal-D; sigma_Hubble 30 -> 24.
- E1c (SDSS DR17) session: [`research/2026-05-19_c5-sdss-spin-orientation-result.md`](2026-05-19_c5-sdss-spin-orientation-result.md) — Outcome Marginal-D + substantive: LSS axis (l=129, b=79) sigma=6.83, CMB-LSS = 36.75 at 5.33 sigma from zero.
- C5 GZ-DECaLS scoping: [`research/2026-05-19_c5-gz-decals-spin-orientation-scoping.md`](2026-05-19_c5-gz-decals-spin-orientation-scoping.md) — Outcome E (chirality observable absent from Walmsley+2022 catalog); identified Shamir 2022 as the retarget candidate in §5.

---

## 1. Pre-registration target

**Test:** independently verify the cosmic galaxy-spin-axis dipole direction derived in the AVE C5 SDSS DR17 epic (l=129, b=79, sigma=6.83 via Longo cos-gamma estimator on Galaxy Zoo 1 + SDSS DR7) against the Shamir 2022 (MNRAS 516(2):2281) result on the DESI Legacy Imaging Survey (~1.287 million spiral galaxies, Ganalyzer algorithmic chirality, DECaLS DR8 + BASS + MzLS imaging). Adjudicate against the pre-registered cross-catalog outcome table (A / C / D / E) below.

The empirical question (per brief): does Shamir 2022 (Ganalyzer on DECaLS DR8) independently recover the SDSS DR17 spin axis at (l=129, b=79), sigma=6.83 within combined uncertainty?

**Out of execution scope** (this session): re-running the Ganalyzer algorithm on the DECaLS imaging to validate Shamir's catalog from scratch (multi-week effort, Outcome-E branch of brief constraint table; see §2.5 below for the access blocker discovered Phase 0). Joint Pantheon+ + SDSS DR17 + Shamir-DESI constraint (separate Option B follow-up if needed).

---

## 1.5. Picture-first (plumber-physical framing)

**Plumber-physical picture:** the Omega-freeze cosmic-grain cascade (per [`omega-freeze-cosmic-grain-cascade.md:52`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)) predicts that the parent black hole's spin axis was imprinted on the cosmic-scale K4 lattice at the lattice's saturation event (Ax 1 chiral I4_1 3 2 space-group; bond-bowing direction locked at lattice genesis). Eight observables project this single underlying direction `\hat{Omega}_freeze`:
- Obs 1: CMB axis-of-evil (empirically at (l=60.28, b=50.48), sigma=0.92, E1b)
- Obs 3: LSS spin direction (SDSS DR17 at (l=129, b=79), sigma=6.83, E1c — same observable channel, different sky tracer)
- Obs 2, 4, 5, 6, 7, 8: other tracers

If two independent observational channels report the same `\hat{Omega}_freeze`, they should project to consistent axis directions within their joint uncertainty. If they don't, EITHER the framework's "same axis" prediction is wrong, OR one (or both) catalogs carry a methodology-specific systematic that rotates the apparent direction.

The C5 SDSS DR17 result (Marginal-D + substantive: CMB-LSS = 5.33sigma from zero) raised the methodology question: is the 36.75-degree CMB-LSS separation reflecting a substrate-physical mismatch between Observable 1 and Observable 3, OR a catalog-systematic in GZ1 / Lintott classification / Longo cos-gamma estimator? The cross-catalog test of this session asks: when an INDEPENDENT method (Ganalyzer vs crowdsourced GZ1 vote) on INDEPENDENT imaging (DECaLS DR8 vs SDSS DR7) finds an LSS axis, does it land at our (l=129, b=79) (independent corroboration of E1c) or somewhere else (catalog systematic)?

**Why this is structurally non-circular** (per brief Grant adjudication): Shamir 2022's analysis was published 2022-09 — entirely independent of, and pre-dating, the AVE C5 SDSS DR17 session of 2026-05-19. Shamir had no access to our axis result. The cross-catalog comparison cannot leak our SDSS DR17 axis backward into Shamir's analysis.

**Convention compatibility verified** (per brief Phase 1 instruction): Shamir 2022 §2 states chirality is determined "as viewed from Earth" — clockwise = positive slope in radial intensity peak regression, counterclockwise = negative slope. Galaxy Zoo 1 (Lintott+2011) uses the same Earth-viewing-the-image perspective. NO convention flip between catalogs. If conventions had been opposite, the apparent axis would flip by 180 degrees in axis-line representation, but the canonical undirected-axis comparison handles this automatically; an actual physical opposite-handedness convention would still be detected by the cross-axis separation.

---

## 2. Verified state pre-execution (per `verify-before-cite` v1.3)

Phase 0 verifications confirmed at session start:

### 2.1 Worktree + branch state (trigger 7c + 8)
- Worktree HEAD: `588e069 docs(_orchestration): 3 parallel Session 2 / new-epic briefs ready for parallel spawns` (matches brief's stated starting tip).
- Branch `analysis/c5-shamir-2022-cross-catalog` created from `origin/analysis/integration` at `588e069`.
- Pre-execution `git status`: clean. Working directory matches `588e069` tree.

### 2.2 Citation verification (trigger 1)
**ANOMALY SURFACED — see §2.5 below**: brief cites Shamir 2022 as **MNRAS 516:2204**. Actual MNRAS reference per author's institutional publication page + DOI 10.1093/mnras/stac2372: **MNRAS 516(2):2281-2291**. The brief's "2204" appears to be a citation transcription error from the orchestration doc; the actual page range is 2281-2291.

The full title and venue are: **Shamir, L., 2022, "Analysis of spin directions of galaxies in the DESI Legacy Survey", Monthly Notices of the Royal Astronomical Society, 516(2):2281-2291.**

### 2.3 Catalog availability check (trigger 1 + 3)
Surveyed all standard public data sources:
- **MNRAS supplementary materials** for DOI 10.1093/mnras/stac2372: no data files released. Paper's Data Availability Statement: "Annotated DESI Legacy Survey data will be provided upon reasonable request" (corresponding author lshamir@mtu.edu).
- **Zenodo**: no Shamir 2022 DESI catalog deposit identified.
- **Author's institutional page** <https://people.cs.ksu.edu/~lshamir/data/>: only `assym_72k/` (Iye et al. 2021 reproduction SDSS dataset, NOT the 1.287M DESI catalog).
- **GitHub**: no `lshamir/desi_legacy` repository identified.

**CONSEQUENCE**: the brief's Phase 1 (catalog ingest with MD5 verification + Q-cuts methodology + driver re-fit on the catalog) is **NOT REACHABLE** in this single-session scope. The catalog cannot be downloaded; the per-galaxy CW/CCW classifications that Shamir derived are not publicly redistributed. This is a structural blocker — **PARTIAL OUTCOME-E surface** of the brief's table — analogous to the GZ-DECaLS scoping session's discovery that Walmsley+2022 has no chirality observable at all. The two Outcome-E branches differ:
- GZ-DECaLS: chirality observable absent from catalog (no observable to compare).
- Shamir 2022: chirality observable PRESENT and methodology compatible, BUT the per-galaxy classifications are not in the public data release. Only the paper's headline (axis position + asymmetric 1sigma box) is accessible.

### 2.4 Paper-quoted results (extracted via `verify-before-cite` v1.3 trigger 1)
Per Shamir 2022 Table 3, the published axis positions + asymmetric 1sigma uncertainty boxes are:

| Data set | RA (deg) | Dec (deg) | sigma | RA 1sigma range | Dec 1sigma range | Galactic (l, b) |
|---|---|---|---|---|---|---|
| DESI Legacy Survey | 63 | -39 | 8.8 | -2 to 118 | 6 to -90 | (242.10, -46.91) |
| DECam | 57 | -10 | 4.7 | 22 to 92 | -39 to 56 | (199.19, -45.09) |
| SDSS | 69 | 56 | 4.6 | 19 to 107 | 25 to 77 | (150.75, 5.78) |
| Pan-STARRS | 47 | -1 | 1.9 | 4 to 117 | -73 to 40 | (180.12, -48.11) |

Equatorial -> galactic transformations performed via `astropy.coordinates.SkyCoord` ICRS->galactic with default frame definitions (precession-aware, equinox J2000).

### 2.5 Anomalies surfaced (flag-don't-fix)

**Anomaly 1 (citation typo)**: brief cites "MNRAS 516:2204" — actual is MNRAS 516(2):2281-2291. Mechanism: page-number transcription error in brief drafting. Action: NOT silently corrected (orchestration may have intentionally cited at the brief's level of fidelity). Surfaced for auditor lane.

**Anomaly 2 (catalog access)**: catalog is not publicly downloadable. Mechanism: Shamir 2022 data-availability statement excludes the per-galaxy classifications from public release; only the paper's analysis output (axis, asymmetric 1sigma box, sigma=8.8) is published. Action: **scope-pivot** — instead of catalog re-fit, this session executes a **paper-quoted-axis comparison** with explicit Outcome-E sub-finding for the access blocker. Surfaced for orchestration adjudication on whether to:
  (a) accept paper-quoted comparison as the cross-catalog validation deliverable (this session's pivot), OR
  (b) escalate to multi-session via author email contact + extended scope, OR
  (c) drop the Shamir 2022 specific target and retarget to McAdam & Shamir 2023 (Advances in Astronomy, "Reanalysis of the spin direction distribution of Galaxy Zoo SDSS spiral galaxies") if that catalog is publicly redistributed.

### 2.6 Corpus-grep findings (per `ave-prereg`)
- AVE-Core: 45 hits for "Shamir / Ganalyzer / DECaLS DR8 / MNRAS 516"
  - All in research preregs/results docs, the SDSS DR17 result doc §4.3 cross-pipeline-consistency discussion, KB closure-roadmap entries, and the cosmology translation-table. No prior estimator code targeting Shamir 2022 specifically.
- AVE-PONDER, AVE-HOPF, AVE-QED, AVE-APU, AVE-Metamaterials, AVE-Protein, AVE-Engineering, AVE-Manifold, AVE-Cosmology: 0 hits each.
- **Conclusion**: this is the first cross-catalog validation against Shamir 2022 in the AVE corpus. Methodology must be pinned in detail in this prereg.

---

## 3. Cross-catalog comparison specification (PINNED BEFORE COMPARISON STATISTICS)

### 3.1 Comparison axes (load-bearing)

| Source | Axis (l, b) | sigma | Method |
|---|---|---|---|
| AVE SDSS DR17 (E1c) | (129.00, 79.00) | 6.83 | Longo cos-gamma on GZ1; Hessian-MC + bootstrap |
| Shamir 2022 DESI Legacy | (242.10, -46.91) | TBD (see §3.2) | Ganalyzer + chi-square grid; MC randomization 1000x |
| CMB axis-of-evil (E1b) | (60.28, 50.48) | 0.92 | Planck PR3 SMICA, max-angular-momentum-dispersion |

### 3.2 sigma_Shamir derivation (from Shamir's asymmetric 1sigma box)

Shamir 2022 reports the 1sigma axis uncertainty as an **asymmetric rectangle in (RA, Dec)**, not a symmetric Gaussian-like sigma value. The brief asks for "sigma_Shamir achieved" — this requires converting the (RA, Dec) rectangle into a galactic-coordinate angular containment radius. The conversion procedure (PINNED BEFORE COMPUTATION):

1. Sample a uniform grid of (RA, Dec) points inside the asymmetric box: RA in [-2, +118], Dec in [-90, +6] (Shamir DESI row of Table 3).
2. Convert each sample to galactic (l, b) via `astropy.SkyCoord` ICRS->galactic.
3. For each sample, compute the undirected great-circle angular separation from the box-center (RA=63, Dec=-39) -> galactic (242.10, -46.91).
4. **Canonical sigma_Shamir** = the 68% containment radius of this distribution.

Rationale: a 2D chi-square contour at 68% confidence in (RA, Dec) — which is what Shamir 2022's asymmetric box represents — maps to a (potentially asymmetric and non-circular) region in galactic (l, b). The 68% containment radius is the natural single-scalar summary of the 1sigma uncertainty in galactic angular space; it conservatively absorbs the projection-induced asymmetry.

### 3.3 Cross-catalog separation + significance

For each pair of axes, compute the undirected angular separation (axis-line convention: (l, b) and (l+180, -b) equivalent, take closer-of-the-two). The Shamir-DESI vs SDSS-DR17 separation is the primary load-bearing quantity.

Significance: 
- separation / sigma_combined where sigma_combined = sqrt(sigma_SDSS_DR17^2 + sigma_Shamir^2)
- Adjudication uses this single-scalar significance against the brief's pre-registered outcome table (§4 below).

### 3.4 Forward-prediction discipline (per `ave-driver-script-honesty` four-discriminator check)

1. **Does Shamir's published axis depend on our SDSS DR17 result?** NO. Shamir 2022 was published 2022-09; AVE C5 SDSS DR17 session ran 2026-05-19. Shamir's analysis was prior-to-and-independent-of our result by ~3.7 years.
2. **Are Shamir's Q-cuts / classification choices biased toward our axis?** NO. Shamir's Ganalyzer pipeline + 30-peak threshold + chi-square integer grid were locked into a single published analysis pipeline, unmodified for the C5 cross-catalog test.
3. **Is the comparison metric `|n_Shamir - n_SDSS|^2` being minimized?** NO. We compute the separation as a direct measurement, not an objective function for any optimization.
4. **Does the result depend on the comparison axis we chose to compare to?** NO. Shamir's axis was published with a paper-pinned 1sigma uncertainty; our SDSS DR17 axis was published with the E1c session's empirical fit. Both are fixed inputs; the comparison is a calculation on those fixed inputs.

**All four discriminators pass.** The comparison is a true cross-catalog validation, not a fit-to-target.

### 3.5 Substrate-native check (per `substrate-native-check` skill)
This is a pure angular-statistics comparison on two pre-existing published axis results. No continuum-field simulation, no K4 / Cosserat / Op14 saturation kernel, no eigsolver. The substrate-native layer enters the prediction (each axis is a projection of `\hat{Omega}_freeze` per the cascade) but not the comparison.

### 3.6 Phase-space coordinate check (per `phase-space-coordinate-check` skill)
Both axes are reported in galactic (l, b). Shamir's published values are in equatorial (RA, Dec) — converted to galactic via the canonical astropy ICRS->galactic transform for the comparison. No real-space ↔ phase-space conversion needed.

### 3.7 Consistency-vs-emergence classification (per `consistency-vs-emergence` v1.1)

**Class E** (operating-point projection / topological-equilibrium observable).

Justification: this is the same observable (LSS spin direction = Observable 3 of the cascade) measured via two independent catalog+methodology paths. The framework's prediction is "same axis as `\hat{Omega}_freeze`", manifesting through both observation channels. This is a **consistency check across catalogs** within Observable 3, layered on top of the consistency check across observables (Observable 3 vs Observable 1) that the SDSS DR17 result already executed.

This is NOT an emergence-class test (we are not deriving `\hat{Omega}_freeze` from substrate axioms). Result-doc framing per Class E discipline:
- A (catalog-agree): "two catalog/methodology paths consistently report the same axis, strengthening the cross-catalog robustness of the LSS-spin-direction observable."
- C (catalog-disagree): "two catalog/methodology paths report substantially different axes — one (or both) carry methodology-specific systematics; cross-observable interpretation (CMB-LSS comparison) needs caveating."

Both outcomes are CONSISTENCY-CHECK conclusions; neither is "AVE prediction confirmed" or "AVE prediction falsified" headlined.

---

## 4. Adjudication mapping (pre-registered, per brief's outcome table)

| Outcome | Criterion | Action |
|---|---|---|
| **A (CATALOG-AGREE)** | Shamir DESI vs SDSS DR17 separation within 1sigma_combined | C5 row: LSS-axis cross-catalog robust; operator-output framing strengthened; cascade interpretation methodology-independent. |
| **C (CATALOG-DISAGREE)** | Shamir DESI vs SDSS DR17 separation > 2sigma_combined | C5 row: methodology systematic dominates; SDSS DR17 axis interpretation needs caveating (the cross-catalog confirmation requirement is the implicit interpretive backbone). |
| **D (CATALOG-MARGINAL)** | 1sigma_combined ≤ separation ≤ 2sigma_combined | C5 row: both results valid with explicit methodology-uncertainty acknowledged; cross-catalog cross-validation incomplete. |
| **E (CATALOG-METHODOLOGY)** | Catalogs incomparable (chirality convention mismatch, or catalog access surface) | Escalate to orchestration BEFORE retry. |

### 4.1 Pre-registered outcome handling for the catalog-access blocker (per brief constraint table)

The brief's outcome E surface is partially activated by the Phase 0 finding (§2.3, catalog not publicly downloadable). Two sub-paths within Outcome E:

- **E1 (catalog-methodology incomparable)**: chirality convention mismatch, observable absence, etc. NOT triggered — convention matches GZ1, chirality observable is present.
- **E2 (catalog-access blocker)**: chirality observable exists with matching convention, but per-galaxy data not in public release; only paper-quoted axis + asymmetric 1sigma box accessible.

**This session adjudicates against the brief's primary outcome table A/C/D using the paper-quoted comparison, AND surfaces the E2 sub-finding for orchestration adjudication.** The final adjudication label is the A/C/D primary outcome from the paper-quoted comparison; the E2 sub-finding is logged as a separate cross-cutting note (does not block primary adjudication but flags reduced cross-catalog depth — we trust Shamir's published axis without independent re-fit).

This dual-adjudication is structurally analogous to the SDSS DR17 result's "Marginal-D + substantive CMB-LSS = 5.33sigma exclusion" finding pattern: primary outcome from pre-registered table + sub-finding that is non-load-bearing for label but substantive for orchestration decision-making.

### 4.2 Tie-breakers (pre-registered)

- If sigma_Shamir > 35 (Shamir's 1sigma box mapped to galactic), the comparison is sigma_Shamir-dominated; flag as sub-finding that the cross-catalog separation precision is bottlenecked by Shamir's published uncertainty, not our SDSS DR17 precision.
- If sigma_Shamir < 10, the comparison precision is symmetric; report both pipeline sigmas + the joint.
- If the 1sigma-box-corner-max-separation exceeds 50, flag that Shamir's box is so wide that almost any direction agrees within 1sigma_combined; the outcome label A in this regime is **weak** (consistent-with-prediction but not informative-as-cross-validation).
- If the (RA, Dec) box samples include points where Dec is outside [-90, +90] (impossible), clip to valid Dec range and log as a sub-finding.

---

## 5. Files to produce

- `src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation.py` — comparison driver implementation (paper-quoted axes + asymmetric-box-to-galactic projection + cross-catalog separation calculation)
- `src/scripts/vol_3_macroscopic/c5_shamir_2022_spin_orientation_results.json` — full numeric output
- `data/shamir_2022/README.md` — canonical catalog reference with metadata + paper-quoted Table 3
- `research/2026-05-19_c5-shamir-2022-cross-catalog-prereg.md` — this document
- `research/2026-05-19_c5-shamir-2022-cross-catalog-result.md` — result doc + cross-catalog matrix
- Updates (in scope):
  - `manuscript/ave-kb/common/divergence-test-substrate-map.md` C5 row(s) — add Shamir 2022 cross-catalog sub-finding
  - `manuscript/ave-kb/claim-quality-closure-roadmap.md` — new entry for cross-catalog C5 sub-result

Out of scope this session:
- Modifying `cmb_axis_alignment_executable_observer.py` corpus pins (the (52, 68.5) Longo pin was previously walked back to the empirical (129, 79) per analysis/c5-corpus-pin-fix; that file is unchanged this session)
- Joint Pantheon+ + SDSS DR17 + Shamir-DESI constraint (Option B follow-up; conditional on this session's outcome)
- McAdam & Shamir 2023 cross-comparison (separate cross-catalog session if needed)
- Live-fire Ganalyzer reproduction on DECaLS imaging (multi-week effort; out of single-session scope)

---

## 6. Skill discipline applied this session

**Upfront (Phase 0):**
- `pre-test-physics-check` — DONE (brief instructed to verify chirality convention before catalog ingest; convention matches; the structural blocker that materialized was catalog access, not methodology incompatibility).
- `ave-prereg` — corpus-grep complete (§2.6 corpus-grep findings; 45 AVE-Core hits all in research/KB context; no prior estimator code).
- `ave-canonical-leaf-pull` v1.2 — data-fitting class (LSS-direction problem); canonical leaves already enumerated by the SDSS DR17 prereg. Triggers 1-13 for data-fitting class re-applied without new leaves required.
- `ave-canonical-source` — confirmed no Avenir constants are load-bearing for this geometric test; `C_0` import retained for stylistic consistency with the SDSS DR17 driver but not used in any computation.
- `verify-before-cite` v1.3 — trigger 1 (content) applied to Shamir 2022 paper text via MNRAS HTML + DOI verification; trigger 7c (cross-branch state) applied to worktree HEAD + SDSS DR17 result location; trigger 8 (commit application) verified branch tip matches brief's stated `588e069`.
- `substrate-native-check` — checked (§3.5); no continuum-field machinery needed.
- `phase-space-coordinate-check` — checked (§3.6); both axes in galactic via standard ICRS->galactic transformation.
- `consistency-vs-emergence` v1.1 — Class E classified (§3.7); result-doc framing discipline pre-committed.

**Conditionally (will fire at named gates):**
- `ave-driver-script-honesty` — four-discriminator check captured in §3.4; re-confirm before running driver.
- `ave-discrimination-check` — IF outcome A (catalog-agree), apply SM-counterfactual + interpretive-alternatives. SM has no a priori cosmic spin-axis prediction; ΛCDM expects galaxy spin axes to be isotropic at large scales (per cosmological principle). A 1sigma-consistent cross-catalog axis-correlation would be a novel anomaly for ΛCDM, but only "AVE-distinct" if alternative parity-violating cosmological models (e.g., Alexander, Cai, Kim-Naselsky inflationary leptogenesis) are also ruled out.
- `ave-evidence-framing-discipline` — applied at result-doc draft; strength language tied to explicit Δsigma numbers + 1sigma-box-width caveats.
- `ave-walk-back` — IF outcome A or C decisively shifts C5 row state, propagate matrix-row + closure-roadmap.
- `flag-don't-fix` — applied to §2.5 anomalies (citation typo + catalog-access blocker). NOT silently corrected.

---

## 7. Pre-registration freeze attestation

**This pre-registration is frozen 2026-05-19 BEFORE the comparison driver writes any numerical output.** Subsequent commits to the driver or result doc on this branch must reference this prereg by file path. Any deviation from §3 (sigma_Shamir derivation procedure, separation calculation, outcome adjudication mapping) requires an explicit "DEVIATION FROM PREREG" entry in the result doc with justification.

---

*End of pre-registration.*
