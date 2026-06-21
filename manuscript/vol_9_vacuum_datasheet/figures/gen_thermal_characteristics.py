#!/usr/bin/env python3
"""Generate the substrate thermal-characteristics figure for Vol 9 Ch 6 (3 panels).

Panel (a)  alpha^-1(T) running, SCHEMATIC. Only the SIGN + EXISTENCE of the
           running is a prediction: alpha^-1(T) < alpha^-1_ideal for T > 0 (the
           cold-lattice closed form 4*pi^3+pi^2+pi sits ABOVE the warm value, and
           thermal mode population drives it down). The MAGNITUDE delta_strain is a
           DEFINITIONAL RESIDUAL (1 - CODATA/alpha_cold), NOT a derivable thermal
           observable: Q-DELTA-MAP-1-quant is CLOSED NEGATIVE (FT-1 2026-05-31,
           ~31 OOM undershoot). So this panel shows the QUALITATIVE DIRECTION ONLY
           -- schematic ticks, no offset 6-digit y-axis that would falsely imply a
           derived alpha^-1(T) curve. Label: "sign/existence predicted; magnitude
           calibrated".

Panel (b)  E-mode vs B-mode Bose-Einstein occupation vs T. E-modes (gapless
           acoustic) populate thermally at any T>0; B-modes (Cosserat mass-gap
           hbar*omega_m ~ 1 MeV) are frozen by exp(-hbar*omega_m/k_B T) below
           T_B-gap ~ 1e10 K. The asymmetry is the Cosserat-Curie ASYM mechanism.

Panel (c)  Johnson-Nyquist noise floor S_v = 4 k_B T R vs T, at the two corpus
           operating points: (300 K, 1 kOhm) bench and (T_CMB, Z_0) cosmic.

Constants imported from canon (ave.core.constants). The cold-lattice alpha^-1
asymptote 4*pi^3+pi^2+pi is the canonical closed form (clm-0ktpcn). The CODATA
alpha^-1 is reached via 1/ALPHA but is NOT plotted as a derived magnitude on panel
(a) -- it is the calibrated empirical endpoint, and the schematic only carries the
SIGN of the warm <-> cold ordering, not a numeric delta.

Run:    PYTHONPATH=src ./.venv/bin/python gen_thermal_characteristics.py
Output: thermal_characteristics.{pdf,png}  (vector + raster, house style).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Resolve the repo's src/ so `ave` imports when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import K_B, Z_0  # noqa: E402
from ave.viz import style  # noqa: E402

style.apply()  # print profile, white background

# cold-lattice closed-form asymptote (clm-0ktpcn) -- used for the panel (a)
# annotation label only; NO numeric alpha^-1(T) magnitude is plotted (the
# magnitude is a definitional residual, Q-DELTA-MAP-1-quant CLOSED NEGATIVE).
T_CMB = 2.725                                          # K (reference)
T_B_GAP = 1.0e10                                       # K, hbar*omega_m/k_B ~ 1 MeV/k_B
HBAR_OMEGA_M_OVER_KB = T_B_GAP                         # B-mode mass-gap in K

fig, axes = plt.subplots(1, 3, figsize=style.figsize("wide"))

# === panel (a): alpha^-1(T) running -- SCHEMATIC, SIGN/EXISTENCE ONLY ==========
# We plot a UNITLESS schematic descent on a normalized vertical axis (1 = cold
# lattice, 0 = warm/calibrated), so the figure carries the predicted DIRECTION
# (alpha^-1 drops below the cold value as T rises) WITHOUT implying a derived
# alpha^-1(T) magnitude. No offset 6-digit numeric y-axis (the prior artifact).
axa = axes[0]
T = np.logspace(0.0, 11.0, 600)  # 1 K .. 1e11 K
ramp = np.clip(T / T_B_GAP, 0.0, None)
shape = ramp / (1.0 + ramp)            # linear at T<<T_B_gap, saturates past it
shape = shape / shape[np.searchsorted(T, T_B_GAP)]  # normalize: unity near the knee
descent = 1.0 - np.clip(shape, 0.0, 1.0)            # 1 at cold, -> ~0 past the knee

axa.plot(T, descent, color=style.COLORS["ave"], lw=2.2, linestyle="-",
         label=r"$\alpha^{-1}(T)$ (schematic)")
# cold-lattice level (top) and calibrated warm level (bottom) as schematic guides
axa.axhline(1.0, color=style.COLORS["accent"], lw=1.0, ls=":")
axa.axhline(0.0, color=style.COLORS["comparison"], lw=1.0, ls=":")
axa.axvline(T_B_GAP, color=style.COLORS["muted"], lw=1.0, ls="--")
axa.set_xscale("log")
# Schematic vertical axis: only the two qualitative levels are ticked, no numbers
# that would imply a derived magnitude.
axa.set_ylim(-0.12, 1.18)
axa.set_yticks([0.0, 1.0])
axa.set_yticklabels([r"warm (calibrated)", r"cold lattice $4\pi^3+\pi^2+\pi$"])
axa.tick_params(axis="y", labelsize=7.0)
axa.set_xlabel(style.axis_label("Temperature", "T", "K") + " (log)")
axa.set_ylabel(style.axis_label(r"$\alpha^{-1}$ running", "", "schematic"))
axa.text(2.0, 1.04, r"cold-lattice asymptote", fontsize=7.0, va="bottom",
         color=style.COLORS["accent"])
axa.text(2.0, -0.07, r"calibrated warm value", fontsize=7.0, va="top",
         color=style.COLORS["comparison"])
axa.text(T_B_GAP, 0.55, r"$T_{B\text{-}gap}\sim10^{10}$ K"+"\n(B-mode unfreeze)",
         fontsize=6.8, ha="right", color=style.COLORS["muted"])
# The load-bearing honesty statement (replaces the false-precision offset axis).
axa.text(0.5, -0.40,
         "sign/existence predicted; magnitude calibrated\n"
         r"($\alpha^{-1}(T)<\alpha^{-1}_{\rm ideal}$ for $T>0$; "
         r"$\delta_{\rm strain}$ is a definitional residual)",
         transform=axa.transAxes, fontsize=6.8, ha="center", va="top",
         color=style.COLORS["data"])

# === panel (b): E-mode vs B-mode occupation ====================================
axb = axes[1]
Tb = np.logspace(0.0, 11.5, 600)
# E-mode: gapless -> high-T classical occupation grows. Clamp the exponent to
# avoid expm1 overflow in the deep-frozen tail (the clamp only affects values
# already << 1e-12, off the plotted axis -- the frozen result is physical).
omega_E_K = 1.0e2  # small effective E-mode reference scale [K] (gapless illustration)
n_E = 1.0 / np.expm1(np.clip(omega_E_K / Tb, None, 700.0))
# B-mode: gapped at hbar*omega_m/k_B ~ T_B_gap
n_B = 1.0 / np.expm1(np.clip(HBAR_OMEGA_M_OVER_KB / Tb, None, 700.0))
axb.plot(Tb, n_E, color=style.COLORS["ave"], lw=2.2, linestyle="-",
         label="E-mode (gapless, thermal)")
axb.plot(Tb, n_B, color=style.COLORS["comparison"], lw=2.2, ls="--",
         label=r"B-mode (gapped $\hbar\omega_m{\sim}$1 MeV)")
axb.axvline(T_CMB, color=style.COLORS["accent"], lw=1.0, ls=":")
axb.axvline(T_B_GAP, color=style.COLORS["muted"], lw=1.0, ls="--")
axb.set_xscale("log")
axb.set_yscale("log")
axb.set_ylim(1e-12, 1e3)
axb.set_xlabel(style.axis_label("Temperature", "T", "K") + " (log)")
axb.set_ylabel(style.axis_label("Bose-Einstein occupation", r"\langle n \rangle", ""))
axb.text(T_CMB, 1e-10, r"$T_{CMB}$", fontsize=7.0, ha="center",
         color=style.COLORS["accent"])
axb.text(T_B_GAP, 1e-10, r"$T_{B\text{-}gap}$", fontsize=7.0, ha="right",
         color=style.COLORS["muted"])
style.legend(axb, where="below", ncol=1)

# === panel (c): Johnson-Nyquist floor ==========================================
axc = axes[2]
Tc = np.logspace(0.0, 3.0, 400)  # 1 K .. 1000 K
R_BENCH = 1.0e3   # 1 kOhm bench
Sv_bench = 4.0 * K_B * Tc * R_BENCH
Sv_cosmic = 4.0 * K_B * Tc * Z_0
axc.plot(Tc, Sv_bench, color=style.COLORS["ave"], lw=2.2, linestyle="-",
         label=r"$R=1$ k$\Omega$ (bench)")
axc.plot(Tc, Sv_cosmic, color=style.COLORS["accent"], lw=2.2, ls="--",
         label=r"$R=Z_0=376.7\,\Omega$ (cosmic)")
# corpus operating points
axc.plot([300.0], [4.0 * K_B * 300.0 * R_BENCH], marker="o", ms=7,
         color=style.COLORS["ave"], zorder=5)
axc.plot([T_CMB], [4.0 * K_B * T_CMB * Z_0], marker="o", ms=7,
         color=style.COLORS["accent"], zorder=5)
axc.set_xscale("log")
axc.set_yscale("log")
axc.set_xlabel(style.axis_label("Temperature", "T", "K") + " (log)")
axc.set_ylabel(style.axis_label("Noise PSD", r"S_v = 4 k_B T R", "V$^2$/Hz"))
axc.text(300.0, 4.0 * K_B * 300.0 * R_BENCH * 1.6, "300 K, 1 k$\\Omega$",
         fontsize=6.8, ha="right", color=style.COLORS["ave"])
axc.text(T_CMB, 4.0 * K_B * T_CMB * Z_0 * 1.6, r"$T_{CMB}$, $Z_0$",
         fontsize=6.8, ha="left", color=style.COLORS["accent"])
style.legend(axc, where="below", ncol=1)

out = Path(__file__).resolve().parent / "thermal_characteristics"
written = style.save(fig, out)
print(f"wrote {[str(p) for p in written]}: "
      f"panel (a) schematic (sign/existence only, no magnitude axis); "
      f"Sv(300K,1k)={4.0*K_B*300.0*R_BENCH:.3e}")
