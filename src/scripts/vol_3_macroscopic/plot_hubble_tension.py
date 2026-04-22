"""
Hubble Tension Position — Figure for Ch.12 Open Problems.

Shows AVE's H∞ = 69.32 km/s/Mpc positioned between Planck (CMB) and
SH0ES (local) measurements, visualizing the Hubble tension.

Output: assets/sim_outputs/hubble_tension_position.png
"""

import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from ave.core.constants import H_INFINITY

# Convert H_inf to km/s/Mpc
H_inf_kms = H_INFINITY * 3.0857e22 / 1e3

# Measurements
measurements = [
    ("Planck (CMB)", 67.4, 0.5, "#4FC3F7", 4),
    ("TRGB (Chicago)", 69.8, 1.7, "#81C784", 3),
    ("ACT (CMB)", 67.6, 1.1, "#7986CB", 3),
    ("SH0ES (Cepheid)", 73.04, 1.04, "#EF5350", 4),
    ("H0LiCOW (Lensing)", 73.3, 1.8, "#FF8A65", 3),
]

fig, ax = plt.subplots(figsize=(10, 5.5))
fig.patch.set_facecolor("#0d1117")
ax.set_facecolor("#0d1117")

# Plot measurement bands
y_pos = list(range(len(measurements)))
for i, (name, val, err, color, sigma) in enumerate(measurements):
    # Error bar
    ax.barh(
        i,
        2 * err,
        left=val - err,
        height=0.4,
        color=color,
        alpha=0.25,
        edgecolor=color,
        linewidth=1,
    )
    # Central value
    ax.plot(val, i, "o", color=color, markersize=8, zorder=5)
    # Label
    label_x = val - err - 0.3
    ax.text(label_x, i, f"{name}\n{val} ± {err}", ha="right", va="center", fontsize=9, color=color)

# AVE prediction
ax.axvline(H_inf_kms, color="#FFD600", linewidth=3, zorder=10, alpha=0.9)
ax.axvline(H_inf_kms, color="#FFD600", linewidth=12, zorder=9, alpha=0.15)
ax.text(
    H_inf_kms + 0.15,
    len(measurements) - 0.3,
    f"AVE: $H_\\infty = {H_inf_kms:.2f}$\nkm/s/Mpc\n(zero parameters)",
    fontsize=11,
    color="#FFD600",
    fontweight="bold",
    va="top",
    ha="left",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#0d1117", edgecolor="#FFD600", alpha=0.9),
)

# Tension band
ax.axvspan(67.4, 73.04, alpha=0.05, color="white", label="Tension band")

ax.set_yticks([])
ax.set_xlabel(r"$H_0$ (km/s/Mpc)", fontsize=14, color="white")
ax.set_title("The Hubble Tension: AVE Prediction in Context", fontsize=15, color="white", pad=15)
ax.set_xlim(63, 78)
ax.grid(True, alpha=0.15, color="#30363d", axis="x")
ax.tick_params(colors="white")
for spine in ax.spines.values():
    spine.set_color("#30363d")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.tight_layout()
output_path = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs", "hubble_tension_position.png")
plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")

import shutil

dst = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs", "hubble_tension_position.png")
shutil.copy2(output_path, dst)
print(f"Copied to: {dst}")
