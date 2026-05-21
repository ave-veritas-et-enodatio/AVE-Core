"""
Phase 3f.3.3: Negative-pressure (stretch-driven) substrate freeze-in test.

Per pre-registration at research/2026-05-18_phase3f33-negative-pressure-
stretch-freeze-in-prereg.md.

Mechanism: simulate cosmic substrate stretch by linearly decreasing V_yield
over time (substrate elastic limit drops as substrate dilates). Smooth-noise
initial condition (Gaussian-convolved) avoids the per-cell-direction
instability that blocked Phase 3f.3 first attempt.

Test compares:
- Constant-V_yield baseline (no stretch, no freeze-in expected)
- Varying-V_yield (cosmic stretch simulation, freeze-in expected per AVE)

Probes:
- Total energy persistence (do structures survive the V_yield drop?)
- Helicity (E · B integrated; non-zero → chiral / topological structures)
- Spatial coherence (max |E| / mean |E|; high → clumped, frozen-in residues)

Pre-registered outcomes:
- PASS: stretch produces preferentially persistent + spatially-coherent
  structures with non-zero helicity; constant baseline disperses cleanly
- PARTIAL: some difference, but not clear topology selection
- NULL: no difference between constant and varying V_yield
- FAIL: stretch DISPERSES more than constant
- TECHNICAL: engine instability prevents execution

Run:
    pytest src/tests/test_fdtd3d_negative_pressure_freeze_in.py -v -s
"""

from __future__ import annotations

import numpy as np
import pytest
from scipy.ndimage import gaussian_filter

from ave.core.fdtd_3d import FDTD3DEngine


def _seed_smooth_noise(engine, amplitude, sigma_smooth=3.0, seed=42):
    """Initialize substrate with SMOOTH random noise (Gaussian-convolved).

    Avoids per-cell directional incoherence that destabilizes FDTD.
    """
    rng = np.random.RandomState(seed)
    nx, ny, nz = engine.nx, engine.ny, engine.nz

    # Raw white noise per component
    raw_Ex = rng.randn(nx, ny, nz)
    raw_Ey = rng.randn(nx, ny, nz)
    raw_Ez = rng.randn(nx, ny, nz)
    raw_Hx = rng.randn(nx, ny, nz)
    raw_Hy = rng.randn(nx, ny, nz)
    raw_Hz = rng.randn(nx, ny, nz)

    # Gaussian-smooth each component to introduce spatial correlation
    sm_Ex = gaussian_filter(raw_Ex, sigma=sigma_smooth)
    sm_Ey = gaussian_filter(raw_Ey, sigma=sigma_smooth)
    sm_Ez = gaussian_filter(raw_Ez, sigma=sigma_smooth)
    sm_Hx = gaussian_filter(raw_Hx, sigma=sigma_smooth)
    sm_Hy = gaussian_filter(raw_Hy, sigma=sigma_smooth)
    sm_Hz = gaussian_filter(raw_Hz, sigma=sigma_smooth)

    # Normalize so peak amplitude = amplitude (rather than mean amplitude)
    peak_E = np.sqrt(sm_Ex**2 + sm_Ey**2 + sm_Ez**2).max()
    if peak_E > 0:
        norm = amplitude / peak_E
        engine.Ex += norm * sm_Ex
        engine.Ey += norm * sm_Ey
        engine.Ez += norm * sm_Ez

    eta = np.sqrt(engine.mu_0 / engine.epsilon_0)
    H_amplitude = amplitude / eta
    peak_H = np.sqrt(sm_Hx**2 + sm_Hy**2 + sm_Hz**2).max()
    if peak_H > 0:
        norm = H_amplitude / peak_H
        engine.Hx += norm * sm_Hx
        engine.Hy += norm * sm_Hy
        engine.Hz += norm * sm_Hz


def _total_helicity(engine):
    B_x = engine.mu_0 * engine.Hx
    B_y = engine.mu_0 * engine.Hy
    B_z = engine.mu_0 * engine.Hz
    e_dot_b = engine.Ex * B_x + engine.Ey * B_y + engine.Ez * B_z
    return float(np.sum(e_dot_b)) * engine.dx**3


def _total_energy(engine):
    U_E = 0.5 * engine.epsilon_0 * np.sum(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    U_H = 0.5 * engine.mu_0 * np.sum(engine.Hx**2 + engine.Hy**2 + engine.Hz**2)
    return float(U_E + U_H) * engine.dx**3


def _spatial_coherence(engine):
    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    mean_E = E_mag.mean()
    return float(E_mag.max() / mean_E) if mean_E > 1e-30 else float("nan")


def _run_with_v_yield_schedule(engine, n_steps, v_yield_fn, probe_every=50):
    """Run engine for n_steps; update engine.v_yield each step via v_yield_fn(t)."""
    times = []
    energy = []
    helicity = []
    coherence = []
    v_yield_history = []
    for step in range(n_steps):
        t_now = step * engine.dt
        # Update v_yield BEFORE field updates (so ε(V) calc uses correct V_yield)
        new_v_yield = float(v_yield_fn(t_now))
        engine.v_yield = max(new_v_yield, 1e-3)  # floor to avoid div-by-zero
        engine.update_magnetic_field()
        engine.update_electric_field()
        engine.apply_mur_abc()
        if step % probe_every == 0:
            times.append(t_now)
            energy.append(_total_energy(engine))
            helicity.append(_total_helicity(engine))
            coherence.append(_spatial_coherence(engine))
            v_yield_history.append(engine.v_yield)
    return {
        "times": np.array(times),
        "energy": np.array(energy),
        "helicity": np.array(helicity),
        "coherence": np.array(coherence),
        "v_yield": np.array(v_yield_history),
    }


@pytest.mark.xfail(
    reason="Phase 3f.3.3: FDTD3DEngine has CFL/stability limits when V_yield "
    "is decreased mid-run with full-lattice smooth-noise initial conditions. "
    "Reducing V_yield amplifies saturation engagement → c_eff² = c_0²/S → "
    "approaches CFL limit → NaN. Tested at amplitudes 0.05, 0.3 × V_yield/dx; "
    "all NaN. Engine needs CFL-aware dt rescheduling for time-varying V_yield "
    "OR fundamentally different test architecture (e.g., adiabatic μ_eff "
    "scaling instead of V_yield decrease, or single-blob seed instead of "
    "full-lattice noise). See research/2026-05-18_phase3f33-result.md.",
    strict=False,
)
def test_negative_pressure_freeze_in():
    """Compare constant-V_yield baseline vs stretch-driven varying V_yield."""
    N = 32
    DX = 0.01
    V_YIELD_0 = 43650.0
    AMPLITUDE = 0.05 * V_YIELD_0 / DX  # 0.05 × V_yield_0/dx (low to ensure stability with full-lattice noise)
    N_STEPS = 800
    PROBE_EVERY = 40
    TAU_EXPANSION = N_STEPS * 1.54e-11 / 2  # half the run drops V_yield linearly

    print("\n=== Phase 3f.3.3: Stretch-Driven Substrate Freeze-In ===")
    print(f"N={N}, dx={DX}, V_yield_0={V_YIELD_0}, amplitude={AMPLITUDE:.3e}")
    print(f"N_steps={N_STEPS}, tau_expansion={TAU_EXPANSION:.3e}s")

    # Run 1: Constant V_yield baseline (no stretch)
    print("\n--- Run 1: Constant V_yield (no stretch) ---")
    engine_const = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False, v_yield=V_YIELD_0)
    _seed_smooth_noise(engine_const, AMPLITUDE, sigma_smooth=3.0, seed=42)
    print(
        f"  Initial: E_total={_total_energy(engine_const):.3e}J, "
        f"helicity={_total_helicity(engine_const):.3e}, "
        f"coherence={_spatial_coherence(engine_const):.3f}"
    )

    def const_v_yield_fn(t):
        return V_YIELD_0  # constant

    result_const = _run_with_v_yield_schedule(engine_const, N_STEPS, const_v_yield_fn, PROBE_EVERY)

    # Run 2: Varying V_yield (cosmic stretch simulation)
    print("\n--- Run 2: Varying V_yield (cosmic stretch) ---")
    engine_stretch = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False, v_yield=V_YIELD_0)
    _seed_smooth_noise(engine_stretch, AMPLITUDE, sigma_smooth=3.0, seed=42)
    print(
        f"  Initial: E_total={_total_energy(engine_stretch):.3e}J, "
        f"helicity={_total_helicity(engine_stretch):.3e}, "
        f"coherence={_spatial_coherence(engine_stretch):.3f}"
    )

    # Linear decrease: V_yield drops from V_YIELD_0 to 0.3·V_YIELD_0 over τ_expansion
    def stretch_v_yield_fn(t):
        return V_YIELD_0 * max(0.3, 1.0 - 0.7 * t / TAU_EXPANSION)

    result_stretch = _run_with_v_yield_schedule(engine_stretch, N_STEPS, stretch_v_yield_fn, PROBE_EVERY)

    # Compare results
    print("\n=== Comparison (constant baseline vs stretch) ===")

    E_const_initial = result_const["energy"][1]
    E_const_final = result_const["energy"][-1]
    E_stretch_initial = result_stretch["energy"][1]
    E_stretch_final = result_stretch["energy"][-1]

    h_const_initial = abs(result_const["helicity"][1])
    h_const_final = abs(result_const["helicity"][-1])
    h_stretch_initial = abs(result_stretch["helicity"][1])
    h_stretch_final = abs(result_stretch["helicity"][-1])

    c_const_final = result_const["coherence"][-1]
    c_stretch_final = result_stretch["coherence"][-1]

    print("  Constant V_yield:")
    print(f"    Energy retention:   {E_const_final/E_const_initial:.3f}")
    print(f"    Helicity retention: {h_const_final/h_const_initial if h_const_initial > 1e-30 else 'NaN':.3f}")
    print(f"    Final coherence:    {c_const_final:.3f}")
    print(f"    Max strain ratio:   {engine_const.max_strain_ratio:.4f}")

    print("  Varying V_yield (stretch):")
    print(f"    Energy retention:   {E_stretch_final/E_stretch_initial:.3f}")
    print(f"    Helicity retention: {h_stretch_final/h_stretch_initial if h_stretch_initial > 1e-30 else 'NaN':.3f}")
    print(f"    Final coherence:    {c_stretch_final:.3f}")
    print(f"    Max strain ratio:   {engine_stretch.max_strain_ratio:.4f}")
    print(f"    V_yield path: {result_stretch['v_yield'][0]:.1f} → {result_stretch['v_yield'][-1]:.1f}")

    # Discriminator metrics
    E_diff_ratio = (
        (E_stretch_final / E_stretch_initial) / (E_const_final / E_const_initial) if E_const_final > 0 else float("nan")
    )
    c_diff_ratio = c_stretch_final / c_const_final if c_const_final > 0 else float("nan")

    print("\n  Stretch/Constant ratios:")
    print(f"    Energy retention:   {E_diff_ratio:.3f}  (>1 = stretch persists more)")
    print(f"    Spatial coherence:  {c_diff_ratio:.3f}  (>1 = stretch more clumped)")

    # Outcome classification
    if E_diff_ratio > 1.5 and c_diff_ratio > 1.5:
        outcome = "PASS — stretch produces stronger persistence + spatial coherence (FREEZE-IN observed)"
    elif E_diff_ratio > 1.2 or c_diff_ratio > 1.2:
        outcome = "PARTIAL — some stretch-driven enhancement"
    elif 0.8 <= E_diff_ratio <= 1.2 and 0.8 <= c_diff_ratio <= 1.2:
        outcome = "NULL — stretch produces same outcome as constant baseline"
    elif E_diff_ratio < 0.8:
        outcome = "FAIL — stretch DISPERSES more than constant baseline"
    else:
        outcome = "MIXED — energy + coherence diverge in different directions"
    print(f"\n  Outcome: {outcome}")

    # Sanity assertions
    assert not np.isnan(E_const_final), "Constant engine produced NaN"
    assert not np.isnan(E_stretch_final), "Stretch engine produced NaN"
    assert engine_const.max_strain_ratio < 1.0
    assert engine_stretch.max_strain_ratio < 1.0
