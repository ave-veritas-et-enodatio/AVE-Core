"""
r10 EE Phase A — Control B2: refined Faraday's law check on chair-ring loop.

Post-hoc analysis on existing capture .npz. Refines Φ_B integration by
including the chair-ring centroid's ω vector (already captured in
interior_omega). Tests whether the 99.98% Faraday violation in A2 is
(a) a coarse-Φ_B-sampling artifact (single-patch hex-area approximation
too crude) vs (b) genuine discrete K4-TLM gauge violation at the closure
loop level.

Three Φ_B estimators compared:
  (i)  ring-only single-patch:       Φ_B ≈ ⟨ω·n̂⟩_ring × hex_area  (= A2's method)
  (ii) centroid-only single-patch:   Φ_B ≈ (ω·n̂)_centroid × hex_area
  (iii) triangle-midpoint Simpson:   split hex into 6 triangles from centroid;
                                      Simpson rule with vertex+centroid
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).parent))

import r10_path_alpha_v8_corrected_measurements as v8


def main():
    print("=" * 78, flush=True)
    print("  r10 EE Phase A — Control B2: refined Faraday's law check")
    print("=" * 78, flush=True)

    npz_path = Path(__file__).parent / "r10_v8_ee_phase_a_capture.npz"
    print(f"Loading {npz_path.relative_to(Path.cwd())}...", flush=True)
    cap = np.load(npz_path, allow_pickle=True)

    DT = float(cap["DT"][0])
    N = int(cap["n_steps"][0])
    nodes = cap["nodes"]
    centroid = cap["centroid"]
    interior_pts = cap["interior_pts"]
    omega_ring = cap["omega"]               # (N, 6, 3)
    omega_interior = cap["interior_omega"]  # (N, n_interior, 3)
    v_inc = cap["v_inc"]                     # (N, 6, 4)
    v_ref = cap["v_ref"]                     # (N, 6, 4)

    # bonds wasn't saved to npz (list of dicts); reconstruct from v8.build_chair_ring
    _, bonds = v8.build_chair_ring(v8.CENTER)

    sw_start = N // 4
    print(f"  N steps: {N}, sw_start: {sw_start}, post-transient samples: {N-sw_start}")
    print(f"  Interior points captured: {len(interior_pts)}")

    # Loop normal
    edge1 = nodes[0] - centroid
    edge2 = nodes[2] - centroid
    n_hat = np.cross(edge1, edge2)
    n_hat = n_hat / np.linalg.norm(n_hat)
    R_ring = float(np.linalg.norm(edge1))
    hex_area = (3.0 * np.sqrt(3.0) / 2.0) * R_ring ** 2
    print(f"  Loop normal n̂: {n_hat.tolist()}")
    print(f"  Ring radius (lnode units): {R_ring:.4f}")
    print(f"  Hexagon area: {hex_area:.4f} ℓ_node²")

    # Compute ∮V·dl(t) per step using V_inc + V_ref = V_total
    n_node_idx = {tuple(n): i for i, n in enumerate(nodes.tolist())}
    loop_V_traj = np.zeros(N)
    for i in range(N):
        loop_V = 0.0
        for bnd in bonds:
            a_site = tuple(bnd["a_site"])
            ring_idx_of_a = n_node_idx[a_site]
            port = bnd["port"]
            a_to_b = np.array(bnd["a_to_b_offset"], dtype=float)
            a_to_b /= np.linalg.norm(a_to_b)
            traversal = np.array(bnd["traversal_direction"], dtype=float)
            sign = float(np.sign(np.dot(a_to_b, traversal)))
            v_total = float(v_inc[i, ring_idx_of_a, port] + v_ref[i, ring_idx_of_a, port])
            loop_V += sign * v_total
        loop_V_traj[i] = loop_V
    loop_V_DC = float(loop_V_traj[sw_start:].mean())

    # Three Φ_B estimators
    omega_normal_ring = omega_ring @ n_hat                 # (N, 6)
    omega_normal_interior = omega_interior @ n_hat          # (N, n_interior)

    Phi_B_i = (omega_normal_ring.mean(axis=1)) * hex_area                # ring-only
    Phi_B_ii = (omega_normal_interior[:, 0]) * hex_area                  # centroid-only
    # Triangle-midpoint Simpson: each of 6 triangles has 1/6 of hex_area
    # Simpson rule on each triangle: (1/3)·(f_v1 + f_centroid + f_v2) × area_tri
    # (3-point average for triangle)
    Phi_B_iii = np.zeros(N)
    area_tri = hex_area / 6.0
    for i in range(N):
        omega_c = omega_normal_interior[i, 0]
        accum = 0.0
        for k in range(6):
            v1 = omega_normal_ring[i, k]
            v2 = omega_normal_ring[i, (k+1) % 6]
            accum += (v1 + v2 + omega_c) / 3.0 * area_tri
        Phi_B_iii[i] = accum

    t_vec = np.arange(N) * DT
    sw = slice(sw_start, N)

    def fit_slope(y):
        return float(np.polyfit(t_vec[sw], y[sw], 1)[0])

    dPhiB_dt_i = fit_slope(Phi_B_i)
    dPhiB_dt_ii = fit_slope(Phi_B_ii)
    dPhiB_dt_iii = fit_slope(Phi_B_iii)

    expected = -loop_V_DC

    def residual(d):
        return d - expected, abs(d - expected) / max(abs(loop_V_DC), 1e-15) * 100

    res_i, pct_i = residual(dPhiB_dt_i)
    res_ii, pct_ii = residual(dPhiB_dt_ii)
    res_iii, pct_iii = residual(dPhiB_dt_iii)

    # Also report the raw mean ω·n̂ at each location
    ring_norm_mean = float(omega_normal_ring[sw].mean())
    centroid_norm_mean = float(omega_normal_interior[sw, 0].mean())

    print()
    print(f"  Mean ⟨ω·n̂⟩ steady-state:")
    print(f"    at ring (6-node avg):  {ring_norm_mean:+.4e}")
    print(f"    at centroid:           {centroid_norm_mean:+.4e}")
    print(f"    ratio centroid / ring: {centroid_norm_mean / max(abs(ring_norm_mean), 1e-15):+.4e}")

    print()
    print(f"  ∮V·dl steady DC: {loop_V_DC:+.4e}")
    print(f"  Faraday expects dΦ_B/dt = {expected:+.4e}")
    print()
    print(f"  Φ_B estimator (i)   ring-only:        dΦ_B/dt = {dPhiB_dt_i:+.4e}, residual = {res_i:+.4e} ({pct_i:.2f}% of ∮V·dl)")
    print(f"  Φ_B estimator (ii)  centroid-only:    dΦ_B/dt = {dPhiB_dt_ii:+.4e}, residual = {res_ii:+.4e} ({pct_ii:.2f}% of ∮V·dl)")
    print(f"  Φ_B estimator (iii) Simpson 6-tri:    dPhi_B/dt = {dPhiB_dt_iii:+.4e}, residual = {res_iii:+.4e} ({pct_iii:.2f}% of ∮V·dl)")

    # Verdict
    min_pct = min(pct_i, pct_ii, pct_iii)
    if min_pct < 10:
        verdict = (
            f"FARADAY HOLDS at the discrete K4-TLM level if best estimator is correct (residual {min_pct:.1f}%). "
            f"DC EMF DOES correspond to a real magnetic flux growing through the loop."
        )
    elif min_pct < 50:
        verdict = (
            f"PARTIAL Faraday consistency (residual {min_pct:.1f}%). "
            f"Φ_B sampling needs further refinement to fully resolve."
        )
    else:
        verdict = (
            f"FARADAY VIOLATED at all sampling refinements (residual {min_pct:.1f}%). "
            f"Discrete K4-TLM does not preserve Faraday at the closure-loop level. "
            f"DC EMF is a discrete-scheme gauge artifact, not a real magnetic flux."
        )
    print()
    print(f"  Verdict: {verdict}")

    out = {
        "test": "Control B2: refined Faraday's law check",
        "loop_V_DC": loop_V_DC,
        "expected_dPhi_B_dt": expected,
        "ring_omega_normal_mean": ring_norm_mean,
        "centroid_omega_normal_mean": centroid_norm_mean,
        "ratio_centroid_to_ring": centroid_norm_mean / max(abs(ring_norm_mean), 1e-15),
        "estimator_i_ring_only": {
            "dPhi_B_dt": dPhiB_dt_i, "residual": res_i, "pct_of_loop_V": pct_i,
        },
        "estimator_ii_centroid_only": {
            "dPhi_B_dt": dPhiB_dt_ii, "residual": res_ii, "pct_of_loop_V": pct_ii,
        },
        "estimator_iii_simpson_6tri": {
            "dPhi_B_dt": dPhiB_dt_iii, "residual": res_iii, "pct_of_loop_V": pct_iii,
        },
        "verdict": verdict,
    }
    out_path = Path(__file__).parent / "r10_v8_ee_phase_a_b2_faraday_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
