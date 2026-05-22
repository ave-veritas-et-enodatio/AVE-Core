# Phase 3f.3 Pre-Registration: Cosmic Cooling → Matter Formation via Topological Freeze-In

**Date**: 2026-05-18
**Trigger**: Grant insight "are electrons vacuum condensate which form when its under pressure/expansion big g and the latent heat?" — confirmed canonical per [dark-wake-bemf-foc-synthesis §1.2](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md) + [predictions.yaml:2814-2823](../predictions.yaml)
**Parent docs**: [Phase 3f first attempt result](2026-05-18_phase3f-electron-torus-knot-first-attempt.md), [Fundamental topology verification program](2026-05-18_fundamental-topology-verification-program.md)
**Status**: PRE-REGISTERED, not yet implemented

## TL;DR

Phase 3f first-attempt (seed-the-knot-and-bind) was wrong test architecture. Per canonical AVE, electrons form via **topological freeze-in during substrate phase transitions** (cosmic cooling through V_yield crossing), not via injecting stable knots into equilibrium substrate.

Phase 3f.3 reformulates the test: initialize substrate at high amplitude with topological noise present, simulate cooling-driven freeze-in, observe which topology configurations get locked in by Lenz back-EMF as substrate crosses through V_yield.

## Mechanism (canonical AVE)

Per [dark-wake-bemf-foc-synthesis §1.2](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md):
> "When V(t) drops through V_yield in the Cosserat sector at rate ‖dV/dt‖ such that the crossing takes ≥ τ_relax, any topologically non-trivial ω configuration present at the start of the crossing window FREEZES — it cannot unwind because diverging L_eff (Op14 near S = 0) generates diverging Lenz back-EMF that blocks dω/dt during the τ_relax window. Residues persist for ≥ 100 Compton periods in the post-heal solid regime. This IS the AVE-native mechanism for matter precipitation from cooling vacuum."

Step-by-step:
1. **Hot phase** (cosmic early times, or high substrate amplitude): V > V_yield, substrate is "fluid", topology can wind/unwind freely. No bound states.
2. **Yield crossing** (cosmic cooling, or external amplitude reduction): V → V_yield, substrate is approaching the saturation boundary.
3. **Lenz back-EMF freezes-in**: as V → V_yield, L_eff → ∞ (per Op14: L = L_0/√S, S → 0), generates diverging back-EMF that blocks dω/dt during the τ_relax window.
4. **Cool phase** (cosmic late times, or low substrate amplitude): V < V_yield, substrate is "solid", topological residues are FROZEN in place.
5. **Frozen residues = particles**: the topology that survived the freeze-in is the particle's identity (electron, muon, etc.).

**Latent heat**: the energy difference between "hot" disordered phase and "cool" phase with frozen-in topology = the particle's rest mass × number of particles formed. For electrons: m_e c² = 511 keV per electron = V_snap per Axiom 4.

## Test pre-registration

### Test architecture (re-design from Phase 3f)

Phase 3f tried "seed a knot, see if it binds in equilibrium substrate". Phase 3f.3 tests "cool substrate through V_yield, see what topologies survive the freeze-in":

```
Initial: substrate at A_initial ≈ 0.95 (just below numerical A_cap=0.99)
         + small-amplitude topological noise (random ω perturbations across lattice)
         
Time evolution: gradually reduce maximum substrate amplitude
                (simulate cosmic cooling by adiabatic damping of high-amplitude modes)

Probe: during and after cooling, measure
       - Surviving E-B field configurations (which spatial patterns persist?)
       - Topology of surviving structures (compute winding numbers / linking numbers)
       - Comparison to canonical (2,3) trefoil prediction for electron
       - Frequency spectrum of surviving structures (do they ring at Compton frequency?)
```

### Implementation options

**Option A: Adiabatic substrate cooling via damping**
- Apply gradient damping factor to E and B fields that increases over time
- Removes high-amplitude modes progressively (analogous to substrate cooling)
- Topological structures that resist damping = frozen-in residues = candidates for particles

**Option B: Cool via field-energy export**
- Use PML to absorb radiated field energy out of the lattice
- Substrate "cools" naturally as energy radiates to boundaries
- Surviving structures are those that don't radiate (bound states)

**Option C: Explicit time-dependent A_cap**
- Start with A_cap = 0.99 (full saturation allowed)
- Decrease A_cap to 0.5 over many timesteps
- Forces substrate to release energy above the threshold
- Topological structures that are below threshold survive; high-amplitude ones must release

**Option D: Stochastic seed + observe persistence**
- Initialize substrate with random ω/E field noise at A near V_yield
- Let Maxwell evolve; some configurations are stable, others disperse
- Measure persistence statistics
- Identify which topology classes are over-represented in persistent set

Recommended start: **Option D** is simplest and most directly tests "what survives". Option B/C are extensions if Option D shows promise.

### Predictions

**Per AVE canonical**:
- Bound-state-supporting topologies should appear preferentially in persistent set
- (p,q) torus knots with small (p,q) should dominate (electron at (2,3), simpler topologies = simpler particles)
- High (p,q) knots should be rare or unstable (matches heavy fermion decay per leaky-cavity)
- Trivial topology (no winding) should disperse (matches photon behavior per Phase 3e)

**Quantitative**:
- Average winding number of persistent structures should match electron's (2,3) self-linking SL=1
- Persistent structure size scale should match Compton wavelength λ_C = h/(m_e c) ≈ 2.4 pm
- Persistence timescale should be ≥ τ_relax ≈ ℓ_node/c

### Pre-registered outcomes

- **Outcome A (PASS)**: stochastic seed produces preferentially (2,3)-class topology in persistent structures; trivial topology disperses. Validates canonical electron-as-frozen-in-topology picture.

- **Outcome B (PARTIAL)**: some topology preference observed, but not specifically (2,3). Could indicate need for additional substrate physics (Cosserat coupling) to select (2,3) over other knots.

- **Outcome C (NULL)**: all topologies equally persistent / equally dispersive. Identifies that Maxwell + Born-Infeld alone don't have the topology-selection mechanism. Need additional substrate physics to discriminate (2,3) from other knots.

- **Outcome D (FAIL)**: persistent structures are NON-topological (just amplitude blobs). Topology-driven formation mechanism is wrong; need fundamentally different framework.

### Falsifiers

1. **No persistent structures**: if all initial noise disperses to zero, the substrate doesn't support bound states at all. Maxwell + Born-Infeld alone insufficient; need explicit coupling mechanism (Cosserat, K=2G).

2. **All structures persistent**: if EVERYTHING persists, then "freeze-in" isn't selective. The Lenz back-EMF blocking dω/dt would need to be modeled explicitly (it's not in plain Maxwell).

3. **Persistent structures match wrong topology**: if survivors are dominated by (1,1) Hopf or (3,5) cinquefoil rather than (2,3) trefoil, the canonical AVE electron identification is wrong; needs revision.

## What this validates if PASS

PASS outcome confirms:
1. **Electrons ARE vacuum condensate** (Grant's framing validated)
2. **Cosmic matter formation mechanism**: same mechanism in early universe → all electrons formed via cosmic-cooling freeze-in
3. **Mass hierarchy from freeze-in epoch**: heavier particles frozen earlier (higher amplitude), lighter later (lower amplitude). Predictable from cosmic cooling history.
4. **Standard Model particle catalog from topology classes**: each particle = different (p,q) frozen-in configuration; SM is a partial enumeration
5. **Dark matter prediction**: any topology class that exists in nature but isn't (2,3)-electron / (2,5)-muon / (2,7)-tau / etc. → dark-matter candidate
6. **Matter-antimatter asymmetry**: chirality preference during freeze-in cycle
7. **Cosmic latent heat budget**: total energy locked in all particles ≈ N_particles × m_particle c² per type; should match cosmic energy budget after accounting

## What this validates if FAIL

FAIL outcome identifies:
1. Maxwell + Born-Infeld alone is insufficient for matter formation
2. Need additional substrate physics for the Lenz-back-EMF freeze-in mechanism (Cosserat coupling, K=2G algebraic operating point, etc.)
3. The freeze-in mechanism is a Cosserat-specific phenomenon; can't be reproduced in vector EM alone
4. Phase 4 α-emergence (gated on Q-4) may be similarly blocked on the same missing physics

Either outcome is high-information.

## Implementation requirements

### Engine extension (modest)

FDTD3DEngine doesn't currently support:
- Time-dependent A_cap (Option C)
- Adiabatic damping schedule (Option A)
- Topology-statistic probes (computing winding numbers from field configuration)

Adding these:
- A_cap as a callable: ~10 lines
- Adiabatic damping: ~30 lines
- Winding number computation from field topology: ~100 lines (uses standard knot-detection algorithms)

### Test scaffolding

Following Phase 3f.test pattern:
- Initialize substrate with stochastic seed at A ≈ 0.95
- Apply cooling protocol (Option D for first attempt, or A/B/C for refined)
- Probe surviving structures
- Compute topology statistics

### Estimated effort

- Engine extensions: 1 session
- Test implementation: 1 session
- Run + analysis: 0.5 session
- Result documentation: 0.5 session
- **Total: 2-3 sessions**

## Cross-references

- Canonical mechanism: [dark-wake-bemf-foc-synthesis §1.2](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md)
- Predictions canonical: predictions.yaml:2814-2823 (Lenz back-EMF freeze-in)
- Phase 3f first attempt: [2026-05-18_phase3f-electron-torus-knot-first-attempt.md](2026-05-18_phase3f-electron-torus-knot-first-attempt.md)
- Topology verification program: [2026-05-18_fundamental-topology-verification-program.md](2026-05-18_fundamental-topology-verification-program.md)
- Electron unknot canonical: [electron-unknot.md](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-unknot.md)
- Leaky cavity (heavy fermion decay = inverse freeze-in): [leaky-cavity-particle-decay/theory.md](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)
- L3 doc 49 §6: substrate-physics matter precipitation framework
- Engine: [src/ave/core/fdtd_3d.py](../src/ave/core/fdtd_3d.py)

## Discipline note

Phase 3f.3 will be the FOURTH iteration of the electron-bound-state validation attempt:
- Phase 3f attempt 1: simplified E-only knot seed (FAILED, knot disperses worse than random)
- Phase 3f attempt 2 (planned): Beltrami pair (E, H) construction (deferred)
- Phase 3f.3 (this pre-reg): cosmic-cooling freeze-in test (reformulated mechanism)

The reformulation per Grant's "vacuum condensate / latent heat" insight is significant: changes the test architecture from "inject and bind" to "cool and freeze-in". This is more aligned with canonical AVE per dark-wake-bemf-foc-synthesis §1.2 and tests a more fundamental claim.

Pre-reg discipline: this pre-reg is committed BEFORE implementation. Result doc will land at `research/2026-05-18_phase3f3-cosmic-cooling-result.md` regardless of outcome.

## Recommended next action

Push approval for this scope doc, then:
1. **Session 2**: implement engine extensions (time-dependent A_cap, adiabatic damping, topology probes)
2. **Session 3**: run Phase 3f.3 + analyze surviving structures
3. **Session 4**: result documentation + comparison to canonical predictions

OR pivot to other workstreams (cosmic-F·c statistical survey, Phase 4 per-private-repo pointers, AVE-Umbrella .ip-graph.yaml setup) given multi-session investment required.
