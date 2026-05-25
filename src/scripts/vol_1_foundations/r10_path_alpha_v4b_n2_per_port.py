"""r10_path_alpha_v4b_n2_per_port.py — Round 10+ Phase 1 path α v4b.

Pre-reg P_phase11_path_alpha_v4b_n2_per_port. Auditor-recommended cheaper
diagnostic BEFORE substrate-native seed reform. Disambiguates path α v4's
LH-internal Δ=23% as statistical noise vs real substrate asymmetry.

Setup IDENTICAL to path α v4 (commit 2a684a4) except: top-2 bonds per port
instead of top-1, giving 8 bonds total (2 each at ports 0/1/2/3). Computes
within-port-spread for each chirality pair (RH = ports 0+2; LH = ports 1+3).

Adjudication:
- Mode I-noise: RH-internal and LH-internal spreads comparable → v4's
  LH-Δ=23% was noise; substrate-native seed reform is solving a non-problem
- Mode II-real-asymmetry: RH-internal stays tight (Δ < 5%) but LH-internal
  spreads (Δ > 15%) → real substrate property
- Mode III: pattern doesn't fit cleanly
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.signal import hilbert

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D


# ─── Constants (matching path α v4 exactly) ───────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

RECORDING_END_P_ABSOLUTE = 200.0
SELECTION_END_P = 15.0
N_RECORDING_STEPS = int((RECORDING_END_P_ABSOLUTE - SELECTION_END_P) * COMPTON_PERIOD / DT)

PORT_OFFSETS = [
    (1, 1, 1),     # port 0 — RH
    (1, -1, -1),   # port 1 — LH
    (-1, 1, -1),   # port 2 — RH
    (-1, -1, 1),   # port 3 — LH
]
PORT_CHIRALITY = ["RH", "LH", "RH", "LH"]
SQRT_3 = np.sqrt(3.0)

N_PER_PORT = 2  # KEY DIFFERENCE from v4

# Adjudication thresholds
WITHIN_PAIR_TIGHT_THRESHOLD = 0.05    # < 5% = tight
WITHIN_PAIR_SPREAD_THRESHOLD = 0.15   # > 15% = spread
RATIO_DIVERGENCE_THRESHOLD = 0.20

REPO_ROOT = Path(__file__).resolve().parents[3]
CACHED_STATE_PATH = REPO_ROOT / "data" / "move5_attractor_15p.npz"
OUTPUT_JSON = Path(__file__).parent / "r10_path_alpha_v4b_n2_per_port_results.json"


def fit_ellipsoid_pca_3d(omega_traj):
    points = omega_traj - omega_traj.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    e0 = float(max(eigvals[0], 1e-30))
    e1 = float(max(eigvals[1], 1e-30))
    e2 = float(max(eigvals[2], 1e-30))
    a0 = float(np.sqrt(e0))
    a1 = float(np.sqrt(e1))
    a2 = float(np.sqrt(e2))
    planarity = a0 / max(a2, 1e-30)
    in_plane_aspect = a2 / max(a1, 1e-30)
    return e0, e1, e2, a0, a1, a2, planarity, in_plane_aspect


def fit_ellipse_pca_2d(x_traj, y_traj):
    points = np.column_stack([x_traj, y_traj])
    points = points - points.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    r_phase = float(np.sqrt(max(eigvals[0], 1e-30)))
    R_phase = float(np.sqrt(max(eigvals[1], 1e-30)))
    return R_phase, r_phase


def chirality_hilbert(x_traj, y_traj):
    x = np.asarray(x_traj) - np.mean(x_traj)
    y = np.asarray(y_traj) - np.mean(y_traj)
    if np.std(x) < 1e-12 or np.std(y) < 1e-12:
        return 0.0, 0.0, 0
    xa = hilbert(x)
    ya = hilbert(y)
    delta_phi = np.angle(xa) - np.angle(ya)
    sin_delta = np.sin(delta_phi)
    mean_sin = float(np.mean(sin_delta))
    std_sin = float(np.std(sin_delta))
    if abs(mean_sin) < 0.1 * (std_sin + 1e-12):
        return mean_sin, std_sin, 0
    return mean_sin, std_sin, int(np.sign(mean_sin))


def make_interior_mask(nx, pml):
    mask = np.zeros((nx, nx, nx), dtype=bool)
    mask[pml:nx - pml, pml:nx - pml, pml:nx - pml] = True
    return mask


def find_top_n_bonds_per_port(engine, interior_mask, n_per_port):
    """For each of the 4 ports, find top-n cells by |V_inc[port]|² in interior."""
    bonds = []
    v_inc = np.asarray(engine.k4.V_inc)
    for port_idx in range(4):
        v_sq = v_inc[..., port_idx] ** 2
        v_sq_interior = v_sq.copy()
        v_sq_interior[~interior_mask] = 0.0
        flat = v_sq_interior.ravel()
        # argpartition for top-n
        top_idx = np.argpartition(flat, -n_per_port)[-n_per_port:]
        top_idx_sorted = top_idx[np.argsort(-flat[top_idx])]
        for rank, idx in enumerate(top_idx_sorted):
            ix, iy, iz = np.unravel_index(idx, v_sq_interior.shape)
            cell_a = (int(ix), int(iy), int(iz))
            offset = PORT_OFFSETS[port_idx]
            cell_b = (cell_a[0] + offset[0], cell_a[1] + offset[1], cell_a[2] + offset[2])
            b_hat = (offset[0] / SQRT_3, offset[1] / SQRT_3, offset[2] / SQRT_3)
            bonds.append({
                "port": port_idx,
                "rank": rank,
                "chirality_label": PORT_CHIRALITY[port_idx],
                "cell_a": list(cell_a),
                "cell_b": list(cell_b),
                "offset": list(offset),
                "b_hat": list(b_hat),
                "v_inc_sq_at_a": float(v_sq_interior[cell_a]),
            })
    return bonds


def main():
    print("=" * 78, flush=True)
    print("  r10 path α v4b — n=2-per-port test (LH-internal noise vs real)")
    print("  P_phase11_path_alpha_v4b_n2_per_port")
    print("=" * 78, flush=True)
    print(f"  Cached state: {CACHED_STATE_PATH.relative_to(REPO_ROOT)}")
    print(f"  Bond-pair selection: top-{N_PER_PORT} per port "
          f"({4 * N_PER_PORT} bonds total)")
    print()

    # ─── Phase 1: load cached state ────────────────────────────────────────
    print("Phase 1 — Load Move 5 cached state at t=15P", flush=True)
    if not CACHED_STATE_PATH.exists():
        raise RuntimeError(f"Cached state not found at {CACHED_STATE_PATH}.")
    engine = VacuumEngine3D.load(CACHED_STATE_PATH)
    print(f"  Loaded engine at t={engine.time:.4f}", flush=True)
    print()

    # ─── Phase 2: bond-pair selection ─────────────────────────────────────
    print(f"Phase 2 — Top-{N_PER_PORT} bonds per port", flush=True)
    interior_mask = make_interior_mask(engine.k4.nx, PML)
    bonds = find_top_n_bonds_per_port(engine, interior_mask, N_PER_PORT)
    for bond in bonds:
        print(f"  port {bond['port']} rank{bond['rank']} ({bond['chirality_label']}): "
              f"cell_a={tuple(bond['cell_a'])}, |V|²={bond['v_inc_sq_at_a']:.4e}",
              flush=True)
    print()

    # ─── Phase 3: recording window ─────────────────────────────────────────
    print(f"Phase 3 — Recording {N_RECORDING_STEPS} steps...", flush=True)
    n_bonds = len(bonds)
    phi_link_traj = np.zeros((N_RECORDING_STEPS, n_bonds))
    omega_xyz_traj = np.zeros((N_RECORDING_STEPS, n_bonds, 3))
    t0 = time.time()
    last = t0
    for i in range(N_RECORDING_STEPS):
        engine.step()
        phi_link = np.asarray(engine.k4.Phi_link)
        omega = np.asarray(engine.cos.omega)
        for k, bond in enumerate(bonds):
            ix, iy, iz = bond["cell_a"]
            port = bond["port"]
            phi_link_traj[i, k] = phi_link[ix, iy, iz, port]
            omega_xyz_traj[i, k, :] = omega[ix, iy, iz]
        if (time.time() - last) > 30.0:
            t_p = (i * DT) / COMPTON_PERIOD + SELECTION_END_P
            print(f"    [progress] step {i}/{N_RECORDING_STEPS}, t≈{t_p:.1f}P, "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()
    elapsed_recording = time.time() - t0
    print(f"  Recording done at {elapsed_recording:.1f}s", flush=True)
    print()

    # ─── Phase 4: per-bond PCA ─────────────────────────────────────────────
    print("=" * 78, flush=True)
    print("  Per-bond ω-orbit PCA + chirality")
    print("=" * 78, flush=True)
    bond_results = []
    for k, bond in enumerate(bonds):
        omega_k = omega_xyz_traj[:, k, :]
        e0, e1, e2, a0, a1, a2, planarity, aspect = fit_ellipsoid_pca_3d(omega_k)
        omega_mag = np.linalg.norm(omega_k, axis=1)
        R_mag, r_mag = fit_ellipse_pca_2d(phi_link_traj[:, k], omega_mag)
        mean_sin, std_sin, chir_sign = chirality_hilbert(phi_link_traj[:, k], omega_mag)
        chir_label = ("CCW" if chir_sign > 0 else "CW" if chir_sign < 0 else "AMBIG")
        bond_results.append({
            **bond,
            "eigvals": [e0, e1, e2],
            "planarity": planarity,
            "aspect_e2_e1": aspect,
            "phi_omega_mag_R_over_r": R_mag / max(r_mag, 1e-30),
            "phi_omega_mag_chirality_sign": chir_sign,
            "phi_omega_mag_chirality_label": chir_label,
            "phi_omega_mag_mean_sin": mean_sin,
        })
        print(f"  port {bond['port']} rank{bond['rank']} ({bond['chirality_label']}): "
              f"aspect={aspect:.4f}, planarity={planarity:.4f}, "
              f"chir={chir_label} (mean_sin={mean_sin:+.4f})")
    print()

    # ─── Phase 5: within-pair + cross-port adjudication ────────────────────
    print("=" * 78, flush=True)
    print("  Within-pair spread + cross-pair comparison")
    print("=" * 78, flush=True)

    rh_aspects = [b["aspect_e2_e1"] for b in bond_results if b["chirality_label"] == "RH"]
    lh_aspects = [b["aspect_e2_e1"] for b in bond_results if b["chirality_label"] == "LH"]
    rh_planarities = [b["planarity"] for b in bond_results if b["chirality_label"] == "RH"]
    lh_planarities = [b["planarity"] for b in bond_results if b["chirality_label"] == "LH"]

    def relative_spread(values):
        if not values:
            return float("nan")
        m = float(np.mean(values))
        if abs(m) < 1e-30:
            return float("nan")
        return float(np.std(values)) / abs(m)

    def max_min_spread(values):
        if not values:
            return float("nan")
        m = float(np.mean(values))
        if abs(m) < 1e-30:
            return float("nan")
        return (float(np.max(values)) - float(np.min(values))) / abs(m)

    rh_internal_std = relative_spread(rh_aspects)
    lh_internal_std = relative_spread(lh_aspects)
    rh_internal_maxmin = max_min_spread(rh_aspects)
    lh_internal_maxmin = max_min_spread(lh_aspects)
    rh_mean = float(np.mean(rh_aspects))
    lh_mean = float(np.mean(lh_aspects))
    rh_lh_diff = abs(rh_mean - lh_mean) / max(0.5 * (rh_mean + lh_mean), 1e-30)

    print(f"  RH aspects (n={len(rh_aspects)}): {[f'{a:.4f}' for a in rh_aspects]}")
    print(f"    RH-internal std/mean: {rh_internal_std:.1%}")
    print(f"    RH-internal max-min:  {rh_internal_maxmin:.1%}")
    print(f"    RH mean: {rh_mean:.4f}")
    print(f"  LH aspects (n={len(lh_aspects)}): {[f'{a:.4f}' for a in lh_aspects]}")
    print(f"    LH-internal std/mean: {lh_internal_std:.1%}")
    print(f"    LH-internal max-min:  {lh_internal_maxmin:.1%}")
    print(f"    LH mean: {lh_mean:.4f}")
    print(f"  RH-vs-LH mean divergence: {rh_lh_diff:.1%}")
    print()

    # Adjudication
    rh_tight = rh_internal_maxmin < WITHIN_PAIR_TIGHT_THRESHOLD
    lh_tight = lh_internal_maxmin < WITHIN_PAIR_TIGHT_THRESHOLD
    rh_spread = rh_internal_maxmin > WITHIN_PAIR_SPREAD_THRESHOLD
    lh_spread = lh_internal_maxmin > WITHIN_PAIR_SPREAD_THRESHOLD

    if rh_tight and lh_tight:
        mode = "I-both-tight"
        verdict = (
            f"Mode I-both-tight: RH-internal max-min={rh_internal_maxmin:.1%} "
            f"AND LH-internal max-min={lh_internal_maxmin:.1%}, both below "
            f"{WITHIN_PAIR_TIGHT_THRESHOLD:.0%} threshold. Path α v4's LH-Δ=23% "
            f"was statistical noise at n=1. Substrate-native seed reform is "
            f"solving a non-problem; original Cartesian-z seed acceptable."
        )
    elif rh_tight and lh_spread:
        mode = "II-real-asymmetry"
        verdict = (
            f"Mode II-real-asymmetry: RH-internal tight (max-min={rh_internal_maxmin:.1%}) "
            f"but LH-internal spread (max-min={lh_internal_maxmin:.1%}). Persistent "
            f"asymmetry between RH-pair and LH-pair internal coherence. Substrate-"
            f"native seed reform is candidate explanation; structural mechanism work "
            f"warranted."
        )
    elif rh_spread and lh_spread:
        mode = "I-both-spread"
        verdict = (
            f"Mode I-both-spread: RH-internal max-min={rh_internal_maxmin:.1%} AND "
            f"LH-internal max-min={lh_internal_maxmin:.1%}, both above "
            f"{WITHIN_PAIR_SPREAD_THRESHOLD:.0%}. Both pairs have spread; suggests "
            f"general statistical noise OR broader spatial-position-dependence; "
            f"the v4 RH-tight finding may have been coincidence at n=1."
        )
    else:
        mode = "III"
        verdict = (
            f"Mode III: pattern doesn't fit cleanly. RH-internal max-min="
            f"{rh_internal_maxmin:.1%}, LH-internal max-min={lh_internal_maxmin:.1%}. "
            f"Neither tight-tight nor tight-spread nor spread-spread."
        )

    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase11_path_alpha_v4b_n2_per_port",
        "test": "n=2-per-port disambiguation of v4 LH-internal Δ=23%",
        "n_per_port": N_PER_PORT,
        "n_bonds_total": n_bonds,
        "elapsed_recording_seconds": elapsed_recording,
        "bond_results": bond_results,
        "rh_aspects": rh_aspects,
        "lh_aspects": lh_aspects,
        "rh_internal_std_over_mean": rh_internal_std,
        "lh_internal_std_over_mean": lh_internal_std,
        "rh_internal_maxmin_relative": rh_internal_maxmin,
        "lh_internal_maxmin_relative": lh_internal_maxmin,
        "rh_mean_aspect": rh_mean,
        "lh_mean_aspect": lh_mean,
        "rh_lh_mean_divergence": rh_lh_diff,
        "thresholds": {
            "within_pair_tight": WITHIN_PAIR_TIGHT_THRESHOLD,
            "within_pair_spread": WITHIN_PAIR_SPREAD_THRESHOLD,
        },
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
