# FROZEN PREREG — the Cleave registry-pump Chern number: sliding vs locked

**Date:** 2026-07-02
**Lane:** implementer (dual-reading Chern driver)
**Branch:** `analysis/cleave-coupling-chern-adjudication` (off main `f556dcdc`)
**Disciplines fired:** `ave-prereg`, `ave-canonical-source`, `substrate-native-check`,
`phase-space-coordinate-check`, `consistency-vs-emergence`, `verify-before-cite`
**Status at freeze:** predictions, gates, outcome bins, and slope arithmetic locked BEFORE any
Chern number is computed. Receipts: `research/2026-07-02_cleave-coupling-derivation_adjudication.md`.

> **SHA-PIN.** This file is frozen at commit time and committed BEFORE the driver
> `src/scripts/vol_4_engineering/cleave_registry_pump_chern.py`. Any change to a setup, a gate,
> an outcome bin, or the slope arithmetic AFTER any C is known is a Rule-16 violation and must be
> a NEW prereg with its own version, not an edit here.

---

## 0. What Grant ruled (2026-07-02) — the frame

Grant ruled **option (b)**: run BOTH substrate readings (sliding/Eulerian and locked/Lagrangian);
whichever setup reproduces the KNOWN ANCHOR — the OA loop holonomy **±0.256776 rad** / bulk
**g₀ = 2.21589 rad per lattice-z-unit** (`research/2026-06-23_chiral-vector-tlm-phase1_result.md:23,65`)
— earns the canon slot. **Doc-109 (sliding-vs-locked) is adjudicated by the engine, not by fiat.**

The question the driver answers: *does the readout boundary loop `∂Ω`, swept adiabatically through
the srs chiral ground state, accumulate a nonzero integer `C·e` of `Link(∂Ω, F)` per registry
period — and in which substrate reading?*

### Substrate-native-check (fired BEFORE the numerical design)

- **K4 / Cosserat / Op14 checkpoints.** The carrier is the chiral **srs** net (I4₁32, the free-mode
  carrier — `chiral_lattice_dynamics`); the pump reads the **T2 Cosserat micro-rotation** channel
  (charge = boundary linking `Link(∂Ω, F) ∈ ℤ`, `boundary-observables-m-q-j.md:20`), NOT the A1
  dilatation-mass "3." No A1 cross-wiring — the pump is a winding/linking effect, sector-orthogonal
  to mass.
- **Phase-space-vs-real-space (A46 / phase-space-coordinate-check).** The Chern number is computed
  in the **`(k_z, θ)` registry-torus phase space** — `k_z` a Bloch momentum, `θ` the registry pump
  phase. This is a phase-space invariant by construction; it is NOT a real-space lattice-Cartesian
  measurement compared to a phase-space prediction. The OA anchor (holonomy / g₀) is *also* a
  phase/holonomy quantity (rad per z-unit), so the anchor cross-check is coordinate-matched: a
  phase invariant compared to a phase anchor. No φ²-in-phase-space vs Cartesian-lattice mismatch.
- **No SM/QED default leaked in.** No Lagrangian minimization, no gradient-descent energy basin —
  the pump is an adiabatic spectral-flow invariant (Berry curvature integral over a closed torus),
  the substrate-native reading of the Thouless charge pump.

### consistency-vs-emergence (frozen tag)

The mechanism CLASS (registry pump) and the FORMS it forces are **adjudication / consistency-class**.
The *value* 414.9 fC/µm is a VALUE-import through the ξ_topo unit-bridge (CODATA-derived through
`ℓ_node = ℏ/m_e c`); it is NOT an emergence-class chord. A nonzero C is an **existence** result (the
mechanism is real), not an emergence-of-the-value result. On any PASS we tag it consistency-class; we
do NOT headline the slope value as emergence.

---

## 1. The two setups (concrete)

Both setups share the frozen srs chiral ground state (`chiral_lattice_dynamics.find_screw_operator` /
`screw_orbit_helix`, enantiomorph ∈ {R, L}) and the same readout `Link(∂Ω, F)` machinery
(`ave.topological.charge_quantization.compute_Q_link` / `compute_F_curl`). They differ ONLY in how
the registry parameter θ couples to plate displacement.

### 1a. SLIDING / Eulerian (canonical engine)

- The screw texture is **fixed in the substrate frame**. The plate's saturation boundary slides
  over it; matter drags NO substrate texture.
- The boundary registry parameter **θ advances with plate displacement** as an external phase
  applied to the readout loop `∂Ω` — the loop moves relative to a static texture.
- Chern integrand: Berry curvature of the occupied band over `(k_z, θ)`, θ = the loop's registry
  phase relative to the fixed screw field, `θ = g₀·x` (mod 2π).
- **Prediction under the sliding reading (from Angles B/C):** if the screw is pure transport
  holonomy with zero net ground-state flux to link, `C_slide = 0` (null). This is the reading that
  Angles B and C argue for.

### 1b. LOCKED / Lagrangian (finite-strain co-moving texture)

- The screw texture **co-moves** with the plate: a finite-strain Lagrangian displacement field
  advects the srs texture, so plate motion carries substrate winding with it.
- The registry parameter θ is the **co-moving strain phase** — displacement transduced through the
  screw into a texture rotation that threads the readout loop.
- Chern integrand: Berry curvature over `(k_z, θ)`, θ = the co-moving finite-strain phase.
- **Prediction under the locked reading (from Angle A):** if the co-moving texture is a genuine
  linkable ground-state field, `C_lock ≠ 0` (a nonzero-Chern pump).

> **Honesty clause (pre-committed).** If the LOCKED setup proves **ill-defined at implementation**
> (e.g. the finite-strain advection has no well-posed adiabatic loop, or the co-moving texture is
> not gauge-closable over the torus), that is a **DOCUMENTED OUTCOME**, not a failure to hide. It
> is reported as "locked reading ill-defined: [concrete reason]," and the sliding reading + toy gate
> still stand as the landed result (deliverable 4's fallback path). We do NOT paper over an
> ill-posed locked setup by forcing a number.

---

## 2. Validate-on-known gate (MUST pass before any srs verdict counts)

**The Chern machinery must first reproduce a known quantized pump in the SAME run.** Toy: a
**Rice-Mele / Thouless charge pump** — a 1D two-band model whose occupied-band Chern number over its
`(k, φ)` pump torus is a known integer **C = ±1** (sign set by the pump direction). The driver
computes C on this toy with the identical Berry-curvature / Fukui-Hatsugai plaquette integration it
uses on the srs ground state.

- **GATE-TOY-PASS:** the toy Chern number rounds to **±1** (|C_toy − round(C_toy)| < 0.1) AND flips
  sign when the pump direction reverses. **If GATE-TOY fails, the run is INCONCLUSIVE** (the machinery
  is not trustworthy) and NO srs verdict is reported — the srs numbers are printed but explicitly
  marked "machinery-unvalidated, not adjudicated."
- Rationale: a Chern integrator that cannot reproduce C=±1 on a textbook pump cannot be trusted to
  report C=0 (a false null) or C≠0 (a false positive) on the srs torus. This is the
  substrate-native "validate-on-known first" gate.

---

## 3. Anchor cross-check (the canon-slot decider — Grant's (b))

Independently of the Chern number, each setup must be checked against the KNOWN OA anchor:
- **Bulk g₀ = ∓2.21589 rad / lattice-z-unit** (srs-R / srs-L), enantiomorph-odd, L-independent
  (`chiral-vector-tlm-phase1_result.md:23,65`).
- **Loop holonomy = ±0.256776 rad** (GATE-1, `:23`).

The driver recomputes the screw-pitch holonomy from the SAME frozen srs ground state each setup uses
(via `screw_orbit_helix` + the bishop-transport rotation already in `chiral_lattice_dynamics`), and
checks it reproduces g₀ = 2.21589 rad/z-unit to the published 0.25% AND the enantiomorph sign flip.
- **ANCHOR-PASS** (for a setup): that setup's screw-holonomy matches g₀ within 0.25% and flips sign
  R↔L. **A setup that does NOT reproduce the anchor cannot earn the canon slot** even if its C≠0.

---

## 4. FROZEN outcome bins (no post-hoc edits)

Computed per enantiomorph; `C` = the occupied-band Chern number over `(k_z, θ)`.

| bin | condition | verdict |
|---|---|---|
| **NULL-DERIVED** | `C_slide = 0 ∧ C_lock = 0` (both integer-round to 0), toy gate PASS | Coupling is **dead**. Cleave rescopes to an **Axiom-2 null-test** (still worth running as a falsifier — a nonzero floor would then falsify AVE). The `Q = ξ_topo·x` mechanism is retired to unit-bridge status; the floor is not a derived pump. |
| **CANON-CANDIDATE** | `C ≠ 0` in **exactly one** reading, toy gate PASS | That reading is the **canon candidate IFF it ALSO reproduces the OA anchor** (§3). The other reading **closes** (documented as C=0 or ill-defined). Slope = `C·e/period` (§5). |
| **BOTH-NONZERO** | `C ≠ 0` in **both** readings | The **anchor cross-check adjudicates** which reading is canonical (§3); the **period fork** (a_cell vs p) settles from the computed pump quantum (which period the integer-per-period corresponds to). |
| **INCONCLUSIVE** | toy gate FAIL, OR non-convergence (C not integer-round within 0.1, or plaquette sum not stable under grid refinement) | No verdict. Report the numbers with an explicit "machinery-unvalidated / non-converged" tag; name the concrete blocker. |

**Enantiomorph-odd requirement (frozen).** For any bin reporting `C ≠ 0`: **C must flip sign
between srs-R and srs-L.** A same-sign C across enantiomorphs is a **RED FLAG** (a genuine chiral
pump is enantiomorph-odd, like the g₀ anchor). A same-sign nonzero C downgrades the result to
INCONCLUSIVE (numerical artifact suspected) regardless of magnitude.

---

## 5. Dimensional evaluation of the expected slopes (FROZEN, from canonical constants)

All from `ave.core.constants` (imported, never hard-coded). `ξ_topo = e/ℓ_node ≈ 4.149×10⁻⁷ C/m`;
`a_cell = 2√2·ℓ_node` (full srs cell); `p = t_z·a_cell = (1/4)·2√2·ℓ_node = (√2/2)·ℓ_node`
(quarter screw-pitch, t_z = 1/4).

- **Full-cell period (Angle A):** `slope = C·e/a_cell = C·ξ_topo/(2√2) = C × 146.7 fC/µm`.
- **Quarter-pitch period (Angle C):** `slope = C·e/p = C·√2·ξ_topo = C × 586.8 fC/µm`.
- **Bench value:** `ξ_topo = e/ℓ_node = 414.9 fC/µm`. This requires period = `ℓ_node`, i.e.
  `C = 2√2` (full-cell) or `C = 1/√2` (quarter-pitch) — **both non-integer, impossible for a Chern
  pump.** The bench's exact 414.9 is NOT reachable by any integer-C registry pump. (This is the G7
  FAIL, pre-frozen: whatever C comes out, 414.9 is not the derived slope; the derived slope is
  `C × {146.7 | 586.8}` fC/µm.)

The driver PRINTS all three (146.7, 586.8, 414.9) side-by-side with the computed C so the period
fork is settled in-run by which period the integer-per-period pump quantum matches. Resolving the
FLAG-1 `2√2` conversion ambiguity (`chiral-vector-tlm-phase1_result.md:105`) is a by-product: the
same z-unit ↔ physical-length convention sets both g₀'s rad/m and the pump's C·e/period; if the
in-run dimensional chain settles it within the run, we document the resolution; if not, we document
it as still-OPEN.

---

## 6. Coordinate + honesty discipline (frozen)

- **phase-space-coordinate-check:** the Chern number lives on the `(k_z, θ)` torus (phase space); the
  anchor g₀ is a holonomy (rad/z-unit, phase). Both invariants are phase-space quantities — matched
  coordinates. The bench slope (fC/µm, real-space) is derived FROM the phase invariant × the
  substrate-native period (`a_cell` or `p`), a physical length — the phase→real bridge is explicit,
  not a coordinate-mismatched comparison.
- **ave-driver-script-honesty:** EVERY printed number is computed in-run. No number is hard-coded;
  ξ_topo, ℓ_node, a_cell, g₀-target all come from `ave.core.constants` or are computed from the
  frozen ground state. The toy Chern, the srs Chern, and the anchor holonomy are all live computes.
- **Route heavy eigensolves to the engine_sim CI lane** (the srs `(k_z, θ)` band eigensolves) via the
  conftest `_ENGINE_SIM_FILES` partition; keep the fast toy-gate + dimensional checks in the gating
  lane. Follow the #411/#414 routing pattern.

---

## 7. What would make this WRONG (pre-committed failure modes)

- A bin edited after C is known to convert a NULL to a CANON-CANDIDATE → Rule-16 violation (§SHA-PIN).
- Toy gate skipped or its threshold loosened after seeing a non-integer srs C → validate-on-known
  violation (§2 is frozen at |C_toy − ±1| < 0.1).
- A same-sign C across enantiomorphs reported as a real pump → enantiomorph-odd guard (§4).
- The locked setup forced to emit a number when it is actually ill-posed → honesty clause (§1b).
- 414.9 fC/µm reverse-engineered as "the derived slope" → §5 pre-freezes that 414.9 is NOT
  integer-C-reachable; the derived slope is C × {146.7 | 586.8}.
- A number hard-coded instead of imported from `ave.core.constants` → driver-honesty violation (§6).

---

## 8. Deliverable

`research/2026-07-02_cleave-registry-pump-chern_result.md`: the toy Chern (validate-on-known gate
pass/fail), the srs `(k_z, θ)` Chern number per setup (sliding, locked) per enantiomorph (R, L), the
anchor cross-check per setup, the settled outcome bin, the derived slope `C × {146.7 | 586.8}` fC/µm,
and the enantiomorph-odd check. Honest solidity, consistency-class. If runtime is prohibitive: land
the toy gate + sliding reading and document the locked reading honestly (blocked/deferred + the
concrete blocker). NO KB/manuscript physics rewrites in the result doc (research/ + minimal
KEEP-BOTH cross-refs only).
