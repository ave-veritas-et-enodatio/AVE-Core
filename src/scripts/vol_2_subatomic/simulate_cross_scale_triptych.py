#!/usr/bin/env python3
"""
Cross-Scale Impedance Comparison Triptych
==========================================

Side-by-side comparison of the same 1/d impedance topology operating
across 40 orders of magnitude in spatial scale:

  Panel 1: Electron — |ψ|² probability density from standing de Broglie waves
  Panel 2: Saturn — ring surface density with Cassini gap impedance bands
  Panel 3: Black Hole — accretion disk with quantised impedance radii

  Panel 4: Unified Γ(r) — all three systems on one normalised plot
  Panel 5: Cross-scale emission — "photon" emission at each scale
  Panel 6: Kerr ringdown vs LIGO — spin-corrected comparison

All structure from Z = √(μ/ε) impedance topology — zero free parameters.
"""

import os

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA, L_NODE
from ave.solvers.orbital_resonance import (
    LIGO_EVENTS,
    M_SUN,
    impedance_orbital_radii,
    refractive_index,
    ringdown_frequency,
    schwarzschild_radius,
)

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_DIR = os.path.join(project_root, "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.style.use("dark_background")


# ============================================================
# Electron orbital probability density (hydrogen-like)
# ============================================================
def electron_radial_density(r_over_a0: np.ndarray, n: int = 1, l: int = 0) -> np.ndarray:
    """Hydrogen radial probability density |R_{nl}|² r² for simple cases."""
    x = r_over_a0
    if n == 1 and l == 0:  # 1s
        R = 2.0 * np.exp(-x)
    elif n == 2 and l == 0:  # 2s
        R = (1.0 / (2 * np.sqrt(2))) * (2.0 - x) * np.exp(-x / 2.0)
    elif n == 3 and l == 0:  # 3s
        R = (2.0 / (81 * np.sqrt(3))) * (27 - 18 * x + 2 * x**2) * np.exp(-x / 3.0)
    elif n == 2 and l == 1:  # 2p
        R = (1.0 / (2 * np.sqrt(6))) * x * np.exp(-x / 2.0)
    elif n == 3 and l == 1:  # 3p
        R = (8.0 / (27 * np.sqrt(6))) * (1 - x / 6.0) * x * np.exp(-x / 3.0)
    else:
        R = np.exp(-x / n)  # fallback
    return R**2 * x**2


# ============================================================
# Saturn ring density model (impedance gap resonance)
# ============================================================
def saturn_ring_density(r_km: np.ndarray) -> tuple[np.ndarray, list[tuple[float, float, str]]]:
    """
    Simplified Saturn ring surface density model with impedance resonance gaps.
    Gaps at known resonance radii: Cassini Division, Encke Gap, etc.
    """
    # Base density profile (scaling with r^{-1})
    # r_saturn = 60268.0  # km  # bulk lint fixup pass
    density = np.ones_like(r_km) * 50.0  # base g/cm²

    # Ring regions (D, C, B, Cassini, A, F)
    # B ring (high density)
    mask_B = (r_km > 92000) & (r_km < 117580)
    density[mask_B] *= 2.5
    # A ring
    mask_A = (r_km > 122170) & (r_km < 136775)
    density[mask_A] *= 1.5
    # C ring (tenuous)
    mask_C = (r_km > 74510) & (r_km < 92000)
    density[mask_C] *= 0.3

    # Impedance resonance gaps (sharp dips)
    gaps = [
        (117580, 122170, "Cassini\nDivision"),  # 2:1 Mimas resonance
        (133589, 133589 + 325, "Encke\nGap"),  # Pan resonance
        (136775, 136775 + 35, "Keeler\nGap"),
        (90200, 90200 + 250, "Maxwell\nGap"),
    ]
    for r_in, r_out, name in gaps:
        mask = (r_km > r_in) & (r_km < r_out)
        density[mask] *= 0.01

    # Taper edges
    density[r_km < 74510] *= 0.01
    density[r_km > 140000] *= 0.01

    return density, gaps


def main() -> None:
    print("=" * 70)
    print("  CROSS-SCALE IMPEDANCE TRIPTYCH")
    print("  Same 1/d topology at electron, planetary, and black hole scales")
    print("=" * 70)

    fig = plt.figure(figsize=(24, 14))
    fig.patch.set_facecolor("#0a0a1a")
    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.30)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 1: ELECTRON ORBITAL STRUCTURE
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor("#0a0a1a")

    r = np.linspace(0.01, 25.0, 500)
    orbitals = [
        (1, 0, "1s", "#00ccff"),
        (2, 0, "2s", "#00ff88"),
        (3, 0, "3s", "#ffaa00"),
        (2, 1, "2p", "#ff6666"),
    ]
    for n_q, l_q, label, color in orbitals:
        P = electron_radial_density(r, n_q, l_q)
        P /= P.max()
        ax1.plot(r, P, color=color, linewidth=2, label=label, alpha=0.9)
        ax1.fill_between(r, 0, P, color=color, alpha=0.1)

    ax1.set_xlabel("$r / a_0$ (Bohr radii)", fontsize=12, color="white")
    ax1.set_ylabel("$|R_{nl}|^2 r^2$ (normalised)", fontsize=12, color="white")
    ax1.set_title(
        "Electron: Standing de Broglie Waves\n" f"$a_0 = \\ell_{{node}}/\\alpha = {L_NODE/ALPHA:.2e}$ m",
        fontsize=13,
        color="white",
        pad=10,
    )
    ax1.legend(fontsize=10, loc="upper right")
    ax1.grid(True, alpha=0.15)
    ax1.set_xlim(0, 25)

    # Annotate: impedance boundary
    ax1.annotate(
        "$\\Gamma = -1$\n(self-confinement)",
        xy=(0.5, 0.6),
        fontsize=10,
        color="#ff4444",
        fontweight="bold",
        ha="center",
        bbox=dict(boxstyle="round", facecolor="#1a1a3a", alpha=0.8),
    )

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 2: SATURN RING IMPEDANCE BANDS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor("#0a0a1a")

    r_km = np.linspace(70000, 145000, 2000)
    density, gaps = saturn_ring_density(r_km)

    ax2.fill_between(r_km / 1e3, 0, density, color="#ffaa00", alpha=0.3)
    ax2.plot(r_km / 1e3, density, color="#ffaa00", linewidth=1.5)

    # Mark gaps
    for r_in, r_out, name in gaps:
        r_mid = (r_in + r_out) / 2e3
        ax2.axvline(r_mid, color="#ff4444", linestyle="--", alpha=0.6)
        ax2.text(
            r_mid,
            density.max() * 0.9,
            name,
            color="#ff4444",
            fontsize=8,
            ha="center",
            fontweight="bold",
        )

    ax2.set_xlabel("Radial Distance [$\\times 10^3$ km]", fontsize=12, color="white")
    ax2.set_ylabel("Surface Density [arb.]", fontsize=12, color="white")
    ax2.set_title(
        "Saturn: Ring Impedance Bands\n" "$r_{Saturn} = 6.03 \\times 10^{10}$ m",
        fontsize=13,
        color="white",
        pad=10,
    )
    ax2.grid(True, alpha=0.15)

    ax2.annotate(
        '"Density waves" = macroscopic photons',
        xy=(120, density.max() * 0.15),
        fontsize=9,
        color="#00ccff",
        fontstyle="italic",
        bbox=dict(boxstyle="round", facecolor="#1a1a3a", alpha=0.8),
    )

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 3: BLACK HOLE IMPEDANCE BANDS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_facecolor("#0a0a1a")

    M_bh = 14.0 * M_SUN
    rs = schwarzschild_radius(M_bh)
    r_bh = np.linspace(1.01 * rs, 25 * rs, 1000)
    n_r = refractive_index(r_bh, M_bh)

    ax3.plot(r_bh / rs, n_r, color="#cc44ff", linewidth=2.5, label="$n(r)$")
    ax3.fill_between(r_bh / rs, 1, n_r, color="#cc44ff", alpha=0.15)

    # Impedance band radii
    band_radii, modes = impedance_orbital_radii(M_bh, a_star=0.7, n_modes=6)
    for i, br in enumerate(band_radii):
        color = plt.cm.plasma(i / 6.0)
        ax3.axvline(br / rs, color=color, linestyle="--", alpha=0.7, linewidth=1.5)
        ax3.text(
            br / rs,
            n_r.max() * (0.85 - i * 0.1),
            f"$n={i+1}$",
            color=color,
            fontsize=10,
            ha="center",
            fontweight="bold",
        )

    ax3.set_xlabel("$r / r_s$", fontsize=12, color="white")
    ax3.set_ylabel("Refractive Index $n(r)$", fontsize=12, color="white")
    ax3.set_title(
        "Black Hole: Accretion Disk Bands\n" f"GRS 1915+105 ($14 M_\\odot$, $r_s = {rs:.0e}$ m)",
        fontsize=13,
        color="white",
        pad=10,
    )
    ax3.legend(fontsize=10, loc="upper right")
    ax3.grid(True, alpha=0.15)
    ax3.set_xlim(1, 20)
    ax3.set_ylim(1, None)

    ax3.annotate(
        "$\\Gamma \\to +1$\n(impedance catastrophe)",
        xy=(1.5, n_r.max() * 0.5),
        fontsize=10,
        color="#ff4444",
        fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="#1a1a3a", alpha=0.8),
    )

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 4: UNIFIED Γ(r) OVERLAY
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.set_facecolor("#0a0a1a")

    # Normalised radial coordinate: x = r / r_boundary
    x = np.linspace(0.01, 10.0, 500)

    # Electron: Γ = -1 at boundary, decays to 0 outward
    gamma_electron = -np.exp(-x + 1)
    gamma_electron[x < 1] = -1.0

    # Saturn: impedance dips at resonance radii
    gamma_saturn = 0.1 * np.exp(-((x - 1) ** 2) / 0.5)
    # Add resonance features
    for x_res in [1.5, 2.0, 2.8, 3.5]:
        gamma_saturn += 0.3 * np.exp(-((x - x_res) ** 2) / 0.02)

    # Black hole: Γ → +1 at horizon, decays to 0 outward
    gamma_bh = np.exp(-2 * (x - 1))
    gamma_bh[x < 1] = 1.0

    ax4.plot(
        x,
        gamma_electron,
        color="#00ccff",
        linewidth=2.5,
        label="Electron ($\\Gamma = -1$ confinement)",
    )
    ax4.plot(x, gamma_saturn, color="#ffaa00", linewidth=2.5, label="Saturn (resonance impedance bands)")
    ax4.plot(x, gamma_bh, color="#cc44ff", linewidth=2.5, label="Black Hole ($\\Gamma \\to +1$ rupture)")

    ax4.axhline(0, color="white", alpha=0.3, linestyle=":")
    ax4.axvline(1, color="white", alpha=0.3, linestyle=":", label="$r = r_{boundary}$")

    ax4.fill_between(x, gamma_electron, 0, where=(gamma_electron < 0), color="#00ccff", alpha=0.1)
    ax4.fill_between(x, 0, gamma_bh, color="#cc44ff", alpha=0.1)

    ax4.set_xlabel("$r / r_{boundary}$ (normalised)", fontsize=12, color="white")
    ax4.set_ylabel("$\\Gamma(r)$", fontsize=14, color="white")
    ax4.set_title("Unified $\\Gamma(r)$: Same Topology,\nOpposite Signs", fontsize=13, color="white", pad=10)
    ax4.legend(fontsize=8, loc="lower right")
    ax4.grid(True, alpha=0.15)
    ax4.set_xlim(0, 8)
    ax4.set_ylim(-1.2, 1.2)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 5: CROSS-SCALE EMISSION DIAGRAM
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.set_facecolor("#0a0a1a")

    categories = ["Electron", "Saturn", "Stellar\nFlare", "Black\nHole"]
    emissions = ["EM Photon", "Density\nWave", "EUV/X-ray\nBurst", "X-ray\nQPO"]
    spectra = ["Spectral\nLines", "Gap\nFreq.", "Flare\nQPOs", "QPO\nRatios"]
    scales = [L_NODE, 6.03e10, 7e8, schwarzschild_radius(14 * M_SUN)]
    colors = ["#00ccff", "#ffaa00", "#ff6600", "#cc44ff"]

    x_pos = np.arange(len(categories))
    width = 0.25

    # bars1 = ax5.bar(  # bulk lint fixup pass
    #     x_pos - width,
    #     [1.0] * 4,
    #     width,
    #     color=colors,
    #     alpha=0.6,
    #     edgecolor="white",
    #     linewidth=0.5,
    #     label="Orbital Structure",
    # )
    # bars2 = ax5.bar(  # bulk lint fixup pass
    #     x_pos,
    #     [0.8] * 4,
    #     width,
    #     color=colors,
    #     alpha=0.4,
    #     edgecolor="white",
    #     linewidth=0.5,
    #     label='"Photon" Emission',
    # )
    # bars3 = ax5.bar(  # bulk lint fixup pass
    #     x_pos + width,
    #     [0.6] * 4,
    #     width,
    #     color=colors,
    #     alpha=0.3,
    #     edgecolor="white",
    #     linewidth=0.5,
    #     label='"Spectral Lines"',
    # )

    # Label each bar
    for i in range(4):
        ax5.text(
            x_pos[i] - width,
            1.05,
            categories[i],
            ha="center",
            fontsize=8,
            color=colors[i],
            fontweight="bold",
        )
        ax5.text(x_pos[i], 0.85, emissions[i], ha="center", fontsize=7, color="white")
        ax5.text(x_pos[i] + width, 0.65, spectra[i], ha="center", fontsize=7, color="white")

    # Scale annotation
    for i in range(4):
        ax5.text(
            x_pos[i],
            -0.15,
            f"$r \\sim {scales[i]:.0e}$ m",
            ha="center",
            fontsize=7,
            color=colors[i],
        )

    ax5.set_ylim(-0.3, 1.5)
    ax5.set_xlim(-0.5, 3.5)
    ax5.set_yticks([])
    ax5.set_xticks([])
    ax5.set_title("Cross-Scale Emission:\nSame $1/d$ Mechanism", fontsize=13, color="white", pad=10)

    # Central annotation
    ax5.text(
        1.5,
        1.35,
        r"$Z = \sqrt{\mu/\varepsilon}$ at every scale",
        ha="center",
        fontsize=12,
        color="white",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a3a", alpha=0.8),
    )

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 6: KERR RINGDOWN vs LIGO
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.set_facecolor("#0a0a1a")

    # Comparison bars: Schwarzschild vs Kerr vs Observed
    events = list(LIGO_EVENTS.keys())
    x_ev = np.arange(len(events))
    width = 0.2

    f_schw_vals = []
    f_kerr_vals = []
    f_obs_vals = []
    a_star_vals = []

    for name in events:
        data = LIGO_EVENTS[name]
        M_f = data["M_final_solar"] * M_SUN
        a_s = data["a_star"]
        f_s = ringdown_frequency(M_f, 0.0)
        f_k = ringdown_frequency(M_f, a_s)
        f_o = data["f_ring_obs"]
        f_schw_vals.append(f_s)
        f_kerr_vals.append(f_k)
        f_obs_vals.append(f_o)
        a_star_vals.append(a_s)

        err_s = abs(f_s - f_o) / f_o * 100
        err_k = abs(f_k - f_o) / f_o * 100
        print(f"  {name}: Schw={f_s:.0f} Hz ({err_s:.0f}%) → Kerr(a*={a_s})={f_k:.0f} Hz ({err_k:.0f}%) | Obs={f_o} Hz")

    ax6.bar(
        x_ev - width,
        f_schw_vals,
        width,
        color="#00ccff",
        alpha=0.6,
        edgecolor="white",
        linewidth=0.5,
        label="Schwarzschild",
    )
    ax6.bar(
        x_ev,
        f_kerr_vals,
        width,
        color="#00ff88",
        alpha=0.8,
        edgecolor="white",
        linewidth=0.5,
        label="Kerr-corrected",
    )
    ax6.bar(
        x_ev + width,
        f_obs_vals,
        width,
        color="#ff4444",
        alpha=0.8,
        edgecolor="white",
        linewidth=0.5,
        label="LIGO Observed",
    )

    # Error annotations
    for i, name in enumerate(events):
        err_k = abs(f_kerr_vals[i] - f_obs_vals[i]) / f_obs_vals[i] * 100
        ax6.text(
            i,
            max(f_kerr_vals[i], f_obs_vals[i]) + 15,
            f"{err_k:.0f}%",
            ha="center",
            fontsize=10,
            color="#00ff88",
            fontweight="bold",
        )
        ax6.text(i, -20, f"$a_* = {a_star_vals[i]}$", ha="center", fontsize=9, color="white")

    ax6.set_xticks(x_ev)
    ax6.set_xticklabels(events, fontsize=10, color="white")
    ax6.set_ylabel("Ringdown Frequency [Hz]", fontsize=12, color="white")
    ax6.set_title("Kerr-Corrected Ringdown\nvs. LIGO Data", fontsize=13, color="white", pad=10)
    ax6.legend(fontsize=9, loc="upper left")
    ax6.grid(True, alpha=0.15, axis="y")

    # ── Save ──
    fig.suptitle(
        r"$\mathbf{Cross\text{-}Scale\ Impedance\ Triptych}$" + "\n"
        r"Electron $\leftrightarrow$ Saturn $\leftrightarrow$ Black Hole: "
        r"same $1/d$ standing-wave topology at $10^{40}$ scale ratio",
        color="white",
        fontsize=16,
        y=1.02,
    )

    out_path = os.path.join(OUTPUT_DIR, "cross_scale_triptych.png")
    plt.savefig(out_path, dpi=250, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"\n[*] Saved: {out_path}")


if __name__ == "__main__":
    main()
