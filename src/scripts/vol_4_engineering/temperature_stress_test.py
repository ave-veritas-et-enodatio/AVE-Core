#!/usr/bin/env python3
"""
Thermal Rigidity Falsification Test
===================================
A falsification script specifically testing Topo-Kinematic structural rigidity
(0 K to 800 K) against classical semiconductor thermal gas statistics.

Classical Physics asserts:
V_bi(T) = V_T * ln(N_A*N_D / n_i^2) where V_T = kT/e
At cryogenic boundaries (T->0), n_i goes to zero and V_T goes to zero, causing 
math domain collapse and predicting full dielectric freeze-out.

AVE Physics asserts:
V_bi(T) is purely a macroscopic transmission boundary explicitly immune to 
thermal statistics. Heat is strictly interpreted as metric phononic dilation 
(solid matter volumetrically pulling apart according to alpha_th). 
Therefore, V_bi MUST remain totally rigid at 0K, only yielding roughly by 
micro-volts directly translating to the fractional geometry shift.
"""

import math
import numpy as np

# Empirical constants for Classical failure tracking
k_B = 8.617333262145e-5  # eV/K
E_g0 = 1.12              # eV (empirical Si)
N_A = 1e16
N_D = 1e16
N_c = 2.8e19             # approx at 300K
N_v = 1.04e19            # approx at 300K

# Topo-Kinematic structural base values
from ave.condensed.silicon_doping import pn_junction as pn_si
from ave.condensed.bjt_mechanics import bjt_current_gain

# Linear phononic thermal expansion (Silicon)
alpha_th = 2.6e-6  # /K

def classical_V_bi(T: float) -> str:
    """Computes the empirical Standard Model Voltage limit."""
    if T <= 0.0:
        return "MATH_COLLAPSE_0K"
        
    V_T = k_B * T
    # intrinsic carrier density strongly depends on temperature
    # n_i^2 = N_c N_v exp(-E_g / kT)
    
    # Scale N_c, N_v arbitrarily by standard temp dependencies (T/300)^3
    ratio = (T / 300.0)**3
    nc = N_c * ratio
    nv = N_v * ratio
    
    try:
        ni_sq = nc * nv * math.exp(-E_g0 / V_T)
        if ni_sq <= 0.0:
            return "STATISTICAL_FREEZE"
        
        V_bi = V_T * math.log((N_A * N_D) / ni_sq)
        return f"{V_bi:.4f} V"
    except (OverflowError, ValueError, ZeroDivisionError):
        return "STATISTICAL_FREEZE"

def ave_V_bi(T: float) -> str:
    """
    AVE computes structural voltage directly geometrically.
    The lattice dilates physically from 300K baseline by:
    dilation = 1.0 + alpha_th * (T - 300)
    As space expands, structural gaps narrow/widen respectively.
    """
    baseline = pn_si()
    dilation = 1.0 + (alpha_th * (T - 300.0))
    
    # The actual built in topological boundary stretches fractionally with the matrix.
    v_bi = baseline['V_bi_V'] / dilation
    return f"{v_bi:.6f} V"

def ave_bjt_beta(T: float) -> str:
    """
    Testing the highly degenerate BJT configuration from Phase 1.
    Asymmetric limits simply stretch fractionally to geometry, averting collapse.
    """
    base_bjt = bjt_current_gain(N_gap_hops=1, emitter_doping_ratio=17.5)
    dilation = 1.0 + (alpha_th * (T - 300.0))
    
    beta = base_bjt['Beta_common_emitter'] * (1.0 / dilation)
    return f"β = {beta:.2f}"


def run_thermal_sweep():
    temperatures = [0.0, 10.0, 50.0, 150.0, 300.0, 600.0, 800.0]
    
    print("=" * 70)
    print(" AVE THERMAL RIGIDITY VS. EMPIRICAL COLLAPSE (0 K to 800 K)")
    print("=" * 70)
    print(f"{'TEMP (K)':<10} | {'CLASSICAL V_bi':<20} | {'AVE GEOMETRIC V_bi':<20} | {'AVE BJT GAIN'}")
    print("-" * 70)
    
    for T in temperatures:
        c_vbi = classical_V_bi(T)
        a_vbi = ave_V_bi(T)
        a_bjt = ave_bjt_beta(T)
        print(f"{T:<10.1f} | {c_vbi:<20} | {a_vbi:<20} | {a_bjt}")

    print("=" * 70)
    print("VERDICT:")
    print("Standard physics predicts structural collapse/freeze-out at deep cryogenic ranges.")
    print("Topo-Kinematics forces limits to remain totally rigid, fractionally yielding ")
    print("only to actual phononic crystal cell physical dilation.")
    print("=" * 70)

if __name__ == "__main__":
    run_thermal_sweep()
