import numpy as np
from ave.core.constants import C_0, M_E, e_charge, HBAR


def simulate_electron_interferometry_parallax(electron_energy_ev=100.0, baseline_m=1.0):
    """
    Simulates the Vol 2 Topological Matter Interferometry Parallax test.
    An electron matter-wave is split in a macroscopic Mach-Zehnder setup.
    Calculates the topological phase shift \u0394\u03A6 caused by Earth's
    Axiom 3 parity violation (n_spatial != n_temporal).
    """
    print("--- Vol 2 Topological Matter Interferometry Parallax ---")

    # Standard QM parameters
    energy_j = electron_energy_ev * e_charge
    velocity_m_s = np.sqrt(2 * energy_j / M_E)
    momentum_kg_m_s = M_E * velocity_m_s
    h_planck = HBAR * 2 * np.pi
    de_broglie_lambda = h_planck / momentum_kg_m_s

    print(f"Electron Energy: {electron_energy_ev} eV")
    print(f"Classical de Broglie Wavelength: {de_broglie_lambda * 1e9:.4f} nm")

    # Axiom 3 Earth Gravitational VSWR strain
    v_esc_m_s = 11.2e3
    eps_11 = 0.5 * (v_esc_m_s / C_0) ** 2

    # Parity anomaly \u0394n = n_spatial - n_temporal
    # n_s = (9/7)*eps_11, n_t = (2/7)*eps_11 => \u0394n = eps_11
    parity_anomaly_dn = eps_11
    print(f"Axiom 3 Parity Anomaly (\u0394n = n_s - n_t): {parity_anomaly_dn:.6e}")

    # Parallax Phase shift over the vertical baseline
    # \u0394\u03A6 = 2\u03C0 * (L * \u0394n) / \u03BB
    delta_phi_rad = 2 * np.pi * (baseline_m * parity_anomaly_dn) / de_broglie_lambda
    delta_phi_deg = np.degrees(delta_phi_rad)

    print(f"\nBaseline: {baseline_m} m vertical vs horizontal")
    print(f"=> Topological Parallax Shift (\u0394\u03A6): {delta_phi_rad:.4f} radians ({delta_phi_deg:.2f} deg)")

    if delta_phi_deg > 0.1:
        print(
            "RESULT: The parity breakdown is macroscopically resolvable. Probability conservation is strictly falsified by topological LC coupling."
        )
    else:
        print("RESULT: Phase shift is below standard detection resolution.")


if __name__ == "__main__":
    simulate_electron_interferometry_parallax()
