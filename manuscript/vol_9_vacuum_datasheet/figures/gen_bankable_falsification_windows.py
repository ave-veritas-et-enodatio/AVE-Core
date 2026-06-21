#!/usr/bin/env python3
"""Generate the two BANKABLE forward-prediction falsification-window figures (Vol 9 Ch 15).

The Ch 15 Forward-Prediction Register (chord-vs-echo) carries two BANKABLE rows --
forced dimensionless ratios that give SM/GR-divergent observable numbers at existing
or near-term instruments. This driver renders the falsification windows for both.

Panel A -- Iron-Kalpha disk edge.  AVE saturation-boundary horizon r_sat = 7GM/c^2
           (= 3.5 r_s) vs GR ISCO at 6GM/c^2.  The discriminator is the inner
           accretion-disk edge via X-ray Fe-Kalpha reflection / kHz QPOs (a MATTER
           observable; NOT the GR-standard photon ring, which AVE keeps at 3GM/c^2).
           Canonical: divergence-test-substrate-map.md:143 (C1-BH-RING).

Panel B -- g_* effective-DOF cutoff.  AVE g_* = 7^3/4 = 343/4 = 85.75 vs SM 106.75.
           Three observable consequences: Omega_GW +7.6% (LISA/DECIGO),
           EW expansion rate -10.4% (CMB-S4), EW latent heat -20% (FCC-ee/CEPC).
           Canonical: divergence-test-substrate-map.md:245,247 (C12-G-STAR).

ALL plotted numbers are PURE DIMENSIONLESS forced ratios (7, 6, 3, 343/4, 106.75,
+7.6%, -10.4%, -20%) -- NO CODATA literal, NO engine constant sits in any plotted
quantity (these are the FORCED-RATIO chords of the form-vs-value frame; their being
dimensionless is exactly why they are bankable). Deterministic: re-running regenerates
the identical PDF.

Run:  python gen_bankable_falsification_windows.py
Output: bankable_falsification_windows.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- forced dimensionless ratios (the bankable chords; no CODATA, no engine const) ---
R_SAT_AVE = 7.0       # AVE saturation-boundary horizon  r_sat = 7 GM/c^2  (= 3.5 r_s)
R_ISCO_GR = 6.0       # GR innermost stable circular orbit  r_isco = 6 GM/c^2
R_PHOTON = 3.0        # photon sphere -- GR-standard, AVE-IDENTICAL (not a discriminator)
R_S = 2.0             # Schwarzschild radius  r_s = 2 GM/c^2  (reference)

G_STAR_AVE = 343.0 / 4.0   # 7^3 / 4 = 85.75   (AVE effective-DOF cutoff)
G_STAR_SM = 106.75         # Standard Model effective DOF at the EW scale

fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.0, 4.6))

# ===================== Panel A: Iron-Kalpha disk edge ============================
# Radial schematic in units of GM/c^2.  Concentric markers at the characteristic radii.
ax = axA
ax.set_aspect("equal")
lim = 8.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

# central BH
ax.add_patch(plt.Circle((0, 0), R_S, color="black", zorder=5))
ax.text(0, 0, "BH", color="white", ha="center", va="center", fontsize=8, zorder=6)

# characteristic radii as circles
circ_specs = [
    (R_PHOTON, "0.6", "--", r"photon sphere $3GM/c^2$ (GR$\equiv$AVE)"),
    (R_ISCO_GR, "tab:blue", "-", r"GR ISCO $6GM/c^2$"),
    (R_SAT_AVE, "tab:red", "-", r"AVE $r_{\mathrm{sat}}=7GM/c^2$ ($=3.5\,r_s$)"),
]
for r, c, ls, lab in circ_specs:
    ax.add_patch(plt.Circle((0, 0), r, fill=False, edgecolor=c, ls=ls, lw=1.8, zorder=3, label=lab))

# the discriminating WINDOW between 6 and 7 GM/c^2 (the matter disk-edge separation)
theta = np.linspace(0, 2 * np.pi, 200)
ax.fill(
    np.concatenate([R_ISCO_GR * np.cos(theta), R_SAT_AVE * np.cos(theta[::-1])]),
    np.concatenate([R_ISCO_GR * np.sin(theta), R_SAT_AVE * np.sin(theta[::-1])]),
    color="tab:red", alpha=0.13, zorder=2,
)
ax.annotate(
    "disk-edge\nwindow\n$\\Delta r = GM/c^2$",
    xy=(0, 6.5), xytext=(4.6, 6.6), fontsize=8, ha="left",
    arrowprops=dict(arrowstyle="->", color="tab:red", lw=1.0),
)
ax.set_title("(A) Iron-K$\\alpha$ disk edge: AVE $7GM/c^2$ vs GR ISCO $6GM/c^2$", fontsize=9)
ax.set_xlabel("radius [$GM/c^2$]", fontsize=8)
ax.legend(loc="lower left", fontsize=6.6, framealpha=0.9)
ax.tick_params(labelsize=7)

# ===================== Panel B: g_* effective-DOF band ===========================
ax = axB
labels = ["AVE\n$g_*=7^3/4$", "SM\n$g_{*,SM}$"]
vals = [G_STAR_AVE, G_STAR_SM]
colors = ["tab:red", "tab:blue"]
bars = ax.bar(labels, vals, color=colors, alpha=0.82, width=0.55, zorder=3)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 1.5, f"{v:.2f}", ha="center", fontsize=8.5)

# the 24-DOF gap window
ax.annotate(
    "",
    xy=(0, G_STAR_AVE), xytext=(0, G_STAR_SM),
    arrowprops=dict(arrowstyle="<->", color="0.3", lw=1.2),
)
ax.text(
    0.06, (G_STAR_AVE + G_STAR_SM) / 2,
    f"$\\Delta g_*={G_STAR_SM - G_STAR_AVE:.2f}$\n(24 fewer\nfermionic DOF)",
    fontsize=7.6, va="center", ha="left",
)
ax.set_ylim(0, 122)
ax.set_ylabel("effective relativistic DOF $g_*$ (EW scale)", fontsize=8)
ax.set_title("(B) $g_*$ cutoff: AVE $85.75$ vs SM $106.75$", fontsize=9)
ax.tick_params(labelsize=7.5)

# observable consequences box
obs = (
    r"Consequences ($g_* = 85.75$ vs $106.75$):"
    "\n"
    r"  $\Omega_{GW}\ +7.6\%$  (LISA / DECIGO)"
    "\n"
    r"  EW expansion $-10.4\%$  (CMB-S4)"
    "\n"
    r"  EW latent heat $-20\%$  (FCC-ee / CEPC)"
)
ax.text(
    0.97, 0.97, obs, transform=ax.transAxes, fontsize=6.8, va="top", ha="right",
    bbox=dict(boxstyle="round", facecolor="0.95", edgecolor="0.6"),
)

fig.suptitle(
    "Vol 9 Ch 15 -- BANKABLE forward-prediction falsification windows (forced dimensionless ratios)",
    fontsize=10,
)
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig("bankable_falsification_windows.pdf")
print("[fig] wrote bankable_falsification_windows.pdf")
