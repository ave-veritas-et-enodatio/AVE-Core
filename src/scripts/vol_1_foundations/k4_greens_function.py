"""
K4 (Diamond) Lattice Green's Function — numerical computation via
direct sparse linear algebra.

Closes open item §7.1 of Theorem 3.1 (research/_archive/L3_electron_soliton/
14_theorem_3_1_mutual_inductance_from_axioms.md).

The K4 diamond lattice is bipartite with A (x+y+z even) and B (x+y+z
odd) sublattices at integer Cartesian positions. Each node connects
to 4 tetrahedral neighbors at offsets (±1, ±1, ±1) with even number
of minuses from A to B and odd from B to A. Bond length in Cartesian
units is sqrt(3).

Green's function G_K4(r, r') solves Laplace equation
  Δ_K4 G_K4(r, r') = δ(r, r')
where Δ_K4 is the graph Laplacian on the K4 diamond. The k=0 zero
mode (constant function) is removed by projection.

Direct solve via sparse LU on a finite N^3 cubic sample with zero
Dirichlet boundary conditions (approximates infinite-lattice G_K4
at r << N/2). Compare to continuum 1/(4*pi*r) at large distances to
verify convergence.

Usage:
    python k4_greens_function.py
"""

import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

# Tetrahedral offsets from A->B (source node A: offsets have even
# number of minus signs; B->A has odd). But with the parity-on-sum
# convention the 4 neighbors of any node (A or B) are at:
PORTS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=int)


def build_lattice(N):
    """Enumerate all K4 lattice sites in an N x N x N Cartesian box.

    Both A and B sublattices are included. Node index mapping:
    index[x, y, z] = x * N * N + y * N + z if (x+y+z) valid, else -1.
    (For the diamond, EVERY integer Cartesian site with x+y+z even
    or odd is a lattice site — both sublattices live on the full
    integer lattice, distinguished only by parity.)

    Returns:
        indices: (N, N, N) array of node indices (-1 if not a lattice site — here always valid)
        n_total: total number of lattice sites = N^3
    """
    indices = np.arange(N * N * N).reshape(N, N, N)
    return indices, N * N * N


def build_laplacian(N):
    """Build sparse K4 graph Laplacian on an N^3 periodic cubic box.

    L_ii = coordination (degree) at site i (= 4 for all interior).
    L_ij = -1 if i, j are nearest-neighbor K4 bonds (distance sqrt(3) in Cartesian).

    Boundary: periodic wrap.
    """
    indices, n_total = build_lattice(N)

    L = lil_matrix((n_total, n_total), dtype=float)
    for x in range(N):
        for y in range(N):
            for z in range(N):
                # Bipartite K4: A-sites (x+y+z even) use +PORTS to reach B-NN.
                # B-sites use -PORTS (pointing back to A-NN). This produces
                # a symmetric graph Laplacian with degree 4 for every node.
                parity = (x + y + z) % 2
                sign = +1 if parity == 0 else -1
                i = indices[x, y, z]
                L[i, i] = 4.0
                for p in PORTS:
                    nx = (x + sign * p[0]) % N
                    ny = (y + sign * p[1]) % N
                    nz = (z + sign * p[2]) % N
                    j = indices[nx, ny, nz]
                    L[i, j] = -1.0

    return L.tocsr()


def compute_greens(N, source=(0, 0, 0)):
    """Compute G_K4(r, source) for all r on the N^3 K4 diamond lattice.

    Strategy: remove the k=0 zero mode by solving the regularized
    problem (L + eps * I) G = delta - mean(delta), projecting the
    constant mode out. For large N, eps -> 0 recovers the
    infinite-lattice G at r << N/2.
    """
    indices, n_total = build_lattice(N)
    L = build_laplacian(N)

    # Source delta: 1 at source, -1/n_total everywhere (charge-neutral,
    # so b is orthogonal to the constant kernel mode of L).
    delta = np.zeros(n_total)
    src_idx = indices[source[0], source[1], source[2]]
    delta[src_idx] = 1.0
    delta -= 1.0 / n_total

    # Moderate regularization so spsolve is well-conditioned on non-zero modes.
    # Then explicitly remove any residual constant-mode contamination.
    eps = 1e-4
    from scipy.sparse import eye as sparse_eye
    L_reg = L + eps * sparse_eye(n_total, format='csr')

    G_flat = spsolve(L_reg, delta)
    # Project out the kernel (constant) mode to recover the pseudoinverse solution:
    G_flat -= np.mean(G_flat)
    G = G_flat.reshape(N, N, N)

    # Normalize so G(source) corresponds to the Watson-integral value
    # (no additional normalization; output G is the raw Green's function
    # with our particular sign convention: Δ G = -source means G > 0
    # for a positive source charge.)
    return G


def main():
    N = 64  # larger for better asymptotic resolution
    print(f"Computing K4 Green's function on {N}^3 diamond lattice...")
    print(f"Total nodes: {N**3}")

    source = (N // 2, N // 2, N // 2)  # center of lattice to minimize boundary effects
    G_raw = compute_greens(N, source=source)

    # Periodic-image contamination: far-field value is a finite constant, not zero.
    # Subtract the value at the most-distant corner (diagonally opposite source) to
    # normalize so G(infty) = 0 and recover the infinite-lattice Green's function.
    corner = (0, 0, 0)  # diagonal opposite of center source
    far_field = G_raw[corner]
    G = G_raw - far_field

    # Extract G at the source (Watson integral analog)
    G_src = G[source]
    print(f"\nG_K4(0,0,0) = {G_src:.6f}  (on-site / self, far-field-subtracted)")
    print(f"Far-field value subtracted: {far_field:.6f}")

    # Extract at various displacements
    print(f"\n=== G_K4 at short distances (same or cross sublattice) ===")
    print(f"{'Displacement':<20} {'|r|':<8} {'parity':<8} {'G_K4':<12} {'continuum':<12} {'kappa_K4':<10}")

    # Displacements relevant for Golden Torus scale (1-3 units)
    short_dispers = [
        (1, 1, 1),   # bond, |r| = sqrt(3), B-site (if origin is A)
        (1, -1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
        (2, 0, 0),   # 2-step, A-site (if origin A)
        (0, 2, 0),
        (0, 0, 2),
        (1, 1, -1),  # NOT valid (3 non-tetrahedral)  -- wait, it has parity 1, so is a B
        (2, 2, 0),   # A
        (3, 1, 1),   # B via second-nearest
        (4, 0, 0),   # A
        (5, 1, 1),   # B
        (6, 0, 0),   # A
        (8, 0, 0),   # A
        (10, 0, 0),  # A
    ]

    for dx, dy, dz in short_dispers:
        x, y, z = source[0] + dx, source[1] + dy, source[2] + dz
        if 0 <= x < N and 0 <= y < N and 0 <= z < N:
            r = np.sqrt(dx**2 + dy**2 + dz**2)
            parity = (dx + dy + dz) % 2  # 0 if same-sublattice, 1 if cross
            val = G[x, y, z]
            continuum = 1.0 / (4 * np.pi * r) if r > 0 else float('inf')
            kappa = val / continuum if continuum > 0 else float('nan')
            parity_label = 'A' if parity == 0 else 'B'
            print(f"({dx:3d}, {dy:3d}, {dz:3d})      "
                  f"{r:.3f}   {parity_label:<7} "
                  f"{val:+.6f}  {continuum:+.6f}  {kappa:+.4f}")

    print(f"\n=== Convergence to continuum at larger distances ===")
    for r_x in [2, 4, 6, 8, 10, 12, 14, 16]:
        x = source[0] + r_x
        if x < N:
            val = G[x, source[1], source[2]]
            continuum = 1.0 / (4 * np.pi * r_x)
            kappa = val / continuum
            print(f"r = {r_x:3d}:  G = {val:+.6f}  continuum = {continuum:+.6f}  "
                  f"kappa = {kappa:+.4f}")

    # ── Specific Golden-Torus-relevant distances ──
    print(f"\n=== Golden-Torus crossing distance (d=1 in bond units = sqrt(3) Cartesian) ===")
    print("At each of the 3 crossings of the (2,3) winding at Golden Torus,")
    print("the two strand centerlines are exactly 1 bond = sqrt(3) ≈ 1.732 apart.")
    print(f"G_K4 at nearest-neighbor (tetrahedral bond vector) = {G[source[0]+1, source[1]+1, source[2]+1]:+.6f}")


if __name__ == "__main__":
    main()
