"""
Phase 3b validation: ρ(Σ|E|², Σ|B|²) ≈ -1 on FDTD3DEngine cavity test.

Per Phase 3 architectural pivot at
research/2026-05-18_phase3-architectural-pivot.md: the canonical Op14
ρ = -0.99 "Cosserat ↔ K4-inductive" trading IS the textbook E-B cavity
energy oscillation in a resonant cavity, computed automatically by full-
vector Maxwell FDTD via the curl equations.

This test validates that the existing FDTD3DEngine reproduces the textbook
ρ ≈ -1 cavity result, demonstrating the architectural pivot is correct
(no Cosserat-coupled engine needed; standard Maxwell does this for free).

Run:
    pytest src/tests/test_fdtd3d_cavity_e_b_correlation.py -v -s
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.fdtd_3d import FDTD3DEngine

# Lattice + sim params
N = 32
DX = 0.01  # 1 cm cells — well within linear regime for moderate E
N_STEPS = 1500
PROBE_EVERY = 1

# Acceptance criteria
RHO_THRESHOLD = -0.9  # textbook cavity ρ(E², B²) ≈ -1; allow margin for boundary leakage + discretization


def pearson_r(x, y):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if len(x) < 2:
        return float("nan")
    xm, ym = x.mean(), y.mean()
    xv, yv = ((x - xm) ** 2).sum(), ((y - ym) ** 2).sum()
    if xv == 0 or yv == 0:
        return float("nan")
    return float(((x - xm) * (y - ym)).sum() / np.sqrt(xv * yv))


def total_E_sq(engine):
    """Total electric field energy proxy: Σ(|E|²)."""
    return float(np.sum(engine.Ex**2 + engine.Ey**2 + engine.Ez**2))


def total_B_sq(engine):
    """Total magnetic field energy proxy: Σ(|B|²) = μ_0²·Σ(|H|²)."""
    H_sq = float(np.sum(engine.Hx**2 + engine.Hy**2 + engine.Hz**2))
    return engine.mu_0**2 * H_sq


def _run_cavity(engine, n_steps, seed_amplitude=1.0, sigma=3.0, apply_abc=True):
    """Run FDTD with Gaussian E_z seed; return (E²) and (B²) time series."""
    i, j, k = np.indices((engine.nx, engine.ny, engine.nz))
    center = engine.nx // 2
    r_sq = (i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2
    engine.Ez += seed_amplitude * np.exp(-r_sq / (2.0 * sigma**2))

    E_sq_series = []
    B_sq_series = []
    for _ in range(n_steps):
        engine.update_magnetic_field()
        engine.update_electric_field()
        if apply_abc:
            engine.apply_mur_abc()
        else:
            # PEC walls: tangential E = 0 at boundaries
            engine.Ex[:, 0, :] = 0
            engine.Ex[:, -1, :] = 0
            engine.Ex[:, :, 0] = 0
            engine.Ex[:, :, -1] = 0
            engine.Ey[0, :, :] = 0
            engine.Ey[-1, :, :] = 0
            engine.Ey[:, :, 0] = 0
            engine.Ey[:, :, -1] = 0
            engine.Ez[0, :, :] = 0
            engine.Ez[-1, :, :] = 0
            engine.Ez[:, 0, :] = 0
            engine.Ez[:, -1, :] = 0
        E_sq_series.append(total_E_sq(engine))
        B_sq_series.append(total_B_sq(engine))
    return np.array(E_sq_series), np.array(B_sq_series)


def test_textbook_cavity_E_B_anticorrelation_PEC():
    """ρ(Σ|E|², Σ|B|²) ≈ -1 on closed PEC cavity (textbook EE result, no absorption)."""
    engine = FDTD3DEngine(
        nx=N,
        ny=N,
        nz=N,
        dx=DX,
        linear_only=True,
        use_pml=False,
    )

    print(f"\nPEC cavity test: N={N}, dx={DX}, dt={engine.dt:.3e}, N_STEPS={N_STEPS}")

    E_sq, B_sq = _run_cavity(engine, N_STEPS, seed_amplitude=1.0, sigma=3.0, apply_abc=False)

    # Post-transient: skip first 20% (let the wave settle into cavity modes)
    skip = len(E_sq) // 5
    E_post = E_sq[skip:]
    B_post = B_sq[skip:]

    rho = pearson_r(E_post, B_post)

    print(f"  PEC ρ(Σ|E|², Σ|B|²) = {rho:.4f}  [textbook: ≈ -1]")
    print(f"  Σ|E|² mean = {E_post.mean():.3e}, std = {E_post.std():.3e}")
    print(f"  Σ|B|² mean = {B_post.mean():.3e}, std = {B_post.std():.3e}")

    assert rho <= RHO_THRESHOLD, f"PEC cavity ρ = {rho:.4f} not at textbook -1; expected ≤ {RHO_THRESHOLD}"


def test_E_B_anticorrelation_with_ABC():
    """ρ(Σ|E|², Σ|B|²) on open lattice with Mur ABCs.

    With ABC absorbing waves at boundaries, energy drains over time and the
    correlation degrades from textbook -1. ρ ≈ -0.7 to -0.9 is expected.
    """
    engine = FDTD3DEngine(
        nx=N,
        ny=N,
        nz=N,
        dx=DX,
        linear_only=True,
        use_pml=False,
    )

    print(f"\nABC test: N={N}, dx={DX}, dt={engine.dt:.3e}, N_STEPS={N_STEPS}")

    E_sq, B_sq = _run_cavity(engine, N_STEPS, seed_amplitude=1.0, sigma=3.0, apply_abc=True)

    skip = len(E_sq) // 5
    E_post = E_sq[skip:]
    B_post = B_sq[skip:]
    rho = pearson_r(E_post, B_post)

    print(f"  ABC ρ(Σ|E|², Σ|B|²) = {rho:.4f}  [expected: -0.7 to -0.9 (boundary leakage)]")

    # Looser threshold for ABC case (boundary absorption degrades cavity ρ)
    assert rho <= -0.7, f"ABC cavity ρ = {rho:.4f}; expected ≤ -0.7"


def test_engine_initializes():
    """Smoke test: FDTD3DEngine instantiates with PML enabled."""
    engine = FDTD3DEngine(nx=16, ny=16, nz=16, dx=0.01, use_pml=True, pml_layers=4)
    assert engine.Ex.shape == (16, 16, 16)
    assert engine.Hx.shape == (16, 16, 16)
    assert engine.dt > 0
    assert engine.use_pml
    print(f"\nEngine: nx={engine.nx}, dt={engine.dt:.3e}, PML layers={engine.pml_layers}")
