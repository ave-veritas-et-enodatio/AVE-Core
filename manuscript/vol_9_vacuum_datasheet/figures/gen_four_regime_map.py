#!/usr/bin/env python3
"""Generate the four-regime S(r) map figure for Vol 9 Ch 14.

Plots the universal saturation kernel S(r)=sqrt(1-r^2) on the operating-point
(excitation) axis r=A/A_c, with the four universal regimes shaded (canonical
REGIME_COLORS, ave.viz.style) and bounded by r1=sqrt(2*alpha), r2=sqrt(3)/2
(spin-2 sector), r3=1:

    I   Linear      r < r1            S > 0.993
    II  Nonlinear   r1 <= r < r2      0.500 < S <= 0.993
    III Avalanche   r2 <= r < r3      0 < S <= 0.500
    IV  Ruptured    r >= r3 = 1       S = 0

This is the datasheet plot of the four-regime partition (tab:vol9_phase_*),
the excitation map of the solid phase (Ch 14 demotes it from the thermodynamic
phase diagram). r2=sqrt(3)/2 is the spin-2 sector value.

ALL boundary values derive ONLY from canonical constants (ave.core.constants).

Run:    python gen_four_regime_map.py
Output: four_regime_map.pdf + .png  (vector + raster, committed alongside).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA

# --- house figure style ----------------------------------------------------------
from ave.viz import style

style.apply()  # print profile (white background)
print("figure style: print profile (white background)")

R1 = np.sqrt(2.0 * ALPHA)  # ~0.1208
R2 = np.sqrt(3.0) / 2.0    # ~0.866 (spin-2 sector)
R3 = 1.0

r = np.linspace(0.0, 1.0, 1000)
S = np.sqrt(1.0 - r**2)

fig, ax = plt.subplots(figsize=style.figsize("single"))
ax.set_xlim(0.0, 1.06)
ax.set_ylim(0.0, 1.05)
ax.set_xlabel(style.axis_label("Excitation operating point", "r = A/A_c", ""))
ax.set_ylabel(style.axis_label("Saturation factor", "S", ""))

# --- regime bands (canonical REGIME_COLORS) --------------------------------------
regimes = [
    (0.0, R1, style.REGIME_COLORS["I"], "I  Linear", "Maxwell / Newton"),
    (R1, R2, style.REGIME_COLORS["II"], "II  Nonlinear", "Axiom-4 curvature"),
    (R2, R3, style.REGIME_COLORS["III"], "III  Avalanche", r"Miller $M\!=\!1/S^2$"),
    (R3, 1.06, style.REGIME_COLORS["IV"], "IV  Ruptured", "topology destroyed"),
]
for lo, hi, color, name, sub in regimes:
    ax.axvspan(lo, hi, facecolor=color, edgecolor="none", alpha=0.45, zorder=0)
    xc = (lo + hi) / 2.0
    narrow = (hi - lo) < 0.16
    # Narrow bands (III Avalanche, IV Ruptured) get a vertical name low in the
    # band so it clears the arc + the r_2 boundary marker that sits at S=0.5.
    yname = 0.18 if narrow else 0.50
    ax.text(xc, yname, name, ha="center", va="center", fontsize=9,
            weight="bold", color=style.COLORS["data"],
            rotation=90 if narrow else 0)
    if not narrow:
        ax.text(xc, 0.40, sub, ha="center", va="center", fontsize=7.4,
                color=style.COLORS["data"])

# --- kernel arc ------------------------------------------------------------------
ax.plot(r, S, color=style.COLORS["ave"], lw=2.6, zorder=5,
        label=r"$S(r)=\sqrt{1-r^2}$")

# --- boundary markers ------------------------------------------------------------
# r_1 callout goes up (clear top whitespace); r_2 callout goes up-LEFT into the
# wide II band's empty upper region so it does not crowd the narrow III/IV bands;
# r_3 callout goes down-left so it clears the right edge.
boundary_specs = [
    (R1, r"$r_1=\sqrt{2\alpha}\approx%.4f$" % R1, (R1, np.sqrt(1 - R1**2) + 0.11), "center"),
    (R2, r"$r_2=\sqrt{3}/2\approx%.4f$ (spin-2)" % R2, (R2 - 0.05, 0.74), "right"),
    (R3, r"$r_3=1$", (R3 - 0.14, 0.10), "right"),
]
for rb, lab, xytext, ha in boundary_specs:
    Sb = np.sqrt(max(0.0, 1.0 - rb**2))
    ax.plot([rb], [Sb], marker="o", ms=6, color=style.COLORS["comparison"], zorder=6)
    ax.annotate(lab, xy=(rb, Sb), xytext=xytext,
                ha=ha, fontsize=7.8, color=style.COLORS["comparison"],
                arrowprops=dict(arrowstyle="->", color=style.COLORS["comparison"], lw=0.9))

style.legend(ax, where="below", ncol=1, fontsize=8.5)
out = style.save(fig, "four_regime_map.pdf")
print(f"wrote {[str(p) for p in out]}: r1={R1:.6f}, r2={R2:.6f}, r3={R3:.1f}")
