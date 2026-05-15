#!/usr/bin/env python3
"""
Higgs Rupture: First-Principles Dielectric Breakdown Simulation
================================================================

The Higgs mechanism in AVE is not spontaneous symmetry breaking of a
scalar field. It is the literal dielectric rupture of a lattice node
when the local field exceeds V_snap:

DERIVATION CHAIN:
─────────────────
1. V_snap = m_e c²√α / e ≈ 43.65 kV        (Axiom 4 dielectric limit per node)
2. S(V) = √(1 - (V/V_snap)²)               (Saturation factor)
3. ε_eff = ε₀ × S(V)                         (Compliance drops under strain)
4. When V → V_snap: S → 0, ε_eff → 0        (Local compliance destroyed)
5. Destroyed compliance → trapped mass:
   M_W = m_e / (α² p_c √(3/7)) ≈ 79,923 MeV  (W boson)
   M_Z = M_W × 3/√7 ≈ 90,624 MeV              (Z boson)
6. Threshold: E_collision > 2M_W ≈ 160 GeV    (pair production)
7. Higgs boson = radial breathing mode of K4 cell:
   m_H = v/2 ≈ 124,417 MeV   (v = Higgs VEV)

All from ave.core.constants and ave.core.universal_operators.

Usage:
    python src/scripts/vol_2_subatomic/simulate_higgs_rupture.py
"""

import os

import matplotlib
import numpy as np

from ave.core.constants import (
    ALPHA,
    C_0,
    EPSILON_0,
    HIGGS_VEV_MEV,
    L_NODE,
    LAMBDA_HIGGS,
    M_E,
    M_HIGGS_MEV,
    M_W_MEV,
    M_Z_MEV,
    P_C,
    V_SNAP,
    V_YIELD,
    e_charge,
)
from ave.core.universal_operators import universal_saturation

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.gridspec import GridSpec  # noqa: E402


def run_simulation() -> None:
    # ── PREREQUISITE GATE: identify operating regime at V_snap ──
    # regime = identify_regime("em_voltage", V_local=float(V_SNAP))  # bulk lint fixup pass
    print()

    print("=" * 78)
    print("  HIGGS RUPTURE: DIELECTRIC BREAKDOWN OF THE LC LATTICE")
    print("  All from ave.core.constants + universal_saturation operator")
    print("=" * 78)

    m_e_MeV = M_E * C_0**2 / (e_charge * 1e6)

    print("\n  ── ENGINE CONSTANTS ──")
    print(f"    V_snap        = {float(V_SNAP):.2f} V  ({float(V_SNAP)/1e3:.2f} kV)")
    print(f"    V_yield       = √α × V_snap = {float(V_YIELD):.2f} V")
    print(f"    ℓ_node        = {float(L_NODE):.3e} m")
    print(f"    α             = 1/{1/ALPHA:.2f}")

    print("\n  ── PARTICLE MASSES FROM DIELECTRIC RUPTURE ──")
    print(f"    M_W   = {float(M_W_MEV):.0f} MeV  (PDG: 80,379)")
    print(f"    M_Z   = {float(M_Z_MEV):.0f} MeV  (PDG: 91,188)")
    print(f"    m_H   = {float(M_HIGGS_MEV):.0f} MeV  (PDG: 125,100)")
    print(f"    v     = {float(HIGGS_VEV_MEV):.0f} MeV  (Higgs VEV)")
    print(f"    λ_H   = 1/(2N_K4) = {float(LAMBDA_HIGGS):.4f}")

    # ── Pair production threshold ──────────────────────────────────────────
    E_threshold_MeV = 2.0 * float(M_W_MEV)
    print("\n  ── PAIR PRODUCTION THRESHOLDS ──")
    print(f"    W+W-:  {E_threshold_MeV:.0f} MeV  ({E_threshold_MeV/1e3:.1f} GeV)")
    print(f"    ZZ:    {2*float(M_Z_MEV):.0f} MeV  ({2*float(M_Z_MEV)/1e3:.1f} GeV)")
    print(f"    HH:    {2*float(M_HIGGS_MEV):.0f} MeV  ({2*float(M_HIGGS_MEV)/1e3:.1f} GeV)")

    # ══════════════════════════════════════════════════════════════════════════
    # SIMULATION: Collision energy ramp → dielectric rupture
    # ══════════════════════════════════════════════════════════════════════════

    # Time axis (arbitrary units — represents collision evolution)
    t = np.linspace(0, 10, 2000)

    # Collision energy profile: Gaussian pulse peaking above 2M_W
    E_peak_MeV = 200e3  # 200 GeV peak
    E_collision = E_peak_MeV * np.exp(-(((t - 4.0) / 0.5) ** 2))

    # Map collision energy to local voltage on the lattice node
    # E_collision = e × V_local → V_local = E_collision / e
    # But we normalize to V_snap for the saturation operator
    # V_ratio = E_collision / (float(V_SNAP) * e_charge / (e_charge * 1e6))  # V/V_snap in MeV terms
    # bulk lint fixup pass

    # Actually: the local voltage per node during collision is
    # V_local = E_collision_MeV / (m_e_MeV × c² / (e × V_snap))
    # Key ratio: E/E_snap where E_snap = e × V_snap = m_e c² √α
    E_snap_MeV = m_e_MeV * np.sqrt(ALPHA)
    ratio = E_collision / E_snap_MeV

    # Saturation factor S(V/V_snap)
    S = np.array([universal_saturation(r, 1.0) for r in ratio])

    # Effective dielectric compliance
    eps_eff = float(EPSILON_0) * S

    # Effective impedance
    # Z_eff = np.where(S > 1e-10, float(Z_0) / np.sqrt(S), float(Z_0) * 1e5)  # bulk lint fixup pass

    # Mass generation: when S drops below threshold, a massive boson forms
    # The "born mass" is the trapped energy from the ruptured cell
    mass_generated = np.where(S < 0.1, float(M_W_MEV), 0.0)

    print("\n  ── RUPTURE DYNAMICS ──")
    print(f"    Peak collision energy: {E_peak_MeV/1e3:.0f} GeV")
    print(f"    E_snap = m_e√α = {E_snap_MeV:.4f} MeV")
    print(f"    Peak ratio E/E_snap: {E_peak_MeV/E_snap_MeV:.1f}")
    print(f"    Saturation at peak: S = {universal_saturation(E_peak_MeV/E_snap_MeV, 1.0):.6f}")
    print(f"    Boson mass generated: {float(M_W_MEV):.0f} MeV (when S < 0.1)")

    # ══════════════════════════════════════════════════════════════════════════
    # PLOTTING
    # ══════════════════════════════════════════════════════════════════════════

    C_BG = "#0a0a1a"
    C_TEXT = "#e0e0e0"
    C_GRID = "#1a2a3a"

    fig = plt.figure(figsize=(20, 12))
    fig.patch.set_facecolor(C_BG)
    gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

    def style_ax(ax: plt.Axes) -> None:
        ax.set_facecolor(C_BG)
        ax.tick_params(colors=C_TEXT, labelsize=9)
        ax.grid(True, alpha=0.12, color=C_GRID)
        for spine in ax.spines.values():
            spine.set_color("#333355")

    # Panel 1: Collision energy + W+W- threshold
    ax1 = fig.add_subplot(gs[0, 0])
    style_ax(ax1)
    ax1.plot(t, E_collision / 1e3, color="#00ccff", linewidth=2.5, label="Collision Energy")
    ax1.axhline(
        y=2 * float(M_W_MEV) / 1e3,
        color="#ff4444",
        linewidth=2,
        linestyle="--",
        label=f"$2M_W$ = {2*float(M_W_MEV)/1e3:.0f} GeV",
    )
    ax1.axhline(
        y=2 * float(M_Z_MEV) / 1e3,
        color="#ffaa44",
        linewidth=1.5,
        linestyle=":",
        label=f"$2M_Z$ = {2*float(M_Z_MEV)/1e3:.0f} GeV",
    )
    ax1.fill_between(
        t,
        2 * float(M_W_MEV) / 1e3,
        E_collision / 1e3,
        where=E_collision > 2 * float(M_W_MEV),
        color="#ff4444",
        alpha=0.15,
        label="Rupture Zone",
    )
    ax1.set_xlabel("Time (arb.)", color=C_TEXT, fontsize=10)
    ax1.set_ylabel("Energy (GeV)", color=C_TEXT, fontsize=10)
    ax1.set_title(
        "Collision Energy vs\nPair Production Threshold",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax1.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)

    # Panel 2: Saturation factor during collision
    ax2 = fig.add_subplot(gs[0, 1])
    style_ax(ax2)
    ax2.plot(t, S, color="#44ff88", linewidth=2.5, label=r"$S(V) = \sqrt{1-(V/V_{snap})^2}$")
    ax2.axhline(
        y=0.1,
        color="#ff4444",
        linewidth=1,
        linestyle=":",
        alpha=0.5,
        label="Rupture threshold (S < 0.1)",
    )
    ax2.fill_between(t, 0, S, where=S < 0.1, color="#ff4444", alpha=0.2)
    ax2.set_xlabel("Time (arb.)", color=C_TEXT, fontsize=10)
    ax2.set_ylabel("Saturation Factor S", color=C_TEXT, fontsize=10)
    ax2.set_title("Dielectric Saturation:\nCompliance Collapse", color=C_TEXT, fontsize=13, fontweight="bold")
    ax2.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax2.set_ylim(-0.05, 1.1)

    # Panel 3: ε_eff and mass generation
    ax3 = fig.add_subplot(gs[0, 2])
    style_ax(ax3)
    ax3_twin = ax3.twinx()
    ax3_twin.set_facecolor(C_BG)
    ax3.plot(
        t,
        eps_eff / float(EPSILON_0),
        color="#44aaff",
        linewidth=2.5,
        label=r"$\varepsilon_{eff}/\varepsilon_0 = S(V)$",
    )
    ax3_twin.plot(
        t,
        mass_generated / 1e3,
        color="#ffaa44",
        linewidth=2.5,
        label=f"Born mass (M_W = {float(M_W_MEV)/1e3:.1f} GeV)",
    )
    ax3.set_xlabel("Time (arb.)", color=C_TEXT, fontsize=10)
    ax3.set_ylabel(r"$\varepsilon_{eff}/\varepsilon_0$", color="#44aaff", fontsize=10)
    ax3_twin.set_ylabel("Generated Mass (GeV)", color="#ffaa44", fontsize=10)
    ax3.set_title("Phase Transition:\nCompliance → Mass", color=C_TEXT, fontsize=13, fontweight="bold")
    ax3.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT, loc="center left")
    ax3_twin.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT, loc="center right")
    ax3_twin.tick_params(colors="#ffaa44")

    # Panel 4: Static saturation curve with particle mass markers
    ax4 = fig.add_subplot(gs[1, 0])
    style_ax(ax4)
    V_range = np.linspace(0, 1.2, 500) * float(V_SNAP)
    S_static = np.array([universal_saturation(V / float(V_SNAP), 1.0) for V in V_range])
    ax4.plot(
        V_range / float(V_SNAP),
        S_static,
        color="#44ff88",
        linewidth=2.5,
        label=r"$S(V) = \sqrt{1 - (V/V_{snap})^2}$",
    )
    ax4.axvline(
        x=1.0,
        color="#ff4444",
        linewidth=2,
        linestyle="--",
        label=f"$V_{{snap}}$ = {float(V_SNAP)/1e3:.2f} kV",
    )
    ax4.axvline(
        x=float(V_YIELD) / float(V_SNAP),
        color="#ffaa44",
        linewidth=1.5,
        linestyle=":",
        label="$V_{{yield}}$ = $\\sqrt{{α}}V_{{snap}}$",
    )
    ax4.scatter(
        [1.0],
        [0.0],
        color="#ff4444",
        s=150,
        zorder=5,
        edgecolors="#ffffff",
        label="Full rupture → W/Z boson",
    )
    ax4.set_xlabel(r"$V / V_{snap}$", color=C_TEXT, fontsize=10)
    ax4.set_ylabel("Saturation Factor S", color=C_TEXT, fontsize=10)
    ax4.set_title(
        "Dielectric Saturation Curve:\nAxiom 4 Operator",
        color=C_TEXT,
        fontsize=13,
        fontweight="bold",
    )
    ax4.legend(fontsize=8, facecolor="#111133", edgecolor="#333355", labelcolor=C_TEXT)
    ax4.set_xlim(0, 1.3)

    # Panel 5: Derivation chain text
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.set_facecolor(C_BG)
    ax5.axis("off")

    chain_text = (
        "HIGGS MECHANISM = DIELECTRIC RUPTURE\n"
        "════════════════════════════════════\n\n"
        f"V_snap = m_e c²√α / e = {float(V_SNAP)/1e3:.2f} kV\n"
        "    ↓\n"
        f"S(V) = √(1 - (V/V_snap)²)\n"
        "    ↓\n"
        f"When V → V_snap: S → 0\n"
        f"  ε_eff → 0 (compliance destroyed)\n"
        "    ↓\n"
        f"Trapped energy → rest mass:\n"
        f"  M_W = {float(M_W_MEV):.0f} MeV\n"
        f"  M_Z = {float(M_Z_MEV):.0f} MeV\n"
        "    ↓\n"
        f"Higgs = K4 breathing mode:\n"
        f"  m_H = v/√N_K4 = v/2\n"
        f"     = {float(M_HIGGS_MEV):.0f} MeV\n"
        f"  λ = 1/8 = {float(LAMBDA_HIGGS):.3f}"
    )
    ax5.text(
        0.05,
        0.95,
        chain_text,
        transform=ax5.transAxes,
        fontfamily="monospace",
        fontsize=10,
        color="#44ff88",
        verticalalignment="top",
    )

    # Panel 6: Particle mass spectrum from rupture
    ax6 = fig.add_subplot(gs[1, 2])
    style_ax(ax6)

    particles = ["e", "μ", "τ", "W", "Z", "H"]
    masses_ave = [
        m_e_MeV,
        m_e_MeV / (ALPHA * np.sqrt(3 / 7)),
        m_e_MeV * float(P_C) / ALPHA**2,
        float(M_W_MEV),
        float(M_Z_MEV),
        float(M_HIGGS_MEV),
    ]
    colors = ["#44aaff", "#44aaff", "#44aaff", "#ff4444", "#ff4444", "#ffaa44"]
    labels = [
        "Topological\n(unknot)",
        "Topological\n(Cosserat)",
        "Topological\n(bending)",
        "Rupture\n(torsion)",
        "Rupture\n(mixing)",
        "Breathing\n(K4 cell)",
    ]

    x = np.arange(len(particles))
    bars = ax6.bar(x, np.log10(masses_ave), color=colors, alpha=0.85, edgecolor="#333355", linewidth=1.5)
    ax6.set_xticks(x)
    ax6.set_xticklabels([f"${p}$\n{l}" for p, l in zip(particles, labels)], color=C_TEXT, fontsize=8)
    ax6.set_ylabel(r"$\log_{10}(m$ / MeV$)$", color=C_TEXT, fontsize=10)
    ax6.set_title("Mass Spectrum:\nTopological vs Rupture", color=C_TEXT, fontsize=13, fontweight="bold")

    for bar, m in zip(bars, masses_ave):
        ax6.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            f"{m:.0f}" if m > 1 else f"{m:.3f}",
            ha="center",
            va="bottom",
            color=C_TEXT,
            fontsize=8,
            fontweight="bold",
        )

    fig.suptitle(
        "Higgs Rupture: Dielectric Breakdown of the LC Lattice\n"
        r"$S(V) = \sqrt{1-(V/V_{snap})^2}$  |  "
        r"$V_{snap} = m_e c^2\sqrt{\alpha}/e$  |  "
        r"All from $\mathtt{ave.core.constants}$",
        color=C_TEXT,
        fontsize=14,
        fontweight="black",
        y=0.995,
    )

    plt.tight_layout(rect=[0, 0, 1, 0.93])

    out_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "electroweak_dielectric_spark.png")
    plt.savefig(out_path, dpi=200, facecolor=C_BG, bbox_inches="tight")
    print(f"\n  ✓ Plot saved → {out_path}")
    print("\n  ═══ HIGGS RUPTURE SIMULATION COMPLETE ═══")


if __name__ == "__main__":
    run_simulation()
