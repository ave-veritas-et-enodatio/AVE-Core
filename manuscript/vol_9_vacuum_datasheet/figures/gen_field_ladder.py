#!/usr/bin/env python3
"""Generate the two-threshold breakdown field-ladder figure for Vol 9 Ch 8.

A vertical log-field ladder locating the substrate's two breakdown field
thresholds and the lab-achievable operating band:

    E_yield = V_yield/l_node = sqrt(alpha)*E_S  ~ 1.13e17 V/m  (macroscopic onset)
    E_S     = V_snap/l_node  = m_e^2 c^3/(e hbar) ~ 1.32e18 V/m (Schwinger rupture)

The ratio E_S/E_yield = 1/sqrt(alpha) ~ 11.7 is the same axiomatic factor that
separates V_snap from V_yield. Lab-achievable fields (~1e10 V/m laser foci) sit
~7 OOM below E_yield (deep Regime I).

The three field bands carry the canonical REGIME_COLORS (ave.viz.style):
  below E_yield  -> Regime I (green, linear / all current devices)
  E_yield..E_S   -> Regimes II-III (orange caution: macroscopic nonlinear onset
                    through avalanche; this single band spans BOTH regimes, so it
                    takes the deeper-caution colour III)
  above E_S      -> Regime IV (vermillion, rupture / pair production)

ALL field values derive ONLY from canonical constants (ave.core.constants);
no CODATA/SM literal sits in the derivation path.

Run:    python gen_field_ladder.py
Output: field_ladder.pdf + .png  (vector + raster, committed alongside).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA, E_CRIT, E_YIELD

# --- house figure style ----------------------------------------------------------
from ave.viz import style

style.apply()  # print profile (white background)
print("figure style: print profile (white background)")

E_S = E_CRIT  # Schwinger pair-production critical field = V_snap/l_node (microscopic rupture)
RATIO = E_S / E_YIELD  # = 1/sqrt(alpha) ~ 11.7

# Lab-achievable reference (corpus magnitude, deep Regime I; feeds no threshold).
E_LAB = 1.0e10  # ultrafast laser foci [V/m]

fig, ax = plt.subplots(figsize=(5.6, 7.2))
ax.set_xlim(0.0, 1.0)
ax.set_ylim(1.0e9, 5.0e18)
ax.set_yscale("log")
ax.set_xticks([])
ax.set_ylabel(style.axis_label("Electric field", "E", "V/m") + "  (log)")

# --- regime backdrop bands (canonical REGIME_COLORS) -----------------------------
ax.axhspan(1.0e9, E_YIELD, facecolor=style.REGIME_COLORS["I"], edgecolor="none",
           alpha=0.40, zorder=0)
ax.axhspan(E_YIELD, E_S, facecolor=style.REGIME_COLORS["III"], edgecolor="none",
           alpha=0.40, zorder=0)
ax.axhspan(E_S, 5.0e18, facecolor=style.REGIME_COLORS["IV"], edgecolor="none",
           alpha=0.40, zorder=0)

ax.text(0.5, np.sqrt(1.0e9 * E_YIELD), "Regime I (linear)\nall current devices",
        ha="center", va="center", fontsize=8.5, color=style.COLORS["data"])
ax.text(0.5, np.sqrt(E_YIELD * E_S),
        "Regimes II-III\n(macroscopic\nnonlinear onset\n$\\to$ avalanche)",
        ha="center", va="center", fontsize=8.0, color=style.COLORS["data"])
ax.text(0.5, np.sqrt(E_S * 5.0e18), "Regime IV\n(rupture; pair\nproduction)",
        ha="center", va="center", fontsize=8.0, color=style.COLORS["data"])

# --- threshold lines -------------------------------------------------------------
ax.axhline(E_YIELD, color=style.COLORS["muted"], lw=2.4, zorder=4)
ax.text(0.02, E_YIELD * 1.18,
        r"$E_{yield}=\sqrt{\alpha}\,E_S\approx%.2f\times10^{17}$ V/m" % (E_YIELD / 1e17),
        ha="left", va="bottom", fontsize=8.2, color=style.COLORS["data"])
ax.text(0.98, E_YIELD * 0.82, "macroscopic nonlinear onset",
        ha="right", va="top", fontsize=7.6, color=style.COLORS["data"])

ax.axhline(E_S, color=style.COLORS["comparison"], lw=2.6, zorder=4)
ax.text(0.02, E_S * 1.18,
        r"$E_S=m_e^2c^3/(e\hbar)\approx%.2f\times10^{18}$ V/m" % (E_S / 1e18),
        ha="left", va="bottom", fontsize=8.2, color=style.COLORS["comparison"])
ax.text(0.98, E_S * 0.82, "Schwinger rupture (microscopic)",
        ha="right", va="top", fontsize=7.6, color=style.COLORS["comparison"])

# --- the axiomatic separation ----------------------------------------------------
ax.annotate("", xy=(0.80, E_S), xytext=(0.80, E_YIELD),
            arrowprops=dict(arrowstyle="<->", color=style.COLORS["data"], lw=1.4),
            zorder=5)
ax.text(0.83, np.sqrt(E_YIELD * E_S),
        r"$E_S/E_{yield}=1/\sqrt{\alpha}\approx%.1f$" % RATIO,
        ha="left", va="center", fontsize=8.0, color=style.COLORS["data"], rotation=90)

# --- lab-achievable marker -------------------------------------------------------
ax.plot([0.5], [E_LAB], marker="v", ms=9, color=style.COLORS["accent"], zorder=6)
ax.text(0.5, E_LAB * 1.7, r"lab foci $\sim10^{10}$ V/m ($\sim$7 OOM below $E_{yield}$)",
        ha="center", va="bottom", fontsize=7.6, color=style.COLORS["accent"])

out = style.save(fig, "field_ladder.pdf")
print(f"wrote {[str(p) for p in out]}: E_yield={E_YIELD:.4e}, E_S={E_S:.4e}, ratio={RATIO:.4f}")
