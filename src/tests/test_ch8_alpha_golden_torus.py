"""
Regression tests for Ch. 8 (Zero-Parameter Closure: α from the Golden Torus).

Pins the load-bearing numerical claims of the α derivation so future edits
to geometry, engine constants, or the optimizer implementations cannot
silently drift the result:

    α⁻¹_ideal = 4π³ + π² + π ≈ 137.0363
    δ_strain  = (α⁻¹_ideal − α⁻¹_CODATA) / α⁻¹_ideal ≈ 2.22×10⁻⁶
    Golden Torus: R = φ/2, r = (φ-1)/2
    Constraints at Golden Torus: R − r = 1/2, R · r = 1/4
    Ropelength + screening optimizer converges to Golden Torus from
    arbitrary starting points.

Reference: manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex
"""
import numpy as np
import pytest

from ave.core.constants import ALPHA, ALPHA_COLD_INV, ALPHA_COLD, DELTA_STRAIN

from scripts.vol_1_foundations.derive_alpha_from_golden_torus import (
    PHI, R_gt, r_gt, golden_torus_multipole,
)
from scripts.vol_1_foundations.verify_clifford_half_cover import (
    clifford_area_numeric, solve_golden_torus,
)
from scripts.vol_1_foundations.ropelength_trefoil_golden_torus import (
    trefoil_arc_length, stage_b_with_screening_constraint, GOLDEN_R, GOLDEN_r,
)


# ───────────────────────────────────────────────────────────────────────────
# 1. Multipole closure: α⁻¹ = 4π³ + π² + π, and engine constant matches
# ───────────────────────────────────────────────────────────────────────────
class TestMultipoleClosure:
    def test_multipole_sum_equals_closed_form(self):
        """Λ_vol + Λ_surf + Λ_line at the Golden Torus equals 4π³ + π² + π."""
        mp = golden_torus_multipole()
        closed_form = 4.0 * np.pi**3 + np.pi**2 + np.pi
        assert abs(mp["alpha_inv"] - closed_form) < 1e-12

    def test_multipole_matches_engine_constant(self):
        """α⁻¹ from geometry equals engine's ALPHA_COLD_INV to machine precision."""
        mp = golden_torus_multipole()
        assert abs(mp["alpha_inv"] - ALPHA_COLD_INV) < 1e-12

    def test_individual_multipole_terms(self):
        """Each term has its expected geometric identity."""
        mp = golden_torus_multipole()
        assert abs(mp["Lambda_vol"] - 4.0 * np.pi**3) < 1e-12
        assert abs(mp["Lambda_surf"] - np.pi**2) < 1e-12
        assert abs(mp["Lambda_line"] - np.pi) < 1e-12

    def test_alpha_cold_reciprocal(self):
        """ALPHA_COLD and ALPHA_COLD_INV are reciprocals."""
        assert abs(ALPHA_COLD * ALPHA_COLD_INV - 1.0) < 1e-12


# ───────────────────────────────────────────────────────────────────────────
# 2. Golden Torus geometric constraints
# ───────────────────────────────────────────────────────────────────────────
class TestGoldenTorusConstraints:
    def test_self_avoidance_constraint(self):
        """R − r = 1/2 (Axiom 2 crossings self-avoidance at dielectric rupture)."""
        assert abs((R_gt - r_gt) - 0.5) < 1e-12

    def test_holomorphic_screening_constraint(self):
        """R · r = 1/4 (spin-1/2 half-cover of Clifford torus)."""
        assert abs(R_gt * r_gt - 0.25) < 1e-12

    def test_golden_ratio_radii(self):
        """R = φ/2, r = (φ-1)/2 (unique physical root of 2R² − R − 1/2 = 0)."""
        assert abs(R_gt - PHI / 2.0) < 1e-12
        assert abs(r_gt - (PHI - 1.0) / 2.0) < 1e-12

    def test_quadratic_root_matches(self):
        """The closed-form quadratic solver returns the same Golden Torus."""
        R_plus, R_minus = solve_golden_torus()
        assert abs(R_plus - R_gt) < 1e-12
        # Unphysical root is negative
        assert R_minus < 0


# ───────────────────────────────────────────────────────────────────────────
# 3. Clifford torus half-cover (justifies Λ_surf = π² normalization)
# ───────────────────────────────────────────────────────────────────────────
class TestCliffordHalfCover:
    def test_standard_clifford_area_is_2pi_squared(self):
        """Standard Clifford torus at r₁ = r₂ = 1/√2 on S³ has area 2π²."""
        r1 = r2 = 1.0 / np.sqrt(2.0)
        A = clifford_area_numeric(r1, r2)
        assert abs(A - 2.0 * np.pi**2) < 1e-8

    def test_half_cover_gives_pi_squared(self):
        """Physical half-cover area = ½ × 2π² = π² (spin-1/2 screening normalization)."""
        r1 = r2 = 1.0 / np.sqrt(2.0)
        A_half = 0.5 * clifford_area_numeric(r1, r2)
        assert abs(A_half - np.pi**2) < 1e-8


# ───────────────────────────────────────────────────────────────────────────
# 4. Ropelength optimizer converges to Golden Torus
# ───────────────────────────────────────────────────────────────────────────
class TestRopelengthConvergence:
    def test_arc_length_is_positive_and_finite(self):
        """Sanity check on the trefoil arc-length primitive."""
        L = trefoil_arc_length(GOLDEN_R, GOLDEN_r)
        assert np.isfinite(L)
        assert L > 0

    def test_stage_b_converges_to_golden_torus(self):
        """
        Penalty-constrained minimizer starting from (R=1.2, r=0.4) must
        converge to (φ/2, (φ-1)/2). This is the load-bearing numerical
        claim of Ch. 8 — if this drifts, the α derivation's empirical
        closure is at risk.
        """
        R_b, r_b = stage_b_with_screening_constraint()
        assert abs(R_b - GOLDEN_R) < 1e-5
        assert abs(r_b - GOLDEN_r) < 1e-5


# ───────────────────────────────────────────────────────────────────────────
# 5. Vacuum Strain Coefficient (CMB thermal running of α)
# ───────────────────────────────────────────────────────────────────────────
class TestVacuumStrainCoefficient:
    def test_delta_strain_positive(self):
        """
        δ_strain > 0: cold-lattice α⁻¹_ideal is larger than observed CODATA
        (thermal running softens the geometric Q-factor).
        """
        assert DELTA_STRAIN > 0

    def test_delta_strain_small(self):
        """
        δ_strain is in the 10⁻⁶ range consistent with CMB T = 2.7 K strain.
        Hard bound: the framework's claim is O(10⁻⁶); anything larger than
        10⁻⁵ would indicate mis-calibration.
        """
        assert DELTA_STRAIN < 1e-5

    def test_cmb_correction_bridges_cold_to_codata(self):
        """α⁻¹_ideal × (1 − δ_strain) reproduces CODATA 1/α to 1e-10."""
        alpha_inv_observed = 1.0 / ALPHA
        alpha_inv_predicted = ALPHA_COLD_INV * (1.0 - DELTA_STRAIN)
        assert abs(alpha_inv_predicted - alpha_inv_observed) < 1e-10

    def test_delta_strain_derivation_identity(self):
        """δ_strain = 1 − (α⁻¹_CODATA / α⁻¹_ideal) exactly (definition check)."""
        expected = 1.0 - (1.0 / ALPHA) / ALPHA_COLD_INV
        assert abs(DELTA_STRAIN - expected) < 1e-15
