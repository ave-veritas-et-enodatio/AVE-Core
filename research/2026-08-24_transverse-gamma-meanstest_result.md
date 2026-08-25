# RESULT — Reciprocal-loading pulse reflection Γ(A) on the 2-component transverse vector-TLM carrier (static-existence Stage 1 / epic P1)

Prereg-file: research/2026-08-24_transverse-gamma-meanstest_prereg_FROZEN.md

**Pair of** the prereg named above (NOT edited — every departure is a dated
DEVIATION entry in §D below). **Prereg frozen at commit `81e94565`; the driver was
committed at `089cce23` BEFORE the run of record, so the executed driver is the
committed driver.**
**Run date:** 2026-08-24 (run of record at the frozen L=24 parameters).
**Driver:** `research/drivers/transverse_gamma_meanstest.py` (consumes the NEW
module `src/ave/solvers/transverse_graded_scatter.py`, whose 25 VOID-linked pytest
gates were green before the run: `src/tests/test_transverse_graded_scatter.py`).
**Per-run V3 check:** `research/drivers/transverse_gamma_meanstest_check_sentinels.py`
(frozen-in from the start per prereg §4.4; full output in §9).
**Raw data:** `research/drivers/data/transverse_gamma_meanstest/raw_{TMAG,TELEC}.json`
(full F/B/back-monitor/sentinel/C1-leak series per grid point) +
`cold_sanity.json` + `run_log.txt`;
`research/drivers/transverse_gamma_meanstest_results.json`.
**Figure:** `research/figures/2026-08-24-transverse-gamma-meanstest/fig1_gamma_overlay.{png,pdf}`
(white house style via `ave.viz.style.apply`, Okabe-Ito, no title, legend outside
the data; the four frozen §2.2 forms drawn, measured points overlaid).

## Scope block (prereg §1/§2.3/§2.4, restated verbatim as binding)

The following conclusion-shapes are FORBIDDEN in this document regardless of what
the run shows: "therefore a bound state / electron can (or cannot) form";
"therefore the energize-LOCK negative is explained away / reopened"; "therefore an
eigenmode exists / does not exist"; any charge-sector, winding, spin, or chirality
statement; any adjudication of WHICH branch "the electron uses" (#260 untouched);
any adjudication of the sector-ownership question (§2.3's flagged split); any claim
that a measured locus is TRANSVERSE-DISTINCT vs the scalar channel; any claim that
the transverse VERTEX behavior is now verified. The prereg §1's operative flag on
the `master-equation.md:106` banner also binds here: the banner's parenthetical
"($Z=Z_0\sqrt{S}$, $|\Gamma|=1$ both ways)" is in tension with the two reciprocal
Z conventions pinned at `universal_operators.py:788-800` (the fork is degenerate
in |Γ|, not in Z) — **this document inherits NEITHER reading**: every Z/Γ
statement here is the declared maps' own.

**The §2.3 flagged canon split (restated, NOT adjudicated here):** the
Grant-ratified INVARIANT-S2 sector split assigns the Z→0 short to the
longitudinal-A1 bond compliance and the Z→∞ open to the transverse-T2 permittivity
(`resonant-lc-solitons.md:41`; `saturation-rim-inversion.md:65-68`), while the
master-equation in-channel branch fork (`:105`/`:107` under the `:106`
sign-selector banner) holds both boundary phases on the wave channel. This run
measured DECLARED IMPEDANCE MAPS; no result sentence assigns the Γ→−1 locus to a
sector.

**The §2.4 replay identity (restated):** with optical activity OFF, a
component-scalar loading, and a component-0 launch, T-MAG's component-0 dynamics
are mathematically the merged Class-C G-J scalar run. T-MAG is a REPRODUCTION
gate (machinery receipt), never an independent transverse measurement and never an
independent confirmation of the scalar locus. All new physics content is T-ELEC
(z = 1/√S — never measured on any channel before this run) plus the cross-loading
MIRROR diagnostic.

## 1 — Config echo + config-grep rerun (prereg §3, on the ACTUAL driver)

Run configuration actually executed (from `run_log.txt`; every parameter printed,
no silent defaults): `build_srs_net(L=24, enantiomorph="right")` → N = 110 592
nodes, degree 3, carrier `srs-z3`, 165 888 bonds; geometry in cells: x_s=2, x_p=6,
x_I=9, x_B=15, W=6, back monitor 15.5, sentinel 19.5 @ 1 %, wrap margin 11;
launch = baseband Gaussian σ_x=1.5 cells, +x̂ directional weighting
max(0, −x̂·b̂), component-0 polarized, peak 0.7047; A-grid = the 16 frozen
literals; 32 graded runs of T=170 steps (hard cap 6000 not approached); probe
bonds 1152, back-monitor bonds 1152, sentinel bonds 1152.

Config-grep rerun (word-bounded, counts reported; run on the COMMITTED driver,
checker, and module):

| §3 config key | pattern | driver | checker | module |
|---|---|---|---|---|
| drive / pump for t>0 | `\b(pump\|drive\|driven\|inject\|source_term)\b` | **0** | **0** | **0** |
| tunable dt / integrator limit | `\b(dt\|dt0\|timestep)\b` | **0** | **0** | **0** |
| eigensolve | `\beig[a-z]*\(\|linalg\.(eig\|eigh\|eigsh)` | **0** | **0** | **0** |
| second carrier / winding observables (#417) | `omega_b\|omega_s\|winding\|poloidal\|toroidal` | **0** | **0** | **1** — the module docstring's own fence sentence (`transverse_graded_scatter.py:49`: "no winding, charge, or spin content"), i.e. the declaration of absence, not machinery |

Structural read of the step (`vector_graded_step`,
`src/ave/solvers/transverse_graded_scatter.py`): no A-update, no V-dependence of
the coefficients — scatter coefficients are precomputed constants from the frozen
A(x). The §3 structural proof holds on the run as executed: genesis requires
(precursor ∧ pump ∧ self-consistency); this config has none of the three
conjuncts. The two polarization components are not #417's two coupled carriers:
no inter-component coupling exists (CS-6a/V5 receipts below), and no winding
observable is constructed. No closed negative (§3.1 energize-LOCK, §3.2 #415,
§3.3 #417) is reconstructed.

## 2 — Pre-graded gates (prereg §5) — **PASS (all)**

| gate | measured | frozen criterion | verdict |
|---|---|---|---|
| CS-1 vector conservation (uniform, actual launch, 200 steps) | max rel drift **1.729e-14** | < 1e-10 | **PASS** |
| CS-2 network factor | polyfit **0.580513** (rel dev 0.548 %); smallest-k **0.580972** (rel dev 0.627 %) vs 1/√3 | < 2 % each | **PASS** — byte-identical to the Class-C §2 values, as the replay identity predicts |
| CS-2 band edge | k_edge = 0.3702 (**bound-from-below: ALL sampled k within 5 % of c₀**, the declared convention); pulse fraction below edge 0.97368 analytic / 0.95880 discrete | ≥ 0.95 (smaller reading) | **PASS** |
| CS-3 time-of-flight | v = 0.56948 vs c₀ = 0.58051; rel dev **1.901 %**; t_cF = 19.87, σ_t = 4.81 | < 5 % | **PASS** |
| CS-4 all-cold vector-vs-scalar regression (200 steps) | max abs dev **1.443e-15**, component 1 exactly 0.0 | ≤ 1e-12 | **PASS** |
| CS-6a decoupling | max component-1 over 200 cold steps = **0.0 exactly** | ≤ 1e-14 | **PASS** |
| CS-6b SO(2) equivariance @ A=0.9 | TMAG **7.105e-15**; TELEC **7.105e-15** | ≤ 1e-12 each | **PASS** (both loading maps, per the re-audited freeze) |
| CS-7 load-map reconcile vs `universal_dynamic_impedance` | \|ΔY\| = **0.0 exactly** at A ∈ {0.5, 0.9}, both configs | ≤ 1e-12 | **PASS** (the sign-lock raise is in the path; the swap demonstration is the module pytest `test_cs7_swap_fails_both_directions`) |
| CT-1 implementation identity | dev_diag 5.6e-17, dev_off 0.0, vs bedrock 0.0 | ≤ 1e-15 | **PASS** — an implementation receipt ONLY (prereg §2.6); the transverse-vertex item remains OPEN |
| T1(a) uniform collapse @ A=0.9 | max\|Δ\| = 1.11e-16 (both loads) | ≤ 1e-13 | **PASS** |
| T1(b) boundary-set identity @ A=0.9 | deviating set == mixed-admittance set, **2304/2304** nodes, max dev 0.170 (TMAG) / 0.195 (TELEC) | sets equal ∧ non-empty ∧ ≥ 1e-3 | **PASS** |
| Module pytest gates | 25/25 green pre-run (`test_transverse_graded_scatter.py`) | all green | **PASS** |

## 3 — Windows + R-1 (prereg §4.4/§5)

Both configs derived identically from the shared cold run + the pinned Class-C
rule: **incident [10, 29], reflected [30, 78]**; wrap-projected probe arrival
87.776 steps (binding close: 87.776 − 2σ_t = 78.16 → 78); slab-back return bound
112.48 (TMAG) / 112.67 (TELEC) — non-binding; back-monitor measurability: **0
runs dropped** in either config (every graded run's transmitted transit was
measurable, D1). Windows constructible with positive width (V3), reflected opens
at incident close + 1 (V4 assert held).

**R-1 (T-MAG only): PASS** — derived [10, 29]/[30, 78] equal the banked Class-C
G-J windows exactly. T-ELEC's derived windows (reported per the prereg's R-1
clause) are identical, so close_f = 78 for both and no E11 set adjustment was
needed.

## 4 — Measured Γ(A) (32-point record; both estimators; frozen flags)

Signed convention (frozen §4.4): Γ < 0 = polarity-inverted echo (short-like,
−1 rim); Γ > 0 = same-polarity echo (open-like, +1 rim), matching Γ = (z−1)/(z+1).

**CS-5 (adjudicated after data collection per the frozen D5-adopted ordering,
before any graded datum was interpreted): PASS** — |Γ(A=0)| = **0.00545** for
BOTH configs through the full extraction pipeline (frozen criterion < 0.02).
Derived adjudication constants: ε₀ = **0.00545**; θ = max(3ε₀, 0.05) =
**0.05000**; δ = max(ε₀, 0.01) = **0.01000**. "TRUNC-SUSPECT" = the S2 point
label for a VALID point whose tail fraction exceeds 0.02; the label does not
invalidate the point.

### T-MAG (load="magnetic", z = √S — the reproduction config)

| A | Γ_meas | \|Γ\|_E | τ* | discordance | tail frac | flags |
|---|---|---|---|---|---|---|
| 0.0 | −0.00545 | 0.01831 | 8 | 0.257 | 0.060 | UNRELIABLE |
| 0.1 | −0.00556 | 0.01835 | 8 | 0.256 | 0.060 | UNRELIABLE |
| 0.2 | −0.00536 | 0.01904 | 30 | 0.274 | 0.054 | UNRELIABLE |
| 0.3 | −0.01203 | 0.02190 | 30 | 0.197 | 0.040 | valid; TRUNC-SUSPECT |
| 0.4 | −0.02201 | 0.02877 | 30 | 0.135 | 0.022 | valid; TRUNC-SUSPECT |
| 0.5 | −0.03613 | 0.04089 | 30 | 0.095 | 0.010 | valid |
| 0.6 | −0.05586 | 0.05955 | 30 | 0.062 | 0.004 | valid |
| 0.7 | −0.08402 | 0.08730 | 30 | 0.037 | 0.002 | valid |
| 0.8 | −0.12695 | 0.13038 | 30 | 0.026 | 0.001 | valid |
| 0.85 | −0.15872 | 0.16249 | 30 | 0.023 | 0.000 | valid |
| 0.9 | −0.20436 | 0.20876 | 30 | 0.021 | 0.000 | valid |
| 0.925 | −0.23690 | 0.24181 | 30 | 0.020 | 0.000 | valid |
| 0.95 | −0.28248 | 0.28816 | 30 | 0.020 | 0.000 | valid |
| 0.9682 | −0.33243 | 0.33899 | 30 | 0.019 | 0.000 | valid |
| 0.98 | −0.38211 | 0.38957 | 30 | 0.019 | 0.000 | valid |
| 0.99 | −0.45280 | 0.46149 | 31 | 0.019 | 0.000 | valid |

Informative-unreliable tally: **0** (> 4 would be INVALID-EXTRACTION) — the three
UNRELIABLE points are all sub-θ near-null points, excluded from the tally by the
frozen E12 informative-point rule and reported here.

### T-ELEC (load="electric", z = 1/√S — the new measurement)

| A | Γ_meas | \|Γ\|_E | τ* | discordance | tail frac | flags |
|---|---|---|---|---|---|---|
| 0.0 | −0.00545 | 0.01831 | 8 | 0.257 | 0.060 | UNRELIABLE |
| 0.1 | −0.00534 | 0.01835 | 8 | 0.260 | 0.060 | UNRELIABLE |
| 0.2 | +0.00536 | 0.01901 | 32 | 0.273 | 0.057 | UNRELIABLE |
| 0.3 | +0.01192 | 0.02185 | 32 | 0.199 | 0.045 | valid; TRUNC-SUSPECT |
| 0.4 | +0.02177 | 0.02869 | 31 | 0.138 | 0.028 | valid; TRUNC-SUSPECT |
| 0.5 | +0.03588 | 0.04080 | 31 | 0.098 | 0.015 | valid |
| 0.6 | +0.05561 | 0.05945 | 31 | 0.065 | 0.008 | valid |
| 0.7 | +0.08376 | 0.08720 | 31 | 0.039 | 0.004 | valid |
| 0.8 | +0.12667 | 0.13028 | 31 | 0.028 | 0.002 | valid |
| 0.85 | +0.15844 | 0.16240 | 31 | 0.024 | 0.002 | valid |
| 0.9 | +0.20406 | 0.20868 | 31 | 0.022 | 0.001 | valid |
| 0.925 | +0.23659 | 0.24174 | 31 | 0.021 | 0.001 | valid |
| 0.95 | +0.28219 | 0.28809 | 30 | 0.020 | 0.001 | valid |
| 0.9682 | +0.33224 | 0.33894 | 30 | 0.020 | 0.001 | valid |
| 0.98 | +0.38202 | 0.38953 | 30 | 0.019 | 0.001 | valid |
| 0.99 | +0.45281 | 0.46147 | 30 | 0.019 | 0.001 | valid |

Informative-unreliable tally: **0** → not INVALID-EXTRACTION.

## 5 — Classifiers (prereg §6.2, computed on valid points)

| classifier | T-MAG | T-ELEC |
|---|---|---|
| n_valid | 13 | 13 |
| SIGN_top (highest valid point with \|Γ\| > θ) | **−** (at A = 0.99) | **+** (at A = 0.99) |
| θ-CROSSING | none | none |
| MONOTONE (±δ) | yes, **decreasing** | yes, **increasing** |
| δ-level sign profile | all 13 points (A = 0.3 … 0.99) **negative** | all 13 points (A = 0.3 … 0.99) **positive** |
| FLOOR (fit over 0 < A ≤ 0.5, 3 valid pts) | intercept +0.0248, \|·\| < θ ⇒ **no floor** | intercept −0.0247, \|·\| < θ ⇒ **no floor** |
| SHAPE (T-ELEC only) | — | **ELEC-CORE-like** (no crossing ∧ monotone increasing) |

**MIRROR (recorded, non-adjudicating):** over the 10 co-valid informative points
(A = 0.6 … 0.99): **max 0.00451 (0.451 %, at A = 0.6), median 0.00139**, and the
defect DECREASES monotonically with A (0.00451 → 0.00001 at A = 0.99). The two
loadings draw near-exact mirror loci. The defect's low-A concentration is
CONSISTENT WITH the shared-vertex-intercept mechanism the prereg names (§2.2) but
is NOT discriminated by this run — MIRROR is a §6.5 non-adjudicator and this
sentence carries no mechanism claim.

## 6 — Reproduction gates + frozen verdicts (§5 R-1..R-3, §6.3/§6.4)

- **R-1 PASS** (§3). **R-2 PASS:** max over the 16 grid points of
  \|Γ_TMAG(A) − Γ_GJ,banked(A)\| = **1.665e-16** (gate < 1e-6) — machine-epsilon
  agreement with the banked scalar record; the §2.4 replay identity is confirmed
  numerically, not just structurally. **R-3 PASS:** SIGN_top/crossings/monotone
  direction all concordant with the banked classifiers; window-stable;
  **zero per-point valid-flag differences** vs the banked run (the foreseen
  A = 0.3 knife-edge flip did not occur — discordance 0.197 reproduced exactly).
- **VERDICT T-MAG (§6.3): REPRODUCED** — a MACHINERY receipt: the new
  2-component graded scatter reproduces the banked Class-C G-J measurement to
  machine epsilon (max |ΔΓ| = 1.7e-16) at the frozen windows. Not an
  independent measurement, not an independent confirmation (§2.4 restated in
  the scope block).
- **VERDICT T-ELEC (§6.3): DRAWS-OPEN** — SIGN_top = + ∧ no +→− crossing ∧
  0 θ-crossings. SHAPE = ELEC-CORE-like: the ε-loading homogenizes to the
  two-port mirror locus (1−√S)/(1+√S), exactly as the scalar precedent
  homogenized the μ-side; the ELEC-VERTEX (Form-B-algebra) candidate was NOT
  drawn — no crossing anywhere, and the δ-level sign profile shows no negative
  region at any A ≥ 0.3, so no vertex-counting signature survives even at the
  δ level. The A\*-probe grid points (0.95–0.99) bracket no sign change.
- **§6.4 pair verdict (frozen table, row 1): the two reciprocal impedance
  loadings draw OPPOSITE boundary phases at response-map level** — the ε-side
  locus measured for the first time on any channel (monotone positive to
  Γ(0.99) = +0.4528, toward the OPEN rim), the μ-side the banked deepening
  negative locus reproduced in the 2-component container. Scoped per §2.5 to
  boundary-phase (impedance-sign) content; NO sector-ownership claim (§2.3's
  flagged INVARIANT-S2-vs-master-equation split stands, un-adjudicated); NO
  transverse-distinctness claim (§2.4); #260 untouched.

## 7 — Window-convergence receipts (§4.4/E11)

- **Close sweep {60, 64, 70, 74, 78} (the E11 Γ-delta record, tabulated):**
  30 of 32 grid points are close-invariant to ROUNDOFF (max spread ≤ 1.2e-16;
  the largest roundoff-level spread is 1.11e-16, at A = 0.9 in each config)
  across the entire sweep. The two exceptions are the T-ELEC low-A weak-signal
  points (A = 0.2, an UNRELIABLE point; A = 0.3, a valid TRUNC-SUSPECT point),
  whose entire spread sits between the close-60 early-truncation PROBE and the
  {64, 70, 74, 78} set: **T-ELEC A = 0.2, spread 2.61e-5; T-ELEC A = 0.3,
  spread 1.26e-4** — both ≪ δ = 0.01, and **Γ(78) − Γ(70) = 0.0 exactly at all
  32 points** (the corrected form of this draft's original blanket
  "five-decimal invariant everywhere" sentence, which the adversarial verify
  falsified at those two points; §REPAIR).

  | config | points with spread ≤ 1.2e-16 (roundoff) | points with spread above roundoff (spread; where) | max \|Γ(78)−Γ(70)\| |
  |---|---|---|---|
  | T-MAG | 16/16 | none | 0.0 exactly |
  | T-ELEC | 14/16 | A=0.2 (2.61e-5; close 60 vs rest), A=0.3 (1.26e-4; close 60 vs rest) | 0.0 exactly |

  The loci at the verdict-relevant closes {70, 74, 78} are exactly invariant —
  fully converged, the same invariance the banked G-J showed.
- **Stability rules:** S1 not fired (SIGN_top and crossing count identical at
  closes 70/74/78, both configs); WINDOW-SENSITIVE points: none (max sweep
  delta ≪ δ); TRUNCATION-SUSPECT points: {0.3, 0.4} in each config (tail
  fractions 0.040/0.022 TMAG, 0.045/0.028 TELEC — weak-signal low-A points
  where the reflected trace has not fully rung down), count 2 < 3 and median
  delta fraction 0.0000 ⇒ **S3 not fired**; no convergence probe owed.
  `tmpl_contained` held at the locked τ* for every reported point (no
  TMPL-CLIPPED flags at the frozen windows).

## 8 — VOID checks (prereg §8)

| condition | status |
|---|---|
| V1 gate fail | **not triggered** — every §5 gate PASS: the pre-graded set (§2 table), CS-5 (§4 preamble: \|Γ(0)\| = 0.00545 both configs < 0.02), R-1 (§3), R-2/R-3 (§6); module pytest 25/25 green at the run-of-record commit `089cce23` |
| V2 grading leaks into dynamics | **not triggered** — E_Y relative drift ≤ **1.484e-14** over all 32 runs (gate 1e-8); SHA re-verified in 32/32 runs (scope as quoted in the prereg §4.2 — over-determined by the drift bound, CS-4 = 1.443e-15, and the structural step read); CS-4 PASS |
| V3 wrap/contamination | **not triggered** — 32/32 STRICT PASS and 32/32 GUARDED PASS per the standalone checker (§9); earliest projected arrival 87.77589 > close 78 in every run; reconcile **0.0 exactly** against the driver's cold projection (both configs) |
| V4 window sanity | **not triggered** — assert held ([30] = [29]+1, width 48 > 0) |
| V5 polarization leak | **not triggered** — max_t C1_leak = **0.0 exactly** in all 32 measurement runs (gate 1e-12): the step is exactly S_u ⊗ I₂ + permutation ⊗ I₂ |
| per-config INVALID-EXTRACTION | **not triggered** — informative-unreliable tallies 0/0 |

## 9 — Per-run V3 sentinel-checker appendix (REQUIRED; full output)

`transverse_gamma_meanstest_check_sentinels.py` (committed pre-run, `089cce23`),
run on the shipped raw series; exit code 0. FULL output, verbatim (the binding
contaminant is the grading-independent backward-launch residual — identical in
every run, both loadings, as in the banked scalar run; the only per-run
variation is in the non-binding forward-arrival columns):

```
==============================================================================
PER-RUN V3 SENTINEL CHECK — 32 graded runs, shipped sentinel series
==============================================================================
  data      : /Users/grantlindblom/AVE-staging/AVE-Core-worktrees/static-existence-s1/research/drivers/data/transverse_gamma_meanstest
  results   : /Users/grantlindblom/AVE-staging/AVE-Core-worktrees/static-existence-s1/research/drivers/transverse_gamma_meanstest_results.json
  a_cell    : 2.828427124746 (engine value, build_srs_net)
  c_meas    : 0.580513073065; sigma_t = 4.806281; guard = 9.612562
  threshold : 0.01; projection bwd 13.5 / fwd 10.5 cells

  cfg   A        t_bwd t_fwd  arr_bwd  arr_fwd  earliest  close  margin  STRICT  GUARDED
  --------------------------------------------------------------------------------------
  TMAG  0.0         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.1         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.2         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.3         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.4         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.5         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.6         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.7         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.8         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.85        22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.9         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TMAG  0.925       22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  TMAG  0.95        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  TMAG  0.9682      22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  TMAG  0.98        22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  TMAG  0.99        22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.0         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.1         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.2         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.3         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.4         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.5         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.6         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.7         22    65   87.776  116.159    87.776     78   9.776    PASS     PASS
  TELEC 0.8         22    66   87.776  117.159    87.776     78   9.776    PASS     PASS
  TELEC 0.85        22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.9         22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.925       22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.95        22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.9682      22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.98        22    67   87.776  118.159    87.776     78   9.776    PASS     PASS
  TELEC 0.99        22    67   87.776  118.159    87.776     78   9.776    PASS     PASS

  runs checked                     : 32
  earliest projected arrival (all) : 87.77589 steps
  guarded bound (earliest - guard) : 78.16333
  STRICT failures                  : 0
  GUARDED failures                 : 0
  driver t_wrap_probe [TMAG]        : 87.77589369774  |check - driver| = 0.000e+00 (RECONCILED)
  driver t_wrap_probe [TELEC]        : 87.77589369774  |check - driver| = 0.000e+00 (RECONCILED)

  VERDICT: PASS — no projected contaminant arrival precedes any window close in any of the 32 runs, and the reconcile holds
```

## D — DEVIATIONS (dated; the prereg file is untouched)

- **D1 (2026-08-24) — back-monitor measurability threshold.** The prereg §4.4
  declares the branch-(a) fallback ("if a config has no measurable back-monitor
  transit, branch (a) is dropped") without a numeric threshold. The driver
  operationalizes "measurable" as per-run max\|Fb\| ≥ 0.01 × launch peak
  (`bm_measurable_frac`, printed in the parameter block). In the event the
  threshold never fired: 0 runs dropped in either config, and branch (a) was
  non-binding by **15.26 (T-MAG) / 15.45 (T-ELEC) steps** against the integer
  close 78 (close bounds 93.26 / 93.45 under the frozen two-subtraction rule — this entry's first draft said
  "~34 steps", the raw back-return-minus-close difference without the two 2σ_t
  subtractions; corrected per the adversarial verify, §REPAIR).
  ENGINEERING-CHOICE, declared in the driver, inert in this run.

No other deviation in the RUN: the frozen geometry, grid, estimator, gate
ordering (pre-graded set → data collection → windows/R-1 → CS-5 →
interpretation), and threshold set were executed as written. Two REPORTING
omissions in this document's first draft — the checker's full-output appendix
(prereg §9.3) and the E11 Γ-delta tabulation (prereg §4.4) — were caught by the
post-draft adversarial verify and repaired in place before presentation
(§REPAIR); the shipped data was complete throughout.

## Bottom line

The Stage-1 deliverable held on both axes:

1. **Machinery (the named extension): validated end-to-end.** The transverse
   per-directed-bond graded scatter reproduces the banked Class-C G-J
   measurement to machine epsilon (R-2 max 1.7e-16) with the identical windows
   (R-1) and concordant classifiers (R-3), passes every structure gate
   (cancellation both ways, SO(2) equivariance under both loadings, component
   decoupling measured at 0.0 in double precision, load-map reconcile against
   the sign-locked reference, E_Y conservation at roundoff — drift ≤ 1.5e-14),
   and the orthogonal-polarization leak sentinel read 0.0 (double precision) in
   all 32 runs.
2. **Physics (the new measurement): the ε-side impedance loading z = 1/√S —
   never measured on any channel before — DRAWS the OPEN boundary phase:** a
   monotone, crossing-free, floorless, window-converged POSITIVE locus rising
   to Γ(0.99) = +0.4528, shape ELEC-CORE-like (the two-port mirror form; the
   vertex-counting candidate did not survive homogenization, at either the θ
   or the δ level). The pair verdict is the frozen §6.4 row-1 language,
   verbatim: **"The two reciprocal impedance loadings draw opposite boundary
   phases at response-map level — the ε-side (z = 1/√S) locus measured for the
   first time on any channel, the μ-side the banked scalar locus reproduced in
   the 2-component container. Scoped per §2.5 to boundary-phase content; NO
   sector-ownership claim (§2.3's flagged split stands); NO
   transverse-distinctness claim (§2.4); #260 untouched. SHAPE and MIRROR
   reported as diagnostics."** The MIRROR diagnostic (max 0.451 %, median
   0.14 %, §5) is reported per that row as a diagnostic — it is a §6.5
   non-adjudicator and carries no evidentiary weight in the verdict. The
   sector-ownership question (§2.3) and the transverse-vertex item (§2.6)
   remain OPEN, exactly as frozen.

No VOID condition fired; no closed negative's config was reconstructed (§1).
The ≥3-lens adversarial verify ran on this document's first committed draft per
prereg §9.6; every finding's disposition is logged in §REPAIR below, and the
repaired text above is the record of record. Verdict language is
frozen-criterion-only throughout.

## REPAIR — disposition of every adversarial-verify finding (2026-08-24)

Three lenses (config-compliance re-grep / physics-coordinates-sector /
independent numerics rerun; 16 findings, each adversarially verified —
dispositions grouped below, several items absorbing convergent multi-lens
variants). All real findings were
repaired in this document; NO verdict, classifier value, gate outcome, or
shipped number changed — every repair is reporting-layer.

1. **Missing REQUIRED appendices + §D denial (MAJOR, CONFIRMED).** The checker's
   FULL 32-row output (prereg §9.3) and the E11 Γ-delta tabulation (prereg
   §4.4) were absent from the first draft while §D said "no other deviation."
   FIXED: full checker output pasted into §9; the sweep-spread table added to
   §7; §D's closing paragraph corrected.
2. **§7 blanket five-decimal-invariance claim false at 2/32 points (CONFIRMED,
   found independently by all three lenses).** T-ELEC A = 0.2 (spread 2.61e-5)
   and A = 0.3 (1.26e-4) vary between the close-60 early-truncation probe and
   the rest — the falsifying points sat exactly in the omitted table. FIXED:
   §7 rewritten with the exact spreads; the verdict-relevant {70, 74, 78}
   invariance (Γ(78)−Γ(70) = 0.0 at all 32 points) stated separately. No
   verdict touched (spreads ≪ δ; closes 60/64 are non-verdict probes).
3. **Bottom-line verdict overreach (MAJOR, CONFIRMED).** The first draft's pair
   sentence paraphrased the frozen §6.4 row-1 language ("the reciprocal-pair
   structure canon states for the branch carve is drawn by the lattice") and
   leaned on MIRROR — a §6.5 non-adjudicator — as an evidentiary premise.
   FIXED: the frozen row-1 language now quoted verbatim; MIRROR demoted to a
   reported diagnostic.
4. **"bit-for-bit" overstated R-2 (CONFIRMED).** Machine-epsilon agreement
   (1.7e-16), not bit-identity. FIXED in §6 and the Bottom line.
5. **D1's "~34 steps" margin wrong (CONFIRMED).** The raw difference, not the
   frozen two-subtraction bound. FIXED: 15.3 steps (93.26/93.45 vs 78), with
   the original error preserved in the entry.
6. **CS-5 outcome never stated against its criterion (CONFIRMED/DOWNGRADED
   variants; one variant REFUTED).** FIXED: explicit CS-5 PASS line in §4's
   preamble; §8 V1 row enumerates where each §5 gate is reported.
7. **"exact E_Y conservation" / "leaked exactly zero" (CONFIRMED/DOWNGRADED).**
   FIXED: stated as measured numbers (drift ≤ 1.5e-14; leak 0.0 in double
   precision).
8. **MIRROR "at most 0.45 %" vs shipped 0.451 % (DOWNGRADED).** FIXED: 0.451 %.
9. **MIRROR mechanism note asserted to "stand" (DOWNGRADED).** FIXED: reworded
   to consistent-with, explicitly not discriminated by this run.
10. **Scope block dropped the prereg §1 banner-tension bullet (DOWNGRADED).**
    FIXED: the operative instruction (inherit neither Z-reading of the
    `master-equation.md:106` parenthetical) restored to the scope block.

REFUTED (no change): the claim that §4's CS-5 pointer was a dead
cross-reference (the §4 preamble carries the values; the repair in item 6 was
made for the CONFIRMED variant's reason, not this one's).

**Second-round re-audit (repairs-need-reaudit, 2026-08-24).** A focused
re-audit of the 10 repair sites confirmed the repairs against the shipped data
and caught TWO new false statements the repair round itself introduced — both
in §7's rewritten paragraph, the same defect shape as the finding it repaired
(a hand-typed bound falsified by the paragraph's own table): (i) "spread ≤
1.1e-16" excluded two points at exactly 1.110e-16 (threshold corrected to
1.2e-16, counts unchanged); (ii) T-ELEC A = 0.2 was mislabeled TRUNC-SUSPECT
(it is UNRELIABLE; label corrected, and the §4 TRUNC-SUSPECT definition's
valid-point restrictor restored). Also fixed: the D1 margin split per config
(15.26/15.45), the §REPAIR tally de-classed, and the Bottom-line quote's
sentence-initial capitalization restored to match the frozen cell exactly.
All other sites PASSED, including a byte-identical diff of the §9 appendix
against a fresh checker run and independent recomputation of every load-bearing
number.
