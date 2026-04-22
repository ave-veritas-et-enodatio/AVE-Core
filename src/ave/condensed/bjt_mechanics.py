"""
Bipolar Junction Transistor (BJT) Mechanics — AVE First Principles
==================================================================

Models NPN and PNP Transistors purely as dual-barrier Topo-Kinematic
Coupled Cavities. 

In classical physics, Current Gain (\beta or h_FE) is calculated using 
diffusion equations of minority carriers. In AVE, it is strictly the 
geometric ratio of the forward longitudinal transmission line (T^2) 
against the orthogonal recombination defect leakage (1 - T^2), 
integrated across the discrete number of alpha-cluster hops (N_gap).

Because Emitters are typically heavily doped (N_E+) compared to the 
Base (N_B-), their structural Avalanche Multipliers (Miller M) offset,
creating a deliberate topological impedance mismatch (Z_E != Z_B). This 
mismatch chokes T^2 off from perfect 1.000, forcing \beta into physically 
realistic bounds (~50 to 300) governed strictly by pure geometry.
"""

from __future__ import annotations


from ave.core.constants import ALPHA
from ave.nuclear.silicon_atom import V_R_OVER_V_BR, Z_SI
from ave.nuclear.boron_atom import Z_BORON
from ave.nuclear.phosphorus_atom import Z_PHOSPHORUS
from ave.condensed.silicon_crystal import K_SI_SI


def compute_asymmetric_impedance(dopant_Z: float, doping_weight: float) -> float:
    """
    Computes the localized nodal impedance by scaling the structural matrix.
    Heavy doping physically pulls the geometric multiplier deeper into avalanche.
    """
    # Weight simulates N_D relative concentrations geometrically
    V_R_ratio = V_R_OVER_V_BR * (dopant_Z / Z_SI) * doping_weight

    # Miller Multiplier structurally loads the matrix
    # Bound the ratio to prevent singularity if heavily forced
    if V_R_ratio >= 1.0:
        V_R_ratio = 0.9999

    M = 1.0 / (1.0 - V_R_ratio**5)

    if dopant_Z < Z_SI:  # Acceptor (Void creates structural pull)
        k_eff = K_SI_SI / M
    else:  # Donor (Surplus creates structural push)
        k_eff = K_SI_SI * M

    # Impedance maps inversely to effective coupling
    return 1.0 / (1.0 + k_eff)


def bjt_current_gain(N_gap_hops: int = 1, emitter_doping_ratio: float = 1.5) -> dict:
    """
    Derives the BJT Current Gain purely from macroscopic transmission limits.

    Args:
        N_gap_hops: The topological width of the Base counted in discrete matrices.
        emitter_doping_ratio: Relative structural density of Emitter vs Base (N_E/N_B).
                              Normally emitters are heavily doped (1.5x -> 10x) vs the base.
    """
    # NPN Configuration
    # Emitter: Phosphorus heavily doped
    # Base: Boron lightly doped

    Z_E = compute_asymmetric_impedance(Z_PHOSPHORUS, doping_weight=emitter_doping_ratio)
    Z_B = compute_asymmetric_impedance(Z_BORON, doping_weight=1.0)

    # The Emitter-Base Transmission Boundary (T_{EB}^2)
    # 4*Z1*Z2 / (Z1+Z2)^2
    T_sq_EB = (4.0 * Z_E * Z_B) / (Z_E + Z_B) ** 2

    # The continuous surviving Forward wave across N matrix gaps
    alpha = (T_sq_EB) ** N_gap_hops

    # Common-Emitter Gain (beta) = Transfer / Recombine
    beta = alpha / (1.0 - alpha) if alpha < 1.0 else float("inf")

    return {
        "Z_Emitter": Z_E,
        "Z_Base": Z_B,
        "T_sq_EB": T_sq_EB,
        "Alpha_common_base": alpha,
        "Beta_common_emitter": beta,
        "N_gap_multiplier": N_gap_hops,
        "Emitter_Doping_Ratio": emitter_doping_ratio,
    }


if __name__ == "__main__":
    res = bjt_current_gain()
    print("Default NPN BJT Topo-Kinematic Derivation:")
    print(f" T_sq EB: {res['T_sq_EB']:.6f}")
    print(f" Gain (Beta): {res['Beta_common_emitter']:.2f}")
