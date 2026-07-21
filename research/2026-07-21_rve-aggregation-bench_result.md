# RVE Aggregation Bench — RESULT (the frozen-bin verdict on Z_bulk,eff/Z₀: does the ensemble homogenize into a macro-cage?)

**Date:** 2026-07-21
**Class:** DERIVATION + lattice-derived research-driver (research-doc; **forms derived, values dimensionless/geometric; mints no `clm-`/`def-`; propagates to no KB/tex leaf**). Resolves the frozen bins of `research/2026-07-21_rve-aggregation-bench_prereg-FROZEN.md`.
**Provenance:** Grant-fired 2026-07-21 (`"kick off the rve aggregation bench"` `[sic]`). THE `N>1` CONSTITUTIVE aggregation half of the two-instrument routing merged **#775** (`research/2026-07-20_deep-rail-kscaling_result.md` §8.2) split the open #767/#770 fork into. Frozen prereg committed + pushed ALONE first (`0cf5f01`-class, COMMIT 1); analytic Leg 5 in `..._derivation.md`; the driver `research/drivers/rve_aggregation_bench.py` (+ `_results.json`, white figure) reuses the #770/#775 `constituent_cage_ensemble.py` primitives, `ave.core.*` read-only, engine BYTE-UNTOUCHED, **reruns BIT-IDENTICAL** (§7.0). Every `[canon]` input content-verified two-method at base HEAD `3d07ceeb`.
**Lane fences:** DERIVATION lane only. Engine byte-untouched; **no** `manuscript/`/`ave-kb/` leaf edit; **no** port-register edit; **no** un-revert; **no** falsification-ledger edit — regardless of outcome (held). Consequence ROUTED to Grant only (the radiative stage-2 is NOT run). Every scan ships its data + code path (the #770 lesson — NO prose-string conclusions).

> **★FROZEN-BIN VERDICT: BIN 4 — REGIME / UNDETERMINED (the macro-cage-vs-matched verdict is NOT lattice-decidable at feasible box size; the CONSTITUTIVE-level confirmation of #775's aggregation-instrument assessment).** The bench is VALIDATED — five of six frozen instrument gates PASS (internal `rel=0.038`; STOP-gate opposite-sign; static-limit cg-tolerance-independence `spread=0.0000`; amplitude-linearity `spread=0.0`; RVE-size `gap=0.014`; Lamé gate `ext/wall=0.029→0`) — but the verdict observable is not resolvable, over-determined by TWO frozen BIN-4 triggers firing on the shipped JSON:
> - **(i) the COLLAPSE CHECK FAILS (watch #7 baked-in):** the two independent routes to `φ` do NOT collapse — `max_rel_disagreement = 0.515` (bulk-only) / `0.742` (symmetric) `≫ 0.30` tol over the overlap band `φ ∈ [0.10, 0.44]`. `φ` is NOT the sole controlling variable — `K_eff` is microstructure-dependent at fixed `φ` (the Voigt-Reuss gap made manifest: route A varies cage size, route B varies spacing; they agree on the CLASS but not the value). Per the frozen §2, the regime CLOSES before the curve is read as effective-medium physics.
> - **(ii) `r_Z` STRADDLES the `0.5` MACRO-CAGE/MATCHED band edge in a verdict-controlling way** — across the `φ` scan (the crash MINIMUM `K_eff/K_0 ≈ 0.16–0.19` at `φ≈0.19–0.28` gives `r_Z ≈ 0.40–0.44`, MACRO-CAGE side; the space-filling end `φ_sf=0.489`, `K_eff/K_0=0.296` gives `r_Z=0.544`, MATCHED side) AND across the pre-stress class (`compressed` `r_Z=0.466` MACRO-side vs `cold` `0.544` / `expanded` `0.568` MATCHED-side — the #779 Leg-C sign flipping the verdict across the band edge).
>
> **★What the bench DOES establish (banked positive characterization, not a null):** the aggregated bulk-only cage array produces a REAL, substantial CONSTITUTIVE compression-softening — `K_eff/K_0` crashes `~5×` above shell-percolation (`φ_perc ≈ 0.09–0.13` geometric) to a minimum `≈ 0.16–0.19`, **well below the Voigt bound (`1−φ ≈ 0.8`) — the cages are NOT bypassed by the matrix.** But it does **NOT reach the catastrophic Reuss/Wood crash (`K_eff/K_0 → 0`) required for a clean MACRO-CAGE** — it plateaus at the intermediate `~0.17–0.30`. The crash is INTERMEDIATE between Voigt and Reuss, and `φ` is not route-controlling, so the class (crash-toward-Reuss = macro-cage vs plateau = matched) is not resolvable at `L=16`. The mechanism NAMED (Leg 5 §2): the coated-sphere-with-SOFT-coating morphology crashes toward Reuss ONLY when the soft shells percolate the load path AND cut the matrix — the lattice reaches shell-percolation but the finite box cannot resolve whether the crash deepens to Reuss at true nuclear packing.
>
> **★Both anti-seduction fences HELD (the #770 lesson NAMED — every scan ships data + code path; verdict cites ONLY frozen-criteria JSON):** MACRO-CAGE (flatters BOTH the Reading-B re-open AND Grant's walked reframe) is NOT declared — `r_Z` straddles `0.5`, the routes fail collapse, and the crash is intermediate (not Reuss). MATCHED/RIGID (flatter the #761→#767→#770 kill-momentum) are NOT declared — a real `~5×` softening exists, `K_eff` sits well below Voigt, and the crash minimum dips into macro-cage territory (`r_Z ≈ 0.40`). **Banked in NEITHER direction.**
>
> **CONSEQUENCE (Rule 11 honest closure): the #767/#770 aggregation fork REMAINS OPEN at the constitutive level; the decisive verdict needs the larger-box / periodic-homogenization instrument #775 flagged as infeasible on this machine class — now CONFIRMED for the CONSTITUTIVE instrument too** (route-collapse fails at `L=16`, exactly as #775's radiative route-collapse failed at `0.833`). This does NOT ground a Reading-B re-open (BIN-1 needs a VALIDATED catastrophic crash + collapse PASS) and does NOT confirm the kill at the aggregation level (BIN-2 needs `0.5<r_Z<2` cleanly with collapse PASS). **Routed to Grant/auditor; NO leaf touched; no rescue derivation minted (Rule 12; slot not refilled).**

---

## §0 — REGIME / SECTOR / PHASE-STATE header

**MODE.** A compact gravitating body; the object = the EFFECTIVE MEDIUM the ensemble of ~`10⁵⁷` bulk-only-caged constituent solitons homogenizes into at scales ≫ core spacing (`electron-bh-isomorphism.md:26` `[canon]`). Contrast column: the textbook bubbly-liquid (Reuss/Wood crash) vs the Voigt/parallel bound. **REGIME.** Regime-I cold-linear STATIC constitutive response — NO drive, NO lock-in, NO radiation port; cages by CONSTITUTIVE GRADING (`S(A)→0` on a `~1`-node shell), NOT a kinematic pin. **PHASE-STATE.** Cold-reactive medium (Ax3-lossless-reactive), saturated cage shells; two pre-stress phase-states (cold rail / radiation-pressurized rail via the `axiom-register.md:193` remap). **SECTOR.** Under test = A1 bulk/compression (`K_eff`) + T2 shear (`G_eff`); mass = A1 dilatation (`master-equation.md:20`); A1⊥T2, NOT cross-wired. **A46 (`phase-space-coordinate-check` PASS):** the corpus claim (the aggregation reframe, walk RECORD §6 seed 3) and the test are BOTH in real-space constitutive + impedance-plane coordinates — matched, NOT a phase-space-vs-real-space mismatch. The discriminator `Z_bulk,eff/Z_0` is the impedance-plane coordinate the corpus's short/open framing (`master-equation.md:107` `Γ_bulk=−1=SHORT`) lives in.

---

## §1 — THE DISCRIMINATOR (frozen; recomputed from the shipped JSON) `[derived]`
`r_Z ≡ Z_bulk,eff/Z_0 = √((K_eff/K_0)·(ρ_eff/ρ_0))` at the space-filling end `φ_sf`. Frozen bins (§2): MACRO-CAGE `r_Z ≤ 0.5` (short) AND `K` falling; MATCHED `0.5<r_Z<2.0`; RIGID `r_Z ≥ 2.0` (open); REGIME `r_Z` flips / collapse or STOP-gate fails. Two ρ readings: PRIMARY engine-native `ρ_eff/ρ_0=1` (acoustic inertia unchanged) ⇒ `r_Z=√(K_eff/K_0)`; COMPANION canon mass-loading `ρ_eff/ρ_0=1+β·φ`, `β∈{0,1,3}` (mass = trapped compression, `master-equation.md:20`; the ontology — is trapped-energy mass acoustic inertia? — is Fork ρ, routed to Grant, §5 prereg).

---

## §2 — LEG 0 (INSTRUMENT VALIDATION — five of six gates PASS) `[derived]`
All read from `rve_aggregation_bench_results.json` `leg0_instrument_validation` (baseline `L=16`, deep rail `S_RAIL=1e-4`).

| Gate | Frozen output | Verdict |
|---|---|---|
| **Internal validation** (KUBC `K_0`,`G_0` vs Bloch `c_P`,`c_S`) | `(K_0+4/3·G_0)/G_0 = 3.16` vs `(c_P/c_S)² = 3.286`, `rel = 0.0385 ≤ 0.20` | **PASS** — the static homogenization recovers the Bloch moduli (`K_0=1.654`, `G_0=0.906`) |
| **STOP-gate** (mirror validity) | rail (bulk-only) `K_eff/K_0 = 0.189, 0.296` (SOFTENS, `<1`); rigid `K_eff/K_0 = 3.1, 1.6` (STIFFENS, `>1`) | **PASS** — OPPOSITE composite-response class confirmed (cavity-softening vs rigid-stiffening); the mirror is valid, lane proceeds |
| **Static-limit / rate** (cg-tolerance independence, DEEP rail) | `K_eff/K_0 = 0.190431 / 0.190437 / 0.190437` across CG tol `1e-4/1e-6/1e-8`, `spread = 0.0000 ≤ 0.02` | **PASS** — the rate→0 static limit is UNIQUE + tolerance-invariant (a linear reactive system; no hysteresis). (Corroborating shallow-rail dynamic ramp `0.208/0.214/0.237`→static `0.245`; the `13%` residual is disclosed explicit-solver under-settling, §7.2, NOT a physics rate-dependence.) |
| **Amplitude linearity** | `K_eff/K_0 = 0.1904` IDENTICAL across `ε = 1e-4/1e-3/1e-2`, `spread = 0.0` | **PASS** — the linear constitutive modulus (amplitude-independent) |
| **RVE-size independence** | `K_eff/K_0 = 0.167 (L12, 8 cages) / 0.190 (L16, 27) / 0.188 (L20, 64)`; `gap(L16,L20) = 0.014 ≤ 0.15` | **PASS** — size-converged (L16/L20 agree to `1.4%`); the ~5× softening is a real effective-medium value, not finite-cluster |
| **Collapse (two-route)** | `max_rel_disagreement = 0.515` (bulk-only) `≫ 0.30` (§5) | **FAIL** — `φ` not route-controlling ⇒ the verdict-determining BIN-4 trigger |

---

## §3 — LEG 1 (SINGLE-CAGE CONSTITUTIVE BASELINE) `[derived]`
Single cage (`r_cage=2.4`) at box center, `L=16` (dilute — one cage in the `L/2` core cube ⇒ weak magnitude, clear SIGN). `leg1_single_cage_baseline`:

| class | `K_eff/K_0` (hydro) | `G_eff/G_0` (shear) | uniaxial |
|---|---|---|---|
| bulk-only, cold | `0.932` | `0.890` | `0.934` |
| bulk-only, **compressed** (pre-stress `ε_pre=−0.08`) | `0.885` | `0.789` | `0.866` |
| bulk-only, **expanded** (`ε_pre=+0.08`) | `0.945` | `0.922` | `0.955` |
| symmetric, cold | `0.817` | `0.667` | `0.783` |

**Reading.** The pre-stress SIGN structure is confirmed at the single-cage level (the #779 Leg-C sign): **compressed `<` cold `<` expanded** (a compressed core SOFTENS `k_s` via the remap ⇒ lower `K`; expanded STIFFENS ⇒ higher `K`); the symmetric wall softens BOTH channels most (also kills shear, `G=0.667`). Magnitude is dilute (weak for one cage in a big cell) — the aggregation (Leg 3) is where the softening accumulates.

---

## §4 — LEG 2 (THE LAMÉ GATE — converged; retroactively adjudicates #770's 0.65) `[derived]`
A single PRESSURIZED cage (interior pinned to a uniform radial expansion, outer boundary `u=0`, the annulus relaxed by preconditioned CG — NO transient). `leg2_lame_gate`:

| class | exterior `∇·u`/wall (mean of 2 shells) | shell-agreement (abs) | converged | Lamé PASS |
|---|---|---|---|---|
| bulk-only, cold | `0.029` | `0.018` | True | **True** |
| bulk-only, compressed | `0.016` | `0.009` | True | **True** |
| symmetric, cold | `0.005` | `0.003` | True | **True** |

**Reading (frozen consistency check, derived-before-measured).** The converged static exterior dilatation `∇·u → 0` (`≈0.03`, `≤0.10`) for all classes — the exterior is PURE-DEVIATORIC-dominated, the **Lamé pressurized-cavity solution `u_r=C/r²` (div-free) CONFIRMED**; the small residual is the finite-box `B·r` term. **★Retroactive adjudication of #770 Leg-1's `0.65`:** the static solve carries NO transient, so the converged exterior-dilatation measurement is STABLE (two shells agree to `0.018` absolute), whereas #770's DYNAMIC window-average swung `0.33→1.60` — confirming (per the frozen `#770/#775` Leg-C1 lesson) that the `0.65` was a TRANSIENT ARTIFACT, not a converged charge fraction. The converged answer is that a pressurized bulk-only cage does NOT leak an exterior compression monopole (it is a clean pressure-release cavity, exterior deviatoric).

---

## §5 — LEG 3 (THE φ SCAN — the centerpiece) + collapse + percolation `[derived]`
`N` cages on a cubic sublattice, NON-OVERLAPPING interiors (`2·r_cage<s`; caps at `φ≈π/6` touching), deep rail `S_RAIL=1e-4`, `L=16`. Two routes to `φ` (A: vary `r_cage` at `s=4.5`; B: vary `s` at `r_cage=1.7`). `leg3_phi_scan`; `K_eff/K_0`:

| `φ` | bulk-only-cold A | bulk-only-cold B | symmetric-cold A | compressed A | expanded A |
|---|---|---|---|---|---|
| `0.075` | — | `0.473` | — | — | — |
| `0.101` | `0.239` | — | `0.129` | `0.180` | `0.259` |
| `0.165` | — | `0.239` | — | — | — |
| `0.188` | `0.189` | — | `0.083` | `0.130` | `0.212` |
| `0.278` | — | `0.164` | — | — | — |
| `0.315` | `0.200` | — | `0.077` | `0.136` | `0.223` |
| `0.441` | — | `0.263` | — | — | — |
| `0.489` (`φ_sf`) | `0.296` | — | `0.149` | `0.218` | `0.322` |

`G_eff/G_0` at `φ_sf` (bulk-only cold) `= 0.671`. **Geometric shell-percolation `φ_perc` = 0.09 (route A) / 0.13 (route B)** (face-connection `2(r_cage+cage_w)=s`).

**★Reading.** `K_eff/K_0` **crashes `~5×` above `φ_perc`** to a MINIMUM `≈0.16–0.19` (both routes) around `φ≈0.19–0.28`, then UPTICKS toward `φ_sf` (`0.26–0.32`) as the cold interiors fill more of the load path near touching. **The crash sits FAR below the Voigt bound** (`1−φ ≈ 0.7–0.9` — the cages are NOT bypassed) **but FAR above the Reuss/Wood bound** (`≈10⁻³` at these `φ` — no catastrophic crash). It is an INTERMEDIATE crash. **The two routes do NOT collapse** (`collapse.max_rel_disagreement = 0.515` bulk-only, `0.742` symmetric `≫0.30`): at matched `φ` they differ by up to `~50–75%` (`φ=0.1`: A gives `0.239`, B-interp `~0.40`) while agreeing on the crash CLASS — the Voigt-Reuss microstructure gap made manifest (`φ` alone does not fix `K_eff`). The symmetric wall crashes deeper (`0.05–0.15`) but also kills shear (wall-class artifact, fenced). The pre-stress axis shifts the whole curve by the #779 sign (compressed lower, expanded higher).

---

## §6 — LEG 4 (VERDICT) + anti-seduction + Leg 5 analytic form `[derived]`
`leg4_verdict`. `r_Z` at `φ_sf=0.489` per class × ρ-reading:

| class | `K_eff/K_0` | `r_Z (β=0)` | `r_Z (β=1)` | `r_Z (β=3)` | bin |
|---|---|---|---|---|---|
| **bulk-only, cold (HEADLINE)** | `0.296` | **`0.544`** | `0.664` | `0.855` | BIN 4 |
| bulk-only, compressed | `0.218` | `0.466` | `0.569` | `0.733` | BIN 4 |
| bulk-only, expanded | `0.322` | `0.568` | `0.693` | `0.892` | BIN 4 |
| symmetric, cold | `0.149` | `0.386` | `0.471` | `0.606` | BIN 4 |

| Leg | Frozen outcome | Decisive step |
|---|---|---|
| **0 — validation** | internal `rel=0.038`; STOP opposite-sign PASS; cg-tol `spread=0.0000`; amp `0.0`; size `gap=0.014`; **collapse FAIL `0.515`** | 5/6 gates PASS ⇒ instrument valid; collapse FAIL ⇒ BIN-4 |
| **1 — single-cage** | pre-stress sign (compressed`<`cold`<`expanded); symmetric lowest | the #779 Leg-C sign, dilute magnitude |
| **2 — Lamé gate** | exterior `∇·u/wall = 0.029 → 0`, converged | Lamé confirmed; #770's `0.65` = transient artifact |
| **3 — φ scan** | `K_eff/K_0` crash `~5×` to `~0.17` min (below Voigt, above Reuss); routes fail collapse `0.515` | INTERMEDIATE crash; `φ` not route-controlling |
| **4 — verdict** | `r_Z=0.544` at `φ_sf`; straddles `0.5` across scan (`min~0.40`) + pre-stress (compressed `0.466`) | **BIN-4 over-determined (collapse fail + `r_Z` straddle)** |

**★Overall frozen-bin verdict: BIN 4 — REGIME/UNDETERMINED.** The instrument is validated but the verdict observable is not lattice-resolvable: (i) collapse fails (`φ` not route-controlling), (ii) `r_Z` straddles the `0.5` MACRO-CAGE/MATCHED edge across the `φ` scan AND the pre-stress class. Verdict invariant across `β` and pre-stress ONLY in the sense that all land BIN-4 (the collapse fail dominates); the physics content is the straddle + the intermediate crash.

**★Anti-seduction fence check (both ways; the #770 lesson NAMED).** (i) The #761→#767→#770 kill arc WANTS a matched/rigid confirm — REFUSED: a real `~5×` `K` softening exists (well below Voigt), the crash min `r_Z ≈ 0.40` dips into macro-cage territory. (ii) The Reading-B / walk reframe WANTS a macro-cage crash — REFUSED: the crash is INTERMEDIATE (not Reuss/Wood `→0`), `r_Z` straddles `0.5`, and the routes fail collapse. **The honest landing is the reopened aggregation gap at the constitutive level, banked in NEITHER direction** — exactly what the fence protects. Every number here is read from `rve_aggregation_bench_results.json` (shipped) via the deterministic driver (shipped); NO prose-string conclusion.

**★Leg 5 (the analytic FORM, `..._derivation.md`).** The coated-sphere-with-soft-coating morphology crashes toward Reuss ONLY when the soft shells percolate AND cut the matrix (§2); below shell-percolation the matrix percolates (Voigt); the dilute slope is finite (matrix shear props isolated cavities, §3). The lattice reaches shell-percolation and confirms the departure from Voigt (`~5×` crash) but CANNOT resolve whether the crash deepens to Reuss at true nuclear `φ→1` (lattice `φ_max≈0.49<1`; the `φ→1` limit is carried by #770's fully-railed homogeneous `c_P→0` result + the Wood form, at DECLARED un-validated scope). The macro-cage-vs-matched class is thus not lattice-decidable — BIN 4.

---

## §7 — Disclosed deviations (the now-standard §-deviations pattern)
- **§7.0 Determinism CONFIRMED.** Two independent full driver runs are **BIT-IDENTICAL** (`diff -q` clean; `DETERMINISM: BIT-IDENTICAL`). Only RNG = `run_c2_speeds(seed=1)` + `omega_max_cold(seed=0)` (both fixed); the static CG (init `u_I=0`) and the dynamic ramp carry no RNG.
- **§7.1 KUBC bound character (Fork B, frozen honest scope).** The kinematic uniform boundary condition gives a STIFF (upper-bound-class) modulus; the interior-`L/2`-core energy reduces but does not eliminate the boundary-layer bias. Per the frozen §3 disclosure: the observed `~5×` crash is bound-robust (the true modulus, bounded above by KUBC, crashes at least as hard); a HOLD would be KUBC-conditional. The intermediate-crash reading is therefore an UPPER bound on `K_eff` — the true `K_eff` could be lower (closer to Reuss), which STRENGTHENS (does not weaken) the "not a clean matched-hold" reading but does NOT convert the intermediate crash to a resolved Reuss crash (the collapse-fail + straddle stand). SUBC/periodic cross-check = owed follow-on (§8), NOT run.
- **§7.2 Deep-rail explicit dynamics under-converge (rate-check §-deviation, disclosed).** The frozen §4 Leg-0 rate check paired a static CG solve with a ramped dynamic relaxation. At DEEP rail (`S_RAIL=1e-4`) the `k_a=1e-4` shell modes are `~100×` slower and explicit dynamics need impractically many hold steps; so the deep-rail static-limit is established by the IMPLICIT preconditioned-CG tolerance-independence (`spread=0.0000` across 4 decades — the definitive gate), and the explicit dynamic ramp was run at SHALLOW rail (`0.03`) where it corroborates directionally (`0.208→0.237` toward static `0.245` as the ramp slows) with a `13%` residual from under-settled soft modes. The physical criterion (the static limit is unique + rate-independent) is definitively met by cg-tolerance-independence; the `13%` is a solver artifact, NOT a physics rate-dependence — disclosed, criterion NOT relaxed post-hoc.
- **§7.3 Overlap regime excluded (frozen grid honesty).** The discrete nearest-center shell model degrades when cage INTERIORS overlap (`2·r_cage>s`) — an early run's high-`φ` uptick past touching was that artifact; the frozen scan is restricted to NON-OVERLAPPING interiors (caps at `φ≈π/6≈0.52`, near-space-filling touching). The true nuclear `φ→1` limit is analytic (Leg 5 + #770), NOT lattice-sampled — disclosed as the load-bearing scope of the BIN-4 verdict (parallels #775's regime gap).
- **§7.4 ρ-ontology (Fork ρ) NOT decided.** `r_Z` is reported under both ρ readings; the ontology (is trapped-energy mass acoustic inertia?) is routed to Grant. The verdict (BIN-4) is invariant across `β` (all land BIN-4 via the collapse fail), so Fork ρ does not control the bin — but it DOES control where in `[0.39, 0.89]` `r_Z` sits, so it is verdict-relevant for any future collapse-passing measurement.
- **§7.5 Single-cage Leg-1 magnitude is dilute.** One cage in the `L=16` `L/2` core cube gives weak ratios (`0.82–0.95`); the SIGN structure (pre-stress + wall-class) is the deliverable, the magnitude is carried by the aggregation (Leg 3). Disclosed.

---

## §8 — Calibration-vs-derived ledger + owed follow-ons
### §8.1 Ledger (`consistency-vs-emergence`)
| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| `K_eff/K_0`, `G_eff/G_0`, `Z_eff/Z_0` | `[derived]` (lattice static homogenization) | dimensionless ratios | MANIFESTATION (lattice) |
| internal `(K+4/3G)/G` vs `(c_P/c_S)²` | `[derived]` (KUBC vs Bloch) | `3.16` vs `3.286` | CONSISTENCY (`K=2G` GR-imported) |
| `ρ*=9.77337` | `[import]` (`ν_Hill=2/7`, `ave.core.constants.N_NU`) | reused from cce, not re-hardcoded | CONSISTENCY (GR-imported `K=2G`) |
| Voigt/Reuss(Wood) reference FORMS | `[derived]` (textbook effective-medium) | the frozen forms the data tests | the FORM (not fit) |
| pre-stress remap `T/ℓ~k_a·ε_pre` | `[canon]`-form (`axiom-register.md:193`) × `[import]` yield strain | sign `ε_pre`-independent | CONSISTENCY (remap at capped tension) |
| the `~5×` intermediate crash + `r_Z≈0.40–0.57` | `[derived]` (lattice) | dimensionless | FORM-UNDETERMINED (BIN-4) |

No emergence-class claim headlined. `α`-CLEAN (the discriminator is a DIMENSIONLESS impedance ratio — the α-circularity lesson: the chord, if any, must be a dimensionless ratio). The deliverable is the BIN-4 regime verdict + the validated instrument + the banked intermediate-crash characterization.

### §8.2 Owed follow-ons (fenced; NOT executed here — Rule 12; slot NOT refilled)
1. **The decisive verdict needs the larger-box / PERIODIC-homogenization instrument** #775 flagged as infeasible on this machine class — now CONFIRMED for the CONSTITUTIVE instrument (route-collapse fails at `L=16`). A periodic-BC homogenization (true effective modulus, microstructure-averaged, between Voigt and Reuss) OR a box `L ≳ O(10²)` would resolve whether the crash deepens to Reuss (macro-cage) or plateaus (matched) at nuclear `φ`. Grant-gated; NO strengthening/revert landed on this lane's basis (BIN-4 grounds neither).
2. **SUBC / lower-bound cross-check (Fork B):** the KUBC upper-bound crash is bound-robust; the SUBC/Reuss lower bound would tighten the class. Owed before any "structurally unreachable"-class strengthening.
3. **The ρ-ontology (Fork ρ)** + the **pre-stress sign (Fork P)** are Grant-adjudicated substrate-ontology inputs (is trapped-energy mass acoustic inertia? is the electron core net-compressed?) — surfaced with file:paths + verbatim content, NOT reframed. They set where `r_Z` sits within the straddle band.
4. **The RADIATIVE consequence** (star-scale Lloyd cancellation at `k·R_star`) is stage-2 radial-solver territory — ROUTED to Grant, NOT run (the bench settles the CONSTITUTIVE half only; per the frozen scope fence, IF a future collapse-passing measurement lands MACRO-CAGE, THAT feeds the radial-solver stage-2).

---

> **Result-doc provenance.** Fired by Grant 2026-07-21 (`"kick off the rve aggregation bench"` `[sic]`). Frozen prereg committed + pushed ALONE first (COMMIT 1); analytic Leg 5 (`..._derivation.md`); driver `research/drivers/rve_aggregation_bench.py` (+ `_results.json`, white figure), reuses #770/#775 `constituent_cage_ensemble.py` primitives, `ave.core.*` read-only, engine byte-untouched, **reruns bit-identical** (§7.0). All `[canon]` citations content-verified two-method at base `3d07ceeb`: `electron-bh-isomorphism.md:26`, `master-equation.md:20/107`, `axiom-register.md:193`, `ave.core.constants.N_NU`. **Attribution:** Grant-verbatim fire + the CONSTITUTIVE reframe (walked, ratified); the KUBC static-homogenization primitive, the collapse-check-baked-in protocol (watch #7), the STOP-gate-as-composite-response-sign, the Lamé gate, and the two-ρ-reading fork are this lane's. **★Verdict: BIN 4 — REGIME/UNDETERMINED** — the instrument is validated (5/6 gates PASS) but the macro-cage-vs-matched verdict is not lattice-decidable (collapse fails `0.515`; `r_Z=0.544` straddles the `0.5` edge across the scan + pre-stress); a real `~5×` intermediate `K`-crash is banked (below Voigt, above Reuss); the #767/#770 aggregation fork REMAINS OPEN; the decisive instrument (periodic/larger-box) is #775-flagged infeasible, now confirmed at the constitutive level. Consequence routed; no leaf touched; no rescue minted. Companions: the frozen prereg, the analytic Leg 5 (`..._derivation.md`), merged **#775** (`research/2026-07-20_deep-rail-kscaling_result.md` §8.2), merged **#770** (`research/2026-07-20_constituent-cage-ensemble_result.md` §8.2), the walk RECORD (§6 seed 3), **#779** (`research/2026-07-21_boundary-strain-amplitude_result.md` §3 `[branch:#779]`), the collapse-check watch (`_orchestration/skill-candidates-watch.md` #7), the port register P9/Q1, and the docket continuation (`### ENTRY 2026-07-21-rve-aggregation-bench`).
