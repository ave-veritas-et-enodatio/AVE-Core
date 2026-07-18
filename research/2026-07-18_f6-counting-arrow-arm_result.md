# F6 counting-arrow arm — recurrence-sweep — RESULT (Phase 1)

**Date:** 2026-07-18 · **Class:** result (Phase-1 fire; honest closure)
**Prereg (FROZEN):** [`2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md`](2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md) — §0–§7 frozen-by-push 2026-07-18T00:36:15Z, **before** any driver code.
**Driver:** `src/scripts/vol_1_foundations/f6_counting_arrow_arm.py` · **Data:** `2026-07-18_f6-counting-arrow-arm_result.json`
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` — **byte-untouched**). **Plant:** standalone-K4 (within the meter certificate; #721 R-1 SCOPE CAVEAT).

> ## ★ VERDICT: the frozen recurrence-collapse prediction is **FALSIFIED** — as a **NULL-OF-REGIME**. The arm's collar-drive is **narrowband** (dominant `ω_d≈0.54`), so it fills only a **narrow few-mode sub-band** (not the full swept comb), and the **weak-κ transfer is SLOW: `τ_transfer ≈ 5·T_rec ≫ T_rec`** — inverting the clean-separation the prereg assumed. The return is **coupling/detuning-controlled** (peaks at `x≈5`), **not** comb-recurrence-controlled (`x=1`). Changing `Δω` moves `T_rec` but **not** `τ_transfer`, so `R_return` does **not** collapse in `x`. A single mechanism explains every failure. **Branch closed negative; routed (INSTRUMENT-first) to a broadband-sustained-drive redesign or the click mechanism.**
>
> **Frozen classifier label = FRICTION-RENAMED — FLAGGED as a semantic misfire** (see §4; energy is stored reversibly, `N_occ 1–3 > 0`, conserved to `9e-14`, and returns — it is **not** the charter's Ax3-illegal friction class). The mechanistically-correct frozen bin is **FOREIGN-EATER** (return **not** tracking `x` → INSTRUMENT-first). Routed to Grant for bin adjudication; **no post-fire retune** (Rule 11).

This is the **empirical-driver discipline working at full strength** (Rule 10): the prereg's physics argument was sound *for an idealised equally-spaced comb* (recurrence at `T_rec = 2π/Δω`), but the integrator revealed the collar-drive never populates that comb — a bug static analysis could not surface.

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

> **Two coupled facts, one root.** (a) **The collar-drive from a settled K4 lattice is narrowband** (dominant `ω_d ≈ 0.54`), so it fills only a **narrow few-mode sub-band** around `ω_d` — a **handful** of modes (`N_occ ≤ 3` at the observation horizon; transiently up to ~10 for the densest comb; `n_pop ≤ 7`), never the full swept comb — and *which* teeth fill is a **resonance accident**. (b) **The weak coupling `κ=0.012` makes the transfer SLOW:** `E_bath` trickles in *monotonically over ~5 recurrence-times*, peaking at `x_peak ≈ 5`. So **`τ_transfer ≈ 5·T_rec ≫ T_rec`** — the exact **inverse** of the prereg's assumed `τ_decay ≪ T_rec` (Wigner–Weisskopf fast-decay) clean-separation. The recurrence at `T_rec` is **masked by ongoing transfer**; the return only appears *after* the transfer peaks, at `x ≈ 4–11`, and is set by `κ`/detuning, **not** by `2π/Δω`.

Every observed failure is downstream of this one root:

- **Non-collapse of `x_50`** — changing `Δω` moves `T_rec` but **not** `τ_transfer` (weak-`κ`, narrow sub-band), so the return does **not** track `x = T·Δω/2π`. `x_50` spreads 3.6 → 11 with no clustering near 1.
- **`peak_frac` is resonance-accident-controlled** (0.03 → 0.97): `Δω=0.015` happened to place a tooth on `ω_d` (96% transfer); `Δω=0.05` placed none nearby (3%). Density does not monotonically raise transfer.
- **`R_ret(0.3)=0` for EVERY comb** *trivially* — at `x=0.3` the slow transfer is still in progress (`x_peak≈5`), so "dense-end pins low" passes for the wrong reason (transfer incomplete), not dense-end irreversibility.
- **`N_occ` does not build a quasi-continuum with density** — the narrowband drive fills only a drive-linewidth sub-band no matter how fine the comb (`N_occ` stays single-digit, `≪ M`).
- **Two-tank sloshing survives** (`R_cum[10]=0.987`) precisely because its two modes both sit *in* the drive band — the reversibility positive control passes, confirming the instrument is live and the failure is regime, not a dead coupling.

**Regime read (regime-discipline).** The counting-arrow (mode-spread with reconvergence ≈ 0) *requires* a populated quasi-continuum. On this arm, with this drive, that regime is **not reached** — so this null is an **ARTIFACT of the arm design (narrowband drive), not a falsification of the mode-count physics itself**. It **is** a decisive falsification of *this arm as designed*: the recurrence-sweep, driven by a settled-lattice collar, cannot exhibit the counting-arrow.

---

## 4 · The classifier label — FLAGGED (flag-don't-fix; Rule 11)

The frozen driver returns **`FRICTION-RENAMED`**. This is a **semantic misfire**, surfaced here (not silently relabelled):

- **Why it fires:** prereg §4 mapped "criterion-7 (`N_occ dense > sparse`) fails → FRICTION-RENAMED," and the decision-tree checks that **before** the collapse/transition logic that would route to FOREIGN-EATER. `N_occ dense (1) > sparse (1)` is False ⇒ short-circuit.
- **Why it is wrong semantically:** the door charter's **FRICTION-RENAMED** (`2026-07-15_f6-mode-count-door_CHARTER.md` §4 bin vi) is "energy leaves the field **but** bath shows **no** mode-count increase (Q-drop / damping alone) → Ax3-illegal." Here the bath **does** gain modes (`N_occ 1–3 > 0`; `E_bath` up to 97% of `E0`), the energy is **stored reversibly and returns** (`R_cum` up to 0.92), and total energy **conserves to `9e-14`**. **There is no dissipation.** This is **not** the Ax3-illegal friction class.
- **The mechanistically-correct frozen bin:** **FOREIGN-EATER** — "return failure **NOT tracking `x`** … INSTRUMENT-first investigation, fail closed" (prereg §4). The narrowband drive is exactly the "something else" that controls the return instead of counting.

**Disclosed prereg deviation (finding, not a fix):** prereg §4's criterion-7→FRICTION-RENAMED mapping conflated the driver's *fingerprint* criterion (`N_occ dense > sparse`) with the charter's *dissipation* criterion (`N_occ` does not increase from zero). Per **Rule 11 the classifier is NOT retuned** post-fire; the frozen label stands as-run, and this mismatch is **routed to Grant** for the correct bin (FRICTION-RENAMED vs FOREIGN-EATER/NULL-OF-REGIME). The physical conclusion — falsification via the narrowband few-mode drive + `τ_transfer ≫ T_rec` inversion — is **unambiguous regardless of the bin label**.

---

## 5 · Companion leg (SECONDARY — non-gating; inconclusive)

Self-termination size sweep `N ∈ {8,10,12,16}` (prereg §6). Result: the emergent-`Re(Z_in)/Z_char` proxy is **negligible** (`0.000 → 0.002`, weakly monotone in `N`) and the port region **retains** its energy (`e_port_frac_min ≈ 1.0` — the localized impulse excites mostly local/few modes and does not disperse into a bulk continuum). **Consistent with the primary finding** (no quasi-continuum populated). Reported at consistency-class only; `Z₀=√(L_bond/C_bond)` is calibration and is **not** approached. **This leg does not (and by prereg §6 cannot) change the arm verdict.**

---

## 6 · Disposition (Rule-12: retract, do not refill)

- **Retract** the recurrence-sweep hypothesis: the arm as designed does **not** carry the counting-arrow. Branch **closed negative**.
- **Do not refill the slot** with a new unverified hypothesis. Two routed follow-ons are **SPEC only** (each earns its own version + verification chain if pursued):
  1. **Broadband-sustained-drive redesign** — a drive that *keeps* injecting broadband content (not "source-off") could populate a quasi-continuum across the comb, letting `Δω` genuinely control the recurrence. This changes the frozen drive protocol ⇒ a **new prereg**, not a retune of this one.
  2. **Route to the click mechanism** — the corpus's *other* licensed arrow source (X40 energy-conserving click; `retention-transition-split.md:34`), which does not depend on populating a mode continuum.
- **Untouched:** the depletion **rate** rung (`Γ=3Hρ_latent`) and the meter certificate (byte-untouched; standalone-K4 identity intact).

---

## 7 · Prereg deviations (disclosed)

1. **§4 bin mapping (criterion-7 → FRICTION-RENAMED)** conflates the driver fingerprint with the charter's dissipation condition (§4 above). Classifier stands as-run (Rule 11); mechanistically-correct bin flagged FOREIGN-EATER/NULL-OF-REGIME; routed to Grant.
2. **Physics-premise deviation:** prereg §2 assumed the fast-transfer (`τ_decay ≪ T_rec`) Wigner–Weisskopf regime; the integrator shows the **inverted** regime `τ_transfer ≈ 5·T_rec ≫ T_rec` (weak-`κ` transfer into a narrow drive-linewidth sub-band). This is the finding, not an error to patch.
3. No other deviation: every declared grid value, control, and threshold was run verbatim.

---

*Honest closure (Rule 11): clean negative, single mechanism named (narrowband few-mode drive + `τ_transfer ≫ T_rec` inversion, not counting), branch closed, follow-ons SPEC'd not claimed. Nothing is banked at emergence-class. The classifier's `FRICTION-RENAMED` label is flagged as a semantic misfire and routed for adjudication — not silently converted to a pass or to a different bin.*
