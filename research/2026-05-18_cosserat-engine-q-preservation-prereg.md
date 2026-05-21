# Cosserat-Lagrangian Engine: Q-Preservation Soliton-Scale Test Pre-Registration

**Date**: 2026-05-18
**Target**: Verify whether C1-BH-RING's lattice-Q preservation mechanism (rigid Cosserat skeleton sets Q invariant of cavity-radius refinement) reproduces on the existing CosseratMasterEquationFDTD engine at soliton-scale.
**Parent docs**:
- C1 closure: [`ligo-ringdown-driver-design.md`](ligo-ringdown-driver-design.md) §10 (Phase 5 lattice-Q preservation derivation)
- Engine architecture: [`2026-05-18_cosserat-lagrangian-engine-full-picture.md`](2026-05-18_cosserat-lagrangian-engine-full-picture.md)
- Engine implementation: [`src/ave/core/cosserat_master_equation_fdtd.py`](../src/ave/core/cosserat_master_equation_fdtd.py)
- Op14 baseline test: [`src/tests/test_cosserat_master_equation_op14.py`](../src/tests/test_cosserat_master_equation_op14.py) (PASSES at ρ = -0.990)

## Section 1.5 — Physical Picture (5 bullets, mechanical/topological)

1. **A cavity with a rigid skeleton + compliant exterior has constant Q under exterior deformation.** C1 found this at BH scale: ν_vac=2/7 fraction of the saturation cavity is rigid (K4 lattice impedance doesn't deform with frame-dragging); 5/7 is compliant (photon-orbit shrinks with spin). When spin shifts the compliant fraction, the cavity ω_R changes but Q (set by the rigid impedance) stays constant. Therefore τ scales inversely with ω_R via τ_v2 = τ_v1·(ω_R,v1/ω_R,v2).

2. **At soliton scale, a Cosserat-coupled engine should exhibit the same behavior if lattice-Q preservation is a general substrate property.** The CosseratMasterEquationFDTD engine has K_eff(V) = K_omega_0/S(V) (compliant Cosserat stiffness modulated by V saturation) — the compliant fraction. The bare K_omega_0 acts as the rigid lattice impedance baseline. As V amplitude rises (driving saturation), K_eff rises (cavity stiffens differently); ω_R of cavity modes should shift, but Q should hold if the lattice-Q preservation rule is correct.

3. **Discrete onset vs smooth curve.** At low amplitude (S ≈ 1, linear regime): K_eff ≈ K_omega_0 (rigid only); cavity Q determined purely by lattice baseline. At high amplitude (S → 0, near saturation): K_eff diverges; cavity should "freeze" — but Q should still be constant if the rigid baseline still controls damping.

4. **What is saturating, where, in what geometry?** A localized cavity excitation (Gaussian blob in (V, ω) initialized as a coupled bound-state-like configuration) on a 32³ FDTD grid. The blob center reaches some peak amplitude A_peak; the boundary stays in linear regime. The Cosserat saturation kernel acts on V; ω experiences modulated stiffness K_eff(V). Cavity oscillation modes (V breathing + ω rotation) are the test observables.

5. **Discriminating outcome categories.** PASS: Q(A) is constant within 10% across amplitude range A ∈ [0.1, 0.7]·V_yield → existing engine reproduces C1's mechanism implicitly. PARTIAL: Q(A) varies smoothly with amplitude (e.g., Q drops by 30% at A=0.7) → engine has SOME rigid baseline but not exact lattice-Q preservation; may need explicit ν_vac=2/7 partition. FAIL: Q(A) varies wildly (>2×) or shows no recoverable scaling → mechanism is BH-topology-specific (rigid-fraction = ν_vac requires (2,3) torus-knot structure not in scalar engine).

## Section 2 — Corpus-Grep Verification (5-min cap)

**Pre-test grep checklist**:

- [x] **Existing engine implements compliant modulation**: [`cosserat_master_equation_fdtd.py:136-139`](../src/ave/core/cosserat_master_equation_fdtd.py:136): `K_eff(V) = K_omega_0/S(V)`. ✓ Compliant fraction present.
- [x] **No explicit rigid/compliant partition in engine**: grep `nu_vac`, `2/7`, `rigid_fraction` in cosserat_master_equation_fdtd.py — absent. ✓ The engine has K_omega_0 (baseline) but no explicit "rigid = ν_vac × K_omega_0 + compliant = (1-ν_vac) × K_omega_0/S(V)" decomposition.
- [x] **C1's formula at KB anchor**: [`ave-merger-ringdown-eigenvalue.md:38`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:38) confirms `x_sat(a*) = 7·[ν_vac + (1-ν_vac)·r_ph+/3M]`. ν_vac=2/7 is the rigid fraction; 1-ν_vac=5/7 the compliant.
- [x] **Op14 ρ = -0.990 baseline**: [`test_cosserat_master_equation_op14.py`](../src/tests/test_cosserat_master_equation_op14.py) PASSES (verified 2026-05-18, all 3 tests). ✓ Engine bidirectional coupling working.

**Provisional hypothesis** (NOT to be taken as conclusion): C1's lattice-Q preservation should partially hold on the existing engine. The K_omega_0 baseline provides a rigid-like component; K_eff(V) modulation provides the compliance. Q is unlikely to be EXACTLY preserved without the explicit ν_vac=2/7 weighting, but should not vary wildly. Most-likely outcome: PARTIAL with ~30% Q variation across amplitude range, identifying the explicit ν_vac=2/7 partition as a needed engine refinement.

## Section 3 — Pre-Registration

**PREREG (target: lattice-Q preservation at soliton-scale on existing CosseratMasterEquationFDTD)**:

**Corpus state**: closed on engine implementation (CosseratMasterEquationFDTD exists, Op14 baseline PASSES). Open on C1-anchored Q-preservation test (no such test exists).

**Prior work cited**:
- [`src/ave/core/cosserat_master_equation_fdtd.py:136-200`](../src/ave/core/cosserat_master_equation_fdtd.py:136) (compliant K_eff(V) modulation)
- [`src/tests/test_cosserat_master_equation_op14.py:69-138`](../src/tests/test_cosserat_master_equation_op14.py:69) (Op14 ρ = -0.990 PASSES, baseline coupling validated)
- [`ave-merger-ringdown-eigenvalue.md:38-40`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:38) (C1's rigid/compliant partition formula)
- [`research/ligo-ringdown-driver-design.md`](ligo-ringdown-driver-design.md) §10 (Phase 5 Q-preservation derivation: τ_v2 = τ_v1·(ω_R,v1/ω_R,v2))

**My prediction**:

Run the engine at 5 amplitude points A ∈ {0.1, 0.25, 0.4, 0.55, 0.7}·V_yield. For each amplitude:
1. Initialize a Gaussian (V, ω) bound-state-like blob centered at grid center
2. Run 3000 timesteps
3. Extract ω_R (peak cavity oscillation frequency, via FFT of V[center] time series)
4. Extract τ (exponential decay time of |V|_peak envelope, via log-linear fit on the late portion)
5. Compute Q = ω_R · τ / 2

**Expected result (PARTIAL outcome most-likely)**: Q(A) shows monotonic dependence on amplitude. Q at A=0.1 differs from Q at A=0.7 by 20-50%. This identifies the engine as having implicit-but-incomplete lattice-Q preservation; the explicit ν_vac=2/7 rigid/compliant partition (currently absent) is the missing piece.

**Why**: The engine's K_eff(V) = K_omega_0/S(V) is a single-fraction compliant modulation. C1's mechanism requires a TWO-fraction partition: rigid (ν_vac × K_omega_0, doesn't modulate) + compliant ((1-ν_vac) × K_omega_0 / S(V), modulates). Q-preservation holds when the rigid fraction dominates the damping rate. The existing engine has K_omega_0 (baseline rigid) plus its modulation (compliant), but they're not decomposed in the way C1 requires.

**Discriminating outcomes**:

- **Outcome A (PASS, ~20% probability)**: Q(A) constant within 10% across full amplitude range. Existing engine reproduces C1's mechanism — Axiom 4 saturation kernel alone is sufficient; lattice-Q preservation is a general substrate property (not specifically Cosserat). **Action**: Document the PASS; promote the engine's existing structure as substrate-canonical Q-preservation. No engine refactor needed. Strong validation of universal lattice-Q claim.

- **Outcome B (PARTIAL, ~60% probability)**: Q(A) varies 20-50% across amplitude. Engine has implicit-but-incomplete Q-preservation; explicit ν_vac=2/7 partition is the missing piece. **Action**: Implement Phase 2c — refactor K_eff(V) to `K_eff(V) = ν_vac × K_omega_0 + (1-ν_vac) × K_omega_0 / S(V)`. Re-test. If Phase 2c PASSES, the ν_vac=2/7 partition is canonical-required.

- **Outcome C (FAIL, ~15% probability)**: Q(A) varies wildly (>2×) or no recoverable scaling. Mechanism is (2,3)-topology-specific; can't be reproduced on a scalar engine. **Action**: Document the FAIL; flag that the soliton-scale Q-preservation requires real (2,3) torus-knot structure (not testable on scalar field engine). Pivots to Phase 4 (chiral coupling refactor + (2,q) ladder).

- **Outcome D (TECHNICAL BLOCKER, ~5% probability)**: Engine becomes unstable at A > 0.5·V_yield (per Phase 3f.3.3 historical CFL stability blocker). **Action**: Document the blocker; restrict amplitude range to A ∈ [0.1, 0.5] for partial test; flag CFL stability as gate for full test.

**Falsifier**: PASS at >10% Q variation across amplitudes invalidates the "lattice-Q is exactly preserved at soliton scale" interpretation. The C1 derivation still holds at BH scale (empirically validated), but the substrate-native interpretation must be sharpened: lattice-Q preservation is an *approximate* property emergent from the rigid-fraction baseline, not exact.

## Section 4 — Implementation

**Test scaffold**: New test file `src/tests/test_cosserat_engine_q_preservation.py` (~150 lines):

```python
def test_q_preservation_across_amplitude_scan():
    """Test C1-derived lattice-Q preservation on CosseratMasterEquationFDTD.

    PREREG: research/2026-05-18_cosserat-engine-q-preservation-prereg.md
    """
    amplitudes = [0.1, 0.25, 0.4, 0.55, 0.7]  # × V_yield
    Q_values = []

    for A_frac in amplitudes:
        engine = CosseratMasterEquationFDTD(
            nx=32, ny=32, nz=32, dx=0.01,
            v_yield=V_YIELD,
            coupling_mode="shared_flux",
        )
        engine.inject_cosserat_blob(
            center=(16, 16, 16), radius=4, amplitude=A_frac * V_YIELD,
        )
        # Also seed V correspondingly
        engine.V[...] = ...  # Gaussian V seed at same center

        V_center = []
        for step in range(3000):
            engine.step()
            V_center.append(engine.V[16, 16, 16])

        omega_R = extract_peak_frequency(V_center)  # FFT
        tau = extract_decay_time(V_center)  # log-linear fit
        Q = omega_R * tau / 2.0
        Q_values.append(Q)

    Q_variation = (max(Q_values) - min(Q_values)) / np.mean(Q_values)
    print(f"Q values: {Q_values}")
    print(f"Q variation across amplitude: {Q_variation:.2%}")
    # Outcome A: < 10% PASS; B: 10-50% PARTIAL; C: > 50% FAIL
```

## Section 5 — Result Doc (created after run)

Will log to `research/2026-05-18_cosserat-engine-q-preservation-result.md` regardless of outcome (PASS, PARTIAL, FAIL, or TECHNICAL BLOCKER).

## Section 6 — Falsifier Discipline (per `ave-prereg` Step 4)

Pre-reg committed BEFORE running the test script. Result logged regardless of outcome. No outcome rewrite.
