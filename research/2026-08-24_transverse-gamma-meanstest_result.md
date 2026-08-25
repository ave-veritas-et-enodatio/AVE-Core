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

> **Round-2 repair note (2026-08-25) — the clause the flag omitted, restored
> verbatim.** The prereg §2.3 (and the canonical restatement at
> `saturation-rim-inversion.md:66`, which ends its quote at *"Orthogonal
> reactances, both `|Γ|=1`, differing only in boundary phase."*) quotes
> `resonant-lc-solitons.md:41` only
> through *"differing only in boundary phase"*, cutting at the em dash. Canon's
> own sentence continues, verbatim
> (`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:41`):
> *"Orthogonal reactances, both $|\Gamma|=1$, differing only in boundary phase —
> so this leaf's electric-sector $Z\to0$ confinement and the master-equation
> magnetic-branch confinement are distinct-sector statements, not a
> contradiction."* Canon therefore already reconciles the pair the flag presents
> as unresolved alternatives: the master-equation magnetic short and the A1
> compliance short are DIFFERENT sectors, not two readings of one.
> **What that clause does NOT settle** — and what stays genuinely open for
> adjudication — is whether the WAVE CHANNEL ITSELF can short, i.e. whether
> μ_eff → 0 is reachable on the transverse channel. `:41` reconciles the
> longitudinal-vs-magnetic pairing; it assigns no sector home to the
> master-equation μ-branch's wave-channel short. That is the routed-open
> μ-at-core fork the prereg already carries verbatim at §2.2 from
> `saturation-rim-inversion.md:70` (*"⚑ OPEN SUB-DETAIL (flagged, not resolved)
> — μ at the knot core. … If `μ → 0` at the core rather than staying cold, the
> `Z_wave → ∞` open-read is complicated."*), so §2.3 and §2.2 are substantially the SAME
> open item counted twice, and the open item is NARROWER than §2.3 frames it.
> This note restores canon's text and states the residue; it adjudicates
> nothing, and no verdict, classifier, or number in this document depends on it.

**The §2.4 replay identity (restated):** with optical activity OFF, a
component-scalar loading, and a component-0 launch, T-MAG's component-0 dynamics
are mathematically the merged Class-C G-J scalar run. T-MAG is a REPRODUCTION
gate (machinery receipt), never an independent transverse measurement and never an
independent confirmation of the scalar locus. All new physics content is T-ELEC
(z = 1/√S — **no prior run found** on any channel that extracts a Γ(A)
response-map off this loading; grep-scope claim, see §D D3 for the exact scope
and for the qualifier this places on the frozen prereg's stronger wording) plus
the cross-loading MIRROR diagnostic.

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

Both configs derived to the SAME windows under the pinned Class-C rule:
**incident [10, 29], reflected [30, 78]**. Provenance, stated exactly (corrected
in round-2 repair; the sentence this replaces said "derived identically from the
shared cold run", which the next line's per-config numbers already contradicted):
the incident window and the wrap-sentinel close branch come from the SHARED cold
run (`derive_windows`, `transverse_gamma_meanstest.py:255-283`, reading
`sanity["t_cF"] / sanity["sigma_t"] / sanity["cold"][…]`), while the
back-monitor close branch (a) is derived PER CONFIG from THAT config's graded
back-monitor series (`transverse_gamma_meanstest.py:588-600`: the loop over
`P["A_grid"]` skips A = 0 and takes `pulse_moments` of each of the 15 remaining
graded runs' `Fb`, then passes `t_back_min = min(cents)` into `derive_windows`;
runs below `bm_measurable_frac` would be dropped, and 0 were) — which is why the two configs
report DIFFERENT back-return bounds below. The equality of the final windows is a
RESULT, not a shared input: the wrap-sentinel branch was binding in both configs,
so branch (a)'s per-config difference never reached the close. Wrap-projected probe arrival
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
  **zero per-point valid-flag differences** vs the banked run (`r3_flag_diffs`
  = `[]`; the foreseen A = 0.3 knife-edge flip did not occur — the A = 0.3
  discordance is reproduced to MACHINE EPSILON, not exactly: 0.19744623329676914
  here vs 0.19744623329676908 banked, Δ = 5.6e-17, and the largest discordance
  deviation anywhere on the 16-point grid is 6.31e-16 at A = 0.8. Both sit more
  than twelve orders of magnitude below the 0.00255 margin that separates
  0.19744623 from `discord_tol` = 0.2,
  so no 1e-16-scale shift can flip the flag. Round-2 repair: the first-round text
  said "reproduced exactly", the same overstatement class §REPAIR item 4
  corrected for R-2.)
- **VERDICT T-MAG (§6.3): REPRODUCED** — a MACHINERY receipt: the new
  2-component graded scatter reproduces the banked Class-C G-J measurement to
  machine epsilon (max |ΔΓ| = 1.7e-16) at the frozen windows. Not an
  independent measurement, not an independent confirmation (§2.4 restated in
  the scope block).
  **How to read the ~1e-16 (round-2 framing note; no number changes).** This is
  ARITHMETIC-FORM agreement, not independent-implementation agreement, and it is
  close to structurally forced: the two codepaths evaluate the same expressions
  at the same degree 3. Banked
  (`research/drivers/engine_gamma_meanstest.py:289-307`: `Yb = 1.0 / z_of_A(Ab)`
  … `a_nodes = 2.0 * Yp / Yp.sum(axis=1, keepdims=True)` … `w = (a_nodes *
  V).sum(axis=1); V_ref = w[:, None] - V`) vs new
  (`src/ave/solvers/transverse_graded_scatter.py:109,168,179-180`:
  `return Y0 / root if load == "magnetic"` … `return 2.0 * Y / Ysum` …
  `w = np.einsum("nd,ndc->nc", a_nodes, V_inc); V_ref = w[:, None, :] - V_inc`) —
  same admittance expression, same coefficient expression, a 3-term reduction
  either way. The paths are nonetheless not bit-identical (the cold observables
  differ in the last bits: t_cF 19.866756764219463 vs banked 19.866756764219467),
  so the achieved value is a real floating-point receipt — but it is a receipt of
  CONTAINER INTEGRITY (the 2-component container did not perturb the scalar
  arithmetic), which is exactly what the frozen gate is for, and the frozen bound
  (1e-6) is ten orders looser than the achieved value. This is why §2.4's
  "MACHINERY receipt, not an independent measurement" scoping is the operative
  reading of R-2, and why R-2 is a §6.5 non-adjudicator of every physics
  question.
- **VERDICT T-ELEC (§6.3): DRAWS-OPEN** — SIGN_top = + ∧ no +→− crossing ∧
  0 θ-crossings. (The SHAPE label is computed separately per §6.2 and is not
  part of this verdict, per §6.3 clause 4.)
- **SHAPE = ELEC-CORE-like (RECORDED, non-adjudicating).** The frozen §6.2
  criterion is qualitative and purely a label: "no θ-crossing ∧ monotone
  increasing within δ". Both conjuncts hold. What was MEASURED, stated at the
  level the run supports: the T-ELEC locus tracks the two-port mirror form
  (1−√S)/(1+√S) to **max |Γ_meas − form| = 0.00112 over the 13 valid points**
  (largest at A = 0.99: 0.45281 measured vs 0.45392 form, ≈ 0.25 % relative),
  and the ELEC-VERTEX (Form-B-algebra) candidate's frozen signature was not
  drawn — no θ-crossing anywhere, and the δ-level sign profile carries no
  negative region at any A ≥ 0.3. That locus is **CONSISTENT WITH** the
  homogenization mechanism the prereg names (§2.7's "ELEC-CORE (homogenized
  mirror)", by analogy to the scalar precedent's homogenized μ-side) **but is
  NOT discriminated by this run — SHAPE is a §6.5 non-adjudicator ("the SHAPE
  label (which candidate T-ELEC draws is recorded, not pass/fail)") and this
  sentence carries no mechanism claim.** The run measured a LOCUS; it did not
  measure homogenization, and no sentence here asserts that a candidate "did or
  did not survive homogenization". (Round-2 repair: the first-round text
  asserted the mechanism — "the ε-loading homogenizes to the two-port mirror
  locus … exactly as the scalar precedent homogenized the μ-side" — which is
  the same defect §REPAIR item 9 fixed for MIRROR; SHAPE now carries the
  identical hedge.) The A\*-probe grid points (0.95–0.99) bracket no sign
  change.
- **δ-level sign profile at A = 0.5 (RECORDED diagnostic, §6.2; non-adjudicating
  per §6.5).** This is the one pre-committed quantitative place the run could
  have gone the other way. The freeze put a homogenization-suppressed vertex
  signature "near −0.036 — below θ but above δ" at A = 0.5 (prereg §2.7:258-262:
  *"At full vertex strength the negative region reaches Γ_B(0.5) ≈ −0.30
  (θ-detectable); homogenization-scale suppression (~×0.12 …) would put it near
  −0.036 — below θ but above δ, hence the δ-level sign profile diagnostic
  (§6.2)"*). Measured: **Γ_TELEC(0.5) = +0.03588** — opposite sign, above δ, at
  the exact A the freeze named, so the diagnostic that was built to keep a
  suppressed vertex signature VISIBLE saw none. Recorded as the §6.2 δ-level
  diagnostic it is; it adjudicates nothing (§6.5 lists the δ-level sign profile
  among the explicit non-adjudicators) and it is not a mechanism claim.
- **§6.4 pair verdict (frozen table, row 1): the two reciprocal impedance
  loadings draw OPPOSITE boundary phases at response-map level** — the ε-side
  locus measured for the first time on any channel (monotone positive to
  Γ(0.99) = +0.4528, toward the OPEN rim), the μ-side the banked deepening
  negative locus reproduced in the 2-component container. Scoped per §2.5 to
  boundary-phase (impedance-sign) content; NO sector-ownership claim (§2.3's
  flagged INVARIANT-S2-vs-master-equation split stands, un-adjudicated); NO
  transverse-distinctness claim (§2.4); #260 untouched.
  **Two qualifiers travel with this frozen cell and must not be dropped if the
  row is reused downstream (round-2 repair):** (i) its "ε-side"/"μ-side" names
  are the prereg §2.2 names for the DECLARED IMPEDANCE MAPS, not constitutive
  attributions — §2.5 states the machinery "cannot distinguish which parameter
  saturates", so the label is a direction name for z = 1/√S vs z = √S and
  nothing more (§D D5); (ii) "measured for the first time on any channel" is the
  frozen wording, and the honest scope of it is "no prior run found that
  extracts a Γ(A) response-map off this loading" — the loading itself is the
  engine's historical Op14 default and HAS been run (§D D3).

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

**Round-2 qualifier entries (2026-08-25).** D2–D5 below are QUALIFIERS on frozen
or previously-asserted TEXT, not run deviations: no parameter, gate, classifier,
verdict, or shipped number is touched by any of them, and the results/raw JSONs
are byte-identical to the run-of-record commit `c0b40d84`. (These are this
document's own D-numbering; the prereg's references to "the Class-C D1/D5" are
the *banked* lane's deviation entries, unrelated.)

- **D2 (2026-08-25) — the pre-freeze adversarial round is DISCLOSED-BUT-UNLOGGED.**
  The prereg's freeze header discloses a pre-freeze round in four lines and names
  only lens TYPES (`..._prereg_FROZEN.md:19-22`: *"**Pre-freeze adversarial check
  (disclosed):** a 3-lens adversarial review (citation-verification /
  gate-fireability / physics-and-sector) ran on the DRAFT of this document before
  freeze; its confirmed findings were repaired in the draft. No run existed at any
  point of that loop."*). **That is the entire landed record.** No per-finding log
  exists on any ref: the prereg has no §REPAIR heading; it landed in ONE commit
  (`git show --stat 81e94565` = 1 file, 773 insertions), so there is no
  draft-and-repair git trail either; and no lane file was found on this branch
  carrying the individually-named catches (grep-scope, `read-don't-grep`: a
  search result, not a proof of absence — but the freeze commit's own shape is).
  Consequently **no finding COUNT from that round is
  auditable and none is asserted here** — any count quoted for it (e.g. in PR
  prose) is unlogged prose, not a receipt, and should not be relied on. The
  reproduction-gate reframe does NOT rest on that round. What carries it, and is
  independently checkable from what shipped, is: (i) the reframe is INSIDE the
  byte-identical freeze commit — `git diff 81e94565 <tip> -- '*prereg_FROZEN.md'`
  is empty, and the frozen text already says T-MAG *"is frozen here as a
  REPRODUCTION gate, not a prediction"* (prereg:17-18) with the full fence at
  §2.4; and (ii) the SUBSTANCE holds numerically — the T-MAG replay identity at
  max |ΔΓ| = **1.665e-16** vs the banked record (`r2_max_dev` in the shipped
  results JSON, gate 1e-6) and the polarization-leak sentinel at **exactly 0.0 in
  all 32 runs** (recomputed from the shipped raw series), which is what makes the
  2-component step S_u ⊗ I₂ in fact and not just in docstring. A faithful
  reconstruction of the pre-freeze log is not possible from the repository, and
  none is fabricated here.
- **D3 (2026-08-25) — novelty claim, restated to its true scope
  (`read-don't-grep`).** The frozen prereg §2.4 asserts *"All of this run's new
  physics content lives in T-ELEC (z = 1/√S has never been run on any channel)"*
  (`..._prereg_FROZEN.md:205-206`). **That parenthetical is FALSE as worded** and is
  qualified here rather than edited (the prereg is frozen). The electric loading
  z = 1/√S is the engine's HISTORICAL Op14 DEFAULT and is run in-tree:
  `src/ave/core/universal_operators.py:788-795` documents it as
  *"load=\"electric\" (DEFAULT, the OPEN form — UNCHANGED legacy behavior):
  Z_eff = Z_0 / √S → ∞ as S → 0. … This is the historical Op14 form
  (universal_operators.py prior default; scale_invariant.impedance_at_strain;
  cosserat_field_3d :340-342)"*, and `src/ave/core/k4_tlm.py:315-318` sets it
  live: *"# Op14 canonical: Z_eff = Z_0 / sqrt(S) … self.z_local_field = 1.0 /
  np.maximum(np.sqrt(S_used), 1e-6)"*. The TRUE and narrower statement — the one
  this result doc makes everywhere — is that **no prior run was found that
  extracts a Γ(A) RESPONSE-MAP off that loading**: the banked Class-C ran the
  magnetic map only (`research/drivers/engine_gamma_meanstest.py:184`:
  *"Canonical impedance map z = sqrt(S(A)) [4.2, shared with chart forms]"*, all
  three configs). Per `read-don't-grep`, even that is reported as a **grep-scope
  claim — "no prior run found", not "never run"**: it states what the searches
  behind this entry returned (the Op14 electric-load consumers named at
  `universal_operators.py:788-795`, `k4_tlm.py:315-318`, and the banked Class-C
  driver's three configs), and it is not a completeness proof over the corpus.
- **D4 (2026-08-25) — the §2.6 departure count undercounts by one.** The prereg
  §2.6 heads its disclosure *"**DECLARED DEPARTURE from one build-brief
  sentence**"* (`..._prereg_FROZEN.md:236`) and then departs from a SECOND brief
  requirement as well: the brief's Stage-1 discipline set requires *"`ave-prereg`
  (frozen, firewalled author — the full Class-C chain is the template, including
  the standalone sentinel checker and the raw-series landing)"*
  (`_orchestration/2026-08-24_static-existence-build-brief.md:37-39`), and this lane
  substitutes a CAUSAL firewall for the organizational one. Nothing is concealed —
  that substitution is disclosed prominently at prereg:7-13 (*"the firewall here
  is CAUSAL, not organizational"*) — but it is attributed there to "the Class-C
  template" rather than to the brief, so "one build-brief sentence" is inaccurate:
  it is two brief requirements, one departed and disclosed in §2.6, one
  substituted and disclosed in the freeze header.
- **D5 (2026-08-25) — the frozen §6.4 row-1 ε/μ labels are MAP names, and must
  travel with that definition.** Row 1 labels the two measured loci by
  constitutive parameter (*"the ε-side (z = 1/√S) locus … the μ-side the banked
  scalar locus"*, `..._prereg_FROZEN.md:682`) while §2.5 of the same prereg
  declares the machinery *"cannot distinguish which parameter saturates"*
  (:216-218) and that the continuum column is *"a DIRECTION label, not what the
  machinery imposes"* (:136-137). As executed this is not a scope violation —
  §2.2 defines ε-side/μ-side as names for the DECLARED maps and this document
  quotes the frozen cell verbatim — but the label would travel without that
  definition if the row is reused downstream. Binding here: **ε-side ≡ the
  declared map z = 1/√S; μ-side ≡ the declared map z = √S; neither names a
  saturating constitutive parameter, and no sentence in this document attributes
  one.**

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
2. **Physics (the new measurement): the ε-side impedance loading z = 1/√S — no
   prior run found that extracts a Γ(A) response-map off it on any channel
   (grep-scope; §D D3) — DRAWS the OPEN boundary phase:** a
   monotone, crossing-free, floorless, window-converged POSITIVE locus rising
   to Γ(0.99) = +0.4528. SHAPE is recorded as ELEC-CORE-like — the locus tracks
   the two-port mirror form to max 0.00112 over the 13 valid points, and the
   ELEC-VERTEX signature was not drawn at either the θ or the δ level. That is
   CONSISTENT WITH the homogenization mechanism §2.7 names but is NOT
   discriminated by this run: SHAPE is a §6.5 non-adjudicator, and this
   sentence carries no mechanism claim. **The run measured a locus; it did not
   measure homogenization** (round-2 repair — the first-round Bottom line said
   "the vertex-counting candidate did not survive homogenization", a mechanism
   assertion on an explicit non-adjudicator; §6 carries the full hedge).
   The pair verdict is the frozen §6.4 row-1 language,
   verbatim: **"The two reciprocal impedance loadings draw opposite boundary
   phases at response-map level — the ε-side (z = 1/√S) locus measured for the
   first time on any channel, the μ-side the banked scalar locus reproduced in
   the 2-component container. Scoped per §2.5 to boundary-phase content; NO
   sector-ownership claim (§2.3's flagged split stands); NO
   transverse-distinctness claim (§2.4); #260 untouched. SHAPE and MIRROR
   reported as diagnostics."** The MIRROR diagnostic (max 0.451 %, median
   0.14 %, §5) is reported per that row as a diagnostic — it is a §6.5
   non-adjudicator and carries no evidentiary weight in the verdict. The frozen
   cell is quoted as frozen; the two qualifiers that travel with it (the
   ε-side/μ-side names are §2.2 names for the DECLARED MAPS, not constitutive
   attributions; and "for the first time on any channel" means "no prior
   response-map run found") are stated at §6 and in §D D3/D5. The
   sector-ownership question (§2.3) and the transverse-vertex item (§2.6)
   remain OPEN, exactly as frozen — and per the §2.3 round-2 note above, canon
   itself already reconciles the A1-compliance-vs-magnetic-branch pairing; what
   is open is narrower (no sector home for the μ-branch's wave-channel short).

No VOID condition fired; no closed negative's config was reconstructed (§1).
The ≥3-lens adversarial verify ran on this document's first committed draft per
prereg §9.6, and a 6-lens orchestrator clearing review then ran on the repaired
tip; every finding's disposition from both rounds is logged in §REPAIR below
(round 2 as its own table), and the repaired text above is the record of record.
No round-2 repair moved a number, a verdict, a gate outcome, or a classifier. Verdict language is
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

### §REPAIR round 2 — orchestrator clearing review (2026-08-25)

A 6-lens orchestrator clearing review ran on the branch tip `61b0f05b` (the
post-§REPAIR state above). Two of its lens objects address this document: the
citation/numerics lens (2 MAJOR + 3 MINOR) and the canon/sector lens (2 MAJOR +
3 MINOR). Both returned **DEFECTS-FOUND, all reporting-layer, no BLOCKER**.
Every finding is dispositioned below. **NOTHING in the run moved:** no shipped
number, verdict, gate outcome, or classifier changed, no driver or module line
was touched, and the results/raw JSONs are byte-identical to `c0b40d84` (SHA-256
re-checked before and after this round).

| # | finding (severity) | disposition |
|---|---|---|
| L1-1 | Pre-freeze "66 findings repaired" claim has no log on any ref; unauditable prose (MAJOR) | **FIXED — honest disclosure landed, no log fabricated.** New **§D D2**: the round is **DISCLOSED-BUT-UNLOGGED** (the prereg's 4-line lens-type disclosure is the entire landed record; no §REPAIR heading, one-commit freeze, no per-finding trail on any ref); **no count is asserted or auditable**; what carries the reproduction-gate reframe is (i) the reframe living inside the byte-identical freeze commit and (ii) independently re-verified substance — T-MAG replay identity 1.665e-16 and C1 leak exactly 0.0 in 32/32. A faithful reconstruction is not possible from the repository and none was invented. |
| L1-2 | Mechanism claim asserted on SHAPE, an explicit §6.5 NON-ADJUDICATOR ("homogenizes … exactly as the scalar precedent homogenized the μ-side"; Bottom line "did not survive homogenization") (MAJOR) | **FIXED — the load-bearing one.** §6's SHAPE bullet rewritten to the exact hedge §REPAIR item 9 applied to MIRROR: locus **CONSISTENT WITH** the §2.7 homogenization mechanism **but NOT discriminated by this run — a §6.5 non-adjudicator, carrying no mechanism claim** — plus the explicit sentence *"the run measured a LOCUS; it did not measure homogenization"*. The "did not survive homogenization" wording is GONE from both §6 and the Bottom line. Measured content restated at the level the run supports (tracking to max 0.00112 over 13 valid points; ELEC-VERTEX signature not drawn at θ or δ). Per the lens's under-featuring note, the one pre-committed quantitative discriminator is now stated in its own bullet as the §6.2 δ-level diagnostic it is: freeze named ≈ −0.036 at A = 0.5, measured **+0.03588** — opposite sign, above δ, at the named A; recorded, non-adjudicating. |
| L1-3 | "discordance 0.197 reproduced exactly" false at full precision (MINOR) | **FIXED.** §6 now states machine-epsilon: 0.19744623329676914 vs banked 0.19744623329676908, **Δ = 5.6e-17**, max grid deviation **6.31e-16 at A = 0.8**, against the 0.00255 margin to `discord_tol` = 0.2 — recomputed here from the two shipped JSONs, `r3_flag_diffs = []` confirmed. Substantive claim (no A = 0.3 flag flip) unchanged and true. |
| L1-4 | Window-provenance sentence wrong: the close derivation consumes each config's GRADED back-monitor runs, not just the shared cold run (MINOR) | **FIXED.** §3 restated exactly: incident window + wrap-sentinel branch from the SHARED cold run (`derive_windows`, `:255-283`); back-monitor branch (a) derived PER CONFIG from that config's 32 graded `Fb` series (`:588-600`) — which is why the two back-return bounds differ (112.48 / 112.67). Window EQUALITY is now stated as a RESULT (the wrap branch was binding in both), not as a shared input. |
| L1-5 | "Reproduces to machine epsilon" invites over-reading as independent-implementation agreement (MINOR, framing) | **FIXED.** §6 carries a framing note: the ~1e-16 is **arithmetic-form** agreement (same admittance and coefficient expressions, 3-term reduction either way — banked `engine_gamma_meanstest.py:289-307` vs new `transverse_graded_scatter.py:109,168,179-180`, both quoted), close to structurally forced, with the frozen gate ten orders looser; the paths are nonetheless not bit-identical (t_cF 19.866756764219463 vs 19.866756764219467). Scoped as a **container-integrity** receipt — which is what the gate is for — reinforcing §2.4's "MACHINERY receipt, not an independent measurement". |
| L3-1 | §2.3 flag truncates canon's sentence at the em dash, dropping canon's own reconciliation (MAJOR) | **FIXED.** The scope block's §2.3 restatement now carries `resonant-lc-solitons.md:41` **in full, verbatim**, including *"— so this leaf's electric-sector Z→0 confinement and the master-equation magnetic-branch confinement are distinct-sector statements, not a contradiction"*, and states precisely **what it does NOT settle**: no sector home for the μ-branch's **wave-channel** short (μ_eff → 0), which is the routed-open μ-at-core fork already carried at §2.2 from `saturation-rim-inversion.md:70` — so §2.3 and §2.2 are substantially ONE open item, narrower than §2.3 frames it. Adjudicates nothing; the frozen prereg is untouched. |
| L3-2 | Frozen §2.4's "z = 1/√S has never been run on any channel" is false as worded (MINOR here; prereg frozen) | **FIXED by qualifier, not edit.** New **§D D3**: the electric loading IS the engine's historical Op14 default and is run in-tree (`universal_operators.py:788-795`, `k4_tlm.py:315-318`, both quoted); the true, narrower statement is **"no prior run found"** that extracts a Γ(A) response-map off it (banked Class-C ran the magnetic map only, `engine_gamma_meanstest.py:184`). Wording changed to "no prior run found" at both live sites (§2.4 restatement, Bottom line) and flagged as a **grep-scope claim** per `read-don't-grep`. The frozen §6.4 row-1 quote stays verbatim with the qualifier attached beside it. |
| L3-3 | §2.6's "one build-brief sentence" undercounts the declared departures by one (MINOR; prereg frozen) | **FIXED by qualifier.** New **§D D4**: the brief's discipline set also requires a *firewalled author* (`build-brief.md:37-39`), for which this lane substituted a CAUSAL firewall — disclosed at prereg:7-13 but attributed there to "the Class-C template" rather than to the brief. Nothing concealed; the count is corrected in the result. |
| L3-4 | Residual SHAPE sentence reaches past the frozen classifier + unreceipted tracking claim (MINOR) | **FIXED — same repair as L1-2**, plus the tracking claim now carries its receipt: **max \|Γ_meas − (1−√S)/(1+√S)\| = 0.00112** over the 13 valid points (≈ 0.25 % relative at A = 0.99; 0.45281 measured vs 0.45392 form), recomputed here from the shipped table. Verb softened from "homogenizes" to a recorded, consistent-with, explicitly-not-discriminated statement. |
| L3-5 | Frozen §6.4 row-1 labels measured loci by constitutive parameter while §2.5 fences that attribution (MINOR; prereg frozen) | **FIXED by qualifier.** New **§D D5** plus an inline qualifier beside the §6 pair verdict and the Bottom-line quote: **ε-side ≡ the declared map z = 1/√S, μ-side ≡ z = √S** — §2.2 names for DECLARED MAPS, never constitutive attributions (§2.5: the run "cannot distinguish which parameter saturates"). Stated so the label cannot travel downstream without its definition. |

**Receipts-unchanged proof for this round.** SHA-256 of
`research/drivers/transverse_gamma_meanstest_results.json`,
`data/transverse_gamma_meanstest/{cold_sanity,raw_TMAG,raw_TELEC}.json` and
`run_log.txt` were captured before the first round-2 edit and re-checked after
the last: **identical**. `git diff --stat c0b40d84..HEAD` touches this result
document only — no driver, module, checker, figure, or data file. Every number
quoted in the repairs above was recomputed by the repair session from the
shipped JSONs, and every file:line cite was re-read at the branch tip before it
was written.
