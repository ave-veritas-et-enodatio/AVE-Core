"""
Phase 3f: Electron (2,3) torus knot bound-state test on FDTD3DEngine.

Per topology verification program at
research/2026-05-18_fundamental-topology-verification-program.md:
Tier 1 #1 — extends v14 Mode I PASS (validated on scalar MasterEquationFDTD)
to vector Maxwell FDTD3DEngine using (E, B) torus-knot seed.

Canonical electron specification per Vol 1 Ch 8 + Vol 2 Ch 1:
- Real-space: 0_1 unknot (toroidal loop, ropelength 2π·ℓ_node)
- Phase-space: (2,3) torus knot trefoil
- Self-linking SL = pq - p - q = 1
- Mass m_e c² = 511 keV = V_snap (per Axiom 4 magnetic snap)
- Chiral coupling κ_chiral = α · pq/(p+q) = α · 6/5

Seed construction (first-pass: simplified Beltrami-like E):
At each point on toroidal shell at major radius R, minor radius r:
- E field tangent to (2,3) torus knot direction × hedgehog envelope amplitude
- Power-law radial falloff (NOT Gaussian — AVE-canonical hedgehog)
- Let Maxwell evolution auto-generate B field via curl(E) coupling

Pre-registered outcomes:
- PASS: knot seed maintains amplitude + FWHM over 500+ timesteps;
  ringing frequency ~ ω_node Compton-scale
- PARTIAL: some persistence but slow dispersion
- NULL: identical to photon (Phase 3e); topology alone doesn't bind on
  vector engine; needs additional mechanism

Falsifier discipline: comparison test vs non-topological random-direction
baseline. Topology-driven binding requires bound knot seed to BIND while
random seed disperses.

Run:
    pytest src/tests/test_fdtd3d_electron_torus_knot_seed.py -v -s
"""

from __future__ import annotations

import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine


def _build_torus_knot_E_seed(engine, R, r, amplitude, p=2, q=3, knot_thickness=2.0):
    """Build vector E_x, E_y, E_z initial condition tracing (p,q) torus knot tangent.

    At each grid cell on the toroidal shell at (R, r) around lattice center:
    - Compute (p,q) torus knot tangent direction
    - Set E vector ∥ tangent direction
    - Apply hedgehog envelope (power-law falloff from torus shell)
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0

    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz

    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R)

    # Hedgehog envelope (power-law, AVE-canonical)
    envelope = amplitude / (1.0 + (rho_tube / knot_thickness) ** 2)

    # (p,q) knot tangent: t = p · d/dphi + q · d/dpsi
    dphi_x = -(R + r * np.cos(psi)) * np.sin(phi)
    dphi_y = (R + r * np.cos(psi)) * np.cos(phi)
    dphi_z = np.zeros_like(phi)
    dpsi_x = -r * np.sin(psi) * np.cos(phi)
    dpsi_y = -r * np.sin(psi) * np.sin(phi)
    dpsi_z = r * np.cos(psi) * np.ones_like(phi)

    t_x = p * dphi_x + q * dpsi_x
    t_y = p * dphi_y + q * dpsi_y
    t_z = p * dphi_z + q * dpsi_z
    t_mag = np.sqrt(t_x**2 + t_y**2 + t_z**2 + 1e-12)
    t_hat_x = t_x / t_mag
    t_hat_y = t_y / t_mag
    t_hat_z = t_z / t_mag

    # E vector ∥ knot tangent × envelope
    engine.Ex += envelope * t_hat_x
    engine.Ey += envelope * t_hat_y
    engine.Ez += envelope * t_hat_z


def _build_random_direction_baseline(engine, R, r, amplitude, knot_thickness=2.0):
    """Build same-envelope baseline with RANDOM direction per cell (no topology).

    Same hedgehog envelope as torus knot, but direction is random unit vector
    per cell. Should produce a non-bound (photon-like) dispersing seed.
    """
    rng = np.random.RandomState(42)
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0

    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz
    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R) ** 2 + z**2 + 1e-12)
    envelope = amplitude / (1.0 + (rho_tube / knot_thickness) ** 2)

    # Random unit vectors per cell
    rx = rng.randn(nx, ny, nz)
    ry = rng.randn(nx, ny, nz)
    rz = rng.randn(nx, ny, nz)
    rmag = np.sqrt(rx**2 + ry**2 + rz**2 + 1e-12)
    engine.Ex += envelope * rx / rmag
    engine.Ey += envelope * ry / rmag
    engine.Ez += envelope * rz / rmag


def _run_and_probe_amplitude(engine, n_steps, probe_every=20):
    """Run engine, track peak |E| amplitude over time (bound state would maintain)."""
    times = []
    peak_E = []
    total_E_sq = []
    for step in range(n_steps):
        engine.update_magnetic_field()
        engine.update_electric_field()
        engine.apply_mur_abc()
        if step % probe_every == 0:
            times.append(step * engine.dt)
            E_total_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
            peak_E.append(float(E_total_mag.max()))
            total_E_sq.append(float(np.sum(E_total_mag**2)))
    return np.array(times), np.array(peak_E), np.array(total_E_sq)


def test_electron_torus_knot_vs_random_baseline():
    """Compare (2,3) knot seed vs random-direction baseline on FDTD3DEngine."""
    N = 48
    DX = 0.01
    R = 8.0  # major radius in cells
    r = 3.0  # minor radius in cells
    AMPLITUDE = 0.5 * 43650.0 / DX  # ~0.5·V_yield/dx (moderate nonlinearity; 0.85 blew up)
    N_STEPS = 500
    PROBE_EVERY = 20

    # Run 1: (2,3) torus knot seed (electron-like)
    print("\n=== Run 1: (2,3) torus knot seed (electron-like) ===")
    engine_knot = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
    _build_torus_knot_E_seed(engine_knot, R, r, AMPLITUDE, p=2, q=3, knot_thickness=2.0)
    print(f"  Seed peak |E| = {np.sqrt(engine_knot.Ex**2+engine_knot.Ey**2+engine_knot.Ez**2).max():.3e} V/m")

    t_knot, peak_knot, total_knot = _run_and_probe_amplitude(engine_knot, N_STEPS, PROBE_EVERY)

    # Run 2: Random-direction baseline (same envelope, no topology)
    print("\n=== Run 2: Random-direction baseline (no topology) ===")
    engine_random = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
    _build_random_direction_baseline(engine_random, R, r, AMPLITUDE, knot_thickness=2.0)
    print(f"  Seed peak |E| = {np.sqrt(engine_random.Ex**2+engine_random.Ey**2+engine_random.Ez**2).max():.3e} V/m")

    t_rand, peak_rand, total_rand = _run_and_probe_amplitude(engine_random, N_STEPS, PROBE_EVERY)

    # Compare amplitude evolution
    initial_peak_knot = peak_knot[0]
    final_peak_knot = peak_knot[-1]
    initial_peak_rand = peak_rand[0]
    final_peak_rand = peak_rand[-1]

    knot_retention = final_peak_knot / initial_peak_knot
    rand_retention = final_peak_rand / initial_peak_rand

    print(f"\nResults over {N_STEPS} timesteps:")
    print(f"  (2,3) knot: peak |E| {initial_peak_knot:.3e} → {final_peak_knot:.3e} (retention {knot_retention:.3f})")
    print(f"  Random:     peak |E| {initial_peak_rand:.3e} → {final_peak_rand:.3e} (retention {rand_retention:.3f})")
    print(f"  Knot/Random retention ratio: {knot_retention/rand_retention:.3f}")
    print(f"  (2,3) knot max strain ratio: {engine_knot.max_strain_ratio:.4f}")
    print(f"  Random max strain ratio: {engine_random.max_strain_ratio:.4f}")

    # Outcome classification
    if knot_retention >= 0.8 * initial_peak_knot / initial_peak_knot:  # i.e., >= 80% of initial
        bound_outcome = "STRONG BIND (≥80% retention)"
    elif knot_retention >= 1.5 * rand_retention:
        bound_outcome = "PARTIAL BIND (knot retention 1.5× random)"
    elif knot_retention >= 0.9 * rand_retention:
        bound_outcome = "NULL (knot ~ random, photon-like)"
    else:
        bound_outcome = "FAIL (knot retention < random; topology DEGRADES localization)"
    print(f"\n  Outcome: {bound_outcome}")

    # Soft assertions
    assert peak_knot[0] > 0, "Knot seed initialization failed"
    assert peak_rand[0] > 0, "Random seed initialization failed"
    assert engine_knot.max_strain_ratio < 1.0, "Knot engine exceeded saturation cap"
    assert engine_random.max_strain_ratio < 1.0, "Random engine exceeded saturation cap"

    # Don't strict-assert specific outcome; document for inspection.
    # If knot retention << random, that's REAL DATA about topology insufficiency.


def test_engine_runs_with_knot_seed():
    """Smoke test: engine runs cleanly with (2,3) torus knot initial condition."""
    N = 32
    engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=0.01, linear_only=False, use_pml=False)
    _build_torus_knot_E_seed(engine, R=6.0, r=2.0, amplitude=0.5 * 43650.0 / 0.01, p=2, q=3, knot_thickness=2.0)
    peak_before = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2).max()

    # Run a few steps
    for _ in range(50):
        engine.update_magnetic_field()
        engine.update_electric_field()
        engine.apply_mur_abc()

    peak_after = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2).max()
    assert peak_before > 0, "Seed failed to initialize"
    assert peak_after > 0, "Engine produced no field after 50 steps"
    assert engine.max_strain_ratio > 0.0, "Saturation not engaged at high-amplitude knot seed"
    print(f"\nSmoke test PASS: peak |E| {peak_before:.3e} → {peak_after:.3e}, max_strain={engine.max_strain_ratio:.3f}")
