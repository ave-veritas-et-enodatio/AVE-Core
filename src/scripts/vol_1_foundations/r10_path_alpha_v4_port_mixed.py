"""r10_path_alpha_v4_port_mixed.py — Round 10+ Phase 1 path α v4 port-mixed test.

Pre-reg P_phase11_path_alpha_v4_port_mixed. Resolves the 4:3:1 ω-orbit
asymmetry origin question that surfaced during Direction 3'.1 derivability
gate-decision dialogue.

KNOWN BUG flagged for follow-up (auditor catch on 2026-04-28 commit landing):
The auto-adjudication logic in main()'s Phase 5 has two issues:
  1. Required unanimous chirality (n_ccw == 4 OR n_cw == 4) for the
     "I-C4-symmetric" mode label — too strict. With 1 CCW + 3 AMBIG,
     this falls through to Mode III despite the aspect-ratio result
     being decisive on chirality-pairing falsification.
  2. Reported "cross-port aspect spread" via std/mean (coefficient of
     variation), which under-weights max-min when one chirality pair
     is tight and the other is spread. Honest reporting needs both
     std/mean AND max-min separately.
Fix in next implementer-lane pass: separate aspect-ratio adjudication
(use std/mean + max-min) from chirality adjudication (use per-port
robust-signal threshold + RH-vs-LH mirror check). Lands as P_phase11
amendment + driver fix; data already in this run's JSON output.

Honest mode label for THIS run per auditor catch:
  - Decisive on RH-vs-LH-mirror-asymmetry: FALSIFIED (RH-mean ≈ LH-mean,
    Δ = 1.5%). Bare TLM scatter+connect treats RH and LH ports
    equivalently in dynamics. Chirality pairing per k4_tlm.py:524 is
    DIAGNOSTIC only.
  - Open on full-port-equivalence: RH-pair tight (Δ = 0.024%) but
    LH-pair spread (Δ = 23%). Cause (statistical noise at n=1 vs
    real substrate asymmetry vs IC seed) unresolved.
  - Subsidiary finding: chirality detectability is port-0-specific.
    Path α v3 v5.1's "100% CCW partial positive" was port-0-sampling-
    only; not robust substrate fingerprint. Doc 79 v5.1 §7.6.4 needs
    Rule-12 addendum.

PATH α v3 BASELINE: 4 bonds all selected at port 0 → ω-orbit ratios e2:e1:e0
≈ 1.25:1:0.5 (variance), planarity 0.47-0.54. The asymmetry source unclear
from port-0-only sampling.

THIS TEST: pick 1 top-amplitude bond per port direction (4 bonds total, 1
each at port 0, 1, 2, 3). Compare ω-orbit ratios across the 4 ports.

USES PHASE 0.1 CACHED STATE: data/move5_attractor_15p.npz (commit 999d2ac).
Saves ~22s pre-evolve + selection overhead per run.

ADJUDICATION CATEGORIES (per pre-reg):
- Mode I-C4-symmetric: ratios consistent (within 10%) across 4 ports +
  chirality consistent across 4 ports → bare TLM C_4 confirmed; 4:3:1
  asymmetry from IC or sampling, NOT bare-TLM-chirality-pairing
- Mode I-chirality-mirror: same magnitudes, mirror chirality on RH vs LH
  ports → helicity sign-flip is only chirality effect; magnitudes
  C_4 symmetric
- Mode II-RH-LH-asymmetric: ratios differ between RH (0,2) and LH (1,3)
  → chirality-pairing creates dynamic asymmetry (would contradict
  auditor's framing of bare TLM C_4)
- Mode III: ratios differ unpredictably across all 4 ports → IC or
  sampling-specific
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


# ─── Constants (matching path α v3 + Move 5) ──────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

# Recording window (same as path α v3)
RECORDING_END_P_ABSOLUTE = 200.0
SELECTION_END_P = 15.0  # cached state was saved at this t
N_RECORDING_STEPS = int((RECORDING_END_P_ABSOLUTE - SELECTION_END_P) * COMPTON_PERIOD / DT)

# K4 tetrahedral port offsets (per k4_tlm.py:84-86)
PORT_OFFSETS = [
    (1, 1, 1),     # port 0 — RH (paired with port 2)
    (1, -1, -1),   # port 1 — LH (paired with port 3)
    (-1, 1, -1),   # port 2 — RH
    (-1, -1, 1),   # port 3 — LH
]
PORT_CHIRALITY = ["RH", "LH", "RH", "LH"]  # per k4_tlm.py:524
SQRT_3 = np.sqrt(3.0)

# Adjudication thresholds (per pre-reg)
RATIO_CONSISTENCY_THRESHOLD = 0.10   # within 10% relative variation = "consistent"
RATIO_DIVERGENCE_THRESHOLD = 0.20    # >20% RH-vs-LH = "divergent"
PHI_SQ_TOL = 0.05                    # for legacy φ² comparison
CHIRALITY_CONSISTENCY_THRESHOLD = 0.75

REPO_ROOT = Path(__file__).resolve().parents[3]
CACHED_STATE_PATH = REPO_ROOT / "data" / "move5_attractor_15p.npz"
OUTPUT_JSON = Path(__file__).parent / "r10_path_alpha_v4_port_mixed_results.json"


def fit_ellipsoid_pca_3d(omega_traj):
    """PCA on 3D ω-trajectory. Returns sorted eigenvalues e0 ≤ e1 ≤ e2."""
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
    """PCA on (x, y) point cloud → (R_phase, r_phase) ellipse axes."""
    points = np.column_stack([x_traj, y_traj])
    points = points - points.mean(axis=0)
    cov = np.cov(points.T)
    eigvals = np.sort(np.linalg.eigvalsh(cov))
    r_phase = float(np.sqrt(max(eigvals[0], 1e-30)))
    R_phase = float(np.sqrt(max(eigvals[1], 1e-30)))
    return R_phase, r_phase


def chirality_hilbert(x_traj, y_traj):
    """Hilbert-transform chirality. Returns (mean_sin_dphi, std, sign)."""
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


def find_top_bond_per_port(engine, interior_mask):
    """For each of the 4 ports, find the cell with maximum |V_inc[port]|² in
    the interior region. Returns list of 4 bond-pair dicts (one per port)."""
    bonds = []
    v_inc = np.asarray(engine.k4.V_inc)
    for port_idx in range(4):
        v_sq = v_inc[..., port_idx] ** 2
        v_sq_interior = v_sq.copy()
        v_sq_interior[~interior_mask] = 0.0

        flat_idx = int(np.argmax(v_sq_interior))
        ix, iy, iz = np.unravel_index(flat_idx, v_sq_interior.shape)
        cell_a = (int(ix), int(iy), int(iz))

        offset = PORT_OFFSETS[port_idx]
        cell_b = (cell_a[0] + offset[0], cell_a[1] + offset[1], cell_a[2] + offset[2])
        b_hat = (offset[0] / SQRT_3, offset[1] / SQRT_3, offset[2] / SQRT_3)

        bonds.append({
            "port": port_idx,
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
    print("  r10 path α v4 — port-mixed bond-pair test")
    print("  P_phase11_path_alpha_v4_port_mixed")
    print("=" * 78, flush=True)
    print(f"  Cached state: {CACHED_STATE_PATH.relative_to(REPO_ROOT)}")
    print(f"  Lattice: N={N_LATTICE}, PML={PML}")
    print(f"  Recording: {SELECTION_END_P} → {RECORDING_END_P_ABSOLUTE} P "
          f"({N_RECORDING_STEPS} steps, ~5 min wall)")
    print(f"  Bond-pair selection: top |V_inc[port_i]|² per port "
          f"(4 bonds, 1 per port direction)")
    print()
    print(f"  K4 port chirality (per k4_tlm.py:524):")
    for p in range(4):
        offset = PORT_OFFSETS[p]
        print(f"    port {p}: offset {offset}, chirality {PORT_CHIRALITY[p]}", flush=True)
    print()

    # ─── Phase 1: load cached state ────────────────────────────────────────
    print("Phase 1 — Load Move 5 cached state at t=15P", flush=True)
    if not CACHED_STATE_PATH.exists():
        raise RuntimeError(
            f"Cached state not found at {CACHED_STATE_PATH}. "
            f"Run r10_save_move5_state.py first to regenerate."
        )
    engine = VacuumEngine3D.load(CACHED_STATE_PATH)
    print(f"  Loaded engine at t={engine.time:.4f}, N={engine.N}")
    omega_peak_at_load = float(np.linalg.norm(engine.cos.omega, axis=-1).max())
    v_inc_l2 = float(np.linalg.norm(engine.k4.V_inc))
    print(f"  Loaded state: peak |ω|={omega_peak_at_load:.4f}, "
          f"||V_inc||_2={v_inc_l2:.4e}")
    print()

    # ─── Phase 2: select 1 bond per port at top |V_inc[port]|² ────────────
    print("Phase 2 — Port-mixed bond-pair selection (top-1 per port)", flush=True)
    interior_mask = make_interior_mask(engine.k4.nx, PML)
    bonds = find_top_bond_per_port(engine, interior_mask)
    for bond in bonds:
        print(f"  port {bond['port']} ({bond['chirality_label']}): "
              f"cell_a={tuple(bond['cell_a'])}, cell_b={tuple(bond['cell_b'])}, "
              f"|V_inc|²={bond['v_inc_sq_at_a']:.4e}", flush=True)
    print()

    # ─── Phase 3: recording window ─────────────────────────────────────────
    print(f"Phase 3 — Recording {N_RECORDING_STEPS} steps "
          f"(t={SELECTION_END_P}P → {RECORDING_END_P_ABSOLUTE}P)...", flush=True)
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
            t_period = (i + N_RECORDING_STEPS * 0) * DT / COMPTON_PERIOD + SELECTION_END_P
            print(f"    [progress] step {i}/{N_RECORDING_STEPS}, "
                  f"t≈{t_period:.1f}P, elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()
    elapsed_recording = time.time() - t0
    print(f"  Recording done at {elapsed_recording:.1f}s", flush=True)
    print()

    # ─── Phase 4: per-port ω-orbit PCA + chirality diagnostics ────────────
    print("=" * 78, flush=True)
    print("  Per-port ω-orbit PCA + chirality on (Φ_link, |ω|)")
    print("=" * 78, flush=True)
    bond_results = []
    for k, bond in enumerate(bonds):
        omega_k = omega_xyz_traj[:, k, :]
        e0, e1, e2, a0, a1, a2, planarity, aspect_e2_e1 = fit_ellipsoid_pca_3d(omega_k)

        # chirality on (Φ_link, |ω|)
        omega_mag = np.linalg.norm(omega_k, axis=1)
        R_mag, r_mag = fit_ellipse_pca_2d(phi_link_traj[:, k], omega_mag)
        R_over_r_mag = R_mag / max(r_mag, 1e-30)
        mean_sin_mag, std_sin_mag, chirality_sign_mag = chirality_hilbert(
            phi_link_traj[:, k], omega_mag
        )
        chir_label_mag = ("CCW" if chirality_sign_mag > 0
                          else "CW" if chirality_sign_mag < 0 else "AMBIG")

        bond_results.append({
            **bond,
            "eigvals_sorted": [e0, e1, e2],
            "axis_lengths": [a0, a1, a2],
            "planarity_e0_over_e2": planarity,
            "aspect_e2_over_e1": aspect_e2_e1,
            "ratio_e2_e1_e0": [e2 / max(e0, 1e-30), e1 / max(e0, 1e-30), 1.0],
            "phi_omega_mag_R_over_r": R_over_r_mag,
            "phi_omega_mag_chirality_sign": chirality_sign_mag,
            "phi_omega_mag_chirality_label": chir_label_mag,
            "phi_omega_mag_mean_sin": mean_sin_mag,
        })
        print(f"  port {bond['port']} ({bond['chirality_label']}):")
        print(f"    eigvals e0:e1:e2 = {e0:.5f} : {e1:.5f} : {e2:.5f}")
        print(f"    ratio e2/e0 : e1/e0 : 1 = "
              f"{e2/max(e0,1e-30):.3f} : {e1/max(e0,1e-30):.3f} : 1.000")
        print(f"    planarity (e0/e2) = {planarity:.4f}, "
              f"aspect (e2/e1) = {aspect_e2_e1:.4f}")
        print(f"    (Φ_link, |ω|) chirality: {chir_label_mag} "
              f"(mean_sin={mean_sin_mag:+.4f})")
        print()

    # ─── Phase 5: cross-port comparison ────────────────────────────────────
    print("=" * 78, flush=True)
    print("  Cross-port comparison (RH = ports 0+2; LH = ports 1+3)")
    print("=" * 78, flush=True)

    # Group by chirality
    rh_bonds = [b for b in bond_results if b["chirality_label"] == "RH"]
    lh_bonds = [b for b in bond_results if b["chirality_label"] == "LH"]

    def group_stats(bonds_subset, key_path):
        """Mean + std of nested key path across bonds_subset."""
        values = []
        for b in bonds_subset:
            v = b
            for k in key_path:
                v = v[k]
            values.append(v)
        if not values:
            return float("nan"), float("nan"), 0
        return float(np.mean(values)), float(np.std(values)), len(values)

    # Aspect ratios e2/e1 per port
    aspects = [b["aspect_e2_over_e1"] for b in bond_results]
    planarities = [b["planarity_e0_over_e2"] for b in bond_results]

    aspect_rh_mean, aspect_rh_std, _ = group_stats(rh_bonds, ["aspect_e2_over_e1"])
    aspect_lh_mean, aspect_lh_std, _ = group_stats(lh_bonds, ["aspect_e2_over_e1"])
    planarity_rh_mean, _, _ = group_stats(rh_bonds, ["planarity_e0_over_e2"])
    planarity_lh_mean, _, _ = group_stats(lh_bonds, ["planarity_e0_over_e2"])

    # Cross-port consistency: relative spread across all 4 ports
    aspect_mean_all = float(np.mean(aspects))
    aspect_std_all = float(np.std(aspects))
    aspect_relative_spread = aspect_std_all / max(abs(aspect_mean_all), 1e-30)

    # RH vs LH divergence
    rh_lh_aspect_diff = abs(aspect_rh_mean - aspect_lh_mean) / max(
        0.5 * (abs(aspect_rh_mean) + abs(aspect_lh_mean)), 1e-30
    )

    # Chirality
    chir_signs = [b["phi_omega_mag_chirality_sign"] for b in bond_results]
    n_ccw = sum(1 for s in chir_signs if s > 0)
    n_cw = sum(1 for s in chir_signs if s < 0)
    n_ambig = sum(1 for s in chir_signs if s == 0)

    rh_chir = [b["phi_omega_mag_chirality_sign"] for b in rh_bonds]
    lh_chir = [b["phi_omega_mag_chirality_sign"] for b in lh_bonds]
    rh_n_ccw = sum(1 for s in rh_chir if s > 0)
    rh_n_cw = sum(1 for s in rh_chir if s < 0)
    lh_n_ccw = sum(1 for s in lh_chir if s > 0)
    lh_n_cw = sum(1 for s in lh_chir if s < 0)

    # Adjudication
    consistent_ratios = aspect_relative_spread < RATIO_CONSISTENCY_THRESHOLD
    divergent_RH_LH = rh_lh_aspect_diff > RATIO_DIVERGENCE_THRESHOLD
    consistent_chirality = (n_ccw == 4) or (n_cw == 4)
    mirror_chirality = (rh_n_ccw == 2 and lh_n_cw == 2) or (rh_n_cw == 2 and lh_n_ccw == 2)

    if consistent_ratios and consistent_chirality:
        mode = "I-C4-symmetric"
        verdict = (
            f"Mode I-C4-symmetric: ratios consistent across 4 ports "
            f"(spread {aspect_relative_spread:.1%} < {RATIO_CONSISTENCY_THRESHOLD:.0%}) "
            f"AND chirality consistent ({'CCW' if n_ccw == 4 else 'CW'} 4/4). "
            f"Bare TLM C_4 symmetry confirmed. 4:3:1 asymmetry source is NOT "
            f"chirality-pairing-in-bare-TLM; must be IC seed asymmetry, "
            f"sampling artifact, or Cosserat self-coupling."
        )
    elif consistent_ratios and mirror_chirality:
        mode = "I-chirality-mirror"
        verdict = (
            f"Mode I-chirality-mirror: ratios consistent across 4 ports "
            f"(spread {aspect_relative_spread:.1%}) BUT chirality mirror "
            f"between RH and LH (RH: {rh_n_ccw} CCW + {rh_n_cw} CW; "
            f"LH: {lh_n_ccw} CCW + {lh_n_cw} CW). Bipartite helicity "
            f"sign-flip is the only chirality dynamic effect; magnitudes "
            f"are C_4 symmetric."
        )
    elif divergent_RH_LH:
        mode = "II-RH-LH-asymmetric"
        verdict = (
            f"Mode II-RH-LH-asymmetric: RH-saturated (mean aspect "
            f"{aspect_rh_mean:.4f}) vs LH-saturated (mean {aspect_lh_mean:.4f}) "
            f"diverge by {rh_lh_aspect_diff:.1%} > {RATIO_DIVERGENCE_THRESHOLD:.0%}. "
            f"Chirality-pairing creates dynamic asymmetry — contradicts "
            f"auditor's framing of bare-TLM C_4 symmetry. Substrate "
            f"understanding needs revision."
        )
    else:
        mode = "III"
        verdict = (
            f"Mode III: ratios spread irregularly across all 4 ports "
            f"(aspect spread {aspect_relative_spread:.1%}, RH/LH diff "
            f"{rh_lh_aspect_diff:.1%}); chirality {n_ccw} CCW + {n_cw} CW + "
            f"{n_ambig} AMBIG. No clean pattern; IC or sampling-specific."
        )

    print(f"  Aspect e2/e1 per port: {[f'{a:.4f}' for a in aspects]}")
    print(f"  Planarity per port:   {[f'{p:.4f}' for p in planarities]}")
    print(f"  Cross-port aspect spread: {aspect_relative_spread:.1%} "
          f"(< {RATIO_CONSISTENCY_THRESHOLD:.0%} = consistent)")
    print(f"  RH mean aspect: {aspect_rh_mean:.4f} ± {aspect_rh_std:.4f}")
    print(f"  LH mean aspect: {aspect_lh_mean:.4f} ± {aspect_lh_std:.4f}")
    print(f"  RH/LH aspect divergence: {rh_lh_aspect_diff:.1%} "
          f"(> {RATIO_DIVERGENCE_THRESHOLD:.0%} = divergent)")
    print(f"  Chirality counts: {n_ccw} CCW + {n_cw} CW + {n_ambig} AMBIG (of 4)")
    print(f"  RH chirality: {rh_n_ccw} CCW + {rh_n_cw} CW (of 2)")
    print(f"  LH chirality: {lh_n_ccw} CCW + {lh_n_cw} CW (of 2)")
    print()
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    # ─── Phase 6: write JSON ───────────────────────────────────────────────
    payload = {
        "pre_registration": "P_phase11_path_alpha_v4_port_mixed",
        "test": "Round 10+ Phase 1 path α v4 port-mixed: 1 bond per port direction",
        "cached_state_source": str(CACHED_STATE_PATH.relative_to(REPO_ROOT)),
        "N": N_LATTICE,
        "PML": PML,
        "R": R_ANCHOR,
        "r": R_MINOR,
        "selection_end_p": SELECTION_END_P,
        "recording_end_p_absolute": RECORDING_END_P_ABSOLUTE,
        "n_recording_steps": N_RECORDING_STEPS,
        "elapsed_recording_seconds": elapsed_recording,
        "omega_peak_at_load": omega_peak_at_load,
        "n_bonds": n_bonds,
        "bond_results": bond_results,
        "aspect_e2_e1_per_port": aspects,
        "planarity_per_port": planarities,
        "aspect_mean_all": aspect_mean_all,
        "aspect_std_all": aspect_std_all,
        "aspect_relative_spread": aspect_relative_spread,
        "rh_bonds_count": len(rh_bonds),
        "lh_bonds_count": len(lh_bonds),
        "aspect_rh_mean": aspect_rh_mean,
        "aspect_rh_std": aspect_rh_std,
        "aspect_lh_mean": aspect_lh_mean,
        "aspect_lh_std": aspect_lh_std,
        "rh_lh_aspect_divergence": rh_lh_aspect_diff,
        "planarity_rh_mean": planarity_rh_mean,
        "planarity_lh_mean": planarity_lh_mean,
        "n_ccw": n_ccw,
        "n_cw": n_cw,
        "n_ambig": n_ambig,
        "rh_n_ccw": rh_n_ccw,
        "rh_n_cw": rh_n_cw,
        "lh_n_ccw": lh_n_ccw,
        "lh_n_cw": lh_n_cw,
        "thresholds": {
            "ratio_consistency": RATIO_CONSISTENCY_THRESHOLD,
            "ratio_divergence": RATIO_DIVERGENCE_THRESHOLD,
            "chirality_consistency": CHIRALITY_CONSISTENCY_THRESHOLD,
        },
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
