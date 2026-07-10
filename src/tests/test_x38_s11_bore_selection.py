"""X38 tests — S₁₁-minimization bore selection.

Covers: the exact symmetric-junction S₁₁ + bare Gamma=-1/3, the canonical Op6
objective (via the canonical code path), the L-match confirm/refute, the small-θ
monotone-reflection expansion, the argmin -> branch (ii), the s-sweep robustness,
and the four gates (G-A/B/C/D) each with a planted-violation proof.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

from ave.core import junction_scattering as js
from ave.core.universal_operators import universal_eigenvalue_target

# ── import the driver module by path (it lives under src/scripts, not a package) ──
_DRIVER_PATH = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations" / "x38_s11_bore_selection.py"
_spec = importlib.util.spec_from_file_location("x38_driver", _DRIVER_PATH)
x38 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(x38)


# ═════════════════════════════════════════════════════════════════════════════
# The exact S₁₁ + the bare-junction baseline (analytic)
# ═════════════════════════════════════════════════════════════════════════════
def test_bare_junction_S11_is_minus_one_third():
    """z=3 star: incident sees Z0/2 -> Gamma = (2-z)/z = -1/3 (memoryless NOT matched)."""
    assert js.bare_junction_s11(3) == pytest.approx(-1.0 / 3.0)
    assert abs(js.bare_junction_s11(3)) == pytest.approx(1.0 / 3.0)


def test_bare_junction_general_coordination():
    """Gamma = (2-z)/z for any z; z=2 through-junction is matched (S11=0)."""
    assert js.bare_junction_s11(2) == pytest.approx(0.0)  # z=2: perfectly matched
    assert js.bare_junction_s11(4) == pytest.approx(-0.5)  # z=4


def test_loaded_S11_recovers_bare_at_f_zero():
    """The LOADED S11 -> bare (2-z)/z as f->0 (through the loaded path, no early return)."""
    for theta in (0.3, 1.0, np.pi):
        assert js.s11_junction(theta, 0.0, 1.0, 1.0) == pytest.approx(-1.0 / 3.0)
    # small nonzero f (loaded path exercised): still -> 1/3 as theta->0
    assert abs(js.s11_junction(1e-6, 1e-5)) == pytest.approx(1.0 / 3.0, abs=1e-6)


# ═════════════════════════════════════════════════════════════════════════════
# The canonical Op6 objective (uses canon's own universal_eigenvalue_target)
# ═════════════════════════════════════════════════════════════════════════════
def test_op6_uses_canonical_operator_and_equals_abs_S11_squared():
    """obj-1 goes through the canonical Op6 code path; for the 1x1 reflection block
    lambda_min(S†S) = |S11|^2 (faithful to the trefoil R.r=1/4 usage)."""
    for f in (0.0, 0.2, 0.5):
        s11 = js.s11_junction(np.pi, f)
        direct = abs(s11) ** 2
        via_operator = universal_eigenvalue_target(np.array([[s11]], dtype=complex))
        assert js.op6_lambda_min(np.pi, f) == pytest.approx(direct)
        assert js.op6_lambda_min(np.pi, f) == pytest.approx(via_operator)


def test_op6_reflectionless_target_is_unreachable():
    """min_theta |S11|^2 = 1/9 for ALL f (the theta->0 floor) — the reflectionless
    target lambda_min->0 is NEVER reached; the z=3 vertex is an intrinsic
    1/9-power branch-backscatterer."""
    for f in (0.0, 0.1, 0.3, 0.5):
        assert js.deepest_notch(f) == pytest.approx(1.0 / 9.0, abs=1e-6)


# ═════════════════════════════════════════════════════════════════════════════
# The L-match: CONFIRMED as a network fact, REFUTED at the physical vertex
# ═════════════════════════════════════════════════════════════════════════════
def test_l_match_ideal_null_is_reachable_Q_equals_one():
    """Q = sqrt(Z_hi/Z_lo - 1) = 1 for the 2:1 step; the ideal 2-element L-match with
    the CORRECT orientation (series toward the Z0/2 load + shunt on the HIGH/source
    side) nulls |S11|->0. This is the network fact the substrate topology CANNOT
    realize (test_physical_vertex_never_dips_below_one_third)."""
    Q = np.sqrt(2.0 / 1.0 - 1.0)
    assert Q == pytest.approx(1.0)
    Xse, Bsh = Q * 0.5, Q / 1.0  # normalized L-match element values
    z_series_load = 1j * Xse + 0.5  # series reactance toward the Z0/2 load
    y_in = 1.0 / z_series_load + 1j * Bsh  # shunt susceptance on the HIGH (source) side
    z_in = 1.0 / y_in
    assert abs((z_in - 1.0) / (z_in + 1.0)) == pytest.approx(0.0, abs=1e-9)  # perfect null


def test_physical_vertex_never_dips_below_one_third():
    """The substrate parasitic orientation (accumulator at the low-Z node, throat in
    the arms) is the step-DOWN L: it CANNOT raise Z0/2 to Z0. |S11| >= 1/3 for all
    theta, all f, all positive s -> the L-match dip is REFUTED at the vertex."""
    thetas = np.linspace(1e-4, 1.5 * np.pi, 2000)
    for f in (0.05, 0.1, 0.2, 0.3, 0.5):
        for s_L, s_C in ((1, 1), (0.3, 3), (3, 0.3), (2, 2)):
            assert np.min(np.abs(js.s11_junction(thetas, f, s_L, s_C))) >= 1.0 / 3.0 - 1e-9


def test_small_theta_expansion_matches_exact():
    """Analytic expansion |S11|^2 = (1/4 + b^2)/(9/4 + b^2),
    b = [(3/2)s_L - (1/4)s_C] f theta (z=3) — matches the exact S11 as theta->0."""
    theta = 1e-3
    for s_L, s_C, f in ((1, 1, 0.3), (0.3, 3, 0.3), (3, 0.3, 0.1), (2, 2, 0.2)):
        b = ((1.5 * s_L) - (0.25 * s_C)) * f * theta
        approx = np.sqrt((0.25 + b * b) / (2.25 + b * b))
        exact = abs(js.s11_junction(theta, f, s_L, s_C))
        assert exact == pytest.approx(approx, rel=1e-5)


# ═════════════════════════════════════════════════════════════════════════════
# TWO-AXIS verdict (R1): obj-1 EXACTLY degenerate; obj-2 uniquely f*=0
# ═════════════════════════════════════════════════════════════════════════════
def test_obj1_touches_one_ninth_exactly_at_half_wave_invisible_extent():
    """R1: |S11(pi;f)|^2 - 1/9 = 8 t^2 (s_C s_L^2 t^2 + s_C - 3 s_L)^2 / [...] (perfect
    square) => obj-1 touches 1/9 EXACTLY (machine zero) at f_touch = sqrt(3 s_L - s_C)/
    (pi sqrt(s_C) s_L). At s=1, f_touch = sqrt(2)/pi."""
    f_touch = js.half_wave_invisible_touch(np.pi, 1.0, 1.0)
    assert f_touch == pytest.approx(np.sqrt(2.0) / np.pi, rel=1e-12)
    assert js.objective_op6(f_touch) - 1.0 / 9.0 == pytest.approx(0.0, abs=1e-12)  # machine zero


def test_obj1_is_exactly_degenerate_obj2_is_not():
    """R1 two-axis: obj-1 (single-freq at pi) is EXACTLY degenerate {0, f_touch} at s=1
    (f_touch in domain); obj-2 (band-integrated) has NO half-wave touch -> not degenerate."""
    assert js.objective_is_degenerate("obj1_op6", 1.0, 1.0)["degenerate"] is True
    assert js.objective_is_degenerate("obj2_band_integrated", 1.0, 1.0)["degenerate"] is False


def test_obj3_touch_out_of_domain_at_s_equal_1():
    """R1: obj-3 (single-freq at pi/2) touch is at 2*f_touch = sqrt(2)*2/pi ~ 0.900,
    OUTSIDE [0,0.5] at s=1 -> obj-3 is not degenerate WITHIN the frozen domain there."""
    f_touch3 = js.half_wave_invisible_touch(np.pi / 2, 1.0, 1.0)
    assert f_touch3 == pytest.approx(2.0 * np.sqrt(2.0) / np.pi, rel=1e-12)
    assert f_touch3 > js.F_WIGNER_SEITZ
    assert js.objective_is_degenerate("obj3_single_freq", 1.0, 1.0)["degenerate"] is False


def test_band_integrated_uniquely_selects_point_junction():
    """R1 banked result: obj-2 (band-integrated, D4-fixed integration from theta=0)
    uniquely selects f*=0 — the ONLY objective that does so robustly."""
    assert js.argmin_bore("obj2_band_integrated").f_star == pytest.approx(0.0, abs=1e-9)
    assert js.objective_spread()["band_integrated_unique_f0"] is True


def test_two_axis_branch_verdict():
    """R1: frozen-primary (obj-1 degenerate) -> branch (iv); band-integrated (obj-2) ->
    branch (ii). KEEP BOTH."""
    verdict = x38.gate_C()["two_axis_verdict"]
    assert verdict["frozen_primary_branch"] == "iv"
    assert verdict["band_integrated_branch"] == "ii"
    assert verdict["primary_degenerate"] is True


def test_d4_obj2_no_integration_cutoff_systematic():
    """R8/D4: with the integration lower bound at theta=0 (not 1e-6), obj-2 has NO
    interior point below its f=0 value at the strong-accumulator cell (the old ~6e-10
    theta_top-cutoff systematic is gone)."""
    fs = np.linspace(0.0, 0.5, 501)
    j = np.array([js.objective_band_integrated(f, 1.0, 3.0) for f in fs])
    assert not np.any(j[1:] < j[0] - 1e-12)  # no interior value below the f=0 floor


# ═════════════════════════════════════════════════════════════════════════════
# s-sweep + the branch-(i) PENDING-GRANT locus (R2)
# ═════════════════════════════════════════════════════════════════════════════
def test_s_sweep_band_integrated_unique_and_branch_i_locus():
    """R2: obj-2 uniquely f*=0 at EVERY (s_L,s_C) cell; cell (2,3) puts the obj-1
    co-minimum f_touch = 1/(2pi) EXACTLY inside f_crit -> a branch-(i) PENDING-GRANT locus."""
    sweep = x38.s_sweep()
    assert sweep["band_integrated_uniquely_f0_all_cells"] is True
    loci = sweep["branch_i_pending_grant_loci"]
    assert any(abs(x["s_L"] - 2.0) < 1e-9 and abs(x["s_C"] - 3.0) < 1e-9 for x in loci)
    assert js.half_wave_invisible_touch(np.pi, 2.0, 3.0) == pytest.approx(1.0 / (2 * np.pi), rel=1e-12)


def test_cell_2_3_touch_inside_f_crit():
    """R2: at cell (2,3) the degenerate touch 1/(2pi)=0.159 is INSIDE f_crit=0.184."""
    assert js.half_wave_invisible_touch(np.pi, 2.0, 3.0) < x38.F_CRIT


# ═════════════════════════════════════════════════════════════════════════════
# The non-reciprocal escape (R3/R4) + reciprocity scoping
# ═════════════════════════════════════════════════════════════════════════════
def test_ideal_circulator_is_matched_lossless_c3_nonreciprocal():
    """R3/R4: matched lossless C3-symmetric 3-ports EXIST — but ONLY non-reciprocally.
    The ideal circulator is unitary (lossless), C3-symmetric (cyclic), NON-reciprocal
    (S != S^T), S11 = 0 (matched). The witness that the 1/3 floor is a RECIPROCITY
    result, so the evanescent-stub (lossless+reciprocal) escape is DEAD (R4)."""
    S = js.ideal_circulator_s_matrix()
    assert np.allclose(S.conj().T @ S, np.eye(3))  # unitary/lossless
    assert abs(S[0, 0]) == pytest.approx(0.0)  # matched
    assert not np.allclose(S, S.T)  # non-reciprocal
    P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)  # C3 cyclic
    assert np.allclose(P @ S @ np.linalg.inv(P), S)  # C3-symmetric


def test_reciprocal_vertex_floor_is_one_third():
    """R5: the classic matched-lossless-RECIPROCAL 3-port theorem — |S11| >= 1/3 for the
    symmetric vertex, confirmed at every f, s (provable via the deepest-notch = 1/9)."""
    for f in (0.05, 0.2, 0.5):
        for s_L, s_C in ((1, 1), (0.3, 3), (3, 0.3)):
            assert js.deepest_notch(f, s_L, s_C) == pytest.approx(1.0 / 9.0, abs=1e-6)


def test_g_scalar_ceiling_recovers_pi_sqrt3_via_canonical_routine():
    """R10: the pi*sqrt3 ceiling recovers as f->0 through the CANONICAL X37 routine
    jp.g_scalar (imported, #616 merged), NOT a re-implementation."""
    from ave.core import junction_parasitics as jp

    assert x38._g_scalar_loaded(1e-5) == pytest.approx(np.pi * np.sqrt(3.0), rel=1e-4)
    assert x38._g_scalar_loaded(0.2) == pytest.approx(jp.g_scalar(0.2), rel=1e-12)  # same routine


# ═════════════════════════════════════════════════════════════════════════════
# Gates + planted-violation proofs (G-A / G-B / G-C / G-D)
# ═════════════════════════════════════════════════════════════════════════════
def test_gate_A_extraction_module_imports_no_scale():
    """G-A: the S11 extraction module references no {OMEGA_C,M_E,L_CELL,C_CELL},
    imports no ave.core.constants, carries no forbidden numeric literal."""
    result = x38.scan_forbidden_inputs(Path(js.__file__).read_text())
    assert result["name_hits"] == []
    assert result["import_hits"] == []
    assert result["literal_hits"] == []
    assert x38.gate_A()["pass"]


def test_gate_A_planted_symbol_and_literal_both_fire():
    """G-D: OMEGA_C by SYMBOL and by NUMERIC LITERAL must both be flagged."""
    from ave.core.constants import OMEGA_C

    sym = x38.scan_forbidden_inputs("from ave.core.constants import OMEGA_C\ndef e(f):\n    return OMEGA_C\n")
    assert sym["name_hits"] and sym["import_hits"]
    lit = x38.scan_forbidden_inputs(f"def e(f):\n    return {OMEGA_C!r} * f\n")
    assert lit["literal_hits"]
    assert x38.gate_A_planted()["pass"]


def test_gate_B_memoryless_and_f_sensitive_legs():
    """G-B (R8): memoryless legs recover bare |S11|=1/3 AND pi*sqrt3; the f-SENSITIVE
    active legs confirm the parasitics actually bite (a disabled path would not move)."""
    gB = x38.gate_B()
    assert gB["bare_rel_error"] < x38.G_B_TOL
    assert gB["ceiling_rel_error"] < x38.G_B_TOL
    assert gB["bare_leg_f_sensitive"] is True  # |S11(pi,0.2)| rises above 1/3
    assert gB["ceiling_leg_f_sensitive"] is True  # g(0.2) drops below pi*sqrt3
    assert gB["pass"]


def test_gate_B_planted_offset_and_sabotage_fire():
    """G-D (R8): (a) a +1% offset fails the reference tolerance; (b) a PARASITICS-
    DISABLED sabotage (memoryless values for all f) FAILS the f-sensitive active legs —
    the sabotage the old f->0-only gate passed spuriously."""
    gp = x38.gate_B_planted()
    assert gp["offset_gate_fires"] is True
    assert gp["sabotage_bare_leg_f_sensitive"] is False  # disabled -> no movement
    assert gp["sabotage_ceiling_leg_f_sensitive"] is False
    assert gp["sabotage_gate_fires"] is True
    assert gp["pass"]


def test_gate_C_reports_two_axis_verdict():
    """G-C (R1): two-axis — frozen-primary (obj-1 degenerate) branch (iv); band-
    integrated (obj-2) branch (ii)."""
    gC = x38.gate_C()
    assert gC["two_axis_verdict"]["frozen_primary_branch"] == "iv"
    assert gC["two_axis_verdict"]["band_integrated_branch"] == "ii"
    assert gC["primary_degenerate"] is True


def test_gate_C_planted_degeneracy_and_scatter_detectors_fire():
    """G-D (R1): (a) the exact-degeneracy detector fires (obj-1 touches 1/9 at f_touch,
    obj-2 does not); (b) a divergent bogus objective fires the scatter detector; the 3
    real objectives (control) do not."""
    gp = x38.gate_C_planted()
    assert gp["degeneracy_detector_fires"] is True
    assert gp["scatter_detector_fires"] is True
    assert gp["pass"]


def test_all_gates_pass_end_to_end():
    """G-D roll-up: every gate + planted proof passes when the driver runs its gate suite."""
    gates = [x38.gate_A(), x38.gate_A_planted(), x38.gate_B(), x38.gate_B_planted(), x38.gate_C(), x38.gate_C_planted()]
    assert all(g["pass"] for g in gates)
