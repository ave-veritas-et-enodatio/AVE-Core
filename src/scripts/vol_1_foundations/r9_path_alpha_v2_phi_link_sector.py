"""r9_path_alpha_v2_phi_link_sector.py — Round 9 path α v2 per P_phase9_path_alpha_v2.

Doc 79_ v4.4 §8.3 path α v2 with corrected sampler. Path α v1 sampled
(V_inc, V_ref) — the LOCKED Compton-frequency channel per Move 11b
empirical (doc 75 §6.2 line 129 verbatim: "K4-capacitive (V_inc, V_ref)
is locked, K4-inductive (Φ_link) and Cosserat trade slowly"). The bound
state's actual dynamics live in (Φ_link, ω) trading channel at slow
~0.020 rad/unit per Move 11b FFT.

Per doc 75 line 140 verbatim: "the corpus electron, IF it exists in this
engine, lives somewhere we haven't probed (Φ_link sector / hybrid V≠0
∧ ω≠0 / different topology)."

Setup IDENTICAL to path α v1 (and Move 5). Methodology corrections:
1. Sampler: (Φ_link[A_bond, port], ω_axial = ω[A_node] · b_hat) at K4
   bond-pairs, NOT (V_inc, V_ref)
2. Recording window: [15, 200] P (extended from v1's [15, 50] P;
   spans ~3-4 trading periods at 0.020 rad/unit ≈ 50 P each)
3. Hilbert chirality on slow-trading signal (frequency ~0.020 rad/unit,
   period ~50 P, much slower than Compton ω_C = 1)
4. Per-cluster R/r adjudication (same as v1)

Dual-criterion (per cluster):
  C1: R_phase/r_phase = φ² ± 5% on (Φ_link, ω_axial) ellipse
  C2: chirality consensus ≥ 75% via Hilbert mean(sin(Δφ))
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


# ─── Constants (matching Move 5 + path α v1 exactly for engine setup) ──────

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

# ─── Path α v2 specific (NEW vs v1) ──────────────────────────────────────────
PRE_EVOLVE_END_P = 10.0          # transient settle (same as v1)
SELECTION_END_P = 15.0           # 5 P selection window (same as v1)
RECORDING_END_P = 200.0          # 185 P recording (~3-4 trading periods at 0.020 rad/unit)

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

# Adjudication thresholds (same as v1)
PHI_SQ_TOL = 0.05
CHIRALITY_CONSISTENCY_THRESHOLD = 0.75
PERSISTENCE_GUARD = 0.40  # relaxed from v1's 0.70 because v2 records over longer window where decay is expected

OUTPUT_JSON = Path(__file__).parent / "r9_path_alpha_v2_phi_link_sector_results.json"


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


def fit_ellipse_pca(x_traj, y_traj):
    """PCA on (x, y) point cloud → ellipse axes (R_phase, r_phase)."""
    points = np.column_stack([x_traj, y_traj])
    points = points - points.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    r_phase = float(np.sqrt(max(eigvals[0], 1e-30)))
    R_phase = float(np.sqrt(max(eigvals[1], 1e-30)))
    return R_phase, r_phase


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
    """K4 tetrahedral bond-pair identification (same as v1)."""
    bond_pairs = []
    used_cells = set()
    for cell_a in top_cells_list:
        if cell_a in used_cells:
            continue
        for port_idx, offset in enumerate(PORT_OFFSETS):
            cell_b = (cell_a[0] + offset[0], cell_a[1] + offset[1], cell_a[2] + offset[2])
            if cell_b in top_cells_set and cell_b not in used_cells:
                # Compute bond direction unit vector b_hat = offset / sqrt(3)
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
    print("  r9 PATH α v2 — Φ_link sector phasor (Op14 trading channel)")
    print("  P_phase9_path_alpha_v2")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, PML={PML} (interior {N_LATTICE - 2*PML}^3)")
    print(f"  Corpus GT: R={R_ANCHOR}, r={R_MINOR:.4f}")
    print(f"  Pre-evolve: t ∈ [0, {PRE_EVOLVE_END_P}] P")
    print(f"  Selection: t ∈ [{PRE_EVOLVE_END_P}, {SELECTION_END_P}] P "
          f"({N_SELECTION_STEPS} steps)")
    print(f"  Recording: t ∈ [{SELECTION_END_P}, {RECORDING_END_P}] P "
          f"({N_RECORDING_STEPS} steps)")
    print(f"  Sampler: (Φ_link[A_bond, port], ω_axial = ω · b_hat)")
    print(f"  Dual-criterion (per cluster):")
    print(f"    C1: R/r = φ²={PHI_SQ:.4f} ± {PHI_SQ_TOL:.0%}")
    print(f"    C2: chirality consensus ≥ {CHIRALITY_CONSISTENCY_THRESHOLD:.0%}")
    print()

    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    # Reset Phi_link to ensure clean accumulation from t=0
    engine.k4.reset_phi_link()

    omega_init = np.asarray(engine.cos.omega)
    omega_peak_init = float(np.linalg.norm(omega_init, axis=-1).max())
    assert A26_GUARD_LOW <= omega_peak_init <= A26_GUARD_HIGH
    print(f"  Initial peak |ω| = {omega_peak_init:.4f} (A26 guard OK)")

    # ─── Phase 1: pre-evolve ───────────────────────────────────────────────────
    print(f"  Pre-evolving to t={PRE_EVOLVE_END_P} P...", flush=True)
    t0 = time.time()
    last_progress = t0
    for step in range(PRE_EVOLVE_END_STEP):
        engine.step()
        if (time.time() - last_progress) > 30.0:
            print(f"    [progress] step={step}, elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()
    print(f"    pre-evolve done at {time.time()-t0:.1f}s", flush=True)

    # ─── Phase 2: cell selection (same as v1 — peak |V_inc[port 0]|² for cell ranking) ─
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
              f"B={tuple(bp['cell_b'])} (offset {offset}, b_hat={[f'{x:.3f}' for x in bp['b_hat']]})",
              flush=True)

    if n_pairs == 0:
        raise RuntimeError("No K4 bond-pairs found — abort")

    # ─── Phase 3: recording window (Φ_link + ω_axial trajectory) ────────────────
    print(f"  Recording window: capturing (Φ_link, ω_axial) at {n_pairs} bond-pairs...",
          flush=True)
    phi_link_traj = np.zeros((N_RECORDING_STEPS, n_pairs))
    omega_axial_traj = np.zeros((N_RECORDING_STEPS, n_pairs))

    for i in range(N_RECORDING_STEPS):
        engine.step()
        phi_link = np.asarray(engine.k4.Phi_link)
        omega = np.asarray(engine.cos.omega)
        for k, bp in enumerate(bond_pairs):
            ix, iy, iz = bp["cell_a"]
            port = bp["port"]
            b_hat = bp["b_hat"]
            phi_link_traj[i, k] = phi_link[ix, iy, iz, port]
            # ω_axial = ω · b_hat (signed projection onto bond direction)
            omega_vec = omega[ix, iy, iz]
            omega_axial_traj[i, k] = (
                omega_vec[0] * b_hat[0] + omega_vec[1] * b_hat[1] + omega_vec[2] * b_hat[2]
            )
        if (time.time() - last_progress) > 30.0:
            t_period = (SELECTION_END_STEP + i) * DT / COMPTON_PERIOD
            print(f"    [progress] t={t_period:6.1f} P  step {i}/{N_RECORDING_STEPS}  "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last_progress = time.time()

    elapsed_total = time.time() - t0
    print(f"  Recording done; total elapsed {elapsed_total:.1f}s", flush=True)

    # ─── Phase 4: per-bond ellipse + Hilbert chirality on (Φ_link, ω_axial) ──
    print()
    print("=" * 78, flush=True)
    print("  Per-bond (Φ_link, ω_axial) ellipse + Hilbert chirality")
    print("=" * 78, flush=True)

    bond_results = []
    for k in range(n_pairs):
        R_phase, r_phase = fit_ellipse_pca(phi_link_traj[:, k], omega_axial_traj[:, k])
        R_over_r = R_phase / max(r_phase, 1e-30)
        mean_sin, std_sin, chirality_sign = chirality_hilbert(
            phi_link_traj[:, k], omega_axial_traj[:, k]
        )
        chir_label = "CCW" if chirality_sign > 0 else "CW" if chirality_sign < 0 else "AMBIG"
        bond_results.append({
            **bond_pairs[k],
            "R_phase": R_phase,
            "r_phase": r_phase,
            "R_over_r": R_over_r,
            "phi_link_amplitude_std": float(np.std(phi_link_traj[:, k])),
            "omega_axial_amplitude_std": float(np.std(omega_axial_traj[:, k])),
            "chirality_mean_sin_dphi": mean_sin,
            "chirality_std_sin_dphi": std_sin,
            "chirality_sign": chirality_sign,
            "chirality_label": chir_label,
        })
        print(f"  [{k}] {tuple(bond_pairs[k]['cell_a'])} → "
              f"{tuple(bond_pairs[k]['cell_b'])}  "
              f"R/r={R_over_r:8.4f}  chirality={chir_label} "
              f"(σ_Φ={np.std(phi_link_traj[:, k]):.3e}, "
              f"σ_ω={np.std(omega_axial_traj[:, k]):.3e})", flush=True)

    # ─── Phase 5: per-cluster + global adjudication ──────────────────────────
    lattice_center = (engine.k4.nx - 1) / 2.0
    clusters = cluster_bond_pairs(bond_pairs, lattice_center)

    cluster_adjudication = {}
    for cluster_key, bp_indices in clusters.items():
        cluster_R_over_r = [bond_results[i]["R_over_r"] for i in bp_indices]
        cluster_chirality = [bond_results[i]["chirality_sign"] for i in bp_indices]
        cluster_median_R_over_r = float(np.median(cluster_R_over_r))
        n_ccw = sum(1 for s in cluster_chirality if s > 0)
        n_cw = sum(1 for s in cluster_chirality if s < 0)
        consensus = max(n_ccw, n_cw)
        consensus_fraction = consensus / max(len(cluster_chirality), 1)
        consensus_dir = "CCW" if n_ccw > n_cw else "CW" if n_cw > n_ccw else "TIE"
        c1_pass = abs(cluster_median_R_over_r - PHI_SQ) <= PHI_SQ_TOL * PHI_SQ
        c2_pass = consensus_fraction >= CHIRALITY_CONSISTENCY_THRESHOLD
        cluster_adjudication[cluster_key] = {
            "n_bonds": len(bp_indices),
            "median_R_over_r": cluster_median_R_over_r,
            "consensus_fraction": consensus_fraction,
            "consensus_direction": consensus_dir,
            "n_ccw": n_ccw, "n_cw": n_cw,
            "c1_pass": c1_pass, "c2_pass": c2_pass,
            "bond_indices": bp_indices,
        }

    cluster_dirs = [a["consensus_direction"] for a in cluster_adjudication.values()
                    if a["consensus_direction"] in ("CCW", "CW")]
    cross_cluster_consistent = (len(set(cluster_dirs)) == 1) if cluster_dirs else False

    omega_final = np.asarray(engine.cos.omega)
    omega_peak_final = float(np.linalg.norm(omega_final, axis=-1).max())
    persistence = omega_peak_final / max(omega_peak_init, 1e-30)
    persistence_ok = persistence >= PERSISTENCE_GUARD

    all_c1_pass = all(a["c1_pass"] for a in cluster_adjudication.values())
    all_c2_pass = all(a["c2_pass"] for a in cluster_adjudication.values())

    if all_c1_pass and all_c2_pass and cross_cluster_consistent:
        mode = "I"
        verdict = (
            f"MODE I — POSITIVE L3 CLOSURE in Φ_link trading sector. All clusters PASS "
            f"C1 (R/r=φ²±5%) AND C2 (chirality ≥75%) on (Φ_link, ω_axial) ellipse, AND "
            f"cross-cluster chirality consistent. Doc 75 line 140's prediction empirically "
            f"confirmed: corpus electron lives in the Φ_link sector. Lemniscate-with-twist + "
            f"Op14-mediated trading mechanism validated. L3 branch closes positive."
        )
    elif all_c1_pass and not all_c2_pass:
        mode = "II-chirality"
        verdict = (
            f"MODE II-chirality — R/r=φ² but chirality inconsistent in trading channel."
        )
    elif not all_c1_pass and all_c2_pass:
        mode = "II-aspect"
        verdict = (
            f"MODE II-aspect — chirality consistent but R/r ≠ φ² in trading channel."
        )
    elif any(a["c1_pass"] for a in cluster_adjudication.values()) != all_c1_pass:
        mode = "III-asymmetric"
        verdict = (
            f"MODE III-asymmetric — clusters diverge in trading channel."
        )
    else:
        mode = "III"
        verdict = (
            f"MODE III — Φ_link sector framing also fails. C1+C2 fail across clusters "
            f"on (Φ_link, ω_axial). Per doc 75 line 140 alternatives, deeper reframe "
            f"needed: hybrid V≠0 ∧ ω≠0 seed, different topology, or continuum-limit-only object."
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
        print(f"    median R/r = {adj['median_R_over_r']:.4f} (target {PHI_SQ:.4f}±5%) → "
              f"C1 {'PASS' if adj['c1_pass'] else 'FAIL'}")
        print(f"    chirality = {max(adj['n_ccw'], adj['n_cw'])} of {adj['n_bonds']} "
              f"({adj['consensus_fraction']:.0%}) {adj['consensus_direction']} → "
              f"C2 {'PASS' if adj['c2_pass'] else 'FAIL'}")
    print(f"  Cross-cluster chirality consistent: {cross_cluster_consistent}")
    print(f"  Persistence: {persistence:.0%}")
    print()
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase9_path_alpha_v2",
        "test": "Round 9 path α v2: (Φ_link, ω_axial) phasor on Move 5 saturated bond-pairs (Op14 trading channel)",
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
