#!/usr/bin/env python3
"""Generate the Axiom-4 quarter-arc S(r) absolute-maximum-margin figure for Vol 9 Ch 2.

Plots the universal saturation kernel S(r)=sqrt(1-r^2) on the operating-point axis
r=A/A_c, with the four-regime bands shaded (r1=sqrt(2*alpha), r2=sqrt(3)/2, r3=1)
and the lab-achievable deep-Regime-I ratios marked (E/E_S, B/B_snap, T/T_melt).

The figure visualizes the absolute-maximum table (tab:vol9_absmax) + the operating-
margin section: every current laboratory operating point sits ~8 OOM below r3=1.

ALL boundary values derive ONLY from canonical constants (ave.core.constants);
no CODATA/SM literal sits in the derivation path (the DAG anti-cheat scan
src/scripts/vol_1_foundations/verify_universe.py forbids smuggled constants).
The lab-achievable ratios are stated-in-corpus engineering reference magnitudes
(02_absolute_maximum_ratings.tex:72), drawn as illustrative deep-Regime-I markers;
they feed no threshold.

Run:    python gen_absmax_quarter_arc.py
Output: absmax_quarter_arc.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA

R1 = np.sqrt(2.0 * ALPHA)  # Regime I/II boundary: Delta-S = alpha  -> sqrt(2*alpha) ~ 0.1208
R2 = np.sqrt(3.0) / 2.0    # Regime II/III boundary (spin-2 sector): Q=1/S=2  -> sqrt(3)/2 ~ 0.866
R3 = 1.0                   # Regime III/IV rupture: S -> 0

# Lab-achievable deep-Regime-I reference ratios (corpus magnitudes,
# 02_absolute_maximum_ratings.tex:72; illustrative markers, feed no threshold).
LAB_MARKERS = [
    (1.0e-8, r"$E/E_S\sim10^{-8}$ (laser foci)"),
    (1.0e-8, r"$B/B_{snap}\sim10^{-8}$ (lab magnets)"),
    (1.0e-3, r"$T/T_{melt}\sim10^{-3}$ (HIC fireball)"),
]

# --- kernel arc ------------------------------------------------------------------
r = np.linspace(0.0, 1.0, 1000)
S = np.sqrt(1.0 - r**2)

fig, ax = plt.subplots(figsize=(8.2, 5.4))
ax.set_xlim(0.0, 1.02)
ax.set_ylim(0.0, 1.04)
ax.set_xlabel(r"normalized operating point  $r = A/A_c$")
ax.set_ylabel(r"saturation factor  $S(r) = \sqrt{1 - r^2}$")

# --- four-regime bands -----------------------------------------------------------
bands = [
    (0.0, R1, "#cfe9d4", "I\nLinear"),
    (R1, R2, "#fdf2c4", "II\nNonlinear"),
    (R2, R3, "#fbd6b8", "III\nAvalanche"),
]
for lo, hi, color, label in bands:
    ax.axvspan(lo, hi, facecolor=color, edgecolor="none", zorder=0)
    ax.text((lo + hi) / 2.0, 0.07, label, ha="center", va="bottom",
            fontsize=8.5, weight="bold", color="#333333")
# Regime IV is the rupture line r>=1 (S=0): a thin band at the right edge.
ax.axvspan(R3, 1.02, facecolor="#f4b4b4", edgecolor="none", zorder=0)

# --- the kernel arc --------------------------------------------------------------
ax.plot(r, S, color="#13406b", lw=2.6, zorder=5,
        label=r"Axiom-4 kernel $S(r)=\sqrt{1-r^2}$")

# --- boundary markers ------------------------------------------------------------
for rb, lab in [
    (R1, r"$r_1=\sqrt{2\alpha}\approx%.4f$" % R1),
    (R2, r"$r_2=\sqrt{3}/2\approx%.4f$" % R2),
    (R3, r"$r_3=1$ (rupture)"),
]:
    Sb = np.sqrt(max(0.0, 1.0 - rb**2))
    ax.plot([rb], [Sb], marker="o", ms=6, color="#b22222", zorder=6)
    ax.annotate(lab, xy=(rb, Sb), xytext=(rb, Sb + 0.10),
                ha="center", fontsize=8.0, color="#7a1414",
                arrowprops=dict(arrowstyle="->", color="#7a1414", lw=0.9))

# --- deep-Regime-I lab-achievable markers ----------------------------------------
ystack = 0.96
for ratio, lab in LAB_MARKERS:
    Sr = np.sqrt(1.0 - ratio**2)
    ax.plot([ratio], [Sr], marker="v", ms=7, color="#1b6b1b", zorder=7)
    ax.text(0.045, ystack, lab, ha="left", va="center", fontsize=7.6, color="#1b6b1b")
    ystack -= 0.052
ax.text(0.045, 0.96 + 0.052, "lab-achievable (deep Regime I, $S\\approx1$):",
        ha="left", va="center", fontsize=7.6, weight="bold", color="#1b6b1b")

ax.set_title("Axiom-4 saturation kernel: four-regime operating margin "
             "(Vol 9 Ch 2, Absolute Maximum Ratings)", fontsize=10.5)
ax.legend(loc="lower left", fontsize=8.5, framealpha=0.9)
fig.tight_layout()
out = "absmax_quarter_arc.pdf"
fig.savefig(out, metadata={"CreationDate": None})
print(f"wrote {out}: r1={R1:.6f}, r2={R2:.6f}, r3={R3:.1f}")
