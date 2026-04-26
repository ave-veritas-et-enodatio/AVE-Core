"""R7.1 multi-seed block Helmholtz eigenmode sweep — fresh-session implementation
of P_phase6_helmholtz_eigenmode_sweep per doc 72_ §3.

Per [doc 72_ §3.1](../../research/L3_electron_soliton/72_vacuum_impedance_design_space.md):
block Helmholtz on joint (V, ω) state. At V=0 seed, cross-blocks vanish per §3.1.1
(Op14 is multiplicative in V); block matrix decouples; eigsh runs on V-block
and ω-block separately.

Per Rule-10 commitment in doc 72_ §6.1: this is reframe 3 of R7.1; subsequent run
is committed to operator choice. Post-run methodology adjustments allowed; pre-run
reframe 4 is not, except for catastrophic methodology error.

ENGINEERING APPROXIMATIONS (documented honestly for post-run interpretation):

1. K_V via weighted K4 graph Laplacian (extending k4_greens_function.py pattern)
   with bond admittances y_ij = 2/(z_i + z_j) where z = (1 - A²)^(-1/4) per
   _update_z_local_total in k4_cosserat_coupling.py. Uses one V per lattice site
   (not per K4 port). This is a SIMPLIFICATION of the full 4-port K4-TLM scatter+
   connect dynamics. Captures Helmholtz spatial structure but may not exactly
   reproduce K4-TLM dispersion. Sufficient for binary "is there an eigenmode at
   ω_Compton?" check; details of mode shape may differ from full TLM.

2. K_ω via finite-difference Hessian-vector product on engine.cos.energy_gradient
   wrapped as scipy.sparse.linalg.LinearOperator. Avoids materializing 100K×100K
   Hessian. Lanczos in eigsh uses ~50 HVP per converged eigenvalue.

3. Engine natural units throughout: ω_Compton = 1, c = 1, ℓ_node = 1, ℏ = 1,
   m_e = 1. So eigenvalue target is λ = ω_C² = 1.0.

4. V=0 at seed (block decouples per §3.1.1). Block Helmholtz answers a strict
   superset of single-sector V Helmholtz (returns V-block + ω-block in one run);
   does not address genuinely hybrid V≠0 ∧ ω≠0 modes (Round 8).

References:
- research/L3_electron_soliton/72_vacuum_impedance_design_space.md (active methodology)
- research/L3_electron_soliton/71_multi_seed_eigenmode_sweep.md §15 (active scope)
- manuscript/predictions.yaml::P_phase6_helmholtz_eigenmode_sweep (frozen pre-reg)
- src/scripts/vol_1_foundations/k4_greens_function.py (K4 Laplacian pattern reused)
- src/ave/topological/cosserat_field_3d.py (energy_gradient via JAX autograd)
- src/ave/topological/k4_cosserat_coupling.py:_update_z_local_total (Op14 z formula)
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse import lil_matrix, csr_matrix, diags
from scipy.sparse.linalg import eigsh, LinearOperator

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.topological.vacuum_engine import VacuumEngine3D


# ─── Pre-registered constants (per doc 72_ §3.1, frozen at commit 675141e) ────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI                          # ≈ 2.618
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)  # ≈ 0.3464 (recovers 0.3π peak from √3/2·π canonical)
GT_PEAK_OMEGA = 0.3 * np.pi                 # ≈ 0.9425

ALPHA = 1.0 / 137.036
OMEGA_COMPTON = 1.0                         # native units (ℓ_node = 1, c = 1, ℏ = 1, m_e = 1)
LAMBDA_TARGET = OMEGA_COMPTON ** 2          # = 1.0

# Tolerances per pred
EIGENMODE_FREQ_TOL = ALPHA * OMEGA_COMPTON  # |√λ - ω_C| < α·ω_C
Q_TARGET = 1.0 / ALPHA                      # ≈ 137.036
Q_TOL_REL = 0.05                             # ±5%
SHAPE_CORR_INFORMATIONAL_THRESH = 0.60      # Q4 two-tier: informational, not PASS

A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA

# Lattice geometry per pred
N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
EIGENMODES_PER_BLOCK = 10                   # k=10 in eigsh, find 10 modes near sigma

# F17-K v2-v2 endpoint ratios per pred
F17K_COS_RATIO = 3.40                       # Cosserat-energy descent endpoint
F17K_S11_RATIO = 1.03                       # Coupled-S₁₁ descent endpoint

OUTPUT_JSON = Path(__file__).parent / "r7_helmholtz_eigenmode_sweep_results.json"


# ─── Engine setup ────────────────────────────────────────────────────────────


def build_engine() -> VacuumEngine3D:
    """A28 + Cosserat self-terms enabled. Post-Round-6 default."""
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,    # A28
        enable_cosserat_self_terms=True,   # Cosserat self-terms restored under A28
    )


def seed_2_3_hedgehog(engine: VacuumEngine3D, R: float, r: float) -> None:
    """A26-corrected (2,3) hedgehog at given (R, r). V=0 implicit."""
    engine.cos.initialize_electron_2_3_sector(
        R_target=R, r_target=r, use_hedgehog=True,
        amplitude_scale=A26_AMP_SCALE,
    )


def seed_random_low(engine: VacuumEngine3D, peak: float = 0.05) -> None:
    """Vacuum-control seed: small uniform-random ω, V=0."""
    rng = np.random.default_rng(seed=42)
    omega = rng.uniform(-peak, peak, size=engine.cos.omega.shape)
    omega *= engine.cos.mask_alive[..., None]
    engine.cos.omega = omega
    engine.cos.omega_dot[...] = 0.0
    engine.cos.u[...] = 0.0
    engine.cos.u_dot[...] = 0.0


# ─── A26 contamination guard (per §4 of v1, retained) ────────────────────────


def a26_guard(engine: VacuumEngine3D, seed_name: str) -> float:
    peak = float(np.linalg.norm(np.asarray(engine.cos.omega), axis=-1).max())
    if seed_name.startswith("GT") or seed_name.startswith("F17K"):
        if not (A26_GUARD_LOW <= peak <= A26_GUARD_HIGH):
            raise AssertionError(
                f"A26 GUARD FAILED for '{seed_name}': peak |ω|={peak:.4f} "
                f"outside [{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}] "
                f"(target 0.3π={GT_PEAK_OMEGA:.4f})."
            )
    return peak


# ─── Op14 z_local at the seed Cosserat configuration ─────────────────────────


def compute_z_local_field(engine: VacuumEngine3D) -> np.ndarray:
    """Return z(x) = (1 - A²(x))^(-1/4) per Vol 1 Ch 7:252 / k4_cosserat_coupling.py.

    A²(x) at V=0 seed comes from Cosserat ω only (K4 V_inc=0):
       A² = |ω|² / ω_yield²    (Cosserat strain saturation contribution)

    Returns shape (nx, ny, nz). Clipped to avoid divergence at A²→1.
    """
    omega = np.asarray(engine.cos.omega)
    omega_yield = engine.cos.omega_yield
    A_sq = np.sum(omega ** 2, axis=-1) / (omega_yield ** 2)
    A_sq_clipped = np.minimum(A_sq, 1.0 - 1e-6)
    S = np.sqrt(1.0 - A_sq_clipped)
    z_local = 1.0 / np.maximum(np.sqrt(S), 1e-6)  # = (1 - A²)^(-1/4)
    return z_local


# ─── K_V: weighted K4 graph Laplacian with Op14 z_local bond admittances ─────


def build_K_V(engine: VacuumEngine3D) -> csr_matrix:
    """Sparse symmetric K4 graph Laplacian with bond admittances
    y_ij = 2/(z_i + z_j) (parallel-impedance composition).

    Engineering approximation: uses one V per lattice site (not per K4 port),
    extending k4_greens_function.py pattern. Captures Helmholtz spatial
    structure; may not exactly reproduce 4-port K4-TLM dispersion.

    Returns sparse N³×N³ symmetric matrix.
    """
    N = engine.cos.nx  # cubic lattice
    n_total = N * N * N
    z_local = compute_z_local_field(engine).flatten()  # shape (N³,)

    # K4 tetrahedral bonds per k4_greens_function.py
    PORTS = np.array([
        [+1, +1, +1],
        [+1, -1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
    ], dtype=int)

    L = lil_matrix((n_total, n_total), dtype=float)
    indices = np.arange(n_total).reshape(N, N, N)

    for x in range(N):
        for y in range(N):
            for z_idx in range(N):
                parity = (x + y + z_idx) % 2
                sign = +1 if parity == 0 else -1
                i = indices[x, y, z_idx]
                z_i = z_local[i]
                for p in PORTS:
                    nx_ = (x + sign * p[0]) % N
                    ny_ = (y + sign * p[1]) % N
                    nz_ = (z_idx + sign * p[2]) % N
                    j = indices[nx_, ny_, nz_]
                    z_j = z_local[j]
                    y_ij = 2.0 / (z_i + z_j)
                    L[i, j] = -y_ij
                    L[i, i] += y_ij  # accumulate diagonal degree

    return L.tocsr()


# ─── K_ω: Hessian of Cosserat W via finite-difference HVP ────────────────────


def build_K_omega_op(engine: VacuumEngine3D, eps: float = 1e-5) -> LinearOperator:
    """Wrap K_ω = ∂²W/∂ω² as scipy LinearOperator using FD HVP.

    For each Hv probe:
        H·v ≈ [grad_W(ω + ε·v) - grad_W(ω - ε·v)] / (2ε)

    Avoids materializing 3·N³ × 3·N³ Hessian. Lanczos in eigsh runs ~50 probes
    per converged eigenvalue; total cost ~500 grad evaluations for k=10.
    """
    omega_seed = engine.cos.omega.copy()
    u_seed = engine.cos.u.copy()
    n_omega = omega_seed.size  # 3·N³

    def matvec(v_flat):
        """Compute H·v (returns flat array same size as v_flat)."""
        v = v_flat.reshape(omega_seed.shape).astype(np.float64)

        # Forward perturbation
        engine.cos.omega = omega_seed + eps * v
        engine.cos.u = u_seed.copy()
        _, dW_domega_plus = engine.cos.energy_gradient()

        # Backward perturbation
        engine.cos.omega = omega_seed - eps * v
        engine.cos.u = u_seed.copy()
        _, dW_domega_minus = engine.cos.energy_gradient()

        # Restore seed
        engine.cos.omega = omega_seed.copy()
        engine.cos.u = u_seed.copy()

        Hv = (np.asarray(dW_domega_plus) - np.asarray(dW_domega_minus)) / (2.0 * eps)
        return Hv.flatten()

    return LinearOperator(shape=(n_omega, n_omega), matvec=matvec, dtype=np.float64)


# ─── Eigsolve helpers ─────────────────────────────────────────────────────────


def eigsolve_V_block(engine: VacuumEngine3D, k: int = EIGENMODES_PER_BLOCK) -> dict:
    """Eigsolve K_V at the seed Cosserat configuration. Returns eigenvalues (=ω²)
    and eigenvectors (mode shapes on the V grid).

    Uses 'SM' (smallest magnitude) without sigma-shift since the K4 graph Laplacian
    has a constant zero-mode and shift-invert is unstable at σ near eigenvalues.
    Find k smallest eigenvalues; check after if any lies near ω_C² = 1.
    """
    from scipy.sparse import eye as sp_eye
    K_V = build_K_V(engine)
    M_V = sp_eye(K_V.shape[0], format='csr')
    try:
        eigvals, eigvecs = eigsh(
            K_V, M=M_V, k=k,
            which='SM',  # smallest magnitude — no shift-invert
            tol=1e-6, maxiter=10000,
        )
    except Exception as e:
        return {"eigvals": None, "eigvecs": None, "error": str(e)}
    # Sort by eigenvalue ascending
    idx = np.argsort(eigvals)
    return {
        "eigvals": eigvals[idx],
        "eigvecs": eigvecs[:, idx],
        "error": None,
    }


def eigsolve_omega_block(engine: VacuumEngine3D, k: int = EIGENMODES_PER_BLOCK) -> dict:
    """Eigsolve K_ω = ∂²W/∂ω² at the seed via FD HVP. M_ω = I_omega · I.

    Uses 'SA' (smallest algebraic) without sigma-shift; LinearOperator can't
    support shift-invert without explicit OPinv.
    """
    K_omega_op = build_K_omega_op(engine)
    I_omega = engine.cos.I_omega
    n_omega = engine.cos.omega.size
    # M = I_omega·I
    M_op = diags(I_omega * np.ones(n_omega)).tocsr()
    try:
        eigvals, eigvecs = eigsh(
            K_omega_op, M=M_op, k=k,
            which='SA',  # smallest algebraic — no shift-invert needed for LinearOperator
            tol=1e-5, maxiter=2000,
        )
    except Exception as e:
        return {"eigvals": None, "eigvecs": None, "error": str(e)}
    idx = np.argsort(eigvals)
    return {
        "eigvals": eigvals[idx],
        "eigvecs": eigvecs[:, idx],
        "error": None,
    }


# ─── Eigenmode diagnostics per pred PASS criteria ─────────────────────────────


def check_omega_compton(eigvals: np.ndarray) -> tuple[bool, int, float]:
    """Return (any_close, idx_closest, |√λ - ω_C|/ω_C of closest)."""
    if eigvals is None or len(eigvals) == 0:
        return False, -1, np.inf
    pos = eigvals[eigvals > 0]
    if len(pos) == 0:
        return False, -1, np.inf
    sqrt_lam = np.sqrt(pos)
    diffs = np.abs(sqrt_lam - OMEGA_COMPTON)
    idx_in_pos = int(np.argmin(diffs))
    rel_diff = float(diffs[idx_in_pos] / OMEGA_COMPTON)
    # Map back to original index
    pos_indices = np.where(eigvals > 0)[0]
    idx_orig = int(pos_indices[idx_in_pos])
    is_close = rel_diff < ALPHA
    return is_close, idx_orig, rel_diff


def compute_Q_factor_from_eigvec(eigvec: np.ndarray, eigval: float, sector: str,
                                  engine: VacuumEngine3D) -> float | None:
    """Q-factor from boundary impedance — informational at V=0 seed.

    For V-block: Q ≈ k / (2·imag(k_complex)) but eigsh returns real eigenvalues
    for symmetric operator; Q diverges. We approximate Q ~ 1/(boundary loss
    estimate) using PML attenuation profile if available.

    For ω-block: Cosserat constitutive Q = ω·η_storage / η_loss. At zero damping
    in W functional, Q diverges; we use spectral spread as a proxy.

    For first-pass: report Q = NaN. Q-factor extraction is a known TODO — eigsh
    returns Hermitian spectrum so loss isn't encoded. Future: solve non-Hermitian
    boundary-coupled problem with PML absorption to get complex eigenvalues.
    """
    return None  # known limitation; see notes


def crossing_count_v_eigvec(eigvec: np.ndarray, sector: str, engine: VacuumEngine3D) -> int:
    """For ω-block eigenvector (shape (N³, 3) → (N, N, N, 3)), use existing
    extract_crossing_count helper. For V-block (scalar field on N³), crossing-count
    isn't well-defined in the Cosserat-ω sense — return -1 (informational only).
    """
    if sector != "omega":
        return -1
    N = engine.cos.nx
    omega_field = eigvec.reshape(N, N, N, 3)
    saved = engine.cos.omega.copy()
    try:
        engine.cos.omega = omega_field
        c = int(engine.cos.extract_crossing_count())
    finally:
        engine.cos.omega = saved
    return c


# ─── Per-seed runner ──────────────────────────────────────────────────────────


def run_seed(name: str, R: float, r: float, gt_family: bool) -> dict:
    print(f"\n  ── seed: {name} ──")
    print(f"    Target (R, r) = ({R:.3f}, {r:.3f}); GT-family = {gt_family}")

    t0 = time.time()
    engine = build_engine()

    if name == "vacuum_control":
        seed_random_low(engine)
    else:
        seed_2_3_hedgehog(engine, R, r)

    peak = a26_guard(engine, name)
    print(f"    A26 guard OK (peak |ω|={peak:.4f})")

    # V-block eigsolve
    print(f"    Building K_V (sparse weighted K4 Laplacian)...", flush=True)
    t_kv = time.time()
    V_result = eigsolve_V_block(engine, k=EIGENMODES_PER_BLOCK)
    print(f"      V-block eigsolve: {time.time() - t_kv:.1f}s, "
          f"{'ok' if V_result['error'] is None else 'ERROR: ' + V_result['error']}")

    # ω-block eigsolve
    print(f"    Building K_ω (FD HVP LinearOperator)...", flush=True)
    t_kw = time.time()
    omega_result = eigsolve_omega_block(engine, k=EIGENMODES_PER_BLOCK)
    print(f"      ω-block eigsolve: {time.time() - t_kw:.1f}s, "
          f"{'ok' if omega_result['error'] is None else 'ERROR: ' + omega_result['error']}")

    # Check ω_Compton hits per block
    V_close, V_idx, V_diff = check_omega_compton(V_result["eigvals"])
    omega_close, omega_idx, omega_diff = check_omega_compton(omega_result["eigvals"])

    eigenmode_found = V_close or omega_close

    # Topological crossing count for ω-block winner (if any)
    omega_c_eigvec = -1
    if omega_close and omega_result["eigvecs"] is not None:
        try:
            omega_c_eigvec = crossing_count_v_eigvec(
                omega_result["eigvecs"][:, omega_idx], "omega", engine
            )
        except Exception as e:
            print(f"    crossing-count error: {e}")

    elapsed = time.time() - t0
    print(f"    Eigenmode-at-ω_Compton: V_close={V_close} (rel_diff={V_diff:.4e}), "
          f"ω_close={omega_close} (rel_diff={omega_diff:.4e})")
    if omega_close:
        print(f"      ω-block c_eigvec = {omega_c_eigvec} (target=3)")
    print(f"    Total seed time: {elapsed:.1f}s")

    return {
        "seed_name": name,
        "R": R, "r": r,
        "gt_family": gt_family,
        "peak_omega_seed": peak,
        "V_block": {
            "eigvals": V_result["eigvals"].tolist() if V_result["eigvals"] is not None else None,
            "close_to_omega_C": V_close,
            "rel_diff": V_diff,
            "error": V_result["error"],
        },
        "omega_block": {
            "eigvals": omega_result["eigvals"].tolist() if omega_result["eigvals"] is not None else None,
            "close_to_omega_C": omega_close,
            "rel_diff": omega_diff,
            "c_eigvec": omega_c_eigvec,
            "error": omega_result["error"],
        },
        "eigenmode_found_at_omega_C": eigenmode_found,
        "elapsed_seconds": elapsed,
    }


# ─── Three-mode falsification adjudication ───────────────────────────────────


def adjudicate(results: dict[str, dict]) -> dict:
    GT_pass = results["GT_corpus"]["eigenmode_found_at_omega_C"]
    F17K_cos_pass = results["F17K_cos_endpoint"]["eigenmode_found_at_omega_C"]
    F17K_s11_pass = results["F17K_s11_endpoint"]["eigenmode_found_at_omega_C"]
    vacuum_pass = results["vacuum_control"]["eigenmode_found_at_omega_C"]

    # Three-mode resolution per doc 72_ §3.3
    if GT_pass:
        mode = "I"
        reading = "Corpus Golden Torus geometry vindicated as engine bound-state location"
    elif F17K_cos_pass or F17K_s11_pass:
        mode = "II"
        reading = (
            f"Engine basin at F17-K endpoint geometry, NOT corpus GT. "
            f"F17K_cos passes: {F17K_cos_pass}; F17K_s11 passes: {F17K_s11_pass}. "
            "Engine W or corpus geometry derivation needs revision."
        )
    else:
        mode = "III"
        reading = (
            "No eigenmode at ω_Compton at any tested geometry. "
            "(2,3) representation needs structural rework, OR bound state "
            "is genuinely hybrid (V≠0 ∧ ω≠0) requiring V≠0 seed (Round 8)."
        )

    negative_control_failure = vacuum_pass

    return {
        "mode": mode,
        "reading": reading,
        "GT_corpus_pass": GT_pass,
        "F17K_cos_pass": F17K_cos_pass,
        "F17K_s11_pass": F17K_s11_pass,
        "vacuum_control_pass": vacuum_pass,
        "negative_control_failure": negative_control_failure,
    }


# ─── Main ────────────────────────────────────────────────────────────────────


def main() -> dict:
    print("=" * 78)
    print("  R7.1 multi-seed block Helmholtz eigenmode sweep")
    print("  P_phase6_helmholtz_eigenmode_sweep (frozen at commit 675141e)")
    print("=" * 78)
    print(f"  Lattice: N={N_LATTICE}, pml={PML}, R_anchor={R_ANCHOR}")
    print(f"  Target: ω_Compton = {OMEGA_COMPTON} (natural units), λ_target = {LAMBDA_TARGET}")
    print(f"  Eigenmode tolerance: |√λ - ω_C| < α·ω_C = {EIGENMODE_FREQ_TOL:.4e}")
    print()

    seed_specs = [
        ("GT_corpus",          R_ANCHOR, R_ANCHOR / PHI_SQ,        True),
        ("F17K_cos_endpoint",  R_ANCHOR, R_ANCHOR / F17K_COS_RATIO, True),
        ("F17K_s11_endpoint",  R_ANCHOR, R_ANCHOR / F17K_S11_RATIO, True),
        ("vacuum_control",     0.0,      0.0,                       False),
    ]

    results: dict[str, dict] = {}
    for name, R, r, gt_family in seed_specs:
        try:
            results[name] = run_seed(name, R, r, gt_family)
        except AssertionError as e:
            results[name] = {"seed_name": name, "fatal_error": str(e)}
            print(f"  HALT (per A26 guard): {e}")
            break
        except Exception as e:
            import traceback
            results[name] = {
                "seed_name": name,
                "fatal_error": str(e),
                "traceback": traceback.format_exc(),
            }
            print(f"  ERROR in {name}: {e}")

    print("\n" + "=" * 78)
    print("  Three-mode falsification adjudication")
    print("=" * 78)
    if all("eigenmode_found_at_omega_C" in r for r in results.values()):
        adj = adjudicate(results)
        print(f"  MODE: {adj['mode']}")
        print(f"  Reading: {adj['reading']}")
        if adj["negative_control_failure"]:
            print(f"  WARN: vacuum_control returned eigenmode at ω_C — "
                  f"sparse Helmholtz operator may have assembly bug.")
    else:
        adj = {"mode": "INCOMPLETE", "reading": "Some seeds errored; no falsification adjudication possible."}
        print(f"  MODE: INCOMPLETE (some seeds errored)")

    payload = {
        "pre_registration": "P_phase6_helmholtz_eigenmode_sweep",
        "doc": "research/L3_electron_soliton/72_vacuum_impedance_design_space.md",
        "commit_frozen_at": "675141e",
        "constants": {
            "N_LATTICE": N_LATTICE, "R_ANCHOR": R_ANCHOR,
            "OMEGA_COMPTON": OMEGA_COMPTON, "LAMBDA_TARGET": LAMBDA_TARGET,
            "ALPHA": ALPHA, "EIGENMODE_FREQ_TOL": EIGENMODE_FREQ_TOL,
            "Q_TARGET": Q_TARGET,
            "engineering_approximations": [
                "K_V via weighted K4 graph Laplacian (one V per site, not per port) — k4_greens_function.py pattern",
                "K_ω via FD HVP LinearOperator (avoids 100K×100K Hessian materialization)",
                "Q-factor: not extracted (eigsh returns real spectrum; loss requires non-Hermitian PML formulation)",
                "Crossing-count: ω-block only (V-block has no Cosserat winding)",
            ],
        },
        "results": results,
        "adjudication": adj,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\n  Results: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
