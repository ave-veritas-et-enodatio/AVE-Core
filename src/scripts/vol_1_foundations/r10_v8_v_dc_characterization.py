"""
r10 path α v8 V_DC spatial characterization.

Follow-up to r10_v8_dc_ac_reanalysis.py (which empirically refuted the
simple DC/AC reframe at the rotational sector but surfaced a partial
capacitive-DC signal: V_DC ≈ 0.19-0.22 V_SNAP at A-sites, ∮V_DC·dl ≈
0.632 around the ring, suggestively close to 2/π = 0.637).

Per Rule 9 v2 (characterize-as-itself first) + auditor 2026-04-29:
walk the V_DC structure as itself before any test design or
interpretation.

Six characterization axes (auditor + implementer):
  (1) V_DC vector at each A-site in lattice coordinates (3-component)
  (2) V_DC alignment with K4 port directions (4-fold structure)
  (3) V_DC alignment with bond tangent (along loop?)
  (4) V_DC dot product between adjacent A-sites (correlation length)
  (5) V_DC magnitudes — 2-fold symmetry from helical IC, or coincidence?
  (6) ∮V_DC·dl per-bond decomposition (which bonds carry the winding?)

Plus: V_DC in local Frenet frame (tangent, radial, binormal) at each
A-site to detect Möbius-wrap signature (180° rotation per ring
traversal) vs Hopf-wrap (360°) vs no wrap.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from ave.core.constants import V_SNAP

import r10_path_alpha_v8_corrected_measurements as v8


def detrend_with_slope(traj):
    n_steps = traj.shape[0]
    t = np.arange(n_steps, dtype=np.float64)
    t_mean = t.mean()
    t_var = ((t - t_mean) ** 2).sum()
    mean = traj.mean(axis=0)
    slope_num = ((t[:, None, None, None, None] - t_mean) * (traj - mean[None, ...])).sum(axis=0)
    slope = slope_num / t_var
    return slope


def normalize(v):
    n = np.linalg.norm(v)
    if n < 1e-15:
        return v
    return v / n


def main():
    print("=" * 78, flush=True)
    print("  r10 path α v8 V_DC spatial characterization  [T=0]")
    print("=" * 78, flush=True)

    nodes, bonds = v8.build_chair_ring(v8.CENTER)
    a_0_per_node, centroid = v8.compute_a_0_at_ring_nodes(
        nodes, v8.A_AMP_POL, v8.HELICAL_PITCH
    )

    # Identify A-sites (even-parity lattice positions per K4 bipartite convention)
    a_site_ring_idxs = [i for i, n in enumerate(nodes) if all(c % 2 == 0 for c in n)]
    print(f"A-site ring indices: {a_site_ring_idxs}")

    engine = VacuumEngine3D.from_args(
        N=v8.N_LATTICE, pml=v8.PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    print("Applying v8 helical Beltrami IC...", flush=True)
    v8.initialize_helical_beltrami_ic(
        engine, nodes, bonds, a_0_per_node,
        v8.K_BELTRAMI, v8.V_AMP, v8.PHI_AMP,
    )

    nx = engine.k4.nx
    N_STEPS = v8.N_RECORDING_STEPS
    print(f"Recording {N_STEPS} steps for slope linear fit...", flush=True)
    phi_link_traj = np.zeros((N_STEPS, nx, nx, nx, 4), dtype=np.float32)
    t0 = time.time()
    last = t0
    for i in range(N_STEPS):
        engine.step()
        phi_link_traj[i] = engine.k4.Phi_link.astype(np.float32)
        if (time.time() - last) > 30.0:
            t_p = (i + 1) * v8.DT / v8.COMPTON_PERIOD
            print(f"    step {i}/{N_STEPS}, t={t_p:.1f}P, elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)

    print("Computing V_DC per port from Phi_link slope...", flush=True)
    phi_slope = detrend_with_slope(phi_link_traj.astype(np.float64))
    V_DC_per_port = phi_slope / v8.DT  # shape (nx, ny, nz, 4) in V_SNAP units

    # ── Characterization at A-sites ──────────────────────────────────────────
    port_dirs_normalized = np.array([normalize(p.astype(float)) for p in v8.PORT_OFFSETS_A])

    a_site_data = {}
    for ring_idx in a_site_ring_idxs:
        node = nodes[ring_idx]
        ix, iy, iz = node
        v_dc_4ports = V_DC_per_port[ix, iy, iz, :]  # shape (4,)

        # 3D vector reconstruction: V_DC vector = sum over ports of V_DC[port] * port_direction
        # This is the engine-native "vector A reconstruction" used elsewhere
        v_dc_vec = np.zeros(3)
        for p in range(4):
            v_dc_vec += v_dc_4ports[p] * port_dirs_normalized[p]
        # Standard Moore-Penrose: ×(3/4)
        v_dc_vec *= (3.0 / 4.0)

        # Frenet frame at this ring node
        tangent, radial, binormal = v8.ring_frame_at_node(nodes, ring_idx, centroid)

        # Project V_DC vector onto Frenet basis
        v_dc_t = float(np.dot(v_dc_vec, tangent))
        v_dc_r = float(np.dot(v_dc_vec, radial))
        v_dc_b = float(np.dot(v_dc_vec, binormal))

        # Alignment of V_DC vector with bond port (the port that points to next ring node)
        # Find which port is the outgoing-bond port
        next_node = np.array(nodes[(ring_idx + 1) % 6])
        offset_to_next = next_node - np.array(node)
        bond_port_idx = int(np.argmin([np.linalg.norm(offset_to_next - p) for p in v8.PORT_OFFSETS_A]))
        v_dc_along_bond = v_dc_4ports[bond_port_idx]

        a_site_data[ring_idx] = {
            "node_position": list(node),
            "V_DC_per_port": v_dc_4ports.tolist(),
            "V_DC_vector_lattice": v_dc_vec.tolist(),
            "V_DC_magnitude_vec": float(np.linalg.norm(v_dc_vec)),
            "V_DC_magnitude_4port_rms": float(np.sqrt(np.sum(v_dc_4ports ** 2))),
            "Frenet_tangent": tangent.tolist(),
            "Frenet_radial": radial.tolist(),
            "Frenet_binormal": binormal.tolist(),
            "V_DC_in_Frenet": {"tangent": v_dc_t, "radial": v_dc_r, "binormal": v_dc_b},
            "bond_port_index": bond_port_idx,
            "V_DC_along_bond": float(v_dc_along_bond),
        }

    # ── Adjacent A-site correlations ─────────────────────────────────────────
    a_site_pairs = []
    a_idx_list = a_site_ring_idxs  # [0, 2, 4]
    for i in range(len(a_idx_list)):
        a = a_idx_list[i]
        b = a_idx_list[(i + 1) % len(a_idx_list)]
        v_a = np.array(a_site_data[a]["V_DC_vector_lattice"])
        v_b = np.array(a_site_data[b]["V_DC_vector_lattice"])
        norm_a = np.linalg.norm(v_a)
        norm_b = np.linalg.norm(v_b)
        dot = float(np.dot(v_a, v_b))
        cos_angle = dot / max(norm_a * norm_b, 1e-15)
        angle_deg = float(np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0))))
        a_site_pairs.append({
            "ring_idx_a": a, "ring_idx_b": b,
            "V_DC_dot": dot,
            "V_DC_cos_angle": cos_angle,
            "V_DC_angle_deg": angle_deg,
        })

    # ── ∮V_DC·dl per-bond decomposition ──────────────────────────────────────
    per_bond_contribution = []
    loop_V_DC_total = 0.0
    for bnd in bonds:
        ix, iy, iz = bnd["a_site"]
        port = bnd["port"]
        a_to_b = np.array(bnd["a_to_b_offset"], dtype=float)
        a_to_b /= np.linalg.norm(a_to_b)
        traversal = np.array(bnd["traversal_direction"], dtype=float)
        sign = float(np.sign(np.dot(a_to_b, traversal)))
        contrib = sign * V_DC_per_port[ix, iy, iz, port]
        loop_V_DC_total += contrib
        per_bond_contribution.append({
            "ring_idx": bnd["ring_idx"],
            "a_site": list(bnd["a_site"]),
            "port": port,
            "traversal_sign": sign,
            "V_DC_along_port": float(V_DC_per_port[ix, iy, iz, port]),
            "contribution": float(contrib),
        })

    # Reverse-traversal sanity check (should give -loop_V_DC_total)
    loop_V_DC_reverse = -loop_V_DC_total

    # ── Magnitude pattern check (auditor q5) ─────────────────────────────────
    mag_pattern = [a_site_data[i]["V_DC_magnitude_vec"] for i in a_site_ring_idxs]
    mag_pattern_4port = [a_site_data[i]["V_DC_magnitude_4port_rms"] for i in a_site_ring_idxs]

    # 2-fold symmetry: under helical IC, sites at ring positions 0 and 4 should be related
    # by reflection through the helical axis. If 2-fold sym holds: |V_DC|_0 == |V_DC|_4 and
    # both differ from |V_DC|_2.
    sym_score_0_vs_4 = abs(mag_pattern[0] - mag_pattern[2]) / max(mag_pattern[0], 1e-15)
    sym_score_2_unique = abs(mag_pattern[1] - mag_pattern[0]) / max(mag_pattern[0], 1e-15)

    # ── Print summary ────────────────────────────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  V_DC spatial characterization at A-sites")
    print("=" * 78, flush=True)
    for ring_idx in a_site_ring_idxs:
        d = a_site_data[ring_idx]
        print(f"\n  Ring node {ring_idx} @ {d['node_position']}")
        print(f"    V_DC per port: {[f'{x:+.4e}' for x in d['V_DC_per_port']]}")
        print(f"    V_DC vector (lattice):  ({d['V_DC_vector_lattice'][0]:+.4e}, "
              f"{d['V_DC_vector_lattice'][1]:+.4e}, {d['V_DC_vector_lattice'][2]:+.4e})")
        print(f"    |V_DC| (vec / 4port-rms): {d['V_DC_magnitude_vec']:.4e} / "
              f"{d['V_DC_magnitude_4port_rms']:.4e}")
        print(f"    V_DC in Frenet (T, R, B): "
              f"({d['V_DC_in_Frenet']['tangent']:+.4e}, "
              f"{d['V_DC_in_Frenet']['radial']:+.4e}, "
              f"{d['V_DC_in_Frenet']['binormal']:+.4e})")
        print(f"    Bond-port index: {d['bond_port_index']}, "
              f"V_DC along bond: {d['V_DC_along_bond']:+.4e}")

    print()
    print("  Adjacent A-site V_DC correlations:")
    for pair in a_site_pairs:
        print(f"    A_{pair['ring_idx_a']} ↔ A_{pair['ring_idx_b']}: "
              f"dot={pair['V_DC_dot']:+.4e}, "
              f"cos={pair['V_DC_cos_angle']:+.4f}, "
              f"angle={pair['V_DC_angle_deg']:.1f}°")

    print()
    print("  ∮V_DC·dl per-bond decomposition:")
    for c in per_bond_contribution:
        print(f"    bond {c['ring_idx']}: a_site={c['a_site']}, port={c['port']}, "
              f"sign={c['traversal_sign']:+.0f}, V_DC[port]={c['V_DC_along_port']:+.4e}, "
              f"contrib={c['contribution']:+.4e}")
    print(f"  Σ ∮V_DC·dl forward:  {loop_V_DC_total:+.4e}")
    print(f"  Σ ∮V_DC·dl reverse:  {loop_V_DC_reverse:+.4e}  (should be -forward)")
    print(f"  2/π reference:       {2/np.pi:.4f}")
    print(f"  Match to 2/π:        {abs(loop_V_DC_total - 2/np.pi) / (2/np.pi) * 100:.2f}% off")

    print()
    print("  Magnitude pattern check:")
    print(f"    |V_DC|_vec at A-sites: {[f'{x:.4e}' for x in mag_pattern]}")
    print(f"    A_0 vs A_4 deviation:  {sym_score_0_vs_4:.4f}  (small ⇒ 2-fold sym)")
    print(f"    A_2 vs A_0 deviation:  {sym_score_2_unique:.4f}  (large ⇒ A_2 unique)")

    out = {
        "test": "v8 V_DC spatial characterization @ T=0",
        "elapsed_recording_seconds": elapsed,
        "n_steps": N_STEPS,
        "engine_DT": v8.DT,
        "centroid": centroid.tolist(),
        "a_site_data": a_site_data,
        "a_site_pairs": a_site_pairs,
        "per_bond_contribution": per_bond_contribution,
        "loop_V_DC_forward": loop_V_DC_total,
        "loop_V_DC_reverse": loop_V_DC_reverse,
        "two_over_pi_reference": float(2 / np.pi),
        "match_to_2_over_pi_pct": float(abs(loop_V_DC_total - 2/np.pi) / (2/np.pi) * 100),
        "mag_pattern_vec": mag_pattern,
        "mag_pattern_4port_rms": mag_pattern_4port,
        "sym_score_0_vs_4": sym_score_0_vs_4,
        "sym_score_2_unique": sym_score_2_unique,
    }
    out_path = Path(__file__).parent / "r10_v8_v_dc_characterization_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
