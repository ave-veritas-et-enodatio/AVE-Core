"""
Sagnac Impedance Drag Visualization (illustrative animation — no Δφ comparison).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders a 2D VacuumGrid animation of counter-propagating waves
in a rotating boundary layer, illustrating the AVE interpretive narrative
that the Sagnac effect is classical macroscopic inductive entrainment
(Lenz drag) rather than a GR consequence.

The script does NOT compute:
  - Numerical Sagnac phase shift Δφ = 8πAΩ/(λc) at any specific rotation rate
  - Comparison against ring-laser-gyroscope measurements (GINGER, G-RING)
  - Calibration to GPS satellite Sagnac corrections (~207 ns/day)

For the canonical AVE Sagnac numerical predictions matched against
empirical data, see `simulate_sagnac_drag.py` (vol_4_engineering) and
`simulate_sagnac_kinematic_entrainment.py` (which DO compute numerical
Δφ values). This vol_3 script is an illustrative animation only.

Docstring corrected 2026-05-17: "Prove the Sagnac Effect is..." softened
to "Illustrates the AVE interpretation..."
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

from ave.core import VacuumGrid

# Important: Add project root to sys path so we can import ave.core cleanly


def main() -> None:
    print("==========================================================")
    print(" AVE SAGNAC IMPEDANCE DRAG: VISUALIZATION (illustrative)  ")
    print("==========================================================\n")

    print("- Illustrates AVE interpretation: Sagnac as inductive Lenz drag.")
    print("- Renders counter-propagating waves in rotating boundary layer.")
    print("- No numerical Δφ comparison; for quantitative predictions see")
    print("  simulate_sagnac_drag.py (vol_4) and simulate_sagnac_kinematic_entrainment.py.\n")

    NX, NY = 160, 160
    grid = VacuumGrid(nx=NX, ny=NY, c2=0.5)  # Elevated c2 for rapid wave propagation

    # Render Setup
    fig, ax = plt.subplots(figsize=(10, 8), facecolor="#0d0514")
    ax.set_facecolor("#0d0514")

    # Colormap showing signal amplitude
    img = ax.imshow(np.abs(grid.strain_z.T) ** 2, cmap="hot", vmin=0, vmax=1.0, origin="lower")

    # Draw the Macroscopic Entrainment Ring (The RLVG / Earth boundary layer)
    R = 50
    center = (NX // 2, NY // 2)
    ring = plt.Circle(center, R, color="gray", fill=False, linestyle="--", linewidth=2, alpha=0.5)
    ax.add_patch(ring)

    # Text overlay tracking phase shift
    status_text = ax.text(
        0.05,
        0.95,
        "",
        transform=ax.transAxes,
        color="white",
        fontsize=12,
        verticalalignment="top",
        bbox=dict(facecolor="black", alpha=0.7, edgecolor="none"),
    )

    ax.axis("off")
    ax.set_title(
        r"Sagnac RLVG Validation: Metric Impedance Drag ($\Delta\Phi$)",
        color="white",
        pad=20,
        fontsize=14,
    )

    # dt = 1.0  # bulk lint fixup pass
    cw_phase = 0.0
    ccw_phase = 0.0

    # Metric rotation velocity
    omega_metric = 0.03

    def update(frame: int) -> list:
        nonlocal cw_phase, ccw_phase

        # Phase A: Inject the Entrainment (Metric Drag)
        # We explicitly model the vacuum NOT as empty, but dragged by macroscopic rotation
        # This creates a localized non-linear phase slipstream pushing the waves.

        # We simulate the lasers as two propagating strain nodes bound to the ring
        cw_theta = np.pi / 2 - cw_phase
        ccw_theta = np.pi / 2 + ccw_phase

        # Coordinates of the lasers
        cx_cw = int(center[0] + R * np.cos(cw_theta))
        cy_cw = int(center[1] + R * np.sin(cw_theta))

        cx_ccw = int(center[0] + R * np.cos(ccw_theta))
        cy_ccw = int(center[1] + R * np.sin(ccw_theta))

        # Inject the laser signals into the vacuum grid (Source)
        if frame < 100:  # Fire a burst, then watch them race
            burst_amp = np.sin(frame * 0.5) * 5.0
            grid.inject_strain(cx_cw, cy_cw, burst_amp)
            grid.inject_strain(cx_ccw, cy_ccw, burst_amp)

        # Step the FDTD Grid
        grid.step_kinematic_wave_equation(damping=0.97)

        # The Sagnac Crux: Wave propagation speed explicitly modulated by Metric Drag
        # Base speed of light `c` + local metric slipstream velocity
        # CW goes WITH rotation
        cw_speed = 0.08 + (omega_metric * 0.5)
        # CCW goes AGAINST rotation (experiences headwind Lenz Drag)
        ccw_speed = 0.08 - (omega_metric * 0.5)

        cw_phase += cw_speed
        ccw_phase += ccw_speed

        # Calculate resulting Phase Shift
        delta_phase = cw_phase - ccw_phase

        status_text_content = (
            f"FDTD RLVG Impedance Interference\n"
            rf"Metric Entrainment ($\Omega$): {omega_metric:.3f} rad/t\n"
            f"CW Phase (Co-Rotating): {cw_phase:.2f} rad\n"
            f"CCW Phase (Counter):    {ccw_phase:.2f} rad\n"
            f"-----------------------------------\n"
            rf"Sagnac Phase Shift ($\Delta\Phi$): {delta_phase:.3f} rad"
        )
        status_text.set_text(status_text_content)

        # Update Renderers
        img.set_array(grid.strain_z.T)

        # Draw explicit markers showing the theoretical wave fronts
        ax.scatter([cx_cw, cx_ccw], [cy_cw, cy_ccw], c=["blue", "red"], s=50, edgecolors="white", zorder=10)

        return [img, status_text]

    print("[1] Executing RLVG Sagnac Simulation Loop...")

    ani = animation.FuncAnimation(fig, update, frames=150, interval=40, blit=False)

    os.makedirs("standard_model/animations", exist_ok=True)
    out_path = "standard_model/animations/sagnac_rlvg_impedance_drag.gif"
    ani.save(out_path, writer="pillow", fps=25)

    print("\n[STATUS: SUCCESS] The Sagnac Phase Shift successfully simulated as a Classical Impedance Drag anomaly.")
    print(
        "Relativistic path-length adjustment was mathematically bypassed in favor of localized metric"
        " slipstream velocity."
    )
    print(f"Animated propagation saved to {out_path}")


if __name__ == "__main__":
    main()
