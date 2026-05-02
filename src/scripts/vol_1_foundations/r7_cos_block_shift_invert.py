"""Cos-block comprehensive coverage via shift-invert at sigma=ω_C²=1 with inner GMRES.

Per [doc 74_ §6.1](../../research/L3_electron_soliton/74_r7_k4tlm_lctank_run_result.md)
follow-up to auditor concern #1: the original k=100 SA-mode covers only the
bottom 100 of 196608 K_cos eigenvalues (~0.05% of spectrum). ω_C² = 1 may
exist at higher index. To find it, shift-invert at sigma=ω_C²=1 with explicit
OPinv via inner iterative GMRES at each outer Lanczos step.

Method:
    eigsh with sigma=σ requires (K_cos - σ·M_cos)^(-1) · M_cos · v at each step.
    For LinearOperator-based K_cos (FD HVP), we provide OPinv as a LinearOperator
    that wraps scipy.sparse.linalg.gmres on the shifted operator.

    Inner solve: (K_cos - σ·M_cos) · x = M_cos · v  →  x = OPinv · v
    Outer Lanczos: eigsh(K_cos, M=M_cos, sigma=1, OPinv=..., k=20, which='LM')

Estimated cost:
    Outer Lanczos: ~50-100 iterations for k=20
    Inner GMRES: ~20-50 iterations per outer step (depends on conditioning)
    Total HVPs: ~1000-5000 per seed
    At ~1s per HVP: ~15-90 min per seed

References:
    - doc 73_ §3 (Cos-block operator construction)
    - doc 74_ §3 (bottom-100 SA-mode result, mode III with caveat)
    - r7_k4tlm_scattering_lctank.py (original driver with SA-mode Cos-block)
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


# Constants per frozen pred (doc 73_ §3, doc 74_ §1)
PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi
from ave.core.constants import ALPHA
OMEGA_COMPTON = 1.0
SIGMA_TARGET = OMEGA_COMPTON ** 2  # = 1.0
LAMBDA_TOL_COS = ALPHA * OMEGA_COMPTON  # ≈ 0.00731 on √λ
A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA

F17K_COS_RATIO = 3.40
F17K_S11_RATIO = 1.03

OUTPUT_JSON = Path(__file__).parent / "r7_cos_block_shift_invert_results.json"


def build_engine(N=32, pml=4):
    return VacuumEngine3D.from_args(
        N=N, pml=pml, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_2_3_hedgehog(engine, R, r):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )


def seed_random_low(engine, peak=0.05):
    rng = np.random.default_rng(seed=42)
    omega = rng.uniform(-peak, peak, size=engine.cos.omega.shape)
    omega *= engine.cos.mask_alive[..., None]
    engine.cos.omega = omega
    engine.cos.omega_dot[...] = 0.0
    engine.cos.u[...] = 0.0
    engine.cos.u_dot[...] = 0.0


def a26_guard(engine, name):
    peak = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    if name.startswith("GT") or name.startswith("F17K"):
        if not (A26_GUARD_LOW <= peak <= A26_GUARD_HIGH):
            raise AssertionError(f"A26 GUARD FAILED for '{name}': peak |ω|={peak:.4f}")
    return peak


# ─── K_cos via FD HVP (same as main driver) ──────────────────────────────────


def build_K_cos_op(engine, eps=1e-5):
    u_seed = engine.cos.u.copy()
    omega_seed = engine.cos.omega.copy()
    n_per = u_seed.size
    n_state = 2 * n_per

    def matvec(v_flat):
        v = np.asarray(v_flat, dtype=np.float64)
        v_u = v[:n_per].reshape(u_seed.shape)
        v_w = v[n_per:].reshape(omega_seed.shape)

        engine.cos.u = u_seed + eps * v_u
        engine.cos.omega = omega_seed + eps * v_w
        dE_du_p, dE_dw_p = engine.cos.energy_gradient()

        engine.cos.u = u_seed - eps * v_u
        engine.cos.omega = omega_seed - eps * v_w
        dE_du_m, dE_dw_m = engine.cos.energy_gradient()

        engine.cos.u = u_seed.copy()
        engine.cos.omega = omega_seed.copy()

        Hv_u = (np.asarray(dE_du_p) - np.asarray(dE_du_m)) / (2.0 * eps)
        Hv_w = (np.asarray(dE_dw_p) - np.asarray(dE_dw_m)) / (2.0 * eps)
        return np.concatenate([Hv_u.flatten(), Hv_w.flatten()])

    return LinearOperator(shape=(n_state, n_state), matvec=matvec, dtype=np.float64)


def build_M_cos_diagonal(engine):
    """M_cos = block-diag(ρ·I, I_ω·I) returned as 1D vector for diagonal multiplication."""
    rho = engine.cos.rho
    I_omega = engine.cos.I_omega
    n_per = engine.cos.u.size
    return np.concatenate([rho * np.ones(n_per), I_omega * np.ones(n_per)])


# ─── Shift-invert OPinv via inner GMRES ──────────────────────────────────────


def build_shift_invert_OPinv(K_op, M_diag, sigma, gmres_tol=1e-5, gmres_maxiter=100, verbose=False):
    """OPinv = (K_op - σ·M)^(-1) wrapped as LinearOperator using inner GMRES.

    For eigsh shift-invert mode at σ, need OPinv s.t. OPinv · v solves
        (K_op - σ·M) · x = v  for x
    """
    n = K_op.shape[0]

    def shifted_matvec(u):
        """Compute (K_op - σ·M) · u = K_op · u - σ · M · u (M diagonal)."""
        return K_op.matvec(u) - sigma * (M_diag * u)

    shifted_op = LinearOperator(shape=(n, n), matvec=shifted_matvec, dtype=K_op.dtype)

    call_count = [0]
    gmres_iter_total = [0]

    def opinv_matvec(v):
        """Solve (K_op - σ·M) · x = v via GMRES."""
        call_count[0] += 1
        # callback to count inner iterations
        iter_count = [0]
        def cb(_):
            iter_count[0] += 1
        x, info = gmres(shifted_op, v, rtol=gmres_tol, maxiter=gmres_maxiter,
                        callback=cb, callback_type='legacy')
        gmres_iter_total[0] += iter_count[0]
        if verbose and call_count[0] % 10 == 0:
            print(f"      OPinv calls: {call_count[0]}, total inner GMRES iters: {gmres_iter_total[0]}")
        if info != 0:
            print(f"      GMRES warning: info={info} at OPinv call {call_count[0]}")
        return x

    opinv = LinearOperator(shape=(n, n), matvec=opinv_matvec, dtype=K_op.dtype)
    opinv._gmres_stats = {"call_count": call_count, "iter_total": gmres_iter_total}
    return opinv


def eigsolve_Cos_block_shift_invert(engine, k=20, sigma=SIGMA_TARGET,
                                     gmres_tol=1e-3, gmres_maxiter=300,
                                     eigsh_tol=1e-4, eigsh_maxiter=300):
    """Eigsolve K_cos at sigma=σ via shift-invert with inner GMRES OPinv."""
    print(f"    Building K_cos LinearOperator (FD HVP)...", flush=True)
    K_op = build_K_cos_op(engine)
    M_diag = build_M_cos_diagonal(engine)
    M_op = diags(M_diag).tocsr()

    print(f"    Building OPinv = (K_cos - σ·M)^(-1) via inner GMRES (σ={sigma})...", flush=True)
    OPinv = build_shift_invert_OPinv(K_op, M_diag, sigma, gmres_tol, gmres_maxiter)

    print(f"    Eigsolve Cos-block shift-invert at σ={sigma}, k={k}...", flush=True)
    t0 = time.time()
    try:
        eigvals, eigvecs = eigsh(
            K_op, M=M_op, k=k,
            sigma=sigma, OPinv=OPinv, which='LM',
            tol=eigsh_tol, maxiter=eigsh_maxiter,
        )
        elapsed = time.time() - t0
        stats = OPinv._gmres_stats
        print(f"      Cos-block shift-invert: {elapsed:.1f}s, "
              f"{len(eigvals)} eigenvalues, "
              f"OPinv calls={stats['call_count'][0]}, "
              f"total GMRES iters={stats['iter_total'][0]}")
    except Exception as e:
        elapsed = time.time() - t0
        print(f"      Cos-block shift-invert ERROR after {elapsed:.1f}s: {e}")
        return {"eigvals": None, "eigvecs": None, "elapsed": elapsed, "error": str(e)}

    idx = np.argsort(eigvals)
    return {
        "eigvals": eigvals[idx],
        "eigvecs": eigvecs[:, idx],
        "elapsed": elapsed,
        "gmres_call_count": stats['call_count'][0],
        "gmres_iter_total": stats['iter_total'][0],
        "error": None,
    }


def check_at_compton(eigvals):
    if eigvals is None or len(eigvals) == 0:
        return False, -1, np.inf
    pos = eigvals[eigvals > 0]
    if len(pos) == 0:
        return False, -1, np.inf
    sqrt_lam = np.sqrt(pos)
    diffs = np.abs(sqrt_lam - OMEGA_COMPTON)
    idx_in_pos = int(np.argmin(diffs))
    rel = float(diffs[idx_in_pos] / OMEGA_COMPTON)
    pos_indices = np.where(eigvals > 0)[0]
    idx_orig = int(pos_indices[idx_in_pos])
    return diffs[idx_in_pos] < LAMBDA_TOL_COS, idx_orig, rel


def run_seed(name, R, r, gt_family, N=32, pml=4, k=20):
    print(f"\n  ── seed: {name} (N={N}) ──")
    engine = build_engine(N=N, pml=pml)
    if name == "vacuum_control":
        seed_random_low(engine)
    else:
        seed_2_3_hedgehog(engine, R, r)
    peak = a26_guard(engine, name)
    print(f"    A26 guard OK (peak |ω|={peak:.4f})")

    res = eigsolve_Cos_block_shift_invert(engine, k=k)
    if res["eigvals"] is None:
        return {"seed_name": name, "error": res["error"], "elapsed": res["elapsed"]}

    close, idx, rel = check_at_compton(res["eigvals"])
    print(f"    Closest positive eigenvalue: λ={res['eigvals'][idx] if idx>=0 else 'NA'}, "
          f"√λ rel_diff to ω_C = {rel:.4e}, PASS={close}")
    print(f"    Smallest 5 positive: {[float(v) for v in res['eigvals'][res['eigvals']>0][:5]]}")
    print(f"    Largest 5 positive: {[float(v) for v in res['eigvals'][res['eigvals']>0][-5:]]}")

    return {
        "seed_name": name,
        "R": R, "r": r,
        "gt_family": gt_family,
        "peak_omega_seed": peak,
        "eigvals": res["eigvals"].tolist(),
        "elapsed_seconds": res["elapsed"],
        "gmres_call_count": res["gmres_call_count"],
        "gmres_iter_total": res["gmres_iter_total"],
        "close_to_omega_C": close,
        "rel_diff": rel,
    }


def main(N=32, smoke=False):
    print("=" * 78, flush=True)
    print(f"  Cos-block shift-invert eigsolve at σ=ω_C²={SIGMA_TARGET} (N={N})")
    print("=" * 78, flush=True)
    print(f"  Per doc 74_ §6.1 follow-up: comprehensive Cos-block coverage")
    print(f"  via shift-invert with inner GMRES OPinv")
    print()

    R_anchor = 6.0 if smoke else 10.0
    pml = 2 if smoke else 4

    if smoke:
        seeds = [("GT_corpus", R_anchor, R_anchor / PHI_SQ, True)]
    else:
        seeds = [
            ("GT_corpus",          R_anchor, R_anchor / PHI_SQ,         True),
            ("F17K_cos_endpoint",  R_anchor, R_anchor / F17K_COS_RATIO, True),
            ("F17K_s11_endpoint",  R_anchor, R_anchor / F17K_S11_RATIO, True),
            ("vacuum_control",     0.0,      0.0,                        False),
        ]

    results = {}
    for name, R, r, fam in seeds:
        try:
            results[name] = run_seed(name, R, r, fam, N=N, pml=pml)
        except Exception as e:
            import traceback
            results[name] = {"seed_name": name, "fatal_error": str(e),
                            "traceback": traceback.format_exc()}
            print(f"  ERROR in {name}: {e}")
            if smoke:
                break

    # Adjudication
    print("\n" + "=" * 78, flush=True)
    print("  Cos-block comprehensive coverage adjudication")
    print("=" * 78, flush=True)
    pass_seeds = [n for n, r in results.items() if r.get("close_to_omega_C")]
    if pass_seeds:
        print(f"  PASS seeds: {pass_seeds}")
    else:
        print(f"  No seed has Cos-block eigenmode within α tolerance of ω_C")
        print(f"  → Comprehensive Mode III for Cos-block (was incomplete-coverage in original run)")

    payload = {
        "context": "doc 74_ §6.1 follow-up — Cos-block shift-invert comprehensive coverage",
        "sigma": SIGMA_TARGET,
        "tolerance": LAMBDA_TOL_COS,
        "N": N,
        "results": results,
        "pass_seeds": pass_seeds,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Results: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    smoke = "--smoke" in sys.argv
    N = 16 if smoke else 32
    main(N=N, smoke=smoke)
