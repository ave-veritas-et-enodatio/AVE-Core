# RESULT — Graded-region pulse reflection Γ(A) on the srs scalar TLM engine (means-test Class C)

Prereg-file: research/2026-08-24_engine-gamma-meanstest_prereg_FROZEN.md

**Pair of** the prereg named on the line above (NOT edited — every departure is a
dated DEVIATION entry in §D below).
**Run date:** 2026-08-24. **Runner:** firewalled from the prereg author; the prereg
was executed as the spec.
**Post-verify amendment:** 2026-08-24 — §AMD below carries the corrected quantitative
record after the 3-lens adversarial verify; §REPAIR logs the disposition of every
verify finding. The frozen adjudication text of §6 is preserved as written.
**Driver:** `research/drivers/engine_gamma_meanstest.py` (NEW code; imports the engine
READ-ONLY, and the chart forms from `src/ave/viz/ave_chart.py` on branch
`infra/2026-08-24-ave-chart-instrument`. The run of record executed it from a run
workspace against the AVE-Core main checkout at commit `90753eef`, whose
`chiral_lattice.py` / `chiral_lattice_dynamics.py` / `viz/style.py` were verified
byte-identical (`cmp`) to the branch copies before the run; the landed driver resolves
both from the enclosing checkout — see D11).
**Per-run V3 check:** `research/drivers/engine_gamma_meanstest_check_sentinels.py`
(consumes the shipped sentinel series; output recorded verbatim in §AMD-3).
**Raw data:** `research/drivers/data/engine_gamma_meanstest/raw_{GJ,GB,GT}.json` (full
F/B/back-monitor/sentinel time series per grid point), `.../cold_sanity.json`,
`research/drivers/engine_gamma_meanstest_results.json`.
**Figure:** `research/figures/2026-08-24-engine-gamma-meanstest/fig1_gamma_overlay.png`
/ `.pdf` (white house style via `ave.viz.style.apply`, Okabe-Ito, no title, legend
outside the data). The plotted G-T series is the CONVERGED-window one (§AMD-1); the
frozen-window G-T points are kept on the same axes as muted × markers so the figure
and the §4 table can be read against each other.
**Log:** `research/drivers/data/engine_gamma_meanstest/run_log.txt` (the driver prints
every parameter it actually uses).

## Scope block (prereg §1, restated verbatim as binding)

This test measured the **medium's response map** — the reflection of a probe pulse off
an imposed, static, kernel-shaped grading. The following conclusion-shapes are
FORBIDDEN in this document regardless of what the run shows:

- "therefore a bound state / electron can (or cannot) form";
- "therefore the energize-LOCK negative is explained away / reopened";
- "therefore an eigenmode exists / does not exist";
- any charge-sector, winding, or spin statement.

The only claims produced: (i) the measured Γ(A) locus per imposed grading geometry,
(ii) the frozen qualitative classification of each locus (§6 of the prereg), (iii) the
resulting adjudication of the J/B/taper fork as response-map forms.

## 1 — Config echo + config-grep rerun (prereg §3, on the ACTUAL driver)

Run configuration actually executed (from the driver's printed parameter block,
`run_log.txt`): `build_srs_net(L=24, enantiomorph="right")` → N = 110 592 nodes,
degree 3, carrier `srs-z3`; `scalar_tlm_step`-equivalent per-node scatter+connect
(CONNECT map untouched, gate CS-4); geometry in cells: x_s=2, x_p=6, x_I=9, x_B=15,
W=6, N_taper=3, wrap margin 11; launch = baseband Gaussian σ_x=1.5 cells,
+x̂-directional weighting, peak amplitude 0.7047; A-grid = 16 points
{0.0 … 0.99}; 48 runs of T=170 steps; hard cap 6000 not approached.

Config-grep rerun against the driver (patterns word-bounded; line numbers are those of
the landed `research/drivers/engine_gamma_meanstest.py`, re-verified after the
post-verify repair edits — all four greps were re-run on the amended file and still
return 0, as do the same four on `engine_gamma_meanstest_check_sentinels.py`):

| §3 config key | grep | result on the actual driver |
|---|---|---|
| drive / pump for t>0 | `grep -cniE "\b(pump\|drive\|driven\|inject\|source_term)\b" engine_gamma_meanstest.py` | **0 hits.** The field is set once at t=0 (`launch()`, defined at :310, called at :318 inside `run()` and at the two CS-gate sites :413/:428); the loop body is scatter+connect only. |
| tunable dt / integrator limit | `grep -cnwE "dt\|dt0\|timestep" engine_gamma_meanstest.py` | **0 hits.** The TLM step IS the discrete bond transit; no dt exists, no dt→0 limit is takeable. |
| eigensolve | `grep -cnE "\beig[a-z]*\(\|linalg\.(eig\|eigh\|eigsh)" engine_gamma_meanstest.py` | **0 hits.** Time-domain scattering only. |
| medium↔field self-consistency | read of `step_graded` (`engine_gamma_meanstest.py:302-308`): body is `w = (a_nodes*V).sum(1); V_ref = w[:,None]-V; connect` | **No A-update, no V-dependence of S.** Scatter coefficients are built ONCE per run from the frozen A-field (`build_scatter`, :289), SHA-256-hashed at t=0 (:299) and re-verified at end-of-run (:879) — all 48 runs `sha_ok=True`. What that checksum can and cannot detect is stated in §7 V2; it is not the load-bearing freeze evidence on its own. |
| second carrier / winding observables (#417) | `grep -niE "omega_b\|omega_s\|winding\|poloidal\|toroidal" engine_gamma_meanstest.py` | **0 hits.** One scalar per port; observable is signed Γ only. |

The §3 structural proof therefore holds on the run as executed: genesis requires
(precursor ∧ pump ∧ self-consistency); this config has none of the three conjuncts.
No closed negative (§3.1 energize-LOCK, §3.2 #415, §3.3 #417) is reconstructed.

## 2 — Cold sanity gate (prereg §5) — **PASS (all five)**

| gate | measured | frozen criterion | verdict |
|---|---|---|---|
| CS-1 closed-system conservation (uniform scatter, actual launch pulse, 200 steps) | max rel drift **1.667e-14** | < 1e-10 | **PASS** |
| CS-2 network factor (`network_velocity_factor`, which wraps `measure_dispersion`; m=1..4, axis=x — see D8/D9) | **0.580513** (the gated k→0 polyfit-in-k² extrapolation) vs analytic 1/√3 = 0.5773503; rel dev **0.548 %**. The prereg's literal "at the smallest k" reading is **0.580972** (c(k₁)/c_link, c_link = `mean_bond_length` = 1.0 to float precision — 1.0000000000000002 on the L=24 net), rel dev **0.627 %** | < 2 % | **PASS on both readings** |
| CS-2 band edge | c(k) = {0.5810, 0.5791, 0.5758, 0.5759} at k = {0.0926, 0.1851, 0.2777, 0.3702}; all within 5 % of c₀ ⇒ k_edge = 0.3702; pulse spectral energy below edge = **0.9737 (analytic) / 0.9588 (discrete FFT, per-cell bins)** | ≥ 0.95 | **PASS** |
| CS-3 time-of-flight | v = **0.56948** vs c₀ = 0.58051; rel dev **1.90 %**; t_centroid = 19.87, σ_t = 4.81 steps | < 5 % | **PASS** |
| CS-4 graded-path regression (all-cold per-node S vs uniform `scatter_matrix(3)`, 200 steps) | max abs dev **1.776e-15** | ≤ 1e-12 | **PASS** |
| CS-5 null calibration (A=0 through the full pipeline, per config) | \|Γ\| = **0.00545** for G-J, G-B, G-T (identical: A=0 IS the cold lattice) | < 0.02 each | **PASS** |

Derived adjudication constants (frozen formulae): ε₀ = **0.00545**;
θ = max(3ε₀, 0.05) = **0.05000**; δ = max(ε₀, 0.01) = **0.01000**.

## 3 — Windows (derived from cold measurements + measured graded transit)

Incident window [10, 29] (t_cF ± 2σ_t); reflected window **[30, 78]** for all three
configs. Expected front-echo centroid 49.1 steps (measured τ* confirms: G-J locks at
τ* = 30 ≈ the 2×3-cell echo delay 29.5). Earliest transmitted centroid at the back
monitor (plane x = 15.5 cells, D10): 66.2 (G-J) / 65.9 (G-T) ⇒ slab-back first return
at the probe ≈ 112.5/112.2; close bound from that path = **93.26 / 92.95**
(recomputed 2026-08-24 from the shipped t_back_return and σ_t — the earlier
93.1/92.8 was an arithmetic slip in this narrative sentence; the bound is
non-binding either way, and the windows are unchanged: see §AMD-4). Wrap contaminant
(direction-resolved sentinel at x = 19.5, threshold 1 % of launch envelope): earliest
projected probe arrival **87.776** over ALL 48 runs ⇒ binding close = 87.776 − 2σ_t
= 78.16 → 78. Windows constructible with positive width for every config (V3),
incident/reflected disjoint by construction (V4), and no projected contaminant
arrival precedes any window close in any of the 48 runs — **the per-run check is
`engine_gamma_meanstest_check_sentinels.py`, whose full output is recorded in
§AMD-3** (48/48 PASS, earliest 87.77589, reconciled to 0.0e+00 against the driver's
own cold-run projection). The driver itself derives the close from the COLD run's
sentinel only; the per-run re-verification lives in that script and nowhere else.

## 4 — Measured Γ(A) (48-point table; both estimators; frozen flags)

Signed convention (frozen at prereg §4.4): Γ < 0 = polarity-inverted echo
(short-like), Γ > 0 = same-polarity echo (open-like), matching Γ = (z−1)/(z+1).

> **Reading note (post-verify, 2026-08-24).** The three tables below are the FROZEN
> record: extracted in the frozen reflected window [30, 78]. G-J is converged in that
> window (invariant here for any close in 60–85; and at L = 32 per the numerical
> verify lens's independent rerun). **G-T is not** — its echo is delayed and
> time-stretched and the wrap-bound close clips its tail, biasing
> |Γ_GT| LOW. The converged G-T locus is §AMD-1's table; every G-T magnitude below is
> a **lower bound** on the converged value. No verdict in §6 changes (all move
> a fortiori).

### G-J (far-side slab)

| A | Gamma_meas (matched) | \|Gamma\|_E | tau* [steps] | discordance | flag |
|---|---|---|---|---|---|
| 0.0 | -0.00545 | 0.01831 | 8 | 0.257 | UNRELIABLE |
| 0.1 | -0.00556 | 0.01835 | 8 | 0.256 | UNRELIABLE |
| 0.2 | -0.00536 | 0.01904 | 30 | 0.274 | UNRELIABLE |
| 0.3 | -0.01203 | 0.02190 | 30 | 0.197 | valid |
| 0.4 | -0.02201 | 0.02877 | 30 | 0.135 | valid |
| 0.5 | -0.03613 | 0.04089 | 30 | 0.095 | valid |
| 0.6 | -0.05586 | 0.05955 | 30 | 0.062 | valid |
| 0.7 | -0.08402 | 0.08730 | 30 | 0.037 | valid |
| 0.8 | -0.12695 | 0.13038 | 30 | 0.026 | valid |
| 0.85 | -0.15872 | 0.16249 | 30 | 0.023 | valid |
| 0.9 | -0.20436 | 0.20876 | 30 | 0.021 | valid |
| 0.925 | -0.23690 | 0.24181 | 30 | 0.020 | valid |
| 0.95 | -0.28248 | 0.28816 | 30 | 0.020 | valid |
| 0.9682 | -0.33243 | 0.33899 | 30 | 0.019 | valid |
| 0.98 | -0.38211 | 0.38957 | 30 | 0.019 | valid |
| 0.99 | -0.45280 | 0.46149 | 31 | 0.019 | valid |

### G-B (single crossing bond)

| A | Gamma_meas (matched) | \|Gamma\|_E | tau* [steps] | discordance | flag |
|---|---|---|---|---|---|
| 0.0 | -0.00545 | 0.01831 | 8 | 0.257 | UNRELIABLE |
| 0.1 | -0.00554 | 0.01831 | 8 | 0.255 | UNRELIABLE |
| 0.2 | -0.00580 | 0.01834 | 8 | 0.251 | UNRELIABLE |
| 0.3 | -0.00378 | 0.01853 | 12 | 0.295 | UNRELIABLE |
| 0.4 | -0.00402 | 0.01910 | 16 | 0.302 | UNRELIABLE |
| 0.5 | +0.00576 | 0.02045 | 39 | 0.294 | UNRELIABLE |
| 0.6 | +0.00877 | 0.02318 | 39 | 0.288 | UNRELIABLE |
| 0.7 | +0.01306 | 0.02821 | 39 | 0.303 | UNRELIABLE |
| 0.8 | +0.01961 | 0.03730 | 39 | 0.354 | UNRELIABLE |
| 0.85 | +0.02452 | 0.04464 | 39 | 0.402 | UNRELIABLE |
| 0.9 | +0.03173 | 0.05574 | 39 | 0.431 | UNRELIABLE |
| 0.925 | +0.03703 | 0.06400 | 39 | 0.421 | UNRELIABLE |
| 0.95 | +0.04475 | 0.07606 | 39 | 0.412 | UNRELIABLE |
| 0.9682 | +0.05378 | 0.09005 | 39 | 0.403 | UNRELIABLE |
| 0.98 | +0.06353 | 0.10499 | 39 | 0.395 | UNRELIABLE |
| 0.99 | +0.07923 | 0.12862 | 39 | 0.384 | UNRELIABLE |

### G-T (3-cell taper)

| A | Gamma_meas (matched) | \|Gamma\|_E | tau* [steps] | discordance | flag |
|---|---|---|---|---|---|
| 0.0 | -0.00545 | 0.01831 | 8 | 0.257 | UNRELIABLE |
| 0.1 | -0.00546 | 0.01832 | 8 | 0.257 | UNRELIABLE |
| 0.2 | -0.00403 | 0.01870 | 48 | 0.293 | UNRELIABLE |
| 0.3 | -0.00904 | 0.02045 | 48 | 0.228 | UNRELIABLE |
| 0.4 | -0.01657 | 0.02503 | 49 | 0.169 | valid |
| 0.5 | -0.02737 | 0.03373 | 49 | 0.127 | valid |
| 0.6 | -0.04251 | 0.04771 | 49 | 0.104 | valid |
| 0.7 | -0.06413 | 0.06896 | 49 | 0.070 | valid |
| 0.8 | -0.09695 | 0.10228 | 49 | 0.052 | valid |
| 0.85 | -0.12104 | 0.12718 | 49 | 0.048 | valid |
| 0.9 | -0.15519 | 0.16306 | 49 | 0.048 | valid |
| 0.925 | -0.18242 | 0.18869 | 50 | 0.033 | valid |
| 0.95 | -0.21698 | 0.22465 | 50 | 0.034 | valid |
| 0.9682 | -0.25445 | 0.26419 | 50 | 0.037 | valid |
| 0.98 | -0.29954 | 0.30375 | 51 | 0.014 | valid |
| 0.99 | -0.35452 | 0.36060 | 51 | 0.017 | valid |

**Per-config extraction validity (frozen §4.4 rule: > 4 unreliable points ⇒
INVALID-EXTRACTION):** G-J 3 unreliable → valid; G-T 4 unreliable → valid;
**G-B 16/16 unreliable → INVALID-EXTRACTION** (no adjudication for G-B; reported as
such per §8).

## 5 — Classifiers (prereg §6.2, computed on valid points)

| classifier | G-J | G-B | G-T |
|---|---|---|---|
| n_valid | 13 | 0 (invalid-extraction) | 12 |
| SIGN_top (at A=0.99) | **−** | — | **−** |
| CROSSING | none | — | none |
| FLOOR (extrapolated intercept, valid 0<A≤0.5) | +0.0248 → **no floor** (\|int\| < θ=0.05) | — | +0.0266 → **no floor** |
| MONOTONE (±δ) | **yes, decreasing** | — | **yes, decreasing** |
| positive Γ>θ at A≤0.5 | no | — | no |
| TAPER-SUPPRESSED (\|Γ_GT\| < ½·\|Γ_GJ\| on A∈[0.5,0.9] where \|Γ_GJ\|>θ) | — | — | **NO** — frozen-window ratio \|Γ_GT\|/\|Γ_GJ\| = 0.759–0.764 at the band points (0.6, 0.7, 0.8, 0.85, 0.9); band point A=0.5 excluded (\|Γ_GJ\| = 0.036 < θ). **Those ratios are window-truncation-biased LOW; the converged ratios are 0.772–0.814 and A-dependent (§AMD-1).** The criterion is < 0.5 either way, so the classifier output NO is unchanged and strengthened. |

## 6 — Adjudication (frozen rules quoted verbatim, then applied)

### 6.1 G-J

> **Frozen §6.3:** "**G-J draws J-class** iff: no CROSSING ∧ SIGN_top = − ∧ MONOTONE.
> With FLOOR ⇒ full Form-J signature; without FLOOR ⇒ 'floorless negative (core/J-class)
> locus' — the side-assignment content of J (graded far arms ⇒ deepening negative echo,
> never a polarity flip) is still drawn; the floor verdict is recorded separately."

Applied: no crossing ∧ SIGN_top = − ∧ monotone = TRUE; FLOOR = FALSE.
**G-J verdict: J-class drawn in the floorless variant — "floorless negative
(core/J-class) locus."** The floor verdict (no floor) is recorded separately, and is
the outcome the prereg's own floor-honesty note foresaw (T4 homogenization: the −1/3
intercept belongs to the isolated vertex, which does not exist in-lattice).

*Report-against observation (non-adjudicating, §6.5):* the measured G-J locus lies on
the lumped **core** curve Γ = (√S−1)/(√S+1) to 0.2–2 % across the entire reliable grid
(ratio Γ_meas/Γ_core = 1.021 at A=0.3 falling to 0.998 for A ≥ 0.8; e.g. measured
−0.33243 at A=0.9682 vs core −0.33318; measured −0.45280 at A=0.99 vs core −0.45392) —
i.e. the in-lattice far-side slab reflects as a plane impedance interface at the
canonical z(A) = √S(A), not with the lumped-J magnitudes (lumped J at A=0.99 is
−0.684). Quantitative deviation from all lumped curves was declared EXPECTED and
adjudicates nothing; the closeness to core is reported for the record.

### 6.2 G-B

> **Frozen §4.4:** "Discordance \|(\|Γ_meas\| − \|Γ\|_E)\| / max(\|Γ\|_E, θ) > 0.2 at a
> grid point marks the point UNRELIABLE; > 4 unreliable points in one config ⇒ that
> config is INVALID-EXTRACTION (no adjudication for it; reported as such)."

Applied: all 16 G-B points exceed the 0.2 discordance bound (range 0.25–0.43).
**G-B verdict: INVALID-EXTRACTION — no adjudication.** Physical reading (recorded, not
adjudicating): the one-bond biased layer is a thin two-interface composite (the
prereg's own DECLARED CAVEAT); its echo is small (matched-filter values −0.006 to
+0.079, i.e. mostly below or near θ) and time-spread beyond the incident template
(τ* drifts 8→39), so the matched-filter and energy estimators disagree by
construction. The frozen B-signature (one −→+ crossing, endpoint +) can be neither
confirmed nor refuted from this geometry at this pulse bandwidth.

**The sign of the G-B matched-filter points carries NO directional information —
struck 2026-08-24 (post-verify).** An earlier draft of this row recorded that the
(unreliable) matched-filter points "turn positive for A ≥ 0.5 … a hint in the
direction of the B-form's sign structure". That hint is a **window artifact** and is
withdrawn in full. Re-extracting the same shipped G-B series against a sweep of
reflected-window closes flips the sign: at A = 0.5 and A = 0.9 alike, Γ_GB is
**negative at close 60, positive at 64/70/78/85, negative again at 95** (§AMD-2 has
the table; the close-95 values are past the 87.776-step contaminant front and are
contaminant, but the 60-vs-64 flip is entirely inside the uncontaminated range).
G-J under the identical perturbation is sign- and value-stable to five decimals
across closes 60–85.
The correct statement is therefore the artifact itself: **the G-B echo is so far
below the estimator pair's reliability bound that even its sign is selected by the
window** — which is what INVALID-EXTRACTION means, independently confirmed. Nothing
about the B-form's sign structure is hinted at, in either direction.

### 6.3 G-T

> **Frozen §6.3:** "**G-T draws the taper expectation** iff: TAPER-SUPPRESSED ∧ no
> FLOOR ∧ no CROSSING in G-T."
> **Frozen §6.2:** "TAPER-SUPPRESSED: \|Γ_GT(A)\| < ½·\|Γ_GJ(A)\| [ENGINEERING-CHOICE:
> factor ½] at EVERY grid A ∈ [0.5, 0.9] where \|Γ_GJ(A)\| > θ."
> **Frozen §6.4:** "G-T fails taper suppression | the taper expectation is REFUTED (a
> qualitative surprise; reported prominently — an adiabatic ramp reflecting ≥ a step is
> a real finding about the graded medium)."

Applied: no FLOOR ∧ no CROSSING = TRUE, but TAPER-SUPPRESSED = FALSE (frozen-window
ratio 0.759–0.764 at the band points, criterion < 0.5). **G-T verdict: the frozen
taper expectation is NOT drawn (fails the factor-½ suppression).** Prominence with
honesty: the §6.4 framing "an adiabatic ramp reflecting ≥ a step" did NOT occur —
\|Γ_GT\| < \|Γ_GJ\| at every valid point (the NONE trigger "\|Γ_GT\| ≥ \|Γ_GJ\| > θ"
never fires). What the lattice drew is a taper suppressed by only ×0.76, not ×½: a
3-cell linear ramp against a pulse of σ_x = 1.5 cells is evidently not deep in the
adiabatic regime. The frozen engineering choice (factor ½) is what failed; the
direction of the effect (taper reflects less than step) is as expected.

> **Quantitative amendment (2026-08-24, post-verify) — the verdict above is
> unchanged; the number in it is not.** The "×0.76" is window-truncation-biased.
> Converged (§AMD-1), the in-band ratio is **0.772 → 0.814, rising with A** (and
> 0.885 at A = 0.99, outside the frozen band). The frozen criterion recomputed on the
> converged numbers is still FALSE at every band point, by a factor of ~1.6, so
> "fails the factor-½ suppression" holds **a fortiori** — the correction moves the
> measurement AWAY from suppression, never toward it. Read "×0.76" above as
> "×0.77–0.81 (frozen-window reading 0.76)". The physical reading is unchanged and
> slightly sharpened: a 3-cell ramp probed by a σ_x = 1.5-cell pulse suppresses the
> echo by ~20 %, not by half, and suppresses it LESS as the grading deepens.

### 6.4 Fork adjudication (frozen §6.4 outcome table applied)

> **Frozen §6.4 rows:** "G-J draws J-class AND G-B draws B-class ⇒ BOTH forms validated
> …" / "G-J draws J-class, G-B = NONE (or vice versa) ⇒ the NONE-side lumped form is
> REFUTED …" / "both stepped configs draw the SAME class ⇒ … DEGENERATE …" /
> "both NONE ⇒ …" / "G-T fails taper suppression ⇒ the taper expectation is REFUTED …"

- **J side:** G-J draws J-class (floorless variant). The side-assignment content of J —
  graded far arms produce a deepening negative echo with no polarity flip — is drawn by
  the lattice.
- **B side:** G-B is INVALID-EXTRACTION, which is neither "draws B-class" nor "NONE".
  **No §6.4 row fires for the J/B pair; the J/B side-assignment fork is NOT adjudicated
  by this run and remains open on the B side.** (Frozen §8: per-config
  INVALID-EXTRACTION "voids that config's adjudication only; the run survives for the
  other configs.")
- **Taper:** the taper-suppression expectation at the frozen factor ½ is REFUTED;
  reported prominently in §6.3 above with the honest direction statement.
- The floor VALUE −1/3 and crossing LOCATION √15/4 stay report-against only (§6.5):
  no floor was measurable at either stepped config; no crossing existed to compare
  against √15/4.

## 7 — VOID checks (prereg §8)

| condition | status |
|---|---|
| V1 cold sanity | **not triggered** — all five CS gates pass (§2) |
| V2 grading leaks into dynamics | **not triggered** — E_Y relative drift ≤ 1.54e-14 over all 48 runs (gate 1e-8); CS-4 regression 1.78e-15 ≤ 1e-12; SHA-256 of the stacked per-node S array re-verified at end-of-run in all 48 runs (`sha_ok=True` ×48). **SHA-gate scope, stated exactly (reworded 2026-08-24, post-verify):** the t=0 hash (`engine_gamma_meanstest.py:299`) and the end-of-run hash (`:879`) are both computed from the SAME in-memory `a_nodes` array. The check can therefore detect **in-place mutation of that array during the run, and nothing else**; it is NOT evidence that the stepper read S from that array rather than from some copy or other source, and it cannot detect a leak that never writes back. It satisfies the prereg §4.2/§8 letter and it CAN fire (in-place mutation is the live leak channel for this code shape), but it is not the load-bearing evidence. The freeze is over-determined by three independent things that ARE load-bearing: the E_Y drift bound, CS-4, and the structural read of `step_graded` (`:302-308` — no A-update, no V-dependence of S, so no feedback path exists to leak through). The reverse structural-null lens holds: the grading IS in the dynamics as a static scatterer (measured Γ responds to A) and ONLY as a static scatterer. |
| V3 wrap-around / contamination | **not triggered at L=24** — windows constructible with positive width; earliest projected contaminant arrival 87.776 > close 78 in **all 48 runs**, machine-checked per run by `engine_gamma_meanstest_check_sentinels.py` (full output §AMD-3; 48/48 STRICT PASS, 48/48 also pass the stricter guarded bound 87.776 − 2σ_t = 78.16 ≥ 78). The driver does NOT perform this per-run check — it derives the close from the cold run's sentinel alone; the check script is the receipt. (At the prereg's default L=16 V3 WAS triggered — see DEVIATION D1.) |
| V4 window overlap | **not triggered** — incident [10,29], reflected [30,78], disjoint |
| per-config INVALID-EXTRACTION | **G-B triggered** (16/16 unreliable); G-J (3) and G-T (4) below the >4 bound |

## D — DEVIATIONS (dated amendments; the prereg file is untouched)

- **D1 (2026-08-24) — L = 16 → 24 [within E1's own latitude].** E1 freezes L=16 with
  the rider "any L ≥ 12 satisfying the V3 timing budget is acceptable, recorded if
  changed." Measured at L=16: the backward-launch residual (~9 % of the pulse in
  coherent probe-sum amplitude) wraps the 3-cell margin (12-cell path) and arrives at
  the probe at t ≈ 48–68 — inside the reflected window (echo centroid ≈ 49): the
  window is non-constructible and V3 fires. L=24 (wrap margin 11 cells) moves the
  wrap arrival to ≈ 98 projected (87.8 with the 1 %-front definition), cleanly after
  the echo. Recorded per E1; all other E2 geometry offsets kept as frozen.
- **D2 (2026-08-24) — launch weighting sign.** The literal §4.3 formula
  max(0, +x̂·b̂) weights the ports whose incident wave ARRIVES from the +x side, which
  launches a −x̂-traveling pulse (verified empirically: the pulse reached the probe on
  the backward ports via the wrap path). The frozen GEOMETRY (source at x_I−7 firing
  into the interface; "the incident wave arrives on a cold feed bond") requires the
  +x̂-propagating pulse, i.e. weight = max(0, −x̂·b̂). Geometry controls; the sign was
  corrected and the correction is recorded here (`engine_gamma_meanstest.py:226-237`).
- **D3 (2026-08-24) — V3 sentinel operationalization.** The prereg names the sentinel
  ("field magnitude at the wrap-margin plane opposite the source") but fixes neither
  plane, threshold, nor how a sentinel crossing maps to probe contamination. Declared
  in the driver: plane x = 19.5 cells (mid wrap margin, 6.5 cells min-image from the
  source so the launch tail ~8e-5 cannot false-trigger); direction-resolved port sums
  on the crossing bonds; contaminant-front threshold 1 % of the unit launch envelope;
  projection to the probe along the crossing direction (−x̂: (x_sent−x_p) cells; +x̂:
  (box−x_sent+x_p) cells) — 13.5 and 10.5 cells respectively; the earliest projected
  arrival, minus the 2σ_t guard, bounds the window close.
  *(Corrected 2026-08-24, post-verify: this entry previously ended "…and the per-run
  check of §7 re-verifies it on every run", which asserted a verification no shipped
  code performed — the driver projects from the COLD run's sentinel only
  (`engine_gamma_meanstest.py:529`). The per-run check now EXISTS as
  `engine_gamma_meanstest_check_sentinels.py`, has been run, and its output is §AMD-3.
  The claim's CONTENT was true — 48/48 pass, earliest 87.77589 — but it was declared
  before it was computed.)*
- **D4 (2026-08-24) — CS-2 discrete band cross-check method.** The pulse's spectral
  fraction below the band edge is computed both analytically (erf(k_edge·σ_x) for the
  Gaussian envelope) and discretely (rfft of the launched envelope binned at ONE bin
  per cell — intra-cell binning would alias srs motif granularity, which is lattice
  structure, not propagating pulse content). Gate applied to the smaller of the two
  (0.9588 ≥ 0.95).
- **D5 (2026-08-24) — gate ordering.** CS-5's extraction needs windows, and the
  G-J/G-T window close consumes "measured graded transit times" (prereg §4.4), so the
  48 graded runs were EXECUTED (data collection only) after CS-1..CS-4 passed and
  before CS-5 was adjudicated; no graded data was interpreted before CS-5 passed. Had
  CS-5 failed, the run would have been declared VOID with the graded data
  uninterpreted.
- **D6 (2026-08-24) — result-file naming.** The Class-C row specifies the result as a
  research-pair `..._result.md` landing via reviewed PR; the run itself was executed
  from a run workspace (`prereg_FROZEN.md` / `result.md` / `driver.py` /
  `check_sentinels.py` / `data/` / `gamma_overlay.*`). The landed names are
  `research/2026-08-24_engine-gamma-meanstest_{prereg_FROZEN,result}.md`,
  `research/drivers/engine_gamma_meanstest{.py,_results.json}`,
  `research/drivers/engine_gamma_meanstest_check_sentinels.py`,
  `research/drivers/data/engine_gamma_meanstest/{raw_*,cold_sanity}.json` +
  `run_log.txt`, and
  `research/figures/2026-08-24-engine-gamma-meanstest/fig1_gamma_overlay.{png,pdf}`
  (the dated-lane figure subdirectory follows the sibling
  `research/figures/2026-08-24-ave-chart-instrument/figN_*` convention). All internal
  cross-references in this document use the landed names.

### D-entries added 2026-08-24 in the post-verify repair

These are driver operationalizations that were **in the executed code and printed in
`run_log.txt`, but absent from this register** — the omission was in the register, not
in the run. Prereg §9.2 requires every departure to be a dated entry; these are those
entries. None changes a gate outcome, a classifier, or a verdict (each states its own
verdict-invariance evidence).

- **D7 (2026-08-24) — matched-filter estimator operationalizations.** Prereg §4.4
  freezes "Γ_meas = (Σ_t B(t)·F(t−τ*)) / (Σ_t F(t−τ*)²) … τ* = argmax over lag of
  |cross-correlation(B, F)|". `extract_gamma`
  (`engine_gamma_meanstest.py:355-400`) adds two things the prereg does not state:
  **(a) a lag-admissibility cutoff** — only lags whose shifted template carries ≥ 25 %
  of its energy inside the reflected window are eligible (`:389`,
  `if den < 0.25 * E_tmpl: continue`); **(b) a mask-restricted denominator** — the
  denominator is the shifted template's energy *inside the reflected window*
  (`:388`, `den = (sh[mask]**2).sum()`), not the full template energy. (a) exists to
  regularize the den→0 pathology at extreme lags; without it the argmax is free to
  select a lag where a sliver of template overlaps the window and divide by ~0.
  **Verdict-invariance:** for every reported VALID point the locked-lag template lies
  fully inside the reflected window (checked explicitly at the extended close — the
  `tmpl_contained` field is True for all 16 G-T points, §AMD-1), so (b) is inert on
  the reported table; where it is not inert (near-edge lags) it can inflate |Γ| by at
  most 1/0.25 = 4×, which is exactly what (a) caps. G-B is voided by the discordance
  gate regardless of τ*; G-J and G-T lock τ* at the physical echo delay. Both
  operationalizations were documented in the function's own docstring at run time; the
  docstring now also names them as D7.
- **D8 (2026-08-24) — CS-2 network-factor reading.** Prereg §5 CS-2 says "the extracted
  network factor c/c_link **at the smallest k** must match ANALYTIC_NETWORK_FACTOR …
  within 2 %". The driver calls `network_velocity_factor`
  (`engine_gamma_meanstest.py:445`), which WRAPS the prereg-named `measure_dispersion`
  (same measurement) and returns `c0` = the k→0 extrapolation of a linear fit in k²
  (`chiral_lattice_dynamics.py:139-160`), and the gate is applied to that. Both
  readings are recorded and **both pass**: extrapolated **0.580513** (rel dev
  **0.548 %**) and at the smallest k **0.580972** (rel dev **0.627 %**), against
  1/√3 = 0.5773503 with c_link = `mean_bond_length` = 1.0 to float precision. (The verify lens
  quoted the smallest-k reading as "0.5810 / 0.633 %"; 0.633 % is what the 4-dp-rounded
  0.5810 gives — 0.6322 % — while the shipped full-precision value 0.5809720966 gives
  0.6273 %. Same quantity, rounding-order difference; both far inside the 2 % gate.
  Recomputed in the amendment block of the results JSON, `cs2_readings`.)
- **D9 (2026-08-24) — CS-2 dispersion axis.** `dispersion_axis = 0` (x̂, the
  propagation axis of this test) where the engine default is axis = 2 (ẑ)
  (`engine_gamma_meanstest.py:148`, printed in the parameter block). The prereg names
  the measurement but not the axis. Measuring dispersion along the axis the probe
  actually travels is the physically correct choice here; the scalar srs mode is
  isotropic to within the CS-2 band tolerance, so this is a declaration, not a result.
- **D10 (2026-08-24) — back-monitor plane.** `back_monitor_x = 15.5` cells
  (`engine_gamma_meanstest.py:129`) is the plane that operationalizes prereg §4.4's
  "measured graded transit times" for the slab-back close bound: half a cell past the
  slab back x_B = 15. The prereg fixes no monitor plane. This bound was never binding
  (93.26 / 92.95 vs the wrap bound 78.16), so the window is unaffected by the choice.
- **D11 (2026-08-24, landing-time, post-verify) — path resolution in the landed
  driver.** The executed driver hard-coded the run-workspace paths (AVE-Core main
  checkout `src/`, and `ave_chart.py` by file path from the chart-instrument
  worktree). The landed driver resolves the engine `src/` and `ave_chart.py` from the
  ENCLOSING checkout, falling back to the recorded run-workspace paths, and writes its
  outputs to the landed names when it sits in `research/drivers/`
  (`engine_gamma_meanstest.py:56-94`). This is a path change, not an engine change:
  the three engine files were verified byte-identical (`cmp`) between the two
  checkouts at run time, and a full rerun of the landed driver reproduces the frozen
  block of the results JSON byte-for-byte and the three `raw_*.json` files exactly
  (§AMD-5).

## 8 — Bottom line (quantitative record as amended — §AMD)

Cold gate: **PASS** (all five, §2). The lattice, asked which lumped form is the real
response map of each bias geometry, answered:

- **The far-side (junction-side-bias) geometry draws the J-class signature in its
  floorless variant** — monotone deepening negative echo, no polarity flip, no
  measurable −1/3 floor — and quantitatively it draws the **core** locus
  (z = √S plane-interface reflection) to ~1 %. This locus is **fully converged**:
  identical to five decimals for any reflected-window close in 60–85, and (per the
  numerical verify lens's independent rerun, not reproduced here) at L = 32.
- **The bond-side geometry could not be adjudicated**: the one-bond layer's echo sits
  below the frozen estimator pair's reliability bound at every A (16/16 discordant ⇒
  INVALID-EXTRACTION), and the post-verify window sweep shows the residual signal is
  so weak that even its SIGN is window-selected (§AMD-2). The J/B fork stays open on
  the B side; no §6.4 row fires.
- **The taper suppresses reflection by ~20 %, not by half.** The converged in-band
  ratio |Γ_GT|/|Γ_GJ| is **0.772 at A = 0.6 rising to 0.814 at A = 0.9** (0.885 at
  A = 0.99, outside the frozen band) — a taper that suppresses LESS as the grading
  deepens. The frozen factor-½ suppression expectation is **REFUTED**, and refuted
  more decisively than the frozen-window numbers (0.759–0.764) showed: the truncation
  bias ran toward the criterion, and removing it moves every band point further from
  it. A 3-cell linear ramp probed by a σ_x = 1.5-cell pulse is simply not in the
  adiabatic regime; direction-of-effect (taper < step) holds at every valid point.

No VOID condition fired (§7); no closed negative's config was reconstructed (§1). The
quantitative record of record for G-T is §AMD-1's converged table, not §4's
frozen-window table; the verdicts are §6's and are unchanged.

## AMD — POST-VERIFY AMENDMENT (dated 2026-08-24)

Three adversarial verify lenses (config-compliance, physics, numerical) returned
DEFECTS-FOUND on this document: one MAJOR (the G-T quantitative record is
window-truncation-biased) and ten MINOR (provenance/declaration class). **No verify
finding changed any verdict**, and none is contested. This section carries the
corrected quantitative record; the frozen adjudication text of §6 is preserved as
written, with pointers here. §REPAIR logs the disposition of every finding
individually.

### AMD-1 — G-T is window-truncated; the converged locus (repairs the MAJOR)

**The defect.** §4/§5/§6.3/§8 banked the taper suppression as "ratio 0.76 ± 0.01 at
every band point". That ±0.01 is not honest: the G-T reflected waveform is still
arriving when the frozen window closes. G-J's echo is a front-face reflection that
lands at τ* = 30 and is essentially over by t ≈ 60 — in-window centroid 50.3 and
97 % of its in-window energy inside [40, 60] at A ≥ 0.9. G-T's is a *distributed*
reflection off a 3-cell ramp, so it is both later and time-stretched: τ* = 48–55,
in-window centroid 61.6 (A = 0.5) → 70.1 (A = 0.9) → 72.0 (A = 0.99), with only
6 % of its energy in G-J's [40, 60] band at A = 0.9. The frozen close at t = 78
clips its tail, and the clipped fraction GROWS with A — exactly the direction that
flattens the measured ratio into a spurious constant.

**The convergence probe.** Re-extract Γ from the SAME shipped raw series with the
reflected window extended to close **85** — the largest close still strictly before
the earliest projected contaminant arrival (87.776 steps, all 48 runs, §AMD-3). No new
lattice run is involved; only the extraction window moves. This close is deliberately
NOT guard-protected (the frozen rule wants a 2σ_t = 9.61-step guard, and 87.776 − 85 =
2.78), which is why it is a **convergence probe and not a re-adjudication**: the
frozen extraction keeps the guarded close of 78.

**Four independent convergence receipts, so the probe is not just another window:**

1. **Template containment.** At close 85 the τ*-locked shifted template lies entirely
   inside the reflected window at every one of the 16 grid points (`tmpl_contained` =
   True ×16; spans in the table below, max [65, 84] ⊂ [30, 85]). Once the template is
   contained, widening the window further cannot change the estimator — and it does
   not: close 85 and close 95 give bit-identical Γ_GT for every A ≥ 0.7.
2. **Post-window tail energy.** Over the valid band A ≥ 0.5, the reflected-trace
   energy left OUTSIDE the window falls from **10.5 % → 33.5 %** at the frozen close
   (rising with A — the truncation signature) to **3.3 % at A = 0.5 and ≤ 1.9 % for
   A ≥ 0.6** at the extended close (≤ 1.1 % for A ≥ 0.7). The G-J control at the
   frozen close is ≤ 1.0 % for A ≥ 0.5 and ≤ 0.03 % at the top of the grid, against
   G-T's 19–33 % there — G-J was never truncated. The A ≤ 0.3 rows of the tail table
   are the near-null points where B is noise at the ε₀ level and neither fraction
   means anything; they are shown for completeness, not as evidence.
3. **Lattice-size cross-check (from the numerical verify lens, not re-run here).** An
   independent L = 32 rerun (262 144 nodes; window re-derived to [30, 93], bound by
   the slab-back return instead of by wrap, so guard-protected) returned
   Γ_GT = −0.02765 / −0.16628 / −0.40070 at A = 0.5 / 0.9 / 0.99, against this
   amendment's L = 24 close-85 values −0.02765 / −0.16629 / −0.40073: **max |Δ| =
   3e-5**. The truncation, not the lattice size, was the cause.
4. **G-J invariance control.** Γ_GJ is bit-identical between the frozen and extended
   windows at all 16 points (`GJ_unchanged_at_extended_close` = True), and invariant
   for any close in 60–85. The correction is specific to the distributed taper echo,
   not a global re-scaling of the extraction.


**The converged G-T locus** (frozen-window value, converged value, their
difference, the converged energy cross-check, the locked lag and its template span,
the converged reliability flag, and both suppression ratios against the same
— unchanged — Γ_GJ). Rows with no ratio are the A-points where G-J itself is
unreliable or A = 0:

| A | Γ_GT frozen (close 78) | Γ_GT converged (close 85) | Δ | \|Γ\|_E conv | τ* conv | template span | flag conv | ratio frozen | ratio converged |
|---|---|---|---|---|---|---|---|---|---|
| 0.0 | -0.00545 | -0.00545 | +0.00000 | 0.01882 | 8 | [18, 37] | UNRELIABLE | — | — |
| 0.1 | -0.00546 | -0.00546 | +0.00000 | 0.01885 | 8 | [18, 37] | UNRELIABLE | — | — |
| 0.2 | -0.00403 | -0.00403 | +0.00000 | 0.01930 | 48 | [58, 77] | UNRELIABLE | — | — |
| 0.3 | -0.00904 | -0.00905 | -0.00002 | 0.02122 | 51 | [61, 80] | UNRELIABLE | 0.751 | 0.753 |
| 0.4 | -0.01657 | -0.01671 | -0.00014 | 0.02614 | 51 | [61, 80] | valid | 0.753 | 0.759 |
| 0.5 | -0.02737 | -0.02765 | -0.00028 | 0.03540 | 51 | [61, 80] | valid | 0.758 | 0.765 |
| 0.6 | -0.04251 | -0.04314 | -0.00063 | 0.05030 | 51 | [61, 80] | valid | 0.761 | 0.772 **[band]** |
| 0.7 | -0.06413 | -0.06556 | -0.00144 | 0.07313 | 51 | [61, 80] | valid | 0.763 | 0.780 **[band]** |
| 0.8 | -0.09695 | -0.10062 | -0.00367 | 0.10947 | 52 | [62, 81] | valid | 0.764 | 0.793 **[band]** |
| 0.85 | -0.12104 | -0.12719 | -0.00615 | 0.13712 | 52 | [62, 81] | valid | 0.763 | 0.801 **[band]** |
| 0.9 | -0.15519 | -0.16629 | -0.01110 | 0.17774 | 53 | [63, 82] | valid | 0.759 | 0.814 **[band]** |
| 0.925 | -0.18242 | -0.19497 | -0.01255 | 0.20732 | 53 | [63, 82] | valid | 0.770 | 0.823 |
| 0.95 | -0.21698 | -0.23635 | -0.01937 | 0.24956 | 54 | [64, 83] | valid | 0.768 | 0.837 |
| 0.9682 | -0.25445 | -0.28295 | -0.02851 | 0.29692 | 54 | [64, 83] | valid | 0.765 | 0.851 |
| 0.98 | -0.29954 | -0.33067 | -0.03113 | 0.34507 | 55 | [65, 84] | valid | 0.784 | 0.865 |
| 0.99 | -0.35452 | -0.40073 | -0.04621 | 0.41522 | 55 | [65, 84] | valid | 0.783 | 0.885 |

**Post-window tail energy** — the receipt behind receipt 2 above. Fractions are
Σ B² over the stated step range divided by Σ B² inside the corresponding window:

| A | G-T tail [79,86] / in-window(78) | G-T tail [86,87] / in-window(85) | G-J tail [79,86] / in-window(78) |
|---|---|---|---|
| 0.0 | 6.03 % | 9.35 % | 6.03 % |
| 0.1 | 6.23 % | 9.37 % | 5.95 % |
| 0.2 | 6.92 % | 9.12 % | 5.42 % |
| 0.3 | 8.12 % | 7.81 % | 3.96 % |
| 0.4 | 9.44 % | 5.46 % | 2.19 % |
| 0.5 | 10.50 % | 3.27 % | 1.01 % |
| 0.6 | 11.46 % | 1.88 % | 0.44 % |
| 0.7 | 12.73 % | 1.14 % | 0.18 % |
| 0.8 | 14.85 % | 0.79 % | 0.08 % |
| 0.85 | 16.57 % | 0.71 % | 0.05 % |
| 0.9 | 19.21 % | 0.70 % | 0.03 % |
| 0.925 | 21.16 % | 0.72 % | 0.03 % |
| 0.95 | 23.94 % | 0.78 % | 0.02 % |
| 0.9682 | 26.96 % | 0.87 % | 0.02 % |
| 0.98 | 29.82 % | 0.96 % | 0.02 % |
| 0.99 | 33.49 % | 1.09 % | 0.02 % |

**What the correction does to the record.** The per-point shift reaches
Δ = −0.046 at A = 0.99 (4.6 % of full scale, and 4.6× the frozen per-point noise
band δ = 0.01), so the frozen table's G-T magnitudes are lower bounds, not
measurements, at high A. The suppression ratio is not a constant at all: it rises
monotonically from 0.765 (A = 0.5) through 0.772 / 0.780 / 0.793 / 0.801 to 0.814
(A = 0.9) and on to 0.885 at A = 0.99. The physical reading changes from "a taper
suppresses by a fixed ~24 %" to **"a taper suppresses by ~19–23 % in the frozen
band, and suppresses LESS as the grading deepens"** — the ramp becomes
progressively less adiabatic relative to the shrinking wavelength inside the graded
region as A → 1.

**Every frozen verdict survives, computed rather than asserted.** The frozen
criterion is **Frozen:** `|Γ_GT(A)| < ½·|Γ_GJ(A)|` at every band point; recomputed
on the converged numbers it is FALSE at all five band points (0.772, 0.780, 0.793,
0.801, 0.814 — each ≥ 1.54× the criterion), so **TAPER-SUPPRESSED = FALSE and the
taper expectation is REFUTED a fortiori**: the truncation bias was pushing the
measurement TOWARD the criterion, and removing it pushes every band point further
away. The rest of the G-T classifier set is likewise unchanged on the converged
table: SIGN_top = − (A = 0.99), crossings = none, MONOTONE = yes/decreasing,
FLOOR = no (intercept +0.0271 vs +0.0266 frozen, both < θ = 0.05), 4 unreliable
points (gate is > 4) so the extraction stays valid, and the valid/unreliable
partition of the 16 G-T points is identical to the frozen one.

**One honest wrinkle in the probe.** Widening the window also widens the unsigned
energy cross-check |Γ|_E, which picks up more late-time tail, so the discordance
metric shifts slightly: at close 85 the G-J point at A = 0.3 crosses the 0.2 bound
(0.197 → 0.206) and would count as unreliable, taking G-J from 3 to 4 unreliable
points (still inside the > 4 gate, extraction still valid). Γ_GJ(0.3) itself is
bit-identical (−0.012032) — only the estimator-agreement metric moved. This is a
property of a wider window on a noisy tail, not new physics, and it is the second
reason the frozen guarded window stays the adjudicating one.

### AMD-2 — the G-B sign "hint" was a window artifact; struck

§6.2 previously recorded that the (unreliable, non-adjudicating) G-B matched-filter
points "turn positive for A ≥ 0.5 … a hint in the direction of the B-form's sign
structure". **That is withdrawn in full.** Re-extracting the same shipped G-B series
across the window-close sweep flips the sign:

| A | close 60 | close 64 | close 70 | close 78 | close 85 | close 95 |
|---|---|---|---|---|---|---|
| 0.0 | -0.00545 | -0.00545 | -0.00545 | -0.00545 | -0.00545 | -0.05831 |
| 0.1 | -0.00554 | -0.00554 | -0.00554 | -0.00554 | -0.00554 | -0.05832 |
| 0.2 | -0.00580 | -0.00580 | -0.00580 | -0.00580 | -0.00580 | -0.05835 |
| 0.3 | -0.00378 | -0.00378 | -0.00378 | -0.00378 | -0.00378 | -0.05839 |
| 0.4 | -0.00402 | +0.00455 | -0.00402 | -0.00402 | -0.00402 | -0.05846 |
| 0.5 | -0.00559 | +0.00671 | +0.00576 | +0.00576 | +0.00576 | -0.05856 |
| 0.6 | -0.00828 | +0.01016 | +0.00877 | +0.00877 | +0.00877 | -0.05868 |
| 0.7 | -0.01211 | +0.01507 | +0.01306 | +0.01306 | +0.01306 | -0.05882 |
| 0.8 | -0.01798 | +0.02153 | +0.01961 | +0.01961 | +0.01961 | -0.05899 |
| 0.85 | -0.02237 | +0.02691 | +0.02452 | +0.02452 | +0.02452 | -0.05908 |
| 0.9 | -0.02881 | +0.03479 | +0.03173 | +0.03173 | +0.03173 | -0.05911 |
| 0.925 | -0.03355 | +0.04059 | +0.03703 | +0.03703 | +0.03703 | -0.05908 |
| 0.95 | -0.04046 | +0.04903 | +0.04475 | +0.04475 | +0.04475 | -0.05894 |
| 0.9682 | -0.04852 | +0.05888 | +0.05378 | +0.05378 | +0.05378 | +0.05378 |
| 0.98 | -0.05721 | +0.06947 | +0.06353 | +0.06353 | +0.06353 | +0.06353 |
| 0.99 | -0.07119 | +0.09089 | +0.07923 | +0.07923 | +0.07923 | +0.07923 |

Read the columns honestly: **close 95 is past the 87.776-step contaminant front**, so
that column is wrap contaminant (note how it collapses onto ≈ −0.058 for every low-A
row — the contaminant, not the echo) and is not evidence about anything. The
load-bearing instability is entirely INSIDE the uncontaminated range: **close 60 gives
a negative Γ_GB at every A, close 64–85 gives a positive one from A = 0.5 up**, and at
A = 0.4 the sign flips twice within the sweep. The same perturbation leaves G-J
invariant to five decimals across 60–85:

| A | close 60 | close 64 | close 70 | close 78 | close 85 | close 95 |
|---|---|---|---|---|---|---|
| 0.5 | -0.03613 | -0.03613 | -0.03613 | -0.03613 | -0.03613 | -0.05448 |
| 0.9 | -0.20436 | -0.20436 | -0.20436 | -0.20436 | -0.20436 | -0.20436 |
| 0.99 | -0.45280 | -0.45280 | -0.45280 | -0.45280 | -0.45280 | -0.45280 |

(G-J's own low-A points do move at close 95 — the same contaminant signature, which is
how we know the 95 column is reading the wrap and not the slab.)

**The replacement statement:** the G-B echo is so far below the estimator pair's
reliability bound that its SIGN is selected by the choice of window. That is an
independent confirmation of the frozen INVALID-EXTRACTION verdict (16/16 discordant),
and it is all that may be said. Nothing in this run points toward, or away from, the
B-form's crossing/endpoint sign structure.

### AMD-3 — the per-run V3 sentinel check now exists, and was run

§3, §7 V3 and D3 asserted that the wrap-contaminant projection had been verified
per run from the saved sentinel series. **No shipped code did that.** The driver
derives the window close from the COLD run's sentinel only
(`engine_gamma_meanstest.py:529`, `sanity["cold"][key]`); the 48 graded runs' own
sentinel series were written to `raw_*.json` and never re-read. That is a
declared-not-computed gate, and the fix is a gate, not a sentence:
`research/drivers/engine_gamma_meanstest_check_sentinels.py` recomputes the D3
projection for every run from the shipped series, reports BOTH the strict bound
(arrival > close, the sentence in §3) and the guarded bound (arrival − 2σ_t ≥ close,
the rule the driver used to derive the close), reconciles its own earliest arrival
against the driver's recorded `t_wrap_probe`, and exits non-zero on any failure.
It takes the lattice constant `a_cell` from the engine rather than hard-coding it.

**Verbatim output (2026-08-24; the claim holds — 48/48 pass both bounds).** This
is the run from the LANDED layout; the run-workspace invocation differs only in
the three header lines that echo resolved paths, and the absolute prefix below is
just wherever the checkout sat when it ran:

```text
==============================================================================
PER-RUN V3 SENTINEL CHECK — 48 graded runs, shipped sentinel series
==============================================================================
  data           : /private/tmp/claude-501/-Users-grantlindblom-AVE-staging/91b867e5-bc0e-42d5-9d27-3ec2573c4b62/scratchpad/gammac-wt/research/drivers/data/engine_gamma_meanstest
  results        : /private/tmp/claude-501/-Users-grantlindblom-AVE-staging/91b867e5-bc0e-42d5-9d27-3ec2573c4b62/scratchpad/gammac-wt/research/drivers/engine_gamma_meanstest_results.json
  engine src     : /private/tmp/claude-501/-Users-grantlindblom-AVE-staging/91b867e5-bc0e-42d5-9d27-3ec2573c4b62/scratchpad/gammac-wt/src
  a_cell         : 2.828427124746  (engine value, build_srs_net)
  c_meas         : 0.580513073065 Cartesian length / step (CS-2 small-k)
  sigma_t        : 4.806281 steps; guard = 2.0*sigma_t = 9.612562
  threshold      : 0.01 of the unit launch envelope
  projection     : bwd 13.5 cells, fwd 10.5 cells (x_sent=19.5, x_p=6.0, box=24.0)

  cfg A        t_bwd t_fwd  arr_bwd  arr_fwd  earliest  close  margin  STRICT  GUARDED
  ------------------------------------------------------------------------------------
  GJ  0.0         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.1         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.2         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.3         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.4         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.5         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.6         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.7         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.8         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.85        22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.9         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GJ  0.925       22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GJ  0.95        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GJ  0.9682      22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GJ  0.98        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GJ  0.99        22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  GB  0.0         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.1         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.2         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.3         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.4         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.5         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.6         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.7         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.8         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.85        22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.9         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.925       22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.95        22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.9682      22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GB  0.98        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GB  0.99        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GT  0.0         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.1         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.2         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.3         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.4         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.5         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.6         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.7         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.8         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.85        22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.9         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.925       22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.95        22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.9682      22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  GT  0.98        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  GT  0.99        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS

  runs checked                     : 48
  earliest projected arrival (all) : 87.77589 steps
  frozen window close              : 78
  guarded bound (earliest - guard) : 78.16333
  STRICT  failures                 : 0
  GUARDED failures                 : 0
  driver t_wrap_probe (cold run)   : 87.77589369774
  |this check - driver|            : 0.000e+00 (RECONCILED)

  [amendment] extended close 85: STRICT PASS (margin +2.776 steps); GUARDED FAIL (needs 9.61 steps of guard, has 2.78) — the extended window is a convergence probe only, cross-validated against the L=32 rerun whose window is not wrap-bound; it is NOT the frozen extraction.

  VERDICT: PASS — no projected contaminant arrival precedes any window close in any of the 48 runs
```

Three things in that output are worth reading twice. (i) The earliest projected
arrival is **identical (87.776) in all 48 runs** — it comes from the backward
launch residual crossing the sentinel at t = 22, which is a property of the launch,
not of the grading, so the grading cannot make it earlier. (ii) The reconciliation
against the driver's own cold-run projection is **exactly 0.0e+00**, so this is a
re-derivation of the same quantity by an independent path, not a different
quantity that happens to pass. (iii) The guarded margin is thin — 78.16 vs the
close of 78, i.e. **0.16 steps** — so the frozen window sits essentially exactly on
its own timing budget. It passes, but there is no room to spend, which is the other
reason §AMD-1's extended close is a probe rather than a re-adjudication.

### AMD-4 — corrected narrative numbers

§3's slab-back close bounds read "93.1/92.8". Recomputed from the shipped values
(`t_back_return` = 112.48287 / 112.17592, σ_t = 4.806281, guard = 2σ_t):
close bound = t_back_return − 2σ_t − 2σ_t = **93.26 (G-J) / 92.95 (G-T)**. The
earlier pair was an arithmetic slip in a narrative sentence; both the old and the
new values are far above the binding wrap bound of 78.16, so no window, extraction,
classifier or verdict is affected. §3 now carries the corrected pair.

### AMD-5 — reproduction receipt for this repair

The repair added the amendment machinery to the driver and changed nothing in the
frozen path. Re-running the driver end-to-end (60 s wall, single-threaded numpy,
`np.random.seed(0)` set but no stochastic input anywhere):

- `raw_GJ.json`, `raw_GB.json`, `raw_GT.json`, `cold_sanity.json` — **byte-identical**
  (`cmp`) to the pre-repair run;
- the results JSON's frozen blocks — `params`, `sanity`, `windows`, `table`,
  `invalid_extraction`, `classifiers`, `verdicts` — **identical** under a
  key-sorted comparison; the only difference in the file is the ADDED
  `post_verify_amendment` block;
- the four §1 config-greps re-run on the amended driver still return **0 hits**
  each (one intermediate edit of mine introduced the word "drive" in a comment and
  turned that grep to 1; it was reworded rather than footnoted, and the grep
  re-run — a repaired file is not a verified file until the check is re-run);
- `engine_gamma_meanstest_check_sentinels.py` exits 0 in BOTH layouts (run workspace
  and landed `research/drivers/`), producing output identical line-for-line except
  the three header lines that echo the resolved paths — it is pure arithmetic on the
  shipped JSON;
- the figure is regenerated from the same run, now plotting the converged G-T
  series with the frozen-window G-T points retained as muted × markers.

## REPAIR — disposition of every adversarial-verify finding (2026-08-24)

Three lenses returned 11 findings (1 MAJOR, 10 MINOR). Every one is dispositioned
below: **FIXED** with the site of the fix, or **NO CHANGE** with the reason. No
finding is dropped, and no verdict was altered to accommodate one — the MAJOR
strengthens the verdict it touches, and the other ten are provenance/declaration
class.

| # | lens / severity | finding (short) | disposition |
|---|---|---|---|
| 1 | config / MINOR | Deviation register incomplete at the operationalization level: (a) matched-filter 25 % lag cutoff, (b) `dispersion_axis=0`, (c) `back_monitor_x=15.5`, (d) CS-2 gated on the k→0 extrapolation rather than the smallest-k reading | **FIXED** — new register entries **D7(a)**, **D9**, **D10**, **D8**; the CS-2 row of §2 now carries both readings with both rel-devs; the driver's own comments at :129 (D10), :148 (D9), :364 (D7) and :439 (D8) name their D-numbers |
| 2 | config / MINOR | The per-run sentinel verification claimed in §3/§7/D3 has no receipt in the workspace | **FIXED** — `engine_gamma_meanstest_check_sentinels.py` written and run; verbatim output in **§AMD-3**; D3's false receipt sentence corrected in place with a dated note; §7 V3 rewritten to say which code does what |
| 3 | config / MINOR | §7 V2 overstates the same-array SHA gate's standalone evidentiary weight | **FIXED** — §7 V2 rewritten to state exactly what the checksum can detect (in-place mutation of that one array) and cannot (dynamics reading S from a copy or elsewhere, or a leak that never writes back), and to name the three things that ARE load-bearing; the same wording is now a comment at the sha1 site (:870-877) so doc and code cannot drift; §1's row points at V2 instead of implying the SHA is the proof |
| 4 | physics / MINOR | Driver performs NO per-run V3 check; also the guard-adjusted slack is only 0.16 steps | **FIXED** — same fix as #2; the 0.16-step slack is computed by the check script, printed in its output, and called out explicitly in §AMD-3 as the reason the extended-window probe is not a re-adjudication |
| 5 | physics / MINOR | Unlogged estimator engineering choice: the ≥ 25 %-of-template-energy lag admissibility cutoff | **FIXED** — **D7(a)**, with the verdict-invariance evidence stated (G-B voided by discordance regardless of τ*; G-J/G-T lock τ* at the physical echo delay) |
| 6 | physics / MINOR | G-T reflected waveform truncated by the window close; 0.76 should be banked as a lower bound, not a measured ratio | **FIXED, and further** — rather than banking a bound, the converged locus is measured and adopted (**§AMD-1**): §4 flags every G-T magnitude as a lower bound, §5/§6.3/§8 carry the converged 0.772–0.814 range, and the figure plots the converged points |
| 7 | physics / MINOR | CS-2 operationalization drift (wrapper vs prereg-named function; polyfit-in-k² vs smallest-k; axis 0 vs engine default 2), unlogged | **FIXED** — **D8** (wrapper + both readings, both passing) and **D9** (axis); §2's CS-2 row rewritten |
| 8 | numerical / **MAJOR** | G-T extraction not converged w.r.t. window close / domain size; the 0.76 ± 0.01 suppression ratio is a window-truncation artifact; converged ratios are 0.765→0.814 and A-dependent | **FIXED** — **§AMD-1** carries the re-extraction at close 85 with four convergence receipts, the full converged table, the corrected A-dependent ratios (in-band 0.772→0.814), and the recomputation of the frozen suppression criterion on the converged numbers (still FALSE, a fortiori). §4 reading note, §5 classifier row, §6.3 quantitative amendment, §8 bottom line and the figure are all updated; the frozen §6 verdict text is preserved |
| 9 | numerical / MINOR | Per-run sentinel check declared but not implemented; and the back-path close bounds 93.1/92.8 recompute to 93.26/92.95 | **FIXED** — §AMD-3 (check) and **§AMD-4** (arithmetic); §3 now carries 93.26/92.95 with the recomputation shown |
| 10 | numerical / MINOR | The recorded G-B matched-filter sign 'hint' is itself a window artifact — the sign flips under window perturbation | **FIXED** — the hint is **struck entirely** from §6.2 and replaced by the artifact finding; **§AMD-2** carries the full 16 × 6 window-close sweep for G-B plus the G-J control |
| 11 | numerical / MINOR | `extract_gamma` adds two unlogged operationalizations: the 25 % lag cutoff AND a mask-restricted denominator | **FIXED** — **D7(a)** and **D7(b)**; the function docstring now names both and states the ≤ 4× inflation bound that the 0.25 floor caps, with the `tmpl_contained` check (True ×16) as the evidence that (b) is inert on the reported table |

### NO-CHANGE rationales (choices made against a lens's suggested remedy)

These are not skipped findings — each finding above is fixed. These are places
where the REMEDY differs from what a lens suggested, or where a lens's number is
not adopted verbatim:

1. **The per-run sentinel check was NOT added to the driver** (the numerical lens
   offered "added to the driver or its ad-hoc provenance stated"). It lives in a
   separate script instead, for two reasons: putting it in the driver would make
   the frozen path's output depend on post-verify code (the frozen results block is
   byte-stable precisely because nothing was inserted upstream of it), and a
   standalone checker re-runs in milliseconds off the shipped JSON instead of
   requiring a 60-second lattice run to re-verify a timing claim.

2. **L = 32 was NOT re-run in this repair.** The convergence claim rests on the
   L = 24 close-85 re-extraction plus four receipts (template containment, tail
   energy, close-85-vs-95 stationarity, G-J invariance). The L = 32 numbers quoted
   in §AMD-1 receipt 3 are **the numerical verify lens's, not reproduced here**, and
   are labelled as such: they are corroboration (max |Δ| = 3e-5 against the values
   this document computes), not the basis of the correction. Re-running L = 32 here
   would be a 262 144-node repeat of a cross-check whose conclusion the in-house
   receipts already carry.

3. **The smallest-k CS-2 rel-dev is reported as 0.627 %, not the lens's 0.633 %.**
   Same quantity, different rounding order: 0.633 % is what the 4-dp-rounded 0.5810
   gives (0.6322 %); the shipped full-precision c(k₁) = 0.5809720966 against
   1/√3 gives 0.6273 %. Both are far inside the 2 % gate, so nothing turns on it,
   but the document quotes the number it computed and says where the other comes
   from rather than silently adopting either. Recomputed in the results JSON
   (`post_verify_amendment.cs2_readings`).

4. **The frozen-window G-T table in §4 was NOT overwritten** with the converged
   values. The frozen record is what the frozen rules were applied to; the
   converged table is §AMD-1's, and §4 carries a reading note pointing there. Same
   discipline for §6.3: the verdict paragraph stands as written, with the
   quantitative correction in an adjacent dated block. Only §8 (the bottom line,
   which is a summary and not a frozen artifact) was rewritten outright.

### Found during the repair, beyond the verify findings

- **G-J's A = 0.3 point crosses the discordance bound at the extended close**
  (0.197 → 0.206) purely because a wider window feeds more tail into the unsigned
  energy estimator; Γ_GJ(0.3) is bit-identical. Recorded in §AMD-1 as a wrinkle of
  the probe, and as a second reason the guarded window remains the adjudicating one.
- **The G-B sign flips at close 60 vs 64**, i.e. inside the uncontaminated range —
  the artifact is not confined to the contaminated close-95 column, which makes the
  "window-selected sign" statement stronger than the lens's version. Conversely the
  close-95 column is contaminant for G-J too, so it is not read as evidence in
  either direction (§AMD-2).
- **§1's grep table had unescaped `|` inside its code spans**, which breaks the
  markdown table; escaped while rewriting the row line numbers.
- **The FROZEN prereg trips one warn-level markdown-link false positive** and is
  deliberately left alone: `verify-md-links` reads the launch formula's
  `V_inc[u,p](t=0)` (prereg line 174) as a markdown link `[u,p](t=0)` and reports
  `[broken intra · warn] -> t=0`. It is a warn, not a gate; fixing it would mean
  editing a frozen document, which is not done. Flagged here so the next reader
  does not 'fix' it.
- **Every driver `file:line` citation in this document was re-derived** after the
  repair edits shifted line numbers, and the landed filenames substituted for the
  run-workspace ones.
