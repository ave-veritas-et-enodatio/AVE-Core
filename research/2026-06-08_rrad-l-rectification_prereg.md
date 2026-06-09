# Prereg — acoustic-rectification DC momentum (dark-wake thrust, Phase 2)

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-rrad-l-darkwake` (CONTINUATION of Phase 1; same branch)
**Status**: FROZEN prereg (pre-driver). Phase 2 of the dark-wake thrust derivation.
**Phase-1 result**: [`2026-06-08_rrad-l-darkwake_result.md`](2026-06-08_rrad-l-darkwake_result.md)
**Adjudication seed**: [`AVE-Propulsion-ionpump/research/2026-06-08_NEXT-STEP_Rrad-L_core-brief.md`]
§"ADJUDICATION 2026-06-08 (Grant) — genuine substrate bounce + acoustic rectification".
**Home leaf (mechanism)**: AVE-Propulsion `manuscript/vol_propulsion/chapters/03_acoustic_rectification.tex`.
**Target gap**: the OPEN τ_zx step-1 thrust object at
[`dark-wake-bemf-foc-synthesis.md:98`](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md),
claim `clm-7tynm2`.

> **REFRAME (load-bearing, the whole reason for Phase 2).** Phase 1 measured the
> **WRONG object**: a steady-CW **LINEAR radiation resistance** `R_rad,L`, and
> correctly found the mode propagating but **reactance-dominated (high-Q)** → "poor
> radiator." Grant's adjudication: the actual thrust is the **SECOND-ORDER,
> asymmetric-cycle RECTIFIED DC momentum** — a different OBJECT (2nd-order time-avg
> directed momentum, not linear R) AND a different DRIVE (asymmetric slow-grip /
> fast-slip duty cycle, not steady CW). Under rectification the **high reactive
> store `X_L` from Phase 1 is the RESERVOIR you pump** — high-Q is a FEATURE, not a
> defect; the deflation inverts. The thrust object is the four-stroke ledger's
> **enclosed area ∮V dq** (2nd-order rectified work/cycle), restated as momentum.

---

## 1. Target (the RIGHT object)

Compute the **rectified DC momentum flux** the substrate carries away per cycle
under an **asymmetric duty-cycle drive** — the "genuine substrate bounce."

    ⟨τ_zx⟩_DC  ≡  time-averaged, DIRECTED net momentum flux  (acoustic rectification)

Two independent measurement channels (cross-check, per reactance-pair discipline):

- **Primary — substrate-recoil momentum drift.** `P_x(t) = ρ Σ_interior u̇_x`,
  the total translational x-momentum in the PML-excluded interior. The **linear
  drift** of `P_x` over an integer number of duty cycles = the net momentum the
  substrate accumulates per unit time = the recoil thrust (Newton-3 mirror of the
  hull reaction). Normalization-light; the cleanest "ledger ∮≠0 / substrate
  recoils" signature.
- **Corroborating — far-plane momentum flux.** `⟨T_pp⟩_far`, the time-averaged
  axial momentum-flux tensor component through the PML-excluded far plane:
      `T_ij = −σ_ij + ρ u̇_i u̇_j`   (Cauchy stress + 2nd-order convective)
      axial thrust carried downstream = `⟨T_pp⟩` over integer duty cycles,
      `p` = propagation/drive axis.
  The linear `⟨−σ_pp⟩` averages to ≈0 for a symmetric drive but NOT for the
  rectified asymmetric cycle (σ→0 in the saturated-slip phase, large in the grip
  phase); the convective `ρ⟨u̇_p²⟩` is intrinsically 2nd-order DC. Both are the
  rectification.

This REPLACES the Phase-1 linear `R_rad,L = P_rad/(½|I|²)` object. Phase 1's
`R_rad,L`/`X_L` machinery (energy flux `I_k`, near-field store) is reused only to
characterize the **reservoir** (`X_L`) being pumped, not as the thrust.

## 2. Mechanism (canonical leaf, verbatim)

From `03_acoustic_rectification.tex` (the home leaf), the asymmetric flyback
stroke bifurcates against the Axiom-4 saturating dielectric:

- **Slow edge (Dielectric Grip):** `|V| < V_sat` → high-reluctance insulator;
  the system **inductively grips the lattice**, transferring a macroscopic
  reaction force to the hull.
- **Fast edge (Inductive Yield):** the nanosecond kickback `|V| ≫ V_sat` → the
  vacuum **yields and slips backward through a saturated zero-impedance phase
  (Γ = −1)**, transferring **zero negative momentum** to the vessel.
- Time-averaging the asymmetric interaction over the full duty cycle yields a
  **continuous DC kinematic thrust**. A **symmetric sine → exactly zero**
  time-averaged thrust.

The rectifier is the Axiom-4 saturation kernel `S(A) = √(1−(A/A_yield)²)`: the
grip stroke rides `S ≈ 1` (high-impedance), the slip stroke crosses `A_yield`
(`S → 0`, zero-impedance). In the engine the Cosserat sector saturates at
`A² = |ε|²/ε_yield² + |κ|²/ω_yield²`, `ω_yield = π`, `ε_yield = 1`
([cosserat_field_3d.py:332,837](../src/ave/topological/cosserat_field_3d.py)).

## 3. Substrate-native RE-WALK (substrate-native-check — for the NEW observable + drive)

The brief §2 walked the 8 checkpoints for the **linear** object (steady-CW R_rad,L,
energy flux). This RE-WALKS them for the **2nd-order DC momentum** under a
**nonlinear time-domain duty-cycle** drive — a different physics class.

- **CP1 (dynamics):** the substrate runs **nonlinear wave propagation under a
  time-varying drive**; the observable is a **cycle-averaged SECOND-ORDER**
  quantity. Method = direct time-domain integration + integer-cycle averaging of
  the momentum-flux tensor. **NOT** eigensolve / Hessian / energy-minimization. The
  rectification LIVES IN THE NONLINEARITY — a linearized/eigenmode treatment
  returns DC ≡ 0 by construction. **This is precisely why the Phase-1 linear pass
  returned "high-Q poor radiator": it measured the linear object, which has no DC.**
- **CP2 (sector):** cross-coupled (Op14). The chiral Cosserat-**ω** drive couples to
  the (u, ω) sector; the rectified DC momentum rides the **translational u**
  sector (the bounce). Bulk-vs-shear of that u is the OPEN question (§7).
- **CP3 (objective):** the thrust = cycle-averaged **directed momentum** (P_x drift
  + ⟨T_pp⟩_far), the ledger ∮V dq restated as momentum. NOT a linear impedance.
- **CP4 (coordinates) — phase-space-coordinate-check (A46):** the drive is specified
  in **operating-point / saturation phase-space** (the duty cycle is a trajectory
  on the Axiom-4 kernel: slow excursion in the sub-yield grip region `S≈1`, fast
  excursion across `A_yield` into the slip region `S→0`). The measured DC momentum
  is a **real-space directed force** — a directed force IS genuinely a real-space
  object, so real-space measurement is correct here (no A46 mismatch). The
  rectification claim is exactly "phase-space duty asymmetry → real-space DC
  momentum." **Discipline kept distinct:** the duty cycle is characterized by its
  **saturation-state excursion** (does the fast edge actually cross `A_yield`?),
  recorded as `A²_max(t)` at the source — not merely by amplitude. A duty cycle
  that never engages saturation is a linear fast edge and CANNOT rectify; that is a
  pre-registered null-mechanism guard, not a result.
- **CP5 (local clock — LOAD-BEARING, A-Rule 10 local-clock-modulation):** the
  fast-slip edge drives `A → A_yield` locally → `S → 0` → `c_shear = c₀√S → 0`
  (local clock freezes) and `Γ → −1` (zero-impedance slip). Record the local
  saturation state `A²(r)` at the source over the cycle; the slip phase MUST
  engage `S → 0` for the rectification to be substrate-native. Report
  `ω_local(r) = ω_global·√(1−A²(r))` excursion at the load-bearing slip site.
- **CP6 (real vs reactive) — reactance-pair tracking (A-Rule 10):** the Phase-1
  high reactive store `X_L` is the **reservoir pumped**; rectification is the valve
  that taps reactive grip → real DC momentum. Record **BOTH** the near-field
  reactive store (grip energy, L-state) AND the far-field real momentum (C-state)
  at **every** recorded step over integer duty cycles. A one-phase snapshot cannot
  distinguish a static grip from a rectifying oscillator caught at peak.
- **CP7 (sampling):** **PML-exclude** the far plane and the interior momentum sum
  (`pml ≤ idx ≤ N−pml−1`). For the bulk-vs-shear decomposition sample the field
  structure (∇·u, ∇×u) at the far plane, not a centroid+offset.
- **CP8 (emergence — consistency-vs-emergence):** does **NOT** fire. This measures a
  property of a **driven** source (the thruster), not an emergent composite.
  Pre-classify **Class-B manifestation / consistency-class** (same as Phase 1).

## 4. Pre-registered adjudication criteria (LOCKED — no post-hoc drift, Rule 11)

### 4a. RECTIFICATION SIGNATURE (the ledger ∮≠0 — primary result)
The drive is an **asymmetric** slow-charge/fast-quench duty cycle (`charge_frac`
high, e.g. 0.8) vs a **symmetric** control (sine or triangle, `charge_frac = 0.5`),
SAME peak amplitude, SAME carrier, SAME period — the ONLY difference is the
time-symmetry of the envelope.
- **CONFIRMED** ⟺ `|⟨DC⟩_ASYM| ≫ |⟨DC⟩_SYM|` AND `⟨DC⟩_SYM ≈ 0` (symmetric → zero
  net, per `03_acoustic_rectification.tex`). The asymmetric/symmetric contrast IS
  the rectification = the ledger ∮V dq ≠ 0.
- **NULL** ⟺ asymmetric also ≈ 0 (no rectification in this engine / regime) — report
  honestly; the dark-wake-as-rectifier premise weakens.
- **Quantitative gate (locked):** "≈ 0" = within the symmetric-control band; "≫"
  = asymmetric DC at least 3× the symmetric DC magnitude AND above the run-to-run
  spread. Mechanism guard: if the asymmetric DC is nonzero but the fast edge never
  crossed `A_yield` (CP4/CP5), the nonzero is NOT rectification — flag it.

### 4b. CHIRAL-DIRECTED (the thrust is a vector — second breaking)
Run LH and RH at fixed (asymmetric) duty.
- **CHIRAL-DIRECTED** ⟺ `sign(⟨DC⟩_ASYM,LH) = −sign(⟨DC⟩_ASYM,RH)` (handedness sets
  direction), so the **non-chiral combination** `⟨DC⟩_LH + ⟨DC⟩_RH ≈ 0`. An explicit
  **linear (non-helical)** drive at asymmetric duty is also run; expectation ≈ 0.
- **NOT chiral-directed** ⟺ LH and RH give the SAME sign (the DC is a drive-axis
  bias, not handedness-directed).

### 4c. BOTH-BREAKINGS-REQUIRED (the core ledger result)
Confirmed ⟺ all hold on the 2×2 (SYM/ASYM × LH/RH):
- SYM × LH ≈ 0 AND SYM × RH ≈ 0 — **chirality alone is insufficient** (no time-asym).
- ASYM × non-chiral (LH+RH sum, or linear) ≈ 0 — **rectification alone is
  insufficient** (no handedness to direct it).
- ASYM × LH and ASYM × RH nonzero and opposite-signed — **both breakings → directed
  thrust**.

### 4d. BULK-vs-SHEAR mode verdict (open question 1 + the unification gate)
At the far plane decompose the carrier into **dilatational** `(∇·u)²` (P-wave,
bulk-acoustic, `c_L = √2 c₀`, **1/7** sector — the ELECTRON pilot-wave channel,
07_qm:43/02_GR:193) vs **shear** `|∇×u|²` (S-wave, **2/7** sector — the photon
channel). Also test which carries the net DC momentum (the convective `ρ⟨u̇_p²⟩` is
the longitudinal/compressional momentum flux).
- **BULK** ⟺ dilatational dominates AND carries the DC → the genuine bounce rides
  the P-wave; the **Q→∞ electron pilot-wave unification RECOVERS at the mode level**
  (dark wake = electron mode, valve open vs shut). Closes the unification beyond
  principle.
- **SHEAR** ⟺ shear dominates → 2/7/photon channel; unification stays
  **mode-blocked** (Phase-1 linear verdict holds for the rectified object too).
- Pre-registered expectation is genuinely OPEN — Grant's "genuine substrate push"
  read points to BULK (mechanical acoustic bounce, the momentum-carrying
  component), inverting the Phase-1 linear-object SHEAR assignment; the driver
  decides.

## 5. Consistency-vs-emergence pre-classification

`⟨τ_zx⟩_DC` is a property of a **driven** source (CP8 does NOT fire). It is
assembled from corpus quantities (Cosserat moduli, Axiom-4 kernel, the chiral
source) each derived/calibrated from Ax 1+3+4. Therefore the rectified DC momentum
is **axiom-manifestation / consistency-class (Class-B)**, NOT a Class-2 emergence
result. Pre-registered so the rectification signature is not headlined as emergence.
**ave-discrimination-check at result time:** is "rectified-DC-from-reactive-store"
**AVE-distinct**, or is it generic acoustic streaming / Rayleigh radiation
pressure? (Pre-registered discriminator: generic acoustic streaming needs only a
nonlinear medium + asymmetric drive; the AVE-distinct content is whether the
rectifier is specifically the **Axiom-4 saturation valve** AND whether the
direction is set by **substrate chirality** (parity selection), neither of which a
generic Newtonian streaming model carries. If the DC survives WITHOUT crossing
`A_yield` and WITHOUT chiral direction, it is generic streaming, not AVE-distinct.)

## 6. Numerical plan (driver)

`src/scripts/vol_4_engineering/rrad_l_acoustic_rectification.py` (canonical-source
compliant; imports constants from `src/ave/core/constants.py`; reuses the Phase-1
constitutive-stress machinery as the single source of truth):
1. Coupled K4-Cosserat engine + a **`DutyCycleBeltramiSource`** (subclass of
   `CosseratBeltramiSource`) replacing the monotonic ramp/sustain envelope with a
   **periodic asymmetric duty-cycle** amplitude waveform (slow charge / fast
   quench); `charge_frac` parameter sets the asymmetry; `symmetric` mode =
   sine/triangle control; `non_chiral` mode = linear (single-axis) drive.
2. **Momentum-flux extractor** (NEW vs Phase 1's energy flux): `T_ij = −σ_ij + ρ
   u̇_i u̇_j` with `σ = ∂W/∂ε` (mirrors Phase-1 constitutive stresses). Headline =
   interior `P_x` drift + far-plane `⟨T_pp⟩`.
3. **Reactance-pair recording (CP6):** near-field grip store + far-field momentum +
   source `A²_max` at every recorded step over integer duty cycles.
4. **2×2 + controls:** {SYM, ASYM} × {LH, RH} + (ASYM × non-chiral linear).
5. **Bulk-vs-shear:** far-plane `(∇·u)²` vs `|∇×u|²` + which carries the DC.

**Honest scope (ave-driver-script-honesty):** the **absolute thrust magnitude is
BLOCKED** (needs a converged radiating sim + a defensible source-"current"
normalization — the same gate as Phase 1). The achievable, high-value result is the
**qualitative rectification signature** (symmetric→0, asymmetric→nonzero,
chiral-directed, both-required) + the **bulk-vs-shear mode verdict** + whether the
**Q→∞ unification recovers**. Report DERIVED / VERIFIED / BLOCKED honestly. A clean
qualitative signature + mode verdict is the success criterion; no false closure on
magnitude.

## 7. Falsifier

If the **asymmetric** duty cycle gives the SAME (≈0) DC momentum as the symmetric
control — i.e. the engine shows NO rectification even with the Axiom-4 saturation
valve engaged (fast edge confirmed crossing `A_yield`) — then the
acoustic-rectification thrust mechanism does not operate in the substrate as
modeled, and the dark-wake-as-thruster premise fails on the 2nd-order object too
(after Phase 1 already deflated the linear object). Honest closure, branch closes.
