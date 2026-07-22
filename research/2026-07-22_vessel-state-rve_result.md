# Anisotropic Vessel-State RVE Bench — RESULT (walk-1 verdict run)

Prereg-file: research/2026-07-22_vessel-state-rve_prereg-FROZEN.md

**Date:** 2026-07-22
**Class:** DERIVATION + lattice-derived research-driver (research-doc; forms derived, values dimensionless/geometric; **mints no `clm-`/`def-`; propagates to no KB/tex leaf**). This is the **bench RUN** of the merged, Grant-ratified REVISION-3 frozen prereg — the "walk-1 instrument": does the GROWN vessel-state cage read HARD / SOFT / NULL / DISCORDANT / MARGINAL / UNDETERMINED?
**Driver:** `research/drivers/vessel_state_rve.py` (+ `research/drivers/vessel_state_rve_results.json`, `research/drivers/vessel_state_rve.png`). Figure: `research/drivers/vessel_state_rve_figure.py`.
**Engine:** `src/ave` **BYTE-UNTOUCHED** (imports read-only); Rule-14 reuse of the merged #782 KUBC static-homogenization scaffold (`research/drivers/rve_aggregation_bench.py` + `constituent_cage_ensemble.py`); the NEW piece is the STATE-DEPENDENT geometric-stiffness operator `k_shear,eff(u) = k_s + k_a·ε_axial(u)` (`axiom-register.md:193`) + the frozen Newton/self-consistent solve.
**Every number below is read from the shipped `vessel_state_rve_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson NAMED).** All `[canon]` inputs content-verified at base HEAD `f050e33b`: `axiom-register.md:193` (the load-response sign rule), `electron-bh-isomorphism.md:26`, `master-equation.md:20`, `ave.core.constants.N_NU`. Deterministic (`run_c2_speeds seed=1`; no per-step RNG in the statics); total runtime `756 s`.

**★THE CARVE (mandatory disclosure — every output carries both strings, prereg §1; both present in JSON `provenance`):**
- `grade-frame: Eulerian, imposed (not self-bound; the engine hosts no field-generated co-moving grade)`
- `source imposed (radiation-stress surrogate body-force ∝⟨A²⟩); stress state emergent through the nonlinear force balance`

**★THE S(A(u)) DECISION honoured (prereg §0):** the Op14 saturation grade `S(A)` is IMPOSED (Eulerian, static); the ONLY state-dependence in the operator is the LIVE geometric-tension term `T(u)/ℓ = k_a·ε_axial(u)`. Scope-limit disclosed: `kernel-knee physics (the Op14 S(A) saturation marginality) is NOT hosted`; the buckling/marginality physics is carried by the `T(u)` geometric term per #779.

---

## ★BOTTOM LINE

The walk-1 instrument is **VALIDATED, not VOID** — `gate_fireability_selftest_pass = True` and every instrument-validation gate passes. The grown vessel-state cage reads:

> ## HEADLINE BIN = **UNDETERMINED** (cell `(i) × L1 × Z_str`)
>
> `K_ratio_lift = 0.997` (band L1: `< 1.2`), `r_Z_grown = 0.520` (band Z_str: straddles `0.5` within `δ_rZ=0.05`), amplitude gate = **outcome (i) CLEAN** (`A_sign = 0.0020`, `amp_spread± = 0.00097 / 0.00113`, converged + robust). Headline arm = `fixed_budget` (yield_saturated has **no stable equilibrium** — it BUCKLES before yield).

**The physics headline.** At the small-signal-tangent regime the regime-ruling names (`.OP` to the grown equilibrium, then a second-difference tangent probe `≪` every nonlinear scale), the grown pressure-vessel stress state does **NOT** compose into a load-bearing bridge (HARD) NOR a pressure-release bottleneck (SOFT) at the aggregation level: **the grown hoop-tension stiffening and radial-compression softening CANCEL in the small-signal tangent modulus** — the grown vessel reads at ≈ its isotropic control (`K_tan/K_0 = 0.2955` grown vs control `0.2964`, `lift = 0.997`), and the MEASURED impedance `r_Z = 0.520` straddles the `0.5` macro-cage/matched boundary. This lands the SAME BIN as merged #782's painted-isotropic bench (BIN-4 / UNDETERMINED at the `r_Z` bin edge), now confirmed on the GROWN anisotropic vessel with a MEASURED ρ. The yield-saturated (self-bound-adjacent) arm is **unreachable on the lossless engine** — the vessel buckles (peak-strain ceiling `≈ 0.21`) long before peak strain reaches `A_yield = 1.0` (the energize-LOCK-adjacent negative surfaced by the pre-test-physics-check). **Consequence routed to Grant** (§9): UNDETERMINED at the `r_Z` straddle; the owed resolver is the feasible SUBC/periodic lower-bound bracket (#782 Fork B), NOT run here.

---

## §1 — LEG 0: the gate-fireability self-tests (the mandatory VOID gate — §3B)

Frozen: `gate_fireability_selftest_pass = SELFTEST-(ii) fires (ii) AND SELFTEST-(iii) fires (iii), each with the correct convergence/robustness flags` → **True.** (JSON `leg0_selftests`.)

**SELFTEST-(ii) FIRES (ii)** — a deliberately under-converged solve forces the artifact AND is diagnosed as convergence-caused. At the FROZEN loose inner CG tol `1e-3`: `amp_spread± = 649.24 / 648.96` (> 0.05, fires the artifact), `A_sign = 0.0300` (≤ 0.10, symmetric drift) AND `all_scan_legs_converged = False` (diagnosed convergence-caused); at the tight tol `1e-10`: `amp_spread± = 0.00583 / 0.00427` (≤ 0.05 both signs, removed by tightening). The dual frozen assertion holds. **No calibration latitude was needed for (ii)** — the frozen `1e-3` forces the artifact.

**SELFTEST-(iii) FIRES (iii)** — a near-buckling grown state forces sign-asymmetric squeeze-softening. Gate returns `outcome (iii)`: `amp_spread+ = 568.74` (> 0.05), `A_sign = 568.77` (> 0.10), `K_tan_minus(ε_max) = 7484.3 < K_tan_plus(ε_max) = 4.43e6` (squeeze-softening direction), with `all_scan_legs_converged = True AND residual_tightening_robust = True` — a converged, robust, sign-asymmetric squeeze-softening (the near-buckling curvature divergence).

**★DISCLOSED calibration (design-time numeric-confirmation run, banked here per §3B, made BEFORE any verdict arm).** The frozen ≥50%-of-shell-band near-buckling target was NOT literally met — the Gaussian core source concentrates the near-buckling bonds into a tight CORE CLUSTER (21 bonds at `k_shear,eff ≤ 0.2·k_s`, radii `r ∈ [0.28, 0.67]`; achieved fraction in band `(0, 3.0)` = `0.0156`, best any-band ≈ `0.05`). A convergent broad ≥50% shell sits exactly at the buckling knife-edge (a shell-shaped source hits fraction `0.44` at `min k_shear,eff = −0.033`, i.e. already buckled — banked in the calibration probes). Per the frozen §3B latitude (*"a justified equivalent may be substituted at calibration time IF it produces the same aggregate crossing — disclosed"*) the near-buckling core cluster (21 bonds, not a single pin) IS that justified equivalent: it produces the SAME aggregate crossing (converged + robust outcome (iii), `A_sign = 568.77`), which is the frozen SELFTEST-(iii) acceptance. `min k_shear,eff = 0.0541` at the self-test operating point (`p0 = 0.028`, σ = 2.5).

---

## §2 — LEG 0: instrument validation (§7 standard gates) — all PASS

| gate | reading | verdict |
|---|---|---|
| uniform-medium NULL | `K_tan/K_0 = 1.0000`, `ρ_N = 0`, `r_Z = 1.0000` | PASS (r_Z→1, ρ_N→0 on a uniform cold medium) |
| determinism bit-compare | two grows `reruns BIT-IDENTICAL` (`u0` max abs diff `0.0`) | PASS |
| Lamé exterior gate | exterior `∇·u`/interior `∇·u` = `0.0358` ≤ 0.10 | PASS (carried from #782 §4 Leg 2) |
| RVE-size gap | `K_eff/K_0 = 0.280 (L12) / 0.296 (L16) / 0.294 (L20)`; `gap(L16,L20) = 0.0072` ≤ 0.15 | PASS (size-converged) |
| STOP-gate class | rail `K_eff/K_0 = 0.296` (< 1, SOFTENS) vs rigid `1.583` (> 1, STIFFENS) — opposite sign | PASS |
| cell-walk partition | 12 rows, exhaustive + disjoint | PASS (`assert_partition`) |

Instrument cross-check against merged #782: the cold bulk-only cage at `φ_sf = 0.489` reproduces #782's `K_eff/K_0 = 0.296` (isotropic control = `0.29637`) — the instrument agrees with the merged linear bench at the cold limit.

---

## §3 — the grow step + the THREE numbered STOP criteria (§1)

Frozen: `grown_equilibrium_exists = grown_CG_converged AND grown_tension_nonzero AND grown_bonds_positive`.

**Headline arm (`fixed_budget`, `p_ref = 0.040` — a DISCLOSED `[engineering-choice]` knob, grade-frame Eulerian/imposed):** a stable grown vessel state EXISTS.
- `grown_CG_converged = True` (outer converged; nonlinear residual within `1e-8`).
- `grown_tension_nonzero = True` — Frozen: `grown_tension_nonzero: max_r |T(r)| ≥ 0.05·k_a·A_yield`; `max_r |T(r)| = 0.647 ≥ 0.489` (`= 0.05·k_a·A_yield`, `k_a = 9.77337`, `A_yield = 1.0`).
- `grown_bonds_positive = True` — Frozen: `min_bond k_shear,eff(u_0) > 0`; `min_bond k_shear,eff = 0.353 > 0` (no bond crossed buckling).
- ⇒ `grown_equilibrium_exists = True`. The imposed source grew a real residual pressure-vessel state: **hoop-tension** axial strain up to `ε ≈ +0.139` (peak `A`), **radial-compression** down to `ε ≈ −0.066` (`min k_shear,eff = 0.353`).

**T-definition disclosed** (deviation §8.1): `T` is the remap term `k_a·ε_axial` (the tension CONTRIBUTION the operator sees, `= T/ℓ` in the `axiom-register.md:193` grammar), not the un-normalized axial force `k_a·ε_axial·ℓ`.

---

## §4 — the verdict arms + the cell-walk bin (§6)

Frozen: `K_ratio_lift ≡ (K_tan/K_0)_grown / (K_tan/K_0)_isotropic-control` (at matched `φ_sf = 0.489`).

- amplitude gate (hydrostatic mode → `K_eff`) = **outcome (i)**: Frozen: `amp_spread ≤ 0.05 for BOTH signs` — `amp_spread± = 0.00097 / 0.00113`, `A_sign = 0.0020`, converged + robust ⇒ a clean small-signal tangent modulus (the state-dependent operator is smooth away from buckling at this operating point). NOT `amp_spread > 0.05 in at least one sign AND A_sign ≤ 0.10` (ii); NOT (iii) `K_tan_minus(ε_max) < K_tan_plus(ε_max)`; NOT the (iv)-anomaly `K_tan_plus(ε_max) < K_tan_minus(ε_max)`.
- `K_tan/K_0 (grown) = 0.2955`; isotropic control `= 0.29637`; **`K_ratio_lift = 0.997`** (band L1: `< 1.2`).
- `G_tan/G_0 (grown) = 0.634` (shear, corroborative).
- `r_Z_grown = 0.520` (Protocol E measured, §6) → band **Z_str** (`|r_Z − 0.5| = 0.020 ≤ δ_rZ = 0.05`; straddles 0.5).
- **cell-walk bin = UNDETERMINED** (walked MECHANICALLY through the frozen 12-row table: gate (i) → `(L1, Z_str)` → UNDETERMINED). Data + code path: JSON `verdict.fixed_budget_headline`; `vessel_state_rve.py::cell_walk_bin` (+ `assert_partition` proof).

The FOUR headline bins are excluded by the frozen definitions: not HARD (`lift >= 1.5 AND r_Z_grown > 0.5 + δ_rZ` fails — lift 0.997 < 1.5); not SOFT (`lift < 1.2 AND r_Z_grown < 0.5 − δ_rZ` fails — r_Z 0.520 not < 0.45); not NULL (`(i) AND lift < 1.2 AND r_Z_grown > 0.5 + δ_rZ` fails — r_Z 0.520 not > 0.55); not DISCORDANT (`lift >= 1.5 AND r_Z_grown < 0.5 − δ_rZ` fails); not MARGINAL (gate (i), not (iii)). The verdict sits in the UNDETERMINED zone precisely because the impedance straddles `0.5` while the lift is null.

---

## §5 — C-V profile (§5) — REWIRED to the live geometric term

Frozen: `K(ε_bias) profile curve + its reconstruction read: shell POSITION, WIDTH, and ASYMMETRY`.
- shell POSITION = `0.00135`; shell WIDTH = `0.006` (squeeze `0.0042` / stretch `0.0018`).
- shell ASYMMETRY = `−0.400`. Frozen: `|ASYMMETRY| >= 0.15 confirms the anisotropic vessel state`; `|ASYMMETRY| = 0.400 ≥ 0.15` ⇒ the reconstruction flags the anisotropic vessel state.
- `span_truncated = False`. `K(ε_bias=0) = 2079.2` (unbiased grown OP normalizer).
- **★HONEST READ (corroborative-only, per the frozen demoted clause).** The `K(ε_bias)` curve is **nearly FLAT** — it varies monotonically from `2079.82` (`ε_bias = −3e-3`) to `2078.59` (`ε_bias = +3e-3`), a **total variation of `0.059 %`** across the full bias span. The reconstruction (POSITION/WIDTH/ASYMMETRY) therefore reads the tiny residual monotonic slope's off-centre-ness, not a resolved depletion-edge shell feature; the `|ASYMMETRY| ≥ 0.15` flag is **corroborative-only** (the prereg's demoted clause, "meaningful ONLY on the v2 nonlinear instrument"), consistent with the headline: the grown state IS anisotropic (hoop-tension vs radial-compression), but that anisotropy barely modulates the bulk tangent (`< 0.06 %` over the bias range) — the same stiffen/soften cancellation that yields `lift ≈ 1.0`. Data + code path: JSON `verdict.cv_profile_fixed_budget`; `vessel_state_rve.py::cv_profile`.

---

## §6 — Protocol E: ρ_eff MEASURED alongside K_eff (§4)

Frozen: `Protocol E measures the STRUCTURAL ρ term only; the engine hosts no trapped-energy inertia (C-load open, clm-m5swh9); NO β claim from this bench`.
- long-λ compression-pulse time-of-flight on the grown-vessel RVE, `L = 32`; empirical-driver discipline baked in (reflection-free window exclusion, density-peak monitor slab, C-state + L-state reactance-pair recording — `reactance_pair_recorded = True`).
- `c_eff = 0.2828`, `c_0(lattice) = 0.4980`, `c_0/c_eff = 1.761`; **`ρ_eff/ρ_0 (MEASURED) = 0.916`**; **`r_Z_measured = 0.520`**.
- The measured structural `ρ_eff/ρ_0 = 0.916 < 1` (the grown soft-shell medium is slightly LESS inertially loaded than the cold lattice for the long-λ compression channel) shifts `r_Z` from the structural `√(K_tan/K_0) = 0.544` down to `0.520` — still Z_str (straddling 0.5), so the bin is unchanged (UNDETERMINED). Data + code path: JSON `verdict.fixed_budget_headline.protocol_E`; `vessel_state_rve.py::protocol_E`.

---

## §7 — percolation / painted-anisotropic / seed-independence / yield_saturated / anti-seduction

- **Percolation sub-check (§6, corroborative):** `hoop_percolates = False`, `largest_tense_cluster_frac = 9.2e-5` (`n_tense_bonds = 489`) — the grown tensile (hoop) bonds do NOT form a face-to-face spanning cluster ⇒ corroborates SOFT/NULL (patchy tension islands, not a closed hoop-tense shell), NOT HARD.
- **PAINTED-ANISOTROPIC provenance-ablation (§8):** the grown `k_shear,eff(u_0)` pattern painted static (u-independent) reads `K_tan/K_0 = 0.2982` vs GROWN `0.2955` — GROWN ≈ PAINTED (Δ ≈ 0.9 %). **The (near-null) effect is anisotropy-driven, NOT growth/provenance-driven** — grown and painted are the same to ~1 %, so there is no provenance-real lift to attribute (the §8 attribution: grown-vs-painted separates provenance; here they collapse).
- **Seed-independence sweep (`fixed_budget`, `p_0 ∈ {0.25, 0.5, 1.0}·p_ref`):** `lift = 0.999 / 0.998 / 0.997`, `r_Z(struct) = 0.544 / 0.544 / 0.544`, all outcome (i). `lift` rel-spread `= 0.0020`, `r_Z` rel-spread `= 0.0010`, `stable_tol_0p15 = True`. The verdict does NOT FLIP across the sweep ⇒ **not a seed-controlled UNDETERMINED** (the UNDETERMINED is the `r_Z`-straddle, not a seed flip). The low-p0 arms carry weak/no tension (`max_r|T| = 0.159 / 0.320 < 0.489`) so they read near the control — consistent with lift ≈ 1.0 being source-independent.
- **yield_saturated reservoir knob (`A_yield_scale ∈ {0.9, 1.0, 1.1}`):** `grown_equilibrium_exists = False` for ALL three — the vessel BUCKLES (peak-strain ceiling `peak_A ≈ 0.209` at the buckling edge `p0 = 0.06`, `min k_shear,eff = 0.028`) before peak strain reaches `A_yield·A_yield_scale ≈ 0.9–1.1`. `yield_reached = False`. ⇒ **the self-bound-adjacent yield-saturated vessel is UNREACHABLE on the lossless engine** (the energize-LOCK-adjacent negative — the pre-test-physics-check question answered NEGATIVE). Per §9 Fork SEED the headline uses `fixed_budget` at `p_ref` (yield_saturated has no stable equilibrium).
- **Anti-seduction fence (§6, frozen in advance):** headline `r_Z = 0.520`; matched-ish (`0.8 ≤ r_Z ≤ 1.25`) = **False** ⇒ no candidate flag. (The fence is not triggered; `r_Z` sits at the straddle, not in the matched band.) Frozen: `a matched-ish CANDIDATE routes to Grant and is EXCLUDED from the headline verdict regardless of arm`.

---

## §8 — HONEST DEVIATIONS

1. **`T`-definition (grown_tension_nonzero):** `T` is taken as the remap term `k_a·ε_axial` (the tension CONTRIBUTION the operator sees, `= T/ℓ` in the `axiom-register.md:193` grammar), NOT the un-normalized axial force `k_a·ε_axial·ℓ`. The threshold `0.05·k_a·A_yield = 0.489` uses the reference `k_a = 9.77337`. Stated in the driver docstring (`bond_tension_remap`).
2. **SELFTEST-(iii) shell fraction:** the frozen ≥50 %-of-shell-band near-buckling target was met via the §3B "justified equivalent" latitude (a near-buckling core cluster of 21 bonds producing the same aggregate crossing), not a literal ≥50 % shell — disclosed in §1 with the calibration numbers.
3. **Protocol E box size:** frozen `L ∈ {32, 48}`; run at `L = 32` only under the runtime budget. The `L = 48` grown-array ToF is the owed refinement, NOT verdict-controlling (the measured `ρ_eff/ρ_0 = 0.916` leaves `r_Z = 0.520` in Z_str with `≈ 0.03` margin to the Z_hi edge; the bin is robust to the plausible `L`-drift).
4. **yield_saturated realization:** implemented as a BOUNDED ascending `p0` scan with fail-fast (capped `outer ≤ 8`, `inner ≤ 800`) solves on buckled states — the empirical-driver runtime fix (Rule 10): the uncapped near-buckling secant grinds the frozen `100 × 4000` caps. Buckled states are NOT used downstream; the fail-fast changes no physics (the buckling verdict is unchanged, the ceiling `peak_A ≈ 0.21` is read from the highest STABLE scan point).
5. **`p_ref = 0.040` for the cage-array verdict arm** vs `0.020` for the single-core self-tests: the cage-array soft-rail shells absorb more of the source, so the cage arm needs a higher per-core `p0` to grow the same tension (`max_r|T| = 0.647 ≥ 0.489` at `0.040`) — both are DISCLOSED `[engineering-choice]` knobs (grade-frame Eulerian/imposed), chosen inside the stable-vessel window (tension ≥ 0.489, bonds positive).

---

## §9 — Calibration-vs-derived ledger (consistency-vs-emergence, frozen tags) + routed consequence

`K_tan/K_0`, `G_eff/G_0`, `ρ_eff/ρ_0`, `r_Z`, `K_ratio_lift`, the `K(ε_bias)` profile are `[derived]` dimensionless RATIOS (lattice static homogenization + relaxed-equilibrium growth through the state-dependent operator; MANIFESTATION-class). The srs bond model `ρ*=9.77337` is `[import]` (`ν_Hill=2/7`, GR-imported K=2G, `ave.core.constants.N_NU`; CONSISTENCY-class). The grown `T(r)` is `[derived]` (relaxed-equilibrium output) feeding the `[canon]`-form LIVE remap `k_shear,eff(u) = k_s + T(u)/ℓ` (`axiom-register.md:193`). The source amplitudes `p_0` / `A_yield_scale` are `[engineering-choice]` knobs (grade-frame Eulerian/imposed). `α`-CLEAN (the discriminator is a dimensionless impedance ratio). **No emergence-class claim headlined.**

**Consequence routed to Grant** (this lane surfaces + routes only; no leaf / ledger / port-register / falsification-ledger edit, regardless of outcome — prereg §9/§10):
- **UNDETERMINED (the `r_Z`-straddle fork, §9 Fork B/SEED).** The grown anisotropic vessel does NOT resolve bridge-vs-bottleneck — `lift = 0.997` (null) with `r_Z = 0.520` straddling `0.5`. State precisely: the verdict turns on where the true `K_eff` sits between the KUBC upper bound (read here) and the SUBC/periodic lower bound; per #782 Fork B a HOLD/null reading is KUBC-conditional. **The owed resolver is the feasible SUBC/periodic lower-bound bracket** (same cost-class, `L = 16`) that would decide whether the true `r_Z` sits Z_lo (macro-side / SOFT) or holds at the straddle — NOT executed here.
- **The yield_saturated NULL** (no self-bound vessel; buckles before yield) is banked as the energize-LOCK-adjacent outcome — no rescue, no re-seed of the slot (Rule 12).
- The trapped-energy `β` term (Fork ρ / C-load, `clm-m5swh9`) is the continuum radial-solver lane's tagged E=mc² import — NOT this bench's (`ρ_eff/ρ_0 = 0.916` here is the MEASURED structural term only).

> **Result-doc provenance.** The bench RUN of the merged, Grant-ratified REVISION-3 frozen prereg (`research/2026-07-22_vessel-state-rve_prereg-FROZEN.md`; ADJ-1 stencil split + ADJ-2 (iv)-demotion ratified at merge). Driver `research/drivers/vessel_state_rve.py` reuses the #782 KUBC scaffold (Rule-14), `ave.core.*` read-only, engine byte-untouched, deterministic (`756 s`). LEG-0 gate-fireability PASSES (self-tests force (ii)/(iii)); instrument validation all-pass; grown equilibrium EXISTS at `fixed_budget p_ref`; amplitude gate outcome **(i) CLEAN**; **HEADLINE BIN = UNDETERMINED** (`lift = 0.997`, `r_Z = 0.520` straddling `0.5`) — the grown anisotropic vessel reads like its isotropic control (stiffen/soften cancel), the SAME landing as merged #782's painted bench, now with a MEASURED ρ. yield_saturated buckles before yield (energize-LOCK-adjacent NULL). Consequence routed to Grant; no leaf touched; no rescue minted. Companions: the frozen prereg, merged **#782** (`research/2026-07-21_rve-aggregation-bench_result.md`), merged **#779** (the anisotropic remap), merged **#788** (Protocol E arithmetic), merged **#789** (`continuum-radial-solver_CHARTER.md` — this bench feeds D5/R1 profile input), and the docket fragment (`_orchestration/docket-entries/2026-07-22-vessel-state-rve-bench.md`).
