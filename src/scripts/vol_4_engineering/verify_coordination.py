"""
W2: Verify z₀ = 51.25 from Lattice Geometry

Generates a Poisson-disk sampled lattice with r_min = ℓ_node,
builds the Delaunay triangulation, and counts the effective
coordination number at different interaction ranges.

The EMT derivation predicts z₀ ≈ 51.25 for the vacuum lattice.
Here we compute the actual mean coordination of the over-braced
Delaunay graph to check physical consistency.
"""

import sys
import os


import numpy as np
from scipy.spatial import Delaunay


def poisson_disk_sample(N_target, box_size, r_min, seed=42):
    """
    Simple dart-throwing Poisson-disk sampling in 3D.
    Places points with minimum separation r_min.
    """
    rng = np.random.default_rng(seed)
    points = []
    max_attempts = N_target * 200

    for _ in range(max_attempts):
        candidate = rng.uniform(0, box_size, 3)
        if len(points) == 0:
            points.append(candidate)
        else:
            pts = np.array(points)
            dists = np.linalg.norm(pts - candidate, axis=1)
            if np.all(dists >= r_min):
                points.append(candidate)
        if len(points) >= N_target:
            break

    return np.array(points)


def count_coordination(pos, r_max, box_size):
    """
    Count mean coordination: number of neighbors within r_max.
    Uses minimum image convention for periodic boundaries.
    """
    N = len(pos)
    z_values = np.zeros(N)

    for i in range(N):
        dr = pos - pos[i]
        dr -= box_size * np.round(dr / box_size)
        dists = np.linalg.norm(dr, axis=1)
        z_values[i] = np.sum((dists > 0) & (dists < r_max))

    return np.mean(z_values), np.std(z_values)


def delaunay_coordination(pos):
    """Mean coordination from Delaunay triangulation."""
    tri = Delaunay(pos)
    neighbors = {i: set() for i in range(len(pos))}
    for simplex in tri.simplices:
        for a in range(4):
            for b in range(a + 1, 4):
                neighbors[simplex[a]].add(simplex[b])
                neighbors[simplex[b]].add(simplex[a])
    z_vals = [len(v) for v in neighbors.values()]
    return np.mean(z_vals), np.std(z_vals)


def run_verification():
    """Verify z₀ from lattice geometry."""
    from ave.core.constants import ALPHA, P_C

    print("=" * 60)
    print("  W2: LATTICE COORDINATION — z₀ VERIFICATION")
    print("=" * 60)

    # Target z₀ from EMT
    z0_emt = 51.25
    p_c = P_C

    # Lattice parameters
    l_node = 1.0  # natural units
    r_min = l_node  # exclusion radius
    overbrace = 1.187  # from manuscript
    box_size = 6.0  # ℓ_node units
    N_target = 300  # nodes in the box

    print(f"\n  Lattice parameters:")
    print(f"    ℓ_node = {l_node}")
    print(f"    r_min = {r_min}")
    print(f"    Overbracing ratio = {overbrace}")
    print(f"    Box = {box_size}³ ℓ_node³")
    print(f"    N_target = {N_target}")

    # Generate Poisson-disk samples
    n_samples = 5
    results_delaunay = []
    results_range = {}

    for R in [1.0, 1.187, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]:
        results_range[R] = []

    for s in range(n_samples):
        pos = poisson_disk_sample(N_target, box_size, r_min, seed=42 + s * 7)
        N = len(pos)

        # Delaunay coordination
        z_mean, z_std = delaunay_coordination(pos)
        results_delaunay.append(z_mean)

        # Range-based coordination
        for R in results_range:
            z_mean_r, _ = count_coordination(pos, R * l_node, box_size)
            results_range[R].append(z_mean_r)

        if s == 0:
            print(f"\n  Sample 0: N = {N} nodes placed")
            print(f"  Packing fraction = {N * (4*np.pi/3*(r_min/2)**3) / box_size**3:.4f}")

    # Results
    z_del = np.mean(results_delaunay)
    print(f"\n  --- Delaunay coordination ---")
    print(f"    z_Delaunay = {z_del:.2f} ± {np.std(results_delaunay):.2f}")
    print()

    print(f"  --- Range-based coordination ---")
    print(f"  {'R/ℓ_node':>10} {'z_eff':>8} {'±σ':>8} {'% of z₀':>10}")
    print(f"  {'-'*40}")

    # Accumulate total: z_eff(R) = sum of neighbors within R
    for R in sorted(results_range.keys()):
        z = np.mean(results_range[R])
        s = np.std(results_range[R])
        pct = z / z0_emt * 100
        marker = "  ← z₀" if abs(z - z0_emt) < 5 else ""
        print(f"  {R:10.3f} {z:8.2f} {s:8.2f} {pct:9.1f}%{marker}")

    print(f"\n  EMT target: z₀ = {z0_emt:.2f}")

    # Find the R that gives z₀ = 51.25
    # By interpolation
    Rs = sorted(results_range.keys())
    zs = [np.mean(results_range[R]) for R in Rs]
    for i in range(len(Rs) - 1):
        if zs[i] <= z0_emt <= zs[i + 1]:
            # Linear interpolation
            frac = (z0_emt - zs[i]) / (zs[i + 1] - zs[i])
            R_interp = Rs[i] + frac * (Rs[i + 1] - Rs[i])
            print(f"  z₀ = 51.25 occurs at R ≈ {R_interp:.3f} ℓ_node")
            print(f"  This is {R_interp:.2f}× the nearest-neighbor distance")
            break


if __name__ == "__main__":
    run_verification()
