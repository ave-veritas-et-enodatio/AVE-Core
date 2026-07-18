# F6 counting-arrow arm — recurrence-sweep — RESULT (Phase 1)

**Date:** 2026-07-18 · **Class:** result (Phase-1 fire; honest closure)
**Prereg (FROZEN):** [`2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md`](2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md) — §0–§7 frozen-by-push 2026-07-18T00:36:15Z, **before** any driver code.
**Driver:** `src/scripts/vol_1_foundations/f6_counting_arrow_arm.py` · **Data:** `2026-07-18_f6-counting-arrow-arm_result.json`
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` — **byte-untouched**). **Plant:** standalone-K4 (within the meter certificate; #721 R-1 SCOPE CAVEAT).

> ## ★ VERDICT — RE-BANKED (PR #722 review R-2 / R-4 / R-5 / R-7)
>
> **Banked (frozen):** the frozen recurrence-collapse **PREDICTION is FALSIFIED at the frozen `κ=0.012`.** The two headline criteria fail decisively (§2): collapse `spread(x_50)=7.35` (frozen `<0.30`), transition `mean(x_50)=7.58` (frozen `[0.7,1.5]`). One mechanism explains every failure: the collar-drive is **narrowband** (dominant `ω_d≈0.524` — R-7 re-measured; the earlier prose `≈0.54` was a transcription drift off the #721-banked `0.52377`), filling only a **few-mode sub-band** (`N_occ≤3`), and the **weak-`κ` transfer is SLOW — `τ_transfer≈5·T_rec ≫ T_rec`** (R-7 per-cell `2.3–10`), inverting the clean-separation the prereg's construction implied. The return is **coupling/detuning-controlled** (`x≈4–11`), **not** comb-recurrence-controlled (`x=1`); changing `Δω` moves `T_rec` but not `τ_transfer`, so `R_return` does **not** collapse in `x`.
>
> **Banked bin readings — BOTH stated (Rule 11: code un-retuned):** the **shipped classifier** (fire-conditions frozen in prereg §4; tree + precedence = post-freeze implementation) returns **`FRICTION-RENAMED`**, a semantic misfire (§4). The **honest un-narrowed frozen reading is `FOREIGN-EATER`** — the shipped `sparse_ok` narrowed the frozen FOREIGN-EATER condition ("return failure NOT tracking `x`") to a two-control check, and a faithful reading of the frozen §4 row **fires FOREIGN-EATER on this data** (§7, R-5). The **FOREIGN-EATER-vs-FRICTION-RENAMED bin adjudication is ROUTED to Grant.**
>
> **NOT banked — ROUTED (R-4):** the regime-interpretation **`NULL-OF-REGIME`** (this run's drive never reached the fast-transfer / populated-quasi-continuum regime) is the **lane's ROUTED interpretation**, carried to Grant *with* the bin adjudication — it is **not one of the frozen §4 classes and is NOT banked as a verdict.**
>
> **★REMAINS OPEN (R-2):** the **counting-arrow QUESTION was not reached and REMAINS OPEN** — the regime (fast transfer + populated quasi-continuum) never existed in this run; **FALSIFIED scopes to the frozen recurrence-sweep prediction at `κ=0.012`, not to the counting arrow.** Review-probe evidence (§6 follow-on 3) shows the regime **IS** reached at `κ=0.03–0.06` — Grant-gated. **Branch closed negative** (this arm as designed); follow-ons SPEC-only (§6).
>
> 🔴 *Rule-12 supersession (PR #722 review, 2026-07-18): the original banking headlined **NULL-OF-REGIME** as the frozen verdict class and quoted `ω_d≈0.54`. NULL-OF-REGIME is demoted here from a banked class to the lane's routed interpretation (R-4); `ω_d` is re-measured to `0.524` (R-7); the FALSIFIED disposition is scoped to `κ=0.012` (R-1/R-2). Original bytes preserved in git history.*

🔴 **Rule-12 supersession (PR #722 review R-3, 2026-07-18 — MAJOR honesty-lag correction; original preserved in git):** the original framed this as "the empirical-driver discipline working at full strength (Rule 10) … a bug static analysis could not surface." That is **retracted as FALSE.** The honest statement: this was a **PREREG-DESIGN MISS** — **both mechanism halves were derivable from the banked #721 meter data at freeze time** (production `N_occ`, W2 transfer rates; the #721 W-battery even banked `ω_d=0.52377` and per-point `transfer_frac` 0.11–0.26, and #721 merged ~35 min before the freeze the prereg itself cites). The fire **confirmed** rather than **discovered** the mechanism; the "Rule-10 at full strength" framing is **retracted.** The prereg's physics argument was sound *for an idealised equally-spaced comb* (`T_rec = 2π/Δω`); what it missed — that the settled-lattice collar drive is narrowband and the weak-`κ` transfer is slow — was already visible in the meter data it consumed.

---

## 1 · Sector header (result-time restatement)

- **Sector:** E-sector ε-store (F6 ε→T2 candidate). **Regime:** Regime I sub-yield, `A_max≈0.10` cold (Phase 1). **Plant:** standalone-K4, within the meter certificate; conservation identity-enforced (#721 R-1) and **audited green** (`max|E_lat+E_bath−E0|/E0 = 9.4e-14`).
- **Consistency-vs-emergence:** the intended **FORM** (counting-arrow collapse) did **not** manifest; nothing is banked at emergence-class. The only positive reads are **consistency-class** (energy conservation identity; sparse two-tank reversibility reproduced).

---

## 2 · Measured vs frozen prediction (the fire)

Every value declared in prereg §3 was run (6-comb density sweep + two-tank control + OFF control + tared bias). `x = T·Δω/2π`; `R_return = 1 − E_bath/E_bath_peak` (t≥peak, else 0); `R_cum` = its running max; `x_50` = first `x` with `R_cum ≥ 0.5`.

| Δω | M | T_rec | peak_frac (E_bath/E0) | N_occ | n_pop(>1%) | **x_50** | R_ret[0.3] | R_cum[10] | cons |
|---|---|---|---|---|---|---|---|---|---|
| 0.010 | 71 | 628 | 0.573 | 3 | 6 | **10.19** | 0.000 | 0.267 | 9.4e-14 |
| 0.015 | 48 | 419 | 0.965 | 2 | 2 | **8.05** | 0.000 | 0.616 | 2.7e-14 |
| 0.020 | 36 | 314 | 0.571 | 3 | 5 | **4.40** | 0.000 | 0.777 | 3.0e-14 |
| 0.030 | 24 | 209 | 0.322 | 1 | 3 | **8.28** | 0.000 | 0.791 | 3.2e-14 |
| 0.050 | 15 | 126 | 0.033 | 1 | 7 | **10.95** | 0.000 | 0.000 | 6.8e-15 |
| 0.080 | 10 | 79 | 0.029 | 1 | 7 | **3.60** | 0.000 | 0.917 | 7.7e-15 |
| two-tank M=2 (ω=0.5/0.7) | 2 | 31 | 0.015 | — | — | 6.43 | — | **0.987** | — |

**Frozen adjudication (prereg §2/§4 thresholds, applied verbatim — no retune):**

| criterion (frozen) | threshold | measured | verdict |
|---|---|---|---|
| collapse `spread(x_50) < 0.30` | 0.30 | **7.347** | ❌ FAIL (25× over) |
| transition `mean(x_50) ∈ [0.7,1.5]` | [0.7,1.5] | **7.577** | ❌ FAIL |
| sparse-control returns `R_cum(x≫1) > 0.70` | 0.70 | 0.917 | ✅ (two-tank reversibility reproduced) |
| dense pins low `R_ret(0.3) < 0.30` | 0.30 | 0.000 | ✅ (but **trivially** — see §3) |
| energy conserved `< 1e-3` | 1e-3 | 9.4e-14 | ✅ (identity, #721 R-1) |
| OFF recovers Ax3 `< 1e-10` | 1e-10 | 2.1e-15 | ✅ |
| mode-count `N_occ dense > sparse` | — | 1 vs 1 | ❌ FAIL |
| protected-core bias (tared) `< 0.05` | 0.05 | 0.000 | ✅ |

The two **headline** criteria (collapse + transition-at-`x≈1`) fail **decisively**: `x_50` spreads over the entire swept range with **no trend toward collapse** and **no clustering near `x=1`**.

---

## 3 · The single mechanism (explains every failure)

> **Two coupled facts, one root.** (a) **The collar-drive from a settled K4 lattice is narrowband** (dominant `ω_d ≈ 0.524` — R-7 re-measured; the earlier prose `≈0.54` drifted off the #721-banked `0.52377`), so it fills only a **narrow few-mode sub-band** around `ω_d` — a **handful** of modes (`N_occ ≤ 3` at the observation horizon, the load-bearing meter count; corroborative `n_pop(>1%)` re-measured `2–10` per-cell, R-7), never the full swept comb — and *which* teeth fill is a **resonance accident**. (b) **The weak coupling `κ=0.012` makes the transfer SLOW:** `E_bath` trickles in *monotonically over several recurrence-times*, peaking at `x_peak = τ_transfer/T_rec ≈ 5` (R-7 re-measured per-cell `2.3–10`; all `≫ 1`). So **`τ_transfer ≈ 5·T_rec ≫ T_rec`** — the exact **inverse** of the fast-transfer `τ_decay ≪ T_rec` (Wigner–Weisskopf fast-decay) clean-separation implicit in the prereg's construction. The recurrence at `T_rec` is **masked by ongoing transfer**; the return only appears *after* the transfer peaks, at `x ≈ 4–11`, and is set by `κ`/detuning, **not** by `2π/Δω`. *(Provenance of `ω_d`, `n_pop`, `τ_transfer/T_rec`: §8, banked in `…_result.json["diagnostics"]`.)*

Every observed failure is downstream of this one root:

- **Non-collapse of `x_50`** — changing `Δω` moves `T_rec` but **not** `τ_transfer` (weak-`κ`, narrow sub-band), so the return does **not** track `x = T·Δω/2π`. `x_50` spreads 3.6 → 11 with no clustering near 1.
- **`peak_frac` is resonance-accident-controlled** (0.03 → 0.97): `Δω=0.015` happened to place a tooth on `ω_d` (96% transfer); `Δω=0.05` placed none nearby (3%). Density does not monotonically raise transfer.
- **`R_ret(0.3)=0` for EVERY comb** *trivially* — at `x=0.3` the slow transfer is still in progress (`x_peak≈5`), so "dense-end pins low" passes for the wrong reason (transfer incomplete), not dense-end irreversibility.
- **`N_occ` does not build a quasi-continuum with density** — at the frozen `κ=0.012` the narrowband drive fills only a drive-linewidth sub-band no matter how fine the comb (`N_occ` stays single-digit, `≪ M`). *(Scoped to `κ=0.012` per R-1: review-probe evidence shows the quasi-continuum IS populated at `κ=0.03–0.06`, §6 follow-on 3.)*
- **Two-tank sloshing survives** (`R_cum[10]=0.987`) precisely because its two modes both sit *in* the drive band — the reversibility positive control passes, confirming the instrument is live and the failure is regime, not a dead coupling.

**Regime read (regime-discipline).** The counting-arrow (mode-spread with reconvergence ≈ 0) *requires* a populated quasi-continuum. On this arm, **at the frozen `κ=0.012`**, that regime is **not reached** — so this null is an **ARTIFACT of the arm design (narrowband drive at `κ=0.012`), not a falsification of the mode-count physics itself** (the counting-arrow QUESTION remains open — ★VERDICT R-2). It **is** a decisive falsification of *the frozen `κ=0.012` recurrence-sweep prediction*: at that coupling the recurrence-sweep, driven by a settled-lattice collar, **cannot exhibit** the counting-arrow. *(Scoped to `κ=0.012` per R-1: at `κ=0.03–0.06` the regime IS reached — §6 follow-on 3, Grant-gated.)*

---

## 4 · The classifier label — FLAGGED (flag-don't-fix; Rule 11)

The **shipped classifier** (fire-conditions frozen in prereg §4; the decision-tree + precedence are **post-freeze implementation**, not frozen) returns **`FRICTION-RENAMED`**. This is a **semantic misfire**, surfaced here (not silently relabelled):

- **Why it fires:** prereg §4 mapped "criterion-7 (`N_occ dense > sparse`) fails → FRICTION-RENAMED," and the shipped tree checks that **before** the collapse/transition logic that would route to FOREIGN-EATER. `N_occ dense (1) > sparse (1)` is False ⇒ short-circuit.
- **Why it is wrong semantically:** the door charter's **FRICTION-RENAMED** (`2026-07-15_f6-mode-count-door_CHARTER.md` §4 bin vi) is "energy leaves the field **but** bath shows **no** mode-count increase (Q-drop / damping alone) → Ax3-illegal." Here the bath **does** gain modes (`N_occ 1–3 > 0`; `E_bath` up to 97% of `E0`), the energy is **stored reversibly and returns** (`R_cum` up to 0.92), and total energy **conserves to `9e-14`**. **There is no dissipation.** This is **not** the Ax3-illegal friction class.
- **The honest frozen-classifier answer is FOREIGN-EATER, not FRICTION-RENAMED (R-5).** The frozen §4 FOREIGN-EATER row is "return failure **NOT tracking `x`** … INSTRUMENT-first, fail closed." The return here decisively **does not track `x`** (that is the headline finding — `x_50` spreads `3.6→11`), so **a faithful implementation of the frozen row FIRES FOREIGN-EATER on this data.** The shipped `sparse_ok` (`f6_counting_arrow_arm.py:225,:240,:253`) tests **only the sparsest comb + the two-tank**, narrowing the frozen FOREIGN-EATER fire condition to its parenthetical example ("sparse control fails to return") — both extreme controls do return, so the tree fell through to FRICTION-RENAMED. This narrowing was **undisclosed at push; corrected here.**

**Disclosed prereg deviation (finding, not a fix; R-5):** the honest frozen-classifier answer on this data is **FOREIGN-EATER** (return not tracking `x`), not the FRICTION-RENAMED the shipped tree returned; the shipped tree **narrowed the frozen FOREIGN-EATER condition** (undisclosed at push). Per **Rule 11 the code is left UN-RETUNED**; **both readings are stated** and the **FRICTION-RENAMED-vs-FOREIGN-EATER adjudication stays routed to Grant** (with `NULL-OF-REGIME` = the lane's routed regime-interpretation, not a frozen class). The physical conclusion — falsification via the narrowband few-mode drive + `τ_transfer ≫ T_rec` inversion — is **unambiguous regardless of the bin label**.

---

## 5 · Companion leg (SECONDARY — non-gating; inconclusive)

Self-termination size sweep `N ∈ {8,10,12,16}` (prereg §6). Result: the emergent-`Re(Z_in)/Z_char` proxy is **negligible** (`0.000 → 0.002`, weakly monotone in `N`) and the port region **retains** its energy (`e_port_frac_min ≈ 1.0` — the localized impulse excites mostly local/few modes and does not disperse into a bulk continuum). **Consistent with the primary finding** (no quasi-continuum populated). Reported at consistency-class only; `Z₀=√(L_bond/C_bond)` is calibration and is **not** approached. **This leg does not (and by prereg §6 cannot) change the arm verdict.**

---

## 6 · Disposition (Rule-12: retract, do not refill)

- **Retract** the **frozen `κ=0.012` recurrence-sweep PREDICTION**; the arm-as-designed does **not reach the regime**; the **counting-arrow question stays open** (see follow-on 3). Branch **closed negative** (this arm as designed).
- **Do not refill the slot** with a new unverified hypothesis. Three routed follow-ons are **SPEC only** (each earns its own prereg + verification chain if pursued):
  1. **Broadband-sustained-drive redesign** — a drive that *keeps* injecting broadband content (not "source-off") could populate a quasi-continuum across the comb, letting `Δω` genuinely control the recurrence. This changes the frozen drive protocol ⇒ a **new prereg**, not a retune of this one.
  2. **Route to the click mechanism** — the corpus's *other* licensed arrow source (X40 energy-conserving click; `retention-transition-split.md:34`), which does not depend on populating a mode continuum.
  3. **★κ-sweep rerun of the same frozen grid (new prereg) — now the CHEAPEST follow-on.** Review-probe evidence (PR #722 review, disclosed scratch probe) shows at `κ=0.03–0.06` the regime **IS** reached: fast transfer (`x_63 = 0.19·T_rec`), `N_occ 15→33/47 of 71` (quasi-continuum populated), dense combs fully irreversible (`R_cum=0.000`) while sparse (`0.793 > 0.70`) and two-tank (`0.996`) controls pass — **the necessary counting shape appears; NOT sufficient** (`x_50 = nan` at dense — the collapse-at-`x≈1` remains unshown). **MANDATORY prerequisites:** (a) meter W-battery **revalidation at the new `κ`** (conservation drift degrades `1e-14 → 6.8e-6 @0.03 → 4.3e-4 @0.06` — the #721 scope-caveat trigger); (b) valid band **bounded above by the `κ=0.12` two-tank-control break**; (c) **dressed-comb / level-repulsion artifact check**. **Grant-gated, not fired.**
- **Untouched:** the depletion **rate** rung (`Γ=3Hρ_latent`) and the meter certificate (byte-untouched; standalone-K4 identity intact).

---

## 7 · Prereg deviations (disclosed)

1. **§4 bin mapping (criterion-7 → FRICTION-RENAMED)** conflates the driver fingerprint with the charter's dissipation condition (§4 above). Classifier stands as-run (Rule 11); the honest frozen bin is **FOREIGN-EATER** (with `NULL-OF-REGIME` = the routed regime-interpretation); routed to Grant.
2. **★FOREIGN-EATER narrowing (undisclosed at push — corrected here; R-5).** The shipped `sparse_ok` (`f6_counting_arrow_arm.py:225,:240,:253`) tests **ONLY the sparsest comb + the two-tank**, narrowing the frozen FOREIGN-EATER fire condition ("return failure NOT tracking `x`"). A **FAITHFUL implementation of the frozen §4 row FIRES FOREIGN-EATER on the shipped data** (the return decisively does not track `x`). So **the honest frozen-classifier answer on this data is FOREIGN-EATER, not FRICTION-RENAMED**; the shipped tree narrowed the condition (undisclosed at push). Code left **un-retuned per Rule 11**; adjudication stays **routed to Grant with BOTH readings stated**. *(This supersedes the previous item-3 "No other deviation" claim, which is retracted.)*
3. **Physics-premise deviation:** the fast-transfer (`τ_decay ≪ T_rec`) Wigner–Weisskopf regime was **implicit in the prereg's `t_peak`/transfer-complete construction and prediction-4 derivation (never stated as a frozen clause)** (R-3/R-8 merged); the integrator shows the **inverted** regime `τ_transfer ≈ 5·T_rec ≫ T_rec` (weak-`κ` transfer into a narrow drive-linewidth sub-band). This is the finding, not an error to patch.

---

## 8 · Regime-diagnostics provenance (PR #722 review R-7)

**The gap (MAJOR, disclosed):** the regime-diagnosis numbers (`ω_d`, `n_pop(>1%)`, `x_peak`/`τ_transfer/T_rec`) existed **only in prose** at push — no shipped script computed them. A shipped diagnostics read now does (`f6_counting_arrow_arm.run_diagnostics`; `--diagnostics`; banked in `…_result.json["diagnostics"]`). **NON-GATING** (the frozen verdict is untouched). Definitions: `ω_d` = dominant angular frequency of the collar coordinate `q(t)` (mean-subtracted rFFT power peak); `n_pop(>1%)` = bath modes with `E_m > 1% of E_bath_peak` at `t_peak`; `τ_transfer/T_rec = t_peak/T_rec`. **The load-bearing few-mode count is the meter's `N_occ` (banked per-cell in `sweep`, `1–3`); `n_pop` is corroborative color.**

**Re-measured vs prose (both stated, R-7 — do not silently adopt):**

| `Δω` | prose `ω_d` | **meas `ω_d`** | prose `n_pop` | **meas `n_pop`** | prose `τ/T_rec` | **meas `τ/T_rec`** |
|---|---|---|---|---|---|---|
| 0.010 | 0.54 | **0.5236** | 6 | **7** | ≈5 | **9.03** |
| 0.015 | 0.54 | **0.5236** | 2 | **2** | ≈5 | **3.35** |
| 0.020 | 0.54 | **0.5236** | 5 | **5** | ≈5 | **2.99** |
| 0.030 | 0.54 | **0.5236** | 3 | **3** | ≈5 | **5.04** |
| 0.050 | 0.54 | **0.5228** | 7 | **10** | ≈5 | **10.02** |
| 0.080 | 0.54 | **0.5236** | 7 | **6** | ≈5 | **2.28** |

- **`ω_d`:** re-measured `0.524` (representative/median), uniform across combs — a **lattice property**, comb-independent (weak-`κ`). The prose `0.54` is a **transcription drift**; the re-measured value **confirms the #721 W-battery bank `ω_d=0.52377`** (`2026-07-17_f6-meter-nonlinear-reval_result.json`). Not a verdict-level number.
- **`n_pop(>1%)`:** re-measured `{7,2,5,3,10,6}` vs prose `{6,2,5,3,7,7}` — **differs at three cells** (the prose was eyeballed; no provenance script existed). The differences do **not** move the verdict: the load-bearing few-mode claim rests on `N_occ` (`1–3`, meter-computed, banked, bit-identical), not on `n_pop`. The largest re-measured value (`10` at `Δω=0.050`) sits on a **weak, detuned transfer** (`peak_frac=0.033`) — energy spread thin over a tiny peak — and is stated honestly rather than narrowed.
- **`τ_transfer/T_rec`:** re-measured per-cell `2.3–10` (median ≈ 4.2). The prose `≈5` is a fair **central** value; every cell is `≫ 1`, so the load-bearing **`τ_transfer ≫ T_rec`** inversion holds unchanged.

---

*Honest closure (Rule 11): clean negative, single mechanism named (narrowband few-mode drive + `τ_transfer ≫ T_rec` inversion, not counting), branch closed, follow-ons SPEC'd not claimed. Nothing is banked at emergence-class. The **frozen recurrence-sweep PREDICTION is FALSIFIED at `κ=0.012`**; the shipped classifier's `FRICTION-RENAMED` output is flagged as a semantic misfire (honest frozen reading = `FOREIGN-EATER`), `NULL-OF-REGIME` is the routed regime-interpretation, and the bin is routed for adjudication — not silently converted to a pass or to a different bin. The **counting-arrow question REMAINS OPEN.***
