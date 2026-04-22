"""
Torus Knot Ladder — Baryon Resonance Spectrum

Computes the mass predictions for the (2,q) torus knot progression
and compares against PDG baryon resonances.

The (2,q) torus knots (odd q only) generate a mass ladder:
    m(c) = I_scalar(κ_eff/c) / (1 - V_halo·p_c) + 1

where c is the crossing number and κ_eff is the thermally softened
Faddeev-Skyrme coupling.

Output: assets/sim_outputs/torus_knot_baryon_spectrum.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

from ave.core.constants import KAPPA_FS, P_C

# Electron mass in MeV
M_E_MEV = 0.51099895

# V_halo and p_c
V_HALO = 2.0


# ---- Solver ----


def phase_profile(r, r_opt, n):
    if r == 0:
        return np.pi
    return np.pi / (1.0 + (r / r_opt) ** n)


def energy_density(r, r_opt, n, kappa):
    dr = 1e-6
    phi1 = phase_profile(r, r_opt, n)
    phi2 = phase_profile(r + dr, r_opt, n)
    dphi = (phi2 - phi1) / dr

    # Axiom 4: gradient saturation at the lattice Nyquist limit
    # gradient yield = π / ℓ_node = π in natural units (ℓ_node = 1)
    gradient_yield = np.pi
    ratio_sq = min(dphi**2 / gradient_yield**2, 1.0 - 1e-15)
    S = np.sqrt(1.0 - ratio_sq)
    dphi_eff = dphi * S

    kinetic = 0.5 * dphi_eff**2
    skyrme = 0.5 * np.sin(phi1) ** 2 / (r**2 + 1e-12)
    return 4 * np.pi * r**2 * (kinetic + kappa**2 * skyrme * dphi_eff**2)


def compute_I_scalar(crossing_number, kappa=KAPPA_FS):
    """Compute I_scalar for a given crossing number c."""
    r_opt_max = kappa / crossing_number

    def objective(params):
        r_opt, n = params
        integral, _ = quad(energy_density, 0, 10 * r_opt, args=(r_opt, n, kappa), limit=100)
        return integral

    result = minimize(objective, [1.0, 2.0], bounds=[(0.1, r_opt_max), (1.0, 4.0)], method="L-BFGS-B")
    return result.fun


def proton_mass_ratio(I_scalar):
    """Convert I_scalar to m/m_e via the eigenvalue equation."""
    return I_scalar / (1.0 - V_HALO * P_C) + 1.0


# ---- PDG Data ----

PDG_RESONANCES = {
    # Nucleon (I=1/2)
    "p": (938.272, "1/2+", "****"),
    # Delta (I=3/2)
    "Δ(1232)": (1232, "3/2+", "****"),
    "Δ(1600)": (1600, "3/2+", "***"),
    "Δ(1620)": (1620, "1/2-", "****"),
    "Δ(1700)": (1700, "3/2-", "****"),
    "Δ(1900)": (1900, "1/2-", "***"),
    "Δ(1905)": (1905, "5/2+", "****"),
    "Δ(1910)": (1910, "1/2+", "****"),
    "Δ(1950)": (1950, "7/2+", "****"),
    "Δ(2420)": (2420, "11/2+", "****"),
    # Higher N*
    "N(2190)": (2190, "7/2-", "****"),
    "N(2220)": (2220, "9/2+", "****"),
    "N(2250)": (2250, "9/2-", "****"),
}


def run_spectrum():
    """Compute and plot the torus knot baryon spectrum."""
    crossing_numbers = [3, 5, 7, 9, 11, 13, 15]
    results = []

    print("=" * 70)
    print("  TORUS KNOT BARYON SPECTRUM")
    print("=" * 70)
    print()

    for c in crossing_numbers:
        I = compute_I_scalar(c)
        m_ratio = proton_mass_ratio(I)
        m_MeV = m_ratio * M_E_MEV

        # Find nearest PDG match
        best_name, best_mass, best_jp, best_stars = "", 0, "", ""
        best_delta = 1e6
        for name, (mass, jp, stars) in PDG_RESONANCES.items():
            if abs(m_MeV - mass) < abs(best_delta):
                best_delta = m_MeV - mass
                best_name = name
                best_mass = mass
                best_jp = jp
                # best_stars = stars  # bulk lint fixup pass

        pct = best_delta / best_mass * 100
        results.append((c, m_MeV, best_name, best_mass, best_jp, pct))

        print(
            f"  (2,{c:2d}):  {m_MeV:7.1f} MeV  →  {best_name:10s} "
            f"({best_mass:.0f} MeV, J^P={best_jp})  "
            f"Δ = {best_delta:+.1f} MeV ({pct:+.2f}%)"
        )

    print()

    # ---- Plot ----
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    # Plot PDG resonances as horizontal bands
    for name, (mass, jp, stars) in PDG_RESONANCES.items():
        alpha = 0.8 if stars == "****" else 0.4
        ax.axhline(mass, color="#2196F3", alpha=alpha * 0.3, linewidth=8)
        ax.text(15.5, mass, f"{name}  ({jp})", fontsize=8, va="center", color="#1565C0", alpha=0.8)

    # Plot predictions
    pred_c = [r[0] for r in results]
    pred_m = [r[1] for r in results]
    ax.scatter(
        pred_c,
        pred_m,
        s=120,
        c="#E53935",
        zorder=5,
        edgecolors="#B71C1C",
        linewidths=1.5,
        label="AVE Prediction",
    )

    # Connect with line
    ax.plot(pred_c, pred_m, "--", color="#E53935", alpha=0.5, linewidth=1.5)

    # Annotate matches
    for c, m_pred, pdg_name, pdg_mass, jp, pct in results:
        if c >= 5:
            ax.annotate(
                f"{m_pred:.0f} MeV\n({pct:+.1f}%)",
                (c, m_pred),
                textcoords="offset points",
                xytext=(-50, 10),
                fontsize=8,
                color="#B71C1C",
                arrowprops=dict(arrowstyle="->", color="#E53935", lw=0.8),
            )

    # Note: gradient saturation annotation
    ax.text(
        0.97,
        0.18,
        "Axiom 4 gradient saturation\n"
        r"$S(|\partial\phi/\partial r|,\;\pi/\ell_{node})$"
        "\n"
        "applied inside the energy\n"
        "functional at all crossing\n"
        "numbers (zero free parameters).",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=9,
        color="#1B5E20",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#E8F5E9", edgecolor="#4CAF50", alpha=0.9),
    )

    ax.set_xlabel("Crossing Number c  [(2,q) torus knot]", fontsize=12)
    ax.set_ylabel("Mass (MeV)", fontsize=12)
    ax.set_title(
        "Torus Knot Ladder — Baryon Resonance Spectrum\n"
        r"$m(c) = I_{scalar}(\kappa_{eff}/c,\;S_{Ax4})\,/\,(1 - 2p_c) + 1$",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_xlim(2, 18)
    ax.set_ylim(400, 2800)
    ax.legend(loc="upper left", fontsize=11)
    ax.grid(True, alpha=0.2)

    # Save
    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "torus_knot_baryon_spectrum.png")
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    print(f"  Figure saved: {out_path}")

    # Also copy to manuscript assets
    ms_assets = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
    os.makedirs(ms_assets, exist_ok=True)
    ms_path = os.path.join(ms_assets, "torus_knot_baryon_spectrum.png")
    import shutil

    shutil.copy2(out_path, ms_path)
    print(f"  Copied to:    {ms_path}")


if __name__ == "__main__":
    run_spectrum()
