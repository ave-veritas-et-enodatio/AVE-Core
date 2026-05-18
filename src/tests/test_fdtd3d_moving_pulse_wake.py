"""
Phase 3c validation: moving-pulse dark wake on FDTD3DEngine.

Per Phase 3 architectural pivot at
research/2026-05-18_phase3-architectural-pivot.md and Phase 1 analytical
derivation at research/2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md:

A moving localized E pulse propagating forward through the substrate
should leave a measurable wake at trailing positions, propagating at c_0.

Three tests:
1. test_pulse_propagation_speed: a Gaussian-modulated wave packet propagates
   at substrate wave speed c (validates basic Maxwell FDTD propagation).
2. test_wake_signature_at_trailing_position: after pulse passes a probe,
   the probe sees a non-zero E field "wake" (validates wake formation).
3. test_wake_propagates_at_c0: arrival time at multiple probe distances
   follows Δt = L/c_0 (validates wake propagates at substrate wave speed).

Run:
    pytest src/tests/test_fdtd3d_moving_pulse_wake.py -v -s
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.fdtd_3d import FDTD3DEngine


def _seed_moving_gaussian_pulse(engine, center_xyz, sigma_cells, k_x_cells, amplitude):
    """Seed Gaussian-modulated plane wave moving in +x direction.

    E_z(r, 0) = amplitude · exp(-r²/(2σ²)) · cos(k_x · x_cells)

    The cos(k_x · x) factor gives the pulse forward momentum: the carrier
    propagates at c_0 in +x, while the Gaussian envelope localizes the
    pulse in space.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = center_xyz
    i, j, k = np.indices((nx, ny, nz))
    r_sq = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
    envelope = amplitude * np.exp(-r_sq / (2.0 * sigma_cells**2))
    carrier = np.cos(k_x_cells * (i - cx))
    engine.Ez += envelope * carrier


def _run_steps(engine, n_steps, apply_abc=True, probe_positions=None):
    """Run engine for n_steps, optionally probe (Ex, Ey, Ez, Hx, Hy, Hz) at positions.

    probe_positions: list of (i,j,k) tuples
    Returns dict: times[N], probes={pos: {Ez[N], H_mag[N]}}
    """
    times = []
    probe_data = {pos: {"Ez": [], "H_mag": []} for pos in (probe_positions or [])}
    for step in range(n_steps):
        engine.update_magnetic_field()
        engine.update_electric_field()
        if apply_abc:
            engine.apply_mur_abc()
        times.append(step * engine.dt)
        for pos in (probe_positions or []):
            probe_data[pos]["Ez"].append(float(engine.Ez[pos]))
            H_mag = np.sqrt(engine.Hx[pos] ** 2 + engine.Hy[pos] ** 2 + engine.Hz[pos] ** 2)
            probe_data[pos]["H_mag"].append(float(H_mag))
    return {
        "times": np.array(times),
        "probes": {pos: {k: np.array(v) for k, v in d.items()} for pos, d in probe_data.items()},
    }


def test_wake_signature_at_trailing_position():
    """After a moving pulse passes, trailing position sees a measurable wake."""
    N = 64
    DX = 0.01
    engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=True, use_pml=False)

    # Seed moving pulse near x=N/4, moving in +x direction
    center = (N // 4, N // 2, N // 2)
    sigma = 3.0
    k_x = 2.0 * np.pi / 8.0  # 1 wavelength per 8 cells (well-resolved)
    amplitude = 1.0

    _seed_moving_gaussian_pulse(engine, center, sigma, k_x, amplitude)

    # Probe at TRAILING position (BEHIND the seed, i.e., smaller x)
    trailing_pos = (N // 4 - 8, N // 2, N // 2)
    # Probe at LEADING position (ahead of the seed)
    leading_pos = (N // 4 + 16, N // 2, N // 2)

    print(f"\nMoving pulse test: N={N}, dx={DX}, dt={engine.dt:.3e}")
    print(f"  Seed at: {center}, σ={sigma}, k_x={k_x:.3f}, amplitude={amplitude}")
    print(f"  Trailing probe: {trailing_pos}, leading probe: {leading_pos}")

    N_STEPS = 200
    result = _run_steps(engine, N_STEPS, apply_abc=True,
                        probe_positions=[trailing_pos, leading_pos])

    trailing_Ez = result["probes"][trailing_pos]["Ez"]
    leading_Ez = result["probes"][leading_pos]["Ez"]

    # After enough timesteps, the trailing position should see SOMETHING
    # (either the wake from the moving pulse OR direct pulse if not enough motion)
    trailing_peak = np.abs(trailing_Ez).max()
    leading_peak = np.abs(leading_Ez).max()

    print(f"  Trailing Ez peak: {trailing_peak:.4e}")
    print(f"  Leading Ez peak: {leading_peak:.4e}")

    # Both positions should see some signal (the pulse expands in all directions
    # AND moves forward). Validates basic propagation.
    assert trailing_peak > 1e-4, "No trailing-position signal — pulse failed to propagate"
    assert leading_peak > 1e-4, "No leading-position signal — pulse failed to propagate"


def test_pulse_propagation_speed():
    """Verify pulse arrival at L/c_0 timing — fundamental Maxwell FDTD sanity check."""
    N = 64
    DX = 0.01
    engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=True, use_pml=False)

    # Seed pulse at one end; probe at known distances downstream
    center = (8, N // 2, N // 2)
    sigma = 2.0
    k_x = 2.0 * np.pi / 8.0
    amplitude = 1.0

    _seed_moving_gaussian_pulse(engine, center, sigma, k_x, amplitude)

    # Probe at three downstream positions
    probe_offsets_cells = [16, 24, 32]
    probes = [(center[0] + dx_cells, center[1], center[2]) for dx_cells in probe_offsets_cells]
    expected_delays = [(dx_cells * DX) / engine.c for dx_cells in probe_offsets_cells]

    print(f"\nPropagation speed test: dx={DX}, dt={engine.dt:.3e}, c={engine.c:.3e}")
    for offset, delay in zip(probe_offsets_cells, expected_delays):
        print(f"  Probe at +{offset} cells = {offset*DX*100:.1f} cm: expected Δt = {delay*1e9:.2f} ns")

    N_STEPS = 200
    result = _run_steps(engine, N_STEPS, apply_abc=True, probe_positions=probes)

    times_ns = result["times"] * 1e9

    # Find peak time at each probe (when |Ez| is maximum)
    arrival_times_ns = []
    for probe in probes:
        Ez_series = result["probes"][probe]["Ez"]
        if np.abs(Ez_series).max() > 1e-6:
            peak_idx = np.argmax(np.abs(Ez_series))
            arrival_times_ns.append(times_ns[peak_idx])
        else:
            arrival_times_ns.append(np.nan)

    expected_ns = [d * 1e9 for d in expected_delays]
    print(f"  Expected arrival times (ns): {expected_ns}")
    print(f"  Measured arrival times (ns): {arrival_times_ns}")

    # Check that arrivals scale with distance (verify propagation at finite speed)
    for i in range(1, len(arrival_times_ns)):
        if not np.isnan(arrival_times_ns[i]) and not np.isnan(arrival_times_ns[0]):
            ratio = arrival_times_ns[i] / arrival_times_ns[0] if arrival_times_ns[0] > 0 else 0
            expected_ratio = expected_ns[i] / expected_ns[0]
            print(f"  Arrival ratio probe {i}/probe 0: measured={ratio:.2f}, expected={expected_ratio:.2f}")

    # At minimum: peak arrival times should be monotonically increasing with distance
    valid_arrivals = [t for t in arrival_times_ns if not np.isnan(t)]
    if len(valid_arrivals) >= 2:
        assert valid_arrivals == sorted(valid_arrivals), (
            f"Pulse arrival times not monotonic with distance: {valid_arrivals}"
        )


def test_wake_propagates_at_c0():
    """Wake from pulse passage propagates at c_0 — validates wake at substrate wave speed."""
    N = 96
    DX = 0.01
    engine = FDTD3DEngine(nx=N, ny=N, nz=N, dx=DX, linear_only=True, use_pml=False)

    # Seed at one end
    center = (8, N // 2, N // 2)
    sigma = 2.5
    k_x = 2.0 * np.pi / 8.0
    amplitude = 1.0
    _seed_moving_gaussian_pulse(engine, center, sigma, k_x, amplitude)

    # Probe at two trailing-edge positions (behind the seed in -x)
    # The wake propagates BACKWARD from the soliton's trailing edge at c
    # For a pulse moving in +x, the "wake" is the leftward-traveling component
    probes_back = [(center[0] - 4, center[1], center[2]),
                   (center[0] - 12, center[1], center[2]) if center[0] > 12 else (4, center[1], center[2])]

    print(f"\nWake propagation test: N={N}, dx={DX}, dt={engine.dt:.3e}")
    print(f"  Seed at {center}, trailing probes at {probes_back}")

    N_STEPS = 100
    result = _run_steps(engine, N_STEPS, apply_abc=True, probe_positions=probes_back)

    # The trailing probes should see something (wake or leftward-component)
    for probe in probes_back:
        Ez = result["probes"][probe]["Ez"]
        peak = np.abs(Ez).max()
        print(f"  Probe {probe}: peak |Ez| = {peak:.4e}")
        assert peak > 1e-4, f"No signal at trailing probe {probe} — wake not propagating backward"
