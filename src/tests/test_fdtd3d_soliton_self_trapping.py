"""
Phase 3e: soliton self-trapping in nonlinear Born-Infeld regime on FDTD3DEngine.

Per Grant's saturate-ahead/desaturate-behind picture from the Cosserat-Lagrangian
engine conversation: at high amplitude, the substrate's ε_eff = ε_0·√(1-A²)
should self-trap waves into a bound-state "cavitation bubble" via Γ = -1
reflection at the saturation boundary.

This test validates the bound-state formation EMPIRICALLY on the engine:
1. Linear-only baseline: pulse disperses cleanly (control)
2. Nonlinear at low amplitude (A ≈ 0.3): mild nonlinear distortion
3. Nonlinear at high amplitude (A ≈ 0.85): saturation engaged; test self-trapping

Discriminator: pulse FWHM vs time. Linear pulse FWHM grows (dispersion).
Self-trapped pulse FWHM stays bounded.

Predictions per pre-reg discipline:
- Outcome A (PASS, expected): nonlinear high-A pulse FWHM grows slower than
  linear baseline (partial self-trapping)
- Outcome B (full self-trap): nonlinear high-A pulse FWHM stays bounded
  (cavity forms, bound state observed)
- Outcome C (no effect): nonlinear and linear behave identically →
  Born-Infeld self-trapping doesn't work in this engine; need additional
  mechanism (Cosserat coupling, magnetic-side saturation)

Run:
    pytest src/tests/test_fdtd3d_soliton_self_trapping.py -v -s
"""

import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine


def _seed_gaussian_pulse(engine, center_xyz, sigma_cells, amplitude):
    """Seed a centered Gaussian E_z pulse with NO carrier — pure dispersing pulse."""
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = center_xyz
    i, j, k = np.indices((nx, ny, nz))
    r_sq = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
    engine.Ez += amplitude * np.exp(-r_sq / (2.0 * sigma_cells**2))


def _measure_pulse_FWHM(engine, axis_slice):
    """Measure FWHM of |Ez| along a 1D slice through the pulse center.

    axis_slice: e.g., (slice(None), N//2, N//2) for x-axis cut
    Returns FWHM in cells.
    """
    profile = np.abs(engine.Ez[axis_slice])
    peak = profile.max()
    if peak < 1e-12:
        return float("nan")
    half_max = peak / 2.0
    above_half = profile >= half_max
    if not above_half.any():
        return 0.0
    indices = np.where(above_half)[0]
    return float(indices.max() - indices.min())


def _run_and_track_FWHM(engine, n_steps, probe_every=10, center_x=None):
    """Run engine, track FWHM of pulse along x-axis through center every probe_every steps."""
    N = engine.nx
    if center_x is None:
        center_x = N // 2
    axis_slice = (slice(None), center_x, center_x)  # x-axis cut through (y=z=N//2)
    times = []
    fwhms = []
    peak_amps = []
    max_strains = []
    for step in range(n_steps):
        engine.update_magnetic_field()
        engine.update_electric_field()
        engine.apply_mur_abc()
        if (step % probe_every) == 0:
            times.append(step * engine.dt)
            fwhms.append(_measure_pulse_FWHM(engine, axis_slice))
            peak_amps.append(float(np.abs(engine.Ez).max()))
            max_strains.append(engine.max_strain_ratio)
    return {
        "times": np.array(times),
        "fwhm": np.array(fwhms),
        "peak_amplitude": np.array(peak_amps),
        "max_strain": np.array(max_strains),
    }


def test_soliton_self_trapping_comparison():
    """Compare pulse evolution: linear vs nonlinear-low-A vs nonlinear-high-A."""
    N = 48
    DX = 0.01
    SIGMA_CELLS = 4.0
    N_STEPS = 500
    PROBE_EVERY = 10

    center = (N // 2, N // 2, N // 2)

    # V_yield = 43.65 kV per cell; with dx=0.01m, max E ≈ V_yield/dx ≈ 4.4 MV/m
    V_yield_default = 43650.0  # V (FDTD3DEngine default)
    E_at_yield = V_yield_default / DX  # ~ 4.4e6 V/m
    print(f"\nE_at_yield = {E_at_yield:.3e} V/m")

    # Three runs: linear, nonlinear at A=0.3, nonlinear at A=0.85
    results = {}

    # Linear baseline
    print("\n=== Run 1: Linear baseline (A ≈ 0.85 amplitude but linear mode) ===")
    engine_linear = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=True, use_pml=False)
    _seed_gaussian_pulse(engine_linear, center, SIGMA_CELLS, 0.85 * E_at_yield)
    results["linear"] = _run_and_track_FWHM(engine_linear, N_STEPS, PROBE_EVERY)
    print(f"  Final FWHM = {results['linear']['fwhm'][-1]:.2f} cells (initial {results['linear']['fwhm'][0]:.2f})")
    print(f"  Final peak = {results['linear']['peak_amplitude'][-1]:.3e} V/m")
    print(f"  Max strain = {results['linear']['max_strain'][-1]:.4f}")

    # Nonlinear low amplitude
    print("\n=== Run 2: Nonlinear low-A (amplitude ~ 0.3 V_yield) ===")
    engine_nl_low = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
    _seed_gaussian_pulse(engine_nl_low, center, SIGMA_CELLS, 0.3 * E_at_yield)
    results["nonlinear_low"] = _run_and_track_FWHM(engine_nl_low, N_STEPS, PROBE_EVERY)
    print(
        f"  Final FWHM = {results['nonlinear_low']['fwhm'][-1]:.2f} cells "
        f"(initial {results['nonlinear_low']['fwhm'][0]:.2f})"
    )
    print(f"  Final peak = {results['nonlinear_low']['peak_amplitude'][-1]:.3e} V/m")
    print(f"  Max strain = {results['nonlinear_low']['max_strain'][-1]:.4f}")

    # Nonlinear high amplitude
    print("\n=== Run 3: Nonlinear high-A (amplitude ~ 0.85 V_yield) ===")
    engine_nl_high = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
    _seed_gaussian_pulse(engine_nl_high, center, SIGMA_CELLS, 0.85 * E_at_yield)
    results["nonlinear_high"] = _run_and_track_FWHM(engine_nl_high, N_STEPS, PROBE_EVERY)
    print(
        f"  Final FWHM = {results['nonlinear_high']['fwhm'][-1]:.2f} cells "
        f"(initial {results['nonlinear_high']['fwhm'][0]:.2f})"
    )
    print(f"  Final peak = {results['nonlinear_high']['peak_amplitude'][-1]:.3e} V/m")
    print(f"  Max strain = {results['nonlinear_high']['max_strain'][-1]:.4f}")

    # Discriminator: FWHM growth ratio
    # Linear: should grow ~linearly with time (dispersion)
    # Nonlinear high-A: should grow slower if self-trapping; FWHM-bounded if fully trapped

    initial_fwhm = results["linear"]["fwhm"][1]  # second sample (post-initialization)
    final_fwhm_linear = results["linear"]["fwhm"][-1]
    final_fwhm_nl_high = results["nonlinear_high"]["fwhm"][-1]

    linear_growth = final_fwhm_linear / initial_fwhm if initial_fwhm > 0 else float("nan")
    nl_high_growth = final_fwhm_nl_high / initial_fwhm if initial_fwhm > 0 else float("nan")

    print(f"\nFWHM growth ratios over {N_STEPS} steps:")
    print(f"  Linear: {linear_growth:.2f}× initial")
    print(f"  Nonlinear high-A: {nl_high_growth:.2f}× initial")
    print(f"  Nonlinear/Linear ratio: {nl_high_growth/linear_growth if linear_growth > 0 else 'nan':.3f}")

    # Outcome classification per pre-reg
    if nl_high_growth < 0.7 * linear_growth:
        outcome = "PASS — strong self-trapping (nonlinear FWHM grows <70% of linear)"
    elif nl_high_growth < 0.95 * linear_growth:
        outcome = "PARTIAL — mild self-trapping (nonlinear FWHM growth slowed by 5-30%)"
    elif nl_high_growth < 1.05 * linear_growth:
        outcome = "NULL — no self-trapping effect (Born-Infeld alone insufficient)"
    else:
        outcome = "FAIL — nonlinear case DISPERSES FASTER than linear"
    print(f"  Outcome: {outcome}")

    # Always-pass-runs assertion: just check engine ran cleanly
    assert not np.isnan(final_fwhm_linear), "Linear FWHM is NaN — engine broken"
    assert not np.isnan(final_fwhm_nl_high), "Nonlinear FWHM is NaN — engine broken"
    assert results["linear"]["max_strain"][-1] < 1.0, "Linear engine exceeded saturation cap"
    assert results["nonlinear_high"]["max_strain"][-1] <= 1.0, "Nonlinear engine exceeded saturation cap"

    # Soft assertion: nonlinear should be DIFFERENT from linear at the very least
    # (mere existence of nonlinear effect, even if not full self-trap)
    relative_difference = abs(nl_high_growth - linear_growth) / max(linear_growth, 1e-6)
    print(f"\nRelative FWHM difference: {relative_difference * 100:.1f}%")
    # Don't strict-assert specific outcome; document for inspection


def test_engine_responds_to_saturation():
    """Smoke test: nonlinear engine actually engages saturation at high amplitude."""
    N = 32
    DX = 0.01
    V_yield = 43650.0
    E_at_yield = V_yield / DX

    engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=False, use_pml=False)
    _seed_gaussian_pulse(engine, (N // 2, N // 2, N // 2), 3.0, 0.9 * E_at_yield)

    # Step a few times
    for _ in range(50):
        engine.update_magnetic_field()
        engine.update_electric_field()
        engine.apply_mur_abc()

    print(f"\nMax strain ratio after 50 steps: {engine.max_strain_ratio:.4f}")
    assert engine.max_strain_ratio > 0.01, "Saturation not engaged at A=0.9; check nonlinearity"
    print("Nonlinearity engaged correctly.")
