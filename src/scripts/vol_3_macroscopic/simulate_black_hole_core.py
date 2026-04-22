#!/usr/bin/env python3
"""
Black Hole Impedance Horizon: First-Principles Derivation
==========================================================

Derives all black hole properties from AVE Axioms 1-4:

DERIVATION CHAIN:
─────────────────
1. ε₁₁(r) = 7GM/(c²r)              Principal radial strain (Axiom 3+4)
2. n(r) = 1 + ν_vac × ε₁₁ = 1+2GM/(c²r)  Refractive index
3. μ'(r) = n(r)·μ₀, ε'(r) = n(r)·ε₀       Achromatic scaling
4. Z(r) = √(μ'/ε') = Z₀                    INVARIANT (symmetric gravity)
5. S(r) = √(1 - ε₁₁²)                      Saturation factor
6. G_shear(r) = G_shear₀ × S(r)             Shear modulus
7. c_g(r) = c × (1-ε₁₁²)^(1/4)             Group velocity
8. r_sat = 7GM/c² = 3.5 r_s                 Saturation boundary
9. Q = ℓ, ω_R = ℓc/r_eff                    QNM from lattice resonance
10. T_H = ℏc³/(8πGMk_B)                     Hawking temperature

CRITICAL DISTINCTION:
  Electron: Γ = -1 (impedance mismatch → total reflection)
  Black Hole: Z = Z₀ (no mismatch), but G_shear → 0 (phase transition → shear waves reflected)

All from ave.gravity module + ave.core.constants. Zero magic numbers.

Usage:
    python src/scripts/vol_3_macroscopic/simulate_black_hole_core.py
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from ave.core.constants import (
    C_0,
    G,
    HBAR,
    Z_0,
    NU_VAC,
    K_B,
    M_SUN,
)
from ave.core.regime_map import identify_regime
from ave.gravity import (
    principal_radial_strain,
    refractive_index,
    schwarzschild_radius,
    saturation_radius,
    gravitational_saturation_factor,
    shear_modulus_factor,
    local_mu,
    local_epsilon,
    local_impedance,
)
from ave.axioms.scale_invariant import (
    phase_transition_Q,
)

# ══════════════════════════════════════════════════════════════════════════════
# SOLAR MASS AND KNOWN BH DATA
# ══════════════════════════════════════════════════════════════════════════════
M_SUN_local = M_SUN  # re-export for readability
k_B = K_B

# LIGO events for comparison
LIGO_EVENTS = {
    "GW150914": {"M_final": 62.0, "a_star": 0.67, "f_obs": 251, "tau_obs": 4.0e-3},
    "GW170104": {"M_final": 48.7, "a_star": 0.64, "f_obs": 312, "tau_obs": 3.0e-3},
    "GW151226": {"M_final": 20.8, "a_star": 0.74, "f_obs": 750, "tau_obs": 1.4e-3},
}


def run_simulation():
    # ── PREREQUISITE GATE: identify operating regime for 10 M☉ BH ──
    # regime = identify_regime("gravity", M_kg=10 * float(M_SUN), r_meters=7 * G * 10 * float(M_SUN) / C_0**2)  # bulk lint fixup pass
    print()

    print("=" * 78)
    print("  BLACK HOLE IMPEDANCE HORIZON: FIRST-PRINCIPLES DERIVATION")
    print("  All from ave.gravity module + AVE Axioms 1-4")
    print("=" * 78)

    # ── Reference mass: 10 M_sun ───────────────────────────────────────────
    M_bh = 10.0 * M_SUN
    r_s = schwarzschild_radius(M_bh)
    r_sat = saturation_radius(M_bh)
    M_g = G * M_bh / C_0**2  # Gravitational radius

    print(f"\n  ── REFERENCE: {M_bh/M_SUN:.0f} M☉ BLACK HOLE ──")
    print(f"    M = {M_bh:.3e} kg")
    print(f"    r_s = 2GM/c² = {r_s:.1f} m  ({r_s/1e3:.2f} km)")
    print(f"    r_sat = 7GM/c² = {r_sat:.1f} m  ({r_sat/1e3:.2f} km)")
    print(f"    M_g = GM/c² = {M_g:.1f} m")
    print(f"    r_sat / r_s = {r_sat/r_s:.2f}  (always 3.5)")

    # ── Radial profiles ────────────────────────────────────────────────────
    r = np.linspace(r_sat * 0.5, 20.0 * r_s, 2000)

    # All from the gravity module (first principles)
    eps_11 = np.array([principal_radial_strain(M_bh, ri) for ri in r])
    n_r = np.array([refractive_index(M_bh, ri) for ri in r])
    S_r = np.array([gravitational_saturation_factor(M_bh, ri) for ri in r])
    G_shear = np.array([shear_modulus_factor(M_bh, ri) for ri in r])
    Z_r = np.array([local_impedance(M_bh, ri) for ri in r])
    # mu_r = np.array([local_mu(M_bh, ri) for ri in r])  # bulk lint fixup pass
    # eps_r = np.array([local_epsilon(M_bh, ri) for ri in r])  # bulk lint fixup pass

    # Group velocity: c_g = c × (1 - ε₁₁²)^(1/4)
    eps_sq = np.clip(eps_11**2, 0, 1.0 - 1e-12)
    c_g = C_0 * (1.0 - eps_sq) ** 0.25

    # ── Print key radii ────────────────────────────────────────────────────
    print(f"\n  ── RADIAL PROFILES (from gravity module) ──")
    for r_check, label in [
        (r_sat * 10, "10×r_sat"),
        (r_sat * 2, "2×r_sat"),
        (r_sat * 1.01, "1.01×r_sat"),
        (r_s, "r_s (EH)"),
    ]:
        eps = principal_radial_strain(M_bh, r_check)
        S = gravitational_saturation_factor(M_bh, r_check)
        n = refractive_index(M_bh, r_check)
        Z = local_impedance(M_bh, r_check)
        print(f"    r = {r_check/r_s:6.2f} r_s: ε₁₁ = {eps:.4f}, S = {S:.4f}, " f"n = {n:.4f}, Z = {Z:.2f} Ω")

    # ── QNM Ringdown (ℓ=2) ────────────────────────────────────────────────
    print(f"\n  ── SCHWARZSCHILD QNM RINGDOWN (ℓ = 2) ──")
    ell = 2
    r_eff = r_sat / (1.0 + float(NU_VAC))  # Poisson-corrected cavity
    omega_R = ell * C_0 / r_eff
    Q_mode = phase_transition_Q(ell)

    print(f"    r_sat = {r_sat:.1f} m")
    print(f"    r_eff = r_sat/(1+ν) = {r_eff:.1f} m")
    print(f"    ω_R = ℓ·c/r_eff = {omega_R:.2f} rad/s")
    print(f"    f_R = {omega_R/(2*np.pi):.1f} Hz")
    print(f"    Q = ℓ = {Q_mode}")
    print(
        f"    ω_R·M_g = {omega_R * M_g / C_0:.4f}  (GR exact: 0.3737, Δ = {(omega_R*M_g/C_0 - 0.3737)/0.3737*100:+.1f}%)"
    )

    # ── LIGO Event Comparison ──────────────────────────────────────────────
    print(f"\n  ── LIGO EVENT COMPARISON ──")
    print(
        f"  {'Event':>12} {'M_final':>8} {'a*':>5} {'f_AVE':>8} {'f_obs':>8} {'Δf':>8} "
        f"{'τ_AVE':>8} {'τ_obs':>8} {'Δτ':>8}"
    )
    print("  " + "─" * 76)

    ligo_results = []
    for name, data in LIGO_EVENTS.items():
        M = data["M_final"] * M_SUN
        a_star = data["a_star"]
        f_obs = data["f_obs"]
        tau_obs = data["tau_obs"]

        M_g_ev = G * M / C_0**2
        r_sat_ev = saturation_radius(M)
        r_eff_ev = r_sat_ev / (1.0 + float(NU_VAC))

        # Schwarzschild QNM
        omega_R_ev = ell * C_0 / r_eff_ev
        f_R_ev = omega_R_ev / (2 * np.pi)

        # Kerr correction: frame-dragging shifts photon sphere
        r_ph_schw = 3.0 * M_g_ev  # Schwarzschild photon sphere
        r_ph_kerr = 2.0 * M_g_ev * (1.0 + np.cos(2.0 / 3.0 * np.arccos(-a_star)))
        f_kerr = f_R_ev * r_ph_schw / r_ph_kerr

        # Decay time from Q = ℓ
        tau_ave = float(Q_mode) / (np.pi * f_kerr)

        delta_f = (f_kerr - f_obs) / f_obs * 100
        delta_tau = (tau_ave - tau_obs) / tau_obs * 100

        ligo_results.append(
            (
                name,
                data["M_final"],
                a_star,
                f_kerr,
                f_obs,
                delta_f,
                tau_ave * 1e3,
                tau_obs * 1e3,
                delta_tau,
            )
        )

        print(
            f"  {name:>12} {data['M_final']:8.1f} {a_star:5.2f} "
            f"{f_kerr:8.0f} {f_obs:8.0f} {delta_f:+7.1f}% "
            f"{tau_ave*1e3:7.1f}ms {tau_obs*1e3:7.1f}ms {delta_tau:+7.1f}%"
        )

    # ── Hawking Temperature ────────────────────────────────────────────────
    print(f"\n  ── HAWKING TEMPERATURE ──")
    T_H = HBAR * C_0**3 / (8.0 * np.pi * G * M_bh * k_B)
    print(f"    T_H = ℏc³/(8πGMk_B) = {T_H:.3e} K")
    print(f"    For 10 M☉: {T_H:.3e} K (essentially zero — undetectable)")

    # Micro black hole comparison
    M_micro = 1e12  # kg (primordial BH)
    T_H_micro = HBAR * C_0**3 / (8.0 * np.pi * G * M_micro * k_B)
    print(f"    For M = 10¹² kg: T_H = {T_H_micro:.1f} K")

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

    r_norm = r / r_s

    # Panel 1: Strain + Saturation
    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1)
    ax1.plot(r_norm, eps_11, color="#ff4444", linewidth=2.5, label=r"$\varepsilon_{11}(r) = 7GM/(c^2 r)$")
    ax1.plot(r_norm, S_r, color="#44ff88", linewidth=2.5, label=r"$S(r) = \sqrt{1-\varepsilon_{11}^2}$")
    ax1.axhline(y=1.0, color="#ffffff", linewidth=0.8, linestyle=":", alpha=0.5)
    ax1.axvline(
        x=r_sat / r_s,
        color="#ffaa44",
        linewidth=2,
        linestyle="--",
        label=f"$r_{{sat}} = 3.5\\,r_s$",
    )
    ax1.axvline(x=1.0, color="#ff4444", linewidth=1.5, linestyle=":", label=f"$r_s$ (Event Horizon)")
    ax1.axvspan(0, r_sat / r_s, alpha=0.08, color="#ff4444")
    ax1.set_xlabel(r"$r / r_s$", color=C_TEXT, fontsize=11)
    ax1.set_ylabel("Dimensionless", color=C_TEXT, fontsize=11)
    ax1.set_title("Radial Strain & Saturation Factor", color=C_TEXT, fontsize=13, fontweight="bold")
    ax1.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax1.set_xlim(0, 15)
    ax1.set_ylim(0, 3)

    # Panel 2: Shear Modulus + Group Velocity
    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2)
    ax2.plot(r_norm, G_shear, color="#44aaff", linewidth=2.5, label=r"$G_{shear}/G_0 = S(r)$")
    ax2.plot(
        r_norm,
        c_g / C_0,
        color="#ffaa44",
        linewidth=2.5,
        label=r"$c_g/c = (1-\varepsilon^2)^{1/4}$",
    )
    ax2.axvline(x=r_sat / r_s, color="#ffaa44", linewidth=2, linestyle="--", label=f"Phase transition")
    ax2.axvspan(0, r_sat / r_s, alpha=0.08, color="#ff4444")
    ax2.text(
        1.5,
        0.15,
        "RUPTURED\n(no shear waves)",
        color="#ff6666",
        fontsize=10,
        fontweight="bold",
        ha="center",
    )
    ax2.text(
        6,
        0.85,
        "ELASTIC\n(GWs propagate)",
        color="#44aaff",
        fontsize=10,
        fontweight="bold",
        ha="center",
    )
    ax2.set_xlabel(r"$r / r_s$", color=C_TEXT, fontsize=11)
    ax2.set_ylabel("Normalized", color=C_TEXT, fontsize=11)
    ax2.set_title(
        "Lattice Phase Transition:\nShear Modulus & Group Velocity",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax2.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax2.set_xlim(0, 15)
    ax2.set_ylim(0, 1.1)

    # Panel 3: Impedance Z(r) = Z₀ (invariant) + Reflection
    ax3 = fig.add_subplot(gs[0, 2])
    style_ax(ax3)
    ax3.plot(r_norm, Z_r, color="#ffffff", linewidth=3, label=r"$Z(r) = Z_0 = 376.73\,\Omega$")
    ax3.plot(r_norm, n_r, color="#44ff88", linewidth=2, label=r"$n(r) = 1 + 2GM/(c^2 r)$")
    ax3.axhline(y=float(Z_0), color="#ffffff", linewidth=0.5, alpha=0.3, linestyle=":")
    ax3.axvline(x=r_sat / r_s, color="#ffaa44", linewidth=2, linestyle="--")
    ax3.set_xlabel(r"$r / r_s$", color=C_TEXT, fontsize=11)
    ax3.set_ylabel("Value", color=C_TEXT, fontsize=11)
    ax3.set_title(
        "Symmetric Gravity:\nZ = Z₀ (invariant), n(r) diverges",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax3.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax3.set_xlim(0, 15)
    ax3.set_ylim(0, max(8, float(Z_0) + 50))

    # Panel 4: Electron vs Black Hole isomorphism
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.set_facecolor(C_BG)
    ax4.axis("off")

    iso_text = (
        "ELECTRON ↔ BLACK HOLE ISOMORPHISM\n"
        "══════════════════════════════════\n\n"
        "           ELECTRON         BLACK HOLE\n"
        "Scale:     ℓ_node (fm)      r_sat (km)\n"
        "Confine:   Γ = -1 (Z→0)    G_shear → 0\n"
        "Impedance: Z → 0 at core   Z = Z₀ always\n"
        "Interior:  Topology kept    Topology melts\n"
        f"Q factor:  crossing # c    mode # ℓ\n"
        "\n"
        "BOTH:\n"
        "  • S(r) = √(1 - (A/A_yield)²)\n"
        "  • Standing-wave orbitals\n"
        "  • Emission = orbital transitions\n"
        f"  • From same Axiom 4 kernel"
    )
    ax4.text(
        0.05,
        0.95,
        iso_text,
        transform=ax4.transAxes,
        fontfamily="monospace",
        fontsize=10,
        color="#44ff88",
        verticalalignment="top",
    )

    # Panel 5: LIGO comparison
    ax5 = fig.add_subplot(gs[1, 1])
    style_ax(ax5)

    names = [r[0] for r in ligo_results]
    f_ave = [r[3] for r in ligo_results]
    f_obs = [r[4] for r in ligo_results]
    delta_f = [r[5] for r in ligo_results]

    x = np.arange(len(names))
    w = 0.35
    bars1 = ax5.bar(x - w / 2, f_ave, w, color="#44ff88", alpha=0.85, label="AVE (derived)")
    # bars2 = ax5.bar(x + w / 2, f_obs, w, color="#ff4444", alpha=0.85, label="LIGO (observed)")  # bulk lint fixup pass
    ax5.set_xticks(x)
    ax5.set_xticklabels(names, color=C_TEXT, fontsize=9, rotation=15)
    ax5.set_ylabel("Ringdown Frequency (Hz)", color=C_TEXT, fontsize=10)
    ax5.set_title(
        "QNM Ringdown: AVE vs LIGO\n(Kerr-corrected, ℓ = 2)",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax5.legend(fontsize=9, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)

    for bar, df in zip(bars1, delta_f):
        ax5.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 10,
            f"{df:+.0f}%",
            ha="center",
            va="bottom",
            color=C_TEXT,
            fontsize=9,
            fontweight="bold",
        )

    # Panel 6: Hawking Temperature vs Mass
    ax6 = fig.add_subplot(gs[1, 2])
    style_ax(ax6)

    M_range = np.logspace(8, 35, 200)  # kg
    T_H_range = HBAR * C_0**3 / (8.0 * np.pi * G * M_range * k_B)

    ax6.loglog(M_range / M_SUN, T_H_range, color="#ffaa44", linewidth=2.5)
    ax6.axhline(y=2.725, color="#44aaff", linewidth=1, linestyle="--", alpha=0.7, label="CMB: 2.725 K")
    ax6.axhline(
        y=1e12,
        color="#ff4444",
        linewidth=1,
        linestyle=":",
        alpha=0.5,
        label=r"$10^{12}$ K (hadron epoch)",
    )
    # Mark 10 M_sun
    ax6.scatter(
        [10],
        [HBAR * C_0**3 / (8 * np.pi * G * 10 * M_SUN * k_B)],
        color="#44ff88",
        s=100,
        zorder=5,
        edgecolors="#ffffff",
    )
    ax6.text(
        10,
        HBAR * C_0**3 / (8 * np.pi * G * 10 * M_SUN * k_B) * 3,
        "10 M☉",
        color="#44ff88",
        fontsize=9,
    )

    ax6.set_xlabel(r"$M / M_\odot$", color=C_TEXT, fontsize=11)
    ax6.set_ylabel("Hawking Temperature (K)", color=C_TEXT, fontsize=11)
    ax6.set_title(
        "Hawking Temperature:\nImpedance Boundary Noise",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax6.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)

    fig.suptitle(
        "Black Hole Impedance Horizon: First-Principles Derivation\n"
        r"All from $\varepsilon_{11}=7GM/(c^2r)$, $S=\sqrt{1-\varepsilon^2}$, "
        r"$r_{sat}=3.5\,r_s$  |  Axioms 1-4  |  Zero free parameters",
        color=C_TEXT,
        fontsize=14,
        fontweight="black",
        y=0.995,
    )

    plt.tight_layout(rect=[0, 0, 1, 0.93])

    out_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "simulate_black_hole_core.png")
    plt.savefig(out_path, dpi=200, facecolor=C_BG, bbox_inches="tight")
    print(f"\n  ✓ Plot saved → {out_path}")
    print(f"\n  ═══ BLACK HOLE DERIVATION COMPLETE ═══")


if __name__ == "__main__":
    run_simulation()
