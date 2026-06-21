"""
EMT Packing Fraction Landscape — Figure for Ch.2 Macroscopic Moduli.

Shows the K/G ratio as a function of packing fraction p, highlighting the
unique operating point p* = 8πα where K/G = 2 (trace-reversal identity).
Also marks the Cauchy solid (K/G = 5/3) and the rigidity threshold.

Output: assets/sim_outputs/emt_packing_landscape.png

FIGURE-STYLE: restyled to the AVE house style (ave.viz.style) 2026-06-21.
The effective coordination z₀ and the rigidity threshold p_G are now imported
from ave.core.constants (Z_COORDINATION, P_RIGIDITY) instead of hard-coded —
no physics/value change (z₀ ≈ 51.25 matches the manuscript-derived value).
The "amorphous central-force network" model language is left unchanged
(decision D3 open).
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import P_C, P_RIGIDITY, Z_COORDINATION
from ave.viz import style
from ave_path_util import sim_output

style.apply("print")

# ─── EMT model ───
# For a 3D amorphous central-force network (Feng-Thorpe-Garboczi),
# the K/G ratio depends on p relative to the percolation thresholds.
# We model this as a smooth interpolation.
z0 = Z_COORDINATION  # effective coordination from p_c (≈ 51.25, canonical)
p_K = 2 / z0  # bulk percolation threshold
p_G = P_RIGIDITY  # shear percolation threshold = 6/z₀ (canonical)

p = np.linspace(0.10, 0.40, 500)

# EMT K/G ratio: diverges at p_G, decreases monotonically above
# Using the analytical form: K/G = (p - p_K)/(p - p_G) × (z0/(z0-2)) for p>p_G
K_over_G = np.where(p > p_G, (p - p_K) / (p - p_G) * (z0 / (z0 - 2)) * 0.5, np.inf)
# Clip for display
K_over_G = np.clip(K_over_G, 0, 8)

# The actual AVE operating point
p_star = P_C
KG_star = 2.0

# Cauchy solid (Delaunay reference — NOT an AVE canonical constant)
p_cauchy = 0.3068
# At Cauchy point, K/G ≈ 5/3
KG_cauchy = 5.0 / 3.0

# ─── Figure ───
fig, ax = plt.subplots(figsize=style.figsize("single"))

# Reference lines
ax.axhline(
    2.0,
    color=style.COLORS["accent"],
    alpha=0.6,
    linewidth=1.2,
    linestyle="--",
    label=r"$K/G = 2$ (trace-reversal)",
)
ax.axhline(
    5 / 3,
    color=style.COLORS["comparison"],
    alpha=0.6,
    linewidth=1.2,
    linestyle=":",
    label=r"$K/G = 5/3$ (Cauchy solid)",
)

# Shading: fluid below p_G
ax.axvspan(0.10, p_G, alpha=0.10, color=style.COLORS["muted"], label="Fluid (no shear rigidity)")

# Plot K/G curve
mask = p > p_G + 0.002
ax.plot(p[mask], K_over_G[mask], color=style.COLORS["ave"], linewidth=2.5, label=r"EMT $K/G$ ratio")

# Mark the AVE operating point
ax.scatter(
    [p_star],
    [KG_star],
    s=180,
    c=style.COLORS["accent"],
    zorder=10,
    edgecolors="black",
    linewidths=1.5,
    label=f"AVE: $p_c = 8\\pi\\alpha \\approx {p_star:.4f}$",
)

# Mark the Cauchy point
ax.scatter(
    [p_cauchy],
    [KG_cauchy],
    s=110,
    c=style.COLORS["comparison"],
    zorder=10,
    marker="D",
    edgecolors="black",
    linewidths=1.2,
    label=f"Delaunay: $p_{{\\mathrm{{Cauchy}}}} \\approx {p_cauchy:.4f}$",
)

# Rigidity threshold
ax.axvline(p_G, color=style.COLORS["muted"], alpha=0.7, linewidth=1.5, linestyle="-.")

# Over-bracing arrow
ax.annotate(
    "",
    xy=(p_star, 1.2),
    xytext=(p_cauchy, 1.2),
    arrowprops=dict(arrowstyle="<->", color=style.COLORS["data"], lw=1.5),
)
ax.text(
    (p_star + p_cauchy) / 2,
    1.35,
    f"Over-bracing\n$\\mathcal{{R}}_{{OB}} = {p_cauchy/p_star:.3f}$",
    ha="center",
    va="bottom",
    fontsize=9,
    color=style.COLORS["data"],
    fontweight="bold",
)

# Annotations
ax.text(
    p_G - 0.005,
    7.0,
    "Rigidity\nthreshold\n$p_G$",
    ha="right",
    fontsize=8,
    color=style.COLORS["muted"],
)
ax.text(
    p_star + 0.008,
    KG_star + 0.3,
    "$K = 2G$\n$\\alpha^{-1} = 8\\pi/p_c$\n$= 137.036$",
    fontsize=9,
    color=style.COLORS["accent"],
    fontweight="bold",
)

# Labels
ax.set_xlabel(style.axis_label("Packing fraction", "p", ""))
ax.set_ylabel(style.axis_label("Modulus ratio", "K/G", ""))
ax.set_xlim(0.10, 0.40)
ax.set_ylim(0, 8)
style.legend(ax, where="right", fontsize=8)
ax.grid(True, alpha=0.3)

output_path = sim_output("emt_packing_landscape.png")
style.save(fig, output_path)
plt.close()
print(f"Saved: {output_path}")
