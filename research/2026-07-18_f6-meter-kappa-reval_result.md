# F6 bath meter — κ-revalidation (X-battery) — RESULT

**Date:** 2026-07-18 · **Class:** result (honest closure; Rule 11)
**Charter (FROZEN):** [`2026-07-16_f6-bath-meter_CHARTER.md`](2026-07-16_f6-bath-meter_CHARTER.md) **Amendment §C** — frozen-by-push `2026-07-18T07:21:52Z` (API committedDate; pushed `07:22:26Z`), **before any X-battery code**.
**Driver:** `src/scripts/vol_1_foundations/f6_bath_meter_validate.py --x-battery` (opt-in; A-battery V1–V6 + W-battery W1–W6 paths **byte-untouched**).
**Data:** `2026-07-18_f6-meter-kappa-reval_result.json` · **Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` — **BYTE-UNTOUCHED**).
**Plant:** standalone-K4 (within the #721 R-1 certificate scope). **Sweep gated on this reval** (counting-arrow follow-on-3; #722 result §6).

> 🔴 **Rule-12 supersession (2026-07-18, post-PR-#724-review).** The banked
> **METER-INVALID-AT-KAPPA** verdict below is **SUPERSEDED** — it was **MANUFACTURED
> by an undisclosed prereg-vs-code deviation (F1, CRITICAL)**: the shipped X2 used
> `_place_detuned_harmonic_aware` (harmonic-avoidance) instead of the FROZEN §C X2
> rule (`_place_detuned_band`, q-power-budget). Harmonic-avoidance is BLIND to the
> plant's INDEPENDENT lattice line at ω≈1.123 (carrying **14.6%** of the plant's own
> q-power, no `n·ω_d`), so the shipped band **[1.07,1.38]** sat ON it and read "LOST"
> **even at the certified κ=0.012 (×3.6)** — a false kill with no κ-specific content.
> **Restoring the frozen placement flips X2 to PASS at κ=0.03 (×128.7, N_det=0) and
> at the reference κ=0.012 (×354.8), and the verdict FLIPS.** The pre-review verdict
> body is preserved verbatim below (Rule 12); the corrected result is the **§C-post-review
> addendum** appended after §8. See §7 + the addendum for all nine findings by number.

> ## ★ VERDICT (post-review, honest re-run) — **METER-VALID-KAPPA-BAND [0.030, 0.030]**
>
> **Banked (frozen §C3, honest X2).** With the FROZEN q-power-budget placement restored,
> the meter is **VALID at `κ = 0.030`** (all of X1–X6 pass at MILD) and **INVALID above it**:
> the drain-attributed kill map is `{0.030: [], 0.045: [X5], 0.06: [X3, X5]}` (the literal-frozen
> map `{0.045: [X5, X2-drain], 0.06: [X3, X5, X2-drain]}` gives the **same band**). The
> **certified band is a single point `[0.030, 0.030]`**, bounded above by X4 `κ_break = 0.09`.
> **The κ-sweep is UNBLOCKED at `κ = 0.030`** (the meter half of follow-on-3 prerequisite
> (a)+(b)+(c) is discharged there); **Grant lands the sweep-launch decision on this band.**
>
> **★X2 resonance-gating is ALIVE at EVERY κ (the pre-review "any comb fills" mechanism is
> RETRACTED — F2).** A genuinely off-content (drain-robust quiet) comb absorbs only
> `7.8e-5 / 1.8e-4 / 3.1e-4` at κ=0.03/0.045/0.06 → collapse **×27604 / ×12267 / ×6898**.
> The measured per-step transfer `Γ_E ≈ 5.4e-3 / 1.2e-2 / 2.2e-2` is **25–101× SMALLER** than
> the 0.55 detuning offset; the coupling linewidth `Γ_κ ≈ 0.22 / 0.22 / 0.62` is `≫ Δω_comb=0.010`
> (quasi-continuum populated — the fast-transfer half is real) but `≤ the 0.55 offset` (a
> detuned comb stays empty — selectivity survives). The transfer is a **GENUINE golden-rule
> coupling** (F4 post-hoc: `Γ_E ∝ DOS^{0.93}`, Fermi's rule). **The coupler needs NO rebuild.**
>
> **What genuinely bounds the band at 0.030 (κ≥0.045 stand as measured).** X5 tare degenerates
> (`E_bath → E0`, `c = √(1−E_bath/E0) → 0`) at κ≥0.045; X3 floor goes dishonest (off-resonant
> sea `1.7e-2 ≥ 1e-2`) at κ=0.06. X2 at κ≥0.045 is a **§C3 DISCLOSED-LIMITATION** (the frozen
> placement keys on the collar-q spectrum, which **drains to DC** at full discharge, so the
> band lands on the drive) — a placement artifact, NOT a physical loss (quiet-band control
> above). Those κ die on X5/X3 regardless; the band is `[0.030, 0.030]` under either reading.
>
> **★Feared risk still DISCONFIRMED (X1, unchanged).** Drift is **BOUNDED** (`≤6.8e-6`, `a₂<0`,
> `|r|≤0.78`) at every (κ,point), `≥6 orders` under the ceiling — the #721 R-1 identity is
> κ-robust. **Controls survive (X4, X6):** two-tank + sparse return (`R_cum>0.70`; `κ_break=0.09`);
> level-repulsion negligible (`pulling≤0.0006`). X1/X3/X4/X5/X6 numbers reproduce the pre-review
> run **byte-for-byte** — only X2's placement changed.
>
> **NOT banked:** any counting-arrow/sweep result. No arm/door/sweep fired. The depletion-rate
> rung (`Γ=3Hρ_latent`) and the #721 κ=0.012 certificate are untouched.

---

> ## ⛔ SUPERSEDED (pre-review verdict — preserved verbatim per Rule 12; see the 🔴 header above)
>
> > ## ★ VERDICT — **METER-INVALID-AT-KAPPA**
> >
> > **Banked (frozen §C3):** the meter is **INVALID across the whole tested band `κ ∈ {0.030, 0.045, 0.060}`** — a KILL fires at **every** band κ: `{0.03: [X2], 0.045: [X2, X5], 0.06: [X2, X3, X5]}`. The **certified band is EMPTY**; the **κ-sweep is BLOCKED pending a meter redesign** (SPEC'd in §5, **NOT built** — §C3).
> >
> > **★The single mechanism (Rule 11 — one root explains every failure).** The strong coupling that *reaches* the counting-arrow regime (fast transfer, quasi-continuum populated — #722) also **FULLY DISCHARGES the cavity into whatever comb is attached** (`E_bath_peak ≥ E0`, `min E_lat/E0 = 0` at every band κ). One fact, three deaths: **X2** the discharge is broadband so the detuned comb absorbs **as much as** the resonant comb (collapse ×1.0–1.5 ≪ the ×100 soul-check) — the transfer is no longer resonance-gated; **X3** the same coupling broadens the lines until the off-resonant sea (`1.7e-2`) climbs above the absolute floor (`1e-2`) at κ=0.06; **X5** full transfer drives `E_bath→E0` so the tare `c=√(1−E_bath/E0)→0` degenerates. **The regime the sweep NEEDS and the regime the meter's weak-coupling discriminators FAIL are the SAME regime.** *(🔴 Retracted per F2: the "fills whatever comb is attached" clause for X2 is quantitatively FALSE — a quiet comb absorbs `≤3.1e-4`, collapse ×6898–27604. The X2 death was the placement bug, not the discharge. X3/X5 stand.)*
> >
> > **★The feared risk is DISCONFIRMED (X1).** The §C1 secular-pump risk did **NOT** materialize: the total-energy drift is **BOUNDED** (round-off-walk; `≤ 6.8e-6`, curvature `a₂<0` saturating, `|r|≤0.78` non-monotone) — **not** a secular pump, at **every** (κ, point). The algebraic-identity structure (#721 R-1) holds even through the over-extraction clamp; the identity break stays `≤ 6.8e-6 ≪ R_BATH_MAX·transfer = 0.2`. The meter's **conservation** survives; its **discriminators** do not. *(This paragraph survives review unchanged.)*
> >
> > **Controls + comb integrity SURVIVE (X4, X6):** the two-tank + sparse-comb reversibility controls return (`R_cum > 0.70`) at every band κ, and the dressed-comb level-repulsion is negligible (`pulling ≤ 0.0006 ≪ Δω/2 = 0.005`) — proving the failure is specifically the meter's **discriminators**, not a dead coupling, a numerical blow-up, or a hybridized comb. The two-tank **κ_break = 0.09** (earlier than the "known by 0.12" ceiling) bounds the band from above independently. *(Survives review unchanged.)*
> >
> > **NOT banked:** any counting-arrow result. No arm/door/sweep fired. The depletion-rate rung (`Γ=3Hρ_latent`) is untouched. The #721 κ=0.012 certificate is untouched (this lane only tests κ=0.03–0.06).

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

> 🔴 **SUPERSEDED (F1, PR #724 review; corrected in the §C-post-review addendum below §8).**
> This table used the **wrong (non-frozen) placement** `_place_detuned_harmonic_aware` — the
> band **[1.07,1.38]** sits ON a genuine lattice line (14.6% of q-power). The **honest X2** with
> the FROZEN `_place_detuned_band` reads **×354.8 @0.012-ref, ×128.7 @0.03 (both PASS, N_det=0)**;
> ×2.6 @0.045 / ×1.0 @0.06 are a **drain-placement artifact** (§C3 disclosed-limitation), not a
> physical loss. See the addendum. The pre-review table is preserved verbatim below (Rule 12).

| κ | `E_bath_peak` resonant (`N_occ`) | detuned band | `E_bath_peak` detuned (`N_occ`) | **collapse ×** (frozen ≥100) | verdict |
|---|---|---|---|---|---|
| 0.03 | 2.14 (15) | [1.07, 1.38] | 1.40 (4) | **×1.5** | **LOST** |
| 0.045 | 2.14 (23) | [1.07, 1.38] | 1.94 (6) | **×1.1** | **LOST** |
| 0.06 | 2.14 (33) | [1.07, 1.38] | 2.14 (9) | **×1.0** | **LOST** |

Robust `ω_d = 0.520` (bath mode-energy peak); detuned band harmonic-aware (`harm_clear = 0.030` from all folded `n·ω_d ∈ {0.52,1.04,1.56,2.08,2.60,3.12}`; §B W3 corrected rule). The detuned comb absorbs **as much as** the resonant comb (`N_det = 4→9 > 0`; the frozen soul-check requires `N_det = 0` and collapse `≥ 100`). At the certified κ=0.012 detuning collapsed the transfer **3.5 orders**; at κ=0.03–0.06 it collapses it **not at all** — the transfer reverts to an **amount-matcher** (the F-1 failure mode the meter was rebuilt to avoid). *(🔴 F1: this whole reading is the placement bug — the frozen q-power-budget band is off the ω≈1.123 line and PASSES at 0.03/0.012-ref.)*

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

> 🔴 **RETRACTED (F2, MAJOR, PR #724 review; corrected in the §C-post-review addendum).**
> The "fully discharges into **whatever** comb is attached" mechanism is **quantitatively
> EXCLUDED**: a genuinely off-content (quiet) comb absorbs only `≤3.1e-4` (collapse ×6898–27604);
> `Γ_E ≈ 5.4e-3…2.2e-2` per step is 25–101× below the 0.55 detuning offset. **Resonance-gating
> is ALIVE at every κ.** The X2 death was the **placement bug (F1)**, not the discharge. The
> orchestrator-routed "linewidth-tradeoff / Wigner–Weisskopf" reading is retracted by the same
> measurement (`Γ_κ ≳ Δω_comb` — quasi-continuum true; but `Γ_κ ≪` the far-detune offset —
> selectivity survives). The X3/X5 halves of the mechanism (floor, tare) stand. Text preserved
> verbatim below (Rule 12).

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

> 🔴 **CORRECTED (F4, MAJOR, PR #724 review; superseded by §D SPEC in the addendum).**
> The premise "the sweep is blocked pending a **meter redesign**" is **wrong**: the meter is
> **VALID at κ=0.030**, and the coupler is a **genuine golden-rule coupling** (`Γ_E ∝ DOS^{0.93}`)
> that needs **NO rebuild**. The three "broken discriminators" below are **regime-honesty limits
> of the frozen criteria at strong κ**, not coupler defects. The redesign fork **narrows** to
> **"§D re-certification with regime-honest criteria"** vs **abandon** — see the §D SPEC in the
> addendum. Text preserved verbatim below (Rule 12).

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

> 🔴 **F5/F6 (PR #724 review).** This section disclosed the X1/X2-ω_d code fixes but **did
> NOT disclose the placement deviation (F1)** — the load-bearing one. That formal §C3 disclosure
> is in the addendum below §8 (F5). The two "first-run" correction-baseline numbers cited here
> (item 1's `clamp_drain` behaviour, item 2's "κ=0.03 ratio ×10") are **SCRATCH-PROVENANCE**
> (a superseded run under the wrong placement); the honest-placement κ=0.03 ratio is **×128.7
> (PASS)**, not ×10 (F6). The full deviation ledger (F1–F9) is in the addendum.

Two shipped operationalizations were corrected **before banking** so the reported numbers are lattice-derived and artifact-free (regime-discipline: a null where the effect can't exist = artifact, not falsification). Neither is a threshold retune; both are disclosed:

1. **X1 code-to-frozen-spec fix.** The first shipped `clamp_drain` boolean KILLed on full cavity discharge (`min E_lat/E0 → 0`); the **frozen §C X1 criterion** KILLs only if the identity break (drift) reaches `R_BATH_MAX·transfer` (it does not — drift ≤6.8e-6 ≪ 0.2). Corrected to the frozen criterion; over-extraction is **reported anatomy**, not an independent KILL. **The drift numbers are identical between the two runs** — only the KILL boolean changed (first run KILLed X1 spuriously; corrected run PASSES X1 per the frozen text). Not a rescue: the frozen criterion always PASSED X1.
2. **X2/X6 ω_d robustness (artifact removed).** The first run read `ω_d` from the collar-q rFFT, which collapses to DC (`ω_d → 0`) at κ≥0.045 because the cavity fully drains (`q → 0`) — a window-averaging artifact that mis-placed the X2 detuned band (overlapped resonance ⇒ spurious `N_det`, ratio) and gave X6 trivial `n_near=0` passes. Corrected to a **drain-robust `ω_d` = bath mode-energy peak** (the bath retains the transferred energy). Post-fix `ω_d = 0.520` is stable at all κ; X6 PASS holds. *(🔴 F1/F6: the clause "X2 was already LOST … κ=0.03 ratio ×10" is SCRATCH-PROVENANCE and FALSE — that ×10 was under the wrong `_place_detuned_harmonic_aware` placement / an intermediate variant; the FROZEN `_place_detuned_band` gives **×128.7 PASS** at κ=0.03. The ω_d artifact is real but is NOT what carried the X2 verdict — the placement bug was.)*
3. **X1 drift vs #722 scratch (flag-don't-fix; §4)** — both readings stated; verdict independent of the discrepancy.

No frozen §C threshold was loosened. A single mechanism explains every failure (§3) — the discipline working at full strength (honest negative closure).

---

## 8 · Gates + freeze margin

- **Freeze margin (real):** §C frozen-by-push at `2026-07-18T07:21:52Z` (API committedDate; pushed `07:22:26Z`), **before any X-battery code existed**. First battery-code commit: this commit (see git log; the margin is the push→first-code interval, reported in the PR).
- **Gates:** `ruff check` clean; `make verify` green; A-battery **V1–V6 byte-identical** (re-ran `METER-VALID-WITHIN-ENVELOPE`) and W-battery **W1–W6 byte-identical** (regression green — the X-battery is additive, opt-in `--x-battery`, A/W functions AST-identical to origin/main).
- **Byte-untouched:** `src/ave/thermal/f6_bath_meter.py` (meter module) and the engine — verified `git diff origin/main` empty on the meter module. The only edits: the charter §C (append-only, 70 insertions/0 deletions above byte-identical) and `f6_bath_meter_validate.py` (X-battery additions + the `--x-battery` dispatch line).

*Honest closure (Rule 11): clean negative, single mechanism named (strong-coupling full-discharge → resonance-gating + floor + tare all break in the counting-arrow regime), branch closed, redesign SPEC'd not built. Nothing banked at emergence-class. The meter is **METER-INVALID-AT-KAPPA** across κ=0.03–0.06; the counting-arrow κ-sweep is **BLOCKED pending a meter redesign**; the feared secular-pump risk is **DISCONFIRMED** (conservation is κ-robust; the discriminators are not).* *(🔴 The METER-INVALID headline of this closing paragraph is SUPERSEDED — see the §C-post-review addendum. The verdict is **METER-VALID-KAPPA-BAND[0.030,0.030]**; the sweep is UNBLOCKED at κ=0.030.)*

---

## §C-post-review addendum — PR #724 adversarial-review repairs (2026-07-18, append-only)

> 🔴 **Rule-12 supersession (2026-07-18, post-review).** The PR #724 adversarial review confirmed
> **9 findings** including **1 CRITICAL** (F1). The banked **METER-INVALID-AT-KAPPA** verdict was
> **MANUFACTURED** by an undisclosed prereg-vs-code deviation in X2's placement. Restoring the
> FROZEN §C X2 placement, re-running the full X-battery, and re-adjudicating per the frozen §C3
> classes **FLIPS the verdict to METER-VALID-KAPPA-BAND[0.030,0.030]**. The §1–§8 body above is
> preserved verbatim (Rule 12); result-level supersessions are recorded HERE, not by editing it.
> **No frozen §C threshold was loosened; restoring the frozen placement is un-doing an unfrozen
> deviation, not a retune (Rule 11).** Driver: `--x-battery` (repaired) + `--genuineness` (post-hoc).

### The honest re-adjudication (frozen §C3 classes, honest X2)

Per-κ, per-leg at the MILD (band-determining) point — every leg at the frozen threshold, no retune:

| κ | X1 drift | X2 collapse (frozen placement) | X3 floor | X4 controls | X5 tare (mild) | X6 pulling | **in VALID band?** |
|---|---|---|---|---|---|---|---|
| **0.012** (ref) | — | **×354.8, N_det=0 PASS** | — | — | — | — | (reference only) |
| **0.030** | BOUNDED ✅ | **×128.7, N_det=0 PASS** | sea 7.2e-3 ✅ | R_cum 0.99/0.89 ✅ | c=0.367,match 1.6e-2 ✅ | 0.0006 ✅ | **✅ YES (all X1–X6 pass)** |
| **0.045** | BOUNDED ✅ | ×2.6 [DRAIN-LIMIT, §C3] | sea 9.2e-3 ✅ | R_cum 0.99/0.83 ✅ | **c=0.000 OVER-TRANSFER ❌** | 0.0002 ✅ | ❌ (X5) |
| **0.060** | BOUNDED ✅ | ×1.0 [DRAIN-LIMIT, §C3] | **sea 1.7e-2 ❌** | R_cum 1.00/0.79 ✅ | **c=0.000 OVER-TRANSFER ❌** | 0.0002 ✅ | ❌ (X3, X5) |

**Verdict: METER-VALID-KAPPA-BAND[0.030, 0.030]** — the contiguous sub-band where all X1–X6 pass
at MILD, bounded above by X4 `κ_break = 0.09` and (independently) X6 pulling `≪ 0.005`. The κ-sweep
prerequisite (a)+(b)+(c) is discharged at κ=0.030; **Grant lands the sweep-launch decision.**

### F1 (CRITICAL) — the X2 KILL was manufactured by an undisclosed placement deviation

The shipped X2 used `_place_detuned_harmonic_aware` (`validate.py:1005`, harmonic-avoidance) —
**NOT** the FROZEN §C X2 rule (charter §C X2 line 356: *q-power-budget placement* — "the lowest
32-mode Nyquist band whose q-power fraction `< W3_POWER_FRAC_MAX = 1e-2`"), whose implementation
`_place_detuned_band` sat **UNUSED at `:560`**. Harmonic-avoidance only dodges the folded harmonics
`n·ω_d`; it is **BLIND to the plant's INDEPENDENT lattice line at ω≈1.123** (a real line, no `n·ω_d`),
which carries **14.6% of the plant's own q-power**. The shipped band **[1.07,1.38]** sat ON that line
and read "LOST" **even at the certified κ=0.012 (×3.6 — no κ-specific content)** — the tell of a
manufactured kill. **Repair (`run_x2` now calls the frozen `_place_detuned_band`, detuned comb at
the meter's canonical `DETUNE_M=32 / Δω=0.030` spanning the placed band):**

| κ | resonant `E_bath_peak` (`N_occ`) | FROZEN band | q-power frac (`<1e-2`) | folded-harm clearance | `E_det` (`N_occ`) | **collapse ×** | placement | frozen gate |
|---|---|---|---|---|---|---|---|---|
| 0.012 (ref) | 1.221 (8) | [1.185, 2.115] | 2.05e-3 | 0.000¹ | 3.44e-3 (0) | **×354.8** | reliable | **PASS** |
| 0.030 | 2.141 (15) | [1.187, 2.117] | 2.03e-3 | 0.000¹ | 1.66e-2 (0) | **×128.7** | reliable | **PASS** |
| 0.045 | 2.141 (23) | [0.779, 1.709] | 4.20e-3 | 0.000¹ | 8.14e-1 (8) | ×2.6 | **DRAINED** | disclosed-limit |
| 0.060 | 2.141 (33) | [0.062, 0.992] | 4.04e-3 | 0.000¹ | 2.143 (12) | ×1.0 | **DRAINED** | disclosed-limit |

¹ The frozen power-budget band CONTAINS folded harmonics n=3 (1.571) / n=4 (2.095) at clearance 0.0 —
this is the R-6 power-budget reading verbatim: a band carrying `<1/100` of the q-power cannot
re-excite past the ≥2-order collapse budget even when it contains a low-power folded harmonic
(demonstrated: ×128.7 with N_det=0). The frozen rule reports band + fraction + clearances per κ, as
its §C text requires.

**★Finder-vs-verifier ×42-vs-×128.7 resolution (careful §C-faithful runs).** The collapse ratio is
**acutely sensitive to the detuned comb's density-of-states** (a denser detuned comb has more modes to
absorb): at the frozen band [1.187,2.117], κ=0.030, the ratio is **×12.1** (comb @Δω=0.010),
**×87.7** (@Δω=0.020), **×128.7** (@Δω=0.030). The FAITHFUL frozen reading is **×128.7** — the literal
`_place_detuned_band` (whose band width is computed with `Δω=0.030`) with the meter's canonical
32-mode probe at that same `Δω=0.030` (self-consistent). This **reproduces the verifier's ×128.7,
N_det=0, PASS** deterministically. The finder's earlier **×42** scratch was a **non-self-consistent
variant** (a detuned-comb density between densest and canonical); it is superseded by the faithful
run. Either way N_det=0 at every reading, and the faithful frozen reading clears the ×100 gate with
margin at κ=0.030 and κ=0.012-ref.

**κ≥0.045 DRAIN-LIMIT (§C3 disclosed-limitation — "a placement rule that turns out unsatisfiable").**
At full discharge the collar-q spectrum drains to DC (`ω_d^qspec → 0.000` vs the drain-robust bath
`ω_d = 0.520`; `ω_99` collapses `1.13 → 0.72 → 0.002`), so the frozen placement — which keys on that
spectrum's 99% cutoff — lands the band ON the drive band's wings. This is a **placement artifact, not a
physical loss** (the drain-robust quiet-band control shows gating alive, F2). Disclosed as a finding;
code left un-retuned; the kill map attributes X2 only where the placement is reliable. κ≥0.045 die on
X5/X3 regardless — the band is [0.030,0.030] under both the drain-attributed and literal-frozen kill
maps (both banked in `result.json → kill_maps`).

### F2 (MAJOR) — the "full discharge fills ANY comb" narrative is RETRACTED (quantitatively excluded)

The pre-review single-mechanism claim (§3) — the discharge "fills whatever comb is attached", so a
detuned comb absorbs as much as the resonant — is **false**. Measured (post-hoc probe, `--genuineness`):

| κ | per-step `Γ_E` | offset/`Γ_E` (offset=0.55) | linewidth `Γ_κ` (FWHM) | `Γ_κ/Δω_comb` | `Γ_κ/offset` | quiet-comb `E_bath_peak` | quiet collapse |
|---|---|---|---|---|---|---|---|
| 0.030 | 5.4e-3 | **101×** | 0.220 | 22 | 0.40 | 7.8e-5 | **×27604** |
| 0.045 | 1.2e-2 | 45× | 0.220 | 22 | 0.40 | 1.8e-4 | ×12267 |
| 0.060 | 2.2e-2 | 25× | 0.620 | 62 | 1.13 | 3.1e-4 | ×6898 |

**Honest Γ_κ vs Δω statement:** `Γ_κ ≳ Δω_comb` (22–62× — the comb IS a quasi-continuum, the
fast-transfer half is REAL) **but** the per-step `Γ_E` is **25–101× below** the 0.55 detuning offset,
and a genuinely off-content quiet comb absorbs only `≤3.1e-4` (collapse ×6898–27604). **Selectivity
survives; resonance-gating is ALIVE at every κ.** This also **retracts the orchestrator-routed
"linewidth-tradeoff / Wigner–Weisskopf" interpretation** — the same measurement kills it (`Γ_κ` never
reaches the detuning offset for a genuinely-detuned comb; only the drained-placement band, sitting on
the drive, catches energy). The X2 death was **F1**, not the discharge.

### F3 (MAJOR) — ratio-saturation is a §C criterion-design artifact (both readings reported)

At strong κ the resonant transfer **ceilings at `E0`** (`E_bath_peak = 2.141 = E0`, full discharge),
so the ×100 collapse gate `E_res/E_det ≥ 100` degenerates to **`E_det < E0/100 = 0.0214`** — an
*absolute detuned-absorption* test, not a ratio. At κ=0.030 the frozen band passes because it genuinely
catches `E_det = 0.0166 < 0.0214` (marginal-but-real: ×128.7). This ceiling means the ≥100× gate could
fail an honest-placement X2 at some band κ purely because `E_res` saturates while `E_det` is unsaturated
— a **criterion-design artifact foreseeable from the #722 numbers**. **Per Rule 11 the frozen gate still
governs the frozen verdict** (X2 PASSES at κ=0.030 on the frozen gate); the artifact is reported so a
§D re-certification (below) can adopt an *absolute detuned-absorption* criterion (`E_det/E0 < 1e-2`)
that is not ceiling-degenerate. **Both the frozen-gate outcome (PASS@0.030) and this criterion-artifact
analysis are reported.**

### F4 (MAJOR) — density-scaling PASSES on the byte-untouched meter → ROUTED POST-HOC EVIDENCE

The review's density-scaling probe (shipped for provenance as `run_genuineness_probes`, `--genuineness`;
**UNFROZEN / NON-GATING / POST-HOC**) shows the coupler's transfer rate tracks the comb
density-of-states — **Fermi's golden rule** `Γ ∝ ρ(ω_d) = 1/Δω`:

| κ | Δω=0.010 (DOS 100) | Δω=0.020 (DOS 50) | Δω=0.040 (DOS 25) | Δω=0.080 (DOS 12.5) | fit `Γ_E ∝ DOS^p` |
|---|---|---|---|---|---|
| 0.030 | Γ_E 5.22e-3 | 2.70e-3 | 1.43e-3 | 7.45e-4 | **p = 0.934** |
| 0.045 | 1.11e-2 | 5.90e-3 | 3.17e-3 | 1.66e-3 | **p = 0.911** |

`p ≈ 0.93 ≈ 1` ⇒ **genuine golden-rule coupling** (the decay rate tracks comb density) — this is the
distinctive fingerprint of a real resonant coupling, **not** an amount-matcher. **Correction to the
redesign SPEC (F4):** the coupler mechanism needs **NO rebuild for genuineness**; the redesign fork
**narrows** to **"§D re-certification with regime-honest criteria"** vs **abandon**. Banked here as
**routed post-hoc evidence** (unfrozen); it feeds — but does not pre-empt — the §D prereg below.

**§D re-certification SPEC (outline only — DO NOT freeze or run in this lane; Grant adjudicates the
fork).** A strong-κ re-certification prereg would freeze: **(1)** density-scaling `Γ_E ∝ DOS^{p}` with
`p ∈ [0.8, 1.2]` as the **frozen strong-regime genuineness criterion** (replaces the ceiling-degenerate
soul-check as the primary genuineness gate at full discharge); **(2)** an **honest X2** — an *absolute
detuned-absorption* gate `E_det/E0 < 1e-2` with a **drain-robust placement** (place off the bath-peak
`ω_d`, not the drained collar-q spectrum), avoiding the F1 blind spot and the F3 ceiling; **(3)** the
strong-κ **X3** with a κ-broadening-aware floor (`floor ∝ measured sea`, DERIVED) and the strong-κ
**X5** with an incremental/rate tare well-defined through `E_bath → E0`. §D would then re-certify a band
above κ=0.030 on regime-honest criteria. **This lane SPECs §D; it does not build, freeze, or run it.**

### F5 (MAJOR) — formal placement-deviation disclosure (per §C3's own rule)

Per the frozen §C3 "per-leg deviation-is-a-finding" rule, the X2 placement deviation is formally
disclosed: **shipped operationalization** = `_place_detuned_harmonic_aware` (harmonic-avoidance);
**frozen §C text** = q-power-budget `_place_detuned_band`. The shipped code deviated **without an
amendment or disclosure** — the pre-review result §7 disclosed the X1/ω_d code fixes but **not** this
load-bearing placement swap. It is now un-done (the frozen rule restored), both bands reported, and the
verdict re-adjudicated. This is the disclosure §C3 required at bank time.

### F6 (MINOR) — §7 "first-run" numbers tagged scratch-provenance

The two §7 correction-baseline "first-run" numbers (item 1's `clamp_drain`; item 2's "κ=0.03 ratio
×10") are **SCRATCH-PROVENANCE** (superseded runs under the wrong/intermediate placement). The
honest-placement κ=0.030 ratio is **×128.7 (PASS)**. Tagged inline in §7.

### F7 + F9 (MINOR) — the X5 FINDING→KILL promotion is a 4th deviation (verdict-neutral)

The shipped `run_x_battery` treats an X5-mild over-transfer as an explicit **KILL** — but the frozen
§C3 **METER-INVALID KILL enumeration OMITS X5** (it lists X1/X2/X3/X4/X6 only), and frozen §C X5 itself
calls over-transfer a **FINDING** ("reported as an over-extraction budget breakdown, not silently
passed"). This is a **4th undisclosed deviation** — but in the **anti-rescue direction** (it makes a κ
*harder* to certify) and it was **verdict-neutral in the shipped result** (X2 killed every band κ
alone). It is **NOT verdict-neutral now**: with the honest X2, X5 is what excludes κ=0.045/0.060 from
the band. **Reconciliation (honest, not a silent fix):** X5 failure legitimately excludes a κ from the
VALID band via the frozen METER-VALID definition — "X1–**X6** all pass at MILD" (which *includes* X5) —
even though X5 is not a named leg in the *METER-INVALID* KILL enumeration. So the band-determination
(all-pass) is faithful; the label "KILL" vs "FINDING that fails the all-pass gate" is a §C3 wording
asymmetry, **flagged for the §D re-cert** (X5 should be enumerated in the strong-regime KILL list, or
explicitly scoped as a band-excluding FINDING). Verdict [0.030,0.030] holds under both labelings.

### F8 (MINOR) — sparse-horizon 864-vs-869 fixed

`SPARSE_HORIZON` used the exact formula `int(round(11·2π/0.08)) = 864`, mismatching the frozen §C X4
value **869** (`= 11·round(T_rec=79)`) and its own in-code comment. Fixed to the frozen `869`
(`T_REC_SPARSE = round(2π/0.08) = 79`, `SPARSE_HORIZON = 11·79 = 869`). **X4 numbers are unchanged**
(the `R_cum(x=10)` read at step 785 is well inside both horizons — verified: sparse `R_cum` still
`0.890/0.834/0.793`, `κ_break = 0.09`).

### Disposition (Rule 12 — substitute, do not refill)

- **Substitute** the METER-INVALID-AT-KAPPA verdict with **METER-VALID-KAPPA-BAND[0.030,0.030]** via
  the restored frozen protocol (a corrected measurement, verified end-to-end — not an unverified
  hypothesis refill). The pre-review body is preserved (Rule 12).
- **Retract** (F2) the "any comb fills / full discharge" narrative and the routed
  linewidth-tradeoff/Wigner–Weisskopf reading — both quantitatively excluded.
- **Routed to Grant:** (1) the **sweep-launch decision** at the certified `κ = 0.030` (now
  **positive** — the prerequisite is discharged); (2) the **§D re-certification vs abandon** fork for
  a band *above* 0.030 (F4: coupler is genuine, no rebuild — the fork is about regime-honest criteria).
- **Untouched:** the #721 κ=0.012 certificate; the depletion-rate rung (`Γ=3Hρ_latent`); the meter
  module + engine (byte-untouched); the frozen §C body (this addendum is append-only).

*Honest closure (Rule 11): restoring the frozen placement is un-doing an unfrozen deviation, not a
retune; the verdict flip follows the data. X1/X3/X4/X5/X6 reproduce byte-for-byte; only X2's placement
changed. The single point κ=0.030 is certified; the coupler is a genuine golden-rule coupling; the
band above 0.030 is bounded by regime-honesty limits of the frozen criteria (F3), routed to a §D
re-cert. Nothing banked at emergence-class.*
