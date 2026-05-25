# C5-CMB-AXIS GZ DECaLS Cross-Catalog Validation — Scoping (Outcome E)

**Date:** 2026-05-19
**Branch:** `analysis/c5-gz-decals-spin-orientation` off `analysis/integration` at `d413726` (rebased to current integration tip mid-session; initial branch off `6436d65`)
**Status:** SCOPING-ONLY. Pre-registration NOT frozen — cross-catalog validation as briefed is infeasible by physical methodology. Stopped at Phase 0 per brief instruction.
**Briefing:** [`_orchestration/_archive/c5-sdss-dr17-spin-orientation.md`](../_orchestration/_archive/c5-sdss-dr17-spin-orientation.md) (reference template for the cross-catalog session) + GZ DECaLS implementor brief (in-session).
**Predecessors:**
- E1b: [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md) — CMB axis (60.28°, 50.48°), σ=0.92°
- E1b-prime: [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md) — σ_Hubble 30°→24°, Marginal-D
- E1c (SDSS DR17 spin): [`research/2026-05-19_c5-sdss-spin-orientation-result.md`](2026-05-19_c5-sdss-spin-orientation-result.md) — LSS axis (129.0°, 79.0°) σ=6.83°, Marginal-D, CMB-LSS = 36.75° at 5.33σ from zero

---

## 0. TL;DR

**Outcome: E (catalog-methodology incompatibility) — STOP and report per brief outcome table.**

GZ DECaLS (Walmsley+2022 MNRAS 509:3966) cannot be used as an independent cross-catalog validation of the SDSS DR17 spin-orientation result because **the Walmsley+2022 catalog does not classify spirals by chirality direction** (clockwise vs anticlockwise). The Galaxy Zoo decision tree was restructured for GZ2 (Hart+2016) and again for GZ DECaLS (Walmsley+2022); the original GZ1 binary chirality question was replaced with **winding tightness** (tight/medium/loose) and **arm count** (1/2/3/4/more-than-4/can't-tell). Without a per-galaxy CW/ACW classification, the Longo 2011 cos γ axial-dipole estimator (which requires a binary χᵢ ∈ {−1, +1} label per galaxy) cannot be applied to GZ DECaLS in any form.

This is the **structural incompatibility branch** of Outcome E from the brief's outcome table:

> E (CATALOG-METHODOLOGY) | Catalogs incomparable (different Q-cuts, sky coverage, chirality conventions) | Escalate to orchestration BEFORE retry — methodology question needs Grant adjudication

The brief explicitly anticipates this branch and instructs (in the constraints section): "If Outcome E (methodology surface): STOP and report rather than retry."

The cross-catalog goal — independent methodology + imaging + classification path — remains valuable and is **NOT vacated** by this finding. The viable cross-catalogs with chirality direction are surfaced in §5 below for orchestration-level adjudication. The natural candidate is **Shamir 2022 MNRAS 516:2204 ("Analysis of spin directions of galaxies in the DESI Legacy Survey")** — Ganalyzer algorithmic chirality applied to DECaLS DR8 imaging, fulfilling the brief's "different imaging + different methodology" requirement while restoring the chirality observable.

---

## 1. Phase 0 verification log

Per brief Phase 0 — verifications run before any prereg or driver work.

### 1.1 Worktree + branch state (per `verify-before-cite` v1.3 trigger 7c + 8)

- Worktree path: `/Users/grantlindblom/AVE-staging/AVE-Core/.claude/worktrees/agent-a9466abaf9e7432be/`
- Branch: `analysis/c5-gz-decals-spin-orientation` (created from `origin/analysis/integration`)
- Initial tip: `6436d65 kb(universal-saturation-kernel-catalog): ε/μ axis explicit + gap-cells + companion-row links` (matches brief's stated starting point).
- Mid-session rebase: origin advanced 5 commits during the Walmsley+2022 schema verification phase (additional 2026-05-19 EOD work landed: `analysis/c5-corpus-pin-fix` Longo axis walk-back + `analysis/soliton-lattice-coupling-operator-scoping`). Rebased to `d413726 Merge analysis/soliton-lattice-coupling-operator-scoping into integration` to capture those updates before commit.
- Post-rebase tip: `d413726`.

### 1.2 Reference template review

Read and inventoried the SDSS DR17 reference template for adaptation:

1. **Driver**: [`src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py`](../src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py) — 950 lines, Longo 2011 cos γ estimator + Hessian-MC + bootstrap + randomization-null + adjudication.
2. **Prereg**: [`research/2026-05-19_c5-sdss-spin-orientation-prereg.md`](2026-05-19_c5-sdss-spin-orientation-prereg.md) — frozen δ_clear=0.4 + 3-pipeline robustness sweep at δ ∈ {0.2, 0.4, 0.6}.
3. **Result**: [`research/2026-05-19_c5-sdss-spin-orientation-result.md`](2026-05-19_c5-sdss-spin-orientation-result.md) — Marginal-D outcome, axis (129.0°, 79.0°) σ=6.83°.
4. **Data**: [`data/sdss_dr17/`](../data/sdss_dr17/) + README — `GalaxyZoo1_DR_table2.csv.gz` with sexagesimal RA/Dec, NVOTE, P_CW, P_ACW, SPIRAL flag columns.

The per-galaxy ±1 chirality label `chirality_i = +1 if P_CW > P_ACW else -1` is the load-bearing input to the cos γ axial-dipole estimator. Without an analog of `P_CW` and `P_ACW` in the cross-catalog, the estimator does not apply.

### 1.3 Corpus-grep (per `ave-prereg`)

`grep -rln` across all 10 AVE-staging repos for "Walmsley", "DECaLS", "gz_decals", "GZ DECaLS", "Galaxy Zoo DECaLS":

- AVE-Core only — `research/2026-05-19_c5-sdss-spin-orientation-result.md` §5.5 next-session-priorities (mentions GZ DECaLS as the proposed cross-catalog), `manuscript/ave-kb/claim-quality-closure-roadmap.md`, `manuscript/ave-kb/common/divergence-test-substrate-map.md`, `_orchestration/soliton-lattice-coupling-operator.md`.
- All other AVE-staging repos: 0 hits.
- No prior implementor work on Walmsley+2022 catalog. No prior chirality / spin-direction estimator code targeting DECaLS imaging anywhere in the workspace.

### 1.4 Walmsley+2022 catalog source verification (per `verify-before-cite` v1.3 trigger 1 + 3)

**Catalog data release**: [Zenodo record 4573248](https://zenodo.org/records/4573248) — confirmed accessible (HTTP 200 on file list endpoint). MD5 checksums published for all files. The data release accompanies Walmsley+2022 MNRAS 509:3966 (the released catalog version is consistent with the paper).

**Files in the data release** (per Zenodo file listing):

| Filename | Size | MD5 |
|---|---|---|
| `gz_decals_auto_posteriors.csv` | 2.6 GB | `5cc06cc0e2d44b5c0eb5c60231530b67` |
| `gz_decals_auto_posteriors.parquet` | 1.6 GB | `2e9f4b4fe9f3473a44f60aed0526911f` |
| `gz_decals_volunteers_1_and_2.csv` | 80.8 MB | `f1be080ac22269fb5ea4e12ddefb8b11` |
| `gz_decals_volunteers_1_and_2.parquet` | 18.7 MB | `e9de511cbd5977e02c81cbdb5d21b7c2` |
| `gz_decals_volunteers_5.csv` | 145.8 MB | `b12e3767b3968f9767d4f4115cc69d4d` |
| `gz_decals_volunteers_5.parquet` | 40.5 MB | `364d0b598b7d2958553350c5ce0ffc14` |
| `schema.md` | 4.8 KB | `d23668017214178201416730e6e7c0e768d` |

**Schema verification** (catalog-column inspection):

Direct HTTPS download of the schema.md from Zenodo confirms the catalog uses `{question}_{answer}` column naming. The schema describes the framework but defers to the paper for the precise list of question-answer pairs per campaign.

**Direct column-header inspection** (HTTPS range-request of the first 8 KB of `gz_decals_volunteers_1_and_2.csv` — confirms actual columns released, not just paper assertions):

```
iauname, ra, dec, redshift, elpetro_absmag_r, sersic_nmgy_r, petro_th50, petro_th90,
petro_theta, upload_group, active_learning_on, in_gzd_c, data_release,
smooth-or-featured_total-votes, smooth-or-featured_smooth, smooth-or-featured_smooth_fraction,
smooth-or-featured_smooth_debiased, smooth-or-featured_featured-or-disk, ...
how-rounded_*, disk-edge-on_*, edge-on-bulge_*,
has-spiral-arms_total-votes, has-spiral-arms_yes, has-spiral-arms_yes_fraction,
has-spiral-arms_yes_debiased, has-spiral-arms_no, has-spiral-arms_no_fraction,
has-spiral-arms_no_debiased,
spiral-winding_total-votes,
spiral-winding_tight, spiral-winding_tight_fraction, spiral-winding_tight_debiased,
spiral-winding_medium, spiral-winding_medium_fraction, spiral-winding_medium_debiased,
spiral-winding_loose, spiral-winding_loose_fraction, spiral-winding_loose_debiased,
spiral-arm-count_total-votes, spiral-arm-count_1, ..., spiral-arm-count_more-than-4_debiased,
bar_*, bulge-size_*, merging_*
```

**No clockwise / anticlockwise / direction / chirality / winding-sense column exists in the released catalog.**

### 1.5 Walmsley+2022 paper verification (per `verify-before-cite` v1.3 trigger 1)

From Walmsley+2022 (MNRAS 509:3966) text via OUP article HTML:

> "The largest workflow change between Galaxy Zoo versions was between the original Galaxy Zoo (GZ1) and Galaxy Zoo 2 (GZ2). GZ1 presented classifiers with a single task per galaxy, a choice between smooth/elliptical, multiple versions of featured/disc (including edge-on, face-on, and directionality of spiral structure), and merger."

The paper explicitly notes that the "directionality of spiral structure" question was a GZ1 feature that did NOT carry forward through the GZ2 → GZ DECaLS decision-tree evolution. The Walmsley+2022 paper's Figure 4 (the GZD-5 decision tree) does not include a chirality / direction question.

This is consistent with the Hart+2016 GZ2 paper, which restructured the decision tree to focus on pitch-angle, bars, bulges, and arm-count — eliminating the binary CW/ACW direction question of GZ1.

### 1.6 Cross-checked alternative GZ catalogs

For completeness, checked whether any post-GZ1 Galaxy Zoo campaign retained the chirality observable:

| Catalog | Chirality question? | Notes |
|---|---|---|
| **GZ1** (Lintott+2011) | YES — `P_CW`, `P_ACW` | Source of SDSS DR17 spin-orientation result; ~667k galaxies |
| **GZ2** (Hart+2016) | NO — restructured to pitch-angle, arm-count, bars; no binary direction question | ~239k galaxies |
| **GZ Hubble** (Willett+2017) | NO — same restructured tree | ~120k galaxies |
| **GZ CANDELS** (Simmons+2017) | NO — same restructured tree | ~50k galaxies |
| **GZ DESI / GZ DECaLS** (Walmsley+2022) | NO — same restructured tree | ~314k galaxies |

**Conclusion**: GZ1 is the ONLY Galaxy Zoo catalog with crowdsourced spiral chirality observables. The Galaxy Zoo decision-tree evolution post-GZ1 removed this observable across all subsequent campaigns.

---

## 2. The methodological blocker (precisely stated)

The Longo 2011 cos γ axial-dipole estimator (used in the SDSS DR17 driver per [`src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py:314-322`](../src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py)) requires:

$$A(\hat{n}_A) = \frac{1}{N} \sum_{i=1}^{N} \chi_i \cdot (\hat{n}_i \cdot \hat{n}_A) \quad \text{with } \chi_i \in \{-1, +1\}$$

The per-galaxy chirality label $\chi_i$ is the LOAD-BEARING input. Without it, no axial-dipole estimator on chirality direction can be constructed.

GZ DECaLS provides per-galaxy:
- **Arm winding tightness**: a 3-way classification {tight, medium, loose}. This is a SCALAR morphological feature, not a signed quantity. There is no natural mapping to $\chi_i \in \{-1, +1\}$ — tight-vs-loose is parity-symmetric (a tight clockwise spiral and a tight anticlockwise spiral are both "tight").
- **Arm count**: integer {1, 2, 3, 4, more-than-4}. Also parity-symmetric.

Neither observable resolves the L/R chirality direction the Longo estimator needs. The closest GZ DECaLS observable to chirality direction is the `wrong_size_warning` flag (catalog-quality artifact filter; nothing to do with spin direction).

**Could chirality direction be re-extracted from the DECaLS DR5 imaging itself?** In principle yes — by running Shamir's Ganalyzer algorithm (the SDSS DR8 analysis path of Shamir 2020 ApJ 891:97) on the DECaLS image cutouts available in the GZ DECaLS data release (`gz_decals_dr5_png_part{1,2,3,4}.zip`, totaling ~104 GB of image cutouts). This would be a NEW classification, NOT a Walmsley+2022 catalog re-use. It belongs in a separate epic with its own prereg + driver + auditor. See §5 below.

---

## 3. Phase plan deviations from brief

The brief's Phase 1-4 (catalog ingest, prereg, driver, result) is not reachable. Phase 0 verifications surface the structural incompatibility before catalog download. Per brief constraint: "If Outcome E (methodology surface): STOP and report rather than retry."

Actions taken this session (in scope):
- Phase 0 verifications (this doc §1)
- Outcome E classification + scoping (this doc §2, §4-5)

Actions NOT taken (out of scope, would require Grant adjudication):
- Walmsley+2022 catalog download (no chirality column to ingest)
- Prereg freeze (cannot pre-register an estimator that does not apply)
- Driver scaffold (no input data shape to scaffold against)
- Matrix updates (no result to feed back into C5 row; the SDSS DR17 row is unaffected by this finding)

---

## 4. Adjudication

Per brief's Outcome adjudication table:

| Outcome | Criterion | This session |
|---|---|---|
| A (CATALOG-AGREE) | GZ DECaLS spin axis within 1σ of SDSS DR17 result (l=129°, b=79°) | N/A — GZ DECaLS does not have a spin-axis observable to fit |
| C (CATALOG-DISAGREE) | GZ DECaLS >2σ from SDSS DR17 | N/A — same reason |
| D (CATALOG-MARGINAL) | 1-2σ separation between catalogs | N/A — same reason |
| **E (CATALOG-METHODOLOGY)** | **Catalogs incomparable (different Q-cuts, sky coverage, chirality conventions)** | **THIS SESSION — chirality observable absent from GZ DECaLS** |

**Outcome: E.** Per brief: "STOP and report rather than retry."

This outcome does NOT modify the SDSS DR17 result. The SDSS DR17 spin-axis result at (129.0°, 79.0°) σ=6.83° stands as Marginal-D per the merged result doc; the cross-catalog robustness check via GZ DECaLS specifically is infeasible by methodology incompatibility, not a new empirical finding about the spin-axis observable itself.

---

## 5. Surfacing the viable cross-catalog candidates (orchestration input)

The brief's goal — independent imaging + classification methodology cross-validation — remains valuable. The viable cross-catalogs with the chirality direction observable that the Longo cos γ estimator requires:

### 5.1 Shamir 2020 ApJ 891:97 (SDSS DR8 Ganalyzer)

- **Methodology**: algorithmic chirality classification via Ganalyzer (image-processing pipeline matching radial intensity profiles).
- **Imaging**: SDSS DR8 (galactic latitude > 30° subset).
- **Sample size**: ~170k SDSS spirals + ~33k Pan-STARRS spirals.
- **Independence from GZ1**: HIGH — different methodology (algorithmic, not crowdsourced) + different DR (DR8 vs DR7).
- **Availability**: SDSS DR17 prereg §2 corpus-grep flagged "not publicly redistributed in a clean machine-readable form; partial tables in the published paper". Verify with author if needed for an actual epic.
- **Brief's requirement match**: PARTIAL — methodology + classification differ, but the imaging dataset overlaps with GZ1 (both are SDSS spirals, just different DR releases). Same instrument noise / systematic floor.

### 5.2 Shamir 2022 MNRAS 516:2204 ("Analysis of spin directions of galaxies in the DESI Legacy Survey")

- **Methodology**: Ganalyzer algorithmic chirality, same family as Shamir 2020.
- **Imaging**: DESI Legacy Imaging Surveys = DECaLS + BASS + MzLS (so the DECaLS-derived subset specifically targets the brief's "DECaLS DR8 imaging" requirement).
- **Sample size**: published ~10⁶ spirals across the full DESI Legacy footprint per related Shamir 2022 Advances in Astronomy result; per-survey subsets (DECaLS-only) are smaller.
- **Independence from GZ1**: HIGH — different methodology (algorithmic vs crowdsourced) AND different imaging dataset (DECaLS vs SDSS).
- **Availability**: TBD — check Shamir's public catalogs page or contact author. Cited via Google Scholar with arxiv ID not surfaced.
- **Brief's requirement match**: BEST — fulfills "different catalog + different methodology + different imaging dataset" exactly as the brief specified, just with Shamir+DECaLS rather than Walmsley+DECaLS. Methodologically more credible for cross-validation than re-using Walmsley's pixel data through a different classifier.

**Recommendation**: if cross-catalog validation is still desired, retarget the epic to Shamir 2022 MNRAS 516:2204 / DESI Legacy chirality catalog. Specifically: locate the Shamir 2022 public catalog (if released) and re-run the SDSS DR17 driver's Longo cos γ estimator on it. This preserves all the methodological discipline of the SDSS DR17 epic while genuinely changing imaging + classification per the cross-catalog cross-validation goal.

### 5.3 Re-classify GZ DECaLS imaging via Ganalyzer (de novo)

- **Methodology**: NEW chirality classification by running Shamir's Ganalyzer (or equivalent open-source spiral-handedness pipeline) on the GZ DECaLS PNG cutouts (~104 GB across 4 zip files in the Zenodo record).
- **Effort**: substantial — Ganalyzer is a multi-step image-processing pipeline (radial intensity profile fitting); reproducing it from the published methodology + a corpus of GZ DECaLS PNGs is a multi-session implementor epic of its own.
- **Independence from GZ1**: HIGH — completely independent classification + imaging.
- **Risk**: re-implementing Ganalyzer from scratch is non-trivial; if Shamir's pipeline is not open-source-released, the implementation effort is the dominant cost.
- **Brief's requirement match**: EXACT — different catalog (de novo), different methodology (Ganalyzer vs CW/ACW crowdsourcing), different imaging dataset (DECaLS DR5 PNGs).

**Recommendation**: prefer 5.2 (Shamir's pre-classified DESI Legacy catalog if publicly available) over 5.3 (de novo re-classification) for cost reasons. 5.3 is the fallback if 5.2's catalog isn't available.

### 5.4 Galaxy Zoo 2 (Hart+2016) — DISMISSED

- **Methodology**: crowdsourced, but the decision tree was restructured to remove the chirality direction question.
- **Conclusion**: same methodological blocker as Walmsley+2022. Not viable.

---

## 6. Cascade implications

### 6.1 C5 row (no change this session)

`manuscript/ave-kb/common/divergence-test-substrate-map.md` C5 row state is UNCHANGED by this session. SDSS DR17 Marginal-D + sub-finding "CMB-LSS = 5.33σ from zero" stands as adjudicated 2026-05-19 EOD.

### 6.2 Closure-roadmap (no change this session)

`manuscript/ave-kb/claim-quality-closure-roadmap.md` is UNCHANGED. The cross-catalog GZ DECaLS line item (if such existed) is now reclassified from "candidate cross-catalog validation" to "infeasible by methodology" — but no roadmap entry was added in the first place, so no walk-back is needed.

### 6.3 Next-session priorities

Surfaced to orchestration / Grant for adjudication:

1. **Adjudicate retarget to Shamir 2022 MNRAS 516:2204** (DESI Legacy / DECaLS Ganalyzer chirality) — investigate catalog availability + methodology before committing to an implementor epic.
2. **Defer until threshold-policy adjudication** — per the SDSS DR17 result doc §5.5 next-session priorities, the 20° alignment threshold is the bottleneck on A/D adjudication. If the threshold is sharpened to σ_combined (Grant decision), the SDSS DR17 result is already PASS-A at 5.33σ — no cross-catalog cross-check needed for that adjudication.
3. **Continue Option B path** (joint Pantheon+ + SDSS DR17 constraint) per SDSS DR17 result doc §5.5 item 2 — independent of the cross-catalog question.
4. **Sub-finding for the manuscript**: the GZ-decision-tree-evolution finding (GZ1 was the only campaign with chirality observable; all subsequent campaigns removed it) is itself an interesting cosmological-measurement-design note. Worth a 1-2 sentence aside in the manuscript treatment of LSS spin-direction observables, mentioning that the available chirality data is bottlenecked by the GZ1-era methodology.

### 6.4 Ω_freeze 8-observable cascade (no change this session)

`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:52` Observable 3 (LSS spin direction) remains at the state set by the SDSS DR17 result. This session's Outcome E does not change the Observable 3 status because the GZ DECaLS catalog could not test it.

---

## 7. Anomalies surfaced (per `flag-don't-fix`)

### 7.1 Brief assumed chirality observable exists in GZ DECaLS

**Observation**: the GZ DECaLS implementor brief stated:

> The chirality convention: verify Walmsley+2022 uses the same orientation convention as Longo 2011 / Hayes+2017 / Shamir 2020 (looking down spin axis from above)

This implicitly assumed the catalog HAS a chirality observable, with the verification scope limited to convention-direction. The actual structural finding is that the chirality observable is absent entirely, not just convention-different.

**Mechanism**: a common assumption that "GZ DECaLS extends GZ1's spiral-galaxy catalog with newer / larger / CNN-derived data" — true for arm-count + winding-tightness + bars + mergers, but FALSE for chirality direction. The decision-tree restructuring between GZ1 and GZ2/DECaLS dropped the chirality question entirely.

**Surfaced for orchestration**: future cross-catalog validation epics targeting LSS chirality should pre-verify chirality-column presence in the catalog at the brief-drafting stage. Per `verify-before-cite` v1.3 trigger 1, a direct read of the catalog schema (or header row) is the canonical step.

### 7.2 No corpus pins corrected this session

The SDSS DR17 result doc §4.1 corpus pin anomaly (Longo 2011 axis cited at (32°, 32°) in `cmb_axis_alignment_executable_observer.py:97-99` instead of Longo's actual (52°, 68.5°)) was landed by a separate walk-back epic between this session's branch-creation and rebase points — see commit `7e3d807 Merge analysis/c5-corpus-pin-fix` + `3f390d0 kb+walk-back: SDSS LSS spin-axis corpus pin (32°,32°) → (52°,68.5°) per Longo 2011`. After rebase, `cmb_axis_alignment_executable_observer.py:116-127` now carries the corrected Longo axis `(l=52°, b=68.5°)` with the corpus-pin-fix walk-back rationale inline. This session does not modify that file (corpus pin was already corrected upstream).

---

## 8. Skill / discipline attestation

- **`ave-prereg`** — corpus-grep complete (§1.3). No prior implementor work on Walmsley+2022; methodology blocker surfaced before any prereg drafting.
- **`verify-before-cite` v1.3** — trigger 1 (content) applied to Walmsley+2022 paper text + Zenodo catalog schema + direct CSV header download; trigger 7c (cross-branch state) applied to worktree HEAD + SDSS DR17 result location; trigger 8 (commit application) verified branch tip matches brief's stated `6436d65`.
- **`ave-canonical-leaf-pull` v1.1** — LSS-direction / data-fitting problem class enumerated via the SDSS DR17 prereg's canonical leaves; no new leaves required this session.
- **`pre-test-physics-check`** — methodological blocker (chirality observable absent) surfaced before any estimator code was attempted. This is the kind of plumber-physical question best surfaced AT DESIGN TIME, not after 30+ commits — exactly the failure mode pre-test-physics-check exists to prevent.
- **`flag-don't-fix`** — assumption-in-brief anomaly (§7.1) surfaced, not silently worked around.
- **`consistency-vs-emergence` v1.1** — this scoping doc is NOT a Class A/B/C/D/E test result; it's a Phase 0 verification log + Outcome E classification. No Class E framing applied because no LSS spin-direction test was actually executed.
- **`ave-driver-script-honesty`** — no driver was written this session (no input data shape to write against); the four-discriminator check is N/A.
- **`substrate-native-check`** — checked, but no continuum-field machinery + no eigsolver / saturation kernel involved. Same as SDSS DR17 — geometric / angular-statistics test domain.
- **`phase-space-coordinate-check`** — N/A because no fit was executed.
- **`ave-discrimination-check`** — N/A because Outcome A was not reached. No SM-counterfactual / interpretive-alternatives drafted.

---

## 9. Honest-closure attestation (per Rule 11)

This is a clean negative methodological finding closed via Outcome E. The cross-catalog validation as briefed cannot proceed because the chirality observable required for the Longo cos γ estimator is absent from the Walmsley+2022 GZ DECaLS catalog by design.

This is NOT a debug-toward-rescue. The framework's prediction (Observable 3, LSS spin direction) is unchanged by this finding. The SDSS DR17 result is unchanged. The cross-catalog cross-validation goal is unchanged — it remains valuable and the natural retarget (Shamir 2022 DESI Legacy) is surfaced in §5.2 for orchestration adjudication.

The branch `analysis/c5-gz-decals-spin-orientation` is closed with this scoping document. The implementor lane returns the methodology-incompatibility finding to orchestration as instructed by the brief's STOP condition.

---

*End of scoping document.*
