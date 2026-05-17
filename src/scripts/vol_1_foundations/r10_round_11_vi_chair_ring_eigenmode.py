"""r10_round_11_vi_chair_ring_eigenmode.py — Round 11 (vi) Stride 3 analytical work.

Solve the discrete Beltrami eigenvalue problem ∇×A = k·A on the chair-ring +
1-step K4 neighborhood graph, per [doc 89 §7.4](../../research/_archive/L3_electron_soliton/89_round_11_vi_stride_2_topological_mismatch.md).

DISCRETE CURL OPERATOR (derived analytically):
At each node n with 4 K4 ports {ê_i: i=0..3} pointing in 4 tetrahedral directions:

    ∂_i A := (A_neighbor_i - A_n) / bond_length     (directional derivative on bond)
    (∇×A)_n = (3/4) Σ_i ê_i × ∂_i A                  (discrete curl)

The (3/4) factor comes from tetrahedral 4-port symmetry: Σ ê_i ⊗ ê_i = (4/3)·I,
so Σ ê_i × ∂_i A in the continuum limit recovers (4/3)·∇×A. The (3/4) is the
inverse normalization.

EIGENVALUE PROBLEM:
At each node n: (3/4) Σ_i ê_i × ((A_neighbor_i - A_n) / bond_length) = k · A_n

This is a linear equation system: M · A_vec = k · A_vec, where:
- A_vec = stacked 3D vectors at all N_total nodes (3·N_total scalars)
- M = sparse curl matrix (3·N_total × 3·N_total)

Solve eigenvalues + eigenvectors of M; report dominant modes; identify the one
corresponding to (1,1) Beltrami at chair-ring scale; compare to continuum
prediction k_continuum ≈ 6.36 (in natural units where ℓ_node=1).

BOUNDARY CONDITIONS:
The chair-ring + 1-step subgraph has 18 active nodes. Out-of-ring nodes (12 of
them) have only 1 of their 4 K4 ports inside the subgraph; the other 3 ports
lead to 2-step+ neighbors. For a localized Beltrami eigenmode, A should decay
beyond 1-step → use Dirichlet boundary (A = 0 at all 2-step neighbors).

Per doc 89 §7.4 + auditor 2026-04-29: this is Stride 3 analytical work; v9 IC
construction follows from the eigenvector output. NO engine run in this script.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_JSON = Path(__file__).parent / "r10_round_11_vi_chair_ring_eigenmode_results.json"

# K4 port offsets (A-site convention; B-site = negation)
PORT_OFFSETS_A = [
    np.array([1, 1, 1]),
    np.array([1, -1, -1]),
    np.array([-1, 1, -1]),
    np.array([-1, -1, 1]),
]
SQRT_3 = np.sqrt(3.0)
BOND_LENGTH = SQRT_3  # tetrahedral diagonal in lattice units (ℓ_node = 1)


def is_a_site(pos):
    """True if (i,j,k) is on A-sublattice (all even)."""
    return all(c % 2 == 0 for c in pos)


def is_b_site(pos):
    """True if (i,j,k) is on B-sublattice (all odd)."""
    return all(c % 2 == 1 for c in pos)


def k4_neighbors(pos):
    """Return list of 4 K4 neighbors of pos with their (port_idx, neighbor_pos) pairs.

    For A-site: ports point in PORT_OFFSETS_A directions
    For B-site: ports point in -PORT_OFFSETS_A directions
    """
    sign = +1 if is_a_site(pos) else -1
    return [
        (i, tuple(int(c + sign * o) for c, o in zip(pos, PORT_OFFSETS_A[i])))
        for i in range(4)
    ]


def port_direction(pos, port_idx):
    """3D unit vector along port port_idx at node pos."""
    sign = +1 if is_a_site(pos) else -1
    return sign * PORT_OFFSETS_A[port_idx].astype(float) / SQRT_3


def build_chair_ring():
    """6-node chair-ring at origin (centered for clean coordinates)."""
    return [
        (0, 0, 0),     # n=0 A
        (1, 1, 1),     # n=1 B
        (0, 2, 2),     # n=2 A
        (-1, 3, 1),    # n=3 B
        (-2, 2, 0),    # n=4 A
        (-1, 1, -1),   # n=5 B
    ]


def build_subgraph(ring_nodes):
    """Build chair-ring + 1-step K4 neighborhood subgraph.

    Returns:
        node_list: list of all node positions (ring + 1-step neighbors)
        node_index: dict mapping position → index in node_list
        bonds: list of (node_a_idx, port_a, node_b_idx) — directed A→B bonds
    """
    node_list = list(ring_nodes)
    node_set = set(ring_nodes)

    # Add 1-step neighbors of ring nodes
    for ring_pos in ring_nodes:
        for port_idx, neighbor_pos in k4_neighbors(ring_pos):
            if neighbor_pos not in node_set:
                node_list.append(neighbor_pos)
                node_set.add(neighbor_pos)

    node_index = {pos: i for i, pos in enumerate(node_list)}

    # Build bonds: each pair of adjacent K4 nodes connected by a port
    # Directed A→B convention: port_idx labels the bond at the A-site
    bonds = []
    for pos in node_list:
        if is_a_site(pos):
            for port_idx, neighbor_pos in k4_neighbors(pos):
                if neighbor_pos in node_index:
                    bonds.append((node_index[pos], port_idx, node_index[neighbor_pos]))

    return node_list, node_index, bonds


def build_curl_matrix(node_list, node_index, n_ring):
    """Build the discrete curl matrix M acting on stacked A vectors.

    M is shape (3*N, 3*N) where N = len(node_list). M·A = k·A is the Beltrami
    eigenvalue equation.

    For each node n, the discrete curl is:
        (∇×A)_n = (3/4) · Σ_i ê_i × (A_neighbor_i - A_n) / bond_length

    where ê_i is the unit vector along port i at node n, and the sum is over
    the 4 K4 ports. If a neighbor is outside the subgraph (boundary), treat
    A_neighbor = 0 (Dirichlet).
    """
    N = len(node_list)
    M = np.zeros((3 * N, 3 * N), dtype=np.float64)

    for n_idx, pos in enumerate(node_list):
        # Computing (∇×A)_n at this node
        for port_idx in range(4):
            e_i = port_direction(pos, port_idx)  # 3D unit vector
            # Find neighbor along this port
            sign = +1 if is_a_site(pos) else -1
            neighbor_pos = tuple(int(c + sign * o) for c, o in zip(pos, PORT_OFFSETS_A[port_idx]))

            # Cross product matrix [e_i ×]
            ex, ey, ez = e_i
            cross_mat = np.array([
                [0, -ez, ey],
                [ez, 0, -ex],
                [-ey, ex, 0],
            ])

            # Coefficient: (3/4) × (1/bond_length)
            coef = (3.0 / 4.0) / BOND_LENGTH

            # Contribution from this port:
            # (3/4) · ê_i × (A_neighbor - A_n) / bond_length
            # = coef · cross_mat · A_neighbor - coef · cross_mat · A_n

            # Subtract A_n contribution: M[3n:3n+3, 3n:3n+3] -= coef · cross_mat
            M[3 * n_idx : 3 * n_idx + 3, 3 * n_idx : 3 * n_idx + 3] -= coef * cross_mat

            # Add A_neighbor contribution if neighbor is inside subgraph
            if neighbor_pos in node_index:
                neighbor_idx = node_index[neighbor_pos]
                M[3 * n_idx : 3 * n_idx + 3, 3 * neighbor_idx : 3 * neighbor_idx + 3] += coef * cross_mat
            # Else: Dirichlet boundary, A_neighbor = 0, no contribution

    return M


def find_chair_ring_modes(eigenvalues, eigenvectors, n_ring, ring_indices):
    """Find eigenmodes most localized at the chair-ring (vs out-of-ring).

    For each eigenvector, compute the fraction of |A|² localized at the 6 ring
    nodes vs the full 18 nodes. Return modes sorted by ring localization.
    """
    n_total = eigenvectors.shape[0] // 3
    n_modes = eigenvectors.shape[1]

    mode_data = []
    for m in range(n_modes):
        v = eigenvectors[:, m].reshape(n_total, 3)  # 3D vectors per node
        norms_sq = np.sum(np.abs(v) ** 2, axis=1)  # |A|² per node
        ring_energy = sum(norms_sq[i] for i in ring_indices)
        total_energy = norms_sq.sum()
        ring_loc = float(ring_energy / max(total_energy, 1e-30))

        # Beltrami amplitude at ring nodes
        ring_a_avg = np.mean([np.linalg.norm(v[i]) for i in ring_indices])

        mode_data.append({
            "index": m,
            "eigenvalue": complex(eigenvalues[m]),
            "ring_localization": ring_loc,
            "ring_amplitude_mean": float(ring_a_avg),
        })

    return sorted(mode_data, key=lambda x: -x["ring_localization"])


def main():
    print("=" * 78)
    print("  Round 11 (vi) Stride 3: discrete Beltrami eigenmode on chair-ring + 1-step K4")
    print("=" * 78)

    ring_nodes = build_chair_ring()
    node_list, node_index, bonds = build_subgraph(ring_nodes)
    n_total = len(node_list)
    n_ring = len(ring_nodes)
    n_out_of_ring = n_total - n_ring

    print(f"  Chair-ring nodes: {n_ring}")
    print(f"  Out-of-ring 1-step neighbors: {n_out_of_ring}")
    print(f"  Total nodes in subgraph: {n_total}")
    print(f"  Bonds in subgraph: {len(bonds)}")
    print(f"  Total DOF (3·N_total): {3 * n_total}")
    print()

    print("Ring nodes:")
    for i, pos in enumerate(ring_nodes):
        sub = "A" if is_a_site(pos) else "B"
        print(f"  n={i} ({sub}): {pos}")
    print()

    print("Out-of-ring 1-step neighbors:")
    for i in range(n_ring, n_total):
        pos = node_list[i]
        sub = "A" if is_a_site(pos) else "B"
        print(f"  n={i} ({sub}): {pos}")
    print()

    print("Building discrete curl matrix...")
    M = build_curl_matrix(node_list, node_index, n_ring)
    print(f"  Matrix shape: {M.shape}")
    print(f"  Sparsity: {np.count_nonzero(M) / M.size * 100:.1f}% nonzero")
    print(f"  Symmetric? {np.allclose(M, M.T)}")
    print(f"  Anti-symmetric? {np.allclose(M, -M.T)}")
    print()

    print("Solving eigenvalue problem...")
    eigenvalues, eigenvectors = np.linalg.eig(M)
    print(f"  {len(eigenvalues)} eigenvalues found")

    # Sort by eigenvalue magnitude
    abs_eigs = np.abs(eigenvalues)
    sort_idx = np.argsort(abs_eigs)[::-1]
    eigenvalues = eigenvalues[sort_idx]
    eigenvectors = eigenvectors[:, sort_idx]

    # Eigenvalue spectrum
    print()
    print("Eigenvalue spectrum (top 20 by magnitude):")
    for i in range(min(20, len(eigenvalues))):
        ev = eigenvalues[i]
        print(f"  λ_{i}: {ev.real:+.4f} + {ev.imag:+.4f}j  (|λ| = {abs(ev):.4f})")

    # For Hermitian discrete curl (anti-symmetric matrix), eigenvalues are
    # purely imaginary. |λ| corresponds to the physical Beltrami k value.
    # Identify modes most localized at the chair-ring
    ring_indices = list(range(n_ring))
    mode_data = find_chair_ring_modes(eigenvalues, eigenvectors, n_ring, ring_indices)

    print()
    print("Top 10 modes by chair-ring localization:")
    for mode in mode_data[:10]:
        print(f"  λ = {mode['eigenvalue'].real:+.4f}{mode['eigenvalue'].imag:+.4f}j  "
              f"|λ| = {abs(mode['eigenvalue']):.4f}  "
              f"ring_loc = {mode['ring_localization']:.4f}  "
              f"ring_amp = {mode['ring_amplitude_mean']:.4f}")

    # Compare to continuum prediction
    k_continuum_11 = np.sqrt(4 * np.pi**2 + 1)  # (1,1) Beltrami at R=1, r=1/(2π)
    print()
    print(f"Continuum (1,1) Beltrami prediction at corpus geometry:")
    print(f"  k_continuum = √((2π)² + 1²) = √(4π² + 1) ≈ {k_continuum_11:.4f}")
    print()
    print(f"Discrete eigenvalues to compare (|λ| should be in 1/bond_length units):")
    print(f"  bond_length = √3, so to convert from 1/bond_length to 1/ℓ_node, multiply by √3:")
    for mode in mode_data[:5]:
        k_disc = abs(mode['eigenvalue'])
        k_disc_lnode = k_disc * SQRT_3
        print(f"  Mode |λ| = {k_disc:.4f} → k in 1/ℓ_node = {k_disc_lnode:.4f}  "
              f"(continuum (1,1): {k_continuum_11:.4f})")

    # Extract dominant ring-localized eigenvector for v9 IC construction
    print()
    print("=" * 78)
    print("  Dominant ring-localized eigenmode analysis (for v9 IC)")
    print("=" * 78)

    # Find the eigenvector index for the top ring-localized mode
    top_mode = mode_data[0]
    # Need to find the column in eigenvectors matrix; search by eigenvalue match
    top_eigvec_idx = None
    for col in range(len(eigenvalues)):
        if (abs(eigenvalues[col] - complex(top_mode["eigenvalue"])) < 1e-10):
            v = eigenvectors[:, col].reshape(n_total, 3)
            ring_e = sum(np.sum(np.abs(v[i]) ** 2) for i in range(n_ring))
            total_e = np.sum(np.abs(v) ** 2)
            if abs(ring_e/total_e - top_mode["ring_localization"]) < 1e-6:
                top_eigvec_idx = col
                break
    if top_eigvec_idx is None:
        top_eigvec_idx = 0

    top_eigvec = eigenvectors[:, top_eigvec_idx].reshape(n_total, 3)
    print(f"  Top ring-localized mode: λ = {eigenvalues[top_eigvec_idx]:.4f}, "
          f"ring_loc = {top_mode['ring_localization']:.4f}")
    print()
    print(f"  Eigenvector A_0 at ring nodes (real part):")
    for i in range(n_ring):
        a = top_eigvec[i].real
        mag = np.linalg.norm(a)
        print(f"    n={i} ({'A' if is_a_site(node_list[i]) else 'B'}) {node_list[i]}: "
              f"A_0 = ({a[0]:+.4f}, {a[1]:+.4f}, {a[2]:+.4f}), |A_0| = {mag:.4f}")
    print()
    print(f"  Eigenvector A_0 at out-of-ring 1-step neighbors (real part):")
    for i in range(n_ring, n_total):
        a = top_eigvec[i].real
        mag = np.linalg.norm(a)
        print(f"    n={i} {node_list[i]}: |A_0| = {mag:.4f}")
    print()

    # Compute mean amplitudes at ring vs out-of-ring
    ring_amps = [np.linalg.norm(top_eigvec[i].real) for i in range(n_ring)]
    out_ring_amps = [np.linalg.norm(top_eigvec[i].real) for i in range(n_ring, n_total)]
    print(f"  Mean amplitude at ring nodes: {np.mean(ring_amps):.4f}")
    print(f"  Mean amplitude at out-of-ring: {np.mean(out_ring_amps):.4f}")
    print(f"  Ring/out-of-ring amplitude ratio: {np.mean(ring_amps)/max(np.mean(out_ring_amps), 1e-12):.4f}")
    print()

    # Save results
    payload = {
        "scope": "Round 11 (vi) Stride 3 — discrete Beltrami eigenmode on chair-ring + 1-step K4",
        "subgraph": {
            "n_ring": n_ring,
            "n_out_of_ring": n_out_of_ring,
            "n_total": n_total,
            "n_bonds": len(bonds),
            "ring_nodes": [list(p) for p in ring_nodes],
            "out_of_ring_nodes": [list(node_list[i]) for i in range(n_ring, n_total)],
        },
        "curl_matrix_properties": {
            "shape": list(M.shape),
            "sparsity_nonzero_fraction": float(np.count_nonzero(M) / M.size),
            "is_symmetric": bool(np.allclose(M, M.T)),
            "is_antisymmetric": bool(np.allclose(M, -M.T)),
        },
        "continuum_prediction": {
            "k_continuum_11_at_corpus": float(k_continuum_11),
            "note": "(1,1) Beltrami at R=1, r=1/(2π); k² = (2π)² + 1²",
        },
        "top_20_eigenvalues": [
            {
                "index": i,
                "real": float(eigenvalues[i].real),
                "imag": float(eigenvalues[i].imag),
                "magnitude": float(abs(eigenvalues[i])),
            }
            for i in range(min(20, len(eigenvalues)))
        ],
        "top_10_chair_ring_localized_modes": [
            {
                "eigenvalue_real": float(mode['eigenvalue'].real),
                "eigenvalue_imag": float(mode['eigenvalue'].imag),
                "magnitude": float(abs(mode['eigenvalue'])),
                "ring_localization": float(mode['ring_localization']),
                "ring_amplitude_mean": float(mode['ring_amplitude_mean']),
                "k_in_lnode_units": float(abs(mode['eigenvalue']) * SQRT_3),
            }
            for mode in mode_data[:10]
        ],
        "top_ring_localized_eigenvector": {
            "eigenvalue": float(eigenvalues[top_eigvec_idx].real),
            "ring_localization": float(top_mode["ring_localization"]),
            "A_0_at_ring_nodes": [
                {"index": i, "position": list(node_list[i]),
                 "A_0": top_eigvec[i].real.tolist(),
                 "magnitude": float(np.linalg.norm(top_eigvec[i].real))}
                for i in range(n_ring)
            ],
            "A_0_at_out_of_ring_nodes": [
                {"index": i, "position": list(node_list[i]),
                 "A_0": top_eigvec[i].real.tolist(),
                 "magnitude": float(np.linalg.norm(top_eigvec[i].real))}
                for i in range(n_ring, n_total)
            ],
            "mean_ring_amplitude": float(np.mean(ring_amps)),
            "mean_out_of_ring_amplitude": float(np.mean(out_ring_amps)),
            "amplitude_ratio_ring_over_out": float(np.mean(ring_amps) / max(np.mean(out_ring_amps), 1e-12)),
        },
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print()
    print(f"Results saved: {OUTPUT_JSON.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
