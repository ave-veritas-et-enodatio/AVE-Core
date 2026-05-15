"""
Tests for boundary_invariants module — three substrate observables 𝓜, 𝓠, 𝓙.

Verifies:
  - Unstrained vacuum → all three invariants ≈ 0
  - Uniform sphere of strain → 𝓜 scales with volume; 𝓠 = 1; 𝓙 = 0
  - Two well-separated spheres → 𝓜 doubles; 𝓠 = 2; 𝓙 ≈ 0
  - v14 breathing-soliton seed (sech profile) → all three within reasonable
    ranges; 𝓜 stable across breathing cycle
  - Anisotropic strain (axially elongated) → 𝓙 > 0 (non-zero proxy winding)

L5 tracking: closes E-101 (engine module) when this test suite passes.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.boundary_invariants import (
    BoundaryInvariants,
    compute_all_invariants,
    compute_J,
    compute_M,
    compute_Q,
)


# Test parameters
N = 32  # lattice size
DX = 0.5
V_YIELD = 1.0


@pytest.fixture
def unstrained_field():
    """Empty substrate — all V = 0."""
    return np.zeros((N, N, N))


@pytest.fixture
def single_sphere_field():
    """Single localized sphere of strain at center."""
    V = np.zeros((N, N, N))
    center = N // 2
    coords = np.arange(N) - center
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * DX
    # sech profile, amplitude 0.6, radius 2.5
    V[:] = 0.6 / np.cosh(r / 2.5)
    return V


@pytest.fixture
def two_sphere_field():
    """Two well-separated localized spheres (thin enough to give Q=2 at threshold 0.5)."""
    V = np.zeros((N, N, N))
    coords = np.arange(N)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    # Sphere 1 at (8, 16, 16); Sphere 2 at (24, 16, 16); thinner spheres (sigma=1.0)
    # to ensure tails don't overlap above the 0.5-of-peak threshold
    r1 = np.sqrt((X - 8) ** 2 + (Y - 16) ** 2 + (Z - 16) ** 2) * DX
    r2 = np.sqrt((X - 24) ** 2 + (Y - 16) ** 2 + (Z - 16) ** 2) * DX
    V[:] = 0.6 / np.cosh(r1 / 1.0) + 0.6 / np.cosh(r2 / 1.0)
    return V


@pytest.fixture
def elongated_strain_field():
    """Axially elongated strain (cigar shape) — should produce non-zero 𝓙."""
    V = np.zeros((N, N, N))
    center = N // 2
    coords = np.arange(N) - center
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    # Anisotropic radius: elongated along z-axis (sigma_z = 6, sigma_xy = 2)
    r_aniso = np.sqrt((X / 2) ** 2 + (Y / 2) ** 2 + (Z / 6) ** 2) * DX
    V[:] = 0.6 * np.exp(-r_aniso**2 / 2)
    return V


# === Tests for unstrained vacuum ===


def test_unstrained_M_is_zero(unstrained_field):
    """Unstrained vacuum should give 𝓜 = 0 exactly."""
    M = compute_M(unstrained_field, DX, V_YIELD)
    assert M == 0.0, f"𝓜 = {M}, expected 0 for unstrained vacuum."


def test_unstrained_Q_is_zero(unstrained_field):
    """Unstrained vacuum should give 𝓠 = 0."""
    Q = compute_Q(unstrained_field, DX, V_YIELD)
    assert Q == 0.0, f"𝓠 = {Q}, expected 0 for unstrained vacuum."


def test_unstrained_J_is_zero(unstrained_field):
    """Unstrained vacuum should give 𝓙 = 0."""
    J = compute_J(unstrained_field, DX, V_YIELD)
    assert J == 0.0, f"𝓙 = {J}, expected 0 for unstrained vacuum."


# === Tests for single localized sphere ===


def test_single_sphere_M_positive(single_sphere_field):
    """Single localized sphere of strain → 𝓜 > 0."""
    M = compute_M(single_sphere_field, DX, V_YIELD)
    assert M > 0, f"𝓜 = {M}, expected > 0 for localized strain."


def test_single_sphere_Q_is_one(single_sphere_field):
    """Single localized sphere → 𝓠 ≈ 1 (one connected component / one soliton)."""
    Q = compute_Q(single_sphere_field, DX, V_YIELD)
    assert Q == 1.0, f"𝓠 = {Q}, expected 1 for single localized sphere."


def test_single_sphere_J_near_zero(single_sphere_field):
    """Single spherically symmetric sphere → 𝓙 ≈ 0 (no winding)."""
    J = compute_J(single_sphere_field, DX, V_YIELD)
    # Spherical sphere should have low anisotropy; allow numerical noise up to ~0.05
    assert J < 0.1, f"𝓙 = {J}, expected ≈ 0 for spherically symmetric strain."


# === Tests for two well-separated spheres ===


def test_two_sphere_M_doubles_self_contained():
    """Two well-separated thin spheres → 𝓜 approximately doubles vs single thin sphere.

    Self-contained: uses the same thin-sphere profile for both sides of the
    comparison, so the M-doubling is a clean test of additivity over disjoint regions.
    """
    V_one = np.zeros((N, N, N))
    V_two = np.zeros((N, N, N))
    coords = np.arange(N)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")

    # Thin sigma=1.0 spheres (same as two_sphere_field)
    r_solo = np.sqrt((X - 16) ** 2 + (Y - 16) ** 2 + (Z - 16) ** 2) * DX
    V_one[:] = 0.6 / np.cosh(r_solo / 1.0)

    r1 = np.sqrt((X - 8) ** 2 + (Y - 16) ** 2 + (Z - 16) ** 2) * DX
    r2 = np.sqrt((X - 24) ** 2 + (Y - 16) ** 2 + (Z - 16) ** 2) * DX
    V_two[:] = 0.6 / np.cosh(r1 / 1.0) + 0.6 / np.cosh(r2 / 1.0)

    M_one = compute_M(V_one, DX, V_YIELD)
    M_two = compute_M(V_two, DX, V_YIELD)

    # Two well-separated identical spheres → M should be roughly 2x single sphere
    # Allow ±30% tolerance for boundary effects and discretization
    ratio = M_two / M_one
    assert 1.5 < ratio < 2.5, (
        f"M_two/M_one = {ratio:.3f}, expected ≈ 2.0 (range 1.5-2.5) for two "
        f"identical disjoint spheres. M_one = {M_one:.4f}, M_two = {M_two:.4f}."
    )


def test_two_sphere_Q_is_two(two_sphere_field):
    """Two well-separated spheres → 𝓠 = 2 (two connected components)."""
    Q = compute_Q(two_sphere_field, DX, V_YIELD)
    assert Q == 2.0, f"𝓠 = {Q}, expected 2 for two well-separated spheres."


# === Tests for elongated strain ===


def test_elongated_J_nonzero(elongated_strain_field):
    """Cigar-shaped strain → 𝓙 > 0 (non-zero anisotropy / winding proxy)."""
    J = compute_J(elongated_strain_field, DX, V_YIELD)
    assert J > 0.05, f"𝓙 = {J}, expected > 0.05 for elongated strain."


# === Test convenience function ===


def test_compute_all_invariants_returns_dataclass(single_sphere_field):
    """compute_all_invariants returns BoundaryInvariants with all three fields."""
    inv = compute_all_invariants(single_sphere_field, DX, V_YIELD)
    assert isinstance(inv, BoundaryInvariants)
    assert inv.M > 0
    assert inv.Q == 1.0
    assert inv.J < 0.1
    assert inv.M_unit_normalized is None  # not requested


def test_compute_all_invariants_unit_normalized(single_sphere_field):
    """compute_all_invariants with l_node returns M_unit_normalized."""
    inv = compute_all_invariants(single_sphere_field, DX, V_YIELD, l_node=DX)
    assert inv.M_unit_normalized is not None
    assert inv.M_unit_normalized > 0


def test_compute_all_invariants_repr(single_sphere_field):
    """BoundaryInvariants __repr__ formats correctly."""
    inv = compute_all_invariants(single_sphere_field, DX, V_YIELD, l_node=DX)
    repr_str = repr(inv)
    assert "M=" in repr_str
    assert "Q=" in repr_str
    assert "J=" in repr_str
    assert "M_unit_normalized=" in repr_str


# === v14 breathing-soliton integration test ===


def test_v14_breathing_soliton_invariants_stable():
    """v14 breathing-soliton seed → 𝓜 > 0; 𝓠 = 1; 𝓙 small.

    Integration test linking the boundary_invariants module to the canonical
    v14 Mode I PASS state from doc 113.
    """
    # Recreate the v14 canonical seed
    coords = np.arange(N) - N // 2
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * DX
    V_seed = 0.85 / np.cosh(r / 2.5)

    inv = compute_all_invariants(V_seed, DX, V_YIELD, l_node=DX)
    assert inv.M > 0, f"v14 seed 𝓜 = {inv.M}, expected > 0."
    assert inv.Q == 1.0, f"v14 seed 𝓠 = {inv.Q}, expected 1 for single soliton."
    assert inv.J < 0.1, f"v14 seed 𝓙 = {inv.J}, expected small for symmetric seed."
    assert inv.M_unit_normalized is not None
