"""r9_path_alpha_v3_3d_aligned.py — Round 9 path α v3 per P_phase9_path_alpha_v3_3d_aligned.

Doc 79_ v5 §7.6 candidate structural reason (δ): c=3 in (2,3) maps to 3
orthogonal Cosserat ω-rotation axes, not 1D-curve crossings on a torus.

Path α v1 sampled (V_inc, V_ref) → bipolar R/r [1.95, 1.60, 9.24, 1.83],
clusters median 1.89/5.42.
Path α v2 sampled (Φ_link, ω · b̂) → bipolar R/r [5.42, 6.01, 3.93, 1.83],
clusters median 3.62/4.97.

Both used scalar projection ω · b̂ where b̂ = (1,1,1)/√3 (port 0) for all
4 selected bonds. This collapses the 3D Cosserat ω-vector into 1 scalar.

(δ) interpretation: if the substrate's bound-state rotation is genuinely
3D-coordinated (one rotation per spatial axis), sampling ω · b̂ projects
out 2 of 3 ω components by construction. Bipolar R/r is the signature of
3D structure sampled along one direction at a time.

Move 10 empirical anchor (doc 74_ §15.4): "Op10 c=3 carrier matches NONE
of standard topology types (torus knot, Hopf-linked, Y_lm) — open question
for Round 8+." (δ) is one possible answer.

Setup IDENTICAL to path α v1+v2 (and Move 5). Sampler change ONLY:
capture (Φ_link[A,port], ω_x, ω_y, ω_z) per bond per step (4 channels).

THREE PER-BOND ELLIPSE TESTS:
(a) 3D ω-trajectory PCA (rotation-invariant): eigenvalues e0 ≤ e1 ≤ e2
    of cov(ω); test e2/e1 ≈ φ² AND planarity e0/e2 < 0.1
(b) Per-axis (Φ_link, ω_i) for i ∈ {x,y,z}: three ellipse fits per bond;
    test if ANY axis yields R/r = φ² with chirality ≥ 75%
(c) (Φ_link, |ω|): scalar magnitude pairing; test R/r = φ² + chirality

Per-cluster Mode I if ANY of (a) / (b-x) / (b-y) / (b-z) / (c) passes
C1 (R/r = φ² ± 5% on median) AND C2 (chirality ≥ 75%).
"""
from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.signal import hilbert

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants (matching Move 5 + path α v1/v2 exactly for engine setup) ──

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ

A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi
A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA
V_AMP_INIT = 0.14

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

# ─── Path α v3 windows (same as v2) ────────────────────────────────────────
PRE_EVOLVE_END_P = 10.0
SELECTION_END_P = 15.0
RECORDING_END_P = 200.0

PRE_EVOLVE_END_STEP = int(PRE_EVOLVE_END_P * COMPTON_PERIOD / DT)
SELECTION_END_STEP = int(SELECTION_END_P * COMPTON_PERIOD / DT)
RECORDING_END_STEP = int(RECORDING_END_P * COMPTON_PERIOD / DT)
N_SELECTION_STEPS = SELECTION_END_STEP - PRE_EVOLVE_END_STEP
N_RECORDING_STEPS = RECORDING_END_STEP - SELECTION_END_STEP

TOP_K_CANDIDATES = 8
SAMPLE_PORT_DEFAULT = 0  # K4 port 0 has offset (+1,+1,+1)

PORT_OFFSETS = [
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
]
SQRT_3 = np.sqrt(3.0)

# Adjudication thresholds
PHI_SQ_TOL = 0.05
CHIRALITY_CONSISTENCY_THRESHOLD = 0.75
PERSISTENCE_GUARD = 0.40
PLANARITY_THRESHOLD = 0.1  # e0/e2 < 0.1 → orbit lies substantially in 2-plane

OUTPUT_JSON = Path(__file__).parent / "r9_path_alpha_v3_3d_aligned_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def make_interior_mask(nx, pml):
    mask = np.zeros((nx, nx, nx), dtype=bool)
    mask[pml:nx - pml, pml:nx - pml, pml:nx - pml] = True
    return mask


def fit_ellipse_pca_2d(x_traj, y_traj):
    """PCA on (x, y) point cloud → ellipse axes (R_phase, r_phase)."""
    points = np.column_stack([x_traj, y_traj])
    points = points - points.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    r_phase = float(np.sqrt(max(eigvals[0], 1e-30)))
    R_phase = float(np.sqrt(max(eigvals[1], 1e-30)))
    return R_phase, r_phase


def fit_ellipsoid_pca_3d(omega_traj):
    """PCA on 3D ω-trajectory → eigenvalues e0 ≤ e1 ≤ e2 of cov(ω).

    Returns (e0, e1, e2, planarity_e0_over_e2, in_plane_aspect_e2_over_e1).
    Eigenvalues are variances; sqrt for axis lengths if needed.
    """
    points = omega_traj - omega_traj.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    e0 = float(max(eigvals[0], 1e-30))
    e1 = float(max(eigvals[1], 1e-30))
    e2 = float(max(eigvals[2], 1e-30))
    # Convert variances to ellipsoid axis lengths (sqrt scale)
    a0 = float(np.sqrt(e0))
    a1 = float(np.sqrt(e1))
    a2 = float(np.sqrt(e2))
    planarity = a0 / max(a2, 1e-30)
    in_plane_aspect = a2 / max(a1, 1e-30)
    return e0, e1, e2, a0, a1, a2, planarity, in_plane_aspect


def chirality_hilbert(x_traj, y_traj):
    """Hilbert-transform-based chirality on slow-trading signal."""
    x = np.asarray(x_traj) - np.mean(x_traj)
    y = np.asarray(y_traj) - np.mean(y_traj)
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return 0.0, 0.0, 0
    xa = hilbert(x)
    ya = hilbert(y)
    phi_x = np.angle(xa)
    phi_y = np.angle(ya)
    delta_phi = phi_x - phi_y
    sin_delta = np.sin(delta_phi)
    mean_sin = float(np.mean(sin_delta))
    std_sin = float(np.std(sin_delta))
    if abs(mean_sin) < 0.1 * (std_sin + 1e-12):
        return mean_sin, std_sin, 0
    return mean_sin, std_sin, int(np.sign(mean_sin))


def find_bond_pairs(top_cells_list, top_cells_set):
    """K4 tetrahedral bond-pair identification (same as v1/v2)."""
    bond_pairs = []
    used_cells = set()
    for cell_a in top_cells_list:
        if cell_a in used_cells:
            continue
        for port_idx, offset in enumerate(PORT_OFFSETS):
            cell_b = (cell_a[0] + offset[0], cell_a[1] + offset[1], cell_a[2] + offset[2])
            if cell_b in top_cells_set and cell_b not in used_cells:
                b_hat = (offset[0] / SQRT_3, offset[1] / SQRT_3, offset[2] / SQRT_3)
                bond_pairs.append({
                    "cell_a": list(cell_a),
                    "port": port_idx,
                    "cell_b": list(cell_b),
                    "b_hat": list(b_hat),
                })
                used_cells.add(cell_a)
                used_cells.add(cell_b)
                break
    return bond_pairs


def cluster_bond_pairs(bond_pairs, lattice_center):
    clusters = defaultdict(list)
    for bp_idx, bp in enumerate(bond_pairs):
        cx = (bp["cell_a"][0] + bp["cell_b"][0]) / 2.0
        cluster_key = "+x" if cx > lattice_center else "-x"
        clusters[cluster_key].append(bp_idx)
    return dict(clusters)


def main():
    print("=" * 78, flush=True)
    print("  r9 PATH α v3 — 3D-aligned ω-vector sampler (auditor (δ) test)")
    print("  P_phase9_path_alpha_v3_3d_aligned")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, PML={PML} (interior {N_LATTICE - 2*PML}^3)")
    print(f"  Corpus GT: R={R_ANCHOR}, r={R_MINOR:.4f}")
    print(f"  Pre-evolve: t ∈ [0, {PRE_EVOLVE_END_P}] P")
    print(f"  Selection: t ∈ [{PRE_EVOLVE_END_P}, {SELECTION_END_P}] P "
          f"({N_SELECTION_STEPS} steps)")
    print(f"  Recording: t ∈ [{SELECTION_END_P}, {RECORDING_END_P}] P "
          f"({N_RECORDING_STEPS} steps)")
    print(f"  Sampler: (Φ_link[A,port], ω_x, ω_y, ω_z) at K4 bond-pairs")
    print(f"  Per-bond ellipse views:")
    print(f"    (a) 3D ω-PCA: eigenvalues + planarity + e2/e1 aspect")
    print(f"    (b) Per-axis (Φ_link, ω_i) for i ∈ {{x, y, z}}")
    print(f"    (c) (Φ_link, |ω|) magnitude pairing")
    print(f"  Mode I criteria (per cluster):")
    print(f"    C1: ANY view yields R/r = φ²={PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}")
    print(f"    C2: chirality consensus ≥ {CHIRALITY_CONSISTENCY_THRESHOLD:.0%}")
    print(f"    Planarity (a-only): e0/e2 < {PLANARITY_THRESHOLD}")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)
    engine.k4.reset_phi_link()

    omega_init = np.asarray(engine.cos.omega)
    omega_peak_init = float(np.linalg.norm(omega_init, axis=-1).max())
    assert A26_GUARD_LOW <= omega_peak_init <= A26_GUARD_HIGH
    print(f"  Initial peak |ω| = {omega_peak_init:.4f} (A26 guard OK)")

    # ─── Phase 1: pre-evolve ──────────────────────────────────────────────
    print(f"  Pre-evolving to t={PRE_EVOLVE_END_P} P...", flush=True)
    t0 = time.time()
    last_progress = t0
    for step in range(PRE_EVOLVE_END_STEP):
        engine.step()
        if (time.time() - last_progress) > 30.0:
            print(f"    [progress] step={step}, elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()
    print(f"    pre-evolve done at {time.time()-t0:.1f}s", flush=True)

    # ─── Phase 2: cell selection (peak |V_inc[port 0]|² for cell ranking) ─
    print(f"  Cell selection window...", flush=True)
    interior_mask = make_interior_mask(engine.k4.nx, PML)
    v_inc_sq_accum = np.zeros((engine.k4.nx, engine.k4.nx, engine.k4.nx))

    for i in range(N_SELECTION_STEPS):
        engine.step()
        v_inc = np.asarray(engine.k4.V_inc)
        v_inc_sq_accum += v_inc[..., SAMPLE_PORT_DEFAULT] ** 2
        if (time.time() - last_progress) > 30.0:
            print(f"    [progress] selection step {i}, elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()

    v_inc_mean_sq = v_inc_sq_accum / N_SELECTION_STEPS
    v_inc_mean_sq_interior = v_inc_mean_sq.copy()
    v_inc_mean_sq_interior[~interior_mask] = 0.0

    flat_idx = np.argpartition(v_inc_mean_sq_interior.ravel(),
                                -TOP_K_CANDIDATES)[-TOP_K_CANDIDATES:]
    sorted_idx = flat_idx[np.argsort(-v_inc_mean_sq_interior.ravel()[flat_idx])]
    top_cells_list = []
    top_cells_set = set()
    for idx in sorted_idx:
        ix, iy, iz = np.unravel_index(idx, v_inc_mean_sq_interior.shape)
        cell = (int(ix), int(iy), int(iz))
        top_cells_list.append(cell)
        top_cells_set.add(cell)

    print(f"  Top-{TOP_K_CANDIDATES} candidates by |V_inc[port {SAMPLE_PORT_DEFAULT}]|²:")
    for k, cell in enumerate(top_cells_list):
        print(f"    [{k}] {cell}  |V|²={v_inc_mean_sq_interior[cell]:.4e}", flush=True)

    bond_pairs = find_bond_pairs(top_cells_list, top_cells_set)
    n_pairs = len(bond_pairs)
    print(f"  Identified {n_pairs} K4 bond-pairs:")
    for k, bp in enumerate(bond_pairs):
        offset = PORT_OFFSETS[bp["port"]]
        print(f"    [{k}] A={tuple(bp['cell_a'])} port {bp['port']} → "
              f"B={tuple(bp['cell_b'])} (offset {offset})", flush=True)

    if n_pairs == 0:
        raise RuntimeError("No K4 bond-pairs found — abort")

    # ─── Phase 3: recording window (4-channel sampler) ────────────────────
    print(f"  Recording window: capturing (Φ_link, ω_x, ω_y, ω_z) at "
          f"{n_pairs} bond-pairs...", flush=True)
    phi_link_traj = np.zeros((N_RECORDING_STEPS, n_pairs))
    omega_xyz_traj = np.zeros((N_RECORDING_STEPS, n_pairs, 3))

    for i in range(N_RECORDING_STEPS):
        engine.step()
        phi_link = np.asarray(engine.k4.Phi_link)
        omega = np.asarray(engine.cos.omega)
        for k, bp in enumerate(bond_pairs):
            ix, iy, iz = bp["cell_a"]
            port = bp["port"]
            phi_link_traj[i, k] = phi_link[ix, iy, iz, port]
            omega_xyz_traj[i, k, :] = omega[ix, iy, iz]
        if (time.time() - last_progress) > 30.0:
            t_period = (SELECTION_END_STEP + i) * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step {i}/{N_RECORDING_STEPS}  "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()

    elapsed_total = time.time() - t0
    print(f"  Recording done; total elapsed {elapsed_total:.1f}s", flush=True)

    # ─── Phase 4: per-bond multi-view ellipse + chirality ────────────────
    print()
    print("=" * 78, flush=True)
    print("  Per-bond multi-view phasor analysis")
    print("=" * 78, flush=True)

    bond_results = []
    axis_labels = ["x", "y", "z"]
    for k in range(n_pairs):
        # (a) 3D ω-PCA
        omega_k = omega_xyz_traj[:, k, :]
        e0, e1, e2, a0, a1, a2, planarity, in_plane_aspect = fit_ellipsoid_pca_3d(omega_k)

        # (b) Per-axis (Φ_link, ω_i)
        per_axis_views = {}
        for ax in range(3):
            R_ax, r_ax = fit_ellipse_pca_2d(phi_link_traj[:, k], omega_k[:, ax])
            R_over_r_ax = R_ax / max(r_ax, 1e-30)
            mean_sin_ax, std_sin_ax, chirality_sign_ax = chirality_hilbert(
                phi_link_traj[:, k], omega_k[:, ax]
            )
            chir_label_ax = ("CCW" if chirality_sign_ax > 0
                             else "CW" if chirality_sign_ax < 0 else "AMBIG")
            per_axis_views[axis_labels[ax]] = {
                "R_phase": R_ax,
                "r_phase": r_ax,
                "R_over_r": R_over_r_ax,
                "omega_amplitude_std": float(np.std(omega_k[:, ax])),
                "chirality_mean_sin_dphi": mean_sin_ax,
                "chirality_std_sin_dphi": std_sin_ax,
                "chirality_sign": chirality_sign_ax,
                "chirality_label": chir_label_ax,
            }

        # (c) (Φ_link, |ω|)
        omega_mag = np.linalg.norm(omega_k, axis=1)
        R_mag, r_mag = fit_ellipse_pca_2d(phi_link_traj[:, k], omega_mag)
        R_over_r_mag = R_mag / max(r_mag, 1e-30)
        mean_sin_mag, std_sin_mag, chirality_sign_mag = chirality_hilbert(
            phi_link_traj[:, k], omega_mag
        )
        chir_label_mag = ("CCW" if chirality_sign_mag > 0
                          else "CW" if chirality_sign_mag < 0 else "AMBIG")

        bond_results.append({
            **bond_pairs[k],
            "phi_link_amplitude_std": float(np.std(phi_link_traj[:, k])),
            "view_a_3d_omega_pca": {
                "eigvals": [e0, e1, e2],
                "axis_lengths": [a0, a1, a2],
                "planarity_e0_over_e2": planarity,
                "in_plane_aspect_e2_over_e1": in_plane_aspect,
            },
            "view_b_per_axis": per_axis_views,
            "view_c_magnitude": {
                "R_phase": R_mag,
                "r_phase": r_mag,
                "R_over_r": R_over_r_mag,
                "omega_mag_std": float(np.std(omega_mag)),
                "chirality_mean_sin_dphi": mean_sin_mag,
                "chirality_std_sin_dphi": std_sin_mag,
                "chirality_sign": chirality_sign_mag,
                "chirality_label": chir_label_mag,
            },
        })
        print(f"  [{k}] {tuple(bond_pairs[k]['cell_a'])} → "
              f"{tuple(bond_pairs[k]['cell_b'])}", flush=True)
        print(f"      (a) 3D ω-PCA: planarity={planarity:.4f}, "
              f"e2/e1={in_plane_aspect:.4f} (target φ²={PHI_SQ:.4f})", flush=True)
        for ax in range(3):
            v = per_axis_views[axis_labels[ax]]
            print(f"      (b-{axis_labels[ax]}) (Φ,ω_{axis_labels[ax]}): "
                  f"R/r={v['R_over_r']:8.4f}  chirality={v['chirality_label']}", flush=True)
        print(f"      (c) (Φ,|ω|): R/r={R_over_r_mag:8.4f}  "
              f"chirality={chir_label_mag}", flush=True)

    # ─── Phase 5: per-cluster + global adjudication ───────────────────────
    lattice_center = (engine.k4.nx - 1) / 2.0
    clusters = cluster_bond_pairs(bond_pairs, lattice_center)

    def cluster_view_pass(bp_indices, view_extractor_R_over_r, view_extractor_chirality):
        """Apply C1+C2 to a single sampler view across a cluster."""
        R_over_r_list = [view_extractor_R_over_r(bond_results[i]) for i in bp_indices]
        chirality_list = [view_extractor_chirality(bond_results[i]) for i in bp_indices]
        median_R_over_r = float(np.median(R_over_r_list))
        n_ccw = sum(1 for s in chirality_list if s > 0)
        n_cw = sum(1 for s in chirality_list if s < 0)
        consensus = max(n_ccw, n_cw)
        consensus_fraction = consensus / max(len(chirality_list), 1)
        consensus_dir = "CCW" if n_ccw > n_cw else "CW" if n_cw > n_ccw else "TIE"
        c1_pass = abs(median_R_over_r - PHI_SQ) <= PHI_SQ_TOL * PHI_SQ
        c2_pass = consensus_fraction >= CHIRALITY_CONSISTENCY_THRESHOLD
        return {
            "median_R_over_r": median_R_over_r,
            "consensus_fraction": consensus_fraction,
            "consensus_direction": consensus_dir,
            "n_ccw": n_ccw, "n_cw": n_cw,
            "c1_pass": bool(c1_pass), "c2_pass": bool(c2_pass),
            "mode_i_pass": bool(c1_pass and c2_pass),
        }

    cluster_adjudication = {}
    for cluster_key, bp_indices in clusters.items():
        # View (a) 3D ω-PCA — no chirality (rotation-invariant); test e2/e1 + planarity
        in_plane_aspect_list = [
            bond_results[i]["view_a_3d_omega_pca"]["in_plane_aspect_e2_over_e1"]
            for i in bp_indices
        ]
        planarity_list = [
            bond_results[i]["view_a_3d_omega_pca"]["planarity_e0_over_e2"]
            for i in bp_indices
        ]
        median_e2_e1 = float(np.median(in_plane_aspect_list))
        median_planarity = float(np.median(planarity_list))
        a_c1_pass = abs(median_e2_e1 - PHI_SQ) <= PHI_SQ_TOL * PHI_SQ
        a_planar = median_planarity < PLANARITY_THRESHOLD
        view_a = {
            "median_e2_over_e1": median_e2_e1,
            "median_planarity_e0_over_e2": median_planarity,
            "c1_pass_aspect": bool(a_c1_pass),
            "planarity_pass": bool(a_planar),
            "mode_i_pass": bool(a_c1_pass and a_planar),
        }

        # View (b) per-axis
        view_b = {}
        for ax in axis_labels:
            view_b[ax] = cluster_view_pass(
                bp_indices,
                lambda r, _ax=ax: r["view_b_per_axis"][_ax]["R_over_r"],
                lambda r, _ax=ax: r["view_b_per_axis"][_ax]["chirality_sign"],
            )

        # View (c) magnitude
        view_c = cluster_view_pass(
            bp_indices,
            lambda r: r["view_c_magnitude"]["R_over_r"],
            lambda r: r["view_c_magnitude"]["chirality_sign"],
        )

        cluster_mode_i = (
            view_a["mode_i_pass"]
            or any(view_b[ax]["mode_i_pass"] for ax in axis_labels)
            or view_c["mode_i_pass"]
        )

        cluster_adjudication[cluster_key] = {
            "n_bonds": len(bp_indices),
            "view_a_3d_omega_pca": view_a,
            "view_b_per_axis": view_b,
            "view_c_magnitude": view_c,
            "cluster_mode_i_pass": bool(cluster_mode_i),
            "bond_indices": bp_indices,
        }

    omega_final = np.asarray(engine.cos.omega)
    omega_peak_final = float(np.linalg.norm(omega_final, axis=-1).max())
    persistence = omega_peak_final / max(omega_peak_init, 1e-30)
    persistence_ok = persistence >= PERSISTENCE_GUARD

    all_clusters_mode_i = all(
        a["cluster_mode_i_pass"] for a in cluster_adjudication.values()
    )

    # Determine which view drove Mode I (if any)
    passing_views = []
    for cluster_key, adj in cluster_adjudication.items():
        if adj["view_a_3d_omega_pca"]["mode_i_pass"]:
            passing_views.append(f"{cluster_key}: view (a) 3D ω-PCA")
        for ax in axis_labels:
            if adj["view_b_per_axis"][ax]["mode_i_pass"]:
                passing_views.append(f"{cluster_key}: view (b-{ax}) per-axis")
        if adj["view_c_magnitude"]["mode_i_pass"]:
            passing_views.append(f"{cluster_key}: view (c) magnitude")

    if all_clusters_mode_i:
        mode = "I"
        verdict = (
            f"MODE I — POSITIVE L3 REOPEN. (δ) interpretation empirically confirmed. "
            f"3D-aligned sampler yields Mode I across both clusters. Passing views: "
            f"{passing_views}. c=3 in (2,3) maps to 3 spatial Cosserat ω-rotation axes "
            f"(or planar 3D orbit per view (a)). Doc 79_ v5 closure flips to Mode I; "
            f"v5.1 lands positive close with structural-reason isolation."
        )
    elif passing_views:
        mode = "III-asymmetric"
        verdict = (
            f"MODE III-asymmetric — (δ) partial signature. Some passing views: "
            f"{passing_views}. But not Mode I in BOTH clusters across any single view. "
            f"Bipolar pattern persists. Doc 79_ v5 Mode III canonical closure stands; "
            f"v5.1 amendment hardens with sampler-exhaustion evidence (3D structure "
            f"sampled but no consistent golden-ratio orbit found)."
        )
    else:
        mode = "III"
        verdict = (
            f"MODE III — (δ) interpretation falsified at engine-representable scale. "
            f"None of (a) 3D ω-PCA, (b-x/y/z) per-axis, (c) magnitude pass C1+C2 in "
            f"both clusters. Sampler axis-projection is NOT the load-bearing flaw. "
            f"Doc 79_ v5 Mode III canonical closure stands with v5.1 amendment "
            f"hardening: structural reason is not 3D-axis-mapping."
        )

    if not persistence_ok:
        verdict += (
            f" CAVEAT: peak |ω| persistence {persistence:.0%} below "
            f"{PERSISTENCE_GUARD:.0%} threshold."
        )

    print()
    print("=" * 78, flush=True)
    print("  Per-cluster + final adjudication")
    print("=" * 78, flush=True)
    for cluster_key, adj in cluster_adjudication.items():
        print(f"  Cluster {cluster_key} ({adj['n_bonds']} bonds):")
        va = adj["view_a_3d_omega_pca"]
        print(f"    (a) 3D ω-PCA: median e2/e1 = {va['median_e2_over_e1']:.4f} "
              f"(target φ²={PHI_SQ:.4f}, "
              f"{'PASS' if va['c1_pass_aspect'] else 'FAIL'}), "
              f"planarity {va['median_planarity_e0_over_e2']:.4f} "
              f"({'PASS' if va['planarity_pass'] else 'FAIL'}) → "
              f"Mode I {'PASS' if va['mode_i_pass'] else 'FAIL'}")
        for ax in axis_labels:
            vb = adj["view_b_per_axis"][ax]
            print(f"    (b-{ax}) (Φ,ω_{ax}): median R/r = {vb['median_R_over_r']:.4f}, "
                  f"chirality {vb['consensus_fraction']:.0%} {vb['consensus_direction']} → "
                  f"C1 {'PASS' if vb['c1_pass'] else 'FAIL'}, "
                  f"C2 {'PASS' if vb['c2_pass'] else 'FAIL'}")
        vc = adj["view_c_magnitude"]
        print(f"    (c) (Φ,|ω|): median R/r = {vc['median_R_over_r']:.4f}, "
              f"chirality {vc['consensus_fraction']:.0%} {vc['consensus_direction']} → "
              f"C1 {'PASS' if vc['c1_pass'] else 'FAIL'}, "
              f"C2 {'PASS' if vc['c2_pass'] else 'FAIL'}")
        print(f"    Cluster Mode I: "
              f"{'PASS' if adj['cluster_mode_i_pass'] else 'FAIL'}")
    print(f"  Persistence: {persistence:.0%}")
    print()
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase9_path_alpha_v3_3d_aligned",
        "test": "Round 9 path α v3: 3D-aligned ω-vector sampler — auditor (δ) interpretation",
        "N": N_LATTICE,
        "PML": PML,
        "R": R_ANCHOR,
        "r": R_MINOR,
        "phi_sq": PHI_SQ,
        "v_amp_init": V_AMP_INIT,
        "a26_amp_scale": A26_AMP_SCALE,
        "pre_evolve_end_p": PRE_EVOLVE_END_P,
        "selection_end_p": SELECTION_END_P,
        "recording_end_p": RECORDING_END_P,
        "n_recording_steps": N_RECORDING_STEPS,
        "top_k_candidates": TOP_K_CANDIDATES,
        "sample_port_default": SAMPLE_PORT_DEFAULT,
        "elapsed_seconds": elapsed_total,
        "omega_peak_init": omega_peak_init,
        "omega_peak_final": omega_peak_final,
        "persistence": persistence,
        "persistence_guard": PERSISTENCE_GUARD,
        "persistence_ok": bool(persistence_ok),
        "n_bond_pairs": n_pairs,
        "bond_results": bond_results,
        "cluster_adjudication": cluster_adjudication,
        "phi_sq_target": PHI_SQ,
        "phi_sq_tolerance": PHI_SQ_TOL,
        "consensus_threshold": CHIRALITY_CONSISTENCY_THRESHOLD,
        "planarity_threshold": PLANARITY_THRESHOLD,
        "passing_views": passing_views,
        "all_clusters_mode_i": bool(all_clusters_mode_i),
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
