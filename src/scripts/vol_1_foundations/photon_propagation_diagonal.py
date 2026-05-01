"""Photon propagation along K4 diagonal port direction (verify v=c).

Per `photon_propagation.py` docstring lines 35-42: "junction-diagonal
propagation (along a single port direction p̂_n) is at speed c; cardinal-
axis propagation (along x̂, ŷ, or ẑ) is at speed c·√2 because the 4-port
pattern forces each lattice step to advance by one full cardinal cell."

Validation: launch the same Gaussian packet but with direction = port-0
unit vector (+1, +1, +1)/√3 instead of cardinal +x̂. Pre-registered
prediction: v_meas/c ≈ 1.0 along the diagonal.

This complements `photon_propagation.py` (cardinal +x̂, v=√2·c) to
characterize the K4 substrate's anisotropic kinematics fully.
"""
from __future__ import annotations

import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from photon_propagation import run_validation


if __name__ == "__main__":
    print("─" * 72)
    print("  Photon along K4 diagonal port (1,1,1)/√3 — pre-reg v/c ≈ 1.0")
    print("─" * 72)

    # Default photon_propagation.run_validation hardcodes direction=(1,0,0).
    # We need to repeat the run with direction set to port-0 unit vector.
    # Easier to call run_validation as a baseline + manually set up the
    # diagonal run via inlined code.

    import numpy as np
    from ave.core.k4_tlm import K4Lattice3D
    from ave.core.constants import C_0, V_SNAP
    from photon_propagation import PlaneSource, xy_slice, packet_centroid_interior

    N = 96
    pml = 8
    source_x = 16
    lambda_cells = 10.0
    sigma_yz = 8.0
    t_sigma_periods = 0.75
    amp_frac = 0.01
    n_steps = 240
    steps_per_frame = 3

    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    dt = lattice.dt
    c = float(C_0)
    omega = 2.0 * np.pi * c / (lambda_cells * 1.0)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma
    amp_volts = amp_frac * float(V_SNAP)

    # Diagonal direction = port-0 unit vector
    inv_sqrt3 = 1.0 / np.sqrt(3.0)
    diag_dir = (inv_sqrt3, inv_sqrt3, inv_sqrt3)

    src = PlaneSource(
        x0=source_x, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=diag_dir, sigma_yz=sigma_yz,
        omega=omega, t_center=t_center, t_sigma=t_sigma,
        amplitude=amp_volts,
    )

    print(f"  Source direction = (1,1,1)/√3 ≈ ({inv_sqrt3:.3f}, {inv_sqrt3:.3f}, {inv_sqrt3:.3f})")
    print(f"  port_w (T₂-projected) = {src.port_w}")

    # Sample energy density at diagonal-displaced planes:
    # Distance d along (1,1,1)/√3 means (x, y, z) = (x0+d/√3, y0+d/√3, z0+d/√3)
    # We'll sample the diagonal-displaced PEAK location at frame intervals.
    sample_distances = [20, 40, 60]  # in "diagonal cells"

    def diagonal_sample_voxels(d_diag: float):
        """Get integer voxel coords for points d_diag along (1,1,1)/√3 from source center."""
        x0 = source_x
        y0 = (N - 1) // 2
        z0 = (N - 1) // 2
        # Step inv_sqrt3 in each axis per d_diag step
        dx_axis = d_diag * inv_sqrt3
        return int(round(x0 + dx_axis)), int(round(y0 + dx_axis)), int(round(z0 + dx_axis))

    voxels = [diagonal_sample_voxels(d) for d in sample_distances]
    print(f"  Sample voxels along diagonal at distances {sample_distances}: {voxels}")

    # Per-frame energy at each sample voxel + neighbors (1-cell radius)
    # to capture peak arrival robustly
    history_per_voxel = [[] for _ in sample_distances]
    times = []

    for step in range(1, n_steps + 1):
        t_pre = step * dt
        src.apply(lattice, t_pre)
        lattice.step()
        if step % steps_per_frame == 0:
            rho = lattice.get_energy_density()
            for vi, (x, y, z) in enumerate(voxels):
                # Sample 3x3x3 around the voxel
                xs, xe = max(0, x - 1), min(N, x + 2)
                ys, ye = max(0, y - 1), min(N, y + 2)
                zs, ze = max(0, z - 1), min(N, z + 2)
                history_per_voxel[vi].append(rho[xs:xe, ys:ye, zs:ze].sum())
            times.append(lattice.timestep * dt)

    times_arr = np.array(times)

    # Peak arrival at each sample voxel
    print(f"\n  Diagonal arrival times (peak energy density):")
    print(f"  {'distance':>10} {'voxel':>15} {'t_peak (s)':>14} {'t_peak (steps)':>16}")
    arrival_times = []
    for vi, d in enumerate(sample_distances):
        series = np.array(history_per_voxel[vi])
        if series.max() > 0:
            idx = int(np.argmax(series))
            t_peak = times_arr[idx]
            arrival_times.append(t_peak)
            print(f"  {d:>10}  {str(voxels[vi]):>15}  {t_peak:>13.3e}  {idx*steps_per_frame:>14d}")
        else:
            arrival_times.append(None)
            print(f"  {d:>10}  {str(voxels[vi]):>15}  no peak detected")

    # Velocity from arrival-time fit (using the two innermost stable points)
    valid = [(d, t) for d, t in zip(sample_distances, arrival_times) if t is not None]
    if len(valid) >= 2:
        d_a, t_a = valid[0]
        d_b, t_b = valid[-1]
        # Physical distance along diagonal = d_diag * dx (dx=1.0; d_diag in cells along axis,
        # so physical 3D distance = d_diag · √3 · dx since each axis advances d_diag/√3)
        # Wait: if voxel is at (x0+d/√3, y0+d/√3, z0+d/√3) and we step in 'd' units of "diagonal-projection",
        # then |voxel - source| = d (3D distance) — that's what 'd_diag' means here.
        # Actually re-reading: I parameterized d_diag as "step size in axis-component", with
        # voxel at (x0+d_diag·1/√3, ...). So physical distance = d_diag.
        # NO — I want d_diag = physical distance along the (1,1,1)/√3 direction.
        # Given voxel at (x0 + d_diag/√3, y0 + d_diag/√3, z0 + d_diag/√3):
        # |voxel - source| = √(3·(d_diag/√3)²) = √(d_diag²) = d_diag. Yes, d_diag IS physical distance.

        v_meas = (d_b - d_a) * 1.0 / (t_b - t_a)  # dx=1.0
        c_ratio = v_meas / c
        print(f"\n  Velocity along diagonal: v = {v_meas:.3e} m/s")
        print(f"  v/c = {c_ratio:.3f}")
        print(f"  Pre-registered: v/c ≈ 1.0 (junction-diagonal photon)")
        print(f"  Verdict: {'PASS (≈ 1.0 within K4 anisotropy)' if 0.9 < c_ratio < 1.1 else 'FAIL — needs analysis'}")
    else:
        print("\n  Insufficient peak detections to compute velocity.")
