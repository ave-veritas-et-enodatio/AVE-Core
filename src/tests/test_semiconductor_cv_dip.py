"""Tests for the semiconductor device-analysis -> vacuum-cell mapping (Task #17).

Pins the vacuum C-V datasheet curve at named bias points and locks the
deliverable-(c) eigenmode-check verdict: the birefringence Letter's two probe
eigen-indices ARE the chord and tangent of the T2 permittivity kernel.

REGIME: cold lattice, quasi-static held bias, small-signal probe (Ax3-lossless
below threshold). Every pinned number is derived from ``ave.core.constants`` and
the Axiom-4 kernel — nothing hardcoded.

Sector/homonym guard under test: A1 keyed V_snap (bond compliance, diverges),
T2 keyed V_yield (permittivity, rolls off). The two are NEVER cross-wired.
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pytest

from ave.core.constants import ALPHA, V_SNAP, V_YIELD

# make the verify/ drivers importable (they live in src/scripts/verify),
# matching the repo convention (cf. test_em_keying_round3_eps_dc_mechanism.py)
_VERIFY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "verify")
if _VERIFY not in sys.path:
    sys.path.insert(0, os.path.abspath(_VERIFY))

from semiconductor_cv_dip import (  # noqa: E402
    a1_chord_over_c0,
    a1_tangent_over_c0,
    eigenmode_check,
    kernel_S,
    loaded_line_dispersion,
    t2_chord_over_eps0,
    t2_tangent_over_eps0,
)

RTOL = 1e-12


# --- section 1: kernel + the anti-cross-wire sector keying -------------------


def test_kernel_cold_limit_is_unity():
    assert kernel_S(0.0) == pytest.approx(1.0, rel=RTOL)


def test_kernel_ruptures_above_yield_is_nan():
    assert np.isnan(kernel_S(1.5))


def test_vyield_over_vsnap_is_sqrt_alpha_exactly():
    # the whole two-critical-voltage ontology rests on V_yield = sqrt(alpha) V_snap
    assert V_YIELD / V_SNAP == pytest.approx(np.sqrt(ALPHA), rel=RTOL)


# --- section 2 / (a): chord vs tangent operational definitions ---------------


def test_a1_diverges_toward_vsnap_not_vyield():
    # A1 (bond compliance) keyed V_snap: still ~1 at V_yield, diverging near V_snap
    assert a1_chord_over_c0(V_YIELD) == pytest.approx(1.0, abs=0.01)
    assert a1_chord_over_c0(0.99 * V_SNAP) > 5.0


def test_t2_rolls_off_toward_vyield_not_vsnap():
    # T2 (permittivity) keyed V_yield: rolls to 0 at V_yield
    assert t2_chord_over_eps0(V_YIELD) == pytest.approx(0.0, abs=1e-9)
    assert t2_chord_over_eps0(0.5 * V_YIELD) == pytest.approx(np.sqrt(3) / 2, rel=RTOL)


def test_a1_tangent_is_one_over_s_cubed():
    # device-circuit-models.md:60 : C_ss = dQ/dV = C0/S^3 (the small-signal C)
    v = 0.5 * V_SNAP
    s = kernel_S(v / V_SNAP)
    assert a1_tangent_over_c0(v) == pytest.approx(1.0 / s**3, rel=RTOL)


def test_a1_tangent_at_electron_sqrt_alpha_bias_matches_corpus():
    # device-circuit-models.md:60 : at A=sqrt(alpha) (V=V_yield on the A1 axis)
    # the small-signal compliance is ~1.011 C0.
    assert a1_tangent_over_c0(V_YIELD) == pytest.approx(1.011, abs=1e-3)


def test_t2_tangent_leading_coefficient_is_minus_three_halves():
    # round-3 RESULT: T2 tangent C0*(S - A^2/S) -> leading 1 - 3/2 A0^2
    a = 1e-3
    v = a * V_YIELD
    tangent = float(t2_tangent_over_eps0(v))
    # (tangent - 1)/(-a^2) -> 3/2
    coeff = (tangent - 1.0) / (-(a**2))
    assert coeff == pytest.approx(1.5, rel=1e-4)


def test_t2_chord_leading_coefficient_is_minus_one_half():
    # round-3 RESULT: T2 chord C0*S -> leading 1 - 1/2 A0^2
    a = 1e-3
    v = a * V_YIELD
    chord = float(t2_chord_over_eps0(v))
    coeff = (chord - 1.0) / (-(a**2))
    assert coeff == pytest.approx(0.5, rel=1e-4)


# --- section 4 / (c): the eigenmode-check verdict ----------------------------


def test_eigenmode_check_verdict_true():
    """The Letter's n_perp = chord sqrt(S), n_par = tangent sqrt(S-A^2/S)."""
    eig = eigenmode_check()
    assert eig["match_perp_is_chord"] is True
    assert eig["match_par_is_tangent"] is True
    assert eig["verdict"] is True


def test_eigenmode_birefringence_leading_is_minus_half_a_squared():
    eig = eigenmode_check()
    # dn_bir = -E^2/(2 E_c^2) = -1/2 A^2 ; dn_iso = -1/4 A^2 (exactly half)
    assert str(eig["dn_bir_leading"]) == "-E**2/(2*E_c**2)"
    assert str(eig["dn_iso_leading"]) == "-E**2/(4*E_c**2)"


# --- section 5 / (d): network loaded-line ----------------------------------


def test_loaded_line_cold_edge_is_sine_law():
    # cold (bias=0): omega/omega ratio at q ell = pi is |sin(pi/2)| = 1
    assert loaded_line_dispersion(0.0, np.pi) == pytest.approx(1.0, rel=RTOL)


def test_loaded_line_bias_pulls_band_edge():
    # a held T2 bias shrinks eps_ss (tangent), so 1/sqrt(eps_ss) > 1 pulls up
    assert loaded_line_dispersion(0.5 * V_YIELD, np.pi) > 1.0
