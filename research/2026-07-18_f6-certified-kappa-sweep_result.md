# F6 certified-κ recurrence sweep — the SUFFICIENT test of the counting arrow — RESULT

**Date:** 2026-07-19 · **Class:** result (the SUFFICIENT fire; honest closure, Rule 11)
**Prereg (FROZEN):** [`2026-07-18_f6-certified-kappa-sweep_prereg_FROZEN.md`](2026-07-18_f6-certified-kappa-sweep_prereg_FROZEN.md) — §0–§7 **frozen-by-push `2026-07-19T16:16:32Z`** (API committedDate), **before any driver code existed**.
**Driver:** `src/scripts/vol_1_foundations/f6_certified_kappa_sweep.py` · **Data:** `2026-07-18_f6-certified-kappa-sweep_result.json`
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` — **BYTE-UNTOUCHED**). **Reused BYTE-UNTOUCHED:** `f6_counting_arrow_arm.py` (#722), `f6_bath_meter_validate.py` (#724 FROZEN `_place_detuned_band`).
**Plant:** standalone-K4, within the meter certificate METER-VALID-KAPPA-BAND[0.030,0.030] @ MILD (#721 R-1 SCOPE CAVEAT). **Cell:** `κ=0.030` EXACTLY, MILD (`scale=0.6`, `A_max≈0.10`).

> ## ★ VERDICT — **FOREIGN-EATER** (frozen §4 tree, byte-faithful; self-check `match=True`)
>
> **Banked (frozen).** The **QUESTION WAS ASKED** — unlike #722, the regime gate **PASSES** at the certified cell (densest comb: `t63/T_rec = 0.194 ≤ 0.5`; `N_occ = 15 ≥ 10`; transfer `peak_frac = 1.000`). The **SUFFICIENT signature is DECISIVELY ABSENT:** the `R_return(x)` curves **do NOT collapse** (`spread(x_50) = 7.37`, frozen `< 0.30`) and the transition is **not at `x≈1`** (`mean(x_50) = 7.41`, frozen `[0.7,1.5]`). The frozen §2 recurrence-collapse **PREDICTION is FALSIFIED at `κ = 0.030`.** The frozen §4 tree returns **FOREIGN-EATER** at precedence step 3 (`grid_return_min = 0.000 < 0.70` — the dense combs never return even after **ten** recurrence-times) and, independently, at step 6 (returns present but not collapsing to `x≈1`). **INSTRUMENT-first, fail-closed** — the correct disposition.
>
> **★The single mechanism (Rule 11 — one root explains every failure).** At `κ=0.030` the strong coupling drives the high-DOS **dense** combs to **FULL DISCHARGE** (`peak_frac → 1.000`: `E_bath → E0`, the cavity drains). A **drained lattice** (`E_lat → 0 ⇒ q ≈ 0`) **decouples** from the bath (`coupling_kick ∝ q ≈ 0`), and the meter's **amount-not-phase** global back-reaction (§A1/§A8, the *known* limitation — ~90% uniform attenuation, phase-blind) **cannot re-inject** energy into the drained lattice. So the phase-invariant `E_bath = Σ½p²+½ω²x²` **HOLDS the transferred energy with no return path** — `R_return ≡ 0.000` across the entire window for the three fully-discharged combs. Where transfer is **PARTIAL** (two-tank `peak_frac=0.091`, sparsest `0.169`, production `0.919`) the energy **does** return — **but at the transfer/back-coupling timescale `x ≈ 3.6–11`, NOT at the recurrence `x ≈ 1`** (reproducing the #722 `τ_transfer ≫ T_rec` inversion). **Root, unified:** the recurrence at `T_rec` is a **PHASE re-coherence**, and the meter's **amount-not-phase back-reaction cannot convert a bath phase re-coherence into an energy return** — so the recurrence is **invisible to the scalar `E_bath` ledger**, and the return (when it happens) is set by the coupling dynamics, never by `2π/Δω`.
>
> **★What SURVIVES pins the root as the back-reaction, NOT a dead coupling or blow-up.** Energy **conserves** (`max_cons = 2.5e-5 ≪ 1e-3`; the densest `6.8e-6` reproduces the reval-banked X1 drift bit-for-bit). **OFF recovers Ax3** (`2.1e-15`). The **partial-transfer controls RETURN** (two-tank `R_cum[10]=0.989`, sparsest `0.890` — bit-for-bit the reval-banked X4). The **Rule-10 reactance pair** proves the held bath is a **LIVE oscillator, not a static snapshot:** the densest comb's C-state/L-state split **swings across the window** (`C/E0: 0.20→0.67→0.25`, `L/E0: 0.20→0.33→0.75`) while `E_bath` holds — genuine C↔L free-rotation exchange of **phase-invariant** energy. The coupling is live, the ledger is intact, the bath oscillates; only the **amount-not-phase back-reaction** breaks the recurrence return.
>
> **★The counting-arrow QUESTION is NOT decided (scoped like #722).** FALSIFIED scopes to the **frozen recurrence-collapse PREDICTION at `κ=0.030` ON THIS METER**, *not* to the counting-arrow physics. The recurrence return is a **PHASE** phenomenon the meter's amount-not-phase back-reaction cannot faithfully measure in the **full-discharge sub-regime** the sweep enters at the 6908-step horizon. **Branch closed negative** (this sweep as designed, on this meter). **Routed (SPEC only, NOT built):** (1) a **phase-faithful back-reaction** meter (returns bath phase, not just amount — the reval §D SPEC #2, now empirically motivated at the recurrence-return level); (2) an operating point that reaches the quasi-continuum **without** full discharge; (3) the door's licensed **click** mechanism (the *other* arrow source, which does not depend on mode-continuum return).
>
> **NOT banked:** any COUNTING-ARROW / CHANNEL-BOUNDED result. Nothing at emergence-class. The depletion-rate rung (`Γ=3Hρ_latent`) and the #721/#724 certificates are untouched. No meter/engine edit.

---

## 1 · Sector header (result-time restatement)

- **Sector:** E-sector ε-store (F6 ε→T2 candidate). **Regime:** Regime I sub-yield, `A_max≈0.10` MILD, at the **certified `κ=0.030`**. **Plant:** standalone-K4; conservation identity-enforced (#721 R-1) and **audited green** (`max|E_lat+E_bath−E0|/E0 = 2.5e-5`; the densest `6.8e-6` = the reval X1 bank).
- **Consistency-vs-emergence:** the intended **FORM** (counting-arrow collapse at `x≈1`) did **not** manifest; nothing banked at emergence-class. The only positive reads are **consistency-class** (energy-conservation identity; partial-transfer controls return, reproducing the reval X4 bank bit-for-bit).

---

## 2 · Measured vs frozen prediction — the fire (every §3 grid value run)

`x = T·Δω/2π`; `R_return = 1 − E_bath/E_bath_peak` (t≥peak, else 0); `R_cum` = running max; `x_50` = first `x` with `R_cum ≥ 0.5`; `t63` = first step `E_bath ≥ (1−1/e)·peak`. Every number BY THE SHIPPED DRIVER, banked in `…_result.json` (§6-provenance discipline).

| Δω | M | T_rec | **peak_frac** | N_occ | t63/T_rec | **x_50** | R_ret[0.3] | **R_cum[10]** | cons | ω_d |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.010 | 71 | 628 | **1.000** | 15 | **0.194** | **nan** | 0.000 | **0.000** | 6.8e-6 | 0.524 |
| 0.015 | 48 | 419 | **1.000** | 10 | 0.442 | **nan** | 0.000 | **0.000** | 2.5e-5 | 0.524 |
| 0.020 | 36 | 314 | **1.000** | 8 | 0.783 | **nan** | 0.000 | **0.000** | 2.5e-5 | 0.524 |
| 0.030 | 24 | 209 | 0.919 | 3 | 2.268 | **7.70** | 0.000 | 0.932 | 2.3e-14 | 0.524 |
| 0.050 | 15 | 126 | 0.193 | 3 | 0.692 | **10.95** | 0.000 | 0.000 | 7.7e-15 | 0.523 |
| 0.080 | 10 | 79 | 0.169 | 1 | 1.324 | **3.58** | 0.000 | 0.890 | 1.0e-14 | 0.524 |
| two-tank M=2 | 2 | 31 | 0.091 | — | — | **6.33** | — | **0.989** | — | — |
| detuned control (FROZEN `_place_detuned_band`, band [1.19,2.12], q-frac 2.0e-3) | 32 | — | **8.6e-3** | 0 | — | — | — | — | — | — |

**Frozen adjudication (prereg §2/§4 thresholds, applied verbatim — no retune):**

| criterion (frozen) | threshold | measured | verdict |
|---|---|---|---|
| **REGIME GATE** t63/T_rec (densest) | ≤ 0.5 | **0.194** | ✅ regime reached |
| **REGIME GATE** N_occ (densest) | ≥ 10 | **15** | ✅ quasi-continuum |
| collapse `spread(x_50) < 0.30` | 0.30 | **7.372** | ❌ FAIL (25× over) |
| transition `mean(x_50) ∈ [0.7,1.5]` | [0.7,1.5] | **7.408** | ❌ FAIL |
| grid-wide return `min R_cum(x=10) ≥ 0.70` | 0.70 | **0.000** | ❌ FAIL → FOREIGN-EATER (step 3) |
| dense pins low `R_ret(0.3) < 0.30` | 0.30 | 0.000 | ✅ (but trivially — see §3) |
| energy conserved `< 1e-3` | 1e-3 | 2.5e-5 | ✅ (identity, #721 R-1) |
| OFF recovers Ax3 `< 1e-10` | 1e-10 | 2.1e-15 | ✅ |
| mode-count `N_occ dense > sparse` | — | 3 vs 1 | ✅ |
| protected-core bias (tared) `< 0.05` | 0.05 | 0.001 | ✅ |
| detuned control gated `peak_frac < 1e-2` | 1e-2 | 8.6e-3 | ✅ resonance-gated |

The two **headline** criteria (collapse + transition-at-`x≈1`) fail **decisively**; the regime gate **passes** (the question was asked); the ledger, OFF, mode-count, bias, and resonance-gating all pass. **The failure is specifically the recurrence RETURN, not the transfer or the instrument's liveness.**

---

## 3 · The single mechanism (explains every failure — Rule 11 honest closure)

> **One root.** At `κ=0.030` the coupling is strong enough that the **dense, high-DOS** combs reach **FULL DISCHARGE** (`peak_frac → 1.000`: `E_bath → E0`, `E_lat → 0`). A drained lattice reads `q ≈ 0` at the collar, so `coupling_kick ∝ q ≈ 0` **decouples** the bath, and the meter's **amount-not-phase** global rescale (§A1/§A8) — which can only remove/add the *amount* `d_e_bath` and requires `q ≠ 0` to do so — **cannot re-inject** the energy. The bath free-rotates, holding its **phase-invariant** `E_bath` forever. The recurrence at `T_rec` is a **PHASE** re-coherence of the comb; it leaves `E_bath = Σ½p²+½ω²x²` (a phase-blind sum of per-mode energies) **unchanged** — so it is **invisible to the scalar `E_bath` ledger** and drives no return.

Every observed failure is downstream of this one root:

- **Dense combs never return** (`R_cum[10] = 0.000` at Δω=0.010/0.015/0.020) — full discharge (`peak_frac=1.000`) drains the lattice; the phase-blind bath holds the energy; `R_return ≡ 0.000` across the entire window (x=0.1→10). *Not* recurrence-irreversibility — a **decoupled hold** the amount-not-phase back-reaction cannot undo.
- **Partial-transfer combs return, but at scattered `x`, NOT `x≈1`** — Δω=0.030 (`peak 0.92`) returns at `x_50=7.70`; Δω=0.080 (`0.17`) at `3.58`; Δω=0.050 (`0.19`) at `10.95`; two-tank (`0.091`) at `6.33`. The return is set by the coupling/back-drive timescale (`τ_transfer`-like), reproducing the **#722 `τ_transfer ≫ T_rec` inversion** — changing `Δω` moves `T_rec` but not the return time, so `x_50` **does not collapse**.
- **`R_ret(0.3)=0` for every comb** *trivially* — either the transfer is incomplete at x=0.3 (partial combs) or the energy is decoupled-held (dense combs); "dense pins low" passes for the wrong reason, exactly as #722.
- **`x_50` spreads `3.6 → 11` with no clustering near 1** — the headline non-collapse.
- **The bath is a LIVE oscillator, not a dead/static hold** — the Rule-10 reactance pair on the densest comb swings `C/E0: 0.20→0.67→0.25` and `L/E0: 0.20→0.33→0.75` across the window (genuine C↔L free-rotation exchange), while `E_bath` holds. The energy is stored reactively and phase-invariantly; it is neither dissipated nor frozen — it simply has **no phase-faithful return channel**.

**Regime read (regime-discipline).** This is **not** a numerical failure (conserves to 2.5e-5), **not** a dead coupling (controls return; bath oscillates), **not** the #722 regime-not-reached (the regime gate PASSES). It is a **meter-limitation confound**: the counting arrow is a **phase** phenomenon, and the certified meter's back-reaction is **amount-not-phase**, so the recurrence return cannot be measured through `E_bath` once the lattice drains at full discharge. **The frozen recurrence-collapse prediction is falsified on this meter; the counting-arrow question is not decided.**

---

## 4 · The classifier label — byte-faithful, no ambiguity (the #722 R-10 lesson discharged)

The shipped classifier implements the frozen §4 tree **with precedence 1→6**; the driver's `self_check` re-derives the verdict from an INDEPENDENT restatement of the tree and reports **`match=True`** (banked `self_check.match`). The verdict is **FOREIGN-EATER**, and — unlike #722 — it is **unambiguous**: the frozen §4 FOREIGN-EATER row is the **faithful grid-wide** condition ("return-failure NOT tracking `x`, across THE WHOLE grid"), and it fires **twice** independently — at step 3 (`grid_return_min = 0.000 < 0.70`, evaluated across all 6 sweep combs + two-tank, **not** narrowed to a subset) and at step 6 (returns present but not collapsing to `x≈1`). No FRICTION-RENAMED misfire is possible: the tree checks the regime gate and the grid-wide return **before** any mode-count fingerprint, and the door bin-(i) mapping (§4 of the prereg) is consumed verbatim, not redefined. **No prereg deviation.**

---

## 5 · Companion leg (SECONDARY — non-gating; inconclusive)

Self-termination size sweep `N ∈ {8,10,12,16}` (prereg §6, reused verbatim). The emergent-`Re(Z_in)/Z_char` proxy is **negligible** (`0.000 → 0.002`, weakly monotone in `N`) and the port region retains its energy (`x_revival ≈ 1.0` by construction). **Consistent with the primary finding** (the localized impulse excites few local modes; no bulk quasi-continuum, and no phase-faithful return channel). Reported at consistency-class only; `Z₀=√(L_bond/C_bond)` is calibration and is not approached. By prereg §6 this leg **cannot** change the sweep verdict.

---

## 6 · Disposition (Rule-12: retract, do NOT refill)

- **Retract** the **frozen `κ=0.030` recurrence-collapse PREDICTION** (§2: collapse + transition at `x≈1`). It is **FALSIFIED on this meter**. The sweep-as-designed does **not** exhibit the counting arrow's SUFFICIENT signature at the certified cell. **Branch closed negative.**
- **Do NOT refill the slot** with a new unverified hypothesis. Three routed follow-ons are **SPEC only** (each earns its own prereg + verification chain if pursued):
  1. **★Phase-faithful back-reaction meter** — the current global rescale returns AMOUNT, not PHASE (§A1/§A8), so it cannot convert the bath's `T_rec` phase re-coherence into an energy return once the lattice drains. A phase-returning coupling (return bath phase, not just amount) is the reval **§D SPEC #2**, now empirically motivated at the recurrence-return level. This is a **meter-mechanism change** ⇒ its own charter + W/X-revalidation (the §B-post-review R-1 identity would need re-checking).
  2. **Quasi-continuum without full discharge** — an operating point (weaker κ, or a rate-limited / per-mode-capped back-reaction) that populates `N_occ ≥ 10` **without** `peak_frac → 1.000`, so the recurrence return is not confounded by lattice drainage. The reval pins the fast-transfer regime to κ≈0.030–0.060 (all of which fully discharge the dense combs), so this may not exist for the comb-bath geometry — a finding, not a promise.
  3. **The click mechanism** — the corpus's *other* licensed arrow source (`retention-transition-split.md`), which does not depend on populating / recohering a mode continuum.
- **★FINDING (routed to Grant; flag-don't-fix — the certificate-window vs sweep-horizon gap).** The §C certificate certified `κ=0.030` at MILD on the X-battery windows (`W_WORKING_STEPS=800` / `X_NSTEP_SOUL=3000`), where the densest comb reads `E_bath/E0 ≈ 0.865` (X5 tare `c=0.367`, usable). The **sweep runs to `11·T_rec = 6908` steps**, where the densest comb reaches **`peak_frac = 1.000` (full discharge)** — the same over-transfer / tare-degeneracy the reval banked at **κ≥0.045** (short window, §C-post-review X5) appears at **κ=0.030 at the long window**. **The certified cell is valid for the meter's discriminators, but its certificate window is SHORTER than the recurrence-sweep horizon** — so the sweep enters a full-discharge sub-regime the certificate did not exercise. This is not a certificate error (nothing was retuned; the certificate stands at its window); it is a **scope gap** the SUFFICIENT test surfaced. A phase-faithful meter (route 1) or a no-full-discharge operating point (route 2) is required to close it.
- **Untouched:** the depletion-rate rung (`Γ=3Hρ_latent`); the #721/#724 meter certificates (byte-untouched; standalone-K4 identity intact); the meter module + engine (byte-untouched).

---

## 7 · Prereg deviations (disclosed) + gates

- **No prereg deviation.** Every §3 grid value was run; the §4 tree was implemented byte-faithfully (self-check `match=True`); the §7 FROZEN `_place_detuned_band` placement was used for the detuned control (band [1.19,2.12], q-frac 2.0e-3, `peak_frac=8.6e-3` gated — reproducing the certified X2 placement); the §2/§4 thresholds were applied verbatim with **no retune** (Rule 11). The single mechanism (full-discharge + amount-not-phase back-reaction) explains every failure — the discipline working at full strength.
- **Diagnostics provenance (F9 discharged):** `ω_d` (re-measured `0.524`, comb-independent — confirms the #721-banked `0.52377`), linewidth, `t63`/`t63_over_trec`, `N_occ`, `x_50`, per-cell `R_return`/`R_cum` tables, per-cell conservation drift, and the **Rule-10 reactance pair** (bath C-state AND L-state across the 11-point window) are **all computed by the shipped driver and banked in `…_result.json`** — nothing prose-only.
- **Gates:** `ruff check` clean; `make verify` green; the byte-faithful classifier cross-check `self_check.match = True`; the sparsest-comb and two-tank controls reproduce the reval-banked X4 numbers (`0.890` / `0.989`) **bit-for-bit**; the densest conservation drift (`6.8e-6`) reproduces the reval-banked X1 drift bit-for-bit — independent evidence the sweep plant matches the certified configuration.
- **Freeze margin (real):** prereg frozen-by-push `2026-07-19T16:16:32Z` (API committedDate), **before any driver code existed**; first driver-code commit is this commit (the margin is the push→first-code interval, reported in the PR).

---

*Honest closure (Rule 11): clean negative, single mechanism named (full discharge → drained lattice → amount-not-phase back-reaction cannot re-inject the phase-invariant `E_bath` ⇒ the recurrence return is invisible to the scalar ledger), branch closed, follow-ons SPEC'd not claimed. Nothing banked at emergence-class. The **frozen recurrence-collapse PREDICTION is FALSIFIED at `κ=0.030` on this meter**; the shipped classifier returns **FOREIGN-EATER** (byte-faithful, self-check green, no bin ambiguity — the #722 R-10/R-5 lessons discharged); the **counting-arrow QUESTION is NOT decided** (the meter's amount-not-phase back-reaction confounds the PHASE recurrence return in the full-discharge regime), routed to a phase-faithful-meter SPEC + the click mechanism. The regime gate PASSED — the question was genuinely asked at the certified cell, and the SUFFICIENT collapse-at-`x≈1` signature is decisively absent.*
