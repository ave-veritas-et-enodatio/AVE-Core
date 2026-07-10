"""X37 — junction-parasitic extraction gates + planted-violation proofs.

Machine-checkable versions of the four pre-registered gates (prereg §6):
  G-A anti-install (AST scan of the extraction path) + planted OMEGA_C fires it,
  G-B independent-reference recovery vs the FROZEN #604 top + planted offset fires it,
  G-C vertex-extent honesty (extent-dominated swing -> branch iii) + planted detector,
  G-D gates-can-fire (every planted violation fires; a no-op control does not).

Prereg (FROZEN): research/2026-07-10_x37-junction-parasitics_prereg_FROZEN.md
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

from ave.core import junction_parasitics as jp

# ── import the driver module by path (it lives under src/scripts, not a package) ──
_DRIVER_PATH = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations" / "x37_junction_parasitics.py"
_spec = importlib.util.spec_from_file_location("x37_driver", _DRIVER_PATH)
x37 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(x37)

PI_SQRT3 = np.pi * np.sqrt(3.0)


# ─────────────────────────────────────────────────────────────────────────────
# G-A — anti-install (the #613 lesson)
# ─────────────────────────────────────────────────────────────────────────────
def test_gate_A_extraction_module_imports_no_scale():
    """The extraction path (ave.core.junction_parasitics) must reference NONE of
    {OMEGA_C, M_E, L_CELL, C_CELL}, import no ave.core.constants, and carry no
    forbidden numeric literal (review R8)."""
    result = x37.gate_A()
    assert result["pass"], result
    assert result["name_hits"] == []
    assert result["import_hits"] == []
    assert result["literal_hits"] == []


def test_gate_A_planted_violation_fires():
    """Planting OMEGA_C by SYMBOL and by NUMERIC LITERAL must both be flagged
    (review R8: the symbol scan alone is blind to a hard-coded value)."""
    result = x37.gate_A_planted()
    assert result["gate_fired"], result
    assert result["literal_hits"]  # the numeric-literal plant fired


def test_gate_A_numeric_literal_scan_fires():
    """A hard-coded omega_C magnitude in an extraction body must be flagged (R8).
    Built from the imported symbol so this test carries no magic number."""
    from ave.core.constants import OMEGA_C

    hits = x37.scan_forbidden_inputs(f"def e(f):\n    return {OMEGA_C!r} * f\n")
    assert any("OMEGA_C" in h for h in hits["literal_hits"])


def test_gate_A_scanner_ignores_docstrings():
    """The AST scanner must NOT false-positive on a forbidden token that appears
    only in a docstring/comment (the extraction module's own FORBIDDEN warning)."""
    src = '"""mentions OMEGA_C and M_E in prose only."""\nx = 1.0\n'
    hits = x37.scan_forbidden_inputs(src)
    assert hits["name_hits"] == []
    assert hits["import_hits"] == []
    assert hits["literal_hits"] == []


# ─────────────────────────────────────────────────────────────────────────────
# G-B — independent-reference recovery vs FROZEN #604 (review R3: exercise the
# LOADED solver at small nonzero f, not the memoryless early-return)
# ─────────────────────────────────────────────────────────────────────────────
def test_gate_B_loaded_solver_converges_to_604():
    """The LOADED dispersion solver at small nonzero f must converge to the #604
    top pi*sqrt3 within the stated tolerance — the solver is genuinely exercised
    (band_ceiling_diagnosis runs the coarse+fine crossing scan, no early return)."""
    result = x37.gate_B()
    assert result["pass"], result
    assert result["loaded_solver_probe_f"] > 0.0  # NOT the f=0 early return
    assert result["rel_error"] < result["tol"]
    # the memoryless identity is still exact, recorded separately
    assert np.isclose(result["memoryless_identity_f0_over_omega_C"], PI_SQRT3, rtol=0, atol=1e-9)


def test_gate_B_planted_violation_fires():
    """A +1% offset loaded-solver output MUST fail the convergence tolerance."""
    result = x37.gate_B_planted()
    assert result["gate_fired"], result
    assert result["rel_error"] >= result["tol"]


# ─────────────────────────────────────────────────────────────────────────────
# G-C — vertex-extent honesty + branch assignment
# ─────────────────────────────────────────────────────────────────────────────
def test_gate_C_extent_dominated_branch_iii():
    """With the equivalent-length normalization the ceiling swings ~31% over
    f in [0, 0.5] (>> 10% threshold) -> branch (iii): not closable at TL level."""
    result = x37.gate_C(1.0, 1.0)
    assert result["swing_over_pi_sqrt3"] > x37.BRANCH_III_SWING
    assert result["branch_fired"] == "iii"


def test_gate_C_planted_detector_discriminates():
    """The extent-dominated detector must NOT flag a flat (f-independent) ceiling
    and MUST flag the real f-dependent one (proves it can fire and does not misfire)."""
    result = x37.gate_C_planted()
    assert result["gate_fired"], result
    assert not result["flat_flagged_extent_dominated"]
    assert result["real_flagged_extent_dominated"]


# ─────────────────────────────────────────────────────────────────────────────
# Physics of the extraction (topology class, monotonicity, resonance)
# ─────────────────────────────────────────────────────────────────────────────
def test_topology_class_is_reactive_low_pass():
    """Both accumulator and throat LOWER the ceiling -> reactive low-pass; the
    parasitic must not LIFT (no parallel-bypass) at any physical extent."""
    for f in (0.05, 0.1, 0.2, 0.3, 0.5):
        assert "low-pass" in jp.topology_class(f, 1.0, 1.0)
        assert jp.g_scalar(f, 1.0, 1.0) < PI_SQRT3  # never lifts


def test_ceiling_monotone_decreasing_in_extent():
    """The connected-band ceiling decreases monotonically with the extent fraction."""
    fs = np.linspace(0.0, 0.5, 21)
    g = np.array([jp.g_scalar(f, 1.0, 1.0) for f in fs])
    assert np.all(np.diff(g) <= 1e-9)


def test_pure_shunt_and_pure_series_both_lower():
    """Isolating each channel: pure shunt-C and pure series-L each lower the
    ceiling (any reactive store slows the network)."""
    assert jp.g_scalar(0.3, 0.0, 1.0) < PI_SQRT3  # pure accumulator
    assert jp.g_scalar(0.3, 1.0, 0.0) < PI_SQRT3  # pure throat


def test_junction_self_resonance_ratio():
    """omega_vertex/omega_C = 1/(sqrt(s_L s_C) f) — pure geometry, no scale."""
    for f in (0.1, 0.2, 0.5):
        vc = jp.extract_vertex_circuit(f, 1.0, 1.0)
        assert np.isclose(vc.omega_vertex_over_omega_C, 1.0 / f)


def test_single_channel_anchor_matches_exact():
    """The single-channel anchor g = pi*sqrt3(1 - kappa f) agrees with the exact
    solve for a PURE channel (pure shunt-C or pure series-L), validating the
    local-mu linearization kappa = s_L + (2/3) s_C (derivation §4)."""
    for f in (0.01, 0.05):
        assert np.isclose(jp.g_scalar(f, 0.0, 1.0), jp.g_scalar_linear(f, 0.0, 1.0), rtol=5e-3)  # pure shunt
        assert np.isclose(jp.g_scalar(f, 1.0, 0.0), jp.g_scalar_linear(f, 1.0, 0.0), rtol=5e-3)  # pure series


def test_shunt_has_exactly_zero_effect_at_s_equal_1():
    """Review R4 (reciprocity identity): at s_L=s_C=1 the combined ceiling EQUALS
    the pure-throat ceiling EXACTLY on every g(f) — the shunt accumulator has ZERO
    effect. This is stronger than 'tracks the stronger channel'."""
    fs = np.linspace(0.02, 0.5, 13)
    for f in fs:
        assert np.isclose(jp.g_scalar(f, 1.0, 1.0), jp.g_scalar(f, 1.0, 0.0), rtol=0, atol=1e-9)


def test_additive_anchor_over_predicts_combined_drop():
    """The naive sum-of-drops anchor badly over-predicts the combined drop
    (the shunt drop is not added — R4)."""
    f = 0.2
    g_shunt, g_series, g_both = jp.g_scalar(f, 0.0, 1.0), jp.g_scalar(f, 1.0, 0.0), jp.g_scalar(f, 1.0, 1.0)
    additive = PI_SQRT3 - ((PI_SQRT3 - g_shunt) + (PI_SQRT3 - g_series))
    assert g_both > additive + 0.1


# ─────────────────────────────────────────────────────────────────────────────
# Review R3 — the detector CAN report a lift (instrument no longer blind)
# ─────────────────────────────────────────────────────────────────────────────
def test_lift_is_reachable_for_nonpassive_loading():
    """A NEGATIVE-reactance (non-passive) loading lifts the ceiling above memoryless
    and MUST be reported as a lift/bypass — the old [0,pi]-clipped detector could
    only ever say 'transparent'."""
    passive = jp.band_ceiling_diagnosis(0.2, 1.0, 1.0)
    lift = jp.band_ceiling_diagnosis(0.2, -1.0, -1.0)
    assert passive["status"] == "low-pass"
    assert lift["status"] == "lift"
    assert jp.g_scalar(0.2, -1.0, -1.0) > PI_SQRT3
    assert "bypass" in jp.topology_class(0.2, -1.0, -1.0)


def test_resolution_guard_small_f_not_false_lift():
    """Review R3: a razor-thin, ultra-shallow small-f zone-edge dip must resolve to
    a (negligible) low-pass drop, NEVER a silent 'no-crossing/lift'."""
    for f in (1e-3, 1e-4, 1e-5):
        d = jp.band_ceiling_diagnosis(f, 1.0, 1.0)
        assert d["status"] in ("low-pass", "transparent"), (f, d)
        assert jp.g_scalar(f, 1.0, 1.0) <= PI_SQRT3 + 1e-9
        assert jp.g_scalar(f, 1.0, 1.0) > PI_SQRT3 - 0.1  # tiny drop, near memoryless


# ─────────────────────────────────────────────────────────────────────────────
# Review R2 — the 1D two-node closed-form cross-check (prereg §3.4 promise)
# ─────────────────────────────────────────────────────────────────────────────
def test_1d_closed_form_memoryless_top():
    """1D loaded line f=0 recovers the memoryless 1D top theta=pi (g_1d = pi, no
    sqrt(3) network factor)."""
    assert np.isclose(jp.band_top_1d(0.0), np.pi, rtol=0, atol=1e-9)


def test_1d_closed_form_lowers_and_cross_checks_srs():
    """The 1D closed-form cross-check shows the SAME qualitative physics as the srs
    numerics: both channels lower the top; combined tracks the stronger channel."""
    assert jp.band_top_1d(0.2, 1.0, 1.0) < np.pi  # loading lowers the 1D top
    assert jp.band_top_1d(0.2, 0.0, 1.0) < np.pi  # pure shunt lowers
    assert jp.band_top_1d(0.2, 1.0, 0.0) < np.pi  # pure series lowers


# ─────────────────────────────────────────────────────────────────────────────
# Review R5 — the ceiling floor is DOUBLY conditional (f<=0.5 AND s=1)
# ─────────────────────────────────────────────────────────────────────────────
def test_shape_factor_bracket_is_doubly_conditional():
    """Over s in [0.3,3]^2 the g(0.5) bracket floor drops well below the s=1 value
    (3.73) — the reported number is conditional on BOTH f<=0.5 AND s=1."""
    b = x37.shape_factor_bracket()
    assert b["g_min"] < 2.5  # floor reaches ~2.1
    assert b["g_min"] < jp.g_scalar(0.5, 1.0, 1.0)  # below the s=1 value


@pytest.mark.parametrize("f", [0.0, 0.1, 0.25, 0.5])
def test_g_scalar_is_order_unity_times_reference(f):
    """FORM check (M6): g = O(1) * (memoryless scale). No 'ceiling near omega_C'
    credit — the value is bounded O(1), as dimensional analysis forces."""
    g = jp.g_scalar(f, 1.0, 1.0)
    assert 0.5 * PI_SQRT3 <= g <= PI_SQRT3 + 1e-9
