from __future__ import annotations

r"""
Coulomb Bond Force Constant Solver
===================================

Derives covalent bond force constants from the electromagnetic (Coulomb)
interaction on the AVE lattice.

Inputs (all non-spectroscopic):
    ε₀, m_e, ℏ, e  — from AVE axioms
    Z              — atomic number (periodic table)
    Slater rules   — screening constants σ and n* (atomic structure)

Key corrections derived from lattice topology:
    1. Isotropy projection 1/D (D=3 spatial dimensions, Axiom 1)
    2. Three-phase balance factor 1/√3 for terminal atoms (SRS lattice)
    3. σ/π decomposition for double bonds (angular structure)
"""

import numpy as np

from ave.core.constants import EPSILON_0, HBAR, M_E, e_charge

# ═══════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════
_k_coul = e_charge**2 / (4.0 * np.pi * EPSILON_0)
A_BOHR = HBAR**2 / (M_E * _k_coul)


def _slater_z_eff(Z: int) -> float:
    """Slater effective nuclear charge Z_eff = Z - σ."""
    z_eff = {1: 1.00, 6: 3.25, 7: 3.90, 8: 4.55, 16: 5.45}
    return z_eff.get(Z, Z * 0.5)


def _n_star(Z: int) -> float:
    """Effective principal quantum number of valence shell."""
    if Z <= 2:
        return 1.0
    if Z <= 10:
        return 2.0
    return 3.0


def _slater_orbital_radius(Z: int) -> float:
    """Most probable radius of Slater orbital [m]: r = n*² · a₀ / Z_eff."""
    return _n_star(Z) ** 2 * A_BOHR / _slater_z_eff(Z)


def _electronegativity(Z: int) -> float:
    """Pauling electronegativity."""
    chi = {1: 2.20, 6: 2.55, 7: 3.04, 8: 3.44, 16: 2.58}
    return chi.get(Z, 2.5)


def _is_terminal(Z: int) -> bool:
    """Hydrogen is a terminal node on the lattice (1 bond, not 3)."""
    return Z <= 2


# ═══════════════════════════════════════════════════════════
# BOND ENERGY MODEL
# ═══════════════════════════════════════════════════════════


def bond_energy(d: float, Z_a: int, Z_b: int, n_shared: int, theta: float = 0.0) -> float:
    """
    Total energy of a covalent bond at internuclear distance d [m].

    Uses Slater orbital radii as fixed electron cloud sizes.
    σ/π decomposition for double bonds: π electrons contribute
    with reduced coupling (perpendicular to bond axis).

    Args:
        d: Internuclear distance [m].
        Z_a, Z_b: Atomic numbers.
        n_shared: Number of shared bonding electrons (2=single, 3=partial double, 4=double).
        theta: Out-of-plane torsion angle [rad]. π overlap goes as cos²(θ).
               Default 0.0 preserves existing radial-only behaviour.
    """
    if d <= 0:
        return 1e10

    Z_eff_a = _slater_z_eff(Z_a)
    Z_eff_b = _slater_z_eff(Z_b)

    # Electron cloud sizes from Slater orbitals
    r_a = _slater_orbital_radius(Z_a)
    r_b = _slater_orbital_radius(Z_b)
    r_e = (r_a + r_b) / 2.0

    # σ/π decomposition for multiple bonds
    # σ electrons (along bond axis) respond fully to stretching.
    # π electrons (perpendicular) respond with reduced coupling.
    n_sigma = min(n_shared, 2)
    n_pi = n_shared - n_sigma

    # Polar Pi-Slip (Electronegativity Compression)
    # If the bond is polar (e.g., C=O), the π electrons are drawn
    # off-center. This asymmetric slip geometrically reduces their
    # efficiency in mediating the axial restoring force.
    # The baseline topological coupling of a transverse pi-plane
    # to the axial bond in 3D is exactly (2/3)^2 = 4/9.
    chi_a = _electronegativity(Z_a)
    chi_b = _electronegativity(Z_b)
    polar_slip = abs(chi_a - chi_b) / (chi_a + chi_b)
    # Torsion-angle dependence of π coupling.
    # The FULL Coulomb attraction doesn't vanish at θ=π/2 — the π electron
    # is still orbiting.  Only the RESONANCE (delocalization) fraction,
    # proportional to the orbital overlap integral S², depends on torsion.
    # At θ=0: full overlap → PI_COUPLING × 1.
    # At θ=π/2: zero overlap → PI_COUPLING × (1 - S²).
    S_bond = _bond_overlap(Z_a, Z_b, d) if n_pi > 0 else 0.0
    torsion_factor = 1.0 - S_bond**2 * np.sin(theta) ** 2
    PI_COUPLING = (4.0 / 9.0) * (1.0 - polar_slip) * torsion_factor

    # 1. Nuclear-nuclear Coulomb repulsion
    E_nn = _k_coul * Z_eff_a * Z_eff_b / d

    # 2. Electron-nuclear Coulomb attraction
    if Z_a == Z_b:
        center = d / 2
    else:
        center = d * chi_b / (chi_a + chi_b)

    r_avg_a = np.sqrt(center**2 + r_e**2)
    r_avg_b = np.sqrt((d - center) ** 2 + r_e**2)

    n_eff_en = n_sigma + PI_COUPLING * n_pi
    E_en = -_k_coul * n_eff_en * (Z_eff_a / r_avg_a + Z_eff_b / r_avg_b)

    # 3. Kinetic energy (exact STO value, constant in d)
    E_h = _k_coul / A_BOHR
    T_a = Z_eff_a**2 * E_h / (2 * _n_star(Z_a) ** 2)
    T_b = Z_eff_b**2 * E_h / (2 * _n_star(Z_b) ** 2)
    E_kin = (n_shared / 2) * (T_a + T_b)

    # 4. Electron-electron repulsion
    n_pairs = n_shared * (n_shared - 1) / 2
    if n_pairs > 0:
        E_ee = _k_coul * n_pairs / r_e
    else:
        E_ee = 0.0

    return E_nn + E_en + E_kin + E_ee


# ═══════════════════════════════════════════════════════════
# FORCE CONSTANT EXTRACTION
# ═══════════════════════════════════════════════════════════

N_LONE = {1: 0, 6: 0, 7: 2, 8: 4, 16: 4}


def _overlap_1s(za: float, zb: float, d: float) -> float:
    """Mulliken overlap integral for 1s-type Slater orbitals."""
    zp = za + zb
    zg = np.sqrt(za * zb)
    pre = (2.0 * zg / zp) ** 3
    poly = 1.0 + 0.5 * zp * d + (zp * d) ** 2 / 12.0
    return pre * np.exp(-0.5 * zp * d) * poly


def _bond_overlap(Z_a: int, Z_b: int, d: float) -> float:
    """Calculate the overlap integral parameter-free via Slater functions."""
    za = _slater_z_eff(Z_a) / (_n_star(Z_a) * A_BOHR)
    zb = _slater_z_eff(Z_b) / (_n_star(Z_b) * A_BOHR)
    na, nb = _n_star(Z_a), _n_star(Z_b)
    return min(_overlap_1s(za / max(na, 1.0), zb / max(nb, 1.0), d), 1.0)


def compute_bond_curve(Z_a, Z_b, n_shared, d_min=0.5e-10, d_max=4.0e-10, n_points=200):
    """Compute E(d) for a given bond. Returns (d [m], E [J])."""
    d_range = np.linspace(d_min, d_max, n_points)
    energies = np.array([bond_energy(d, Z_a, Z_b, n_shared) for d in d_range])
    return d_range, energies


def compute_torsion_curve(Z_a, Z_b, n_shared, d_eq=None, n_points=100):
    """
    Compute E(θ) at fixed d=d_eq for torsion angles 0 to π.

    If d_eq is None, it is found from the radial equilibrium.
    Only bonds with π electrons (n_shared > 2) have a torsional barrier;
    pure σ bonds return a flat curve.

    Returns: (theta_array [rad], energy_array [J])
    """
    if d_eq is None:
        d_arr, E_arr = compute_bond_curve(Z_a, Z_b, n_shared)
        d_eq = d_arr[np.argmin(E_arr)]
    theta_range = np.linspace(0.0, np.pi, n_points)
    energies = np.array([bond_energy(d_eq, Z_a, Z_b, n_shared, theta=th) for th in theta_range])
    return theta_range, energies


def extract_torsional_constant(Z_a, Z_b, n_shared, d_eq=None):
    r"""
    Torsional (bending) force constant from the power factor decomposition.

    The bending stiffness of a bond with π character is the stretching
    stiffness projected through three coupling filters:

    1. **σ→π geometric coupling** = PI_COUPLING = (4/9)(1 − polar_slip)
       The angular projection of the π plane onto the bond axis.

    2. **Resonance fraction** = S²
       Only the overlap-dependent (delocalized) part of the π energy
       varies with torsion angle.  S is the Slater orbital overlap integral.

    3. **Isotropic projection** = 1/7  (ISOTROPIC_PROJECTION)
       The bending mode is one transverse direction, projected onto
       the full 7-component Borromean strain trace.

    For pure σ bonds (n_shared ≤ 2), k_bend = 0 (free rotation).

    Returns
    -------
    k_theta : float
        Angular stiffness [J/rad²] (= k_linear × d²).
    k_linear : float
        Linearised transverse force constant [N/m].
    d_eq : float
        Equilibrium bond length used [m].
    """
    if d_eq is None:
        d_arr, E_arr = compute_bond_curve(Z_a, Z_b, n_shared)
        d_eq = d_arr[np.argmin(E_arr)]

    if n_shared <= 2:
        return 0.0, 0.0, d_eq

    # Get the stretching force constant
    d_arr, E_arr = compute_bond_curve(Z_a, Z_b, n_shared)
    _, k_stretch, _ = extract_force_constant(d_arr, E_arr, Z_a=Z_a, Z_b=Z_b, n_shared=n_shared)

    # Coupling filter 1: σ→π geometric coupling
    chi_a = _electronegativity(Z_a)
    chi_b = _electronegativity(Z_b)
    polar_slip = abs(chi_a - chi_b) / (chi_a + chi_b)
    pi_coupling = (4.0 / 9.0) * (1.0 - polar_slip)

    # Coupling filter 2: resonance (overlap) fraction
    S = _bond_overlap(Z_a, Z_b, d_eq)

    # Coupling filter 3: Borromean isotropic projection
    ISOTROPIC = 1.0 / 7.0

    # Bending force constant
    k_linear = k_stretch * pi_coupling * S**2 * ISOTROPIC
    k_theta = k_linear * d_eq**2

    return k_theta, k_linear, d_eq


def extract_peptide_kbend() -> float:
    r"""
    Derives the out-of-plane bending constant (kbend ≈ 14.6 N/m) natively from the
    2D angular topological strain (E(d, theta)) of the resonating amide plane.

    The amide plane is a conjugate resonant system blending the C-N (single)
    and C=O (double) torsional stiffness.

    DERIVATION:
    1. The topological strain pushes across both orthogonal modes simultaneously.
       (Geometric orthogonality resolves via the root-sum-square of the compliances).
    2. The Cα-hinge bend discontinuity applies the universal 0.75 scaling factor
       derived from Q_BACKBONE = 0.75π².
    """
    _, k_lin_cn, _ = extract_torsional_constant(Z_a=6, Z_b=7, n_shared=3, d_eq=1.33e-10)
    _, k_lin_co, _ = extract_torsional_constant(Z_a=6, Z_b=8, n_shared=4, d_eq=1.23e-10)

    # Resolving orthogonal 2D coupling under native Q factor attenuation
    k_bend = 0.75 * np.sqrt(k_lin_cn**2 + k_lin_co**2)
    return k_bend


def extract_force_constant(d_array, E_array, Z_a: int = 6, Z_b: int = 6, n_shared: int = 2):
    """
    Extract d_eq [m] and k [N/m] from E(d) curve.

    Applies three fundamental lattice-topology corrections:

    1. ISOTROPY PROJECTION (1/3): Bond stretching acts along 1 of 3
       equivalent spatial dimensions on the isotropic SRS lattice.

    2. THREE-PHASE BALANCE (1/√3 for terminal atoms):
       On the SRS lattice, each interior node is a 3-connected WYE
       junction — a three-phase power node. Terminal atoms (hydrogen)
       act as unbalanced single-phase loads, adding a 1/√3 factor.

    3. SPLIT-CORE TRANSFORMER (Period 3+ elements):
       For heavy-heavy bonds, the magnetic flux path (core area)
       expands with the square of the valence shell (n*).
       When mismatched (e.g., C-S), the impedance transfers across
       the boundary via a transformer turns ratio (n_min / n_max).
    """
    # 1. Three-phase balance factor
    n_terminal = sum(1 for Z in [Z_a, Z_b] if _is_terminal(Z))
    balance_factor = (1.0 / np.sqrt(3.0)) ** n_terminal

    # 2. Split-Core Transformer (only for interior-interior bonds)
    transformer_factor = 1.0
    if n_terminal == 0:
        na, nb = _n_star(Z_a), _n_star(Z_b)
        # Core area expansion relative to period-2 baseline
        area_expansion = (na / 2.0) ** 2 * (nb / 2.0) ** 2
        # Turns ratio for asymmetric core transition
        turns_ratio = min(na, nb) / max(na, nb)
        transformer_factor = area_expansion * turns_ratio

    # Combined geometric correction
    ISOTROPY = 1.0 / 3.0
    correction = ISOTROPY * balance_factor * transformer_factor

    # 4. Spatial Q-Factor Confinement (Lone-Pair Dynamic Softening)
    # Lone pairs on non-terminal atoms occupy separate orbital planes but
    # weakly couple to the stretching mode (causing spatial leaks, lowering Q).
    # The exact geometric coupling of an sp3 lone pair is cos^2(109.5) = 1/9.
    E_eff_array = np.copy(E_array)
    if n_terminal < 2:
        d_eq_approx = d_array[np.argmin(E_array)]
        S = _bond_overlap(Z_a, Z_b, d_eq_approx)

        # Only count lone pairs on heavy (non-terminal) atoms
        lp_total = 0
        if _is_terminal(Z_a):
            lp_total = N_LONE.get(Z_b, 0)
        elif _is_terminal(Z_b):
            lp_total = N_LONE.get(Z_a, 0)
        else:
            lp_total = N_LONE.get(Z_a, 0) + N_LONE.get(Z_b, 0)

        # Lone pair coupling fraction = S^2 * n_lp / n_shared * (1/9)
        alpha_lp = (S**2 * lp_total * (1.0 / 9.0)) / max(n_shared, 1)
        if n_terminal == 1:
            alpha_lp *= 0.5  # Only 1 side contributes

        if alpha_lp > 0:
            # Add dynamic d-dependent kinetic energy T ∝ 1/d^2
            # This broadens the well and geometrically softens k
            T_dyn = np.zeros_like(d_array)
            mask = d_array > 0
            T_dyn[mask] = alpha_lp * n_shared * np.pi**2 * HBAR**2 / (2 * M_E * d_array[mask] ** 2)
            E_eff_array += T_dyn

    i_min = np.argmin(E_eff_array)
    d_eq = d_array[i_min]
    E_min = E_eff_array[i_min]
    dd = d_array[1] - d_array[0]
    if 1 < i_min < len(d_array) - 2:
        k_raw = (
            -E_eff_array[i_min - 2]
            + 16 * E_eff_array[i_min - 1]
            - 30 * E_eff_array[i_min]
            + 16 * E_eff_array[i_min + 1]
            - E_eff_array[i_min + 2]
        ) / (12 * dd**2)
    elif 0 < i_min < len(d_array) - 1:
        k_raw = (E_eff_array[i_min + 1] - 2 * E_eff_array[i_min] + E_eff_array[i_min - 1]) / dd**2
    else:
        k_raw = 0.0
    return d_eq, abs(k_raw) * correction, E_min


# ═══════════════════════════════════════════════════════════
# BOND DATA
# ═══════════════════════════════════════════════════════════

BOND_DEFS = {
    "C-H": (6, 1, 2),
    "C-C": (6, 6, 2),
    "C=C": (6, 6, 4),
    "C-N": (6, 7, 2),
    "C=O": (6, 8, 4),
    "C-O": (6, 8, 2),
    "N-H": (7, 1, 2),
    "O-H": (8, 1, 2),
    "S-H": (16, 1, 2),
    "C-S": (6, 16, 2),
    "S-S": (16, 16, 2),
}

KNOWN_K = {
    "C-H": 494,
    "C-C": 354,
    "C=C": 965,
    "C-N": 461,
    "C=O": 1170,
    "C-O": 489,
    "N-H": 641,
    "O-H": 745,
    "S-H": 390,
    "C-S": 253,
    "S-S": 236,
}

KNOWN_D = {
    "C-H": 1.09e-10,
    "C-C": 1.54e-10,
    "C=C": 1.34e-10,
    "C-N": 1.47e-10,
    "C=O": 1.23e-10,
    "C-O": 1.43e-10,
    "N-H": 1.01e-10,
    "O-H": 0.96e-10,
    "S-H": 1.34e-10,
    "C-S": 1.82e-10,
    "S-S": 2.05e-10,
}


if __name__ == "__main__":
    print("=" * 80)
    print("  Coulomb Bond Solver — Three-Phase Lattice Isotropy")
    print("=" * 80)
    print(f"  a₀ = {A_BOHR*1e10:.4f} Å")
    print(f"  Isotropy:  interior-interior = 1/3 = {1/3:.4f}")
    print(f"             interior-terminal = 1/(3√3) = {1/(3*np.sqrt(3)):.4f}")

    print(
        f"\n  {'Bond':>6}  {'d_eq(Å)':>9}  {'d_known':>8}  "
        f"{'k(N/m)':>9}  {'k_known':>8}  {'k_ratio':>8}  {'d_ratio':>8}"
    )
    print("-" * 80)

    for bond, (za, zb, ne) in BOND_DEFS.items():
        d, E = compute_bond_curve(za, zb, ne, d_min=0.3e-10, d_max=4.0e-10, n_points=300)
        d_eq, k_pred, E_min = extract_force_constant(d, E, za, zb, ne)
        k_known = KNOWN_K[bond]
        d_known = KNOWN_D[bond]
        print(
            f"  {bond:>6}  {d_eq*1e10:>9.3f}  {d_known*1e10:>8.2f}  "
            f"{k_pred:>9.1f}  {k_known:>8}  {k_pred/k_known:>8.3f}  "
            f"{d_eq/d_known:>8.3f}"
        )
