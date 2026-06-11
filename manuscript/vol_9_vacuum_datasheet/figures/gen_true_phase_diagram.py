#!/usr/bin/env python3
"""Generate the substrate true-thermodynamic-phase-diagram figure for Vol 9 Ch 14.

Axes:   thermal occupation T (vertical, log)  x  bulk dilatation rho_bar (horizontal).
Phases: SOLID (K4-Cosserat crystal)  /  MELT (pre-geodesic plasma)  /  CAVITATED (candidate).
Lines:  melt line  T_melt = m_e c^2 / k_B          (CANONICAL; 02_absolute_maximum_ratings.tex:38,60)
        cavitation line  rho_bar_cav = -1/phi      (CANDIDATE, CONTESTED; cavitation_flow.py:62-64)
Path:   the Regime I->IV excitation map drawn as a TRAJECTORY WITHIN the solid (not an axis);
        its terminus r->1 (local rupture) lands ON the melt line (the BH-interior crossing).

All scalar thresholds derive from canonical constants (ave.core.constants); this script
hardcodes NO observable target. Run:  python gen_true_phase_diagram.py
Output: true_phase_diagram.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
# Imported from canon ONLY; NO hardcoded CODATA literals (the DAG anti-cheat scan
# src/scripts/vol_1_foundations/verify_universe.py forbids smuggled SM constants,
# and substrate-first-for-numbers requires every threshold to derive from canon).
from ave.core.constants import C_0, K_B, M_E, PHI

T_MELT = M_E * C_0**2 / K_B  # melt line: k_B T_melt = m_e c^2  -> ~5.93e9 K (CANONICAL)
RHO_CAV = -1.0 / PHI  # cavitation line: c_bulk^2 = 0 root     -> ~ -0.618 (CANDIDATE)
T_CMB = 2.725  # standard cosmic phase bath temperature [K] (reference marker)

# --- plane extents ---------------------------------------------------------------
RHO_MIN, RHO_MAX = -0.85, 0.50
T_MIN, T_MAX = 1.0, 1.0e11

fig, ax = plt.subplots(figsize=(8.2, 6.0))
ax.set_xlim(RHO_MIN, RHO_MAX)
ax.set_ylim(T_MIN, T_MAX)
ax.set_yscale("log")
ax.set_xlabel(r"bulk dilatation  $\bar{\rho}$  (mean compression / rarefaction)")
ax.set_ylabel(r"thermal occupation  $T$  [K]  (log)")

# --- phase regions ---------------------------------------------------------------
# SOLID: rho_bar > rho_cav AND T < T_melt
ax.add_patch(
    mpatches.Rectangle(
        (RHO_CAV, T_MIN), RHO_MAX - RHO_CAV, T_MELT - T_MIN,
        facecolor="#cfe3f7", edgecolor="none", zorder=0,
    )
)
# MELT: T > T_melt (full width)
ax.add_patch(
    mpatches.Rectangle(
        (RHO_MIN, T_MELT), RHO_MAX - RHO_MIN, T_MAX - T_MELT,
        facecolor="#f7d2c4", edgecolor="none", zorder=0,
    )
)
# CAVITATED (candidate): rho_bar < rho_cav, below the melt line
ax.add_patch(
    mpatches.Rectangle(
        (RHO_MIN, T_MIN), RHO_CAV - RHO_MIN, T_MELT - T_MIN,
        facecolor="#e6e6e6", edgecolor="none", hatch="xx", zorder=0,
    )
)

# --- failure lines ---------------------------------------------------------------
ax.axhline(T_MELT, color="#b22222", lw=2.4, zorder=4)  # melt line (canonical, solid)
ax.axvline(RHO_CAV, color="#555555", lw=2.0, ls="--", zorder=4)  # cavitation (candidate, dashed)

# --- phase labels ----------------------------------------------------------------
ax.text(0.30, 6.0e3, "SOLID\n(K4-Cosserat crystal)\nthe canonical AVE vacuum",
        ha="center", va="center", fontsize=10, weight="bold", color="#13406b")
ax.text(0.10, 2.6e10, "MELT  (pre-geodesic plasma)\nBH interior - parent medium - pre-K4 cosmos",
        ha="center", va="center", fontsize=9.5, weight="bold", color="#8a2b12")
ax.text(-0.75, 3.0e2, "CAVITATED /\nVAPOR\n(CANDIDATE)",
        ha="center", va="center", fontsize=8.5, weight="bold", color="#444444",
        rotation=90)

# --- failure-line annotations ----------------------------------------------------
ax.text(0.49, T_MELT * 0.30,
        r"melt line  $T_{melt}\!\approx\!5.93{\times}10^{9}$ K  ($k_BT\!=\!m_ec^2$)  -- CANONICAL",
        ha="right", va="top", fontsize=8.5, color="#b22222")
ax.text(RHO_CAV - 0.012, 8.0e6,
        r"cavitation line  $\bar{\rho}_{cav}\!=\!-1/\varphi\!\approx\!-0.618$  ($c_{bulk}^2\!=\!0$) -- CANDIDATE",
        ha="right", va="center", fontsize=8.5, color="#555555", rotation=90)

# --- standard cosmic operating point ---------------------------------------------
ax.plot([0.0], [T_CMB], marker="*", ms=15, color="#1b6b1b", zorder=6)
ax.annotate(r"standard cosmic phase  ($T_{CMB}=2.725$ K)",
            xy=(0.0, T_CMB), xytext=(0.10, 60),
            fontsize=8.5, color="#1b6b1b",
            arrowprops=dict(arrowstyle="->", color="#1b6b1b", lw=1.0))

# --- the excitation PATH (Regime I->IV) drawn WITHIN the solid --------------------
# A trajectory of local-strain excitation r=A/A_c: a path inside the solid region,
# NOT a thermodynamic axis. Its terminus r->1 (local rupture) lands on the melt line.
px = np.array([0.06, 0.05, 0.035, 0.015, 0.0])
py = np.array([2.0e2, 5.0e4, 8.0e6, 4.0e8, T_MELT])
ax.plot(px, py, color="#222222", lw=1.6, zorder=5)
ax.annotate("", xy=(px[-1], py[-1]), xytext=(px[-2], py[-2]),
            arrowprops=dict(arrowstyle="-|>", color="#222222", lw=1.6), zorder=5)
for (x, y, lab) in [
    (px[0], py[0], "I"), (px[1], py[1], "II"), (px[2], py[2], "III"), (px[3], py[3], "IV"),
]:
    ax.plot([x], [y], marker="o", ms=5, color="#222222", zorder=6)
    ax.text(x + 0.022, y, lab, fontsize=9, weight="bold", va="center", color="#222222")
ax.text(0.30, 2.0e8,
        "excitation path  $r=A/A_c$ : I$\\to$II$\\to$III$\\to$IV\n"
        "a TRAJECTORY within the solid, not an axis",
        ha="center", va="center", fontsize=8.5, style="italic", color="#222222")
ax.annotate("r$\\to$1 local rupture\n= melt (BH interior)",
            xy=(0.0, T_MELT), xytext=(-0.33, 1.4e8),
            fontsize=8, color="#8a2b12", ha="center",
            arrowprops=dict(arrowstyle="->", color="#8a2b12", lw=1.0))

ax.set_title("Substrate true thermodynamic phase diagram  (Vol 9 Ch 14, "
             "$\\S$ True Phase Diagram)", fontsize=11)
fig.tight_layout()
out = "true_phase_diagram.pdf"
fig.savefig(out)
print(f"wrote {out}: T_melt={T_MELT:.3e} K, rho_cav={RHO_CAV:.6f}, T_CMB={T_CMB} K")
