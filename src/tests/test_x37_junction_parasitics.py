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
    {OMEGA_C, M_E, L_CELL, C_CELL} and must not import ave.core.constants."""
    result = x37.gate_A()
    assert result["pass"], result
    assert result["name_hits"] == []
    assert result["import_hits"] == []


def test_gate_A_planted_violation_fires():
    """Planting OMEGA_C into an extraction body MUST be flagged (gate can fire)."""
    result = x37.gate_A_planted()
    assert result["gate_fired"], result
    assert "OMEGA_C" in result["name_hits"]


def test_gate_A_scanner_ignores_docstrings():
    """The AST scanner must NOT false-positive on a forbidden token that appears
    only in a docstring/comment (the extraction module's own FORBIDDEN warning)."""
    src = '"""mentions OMEGA_C and M_E in prose only."""\nx = 1.0\n'
    hits = x37.scan_forbidden_inputs(src)
    assert hits["name_hits"] == []
    assert hits["import_hits"] == []


# ─────────────────────────────────────────────────────────────────────────────
# G-B — independent-reference recovery vs FROZEN #604
# ─────────────────────────────────────────────────────────────────────────────
def test_gate_B_recovers_604_memoryless_top():
    """f->0 must recover the #604 top pi*sqrt3 within 1e-3."""
    result = x37.gate_B()
    assert result["pass"], result
    assert result["rel_error"] < x37.G_B_TOL
    assert np.isclose(jp.g_scalar(0.0), PI_SQRT3, rtol=0, atol=1e-9)


def test_gate_B_planted_violation_fires():
    """A +1% offset f->0 limit MUST fail the recovery tolerance (gate can fire)."""
    result = x37.gate_B_planted()
    assert result["gate_fired"], result
    assert result["rel_error"] >= x37.G_B_TOL


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


def test_combined_channel_is_non_additive():
    """Driver-time finding (§4a): the combined connected-band ceiling is NOT the
    sum of the two channel drops — it tracks the STRONGER (series) channel, because
    the re-entrant zone-edge gap (s_C>0) absorbs the shunt contribution above the
    first mu=-3 crossing. The naive additive anchor over-predicts the drop."""
    f = 0.2
    g_shunt = jp.g_scalar(f, 0.0, 1.0)
    g_series = jp.g_scalar(f, 1.0, 0.0)
    g_both = jp.g_scalar(f, 1.0, 1.0)
    # combined tracks the stronger (series, larger drop) channel, not their sum
    assert np.isclose(g_both, g_series, rtol=1e-3)
    additive = PI_SQRT3 - ((PI_SQRT3 - g_shunt) + (PI_SQRT3 - g_series))
    assert g_both > additive + 0.1  # the sum-of-drops badly over-predicts


@pytest.mark.parametrize("f", [0.0, 0.1, 0.25, 0.5])
def test_g_scalar_is_order_unity_times_reference(f):
    """FORM check (M6): g = O(1) * (memoryless scale). No 'ceiling near omega_C'
    credit — the value is bounded O(1), as dimensional analysis forces."""
    g = jp.g_scalar(f, 1.0, 1.0)
    assert 0.5 * PI_SQRT3 <= g <= PI_SQRT3 + 1e-9
