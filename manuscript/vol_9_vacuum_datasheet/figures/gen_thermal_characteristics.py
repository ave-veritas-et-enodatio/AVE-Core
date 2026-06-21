#!/usr/bin/env python3
"""Generate the substrate thermal-characteristics figure for Vol 9 Ch 6 (3 panels).

Panel (a)  alpha^-1(T) running: from the cold-lattice asymptote
           alpha^-1_ideal = 4*pi^3 + pi^2 + pi toward the CODATA value, across the
           linear-Cosserat-Curie regime, with the T_B-gap B-mode unfreezing knee.
           SCHEMATIC: the delta_strain MAGNITUDE is a DEFINITIONAL RESIDUAL
           (Q-DELTA-MAP-1-quant CLOSED NEGATIVE, FT-1 2026-05-31, ~31 OOM undershoot);
           the curve is anchored to the corpus delta_strain ~ 2.225e-6 endpoint and
           illustrates the SIGN + linear-then-unfreeze SHAPE, not a derived magnitude.

Panel (b)  E-mode vs B-mode Bose-Einstein occupation vs T. E-modes (gapless
           acoustic) populate thermally at any T>0; B-modes (Cosserat mass-gap
           hbar*omega_m ~ 1 MeV) are frozen by exp(-hbar*omega_m/k_B T) below
           T_B-gap ~ 1e10 K. The asymmetry is the Cosserat-Curie ASYM mechanism.

Panel (c)  Johnson-Nyquist noise floor S_v = 4 k_B T R vs T, at the two corpus
           operating points: (300 K, 1 kOhm) bench and (T_CMB, Z_0) cosmic.

Constants imported from canon (ave.core.constants). The cold-lattice alpha^-1
asymptote 4*pi^3+pi^2+pi is the canonical closed form (clm-0ktpcn); the CODATA
alpha^-1 is reached via 1/ALPHA (a calibration anchor, labeled as the empirical
endpoint, NOT a derived target).

Run:    python gen_thermal_characteristics.py
Output: thermal_characteristics.pdf  (vector, committed alongside this script).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical constants ---------------------------------------------------------
from ave.core.constants import ALPHA, K_B, Z_0

# cold-lattice closed-form asymptote (clm-0ktpcn)
ALPHA_INV_IDEAL = 4.0 * np.pi**3 + np.pi**2 + np.pi  # ~ 137.0363038
ALPHA_INV_CODATA = 1.0 / ALPHA                         # ~ 137.035999 (empirical endpoint)
T_CMB = 2.725                                          # K (reference)
T_B_GAP = 1.0e10                                       # K, hbar*omega_m/k_B ~ 1 MeV/k_B (corpus ~1e10)
HBAR_OMEGA_M_OVER_KB = T_B_GAP                         # B-mode mass-gap in K

fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.4))

# === panel (a): alpha^-1(T) running ============================================
axa = axes[0]
T = np.logspace(0.0, 11.0, 600)  # 1 K .. 1e11 K
# Linear-Cosserat-Curie rise anchored to the corpus endpoint at T_CMB, rolling
# over near T_B_GAP as B-modes unfreeze (SHAPE/SIGN illustration, not a magnitude
# derivation). delta(T) in [0,1] units of the total cold->CODATA gap.
ramp = np.clip(T / T_B_GAP, 0.0, None)
shape = ramp / (1.0 + ramp)            # linear at T<<T_B_gap, saturates past it
shape = shape / shape[np.searchsorted(T, T_B_GAP)]  # normalize: unity near the knee
delta_gap = ALPHA_INV_IDEAL - ALPHA_INV_CODATA      # total gap (cold above CODATA)
alpha_inv_T = ALPHA_INV_IDEAL - delta_gap * np.clip(shape, 0.0, 1.0)

axa.plot(T, alpha_inv_T, color="#13406b", lw=2.2)
axa.axhline(ALPHA_INV_IDEAL, color="#1b6b1b", lw=1.0, ls=":")
axa.axhline(ALPHA_INV_CODATA, color="#b22222", lw=1.0, ls=":")
axa.axvline(T_B_GAP, color="#999999", lw=1.0, ls="--")
axa.set_xscale("log")
axa.set_xlabel(r"temperature  $T$  [K]  (log)")
axa.set_ylabel(r"$\alpha^{-1}(T)$")
axa.text(2.0, ALPHA_INV_IDEAL, r"cold-lattice $4\pi^3+\pi^2+\pi$",
         fontsize=7.2, va="bottom", color="#1b6b1b")
axa.text(2.0, ALPHA_INV_CODATA, r"CODATA $\alpha^{-1}$ (anchor)",
         fontsize=7.2, va="top", color="#b22222")
axa.text(T_B_GAP, ALPHA_INV_IDEAL - 0.3 * delta_gap,
         r"$T_{B\text{-}gap}\sim10^{10}$ K"+"\n(B-mode unfreeze)",
         fontsize=6.8, ha="right", color="#555555")
axa.set_title(r"(a) $\alpha^{-1}(T)$ running"+"\n(SCHEMATIC: magnitude is a"
              +" definitional residual)", fontsize=8.6)

# === panel (b): E-mode vs B-mode occupation ====================================
axb = axes[1]
Tb = np.logspace(0.0, 11.5, 600)
# E-mode: gapless -> high-T classical occupation grows ~ linearly (illustrative,
# normalized); use Bose factor for a small reference frequency.
# Clamp the exponent to avoid expm1 overflow in the deep-frozen tail (huge
# exponent -> occupation underflows to 0, the physically correct frozen result);
# the clamp only affects values already << 1e-12 (off the plotted axis).
omega_E_K = 1.0e2  # small effective E-mode reference scale [K] (gapless illustration)
n_E = 1.0 / np.expm1(np.clip(omega_E_K / Tb, None, 700.0))
# B-mode: gapped at hbar*omega_m/k_B ~ T_B_gap
n_B = 1.0 / np.expm1(np.clip(HBAR_OMEGA_M_OVER_KB / Tb, None, 700.0))
axb.plot(Tb, n_E, color="#13406b", lw=2.2, label="E-mode (gapless, thermal)")
axb.plot(Tb, n_B, color="#b22222", lw=2.2, ls="--",
         label=r"B-mode (gapped $\hbar\omega_m{\sim}$1 MeV)")
axb.axvline(T_CMB, color="#1b6b1b", lw=1.0, ls=":")
axb.axvline(T_B_GAP, color="#999999", lw=1.0, ls="--")
axb.set_xscale("log")
axb.set_yscale("log")
axb.set_ylim(1e-12, 1e3)
axb.set_xlabel(r"temperature  $T$  [K]  (log)")
axb.set_ylabel(r"Bose-Einstein occupation  $\langle n \rangle$")
axb.text(T_CMB, 1e-10, r"$T_{CMB}$", fontsize=7.0, ha="center", color="#1b6b1b")
axb.text(T_B_GAP, 1e-10, r"$T_{B\text{-}gap}$", fontsize=7.0, ha="right", color="#555555")
axb.set_title("(b) E-mode vs B-mode occupation\n(Cosserat-Curie ASYM)", fontsize=8.6)
axb.legend(loc="lower right", fontsize=6.6, framealpha=0.9)

# === panel (c): Johnson-Nyquist floor ==========================================
axc = axes[2]
Tc = np.logspace(0.0, 3.0, 400)  # 1 K .. 1000 K
R_BENCH = 1.0e3   # 1 kOhm bench
Sv_bench = 4.0 * K_B * Tc * R_BENCH
Sv_cosmic = 4.0 * K_B * Tc * Z_0
axc.plot(Tc, Sv_bench, color="#13406b", lw=2.2, label=r"$R=1$ k$\Omega$ (bench)")
axc.plot(Tc, Sv_cosmic, color="#1b6b1b", lw=2.2, ls="--", label=r"$R=Z_0=376.7\,\Omega$ (cosmic)")
# corpus operating points
axc.plot([300.0], [4.0 * K_B * 300.0 * R_BENCH], marker="o", ms=7, color="#13406b", zorder=5)
axc.plot([T_CMB], [4.0 * K_B * T_CMB * Z_0], marker="o", ms=7, color="#1b6b1b", zorder=5)
axc.set_xscale("log")
axc.set_yscale("log")
axc.set_xlabel(r"temperature  $T$  [K]  (log)")
axc.set_ylabel(r"$S_v = 4 k_B T R$  [V$^2$/Hz]")
axc.text(300.0, 4.0 * K_B * 300.0 * R_BENCH * 1.6, "300 K, 1 k$\\Omega$",
         fontsize=6.8, ha="right", color="#13406b")
axc.text(T_CMB, 4.0 * K_B * T_CMB * Z_0 * 1.6, r"$T_{CMB}$, $Z_0$",
         fontsize=6.8, ha="left", color="#1b6b1b")
axc.set_title("(c) Johnson-Nyquist noise floor\n$S_v=4k_BTR$", fontsize=8.6)
axc.legend(loc="upper left", fontsize=6.8, framealpha=0.9)

fig.suptitle("Substrate temperature characteristics (Vol 9 Ch 6): "
             "Cosserat-Curie thermal-mode population", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.95))
out = "thermal_characteristics.pdf"
fig.savefig(out, metadata={"CreationDate": None})
print(f"wrote {out}: alpha_inv_ideal={ALPHA_INV_IDEAL:.7f}, "
      f"alpha_inv_codata={ALPHA_INV_CODATA:.7f}, "
      f"Sv(300K,1k)={4.0*K_B*300.0*R_BENCH:.3e}")
