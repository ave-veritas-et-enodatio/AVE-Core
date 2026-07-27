# Anisotropic Vessel-State RVE Bench — RESULT (walk-1 verdict run)

Prereg-file: research/2026-07-22_vessel-state-rve_prereg-FROZEN.md

**Date:** 2026-07-22
**Class:** DERIVATION + lattice-derived research-driver (research-doc; forms derived, values dimensionless/geometric; **mints no `clm-`/`def-`; propagates to no KB/tex leaf**). This is the **bench RUN** of the merged, Grant-ratified REVISION-3 frozen prereg — the "walk-1 instrument": does the GROWN vessel-state cage read HARD / SOFT / NULL / DISCORDANT / MARGINAL / UNDETERMINED?
**Driver:** `research/drivers/vessel_state_rve.py` (+ `research/drivers/vessel_state_rve_results.json`, `research/drivers/vessel_state_rve.png`). Figure: `research/drivers/vessel_state_rve_figure.py`.
**Engine:** `src/ave` **BYTE-UNTOUCHED** (imports read-only); Rule-14 reuse of the merged #782 KUBC static-homogenization scaffold (`research/drivers/rve_aggregation_bench.py` + `constituent_cage_ensemble.py`); the NEW piece is the STATE-DEPENDENT geometric-stiffness operator `k_shear,eff(u) = k_s + k_a·ε_axial(u)` (`axiom-register.md:193`) + the frozen Newton/self-consistent solve.
**Every number below is read from the shipped `vessel_state_rve_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson NAMED).** All `[canon]` inputs content-verified at base HEAD `f050e33b`: `axiom-register.md:193` (the load-response sign rule), `electron-bh-isomorphism.md:26`, `master-equation.md:20`, `ave.core.constants.N_NU`. Deterministic (`run_c2_speeds seed=1`; no per-step RNG in the statics); total runtime `1049 s`.

> **★REVISION (2026-07-22, post-review — PR#796 adversarial-review repairs, PRE-MERGE, disclosed).** This result doc is REVISED from its first-run form to answer the PR#796 review (15 confirmed findings). The re-bank is results-repair-under-review, pre-merge, disclosed — nothing was banked to canon (the frozen prereg is byte-untouched; the driver/JSON were repaired and re-run). The load-bearing corrections: **(F2)** Protocol E was re-implemented per the frozen §4 sub-requirements (PML/window exclusion, density-peak top-K sampling, the frozen reflection-free window, a FROZEN cross-correlation arrival criterion, a REAL reactance-pair flag) and RUN at BOTH `L∈{32,48}` — the ρ-side is now MEASURED with those guards, and the finding is that the ToF is **method-indeterminate on the grown scatterer** (below); the shipped "clean measured `r_Z = 0.520`" is **RETRACTED**. **(F6)** the "hoop-vs-radial CANCELLATION" mechanism headline is **RETRACTED** (the cheapest ablation refutes it — below). **(F11)** the `yield_saturated` NULL is re-graded from an *extrapolated* to an *OBSERVED* buckling-onset, instrument-scoped. **(F1/F4/F5/F7/F9/F10/F14)** the Leg-0 (iii) claim narrowed, the calibration string regenerated to computed truth, the determinism gate upgraded to a two-full-runs digest, the σ-knob ledgered + tested, deviations §8 completed, the F7 design-lesson recorded. **The HEADLINE BIN is UNCHANGED (UNDETERMINED) but its BASIS is repaired** — it now rests on the structural-ρ anchor (`r_Z = √K_ratio = 0.5436`, Z_str) with the ToF ρ-correction disclosed as non-decisive, NOT on a clean measured `0.520`. No old bin is defended: the bin is re-derived from the frozen table on the repaired numbers.

**★THE CARVE (mandatory disclosure — every output carries both strings, prereg §1; both present in JSON `provenance`):**
- `grade-frame: Eulerian, imposed (not self-bound; the engine hosts no field-generated co-moving grade)`
- `source imposed (radiation-stress surrogate body-force ∝⟨A²⟩); stress state emergent through the nonlinear force balance`

**★THE S(A(u)) DECISION honoured (prereg §0):** the Op14 saturation grade `S(A)` is IMPOSED (Eulerian, static); the ONLY state-dependence in the operator is the LIVE geometric-tension term `T(u)/ℓ = k_a·ε_axial(u)`. Scope-limit disclosed: `kernel-knee physics (the Op14 S(A) saturation marginality) is NOT hosted`; the buckling/marginality physics is carried by the `T(u)` geometric term per #779.

---

## ★BOTTOM LINE

The walk-1 instrument is **VALIDATED, not VOID** — `gate_fireability_selftest_pass = True` and every instrument-validation gate passes. The grown vessel-state cage reads:

> ## HEADLINE BIN = **UNDETERMINED** (cell `(i) × L1 × Z_str`)
>
> `K_ratio_lift = 0.997` (band L1: `< 1.2`), `r_Z = 0.5436` (structural anchor `√K_ratio`; band Z_str: `|r_Z − 0.5| = 0.044 ≤ δ_rZ = 0.05`), amplitude gate = **outcome (i) CLEAN** (`A_sign = 0.0020`, `amp_spread± = 0.00097 / 0.00113`, converged + robust). Headline arm = `fixed_budget` (yield_saturated has **no stable equilibrium** — it BUCKLES before yield). **The Protocol E ToF ρ-correction is method-indeterminate on the grown scatterer (below) and does NOT move the bin off the structural anchor.**

**The physics headline (repaired).** At the small-signal-tangent regime the regime-ruling names (`.OP` to the grown equilibrium, then a second-difference tangent probe `≪` every nonlinear scale), the grown pressure-vessel stress state does **NOT** compose into a load-bearing bridge (HARD) NOR a pressure-release bottleneck (SOFT) at the aggregation level: **`K_ratio_lift = 0.997` — the grown vessel's small-signal tangent modulus is indistinguishable from its isotropic control** (`K_tan/K_0 = 0.29548` grown vs control `0.29637`). The shipped decomposition attributes this null to the **live-operator / provenance channel** (GROWN ≈ PAINTED ≈ isotropic control, all within ~1 %), **NOT to a hoop-stiffen-vs-radial-soften cancellation** — the cheapest ablation refutes that mechanism (§7, F6): with a core-restricted energy the "radial-soften" pattern does **not** soften the core tangent (it raises it `+0.43 %`); both named components STIFFEN. This lands the SAME BIN as merged #782's painted-isotropic bench (UNDETERMINED), now confirmed on the GROWN anisotropic vessel. The impedance `r_Z` is the structural anchor `√K_ratio = 0.5436` (straddling `0.5`); the Protocol E ToF ρ-correction is **method-indeterminate on these box sizes** — the cold reference validates against the Bloch speed (rel `1 %` at L=32) but the grown cage-array is such a strong scatterer that the ToF returns an **unphysical `c_eff > c_0`** (the softer grown medium appearing FASTER than cold) and the self-consistent iteration **DIVERGES** (`0.519 → 0.701 → 1.499`), so no reliable `ρ_eff` is extractable (§6). The yield-saturated (self-bound-adjacent) arm is **unreachable on the lossless engine** — the vessel BUCKLES at an OBSERVED onset `p0 ≈ 0.062` (`min k_shear,eff = −0.0028 < 0`), before peak strain reaches `A_yield = 1.0` (the energize-LOCK-adjacent negative surfaced by the pre-test-physics-check). **Consequence routed to Grant** (§9): UNDETERMINED at the `r_Z` straddle; the owed resolver is the feasible SUBC/periodic lower-bound bracket (#782 Fork B), NOT run here — and the ToF's inability to tighten the ρ-side REINFORCES that a static bound (not a ToF) is what's needed.

---

## §1 — LEG 0: the gate-fireability self-tests (the mandatory VOID gate — §3B)

Frozen: `gate_fireability_selftest_pass = SELFTEST-(ii) fires (ii) AND SELFTEST-(iii) fires (iii), each with the correct convergence/robustness flags` → **True.** (JSON `leg0_selftests`.)

**SELFTEST-(ii) FIRES (ii)** — a deliberately under-converged solve forces the artifact AND is diagnosed as convergence-caused. At the FROZEN loose inner CG tol `1e-3`: `amp_spread± = 649.24 / 648.96` (> 0.05, fires the artifact), `A_sign = 0.0300` (≤ 0.10, symmetric drift) AND `all_scan_legs_converged = False` (diagnosed convergence-caused); at the tight tol `1e-10`: `amp_spread± = 0.00583 / 0.00427` (≤ 0.05 both signs, removed by tightening). The dual frozen assertion holds. **No calibration latitude was needed for (ii)** — the frozen `1e-3` was shipped UNCHANGED and forced the artifact (the calibration-disclosure string is regenerated to this computed truth — F4/F15).

**SELFTEST-(iii) FIRES (iii) — fireability-in-extremis (claim narrowed, F1).** A near-buckling grown state forces sign-asymmetric squeeze-softening. Gate returns `outcome (iii)`: `amp_spread+ = 568.74` (> 0.05), `A_sign = 568.77` (> 0.10), `K_tan_minus(ε_max) = 7484.3 < K_tan_plus(ε_max) = 4.43e6` (squeeze-softening direction), with `all_scan_legs_converged = True AND residual_tightening_robust = True`. **★HONEST SCOPE (F1 narrowing):** this firing meets the frozen (iii) acceptance LITERALLY (the one-sign clause), but it demonstrates **fireability-in-extremis** — a localized stretch-side curvature divergence at a tight near-buckling core cluster — NOT a threshold-scale aggregate squeeze-softening. The demonstrated dynamic range is `0.002 ↔ 568` with nothing between: the gate is shown to be capable of firing (iii), which is what §3B requires, but the fired magnitude is a divergence, not a graded aggregate signal. The (iii) self-test VALIDATES the gate is not a checklist; it does NOT establish threshold-scale detectability of graded compressive marginality.

**★DISCLOSED calibration (design-time numeric-confirmation run, banked here per §3B, made BEFORE any verdict arm).** The frozen ≥50 %-of-shell-band near-buckling target was NOT literally met — the Gaussian core source concentrates the near-buckling bonds into a tight CORE CLUSTER (achieved fraction in the calibrated shell band = `0.0156`; `min k_shear,eff = 0.0541` at the self-test operating point `p0 = 0.028`, σ = 2.5). Per the frozen §3B latitude (*"a justified equivalent may be substituted at calibration time IF it produces the same aggregate crossing — disclosed"*) the near-buckling core cluster IS that justified equivalent: it produces the frozen SELFTEST-(iii) acceptance (converged + robust outcome (iii), `A_sign = 568.77`). All calibration numbers are read from JSON `leg0_selftests.calibration_disclosure` + `leg0_selftests.selftest_iii` — the line-9 no-prose-numbers rule applied to the doc's own calibration story (F1): the earlier prose-only figures ("best any-band ≈ 0.05", "0.44 / −0.033 shell-shaped source") are DELETED here; the driver ships only the achieved fraction (`0.0156`) and the fired metrics.

---

## §2 — LEG 0: instrument validation (§7 standard gates) — all PASS

| gate | reading | verdict |
|---|---|---|
| uniform-medium NULL | `K_tan/K_0 = 1.0000`, `ρ_N = 0`, `r_Z = 1.0000` | PASS (r_Z→1, ρ_N→0 on a uniform cold medium) |
| determinism (two full runs) | two independent full driver runs → **identical `determinism_digest = 69968227…`** (`diff -q` clean on the timing-stripped results) | PASS (see F5/F13 below + §8.8) |
| Lamé exterior gate | exterior `∇·u`/interior `∇·u` = `0.0358` ≤ 0.10 | PASS (carried from #782 §4 Leg 2) |
| RVE-size gap | `K_eff/K_0 = 0.280 (L12) / 0.296 (L16) / 0.294 (L20)`; `gap(L16,L20) = 0.0072` ≤ 0.15 | PASS (size-converged) |
| STOP-gate class | rail `K_eff/K_0 = 0.296` (< 1, SOFTENS) vs rigid `1.583` (> 1, STIFFENS) — opposite sign | PASS |
| Bloch cross-check (§8, F14) | cold ToF vs `run_c2_speeds`: `c_P` rel `= 0.011` ✓, `c_S` rel `= 0.188` ✓ (both ≤ 0.20, advisory) | PASS (the repaired ToF recovers the Bloch speeds on a UNIFORM medium) |
| cell-walk partition | 12 rows, exhaustive + disjoint | PASS (`assert_partition`) |

Instrument cross-check against merged #782: the cold bulk-only cage at `φ_sf = 0.489` reproduces #782's `K_eff/K_0 = 0.296` (isotropic control = `0.29637`) — the instrument agrees with the merged linear bench at the cold limit.

**★The Bloch cross-check (F14) is the load-bearing sanity check on the repaired Protocol E ToF:** the cold uncaged P/S pulse ToF speeds (the repaired `_pe_pulse_xcorr`, L=20) match the Bloch `c_P`/`c_S` from `run_c2_speeds` to `1.1 % / 18.8 %`. The ToF instrument is therefore SOUND on a uniform medium — which is exactly why its FAILURE on the grown cage-array scatterer (§6) is a physical finding about the medium, not a broken instrument.

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

- amplitude gate (hydrostatic mode → `K_eff`) = **outcome (i)**: Frozen: `amp_spread ≤ 0.05 for BOTH signs` — `amp_spread± = 0.00097 / 0.00113`, `A_sign = 0.0020`, converged + robust ⇒ a clean small-signal tangent modulus. NOT (ii), NOT (iii), NOT the (iv)-anomaly.
- `K_tan/K_0 (grown) = 0.29548`; isotropic control `= 0.29637`; **`K_ratio_lift = 0.997`** (band L1: `< 1.2`).
- `G_tan/G_0 (grown) = 0.634` (shear, corroborative).
- `r_Z = 0.5436` — the **structural anchor** `√(K_tan/K_0)` (ρ_eff/ρ_0 ≡ 1, the long-λ k→0 limit for uniform point masses) → band **Z_str** (`|r_Z − 0.5| = 0.044 ≤ δ_rZ = 0.05`; straddles 0.5). **The Protocol E ToF ρ-correction (§6) is method-indeterminate and does NOT override this anchor** (the driver's `rz_decider = structural_anchor (ToF method-indeterminate/size-flip)`).
- **cell-walk bin = UNDETERMINED** (walked MECHANICALLY through the frozen 12-row table: gate (i) → `(L1, Z_str)` → UNDETERMINED). Data + code path: JSON `verdict.fixed_budget_headline`; `vessel_state_rve.py::cell_walk_bin` (+ `assert_partition` proof).

The FOUR headline bins are excluded by the frozen definitions: not HARD (`lift >= 1.5` fails — lift 0.997); not SOFT (`r_Z_grown < 0.5 − δ_rZ` fails on the anchor — 0.5436 not < 0.45); not NULL (`r_Z_grown > 0.5 + δ_rZ` fails — 0.5436 not > 0.55); not DISCORDANT (lift < 1.5); not MARGINAL (gate (i), not (iii)). The verdict sits in the UNDETERMINED zone precisely because the anchor impedance straddles `0.5` while the lift is null AND the ToF cannot tighten the ρ-side.

---

## §5 — C-V profile (§5) — REWIRED to the live geometric term

Frozen: `K(ε_bias) profile curve + its reconstruction read: shell POSITION, WIDTH, and ASYMMETRY`.
- shell POSITION = `0.00135`; shell WIDTH = `0.006` (squeeze `0.0042` / stretch `0.0018`).
- shell ASYMMETRY = `−0.400`. Frozen: `|ASYMMETRY| >= 0.15 confirms the anisotropic vessel state`; `|ASYMMETRY| = 0.400 ≥ 0.15` ⇒ the reconstruction flags the anisotropic vessel state.
- `span_truncated = False`. `K(ε_bias=0) = 2079.2` (unbiased grown OP normalizer).
- **★HONEST READ (corroborative-only, per the frozen demoted clause).** The `K(ε_bias)` curve is **nearly FLAT** — it varies monotonically from `2079.82` (`ε_bias = −3e-3`) to `2078.59` (`ε_bias = +3e-3`), a **total variation of `0.059 %`** across the full bias span. The reconstruction (POSITION/WIDTH/ASYMMETRY) therefore reads the tiny residual monotonic slope's off-centre-ness, not a resolved depletion-edge shell feature; the `|ASYMMETRY| ≥ 0.15` flag is **corroborative-only** (the prereg's demoted clause, "meaningful ONLY on the v2 nonlinear instrument"), consistent with the headline: the grown state IS anisotropic (hoop-tension vs radial-compression), but that anisotropy barely modulates the bulk tangent (`< 0.06 %` over the bias range) — the same null lift the ablation (§7) attributes to the provenance/live-operator channel, not a cancellation. Data + code path: JSON `verdict.cv_profile_fixed_budget`; `vessel_state_rve.py::cv_profile`.

---

## §6 — Protocol E: ρ_eff MEASURED alongside K_eff (§4) — REPAIRED per the frozen §4 (F2)

Frozen: `Protocol E measures the STRUCTURAL ρ term only; the engine hosts no trapped-energy inertia (C-load open, clm-m5swh9); NO β claim from this bench`.

**The frozen §4 sub-requirements are now implemented AS WRITTEN (the F2 repair — the shipped extraction was under-guarded):**
- **PML/window boundary-cell exclusion** — all top-K field-density extractions filter `pml_thickness ≤ {i,j,k} ≤ N − pml_thickness − 1` (here: nodes within `pml_thickness = 2.0` of any face) BEFORE any `argpartition`.
- **Density-peak (top-K |field|²) sampling** — the pulse is sampled at energy-density peaks (top-K = 48 `|field|²` nodes per monitor slab), NOT a slab-mean.
- **The FROZEN reflection-free window** — Frozen: `t_end ≤ 0.9·(L/2 − r_meas)/c_P` (source at box CENTER; `r_meas` = the far density-peak monitor). The shipped window exceeded this by `~12×`.
- **A FROZEN arrival criterion (documented)** — a two-monitor **cross-correlation transit-time** (parabolic sub-step interpolated, positive-lag constrained) between two density-peak monitors, launched as a coherent rightward compression pulse. Two coherent extractions are frozen and shipped as a method-band: (a) launch@`c_P` one-shot (the fast coherent FRONT = the prereg's "first-arrival group speed"); (b) SC-coherent (the self-consistent forward-eigenmode group speed). This REPLACES the shipped unfrozen argmax-of-slab-mean.
- **A REAL reactance-pair flag** — the C-state (compression amplitude) AND L-state (kinetic flux) are recorded at EVERY step over the frozen window; `reactance_pair_recorded = True` is now a genuine both-non-trivial check with distinct peak steps (`C_peak_step = 110`, `L_peak_step = 21` at L=32 — a genuine reactive C↔L exchange, not a one-phase snapshot), not a hardcoded `True`.
- **BOTH `L ∈ {32, 48}`** — run at both (the shipped run was L=32 only).

**★THE FINDING — the ToF is method-indeterminate on the grown scatterer (retracts the shipped clean `r_Z = 0.520`).**

| | cold `c_0` (Bloch rel) | grown `c_eff` | `c_0/c_eff` | `ρ_eff/ρ_0` | `r_Z` | bin |
|---|---|---|---|---|---|---|
| **L=32 launch@c_P** | `0.5133` (rel `0.011`) | `0.7005` | `0.733` | `0.159` | `0.2165` | Z_lo |
| **L=32 SC-coherent** | `0.5101` | `1.499` (**diverges** `0.52→0.70→1.50`) | `0.340` | `0.034` | `0.1005` | Z_lo |
| **L=48 launch@c_P** | `0.4372` (rel `0.157`) | `0.6543` | `0.668` | `0.132` | `0.1975` | Z_lo |
| **structural anchor** | — | — | — | `≡ 1` | `0.5436` | Z_str |

- The cold reference `c_0` is Bloch-VALIDATED (rel `1.1 %` at L=32) — the instrument is sound on a uniform medium.
- The grown `c_eff` is **UNPHYSICAL**: `c_eff = 0.70 > c_0 = 0.51` — the SOFTER grown medium (`K_tan/K_0 = 0.2955 < 1`, expected `c_eff ≈ √0.2955·c_0 ≈ 0.28`) appears FASTER than cold — and the self-consistent iteration **DIVERGES** (`0.519 → 0.701 → 1.499`) rather than converging. The grown cage-array (soft-shell inclusions, marginal-λ `k·r_core ≈ 2–4` on L∈{32,48}) is a strong LOCALLY-RESONANT SCATTERER; the compression pulse does NOT propagate coherently, so the cross-correlation transit-time is not a physical group speed.
- **method_indeterminate = True** — the r_Z band `[0.10, 0.54]` straddles `Z_lo` (SOFT) and `Z_str` (UNDETERMINED); the raw launch@`c_P` bins read SOFT at both L, but they rest on the unphysical `c_eff > c_0`. **The ρ-correction is therefore REJECTED as non-decisive; the bin rests on the structural anchor** `r_Z = √K_ratio = 0.5436` (Z_str). Driver: `rz_decider = structural_anchor (ToF method-indeterminate/size-flip)`.

**★DISCLOSED engineering choice (F2):** the ToF-medium is grown with a fail-fast capped solve (`outer ≤ 12`, `inner_tol = 1e-6`) — the ToF medium is a homogenized TANGENT operator, verified insensitive to the last outer/inner digits (`L=32` capped `min k_shear,eff = 0.34722` IDENTICAL to the frozen full `1e-10/100-outer` solve); the VERDICT K_tan solve keeps the frozen `1e-10`. This makes the `L=48` grow feasible (`~86 s`) without changing the grown operator.

**★Consequence (routed to Grant, §9):** the ToF cannot tighten the ρ-side on L∈{32,48}; the verdict is UNDETERMINED on the structural anchor. This REINFORCES the routed resolver — a STATIC SUBC/periodic lower-bound bracket (#782 Fork B), NOT a ToF, is what decides whether the true `r_Z` sits Z_lo (SOFT) or holds at the straddle. Data + code path: JSON `verdict.fixed_budget_headline.protocol_E`; `vessel_state_rve.py::protocol_E`.

---

## §7 — percolation / painted-anisotropic / ABLATION / seed-independence / yield_saturated / σ-variant / anti-seduction

- **Percolation sub-check (§6, corroborative):** `hoop_percolates = False`, `largest_tense_cluster_frac = 9.2e-5` (`n_tense_bonds = 489`) — the grown tensile (hoop) bonds do NOT form a face-to-face spanning cluster ⇒ corroborates SOFT/NULL (patchy tension islands, not a closed hoop-tense shell), NOT HARD.
- **PAINTED-ANISOTROPIC provenance-ablation (§8):** the grown `k_shear,eff(u_0)` pattern painted static (u-independent) reads `K_tan/K_0 = 0.29824` vs GROWN `0.29548` — GROWN ≈ PAINTED (Δ ≈ 0.9 %). **The (near-null) effect is anisotropy-driven, NOT growth/provenance-driven** at the grown-vs-painted level — grown and painted collapse to ~1 %.
- **★ABLATION DECOMPOSITION (F6 — the "cancellation"-mechanism REFUTATION, JSON-shipped).** The retracted headline claimed the null lift is a hoop-stiffen ⊕ radial-soften CANCELLATION. That mechanism predicts `hoop_only > control AND radial_only < control` (one stiffens, one softens, cancelling to ≈ control). The cheapest ablation — paint ONLY the tensile-bond remap (radial bonds reset cold) vs ONLY the compressive-bond remap (hoop bonds reset cold), each measured core-restricted vs the isotropic control — REFUTES it:
  - `K_tan/K_0`: control `0.29637`, full-painted `0.29824`, **hoop_only `0.29696` (`+0.200 %` vs control)**, **radial_only `0.29764` (`+0.429 %` vs control)**.
  - `radial_only_softens_core_tangent = False`; `cancellation_mechanism_supported = False`. The "radial-soften" pattern does NOT soften the core tangent — it RAISES it `+0.43 %`. **BOTH named components STIFFEN.** ⇒ **the null lift (`≈ 1.0`) is provenance/live-operator-driven (grown ≈ painted ≈ isotropic control), NOT a hoop-vs-radial cancellation.** Data: JSON `verdict.ablation_decomposition_fixed_budget`; `vessel_state_rve.py::ablation_decomposition`.
- **Seed-independence sweep (`fixed_budget`, `p_0 ∈ {0.25, 0.5, 1.0}·p_ref`):** `lift = 0.999 / 0.998 / 0.997`, `r_Z(struct) = 0.5441 / 0.5439 / 0.5436`, all outcome (i). `lift` rel-spread `= 0.0020`, `r_Z` rel-spread `= 0.0010`, `stable_tol_0p15 = True` ⇒ **not a seed-controlled UNDETERMINED** (the UNDETERMINED is the `r_Z`-straddle, not a seed flip). The low-p0 arms carry weak/no tension (`max_r|T| = 0.159 / 0.320 < 0.489`) so they read near the control — consistent with lift ≈ 1.0 being source-independent.
- **yield_saturated reservoir knob (`A_yield_scale ∈ {0.9, 1.0, 1.1}`) — re-graded to OBSERVED buckling onset (F11/F3/F8).** The shipped scan stopped at an undisclosed hard-coded `p0 = 0.06` ceiling with every point STABLE, and banked yield_saturated as an *extrapolated* NULL. The scan is now EXTENDED past the ceiling and OBSERVES the terminal state: `grown_equilibrium_exists = False` for all three; the highest STABLE point is `p0 = 0.06` (`peak_A_ceiling = 0.2087`), and the FIRST non-stable point is the **OBSERVED buckling onset `p0 = 0.062`** with `min k_shear,eff = −0.0028 ≤ 0` (physical buckling, classified `buckled`, not a converged=False (ii)-stall). ⇒ **yield UNREACHED within the scanned amplitude range; near-buckling trend CONFIRMED by the observed buckling onset at `p0 = 0.062`; INSTRUMENT-SCOPED** (this source family σ = 1.6, this affine radiation-stress surrogate, this cage geometry `φ_sf = 0.489`) — NOT an engine-level unreachability claim (F8's scope carve). The energize-LOCK-adjacent negative — the pre-test-physics-check question answered NEGATIVE, now with a MEASURED onset rather than an extrapolation. Data: JSON `verdict.yield_saturated_reservoir_knob.*.yield_scan`.
- **★σ-variant arm (F10/F14 — VERDICT_SRC_SIGMA ledgered + tested).** `VERDICT_SRC_SIGMA = 1.6` is a DISCLOSED `[engineering-choice]` per-core source width (differing from the single-core calibrated `2.5`), now on the engineering-choice ledger. A σ-variant verdict arm at `σ = 2.5`: `K_tan/K_0 = 0.29554`, `lift = 0.9972`, `r_Z(struct) = 0.5436`, gate (i) → bin `UNDETERMINED`. `verdict_relevant_flip = False` — the headline bin is σ-INSENSITIVE. Data: JSON `verdict.sigma_variant_arm`.
- **Anti-seduction fence (§6, frozen in advance):** headline `r_Z = 0.5436`; matched-ish (`0.8 ≤ r_Z ≤ 1.25`) = **False** ⇒ no candidate flag.

---

## §8 — HONEST DEVIATIONS (completed per F14)

1. **`T`-definition (grown_tension_nonzero):** `T` is taken as the remap term `k_a·ε_axial` (`= T/ℓ` in the `axiom-register.md:193` grammar), NOT the un-normalized axial force `k_a·ε_axial·ℓ`. Threshold `0.05·k_a·A_yield = 0.489` uses `k_a = 9.77337`. Stated in the driver docstring (`bond_tension_remap`).
2. **SELFTEST-(iii) shell fraction + scope:** the frozen ≥50 %-of-shell-band target was met via the §3B "justified equivalent" latitude (a near-buckling core cluster, achieved fraction `0.0156`) — disclosed in §1; the (iii) firing is scoped to fireability-in-extremis (F1), not threshold-scale aggregate detectability.
3. **Protocol E method (F2):** the frozen §4 sub-requirements are implemented as written and RUN at BOTH `L ∈ {32, 48}`; the arrival criterion is a documented two-monitor cross-correlation transit-time (launch@c_P "first-arrival" + SC-coherent band). The ToF-medium grow uses a capped solve (`outer ≤ 12`, `inner 1e-6`; verified identical grown OP; the VERDICT K_tan keeps `1e-10`). The grown-medium ToF is method-indeterminate (§6); the ρ-correction is non-decisive and the bin rests on the structural anchor.
4. **yield_saturated realization (F9):** implemented as a BOUNDED ascending `p0` scan (`YIELD_SCAN_P0` = `[0.005 … 0.08]`, extended past the ceiling) with a fail-fast cap (`outer ≤ 8`, `inner ≤ 800`) applied UNCONDITIONALLY to EVERY yield-scan solve (NOT only buckled ones — the §8.4 mis-description is corrected). A converged=False onset with bonds still positive would route to (ii)-artifact per §2; the OBSERVED onset (`p0 = 0.062`) is a physical `buckled` (`min k_shear,eff ≤ 0`). Capped-vs-uncapped confirmation at the onset: re-solving at `2×` the fail-fast cap (`outer ≤ 16`, `inner ≤ 1600`) leaves the classification UNCHANGED (`buckled`, `min k_shear,eff = −0.0028`, `classification_unchanged = True`) — more iterations do not rescue the buckled state (the full frozen `100×4000` is NOT used: a non-SPD buckled state makes the inner CG non-convergent and would grind, the pathology the fail-fast cap avoids, Rule 10). Data: JSON `yield_scan.capped_vs_uncapped`.
5. **`p_ref = 0.040` cage-array knob + `VERDICT_SRC_SIGMA = 1.6`** (F10): both DISCLOSED `[engineering-choice]` knobs (grade-frame Eulerian/imposed), on the ledger; the σ-variant arm (§7) tests σ-verdict-relevance (no flip).
6. **Bloch cross-check (F14):** the frozen §8 internal validation (cold `K_0`/`G_0` vs Bloch `c_P`/`c_S`, rel ≤ 0.20) — never run before — now RUNS: cold P/S ToF vs `run_c2_speeds`, rel `0.011 / 0.188` (both pass, advisory). §2.
7. **Grown-K_tan single-size caveat (F14):** the RVE-size gap gate (§2) ran on the COLD linear cage (L∈{12,16,20}); the GROWN-`K_tan` lift + amplitude gate were read on the L=16 cage only (the verdict arm). The seed-independence + σ-variant + painted + ablation arms corroborate the null lift is source/provenance-robust, but a grown-`K_tan` RVE-size gap (e.g. a grown L=20 arm) is NOT run here — the grown lift is a single-size read. Disclosed.
8. **Determinism two-full-runs (F5/F13):** the shipped `determinism` gate bit-compared two IN-PROCESS grow calls (a PROXY, relabelled as such in the JSON). The FROZEN criterion — two independent full driver runs Frozen: `reruns BIT-IDENTICAL` (`diff -q` clean) — is now satisfied by a `determinism_digest` (a SHA-256 over the results minus timing): two independent full driver runs produced the IDENTICAL digest `69968227e455137f…`, i.e. `diff -q` clean on the timing-stripped results. The earlier in-process substitution is disclosed.

---

## §9 — Calibration-vs-derived ledger (consistency-vs-emergence, frozen tags) + routed consequence + F7 design-lesson

`K_tan/K_0`, `G_eff/G_0`, `ρ_eff/ρ_0`, `r_Z`, `K_ratio_lift`, the `K(ε_bias)` profile are `[derived]` dimensionless RATIOS (lattice static homogenization + relaxed-equilibrium growth through the state-dependent operator; MANIFESTATION-class). The srs bond model `ρ*=9.77337` is `[import]` (`ν_Hill=2/7`, GR-imported K=2G, `ave.core.constants.N_NU`; CONSISTENCY-class). The grown `T(r)` is `[derived]` (relaxed-equilibrium output) feeding the `[canon]`-form LIVE remap `k_shear,eff(u) = k_s + T(u)/ℓ` (`axiom-register.md:193`). The source amplitudes `p_0` / `A_yield_scale` / the source width `VERDICT_SRC_SIGMA` are `[engineering-choice]` knobs (grade-frame Eulerian/imposed). `α`-CLEAN (the discriminator is a dimensionless impedance ratio). **No emergence-class claim headlined.**

**Consequence routed to Grant** (this lane surfaces + routes only; no leaf / ledger / port-register / falsification-ledger edit, regardless of outcome — prereg §9/§10):
- **UNDETERMINED (the `r_Z`-straddle fork, §9 Fork B/SEED).** The grown anisotropic vessel does NOT resolve bridge-vs-bottleneck — `lift = 0.997` (null) with the structural anchor `r_Z = 0.5436` straddling `0.5`, and the Protocol E ToF ρ-correction method-indeterminate (§6). **The owed resolver is the feasible SUBC/periodic lower-bound bracket** (same cost-class, `L = 16`) that would decide whether the true `r_Z` sits Z_lo (macro-side / SOFT) or holds at the straddle — NOT executed here. The ToF's failure on the grown scatterer STRENGTHENS the case for a STATIC bound over a dynamic ToF.
- **The yield_saturated NULL** (no self-bound vessel; buckles at the OBSERVED onset `p0 = 0.062`, `min k_shear,eff = −0.0028`) is banked as the energize-LOCK-adjacent outcome, INSTRUMENT-SCOPED — no rescue, no re-seed of the slot (Rule 12).
- The trapped-energy `β` term (Fork ρ / C-load, `clm-m5swh9`) is the continuum radial-solver lane's tagged E=mc² import — NOT this bench's.

**★F7 DESIGN-LESSON (dated note, carried forward — NO post-hoc re-banding here).** The frozen band placement made a clean NULL/SOFT verdict UNREACHABLE for a null-effect vessel of this outcome class: the #782 baseline `r_Z(β=0) ≈ 0.544` sits INSIDE the Z_str straddle band, so any bin OTHER than UNDETERMINED required the grown ρ-correction to shift `r_Z` OUTSIDE the straddle — which (a) is the scoped-bubble-sign direction and (b) turned out to depend on a ToF the grown scatterer defeats. A null-lift vessel with a structural `r_Z` inside the straddle can ONLY read UNDETERMINED absent a decisive ρ measurement. **The follow-on SUBC-bracket prereg MUST place its bands so every outcome class (HARD/SOFT/NULL/UNDETERMINED) has a reachable bin** (e.g. band the SUBC lower bound and the KUBC upper bound as the discriminator, not a single-point `r_Z` against a straddle that the baseline already occupies). This run is NOT re-banded post-hoc — the frozen table decides on the repaired numbers; the lesson is recorded for the next prereg.

> **Result-doc provenance.** The bench RUN of the merged, Grant-ratified REVISION-3 frozen prereg (`research/2026-07-22_vessel-state-rve_prereg-FROZEN.md`; ADJ-1 stencil split + ADJ-2 (iv)-demotion ratified at merge), REVISED 2026-07-22 to answer the PR#796 adversarial review (15 confirmed findings; repairs live in the driver/result/JSON — the frozen prereg is BYTE-UNTOUCHED). Driver `research/drivers/vessel_state_rve.py` reuses the #782 KUBC scaffold (Rule-14), `ave.core.*` read-only, engine byte-untouched, deterministic (`1049 s`; two-full-runs digest `69968227…`). LEG-0 gate-fireability PASSES (self-tests force (ii)/(iii); (iii) scoped to fireability-in-extremis); instrument validation all-pass (+ Bloch cross-check); grown equilibrium EXISTS at `fixed_budget p_ref`; amplitude gate outcome **(i) CLEAN**; **HEADLINE BIN = UNDETERMINED** (`lift = 0.997`, structural anchor `r_Z = 0.5436` straddling `0.5`; the Protocol E ToF ρ-correction method-indeterminate on the grown scatterer, cold Bloch-validated) — the grown anisotropic vessel reads like its isotropic control (the null lift attributed by the ablation to the provenance/live-operator channel, NOT a hoop-vs-radial cancellation). yield_saturated buckles at the OBSERVED onset `p0 = 0.062` (energize-LOCK-adjacent NULL, instrument-scoped). Consequence routed to Grant; no leaf touched; no rescue minted. Companions: the frozen prereg, merged **#782** (`research/2026-07-21_rve-aggregation-bench_result.md`), merged **#779** (the anisotropic remap), merged **#788** (Protocol E arithmetic), merged **#789** (`continuum-radial-solver_CHARTER.md` — this bench feeds D5/R1 profile input), and the docket fragment (`_orchestration/docket-entries/2026-07-22-vessel-state-rve-bench.md`).
