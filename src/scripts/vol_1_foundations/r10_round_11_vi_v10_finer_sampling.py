"""r10_round_11_vi_v10_finer_sampling.py — Round 11 (vi) Stride 5 / v10 (i-a) test.

Per doc 91 + auditor 2026-04-29: v9 Mode III led to Round 11 (vi) closure into
secondary candidates. (i-a) numerical refinement test: does the discrete K4
eigenvalue spectrum approach the continuum (1,1) Beltrami prediction (k=6.36
in 1/ℓ_node units) as we add more K4 neighborhood nodes (2-step, 3-step)?

LOCKED QUESTION: is the 12× gap (continuum k=6.36 vs Stride 3 chair-ring +
1-step k_disc=0.52 in 1/ℓ_node) STRUCTURAL (caps below 6.36 even at full K4
lattice) or REFINABLE (closes monotonically with more nodes)?

If REFINABLE → framework intact, v6/v7/v8/v9 were under-sampled approximations
If STRUCTURAL → Ax 1 K4-at-ℓ_node substrate insufficient; finer-than-K4 needed

This script extends Stride 3's eigenvalue solver to chair-ring + N-step K4
neighborhood for N = 1, 2, 3. Reports for each:
- Subgraph node count
- Eigenvalue spectrum top |λ|
- k_in_lnode_units corrected via /√3 conversion
- Most ring-localized mode's k value
- Trajectory of how max k approaches continuum 6.36

Discrete curl operator (per Stride 3): ∇×A = (3/4) Σ ê_i × (A_neighbor - A_n) / bond_length
Boundary condition: Dirichlet (A=0 outside subgraph)

Per doc 86 §7.6 + doc 87 §7.2 locked gate logic: this is v10 = secondary
candidate (i-a) test. NOT a v9 IC tweak. Test is analytical only — NO engine
run, just eigenvalue computation at increasing subgraph sizes.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_JSON = Path(__file__).parent / "r10_round_11_vi_v10_finer_sampling_results.json"

PORT_OFFSETS_A = [
    np.array([1, 1, 1]),
    np.array([1, -1, -1]),
    np.array([-1, 1, -1]),
    np.array([-1, -1, 1]),
]
SQRT_3 = np.sqrt(3.0)
BOND_LENGTH = SQRT_3


def is_a_site(pos):
    return all(c % 2 == 0 for c in pos)


def k4_neighbors(pos):
    sign = +1 if is_a_site(pos) else -1
    return [
        (i, tuple(int(c + sign * o) for c, o in zip(pos, PORT_OFFSETS_A[i])))
        for i in range(4)
    ]


def port_direction(pos, port_idx):
    sign = +1 if is_a_site(pos) else -1
    return sign * PORT_OFFSETS_A[port_idx].astype(float) / SQRT_3


def build_chair_ring():
    return [
        (0, 0, 0), (1, 1, 1), (0, 2, 2),
        (-1, 3, 1), (-2, 2, 0), (-1, 1, -1),
    ]


def build_n_step_neighborhood(ring_nodes, max_steps):
    """Build chair-ring + N-step K4 neighborhood subgraph.

    Returns (node_list, node_index, ring_indices) where ring_indices are
    the indices of the original 6 ring nodes within node_list.
    """
    node_list = list(ring_nodes)
    node_set = set(ring_nodes)
    distance = {pos: 0 for pos in ring_nodes}

    current_shell = list(ring_nodes)
    for step in range(1, max_steps + 1):
        next_shell = []
        for pos in current_shell:
            for _, neighbor_pos in k4_neighbors(pos):
                if neighbor_pos not in node_set:
                    node_set.add(neighbor_pos)
                    node_list.append(neighbor_pos)
                    distance[neighbor_pos] = step
                    next_shell.append(neighbor_pos)
        current_shell = next_shell

    node_index = {pos: i for i, pos in enumerate(node_list)}
    ring_indices = list(range(len(ring_nodes)))

    # Count nodes per shell
    shell_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for pos in node_list:
        d = distance.get(pos, max_steps + 1)
        if d <= 3:
            shell_counts[d] += 1

    return node_list, node_index, ring_indices, shell_counts


def build_curl_matrix(node_list, node_index):
    N = len(node_list)
    M = np.zeros((3 * N, 3 * N), dtype=np.float64)

    for n_idx, pos in enumerate(node_list):
        for port_idx in range(4):
            e_i = port_direction(pos, port_idx)
            sign = +1 if is_a_site(pos) else -1
            neighbor_pos = tuple(int(c + sign * o) for c, o in zip(pos, PORT_OFFSETS_A[port_idx]))

            ex, ey, ez = e_i
            cross_mat = np.array([
                [0, -ez, ey],
                [ez, 0, -ex],
                [-ey, ex, 0],
            ])

            coef = (3.0 / 4.0) / BOND_LENGTH
            M[3 * n_idx : 3 * n_idx + 3, 3 * n_idx : 3 * n_idx + 3] -= coef * cross_mat

            if neighbor_pos in node_index:
                neighbor_idx = node_index[neighbor_pos]
                M[3 * n_idx : 3 * n_idx + 3, 3 * neighbor_idx : 3 * neighbor_idx + 3] += coef * cross_mat
            # Dirichlet: A_neighbor = 0 if outside subgraph

    return M


def find_top_ring_localized_modes(eigenvalues, eigenvectors, ring_indices, n_total, top_k=10):
    """Find top-k eigenmodes by ring localization."""
    mode_data = []
    for m in range(eigenvectors.shape[1]):
        v = eigenvectors[:, m].reshape(n_total, 3)
        norms_sq = np.sum(np.abs(v) ** 2, axis=1)
        ring_energy = sum(norms_sq[i] for i in ring_indices)
        total_energy = norms_sq.sum()
        ring_loc = float(ring_energy / max(total_energy, 1e-30))
        mode_data.append({
            "eigenvalue_real": float(eigenvalues[m].real),
            "eigenvalue_imag": float(eigenvalues[m].imag),
            "magnitude": float(abs(eigenvalues[m])),
            "ring_localization": ring_loc,
        })
    return sorted(mode_data, key=lambda x: -x["ring_localization"])[:top_k]


def analyze_at_max_steps(max_steps, ring_nodes):
    print(f"\n{'='*78}")
    print(f"  Subgraph at max_steps = {max_steps} (chair-ring + {max_steps}-step neighborhood)")
    print(f"{'='*78}")

    node_list, node_index, ring_indices, shell_counts = build_n_step_neighborhood(ring_nodes, max_steps)
    n_total = len(node_list)
    print(f"  Total nodes: {n_total}")
    print(f"  Shell breakdown: ring(6) + 1-step({shell_counts[1]}) + 2-step({shell_counts.get(2,0)}) + 3-step({shell_counts.get(3,0)})")
    print(f"  DOF (3·N_total): {3 * n_total}")
    print(f"  Curl matrix shape: ({3 * n_total}, {3 * n_total})")

    M = build_curl_matrix(node_list, node_index)
    print(f"  Sparsity: {np.count_nonzero(M) / M.size * 100:.1f}% nonzero")
    print(f"  Symmetric? {np.allclose(M, M.T)}")

    eigenvalues, eigenvectors = np.linalg.eig(M)

    abs_eigs = np.abs(eigenvalues)
    sort_idx = np.argsort(abs_eigs)[::-1]
    eigenvalues = eigenvalues[sort_idx]
    eigenvectors = eigenvectors[:, sort_idx]

    max_eig = abs(eigenvalues[0])
    max_eig_lnode = max_eig / SQRT_3  # CORRECTED conversion (doc 91 §1)

    print(f"\n  Spectrum max |λ| = {max_eig:.4f} (1/bond_length)")
    print(f"  Max k in 1/ℓ_node units (corrected: /√3) = {max_eig_lnode:.4f}")
    print(f"  Continuum (1,1) at corpus: k = √(4π² + 1) ≈ 6.3623")
    print(f"  Discrete/continuum ratio: {max_eig_lnode / 6.3623:.4f}")

    # Top 10 modes by ring localization
    top_modes = find_top_ring_localized_modes(eigenvalues, eigenvectors, ring_indices, n_total)

    print(f"\n  Top 5 ring-localized modes:")
    for i, mode in enumerate(top_modes[:5]):
        k_lnode = mode['magnitude'] / SQRT_3
        print(f"    rank {i}: |λ| = {mode['magnitude']:.4f} → k_lnode = {k_lnode:.4f}, "
              f"ring_loc = {mode['ring_localization']:.4f}")

    return {
        "max_steps": max_steps,
        "n_total": n_total,
        "shell_counts": shell_counts,
        "spectrum_max_magnitude": float(max_eig),
        "spectrum_max_k_lnode": float(max_eig_lnode),
        "spectrum_max_to_continuum_ratio": float(max_eig_lnode / 6.3623),
        "top_5_ring_localized_modes": [
            {**m, "k_lnode": float(m["magnitude"] / SQRT_3)}
            for m in top_modes[:5]
        ],
        "top_ring_localized_k_lnode": float(top_modes[0]["magnitude"] / SQRT_3),
        "top_ring_localized_loc": float(top_modes[0]["ring_localization"]),
    }


def main():
    print("="*78)
    print("  Round 11 (vi) v10 (i-a): finer K4 sampling — does discrete spectrum")
    print("  approach continuum (1,1) k=6.36 with more neighborhood nodes?")
    print("="*78)

    ring_nodes = build_chair_ring()
    K_CONTINUUM_11 = np.sqrt(4 * np.pi ** 2 + 1)  # = 6.3623
    K_COMPTON = 1.0  # in 1/ℓ_node units

    results_per_step = []
    for max_steps in [1, 2, 3]:
        result = analyze_at_max_steps(max_steps, ring_nodes)
        results_per_step.append(result)

    # Summary trajectory
    print(f"\n\n{'='*78}")
    print(f"  TRAJECTORY: discrete spectrum max k_lnode vs subgraph size")
    print(f"{'='*78}")
    print(f"  {'max_steps':<12}{'n_total':<12}{'spectrum_max_k_lnode':<25}{'continuum_ratio':<20}{'top_ring_loc_k':<20}")
    for r in results_per_step:
        print(f"  {r['max_steps']:<12}{r['n_total']:<12}{r['spectrum_max_k_lnode']:<25.4f}{r['spectrum_max_to_continuum_ratio']:<20.4f}{r['top_ring_localized_k_lnode']:<20.4f}")

    print(f"\n  Continuum (1,1) at corpus: k = {K_CONTINUUM_11:.4f}")
    print(f"  Compton frequency: k = {K_COMPTON:.4f}")
    print(f"\n  CONCLUSION:")
    if results_per_step[-1]["spectrum_max_k_lnode"] > 0.9 * K_CONTINUUM_11:
        print(f"    Spectrum max APPROACHES continuum 6.36 with finer sampling — REFINABLE")
        print(f"    Framework intact at K4 substrate; v6/v7/v8/v9 were under-sampled approximations")
    elif results_per_step[-1]["spectrum_max_k_lnode"] > 1.0:
        print(f"    Spectrum max GROWS with sampling but doesn't reach continuum 6.36")
        print(f"    Continues to grow with more nodes? Need deeper sampling test")
    else:
        print(f"    Spectrum max STAYS BELOW Compton k=1.0 even at 3-step neighborhood")
        print(f"    Suggests STRUCTURAL — K4 at ℓ_node sampling cannot host continuum (1,1)")
        print(f"    Path forward: (i-b) substrate revision OR continuum FDTD test")

    payload = {
        "scope": "Round 11 (vi) v10 (i-a) test: finer K4 sampling spectrum trajectory",
        "ring_nodes": [list(p) for p in ring_nodes],
        "continuum_11_at_corpus_k_lnode": float(K_CONTINUUM_11),
        "compton_k_lnode": K_COMPTON,
        "trajectory": results_per_step,
        "interpretation": (
            "REFINABLE" if results_per_step[-1]["spectrum_max_k_lnode"] > 0.9 * K_CONTINUUM_11
            else "GROWING (test deeper)" if results_per_step[-1]["spectrum_max_k_lnode"] > 1.0
            else "STRUCTURAL (cap below Compton)"
        ),
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Result: {OUTPUT_JSON.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
