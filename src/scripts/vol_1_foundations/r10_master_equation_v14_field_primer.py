"""
R10 v14 Field Primer — what the simulation actually shows

Per Grant directive 2026-05-14 late evening (3rd):
  "what field or strain or what exactly is the image showing?
   what does simulation physically represent?"

This script generates a primer figure showing the SAME breathing-soliton
snapshot through 4 physically distinct lenses, with explicit labels on
what each plotted quantity IS:

  Panel 1: V (signed substrate potential)
    The Master Equation's primary state variable. Substrate-native.
    Colormap: diverging RdBu_r (red = +V, blue = −V).

  Panel 2: A(r) = |V|/V_yield (substrate strain ratio)
    The canonical substrate-native amplitude measure (dimensionless).
    A → 1 = saturation boundary onset. A → 0 = vacuum.
    Colormap: viridis.

  Panel 3: S(A) = √(1−A²) (Axiom 4 saturation kernel)
    The kernel modulating ε_eff and c_eff in the Master Equation.
    S → 1 = vacuum, S → 0 = saturation boundary.
    Colormap: plasma (collapse-near-boundary).

  Panel 4: n(r) = S(A)^(1/4) (substrate refractive index)
    Gravity-flavored representation. n < 1 inside the soliton =
    "compressed substrate" relative to vacuum.
    Colormap: magma.

Plus annotated legend explaining what each layer represents in different
observation-frame projections (EE / ME / GR / QFT / substrate-native).
"""
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.core.master_equation_fdtd import MasterEquationFDTD


print("=" * 78)
print("R10 v14 Field Primer — what the simulation shows")
print("=" * 78)
print()


# Configuration (same as v14 v2 canonical seed)
N = 32
DX = 1.0
V_YIELD = 1.0
PML = 4
CENTER = (N // 2, N // 2, N // 2)
SEED_AMP = 0.85
SEED_R = 2.5
N_STEPS_TO_HIGH_PHASE = 1175  # from v14 v2 run, this was the high-phase timestep

ZOOM_HALF = 7
ZOOM_LO = N // 2 - ZOOM_HALF
ZOOM_HI = N // 2 + ZOOM_HALF

OUT = REPO_ROOT / "assets" / "sim_outputs"


# Run to high-phase timestep
print(f"Running engine to high-phase moment (~step {N_STEPS_TO_HIGH_PHASE})...")
engine = MasterEquationFDTD(
    N=N, dx=DX, V_yield=V_YIELD, c0=1.0,
    pml_thickness=PML, A_cap=0.99, S_min=0.05,
)
engine.inject_localized_blob(
    center=CENTER, radius=SEED_R,
    amplitude=SEED_AMP * V_YIELD, profile="sech",
)
for _ in range(N_STEPS_TO_HIGH_PHASE):
    engine.step()
V_state = engine.V.copy()
V_peak = float(np.abs(V_state).max())
print(f"  V_peak at this moment = {V_peak:.4f}")
print()


# =============================================================================
# Compute the four fields
# =============================================================================
V_slice = V_state[ZOOM_LO:ZOOM_HI, ZOOM_LO:ZOOM_HI, CENTER[2]]
A_slice = np.abs(V_slice) / V_YIELD
A_clipped = np.minimum(A_slice, 0.99)
S_slice = np.sqrt(np.maximum(1.0 - A_clipped ** 2, 0.05))
n_slice = S_slice ** 0.25


# =============================================================================
# Generate the 4-panel field-interpretation figure
# =============================================================================
print("Generating 4-panel field primer figure...")

fig = plt.figure(figsize=(15, 13), facecolor="#0a0a0a")
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.25,
              height_ratios=[1.0, 1.0, 0.5])

extent = [ZOOM_LO, ZOOM_HI, ZOOM_LO, ZOOM_HI]
center_x = CENTER[0] + 0.5
center_y = CENTER[1] + 0.5

# Panel 1: V (signed substrate potential)
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_facecolor("#0f0f0f")
vmax_V = V_peak * 0.8
im1 = ax1.imshow(V_slice.T, origin="lower", cmap="RdBu_r",
                  extent=extent, aspect="equal",
                  vmin=-vmax_V, vmax=vmax_V)
ax1.plot(center_x, center_y, "*", color="cyan", ms=18,
         markeredgecolor="white", markeredgewidth=1.5)
ax1.set_title("Panel 1: V (substrate potential, signed)",
              color="white", fontsize=13, pad=10)
ax1.set_xlabel("x (cells)", color="white")
ax1.set_ylabel("y (cells)", color="white")
ax1.tick_params(colors="white")
for spine in ax1.spines.values():
    spine.set_color("#444")
cbar1 = plt.colorbar(im1, ax=ax1, fraction=0.045)
cbar1.set_label("V (substrate's intrinsic state)", color="white")
cbar1.ax.tick_params(colors="white")

# Panel 2: A = |V|/V_yield (substrate strain ratio)
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor("#0f0f0f")
im2 = ax2.imshow(A_slice.T, origin="lower", cmap="viridis",
                  extent=extent, aspect="equal",
                  vmin=0, vmax=1.0)
ax2.plot(center_x, center_y, "*", color="red", ms=18,
         markeredgecolor="white", markeredgewidth=1.5)
# Contour at A=0.5 (transition zone)
ax2.contour(A_slice.T, levels=[0.5, 0.9],
             colors=["#ffcc40", "#ff4040"], linewidths=[1.5, 2.5],
             extent=extent)
ax2.set_title("Panel 2: A = |V|/V_yield (substrate strain ratio)",
              color="white", fontsize=13, pad=10)
ax2.set_xlabel("x (cells)", color="white")
ax2.set_ylabel("y (cells)", color="white")
ax2.tick_params(colors="white")
for spine in ax2.spines.values():
    spine.set_color("#444")
cbar2 = plt.colorbar(im2, ax=ax2, fraction=0.045)
cbar2.set_label("A (1 = saturation boundary, 0 = vacuum)", color="white")
cbar2.ax.tick_params(colors="white")

# Panel 3: S(A) = √(1-A²) (saturation kernel)
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_facecolor("#0f0f0f")
im3 = ax3.imshow(S_slice.T, origin="lower", cmap="plasma",
                  extent=extent, aspect="equal",
                  vmin=0.05, vmax=1.0)
ax3.plot(center_x, center_y, "*", color="cyan", ms=18,
         markeredgecolor="white", markeredgewidth=1.5)
ax3.set_title("Panel 3: S(A) = √(1−A²)  (Axiom 4 saturation kernel)",
              color="white", fontsize=13, pad=10)
ax3.set_xlabel("x (cells)", color="white")
ax3.set_ylabel("y (cells)", color="white")
ax3.tick_params(colors="white")
for spine in ax3.spines.values():
    spine.set_color("#444")
cbar3 = plt.colorbar(im3, ax=ax3, fraction=0.045)
cbar3.set_label("S (1 = vacuum, 0 = Γ→−1 boundary)", color="white")
cbar3.ax.tick_params(colors="white")

# Panel 4: n(r) = S^(1/4) (substrate refractive index)
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_facecolor("#0f0f0f")
im4 = ax4.imshow(n_slice.T, origin="lower", cmap="magma",
                  extent=extent, aspect="equal",
                  vmin=0.5, vmax=1.0)
ax4.plot(center_x, center_y, "*", color="cyan", ms=18,
         markeredgecolor="white", markeredgewidth=1.5)
ax4.set_title("Panel 4: n(r) = S(A)^(1/4)  (substrate refractive index)",
              color="white", fontsize=13, pad=10)
ax4.set_xlabel("x (cells)", color="white")
ax4.set_ylabel("y (cells)", color="white")
ax4.tick_params(colors="white")
for spine in ax4.spines.values():
    spine.set_color("#444")
cbar4 = plt.colorbar(im4, ax=ax4, fraction=0.045)
cbar4.set_label("n (1 = vacuum, < 1 = compressed substrate)", color="white")
cbar4.ax.tick_params(colors="white")

# Panel 5 (bottom, spans both columns): explanatory text
ax5 = fig.add_subplot(gs[2, :])
ax5.axis("off")
explanation = (
    "WHAT THIS SIMULATION SHOWS:\n"
    "An AVE-canonical electron in substrate-native form. The Master Equation FDTD engine integrates the scalar nonlinear wave\n"
    "equation from Vol 1 Ch 4 (eq:master_wave) on a 3D K4 substrate lattice. The four panels above show the SAME instant of the\n"
    "SAME simulation through four physically distinct lenses:\n"
    "\n"
    "  Panel 1 (V):    The substrate's intrinsic state — the canonical AVE substrate variable. Signed, oscillates between + and −\n"
    "                  phases like AC voltage. In EE-projection this would be 'voltage'; in ME-projection this would be 'force';\n"
    "                  in GR-projection this would be 'metric perturbation'. But fundamentally V is just V (per App G vocabulary).\n"
    "\n"
    "  Panel 2 (A):    The substrate-native strain ratio A = |V|/V_yield. Dimensionless. A → 1 means local saturation (kernel\n"
    "                  collapse); A → 0 means vacuum. The yellow contour at A=0.5 is the transition zone; the red at A=0.9 is\n"
    "                  the Γ→−1 boundary onset. This IS the soliton's envelope.\n"
    "\n"
    "  Panel 3 (S):    The Axiom 4 saturation kernel S(A) = √(1−A²). Modulates the Master Equation's wave-speed coefficient.\n"
    "                  At S → 0 inside the soliton, c_eff diverges, the wave self-traps via impedance reflection (Γ → −1).\n"
    "\n"
    "  Panel 4 (n):    The substrate refractive index n = c₀/c_eff(V) = S(A)^(1/4). The GR-projection picture: matter compresses\n"
    "                  spacetime via the refractive index gradient (Vol 3 Ch 2:35 canonical, gravity-as-strain).\n"
    "\n"
    "PHYSICAL INTERPRETATION:\n"
    "The localized region of high |V| IS an electron in its substrate-native form (per doc 101 three-layer canonical: real-space\n"
    "unknot + SU(2) bundle + (2,3) phase-space winding). The breathing oscillation is the natural ω_Compton bulk-spin rate.\n"
    "The boundary at A→1 is the canonical Γ→−1 envelope with substrate-observable invariants 𝓜, 𝓠, 𝓙. Everything outside the\n"
    "yellow contour in Panel 2 is vacuum substrate. Everything inside is the electron itself — its physical extent in the substrate.\n"
    "\n"
    "This is the first time an AVE engine has autonomously hosted this bound state (per doc 113 Mode I PASS)."
)
ax5.text(0.01, 0.99, explanation, transform=ax5.transAxes,
         fontsize=10, family="monospace", verticalalignment="top",
         color="white",
         bbox=dict(boxstyle="round,pad=0.5", facecolor="#181818",
                    edgecolor="#444", alpha=0.95))

fig.suptitle(
    "Field primer: what the v14 visualization actually shows "
    "(same instant, four physical lenses)",
    color="white", fontsize=14, y=0.985
)

primer_path = OUT / "v14_field_primer.png"
plt.savefig(primer_path, dpi=160, facecolor="#0a0a0a", bbox_inches="tight")
print(f"  {primer_path}")
plt.close(fig)


# =============================================================================
# Summary
# =============================================================================
print()
print("=" * 78)
print("FIELD PRIMER COMPLETE")
print("=" * 78)
print(f"  Figure: {primer_path}")
print()
print("Four physical lenses on the same simulation:")
print(f"  V       (substrate potential, signed):       range [{V_slice.min():.3f}, {V_slice.max():.3f}]")
print(f"  A       (strain ratio |V|/V_yield):           range [0, {A_slice.max():.3f}]")
print(f"  S(A)    (saturation kernel √(1−A²)):          range [{S_slice.min():.3f}, {S_slice.max():.3f}]")
print(f"  n(r)    (refractive index S^(1/4)):           range [{n_slice.min():.3f}, {n_slice.max():.3f}]")
print()
print("V is the substrate's intrinsic state. A, S, n are derived quantities.")
print("The localized region of high |V| IS the canonical AVE electron in")
print("substrate-native form (doc 101 three-layer canonical).")
print("=" * 78)
