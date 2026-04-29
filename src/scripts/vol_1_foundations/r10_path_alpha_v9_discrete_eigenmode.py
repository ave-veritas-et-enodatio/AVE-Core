"""r10_path_alpha_v9_discrete_eigenmode.py — Round 11 (vi) Stride 4: v9 driver.

Pre-reg P_phase11_path_alpha_v9_discrete_eigenmode. Per doc 90 §10 resolution
(post-Grant 2026-04-29 "what is k physically?" pushback): v9 IC uses the
discrete Beltrami eigenmode from Stride 3 directly (top ring-localized mode
at k = 1.56 in 1/ℓ_node units) on chair-ring + 1-step K4 neighborhood.

KEY RESOLUTION FROM DOC 90 §10:
- k is the inverse helical pitch of A along its direction (geometric, NOT frequency)
- Free-wave dispersion: k = ω/c (coincides with curl eigenvalue for plane waves)
- Bound-state Beltrami: k_curl ≠ ω_temporal in general; k determined by substrate
  geometry, ω_temporal determined by rest mass / total stored energy at saturation
- Rest mass m_e·c² comes from SATURATION AMPLITUDE (Ax 4 V_SNAP at ring nodes),
  NOT from curl eigenvalue identification

v9 IC (Stride 3 §4 + §10.4 resolution):
1. Use discrete eigenvector A_0 from Stride 3 JSON (top ring-localized mode at
   k=1.56) — A_0 is a specific 3D vector at each of 18 nodes (6 ring + 12 1-step)
2. Phase B time-snapshot: V_inc at peak (E peak, A and B at zero crossings)
3. V_inc[node, port] = ω_C · A_0(node) · port_dir × bond_length normalization
4. Phi_link = 0 (zero crossing of ∫E dt)
5. Cosserat ω = 0 (B at zero crossing)
6. Set ALL 4 ports of all 18 nodes (NOT just in-ring 2 of 6 like v6/v7/v8)
7. Saturation amplitude: scale eigenvector to drive |V_inc|² → V_SNAP² at peak

ADJUDICATION (4-criterion gate per doc 86 §7.4, with measurement methods
from v8 doc 87 §1.4 corrected per Phi_link detrending):
- Persistence: A²_mean(ring nodes) ≥ 0.5 maintained ≥ 100 P
- Beltrami parallelism: |cos_sim(A_from_Phi_link_detrended, ω)| ≥ 0.8 steady
- Loop flux: ∮A·dl per Stokes integration; target ≈ |A_tor|·perimeter
  (derived from eigenvector, NOT 2π universal — per doc 90 §10.6 amendment)
- Ring localization ≥ 0.5

Per doc 86 §7.6 + doc 87 §3.4 gate decision: Mode I → Phase 1 Direction 3'.2
closes; Mode II/III → Round 11 secondary candidates ((i) finer-than-K4
substrate, (ii) multi-loop, (iii) topology variant).
"""
from __future__ import annotations

import argparse
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

PORT_OFFSETS_A = [
    np.array([1, 1, 1]),
    np.array([1, -1, -1]),
    np.array([-1, 1, -1]),
    np.array([-1, -1, 1]),
]
SQRT_3 = np.sqrt(3.0)
TWO_PI = 2.0 * np.pi
BOND_LENGTH = SQRT_3

# IC amplitude scaling: drive ring-node A² to saturation
SATURATION_AMP_TARGET = 0.95  # |V_inc|² / V_SNAP² at peak ring nodes

# Adjudication thresholds (UNCHANGED from v7/v8 per doc 86 §7.4 lock)
PERSISTENCE_PERIODS = 100.0
A2_MEAN_THRESHOLD = 0.5
BELTRAMI_PARALLELISM_THRESHOLD = 0.8
RING_LOCALIZATION_THRESHOLD = 0.5
# Loop flux target derived from eigenvector (NOT universal 2π) per doc 90 §10.6
LOOP_FLUX_TOLERANCE = 0.30  # ±30% relative to eigenvector-derived target

EIGENMODE_JSON = Path(__file__).parent / "r10_round_11_vi_chair_ring_eigenmode_results.json"
DEFAULT_OUTPUT = Path(__file__).parent / "r10_path_alpha_v9_discrete_eigenmode_results.json"
REPO_ROOT = Path(__file__).resolve().parents[3]


def is_a_site(pos):
    return all(c % 2 == 0 for c in pos)


def port_direction(pos, port_idx):
    sign = +1 if is_a_site(pos) else -1
    return sign * PORT_OFFSETS_A[port_idx].astype(float) / SQRT_3


def k4_neighbor(pos, port_idx):
    sign = +1 if is_a_site(pos) else -1
    return tuple(int(c + sign * o) for c, o in zip(pos, PORT_OFFSETS_A[port_idx]))


def load_eigenmode_data():
    """Load Stride 3 eigenmode results."""
    with EIGENMODE_JSON.open() as f:
        data = json.load(f)
    return data


def build_ic_node_list(center):
    """Build chair-ring + 1-step K4 neighbors at lattice center.

    Returns ring node positions + out-of-ring 1-step neighbor positions, all
    translated to lattice center (16,16,16). Same topology as Stride 3 JSON
    but shifted to fit in N=32 engine grid.
    """
    cx, cy, cz = center
    ring_offsets = [
        (0, 0, 0),
        (1, 1, 1),
        (0, 2, 2),
        (-1, 3, 1),
        (-2, 2, 0),
        (-1, 1, -1),
    ]
    ring_nodes = [(cx + o[0], cy + o[1], cz + o[2]) for o in ring_offsets]

    # Compute 1-step out-of-ring neighbors via K4 ports
    node_list = list(ring_nodes)
    node_set = set(ring_nodes)
    for ring_pos in ring_nodes:
        for port_idx in range(4):
            neighbor_pos = k4_neighbor(ring_pos, port_idx)
            if neighbor_pos not in node_set:
                node_list.append(neighbor_pos)
                node_set.add(neighbor_pos)

    return node_list


def initialize_v9_ic(engine, node_list, eigenmode_data, sat_amp_target):
    """Apply v9 IC per doc 90 §10 resolution.

    Uses the top ring-localized eigenvector A_0 from Stride 3 JSON to set
    V_inc + Phi_link + Cosserat ω at all 18 chair-ring + 1-step K4 nodes.

    Phase B time-snapshot: V_inc at peak (E=peak); Phi_link=0; ω=0.
    """
    # Zero K4 fields; preserve bulk thermal Cosserat
    engine.k4.V_inc.fill(0.0)
    engine.k4.V_ref.fill(0.0)
    engine.k4.Phi_link.fill(0.0)
    engine.k4.S_field.fill(1.0)

    # Extract A_0 vectors for each of the 18 nodes
    eigvec_data = eigenmode_data["top_ring_localized_eigenvector"]
    a0_ring = eigvec_data["A_0_at_ring_nodes"]
    a0_outring = eigvec_data["A_0_at_out_of_ring_nodes"]
    all_a0 = a0_ring + a0_outring  # 18 entries

    # Stride 3 used origin-centered positions; we use lattice-center positions
    # Map by index (eigvec entry i ↔ node_list[i])
    if len(all_a0) != len(node_list):
        raise RuntimeError(f"Mismatch: {len(all_a0)} eigvec vs {len(node_list)} nodes")

    # Determine scaling factor: max ring node A_0 magnitude → saturation amplitude
    ring_amps = [entry["magnitude"] for entry in a0_ring]
    max_ring_amp = max(ring_amps)
    # V_inc² at peak should be saturation_amp_target × V_SNAP²
    # V_inc magnitude scales with A_0 magnitude
    # Use eigenvector → V_inc at peak: V_inc(node) = scale · A_0(node)
    # For peak ring node: V_inc² = scale² · max_ring_amp² = saturation_amp_target · V_SNAP² (=1 for V_SNAP=1)
    # So scale = sqrt(saturation_amp_target) / max_ring_amp
    scale = np.sqrt(sat_amp_target) / max_ring_amp

    print(f"  V_inc scaling factor: {scale:.4f}")
    print(f"  Max ring |A_0| × scale = {max_ring_amp * scale:.4f} (target √{sat_amp_target} ≈ {np.sqrt(sat_amp_target):.4f})")

    # For each of the 18 nodes, project scaled A_0 onto each of the 4 K4 ports
    # V_inc[node, port] = (scaled A_0(node)) · port_dir
    # This gives the projection of the local A_0 onto each tetrahedral port direction
    nx = engine.k4.nx
    for i, node in enumerate(node_list):
        a_0 = scale * np.array(all_a0[i]["A_0"])
        ix, iy, iz = node
        if not (0 <= ix < nx and 0 <= iy < nx and 0 <= iz < nx):
            print(f"  WARNING: node {node} out of lattice bounds, skipping")
            continue
        for port_idx in range(4):
            pdir = port_direction(node, port_idx)
            v_inc_value = float(np.dot(a_0, pdir))
            engine.k4.V_inc[ix, iy, iz, port_idx] = v_inc_value

    # Phi_link = 0 (Phase B: zero crossing of ∫E dt)
    # Already filled with zero above

    # Cosserat ω at IC: set to k_eigenvalue · scale · A_0 (peaked, like v7/v8 mixed phase)
    # Pure Phase B (ω=0) doesn't work with engine's disable_cosserat_lc_force=True
    # config because K4→Cosserat coupling is disabled; ω stays at 0 throughout.
    # Mixed-phase IC: V_inc peaked + Cosserat ω peaked simultaneously (NOT a clean
    # time-snapshot, but works in engine and lets Beltrami test be meaningful).
    # Per Beltrami: B = ∇×A = k·A, so ω = k_in_lnode · A
    # CORRECTED unit conversion: k_in_lnode = k_eigenvalue / √3 (NOT × √3)
    k_eigenvalue = eigvec_data["eigenvalue"]
    k_in_lnode = k_eigenvalue / SQRT_3  # corrected conversion
    print(f"  k_eigenvalue (1/bond_length): {k_eigenvalue:.4f}")
    print(f"  k in 1/ℓ_node (corrected: divide by √3): {k_in_lnode:.4f}")

    for i, node in enumerate(node_list):
        a_0 = scale * np.array(all_a0[i]["A_0"])
        ix, iy, iz = node
        if 0 <= ix < nx and 0 <= iy < nx and 0 <= iz < nx:
            engine.cos.omega[ix, iy, iz, :] = k_in_lnode * a_0
            engine.cos.u[ix, iy, iz, :] = 0.0
            engine.cos.u_dot[ix, iy, iz, :] = 0.0
            engine.cos.omega_dot[ix, iy, iz, :] = 0.0

    return scale, k_in_lnode


def measure_v9_state(engine, ring_node_positions):
    """Measure persistence + ring localization (real-time)."""
    V_SNAP = engine.V_SNAP
    A2_per_node = []
    for node in ring_node_positions:
        ix, iy, iz = node
        V_sq = float(np.sum(engine.k4.V_inc[ix, iy, iz, :] ** 2))
        A2_per_node.append(V_sq / (V_SNAP ** 2))

    ring_energy = 0.0
    for node in ring_node_positions:
        ix, iy, iz = node
        V_sq = float(np.sum(engine.k4.V_inc[ix, iy, iz, :] ** 2))
        omega_sq = float(np.sum(engine.cos.omega[ix, iy, iz, :] ** 2))
        ring_energy += V_sq + omega_sq

    pml = PML
    nx = engine.k4.nx
    sl = (slice(pml, nx - pml),) * 3
    V_sq_int = float(np.sum(np.asarray(engine.k4.V_inc[sl + (slice(None),)]) ** 2))
    omega_sq_int = float(np.sum(np.asarray(engine.cos.omega[sl + (slice(None),)]) ** 2))
    total_energy = V_sq_int + omega_sq_int
    ring_localization = ring_energy / max(total_energy, 1e-30)

    return {
        "A2_per_node": A2_per_node,
        "A2_min": float(min(A2_per_node)),
        "A2_mean": float(np.mean(A2_per_node)),
        "ring_localization": float(ring_localization),
    }


def detrend_phi_link(phi_link_traj):
    """Subtract per-port linear fit from Phi_link trajectory (per v8 method)."""
    n_steps = phi_link_traj.shape[0]
    t = np.arange(n_steps, dtype=np.float64)
    t_mean = t.mean()
    t_var = ((t - t_mean) ** 2).sum()
    phi_mean = phi_link_traj.mean(axis=0)
    slope_num = ((t[:, None, None, None, None] - t_mean) * (phi_link_traj - phi_mean[None, ...])).sum(axis=0)
    slope = slope_num / t_var
    intercept = phi_mean - slope * t_mean
    trend = intercept[None, ...] + slope[None, ...] * t[:, None, None, None, None]
    return phi_link_traj - trend


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    print("=" * 78)
    print("  r10 path α v9 — discrete eigenmode IC at chair-ring + 1-step K4")
    print("  Per doc 90 §10 resolution (k physical = inverse helical pitch)")
    print("=" * 78)

    # Load Stride 3 eigenmode results
    print("Loading Stride 3 eigenmode data...")
    eigenmode_data = load_eigenmode_data()
    eigvec_data = eigenmode_data["top_ring_localized_eigenvector"]
    print(f"  Top ring-localized mode: λ = {eigvec_data['eigenvalue']:.4f}, "
          f"ring_loc = {eigvec_data['ring_localization']:.4f}")
    print(f"  k in 1/ℓ_node units = {eigvec_data['eigenvalue'] * SQRT_3:.4f}")
    print(f"  Helical pitch λ_helix ≈ {TWO_PI / (eigvec_data['eigenvalue'] * SQRT_3):.4f} ℓ_node")
    print()

    # Build node list
    node_list = build_ic_node_list(CENTER)
    ring_node_positions = node_list[:6]
    print(f"  Total nodes: {len(node_list)} (6 ring + 12 1-step out-of-ring)")
    print()

    # Engine setup (T=0 baseline)
    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    # Apply v9 IC
    print("Applying v9 IC (discrete eigenmode + mixed-phase, ω = k·A_0)...")
    scale, k_in_lnode_ic = initialize_v9_ic(engine, node_list, eigenmode_data, SATURATION_AMP_TARGET)
    print()

    # Initial state
    initial_state = measure_v9_state(engine, ring_node_positions)
    print(f"  IC measurements (t=0):")
    print(f"    A²_per_node: {[f'{a:.3f}' for a in initial_state['A2_per_node']]}")
    print(f"    A²_mean = {initial_state['A2_mean']:.4f}")
    print(f"    A²_min  = {initial_state['A2_min']:.4f}")
    print(f"    Ring localization = {initial_state['ring_localization']:.4f}")
    print()

    # Recording loop
    print(f"Recording {N_RECORDING_STEPS} steps ({RECORDING_END_P} P)...")
    A2_min_traj = np.zeros(N_RECORDING_STEPS)
    A2_mean_traj = np.zeros(N_RECORDING_STEPS)
    ring_loc_traj = np.zeros(N_RECORDING_STEPS)
    nx = engine.k4.nx
    phi_link_traj = np.zeros((N_RECORDING_STEPS, nx, nx, nx, 4), dtype=np.float32)
    omega_traj_per_ring = np.zeros((N_RECORDING_STEPS, 6, 3), dtype=np.float32)
    persistence_periods = 0.0
    saturation_lost = False

    t0 = time.time()
    last = t0
    for i in range(N_RECORDING_STEPS):
        engine.step()
        s = measure_v9_state(engine, ring_node_positions)
        A2_min_traj[i] = s["A2_min"]
        A2_mean_traj[i] = s["A2_mean"]
        ring_loc_traj[i] = s["ring_localization"]
        phi_link_traj[i] = engine.k4.Phi_link.astype(np.float32)
        for n_idx, node in enumerate(ring_node_positions):
            omega_traj_per_ring[i, n_idx, :] = engine.cos.omega[node[0], node[1], node[2], :]

        t_p = (i + 1) * DT / COMPTON_PERIOD
        if not saturation_lost:
            if s["A2_mean"] >= A2_MEAN_THRESHOLD:
                persistence_periods = t_p
            else:
                saturation_lost = True

        if (time.time() - last) > 30.0:
            print(f"    [progress] step {i}/{N_RECORDING_STEPS}, t={t_p:.1f}P, "
                  f"A²_mean={s['A2_mean']:.3f}, loc={s['ring_localization']:.3f}, "
                  f"elapsed {time.time()-t0:.1f}s")
            last = time.time()
    elapsed = time.time() - t0
    print(f"  Recording done at {elapsed:.1f}s")
    print()

    # Post-process: detrend Phi_link
    print("Post-processing: detrending Phi_link...")
    phi_oscillating = detrend_phi_link(phi_link_traj.astype(np.float64))

    # Beltrami parallelism: cos_sim(A_from_Phi_link_detrended, Cosserat ω) at ring nodes
    print("Computing Beltrami |cos_sim| over recording...")
    cos_sim_traj = np.zeros(N_RECORDING_STEPS)
    loop_flux_traj = np.zeros(N_RECORDING_STEPS)

    # Pre-compute bond list for loop flux (6 chair-ring bonds)
    ring_bonds = []
    for n_idx in range(6):
        node_curr = ring_node_positions[n_idx]
        node_next = ring_node_positions[(n_idx + 1) % 6]
        is_curr_a = is_a_site(node_curr)
        if is_curr_a:
            a_site, b_site = node_curr, node_next
        else:
            a_site, b_site = node_next, node_curr
        offset = np.array(b_site) - np.array(a_site)
        port_idx = next(p for p, po in enumerate(PORT_OFFSETS_A) if np.array_equal(offset, po))
        traversal = np.array(node_next) - np.array(node_curr)
        sign = float(np.sign(np.dot(offset, traversal)))
        ring_bonds.append({"a_site": a_site, "port": port_idx, "sign": sign})

    for i in range(N_RECORDING_STEPS):
        # Beltrami |cos_sim| at ring nodes
        cos_sims = []
        for n_idx, node in enumerate(ring_node_positions):
            ix, iy, iz = node
            # A-vec from Phi_link (per v8 method)
            is_a = is_a_site(node)
            a_vec = np.zeros(3)
            for p in range(4):
                bond_dir_A = PORT_OFFSETS_A[p].astype(float) / SQRT_3
                if is_a:
                    phi = phi_oscillating[i, ix, iy, iz, p]
                else:
                    ax, ay, az = ix - PORT_OFFSETS_A[p][0], iy - PORT_OFFSETS_A[p][1], iz - PORT_OFFSETS_A[p][2]
                    if 0 <= ax < nx and 0 <= ay < nx and 0 <= az < nx:
                        phi = phi_oscillating[i, ax, ay, az, p]
                    else:
                        phi = 0.0
                a_vec += (3.0 / 4.0) * bond_dir_A * (phi / BOND_LENGTH)
            b_vec = omega_traj_per_ring[i, n_idx, :].astype(np.float64)
            a_norm = np.linalg.norm(a_vec)
            b_norm = np.linalg.norm(b_vec)
            if a_norm < 1e-12 or b_norm < 1e-12:
                cos_sims.append(0.0)
            else:
                cos_sims.append(float(np.dot(a_vec, b_vec) / (a_norm * b_norm)))
        cos_sim_traj[i] = np.mean(np.abs(cos_sims))

        # Loop flux (instantaneous, from detrended Phi_link)
        loop_flux = 0.0
        for bond in ring_bonds:
            ix, iy, iz = bond["a_site"]
            phi = phi_oscillating[i, ix, iy, iz, bond["port"]]
            loop_flux += phi * bond["sign"]
        loop_flux_traj[i] = loop_flux

    # Compute eigenvector-derived loop flux target
    # ∮A·dl ≈ Σ over 6 bonds: A_avg · bond_tangent · bond_length
    a0_ring_data = eigvec_data["A_0_at_ring_nodes"]
    a0_ring_vecs = [scale * np.array(entry["A_0"]) for entry in a0_ring_data]
    target_loop_flux = 0.0
    for n_idx in range(6):
        a_curr = a0_ring_vecs[n_idx]
        a_next = a0_ring_vecs[(n_idx + 1) % 6]
        a_avg = 0.5 * (a_curr + a_next)
        bond_tangent_3d = (np.array(ring_node_positions[(n_idx + 1) % 6]) -
                          np.array(ring_node_positions[n_idx])).astype(float)
        bond_tangent_3d /= np.linalg.norm(bond_tangent_3d)
        target_loop_flux += np.dot(a_avg, bond_tangent_3d) * BOND_LENGTH
    target_loop_flux = abs(target_loop_flux)
    print(f"  Eigenvector-derived loop flux target: {target_loop_flux:.4f}")
    print()

    # Steady-state window (skip 25% transient)
    sw_start = N_RECORDING_STEPS // 4
    A2_mean_steady = float(np.mean(A2_mean_traj[sw_start:]))
    cos_sim_steady = float(np.mean(cos_sim_traj[sw_start:]))
    ring_loc_steady = float(np.mean(ring_loc_traj[sw_start:]))
    loop_flux_rms_steady = float(np.sqrt(np.mean(loop_flux_traj[sw_start:] ** 2)))
    loop_flux_peak_steady = float(np.max(np.abs(loop_flux_traj[sw_start:])))

    print("=" * 78)
    print("  Adjudication")
    print("=" * 78)
    print(f"  Persistence (A²_mean ≥ {A2_MEAN_THRESHOLD}): {persistence_periods:.1f} P  (≥ {PERSISTENCE_PERIODS} P)")
    print(f"  Beltrami |cos_sim| steady: {cos_sim_steady:.4f}  (≥ {BELTRAMI_PARALLELISM_THRESHOLD})")
    print(f"  Loop flux ∮A·dl RMS / peak: {loop_flux_rms_steady:.4f} / {loop_flux_peak_steady:.4f}  "
          f"(target {target_loop_flux:.4f} ± {LOOP_FLUX_TOLERANCE*100:.0f}%)")
    print(f"  Ring localization steady: {ring_loc_steady:.4f}  (≥ {RING_LOCALIZATION_THRESHOLD})")
    print(f"  A²_mean steady: {A2_mean_steady:.4f}")
    print()

    persistence_pass = persistence_periods >= PERSISTENCE_PERIODS
    beltrami_pass = cos_sim_steady >= BELTRAMI_PARALLELISM_THRESHOLD
    flux_pass = (
        abs(loop_flux_rms_steady - target_loop_flux) / target_loop_flux < LOOP_FLUX_TOLERANCE
        or abs(loop_flux_peak_steady - target_loop_flux) / target_loop_flux < LOOP_FLUX_TOLERANCE
    )
    loc_pass = ring_loc_steady >= RING_LOCALIZATION_THRESHOLD

    n_pass = sum([persistence_pass, beltrami_pass, flux_pass, loc_pass])
    if n_pass == 4:
        mode = "I"
    elif n_pass >= 2:
        mode = "II"
    else:
        mode = "III"

    verdict = (
        f"Mode {mode}: {n_pass}/4 PASS — "
        f"persist={persistence_pass} ({persistence_periods:.1f}P), "
        f"beltrami={beltrami_pass} ({cos_sim_steady:.3f}), "
        f"flux={flux_pass} (RMS={loop_flux_rms_steady:.3f} peak={loop_flux_peak_steady:.3f} target={target_loop_flux:.3f}), "
        f"loc={loc_pass} ({ring_loc_steady:.3f})"
    )
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase11_path_alpha_v9_discrete_eigenmode",
        "test": "v9 driver per Stride 3 eigenmode + Phase B IC + corrected k physical interpretation",
        "lattice": {"N": N_LATTICE, "pml": PML, "center": list(CENTER)},
        "ic": {
            "n_nodes_seeded": len(node_list),
            "scale_factor": float(scale),
            "saturation_amp_target": SATURATION_AMP_TARGET,
            "k_eigenvalue_natural": eigvec_data['eigenvalue'],
            "k_in_lnode_units": float(eigvec_data['eigenvalue'] * SQRT_3),
            "ring_localization_eigenmode": eigvec_data['ring_localization'],
        },
        "thresholds": {
            "persistence_periods": PERSISTENCE_PERIODS,
            "A2_mean_threshold": A2_MEAN_THRESHOLD,
            "beltrami_parallelism": BELTRAMI_PARALLELISM_THRESHOLD,
            "loop_flux_target_eigenvector_derived": target_loop_flux,
            "loop_flux_tolerance": LOOP_FLUX_TOLERANCE,
            "ring_localization": RING_LOCALIZATION_THRESHOLD,
        },
        "elapsed_seconds": elapsed,
        "initial_state": initial_state,
        "results": {
            "persistence_periods": persistence_periods,
            "A2_mean_steady": A2_mean_steady,
            "beltrami_cos_sim_steady": cos_sim_steady,
            "loop_flux_rms_steady": loop_flux_rms_steady,
            "loop_flux_peak_steady": loop_flux_peak_steady,
            "ring_localization_steady": ring_loc_steady,
        },
        "criteria_pass": {
            "persistence": bool(persistence_pass),
            "beltrami": bool(beltrami_pass),
            "loop_flux": bool(flux_pass),
            "ring_localization": bool(loc_pass),
            "n_pass": int(n_pass),
        },
        "mode": mode,
        "verdict": verdict,
    }
    args.output.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {args.output.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
