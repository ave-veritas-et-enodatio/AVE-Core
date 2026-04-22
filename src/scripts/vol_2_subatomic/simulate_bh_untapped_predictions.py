#!/usr/bin/env python3
"""
Untapped First-Principles Black Hole Predictions
=================================================

Generates a 5-panel figure demonstrating falsifiable AVE predictions
for black hole physics, all derived from the same impedance topology
without free parameters:

  1. Merger Ringdown vs. LIGO Data (cavity resonance)
  2. Iron Kα Line Profile (impedance band sub-peaks)
  3. Jet Impedance Map (polar vs. equatorial Γ)
  4. Hawking Temperature Scaling (impedance noise leakage)
  5. GW Memory Strain (residual lattice deformation)

All constants from ave.core.constants — zero free parameters.
"""

import os

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA
from ave.solvers.orbital_resonance import (
    LIGO_EVENTS,
    M_SUN,
    gw_memory_strain,
    hawking_temperature,
    iron_ka_line_profile,
    jet_impedance_map,
    ringdown_frequency,
    ringdown_Q_and_decay,
)

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_DIR = os.path.join(project_root, "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.style.use("dark_background")


def main() -> None:
    print("=" * 70)
    print("  UNTAPPED FIRST-PRINCIPLES BLACK HOLE PREDICTIONS")
    print("  AVE Impedance Framework — Zero Free Parameters")
    print("=" * 70)

    fig = plt.figure(figsize=(24, 10))
    fig.patch.set_facecolor("#0a0a1a")
    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.30)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 1: MERGER RINGDOWN vs LIGO
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor("#0a0a1a")

    M_range = np.linspace(10.0, 200.0, 200)  # solar masses
    f_schw = np.array([ringdown_frequency(m * M_SUN, 0.0) for m in M_range])
    f_kerr_07 = np.array([ringdown_frequency(m * M_SUN, 0.7) for m in M_range])

    ax1.plot(
        M_range,
        f_schw,
        color="#00ccff",
        linewidth=2,
        alpha=0.5,
        linestyle="--",
        label="Schwarzschild ($a_* = 0$)",
    )
    ax1.plot(M_range, f_kerr_07, color="#00ff88", linewidth=2.5, label="Kerr-corrected ($a_* = 0.7$)")

    # Overlay LIGO events with Kerr corrections
    colors_ligo = ["#ff4444", "#ff8844", "#ffcc44"]
    for i, (name, data) in enumerate(LIGO_EVENTS.items()):
        M_obs = data["M_final_solar"]
        f_obs = data["f_ring_obs"]
        a_star = data["a_star"]
        f_ave_schw = ringdown_frequency(M_obs * M_SUN, 0.0)
        f_ave_kerr = ringdown_frequency(M_obs * M_SUN, a_star)
        error_schw = abs(f_ave_schw - f_obs) / f_obs * 100
        error_kerr = abs(f_ave_kerr - f_obs) / f_obs * 100

        ax1.scatter(
            M_obs,
            f_obs,
            color=colors_ligo[i],
            s=120,
            marker="*",
            zorder=10,
            edgecolors="white",
            linewidths=0.5,
            label=f"{name}: {f_obs} Hz",
        )
        ax1.scatter(
            M_obs,
            f_ave_kerr,
            color="#00ff88",
            s=80,
            marker="o",
            zorder=10,
            edgecolors="white",
            linewidths=0.5,
        )
        ax1.plot([M_obs, M_obs], [f_obs, f_ave_kerr], ":", color="white", alpha=0.4)

        print(f"  {name}: Schw={f_ave_schw:.0f} Hz, Kerr(a*={a_star})={f_ave_kerr:.0f} Hz, Obs={f_obs} Hz")
        print(f"          Error: Schw={error_schw:.1f}%, Kerr={error_kerr:.1f}%")

    ax1.set_xlabel("Final Mass [$M_\\odot$]", fontsize=11, color="white")
    ax1.set_ylabel("Ringdown Frequency [Hz]", fontsize=11, color="white")
    ax1.set_title("1. Merger Ringdown\nvs. LIGO Data (Kerr-corrected)", fontsize=13, color="white", pad=10)
    ax1.legend(fontsize=7, loc="upper right")
    ax1.grid(True, alpha=0.15)
    ax1.set_yscale("log")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 2: IRON Kα LINE PROFILE
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor("#0a0a1a")

    M_bh = 10.0 * M_SUN
    E_centers, flux, band_E = iron_ka_line_profile(M_bh, a_star=0.0)

    ax2.fill_between(E_centers, 0, flux, color="#ff6600", alpha=0.3)
    ax2.plot(E_centers, flux, color="#ff6600", linewidth=2, label="Fe Kα Profile")

    # Mark impedance band sub-peaks
    for i, be in enumerate(band_E):
        color = plt.cm.viridis(i / 6.0)
        ax2.axvline(be, color=color, linestyle="--", alpha=0.7, linewidth=1.2)
        ax2.text(be, 0.85 - i * 0.12, f"n={i+1}", color=color, fontsize=9, ha="center", fontweight="bold")

    ax2.axvline(6.4, color="white", linestyle=":", alpha=0.4, label="Rest frame 6.4 keV")
    ax2.set_xlabel("Energy [keV]", fontsize=11, color="white")
    ax2.set_ylabel("Relative Flux", fontsize=11, color="white")
    ax2.set_title("2. Iron Kα Line Profile\n(Impedance Band Sub-Peaks)", fontsize=13, color="white", pad=10)
    ax2.set_xlim(2.0, 7.5)
    ax2.legend(fontsize=9, loc="upper left")
    ax2.grid(True, alpha=0.15)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 3: JET IMPEDANCE MAP (2D Γ(r,θ))
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax3 = fig.add_subplot(gs[0, 2], polar=True)
    ax3.set_facecolor("#0a0a1a")

    M_jet = 10.0 * M_SUN
    R_map, Theta_map, Gamma_map = jet_impedance_map(M_jet, a_star=0.9)

    # Plot in polar coords (r vs theta)
    pcm = ax3.pcolormesh(Theta_map, R_map, Gamma_map, cmap="inferno", vmin=0, vmax=1.0, shading="auto")
    cbar = fig.colorbar(pcm, ax=ax3, shrink=0.6, pad=0.1)
    cbar.set_label(r"$\Gamma(r, \theta)$", color="white", fontsize=10)
    cbar.ax.yaxis.set_tick_params(color="white")
    plt.setp(cbar.ax.get_yticklabels(), color="white")

    # Annotate jet channel
    ax3.annotate(
        "JET\n$\\Gamma \\approx 0$",
        xy=(0.0, 3.0),
        fontsize=10,
        color="#00ff88",
        fontweight="bold",
        ha="center",
    )
    ax3.annotate(
        "DISK\n$\\Gamma \\to 1$",
        xy=(np.pi / 2, 5.0),
        fontsize=9,
        color="#ff4444",
        fontweight="bold",
        ha="center",
    )

    ax3.set_title("3. Jet Launching:\nPolar Impedance Matching", fontsize=13, color="white", pad=20)
    ax3.tick_params(colors="white")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 4: HAWKING TEMPERATURE SCALING
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.set_facecolor("#0a0a1a")

    M_hawk = np.logspace(-1, 10, 500) * M_SUN  # 0.1 to 10^10 M☉
    T_hawk = np.array([hawking_temperature(m) for m in M_hawk])

    ax4.plot(
        M_hawk / M_SUN,
        T_hawk,
        color="#ff66cc",
        linewidth=2.5,
        label=r"$T_H = \hbar c^3 / (8\pi G M k_B)$",
    )

    # Mark specific objects
    targets = [
        (14.0, "GRS 1915", "#00ccff"),
        (4.0e6, "Sgr A*", "#ffaa00"),
        (6.5e9, "M87*", "#ff4444"),
    ]
    for M_t, name, col in targets:
        T_t = hawking_temperature(M_t * M_SUN)
        ax4.scatter(M_t, T_t, color=col, s=100, zorder=10, edgecolors="white", linewidths=0.5)
        ax4.annotate(
            name,
            (M_t, T_t),
            textcoords="offset points",
            xytext=(10, 10),
            color=col,
            fontsize=9,
            fontweight="bold",
        )

    ax4.set_xscale("log")
    ax4.set_yscale("log")
    ax4.set_xlabel("Mass [$M_\\odot$]", fontsize=11, color="white")
    ax4.set_ylabel("Hawking Temperature [K]", fontsize=11, color="white")
    ax4.set_title("4. Hawking Temperature\n(Impedance Boundary Noise)", fontsize=13, color="white", pad=10)
    ax4.legend(fontsize=9, loc="upper right")
    ax4.grid(True, alpha=0.15, which="both")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 5: GW MEMORY STRAIN
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.set_facecolor("#0a0a1a")

    h_peak = np.logspace(-25, -1, 500)
    h_memory = gw_memory_strain(h_peak)

    ax5.plot(
        h_peak,
        h_memory,
        color="#00ff88",
        linewidth=2.5,
        label=r"$\Delta h = h_{peak} \cdot (h/h_{yield})^2$",
    )
    ax5.axvline(
        np.sqrt(ALPHA),
        color="#ffaa00",
        linestyle="--",
        alpha=0.7,
        label=f"$h_{{yield}} = \\sqrt{{\\alpha}} \\approx {np.sqrt(ALPHA):.4f}$",
    )

    # Mark LIGO sensitivity
    ax5.axvline(1e-21, color="#ff4444", linestyle=":", alpha=0.5, label="LIGO sensitivity ($10^{-21}$)")

    ax5.set_xscale("log")
    ax5.set_yscale("log")
    ax5.set_xlabel("Peak GW Strain $h_{peak}$", fontsize=11, color="white")
    ax5.set_ylabel("Memory Strain $\\Delta h_{memory}$", fontsize=11, color="white")
    ax5.set_title("5. GW Memory\n(Residual Lattice Deformation)", fontsize=13, color="white", pad=10)
    ax5.legend(fontsize=8, loc="upper left")
    ax5.grid(True, alpha=0.15, which="both")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # PANEL 6: AXIOM 4 CAVITY Q & DECAY TIME
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.set_facecolor("#0a0a1a")

    events = list(LIGO_EVENTS.keys())
    x_ev = np.arange(len(events))
    width = 0.25

    tau_ave_vals = []
    tau_obs_vals = []
    Q_vals = []

    for name in events:
        data = LIGO_EVENTS[name]
        M_f = data["M_final_solar"] * M_SUN
        a_s = data["a_star"]
        Q, tau, f = ringdown_Q_and_decay(M_f, a_s, saturated=True)
        tau_ave_vals.append(tau * 1e3)  # ms
        tau_obs_vals.append(data["tau_ring_obs"] * 1e3)  # ms
        Q_vals.append(Q)

    ax6.bar(
        x_ev - width / 2,
        tau_ave_vals,
        width,
        color="#00ff88",
        alpha=0.8,
        edgecolor="white",
        linewidth=0.5,
        label="AVE (Axiom 4 sat.)",
    )
    ax6.bar(
        x_ev + width / 2,
        tau_obs_vals,
        width,
        color="#ff4444",
        alpha=0.8,
        edgecolor="white",
        linewidth=0.5,
        label="LIGO Observed",
    )

    for i, name in enumerate(events):
        err = abs(tau_ave_vals[i] - tau_obs_vals[i]) / tau_obs_vals[i] * 100
        ax6.text(
            i,
            max(tau_ave_vals[i], tau_obs_vals[i]) + 0.5,
            f"Q={Q_vals[i]:.1f}\n{err:.0f}%",
            ha="center",
            fontsize=9,
            color="#00ff88",
            fontweight="bold",
        )

    ax6.set_xticks(x_ev)
    ax6.set_xticklabels(events, fontsize=10, color="white")
    ax6.set_ylabel("Decay Time $\\tau_{ring}$ [ms]", fontsize=11, color="white")
    ax6.set_title(
        "6. Axiom 4 Cavity Q\n$n_{max} = 1/\\sqrt{\\alpha}$ Saturation",
        fontsize=13,
        color="white",
        pad=10,
    )
    ax6.legend(fontsize=9, loc="upper left")
    ax6.grid(True, alpha=0.15, axis="y")

    # ── Save ──
    fig.suptitle(
        r"$\mathbf{Untapped\ First\text{-}Principles\ Predictions}$" + "\n"
        r"All derived from $Z = \sqrt{\mu/\varepsilon}$ impedance topology — zero free parameters",
        color="white",
        fontsize=16,
        y=1.02,
    )

    out_path = os.path.join(OUTPUT_DIR, "bh_untapped_predictions.png")
    plt.savefig(out_path, dpi=250, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"\n[*] Saved figure: {out_path}")

    # ── Console ringdown comparison ──
    print(f"\n{'─' * 70}")
    print("  MERGER RINGDOWN: AVE vs LIGO")
    print(f"{'─' * 70}")
    for name, data in LIGO_EVENTS.items():
        M_f = data["M_final_solar"] * M_SUN
        a_star = data["a_star"]
        f_schw = ringdown_frequency(M_f, 0.0)
        f_kerr = ringdown_frequency(M_f, a_star)
        f_obs = data["f_ring_obs"]
        Q, tau, _ = ringdown_Q_and_decay(M_f, a_star, saturated=True)
        tau_obs = data["tau_ring_obs"]
        err_f = abs(f_kerr - f_obs) / f_obs * 100
        err_t = abs(tau - tau_obs) / tau_obs * 100
        print(
            f"  {name:12s}: f_Kerr={f_kerr:7.1f} Hz ({err_f:4.1f}%) | Q={Q:.1f}"
            f" | τ={tau*1e3:.2f} ms ({err_t:.1f}%) | Obs: f={f_obs} Hz, τ={tau_obs*1e3:.1f} ms"
        )

    print(f"\n{'=' * 70}")
    print("  DONE")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
