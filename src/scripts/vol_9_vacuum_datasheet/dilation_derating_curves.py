#!/usr/bin/env python3
"""Dark-sector response characterization — §3 THE DILATION CURVES (derating style).

The THREE canonical sector speeds (substrate-temporal-values-definition.md:28-30;
cavitation_flow.py EOS), rendered as datasheet derating curves:

    c_EM    = c0 (1 - A^2)^(-1/2)            RISES  (-> inf at A->1)   [Maxwell phase / alpha-speed]
    c_shear = c0 (1 - A^2)^(+1/4)            FREEZES (-> 0  at A->1)   [matter clock; tracks Schwarzschild]
    c_bulk  = c0 sqrt(1 + rho/(1 - rho^2))   FREEZES at rho_cav=-1/phi [compressional; cavitation floor]

OBSERVED-FREQUENCY TRANSFER FUNCTIONS (the redshift a signal carries out of a
saturated region; clock-rate ratio source/observer, substrate-temporal-values:40-42):

    H_shear(A^2) = omega_shear/omega0 = (1-A^2)^(+1/4)   (spectral-line gravitational redshift)
    H_EM(A^2)    = omega_EM/omega0    = (1-A^2)^(-1/2)   (EM phase advances FASTER)
    H_bulk(rho)  = omega_bulk/omega0  = sqrt(1+rho/(1-rho^2))

c_shear/SCHWARZSCHILD TRACKING made quantitative: c_shear/c0 = (1-A^2)^(1/4)
== sqrt(1 - rs/r)  (operators.md:56; temporal-values:29).

c_EM-RISES CONSEQUENCE — surfaced for the BH matrix, NOT resolved here: the
matter clock (shear) gives the standard spectral-line redshift (1-A^2)^(1/4),
but the EM PHASE speed RISES (1-A^2)^(-1/2). What a rising EM phase speed near
saturation does to imaging (lensing/shadow) is a genuine open question for the
BH matrix; this script quantifies both channels and flags the divergence.

Class tags: three speeds = canonical (rendered); transfer functions =
derived-this-arc (redshift factors from canonical clock-rate forms);
Schwarzschild tracking = canonical identity rendered.
"""
from __future__ import annotations

import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import ave.core.constants as _avc
from ave.core.constants import PHI

# RHO_CAV lives in cavitation_flow.py, NOT constants.py (registry R8) — import canonically
from ave.core.cavitation_flow import RHO_CAV

assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
assert abs(RHO_CAV - (-1.0 / PHI)) < 1e-12, "RHO_CAV != -1/phi"

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.normpath(
    os.path.join(HERE, "../../../research/figures/2026-06-11-dark-sector-response")
)
os.makedirs(FIGDIR, exist_ok=True)

# ----------------------------------------------------------------------
# §3.1 three sector speeds vs operating point
# ----------------------------------------------------------------------
A2 = np.linspace(0.0, 0.999, 500)
cEM = (1.0 - A2) ** (-0.5)          # /c0
cShear = (1.0 - A2) ** (0.25)       # /c0
# bulk uses its own variable rho in [rho_cav, +0.95]
rho = np.linspace(RHO_CAV + 1e-4, 0.95, 500)
cBulk2 = 1.0 + rho / (1.0 - rho**2)
cBulk = np.sqrt(np.clip(cBulk2, 0.0, None))  # /c0

print("=" * 72)
print("§3.1 three sector speeds (/c0)   rho_cav = -1/phi = %.6f" % RHO_CAV)
print("=" * 72)
for a2 in (0.0, 0.117, 0.5, 0.9, 0.99):
    print(f"  A^2={a2:5.3f} | c_EM={(1-a2)**-0.5:7.3f}  c_shear={(1-a2)**0.25:6.4f}")
print(f"  c_bulk(rho=0)      = {np.sqrt(1+0/(1-0)):.4f}")
print(f"  c_bulk(rho=+0.5)   = {np.sqrt(1+0.5/(1-0.25)):.4f}  (stiffens)")
print(f"  c_bulk(rho_cav)    = {np.sqrt(max(0,1+RHO_CAV/(1-RHO_CAV**2))):.4f}  (FREEZES at floor)")

csv1 = os.path.join(FIGDIR, "three_speed_split.csv")
with open(csv1, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["A2", "cEM_over_c0", "cShear_over_c0"])
    for i in range(len(A2)):
        w.writerow([f"{A2[i]:.5f}", f"{cEM[i]:.6f}", f"{cShear[i]:.6f}"])
csv1b = os.path.join(FIGDIR, "bulk_speed_vs_rho.csv")
with open(csv1b, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["rho_bar", "cBulk_over_c0"])
    for i in range(len(rho)):
        w.writerow([f"{rho[i]:.5f}", f"{cBulk[i]:.6f}"])
print(f"  wrote {csv1}, {csv1b}")

# ----------------------------------------------------------------------
# §3.2 observed-frequency transfer functions per channel
# ----------------------------------------------------------------------
H_shear = (1.0 - A2) ** (0.25)     # spectral-line redshift (matter clock)
H_EM = (1.0 - A2) ** (-0.5)        # EM phase advances faster
H_bulk = cBulk                     # omega_bulk/omega0 = c_bulk/c0 (same factor)

csv2 = os.path.join(FIGDIR, "observed_frequency_transfer.csv")
with open(csv2, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["A2", "H_shear_redshift", "H_EM_phase"])
    for i in range(len(A2)):
        w.writerow([f"{A2[i]:.5f}", f"{H_shear[i]:.6f}", f"{H_EM[i]:.6f}"])
print(f"  wrote {csv2}")
print("\n§3.2 transfer functions (omega_observed/omega_source):")
for a2 in (0.117, 0.5, 0.9):
    print(f"  A^2={a2:4.2f} | shear(redshift)={(1-a2)**0.25:.4f}  EM(phase)={(1-a2)**-0.5:.4f}")

# ----------------------------------------------------------------------
# §3.3 c_shear / Schwarzschild tracking made quantitative
# ----------------------------------------------------------------------
x = np.linspace(1.001, 8.0, 400)               # r/rs
cShear_of_r = np.sqrt(1.0 - 1.0 / x)           # = (1-A^2)^(1/4) with S=1-rs/r
schwarz = np.sqrt(1.0 - 1.0 / x)               # GR c*sqrt(1-rs/r)
track_err = np.max(np.abs(cShear_of_r - schwarz))
print(f"\n§3.3 c_shear(r)/c0 vs Schwarzschild sqrt(1-rs/r): max|diff| = {track_err:.2e} (identity)")

# ----------------------------------------------------------------------
# §3.4 c_EM-rises imaging flag (surfaced, not resolved)
# ----------------------------------------------------------------------
print("\n§3.4 c_EM-RISES FLAG (for BH matrix, NOT resolved here):")
print("  spectral-line redshift rides the SHEAR matter clock -> (1-A^2)^(1/4) (drops);")
print("  the EM PHASE speed RISES -> (1-A^2)^(-1/2). At A^2=0.9: line x0.562, EM-phase x3.162.")
print("  What a rising EM phase speed near saturation does to lensing/shadow imaging is")
print("  a genuine OPEN question -> surfaced to the BH matrix (shadow/lensing row).")

# ----------------------------------------------------------------------
# figure: the three-speed split IS the figure
# ----------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16.5, 5))

ax = axes[0]
ax.plot(A2, cEM, color="#c44e52", lw=2.4, label=r"$c_{EM}=c_0(1-A^2)^{-1/2}$ (RISES)")
ax.plot(A2, cShear, color="#4c72b0", lw=2.4,
        label=r"$c_{shear}=c_0(1-A^2)^{1/4}$ (FREEZES, matter clock)")
ax.axhline(1.0, color="gray", ls=":", lw=1)
ax.set_xlabel(r"operating-point $A^2$")
ax.set_ylabel(r"speed $/c_0$")
ax.set_title("§3.1 three-speed split (EM rises, shear freezes)")
ax.set_ylim(0, 5)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(rho, cBulk, color="#55a868", lw=2.4, label=r"$c_{bulk}=c_0\sqrt{1+\bar\rho/(1-\bar\rho^2)}$")
ax.axvline(RHO_CAV, color="black", ls="--", alpha=0.7,
           label=fr"$\bar\rho_{{cav}}=-1/\varphi={RHO_CAV:.3f}$ (freeze floor)")
ax.axhline(1.0, color="gray", ls=":", lw=1)
ax.set_xlabel(r"bulk density $\bar\rho$")
ax.set_ylabel(r"$c_{bulk}/c_0$")
ax.set_title(r"§3.1 bulk speed — freezes at cavitation floor, stiffens at compression")
ax.set_ylim(0, 4)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)

ax = axes[2]
ax.plot(A2, H_shear, color="#4c72b0", lw=2.4,
        label=r"$H_{shear}=(1-A^2)^{1/4}$ (line redshift)")
ax.plot(A2, H_EM, color="#c44e52", lw=2.4,
        label=r"$H_{EM}=(1-A^2)^{-1/2}$ (phase BLUE)")
ax.axhline(1.0, color="gray", ls=":", lw=1)
ax.set_xlabel(r"source-region $A^2$")
ax.set_ylabel(r"$\omega_{observed}/\omega_{source}$")
ax.set_title("§3.2 per-channel transfer fn (c_EM-rises FLAG)")
ax.set_ylim(0, 4)
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)

fig.suptitle(
    "Dark-sector response §3 — dilation derating curves  "
    "[shear=matter clock freezes; EM phase rises; bulk freezes at -1/phi]  from constants.py",
    fontsize=11,
)
fig.tight_layout(rect=(0, 0, 1, 0.96))
out = os.path.join(FIGDIR, "fig3_dilation_derating.png")
fig.savefig(out, dpi=140)
print(f"\n  wrote {out}")
print("DONE §3.")
