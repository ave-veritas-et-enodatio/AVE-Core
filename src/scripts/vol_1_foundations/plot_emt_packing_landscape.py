"""
EMT Packing Fraction Landscape — Figure for Ch.2 Macroscopic Moduli.

Shows the K/G ratio as a function of packing fraction p, highlighting the
unique operating point p* = 8πα where K/G = 2 (trace-reversal identity).
Also marks the Cauchy solid (K/G = 5/3) and the rigidity threshold.

Output: assets/sim_outputs/emt_packing_landscape.png
"""

import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from ave.core.constants import ALPHA, P_C

# ─── EMT model ───
# For a 3D amorphous central-force network (Feng-Thorpe-Garboczi),
# the K/G ratio depends on p relative to the percolation thresholds.
# We model this as a smooth interpolation.
z0 = 51.25  # effective coordination from p_c
p_K = 2 / z0  # bulk percolation threshold
p_G = 6 / z0  # shear percolation threshold

p = np.linspace(0.10, 0.40, 500)

# EMT K/G ratio: diverges at p_G, decreases monotonically above
# Using the analytical form: K/G = (p - p_K)/(p - p_G) × (z0/(z0-2)) for p>p_G
K_over_G = np.where(p > p_G, (p - p_K) / (p - p_G) * (z0 / (z0 - 2)) * 0.5, np.inf)
# Clip for display
K_over_G = np.clip(K_over_G, 0, 8)

# The actual AVE operating point
p_star = P_C
KG_star = 2.0

# Cauchy solid
p_cauchy = 0.3068
# At Cauchy point, K/G ≈ 5/3
KG_cauchy = 5.0 / 3.0

# ─── Figure ───
fig, ax = plt.subplots(figsize=(10, 6.5))
fig.patch.set_facecolor("#0d1117")
ax.set_facecolor("#0d1117")

# Stability regions
ax.axhspan(0, 0, color="red", alpha=0.05)
ax.axhline(
    2.0,
    color="#4CAF50",
    alpha=0.3,
    linewidth=1,
    linestyle="--",
    label=r"$K/G = 2$ (Trace-Reversal)",
)
ax.axhline(
    5 / 3,
    color="#FF9800",
    alpha=0.3,
    linewidth=1,
    linestyle=":",
    label=r"$K/G = 5/3$ (Cauchy Solid)",
)

# Shading: fluid below p_G
ax.axvspan(0.10, p_G, alpha=0.10, color="#F44336", label="Fluid (no shear rigidity)")

# Plot K/G curve
mask = p > p_G + 0.002
ax.plot(p[mask], K_over_G[mask], color="#58a6ff", linewidth=2.5, label=r"EMT $K/G$ ratio")

# Mark the AVE operating point
ax.scatter(
    [p_star],
    [KG_star],
    s=200,
    c="#4CAF50",
    zorder=10,
    edgecolors="white",
    linewidths=2,
    label=f"AVE: $p_c = 8\\pi\\alpha \\approx {p_star:.4f}$",
)

# Mark the Cauchy point
ax.scatter(
    [p_cauchy],
    [KG_cauchy],
    s=120,
    c="#FF9800",
    zorder=10,
    marker="D",
    edgecolors="white",
    linewidths=1.5,
    label=f"Delaunay: $p_{{Cauchy}} \\approx {p_cauchy:.4f}$",
)

# Rigidity threshold
ax.axvline(p_G, color="#F44336", alpha=0.5, linewidth=1.5, linestyle="-.")

# Over-bracing arrow
ax.annotate(
    "",
    xy=(p_star, 1.2),
    xytext=(p_cauchy, 1.2),
    arrowprops=dict(arrowstyle="<->", color="#f0883e", lw=2),
)
ax.text(
    (p_star + p_cauchy) / 2,
    1.35,
    f"Over-Bracing\n$\\mathcal{{R}}_{{OB}} = {p_cauchy/p_star:.3f}$",
    ha="center",
    va="bottom",
    fontsize=10,
    color="#f0883e",
    fontweight="bold",
)

# Annotations
ax.text(
    p_G - 0.005,
    7.0,
    "Rigidity\nThreshold\n$p_G$",
    ha="right",
    fontsize=9,
    color="#F44336",
    alpha=0.8,
)
ax.text(
    p_star + 0.008,
    KG_star + 0.3,
    f"$K = 2G$\n$\\alpha^{{-1}} = 8\\pi/p_c$\n$= 137.036$",
    fontsize=10,
    color="#4CAF50",
    fontweight="bold",
)

# Labels
ax.set_xlabel("Packing Fraction $p$", fontsize=14, color="white")
ax.set_ylabel("$K / G$ Ratio", fontsize=14, color="white")
ax.set_title(
    "Effective Medium Theory: The Trace-Reversal Operating Point",
    fontsize=15,
    color="white",
    pad=15,
)
ax.set_xlim(0.10, 0.40)
ax.set_ylim(0, 8)
ax.legend(fontsize=9, facecolor="#161b22", edgecolor="#30363d", labelcolor="white", loc="upper right")
ax.grid(True, alpha=0.15, color="#30363d")
ax.tick_params(colors="white")
for spine in ax.spines.values():
    spine.set_color("#30363d")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
output_path = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs", "emt_packing_landscape.png")
plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")

# Also copy to standard location
import shutil

dst = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs", "emt_packing_landscape.png")
shutil.copy2(output_path, dst)
print(f"Copied to: {dst}")
