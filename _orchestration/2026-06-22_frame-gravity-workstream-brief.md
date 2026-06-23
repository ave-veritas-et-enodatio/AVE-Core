# Lab-frame + gravity experimental-prediction layer — workstream brief

**Status:** DRAFT, landed for tracking. **Queue position: 2nd** — after `waem9tk6r` (single-scale unification) lands/reviews; fires before the echo-reanalysis. Phase 0 is the substrate-first gate and the most load-bearing physics in the queue.

**Origin:** Grant (2026-06-22), on the K4 dispersion result: *"did we factor in our universe's spin, galaxy's spin, solar-system spin, our spin, the moons? can we do a gravity sensitivity sweep?"* The K4 eigensolve computed the dispersion in the **substrate's own rest frame** — no Earth/orbit/solar/galactic/cosmic motion, no gravity. No instrument sits in that frame.

## Purpose

Build the reusable layer that maps any substrate-frame AVE-distinct prediction (the (q·ℓ)⁴ anisotropy, the birefringence coefficient, any cutoff signature) → the **lab observable** + its sidereal/annual/boost/gravitational modulation + a sensitivity sweep. This is the "fully model any bench" piece of the testing pivot — built once, used by every bench (Cleave, birefringence, dispersion).

## Phase 0 — the GATE (substrate-first, refute-by-default). Settles whether ANY of this is observable.

- **Orientation coherence:** is the vacuum lattice globally single-crystal (one [100]/[111] orientation → a clean sidereal signal) or domain-averaged polycrystal (the anisotropy washes out → NO directional signal)? "Amorphous" was retired (K4 geometry is local), but global orientation is underived.
- **Preferred frame:** does the substrate have a rest frame (≈ CMB frame?), tied to the cosmic-rotation thread + the emergent-Lorentz operating point (k² isotropic; frame-dependence only at k⁴).
- **Outcome:** if domain-averaged, the directional/sidereal half is moot → scope collapses to the non-directional boost + gravity effects. **No frame code runs until this gate resolves** — no point modeling Earth's spin against an axis that doesn't globally exist. (Derive-every-aspect-before-claiming-a-test discipline.)

## Phase 1 — the frame stack (conditional on Phase-0 coherence)

Transformation engine: substrate-frame prediction + lab motion/orientation relative to the substrate, decomposed —
- Earth rotation → **sidereal** modulation; Earth orbit → **annual** modulation
- solar system through the galaxy (~230 km/s) + galaxy vs CMB (~370 km/s) → **boost / preferred-frame wind** (CMB dipole as the empirical anchor — itself a hypothesis the gate tests)
- cosmic rotation → the residual (AVE cosmic-rotation ↔ soliton-coupling thread)
- **Output:** lab observable vs sidereal/annual time + boost-velocity dependence.

## Phase 2 — gravity sensitivity sweep

AVE treats gravity as substrate density/strain (the gravity-PPN work), so the local gravitational environment can modulate the substrate state (ℓ_node, c_eff, ω_C, the saturation scale, the anisotropy). Sweep: altitude (Earth potential), the Sun–Moon tidal cycle (diurnal + monthly), the annual solar-potential swing → the **gravitational systematic budget** AND any AVE-distinct gravity-modulation signal.

## Phase 3 — adversarial audit → THEN document

Symmetric-standard before a single KB/manuscript line: does AVE's predicted sidereal/gravitational modulation actually *differ* from GR / standard-LIV templates, or are we re-deriving the standard aether-drift formalism? Is anything above current bounds? Is the orientation assumption load-bearing + honestly scoped? Canonicalize only what survives (standing rule).

## Deliverable

A reusable frame+gravity prediction engine (code) + the orientation-coherence derivation + per-bench systematic budgets (Cleave, birefringence) + an honest **"new test axis vs systematic-only"** verdict.

## Connects to

The testing pivot (fully-model-any-bench + full-sensitivity-sweeps), the cosmic-rotation ↔ soliton-coupling thread, the gravity-PPN coherence work, `feedback_experiments_fully_lattice_derived`.

## Open for Grant

- Approve scope. The honest framing up front: this is most likely **systematic-budget + test-axis-IF-coherent**, not a guaranteed new falsifier — Phase 0 decides which.
