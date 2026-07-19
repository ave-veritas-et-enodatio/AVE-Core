# RESULT — Yield-fork discriminators: thixotropy-τ (Leg A) + memristor loop-area (Leg B)

> **SECTOR HEADER (read first).**
> - **MODE:** driven, time-domain LC-relaxation of the longitudinal-A1 bulk saturation state `S(t)`. NOT a minimization, NOT continuum-Helmholtz.
> - **REGIME / PHASE-STATE:** near-yield crossing, **Regime II→III** (V_SNAP-referenced three-regime convention, `k4_tlm.py:308–311`). The registered drive `r∈[0.4,1.0]` spans Regime II into III/rupture — the band the thixotropy prereg §2.6/§40 mandates (bulk, near-yield; NOT the transverse achromatic sector, which is rate-asymmetry-free by construction).
> - **DISCIPLINE:** frozen-then-run (protocols pushed before driver code); engine/meter byte-UNTOUCHED (kernel byte-locked to `k4_tlm.py:283,291` and proven bit-identical by test); Rule-11 (frozen adjudication governs the verdict; findings do not retro-edit it); flag-don't-fix; verify-before-cite.

**Date:** 2026-07-19 · **Lane:** implementer, yield-fork discriminators (Grant dispatch 2026-07-19) · **Branch:** `feat/yield-fork-discriminators` · **Sidecar:** `research/2026-07-19_yield-fork-discriminators_result.json`

**The fork this lane serves (unchanged, OPEN, ruling stays Grant's):** *finite-area memristive loop (`∮S dr≠0`, dissipative) vs zero-area saturating reactance (lossless refusal) at the near-yield crossing* (`research/2026-07-17_regime-iv-dissipation-audit.md` §5). Grant's reversible-reactive lean is RECORDED; the fork stays OPEN; this lane RUNS the two registered discriminators. **It does not close the fork.**

---

## 1. Headline

| Leg | Frozen protocol | Verdict (frozen bin) | One line |
|---|---|---|---|
| **A — thixotropy τ** | `2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md` (+ PROTOCOL-COMPLETION 2026-07-19) | **B** (rectification door closed by derivation) | canonical kernel has **no genuine `sign(dr/dt)` memory** and is dissipative → excluded from bin A |
| **B — loop area** | `2026-07-19_yield-fork-loop-area_PROTOCOL-COMPLETION.md` (`P_phase5`, `tau-relax-derivation.md:109`) | **NEITHER** (fail-closed) | loop is **finite** (not zero) but the (r,S) peak is at `ωτ≈1.00`, **outside** the P_phase5 `[0.85,0.95]` window |

**Neither leg adjudicates the fork against Grant's lean.** Both relocate the crux to the same upstream object: **`#59` Flag F** — whether the near-yield `S`-dynamics are *first-order overdamped* (dissipative, the frozen model) or *second-order reactive* (`I_S≠0`, lossless, Grant's branch). That is a **derivation** question, upstream of and unreachable by either driver. Routed to Grant (§6).

---

## 2. What was run (both legs share one byte-locked kernel; engine untouched)

Canonical Level-2 kernel, **byte-locked to the engine**:
- `S_eq(r) = √(max(0, 1 − min(|r|,1)²))` — verbatim `k4_tlm.py:283`.
- Level-2 ODE `dS/dt = (S_eq − S)/τ_relax`, backward Euler `S_{n+1} = (S_n·τ + dt·S_eq)/(τ + dt)` — verbatim `k4_tlm.py:291`.
- Engine-native units: `τ_relax = TAU_RELAX_NATIVE = 1.0` (constants.py:453, asserted in-driver), `V_SNAP=1`, `ℓ_node=1`, `m_e c²=1`, so `r ≡ V/V_SNAP`, `ωτ=ω`.
- Symmetric drive `r(t)=0.7+0.3·sin(ωt)` (registered `#59` §6.4/§11 near-yield point). `dt=min(2π/ω/512, τ/50)`; settle `max(8 periods,20τ)`; measure the last full steady-state period.

**Byte-match is proven, not assumed:** `test_yield_fork_discriminators.py::test_backward_euler_bit_identical_to_engine` drives a live `K4Lattice3D(use_memristive_saturation=True)` at one site and asserts its `S_field` equals the driver's `be_step` iteration to `rel=1e-12` using the engine's own `dt, tau_relax`. Engine byte-UNTOUCHED.

---

## 3. Leg A — thixotropy amplitude-dependent-τ

**Question (prereg §1):** does `τ_relax(A)` carry a `sign(dA/dt)` memory (true two-τ thixotropy → rectifies → a genuine directional loop) or is it an instantaneous even `τ(A)` (time-symmetric → no rectification)? **A ⇔** non-zero net area *with H conserved* (reactive rectifier); **B ⇔** no sign-memory OR the area is dissipative (loss, not H-conserving thrust).

**Three arms, one symmetric near-yield drive** (all reach Regime III: `max_r=1.000`; all finite):

| Arm | raw `R` | raw `Δτ_rel` | `W_cycle` (∮S dr) | reading |
|---|---|---|---|---|
| 1 · canonical single-τ | −0.200 | 0.540 | 0.174 | dissipative; raw asymmetry present |
| 2 · two-τ control (`τ_down=3τ_up`) | −0.539 | 1.011 | (dissipative) | **instrument LIVE** |
| 3 · even `τ(A)=τ(1+A²)` | −0.031 | 0.618 | (dissipative) | amplitude-dep alone: small `R` |

**Finding F-A1 (discovered at integrator time — Rule-10 empirical-driver discipline).** The frozen A.4 raw observables `R` and `Δτ_rel` are **contaminated by nonlinear loop-shape asymmetry** at the strongly-nonlinear registered point (`r→1`). Proof: the single-τ raw `R` **scales with drive amplitude and vanishes as Δr→0** — `R(Δr=0.30)=−0.200 → R(Δr=0.02)=−0.009 → R(Δr=0.01)=−0.005`. A single-τ model has **zero** sign-memory by construction, so this residual `R` is a memoryless nonlinear-loop artifact, not memory. The frozen classifier therefore sub-labels arm 1 "B-anelastic" — an artifact of the contaminated raw observable (disclosed; the verdict-CLASS is robust, below).

**The CLEAN referenced discriminator (τ-swap sign-flip) — the airtight isolation of genuine memory:**
- `R_mem ≡ R(model) − R(single-τ baseline)`. Single-τ baseline `R=−0.200` is the memoryless midpoint.
- two-τ **down-slow** (`τ_down=3τ_up`): `R_mem = −0.339`.
- two-τ **up-slow** (`τ_up=3τ_down`): `R_mem = +0.379`.
- **They FLIP SIGN under the swap** → genuine `sign(dr/dt)` memory. Single-τ: `R_mem = 0` → **no genuine sign-memory**.

**Verdict A = B (robust, via the H-gate — NOT contaminated):** bin A requires `W_cycle ≤ tol` (H-conserved). The canonical loop is **dissipative**, `W_cycle = 0.174 ≫ tol = 0.0035` → **excluded from A regardless of any memory estimate**. Combined with the clean result (`R_mem = 0`, no swap-flip → no genuine memory), the canonical kernel **does not rectify a symmetric drive** → the rectification-thrust door is **closed by derivation** (upgrades the prereg's dead-by-default to dead-by-proof on the sign-memory axis). The two-τ positive control fires (instrument live), so the null is real, not a dead instrument.

**Structural corollary (ties Leg A to the fork):** every first-order relaxation (single- **or** two-τ) is dissipative (`W>0`), so **bin A is structurally unreachable within the first-order framework**. A *reactive* (H-conserving) rectifier requires the **second-order reactive `S`-structure = `#59` Flag F = the lossless branch of the fork.** Leg A thus kills the *two-τ thixotropic* version of the dissipative branch and points the only surviving route to A at Flag F.

---

## 4. Leg B — memristor loop-area (`P_phase5_memristor_loop_area`)

**Prediction (`tau-relax-derivation.md:109`, `#59` §6/§11):** loop area `= ℓ_node²·m_e c²·f(ωτ)`, `f` a K4-nonlinear-corrected Debye shape **peaking at `ωτ≈0.9`**, falsification window **`[0.85,0.95]`**.

**Integrator floor (frozen §6):** both analytic-zero limits give `ε_qs = ε_fr = 3.53×10⁻⁴`; `tol = 10·max = 3.53×10⁻³`.

**Measured (60-pt `ωτ`-sweep + fine-grid peak refit):**

| Quantity | (r,S) plane [primary] | (V,I) Lissajous [cross-check] |
|---|---|---|
| peak `ωτ` (Δr=0.30) | **1.001** | 0.911 |
| peak `ωτ` (Δr=0.25, sub-rupture) | 1.001 | 0.955 |
| area at peak | 0.175 (`≫ tol`) | 0.086 |

**Adjudication (frozen bins, verbatim):** the (r,S)-plane area is **FINITE** (`0.175 ≫ tol`) → **not** the zero-area lossless bin; but the peak `ωτ=1.001` is **OUTSIDE `[0.85,0.95]`** → does **not** match P_phase5 → **NEITHER / fail-closed**.

**Finding F-B1 — the P_phase5 nonlinear peak-shift is NOT reproduced in its stated plane.** The (r,S) loop peaks at `ωτ=1.00` — the **linear** Debye value (`#59` §6.2), not the nonlinear-corrected `0.9` (`#59` §6.3-6.4). Per `#59` §11's own falsifier ("peak outside `[0.85,0.95]` → higher-harmonic corrections or a different axiom-derivation required"), the specific two-channel peak-shift sub-prediction is **falsified in the (r,S) plane** at the registered operating point. `#59` §6.5 Flag C already warned the two-channel form is not the full nonlinear solution; running it confirms the shift does not survive. (The (V,I) plane peaks at 0.911, inside — but see F-B2.)

**Finding F-B2 — the (V,I) "pinched hysteresis" registration does not apply at the near-yield point.** `nonlinear-vacuum-capacitance.md:66` registers a Lissajous that "passes through the origin." At `r_0=0.7, Δr=0.3` the drive `r∈[0.4,1.0]` **never crosses `r=0`**, so `min|I|=0.354 ≠ 0` → the loop is **offset, not origin-pinched**. The origin-pinch is a property of a full-swing drive, not the small-amplitude near-yield drive `#59` registered; the (r,S) plane is the appropriate one here (and it is the plane the prediction is stated in, `tau-relax:24`).

**Finding F-B3 (the H-ledger throughline).** The loop area is a **rate-dependent Debye lag**: it → 0 in **both** the quasi-static (`ωτ→0`) and frozen (`ωτ→∞`) limits (`3.53×10⁻⁴` each vs `0.175` at peak). A rate-dependent lag is produced by a reactive element too; **the finite `∮` alone does not require a resistor.** Its *dissipative* reading is inherited from the **first-order overdamped** model structure (Eq 2.1), which `#59` §12 **Flag F** flags as *asserted, not derived*. A second-order kinetic-`S` form (`I_S≠0`) gives the **same** `τ`-lag but conserves H (lossless). So the frozen bin's identity "finite `∮` = dissipative" is exactly the assertion the fork questions — the measurement confirms the lag is finite and rate-dependent; it does **not** independently establish dissipation.

---

## 5. Capability finding (experiments-fully-lattice-derived rule)

`#59` §10 and `tau-relax-derivation.md:117` state the dynamic Level-2 `S(t)` relaxation-ODE was **UNBUILT** ("flagged for future engine work"). **This is now stale:** the engine implements it via `use_memristive_saturation=True` (`k4_tlm.py:266–296`, backward Euler at `:291`), added since `#59` was written. So Leg B did **not** require an engine change — the drivers reproduce the engine's own memristive update (byte-match test) with the engine byte-untouched. **No CANNOT-RUN-AS-FROZEN was needed; no silent approximation was made.** (Routed as a doc-staleness flag for the auditor lane: `tau-relax-derivation.md:117` and `#59` §10/§28 should note the capability now exists; I surface it, the auditor lands it.)

---

## 6. FORK ADJUDICATION — routed to Grant (NOT closed here)

Per the KEEP-BOTH fork record (`2026-07-17` §5): the substrate decides via the registered discriminators; the ruling stays Grant's. Both discriminators ran cleanly. What each outcome means for the fork:

- **Leg A (B):** the canonical kernel has **no genuine `sign(dr/dt)` memory** and is dissipative → the **two-τ thixotropic (fast-liquefy/slow-refreeze)** version of the dissipative branch is **closed by derivation.** This does *not* settle dissipative-vs-reversible for the *symmetric* single-τ loop (a symmetric loop can be either); it kills only the directional/thixotropic sub-branch and shows the only route to a *reactive* rectifier (bin A) is the **second-order reactive structure = Flag F = your lossless branch.**
- **Leg B (NEITHER):** the loop is **finite** (argues against a *strict* zero-area reading at the (r,S)-area level) but its peak **fails the P_phase5 magnitude test** (peak at `1.00`, not `0.9`, in the stated plane) → the specific memristive prediction is **not confirmed** and its peak-shift sub-claim is **falsified.** And (F-B3) the finite area's *dissipative* character is inherited from the first-order model, not measured — so a finite `∮` does not by itself falsify your reversible lean.

**Net for the fork.** Neither discriminator adjudicates against your reversible-reactive lean. They **converge on relocating the crux to `#59` Flag F**: *is the near-yield `S`-dynamics first-order overdamped (dissipative) or second-order reactive (`I_S≠0`, lossless)?* That is a **derivation** question — deriving the overdamped limit rigorously from a K4 Lagrangian with a kinetic term in `S` (Flag F / Flag A), showing whether `I_S→0` is forced. Until that is done, the memristive-loop object stays **LOSS-REQUIRED by its own prose but NOT axiom-forced** (exactly the `2026-07-17` §5 status). **Fork stays OPEN.** Recommended next step (yours to call): a Flag-F derivation branch, not another driver — the drivers have said what they can.

**Adjudication criteria were NOT dropped to convert a verdict (Rule-11):** Leg A's literal frozen classifier output (arm-1 "B-anelastic") is preserved in the sidecar; the robust verdict-class (B, not-A) is reached via the un-contaminated H-gate, with the contamination disclosed as F-A1. Leg B's NEITHER is the literal frozen bin.

---

## 7. Gates, deviations, status

**Gates (all pass):** regime gate (drive reaches Regime III, `max_r=1.00`); finite gate (all swept points finite; no blow-up); byte-match gate (driver kernel bit-identical to engine, `rel<1e-12`); symmetric-drive gate (drive is a pure symmetric oscillation, no banned waveform asymmetry); positive-control gate (two-τ instrument LIVE).

**Deviations disclosed:**
1. Leg B protocol is a **standalone frozen doc**, not a bottom-append (the `P_phase5` prediction lives in a claim-hosting KB leaf, not an editable prereg — auditor-lane/Rule-12). Disclosed in that doc §0.
2. **F-A1** frozen raw observables contaminated by nonlinear loop-shape → clean referenced τ-swap discriminator supplied; verdict-class robust via H-gate. Frozen output preserved.
3. **F-B1** P_phase5 peak-shift not reproduced in the (r,S) plane (peak 1.00 vs predicted 0.9) → NEITHER.
4. **F-B2** origin-pinch absent at the near-yield operating point.
5. **F-B3** finite `∮` is rate-dependent Debye lag; dissipative reading is model-structural (Flag F), not measured.
6. Leg A driver is **0D** (temporal kernel); spatial self-steepening is out-of-scope **by the prereg's own §4/§7 reversibility guard** (it is not the rectifier). Disclosed in amendment §A.8.
7. Capability staleness: `tau-relax-derivation.md:117` / `#59` §10 "unbuilt" is stale (§5).

**Status tags:**
- **DERIVED:** Leg A no-sign-memory → B (H-gate + τ-swap flip); bin-A-requires-Flag-F corollary.
- **VERIFIED:** engine byte-match (`rel<1e-12`); independent shoelace re-derivation of `∮` (`rel<1e-12`); zero-limits below `0.01×`peak; amplitude-scaling of the artifact; positive-control liveness. `make verify` PASS; `ruff` clean; 13/13 tests pass (routed to `make test-engine`).
- **BLOCKED / OPEN (routed to Grant):** the fork itself — resolvable only by a **Flag-F derivation** (first-order overdamped vs second-order reactive `S`-dynamics), not by a driver.

*Run 2026-07-19 by Opus 4.8 (implementer lane) per Grant's yield-fork discriminator dispatch. Frozen protocols governed; deviations recorded as findings; the fork ruling stays Grant's.*
