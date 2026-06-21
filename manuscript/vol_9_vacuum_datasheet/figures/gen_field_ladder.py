#!/usr/bin/env python3
"""Generate the two-threshold breakdown field-ladder figure for Vol 9 Ch 8.

A vertical log-field ladder locating the substrate's two breakdown field
thresholds and the lab-achievable operating band:

    E_yield = V_yield/l_node = sqrt(alpha)*E_S  ~ 1.13e17 V/m  (macroscopic onset)
    E_S     = V_snap/l_node  = m_e^2 c^3/(e hbar) ~ 1.32e18 V/m (Schwinger rupture)

The ratio E_S/E_yield = 1/sqrt(alpha) ~ 11.7 is the same axiomatic factor that
separates V_snap from V_yield. Lab-achievable fields (~1e10 V/m laser foci) sit
~7 OOM below E_yield (deep Regime I).

ALL field values derive ONLY from canonical constants (ave.core.constants);
no CODATA/SM literal sits in the derivation path.

Run:    python gen_field_ladder.py
Output: field_ladder.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA, E_CRIT, E_YIELD

E_S = E_CRIT  # Schwinger pair-production critical field = V_snap/l_node (microscopic rupture)
RATIO = E_S / E_YIELD  # = 1/sqrt(alpha) ~ 11.7

# Lab-achievable reference (corpus magnitude, deep Regime I; feeds no threshold).
E_LAB = 1.0e10  # ultrafast laser foci [V/m]

fig, ax = plt.subplots(figsize=(5.6, 7.2))
ax.set_xlim(0.0, 1.0)
ax.set_ylim(1.0e9, 5.0e18)
ax.set_yscale("log")
ax.set_xticks([])
ax.set_ylabel(r"electric field  $E$  [V/m]  (log)")

# --- regime backdrop: deep Regime I band up to E_yield --------------------------
ax.axhspan(1.0e9, E_YIELD, facecolor="#cfe9d4", edgecolor="none", zorder=0)
ax.axhspan(E_YIELD, E_S, facecolor="#fbd6b8", edgecolor="none", zorder=0)
ax.axhspan(E_S, 5.0e18, facecolor="#f4b4b4", edgecolor="none", zorder=0)

ax.text(0.5, np.sqrt(1.0e9 * E_YIELD), "Regime I (linear)\nall current devices",
        ha="center", va="center", fontsize=8.5, color="#1b5e2a")
ax.text(0.5, np.sqrt(E_YIELD * E_S), "Regime II-III\n(macroscopic\nnonlinear onset\n$\\to$ avalanche)",
        ha="center", va="center", fontsize=8.0, color="#8a4b12")
ax.text(0.5, np.sqrt(E_S * 5.0e18), "Regime IV\n(rupture; pair\nproduction)",
        ha="center", va="center", fontsize=8.0, color="#8a1212")

# --- threshold lines -------------------------------------------------------------
ax.axhline(E_YIELD, color="#b8860b", lw=2.4, zorder=4)
ax.text(0.02, E_YIELD * 1.18,
        r"$E_{yield}=\sqrt{\alpha}\,E_S\approx%.2f\times10^{17}$ V/m" % (E_YIELD / 1e17),
        ha="left", va="bottom", fontsize=8.2, color="#7a5a08")
ax.text(0.98, E_YIELD * 0.82, "macroscopic nonlinear onset",
        ha="right", va="top", fontsize=7.6, color="#7a5a08")

ax.axhline(E_S, color="#b22222", lw=2.6, zorder=4)
ax.text(0.02, E_S * 1.18,
        r"$E_S=m_e^2c^3/(e\hbar)\approx%.2f\times10^{18}$ V/m" % (E_S / 1e18),
        ha="left", va="bottom", fontsize=8.2, color="#7a1414")
ax.text(0.98, E_S * 0.82, "Schwinger rupture (microscopic)",
        ha="right", va="top", fontsize=7.6, color="#7a1414")

# --- the axiomatic separation ----------------------------------------------------
ax.annotate("", xy=(0.80, E_S), xytext=(0.80, E_YIELD),
            arrowprops=dict(arrowstyle="<->", color="#333333", lw=1.4), zorder=5)
ax.text(0.83, np.sqrt(E_YIELD * E_S),
        r"$E_S/E_{yield}=1/\sqrt{\alpha}\approx%.1f$" % RATIO,
        ha="left", va="center", fontsize=8.0, color="#333333", rotation=90)

# --- lab-achievable marker -------------------------------------------------------
ax.plot([0.5], [E_LAB], marker="v", ms=9, color="#1b6b1b", zorder=6)
ax.text(0.5, E_LAB * 1.7, r"lab foci $\sim10^{10}$ V/m ($\sim$7 OOM below $E_{yield}$)",
        ha="center", va="bottom", fontsize=7.6, color="#1b6b1b")

ax.set_title("Two-threshold breakdown field ladder\n(Vol 9 Ch 8)", fontsize=10.5)
fig.tight_layout()
out = "field_ladder.pdf"
fig.savefig(out, metadata={"CreationDate": None})
print(f"wrote {out}: E_yield={E_YIELD:.4e}, E_S={E_S:.4e}, ratio={RATIO:.4f}")
