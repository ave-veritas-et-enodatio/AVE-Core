#!/usr/bin/env python3
r"""
AVE: Meissner Effect as Phase-Locked Gear Train
================================================
Generates 'meissner_gear_train.png' for Book 3, Chapter 17.

Left: Normal conduction — boundary torque causes localized slipping
      and deep chaotic penetration into the bulk (Resistance/Skin Effect).
Right: Superconduction — phase-locked flywheels create infinite inertia,
       boundary gears refuse to rotate, exponential decay = London penetration depth.
"""
import os
import pathlib
import numpy as np
import matplotlib.pyplot as plt

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()


def generate():
    print("[*] Generating Meissner Gear Train Figure...")
    plt.style.use("dark_background")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    fig.patch.set_facecolor("#0f0f12")

    x = np.linspace(0, 5, 500)

    # --- LEFT PANEL: Normal Conduction (Skin Effect) ---
    ax1.set_facecolor("#1a1a1f")

    # Each flywheel independently couples with friction -> chaotic decay
    omega_normal = np.exp(-x / 2.0) * (1.0 + 0.3 * np.sin(8 * x) * np.exp(-x / 1.5))
    ax1.plot(x, omega_normal, color="#ff3366", lw=3, label="$\\omega(x)$ — Chaotic Penetration")
    ax1.fill_between(x, 0, omega_normal, alpha=0.15, color="#ff3366")

    # Draw gear icons (circles at key depths)
    gear_x = np.linspace(0.2, 4.0, 12)
    gear_omega = np.exp(-gear_x / 2.0) * (1.0 + 0.3 * np.sin(8 * gear_x) * np.exp(-gear_x / 1.5))
    sizes = 200 * (gear_omega / gear_omega.max())
    ax1.scatter(
        gear_x,
        gear_omega,
        s=sizes,
        c="#ff6699",
        edgecolors="white",
        linewidth=1.5,
        zorder=5,
        alpha=0.8,
    )

    # Arrows showing slipping
    for i in range(0, len(gear_x) - 1, 2):
        ax1.annotate(
            "",
            xy=(gear_x[i + 1], gear_omega[i + 1]),
            xytext=(gear_x[i], gear_omega[i]),
            arrowprops=dict(arrowstyle="->", color="white", lw=1, alpha=0.4),
        )

    ax1.axhline(0, color="white", lw=0.5, alpha=0.3)
    ax1.set_title("Normal Conduction\n(Independent Flywheel Slipping)", color="white", fontsize=14, pad=15)
    ax1.set_xlabel("Depth into Conductor $x / \\lambda$", color="#cccccc", fontsize=12)
    ax1.set_ylabel("Angular Velocity $\\omega(x)$", color="#cccccc", fontsize=12)
    ax1.legend(frameon=False, fontsize=11, loc="upper right")
    ax1.grid(True, color="#333344", alpha=0.3)
    ax1.tick_params(colors="#888899")
    for spine in ax1.spines.values():
        spine.set_color("#444455")

    # --- RIGHT PANEL: Superconductor (Phase-Locked Gear Train) ---
    ax2.set_facecolor("#1a1a1f")

    # London penetration depth: perfect exponential decay
    lambda_L = 0.3  # London penetration depth (normalized)
    omega_super = np.exp(-x / lambda_L)

    ax2.plot(x, omega_super, color="#33ffcc", lw=3, label=f"$\\omega(x) = \\omega_0 e^{{-x/\\lambda_L}}$")
    ax2.fill_between(x, 0, omega_super, alpha=0.1, color="#33ffcc")

    # Draw phase-locked gears (all same size = rigid coupling)
    gear_x2 = np.linspace(0.1, 2.0, 15)
    gear_omega2 = np.exp(-gear_x2 / lambda_L)
    ax2.scatter(
        gear_x2,
        gear_omega2,
        s=150,
        c="#33ffcc",
        edgecolors="white",
        linewidth=2.0,
        zorder=5,
        alpha=0.9,
        marker="o",
    )

    # Draw rigid coupling lines between gears
    for i in range(len(gear_x2) - 1):
        ax2.plot(
            [gear_x2[i], gear_x2[i + 1]],
            [gear_omega2[i], gear_omega2[i + 1]],
            color="#ffcc00",
            lw=2,
            alpha=0.5,
        )

    # Mark lambda_L
    ax2.axvline(
        lambda_L,
        color="#ffcc00",
        linestyle="--",
        lw=2,
        alpha=0.7,
        label=f"$\\lambda_L = {lambda_L}$",
    )

    ax2.axhline(0, color="white", lw=0.5, alpha=0.3)
    ax2.set_title(
        "Superconductor ($T < T_c$)\n(Phase-Locked Macroscopic Gear Train)",
        color="white",
        fontsize=14,
        pad=15,
    )
    ax2.set_xlabel("Depth into Superconductor $x / \\lambda$", color="#cccccc", fontsize=12)
    ax2.set_ylabel("Angular Velocity $\\omega(x)$", color="#cccccc", fontsize=12)
    ax2.legend(frameon=False, fontsize=11, loc="upper right")
    ax2.grid(True, color="#333344", alpha=0.3)
    ax2.tick_params(colors="#888899")
    for spine in ax2.spines.values():
        spine.set_color("#444455")

    # Annotation
    ax2.text(
        1.5,
        0.5,
        "Infinite Macroscopic\nInertia → Perfect\nField Expulsion",
        color="#ffcc00",
        fontsize=12,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#1a1a1f", edgecolor="#ffcc00", alpha=0.8),
    )

    plt.tight_layout(pad=2.5)

    out_dir = project_root / "assets" / "sim_outputs"
    os.makedirs(out_dir, exist_ok=True)
    out_path = out_dir / "meissner_gear_train.png"
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"[*] Meissner Gear Train Figure Saved: {out_path}")


if __name__ == "__main__":
    generate()
