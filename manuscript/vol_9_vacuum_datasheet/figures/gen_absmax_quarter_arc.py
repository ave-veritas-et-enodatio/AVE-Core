#!/usr/bin/env python3
"""Generate the Axiom-4 quarter-arc S(r) absolute-maximum-margin figure for Vol 9 Ch 2.

Plots the universal saturation kernel S(r)=sqrt(1-r^2) on the operating-point axis
r=A/A_c, with the four-regime bands shaded (r1=sqrt(2*alpha), r2=sqrt(3)/2, r3=1)
and the lab-achievable deep-Regime-I ratios marked (E/E_S, B/B_snap, T/T_melt).

The figure visualizes the absolute-maximum table (tab:vol9_absmax) + the operating-
margin section: every current laboratory operating point sits ~8 OOM below r3=1.

Regime bands use the canonical REGIME_COLORS convention (ave.viz.style),
single-sourced to four-regimes.md; boundaries r1/r2/r3 derive ONLY from canonical
constants (ave.core.constants). No CODATA/SM literal sits in the derivation path
(the DAG anti-cheat scan src/scripts/vol_1_foundations/verify_universe.py forbids
smuggled constants). The lab-achievable ratios are stated-in-corpus engineering
reference magnitudes (02_absolute_maximum_ratings.tex:72), drawn as illustrative
deep-Regime-I markers; they feed no threshold.

Run:    python gen_absmax_quarter_arc.py
Output: absmax_quarter_arc.pdf + .png  (vector + raster, committed alongside).
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

style.apply()  # print profile (white background) — prints the profile line below.
print("figure style: print profile (white background)")

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

fig, ax = plt.subplots(figsize=style.figsize("single"))
ax.set_xlim(0.0, 1.02)
ax.set_ylim(0.0, 1.04)
ax.set_xlabel(style.axis_label("Normalized operating point", "r = A/A_c", ""))
ax.set_ylabel(style.axis_label("Saturation factor", "S", ""))

# --- four-regime bands (canonical REGIME_COLORS) ---------------------------------
bands = [
    (0.0, R1, style.REGIME_COLORS["I"], "I\nLinear"),
    (R1, R2, style.REGIME_COLORS["II"], "II\nNonlinear"),
    (R2, R3, style.REGIME_COLORS["III"], "III\nAvalanche"),
]
for lo, hi, color, label in bands:
    ax.axvspan(lo, hi, facecolor=color, edgecolor="none", alpha=0.45, zorder=0)
    ax.text((lo + hi) / 2.0, 0.07, label, ha="center", va="bottom",
            fontsize=8.5, weight="bold", color=style.COLORS["data"])
# Regime IV is the rupture line r>=1 (S=0): a thin band at the right edge.
ax.axvspan(R3, 1.02, facecolor=style.REGIME_COLORS["IV"], edgecolor="none",
           alpha=0.45, zorder=0)

# --- the kernel arc --------------------------------------------------------------
ax.plot(r, S, color=style.COLORS["ave"], lw=2.6, zorder=5,
        label=r"Axiom-4 kernel $S(r)=\sqrt{1-r^2}$")

# --- boundary markers ------------------------------------------------------------
# r_2 sits at S=0.5; its annotation is nudged DOWN-LEFT (xytext below the marker)
# so it no longer collides with the r_1 callout that rides high on the arc.
boundary_specs = [
    (R1, r"$r_1=\sqrt{2\alpha}\approx%.4f$" % R1, (R1, np.sqrt(1 - R1**2) + 0.10), "center"),
    (R2, r"$r_2=\sqrt{3}/2\approx%.4f$" % R2, (R2 - 0.04, 0.36), "right"),
    (R3, r"$r_3=1$ (rupture)", (R3 - 0.13, 0.20), "right"),
]
for rb, lab, xytext, ha in boundary_specs:
    Sb = np.sqrt(max(0.0, 1.0 - rb**2))
    ax.plot([rb], [Sb], marker="o", ms=6, color=style.COLORS["comparison"], zorder=6)
    ax.annotate(lab, xy=(rb, Sb), xytext=xytext,
                ha=ha, fontsize=8.0, color=style.COLORS["comparison"],
                arrowprops=dict(arrowstyle="->", color=style.COLORS["comparison"], lw=0.9))

# --- deep-Regime-I lab-achievable markers ----------------------------------------
# The marker triangles ride at S~1 (top of the arc) where r is tiny; the text
# block is placed in the clear whitespace UNDER the arc (lower-left triangle) so
# it never overlaps the kernel curve.
for ratio, _ in LAB_MARKERS:
    Sr = np.sqrt(1.0 - ratio**2)
    ax.plot([ratio], [Sr], marker="v", ms=7, color=style.COLORS["accent"], zorder=7)
ystack = 0.60
ax.text(0.045, ystack + 0.052, "lab-achievable (deep Regime I, $S\\approx1$):",
        ha="left", va="center", fontsize=7.6, weight="bold", color=style.COLORS["accent"])
for _, lab in LAB_MARKERS:
    ax.text(0.045, ystack, lab, ha="left", va="center", fontsize=7.6,
            color=style.COLORS["accent"])
    ystack -= 0.052

style.legend(ax, where="below", ncol=1, fontsize=8.5)
out = style.save(fig, "absmax_quarter_arc.pdf")
print(f"wrote {[str(p) for p in out]}: r1={R1:.6f}, r2={R2:.6f}, r3={R3:.1f}")
