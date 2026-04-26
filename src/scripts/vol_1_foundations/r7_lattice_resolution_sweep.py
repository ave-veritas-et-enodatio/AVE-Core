"""V-block lattice-resolution sweep: K4-TLM scatter+connect transmission
eigsolve at N=64, GT_corpus seed only, vs N=32 baseline result.

Per `P_phase6_lattice_resolution_sweep` (frozen in manuscript/predictions.yaml)
and doc 74_ §6 + auditor concern #3. Tests whether the V-block Mode III gap
at N=32 (closest-mode phase 0.71574, 1.22% off ω_C·dt = 0.7071) is a real
K4-TLM lattice-physics finding OR a finite-N artifact that closes at higher
resolution.

Reuses build_T_operator (with Op3 bond reflection) from
r7_k4tlm_scattering_lctank.py — same V-block operator construction at the
new lattice size.

PASS criteria per pred (both required):
  (a) Gap-closure: |phase_N64 - ω_C·dt| > 0.5 × |phase_N32 - ω_C·dt|
      (gap retains >50% of N=32 gap → real K4-TLM finding)
  (b) Cluster-stability: phase_N64 within 1% of phase_N32 = 0.71574 rad
      (cluster preserves relative structure)

Falsification:
  - (a) fails: gap closes; N=32 Mode III is finite-N artifact
  - (b) fails: cluster shifts >1%; methodology issue
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import eigs

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D

# Import build_T_operator + helpers from main R7.1 driver
sys.path.insert(0, str(Path(__file__).resolve().parent))
from r7_k4tlm_scattering_lctank import (
    PHI, PHI_SQ, A26_AMP_SCALE, GT_PEAK_OMEGA, ALPHA, OMEGA_COMPTON,
    DT, TARGET_PHASE, PHASE_TOL_V,
    A26_GUARD_LOW, A26_GUARD_HIGH,
    seed_2_3_hedgehog, a26_guard,
    build_T_operator,
)

# Per-pred frozen constants
N_RESOLUTION_NEW = 64
PML_NEW = 4
R_ANCHOR_NEW = 10.0
EIGENMODES_NEW = 20

# N=32 baseline values per doc 74_ §2.1 (GT_corpus result)
PHASE_N32_GT = 0.7157399782985672
GAP_N32_GT = abs(PHASE_N32_GT - TARGET_PHASE)  # ≈ 0.00863 rad

OUTPUT_JSON = Path(__file__).parent / "r7_lattice_resolution_sweep_results.json"


def main():
    print("=" * 78, flush=True)
    print(f"  V-block lattice-resolution sweep at N={N_RESOLUTION_NEW}")
    print(f"  GT_corpus seed only; comparing to N=32 baseline (phase {PHASE_N32_GT:.6f})")
    print("=" * 78, flush=True)
    print(f"  Target: ω_C·dt = {TARGET_PHASE:.6f} rad")
    print(f"  N=32 closest-mode phase: {PHASE_N32_GT:.6f}, gap = {GAP_N32_GT:.4e} ({100*GAP_N32_GT/TARGET_PHASE:.4f}%)")
    print(f"  PASS tolerance (per V-block): {PHASE_TOL_V:.4e} rad ({100*PHASE_TOL_V/TARGET_PHASE:.4f}%)")
    print()

    engine = VacuumEngine3D.from_args(
        N=N_RESOLUTION_NEW, pml=PML_NEW, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    R = R_ANCHOR_NEW
    r = R_ANCHOR_NEW / PHI_SQ
    print(f"  Seed: GT_corpus at (R={R}, r={r:.4f}); N={N_RESOLUTION_NEW} active sites = 2·(N/2)³ = {2*(N_RESOLUTION_NEW//2)**3}")
    seed_2_3_hedgehog(engine, R, r)
    peak = a26_guard(engine, "GT_corpus")
    print(f"  A26 guard OK (peak |ω|={peak:.4f})")
    print()

    print(f"  Building T = C_op3 · S(z_local) at N={N_RESOLUTION_NEW}...", flush=True)
    t0 = time.time()
    T, sites, n_active = build_T_operator(engine)
    print(f"    T built in {time.time() - t0:.1f}s; dim={T.shape[0]}, nnz={T.nnz}")
    print()

    sigma = complex(np.cos(TARGET_PHASE), np.sin(TARGET_PHASE))
    print(f"  Eigsolve V-block at sigma=exp(i·{TARGET_PHASE:.4f})...", flush=True)
    t1 = time.time()
    try:
        eigvals, eigvecs = eigs(
            T, k=EIGENMODES_NEW, sigma=sigma, which='LM',
            tol=1e-6, maxiter=2000,
        )
        elapsed = time.time() - t1
        print(f"    V-block eigsolve: {elapsed:.1f}s, {len(eigvals)} eigenvalues")
    except Exception as e:
        print(f"    V-block eigsolve ERROR: {e}")
        return {"error": str(e)}

    # Find closest eigenvalue to target phase
    phases = np.angle(eigvals)
    diffs = np.abs(phases - TARGET_PHASE)
    diffs_neg = np.abs(phases - (-TARGET_PHASE))
    diffs_combined = np.minimum(diffs, diffs_neg)
    idx_closest = int(np.argmin(diffs_combined))
    phase_closest_N64 = float(phases[idx_closest])
    gap_N64 = float(diffs_combined[idx_closest])

    print()
    print(f"  Result: closest mode at phase {phase_closest_N64:.6f} rad")
    print(f"          gap to ω_C·dt = {gap_N64:.4e} rad ({100*gap_N64/TARGET_PHASE:.4f}%)")
    print()

    # Adjudication per pred
    gap_closure_ratio = gap_N64 / GAP_N32_GT
    cluster_shift = abs(phase_closest_N64 - PHASE_N32_GT) / abs(PHASE_N32_GT)

    print("=" * 78, flush=True)
    print("  Resolution-trend adjudication per P_phase6_lattice_resolution_sweep")
    print("=" * 78, flush=True)
    print(f"  (a) Gap-closure: gap_N64/gap_N32 = {gap_closure_ratio:.4f}")
    print(f"      Required > 0.5 (gap retains >50% of N=32 gap)")
    a_pass = gap_closure_ratio > 0.5
    print(f"      → {'PASS' if a_pass else 'FAIL — N=32 Mode III may be finite-N artifact'}")
    print()
    print(f"  (b) Cluster-stability: |phase_N64 - phase_N32| / phase_N32 = {cluster_shift:.4e}")
    print(f"      Required < 0.01 (1% relative cluster stability)")
    b_pass = cluster_shift < 0.01
    print(f"      → {'PASS' if b_pass else 'FAIL — cluster shifted >1%, methodology issue'}")
    print()

    if a_pass and b_pass:
        verdict = "BOTH PASS — N=32 Mode III is real K4-TLM lattice-physics finding"
    elif not a_pass and b_pass:
        verdict = "(a) FAILS, (b) PASSES — gap closes at N=64; N=32 Mode III is FINITE-N ARTIFACT. Continuum-limit may have eigenmode at ω_C; corpus GT may yet be correct."
    elif a_pass and not b_pass:
        verdict = "(b) FAILS — cluster shifted; methodology issue"
    else:
        verdict = "BOTH FAIL — pred falsified comprehensively"

    print(f"  VERDICT: {verdict}")

    payload = {
        "pre_registration": "P_phase6_lattice_resolution_sweep",
        "N_baseline": 32,
        "N_test": N_RESOLUTION_NEW,
        "phase_N32_baseline": PHASE_N32_GT,
        "gap_N32_baseline": GAP_N32_GT,
        "phase_N64": phase_closest_N64,
        "gap_N64": gap_N64,
        "gap_closure_ratio": gap_closure_ratio,
        "cluster_shift_relative": cluster_shift,
        "(a)_gap_closure_pass": a_pass,
        "(b)_cluster_stability_pass": b_pass,
        "verdict": verdict,
        "elapsed_seconds": elapsed,
        "T_dim": int(T.shape[0]),
        "T_nnz": int(T.nnz),
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Results: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
