"""
Test suite for Topological Generators (src/ave/topological/borromean.py).

Validates the coordinate-geometry properties of the three fundamental
topological defects: unknot (electron), trefoil (antenna topology),
and Borromean link (proton).
"""

import numpy as np
import pytest

from ave.topological.borromean import FundamentalTopologies


# ---------------------------------------------------------------------------
# Unknot (0_1) — Fundamental lepton topology
# ---------------------------------------------------------------------------

class TestUnknot:
    """The 0_1 unknot: a single closed loop at minimum ropelength = 2π."""

    @pytest.fixture
    def coords(self):
        return FundamentalTopologies.generate_unknot_0_1(radius=1.0, resolution=500)

    def test_shape(self, coords):
        """Must return [N, 3] coordinate array."""
        assert coords.shape == (500, 3)

    def test_closed_curve(self, coords):
        """First and last points must coincide (closed loop)."""
        np.testing.assert_allclose(coords[0], coords[-1], atol=1e-10)

    def test_planar(self, coords):
        """Unknot lies in the XY plane (z = 0 identically)."""
        np.testing.assert_allclose(coords[:, 2], 0.0, atol=1e-15)

    def test_radius_scales(self):
        """Bounding radius scales with input parameter."""
        c1 = FundamentalTopologies.generate_unknot_0_1(radius=1.0)
        c2 = FundamentalTopologies.generate_unknot_0_1(radius=3.0)
        max_r1 = np.max(np.linalg.norm(c1, axis=1))
        max_r2 = np.max(np.linalg.norm(c2, axis=1))
        assert max_r2 == pytest.approx(3.0 * max_r1, rel=1e-6)

    def test_ropelength_is_2pi(self):
        """The unknot's ropelength (circumference/tube_diameter) = 2π for
        a tube whose radius equals r/(2π), giving ropelength = 2πr / (2·r/(2π)) = 2π²/... 
        Actually, the ropelength of the ideal tight unknot is exactly 2π.
        For a unit-radius circle, circumference = 2π, tube radius = 1 → ropelength = 2π/1 = 2π.
        We verify the circumference here as 2π·R."""
        coords = FundamentalTopologies.generate_unknot_0_1(radius=1.0, resolution=10000)
        diffs = np.diff(coords, axis=0)
        arc_lengths = np.linalg.norm(diffs, axis=1)
        circumference = np.sum(arc_lengths)
        assert circumference == pytest.approx(2 * np.pi, rel=1e-3)


# ---------------------------------------------------------------------------
# Trefoil (3_1) — NOT the electron; used for antenna topology
# ---------------------------------------------------------------------------

class TestTrefoil:
    """The 3_1 trefoil knot: used for HOPF-01 antenna, not the electron."""

    @pytest.fixture
    def coords(self):
        return FundamentalTopologies.generate_trefoil_3_1(radius=1.0, resolution=500)

    def test_shape(self, coords):
        assert coords.shape == (500, 3)

    def test_closed_curve(self, coords):
        np.testing.assert_allclose(coords[0], coords[-1], atol=1e-10)

    def test_not_planar(self, coords):
        """Trefoil must occupy 3D space (z ≠ 0 everywhere)."""
        assert np.max(np.abs(coords[:, 2])) > 0.01

    def test_normalized_bounding(self, coords):
        """Maximum extent should equal the requested radius."""
        max_r = np.max(np.linalg.norm(coords, axis=1))
        assert max_r == pytest.approx(1.0, rel=0.01)


# ---------------------------------------------------------------------------
# Borromean Link (6^3_2) — Proton topology
# ---------------------------------------------------------------------------

class TestBorromean:
    """The 6^3_2 Borromean link: three mutually interlocking rings."""

    @pytest.fixture
    def rings(self):
        return FundamentalTopologies.generate_borromean_6_3_2(radius=1.0, resolution=500)

    def test_returns_three_rings(self, rings):
        """Must return exactly 3 ring arrays."""
        assert len(rings) == 3

    def test_ring_shapes(self, rings):
        """Each ring must be [N, 3]."""
        for ring in rings:
            assert ring.shape == (500, 3)

    def test_each_ring_closed(self, rings):
        """Each ring must be a closed curve."""
        for ring in rings:
            np.testing.assert_allclose(ring[0], ring[-1], atol=1e-10)

    def test_mutually_perpendicular(self, rings):
        """The three rings should be oriented in approximately orthogonal planes."""
        # Ring 1: primarily XY, Ring 2: primarily YZ, Ring 3: primarily ZX
        # Check by looking at which axis has minimal variance per ring
        dominant_zero_axes = []
        for ring in rings:
            variances = np.var(ring, axis=0)
            dominant_zero_axes.append(np.argmin(variances))
        # All three axes should be represented
        assert len(set(dominant_zero_axes)) == 3

    def test_eccentricity_scales(self):
        """Increasing eccentricity should elongate the rings."""
        r_round = FundamentalTopologies.generate_borromean_6_3_2(1.0, eccentricity=1.0)
        r_flat = FundamentalTopologies.generate_borromean_6_3_2(1.0, eccentricity=2.0)
        # Ring 1: y extent should be larger with higher eccentricity
        y_extent_round = np.max(r_round[0][:, 1]) - np.min(r_round[0][:, 1])
        y_extent_flat = np.max(r_flat[0][:, 1]) - np.min(r_flat[0][:, 1])
        assert y_extent_flat > y_extent_round

    def test_rings_not_identical(self, rings):
        """All three rings must be geometrically distinct."""
        for i in range(3):
            for j in range(i + 1, 3):
                assert not np.allclose(rings[i], rings[j])
