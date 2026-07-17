# F6 bath meter — rebuilt mode-count detector — CHARTER

**Date:** 2026-07-16 · **Class:** charter (design + validation battery frozen BEFORE any code) · **Lane:** METER (instrumentation, NOT a gate-run). · **Status:** design frozen; instrument to be validated on synthetic plants only. · **Priority:** hardware-ratings-map R7 / §7 JOINT detector-rebuild GATE (post-#711/#714).

**What this is.** The instrument mandated by the JOINT detector-rebuild GATE. It is the meter behind that gate; this lane BUILDS and VALIDATES the meter. **NO F6 arm fires with it here** — validation is on hand-built plants only.

**What this is NOT.** Not an F6/R7 arm. Not a CHANNEL-BOUNDED attempt. Not a thermometer ungate. Not a soliton-genesis door. Not a retune of the banked Arm A/B BIAS-MOVED verdicts (those survive independently on the protected-core `S_core` knife and are untouched here). Not an edit of `k4_cosserat_coupling.py` / `k4_tlm.py` (a sibling lane owns the F1 ordering fix there — see §9 rebase dependency). Any temptation to "just try the door" once the meter is green is **explicitly out of scope**: the meter's green light is an instrument certificate, not a licence to fire an arm.

---

## 0 · Sector header + regime declaration (mandatory before any substrate claim)

- **Sector:** R7 — thermal / entropy-sink (T2 latent-heat channel; the F6 ε→T2 candidate). NOT A1 mass, NOT Cosserat (2,3) charge/spin. The bath is a T2 dissipation-sink DOF; it does not carry winding or dilatation mass.
- **Mode:** classical reactive TLM lattice (K4, z=3 srs, 4 ports) coupled to a Caldeira–Leggett independent-oscillator bath.
- **Regime:** linear-response / driven; small-amplitude collar tap. No Op14 saturation active (cold plant). No node creation (no frontier mint).
- **Phase-state:** cold plant — a seeded low-amplitude lattice, NOT a saturated soliton core. There is no |Γ|→1 yield wall in the meter's plants; the meter is characterised where the physics it will later measure is *absent-or-known*, which is the correct place to calibrate an instrument.
- **Coordinate discipline (A46):** the mode-count claim lives in the bath's **modal / spectral** phase-space (per-oscillator energy `E_m = ½p_m² + ½ω_m² x_m²` over the frequency comb `{ω_m}`). `N_occ` is read in that matching coordinate — a spectral read, not a real-space lattice-Cartesian read. Real-space quantities (collar `q`, lattice energy) enter only as the coupling and the energy ledger.
- **Consistency-vs-emergence tag:** every verdict here is **CONSISTENCY-class** (does the meter read what a known plant puts in?). No emergence claim. Instrument numbers (`M`, `Δω`, `ω_min`, `FLOOR`, `κ`, collar radii) are **engineering choices tagged as such** — they are not CODATA-derived and carry no physics claim. Canonical constants (`Z_0`, `V_SNAP`, numerical epsilons) are imported from `ave.core.constants`; the bath frequencies are in lattice-step units (dimensionless), an instrument choice.

---

## 1 · Why the old detector was void (the autopsies this charter answers)

The meter exists because the previous mode-count infrastructure was voided by the JOINT #711/#714 adversarial review. The two failure mechanisms, verbatim-sourced:

- **F-1 — the "bath" was a write-only side-array with zero back-reaction.** `bath_modes = np.zeros(M_MODES)` written only by `_credit_modes`, read only by `_n_occ`; never coupled back to the lattice (`src/scripts/vol_1_foundations/f6_mode_count_event_gated.py`). Arm B twin: `b[m]` "write-only (zero back-reaction)" (`research/2026-07-16_f6-arm-b-exterior-leave_prereg_FROZEN.md:139`, Amendment A1). Consequence: `ΔN_occ ≡ M_MODES` by construction — live-fire `M_MODES∈{16,48,64,128,256} → ΔN_occ={16,48,64,128,256}`, `E_bath` invariant. It read the accumulator dimension, not physics.
- **F-2 — the FRICTION-RENAMED control was a flag readback.** Production and `--sabotage-friction` were bit-identical except the `credit_modes` side-array increment (`research/2026-07-16_f6-mode-count-event-gated_prereg_FROZEN.md:137`, Amendment A2). The energy-removing op ran in both paths; the control "cannot fail on any energetic run" — vacuous as a physical discriminator.
- **F-3 — the twin-64 was one constant printed twice.** Arm-A-interior-64 = Arm-B-exterior-64 = the same `M_MODES=64` constant, "not two geometries converging on a measurement" (docket `_orchestration/2026-07-10_rulings-docket.md`, "Continuation — 2026-07-16: F6 Arm A/B adversarial-review repair (mode-count DEMOTED; twin-64)").
- **F-4 — the baseline was captured off-shell.** `E0 = lat.total_energy()` on a `V_ref=0` seed doubles exactly `2.000000×` at the first TLM connect (`get_energy_density = Σ_p V_inc² + V_ref²`), so the soft-ledger `CHANNEL-BOUNDED` pass-bin was structurally unreachable (Arm A `..._prereg_FROZEN.md:161` A3; Arm B `...arm-b..._prereg_FROZEN.md:145` A2). Repair: capture E0 **post-first-step** (on-shell). Both arm repairs cite the same E0-convention bug class.

The GATE (ratings-map §7, verbatim): the detector MUST be rebuilt to satisfy **both** (1) a **real bath DOF** — actual dynamics/frequencies with **back-reaction** onto the lattice (not a `np.zeros(M_MODES)` side-array with zero dynamical consequence); and (2) a **FRICTION-RENAMED control that varies a physical quantity**, not the `credit_modes` bookkeeping flag.

---

## 2 · Design — the real bath DOF (production coupling; lossless-reactive)

**The bath.** `M` independent harmonic oscillators, index `m = 0…M−1`, each with its own frequency `ω_m = ω_min + m·Δω`, its own state `(x_m, p_m)`, evolved **every step**. `Δω` and `ω_min` are **fixed physical properties** of the bath's dispersion comb; `M` is a **truncation count**, not a physics knob. Larger `M` extends the comb to higher `ω` — it does not densify the driven band. This is the design pin that kills the twin-64: adding oscillators adds *undriven* high-`ω` modes, so a correct occupancy read does not track `M`.

**The coupling (Caldeira–Leggett bilinear; back-reaction is the coupled equations, not a ledger).** A fixed shell of active lattice sites (`collar`, radii `[r_in, r_out]` about centre) is the coupling port. Each step reads a scalar collective coordinate `q = Σ_{s∈collar} mean_p V_inc[s,p]` (the dilatation-port projection — a read of the collar field). Bath equations of motion:

```
ẋ_m = p_m
ṗ_m = −ω_m² x_m + κ g_m q          # the lattice drives the bath
```

**Back-reaction (the load-bearing requirement).** The bath's stored field exerts a reaction force on the collar, applied as an increment to the lattice `V_inc`:

```
F_q = κ Σ_m g_m x_m − κ² q Σ_m g_m²/ω_m²   # reaction + Caldeira–Leggett counter-term
V_inc[s∈collar, p] += (dt · F_q) / (n_collar · n_port)
```

Because `F_q` writes `V_inc`, energy deposited in the bath **changes subsequent lattice dynamics** — this is genuine back-reaction, not a side-array. V5 measures it directly (coupling ON vs OFF trajectory divergence). `g_m = g0` is a fixed spectral coupling density (function of `ω_m` only, independent of `M`), so the driven set is `M`-invariant.

**Integrator (symmetric leapfrog, per step):** (1) `lat.step()` — lattice advances losslessly; (2) read `q`; (3) half coupling-kick to bath `p_m`; (4) exact free rotation `(x_m,p_m) ← R(ω_m·dt)` — energy-exact for the free part; (5) half coupling-kick; (6) back-react `F_q` onto collar `V_inc`.

**Ax3 discipline (lossless-reactive).** The production coupling contains **no** dissipative (`Re(Z)`) term — energy moves reactively between lattice and bath; total `E_lat + E_bath + E_int` is conserved (measured by V6; non-secular integrator drift only, no secular loss). The irreversibility this instrument will later measure is **by mode-spreading** — energy dispersed across many incommensurate `ω_m` with no return path on relevant timescales — the honest F6 ε→T2 candidate, NOT a smuggled friction. The no-smuggle rail (conservative bookkeeping; no `Re(Z)`; no ℏ-FD) is preserved from the Arm-A repair.

---

## 3 · Design — the occupancy read (`N_occ`) that can genuinely fail

`N_occ = #{ m : Ē_m > FLOOR }`, where `Ē_m` is the cycle-averaged per-mode energy and `FLOOR` is an **absolute** physical threshold (an engineering choice, tagged; a fixed fraction of the drive scale). Secondary reads reported alongside: occupied bandwidth `Δω_occ = N_occ·Δω` (intensive), and participation number `N_eff = (Σ Ē_m)² / (Σ Ē_m²)`.

**Failure modes the read must exhibit (design intent):**
- a leave that **never populates modes** reads `N_occ = 0` (V1 lossless control);
- a **narrowband** leave populates **few** modes, the count tracking the drive's bandwidth (V3);
- varying `M` with fixed physics leaves `N_occ` **invariant** (V2) — the physics that guarantees this: with fixed `Δω`, only modes whose `ω_m` falls in the driven band (a fixed spectral window set by the collar drive, resonance-selected) rise above `FLOOR`; the extra modes at larger `M` are off-resonance and stay below `FLOOR`.

---

## 4 · Design — the FRICTION control that varies a physical quantity

The friction plant **replaces the reactive bath coupling with a real dissipative `Re(Z)` term of matched magnitude** — a lossy multiplicative termination at the collar, `V_inc[collar] ← (1−γ)·V_inc[collar]`, with `γ` **calibrated** so the total energy removed over the run matches the reactive bath's absorbed `E_bath` (target: within 20%). This is a genuine resistor (`Re(Z) > 0`), not a `credit_modes` flag: it perturbs the energetic/dynamical state and can fail.

**The physical discriminator (declared BEFORE running — required for V4).** The meter separates reactive bath-transfer from dissipation by a **physical signature**, not by which code path ran:
- **Closed-ledger fraction** `R = |ΔE_lat + ΔE_bath| / |ΔE_lat|` — is the lattice's lost energy *found in a DOF*? Reactive bath: `R < 0.2` (energy present in `E_bath`, recoverable/accounted, total conserved). Friction: `R > 0.8` (energy gone, no bath, total ledger broken).
- **Occupancy** `N_occ`: reactive bath `> 0`; friction `= 0` (no populated modes exist).

Both signatures are computed identically for both plants; the plants land in different bins **because of the physics** (energy in a DOF vs gone), not because a flag was read. Matched magnitude is the point: identical energy removed, opposite discriminator bin.

---

## 5 · Baseline convention (on-shell E0)

Per both arm repairs: capture `E0` **after the first `lat.step()`** (on-shell), because the `V_ref=0` seed doubles exactly `2.000000×` at the first TLM connect (`...event-gated_prereg_FROZEN.md:161` A3; `...arm-b..._prereg_FROZEN.md:145` A2). The energy ledger is booked against this equilibrated baseline. V6 requires the ledger to close on the lossless control to machine precision.

---

## 6 · VALIDATION BATTERY (the meter's own gates — frozen)

| ID | Plant | PASS criterion (declared before running) |
|----|-------|------------------------------------------|
| **V1** | Lossless control (`κ=0`, bath free & undriven) | `\|ΔE_lat\|/E0 < 1e-10` (machine-clean) **AND** `N_occ = 0` |
| **V2** | M-variation, fixed physics, `M∈{32,64,128}` | `N_occ` invariant: `\|N_occ(M) − N_occ(64)\| ≤ 1` for all `M` (kills twin-64) |
| **V3** | Known-transfer plant: narrowband tone `q(t)=A·sin(ω_d t)` driven into bath | measured `N_occ` = predicted resonance-window count within `±1`, **and** invariant across `M` (count tracks drive bandwidth, not `M`) |
| **V4** | Friction plant: `Re(Z)` termination, `γ` matched to `E_bath` (≤20%) | reactive-bath and friction land in **different discriminator bins**: bath `R<0.2 & N_occ>0`; friction `R>0.8 & N_occ=0` |
| **V5** | Back-reaction liveness: coupling ON vs OFF, same seed | trajectory divergence `D_final = ‖V_inc^ON − V_inc^OFF‖₂ / ‖V_inc^OFF‖₂ > 1e-3` and growing (voided detector had `D≡0`) |
| **V6** | Baseline convention | on-shell `E0` used; lossless-control ledger closes `< 1e-10`; coupled-run total-energy drift **non-secular** and below the V4 friction bin |

**Frozen tolerances:** `MACHINE_TOL = 1e-10`; `N_OCC_M_TOL = 1`; `N_OCC_V3_TOL = 1`; `R_BATH_MAX = 0.2`; `R_FRICTION_MIN = 0.8`; `D_LIVE_MIN = 1e-3`; `FRICTION_MATCH_TOL = 0.20`. Do not retune to rescue a result (Rule 11); if a plant fails, record it and classify the meter accordingly.

---

## 7 · Verdict classes (for the VALIDATION only)

- **METER-VALID** — all of V1–V6 pass. The instrument satisfies both §7 gate conditions (real bath DOF + back-reaction; physical friction control) and is fit to be handed to a future F6/R7 arm (in a *different* lane).
- **METER-PARTIAL(list)** — some pass, some fail; the list names which. The meter is usable only for the passing aspects; a gate-run may not rely on any failed axis.
- **METER-INVALID** — any core requirement fails (real bath DOF, back-reaction liveness V5, M-invariance V2, or friction discrimination V4). The meter cannot be used for any F6 arm; the §7 gate remains unmet.

This lane returns a verdict on the **meter**, never on F6. A METER-VALID result does not bank CHANNEL-BOUNDED, does not ungate the thermometer, and does not fire an arm.

---

## 8 · Substrate-native walk (K4 / Cosserat / Op14 / phase-space)

- **K4:** the meter reads the lattice's own `V_inc`/`V_ref` port fields and `get_energy_density` (Σ_p over the 4 K4 ports); no Cartesian stencil is imposed. The collar is a set of native active sites.
- **Cosserat:** the bath is a T2 dissipation-sink DOF; it carries no (2,3) winding and no dilatation mass. Sector-ownership respected (§0). The bath does not confine or hold charge.
- **Op14:** no saturation kernel active — the plants are cold; local-clock modulation is out of scope for the meter (flagged, not invoked).
- **Phase-space (A46):** `N_occ` is read in the bath's modal/spectral coordinate, matching the mode-count claim's own coordinate. No real-space φ² surrogate.

The bath model is Caldeira–Leggett (independent-oscillator), the canonical *honest* model of irreversibility-by-mode-spreading — reactive (lossless) coupling, not gradient-descent, not an energy-basin relaxation, not a continuum-Helmholtz sink.

---

## 9 · Rebase dependency + rails

- **F1 ordering defect (sibling lane).** A sibling lane is fixing an ordering defect in `k4_cosserat_coupling.py` / `k4_tlm.py`. This meter is built as a **standalone module** coupled through a **minimal clean interface** (reads `V_inc`, `mask_active`, `get_energy_density`, `step`; writes `V_inc` at the collar). It does **not** edit those two files. **Rebase-before-integration:** before any future F6 arm integrates this meter, rebase onto the merged F1 fix and re-run V1–V6 (the back-reaction path writes `V_inc`, which the F1 ordering fix touches).
- **Rails:** charter pushed before code; canonical constants imported; sector headers + regime declarations present; NO F6 arm fired; flag-don't-fix anything else; per-cluster commits; `make verify` before each push. Verdict classes above are for the validation only.

---

## Amendment §A — post-#717-review repairs (2026-07-17, append-only; §0–§9 body preserved byte-for-byte)

> 🔴 **Rule-12 supersession (2026-07-17, post-review).** The PR #717 adversarial review (14 findings confirmed, 0 refuted; 1 CRITICAL/CONCLUSION-WRONG) established that the banked **METER-VALID** was WRONG: the production coupling had a **secular energy pump**, and several frozen declarations were deviated-from in code without an amendment. The meter's **core genuineness SURVIVED** (the mid-band detuning collapse proves the transfer is bath-EOM-gated — a real coupling, not an amount-matcher), but the certificate was void. This amendment records the deviations-and-corrections and re-adjudicates the §7 gate on the mechanism **as actually shipped**. The §0–§9 body above is the frozen pre-reg and is preserved; the code now implements the corrected design recorded here. New/changed thresholds are registered below (Rule 11: derived, not tuned-to-pass).

### A1 — Back-reaction mechanism: §2 bilinear force law → GLOBAL energy-matched reactive load (the load-bearing swap, now recorded)

§2 froze the back-reaction as a **bilinear Caldeira–Leggett force law** `F_q = κ Σ g_m x_m − κ² q Σ g_m²/ω_m²` written additively into `V_inc`. That law was **never shipped** and does not conserve against the opaque TLM stepper (it pumps; the 1/ω² counter-term destabilises — drift 4–19%). A **local** collar amplitude rescale (the first shipped fix) drove the lattice **off-shell** every step and pumped **+4.1e-2 / 3000 steps** (the #717 CRITICAL; verified: the leak is entirely in `lat.step()`, not the rescale arithmetic).

**Correction (shipped):** the back-reaction is a **GLOBAL, phase-preserving, energy-matched reactive load** — the whole active-cell amplitude `(V_inc, V_ref)` is rescaled by the ΔE the bath's own coupled EOM absorbed. Because a scalar multiple of an on-shell TLM state stays on-shell, total `E_lat + E_bath` conserves to **~1e-15 over 3000 steps** (measured; V6 slope 1.1e-17/step, non-secular). The `max(…,0)` clamp is never triggered at the operating point (transfer < collar energy); it would truncate the ledger only in an over-extraction regime, which the conserving global scheme does not reach.

**§7 gate re-adjudication (SATISFIES-WITH-REWORDING).** The shipped back-reaction **returns AMOUNT, not PHASE**: it is bath-EOM-gated (off-resonance ⇒ ΔE≈0 ⇒ rescale≈1 ⇒ no back-reaction; detuning collapses the transfer ~3000×, proving a genuine resonant coupling and not an amount-matcher) and bidirectional in amount (ΔE<0 ⇒ cavity scales UP), but it is **spatially uniform and phase-blind** (no bath phase re-enters the lattice). Stated as a **known limitation.** Given the detuning evidence, this satisfies §7 condition (1) "a real bath DOF with back-reaction (coupled equations, not a ledger)": the transferred amount is set by the bath's own dynamics, and the lattice trajectory genuinely diverges (V5 D=0.15). It is NOT the frozen §2 bilinear law; §2 is superseded by this A1.

### A2 — Secular-pump kill + V6 rebuilt with a MEASURED, non-secular criterion and a DERIVED ceiling (Rule 11)

§6 froze the V6 criterion qualitatively ("non-secular and below the V4 friction bin"); the shipped V6 printed "non-secular" as an unearned string and gated a 300-step max against an **unfrozen** 0.02 ceiling (the #717 finding). **Correction:** V6 now runs **3000 steps**, computes the drift **slope** (secularity), and gates on a **DERIVED** ceiling — the drift as a fraction of the bath transfer must stay below `R_BATH_MAX` (the reactive-bin boundary; else the ledger would leave its own bin). Result: max/transfer = 1.3e-13, slope 1.1e-17/step → non-secular, PASS honestly (the pump is gone, not masked by a tuned window).

### A3 — N_occ floor: relative-to-peak → ABSOLUTE (restores the frozen §3 semantics) + minimum-E_bath gate

§3 froze an **absolute** floor ("a fixed fraction of the drive scale"); the shipped code used **relative-to-peak**, which counted the off-resonant sea (N_occ=8 on E_bath~1e-21; 33–42/64 on collapsed transfer) — the #717 MAJOR. **Correction:** `FLOOR_ABS = 1e-2` (absolute, one order above the production off-resonant sea) **plus** a minimum-total gate `E_BATH_MIN = 1e-2` (no occupancy read below it). Now eps-level and detuned spectra read **N_occ = 0** (verified), and production reads N_occ=6, M-invariant.

### A4 — Nyquist envelope enforced; "twin-64 killed" → "killed-within-envelope"

The coupling kicks sample the drive at dt=1.0, so modes at `ω_m ≡ ±ω_drive (mod 2π)` are re-driven by **aliasing**; the twin-64 resurrected at M≥~184 (N_occ 8,8,8,12,31 for M=32/64/128/200/256) — the #717 CRITICAL. **Correction:** `OscillatorBath.__post_init__` now **asserts `ω_max·dt < π`** (caps M ≤ 95 at the frozen comb). V2's M-sweep is held **within** the envelope (M∈{32,64,90}). The unconditional "twin-64 killed" is demoted to **killed-within-the-Nyquist-envelope**, and the verdict class is **METER-VALID-WITHIN-ENVELOPE**.

**V2 physics-tracking leg (replaces the confounded Δω-bandwidth check).** Varying Δω changes the drive-resonance overlap, so the transfer magnitude (E_bath) itself swings 50× — Δω-variation is NOT "fixed physics." The decisive controlled test is **detuning**: shifting the comb off the drive band (within Nyquist) collapses N_occ to **0** (the old ΔN_occ≡M detector would still read M). V2 now gates on M-invariance **and** detuning-collapse; the Δω-response (N_occ not pinned) is reported as a non-gating diagnostic.

### A5 — Friction plant rebuilt so the bin can FAIL (bath LIVE + Re(Z) damping)

The shipped friction plant early-returned before driving the bath, forcing `E_bath≡0 ⇒ R≡1, N_occ≡0` by code path — the same "cannot fail on any energetic run" class the F-2 autopsy voided (the #717 MAJOR). **Correction:** friction now keeps the bath **coupling LIVE** (same reactive drive) but adds a real **Re(Z) damping on the bath modes** (`β`), so the transferred energy is **dissipated (gone)** rather than stored. The discriminator is the closed-ledger fraction **R**, genuinely measured on **both** driven baths and able to fail: reactive R<0.2 (stored) vs friction R>0.8 (gone). Matched magnitude: friction **dissipates** ≈ what the reactive plant **stores** (Δ=11% ≤ 20%). This is the recoverable-vs-gone signature, by physics not code path.

### A6 — Cold-plant consistency + registered thresholds + Ax3 wording

- **Cold plant.** §0 declares "no Op14 saturation"; the code now uses a **LINEAR** lattice (`nonlinear=False`), consistent with that declaration (the pump is independent of nonlinearity — verified — but the linear lattice is the honest cold-plant choice).
- **Ax3 wording.** "conserved by construction" is demoted to **"conserved to integrator order (measured by V6); global on-shell rescale conserves to ~1e-15 over 3000 steps"** (module + §2 wording corrected).
- **Registered thresholds (were post-charter, now recorded here):** `V6` drift ceiling = `R_BATH_MAX` (DERIVED, not asserted); `V3` gates on a **COMPUTED** resonance-window prediction (modes within one comb spacing of the tone) tested within `±N_OCC_V3_TOL`; the V3 peak-location tolerance = `2·Δω`; friction `β = 0.01`; operating point `κ = 0.012`, `M_LIST = {32,64,90}`, detuned probe `(ω_min=1.5, M=32)`.

### A7 — Honest re-bank

Verdict (this validation only): **METER-VALID-WITHIN-ENVELOPE** — all V1–V6 pass with the corrected instruments, including the 3000-step non-secular drift curve, the absolute-floor occupancy read, the Nyquist-bounded M-invariance + detuning collapse, and the bath-live friction discriminator. The "within-envelope" qualifier is load-bearing: the M-invariance (twin-64 kill) holds only for combs satisfying `ω_max·dt < π` (M ≤ 95 at the frozen comb), now enforced. NO F6 arm is fired; the R7 §7 receipt stays with the auditor lane; rebase-before-integration onto the F1 fix still stands (§9).
