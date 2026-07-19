# F6 thermal-floor arm — revival-vs-floor — RESULT

**Date:** 2026-07-19 · **Class:** result (the fire; honest closure, Rule 11 — a pre-registered prediction fails decisively and one mechanism explains it).
**Prereg (FROZEN):** [`2026-07-19_f6-thermal-floor-arm_prereg_FROZEN.md`](2026-07-19_f6-thermal-floor-arm_prereg_FROZEN.md) — §0–§7 frozen-by-push `2026-07-19T22:31:10Z` (API committedDate), **BEFORE any arm driver code existed** (freeze margin ≈ **5.5 min**, push→first-arm-code).
**Driver:** `src/scripts/vol_1_foundations/f6_thermal_floor_arm.py` · **Data:** `2026-07-19_f6-thermal-floor-arm_result.json` · **Test:** `src/tests/test_f6_thermal_floor_arm.py`
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` — **BYTE-UNTOUCHED**; floor = config-only). **Certificate consumed:** FLOOR-METER-VALID-BAND[0,5] (STAGE-1). **Plant:** standalone-K4, κ=0.030 MILD.

> ## ★ VERDICT — **NO-SUPPRESSION** (frozen §4 tree, byte-faithful; self-check `match=True`)
>
> **The static pre-occupied noise floor does NOT set the local arrow by dephasing.** The coherent revival **rides on top of the floor essentially unchanged** across the whole certified band `ρ ∈ [0, 5]` (floor from below-signal to 5× signal-per-mode). **Grant's ride-on-top alternative is CONFIRMED; the FLOOR-ARROW hypothesis (revivals die as the floor rises past the signal) is FALSIFIED at this cell.**
>
> **★The clean evidence (ensemble-average-first coherent revival — jitter cancels √6).** Averaging the excess ledger `ΔE_bath(t)` over the 6 frozen seeds BEFORE taking the dip removes the random floor jitter (the coherent revival is seed-independent; the floor phases are random and cancel). The resulting **coherent revival is FLAT at `~0.90` across the entire ρ ladder** — `0.899 (ρ=0) → 0.903 → 0.908 → 0.915 → 0.920 → 0.923 (ρ=5)` — a `+2.7%` change, well inside the ensemble SEM. **It does not decay with ρ.** (`ρ=0` is the unambiguous cold revival, `0.899`, reproducing the banked #726 `Δω=0.050` value bit-for-bit; it stays there as the floor rises.)
>
> **★The mechanism (Rule 11 — one root, honest closure).** The bath is a set of **INDEPENDENT harmonic oscillators** (Caldeira–Leggett; free rotation is per-mode, linear). The signal modes were driven coherently and re-phase at their recurrence **independently of the floor modes' random phases** — there is **NO mode–mode coupling** in the lossless-reactive bath, so a static random floor **SUPERPOSES with** rather than **DEPHASES** the coherent revival. Dephasing-that-sets-the-arrow requires a **mode-coupled / interacting / dissipative** bath (thermalization), which the Ax3 lossless-reactive regime does **not** provide. This one mechanism explains every ρ cell: the revival is untouched because the floor and the signal never interact.
>
> **★Observable-artifact DISCLOSED (fire-time finding, the #726 R-1 class; flag-don't-fix).** The frozen §4 `S(ρ)` metric (per-seed `R_cum` normalized by the excess first-plateau, minus the detuned control) is **partly artifactual**: (a) the detuned control's `R_rev` **blows up** (`0.875–1.5`) because dividing `R_return = 1 − ΔE_bath/plateau` by the detuned's near-zero no-transfer plateau (`≈0.0096`) explodes — so `detuned_valid=False` is the **normalization symptom, not a resonance-gating failure** (the detuned transfer IS gated: plateau `0.0096 < 1e-2`); (b) floor-pumping drives `ΔE_bath` negative, inflating the raw per-seed `R_cum > 1` (`0.90 → 1.39` with ρ) — an artifact of the amount-channel back-reaction, not a revival. **The verdict is ROBUST to this:** the frozen §4 tree returns NO-SUPPRESSION because `S(ρ)` does **not decrease** (it increases, `ratio5 = 7.07 ≥ 0.80`), AND the clean ensemble-average-first reading independently returns NO-SUPPRESSION (flat coherent revival). Both point the same way; the broken metric could not have hidden a real suppression (a suppression would have decreased **both** readings).
>
> **NOT banked:** any FLOOR-ARROW / arrow-of-time-from-noise-floor result; nothing at emergence-class. The depletion-rate rung (`Γ=3Hρ_latent`), the growth/node-genesis picture (re-homed), and the #721/#724/§D certificates are untouched. Meter module + K4 engine **byte-untouched** (floor = config-only).

---

## 1 · Sector header (result-time restatement)

- **Sector:** R7 thermal / entropy-sink (F6 ε→T2 candidate). **NOT** A1 mass, **NOT** Cosserat (2,3) winding/charge. **Regime:** Regime I sub-yield, `A_max≈0.10` MILD, κ=0.030; driven-then-source-off; closed cavity (pml=0). **Plant:** standalone-K4, conservation identity-enforced and audited green (`max drift = 2.3e-14 ≪ 1e-6`, no clamp).
- **The ruling under test (Grant verbatim, [sic]):** "my gut says its couples through a static noise floor" / "so wffectively constant" / "the noise floor woild set the arrow of time right?" — **tested, falsified at this cell** (the floor does not dephase the coherent revival).
- **Consistency-vs-emergence:** the FLOOR-ARROW **FORM** (revival suppression tracking ρ) was **not observed** — a clean **CONSISTENCY-class negative**. Nothing at emergence-class.

---

## 2 · The fire (every §3 grid value run; revival-vs-ρ table)

Primary comb `Δω=0.050, M=15`; sparse `Δω=0.080, M=10`; detuned band `ω_min=1.18, q-frac=2.1e-3` (FROZEN `_place_detuned_band`). 6-seed ensemble; window `11·T_rec`.

| ρ | floor/E0 | **coherent revival (eaf, CLEAN)** | raw `R̄_rev` (§4, artifact) | ±SEM | detuned `R̄_rev` (artifact) | detuned plateau (gated) | primary plateau | drift |
|---|---|---|---|---|---|---|---|---|
| 0.0 | 0.00 | **0.899** | 0.899 | 0.000 | 0.875 | 0.0096 ✅ | 0.193 | 7.7e-15 |
| 0.3 | 0.14 | **0.903** | 0.942 | 0.036 | 1.497 | 0.030 | 0.194 | 2.3e-14 |
| 1.0 | 0.47 | **0.908** | 1.032 | 0.084 | 1.455 | 0.053 | 0.224 | 1.8e-14 |
| 2.0 | 0.93 | **0.915** | 1.148 | 0.117 | 1.418 | 0.076 | 0.252 | 2.0e-14 |
| 3.0 | 1.40 | **0.920** | 1.255 | 0.137 | 1.366 | 0.098 | 0.275 | 1.6e-14 |
| 5.0 | 2.33 | **0.923** | 1.389 | 0.166 | 1.218 | 0.135 | 0.311 | 1.5e-14 |

**The load-bearing column is the coherent revival (eaf): FLAT `~0.90` across ρ ∈ [0,5]** — the revival is NOT suppressed. The raw `R̄_rev` and detuned columns are the artifact-laden frozen §4 ingredients (disclosed); they do not decrease either.

| criterion (frozen §4) | threshold | measured | verdict |
|---|---|---|---|
| CONSERVATION (all cells) | `< 1e-6` | `2.3e-14` | ✅ |
| CLAMP-NEVER (all cells) | none clamp | none | ✅ (the band [0,5] holds) |
| COLD-CONTROL-REPRODUCES (ρ=0 bit-for-bit) | `diff = 0.0` | `0.0` | ✅ (ρ=0 = banked #726 `Δω=0.050`) |
| DETUNED transfer-gated (ρ=0) | plateau `< 1e-2` | `0.0096` | ✅ (resonance-gating alive) |
| DETUNED `R_rev` sub-primary | `< 0.5·primary` | `0.875` (artifact) | ❌ (normalization blowup — disclosed, not a gating failure) |
| `S(5)/S(0) ≥ 0.80` ⇒ NO-SUPPRESSION | 0.80 | **7.07** (S does not decrease) | ✅ → **NO-SUPPRESSION** |
| coherent revival decays with ρ (eaf) | monotone ↓ | **flat `+2.7%`** | ❌ FLOOR-ARROW falsified |

Frozen §4 tree → **NO-SUPPRESSION** (byte-faithful; `self_check.match=True`).

---

## 3 · The mechanism (Rule 11 — one root explains every cell)

**One root: the lossless-reactive bath has no mode–mode coupling, so a static floor cannot dephase a coherent revival.** Each bath oscillator free-rotates independently (`OscillatorBath.free_rotate` is diagonal in the mode basis). The coherent signal — driven from the collar with a fixed phase relation — re-coheres at its recurrence **on its own**, and the pre-seeded floor (random per-mode phases) evolves **alongside** it without exchanging energy mode-to-mode. When the excess ledger is ensemble-averaged, the floor's random contribution cancels (√6) and the **intact** coherent revival is exposed, flat at `~0.90` for every ρ. The floor's only channel to the signal is the **shared collar + amount-channel back-reaction** (weak, κ=0.03), which the ensemble-average removes as random jitter and which — being amount-not-phase (§A1) — cannot carry phase information between floor and signal anyway.

**Why Grant's picture fails HERE (regime-scoped, honest).** "A noise floor sets the arrow" is a **thermalization** intuition — it requires the floor to *scramble* the signal's phase, which needs **interaction** (mode coupling, nonlinearity, or dissipation). The Ax3 **lossless-reactive** regime this meter operates in is **linear and non-interacting** by construction (the honest no-valve rail), so the floor and signal **superpose** rather than thermalize. The arrow-from-noise-floor mechanism is **inexpressible** on a non-interacting reactive bath — the same structural reason the #721 conservation was an identity. This does not falsify arrow-from-thermalization in an *interacting* bath (untested); it falsifies **arrow-from-a-STATIC-REACTIVE-floor** at this cell.

**Regime read.** Not numerical (drift `2e-14`, no clamp). Not a dead coupling (the floor exchanges — jitter grows with ρ, FD leg §5). Not a masked signal (both the clean eaf AND the frozen §4 tree agree on no-suppression). A clean, mechanism-named negative.

---

## 4 · Disposition (Rule 12 — retract, do NOT refill)

- **Retract** the frozen **FLOOR-ARROW prediction** (revival amplitude decays with ρ). It is **decisively not observed**; the coherent revival is flat across ρ ∈ [0,5]. **Branch closed negative.** Grant's **ride-on-top alternative** (NO-SUPPRESSION) is confirmed.
- **Do NOT refill the slot.** The routed follow-ons are **SPEC only** (each earns its own charter + verification chain if pursued):
  1. **★The dephasing arrow needs an INTERACTING bath (SPEC; the mechanism this fire named).** A floor that dephases a coherent revival requires **mode–mode coupling** (a nonlinear / interacting / genuinely dissipative bath), absent in the lossless-reactive Caldeira–Leggett comb. This is a **meter/physics change** (breaks the #721 identity ⇒ full W/X/floor-battery re-cert) — SPEC, NOT built. It is the honest next home for "does thermalization set the local arrow?"
  2. **The observable needs an interaction-robust revival metric** — the frozen §4 `S(ρ)` normalization is artifactual off-plateau (disclosed §2); a future interacting-bath arm should use the **ensemble-average-first coherent-revival** metric (the eaf here, well-defined) as the gating observable.
- **Re-homed / MOOT (unchanged):** the growth/node-genesis picture stays at the cosmological rate rung; the DOS-balance A/B fork stays MOOT (bath-emptiness, not head-count).
- **Untouched:** depletion-rate rung; #721/#724/§D certificates; meter module + K4 engine (byte-untouched; floor = config-only).

---

## 5 · The FD leg (SECONDARY — non-gating; §7; NO claim minted)

The floor-injected fluctuation (ensemble seed-spread of `R_rev`, a fluctuation proxy) vs the relaxation rate (`t_fp / T_rec`, the excess-transfer 1/e time). **FD ratio = fluctuation / relaxation** per ρ (exploratory data routed to the ℏ-as-FD open; **excluded from the §4 verdict**):

| ρ | 0.0 | 0.3 | 1.0 | 2.0 | 3.0 | 5.0 |
|---|---|---|---|---|---|---|
| FD ratio | 0.000 | 0.051 | 0.088 | 0.092 | 0.107 | 0.129 |

The fluctuation proxy grows with ρ (more floor ⇒ more jitter) while the relaxation time is roughly ρ-stable, so the FD ratio rises smoothly with the floor level. **No fluctuation-dissipation theorem is asserted;** banked for the routed open only.

---

## 6 · Independent re-derivation + gates + provenance

- **Independent re-derivation from the raw banked JSON (the #726 F9 lesson — NOT the driver's own booleans):** `src/tests/test_f6_thermal_floor_arm.py` loads `…_result.json` and, using **only** the raw per-ρ ensemble fields, independently re-derives: (i) the coherent revival (eaf) is flat (`max − min ≤ 0.05`, non-decreasing) across ρ ∈ [0,5]; (ii) `S(5)/S(0) ≥ 0.80` ⇒ NO-SUPPRESSION by the frozen tree; (iii) every cell conserves (`< 1e-6`) with no clamp; (iv) ρ=0 reproduces the banked cold revival bit-for-bit; (v) the detuned transfer is gated (`plateau(ρ=0) < 1e-2`) while its `R_rev` is the disclosed artifact. It **also** runs a **live** ρ=0 and ρ=5 primary cell and asserts the coherent revival does not drop. The independent re-derivation reproduces **NO-SUPPRESSION**.
- **Diagnostics provenance:** every number is driver-computed and banked in `…_result.json` — the ensemble `R̄_rev`/SEM per ρ/comb, the clean `ens_avg_first` coherent revival, `S(ρ)` primary + sparse, the detuned reads, per-cell drift/clamp, the cold-control bit-for-bit diff, the **Rule-10 reactance pair** (bath C-state AND L-state across the window at ρ∈{0,1,5} on the primary comb), and the FD-leg rows. Nothing prose-only.
- **Gates:** `ruff check` clean; `make verify` green; the classifier self-check `match=True` (a precedence guard — the genuinely independent check is the test's raw-JSON + live re-derivation).
- **Prereg deviations (DISCLOSED):** the frozen §4 `S(ρ)` observable is **partly artifactual off-plateau** (§2, the detuned-normalization blowup + floor-pumping `R_cum>1`) — a fire-time finding (#726 R-1 class), disclosed not silently fixed; the verdict is robust to it (§0/§2). The `ens_avg_first` coherent-revival metric was **pre-registered as a non-gating cross-check** (§4 "banked as a disclosed non-gating cross-check") and is the clean corroborator. No threshold was retuned (Rule 11).
- **Freeze margin (real):** prereg frozen-by-push `2026-07-19T22:31:10Z`, arm driver first written `~22:36:38Z` (≈5.5 min); the revival-vs-ρ prediction was UNMEASURED at freeze.

---

*Honest closure (Rule 11 / Rule 12): the pre-registered **FLOOR-ARROW** prediction — the static noise floor's phase-randomness sets the local arrow by dephasing coherent revivals — **fails decisively**. Across the certified band `ρ ∈ [0, 5]` the coherent revival (ensemble-average-first, clean) is **flat at `~0.90`**; it does not decay with the floor. **One mechanism explains every cell:** the lossless-reactive Caldeira–Leggett bath has **no mode–mode coupling**, so a static random floor **superposes with** rather than **dephases** the coherent revival — dephasing-that-sets-the-arrow requires an interacting/dissipative bath the Ax3 reactive regime does not provide. **Grant's ride-on-top alternative is confirmed; the branch is closed negative.** The frozen §4 `S(ρ)` observable is disclosed partly-artifactual (the #726 R-1 class), and the verdict is robust to it (both the frozen tree and the clean cross-check return NO-SUPPRESSION). The dephasing arrow, if it exists, lives in an **interacting** bath — SPEC only, not built. Nothing banked at emergence-class; the meter + engine are byte-untouched.*
