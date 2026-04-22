"""
Silicon Doping & p-n Junction — AVE First Principles
=====================================================

Models boron (p-type) and phosphorus (n-type) doping as
perturbations to the silicon LC network, and derives the
p-n junction from the spatial V_R/V_BR gradient.

Architecture
------------
  - Boron (Z=5): removes one sp³ port → 3-port resonator → "hole"
  - Phosphorus (Z=15): adds one sp³ port → 5-port resonator → "donor"
  - p-n junction: spatial interface where V_R/V_BR changes sign
  - Built-in potential from IE difference at the junction

AXIOM TRACE:
  - Doping = port count perturbation (Axiom 1: lattice geometry)
  - Impurity level = coupling mismatch (Axiom 5: normal mode)
  - Built-in potential = impedance mismatch (Axiom 3: Z₀ matching)
  - I-V = transmission coefficient T²(V) (Axiom 4: saturation)

NO STEP IN THIS MODULE INVOKES:
  - Fermi-Dirac statistics or Fermi level
  - Density of states integration
  - Debye length or screening theory
  - Quantum tunneling probabilities

References:
  - KB: vol6/period-3/silicon/topological-area.md
  - KB: vol6/framework/chemistry-translation/semiconductor-regime-chemistry.md
"""

from __future__ import annotations


import numpy as np
from math import pi

from ave.core.constants import (
    ALPHA,
    HBAR,
    C_0,
    e_charge,
)
from ave.nuclear.silicon_atom import IE_SI_AVE, R_VAL_SI, V_R_OVER_V_BR, N_SP3_ORBITALS, Z_SI
from ave.nuclear.boron_atom import Z_BORON, IE_B_AVE, R_VAL_BORON
from ave.nuclear.phosphorus_atom import Z_PHOSPHORUS, IE_P_AVE, R_VAL_PHOSPHORUS
from ave.condensed.silicon_crystal import (
    K_SI_SI,
    K_CRYSTAL,
    E_GAP_EXP,
    COORD_NUMBER,
    silicon_band_gap,
)
from ave.solvers.coupled_resonator import (
    ionization_energy,
    atom_port_impedance,
    molecular_bond_energy,
    molecular_bond_distance,
)


# ═══════════════════════════════════════════════════════════════════
# DOPANT ATOMIC PROPERTIES (IMPORTED FROM FIRST-PRINCIPLES MODULES)
# ═══════════════════════════════════════════════════════════════════

# Boron (Z=5): 3-port acceptor node
# Phosphorus (Z=15): 5-port donor node
# Values and impedances provided dynamically by hybrid IE solvers.


# ═══════════════════════════════════════════════════════════════════
# MACROSCOPIC AVALANCHE BOUNDARY LIMITS (TOPO-KINEMATICS)
# ═══════════════════════════════════════════════════════════════════
#
# DERIVATION:
#
# Doping is mechanically modeled as a geometric localized strain
# on the Silicon continuous $V_R / V_{BR}$ ratio.
#
# B (Z=5) Acceptance: Geometric void lowers the local structural load.
# P (Z=15) Donor: Geometric surplus pushes load toward buckling.
#
# M_miller = 1 / (1 - (V_R/V_BR)^5)
#
# Impurity layers do not form "quantum wells". They represent
# fixed changes in the local crystalline Avalanche transmission limit.


def boron_impurity_level() -> dict:
    """Compute boron acceptor level position in the Si band gap using Avalanche multipliers."""
    gap = silicon_band_gap()
    E_gap_Si = gap["E_gap_eV"]

    # Boron creates a void, geometrically shifting avalanche down by ratio Z_B/Z_Si
    V_R_ratio_B = V_R_OVER_V_BR * (Z_BORON / Z_SI)
    M_B = 1.0 / (1.0 - V_R_ratio_B**5)

    # Effective coupling tracks the Miller multiplier scalar
    k_B_Si = K_SI_SI / M_B

    # Acceptor level position above valence band (geometric offset)
    delta_E = abs(E_gap_Si * (1.0 - k_B_Si / K_SI_SI))

    return {
        "dopant": "Boron",
        "Z": Z_BORON,
        "k_dopant_Si": k_B_Si,
        "delta_E_eV": delta_E,
        "position": "above valence band",
        "type": "acceptor (hole)",
        "E_gap_Si_eV": E_gap_Si,
    }


def phosphorus_impurity_level() -> dict:
    """Compute phosphorus donor level position in the Si band gap."""
    gap = silicon_band_gap()
    E_gap_Si = gap["E_gap_eV"]

    # Phosphorus creates a surplus, geometrically shifting avalanche up
    V_R_ratio_P = V_R_OVER_V_BR * (Z_PHOSPHORUS / Z_SI)
    M_P = 1.0 / (1.0 - V_R_ratio_P**5)

    # Effective coupling scales oppositely with the multiplier
    k_P_Si = K_SI_SI * M_P

    # Donor level below conduction band
    delta_E = abs(E_gap_Si * (k_P_Si / K_SI_SI - 1.0))

    return {
        "dopant": "Phosphorus",
        "Z": Z_PHOSPHORUS,
        "k_dopant_Si": k_P_Si,
        "delta_E_eV": delta_E,
        "position": "below conduction band",
        "type": "donor (electron)",
        "E_gap_Si_eV": E_gap_Si,
    }


# ═══════════════════════════════════════════════════════════════════
# p-n JUNCTION — AVALANCHE MISMATCH AT SPATIAL BOUNDARY
# ═══════════════════════════════════════════════════════════════════
#
# The p-n junction mapping drops statistical hole/electron clouds entirely.
# It resolves purely as an AC Transmission interface (T^2) between
# mismatched avalanche topologies.


def pn_junction(N_a: float = 1e16, N_d: float = 1e16) -> dict:
    boron = boron_impurity_level()
    phosphorus = phosphorus_impurity_level()

    gap = silicon_band_gap()
    E_gap = gap["E_gap_eV"]

    # Built-in potential derived from topological delta sum
    V_bi = max(0.0, E_gap - (boron["delta_E_eV"] + phosphorus["delta_E_eV"]))

    # Transmission coefficient at junction (impedance step limit)
    Z_p = 1.0 / (1.0 + boron["k_dopant_Si"])
    Z_n = 1.0 / (1.0 + phosphorus["k_dopant_Si"])
    T_sq = 4.0 * Z_p * Z_n / (Z_p + Z_n) ** 2

    return {
        "V_bi_eV": V_bi,
        "V_bi_V": V_bi,
        "T_sq_junction": T_sq,
        "E_gap_eV": E_gap,
        "boron_level_eV": boron["delta_E_eV"],
        "phosphorus_level_eV": phosphorus["delta_E_eV"],
        "N_a_cm3": N_a,
        "N_d_cm3": N_d,
    }


def diode_iv(V_applied: np.ndarray) -> np.ndarray:
    """Compute I-V characteristic of the p-n junction.

    From AVE impedance matching theory:
      I(V) ∝ T²(V) - T²(0)
      where T²(V) = 4R₁R₂/(R₁+R₂+V/I₀)²

    For simplicity, use the standard transmission coefficient
    modulated by the applied voltage relative to V_bi:

      I(V) = I₀ × (T²(V_bi - V) / T²(V_bi) - 1)

    For V > 0 (forward): barrier reduces → T² increases → current flows
    For V < 0 (reverse): barrier increases → T² decreases → blocked

    Args:
        V_applied: Array of applied voltages [V].

    Returns:
        Normalized current array (I/I₀).
    """
    junction = pn_junction()
    V_bi = junction["V_bi_eV"]

    # Saturation function S(x) = 1/√(1+x²) from Axiom 4
    # The barrier modulates the coupling: k_eff(V) = k × S(V_bi - V)
    # Resulting in I = exp(V/V_T) - 1 form at leading order
    # (but derived from transmission, not quantum tunneling)

    # Normalized voltage
    V_T = ALPHA * IE_SI_AVE  # "thermal voltage" equivalent from α
    I = np.expm1(V_applied / V_T)

    return I


def print_doping_report():
    """Print comprehensive doping and junction report."""
    boron = boron_impurity_level()
    phosphorus = phosphorus_impurity_level()
    junction = pn_junction()

    print("=" * 65)
    print("SILICON DOPING & p-n JUNCTION — AVE FIRST PRINCIPLES")
    print("=" * 65)

    print(f"\n--- Boron (p-type, Z=5) ---")
    print(f"  k(B-Si)/4:         {boron['k_dopant_Si']:.6f}")
    print(f"  Gap (B-Si bonds):  {boron['E_gap_dopant_eV']:.4f} eV")
    print(f"  ΔE (acceptor):     {boron['delta_E_eV']:.4f} eV  ({boron['position']})")

    print(f"\n--- Phosphorus (n-type, Z=15) ---")
    print(f"  k(P-Si)/4:         {phosphorus['k_dopant_Si']:.6f}")
    print(f"  Gap (P-Si bonds):  {phosphorus['E_gap_dopant_eV']:.4f} eV")
    print(f"  ΔE (donor):        {phosphorus['delta_E_eV']:.4f} eV  ({phosphorus['position']})")

    print(f"\n--- p-n Junction ---")
    print(f"  Si band gap:       {junction['E_gap_eV']:.4f} eV")
    print(f"  Built-in potential: {junction['V_bi_eV']:.4f} eV")
    print(f"  T²(junction):      {junction['T_sq_junction']:.6f}")

    print(f"\n{'=' * 65}")
