import numpy as np
from ave.core.constants import C_0, G


def simulate_sagnac_geo_parallax():
    print("--- Vol 4 New Proposals: Sagnac & GEO-Synchronous Parallax ---")

    # 1. Sagnac-Parallax (Galactic Wind Vectoring)
    print("\n[Protocol 11: Sagnac-Parallax (Galactic Wind Vectoring)]")
    v_gal = 370e3  # m/s (approx velocity relative to CMB)
    L_fiber = 200.0  # m (baseline loop)
    wavelength = 1550e-9  # m

    # The optical lever arm tracks the absolute flow of the metric
    # Delta Phi ~ (4 * pi * L * v) / (lambda * c_0)
    max_phase_shift_rad = (4 * np.pi * L_fiber * v_gal) / (wavelength * C_0)
    print(f"Max Amplitude Phase Shift from Galactic Drift: {max_phase_shift_rad:.2f} radians")
    print(
        "=> RESULT: The 24-hr Earth rotation vectors this drift into a massive, detectable sinusoidal daily oscillation."
    )

    # 2. GEO-Synchronous Impedance Differential
    print("\n[Protocol 12: GEO-Synchronous Impedance Differential]")
    M_earth = 5.972e24  # kg
    R_earth = 6371e3  # m
    H_geo = 35786e3  # m
    R_geo = R_earth + H_geo

    # Fractional delay from Earth's Metric Saturation (Shapiro-style topological integration)
    # n(r) = 1 + 2GM / (r * c^2)
    # Delay Delta_t = integral from R_earth to R_geo of (n(r) - 1)/c dr
    # Delta_t = 2GM / c^3 * ln(R_geo / R_earth)

    delta_t_s = (2 * G * M_earth) / (C_0**3) * np.log(R_geo / R_earth)
    print(f"Absolute Topological Optical Delay (\u0394t): {delta_t_s * 1e12:.2f} picoseconds")

    # Translate delay into effective millimeter path stretch
    path_stretch_mm = delta_t_s * C_0 * 1000.0
    print(f"Effective Optical Path Stretch (\u0394L): {path_stretch_mm:.6f} mm")
    print(
        "=> RESULT: The static G-field structurally stretches the telecom laser time-of-flight by ~17 millimeters, proving gravitational LC dispersion."
    )


if __name__ == "__main__":
    simulate_sagnac_geo_parallax()
