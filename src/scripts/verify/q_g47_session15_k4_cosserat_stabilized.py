"""
Q-G47 Session 15: Stabilized K4 Cosserat lattice with sublattice relaxation.

Companion to AVE-QED/docs/analysis/2026-05-15_Q-G47_session15_stabilized_scaffold.md.

Purpose:
    Add Cosserat couple-stress (bond-bending) contributions to the Session 14
    sublattice-relaxation scaffold. Verify that the couple-stress terms
    stabilize G > 0 under relaxation (resolving Session 14's classical
    central-force K4 instability).

Approach:
    Each K4 bond has:
      - Central-force axial stiffness: k_a (force per unit Δu along bond)
      - Bond-bending angular stiffness: k_θ (force per unit angle deviation
        from the equilibrium bond direction)

    The bending term couples to TRANSVERSE relative displacement:
      U_bend = (1/2) k_θ · (Δu_transverse / d)²
            = (1/2) (k_θ/d²) · |Δu - n̂(n̂·Δu)|²

    This is mathematically equivalent to adding a "shear stiffness" k_s = k_θ/d²
    to the central-force model. Hence the Session 12 isotropic Cosserat-rod
    bond (which had k_a = k_s = 1) implicitly included bond-bending.

    Session 15 distinguishes them explicitly and verifies stability.

Run:
    python src/scripts/verify/q_g47_session15_k4_cosserat_stabilized.py
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass

K4_BOND_DIRECTIONS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3.0)


@dataclass
class KeatingBond:
    """
    Keating-style K4 bond with central-force + bond-bending stiffnesses.

    U_bond(n̂, Δu) = (1/2) k_a (n̂·Δu)²            [central force]
                  + (1/2) (k_θ/d²) |Δu - n̂(n̂·Δu)|²  [bond bending]

    The k_θ/d² combination has units of [N/m], same as k_a, so dimensionally
    consistent. Treat k_θ as a free parameter; k_a as the canonical bond
    stretching stiffness.
    """
    k_a: float = 1.0      # axial Hookean [N/m]
    k_theta: float = 1.0  # bond-bending [N·m/rad²], divided by d² in energy
    d: float = 1.0        # bond length [m]

    def energy(self, n_hat: np.ndarray, delta_u: np.ndarray) -> float:
        n = n_hat / np.linalg.norm(n_hat)
        axial = np.dot(n, delta_u)
        transverse = delta_u - axial * n
        k_s = self.k_theta / self.d**2
        return 0.5 * self.k_a * axial**2 + 0.5 * k_s * np.dot(transverse, transverse)


def unit_cell_energy_keating(
    strain_3x3: np.ndarray,
    u_int: np.ndarray,
    bond: KeatingBond,
) -> float:
    """Total elastic energy for K4 unit cell under macro-strain + internal u."""
    U_total = 0.0
    for n_hat in K4_BOND_DIRECTIONS:
        delta_u_affine = bond.d * (strain_3x3 @ n_hat)
        delta_u = delta_u_affine + u_int
        U_total += bond.energy(n_hat, delta_u)
    return U_total


def relaxed_energy_keating(strain_3x3: np.ndarray, bond: KeatingBond):
    from scipy.optimize import minimize
    res = minimize(
        lambda u: unit_cell_energy_keating(strain_3x3, u, bond),
        x0=np.zeros(3),
        method='BFGS',
        tol=1e-14,
    )
    return res.fun, res.x


def extract_KG_relaxed(bond: KeatingBond, eps: float = 0.01):
    """Return (K_rigid, K_relaxed, G_rigid, G_relaxed)."""
    # Bulk: isotropic strain
    strain_vol = (eps / 3.0) * np.eye(3)
    U_K_rigid = unit_cell_energy_keating(strain_vol, np.zeros(3), bond)
    U_K_relaxed, _ = relaxed_energy_keating(strain_vol, bond)
    K_rigid = 2 * U_K_rigid / eps**2
    K_relaxed = 2 * U_K_relaxed / eps**2

    # Shear: ε_xy = ε/2
    strain_sh = np.zeros((3, 3))
    strain_sh[0, 1] = eps / 2
    strain_sh[1, 0] = eps / 2
    U_G_rigid = unit_cell_energy_keating(strain_sh, np.zeros(3), bond)
    U_G_relaxed, _ = relaxed_energy_keating(strain_sh, bond)
    G_rigid = 2 * U_G_rigid / eps**2
    G_relaxed = 2 * U_G_relaxed / eps**2

    return K_rigid, K_relaxed, G_rigid, G_relaxed


def main():
    print("=" * 75)
    print("Q-G47 Session 15: K4 with Keating bond-bending + sublattice relaxation")
    print("=" * 75)
    print()
    print("Question 1: does k_θ > 0 stabilize G > 0 under sublattice relaxation?")
    print()
    print(f"{'k_a':>6} {'k_θ':>6} {'K_rigid':>10} {'K_relaxed':>11} {'G_rigid':>10} {'G_relaxed':>11} {'K/G relaxed':>13}")
    print("-" * 75)

    test_bonds = [
        (1.0, 0.0),    # central-force only (Session 14 baseline)
        (1.0, 0.1),    # tiny bending
        (1.0, 0.5),    # half-strength bending
        (1.0, 1.0),    # canonical isotropic (matches Session 12 k_a=k_s=1)
        (1.0, 2.0),    # strong bending
        (1.0, 5.0),    # very strong bending
        (1.0, 10.0),   # bending-dominated
    ]

    K_relaxed_list, G_relaxed_list = [], []
    for k_a, k_theta in test_bonds:
        bond = KeatingBond(k_a=k_a, k_theta=k_theta, d=1.0)
        K_r, K_rel, G_r, G_rel = extract_KG_relaxed(bond)
        ratio_str = f"{K_rel/G_rel:.4f}" if G_rel > 1e-10 else "∞"
        print(f"{k_a:>6.2f} {k_theta:>6.2f} {K_r:>10.4f} {K_rel:>11.4f} {G_r:>10.4f} {G_rel:>11.4f} {ratio_str:>13}")
        K_relaxed_list.append(K_rel)
        G_relaxed_list.append(G_rel)

    print()
    print("Question 2: what k_θ/k_a ratio gives Cauchy K/G = 5/3?")

    # Sweep k_theta/k_a to find K/G = 5/3
    target = 5/3
    print(f"{'k_θ/k_a':>10} {'K/G relaxed':>15}")
    print("-" * 30)
    for k_theta in np.linspace(0.0, 3.0, 16):
        bond = KeatingBond(k_a=1.0, k_theta=k_theta, d=1.0)
        _, K_rel, _, G_rel = extract_KG_relaxed(bond)
        ratio = K_rel/G_rel if G_rel > 1e-10 else float('inf')
        marker = " ← Cauchy 5/3" if abs(ratio - 5/3) < 0.05 else ""
        print(f"{k_theta:>10.4f} {ratio:>15.4f}{marker}")

    print()
    print("=" * 75)
    print("Question 3: does a baseline K_0 = 12 emerge here too?")
    # Check at k_θ/k_a = 1 (canonical isotropic limit)
    bond = KeatingBond(k_a=1.0, k_theta=1.0, d=1.0)
    K_r, K_rel, G_r, G_rel = extract_KG_relaxed(bond)
    print(f"Canonical (k_a=k_θ=1): K_rigid = {K_r:.4f}, G_rigid = {G_r:.4f}")
    print(f"Cf. Session 12 K_0 = 12: Session 12 used different normalization")
    print(f"   (Session 12: K_0 = 4 k_a + 8 k_s with k_a=k_s=1 → 12.")
    print(f"    Here: scaled differently due to strain-based extraction.)")
    print("=" * 75)


if __name__ == "__main__":
    main()
