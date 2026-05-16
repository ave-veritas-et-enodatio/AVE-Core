"""
Q-G47 Session 14: K4 Cosserat lattice with Born–Huang sublattice relaxation.

Companion to AVE-QED/docs/analysis/2026-05-15_Q-G47_session14_sublattice_relaxation.md.

Purpose:
    Extend Session 12 scaffold (q_g47_session12_k4_cosserat_lattice.py) to
    include Born–Huang internal-strain (sublattice-relaxation) mode. This
    is the standard fix that should recover the Cauchy K_0/G_0 = 5/3 baseline
    instead of the rigid-sublattice K_0/G_0 = 3 from Session 12.

Approach:
    For a uniform macroscopic strain ε_macro applied to the K4 unit cell,
    the A and B sublattices relax relative to each other to minimize energy.
    The relaxed modulus is

        M_relaxed = M_rigid - K_coupling^T K_internal^{-1} K_coupling

    where K_coupling is the cross-term between macroscopic strain and
    internal A-B relative displacement.

Run:
    python src/scripts/verify/q_g47_session14_k4_sublattice_relaxation.py
"""

from __future__ import annotations

import numpy as np
from dataclasses import dataclass


# K4 bond directions (canonical tetrahedral)
K4_BOND_DIRECTIONS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=float) / np.sqrt(3.0)


@dataclass
class CentralForceBond:
    """Central-force only K4 bond (Cauchy elasticity baseline).

    k_a only; no shear, no couple. This is the bond model that should
    reproduce the canonical Cauchy K/G = 5/3 ratio for diamond/K4.
    """
    k_a: float = 1.0
    d: float = 1.0

    def stiffness(self, n_hat: np.ndarray, delta_u: np.ndarray) -> float:
        """Elastic energy for central-force bond under Δu = u_B - u_A.

        U_bond = (1/2) k_a (n̂ · Δu)²
        """
        n = n_hat / np.linalg.norm(n_hat)
        axial_extension = np.dot(n, delta_u)
        return 0.5 * self.k_a * axial_extension**2


# ----------------------------------------------------------------------
# UNIT CELL: A at origin, B at (d/2, d/2, d/2) (diamond conventional)
# ----------------------------------------------------------------------
# Under macroscopic strain ε (3×3 symmetric tensor), apply affine
# displacement u(r) = ε · r to all atoms, plus an internal A-B relative
# displacement u_int (3-vector).

def affine_displacement(strain_3x3: np.ndarray, position: np.ndarray) -> np.ndarray:
    """Apply affine deformation u(r) = ε·r."""
    return strain_3x3 @ position


def unit_cell_energy(
    strain_3x3: np.ndarray,
    u_int: np.ndarray,
    bond: CentralForceBond,
) -> float:
    """
    Total elastic energy per unit cell under macroscopic strain ε + internal
    sublattice displacement u_int.

    A-node at origin; B-node at (d/2)·(1,1,1) (one of the K4 sublattice
    positions). Under strain, B is displaced by ε·r_B + u_int relative to
    A's frame (where A's affine displacement is taken as zero by convention).

    Each of B's 4 K4 neighbors is at A's position translated by d·n̂_i, so
    A->B bond vector is d·n̂_i and the relative displacement is
    (B's total displacement) - (A's total displacement at the displaced
    bond endpoint).

    For the 4 bonds emanating from A:
      Δu_bond_i = u_B_total - u_A_total
                = [ε · (d·n̂_i) + u_int] - [0]
                = d·(ε·n̂_i) + u_int
    """
    U_total = 0.0
    for n_hat in K4_BOND_DIRECTIONS:
        delta_u_affine = bond.d * (strain_3x3 @ n_hat)
        delta_u = delta_u_affine + u_int
        U_total += bond.stiffness(n_hat, delta_u)
    return U_total


def relaxed_modulus(strain_3x3: np.ndarray, bond: CentralForceBond) -> float:
    """
    Apply macroscopic strain, minimize energy over internal u_int.

    Returns U_relaxed (per unit cell).
    """
    from scipy.optimize import minimize

    def obj(u_int):
        return unit_cell_energy(strain_3x3, u_int, bond)

    res = minimize(obj, x0=np.zeros(3), method='BFGS', tol=1e-14)
    return res.fun, res.x


# ----------------------------------------------------------------------
# Extract K and G with sublattice relaxation
# ----------------------------------------------------------------------

def extract_K_eff_relaxed(bond: CentralForceBond, eps: float = 0.01) -> float:
    """Bulk modulus via uniform isotropic strain ε_ij = (ε/3)·δ_ij.

    Standard convention: U = (1/2) K (ε_volumetric)² where ε_vol = tr(ε) = ε.
    """
    # Apply uniform isotropic strain (volumetric, ε_volumetric = ε)
    strain = (eps / 3.0) * np.eye(3)
    U_rigid = unit_cell_energy(strain, np.zeros(3), bond)
    U_relaxed, u_int_eq = relaxed_modulus(strain, bond)
    # K = 2U / ε_vol² (volumetric)
    K_rigid = 2.0 * U_rigid / eps**2
    K_relaxed = 2.0 * U_relaxed / eps**2
    return K_rigid, K_relaxed, u_int_eq


def extract_G_eff_relaxed(bond: CentralForceBond, eps: float = 0.01) -> float:
    """Shear modulus via traceless shear strain.

    Apply ε_xy = ε_yx = ε/2 (all others zero). U = (1/2) (2G) (2ε_xy)² = G ε²
    in this convention. Actually: U = G·(2ε_xy)² for engineering shear;
    in tensor form: 2U = 2 G ε_ij ε_ij. For ε_xy = ε/2 only:
        2U = 2G · 2·(ε/2)² = G·ε²
        → U = (1/2) G ε² → G = 2U/ε²
    """
    strain = np.zeros((3, 3))
    strain[0, 1] = eps / 2.0
    strain[1, 0] = eps / 2.0
    U_rigid = unit_cell_energy(strain, np.zeros(3), bond)
    U_relaxed, u_int_eq = relaxed_modulus(strain, bond)
    G_rigid = 2.0 * U_rigid / eps**2
    G_relaxed = 2.0 * U_relaxed / eps**2
    return G_rigid, G_relaxed, u_int_eq


# ----------------------------------------------------------------------
# Main: compute Cauchy K/G with and without sublattice relaxation
# ----------------------------------------------------------------------

def main():
    print("=" * 72)
    print("Q-G47 Session 14: K4 Cauchy elasticity with sublattice relaxation")
    print("=" * 72)
    print()
    print("Central-force only bond model (k_a = 1, no shear, no couple).")
    print("Test: rigid-sublattice K/G vs relaxed K/G.")
    print("Target: relaxed K/G = 5/3 (Session 2 Cauchy baseline for K4/diamond)")
    print()

    bond = CentralForceBond(k_a=1.0, d=1.0)

    K_rigid, K_relaxed, u_K = extract_K_eff_relaxed(bond)
    G_rigid, G_relaxed, u_G = extract_G_eff_relaxed(bond)

    print("Bulk modulus K (isotropic volumetric strain):")
    print(f"  rigid sublattice  : K = {K_rigid:.6f}")
    print(f"  relaxed sublattice: K = {K_relaxed:.6f}")
    print(f"  internal displacement u_int at equilibrium: {u_K}")
    print()

    print("Shear modulus G (ε_xy = ε/2 traceless shear):")
    print(f"  rigid sublattice  : G = {G_rigid:.6f}")
    print(f"  relaxed sublattice: G = {G_relaxed:.6f}")
    print(f"  internal displacement u_int at equilibrium: {u_G}")
    print()

    print("Cauchy ratios:")
    print(f"  rigid   : K/G = {K_rigid/G_rigid:.6f}")
    print(f"  relaxed : K/G = {K_relaxed/G_relaxed:.6f}  (Cauchy target 5/3 ≈ 1.667)")
    print()

    # Poisson's ratio from K/G
    def poisson_from_KG(KG):
        # K/G = (2/3)(1+ν)/(1-2ν) → solve for ν
        # 3(K/G)(1-2ν) = 2(1+ν) → 3KG - 6KGν = 2 + 2ν → ν = (3KG - 2)/(6KG + 2)
        return (3 * KG - 2) / (6 * KG + 2)

    nu_rigid = poisson_from_KG(K_rigid / G_rigid)
    nu_relaxed = poisson_from_KG(K_relaxed / G_relaxed)
    print(f"  Poisson's ratio (rigid)  : ν = {nu_rigid:.4f}")
    print(f"  Poisson's ratio (relaxed): ν = {nu_relaxed:.4f}  (Cauchy target ν = 1/4)")
    print()

    print("=" * 72)
    if abs(K_relaxed / G_relaxed - 5/3) < 0.05:
        print("✓ SUCCESS: Cauchy K/G = 5/3 RECOVERED after sublattice relaxation.")
        print("  Session 12's K/G = 3 was the rigid-sublattice value.")
        print("  Session 13 diagnosis confirmed: Born–Huang internal-strain fix works.")
    else:
        print("⚠ K/G = 5/3 NOT recovered. Further investigation needed:")
        print("  - Maybe the sublattice position isn't (d/2,d/2,d/2) for K4 diamond")
        print("  - Maybe additional bonds (B's K4 neighbors) need to be included")
        print("  - Diamond has 2 sublattices but 8 atoms per cubic cell; check scope")
    print("=" * 72)


if __name__ == "__main__":
    main()
