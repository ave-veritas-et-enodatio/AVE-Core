#!/usr/bin/env python3
"""Regression gate for the SCX reference-side boundary classifier.

WHAT WENT WRONG (found at the PR #1016 clearing review, closed here)
-------------------------------------------------------------------
``scx_phase1_crosscheck.arccos_reference`` classified interior-vs-boundary with
an independent margin of ``1e-9`` stated in THETA. Near ``mu = +-z`` the arccos
map is SQUARE-ROOT singular::

    mu = -z + delta   =>   theta = pi - sqrt(2*delta/z)

so a 1e-9 margin in theta demands ``|mu + z| <= z*(1e-9)**2/2 = 1.5e-18`` --
roughly three decades BELOW double-precision resolution at ``|mu| = 3``
(``ulp(3.0) = 4.44e-16``). A boundary eigenvalue that misses its exact integer by
a few ULPs in the wrong direction then classifies INTERIOR and mints a spurious
mode. That is the same floating-point-accident failure mode AMENDMENT A1 was
written to fix, sitting unnoticed in the reference-side classifier.

The margin is now ``BOUNDARY_THETA_MARGIN = TOL_FREQ * pi`` -- the SOLVER side's
own interior filter -- so both sides of the comparison partition on ONE
definition and no new knob is minted.

WHY THIS FILE IS NOT A VACUOUS GREEN
------------------------------------
``test_old_margin_misclassifies_the_recorded_mu_min`` drives the classifier with
the OLD margin and REQUIRES it to give the WRONG answer, on the exact value the
driver itself recorded (``reproduction_gate.fresh.srs_L3_mu_min``). If a future
edit reintroduces a theta-space margin of that order, this file fails. The
mu-space arithmetic is asserted independently of the classifier, so the test does
not merely restate the implementation.

NO PHASE-1 NUMBER MOVES. ``test_repair_moves_no_phase1_reference`` pins the K_4
and srs L=2 reference sets that the shipped Phase-1 record was compared against.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np
import pytest

_DRIVER = (Path(__file__).resolve().parents[1]
           / "scripts" / "vol_1_foundations" / "scx_phase1_crosscheck.py")


def _load():
    spec = importlib.util.spec_from_file_location("scx_phase1_crosscheck_under_test", _DRIVER)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod          # dataclasses resolve via sys.modules
    spec.loader.exec_module(mod)
    return mod


SCX = _load()

#: The DEFECTIVE margin, kept here as the fixture it now is. It is NOT imported
#: from the driver -- the driver no longer contains it, which is the point.
_OLD_THETA_MARGIN = 1.0e-9

#: The driver's OWN recorded value: `reproduction_gate.fresh.srs_L3_mu_min` in
#: `research/drivers/scx_phase1_crosscheck_results.json`. A measurement, quoted
#: as a literal so this gate does not depend on re-running the driver.
_RECORDED_SRS_L3_MU_MIN = -2.9999999999999987

_Z = 3  # srs coordination


def _theta(mu: float, degree: int = _Z) -> float:
    return float(np.arccos(np.clip(mu / degree, -1.0, 1.0)))


# ── the margin itself, exercised in BOTH directions ──────────────────────────

def test_old_margin_misclassifies_the_recorded_mu_min():
    """CAN-FIRE arm. The old margin must give the WRONG answer here."""
    th = _theta(_RECORDED_SRS_L3_MU_MIN)
    assert th < math.pi, "precondition: clip did not fire, so a theta margin is what decides"
    assert SCX.boundary_class(th, _OLD_THETA_MARGIN) == "interior", (
        "the defect is not reproduced: with the old 1e-9 theta margin this "
        "boundary eigenvalue must classify INTERIOR, which is what minted a "
        "spurious mode"
    )
    # and it misses the band edge by ~3e-08 -- 1.5 decades outside the old margin
    assert 1.0e-8 < math.pi - th < 1.0e-7


def test_repaired_margin_classifies_the_recorded_mu_min_as_boundary():
    """FIX arm, same input, same helper, opposite verdict."""
    th = _theta(_RECORDED_SRS_L3_MU_MIN)
    assert SCX.boundary_class(th, SCX.BOUNDARY_THETA_MARGIN) == "top"


def test_margin_is_the_solver_sides_own_filter_not_a_new_knob():
    assert SCX.BOUNDARY_THETA_MARGIN == SCX.TOL_FREQ * math.pi


def test_theta_margin_in_mu_space_clears_double_resolution():
    """The arithmetic that makes the old margin unsatisfiable, asserted directly.

    ``theta = pi - sqrt(2*delta/z)`` => a theta margin ``m`` is a mu margin
    ``z*m**2/2``. Independent of the classifier: it is why a theta-space margin
    of 1e-9 cannot be met, not a restatement of what the classifier does.
    """
    ulp3 = float(np.spacing(3.0))
    old_mu_margin = _Z * _OLD_THETA_MARGIN**2 / 2.0
    new_mu_margin = _Z * SCX.BOUNDARY_THETA_MARGIN**2 / 2.0
    assert old_mu_margin < ulp3 / 100.0, "the old margin was already sub-ULP by decades"
    assert new_mu_margin > 100.0 * ulp3, "the repaired margin must clear double resolution"
    # ...and stay far below any genuine interior eigenvalue's distance from +-z.
    # The closest genuine interior eigenvalue on any rung this lane runs is the
    # K_4 mu = -1, i.e. 2.0 away from -z.
    assert new_mu_margin < 1.0e-6


@pytest.mark.parametrize("mu", [-3.0, 3.0, -2.9999999999999987, 3.0000000000000013])
def test_exact_and_near_exact_band_edges_are_boundary_under_the_repair(mu):
    assert SCX.boundary_class(_theta(mu), SCX.BOUNDARY_THETA_MARGIN) in ("dc", "top")


# ── the full classifier on real engine objects ───────────────────────────────

def test_srs_L3_reference_has_exactly_one_dc_and_one_top_block():
    """END-TO-END arm: the object the defect actually bit, through the real API.

    srs L=3 is bipartite and 3-regular, so its adjacency spectrum contains
    ``mu = +3`` (uniform, the DC root) and ``mu = -3`` (the theta = pi root)
    exactly once each. Interior total must therefore be ``N - 2``.
    """
    net3 = SCX.build_srs_net(3)
    edges = SCX.X.edges_from_net(net3)
    ref = SCX.arccos_reference(edges, net3.n_nodes, _Z)
    assert ref["n_dc"] == 1
    assert ref["n_top"] == 1, (
        "the theta = pi root was not classified as a boundary block -- this is "
        "the defect regressing"
    )
    assert ref["interior_total"] == net3.n_nodes - 2
    assert sum(ref["interior_mult"]) == ref["interior_total"]
    assert len(ref["interior_theta"]) == len(ref["interior_mult"])


def test_repair_moves_no_phase1_reference():
    """The Phase-1 rungs' reference sets are BYTE-IDENTICAL after the repair."""
    k4 = SCX.arccos_reference(SCX.X.srs_primitive_cell_edges(), 4, _Z)
    assert (k4["n_dc"], k4["n_top"], k4["interior_total"]) == (1, 0, 3)
    assert k4["interior_mult"] == [3]

    net2 = SCX.build_srs_net(2)
    l4 = SCX.arccos_reference(SCX.X.edges_from_net(net2), net2.n_nodes, _Z)
    assert (l4["n_dc"], l4["n_top"], l4["interior_total"]) == (1, 1, 62)
    assert l4["interior_mult"] == [6, 6, 4, 9, 6, 6, 9, 4, 6, 6]
    assert len(l4["interior_theta"]) == 10


# ── the L4 engine leg, which had no recorded receipt before this repair ──────

def test_engine_leg_receipt_at_L4_is_a_real_three_way_anchor():
    """The engine's OWN stepper vs the node-space closed form, at L4.

    ``scalar_tlm_step`` + ``scatter_matrix(3)`` never assembles a nodal admittance
    matrix; the arccos leg is the closed form OF that matrix. Agreement here is
    cross-formulation, which is the content the gated solver-vs-arccos comparison
    does not carry.
    """
    net2 = SCX.build_srs_net(2)
    tlm = SCX.tlm_operator_spectrum(net2)
    ref = SCX.arccos_reference(SCX.X.edges_from_net(net2), net2.n_nodes, _Z)
    rec = SCX.engine_leg_receipt(tlm, ref)

    assert rec["engine_n_distinct"] == rec["reference_n_distinct"] == 10
    assert rec["mult_is_exactly_double"], "port space folds +-theta pairs into one block"
    assert rec["engine_total_mult"] == 2 * rec["reference_total_mult"] == 124
    assert rec["engine_dc_block"] == rec["engine_top_block"] == 34
    assert rec["max_rel_dev"] <= SCX.TOL_FREQ
    assert rec["max_rel_dev"] < 1.0e-12, "agreement is at machine precision, not at tolerance"
    assert rec["orthogonality_residual"] < 1.0e-14
    assert rec["pass"] is True
    assert rec["tolerance"] == SCX.TOL_FREQ, "the receipt must not mint a tolerance"


def test_engine_leg_receipt_can_fire():
    """A receipt that cannot fail is a checklist. Perturb one block and check."""
    net2 = SCX.build_srs_net(2)
    tlm = SCX.tlm_operator_spectrum(net2)
    ref = SCX.arccos_reference(SCX.X.edges_from_net(net2), net2.n_nodes, _Z)

    bad_freq = dict(tlm)
    means = list(tlm["interior_theta_mean"])
    means[0] *= 1.0 + 1.0e-5          # 100x TOL-FREQ
    bad_freq["interior_theta_mean"] = means
    assert SCX.engine_leg_receipt(bad_freq, ref)["pass"] is False

    bad_mult = dict(tlm)
    mult = list(tlm["interior_mult"])
    mult[0] += 1
    bad_mult["interior_mult"] = mult
    assert SCX.engine_leg_receipt(bad_mult, ref)["pass"] is False


# ── the prereg sec 3.6 drift registry ────────────────────────────────────────

def test_prereg_s36_drift_registry_reports_and_does_not_gate():
    """The prereg's own rule ("drift ... is itself a finding banked"), executed.

    The registry must REPORT the drift and must NOT be wired into the
    reproduction gate's pass -- prereg sec 3.4 step 7 makes the comparison consume
    the FRESH reference, so no verdict may turn on the frozen table.
    """
    net2 = SCX.build_srs_net(2)
    ref = SCX.arccos_reference(SCX.X.edges_from_net(net2), net2.n_nodes, _Z)
    d = SCX.prereg_s36_drift(ref)

    assert len(d["rows"]) == len(SCX.PREREG_S36_L4_FROZEN) == 10
    assert d["mult_all_match"], "the frozen multiplicity column is correct and must stay so"
    # The theta column reproduces to its printed precision on every row...
    assert d["theta_rows_beyond_print_precision"] == []
    # ...and the omega/omega_C column does not, which is the banked finding.
    assert d["w_over_wc_rows_beyond_print_precision"], (
        "if this is empty the frozen table now reproduces and the dated note "
        "in the prereg must be revisited rather than this assertion relaxed"
    )
    assert d["w_over_wc_max_drift_in_TOL_FREQ_units"] > 100.0
    # A single frozen map cannot produce that column: the implied factor varies.
    assert d["implied_factor_spread"] > 1.0e-5
    assert "NOT GATING" in d["status"]
