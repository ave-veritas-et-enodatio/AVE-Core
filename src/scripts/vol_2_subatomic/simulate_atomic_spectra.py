#!/usr/bin/env python3
"""
Atomic Spectra: LC Cavity Resonances from First Principles
============================================================

In AVE, an atom is a topological defect (unknot) trapped in the LC lattice.
The "electron orbitals" are standing-wave resonances of the surrounding
impedance cavity. The Rydberg spectral lines are the harmonic series of
this cavity — not probability clouds, but phonon-polariton modes.

DERIVATION CHAIN:
─────────────────
1. ℓ_node = ℏ/(m_e c)                    (lattice pitch)
2. α = e²/(4πε₀ℏc)                       (coupling constant)
3. a₀ = ℓ_node/α = ℏ/(m_e c α) = 0.529 Å (Bohr radius = cavity fundamental)
4. E_n = -E_ion/n²                         (1/n² LC cavity harmonics)
5. E_ion = ½α²m_ec² = 13.606 eV           (ionization energy)
6. R_∞ = α²m_ec/(2h)                       (Rydberg constant)
7. λ_{n→m} = 1/(R_∞ × (1/m² - 1/n²))     (transition wavelengths)

All constants from ave.core.constants. Zero free parameters.

Usage:
    python src/scripts/vol_2_subatomic/simulate_atomic_spectra.py
"""

import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.gridspec import GridSpec  # noqa: E402

from ave.core.constants import ALPHA, C_0, HBAR, L_NODE, M_E, e_charge  # noqa: E402

# ══════════════════════════════════════════════════════════════════════════════
# DERIVED CONSTANTS (from engine primitives)
# ══════════════════════════════════════════════════════════════════════════════
h_planck = 2.0 * np.pi * HBAR

# Bohr radius: a₀ = ℓ_node / α = ℏ/(m_e c α)
A_BOHR = float(L_NODE) / ALPHA  # m

# Ionization energy: E_ion = ½ α² m_e c²
E_ION_J = 0.5 * ALPHA**2 * M_E * C_0**2
E_ION_EV = E_ION_J / e_charge

# Rydberg constant: R_∞ = α² m_e c / (2h) = E_ion/(hc)
R_INF = ALPHA**2 * M_E * C_0 / (2.0 * h_planck)  # m⁻¹

# Rydberg energy (= E_ion = 1 Rydberg)
RY_EV = float(E_ION_EV)

# NIST experimental values for comparison
NIST = {
    "a_bohr": 5.29177e-11,  # m
    "E_ion": 13.6057,  # eV
    "R_inf": 1.0973732e7,  # m⁻¹
}


def run_simulation():
    print("=" * 78)
    print("  ATOMIC SPECTRA: LC CAVITY RESONANCES FROM FIRST PRINCIPLES")
    print("  Inputs: m_e, c, α, ℏ  |  All from ave.core.constants")
    print("=" * 78)

    print("\n  ── DERIVED ATOMIC CONSTANTS ──")
    print(f"    ℓ_node = ℏ/(m_e c) = {float(L_NODE):.4e} m")
    print(f"    α      = {ALPHA:.6e} = 1/{1/ALPHA:.2f}")
    print(f"    a₀     = ℓ_node/α  = {A_BOHR:.4e} m  (NIST: {NIST['a_bohr']:.4e})")
    print(f"    E_ion  = ½α²m_ec²  = {RY_EV:.4f} eV  (NIST: {NIST['E_ion']:.4f})")
    print(f"    R_∞    = α²m_ec/2h = {R_INF:.6e} m⁻¹  (NIST: {NIST['R_inf']:.6e})")

    delta_a = (A_BOHR - NIST["a_bohr"]) / NIST["a_bohr"] * 100
    delta_E = (RY_EV - NIST["E_ion"]) / NIST["E_ion"] * 100
    delta_R = (R_INF - NIST["R_inf"]) / NIST["R_inf"] * 100

    print(f"\n    Δ(a₀)  = {delta_a:+.4f}%")
    print(f"    Δ(E_ion) = {delta_E:+.4f}%")
    print(f"    Δ(R_∞) = {delta_R:+.4f}%")

    # ── Energy levels ──────────────────────────────────────────────────────
    print("\n  ── HYDROGEN ENERGY LEVELS ──")
    n_levels = np.arange(1, 8)
    # E_n = -RY_EV / n_levels**2  # bulk lint fixup pass

    print(f"  {'n':>4} {'E_n (eV)':>12} {'r_n / a₀':>10}")
    print(f"  {'─'*28}")
    for n in n_levels:
        E = -RY_EV / n**2
        r = n**2  # r_n / a₀ = n²
        print(f"  {n:4d} {E:12.4f} {r:10.1f}")

    # ── Spectral series ────────────────────────────────────────────────────
    print("\n  ── SPECTRAL SERIES (Balmer) ──")
    print(f"  {'Transition':>14} {'λ_AVE (nm)':>12} {'λ_NIST (nm)':>12} {'Δ':>8}")
    print(f"  {'─'*50}")

    # Balmer series: transitions to n=2
    balmer_nist = {3: 656.28, 4: 486.13, 5: 434.05, 6: 410.17, 7: 397.01}
    for n_upper in range(3, 8):
        lambda_m = 1.0 / (R_INF * (1.0 / 4.0 - 1.0 / n_upper**2))
        lambda_nm = lambda_m * 1e9
        nist_nm = balmer_nist.get(n_upper, None)
        delta = (lambda_nm - nist_nm) / nist_nm * 100 if nist_nm else 0
        print(f"  {n_upper}→2{' ':>10} {lambda_nm:12.2f} {nist_nm:12.2f} {delta:+7.3f}%")

    # Lyman series: transitions to n=1
    print("\n  ── SPECTRAL SERIES (Lyman) ──")
    lyman_nist = {2: 121.57, 3: 102.57, 4: 97.25, 5: 94.97, 6: 93.78}
    for n_upper in range(2, 7):
        lambda_m = 1.0 / (R_INF * (1.0 - 1.0 / n_upper**2))
        lambda_nm = lambda_m * 1e9
        nist_nm = lyman_nist.get(n_upper, None)
        delta = (lambda_nm - nist_nm) / nist_nm * 100 if nist_nm else 0
        print(f"  {n_upper}→1{' ':>10} {lambda_nm:12.2f} {nist_nm:12.2f} {delta:+7.3f}%")

    # ══════════════════════════════════════════════════════════════════════════
    # PLOTTING
    # ══════════════════════════════════════════════════════════════════════════

    C_BG = "#0a0a1a"
    C_TEXT = "#e0e0e0"
    C_GRID = "#1a2a3a"

    fig = plt.figure(figsize=(20, 12))
    fig.patch.set_facecolor(C_BG)
    gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

    def style_ax(ax):
        ax.set_facecolor(C_BG)
        ax.tick_params(colors=C_TEXT, labelsize=9)
        ax.grid(True, alpha=0.12, color=C_GRID)
        for spine in ax.spines.values():
            spine.set_color("#333355")

    # Panel 1: Energy level diagram
    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1)
    for n in range(1, 8):
        E = -RY_EV / n**2
        ax1.hlines(E, 0.3, 0.7, color="#44ff88", linewidth=2)
        ax1.text(0.75, E, f"n={n}\n{E:.2f} eV", color=C_TEXT, fontsize=8, va="center")
    # Show some transitions (Balmer)
    for n_up in [3, 4, 5]:
        E_low = -RY_EV / 4
        E_high = -RY_EV / n_up**2
        ax1.annotate(
            "",
            xy=(0.5, E_low),
            xytext=(0.5, E_high),
            arrowprops=dict(arrowstyle="->", color="#ff4444", lw=1.5),
        )
    ax1.set_xlim(0, 1)
    ax1.set_ylabel("Energy (eV)", color=C_TEXT, fontsize=10)
    ax1.set_title(
        f"Hydrogen Energy Levels\n$E_n = -E_{{ion}}/n^2$, $E_{{ion}}$ = {RY_EV:.3f} eV",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax1.set_xticks([])

    # Panel 2: Balmer series spectral lines
    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2)
    colors_nm = plt.cm.rainbow(np.linspace(0.1, 0.9, 5))
    for i, n_up in enumerate(range(3, 8)):
        lam = 1.0 / (R_INF * (0.25 - 1.0 / n_up**2)) * 1e9
        ax2.axvline(
            lam,
            color=colors_nm[i],
            linewidth=3,
            alpha=0.8,
            label=f"H-{chr(945+i-1) if i > 0 else 'α'}: {lam:.1f} nm",
        )
    ax2.set_xlabel("Wavelength (nm)", color=C_TEXT, fontsize=10)
    ax2.set_yticks([])
    ax2.set_title("Balmer Series:\nLC Cavity Harmonics", color=C_TEXT, fontsize=13, fontweight="bold")
    ax2.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax2.set_xlim(370, 700)

    # Panel 3: Radial probability density (hydrogenic wavefunctions)
    ax3 = fig.add_subplot(gs[0, 2])
    style_ax(ax3)
    r_bohr = np.linspace(0, 25, 500)  # in units of a₀

    # Hydrogenic radial functions R_{n,0}(r) for ℓ=0
    def R_10(r):
        return 2.0 * np.exp(-r)

    def R_20(r):
        return (1.0 / (2 * np.sqrt(2))) * (2 - r) * np.exp(-r / 2)

    def R_30(r):
        return (2.0 / (81 * np.sqrt(3))) * (27 - 18 * r + 2 * r**2) * np.exp(-r / 3)

    P_1s = r_bohr**2 * R_10(r_bohr) ** 2
    P_2s = r_bohr**2 * R_20(r_bohr) ** 2
    P_3s = r_bohr**2 * R_30(r_bohr) ** 2

    ax3.fill_between(r_bohr, P_1s / max(P_1s), alpha=0.3, color="#00ccff")
    ax3.plot(r_bohr, P_1s / max(P_1s), color="#00ccff", linewidth=2.5, label="1s")
    ax3.fill_between(r_bohr, P_2s / max(P_2s), alpha=0.2, color="#ff44aa")
    ax3.plot(r_bohr, P_2s / max(P_2s), color="#ff44aa", linewidth=2, label="2s")
    ax3.fill_between(r_bohr, P_3s / max(P_3s), alpha=0.15, color="#ffaa44")
    ax3.plot(r_bohr, P_3s / max(P_3s), color="#ffaa44", linewidth=2, label="3s")
    ax3.set_xlabel(r"$r / a_0$", color=C_TEXT, fontsize=10)
    ax3.set_ylabel("Radial density (normalized)", color=C_TEXT, fontsize=10)
    ax3.set_title(
        "Standing Wave Envelopes:\nPhonon-Polariton Modes",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax3.legend(fontsize=9, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)

    # Panel 4: Derivation chain
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.set_facecolor(C_BG)
    ax4.axis("off")

    chain_text = (
        "LC CAVITY RESONANCE CHAIN\n"
        "═════════════════════════\n\n"
        f"ℓ_node = ℏ/(m_e c)\n"
        f"     = {float(L_NODE):.3e} m\n"
        "    ↓\n"
        f"a₀ = ℓ_node/α\n"
        f"   = {A_BOHR:.3e} m\n"
        "    ↓\n"
        f"E_ion = ½α²m_ec²\n"
        f"      = {RY_EV:.4f} eV\n"
        "    ↓\n"
        f"R_∞ = α²m_ec/(2h)\n"
        f"    = {R_INF:.4e} m⁻¹\n"
        "    ↓\n"
        f"λ_{{n→m}} = 1/(R_∞(1/m²-1/n²))\n"
        f"  Hα: {1/(R_INF*(0.25-1/9))*1e9:.1f} nm"
    )
    ax4.text(
        0.05,
        0.95,
        chain_text,
        transform=ax4.transAxes,
        fontfamily="monospace",
        fontsize=10,
        color="#44ff88",
        verticalalignment="top",
    )

    # Panel 5: Full spectrum (all series)
    ax5 = fig.add_subplot(gs[1, 1])
    style_ax(ax5)

    series = {
        "Lyman": (1, "#8844ff"),
        "Balmer": (2, "#ff4444"),
        "Paschen": (3, "#ffaa44"),
        "Brackett": (4, "#44aaff"),
    }
    for name, (m, color) in series.items():
        wavelengths = []
        for n_up in range(m + 1, m + 7):
            lam = 1.0 / (R_INF * (1.0 / m**2 - 1.0 / n_up**2)) * 1e9
            wavelengths.append(lam)
        ax5.scatter(
            wavelengths,
            [m] * len(wavelengths),
            color=color,
            s=80,
            label=f"{name} (→n={m})",
            zorder=5,
            edgecolors="#ffffff",
            linewidths=0.5,
        )
        for lam in wavelengths:
            ax5.axvline(lam, color=color, alpha=0.15, linewidth=1)

    ax5.set_xlabel("Wavelength (nm)", color=C_TEXT, fontsize=10)
    ax5.set_ylabel("Series (lower n)", color=C_TEXT, fontsize=10)
    ax5.set_title("Complete Spectral Map:\n4 Series from R_∞", color=C_TEXT, fontsize=13, fontweight="bold")
    ax5.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax5.set_xscale("log")
    ax5.set_xlim(50, 5000)
    ax5.set_yticks([1, 2, 3, 4])
    ax5.set_yticklabels(["Lyman", "Balmer", "Paschen", "Brackett"], fontsize=9)

    # Panel 6: Impedance cavity analogy
    ax6 = fig.add_subplot(gs[1, 2])
    style_ax(ax6)

    # Show V(r) = -e²/(4πε₀r) as impedance cavity potential
    r_pot = np.linspace(0.1, 20, 500)
    V_pot = -1.0 / r_pot  # in units of E_ion
    ax6.plot(r_pot, V_pot, color="#44ff88", linewidth=2.5, label=r"$V(r) = -E_{ion} \cdot a_0/r$")
    # Energy levels
    for n in [1, 2, 3, 4]:
        E_level = -1.0 / n**2
        r_turn = -1.0 / E_level  # classical turning point: r_n = n² a₀
        ax6.hlines(E_level, 0, r_turn, color="#ff4444", linewidth=1.5, alpha=0.7)
        ax6.text(r_turn + 0.3, E_level, f"n={n}", color=C_TEXT, fontsize=9)
    ax6.axhline(y=0, color="#ffffff", linewidth=0.5, alpha=0.3)
    ax6.set_xlabel(r"$r / a_0$", color=C_TEXT, fontsize=10)
    ax6.set_ylabel(r"$V / E_{ion}$", color=C_TEXT, fontsize=10)
    ax6.set_title("Impedance Cavity:\n1/r Potential Well", color=C_TEXT, fontsize=13, fontweight="bold")
    ax6.legend(fontsize=9, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax6.set_ylim(-2, 0.5)
    ax6.set_xlim(0, 20)

    fig.suptitle(
        "Atomic Spectra: LC Cavity Resonances from First Principles\n"
        r"$a_0 = \ell_{node}/\alpha$,  $E_{ion} = \frac{1}{2}\alpha^2 m_e c^2$ = "
        f"{RY_EV:.3f} eV,  "
        r"$R_\infty$ = " + f"{R_INF:.4e} m$^{{-1}}$  |  "
        r"All from $\mathtt{ave.core.constants}$",
        color=C_TEXT,
        fontsize=14,
        fontweight="black",
        y=0.995,
    )

    plt.tight_layout(rect=[0, 0, 1, 0.93])

    out_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "atomic_spectra_cavity.png")
    plt.savefig(out_path, dpi=200, facecolor=C_BG, bbox_inches="tight")
    print(f"\n  ✓ Plot saved → {out_path}")
    print("\n  ═══ ATOMIC SPECTRA DERIVATION COMPLETE ═══")


if __name__ == "__main__":
    run_simulation()
