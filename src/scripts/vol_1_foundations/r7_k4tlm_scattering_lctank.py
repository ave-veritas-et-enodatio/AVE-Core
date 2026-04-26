"""R7.1 multi-seed K4-TLM scatter+connect transmission eigenmode + Cosserat (u,ω)
LC-tank Hessian-of-W eigenmode sweep — fresh-session implementation of
P_phase6_k4tlm_scattering_lctank per doc 73_ §2-§5.

Per [doc 73_](../../research/L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md):
discrete K4-TLM scatter+connect transmission operator T = C·S(z_local) for the V-block
(unitary eigenvalue problem with eigenvalues on unit circle), Cosserat (u,ω) LC-tank
Hessian-of-W for the Cos-block (real-symmetric eigenvalue problem), Op14 cross-coupling
that vanishes at V=0 seed → block decoupled.

Per Rule-10 commitment in doc 73_ §6: this is reframe 4 of R7.1 with §6.1 catastrophic-
error carve-out invoked on-record per Grant approval ("confirmed 6.1" 2026-04-25).
Subsequent run is committed to operator choice barring catastrophic methodology error.

References:
- research/L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md (active methodology)
- manuscript/predictions.yaml::P_phase6_k4tlm_scattering_lctank (frozen pre-reg)
- src/ave/core/k4_tlm.py:36-65 build_scattering_matrix (S block)
- src/ave/core/k4_tlm.py:348-426 _connect_all (C connect operator structure)
- src/ave/topological/cosserat_field_3d.py energy_gradient (Cos-block HVP)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse import lil_matrix, csr_matrix, csc_matrix, diags
from scipy.sparse.linalg import eigs, eigsh, LinearOperator

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D
from ave.core.k4_tlm import build_scattering_matrix


# ─── Pre-registered constants (frozen per doc 73_ §2-§5) ─────────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi

ALPHA = 1.0 / 137.036
OMEGA_COMPTON = 1.0
DT = 1.0 / np.sqrt(2.0)        # K4-TLM timestep dt = dx/(c·√2) per k4_tlm.py:144
TARGET_PHASE = OMEGA_COMPTON * DT      # ≈ 0.7071 rad — V-block target eigenvalue phase
TARGET_LAMBDA_COS = OMEGA_COMPTON ** 2  # = 1.0 — Cos-block target eigenvalue

PHASE_TOL_V = ALPHA * TARGET_PHASE      # ≈ 0.00516 rad for V-block PASS
LAMBDA_TOL_COS = ALPHA * OMEGA_COMPTON  # ≈ 0.00731 for Cos-block PASS (on √λ)

A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
EIGENMODES_V = 20
EIGENMODES_COS = 100   # bumped from 20: K_cos has ~9-dim null space (rigid u/ω modes); need wider span to reach ω_C² level
NULL_SKIP_THRESH = 1e-6  # eigenvalues below this treated as null-space artifacts

F17K_COS_RATIO = 3.40
F17K_S11_RATIO = 1.03

# K4-TLM tetrahedral port offsets (A→B). B→A is exact negative.
PORTS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=int)

OUTPUT_JSON = Path(__file__).parent / "r7_k4tlm_scattering_lctank_results.json"


# ─── Engine setup ────────────────────────────────────────────────────────────


def build_engine() -> VacuumEngine3D:
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_2_3_hedgehog(engine, R, r):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True,
        amplitude_scale=A26_AMP_SCALE,
    )


def seed_random_low(engine, peak=0.05):
    rng = np.random.default_rng(seed=42)
    omega = rng.uniform(-peak, peak, size=engine.cos.omega.shape)
    omega *= engine.cos.mask_alive[..., None]
    engine.cos.omega = omega
    engine.cos.omega_dot[...] = 0.0
    engine.cos.u[...] = 0.0
    engine.cos.u_dot[...] = 0.0


def a26_guard(engine, seed_name):
    peak = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    if seed_name.startswith("GT") or seed_name.startswith("F17K"):
        if not (A26_GUARD_LOW <= peak <= A26_GUARD_HIGH):
            raise AssertionError(
                f"A26 GUARD FAILED for '{seed_name}': peak |ω|={peak:.4f}"
            )
    return peak


# ─── V-block: K4-TLM scatter+connect transmission operator T = C·S ───────────


def compute_z_local_field(engine):
    """Op14 z_local from Cosserat A² at V=0 seed."""
    omega = np.asarray(engine.cos.omega)
    omega_yield = engine.cos.omega_yield
    A_sq = np.sum(omega ** 2, axis=-1) / (omega_yield ** 2)
    A_sq_clipped = np.minimum(A_sq, 1.0 - 1e-6)
    S = np.sqrt(1.0 - A_sq_clipped)
    return 1.0 / np.maximum(np.sqrt(S), 1e-6)


def get_active_sites(N):
    """Return list of (x, y, z) for K4-TLM active sites: all-even ∪ all-odd.
    Returns dict mapping (x,y,z) → flat global index 0..N_active-1.
    """
    sites = {}
    idx = 0
    for x in range(N):
        for y in range(N):
            for z in range(N):
                all_even = (x % 2 == 0) and (y % 2 == 0) and (z % 2 == 0)
                all_odd = (x % 2 == 1) and (y % 2 == 1) and (z % 2 == 1)
                if all_even or all_odd:
                    sites[(x, y, z)] = idx
                    idx += 1
    return sites


def is_A_site(x, y, z):
    return (x % 2 == 0) and (y % 2 == 0) and (z % 2 == 0)


def build_T_operator(engine):
    """Build sparse T = C_op3 · S ∈ ℂ^{4N_active × 4N_active} for the V-block.

    BUG-FIX 2026-04-25 (post-first-run analysis): the previous version called
    build_scattering_matrix(z_local) which returns 0.5·11ᵀ - I regardless of
    z_local (because all 4 ports of a single K4 node share the same z, so
    2y/y_total = 0.5 cancels). z_local in K4-TLM enters via OP3 BOND REFLECTION
    in _connect_all (k4_tlm.py:393-415), NOT in the per-node scatter.

    Per Op3 bond reflection: for port p of site i with neighbor j at PORTS[p]
    (or -PORTS[p] for B-site), the connect step reads:
        V_inc(t+dt)[i, p] = γ_ij · V_ref[i, p] + T_ij · V_ref[j, p]
    where γ_ij = (z_j - z_i)/(z_j + z_i), T_ij = √(1 - γ_ij²).

    So T_op3 = C_op3 · S where C_op3 row (i, p) has 2 nonzeros: γ at (i, p) and
    T_ij at (j_neighbor, p). After multiplying with S (block-diag, 0.5-δ within
    each site block), T_op3 row (i, p) has 8 nonzeros total.
    """
    N = engine.cos.nx
    z_local = compute_z_local_field(engine)
    sites = get_active_sites(N)
    n_active = len(sites)
    n_total = 4 * n_active
    EPS = 1e-12

    T = lil_matrix((n_total, n_total), dtype=complex)

    # Pre-compute the universal 4×4 scatter matrix block: S_pq = 0.5 - δ_pq.
    # (Same for every site; impedance variation is handled by C_op3 below.)
    S_block = 0.5 * np.ones((4, 4)) - np.eye(4)

    for (x, y, z), i_global in sites.items():
        sign = +1 if is_A_site(x, y, z) else -1
        z_self = z_local[x, y, z]

        for p_t in range(4):
            offset = sign * PORTS[p_t]
            nx, ny, nz = (x + offset[0]) % N, (y + offset[1]) % N, (z + offset[2]) % N
            if (nx, ny, nz) not in sites:
                continue
            j_neighbor = sites[(nx, ny, nz)]

            z_nbr = z_local[nx, ny, nz]
            gamma = (z_nbr - z_self) / (z_nbr + z_self + EPS)
            T_trans = float(np.sqrt(max(0.0, 1.0 - gamma * gamma)))

            # T_op3 row (i_global, p_t):
            #   own-site contributions:    gamma · S_block[p_t, q]  at columns (i_global, q)
            #   neighbor contributions:    T_trans · S_block[p_t, q]  at columns (j_neighbor, q)
            row = 4 * i_global + p_t
            for q in range(4):
                # own-site reflection (i, q)
                col_self = 4 * i_global + q
                T[row, col_self] += complex(gamma * S_block[p_t, q])
                # neighbor transmission (j_neighbor, q)
                col_nbr = 4 * j_neighbor + q
                T[row, col_nbr] += complex(T_trans * S_block[p_t, q])

    return T.tocsc(), sites, n_active


def eigsolve_V_block(engine, k=EIGENMODES_V):
    """Eigsolve T = C·S for k eigenvalues nearest target phase exp(i·ω_C·dt)."""
    print(f"    Building T = C·S(z_local) sparse operator...", flush=True)
    t0 = time.time()
    T, sites, n_active = build_T_operator(engine)
    print(f"      T built in {time.time() - t0:.1f}s; dim={T.shape[0]}, nnz={T.nnz}")

    sigma = complex(np.cos(TARGET_PHASE), np.sin(TARGET_PHASE))
    print(f"    Eigsolve V-block at sigma=exp(i·{TARGET_PHASE:.4f})...", flush=True)
    t1 = time.time()
    try:
        # eigs is general (not symmetric); shift-invert with sigma for unitary T.
        # For T unitary, eigenvalues lie on unit circle.
        eigvals, eigvecs = eigs(T, k=k, sigma=sigma, which='LM',
                                tol=1e-6, maxiter=2000)
        print(f"      V-block eigsolve: {time.time() - t1:.1f}s, {len(eigvals)} eigenvalues")
    except Exception as e:
        print(f"      V-block eigsolve ERROR: {e}")
        return {"eigvals": None, "eigvecs": None, "n_active": n_active, "error": str(e)}

    return {
        "eigvals": eigvals,  # complex array
        "eigvecs": eigvecs,  # complex (4·n_active, k)
        "n_active": n_active,
        "sites_dict": sites,
        "error": None,
    }


# ─── Cos-block: Hessian-of-W on (u, ω) joint via FD HVP ──────────────────────


def build_K_cos_op(engine, eps=1e-5):
    """LinearOperator for K_cos = ∂²W/∂(u,ω)² at the seed configuration via FD HVP.

    State vector: ψ_cos = [u_flat, ω_flat] of size 6·N³.
    """
    u_seed = engine.cos.u.copy()
    omega_seed = engine.cos.omega.copy()
    n_total_per_field = u_seed.size  # 3·N³
    n_state = 2 * n_total_per_field  # 6·N³

    def matvec(v_flat):
        v = np.asarray(v_flat, dtype=np.float64)
        v_u = v[:n_total_per_field].reshape(u_seed.shape)
        v_w = v[n_total_per_field:].reshape(omega_seed.shape)

        # Forward
        engine.cos.u = u_seed + eps * v_u
        engine.cos.omega = omega_seed + eps * v_w
        dE_du_p, dE_dw_p = engine.cos.energy_gradient()

        # Backward
        engine.cos.u = u_seed - eps * v_u
        engine.cos.omega = omega_seed - eps * v_w
        dE_du_m, dE_dw_m = engine.cos.energy_gradient()

        # Restore
        engine.cos.u = u_seed.copy()
        engine.cos.omega = omega_seed.copy()

        Hv_u = (np.asarray(dE_du_p) - np.asarray(dE_du_m)) / (2.0 * eps)
        Hv_w = (np.asarray(dE_dw_p) - np.asarray(dE_dw_m)) / (2.0 * eps)
        return np.concatenate([Hv_u.flatten(), Hv_w.flatten()])

    return LinearOperator(shape=(n_state, n_state), matvec=matvec, dtype=np.float64)


def build_M_cos(engine):
    """Mass matrix M_cos = block-diag(ρ·I, I_ω·I) sparse diagonal."""
    rho = engine.cos.rho
    I_omega = engine.cos.I_omega
    n_per_field = engine.cos.u.size
    diag = np.concatenate([
        rho * np.ones(n_per_field),
        I_omega * np.ones(n_per_field),
    ])
    return diags(diag).tocsr()


def eigsolve_Cos_block(engine, k=EIGENMODES_COS):
    """Eigsolve K_cos · δψ = ω² · M_cos · δψ for k smallest-algebraic eigenvalues."""
    print(f"    Building K_cos LinearOperator (FD HVP)...", flush=True)
    K_op = build_K_cos_op(engine)
    M = build_M_cos(engine)
    n_state = K_op.shape[0]

    print(f"    Eigsolve Cos-block (dim={n_state}, k={k})...", flush=True)
    t0 = time.time()
    eigvals, eigvecs, eigsolve_mode = None, None, None

    # Try 'SA' first (smallest algebraic — covers negative eigenvalues at
    # non-stationary seeds). If no convergence, fall back to 'LM' (largest
    # magnitude — well-converged for ARPACK regular mode) which finds the
    # extremes of the spectrum. Both contribute info; 'LM' gives the high-frequency
    # modes which may still include a candidate near ω_C if the bound state has
    # large positive eigenvalue.
    for mode_try, tol_try, maxiter_try in [
        ('SA', 1e-3, 5000),
        ('LM', 1e-3, 5000),
    ]:
        try:
            eigvals, eigvecs = eigsh(
                K_op, M=M, k=k,
                which=mode_try, tol=tol_try, maxiter=maxiter_try,
            )
            eigsolve_mode = mode_try
            print(f"      Cos-block eigsolve: {time.time() - t0:.1f}s, "
                  f"{len(eigvals)} eigenvalues (mode={mode_try})")
            break
        except Exception as e:
            print(f"      Cos-block eigsolve ({mode_try}) ERROR: {e}")
            continue

    if eigvals is None:
        return {"eigvals": None, "eigvecs": None, "mode": None,
                "error": "Both SA and LM modes failed to converge"}

    idx = np.argsort(eigvals)
    return {
        "eigvals": eigvals[idx],
        "eigvecs": eigvecs[:, idx],
        "mode": eigsolve_mode,
        "error": None,
    }


# ─── Eigenmode diagnostics ────────────────────────────────────────────────────


def check_V_block_at_compton(eigvals):
    """For complex eigvals (unitary, |λ|=1), find one with phase nearest ω_C·dt."""
    if eigvals is None or len(eigvals) == 0:
        return False, -1, np.inf, None
    phases = np.angle(eigvals)  # [-π, π]
    diffs = np.abs(phases - TARGET_PHASE)
    # Also check near -TARGET_PHASE (eigenmodes come in conjugate pairs)
    diffs_neg = np.abs(phases - (-TARGET_PHASE))
    diffs_combined = np.minimum(diffs, diffs_neg)
    idx = int(np.argmin(diffs_combined))
    rel_diff = float(diffs_combined[idx] / abs(TARGET_PHASE))
    is_close = diffs_combined[idx] < PHASE_TOL_V
    return is_close, idx, rel_diff, float(phases[idx])


def check_Cos_block_at_compton(eigvals):
    """For real eigvals (Hessian, mixed sign with ~9-dim null space from rigid-body modes),
    skip near-zero (null-space) eigenvalues and find positive one with √λ nearest ω_C."""
    if eigvals is None or len(eigvals) == 0:
        return False, -1, np.inf
    # Filter: positive AND above null-space threshold
    nontrivial_mask = eigvals > NULL_SKIP_THRESH
    if not np.any(nontrivial_mask):
        return False, -1, np.inf
    nontrivial_indices = np.where(nontrivial_mask)[0]
    sqrt_lam = np.sqrt(eigvals[nontrivial_mask])
    diffs = np.abs(sqrt_lam - OMEGA_COMPTON)
    idx_in_nt = int(np.argmin(diffs))
    rel_diff = float(diffs[idx_in_nt] / OMEGA_COMPTON)
    idx_orig = int(nontrivial_indices[idx_in_nt])
    is_close = diffs[idx_in_nt] < LAMBDA_TOL_COS
    return is_close, idx_orig, rel_diff


def crossing_count_cos_eigvec(eigvec, engine):
    """Compute c_eigvec on the ω-component of the (u, ω) joint eigenvector."""
    n_per_field = engine.cos.u.size
    omega_part = eigvec[n_per_field:]  # latter half
    N = engine.cos.nx
    omega_field = omega_part.reshape(N, N, N, 3)
    saved = engine.cos.omega.copy()
    try:
        engine.cos.omega = omega_field
        c = int(engine.cos.extract_crossing_count())
    except Exception:
        c = -1
    finally:
        engine.cos.omega = saved
    return c


# ─── Per-seed runner ──────────────────────────────────────────────────────────


def run_seed(name, R, r, gt_family):
    print(f"\n  ── seed: {name} ──")
    print(f"    Target (R, r) = ({R:.3f}, {r:.3f}); GT-family = {gt_family}")

    t_start = time.time()
    engine = build_engine()
    if name == "vacuum_control":
        seed_random_low(engine)
    else:
        seed_2_3_hedgehog(engine, R, r)

    peak = a26_guard(engine, name)
    print(f"    A26 guard OK (peak |ω|={peak:.4f})")

    V_result = eigsolve_V_block(engine, k=EIGENMODES_V)
    Cos_result = eigsolve_Cos_block(engine, k=EIGENMODES_COS)

    V_close, V_idx, V_rel_diff, V_phase = check_V_block_at_compton(V_result["eigvals"])
    Cos_close, Cos_idx, Cos_rel_diff = check_Cos_block_at_compton(Cos_result["eigvals"])

    cos_c_eigvec = -1
    if Cos_close and Cos_result["eigvecs"] is not None:
        try:
            cos_c_eigvec = crossing_count_cos_eigvec(
                Cos_result["eigvecs"][:, Cos_idx], engine
            )
        except Exception as e:
            print(f"    crossing-count error: {e}")

    eigenmode_found = V_close or Cos_close
    elapsed = time.time() - t_start
    print(f"    V-block: close={V_close} (rel_diff={V_rel_diff:.4e}, phase={V_phase})")
    print(f"    Cos-block: close={Cos_close} (rel_diff={Cos_rel_diff:.4e}, c_eigvec={cos_c_eigvec})")
    print(f"    Total seed time: {elapsed:.1f}s")

    return {
        "seed_name": name,
        "R": R, "r": r,
        "gt_family": gt_family,
        "peak_omega_seed": peak,
        "V_block": {
            "eigvals_real": (V_result["eigvals"].real.tolist() if V_result["eigvals"] is not None else None),
            "eigvals_imag": (V_result["eigvals"].imag.tolist() if V_result["eigvals"] is not None else None),
            "n_active": V_result["n_active"],
            "close_to_omega_C": V_close,
            "rel_diff": V_rel_diff,
            "phase_closest": V_phase,
            "error": V_result["error"],
        },
        "Cos_block": {
            "eigvals": (Cos_result["eigvals"].tolist() if Cos_result["eigvals"] is not None else None),
            "close_to_omega_C": Cos_close,
            "rel_diff": Cos_rel_diff,
            "c_eigvec_closest": cos_c_eigvec,
            "error": Cos_result["error"],
        },
        "eigenmode_found_at_omega_C": eigenmode_found,
        "elapsed_seconds": elapsed,
    }


# ─── Three-mode falsification ─────────────────────────────────────────────────


def adjudicate(results):
    GT_pass = results["GT_corpus"].get("eigenmode_found_at_omega_C", False)
    F17K_cos_pass = results["F17K_cos_endpoint"].get("eigenmode_found_at_omega_C", False)
    F17K_s11_pass = results["F17K_s11_endpoint"].get("eigenmode_found_at_omega_C", False)
    vacuum_pass = results["vacuum_control"].get("eigenmode_found_at_omega_C", False)

    if GT_pass:
        mode = "I"
        reading = "Corpus Golden Torus geometry vindicated."
    elif F17K_cos_pass or F17K_s11_pass:
        mode = "II"
        reading = (
            f"Engine basin at F17-K endpoint, NOT corpus GT. "
            f"F17K_cos={F17K_cos_pass}, F17K_s11={F17K_s11_pass}."
        )
    else:
        mode = "III"
        reading = (
            "No eigenmode at ω_C at any tested seed. (2,3) representation "
            "needs structural rework OR bound state hybrid V≠0∧ω≠0 (Round 8)."
        )

    return {
        "mode": mode,
        "reading": reading,
        "GT_corpus_pass": GT_pass,
        "F17K_cos_pass": F17K_cos_pass,
        "F17K_s11_pass": F17K_s11_pass,
        "vacuum_control_pass": vacuum_pass,
        "negative_control_failure": vacuum_pass,
    }


# ─── Main ────────────────────────────────────────────────────────────────────


def main():
    print("=" * 78, flush=True)
    print("  R7.1 K4-TLM scatter+connect + Cosserat LC-tank Hessian eigenmode sweep")
    print("  P_phase6_k4tlm_scattering_lctank (frozen, reframe 4 per doc 73_ §6.1)")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}, R_anchor={R_ANCHOR}")
    print(f"  V-block target: phase ω_C·dt = {TARGET_PHASE:.4f} rad on unit circle, tol {PHASE_TOL_V:.4e}")
    print(f"  Cos-block target: λ = ω_C² = {TARGET_LAMBDA_COS}, tol {LAMBDA_TOL_COS:.4e} on √λ")

    seed_specs = [
        ("GT_corpus",          R_ANCHOR, R_ANCHOR / PHI_SQ,         True),
        ("F17K_cos_endpoint",  R_ANCHOR, R_ANCHOR / F17K_COS_RATIO, True),
        ("F17K_s11_endpoint",  R_ANCHOR, R_ANCHOR / F17K_S11_RATIO, True),
        ("vacuum_control",     0.0,      0.0,                        False),
    ]

    results = {}
    for name, R, r, gt_family in seed_specs:
        try:
            results[name] = run_seed(name, R, r, gt_family)
        except AssertionError as e:
            results[name] = {"seed_name": name, "fatal_error": str(e)}
            print(f"  HALT: {e}")
            break
        except Exception as e:
            import traceback
            results[name] = {"seed_name": name, "fatal_error": str(e),
                            "traceback": traceback.format_exc()}
            print(f"  ERROR in {name}: {e}")

    print("\n" + "=" * 78, flush=True)
    print("  Three-mode falsification adjudication")
    print("=" * 78, flush=True)
    adj = adjudicate(results) if all("eigenmode_found_at_omega_C" in r for r in results.values()) else {"mode": "INCOMPLETE"}
    print(f"  MODE: {adj.get('mode', '?')}")
    print(f"  Reading: {adj.get('reading', 'incomplete')}")

    payload = {
        "pre_registration": "P_phase6_k4tlm_scattering_lctank",
        "doc": "research/L3_electron_soliton/73_discrete_k4_tlm_lctank_operator.md",
        "constants": {
            "N_LATTICE": N_LATTICE, "R_ANCHOR": R_ANCHOR,
            "OMEGA_COMPTON": OMEGA_COMPTON, "DT": DT,
            "TARGET_PHASE": TARGET_PHASE, "PHASE_TOL_V": PHASE_TOL_V,
            "TARGET_LAMBDA_COS": TARGET_LAMBDA_COS, "LAMBDA_TOL_COS": LAMBDA_TOL_COS,
            "ALPHA": ALPHA,
        },
        "results": results,
        "adjudication": adj,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Results: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
