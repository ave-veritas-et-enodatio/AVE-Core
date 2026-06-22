#!/usr/bin/env python3
r"""
Membrane Phase Buffering: Cholesterol as a Topological LLCP Wedge
=================================================================

Demonstrates the AVE-native mechanism by which cholesterol phase-buffers
biological membranes at the K=2G structural yield boundary.

ALL curves derived from the AVE universal operators:
  - Op2: universal_saturation()   — Axiom 4 non-linear kernel
  - Op3: universal_reflection()   — impedance boundary Gamma
  - Op14: universal_dynamic_impedance() — Z_eff under strain

NO Boltzmann sigmoids, NO tanh, NO empirical fitting.

Cooperative Amplification Derivation
-------------------------------------
The cooperative phase transition is governed by the EDGE COUNT of the
coordination polyhedron x an isotropic 3D projection factor:

  n = E_edges x D/(D-1) = 6 x 3/2 = 9

where:
  E_edges = 6 (tetrahedral H-bond network: 4 vertices, 6 edges)
  D = 3     (3D space)
  D/(D-1) = 3/2  (isotropic projection of 2-body pairwise correlation)

Cross-validation: T_c(water) = E_HB / (9 x k_B) ~ 5.1 C
  -> Matches the +4 C density anomaly within ~1.1 C.

Cholesterol Mechanism
---------------------
Cholesterol's sp3 4-ring wedge raises the effective yield limit by
the FCC packing fraction phi:
  A_yield_eff = 1 + phi ~ 1.7405
  T_c_buffered = T_c x (1 + phi) ~ 484 K ~ 211 C

This pushes the catastrophic snap far outside biological range,
keeping the membrane permanently at the K=2G yield threshold.

Output
------
Saved to assets/sim_outputs/cholesterol_topological_phase_buffer.png

Run: PYTHONPATH=src python src/scripts/vol_5_biology/simulate_membrane_llcp.py

Ported from the Applied-Vacuum-Engineering archive; restyled to the AVE
white manuscript house style (ave.viz.style, Okabe-Ito).
"""

import matplotlib

import numpy as np

from ave.core.constants import (
    N_PHI_PACK,   # FCC packing fraction phi ~ 0.7405
    N_VOID_FRAC,  # Void fraction (1-phi) ~ 0.2595
    K_B,          # Boltzmann constant [J/K]
    e_charge,     # Elementary charge [C]
    Z_0,          # Vacuum impedance [Ohm]
)
from ave.core.universal_operators import (
    universal_saturation,
    universal_reflection,
    universal_dynamic_impedance,
)
from ave.viz import style
from ave_path_util import sim_output

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# =============================================================================
# Derived constants (all from engine + Op4 derivation, zero engineering magic)
# =============================================================================

# H-bond energy: E_HB = U_raw x (1-phi) = 0.8317 x 0.2595 ~ 0.2158 eV
# (Op4 raw bond depth U_raw is derived in Vol 5, Ch 2, Eqs. 12-14; the void-
#  fraction factor (1-phi) is the canonical N_VOID_FRAC.)
_U_RAW_EV = 0.8317  # Op4 raw H-bond depth [eV] (Vol 5 Ch 2 derivation)
E_HB_EV = _U_RAW_EV * N_VOID_FRAC
E_HB_J = E_HB_EV * e_charge

# Cooperative amplification: n = E_edges x D/(D-1) = 6 x 3/2 = 9
# Tetrahedral coordination polyhedron: 4 vertices, 6 edges, 4 faces.
N_EDGES_TETRA = 6
D_SPATIAL = 3
N_COOPERATIVE = N_EDGES_TETRA * D_SPATIAL / (D_SPATIAL - 1)  # = 9

# Cooperative yield temperature: T_c = E_HB / (n x k_B)
T_C_WATER = E_HB_J / (N_COOPERATIVE * K_B)  # ~ 278.3 K ~ 5.1 C

# Cholesterol buffering: sp3 wedge raises effective yield by phi.
A_YIELD_PURE = 1.0                    # Normalised yield (A = 1 at T_c)
A_YIELD_BUFFERED = 1.0 + N_PHI_PACK   # ~ 1.7405


def compute_membrane_response(T_kelvin, A_yield):
    """Compute the membrane impedance response at temperature T.

    The strain amplitude captures the cooperative thermal disruption:
      A(T) = n_cooperative x k_B x T / E_HB
    normalised by A_yield (= 1 for pure lipid, 1+phi for cholesterol-buffered).
    """
    A = N_COOPERATIVE * K_B * T_kelvin / E_HB_J
    A_norm = A / A_yield
    S = universal_saturation(A_norm, 1.0)          # Op2: S = sqrt(1 - (A/A_yield)^2)
    Z_eff = universal_dynamic_impedance(Z_0, S)    # Op14: Z_eff = Z_0 / sqrt(S)
    Gamma = universal_reflection(Z_0, Z_eff)       # Op3: Gamma = (Z_eff-Z_0)/(Z_eff+Z_0)
    return {
        "saturation": S,
        "impedance_ratio": Z_eff / Z_0,
        "reflection": Gamma,
        "strain": A,
    }


def generate_llcp_simulation():
    """Generate the membrane LLCP phase-buffer visualisation."""

    # Temperature sweep: -20 C to +80 C (wide enough to see the transition).
    T_celsius = np.linspace(-20, 80, 600)
    T_kelvin = T_celsius + 273.15

    pure = compute_membrane_response(T_kelvin, A_YIELD_PURE)
    buffered = compute_membrane_response(T_kelvin, A_YIELD_BUFFERED)

    T_c_celsius = T_C_WATER - 273.15

    # --- Plotting: white house style, Okabe-Ito ---
    style.apply()
    fig, axes = plt.subplots(1, 3, figsize=style.figsize("wide"))

    c_pure = style.COLORS["comparison"]   # vermillion — pure lipid
    c_buf = style.COLORS["accent"]        # bluish-green — cholesterol-buffered
    c_ref = style.COLORS["muted"]         # gray — reference guides

    # Panel 1: Cooperative Strain A(T)
    ax = axes[0]
    ax.plot(T_celsius, pure["strain"], color=style.COLORS["ave"], lw=2.0,
            label=r"$A(T) = 9\,k_B T / E_{HB}$")
    ax.axhline(A_YIELD_PURE, color=c_pure, ls="--", lw=1.3,
               label=r"$A_{yield}^{pure} = 1.0$")
    ax.axhline(A_YIELD_BUFFERED, color=c_buf, ls="--", lw=1.3,
               label=r"$A_{yield}^{chol} = 1+\phi = %.4f$" % A_YIELD_BUFFERED)
    ax.axvline(T_c_celsius, color=c_ref, ls=":", lw=1.2,
               label=r"$T_c = %.1f\,^\circ$C" % T_c_celsius)
    ax.axvline(37, color=c_ref, ls="-.", lw=1.0, label=r"Body temp 37 $^\circ$C")
    ax.set_xlabel(style.axis_label("Temperature", "T", r"$^\circ$C"))
    ax.set_ylabel(style.axis_label("Cooperative strain", r"A", ""))
    ax.set_ylim(0, 2.5)
    style.legend(ax, where="below", ncol=2, fontsize=7)

    # Panel 2: Saturation Factor S(T)
    ax = axes[1]
    ax.plot(T_celsius, pure["saturation"], color=c_pure, lw=2.0,
            label=r"Pure membrane ($A_{yield}=1$)")
    ax.plot(T_celsius, buffered["saturation"], color=c_buf, lw=2.4,
            label=r"Cholesterol buffered ($A_{yield}=1+\phi$)")
    ax.axhline(N_PHI_PACK, color=c_ref, ls=":", lw=1.2,
               label=r"$\phi = %.4f$" % N_PHI_PACK)
    ax.axvline(T_c_celsius, color=c_ref, ls=":", lw=1.0)
    ax.axvline(37, color=c_ref, ls="-.", lw=1.0)
    ax.set_xlabel(style.axis_label("Temperature", "T", r"$^\circ$C"))
    ax.set_ylabel(style.axis_label("Saturation factor", "S(T)", ""))
    ax.set_ylim(-0.05, 1.05)
    ax.text(60, 0.85, r"$V_I$ ordered (LC lattice)", color=c_buf, fontsize=8)
    ax.text(-15, 0.12, r"$V_{II}$ fluid (disordered)", color=c_pure, fontsize=8)
    style.legend(ax, where="below", ncol=1, fontsize=7)

    # Panel 3: Reflection Coefficient |Gamma|(T)
    ax = axes[2]
    ax.plot(T_celsius, np.abs(pure["reflection"]), color=c_pure, lw=2.0,
            label=r"Pure — $V_I \to V_{II}$ snap")
    ax.plot(T_celsius, np.abs(buffered["reflection"]), color=c_buf, lw=2.4,
            label=r"Cholesterol — phase buffered")
    ax.axhline(0.5, color=c_ref, ls=":", lw=1.2, label=r"$|\Gamma| = 0.5$")
    ax.axvline(T_c_celsius, color=c_ref, ls=":", lw=1.0)
    ax.axvline(37, color=c_ref, ls="-.", lw=1.0)
    ax.set_xlabel(style.axis_label("Temperature", "T", r"$^\circ$C"))
    ax.set_ylabel(style.axis_label("Reflection magnitude", r"|\Gamma(T)|", ""))
    ax.set_ylim(-0.05, 1.05)
    style.legend(ax, where="below", ncol=1, fontsize=7)

    out_path = sim_output("cholesterol_topological_phase_buffer.png")
    style.save(fig, out_path, formats=("png",))
    plt.close(fig)
    print(f"Saved visualisation to {out_path}")

    # Validation print
    print(f"\n{'='*60}")
    print("Derived Constants (zero engineering magic numbers)")
    print(f"{'='*60}")
    print(f"  E_HB            = {E_HB_EV:.4f} eV  (U_raw x (1-phi))")
    print(f"  N_cooperative   = {N_COOPERATIVE:.0f}  (6 edges x 3/2)")
    print(f"  T_c (water)     = {T_C_WATER:.2f} K = {T_c_celsius:.1f} C")
    print(f"  Target          = 277.15 K = +4.0 C")
    print(f"  Error           = {abs(T_C_WATER - 277.15)/277.15*100:.2f}%")
    print(f"  phi (FCC)       = {N_PHI_PACK:.4f}")
    print(f"  A_yield_pure    = {A_YIELD_PURE:.4f}")
    print(f"  A_yield_buffered= {A_YIELD_BUFFERED:.4f}")


if __name__ == "__main__":
    generate_llcp_simulation()
