# F6 thermal-floor arm — revival-vs-floor — PREREG (FROZEN)

**Date:** 2026-07-19 · **Class:** prereg (frozen-by-push BEFORE any arm driver code; the revival-vs-ρ PREDICTION is UNMEASURED at freeze). · **Lane:** F6 thermal-floor arm (revival-vs-floor). · **Status:** §0–§7 frozen by the push of this file.
**Charter (FROZEN):** [`2026-07-16_f6-bath-meter_CHARTER.md`](2026-07-16_f6-bath-meter_CHARTER.md) §D + §D-post.
**Certificate consumed:** STAGE-1 floor-battery [`2026-07-19_f6-floor-battery_result.md`](2026-07-19_f6-floor-battery_result.md) → **FLOOR-METER-VALID-BAND[0, 5]** on the densest-viable comb `Δω=0.050` (κ=0.030 MILD, standalone-K4), extending `METER-VALID-KAPPA-BAND[0.030,0.030]` (§C-post).
**Instrument:** `src/ave/thermal/f6_bath_meter.py` (**BYTE-UNTOUCHED**; the floor is the CONFIG-ONLY `bath.x`/`bath.p` seed, §D.D1). **Reused BYTE-UNTOUCHED:** `f6_counting_arrow_arm.py` (#722 `_build`/`_m_for`), `f6_floor_battery.py` (STAGE-1 `seed_floor`/`_signal_per_mode`), `f6_bath_meter_validate.py` (#724 FROZEN `_place_detuned_band`).

---

## 0 · Sector header + certificate scope + the ruling/hypothesis record

- **Sector:** R7 thermal / entropy-sink (T2 latent-heat channel; F6 ε→T2 candidate). **NOT** A1 dilatation-mass, **NOT** Cosserat (2,3) winding/charge. The floor is a T2 sink DOF (no winding/mass; sector-ownership respected).
- **Mode:** reactive K4 TLM lattice (z=3 srs, 4 ports) + modal oscillator bath **PRE-OCCUPIED** at a target energy-per-mode with FROZEN random phases; symmetric-leapfrog coupling (`LatticeBathCoupler.step`).
- **Regime:** Regime I sub-yield, `A_max≈0.10` MILD, at the certified `κ=0.030`. Driven-then-source-off, closed cavity (pml=0, energy-conserving).
- **Phase-state:** the floor is **static** (pre-seeded, "effectively constant"); the small driven signal perturbs it only slightly.
- **Coordinate discipline (A46):** the revival is read in the **excess energy ledger** `ΔE_bath = E_bath − E_floor_expected` (§D.D2) — the bath's own scalar-energy coordinate, matching the recurrence-return claim's coordinate. NOT a raw `N_occ` (every mode saturates on a floor) and NOT a real-space φ² surrogate.
- **Certificate scope:** the arm runs ONLY inside `FLOOR-METER-VALID-BAND[0,5]` (ρ ladder ⊆ [0,5]); the densest-viable comb `Δω=0.050`; the 6-seed frozen ensemble; the arm-ensemble budget `CoV≈0.23` (STAGE-1 FB4) is a frozen gate ingredient (§4).

**★THE RULING (Grant verbatim, in-chat 2026-07-19; `[sic]` preserved — the standing attribution lesson):**

> "my gut says its couples through a static noise floor" / "so wffectively constant" / "word, that picture makes perfect sense to me, and the noise floor woild set the arrow of time right?"

- **Ruling (execution wording — tagged; NOT Grant's words):** the T2 sink couples locally as a STATIC pre-occupied NOISE FLOOR.
- **Hypothesis under test (hypothesis wording — tagged):** the floor's phase-randomness **sets the LOCAL arrow** — coherent returns (Poincaré revivals) **dephase into the occupied random background**, so **revivals die as the floor rises past the signal**.
- **Scope fences (execution):** the growth / node-genesis picture is **re-homed to the cosmological rate rung** (`Γ=3Hρ_latent`), NOT tested here; the DOS-balance A/B fork is **MOOT** (the pathology was bath EMPTINESS, not head-count); **floor provenance** and the **cosmological rate** are EXPLICITLY out of scope — this arm tests only the **local arrow** at the certified cell.

---

## 1 · FORM/VALUE + Poincaré honesty + mechanism-rung scope

- **FORM vs VALUE.** The floor **LEVEL** (the ρ ladder) is **instrument-calibrated** (an ENGINEERING CHOICE, tagged; ρ = E_floor_per_mode/E_signal_per_mode, referenced to the cold first-plateau). The **CLAIM** under test is the **FORM**: does the revival amplitude **suppress as a function of ρ** (the floor rising past the signal)? The magnitude of any suppression is a consistency-class read, not an emergence claim.
- **Poincaré honesty.** A finite seeded comb (M modes, spacing Δω) **still recurs in principle** at vastly longer times (`T_rec = 2π/Δω`, and full multi-mode re-coherence at the least-common-multiple horizon). This arm measures **revival SUPPRESSION window-relative** (`T_window = 11·T_rec`): whether, *within the observation window*, the coherent return that is present at ρ=0 is suppressed as ρ rises. It is a horizon-relative arrow (the same epistemic status as radiation resistance / the #722 counting arrow), NOT a claim that recurrence is destroyed for all time.
- **Mechanism-rung scope.** The claim is a **LOCAL arrow** (does the local floor dephase the local revival?). Floor **provenance** (where the pre-occupation comes from) and the **cosmological depletion rate** are OUT of scope (re-homed, §0). No emergence-class VALUE is headlined.

---

## 2 · Premises from banked data (the cold-cell expectation, cited)

- **The revival exists to be suppressed (cold, ρ=0).** #726 (`2026-07-18_f6-certified-kappa-sweep_result.md`, corrected first-plateau observable) banks, at κ=0.030 MILD: the **densest** comb `Δω=0.010` dips **14.9% @ x≈1.3 → 35.5% @ x≈2.46** (recurrence-timed, growing) — the general revival premise; and the **primary plant** `Δω=0.050` returns **`R_cum[10]=0.932 @ x≈2`** (`dipRmax=0.932 @ x=2.00`) — the ρ=0 revival the arm's positive control must reproduce.
- **The floor is readable here (STAGE 1).** FLOOR-METER-VALID-BAND[0,5] on `Δω=0.050`: identity `2e-14`, excess-ledger + tare well-defined, cold-limit bit-for-bit, floor-transfer seed-spread `CoV≈0.23` (the ensemble budget). The banked-dip `Δω=0.010` comb is NOT floor-viable (clamps under a floor), so the primary plant is the densest-**viable** comb `Δω=0.050` (§D-post Dp-4).

---

## 3 · THE GRID (every value enumerated; frozen)

**Common:** κ=0.030, MILD (`scale=0.6`), `nonlinear=True`, `op3_bond_reflection=True`, `V_SNAP=1.0`, `dt=1.0`, `pml=0`, driven-then-source-off, E0 on-shell (post-first-step). Floor = config-only `seed_floor` (§D.D1). Window `T_window = 11·T_rec` per comb (`≥ 2.5·T_rec`). **Ensemble:** the FROZEN 6-seed set `SEEDS = {20260719, 20260720, 20260721, 20260722, 20260723, 20260724}` at EVERY cell; reads are the ensemble MEAN ± SEM (the §D-post FB4 arm-ensemble requirement).

- **Floor ladder (ρ):** `{0, 0.3, 1.0, 2.0, 3.0, 5.0}` — **6 levels**, ρ=0 the POSITIVE CONTROL (must reproduce the primary comb's banked cold revival bit-for-bit), 0.3 clearly **below-signal**, 1.0 **at-signal**, 2.0/3.0/5.0 clearly **above-signal**; all ⊆ FLOOR-METER-VALID-BAND[0,5]. `ρ = e_floor_per_mode / E_signal_per_mode`, `E_signal_per_mode` = cold first-plateau excess / M (FROZEN config reference, computed once per comb).
- **Combs:**
  - **Primary (densest-viable):** `Δω=0.050, ω_min=0.30, M=15` (T_rec=126; horizon 1382).
  - **Sparse control:** `Δω=0.080, ω_min=0.30, M=10` (T_rec=79; horizon 869) — fewer floor modes; tests comb-density dependence (the SUPPRESSION-NOT-TRACKING discriminator).
  - **Detuned-floor control:** the **primary comb seeded with the floor at each ρ**, but the **drive detuned** via the FROZEN `_place_detuned_band` (q-power-budget placement, #724) — i.e. the floor is present but the collar drive is off-resonance. The floor ALONE must not fake a coherent revival (it is the jitter floor of the excess-return observable). Run over the same ρ ladder + seeds.
- **Full grid:** `{primary, sparse} × {6 ρ} × {6 seeds}` + `{detuned-floor} × {6 ρ} × {6 seeds}` = 216 cells.

---

## 4 · THE FROZEN TREE + precedence (validity gates FIRST; Rule 11 — no retune)

**The observable (frozen).** Per cell: `ΔE_bath(t) = E_bath(t) − E_floor_expected` (excess ledger, §D.D2). `t_fp` = first-plateau step (ΔE_bath first reaches `(1−1/e)·max`). `R_return(t) = clip(1 − ΔE_bath(t)/ΔE_bath(t_fp), 0, None)` for `t≥t_fp`, else 0. `R_cum` = running max. **Cell revival** `R_rev = R_cum` at window end (deepest fractional excess-return over the window). **Ensemble read** `R̄_rev(ρ, comb) = mean_seed(R_rev)`, `SEM(ρ,comb) = std_seed(R_rev)/√6`. **Jitter-subtracted coherent revival** `S(ρ) = max( R̄_rev(ρ, primary) − R̄_rev(ρ, detuned-floor), 0 )` — the resonant excess-return ABOVE the floor-jitter floor at the same ρ. `S(ρ)` is the FLOOR-ARROW observable.

**Frozen thresholds (DERIVED — anchored to the banked cold revival + the FB4 seed budget; NOT tuned to a measured S(ρ>0), which is unmeasured):**
- `RIDE_ON_TOP = 0.80` — `S(5)/S(0) ≥ 0.80` ⇒ the revival rides on top essentially unchanged.
- `SIG_DROP = max(2·SEM_pooled, 0.15)` — a decay counts as real only if `S(0) − S(5)` exceeds twice the pooled ensemble SEM AND an absolute floor `0.15` (above the `~0.09` per-cell SEM implied by the `CoV≈0.23` budget / √6) — the FB4 arm-ensemble budget made a gate.
- `MONO_TOL = SEM(ρ)` — `S(ρ)` is "monotone non-increasing tracking ρ" iff each step satisfies `S(ρ_{i+1}) ≤ S(ρ_i) + SEM(ρ_i)` (non-increasing within seed noise).
- `HALVED = 0.50` — strong-form marker (`S(5) ≤ 0.50·S(0)`): "the revival at least halves when the floor is 5× the signal per mode." Reported; the FLOOR-ARROW gate is `S(5) < RIDE_ON_TOP·S(0)` (real suppression) + monotone-tracking + significant, with `HALVED` as the strong/weak descriptor.
- `STAYS_TOL = 0.20` — at ρ=5 the excess **relaxes to the equilibrium share and STAYS**: the late-window excess-return does not re-grow, `R_cum(end) − R_cum(0.8·window) ≤ STAYS_TOL·R_rev` (no late re-revival).

**Validity gates (checked FIRST; frozen):**
1. **CONSERVATION** — every cell identity `max|E_lat+E_bath−etot0|/E0 < 1e-6` (LEDGER_ID_TOL). Fail (any cell) ⇒ **NUMERICAL**.
2. **CLAMP-NEVER** — no cell fires the `scale=0` absorbing clamp (the floor should prevent it inside [0,5]; gate it anyway). A clamped cell is **NO-INFORMATION**; any clamped in-grid cell ⇒ **NUMERICAL** (the grid left the certified band).
3. **SEED-FROZEN** — the 6 frozen seeds are used verbatim; realizations differ (`‖x_A−x_B‖>0`); the ensemble is the read.
4. **COLD-CONTROL-REPRODUCES** — ρ=0 on the primary comb reproduces the banked #726 `Δω=0.050` `R_cum` **bit-for-bit** (`max diff = 0.0`; the floor seed is a no-op at ρ=0).
5. **DETUNED-VALID** — the detuned-floor control at ρ=0 shows **no coherent revival** (`R̄_rev(0, detuned) < 0.5·R̄_rev(0, primary)`), i.e. the ρ=0 resonant revival is a genuine coherent return, not a floor-jitter artifact. Fail ⇒ the observable cannot separate revival from jitter ⇒ **SUPPRESSION-NOT-TRACKING-ρ** (the "suppression" would be jitter-masking).

**Verdict tree (precedence 1→4, after the validity gates):**
1. If any validity gate 1–2 fails ⇒ **NUMERICAL**.
2. **NO-SUPPRESSION** iff `S(5)/S(0) ≥ RIDE_ON_TOP` (`≥0.80`) — the coherent revival rides on top essentially unchanged (Grant's ride-on-top alternative; **fail closed honestly** — the floor does NOT set the local arrow by dephasing).
3. **FLOOR-ARROW** iff **all**: `S(ρ)` monotone-tracking-ρ (each step within `MONO_TOL`) **AND** `S(0) − S(5) > SIG_DROP` (significant real decay) **AND** `S(5) < RIDE_ON_TOP·S(0)` **AND** the excess at ρ=5 relaxes-and-STAYS (`STAYS_TOL`) **AND** validity gate 5 (DETUNED-VALID) passes **AND** the sparse control's `S(ρ)` also decays with ρ (whole-grid coherence — the suppression is a floor property, not a single-comb accident). Strong-form if `S(5) ≤ HALVED·S(0)`.
4. **SUPPRESSION-NOT-TRACKING-ρ** (the faithful whole-grid foreign-eater analog) — otherwise: a significant suppression is present (`S(5) < RIDE_ON_TOP·S(0)`) BUT it does **not** cleanly track ρ (non-monotone, OR sparse-control disagrees, OR gate-5 fails so it is jitter-masking, OR monotone-but-sub-`SIG_DROP`).

**Rule 11.** No threshold is retuned after the fire. A single mechanism that explains all cells is the discipline at full strength. Deviations from this frozen §4 are disclosed as findings (both readings), never a silent relabel.

---

## 5 · §5b circuit-map fill (port / regime / Γ; the no-valve rail)

- **Port:** the collar shell (`r∈[2,4]`) — the dilatation-port projection `q = Σ_collar mean_p(V_inc+V_ref)`. **Regime:** driven-then-source-off, closed cavity (Γ=−1 hard walls at pml=0; energy-conserving). **Bath port:** the modal comb, PRE-OCCUPIED (the floor) — a set of lossless reactive oscillators.
- **The no-valve rail (load-bearing).** NO `Re(Z)` element exists anywhere: the comb is lossless (`friction=False`, `bath.damp` OFF), the coupling is a symplectic CL kick + exact free rotation, the back-reaction is a phase-preserving energy-matched rescale. **The floor is lossless pre-occupied REACTANCE.** Any local arrow is therefore **EMERGENT from phase-statistics** (the random floor phases dephasing the coherent return), NOT a smuggled resistor. This is the honest F6 ε→T2 candidate: irreversibility-by-phase-randomization, conservative bookkeeping.

---

## 6 · Diagnostics (all driver-computed; nothing prose-only)

Per cell / per ρ, the shipped driver banks: `E_signal_per_mode`; `E_floor_expected` (+ seed-exactness); the excess ledger `ΔE_bath(t)` first-plateau + `R_return`/`R_cum` tables (X-grid); `R_rev` per seed + ensemble mean/SEM; the jitter-subtracted `S(ρ)`; the conservation drift + clamp flags (validity gates); the excess-relaxation "stays" check; the **Rule-10 reactance pair** (bath C-state `Σ½ω²x²` AND L-state `Σ½p²`) across the window on the primary comb at ρ∈{0,1,5}; the detuned-floor control reads; the sparse-control `S(ρ)`; the cold-control bit-for-bit diff.

---

## 7 · The FD leg (SECONDARY — non-gating; clearly fenced)

**Fenced: this leg is SECONDARY, cannot affect the arm verdict, and mints NO claim.** Bank the **floor-injected fluctuation spectrum** (the lattice jitter `σ(E_lat)` and its power spectrum over the alive window) vs the **measured relaxation rate** (the 1/e time of the excess-return decay / the excess reaching its plateau). Report the **FD ratio** `fluctuation / relaxation` per ρ as **exploratory data routed to the ℏ-as-FD open** (`manuscript/ave-kb/…` fluctuation-dissipation thread). NO fluctuation-dissipation theorem is asserted; the numbers are banked for the routed open question only and are **explicitly excluded** from the §4 verdict tree.

---

*Freeze discipline: §0–§7 frozen by the push of this file BEFORE any `f6_thermal_floor_arm.py` code exists. The revival-vs-ρ prediction `S(ρ)` is UNMEASURED at freeze (only the banked cold `R_cum(0)≈0.93` premise and the STAGE-1 viability/seed-budget were measured — neither is the prediction). The freeze margin is the push→first-arm-code interval, reported in the RESULT + PR. Rule 11: no threshold retune post-fire; honest closure whichever branch fires.*
