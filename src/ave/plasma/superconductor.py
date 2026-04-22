"""
AVE Superconductivity: Magnetic Saturation as Meissner Onset
=============================================================

Superconductivity in the AVE framework is the DUAL of plasma physics.

  Plasma:         ε_eff → 0   →  E-field expelled (Debye screening)
  Superconductor: μ_eff → 0   →  B-field expelled (Meissner effect)

Both use the SAME saturation operator ``saturation_factor(A, A_yield)``:

  Plasma:          S(E·ℓ/V_snap)  drives ε_eff = ε₀·S
  Superconductor:  S(B/B_c)       drives μ_eff = μ₀·S

The BCS critical field formula B_c(T) = B_c0·√(1 − (T/T_c)²) is
LITERALLY ``saturation_factor(T, T_c)`` applied to temperature.
This identity was hiding in plain sight; it proves that the
superconducting phase transition is the thermal-sector instance
of Axiom 4 dielectric saturation.

Physical picture (from the manuscript Ch. 8):
  - Each electron is an inductive flywheel storing helicity.
  - At T > T_c: thermal noise shatters coupling → gears slip → resistance.
  - At T < T_c: noise drops below coupling threshold → gears lock →
    the entire lattice becomes a rigid phase-locked gear train.
  - External B-field = boundary torque on infinitely rigid gearbox → rejected.
  - Penetration = exponential angular momentum decay = London depth λ_L.

Correspondences with plasma ``cutoff.py``:

    Plasma                          Superconductor
    ──────                          ──────────────
    ε_eff = ε₀ · S(V/V_snap)       μ_eff = μ₀ · S(B/B_c)
    ω_p = √(n_e e²/m_e ε₀)        1/λ_L = √(μ₀ n_s e²/m*)
    skin depth δ = c / ω_p         London depth λ_L
    Γ → −1 for ω < ω_p             Γ → −1 for B < B_c
"""

from __future__ import annotations


import numpy as np
from dataclasses import dataclass

from ave.core.constants import (
    EPSILON_0,
    MU_0,
    Z_0,
    e_charge,
    M_E,
    HBAR,
)
from ave.axioms.scale_invariant import (
    saturation_factor,
    mu_eff as _si_mu_eff,
    impedance,
    reflection_coefficient,
)


# ═══════════════════════════════════════════════════════════════
# Core saturation functions — the magnetic dual of plasma
# ═══════════════════════════════════════════════════════════════


def critical_field(T: float | np.ndarray, T_c: float, B_c0: float) -> float | np.ndarray:
    r"""
    Thermodynamic critical field as a function of temperature.

    .. math::
        B_c(T) = B_{c0} \cdot \sqrt{1 - (T/T_c)^2}

    This is EXACTLY ``saturation_factor(T, T_c)`` — the same Axiom 4
    operator that confines particles, drives FDTD, causes plasma cutoff,
    and produces flat galaxy rotation curves.

    Physical meaning: the condensate's pair-breaking energy decreases
    with temperature via the same √(1−r²) that governs all saturation
    in the AVE framework.

    Args:
        T: Temperature [K] (scalar or array).
        T_c: Critical temperature [K].
        B_c0: Critical field at T = 0 [T].

    Returns:
        Critical magnetic field at temperature T [T].
    """
    # saturation_factor clips at yield → B_c = 0 above T_c
    S = saturation_factor(T, T_c)
    return B_c0 * S


def meissner_mu_eff(B_applied: float | np.ndarray, B_critical: float) -> float | np.ndarray:
    r"""
    Effective permeability in the superconducting state.

    .. math::
        \mu_{eff}(B) = \mu_0 \cdot \sqrt{1 - (B/B_c)^2}

    When B < B_c: μ_eff ≈ μ₀ (supports field weakly near boundary).
    When B → B_c: μ_eff → 0 (inductor shorts — total screening).
    When B = 0:   μ_eff = μ₀ (but bulk is shielded, so B stays 0).

    This is the DUAL of plasma ε_eff = ε₀·S(V/V_snap) in ``cutoff.py``.

    Args:
        B_applied: Applied magnetic field [T].
        B_critical: Critical field at current temperature [T].

    Returns:
        Effective permeability [H/m].
    """
    return _si_mu_eff(B_applied, B_critical, mu_base=MU_0)


def superconducting_impedance(B_applied: float | np.ndarray, B_critical: float) -> float | np.ndarray:
    r"""
    Characteristic impedance of the superconducting medium.

    .. math::
        Z_{sc}(B) = \sqrt{\mu_{eff}(B) / \varepsilon_0}

    When B → 0: Z_sc → Z₀ (vacuum-like, but B is expelled).
    When B → B_c: Z_sc → 0 (perfect short — all energy reflected).

    Args:
        B_applied: Applied magnetic field [T].
        B_critical: Critical field [T].

    Returns:
        Impedance [Ω].
    """
    mu = meissner_mu_eff(B_applied, B_critical)
    return impedance(mu, EPSILON_0)


def meissner_reflection(B_applied: float | np.ndarray, B_critical: float) -> float | np.ndarray:
    r"""
    Reflection coefficient at the vacuum–superconductor boundary.

    .. math::
        \Gamma = \frac{Z_{sc} - Z_0}{Z_{sc} + Z_0}

    When B_applied ≈ 0 in the bulk (Meissner state):
      Z_sc ≈ Z₀ at the boundary, but the phase-locked bulk has
      effectively Z → 0 → Γ → −1 (total reflection).

    When B_applied → B_c (type-II mixed state or transition):
      Z_sc → 0 → Γ → −1.

    In the normal state (B > B_c): μ_eff = μ₀ → Z_sc = Z₀ → Γ = 0.

    This is the SAME ``reflection_coefficient()`` used for:
      - Pauli exclusion (particle confinement: Γ → −1)
      - PONDER-01 antenna port S₁₁
      - Seismic Moho reflections

    Args:
        B_applied: Applied magnetic field at the boundary [T].
        B_critical: Critical field [T].

    Returns:
        Reflection coefficient (dimensionless, −1 ≤ Γ ≤ 0).
    """
    Z_sc = superconducting_impedance(B_applied, B_critical)
    return reflection_coefficient(Z_0, Z_sc)


# ═══════════════════════════════════════════════════════════════
# London penetration depth — the magnetic analog of skin depth
# ═══════════════════════════════════════════════════════════════


def london_penetration_depth(n_s: float, m_eff: float = M_E) -> float:
    r"""
    London penetration depth from superfluid density.

    .. math::
        \lambda_L = \sqrt{\frac{m^*}{\mu_0 \, n_s \, e^2}}

    This is the magnetic-sector dual of the plasma skin depth:
      δ_plasma = c / ω_p = √(m_e / (μ₀ n_e e²))  ← same formula!

    The field decays as B(x) = B₀·exp(−x/λ_L), exactly as derived
    in the manuscript from rotational inertia of the gear-train model.

    Args:
        n_s: Superfluid (Cooper pair) density [m⁻³].
        m_eff: Effective carrier mass [kg]. Default = m_e.
              For Cooper pairs, use 2·m_e.

    Returns:
        London penetration depth [m].
    """
    return np.sqrt(m_eff / (MU_0 * n_s * e_charge**2))


def coherence_length(v_F: float, delta_0: float) -> float:
    r"""
    BCS coherence length (Pippard).

    .. math::
        \xi_0 = \frac{\hbar \, v_F}{\pi \, \Delta_0}

    The coherence length is the spatial extent of a Cooper pair.
    In AVE terms, it is the minimum radius at which the phase-locked
    gear train can execute a smooth 2π rotation without tearing.

    Args:
        v_F: Fermi velocity [m/s].
        delta_0: Superconducting gap energy at T = 0 [J].

    Returns:
        Coherence length [m].
    """
    return HBAR * v_F / (np.pi * delta_0)


def ginzburg_landau_kappa(lambda_L: float, xi_0: float) -> float:
    r"""
    Ginzburg-Landau parameter κ = λ_L / ξ₀.

    κ < 1/√2: Type-I superconductor (complete Meissner).
    κ > 1/√2: Type-II superconductor (vortex lattice).

    In AVE: Type-I = uniform saturation (μ → 0 everywhere).
            Type-II = localized saturation vortices (μ → 0 in cores,
                      μ ≈ μ₀ between them).

    Args:
        lambda_L: London penetration depth [m].
        xi_0: Coherence length [m].

    Returns:
        Ginzburg-Landau parameter (dimensionless).
    """
    return lambda_L / xi_0


# ═══════════════════════════════════════════════════════════════
# Superconductor catalog
# ═══════════════════════════════════════════════════════════════


@dataclass
class SuperconductorProperties:
    """Properties of a superconducting material."""

    name: str
    T_c: float  # Critical temperature [K]
    B_c0: float  # Critical field at T = 0 [T]
    n_s: float  # Superfluid density [m⁻³]
    lambda_L_0: float  # London depth at T = 0 [m]
    type: str = "I"  # "I" or "II"

    def critical_field_at(self, T: float) -> float:
        """B_c(T) = B_c0 · saturation_factor(T, T_c)."""
        return critical_field(T, self.T_c, self.B_c0)

    def mu_eff_at(self, B: float, T: float) -> float:
        """Effective μ at given B and T."""
        B_c = self.critical_field_at(T)
        if B_c <= 0:
            return MU_0  # Normal state
        return meissner_mu_eff(B, B_c)

    def impedance_at(self, B: float, T: float) -> float:
        """Z at given B and T."""
        B_c = self.critical_field_at(T)
        if B_c <= 0:
            return Z_0  # Normal state
        return superconducting_impedance(B, B_c)

    def reflection_at(self, B: float, T: float) -> float:
        """Γ at given B and T."""
        B_c = self.critical_field_at(T)
        if B_c <= 0:
            return 0.0  # Normal state — matched
        return meissner_reflection(B, B_c)


# Common superconductors
SC_CATALOG = {
    "Aluminium": SuperconductorProperties(
        name="Aluminium",
        T_c=1.18,
        B_c0=0.0105,  # 10.5 mT
        n_s=1.81e29,  # from n_e of Al
        lambda_L_0=50e-9,  # ~50 nm
        type="I",
    ),
    "Lead": SuperconductorProperties(
        name="Lead",
        T_c=7.19,
        B_c0=0.0803,  # 80.3 mT
        n_s=1.32e29,
        lambda_L_0=37e-9,
        type="I",
    ),
    "Niobium": SuperconductorProperties(
        name="Niobium",
        T_c=9.25,
        B_c0=0.206,  # 206 mT (upper B_c2 is higher)
        n_s=5.56e28,
        lambda_L_0=39e-9,
        type="II",
    ),
    "YBCO": SuperconductorProperties(
        name="YBCO (YBa₂Cu₃O₇)",
        T_c=92.0,
        B_c0=100.0,  # ~100 T (B_c2)
        n_s=2e27,
        lambda_L_0=150e-9,
        type="II",
    ),
    "MgB2": SuperconductorProperties(
        name="MgB₂",
        T_c=39.0,
        B_c0=16.0,  # ~16 T (B_c2)
        n_s=1.7e28,
        lambda_L_0=85e-9,
        type="II",
    ),
}
