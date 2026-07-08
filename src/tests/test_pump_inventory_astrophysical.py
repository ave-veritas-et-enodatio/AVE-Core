"""Fast-core gates for the PUMP INVENTORY (P6 make-or-break gate).

Pins the load-bearing COMPUTED outputs of
scripts.vol_9_device.pump_inventory_astrophysical:
  - FORK-1 static-B transparency EMERGES (A_I=0, S_B=1, dn_mu=0) at magnetar B;
  - the curl operator is a live (can-fire) informative null, not a dead zero;
  - the magnitude-keyed counterfactual is super-yield (excluded);
  - the strongest clean-path pump is below the lab pump;
  - AVE does not overshoot the static-B IXPE observation;
  - the CMB coincidence routes SPURIOUS and the verdict is PUMP-SAFE.
"""

from __future__ import annotations

import math

import pytest

from scripts.vol_9_device import pump_inventory_astrophysical as P


@pytest.fixture(scope="module")
def fork1():
    return P.fork1_static_B_test()


@pytest.fixture(scope="module")
def envs():
    return P.build_environment_table()


def test_canonical_self_check_passes():
    checks = P.canonical_self_check()
    assert all(checks.values())


def test_fork1_uniform_static_B_is_transparent(fork1):
    # A_I EMERGES = 0 from curl H of a uniform static B at 1e11 T (not asserted).
    assert fork1["A_I_uniform_static"] == 0.0
    assert fork1["S_B_uniform_static"] == 1.0
    assert fork1["dn_mu_uniform_static"] == 0.0
    assert fork1["fork1_holds"] is True


def test_fork1_dipole_magnetar_geometry_machine_zero(fork1):
    # Non-uniform dipole at true magnetar geometry: A_I is machine-zero.
    assert fork1["A_I_dipole_magnetar_geometry"] < 1e-9


def test_fork1_source_free_curl_converges_O_h2(fork1):
    # The curl operator returns the source-free zero as O(h^2) (ratios ~4): the
    # zero is a genuine limit of a working operator, not a dead operator.
    r1 = fork1["dipole_Oh2_ratio_h_to_h2"]
    r2 = fork1["dipole_Oh2_ratio_h2_to_h4"]
    assert 3.5 < r1 < 4.5
    assert 3.5 < r2 < 4.5


def test_fork1_positive_control_fires(fork1):
    # A field WITH circulation returns A_I > 0 -> the null is informative (can-fire).
    assert fork1["positive_control_fires"] is True
    assert fork1["positive_control_A_I_circulation_field"] > 1e-3


def test_magnitude_keyed_counterfactual_is_super_yield(fork1):
    # IF the mu-grade keyed on |B| magnitude, a magnetar would be super-yield
    # (vacuum rupture) -> observationally excluded -> the null is not vacuous.
    assert fork1["counterfactual_magnitude_keyed_super_yield"] is True
    assert fork1["counterfactual_magnitude_keyed_A2_via_B_SNAP"] > 1.0
    # the task's 1e7 T cross-check reproduces ~7e-4
    assert math.isclose(fork1["crosscheck_1e7T_A2_via_B_dual"], 7.0e-4, rel_tol=0.1)


def test_all_static_B_environments_are_transparent(envs):
    for e in envs:
        if e.kind == "static-B":
            assert e.A2_active == 0.0
            assert e.dn_ave == 0.0


def test_bulk_space_static_E_is_zero(envs):
    # Quasi-neutral bulk space (IGM/ISM) has no macroscopic static E pump.
    e6 = next(e for e in envs if e.tag == "E6")
    assert e6.A2_active == 0.0


def test_cmb_and_isrf_radiation_negligible(envs):
    for tag in ("E11", "E12"):
        e = next(x for x in envs if x.tag == tag)
        assert e.A2_active < 1e-30


def test_clean_path_radiation_below_lab_pump(envs):
    clean = {"E3", "E4", "E6", "E7", "E10", "E11", "E12"}
    for e in envs:
        if e.kind == "radiation" and e.tag in clean:
            assert e.A2_active < P.A_LAB_SQ


def test_strongest_pump_is_the_giant_flare(envs):
    strongest = max(envs, key=lambda e: e.A2_active)
    assert strongest.tag == "E8"
    # numerically strongest but a near-source collinear transient (non-constraining)
    assert strongest.A2_active > P.A_LAB_SQ


def test_ixpe_ave_does_not_overshoot():
    ix = P.ixpe_comparison()
    assert ix["dn_AVE_static_FORK1"] == 0.0
    assert ix["AVE_overshoots_IXPE"] is False
    # QED baseline is nonzero (the effect IXPE is consistent with)
    assert ix["dn_QED_magnetic_static"] > 0.0
    # magnitude-keying would be past yield (NaN) -> excluded
    assert math.isnan(float(ix["dn_AVE_if_magnitude_keyed"]))


def test_verdict_is_pump_safe_and_cmb_spurious(fork1, envs):
    res = P.resolve(envs, fork1)
    assert res["VERDICT"] == "PUMP-SAFE"
    assert res["cmb_coincidence"] == "SPURIOUS"
    assert res["cmb_path_pumps"] is False
