"""
Q-G47 Path B+ (doc 128): Full Cosserat 12-DOF K4 eigenmode extraction.

Purpose:
    Extend Path B (Cauchy 9 DOFs) to full Axiom-1 compliance:
    - 12 DOFs per unit cell: 6 macro-strain + 3 internal translation +
      3 internal MICROROTATION (the Cosserat DOFs per Axiom 1)
    - Bond energy: Keating translation + Cosserat couple-stress + chiral
      coupling (right-handed I4₁32)

Physical picture (per Grant's "stored reactance" reframe):
    Each DOF = one capacitive (translational) or inductive (microrotational)
    energy storage channel at each node. An eigenmode is one normal mode of
    the 12-DOF coupled-oscillator network. The eigenvalue is the effective
    spring constant (ω²) for that mode. Chirality couples C-channels to
    L-channels.

Group-theory prediction to test:
    For K4 cubic (proper tetrahedral group T = |T|=12), strain DOFs decompose
    as S²(R³) = A₁ ⊕ E ⊕ T₂, and vector DOFs (translation + rotation) as
    T₁ ⊕ T₁. The E-irrep strain (D1, D2 directions) might NOT couple to T₁
    microrotation even with chirality, because no direct E×T₁ → trivial
    irrep exists. If so: the 4/21 ≈ 0.187 result for the soft shear E mode
    SURVIVES the Cosserat upgrade — λ_G = (4/3)k_s independent of microrot.

If the prediction holds: Path B's 4/21 IS the Cosserat result, and the
2-4% gap to u_0* = 0.187 / p* = 0.1834 is intrinsic (either real or
needs further interpretation).

If the prediction fails: the E-mode mixes with microrotation via some
indirect coupling, and λ_G renormalizes from 4/21 toward (hopefully) 0.187
or 0.1834.

Run:
    python src/scripts/verify/q_g47_path_b_plus_cosserat.py
"""
from __future__ import annotations

import json
import os
import numpy as np
from dataclasses import dataclass
from scipy.linalg import eigh
from scipy.optimize import brentq

ALPHA_INV = 137.035999084
ALPHA = 1.0 / ALPHA_INV

TARGETS = {
    "u_0_star_A029": 0.187,
    "p_star_8pi_alpha": 8 * np.pi * ALPHA,
    "Path_B_4_over_21": 4 / 21,
    "sqrt_1_over_28": np.sqrt(1 / 28),
    "sqrt_1_over_42": np.sqrt(1 / 42),
}

K4_BOND_DIRECTIONS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3.0)


@dataclass
class CosseratBond:
    """Full Cosserat-Keating K4 bond with translation + microrotation + chirality.

    Energy form (per bond, with d=1):
        U = (1/2) k_a · (n̂·Δu)²           [Cauchy axial — translation]
          + (1/2) k_s · |Δu - n̂(n̂·Δu)|²    [Keating transverse — translation]
          + (1/2) k_β · (n̂·Δφ)²            [Cosserat axial couple-stress]
          + (1/2) k_γ · |Δφ - n̂(n̂·Δφ)|²   [Cosserat transverse couple-stress]
          + k_χ · n̂·(Δu × Δφ)             [Chiral coupling, parity-odd]

    The chiral term n̂·(Δu × Δφ) is the simplest right-handed mixing:
    pushing translationally along Δu generates a torque ∝ Δφ × n̂.
    Sign convention: positive k_χ = right-handed coupling (matches I4₁32).
    """
    k_a: float = 1.0       # translational axial [Cauchy]
    k_s: float = 1.0 / 7   # translational transverse [Keating bond-bending]
    k_beta: float = 1.0    # microrotational axial [Cosserat α-equivalent]
    k_gamma: float = 1.0 / 7  # microrotational transverse [Cosserat (β+γ)/d²]
    k_chi: float = 0.0     # chiral coupling [right-handed I4₁32, varies]
    d: float = 1.0

    def energy(self, n_hat, du, dphi):
        n = n_hat / np.linalg.norm(n_hat)
        # Translation
        ax_t = float(np.dot(n, du))
        trans_t = du - ax_t * n
        # Rotation
        ax_r = float(np.dot(n, dphi))
        trans_r = dphi - ax_r * n
        # Chiral coupling (parity-odd, sums non-trivially over K4):
        #   (n·du)(n·dφ) is pseudoscalar (n·du polar-even, n·dφ pseudoscalar-odd)
        # AND transverse term: (du - n(n·du)) · (dφ - n(n·dφ))
        #   captures translation-rotation cross-coupling in the bond's
        #   transverse plane (Cosserat "α" mixing).
        chi_axial = ax_t * ax_r
        chi_trans = float(np.dot(trans_t, trans_r))
        return (
            0.5 * self.k_a * ax_t**2
            + 0.5 * self.k_s * float(np.dot(trans_t, trans_t))
            + 0.5 * self.k_beta * ax_r**2
            + 0.5 * self.k_gamma * float(np.dot(trans_r, trans_r))
            + self.k_chi * (chi_axial + chi_trans)
        )


# ============================================================
# 12-DOF assembly
# ============================================================
# DOF ordering (12 total):
#   x[0:3]   = ε_xx, ε_yy, ε_zz       (diagonal strain)
#   x[3:6]   = ε_xy, ε_yz, ε_xz       (off-diagonal strain)
#   x[6:9]   = u_int_x, u_int_y, u_int_z   (internal translation)
#   x[9:12]  = φ_int_x, φ_int_y, φ_int_z   (internal MICROROTATION)
#
# For macro microrotation gradient: we use the strain-like assumption that
# uniform macro microrotation is just a global rigid rotation and doesn't
# enter the unit-cell energy. So only INTERNAL microrotation (sublattice
# microrotation, A vs B antisymmetric) enters.


def x_to_strain_uint(x: np.ndarray):
    eps = np.array([
        [x[0], x[3], x[5]],
        [x[3], x[1], x[4]],
        [x[5], x[4], x[2]],
    ])
    u_int = x[6:9].copy()
    phi_int = x[9:12].copy()
    return eps, u_int, phi_int


def unit_cell_energy(strain, u_int, phi_int, bond: CosseratBond):
    U = 0.0
    for n_hat in K4_BOND_DIRECTIONS:
        # The displacement and microrotation differences between A and B
        # sublattices for this bond:
        du = bond.d * (strain @ n_hat) + u_int
        dphi = phi_int.copy()  # macro rotation gradient absent; only internal
        U += bond.energy(n_hat, du, dphi)
    return U


def energy_x(x: np.ndarray, bond: CosseratBond) -> float:
    eps, u_int, phi_int = x_to_strain_uint(x)
    return unit_cell_energy(eps, u_int, phi_int, bond)


def build_hessian_12x12(bond: CosseratBond, h: float = 1e-5) -> np.ndarray:
    n = 12
    H = np.zeros((n, n))
    x0 = np.zeros(n)
    f0 = energy_x(x0, bond)
    for i in range(n):
        xp = x0.copy(); xp[i] += h
        xm = x0.copy(); xm[i] -= h
        H[i, i] = (energy_x(xp, bond) - 2 * f0 + energy_x(xm, bond)) / h**2
    for i in range(n):
        for j in range(i + 1, n):
            xpp = x0.copy(); xpp[i] += h; xpp[j] += h
            xpm = x0.copy(); xpm[i] += h; xpm[j] -= h
            xmp = x0.copy(); xmp[i] -= h; xmp[j] += h
            xmm = x0.copy(); xmm[i] -= h; xmm[j] -= h
            H[i, j] = (energy_x(xpp, bond) - energy_x(xpm, bond)
                       - energy_x(xmp, bond) + energy_x(xmm, bond)) / (4 * h**2)
            H[j, i] = H[i, j]
    return 0.5 * (H + H.T)


def project_eigenvector_12(v: np.ndarray):
    eps_xx, eps_yy, eps_zz = v[0], v[1], v[2]
    eps_xy, eps_yz, eps_xz = v[3], v[4], v[5]
    u_int = v[6:9]
    phi_int = v[9:12]

    trace = (eps_xx + eps_yy + eps_zz) / np.sqrt(3.0)
    D1 = (eps_xx - eps_yy) / np.sqrt(2.0)
    D2 = (eps_xx + eps_yy - 2 * eps_zz) / np.sqrt(6.0)
    D3 = np.sqrt(2.0) * eps_xy
    D4 = np.sqrt(2.0) * eps_yz
    D5 = np.sqrt(2.0) * eps_xz

    K_amp = abs(trace)
    G_E_amp = np.sqrt(D1**2 + D2**2)      # E-irrep deviatoric
    G_T2_amp = np.sqrt(D3**2 + D4**2 + D5**2)  # T₂-irrep deviatoric
    u_amp = float(np.linalg.norm(u_int))
    phi_amp = float(np.linalg.norm(phi_int))

    total = np.sqrt(K_amp**2 + G_E_amp**2 + G_T2_amp**2 + u_amp**2 + phi_amp**2)
    return {
        "K_amp": K_amp,
        "G_E_amp": G_E_amp,
        "G_T2_amp": G_T2_amp,
        "u_int_amp": u_amp,
        "phi_int_amp": phi_amp,
        "K_frac": K_amp / total if total > 0 else 0,
        "G_E_frac": G_E_amp / total if total > 0 else 0,
        "G_T2_frac": G_T2_amp / total if total > 0 else 0,
        "u_frac": u_amp / total if total > 0 else 0,
        "phi_frac": phi_amp / total if total > 0 else 0,
    }


def compare_to_targets(value: float) -> str:
    matches = []
    for tname, tval in TARGETS.items():
        if abs(tval) < 1e-12:
            continue
        rel = abs(value - tval) / abs(tval)
        if rel < 0.10:
            matches.append((tname, tval, rel))
    if not matches:
        return f"{value:.4f} — no target match within 10%"
    matches.sort(key=lambda m: m[2])
    s = f"{value:.4f}"
    for tname, tval, rel in matches[:2]:
        s += f" | {tname}={tval:.4f} ({rel*100:.1f}% off)"
    return s


def run_chirality_sweep():
    """Sweep k_χ from 0 (Cauchy limit) to large values and track λ_G."""
    print("\n" + "=" * 80)
    print("Chirality sweep — does k_χ shift the soft-shear eigenvalue?")
    print("=" * 80)
    print(f"  Holding k_a=1, k_s=1/7 (K=2G operating point), k_β=k_γ=1/7")
    print()
    print(f"{'k_χ':>10} {'λ_min (soft)':>15} {'cluster sizes':>20} {'Cauchy 4/21':>12}")
    print("-" * 70)

    for k_chi in [0.0, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
        bond = CosseratBond(k_a=1.0, k_s=1/7, k_beta=1/7, k_gamma=1/7, k_chi=k_chi)
        H = build_hessian_12x12(bond)
        eigvals, _ = eigh(H, np.eye(12))
        # cluster
        clusters = []
        cur = [0]
        for i in range(1, 12):
            if abs(eigvals[i] - eigvals[cur[-1]]) < 1e-4:
                cur.append(i)
            else:
                clusters.append(len(cur)); cur = [i]
        clusters.append(len(cur))
        soft = eigvals[0] if eigvals[0] > 1e-8 else (eigvals[3] if len(eigvals) > 3 else 0)
        print(f"  {k_chi:>10.4f} {soft:>15.6f} {str(clusters):>20s} {4/21:>12.6f}")


def main():
    print("=" * 80)
    print("Q-G47 Path B+ (doc 128): Cosserat 12-DOF K4 eigenmode")
    print("=" * 80)
    print()
    print(f"α = 1/{ALPHA_INV:.4f}")
    print(f"p* = 8πα = {8 * np.pi * ALPHA:.6f}")
    print(f"Path B Cauchy result: λ_G = 4/21 = {4/21:.6f}")
    print()

    # ─── Test 1: zero chirality, equal trans/rot stiffness ────────────
    print("─" * 80)
    print("Test 1: Non-chiral limit (k_χ=0) — does the soft shear stay at 4/21?")
    print("─" * 80)
    print("  Bond: k_a=1, k_s=1/7, k_β=1, k_γ=1/7, k_χ=0")
    bond_0 = CosseratBond(k_a=1.0, k_s=1/7, k_beta=1.0, k_gamma=1/7, k_chi=0.0)
    H = build_hessian_12x12(bond_0)
    print(f"  Hessian symmetric: {np.abs(H - H.T).max():.2e}")
    eigvals, eigvecs = eigh(H, np.eye(12))
    print(f"\n  Eigenvalues (12 total):")
    for i, ev in enumerate(eigvals):
        print(f"    λ_{i:2d} = {ev:+.6f}")

    print(f"\n  Projections (K, G_E, G_T2, u_int, φ_int):")
    print(f"  {'i':>3} {'λ':>10} {'K':>6} {'G_E':>6} {'G_T2':>6} {'u_int':>6} {'φ_int':>6}")
    for i in range(12):
        proj = project_eigenvector_12(eigvecs[:, i])
        print(f"  {i:>3d} {eigvals[i]:>+10.5f}"
              f" {proj['K_frac']:>6.3f} {proj['G_E_frac']:>6.3f}"
              f" {proj['G_T2_frac']:>6.3f} {proj['u_frac']:>6.3f}"
              f" {proj['phi_frac']:>6.3f}")

    print(f"\n  KEY: does E-irrep soft shear (λ = 4/21) survive?")
    for i in range(12):
        proj = project_eigenvector_12(eigvecs[:, i])
        if proj['G_E_frac'] > 0.9:  # E-dominated mode
            print(f"    Mode {i}: λ = {eigvals[i]:.6f} | E_frac = {proj['G_E_frac']:.3f}"
                  f" | φ_frac = {proj['phi_frac']:.3f} | cf 4/21 = {4/21:.6f}")

    # ─── Test 2: with chirality ────────────────────────────────────
    print()
    print("─" * 80)
    print("Test 2: With chirality (k_χ=0.1) — does mixing change E-mode?")
    print("─" * 80)
    bond_chi = CosseratBond(k_a=1.0, k_s=1/7, k_beta=1.0, k_gamma=1/7, k_chi=0.1)
    H = build_hessian_12x12(bond_chi)
    eigvals_chi, eigvecs_chi = eigh(H, np.eye(12))

    print(f"\n  Eigenvalues with k_χ=0.1:")
    for i, ev in enumerate(eigvals_chi):
        print(f"    λ_{i:2d} = {ev:+.6f}")

    print(f"\n  KEY: E-mode shifted by chirality?")
    for i in range(12):
        proj = project_eigenvector_12(eigvecs_chi[:, i])
        if proj['G_E_frac'] > 0.3:  # any E content
            print(f"    Mode {i}: λ = {eigvals_chi[i]:.6f} | E_frac = {proj['G_E_frac']:.3f}"
                  f" | φ_frac = {proj['phi_frac']:.3f}")

    # ─── Test 3: full chirality sweep ────────────────────────────
    run_chirality_sweep()

    # ─── Test 4: dump JSON ────────────────────────────────────────
    cache = {
        "k_chi_0": {
            "eigenvalues": eigvals.tolist(),
            "projections": [project_eigenvector_12(eigvecs[:, i]) for i in range(12)],
        },
        "k_chi_p1": {
            "eigenvalues": eigvals_chi.tolist(),
            "projections": [project_eigenvector_12(eigvecs_chi[:, i]) for i in range(12)],
        },
        "targets": TARGETS,
        "path_B_result_4_21": 4 / 21,
    }

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

    out_path = os.path.join(
        os.path.dirname(__file__),
        "q_g47_path_b_plus_cosserat_results.json"
    )
    with open(out_path, "w") as f:
        json.dump(to_native(cache), f, indent=2)
    print(f"\n  Wrote: {out_path}")
    print()
    print("=" * 80)
    print("DONE — see doc 128 for interpretation")
    print("=" * 80)


if __name__ == "__main__":
    main()
