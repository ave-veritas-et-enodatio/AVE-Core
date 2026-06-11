#!/usr/bin/env python3
"""Generate the substrate true-thermodynamic-phase-diagram figure for Vol 9 Ch 14.

Axes:   thermal occupation T (vertical, log)  x  bulk dilatation rho_bar (horizontal).
Phases: SOLID (K4-Cosserat crystal)  /  MELT (pre-geodesic plasma)  /  CAVITATED (candidate).
Lines:  melt line  T_melt = m_e c^2 / k_B          (CANONICAL; 02_absolute_maximum_ratings.tex:38,60)
        cavitation line  rho_bar_cav = -1/phi      (CANDIDATE, CONTESTED; cavitation_flow.py:62-64)
Excit.: the Regime I->IV excitation r=A/A_c is a THIRD coordinate, orthogonal to BOTH
        plotted axes (driving r at a point raises neither bath-T nor rho_bar). It is drawn
        as a SEPARATE inset axis, NOT as a climb up the bath-T axis; the excursion is taken
        at a fixed bath state and local rupture at r->1 reaches the MELT phase at ANY bath T
        (the BH-interior crossing).

The two phase-boundary thresholds (T_melt, rho_cav) derive ONLY from canonical constants
(ave.core.constants); no fundamental/CODATA literal sits in their derivation path (the DAG
anti-cheat scan forbids smuggled SM constants). T_CMB is a non-load-bearing reference marker
for the standard cosmic operating point -- it feeds neither threshold.
Run:  python gen_true_phase_diagram.py
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
            xy=(0.0, T_CMB), xytext=(-0.15, 22), ha="right", va="center",
            fontsize=8.5, color="#1b6b1b",
            arrowprops=dict(arrowstyle="->", color="#1b6b1b", lw=1.0))

# --- the excitation COORDINATE r=A/A_c : a THIRD axis, orthogonal to the plane ------
# r is the Axiom-4 deviatoric/shear excitation amplitude. It is NOT a direction in this
# (T, rho_bar) plane: driving r at a point raises NEITHER the bath temperature T NOR the
# mean dilatation rho_bar. So it is drawn as a SEPARATE inset coordinate, NOT as a climb
# up the bath-T axis (the old climbing-path render re-encoded "regime = temperature", the
# exact conflation the chapter demotes). The excursion is taken at a FIXED bath state
# (here the cosmic operating point: T_CMB, rho_bar~0); local rupture at r->1 reaches the
# MELT phase locally -- at ANY bath T (the BH-interior crossing).

# (a) mark, on the main plane, WHERE r is driven: a fixed point; r runs into the page.
ax.annotate("local excitation $r$ driven here\n(into page $\\to$ inset)",
            xy=(0.0, T_CMB), xytext=(0.07, 7.5), fontsize=7.3, color="#222222",
            va="center", ha="left",
            arrowprops=dict(arrowstyle="->", color="#222222", lw=0.9))
# (b) the physical content of the terminus, stated on the plane WITHOUT a climbing path.
ax.text(-0.25, 4.0e6,
        "local rupture ($r\\to1$) reaches\nthe MELT phase at ANY bath $T$\n-- not a climb up this axis\n(see inset for the $r$ axis)",
        ha="center", va="center", fontsize=8.0, style="italic", color="#8a2b12")

# (c) inset: the excitation coordinate r as its OWN axis, orthogonal to (T, rho_bar).
axin = ax.inset_axes([0.55, 0.46, 0.42, 0.17])
axin.set_xlim(-0.04, 1.20)
axin.set_ylim(0.0, 1.0)
axin.set_yticks([])
axin.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
axin.tick_params(labelsize=6.5)
axin.set_facecolor("#fbf6df")
for spine in axin.spines.values():
    spine.set_edgecolor("#999999")
axin.set_xlabel("excitation  $r=A/A_c$  (3rd coord $\\perp\\,T,\\bar{\\rho}$; fixed bath state)",
                fontsize=7.0)
# r increases left->right with T and rho_bar held FIXED (a horizontal track, no bath-T climb)
axin.plot([0.0, 1.0], [0.5, 0.5], color="#222222", lw=1.5, zorder=2)
for rx, lab in [(0.10, "I"), (0.40, "II"), (0.68, "III"), (0.92, "IV")]:
    axin.plot([rx], [0.5], marker="o", ms=5, color="#222222", zorder=3)
    axin.text(rx, 0.80, lab, ha="center", va="center", fontsize=8, weight="bold", color="#222222")
# terminus r->1 -> into a MELT swatch (the phase reached, drawn off the r-axis end)
axin.add_patch(mpatches.Rectangle((1.0, 0.16), 0.18, 0.68, facecolor="#f7d2c4",
                                  edgecolor="#b22222", lw=1.0, zorder=1))
axin.annotate("", xy=(1.02, 0.5), xytext=(0.92, 0.5),
              arrowprops=dict(arrowstyle="-|>", color="#b22222", lw=1.6), zorder=4)
axin.text(1.09, 0.5, "MELT\nphase", ha="center", va="center", fontsize=6.4,
          weight="bold", color="#8a2b12")
axin.text(0.5, 0.05, "$r\\!\\to\\!1$ local rupture $\\to$ melt, at any bath $T$",
          ha="center", va="bottom", fontsize=6.2, color="#8a2b12")

ax.set_title("Substrate true thermodynamic phase diagram  (Vol 9 Ch 14, "
             "$\\S$ True Phase Diagram)", fontsize=11)
fig.tight_layout()
out = "true_phase_diagram.pdf"
# Omit the embedded CreationDate so the artifact is byte-for-byte reproducible
# (no wall-clock timestamp leaks into the committed PDF; supports the audit's
# deterministic-regeneration check).
fig.savefig(out, metadata={"CreationDate": None})
print(f"wrote {out}: T_melt={T_MELT:.3e} K, rho_cav={RHO_CAV:.6f}, T_CMB={T_CMB} K")
