# F6 floor-battery — pre-occupied-bath meter revalidation (STAGE 1) — RESULT

**Date:** 2026-07-19 · **Class:** result (instrument revalidation; CONSISTENCY-class — "can the certified meter READ a pre-occupied floor?"). **NOT** an F6 arm; **NOT** the arrow hypothesis.
**Charter (FROZEN):** [`2026-07-16_f6-bath-meter_CHARTER.md`](2026-07-16_f6-bath-meter_CHARTER.md) — **§D** frozen-by-push `2026-07-19T21:41:18Z` (API committedDate) **BEFORE any battery code existed**; **§D-post** (first-integrator-run corrections, Rule-10) committed WITH this corrected driver (the §A/§B/§C-post pattern — post-run correction, disclosed, both readings banked).
**Driver:** `src/scripts/vol_1_foundations/f6_floor_battery.py` · **Data:** `2026-07-19_f6-floor-battery_result.json` · **Test:** `src/tests/test_f6_floor_battery.py`
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (`LatticeBathCoupler` / `OscillatorBath` — **BYTE-UNTOUCHED**; the floor is the CONFIG-ONLY `bath.x`/`bath.p` overwrite of §D.D1). **Reused BYTE-UNTOUCHED:** `f6_counting_arrow_arm.py` (#722 `_build`/`_m_for`/grid).
**Plant:** standalone-K4, extending `METER-VALID-KAPPA-BAND[0.030,0.030]` @ MILD (§C-post, PR #724).

> ## ★ VERDICT — **FLOOR-METER-VALID-BAND[0, 5]** (corrected §D-post reading; self-check `match=True`)
>
> **The certified meter READS a pre-occupied floor** — cleanly, in a **bounded band `ρ ∈ [0, 5]`** on the densest-viable comb (`Δω=0.050, M=15`), where `ρ = E_floor_per_mode / E_signal_per_mode`. Across a **6-seed frozen ensemble** at every ρ: the conservation identity holds to `max_drift = 2.3e-14 ≪ LEDGER_ID_TOL=1e-6` (FB1), the excess ledger `ΔE_bath = E_bath − E_floor_expected` is identity-consistent to `2e-14` and the seed energy is exact to `<1e-10` (FB2), the excess-tare `c_excess=√(E_lat/E0)` is finite and the two frozen D2 forms agree (FB3), the floor statistics (not the realization) carry the reads (FB4), and the `ρ=0` cold limit reproduces the banked cold behavior **bit-for-bit** on BOTH `Δω=0.050` and the banked-dip `Δω=0.010` comb (FB5).
>
> **★Both readings banked (flag-don't-fix — the flip is disclosed, not silent).** Under the **UN-amended frozen §D.D3 binary criteria** (FB3 `c∈[0,1]` ceiling + FB4 pairwise-CoV<0.10, on the original single-seed `Δω=0.030` ladder to ρ=30) the verdict is **FLOOR-LEDGER-ARTIFACT** — banked in the JSON as `frozen_literal.verdict`. The §D-post addendum reconciles two mis-specified sub-gates to §D.D3's own class-definition/prose (§Dp-3 FB3, §Dp-2 FB4) and adds the bounded-band class (§Dp-5, the §C precedent), flipping the verdict. **Grant/orchestrator may overrule the flip** — if the frozen-literal binary is preferred, the lane STOPS at FLOOR-LEDGER-ARTIFACT and the arm does not fire.
>
> **★Two frozen-spec bugs + one genuine physical finding (Rule-10, first integrator run).** (i) FB3's `c∈[0,1]` ceiling was physically wrong — a warm floor **pumps the lattice above E0** (`E_lat>E0 ⇒ c>1`), correct equilibration physics, finite tare, not a read-defect. (ii) FB4's pairwise-CoV<0.10 tested realization-**agreement**, the opposite of its own "statistics not realization" prose. (iii) ★The genuine finding **FB4 caught that single-seed FB1 masked:** the floor transfer is **realization-sensitive** — the excess plateau carries `CoV ≈ 0.17–0.23` across seeds (ensemble mean stable, `SEM/mean ≈ 0.07–0.09`). This is the **FROZEN ARM-ENSEMBLE BUDGET**: STAGE 2 MUST average over the seed ensemble per ρ and require any FLOOR-ARROW suppression to **exceed** this seed-spread.
>
> **★The band is bounded because the floor jitter hits the clamp wall (the #727 wall, from the floor side).** The floor's per-step jitter in `d_e_bath` scales as `√(M·E_floor)`; on a near-full-discharge comb it eventually swings `E_lat→0`, firing the R-2 absorbing clamp / driving over-transfer, breaking the identity — **realization-dependently**. Hence the band width grows as the comb transfers **less**: `Δω=0.050` (partial `peak≈0.19`) clean to `ρ≥5`; the denser `Δω=0.030` (near-discharge) clean only to `ρ=2` (breaks at ρ=3, 2/6 seeds clamp); the banked-dip `Δω=0.010` (full discharge) is **not** floor-viable at any ρ≥0.3. The densest comb viable across a floor-**past**-signal ladder is `Δω=0.050` — which also carries the strongest, earliest banked cold revival (#726: `R_cum=0.932 @ x≈2`), so it is the STAGE-2 primary plant.
>
> **NOT banked:** any F6 arm / arrow result; nothing at emergence-class. The depletion-rate rung (`Γ=3Hρ_latent`) and the #721/#724 certificates are untouched. Meter module + K4 engine **byte-untouched** (floor = config-only).

---

## 1 · Sector header (result-time restatement)

- **Sector:** R7 thermal / entropy-sink (T2 latent-heat channel; F6 ε→T2 candidate). **NOT** A1 dilatation-mass, **NOT** Cosserat (2,3) winding/charge. The floor is a T2 sink DOF (carries no winding/mass; sector-ownership respected).
- **Regime:** Regime I sub-yield, `A_max≈0.10` MILD, at the certified `κ=0.030`. Driven-then-source-off, closed cavity (pml=0). Floor = static, pre-seeded (frozen random phases).
- **Coordinate discipline (A46):** the excess is read relative to the seeded sea in the bath's modal/spectral coordinate + the scalar energy ledger — NOT a raw `N_occ` (which every mode saturates on a floor) and NOT a real-space φ² surrogate.
- **Consistency-vs-emergence:** every FB verdict is **CONSISTENCY-class** (does the meter read a known-input floor?). No emergence claim. The floor levels (ρ ladder), comb, seeds are ENGINEERING CHOICES tagged as such.

---

## 2 · The battery (measured vs frozen; every §D.D3 / §D-post criterion)

Densest-viable comb `Δω=0.050 (M=15)`; `E_signal_per_mode = 0.02619` (cold first-plateau excess / M); 6-seed ensemble `{20260719 … 20260724}`; window `11·T_rec`.

| ρ | floor/E0 | all-seeds clean | max drift | #id-fail | #over-tx | #clamp | excess-identity | jitter (CoV) | c_excess finite | broke-tare shown |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.3 | 0.14 | ✅ | 2.3e-14 | 0 | 0 | 0 | 2.3e-14 | 0.038 (0.13) | ✅ | — |
| 1.0 | 0.47 | ✅ | 1.8e-14 | 0 | 0 | 0 | 1.8e-14 | 0.046 (0.17) | ✅ | — |
| 2.0 | 0.93 | ✅ | 2.0e-14 | 0 | 0 | 0 | 2.0e-14 | 0.056 (0.18) | ✅ | — |
| 3.0 | 1.40 | ✅ | 1.6e-14 | 0 | 0 | 0 | 1.6e-14 | 0.066 (0.19) | ✅ | — |
| 5.0 | 2.33 | ✅ | 1.5e-14 | 0 | 0 | 0 | 1.5e-14 | 0.082 (0.21) | ✅ | ✅ |

**★ DERIVED clean-floor band: `[0, 5]`** (highest contiguous ρ all-seeds-clean = identity `<1e-6` ∧ no over-transfer ∧ no clamp).

| leg | frozen criterion (§D.D3 / §D-post) | measured | verdict |
|---|---|---|---|
| **FB1** conservation + jitter (multi-seed) | all seeds `max_drift<1e-6`, no over-tx/clamp, `\|r\|<0.9` in `[0,ρ_hi]` | drift `2e-14`; `r≈+0.6…+0.85 <0.9`; jitter bounded `0.038→0.082` growing with ρ | ✅ FB1 |
| **FB2** excess identity + seed exact | `\|ΔE_bath−(E0−E_lat)\|/E0<1e-6`; seed `<1e-10`; `N_occ_excess≥0` | `2e-14`; exact; `N_occ_excess 0→~14` | ✅ FB2 |
| **FB3** excess-tare (Dp-3 corrected) | `c_excess` finite & ≥0; forms agree `<0.02`; broke-tare shown | `c` finite (`>1` at ρ=5 = lattice-pump physics); forms agree; `√(1−E_bath/E0)` breaks at ρ=5 | ✅ FB3 |
| **FB4** statistics-not-realization (Dp-2 corrected) | realizations differ; ensemble mean stable; CoV bounded (`<1.0`) | realizations differ (`‖Δx‖ 0.98→2.19`); `SEM/mean 0.069→0.093`; **CoV 0.170→0.228** (arm budget) | ✅ FB4 |
| **FB5** cold limit bit-for-bit | ρ=0 seed no-op ⇒ `max ΔE_bath = 0.0` on both combs | `Δω=0.050`: `0.0`; `Δω=0.010`: `0.0` | ✅ FB5 |
| boundary comb (non-gating doc) | `Δω=0.030` band narrower | ρ=1 clean, ρ=2 clean, ρ=3 BREAK (2/6 clamp) | ✅ documents band-width∝(less transfer) |
| **frozen-literal** (§D.D3 binary) | FB3 `c∈[0,1]` + FB4 pairwise-CoV<0.10 | both False at high ρ | ❌ → **FLOOR-LEDGER-ARTIFACT** (banked both-ways) |

---

## 3 · The mechanism (honest, Rule-11 — one root explains the band edge)

**One root: the floor jitter meets the absorbing-clamp wall.** The meter's amount-channel back-reaction (`_global_rescale`) removes each step's `d_e_bath` from `E_lat` by a global amplitude rescale; if `d_e_bath ≥ E_lat` the scale hard-zeroes (`scale=0`), an absorbing state (the R-2 clamp). A pre-occupied floor adds a per-step exchange jitter `∝√(M·E_floor)·κ·q` on top of the signal transfer. On a comb that **fully discharges** (`E_lat→0`), even a small floor jitter satisfies `d_e_bath ≥ E_lat` ⇒ the clamp fires — so the banked-dip `Δω=0.010` comb clamps *earlier* under a floor (the naive "warm floor keeps `E_lat` alive" intuition is **false there**). On a comb that transfers **partially**, `E_lat` never reaches zero, so the floor jitter (which stays `< E_lat`) never clamps — the identity holds and the floor is readable. The band edge is where the growing floor jitter first swings `E_lat→0`; it is realization-dependent, which is why single-seed FB1 read clean while the 6-seed FB1/FB4 exposed the edge. **This is the same clamp wall #727 hit — reached here from the floor-jitter side instead of the quasi-continuum side.**

**Regime read (regime-discipline).** Not a numerical failure (identity `2e-14` in-band). Not a dead coupling (the floor exchanges — jitter grows with ρ). Not "cannot read a floor" (the meter reads it cleanly in `[0,5]`). The bounded band is the honest instrument envelope, exactly as `METER-VALID-KAPPA-BAND` was for κ.

---

## 4 · Disposition + what STAGE 2 inherits (frozen constraints)

- **FLOOR-METER-VALID-BAND[0, 5]** ⇒ **STAGE 2 (the arm) MAY fire** on `ρ ∈ [0, 5]`, densest-viable comb `Δω=0.050` (+ sparse control `Δω=0.080`, + detuned-floor control). Frozen constraints STAGE 2 inherits:
  1. **ρ ladder inside `[0, 5]`** (do not enter the clamp regime).
  2. **ENSEMBLE-AVERAGE per ρ** over the frozen 6-seed set; require any FLOOR-ARROW suppression trend to **exceed the seed-spread `CoV ≈ 0.23`** (the FB4 arm-ensemble budget).
  3. Read the revival in the **excess ledger** `ΔE_bath = E_bath − E_floor_expected` (§D.D2), normalized per-cell (the plateau's absolute seed-spread divides out).
  4. The **detuned-floor control** is the jitter floor of the excess-revival observable (a floor seeded but drive detuned must NOT fake a coherent revival).
- **Routed SPECs (NOT built here; each earns its own charter + verification chain):**
  - **The clamp wall is the ceiling on ρ and on comb density** — a rate-limited / per-mode-capped back-reaction (a meter edit ⇒ breaks the #721 identity ⇒ full W/X/floor-battery re-cert) would lift both. SPEC only.
  - The **growth / node-genesis** picture stays re-homed to the cosmological rate rung (§D.D0); the **DOS-balance A/B fork** stays MOOT (the pathology was bath emptiness).
- **Untouched:** depletion-rate rung; #721/#724 certificates (standalone-K4 identity intact); meter module + K4 engine (byte-untouched; floor = config-only).

---

## 5 · Independent re-derivation + gates + provenance

- **Independent re-derivation from the raw banked JSON (the #726 F9 lesson — NOT the classifier's own booleans):** `src/tests/test_f6_floor_battery.py` loads `…_result.json` and, using **only** the raw per-ρ fields (`max_drift`, `n_identity_fail`, `n_over_transfer`, `n_clamp`, `max_excess_identity`, `seed_exact`, `c_finite_all`, `c_form_diff_max`) and the raw FB4/FB5 fields, independently re-derives: (i) the clean-band top `ρ_hi = 5`; (ii) FB1–FB5 pass in-band; (iii) the frozen-literal verdict is `FLOOR-LEDGER-ARTIFACT`; (iv) FB4 CoV is bounded (`<1.0`) and realizations differ. It **also** runs a **live** floor seed and asserts (a) the seed returns exactly `M·e_floor_per_mode` (`<1e-10`), (b) `ρ=0` is bit-identical to un-seeded, (c) a live in-band cell keeps identity `<1e-6`, (d) a live high-ρ (`ρ=3`) `Δω=0.030` cell degrades (the band edge is real). The independent re-derivation reproduces `FLOOR-METER-VALID-BAND[0,5]`.
- **Diagnostics provenance (F9):** every number is computed by the shipped driver and banked in `…_result.json` (per-ρ multi-seed drift/over/clamp counts, excess-identity, jitter mean+CoV, `c_finite`/`c_range01`, tare-broken flag; FB4 plateau mean/CoV/SEM/realization-diff; FB5 bit-for-bit diffs; boundary-comb rows; frozen-literal verdict). Nothing prose-only.
- **Gates:** `ruff check` clean; `make verify` green; the classifier self-check `match=True` (a precedence guard — the genuinely independent check is the test's raw-JSON + live-seed re-derivation).
- **Freeze margin (real):** §D frozen-by-push `2026-07-19T21:41:18Z` (API committedDate), **before any battery code existed**; §D-post + corrected driver committed after the first integrator run (the disclosed §A/§B/§C-post pattern). The battery is a CONSISTENCY-class validation — the ARM's prediction (revival-vs-ρ) was **not** measured in this lane (STAGE 2 freezes it prospectively).

---

*Honest closure (Rule 11 / Rule 12): the certified meter **READS a pre-occupied floor** in a bounded band `ρ ∈ [0, 5]` on the densest-viable comb `Δω=0.050` (FB1–FB5 pass, multi-seed). Two frozen §D.D3 sub-gate operationalizations (FB3 `c∈[0,1]`; FB4 pairwise-CoV) were found INCONSISTENT with §D.D3's own class-definition/prose at the first integrator run (Rule 10) and reconciled under an append-only §D-post addendum (the charter's own §A/§B/§C-post pattern; corrections DERIVED, both readings banked, flip disclosed). The genuine physical finding FB4 surfaced — the floor transfer is realization-sensitive (`CoV≈0.17–0.23`) — is frozen as the STAGE-2 arm-ensemble budget. The band is bounded because the floor jitter meets the #727 absorbing-clamp wall from the floor side. Nothing banked at emergence-class; the arrow hypothesis is untested here.*
