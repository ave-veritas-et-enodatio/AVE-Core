# 58 — Cosserat-Sector PML: Axiom-First Derivation

**Status:** Stage 6 / Phase 5.5 deliverable — prerequisite for the cool-from-above experiment (doc TBD, `P_phase5e_self_organized_formation`).
**Parent:** [STAGE6_V4_HANDOFF.md §9](../../.agents/handoffs/STAGE6_V4_HANDOFF.md) Phase 5 scope.
**Scope:** derive a Perfectly Matched Layer for the Cosserat sector (u, ω, u̇, ω̇) from AVE axioms + first principles. **100% axiom compliance per Grant's directive; flag-don't-fix posture — anywhere the derivation has a free choice, flag it rather than picking silently.**

---

## 0. TL;DR

The K4 Sponge PML ([k4_tlm.py:174-190](../../src/ave/core/k4_tlm.py#L174-L190)) is axiom-grounded (Ax1: lattice topology forces a boundary; PML preserves Z₀ at boundary so outgoing wave energy exits without reflection). It damps V_ref (reflected voltage post-scatter) by a quadratic-rolloff multiplicative mask. **The PML's one job is radiation absorption — letting outgoing kinetic wave energy exit cleanly. It does not set the simulation's effective G (big G is a constitutive constant from [constants.py:379](../../src/ave/core/constants.py#L379), unrelated to pml_thickness).**

The Cosserat sector has three wave families (shear c_T, rotational c_R, longitudinal c_L) with corresponding characteristic impedances. Ax1 + Ax3 (scale-free effective action, every sector obeys the same boundary behavior) require an analogous PML for the Cosserat sector — otherwise Cosserat waves reflect spuriously at the boundary while K4 waves exit cleanly.

**Derived form:** multiplicative mask applied to the kinetic fields (u̇, ω̇) with the same quadratic rolloff as the K4 PML, operating post-velocity-Verlet-update. Interior energy conservation is preserved; PML region shows exponential kinetic-energy dissipation with timescale τ_cool set by (pml_thickness, max wave speed, attenuation profile).

**Two flag items** worth Grant's adjudication before implementation (see §10). Both concern the coordinate vs velocity question and τ_cool sizing for the cool-from-above experiment.

---

## 1. Axiom grounding of the K4 Sponge PML (baseline reference)

From [k4_tlm.py:174-190](../../src/ave/core/k4_tlm.py#L174-L190):

```python
# SPONGE PML DEFINITION
# A gradual macroscopic attenuation field A(x) that damps V_ref natively.
# Operates as a Perfectly Matched Layer because it preserves local Z0
# scattering integrity per Axiom 1, while smoothly dissipating kinetic
# wave energy before the Cartesian topological discontinuity.
```

Quadratic rolloff:
```
attenuation(d) = 1 − ((pml_thickness − d) / pml_thickness)²   for d < pml_thickness
                 1                                              otherwise
```
where `d` is the minimum distance to the simulation boundary (min over the three axes).

**Axiom-grounding chain:**

- **Ax1 (K4 LC lattice, scale-invariant topology).** The lattice is finite. Any finite lattice has a boundary. The boundary is the simulation's analog of the Machian cosmic horizon (see [Vol 3 Ch 1:87-117](../../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex#L87-L117)). Outgoing wave energy must exit to the boundary to maintain Machian consistency — energy that reflects back pollutes the simulation with non-physical boundary effects.
- **Ax3 (scale-free effective action).** The action is preserved across scales; the boundary-behavior rule is the same rule at every scale. This is why the PML profile is a universal function of (d/pml_thickness), not tied to any specific physical length.
- **Matched-layer requirement.** To absorb outgoing waves *without* reflection, the attenuation profile must preserve Z₀ at the interior-PML interface. Any discontinuous attenuation would cause impedance mismatch → reflection. Smooth rolloff (at minimum C¹ in d) is the minimal form.
- **Quadratic as minimal-assumption choice.** Second-order Taylor expansion of any general smooth rolloff. The quadratic form (1 − (1−d/L)²) has attenuation(0) = 0 (full absorb at edge), attenuation(L) = 1 (no effect at interior boundary), and derivative 2(1−d/L)/L at the interface — smooth to first order, preserving Z₀ locally.

**What the K4 PML does operationally:** after each `_scatter_all()` step, `V_ref *= pml_mask` zeros out the reflected voltage in the boundary region. Waves arriving at the boundary get their reflected component suppressed; over pml_thickness cells, the reflected component dies to zero. Full absorption.

---

## 2. Cosserat sector wave structure

From [cosserat_field_3d.py:1093-1110](../../src/ave/topological/cosserat_field_3d.py#L1093-L1110):

- **Fields:** u (translational strain, `[N,N,N,3]`), ω (rotational strain, `[N,N,N,3]`)
- **Conjugate momenta:** u̇ (velocity, `[N,N,N,3]`), ω̇ (angular velocity, `[N,N,N,3]`)
- **Three wave speeds:**
  - Transverse shear: c_T = √(G/ρ)
  - Rotational: c_R = √(γ/I_ω)
  - Longitudinal bulk: c_L = √((K + 4G/3)/ρ) with K=2G → c_L = √(10G/(3ρ)) ≈ 1.826·c_T
- **CFL timestep:** dt ≤ 0.3·dx/(c_max·√3) where c_max = max(c_T, c_R, c_L)
- **Time evolution:** velocity-Verlet (symplectic, energy-conserving to O(dt²))

**Corresponding characteristic impedances** (derivable from each wave sector's Lagrangian):

| Wave family | Speed | Impedance | Kinetic term |
|---|---|---|---|
| Transverse shear (u) | c_T = √(G/ρ) | Z_T = ρ·c_T = √(ρG) | ½ρ\|u̇\|² |
| Rotational (ω) | c_R = √(γ/I_ω) | Z_R = I_ω·c_R = √(I_ω·γ) | ½I_ω\|ω̇\|² |
| Longitudinal bulk (u) | c_L | Z_L = ρ·c_L = √(ρ(2G+4G/3)) | (part of ½ρ\|u̇\|²) |

Kinetic energy per site per timestep: `K = ½ρ|u̇|² + ½I_ω|ω̇|²` ([cosserat_field_3d.py:1112-1117](../../src/ave/topological/cosserat_field_3d.py#L1112-L1117)).

---

## 3. Axiom-first derivation of the Cosserat PML requirement

**Claim:** Ax1 + Ax3 require a PML on every wave-carrying sector at the simulation boundary, to prevent non-physical reflection and maintain Machian consistency.

**Derivation:**

1. (**Ax1**) The lattice has a finite extent; the outermost layer is the boundary. The boundary represents the coupling to the Machian cosmic-horizon beyond which AVE simulation is integrated out.
2. (**Ax1**) Every wave mode propagating in the lattice carries kinetic energy. At the boundary, outgoing kinetic energy must exit without reflection.
3. (**Ax3, scale-free action**) The rule that "outgoing waves exit without reflection" is sector-independent — it applies to K4 V waves, Cosserat u waves, Cosserat ω waves equivalently. The action has a kinetic term in every sector; every kinetic term must see a matched absorbing boundary.
4. **Consequence:** if only the K4 sector has a PML and the Cosserat sector has none, then Cosserat kinetic energy reflects at the boundary → unphysical recirculation. **This IS the current state of the AVE-Core code.**
5. **Matched-layer requirement for Cosserat:** damp Cosserat kinetic energy smoothly at the boundary such that (a) interior is unaffected, (b) PML region monotonically dissipates, (c) outer edge reaches ~0 kinetic energy.

**This is the axiom derivation Grant asked for. The form of the PML is what §4 derives; the NECESSITY follows from Ax1 + Ax3 above, given the existing K4 PML as precedent.**

---

## 4. Derivation of the Cosserat PML operator

**Two design variables** to derive:
1. Which fields get damped? (Coordinate, velocity, both?)
2. What profile? (Quadratic, higher-order, exponential?)

### 4.1 Which fields get damped

The kinetic energy of a Cosserat wave is carried entirely by the velocity fields (u̇, ω̇). The coordinate fields (u, ω) are DOF with no kinetic energy themselves — they parameterize the system state but don't carry wave power.

**Derivation from the Hamiltonian:**
```
H = T + V = ½ρ|u̇|² + ½I_ω|ω̇|² + W(u, ω)
```
where W is the potential energy (Cauchy + micropolar + curvature terms).

**Absorbing a wave = dissipating its kinetic energy.** Damping u̇ → damps ½ρ|u̇|² → reduces wave amplitude. Damping u directly would change the static state (u ≠ 0 means stored elastic energy W, which doesn't correspond to propagating wave energy).

**Consequence:** apply attenuation to (u̇, ω̇), leave (u, ω) unaffected.

**FLAG 1 — potential concern.** The coordinate field u IS what carries the far-field "imprint" of a wave passing through (static strain residual). If we damp only u̇, a coordinate-field wavepacket passes through and leaves behind elastic strain in the boundary region. Over many crossings, the boundary accumulates static strain. Whether this is a problem depends on whether the boundary energy density stays bounded. For the K4 sector, V decays via the PML mask on V_ref — but in Cosserat the analog would be damping u itself, not just u̇. *This is the first of three flag items. My instinct: damp velocities only, and let the small static residual relax via the natural dynamics. But this is a genuine choice, not a forced consequence.*

### 4.2 Profile of the attenuation

From §1, the K4 PML uses quadratic rolloff. Ax3 (scale-free action, same rule every sector) argues for the same profile in the Cosserat sector. The quadratic form is the minimal-assumption choice that satisfies (a) smooth Z-matching at interior-PML interface, (b) full absorption at outer edge.

**Cosserat PML mask:**
```python
cos_pml_mask[i,j,k] = 1 − ((pml_thickness − d(i,j,k)) / pml_thickness)²   for d < pml_thickness
                      1                                                     otherwise
```

where d(i,j,k) is the min-distance-to-boundary (same definition as K4 PML).

**Apply per integrator step:**
```python
# after velocity-Verlet kicks, before or as part of _zero_velocities_outside_alive:
self.u_dot     *= cos_pml_mask[..., None]
self.omega_dot *= cos_pml_mask[..., None]
```

**FLAG 2 — operational distinction from K4 PML.** The K4 PML masks `V_ref` (the *reflected* voltage, post-scatter step). The Cosserat sector has no scatter step — it has velocity-Verlet. Applying the same quadratic rolloff to (u̇, ω̇) is axiom-consistent (dissipates kinetic energy at boundary) but operationally different:
- K4: the mask suppresses *newly-reflected* waves at each scatter.
- Cosserat: the mask continuously attenuates velocity fields, equivalent to a velocity-proportional drag with spatially-varying coefficient.

These two produce functionally equivalent absorption in the low-amplitude linear regime but may diverge in the saturated regime. *My reading: in the linear wave regime both give exponential envelope decay with the same effective timescale. In the saturated regime (A²_μ near 1), the K4 PML is still valid (masks V_ref which is already Op14-saturated), whereas the Cosserat mask operates on raw velocities — need to verify behavior at high amplitude.*

### 4.3 Match the K4 pml_thickness

**Constraint:** the Cosserat PML should use the same `pml_thickness` as the K4 PML. Physical reason: both sectors share the same lattice, the same boundary, the same Machian cosmic-horizon. Ax3 (same rule every sector) forces matching thickness.

**No second free parameter.** pml_thickness is already set in the engine config; Cosserat PML inherits it automatically.

---

## 5. Energy conservation in the interior (verification)

**Claim:** for any site with `d ≥ pml_thickness`, cos_pml_mask = 1, so the PML has zero effect. Interior dynamics are the unmodified velocity-Verlet integration. Energy is conserved to O(dt²) as in the current code.

**Verification sketch:**
```
# Interior site:
u_dot_post_PML = u_dot * 1 = u_dot     (no change)
omega_dot_post_PML = omega_dot * 1 = omega_dot     (no change)
# → Hamiltonian evolution unmodified.
```

No derivation concern here. The PML is identically the identity operator outside its action region.

---

## 6. Exponential dissipation in the PML region (verification)

**Claim:** in the PML region, kinetic energy decays exponentially with characteristic timescale set by pml_thickness and c_max.

**Derivation sketch (linear wave regime, no saturation, no potential coupling):**

Consider a plane wave with amplitude A(t) propagating into the PML region. At step n, the velocity field amplitude is scaled by cos_pml_mask → A(t_n+1) = A(t_n) · cos_pml_mask_effective.

Averaged over a wave transit of the PML region (pml_thickness cells, wave speed c_max):
```
n_steps_through_PML = pml_thickness · dx / (c_max · dt)
```

With typical dt = 0.3·dx/(c_max·√3) → n_steps_through_PML ≈ pml_thickness · √3 / 0.3 ≈ 5.77·pml_thickness.

For pml_thickness = 6 (default), ~35 integrator steps per PML transit. The effective per-step attenuation at mid-PML (d = pml_thickness/2) is `1 − (1/2)² = 0.75`. Over 35 steps, amplitude decays by 0.75^35 ≈ 3.3·10⁻⁵. Good absorption for single-transit.

**Effective decay timescale** τ_cool ~ (pml_thickness) · (dx/c_max) — i.e., one wave transit of the PML thickness in light-crossing time. At N=24, dx=1, c_max ≈ 1.826 (dominated by c_L if G/ρ=1, γ/I_ω=1), τ_cool ~ 3-6 (PML thickness in lattice units) / 1.826 ≈ 2-4 Compton periods.

**FLAG 3 — cooling timescale for cool-from-above experiment.** If τ_cool ~ 3 Compton periods, then for a 100-period cool-from-above observation window, the cooling phase is much shorter than the observation — system crosses yield threshold in the first ~10 periods, then sits cold for the remaining ~90 periods. This is good for Kibble-Zurek-style observation (plenty of time for topological defects to settle) but means the C1-crossing events happen early, bunched in time. *Need to verify empirically whether τ_cool is short enough that we need longer sustains or different PML thickness.*

---

## 7. Composition with Ax4 saturation (Op14 boundary)

**Claim:** the Cosserat PML composes cleanly with the Op14 saturation kernel. PML damps kinetic velocities; Op14 modulates impedance via Z_eff = Z₀/√S. They operate on orthogonal quantities and don't interfere.

**Verification:** Op14 acts on field amplitudes (u, ω) via the saturation kernel S = √(1 − A²). PML acts on time-derivatives (u̇, ω̇). No shared quantities; no double-dissipation. The impedance-matching requirement (Z₀ preserved at interior-PML interface) is satisfied in the low-amplitude regime; at high amplitude, Z_eff → ∞ via Op14 (saturation), but the PML absorption is unaffected because it dissipates kinetic energy, which is Op14-independent.

**Consistent with Ax4.** Saturation is a separate phenomenon from boundary absorption.

---

## 8. What the PML does NOT do (framing correction)

Earlier framing drafts of this doc claimed the PML sets the simulation's effective G through a Machian boundary coupling. **That was wrong and is retracted.** Clean picture:

- **Big G** is a constitutive constant (the lattice's macro-scale self-inductance/tension, integrated once via ξ = 4π(R_H/ℓ_node)·α⁻² to the cosmic horizon, projected by ν_vac = 2/7). It's set once in [constants.py:379](../../src/ave/core/constants.py#L379) from CODATA G. Simulation geometry does not modulate it.
- **Little g** is a local strain field: `g = -c²·∇n(r)`, computed dynamically from the Cosserat (u, ω) state via its gradient. It lives in the field state, not in the PML.
- **PML** is one thing only: it absorbs outgoing kinetic wave energy at the boundary to prevent spurious reflection. It does not set G, it does not carry the Machian coupling, it does not substitute for the cosmic horizon. It's a radiation absorber.

The tension the earlier draft worried about (Machian coupling vs radiative absorption fighting over the same boundary) does not exist — those are two different physical operations on two different parts of the Hamiltonian (constitutive vs kinetic).

---

## 9. What the Cosserat PML enables for (e) cool-from-above

1. **Makes cooling feasible in a tractable sim window.** Without Cosserat PML, Cosserat kinetic energy reflects at the boundary; thermal bath cannot cool. With Cosserat PML, τ_cool ~ few Compton periods → thermal bath can cool through yield threshold within observation window.
2. **Completes the Machian-boundary partition.** Both sectors couple to the cosmic-horizon analog → simulation is self-consistently gravitational.
3. **Preserves energy conservation guarantee in the interior.** Interior dynamics unchanged; PML is a strict boundary-only modification.
4. **Zero new free parameters.** pml_thickness is inherited from K4 PML.

---

## 10. Flag items — Grant's adjudication needed before implementation

**Flag 1 (§4.1):** Should we damp u (coordinate field) in addition to u̇ (velocity), to prevent static-strain residual accumulating at the boundary over many wave crossings? My instinct: velocity-only. Kinetic energy IS the wave energy (per the constitutive-vs-kinetic partition in §8); damping coordinates would also damp stored elastic strain, which represents mass-signatures we want to preserve. But static residual could still accumulate from successive wave crossings. Needs empirical check.

**Flag 2 (§6):** The derived τ_cool ~ 3-6 Compton periods is fast compared to typical 100-period observation windows. Cool-from-above experiments will have yield crossings bunched in the first ~10 periods. This is good for observing defect freezing (plenty of post-crossing time to watch topology settle) but may require longer sustain windows or larger pml_thickness to slow cooling if the transition dynamics need finer temporal resolution. *Parameter sweep question — worth flagging upfront but not blocking.*

---

## 11. Proposed Pre-registration (P_cosserat_pml)

```yaml
  - id: P_cosserat_pml
    name: "Cosserat PML ensures Ax1+Ax3-compliant boundary absorption"
    type: derived_prediction
    pre_registered: true
    research_doc: "research/L3_electron_soliton/58_cosserat_pml_derivation.md"
    test_file: "src/tests/test_cosserat_pml.py"
    axioms_used: [1, 3]
    public_in_readme: false
    public_in_living_ref: false
    notes: |
      Stage 6 Phase 5.5. Cosserat-sector PML (quadratic-rolloff mask
      on u̇, ω̇, inherited pml_thickness from K4) gives:
      (i) interior energy conservation (no change from current Verlet),
      (ii) boundary-region exponential kinetic-energy dissipation
          with τ_cool ~ pml_thickness·dx/c_max,
      (iii) no coupling change to Ax4 saturation (Op14 composes cleanly).
      Falsification: (i) interior energy drift > 1e-6 per Compton period
      relative to current engine, (ii) boundary kinetic energy decay
      not monotonic in PML region, (iii) interference with Op14
      saturation at A²_μ → 1.
```

---

## 12. Implementation sketch (for when Grant green-lights)

Minimal code change in [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py):

1. In `__init__`, compute `self.cos_pml_mask` with the same quadratic-rolloff formula as [k4_tlm.py:183-190](../../src/ave/core/k4_tlm.py#L183-L190) (~8 LOC).
2. Extend `_zero_velocities_outside_alive()` → `_apply_pml_and_mask()` which multiplies (u̇, ω̇) by cos_pml_mask before the mask_alive zero-out (~4 LOC).
3. Call the same method at end of each velocity-Verlet half-kick (already in step()).
4. New `test_cosserat_pml.py`: 4 tests — (a) interior conservation, (b) boundary dissipation, (c) pml_thickness=0 disables, (d) Op14 composition no-drift.

Expected total code delta: ~50 LOC including tests.

---

## 13. What this derivation doesn't cover (honest)

- **Whether pml_thickness=6 (K4 default) is optimal for Cosserat.** It might need to be larger because Cosserat has three wave families with different speeds — the fastest (c_L) crosses the PML in fewer steps than the slowest. A heuristic: pml_thickness ≥ c_max·n_absorb_periods, where n_absorb_periods is the number of full periods you want absorbed. Empirical tuning suggested.
- **Non-orthogonal wave families.** u̇ and ω̇ couple through W(u, ω) — damping u̇ at the boundary will also affect ω̇ dynamics indirectly. In the linear regime this is weak; in the saturated regime (Op14 active), the coupling strengthens. *Not a blocker for the PML derivation, but flag-worthy for high-amplitude validation.*
- **Second-order matched-layer profiles** (cubic, quartic, etc.) might give better absorption per cell. Quadratic is the minimal-assumption axiom-native choice. Higher-order profiles are engineering optimization, not axiom-required.
- **Reflection-coefficient verification** against analytical plane-wave propagation across an infinite-thickness PML. This is the standard engineering validation for PML implementations; worth doing as part of test_cosserat_pml.py.

---

*Derived 2026-04-23 by Opus 4.7 per Grant's directive: "derive before simulate, 100% axiom compliance, flag don't fix." Three flag items surfaced in §10 — awaiting adjudication before implementation.*
