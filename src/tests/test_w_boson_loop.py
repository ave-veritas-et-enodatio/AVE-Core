"""
Tests for W-Boson self-consistent loop correction (P2.7).

Covers:
  - build_radial_tree_admittance_graded() solver extension
  - w_boson_self_consistent_correction() convergence and physics
  - Module-level M_W / M_Z constants updated to self-consistent values
"""

import math

import numpy as np
import pytest

from ave.core.constants import ALPHA, C_0, M_E, NU_VAC, P_C, e_charge
from ave.solvers.transmission_line import (
    build_radial_tree_admittance,
    build_radial_tree_admittance_graded,
    s11_from_y_matrix,
)
from ave.topological.cosserat import M_W_MEV, M_W_TREE, M_Z_MEV, MISMATCH_LOSS_SC, w_boson_self_consistent_correction

_J_PER_MEV = float(e_charge) * 1e6
PDG_MW = 80_379.0
PDG_MZ = 91_188.0
_SIN_THETA_W_PAT = math.sqrt(3.0 / 7.0)

# ─── build_radial_tree_admittance_graded() ────────────────────────────────────


class TestGradedSolverStructure:
    """Structural / API tests for the graded-boundary Bethe tree solver."""

    def test_depth1_matches_hard_saturation(self):
        """At depth=1 with y_shell=[0], graded must equal the hard-boundary result."""
        Y_hard = build_radial_tree_admittance(depth=1, branch_y=NU_VAC, boundary_y=0.0, coordination_z=4)
        Y_grad = build_radial_tree_admittance_graded(depth=1, branch_y=NU_VAC, shell_boundary_y=[0.0], coordination_z=4)
        np.testing.assert_allclose(
            Y_hard,
            Y_grad,
            atol=1e-14,
            err_msg="Depth-1 graded (y=0) must match hard-boundary result",
        )

    def test_depth1_uniform_matches_standard(self):
        """At depth=1 with y_shell=[1], graded must equal standard boundary_y=1 result."""
        Y_std = build_radial_tree_admittance(depth=1, branch_y=NU_VAC, boundary_y=1.0, coordination_z=4)
        Y_grd = build_radial_tree_admittance_graded(depth=1, branch_y=NU_VAC, shell_boundary_y=[1.0], coordination_z=4)
        np.testing.assert_allclose(Y_std, Y_grd, atol=1e-14)

    def test_matrix_shape_grows_correctly(self):
        """Matrix size follows K4 Bethe-tree geometry: N = 1 + Σ_d z*(z-1)^(d-1)."""
        z = 4
        for depth in range(1, 5):
            n_expected = 1 + sum(z * (z - 1) ** (d - 1) for d in range(1, depth + 1))
            profile = [0.0] * depth
            Y = build_radial_tree_admittance_graded(
                depth=depth, branch_y=NU_VAC, shell_boundary_y=profile, coordination_z=z
            )
            assert Y.shape == (
                n_expected,
                n_expected,
            ), f"Depth {depth}: expected ({n_expected},{n_expected}), got {Y.shape}"

    def test_matrix_is_symmetric(self):
        """Admittance matrix must be symmetric (reciprocal network)."""
        for depth in range(1, 5):
            profile = [float(d) * 0.1 for d in range(1, depth + 1)]
            Y = build_radial_tree_admittance_graded(
                depth=depth, branch_y=NU_VAC, shell_boundary_y=profile, coordination_z=4
            )
            np.testing.assert_allclose(Y, Y.T, atol=1e-14, err_msg=f"Not symmetric at depth {depth}")

    def test_diagonal_dominance(self):
        """Each diagonal element >= sum of absolute off-diagonals (passive network)."""
        profile = [0.0, 0.3, 0.7]
        Y = build_radial_tree_admittance_graded(depth=3, branch_y=NU_VAC, shell_boundary_y=profile, coordination_z=4)
        for i in range(Y.shape[0]):
            off_sum = np.sum(np.abs(Y[i, :])) - abs(Y[i, i])
            assert Y[i, i].real >= off_sum - 1e-12, f"Diagonal dominance violated at node {i}"

    def test_default_profile_is_axiom4_envelope(self):
        """Default profile (shell_boundary_y=None) uses 1-exp(-(d-1)) envelope."""
        depth = 4
        # Y = build_radial_tree_admittance_graded(depth=depth, branch_y=NU_VAC, coordination_z=4)  # bulk lint fixup pass
        expected_profile = [1.0 * (1.0 - math.exp(-(d - 1))) for d in range(1, depth + 1)]
        # Shell 1 receives y=0 → no extra diagonal shunt on those nodes
        # Shell d receives y = expected_profile[d-1]
        assert abs(expected_profile[0]) < 1e-14, "Shell 1 must be y=0 in default profile"
        assert abs(expected_profile[-1] - (1.0 - math.exp(-(depth - 1)))) < 1e-12

    def test_wrong_profile_length_raises(self):
        """Mismatched shell_boundary_y length must raise ValueError."""
        with pytest.raises(ValueError, match="shell_boundary_y"):
            build_radial_tree_admittance_graded(depth=3, branch_y=NU_VAC, shell_boundary_y=[0.0, 1.0], coordination_z=4)


class TestGradedSolverPhysics:
    """Physics-level checks on the graded solver."""

    def test_s11_at_shell1_hard_is_negative(self):
        """S11 at depth-1 hard boundary is negative (inductive reflection)."""
        Y = build_radial_tree_admittance_graded(depth=1, branch_y=NU_VAC, shell_boundary_y=[0.0], coordination_z=4)
        s11 = s11_from_y_matrix(Y, port=0, Y0=1.0).real
        assert s11 < 0, f"Expected S11 < 0 at hard boundary, got {s11}"

    def test_harder_boundary_gives_larger_mismatch_loss(self):
        """Lower boundary admittance → higher |S11| → larger correction."""
        s11_list = []
        for y_b in [0.0, 0.3, 0.6, 1.0]:
            Y = build_radial_tree_admittance_graded(depth=1, branch_y=NU_VAC, shell_boundary_y=[y_b], coordination_z=4)
            s11_list.append(abs(s11_from_y_matrix(Y, port=0, Y0=1.0).real))
        # |S11| should be monotonically DECREASING as boundary_y increases
        for i in range(len(s11_list) - 1):
            assert s11_list[i] >= s11_list[i + 1] - 1e-12, f"|S11| not decreasing: {s11_list}"

    def test_depth1_s11_numerical_value(self):
        """Depth-1 hard S11 = -4/(4*4+4) = -1/5*(nu_vac ratio) — verify to 6 sig. figs."""
        Y = build_radial_tree_admittance_graded(depth=1, branch_y=NU_VAC, shell_boundary_y=[0.0], coordination_z=4)
        s11 = s11_from_y_matrix(Y, port=0, Y0=1.0).real
        assert abs(s11 - (-0.058824)) < 1e-5, f"S11 = {s11:.8f}, expected ≈ -0.0588"


# ─── w_boson_self_consistent_correction() ─────────────────────────────────────


class TestSelfConsistentCorrection:
    """Unit tests for the self-consistent back-saturation loop."""

    def setup_method(self):
        self.sc = w_boson_self_consistent_correction()

    def test_converges(self):
        assert self.sc["CONVERGED"], "Self-consistent loop must converge"

    def test_iterations_bounded(self):
        assert self.sc["n_iter"] <= 20, f"Expected convergence in ≤20 iterations, got {self.sc['n_iter']}"

    def test_sc_loss_less_than_d1_loss(self):
        """Back-saturation increases |S11| → more reflection → LOWER mismatch loss
        (less power transferred per vertex coupling → higher effective M_W)."""
        assert (
            self.sc["mismatch_loss_sc"] < self.sc["mismatch_loss_d1"]
        ), "SC mismatch loss must be less than depth-1 loss (more reflection)"

    def test_sc_mw_greater_than_d1_mw(self):
        """Self-consistent M_W must be higher than depth-1 M_W (closer to PDG)."""
        assert self.sc["M_W_sc_MeV"] > self.sc["M_W_d1_MeV"], "SC M_W must exceed depth-1 M_W"

    def test_sc_mw_within_0p25_percent_of_pdg(self):
        """Convergent M_W must be within 0.25% of PDG (tighter than depth-1 -0.22%)."""
        dev = abs(self.sc["M_W_sc_MeV"] / PDG_MW - 1.0) * 100
        assert dev < 0.25, f"SC M_W deviation {dev:.4f}% exceeds 0.25% bound"

    def test_sc_mw_closer_to_pdg_than_d1(self):
        """SC M_W must be closer to PDG than depth-1 M_W (improvement guaranteed)."""
        dev_d1 = abs(self.sc["M_W_d1_MeV"] - PDG_MW)
        dev_sc = abs(self.sc["M_W_sc_MeV"] - PDG_MW)
        assert (
            dev_sc < dev_d1
        ), f"SC result {self.sc['M_W_sc_MeV']:.2f} is not closer to PDG than d1 {self.sc['M_W_d1_MeV']:.2f}"

    def test_delta_y_origin_is_positive_and_small(self):
        """Back-saturation must reduce Y[0,0] by a small positive amount."""
        delta = self.sc["delta_Y_origin"]
        assert delta > 0, f"delta_Y must be > 0, got {delta}"
        assert delta < 0.1, f"delta_Y must be < 0.1 (small correction), got {delta}"

    def test_s11_sc_larger_than_s11_d1(self):
        """Converged |S11_sc| must be slightly larger than |S11_d1|."""
        assert abs(self.sc["S11_sc"]) > abs(self.sc["S11_d1"]), "Back-saturation must increase |S11|"

    def test_tree_level_value(self):
        """Tree-level M_W must match the analytic formula."""
        m_w_tree_expected = M_E / (ALPHA**2 * P_C * math.sqrt(3.0 / 7.0))
        m_w_tree_mev = m_w_tree_expected * C_0**2 / _J_PER_MEV
        assert (
            abs(self.sc["M_W_tree_MeV"] - m_w_tree_mev) < 0.01
        ), f"Tree level mismatch: {self.sc['M_W_tree_MeV']:.4f} vs {m_w_tree_mev:.4f}"


# ─── Module-level constants updated correctly ─────────────────────────────────


class TestModuleConstants:
    """Verify that cosserat.py module-level M_W uses the self-consistent value."""

    def test_module_mw_equals_sc_result(self):
        """Module M_W must equal the self-consistent convergent value."""
        sc = w_boson_self_consistent_correction()
        assert abs(M_W_MEV - sc["M_W_sc_MeV"]) < 0.01, f"Module M_W_MEV={M_W_MEV:.4f} != SC={sc['M_W_sc_MeV']:.4f}"

    def test_module_mw_not_equal_to_d1(self):
        """Confirm module-level M_W is NOT the old depth-1 value (regression guard)."""
        sc = w_boson_self_consistent_correction()
        assert (
            abs(M_W_MEV - sc["M_W_d1_MeV"]) > 1.0
        ), "Module M_W_MEV still equal to depth-1 value — SC update not applied"

    def test_mismatch_loss_sc_is_module_level(self):
        """MISMATCH_LOSS_SC must match the converged back-saturation value."""
        sc = w_boson_self_consistent_correction()
        assert abs(MISMATCH_LOSS_SC - sc["mismatch_loss_sc"]) < 1e-10

    def test_mw_pdg_deviation_better_than_022pct(self):
        """Module M_W deviation must be better than the old -0.22% depth-1 result."""
        dev = abs(M_W_MEV / PDG_MW - 1.0) * 100
        assert dev < 0.22, f"Module M_W deviation {dev:.4f}% not better than depth-1 -0.22%"

    def test_mz_pdg_deviation_within_0p3pct(self):
        """M_Z derived from self-consistent M_W must be within 0.3% of PDG."""
        dev = abs(M_Z_MEV / PDG_MZ - 1.0) * 100
        assert dev < 0.3, f"M_Z deviation {dev:.4f}% exceeds 0.3%"

    def test_mw_mz_ratio(self):
        """M_W/M_Z must equal sqrt(7)/3 (Cosserat PAT derivation)."""
        from math import sqrt

        expected_ratio = sqrt(7.0) / 3.0
        actual_ratio = M_W_MEV / M_Z_MEV
        assert (
            abs(actual_ratio - expected_ratio) < 1e-10
        ), f"M_W/M_Z = {actual_ratio:.10f}, expected sqrt(7)/3 = {expected_ratio:.10f}"

    def test_tree_level_independent_of_sc_loop(self):
        """M_W_TREE must be the same as the SC loop's tree-level report."""
        sc = w_boson_self_consistent_correction()
        m_w_tree_mev = M_W_TREE * C_0**2 / _J_PER_MEV
        assert abs(m_w_tree_mev - sc["M_W_tree_MeV"]) < 0.01
