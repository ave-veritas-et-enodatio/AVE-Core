# Phase 3f.3.3 Pre-Registration: Negative-Pressure (Stretch-Driven) Substrate Freeze-In

**Date**: 2026-05-18
**Trigger**: Grant insight "its more like the negative pressure of the expansion?" — refines earlier "cooling" framing to substrate-stretch-driven mechanism
**Parent docs**: [Phase 3f.3 prereg](2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md), [Phase 3f.3 first attempt result](2026-05-18_phase3f3-first-attempt-result.md)
**Status**: PRE-REGISTERED, not yet implemented

## TL;DR

Reframe Phase 3f.3 mechanism from "cooling" to **substrate stretch from cosmic expansion (negative pressure)**. Per AVE substrate-physics:
- Cosmic expansion stretches K4 lattice → ℓ_node grows
- Capacitance per node grows → V per node drops at constant charge
- Substrate amplitude $A = V/V_{\text{yield}}$ effectively drops as substrate stretches
- Crosses through $V_{\text{yield}}$ from above → Lenz back-EMF freezes-in topology
- Frozen topology = particles; latent heat (stretched-spring elastic energy) = particle rest mass

Test simulates substrate stretch via TIME-VARYING V_YIELD: decrease V_yield over time to simulate the substrate's elastic limit dropping as it dilates. This is implementable in ~30 lines of engine modification.

## Mechanism (refined)

**Original "cooling" framing** (Phase 3f.3 prereg): substrate at high amplitude → cool → amplitude drops → crosses V_yield → freeze-in.

**Refined "negative pressure" framing** (this prereg per Grant insight): substrate at high amplitude → cosmic expansion stretches lattice → V_yield (substrate elastic limit) drops as ℓ_node grows → amplitude/V_yield ratio crosses unity → freeze-in.

Both framings produce yield-crossing-driven freeze-in via Lenz back-EMF. The negative-pressure framing is more physically grounded:
- Driving force is geometric (substrate dilation) not thermodynamic (temperature)
- Connects directly to cosmological observables (Hubble flow, expansion rate, dark energy)
- Same mechanism unifies inflation, BBN, current dark energy, future heat death

**Connection to canonical AVE**:
- Dark-wake-bemf-foc-synthesis §1.2 freeze-in mechanism is V-dependent, not T-dependent (consistent with negative-pressure framing)
- predictions.yaml:2814-2823 specifies "When V(t) drops through V_yield" — V is the driver, not T
- Vol 3 Ch 1 K=2G operating point describes substrate algebraic equilibrium; cosmic expansion drives substrate away from equilibrium

## Test architecture

```
Initial: substrate at moderate amplitude (A ≈ 0.3) with smooth topological noise
         V_yield(0) = V_yield_0 (high — substrate is "compressed")
         
Time evolution: V_yield(t) = V_yield_0 × (1 - t/τ_expansion)
                (substrate elastic limit drops linearly as substrate stretches)

At yield crossing (t when A · V_yield_0 = V_yield(t), i.e., when amplitude
exceeds the dropping V_yield):
- Lenz back-EMF should engage at high-amplitude regions
- Topology in those regions should freeze in
- Surrounding low-amplitude regions remain mobile

Probe (during and after crossing):
- Total field energy (does it stay, or radiate away?)
- Spatial coherence (clumped or diffuse?)
- Topology of persistent structures (winding numbers, helicity)
- Frequency spectrum (do persistent structures ring at characteristic frequencies?)
```

## Implementation requirements

### Engine modification (~30 lines)

Modify FDTD3DEngine to accept time-varying V_yield:

```python
def __init__(self, ..., v_yield):
    if callable(v_yield):
        self._v_yield_fn = v_yield
        self.v_yield = float(v_yield(0.0))
    else:
        self._v_yield_fn = None
        self.v_yield = float(v_yield)

def update_electric_field(self):
    if self._v_yield_fn is not None:
        self.v_yield = float(self._v_yield_fn(self.time))
    # ... rest of update unchanged
```

Test usage:
```python
def linear_yield_decrease(t):
    return V_YIELD_0 * max(0.1, 1.0 - t / TAU_EXPANSION)

engine = FDTD3DEngine(..., v_yield=linear_yield_decrease)
```

### Test scaffolding (~150 lines)

Following Phase 3f.3 first-attempt pattern but with:
- Smooth noise (Gaussian-convolved random field per Phase 3f.3 result) to avoid numerical instability
- Time-varying V_yield protocol simulating cosmic stretch
- Probes for persistence, helicity, spatial coherence
- Comparison: constant-V_yield baseline (no stretch) vs varying-V_yield (cosmic stretch)

### Estimated effort

- Engine modification: 30 min
- Test implementation: 1 hour
- Run + analysis: 30 min
- Result documentation: 30 min
- **Total: ~3 hours single session**

## Pre-registered outcomes

- **Outcome A (PASS)**: stretch-driven engine produces preferentially (2,3)-class topology in persistent structures; constant-V_yield baseline does NOT produce topology preference. Validates the negative-pressure freeze-in mechanism as the matter-formation driver.

- **Outcome B (PARTIAL)**: stretch produces SOME topology preference but not specifically (2,3) class. Could indicate need for additional substrate physics (Cosserat coupling, K=2G algebraic operating point) to select electron-specific topology.

- **Outcome C (NULL)**: stretch produces same persistence statistics as constant-V_yield baseline. Negative-pressure mechanism alone is insufficient; need explicit Cosserat-K4 coupling for freeze-in.

- **Outcome D (FAIL)**: persistent structures are anti-correlated with topology (non-topological blobs preferred). Topology-driven matter formation framework needs fundamental revision.

- **Outcome E (TECHNICAL BLOCKER)**: engine instability, smooth-noise generation issues, or other numerical problems prevent execution. Identifies needed engine refinements.

## Falsifiers

1. **Constant-V_yield baseline produces same topology as varying-V_yield**: rules out stretch-driven mechanism; freeze-in (if observed) is from some other process.
2. **No topology preference in either case**: rules out topology-driven matter formation entirely; need additional substrate physics.
3. **Wrong topology dominant** (e.g., (1,1) Hopf instead of (2,3) trefoil): identifies that the substrate's natural topology preference isn't electron-like; framework needs revision.
4. **Stretch produces MORE dispersion, not freeze-in**: counterintuitive but would invalidate the Lenz back-EMF freeze-in mechanism.

## What this validates if PASS

1. **Negative-pressure substrate stretch IS the matter-formation driver** (Grant's refined framing)
2. **Cosmic expansion produces matter** (electrons, etc.) via the same mechanism observable in lab
3. **Dark energy = residual substrate tension** (substrate still stretching toward equilibrium)
4. **Inflation = extreme initial stretch** producing rapid matter precipitation at end
5. **Heat death = substrate disintegration** when stretched beyond elastic limit
6. **AVE thrust devices = local substrate-tensioners** (same physics, lab scale, reversible)

## Cosmological observable predictions

If PASS, this gives:

1. **Particle mass spectrum from cosmic-expansion-rate history**: $m_{\text{particle}} \propto V_{\text{yield}}(t_{\text{freeze}})$. Mass spectrum predictable from Hubble flow history. Lepton masses, quark masses → cosmic timing.

2. **Dark energy ↔ substrate residual tension**: $\rho_{\Lambda} \propto (V_{\text{current}} - V_{\text{equilibrium}})/V_{\text{equilibrium}}$. Measurable.

3. **Inflation parameters**: τ_inflation ~ τ_relax × log(stretch_max / stretch_yield). Predictable.

4. **Future heat death timeline**: time when substrate hits absolute elastic limit. Calculable from Axiom 4 + Hubble flow.

5. **Matter-antimatter asymmetry**: chirality preference during stretch-driven freeze-in. Quantifiable from substrate chirality parameters.

6. **BBN epoch from substrate stretch rate**: when V_yield drops past nucleon binding scale.

## Connection to ongoing engine work

This test sits at the intersection of:
- **Phase 3 substrate physics validation** (extends Phase 3a-f systematically)
- **Cosmic-F·c validation** (same substrate-stretch mechanism produces dark-wake AND matter formation)
- **α-emergence Phase 4** (if topology-from-stretch validates, α-emergence test architecture changes too)
- **Dark energy / cosmology** (canonical AVE prediction for cosmological observables)

This is highest-leverage single test we could run next: validates substrate-physics matter formation mechanism + connects lab to cosmology.

## Cross-references

- Canonical mechanism: [dark-wake-bemf-foc-synthesis §1.2](../manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md)
- predictions.yaml:2814-2823 (Lenz back-EMF freeze-in)
- Phase 3f.3 prereg (cooling framing, now refined): [2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md](2026-05-18_phase3f3-cosmic-cooling-matter-formation-prereg.md)
- Phase 3f.3 first attempt blocker: [2026-05-18_phase3f3-first-attempt-result.md](2026-05-18_phase3f3-first-attempt-result.md)
- Topology verification program: [2026-05-18_fundamental-topology-verification-program.md](2026-05-18_fundamental-topology-verification-program.md)
- Engine: [src/ave/core/fdtd_3d.py](../src/ave/core/fdtd_3d.py)
- Cosmic K=2G operating point: Vol 3 Ch 1, [trace-reversal-mechanism.md](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md)

## Pre-reg discipline note

This pre-reg is committed BEFORE implementation. Result doc will land at `research/2026-05-18_phase3f33-stretch-freeze-in-result.md` regardless of outcome.

Iteration history:
- Phase 3f attempt 1 (3d67cae): simplified knot seed → FAIL informative
- Phase 3f.3 attempt 1 (caca36b): random noise → BLOCKED on engine stability
- Phase 3f.3.3 (this pre-reg): stretch-driven, smooth noise → TBD

Each iteration sharpens the test architecture per pre-reg discipline lessons. Phase 3f.3.3 incorporates:
- Smooth noise (per Phase 3f.3 result)
- Stretch-driven mechanism (per Grant negative-pressure insight)
- Comparison baseline (constant-V_yield vs varying-V_yield)
- Pre-registered TECHNICAL/IMPLEMENTATION outcome category

## Recommended next action

This pre-reg is small enough to commit + push approval, then implement in same session if budget allows. Implementation is ~3 hours total.

Alternative: pause and pivot to other high-leverage work (cosmic-F·c statistical survey, AVE-Umbrella .ip-graph.yaml, Phase 4 per-private-repo pointers).
