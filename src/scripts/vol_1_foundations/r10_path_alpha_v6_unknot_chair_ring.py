"""r10_path_alpha_v6_unknot_chair_ring.py — Round 10+ Phase 1 Direction 3'.2.

Pre-reg P_phase11_path_alpha_v6_unknot_chair_ring_IC. Tests the corpus-canonical
trapped-CP-photon electron at bond-pair scale: 6-node hexagonal chair-ring on
K4 diamond, one full Compton wavelength circumference, CP photon amplitude
distributed with 60° polarization advance per node, A² → 1 saturation at ring
nodes (V_snap subatomic-scale per Vol 4 Ch 1:711).

Manuscript-canonical framing (NOT (2,3) phase-space winding which is research-tier):
- electron = unknot 0_1 Beltrami standing wave (Vol 1 Ch 1:18, Vol 1 Ch 3:402,
  backmatter/05:302)
- trapped CP photon at one full Compton wavelength on chiral K4 substrate
- Möbius half-twist substrate-inherited from K4 chirality (distributed)
- single intrinsic chirality globally (lattice-genesis); spin up/down is
  measurement-frame selection bias, NOT intrinsic
- charge sign = loop-traversal direction (Ax 2 TKI winding); CCW chosen here
- c_eff → 0 at saturation per canonical eq_axiom_4 (Confinement Bubble Γ=-1
  mechanism); canonical contradicts Vol 1 Ch 4:64-67 ε-only formula

Adjudication criteria (all 4 required for Mode I):
1. Persistence: A² ≥ 0.5 maintained at all 6 ring nodes for ≥100 Compton
   periods
2. Beltrami parallelism: |cos_sim(A_vec, B_vec)| ≥ 0.8 mean over steady-state
   window (after 25% transient)
3. Centroid flux: |∫ω·dA over ring centroid plane| RMS < 5% of local |ω|
4. Topological localization: ring-node energy fraction ≥ 50% of total active
   energy at steady state (trapped state stays at the 6 ring nodes, not
   dissolved into bulk)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


# ─── Constants ─────────────────────────────────────────────────────────────

N_LATTICE = 32
PML = 4
CENTER = (16, 16, 16)

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

RECORDING_END_P = 200.0
N_RECORDING_STEPS = int(RECORDING_END_P * COMPTON_PERIOD / DT)

# K4 port offsets (A's perspective; B's port-i offset = -A's port-i)
PORT_OFFSETS_A = [
    np.array([1, 1, 1]),    # port 0
    np.array([1, -1, -1]),  # port 1
    np.array([-1, 1, -1]),  # port 2
    np.array([-1, -1, 1]),  # port 3
]
SQRT_3 = np.sqrt(3.0)

# IC amplitudes (V_SNAP units; engine V_SNAP=1 in natural units)
# Drive A² = V²/V_SNAP² ≈ 1 at ring nodes (saturation onset / Confinement Bubble)
V_AMP_SATURATION = 0.95
PHI_AMP = V_AMP_SATURATION   # 90° quadrature, equal magnitude (Virial split)
OMEGA_AMP = V_AMP_SATURATION # B-field magnitude matches E-field for CP photon

# Adjudication thresholds
SATURATION_PERSISTENCE_PERIODS = 100.0
SATURATION_A2_THRESHOLD = 0.5
BELTRAMI_PARALLELISM_THRESHOLD = 0.8
CENTROID_FLUX_REL_THRESHOLD = 0.05
RING_LOCALIZATION_THRESHOLD = 0.5

REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_JSON = Path(__file__).parent / "r10_path_alpha_v6_unknot_chair_ring_results.json"


def build_chair_ring(center):
    """Construct 6-node hexagonal chair-ring + 6 bonds at lattice center.

    Doc 83 traversal translated to lattice center (16,16,16). Returns
      nodes: list of 6 (i,j,k) ring positions, alternating A (even) and B (odd)
      bonds: list of 6 dicts per bond (a_site, b_site, port at A, traversal direction)
    """
    cx, cy, cz = center
    nodes = [
        (cx, cy, cz),               # n=0  A (all even)
        (cx + 1, cy + 1, cz + 1),   # n=1  B
        (cx, cy + 2, cz + 2),       # n=2  A
        (cx - 1, cy + 3, cz + 1),   # n=3  B
        (cx - 2, cy + 2, cz),       # n=4  A
        (cx - 1, cy + 1, cz - 1),   # n=5  B
    ]

    bonds = []
    for n in range(6):
        node_curr = nodes[n]
        node_next = nodes[(n + 1) % 6]

        # Identify A-site (all even) vs B-site (all odd)
        curr_is_a = all(c % 2 == 0 for c in node_curr)
        if curr_is_a:
            a_site, b_site = node_curr, node_next
        else:
            a_site, b_site = node_next, node_curr

        offset = np.array(b_site) - np.array(a_site)

        port_idx = None
        for p_idx, p_offset in enumerate(PORT_OFFSETS_A):
            if np.array_equal(offset, p_offset):
                port_idx = p_idx
                break
        if port_idx is None:
            raise RuntimeError(f"No A-port matches offset {offset.tolist()}")

        traversal_dir = (np.array(node_next) - np.array(node_curr)).astype(float)
        traversal_dir /= np.linalg.norm(traversal_dir)

        bonds.append({
            "ring_idx": n,
            "node_curr": list(node_curr),
            "node_next": list(node_next),
            "a_site": list(a_site),
            "b_site": list(b_site),
            "port": port_idx,
            "a_to_b_offset": offset.tolist(),
            "traversal_direction": traversal_dir.tolist(),
        })
    return nodes, bonds


def ring_frame_at_node(nodes, n_idx, centroid):
    """Frenet-like frame at ring node n: tangent, radial-perp, binormal.

    Tangent = direction along loop (next - prev). Radial = centroid-to-node
    projected perpendicular to tangent. Binormal = tangent × radial. The
    (radial, binormal) pair spans the local poloidal plane.
    """
    next_node = np.array(nodes[(n_idx + 1) % 6])
    prev_node = np.array(nodes[(n_idx - 1) % 6])
    tangent = (next_node - prev_node).astype(float)
    tangent /= np.linalg.norm(tangent)

    radial = centroid - np.array(nodes[n_idx])
    radial = radial - np.dot(radial, tangent) * tangent
    radial_norm = np.linalg.norm(radial)
    if radial_norm < 1e-10:
        # Degenerate: pick arbitrary perpendicular
        candidate = np.cross(tangent, [1.0, 0.0, 0.0])
        if np.linalg.norm(candidate) < 1e-10:
            candidate = np.cross(tangent, [0.0, 1.0, 0.0])
        radial = candidate / np.linalg.norm(candidate)
    else:
        radial /= radial_norm

    binormal = np.cross(tangent, radial)
    binormal /= max(np.linalg.norm(binormal), 1e-12)

    return tangent, radial, binormal


def initialize_chair_ring_ic(engine, nodes, bonds, v_amp, phi_amp, omega_amp):
    """Set fields at the 6 ring nodes + bonds; zero elsewhere.

    Per the trapped-photon picture:
    - V_inc at each bond's A-site, on the bond's port: cos(2π·n/6) for n=0..5
      (one full polarization cycle distributed over 6 bonds = one toroidal
      traversal of the closed loop)
    - Phi_link 90° quadrature (sin(2π·n/6)) — LC tank standing-wave
    - Cosserat ω at ring nodes in local poloidal plane (radial × binormal),
      orientation phase-advanced 60° per node
    """
    engine.k4.V_inc.fill(0.0)
    engine.k4.V_ref.fill(0.0)
    engine.k4.Phi_link.fill(0.0)
    engine.k4.S_field.fill(1.0)
    engine.cos.u.fill(0.0)
    engine.cos.omega.fill(0.0)
    engine.cos.u_dot.fill(0.0)
    engine.cos.omega_dot.fill(0.0)

    centroid = np.mean([np.array(n) for n in nodes], axis=0)

    # V_inc at BOTH endpoints of each bond + Phi_link at A-site only
    # (Phi_link is stored at A-sites per k4_tlm.py:158-167; V_inc is local
    # to each node and represents incident wave from its side of the bond)
    for bond_idx, bond in enumerate(bonds):
        phase = 2.0 * np.pi * bond_idx / 6.0
        v_value = v_amp * np.cos(phase)
        phi_value = phi_amp * np.sin(phase)

        # V_inc at A-site, on A's port toward B
        ix_a, iy_a, iz_a = bond["a_site"]
        port_a = bond["port"]
        engine.k4.V_inc[ix_a, iy_a, iz_a, port_a] = v_value

        # V_inc at B-site, on B's port toward A (B's port-i has offset = -A's port-i)
        # B's port index is the same number as A's port (port-i↔port-i convention)
        ix_b, iy_b, iz_b = bond["b_site"]
        engine.k4.V_inc[ix_b, iy_b, iz_b, port_a] = v_value

        # Phi_link at A-site only (canonical storage convention)
        engine.k4.Phi_link[ix_a, iy_a, iz_a, port_a] = phi_value

    # Cosserat ω at each ring node: local poloidal plane, phase advance 60°·n
    # Rotation handedness CCW around the ring axis (RH photon polarization
    # matched to K4 substrate chirality)
    for n_idx, node in enumerate(nodes):
        _, radial, binormal = ring_frame_at_node(nodes, n_idx, centroid)
        phase = 2.0 * np.pi * n_idx / 6.0
        omega_vec = omega_amp * (np.cos(phase) * radial + np.sin(phase) * binormal)
        ix, iy, iz = node
        engine.cos.omega[ix, iy, iz, :] = omega_vec


def measure_ring_state(engine, nodes, plane_normal):
    """Measure A², Beltrami parallelism, centroid flux, ring localization."""
    V_SNAP = engine.V_SNAP

    # A² at each ring node
    A2_per_node = []
    for node in nodes:
        ix, iy, iz = node
        V_sq = float(np.sum(engine.k4.V_inc[ix, iy, iz, :] ** 2))
        A2_per_node.append(V_sq / (V_SNAP ** 2))

    # Beltrami: cos_sim(A_vec, B_vec) at each ring node
    # A_vec ≈ Σ V_inc[port] · port_direction (4-port → 3D vector)
    # B_vec ≈ Cosserat ω (Vol 1 Ch 4:21-26: rotational/inductive DOF)
    cos_sim_per_node = []
    for node in nodes:
        ix, iy, iz = node
        is_a = all(c % 2 == 0 for c in node)
        port_dirs = (
            [p / SQRT_3 for p in PORT_OFFSETS_A] if is_a
            else [-p / SQRT_3 for p in PORT_OFFSETS_A]
        )
        a_vec = np.zeros(3)
        for p_idx in range(4):
            a_vec += float(engine.k4.V_inc[ix, iy, iz, p_idx]) * port_dirs[p_idx]
        b_vec = np.array(engine.cos.omega[ix, iy, iz, :], dtype=float)
        a_norm = np.linalg.norm(a_vec)
        b_norm = np.linalg.norm(b_vec)
        if a_norm < 1e-12 or b_norm < 1e-12:
            cos_sim_per_node.append(0.0)
        else:
            cos_sim_per_node.append(float(np.dot(a_vec, b_vec) / (a_norm * b_norm)))

    # Centroid flux: sum of ω · plane_normal at ring nodes
    flux_total = 0.0
    omega_mag_total = 0.0
    for node in nodes:
        ix, iy, iz = node
        omega_at = np.array(engine.cos.omega[ix, iy, iz, :], dtype=float)
        flux_total += float(np.dot(omega_at, plane_normal))
        omega_mag_total += float(np.linalg.norm(omega_at))
    flux_relative = (
        abs(flux_total) / max(omega_mag_total / 6.0, 1e-12)
    )

    # Ring-node energy localization
    ring_energy = 0.0
    for node in nodes:
        ix, iy, iz = node
        V_sq = float(np.sum(engine.k4.V_inc[ix, iy, iz, :] ** 2))
        omega_sq = float(np.sum(engine.cos.omega[ix, iy, iz, :] ** 2))
        ring_energy += V_sq + omega_sq

    # Total active energy (excluding PML)
    pml = PML
    nx = engine.k4.nx
    interior_slice = (
        slice(pml, nx - pml),
        slice(pml, nx - pml),
        slice(pml, nx - pml),
    )
    V_sq_interior = float(np.sum(
        np.asarray(engine.k4.V_inc[interior_slice + (slice(None),)]) ** 2
    ))
    omega_sq_interior = float(np.sum(
        np.asarray(engine.cos.omega[interior_slice + (slice(None),)]) ** 2
    ))
    total_energy = V_sq_interior + omega_sq_interior

    ring_localization = ring_energy / max(total_energy, 1e-30)

    return {
        "A2_per_node": A2_per_node,
        "A2_min": float(min(A2_per_node)),
        "A2_mean": float(np.mean(A2_per_node)),
        "cos_sim_per_node": cos_sim_per_node,
        "cos_sim_mean": float(np.mean(cos_sim_per_node)),
        "centroid_flux_total": flux_total,
        "centroid_flux_relative": flux_relative,
        "ring_energy": ring_energy,
        "total_energy": total_energy,
        "ring_localization": ring_localization,
    }


def main():
    print("=" * 78, flush=True)
    print("  r10 path α v6 — trapped-photon unknot chair-ring IC")
    print("  P_phase11_path_alpha_v6_unknot_chair_ring_IC")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, PML={PML}, center={CENTER}")
    print(f"  Recording window: {RECORDING_END_P} Compton periods")
    print(f"  IC amplitudes: V={V_AMP_SATURATION}, Φ={PHI_AMP}, ω={OMEGA_AMP}")
    print()

    nodes, bonds = build_chair_ring(CENTER)
    centroid = np.mean([np.array(n) for n in nodes], axis=0)

    # Approx ring-plane normal for centroid flux measurement
    # Chair-ring is non-planar; use cross product of two centroid-to-node vectors
    v0 = np.array(nodes[0]) - centroid
    v2 = np.array(nodes[2]) - centroid
    plane_normal = np.cross(v0, v2)
    plane_normal /= max(np.linalg.norm(plane_normal), 1e-12)

    print(f"Chair-ring centroid: {centroid.tolist()}")
    print(f"Approx ring-plane normal: {plane_normal.tolist()}")
    print()
    print("Ring nodes:")
    for n_idx, node in enumerate(nodes):
        sublattice = "A" if all(c % 2 == 0 for c in node) else "B"
        print(f"  n={n_idx} ({sublattice}): {node}")
    print()
    print("Bonds (A-site, port, b̂_traversal):")
    for b_idx, bond in enumerate(bonds):
        print(f"  bond {b_idx}: A{tuple(bond['a_site'])} port {bond['port']}, "
              f"b̂_traversal={[f'{x:+.3f}' for x in bond['traversal_direction']]}")
    print()

    print("Engine setup...", flush=True)
    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )
    print(f"  V_SNAP = {engine.V_SNAP}")
    print()

    print("IC initialization at chair-ring nodes...", flush=True)
    initialize_chair_ring_ic(
        engine, nodes, bonds, V_AMP_SATURATION, PHI_AMP, OMEGA_AMP
    )

    initial_state = measure_ring_state(engine, nodes, plane_normal)
    print(f"  A² at ring nodes (t=0):  min={initial_state['A2_min']:.4f}, "
          f"mean={initial_state['A2_mean']:.4f}")
    print(f"  Beltrami cos_sim (t=0):  mean={initial_state['cos_sim_mean']:+.4f}")
    print(f"  Centroid flux rel (t=0): {initial_state['centroid_flux_relative']:.4e}")
    print(f"  Ring localization (t=0): {initial_state['ring_localization']:.4f}")
    print()

    print(f"Recording {N_RECORDING_STEPS} steps ({RECORDING_END_P} P)...", flush=True)
    A2_min_traj = np.zeros(N_RECORDING_STEPS)
    A2_mean_traj = np.zeros(N_RECORDING_STEPS)
    cos_sim_traj = np.zeros(N_RECORDING_STEPS)
    flux_rel_traj = np.zeros(N_RECORDING_STEPS)
    ring_loc_traj = np.zeros(N_RECORDING_STEPS)
    persistence_period = 0.0
    saturation_lost = False

    t0 = time.time()
    last = t0
    for i in range(N_RECORDING_STEPS):
        engine.step()
        s = measure_ring_state(engine, nodes, plane_normal)
        A2_min_traj[i] = s["A2_min"]
        A2_mean_traj[i] = s["A2_mean"]
        cos_sim_traj[i] = s["cos_sim_mean"]
        flux_rel_traj[i] = s["centroid_flux_relative"]
        ring_loc_traj[i] = s["ring_localization"]

        t_p = (i + 1) * DT / COMPTON_PERIOD
        if not saturation_lost:
            if s["A2_min"] >= SATURATION_A2_THRESHOLD:
                persistence_period = t_p
            else:
                saturation_lost = True

        if (time.time() - last) > 30.0:
            print(f"    [progress] step {i}/{N_RECORDING_STEPS}, t={t_p:.1f}P, "
                  f"A²_min={s['A2_min']:.3f}, cos_sim={s['cos_sim_mean']:+.3f}, "
                  f"loc={s['ring_localization']:.3f}, "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s", flush=True)
    print()

    # Steady-state window: skip first 25% for transients
    sw_start = N_RECORDING_STEPS // 4

    cos_sim_steady = float(np.mean(np.abs(cos_sim_traj[sw_start:])))
    flux_rel_steady = float(np.mean(flux_rel_traj[sw_start:]))
    A2_mean_steady = float(np.mean(A2_mean_traj[sw_start:]))
    ring_loc_steady = float(np.mean(ring_loc_traj[sw_start:]))

    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    print(f"  Persistence: A²_min ≥ {SATURATION_A2_THRESHOLD} maintained for "
          f"{persistence_period:.1f} P  (threshold ≥ "
          f"{SATURATION_PERSISTENCE_PERIODS} P)")
    print(f"  Beltrami |cos_sim| steady-state: {cos_sim_steady:.4f}  "
          f"(threshold ≥ {BELTRAMI_PARALLELISM_THRESHOLD})")
    print(f"  Centroid flux (rel) steady-state: {flux_rel_steady:.4e}  "
          f"(threshold < {CENTROID_FLUX_REL_THRESHOLD})")
    print(f"  Ring localization steady-state: {ring_loc_steady:.4f}  "
          f"(threshold ≥ {RING_LOCALIZATION_THRESHOLD})")
    print(f"  A²_mean steady-state: {A2_mean_steady:.4f}")
    print()

    persistence_pass = persistence_period >= SATURATION_PERSISTENCE_PERIODS
    beltrami_pass = cos_sim_steady >= BELTRAMI_PARALLELISM_THRESHOLD
    flux_pass = flux_rel_steady < CENTROID_FLUX_REL_THRESHOLD
    loc_pass = ring_loc_steady >= RING_LOCALIZATION_THRESHOLD

    n_pass = sum([persistence_pass, beltrami_pass, flux_pass, loc_pass])

    if n_pass == 4:
        mode = "I"
        verdict = (
            f"Mode I: trapped-photon unknot at bond-pair scale empirically confirmed. "
            f"Persistence {persistence_period:.1f}P, Beltrami {cos_sim_steady:.3f}, "
            f"flux_rel {flux_rel_steady:.3e}, loc {ring_loc_steady:.3f} — "
            f"all 4 criteria PASS."
        )
    elif n_pass >= 2:
        mode = "II"
        verdict = (
            f"Mode II partial: {n_pass}/4 criteria pass. "
            f"Persistence={'P' if persistence_pass else 'F'} ({persistence_period:.1f}P), "
            f"Beltrami={'P' if beltrami_pass else 'F'} ({cos_sim_steady:.3f}), "
            f"flux={'P' if flux_pass else 'F'} ({flux_rel_steady:.3e}), "
            f"loc={'P' if loc_pass else 'F'} ({ring_loc_steady:.3f})."
        )
    else:
        mode = "III"
        verdict = (
            f"Mode III: bond-pair-scale trapped-photon unknot fails. "
            f"{n_pass}/4 criteria pass. "
            f"Persistence={persistence_period:.1f}P, Beltrami={cos_sim_steady:.3f}, "
            f"flux_rel={flux_rel_steady:.3e}, loc={ring_loc_steady:.3f}. "
            f"Either IC framing wrong, or engine doesn't host this configuration."
        )

    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase11_path_alpha_v6_unknot_chair_ring_IC",
        "test": "trapped-photon unknot bond-pair-scale chair-ring IC",
        "lattice": {"N": N_LATTICE, "pml": PML, "center": list(CENTER)},
        "recording_periods": RECORDING_END_P,
        "n_recording_steps": N_RECORDING_STEPS,
        "elapsed_seconds": elapsed,
        "ring_nodes": [list(n) for n in nodes],
        "ring_centroid": centroid.tolist(),
        "ring_plane_normal": plane_normal.tolist(),
        "ring_bonds": bonds,
        "ic_amplitudes": {
            "v_amp_saturation": V_AMP_SATURATION,
            "phi_amp": PHI_AMP,
            "omega_amp": OMEGA_AMP,
        },
        "thresholds": {
            "saturation_persistence_periods": SATURATION_PERSISTENCE_PERIODS,
            "saturation_a2": SATURATION_A2_THRESHOLD,
            "beltrami_parallelism": BELTRAMI_PARALLELISM_THRESHOLD,
            "centroid_flux_relative": CENTROID_FLUX_REL_THRESHOLD,
            "ring_localization": RING_LOCALIZATION_THRESHOLD,
        },
        "results": {
            "persistence_period_P": persistence_period,
            "beltrami_cos_sim_steady_abs_mean": cos_sim_steady,
            "centroid_flux_rel_steady_mean": flux_rel_steady,
            "ring_localization_steady_mean": ring_loc_steady,
            "A2_mean_steady": A2_mean_steady,
            "A2_min_first10": A2_min_traj[:10].tolist(),
            "A2_min_last10": A2_min_traj[-10:].tolist(),
            "A2_min_overall_min": float(np.min(A2_min_traj)),
            "A2_min_overall_max": float(np.max(A2_min_traj)),
        },
        "initial_state": initial_state,
        "criteria_pass": {
            "persistence": bool(persistence_pass),
            "beltrami": bool(beltrami_pass),
            "centroid_flux": bool(flux_pass),
            "ring_localization": bool(loc_pass),
            "n_pass": int(n_pass),
        },
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
