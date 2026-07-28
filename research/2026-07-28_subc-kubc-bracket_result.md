# SUBC/KUBC Bracket — RESULT (OWED-1: `K` bounded on BOTH sides, not one)

Prereg-file: research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md

**Date:** 2026-07-28
**Class:** DERIVATION + lattice-derived research-driver (research-doc; forms derived, values dimensionless/geometric; **mints no `clm-`/`def-`; propagates to no KB/tex leaf**). This is the bench RUN of the frozen prereg committed and pushed ALONE at `1288e288`.
**Driver:** `research/drivers/subc_kubc_bracket.py` (+ `research/drivers/subc_kubc_bracket_results.json`, `research/drivers/subc_kubc_bracket.png`).
**Engine:** `src/ave` **BYTE-UNTOUCHED** (imports read-only). Rule-14 reuse of the merged #782 KUBC scaffold (`research/drivers/rve_aggregation_bench.py`) and the merged #796 state-dependent grow (`research/drivers/vessel_state_rve.py`). The NEW piece is the SUBC (uniform-traction, pure-Neumann) primitive: the discrete traction load set, the Hill-lemma macroscopic-stress identification, the active-node restriction and the translation-only null-space projection.
**Every number below is read from the shipped `subc_kubc_bracket_results.json` via the deterministic driver — NO prose-string conclusions (the #770 lesson NAMED).** Deterministic; shipped run `346.0 s`; `determinism_digest = c5fe89f5a95acbc7…`.

**★WHICH MODULUS THIS `K` IS — stated once here and repeated at every headline.** The frozen §1.2 fixes both ends of the hydrostatic mode to the pure dilatational response (`E = ε·I` ⇒ `dev E = 0`; `Σ = σ·I` ⇒ `dev Σ = 0`), so the bracketed modulus is the **BULK modulus `K`** — **NOT** any longitudinal modulus that a normal-incidence impedance `Z = ρc_P` carries, and **NOT** Young's `E`. The `T2` companion mode is the pure deviatoric shear constant, which on this lattice is specifically **`C44`** (the `xy` engineering shear). Supplementary longitudinal axes are shipped ADDITIVELY in §6 — they are **not** the frozen deliverable and amend nothing.

> **★ANISOTROPY DISCLOSURE, added by the PR #802 adversarial review (finding F2) and stated before any longitudinal number is read.** This medium is **CUBIC, not isotropic.** Measured Zener anisotropy of the cold uncaged reference at `L = 16`: `A = C44/C′ = 1.330402` (SUBC) and `1.605316` (KUBC) — far from the isotropic `A = 1`. **A cubic medium therefore has no single "longitudinal modulus": it is direction-dependent.** Along `[100]` the longitudinal modulus is `C11 = K + 4C′/3` with `C′ = (C11−C12)/2`; along `[111]` it is `K + 4C44/3`. The axis this driver previously shipped and labelled *"the P-wave modulus `M = K + 4G/3` (`= C11` for an isotropic average)"* is the **`[111]`** one, and that label is **WITHDRAWN**: on the cold uncaged reference it overstates the true `C11` by **`18.9 %`** under KUBC (`M_[111] = 2.861883` vs `C11 = 2.406553`) and by **`7.9 %`** under SUBC (`1.891127` vs `1.752290`). `C′` is now MEASURED directly through the same machinery (§6.5). **No downstream reader may consume `M_*_abs` as `C11`.** No isotropy check existed anywhere in the frozen prereg, the driver, or the first version of this result doc — that absence is the finding.

**★SCOPE, verbatim from the frozen §7 and required at every headline:** `SCOPE: this bench brackets K_eff ONLY. Every r_Z interval it reports is a K-BRACKET AROUND AN ASSUMED ρ_eff/ρ_0 ≡ 1 — the ρ half is ASSUMED, not measured, not bracketed. This lane does NOT resolve walk-1's ρ half; that is OWED-2 (research/2026-07-22_vessel-state-rve_result.md §9), a separate lane, and OWED-1 does not dispose of it.`

**★SCOPE, verbatim from the frozen §7 and required at every headline:** `SCOPE: this bench brackets K_eff ONLY. Every r_Z interval it reports is a K-BRACKET AROUND AN ASSUMED ρ_eff/ρ_0 ≡ 1 — the ρ half is ASSUMED, not measured, not bracketed. This lane does NOT resolve walk-1's ρ half; that is OWED-2 (research/2026-07-22_vessel-state-rve_result.md §9), a separate lane, and OWED-1 does not dispose of it.`

---

## ★BOTTOM LINE

**The bracket was built, run, and reproduces the merged corpus bit-exactly. The frozen GATE STRUCTURE then returned VOID on two independent counts — and both are defects in the frozen criteria, not in the extraction.** Under the frozen §4B rule (`gate_fireability_selftest_pass = selftest_G1_fires AND selftest_G2b_fires AND selftest_partition_pass. If ANY fails to force its target, the correctness gates are a checklist not gates ⇒ the bench is VOID before any bracket is read; route to Grant.`) the correct disposition is: **the bracket is COMPUTED AND SHIPPED IN FULL, but is NOT BANKED as physics, and the two criterion defects are ROUTED.** Nothing is relabelled to convert a ❌ into a ✅.

> ### BENCH STATUS = **VOID AS FROZEN** — on two counts, both criterion-side
>
> **COUNT 1 — `selftest_G2b_fires = False`.** The frozen §4B self-test cannot fire as written. Ships both normalizations, as the frozen latitude requires.
> **COUNT 2 — frozen §4 G1 ratio-ordering violations on 8 of 48 measurements**, every one of them in the `T2` shear companion mode, every one of them RATIO-ONLY: `absolute_theorem_grade_ordering_holds_everywhere = True` (48/48). Under the strict reading of "VOID for that configuration" this voids 8 configurations **including both headline arms**.

**And here is what the instrument nevertheless established, labelled as computed-not-banked:**

> **THE BRACKET (BULK `K`; `ρ_eff/ρ_0 ≡ 1` ASSUMED, not measured).** For the #782 headline wall `bulk_only_cold` at `φ_sf` (`L=16`, `r_cage = 2.2`, `s = 4.5`, deep rail `1e-4`):
> `K_eff/K_0 ∈ [0.26340, 0.41421]` (PRIMARY, width `0.15081`, `w_rel = 0.44514`) ⇒ `r_Z ∈ [0.51322, 0.64359]`
> `K_eff/K_0 ∈ [0.21209, 0.51442]` (CONSERVATIVE / theorem-grade) ⇒ `r_Z ∈ [0.46053, 0.71723]`
>
> For the **#796 grown arm on its frozen tangent operator**:
> `K_eff/K_0 ∈ [0.26367, 0.41429]` (PRIMARY, width `0.15062`) ⇒ `r_Z ∈ [0.51348, 0.64365]`
> `K_eff/K_0 ∈ [0.21231, 0.51451]` (CONSERVATIVE) ⇒ `r_Z ∈ [0.46077, 0.71729]`
>
> **★THE VERDICT-RELEVANT SPLIT, and it is the whole result:** against the #782 band edge `T1: r_Z = 0.5`, the **PRIMARY** bracket **RESOLVES-HIGH** at both headline arms (`0.51322 > 0.5`, `0.51348 > 0.5`) — but the **CONSERVATIVE (theorem-grade)** bracket **STRADDLES** it (`0.46053 ≤ 0.5 ≤ 0.71723`). **The two bracket definitions disagree about whether the corpus's `r_Z ≈ 0.54` reading is bound-robust, and the one that disagrees is the rigorous one.** Both were frozen in advance precisely so this could not be chosen after the fact.

**The banked corpus numbers sit INSIDE their brackets.** #782's `K_eff/K_0 = 0.296` (core convention) reproduces at `0.29636822324939766` and lies inside `[0.26340, 0.41421]`; #796's painted/frozen-tangent `0.2982369862639104` reproduces to `0.2982369859937546` and lies inside `[0.26367, 0.41429]`; #796's grown live-operator `K_tan/K_0 = 0.29548` also lies inside. `core_estimator_inside_primary_bracket = True` at both headline arms. **No banked number is contradicted by this bench.**

> ### ★AND THE CONSEQUENCE THAT CUTS THE OTHER WAY — stated here, at the top, with numbers
>
> **#782's SOLE bound-robust macro-side reading does NOT survive on the bound-carrying measure.** Merged #782 `research/2026-07-21_rve-aggregation-bench_result.md:124` states, verbatim: `only compressed r_Z = 0.466 < 0.5 is bound-robust.` `:12` carries that same compressed leg as the MACRO-side leg of the BIN-4 `r_Z` straddle. **That `0.466` is `√(R_KUBC_core)` — the CORE-energy estimator, which the frozen prereg §2.3 states carries NO bound status under EITHER boundary condition.** This lane reproduces it **bit-for-bit** (`K_here_core = 0.2176075097402979` = #782's own shipped `leg4_verdict.by_class.bulk_only_compressed.K_eff_over_K0_sf`, `reproduces_782_core_bitwise = true`) and then measures the same configuration on the WHOLE-CELL apparent modulus — the measure the Hill/Huet kinematic-uniform theorem actually bounds from above:
>
> | #782 leg (at `φ_sf`) | `r_Z` CORE estimator (#782's number; **no bound status**) | `r_Z` WHOLE-CELL KUBC (**the actual upper bound**) | macro-side (`< 0.5`) on the bound-carrying measure? |
> |---|---|---|---|
> | `bulk_only_compressed` | `0.4664842009546496` | `0.6098352173422836` | **NO** |
> | `symmetric_cold` | `0.38583455489392426` | `0.5850392860613116` | **NO** |
> | `bulk_only_cold` | `0.5443971190678709` | `0.6435934144284258` | NO |
> | `bulk_only_expanded` | `0.5676919873253737` | `0.6556895088638865` | NO |
>
> **`2` of `4` legs read macro-side on the core estimator; `0` of `4` do on the bound-carrying measure.** The core estimator sits BELOW the bound-carrying KUBC reading at **every** leg — the direction that manufactures a macro-side reading out of a measure that cannot support one. **So `compressed r_Z = 0.466 < 0.5` is not bound-robust; it is estimator-conditional.** Adding this lane's lower bound, the compressed leg's true `r_Z` is bracketed `[0.4243721849890805, 0.6098352173422836]` — it **STRADDLES** `0.5`. JSON: `F5_782_bound_robustness_crosscheck_NOT_FROZEN`.
>
> **Does "#782 BIN-4 stands unchanged" survive this? Re-examined honestly: the BIN survives; its stated BASIS does not, and the basis correction is stated rather than absorbed.** BIN-4 is *UNDETERMINED*. Removing a bound-robust macro-side leg makes the `r_Z` axis **more** undetermined, not less, so nothing here can promote BIN-4 to a decided bin — and this lane mints no bin and edits no merged doc. **But #782 §7.1's basis sentence is now known to be wrong as written**, and #782 §5's *"verdict-controlling cross-class flip"* between a macro-side compressed leg and matched-side cold/expanded legs **does not exist on the bound-carrying measure** — there, all four legs' upper bounds sit above `0.5` and the two-sided brackets STRADDLE or RESOLVE-HIGH, never RESOLVE-LOW. **The honest statement is therefore: BIN-4's label stands, #782's stated basis for it weakens, and this is the second basis correction routed to #782 (the first came from the ρ-flags audit).** ROUTED to Grant / the auditor lane — see §8 consequence 7. It is **not** softened here: it was computed by this lane, it cuts against the lane's own status-quo-preserving headline, and it is stated in the same breath as the headline it undercuts.

**What this does NOT do.** It does not measure `ρ`. It does not resolve OWED-2. It does not tighten, move or re-band any standing verdict — under the frozen §5.5 the STRADDLE disposition is explicit: `If a bracket STRADDLES its threshold: the corresponding corpus verdict is recorded as BOUND-CONDITIONAL and is NOT tightened in either direction. The standing #782 BIN-4 and #796 UNDETERMINED labels STAND UNCHANGED. No new bin is minted, no side is picked, no rescue is derived (Rule 11/12).` That is the disposition taken **on the bin label**; the *basis* correction above is stated separately and routed, because a disposition that leaves a label alone is not licence to leave a known-wrong basis unstated.

---

## §1 — Instrument validation: the SUBC primitive is sound

| check | reading | verdict |
|---|---|---|
| active set / connectivity | `L∈{12,16,20}`: exactly `1` degree-0 node each; degree>0 subgraph = `1` connected component at all three sizes | PASS (the frozen null space is the 3 translations of a single component) |
| Born-model rotation (frozen §0 walk item 7) | `E(uniform translation) = 0.0` exactly; `E(rigid rotation, 1e-3) = 1.984e-3 > 0`; `born_model_confirmed_rotations_cost_energy = True` | CONFIRMED as an instrument fact — rotations are NOT null modes, so translation-only projection is correct |
| Hill-lemma stress deficit | `Σ̄/σ = 0.872309 (L12) / 0.904749 (L16) / 0.924044 (L20)` | the expected shell-mean-depth deficit; it CANCELS in every ratio |
| G4 SUBC convergence | worst relative residual `9.99e-10 ≤ 1e-9` over `48` solves; worst iteration count `6474` vs the `60000` cap | **PASS** |
| G5 work identity | worst `|U − ½f·u|/U = 8.63e-16 ≤ 1e-8` | **PASS** (convergence-EQUIVALENT, labelled) |
| G8 load-amplitude invariance | `R_SUBC(σ) vs R_SUBC(10σ)` rel `1.05e-15 ≤ 1e-10` | **PASS** (IDENTITY, labelled — not a discriminating gate) |
| G2a uniform-medium null | both ratios `1.0` to `< 1e-12`, both modes | holds (IDENTITY, labelled — never counted as a gate) |
| G3 determinism | two independent full runs, separate processes, separate `--out`; `diff -q` **CLEAN**, timing-stripped payloads byte-identical (`289 780 B` each); `determinism_digest` identical `c5fe89f5a95acbc72295eb4c998aaf31b851eca4e899fa51a1d16953e8d4fd56` | **PASS** — the frozen criterion itself, RUN, not a proxy |

Frozen: `G4: every SUBC pure-Neumann solve reaches relative residual ≤ 1e-9 within the 60000-iteration cap; the residual and iteration count of every solve are shipped in the JSON.` → PASS.
Frozen: `G3: two independent full driver runs, in separate processes writing separate output paths, produce byte-identical timing-stripped results (diff -q CLEAN) and an identical determinism digest.` → PASS.
Frozen: `G5: for every SUBC solve, |U_SUBC − ½·f·u| / U_SUBC ≤ 1e-8.` → PASS.
Frozen: `G8: R_SUBC is invariant under σ → 10σ to within 1e-10.` → PASS.

### §1.1 — G6, the reproduction cross-check: BIT-EXACT

Frozen: `G6: the driver's own KUBC re-computations must reproduce the merged numbers within 2e-3 relative` → **PASS**, and two of the three at machine zero.

| merged quantity | recomputed | merged target | rel |
|---|---|---|---|
| #782 `bulk_only_cold` core-energy ratio at `φ_sf` | `0.2963682232` | `0.296` | `1.24e-03` |
| #796 isotropic control | `0.2963682232` | `0.2963682232` | `0.00e+00` |
| #796 painted-anisotropic | `0.2982369863` | `0.2982369863` | `0.00e+00` |

**This is the load-bearing sanity check:** our reconstruction of the shipped #782/#796 arms IS the shipped arm, to the last printed digit. Everything that follows is therefore a statement about boundary conditions, not about a re-implementation drifting from the corpus.

### §1.2 — G7, the STOP-gate mirror and the size trend

Frozen: `G7a (mirror validity, carried from #782): under BOTH boundary conditions the deep-rail bulk-only cage array must SOFTEN (ratio < 1) while the RIGID control must STIFFEN (ratio > 1). A wrong-sign mirror under EITHER boundary condition stops the lane.` → **PASS.** `bulk_only` at `φ_sf`: `R_SUBC = 0.26340 < 1` and `R_KUBC = 0.41421 < 1`. `rigid`: `R_SUBC = 1.84885 > 1` and `R_KUBC = 20.91818 > 1`. The mirror holds under BOTH boundary conditions — the sign is the gate, and it does not turn on the boundary condition.

Frozen: `G7b (size trend): the PRIMARY bracket width w(L) at φ_sf must be non-increasing across L ∈ {12,16,20} within a 0.02 absolute slack` → **PASS** as written: `w = 0.22153 (L12) → 0.15081 (L16) → 0.09937 (L20)`, monotonically decreasing.

**★HONEST CAVEAT ON G7b, disclosed rather than banked (see §6 deviation D-4).** The three size points do NOT hold the composite fixed: at a fixed intensive label `φ = 0.48946` the REALIZED cage fraction is `0.2200 / 0.3082 / 0.3705` (box basis) and `0.2186 / 0.3079 / 0.3713` (bond basis) at `L = 12/16/20`, because the number of cages that fit inside the standoff grows `8 → 27 → 64`. So `w(L)` is a trend across three DIFFERENT realized composites, not a clean size-convergence trend. The gate passes as written; the inference "the bracket is converging with box size" is **NOT** licensed by it and is not made.

---

## §2 — ★THE BRACKET (frozen §5.1), per configuration

All at `L = 16` unless stated; `bw = 1.5`; deep rail `S_RAIL = 1e-4`; `cage_w = 1.0`; KUBC `ε = 1e-3`; SUBC `σ = 1`. **Modulus = BULK `K` (hydro rows) / SHEAR `G` (shear rows).** `ρ_eff/ρ_0 ≡ 1` ASSUMED throughout.

| configuration (mode) | PRIMARY `[SUBC, KUBC]` | width | `g_0` | CONSERVATIVE `[R_lo, R_hi]` | banked CORE | `T1` PRIMARY / CONSERVATIVE |
|---|---|---|---|---|---|---|
| `bulk_only_cold_rc1.3` (hydro) | `[0.34824, 0.56040]` | `0.2122` | `1.2419` | `[0.28040, 0.69588]` | `0.23907` | RESOLVES-HIGH / RESOLVES-HIGH |
| `bulk_only_cold_rc1.6` (hydro) | `[0.26889, 0.48343]` | `0.2145` | `1.2419` | `[0.21651, 0.60034]` | `0.18948` | RESOLVES-HIGH / STRADDLES |
| `bulk_only_cold_rc1.9` (hydro) | `[0.23983, 0.42898]` | `0.1892` | `1.2419` | `[0.19311, 0.53275]` | `0.19972` | STRADDLES / STRADDLES |
| **`bulk_only_cold_phi_sf` (hydro)** | **`[0.26340, 0.41421]`** | `0.1508` | `1.2419` | **`[0.21209, 0.51442]`** | `0.29637` | **RESOLVES-HIGH / STRADDLES** |
| `bulk_only_cold_phi_sf` (shear) | `[0.69233, 0.60774]` | `−0.0846` | `2.1600` | `[0.32052, 1.31274]` | `0.67119` | ★G1 RATIO INVERSION |
| `symmetric_cold_rc1.3` (hydro) | `[0.23145, 0.50562]` | `0.2742` | `1.2419` | — | `0.12874` | STRADDLES / STRADDLES |
| `symmetric_cold_rc1.6` (hydro) | `[0.14984, 0.42955]` | `0.2797` | `1.2419` | — | `0.08331` | STRADDLES / STRADDLES |
| `symmetric_cold_rc1.9` (hydro) | `[0.10939, 0.36323]` | `0.2538` | `1.2419` | — | `0.07686` | STRADDLES / STRADDLES |
| `symmetric_cold_phi_sf` (hydro) | `[0.10945, 0.34227]` | `0.2328` | `1.2419` | — | `0.14887` | STRADDLES / STRADDLES |
| `bulk_only_compressed_phi_sf` (hydro) | `[0.18009, 0.37190]` | `0.1918` | `1.2419` | — | `0.21761` | STRADDLES / STRADDLES |
| `bulk_only_expanded_phi_sf` (hydro) | `[0.29366, 0.42993]` | `0.1363` | `1.2419` | — | `0.32227` | RESOLVES-HIGH / STRADDLES |
| `rigid_phi_sf` (hydro) | `[1.84885, 20.91818]` | `19.069` | `1.2419` | — | `1.58271` | RESOLVES-HIGH / RESOLVES-HIGH |
| `routeB_…_s3.6` (hydro) | `[0.37170, 0.59742]` | `0.2257` | `1.2419` | — | `0.20390` | RESOLVES-HIGH / RESOLVES-HIGH |
| `routeB_…_s4.2` (hydro) | `[0.27764, 0.50501]` | `0.2274` | `1.2419` | — | `0.16391` | RESOLVES-HIGH / STRADDLES |
| `routeB_…_s5.0` (hydro) | `[0.26089, 0.41606]` | `0.1552` | `1.2419` | — | `0.23922` | RESOLVES-HIGH / STRADDLES |
| `routeB_…_s6.5` (hydro) | `[0.58429, 0.72413]` | `0.1398` | `1.2419` | — | `0.47279` | RESOLVES-HIGH / RESOLVES-HIGH |
| **`grown_frozen_tangent` (hydro)** | **`[0.26367, 0.41429]`** | `0.1506` | `1.2419` | **`[0.21231, 0.51451]`** | `0.29824` | **RESOLVES-HIGH / STRADDLES** |
| `grown_frozen_tangent` (shear) | `[0.66805, 0.59587]` | `−0.0722` | `2.1600` | `[0.30928, 1.28710]` | `0.63239` | ★G1 RATIO INVERSION |
| `painted_anisotropic` (hydro) | `[0.26367, 0.41429]` | `0.1506` | `1.2419` | — | `0.29824` | RESOLVES-HIGH / STRADDLES |
| `isotropic_control` (hydro) | `[0.26340, 0.41421]` | `0.1508` | `1.2419` | — | `0.29637` | RESOLVES-HIGH / STRADDLES |
| `uniform_medium_null` (both) | `[1.00000, 1.00000]` | `0.0000` | — | — | `1.00000` | IDENTITY (§4 G2a) |
| `bulk_only_cold_phi_sf_L12` (hydro) | `[0.30027, 0.52180]` | `0.2215` | `1.3452` | — | `0.27990` | RESOLVES-HIGH / STRADDLES |
| `bulk_only_cold_phi_sf_L20` (hydro) | `[0.24927, 0.34864]` | `0.0994` | `1.1845` | — | `0.29423` | STRADDLES / STRADDLES |

Full per-row data (both modes, all 48 measurements, every CG residual and iteration count, every `r_Z` interval, both VOID scopings and the no-VOID-overlay class): JSON `reads` and `configurations`; code path `subc_kubc_bracket.py::read_config` / `::bracket_from_pair`.

**The `painted_anisotropic` row is byte-identical to `grown_frozen_tangent` by construction** — on the #796 carve they are the SAME operator, and running both is the G6 faithfulness cross-check, not two physics arms (frozen §3 B.8).

### §2.1 — Anti-seduction fence, applied

Frozen: `a wide bracket is a statement about the INSTRUMENT, not about the medium: the result doc may NOT convert bracket width into physical significance in either direction, and must report the uncaged gap g_0 alongside every width so the reader can see how much of it is finite-size boundary layer`. `g_0` is in every row above. The headline width `0.1508` sits on an uncaged gap of `1.2419`; **no physical significance is claimed for the width in either direction.**

---

## §3 — ★COUNT 1: `selftest_G2b_fires = False` — the frozen self-test cannot fire as written

Frozen: `SELFTEST-G2b: recompute the uncaged g_0 using the NOMINAL applied σ instead of the Hill-lemma Σ̄ read from the shipped load set, and assert G2b REPORTS A VIOLATION (g_0 < 1 or non-monotone in L).`
Frozen acceptance: `selftest_G2b_fires = True`. **COMPUTED: `False`.**

The frozen latitude's SHIPS-clause is discharged — both normalizations are in the JSON unconditionally:

| `L` | `Σ̄/σ` | `g_0` (Hill-normalized, correct) | `g_0` (NOMINAL-σ, deliberately broken) | `1/(Σ̄/σ)²` |
|---|---|---|---|---|
| 12 | `0.872309` | `1.3451548` | `1.0235586` | `1.3141942` |
| 16 | `0.904749` | `1.2419126` | `1.0165925` | `1.2216425` |
| 20 | `0.924044` | `1.1844537` | `1.0113541` | `1.1711562` |

The mis-normalized `g_0` is `≥ 1` at every `L` **and** still non-increasing in `L`. **Neither clause of G2b fires**, so the deliberately-broken extraction is not caught.

**★THE MECHANISM — and it is a real instrument finding, not an excuse.** `g_0(L)` and `1/(Σ̄/σ)²` agree to `2.4 % / 1.7 % / 1.1 %` and are converging. **The uncaged KUBC/SUBC gap and the Hill-stress deficit are the SAME finite boundary layer measured two ways.** Substituting the nominal `σ` therefore multiplies `g_0` by very nearly its own inverse, landing at `1.01–1.02` — just barely on the PASSING side. The frozen §4B design anticipated the magnitude (*"the same order as the true gap"*) but drew the opposite conclusion from it: same-order **and same-sign** means the perturbation cancels the signal rather than probing it. **This is a frozen-criterion design defect, surfaced at integrator time (Rule 10), and it is NOT repaired here** (repairing a frozen self-test post-hoc is exactly the move the §4B rule exists to prevent).

**★THE FROZEN TEXT IS AMBIGUOUS ABOUT WHAT HAPPENS NEXT, and this lane does not resolve it.** The frozen latitude reads: `if the nominal-σ mis-normalization does not push g_0 below 1 at every L, the self-test is accepted on the MONOTONICITY clause alone provided the driver SHIPS the computed g_0(L) under both normalizations so the reader can see which clause fired`. Two readings:

- **(a) "judged on the monotonicity clause alone"** — monotonicity is not violated either ⇒ the self-test does **not** fire ⇒ `gate_fireability_selftest_pass = False` ⇒ VOID.
- **(b) "accepted, provided both normalizations are shipped"** — both are shipped ⇒ accepted ⇒ not VOID.

Reading (a) is the one this result carries, **because it is the reading that voids the bench** and therefore cannot be a rescue. The adjudication is Grant's / the auditor's, not this lane's. Both booleans are shipped: JSON `selftest_G2b.selftest_G2b_fires_STRICT` and `.selftest_G2b_fires_LATITUDE_SHIPS_CLAUSE`.

**The other two self-tests DO fire.**
- Frozen: `SELFTEST-G1: recompute R_SUBC with the ratio taken in the KUBC direction (U_SUBC^arm/U_SUBC^uncaged instead of U_SUBC^uncaged/U_SUBC^arm) on the bulk_only_cold φ_sf configuration, and assert G1 REPORTS A VIOLATION.` → **FIRES.** Correct direction `R_SUBC = 0.26340` (ordering OK); inverted `3.79654` (ordering VIOLATED, as required). `selftest_G1_fires = True`.
- Frozen: `SELFTEST-PARTITION: walk a synthetic grid of (bracket_lo, bracket_hi, threshold) tuples through the SAME classifier the verdict uses; assert every tuple lands in EXACTLY one of RESOLVES-LOW / RESOLVES-HIGH / STRADDLES / VOID, that each of the three non-VOID classes is returned by at least one tuple, and that no tuple is unclassified.` → **PASSES.** `32` tuples, `0` unclassified, all four classes returned. `selftest_partition_pass = True`.

---

## §4 — ★COUNT 2: the G1 ratio-ordering violations — 8 of 48, ALL shear, ALL ratio-only

Frozen: `G1: for EVERY bracketed configuration and BOTH modes, R_SUBC ≤ R_KUBC must hold on the WHOLE-CELL pair, with a numerical slack of 1e-6 relative. A violation means the SUBC extraction is WRONG — the bench is VOID for that configuration and the violation is reported as an instrument failure, NEVER as a physical finding that the lower bound exceeds the upper bound.`

**Computed: 8 violations of 48 checked measurements.** Every one is in the `T2` shear companion mode:
`bulk_only_cold_phi_sf::shear`, `bulk_only_cold_phi_sf_L12::shear`, `bulk_only_cold_phi_sf_L20::shear`, `bulk_only_expanded_phi_sf::shear`, `grown_frozen_tangent::shear`, `isotropic_control::shear`, `painted_anisotropic::shear`, `routeB_bulk_only_cold_s5.0::shear`.
**The hydrostatic (A1) sector — the headline sector — is clean: 24 of 24 ordered correctly.**

**★AND THE VIOLATIONS DO NOT SUPPORT THE INFERENCE THE FROZEN TEXT DRAWS FROM THEM (flag-don't-fix).** G1's second clause is `G1 also requires the ABSOLUTE ordering K_SUBC ≤ K_KUBC and G_SUBC ≤ G_KUBC on every configuration INCLUDING the uncaged reference.` That clause — the theorem-grade one — **holds on all 48 measurements**, including every violating row: JSON `gate_G1_VOID_ordering.absolute_theorem_grade_ordering_holds_everywhere = True`, and `violations_that_are_RATIO_ONLY_with_absolute_ordering_intact` contains all 8. At `bulk_only_cold_phi_sf` shear the absolutes are `G_SUBC = 0.290283 ≤ G_KUBC = 0.550409`. **So the SUBC extraction is NOT wrong at those rows, and the frozen inference "a violation means the SUBC extraction is WRONG" is not supported by the data.**

**The mechanism is algebraic and the prereg already contains it.** `R_KUBC/R_SUBC = g_0^arm / g_0^uncaged`, so the PRIMARY ratio pair is bound-ordered **only when the arm's own KUBC/SUBC gap exceeds the reference's**. In the shear channel the UNCAGED gap is huge (`g_0 = 2.1600` at `L=16`, vs `1.2419` in bulk) because the under-coordinated free surface is far floppier in shear; the caged arm's gap is smaller (`0.550409/0.290283 = 1.896 < 2.160`), so the ratio inverts. The frozen §2.1 states this outright: `the PRIMARY same-instrument bracket cancels the finite-size boundary-layer bias to leading order (numerator and denominator share the box and the boundary condition) but is NOT theorem-grade on the RATIO, because the uncaged reference is itself boundary-conditioned`. **G1 demands a theorem-grade ordering from a quantity the same prereg declares not theorem-grade.** This is the SAME mutual-satisfiability defect the prereg's §6 audit caught for the core estimator and moved G1 off — the audit moved the gate from the core pair to the whole-cell pair but did not notice the whole-cell RATIO carries the identical exposure whenever the reference's own gap is large. **The gate outcome is reported AS FROZEN (VOID). The criterion is ROUTED, not relabelled.**

**★VOID SCOPING — also ambiguous, also shipped both ways, also resolved conservatively.** Frozen G1 says the bench is VOID "for that configuration"; §5.3 says `G1 violated for that configuration`. Under the **STRICT** reading a shear-mode inversion voids that configuration's hydrostatic read too — voiding 8 configurations **including both headline arms**. Under the per-`(configuration, mode)` reading only the 8 shear measurements void. **This result carries the STRICT reading**, again because it is the one that voids more and so cannot be a rescue. Both are shipped: JSON `gate_G1_VOID_ordering.void_configs_STRICT` and `.void_config_modes`, and every read row carries `VOID_strict_per_configuration`, `VOID_per_configuration_and_mode`, and `classes_no_void_overlay` so the VOID overlay is separable from the threshold relation.

Per frozen §5.5 item 4: `If a configuration VOIDs: its bracket is NOT reported as physics; the standing merged verdict for that configuration is left exactly as merged, and the extraction failure is reported as an instrument finding with its residuals.` — **honoured: nothing above is banked, and no standing verdict is moved.**

---

## §5 — ★THE READ, had the gates not voided (frozen §5.4) — reported as CONDITIONAL, not banked

Frozen: `HEADLINE: the PRIMARY r_Z bracket of configuration 1 (bulk_only_cold at φ_sf) against T1 (r_Z = 0.5), and the PRIMARY r_Z bracket of configuration 7 (the #796 grown frozen-tangent arm) against T1 and T2 — each reported with its outcome class, its width, and its CONSERVATIVE counterpart.`

| arm | `r_Z` PRIMARY | vs `T1 = 0.50` | `r_Z` CONSERVATIVE | vs `T1 = 0.50` | vs `T2 = 0.45` | vs `T2 = 0.55` |
|---|---|---|---|---|---|---|
| `bulk_only_cold` @ `φ_sf` | `[0.51322, 0.64359]` | **RESOLVES-HIGH** | `[0.46053, 0.71723]` | **STRADDLES** | RESOLVES-HIGH | STRADDLES |
| #796 `grown_frozen_tangent` | `[0.51348, 0.64365]` | **RESOLVES-HIGH** | `[0.46077, 0.71729]` | **STRADDLES** | RESOLVES-HIGH | STRADDLES |

**All numbers `[derived]` in their `K` factor and `[assumption]` in their `ρ` factor — MIXED-provenance. `SCOPE: this bench brackets K_eff ONLY.`**

**What this would have meant, stated conditionally.** On the PRIMARY (same-instrument) definition, the low side of both headline brackets sits **above** the `r_Z = 0.5` macro-cage edge, so the `Z_lo`/SOFT reading — the one #796 §4 flagged as excluded only by the anchor choice, and the one that would re-open the Reading-B route — would be **excluded on both boundary conditions**, i.e. the exclusion would not be an artefact of clamping. **On the CONSERVATIVE (theorem-grade) definition it would not be excluded**: the rigorous bracket still contains `0.5`. Frozen §2.2: `the CONSERVATIVE bracket is theorem-grade and always contains the PRIMARY bracket; it is wider by exactly the uncaged gap g_0 on each side`. **The rigorous answer is therefore that the corpus's `r_Z ≈ 0.54` remains BOUND-CONDITIONAL, and the frozen §5.5 STRADDLE disposition applies: standing labels UNCHANGED.**

**T3 (`R = 1.0`, the soften/stiffen sign) is the one threshold that resolves under BOTH definitions and both boundary conditions**: every deep-rail cage arm is RESOLVES-LOW (softens) and the `rigid` control is RESOLVES-HIGH (stiffens). That is the §5.3 Layer-2 forced-reachability discharge, realized. `outcome_classes_returned_with_VOID_overlay_removed = ["RESOLVES-HIGH", "RESOLVES-LOW", "STRADDLES"]` — all three non-VOID classes were returned on the physical set, and VOID was returned by SELFTEST-G1. **No class was a dead letter.**

**T4 lift (frozen §5.2), applied per-boundary-condition to the grown-vs-control pair:** `lift_under_SUBC = 1.00102` (band `L1`), `lift_under_KUBC = 1.00019` (band `L1`), `band_flips_across_boundary_condition = False`. **#796's null lift is boundary-condition-robust.** Reported as a per-BC pair, not a bracket — a ratio of two ratios is not bound-ordered (JSON `verdict.T4_lift_bands_per_boundary_condition.note`).

---

## §6 — SUPPLEMENTARY axes shipped ADDITIVELY (NOT frozen, NOT the deliverable, nothing amended)

### §6.1 — The `[111]` longitudinal modulus `K + 4·C44/3` (the modulus-identity question, ROUTED)

> **★LABEL WITHDRAWN (PR #802 review, finding F2).** This axis was previously shipped as *"the P-wave / VRH modulus `M = K + 4G/3` (`= C11` for an isotropic average)"*. **That label is WRONG on this medium and is withdrawn.** The `G` this driver measures is the `xy` engineering shear constant **`C44`**, and the medium is **cubic-anisotropic** (§6.5). On a cubic medium `K + 4C44/3` is the longitudinal modulus along the body diagonal **`[111]`**; the `[100]` longitudinal modulus is `C11 = K + 4C′/3` with `C′ = (C11−C12)/2`, and the two differ by `(4/3)(C44 − C′)`. **`M_SUBC_abs` / `M_KUBC_abs` below are the `[111]` quantity and must NOT be consumed as `C11`.** The true `C11` is measured and shipped in §6.5.

The frozen deliverable is the BULK-`K` bracket. But a normal-incidence impedance is `Z = ρc_P = √(ρ(K + 4G/3))`, and `√(ρK)` is the correct impedance **only for a `G = 0` medium** — which this composite is not (`G_eff/G_0 ≈ 0.61–0.67` at `φ_sf`). Because both `K` and `G` are bracketed by the same pair of boundary conditions and `M` is monotone increasing in both, `M_SUBC = K_SUBC + 4G_SUBC/3 ≤ M* ≤ M_KUBC` is a legitimate absolute bracket. Shipped for every configuration that ran both modes:

| arm | `M` absolute `[SUBC, KUBC]` | `R_M` `[lo, hi]` | `r_Z(M)` `[lo, hi]` | `g_0(M)` |
|---|---|---|---|---|
| `bulk_only_cold` @ `φ_sf` | `[0.7379, 1.4191]` | `[0.39020, 0.49587]` | `[0.62466, 0.70418]` | `1.5133` |
| `symmetric_cold` @ `φ_sf` | `[0.2897, 1.1408]` | `[0.15319, 0.39860]` | `[0.39140, 0.63135]` | `1.5133` |
| `bulk_only_compressed` @ `φ_sf` | `[0.4928, 1.2536]` | `[0.26056, 0.43803]` | `[0.51045, 0.66184]` | `1.5133` |
| #796 `grown_frozen_tangent` | `[0.7247, 1.4049]` | `[0.38321, 0.49091]` | `[0.61904, 0.70065]` | `1.5133` |

**The axis choice moves the bin.** At the headline arm the bulk-`K` `r_Z` bracket is `[0.513, 0.644]` while the P-wave `r_Z(M)` bracket is `[0.625, 0.704]` — the latter clears `T2 = 0.55` entirely (`Z_hi`), the former does not. **WHICH modulus the corpus discriminator `r_Z` should ride is a DEFINITION question this lane does not own and does not settle.** It is surfaced with data and ROUTED to Grant. The frozen bulk-`K` axis remains the deliverable; nothing here amends the frozen prereg (§9 note 2).

### §6.2 — The pinned-shell confound (KUBC side only)

`rve_aggregation_bench.cubic_cage_centers` documents a `margin = 3.0` standoff *"so cages never touch the KUBC boundary shell"*, but the cage SHELL has radius `r_cage + cage_w`, so at larger `r_cage` the shell reaches into the `bw = 1.5` Dirichlet layer. Measured fraction of cage-shell NODES that are pinned under KUBC:

- route A (`s = 4.5`, `r_cage = 1.3/1.6/1.9/2.2`): `9.4 % / 19.4 % / 34.3 % / **51.3 %**`
- route B (`r_cage = 1.7`, `s = 3.6/4.2/5.0/6.5`): `0.0 % / 12.7 % / 40.9 % / 0.0 %`
- size scan at `φ_sf`: `53.3 % (L12) / 51.3 % (L16) / 48.5 % (L20)`

**At the headline geometry more than half the soft shell is clamped affine and cannot open, which stiffens the KUBC side.** Under SUBC no displacement is prescribed anywhere, so `pinned_fraction_SUBC = 0.0` by construction. **This asymmetry is exactly what a two-sided bracket is positioned to expose**, and it is a live confound for any KUBC-side number in this bench family — including the merged ones. It is reported **RAW and never subtracted** (frozen §0 pre-test check: RAW, no subtraction), and **no claim is made here about how much of the KUBC/SUBC gap it accounts for** — that attribution is routed, not asserted. It is also strongly route-dependent, so it cannot be treated as a common-mode offset that cancels in a scan.

### §6.3 — Realized vs intensive phase fractions (the labelling question, settled for THIS lane's configs)

The intensive label `φ = (4/3)πr³/s³` is a per-array-cell quantity; the finite bench cell realizes less because the cage cluster stands off the outer faces. Measured, for every configuration (JSON `configurations[*].fractions`):

| configuration | `n_cages` | `φ` intensive | `φ` realized (box) | `φ` realized (bond) | `f_incl` intensive |
|---|---|---|---|---|---|
| `bulk_only_cold_rc1.3` | 27 | `0.1010` | `0.0636` | `0.0612` | `0.5593` |
| `bulk_only_cold_rc1.6` | 27 | `0.1883` | `0.1186` | `0.1123` | `0.8079` |
| `bulk_only_cold_rc1.9` | 27 | `0.3153` | `0.1986` | `0.1973` | `1.1211` |
| `bulk_only_cold_phi_sf` | 27 | `0.4895` | `0.3082` | `0.3079` | `1.5063` |
| `routeB_…_s3.6` | 27 | `0.4411` | `0.1422` | `0.1400` | `1.7671` |
| `routeB_…_s4.2` | 27 | `0.2778` | `0.1422` | `0.1392` | `1.1128` |
| `routeB_…_s5.0` | 27 | `0.1646` | `0.1422` | `0.1395` | `0.6596` |
| `routeB_…_s6.5` | 8 | `0.0749` | `0.0421` | `0.0413` | `0.3002` |
| `…_phi_sf_L12` | 8 | `0.4895` | `0.2200` | `0.2186` | `1.5063` |
| `…_phi_sf_L20` | 64 | `0.4895` | `0.3705` | `0.3713` | `1.5063` |

**Two facts follow and are stated without adjudicating anything.** (i) The three `L∈{12,16,20}` size points carry the SAME intensive label `0.4895` but THREE DIFFERENT realized fractions (`0.220 / 0.308 / 0.371`) — so any size gate on this family compares three different composites (see §1.2 caveat, and note this bears on the merged #782/#796 RVE-size gate, which is the auditor's to assess, not this lane's to re-open). (ii) Route B holds realized `φ ≈ 0.142` almost constant across `s = 3.6/4.2/5.0` while the intensive label sweeps `0.441 → 0.165` — the two routes are not scanning the same variable in realized terms. **Nothing in this lane's bracket depends on either convention:** every frozen configuration is fixed by the TUPLE `(L, r_cage, s, cage_w, wall_class, s_rail)`, never by a `φ` label.

### §6.4 — The fully-SUBC-grown companion (frozen §3 D — explicitly NOT a bracket)

Frozen: `A fully-SUBC-grown arm, if run, is reported as a labelled companion and is explicitly NOT part of any bracket, because its microstructure co-varies with the boundary condition`.
Frozen budget: `the fully-SUBC-grown companion is capped at 40 outer iterations and 20 minutes wall-clock; on exceeding either it is reported as NOT-RUN with the reason, and no verdict depends on it` → **RAN and CONVERGED well inside budget: `5` outer iterations, `15.2 s`.** Self-consistency decay `0.6891 → 0.02404 → 3.592e-4 → 8.939e-6 → 1.371e-7`.

Grown under a traction-free boundary, the vessel reaches `min k_shear,eff = 0.29044 > 0` (no bond buckles), `peak_A = 0.07260`, `max|T| = 0.68910`. Probed under traction on its own frozen tangent: `R_SUBC = 0.26189`, `R_KUBC = 0.41276`, core `0.29820`. **These sit within `~0.6 %` of the KUBC-grown frozen-tangent arm** — i.e. the growth boundary condition barely moves the resulting tangent modulus on this instrument. **That is a COMPANION observation only and enters no bound-robustness claim** (frozen §8 Fork TANGENT); it is reported because it is cheap and informative, not because it brackets anything.

### §6.5 — ★THE MEDIUM IS CUBIC, NOT ISOTROPIC: `C′`, the true `C11`, and the Zener anisotropy (PR #802 review, finding F2)

**No isotropy check existed in the frozen prereg, in the driver, or in the first version of this result doc.** The `[111]`/`C11` mislabel of §6.1 survived precisely because nobody measured whether the assumption behind it holds. It does not. The repair MEASURES the missing constant rather than assuming it away.

**How `C′` is measured — through this lane's own machinery, no new physics.** A third probe mode `tetra` is added with `E = ε·diag(1,−1,0)` (KUBC) and `Σ = σ·diag(1,−1,0)` (SUBC), run through the SAME `subc_solve` / `kubc_solve` primitives, the SAME operator, the SAME tolerances as the two frozen modes. For a cubic medium that mode has strain energy density `2C′ε²` and complementary energy density `σ²/(2C′)`, so both extractions return `C′ = (C11−C12)/2` directly. **It is deliberately NOT in `BOTH_MODES` and NOT in any `by_mode` block, so it enters NO frozen gate, NO frozen read and NO frozen count** — it is carried in a separately-labelled `SUPPLEMENTARY_anisotropy_NOT_FROZEN` block. Additive, never substitutive. The realized SUBC macroscopic stress is `diag(+0.9047486144890591, −0.9047486144890545, 0)` to `7e-5` off-diagonal at `L = 16` — i.e. the cubic axes are the lattice axes, as assumed.

**The cold uncaged reference medium, both boundary conditions, all three box sizes:**

| `L` | `C44` `[SUBC, KUBC]` | `C′` `[SUBC, KUBC]` | **Zener `A = C44/C′`** `[SUBC, KUBC]` | `M_[111] = K + 4C44/3` `[SUBC, KUBC]` | **true `C11 = K + 4C′/3`** `[SUBC, KUBC]` |
|---|---|---|---|---|---|
| 12 | `[0.408064, 1.019449]` | `[0.312143, 0.625135]` | **`[1.307300, 1.630766]`** | `[1.780225, 3.022065]` | `[1.652330, 2.496313]` |
| 16 | `[0.419281, 0.905662]` | `[0.315154, 0.564165]` | **`[1.330402, 1.605316]`** | `[1.891127, 2.861883]` | `[1.752290, 2.406553]` |
| 20 | `[0.426097, 0.828878]` | `[0.316846, 0.523053]` | **`[1.344806, 1.584690]`** | `[1.960543, 2.754420]` | `[1.814875, 2.346654]` |

**`A ≠ 1` under BOTH boundary conditions at every box size — the medium is strongly cubic.** At `L = 16` the shipped `M_[111]` **overstates the true `C11` by `18.9 %` under KUBC and `7.9 %` under SUBC.**

**And the caged arms are cubic too** (`SUPPLEMENTARY_anisotropy_NOT_FROZEN` on every configuration). At the two headline arms:

| arm | `C′` `[SUBC, KUBC]` | Zener `A` `[SUBC, KUBC]` | `M_[111]` `[SUBC, KUBC]` | true `C11` `[SUBC, KUBC]` | `M_[111]` overstates `C11` by |
|---|---|---|---|---|---|
| `bulk_only_cold` @ `φ_sf` | `[0.26297, 0.39424]` | `[1.1039, 1.3961]` | `[0.73791, 1.41912]` | `[0.70149, 1.21090]` | `5.2 %` SUBC / `17.2 %` KUBC |
| #796 `grown_frozen_tangent` | `[0.25311, 0.38466]` | `[1.1066, 1.4029]` | `[0.72469, 1.40492]` | `[0.68871, 1.19826]` | `5.2 %` SUBC / `17.2 %` KUBC |

`C11 = K + 4C′/3` is monotone increasing in BOTH `K` and `C′`, each bracketed in the same direction by the same boundary-condition pair, so `C11_SUBC ≤ C11* ≤ C11_KUBC` is a legitimate ABSOLUTE bracket, exactly as for the `[111]` axis. Ratio brackets, both definitions, at the headline arms: `r_Z(C11)` PRIMARY `[0.63271, 0.70934]` / CONSERVATIVE `[0.53990, 0.83129]` (`bulk_only_cold`); PRIMARY `[0.62693, 0.70563]` / CONSERVATIVE `[0.53496, 0.82694]` (grown).

> ### ★ROUTED TO GRANT — this SHARPENS the modulus-identity question rather than answering it
>
> **A cubic medium has a DIRECTION-DEPENDENT longitudinal modulus. Protocol E launches its pulse along `[100]`.** Therefore the comparator for a Protocol-E time-of-flight is **`C11 = K + 4C′/3`** — **not** the `K + 4C44/3` axis this driver previously mislabelled "`C11` for an isotropic average", and **not** a VRH isotropic average of the two. This is a *third* live option in the already-routed modulus question (`K` vs `[111]` vs `[100]`), and the three do not agree: at the headline arm the CONSERVATIVE `r_Z` brackets are `K`: `[0.46053, 0.71723]` (STRADDLES `T1`), `M_[111]`: `[0.50778, 0.86626]` (RESOLVES-HIGH), `C11_[100]`: `[0.53990, 0.83129]` (RESOLVES-HIGH). **This lane does not answer it and does not pick.** JSON `configurations[*].SUPPLEMENTARY_anisotropy_NOT_FROZEN.ROUTED_TO_GRANT`.
---

## §7 — HONEST DEVIATIONS

1. **★D-1 — the lane died mid-run and was RESUMED.** The original lane process was killed by an API error immediately after the frozen prereg was committed and pushed ALONE (`1288e288`), at the point recorded as *"Now the driver."* A 437-line driver skeleton survived UNCOMMITTED in the worktree (the SUBC primitive, the three ratio definitions, the classifier, SELFTEST-PARTITION, the geometry helpers); it was read, kept, and completed. **The frozen prereg was BYTE-UNTOUCHED across the interruption and remains so** (verified: the committed blob at `1288e288` is the file that gates this doc). No verdict number existed before the freeze; none was carried across the interruption.
2. **★D-2 — SELFTEST-G2b does not fire (§3).** A frozen-criterion design defect: the mis-normalization the self-test uses is the same finite boundary layer as the gap it is meant to break, so it cancels rather than probes. Both normalizations shipped as the frozen latitude requires. The latitude sentence is ambiguous; the VOIDing reading is carried; the adjudication is ROUTED. **Not repaired.**
3. **★D-3 — frozen G1 fires on 8 non-errors (§4).** All shear-mode, all ratio-only, absolute theorem-grade ordering intact on 48/48. G1 demands a bound-ordering from the PRIMARY ratio, which frozen §2.1 itself declares not theorem-grade. Reported AS FROZEN (VOID); criterion ROUTED. **Not repaired, not relabelled.** Both VOID scopings shipped; the stricter one carried.
4. **★D-4 — G7b passes but its inference does not transfer.** The size scan changes the realized composite as it changes `L` (§6.3), so the monotone width decrease is not clean size-convergence evidence. Disclosed; the "bracket is converging" inference is NOT made.
5. **★D-5 — a prereg pilot number does NOT reproduce.** Frozen §1.1 discloses the design-time pilot as moment-free: *"`|Σ_i (x_i−x_c)×f_i| = 3.2e-14`"* at `L=12`. The shipped driver measures `4.284e-3` at `L=12` (`4.283e-3` at `L=16`, `4.309e-3` at `L=20`) — about `2.6e-6` of the `σ·A·span` scale, but **eleven orders above the disclosed pilot value**. Net FORCE is machine-zero as disclosed (`|Σf| = 4.5e-12`). The residual moment is **harmless and does not touch any result**: (i) it is reference-point-independent because the net force vanishes, (ii) rigid rotations are NOT null modes of the Born bond model (§1), so a moment-carrying load is admissible and the pure-Neumann operator is invertible on the complement of the translations, and (iii) Hill's lemma symmetrizes, so the antisymmetric part never enters `Σ̄`. Every solve converged to `≤ 1e-9` with the work identity exact to `8.6e-16`. **Flagged, not fixed** — I could not reproduce the pilot's `3.2e-14`, and I do not know what the pilot computed differently; the prereg is frozen and is not amended.
6. **★D-6 — supplementary axes added post-freeze, ADDITIVELY.** The P-wave `M = K + 4G/3` axis (§6.1), the pinned-shell fractions (§6.2) and the realized-fraction table (§6.3) are **NOT** frozen criteria and are labelled as such everywhere they appear. They add data; they replace, reweight and amend nothing. To supply the `M` axis, every bracketed configuration was run in BOTH modes rather than the frozen §3 per-configuration mode list (which called for `hydro` only on most arms) — a SUPERSET of the frozen configuration set, never a substitution. Runtime cost `188 s → 346 s`.
7. **★D-7 — a driver bug found and fixed before shipping (Rule 10).** The companion's self-consistency test initially compared the pre-solve operator against the previous pre-solve operator, which returns `0` on the first pass and declared convergence at `u = 0` after one outer iteration. Fixed to compare the operator re-evaluated at the NEW iterate against the one the solve used; the companion now converges in 5 outer iterations with clean decay (§6.4). The bug affected the companion only — which is explicitly not part of any bracket — and no bracket number changed.
8. **★D-8 — what was NOT run.** No periodic-BC arm (it is not a bound and is not what OWED-1 asks for; frozen §9 owed item 2). No surface-corrected SUBC estimator (frozen Fork SURFACE; routed). No `ρ` measurement of any kind (§7 scope fence; OWED-2 stands). No uniaxial `C11` mode under a matched dual pair — the `M` axis of §6.1 is assembled from the bracketed `K` and `G`, which is rigorous for `M` but is not a direct `C11` probe.
9. **★D-9 — an externally-reported claim NOT relied on.** A concurrent un-reviewed scoping lane reported a "3.19× KUBC over-stiffening" from a PBC comparison. That claim was subsequently root-caused as an artefact of a rotation-contaminated elastic-constant reconstruction and is **REFUTED**; **nothing in this lane's design, execution or reading depends on it**, and it is recorded here only so the non-dependence is explicit. This lane does not adjudicate PBC-vs-KUBC — that is a different lane's and the auditor's question (frozen §9 owed item 2).

---

## §8 — Calibration-vs-derived ledger (`consistency-vs-emergence`, frozen tags) + routed consequence

`R_SUBC`, `R_KUBC`, `R_KUBC_core`, `R_SUBC_core`, `R_lo`, `R_hi`, `g_0`, the bracket widths and the `G_eff` counterparts are `[derived]` dimensionless RATIOS (lattice static homogenization under two boundary conditions) — **CONSISTENCY-class, not emergence**: they test whether an already-banked lattice number is boundary-condition-robust, which is an internal-consistency question, and **no new physical constant is produced**. `ρ_eff/ρ_0 ≡ 1` is `[assumption]`, so every `r_Z` interval is **MIXED-provenance** — `[derived]` in `K`, `[assumption]` in `ρ` — and must be cited as such downstream. The srs bond model `ρ* = 9.77337` is `[import]` (`ν_Hill = 2/7`, GR-imported `K = 2G`, `ave.core.constants.N_NU`). The probe amplitudes (`ε = 1e-3`, `σ = 1`) and solver tolerances are `[engineering-choice]`, disclosed, and shown to cancel (G8) or be converged (G4). The Hill/Huet apparent-modulus ordering is a `[derived]` textbook theorem — the FORM the extraction is built on, not a fit. **`α`-CLEAN** (no `α`, no `Q_TANK`; every value is a dimensionless ratio). **No emergence-class claim headlined. No `clm-`/`def-` minted. No KB/tex leaf, port-register, falsification-ledger or matrix edit — regardless of outcome.**

**Consequences ROUTED to Grant / the auditor lane (this lane surfaces and routes only):**

1. **★The two frozen-criterion defects (§3, §4)** — `SELFTEST-G2b` cannot fire as written, and `G1` fires on 8 non-errors. Both are VOID triggers as frozen. Grant/the auditor own whether the bench is VOID, whether the G1 clause should be restated on the CONSERVATIVE (theorem-grade) pair where it is a genuine theorem, and how the two ambiguous frozen sentences (the G2b latitude, the G1 VOID scope) resolve. **This lane does not amend the frozen prereg and does not pick.**
2. **★The modulus-identity question (§6.1) — now SHARPENED into a THREE-way question by the anisotropy measurement (§6.5), not a two-way one.** The corpus `r_Z` is built on bulk `K`. A normal-incidence impedance carries a LONGITUDINAL modulus — but **the medium is CUBIC (Zener `A = 1.605316` KUBC / `1.330402` SUBC on the cold reference), so "the longitudinal modulus" is DIRECTION-DEPENDENT and is not a single number.** ★**Protocol E launches along `[100]`, so a Protocol-E time-of-flight comparator is `C11 = K + 4C′/3` — NOT the `K + 4C44/3` axis this lane previously mislabelled `C11`, and NOT a VRH isotropic average.** On the theorem-grade CONSERVATIVE bracket at the headline arm the three candidates disagree at the controlling bin edge: `K` `[0.46053, 0.71723]` **STRADDLES** `T1 = 0.5`, `M_[111]` `[0.50778, 0.86626]` **RESOLVES-HIGH**, `C11_[100]` `[0.53990, 0.83129]` **RESOLVES-HIGH**. **A definition question, surfaced with data, sharpened rather than answered, and NOT settled here.**
3. **★The pinned-shell confound (§6.2)** — `51.3 %` of the soft shell is clamped affine under KUBC at the headline geometry, `0 %` under SUBC, strongly route-dependent. A live confound on the KUBC side of every number in this bench family. Reported raw; attribution routed.
4. **★The realized-vs-intensive `φ` labelling (§6.3)** — the size scan compares three different realized composites at one intensive label. Bears on the merged RVE-size gate; **the auditor's to assess, not this lane's to re-open.**
5. **OWED-2 stands entirely untouched.** A `K`-bracket does not dispose of the `ρ` question. Said again so it cannot be quietly counted as closed.
6. **The standing verdicts are NOT moved.** #782 BIN-4 and #796 UNDETERMINED stand exactly as merged, per frozen §5.5 item 1 and item 4. Frozen §5.5 item 3 (`If a bracket RESOLVES-HIGH at T1 on a headline arm: the matched-side reading becomes BOUND-ROBUST`) is **NOT invoked**: it is conditioned on a headline arm's bracket resolving, and on the theorem-grade CONSERVATIVE bracket neither headline arm resolves — quite apart from the VOID.
7. **★#782'S STATED BASIS FOR BIN-4 IS CORRECTED — the consequence that cuts AGAINST the status quo (§BOTTOM LINE, JSON `F5_782_bound_robustness_crosscheck_NOT_FROZEN`).** Merged #782 §7.1 states `only compressed r_Z = 0.466 < 0.5 is bound-robust`, and §5 carries that leg as the macro-side leg of the BIN-4 straddle. **That `0.466` is `√(R_KUBC_core)`, the core estimator, which frozen §2.3 says carries NO bound status.** This lane reproduces it bit-for-bit and measures the same configuration on the bound-carrying WHOLE-CELL modulus: **`0.6098352173422836` — above `0.5`.** Across #782's four `φ_sf` legs, `2` read macro-side on the core estimator and **`0` do on the bound-carrying measure**, with the core estimator sitting below the bound-carrying value at every leg. **So #782's sole bound-robust macro-side reading is not bound-robust; it is estimator-conditional, and the "verdict-controlling cross-class flip" #782 §5 describes does not exist on the bound-carrying measure.** BIN-4's *label* survives (removing a macro-side leg makes the axis more undetermined, not less) but its *stated basis* does not. **This lane mints no bin, edits no merged doc, and does not re-bin #782** (frozen lane fence: `no edit to the merged #782 or #796 result docs regardless of outcome`). The **basis correction is ROUTED** — the second such correction to #782, after the ρ-flags audit.

> **Result-doc provenance.** The bench RUN of the frozen prereg `research/2026-07-28_subc-kubc-bracket_prereg-FROZEN.md` (committed and pushed ALONE at `1288e288`, **BYTE-UNTOUCHED** since, including across the mid-lane interruption disclosed in §7 D-1). Driver `research/drivers/subc_kubc_bracket.py`; JSON `research/drivers/subc_kubc_bracket_results.json`; white figure `research/drivers/subc_kubc_bracket.png`. Engine `src/ave` byte-untouched; Rule-14 reuse of merged #782 and merged #796; deterministic (`346.0 s`; G3 two-full-runs `diff -q` CLEAN, digest `c5fe89f5a95acbc7…`). **G6 reproduces the merged corpus BIT-EXACTLY** (#796 control and painted at `rel = 0`), so the instrument is the shipped instrument. **BENCH STATUS = VOID AS FROZEN on two counts, both criterion-side, both ROUTED**; the bracket is computed and shipped in full but **NOT BANKED**, and no standing verdict is moved. **★SCOPE, repeated: this brackets `K` ONLY — every `r_Z` interval is a `K`-bracket around an ASSUMED `ρ ≡ 1`, the modulus is the BULK `K` and not the P-wave `M = K + 4G/3`, and OWED-2 is NOT discharged.** **★ANISOTROPY, repeated: the medium is CUBIC — `M_*_abs` is the `[111]` longitudinal modulus, NOT `C11`; the `[100]` `C11` is measured separately in §6.5.** **★AND, repeated because it cuts against this lane's own status-quo headline: #782's sole bound-robust macro-side reading does NOT survive on the bound-carrying measure (§8 consequence 7).** Companions: the frozen prereg, merged **#782** (`research/2026-07-21_rve-aggregation-bench_result.md`), merged **#796** (`research/2026-07-22_vessel-state-rve_result.md`), and the docket fragment (`_orchestration/docket-entries/2026-07-28-subc-kubc-bracket.md`).
