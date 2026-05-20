# C5-CMB-AXIS SDSS Spin-Orientation Re-Analysis — Execution-Session Pre-Registration

**Date:** 2026-05-19
**Branch:** `analysis/c5-sdss-dr17-spin-orientation` off `analysis/integration` at `5f926ad`
**Status:** EXECUTION-SESSION PRE-REGISTRATION. Frozen BEFORE estimator implementation + data analysis. Subordinate to the frozen 2026-05-15 A-034 methodology prereg at [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md).

**Briefing:** [`_orchestration/c5-sdss-dr17-spin-orientation.md`](../_orchestration/c5-sdss-dr17-spin-orientation.md) — Option A adjudicated 2026-05-19 EOD (SDSS DR17-class spin-orientation re-fit only; parallel-runnable with h-infinity-downstream-cascade).

**Predecessors:**
- E1b session: [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md) — Outcome D; CMB axis at (l=60.28°, b=50.48°) σ=0.92°; CMB-LSS = 27.9° (paper-pinned LSS at literature value).
- E1b-prime session: [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md) — Outcome Marginal-D; σ_Hubble tightened 30° → 24.0°; CMB-Hubble at +2.83σ above alignment threshold, not 3σ-decisive.

---

## 1. Pre-registration target

**Test:** re-fit the LSS galaxy-spin-axis dipole direction (and its σ) from raw galaxy-chirality data, replacing the paper-pinned Longo 2011 + Shamir 2020 literal `(l = 32°, b = 32°), σ_LSS = 30°` with a fresh, locally-derived `(l_LSS, b_LSS, σ_LSS)` triple. Recompute the CMB-vs-LSS separation in σ-units, then re-adjudicate C5 against the frozen 2026-05-15 A-034 prereg outcomes (A / C / D / E).

The goal is to settle whether the central-value 27.9° CMB-vs-LSS separation is decisive against alignment at 3σ — which σ_LSS ≈ 30° (literature) is too wide to determine.

**Out of execution scope** (this session): joint Pantheon+ + LSS constraint (Option B; queued follow-up if outcome stays Marginal-D), Observable 5 (E/B polarization), Observable 6 (orbital-plane alignment), Observable 7 (CODATA G P_2 anisotropy), Observable 8 (CMB QNM matching). These are independent workstreams; folding them in exceeds single-session scope per Grant adjudication 2026-05-19 EOD.

---

## 1.5. Picture-first (plumber-physical framing)

**Plumber-physical picture:** at the parent black hole's geometric saturation event, the cosmic-scale K4 lattice was crystallized with the parent BH's spin axis $\hat{S}_{\text{parent}}$ imprinted as its preferred internal direction $\hat{\Omega}_{\text{freeze}}$ (per [`omega-freeze-cosmic-grain-cascade.md:34-40`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)). The I4₁32 chiral space group (Ax 1) means the bond-bowing direction is locked at lattice genesis. If the substrate's chirality leaks into galaxy formation at large scales — by direction-selecting whichever angular-momentum direction was favoured at the K4 grain-coherence scale — then we expect **a non-zero dipole component in the spatial distribution of spiral-galaxy chirality**, with dipole axis aligned with $\hat{\Omega}_{\text{freeze}}$.

This is Observable 3 of the 8-observable Ω_freeze cascade (per [`omega-freeze-cosmic-grain-cascade.md:52`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)).

**Why this is testable now:** the literature pin `σ_LSS = 30°` is dominated by inter-study scatter (Longo 2011 hand-classified ~15k SDSS DR6 spirals; Shamir 2020 algorithmic ~170k SDSS DR8). A direct dipole fit on the full Galaxy Zoo 1 (GZ1) crowdsourced classification of ~667k SDSS DR7 galaxies (Lintott+2008, Lintott+2011, Hayes+2017 bias-corrected subset) should yield σ_LSS in the 5-15° range with the right estimator (Longo 2011 cos γ axial-dipole class, or equivalent χ² minimization on the ±1 chirality assignment).

**Why this is structurally non-circular** (per Grant adjudication 2026-05-19 EOD): SDSS galaxy-chirality data is INDEPENDENT of Planck CMB-axis-of-evil data (different observational instruments, different physics — galaxy morphology vs CMB temperature multipoles). Subtracting any chirality-classification bias does NOT impose the tested direction — bias appears as a monopole, not a dipole. Longo 2011 §3 explicitly addresses this point: an overall L/R-vote bias shows up as a monopole and is removed by the dipole-fit specification.

**Defense-in-depth requirement:** the GZ1 catalog has a known systematic that Hayes+2017 (Galaxy Zoo 1 winding-direction bias correction) identified — clockwise/anticlockwise vote shares are NOT symmetric due to scanner-side handedness preferences. Mitigations applied here:
- Use the (P_CW − P_ACW) signed score per galaxy, which subtracts the per-galaxy monopole. Treat per-galaxy classification as a sign ±1 only when |P_CW − P_ACW| > δ_clear (clear-classification threshold; default δ=0.4 conservative). This subset reproduces Longo 2011's "clear handedness" methodology.
- Report the global monopole asymmetry (Σ chirality)/N as a diagnostic. If significantly nonzero, flag it but proceed — the dipole fit is orthogonal to the monopole.
- Cross-check the dipole-fit result against a single-author algorithmic-chirality catalog (Shamir 2020 / Ganalyzer-class) as a sub-analysis if accessible; defer if not.

---

## 2. Verified state pre-execution (per `verify-before-cite` v1.3)

Phase 0 verifications confirmed at session start (trigger 7c for cross-branch state + trigger 8 for commit-application):

1. **Worktree HEAD verified**: `git log analysis/integration -1 --oneline` returns `5f926ad docs(_orchestration): SDSS DR17 epic ACTIVE — Option A adjudicated`. Worktree initially at `05e2a45` (formatting-linting merge); rebased to integration HEAD `5f926ad` before branch creation.
2. **E1b empirical CMB axis** (load-bearing for post-fit comparison): from `src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer_results.json`, `axis_of_evil_computation.l_deg = 60.2830°`, `b_deg = 50.4800°`, `sigma_deg = 0.9161°`. Confirmed not from literature, computed from Planck PR3 SMICA.
3. **Existing SDSS LSS pin in corpus**: `cmb_axis_alignment_executable_observer.py:97-103` and `cmb_axis_alignment_executable_observer_results.json:20-23` cite Longo 2011 + Shamir 2020 at `(l=32°, b=32°), σ=30°`. **ANOMALY SURFACED — see §2.5 below**.
4. **Constants module**: `src/ave/core/constants.py` exports `C_0` (line 78); no other constants load-bearing for this test (no velocity, no Hubble flow; pure angular geometry).
5. **Python dependencies**: `numpy 2.4.3`, `scipy 1.17.1`, `astropy 7.2.0` (installed mid-Phase-0; required for ICRS→galactic coordinate transform).
6. **Galaxy Zoo 1 catalog availability**: HTTPS `https://static.zooniverse.org/data.galaxyzoo.org/data/gz1/GalaxyZoo1_DR_table2.csv.gz` returns HTTP 200, content-length 20384458 bytes (19.4 MB gzipped, ~75 MB uncompressed). Header column verified by spot-download: `OBJID, RA, DEC, NVOTE, P_EL, P_CW, P_ACW, P_EDGE, P_DK, P_MG, P_CS, P_EL_DEBIASED, P_CS_DEBIASED, SPIRAL, ELLIPTICAL, UNCERTAIN`. 667,944 rows. RA/Dec are sexagesimal strings (J2000), not decimal — parser must handle this.
7. **Cosmic-axes-and-frames-glossary leaf** at [`manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md`](../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md): present in `analysis/integration` after the 2026-05-19 merges. The K4-rest-frame vs $\hat{\Omega}_{\text{freeze}}$ distinction (§5) is load-bearing for the non-circularity argument here too.

**Corpus-grep findings (cross-repo):**
- AVE-Core: 21 hits for "SDSS / galaxy-spin / Longo / Shamir / axis-of-evil / Hayes" — all in research preregs/results docs, archived L3 docs, and the `cmb_axis_alignment_executable_observer.py` driver. No prior SDSS spin-orientation **estimator code** in AVE-Core.
- AVE-QED: 1 hit at `docs/analysis/2026-05-15_Q-G47_session18_A_034_reframing.md` (methodology re-framing for A-034; doesn't compute the LSS axis).
- AVE-PONDER, AVE-HOPF, AVE-APU, AVE-Metamaterials, AVE-Protein, AVE-Engineering, AVE-Manifold, AVE-Cosmology: zero hits. No prior raw-SDSS-chirality dipole estimator anywhere in the AVE workspace.
- **Conclusion**: this is the first raw-SDSS-chirality dipole estimator in the AVE corpus. Methodology must be pinned in detail in this prereg.

### §2.5 — ANOMALY SURFACED (flag-don't-fix per Grant durable directive)

**Discrepancy**: the existing executable observer driver at `cmb_axis_alignment_executable_observer.py:97-103` pins the Longo 2011 SDSS LSS spin-axis at `(l=32°, b=32°)`. However, **the Longo 2011 paper (Phys. Lett. B 699:224) explicitly reports the dipole axis at galactic `(l, b) = (52°, 68.5°)`** corresponding to equatorial `(α_A, δ_A) = (217°, 32°)` (Longo 2011 §3 The Dipole, second paragraph; cf. PDF page 6, line 7).

Mechanism of error: the corpus pin appears to have substituted the equatorial **declination 32°** for the galactic latitude (b) and re-used **32°** for galactic longitude (l) as well, conflating the two coordinate systems. The actual Longo axis is 49° away from the corpus-pinned value (great-circle separation between (32°, 32°) and (52°, 68.5°)).

**Action this session**: NOT silently fixing per flag-don't-fix. Instead:
- This session's empirical re-fit will produce its own independent (l_LSS, b_LSS, σ_LSS) from raw GZ1 data — the corpus pin error is moot for the new measurement.
- The corpus-pin error is surfaced in the result doc + an anomaly will be logged for the auditor lane to land a manual correction or replace the literature pin with the empirical re-fit. Until that lane operates, the (32°, 32°) value remains a corpus anomaly.

This is the second corpus citation-pin error identified in the C5 chain (the first being the 174°, -5° literature placeholder for the CMB axis, now empirically pinned to (60.28°, 50.48°) via E1b execution).

---

## 3. Spin-axis estimator specification (PINNED BEFORE IMPLEMENTATION)

### 3.1 Data source + columns

- **Catalog**: `data/sdss_dr17/GalaxyZoo1_DR_table2.csv` (Galaxy Zoo 1 Table 2 main catalog per Lintott+2011, MNRAS 410:166; matched to SDSS DR7 imaging which is fully contained in DR17). Cached locally via `data/sdss_dr17/` per Pantheon+ pattern.
- **Per-galaxy fields used**:
  - `OBJID` (SDSS unique identifier; not used in fit, kept for reproducibility)
  - `RA` (right ascension, sexagesimal `hh:mm:ss.s` J2000) — parsed to decimal degrees
  - `DEC` (declination, sexagesimal `±dd:mm:ss.s` J2000) — parsed to decimal degrees
  - `NVOTE` (number of volunteer votes for this galaxy)
  - `P_CW` (probability clockwise spiral from raw votes)
  - `P_ACW` (probability anticlockwise spiral from raw votes)
  - `SPIRAL` (Lintott+2011 binary classification flag; 1 if clean spiral by GZ1 criteria)
  - `P_CS` (probability "combined spiral", = P_CW + P_ACW + P_EDGE; sanity gate)

### 3.2 Galaxy selection (Q-cuts)

Cuts applied in order:
1. **Spiral classification**: `SPIRAL == 1` (Lintott+2011 clean-spiral flag — debiased-spiral probability > threshold per their methodology). Removes ellipticals, unclear-morphology, edge-on galaxies.
2. **Minimum vote count**: `NVOTE >= 10` (so vote-share statistics are meaningful per Longo 2011 §2 conservatism).
3. **Chirality clarity**: `|P_CW - P_ACW| >= delta_clear` (default `delta_clear = 0.4`). Galaxies with ambiguous chirality (P_CW ≈ P_ACW) are excluded from the ±1 sign assignment, matching Longo 2011 §2 "scanners were instructed to classify galaxies as Unclear unless the handedness was clear". This delta_clear value is a free hyperparameter; we report sensitivity at `delta_clear ∈ {0.2, 0.4, 0.6}` as a robustness sub-analysis.
4. **Coordinate sanity**: parsed RA in [0°, 360°), Dec in [−90°, +90°).

Per-galaxy chirality assignment after cuts: `chirality_i = +1 if P_CW_i > P_ACW_i else -1` (clockwise = +1, anticlockwise = -1). Sign convention is arbitrary (the axis is direction-only, not a ray); the axial-dipole magnitude is invariant under global sign flip.

### 3.3 Axial-dipole estimator (per Longo 2011 §3)

For each candidate axis direction $\hat{n}_A$ (galactic Cartesian unit vector), compute the dipole asymmetry:

$$A(\hat{n}_A) = \frac{1}{N} \sum_{i=1}^{N} \chi_i \cdot \cos\gamma_i$$

where:
- $\chi_i \in \{-1, +1\}$ is the per-galaxy chirality after cuts
- $\cos\gamma_i = \hat{n}_i \cdot \hat{n}_A$ (line-of-sight projection onto candidate axis)
- $\hat{n}_i$ is the galactic-Cartesian unit vector to galaxy $i$
- $N$ is the post-cut sample size

The best-fit axis $\hat{n}_A^*$ is the one that maximizes $|A(\hat{n}_A)|$ — equivalently, minimizes $\chi^2 = N(1 - A^2)$ where the residual is per-galaxy "expected chirality given dipole magnitude $A$".

**Search strategy**: two-stage HEALPix grid search (mirrors `cmb_axis_alignment_executable_observer.py` Stage 1 + Stage 2 pattern):
- Stage 1: coarse grid at `NSIDE=16` (3072 pixels, ~3.6° pixel size). Compute $A^2$ at each candidate direction; find global maximum.
- Stage 2: refined grid at `NSIDE=64` (~0.9° pixel size) over a 15° cap around Stage 1 best. Final best-fit direction.

Canonicalize to undirected axis: $(l, b)$ and $(l + 180°, -b)$ are equivalent; report in convention $0° \leq l < 180°$.

### 3.4 σ_LSS (the load-bearing quantity)

Direction uncertainty comes from two routes (mirror `c5_pantheon_bulk_flow_tightening.py` Hessian-MC + block-bootstrap pattern):

**(A) Hessian + Monte Carlo.** Compute numerical Hessian of $-A^2$ (acting as a $-\ln L$ proxy) at the best-fit direction in galactic-Cartesian coordinates with the unit-norm constraint imposed via Lagrange multiplier (or equivalently: parameterize the axis as $(l, b)$ and Hessian in those 2 degrees of freedom). Draw 1000 Monte Carlo samples from the Gaussian approximation $\mathcal{N}(\hat{n}_A^*, \Sigma_{\text{Hessian}})$; convert each to $(l, b)$; take the great-circle 68% containment radius around $\hat{n}_A^*$ as σ_Hessian.

**(B) Block bootstrap.** Draw 500 bootstrap resamples (with replacement) of the post-cut galaxy sample; re-fit the axial dipole on each (warm-started from $\hat{n}_A^*$ for speed); take the 68% containment radius of the direction distribution as σ_bootstrap.

**Canonical σ_LSS** = `max(σ_Hessian, σ_bootstrap)` (conservative; matches E1b-prime convention).

### 3.5 Significance test (per Longo 2011 §3 randomization)

To compute the p-value for the observed dipole asymmetry: generate `n_random = 10000` synthetic catalogs by randomly re-assigning $\chi_i \in \{-1, +1\}$ with equal probability to each galaxy (preserving spatial distribution); for each, run the same two-stage HEALPix search; record the resulting $\max_{\hat{n}}|A|$. The p-value is the fraction of random catalogs with $\max|A| \geq |A^*|_{\text{observed}}$.

This is the Longo 2011 §3 procedure for handling the discrete ±1 chirality non-Gaussianity. The p-value is reported alongside the σ_LSS metric. The 3σ-decisive criterion is checked against σ_LSS (the parameter uncertainty on the direction estimate), NOT against the randomization p-value (which is a presence-of-signal test).

### 3.6 Forward-prediction discipline (per `ave-driver-script-honesty` four-discriminator check)

1. **Does the estimator have access to the CMB axis (60.28°, 50.48°) during fitting?** NO. The CMB axis is loaded only for the post-fit comparison; the dipole search sees only galaxy positions + chirality assignments.
2. **Are the starting parameters / grid biased toward the CMB axis?** NO. The HEALPix Stage 1 grid is uniform over the full sphere. No starting direction is favored.
3. **Is the metric $|\hat{n}_A - \hat{n}_{\text{CMB}}|$ or some such alignment functional being minimized?** NO. The fit metric is $-A^2 = -(\langle\chi \cos\gamma\rangle)^2$, direction-agnostic.
4. **Does the result depend on the comparison axis we chose to compare to?** NO. The best-fit direction is independent of which target axis we later use for the separation calculation.

**All four discriminators pass.** The estimator is a forward-prediction.

### 3.7 Substrate-native check (per `substrate-native-check` skill)

This is a phase-space / direction-statistics test, not a continuum-field simulation. The K4 / Cosserat / Op14 substrate-native layer enters the prediction (chirality of bond-bowing direction at lattice genesis = $\hat{\Omega}_{\text{freeze}}$ direction in observable cosmology) but the estimator operates on observational unit-vector data in galactic coordinates. No PML / saturation kernel / eigsolver concerns.

### 3.8 Phase-space coordinate check (per `phase-space-coordinate-check` skill)

Both this test and the corpus claim (CMB axis-of-evil pin at (60.28°, 50.48°), Pantheon+ bulk-flow at (129.76°, -13.64°)) live in galactic coordinates (l, b). The K4 substrate predicts a single $\hat{\Omega}_{\text{freeze}}$ direction in the K4 rest frame = CMB rest frame; galactic coordinates are the standard observational projection of this frame. Coordinate-system match is exact. No real-space ↔ phase-space conversion needed.

### 3.9 Consistency-vs-emergence classification (per `consistency-vs-emergence` v1.1)

**Class E** (operating-point projection / topological-equilibrium observable).

Justification: LSS spin direction is one of 8 projections of $\Omega_{\text{freeze}}$ (per [`omega-freeze-cosmic-grain-cascade.md:46-58`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md)). $\hat{\Omega}_{\text{freeze}}$ is the cosmological initial-data parameter locked at lattice genesis; the prediction is direction-only (not magnitude). Same class as H_∞ (recently reclassified per Thread 2; see [`h-infinity-framing-forward.md`](../_orchestration/h-infinity-framing-forward.md)), $\alpha$, $G$. The test is a CONSISTENCY-CHECK: does the LSS spin axis observable project consistently with the same $\hat{\Omega}_{\text{freeze}}$ direction that the CMB axis observable already pinned?

This is NOT an emergence-class prediction (we are not deriving $\hat{\Omega}_{\text{freeze}}$ from substrate axioms; we are testing whether two independent observables project to the same point in direction space). Result-doc framing per Class E discipline: tighten the central-value separation in σ-units; do NOT headline "AVE prediction confirmed" if the test happens to PASS — frame as "two observables consistently project to a common axis, as the framework asserts they must".

---

## 4. Adjudication mapping (pre-registered, single-table)

Per the brief Phase 3 + the C5 row state:

| Outcome | σ_LSS | CMB-LSS separation in σ | Action |
|---|---|---|---|
| **A — PASS** (tension confirmed) | σ_LSS < 15° | (27.9 − 20) / σ_combined > 3σ — i.e. σ_LSS < 2.5° (unlikely) OR | C5 row → PASS-tension; D4-A034 cosmic instance RETIRES (catalog of 20+ other instances survives). E1c UNBLOCKS via decisive falsification. |
| | | **alt**: the empirical re-fit lands at a direction ≥ 50° from CMB axis, with σ_LSS < 15°, giving 3σ misalignment | |
| **C — NULL** (alignment confirmed) | σ_LSS < 15° | < 3σ separation from 0° | C5 row → NULL-aligned; D4-A034 cosmic instance STRENGTHENS. E1c needs alternative path (e.g. Observable 5/6/7 magnitude test). |
| **D-sustained** | σ_LSS ≥ 25° | not decisive | C5 row → D-sustained; queue joint Pantheon+ + LSS Option B session. E1c stays deferred. |
| **Marginal D** | 15° ≤ σ_LSS < 25° | between 1.5σ and 3σ either way | C5 row → D-refined; queue Option B joint constraint OR Observable 5/6/7. |
| **E — methodology surface** | N/A | estimator fails / structural surprise / GZ1 bias dominates | STOP and report to Grant before retry. |

**Decisiveness against alignment** (PASS-tension) is hard to reach because the central-value 27.9° separation is small. The combined σ would need to satisfy:

$$\text{decisive against alignment} \iff \frac{27.9 - 20}{\sqrt{0.92^2 + \sigma_{\text{LSS}}^2}} > 3\sigma \iff \sigma_{\text{LSS}} < \sqrt{(7.9 / 3)^2 - 0.92^2} \approx 2.46°$$

A σ_LSS < 2.5° is unreachable from any single SDSS-class catalog (the GZ1 vote-share noise alone caps the per-galaxy chirality precision). More likely PASS path: the empirical axis re-fit returns a CENTRAL DIRECTION substantially different from the literature pin AND σ_LSS < 15°, in which case the CMB-LSS separation could grow well past 27.9°.

**Decisiveness for alignment** (NULL-aligned):

$$\text{decisive for alignment} \iff 27.9° < 3\sqrt{0.92^2 + \sigma_{\text{LSS}}^2} \iff \sigma_{\text{LSS}} > \sqrt{(27.9/3)^2 - 0.92^2} \approx 9.25°$$

So if σ_LSS lands in [9.25°, 25°] AND the re-fit central direction stays within 27.9° of the CMB axis (or moves CLOSER), the outcome is **C-NULL (alignment confirmed at 3σ)** — the load-bearing case for un-deferring E1c.

This is the most likely outcome given:
- Longo 2011 reported axis (52°, 68.5°) is only 17.5° from the CMB axis-of-evil (60.28°, 50.48°). Closer than the corpus-cited (32°, 32°) value.
- The full GZ1 catalog (667k galaxies, ~40-100x Longo's effective sample) should tighten σ_LSS substantially.

**3σ-decisive boundary for alignment**: σ_LSS > 9.25° AND CMB-LSS separation < 3σ_combined. Above ~9.3° σ_LSS, the central-value separation 27.9° is consistent-with-alignment at 3σ. Below ~9.3°, the central-value 27.9° separation would itself become 3σ-decisive AGAINST alignment.

### §4.1 — Tie-breakers (pre-registered)

- If σ_LSS from (A) Hessian and (B) bootstrap differ by more than a factor of 1.5, report both, take the LARGER as canonical, add a "Hessian-bootstrap divergence" sub-finding.
- If the two-stage HEALPix search finds multiple local maxima with |A| within 5% of the global maximum, report the second-best direction as a "secondary axis" sub-finding.
- If the post-cuts sample size $N < 5000$ (vs Longo 2011's ~15k), document and proceed — Longo 2011 reached the dipole signal with this sample size.
- If the global monopole asymmetry $\bar{\chi} = (1/N)\sum\chi_i$ exceeds 0.05 in absolute value, flag the GZ1 bias and proceed (dipole fit is orthogonal to monopole; the bias does not directly contaminate the dipole estimate).
- If the dipole magnitude $|A^*|$ from the best fit is below the 1σ tail of the randomization null (i.e., randomization p-value > 0.32), report as automatic **D-sustained** with "dipole-consistent-with-zero" sub-finding, regardless of nominal σ_LSS (the direction is effectively unconstrained when the dipole magnitude is statistically indistinguishable from noise).

---

## 5. Files to produce

- `src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation.py` — driver implementation
- `src/scripts/vol_3_macroscopic/c5_sdss_spin_orientation_results.json` — full numeric output
- `research/2026-05-19_c5-sdss-spin-orientation-result.md` — result doc
- `data/sdss_dr17/GalaxyZoo1_DR_table2.csv` — canonical catalog cache (Phase 1, tracked via gitignore allowlist; ~75 MB; in regular git, no LFS — under 100 MB threshold)
- `data/sdss_dr17/README.md` — re-download instructions + MD5 checksums + provenance
- Updates (in scope):
  - `manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428, 514, 554 — C5 row state with LSS sub-finding
  - `manuscript/ave-kb/common/closure-roadmap.md` — new entry for C5 LSS tightening
  - `_orchestration/c5-sdss-dr17-spin-orientation.md` — IF outcome decisive, status update (orchestration lands the final close; this implementor surfaces only)

Out of scope this session:
- Editing `cmb_axis_alignment_executable_observer.py` to fix the (32°, 32°) corpus pin (anomaly surfaced per §2.5; auditor lane lands the fix)
- Joint Pantheon+ + LSS constraint (Option B; conditional on Marginal-D outcome here)
- Observables 5-8 execution
- `omega-freeze-cosmic-grain-cascade.md:52` "(~1-2σ preferred direction, contested)" wording update — that's an auditor-lane edit after the result lands

---

## 6. Skill discipline applied this session

**Upfront (Phase 0):**
- `pre-test-physics-check` — DONE upstream (Grant's Option A adjudication 2026-05-19 EOD; LSS bias is a known systematic, mitigated per §3.2 delta_clear cut + §1.5 monopole-vs-dipole orthogonality).
- `ave-prereg` — corpus-grep complete (this doc §2 corpus-grep findings; surfaced corpus pin anomaly §2.5).
- `ave-canonical-leaf-pull` — LSS-direction problem class: no prior raw-chirality dipole estimator in any AVE-staging repo. Methodology pinned to Longo 2011 cos γ axial-dipole class (§3.3).
- `ave-canonical-source` — confirmed no Avenir constants are load-bearing for this geometric test; `C_0` import retained for stylistic consistency with the bulk-flow driver but not used in any computation.
- `verify-before-cite` v1.3 — E1b CMB axis verified from JSON file (§2 item 2); GZ1 catalog availability + columns verified via HTTPS HEAD + spot-download (§2 item 6); branch state verified via `git log analysis/integration` + `git merge-base` (§2 item 1).
- `substrate-native-check` — checked (§3.7); no continuum-field machinery needed; substrate-native layer enters the prediction (chirality of bond-bowing direction = $\hat{\Omega}_{\text{freeze}}$ direction in observable cosmology) but not the estimator.
- `phase-space-coordinate-check` — checked (§3.8); both data and corpus claim in galactic (l, b); exact match.
- `consistency-vs-emergence` v1.1 — Class E classified (§3.9); result-doc framing discipline pre-committed (do NOT headline "AVE prediction confirmed" on PASS; frame as "consistent projection of $\hat{\Omega}_{\text{freeze}}$").

**Conditionally (will fire at named gates):**
- `ave-driver-script-honesty` — four-discriminator check captured in §3.6 above; will re-confirm before running estimator.
- `ave-discrimination-check` — IF outcome PASS-tension (>3σ misalignment), apply SM-counterfactual + interpretive-alternatives. SM has no a priori cosmic spin-axis prediction; ΛCDM expects galaxy spin axes to be isotropic at large scales (per cosmological principle). A 3σ-misalignment from CMB axis would be a novel anomaly for ΛCDM, but only "AVE-distinct" if alternative parity-violating cosmological models (e.g., Alexander, Cai, Kim-Naselsky inflationary leptogenesis) are also ruled out.
- `ave-evidence-framing-discipline` — applied at result-doc draft; strength language ("tightens", "decisive") tied to explicit Δσ numbers.
- `ave-walk-back` — IF outcome A or C decisively closes C5, propagate matrix-row + closure-roadmap + 8-observable table at `omega-freeze-cosmic-grain-cascade.md`.
- `flag-don't-fix` — applied to §2.5 corpus pin anomaly (the (32°, 32°) ≠ Longo's actual (52°, 68.5°) discrepancy is surfaced, not silently corrected).

---

## 7. Skill / pre-reg freeze attestation

**This pre-registration is frozen 2026-05-19 before any estimator code is written or any fit run.** Subsequent commits to the driver or result doc on this branch must reference this prereg by file path. Any deviation from §3 (estimator class, Q-cuts, axis-search grid, σ computation method, randomization null) requires an explicit "DEVIATION FROM PREREG" entry in the result doc with justification.

---

*End of pre-registration.*
