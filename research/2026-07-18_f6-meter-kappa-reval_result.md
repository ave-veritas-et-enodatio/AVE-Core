# F6 bath meter — κ-revalidation (X-battery) — RESULT

**Date:** 2026-07-18 · **Class:** result (honest closure; Rule 11)
**Charter (FROZEN):** [`2026-07-16_f6-bath-meter_CHARTER.md`](2026-07-16_f6-bath-meter_CHARTER.md) **Amendment §C** — frozen-by-push `2026-07-18T07:21:52Z` (API committedDate; pushed `07:22:26Z`), **before any X-battery code**.
**Driver:** `src/scripts/vol_1_foundations/f6_bath_meter_validate.py --x-battery` (opt-in; A-battery V1–V6 + W-battery W1–W6 paths **byte-untouched**).
**Data:** `2026-07-18_f6-meter-kappa-reval_result.json` · **Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` — **BYTE-UNTOUCHED**).
**Plant:** standalone-K4 (within the #721 R-1 certificate scope). **Sweep gated on this reval** (counting-arrow follow-on-3; #722 result §6).

> ## ★ VERDICT — **METER-INVALID-AT-KAPPA**
>
> **Banked (frozen §C3):** the meter is **INVALID across the whole tested band `κ ∈ {0.030, 0.045, 0.060}`** — a KILL fires at **every** band κ: `{0.03: [X2], 0.045: [X2, X5], 0.06: [X2, X3, X5]}`. The **certified band is EMPTY**; the **κ-sweep is BLOCKED pending a meter redesign** (SPEC'd in §5, **NOT built** — §C3).
>
> **★The single mechanism (Rule 11 — one root explains every failure).** The strong coupling that *reaches* the counting-arrow regime (fast transfer, quasi-continuum populated — #722) also **FULLY DISCHARGES the cavity into whatever comb is attached** (`E_bath_peak ≥ E0`, `min E_lat/E0 = 0` at every band κ). One fact, three deaths: **X2** the discharge is broadband so the detuned comb absorbs **as much as** the resonant comb (collapse ×1.0–1.5 ≪ the ×100 soul-check) — the transfer is no longer resonance-gated; **X3** the same coupling broadens the lines until the off-resonant sea (`1.7e-2`) climbs above the absolute floor (`1e-2`) at κ=0.06; **X5** full transfer drives `E_bath→E0` so the tare `c=√(1−E_bath/E0)→0` degenerates. **The regime the sweep NEEDS and the regime the meter's weak-coupling discriminators FAIL are the SAME regime.**
>
> **★The feared risk is DISCONFIRMED (X1).** The §C1 secular-pump risk did **NOT** materialize: the total-energy drift is **BOUNDED** (round-off-walk; `≤ 6.8e-6`, curvature `a₂<0` saturating, `|r|≤0.78` non-monotone) — **not** a secular pump, at **every** (κ, point). The algebraic-identity structure (#721 R-1) holds even through the over-extraction clamp; the identity break stays `≤ 6.8e-6 ≪ R_BATH_MAX·transfer = 0.2`. The meter's **conservation** survives; its **discriminators** do not.
>
> **Controls + comb integrity SURVIVE (X4, X6):** the two-tank + sparse-comb reversibility controls return (`R_cum > 0.70`) at every band κ, and the dressed-comb level-repulsion is negligible (`pulling ≤ 0.0006 ≪ Δω/2 = 0.005`) — proving the failure is specifically the meter's **discriminators**, not a dead coupling, a numerical blow-up, or a hybridized comb. The two-tank **κ_break = 0.09** (earlier than the "known by 0.12" ceiling) bounds the band from above independently.
>
> **NOT banked:** any counting-arrow result. No arm/door/sweep fired. The depletion-rate rung (`Γ=3Hρ_latent`) is untouched. The #721 κ=0.012 certificate is untouched (this lane only tests κ=0.03–0.06).

---

## 1 · Sector header (result-time restatement)

- **Sector:** R7 thermal / entropy-sink (T2). **Regime:** driven-then-source-off, standalone-K4, **strong-coupling** (κ=0.03–0.06, vs the certified κ=0.012). **Phase-state:** MILD (Phase-1 sweep point, `A_max≈0.10`; band-determining) + MODERATE (`A_max≈0.30`; stress). **Coord (A46):** `N_occ`, collapse, and mode-pulling read in the bath's modal/spectral coordinate; drift is a scalar ledger read.
- **Consistency-vs-emergence:** every reading is **consistency-class** (does the meter's read survive at the new κ?). Nothing banked at emergence-class. The verdict is a **meter certificate bound**, never an F6 result.

---

## 2 · Measured vs frozen thresholds (per leg, per κ) — the fire

**MILD is band-determining; MODERATE (X1/X5) is the stress cross-check.** Frozen thresholds applied verbatim, no retune (Rule 11).

### X1 — drift anatomy (densest comb, N_sweep = 6908 steps) — **PASS** (feared pump DISCONFIRMED)

| κ · point | `proj\|slope·N\|/transfer` | `realized/transfer` | curvature `a₂` | `r` | label | transfer_frac | KILL (ceil 0.2) |
|---|---|---|---|---|---|---|---|
| 0.03 · mild | 8.2e-6 | 6.8e-6 | −1.8e-5 | +0.78 | BOUNDED | 1.0000068 | **False** |
| 0.03 · moderate | 5.7e-5 | 4.7e-5 | −1.2e-4 | +0.78 | BOUNDED | 1.0000473 | **False** |
| 0.045 · mild | 7.2e-8 | 1.6e-7 | −3.0e-7 | +0.47 | BOUNDED | 1.0000002 | **False** |
| 0.045 · moderate | 1.2e-7 | 2.7e-7 | −4.9e-7 | +0.47 | BOUNDED | 1.0000003 | **False** |
| 0.06 · mild | 4.8e-8 | 1.9e-7 | −2.2e-7 | +0.35 | BOUNDED | 1.0000002 | **False** |
| 0.06 · moderate | 7.2e-8 | 2.9e-7 | −3.3e-7 | +0.35 | BOUNDED | 1.0000003 | **False** |

Every drift fraction is `≥ 6 orders under` the `R_BATH_MAX = 0.2` ceiling; `a₂ < 0` (saturating, curvature bends the drift *back* toward zero); `|r| ≤ 0.78` (not the monotone one-sign accumulation of a pump). **NOT SECULAR at any (κ, point).** Over-extraction anatomy (reported, not a KILL — §C1-i, faithful to the frozen §C X1 criterion): `min E_lat/E0 = 0` and `E_bath_peak/E0 ≥ 1` at every point — the cavity **fully discharges** into the bath, and the identity still holds to `≤ 6.8e-6`. See §4.

### X2 — detuning soul-check (densest comb, MILD) — **LOST at all κ** ★

| κ | `E_bath_peak` resonant (`N_occ`) | detuned band | `E_bath_peak` detuned (`N_occ`) | **collapse ×** (frozen ≥100) | verdict |
|---|---|---|---|---|---|
| 0.03 | 2.14 (15) | [1.07, 1.38] | 1.40 (4) | **×1.5** | **LOST** |
| 0.045 | 2.14 (23) | [1.07, 1.38] | 1.94 (6) | **×1.1** | **LOST** |
| 0.06 | 2.14 (33) | [1.07, 1.38] | 2.14 (9) | **×1.0** | **LOST** |

Robust `ω_d = 0.520` (bath mode-energy peak); detuned band harmonic-aware (`harm_clear = 0.030` from all folded `n·ω_d ∈ {0.52,1.04,1.56,2.08,2.60,3.12}`; §B W3 corrected rule). The detuned comb absorbs **as much as** the resonant comb (`N_det = 4→9 > 0`; the frozen soul-check requires `N_det = 0` and collapse `≥ 100`). At the certified κ=0.012 detuning collapsed the transfer **3.5 orders**; at κ=0.03–0.06 it collapses it **not at all** — the transfer reverts to an **amount-matcher** (the F-1 failure mode the meter was rebuilt to avoid).

### X3 — N_occ honesty (production comb) — floor **DISHONEST at κ=0.06**

| κ | `ω_d` | FWHM (modes) | off-resonant sea `p90` | floor `1e-2` honest? | `N_occ(M=32,64,90)` | M-inv | detuned→0 |
|---|---|---|---|---|---|---|---|
| 0.03 | 0.527 | 0.060 (3) | 7.2e-3 | **True** | [7,7,7] | True | True |
| 0.045 | 0.527 | 0.060 (3) | 9.2e-3 | **True** | [9,9,9] | True | True |
| 0.06 | 0.527 | 0.060 (3) | **1.7e-2** | **False** | [17,17,17] | True | True |

Coupling-broadening lifts the off-resonant sea above the absolute floor at κ=0.06 (`sea_p90 = 1.7e-2 ≥ 1e-2`); `N_occ` climbs 7→9→17 as the sea enters the count. The floor is **NOT re-tuned to rescue** (Rule 11); a κ-broadening-aware floor is SPEC'd (§5). At κ=0.03/0.045 the floor is still honest (sea below floor); M-invariance and detuned-rejection hold at all κ.

### X4 — controls + κ_break (two-tank + sparse) — **PASS** (κ_break = 0.09)

| κ | two-tank `R_cum(x=10)` | sparse `R_cum(x=10)` | pass (>0.70) |
|---|---|---|---|
| 0.03 | 0.989 | 0.890 | ✅ |
| 0.045 | 0.992 | 0.834 | ✅ |
| 0.06 | 0.996 | 0.793 | ✅ |

Two-tank break scan `{0.03:0.989, 0.06:0.996, 0.09:0.000, 0.12:0.000, …}` ⇒ **κ_break = 0.09** (first κ with `R_cum ≤ 0.70`) — **earlier than the "known by κ=0.12" ceiling**; bounds any certified band above at `κ_hi < 0.09`. (Bit-consistent with the #722 probe: two-tank 0.996, sparse 0.793 at κ=0.06.)

### X5 — tare residual vs κ (densest comb) — **degenerate**

| κ · point | `c=√(1−E_bath/E0)` | `c_fit` | `\|c_fit−c\|/c` (frozen <0.02) | resid | usable |
|---|---|---|---|---|---|
| 0.03 · mild | 0.367 | 0.361 | 1.6e-2 | 0.066 | ✅ (budget grows from W5's 0.026) |
| 0.03 · moderate | 0.366 | 0.306 | 1.6e-1 | 0.200 | ❌ (match > 0.02) |
| 0.045 · mild/mod | **0.000** | 0.000 | — | — | ❌ **OVER-TRANSFER** (c degenerate) |
| 0.06 · mild/mod | **0.000** | 0.000 | — | — | ❌ **OVER-TRANSFER** (c degenerate) |

Full transfer (`E_bath/E0 → 1.0000…`) drives `c → 0` at κ≥0.045, degenerating the tare scalar. Per §C X5 the over-transfer is a **FINDING, not a silent (vacuous `|0−0|/0`) pass** — the gate fails on it. The tare is usable only at κ=0.03 mild (resid 0.066, the spatial budget growing with κ).

### X6 — dressed-comb / level-repulsion (densest comb, MILD) — **PASS** (comb integrity survives)

| κ | `pulling = max\|ω_dressed−ω_bare\|` (near-res) | adj-tooth diff | lattice-line pull | artifact (ceil 0.005) |
|---|---|---|---|---|
| 0.03 | 0.0006 | 0.0009 | 0.0038 | **False** |
| 0.045 | 0.0002 | 0.0004 | 0.0038 | **False** |
| 0.06 | 0.0002 | 0.0004 | 0.0038 | **False** |

Robust `ω_d = 0.520` (9 near-resonant modes at every κ). The dressed teeth stay `≥ 8×` inside the `Δω/2 = 0.005` ceiling; the lattice line pulls only `0.0038 < 0.005`. **The comb the prereg sweeps survives the dressing** — the sweep's `x = T·Δω/2π` collapse variable is not spoiled by level repulsion. (The failure is X2/X3/X5, not comb hybridization.)

---

## 3 · The single mechanism (one root, every failure — Rule 11 honest closure)

> **One fact.** At κ=0.03–0.06 the coupling is strong enough that the cavity **fully discharges into whatever comb is attached** — `E_bath_peak/E0 ≥ 1` and `min E_lat/E0 = 0` at **every** band κ and operating point. This is the same fast, near-complete transfer the #722 probe found reaches the counting-arrow regime (`x_63 = 0.19·T_rec`, quasi-continuum populated). Every failure is downstream of it:

- **X2 (soul-check lost).** A full discharge is a **broadband** transient (a near-impulse in time), so it fills a properly-placed, harmonic-avoiding **detuned** comb (`E_det ≈ 2.1 ≈ E0`) just as much as the resonant comb (`E_res = 2.1`). The transfer is **no longer resonance-gated** — the meter reverts to the **amount-matcher** it was rebuilt to escape. This is the load-bearing genuineness certificate (§A8/§B) dying: it was a **weak-coupling** phenomenon.
- **X3 (floor dishonest at κ=0.06).** The same strong coupling broadens the resonant line's wings, lifting the off-resonant sea (`1.7e-2`) above the fixed absolute floor (`1e-2`); `N_occ` inflates 7→17.
- **X5 (tare degenerate).** Full transfer ⇒ `E_bath → E0` ⇒ the tare `c = √(1 − E_bath/E0) → 0` — the computable spatial tare (RULING 19) is undefined in the full-discharge regime.

**What SURVIVES pins the root as the discriminators, not the plant.** X1 (drift bounded, identity holds to `≤6.8e-6` — the algebraic-identity structure of #721 R-1 is κ-robust); X4 (the two-tank + sparse controls return — the coupling is live and reversible where the comb is sparse); X6 (level repulsion negligible — the comb is un-dressed). So the coupling is **live, reversible-where-sparse, and un-hybridized** — the meter's **conservation** is intact; only its **weak-coupling discriminating reads** (resonance-gating, absolute floor, amplitude tare) break.

**Regime read (regime-discipline).** This is **not** a numerical failure and **not** a dead coupling — it is a genuine **regime boundary**: the counting-arrow regime and the meter-discriminator-failure regime **coincide**. You cannot reach the strong-coupling quasi-continuum the sweep needs without the same coupling dumping the whole cavity into any comb (killing resonance-gating), broadening the lines (killing the floor), and fully transferring (killing the tare). **The sweep is blocked at the instrument level, not the plant level.**

---

## 4 · Drift slope anatomy — SECULAR vs BOUNDED (the §C1 decisive read)

The §C1 discriminator was the **slope over the sweep's longest horizon** (`N_sweep = 6908`), not the drift magnitude. Verdict at **every** (κ, point): **BOUNDED (round-off-walk), NOT SECULAR.**

- **Signed drift** is tiny and **saturating**: `signed_end ≤ +6.8e-6`; curvature `a₂ < 0` (opposite sign to the drift — the curve bends back toward zero, the signature of a bounded walk, not an accelerating pump); `|Pearson r(signed drift, step)| ≤ 0.78` (the one-sign monotone accumulation of a pump would give `|r| → 1`).
- **Projected `|slope|·N_sweep / transfer`** (the load-bearing gate) `≤ 5.7e-5`, and **realized** `≤ 6.8e-6` — both `≥ 6 orders` under `R_BATH_MAX = 0.2`.
- **Over-extraction sub-mode (§C1-i), REPORTED as anatomy:** the `max(·,0)` clamp fires and the cavity fully discharges (`min E_lat/E0 = 0`, `E_bath_peak ≥ E0`), but the identity break it creates is bounded by the residual `E_lat` at clamp-fire — which **shrinks** as the discharge completes faster at higher κ. Hence the drift is **NON-monotone (decreasing) in κ**: `6.8e-6 @0.03 → 1.6e-7 @0.045 → 1.9e-7 @0.06` (mild). Per the frozen §C X1 criterion the over-extraction KILLs only if it pushes the drift past `R_BATH_MAX·transfer` (it does not) — so X1 **PASSES**, and the feared secular pump is **DISCONFIRMED**.

**★Flag-don't-fix vs the #722 scratch probe (both readings stated).** #722 §6 quoted "drift `1e-14@0.012 → 6.8e-6@0.03 → 4.3e-4@0.06`." This banked reproduction **confirms `6.8e-6 @0.03`** but measures **`1.9e-7 @0.06`** (not `4.3e-4`) — the drift **decreases**, not increases, with κ, for the mechanism above (faster discharge ⇒ clamp fires at smaller residual `E_lat` ⇒ smaller over-creation). The #722 scratch `4.3e-4@0.06` is a review-probe number with no shipped provenance; it is **superseded at the result level** by this banked measurement (same class as the counting-arrow R-3/R-7 scratch-provenance supersession). Both stated per Rule 11; **the verdict does not turn on this number** (X1 passes on either reading — the conservation is intact; X2/X3/X5 carry the INVALID).

---

## 5 · Redesign SPEC (METER-INVALID-AT-KAPPA ⇒ SPEC, do NOT build — §C3)

The sweep is blocked pending a meter redesign. The redesign is **SPEC'd here as a finding, NOT built** (§C3; engine + meter module byte-untouched). A κ-honest meter must restore the three broken discriminators without re-breaking conservation:

1. **Resonance-gating at strong coupling (restores X2 — the load-bearing one).** The global energy-matched rescale dumps the whole cavity into any attached comb, so off-resonance transfer is not suppressed. Candidate: a **rate-limited / per-mode-capped** back-reaction (cap the per-step transfer so the cavity cannot fully discharge in a broadband burst), or a **phase-returning** coupling (return bath phase, not just amount — the A1 "amount-not-phase" limitation is what makes the dump indiscriminate). Either is a **meter-mechanism change** requiring its own charter + W/X-revalidation.
2. **κ-broadening-aware occupancy floor (restores X3).** Replace the fixed absolute `FLOOR_ABS = 1e-2` with a floor that scales with the *measured* coupling-broadened linewidth (e.g. floor = `k × sea_p90`), so `N_occ` counts resonant modes above the κ-lifted sea. Must be DERIVED, not tuned.
3. **Over-transfer-robust tare (restores X5).** The amplitude-ratio tare `c = √(1 − E_bath/E0)` degenerates as `E_bath → E0`. Candidate: an **incremental / rate** tare accumulated over the transfer, well-defined through full discharge.

**OR** (the cheaper route if it exists): find a **(κ, comb, horizon)** operating point that reaches the quasi-continuum **without** full discharge — but the #722 evidence pins the regime to κ=0.03–0.06, exactly where full discharge occurs, so this may not exist. **SPEC only; Grant adjudicates the redesign-vs-abandon fork.**

---

## 6 · Disposition (Rule 12 — retract, do not refill)

- **Retract** the implicit premise (from the #722 follow-on-3 routing) that the κ-sweep is merely "the cheapest follow-on gated on a routine meter re-run." The re-run is **not routine**: the meter is **INVALID at the sweep's own regime**. The κ-sweep is **BLOCKED**.
- **Do NOT refill the slot** with a new unverified hypothesis. The redesign (§5) is **SPEC only** — it earns its own charter + verification chain if pursued.
- **Untouched:** the #721 κ=0.012 certificate (this lane tests only κ=0.03–0.06); the depletion-rate rung (`Γ=3Hρ_latent`); the meter module + engine (byte-untouched).
- **Routed to Grant:** the redesign-vs-abandon fork (§5) and the sweep-launch decision (now **negative** for κ=0.03–0.06 as-is).

---

## 7 · §C deviations disclosed (per-leg deviation-is-a-finding, §C3 / Rule 11)

Two shipped operationalizations were corrected **before banking** so the reported numbers are lattice-derived and artifact-free (regime-discipline: a null where the effect can't exist = artifact, not falsification). Neither is a threshold retune; both are disclosed:

1. **X1 code-to-frozen-spec fix.** The first shipped `clamp_drain` boolean KILLed on full cavity discharge (`min E_lat/E0 → 0`); the **frozen §C X1 criterion** KILLs only if the identity break (drift) reaches `R_BATH_MAX·transfer` (it does not — drift ≤6.8e-6 ≪ 0.2). Corrected to the frozen criterion; over-extraction is **reported anatomy**, not an independent KILL. **The drift numbers are identical between the two runs** — only the KILL boolean changed (first run KILLed X1 spuriously; corrected run PASSES X1 per the frozen text). Not a rescue: the frozen criterion always PASSED X1.
2. **X2/X6 ω_d robustness (artifact removed).** The first run read `ω_d` from the collar-q rFFT, which collapses to DC (`ω_d → 0`) at κ≥0.045 because the cavity fully drains (`q → 0`) — a window-averaging artifact that mis-placed the X2 detuned band (overlapped resonance ⇒ spurious `N_det`, ratio) and gave X6 trivial `n_near=0` passes. Corrected to a **drain-robust `ω_d` = bath mode-energy peak** (the bath retains the transferred energy). Post-fix `ω_d = 0.520` is stable at all κ; **X2 LOST and X6 PASS both hold on the valid measurement** — the artifact did not manufacture the verdict (X2 was already LOST at the one κ with a valid first-run placement, κ=0.03 ratio ×10).
3. **X1 drift vs #722 scratch (flag-don't-fix; §4)** — both readings stated; verdict independent of the discrepancy.

No frozen §C threshold was loosened. A single mechanism explains every failure (§3) — the discipline working at full strength (honest negative closure).

---

## 8 · Gates + freeze margin

- **Freeze margin (real):** §C frozen-by-push at `2026-07-18T07:21:52Z` (API committedDate; pushed `07:22:26Z`), **before any X-battery code existed**. First battery-code commit: this commit (see git log; the margin is the push→first-code interval, reported in the PR).
- **Gates:** `ruff check` clean; `make verify` green; A-battery **V1–V6 byte-identical** (re-ran `METER-VALID-WITHIN-ENVELOPE`) and W-battery **W1–W6 byte-identical** (regression green — the X-battery is additive, opt-in `--x-battery`, A/W functions AST-identical to origin/main).
- **Byte-untouched:** `src/ave/thermal/f6_bath_meter.py` (meter module) and the engine — verified `git diff origin/main` empty on the meter module. The only edits: the charter §C (append-only, 70 insertions/0 deletions above byte-identical) and `f6_bath_meter_validate.py` (X-battery additions + the `--x-battery` dispatch line).

*Honest closure (Rule 11): clean negative, single mechanism named (strong-coupling full-discharge → resonance-gating + floor + tare all break in the counting-arrow regime), branch closed, redesign SPEC'd not built. Nothing banked at emergence-class. The meter is **METER-INVALID-AT-KAPPA** across κ=0.03–0.06; the counting-arrow κ-sweep is **BLOCKED pending a meter redesign**; the feared secular-pump risk is **DISCONFIRMED** (conservation is κ-robust; the discriminators are not).*
