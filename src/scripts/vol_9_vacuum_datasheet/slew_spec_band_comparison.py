#!/usr/bin/env python3
"""Dark-sector response characterization — §1 THE SLEW SPEC + BAND COMPARISON.

Datasheet-style large-signal rate limit of the K4-TLM lattice, derived from
canonical `ave.core.constants` primitives ONLY (ave-canonical-source discipline).

THE DATASHEET SR (large-signal slew rate, op-amp analog):

    SR_max = V_yield * omega_node ,   omega_node = c0 / ell_node

    - V_yield  = sqrt(alpha) * V_snap        (Axiom-2/4 yield voltage, constants.py:409)
    - omega_node = c0 / ell_node             (the bond-LC / Compton angular rate;
                                              Vol-9 ch5 AC index: omega_C = c0/ell_node)

This is the MAXIMUM dV/dt the lattice can support: one full V_yield-sized swing
in one voxel-crossing time tau0 = ell_node/c0 (the gear tooth advancing once).
Op-amp datasheet analog: SR = (max output swing)/(min slew time).

ONSET / COMPRESSION (large-signal boundary, from the canonical varactor kernel,
NOT invented): the bond is a vacuum varactor C_eff(V) = C0/sqrt(1-(V/V_yield)^2)
(parametric-coupling-kernel.md:48; constants.py:465 small-signal eps_eff=eps0*S).
For a fixed charge-delivery current the achievable slew compresses as the
capacitance stiffens:

    SR(A) = SR_max * S(A) ,   S(A) = sqrt(1 - A^2) ,   A = V/V_yield  (= "r")

so the slew freezes to 0 at the rupture wall A->1 (the gear seizes), and the
small-signal<->large-signal boundary sits at the canonical regime-I limit
A = sqrt(2*alpha) ~ 0.1208 (four-regimes.md:26,33).

THE OTHER CANDIDATE (tagged, NOT the datasheet SR): the alpha-slew FLYWHEEL
refresh rate omega_slew = alpha * omega_node (parametric-coupling-kernel.md:52),
nu_slew = alpha * nu_node = 9.02e17 Hz. This is the substrate's intrinsic
SMALL-SIGNAL reactive refresh (the Schwinger a_e=alpha/2pi per-cycle reactive
leak of the electron LC tank), i.e. the op-amp GAIN-BANDWIDTH / unity-gain
analog, NOT the large-signal slew limit. Honest provenance note printed below.

BAND COMPARISON: the substrate frequency ceiling nu_node (substrate Nyquist
ceiling per Vol-9 ch5 AC index) vs LIGO ringdown / EHT variability / X-ray QPO
source-frame bands. Scaling chain stated in the doc + printed here.

Class tags: SR_max = derived-this-arc (from canonical V_yield, ell_node, c0);
the alpha-slew = canonical (parametric-coupling-kernel.md / dama-alpha-slew);
band edges = engineering-convention (observational literature, cited).
"""
from __future__ import annotations

import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- canonical-source discipline: import primitives, do NOT hard-code ---
import ave.core.constants as _avc
from ave.core.constants import ALPHA, C_0, L_NODE, V_SNAP, V_YIELD

assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
# cross-checks against canonical relations (6+ sig figs)
assert abs(V_YIELD / (np.sqrt(ALPHA) * V_SNAP) - 1.0) < 1e-9, "V_yield != sqrt(alpha)*V_snap"

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.normpath(
    os.path.join(HERE, "../../../research/figures/2026-06-11-dark-sector-response")
)
os.makedirs(FIGDIR, exist_ok=True)

# ----------------------------------------------------------------------
# §1.1 The datasheet SR and its companions (all forward from primitives)
# ----------------------------------------------------------------------
omega_node = C_0 / L_NODE                  # bond-LC / Compton angular rate [rad/s]
nu_node = omega_node / (2.0 * np.pi)       # substrate Nyquist ceiling [Hz]
tau0 = L_NODE / C_0                         # voxel tick (Compton time) [s]
SR_max = V_YIELD * omega_node              # THE DATASHEET SR [V/s]

# alpha-slew flywheel (tagged companion, NOT the datasheet SR)
omega_slew = ALPHA * omega_node            # parametric-coupling-kernel.md:52
nu_slew = ALPHA * nu_node                  # = alpha * nu_node
v_substrate = ALPHA * C_0 / (2.0 * np.pi)  # Gaia-demoted equilibrium velocity

# small-signal <-> large-signal boundary (canonical regime I limit)
A_onset = np.sqrt(2.0 * ALPHA)             # four-regimes.md:33


def S(A: np.ndarray) -> np.ndarray:
    """Universal saturation kernel S(A)=sqrt(1-A^2), A in [0,1)."""
    return np.sqrt(np.clip(1.0 - A**2, 0.0, 1.0))


print("=" * 72)
print("§1 SLEW SPEC — datasheet large-signal rate limit (forward from primitives)")
print("=" * 72)
print(f"  ell_node            = {L_NODE:.6e} m   (constants.py:239)")
print(f"  V_yield             = {V_YIELD/1e3:.4f} kV  (= sqrt(alpha)*V_snap)")
print(f"  tau0 = ell/c0       = {tau0:.6e} s   (voxel tick = Compton time)")
print(f"  omega_node = c0/ell = {omega_node:.6e} rad/s")
print(f"  nu_node             = {nu_node:.6e} Hz  (substrate Nyquist ceiling)")
print(f"  >>> SR_max = V_yield*omega_node = {SR_max:.6e} V/s   [DATASHEET SR]")
print(f"  small/large-signal boundary A_onset = sqrt(2*alpha) = {A_onset:.4f}")
print("-" * 72)
print("  COMPANION (tagged, NOT the datasheet SR): alpha-slew flywheel refresh")
print(f"  omega_slew = alpha*omega_node = {omega_slew:.6e} rad/s")
print(f"  nu_slew    = alpha*nu_node    = {nu_slew:.6e} Hz")
print(f"  v_substrate= alpha*c0/2pi     = {v_substrate/1e3:.2f} km/s (Gaia-DEMOTED)")
print("-" * 72)
print("  PROVENANCE FLAG (verify-before-cite): dama-alpha-slew-derivation.md:21")
print("  writes nu_slew = (alpha/2pi)*nu_Compton, which numerically = "
      f"{(ALPHA/(2*np.pi))*nu_node:.3e} Hz,")
print("  NOT the stated 9.02e17 Hz. The stated NUMBER matches nu_slew = alpha*nu_node")
print("  = omega_slew/2pi with omega_slew = alpha*omega_node (parametric-coupling-")
print("  kernel.md:52, authoritative + self-consistent). The '(alpha/2pi)' written")
print("  form is a 2pi notational slip; the angular primitive omega_slew=alpha*omega_node")
print("  is used here. FLAG surfaced, not silently reconciled.")

# ----------------------------------------------------------------------
# §1.2 Onset / compression curve SR(A) = SR_max * S(A)
# ----------------------------------------------------------------------
A = np.linspace(0.0, 0.999, 400)
SR_curve = SR_max * S(A)

csv_path = os.path.join(FIGDIR, "slew_compression_curve.csv")
with open(csv_path, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["A_strain", "S(A)", "SR_over_SRmax", "SR_V_per_s"])
    for a, sr in zip(A, SR_curve):
        w.writerow([f"{a:.5f}", f"{S(np.array([a]))[0]:.6f}",
                    f"{sr/SR_max:.6f}", f"{sr:.6e}"])
print(f"\n  wrote {csv_path}")

# ----------------------------------------------------------------------
# §1.3 Band comparison (observational, engineering-convention edges)
# ----------------------------------------------------------------------
# Source-frame bands [Hz, Hz] (conservative: source frame, no cosmo redshift).
bands = {
    "EHT variability\n(SMBH M87*/SgrA*)": (1e-5, 1e-2),   # min-day timescales
    "X-ray QPO\n(NS/BH binaries)": (1e-1, 1.25e3),        # up to ~1.25 kHz HF-QPO
    "LIGO ringdown\n(stellar-IM BH QNM)": (1e1, 1e4),     # source-scale strain rates
}
band_colors = {
    "EHT variability\n(SMBH M87*/SgrA*)": "#4c72b0",
    "X-ray QPO\n(NS/BH binaries)": "#55a868",
    "LIGO ringdown\n(stellar-IM BH QNM)": "#c44e52",
}

print("\n  BAND COMPARISON (substrate ceiling nu_node vs source-frame BH bands):")
for name, (lo, hi) in bands.items():
    oom_lo = np.log10(nu_node / hi)   # closest approach = ceiling vs band-high edge
    oom_hi = np.log10(nu_node / lo)
    tag = name.split("\n")[0]
    print(f"    {tag:28s} {lo:.1e}-{hi:.1e} Hz  -> ceiling is "
          f"{oom_lo:.1f}-{oom_hi:.1f} OOM above")
print("    => CLEAN NULL: substrate rate limit sits >=16 OOM above every band;")
print("       the lattice is NEVER slew-limited at any astrophysical BH frequency.")

# --- figure ---
fig, ax = plt.subplots(figsize=(12, 5.2))
for name, (lo, hi) in bands.items():
    ax.axvspan(lo, hi, color=band_colors[name], alpha=0.30, label=name)
    ax.text(np.sqrt(lo * hi), 0.82, name, ha="center", va="center",
            fontsize=8, transform=ax.get_xaxis_transform())

# substrate markers
ax.axvline(nu_slew, color="#8172b3", ls="--", lw=2)
ax.text(nu_slew, 0.40, f"  alpha-slew\n  refresh\n  {nu_slew:.2e} Hz",
        rotation=90, va="center", ha="right", fontsize=8, color="#5b4d8c",
        transform=ax.get_xaxis_transform())
ax.axvline(nu_node, color="black", ls="-", lw=2.5)
ax.text(nu_node, 0.40, f"  substrate ceiling\n  nu_node {nu_node:.2e} Hz",
        rotation=90, va="center", ha="right", fontsize=8.5, fontweight="bold",
        transform=ax.get_xaxis_transform())

ax.set_xscale("log")
ax.set_xlim(1e-6, 1e22)
ax.set_ylim(0, 1)
ax.set_yticks([])
ax.set_xlabel("frequency (source frame) [Hz]")
ax.set_title(
    "Dark-sector response §1 — lattice slew ceiling vs astrophysical BH bands\n"
    f"SR_max = V_yield·omega_node = {SR_max:.3e} V/s; "
    f"ceiling nu_node = {nu_node:.3e} Hz  >= 16 OOM above every band (CLEAN NULL)",
    fontsize=10,
)
ax.legend(loc="upper left", fontsize=7.5, framealpha=0.9)
fig.tight_layout()
band_fig = os.path.join(FIGDIR, "fig1_slew_band_comparison.png")
fig.savefig(band_fig, dpi=140)
print(f"\n  wrote {band_fig}")

# --- compression-curve figure ---
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(A, SR_curve / SR_max, color="#c44e52", lw=2.2,
         label=r"$SR(A)/SR_{max}=S(A)=\sqrt{1-A^2}$")
ax2.axvline(A_onset, color="#4c72b0", ls="--",
            label=fr"small/large-signal boundary $A=\sqrt{{2\alpha}}={A_onset:.3f}$ (universal)")
# NB: sqrt(3)/2 is the SPIN-2 / shear-sector avalanche-onset boundary
# (four-regimes.md:41,50). The slew DRIVE here is bond-LC longitudinal-V =
# SCALAR sector (ell_min=0), which has NO avalanche-onset boundary
# (four-regimes.md:48); the scalar-channel onset is V_yield (A=1). Drawn as a
# reference for the spin-2 sector only, NOT a boundary of THIS scalar curve.
ax2.axvline(np.sqrt(3) / 2, color="#dd8452", ls=":",
            label="$A=\\sqrt{3}/2$ — spin-2/shear avalanche onset\n"
                  "(reference only; NOT a scalar-channel boundary)")
ax2.axvline(1.0, color="black", ls="-", alpha=0.6,
            label=r"rupture = scalar onset $A=1$ ($V=V_{yield}$; slew freezes)")
ax2.set_xlabel(r"operating-point strain $A = V/V_{yield}$ (= $r$)")
ax2.set_ylabel(r"normalized slew $SR(A)/SR_{max}$")
ax2.set_title("§1 onset/compression — slew freezes at the wall (canonical varactor kernel)")
ax2.set_xlim(0, 1.0)
ax2.set_ylim(0, 1.02)
ax2.legend(fontsize=8, loc="lower left")
ax2.grid(alpha=0.3)
fig2.tight_layout()
comp_fig = os.path.join(FIGDIR, "fig1b_slew_compression.png")
fig2.savefig(comp_fig, dpi=140)
print(f"  wrote {comp_fig}")
print("\nDONE §1.")
