"""Keepers for the spectral-liveness diagnostic (ave-prereg Step 3.8 operational).

Prereg : research/2026-07-03_localization-readjudication_prereg.md §5.

Validates the diagnostic by REPRODUCING the 2026-07-03 verdict-exposure sweep
findings independently (the diamond L_D nullspace burden + the v14 sech's ~93%
nullspace projection) and by witnessing the srs instrument contrast (nullspace
dim = 1). These are the diagnostic's own liveness proof: it reads the KNOWN
degenerate case (diamond) high and the KNOWN well-posed case (srs) low.
"""

import numpy as np
import pytest

from ave.core.chiral_lattice import build_srs_net
from ave.solvers.native_cage_imex import assemble_L_D, build_grad_div_periodic
from ave.solvers.spectral_liveness import (
    localized_eigenmode,
    project_out_nullspace,
    spectral_liveness,
)
from ave.solvers.srs_cage_winding import assemble_L_srs, build_incidence


def _v14_sech(N, *, amp=0.85, radius=2.5, dx=0.5):
    c = N // 2
    coords = np.arange(N) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * dx
    return amp / np.cosh(r / radius)


def _diamond_L_D(N):
    Grad, Div = build_grad_div_periodic(N)
    return assemble_L_D(Grad, Div, np.ones(N**3))


def _srs_L(L):
    net = build_srs_net(L=L, enantiomorph="right")
    B, bonds = build_incidence(net)
    return assemble_L_srs(B, bonds, np.ones(net.n_nodes)), net


# ─────────────────────────────────────────────────────────────────────────────
# The diagnostic reproduces the EXPOSURE (diamond L_D is nullspace-heavy and the
# v14 sech projects dominantly onto the frozen kernel).
# ─────────────────────────────────────────────────────────────────────────────
def test_diamond_nullspace_heavy_reproduces_exposure():
    """L_D at N=12 has a large frozen kernel and the v14 sech sits mostly in it —
    the diagnostic must READ this (the exposure it exists to catch)."""
    N = 12
    L_D = _diamond_L_D(N)
    seed = _v14_sech(N)
    res = spectral_liveness(seed, L_D)
    # nullspace dim matches the independently-verified 16 at N=12.
    assert res.nullspace_dim == 16, res.nullspace_dim
    # the v14 sech dumps the dominant majority of its energy into the dead-leg.
    assert res.nullspace_energy_fraction > 0.85, res.nullspace_energy_fraction
    # so the operator-governed (live) fraction is a small minority.
    assert res.live_energy_fraction < 0.15, res.live_energy_fraction
    # fractions partition unity.
    assert abs(res.nullspace_energy_fraction + res.live_energy_fraction - 1.0) < 1e-10


def test_diamond_null_and_live_partition_and_orthogonality():
    """project_out_nullspace returns a field whose spectral-liveness has ~0
    nullspace fraction (it IS the operator-governed complement)."""
    N = 10
    L_D = _diamond_L_D(N)
    seed = _v14_sech(N)
    live = project_out_nullspace(seed, L_D)
    assert live.shape == seed.shape
    if np.linalg.norm(live) > 1e-9:
        res_live = spectral_liveness(live, L_D)
        assert res_live.nullspace_energy_fraction < 1e-6, res_live.nullspace_energy_fraction


# ─────────────────────────────────────────────────────────────────────────────
# The srs instrument CONTRAST: nullspace dim = 1 (constant mode), a localized
# seed is almost entirely live.
# ─────────────────────────────────────────────────────────────────────────────
def test_srs_nullspace_is_constant_mode_only():
    """L_srs at L=4 has nullspace dim 1 (the constant mode) — the sharp contrast
    with the diamond's 8-16 dim frozen kernel."""
    L_srs, net = _srs_L(4)
    # a delta-like localized node seed
    seed = np.zeros(net.n_nodes)
    seed[net.n_nodes // 2] = 1.0
    res = spectral_liveness(seed, L_srs)
    assert res.nullspace_dim == 1, res.nullspace_dim
    # a localized seed's only nullspace overlap is the tiny constant-mode piece.
    assert res.nullspace_energy_fraction < 0.05, res.nullspace_energy_fraction
    assert res.live_energy_fraction > 0.95, res.live_energy_fraction


def test_srs_smooth_core_is_mostly_live():
    """A smooth localized A1 core on srs is dominantly operator-governed — the
    diagnostic must read the srs readout as LIVE (unlike the diamond's 6.5%).

    FINDING (flag-don't-fix, verified L=4/6/8, L-INVARIANT): the sech core's
    live fraction is ~0.895 — the ~0.105 nullspace overlap is the seed's DC/
    constant content (an all-positive sech has a nonzero mean absorbed by the
    graph Laplacian's SINGLE constant-mode nullspace). This is NOT a frozen
    dead-leg like the diamond's 8-16 dim kernel — it is the physical DC overlap
    that the prereg §6.5 requires be REPORTED AND SUBTRACTED. The instrument
    contrast is decisive: 0.895 live (srs) vs 0.065 live (diamond) = 13.7×."""
    from ave.solvers.srs_cage_winding import SrsCageWinding, SrsCageWindingConfig

    eng = SrsCageWinding(SrsCageWindingConfig(L=4, winding_on=False))
    eng.seed_A1_sech(amplitude=0.85, radius=2.5)
    L_srs, _ = _srs_L(4)
    res = spectral_liveness(np.abs(eng.a_A1), L_srs)
    # decisively more live than the diamond (0.065); the ~0.105 shortfall is the
    # sech's DC/constant content, not a frozen kernel (nullspace dim = 1).
    assert res.live_energy_fraction > 0.85, res.live_energy_fraction
    assert res.live_energy_fraction > 10.0 * 0.065, res.live_energy_fraction  # ≫ diamond
    assert res.nullspace_dim == 1, res.nullspace_dim  # DC only, no dead-leg


# ─────────────────────────────────────────────────────────────────────────────
# localized_eigenmode: srs HAS a localized nonzero mode (route-1 positive control
# constructible); the diamond's frozen-kernel structure is exposed by contrast.
# ─────────────────────────────────────────────────────────────────────────────
def test_srs_has_localized_nonzero_eigenmode():
    """The srs operator admits a localized nonzero eigenmode — a route-1 positive
    control IS constructible on the canonical carrier."""
    L_srs, net = _srs_L(4)
    u, lam, frac = localized_eigenmode(L_srs, band="high", max_participation_frac=0.9)
    assert lam > 1e-9, lam
    assert 0.0 < frac < 0.9, frac
    # the mode is a genuine unit eigenvector.
    assert abs(np.linalg.norm(u) - 1.0) < 1e-8


def test_asymmetric_operator_rejected():
    """A non-symmetric operator is a caller error (the diagnostic assumes a
    div-form SPD stiffness)."""
    M = np.array([[1.0, 2.0], [0.0, 1.0]])  # not symmetric
    with pytest.raises(ValueError, match="not symmetric"):
        spectral_liveness(np.array([1.0, 0.0]), M)


def test_seed_size_mismatch_rejected():
    L_srs, net = _srs_L(4)
    with pytest.raises(ValueError, match="!= operator dim"):
        spectral_liveness(np.ones(net.n_nodes + 1), L_srs)
