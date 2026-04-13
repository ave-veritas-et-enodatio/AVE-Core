"""
Test suite for the Cosserat Electroweak Sector (src/ave/topological/cosserat.py).

Locks in the AVE framework's zero-parameter electroweak predictions against
PDG experimental values. Every assertion uses a generous tolerance band
(typically ±5%) since the tree-level derivations intentionally exclude
higher-order radiative corrections.
"""

import math
import pytest


# ---------------------------------------------------------------------------
# Import everything from the Cosserat module
# ---------------------------------------------------------------------------
from ave.topological.cosserat import (
    SIN2_THETA_W,
    M_W_MEV,
    M_Z_MEV,
    M_MU_MEV,
    M_TAU_MEV,
    SUM_M_NU_EV,
    G_MINUS_2_TREE,
    L_COSSERAT,
)

# ---------------------------------------------------------------------------
# PDG / CODATA reference values
# ---------------------------------------------------------------------------
PDG_SIN2_THETA_W_ONSHELL = 0.2230    # on-shell scheme
PDG_M_W_MEV = 80_379.0               # W boson mass
PDG_M_Z_MEV = 91_188.0               # Z boson mass
PDG_M_MU_MEV = 105.658               # Muon mass
PDG_M_TAU_MEV = 1776.86              # Tau mass
PLANCK_SUM_MNU_BOUND_EV = 0.12       # Cosmological upper bound
SCHWINGER_G2 = 1.0 / (2 * math.pi) * (1.0 / 137.035999084)  # alpha/(2*pi)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestWeakMixingAngle:
    """sin²θ_W = 2/9 from the Perpendicular Axis Theorem."""

    def test_exact_value(self):
        assert SIN2_THETA_W == pytest.approx(2.0 / 9.0, rel=1e-10)

    def test_vs_pdg(self):
        assert SIN2_THETA_W == pytest.approx(PDG_SIN2_THETA_W_ONSHELL, rel=0.01)


class TestWBosonMass:
    """M_W = m_e / (α² · p_c · √(3/7))."""

    def test_vs_pdg(self):
        assert M_W_MEV == pytest.approx(PDG_M_W_MEV, rel=0.02)

    def test_below_z(self):
        assert M_W_MEV < M_Z_MEV


class TestZBosonMass:
    """M_Z = M_W · 3/√7."""

    def test_vs_pdg(self):
        assert M_Z_MEV == pytest.approx(PDG_M_Z_MEV, rel=0.02)

    def test_ratio(self):
        ratio = M_W_MEV / M_Z_MEV
        expected = math.sqrt(7) / 3
        assert ratio == pytest.approx(expected, rel=1e-10)


class TestMuonMass:
    """m_μ = m_e / (α · √(3/7))."""

    def test_vs_pdg(self):
        assert M_MU_MEV == pytest.approx(PDG_M_MU_MEV, rel=0.02)


class TestTauMass:
    """m_τ = m_e · p_c / α²."""

    def test_vs_pdg(self):
        assert M_TAU_MEV == pytest.approx(PDG_M_TAU_MEV, rel=0.02)


class TestNeutrinoSum:
    """Σm_ν ≈ 0.054 eV (must be < 0.12 eV Planck bound)."""

    def test_below_planck_bound(self):
        assert SUM_M_NU_EV < PLANCK_SUM_MNU_BOUND_EV

    def test_order_of_magnitude(self):
        assert 0.01 < SUM_M_NU_EV < 0.10


class TestSchwingerGMinus2:
    """a_e = α/(2π) (Schwinger, 1948)."""

    def test_exact_formula(self):
        from ave.core.constants import ALPHA
        expected = ALPHA / (2 * math.pi)
        assert G_MINUS_2_TREE == pytest.approx(expected, rel=1e-10)

    def test_vs_schwinger(self):
        assert G_MINUS_2_TREE == pytest.approx(SCHWINGER_G2, rel=1e-6)


class TestCosseratLength:
    """Weak force range: ℓ_C = ℏ/(M_W·c) ≈ 2.5 × 10⁻¹⁸ m."""

    def test_order_of_magnitude(self):
        assert 1e-19 < L_COSSERAT < 1e-17


class TestMassHierarchy:
    """m_e < m_μ < m_τ < M_W < M_Z (strict ordering)."""

    def test_ordering(self):
        from ave.core.constants import M_E, C_0
        M_E_MEV = M_E * C_0**2 / 1.602176634e-13
        assert M_E_MEV < M_MU_MEV < M_TAU_MEV < M_W_MEV < M_Z_MEV
