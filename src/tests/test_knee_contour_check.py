"""Test for the knee-contour vs collar-edge check (F5-walk registered check).

Covers (1) the verdict-class logic at its declared thresholds and (2) that the
imported-#693-solver measurement functions run and return sane, kernel-consistent
numbers on a tiny mesh. No physics constants hard-coded — all from ave.core.constants
via the driver.
"""
import numpy as np
import pytest

from scripts.vol_2_subatomic.knee_contour_check import (
    A_YIELD,
    D_SAT,
    DSAT_IN_LNODE,
    MATCH_FACTOR,
    PARTIAL_FACTOR,
    classify,
    enclosed_correction,
    kernel_S,
    knee_from_profile,
    reflection_Gamma,
    single_probe_profile,
)
from ave.core.constants import ALPHA, R_I


def test_knee_amplitude_is_canonical():
    """A_YIELD must be R_I = sqrt(2*alpha) (the deficit-knee / regime-I boundary),
    imported from constants — never hard-coded."""
    assert A_YIELD == pytest.approx(R_I)
    assert A_YIELD == pytest.approx(np.sqrt(2.0 * ALPHA))
    # unit map is the canonical 1:1 (d_sat == ell_node)
    assert DSAT_IN_LNODE == 1.0


def test_classify_declared_thresholds():
    """Verdict-class logic at its frozen boundaries (declared before any computation)."""
    # MATCH: within a factor of 2 (either direction)
    assert classify(2.0, 2.0) == "MATCH"
    assert classify(2.0, 3.9) == "MATCH"          # ratio 1.95 < 2
    assert classify(3.9, 2.0) == "MATCH"          # symmetric
    # PARTIAL: factor 2-5
    assert classify(2.0, 4.5) == "PARTIAL"        # ratio 2.25
    assert classify(2.0, 9.9) == "PARTIAL"        # ratio 4.95 < 5
    # NO-MATCH: > 5x
    assert classify(2.0, 11.0) == "NO-MATCH"      # ratio 5.5
    assert classify(1.0, 100.0) == "NO-MATCH"
    # exact boundaries fall on the inclusive side
    assert classify(1.0, MATCH_FACTOR) == "MATCH"
    assert classify(1.0, PARTIAL_FACTOR) == "PARTIAL"
    assert classify(1.0, 0.0) == "UNDEFINED"


def test_kernel_S_and_Gamma_at_knee():
    """At the deficit knee A=sqrt(2a): S=sqrt(1-2a) ~= 1-alpha (DeltaS=alpha), and the
    E-sector reflection magnitude ~ alpha/4 (matches the ruling's |Gamma| ~ 0.002)."""
    S = kernel_S(A_YIELD)
    assert S == pytest.approx(np.sqrt(1.0 - 2.0 * ALPHA))
    assert (1.0 - S) == pytest.approx(ALPHA, rel=0.02)     # DeltaS = alpha (proportional limit)
    G = reflection_Gamma(S)
    assert abs(G) == pytest.approx(ALPHA / 4.0, rel=0.05)  # |Gamma| ~ alpha/4 ~ 0.0018
    # unsaturated limit: A->0 => S->1 => Gamma->0
    assert reflection_Gamma(kernel_S(0.0)) == pytest.approx(0.0, abs=1e-12)


def test_single_probe_profile_matches_field_strain():
    """The measured kernel-consumed A(s) must track the bare FIELD-strain (d_sat/s)^2
    (NOT the voltage-strain d_sat/s) near a single probe — the amplitude-discipline check."""
    prof = single_probe_profile(50.0, 0.03, n_r=8, n_ang=12)
    s, A = np.asarray(prof["s"]), np.asarray(prof["A"])
    inner = s < 5.0
    assert inner.sum() >= 2
    # field-strain (d_sat/s)^2, not voltage-strain (d_sat/s)
    assert np.allclose(A[inner], (D_SAT / s[inner]) ** 2, rtol=0.05)
    assert not np.allclose(A[inner], D_SAT / s[inner], rtol=0.05)


def test_knee_from_profile_ordering():
    """Field-strain knee < voltage-strain knee (the (2a)^{1/4} vs (2a)^{1/2} split)."""
    prof = single_probe_profile(50.0, 0.03, n_r=8, n_ang=12)
    k = knee_from_profile(prof)
    assert k["s_knee_field_bare_dsat"] == pytest.approx(D_SAT * A_YIELD ** -0.5)
    assert k["s_knee_voltage_dsat_FLAGGED"] == pytest.approx(D_SAT / A_YIELD)
    assert k["s_knee_field_bare_dsat"] < k["s_knee_voltage_dsat_FLAGGED"]


def test_enclosed_correction_monotone_and_bounded():
    """Enclosed-correction fraction is monotone 0->~1 and the collar radii are ordered
    r50 <= r90 <= r99, all inside the mesh."""
    e = enclosed_correction(30.0, 0.03, n_orient=1, n_cut=12, n_r=8, n_ang=12)
    frac = np.asarray(e["enclosed_frac"])
    assert np.all(np.diff(frac) >= -1e-9)          # monotone nondecreasing
    assert frac[-1] == pytest.approx(1.0, abs=0.05)
    r50, r90, r99 = e["r50_dsat"], e["r90_dsat"], e["r99_dsat"]
    if np.isfinite(r50) and np.isfinite(r90) and np.isfinite(r99):
        assert r50 <= r90 <= r99 + 1e-9
