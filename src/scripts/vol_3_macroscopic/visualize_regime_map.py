#!/usr/bin/env python3
"""
Regime Map Visualization
========================
Generates the multi-panel regime diagram for the manuscript (Ch.2 of Book 7).

Panels:
  1. S(r) curve with 4 regime zones shaded
  2. Cross-domain operating points on the regime diagram
  3. Quality factor Q = 1/S divergence

Output: manuscript/vol_1_foundations/regime_map.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.regime_map import R_LINEAR_MAX, R_NONLINEAR_MAX, R_YIELD_MAX


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("The Universal Regime Map", fontsize=16, fontweight="bold", y=1.02)

    # ── Panel 1: S(r) with regime zones ──
    ax1 = axes[0]
    r = np.linspace(0, 1.05, 1000)
    S = np.where(r <= 1.0, np.sqrt(np.maximum(0, 1 - r**2)), 0.0)

    # Shade regimes
    ax1.axvspan(0, R_LINEAR_MAX, alpha=0.15, color="#2196F3", label="I Linear")
    ax1.axvspan(R_LINEAR_MAX, R_NONLINEAR_MAX, alpha=0.15, color="#FFC107", label="II Nonlinear")
    ax1.axvspan(R_NONLINEAR_MAX, R_YIELD_MAX, alpha=0.15, color="#FF9800", label="III Yield")
    ax1.axvspan(R_YIELD_MAX, 1.05, alpha=0.15, color="#F44336", label="IV Ruptured")

    ax1.plot(r, S, "k-", linewidth=2.5)
    ax1.set_xlabel(r"$r = A/A_c$", fontsize=13)
    ax1.set_ylabel(r"$S(r) = \sqrt{1 - r^2}$", fontsize=13)
    ax1.set_title("Saturation Factor", fontsize=13)
    ax1.set_xlim(0, 1.05)
    ax1.set_ylim(-0.05, 1.05)
    ax1.legend(fontsize=9, loc="upper right")
    ax1.grid(True, alpha=0.3)

    # Mark key r values
    for rv, label in [(0.1, "r=0.1"), (0.9, "r=0.9"), (1.0, "r=1.0")]:
        Sv = np.sqrt(max(0, 1 - rv**2))
        ax1.axvline(rv, color="gray", ls="--", alpha=0.5)
        ax1.annotate(label, (rv, Sv + 0.05), fontsize=8, ha="center")

    # ── Panel 2: Cross-domain operating points ──
    ax2 = axes[1]

    # (name, r, domain_color, marker)
    points = [
        # Regime I
        ("LIGO GW", 1e-20, "#2196F3", "s"),
        ("Solar\nsurface", 2.1e-6, "#2196F3", "o"),
        ("Lab cap\n(1 kV)", 0.023, "#2196F3", "^"),
        # Regime II
        ("PONDER-05\n30 kV", 0.687, "#FFC107", "D"),
        ("Nb @ 4K", 0.435, "#FFC107", "v"),
        # Regime III
        ("PONDER-05\n43 kV", 0.985, "#FF9800", "D"),
        # Regime IV
        ("NS 1.4M☉", 1.46, "#F44336", "*"),
        ("BH at rs", 3.5, "#F44336", "p"),
        ("Magnetar", 5.29, "#F44336", "h"),
    ]

    # Use log scale for r to show the enormous dynamic range
    # r_vals = [p[1] for p in points]  # bulk lint fixup pass
    y_positions = np.linspace(0.9, 0.1, len(points))

    for i, (name, rv, color, marker) in enumerate(points):
        ax2.scatter(
            rv,
            y_positions[i],
            c=color,
            marker=marker,
            s=120,
            edgecolors="black",
            linewidths=0.5,
            zorder=5,
        )
        ax2.annotate(
            name,
            (rv, y_positions[i]),
            fontsize=8,
            ha="left",
            va="center",
            xytext=(8, 0),
            textcoords="offset points",
        )

    # Shade regime zones
    ax2.axvspan(1e-22, R_LINEAR_MAX, alpha=0.1, color="#2196F3")
    ax2.axvspan(R_LINEAR_MAX, R_NONLINEAR_MAX, alpha=0.1, color="#FFC107")
    ax2.axvspan(R_NONLINEAR_MAX, R_YIELD_MAX, alpha=0.1, color="#FF9800")
    ax2.axvspan(R_YIELD_MAX, 10, alpha=0.1, color="#F44336")

    for rv in [R_LINEAR_MAX, R_NONLINEAR_MAX, R_YIELD_MAX]:
        ax2.axvline(rv, color="gray", ls="--", alpha=0.4)

    ax2.set_xscale("log")
    ax2.set_xlim(1e-22, 10)
    ax2.set_ylim(0, 1)
    ax2.set_xlabel(r"$r = A/A_c$", fontsize=13)
    ax2.set_title("Cross-Domain Operating Points", fontsize=13)
    ax2.set_yticks([])
    ax2.grid(True, alpha=0.3, which="both")

    # Regime labels at top
    for rx, label in [(1e-15, "I"), (0.3, "II"), (0.95, "III"), (3, "IV")]:
        ax2.text(rx, 0.97, label, ha="center", va="top", fontsize=12, fontweight="bold", color="gray")

    # ── Panel 3: Q factor divergence ──
    ax3 = axes[2]
    r3 = np.linspace(0, 0.999, 500)
    Q3 = 1.0 / np.sqrt(1 - r3**2)

    ax3.axvspan(0, R_LINEAR_MAX, alpha=0.15, color="#2196F3")
    ax3.axvspan(R_LINEAR_MAX, R_NONLINEAR_MAX, alpha=0.15, color="#FFC107")
    ax3.axvspan(R_NONLINEAR_MAX, R_YIELD_MAX, alpha=0.15, color="#FF9800")

    ax3.semilogy(r3, Q3, "k-", linewidth=2.5)
    ax3.set_xlabel(r"$r = A/A_c$", fontsize=13)
    ax3.set_ylabel(r"$Q(r) = 1/S(r)$", fontsize=13)
    ax3.set_title("Energy Trapping Quality Factor", fontsize=13)
    ax3.set_xlim(0, 1.0)
    ax3.set_ylim(1, 1e3)
    ax3.grid(True, alpha=0.3)

    # Mark PONDER-05 Q value
    r_p05 = 0.687
    Q_p05 = 1.0 / np.sqrt(1 - r_p05**2)
    ax3.plot(
        r_p05,
        Q_p05,
        "D",
        color="#FFC107",
        markersize=10,
        markeredgecolor="black",
        markeredgewidth=1,
    )
    ax3.annotate(
        f"PONDER-05\nQ = {Q_p05:.1f}",
        (r_p05, Q_p05),
        fontsize=9,
        ha="left",
        xytext=(10, 0),
        textcoords="offset points",
    )

    plt.tight_layout()

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "manuscript", "vol_1_foundations")
    out_path = os.path.join(out_dir, "regime_map.png")
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    print(f"Saved: {out_path}")

    plt.close()


if __name__ == "__main__":
    main()
