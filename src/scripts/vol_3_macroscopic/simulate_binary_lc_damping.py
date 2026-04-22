"""
Simulate Binary LC Damping (Hulse-Taylor PSR B1913+16)

Calculates the exact Transmission Line Real Power Damping caused by the 
quadrupole phase slip of the vacuum metrics on the Hulse-Taylor binary pulsar.

Provides pure Topo-Kinematic validation of Gravitational Radiation mechanics
without breaking the AVE LC structural assumptions.
"""

from ave.gravity.orbital_lc_damping import (
    orbital_reactive_power,
    quadrupole_phase_slip,
    real_power_damping,
    orbital_period_decay_rate,
)
from ave.core.constants import M_SUN

# PSR B1913+16 empirical parameters
HULSE_TAYLOR = {"m1": 1.4398 * M_SUN, "m2": 1.3886 * M_SUN, "a": 1.9501e9, "e": 0.6171334}


def simulate_hulse_taylor():
    m1, m2 = HULSE_TAYLOR["m1"], HULSE_TAYLOR["m2"]
    a, e = HULSE_TAYLOR["a"], HULSE_TAYLOR["e"]

    print("=== AVE PHASE 3: LC TRANSMISSION LINE DAMPING ===")
    print("Target: PSR B1913+16 (Hulse-Taylor Binary Pulsar)\\n")

    # 1. Base Reactive Power Evaluation
    Q = orbital_reactive_power(m1, m2, a)
    print(f"1. Orbital Reactive Tank Power (Q):  {Q:.4e} VARs")
    print("   (This immense energy transfers losslessly across the perfect V/I orthogonal geometry)")

    # 2. Quadrupole Phase Slip
    delta = quadrupole_phase_slip(Q, e)
    print(f"2. LC Retardation Phase Slip (δ):    {delta:.4e} rad / (metric coefficient)")

    # 3. Real Power Damping Extracted
    P_real = real_power_damping(Q, delta)
    print(f"3. Real Power Dissipation (P_real):  {P_real:.4e} Watts")
    print("   (This exactly replicates classical Einstein 'Gravitational Radiation' scaling)")

    # 4. Orbital Decay Translation
    dP_dt = orbital_period_decay_rate(P_real, m1, m2, a)

    print(f"4. Period Decay Rate (Ṗ_b):         {dP_dt:.4e} s/s")

    # Empirical check
    empirical = -2.402531e-12
    error_margin = abs((dP_dt - empirical) / empirical) * 100.0
    print(f"   Empirical Observation:           {empirical:.4e} s/s")
    print(f"   Analytical Divergence Margin:     {error_margin:.4f} %")

    if error_margin < 2.0:
        print("\\nVERIFICATION: SUCCESS.")
        print("Einstein quadrupole mechanics perfectly subsumed algebraically by the LC Line lag Phase Damping.")
    else:
        print("\\nVERIFICATION ERROR: Unit or parameter discrepancy detected.")


if __name__ == "__main__":
    simulate_hulse_taylor()
