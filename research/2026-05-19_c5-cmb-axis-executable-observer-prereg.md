# C5-CMB-AXIS Executable Observer — Execution-Session Pre-Registration

**Date:** 2026-05-19
**Branch:** `analysis/c5-cmb-axis-driver` off `analysis/integration` at `e61a3dc` (post-E1a merge)
**Status:** EXECUTION-SESSION PRE-REGISTRATION. Frozen BEFORE driver implementation + data analysis. Separate from the methodology pre-registration at [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md) (which is the immutable frozen methodology spec; this doc pins the specific execution choices).

**Handoff:** [`/Users/grantlindblom/.claude/plans/e1b-c5-cmb-axis-handoff.md`](/Users/grantlindblom/.claude/plans/e1b-c5-cmb-axis-handoff.md) — E1b session of Section E cascade.

---

## 1. Pre-registration target (per ave-prereg Step 1)

**Test:** execute the frozen 2026-05-15 A-034 CMB axis-alignment empirical prereg by:
1. Computing the CMB quadrupole-octupole axis-of-evil from raw Planck PR3 SMICA temperature data (Observable 1, primary).
2. Pinning literature-published axis directions for Observables 2-4 (Hubble flow, LSS spin, matter asymmetry) using paper-pinned references at the same epistemological grade as C8-BARYON-LADDER PDG anchors and E1a BMW lattice baselines (i.e., paper-quoted literals, not re-derivation).
3. Computing the pairwise angular-separation matrix among the 4 primary observables.
4. Computing the degree-class agreement statistic vs uniform-prior null.
5. Adjudicating per the 5+ pre-registered outcomes (A / A+ / B / C / D / E) from the frozen methodology prereg.

**Out of execution scope** (this session): Observable 5 (E/B polarization), Observable 6 (orbital-plane alignment statistics), Observable 7 (CODATA G P_2 anisotropy). These are documented in the methodology prereg §1.5 / §1.6 / §1.7 and are individual workstreams of comparable size to the 4-axis test; folding them into this session would exceed single-session scope per ave-evidence-framing-discipline. The driver outputs an explicit "Observable 5-7: future execution session" status.

---

## 1.5. Picture-first (per ave-prereg Step 1.5)

**Plumber-physical picture:** the cosmic-scale K4 lattice was crystallized at the parent black hole's geometric saturation event (A-034 §A-034.5 + Vol 3 Ch 4 §TKI strain-snap). The parent BH had a spin axis $\hat{S}_{\text{parent}}$; the saturation event froze the K4 lattice's orientation in such a way that $\hat{S}_{\text{parent}}$ remains imprinted as the lattice's preferred internal direction $\hat{\Omega}_{\text{freeze}}$. Multiple cosmological observables (CMB low-ℓ multipoles, Hubble flow anisotropy, large-scale-structure galaxy spin orientations, matter-asymmetry direction) are different observational projections of this same underlying axis.

**Why this is testable:** standard cosmology (ΛCDM + inflation) has no mechanism to imprint a preferred axis. A statistical fluctuation could produce alignment in 2-of-4 observables; alignment in 4-of-4 (or 5+) requires either a mechanism (A-034) or extraordinary coincidence. The pairwise angular-separation matrix discriminates these hypotheses.

**Why no specific direction is predicted:** per the frozen methodology prereg §7 (line 413-416): *"It does NOT predict the SPECIFIC direction of the cosmic spin axis from theory (only that all four axes align). Theory doesn't predict the parent BH's spin direction."* The (l=174°, b=-5°) corpus-quoted value at [`universal-saturation-kernel-catalog.md:88`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) is an EMPIRICAL reference point from prior literature, not an AVE-derived prediction. Per [`closure-roadmap.md:100`](../manuscript/ave-kb/claim-quality-closure-roadmap.md) option (c): *the AVE prediction is an alignment correlation, not a specific axis value; the empirical axis emerges from the data.*

---

## 2. Verified state pre-execution (per verify-before-cite v1.2)

10 Phase-0 verifications confirmed at session start:
1. Frozen methodology prereg at `research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md` (file exists, 516 lines)
2. Predecessor commits reachable from `analysis/integration`: `fb9d9c0` (landing) + `1b2ef6d` (E/B extension) + `fc05b5c` (G-anisotropy Observable 7)
3. C5-CMB-AXIS matrix entries at `manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428 (Predictions) + 514 (Lifecycle) + 554 (Execution) + 907 (Mermaid)
4. A-034 catalog at `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` lines 85-95 lists the 4-observable prediction
5. Closure-roadmap entries at lines 35 (prereg landing) + 100 (citation gap deferral) + 289 (5-observable summary) + 947 (Route 3 leverage)
6. Phase 1 driver at `src/scripts/vol_3_macroscopic/cmb_axis_alignment_driver.py` (333 lines, literature-comparison only)
7. SPARC template at `src/scripts/vol_3_macroscopic/sparc_catalog_ingest.py` (272 lines, gold-standard public-data ingest)
8. E1a result-doc template at `research/2026-05-19_c3-muon-delta-fermilab-driver-rerun-result.md`
9. Skill ecosystem: `ave-prereg`, `verify-before-cite`, `ave-canonical-leaf-pull`, `substrate-native-check`, `consistency-vs-emergence`, `ave-driver-script-honesty`, `ave-canonical-source`, `ave-evidence-framing-discipline`, `ave-discrimination-check`, `ave-audit`, `ave-walk-back`, `phase-space-coordinate-check` (NA), `pre-test-physics-check` (internal-adherence)
10. Integration HEAD at `e61a3dc` (Merge analysis/c3-muon-delta-driver-rerun into integration)

**Python dependencies installed at session start:** `healpy 1.19.0`, `astropy 7.2.0` (upgraded from 7.1.1 for numpy 2.x compatibility), `numpy 2.4.4`, `scipy 1.15.3`.

**Corpus-grep findings (ave-corpus-grep):**
- Zero prior `healpy` / `astropy` / HEALPix code in any of the 10 AVE-staging repos. E1b establishes the pipeline pattern from scratch.
- Phase 1 driver provides the literature-axis comparison + (l=174°, b=-5°) reference structure.
- C5 is the 5th cosmic-scale A-034 instance and the only PROSPECTIVE forward-prediction one (the other 4 cosmic-scale rows are retrospective: BCS, solar flare, BH ring-down, Schwarzschild identity).
- K4 cubic-symmetry suppression that retired C17 (Sagnac), C18 (vacuum birefringence) does NOT apply to C5. C5 is at q ≈ 10⁻²⁶ m⁻¹ (cosmological), the opposite extreme from optical q ≈ 10⁷ m⁻¹; C5 tests the BULK SYMMETRY AXIS of the K4 lattice, not propagation anisotropy.

---

## 3. Specific execution choices (PINNED BEFORE EXECUTION)

### 3.1 Planck data source

**Component-separation map:** **SMICA** (Spectral Matching Independent Component Analysis), Planck 2018 PR3.
- File: `COM_CMB_IQU-smica_2048_R3.00_full.fits` (full-mission, NSIDE=2048, ~600 MB)
- Source: ESA Planck Legacy Archive `https://pla.esac.esa.int/pla/aio/product-action?MAP.MAP_ID=COM_CMB_IQU-smica_2048_R3.00_full.fits`
- Cached at: `data/planck_pr3/` (gitignored)
- Per the matrix-cited canonical source at [`divergence-test-substrate-map.md:554`](../manuscript/ave-kb/common/divergence-test-substrate-map.md).

**Why SMICA over NILC/Commander/SEVEM:** SMICA is the default canonical component-separation algorithm used in Planck collaboration publications for CMB-only analyses. Cross-validation between methods is a multi-session work item (~one driver per method) and not part of this session's single-deliverable scope. Per `pre-test-physics-check` internal-adherence, autonomous-mode default is SMICA + DR17 (matching the matrix's existing references). If a follow-up session surfaces methodology-driven differences (Outcome D), one of NILC/Commander/SEVEM cross-checks becomes the natural next session.

**Axis estimation algorithm:** maximum angular-momentum dispersion estimator following the methodology established by de Oliveira-Costa et al. 2004 (Phys. Rev. D 69:063516, "Significance of the largest scale CMB fluctuations in WMAP"):
- For each candidate sky direction $\hat{n}$, rotate the alm such that $\hat{n}$ is the new z-axis, compute $\sum_m m^2 |a_{\ell m}|^2$ in the rotated frame.
- The preferred axis for multipole $\ell$ is the $\hat{n}$ that maximizes this dispersion.
- For axis-of-evil (quadrupole + octupole combined), use the joint maximization over $\ell=2$ AND $\ell=3$ via the normalized $\sum_\ell \sum_m m^2 |a_{\ell m}|^2 / (\ell(\ell+1)\sum_m |a_{\ell m}|^2)$ functional.
- Grid resolution: HEALPix NSIDE=32 (12,288 candidate directions, ~3° per pixel) for initial scan, then NSIDE=128 (196,608 pixels, ~0.5°) refinement around the maximum.
- Compute alm via `hp.map2alm(map, lmax=3, use_pixel_weights=True)` after applying the inpainted-pixel-weighted or whole-sky alm extraction.

### 3.2 Hubble flow direction (Observable 2)

**Paper-pinned reference value:** Whitford et al. 2023 (MNRAS 526:3051) bulk-flow analysis on Pantheon+ Type Ia supernovae:
- Bulk-flow direction at scale $h = 150~h^{-1}$ Mpc: $(l, b) \approx (323°, 26°)$ with combined uncertainty $\sim 30°$ at 1σ.
- This is the most recent peer-reviewed value at the time of writing (2026-05-19).
- Pantheon+ raw data: `https://github.com/PantheonPlusSH0ES/DataRelease/raw/main/Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat`

**Why paper-pinned not re-fit:** the Pantheon+ bulk-flow fit is a multi-step regression involving supernova distance moduli, dust corrections, and peculiar velocity decomposition. Re-deriving from raw SN data requires ~1-2 sessions of dedicated work matching Whitford+2023 methodology. Per the C8-BARYON-LADDER PDG-anchor pattern, paper-pinned values are epistemologically equivalent to running our own fit when the published methodology is sound and the value is well-established. Driver records the paper-pinned value with explicit comment + reference.

### 3.3 Large-scale-structure spin axis (Observable 3)

**Paper-pinned reference value:** Shamir 2020 (Astrophys. J. 891:97) and earlier Longo 2011 (Phys. Lett. B 699:224) reported preferred galaxy spin-orientation directions from SDSS:
- Longo 2011 (DR7 spiral handedness): preferred axis $(l, b) \approx (32°, 32°)$ — northern galactic dipole direction; ~2-3σ significance.
- Shamir 2020 (DR8 ~10⁶ galaxies): broadly consistent with dipole structure aligned within ~30° of Longo direction.
- Combined pinned value: $(l, b) \approx (32°, 32°)$ with $\sigma \approx 30°$ uncertainty (literature scatter dominates).

**Caveat:** the SDSS LSS spin alignment is contested in the literature; some analyses find no significant axis (consistent with isotropic). The driver records the Longo direction with explicit "disputed" annotation and the AVE-framework discriminator is downstream: does the alignment with the OTHER observables emerge above what isotropic-uniform-prior would expect, given the SDSS measurement uncertainty?

### 3.4 Matter-asymmetry direction (Observable 4)

**Status:** per the frozen methodology prereg §3.4 (line 314-316): *"this is the weakest of the four tests because the directional probes for matter asymmetry are themselves marginal. May be inconclusive."*

**Driver handling:** record as "weak/inconclusive" with the framework-quoted axis (l=174°, b=-5°) as the prereg-cited matter-asymmetry direction. Do NOT count this observable in the primary pairwise alignment statistic. Include in the report but flag explicitly as low-confidence.

### 3.5 AVE-framework reference axis

**$\hat{\Omega}_{\text{freeze}}$ reference:** $(l=174°, b=-5°)$ per [`universal-saturation-kernel-catalog.md:88`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md). This is NOT an AVE-derived prediction (see §1.5 above); it is the empirical-literature-quoted reference point. The driver records it as the "framework reference direction" and computes pairwise alignments between this reference and the data-derived axes.

---

## 4. Pre-registered adjudication mapping

Mapping the frozen methodology prereg's outcomes (A / A+ / B / C / D / E) to driver auto-classification:

**Outcome A+** (strongest PASS): all 4 primary axes (CMB / Hubble / LSS / framework-reference) mutually aligned within 10° at 3σ; degree-class agreement statistic > 95% vs uniform-prior null.

**Outcome A** (PASS): 3-of-4 axes mutually aligned within 20° at combined 3σ; degree-class agreement > 80%.

**Outcome B** (PARTIAL CONFIRMATION): 2-of-4 axes aligned; 1-2 systematically misaligned; degree-class agreement between 50% and 80%. Tension structure to investigate.

**Outcome C** (NULL / framework FALSIFIES at cosmic scale): pairwise angular separations consistent with uniform-prior null; degree-class agreement < 50% (i.e., chance-level). A-034 cosmic-scale instance fails; catalog survives if ≥20 other instances hold per matrix line 428.

**Outcome D** (DATA INSUFFICIENT / FLAG for methodology): individual axis directions have uncertainty regions so large that A, B, and C cannot be distinguished. Surface to Grant for methodology re-adjudication.

**Outcome E** (RETIRE this session): Planck data download fails, healpy import fails, or alm computation produces inconsistent results that cannot be debugged in-session. Defer to a session with data-staging infrastructure.

### Sharpest single falsifier (per closure-roadmap.md:35 and frozen prereg §5)

**The single sharpest falsifier:** if $\Delta\theta(\text{CMB axis-of-evil}, \text{Hubble flow bulk direction}) > 20°$ at combined 3σ uncertainty, A-034's cosmic-scale prediction has failed → Outcome C immediate. Both CMB (Planck PR3) and Hubble flow (Pantheon+ via Whitford+2023) are well-measured enough to provide a crisp test.

---

## 5. Cascade implications mapped pre-execution

Per [closure-roadmap.md:947](../manuscript/ave-kb/claim-quality-closure-roadmap.md): *"Route 3 driver is the highest-leverage operational move for the entire framework, not just C5-CMB-AXIS."*

**Outcome → cascade:**
- **A+ / A (PASS):** D4-A034 cosmic row strengthens; C4 three-route Route 3 ($\mathcal{J}_{cosmic}$) gains empirical anchor; E1c (Route 3 framework-commitment activation) becomes immediately tractable.
- **B (PARTIAL):** D4-A034 cosmic row holds with tension flag; E1c deferred pending methodology investigation.
- **C (NULL):** D4-A034 cosmic row retires; catalog survives via the 20+ smaller-scale instances; Route 3 stays deferred on A-031 cosmic-parameter-horizon; E2b (DM META closure) becomes natural next session.
- **D (FLAG):** methodology adjudication with Grant; possible re-run with different Planck map (NILC/Commander) or refined estimator; E1c deferred until C5 settles.
- **E (RETIRE):** data-access issue; A-034 catalog status unchanged (held at "execution pending"); E2b becomes natural alternative.

---

## 6. Compliance with ave-prereg discipline

- ✓ Test methodology + outcomes fixed BEFORE execution
- ✓ Specific Planck map version + SDSS catalog version + axis estimators pinned in §3
- ✓ 5+ pre-registered outcomes enumerated in §4 with discriminating criteria
- ✓ Sharpest single falsifier identified in §4 final paragraph
- ✓ Picture-first physical content in §1.5
- ✓ Corpus-coverage check via ave-corpus-grep (no prior healpy/Planck infrastructure; this is the first)
- ✓ Honest scope: Observables 5-7 explicitly deferred to future sessions
- ✓ Cascade implications mapped pre-execution in §5

---

## 7. What this prereg does NOT do

- ❌ Does NOT predict the SPECIFIC AXIS DIRECTION (per frozen methodology prereg §7 and §1.5 above). The AVE prediction is alignment-correlation.
- ❌ Does NOT execute Observables 5 (E/B), 6 (orbital), 7 (G P_2 anisotropy). These are explicit future-session scope.
- ❌ Does NOT cross-validate SMICA vs NILC vs Commander vs SEVEM. Single component-separation method (SMICA) is the canonical choice for this session.
- ❌ Does NOT close A-034 catalog. A-034 catalog status is unchanged regardless of C5 outcome; this driver tests ONLY the cosmic-scale instance.
- ❌ Does NOT pin the literature citation for (l=174°, b=-5°) — per [`closure-roadmap.md:100`](../manuscript/ave-kb/claim-quality-closure-roadmap.md) option (c), executing the driver makes the citation moot. The driver computes its own axis-of-evil direction from Planck data; the (174°, -5°) value is recorded as a literature reference point only.

---

## 8. Provenance

- **Drafted under:** 2026-05-19, E1b session of Section E cascade (post-E1a-merge at integration `e61a3dc`).
- **Branch:** `analysis/c5-cmb-axis-driver`.
- **Pure-AVE-corpus rule:** all content above is pure physics + corpus-rooted methodology. No external context.
- **Frozen:** this prereg is frozen before the driver's first line of code is written. Execution discoveries that change the prereg are recorded in the result doc as walk-backs, not as retroactive edits to this prereg.
