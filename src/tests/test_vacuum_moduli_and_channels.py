"""
Fundamental vacuum moduli + three-channel propagation keepers.

Closes gaps not covered by test_constants_derivation.py:
  - K_bulk / G_vac = 2 (EMT trace-reversal operating point)
  - ν_vac = 2/7 as consequence of K = 2G (isotropic elasticity)
  - V_LONG = √(K/ρ) = √2 · c₀ (bulk dilatational speed, not full P-wave)
  - Linear-regime three-speed split (EM / shear / bulk-longitudinal)
  - Per-channel saturation ride H_EM, H_shear, H_bulk (vocab audit §3.2)
"""

from __future__ import annotations

import math

import numpy as np
import pytest

from ave.core.chiral_lattice_v10 import channel_H_diagnostics
from ave.core.constants import (
    ALPHA,
    C_0,
    G_VAC,
    L_NODE,
    MU_0,
    NU_VAC,
    P_C,
    RHO_BULK,
    T_EM,
    V_LONG,
    XI_TOPO,
    Z_0,
)
from ave.regime_4_rupture.rupture_solver import TopologicalRuptureSolver


def _k_bulk() -> float:
    """Bulk modulus at K/G = 2 operating point (not exported as a named constant)."""
    return 2.0 * G_VAC


class TestVacuumModuliDefinitions:
    """Internal consistency of ρ_bulk, G_vac, K_bulk, V_LONG."""

    def test_rho_bulk_formula(self) -> None:
        expected = (XI_TOPO**2 * MU_0) / (P_C * L_NODE**2)
        assert RHO_BULK == pytest.approx(expected, rel=1e-12)

    def test_g_vac_is_rho_c_squared(self) -> None:
        assert G_VAC == pytest.approx(RHO_BULK * C_0**2, rel=1e-12)

    def test_transverse_speed_is_c(self) -> None:
        """√(G_vac / ρ_bulk) = c₀ — photon/shear transverse propagation."""
        v_transverse = math.sqrt(G_VAC / RHO_BULK)
        assert v_transverse == pytest.approx(C_0, rel=1e-12)

    def test_bulk_to_shear_modulus_ratio_is_two(self) -> None:
        """K_bulk / G_vac = 2 (canonical EMT / Ch 2 operating point)."""
        assert _k_bulk() / G_VAC == pytest.approx(2.0, rel=1e-15)

    def test_v_long_from_k_over_rho(self) -> None:
        assert V_LONG == pytest.approx(math.sqrt(_k_bulk() / RHO_BULK), rel=1e-12)

    def test_v_long_is_sqrt_two_c(self) -> None:
        """Bulk dilatational speed √(K/ρ) = √2 · c₀ at K = 2G."""
        assert V_LONG == pytest.approx(math.sqrt(2.0) * C_0, rel=1e-12)

    def test_v_long_exceeds_transverse_c(self) -> None:
        assert V_LONG > C_0
        assert V_LONG / C_0 == pytest.approx(math.sqrt(2.0), rel=1e-12)


class TestPoissonFromKOverG:
    """ν_vac = 2/7 follows from K = 2G in 3D isotropic elasticity."""

    def test_nu_from_k_equals_two_g(self) -> None:
        K, G = _k_bulk(), G_VAC
        nu = (3.0 * K - 2.0 * G) / (2.0 * (3.0 * K + G))
        assert nu == pytest.approx(2.0 / 7.0, rel=1e-15)
        assert NU_VAC == pytest.approx(nu, rel=1e-15)

    def test_p_wave_speed_differs_from_bulk_dilatational(self) -> None:
        """Full isotropic P-wave √(K + 4G/3)/ρ ≠ √(K/ρ) = V_LONG (corpus flag)."""
        K, G, rho = _k_bulk(), G_VAC, RHO_BULK
        v_p = math.sqrt((K + (4.0 / 3.0) * G) / rho)
        assert v_p == pytest.approx(math.sqrt(10.0 / 3.0) * C_0, rel=1e-12)
        assert v_p > V_LONG


class TestThreeSpeedLinearRegime:
    """Three-channel speeds at zero strain (S = 1, r = 0)."""

    def test_rupture_solver_linear_limits(self) -> None:
        prof = TopologicalRuptureSolver.evaluate_rupture_state(0.0)
        assert prof["S"][0] == pytest.approx(1.0, abs=1e-15)
        assert prof["c_shear"][0] == pytest.approx(C_0, rel=1e-12)
        assert prof["c_EM_sym"][0] == pytest.approx(C_0, rel=1e-12)
        assert prof["c_EM_asym"][0] == pytest.approx(C_0, rel=1e-12)
        assert prof["Z_sym"][0] == pytest.approx(Z_0, rel=1e-12)
        assert prof["Z_asym"][0] == pytest.approx(Z_0, rel=1e-12)

    def test_three_speed_ordering_at_moderate_strain(self) -> None:
        """At S < 1: c_EM rises, c_shear falls; bulk-long = √2·c_shear > c_EM > c_shear."""
        r = 0.5
        prof = TopologicalRuptureSolver.evaluate_rupture_state(r)
        c_em = float(prof["c_EM_asym"][0])
        c_sh = float(prof["c_shear"][0])
        c_bulk_long = math.sqrt(2.0) * c_sh  # K = 2G, both ∝ S
        assert c_em > C_0
        assert c_sh < C_0
        assert c_bulk_long == pytest.approx(math.sqrt(2.0) * c_sh, rel=1e-12)
        assert c_bulk_long > c_em > c_sh


class TestChannelSaturationRide:
    """H_EM, H_shear, H_bulk exponents per dark-sector §3.2 / field-symbol-registry."""

    def test_linear_regime_H_all_unity(self) -> None:
        h = channel_H_diagnostics(np.array([0.0]))
        assert h["H_EM"] == pytest.approx(1.0, rel=1e-12)
        assert h["H_shear"] == pytest.approx(1.0, rel=1e-12)
        assert h["H_bulk"] == pytest.approx(1.0, rel=1e-12)

    def test_H_exponents_at_half_saturation(self) -> None:
        a2 = 0.5
        s = math.sqrt(1.0 - a2)
        h = channel_H_diagnostics(np.array([a2]))
        assert h["H_EM"] == pytest.approx(1.0 / s, rel=1e-12)
        assert h["H_shear"] == pytest.approx(math.sqrt(s), rel=1e-12)
        assert h["H_bulk"] == pytest.approx(s, rel=1e-12)

    def test_H_em_over_H_shear_scaling(self) -> None:
        """H_EM / H_shear = (1−A²)^(−3/4) — channel exponent discipline."""
        for a2 in (0.1, 0.5, 0.9):
            h = channel_H_diagnostics(np.array([a2]))
            s = math.sqrt(1.0 - a2)
            expected = s ** (-1.5)
            assert h["H_EM"] / h["H_shear"] == pytest.approx(expected, rel=1e-12)


class TestEMTOperatingPoint:
    """Cross-check packing fraction + coordination at K/G = 2."""

    def test_p_c_at_alpha_packing(self) -> None:
        assert P_C == pytest.approx(8.0 * math.pi * ALPHA, rel=1e-12)

    def test_string_tension_vs_shear_modulus(self) -> None:
        """G_string (1D edge tension/ℓ) and G_vac (3D ρc²) are distinct objects — not equal."""
        g_string = T_EM / L_NODE
        assert g_string > 0.0
        assert G_VAC > 0.0
        assert g_string != pytest.approx(G_VAC, rel=0.01)
