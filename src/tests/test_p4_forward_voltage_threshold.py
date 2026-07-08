"""Standing tests for the P4 forward-voltage conduction threshold driver.

Pins the make-or-break findings: constants cross-check COMPUTED, the LC-cell
reactances, the gapless dispersion (no phonon-seeded V_f), the V_f candidate
scales, round-3 compatibility (E_f=0 => the continuous kernel, no dead zone),
copper CONSISTENT, muonic C-STANDS below the turnover, and the Delbruck fence.

Every pinned number derives from ave.core.constants; delta_Cu is external (tagged).
"""

from __future__ import annotations

import math
import os
import sys

import numpy as np
import pytest

from ave.core.constants import ALPHA, E_YIELD, L_NODE, V_SNAP, V_YIELD, Z_0

# make the vol_9_device driver importable (repo convention, cf. semiconductor test)
_DRV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "vol_9_device")
if _DRV not in sys.path:
    sys.path.insert(0, os.path.abspath(_DRV))

from p4_forward_voltage_threshold import (  # noqa: E402
    cell_reactances,
    copper_decrement,
    delbruck_fence,
    dispersion_has_gap,
    eps_eff_over_eps0,
    kernel_S,
    muonic_loading_with_threshold,
    verify_constants,
    vf_candidates,
)

RTOL = 1e-9


# --------------------------------------------------------------------------- #
# section 0 — canonical-source cross-check
# --------------------------------------------------------------------------- #
def test_verify_constants_all_pass():
    vc = verify_constants()
    assert vc["all_pass"], vc["checks"]


def test_cell_reactances_Z0_and_omegaC():
    cell = cell_reactances()
    assert math.isclose(cell["Z0_ohm"], Z_0, rel_tol=RTOL)
    # omega_C = 1/sqrt(LC) = c/ell_node
    from ave.core.constants import C_0

    assert math.isclose(cell["omegaC_rad_s"], C_0 / L_NODE, rel_tol=RTOL)


# --------------------------------------------------------------------------- #
# section 1 — S1 round-3 compatibility: E_f=0 is the continuous kernel (no dead zone)
# --------------------------------------------------------------------------- #
def test_S1_zero_threshold_recovers_round3_continuous_kernel():
    """E_f=0 (no dead zone) must equal the smooth kernel S(A) at every field."""
    E = np.linspace(0.0, 0.9, 50) * E_YIELD
    assert np.allclose(eps_eff_over_eps0(E, 0.0), kernel_S(E / E_YIELD), atol=1e-14)


def test_S1_nonzero_threshold_introduces_a_dead_zone_departure():
    """A nonzero dead zone MUST depart from round-3: eps=eps0 (flat) below E_f,
    while round-3 already loads there (S<1). This is the flag: V_f>0 contradicts
    round-3's continuous loading."""
    A_f = 0.3
    E_below = 0.2 * E_YIELD  # A=0.2 < A_f
    gated = float(eps_eff_over_eps0(E_below, A_f * E_YIELD))
    round3 = float(kernel_S(0.2))
    assert math.isclose(gated, 1.0)  # dead zone: transparent
    assert round3 < 1.0  # round-3 already loaded here
    assert gated != pytest.approx(round3)  # they genuinely differ (can-fire)


# --------------------------------------------------------------------------- #
# section 2 — DERIVE V_f: FORCED or FREE
# --------------------------------------------------------------------------- #
def test_C1_dispersion_is_gapless_no_phonon_seeded_Vf():
    d = dispersion_has_gap()
    assert d["is_gapped"] is False
    assert d["gap_voltage_V"] == 0.0


def test_vf_candidates_scales():
    c = vf_candidates()
    # C2 slew: A_f = sqrt(alpha)
    assert math.isclose(c["C2_slew"]["A_f"], math.sqrt(ALPHA), rel_tol=RTOL)
    # C3 turnover reference: A_f = 1/2 exactly
    assert math.isclose(c["C3_turnover_ref"]["A_f"], 0.5, rel_tol=RTOL)
    assert math.isclose(c["C3_turnover_ref"]["Vf_V"], V_YIELD / 2.0, rel_tol=RTOL)
    # C4 turnover actual: A_f = 1/sqrt2
    assert math.isclose(c["C4_turnover_actual"]["A_f"], 1.0 / math.sqrt(2.0), rel_tol=RTOL)
    # C5 pair gap: V_f = V_snap
    assert math.isclose(c["C5_pair_gap"]["Vf_V"], V_SNAP, rel_tol=RTOL)
    # C6 A0-cutoff image is a tiny bond voltage (~46 V) — not a canonical scale
    assert c["C6_A0_cutoff_image"]["Vf_V"] < 100.0


# --------------------------------------------------------------------------- #
# section 3a — copper CONSISTENT (OUR compute)
# --------------------------------------------------------------------------- #
def test_copper_decrement_is_consistent_and_far_below_delta_Cu():
    cu = copper_decrement(A_f=0.0)
    assert cu["verdict_index"] == "CONSISTENT"
    # our index decrement is ~4e-8, ~3 OOM below the measured 2.4e-5
    assert cu["delta_index_interior_excl"] < cu["delta_Cu_1pct_band"]
    assert cu["ratio_index_to_delta_Cu"] < 1e-2
    # a modest dead zone does not change the consistency (copper dominated by core)
    cu_thr = copper_decrement(A_f=0.2)
    assert cu_thr["verdict_index"] == "CONSISTENT"


# --------------------------------------------------------------------------- #
# section 3b — muonic: the dead zone does NOT rescue below the turnover
# --------------------------------------------------------------------------- #
def test_muonic_C_stands_for_subturnover_threshold():
    """A forward-voltage dead zone at A_f < 1/2 keeps the near-nucleus overshoot:
    the surviving loading fraction stays ~1 and [C-EXCLUDED] stands. Only the
    turnover A_f>=1/2 (a HIGH-field ceiling, upside-down as a floor) empties it."""
    mu = muonic_loading_with_threshold(A_f=0.05)
    assert mu["verdict"] == "C-STANDS"
    assert mu["surviving_loading_fraction"] > 0.5  # far tail removed only
    # at the turnover the real-branch loading is emptied (direction demonstration)
    mu_turn = muonic_loading_with_threshold(A_f=0.5)
    assert mu_turn["surviving_loading_fraction"] == 0.0


# --------------------------------------------------------------------------- #
# section 3c — Delbruck / gamma fence
# --------------------------------------------------------------------------- #
def test_delbruck_fence_band_edge():
    f = delbruck_fence()
    assert f["fenced"] is True
    # response scale hbar*omega_C = 511 keV; band edge 2x = 1.022 MeV
    assert math.isclose(f["E_response_scale_keV"], 511.0, rel_tol=1e-3)
    assert math.isclose(f["E_band_edge_MeV"], 1.022, rel_tol=1e-2)
