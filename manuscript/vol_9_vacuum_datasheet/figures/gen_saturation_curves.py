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

The four-regime boundaries r1=sqrt(2*alpha), r2=sqrt(3)/2, r3=1 are marked.

ALL boundary values derive ONLY from canonical constants (ave.core.constants);
no CODATA/SM literal sits in the derivation path.

Run:    python gen_saturation_curves.py
Output: saturation_curves.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA

R1 = np.sqrt(2.0 * ALPHA)  # ~0.1208
R2 = np.sqrt(3.0) / 2.0    # ~0.866
R3 = 1.0

# r up to just shy of rupture (1/S diverges at r=1).
r = np.linspace(0.0, 0.985, 1000)
S = np.sqrt(1.0 - r**2)

curves = [
    (S,            r"$\varepsilon_{eff}/\varepsilon_0 = S$",              "#13406b", "-"),
    (1.0 / S,      r"$C_{eff}/C_0 = c_{EM}/c_0 = 1/S$",                    "#b22222", "-"),
    (np.sqrt(S),   r"$c_{shear}/c_0 = \sqrt{S}$",                         "#1b6b1b", "--"),
]

fig, ax = plt.subplots(figsize=(8.2, 5.4))
ax.set_xlim(0.0, 1.0)
ax.set_ylim(0.0, 4.0)
ax.set_xlabel(r"normalized operating point  $r = A_0/A_{yield}$")
ax.set_ylabel(r"effective parameter / cold-lattice value")

# --- four-regime boundary lines --------------------------------------------------
for rb, lab, ypos in [
    (R1, r"$r_1=\sqrt{2\alpha}$", 3.7),
    (R2, r"$r_2=\sqrt{3}/2$", 3.7),
    (R3, r"$r_3=1$", 3.7),
]:
    ax.axvline(rb, color="#999999", lw=1.0, ls=":", zorder=1)
    ax.text(rb, ypos, lab, ha="center", va="bottom", fontsize=8.0, color="#555555")

# --- characteristic curves -------------------------------------------------------
for y, lab, color, ls in curves:
    ax.plot(r, y, color=color, lw=2.4, ls=ls, label=lab, zorder=5)

# --- cold-lattice reference line -------------------------------------------------
ax.axhline(1.0, color="#cccccc", lw=1.0, zorder=0)

ax.set_title("Substrate operating-point characteristic curves "
             "(Vol 9 Ch 7, Table of saturation curves)", fontsize=10.5)
ax.legend(loc="upper left", fontsize=9.0, framealpha=0.9)
fig.tight_layout()
out = "saturation_curves.pdf"
fig.savefig(out, metadata={"CreationDate": None})
print(f"wrote {out}: r1={R1:.6f}, r2={R2:.6f}, r3={R3:.1f}")
