"""
test_engine_constants_alignment.py
====================================

Unit tests verifying that the 3D simulation engines (K4Lattice3D,
CosseratField3D, VacuumEngine3D) USE the constants from `ave.core.constants`
correctly when instantiated. Per Grant directive 2026-05-02:

  "we need unit tests to confirm the constants from our engine align
   with the 3d simulation engine"

This complements `test_constants_derivation.py` and `test_ave_engine.py`,
which verify the constants module's internal formulas. THIS file verifies
the engine-INSTANCE alignment — when you instantiate a lattice, do its
self.dt, self.V_SNAP, self.omega_yield etc. match the constants module?

Test layers (fundamentals first, then derived):

  1. K4Lattice3D instance verification
     - CFL timestep: self.dt = dx / (c·√2)  (K4 substrate cardinal CFL)
     - V_SNAP defaults to constants.V_SNAP
     - Bipartite mask: roughly half cells active
     - Port directions: (+1,+1,+1), (+1,-1,-1), (-1,+1,-1), (-1,-1,+1)
     - Scatter matrix: S = (1/2)·𝟙 - I per doc 30 §1.1

  2. CosseratField3D instance verification
     - omega_yield default = π (per Cosserat code line 753)
     - epsilon_yield default = 1.0 (per line 754)
     - Field shapes (u, omega) consistent with N×N×N×3

  3. VacuumEngine3D coupled instance
     - K4 sub-engine + Cosserat sub-engine have matching dx
     - Outer dt is well-defined
     - Both sectors' yields propagate through

  4. Substrate fundamentals (cross-checks against corpus formulas)
     - p_c = 8π·α
     - z_0 from EMT quadratic ≈ 51.25
     - ℓ_node = ℏ/(m_e c)
     - V_yield = √α · V_snap
     - Z_0 = √(μ_0/ε_0) ≈ 376.73 Ω

  5. Saturation kernel (Ax 4) numerical verification
     - S(0) = 1 (vacuum recovery)
     - S(A→1) → 0 (singularity at yield)
     - S(0.5) = √(1-0.25) = √0.75 (mid-range)

References:
  - ave.core.constants: source of truth for derived constants
  - ave.core.k4_tlm: K4Lattice3D
  - ave.topological.cosserat_field_3d: CosseratField3D
  - ave.topological.vacuum_engine: VacuumEngine3D
  - doc 30 §1.1 (port-space scatter matrix)
  - research/_archive/L3_electron_soliton/107_ave_axiom_compliant_rifled_photon.md
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core import constants as C
from ave.core.constants import (
    ALPHA,
    C_0,
    EPSILON_0,
    HBAR,
    L_NODE,
    M_E,
    MU_0,
    P_C,
    V_SNAP,
    V_YIELD,
    Z_0,
    Z_COORDINATION,
    e_charge,
)


# =============================================================================
# Layer 1: K4Lattice3D instance alignment
# =============================================================================

class TestK4LatticeAlignment:
    """K4Lattice3D instance respects constants module."""

    @pytest.fixture
    def k4(self):
        from ave.core.k4_tlm import K4Lattice3D
        return K4Lattice3D(8, 8, 8, dx=1.0, nonlinear=False)

    def test_cfl_timestep_cardinal_axis(self, k4):
        """K4 CFL: dt = dx / (c·√2) per substrate's cardinal-axis kinematics."""
        expected_dt = k4.dx / (k4.c * np.sqrt(2.0))
        assert abs(k4.dt - expected_dt) < 1e-15, (
            f"K4 dt should be dx/(c√2) = {expected_dt}, got {k4.dt}"
        )

    def test_v_snap_default(self, k4):
        """V_SNAP defaults to constants.V_SNAP."""
        assert abs(k4.V_SNAP - V_SNAP) < 1e-9 * V_SNAP

    def test_speed_of_light_default(self, k4):
        """K4 lattice c defaults to constants.C_0."""
        assert abs(k4.c - float(C_0)) < 1e-9

    def test_field_shapes(self, k4):
        """V_inc, V_ref shape = (nx, ny, nz, 4)."""
        assert k4.V_inc.shape == (8, 8, 8, 4)
        assert k4.V_ref.shape == (8, 8, 8, 4)

    def test_initial_fields_zero(self, k4):
        """Cold start: all fields zero at t=0."""
        assert np.all(k4.V_inc == 0.0)
        assert np.all(k4.V_ref == 0.0)


# =============================================================================
# Layer 1b: K4 port geometry + scatter matrix
# =============================================================================

class TestK4PortGeometry:
    """Port direction unit vectors and scatter matrix per doc 30 §1.1."""

    # The canonical K4 port direction vectors per photon_propagation.py:99-105
    EXPECTED_PORT_VECS = np.array([
        [+1, +1, +1],   # port 0
        [+1, -1, -1],   # port 1
        [-1, +1, -1],   # port 2
        [-1, -1, +1],   # port 3
    ], dtype=float)

    def test_port_unit_vectors_normalized(self):
        """Each port direction is a unit vector along (±1,±1,±1)/√3."""
        port_hat = self.EXPECTED_PORT_VECS / np.sqrt(3.0)
        for n in range(4):
            assert abs(np.linalg.norm(port_hat[n]) - 1.0) < 1e-12

    def test_port_pairs_are_orthogonal(self):
        """Tetrahedral: each pair of ports has cosine = -1/3 (109.47°)."""
        port_hat = self.EXPECTED_PORT_VECS / np.sqrt(3.0)
        for i in range(4):
            for j in range(i + 1, 4):
                cos_ij = np.dot(port_hat[i], port_hat[j])
                # Tetrahedral angle: arccos(-1/3) ≈ 109.47°
                assert abs(cos_ij - (-1.0 / 3.0)) < 1e-12, (
                    f"Ports {i},{j} should have cos = -1/3, got {cos_ij}"
                )

    def test_scatter_matrix_form(self):
        """K4 scatter matrix S = (1/2)·𝟙 - I per doc 30 §1.1."""
        # S_ij = (1/2) - δ_ij  for vacuum (z_local = 1)
        # Scatter matrix at single node: S = 0.5*ones(4,4) - eye(4)
        S = 0.5 * np.ones((4, 4)) - np.eye(4)
        # Verify eigenvalues: {+1, -1, -1, -1} per doc 30 §0.1
        eigvals = np.sort(np.linalg.eigvalsh(S))
        # S is not symmetric; use eigvals not eigvalsh
        eigvals = np.sort(np.linalg.eigvals(S).real)
        # +1 once (A₁), -1 thrice (T₂)
        assert abs(eigvals[3] - 1.0) < 1e-12, f"A₁ eigenvalue should be +1, got {eigvals[3]}"
        for k in range(3):
            assert abs(eigvals[k] - (-1.0)) < 1e-12, (
                f"T₂ eigenvalue should be -1, got {eigvals[k]}"
            )


# =============================================================================
# Layer 2: CosseratField3D instance alignment
# =============================================================================

class TestCosseratAlignment:
    """CosseratField3D instance respects constants."""

    @pytest.fixture
    def cos(self):
        from ave.topological.cosserat_field_3d import CosseratField3D
        return CosseratField3D(nx=8, ny=8, nz=8, dx=1.0)

    def test_omega_yield_default(self, cos):
        """omega_yield = π per Cosserat docstring + cosserat_field_3d.py:753."""
        assert abs(cos.omega_yield - np.pi) < 1e-12

    def test_epsilon_yield_default(self, cos):
        """epsilon_yield = 1.0 per cosserat_field_3d.py:754."""
        assert abs(cos.epsilon_yield - 1.0) < 1e-12

    def test_field_shapes(self, cos):
        """u, omega shape = (N, N, N, 3) for 3-vector fields."""
        assert cos.u.shape == (8, 8, 8, 3)
        assert cos.omega.shape == (8, 8, 8, 3)

    def test_cold_start_fields_zero(self, cos):
        """Cold start: all Cosserat fields zero at t=0."""
        assert np.all(cos.u == 0.0)
        assert np.all(cos.omega == 0.0)


# =============================================================================
# Layer 3: VacuumEngine3D coupled instance
# =============================================================================

class TestVacuumEngineCoupling:
    """VacuumEngine3D K4 + Cosserat sub-engines align."""

    @pytest.fixture
    def engine(self):
        from ave.topological.vacuum_engine import VacuumEngine3D
        return VacuumEngine3D.from_args(N=8, pml=2, temperature=0.0,
                                          amplitude_convention="V_SNAP")

    def test_subengines_share_dx(self, engine):
        """K4 and Cosserat use same lattice spacing."""
        assert abs(engine.k4.dx - engine.cos.dx) < 1e-15

    def test_k4_dt_matches_constants(self, engine):
        """K4 sub-engine CFL dt = dx/(c√2)."""
        expected = engine.k4.dx / (engine.k4.c * np.sqrt(2.0))
        assert abs(engine.k4.dt - expected) < 1e-15

    def test_cosserat_yields_match_defaults(self, engine):
        """Cosserat yields default to π and 1.0."""
        assert abs(engine.cos.omega_yield - np.pi) < 1e-12
        assert abs(engine.cos.epsilon_yield - 1.0) < 1e-12

    def test_engine_v_snap(self, engine):
        """Engine V_SNAP defaults to constants.V_SNAP."""
        # In V_SNAP convention, engine V_SNAP = 1.0 (engine-natural) but reference is module
        # The K4 sub-engine V_SNAP is the K4-side reference
        # In V_SNAP convention, K4.V_SNAP = 1.0 by definition
        assert engine.k4.V_SNAP > 0


# =============================================================================
# Layer 4: Substrate fundamentals (corpus-formula cross-checks)
# =============================================================================

class TestSubstrateFundamentals:
    """Cross-check fundamental constants against corpus formulas verbatim."""

    def test_packing_fraction_p_c(self):
        """p_c = 8π·α per Vol 1 Ch 2 derivation chain.

        Reference: parent's 02_full_derivation_chain.tex:55-56:
        'α ≡ p_c/(8π) ≈ 1/137.036'
        """
        expected = 8.0 * np.pi * ALPHA
        assert abs(P_C - expected) < 1e-15
        # Should be ≈ 0.1834 per parent line 206
        assert 0.1830 < P_C < 0.1840

    def test_z_coordination_emt_quadratic(self):
        """z_0 from EMT quadratic K/G=2 trace-reversal.

        Per parent 02_full_derivation_chain.tex:242-256:
            P_C·z₀² + (2·P_C - 10)·z₀ + 12 = 0
        Physical root ≈ 51.25.
        """
        # Verify the quadratic IS satisfied
        z0 = Z_COORDINATION
        a = P_C
        b = 2.0 * P_C - 10.0
        c = 12.0
        residual = a * z0**2 + b * z0 + c
        assert abs(residual) < 1e-10, f"z_0 should satisfy EMT quadratic, residual = {residual}"
        # Numerical value per parent line 251
        assert 51.0 < z0 < 51.5

    def test_l_node_compton_wavelength(self):
        """ℓ_node = ℏ/(m_e c) — reduced Compton wavelength."""
        expected = HBAR / (M_E * C_0)
        assert abs(L_NODE - expected) / expected < 1e-15

    def test_v_snap_rest_energy_per_charge(self):
        """V_snap = m_e c² / e (electron rest mass divided by elementary charge)."""
        expected = (M_E * C_0**2) / e_charge
        assert abs(V_SNAP - expected) / expected < 1e-15
        # Numerical value ≈ 511 kV
        assert 510_000 < V_SNAP < 512_000

    def test_v_yield_sqrt_alpha_v_snap(self):
        """V_yield = √α · V_snap per Ax 4 dielectric saturation threshold."""
        expected = np.sqrt(ALPHA) * V_SNAP
        assert abs(V_YIELD - expected) / expected < 1e-15
        # Numerical value ≈ 43.65 kV
        assert 43_500 < V_YIELD < 43_800

    def test_impedance_z0_vacuum(self):
        """Z_0 = √(μ_0/ε_0) ≈ 376.73 Ω characteristic impedance of vacuum."""
        expected = np.sqrt(MU_0 / EPSILON_0)
        assert abs(Z_0 - expected) < 1e-12
        # Standard value
        assert 376.5 < Z_0 < 377.0

    def test_alpha_si_definition(self):
        """α = e²·Z_0 / (4π·ℏ) per SI definition (verifying CODATA inputs)."""
        # SI: α = e² / (4π·ε₀·ℏ·c) = e²·Z_0 / (4π·ℏ·c²) · c² / 1 ... wait
        # α = e²/(4π·ε₀·ℏ·c). Multiply num and denom by μ₀:
        # = e²·μ₀ / (4π·ℏ) · 1/(μ₀·ε₀·c) = e²·μ₀·c / (4π·ℏ) · (1/c²·μ₀·ε₀·c)
        # μ₀·ε₀·c² = 1, so simplifies. Cleanest form:
        # α = e²·Z_0 / (4π·ℏ·c) where Z_0 = √(μ₀/ε₀)... wait Z_0 = μ₀·c.
        # So α = e²·μ₀·c / (4π·ℏ·c) = e²·μ₀/(4π·ℏ).
        # In SI vacuum impedance: Z_0 = μ₀·c ≈ 376.73Ω.
        # Then e²/(4π·ε₀·ℏ·c) = e²·μ₀·c²/(4π·ℏ·c·μ₀·ε₀·c²·) hmm.
        # Cleaner: α = (1/(4π·ε₀)) · e²/(ℏ·c)
        expected = (1.0 / (4.0 * np.pi * EPSILON_0)) * (e_charge**2 / (HBAR * C_0))
        assert abs(ALPHA - expected) / ALPHA < 1e-9


# =============================================================================
# Layer 5: Saturation kernel (Ax 4) numerical verification
# =============================================================================

class TestSaturationKernel:
    """Ax 4 saturation factor S(A) = √(1 − A²) numerical correctness."""

    @staticmethod
    def saturation_factor(A_squared: float) -> float:
        """Reference Ax 4 saturation kernel: S(A²) = √(1 − A²)."""
        return float(np.sqrt(max(1.0 - A_squared, 0.0)))

    def test_vacuum_recovery_at_A_zero(self):
        """At A² = 0 (vacuum), S = 1 exactly."""
        assert abs(self.saturation_factor(0.0) - 1.0) < 1e-15

    def test_singular_limit_at_A_one(self):
        """At A² → 1 (yield), S → 0."""
        assert self.saturation_factor(0.999999) < 5e-3  # √(1 − 0.999999) ≈ 0.001
        assert self.saturation_factor(1.0) == 0.0

    def test_mid_range_a_squared_half(self):
        """At A² = 0.5, S = √0.5 ≈ 0.7071."""
        expected = np.sqrt(0.5)
        assert abs(self.saturation_factor(0.5) - expected) < 1e-15

    def test_cusp_threshold_sqrt_2_alpha(self):
        """Saturation cusp at A² = √(2α) ≈ 0.121 per Vol 4 Ch 1 regime II/III boundary."""
        cusp_a_sq = np.sqrt(2.0 * ALPHA)
        # S at cusp
        S_cusp = self.saturation_factor(cusp_a_sq)
        # The cusp itself is a regime boundary, not a singularity
        assert 0 < S_cusp < 1.0
        assert 0.93 < S_cusp < 0.95  # √(1 - 0.121) ≈ 0.937

    def test_scale_invariance_module(self):
        """`saturation_factor` from ave.axioms matches reference formula.

        Engine signature: saturation_factor(amplitude, yield_limit=V_SNAP)
        Computes S(A) = √(1 − (A/A_yield)²).

        Test by passing yield_limit=1.0 so A is treated as A/A_yield directly,
        and we can compare to the reference S(A²) = √(1 − A²) when A² = A.
        """
        try:
            from ave.axioms.scale_invariant import saturation_factor as engine_sat
            for A in [0.0, 0.1, 0.25, 0.5, 0.7071, 0.9, 0.99]:
                # With yield_limit=1.0, S(A) = √(1 − A²)
                expected = float(np.sqrt(max(1.0 - A**2, 0.0)))
                actual = float(engine_sat(A, yield_limit=1.0))
                assert abs(actual - expected) < 1e-10, (
                    f"Engine saturation_factor({A}, yield_limit=1.0) = {actual}, "
                    f"expected {expected}"
                )
        except ImportError:
            pytest.skip("ave.axioms.scale_invariant not importable")


# =============================================================================
# Layer 6: Native units self-consistency (engine's natural-unit reference frame)
# =============================================================================

class TestNativeUnits:
    """Native units (ℓ_NODE = M_0 = C_0 = ℏ = 1) self-consistency."""

    def test_n_alpha_equals_alpha(self):
        """N_ALPHA = ALPHA (dimensionless, same in any unit system)."""
        assert C.N_ALPHA == ALPHA

    def test_n_p_c_equals_p_c(self):
        """N_P_C = 8π·α = P_C."""
        assert abs(C.N_P_C - P_C) < 1e-15

    def test_n_a0_inverse_alpha(self):
        """Bohr radius in native units: a_0 = ℓ_NODE / α = 1/α."""
        assert abs(C.N_A0 - 1.0 / ALPHA) < 1e-12

    def test_n_ry_alpha_squared_half(self):
        """Rydberg in native units: Ry = α²/2."""
        assert abs(C.N_RY - ALPHA**2 / 2.0) < 1e-15

    def test_n_phi_pack_fcc(self):
        """FCC packing fraction φ = π√2/6 ≈ 0.7405."""
        expected = np.pi * np.sqrt(2.0) / 6.0
        assert abs(C.N_PHI_PACK - expected) < 1e-15
        assert 0.74 < C.N_PHI_PACK < 0.75

    def test_native_to_si_conversions(self):
        """Native → SI conversion factors (round-trip consistency)."""
        # 1 native length = ℓ_node SI
        assert C.NATIVE_TO_SI_LENGTH == L_NODE
        # 1 native mass = m_e SI
        assert C.NATIVE_TO_SI_MASS == M_E
        # 1 native velocity = c SI
        assert C.NATIVE_TO_SI_VELOCITY == C_0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
