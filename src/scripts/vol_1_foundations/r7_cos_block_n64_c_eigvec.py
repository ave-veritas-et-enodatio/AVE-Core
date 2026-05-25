"""Test A — Cos-block N=64 GT_corpus c_eigvec re-extraction with 4-category adjudication.

Per `P_phase6_cos_block_n64_c_eigvec_recheck` (frozen at this commit) +
audit on commit 88ec7c3 + A42 finding (corpus-canonical topology measure
for (2,3) electron eigenmode is c=3 via Op10 scalar crossing-count per
Doc 07_, NOT real-space shell-localization which is heuristic proxy).

Re-runs the same Cos-block N=64 GT_corpus eigsolve as the original
`r7_cos_block_n64_topology.py` (commit d3adcc2) but with c_eigvec
extraction via extract_crossing_count on the ω-component of the closest
eigvec, and 4-category adjudication.

Four-mode adjudication (per pred body):
    Mode I:        freq PASS AND c_eigvec = 3
    Mode III-freq: c_eigvec = 3 BUT freq FAIL
                   (topology right, frequency wrong — bound state at
                    different (R, r) than corpus GT)
    Mode III-topo: freq PASS BUT c_eigvec ≠ 3
                   (band-density coincidence on non-(2,3) bulk mode)
    Mode III-both: freq FAIL AND c_eigvec ≠ 3
                   (Cosserat sector empty at corpus GT in both axes)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r7_cos_block_shift_invert import (
    PHI_SQ, A26_AMP_SCALE, GT_PEAK_OMEGA, ALPHA, OMEGA_COMPTON,
    SIGMA_TARGET, LAMBDA_TOL_COS,
    A26_GUARD_LOW, A26_GUARD_HIGH,
    seed_2_3_hedgehog, a26_guard,
    build_K_cos_op, build_M_cos_diagonal, build_shift_invert_OPinv,
)

N_LATTICE = 64
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ

# Corpus-canonical topology criterion (per Doc 07_ + Op10)
TOPOLOGY_TARGET_C = 3   # (2,3) electron eigenmode crossing-count

EIGENMODES = 20
GMRES_TOL = 1e-3
GMRES_MAXITER = 300
EIGSH_TOL = 1e-4
EIGSH_MAXITER = 300

OUTPUT_JSON = Path(__file__).parent / "r7_cos_block_n64_c_eigvec_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def crossing_count_on_omega_eigvec(eigvec, engine):
    """Compute c_eigvec via extract_crossing_count on the ω-component
    of the joint (u, ω) eigvec, per Op10 (Doc 07_).

    eigvec: shape (6·N³,) — first half u, second half ω.
    Returns int crossing count.
    """
    n_per_field = engine.cos.u.size
    omega_part = eigvec[n_per_field:]  # latter half = ω
    N = engine.cos.nx
    omega_field = omega_part.reshape(N, N, N, 3)
    saved = engine.cos.omega.copy()
    try:
        engine.cos.omega = omega_field
        c = int(engine.cos.extract_crossing_count())
    finally:
        engine.cos.omega = saved
    return c


def main():
    print("=" * 78, flush=True)
    print(f"  Test A — Cos-block N={N_LATTICE} GT_corpus c_eigvec re-extraction")
    print(f"  P_phase6_cos_block_n64_c_eigvec_recheck (4-category adjudication)")
    print("=" * 78, flush=True)
    print(f"  Corpus-canonical topology criterion: c_eigvec = {TOPOLOGY_TARGET_C}")
    print(f"    (Op10 scalar crossing-count via extract_crossing_count, per Doc 07_)")
    print(f"  Frequency criterion: |√λ - ω_C| < α·ω_C = {LAMBDA_TOL_COS:.4e}")
    print()

    engine = build_engine()
    seed_2_3_hedgehog(engine, R_ANCHOR, R_MINOR)
    peak = a26_guard(engine, "GT_corpus")
    print(f"  A26 guard OK (peak |ω|={peak:.4f})")
    print()

    print(f"  Building K_cos LinearOperator (FD HVP) at N={N_LATTICE}...", flush=True)
    K_op = build_K_cos_op(engine)
    M_diag = build_M_cos_diagonal(engine)
    M_op = diags(M_diag).tocsr()
    print(f"    dim = {K_op.shape[0]}")

    print(f"  Building OPinv = (K_cos - σ·M)^(-1) via inner GMRES (σ={SIGMA_TARGET})...", flush=True)
    OPinv = build_shift_invert_OPinv(K_op, M_diag, SIGMA_TARGET, GMRES_TOL, GMRES_MAXITER)

    print(f"  Eigsolve Cos-block at σ={SIGMA_TARGET}, k={EIGENMODES}...", flush=True)
    t0 = time.time()
    eigvals, eigvecs = eigsh(
        K_op, M=M_op, k=EIGENMODES,
        sigma=SIGMA_TARGET, OPinv=OPinv, which='LM',
        tol=EIGSH_TOL, maxiter=EIGSH_MAXITER,
    )
    elapsed = time.time() - t0
    stats = OPinv._gmres_stats
    print(f"    Eigsolve: {elapsed:.1f}s, {len(eigvals)} eigenvalues, "
          f"OPinv calls={stats['call_count'][0]}, "
          f"total inner GMRES iters={stats['iter_total'][0]}")

    # Sort
    idx_sort = np.argsort(eigvals)
    eigvals = eigvals[idx_sort]
    eigvecs = eigvecs[:, idx_sort]

    # Closest positive eigenvalue (skip null-space artifacts)
    pos_mask = eigvals > 1e-6
    if not np.any(pos_mask):
        print(f"    No non-null positive eigenvalues found")
        return None
    pos_indices = np.where(pos_mask)[0]
    sqrt_lam = np.sqrt(eigvals[pos_mask])
    diffs = np.abs(sqrt_lam - OMEGA_COMPTON)
    idx_in_pos = int(np.argmin(diffs))
    idx_orig = int(pos_indices[idx_in_pos])
    closest_lam = float(eigvals[idx_orig])
    closest_sqrt_lam = float(sqrt_lam[idx_in_pos])
    closest_rel_diff = float(diffs[idx_in_pos] / OMEGA_COMPTON)
    freq_pass = closest_rel_diff < ALPHA

    print()
    print(f"  Closest positive eigenvalue: λ={closest_lam:.6f}, √λ={closest_sqrt_lam:.6f}")
    print(f"    rel_diff to ω_C: {closest_rel_diff:.4e} ({100*closest_rel_diff:.4f}%)")
    print(f"    Frequency criterion: {'PASS' if freq_pass else 'FAIL'}")
    print()

    # CORPUS-CANONICAL TOPOLOGY: c_eigvec via extract_crossing_count on ω-component
    print(f"  Computing c_eigvec via extract_crossing_count on ω-component...", flush=True)
    eigvec = eigvecs[:, idx_orig]
    c_eigvec = crossing_count_on_omega_eigvec(eigvec, engine)
    topo_pass = (c_eigvec == TOPOLOGY_TARGET_C)
    print(f"    c_eigvec = {c_eigvec} (target = {TOPOLOGY_TARGET_C})")
    print(f"    Topology criterion: {'PASS' if topo_pass else 'FAIL'}")
    print()

    # Compute c_eigvec for next 5 modes too (informational)
    print(f"  c_eigvec spectrum for top-5 nearest-to-σ modes (informational):")
    for j in range(min(5, len(eigvals))):
        # Find j-th closest by frequency
        diffs_all = np.abs(np.sqrt(np.abs(eigvals)) - OMEGA_COMPTON)
        order = np.argsort(diffs_all)
        idx_j = int(order[j])
        lam_j = float(eigvals[idx_j])
        if lam_j > 1e-6:
            sqrt_lam_j = float(np.sqrt(lam_j))
            rel_diff_j = abs(sqrt_lam_j - OMEGA_COMPTON) / OMEGA_COMPTON
            try:
                c_j = crossing_count_on_omega_eigvec(eigvecs[:, idx_j], engine)
            except Exception as e:
                c_j = -1
            print(f"    [{j}] λ={lam_j:.4f} √λ={sqrt_lam_j:.4f} "
                  f"rel_diff={100*rel_diff_j:.4f}% c_eigvec={c_j}")
    print()

    # FOUR-CATEGORY ADJUDICATION per pred
    print("=" * 78, flush=True)
    print("  Four-category adjudication (per P_phase6_cos_block_n64_c_eigvec_recheck)")
    print("=" * 78, flush=True)
    if freq_pass and topo_pass:
        mode = "I"
        verdict = (
            f"MODE I — Cosserat sector hosts (2,3) electron eigenmode at corpus GT. "
            f"Frequency PASS (rel_diff {100*closest_rel_diff:.4f}%) AND c_eigvec={c_eigvec} "
            f"matches corpus target {TOPOLOGY_TARGET_C}. Doc 66_ §17.2 three-storage-mode "
            f"picture confirmed. Round 7 closes with corpus vindicated."
        )
    elif topo_pass and not freq_pass:
        mode = "III-freq"
        verdict = (
            f"MODE III-freq (topology right, frequency wrong) — c_eigvec={c_eigvec} matches "
            f"corpus target {TOPOLOGY_TARGET_C} BUT frequency rel_diff {100*closest_rel_diff:.4f}% "
            f"≥ α tolerance {100*ALPHA:.4f}%. Cosserat sector has a (2,3)-topological eigenmode "
            f"but NOT at ω_C with this geometry. Bounded statement: (2,3) topology exists in "
            f"this seed's spectrum, just at a slightly different frequency than ω_C. Round 8 "
            f"reframes to 'what (R, r) gives ω = ω_C at this c=3 mode?' — different from "
            f"Φ_link sector entry."
        )
    elif freq_pass and not topo_pass:
        mode = "III-topo"
        verdict = (
            f"MODE III-topo (frequency right, topology wrong) — frequency rel_diff "
            f"{100*closest_rel_diff:.4f}% < α but c_eigvec={c_eigvec} ≠ {TOPOLOGY_TARGET_C}. "
            f"Frequency-PASS via band-density coincidence on a non-(2,3) bulk mode (same "
            f"failure mode as V-block N=64 per commit b8d97d9). Cosserat sector has bulk "
            f"modes at ω_C² but no (2,3) localization."
        )
    else:
        mode = "III-both"
        verdict = (
            f"MODE III-both (everything fails) — frequency rel_diff {100*closest_rel_diff:.4f}% "
            f"≥ α AND c_eigvec={c_eigvec} ≠ {TOPOLOGY_TARGET_C}. Cosserat sector empty at "
            f"corpus GT both at frequency and topology levels. Round 8 Φ_link sector becomes "
            f"cleanest gap per original framing."
        )
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase6_cos_block_n64_c_eigvec_recheck",
        "test": "Test A per audit on commit 88ec7c3 + A42 finding",
        "topology_criterion": "c_eigvec via extract_crossing_count (Op10 scalar, Doc 07_)",
        "topology_target_c": TOPOLOGY_TARGET_C,
        "N": N_LATTICE,
        "R_anchor": R_ANCHOR,
        "r_minor": R_MINOR,
        "GT_corpus_peak_omega_seed": peak,
        "elapsed_seconds": elapsed,
        "gmres_call_count": stats['call_count'][0],
        "gmres_iter_total": stats['iter_total'][0],
        "eigvals": eigvals.tolist(),
        "closest_eigenvalue": closest_lam,
        "closest_sqrt_lam": closest_sqrt_lam,
        "closest_rel_diff": closest_rel_diff,
        "frequency_pass": bool(freq_pass),
        "c_eigvec": c_eigvec,
        "topology_pass": bool(topo_pass),
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
