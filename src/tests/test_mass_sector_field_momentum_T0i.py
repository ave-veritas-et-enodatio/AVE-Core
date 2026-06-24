"""Regression: mass-sector field-momentum T^{0i} = (∂_t V)(∂_i V) readout.

Locks the two load-bearing invariants of the §390 R3 false-null hatch
(`research/2026-06-23_mass-sector-two-body-scattering_T0i_result.md`):

  1. OBSERVABLE-SOUND: an isolated stationary breather centered on the true grid
     center (XC = (N−1)/2) carries EXACTLY zero net field-momentum (P_total = 0).
     This is the momentum-conservation sanity check a T^{0i} readout lives or
     dies by; it also pins the half-integer-centering fix (integer N//2 centering
     gives a spurious nonzero P_total — the bug this test guards against).

  2. PASS / FM-DIFFRACTION signature: a head-on b=0 symmetric two-body pair shows
     (a) symmetry-forced zero TRANSPORTED flux Φ_x, and (b) phase-DEPENDENT,
     AC-dominated DELIVERED-momentum imbalance dP=(P_L−P_R) — i.e. generic-soliton
     breathing interference, NOT a phase-independent DC momentum-transport pull.
     This is the substrate-native confirmation that gravity is FREQUENCY
     MODULATION / diffraction, not a stress-tensor pull
     (optical-refraction-gravity.md:17).
"""

import importlib.util
import os

import numpy as np

_DRIVER = os.path.join(
    os.path.dirname(__file__),
    "..", "scripts", "vol_1_foundations", "mass_sector_field_momentum_T0i.py",
)


def _load():
    spec = importlib.util.spec_from_file_location("t0i_driver", os.path.abspath(_DRIVER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_isolated_blob_carries_zero_net_momentum():
    """Invariant 1 — a stationary breather at the true grid center XC has P_total=0.

    Guards the half-integer-centering fix: integer N//2 centering would give a
    spurious P_total ~ +20 (the discretization bias). At XC=(N−1)/2 the discrete
    field is exactly mirror-symmetric, so T^{0x} is exactly odd and integrates to 0.
    """
    m = _load()
    eng = m._make_engine()
    m._seed_breather(eng, m.XC, +1.0)  # dead center, true grid center
    eng.V_prev = eng.V.copy()
    for _ in range(50):
        eng.step()
    mi = m.momentum_integrals(eng.V, eng.V_prev, eng.dt)
    # exact zero to floating-point round-off (the field is bit-symmetric about XC)
    assert abs(mi["p_total"]) < 1e-9, f"isolated blob P_total not conserved: {mi['p_total']}"
    assert abs(mi["phi_midplane"]) < 1e-9, f"isolated blob Φ_x not zero: {mi['phi_midplane']}"


def test_known_motion_registers_nonzero_momentum():
    """Observable is not trivially zero: a blob with imposed +x velocity registers
    nonzero P_total (the field-momentum readout responds to real bulk motion)."""
    m = _load()
    eng = m._make_engine()
    m._seed_breather(eng, m.XC, +1.0)
    Vp = np.zeros_like(eng.V)
    Vp[1:, :, :] = eng.V[:-1, :, :]  # V_prev = V shifted +x -> imposed velocity
    eng.V_prev = Vp
    mi = m.momentum_integrals(eng.V, eng.V_prev, eng.dt)
    assert abs(mi["p_total"]) > 1.0, (
        f"observable failed to register imposed motion: P_total={mi['p_total']}"
    )


def test_two_body_pass_fm_diffraction_signature():
    """Invariant 2 — symmetric head-on pair gives the PASS/FM-DIFFRACTION signature:
    transported flux Φ_x symmetry-zero + phase-DEPENDENT, AC-dominated dP."""
    m = _load()
    d0 = 8
    ctrl = m.run_single_blob_control(d0)
    in_res = m.run_two_body(d0, "in")
    out_res = m.run_two_body(d0, "out")

    # (a) transported flux is symmetry-forced zero at both phases
    assert abs(in_res["phi_midplane_net"]) < 1e-9
    assert abs(out_res["phi_midplane_net"]) < 1e-9
    # P_total conserved (exact) at both phases
    assert in_res["p_total_stats"]["abs_mean"] < 1e-9
    assert out_res["p_total_stats"]["abs_mean"] < 1e-9

    # (b) delivered-momentum imbalance dP is phase-DEPENDENT (in >> out) and
    #     AC-dominated (ac/dc > 1) -> generic-soliton breathing, NOT a DC pull
    assert abs(in_res["dP_net"]) > 3.0 * abs(out_res["dP_net"]), (
        "dP is not phase-dependent -> would indicate a phase-independent pull "
        f"(in={in_res['dP_net']}, out={out_res['dP_net']})"
    )
    assert in_res["dP_ac_dc"] > 1.0, (
        f"dP is DC-sustained (ac/dc={in_res['dP_ac_dc']}<1) -> a real pull, "
        "which would OVERTURN the FM/diffraction picture"
    )

    bin_name, _ = m.classify(in_res, out_res, ctrl)
    assert bin_name == "PASS / FM-DIFFRACTION", f"unexpected verdict: {bin_name}"
