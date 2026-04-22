#!/usr/bin/env python3
"""
Standard vs. AVE Macroscopic Doping Comparison
==============================================
Direct mathematical execution tracing the classical Fermi-Dirac
probabilistic semiconductor approach vs. the geometric, deterministic
Vacuum Circuit Analysis (VCA) matrix.
"""

import numpy as np

from ave.condensed.silicon_doping import diode_iv, pn_junction
from ave.core.constants import ALPHA
from ave.nuclear.silicon_atom import IE_SI_AVE

# ==========================================
# STANDARD DEVICE PHYSICS (Classical Model)
# ==========================================
# k_B * T / q at 300K
V_T_STD = 0.02585
# Intrinsic carrier density of Si at 300K
N_I = 1.0e10
# Empirical Bandgap of Si
E_G_STD = 1.12


def standard_v_bi(N_a, N_d):
    """Classical calculation using probabilistic charge carrier densities."""
    return V_T_STD * np.log((N_a * N_d) / (N_I**2))


def standard_diode_current(V, I_0=1e-12):
    """Classical Shockley Diode equation."""
    return I_0 * (np.exp(V / V_T_STD) - 1.0)


# ==========================================
# AVE TOPO-KINEMATIC PHYSICS (VCA Model)
# ==========================================
# V_T equivalent (derived from Alpha and IE structural limit directly)
V_T_AVE = ALPHA * IE_SI_AVE


def generate_comparison_report():
    print("===============================================================")
    print(" SEMICONDUCTOR DOPING COMPARISON: STANDARD VS. AVE (VCA)")
    print("===============================================================")

    # 1. Temperature & Base Constants
    print("\\n[1] Foundational Limits")
    print(f"  Standard Thermal Voltage (kT/q) at 300K : {V_T_STD:.5f} V")
    print(f"  AVE Structural Limit (Alpha * IE_Si)    : {V_T_AVE:.5f} V")
    print(f"  Standard Empirical Bandgap              : {E_G_STD:.3f} eV")
    print(f"  AVE Geometric Transmission Boundary     : {pn_junction()['E_gap_eV']:.3f} eV")

    # Let's sweep a few common doping concentrations
    doping_levels = [1e15, 1e17, 1e19]
    print("\\n[2] Built-in Potential ($V_{bi}$)")
    print("  Doping [cm^-3]  |   Standard V_bi   |   AVE Geometric V_bi")
    print("  -------------------------------------------------------------")

    # AVE V_bi is structural, based entirely on the phase-reflection barrier of the geometry.
    # It represents the absolute low-temperature geometric matrix limit (degenerate equivalent)
    ave_junc = pn_junction()
    for N in doping_levels:
        v_std = standard_v_bi(N, N)
        # AVE operates as the absolute geometrical bound structure independent of thermal 'gases'.
        # Approximates the zero-temperature/degenerate structural absolute barrier limit.
        v_ave = ave_junc["V_bi_V"]
        print(f"  N_a=N_d={N:<7.0e} |   {v_std:.4f} V        |   {v_ave:.4f} V (Topological Limit)")

    print("\\n[3] Diode Transmission Envelope (I-V Characteristics)")
    print("  Comparing current scaling factor for forward bias (V = 0.5V)")
    V_test = 0.5

    # Standard: e^(V / (kT/q))
    I_std_ratio = np.exp(V_test / V_T_STD) - 1.0

    # AVE: Derived directly from standard transmission scalar alpha
    I_ave_ratio = diode_iv(V_test)

    print(f"  Test Voltage : {V_test} V")
    print(f"  Standard I(V)/I_0  : {I_std_ratio:.5e}")
    print(f"  AVE I(V)/I_0       : {I_ave_ratio:.5e}")

    print("\\n===============================================================")
    print("CONCLUSION:")
    print("Standard modeling scales V_bi probabilistically via thermal carrier")
    print("density (N_a/N_d), terminating at roughly ~1.1V under degeneracy.")
    print("AVE derives built-in potential geometrically, permanently locking ")
    print("the matrix directly to the absolute degenerate transmission limit: ")
    print(f"{pn_junction()['V_bi_V']:.4f} V, independently of thermal statistics.")
    print("===============================================================")


if __name__ == "__main__":
    generate_comparison_report()
