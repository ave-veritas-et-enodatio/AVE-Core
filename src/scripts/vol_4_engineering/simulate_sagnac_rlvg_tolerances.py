"""
AVE Physical Predictions: Sagnac RLVG System Tolerances
======================================================
The AVE Kinematic and Electromagnetic Entrainment anomalies predict that 
the Sagnac phase shift depends on local rotor density, permeability, and ambient strain.
However, these deviations are exceedingly small (often on the order of 1e-9 to 1e-12 
radians depending on the physical tabletop setup).

To definitively isolate the AVE topological signature from standard experimental noise,
a Ring Laser Vacuum Gyroscope (RLVG) must be engineered with extreme precision. 

This script models the four most critical hardware tolerance noise floors:
1. THERMAL EXPANSION (Delta L / L): Changes in the geometric area of the ring.
2. LASER FREQUENCY STABILITY (Delta f / f): Wavelength drift causing phase jitter.
3. SEISMIC VIBRATION: Mechanical jitter coupling into the mirrors.
4. BACKSCATTER LOCK-IN / SHOT NOISE: The fundamental quantum measurement limit.

By simulating these noise sources, we establish the explicit "Signal-to-Noise Ratio (SNR)"
required to falsify or confirm the AVE Kinematic Entrainment Law.
"""

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import C_0, HBAR


project_root = pathlib.Path(__file__).parent.parent.parent.absolute()
# Target AVE Signal Amplitude (Estimate from Lead vs. Aluminum 1-meter RLG at 1000 RPM)
# The density difference generates a microscopic but steady phase offset.
AVE_TARGET_ANOMALY_PHASE = 1.5e-10  # Radians (Order of magnitude estimate for tabletop RLGs)

# Baseline RLVG Setup
RLV_RADIUS = 0.5  # Meters
RLV_PERIMETER = 2 * np.pi * RLV_RADIUS
RLV_AREA = np.pi * RLV_RADIUS**2
LASER_FREQ = 4.73e14  # Hz (HeNe Laser ~632.8 nm)
LASER_LAMBDA = C_0 / LASER_FREQ
OMEGA_TABLE = 100.0  # rad/s base rotation rate


def compute_thermal_noise(delta_temp_K, cte):
    """
    Delta Phi proportional to Delta Area.
    Area scales as length squared, so Delta A / A = 2 * (Delta L / L)
    Delta L / L = CTE * Delta T
    """
    fractional_area_change = 2.0 * cte * delta_temp_K
    base_sagnac = (4 * RLV_AREA * OMEGA_TABLE) / (LASER_LAMBDA * C_0)
    return base_sagnac * fractional_area_change


def compute_laser_drift_noise(delta_f_hz):
    """
    Delta Phi proportional to frequency f (since lambda = c/f).
    Delta Phi / Phi = Delta f / f
    """
    base_sagnac = (4 * RLV_AREA * OMEGA_TABLE) / (LASER_LAMBDA * C_0)
    fractional_f_change = delta_f_hz / LASER_FREQ
    return base_sagnac * fractional_f_change


def compute_shot_noise(power_watts, integration_time_s):
    """
    Fundamental quantum limit for interferometry.
    Delta Phi_shot ~ 1 / sqrt(N), where N is number of photons.
    N = (P * t) / (h * f)
    """
    h = HBAR * 2.0 * np.pi  # Planck's constant (J·s)
    photon_energy = h * LASER_FREQ
    num_photons = (power_watts * integration_time_s) / photon_energy
    return 1.0 / np.sqrt(max(1.0, num_photons))


def compute_seismic_noise(vibration_amp_m):
    """
    Mechanical mirror dither translates directly to path length uncertainty.
    Delta Phi_seismic = (2 * pi / lambda) * Delta L
    """
    return (2.0 * np.pi / LASER_LAMBDA) * vibration_amp_m


def run_tolerance_sweeps():
    print("[*] Initializing Sagnac RLVG System Tolerance Analyzer...")

    # 1. Thermal Sweep (Zerodur/ULE vs Quartz vs Aluminum)
    temps_mK = np.logspace(-3, 1, 100)  # 1 mK to 10 K temperature fluctuation
    cte_zerodur = 0.05e-6  # 0.05 ppm/K
    cte_quartz = 0.55e-6  # Fused Quartz 0.55 ppm/K
    cte_alum = 23.0e-6  # Aluminum 23 ppm/K

    thermal_z = [compute_thermal_noise(t, cte_zerodur) for t in temps_mK]
    thermal_q = [compute_thermal_noise(t, cte_quartz) for t in temps_mK]
    thermal_a = [compute_thermal_noise(t, cte_alum) for t in temps_mK]

    # 2. Laser Drift Wavelength Sweep (Linewidth stability)
    drifts_hz = np.logspace(0, 6, 100)  # 1 Hz to 1 MHz drift
    laser_noise = [compute_laser_drift_noise(f) for f in drifts_hz]

    # 3. Seismic Vibration Sweep
    vibes_m = np.logspace(-15, -9, 100)  # 1 fm to 1 nm displacement
    seismic_noise = [compute_seismic_noise(v) for v in vibes_m]

    # Plotting
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.patch.set_facecolor("#0f0f0f")

    for ax in axes:
        ax.set_facecolor("#0f0f0f")
        ax.grid(color="#333333", linestyle="--", alpha=0.5)
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")

        # Shade the "AVE Signal Detection Zone" (Everything above this line drowns out the AVE anomaly)
        ax.axhline(
            AVE_TARGET_ANOMALY_PHASE,
            color="#00ffcc",
            linestyle="-",
            lw=2,
            label="AVE Kinematic Signal Target",
        )
        ax.fill_between(
            [1e-15, 1e10],
            AVE_TARGET_ANOMALY_PHASE,
            1e0,
            color="red",
            alpha=0.1,
            label="Noise Drowns Signal",
        )
        ax.fill_between(
            [1e-15, 1e10],
            1e-15,
            AVE_TARGET_ANOMALY_PHASE,
            color="green",
            alpha=0.1,
            label="Clean Detection Zone",
        )

        for spine in ax.spines.values():
            spine.set_edgecolor("#555555")

    fig.suptitle(
        "RLVG Experimental System Tolerances to Isolate the AVE Sagnac Anomaly",
        color="#ffcc00",
        fontsize=16,
    )

    # Panel 1: Thermal
    ax1 = axes[0]
    ax1.plot(temps_mK, thermal_z, color="#66ccff", lw=2, label="Zerodur Ring")
    ax1.plot(temps_mK, thermal_q, color="#ffcc66", lw=2, label="Fused Quartz Ring")
    ax1.plot(temps_mK, thermal_a, color="#ff6666", lw=2, label="Aluminum Ring")
    ax1.set_title(r"1. Thermal Expansion Limits ($\Delta T$)")
    ax1.set_xlabel(r"Temperature Stability Fluctuation (Kelvin)")
    ax1.set_ylabel(r"Induced Sagnac Phase Noise (Rad)")
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlim([min(temps_mK), max(temps_mK)])
    ax1.set_ylim([1e-12, 1e-3])
    ax1.legend(loc="lower right", fontsize=8)

    # Panel 2: Laser Drift
    ax2 = axes[1]
    ax2.plot(drifts_hz, laser_noise, color="#ff99ff", lw=2, label="HeNe Frequency Jitter")
    ax2.set_title(r"2. Laser Frequency Stability ($\Delta f$)")
    ax2.set_xlabel(r"Continuous Laser Frequency Drift (Hz)")
    ax2.set_ylabel(r"Induced Sagnac Phase Noise (Rad)")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlim([min(drifts_hz), max(drifts_hz)])
    ax2.set_ylim([1e-12, 1e-3])
    ax2.legend(loc="lower right", fontsize=8)

    # Panel 3: Seismic
    ax3 = axes[2]
    ax3.plot(vibes_m, seismic_noise, color="#99ff99", lw=2, label="Mirror Dither / Vibration")
    ax3.set_title(r"3. Seismic / Mechanical Isolation ($\Delta L_{path}$)")
    ax3.set_xlabel(r"Mechanical Mirror Displacement (meters)")
    ax3.set_ylabel(r"Induced Sagnac Phase Noise (Rad)")
    ax3.set_xscale("log")
    ax3.set_yscale("log")
    ax3.set_xlim([min(vibes_m), max(vibes_m)])
    ax3.set_ylim([1e-12, 1e-3])
    ax3.legend(loc="lower right", fontsize=8)

    plt.tight_layout()
    plt.subplots_adjust(top=0.85)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "sagnac_rlvg_tolerances.png"
    plt.savefig(target, dpi=300)
    print(f"[*] Plotted System Tolerance Sweeps: {target}")

    print("\n--- CRITICAL ENGINEERING REQUIREMENTS FOR AVE VERIFICATION ---")
    print(f"To detect the AVE Kinematic Target Phase of {AVE_TARGET_ANOMALY_PHASE:.2e} rad:")

    target_k = next((t for t, n in zip(temps_mK, thermal_z) if n > AVE_TARGET_ANOMALY_PHASE), temps_mK[-1])
    print(f">> THERMAL (Zerodur): Ring MUST be stabilized to better than {target_k:.4f} Kelvin.")

    target_hz = next((f for f, n in zip(drifts_hz, laser_noise) if n > AVE_TARGET_ANOMALY_PHASE), drifts_hz[-1])
    print(f">> LASER DRIFT: Source laser MUST be frequency-locked to better than {target_hz:.1f} Hz.")

    target_pm = next((v for v, n in zip(vibes_m, seismic_noise) if n > AVE_TARGET_ANOMALY_PHASE), vibes_m[-1])
    print(f">> SEISMIC: Mirror isolation MUST suppress vibrations above {target_pm*1e12:.2f} pico-meters.")


if __name__ == "__main__":
    run_tolerance_sweeps()
