# NOTE — Harmonic-balance solver on the graded srs network: Stage-2 validation receipts

**Build brief:** [`_orchestration/2026-08-24_static-existence-build-brief.md`](../_orchestration/2026-08-24_static-existence-build-brief.md) Stage 2.
**Design ruling consumed:** [`research/2026-08-24_g1-ac-steady-state-walk_RECORD.md`](2026-08-24_g1-ac-steady-state-walk_RECORD.md) (the AC-steady-state reframe).
**Module:** `src/ave/solvers/harmonic_balance_srs.py` · **Tests:** `src/tests/test_harmonic_balance_srs.py` ·
**Driver:** `research/drivers/harmonic_balance_validation.py` · **Receipts:** `research/drivers/data/harmonic_balance_validation/receipts.json` ·
**Gating checker:** `research/drivers/harmonic_balance_number_check.py` (auto-discovered by `make verify`; mutation-receipt live).

## Sector header (house table)

| axis | declaration |
|---|---|
| MODE | scalar channel on the srs-z3 carrier (the Class-C lane's); T2/Cosserat NOT wired; A1 ⊥ T2 honoured |
| REGIME | linear (gates 1–2: cold / frozen-S); the self-consistent S-field machinery reaches regime-2 nonlinear but is validated here only on its convergence receipts, not on any physics claim |
| PHASE-STATE | AC steady state — stationary, not DC: the phasor description is a fixed point ("everything moves, nothing changes", G1 walk §1) |
| CLASS | **Engineering tool / instrument-grade infrastructure. Nothing minted.** No fork adjudicated, no solidity moved, no (2,3) tone set run. The P2 existence solve is gated on the G2 frozen prereg and is NOT this document. |

**Consistency-vs-emergence classification of every gate below: implementation-verification** (instrument consistency against (i) the canonical analytic band map, (ii) the lattice's own measured response map, (iii) constructed known cases). The 0-ish deviations below are instrument calibration, not predictions.

## What the solver is

Phasor-domain Kirchhoff fixed point on the graded srs TLM network: posit a tone set {θ_m} (rad/step; harmonic balance posits tones, not tube phases — epic guard 8), solve

> e^{iθ_m} v_m = M(S) v_m + sources,  M(S) = C · blockdiag(S_u),  S_ij = 2Y_j/ΣY_k − δ_ij,  Y = Y₀/√S(A)

with the S-field a self-consistent unknown read from the DP-1 cycle-average envelope of the tone phasors (A_b² = Σ_m |v_m,b|²/2 per yield² — the cross-tone terms time-average to zero, so the multi-tone rule is derived, not chosen). No time axis; no damping device; Ax3 untouched by construction — the graded scatter conserves the Y-weighted energy exactly (tested to 1e-12), and the only sink is a declared matched termination (a boundary condition, checkpoint-10 class, never a bulk loss term). Source-idle machinery measures scaffold-removability: source amplitude, scaffold exchange, the autonomous defect r_auto = ‖e^{iθ}v − M_full v‖/‖v‖, and the power ledger — all computed, thresholds always caller-declared.

## The coordinate map (phase-space-coordinate-check, declared)

The measured Class-C Γ(A) ([`2026-08-24_engine-gamma-meanstest_result.md`](2026-08-24_engine-gamma-meanstest_result.md)) is the **time-window-isolated front-face echo** of a pulse. A steady state has no time axis, so the same physical quantity is reached by a different isolation: the interface is measured as a linear two-port in the single-Bloch-mode basis — fit traveling waves on both sides, repeat with the absorbing load at ≥3 positions, and solve b = Γa + T′d, c = Ta + Γ′d for the interface's own (Γ, T, Γ′, T′). **Γ with the far side matched (d = 0) is exactly the front-face quantity the time-windowed measurement reports.** The two-port model's validity is a computed overdetermination residual, never an assumption. This de-embedding is also what removes the scaffold's own artifact: a bond-matched termination is an imperfect absorber of the Bloch wave — the committed receipt `gate2.cold_single_load_gamma_raw` records the raw single-load |Γ| at A=0 (the artifact-only composite, ~0.10 per load plane at θ=0.15), and single-solve Γ readings without de-embedding are biased by exactly that amount. Sign convention mapped to the measurement's signed-real one (Γ < 0 = polarity-inverted echo); the solver's Γ phase is a computed receipt (≈ π at quasi-static θ).

## Gate results (each computed by the driver, re-verified by the gating checker and the regression tests)

### Gate 1 — cold linear limit → the arccos band structure: **PASS**

Cold srs L=8, θ sweep 0.05→0.80 rad/step, driven solve + traveling-wave k-fit (fit residuals ≤ 3e-8, solve residuals ≤ 2e-12):

- **Velocity factor:** c(θ=0.05) = 0.577320 vs `ANALYTIC_NETWORK_FACTOR` = 1/√3 = 0.577350 — rel. dev. **0.005%** (frozen CS-2 gate: < 2%). PASS.
- **Arccos map:** max |θ_band(k_fit) − θ| = **4.2e-9 rad** over the 8-point sweep (tol 1e-3), where θ_band is the nearest band of θ_n(k) = arccos(μ_n(k)/3) from the net's own Bloch adjacency. Branch identification is honest and can-fire-tested: μ_max labels the acoustic branch only below the first band crossing (at θ = 0.8 the fitted k lies on folded band 6 with θ_band = 0.800000); a deliberately wrong k sits ≥ 0.05 rad from every band (test receipt). PASS.
- **Band edge (CS-2 criterion re-applied):** all 4 swept points with k ≤ the measured cold-gate k_edge = 0.37024 have c within **0.084%** of 1/√3 (tol 5%). PASS.

### Gate 2 — single-tone graded limit → the MEASURED Class-C response map: **PASS**

Geometry loaded from the measured run's own params (L=24, srs right, x_I=9, x_B=15; N=110 592). Single tone θ=0.15 rad/step (inside the measured pulse band), 3 absorber loads (11.5/12.0/12.5 cells), de-embedded interface Γ per the declared coordinate map. Target: the 13 measured-VALID G-J points of [`engine_gamma_meanstest_results.json`](drivers/engine_gamma_meanstest_results.json) `table.GJ`.

- **Cold null:** |Γ(A=0)| = **6.3e-10** through the identical chain (the scaffold's ~10% bond-matched-cut artifact is fully removed by the de-embedding; de-embed residual 1.5e-8).
- **All 13 points PASS**, max |Γ_solver − Γ_measured| = **0.00129** (at A = 0.99), a factor ~8 inside the 0.010 tolerance floor; per-point deviations run from 2e-5 (A = 0.7) through (1–2.4)e-4 over the grid interior, rising toward the rail ((3.9–12.9)e-4 for A ≥ 0.9). Γ phases 2.975–2.988 rad (≈ π, the polarity-inverted class — matching the measured sign convention at every point). De-embed (two-port model) residuals ≤ 4e-8.
- **θ-flatness receipt:** at A = 0.9, Γ(θ=0.10/0.15/0.20) spread = **7e-5** — the θ = 0.15 choice is quasi-static to well below the comparison band.
- Figure: [`fig1_gate2_overlay`](figures/2026-08-24-harmonic-balance-solver/fig1_gate2_overlay.png) — measured points and solver points overlap on the core locus.

**Reading, honestly bounded:** the lattice's measured pulse-echo response and this solver's steady-state fixed point agree on the graded-interface reflection to ≤ 1.3e-3 absolute across the full valid grid — two estimator classes drawing the same curve. This is instrument cross-validation; it asserts nothing beyond the response map already banked by the Class-C result.

### Gate 3 — source-idle machinery on the known driven-vs-autonomous pair: **PASS**

Declared thresholds: source_tol = 1e-12, exchange_tol = 1e-12, r_auto_tol = 1e-10.

- **Initialized lossless ring** (N=12, m=2, θ = k = 1.0472): r_auto = **5.7e-16**, source = 0, exchange = 0 → **idle** (the trivial side, exact).
- **Driven cold srs tank** (L=2, θ=0.3): source amp 1.0, scaffold exchange 0.999 (the lossless tank returns O(1) to the scaffold), r_auto = **0.628** → **not idle** (solve residual 2.4e-12).

The machinery separates the pair by >14 orders of magnitude in r_auto with all observables computed from the solved state.

## Honest caveats and flags

- **Termination artifact (measured, then de-embedded).** Bond-matched cuts reflect O(10%) of the Bloch wave — the raw measurement is the committed `gate2.cold_single_load_gamma_raw` receipt (single-load |Γ| at A=0, per load plane); all Γ receipts go through the multi-load de-embedding. A single-load reading from this instrument is NOT calibrated — the module docstring says so.
- **Fit-region discipline.** Traveling-wave fits keep declared evanescent margins off interfaces and terminations (gate 2: 1 cell off the source plane and the interface on the feed side, 0.5 cells inside the slab; gate 1: 0.5 cells off the source, 0.7 off the absorber — all echoed in the driver's parameter block); fit residuals are receipts in the JSON.
- **Gate-2 tolerance is an ENGINEERING-CHOICE** (abs floor 0.01, rel 5%): floor from the two instruments' null floors (measured ε₀ = 0.00545; this instrument's cold null below), band from the measured locus's own 0.2–2% spread vs the core curve and the different estimator classes (pulse matched-filter vs steady-state fit). Tagged, not derived.
- **The lumped-model trap is closed by construction**: the linear operator is the certified scatter+connect map itself; its cold dispersion is the arccos TL map (the graph-Laplacian √λ model, which fails the frozen 1/√3 gate, appears nowhere).
- **ω_C scale-label (R1/R2)**: all gate-1 numbers are in engine units (rad/step, bond-lengths); the canonical R2 labeling (c₀ = c_link/√3) is cited for the KB comparison only, so the R1/R2 flag (srs-band-structure.md:153-157) never enters the arithmetic.
- **Structural config-disjointness from the closed negatives** (the G2 prereg owes the full config-grep; this is the solver-level receipt): the module has no time axis, no dt and no dt→0 limit to take, no free-precursor genesis, no pump ramp; the S-field updates only from the cycle-average envelope of a steady state. The instrument cannot reconstruct the energize-LOCK config class by construction — but the grep is still owed at G2, not waived here (G1 walk §5).
- **R40-B2a carried**: the longitudinal-TLM-port reading on the reused n-port machinery is DEMOTED (NEEDS-RE-DERIVATION, BIAS-DEBT); this module load-bears only the network/scatter algebra and the C_eff = C₀/S bond-compliance reactance. Dated note at the end of the module file; epic guard 6 honoured.
- **A_cap floor caveat travels** (vacuum-varactor index note): the canonical kernel caps A at 0.99; gate 2's grid tops at A = 0.99 where cap and floor are inactive, so the caveat is dormant here but applies to any future use beyond the grid.

## Deviations register

- **D1 (2026-08-24) — first-run gate-1 FAIL was a check bug, not a solver defect.** The first validation run FAILED gate 1 at θ=0.8: μ_max labels the acoustic branch only below the first band crossing (the fitted k lies on folded band 6, θ_band = 0.800000). Fixed to nearest-band identification with the deviation as the receipt plus a can-it-fire counter-test; the solver's numbers were unchanged; the run of record is the post-fix rerun.
- **D2 (2026-08-24, post-review repair round).** The 3-lens adversarial self-review (3 finders → refute-first verify per finding) returned 4 CONFIRMED-MAJOR + minors; all repaired before hand-off: (a) `crossing_ports` made wrap-aware (planes within one bond-x-extent of the periodic boundary were silently invisible — latent only; every committed plane is interior and its port set is unchanged); (b) `ToneSet` canonical-domain guard (0, π) enforced (pairwise distinctness under-enforced the DP-1 precondition: {θ, 2π−θ} is one physical line; θ = 0/π self-conjugate), with docstrings corrected and the DP-3 R2-fix (V_inc, Φ_link) tank form cited as the canonical envelope this module's C-state projection operationalizes; (c) end-to-end two-tone machinery test committed (shared-S-field coupling shown real, with a cold decoupling control); (d) the ~10% termination-artifact claim now carries a committed receipt (`cold_single_load_gamma_raw`), the receipts were regenerated by the amended driver (gate verdicts and every solve number unchanged — the amendment only ADDS the receipt field and an empty-band log guard), and two note sentences (fit margins, per-point deviation ranges) were corrected to match the receipts exactly.
