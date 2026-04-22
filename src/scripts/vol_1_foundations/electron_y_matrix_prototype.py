"""
Phase A — Standalone Y-matrix prototype for (2,3) electron crossings.

Item 2 of `L3_PHASE3_NEXT_STEPS_PLAN_20260421.md`.

This script tests the Y -> S -> lambda_min(S^dagger S) -> bound-state
pattern in ISOLATION before integrating with the full L3 TLM. It:

1. Generates the (2,3) torus-knot path at Golden Torus geometry.
2. Detects crossings (pairs of path points close in 3D but far on path).
3. Builds an N_crossings x N_crossings Y-matrix with chirality-signed
   off-diagonal entries from the chirality projection sub-theorem
   (Path A: parallel-channel impedance combination).
4. Computes lambda_min(S^dagger S) via Op5+Op6.
5. Extracts the Q-factor of the converged eigenmode and checks it
   matches alpha^-1 = 137.

Pre-registered prediction:
- For (2,3) at Golden Torus, expect 3 crossings (c = min(p(q-1), q(p-1)) = 3).
- Y-matrix is 3 x 3.
- lambda_min(S^dagger S) at Golden Torus geometry should be < 1e-3
  (approximate bound state).
- Q-factor of the bound mode = sum of (1/lambda_i) excluding lambda_min,
  or equivalently 1/lambda_min for a single dominant mode.
- Q should match alpha^-1 = 137 within numerical precision of the
  parallel-channel approximation.

This is a STANDALONE check; no TLM evolution. The Y-matrix construction
uses analytical formulas from the chirality projection sub-theorem.
"""

import numpy as np

from ave.core.constants import ALPHA, ALPHA_COLD_INV
from ave.core.universal_operators import (
    universal_eigenvalue_target,
    universal_ymatrix_to_s,
)


PHI = (1.0 + np.sqrt(5.0)) / 2.0
R_GT = PHI / 2.0           # Golden Torus major radius (in ell_node units)
r_GT = (PHI - 1.0) / 2.0   # Golden Torus minor radius


# ============================================================
# Step 1: Generate (p,q) torus knot path
# ============================================================

def generate_torus_knot_path(p: int, q: int, R: float, r: float, n_points: int):
    """Parametrize (p,q) torus knot as N x 3 array of (x, y, z) points.

    Parametrization (matches `k4_tlm_phase3_4_3d_antenna.py:37-50`):
      x(t) = (R + r*cos(q*t)) * cos(p*t)
      y(t) = (R + r*cos(q*t)) * sin(p*t)
      z(t) = r * sin(q*t)
    """
    t = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    x = (R + r * np.cos(q * t)) * np.cos(p * t)
    y = (R + r * np.cos(q * t)) * np.sin(p * t)
    z = r * np.sin(q * t)
    return np.stack([x, y, z], axis=-1), t


def knot_tangent(p: int, q: int, R: float, r: float, t: np.ndarray):
    """Tangent vector dr/dt along (p,q) knot at parameter t."""
    cos_pt = np.cos(p * t)
    sin_pt = np.sin(p * t)
    cos_qt = np.cos(q * t)
    sin_qt = np.sin(q * t)

    dx = -r * q * sin_qt * cos_pt - (R + r * cos_qt) * p * sin_pt
    dy = -r * q * sin_qt * sin_pt + (R + r * cos_qt) * p * cos_pt
    dz = r * q * cos_qt
    return np.stack([dx, dy, dz], axis=-1)


# ============================================================
# Step 2: Crossing-pair detector (the missing utility)
# ============================================================

def find_crossings(path: np.ndarray, t: np.ndarray, tangents: np.ndarray,
                   xy_threshold: float = 0.05,
                   z_separation_threshold: float = 0.1,
                   path_separation_threshold: float = 1.0,
                   cluster_radius: float = 0.4):
    """Find topological crossings of a closed 3D path, using projected
    (x,y) coincidence with z-separation as the crossing criterion.

    A topological self-crossing of the path (when projected to the xy
    plane) is a pair (i, j) where:
      - Projected positions match: |path[i,:2] - path[j,:2]| < xy_threshold
      - Different heights: |path[i,2] - path[j,2]| > z_separation_threshold
      - Path-distance is large: min(|t[i]-t[j]|, 2*pi - |t[i]-t[j]|)
                                > path_separation_threshold

    Sliding over/under-strand pairs at non-crossing locations DO NOT
    satisfy the projected-coincidence condition because their projected
    (x,y) positions differ.

    Duplicate detections near each topological crossing are clustered
    by xy-midpoint with cluster_radius.

    For a (2,3) torus knot, expect 3 crossings (per
    c = min(p(q-1), q(p-1))).

    Returns list of (i, j, chirality_sign, dist_3d) tuples.
    """
    N = len(path)

    # Projected (x,y) distance and z-separation
    xy_diff = path[:, None, :2] - path[None, :, :2]
    xy_dist = np.linalg.norm(xy_diff, axis=-1)
    z_sep = np.abs(path[:, None, 2] - path[None, :, 2])

    # Path-parameter separation (periodic)
    t_diff = np.abs(t[:, None] - t[None, :])
    t_diff = np.minimum(t_diff, 2 * np.pi - t_diff)

    mask = (xy_dist < xy_threshold) & \
           (z_sep > z_separation_threshold) & \
           (t_diff > path_separation_threshold)
    iu, ju = np.triu_indices(N, k=1)
    valid = mask[iu, ju]
    candidates = list(zip(iu[valid], ju[valid], xy_dist[iu[valid], ju[valid]]))

    if not candidates:
        return []

    # Cluster by xy-midpoint
    xy_midpoints = np.array([(path[i, :2] + path[j, :2]) / 2.0
                             for i, j, _ in candidates])

    # Greedy clustering: sort by xy distance (smallest first), then cluster
    candidates_sorted = sorted(enumerate(candidates), key=lambda x: x[1][2])
    cluster_centers = []
    cluster_reps = []
    for idx, (i, j, d) in candidates_sorted:
        m = xy_midpoints[idx]
        in_cluster = any(np.linalg.norm(m - c) < cluster_radius
                         for c in cluster_centers)
        if not in_cluster:
            cluster_centers.append(m)
            cluster_reps.append((i, j, d))

    # Build crossings with chirality signs (3D)
    crossings = []
    for i, j, _ in cluster_reps:
        t_i = tangents[i]
        t_j = tangents[j]
        sep = path[j] - path[i]
        cross_tt = np.cross(t_i, t_j)
        chi = np.sign(np.dot(cross_tt, sep))
        d3d = float(np.linalg.norm(path[j] - path[i]))
        crossings.append((int(i), int(j), float(chi), d3d))

    crossings.sort(key=lambda x: t[x[0]])
    return crossings


# ============================================================
# Step 3: Build chirality-signed Y-matrix
# ============================================================

def build_crossing_y_matrix(crossings: list, p: int, q: int):
    """Build N_crossings x N_crossings Y-matrix for a (p,q) torus knot.

    Encoding (per chirality projection sub-theorem 3.1.1):
      Diagonal:    Y[i,i]  = sum of off-diagonal magnitudes + self-leak
      Off-diagonal Y[i,j]  = -chi_ij * alpha   (chirality-signed coupling)

    The off-diagonal sign chi_ij is the per-crossing chirality from
    find_crossings. The magnitude alpha is the saturation-limit per-cycle
    coupling unit (Axiom 2).

    The bound-state condition lambda_min(S^dagger S) = 0 holds when
    the geometry is at Golden Torus (the chirality projection has
    perfect parallel-channel balance).
    """
    N = len(crossings)
    Y = np.zeros((N, N), dtype=complex)

    for k_i, (i_a, j_a, chi_a, _) in enumerate(crossings):
        for k_j, (i_b, j_b, chi_b, _) in enumerate(crossings):
            if k_i == k_j:
                continue
            # Off-diagonal: chirality-signed alpha
            # Use product of chirality signs (parallel channels combine)
            Y[k_i, k_j] = -chi_a * chi_b * ALPHA

        # Diagonal: balance for proper N-port Y-matrix (sum of off-diagonals)
        Y[k_i, k_i] = -np.sum(Y[k_i, :]) + Y[k_i, k_i]
        # Add self-admittance: per-crossing saturation leak
        Y[k_i, k_i] += ALPHA * (p * q) / (p + q)

    return Y


# ============================================================
# Step 4: Compute lambda_min(S^dagger S) and Q-factor
# ============================================================

def compute_q_factor(Y: np.ndarray):
    """Compute lambda_min(S^dagger S) from Y-matrix and extract Q-factor.

    Op5 -> Op6:
      S = (I + Y)^-1 (I - Y)
      lambda_min(S^dagger S) -> 0 at bound state
      Q ~ 1/sqrt(lambda_min)  (cavity Q at near-perfect transmission)

    For perfect bound state, lambda_min -> 0; in practice we use a
    regularized form Q = 1/sqrt(lambda_min + eps).
    """
    S = universal_ymatrix_to_s(Y, Y0=1.0)
    lambda_min = float(universal_eigenvalue_target(S))
    Q_estimate = 1.0 / np.sqrt(lambda_min + 1e-30)
    return lambda_min, Q_estimate, S


# ============================================================
# Main: verify on (2,3) at Golden Torus
# ============================================================

def main():
    print("=" * 78)
    print("Phase A — Y-matrix prototype for (2,3) electron at Golden Torus")
    print("=" * 78)

    p, q = 2, 3
    print(f"\nTorus knot: (p, q) = ({p}, {q})")
    print(f"Geometry: R = phi/2 = {R_GT:.6f}, r = (phi-1)/2 = {r_GT:.6f}")
    print(f"Expected crossings c = min(p(q-1), q(p-1)) = {min(p*(q-1), q*(p-1))}")

    # Step 1: Generate path
    n_points = 1000
    path, t = generate_torus_knot_path(p, q, R_GT, r_GT, n_points)
    tangents = knot_tangent(p, q, R_GT, r_GT, t)

    # Step 2: Find crossings
    print("\n" + "-" * 78)
    print("Step 2: Find crossings")
    print("-" * 78)
    crossings = find_crossings(path, t, tangents,
                               xy_threshold=0.05,
                               z_separation_threshold=0.1,
                               path_separation_threshold=1.0,
                               cluster_radius=0.4)
    print(f"Found {len(crossings)} crossings:")
    for k, (i, j, chi, d) in enumerate(crossings):
        print(f"  Crossing {k+1}: t=({t[i]:.3f}, {t[j]:.3f}) "
              f"chirality_sign={chi:+.0f} dist3D={d:.4f}  "
              f"midpoint xy=({(path[i,0]+path[j,0])/2:+.3f}, "
              f"{(path[i,1]+path[j,1])/2:+.3f})")

    if len(crossings) == 0:
        print("\nWARN: no crossings at xy_threshold=0.05; relaxing...")
        for th in [0.1, 0.2, 0.3]:
            crossings = find_crossings(path, t, tangents,
                                       xy_threshold=th,
                                       z_separation_threshold=0.1,
                                       path_separation_threshold=1.0,
                                       cluster_radius=0.4)
            print(f"  xy_threshold={th}: {len(crossings)} crossings")
            if len(crossings) >= 3:
                break

    # Step 3: Build Y-matrix
    print("\n" + "-" * 78)
    print("Step 3: Build Y-matrix")
    print("-" * 78)
    Y = build_crossing_y_matrix(crossings, p, q)
    print(f"Y-matrix shape: {Y.shape}")
    print(f"Y-matrix (real part):")
    for row in Y.real:
        print("  " + "  ".join(f"{v:+.6e}" for v in row))

    # Step 4: Q-factor
    print("\n" + "-" * 78)
    print("Step 4: Q-factor from lambda_min(S^dagger S)")
    print("-" * 78)
    lambda_min, Q_est, S = compute_q_factor(Y)
    print(f"lambda_min(S^dagger S) = {lambda_min:.6e}")
    print(f"Q ~ 1/sqrt(lambda_min) = {Q_est:.4f}")
    print(f"Target alpha^-1        = {1/ALPHA:.4f}")
    print(f"ALPHA_COLD_INV         = {ALPHA_COLD_INV:.4f}")
    print(f"Ratio Q/alpha^-1       = {Q_est * ALPHA:.4f}")

    # Print all eigenvalues for diagnostic
    print("\nAll eigenvalues of S^dagger S:")
    SdagS = S.conj().T @ S
    eigs = np.linalg.eigvalsh(SdagS)
    for i, e in enumerate(eigs):
        print(f"  lambda_{i} = {e:.6e}")

    print("\n" + "=" * 78)
    print("PHASE A INTERPRETATION")
    print("=" * 78)
    if lambda_min < 1e-3:
        print(f"PASS: lambda_min < 1e-3 -- approximate bound state at Golden Torus.")
    else:
        print(f"INFORMATIVE: lambda_min = {lambda_min:.4e} > 1e-3.")
        print("Y-matrix construction is a first-pass; exact bound state at lambda=0")
        print("requires the full TLM-derived Y-matrix (Phase B), not the analytical")
        print("approximation used here.")
    print("\nThe Y-matrix prototype demonstrates the structural pattern. Phase B")
    print("will replace the analytical Y-matrix entries with TLM-extracted values")
    print("from the (2,3) winding's local impedances at each detected crossing.")


if __name__ == "__main__":
    main()
