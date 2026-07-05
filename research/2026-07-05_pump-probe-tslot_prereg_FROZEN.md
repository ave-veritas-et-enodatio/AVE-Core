# PREREG (FROZEN) — Pump-probe on the honest nonlinear chain: the substrate adjudicates the #526 T-slot scope fork

> ## ⚠ ERRATUM / DEVIATION BANNER (2026-07-05, orchestrator review of PR #532 — MAJOR-a)
> The frozen prereg (§PROBE, §CONVERGENCE) specified a **genuinely dynamical slow weak probe
> WAVE** — "measuring the effective transverse stiffness / phase velocity in the measurement
> window", with an Ω/ω sweep. **The driver as implemented did NOT run that probe.** It measured
> the **cycle-averaged transverse tangent stiffness** `⟨−∂F_y/∂y⟩` — a frozen-configuration
> finite-difference on the pump snapshots, which OMITS the pump's back-reaction to the probe and,
> critically, is a **LAB-FRAME** observable (it feels the axial spring through the bond slope).
> This silent substitution is the root of the [ADJUDICATION-INVALID] verdict: the finite-difference
> observable is not the frozen dynamical-probe observable, and it mixes in a kinematic tilt term the
> frozen (bond-frame) arms never modeled. The frozen prereg body below is PRESERVED (Rule 12); this
> banner records the deviation. A valid future adjudication must run the frozen dynamical probe (or
> a bond-frame observable) — see `2026-07-05_pump-probe-tslot_result.md` §REQUIREMENTS.
> (The one numeric correction: the DC-BIAS liveness prediction 1.0376 was for a zig-zag held bow,
> found to confound channels; the clean uniform-stretch control 1.0786 is the one that ran.)

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/pump-probe-tslot`
**Driver (dynamics):** `src/scripts/vol_1_foundations/pump_probe_chain.py` (to be scaffolded)
**Prediction module (INDEPENDENT):** `src/scripts/vol_1_foundations/pump_probe_predictions.py` (the frozen arm formulas; NEVER consumed by the dynamics — the #531 tautology guard)
**Tests:** `src/tests/test_pump_probe_chain.py`
**Output:** `src/scripts/vol_1_foundations/_output/pump_probe_chain.json` (driver-regenerable; gitignored)

**Grant directive recorded verbatim (attributed Grant 2026-07-05):**
> "let the vacuum substrate lead the way..."

This freezes the arms and bins BEFORE the honest-dynamics driver runs. Commit order is the freeze proof.

---

## THE FORK BEING ADJUDICATED (from PR #531, the fork-record)

PR #531 (`research/2026-07-05_channel-resolved-loading_result.md`, branch `analysis/channel-discriminator`) dissolved a canon-vs-canon "conflict" into an **OPEN T-slot SCOPE FORK**, Grant's to resolve by fiat OR (Grant's demonstrated standing preference, pre-test-physics-check Trigger 9) by the engine:

- **ARM DC_ONLY** — the #526 frozen scope (`research/2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78): the pre-stress T-slot accepts ONLY a static DC-bias tension `T = Φ'(A_DC)`, which is **0 for a zero-mean AC wave** ("NO ⟨sin²⟩=½ time-average factor"). A traveling transverse pump loads NOTHING; a slow probe through it recovers the cold transverse stiffness.
- **ARM EXTENDED** — this arc's #529 re-keying: the slot accepts the cycle-averaged rectified tension `⟨T⟩ = (k_a/ℓ)y₀² ≠ 0`. A traveling pump adds stiffness; a slow probe through it reads STIFFER than cold.

Instead of a fiat ruling, per Grant's directive, we run the **FULL NONLINEAR DYNAMICS — no slot bookkeeping** — and measure what a slow probe actually sees through a wave-carrying region. **The dynamics do not care how terms were divided between S and T; they just respond.**

---

## PRE-TEST PHYSICS CHECK (pre-test-physics-check, Trigger 6 + 9) — the plumber question surfaced to Grant

**Question (surfaced, recorded per Step 5):** The corpus holds two mechanisms that point OPPOSITE ways on this exact fork:
- The #526 T-slot is DC-scoped (`prestress-tensor_prereg_FROZEN.md`:64-78) — a zero-mean AC wave loads nothing.
- The PONDER-01 **Jensen-rectification chain** (`manuscript/ave-kb/vol4/claim-quality.md:263`: "Axiom 4 (concave S(E) → Jensen rectification)"; `:246` "⟨S⟩<1 → DC stress") says a concave kernel under oscillation DOES rectify to a nonzero DC mean stress.

**Plumber-physically: when a genuine traveling transverse wave runs through the honest bond geometry, does the slow probe feel the rectified 2nd-order mean (⟨T⟩≠0, EXTENDED) or the zero-mean rest state (DC_ONLY)?** My read: **the honest dynamics answer this directly — no fiat ruling needed to build** — but flagged because if the Jensen chain is understood to settle it toward EXTENDED, then a NEITHER/EXTENDED verdict is the *expected* outcome, not a surprise. **Authorization to proceed: Grant's 2026-07-05 directive "let the vacuum substrate lead the way" IS the run-the-engine authorization (Trigger 9, standing preference (b)).** The Jensen tension is surfaced prominently in the result doc for Grant at review.

---

## SUBSTRATE-FIRST SECTOR HEADER

- **SECTOR:** translational-u elastic sector of the ratified chiral srs — but the ADJUDICATION is done on a **2-DOF-per-node chain** (longitudinal u + transverse y) as the minimal honest carrier of the transverse-to-axial coupling. BOTH the axial spring (k_a) and shear spring (k_s) are translational-u / **capacitive** springs of the same bond (PR#516). The transverse-to-axial coupling is NOT inserted by hand — it arises from the exact bond-length function `L = √((a₀+Δu)² + (Δy)²)`.
- **MODE:** TIME-DOMAIN nonlinear integration (symplectic velocity-Verlet; energy-drift-gated). NOT a slot-bookkeeping algebra — the whole point is that the dynamics do not know about slots.
- **REGIME:** small-signal ADIABATIC probe (Ω ≪ ω_pump, amplitude ≪ pump) about a traveling pump. Op14/Ax4 kernel ON (the axial constitutive law is the canonical kernel potential Φ). **PHASE-STATE:** sub-yield interior; boundaries absorbing so the pump genuinely travels (SWR measured + reported).
- **DC-vs-AC (AC/DC carve, clm-acdc07):** this is the **AC→AC sibling** of the SPICE lane's DC→AC bias-couples-to-wave rung (`_orchestration/2026-07-03_spice-lane-charter.md`). The pump is an AC traveling wave; the probe is a slow AC transverse signal. The fork is precisely whether the AC pump deposits a DC bias the probe can feel.
- **T2 HOMONYM GUARD (binding, #527):** the transverse bow y is the MECHANICAL T2-response bend of the strut, NOT the Cosserat (2,3) charge winding (`resonant-lc-solitons.md`:95,:128; A1⊥T2). "Transverse" = the mechanical displacement DOF, never re-welded to the winding. mass=A1; charge=Cosserat-winding; bow=T2-mechanical-response.
- **COORDS (A46):** pump/probe amplitudes live in real-space displacement; the measured stiffness is a real-space transverse restoring constant. Both in real-space; A46-clean (this is a real-space dynamical measurement, not a phase-space φ² comparison).
- **CLASS (consistency-vs-emergence):** **CONSISTENCY / DC-internal.** No VALUE derived (2/7, ρ*=9.7734, /7 stay GR-imported, PR#261/#506). This adjudicates which of two bookkeeping scopes the honest dynamics realize. EMERGENCE FORBIDDEN for any value; ½, ¼, 2/7, 9.7734, 2.04% are visible targets, none tuned toward (anti-tune ledger + frozen bins are the guard).

---

## THE HONEST NONLINEAR CHAIN (the load-bearing construction — geometry + kernel, NO slot formulas)

**Host:** an N-node chain, 2 DOF per node — longitudinal `u_i` and transverse `y_i`. Rest spacing `a₀=1` along x̂.

**Bond length (the ONLY source of transverse↔axial coupling — NOT inserted by hand):**
> `L_{i} = √((a₀ + u_{i+1} − u_i)² + (y_{i+1} − y_i)²)`

**Axial constitutive law = the canonical kernel potential Φ** (`scale_invariant.py:107-156`; the merged reading of `bond_force_sign_rule`):
> `Φ''(a) = k₀·S(a) = k₀·√(1 − a²)`  ⟹  `Φ'(A) = k₀·(A√(1−A²) + arcsin A)/2`  (integrate once, sympy-verified: 5 exact-zero residuals, `pump_probe_predictions.py`).

Each bond's axial strain `A_bond = L − a₀`, axial tension `T_bond = Φ'(A_bond)`, transverse restoring stiffness from that bond `T_bond / L` (the string-tension term — arises automatically from the geometry, NOT a T/ℓ slot term inserted by hand). The chain Hamiltonian is `H = Σ_i ½(u̇_i² + ẏ_i²)/m + Σ_bond Φ(A_bond)` — the transverse dynamics inherit their stiffness ENTIRELY from Φ through the bond-length geometry.

**Integrator:** symplectic velocity-Verlet (justified: the measurement is an energy-conservation-sensitive long-time average of a Hamiltonian system; a symplectic integrator bounds energy drift without dissipating the pump; RK would leak amplitude over the recording window and fake the answer). Energy-drift gate: |ΔH/H| bounded over the recording window (target ≤ 1e-4, converged in the dt sweep).

**Boundaries:** absorbing (damped sponge layers or long-chain windows) so the pump is genuinely traveling. **The standing-wave ratio (SWR) in the measurement window is MEASURED and REPORTED** — a hidden reflection fakes the answer (would fabricate a standing-wave antinode ⟨T⟩ per #529 (ii), which is NOT the traveling-wave question).

**Probe:** a slow (Ω ≪ ω_pump), weak (amplitude ≪ y₀_pump) transverse probe measuring the effective transverse stiffness / phase velocity in the measurement window. **Separations declared and SWEPT** (Ω/ω, amplitude ratio) to show the measurement is in the adiabatic small-signal regime.

---

## THE TAUTOLOGY GUARD (#531 lesson, binding) — TWO SEPARATE MODULES

The **prediction module** (`pump_probe_predictions.py`) computes the frozen ARM DC_ONLY / ARM EXTENDED numbers from the merged slot laws (Φ', ⟨T⟩=(k_a/ℓ)y₀², k_trans = k_s + T/ℓ). The **dynamics module** (`pump_probe_chain.py`) integrates the honest chain and measures the probe stiffness from the time-domain response ONLY — it NEVER imports the slot formulas it adjudicates. The **#528 ReconcileGate** compares the two modules' OUTPUTS (measured probe stiffness vs each frozen arm prediction). The measurement must NOT consume the slot formulas.

---

## FROZEN PREDICTIONS (derived symbolically, `pump_probe_predictions.py`; kernel units k₀=ℓ=k_a=k_s=1)

Sympy backbone (5 exact-zero residuals, this session): `∫₀^A Φ'' − Φ'_closed = 0`; `Φ'(0)=0`; `Φ'(1)=k₀π/4`; `⟨sin²⟩−½=0`; `⟨T_pump⟩_lead − (k_a/ℓ)y₀² = 0`.

| State | Predicted transverse stiffness `k_trans` | Basis |
|---|---|---|
| **(a) COLD** (pump off) | **1.000000** = k_s | `k_s·S(0) + Φ'(0)/ℓ = 1 + 0` |
| **(b) DC-BIAS liveness** (honest held bow y_bias=0.1428, tent edge) | **1.037637** (+3.764% over cold; pure geometric T/L term = 0.038437) | held-bow geometry: L=1.039984, A_bond=0.039984, T_dc=Φ'(A_bond)=0.039974, S(A_bond)=0.999200; `k_s·S(A_bond) + T_dc/L` — BOTH terms (constitutive-at-Q + T/ℓ geometric), the merged #526 form |
| **(c) PUMP, ARM DC_ONLY** (y₀=0.1428) | **1.000000** (cold recovered) | pump mean bow = 0 ⟹ slot empty ⟹ no tension term |
| **(c) PUMP, ARM EXTENDED** (y₀=0.1428) | **1.020392** | `k_s + (k_a/ℓ)y₀² = 1 + 0.020392` |

**Arm separation at tent-edge y₀=0.1428:** `(k_a/ℓ)y₀²/k_s = 0.020392 = 2.039%` in stiffness (`√(1+sep)−1 = 1.014%` in phase velocity). At elastica-edge y₀=0.4153 the separation is 17.25% (stiffness). Both well above the demonstrated tolerances (see gate band below). The 2.04% is `(0.1428)² = 0.020394`, a **derived geometric factor** — NOT ½, ¼, 2/7, 9.7734 (knife-clean, §KNIFE).

**Held-bow vs pump consistency (derived):** the held-bow 2nd-order tension (`≈2y²`) is exactly TWICE the pump's rectified mean (`≈y²`) — the `⟨sin²⟩=½` factor. Self-consistent, not tuned.

---

## GATE + DERIVED TOLERANCE (the #531 lesson: no vacuous bands; band just above the derived residual)

Gates are the **#528 ReconcileGate** ONLY (`src/ave/validation/reconcile_gate.py`), can-fire proven on real data paths including dropped-term and sign-flip synthetics. The reconcile band is DERIVED, not vacuous:

- **Truncation/discretization residual** (to be measured in the convergence sweep): the leading finite-dt symplectic energy-drift + the finite-chain SWR-leak + the finite Ω/ω adiabatic-correction. The band = **3× the summed converged residual** (matching the #531 discipline). The gate band will be FROZEN as a number after the convergence sweep establishes the residual floor, and it must be **strictly below the 2.04% arm separation** (else → [UNRESOLVED], and the resolution analysis is reported). The prereg PREDICTS the residual will be ≪ 2% (symplectic drift ~1e-4, SWR-leak controllable to <1% with adequate sponge, adiabatic correction ~(Ω/ω)² ≪ 1); if it is not, that is the [UNRESOLVED] path, honestly reported.
- **Gate the CONSUMED observable** (the probe's measured transverse stiffness / phase velocity), never a proxy.

## POSITIVE CONTROLS (null-verdict liveness, ave-prereg Step 3.8 / pre-test-physics-check Trigger 10)

- **PC-COLD** (mandatory control): pump off ⟹ probe MUST recover k_trans = 1.000000 to tight tolerance. The instrument's zero.
- **PC-DC-LIVENESS** (the MANDATORY structural-null stencil guard): a HELD static bow at y_bias=0.1428 MUST reproduce k_trans = 1.037637 (both terms, +3.76%). **This PROVES the probe can see a genuine tension term when one exists.** If PC-DC-LIVENESS FAILS (the probe does NOT see the held-bow tension), **HALT — the instrument is blind and no null on the pump means anything.** (This is the positive control the pump's possible DC_ONLY null requires: DC_ONLY's k_trans=cold is a null, and a null is only bookable if the same pipeline demonstrably reads the known-nonzero DC-bias case.)
- **PC-SWR**: measured standing-wave ratio in the window reported; a traveling-wave verdict is only read where SWR ≈ 1 (report the number; SWR far from 1 ⟹ the pump isn't traveling ⟹ out-of-scope cell).
- **PC-ENERGY**: |ΔH/H| over the recording window within the drift gate.

---

## BINS (frozen verbatim)

- **[DC-ONLY-CONFIRMED]** — the measured probe stiffness matches the DC_ONLY prediction (k_trans = 1.000, cold recovered) within the honest band and EXCLUDES the EXTENDED prediction ⟹ the #526 scope is engine-confirmed; #518's radiation null stands; the hum-tension carrier is closed dead.
- **[EXTENDED-CONFIRMED]** — matches EXTENDED (k_trans = 1.020392), excludes DC_ONLY ⟹ cycle-averaged tension is real medium bias; #518's null goes up for revision (surface, do not perform it).
- **[NEITHER]** — matches neither ⟹ the slot decomposition itself is wrong at 2nd order; report the measured law honestly (this is a DISCOVERY bin, not a failure).
- **[UNRESOLVED]** — numerics cannot separate the arms (the derived residual band is NOT below the 2.04% separation); show the resolution analysis; name what would resolve it (finer dt, longer chain, better sponge, larger y₀ to elastica edge where separation is 17%).

**Knife ARMED:** the ~2% separation, ½/¼ (derived factors only), 2/7, 9.7734, 1/√α, identity endpoints. If (c) lands ON either prediction suspiciously exactly, VERIFY the prediction wasn't leaked into the measurement (shared code paths — the #531 tautology lesson). The dynamics module and prediction module are separate; the ReconcileGate compares outputs.

---

## DISCRIMINATING OUTCOMES (Step 3 stakes-table, sector-classified)

- **Outcome A (Jensen-leaning):** [EXTENDED-CONFIRMED] — the concave kernel rectifies the traveling pump to a real DC ⟨T⟩ the probe feels. Sector: DC→AC coupling (a DC medium state read out through the AC probe). Bears on #518's null (surface).
- **Outcome B (canon-keying-leaning):** [DC-ONLY-CONFIRMED] — the traveling wave loads nothing; #526's DC scope is what the dynamics realize. Sector: DC→AC coupling.
- **Outcome C (discovery):** [NEITHER] — the honest 2nd-order response is a law neither arm wrote (e.g. a partial rectification, or a coupling to the longitudinal channel neither slot captured). Report the measured law.
- **Outcome D (null-of-instrument):** [UNRESOLVED] — the numerics can't separate 2%. Named resolutions listed.

**Falsifier of the framing:** if PC-DC-LIVENESS fails (the probe can't even see a held static tension), the whole measurement design is blind — HALT, no bin, redesign the probe.

---

## CONVERGENCE / ROBUSTNESS PLAN (declared pre-run)

- **dt sweep** — halve dt until measured probe stiffness stable to ≪ 2%; report the drift floor.
- **chain-length / window sweep** — lengthen chain + measurement window until SWR ≈ 1 and the measured stiffness is window-independent; report SWR.
- **timescale separation sweep** — sweep Ω/ω_pump and probe-amplitude/pump-amplitude; show the measured stiffness is on the adiabatic small-signal plateau (independent of Ω/ω and probe amplitude in the declared regime).
- Bands, NOT six-digit precision, in the verdict.

---

## LEDGER (canon-forced vs derived vs engineering-choice; all magnitudes banded)

| # | Term | Status | Basis |
|---|---|---|---|
| 1 | Kernel `Φ''(a)=k₀√(1−a²)` | CANON-FORCED | Ax4, `scale_invariant.py:107-156` |
| 2 | Tension `Φ'(A)=k₀(A√(1−A²)+arcsin A)/2` | DERIVED (sympy) | integrate once, 5 exact-zero residuals |
| 3 | Bond length `L=√((a₀+Δu)²+Δy²)` | GEOMETRY (honest) | NOT a slot term; the coupling source |
| 4 | `⟨T⟩=(k_a/ℓ)y₀²` (#529 cycle-avg) | DERIVED (IMPORTED as prediction only) | ⟨sin²⟩=½; used in the PREDICTION module, NOT the dynamics |
| 5 | k₀=ℓ=k_a=k_s=1 (kernel units) | CONVENTION | same as #526/#529/#531 (k₀=1 units into ρ) |
| 6 | Symplectic velocity-Verlet | ENGINEERING (justified) | Hamiltonian, energy-conservation-sensitive average |
| 7 | Gate band = 3× derived residual | DERIVED (post-sweep) | #531 discipline; frozen after convergence sweep, must be < 2.04% |
| 8 | y₀ tent/elastica edges (0.1428, 0.4153) | READ-OFF (#527/#529 in-regime ceiling) | `axiom-register.md:189` arc* band; never tuned |

**0 free parameters tuned toward 2/7 / 9.7734 / 2.04%.** The gate band and y₀ edges are the only knobs; both are read-off/derived, not tuned.

---

## CROSS-REFERENCES (grep-verified at branch HEAD this session)

- Fork record (PR #531): `research/2026-07-05_channel-resolved-loading_result.md` (branch `analysis/channel-discriminator`)
- #526 frozen T-slot scope: `research/2026-07-04_prestress-tensor_prereg_FROZEN.md`:64-78
- #526 result (remap, prestress tensor form): `research/2026-07-04_prestress-tensor_result.md`
- #529 [RADIATION-CONTAMINATED] (⟨T⟩=(k_a/ℓ)y₀² carrier died): `research/2026-07-04_resonant-tension-law_result.md`
- Bond-force sign rule (merged Φ', channel-keyed sign): `research/2026-07-04_bond-force-sign-rule_result.md`
- Kernel: `src/ave/axioms/scale_invariant.py:107-156`; core `src/ave/core/universal_operators.py` `universal_saturation`
- ReconcileGate (#528): `src/ave/validation/reconcile_gate.py`
- Jensen-rectification chain (the physics tension surfaced to Grant): `manuscript/ave-kb/vol4/claim-quality.md:246,:263`
- SPICE lane charter (DC→AC sibling cross-ref): `_orchestration/2026-07-03_spice-lane-charter.md`
- T2 homonym guard: `resonant-lc-solitons.md:95,:128` (A1⊥T2, Grant-ratified 2026-06-14)
