"""
Tabletop Ferromagnetic Bullet Cluster Analogue Design.
Derives the physical lab requirements (Magnetic field, viscous scaling) bridging 
the cosmological Vacuum H_INFINITY bound to a tabletop ferrofluid container.
"""

import sys
import os
import numpy as np

# Ensure local ave package is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from ave.core.constants import MU_0
from ave.regime_3_saturated.galactic_rotation import A0_LATTICE


def design_tabletop_ferrofluid():
    """
    Calculates the exact Electromechanical requirements for a physical lab replication
    of the Bullet Cluster Dark Matter offset.
    """
    # 1. Fundamental Cosmological Metric
    print("=" * 60)
    print("AVE TABLETOP FALSIfICATION: FERROMAGNETIC VISCOSITY")
    print("=" * 60)
    print(f"Cosmological Yield Limit (a_0): {A0_LATTICE:.3e} m/s^2")

    # 2. Lab Ferrofluid Characteristics (Standard Ferrotec EFH1 Equivalent)
    # The ferrofluid structurally replaces the Vacuum LC Lattice
    fluid_mu_initial = 400.0  # Dense magnetic permeability
    fluid_B_sat = 0.044  # Saturation Magnetization in Tesla (440 Gauss)

    print("\n[Stator] Ferrofluid Lattice Characteristics:")
    print(f" - Base Magnetic Permeability (mu_r): {fluid_mu_initial}")
    print(f" - Structural Yield Limit (B_sat): {fluid_B_sat:.4f} Tesla")

    # 3. Scaling the Phenomenon
    # The physical radius from the magnetic core where B exactly equals B_sat
    # defines the Absolute Saturated Core (The equivalent of the stalled Gas core)
    # B(r) = (mu_0 * mu_r * m) / (4 * pi * r^3)
    # We want a manageable tabletop demonstration, say a 5cm saturation radius.
    target_r_sat = 0.05  # 5 centimeters

    # Required Magnetic Dipole Moment (m) of the spinning electromagnetic ball
    # m = B_sat * 4 * pi * r_sat^3 / (mu_0 * mu_initial)
    required_m_moment = fluid_B_sat * 4 * np.pi * (target_r_sat**3) / (MU_0 * fluid_mu_initial)

    print("\n[Rotor] Gyroscopic Electromagnet Requirements (Galaxy Cores):")
    print(f" - Target Saturation Radius (r_sat): {target_r_sat * 100:.1f} cm")
    print(f" - Required Internal Dipole Moment: {required_m_moment:.2f} A·m^2")

    # Physical Motor Core Specifications (assuming a 2cm radius internal coil)
    rotor_radius = 0.02  # 2 cm
    # m = N * I * A  ==>  N*I = m / (pi * r^2)
    ampere_turns = required_m_moment / (np.pi * (rotor_radius**2))

    print(f" - Required Coil Energization: {ampere_turns:.1f} Ampere-Turns")
    print("\nOPERATIONAL PREDICTION:")
    print("When two such spheres cross at high velocity while spinning laterally:")
    print("  1. The overlapping saturated boundaries (r < 5cm) will lock magnetically and mechanically shock.")
    print("  2. The extensive outer unsaturated B-fields (r > 5cm) will linearly superimpose and")
    print("     structurally shear the fluid independently, passing their viscous pressure wakes")
    print("     collsionlessly through each other, perfectly replicating the exact lensing offset")
    print("     of the Bullet Cluster without requiring invisible particulate matter.")
    print("=" * 60)


if __name__ == "__main__":
    design_tabletop_ferrofluid()
