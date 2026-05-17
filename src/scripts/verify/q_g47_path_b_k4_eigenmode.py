"""
Q-G47 Path B (doc 127): K=2G operating point eigenmode extraction.

Purpose:
    Per Grant's "phase offset between bulk (C) and shear (L) modes" reframe,
    test whether the K=2G operating point eigenmode of the K4 Keating scaffold
    exhibits a structural quantity ≈ 0.187 ≈ p* = 8πα that could be the
    discrete analogue of the A-029 magic angle u_0*.

    This is a STRUCTURAL VERIFICATION, not an independent re-derivation
    (per doc 126 Picture A caveat: u_0* = r_sec/d - 1 = p*/(8π) may all
    express the same K4 substrate scale).

Method:
    1. Find k_θ/k_a* such that K_relaxed = 2 G_relaxed in the Keating
       scaffold (bisection on Session 15 sweep)
    2. At that operating point, build the full 9-DOF Hessian
       (6 macro-strain components + 3 internal optic-mode components)
    3. Solve eigh(H, M) for eigenfrequencies + eigenvectors
    4. Project each eigenvector onto:
       - K-channel: hydrostatic strain (1 component)
       - G-channel: deviatoric strain (5 components)
       - Internal channel: optic-mode displacement (3 components)
    5. Identify candidate eigenmodes + report all amplitude ratios
       and frequency ratios
    6. Compare against target 0.187 (and related quantities: p* = 8πα,
       √(K_0/G_0 - 2 stuff), etc.)

Output:
    JSON cache + console table for doc 127 inclusion.

Run:
    python src/scripts/verify/q_g47_path_b_k4_eigenmode.py
"""
from __future__ import annotations

import json
import os
import numpy as np
from dataclasses import dataclass, asdict
from scipy.linalg import eigh
from scipy.optimize import brentq, minimize

# Physical constants for comparison targets
ALPHA_INV = 137.035999084
ALPHA = 1.0 / ALPHA_INV

# Target quantities (substrate-scale "0.187 candidates")
TARGETS = {
    "u_0_star_A029": 0.187,                        # A-029 magic angle
    "p_star_8pi_alpha": 8 * np.pi * ALPHA,         # 0.18335 — fabric weave density
    "r_sec_d_minus_1": 0.187,                      # over-bracing 1.187-1
    "sqrt_1_over_42": np.sqrt(1.0 / 42),           # 0.1543 — naive K_0/G_0=5/3 chi_K=12
    "sqrt_1_over_60": np.sqrt(1.0 / 60),           # 0.1291 — naive chi_G=0 case
    "sqrt_1_over_28": np.sqrt(1.0 / 28),           # 0.1890 — K_0/G_0=14/9 case
}

K4_BOND_DIRECTIONS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3.0)


@dataclass
class KeatingBond:
    k_a: float = 1.0
    k_theta: float = 1.0
    d: float = 1.0

    def energy(self, n_hat: np.ndarray, delta_u: np.ndarray) -> float:
        n = n_hat / np.linalg.norm(n_hat)
        axial = float(np.dot(n, delta_u))
        transverse = delta_u - axial * n
        k_s = self.k_theta / self.d**2
        return 0.5 * self.k_a * axial**2 + 0.5 * k_s * float(np.dot(transverse, transverse))


def unit_cell_energy(strain_3x3: np.ndarray, u_int: np.ndarray, bond: KeatingBond) -> float:
    U = 0.0
    for n_hat in K4_BOND_DIRECTIONS:
        delta_u = bond.d * (strain_3x3 @ n_hat) + u_int
        U += bond.energy(n_hat, delta_u)
    return U


def relaxed_energy(strain_3x3: np.ndarray, bond: KeatingBond):
    res = minimize(
        lambda u: unit_cell_energy(strain_3x3, u, bond),
        x0=np.zeros(3),
        method="BFGS",
        tol=1e-14,
    )
    return float(res.fun), res.x


def extract_K_G(bond: KeatingBond, eps: float = 0.01):
    strain_vol = (eps / 3.0) * np.eye(3)
    U_K, _ = relaxed_energy(strain_vol, bond)
    K = 2.0 * U_K / eps**2

    strain_sh = np.zeros((3, 3))
    strain_sh[0, 1] = eps / 2
    strain_sh[1, 0] = eps / 2
    U_G, _ = relaxed_energy(strain_sh, bond)
    G = 2.0 * U_G / eps**2
    return K, G


# ============================================================
# Path B Step 1: locate K=2G operating point
# ============================================================

def find_k_theta_for_K_2G() -> float:
    """Find k_θ/k_a such that K_relaxed = 2 G_relaxed."""
    def f(kt):
        bond = KeatingBond(k_a=1.0, k_theta=kt, d=1.0)
        K, G = extract_K_G(bond)
        return K - 2.0 * G

    # Bracket: Session 15 sweep shows K/G = 2.67 at k_θ=0.1, K/G = 1.56 at k_θ=0.2
    # So K=2G crosses between 0.1 and 0.2
    return brentq(f, 0.05, 0.5, xtol=1e-10)


# ============================================================
# Path B Step 2: build full 9-DOF Hessian
# ============================================================
#
# DOF ordering (9 total):
#   x[0] = ε_xx (diagonal strain)
#   x[1] = ε_yy
#   x[2] = ε_zz
#   x[3] = ε_xy (off-diagonal, symmetric)
#   x[4] = ε_yz
#   x[5] = ε_xz
#   x[6] = u_int_x (internal optic-mode displacement)
#   x[7] = u_int_y
#   x[8] = u_int_z
#
# This is the natural "macro strain + internal sublattice relaxation" DOF set
# for a Born-Huang K4 unit cell with Cosserat couple-stress.

def x_to_strain_uint(x: np.ndarray):
    eps = np.array([
        [x[0], x[3], x[5]],
        [x[3], x[1], x[4]],
        [x[5], x[4], x[2]],
    ])
    u_int = x[6:9].copy()
    return eps, u_int


def energy_x(x: np.ndarray, bond: KeatingBond) -> float:
    eps, u_int = x_to_strain_uint(x)
    return unit_cell_energy(eps, u_int, bond)


def build_hessian_9x9(bond: KeatingBond, h: float = 1e-5) -> np.ndarray:
    """Numerical Hessian at x=0 via 5-point stencil on the diagonal,
    cross-derivatives via four-point mixed second difference."""
    n = 9
    H = np.zeros((n, n))
    x0 = np.zeros(n)
    f0 = energy_x(x0, bond)

    # Diagonal: second derivatives
    for i in range(n):
        xp = x0.copy(); xp[i] += h
        xm = x0.copy(); xm[i] -= h
        H[i, i] = (energy_x(xp, bond) - 2 * f0 + energy_x(xm, bond)) / h**2

    # Off-diagonal: mixed second derivatives
    for i in range(n):
        for j in range(i + 1, n):
            xpp = x0.copy(); xpp[i] += h; xpp[j] += h
            xpm = x0.copy(); xpm[i] += h; xpm[j] -= h
            xmp = x0.copy(); xmp[i] -= h; xmp[j] += h
            xmm = x0.copy(); xmm[i] -= h; xmm[j] -= h
            H[i, j] = (energy_x(xpp, bond) - energy_x(xpm, bond)
                       - energy_x(xmp, bond) + energy_x(xmm, bond)) / (4 * h**2)
            H[j, i] = H[i, j]
    return H


# ============================================================
# Path B Step 3: eigendecomposition + channel projections
# ============================================================

def project_eigenvector(v: np.ndarray):
    """Decompose a 9-vector into K-channel (hydrostatic), G-channel
    (deviatoric), and internal-channel amplitudes.

    Returns dict with magnitudes, signed components, fraction-of-norm.
    """
    # Strain part (first 6 components)
    eps_xx, eps_yy, eps_zz = v[0], v[1], v[2]
    eps_xy, eps_yz, eps_xz = v[3], v[4], v[5]
    u_int = v[6:9]

    # Hydrostatic (K-channel): trace = ε_xx + ε_yy + ε_zz, normalized by √3
    trace = (eps_xx + eps_yy + eps_zz) / np.sqrt(3.0)

    # Deviatoric (G-channel): 5 components after removing trace.
    # Use standard orthonormal basis for traceless symmetric 3x3 tensors:
    #   D1 = (ε_xx - ε_yy) / √2
    #   D2 = (ε_xx + ε_yy - 2ε_zz) / √6
    #   D3 = √2 ε_xy
    #   D4 = √2 ε_yz
    #   D5 = √2 ε_xz
    D1 = (eps_xx - eps_yy) / np.sqrt(2.0)
    D2 = (eps_xx + eps_yy - 2 * eps_zz) / np.sqrt(6.0)
    D3 = np.sqrt(2.0) * eps_xy
    D4 = np.sqrt(2.0) * eps_yz
    D5 = np.sqrt(2.0) * eps_xz

    K_amp = abs(trace)
    G_amp = np.sqrt(D1**2 + D2**2 + D3**2 + D4**2 + D5**2)
    int_amp = float(np.linalg.norm(u_int))

    total = np.sqrt(K_amp**2 + G_amp**2 + int_amp**2)
    return {
        "K_amp": K_amp,
        "G_amp": G_amp,
        "int_amp": int_amp,
        "K_frac": K_amp / total if total > 0 else 0.0,
        "G_frac": G_amp / total if total > 0 else 0.0,
        "int_frac": int_amp / total if total > 0 else 0.0,
        "trace": trace,
        "dev": [D1, D2, D3, D4, D5],
        "u_int": u_int.tolist(),
    }


def candidate_quantities(eigvals, eigvecs):
    """Extract all candidate 0.187-matching quantities from the spectrum."""
    cands = {}
    n_modes = len(eigvals)

    # Group eigenvalues into degenerate clusters
    # (For K4 cubic symmetry, expect 1+5 macro strain + 3 internal modes)
    clusters = []
    if n_modes > 0:
        cluster_tol = 1e-3 * max(abs(eigvals.max()), 1.0)
        current = [0]
        for i in range(1, n_modes):
            if abs(eigvals[i] - eigvals[current[-1]]) < cluster_tol:
                current.append(i)
            else:
                clusters.append(current)
                current = [i]
        clusters.append(current)

    cands["clusters"] = [
        {"indices": c, "eigenvalue": float(eigvals[c[0]]), "degeneracy": len(c)}
        for c in clusters
    ]

    # Per-mode projections
    projections = []
    for i in range(n_modes):
        proj = project_eigenvector(eigvecs[:, i])
        projections.append({
            "index": i,
            "eigenvalue": float(eigvals[i]),
            "freq_ratio_sqrt": float(np.sqrt(max(eigvals[i], 0)) / np.sqrt(max(eigvals[0], 1e-12))) if eigvals[0] > 1e-12 else None,
            **{k: (v if not isinstance(v, (list, np.ndarray)) else
                   (v if isinstance(v, list) else v.tolist()))
               for k, v in proj.items()},
        })

    cands["modes"] = projections

    # Compute amplitude ratios for each mode
    ratios = []
    for i in range(n_modes):
        proj = projections[i]
        r = {"mode": i, "eigenvalue": proj["eigenvalue"]}
        if proj["K_amp"] > 1e-8 and proj["G_amp"] > 1e-8:
            r["G_over_K"] = proj["G_amp"] / proj["K_amp"]
            r["K_over_G"] = proj["K_amp"] / proj["G_amp"]
        if proj["int_amp"] > 1e-8:
            if proj["K_amp"] > 1e-8:
                r["int_over_K"] = proj["int_amp"] / proj["K_amp"]
            if proj["G_amp"] > 1e-8:
                r["int_over_G"] = proj["int_amp"] / proj["G_amp"]
            total = proj["K_amp"] + proj["G_amp"] + proj["int_amp"]
            r["int_frac"] = proj["int_amp"] / total
        ratios.append(r)
    cands["ratios"] = ratios

    return cands


# ============================================================
# Path B Step 4: comparison report
# ============================================================

def compare_to_targets(value: float, name: str = "") -> str:
    """Return summary string of nearest-targets for a value."""
    matches = []
    for tname, tval in TARGETS.items():
        if abs(tval) < 1e-12:
            continue
        rel = abs(value - tval) / abs(tval)
        if rel < 0.10:  # within 10%
            matches.append((tname, tval, rel))
    if not matches:
        return f"{value:.4f} — no target match within 10%"
    matches.sort(key=lambda m: m[2])
    s = f"{value:.4f}"
    for tname, tval, rel in matches[:3]:
        s += f" | {tname}={tval:.4f} ({rel*100:.1f}% off)"
    return s


def main():
    print("=" * 80)
    print("Q-G47 Path B (doc 127): K=2G operating point eigenmode extraction")
    print("=" * 80)
    print()
    print(f"α = 1/{ALPHA_INV:.4f}")
    print(f"p* = 8πα = {8 * np.pi * ALPHA:.6f}  (fabric weave density target)")
    print(f"A-029 u_0* = 0.187  (magic angle target)")
    print()

    # ─── Step 1: locate K=2G operating point ──────────────────────
    print("─" * 80)
    print("Step 1: Locate k_θ/k_a* such that K_relaxed = 2 G_relaxed")
    print("─" * 80)

    kt_star = find_k_theta_for_K_2G()
    bond_star = KeatingBond(k_a=1.0, k_theta=kt_star, d=1.0)
    K_star, G_star = extract_K_G(bond_star)

    print(f"  k_θ/k_a*       = {kt_star:.6f}")
    print(f"  K_relaxed*     = {K_star:.6f}")
    print(f"  G_relaxed*     = {G_star:.6f}")
    print(f"  K/G            = {K_star/G_star:.6f}  (target 2.0)")
    print(f"  ν (Poisson)    = {(3*K_star - 2*G_star) / (2*(3*K_star + G_star)):.6f}  (target 2/7 = {2/7:.6f})")
    print()
    print(f"  Cf. Session 17: ℓ_c/d = √(ξ_K2/(2ξ_K1)) = √6 ≈ {np.sqrt(6):.4f}")
    print(f"      so χ_K = (ℓ_c/d)² = 6 in continuous picture")
    print(f"      vs discrete k_θ/(k_a·d²) = {kt_star:.4f}")
    print(f"      → MISMATCH by factor ~{6/kt_star:.1f}: discrete-continuous prefactor convention?")
    print()

    # ─── Step 2: build Hessian, solve eigenvalue problem ────────────
    print("─" * 80)
    print("Step 2: Build 9×9 Hessian + solve eigh(H, I)")
    print("─" * 80)

    H = build_hessian_9x9(bond_star)
    print(f"  Hessian symmetric error: {np.abs(H - H.T).max():.2e}")
    print(f"  Hessian shape: {H.shape}")
    print(f"  Hessian condition number: {np.linalg.cond(H + 1e-12*np.eye(9)):.2e}")

    # Symmetrize numerically
    H = 0.5 * (H + H.T)
    M = np.eye(9)
    eigvals, eigvecs = eigh(H, M)

    print(f"\n  Eigenvalues:")
    for i, ev in enumerate(eigvals):
        print(f"    λ_{i} = {ev:+.6f}")
    print()

    # ─── Step 3: project eigenvectors ────────────────────────────
    print("─" * 80)
    print("Step 3: Project each eigenvector onto (K, G, internal) channels")
    print("─" * 80)
    print()
    print(f"  {'i':>3} {'λ':>11} {'K_amp':>9} {'G_amp':>9} {'int_amp':>9} {'K_frac':>8} {'G_frac':>8} {'int_frac':>8}")
    print("  " + "-" * 70)
    for i in range(9):
        proj = project_eigenvector(eigvecs[:, i])
        print(f"  {i:>3d} {eigvals[i]:>+11.5f} {proj['K_amp']:>9.4f} {proj['G_amp']:>9.4f} {proj['int_amp']:>9.4f} {proj['K_frac']:>8.4f} {proj['G_frac']:>8.4f} {proj['int_frac']:>8.4f}")
    print()

    # ─── Step 4: candidate quantity extraction ─────────────────────
    print("─" * 80)
    print("Step 4: Candidate quantities + comparison to 0.187 target")
    print("─" * 80)
    print()

    cands = candidate_quantities(eigvals, eigvecs)
    print(f"  Eigenvalue clusters (degenerate sets):")
    for c in cands["clusters"]:
        print(f"    λ = {c['eigenvalue']:+.6f}, degeneracy = {c['degeneracy']}, indices = {c['indices']}")
    print()

    print(f"  Per-mode amplitude ratios:")
    for r in cands["ratios"]:
        if "G_over_K" in r or "int_frac" in r:
            print(f"\n    Mode {r['mode']} (λ = {r['eigenvalue']:+.4f}):")
            for k, v in r.items():
                if k in ("mode", "eigenvalue"):
                    continue
                if isinstance(v, float):
                    cmp = compare_to_targets(v, k)
                    print(f"      {k:<14} = {cmp}")

    # ─── Step 5: frequency ratio analysis ─────────────────────────
    print()
    print("─" * 80)
    print("Step 5: Frequency-ratio analysis (sqrt of eigenvalue ratios)")
    print("─" * 80)
    pos_eigs = [ev for ev in eigvals if ev > 1e-10]
    if len(pos_eigs) >= 2:
        ratios = []
        for i in range(len(pos_eigs)):
            for j in range(i + 1, len(pos_eigs)):
                r_freq = np.sqrt(pos_eigs[j] / pos_eigs[i])
                ratios.append((i, j, r_freq))
        print(f"  ω_j/ω_i pairs:")
        for i, j, r in ratios[:10]:
            cmp = compare_to_targets(r, f"omega_{j}/omega_{i}")
            print(f"    ω_{j}/ω_{i} = {cmp}")
        # Also report 1/r for the small-value cases
        print(f"\n  ω_i/ω_j (inverse) pairs:")
        for i, j, r in ratios[:10]:
            if r > 1:
                cmp = compare_to_targets(1.0/r, f"omega_{i}/omega_{j}")
                print(f"    ω_{i}/ω_{j} = {cmp}")

    # ─── Step 6: dump JSON ────────────────────────────────────────
    print()
    print("─" * 80)
    print("Step 6: Cache JSON for doc 127 inclusion")
    print("─" * 80)

    cache = {
        "operating_point": {
            "k_theta_over_k_a": kt_star,
            "K_relaxed": K_star,
            "G_relaxed": G_star,
            "K_over_G": K_star / G_star,
            "poisson": (3*K_star - 2*G_star) / (2*(3*K_star + G_star)),
        },
        "targets": TARGETS,
        "eigenvalues": eigvals.tolist(),
        "eigenvectors": eigvecs.tolist(),
        "projections": [project_eigenvector(eigvecs[:, i]) for i in range(9)],
        "clusters": cands["clusters"],
    }

    # Convert numpy types for JSON serialization
    def to_native(o):
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, (np.floating, np.integer)):
            return o.item()
        if isinstance(o, dict):
            return {k: to_native(v) for k, v in o.items()}
        if isinstance(o, list):
            return [to_native(x) for x in o]
        return o

    cache_native = to_native(cache)
    out_path = os.path.join(
        os.path.dirname(__file__),
        "q_g47_path_b_k4_eigenmode_results.json"
    )
    with open(out_path, "w") as f:
        json.dump(cache_native, f, indent=2)
    print(f"  Wrote: {out_path}")
    print()
    print("=" * 80)
    print("DONE — see doc 127 for verdict + ambiguities")
    print("=" * 80)


if __name__ == "__main__":
    main()
