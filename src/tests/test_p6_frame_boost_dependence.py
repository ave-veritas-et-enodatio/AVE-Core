"""Standing tests for the P6-FRAME three-corner boost-dependence adjudication.

Locks the driver `scripts.vol_9_device.p6_frame_boost_dependence` as the artifact
for the frame-corner verdict (research/2026-07-08_p6-frame-boost-dependence_result.md):

  * the kernel argument A = |E|/E_YIELD is a frame-dependent MAGNITUDE, not an
    invariant (a covariant kernel gives ZERO pump birefringence for a radiation pump);
  * the response's boost-dependence is O(beta) when keyed on the substrate/CMB-frame
    magnitude (BULK), exactly 0 when keyed on the lab-frame magnitude (LOCAL), and
    O((q*l_node)^4 * beta) when discreteness-gated (LATTICE);
  * ANTI-TAUTOLOGY: all three bins are reachable, and a planted-order guard confirms
    the slope-reader is not floored.

No new claim-id / constant / axiom (CONSISTENCY class). Every physical constant rides
in from ave.core.constants; v_CMB is a labeled EXTERNAL input.
"""
from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_9_device.p6_frame_boost_dependence import (
    assess,
    corner_sweep,
    observable_frac,
    planted_order_guard,
    symbolic_kernel_transform,
    verify_constants,
)


@pytest.fixture(scope="module")
def res():
    r = corner_sweep()
    r["assessment"] = assess(r)
    return r


# --------------------------------------------------------------------------
# Canonical-source guard
# --------------------------------------------------------------------------
def test_constants_canonical_and_beta_reproduces():
    c = verify_constants()
    assert c["C_0_is_codata_exact"] is True
    # beta = v_CMB / c and the registered (v/c)^2 both reproduce
    assert c["beta_CMB"] == pytest.approx(370e3 / 299792458.0, rel=1e-12)
    assert c["beta_CMB_squared"] == pytest.approx(1.523e-6, rel=5e-3)


# --------------------------------------------------------------------------
# The load-bearing analytic sub-question: kernel-argument Lorentz transform
# --------------------------------------------------------------------------
def test_radiation_pump_invariant_vanishes():
    """A covariant (invariant-keyed) kernel gives A=0 -> ZERO pump birefringence:
    the covariant-LOCAL route is inconsistent with the Letter's central prediction."""
    st = symbolic_kernel_transform()
    assert st["radiation_pump_invariant_F_eq_B2_minus_E2"] == "0"
    assert st["radiation_pump_invariant_G_eq_EdotB"] == "0"
    assert st["invariant_keyed_kernel_gives_zero_pump_birefringence"] is True


def test_radiation_branch_is_first_order_static_branch_is_second():
    """Doppler powers D^1/D^2/D^4 carry nonzero linear-in-beta coeffs (cos, 2cos, 4cos);
    the static-field magnitude (gamma) has NO linear term (O(beta^2))."""
    st = symbolic_kernel_transform()
    fp = st["field_powers"]
    assert fp["D_field^1   (|E| ~ pump amplitude)"]["linear_in_beta_coeff"] == "costheta"
    assert fp["D^2  (delta_n_bir ~ A^2 ~ |E|^2)"]["linear_in_beta_coeff"] == "2*costheta"
    assert fp["D^4  (P_flip ~ |E|^4)"]["linear_in_beta_coeff"] == "4*costheta"
    for v in fp.values():
        assert v["linear_is_nonzero"] is True
    # static branch: gamma has zero linear-in-beta coefficient
    assert st["static_field_linear_in_beta_coeff"] == "0"


# --------------------------------------------------------------------------
# The REAL EM-field boost matches the closed-form Doppler factor (no hand-plug)
# --------------------------------------------------------------------------
def test_vector_boost_matches_doppler(res):
    dc = res["doppler_vector_crosscheck"]
    assert dc["rel_err"] < 1e-9  # |E_sub| read off the vector transform == Doppler


# --------------------------------------------------------------------------
# ANTI-TAUTOLOGY liveness: all three bins reachable + planted-order guard
# --------------------------------------------------------------------------
def test_planted_order_guard():
    g = planted_order_guard()
    assert g["planted_n1_reads"] == pytest.approx(1.0, abs=0.02)
    assert g["planted_n2_reads"] == pytest.approx(2.0, abs=0.02)
    assert g["planted_flat_reads_nan"] is True


def test_all_three_bins_reachable(res):
    a = res["assessment"]
    d = a["liveness_detail"]
    assert d["LOCAL_lab_reachable_flat"] is True
    assert d["LOCAL_invariant_reachable_zero_pump_birefringence"] is True
    assert d["BULK_substrate_reachable_order1"] is True
    assert d["LATTICE_reachable_order1_suppressed"] is True
    assert a["liveness_all_three_bins_reachable"] is True


def test_local_configs_are_exactly_flat(res):
    """lab + invariant configs return exactly 0 modulation (order -> nan / flat)."""
    c = res["magnitude_sweep_corners"]
    assert np.isnan(c["lab"]["order_P_flip"])
    assert np.isnan(c["invariant"]["order_P_flip"])
    assert c["lab"]["frac_P_at_beta_cmb"] == 0.0
    assert c["invariant"]["frac_P_at_beta_cmb"] == 0.0


# --------------------------------------------------------------------------
# BULK corner: O(beta), the 4.9e-3 headline, and the sidereal harmonic structure
# --------------------------------------------------------------------------
def test_bulk_is_order_one_in_beta(res):
    c = res["magnitude_sweep_corners"]["substrate"]
    assert c["order_P_flip"] == pytest.approx(1.0, abs=0.02)


def test_bulk_sidereal_headline_4beta(res):
    """P_flip 1st-harmonic = 4 beta ~ 4.94e-3 (reproduces PR #574 under the CMB premise);
    delta_n 1st-harmonic = 2 beta; 2nd harmonic is O(beta^2)."""
    s = res["sidereal_direction_sweep_BULK"]
    beta = res["constants"]["beta_CMB"]
    assert s["P_flip_1st_harmonic_amp"] == pytest.approx(4.0 * beta, rel=1e-3)
    assert s["delta_n_1st_harmonic_amp"] == pytest.approx(2.0 * beta, rel=1e-3)
    # second harmonic is O(beta^2) (exact projection ~3 beta^2), ~3 OOM below the first
    assert s["P_flip_2nd_harmonic_amp"] < 1e-2 * s["P_flip_1st_harmonic_amp"]
    assert beta**2 < s["P_flip_2nd_harmonic_amp"] < 6.0 * beta**2


def test_bulk_frac_at_beta_cmb_is_4p9e_minus_3(res):
    c = res["magnitude_sweep_corners"]["substrate"]
    assert c["frac_P_at_beta_cmb"] == pytest.approx(4.94e-3, rel=2e-2)


# --------------------------------------------------------------------------
# LATTICE corner: same O(beta) order, suppressed amplitude; physical optical value
# --------------------------------------------------------------------------
def test_lattice_is_suppressed_but_order_one(res):
    c = res["magnitude_sweep_corners"]
    assert c["lattice"]["order_P_flip"] == pytest.approx(1.0, abs=0.02)
    # suppressed vs BULK (demonstrated at X-ray q_ln)
    assert abs(c["lattice"]["frac_P_at_beta_cmb"]) < 1e-3 * abs(c["substrate"]["frac_P_at_beta_cmb"])


def test_lattice_physical_optical_unobservable(res):
    lp = res["lattice_physical_optical"]
    # (q*l_node)^4 at optical scale ~ 2e-22 -> the lattice sidereal signal is ~1e-24
    assert lp["supp_qln4_optical"] < 1e-20
    assert lp["P_flip_1st_harmonic_if_lattice"] < 1e-22


# --------------------------------------------------------------------------
# The substrate-native verdict (the physical determination)
# --------------------------------------------------------------------------
def test_substrate_native_verdict_is_bulk(res):
    a = res["assessment"]
    assert a["substrate_native_verdict"] == "BULK"
    assert a["BULK_sidereal_P_flip_1st_harmonic"] == pytest.approx(4.94e-3, rel=2e-2)


def test_lab_frame_reading_gives_exactly_zero():
    """The LOCAL alternative (main.tex:404, lab-frame evaluation) -> sidereal exactly 0."""
    E0 = 1e-3 * 1.1304105713057405e17  # ~A=1e-3 (E_YIELD rides in via the driver)
    khat = np.array([0.0, 0.0, 1.0])
    fdn, fP = observable_frac(E0, khat, -1.234e-3 * np.array([0.0, 0.0, 1.0]), "lab")
    assert fdn == 0.0 and fP == 0.0
