# PREREG (FROZEN-BY-PUSH) — Flag-F three-form contrast battery (yield-fork adjudicator, Stage 2)

> **SECTOR HEADER (read first).**
> - **MODE:** frozen prereg for a three-way 0D contrast on ONE `(V,I)` protocol. Pushed **before** any driver code (freeze-by-push; the push timestamp is the real margin). No post-hoc freedom.
> - **REGIME / PHASE-STATE:** near-yield crossing, Regime II→III (`k4_tlm.py:308–311`), driven time-domain, `A=V/V_SNAP→1`.
> - **CLASS (consistency-vs-emergence):** **CONSISTENCY.** The comparison targets — the `(V,I)` peak `ωτ=0.911` / sub-rupture `0.9577` (`#735` engine-measured, `2026-07-19_yield-fork-discriminators_result.md:81–82`) and the `[0.85,0.95]` (`#59` §11) / `0.954–0.978` (`#59` Eq 6.3 own-arithmetic, `#735` F-B1) windows — are engine-measured / corpus-registered, NOT CODATA. This tests whether a DERIVED form reproduces a MEASURED datum. No emergence claim.
> - **DISCIPLINE:** freeze-then-run; Rule-11 (the frozen tree governs the verdict; findings do not retro-edit it); flag-don't-fix; verify-before-cite; engine BYTE-UNTOUCHED (the shipped form byte-matches `k4_tlm.py:283,291`, the other two are standalone research drivers). KEEP-BOTH on the two windows and the two drive amplitudes.

**Date:** 2026-07-19 · **Lane:** implementer, Flag-F derivation Stage 2 · **Branch:** `feat/flag-f-s-dynamics`.
**Gated by:** `research/2026-07-19_flag-f-s-dynamics-derivation.md` §8 (landed cleanly in world (a); the (a)/(b)/shipped forms defined as `ζ=0 / 0<ζ<∞ / ζ→∞` corners of one damped-bow-oscillator).

---

## 1. What Stage 2 decides (and what it does NOT)

**Decides:** on the identical `#735`-Leg-B drive family, does the DERIVED reactive form (world a) reproduce the `(V,I)` peak near `0.911` that `#735` found leaning toward the memristive window — and is its loop **shape class** distinguishable from the shipped Eq 2.1 Debye shape? Per the frozen decision semantics (§6): **if multiple forms land in-window, the datum does not discriminate (say so); if exactly one does, the substrate has spoken.**

**Does NOT decide:** the fork itself — the derivation already ruled world (a) at the crossing (§8 of the derivation). Stage 2 is the empirical cross-check that (i) confirms the reactive form's resonant/phase-inversion shape class is real and distinct from Debye, and (ii) tests whether the peak-location axis is discriminating or degenerate. Rule-11: the derivation verdict is not retro-edited by Stage 2; Stage 2 reports the frozen bins.

## 2. The three forms (frozen definitions; native units `τ_relax=1, V_SNAP=1, ℓ_node=1, Z_0=1`)

Shared drive (registered, `#59` §6.4/§11, identical to `#735` Leg B): `r(t)=r_0+Δr·sin(ωt)`, `r_0=0.7`, `Δr=0.3` (primary); sub-rupture `Δr=0.25` (max `r=0.95`) KEEP-BOTH robustness axis. `S_eq(r)=√(max(0,1−min(|r|,1)²))` (`k4_tlm.py:283`, byte-verbatim).

- **Form S (shipped, `ζ→∞` / first-order Eq 2.1):** `dS/dt=(S_eq−S)/τ_relax`, backward Euler `S_{n+1}=(S_n·τ+dt·S_eq)/(τ+dt)` (`k4_tlm.py:291`, byte-verbatim). **No free parameter** (`τ=1`). Reuses `yield_fork_kernel.py` (the `#735` byte-locked kernel).
- **Form R (reactive, world a, `ζ=0.1` underdamped):** `S̈ + 2ζω_S Ṡ + ω_S²(S−S_eq(r(t)))=0`, `ζ=0.1` (lightly damped → a well-defined periodic steady state with a Lorentzian resonance; the physically-realized near-crossing `ζ≈0` form — pure `ζ=0` is secularly unbounded at exact resonance, disclosed). Symplectic/RK integrator, energy-audited. **Scan** `ω_S·τ ∈ logspace(log10 0.3, log10 3, 25)` (the derivation's `ω_S~1/τ_relax` FORM; the O(1) prefactor is calibration-tagged/unpinned — hence a scan, not a single value).
- **Form T (transductive crossover, world b, `ζ=1.0` critical):** same 2nd-order ODE, `ζ=1.0`. **Scan** the same `ω_S·τ` grid. This is the `0<ζ<∞` corner (resonance broadened by a derived transduction `Γ`).

**Family identity (frozen):** all three are corners of `I_S S̈ + Γ Ṡ + κ_eff(S−S_eq)=0`, `ω_S²=κ_eff/I_S`, `ζ=Γ/(2√(I_S κ_eff))`. Form S is the `I_S→0, ζ→∞, τ_eff=Γ/κ_eff=1` overdamped limit (derivation §5.1). The consistency check `ζ_R < 1 < ζ_S=∞` orders the three forms.

## 3. ω-sweep and the two registered planes (identical to `#735` Leg B)

Sweep `ωτ ∈ logspace(log10 0.05, log10 10, 60)`. At each `ωτ`, on the last full steady-state period (settle `max(8 periods, 20τ)`; `dt=min(2π/ω/512, τ/50)`; for Form R/T also `dt ≤ (2π/ω_S)/64` to resolve the bow mode):
- **Plane 1 — `(r,S)`** (`tau-relax-derivation.md:24`): `A_rS = |∮ S dr|` (trapezoid).
- **Plane 2 — `(V,I)`** (`nonlinear-vacuum-capacitance.md:66`): `V=r`, `I=r·√(max(S,0))` (Op14 `Z_eff=Z_0/√S`, native `Z_0=1`); `A_VI=|∮ I dV|`; record `min|V|,min|I|` (origin-pinch check, F-B2).

For Forms R/T the peak `ωτ*` is reported **per scanned `ω_S·τ`** (the peak tracks the resonance). For Form S the peak is single-valued (byte-locked).

## 4. Regime gates (fail-closed, checked FIRST — before any adjudication)

- **G0 Regime gate:** drive reaches Regime III (`max r ≥ √3/2`; at `r_0=0.7,Δr=0.3`, `max r=1.0`). Fire.
- **G1 Finite gate:** every swept point of every form finite; any non-finite point banks INSTRUMENT for that point (excluded from peak fit); a wholly non-finite form banks INSTRUMENT-DEAD (Form R at `ζ=0.1` is bounded by construction; if it blows up the ζ is too small — disclosed, re-run at `ζ=0.15`, not retro-edited).
- **G2 Byte-match gate (load-bearing):** Form S per-step update **bit-identical** to a live `K4Lattice3D(use_memristive_saturation=True)` driven at one site, `rel<1e-12`, using the engine's own `dt, tau_relax`. If it fails, the leg does not run (CANNOT-RUN-AS-FROZEN). Forms R/T are standalone (no engine analog to byte-match; their integrators are energy-audited instead — G3).
- **G3 Energy-audit gate (Forms R/T):** for `ζ=0` control the symplectic integrator conserves the oscillator invariant `E=½I_S Ṡ²+½κ_eff(S−S_eq)²` to `<1%` over a period at off-resonance `ω`; confirms the reactive integrator is not spuriously dissipating. (At `ζ>0` the audited quantity is the transduced work `Γ∫Ṡ²dt` matching `∮` to `<5%`.)

## 5. The three frozen discriminator axes (KEEP-BOTH on windows + amplitudes)

- **Axis (i) — `(V,I)` peak location vs the measured datum.** Compare each form's `(V,I)` peak `ωτ*` to `0.911` (registered `Δr=0.3`) and `0.9577` (sub-rupture `Δr=0.25`), against **BOTH** windows: legacy `[0.85,0.95]` (`#59` §11) **AND** Eq-6.3 own-arithmetic `[0.954,0.978]` (`#735` F-B1, `window_test_reframe`). For Forms R/T "in-window" means: **∃ a scanned `ω_S·τ` for which the peak lands in the window** (the peak is `ω_S`-controlled; `ω_S` is calibration-tagged). Report the `ω_S·τ` that achieves it, and whether it is O(1) (i.e. `~1/τ_relax`, physically plausible per the derivation) or requires an implausible `ω_S`.
- **Axis (ii) — origin-pinch yes/no per form.** `passes_through_origin ≡ (min|V|<10⁻³ AND min|I|<10⁻³)`. Expected NO for all (drive `r∈[0.4,1.0]` never crosses `r=0`; F-B2). KEEP-BOTH: also report at sub-rupture.
- **Axis (iii) — loop shape class per form (form-level, dimensionless — the real discriminator).** Classify each form's `A(ωτ)` and its loop **chirality/phase**:
  - **Debye class:** `(r,S)` peak **pinned at `ωτ≈1`** independent of parameters (the F-B1 theorem-of-the-observable); monotonic phase lag `→90°`; loop traversal direction (`sign ∮`) does NOT flip across the sweep.
  - **Resonant class:** `(r,S)`/`(V,I)` peak **tracks `ω_S`** (moves with the scanned `ω_S·τ`); **180° phase inversion through resonance** ⇒ the loop traversal direction (`sign of the signed ∮ I dV`) **FLIPS** across `ω=ω_S`. (This is the `#735` F-B3 retracted-and-corrected signature: *"a lossless second-order kinetic-S is resonant … not the monotonic Debye lag."*)
  - Driver computes: `(r,S)` peak vs `ω_S` (does it track or pin?), and `sign(∮I dV)` across the sweep (does it flip?).

## 6. Decision tree (FROZEN — precedence top-to-bottom)

1. **If G0/G1/G2/G3 fail → INSTRUMENT / CANNOT-RUN.** No verdict.
2. **Axis (iii) shape class is decided first (it is parameter-robust):** Form S must land Debye (peak pinned `ωτ≈1`, no chirality flip); Forms R/T must land Resonant (peak tracks `ω_S`, chirality flips) — this confirms the derivation's `ζ`-family structure. If Form S is NOT Debye or Forms R/T are NOT Resonant → the driver contradicts the derivation → **FLAG, surface to Grant (do not retro-fit).**
3. **Axis (i) peak-location discrimination:**
   - **Both Form S AND (Form R at some O(1) `ω_S·τ`) land in a window** ⇒ **DATUM-DOES-NOT-DISCRIMINATE** (the `0.911` `(V,I)` peak is degenerate between shipped-memristive and derived-reactive; the reactive form's free `ω_S` reaches it). Bank this as the honest outcome and route the true discriminator to Axis (iii).
   - **Exactly one form lands in a window** ⇒ **SUBSTRATE-HAS-SPOKEN** for that form; name it.
   - **No form lands in either window** ⇒ the datum falsifies all three at the registered drive; bank fail-closed.
4. **Axis (ii) origin-pinch** is reported as a registration-quality caveat (per form), not a pass/fail gate (F-B2 established the near-yield drive is not origin-pinched).
5. **Precedence:** Axis (iii) shape class (structural, parameter-robust) **outranks** Axis (i) peak location (parameter-tunable for R/T) for the physics verdict. The final banked verdict states: which shape class each form is in (structural), and whether the peak-location datum discriminates (degenerate vs decisive).

**Anti-rescue lock (Rule-11):** if Form R fails to reach a window for any O(1) `ω_S·τ`, that is banked as-is (reactive form falsified on the peak axis at the registered drive); the `ω_S` scan is NOT widened post-hoc beyond the frozen `[0.3,3]·(1/τ)` grid to manufacture a match.

## 7. Integrator floor (frozen)

Reuse the `#735` Leg-B floor: quasi-static `ωτ=10⁻³` and frozen `ωτ=10³` both give analytic-zero `∮` for Form S; `tol=10·max(ε_qs,ε_fr)`. For Forms R/T the floor is the G3 energy-audit residual. `A_rS>tol` ⇒ finite; `≤tol` ⇒ zero-area.

## 8. Deliverables + disclosure

- `research/2026-07-19_flag-f-s-dynamics/` : `reactive_kernel.py` (Forms R/T 2nd-order integrator), `contrast_battery.py` (three-form sweep + frozen adjudication), `test_flag_f_s_dynamics.py` (G2 byte-match + G3 energy-audit).
- `research/2026-07-19_flag-f-s-dynamics_result.md` : the frozen-tree outcome + any deviations as findings (Rule-11: frozen tree not retro-edited).
- Engine BYTE-UNTOUCHED. Form S reuses the `#735` byte-locked kernel; Forms R/T are standalone research drivers.
- Any deviation discovered at integrator time (Rule-10) is disclosed as a finding, not folded into the frozen tree.

---

*Frozen-by-push 2026-07-19 by Opus 4.8 (implementer lane), BEFORE driver code, per the yield-fork adjudicator dispatch Stage-2 gate. The frozen decision tree (§6) governs the verdict; Stage-2 does not retro-edit the derivation's world-(a) ruling (Rule-11).*
