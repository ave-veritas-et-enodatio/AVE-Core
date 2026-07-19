# F6 certified-κ recurrence sweep — the SUFFICIENT test of the counting arrow — prereg FROZEN

**Date:** 2026-07-18 (freeze) · **Class:** prereg — **freeze-by-push BEFORE any driver code exists** (ave-prereg Step 3.11).
**Question owner:** Grant-greenlit 2026-07-18 (post-#724 merge; story-2 = the counting arrow, tested where it can finally be asked — at the certified cell).

**Charters (frozen taxonomy CONSUMED, not redefined):**
[`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md) §4 bin **(i) CHANNEL-BOUNDED** (quoted verbatim §4 here) + §5b gate;
[`2026-07-16_f6-circuit-map-fill-PROTOCOL.md`](2026-07-16_f6-circuit-map-fill-PROTOCOL.md) (§5b fill rule);
[`2026-07-16_f6-bath-meter_CHARTER.md`](2026-07-16_f6-bath-meter_CHARTER.md) §A/§B + **§B-post-review R-1 ★SCOPE CAVEAT** + **§C κ-revalidation** + **§C-post-review addendum** (the instrument certificate this sweep consumes).
**Certificate under consumption:** [`2026-07-18_f6-meter-kappa-reval_result.md`](2026-07-18_f6-meter-kappa-reval_result.md) — **METER-VALID-KAPPA-BAND[0.030, 0.030]** at the MILD operating point (§C-post-review VERDICT, lines 22–55 + addendum lines 268–277).
**Prior arm (the falsified NECESSARY-shape run, κ=0.012):** [`2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md`](2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md) + [`…_result.md`](2026-07-18_f6-counting-arrow-arm_result.md) (#722).
**License under test:** [`manuscript/ave-kb/common/retention-transition-split.md`](../manuscript/ave-kb/common/retention-transition-split.md) — the *TRANSITION* crossing-arrow, "licensed **only** from counting … mode-spread with reconvergence ≈ 0 … never a valve."
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler`) — **BYTE-UNTOUCHED**. **Driver (to be written AFTER this push):** `src/scripts/vol_1_foundations/f6_certified_kappa_sweep.py` (may import the #722 arm `f6_counting_arrow_arm.py` + the meter validate `f6_bath_meter_validate.py` — **both BYTE-UNTOUCHED**). §5b probe reused: `f6_counting_arrow_probe.py`.
**Ruling:** `_orchestration/2026-07-10_rulings-docket.md` RULING 19 (tare rule) + ENTRY 17 (counting-arrow arm).

> ★ **FROZEN.** §0–§7 locked before any RESULT or driver. **No retune after fire (Rule 11).** Deviations from this prereg are **findings**, disclosed in the result — never silent, never a KILL→PASS relabel. The collapse `R_return(x)` was **NOT** measured before this freeze; §2's prediction is derived from recurrence physics, not fitted. The classifier tree (§4) is frozen **complete with precedence order** (the #722 R-10 lesson: fire-conditions alone are not a classifier); the shipped driver must implement §4 **byte-faithfully** and the result must carry a byte-faithful cross-check.

---

## §0 Sector header + MODE / REGIME / PHASE-STATE + instrument-certificate SCOPE (mandatory before any substrate claim)

- **Sector:** **E-sector ε-store** — the reactive lattice field energy that is the F6 ε→T2 transfer candidate. **NOT** A1 dilatation-mass, **NOT** Cosserat (2,3) winding/charge. The bath is a **T2 dissipation-sink DOF** (external Foster/Caldeira–Leggett oscillator comb), carrying no winding and no mass; sector-ownership respected (the bath does not confine or hold charge).
- **Mode:** classical reactive TLM lattice (K4, z=3 srs, 4 ports) coupled to an external Foster comb bank (Caldeira–Leggett independent-oscillator bath) via a collar port. Symmetric-leapfrog integrator (the meter's `LatticeBathCoupler.step`).
- **Regime:** **Regime I sub-yield (Phase 1)** — cold, `A_max ≈ 0.10` (MILD; `A² ≈ 2.5e-3 ≪ 2α = 1.46e-2`), at the **strong-but-certified coupling `κ = 0.030` EXACTLY**. Op14 saturation carried only weakly through op3's bond Γ(A) (second-order at this amplitude); no `|Γ|→1` yield wall; no memristive hysteresis (`use_memristive_saturation=False`); no node mint. **NO Phase-2 / near-knee, NO §D, NO other κ** is run in this lane (out of scope, §3).
- **Phase-state:** driven-then-source-off in a **closed cavity** (`pml_thickness=0`, energy-conserving); the scaled broadband seed is the drive impulse, the source is off for the whole recording window (free coupled evolution). Drive protocol / seed / collar are **identical to the certified configuration** (§3).
- **★Instrument-certificate SCOPE (the cell this sweep is allowed to fire in):**
  - **Plant:** **STANDALONE-K4** — *within* the meter certificate (§B-post-review R-1 ★SCOPE CAVEAT: certificate scoped to standalone-K4; energy conservation is an **algebraic identity** on this junction, not an empirical outcome). No `CoupledK4Cosserat`, no ε→T2 depletion primitive is introduced (either BREAKS the identity ⇒ W/X-battery revalidation per the caveat). This sweep consumes the meter **as certified**.
  - **Operating point:** **MILD** (seed `scale = 0.6`, `A_max ≈ 0.10`) — **the certified cell** (§C-post-review: X1–X6 all pass at MILD κ=0.030). κ=0.045/0.060 are OUT (excluded from the certified band by X5/X3); this sweep does **not** touch them.
  - **Coupling:** `κ = 0.030` EXACTLY — the single certified point `[0.030, 0.030]` (§C-post-review VERDICT). No κ-scan.
  - **Meter §A/§B/§C certificates cited:** §A7 METER-VALID-WITHIN-ENVELOPE; §B-post-review METER-VALID-NONLINEAR-ENVELOPE (standalone-K4); §C-post-review METER-VALID-KAPPA-BAND[0.030,0.030] at MILD.
  - **Nyquist envelope:** every comb satisfies `ω_max·dt < π` (`ω_max ≈ 1.0`, `dt = 1.0`; enforced by `OscillatorBath.__post_init__`).
  - **NO meter/engine edits.** The meter module (`f6_bath_meter.py`), the K4 engine, the #722 arm driver, and the meter validate driver are **byte-untouched**. Any needed capability = **FINDING + SPEC**, not a silent edit.

- **Coordinate discipline (A46 / phase-space-coordinate-check):** the corpus claim (mode-count irreversibility) lives in the bath's **modal/spectral** phase-space. The headline observable `R_return` is a **scalar energy-ledger** read (coordinate-free); the collapse variable `x = T_window·Δω/2π` is a **spectral** coordinate — matched to the claim's coordinate. `N_occ` is read per-mode over `{ω_m}` (spectral). No real-space Cartesian φ² surrogate is compared against a phase-space φ² prediction. The one spatial read (§4·8 core-bias) is tared per RULING 19 before comparison.
- **Consistency-vs-emergence tag:** the **FORM** (irreversibility born from a lossless comb; the `2π/Δω` recurrence collapse in `x`; the transition at `x≈1` and nowhere else) is a **substrate-mechanism manifestation** (Class-B / manifestation, **FORM-derived**). The **VALUE** of any emergent input resistance `Re(Z)` is **Class-4 consistency / calibration** — *not* an emergence of `Z₀ = 377 Ω`. No CODATA input reaches a headline target through SI substitution; `Z₀` enters **only** the companion-leg consistency comparison (§6), tagged.

---

## §1 THE QUESTION + FORM/VALUE declaration + honesty flags

**The question (the only load-bearing one — the SUFFICIENT test):**

> The #722 review-probe found the **NECESSARY** counting shape at κ=0.030 (fast transfer, quasi-continuum populating, dense R_cum≈0 with controls passing). **Does the SUFFICIENT signature exist** — do the `R_return(x)` curves, swept over comb density, **COLLAPSE onto one universal curve in `x = T_window·Δω/2π`, with the transition at `x ≈ 1` AND NOWHERE ELSE?** That collapse-at-`x≈1` is the fingerprint that the arrow is a **Poincaré horizon-crossing** (`T_window < T_rec = 2π/Δω`) — irreversibility **by counting**, not by transfer-timescale or by a foreign sink.

The mechanism under test is the corpus's licensed one: *mode-spread with reconvergence ≈ 0 within the window* (`retention-transition-split.md`). A finite comb of `M` equally-spaced oscillators (spacing `Δω`) has an **exact Poincaré recurrence** at `T_rec = 2π/Δω` (all phases `ω_m t = ω_min t + mΔω t` re-cohere when `Δω t ∈ 2πℤ`, independent of `M` and `ω_min`). Energy transferred out **returns** at `T_rec`. So the arrow is a **horizon-crossing**: irreversible *iff* `T_window < T_rec`, i.e. iff the comb is dense enough (small `Δω`) that the recurrence outruns the window. If it is genuine counting, `T_rec` is the ONLY timescale that sets the return, so the curves collapse in `x`.

**FORM/VALUE declaration (frozen):** the sweep tests the **FORM** — the collapse + the transition location `x≈1`. Any emergent real input resistance `Re(Z)` at the recurrence crossing is born from a **lossless comb** (no `Re(Z)` primitive anywhere; §5b no-valve rail); its **VALUE is instrument-calibrated** (κ, weights, density) — this is **NOT** a derivation of `Z₀ = 377 Ω`. The companion leg (§6, secondary/non-gating) makes the mechanism-identity with the lattice's own characteristic impedance explicit at **consistency-class only**.

**Honesty flags (frozen):**
1. **Window-relative arrow = horizon-crossing.** A finite comb is reversible in principle (the recurrence at `T_rec` always returns the energy). The arrow measured here is a **horizon-crossing** (`T_window < T_rec`), the **same epistemic status as radiation resistance** (a matched line looks resistive only until the reflection returns). This sweep does **not** claim thermodynamic irreversibility in the `N,T → ∞` limit; it claims the counting-arrow **exists and collapses in `x`** at the certified cell.
2. **Mechanism-existence rung, NOT the rate rung.** This tests *whether* counting produces the arrow, not the depletion **rate**. `Γ = 3Hρ_latent` (the DE-tracks-matter rate) is **UNTOUCHED**.
3. **Plant = standalone-K4 (certificate valid).** Any future ε→T2 primitive or `CoupledK4Cosserat` front BREAKS the conservation identity ⇒ W/X-battery re-validation per the §B-post-review R-1 caveat.

---

## §2 ★PREMISES CHECKED AGAINST BANKED DATA AT FREEZE TIME (the #722 lesson — NO assumed premises)

The #722 arm at κ=0.012 was FALSIFIED because its two load-bearing premises (fast transfer; populated quasi-continuum) were **assumed, not checked against the banked meter data** — both were in fact derivable-as-FALSE from #721 at freeze time (#722 result R-3). This sweep freezes **only** premises that are **banked at κ=0.030** at freeze time, each quoted with its receipt. *(Each receipt was re-verified against the JSON at freeze; the shipped driver additionally RE-DERIVES every regime number so the fire does not rest on the receipt alone — §6/§4 regime gate.)*

| # | Premise (must hold for the QUESTION to be askable) | Banked receipt @ κ=0.030 (file → JSON path / line, verified at freeze) | Status |
|---|---|---|---|
| P1 | **Fast transfer** (transfer completes well within the recurrence — the τ_transfer ≪ T_rec separation the #722 prereg only ASSUMED) | `…_meter-kappa-reval_result.json → post_hoc_genuineness.selectivity_f2["0.03"]`: per-step `Γ_E = 5.445e-3`, `offset/Γ_E = 101×`; **and** `density_scaling_f4["0.03"].rows[0]` (Δω=0.010, M=71): `Γ_E_first = 5.444e-3`, `Γ_E_slope = 5.217e-3`. Corroborates the #722 review-probe `t63 ≈ 0.19·T_rec` (result §6). **NOTE: the reval F2/F4 reads are POST-HOC / UNFROZEN / NON-GATING** (`post_hoc_genuineness.note`); the `t63` number itself is #722-scratch. ⇒ the driver **RE-DERIVES `t63/T_rec` as the FROZEN regime gate** (§4·REGIME-NOT-REACHED). | **BANKED (post-hoc) + re-derived by driver** |
| P2 | **Quasi-continuum reachable** (many resonant modes populate, not the #722 few-mode 1–3) | `…reval_result.json → battery.results[X2].metrics.per_kappa[κ=0.03]`: resonant `N_occ = n_res = 15` (densest comb, FROZEN X2 leg); `selectivity_f2["0.03"].gamma_k_over_dw_comb = 22.0` (`Γ_κ ≳ Δω_comb` ⇒ comb IS a quasi-continuum, reval F2). | **BANKED (X2 frozen leg + F2)** |
| P3 | **Golden-rule coupling** (genuine resonant coupling, not an amount-matcher / broadband dump) | `density_scaling_f4["0.03"].golden_rule_exponent = 0.934` (`Γ_E ∝ DOS^{0.93}`, Fermi's rule; reval F4). Quiet-comb control `selectivity_f2["0.03"].quiet_collapse = 27604` (a q-power-quiet comb absorbs `≤7.8e-5`). | **BANKED (F4 + F2 quiet-band)** |
| P4 | **Controls certified** (two-tank + sparsest comb return; reversibility live) | `battery.results[X4].metrics.per_kappa[κ=0.03]`: two-tank `R_cum(x=10) = 0.989`, sparse `R_cum(x=10) = 0.890` (both `> 0.70`); `κ_break = 0.09` bounds the band above. | **BANKED (X4 frozen leg)** |
| P5 | **Comb un-dressed** (dressed teeth stay put ⇒ the `x = T·Δω/2π` collapse variable is valid; the #722-demanded level-repulsion check) | `battery.results[X6].metrics.per_kappa[κ=0.03]`: `pulling = 0.0006 ≪ Δω/2 = 0.005` (`9` near-resonant modes; adj-tooth `0.0009`, lattice-line pull `0.0038`). **This is the dressed-comb artifact clearance at κ=0.030** (§7 cite). | **BANKED (X6 frozen leg)** |
| P6 | **Meter valid at the cell** (conservation identity + tare usable at MILD κ=0.030) | `…reval_result.md` §C-post-review VERDICT (lines 22–55) + addendum table (271): X1 drift BOUNDED; X5 tare `c=0.367`, `|c_fit−c|/c=1.6e-2 < 0.02`, spatial residual budget `0.066`. | **BANKED (§C-post-review)** |

**Premise verdict at freeze:** all six premises are **BANKED at κ=0.030** (P1 corroborated by post-hoc reval reads + the #722 scratch `t63`; the driver re-derives `t63/T_rec` and `N_occ` as FROZEN regime gates so the fire is self-certifying, not receipt-dependent). **The QUESTION is askable at this cell.** *(If a regime gate fails at fire time despite the banked receipts, the honest disposition is REGIME-NOT-REACHED — §4 — not a rescue.)*

---

## §3 THE OBSERVABLE + GRID (every value declared; frozen)

### The ledger read (defined exactly — both-field, tare-consistent per RULING 19)

Per step record `E_lat(t) = lat.total_energy()` and `E_bath(t) = bath.energy()` (**both-field**: `E_lat = Σ_p V_inc² + V_ref²`; `E_bath = Σ_m ½p_m² + ½ω_m²x_m²` — the reactance pair, **both** the C-state `Σ½ω²x²` AND the L-state `Σ½p²`, recorded across the window, §6). `E0 = E_lat(post-first-step)` (on-shell; bath empty ⇒ `Etot0 = E0`). Conservation `E_lat(t) + E_bath(t) = E0` is identity-enforced (#721 R-1) and is **audited** (§4 NUMERICAL/DETONATE), so `E_lat` recovery and `E_bath` residual are the **same** ledger read tared consistently.

- `t_peak = argmax_t E_bath(t)` (transfer-complete time; first/global transfer peak). `E_bath_peak = E_bath(t_peak)` = the transferred energy (the return reference).
- **R_return(t)** `= 1 − E_bath(t)/E_bath_peak` for `t ≥ t_peak`, else `0` (transfer incomplete ⇒ nothing has returned). Fraction of the transferred energy back in the lattice ledger.
- **Cumulative return** `R_ret_cum(t) = max_{t_peak ≤ t' ≤ t} R_return(t')` (monotone; "has the energy returned by `t`").
- **`t63`** `= min{ t : E_bath(t) ≥ (1 − 1/e)·E_bath_peak }` (transfer-timescale; the regime-gate observable). `t63/T_rec` at the densest comb is the REGIME gate.
- **`x_50`** `= min{ x : R_ret_cum(x) ≥ 0.5 }` (the **transition midpoint**; `nan` if never). The per-cell collapse coordinate.
- **RULING-19 tare on the ONE spatial read (§4·8):** the protected-core bias is tared by `c = √(1 − E_bath/E0)` before ON-vs-OFF comparison; the spatial residual budget at MILD κ=0.030 is **0.066** (X5 reval receipt, P6). The headline `R_return` is a scalar ledger read (not spatial), so the tare does not gate it.

### THE COLLAPSE VARIABLE

> **`x = T_window · Δω / (2π) = T_window / T_rec`.**

### THE GRID (both knobs; every value enumerated)

**Fixed** across the whole sweep (ENGINEERING CHOICES — tagged; inherited **identical** from the certified configuration): grid `N = 12³`, center `(6,6,6)`, collar `[r_in,r_out] = [2.0, 4.0]`, **`κ = 0.030` EXACTLY**, `ω_min = 0.30`, `dt = 1.0`, `pml_thickness = 0`, seed `SEED = 1`, **seed scale `0.6` (MILD, `A_max ≈ 0.10` — the certified cell)**, `nonlinear = True` + `op3_bond_reflection = True` + `V_SNAP = 1.0`. **Drive protocol:** the scaled broadband seed (`_seed_lattice`, byte-identical to the meter's) is the impulse; `E0` captured post-first-step (on-shell); source off for the whole window (free coupled evolution). This is byte-identical to the #722 arm plant EXCEPT `κ: 0.012 → 0.030`.

**Knob 1 — comb density `Δω`** (reuse the #722 frozen comb ladder, certified; band top held at `ω_max ≈ 1.0`, so `M = round(0.70/Δω)+1`; `ω_max·dt < π` holds for every row):

| `Δω` | `M` | `ω_max` | `T_rec = 2π/Δω` (steps) | run horizon `T_max = 11·T_rec` (steps) | role |
|---|---|---|---|---|---|
| 0.010 | 71 | 1.000 | 628 | 6908 | **densest** (deepest irreversible; the REGIME-gate + X1/X5/X6 primary plant) |
| 0.015 | 48 | 1.005 | 419 | 4607 | dense |
| 0.020 | 36 | 1.000 | 314 | 3455 | dense |
| 0.030 | 24 | 0.990 | 209 | 2304 | production comb |
| 0.050 | 15 | 1.000 | 126 | 1382 | sparse |
| 0.080 | 10 | 1.020 | 79 | 869 | **sparsest** (positive-control edge) |

**Knob 2 — `T_window`.** Read off each single trajectory (one run per `Δω`, `R_ret_cum(x)` sampled every step). For the RESULT table, report `R_return` and `R_ret_cum` at the frozen window points **`x ∈ {0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0}`** (11 points over 2 decades = ≥3/decade; `T_window = x·T_rec` snapped to the nearest recorded step). Every `Δω` run reaches `x = 11 > 10`; the densest reaches `x=0.1` at step 63.

**Positive control (declared separately):** **two-tank** `M=2`, `ω = {0.50, 0.70}` (`Δω = 0.20`, `T_rec = 31.4`), horizon `T_max = 12·T_rec = 377` steps — the cleanest sloshing reservoir (reproduces two-reservoir reversibility; X4-certified `R_cum(x=10) = 0.989` @κ=0.030).

**Negative control (resonance-gating guard; FROZEN placement per §7).** A **detuned comb** placed OFF the plant's own measured q-power content via the FROZEN q-power-budget rule `_place_detuned_band` (`f6_bath_meter_validate.py:560`; `DETUNE_M = 32`, `Δω = 0.030`, `W3_POWER_FRAC_MAX = 1e-2`). It MUST show **negligible transfer** (`peak_frac < E_BATH_MIN = 1e-2`) — confirming the sweep's transfer is **resonance-gated**, not a broadband dump that fills any comb (the #724 F2 lesson: measure resonance-gating in THIS regime, don't assume it). Reproduces the certified X2 placement (×128.7, N_det=0 @κ=0.030).

**OFF control:** `κ = 0` closed cavity — must recover Ax3 (`drift < 1e-10`).

**OUT OF SCOPE (explicit — NOT run in this lane):** Phase-2 / near-knee (`scale ≥ 1.8`); any κ ≠ 0.030; the §D re-certification; any meter/engine edit. Those are separate fires with their own preregs.

### PREDICTION (frozen — derived from recurrence physics, NOT fitted)

1. **Collapse.** All `R_ret_cum(x)` curves (swept over `Δω`) **collapse onto one universal curve in `x`** (the `Δω`-dependence divides out because `T_rec = 2π/Δω` exactly).
2. **Transition at `x ≈ 1` and NOWHERE ELSE.** Each qualifying curve crosses `R_ret_cum = 0.5` at `x_50(Δω)`; `mean(x_50) ∈ [0.7, 1.5]` (the first full recurrence is at `x=1`; the cumulative-0.5 crossing may precede `1` by the dephasing offset `≈ Δω/band` and may follow up to the 2nd recurrence). Collapse quality `spread(x_50) = max(x_50) − min(x_50) < 0.30` (systematic bound `≈ 0.13`; a transition tracking `T_window` rather than `x` would spread `x_50` by the full `Δω` factor `8×`).
3. **Sparse end = full return (built-in positive control).** Two-tank AND the sparsest comb at `x ≫ 1` show `R_ret_cum > 0.70` — reproducing X4-certified reversibility.
4. **Dense/short-window end pins low.** For dense combs (`Δω ≤ 0.03`), `R_return(x = 0.3) < 0.30` — energy transferred but not yet returned (`x < 1`).
5. **Mode-count fingerprint.** `N_occ(dense) > N_occ(sparse)` and `N_occ` at the dense end is a populated quasi-continuum (`≥ 10`, P2), tracking the driven bandwidth not the array size.

If (1)+(2) hold and (3)+(4)+(5) hold with energy conserved, OFF recovering Ax3, core-bias tared-within-tol, and the detuned control gated → **COUNTING-ARROW** (§4). Any other pattern maps to a frozen fail-closed bin (§4).

---

## §4 FROZEN VERDICT CLASSES + THE COMPLETE DECISION TREE WITH PRECEDENCE (the #722 R-10 lesson)

**Rule-11: no retune after any fire.** Every threshold below appears here **BEFORE any code**. The driver must implement the tree **byte-faithfully**; the result carries a byte-faithful cross-check (§ validation). Blow-up = INSTRUMENT. A single mechanism that explains all failures is the discipline working (honest closure).

### Frozen thresholds (all DERIVED / inherited; no tuning)

| Constant | Value | Provenance |
|---|---|---|
| `CONS_TOL` | `1e-3` | door bin (ii); #721 R-1 identity holds ≪ this |
| `T63_GATE` | `0.5` | **DERIVED (regime gate):** the #722 falsification was `τ_transfer ≈ 5·T_rec ≫ T_rec` — the transfer masked the recurrence, so `x_50` tracked `τ_transfer` not `T_rec`. `t63 ≤ 0.5·T_rec` requires the transfer ≥63%-complete by the first **half**-recurrence, so the return at `x=1` is a genuine recurrence of already-transferred energy — the clean `τ_transfer ≪ T_rec` separation #722 assumed but never gated. Banked `t63 ≈ 0.19·T_rec` @κ=0.030 (P1) clears it with ~2.6× margin. |
| `NOCC_GATE` | `10` | **DERIVED (regime gate):** a counting arrow needs a **populated quasi-continuum** (many incommensurate phases to dephase); #722 failed with `N_occ` 1–3 (few-mode). Banked `N_occ = 15` @κ=0.030 densest (P2); `10` = the probe's 15 with ~1.5× margin, comfortably above the #722 few-mode failure. |
| `E_BATH_MIN` | `1e-2` | NULL / no-transfer floor (arm §2; meter §A3); also the detuned-control gate |
| `SPARSE_RETURN_MIN` | `0.70` | arm §2·3 / §C X4: a finite lossless comb recurs exactly ⇒ return → 1; `0.70` allows non-recurring lattice-internal leakage |
| `COLLAPSE_SPREAD_MAX` | `0.30` | arm §2·2 (DERIVED: systematic bound ≈ 0.13; `0.30 ≈ 2.3×`) |
| `TRANSITION_LO, TRANSITION_HI` | `0.7, 1.5` | arm §2·2 (first-substantial-return window brackets `x=1`) |
| `DENSE_PLATEAU_MAX` | `0.30` | arm §2·4 |
| `DENSE_MAX_DW` | `0.030` | combs at/below feed the dense-end checks (arm §3) |
| `OFF_DRIFT_MAX` | `1e-10` | arm §4·6 (OFF recovers Ax3) |
| `BIAS_TARE_TOL` | `0.05` | arm §4·8 (core-bias, tared) |
| `R_HALF` | `0.5` | cumulative-return crossing level for `x_50` |

### Verdict classes (map onto the door taxonomy; consumed, not redefined)

| Verdict | Door bin | Meaning |
|---|---|---|
| **REGIME-NOT-REACHED** | — | a regime gate fails ⇒ the counting regime does not exist in this run ⇒ **the QUESTION is UNASKED; NO physics bin fires** (the #722 κ=0.012 outcome). Instrument/regime artifact, routed — **not** a falsification of the counting physics. |
| **COUNTING-ARROW** | **(i) CHANNEL-BOUNDED** | the collapse exists: curves collapse in `x`, transition at `x≈1` and nowhere else, controls return, mode-count rises, conserved, OFF-Ax3, core-bias tared-OK, transfer resonance-gated. **The SUFFICIENT signature.** |
| **NO-ARROW** | — | `R_return` high across ALL `x` (echo always home *before* the recurrence) — **counting alone does not produce the arrow** in this engine; **route to the click mechanism** (X40), do not rescue. |
| **FOREIGN-EATER** | — | **the FAITHFUL frozen condition (the #722 R-5 lesson):** return-failure **NOT tracking `x`**, evaluated across **THE WHOLE GRID** (no narrowing to a subset of controls). Fires either as (a) any comb fails to return by `x=10` (ten recurrences elapsed — a lossless comb MUST return; failure = a foreign sink ate the echo), OR (b) energy returns but `x_50` does not collapse to `x≈1` (return set by transfer/detuning/foreign, not recurrence). INSTRUMENT-first; fail closed. |
| **NUMERICAL / DETONATE** | (ii) | NaN / energy blow-up / conservation-identity broken (`max_grid |E_lat+E_bath−E0|/E0 ≥ CONS_TOL`) — INSTRUMENT; fail closed. |

### ★THE COMPLETE FROZEN DECISION TREE (precedence order 1→6; the driver implements THIS byte-faithfully)

```
# Aggregates (ALL computed by the shipped driver; banked in result.json):
#   densest  = the Δω=0.010 comb
#   sweep    = the 6-row comb ladder;  dense = {c in sweep : Δω <= DENSE_MAX_DW}
#   max_cons = max over {sweep + two_tank} of max|E_lat+E_bath−E0|/E0
#   t63_over_trec(densest), N_occ(densest), peak_frac(densest)
#   grid_return_min = min over {all 6 sweep combs + two_tank} of R_ret_cum(x=10)
#   x50s = [c.x_50 for c in sweep if isfinite]; spread, mean_x50 from x50s
#   dense_plateau = max over dense of R_return(x=0.3)
#   n_occ_dense = min over dense of N_occ ; n_occ_sparse = sparsest(sweep).N_occ
#   off_drift (kappa=0) ; bias_resid (tared) ; det_ctrl_peak_frac (detuned negative control)

1. if (any NaN) or (max_cons >= CONS_TOL):                      return NUMERICAL/DETONATE
2. if (t63_over_trec(densest) > T63_GATE)
      or (N_occ(densest) < NOCC_GATE)
      or (peak_frac(densest) < E_BATH_MIN):                     return REGIME-NOT-REACHED
3. if grid_return_min < SPARSE_RETURN_MIN:                      return FOREIGN-EATER   # (a) grid-wide, not narrowed
4. if dense_plateau >= DENSE_PLATEAU_MAX:                       return NO-ARROW        # echo home before recurrence
5. collapse_ok    = isfinite(spread) and spread < COLLAPSE_SPREAD_MAX
   transition_ok  = TRANSITION_LO <= mean_x50 <= TRANSITION_HI
   controls_ok    = two_tank.R_cum(10) >= SPARSE_RETURN_MIN and sparsest.R_cum(10) >= SPARSE_RETURN_MIN
   off_ok         = off_drift < OFF_DRIFT_MAX
   mode_count_ok  = n_occ_dense > n_occ_sparse
   bias_ok        = bias_resid < BIAS_TARE_TOL
   det_gated      = det_ctrl_peak_frac < E_BATH_MIN
   if (collapse_ok and transition_ok and controls_ok and off_ok
       and mode_count_ok and bias_ok and det_gated):            return COUNTING-ARROW
6. else:                                                        return FOREIGN-EATER   # (b) returns, NOT tracking x
```

**Precedence rationale (frozen):** (1) ledger sanity precedes all physics — a broken identity invalidates every regime and return read. (2) the regime gate precedes any physics bin — **the #722 lesson: do not fire a physics bin on data where the regime does not exist** (question unasked ≠ counting falsified). (3) grid-wide FOREIGN-EATER precedes the collapse logic — a foreign sink that eats the echo anywhere on the grid is caught **before** any x-collapse read, and is evaluated across the **whole grid**, not narrowed to two controls (the #722 R-5 repair; the #722 shipped tree narrowed it to `sparse_ok` and mis-returned FRICTION-RENAMED). (4) NO-ARROW (echo home before the recurrence) precedes COUNTING. (5) COUNTING requires the **full conjunction** (door bin (i) + the arm-specific collapse). (6) the residual — regime reached, grid returns, dense pins low, but no `x≈1` collapse — is FOREIGN-EATER (returns not tracking `x`, the exact #722 signature).

### ★Door bin (i) CHANNEL-BOUNDED — QUOTED VERBATIM + honest mapping (consumed, NOT redefined)

> **(i) CHANNEL-BOUNDED** — "Transfer ON: energy leaves ε-store into bath; total energy conserved within tol; Hamiltonian / energy norm bounded; OFF recovers reversible Ax3 behavior; **and** bath mode-count / phase-space volume increases (fool-mode-3 pass); protected-core bias and drain within tol" (`2026-07-15_f6-mode-count-door_CHARTER.md:71`).

**Honest mapping (COUNTING-ARROW ⊆ CHANNEL-BOUNDED; no bin redefinition — the #722 AMENDMENT-1 / #724 F7 lesson):**

| bin (i) clause (verbatim) | COUNTING-ARROW evidence | tree conjunct |
|---|---|---|
| energy leaves ε-store into bath | transfer completes fast, `peak_frac ≥ E_BATH_MIN` | regime gate (step 2) |
| total energy conserved within tol | `max_cons < CONS_TOL` (#721 R-1 identity) | step 1 pass |
| Hamiltonian / energy norm bounded | no blow-up / NaN | step 1 pass |
| OFF recovers reversible Ax3 | `off_drift < 1e-10` | `off_ok` |
| bath mode-count / phase-space volume increases (fool-mode-3) | `N_occ` rises toward dense end; `≥10` quasi-continuum | `mode_count_ok` + regime gate |
| protected-core bias and drain within tol | tared core-bias `< 0.05` | `bias_ok` |
| **[arm-specific, ADDED not substituted]** the mode-count increase produces a **counting arrow** | collapse in `x` + transition at `x≈1` | `collapse_ok` + `transition_ok` |

The arm-specific collapse is **ADDED** as the discriminating evidence that the mode-count increase is a genuine *counting* arrow (not mere occupancy) — it does **not** replace or redefine any bin-(i) clause (contrast #722 AMENDMENT-1, where FRICTION-RENAMED substituted a dense-vs-sparse fingerprint for bin-(vi)'s dissipation condition). Only **COUNTING-ARROW** licenses the successor gates (thermometer / spatial-F6); **NO-ARROW**, **FOREIGN-EATER**, **REGIME-NOT-REACHED** are honest negative/unasked closures, routed, **not** retuned.

---

## §5b Circuit map (§5b) — FROZEN (filled pre-freeze per the fill-PROTOCOL)

**Object:** **F6 occupancy chord** (one taxonomy object; kept separate from frontier crystallization and the finished-A1 wall — fill-PROTOCOL Step 0). Probe: `f6_counting_arrow_probe.py` (Phase-1 MILD plant, `A_max≈0.10`). This is the **same cold-baseline probe** the #722 arm filled (`…counting-arrow-arm_prereg_FROZEN.md` §5b) — the collar/regime/port cold reads are κ-independent (the probe is at κ=0.012 cold; the `Γ`-vs-`x` transition is the frozen hypothesis this sweep tests, now at the certified κ=0.030).

| Question | Claim | Cite | Observable / null (measured value + `probe.py:line`) |
|---|---|---|---|
| Ports | collar shell of K4 tetrahedral bond sites; all 4 ports `p0..p3` read via `mean_p(V_inc+V_ref)`; coupling port = collar → Foster comb bank | `f6_bath_meter.py:make_collar_mask` + `read_q`; `k4_tlm.py` 4-port `V_inc[...,p]` | `collar_sites=56`, `ports_read=all_4_K4_bonds`, `pml_thickness=0` (`probe.py:85`) |
| Regime | **cold sub-yield** (Regime I) | envelope-anatomy / Ax-4 kernel; `A²≪2α` | `A_max(collar)=0.0744`, `⟨A²⟩=2.47e-3 ≪ 2α=1.46e-2`, `⟨S⟩=0.99877` (`probe.py:94`) |
| Port behavior (cold baseline) | **matched pass** at the op3 bond front (cold); the `Γ`-vs-`x` transition is the FROZEN HYPOTHESIS | translation-circuit cold≈matched; op3 `z_local=(1−A²)^(−1/4)` | `z_local(collar)∈[1.00005,1.00155]` spread `1.50e-3` (~1.00 matched, cold) (`probe.py:104`) |
| Port behavior (predicted vs `x`) — **the morph this sweep tests** | **sparse: reactive `|Γ|≈1` phase-rotating** (energy reflects back = recurrence within window); **dense: matched-line `Re(Z)` EMERGENT** (energy stays out for `x<1` = counting; radiation-resistance morph) | recurrence identity `T_rec=2π/Δω`; §1 | *frozen prediction, tested by §2 — the SUFFICIENT collapse; NOT a probe read* |
| Energy fate | **in-network reactive, reversibly exchanged with a lossless comb; total conserved** (identity, #721 R-1). Return-vs-window is the observable (§2) | circuit-first "reflection ≠ T2 leave"; #721 R-1 | closed-cavity `|ΔE_lat|/E0=1.87e-15`; comb-on `|Δ(E_lat+E_bath)|/E0=2.28e-15` (`probe.py:124`) |
| A1 protection | interior reversibility protected by **losslessness** (lossless comb + on-shell global rescale); **no `CORE_R` mask, no siphon** — reversibility is the recurrence, not a valve | Ax3 lossless interior; bias≠release | closed-cavity drift `1.9e-15` = the bias≠release control (`probe.py:130`) |
| Forbidden costumes | **not** Re(Z)-dump (`friction=False, β=0`), **not** PML sponge (`pml=0`), **not** face-`V`-scale siphon (back-reaction = global energy-matched rescale), **not** dump-R; the comb is **lossless** — any real impedance is **EMERGENT from counting** | mode-count charter §5b costume row | `friction=False, β=0.0, pml_thickness=0` (`probe.py:136`) |

**★The no-valve rail (frozen):** **no `Re(Z)` element exists anywhere** — the comb is lossless (`bath.damp` production-OFF), the coupling is a symplectic Caldeira–Leggett kick + exact free rotation, the back-reaction is a phase-preserving energy-matched rescale. **Port/regime/Γ-vs-x/energy-fate morph (§5b fill):** the **sparse end → reactive** (`|Γ|→1`, energy reflects back within the window = recurrence), the **dense end → radiation-resistance** (`Re(Z)` EMERGENT from counting, energy stays out for `x<1`). Any real input resistance the port sees is **EMERGENT FROM MODE-COUNTING** (reconvergence outrunning the window), never a dissipative primitive.

**Pre-freeze consistency pass: PASS (1)–(6)** (inherited from the #722 §5b, same cold probe) — cite `f6_counting_arrow_probe.py:85,94,104,124,130,136`. (1) one object (F6 occupancy chord). (2) regime cold (`A²=2.47e-3`) matches label. (3) port cold = matched (`z_local≈1.001`); the `|Γ|→1` wall is the frozen `x`-prediction, not claimed cold. (4) energy fate in-network conserving (`2.28e-15`). (5) A1 protection = losslessness, no parallel `CORE_R`. (6) no killed class (`friction=False, pml=0`, global rescale not siphon).

---

## §6 DIAGNOSTICS PROVENANCE (the #722 F9 lesson: every number BY THE SHIPPED DRIVER, banked in JSON — nothing prose-only) + THE COMPANION LEG

**Every regime/mechanism number is computed by the shipped driver and banked in `2026-07-18_f6-certified-kappa-sweep_result.json`** — nothing prose-only (the #722 R-7 gap this closes at design time):

| number | definition | JSON path |
|---|---|---|
| `t63`, `t63/T_rec` (per comb; densest = the gate) | first step `E_bath ≥ (1−1/e)·E_bath_peak`, over `T_rec` | `sweep[i].t63`, `.t63_over_trec` |
| `N_occ` (per comb) | meter `bath.n_occ()` (absolute floor, spectral) | `sweep[i].n_occ` |
| `x_50` (per comb) | first `x` with `R_ret_cum ≥ 0.5` | `sweep[i].x_50` |
| collapse `spread(x_50)`, transition `mean(x_50)` | max−min / mean over finite `x_50` | `criteria.collapse_spread`, `.mean_x50` |
| drive linewidth `ω_d`, FWHM (re-measured, per comb) | rFFT of collar `q(t)` (mean-subtracted); dominant + half-power width | `diagnostics.cells[i].omega_d`, `.linewidth_fwhm` |
| per-cell `R_return` / `R_ret_cum` tables | the 11-point `x`-grid | `sweep[i].r_return_table`, `.r_cum_table` |
| conservation drift (per comb) | `max|E_lat+E_bath−E0|/E0` | `sweep[i].max_cons_drift` |
| **reactance pair (Rule-10 corollary):** bath C-state `Σ½ω²x²` AND L-state `Σ½p²` across the window (11-point `x`-grid, NOT just at peak) | both reactances at every `x`-point — distinguishes a genuine oscillating bath (C↔L exchange over the window) from a static-caught-at-peak artifact | `sweep[i].ebath_c_table`, `.ebath_l_table` (+ `.ebath_c_at_peak`, `.ebath_l_at_peak`) |
| detuned-control `peak_frac` + placement receipt | `_place_detuned_band` band + q-power frac + `peak_frac` | `detuned_control.*` |

*(PML cell exclusion (A-Rule-10 corollary) is N/A here: `pml_thickness = 0` (closed cavity), and every field read is either a scalar ledger, a spectral bath read (`N_occ`), or the `max` over `mask_active` (core-bias) — no top-K `argpartition` over a PML-bearing grid.)*

**THE COMPANION LEG (SECONDARY — non-gating; opt-in `--companion`; clearly fenced).** Its outcome **CANNOT** change the sweep verdict (§4 rests only on the primary comb-bath sweep). The self-termination size-sweep `N ∈ {8,10,12,16}` uses the lattice's own modes as the reservoir (no external comb): measures `Δω_lattice`, the local return `R_in(t)`, and the emergent input-resistance proxy `Re(Z_in)/Z_char`, and reports the same `x = T·Δω_lattice/2π` collapse across `N`. **Consistency target (VALUE = calibration, stated):** `Z₀ = √(L_bond/C_bond)`. **This is NOT a derivation of `Z₀`** — the ratio is reported at consistency-class; `Z₀`, `Δω_lattice` are instrument-calibrated. (Reused byte-for-byte from the #722 arm `run_companion`.)

---

## §7 CONTROL PLACEMENT + honesty flags (frozen)

- **★Detuned/control-band placement (the #724 CRITICAL lesson).** Any detuned band uses the **FROZEN q-power-budget placement rule `_place_detuned_band`** (`f6_bath_meter_validate.py:560`; the frozen §C X2 rule — "the lowest 32-mode Nyquist band whose measured q-power fraction `< W3_POWER_FRAC_MAX = 1e-2`"), **NOT** the harmonic-avoidance helper `_place_detuned_harmonic_aware` (`:1010`, the #724 F1 manufactured-kill bug — blind to the plant's independent ω≈1.123 line). The negative control (§3) reproduces the certified X2 placement (×128.7 collapse, `N_det=0` @κ=0.030). The `DETUNE_M=32`, `Δω=0.030` probe density is the self-consistent frozen reading (§C-post-review §C-pr1).
- **★X6 pulling clearance = the dressed-comb artifact clearance at THIS κ (P5 cite).** `pulling = 0.0006 ≪ Δω_densest/2 = 0.005` @κ=0.030 (X6 reval, `battery.results[X6].per_kappa[0.03]`) — the dressed teeth stay ≥8× inside the Rayleigh/recurrence ceiling, so the `x = T·Δω/2π` collapse variable is **not** spoiled by level repulsion. This is the certified clearance the sweep inherits; it is **not** re-measured by this driver (the meter certified it), it is **cited** as the premise (P5).
- **Meter tare (RULING 19).** The back-reaction is ~90% uniform amplitude attenuation + ~10% spatial (amount-not-phase). The headline `R_return` is a **scalar** ledger read ⇒ the tare does not gate it. The one spatial read (§4·8 core-bias) is tared by `c = √(1 − E_bath/E0)` before comparison; budget = the MILD κ=0.030 W5 residual `0.066` (P6).
- **FORM-derives / VALUE-imports.** Consistent with the corpus meta-finding: the sweep forces the **FORM** (counting-arrow, collapse, emergent `Re(Z)`); the **VALUE** (`Z₀=377Ω`) is calibration, explicit only at consistency-class in §6.

---

*Prereg only. Nothing here banks COUNTING-ARROW; §2/§3 predictions are derived from recurrence physics and were not measured before this freeze. The classifier tree (§4) is frozen complete with precedence; the driver must implement it byte-faithfully. The RESULT (with Rule-11 honesty on any fail) follows in `2026-07-18_f6-certified-kappa-sweep_result.md`. NO Phase-2/near-knee, NO §D, NO other κ.*

---

## POST-FREEZE AMENDMENT — 2026-07-19 (PR #726 review, 10 confirmed / 0 refuted; disclosures only)

> ★ **The frozen body (§0–§7) above is BYTE-UNTOUCHED.** This amendment is appended AFTER the fire per the RAILS: it discloses (it does **not** retune) the observable-ambiguity resolution and the instrument/spec deviations the review surfaced. The **FROZEN §4 verdict (FOREIGN-EATER) and "the counting-arrow QUESTION is NOT decided" both SURVIVE**; only the *mechanism story* in the result was wrong (rewritten under Rule-12 in the result, not here). Each item below is a **finding**, per the §16 freeze-block rule "deviations are findings, disclosed — never silent."

**A-1 (the observable — resolves the §3 FROZEN ambiguity; Rule-11 disclosed-resolution, NOT a retune).** §3 line "`t_peak = argmax_t E_bath(t)` (transfer-complete time; **first/global** transfer peak)" is a **frozen ambiguity** — it names *two* readings. The originally-shipped driver resolved it to **GLOBAL argmax**, which at κ=0.030 lands on the **post-clamp plateau** (`E_bath ≡ E0` once the scale=0 back-reaction clamp hard-zeroes the lattice; densest global argmax = step 6861, `peak_frac = 1.0000068` = the clamp artifact) ⇒ **`R_return ≡ 0` over the whole physical run, ERASING the signal.** The review's re-derivation from the raw trace found the erased signal: `E_bath` plateaus ~0.994 by `x≈1`, then **DIPS at `k·T_rec`** (14.7% returned at `x≈1.1–1.3`, growing to ~36% at `x≈2–2.5`), delivered by the amount channel (`f6_bath_meter.py:303–305`: `d_e_bath<0 ⇒ scale>1` actively returns energy — the meter **can** return amount). **Resolution (this amendment):** the repaired driver implements the **FIRST-PLATEAU / transfer-complete** reading — the OTHER frozen reading of "first/global". Per the RAILS this is **disclosed-resolution of the prereg's own frozen ambiguity, NOT a Rule-11 retune** (no threshold changed; the §4 tree is byte-identical; only which of the two frozen readings of "first/global" is used). The **superseded global-argmax tables are preserved** in the JSON as `*_global_superseded`, and a parameter-free **dip-vs-running-max** diagnostic is banked alongside. `PLATEAU_PROM = 0.05·E0` is the transfer-complete prominence tolerance for the first-plateau detector (rejects the ≤5% rising-edge ripple, catches the ≥14% recurrence dips).

**A-2 (the clamp is an ABSORBING state — amends §3's ledger read).** §3 defines `E_lat` recovery as the return read, but does **not** disclose that the back-reaction `scale = √(max((E_lat − d_e_bath)/E_lat, 0))` (`f6_bath_meter.py:303`) **hard-zeroes the lattice EXACTLY** when `d_e_bath ≥ E_lat` (`scale = 0 ⇒ E_lat ≡ 0` for the remaining window). Post-clamp `R_return ≡ 0` is therefore **STRUCTURAL (cannot-fail / cannot-return)**, not physics. At κ=0.030 MILD the densest comb clamps at `x = 3.15` (**71%** of its window dead); the Δω=0.015/0.020 combs clamp at `x = 1.17/1.72` (**89%/84%** dead) — **before one recurrence of observation past transfer completes**, so they are **NO-INFORMATION** for the recurrence-return question and are marked so in the JSON (`no_information`). The banked `6.8e-6` densest "conservation drift" is largely **clamp-created**, not integrator error.

**A-3 (§3 horizon rounding deviation).** §3's grid table lists the run horizon as `T_max = 11·round(T_rec)` (densest 6908, sparsest 869). The shipped driver computes `n_steps = round(11·T_rec)` (densest **6912**, sparsest **864**). Deviation disclosed; **immaterial** to the physics (the 4 extra densest steps are all post-clamp / dead). Not fixed in code (the difference is below any threshold); the result prose is corrected to the as-run 6912/864.

**A-4 (the validation self-check is a precedence guard, not the independent check).** §validation's byte-faithful `self_check` **consumes classify()'s own booleans** — it re-derives the verdict from the *criteria dict*, not from the raw trace. It therefore catches precedence/wiring drift **only**; it structurally **cannot** catch an observable-definition bug (exactly the A-1 argmax-gating). The genuinely independent check is the PR #726 review's re-derivation from the raw trace (result §4/§7).

*Amendment records disclosures per §16; verdict class unchanged; body frozen. The corrected-observable RESULT re-derivation is in `2026-07-18_f6-certified-kappa-sweep_result.md` §2–§7 (Rule-12 supersessions marked there).*
