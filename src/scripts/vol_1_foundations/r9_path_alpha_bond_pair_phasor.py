"""r9_path_alpha_bond_pair_phasor.py — Round 9 path α per P_phase9_path_alpha.

Doc 79_ v3.1 §7 empirical test. Decides positive vs negative L3 closure under
the lemniscate-with-q-half-twists bond-pair object class.

Setup IDENTICAL to Move 5 + r9 (N=32, R=10, r=R/φ², 200 Compton periods,
Cosserat self-terms, no drive, peak |ω|=0.3π via A26 scale, V_amp=0.14).

Four methodology fixes vs r9:
1. Recording window EARLIER: t ∈ [15, 50] P (fresh attractor pre-decay)
2. Sampler = top-K SATURATED A-B BOND PAIRS via K4 tetrahedral port offsets
   (NOT top-K single cells)
3. Chirality via Hilbert transform analytic-signal phase difference
   (NOT mean P × dP/dt cross-product)
4. Per-cluster R/r adjudication (NOT single global median)

Dual-criterion (per cluster):
  C1: R_phase/r_phase = φ² ± 5%
  C2: chirality consensus ≥ 75% via mean(sin(Δφ_Hilbert))
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


# ─── Constants (matching Move 5 + r9 exactly for engine setup) ─────────────

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
N_PERIODS_TOTAL = 200.0  # Move 5 horizon (we don't run all of it; just for reference)
DT = 1.0 / np.sqrt(2.0)

# ─── Path α specific (NEW vs r9) ────────────────────────────────────────────
PRE_EVOLVE_END_P = 10.0          # transient settle
SELECTION_END_P = 15.0           # 5 P selection window
RECORDING_END_P = 50.0           # 35 P recording (fresh attractor pre-decay)

PRE_EVOLVE_END_STEP = int(PRE_EVOLVE_END_P * COMPTON_PERIOD / DT)
SELECTION_END_STEP = int(SELECTION_END_P * COMPTON_PERIOD / DT)
RECORDING_END_STEP = int(RECORDING_END_P * COMPTON_PERIOD / DT)
N_SELECTION_STEPS = SELECTION_END_STEP - PRE_EVOLVE_END_STEP
N_RECORDING_STEPS = RECORDING_END_STEP - SELECTION_END_STEP

TOP_K_CANDIDATES = 8        # find 8 saturated cells, pair up to 4 bond-pairs
SAMPLE_PORT = 0             # port 0 of A-side cell

# K4 tetrahedral port offsets (standard layout: 4 vertices of tetrahedron)
PORT_OFFSETS = [
    (1, 1, 1),    # port 0: +x +y +z
    (1, -1, -1),  # port 1: +x -y -z
    (-1, 1, -1),  # port 2: -x +y -z
    (-1, -1, 1),  # port 3: -x -y +z
]

# Adjudication thresholds
PHI_SQ_TOL = 0.05           # ±5%
CHIRALITY_CONSISTENCY_THRESHOLD = 0.75
PERSISTENCE_GUARD = 0.70    # tighter than r9's 0.40 because window is earlier

OUTPUT_JSON = Path(__file__).parent / "r9_path_alpha_bond_pair_results.json"


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


def fit_ellipse_pca(v_inc_traj, v_ref_traj):
    """PCA on (V_inc, V_ref) point cloud → ellipse axes.
    Returns (R_phase, r_phase) = (major, minor) axis lengths.
    """
    points = np.column_stack([v_inc_traj, v_ref_traj])
    points = points - points.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    r_phase = float(np.sqrt(max(eigvals[0], 1e-30)))
    R_phase = float(np.sqrt(max(eigvals[1], 1e-30)))
    return R_phase, r_phase


def chirality_hilbert(v_inc_traj, v_ref_traj):
    """Hilbert-transform-based chirality measurement.

    Compute analytic signals via Hilbert transform; instantaneous phases
    via complex argument; phase difference Δφ(t); mean(sin(Δφ)) gives
    chirality magnitude (+1: V_inc leads V_ref by π/2 = CCW;
    −1: V_inc lags by π/2 = CW; 0: in phase or out of phase = no rotation).

    More robust to amplitude fluctuations than mean P × dP/dt because it
    tracks PHASE rather than amplitude-weighted cross-product.
    """
    v_inc = np.asarray(v_inc_traj) - np.mean(v_inc_traj)
    v_ref = np.asarray(v_ref_traj) - np.mean(v_ref_traj)

    # Skip if either trace is essentially zero (degenerate)
    if np.std(v_inc) < 1e-12 or np.std(v_ref) < 1e-12:
        return 0.0, 0.0, 0

    v_inc_a = hilbert(v_inc)
    v_ref_a = hilbert(v_ref)

    phi_inc = np.angle(v_inc_a)
    phi_ref = np.angle(v_ref_a)

    delta_phi = phi_inc - phi_ref
    sin_delta = np.sin(delta_phi)

    mean_sin = float(np.mean(sin_delta))
    std_sin = float(np.std(sin_delta))

    # Robust sign: only ±1 if |mean| > some fraction of std (else 0)
    if abs(mean_sin) < 0.1 * (std_sin + 1e-12):
        chirality_sign = 0
    else:
        chirality_sign = int(np.sign(mean_sin))

    return mean_sin, std_sin, chirality_sign


def find_bond_pairs(top_cells_list, top_cells_set):
    """Find K4 bond-pairs among top candidates via tetrahedral port offsets.

    For each top cell, check if any of its 4 K4 port-neighbors is also a
    top candidate. If yes, register as bond-pair.
    """
    bond_pairs = []
    used_cells = set()

    for cell_a in top_cells_list:
        if cell_a in used_cells:
            continue
        for port_idx, offset in enumerate(PORT_OFFSETS):
            cell_b = (cell_a[0] + offset[0], cell_a[1] + offset[1], cell_a[2] + offset[2])
            if cell_b in top_cells_set and cell_b not in used_cells:
                bond_pairs.append({
                    "cell_a": list(cell_a),
                    "port": port_idx,
                    "cell_b": list(cell_b),
                })
                used_cells.add(cell_a)
                used_cells.add(cell_b)
                break
    return bond_pairs


def cluster_bond_pairs(bond_pairs, lattice_center):
    """Group bond-pairs by spatial cluster (e.g., +x quadrant vs -x quadrant).

    Use centroid of (cell_a, cell_b) as the bond-pair location. Cluster by
    sign of (centroid_x - lattice_center_x) → +x cluster vs -x cluster.
    Falls back to (sign of centroid_y - center_y) if no x-asymmetry.
    """
    clusters = defaultdict(list)
    for bp_idx, bp in enumerate(bond_pairs):
        cx = (bp["cell_a"][0] + bp["cell_b"][0]) / 2.0
        cy = (bp["cell_a"][1] + bp["cell_b"][1]) / 2.0
        # Primary clustering: sign of (centroid_x - center_x)
        cluster_key = "+x" if cx > lattice_center else "-x"
        clusters[cluster_key].append(bp_idx)
    return dict(clusters)


def main():
    print("=" * 78, flush=True)
    print("  r9 PATH α — Bond-pair phasor on Move 5 fresh attractor")
    print("  P_phase9_path_alpha")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, PML={PML} (interior {N_LATTICE - 2*PML}^3)")
    print(f"  Corpus GT: R={R_ANCHOR}, r={R_MINOR:.4f}")
    print(f"  Pre-evolve: t ∈ [0, {PRE_EVOLVE_END_P}] P")
    print(f"  Selection: t ∈ [{PRE_EVOLVE_END_P}, {SELECTION_END_P}] P "
          f"({N_SELECTION_STEPS} steps)")
    print(f"  Recording: t ∈ [{SELECTION_END_P}, {RECORDING_END_P}] P "
          f"({N_RECORDING_STEPS} steps)")
    print(f"  Top-K candidates: {TOP_K_CANDIDATES}; bond-pair via K4 port offsets")
    print(f"  Chirality: Hilbert-transform mean(sin(Δφ))")
    print(f"  Dual-criterion (per cluster):")
    print(f"    C1: R/r = φ²={PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}")
    print(f"    C2: chirality consensus ≥ {CHIRALITY_CONSISTENCY_THRESHOLD:.0%}")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    omega_init = np.asarray(engine.cos.omega)
    omega_peak_init = float(np.linalg.norm(omega_init, axis=-1).max())
    assert A26_GUARD_LOW <= omega_peak_init <= A26_GUARD_HIGH, (
        f"A26 guard FAILED: peak |ω|={omega_peak_init:.4f}"
    )
    print(f"  Initial peak |ω| = {omega_peak_init:.4f} (A26 guard OK)")

    # ─── Phase 1: pre-evolve ─────────────────────────────────────────────────
    print(f"  Pre-evolving to t={PRE_EVOLVE_END_P} P...", flush=True)
    t0 = time.time()
    last_progress = t0
    for step in range(PRE_EVOLVE_END_STEP):
        engine.step()
        if (time.time() - last_progress) > 30.0:
            t_period = step * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step={step:5d}  "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()
    print(f"    pre-evolve done at {time.time()-t0:.1f}s", flush=True)

    # ─── Phase 2: cell selection (accumulate |V_inc[port 0]|² per cell) ─────
    print(f"  Cell selection window...", flush=True)
    interior_mask = make_interior_mask(engine.k4.nx, PML)
    v_inc_sq_accum = np.zeros((engine.k4.nx, engine.k4.nx, engine.k4.nx))

    for i in range(N_SELECTION_STEPS):
        engine.step()
        v_inc = np.asarray(engine.k4.V_inc)
        v_inc_sq_accum += v_inc[..., SAMPLE_PORT] ** 2
        if (time.time() - last_progress) > 30.0:
            t_period = (PRE_EVOLVE_END_STEP + i) * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  elapsed {time.time()-t0:.1f}s",
                  flush=True)
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

    print(f"  Top-{TOP_K_CANDIDATES} candidates by |V_inc[port {SAMPLE_PORT}]|²:")
    for k, cell in enumerate(top_cells_list):
        print(f"    [{k}] {cell}  |V|²={v_inc_mean_sq_interior[cell]:.4e}", flush=True)

    # ─── Phase 3: bond-pair identification via K4 port offsets ──────────────
    bond_pairs = find_bond_pairs(top_cells_list, top_cells_set)
    n_pairs = len(bond_pairs)
    print(f"  Identified {n_pairs} K4 bond-pairs:")
    for k, bp in enumerate(bond_pairs):
        offset = PORT_OFFSETS[bp["port"]]
        print(f"    [{k}] A={tuple(bp['cell_a'])} port {bp['port']} → "
              f"B={tuple(bp['cell_b'])} (offset {offset})", flush=True)

    if n_pairs == 0:
        print("  ⚠ NO BOND-PAIRS FOUND — top cells are not K4-adjacent.")
        print("  Falling back to closest-pair adjacency (Euclidean, any offset).")
        # Fallback: just pair top cells by Euclidean closeness
        used = set()
        for i, ca in enumerate(top_cells_list):
            if i in used:
                continue
            best_j = -1
            best_d = float("inf")
            for j, cb in enumerate(top_cells_list):
                if j == i or j in used:
                    continue
                d = sum((ca[k] - cb[k])**2 for k in range(3))
                if d < best_d:
                    best_d = d
                    best_j = j
            if best_j != -1:
                bond_pairs.append({
                    "cell_a": list(ca),
                    "port": SAMPLE_PORT,
                    "cell_b": list(top_cells_list[best_j]),
                    "fallback_euclidean": True,
                })
                used.add(i)
                used.add(best_j)
        n_pairs = len(bond_pairs)
        print(f"  Fallback identified {n_pairs} closest-pair groupings:")
        for k, bp in enumerate(bond_pairs):
            d = np.sqrt(sum((bp['cell_a'][i] - bp['cell_b'][i])**2 for i in range(3)))
            print(f"    [{k}] {tuple(bp['cell_a'])} ↔ {tuple(bp['cell_b'])}  d={d:.2f}",
                  flush=True)

    if n_pairs == 0:
        raise RuntimeError("Could not identify any bond-pairs — abort")

    # ─── Phase 4: recording window (per-step trajectory at bond-pair A-side port) ─
    print(f"  Recording window: capturing V_inc, V_ref at {n_pairs} bond-pairs' "
          f"A-side port {SAMPLE_PORT}...", flush=True)
    v_inc_traj = np.zeros((N_RECORDING_STEPS, n_pairs))
    v_ref_traj = np.zeros((N_RECORDING_STEPS, n_pairs))

    for i in range(N_RECORDING_STEPS):
        engine.step()
        v_inc = np.asarray(engine.k4.V_inc)
        v_ref = np.asarray(engine.k4.V_ref)
        for k, bp in enumerate(bond_pairs):
            ix, iy, iz = bp["cell_a"]
            port = bp["port"]
            v_inc_traj[i, k] = v_inc[ix, iy, iz, port]
            v_ref_traj[i, k] = v_ref[ix, iy, iz, port]
        if (time.time() - last_progress) > 30.0:
            t_period = (SELECTION_END_STEP + i) * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  elapsed {time.time()-t0:.1f}s",
                  flush=True)
            last_progress = time.time()

    elapsed_total = time.time() - t0
    print(f"  Recording done; total elapsed {elapsed_total:.1f}s", flush=True)

    # ─── Phase 5: per-bond ellipse + Hilbert chirality ──────────────────────
    print()
    print("=" * 78, flush=True)
    print("  Per-bond ellipse + Hilbert chirality")
    print("=" * 78, flush=True)

    bond_results = []
    for k in range(n_pairs):
        R_phase, r_phase = fit_ellipse_pca(v_inc_traj[:, k], v_ref_traj[:, k])
        R_over_r = R_phase / max(r_phase, 1e-30)
        mean_sin, std_sin, chirality_sign = chirality_hilbert(
            v_inc_traj[:, k], v_ref_traj[:, k])
        chir_label = "CCW" if chirality_sign > 0 else "CW" if chirality_sign < 0 else "AMBIG"
        bond_results.append({
            **bond_pairs[k],
            "R_phase": R_phase,
            "r_phase": r_phase,
            "R_over_r": R_over_r,
            "chirality_mean_sin_dphi": mean_sin,
            "chirality_std_sin_dphi": std_sin,
            "chirality_sign": chirality_sign,
            "chirality_label": chir_label,
        })
        print(f"  [{k}] {tuple(bond_pairs[k]['cell_a'])} → "
              f"{tuple(bond_pairs[k]['cell_b'])}  "
              f"R/r={R_over_r:8.4f}  chirality={chir_label} "
              f"(mean(sin Δφ)={mean_sin:+.3e}, std/|mean|="
              f"{std_sin/max(abs(mean_sin), 1e-30):.2f})", flush=True)

    # ─── Phase 6: per-cluster adjudication ──────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  Per-cluster adjudication")
    print("=" * 78, flush=True)

    lattice_center = (engine.k4.nx - 1) / 2.0
    clusters = cluster_bond_pairs(bond_pairs, lattice_center)
    print(f"  Lattice center: {lattice_center:.1f}")
    print(f"  Clusters: {dict((k, len(v)) for k, v in clusters.items())}")

    cluster_adjudication = {}
    for cluster_key, bp_indices in clusters.items():
        cluster_R_over_r = [bond_results[i]["R_over_r"] for i in bp_indices]
        cluster_chirality = [bond_results[i]["chirality_sign"] for i in bp_indices]
        cluster_median_R_over_r = float(np.median(cluster_R_over_r))
        n_ccw = sum(1 for s in cluster_chirality if s > 0)
        n_cw = sum(1 for s in cluster_chirality if s < 0)
        n_ambig = sum(1 for s in cluster_chirality if s == 0)
        consensus = max(n_ccw, n_cw)
        consensus_fraction = consensus / max(len(cluster_chirality), 1)
        consensus_dir = ("CCW" if n_ccw > n_cw else "CW" if n_cw > n_ccw
                         else "TIE")

        c1_pass = abs(cluster_median_R_over_r - PHI_SQ) <= PHI_SQ_TOL * PHI_SQ
        c2_pass = consensus_fraction >= CHIRALITY_CONSISTENCY_THRESHOLD

        cluster_adjudication[cluster_key] = {
            "n_bonds": len(bp_indices),
            "median_R_over_r": cluster_median_R_over_r,
            "consensus_fraction": consensus_fraction,
            "consensus_direction": consensus_dir,
            "n_ccw": n_ccw, "n_cw": n_cw, "n_ambig": n_ambig,
            "c1_pass": c1_pass,
            "c2_pass": c2_pass,
            "bond_indices": bp_indices,
        }
        print(f"  Cluster {cluster_key} ({len(bp_indices)} bonds):")
        print(f"    median R/r = {cluster_median_R_over_r:.4f} (target {PHI_SQ:.4f}±5%) → "
              f"C1 {'PASS' if c1_pass else 'FAIL'}")
        print(f"    chirality = {consensus} of {len(bp_indices)} ({consensus_fraction:.0%}) "
              f"{consensus_dir} → C2 {'PASS' if c2_pass else 'FAIL'}")

    # Cross-cluster chirality consistency (electron's substrate-fossilized
    # chirality should be SAME across clusters within one electron object)
    cluster_dirs = [a["consensus_direction"] for a in cluster_adjudication.values()
                    if a["consensus_direction"] in ("CCW", "CW")]
    cross_cluster_consistent = (len(set(cluster_dirs)) == 1) if cluster_dirs else False

    # ─── Persistence guard ──────────────────────────────────────────────────
    omega_final = np.asarray(engine.cos.omega)
    omega_peak_final = float(np.linalg.norm(omega_final, axis=-1).max())
    persistence = omega_peak_final / max(omega_peak_init, 1e-30)
    persistence_ok = persistence >= PERSISTENCE_GUARD

    # ─── Mode adjudication ──────────────────────────────────────────────────
    all_c1_pass = all(a["c1_pass"] for a in cluster_adjudication.values())
    all_c2_pass = all(a["c2_pass"] for a in cluster_adjudication.values())

    if all_c1_pass and all_c2_pass and cross_cluster_consistent:
        mode = "I"
        verdict = (
            f"MODE I — POSITIVE L3 CLOSURE. All clusters PASS C1 (R/r=φ²±5%) AND "
            f"C2 (chirality ≥75%), AND cross-cluster chirality consistent. "
            f"Lemniscate-with-twist bond-pair object class empirically confirmed. "
            f"L3 branch closes positive at canonical doc 79_ §1 framing."
        )
    elif all_c1_pass and not all_c2_pass:
        mode = "II-chirality"
        verdict = (
            f"MODE II-chirality — R/r matches φ² across clusters but chirality "
            f"inconsistent. Closed ellipse at right aspect, not coherent vortex."
        )
    elif not all_c1_pass and all_c2_pass:
        mode = "II-aspect"
        verdict = (
            f"MODE II-aspect — chirality consistent but R/r ≠ φ². Stable phasor "
            f"with chirality at non-corpus aspect; characterize-as-itself per Rule 10."
        )
    elif any(a["c1_pass"] for a in cluster_adjudication.values()) != all_c1_pass:
        mode = "III-asymmetric"
        verdict = (
            f"MODE III-asymmetric — clusters diverge: some pass C1, others fail. "
            f"Genuinely bipolar substrate response; needs separate physical "
            f"explanation. NOT a clean L3 closure either way."
        )
    else:
        mode = "III"
        verdict = (
            f"MODE III — NEGATIVE L3 CLOSURE. C1+C2 fail across clusters. "
            f"Bond-pair lemniscate framing also fails. Either substrate doesn't "
            f"host (2,q) at engine-representable scale, deeper reframe needed, "
            f"or engine V·S/T·1 implementation gap is load-bearing."
        )

    if not persistence_ok:
        verdict += (
            f" CAVEAT: peak |ω| persistence {persistence:.0%} below "
            f"{PERSISTENCE_GUARD:.0%} threshold."
        )

    print()
    print("=" * 78, flush=True)
    print("  Final adjudication")
    print("=" * 78, flush=True)
    print(f"  Cross-cluster chirality consistent: {cross_cluster_consistent}")
    print(f"  Persistence: {persistence:.0%} (guard {PERSISTENCE_GUARD:.0%}: "
          f"{'OK' if persistence_ok else 'VIOLATED'})")
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase9_path_alpha",
        "test": "Round 9 path α: bond-pair (V_inc, V_ref) phasor on Move 5 fresh attractor with methodology fixes",
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
        "sample_port": SAMPLE_PORT,
        "elapsed_seconds": elapsed_total,
        "omega_peak_init": omega_peak_init,
        "omega_peak_final": omega_peak_final,
        "persistence": persistence,
        "persistence_guard": PERSISTENCE_GUARD,
        "persistence_ok": bool(persistence_ok),
        "n_bond_pairs": n_pairs,
        "bond_results": bond_results,
        "cluster_adjudication": cluster_adjudication,
        "cross_cluster_chirality_consistent": cross_cluster_consistent,
        "phi_sq_target": PHI_SQ,
        "phi_sq_tolerance": PHI_SQ_TOL,
        "consensus_threshold": CHIRALITY_CONSISTENCY_THRESHOLD,
        "all_c1_pass": all_c1_pass,
        "all_c2_pass": all_c2_pass,
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
