#!/usr/bin/env python3
r"""
AVE: Photon Helical Spin-1 Confinement
=======================================
Generates 'photon_helical_spin.png' for Book 2, Chapter 5.

Visualizes how a propagating transverse EM wave natively winds into a
stationary Spin-1 helical loop when encountering extreme localized
network impedance (Z → Z_crit). The discrete sequential excitation of
the M_A LC nodes structurally guarantees absolute charge containment.
"""

import os
import sys
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

def generate_photon_helical_spin():
    print("[*] Generating Photon Helical Spin-1 Confinement Figure...")

    plt.style.use('dark_background')
    fig = plt.figure(figsize=(18, 7))
    fig.patch.set_facecolor('#0f0f12')

    # =====================================================================
    # LEFT PANEL: Free propagating transverse EM wave
    # =====================================================================
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.set_facecolor('#0f0f12')

    t = np.linspace(0, 6 * np.pi, 1000)
    k = 1.0  # wavenumber

    # E-field (x-polarized) and B-field (y-polarized) of a propagating photon
    Ex = np.cos(k * t)
    By = np.cos(k * t)
    z_prop = t / (2 * np.pi)  # propagation axis

    ax1.plot(Ex, np.zeros_like(t), z_prop, color='#ff3366', lw=2, label='$\\vec{E}$ (Electric)')
    ax1.plot(np.zeros_like(t), By, z_prop, color='#3399ff', lw=2, label='$\\vec{B}$ (Magnetic)')
    ax1.plot(np.zeros_like(t), np.zeros_like(t), z_prop, color='white', lw=0.5, alpha=0.3)

    ax1.set_title("Linear Photon\n(Free Propagation)", color='white', fontsize=13, pad=10)
    ax1.set_xlabel("$E_x$", color='#ff3366', fontsize=11)
    ax1.set_ylabel("$B_y$", color='#3399ff', fontsize=11)
    ax1.set_zlabel("z (Propagation)", color='white', fontsize=10)
    ax1.legend(frameon=False, fontsize=9, loc='upper left')

    ax1.xaxis.pane.fill = False
    ax1.yaxis.pane.fill = False
    ax1.zaxis.pane.fill = False
    ax1.grid(True, alpha=0.15)
    ax1.view_init(elev=15, azim=-60)

    # =====================================================================
    # CENTER PANEL: Impedance transition zone
    # =====================================================================
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.set_facecolor('#0f0f12')

    # Wave compresses as impedance increases — wavelength shrinks, amplitude grows
    t2 = np.linspace(0, 4 * np.pi, 800)
    z2 = t2 / (2 * np.pi)

    # Impedance gradient: increases along z
    Z_gradient = 1.0 + 2.0 * (z2 / z2[-1]) ** 2
    wavelength_factor = 1.0 / Z_gradient
    amplitude_factor = np.sqrt(Z_gradient)

    # Cumulative phase (compressing wavelength)
    phase = np.cumsum(wavelength_factor) * (t2[1] - t2[0]) * k
    Ex2 = amplitude_factor * np.cos(phase)
    By2 = amplitude_factor * np.cos(phase)

    ax2.plot(Ex2, np.zeros_like(t2), z2, color='#ff3366', lw=2)
    ax2.plot(np.zeros_like(t2), By2, z2, color='#3399ff', lw=2)
    ax2.plot(np.zeros_like(t2), np.zeros_like(t2), z2, color='white', lw=0.5, alpha=0.3)

    # Draw impedance gradient as background color
    for i in range(0, len(z2) - 10, 10):
        alpha_val = 0.02 + 0.15 * (z2[i] / z2[-1]) ** 2
        ax2.plot([0], [0], [z2[i]], 'o', color='#ffcc00', alpha=alpha_val, markersize=20)

    ax2.set_title("Impedance Gradient\n($Z \\rightarrow Z_{crit}$)", color='white', fontsize=13, pad=10)
    ax2.set_xlabel("$E_x$", color='#ff3366', fontsize=11)
    ax2.set_ylabel("$B_y$", color='#3399ff', fontsize=11)
    ax2.set_zlabel("z", color='white', fontsize=10)

    ax2.xaxis.pane.fill = False
    ax2.yaxis.pane.fill = False
    ax2.zaxis.pane.fill = False
    ax2.grid(True, alpha=0.15)
    ax2.view_init(elev=15, azim=-60)

    # =====================================================================
    # RIGHT PANEL: Confined Spin-1 Helical Loop (the electron)
    # =====================================================================
    ax3 = fig.add_subplot(133, projection='3d')
    ax3.set_facecolor('#0f0f12')

    # Toroidal helix — light trapped in a closed loop
    phi = np.linspace(0, 2 * np.pi, 600)  # Major loop angle
    R_major = 1.5   # Major radius (toroid)
    R_minor = 0.5   # Minor radius (helix winding)
    n_winds = 3     # Number of helical windings (Spin-1 = one winding per 2π)

    x_torus = (R_major + R_minor * np.cos(n_winds * phi)) * np.cos(phi)
    y_torus = (R_major + R_minor * np.cos(n_winds * phi)) * np.sin(phi)
    z_torus = R_minor * np.sin(n_winds * phi)

    # Color gradient to show phase progression
    colors = plt.cm.cool(np.linspace(0, 1, len(phi)))

    for i in range(len(phi) - 1):
        ax3.plot(x_torus[i:i+2], y_torus[i:i+2], z_torus[i:i+2],
                 color=colors[i], lw=3, alpha=0.9)

    # Central axis
    ax3.plot([0], [0], [0], 'o', color='#ffcc00', markersize=8, zorder=10)

    # Rotation arrow indicator
    arrow_phi = np.linspace(0, 1.8 * np.pi, 100)
    r_arrow = 2.2
    ax3.plot(r_arrow * np.cos(arrow_phi), r_arrow * np.sin(arrow_phi),
             np.zeros_like(arrow_phi), color='#33ffcc', lw=1.5, alpha=0.5, linestyle='--')

    ax3.set_title("Confined Spin-1 Loop\n(Stationary Electron)", color='white', fontsize=13, pad=10)

    ax3.set_xlim([-2.5, 2.5])
    ax3.set_ylim([-2.5, 2.5])
    ax3.set_zlim([-1.5, 1.5])
    ax3.set_box_aspect([1, 1, 0.6])

    ax3.xaxis.pane.fill = False
    ax3.yaxis.pane.fill = False
    ax3.zaxis.pane.fill = False
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_zticks([])
    ax3.grid(True, alpha=0.15)
    ax3.view_init(elev=25, azim=-45)

    plt.tight_layout(pad=2.0)

    out_dir = project_root / "assets" / "sim_outputs"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "photon_helical_spin.png"
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()

    print(f"[*] Photon Helical Spin Figure Saved: {out_path}")

if __name__ == "__main__":
    generate_photon_helical_spin()
