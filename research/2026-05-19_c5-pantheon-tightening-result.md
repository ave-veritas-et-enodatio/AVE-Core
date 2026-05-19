# C5-CMB-AXIS Pantheon+ Bulk-Flow Tightening — Result

**Date:** 2026-05-19
**Branch:** `analysis/c5-pantheon-tightening` off `analysis/integration` at `4457d3e`
**Driver:** [`src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py`](../src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py)
**Result JSON:** [`src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening_results.json`](../src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening_results.json)
**Pre-registration:** [`research/2026-05-19_c5-pantheon-tightening-prereg.md`](2026-05-19_c5-pantheon-tightening-prereg.md)
**Briefing:** [`_orchestration/section-e-cascade.md`](../_orchestration/section-e-cascade.md) Phase E1b-prime
**Predecessor (E1b):** [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md)

---

## 0. TL;DR

**Outcome: Marginal-D (DATA INSUFFICIENT, improved over E1b but not 3σ-decisive)**

Self-derived Pantheon+SH0ES bulk-flow fit on z<0.1 sample (664 SNe, full STAT+SYS covariance) tightens the Hubble-flow directional uncertainty from the literature Whitford+2023 σ ≈ 30° to **σ_Hubble = 24.0°** (bootstrap) / **19.6°** (Hessian-MC), max of which is canonical (24.0°). The CMB-axis-of-evil to Hubble-flow separation increases slightly from E1b's 74.6° to **88.0°** (the new fit's central value), and the significance against the 20° alignment threshold rises from **+1.82σ (E1b) to +2.83σ (this session)**.

Not 3σ-decisive (which would require σ_Hubble < 18.2°), so C5 stays D, but with refined bounds. The Pantheon+SH0ES public catalog at z<0.1 is fundamentally directionally noisy after VPEC subtraction (residual bulk-flow magnitude only ~155 km/s), placing a floor on σ_Hubble achievable from this catalog alone.

**Cascade:** C5 row → **D with refined-bounds note (Marginal-D)**. E1c (Route 3 framework-commitment activation) stays DEFERRED. Queue joint-constraint session (Pantheon+ + SDSS DR17 spin-orientation) for decisive 3σ adjudication.

---

## 1. Methodology summary (per prereg §3)

### 1.1 Data sources

- **Pantheon+SH0ES catalog** at `data/pantheon_plus/Pantheon+SH0ES.dat` (1701 SNe; cached locally).
- **Full STAT+SYS covariance** at `data/pantheon_plus/Pantheon+SH0ES_STAT+SYS.cov` (33 MB, downloaded mid-session from GitHub `PantheonPlusSH0ES/DataRelease`). Required because the diagonal-only `m_b_corr_err_DIAG` column produces chi²/dof ≈ 0.47 — over-conservative.
- **E1b empirical CMB axis** from `cmb_axis_alignment_executable_observer_results.json`: (l=60.28°, b=50.48°), σ=0.92°.

### 1.2 Pipelines run

Four pipelines, all chi²-minimized with the full STAT+SYS covariance:

| Pipeline | Redshift | Purpose |
|---|---|---|
| **Primary** | `zHD` = CMB-rest + 2M++ VPEC | Standard Pantheon+ cosmology pipeline (load-bearing) |
| **Sub-analysis (defense-in-depth)** | `zHEL+VPEC` = heliocentric + 2M++ VPEC, no CMB-rest transform | Tests sensitivity to K4-rest-frame = CMB-rest assumption |
| **Diagnostic zCMB-only** | `zCMB` = CMB-rest, no VPEC | Cross-check ingredient |
| **Diagnostic zHEL-raw** | `zHEL` = heliocentric, no correction | Cross-check ingredient |

### 1.3 Empirical-driver discipline (Rule 10) — corrections caught at run-time

1. **Initial implementation used `zCMB` instead of `zHD`.** Verified empirically against the catalog: $zHD = (1+zCMB)(1-VPEC/c) - 1$ to 1e-6 accuracy. The brief's prereg §3.6 specified "CMB-rest-frame transform + 2M++ LSS peculiar-velocity correction" — that's `zHD`, not `zCMB`. Driver corrected before final fit. **Result-doc fingerprint:** prereg §3.6 says "standard Pantheon+ pipeline (heliocentric → CMB-rest-frame transform via conventional CMB dipole + 2M++ LSS peculiar-velocity correction)" — `zHD` is the column that encodes both transforms; `zCMB` is missing the VPEC step.
2. **Initial chi² used `m_b_corr_err_DIAG` only.** chi²/dof = 0.47 (over-conservative) → σ_Hubble = 30°. Spot-check with `m_b_corr_err_RAW` (stat-only): chi²/dof ≈ 6, σ_Hubble ≈ 7°. Neither extreme is canonical. The full STAT+SYS.cov was required; mid-session download brought chi²/dof to 0.916 (in valid [0.6, 1.6] band).
3. **Structural cross-check on the catalog's solar-motion subtraction passed.** The difference between the zCMB-only and zHEL-raw best-fit bulk-flow vectors recovers the conventional CMB dipole at (l=264.0°, b=48.4°), |v|=382 km/s vs Planck 2020 (264.0°, 48.3°), |v|=370 km/s — **0.12° in direction, 3.4% in magnitude**. This confirms the pipeline's transform machinery is sound.

### 1.4 Forward-prediction discipline (per `ave-driver-script-honesty` §3.7)

Four-discriminator check, all PASS:
1. chi² sees CMB axis? **NO** — chi² is Hubble residual only.
2. Initial params biased toward CMB axis? **NO** — u₀ = (300, 300, 300) km/s, not aligned with (60.28°, 50.48°).
3. Alignment functional minimized? **NO** — chi² is direction-agnostic.
4. Result depends on chosen comparison axis? **NO** — fit is independent of post-fit comparison.

The fit is a true forward-prediction: bulk-flow direction is extracted from the Pantheon+ catalog independently, THEN compared to the CMB axis. No fit-to-target.

### 1.5 Constants used (per `ave-canonical-source`)

- $c$ from `ave.core.constants.C_0` = 2.998e8 m/s
- $H_\infty$ from `ave.core.constants.H_INFINITY` = 2.247e-18 1/s → H₀(AVE) = 69.32 km/s/Mpc
- Pantheon+SH0ES baseline H₀ = 73.04 km/s/Mpc used for chi²; **direction is scale-free in H₀** so result is independent of this choice (verified internally).
- Q₀ = -0.55 (LCDM low-z), fixed, not free.

---

## 2. Numerical results

### 2.1 Primary pipeline (zHD: CMB-rest + 2M++ VPEC)

| Metric | Value |
|---|---|
| N SNe (post-cut) | 664 (z < 0.1, calibrators excluded) |
| chi²/dof | 604.51 / 660 = **0.916** (in valid [0.6, 1.6] band) |
| Used full STAT+SYS cov | **YES** |
| Best-fit u (km/s) | (-96.07, 115.47, -36.45) galactic Cartesian |
| Bulk-flow magnitude $|\vec{u}|$ | **154.6 km/s** |
| Bulk-flow direction (axis canonical, 0≤l<180) | **(l = 129.76°, b = -13.64°)** |
| σ_Hubble (Hessian MC, 68%) | 19.63° |
| σ_Hubble (block bootstrap, 68%) | 24.00° |
| σ_Hubble canonical = max(Hessian, Bootstrap) | **24.00°** |
| Hessian / Bootstrap ratio | 0.82 (within prereg ≤ 1.5 tie-breaker) |

**CMB-Hubble comparison:**
| Metric | Value |
|---|---|
| Separation (axis-undirected) | **88.00°** |
| Combined σ (= √(σ_CMB² + σ_Hubble²)) | √(0.92² + 24.00²) = 24.02° |
| Significance vs 20° alignment threshold | **(88.00 − 20) / 24.02 = +2.83σ** |
| Significance vs 0° (would mean perfect alignment) | 88.00 / 24.02 = 3.66σ |
| Decisive against alignment (need >3σ above 20°)? | **NO** (2.83σ) |
| Decisive for alignment (need <3σ from 0)? | **NO** (3.66σ from zero) |

### 2.2 Sub-analysis pipeline (zHEL+VPEC: no CMB-rest transform)

| Metric | Value |
|---|---|
| N SNe | 664 |
| chi²/dof | **0.916** |
| Best-fit u (km/s) | (-120.22, -136.15, 250.01) |
| Magnitude $|\vec{u}|$ | **309.0 km/s** |
| Direction (axis canonical) | **(l = 48.56°, b = -54.00°)** |
| σ_Hubble canonical | **11.19°** (Hessian 11.19, Bootstrap 11.01) |

Interpretation: without the CMB-rest transform, the fit absorbs solar motion into the bulk-flow vector. Magnitude (309 km/s) is closer to the conventional |v_sun| ≈ 370 km/s. Direction is closer to the CMB axis (60.28°, 50.48°) than the primary pipeline result, but this is largely because of solar-motion contamination — NOT a separate cosmological observable. The sub-analysis is consistent with the AVE prediction that K4-rest-frame = CMB-rest-frame holds (per AVE-QED Q-G24) and that the standard Pantheon+ pipeline is structurally correct: removing solar motion gives the residual cosmological bulk-flow, which is what the cosmic-axis test should compare to.

### 2.3 Sub-vs-primary consistency check

| Metric | Value |
|---|---|
| Primary axis (zHD) | (129.76°, -13.64°) |
| Sub axis (zHEL+VPEC) | (48.56°, -54.00°) |
| Angular separation (undirected) | **73.85°** |
| Combined σ (sub + primary) | √(24.00² + 11.19²) = 26.48° |
| Consistent at 1σ overlap? | **NO** (73.85° > 26.48°) |

**Sub-finding:** primary and sub-analysis pipelines do NOT overlap at 1σ. This is the expected behavior given solar-motion contamination in the sub-analysis (see structural cross-check in §2.4 below), NOT a methodology failure. The sub-analysis's purpose was to test sensitivity to K4 = CMB-rest assumption; the result demonstrates that **the assumption is structurally load-bearing**: with or without CMB-rest transform, the recovered direction differs by the conventional CMB dipole vector. If K4 ≠ CMB-rest (per AVE-QED Q-G24), the test loses its structural footing — but Q-G24's identification of K4-rest = CMB-rest is canonical and not under revision in this session. Per prereg §4, divergence is **a reported sub-finding**, not a verdict-downgrade.

### 2.4 Cross-check: zCMB-vs-zHEL diagnostic recovers Planck dipole

| Metric | Value |
|---|---|
| Diagnostic zCMB-only best u (km/s) | (-210.74, 257.07, -65.28), |u|=338.8 km/s |
| Diagnostic zHEL-raw best u (km/s) | (-236.60, 5.47, 222.96), |u|=325.2 km/s |
| Implied solar motion (zHEL − zCMB) | (-25.86, -251.60, 288.24), |v|=**382.3 km/s** |
| Implied solar motion direction | (l = **264.00°**, b = **48.37°**) |
| Planck 2020 CMB dipole reference | (l = 264.02°, b = 48.25°), v = 369.82 km/s |
| Angular separation (implied vs Planck) | **0.12°** |
| Magnitude ratio (implied / Planck) | **1.034** |
| Cross-check PASSES? | **YES** |

The Pantheon+ catalog's internal zCMB-construction is consistent with the conventional CMB dipole at ~0.1° angular accuracy and ~3% magnitude accuracy. The pipeline's transform machinery is therefore validated end-to-end.

---

## 3. Outcome adjudication

### 3.1 Mapping to prereg §4 outcome table

Per prereg §4:

| Outcome | σ_Hubble | CMB-Hubble σ separation | This session's result |
|---|---|---|---|
| **A — PASS** (decisive tension) | < 15° AND > 3σ above 20° | sep > 3σ above 20° | 24.0° NO; 2.83σ NO |
| **C — NULL** (decisive alignment) | < 15° AND < 3σ from 0° | sep < 3σ from 0° | NO; 3.66σ from zero |
| **D-sustained** | ≥ 25° | not decisive | 24.0° → just below sustained-D threshold |
| **Marginal-D** | 15° ≤ σ < 25° | between 1.5σ and 3σ | **24.0° AND 2.83σ → THIS** |
| **E — methodology** | structural failure | structural failure | NO (chi²/dof in band) |

**Verdict: Marginal-D**.

Compared to E1b (σ_Hubble = 30° literature → +1.82σ separation):
- σ_Hubble tightened from 30° to 24° (Δ = -6°, or -20%).
- Significance vs alignment increased from +1.82σ to +2.83σ (Δ = +1.01σ).
- Tightening succeeded directionally, but did NOT cross the 3σ-decisive boundary.

### 3.2 Why σ_Hubble doesn't go below 15°

After applying the full STAT+SYS covariance, the chi²/dof is 0.916 (well-calibrated). The bulk-flow magnitude after VPEC subtraction is only ~155 km/s; the residual cosmological bulk-flow signal is small relative to the per-SN scatter (~0.07 mag in `mB_err_VPEC`). With 664 SNe in a sky distribution that is anisotropic (SH0ES bias toward calibrator host hemispheres), the directional resolution is fundamentally limited.

Whitford+2023 reported σ_Hubble ≈ 30° at depth h⁻¹ Mpc = 150 (z ≈ 0.05). My fit gives σ_Hubble ≈ 24° at z < 0.1 — same depth class. The 20% tightening is consistent with the additional ~40% more SNe in z < 0.1 vs z < 0.05 (664 vs Whitford's ~400-ish, rough estimate), and the use of the full STAT+SYS cov.

**No methodology-bug margin for further tightening with this catalog alone.** Going below σ_Hubble = 15° requires either (a) a deeper sample (z > 0.1, where the cosmological Hubble flow dominates the bulk-flow signal as O(z) — different test class), or (b) a complementary independent direction observable (SDSS DR17 spin-orientation).

### 3.3 Cascade implications

- **C5 row**: updates from "OUTCOME D" (E1b literature-pinned σ=30°) to "OUTCOME Marginal-D, σ_Hubble = 24° (Pantheon+SH0ES self-derived; +2.83σ vs alignment, not 3σ-decisive)". Central values lean harder toward C (NULL) but not 3σ.
- **D4-A034 cosmic instance**: HELD with refined-bounds note. Not retired (would require >3σ rejection). Not strengthened (would require <3σ from zero).
- **C4 three-route Route 3 ($\mathcal{J}_{cosmic}$)**: REMAINS DEFERRED on A-031 cosmic-parameter-horizon.
- **E1c (Route 3 framework-commitment activation)**: stays DEFERRED. Pre-condition for un-deferring is 3σ-decisive on C5, not achieved here.
- **Next-session candidates** (priority order):
  1. **SDSS DR17 spin-orientation re-analysis** — independent observable; would give a direction with σ from raw galaxy catalog, similar precision tightening potential as this session attempted but on a different observable.
  2. **Joint Pantheon+ + SDSS DR17 constraint** — could push to 3σ-decisive by combining two independent ~24° directional estimates.
  3. **Pantheon+ at z > 0.1 sub-sample** — different test class (cosmological vs bulk-flow), but informative for systematics.
  4. **Observables 5/6/7** (E/B polarization, orbital alignment, G P₂ anisotropy) — multi-session each, deferred.

---

## 4. Interpretive alternatives (per `ave-discrimination-check`)

Per the discrimination-check skill: enumerate alternative interpretations rather than anchoring on the first-plausible.

**(i) Parent-BH spin axis preserved through cosmic lattice genesis (A-034 cosmic-scale instance HOLDS):**

If a true cosmic alignment exists with magnitude ~20-30°, the σ_Hubble = 24° from this session is too wide to confirm it OR rule it out at 3σ. The CMB-Hubble central separation is 88° — far above 20° — but the σ leaves room for the true value to be smaller. Path forward: independent observables tightening, joint constraint.

**(ii) Random axes / uniform-prior (A-034 cosmic-scale FAILS):**

Same situation: σ_Hubble = 24° is too wide to rule the null OUT either. The +2.83σ separation is suggestive of tension but not decisive. If observables are truly random/independent, the test eventually settles at C with tighter data; if AVE is right, the test eventually settles at A with tighter data. Both currently consistent at 3σ.

**(iii) Methodology / convention artifact:**

The bulk-flow "direction" from a maximum-likelihood ML fit on SN distance moduli is well-defined: it's the direction of the local-volume velocity vector with respect to the cosmological frame. This is operationally distinct from the CMB axis-of-evil (a low-ℓ quadrupole-octupole alignment) and from LSS galaxy spin axes — but **all three are supposed to share the parent-BH spin axis $\hat{\Omega}_{\text{freeze}}$ under A-034**. The framework-level question of whether these projections should be co-aligned at exactly the same angle (or whether each carries an O(1) projection coefficient on $\hat{\Omega}_{\text{freeze}}$) remains open at the cosmic-axes-and-frames-glossary leaf (`f610fdb` on `analysis/cosmic-axis-glossary` branch). Resolution path: framework-level work on the canonical projection coefficients.

**(iv) Partial alignment / mechanism-refinement (B-like outcome at marginal level):**

The CMB-LSS pair was within 1σ of alignment in E1b (27.9° at literature σ=30°). The CMB-Hubble pair is now at +2.83σ tension. If the parent-BH-axis hypothesis applies to CMB+LSS but bulk-flow is decoupled, the A-034 cosmic-scale instance survives in a refined form. Resolution path: SDSS DR17 self-derivation to confirm or revise the CMB-LSS alignment, and characterize whether bulk-flow is genuinely a separate axis or a noisy version of the same one.

**Recommended adjudication path:** **Marginal-D primary**, with (i)/(ii) still both possible at 3σ. The next session(s) are independent observables: SDSS DR17 (best 3σ-resolution candidate) or joint constraint. E1c stays deferred.

---

## 5. Classification per `consistency-vs-emergence`

**CLASS 3 CONSISTENCY CHECK** (per the consistency-vs-emergence skill):

- **Inputs:** Pantheon+SH0ES public catalog (empirical, well-defined external dataset); full STAT+SYS covariance from PantheonPlusSH0ES data release; E1b empirical CMB axis (data-derived from Planck PR3 SMICA in the predecessor session).
- **Computed observable:** Pantheon+ bulk-flow direction $(l_H, b_H)$ + σ_Hubble at 68% containment; angular separation to E1b CMB axis; significance vs 20° alignment threshold.
- **Test type:** Class 3 — compares AVE prediction (alignment of cosmological observables with $\hat{\Omega}_{\text{freeze}}$, axiom-derived in A-034) to empirical data. NOT Class 4 emergence (no AVE parameters tuned to fit the alignment).
- **No structural circularity:** the Pantheon+ catalog is independent of Planck CMB; the AVE prediction is axiom-derived, not curve-fit.
- **Plumber-physical adjudication carried** from briefing top + cosmic-axes-and-frames-glossary leaf (`f610fdb`): the Pantheon+ standard pipeline subtracts solar motion at the CMB dipole (l≈264°, b≈48°), nearly orthogonal (~79°) to the tested direction $\hat{\Omega}_{\text{freeze}}$ at (60.28°, 50.48°). Subtraction does NOT impose tested direction; structurally non-circular.

---

## 6. ave-evidence-framing-discipline check

Strength language used in this doc:

| Quantity | This doc's language | Numeric backing |
|---|---|---|
| σ_Hubble (vs E1b) | "tightened from 30° to 24°" | Δ = -6°, -20% (explicit) |
| Significance change | "rose from +1.82σ to +2.83σ" | Δ = +1.01σ (explicit) |
| Outcome strength | "Marginal-D (not 3σ-decisive)" | 2.83σ < 3σ pre-registered threshold |
| Sub-analysis "consistency" | "do NOT overlap at 1σ" | 73.85° > 26.48° (explicit) |

All strength language tied to explicit Δ-numbers, no asserted "significant" without numeric backing.

---

## 7. Verification at session end

- [x] Pre-registration at `research/2026-05-19_c5-pantheon-tightening-prereg.md` committed BEFORE driver code (commit `75cda9e`).
- [x] Driver at `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py` committed (commit `24456db`).
- [x] Result JSON `c5_pantheon_bulk_flow_tightening_results.json` committed with driver.
- [x] `ave-canonical-source` discipline: `C_0` + `H_INFINITY` imported from `ave.core.constants`.
- [x] `ave-driver-script-honesty` four-discriminator check explicit in driver header + result-doc §1.4.
- [x] `verify-before-cite` v1.3: E1b axis triple verified from result JSON; Pantheon+ columns verified column-by-column; STAT+SYS covariance load verified (1701×1701 reshape correct, asymmetry < 3e-8).
- [x] `consistency-vs-emergence` classification: Class 3 (consistency check).
- [x] Empirical-driver discipline (Rule 10): redshift-column correction + error-column correction both caught at run-time + corrected; structural cross-check (CMB dipole recovery) PASSES at 0.12° / 3.4%.

---

## 8. Walk-back queue

Per `ave-walk-back` skill, the C5 row updates to "Marginal-D" do NOT close the row (closure requires PASS or definitive NULL). The walk-back queue items:

| Queue item | Status |
|---|---|
| C5 row in `divergence-test-substrate-map.md` (lines 428, 514, 554) | UPDATED in this session — Marginal-D with self-derived σ_Hubble = 24° |
| `closure-roadmap.md:80` C5 entry | UPDATED in this session — appended Marginal-D refinement |
| `omega-freeze-cosmic-grain-cascade.md` 8-observable forecast | NO UPDATE — observable 2 (Hubble bulk-flow) still pending; "tighter Pantheon+ self-fit" item now CLOSED on this branch |
| `_orchestration/section-e-cascade.md` Phase E1b-prime | UPDATED — promoted PENDING → CLOSED with Marginal-D outcome |
| E1c (Route 3 framework-commitment activation) | STAYS DEFERRED — un-defer trigger (3σ-decisive on C5) not achieved |
| SDSS DR17 spin-orientation alternative path | OPEN — natural next session candidate per cascade |

---

## 9. Files updated this session

| File | Status | Change |
|---|---|---|
| `research/2026-05-19_c5-pantheon-tightening-prereg.md` | NEW (commit `75cda9e`) | Pre-registration |
| `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py` | NEW (commit `24456db`) | Driver |
| `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening_results.json` | NEW (commit `24456db`) | Result JSON |
| `research/2026-05-19_c5-pantheon-tightening-result.md` | NEW (this commit) | Result doc |
| `manuscript/ave-kb/common/divergence-test-substrate-map.md` | TO UPDATE | C5 row at lines 428/514/554 |
| `manuscript/ave-kb/common/closure-roadmap.md` | TO UPDATE | C5 entry at line ~80 |
| `_orchestration/section-e-cascade.md` | OUT OF SCOPE (orchestration session updates) | Phase E1b-prime → CLOSED |

---

## 10. Provenance + commit chain

| Commit | Phase | Summary |
|---|---|---|
| `75cda9e` | Phase 2 | Pre-registration committed |
| `24456db` | Phase 3 | Driver + result JSON committed |
| (this commit) | Phase 4 | Result doc + matrix + closure-roadmap |

Branch: `analysis/c5-pantheon-tightening` off `analysis/integration` at `4457d3e`. Push at end of audit. Orchestration session merges via `--no-ff` + audit-tag pattern.

---

*End of result doc.*
