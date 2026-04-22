"""
Test suite for GW Detection (Gap 4).

Verifies:
  1. Detector catalog properties
  2. Phase shift scales with h and L_eff
  3. Shot noise matches LIGO sensitivity order of magnitude
  4. GW is always in the linear regime (V_gw << V_snap)
  5. Sensitivity curve produces valid output
"""

import numpy as np
import pytest

from ave.gravity.gw_detector import (
    GWDetector,
    DETECTOR_CATALOG,
    impedance_modulation,
    phase_shift,
    shot_noise_strain,
    radiation_pressure_strain,
    total_strain_sensitivity,
    lattice_voltage_ratio,
    detector_summary,
)
from ave.core.constants import Z_0


class TestDetectorCatalog:
    """Detector configurations must be physically reasonable."""

    def test_ligo_exists(self):
        """LIGO must be in the catalog."""
        assert "LIGO" in DETECTOR_CATALOG

    def test_lisa_exists(self):
        """LISA must be in the catalog."""
        assert "LISA" in DETECTOR_CATALOG

    def test_ligo_arm_length(self):
        """LIGO arm length = 4 km."""
        assert DETECTOR_CATALOG["LIGO"].arm_length_m == 4000

    def test_ligo_effective_length(self):
        """L_eff = 4 km × 280 bounces."""
        ligo = DETECTOR_CATALOG["LIGO"]
        assert ligo.effective_length_m == pytest.approx(4000 * 280, rel=0.01)

    def test_lisa_arm_length(self):
        """LISA arm length = 2.5 million km."""
        assert DETECTOR_CATALOG["LISA"].arm_length_m == pytest.approx(2.5e9, rel=0.01)


class TestImpedanceModulation:
    """GW strain must produce correct impedance perturbation."""

    def test_modulation_proportional_to_h(self):
        """δZ = Z₀ × h."""
        assert impedance_modulation(1e-21) == pytest.approx(Z_0 * 1e-21, rel=1e-10)

    def test_modulation_zero_for_no_strain(self):
        """No strain → no modulation."""
        assert impedance_modulation(0.0) == 0.0


class TestPhaseShift:
    """Phase shift must scale correctly."""

    def test_phase_proportional_to_h(self):
        """Δφ ∝ h."""
        ligo = DETECTOR_CATALOG["LIGO"]
        phi1 = phase_shift(1e-21, ligo)
        phi2 = phase_shift(2e-21, ligo)
        assert phi2 == pytest.approx(2 * phi1, rel=1e-10)

    def test_phase_proportional_to_L(self):
        """Δφ ∝ L_eff."""
        det1 = GWDetector("short", 1000, 100, 1, 1064e-9, 100)
        det2 = GWDetector("long", 2000, 100, 1, 1064e-9, 100)
        phi1 = phase_shift(1e-21, det1)
        phi2 = phase_shift(1e-21, det2)
        assert phi2 == pytest.approx(2 * phi1, rel=1e-10)

    def test_ligo_phase_tiny(self):
        """For h=10⁻²¹, raw phase shift ~ 10⁻²¹ rad (raw, before readout)."""
        ligo = DETECTOR_CATALOG["LIGO"]
        phi = phase_shift(1e-21, ligo)
        assert 1e-25 < abs(phi) < 1e-15


class TestSensitivity:
    """Strain sensitivity must match known orders of magnitude."""

    def test_ligo_shot_noise_order(self):
        """LIGO shot noise ≈ 10⁻²⁴ to 10⁻²² /√Hz at 100 Hz."""
        ligo = DETECTOR_CATALOG["LIGO"]
        h_s = shot_noise_strain(ligo, 100.0)
        assert 1e-26 < h_s < 1e-20

    def test_rad_pressure_low_freq(self):
        """Radiation pressure dominates at low freq."""
        ligo = DETECTOR_CATALOG["LIGO"]
        h_rp_10 = radiation_pressure_strain(ligo, 10.0)
        h_rp_1000 = radiation_pressure_strain(ligo, 1000.0)
        assert h_rp_10 > h_rp_1000  # Worse at low freq

    def test_total_sensitivity_curve(self):
        """Total sensitivity must produce valid output."""
        ligo = DETECTOR_CATALOG["LIGO"]
        freq = np.logspace(1, 3, 50)
        sens = total_strain_sensitivity(ligo, freq)
        assert len(sens) == 50
        assert np.all(sens > 0)
        assert np.all(np.isfinite(sens))


class TestLinearRegime:
    """GW must always be in the linear regime."""

    def test_ligo_voltage_ratio(self):
        """V_GW / V_SNAP << 1 for LIGO strain."""
        ratio = lattice_voltage_ratio(1e-21)
        assert ratio < 1e-10

    def test_even_extreme_strain_linear(self):
        """Even h=10⁻¹⁵ (supernovae close-up) is linear."""
        ratio = lattice_voltage_ratio(1e-15)
        assert ratio < 1e-3


class TestSummary:
    """Summary function must produce complete output."""

    def test_summary_runs(self):
        """Summary should run without errors."""
        result = detector_summary("LIGO")
        assert result["name"] == "LIGO"
        assert result["phase_shift_rad"] > 0
        assert len(result["sensitivity_curve"]) > 0
