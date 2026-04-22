"""
Cross-Scale Verification Dashboard — Figure for Ch.9 Computational Proof.

Shows the 39 orders of magnitude spanned by the single AVE saturation
operator, from ℓ_node (~10⁻¹³ m) to the Hubble radius (~10²⁶ m).

Output: assets/sim_outputs/cross_scale_verification.png
"""

import os

import matplotlib.pyplot as plt

# Domain data: (name, log10(scale_m), agreement, color)
domains = [
    ("Lattice Node\n$\\ell_{node}$", -13, "—", "#B388FF"),
    ("Proton\n$r_p$", -15, "0.002%", "#7C4DFF"),
    ("Nuclear\n$K_{mut}$", -14.5, "1%", "#9C27B0"),
    ("Superconductor\n$B_c(T)$", -9, "exact", "#4FC3F7"),
    ("Molecular\n(protein)", -9.5, "5%", "#00BCD4"),
    ("Seismic\n(PREM)", 6.8, "matches", "#4CAF50"),
    ("Stellar\nInterior", 9, "8%", "#FF9800"),
    ("Planetary\nMagnetosphere", 7.5, "9-12%", "#CDDC39"),
    ("Solar System\n(Kirkwood)", 11, "<0.3%", "#FFC107"),
    ("Galactic\nRotation", 20, "5%", "#EF5350"),
    ("Hubble\n$H_\\infty$", 26, "2.9%", "#F44336"),
]

fig, ax = plt.subplots(figsize=(14, 5))
fig.patch.set_facecolor("#0d1117")
ax.set_facecolor("#0d1117")

# Scale bar from 10^-16 to 10^27
for i, (name, log_scale, agreement, color) in enumerate(domains):
    ax.scatter([log_scale], [0], s=200, c=color, zorder=10, edgecolors="white", linewidths=1.5)
    # Alternate label positions
    y_off = 0.4 if i % 2 == 0 else -0.5
    va = "bottom" if i % 2 == 0 else "top"
    ax.annotate(
        f"{name}\n({agreement})",
        xy=(log_scale, 0),
        xytext=(log_scale, y_off),
        fontsize=8,
        color=color,
        ha="center",
        va=va,
        arrowprops=dict(arrowstyle="-", color=color, alpha=0.4, lw=0.8),
    )

# Central line
ax.axhline(0, color="#58a6ff", linewidth=2, alpha=0.3, zorder=1)

# The "one operator" banner
ax.fill_between([-16, 27], -0.05, 0.05, color="#58a6ff", alpha=0.1)
ax.text(
    5,
    -1.05,
    r"$\mathbf{S(x, x_{yield}) = \sqrt{1 - (x/x_{yield})^2}}$",
    fontsize=14,
    color="#58a6ff",
    ha="center",
    va="center",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#0d1117", edgecolor="#58a6ff", alpha=0.9),
)

# Scale annotations
ax.text(-15, 0.95, "Subatomic", fontsize=10, color="#B388FF", ha="center", alpha=0.6)
ax.text(-9, 0.95, "Lab Scale", fontsize=10, color="#4FC3F7", ha="center", alpha=0.6)
ax.text(7.5, 0.95, "Planetary", fontsize=10, color="#4CAF50", ha="center", alpha=0.6)
ax.text(20, 0.95, "Galactic", fontsize=10, color="#EF5350", ha="center", alpha=0.6)

# Span arrow
ax.annotate(
    "",
    xy=(26, -0.85),
    xytext=(-15, -0.85),
    arrowprops=dict(arrowstyle="<->", color="white", lw=1.5),
)
ax.text(
    5,
    -0.78,
    "39 orders of magnitude — one operator",
    fontsize=11,
    color="white",
    ha="center",
    fontweight="bold",
)

ax.set_xlabel(r"$\log_{10}$(Scale / meters)", fontsize=14, color="white")
ax.set_xlim(-17, 28)
ax.set_ylim(-1.2, 1.15)
ax.set_yticks([])
ax.set_title(
    "Cross-Scale Verification: One Saturation Kernel Across All Physics",
    fontsize=15,
    color="white",
    pad=15,
)
ax.tick_params(colors="white")
for spine in ax.spines.values():
    spine.set_color("#30363d")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.tight_layout()
output_path = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs", "cross_scale_verification.png")
plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")

import shutil

dst = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs", "cross_scale_verification.png")
shutil.copy2(output_path, dst)
print(f"Copied to: {dst}")
