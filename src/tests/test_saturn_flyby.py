"""
Tests for Saturn ring gaps and Earth flyby anomaly.

Saturn ring gaps use the same Kepler resonance physics as Kirkwood gaps.
Flyby anomaly uses Anderson (2008) formula derived from AVE impedance.
"""

import numpy as np

from ave.gravity.solar_impedance import (
    A_MIMAS,
    flyby_anomaly_anderson,
    flyby_anomaly_impedance,
    flyby_catalog,
    saturn_gap_radius,
    saturn_ring_gap_model,
)

# ═══════════════════════════════════════════════════════════════
# Saturn Ring Gaps
# ═══════════════════════════════════════════════════════════════


class TestSaturnRingGaps:

    def test_gap_radius_formula(self):
        """a_gap = a_moon × (q/p)^(2/3) — same as Kirkwood."""
        # 2:1 with Mimas: a_gap = a_Mimas × (1/2)^(2/3)
        r = saturn_gap_radius(2, 1, A_MIMAS)
        expected = A_MIMAS * (0.5) ** (2.0 / 3.0)
        assert abs(r - expected) < 1.0

    def test_cassini_division_accuracy(self):
        """Cassini Division (2:1 Mimas): < 1% error."""
        gaps = saturn_ring_gap_model()
        cassini = [g for g in gaps if "Cassini" in g["gap_name"]][0]
        assert cassini["error_pct"] < 1.0

    def test_encke_gap_exact(self):
        """Encke Gap at Pan's position: 0% error (Pan IS the gap)."""
        gaps = saturn_ring_gap_model()
        encke = [g for g in gaps if "Encke" in g["gap_name"]][0]
        assert encke["error_pct"] < 0.01

    def test_all_gaps_within_rings(self):
        """All predicted gaps are inside Saturn's ring system (< 300,000 km)."""
        for g in saturn_ring_gap_model():
            assert g["r_predicted_km"] < 300_000
            assert g["r_predicted_km"] > 60_000  # Inside D ring

    def test_cassini_inside_a_ring(self):
        """Cassini Division is between B and A rings (117-122 × 10³ km)."""
        gaps = saturn_ring_gap_model()
        cassini = [g for g in gaps if "Cassini" in g["gap_name"]][0]
        assert 100_000 < cassini["r_predicted_km"] < 130_000


# ═══════════════════════════════════════════════════════════════
# Earth Flyby Anomaly
# ═══════════════════════════════════════════════════════════════


class TestFlybyAnomaly:

    def test_anderson_formula_symmetric_zero(self):
        """Equal in/out declination → zero anomaly."""
        dv = flyby_anomaly_anderson(10_000.0, 30.0, 30.0)
        assert abs(dv) < 1e-10

    def test_anderson_formula_equatorial(self):
        """Equatorial flyby with large declination change gives nonzero Δv."""
        dv = flyby_anomaly_anderson(10_000.0, 0.0, -60.0)
        assert abs(dv) > 0

    def test_anderson_formula_sign(self):
        """Positive Δv when cos(δ_in) > cos(δ_out) (equator→pole)."""
        dv = flyby_anomaly_anderson(10_000.0, 0.0, -60.0)
        assert dv > 0  # cos(0) > cos(-60°)

    def test_near_flyby_prediction(self):
        """NEAR (1998): predicted ≈ 13.25 mm/s vs observed 13.46 mm/s."""
        result = flyby_anomaly_impedance(6851.0, 1.23, 20.8, -71.9)
        assert abs(result["dv_predicted_mm_s"] - 13.46) < 1.0

    def test_galileo_i_prediction(self):
        """Galileo I (1990): predicted ≈ 4.14 mm/s vs observed 3.92 mm/s."""
        result = flyby_anomaly_impedance(8949.0, 1.97, -12.5, -34.2)
        assert abs(result["dv_predicted_mm_s"] - 3.92) < 1.0

    def test_messenger_near_zero(self):
        """Messenger (2005): symmetric trajectory → near-zero anomaly."""
        result = flyby_anomaly_impedance(4056.0, 3.35, 31.4, -31.4)
        # cos(31.4) ≈ cos(-31.4) → Δv ≈ 0
        assert abs(result["dv_predicted_mm_s"]) < 0.5

    def test_catalog_has_7_flybys(self):
        """Catalog contains all 7 known flyby events."""
        assert len(flyby_catalog()) == 7

    def test_catalog_all_have_predictions(self):
        """Every flyby has a numerical prediction."""
        for f in flyby_catalog():
            assert np.isfinite(f["dv_predicted_mm_s"])

    def test_gravitomagnetic_coefficient(self):
        """K = 2ωR/c ≈ 3.1×10⁻⁹ (correct order of magnitude)."""
        result = flyby_anomaly_impedance(10_000.0, 2.0, 0.0, -30.0)
        K = result["K_gravitomagnetic"]
        assert 2e-6 < K < 5e-6  # ~3.1×10⁻⁶
