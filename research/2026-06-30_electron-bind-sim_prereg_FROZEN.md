# PRE-REG (FROZEN) — Electron self-braced BIND: MEASURE the deep-core pull slope `p`

**Date:** 2026-06-30 · **Lane:** implementer · **Branch:** `analysis/electron-bind-sim`
(worktree `/private/tmp/electron-bind-sim`, off `main` @ `e1e14572` — the MERGE of PR #441).
**Type:** SIMULATION (time-domain force-balance measurement). This is the CONFIRMATION sim the
merged port-map derivation (`research/2026-06-30_electron-portmap-derivation_result.md` §7.3) named:
it MEASURES the slopes the symbolic derivation predicted, to CONFIRM or REFUTE the BIND verdict.

**Freeze-before-run:** this prereg is committed as the FIRST commit of the branch; the SHA-pin below is
filled at commit time and the adjudication criteria (§ADJUDICATION) are frozen BEFORE any driver line
is written. Per Rule 11 no criterion is dropped/weakened post-hoc to convert a NO-BIND verdict into a
BIND verdict. Per A47 v11b no new hypothesis refills a NO-BIND slot.

**SHA-pin (this file, frozen commit):** `f678b0fc` — the driver + result are built AFTER this
commit and cite it. (This edit adds only the pin; the frozen adjudication criteria in §ADJUDICATION
are unchanged from `f678b0fc`.)

**Upstream derivation this sim CONFIRMS (SHA-pinned, verify-before-cite):**
- merged @ `e1e14572` (PR #441). Derivation result: `research/2026-06-30_electron-portmap-derivation_result.md`
  (frozen prereg `a6c03c72`). KB leaf: `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md`.
- The derivation reduced the electron's binding to ONE measurable inequality (result §5.1):
  ```
  STABLE   ⇔  p < 3     (pull SHALLOWER than the r^{−3} brace)
  UNSTABLE ⇔  p > 3     (pull STEEPER — out-runs the brace)
  MARGINAL ⇔  p = 3
  ```
  with `sign(dF_net/dr|_{r*}) = sign(3 − p)`, `P(r)=c_P r^{−p}`, `B(r)=c_B r^{−3}`.
- Under Grant's `def-vyvsn1 = T2` ruling (2026-06-30, landed in KB) the A1 mass core operates
  SUB-SATURATED at `A = V_YIELD/V_SNAP = √α ≈ 0.0854` (`S(√α)=√(1−α)≈0.996`), where the symbolic
  reading predicts `p ∈ [1,2] ≪ 3` → BINDS. **THIS SIM MEASURES the actual `p`** to confirm or refute.

---

## SECTOR HEADER (stated before any standard-physics word)

- **MODE:** standing electron — **EXISTENCE**, not genesis, not the static eigenstate. We ask whether
  the radial force balance of a PRE-EXISTING winding + A1 core is a stable well. The self-formation slot
  is twice-falsified and stays BARRED (A47 v11b); the static eigensolve slot read DOES-NOT-EXIST
  (#415/#417) and is NOT re-entered — this is the time-domain FORCE-BALANCE, a different operator question.
- **REGIME:** A1 mass core SUB-SATURATED at `A=√α` (T2 wall at `V_yield`; A1 rail at `V_snap=V_yield/√α`,
  11.7× higher). `S(√α)=0.996` — Regime I. The `S→0` deep-saturation runaway (Regime II) is a real
  feature of the A1 varactor but the mass core NEVER reaches it. Op14 saturation nonlinearity is LIVE
  (not linearized) but small at this operating point.
- **PHASE-STATE:** a lossless REACTIVE self-braced balance. The (2,3) winding runs an AC circulation
  (→ rectified ponderomotive DC compression = the inward pull) AND carries a DC circulation `∝ r^{−3}`
  (= the outward brace). We ask whether the DC brace out-steepens the rectified pull.
- **SECTORS in the loop:** A1 dilatation = MASS = capacitive varactor `C_eff=C_0/S` (`Z_bulk`).
  (2,3) Cosserat winding = CHARGE = inductive, DC circulation + AC ring (`Z_shear`). Γ=−1 T2 wall =
  reflective termination (a BOUNDARY condition, NOT a bulk force — CP10). A1 ⊥ T2 (never cross-wired).

**Guard against SM/QED leak (substrate-native-walk recorded in §SUBSTRATE-WALK below):** no
Lagrangian-minimization, no gradient-descent-on-energy-basin, no continuum-Helmholtz eigensolve. The
equilibrium is a REACTIVE PRESSURE balance read off DYNAMICALLY-EVOLVED fields at the self-set
`A=√α` operating point. Ports native Cosserat (A1/μ), NOT Cartesian stencils. The (2,3) winding lives
in its PHASE-SPACE home (the Link integer on the frozen ê_w template, conserved by construction), NOT a
real-space geometric torus.

---

## THE PICTURE BEING TESTED (stated so it can FAIL)

The pre-existing (2,3) winding + A1 core at `A=√α` produces:
1. an inward ponderomotive PULL `P(r)` (the rectified varactor DC compression, derivation §2), and
2. an outward reactive BRACE `B(r) ∝ r^{−3}` (the conserved DC circulation's centrifugal pressure, §3.1).

**BINDS** iff the brace out-steepens the pull at the crossing — formally `p<3` and `dF_net/dr|_{r*}>0`.
**FALSIFIABLE at three points** (honest NEGATIVE, not debugged toward a rescue):
- (i) the measured pull slope could come out `p > 3` (deep-core runaway fires even at `A=√α`) →
  IMPLOSION → **NO-BIND**, a legitimate honest negative;
- (ii) `dF_net/dr < 0` at the crossing → UNSTABLE equilibrium → NO-BIND;
- (iii) the winding circulation `L_w` could FAIL to conserve (unwinds under evolution) → the brace is not
  the claimed conserved-circulation reactive pressure → the picture's brace leg is absent.

**Prior odds held AGAINST easy binding (verify-before-cite):** the static coupled eigensolve read
DOES-NOT-EXIST (#415/#417); the S3 real-space coupled PDE (this exact solver family) read
DISPERSE-FALSIFIED for the PINNING question; the #83 "stabilized loop" was a RETRACTED artifact
(damping-bought localization, Ax3 violation). Binding does NOT fall out easily; a NO-BIND result here
is a real live outcome.

---

## SUBSTRATE-NATIVE WALK (recorded BEFORE the driver — substrate-native-check + phase-space-coordinate-check)

- **CP1 (dynamics):** time-domain wave propagation via the UNITARY Crank–Nicolson step on the K4-native
  `L_D` stencil (`CoupledCageWinding.step()`) — NOT energy-minimization / gradient-descent / Helmholtz.
  Equilibrium = a reactive PRESSURE balance read off evolved fields, not a basin minimum.
- **CP2 (sector):** cross-coupled A1 (bulk/mass, capacitive) ↔ ω-winding (shear/charge, inductive);
  Op14 saturation active but sub-saturated at `A=√α`.
- **CP3 (objective):** reactive pressure balance / ponderomotive potential gradient — NOT a Lagrangian
  eigenvalue. Pull = `−∂⟨U_pond⟩/∂r`; brace = centrifugal `L_w²/(m r³)`.
- **CP4 (coordinate discipline — the A46 hazard, explicitly cleared):** the (2,3) winding TOPOLOGY
  (Link integer) lives in PHASE-SPACE and is carried by the FROZEN ê_w template (conserved by
  construction — the correct home; I do NOT evolve it as a real-space geometric torus, do NOT extract an
  `R_phase/r_phase=φ²` claim). The derivation's `p`-slope and `r^{−3}` brace are EXPLICITLY real-space
  RADIAL scalings (result §3.4, §5). So measuring `P(r)`, `B(r)` as radial profiles of the evolved
  fields IS the corpus-claim-matching coordinate — this is a real-space radial FORCE scaling the
  derivation itself poses in real-space `r`, NOT a real-space measurement compared to a phase-space φ²
  prediction. Coordinate-matched. ✓
- **CP5 (local clock):** `ω_local(r)=ω_global·√(1−A²(r))` applied (Op14 active). At `A=√α`, `S≈0.996`
  ⇒ modulation ≈0.2% — recorded, small.
- **CP6 (reactance pair):** record BOTH the C-state (`|b_ω|`, the winding AC/DC amplitude) AND the
  L-state (`Im(b_ω)`, `ω_dot`) over the recording window (`omega_field()` C-state, `omega_momentum()`
  L-state). A one-phase snapshot cannot distinguish the static brace from the oscillator at peak.
- **CP7 (sampling):** PML-excluded interior mask (`pml_thickness ≤ {i,j,k} ≤ N−pml−1`) BEFORE any
  top-K extraction; sample at energy-density top-K `|field|²` PEAKS, NOT the shell centroid.
- **CP8 (NOT a hosting test):** TRAP-not-CREATE. The winding pre-exists (seeded, conserved by
  construction). We measure the force balance on the pre-existing configuration; we do NOT ask the engine
  to BUILD the electron (the barred genesis slot). This is the EXISTENCE question.
- **CP9 (heuristic vs dynamical):** the fields `a_A1, b_ω` ARE dynamically evolved by `step()`. The
  rectified softening `⟨S⟩` that sets the pull is driven by the ACTUAL AC swing of the evolved `b_ω`
  (measured `δA` from the reactance-pair trace), NOT a plugged-in `δA` formula. `P(r)`, `B(r)` are
  observer reads of dynamically-evolved fields (the corpus-canonical pressure-balance methodology,
  Fork-A #419). Stated: observer reads of DYNAMICAL fields.
- **CP10 (boundary not bulk — the load-bearing guard):** the pull is the gradient of the BOUNDED
  ponderomotive energy `U_C=½Q²S(A)/C_0` (`S∈[S_min,1]`; at `A=√α`, `S≈0.996`, far from the wall) —
  it is NOT the singular `dS/dA→∞` bulk force at `A→1` (which only detonates in the Regime-II core the
  electron never reaches). The Γ=−1 confinement wall stays a BOUNDARY condition; it is NOT added as a
  bulk force. ✓

---

## THE MEASUREMENT (the deliverable)

Seed a PRE-EXISTING standing (2,3) winding + A1 core at operating point `A=√α`. Evolve the coupled
A1+winding dynamics (time-domain, `CoupledCageWinding` — the UNITARY, lossless, winding-conserving
solver; NOT the static eigensolve). Over a recording window, measure the radial force balance:

1. **DEEP-CORE PULL SLOPE `p`** — fit the ponderomotive pull `P(r) ∝ r^{−p}` over the interior radial
   shells at the peak-density sites. **PASS iff `p < 3`.**
2. **BRACE SLOPE** — confirm `B(r) ∝ r^{−3}` from the conserved DC circulation (measure the exponent;
   expect −3 ± tolerance).
3. **STABILITY `dF_net/dr` at equilibrium** — with `F_net=P−B`, evaluate the sign at the crossing `r*`.
   **PASS iff `dF_net/dr > 0`** (restoring → stable well). Consistency check vs the analytic
   `sign(3−p)`.
4. **α-ROBUSTNESS SWEEP (the keystone test)** — vary `α` across a range (so the operating point `A=√α`
   slides); confirm the electron stays bound WITH MARGIN (`p<3`, `dF/dr>0`) across small-`α`, i.e. `α`
   only SLIDES the operating point, it does NOT sit on the `p=3` knife-edge. Earns "keystone, not
   fine-tune" iff `p` stays comfortably `<3` (margin `3−p` bounded away from 0) across the sweep.
5. **`L_w` (circulation quantum)** — MEASURE it (both the hypothesis `L_w` = the (2,3) `Link=−1`
   topological circulation, AND the measured value); it sets the equilibrium SIZE `r*~ℓ_node`, NOT the
   stability.

**Measurement discipline (from derivation §7.3 — load-bearing; a naive read gives a false slope):**
- REACTANCE-PAIR tracking (C-state AND L-state) over the window.
- ENERGY-DENSITY-PEAK sampling (top-K `|field|²`), NOT centroid.
- PML-cell filter BEFORE top-K extraction.
- LOCAL-CLOCK `ω_local(r)=ω_global·√(1−A²(r))`.
- Tellegen-LOSSLESS: NO dissipative term anywhere. If damping is needed to stabilize, that is a FAIL,
  not a fix (the #83 `e^{−ηM}` viscosity crutch is exactly what Ax3 forbids). Energy conservation
  `|dH/H|` reported as the losslessness certificate.
- RESOLUTION-ROBUSTNESS: re-confirm the slope verdict at ≥2 grid resolutions before banking.

---

## ADJUDICATION CRITERIA (FROZEN — locked before running)

Let `P(r)` = inward pull magnitude, `B(r)` = outward brace magnitude, `F_net = P − B`, at radius `r`,
read from the PML-excluded interior at density-peak sites, with the reactance pair tracked.

**BINDS-CONFIRMED** (the derivation's BIND verdict is CONFIRMED by measurement) **iff ALL:**
- (C1) measured deep-core pull slope `p < 3` at `A=√α` (with a resolution-robust fit, ≥2 grids), AND
- (C2) measured brace slope consistent with `r^{−3}` (exponent −3 within tolerance), AND
- (C3) `dF_net/dr > 0` at the crossing `r*` (stable/restoring; sign consistent with `sign(3−p)>0`), AND
- (C4) losslessness holds: `|dH/H|` at solver tolerance over the window (NO dissipative term), AND
- (C5) α-robustness: `p<3` with margin (`3−p` bounded away from 0) across the small-α sweep — the BIND
  is NOT a `p=3` knife-edge; `α` only slides the operating point.

**NO-BIND** (HONEST NEGATIVE — the self-braced electron does not bind) **if ANY:**
- (N1) measured `p > 3` at `A=√α` (the deep-core runaway fires even sub-saturated) → IMPLOSION, OR
- (N2) `∄` finite crossing `r*` (brace-too-weak → runaway compression; brace-dominates-everywhere →
  dispersion), OR
- (N3) `dF_net/dr < 0` at `r*` (UNSTABLE equilibrium), OR
- (N4) the winding circulation `L_w` FAILS to conserve (unwinds under lossless evolution) → the claimed
  conserved-circulation brace is absent, OR
- (N5) a dissipative term is REQUIRED to stabilize (`|dH/H|` not at tolerance without damping) —
  DISQUALIFIED as the #83 forbidden crutch.

**INCONCLUSIVE** (resolution-limited) if the slope verdict does NOT hold across the ≥2 resolutions
(the `p<3` vs `p>3` verdict FLIPS with grid), OR the fit `R²` / dynamic range is too poor to place `p`
relative to 3 — reported as resolution-limited, NOT forced to a verdict.

**Anti-rescue guards (frozen):**
- No dissipative brace may be introduced to force a balance (#83 lesson; N5).
- No new hypothesis refills a NO-BIND slot (A47 v11b substitution-not-retraction).
- If all failure paths point to one mechanism, that is Rule-11 honest closure — name it, close it.
- The α-robustness verdict is NOT dropped post-hoc if it fails; a knife-edge (`p→3` as α→0) is a
  FINE-TUNE finding, reported as such (weakens "keystone").
- `m_e`, α, `A=√α` VALUES are calibrated/imported/echo; only the FORM (the measured slopes + the
  stability sign) is the sim's deliverable. NO number-emergence claim.

---

## CLASSIFICATION (consistency-vs-emergence — pre-committed)

**Class C — CONSISTENCY / FORM-chord throughout.** The mechanism (a reactive brace out-steepening the
rectified pull) is at best a FORM-chord: it gives the SM-absent mechanism for a stable localized electron
mass, but every dimensionful anchor is imported/echo — the operating point `A=√α` is an EXACT α-echo
(`V_yield=√α·V_snap`, `constants.py:464`), `m_e` is definitional, the size `r*~L_NODE=ℏ/(m_e c)` carries
`m_e`, and `R·r=¼` is a Class-B input. There is NO Class-D emergence here (no dimensionless observable
computed free of the target). The α-robustness sweep varies α as a KNOB to test knife-edge-vs-keystone;
it does NOT compute α. A BINDS-CONFIRMED verdict is a Class-C FORM-chord confirmation; a NO-BIND verdict
is a Class-C consistency negative with a named mechanism. Either way, NOT emergence (A47 v17 family).

---

## DELIVERABLE

`research/2026-06-30_electron-bind-sim_result.md`: the measured pull slope `p`, the brace slope,
`dF_net/dr` sign, the α-robustness sweep, `L_w`, all with the reactance-pair / density-peak / PML /
local-clock / lossless discipline applied and resolution-robust (≥2 grids). VERDICT:
BINDS-CONFIRMED vs NO-BIND vs INCONCLUSIVE, with honest solidity + open items. NO KB/manuscript edits
(research/ only). Incremental commits (prereg → driver → sweep → result). Push branch, STOP
(orchestrator opens the PR after independent verify).

---

## PHYSICS QUESTION SURFACED TO GRANT (flag-don't-fix — NON-BLOCKING, does not gate the sim)

**Q (plumber-physical): how is the DC circulation `L_w` set on the rigid_template winding, and does the
sim's `L_w` conservation actually exercise the brace, or only certify the topological Link?**

The `CoupledCageWinding` rigid_template carries the (2,3) Link integer in the FROZEN ê_w template
(conserved by CONSTRUCTION), and the dynamical `b_ω` amplitude carries the LC energy. The brace of the
derivation is the DC circulation's centrifugal reactive pressure `L_w²/(m r³)`. In this solver the loop
RADIUS `r` does not dynamically shrink (the template geometry R,r is fixed at seed), so the sim measures
the brace's `r`-SCALING by reading the circulation reactive pressure across a RADIAL PROFILE at fixed
time (the shells at different `r` in the seeded configuration), NOT by dynamically compressing the loop.
This is legitimate for measuring the `r^{−3}` FORM (the scaling is a spatial-profile property of a
conserved circulation), but it is a PROFILE read, not a compression trajectory. Flagged so Grant can
rule whether a compression-trajectory brace measurement is required before banking C2/C3, or whether the
profile read + the derivation's analytic `L²/2I` argument suffices for the FORM-confirmation this sim
scopes. Does NOT block: the sim proceeds with the profile read and reports the distinction explicitly.
