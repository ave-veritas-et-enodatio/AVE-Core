"""
Theorem 3.1 decisive numerical test.

Compute the Neumann integral for the (2,3) torus knot at Golden
Torus geometry and compare to Ch 8's Lambda decomposition:
    Lambda_vol  = 4*pi^3 ~ 124.025   (self-L volumetric)
    Lambda_surf = pi^2  ~  9.870     (mutual-M at 3 crossings)
    Lambda_line = pi    ~  3.142     (line/Nyquist)
    alpha^-1    = 137.036

Pre-registered hypothesis: the MUTUAL part of the Neumann integral,
summed over the 3 crossings of the (2,3) winding, equals Lambda_surf
= pi^2.

At Golden Torus: R = phi/2 ~= 0.809, r = (phi-1)/2 ~= 0.309, d = 1
(Nyquist tube thickness). Natural units (mu_0 = 1, ell_node = 1, Z_0 = 1).

Computation:
1. Parametrize (p, q) = (2, 3) knot with N sample points.
2. Compute full Neumann double-integral with tube-thickness
   regularization |r - r'| -> max(|r - r'|, d).
3. Identify crossings: pairs (t_i, t_j) with large |t_i - t_j| (not
   adjacent along path) but small |r_i - r_j|.
4. Split contributions: local self-L (|t_i - t_j| small) vs
   crossing mutual-L vs bulk integral.
5. Compare crossing contribution to pi^2.
"""

import numpy as np

# Constants (natural units: mu_0 = 1, ell_node = 1)
PHI = (1 + np.sqrt(5)) / 2.0
R_GT = PHI / 2.0            # Golden Torus major radius
r_GT = (PHI - 1) / 2.0      # Golden Torus minor radius
d_tube = 1.0                # Nyquist tube thickness (one lattice pitch)


def knot_path(t, p=2, q=3, R=R_GT, r=r_GT):
    """(p,q) torus knot position at parameter t in [0, 2*pi)."""
    x = (R + r * np.cos(q * t)) * np.cos(p * t)
    y = (R + r * np.cos(q * t)) * np.sin(p * t)
    z = r * np.sin(q * t)
    return np.stack([x, y, z], axis=-1)


def knot_tangent(t, p=2, q=3, R=R_GT, r=r_GT):
    """(p,q) torus knot tangent (dr/dt) at parameter t."""
    cos_pt = np.cos(p * t)
    sin_pt = np.sin(p * t)
    cos_qt = np.cos(q * t)
    sin_qt = np.sin(q * t)

    dx_dt = -r * q * sin_qt * cos_pt - (R + r * cos_qt) * p * sin_pt
    dy_dt = -r * q * sin_qt * sin_pt + (R + r * cos_qt) * p * cos_pt
    dz_dt = r * q * cos_qt
    return np.stack([dx_dt, dy_dt, dz_dt], axis=-1)


def full_neumann_integral(N=4000, p=2, q=3, R=R_GT, r=r_GT, d=d_tube):
    """Compute full Neumann double-integral for (p,q) knot at (R, r).

    M = (1 / 4 pi) * integral ds integral ds' (dl . dl') / max(|r - r'|, d)

    Returns total Neumann integral in natural units (mu_0 = 1, ell_node = 1).
    """
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)
    dt = 2 * np.pi / N

    positions = knot_path(t, p, q, R, r)  # shape (N, 3)
    tangents = knot_tangent(t, p, q, R, r)  # shape (N, 3)

    # Pairwise displacements and distances
    r_ij = positions[:, None, :] - positions[None, :, :]  # (N, N, 3)
    dist = np.linalg.norm(r_ij, axis=-1)                   # (N, N)
    dist_reg = np.maximum(dist, d)                         # regularize

    # Pairwise tangent dot products
    dot_ij = np.einsum('ik,jk->ij', tangents, tangents)    # (N, N)

    # Neumann integrand
    integrand = dot_ij / dist_reg                          # (N, N)

    # Exclude diagonal (self-term is handled by regularization)
    np.fill_diagonal(integrand, 0.0)

    # Integrate
    M_total = integrand.sum() * (dt ** 2) / (4 * np.pi)

    return M_total, positions, tangents, dist


def decompose_by_path_separation(N=4000, t_crossing_threshold=0.5):
    """Split Neumann integral by path-distance separation |t_i - t_j|.

    Near part: |t_i - t_j| < threshold  (local self-L along wire)
    Far part:  |t_i - t_j| > threshold  (mutual-L including crossings)
    """
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)
    dt = 2 * np.pi / N

    positions = knot_path(t)
    tangents = knot_tangent(t)

    # t-separation (minimum over periodic wrap)
    t_diff = np.abs(t[:, None] - t[None, :])
    t_diff = np.minimum(t_diff, 2 * np.pi - t_diff)  # periodic distance

    r_ij = positions[:, None, :] - positions[None, :, :]
    dist = np.linalg.norm(r_ij, axis=-1)
    dist_reg = np.maximum(dist, d_tube)
    dot_ij = np.einsum('ik,jk->ij', tangents, tangents)
    integrand = dot_ij / dist_reg
    np.fill_diagonal(integrand, 0.0)

    near_mask = t_diff < t_crossing_threshold
    far_mask = ~near_mask

    near_contribution = integrand[near_mask].sum() * (dt ** 2) / (4 * np.pi)
    far_contribution = integrand[far_mask].sum() * (dt ** 2) / (4 * np.pi)

    return near_contribution, far_contribution, t, positions, dist


def find_crossings(t, positions, dist, N_expected=3):
    """Identify the 3 crossings of the (2,3) torus knot.

    A crossing is a pair (i, j) with large t-separation but small
    spatial distance. We find them as local minima of dist in the
    far-separation region.
    """
    N = len(t)
    t_diff = np.abs(t[:, None] - t[None, :])
    t_diff = np.minimum(t_diff, 2 * np.pi - t_diff)

    # Mask: only far pairs
    far_mask = t_diff > 0.5
    far_dist = np.where(far_mask, dist, np.inf)

    # Find local minima: for each i, find j* = argmin far_dist[i, j]
    j_stars = np.argmin(far_dist, axis=1)
    # Unique crossings (i < j*)
    crossings = set()
    for i in range(N):
        j = j_stars[i]
        if i < j and far_dist[i, j] < 2 * d_tube:
            crossings.add((i, j))

    return sorted(crossings)


def main():
    print("="*70)
    print("Theorem 3.1 Neumann-integral validation")
    print(f"(p, q) = (2, 3) torus knot at Golden Torus")
    print(f"R = phi/2 = {R_GT:.6f}, r = (phi-1)/2 = {r_GT:.6f}, d = {d_tube}")
    print(f"R*r = {R_GT * r_GT:.6f} (expected 1/4 = 0.25)")
    print(f"R-r = {R_GT - r_GT:.6f} (expected 1/2 = 0.5)")
    print("="*70)

    # Ch 8 predictions
    lambda_vol_ch8 = 4 * np.pi ** 3
    lambda_surf_ch8 = np.pi ** 2
    lambda_line_ch8 = np.pi
    alpha_inv_ch8 = lambda_vol_ch8 + lambda_surf_ch8 + lambda_line_ch8
    print(f"\nCh 8 predictions:")
    print(f"  Lambda_vol  = 4*pi^3 = {lambda_vol_ch8:.4f}")
    print(f"  Lambda_surf = pi^2   = {lambda_surf_ch8:.4f}")
    print(f"  Lambda_line = pi     = {lambda_line_ch8:.4f}")
    print(f"  alpha^-1    = {alpha_inv_ch8:.4f}")

    # Full Neumann integral
    N_sample = 4000
    print(f"\nComputing with N = {N_sample} samples along knot...")
    M_total, positions, tangents, dist = full_neumann_integral(N=N_sample)
    print(f"Full Neumann integral M_total = {M_total:.4f}")
    print(f"  (continuum, classical Neumann, regularized at |r|=d=1)")

    # Near/far decomposition
    near, far, t, _, _ = decompose_by_path_separation(N=N_sample,
                                                      t_crossing_threshold=0.5)
    print(f"\nNear-path (|t_i - t_j| < 0.5): M_near = {near:.4f}")
    print(f"Far-path  (|t_i - t_j| > 0.5): M_far  = {far:.4f}")
    print(f"Sum check: {near + far:.4f} vs {M_total:.4f}")

    # Crossings
    crossings = find_crossings(t, positions, dist)
    print(f"\nFound {len(crossings)} crossings:")
    for i, j in crossings:
        print(f"  Crossing at t=({t[i]:.3f}, {t[j]:.3f})  r=({positions[i,0]:.3f}, {positions[i,1]:.3f}, {positions[i,2]:.3f})  dist={dist[i,j]:.3f}")

    # Try different thresholds for near/far split
    print(f"\nSensitivity to split threshold:")
    for thresh in [0.2, 0.5, 1.0, 1.5, 2.0, 3.0]:
        near_t, far_t, _, _, _ = decompose_by_path_separation(
            N=N_sample, t_crossing_threshold=thresh
        )
        print(f"  thresh = {thresh:.1f}: near = {near_t:.4f}, far = {far_t:.4f}, "
              f"ratio far / pi^2 = {far_t / np.pi**2:.4f}")

    print("\n" + "="*70)
    print("PRE-REGISTERED COMPARISON")
    print("="*70)
    print(f"Target: Lambda_surf = pi^2 = {lambda_surf_ch8:.4f}")
    print(f"Candidate: far-path Neumann contribution (thresh=1.0) "
          f"approx = {decompose_by_path_separation(N_sample, 1.0)[1]:.4f}")


if __name__ == "__main__":
    main()
