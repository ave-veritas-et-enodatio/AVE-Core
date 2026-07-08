"""Standing tests for the P6-LV Part-1 sector-trace + SME classification.

Locks the driver `scripts.vol_9_device.p6_lv_sector_classification` as the artifact
for the sector verdict (research/2026-07-08_p6-lv-sector-classification_result.md):

  * D1: for a radiation pump both EM invariants vanish => the live kernel keys on the
    MAGNITUDE |E| (non-covariance enters here).
  * D2: the birefringence kernel modulates the TRANSVERSE-T2 permittivity eps0*S (the
    DROPPING branch), NOT the longitudinal-A1 compliance C0/S (the RISING branch) =>
    Grant's "response sourced in A1" is REFUTED at the response-channel level. The
    par-perp birefringence is ~2x the isotropic shift; both are T2-photon permittivities.
  * D3: E_YIELD chains to M_E (the A1 dilatation rest-mass) via two agreeing routes =>
    the preferred-frame ANCHOR is A1 (a massless T2 photon has no rest frame).
  * D4: the O(beta) first harmonic rides beta.k_hat (propagation-parallel); a transverse
    boost is O(beta^2). Keeps the three senses of 'longitudinal' separate.
  * D5: the AVE birefringence coefficient is field-DEPENDENT (~A^2, vanishes at E=0) =>
    NOT the minimal-SME k_F/k_AF (field-INDEPENDENT). ANTI-TAUTOLOGY: a planted constant
    coefficient is flagged field-independent (k_F-class).

No new claim-id / constant / axiom (CONSISTENCY class). Constants ride in from
ave.core.constants; v_CMB is a labeled EXTERNAL input.
"""
from __future__ import annotations

import sympy as sp

from scripts.vol_9_device.p6_lv_sector_classification import (
    d1_invariance_class,
    d2_response_channel_sector,
    d3_frame_anchor_provenance,
    d4_boost_order_projection,
    d5_sme_field_dependence,
    run,
    verify_constants,
)


def test_verify_constants_codata_and_yield_chain():
    c = verify_constants()
    assert c["C_0_is_codata_exact"] is True
    assert c["C_0_mps"] == 299792458.0
    assert c["V_SNAP_eq_mec2_over_e"] is True
    assert c["E_YIELD_eq_sqrt_alpha_E_CRIT"] is True
    # beta and the reported 1st/2nd harmonic amplitudes reproduce the upstream numbers
    assert abs(c["beta_CMB"] - 370.0e3 / 299792458.0) < 1e-15
    assert abs(c["four_beta"] - 4.0 * c["beta_CMB"]) < 1e-18


def test_d1_kernel_is_magnitude_not_invariant():
    d1 = d1_invariance_class()
    # radiation pump => F = B^2 - E^2/c^2 = 0 => invariant-keyed kernel gives 0 pump bir.
    assert d1["invariant_keyed_kernel_gives_zero_pump_birefringence"] is True
    assert d1["live_kernel_argument"] == "E"


def test_d2_response_channel_is_transverse_T2():
    d2 = d2_response_channel_sector()
    # T2 signature: eps_eff/eps0 = S DROPS with A; the A1 compliance C0/S RISES (contrast)
    assert d2["permittivity_branch_drops_with_A_(T2 signature)"] is True
    assert d2["A1_compliance_branch_would_rise_with_A_(contrast)"] is True
    assert d2["birefringence_index_shift_negative_(vacuum softens)"] is True
    # par-perp birefringence ~ 2x isotropic single-arm shift; both are T2-photon perms
    assert abs(d2["dn_bir_over_dn_iso_ratio"] - 2.0) < 0.1
    assert d2["sector_of_response_channel"] == "TRANSVERSE-T2 (permittivity eps0*S)"
    assert "REFUTED" in d2["H_A1_response_channel"]


def test_d3_frame_anchor_is_A1_rest_mass():
    d3 = d3_frame_anchor_provenance()
    assert d3["E_YIELD_chains_to_M_E"] is True
    assert d3["routes_agree"] is True
    assert d3["massless_T2_photon_has_no_rest_frame"] is True
    assert "A1" in d3["frame_anchor_sector"]
    assert "CONFIRMED" in d3["H_A1_frame_anchor"]


def test_d4_O_beta_rides_propagation_parallel_projection():
    d4 = d4_boost_order_projection()
    coeffs = d4["field_power_linear_coeffs"]
    # linear-beta coeff of |E|^p Doppler power is -p cos(theta): O(beta), propagation-||
    for name, p in (("D1_|E|", 1), ("D2_dn_bir_~A2", 2), ("D4_P_flip_~|E|4", 4)):
        lin = sp.sympify(coeffs[name]["linear_beta_coeff"])
        assert sp.simplify(lin - (-p * sp.cos(sp.Symbol("theta")))) == 0
    # a boost perpendicular to k_hat (cos theta = 0) has NO O(beta) term: leading O(beta^2)
    assert d4["transverse_boost_series"] == "2*beta**2 + 1"


def test_d5_nonlinear_not_minimal_SME():
    d5 = d5_sme_field_dependence()
    assert d5["AVE_is_field_dependent_NONLINEAR"] is True
    assert d5["kF_class_is_field_independent"] is True  # planted control: field-independent
    assert d5["maps_to_minimal_SME_kF_or_kAF"] is False


def test_verdict_split_and_liveness():
    v = run()["VERDICT"]
    assert v["sector_of_LV_response"] == "TRANSVERSE-T2 (permittivity eps0*S)"
    assert v["sector_of_frame_anchor"].startswith("A1")
    assert "REFUTED" in v["grant_mechanism"] and "CONFIRMED" in v["grant_mechanism"]
    assert v["bounded_by_existing_linear_LV_tests"] is False
    assert v["in_principle_transverse_sector_object_Part2_checks_nonlinear_bounds"] is True
    assert v["liveness_ok"] is True
