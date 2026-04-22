"""
Test VacuumGrid and Topological Combiner
=========================================

Tests for the core VacuumGrid (2D wave equation) and the NucleonCombiner
(Euler rotation + translation for nuclear assembly).
"""

import numpy as np
import pytest
from ave.core.grid import VacuumGrid
from ave.topological.combiner import NucleonCombiner


# ═══════════════════════════════════════════════════════════════════════
# VacuumGrid
# ═══════════════════════════════════════════════════════════════════════


class TestVacuumGrid:
    def test_initial_strain_is_zero(self):
        g = VacuumGrid(10, 10)
        assert np.allclose(g.strain_z, 0.0)

    def test_inject_strain(self):
        g = VacuumGrid(10, 10)
        g.inject_strain(5, 5, 1.0)
        assert g.get_local_strain(5, 5) == pytest.approx(1.0)

    def test_boundary_injection_stays_zero(self):
        g = VacuumGrid(10, 10)
        g.inject_strain(0, 0, 1.0)  # Should be suppressed (boundary)
        assert g.get_local_strain(0, 0) == pytest.approx(0.0)

    def test_step_propagates_energy(self):
        g = VacuumGrid(20, 20)
        g.inject_strain(10, 10, 10.0)
        g.step_kinematic_wave_equation(damping=1.0)
        # After one step, energy should spread to neighbors
        assert g.get_local_strain(10, 10) < 10.0
        assert g.get_local_strain(11, 10) != 0.0

    def test_temperature_setting(self):
        g = VacuumGrid(10, 10, thermal_mode="boundary")
        g.set_temperature(1.0)
        assert g.temperature == 1.0

    def test_bulk_thermal_mode_sets_correctly(self):
        g = VacuumGrid(20, 20, thermal_mode="bulk")
        g.set_temperature(1.0)
        assert g.thermal_mode == "bulk"
        assert g.temperature == 1.0
        # Step runs without error
        g.step_kinematic_wave_equation()


# ═══════════════════════════════════════════════════════════════════════
# NucleonCombiner
# ═══════════════════════════════════════════════════════════════════════


class TestNucleonCombiner:
    def test_rotate_identity(self):
        mesh = np.eye(3)
        rotated = NucleonCombiner.rotate_mesh(mesh, (0, 0, 0))
        np.testing.assert_allclose(rotated, mesh, atol=1e-12)

    def test_rotate_preserves_norm(self):
        mesh = np.random.randn(10, 3)
        rotated = NucleonCombiner.rotate_mesh(mesh, (0.5, 1.0, 0.3))
        norms_orig = np.linalg.norm(mesh, axis=1)
        norms_rot = np.linalg.norm(rotated, axis=1)
        np.testing.assert_allclose(norms_rot, norms_orig, atol=1e-10)

    def test_translate(self):
        mesh = np.zeros((5, 3))
        shifted = NucleonCombiner.translate_mesh(mesh, (1.0, 2.0, 3.0))
        expected = np.tile([1.0, 2.0, 3.0], (5, 1))
        np.testing.assert_allclose(shifted, expected)

    def test_assemble_cluster_non_empty(self):
        def dummy_gen(radius=1.0):
            return [np.random.randn(10, 3)]

        placements = [
            {"shift": (0, 0, 0), "label": "p1"},
            {"shift": (1, 0, 0), "rot": (0, np.pi / 2, 0), "label": "p2"},
        ]
        cluster = NucleonCombiner.assemble_cluster(dummy_gen, placements)
        assert len(cluster) == 2
        assert cluster[0]["label"] == "p1"
        assert cluster[1]["label"] == "p2"
