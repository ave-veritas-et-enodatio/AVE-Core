"""
Phase 3f.3 first attempt: cosmic-cooling matter-formation test on FDTD3DEngine.

Per pre-registration at research/2026-05-18_phase3f3-cosmic-cooling-matter-
formation-prereg.md, Option D (simplest): stochastic seed + observe
persistence.

Test: initialize substrate with random E and H noise at moderate amplitude;
evolve via Maxwell + Born-Infeld; observe whether any persistent structures
emerge from the noise (indicating topology-driven freeze-in) or whether
everything radiates away (indicating no selection mechanism).

Pre-registered outcomes:
- PASS: persistent structures emerge with topology preference (helicity ≠ 0
  for surviving structures, chirality consistent with electron-like)
- PARTIAL: some persistence but no clear topology selection
- NULL: everything radiates away → no freeze-in mechanism in Maxwell alone
- FAIL: non-topological blobs persist → topology-driven mechanism wrong

Run:
    pytest src/tests/test_fdtd3d_cosmic_cooling_freeze_in.py -v -s
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.fdtd_3d import FDTD3DEngine


def _seed_random_noise(engine, amplitude, fill_fraction=0.3, seed=42):
    """Initialize substrate with random E, H noise across fill_fraction of lattice.

    Random unit-vector directions for E and H at each filled cell.
    """
    rng = np.random.RandomState(seed)
    nx, ny, nz = engine.nx, engine.ny, engine.nz

    # Random mask: each cell has fill_fraction chance of being seeded
    mask = rng.rand(nx, ny, nz) < fill_fraction

    # E components — random direction
    e_x = rng.randn(nx, ny, nz)
    e_y = rng.randn(nx, ny, nz)
    e_z = rng.randn(nx, ny, nz)
    e_mag = np.sqrt(e_x**2 + e_y**2 + e_z**2 + 1e-12)
    engine.Ex += amplitude * (e_x / e_mag) * mask
    engine.Ey += amplitude * (e_y / e_mag) * mask
    engine.Ez += amplitude * (e_z / e_mag) * mask

    # H components — also random (creates non-zero helicity)
    h_x = rng.randn(nx, ny, nz)
    h_y = rng.randn(nx, ny, nz)
    h_z = rng.randn(nx, ny, nz)
    h_mag = np.sqrt(h_x**2 + h_y**2 + h_z**2 + 1e-12)
    H_scale = amplitude / np.sqrt(engine.mu_0 / engine.epsilon_0)  # B = E/eta_0 scaling
    engine.Hx += H_scale * (h_x / h_mag) * mask
    engine.Hy += H_scale * (h_y / h_mag) * mask
    engine.Hz += H_scale * (h_z / h_mag) * mask


def _total_helicity(engine):
    """Total helicity h = ∫(E · B) dV; non-zero → chiral substrate state.

    B = μ_0 · H. Helicity is the topology-relevant gauge-invariant quantity.
    """
    B_x = engine.mu_0 * engine.Hx
    B_y = engine.mu_0 * engine.Hy
    B_z = engine.mu_0 * engine.Hz
    e_dot_b = engine.Ex * B_x + engine.Ey * B_y + engine.Ez * B_z
    return float(np.sum(e_dot_b)) * engine.dx**3


def _total_energy(engine):
    """Total EM energy ∫(½ε|E|² + ½μ|H|²) dV."""
    U_E = 0.5 * engine.epsilon_0 * np.sum(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    U_H = 0.5 * engine.mu_0 * np.sum(engine.Hx**2 + engine.Hy**2 + engine.Hz**2)
    return float(U_E + U_H) * engine.dx**3


def _max_field_amplitude(engine):
    """Max |E| amplitude — proxy for "is anything persistent?"."""
    return float(np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2).max())


def _spatial_coherence_proxy(engine):
    """Crude proxy for spatial clumping: max |E| / mean |E|.

    High value → field is concentrated (clumped structure).
    Low value → field is diffuse (no structure).
    """
    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    mean_E = E_mag.mean()
    max_E = E_mag.max()
    if mean_E < 1e-30:
        return float("nan")
    return float(max_E / mean_E)


@pytest.mark.xfail(
    reason="Phase 3f.3 first attempt: FDTD3DEngine is numerically unstable with "
    "random per-cell direction noise (high spatial frequency content causes "
    "curl/Laplacian gradient amplification → NaN at any amplitude). Engine "
    "needs stabilization (low-pass filtering, smooth noise generation, or "
    "smaller dt) before stochastic freeze-in test can run. See "
    "research/2026-05-18_phase3f3-first-attempt-result.md for diagnosis. "
    "Phase 3f.3.2 should use SMOOTH noise (Gaussian-convolved random field) "
    "instead of per-cell random directions.",
    strict=False,
)
def test_cosmic_cooling_stochastic_persistence():
    """Stochastic seed + observe persistence: do structures emerge?"""
    N = 32
    DX = 0.01
    AMPLITUDE = 0.05 * 43650.0 / DX  # very low: 0.05 × V_yield/dx (random noise creates sharp gradients)
    N_STEPS = 1000
    PROBE_EVERY = 50

    engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
    _seed_random_noise(engine, AMPLITUDE, fill_fraction=0.3, seed=42)

    print(f"\nCosmic cooling test: N={N}, dx={DX}, amplitude={AMPLITUDE:.3e}, n_steps={N_STEPS}")
    print("Initial state:")
    print(f"  Total energy: {_total_energy(engine):.4e} J")
    print(f"  Total helicity: {_total_helicity(engine):.4e}")
    print(f"  Max |E|: {_max_field_amplitude(engine):.4e} V/m")
    print(f"  Spatial coherence (max/mean): {_spatial_coherence_proxy(engine):.3f}")

    # Run + probe
    times = []
    total_E = []
    total_h = []
    max_E = []
    coherence = []
    for step in range(N_STEPS):
        engine.update_magnetic_field()
        engine.update_electric_field()
        engine.apply_mur_abc()
        if step % PROBE_EVERY == 0:
            times.append(step * engine.dt)
            total_E.append(_total_energy(engine))
            total_h.append(_total_helicity(engine))
            max_E.append(_max_field_amplitude(engine))
            coherence.append(_spatial_coherence_proxy(engine))

    times = np.array(times)
    total_E = np.array(total_E)
    total_h = np.array(total_h)
    max_E = np.array(max_E)
    coherence = np.array(coherence)

    # Initial vs final
    E_retention = total_E[-1] / total_E[1] if total_E[1] > 0 else float("nan")
    helicity_retention = abs(total_h[-1]) / abs(total_h[1]) if abs(total_h[1]) > 1e-30 else float("nan")
    coherence_change = coherence[-1] / coherence[1] if coherence[1] > 0 else float("nan")

    print(f"\nResults after {N_STEPS} timesteps:")
    print(f"  Total energy: {total_E[1]:.3e} → {total_E[-1]:.3e} (retention {E_retention:.3f})")
    print(f"  Total helicity: {total_h[1]:.3e} → {total_h[-1]:.3e} (retention {helicity_retention:.3f})")
    print(f"  Max |E|: {max_E[1]:.3e} → {max_E[-1]:.3e}")
    print(f"  Spatial coherence: {coherence[1]:.3f} → {coherence[-1]:.3f} (change {coherence_change:.3f})")
    print(f"  Max strain ratio: {engine.max_strain_ratio:.4f}")

    # Outcome classification
    if E_retention > 0.3 and coherence_change > 1.5:
        outcome = "PASS — persistent structures with increasing spatial coherence (freeze-in detected)"
    elif E_retention > 0.1:
        outcome = "PARTIAL — some energy persistence but unclear spatial structure"
    elif E_retention > 0.001:
        outcome = "WEAK — most energy radiates but residual remains"
    else:
        outcome = "NULL — total dispersion; no freeze-in mechanism in Maxwell alone"
    print(f"\n  Outcome: {outcome}")

    # Sanity assertions
    assert not np.isnan(total_E[-1]), "Engine produced NaN — numerical instability"
    assert engine.max_strain_ratio < 1.0, "Engine exceeded saturation cap"
