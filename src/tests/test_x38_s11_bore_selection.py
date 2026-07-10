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
# The argmin -> branch (ii); s-sweep robustness
# ═════════════════════════════════════════════════════════════════════════════
def test_all_three_objectives_select_point_junction():
    """f* = 0 (point junction) under obj-1 (Op6), obj-2 (band-int), obj-3 (single-freq)."""
    for name in js.OBJECTIVES:
        assert js.argmin_bore(name).f_star == pytest.approx(0.0, abs=1e-9)


def test_objective_spread_is_robust_branch_ii():
    """At s=1 the three objectives agree exactly (spread 0) -> robust -> branch (ii)."""
    sp = js.objective_spread()
    assert sp["spread"] < x38.G_C_ROBUST_SPREAD
    assert sp["f_stars"]["obj1_op6"] == pytest.approx(0.0, abs=1e-9)


def test_primary_op6_f_star_is_zero_across_s_grid():
    """The PRIMARY objective (obj-1 Op6) gives f*=0 for EVERY (s_L,s_C) in [0.3,3]^2;
    any nonzero worst-case f* (comparator obj-2 float-tie on its flat plateau) stays
    below the robust threshold (X37 R5 shape-factor honesty)."""
    sweep = x38.s_sweep()
    for row in sweep["rows"]:
        assert row["f_star_op6"] == pytest.approx(0.0, abs=1e-9)
    assert sweep["worst_f_star"] < x38.G_C_ROBUST_SPREAD  # <0.02 -> still robust
    assert sweep["max_spread"] < x38.G_C_ROBUST_SPREAD


def test_obj1_near_degenerate_interior_dip_does_not_beat_f0():
    """HONEST disclosure (visible in the figure): obj-1 has a near-degenerate interior
    local minimum (~f=0.45) that comes within ~1e-7 of the f=0 floor but does NOT beat
    it, and sits BEYOND f_crit (self-invalidated regime) -> not a physical competitor;
    f*=0 stands."""
    nd = x38.near_degeneracy_disclosure()
    assert nd["interior_beats_f0"] is False
    assert nd["interior_minus_floor"] > 0.0
    assert nd["best_interior_beyond_f_crit"] is True  # the dip is at f > f_crit


def test_f_star_below_f_crit_does_not_self_invalidate():
    """f*=0 < f_crit~0.184 -> the lumped abstraction is self-consistent at its minimum."""
    assert js.argmin_bore("obj1_op6").f_star < x38.F_CRIT


def test_f_star_matches_neither_soliton_mark():
    """f*=0 matches NEITHER 1/(2pi) nor 1 -> branch (i) identity candidate does NOT fire."""
    f_star = js.argmin_bore("obj1_op6").f_star
    assert abs(f_star - x38.TUBE_RADIUS_MARK) >= 0.02
    assert abs(f_star - x38.CORE_THICKNESS_MARK) >= 0.02


def test_g_scalar_ceiling_recovers_pi_sqrt3_via_loaded_path():
    """The loaded connected-band top (ported X37 loaded-mu form) recovers pi*sqrt3 as
    f->0 — the X37/#604 ceiling, through the loaded path (cross-check of the parasitics)."""
    assert x38._g_scalar_loaded(1e-5) == pytest.approx(np.pi * np.sqrt(3.0), rel=1e-4)


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
    assert x38.gate_A()["pass"] is True


def test_gate_A_planted_symbol_and_literal_both_fire():
    """G-D: OMEGA_C by SYMBOL and by NUMERIC LITERAL must both be flagged."""
    from ave.core.constants import OMEGA_C

    sym = x38.scan_forbidden_inputs("from ave.core.constants import OMEGA_C\ndef e(f):\n    return OMEGA_C\n")
    assert sym["name_hits"] and sym["import_hits"]
    lit = x38.scan_forbidden_inputs(f"def e(f):\n    return {OMEGA_C!r} * f\n")
    assert lit["literal_hits"]
    assert x38.gate_A_planted()["pass"] is True


def test_gate_B_recovers_both_baselines_through_loaded_path():
    """G-B: loaded path recovers bare |S11|=1/3 AND the pi*sqrt3 ceiling (both within tol)."""
    gB = x38.gate_B()
    assert gB["bare_rel_error"] < x38.G_B_TOL
    assert gB["ceiling_rel_error"] < x38.G_B_TOL
    assert gB["pass"]


def test_gate_B_planted_offset_fires():
    """G-D: a +1% offset on both loaded recoveries FAILS the tolerance (gate fires)."""
    assert x38.gate_B_planted()["pass"]


def test_gate_C_reports_branch_and_spread():
    """G-C: the three objectives + spread + frozen branch assignment; branch (ii) at s=1."""
    gC = x38.gate_C()
    assert gC["branch_fired"] == "ii"
    assert gC["spread"] < x38.G_C_ROBUST_SPREAD


def test_gate_C_planted_divergent_objective_fires_scatter_detector():
    """G-D: a DIVERGENT bogus objective (maximise reflection -> f!=0) pushes the spread
    across the scatter threshold; the 3 real objectives (control) do NOT. Proves the
    branch-(iv) detector can fire."""
    gp = x38.gate_C_planted()
    assert gp["control_flagged_scatter"] is False  # real objectives agree
    assert gp["planted_flagged_scatter"] is True  # divergent plant flagged
    assert gp["pass"] is True


def test_all_gates_pass_end_to_end():
    """G-D roll-up: every gate + planted proof passes when the driver runs its gate suite."""
    gates = [x38.gate_A(), x38.gate_A_planted(), x38.gate_B(), x38.gate_B_planted(), x38.gate_C(), x38.gate_C_planted()]
    assert all(g["pass"] for g in gates)
