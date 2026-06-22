r"""
FTIR Comparison — Amino Acid Predicted vs Experimental
======================================================
Overlays the AVE-predicted transfer function (Bode plot) against
known experimental FTIR absorption peaks from NIST and literature.

The predicted curve has a FIXED frequency scale (locked by xi_topo).
The experimental peaks are measured.  No parameters are tuned: the
overlay is a fixed-scale comparison, not a fit.

Sources:
  - Shimanouchi (1972), NIST Chemistry WebBook
  - Dhamelincourt & Ramirez (2000), Raman and IR spectra of glycine
  - NIST Standard Reference Database 69

Run: PYTHONPATH=src python src/scripts/vol_5_biology/simulate_ftir_comparison.py

Ported from the Applied-Vacuum-Engineering archive; restyled to the AVE
white manuscript house style (ave.viz.style, Okabe-Ito). Depends on the
co-ported spice_organic_mapper (same directory).
"""

import matplotlib

import numpy as np

from ave.core.constants import Z_0, C_0
from ave.viz import style
from ave_path_util import sim_output
from spice_organic_mapper import get_inductance, get_capacitance

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# --- Known Experimental FTIR Peaks for Glycine (zwitterion, solid state) ---
# Sources: NIST WebBook, Shimanouchi 1972.
GLYCINE_FTIR = {
    607: r"COO$^-$ rock",
    893: r"C-C stretch",
    1034: r"C-N stretch",
    1130: r"NH$_3^+$ rock",
    1323: r"CH$_2$ wag",
    1414: r"COO$^-$ sym stretch",
    1524: r"NH$_3^+$ asym bend",
    1596: r"COO$^-$ asym stretch",
    2900: r"C-H stretch",
    3090: r"NH$_3^+$ stretch",
    3170: r"N-H sym stretch",
}

ALANINE_FTIR = {
    770: r"C-C-N skeletal",
    851: r"C-C stretch",
    1015: r"C-N stretch",
    1114: r"NH$_3^+$ rock",
    1307: r"CH bend",
    1363: r"COO$^-$ sym",
    1413: r"CH$_3$ asym bend",
    1456: r"CH$_3$ asym bend",
    1587: r"COO$^-$ asym",
    2942: r"C-H stretch",
    3070: r"NH$_3^+$ stretch",
}

# --- Transfer Function Solver ---
f = np.logspace(10.5, 14.6, 10000)
w = 2 * np.pi * f


def z_L(L):
    return 1j * w * L


def z_C(C):
    return 1.0 / (1j * w * C)


def parallel(z1, z2):
    return (z1 * z2) / (z1 + z2)


def z_rgroup_glycine():
    return z_C(get_capacitance("C-H")) + z_L(get_inductance("H"))


def z_rgroup_alanine():
    z_rh = z_C(get_capacitance("C-H")) + z_L(get_inductance("H"))
    return z_C(get_capacitance("C-C")) + z_L(get_inductance("C")) + z_rh / 3.0


def compute_transfer_function(z_rgroup):
    Z_load = Z_0
    Z_out = z_L(get_inductance("O")) + Z_load
    Z_co_single = z_C(get_capacitance("C-O")) + Z_out
    Z_o_double = z_C(get_capacitance("C=O")) + z_L(get_inductance("O"))
    Z_split = parallel(Z_o_double, Z_co_single)
    Z_carb = z_L(get_inductance("C")) + Z_split
    Z_alpha_out = z_C(get_capacitance("C-C")) + Z_carb
    Z_alpha_main = z_L(get_inductance("C")) + Z_alpha_out
    Z_alpha = parallel(z_rgroup, Z_alpha_main)
    Z_amino = z_C(get_capacitance("C-N")) + Z_alpha
    Z_in = z_L(get_inductance("N")) + Z_amino
    H = (Z_alpha / Z_in) * (Z_split / Z_alpha_main) * (Z_load / Z_co_single)
    return H


# --- Compute ---
nu = f / (C_0 * 100)  # Convert Hz -> cm^-1

H_gly = compute_transfer_function(z_rgroup_glycine())
H_ala = compute_transfer_function(z_rgroup_alanine())

P_gly_db = 10 * np.log10(np.clip(np.abs(H_gly) ** 2, 1e-30, None))
P_ala_db = 10 * np.log10(np.clip(np.abs(H_ala) ** 2, 1e-30, None))


def _plot_amino(ax, nu_arr, p_db, ftir_peaks, curve_color, peak_color, label):
    """Plot one amino acid transfer function with experimental FTIR overlay."""
    ax.plot(nu_arr, p_db, color=curve_color, lw=2.0, label=label, zorder=5)

    sorted_peaks = sorted(ftir_peaks.items())
    for wn, _ in sorted_peaks:
        ax.axvline(wn, color=peak_color, alpha=0.35, ls="--", lw=0.8)

    # Single proxy entry for the measured-peak markers (not one per line).
    ax.axvline(sorted_peaks[0][0], color=peak_color, alpha=0.35, ls="--", lw=0.8,
               label="Experimental FTIR peak")

    y_levels = [-15, -25, -35, -45, -55]
    for i, (wn, _) in enumerate(sorted_peaks):
        y = y_levels[i % len(y_levels)]
        ax.annotate(
            f"{wn}",
            xy=(wn, p_db[np.argmin(np.abs(nu_arr - wn))]),
            xytext=(wn, y),
            fontsize=6.5,
            color=peak_color,
            ha="center",
            va="top",
            arrowprops=dict(arrowstyle="-", color=peak_color, alpha=0.3, lw=0.5),
        )

    ax.set_ylabel(style.axis_label("Power transfer", r"|H|^2", "dB"))
    ax.set_xlim(300, 4000)
    top_y = max(10, np.max(p_db) + 5)
    ax.set_ylim(-100, top_y)

    # Neutral band guides for the IR regions.
    ax.axvspan(600, 1600, alpha=0.05, color=style.COLORS["muted"])
    ax.text(1100, 6, "Fingerprint region", fontsize=8,
            color=style.COLORS["muted"], ha="center")
    ax.axvspan(2500, 3800, alpha=0.05, color=style.COLORS["ave"])
    ax.text(3150, 6, "Stretch region", fontsize=8,
            color=style.COLORS["ave"], ha="center")
    style.legend(ax, where="right", fontsize=8)


def generate_ftir_comparison():
    style.apply()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(style.figsize("wide")[0], 7.5))

    _plot_amino(ax1, nu, P_gly_db, GLYCINE_FTIR,
                style.COLORS["ave"], style.COLORS["comparison"],
                "AVE predicted (glycine)")
    _plot_amino(ax2, nu, P_ala_db, ALANINE_FTIR,
                style.COLORS["accent"], style.COLORS["comparison"],
                "AVE predicted (L-alanine)")

    ax2.set_xlabel(style.axis_label("Wavenumber", r"\tilde{\nu}", r"cm$^{-1}$"))

    out_path = sim_output("amino_acid_ftir_comparison.png")
    style.save(fig, out_path, formats=("png",))
    plt.close(fig)
    print(f"Saved -> {out_path}")

    # --- Diagnostic: predicted transfer level at each measured peak ---
    print("\n  GLYCINE — predicted |H|^2 at measured FTIR peaks:")
    print(f"  {'Peak (cm^-1)':>14}  {'Assignment':>20}  {'Predicted |H|^2 (dB)':>22}")
    for wn, label in sorted(GLYCINE_FTIR.items()):
        idx = np.argmin(np.abs(nu - wn))
        print(f"  {wn:>14}  {label:>20}  {P_gly_db[idx]:>22.1f}")

    print("\n  ALANINE — predicted |H|^2 at measured FTIR peaks:")
    print(f"  {'Peak (cm^-1)':>14}  {'Assignment':>20}  {'Predicted |H|^2 (dB)':>22}")
    for wn, label in sorted(ALANINE_FTIR.items()):
        idx = np.argmin(np.abs(nu - wn))
        print(f"  {wn:>14}  {label:>20}  {P_ala_db[idx]:>22.1f}")


if __name__ == "__main__":
    generate_ftir_comparison()
