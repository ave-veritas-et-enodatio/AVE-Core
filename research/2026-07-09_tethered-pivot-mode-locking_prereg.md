# Tethered-pivot mode-locking — does a WALL-ANCHORED (2,3) traversal MODE-LOCK where #417's free orbit TRACKED the carrier?

**Status:** **FROZEN PRE-REG.** Frozen BEFORE the driver run. Both Grant gut-checks ruled (2026-07-09).
**Class:** CONSISTENCY (a PASS/LOCK confirms a *derived protection mechanism* — boundary-condition
quantization — for the imported (2,3) SELECTION; it is NOT a novel α-free chord and NOT an emergence
result). Q=137 EMPTY. mass=A1 (#260) UNTOUCHED. The (2,3) SELECTION stays IMPORTED either way.
**Base:** `analysis/x34-tethered-pivot` off main `37eaded5`. Reuses (Rule 14) the #417 harness verbatim +
ONE new ingredient (the clamped coordinate).
**Test id:** x34.

## §0 WHY THIS, WHY NOW — the #417 NEGATIVE this test must RESPECT

`research/2026-06-24_engine-phase-space-winding_result.md` (#417) ran the FREE conservative orbit of the
inter-grade A1↔ω coupling and returned **BREAK**: the phase-space traversal reads the **carrier ratio
(1,1)-class**, and — the load-bearing discriminator — the winding ratio **TRACKS the detuning knob
continuously** (ω_b:ω_s = 1:1→0.93, 2:3→0.65, 3:2→1.54, 1:2→0.48). The kill was *ratio-follows-knob*: a
carrier-set global phase, not a topology-protected charge.

This test differs from #417 by **exactly ONE ingredient: the ANCHOR.** The W5 circuit walk
(`research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md:159`) proposed that a
**wall-anchored** traversal — the poloidal loop terminated on the torus axis — makes BOTH (2,3) integers
**BC-quantized MODE INDICES** (discrete, knobless), so #417's ratio-tracks-detuning kill *structurally
cannot fire* on them. This pre-reg tests that proposal DIRECTLY, in the SAME phase-space read where #417
found tracking.

## §1 GRANT RULINGS APPLIED (recorded per instruction)

- **gut-check (a) — the anchor is THE AXIS.** Node-at-center family; the W4 frozen-flux walk
  (`...walked-framing.md:157`): the pivot is the AXIS (point termination), not the collimator. The anchor
  is implemented as the **equatorial (z≈0) reference plane** of the winding host — the node-plane through
  the torus axis.
- **gut-check (b) — CONFIRMED: #260's "magnetic-vs-capacitive Γ=−1 wall" = WHICH QUADRATURE carries the
  node.** Capacitive wall pins the **V/d-quadrature** (Re(b_ω) node, I-antinode); magnetic wall pins the
  **I/q-quadrature** (Im(b_ω) node). Degenerate energy; the choice = the **μ-sign selector**. Signature 3
  below is therefore the **first direct ENGINE PROBE of the #260 adjudication.**

## §2 SCOPE-LOCK (load-bearing distinctions, inherited from #417 §0)

- **SEED, never FORM.** Seed the already-placed electron (`build_seeded_sim` → `seed_A1_sech` + `seed_winding`
  at the V_yield front) and evolve. No precursor ICs; the barred self-formation slot stays BARRED.
- **BC in the phase dynamics, NOT a drive.** The anchor pins one quadrature's phase at the host boundary; it
  does NOT inject energy. The projection can only REMOVE norm (never add) ⇒ the #417 anti-pumping guard is
  satisfied **by construction** (a lock under an energy-REMOVING wall cannot be a pumped illusion). The clamp
  is a **lossy-Dirichlet Γ=−1 wall** (not strictly conservative); the removed-norm budget is tracked and
  reported (honest energy bookkeeping — this pre-reg does NOT claim strict unitarity for the clamped runs).
- **α-clean / phase-only.** The verdict observable is a pure `arg()` ratio (dimensionless). No Ω/A*-weighting,
  no ALPHA/Q_TANK on the read. κ̃=6/5 host; Q=137 empty. The α-carrier V_yield divides out of any `arg()` ratio.
- **Sector fence (mandatory, per W5 iv + #585).** The rotation number 3/2 ⇒ the anchored traversal closes only
  after 2 toroidal circuits (4π) — this is the TEXTURE's q-odd structure ((−1)^q), **NOT** the spin selection.
  The texture/spin weld stays DEAD (#585). No parity/spin conclusion is drawn — only mode-existence + the
  quadrature-selector (μ-sign) read.
- **Phase-space coordinate discipline (A46).** The corpus claim is a phase-space TRAVERSAL rotation number; the
  read is in matching phase-space coordinates (the Clifford global-phase angles), NOT real-space Cartesian. The
  clamp acts on the field (real-space b_ω) but the VERDICT is read in phase-space, and the CONTROL (clamp off)
  must reproduce #417's phase-space tracking values. Coordinate-consistent by construction.

## §3 THE ANCHOR (frozen — the ONE new ingredient)

The **winding host** = the ω/charge dynamical sector `b_ω` (the rigid_template LC-quadrature amplitude on the
fixed (2,3) template `e_w`; `coupled_cage_winding.py:238,302`). `Re(b_ω)` = the V/C-state (voltage quadrature);
`Im(b_ω)` = the I/L-state (current quadrature) (analytic-signal convention, `coupled_cage_winding.py:428`).

- **Anchor node-set** `M` (frozen): the **equatorial node-plane** of the winding host — tube cells with
  `|z| ≤ z_anchor` (z = k − center), **field-supported** (`|b_ω| > 1e-6`), **PML-excluded interior**. This is
  the axis-anchored / node-at-center family (gut-check a): the z≈0 plane cuts the poloidal loop and is
  anchored on the torus axis. Frozen `z_anchor = 1.0` lattice cell (≈ the poloidal equatorial band). The W5
  "closed toroidal ring" is already supplied by the ring topology + periodic lattice; this ADDS the
  axis-anchored poloidal termination.
- **Capacitive/short branch** (V-node): each step, after the Cayley solve, project `Re(b_ω)[M] ← 0`
  (V-quadrature pinned, I-antinode). = the short/capacitive Γ=−1 wall.
- **Magnetic/open branch** (I-node): each step, project `Im(b_ω)[M] ← 0` (I-quadrature pinned). = the
  magnetic Γ=−1 wall.
- `e_w` (the frozen topological template, real-space (2,3) integer) is **untouched** — the anchor is a BC on
  the phase DYNAMICS, not on the topology.

## §4 THE READ (frozen — reuse #417 verbatim)

- Toroidal `φ(t) = arg(Σ_x a_A1)` (mass sector global phase, "2"); poloidal `ψ(t) = arg(Σ_x b_ω)` (charge
  sector global phase, "3"). The **traversal rotation number** `ρ = (net φ-turns)/(net ψ-turns)`.
- **Two-method read** (F4): unwrap-count AND circulation integral. **F4 caveat HONORED** (from #417): the two
  are the same wrapped-increment estimator (near-zero added assurance). The **load-bearing discriminator is the
  DETUNING RESPONSE of ρ** — exactly as in #417 — not F4 agreement.

## §5 THE THREE FROZEN SIGNATURES (from W5) — no preferred outcome

1. **MODE-LOCKING (the forbidden-knob discriminator).** Under a CONTINUOUS detuning sweep (ω_b=1 fixed,
   ω_s ∈ [0.7, 1.4]) plus the four rational points {1:1, 2:3, 3:2, 1:2}: does the anchored ρ(ω_s) hold
   **rational PLATEAUS and jump DISCRETELY** (LOCK — BC-quantized mode indices, no knob), or **TRACK the knob
   continuously** as #417's free orbit did (TRACK)?
2. **HYSTERESIS at the jumps.** Ramp ω_s up (0.7→1.4) and down (1.4→0.7) carrying state (memory): do the jump
   locations differ (a hysteresis loop, the driven-bounded-resonator fingerprint)? LOCK ⇒ width > 0; TRACK ⇒ 0.
3. **TERMINATION FLIP (the #260 selector probe).** Rerun with the magnetic clamp (pin Im instead of Re): does
   the traversal ORIENTATION INVERT (sign of ρ / the poloidal net-turn sign flips between cap and mag)?
   FLIP ⇒ the #260 μ-sign selector is a live engine observable; NO-FLIP ⇒ the selector does not manifest in
   this temporal-winding read (report the null; do not rescue).

## §6 ANALYTIC EXPECTATIONS (frozen — the menu + the control)

- **CONTROL (clamp OFF) MUST reproduce #417** (else the harness is broken → HALT): ρ(1:1)≈1, ρ(2:3)≈0.65,
  ρ(3:2)≈1.55, ρ(1:2)≈0.48; ρ(ω_s) a CONTINUOUS (smooth) curve tracking ω_b/ω_s.
- **LOCK menu (if the pivot picture holds):** ρ holds plateaus on the small-denominator mode-index rationals
  {1:1, 1:2, 2:1, 2:3, 3:2, 1:3, 3:1}, with discrete jumps, hysteresis, and a cap↔mag orientation flip.
- **TRACK (if the pivot picture fails):** ρ_anchored(ω_s) ≈ ρ_free(ω_s), continuous, no plateaus/jumps/flip
  → the anchored ratio STILL follows the knob → the pivot picture dies, banked next to #417.

**Lock-detector (frozen):** over the fine sweep, `staircase_fraction` = fraction of adjacent sweep intervals
with `|Δρ| < 0.03` (flat); `jump_count` = intervals with `|Δρ| > 0.15`; `track_R2` = R² of ρ_anchored vs
ρ_free. **LOCK** ⇔ `staircase_fraction ≥ 0.5` AND `jump_count ≥ 1`. **TRACK** ⇔ `track_R2 ≥ 0.9` AND
`staircase_fraction < 0.2`. Anything else = PARTIAL (report per-signature). Genuinely unresolved (Nyquist /
gauge-degenerate clamp) = INCONCLUSIVE.

## §7 GATES (frozen)

- **validate-on-known:** (i) a PLANTED LOCKED rotation-number staircase must read `staircase_fraction≥0.5`,
  `jump_count≥1` (LOCK); (ii) a PLANTED TRACKING (linear) rotation number must read `track_R2≥0.9`,
  `staircase_fraction<0.2` (TRACK). If the detector can't separate the two synthetic controls, it is broken →
  HALT.
- **dead-actuator:** the pinned quadrature's variance over `M` must COLLAPSE vs unclamped:
  `var_clamped / var_unclamped < 0.05` (the clamp demonstrably constrains). A clamp that does not collapse the
  variance is a dead actuator → INCONCLUSIVE (no verdict on a dead clamp).
- **energy ledger:** clamp OFF conserves joint norm to #417 standard (`<1e-6`); clamp ON is monotone-non-pumping
  (`max_t E(t) ≤ E(0)·(1+1e-9)`) with the removed-norm budget reported. A clamp that PUMPS (E grows) → the
  guard is violated → INCONCLUSIVE (a pumped lock is an artifact, per #417 §0).
- **two-method winding read** with the F4 caveat honored (§4).

## §8 BRANCHES (no preferred outcome — substrate adjudicates)

- **LOCK** (all 3 signatures): the (2,3) gains a DERIVED protection mechanism (BC quantization). **The SELECTION
  stays IMPORTED** (FORM/VALUE scoping verbatim: the *form* — that a bounded traversal quantizes — would be
  derived; the *value* (2,3) is still adopted-by-geometry, NOT emerged). Spin-weld stays dead (#585); sector
  fence holds. Register note: the #260 selector is a live engine observable.
- **TRACK** (anchored ρ follows the knob): the pivot picture DIES; banked next to #417. The carrier-set
  global-phase mechanism is ROBUST to anchoring.
- **PARTIAL** (lock without flip / flip without lock / etc.): report per-signature, name what held and what
  did not.
- **INCONCLUSIVE** (Rule 11): clamp gauge-degenerate (dead-actuator gate fails), clamp pumps (energy gate
  fails), or Nyquist-unresolved. Report; re-scope; NO rescue.

## §9 BUILDABILITY / REUSE (Rule 14)

Reuse verbatim: `coupled_cage_winding.CoupledCageWinding.step()` (conservative unitary evolver), `build_seeded_sim`
+ `seed_A1_sech`/`seed_winding` (the electron seed), the #417 `_sector_phase`/`_cross_phase`/`_net_turns_*` reads,
the two-method winding reader, the energy gate, the validate-on-known scaffold. NEW: the anchor projection
(`_apply_clamp`), the detuning-sweep rotation-number map, the lock-detector, the hysteresis ramp, the
termination-flip comparison, the dead-actuator gate. No new engine. The dynamical runs are `engine_sim`
(off the PR-blocking gate per the #414 partition).

## §10 HOST-STENCIL CAVEAT (inherited from #417 evidentiary-exposure sweep)

The evolver builds on the native diamond `TETRA_OFFSETS` stencil (achiral z=4). This is a chiral-(2,3) template
on an achiral host — the SAME caveat as #417 (`..._result.md:162-166`); an srs-native re-run is separately
queued. The load-bearing discriminator here (does ρ track or lock under detuning) is carrier/BC-based and
stencil-chirality-independent, as it was in #417. No parity conclusion is drawn (sector fence, §2).
