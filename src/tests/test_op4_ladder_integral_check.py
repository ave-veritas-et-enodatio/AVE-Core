"""Test for the Op4 ladder-integral check (Ruling-11 registered check).

Covers (1) the verdict-class logic at its declared thresholds; (2) the Op4 dress is the
documented canonical-kernel identity Z/Z0 = (1-(d/r)^2)^{-1/4}; (3) the exact ladder
recursion converges to the local WKB dress (adiabatic invariant); (4) the VOLTAGE-register
control ladder recovers Op4 (p=2) while the FIELD-strain ladder gives p=4 under BOTH signs
(the NO-MATCH signature). No physics constants hard-coded — Z_0/EPS_CLIP via ave.core; the
kernel via ave.core.universal_operators (imported unmodified by the driver).
"""
import numpy as np
import pytest

from scripts.vol_1_foundations.op4_ladder_integral_check import (
    D_SAT,
    FIELD_P_TOL,
    MATCH_P_TOL,
    MATCH_REL,
    classify,
    fit_exponent,
    kernel_S,
    ladder_zin,
    op4_dress,
    strain_field,
    strain_voltage,
    z_local,
)
from ave.core.constants import Z_0
from ave.core.universal_operators import universal_saturation


def test_op4_dress_is_canonical_kernel_identity():
    """op4_dress reconstructs the documented Z/Z0 = (1-(d/r)^2)^{-1/4} identity
    (universal_operators.py:229) via the CANONICAL kernel — never a re-implemented form."""
    r = np.geomspace(2.0, 300.0, 40)
    documented = (1.0 - (D_SAT / r) ** 2) ** (-0.25)
    assert np.allclose(op4_dress(r) / Z_0, documented, rtol=1e-12)
    # and it is exactly S(A_V)^{-1/2} with the voltage-strain A_V = d/r
    S_v = universal_saturation(D_SAT / r, 1.0)
    assert np.allclose(op4_dress(r) / Z_0, S_v ** (-0.5), rtol=1e-12)


def test_strains_are_distinct_registers():
    """FIELD-strain (d/s)^2 (~1/s^2) is NOT the VOLTAGE-strain d/s (~1/s) — the fork this
    check turns on."""
    s = np.array([2.0, 5.0, 10.0])
    assert np.allclose(strain_field(s), (D_SAT / s) ** 2)
    assert np.allclose(strain_voltage(s), D_SAT / s)
    assert not np.allclose(strain_field(s), strain_voltage(s))


def test_classify_declared_thresholds():
    """Verdict-class logic at its frozen boundaries (declared before any computation)."""
    # MATCH-FORM: both sign variants recover Op4's p=2 within tol AND small deviation
    assert classify(2.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0) == "MATCH-FORM"
    # MATCH-UP-TO-SIGN: only one sign variant matches
    assert classify(2.0, 0.0, 4.0, 0.1, 0.0, 0.0, 2.0) == "MATCH-UP-TO-SIGN"
    # PARTIAL: neither matches (near deviation too large) but far agrees & best p ~ 2
    assert classify(2.0, 0.05, 2.0, 0.05, 0.05, 1e-3, 2.0) == "PARTIAL"
    # NO-MATCH: field ladder is structurally p=4
    assert classify(4.0, 0.054, 4.0, 0.084, 0.054, 2.6e-4, 4.0) == "NO-MATCH"
    # NO-MATCH also when p is clearly not 2 and not the PARTIAL shape
    assert classify(4.0, 0.5, 4.0, 0.5, 0.5, 0.5, 4.0) == "NO-MATCH"


def test_kernel_S_is_canonical():
    """kernel_S is the imported Ax4 kernel S=sqrt(1-A^2); unsaturated A->0 => S->1."""
    assert kernel_S(0.0) == pytest.approx(1.0)
    assert kernel_S(0.5) == pytest.approx(np.sqrt(1.0 - 0.25))


def test_ladder_converges_to_local_dress_adiabatic():
    """The exact transmission-line cascade converges to the local characteristic impedance
    (the WKB/adiabatic invariant) as the discretization refines — for the FIELD register,
    both sign variants. Residual must DECREASE with cell count."""
    r = 2.0  # deepest near-zone sample (largest dress)
    for sign in (-1, +1):
        local = float(z_local(r, strain_field, sign))
        resids = [abs(ladder_zin(r, strain_field, sign, n, 0.30).real - local)
                  for n in (400, 1200, 4000)]
        assert resids[0] > resids[1] > resids[2]          # monotone convergence
        assert resids[-1] / abs(local) < 5e-3             # reaches the local dress


def test_voltage_control_recovers_op4_but_field_does_not():
    """CONTROL: the VOLTAGE-register ladder reproduces Op4 (p=2). The FIELD-strain ladder
    gives p=4 under BOTH signs and diverges from Op4 in the near zone (the NO-MATCH core)."""
    # voltage register recovers Op4's exponent
    fv = fit_exponent(strain_voltage, sign=-1, q=-0.25)
    assert abs(fv["p"] - 2.0) <= MATCH_P_TOL
    # exact voltage-ladder port ~ Op4 pointwise
    r = 2.0
    assert ladder_zin(r, strain_voltage, -1, 4000, 0.30).real == pytest.approx(float(op4_dress(r)), rel=5e-3)

    # field register is p=4 (NOT p=2), both signs
    ffr = fit_exponent(strain_field, sign=-1, q=-0.25)
    ffl = fit_exponent(strain_field, sign=+1, q=+0.25)
    assert abs(ffr["p"] - 4.0) <= FIELD_P_TOL
    assert abs(ffl["p"] - 4.0) <= FIELD_P_TOL
    assert abs(ffr["p"] - 2.0) > MATCH_P_TOL
    # near-zone deviation of the field dress from Op4 exceeds the MATCH tolerance
    zl = float(z_local(r, strain_field, -1))
    assert abs(zl / float(op4_dress(r)) - 1.0) > MATCH_REL
