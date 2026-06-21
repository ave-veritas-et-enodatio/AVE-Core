"""
Derive α from the Golden Torus Trefoil Q-Factor.

Companion figure for Ch.8 (Zero-Parameter Closure). Renders the trefoil
(2,3) torus knot at dielectric ropelength (Golden Torus geometry:
R = φ/2, r = (φ-1)/2) with strain coloring, and annotates the multipole
decomposition of its impedance on T² ⊂ S³ ⊂ ℂ² into volumetric, surface,
and line terms:

    α⁻¹_ideal = Λ_vol + Λ_surf + Λ_line = 4π³ + π² + π ≈ 137.0363

Also asserts agreement between the closed-form expression and the engine's
ALPHA_COLD_INV constant (imported from ave.core.constants).

Output: assets/sim_outputs/trefoil_alpha_qfactor.png

Reference: manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex
"""

import sys
from pathlib import Path

import numpy as np

# Resolve the repo's src/ so `ave` + `ave_path_util` import when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ave.core.constants import ALPHA, ALPHA_COLD_INV, DELTA_STRAIN
from ave_path_util import sim_output

# ═══════════════════════════════════════════════════════════════════════════
# Pure-numeric module-level constants (safe to import)
# ═══════════════════════════════════════════════════════════════════════════
PHI = (1.0 + np.sqrt(5.0)) / 2.0  # Golden ratio
R_gt = PHI / 2.0  # Golden Torus major radius
r_gt = (PHI - 1.0) / 2.0  # Golden Torus minor radius


def golden_torus_multipole() -> dict[str, float]:
    """
    Evaluate the multipole decomposition of α⁻¹ on T² ⊂ S³ ⊂ ℂ² at the
    Golden Torus (R = φ/2, r = (φ-1)/2, d = 1).

    Returns
    -------
    dict
        Keys: Lambda_vol, Lambda_surf, Lambda_line, alpha_inv.
        Values satisfy Lambda_vol + Lambda_surf + Lambda_line = alpha_inv
        and alpha_inv == 4π³ + π² + π to machine precision.
    """
    Lambda_vol = 16.0 * np.pi**3 * (R_gt * r_gt)  # = 4π³
    Lambda_surf = 4.0 * np.pi**2 * (R_gt * r_gt)  # = π²
    Lambda_line = np.pi * 1.0  # = π (d = ℓ_node = 1)
    return {
        "Lambda_vol": Lambda_vol,
        "Lambda_surf": Lambda_surf,
        "Lambda_line": Lambda_line,
        "alpha_inv": Lambda_vol + Lambda_surf + Lambda_line,
    }


def render_figure(output_path: str | None = None) -> str:
    """Render the trefoil soliton figure at Golden Torus ropelength.

    House style (``ave.viz.style``): white print background, CMAP_SEQ strain
    colouring, NO baked title (the alpha headline belongs in the LaTeX caption).
    The geometry / multipole values stay as an in-figure data annotation box
    (legitimate data labels, not a caption). Physics is untouched — only the
    figure presentation is restyled.
    """
    import matplotlib

    matplotlib.use("Agg")  # headless: render-to-file driver

    import matplotlib.pyplot as plt

    from ave.viz import style

    style.apply()  # print profile (white background)

    mp = golden_torus_multipole()
    Lambda_vol = mp["Lambda_vol"]
    Lambda_surf = mp["Lambda_surf"]
    Lambda_line = mp["Lambda_line"]
    alpha_inv_computed = mp["alpha_inv"]

    # Parametric (2,3) torus knot on the Golden Torus
    t = np.linspace(0.0, 2.0 * np.pi, 1200)
    u = 2.0 * t  # strand 2 (p = 2 strands per major turn)
    v = 3.0 * t  # strand 3 (q = 3 crossings)
    x = (R_gt + r_gt * np.cos(v)) * np.cos(u)
    y = (R_gt + r_gt * np.cos(v)) * np.sin(u)
    z = r_gt * np.sin(v)

    dx = np.gradient(x)
    dy = np.gradient(y)
    dz = np.gradient(z)
    ddx = np.gradient(dx)
    ddy = np.gradient(dy)
    ddz = np.gradient(dz)
    strain = np.sqrt(ddx**2 + ddy**2 + ddz**2)
    strain /= strain.max()

    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot(x, y, z, color=style.COLORS["muted"], linewidth=0.8, alpha=0.45, zorder=1)
    sc = ax.scatter(
        x, y, z, c=strain, cmap=style.CMAP_SEQ, s=18, alpha=0.92,
        edgecolors="none", zorder=5,
    )

    for spine in ("left", "right", "top", "bottom"):
        if spine in ax.spines:
            ax.spines[spine].set_visible(False)
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Strain colorbar (Axis 2: quantity + symbol + unit, normalised → dimensionless).
    cb = fig.colorbar(sc, ax=ax, shrink=0.6, pad=0.02)
    cb.set_label(
        style.axis_label("Normalised strain", r"|\ddot{\mathbf{r}}|", "dimensionless")
    )

    # In-figure DATA annotation: geometry + multipole decomposition values. These
    # are data labels (the decomposition the figure exists to show), not a title —
    # the alpha headline / "electron soliton" framing belongs in the LaTeX caption.
    textstr = (
        rf"$R = \varphi/2 \approx {R_gt:.4f}$,  $r = (\varphi-1)/2 \approx {r_gt:.4f}$" + "\n"
        rf"$\Lambda_{{vol}}  = 4\pi^3 \approx {Lambda_vol:.3f}$  (3-torus phase volume)" + "\n"
        rf"$\Lambda_{{surf}} = \pi^2 \approx {Lambda_surf:.3f}$    (Clifford torus)" + "\n"
        rf"$\Lambda_{{line}} = \pi \approx {Lambda_line:.3f}$       (core magnetic moment)" + "\n"
        rf"$\alpha^{{-1}}_{{\mathrm{{ideal}}}} = \Lambda_{{vol}}+\Lambda_{{surf}}+\Lambda_{{line}}"
        rf" \approx {alpha_inv_computed:.4f}$"
    )
    ax.text2D(
        0.02,
        0.04,
        textstr,
        transform=ax.transAxes,
        color=style.COLORS["data"],
        fontsize=9,
        bbox=dict(
            facecolor="white", edgecolor=style.COLORS["ave"], alpha=0.85, pad=8
        ),
    )

    ax.view_init(elev=22, azim=38)

    if output_path is None:
        output_path = str(sim_output("trefoil_alpha_qfactor.png"))

    style.save(fig, output_path)
    plt.close()
    return output_path


def main() -> None:
    # Geometric sanity checks
    assert np.isclose(R_gt - r_gt, 0.5), "Self-avoidance R - r = 1/2 violated"
    assert np.isclose(R_gt * r_gt, 0.25), "Clifford-torus screening R·r = 1/4 violated"

    mp = golden_torus_multipole()
    alpha_inv_computed = mp["alpha_inv"]

    # Closure check against the engine constant
    assert np.isclose(
        alpha_inv_computed, ALPHA_COLD_INV, rtol=1e-12
    ), f"Multipole sum {alpha_inv_computed} disagrees with ALPHA_COLD_INV {ALPHA_COLD_INV}"

    print("=" * 72)
    print("  Golden Torus Multipole α Derivation")
    print("=" * 72)
    print(f"  Golden Ratio       φ = {PHI:.10f}")
    print(f"  Major radius       R = φ/2      = {R_gt:.10f}")
    print(f"  Minor radius       r = (φ-1)/2  = {r_gt:.10f}")
    print(f"  Self-avoidance     R - r = {R_gt - r_gt:.4f}   (expected 0.5)")
    print(f"  Holom. screening   R · r = {R_gt * r_gt:.4f}   (expected 0.25)")
    print()
    print(f"  Λ_vol  = 16π³(R·r)  = {mp['Lambda_vol']:.6f}   (= 4π³)")
    print(f"  Λ_surf = 4π²(R·r)   = {mp['Lambda_surf']:.6f}   (= π²)")
    print(f"  Λ_line = π·d        = {mp['Lambda_line']:.6f}   (= π)")
    print()
    print(f"  α⁻¹_ideal = Λ_vol + Λ_surf + Λ_line = {alpha_inv_computed:.10f}")
    print(f"  Closed form: 4π³ + π² + π          = {4*np.pi**3 + np.pi**2 + np.pi:.10f}")
    print(f"  Engine ALPHA_COLD_INV              = {ALPHA_COLD_INV:.10f}")
    print()
    print(f"  Observed α⁻¹ (CODATA)              = {1.0/ALPHA:.10f}")
    print(f"  δ_strain (CMB thermal correction)  = {DELTA_STRAIN:.6e}")
    print(
        f"  α⁻¹_ideal × (1 − δ_strain)         = "
        f"{alpha_inv_computed * (1.0 - DELTA_STRAIN):.10f}   (should match CODATA)"
    )
    print()
    print(
        f"  Cold prediction vs CODATA: Δ = {(alpha_inv_computed - 1.0/ALPHA):.6e} "
        f"({(alpha_inv_computed - 1.0/ALPHA)/(1.0/ALPHA)*100:.6f}%)"
    )
    print("=" * 72)

    output_path = render_figure()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
