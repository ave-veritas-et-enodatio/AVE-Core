# Deep-Rail k-Scaling — RESULT (the frozen-bin verdict on ρ_N(k·r_core), the gravitational-sector survival measurement)

**Date:** 2026-07-20
**Class:** DERIVATION + lattice-derived research-driver (research-doc; **forms derived, values calibration/observation-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). Resolves the frozen bins of `research/2026-07-20_deep-rail-kscaling_prereg-FROZEN.md`.
**Provenance:** Grant-fired 2026-07-20 (`"word"`, item-2 `"Proceed"` `[sic]`). THE decisive adjudicator discharging merged **#770** §8.2 (which discharges #767 §6.2-1). Frozen prereg committed + pushed ALONE first (`41fbf1e7`); analytic Leg A + the regime-gap in `..._derivation.md`; the driver `research/drivers/deep_rail_kscaling.py` (+ `_results.json`, white figure) reuses the #770 machinery (`constituent_cage_ensemble.py` primitives), `ave.core.*` read-only, engine BYTE-UNTOUCHED. Every `[canon]` input content-verified two-method at base HEAD `d3203d37`.
**Lane fences:** DERIVATION lane only. Engine byte-untouched; **no** `manuscript/`/`ave-kb/` leaf edits; **no** port-register edit; **no** un-revert; **no** falsification-ledger edit — regardless of outcome (held). Consequence ROUTED to Grant only.

> **★FROZEN-BIN VERDICT: BIN 3 — MIXED / FORM-UNDETERMINED.** The decisive lattice measurement — the RADIATIVE `ρ_N(k·r_core)` (Leg K, driven + lock-in) — **cannot discriminate the frozen candidate forms**, and the frozen BIN-3 triggers fire directly on the shipped JSON: **(a) the two independent routes to `k·r_core` FAIL to collapse** (`route_collapse.max_rel_disagreement = 0.833 ≫ 0.30` tol) ⇒ `k·r_core` is NOT the controlling variable on the lattice; **(b) the accessible band is resonance-dominated** — the radiative `ρ_N` is NON-MONOTONE across `k·r_core ∈ [0.9, 5.9]` (values `0.26 … 2.90`, straddling the first cage-cavity resonance `k·r_core ≈ π`), no frozen form is discriminated (`F0_const` is min-AICc only as a least-bad NULL over the scatter, `RSS_log = 6.41`; the free power `p = −0.32 ± 0.68` is UNRESOLVED / consistent with 0; the Lloyd `F2 (k·r)²` is DISFAVORED, `ΔAICc = 8.47`). **Mechanism NAMED (Leg A §2, Fork R): the deep-rail (`Γ_bulk ≈ −1`) cage is a HIGH-Q RESONANT CAVITY at `k·r_core ~ O(1)`; the lattice samples the RESONANT regime, NOT the sub-resonant quasistatic regime (`k·r_core ≪ π`) where the Lloyd `(k·r_core)²` law holds. The two regimes are on OPPOSITE SIDES of the fundamental cage resonance; the physical system (`k·r_core ~ 10⁻²⁵`) is deep quasistatic, the lattice cannot reach it on a feasible box.**
>
> **★Both anti-seduction fences HELD (the #770 fabricated-`"ROBUST…pressure-tested"`-string lesson NAMED — every scan here ships its data + code path; the verdict cites ONLY frozen-criteria JSON outputs, no prose-string conclusion):**
> - **NOT a kill (BIN-2 SCALING-FLAT is NOT satisfied):** the RADIATIVE `ρ_N` is NOT `k`-independent within any tolerance — it swings `0.26 → 2.90` non-monotonically and the routes fail to collapse. The clean plateau `~0.33` belongs to the STATIC texture control (the mass, EXPLICITLY untouched by the image per walk §6-3), which is FENCED from the radiative verdict (prereg §0 A46; Fork O). So the `78×` floor is NOT confirmed at the radiative level; the kill does NOT bank clean at the k-scaling level.
> - **NOT a suppression (BIN-1 SCALING-SUPPRESSED is NOT satisfied):** the Lloyd `F2` is DISFAVORED by the lattice data (`ΔAICc = 8.47`), no positive power is resolved (`p = −0.32 ± 0.68`), and the `F2` extrapolation (`9.5×10⁻⁵²`) is MEANINGLESS because `F2` fails the fit. The `(k·r_core)²` suppression exists ONLY in the analytic quasistatic Leg-A form, which the lattice — being in the RESONANT regime — can neither validate nor refute. The lattice DISFAVORING `F2` is EXPECTED (wrong regime), NOT a refutation of Lloyd.
>
> **CONSEQUENCE (Rule 11 honest closure): the fork #767/#770 left open REMAINS OPEN; the decisive measurement is NOT lattice-accessible in the quasistatic regime.** This does NOT ground a Reading-B re-open (BIN-1 needs a VALIDATED suppression) AND does NOT earn the "structurally unreachable" strengthening (BIN-2 needs a clean `k`-independent RADIATIVE plateau). **What WOULD resolve it (stated exactly, prereg §5):** reach `k·r_core ≪ π` (sub-resonant quasistatic) with a radiation sponge thicker than the (long) wavelength — a box `L ≳ O(10²–10³)`, infeasible on this machine class — OR a spherically-symmetric continuum radial solver that reaches the quasistatic limit analytically-cleanly (a different lane). The analytic Leg A carries the quasistatic form (`p = 2`) at DECLARED un-validated scope; the aggregation fork (does `p` survive the ensemble sum?) is un-settled. **Routed to Grant/auditor; NO leaf touched. No rescue derivation minted (Rule 12; slot not refilled).**

---

## §0 — REGIME / SECTOR / PHASE-STATE header

**MODE.** Compact binary source (HT, J0737); the object = the ENSEMBLE of ~`10⁵⁷` constituent solitons, each canonically carrying a bulk-only `Γ_bulk=−1` knot-core cage (`electron-bh-isomorphism.md:26` `[canon]`). **REGIME.** Regime-I cold-linear far field; DEEP-RAIL caged sources (`S_RAIL ≤ 1e-4`, `Γ_bulk ≤ −0.95`), constitutive grade (no kinematic pin). **PHASE-STATE.** Cold-reactive far field; the far-field radiation port emulated by an outer graded-damping SPONGE (Ax3 loss channel). **SECTOR.** Under test = A1 bulk/compression (radiative P-branch); observed GW = T2 shear; charge/spin = `(2,3)` Cosserat winding — A1⊥T2, NOT cross-wired. **A46:** the verdict coordinate is the RADIATIVE (drive-frequency) longitudinal/transverse partition; the Lloyd claim suppresses the RADIATIVE moment ONLY, the static texture (mass) is untouched (walk §6-3) — so the driven radiative `ρ_N` is the verdict observable, the static-release `ρ_N` (leg5) the fenced texture control.

---

## §1 — THE SURVIVAL THRESHOLD (frozen; recomputed from the banked numbers) `[derived-from-import]`
`κ_max² = δ_DP = 1.3×10⁻⁴` (double-pulsar binding, Kramer 2021 `[import]`); uncaged baseline `κ_env² = 0.034` (#767 `[canon]`). Survival requires the ENSEMBLE radiative coupling clear the bound:
$$\rho_N^{\rm survive} \le \kappa_{\max}^2/\kappa_{\rm env}^2 = 1.3\times10^{-4}/0.034 = 3.82\times10^{-3}.$$
The deep-rail STATIC-texture plateau `ρ_N ~ 0.33` (§5) gives `κ_ensemble² = 0.33·0.034 = 0.011 = 87×` over the bound; survival needs the RADIATIVE `ρ_N` fall by `≥ 87×` — the `(k·r_core)^p` scaling is the only route. **The measurement of that scaling is the whole lane.**

---

## §2 — LEG W (wall-depth ladder — the SOLID antecedent) `[derived]`
`run_c2_speeds` reuse; frozen `S_RAIL` ladder `0.03/0.003/1e-4/1e-6/0`, both classes (JSON `legW_rail_ladder`):

| `S_RAIL` | bulk-only `Γ_bulk` | bulk-only `c_S` | bulk-only `1+Γ_shear` (shear transmission) |
|---|---|---|---|
| `0.03` | `−0.512` | `0.218` | `0.764` |
| `0.003` | `−0.784` | `0.183` | `0.764` |
| `1e-4` | `−0.956` | `0.177` | `0.764` |
| `1e-6` | `−0.9955` | `0.177` | `0.764` |
| `0` (canon wall) | `−0.9997` | `0.1768` (**FINITE**) | `0.764` |

⇒ **the canon bulk-only wall IS realizable** (`Γ_bulk → −1` with `c_S` finite, `canon_bulk_only_wall_realizable = True`) — the #770 review-repair finding reproduced under freeze. This is the ANTECEDENT the k-scan needs (a real `Γ_bulk=−1` cage exists); it is the ONE clean, solid empirical result of this lane. Symmetric `c_P/c_S` stays `1.813` (degree-0 grade-lock, `electron-bh-isomorphism.md:38`). Bulk-only shear transmission is a flat `0.764` (`Γ_shear` saturates `−0.236`) — the intrinsic wall shear-pass the Leg-S gate must not mistake for a cage effect.

---

## §3 — LEG K (the centerpiece: RADIATIVE `ρ_N(k·r_core)`, driven + lock-in) `[derived]`
Deep rail `S_RAIL=1e-4`, `N=1` isolated core, `L=24`, harmonic radial body-force compression drive (curl-free: `drive_transverse_frac = 3.7×10⁻³²`), outer sponge radiation-port, lock-in of the `r_meas`-shell radial displacement at `Ω` (JSON `legK_driven_kscan_s1e-4`). `k·r_core = Ω·r_cage/c_P,cold`.

| route | `k·r_core` | radiative `ρ_N` | energy-drift `|ΔH/H|_win` | admissible (`≤0.30`) |
|---|---|---|---|---|
| Ω (`r_cage=1.6`) | `0.925` | `0.851` | `0.834` | ✗ |
| Ω | `1.388` | `0.496` | `0.389` | ✗ |
| Ω | `2.004` | `1.023` | `0.132` | ✓ |
| Ω | `2.775` | `0.377` | `0.059` | ✓ |
| Ω | `4.009` | `0.438` | `0.027` | ✓ |
| Ω | `5.859` | `1.705` | `0.073` | ✓ |
| r (`Ω=0.65`) | `1.253` | `2.897` | `0.132` | ✓ |
| r | `2.004` | `1.023` | `0.132` | ✓ |
| r | `2.756` | `0.330` | `0.132` | ✓ |
| r | `3.758` | `0.264` | `0.165` | ✓ |
| r | `4.761` | `2.312` | `0.132` | ✓ |

**Frozen model comparison (AICc, admissible points pooled — JSON `legK…fit`):** `F0_const` AICc `2.95` (min, but `RSS_log=6.41` — a least-bad NULL over the scatter, NOT a resolved plateau); `Fp_free_power` `p=−0.32±0.68` (UNRESOLVED, consistent with 0), AICc `7.47` (`ΔAICc=4.52`); `F2_lloyd (k·r)²` AICc `11.42` (`ΔAICc=8.47`, DISFAVORED); `Fap_plateau_power` AICc `15.15` (`ΔAICc=12.21`). **Route-collapse (frozen consistency check): FAILS** — `max_rel_disagreement=0.833`, `mean=0.384`, `collapses_within_tol=False` (tol `0.30`) over the overlap `k·r_core ∈ [2.00, 4.76]`. **Convergence probe:** `ρ_N` settle-stable (`Δρ_N=0.0006` between `settle=5` and `7` crossings) but the absolute drift is high (`0.26`) — the ratio converges while the sponge under-absorbs (the reason the low-`k` points are inadmissible).

**Deep cross-check `S_RAIL=1e-6` (JSON `legK…s1e-6_xcheck`):** `ρ_N(k·r_core) = 0.496 / 0.377 / 0.440` at `k·r_core = 1.39 / 2.78 / 4.01` — bit-for-bit essentially identical to `1e-4` (`0.496 / 0.377 / 0.438`) ⇒ the radiative measurement is already saturated at deep rail; deeper rail does not change it (the wall is `Γ_bulk ≈ −1` at both).

**★Reading (frozen).** The radiative `ρ_N` is a RESONANCE COMB (values `0.26 … 2.90`, `ρ_N > 1` where the cage cavity amplifies near `k·r_core ≈ π` and again near `~4.8`), NOT a monotone `(k·r_core)^p` fall and NOT a flat plateau. The routes fail to collapse ⇒ `k·r_core` is not the controlling variable on the lattice. Both are the direct signatures of Fork R (Leg A §2): the lattice is IN the resonant regime.

---

## §4 — LEG C1 (converged charged-line) + LEG S (shear diagnosis) `[derived]`
**Leg C1 (deep rail `S_RAIL=1e-4`; JSON `legC1_converged_charged_line_s1e-4`):** the exterior DC `∇·u` is **NON-CONVERGED** by the frozen window-half criterion — half-disagreement `0.65` (bulk-only), `1.23` (uncaged), `0.91` (symmetric), ALL `> 0.25`. Same failure class as #770 Finding 3 (its Leg-1 swung `0.33→1.60`). **Fall back to the frozen BINARY discriminator only:** exterior `∇·u` does NOT `→ 0` — bulk-only/uncaged ratio `= 0.646` (charged line, BIN-1 shape), symmetric/uncaged `= 0.164`. The converged charge-fraction is NOT establishable on `L=24`; only the binary (the line IS charged) survives — CONFIRMING #770's retraction of the `0.65` as a converged number (the coincident `0.646` is itself unconverged).

**Leg S (shear-gate diagnosis BEFORE gating; JSON `legS_shear_diagnosis_s1e-4`):** `σ_N = F_shear^caged/F_shear^uncaged` is heavily contaminated: **N-dependent** (`σ_N = 0.47 / 0.79 / 0.78 / 1.00` for `N=1,2,4,8` — rising toward full coupling at `N=8`) AND **strongly near-field-dependent** (`σ_N = 1.58 / 0.78 / 0.37` at `r_meas = 6 / 7.5 / 9` for `N=4`). The intrinsic wall shear-transmission at deep rail (Leg W) is a flat `0.764`. ⇒ **the shear consistency gate is NOT cleanly applicable on the lattice** — the `0.60×/0.23×` #770 readings are near-field + N artifacts, not a clean cage suppression; there is no single `σ_N` to gate on. (The DRIVEN `σ_N` is uninformative — the radial compression drive is curl-free (`3.7×10⁻³²`), so the driven shear ratio is a ratio of numerical noise; fenced, gate uses the static Leg-S.) This inapplicability is itself a BIN-3 contribution.

---

## §5 — STATIC texture control (the untouched mass; FENCED from the verdict) `[derived]`
Static-release `ρ_N` (leg5 reuse; JSON `static_texture_control_s1e-4`). Walk §6-3: the static texture (`∝M`) is EXPLICITLY untouched by the image — so its plateau is EXPECTED and does NOT test Lloyd (prereg §0 A46; Fork O).
- **Aggregation `ρ_N(N)`** (deep rail): `0.235 → 0.308 → 0.349 → 0.335` for `N=1,2,4,8` — a plateau `~0.33` (matches #770's `~0.3` deep-rail static plateau; `κ_ensemble² = 0.33·0.034 = 87× κ_max²`). This is the MASS, real and uncancelled — the thing that gravitates.
- **Two-route `k·r_core=r_cage/σ` check:** Route-σ `ρ_N = 0.345→0.259` (falling weakly with `k·r_core`), Route-r `ρ_N = 0.180→0.289` (rising) — the two routes do NOT collapse (e.g. at `k·r_core≈1`: `0.340` vs `~0.18`), CONFIRMING the static observable is ALSO not a clean function of `k·r_core`. Fenced: this plateau is the texture, not the radiative Lloyd test.

---

## §6 — FROZEN-BIN VERDICT + anti-seduction + Leg A form

| Leg | Frozen outcome | Decisive step |
|---|---|---|
| **W — rail ladder** | bulk-only `Γ_bulk→−1`, `c_S` finite `0.177`; canon wall realizable = True | the SOLID antecedent (a real `Γ_bulk=−1` cage exists) |
| **K — radiative `ρ_N(k·r_core)`** | resonance comb `0.26…2.90`, non-monotone; routes FAIL collapse (`0.833>0.30`); no form discriminated (`F0` least-bad null, `Fp p=−0.32±0.68`, `F2` `ΔAICc=8.47`) | **route-collapse failure + resonance-domination ⇒ FORM-UNDETERMINED** |
| **C1 — charged-line** | NON-CONVERGED (half-disagreement `0.65`); binary only: line IS charged (`0.646`) | converged charge-fraction not `L=24`-establishable (confirms #770 F3) |
| **S — shear gate** | `σ_N` near-field- (`1.58→0.37`) + N- (`0.47→1.00`) contaminated; gate NOT cleanly applicable | the `0.60×/0.23×` readings are artifacts, not a clean cage effect |
| **A — analytic Lloyd** | quasistatic `p=2` (`ρ_N∝(k·r_core)²`) — the FORM the lattice cannot reach | Fork R: lattice in RESONANT regime, physical system in QUASISTATIC |

**★Overall frozen-bin verdict: BIN 3 — MIXED / FORM-UNDETERMINED.** The decisive lattice measurement cannot discriminate the frozen forms; the frozen BIN-3 triggers (routes fail collapse; resonance-dominated band; no form discriminated) fire on the shipped JSON. The mechanism is the REGIME GAP (Leg A §2): a deep-rail cage is a high-Q resonant cavity at `k·r_core~O(1)`, so the lattice samples the resonant regime, not the sub-resonant quasistatic regime where the Lloyd `(k·r_core)²` holds.

**★Anti-seduction fence check (both ways; the #770 lesson NAMED).** (i) The #761→#767→#770 KILL arc WANTS a clean `k`-independent floor (BIN-2) — the data REFUSE it: the RADIATIVE `ρ_N` is non-monotone (`0.26…2.90`) and the routes fail collapse; only the FENCED static texture plateaus. (ii) The walk's Lloyd picture WANTS suppression (BIN-1) — the data REFUSE it too: `F2` is DISFAVORED (`ΔAICc=8.47`), no power resolved, the extrapolation meaningless; the suppression lives ONLY in the un-validatable analytic quasistatic form. **The honest landing is the reopened regime gap, banked in neither direction** — exactly what the fence protects. Every number here is read from `deep_rail_kscaling_results.json` (shipped) via the deterministic driver (shipped); NO prose-string conclusion (the #770 `"ROBUST…pressure-tested"` fabrication, named and avoided).

**★Leg A (the analytic form, DECLARED un-validated scope).** `..._derivation.md §1`: the pressure-release image / soft-sphere cancellation gives the per-core residual radiative moment `∝ (k·r_core)²` (`p=2`) in the sub-resonant quasistatic limit; §2 states the regime gap (why the lattice cannot validate it); the aggregation fork (does `p` survive the ensemble sum, or does an uncancelled coarse-grained texture emerge?) is un-settled. Extrapolated to `k·r_core~10⁻²⁵`, `F2` gives `ρ_N~10⁻⁵⁰` — but this is analytic, NOT lattice-validated, and does NOT settle aggregation ⇒ NOT a BIN-1.

---

## §7 — Disclosed deviations (the now-standard §-deviations pattern)
- **§7.0 Determinism CONFIRMED (post-commit, at the branch tip).** Two independent full driver runs are **BIT-IDENTICAL** (`deep_rail_kscaling_results.json` run1 ≡ run2, `diff -q` clean), and the shipped JSON equals that reproduced output. Re-verified at the branch tip after the merge-forward past #772/#774: those merges touched NO driver dependency (`git diff` on `ave.core.chiral_lattice` / `srs_band_survey` / `srs_vector_band_survey` / `constituent_cage_ensemble.py` / `ave.viz.style` / `ave.core.constants` = empty; only `ligo_ringdown_driver.py` changed, unused here), and a fresh spot-check at the tip reproduces the exact floats to 12 decimals (`spectral cP/cS=1.812836294696`, `legW γ_bulk(s=0)=−0.999730521790`, driven `ρ_N(Ω=0.90)=0.376945058323`, driven `drift=0.059169341101`). The only RNG is `run_c2_speeds(seed=1)` + `omega_max_cold(seed=0)` (both fixed); the dynamics carry no RNG.
- **§7.1 Energy-drift `|ΔH/H|_win` reported for EVERY driven config** (JSON, per-point) — the twice-dropped #770 deliverable, now shipped. It is the OPEN-system driven-window swing (the sponge radiation port + the harmonic drive pump work); it is the reason the low-`k` (longest-wavelength) points are inadmissible (the finite sponge under-absorbs when the wavelength exceeds its thickness). The `ρ_N` RATIO converges w.r.t. settle-time (`Δρ_N=0.0006`) despite the high absolute drift (both arms drift alike).
- **§7.2 Drive transverse fraction reported** (`drive_transverse_frac = 3.7×10⁻³²`) — the radial compression drive is curl-free by construction; the compression channel is cleanly isolated; the driven shear ratio is therefore uninformative (fenced; the shear gate uses static Leg S).
- **§7.3 Box / regime scope (Fork R, the load-bearing honest scope).** `L=24` reaches only `k·r_core ~ O(1)`, straddling the fundamental cage resonance `k·r_core≈π`; the quasistatic regime (`k·r_core~10⁻²⁵`) is NOT lattice-accessible. This is not a defect to fix but the physical regime gap — stated as the BIN-3 mechanism, not papered over.
- **§7.4 `N=1` verdict class for the driven leg (declared feasibility).** The driven ensemble (`N=4`) does not fit the sponge + shell inside `L=24`; the driven verdict is on the isolated single core (the Leg-A per-core Lloyd test). The `N`-scaling (aggregation) is carried by the STATIC leg5 ensemble (`ρ_N~0.33` plateau, §5) + the analytic Leg-A aggregation fork. Disclosed; the ensemble RADIATIVE k-scaling remains the un-accessed measurement (owed-follow-on §8).
- **§7.5 Leg C1 non-convergence** (half-disagreement `0.65 > 0.25`) — reported honestly; binary discriminator only. **§7.6 Leg S gate inapplicability** (near-field + N contamination) — reported; no clean gate value.

---

## §8 — Calibration-vs-derived ledger + owed follow-ons
### §8.1 Ledger (`consistency-vs-emergence`)
| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| `κ_max²=1.3×10⁻⁴` / threshold `ρ_N≤3.82×10⁻³` | `[derived]` (`=δ_DP`; arithmetic) | `[import]` (Kramer 2021) / `[canon]` `κ_env²` | manifestation given import |
| bulk-only `Γ_bulk→−1`, `c_S` finite (Leg W) | `[derived]` (railed Bloch speeds) | `Γ_bulk:−0.51→−0.9997`; `c_S=0.177` | CONSISTENCY — canon wall realizable (#770-parity) |
| Lloyd form `ρ_N∝(k·r_core)²`, `p=2` (Leg A) | `[derived]` (image/soft-sphere theorem) | `p=2` | the quasistatic FORM — un-validated on lattice (regime gap) |
| radiative `ρ_N(k·r_core)` (Leg K) | `[derived]` (lattice driven lock-in) | resonance comb `0.26…2.90`; routes fail collapse | FORM-UNDETERMINED (resonant regime) |
| static texture plateau `ρ_N~0.33` | `[derived]` (leg5) | dimensionless | the MASS (untouched texture) — fenced |
| pulsar exclusion (banked) | — | `[import]` | import (banked #761/#767/#770/q1) |

No emergence-class claim headlined. The deliverable is the BIN-3 regime-gap verdict + the SOLID Leg-W antecedent, riding on lattice measurement + the analytic Leg-A form, not a hidden calibration.

### §8.2 Owed follow-ons (fenced; NOT executed here — Rule 12; slot NOT refilled)
1. **The decisive measurement is NOT lattice-accessible in the quasistatic regime.** To empirically discriminate the frozen forms one must reach `k·r_core ≪ π`: a box `L ≳ O(10²–10³)` (sponge thicker than the long wavelength) — infeasible on this machine class — OR a spherically-symmetric continuum radial-acoustic solver reaching the quasistatic limit (a DIFFERENT lane, new prereg). The ENSEMBLE (`N>1`) RADIATIVE k-scaling (aggregation of the per-core residual) is the specific un-accessed measurement. Grant-gated; auditor lands no strengthening/revert on this lane's basis (BIN-3 grounds neither).
2. **Leg A's quasistatic `p=2` + aggregation fork** become a NEW analytic derivation with its own version + verification chain IF pursued (Rule 12; not minted here). The re-open of the reverted Q1 ruling is Grant's alone; #767's "structurally unreachable" strengthening is NOT earned (BIN-3 ≠ BIN-2). This lane surfaces + routes; the auditor lands any KB/port-register/ledger edit — this lane touched NO leaf.
3. **Fork W (which `Γ` a knot core presents to each channel; A1⊥T2 sector-ownership)** — unchanged from #770; the `k_a`-only surrogate used here is canon-realizable (Leg W); the mode/geometry mechanism remains un-derived, routed to Grant.

---

> **Result-doc provenance.** Fired by Grant 2026-07-20 (`"word"`, item-2 `"Proceed"` `[sic]`). Frozen prereg committed + pushed ALONE first (`41fbf1e7`); driver `research/drivers/deep_rail_kscaling.py` (+ `_results.json`, white figure), reuses #770 `constituent_cage_ensemble.py` primitives, `ave.core.*` read-only, engine byte-untouched, **reruns bit-identical** (determinism check §-provenance). All `[canon]` citations content-verified two-method at base `d3203d37`. **★Verdict: BIN 3 — MIXED / FORM-UNDETERMINED** — the decisive RADIATIVE `ρ_N(k·r_core)` cannot discriminate the frozen forms (routes fail collapse `0.833>0.30`; resonance-dominated band; no form discriminated); the mechanism is the REGIME GAP (deep-rail cage = high-Q cavity at `k·r_core~O(1)`; the quasistatic Lloyd regime is not lattice-accessible); both anti-seduction fences held (banked in NEITHER direction); the #767/#770 fork REMAINS OPEN; the decisive measurement is routed to Grant with the exact range/precision/box that would resolve it. Consequence routed; no leaf touched; no rescue minted. Companions: the frozen prereg, the analytic Leg A (`..._derivation.md`), merged #770 (`..._constituent-cage-ensemble_result.md` §8.2), the walk RECORD (§6-3), q1 §2.2, the port register P9/Q1, and the docket continuation (`### ENTRY 2026-07-20-deep-rail-kscaling`).
