"""r10_path_alpha_v9_bond_pair_quadrature.py — E-094: Phase 1 bond-pair rerun.

Per auditor directive 2026-04-30 + doc 100 §10.31: bond-pair scale rerun closing
A-016 caveat from L3 closure. Uses corpus-canonical (V_inc, V_ref) quadrature
eigenmode IC per A47 v7 + A-023, NOT the V_inc-only seeder used by path α
v1-v4(b) at bond-cluster scale.

Reframe per doc 83 §2 + §4:
  Path α v1-v4(b) tested bond-CLUSTER scale (R=10, multi-cell extended torus).
  Corpus electron is bond-PAIR scale (~ℓ_node, single A-B + 3 lateral neighbors).
  This driver tests at bond-PAIR scale: small R, small lattice, single saturated
  bond-pair as test object.

Methodology vs r9_path_alpha_bond_pair_phasor.py:
  1. IC: initialize_quadrature_2_3_eigenmode (V_inc + V_ref at 90° per A47 v7)
     vs r9's initialize_2_3_voltage_ansatz (V_inc-only).
  2. R=2 (bond-pair envelope), vs r9's R=10 (bond-cluster).
  3. N=16 lattice (interior 8³), vs r9's N=32.
  4. Same K4 tetrahedral bond-pair sampling + Hilbert phasor analysis.

Dual-criterion adjudication (per cluster) per doc 28 §5.1 + doc 79 v5.1 §6:
  C1: R_phase / r_phase = φ² ± 5%
  C2: chirality consensus ≥ 75% via mean(sin(Δφ_Hilbert))

Pre-reg outcome classes:
  Mode I:    C1 PASS + C2 PASS  (corpus electron at bond-pair scale empirically realized)
  Mode II:   C1 PASS, C2 FAIL  (R/r = φ² but no chirality)
  Mode II':  C1 FAIL, C2 PASS  (chirality but R/r ≠ φ²)
  Mode III:  C1 FAIL + C2 FAIL  (corpus electron at bond-pair scale NOT empirically realized)

Mode III at bond-pair scale closes A-016 caveat: substrate cannot host the
corpus electron at any tested object class. Mode I overturns A-014 verdict.

A-021 pre-flight grep applied: no prior bond-pair-quadrature drivers exist;
r9_path_alpha_bond_pair_phasor.py is the closest template (V_inc-only at
bond-cluster) which this driver supersedes per A47 v7 quadrature requirement.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.signal import hilbert

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_quadrature_2_3_eigenmode


# ─── Bond-pair-scale constants ────────────────────────────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 16
PML = 4
R_ANCHOR = 2.0                # bond-pair scale (vs r9's R=10 bond-cluster)
R_MINOR = R_ANCHOR / PHI_SQ   # ≈ 0.764
AMPLITUDE = 0.05              # sub-yield (V_yield ≈ 0.0854)

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

PRE_EVOLVE_END_P = 5.0
SELECTION_END_P = 10.0
RECORDING_END_P = 35.0

PRE_EVOLVE_END_STEP = int(PRE_EVOLVE_END_P * COMPTON_PERIOD / DT)
SELECTION_END_STEP = int(SELECTION_END_P * COMPTON_PERIOD / DT)
RECORDING_END_STEP = int(RECORDING_END_P * COMPTON_PERIOD / DT)
N_RECORDING_STEPS = RECORDING_END_STEP - SELECTION_END_STEP

TOP_K_CANDIDATES = 8
SAMPLE_PORT = 0

# K4 tetrahedral port offsets (standard A→B layout)
PORT_OFFSETS = [
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
]

# Adjudication thresholds
PHI_SQ_TOL = 0.05
CHIRALITY_CONSISTENCY_THRESHOLD = 0.75
PERSISTENCE_GUARD = 0.50

OUTPUT_JSON = Path(__file__).parent / "r10_path_alpha_v9_bond_pair_quadrature_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def find_bond_pairs(top_cells_list, top_cells_set):
    """Find K4 A-B bond-pairs among top saturated cells via tetrahedral offsets."""
    bond_pairs = []
    used = set()
    for cell in top_cells_list:
        if cell in used:
            continue
        for offset in PORT_OFFSETS:
            partner = (cell[0] + offset[0], cell[1] + offset[1], cell[2] + offset[2])
            if partner in top_cells_set and partner not in used:
                bond_pairs.append({"A": cell, "B": partner, "offset": offset})
                used.add(cell)
                used.add(partner)
                break
    return bond_pairs


def cluster_bond_pairs(bond_pairs, lattice_center):
    """Group bond-pairs by spatial proximity (single cluster expected at bond-pair scale)."""
    if not bond_pairs:
        return {}
    return {"central": bond_pairs}


def measure_phasor(engine, bond_pair, port):
    """Return (V_inc, V_ref) at bond-pair A-side cell on specified port."""
    A = bond_pair["A"]
    V_inc = float(engine.k4.V_inc[A[0], A[1], A[2], port])
    V_ref = float(engine.k4.V_ref[A[0], A[1], A[2], port])
    return V_inc, V_ref


def adjudicate_per_cluster(cluster_phasors):
    """Per-cluster dual-criterion adjudication.

    cluster_phasors: dict cluster_name -> list of (V_inc_traj, V_ref_traj) tuples
                     where each is np.array shape (n_steps,)
    Returns: dict with R_phase, r_phase, ratio, chirality, mode per cluster.
    """
    out = {}
    for name, phasors in cluster_phasors.items():
        if not phasors:
            out[name] = {"mode": "EMPTY", "n_pairs": 0}
            continue

        # Aggregate V_inc, V_ref across all bond-pair phasors in cluster
        all_V_inc = np.concatenate([p[0] for p in phasors])
        all_V_ref = np.concatenate([p[1] for p in phasors])

        # Center on origin
        V_inc_c = all_V_inc - all_V_inc.mean()
        V_ref_c = all_V_ref - all_V_ref.mean()

        # PCA → ellipse axes
        cov = np.cov(np.stack([V_inc_c, V_ref_c]))
        eigvals, _ = np.linalg.eigh(cov)
        eigvals = np.sort(np.abs(eigvals))[::-1]  # major first
        if eigvals[1] < 1e-15:
            ratio = float("inf")
        else:
            R_phase = np.sqrt(eigvals[0])
            r_phase = np.sqrt(eigvals[1])
            ratio = R_phase / r_phase if r_phase > 0 else float("inf")

        # Chirality via Hilbert-transform analytic signal phase difference
        chirality_signs = []
        for V_inc_traj, V_ref_traj in phasors:
            if len(V_inc_traj) < 16:
                continue
            try:
                a_inc = hilbert(V_inc_traj - V_inc_traj.mean())
                a_ref = hilbert(V_ref_traj - V_ref_traj.mean())
                phase_diff = np.angle(a_ref / np.maximum(np.abs(a_inc), 1e-12) /
                                      np.exp(1j * np.angle(a_inc)))
                chirality_signs.append(float(np.mean(np.sin(phase_diff))))
            except Exception:
                continue

        mean_chirality = float(np.mean(chirality_signs)) if chirality_signs else 0.0
        consensus_count = sum(1 for c in chirality_signs if abs(c) > 0.1)
        consensus_frac = consensus_count / len(chirality_signs) if chirality_signs else 0.0
        ccw_consensus = sum(1 for c in chirality_signs if c > 0.1) / max(len(chirality_signs), 1)
        cw_consensus = sum(1 for c in chirality_signs if c < -0.1) / max(len(chirality_signs), 1)

        # Adjudication
        c1_pass = abs(ratio - PHI_SQ) / PHI_SQ <= PHI_SQ_TOL if ratio != float("inf") else False
        c2_pass = max(ccw_consensus, cw_consensus) >= CHIRALITY_CONSISTENCY_THRESHOLD

        if c1_pass and c2_pass:
            mode = "Mode I"
        elif c1_pass and not c2_pass:
            mode = "Mode II"
        elif not c1_pass and c2_pass:
            mode = "Mode II'"
        else:
            mode = "Mode III"

        out[name] = {
            "mode": mode,
            "n_pairs": len(phasors),
            "ratio": float(ratio) if ratio != float("inf") else None,
            "phi_sq_target": float(PHI_SQ),
            "ratio_gap_pct": float(abs(ratio - PHI_SQ) / PHI_SQ * 100) if ratio != float("inf") else None,
            "mean_chirality": mean_chirality,
            "ccw_consensus_frac": float(ccw_consensus),
            "cw_consensus_frac": float(cw_consensus),
            "c1_pass": bool(c1_pass),
            "c2_pass": bool(c2_pass),
        }
    return out


def main():
    print("=" * 60)
    print("E-094 Phase 1 bond-pair rerun (A-016 closure test)")
    print(f"Lattice N={N_LATTICE} (interior {N_LATTICE-2*PML}^3), R={R_ANCHOR} (bond-pair), r={R_MINOR:.3f}")
    print(f"IC: initialize_quadrature_2_3_eigenmode (V_inc + V_ref at 90°) per A47 v7")
    print(f"Recording window: {SELECTION_END_P:.0f}P to {RECORDING_END_P:.0f}P")
    print("=" * 60)

    engine = build_engine()

    # Apply corpus-canonical quadrature IC
    initialize_quadrature_2_3_eigenmode(
        engine.k4,
        R=R_ANCHOR,
        r=R_MINOR,
        amplitude=AMPLITUDE,
        chirality=1.0,  # explicit electron (RH K4)
    )

    # Pre-evolve to settle transients
    print(f"\n[Pre-evolve] {PRE_EVOLVE_END_P:.0f} P ({PRE_EVOLVE_END_STEP} steps)...")
    for _ in range(PRE_EVOLVE_END_STEP):
        engine.step()

    # Selection: find top-K saturated bond-pairs over selection window
    print(f"[Selection] {SELECTION_END_P - PRE_EVOLVE_END_P:.0f} P selection window...")
    selection_steps = SELECTION_END_STEP - PRE_EVOLVE_END_STEP
    accumulated_amp_sq = np.zeros((N_LATTICE, N_LATTICE, N_LATTICE))
    for _ in range(selection_steps):
        engine.step()
        # Accumulate per-cell |V_inc|²+|V_ref|² across active mask, port 0
        active = engine.k4.mask_active
        amp_sq = (engine.k4.V_inc[..., 0]**2 + engine.k4.V_ref[..., 0]**2) * active
        accumulated_amp_sq += amp_sq

    # Find top-K saturated cells (excluding PML)
    interior_mask = np.zeros_like(accumulated_amp_sq, dtype=bool)
    interior_mask[PML:N_LATTICE-PML, PML:N_LATTICE-PML, PML:N_LATTICE-PML] = True
    masked_amp_sq = np.where(interior_mask, accumulated_amp_sq, -np.inf)
    flat = masked_amp_sq.flatten()
    top_indices = np.argpartition(flat, -TOP_K_CANDIDATES)[-TOP_K_CANDIDATES:]
    top_cells_list = [tuple(np.unravel_index(idx, accumulated_amp_sq.shape)) for idx in top_indices]
    top_cells_set = set(top_cells_list)

    print(f"[Selection] Top {TOP_K_CANDIDATES} saturated cells: {sorted(top_cells_list)}")

    # Find bond-pairs
    bond_pairs = find_bond_pairs(top_cells_list, top_cells_set)
    print(f"[Selection] Found {len(bond_pairs)} bond-pair(s) via K4 tetrahedral offsets")

    if not bond_pairs:
        print("\n[Result] NO BOND-PAIRS FORMED at bond-pair scale.")
        print("Mode III by absence: corpus electron's bond-pair structure does not")
        print("manifest from this IC at this scale. A-016 caveat closure: NEGATIVE.")
        result = {
            "lattice_N": N_LATTICE,
            "R": R_ANCHOR,
            "r": R_MINOR,
            "amplitude": AMPLITUDE,
            "ic_seeder": "initialize_quadrature_2_3_eigenmode",
            "n_bond_pairs": 0,
            "mode": "Mode III (no bond-pairs formed)",
            "a_016_closure": "NEGATIVE",
            "top_cells": sorted(top_cells_list),
        }
        OUTPUT_JSON.write_text(json.dumps(result, indent=2, default=str))
        return result

    # Recording: capture phasor trajectories at each bond-pair
    print(f"[Recording] {RECORDING_END_P - SELECTION_END_P:.0f} P recording at {len(bond_pairs)} bond-pair(s)...")
    pair_V_inc = [[] for _ in bond_pairs]
    pair_V_ref = [[] for _ in bond_pairs]
    for _ in range(N_RECORDING_STEPS):
        engine.step()
        for i, bp in enumerate(bond_pairs):
            V_inc, V_ref = measure_phasor(engine, bp, SAMPLE_PORT)
            pair_V_inc[i].append(V_inc)
            pair_V_ref[i].append(V_ref)

    # Cluster + adjudicate
    lattice_center = (N_LATTICE / 2, N_LATTICE / 2, N_LATTICE / 2)
    clusters = cluster_bond_pairs(bond_pairs, lattice_center)
    cluster_phasors = {}
    for name, pairs in clusters.items():
        cluster_phasors[name] = []
        for bp in pairs:
            i = bond_pairs.index(bp)
            V_inc_traj = np.array(pair_V_inc[i])
            V_ref_traj = np.array(pair_V_ref[i])
            cluster_phasors[name].append((V_inc_traj, V_ref_traj))

    adj = adjudicate_per_cluster(cluster_phasors)

    # Report
    print("\n" + "=" * 60)
    print("ADJUDICATION (per cluster)")
    print("=" * 60)
    for name, info in adj.items():
        print(f"\nCluster '{name}' (n_pairs={info['n_pairs']}):")
        print(f"  Mode: {info['mode']}")
        if info.get("ratio") is not None:
            print(f"  R_phase/r_phase = {info['ratio']:.3f} (target φ² = {info['phi_sq_target']:.3f}, "
                  f"gap {info['ratio_gap_pct']:.1f}%)")
            print(f"  C1 (R/r=φ² ±5%): {'PASS' if info['c1_pass'] else 'FAIL'}")
        print(f"  CCW consensus: {info.get('ccw_consensus_frac', 0)*100:.1f}%, "
              f"CW consensus: {info.get('cw_consensus_frac', 0)*100:.1f}%")
        print(f"  C2 (≥75% chirality): {'PASS' if info.get('c2_pass') else 'FAIL'}")

    # Write results
    result = {
        "lattice_N": N_LATTICE,
        "R": R_ANCHOR,
        "r": R_MINOR,
        "amplitude": AMPLITUDE,
        "ic_seeder": "initialize_quadrature_2_3_eigenmode",
        "n_bond_pairs": len(bond_pairs),
        "bond_pairs": [{"A": list(bp["A"]), "B": list(bp["B"]),
                        "offset": list(bp["offset"])} for bp in bond_pairs],
        "adjudication": adj,
    }
    OUTPUT_JSON.write_text(json.dumps(result, indent=2, default=str))
    print(f"\n[Result] Written to {OUTPUT_JSON}")
    return result


if __name__ == "__main__":
    main()
