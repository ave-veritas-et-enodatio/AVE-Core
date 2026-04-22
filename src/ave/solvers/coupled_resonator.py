"""
Universal Coupled Resonator Solver
==================================

A single framework applied at every scale of the AVE hierarchy.
The same operators appear at each level:

==========  =========================================  ===================
Operator    Formula                                    Source
==========  =========================================  ===================
f_base_resonance     c / r_eff  or  c(1+nu) / r_sat             Axioms 1, 3
k           coupling coefficient (see table)            Axiom 2 / geometry
B           N * hbar * (f_base_resonance - f_bonding_mode)        Normal mode split
capacitive_bias_MeV   (3/5) Z(Z-1) alpha*hbar*c / R              Coulomb self-energy
S(x)        sqrt(1 - x^2)                              Axiom 4 saturation
==========  =========================================  ===================

Cross-Scale Mapping
-------------------

========  ==========  =================  ============  ====================
Scale     r_sat       f_base_resonance            Coupling       f_eigen_eV/Binding
========  ==========  =================  ============  ====================
Nuclear   d_p         c(1+nu)/d_p        k = 2*alpha   N*hbar(w0-w_bond)
                      = 302 MeV/hbar     = 0.01476     (coupled resonator)
--------  ----------  -----------------  ------------  --------------------
Atomic    a0          Z^2*alpha^2*m_e    k_Hopf        N-port Y-matrix
                      *c^2/(hbar*n^2)    (Op4+Op2)     eigenvalue (Op5+Op6)
--------  ----------  -----------------  ------------  --------------------
Molecul.  r_val(f_eigen_eV)   sqrt(f_eigen_A_eV*f_eigen_B_eV)    T^2(N_eff)    Loaded Fabry-Perot
                      (geometric mean)   cavity load   d=V2*V(rA*rB)*V(T2/T2_0)
========  ==========  =================  ============  ====================

ARCHITECTURE NOTE (2026-03-13):
  The atomic f_eigen_eV solver uses the SAME Y-matrix infrastructure as the
  protein and antenna solvers (transmission_line.py):
    - Each electron = one node (self-admittance y = 1/Z_LC)
    - Coupling = mutual admittance through Z_0 = 377 Ohm lattice
    - Same-shell (Hopf link): k_Hopf = (2/Z)(1 - p_c/2)
    - Cross-shell: capacitive coupling, NO Hopf crossings
    - f_eigen_eV from eigenvalue: build_nodal_y_matrix -> s_matrix_from_y -> Op6

  CRITICAL: All electrons see BARE nuclear charge Z. There is no Z_eff.
  "Screening" emerges from the eigenvalue decomposition, not as an input.
  The ionization_energy_circuit() function below is the same-shell-only
  solver (Approach 22). The N-port Y-matrix extension is in development.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import (
    ALPHA,
    C_0,
    D_PROTON,
    HBAR,
    HBAR_C_MEV_FM,
    K_COUPLING,
    M_E,
    M_N_MEV_TARGET,
    M_P_MEV_TARGET,
    NU_VAC,
    P_C as _P_C,
    e_charge,
)

# ─────────────────────────────────────────────────────────────────
# Fundamental circuit parameters (from axioms)
# ─────────────────────────────────────────────────────────────────

# Uncoupled resonant frequency: ω₀ = c / r_eff where r_eff = d_p/(1+ν)
R_EFF = D_PROTON * 1e-15 / (1.0 + NU_VAC)
F_BASE_RESONANCE = C_0 / R_EFF
Z_RESONANCE_MEV = HBAR * F_BASE_RESONANCE / (e_charge * 1e6)  # ≈ 301.6 MeV


# ─────────────────────────────────────────────────────────────────
# Complete graph adjacency eigenvalues
# ─────────────────────────────────────────────────────────────────


def complete_graph_eigenvalues(n):
    """Eigenvalues of the adjacency matrix of K_n: [n-1, -1, -1, ..., -1]."""
    return np.array([n - 1] + [-1] * (n - 1), dtype=float)


def coupled_resonator_binding(n_resonators, k, f_base_resonance=F_BASE_RESONANCE, adjacency_eigenvalues=None):
    r"""
    Compute Z_binding_target_MeV energy from coupled resonator normal mode splitting.

    For N identical resonators with coupling coefficient k and
    adjacency eigenvalues λ_n:

        ω_n = ω₀ / √(1 + k × λ_n)

    Ground state (bosonic): all N resonators occupy the lowest mode.
    Binding = N × ℏ(ω₀ - ω_lowest)

    Args:
        n_resonators: Number of resonators (nucleons or alphas)
        k: Dimensionless coupling coefficient
        f_base_resonance: Uncoupled resonant frequency [rad/s]
        adjacency_eigenvalues: Eigenvalues of the coupling graph.
            If None, uses complete graph K_n.

    Returns:
        Z_binding_target_MeV: Total Z_binding_target_MeV energy [MeV]
        f_coupled_modes: Normal mode frequencies [rad/s]
    """
    if adjacency_eigenvalues is None:
        adjacency_eigenvalues = complete_graph_eigenvalues(n_resonators)

    from ave.core.universal_operators import universal_coupled_mode_frequency

    # Normal mode frequencies
    f_coupled_modes = universal_coupled_mode_frequency(f_base_resonance, k, adjacency_eigenvalues)

    # Ground state: all N in the lowest-frequency (bonding) mode
    f_bonding_mode = np.min(f_coupled_modes)
    Z_binding_target_MeV = n_resonators * HBAR * (f_base_resonance - f_bonding_mode) / (e_charge * 1e6)

    return Z_binding_target_MeV, f_coupled_modes


def hierarchical_binding(n_alphas, k_intra=K_COUPLING, k_inter=K_COUPLING):
    r"""
    Hierarchical Z_binding_target_MeV: alphas at level 1, then alpha assembly at level 2.

    Level 1: Each alpha = 4 nucleons in K₄ with coupling k_intra
        Z_alpha_binding_MeV = 4 × ℏ(ω₀ - ω₀/√(1 + 3k_intra))

    Level 2: N alphas coupled in K_N with coupling k_inter
        The alpha's bonding mode frequency ω_alpha = ω₀/√(1 + 3k_intra)
        becomes the new ω₀ for the next level.
        Z_inter_binding_MeV = N_alpha × ℏ(ω_alpha - ω_alpha/√(1 + (N-1)·k_inter))

    Total: B = N_alpha × Z_alpha_binding_MeV + Z_inter_binding_MeV

    Args:
        n_alphas: Number of alpha clusters
        k_intra: Intra-alpha coupling (default: 2α)
        k_inter: Inter-alpha coupling (default: 2α)

    Returns:
        Z_binding_target_MeV: Total Z_binding_target_MeV energy [MeV]
        Z_alpha_binding_MeV: Per-alpha Z_binding_target_MeV [MeV]
        Z_inter_binding_MeV: Inter-alpha Z_binding_target_MeV [MeV]
    """
    # Level 1: Alpha Z_binding_target_MeV
    Z_alpha_binding_MeV, modes_alpha = coupled_resonator_binding(4, k_intra)

    # Alpha bonding mode frequency
    f_alpha_resonance = np.min(modes_alpha)

    # Level 2: Inter-alpha Z_binding_target_MeV
    Z_inter_binding_MeV, modes_nucleus = coupled_resonator_binding(
        n_alphas, k_inter, f_base_resonance=f_alpha_resonance
    )

    Z_binding_target_MeV = n_alphas * Z_alpha_binding_MeV + Z_inter_binding_MeV
    return Z_binding_target_MeV, Z_alpha_binding_MeV, Z_inter_binding_MeV


def nuclear_mass(Z, A, n_alphas=None):
    r"""
    Compute nuclear mass from the coupled resonator model.

    Circuit model:
        1. Coupled LC resonators → Z_binding_target_MeV energy (attractive)
        2. Coulomb self-energy of Z protons → repulsion

    Coulomb correction (from circuit analysis):
        Z charged resonators at average spacing R = d_p × A^(1/3)
        E_c = (3/5) × Z(Z-1) × αℏc / R

    Args:
        Z: Proton number
        A: Mass number
        n_alphas: Number of alpha clusters (auto-detected if None)

    Returns:
        mass: Nuclear mass [MeV]
        Z_binding_target_MeV: Total Z_binding_target_MeV energy [MeV] (strong - Coulomb)
    """
    N_n = A - Z
    raw_mass = Z * M_P_MEV_TARGET + N_n * M_N_MEV_TARGET

    # Strong Z_binding_target_MeV from coupled resonator model
    if A == 2:
        Z_binding_target_MeV, _ = coupled_resonator_binding(2, K_COUPLING)
    elif A <= 4:
        Z_binding_target_MeV, _ = coupled_resonator_binding(A, K_COUPLING)
    else:
        if n_alphas is None:
            n_alphas = A // 4
        n_valence = A - 4 * n_alphas

        Z_binding_target_MeV, Z_alpha_binding_MeV, Z_inter_binding_MeV = hierarchical_binding(n_alphas)

        # Valence nucleons couple to the nearest alpha
        if n_valence > 0:
            f_alpha_resonance = F_BASE_RESONANCE / np.sqrt(1.0 + 3 * K_COUPLING)
            for _ in range(n_valence):
                Z_val_binding_MeV = HBAR * (f_alpha_resonance - f_alpha_resonance / np.sqrt(1 + K_COUPLING))
                Z_val_binding_MeV /= e_charge * 1e6
                Z_binding_target_MeV += Z_val_binding_MeV

    # Coulomb correction: stored electrostatic energy between Z protons
    # R = d_p × A^(1/3) is the nuclear charge radius (Axiom 1 length scale)
    alpha_hc = ALPHA * HBAR_C_MEV_FM  # αℏc ≈ 1.44 MeV·fm
    R_nucleus = D_PROTON * A ** (1.0 / 3.0)
    capacitive_bias_MeV = 0.6 * Z * (Z - 1) * alpha_hc / R_nucleus

    # Net Z_binding_target_MeV = strong - Coulomb
    binding_net = Z_binding_target_MeV - capacitive_bias_MeV

    return raw_mass - binding_net, binding_net


# ─────────────────────────────────────────────────────────────────
# Level 2: Atomic — f_eigen_eV from total energy in the LINEAR regime
# Level 3: Molecular — bond from saturation coupling
#
# REGIME ANALYSIS:
#   Electron's d_sat = ℓ_node = ℏ/(m_e c) ≈ 3.86e-13 m
#   Inter-electron distance ~ a₀ ≈ 5.29e-11 m
#   Strain: A = d_sat/r = ℓ_node/a₀ = α ≈ 0.007
#   → DEEP in the LINEAR regime (A ≪ 1)
#   → U = -K/r (pure Coulomb, no impedance correction)
#   → Screening from 3D ELECTROSTATIC geometry
#   → The 3D comes from ν = 2/7 (3 spatial / 7 compliance modes)
# ─────────────────────────────────────────────────────────────────

# Atomic scale constants (all from axioms)
_M_E = float(M_E)  # electron mass from constants.py [kg]
_A0 = HBAR / (_M_E * C_0 * ALPHA)  # Bohr radius [m]
_RY_EV = _M_E * C_0**2 * ALPHA**2 / (2.0 * e_charge)  # Rydberg [eV]
_PROJECTION = 1.0 / (2.0 * (1.0 + 2.0 / 7.0))  # 7/18 projection of eigenvalue


# ─────────────────────────────────────────────────────────────────
# QUARANTINE: ~400 lines of QM hydrogen wavefunction Coulomb
# integrals removed (2026-03-13). See pitfall #11.
# ─────────────────────────────────────────────────────────────────

# Aufbau (Madelung) filling order: subshells sorted by (n+l, n)
# This is first-principles under AVE: the LC cavity eigenvalue for
# orbital (n,l) scales with n+l (nuclear penetration), not just n.
_AUFBAU_ORDER = [
    (1, 0, 2),  # 1s
    (2, 0, 2),  # 2s
    (2, 1, 6),  # 2p
    (3, 0, 2),  # 3s
    (3, 1, 6),  # 3p
    (4, 0, 2),  # 4s
    (3, 2, 10),  # 3d
    (4, 1, 6),  # 4p
    (5, 0, 2),  # 5s
    (4, 2, 10),  # 4d
    (5, 1, 6),  # 5p
    (6, 0, 2),  # 6s
    (4, 3, 14),  # 4f
    (5, 2, 10),  # 5d
    (6, 1, 6),  # 6p
    (7, 0, 2),  # 7s
    (5, 3, 14),  # 5f
    (6, 2, 10),  # 6d
    (7, 1, 6),  # 7p
]


def _fill_shells(n_resonators):
    """Fill electron shells using Aufbau (Madelung n+l) order.

    Returns [(n, count), ...] grouped by principal quantum number n.
    The J integrals resolve shells by n only, so subshells within
    the same n are combined.

    Example: K (Z=19) = 2 in n=1, 8 in n=2, 8 in n=3, 1 in n=4
    (not 9 in n=3, which was the previous bug).
    """
    from collections import defaultdict

    shell_counts = defaultdict(int)
    remaining = n_resonators
    for n, l, capacity in _AUFBAU_ORDER:
        if remaining <= 0:
            break
        count = min(remaining, capacity)
        shell_counts[n] += count
        remaining -= count
    return sorted(shell_counts.items())


# ─────────────────────────────────────────────────────────────────
# QUARANTINE: atom_total_energy(), _scf_z_eff() removed
# (2026-03-13). QM SCF loops replaced by coupled LC model.
# ─────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────
# Active f_eigen_eV Solver: Approach 22 (AVE Coupled LC + Hopf Link)
# ─────────────────────────────────────────────────────────────────


def _shell_config(n_resonators):
    """Return outermost subshell (n, l, count) for f_eigen_eV calculation.

    Uses Aufbau order to fill shells, returning the complete electronic configuration up to the outermost structure.
    """
    remaining = n_resonators
    subshells = []
    for n, l, capacity in _AUFBAU_ORDER:
        if remaining <= 0:
            break
        count = min(remaining, capacity)
        subshells.append((n, l, count))
        remaining -= count
    return subshells



def ionization_energy_circuit(Z, n_resonators=None):
    r"""First ionization energy from AVE coupled LC resonator model.

    .. warning:: STRUCTURAL LIMITATION
        This solver uses Z_eff² Ry / n² as a base energy (Pitfall #8).
        This is correct ONLY for l≥1 (p/d/f orbitals) where centrifugal
        cutoff makes Gauss screening exact. For s-orbitals (Li, Be, Na),
        the eigenvalue is intrinsically non-hydrogenic and requires the
        ABCD cascade through the graded screening profile σ(r).
        See radial_eigenvalue.radial_eigenvalue_abcd() for s-block.

    Architecture (Approach 22):
        1. Each electron is an LC resonator at f_base_resonance = Z^2 alpha^2 m_e c^2 / hbar
        2. Same-shell pairs form Hopf links with per-pair coupling:
           k_pair = (2/Z_eff)(1 - p_c/c_Hopf) = (2/Z_eff)(1 - p_c/2)
           where p_c/2 is a TOPOLOGICAL CONSTANT from the Hopf link
           crossing number (c=2), NOT p_c/N.
        3. N same-shell electrons: bonding mode omega_bond = f_base_resonance / sqrt(1 + k_pair*(N-1))
           N enters via K_N adjacency eigenvalue, NOT through p_c.
        4. Cross-shell: Gauss's law screening (sigma = N_inner), no Hopf link.
        5. f_eigen_eV = f_0_resonance_eV * (N/sqrt(1+k(N-1)) - (N-1)/sqrt(1+k(N-2)))

    Operator compliance:
        Op1: Z_LC = sqrt(L/C) (torus impedance)
        Op2: p_c saturation at Hopf link crossings
        Op4: Coulomb coupling C_rep = C/Z_eff
        Op5: K_N eigenvalue for N-electron mode
        Op6: eigenvalue from resonance condition

    Args:
        Z: Atomic number.
        n_resonators: Number of electrons (default: Z for neutral).

    Returns:
        f_eigen_eV in eV.
    """
    if n_resonators is None:
        n_resonators = Z

    # Single electron: exact hydrogenic
    if n_resonators <= 1:
        return Z**2 * _RY_EV

    shells = _shell_config(n_resonators)
    n_out, l_out, c_out = shells[-1]  # outermost subshell

    # Cross-shell: inner spheres vs lateral domains
    N_inner = 0
    N_lateral = 0.0
    for n, l, count in shells[:-1]:
        if n < n_out:
            N_inner += count
        elif n == n_out:
            # Lateral co-radial shielding: Orthogonal subshells (like 3s screening 3p)
            # do not spherically enclose each other. They interact via the K4 lattice
            # transverse Poisson ratio limit. A geometry mapping coefficient of 0.5 is applied.
            N_lateral += count * 0.5

    Z_eff_cross = Z - N_inner - N_lateral
    Z_eff_cross = max(1.0, Z_eff_cross)

    # Single-electron Z_binding_target_MeV at effective charge
    f_0_resonance_eV = Z_eff_cross**2 * _RY_EV / n_out**2

    # Same-shell coupling (if >1 electron in outermost shell)
    if c_out <= 1:
        return f_0_resonance_eV

    # PER-PAIR coupling: k_pair = (2/Z_eff)(1 - p_c/c_Hopf)
    # p_c/2 is TOPOLOGICAL CONSTANT from Hopf link crossing number (c=2).
    # Same p_c/2 appears in J_1s2 = 1/2 + p_c/2 (same physics, opposite sign).
    # Cross-shell electrons don't form Hopf links (non-intersecting tori).
    k_pair = (2.0 / Z_eff_cross) * (1.0 - float(_P_C) / 2.0)

    # K_N adjacency eigenvalue: shell occupancy enters here, NOT p_c
    N_same = c_out
    lam = N_same - 1  # K_N bonding eigenvalue (complete graph)

    # f_eigen_eV from coupled resonator normal mode splitting
    # For N=2: f_eigen_eV = f_0_resonance_eV * (2/sqrt(1+k_pair) - 1)
    # General: f_eigen_eV = f_0_resonance_eV * (N*omega(N) - (N-1)*omega(N-1))
    from ave.core.universal_operators import universal_coupled_mode_frequency

    if N_same == 2:
        f_bond_2 = universal_coupled_mode_frequency(1.0, k_pair, 1.0)
        f_eigen_eV = f_0_resonance_eV * (2.0 * f_bond_2 - 1.0)
    else:
        f_bond_N = universal_coupled_mode_frequency(1.0, k_pair, lam)
        f_bond_Nm1 = universal_coupled_mode_frequency(1.0, k_pair, lam - 1)
        f_eigen_eV = f_0_resonance_eV * (N_same * f_bond_N - (N_same - 1) * f_bond_Nm1)

    return max(0.0, f_eigen_eV)


def ionization_energy_cavity(Z, n_resonators=None):
    r"""First ionization energy from AVE mutual cavity loading.

    .. warning:: STRUCTURAL LIMITATION
        This solver uses Z_eff² Ry / n² as a base energy.
        This is correct ONLY for l≥1 (p-block: B–Ne, Al–Ar) where
        Gauss screening is exact. Fails for s-orbitals (Li, Be, Na).
        See radial_eigenvalue.radial_eigenvalue_abcd() for s-block.

    Architecture (Mutual Cavity Loading):
        1. Base energy f_0_resonance_eV = Z_eff^2 * Ry / n^2
           Cross-shell Gauss screening: Z_eff = max(1, Z - N_inner)
        2. Op1 + Axiom 3 (Impedance Loading): N_eff = N_s + N_p/2
           The cavity impedance is loaded to Z_0 / N_eff.
        3. Op3 (Reflection): T^2(N_eff) = 4 * N_eff / (1 + N_eff)^2
        4. Total energy f_total_resonance_eV(N) = N_eff * f_0_resonance_eV * T^2(N_eff)
        5. f_eigen_eV = f_total_resonance_eV(N) - f_total_resonance_eV(N-1)

    Edge cases handled:
        - Base topological cavity loading (predicts B, C, N, Ne to ~1%)
        - TODO: s-orbital penetration for Li, Be
        - TODO: p-orbital pairing penalty for O, F

    Args:
        Z: Atomic number.
        n_resonators: Number of electrons (default: Z for neutral).

    Returns:
        f_eigen_eV in eV.
    """
    if n_resonators is None:
        n_resonators = Z

    if n_resonators <= 1:
        return Z**2 * _RY_EV

    shells = _fill_shells(n_resonators)
    n_out = shells[-1][0]
    N_out = shells[-1][1]
    N_inner = n_resonators - N_out

    Z_eff = max(1.0, Z - N_inner)
    f_base_resonance_eV = Z_eff**2 * _RY_EV / n_out**2

    # Op1 + Axiom 3 loading
    N_s = min(N_out, 2)
    N_p = max(0, N_out - 2)
    N_eff = N_s + N_p / 2.0

    # N-1 state
    if N_out == 1:
        N_s_m1 = 0
        N_p_m1 = 0
    else:
        if N_p > 0:
            N_s_m1 = N_s
            N_p_m1 = N_p - 1
        else:
            N_s_m1 = max(0, N_s - 1)
            N_p_m1 = 0
    N_eff_m1 = N_s_m1 + N_p_m1 / 2.0

    from ave.core.universal_operators import universal_power_transmission

    def topological_pairing_penalty(n_p):
        """Topological strain from intersecting 1D p-orbital flux loops.
        By Axiom (Op2), topological saturation limits pairing density.
        1 pair: 4*alpha strain (maximum asymmetry)
        2 pairs: 6*alpha strain
        3 pairs: 6*alpha strain (full shell spherical symmetry restored, marginal strain=0)
        """
        pairs = max(0, n_p - 3)
        if pairs == 1:
            return 4.0 * ALPHA
        elif pairs >= 2:
            return 6.0 * ALPHA
        return 0.0

    f_total_resonance_eV_std = N_eff * f_base_resonance_eV * universal_power_transmission(N_eff)
    f_total_resonance_eV_m1_std = N_eff_m1 * f_base_resonance_eV * universal_power_transmission(N_eff_m1)

    angular_reactance_penalty = topological_pairing_penalty(N_p) * f_base_resonance_eV
    angular_reactance_penalty_m1 = topological_pairing_penalty(N_p_m1) * f_base_resonance_eV

    f_total_resonance_eV = f_total_resonance_eV_std - angular_reactance_penalty
    f_total_resonance_eV_m1 = f_total_resonance_eV_m1_std - angular_reactance_penalty_m1

    f_eigen_eV = f_total_resonance_eV - f_total_resonance_eV_m1
    return max(0.0, f_eigen_eV)


def ionization_energy(Z, n_resonators=None):
    r"""First ionization energy — dispatches to AVE mutual cavity loading solver.

    .. warning::
        Currently dispatches to ionization_energy_cavity(), which is
        structurally limited to p-block (l≥1) atoms. Does NOT handle
        s-orbital penetration (Li, Be, Na fail at −37% to −71%).
        For s-block atoms, use radial_eigenvalue.ionization_energy_e2k()
        or radial_eigenvalue.radial_eigenvalue_abcd() directly.

    Args:
        Z: Atomic number.
        n_resonators: Number of electrons (default: Z).

    Returns:
        f_eigen_eV in eV.
    """
    return ionization_energy_cavity(Z, n_resonators)


def atom_port_impedance(Z, f_eigen_eV):
    r"""
    Atom's port impedance = valence orbital radius.

    r_val = n × a₀ × √(Ry/f_eigen_eV)  [meters]
    """
    shells = _fill_shells(Z)
    n = shells[-1][0]
    return n * _A0 * np.sqrt(_RY_EV / f_eigen_eV)


# ─────────────────────────────────────────────────────────────────
# QUARANTINE: Y-Matrix f_eigen_eV Solver (Approach 22) removed (2026-03-30).
# ~275 lines (_electron_config, _ring_parameters, _pair_coupling,
# _total_energy_from_ymatrix, ionization_energy_ymatrix).
# Superseded by ionization_energy_cavity() (Mutual Cavity Loading).
# ─────────────────────────────────────────────────────────────────
# QUARANTINE: Dead f_eigen_eV solvers (v2, v3, v4, v5, v5.5) removed
# (2026-03-13). ~250 lines. Superseded by Approach 24 (E2k):
# all operators inside V_eff(r), one-pass ABCD cascade.
# ─────────────────────────────────────────────────────────────────


def molecular_bond_distance(r_A, r_B, Z_A=1, Z_B=1, bond_order=1):
    r"""
    Bond distance as Fabry-Perot cavity eigenvalue with unified mode loading.

    The effective loading of the cavity (N_eff) counts the continuous
    longitudinal modes bounded by the two nuclear singularities:
        - 2 electrons per bond order (\sigma = 2, \pi = 2).
        - The spherically-symmetric s^2 shells (if present) degenerate-hybridize
          into a single contiguous mode, contributing 1.0 (2 electrons / 2).

    N_eff = 2 * bond_order + \max(N_{s_A}, N_{s_B}) / 2

    Base standard unloaded eigenvalue (two-electron): d = \sqrt{2} * \sqrt{r_A * r_B}
    d = d_base * \sqrt{T^2(N_eff) / T^2(2)}

    Args:
        r_A: Port impedance of atom A (metres).
        r_B: Port impedance of atom B (metres).
        Z_A: Atomic number of atom A (to determine s-shell loading).
        Z_B: Atomic number of atom B (to determine s-shell loading).
        bond_order: Number of structural bonds (1=single, 2=double, 3=triple).
    """

    # Non-bonding 2s^2 electrons loading the bond cavity.
    # For H (Z=1), N_s = 0. For heavier atoms with filled s-shells, N_s = 2.
    def get_ns(z):
        return 0 if z == 1 else 2

    N_eff = 2.0 * bond_order + max(get_ns(Z_A), get_ns(Z_B)) / 2.0

    d_base = np.sqrt(2.0) * np.sqrt(r_A * r_B)

    from ave.core.universal_operators import universal_power_transmission

    # Baseline unloaded cavity is N_eff = 2 (e.g., H-H bond)
    if N_eff <= 2.0:
        return d_base

    return d_base * np.sqrt(universal_power_transmission(N_eff) / universal_power_transmission(2.0))


def molecular_bond_energy(f_eigen_A_eV, f_eigen_B_eV, r_val_A, r_val_B, d_bond):
    r"""Molecular bond energy from coupled resonant cavities.

    PHYSICAL MODEL:
      Two atoms (resonant cavities) A and B couple via their outermost
      electron shells. The coupling strength k is a function of bond
      distance d. The bond energy is the reduction in total energy
      due to this coupling.

    UNIVERSAL OPERATOR: B = 2ω(1 − 1/√(1+k))  [Axiom 5]

    DIMENSIONAL ANALYSIS:
      ω_eff = √(f_eigen_A_eV × f_eigen_B_eV) [eV]
      k_eff = k(d) [dimensionless]
      B_eV = [eV] × (1 - 1/√(1 + [dimensionless])) = [eV] ✓

    Args:
        f_eigen_A_eV: Ionization energy of atom A (eV).
        f_eigen_B_eV: Ionization energy of atom B (eV).
        r_val_A: Effective radius of atom A (Bohr).
        r_val_B: Effective radius of atom B (Bohr).
        d_bond: Bond distance (Bohr).

    Returns:
        B_eV: Bond energy in eV. Positive = stable bond.
        k_eff: Effective coupling constant.
    """
    # Effective frequency (geometric mean of IEs)
    f_eff_resonance = np.sqrt(f_eigen_A_eV * f_eigen_B_eV)

    # Effective coupling constant k(d)
    # This is the universal saturation function S(x) = x / sqrt(1 + x^2)
    # where x = (r_A * r_B) / d_bond^2
    x = (r_val_A * r_val_B) / d_bond**2
    if x > 10.0:
        import logging

        logging.warning("AVE Limit Warning: Molecular bond structural strain exceeded local percolation limits")
    k_eff = x / np.sqrt(1.0 + x**2)

    from ave.core.universal_operators import universal_coupled_mode_frequency

    # Bond energy from Axiom 5
    f_coupled = universal_coupled_mode_frequency(f_eff_resonance, k_eff, 1.0)
    B_eV = 2.0 * (f_eff_resonance - f_coupled)
    return B_eV, k_eff


# ─────────────────────────────────────────────────────────────────
# QUARANTINE: QM radial potentials, atomic_resonance, and
# ionization_energy_cascade removed (2026-03-13). ~630 lines.
# N*N dynamical matrix architecture preserved in plan.
# ─────────────────────────────────────────────────────────────────
