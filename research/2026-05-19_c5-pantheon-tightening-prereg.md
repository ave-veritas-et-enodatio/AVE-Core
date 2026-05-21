# C5-CMB-AXIS Pantheon+ Bulk-Flow Tightening — Execution-Session Pre-Registration

**Date:** 2026-05-19
**Branch:** `analysis/c5-pantheon-tightening` off `analysis/integration` at `4457d3e`
**Status:** EXECUTION-SESSION PRE-REGISTRATION. Frozen BEFORE estimator implementation + data analysis. Subordinate to the frozen 2026-05-15 A-034 methodology prereg at [`research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md`](_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md).

**Briefing:** [`_orchestration/section-e-cascade.md`](../_orchestration/theoretical/section-e-cascade.md) — Phase E1b-prime brief at line 59, promoted ACTIVE 2026-05-19 EOD (commit `4457d3e`).

**Predecessor:** E1b session result doc [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md) returned Outcome D (data-insufficient at 3σ due to literature Whitford+2023 σ_Hubble ≈ 30°).

---

## 1. Pre-registration target

**Test:** re-fit Pantheon+SH0ES Type Ia supernova bulk-flow direction (and its σ) from the raw catalog, replacing the paper-pinned Whitford+2023 literal `(l=323°, b=26°), σ=30°` with a fresh, locally-derived `(l, b, σ_Hubble)` triple. Recompute the CMB-vs-Hubble separation in σ-units using the new σ_Hubble, then re-adjudicate C5 against the frozen 2026-05-15 A-034 prereg outcomes (A / B / C / D / E).

The goal is to settle whether the central-value 74.6° CMB-vs-Hubble separation is decisive against alignment at 3σ — which σ_Hubble ≈ 30° (literature) is too wide to determine.

**Out of execution scope** (this session): SDSS DR17 spin-orientation re-analysis, Observable 5 (E/B polarization), Observable 6 (orbital-plane alignments), Observable 7 (CODATA G P_2 anisotropy). These are independent workstreams; folding them in exceeds single-session scope.

---

## 1.5. Picture-first (plumber-physical framing)

**Plumber-physical picture:** at the parent black hole's geometric saturation event, the cosmic-scale K4 lattice was crystallized with the parent BH's spin axis $\hat{S}_{\text{parent}}$ imprinted as its preferred internal direction $\hat{\Omega}_{\text{freeze}}$. The CMB axis-of-evil (Planck PR3 SMICA) at $(l=60.28°, b=50.48°)$ is the empirical pin on $\hat{\Omega}_{\text{freeze}}$ from low-ℓ multipoles. If the same axis is imprinted on the Hubble-flow direction, then **fitting the bulk-flow direction from Pantheon+SH0ES Type Ia SNe must yield a direction near $\hat{\Omega}_{\text{freeze}}$** — i.e., a bulk-flow vector whose direction is the same axis as the CMB axis-of-evil, modulo the 180° axis-degeneracy (an axis is direction-only, not a ray).

**Why this is testable now:** Whitford+2023's $\sigma_{\text{Hubble}} \approx 30°$ uncertainty (from their reported $(l=323°, b=26°)$ bulk-flow with combined methodology error) is too wide to distinguish "74.6° separation from CMB axis" from "aligned within combined uncertainty" at 3σ. The Pantheon+SH0ES public catalog has 1701 SNe; a direct maximum-likelihood fit on the redshift-distance-direction triple should yield $\sigma_{\text{Hubble}}$ in the 5-15° range with the right estimator (Watkins-Feldman-Hudson 2009 ML class, or equivalent).

**Why this is structurally non-circular (per Grant adjudication 2026-05-19 EOD):** the Pantheon+ standard pipeline subtracts solar motion at the CMB dipole direction $(l \approx 264°, b \approx 48°)$ — angularly separated from $\hat{\Omega}_{\text{freeze}}$ at $(l=60.28°, b=50.48°)$ by ~79° (minimum, accounting for axis degeneracy). The K4 lattice rest frame is identified with the CMB rest frame per AVE-QED Q-G24; $\hat{\Omega}_{\text{freeze}}$ is a separate, nearly-orthogonal concept (parent-BH spin axis preserved through K4 crystallization at lattice genesis). Subtracting the rest-frame velocity does NOT impose the tested direction. See cosmic-axes-and-frames-glossary leaf on `analysis/cosmic-axis-glossary` branch (commit `f610fdb`) for the canonical distinction.

**Defense-in-depth requirement:** the standard pipeline yields the primary fit. A parallel sub-analysis on heliocentric velocities (with only 2M++ LSS peculiar-velocity correction, no CMB-rest-frame transform) provides a structural cross-check. The two fits must overlap within 1σ contour for a clean A/C verdict; divergence is a diagnostic sub-finding reported on its own.

---

## 2. Verified state pre-execution (per verify-before-cite v1.3)

Phase 0 verifications confirmed at session start:

1. **Pantheon+ catalog**: `data/pantheon_plus/Pantheon+SH0ES.dat` — 1702 lines including header (1701 SNe), 47 columns including `zCMB`, `zHEL`, `zHD`, `m_b_corr`, `RA`, `DEC`, `VPEC`, `VPECERR`, `IS_CALIBRATOR`, `USED_IN_SH0ES_HF`. Header verified column-by-column 2026-05-19.
2. **E1b empirical CMB axis**: from `src/scripts/vol_3_macroscopic/cmb_axis_alignment_executable_observer_results.json`, `axis_of_evil_computation.l_deg = 60.2830°`, `b_deg = 50.4800°`, `sigma_deg = 0.9161°`. Confirmed not from literature, computed from Planck PR3 SMICA. Reference axis for this session.
3. **C5 row state in matrix**: `manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428 + 514 + 554 all read "OUTCOME D (DATA INSUFFICIENT at 3σ)" per E1b result.
4. **Constants module**: `src/ave/core/constants.py` exports `C_0` (line 78), `H_INFINITY` (line 534), `R_HUBBLE` (line 537). No hard-coded values of `c` or `H_0` needed in the driver.
5. **Python dependencies**: `astropy 7.2.0` (galactic coordinate transforms via `SkyCoord.transform_to('galactic')`), `scipy 1.15.3` (`scipy.optimize.minimize`, `scipy.stats.chi2`), `numpy` ≥ 2.0.
6. **Worktree on correct HEAD**: `git log analysis/c5-pantheon-tightening -1 --oneline` returns `4457d3e docs(_orchestration): E1b-prime A4 amendment + h-infinity-framing-forward epic spawned`.
7. **Grant's plumber-question adjudication present in briefing**: the K4-rest-frame ↔ $\hat{\Omega}_{\text{freeze}}$ distinction is explicit at briefing top (lines 63-74), resolved 2026-05-19 EOD with quantitative ~79° separation justifying standard-pipeline non-circularity.
8. **Cosmic-axes-and-frames-glossary leaf**: present on `analysis/cosmic-axis-glossary` (commit `f610fdb` + walk-back `f6c227a`), pending merge to `analysis/integration`. The substantive distinction is load-bearing here even though the leaf file itself is not yet on `analysis/integration`.

**Corpus-grep findings (cross-repo):**
- AVE-Core: 45 hits for "bulk_flow / peculiar_velocity / hubble_flow" — all derive from the E1b session's Whitford+2023 paper-pinned reference, the closure-roadmap, and the divergence-test substrate map. No prior raw-SN bulk-flow estimator code in AVE-Core.
- AVE-PONDER, AVE-HOPF, AVE-QED, AVE-APU, AVE-Metamaterials, AVE-Fusion, AVE-Protein, AVE-Tesla, AVE-Propulsion: zero hits. No prior bulk-flow code anywhere in the AVE workspace.
- Conclusion: this is the first raw-SN bulk-flow estimator in the AVE corpus. Methodology must be pinned in detail in this prereg.

---

## 3. Bulk-flow estimator specification (PINNED BEFORE IMPLEMENTATION)

### 3.1 Data source + columns

- **Catalog:** `data/pantheon_plus/Pantheon+SH0ES.dat` (Pantheon+SH0ES public release; cached locally; ESA-equivalent format).
- **Per-SN fields used:**
  - `zCMB` (CMB-rest-frame redshift) — primary-pipeline redshift.
  - `zHEL` (heliocentric redshift) — sub-analysis-pipeline redshift.
  - `m_b_corr` (bias-corrected B-band peak magnitude, used for distance modulus).
  - `m_b_corr_err_DIAG` (diagonal magnitude uncertainty).
  - `RA`, `DEC` (equatorial degrees, J2000) — converted to galactic $(l, b)$ via `astropy.coordinates.SkyCoord`.
  - `IS_CALIBRATOR` (1 = SH0ES Cepheid host calibrator, EXCLUDED from cosmological fit per Pantheon+ convention).
  - `USED_IN_SH0ES_HF` (1 = used in SH0ES Hubble-flow; required filter for low-z fit).

### 3.2 Redshift cut

- **z < 0.1** cut on `zCMB` (primary) or `zHEL` (sub-analysis). The dipole-flow regime: at $z > 0.1$, structural Hubble flow dominates and the bulk-flow signal averages out. The Whitford+2023 analysis depth was $h = 150~h^{-1}$ Mpc ≈ $z \sim 0.05$; this session's z<0.1 cut is comparable.
- Calibrator SNe excluded (`IS_CALIBRATOR == 1`).

### 3.3 Distance estimator

For each SN:

$$\mu_i = m_{B,i}^{\text{corr}} - M$$

with the absolute magnitude $M$ marginalized out as a free nuisance parameter in the fit (its scale-free direction is the bulk-flow vector). The "predicted" distance modulus from a Hubble-flow model:

$$\mu^{\text{pred}}_i(z_i; H_0, \vec{u}) = 5 \log_{10}\!\left[ \frac{c\, z_i}{H_0} \left(1 + \frac{1}{2}(1 - q_0) z_i\right) \right] + 25 + \frac{1}{c \ln 10}\, \frac{\vec{u} \cdot \hat{n}_i}{z_i}$$

(low-z bulk-flow correction; per Watkins-Feldman-Hudson 2009 eq. 9, equivalent to perturbing the velocity-redshift relation). Here:
- $\vec{u}$ is the local-volume bulk-flow vector (km/s) — three free parameters.
- $\hat{n}_i$ is the unit direction to SN $i$ in galactic coords.
- $q_0 = -0.55$ (LCDM low-z, fixed; not free).
- $c$ from `ave.core.constants.C_0` in m/s.
- $H_0$ from `ave.core.constants.H_INFINITY` (AVE prediction) for primary pipeline; cross-check at $H_0 = 73$ km/s/Mpc (Pantheon+SH0ES baseline) for residual check. The fit is **scale-free in direction**: the bulk-flow direction is independent of $H_0$.

The fit minimizes:

$$\chi^2(\vec{u}, M) = \sum_i \frac{[\mu_i - \mu_i^{\text{pred}}(\vec{u})]^2}{\sigma_{\mu,i}^2}$$

with $\sigma_{\mu, i}$ from `m_b_corr_err_DIAG`. Three parameters ($u_x, u_y, u_z$ in galactic Cartesian) plus $M$ as a degenerate offset.

### 3.4 Bulk-flow direction extraction

After minimization, $\vec{u}_{\text{fit}}$ in galactic Cartesian is converted to:
- Direction $(l_{\text{Hubble}}, b_{\text{Hubble}}) = \arctan(u_y / u_x)$, $\arcsin(u_z / |\vec{u}|)$.
- Magnitude $|\vec{u}|$ (km/s).
- Direction is **undirected** (axis): $(l, b)$ and $(l+180°, -b)$ are equivalent. We canonicalize to $0° \le l < 180°$ for consistency with the E1b axis-of-evil convention.

### 3.5 σ_Hubble (the load-bearing quantity)

Bulk-flow direction uncertainty comes from two routes:

(A) **Hessian + bootstrap composite.** Hessian-based 1σ contour around the best-fit $\vec{u}$, propagated to angular uncertainty on $(l_{\text{Hubble}}, b_{\text{Hubble}})$ by Monte Carlo: draw 1000 samples from $\mathcal{N}(\vec{u}_{\text{fit}}, \Sigma_{\text{Hessian}})$, convert each to $(l, b)$, take the angular dispersion (great-circle 68% containment radius) as $\sigma_{\text{Hubble}}$.

(B) **Block-bootstrap on the SN catalog.** Draw 500 bootstrap resamples (with replacement) of the SN catalog, re-fit $\vec{u}$ on each, take the 68% containment radius of the direction distribution as the bootstrap σ. Report both; canonical $\sigma_{\text{Hubble}}$ is the LARGER of (A) and (B) (conservative).

### 3.6 Velocity-convention sub-analyses

Per Grant's adjudication and A4 of the brief:

- **Primary pipeline** — use `zCMB` (CMB-rest-frame redshift). This is the standard Pantheon+ pipeline. Subtracted solar-motion direction $(l \approx 264°, b \approx 48°)$ is ~79° from $\hat{\Omega}_{\text{freeze}}$ at $(l = 60.28°, b = 50.48°)$, so the subtraction does not impose the tested direction.
- **Sub-analysis pipeline (defense-in-depth)** — use `zHEL` (heliocentric redshift, no CMB-rest-frame transform). Apply only the `VPEC` 2M++ LSS correction. This is the "if our K4=CMB-rest-frame identification is wrong, would the answer change?" cross-check.

Both pipelines produce $(l, b, \sigma_{\text{Hubble}})$ triples. They must overlap within 1σ for the primary result to count as clean. Divergence is itself a sub-finding.

### 3.7 Forward-prediction discipline (per ave-driver-script-honesty)

**Four-discriminator check:**
1. **Does the estimator have access to the CMB axis $(60.28°, 50.48°)$ during fitting?** NO. The CMB axis is loaded only for the post-fit comparison; the χ² minimizer sees only Pantheon+ data + $H_0$.
2. **Are the starting parameters $\vec{u}_0$ biased toward the CMB axis?** NO. The minimizer starts at $\vec{u}_0 = (300, 300, 300)$ km/s — a generic non-zero initial point, NOT aligned with $\hat{\Omega}_{\text{freeze}}$. Alternative starting points tested: $\vec{u}_0 = (0, 0, 0)$, $(370, 0, 0)$, $(0, 370, 0)$, $(0, 0, 370)$, and a CMB-axis-aligned start; if minimizer is non-pathological all converge to the same minimum (we verify this).
3. **Is the metric $|\hat{u}_{\text{fit}} - \hat{n}_{\text{CMB}}|$ or some such alignment functional being minimized?** NO. The χ² is the standard Hubble-residual χ², direction-agnostic.
4. **Does the result depend on the comparison axis we chose to compare to?** NO. The fit yields a direction $(l, b, \sigma_{\text{Hubble}})$ irrespective of which target axis we choose for post-fit separation calculation.

**All four discriminators pass.** The estimator is a forward-prediction.

---

## 4. Adjudication mapping (pre-registered, single-table)

Per the brief Phase 4 + A8:

| Outcome | $\sigma_{\text{Hubble}}$ | CMB-Hubble separation in σ | Action |
|---|---|---|---|
| **A — PASS** (tension confirmed, sustained) | $\sigma_{\text{Hubble}} < 15°$ | $\frac{74.6 - 20}{\sigma_{\text{combined}}} > 3\sigma$ | C5 row → PASS; E1c UNBLOCKS. D4-A034 cosmic instance RETIRES (catalog of 20+ other instances survives). |
| **C — NULL** (alignment confirmed, < 3σ separation) | $\sigma_{\text{Hubble}} < 15°$ | $< 3\sigma$ | C5 row → NULL/PASS-aligned; E1c needs alternative path. D4-A034 cosmic instance STRENGTHENS. |
| **D-sustained** | $\sigma_{\text{Hubble}} \ge 25°$ | not decisive | C5 row → D-sustained; queue SDSS DR17 session. E1c stays deferred. |
| **Marginal D** | $15° \le \sigma_{\text{Hubble}} < 25°$ | between 1.5σ and 3σ | C5 row → D-refined; queue joint-constraint session. |
| **E — methodology surface** | N/A | estimator fails / structural surprise | STOP and report to Grant before retry. |

**Decisiveness against alignment** depends on whether the central-value 74.6° separation exceeds the 20° pre-registered alignment threshold by 3σ.

$$\text{decisive} \iff \frac{74.6° - 20°}{\sqrt{0.92°^2 + \sigma_{\text{Hubble}}^2}} > 3\sigma \iff \sigma_{\text{Hubble}} < \sqrt{(54.6 / 3)^2 - 0.92^2} \approx 18.2°$$

So $\sigma_{\text{Hubble}} < 18.2°$ gives 3σ-decisive against alignment (tension/PASS). The brief's 15° target is conservative.

**Decisiveness for alignment** depends on whether the 74.6° separation falls within the combined 3σ:

$$74.6° < 3 \sqrt{0.92°^2 + \sigma_{\text{Hubble}}^2} \iff \sigma_{\text{Hubble}} > 24.9°$$

So $\sigma_{\text{Hubble}} > 24.9°$ leaves alignment possible at 3σ. Between 18.2° and 24.9° is the marginal-D window.

**Sub-analysis consistency** is a separate condition: both pipelines (zCMB-primary, zHEL-sub) must overlap within 1σ. If they diverge, both directional outputs are reported as a sub-finding, the primary verdict is downgraded (PASS → marginal-A; D-sustained stays D-sustained; etc.), and a methodology investigation is queued.

---

## 5. Adjudication tie-breakers (pre-registered)

- If $\sigma_{\text{Hubble}}$ from (A) Hessian and (B) bootstrap differ by more than a factor of 1.5, report both, take the LARGER as canonical, and add a "Hessian-bootstrap divergence" sub-finding.
- If the χ² minimizer fails to converge or finds multiple local minima ≥ 5% apart in χ² value, surface to Grant as Outcome E.
- If the redshift cut z<0.1 produces fewer than 500 SNe in the fit sample, document the count and proceed (Pantheon+ should have ≳ 1400 at z<0.1).
- If the bulk-flow magnitude $|\vec{u}|$ comes out at < 50 km/s (consistent with zero), the direction is effectively unconstrained; report this as an automatic D-sustained with a "magnitude-consistent-with-zero" sub-finding, regardless of nominal $\sigma_{\text{Hubble}}$.

---

## 6. Files to produce

- `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening.py` — driver implementation
- `src/scripts/vol_3_macroscopic/c5_pantheon_bulk_flow_tightening_results.json` — full numeric output
- `research/2026-05-19_c5-pantheon-tightening-result.md` — result doc

Updates (in scope):
- `manuscript/ave-kb/common/divergence-test-substrate-map.md` lines 428, 514, 554 — C5 row state
- `manuscript/ave-kb/common/closure-roadmap.md` line ~80 — C5 entry
- `_orchestration/section-e-cascade.md` Phase E1b-prime section — CLOSED status + outcome summary

---

## 7. Skill discipline applied this session

**Upfront:**
- `pre-test-physics-check` — DONE upstream (Grant's adjudication 2026-05-19 EOD captured in briefing top).
- `ave-prereg` — corpus-grep complete (this doc §2 corpus-grep findings).
- `ave-canonical-leaf-pull` — data-fitting class: confirmed no prior raw-SN bulk-flow code in AVE-Core. Methodology pinned to Watkins-Feldman-Hudson 2009 ML class (per A4 of brief).
- `ave-canonical-source` — `C_0`, `H_INFINITY` imports confirmed in §2.
- `verify-before-cite` v1.3 — E1b axis triple verified from result JSON (§2 item 2); Pantheon+ columns verified column-by-column (§2 item 1); briefing commit `4457d3e` verified (§2 item 6).

**Conditionally (will fire at named gates):**
- `ave-driver-script-honesty` — four-discriminator check captured in §3.7 above; will re-confirm before running estimator.
- `ave-discrimination-check` — IF outcome PASS, apply SM-counterfactual: SM has no a priori bulk-flow direction prediction; SM mass distribution is statistical and would average to zero at depth.
- `ave-evidence-framing-discipline` — applied at result-doc draft; strength language ("tightens", "decisive") tied to explicit Δσ_Hubble numbers.
- `ave-walk-back` — IF outcome A or C closes C5, propagate matrix-row + closure-roadmap.

---

## 8. Skill / pre-reg freeze attestation

**This pre-registration is frozen 2026-05-19 before any estimator code is written or any fit run.** Subsequent commits to the driver or result doc on this branch must reference this prereg by file path. Any deviation from §3 (estimator class, redshift cut, fit parameters, σ_Hubble computation method, sub-analysis pipeline) requires an explicit "DEVIATION FROM PREREG" entry in the result doc with justification.

---

*End of pre-registration.*
