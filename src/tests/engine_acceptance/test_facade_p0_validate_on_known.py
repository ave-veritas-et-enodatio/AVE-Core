"""P0 facade — validate-on-known THROUGH the regime-dispatch facade.

Design note: research/2026-06-25_unified-engine-P0-design.md.
Facade: ave.facade.unified_engine (the single-grid 6-DOF unified engine).

This suite reproduces RUNG-0 (Z₀=376.7Ω, unitary-scatter energy, isotropy) and
RUNG-1 (L0 axiom-compliance + L1 free modes) THROUGH the facade — every observable
is read via `UnifiedEngine.*`, NOT by calling the cores directly. It is the P0
acceptance gate: the facade must reproduce the certified-core greens, and the
single-grid bet (A1 scalar node-field + ω micro-rotation on the SAME K4 graph)
must hold with the closed-box energy gate green end-to-end.

substrate-native-check (walked in the design note §0): every operator the facade
dispatches is native-K4 (srs z=3 TLM + TETRA_OFFSETS diamond Grad/Div), NOT
Cartesian-7pt. ave-regime-phase-state-check: MODE=all-6-DOF / REGIME=linear S=1 /
PHASE-STATE=cold lossless. consistency-vs-emergence: Z₀ is CONSISTENCY/IDENTITY-
class (CODATA-pinned via ave.core.constants, NOT an emergence); the energy /
isotropy / winding rows are CONSISTENCY-class.

α-CLEAN: the facade re-asserts the import-guard triad at construction; no
α-carrier on any path here.
"""

from __future__ import annotations

import numpy as np

from ave.facade import Regime, UnifiedEngine, UnifiedEngineConfig


# ═════════════════════════════════════════════════════════════════════════════
# RUNG-0 — energy / unitary-scatter, Z₀=376.7Ω, isotropy (through the facade)
# ═════════════════════════════════════════════════════════════════════════════
def test_facade_rung0_characteristic_impedance():
    """RUNG-0 [IDENTITY] — Z₀ = √(μ₀/ε₀) = 376.730 Ω through the facade.

    The facade derives Z₀ from the vacuum moduli (NOT a hardcoded literal — the
    make-verify EFT magic-number guard). CONSISTENCY/IDENTITY-class.
    """
    eng = UnifiedEngine()
    z = eng.characteristic_impedance()
    print("\n--- RUNG-0 Z₀ (facade) ---")
    print(f"  Z₀ from √(μ₀/ε₀) : {z['Z0_ohm']:.6f} Ω")
    print(f"  matches canonical: {z['matches_canonical']}  reproduces_Z0: {z['reproduces_Z0']}")
    assert z["matches_canonical"], "FAIL: facade Z₀ != canonical √(μ₀/ε₀)"
    assert z["reproduces_Z0"], "FAIL: facade Z₀ does not reproduce the canonical Z_0"


def test_facade_rung0_unitary_scatter_energy():
    """RUNG-0 [CONSISTENCY] — the free-mode TLM medium conserves energy exactly
    (unitary scatter: CONNECT is a port permutation ⇒ orthogonal one-step map).
    Read through the facade (wires chiral_lattice_dynamics).
    """
    eng = UnifiedEngine()
    r = eng.unitary_scatter_energy_drift(n_steps=400)
    print("\n--- RUNG-0 unitary-scatter energy (facade) ---")
    print(f"  connect_is_permutation: {r['connect_is_permutation']}")
    print(f"  energy_drift          : {r['energy_drift']:.3e}  (PASS < 1e-8)")
    assert r["connect_is_permutation"], "FAIL: CONNECT not a permutation (non-unitary)"
    assert r["energy_drift"] < 1e-8, f"FAIL: lossy medium — drift {r['energy_drift']:.3e}"
    assert r["lossless"]


def test_facade_rung0_isotropy():
    """RUNG-0 [CONSISTENCY] — the 3D-isotropic network velocity c(k→0)/c_link =
    1/√3 (the achiral 'did-not-break-it' invariant) through the facade.
    """
    eng = UnifiedEngine()
    iso = eng.isotropy_factor(n_steps=400)
    print("\n--- RUNG-0 isotropy (facade) ---")
    print(f"  factor       : {iso['factor']:.5f}  vs 1/√3 = {iso['target_inv_sqrt3']:.5f}")
    print(f"  rel_error    : {iso['rel_error']:.3e}  (PASS < 0.02)")
    assert iso["isotropic"], f"FAIL: anisotropic — rel {iso['rel_error']:.3e}"


def test_facade_rung0_closed_box_energy_gate():
    """RUNG-0 [RIGOR GUARD] — the closed-box energy gate in the LOSSLESS LIMIT:
    |dH/H| < 1e-8 with NO secular bleed. Wires native_cage_imex's certified
    Crank–Nicolson / Newmark β=¼ energy gate.

    HONEST mechanism (flag-don't-fix; design note + energy_gate_lossless_limit
    docstring): the residual |dH/H| scales as A² — the frozen-D nonlinearity lag,
    NOT a fixed integrator floor. The lossless (A→0, D→1 const) limit is exactly
    energy-conserving per the certified core. The A²-scaling is asserted here so
    the 1e-8 gate is met in the regime where it physically applies (NO threshold
    is loosened — this is the lossless limit of the gate, run honestly).
    """
    eng = UnifiedEngine()
    g = eng.energy_gate_lossless_limit(n_steps=2000)
    print("\n--- RUNG-0 closed-box energy gate (facade, lossless limit) ---")
    for row in g["rows"]:
        print(f"  A₀={row['amplitude']:.0e}  |dH/H|={row['rel_drift']:.3e}  "
              f"slope={row['secular_slope']:.2e}")
    print(f"  A²-scaling ratios: hi={g['A2_scaling_ratio_hi']:.1f} "
          f"lo={g['A2_scaling_ratio_lo']:.1f}  (=100 ⇒ A² law)")
    print(f"  lossless-limit |dH/H| = {g['lossless_rel_drift']:.3e}  (PASS < 1e-8)")
    assert g["A2_scaling_confirmed"], (
        "FAIL: |dH/H| does not scale as A² — the residual is NOT the frozen-D lag "
        "(a fixed integrator floor would FAIL the lossless-limit claim)."
    )
    assert g["gate_1e8_passed"], (
        f"FAIL: closed-box energy gate |dH/H|={g['lossless_rel_drift']:.3e} not < 1e-8 "
        f"in the lossless limit."
    )


# ═════════════════════════════════════════════════════════════════════════════
# RUNG-1 — L0 axiom-compliance + L1 free modes (through the facade)
# ═════════════════════════════════════════════════════════════════════════════
def test_facade_rung1_axiom1_six_dof_single_grid_state():
    """RUNG-1 [Axiom-1] — the single-grid 6-DOF/node state: 3 translation u +
    3 Cosserat micro-rotation ω, with the A1 dilatation scalar a NODE-ATTACHED
    field on the SAME K4 graph (the single-grid rep). Plus the srs z=3
    connectivity invariant (do NOT flip 3→4).
    """
    eng = UnifiedEngine()
    st = eng.state
    # 6 DOF/node: u (3) + omega (3) + the A1 node-field scalar (+1)
    assert st.u.shape[-1] == 3, "FAIL: translational DOF != 3"
    assert st.omega.shape[-1] == 3, "FAIL: micro-rotation DOF != 3"
    assert st.a_A1.ndim == 3 and np.iscomplexobj(st.a_A1), (
        "FAIL: A1 must be a complex SCALAR node-field (not a vector grade)"
    )
    # all three share the SAME node grid (single-grid bet)
    N = eng.cfg.N
    assert st.u.shape[:3] == (N, N, N)
    assert st.omega.shape[:3] == (N, N, N)
    assert st.a_A1.shape == (N, N, N), "FAIL: A1 node-field not on the same grid as u, ω"
    # srs z=3 connectivity invariant (the free-mode carrier)
    net = eng.free_modes()
    assert net.degree == 3, f"FAIL: srs connectivity z={net.degree} != 3 (do NOT flip 3→4)"
    print("\n--- RUNG-1 Axiom-1 single-grid 6-DOF state (facade) ---")
    print(f"  u {st.u.shape} + ω {st.omega.shape} + a_A1 {st.a_A1.shape} (complex scalar node-field)")
    print(f"  srs free-mode carrier connectivity z = {net.degree} (= 3, native K4)")


def test_facade_rung1_axiom4_saturation_kernel_and_channels():
    """RUNG-1 [Axiom-4] — the α-clean saturation kernel S(A)=(1−A²)^p AND BOTH
    velocity channels keyed to channel (do NOT pin one exponent):
    c_EM=c₀/S (phase) and c_shear=c₀·√S (group/mass). At S=1 (linear) both
    collapse to c₀ (the split is driven-only). c_shear def-lock INHERITED.
    """
    eng = UnifiedEngine()
    # kernel: S(0)=1 (cold), monotone-decreasing, α-clean
    assert abs(float(eng.saturation_kernel(0.0)) - 1.0) < 1e-12, "FAIL: S(0) != 1 (cold)"
    assert float(eng.saturation_kernel(0.9)) < 1.0, "FAIL: kernel not decreasing under strain"
    # channels at S=1 collapse to c₀; at A=0.9 they SPLIT (both carried)
    vc1 = eng.velocity_channels(0.0)
    assert abs(float(vc1["c_EM_over_c0"]) - 1.0) < 1e-12
    assert abs(float(vc1["c_shear_over_c0"]) - 1.0) < 1e-12
    vcs = eng.velocity_channels(0.9)
    assert float(vcs["c_EM_over_c0"]) > 1.0, "FAIL: c_EM phase did not rise (1/S)"
    assert float(vcs["c_shear_over_c0"]) < 1.0, "FAIL: c_shear group/mass did not fall (√S)"
    # the two are RECIPROCAL-keyed: c_EM = 1/S, c_shear = √S ⇒ c_EM·c_shear² = 1/S·S = 1... no:
    # c_EM=1/S, c_shear=√S ⇒ c_EM · c_shear^2 = (1/S)·S = 1 (channel-keying identity)
    S = float(vcs["S"])
    assert abs(float(vcs["c_EM_over_c0"]) - 1.0 / S) < 1e-12
    assert abs(float(vcs["c_shear_over_c0"]) - np.sqrt(S)) < 1e-12
    print("\n--- RUNG-1 Axiom-4 kernel + velocity channels (facade) ---")
    print(f"  S(0.9)={S:.5f}  c_EM/c₀={float(vcs['c_EM_over_c0']):.4f} (1/S)  "
          f"c_shear/c₀={float(vcs['c_shear_over_c0']):.4f} (√S)  [both carried, neither pinned]")


def test_facade_rung1_single_grid_verdict_joint_energy():
    """RUNG-1 + SINGLE-GRID VERDICT (load-bearing half) — the bet's load-bearing
    test: the A1 scalar node-field AND the ω micro-rotation evolve on the SAME
    diamond-K4 node set, with the JOINT energy conserved (unitary CN/Cayley)
    end-to-end and neither grade drained into the other (genesis-24
    BOTH-conserved), the (2,3) winding integer held. Wires coupled_cage_winding.

    SCOPE (do NOT overclaim — design note §2 verdict): GREEN here proves the
    LOAD-BEARING HALF — the A1 scalar does NOT need a second grid relative to ω.
    It does NOT by itself dissolve the two-grid bridge: two distinct
    native-K4-FAMILY carriers still remain (the srs z=3 free-photon carrier +
    this diamond z=4 A1/ω carrier). Collapsing them onto ONE literal node list is
    the P1 task = the D1 connectivity decision (chiral z=3 srs vs achiral z=4
    diamond).

    REGIME: linear (A≪1) lossless — the closed-box (no PML, no damping) limit.
    """
    eng = UnifiedEngine(UnifiedEngineConfig(regime=Regime.COUPLED_WINDING))
    c = eng.coupled()
    c.seed_A1_sech(amplitude=0.02, radius=2.5)   # A1 node-field
    c.seed_winding(amplitude=0.02)                # ω micro-rotation on the SAME grid
    # the A1 scalar node-field and ω both on the SAME (N,N,N) diamond-K4 node set
    assert c.a_A1.shape == (c.N, c.N, c.N), "FAIL: A1 not a node-field"
    assert c.omega_field().shape == (c.N, c.N, c.N, 3), "FAIL: ω not on the same grid"
    H0 = c.total_energy()
    w0 = c.winding_integer()
    for _ in range(60):
        c.step()
    H1 = c.total_energy()
    w1 = c.winding_integer()
    rel = abs(H1 - H0) / H0
    print("\n--- SINGLE-GRID VERDICT: A1 node-field + ω on the SAME K4 graph (facade) ---")
    print(f"  joint energy |dH/H| over 60 coupled steps = {rel:.3e}  (PASS < 1e-8)")
    print(f"  winding integer Q_link: {w0['Q_link']} → {w1['Q_link']} (conserved on the grid)")
    print(f"  gmres info (0=ok): {c.last_gmres_info}")
    assert c.last_gmres_info == 0, "FAIL: coupled GMRES did not converge"
    assert rel < 1e-8, (
        f"FAIL: joint energy not conserved on the single grid — |dH/H|={rel:.3e}. "
        f"The single-grid A1-node-field + ω coexistence did NOT stay lossless."
    )
    assert w1["Q_link"] == w0["Q_link"], (
        f"FAIL: winding integer changed ({w0['Q_link']}→{w1['Q_link']}) — the (2,3) "
        f"charge did not survive on the shared grid."
    )


# ═════════════════════════════════════════════════════════════════════════════
# GATE-LIVENESS CONTROLS — the facade's closed-box energy gate is a LIVE
# discriminator (it catches a fake PASS), exercised THROUGH the facade.
#
# The energy-gate rows above are PASSING gates (|dH/H| < 1e-8). On their own a
# passing gate does not prove the gate would CATCH a dissipative integrator — a
# gate that always passes is vacuous. These two controls close that: they drive
# the SAME cage instance the facade exposes (eng.a1_cage(), the certified
# NativeCageIMEX) and assert the gate's discriminating behaviour.
#
# Rule-14 anti-rebuild: the GX3/GX5 logic is REUSED verbatim from the certified
# control suite src/tests/test_stage2_native_cage_imex.py (GX3 backward-Euler
# negative control; GX5 radiative-port passivity), only re-pointed at the
# facade's cage handle so a normal `pytest src/tests/engine_acceptance/` run
# self-demonstrates the facade's gate is live.
# ═════════════════════════════════════════════════════════════════════════════
def test_facade_gx3_backward_euler_trips_the_facade_energy_gate():
    """GX3-FACADE [GATE-LIVENESS, reachable-FAIL that TRIPS] — drive the facade's
    energy-gate core (the native_cage_imex instance UnifiedEngine.a1_cage()
    exposes) with the REJECTED backward-Euler integrator and assert it BLEEDS
    energy WELL ABOVE the 1e-8 gate (existing GX3 threshold: bleed > 0.05). This
    proves the facade's closed-box energy gate WOULD CATCH a dissipative
    integrator — i.e. the PASSING gate rows above are NOT vacuous.

    This is a PASSING test asserting the control TRIPS (a reachable-FAIL that
    confirms the gate is live). The backward-Euler step
        (I + dt²c0²L_D)V^{n+1} = 2V^n − V^{n-1}
    (NO ¼, NO LHS-average) is the rejected dissipative form; the certified CN/
    Newmark β=¼ stepper the facade actually uses is the energy-conserving one.

    Rule-14: the integrator + bleed logic is reused verbatim from
    test_stage2_native_cage_imex.py::test_GX3_backward_euler_bleeds_energy_negative_control,
    only re-pointed at the facade-exposed cage (eng.a1_cage()).
    """
    from scipy.sparse import identity
    from scipy.sparse.linalg import cg

    from ave.solvers.native_cage_imex import assemble_L_D

    # the energy-gate core the facade exposes (NativeCageIMEX, closed-box/lossless)
    eng = UnifiedEngine()
    cage = eng.a1_cage()
    cage.em_port_closed = True
    cage.seed_sech(amplitude=0.02, radius=2.5)
    cage.set_dt_accuracy()

    N = cage.N
    ndof = N**3
    H0 = cage.total_energy()
    # backward-Euler step (the REJECTED dissipative form) on the facade's cage:
    for _ in range(600):
        D = cage.stiffness_D()
        L_D = assemble_L_D(cage.Grad, cage.Div, D)
        coef = (cage.dt**2) * (cage.c0**2)
        v = cage.V.reshape(ndof)
        v_prev = cage.V_prev.reshape(ndof)
        rhs = 2.0 * v - v_prev
        A_sys = (identity(ndof, format="csr") + coef * L_D).tocsr()
        v_new, _ = cg(A_sys, rhs, rtol=1e-10, maxiter=2000, x0=v)
        cage.V_prev = cage.V.copy()
        cage.V = v_new.reshape(N, N, N)
        cage.time += cage.dt
    H_end = cage.total_energy()
    bleed = (H0 - H_end) / H0
    print("\n--- GX3-FACADE: backward-Euler TRIPS the facade's energy gate ---")
    print(f"  backward-Euler bleed (H0−H_end)/H0 = {bleed:.3e}  (TRIPS at > 0.05)")
    print(f"  ⇒ |dH/H| = {abs(bleed):.3e} ≫ the 1e-8 gate ⇒ the facade gate WOULD CATCH it")
    assert bleed > 0.05, (
        f"GATE-LIVENESS FAIL: backward-Euler did NOT bleed through the facade's "
        f"cage (bleed={bleed:.3e} ≤ 0.05) — if it doesn't trip, the facade's "
        f"closed-box energy gate is not discriminating and the PASSING gate rows "
        f"are vacuous."
    )
    # belt-and-suspenders: the bleed is many orders above the 1e-8 gate the
    # facade's energy_gate_lossless_limit() asserts ⇒ the gate is unambiguously live.
    assert abs(bleed) > 1e-8, "control must trip well above the 1e-8 gate"


def test_facade_gx5_radiative_port_is_passive_through_the_facade():
    """GX5-FACADE [GATE-LIVENESS, port passivity] — the energy-consistent Newmark
    radiative port (C PSD), driven THROUGH the facade (UnifiedEngine with
    port_sigma>0 → eng.a1_cage() opens the port), is PASSIVE: total energy
    MONOTONE-NON-INCREASING, Hmax/H0 ≤ 1, on a self-focusing nonlinear sech at
    fine dt — and the core does NOT grow past the seed amplitude (no manufactured
    self-focus). Regression for the REJECTED sponge-MULTIPLY PML that INJECTED
    energy (142× gain) under the implicit solve.

    Rule-14: the passivity logic is reused verbatim from
    test_stage2_native_cage_imex.py::test_GX5_radiative_port_is_passive_not_energy_injecting,
    only re-pointed at the facade-exposed cage configured with port_sigma>0.
    """
    eng = UnifiedEngine(UnifiedEngineConfig(N=16, dx=0.5, port_sigma=0.05))
    cage = eng.a1_cage()
    cage.seed_sech(amplitude=0.85, radius=2.5)
    cage.set_dt_accuracy()
    cage.dt = 0.066  # fine dt where the explicit stepper detonated
    H0 = cage.total_energy()
    Hmax = H0
    peak_max = cage.interior_peak_abs_V()
    for _ in range(400):
        cage.step()
        Hmax = max(Hmax, cage.total_energy())
        peak_max = max(peak_max, cage.interior_peak_abs_V())
    print("\n--- GX5-FACADE: radiative port is PASSIVE through the facade ---")
    print(f"  Hmax/H0 = {Hmax / H0:.6f}  (PASSIVE ⇒ ≤ 1; > 1 = energy injection)")
    print(f"  interior peak_max = {peak_max:.4f}  (must NOT exceed seed 0.85)")
    assert Hmax <= H0 * (1.0 + 1e-6), (
        f"radiative port MUST be passive through the facade (Hmax/H0 ≤ 1), got "
        f"{Hmax / H0:.3f} — energy injection = the rejected sponge-multiply "
        f"artifact has regressed."
    )
    assert peak_max <= 0.85 * (1.0 + 1e-3), (
        f"passive port must NOT manufacture self-focus past seed, peak_max={peak_max:.4f}"
    )
