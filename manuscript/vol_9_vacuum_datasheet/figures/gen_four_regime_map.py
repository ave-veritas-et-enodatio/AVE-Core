#!/usr/bin/env python3
"""Generate the four-regime S(r) map figure for Vol 9 Ch 14.

Plots the universal saturation kernel S(r)=sqrt(1-r^2) on the operating-point
(excitation) axis r=A/A_c, with the four universal regimes shaded and bounded by
r1=sqrt(2*alpha), r2=sqrt(3)/2 (spin-2 sector), r3=1:

    I   Linear      r < r1            S > 0.993
    II  Nonlinear   r1 <= r < r2      0.500 < S <= 0.993
    III Avalanche   r2 <= r < r3      0 < S <= 0.500
    IV  Ruptured    r >= r3 = 1       S = 0

This is the datasheet plot of the four-regime partition (tab:vol9_phase_*),
the excitation map of the solid phase (Ch 14 demotes it from the thermodynamic
phase diagram). r2=sqrt(3)/2 is the spin-2 sector value.

ALL boundary values derive ONLY from canonical constants (ave.core.constants).

Run:    python gen_four_regime_map.py
Output: four_regime_map.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA

R1 = np.sqrt(2.0 * ALPHA)  # ~0.1208
R2 = np.sqrt(3.0) / 2.0    # ~0.866 (spin-2 sector)
R3 = 1.0

r = np.linspace(0.0, 1.0, 1000)
S = np.sqrt(1.0 - r**2)

fig, ax = plt.subplots(figsize=(8.2, 5.4))
ax.set_xlim(0.0, 1.06)
ax.set_ylim(0.0, 1.05)
ax.set_xlabel(r"excitation operating point  $r = A/A_c$")
ax.set_ylabel(r"saturation factor  $S(r) = \sqrt{1 - r^2}$")

# --- regime bands ----------------------------------------------------------------
regimes = [
    (0.0, R1, "#cfe9d4", "I  Linear", "Maxwell / Newton"),
    (R1, R2, "#fdf2c4", "II  Nonlinear", "Axiom-4 curvature"),
    (R2, R3, "#fbd6b8", "III  Avalanche", r"Miller $M\!=\!1/S^2$"),
    (R3, 1.06, "#f4b4b4", "IV  Ruptured", "topology destroyed"),
]
for lo, hi, color, name, sub in regimes:
    ax.axvspan(lo, hi, facecolor=color, edgecolor="none", zorder=0)
    xc = (lo + hi) / 2.0
    ax.text(xc, 0.50, name, ha="center", va="center", fontsize=9,
            weight="bold", color="#333333", rotation=90 if (hi - lo) < 0.12 else 0)
    if (hi - lo) >= 0.12:
        ax.text(xc, 0.40, sub, ha="center", va="center", fontsize=7.4,
                color="#555555")

# --- kernel arc ------------------------------------------------------------------
ax.plot(r, S, color="#13406b", lw=2.6, zorder=5,
        label=r"$S(r)=\sqrt{1-r^2}$")

# --- boundary markers ------------------------------------------------------------
for rb, lab in [
    (R1, r"$r_1=\sqrt{2\alpha}\approx%.4f$" % R1),
    (R2, r"$r_2=\sqrt{3}/2\approx%.4f$ (spin-2)" % R2),
    (R3, r"$r_3=1$"),
]:
    Sb = np.sqrt(max(0.0, 1.0 - rb**2))
    ax.plot([rb], [Sb], marker="o", ms=6, color="#b22222", zorder=6)
    ax.annotate(lab, xy=(rb, Sb), xytext=(rb, Sb + 0.11),
                ha="center", fontsize=7.8, color="#7a1414",
                arrowprops=dict(arrowstyle="->", color="#7a1414", lw=0.9))

ax.set_title("Four-regime saturation map (Vol 9 Ch 14): "
             "the excitation map of the solid phase", fontsize=10.5)
ax.legend(loc="lower left", fontsize=8.5, framealpha=0.9)
fig.tight_layout()
out = "four_regime_map.pdf"
fig.savefig(out, metadata={"CreationDate": None})
print(f"wrote {out}: r1={R1:.6f}, r2={R2:.6f}, r3={R3:.1f}")
