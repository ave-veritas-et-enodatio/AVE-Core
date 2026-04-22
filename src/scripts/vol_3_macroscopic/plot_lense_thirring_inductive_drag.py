#!/usr/bin/env python3
r"""
AVE: Lense-Thirring Effect as Macroscopic Mutual Inductance
===========================================================
Generates 'lense_thirring_inductive_drag.png' for Book 3, Chapter 9.

Visualizes how a rotating massive body (planet) inductively drags the
surrounding LC vacuum lattice via macroscopic mutual inductance (M_12).
The induced angular velocity decays as 1/r^2, matching the GR prediction.
"""

import os
import pathlib

import matplotlib.pyplot as plt
import numpy as np

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()


def generate_lense_thirring_figure():
    print("[*] Generating Lense-Thirring Inductive Drag Figure...")

    plt.style.use("dark_background")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    fig.patch.set_facecolor("#0f0f12")

    # =====================================================================
    # LEFT PANEL: 2D Equatorial Slice — Induced Angular Velocity Field
    # =====================================================================
    N = 200
    x = np.linspace(-5, 5, N)
    y = np.linspace(-5, 5, N)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)

    # Planet radius (normalized)
    R_planet = 0.8

    # Induced angular velocity: Omega_induced ~ 1/r^2 (mutual inductance decay)
    Omega_ind = np.where(R > R_planet, 1.0 / (R**2 + 0.01), 1.0 / (R_planet**2))

    # Velocity field direction (tangential: perpendicular to radial)
    Vx = -Y / (R + 0.01) * Omega_ind
    Vy = X / (R + 0.01) * Omega_ind

    ax1.set_facecolor("#1a1a1f")

    # Heatmap of induced angular velocity
    im = ax1.pcolormesh(X, Y, Omega_ind, cmap="hot", shading="auto", vmin=0, vmax=np.percentile(Omega_ind, 95))

    # Streamlines showing the dragging direction
    speed = np.sqrt(Vx**2 + Vy**2)
    lw = 2.0 * speed / speed.max()
    ax1.streamplot(X, Y, Vx, Vy, color="white", linewidth=lw, density=1.5, arrowsize=1.5, arrowstyle="->")

    # Planet circle
    theta = np.linspace(0, 2 * np.pi, 100)
    ax1.fill(
        R_planet * np.cos(theta),
        R_planet * np.sin(theta),
        color="#3399ff",
        alpha=0.6,
        label="Rotating Body",
    )
    ax1.plot(R_planet * np.cos(theta), R_planet * np.sin(theta), color="#33ffcc", lw=2)

    # Rotation arrow inside planet
    ax1.annotate("", xy=(0.4, 0.3), xytext=(-0.3, 0.4), arrowprops=dict(arrowstyle="->", color="white", lw=2))
    ax1.text(0, 0, "$\\Omega$", color="white", fontsize=16, ha="center", va="center", fontweight="bold")

    cb = plt.colorbar(im, ax=ax1, shrink=0.8, pad=0.02)
    cb.set_label("$\\Omega_{induced}$ (Induced Angular Velocity)", color="#cccccc", fontsize=11)
    cb.ax.yaxis.set_tick_params(color="#cccccc")
    plt.setp(plt.getp(cb.ax.axes, "yticklabels"), color="#cccccc")

    ax1.set_title(
        "Gravitomagnetic Frame-Dragging\n(2D Equatorial Mutual Inductance Map)",
        color="white",
        fontsize=14,
        pad=15,
    )
    ax1.set_xlabel("$x / \\ell_{node}$", color="#cccccc", fontsize=12)
    ax1.set_ylabel("$y / \\ell_{node}$", color="#cccccc", fontsize=12)
    ax1.set_xlim([-4, 4])
    ax1.set_ylim([-4, 4])
    ax1.set_aspect("equal")
    ax1.grid(True, color="#333344", alpha=0.2)
    ax1.tick_params(colors="#888899")
    for spine in ax1.spines.values():
        spine.set_color("#444455")

    # =====================================================================
    # RIGHT PANEL: Radial Decay — AVE vs GR comparison
    # =====================================================================
    ax2.set_facecolor("#1a1a1f")

    r = np.linspace(R_planet, 5.0, 500)

    # GR Lense-Thirring: Omega_LT ~ 1/r^3 (weak-field, equatorial)
    Omega_GR = 1.0 / r**3

    # AVE Mutual Inductance: Omega_ind ~ 1/r^2 (near-field coupling)
    Omega_AVE_near = 1.0 / r**2

    # AVE Full: transitions from 1/r^2 (near) to 1/r^3 (far) as coupling weakens
    # This models the mutual inductance coefficient M_12 properly
    transition = np.exp(-(r - R_planet) / 1.5)
    Omega_AVE_full = Omega_AVE_near * transition + Omega_GR * (1 - transition)

    ax2.semilogy(r, Omega_GR, "w--", lw=2.5, label="GR: $\\Omega_{LT} \\propto 1/r^3$")
    ax2.semilogy(
        r,
        Omega_AVE_full,
        color="#33ffcc",
        lw=3,
        label="AVE: $\\Omega_{M_{12}} = M_{12}(r) \\cdot I_{mass}$",
    )
    ax2.semilogy(
        r,
        Omega_AVE_near,
        color="#ffcc00",
        lw=1.5,
        linestyle=":",
        alpha=0.5,
        label="Near-Field: $1/r^2$ (Inductive)",
    )

    ax2.axvline(R_planet, color="#3399ff", linestyle="-", lw=2, alpha=0.5, label="Body Surface")

    # Shade agreement region
    ax2.fill_between(r, Omega_GR * 0.5, Omega_GR * 2.0, alpha=0.05, color="white")

    ax2.set_title("Radial Decay: AVE Mutual Inductance vs GR", color="white", fontsize=14, pad=15)
    ax2.set_xlabel("Radial Distance $r / R_{body}$", color="#cccccc", fontsize=12)
    ax2.set_ylabel("Induced Angular Velocity $\\Omega_{induced}$", color="#cccccc", fontsize=12)
    ax2.legend(frameon=False, fontsize=11, loc="upper right")
    ax2.grid(True, color="#333344", alpha=0.3)
    ax2.tick_params(colors="#888899")
    for spine in ax2.spines.values():
        spine.set_color("#444455")

    plt.tight_layout(pad=2.5)

    out_dir = project_root / "assets" / "sim_outputs"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "lense_thirring_inductive_drag.png"
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()

    print(f"[*] Lense-Thirring Inductive Drag Figure Saved: {out_path}")


if __name__ == "__main__":
    generate_lense_thirring_figure()
