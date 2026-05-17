"""
Vol 2 Topological Matter Interferometry Parallax (C11-MACH-ZEHNDER driver).

SCOPE NOTE (2026-05-17 audit): Prior version of this script computed
eps_11 = 0.5 * (v_esc/C_0)**2 = phi/c^2 (Newtonian potential). This was
NON-CANONICAL — the AVE engine's canonical strain field is

    eps_11(r) = 7 * G * M / (c^2 * r) = 7 * phi(r)

per `ave.gravity.principal_radial_strain` (canonical function) and the
single-source derivation at `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-
relativity/gordon-optical-metric.md:16-29`. The factor 7 comes from the K4
Poisson ratio nu_vac = 2/7 + the Machian impedance limit T_max,g = c^4/(7G);
it is UNIVERSAL across all scales (BH horizon to weak field).

Prior driver-script form was factor-7 LOW. This produced a 35-rad Mach-Zehnder
phase-shift prediction, which the C11 matrix row inherited. The canonical
prediction is ~250 rad (factor 7 larger; easier to detect, not harder).

This script now imports `principal_radial_strain` from the canonical engine
instead of hard-coding the Newtonian-potential form. See:
- `src/ave/gravity/__init__.py:23-41` for the canonical function
- `manuscript/ave-kb/common/closure-roadmap.md` §0.5 for the 2026-05-17 factor-7
  cleanup changelog entry
- `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-
  standing-wave.md:51` for the C11 source leaf (notation parallelism cleanup
  also landed)
"""

import numpy as np

from ave.core.constants import C_0, HBAR, M_E, e_charge
from ave.gravity import principal_radial_strain


# Earth canonical parameters
M_EARTH_KG = 5.972e24
R_EARTH_M = 6.371e6


def simulate_electron_interferometry_parallax(electron_energy_ev: float = 100.0, baseline_m: float = 1.0) -> None:
    """
    Simulates the Vol 2 Topological Matter Interferometry Parallax test.
    An electron matter-wave is split in a macroscopic Mach-Zehnder setup.
    Calculates the topological phase shift Delta-Phi caused by Earth's
    Axiom 3 parity violation (n_spatial != n_temporal).
    """
    print("--- Vol 2 Topological Matter Interferometry Parallax (C11-MACH-ZEHNDER) ---")
    print("(Driver corrected 2026-05-17: now uses canonical eps_11 = 7GM/c^2 r from ave.gravity)")

    # Standard QM parameters
    energy_j = electron_energy_ev * e_charge
    velocity_m_s = np.sqrt(2 * energy_j / M_E)
    momentum_kg_m_s = M_E * velocity_m_s
    h_planck = HBAR * 2 * np.pi
    de_broglie_lambda = h_planck / momentum_kg_m_s

    print(f"Electron Energy: {electron_energy_ev} eV")
    print(f"Classical de Broglie Wavelength: {de_broglie_lambda * 1e9:.4f} nm")

    # Canonical AVE Earth gravitational strain (universal factor 7 from nu_vac + Machian limit)
    eps_11 = principal_radial_strain(M_EARTH_KG, R_EARTH_M)
    print(f"Earth eps_11 (canonical, 7GM/c^2 R): {eps_11:.6e}")
    print(f"  (compare: naive Newtonian phi/c^2 = {0.5 * (11.2e3 / C_0) ** 2:.6e}, factor 7 low)")

    # Parity anomaly: Delta_n = n_spatial - n_temporal
    # Canonical forms (both with implicit "1 +"):
    #   n_s = 1 + (9/7) * eps_11
    #   n_t = 1 + (2/7) * eps_11
    # => Delta_n = (7/7) * eps_11 = eps_11
    parity_anomaly_dn = eps_11
    print(f"Axiom 3 Parity Anomaly (Delta_n = n_s - n_t = eps_11): {parity_anomaly_dn:.6e}")

    # Parallax Phase shift over the vertical baseline
    # Delta_Phi = 2*pi * (L * Delta_n) / lambda_dB
    delta_phi_rad = 2 * np.pi * (baseline_m * parity_anomaly_dn) / de_broglie_lambda
    delta_phi_deg = np.degrees(delta_phi_rad)

    print(f"\nBaseline: {baseline_m} m vertical vs horizontal")
    print(f"=> Topological Parallax Shift (Delta_Phi): {delta_phi_rad:.4f} radians ({delta_phi_deg:.2f} deg)")

    if delta_phi_deg > 0.1:
        print(
            "RESULT: Parity violation predicted at macroscopically resolvable magnitude."
            " Discriminates AVE Axiom 3 from Lorentz-invariant QM if observed at this magnitude."
        )
    else:
        print("RESULT: Phase shift is below standard detection resolution.")


if __name__ == "__main__":
    simulate_electron_interferometry_parallax()
