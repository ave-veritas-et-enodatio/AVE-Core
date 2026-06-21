#!/usr/bin/env python3
"""Generate the saturation characteristic-curve family figure for Vol 9 Ch 7.

Visualizes Table tab:vol9_saturation_curves: the substrate effective parameters
as functions of the normalized operating point r=A_0/A_yield, all following from
the single Axiom-4 kernel S(r)=sqrt(1-r^2):

    S(r)            = sqrt(1-r^2)        (softens to 0)
    eps_eff/eps_0   = S                  (T2 transverse permittivity; softens)
    C_eff/C_0       = 1/S                (A1 longitudinal compliance; stiffens)
    c_EM/c_0        = 1/S                (Maxwell phase velocity; diverges)
    c_shear/c_0     = sqrt(S)            (mechanical / rest-mass velocity; -> 0)

The four-regime boundaries r1=sqrt(2*alpha), r2=sqrt(3)/2, r3=1 are marked with
the canonical REGIME_COLORS bands (ave.viz.style, single-sourced to four-regimes.md).

CONTENT DISCLOSURE (audit fix). Two facts the prior render hid are now stated on
the figure rather than only in the LaTeX table (tab:vol9_saturation_curves):
  (1) C_eff/C_0 (A1 longitudinal compliance) and c_EM/c_0 (Maxwell phase velocity)
      are two PHYSICALLY DISTINCT reactances that happen to share the identical
      1/S trace — the single drawn "1/S" curve is BOTH, not one of them. Labelled
      as such so the co-incidence is disclosed, not silently merged.
  (2) alpha_eff/alpha_0 (the substrate-DISTINCT prediction) is the sixth tabulated
      quantity and is NOT plotted here precisely because it does NOT factor through
      S alone: under SYM-class saturation it is exactly 1 at every r; under ASYM
      it deviates sector-dependently. A note records this so the figure does not
      read as "everything is an S-curve" — the one quantity that breaks the
      S-family is the falsifiable one, and its absence is intentional, not an
      omission.

ALL boundary values derive ONLY from canonical constants (ave.core.constants);
no CODATA/SM literal sits in the derivation path.

Run:    python gen_saturation_curves.py
Output: saturation_curves.pdf + .png  (vector + raster, committed alongside).
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
R2 = np.sqrt(3.0) / 2.0    # ~0.866
R3 = 1.0

# r up to just shy of rupture (1/S diverges at r=1).
r = np.linspace(0.0, 0.985, 1000)
S = np.sqrt(1.0 - r**2)

# The 1/S trace is BOTH C_eff/C_0 (A1 compliance) AND c_EM/c_0 (Maxwell velocity):
# two distinct reactances that coincide on this curve. Disclosed in the label.
curves = [
    (S,            r"$\varepsilon_{eff}/\varepsilon_0 = S$  (T2 permittivity, softens)",
     style.COLORS["ave"], "-"),
    (1.0 / S,      r"$C_{eff}/C_0 = c_{EM}/c_0 = 1/S$  (two reactances coincide)",
     style.COLORS["comparison"], "-"),
    (np.sqrt(S),   r"$c_{shear}/c_0 = \sqrt{S}$  (rest-mass velocity)",
     style.COLORS["accent"], "--"),
]

fig, ax = plt.subplots(figsize=style.figsize("single"))
ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.0, 4.0)
ax.set_xlabel(style.axis_label("Normalized operating point", "r = A_0/A_{yield}", ""))
ax.set_ylabel(style.axis_label("Effective parameter / cold-lattice value", "", ""))

# --- four-regime boundary lines, tinted with the canonical REGIME band colours ---
# Faint band fills behind the curves keep the regime convention visible without
# competing with the line data; the vertical boundary lines are the precise marks.
band_spans = [
    (0.0, R1, "I"),
    (R1, R2, "II"),
    (R2, R3, "III"),
]
for lo, hi, key in band_spans:
    ax.axvspan(lo, hi, facecolor=style.REGIME_COLORS[key], edgecolor="none",
               alpha=0.16, zorder=0)
for rb, lab in [
    (R1, r"$r_1=\sqrt{2\alpha}$"),
    (R2, r"$r_2=\sqrt{3}/2$"),
    (R3, r"$r_3=1$"),
]:
    ax.axvline(rb, color=style.COLORS["muted"], lw=1.0, ls=":", zorder=1)
    ax.text(rb, 3.7, lab, ha="center", va="bottom", fontsize=8.0,
            color=style.COLORS["muted"])

# --- characteristic curves -------------------------------------------------------
for y, lab, color, ls in curves:
    ax.plot(r, y, color=color, lw=2.4, ls=ls, label=lab, zorder=5)

# --- cold-lattice reference line -------------------------------------------------
ax.axhline(1.0, color=style.COLORS["muted"], lw=1.0, ls="-", alpha=0.5, zorder=0)

# --- DISCLOSURE note: the sixth quantity that does NOT factor through S ----------
ax.text(
    0.035, 0.30,
    "Not plotted: "
    r"$\alpha_{eff}/\alpha_0$" "\n"
    "does NOT factor through $S$\n"
    "(SYM: $=1\\ \\forall r$; ASYM: deviates)\n"
    "— the substrate-distinct line.\n"
    "See Tab. of saturation curves\n"
    "+ Ch. 15 (Falsification).",
    ha="left", va="center", fontsize=7.0, color=style.COLORS["data"],
    bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
              edgecolor=style.COLORS["muted"], lw=0.7, alpha=0.92),
    zorder=8,
)

style.legend(ax, where="below", ncol=1, fontsize=8.0)
out = style.save(fig, "saturation_curves.pdf")
print(f"wrote {[str(p) for p in out]}: r1={R1:.6f}, r2={R2:.6f}, r3={R3:.1f}")
