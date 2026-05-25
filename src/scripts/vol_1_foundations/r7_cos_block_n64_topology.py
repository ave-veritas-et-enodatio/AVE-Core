"""Cos-block N=64 dual-criterion bound-state test (frequency + shell-localization).

Per `P_phase6_cos_block_n64_dual_criterion` (frozen at commit 1c89fa1).
Combines:
  - Shift-invert at σ=ω_C²=1 with inner GMRES OPinv
    (from r7_cos_block_shift_invert.py)
  - Shell-fraction topology extraction on the closest-eigenvalue ω-eigvec
    (analogous to r7_n64_topology_check.py for V-block)

Three-mode falsification (per pred body):
  - Mode I:        freq PASS AND shell_fraction ≥ 0.80
  - Mode I-FAIL:   freq PASS but shell_fraction < 0.80
                   (sub: 0.10-0.80 partial; <0.10 bulk-mode coincidence)
  - Mode III:      no eigenvalue within α tolerance regardless of localization

Cost: shift-invert + GMRES at N=64 dim 1.5M; topology extraction is ms.
Wall time: ~1-3 hr at N=64 GT_corpus single-seed. If Mode I confirms,
expand to F17K endpoints + vacuum_control in follow-up.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh, gmres, LinearOperator

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
R_MINOR = R_ANCHOR / PHI_SQ  # ≈ 3.82 — corpus GT minor radius

# Pred-locked threshold (per Grant adjudication 2026-04-26)
SHELL_THRESHOLD_MODE_I = 0.80
SHELL_BULK_BOUNDARY = 0.10

EIGENMODES = 20
GMRES_TOL = 1e-3
GMRES_MAXITER = 300
EIGSH_TOL = 1e-4
EIGSH_MAXITER = 300

OUTPUT_JSON = Path(__file__).parent / "r7_cos_block_n64_topology_results.json"


def build_engine(N=N_LATTICE, pml=PML):
    return VacuumEngine3D.from_args(
        N=N, pml=pml, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def cos_block_shell_localization(eigvec, engine, R_anchor, r_minor):
    """Compute shell-fraction localization on the ω-component of the joint
    (u, ω) eigvec. Shell is centered at radius R_anchor (xy-plane), thickness ±r_minor.

    eigvec: shape (6·N³,) — first half is u (3·N³), second half is ω (3·N³).
    Returns dict with energies + shell fraction on the ω-component.
    """
    N = engine.cos.nx
    n_per_field = engine.cos.u.size  # 3·N³
    omega_part = eigvec[n_per_field:]  # latter half = ω
    omega_field = omega_part.reshape(N, N, N, 3)

    # Per-site |ω|² density
    omega_density = np.sum(omega_field ** 2, axis=-1)  # shape (N, N, N)

    cx, cy, cz = (N - 1) / 2.0, (N - 1) / 2.0, (N - 1) / 2.0

    # Site distances from torus axis
    i_idx, j_idx, k_idx = np.indices(omega_density.shape)
    rho_xy = np.sqrt((i_idx - cx) ** 2 + (j_idx - cy) ** 2)
    rho_tube = np.sqrt((rho_xy - R_anchor) ** 2 + (k_idx - cz) ** 2)

    shell_mask = rho_tube <= r_minor
    bulk_mask = ~shell_mask

    total_energy = float(omega_density.sum())
    shell_energy = float(omega_density[shell_mask].sum())
    bulk_energy = float(omega_density[bulk_mask].sum())

    if total_energy < 1e-30:
        return None
    return {
        "total_energy": total_energy,
        "shell_energy": shell_energy,
        "bulk_energy": bulk_energy,
        "shell_fraction": shell_energy / total_energy,
        "bulk_uniform_expectation": float(4 * np.pi**2 * R_anchor * r_minor / N**3),
    }


def main():
    print("=" * 78, flush=True)
    print(f"  Cos-block N={N_LATTICE} dual-criterion bound-state test")
    print(f"  P_phase6_cos_block_n64_dual_criterion (frozen at 1c89fa1)")
    print("=" * 78, flush=True)
    print(f"  Pred PASS criteria: freq PASS AND shell_fraction ≥ {SHELL_THRESHOLD_MODE_I}")
    print(f"  Frequency target: ω_C² = {SIGMA_TARGET} (natural units)")
    print(f"  Frequency tolerance: |√λ - ω_C| < α·ω_C = {LAMBDA_TOL_COS:.4e}")
    print(f"  Bulk-mode boundary: shell_fraction < {SHELL_BULK_BOUNDARY}")
    print()

    print(f"  Building engine at N={N_LATTICE}, GT_corpus seed (R={R_ANCHOR}, r={R_MINOR:.4f})...")
    engine = build_engine()
    seed_2_3_hedgehog(engine, R_ANCHOR, R_MINOR)
    peak = a26_guard(engine, "GT_corpus")
    print(f"    A26 guard OK (peak |ω|={peak:.4f})")
    print()

    print(f"  Building K_cos LinearOperator (FD HVP)...", flush=True)
    K_op = build_K_cos_op(engine)
    M_diag = build_M_cos_diagonal(engine)
    M_op = diags(M_diag).tocsr()
    print(f"    dim = {K_op.shape[0]}")

    print(f"  Building OPinv = (K_cos - σ·M)^(-1) via inner GMRES (σ={SIGMA_TARGET})...", flush=True)
    OPinv = build_shift_invert_OPinv(K_op, M_diag, SIGMA_TARGET, GMRES_TOL, GMRES_MAXITER)

    print(f"  Eigsolve Cos-block at σ={SIGMA_TARGET}, k={EIGENMODES}...", flush=True)
    t0 = time.time()
    try:
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
    except Exception as e:
        elapsed = time.time() - t0
        print(f"    Eigsolve ERROR after {elapsed:.1f}s: {e}")
        return None

    # Sort by eigenvalue ascending
    idx_sort = np.argsort(eigvals)
    eigvals = eigvals[idx_sort]
    eigvecs = eigvecs[:, idx_sort]

    # Find closest positive eigenvalue to ω_C²
    pos_mask = eigvals > 1e-6  # skip null-space artifacts
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
    print(f"    Frequency criterion: {'PASS' if freq_pass else 'FAIL'} "
          f"(tolerance α = {ALPHA:.4e} = {100*ALPHA:.4f}%)")
    print()

    # Topology check on closest eigvec
    print(f"  Computing shell localization for closest eigvec...")
    eigvec = eigvecs[:, idx_orig]
    loc = cos_block_shell_localization(eigvec, engine, R_ANCHOR, R_MINOR)
    if loc is None:
        print(f"    ERROR: zero eigvec ω-component energy")
        return None
    sf = loc["shell_fraction"]
    bulk_unif = loc["bulk_uniform_expectation"]
    print(f"    Total ω-energy:    {loc['total_energy']:.4e}")
    print(f"    Shell ω-energy:    {loc['shell_energy']:.4e}")
    print(f"    Shell fraction:    {sf:.4f}")
    print(f"    Bulk-uniform exp:  {bulk_unif:.4f}")
    print(f"    Localization factor vs bulk-uniform: {sf / bulk_unif:.2f}×")
    print()

    # Three-mode adjudication per pred
    print("=" * 78, flush=True)
    print("  Cos-block N=64 dual-criterion adjudication")
    print("=" * 78, flush=True)
    if freq_pass and sf >= SHELL_THRESHOLD_MODE_I:
        mode = "I"
        verdict = (
            "MODE I — Cosserat sector hosts (2,3) bound state at corpus GT geometry. "
            f"Frequency PASS (rel_diff {100*closest_rel_diff:.4f}%) AND "
            f"shell fraction {sf:.4f} ≥ threshold {SHELL_THRESHOLD_MODE_I}. "
            "Doc 66_ §17.2 three-storage-mode picture confirmed; ε-strain/κ-curvature "
            "is the bound-state-hosting LC tank. Round 7 closes with corpus vindicated."
        )
    elif freq_pass:
        if sf < SHELL_BULK_BOUNDARY:
            mode = "I-FAIL (bulk-mode coincidence)"
            verdict = (
                f"MODE I-FAIL (bulk-mode coincidence) — Frequency PASS but shell "
                f"fraction {sf:.4f} < {SHELL_BULK_BOUNDARY} (bulk threshold). "
                "Same failure mode V-block hit at N=64 per doc 74_ §7 (band-density "
                "artifact). Cosserat-sector bound-state hypothesis FAILS. "
                "Round 8 Φ_link sector becomes cleanest gap."
            )
        else:
            mode = "I-FAIL (partial localization, ambiguous)"
            verdict = (
                f"MODE I-FAIL (partial localization) — Frequency PASS but shell "
                f"fraction {sf:.4f} ∈ [{SHELL_BULK_BOUNDARY}, {SHELL_THRESHOLD_MODE_I}). "
                "Eigvec has shell preference but significant bulk leak. §3.1.1 V=0 "
                "decoupling argues genuine bound state should be tightly localized; "
                "this is suspicious. Cosserat-sector bound-state hypothesis FAILS at "
                "the canonical threshold; could indicate hybrid mode or strong lattice-"
                "discretization spread, but pred-locked threshold says FAIL."
            )
    else:
        mode = "III"
        verdict = (
            f"MODE III — Cosserat sector also empty. No eigenvalue within α "
            f"tolerance of ω_C² (closest {100*closest_rel_diff:.4f}% off). "
            "V-pressure AND ε-strain/κ-curvature both empty. Round 8 Φ_link sector "
            "becomes cleanest gap."
        )
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_phase6_cos_block_n64_dual_criterion",
        "frozen_at_commit": "1c89fa1",
        "shell_threshold_mode_I": SHELL_THRESHOLD_MODE_I,
        "shell_bulk_boundary": SHELL_BULK_BOUNDARY,
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
        "topology": loc,
        "mode": mode,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
