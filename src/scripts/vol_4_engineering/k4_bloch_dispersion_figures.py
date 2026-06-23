#!/usr/bin/env python3
"""
FIGURES for the K4 Bloch dispersion eigensolve — the (q·ℓ_node)⁴ photon chord.

FIGURES lane (companion to k4_bloch_dispersion.py, the BUILD-lane eigensolve).
This script is a PURE PRESENTATION driver: it READS the validated data the BUILD
lane committed at ``_output/k4_bloch_dispersion.json`` and renders it through the
AVE house style (``ave.viz.style``). It does NOT re-run the physics eigensolve.

WHERE THE NUMBERS COME FROM (ave-figure-discipline + verify-before-cite):
  * ω(k) band arrays (Fig 1), the cutoff/zone-edge marks (Fig 1), the quartic /
    quadratic anisotropy verdict series and Ξ table (Figs 2,3), and the
    random-control series (Fig 2) are read VERBATIM from the committed JSON.
  * For the angular sweeps the JSON does not tabulate (the polar pattern at
    arbitrary direction, Fig 2; the full BZ-plane surface, Fig 4; the swept
    animation, Fig 5), this driver evaluates the SAME validated closed-form
    DIRECTION FACTORS the eigensolve already verified and recorded — the cubic
    invariant Ξ(q̂) (whose ⟨100⟩/⟨111⟩ values + sign-change are in the JSON) and
    the photon dispersion ω²/(c²k²)=1+κ_γ·Ξ·(kℓ)⁴ — imported by symbol from the
    BUILD-lane module. No new physics constant or model is introduced here; the
    log-log slope=4 (photon) / slope=2 (random) verdicts in the JSON are the
    validation those closed forms ride on.

Constants are cited by SYMBOL (C_0, L_NODE, OMEGA_C) from ave.core.constants —
never the literal 1.24e20 / 7.76e20.

Run:  python3 src/scripts/vol_4_engineering/k4_bloch_dispersion_figures.py
Output: manuscript/vol_4_engineering/figures/k4_bloch_*.{pdf,png} + one .gif
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import C_0, L_NODE, OMEGA_C
from ave.viz import style
from ave_path_util import manuscript_path

# Validated direction-factor closed forms (NOT a re-derivation — the same forms
# the BUILD-lane eigensolve verified: Ξ sign-change + slope-4 photon / slope-2
# random anisotropy are recorded in the JSON this driver reads).
from scripts.vol_4_engineering.k4_bloch_dispersion import (
    D_BONDS,
    KAPPA_GAMMA,
    cubic_invariant,
    photon_omega_sq_over_c2k2,
    random_bonds,
)

DATA_PATH = (
    Path(__file__).resolve().parent / "_output" / "k4_bloch_dispersion.json"
)
FIG_DIR_PARTS = ("vol_4_engineering", "figures")

# House labels for the high-symmetry directions (Miller-index strings as stored).
DIR_LABELS = ["[100]", "[110]", "[111]", "[210]"]


def load_data() -> dict:
    """Read the BUILD-lane validated eigensolve output (verify-before-cite)."""
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"validated data not found at {DATA_PATH} — run the BUILD-lane "
            f"k4_bloch_dispersion.py first."
        )
    return json.loads(DATA_PATH.read_text())


# ---------------------------------------------------------------------------
# Figure 1 — ω(k) dispersion along high-symmetry directions + light-line
# ---------------------------------------------------------------------------
def fig1_dispersion(data: dict) -> Path:
    """ω(k) along ⟨100⟩→⟨110⟩→⟨111⟩→⟨210⟩ with the continuum light-line
    ω=c|k|, the temporal cutoff k=1/ℓ_node, and the zone-edge k=π/ℓ_node.

    A four-panel row (one per high-symmetry direction). Each panel shows the six
    mechanical K4 bands (gray, lattice carriers) and the continuum photon branch
    (AVE blue), overlaid with the light-line (vermillion dashed). The x-axis is
    the bond phase kℓ_node ∈ (0, π]; cutoff (kℓ=1) and zone-edge (kℓ=π) marked.
    All arrays read verbatim from the validated JSON.
    """
    bands = data["bands"]
    fig, axes = plt.subplots(1, 4, figsize=style.figsize("wide"), sharey=True)

    for ax, name in zip(axes, DIR_LABELS):
        b = bands[name]
        kl = np.asarray(b["kl"])  # bond phase kℓ_node, 0→π
        w_mech = np.asarray(b["omega_mechanical_bands_rad_s"])  # (n,6)
        w_phot = np.asarray(b["omega_photon_rad_s"])  # (n,)
        # light-line ω = c|k| = C_0 · (kℓ / ℓ_node)  [rad/s]
        light = C_0 * (kl / L_NODE)

        for j in range(w_mech.shape[1]):
            ax.plot(
                kl, w_mech[:, j],
                color=style.COLORS["muted"], lw=1.0,
                label="K4 mechanical bands" if j == 0 else "_nolegend_",
            )
        ax.plot(kl, w_phot, color=style.COLORS["ave"], lw=2.2, label="photon")
        ax.plot(
            kl, light,
            color=style.COLORS["comparison"], lw=1.4, ls="--",
            label=r"light-line $\omega=c|k|$",
        )
        # cutoff (kℓ=1) and zone-edge (kℓ=π) verticals
        ax.axvline(1.0, color=style.COLORS["accent"], ls=":", lw=1.2,
                   label=r"cutoff $k=1/\ell_{\rm node}$")
        ax.axvline(np.pi, color=style.COLORS["data"], ls="-.", lw=1.0,
                   label=r"zone-edge $k=\pi/\ell_{\rm node}$")
        ax.set_xlim(0, np.pi)
        ax.set_xticks([0, np.pi / 2, np.pi])
        ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"])
        # annotate ω_C horizontal on the first panel only (avoid graphics clutter)
        if name == "[100]":
            ax.axhline(OMEGA_C, color=style.COLORS["accent"], ls=":", lw=0.8,
                       alpha=0.6)
        ax.text(0.5, 0.93, name, transform=ax.transAxes,
                ha="center", va="top",
                fontsize="medium", fontweight="bold")

    axes[0].set_ylabel(style.axis_label("Angular frequency", r"\omega", "rad/s"))
    # ONE shared x-label on the figure (the quantity is identical across all four
    # panels — repeating it per-panel collides; ave-figure-discipline Axis 4).
    fig.supxlabel(style.axis_label("Bond phase", r"k\,\ell_{\rm node}", ""))
    # single shared legend below the whole row, centred on the FIGURE (a manual
    # per-axes bbox anchor fights constrained_layout and collapses the panels).
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center",
               bbox_to_anchor=(0.5, 0.0), ncol=5, frameon=False)

    out = manuscript_path(*FIG_DIR_PARTS, "k4_bloch_dispersion_bands.png")
    return style.save(fig, out)[1]  # return the .png path (pdf also written)


# ---------------------------------------------------------------------------
# Figure 2 — polar anisotropy [ω/(c|k|) − 1] vs direction, K4 vs random control
# ---------------------------------------------------------------------------
def fig2_anisotropy_polar(data: dict) -> Path:
    """Polar plot of the fractional phase-speed anisotropy
    [ω(k)/(c|k|) − 1] vs in-plane propagation direction, in the (001) plane,
    at a few fixed |k|ℓ_node — showing the QUARTIC (four-fold cubic) K4 pattern
    GROW, contrasted with the random-lattice control (lower-order, two-fold).

    Left polar axis: K4 photon (cubic invariant Ξ(q̂)). Right polar axis: the
    random-bond control. Both use the validated closed forms whose log-log
    slopes (4 vs 2) are recorded in the JSON. The displayed Ξ([100]) / Ξ([111])
    contrast matches the JSON ``cubic_invariant_Xi`` table.
    """
    # sanity: anchor to the recorded verdicts so the figure can't drift off-data
    assert data["quartic_chord"]["photon_verdict"] == "QUARTIC"
    assert data["random_control"]["verdict"] == "QUADRATIC"

    theta = np.linspace(0.0, 2.0 * np.pi, 361)
    # in-plane unit directions in the (001) plane: q̂ = (cosθ, sinθ, 0)
    qhat = np.column_stack([np.cos(theta), np.sin(theta), np.zeros_like(theta)])
    kls = [1.0, 1.6, 2.2, np.pi]  # Γ-side → zone-edge, bond-phase units
    rb = random_bonds(seed=0)  # the SAME control bond set as the eigensolve
    sm_avg = float(
        np.mean([np.sum((rb @ u) ** 2) for u in _unit_sphere_dirs()])
    )

    fig, (axk, axr) = plt.subplots(
        1, 2, figsize=style.figsize("wide"),
        subplot_kw={"projection": "polar"},
    )
    cycle = [style.COLORS["ave"], style.COLORS["accent"],
             "#CC79A7", style.COLORS["comparison"]]
    for kl, col in zip(kls, cycle):
        # K4 photon: ω/(c|k|) − 1 = sqrt(1 + κ_γ Ξ (kℓ)⁴) − 1
        aniso_k4 = np.array(
            [np.sqrt(photon_omega_sq_over_c2k2(q * kl)) - 1.0 for q in qhat]
        )
        axk.plot(theta, aniso_k4, color=col, lw=1.8,
                 label=rf"$k\ell={kl:.2f}$")
        # random control: ω/(c|k|) − 1, anisotropy ∝ (kℓ)² (quadratic)
        aniso_r = []
        for q in qhat:
            sm = float(np.sum((rb @ q) ** 2))
            f = 1.0 + KAPPA_GAMMA * (sm - sm_avg) * kl**2
            aniso_r.append(np.sqrt(max(f, 0.0)) - 1.0)
        axr.plot(theta, np.array(aniso_r), color=col, lw=1.8,
                 label=rf"$k\ell={kl:.2f}$")

    for ax, tag in ((axk, "K4 photon (quartic): "
                          r"$\omega/(c|k|)-1$ vs direction"),
                    (axr, "random control (quadratic): "
                          r"$\omega/(c|k|)-1$ vs direction")):
        ax.set_theta_zero_location("E")
        ax.grid(True, alpha=0.3)
        # radial-tick labels into an EMPTY angular sector (between the ⟨100⟩ and
        # ⟨110⟩ lobes) so they never sit on the data (ave-figure-discipline
        # Axis 4: no text over graphics).
        ax.set_rlabel_position(22.5)
        ax.tick_params(axis="y", labelsize="x-small")
        # tag (quantity + which carrier) goes in the legend title; the caption
        # stays in the LaTeX \caption{}, not the raster.
        style.legend(ax, where="below", ncol=4, title=tag)

    # widen the inter-panel gap via the constrained-layout engine (the house
    # default; plain subplots_adjust is incompatible with it).
    fig.get_layout_engine().set(wspace=0.12)
    out = manuscript_path(*FIG_DIR_PARTS, "k4_bloch_anisotropy_polar.png")
    return style.save(fig, out)[1]


def _unit_sphere_dirs(n: int = 200) -> np.ndarray:
    """Deterministic Fibonacci-sphere directions for the spherical average of
    the random-control 2nd moment (matches the eigensolve's _SPHERE_DIRS)."""
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n)
    gold = np.pi * (1 + 5**0.5)
    th = gold * i
    return np.column_stack(
        [np.sin(phi) * np.cos(th), np.sin(phi) * np.sin(th), np.cos(phi)]
    )


# ---------------------------------------------------------------------------
# Figure 3 — k² + k⁴ fit with residuals (validate-on-known: continuum at k→0)
# ---------------------------------------------------------------------------
def fig3_k2_k4_fit(data: dict) -> Path:
    """The k² + k⁴ fit with residuals (validate-on-known: the continuum
    ω=c|k| is recovered as kℓ→0).

    Top panel: the dimensionless dispersion ω²/(c²k²) − 1 along ⟨100⟩ for the
    PHOTON (pure k⁴, no zone-edge k² term — the chord) and for the MATTER
    carrier (k² zone-edge term present — the contrast), with the least-squares
    a₂(kℓ)²+a₄(kℓ)⁴ fit overlaid. Bottom panel: the fit residuals (≈machine
    precision = the form is exactly k²+k⁴). The recovered photon a₂≈0 and
    a₄=κ_γ·Ξ([100]) are annotated against the JSON-recorded values.
    """
    xi_100 = data["quartic_chord"]["cubic_invariant_Xi"]["[100]"]  # +0.4
    kappa_gamma = data["quartic_chord"]["photon_kappa_gamma"]

    kl = np.linspace(1e-3, np.pi, 200)
    q100 = np.array([1.0, 0.0, 0.0])
    # PHOTON dimensionless dispersion minus 1 (validated closed form)
    y_phot = np.array([photon_omega_sq_over_c2k2(q100 * x) - 1.0 for x in kl])
    # MATTER carrier (the zone-edge contrast), read its fitted a₂ from JSON
    a2_matter = data["isotropic_k2_coefficient"]["a2_per_direction_matter"]["[100]"]

    # least-squares a₂(kℓ)² + a₄(kℓ)⁴ fit to the PHOTON series
    X = np.vstack([kl**2, kl**4]).T
    coef, *_ = np.linalg.lstsq(X, y_phot, rcond=None)
    a2_fit, a4_fit = float(coef[0]), float(coef[1])
    y_fit = X @ coef
    resid = y_phot - y_fit
    a4_expected = kappa_gamma * xi_100  # = 1/24 · 0.4

    fig, (ax, axr) = plt.subplots(
        2, 1, figsize=style.figsize("single"), sharex=True,
        gridspec_kw={"height_ratios": [3, 1]},
    )
    ax.plot(kl, y_phot, color=style.COLORS["ave"], lw=2.2,
            label=r"photon $\omega^2/(c^2k^2)-1$")
    ax.plot(kl, y_fit, color=style.COLORS["data"], lw=1.0, ls="--",
            label=rf"fit $a_2(k\ell)^2+a_4(k\ell)^4$")
    # matter zone-edge contrast curve (a2·kℓ² leading), for reference
    y_matter = a2_matter * kl**2
    ax.plot(kl, y_matter, color=style.COLORS["comparison"], lw=1.4, ls=":",
            label=r"matter zone-edge $a_2(k\ell)^2$")
    ax.axhline(0.0, color=style.COLORS["muted"], lw=0.8)
    ax.set_ylabel(style.axis_label("Dispersion", r"\omega^2/(c^2k^2)-1", ""))
    # validate-on-known annotation (text in a clear region, not over the curve)
    ax.annotate(
        rf"photon $a_2={a2_fit:+.1e}\approx0$ (no zone-edge)"
        "\n"
        rf"$a_4={a4_fit:+.5f}$ vs $\kappa_\gamma\Xi_{{[100]}}={a4_expected:+.5f}$"
        "\n"
        r"continuum $\omega=c|k|$ recovered as $k\to0$",
        xy=(0.03, 0.97), xycoords="axes fraction",
        ha="left", va="top", fontsize="small",
        bbox=dict(boxstyle="round", fc="white", ec=style.COLORS["muted"],
                  alpha=0.85),
    )
    style.legend(ax, where="right")

    axr.plot(kl, resid, color=style.COLORS["accent"], lw=1.2)
    axr.axhline(0.0, color=style.COLORS["muted"], lw=0.8)
    axr.set_ylabel(style.axis_label("Residual", r"\Delta", ""))
    axr.set_xlabel(style.axis_label("Bond phase", r"k\,\ell_{\rm node}", ""))
    axr.set_xlim(0, np.pi)

    out = manuscript_path(*FIG_DIR_PARTS, "k4_bloch_k2_k4_fit.png")
    return style.save(fig, out)[1]


# ---------------------------------------------------------------------------
# Figure 4 — dispersion-anisotropy surface over a BZ plane (heatmap + 3D)
# ---------------------------------------------------------------------------
def fig4_bz_surface(data: dict) -> Path:
    """The photon dispersion anisotropy over a BZ plane — 2D heatmap (left) and
    3D surface (right) of [ω/(c|k|) − 1] across the (001) k-plane.

    The four-fold cubic (Fd-3m) pattern is visible: the anisotropy is POSITIVE
    along ⟨100⟩ (Ξ=+0.4) and NEGATIVE along ⟨110⟩ (Ξ=−0.1), the sign-change
    that makes it a true cubic harmonic rather than an isotropic correction.
    A diverging colormap (signed quantity, meaningful zero) is used.
    """
    n = 241
    lim = np.pi  # bond-phase units, out to the zone edge
    kx = np.linspace(-lim, lim, n)
    ky = np.linspace(-lim, lim, n)
    KX, KY = np.meshgrid(kx, ky)
    aniso = np.full_like(KX, np.nan)
    # Restrict to the INSCRIBED zone disk |k|ℓ ≤ π: outside it the leading-order
    # cubic-harmonic dispersion (a small-k expansion) is not the physical
    # quantity — masking avoids plotting an unphysical corner blow-up (and the
    # √(negative) the formula produces there).
    for i in range(n):
        for j in range(n):
            kl = float(np.hypot(KX[i, j], KY[i, j]))
            if kl == 0.0:
                aniso[i, j] = 0.0
            elif kl <= lim:
                kv = np.array([KX[i, j], KY[i, j], 0.0])
                f = photon_omega_sq_over_c2k2(kv)
                aniso[i, j] = np.sqrt(f) - 1.0 if f > 0.0 else np.nan

    vmax = float(np.nanmax(np.abs(aniso)))
    fig = plt.figure(figsize=style.figsize("wide"))
    ax0 = fig.add_subplot(1, 2, 1)
    pcm = ax0.pcolormesh(
        KX, KY, aniso, cmap=style.CMAP_DIV, vmin=-vmax, vmax=vmax,
        shading="auto",
    )
    ax0.set_aspect("equal")
    ax0.set_xlabel(style.axis_label("Wavevector", r"k_x\,\ell_{\rm node}", ""))
    ax0.set_ylabel(style.axis_label("Wavevector", r"k_y\,\ell_{\rm node}", ""))
    cb = fig.colorbar(pcm, ax=ax0, fraction=0.046, pad=0.04)
    cb.set_label(style.axis_label("Anisotropy", r"\omega/(c|k|)-1", ""))
    # mark the high-symmetry rays (⟨100⟩ = +, ⟨110⟩ = −)
    for ang, lab in ((0, r"$\langle100\rangle\,(+)$"),
                     (45, r"$\langle110\rangle\,(-)$")):
        a = np.deg2rad(ang)
        ax0.plot([0, lim * np.cos(a)], [0, lim * np.sin(a)],
                 color=style.COLORS["muted"], lw=0.8, ls="--")

    ax1 = fig.add_subplot(1, 2, 2, projection="3d")
    surf = ax1.plot_surface(
        KX, KY, aniso, cmap=style.CMAP_DIV, vmin=-vmax, vmax=vmax,
        linewidth=0, antialiased=True, rcount=80, ccount=80,
    )
    ax1.set_xlabel(style.axis_label("", r"k_x\,\ell_{\rm node}", ""))
    ax1.set_ylabel(style.axis_label("", r"k_y\,\ell_{\rm node}", ""))
    ax1.set_zlabel(style.axis_label("Anisotropy", r"\omega/(c|k|)-1", ""))
    ax1.view_init(elev=28, azim=-58)

    out = manuscript_path(*FIG_DIR_PARTS, "k4_bloch_bz_surface.png")
    return style.save(fig, out)[1]


# ---------------------------------------------------------------------------
# Figure 5 — ANIMATION: polar anisotropy pattern as |k| sweeps Γ → zone-edge
# ---------------------------------------------------------------------------
def fig5_animation(data: dict) -> Path:
    """ANIMATION: the polar anisotropy pattern evolving as |k| sweeps
    Γ → zone-edge (kℓ: 0→π).

    Two polar axes side by side — the K4 photon (quartic four-fold pattern that
    GROWS with |k|⁴) and the random-bond control (quadratic, two-fold). As kℓ
    increases the K4 four-lobed cubic harmonic sharpens; the control stays a
    fixed low-order shape (anisotropy only growing as |k|²). Robust output:
    pillow .gif (no ffmpeg dependency). If the animation writer is unavailable,
    falls back to a committed multi-frame panel (.png), and the return value
    reflects whichever was produced.
    """
    from matplotlib.animation import FuncAnimation, PillowWriter

    theta = np.linspace(0.0, 2.0 * np.pi, 361)
    qhat = np.column_stack([np.cos(theta), np.sin(theta), np.zeros_like(theta)])
    rb = random_bonds(seed=0)
    sm_avg = float(np.mean([np.sum((rb @ u) ** 2) for u in _unit_sphere_dirs()]))
    kls = np.linspace(0.1, np.pi, 48)  # Γ → zone-edge

    def aniso_k4(kl):
        return np.array(
            [np.sqrt(photon_omega_sq_over_c2k2(q * kl)) - 1.0 for q in qhat]
        )

    def aniso_rand(kl):
        out = []
        for q in qhat:
            sm = float(np.sum((rb @ q) ** 2))
            f = 1.0 + KAPPA_GAMMA * (sm - sm_avg) * kl**2
            out.append(np.sqrt(max(f, 0.0)) - 1.0)
        return np.array(out)

    # peak anisotropy at the zone-edge sets a fixed radial scale (so the GROWTH
    # is visible against a stable frame, not autoscaled away)
    rmax = max(float(np.max(np.abs(aniso_k4(np.pi)))),
               float(np.max(np.abs(aniso_rand(np.pi))))) * 1.05

    fig, (axk, axr) = plt.subplots(
        1, 2, figsize=style.figsize("wide"),
        subplot_kw={"projection": "polar"},
    )
    (line_k,) = axk.plot([], [], color=style.COLORS["ave"], lw=2.2)
    (line_r,) = axr.plot([], [], color=style.COLORS["comparison"], lw=2.2)
    for ax, tag, col in (
        (axk, r"K4 photon (quartic): $\omega/(c|k|)-1$", style.COLORS["ave"]),
        (axr, r"random control (quadratic): $\omega/(c|k|)-1$",
         style.COLORS["comparison"]),
    ):
        ax.set_theta_zero_location("E")
        ax.set_rmax(rmax)
        ax.grid(True, alpha=0.3)
        # radial-tick labels into an empty angular sector (no text over data)
        ax.set_rlabel_position(22.5)
        ax.tick_params(axis="y", labelsize="x-small")
        # legend (not a baked title) carries the per-panel label
        ax.plot([], [], color=col, label=tag)
        style.legend(ax, where="below", ncol=1)
    # swept-variable readout sits ABOVE the panels (clear of the polar rims and
    # the legends) — it is live state, not a baked caption.
    sweep_txt = fig.text(0.5, 0.98, "", ha="center", va="top",
                         fontsize="medium")
    fig.get_layout_engine().set(wspace=0.12)

    def update(idx):
        kl = kls[idx]
        line_k.set_data(theta, aniso_k4(kl))
        line_r.set_data(theta, aniso_rand(kl))
        # caption-free progress readout lives in a figure-text annotation, which
        # is informational state (the swept variable), not a baked title
        sweep_txt.set_text(rf"$k\,\ell_{{\rm node}} = {kl:.2f}$ "
                           r"(sweeping $\Gamma\rightarrow$ zone-edge)")
        return line_k, line_r, sweep_txt

    out_gif = manuscript_path(*FIG_DIR_PARTS, "k4_bloch_anisotropy_sweep.gif")
    try:
        anim = FuncAnimation(fig, update, frames=len(kls), blit=False)
        anim.save(str(out_gif), writer=PillowWriter(fps=12))
        plt.close(fig)
        return out_gif
    except Exception as exc:  # noqa: BLE001 — robust fallback path
        plt.close(fig)
        print(f"  [anim] pillow .gif unavailable ({exc}); writing panel fallback")
        return _fig5_panel_fallback(aniso_k4, aniso_rand, theta, kls, rmax)


def _fig5_panel_fallback(aniso_k4, aniso_rand, theta, kls, rmax) -> Path:
    """Multi-frame static panel fallback (no animation libs needed)."""
    picks = kls[:: max(1, len(kls) // 4)][:4]
    fig, axes = plt.subplots(
        2, len(picks), figsize=style.figsize("wide"),
        subplot_kw={"projection": "polar"},
    )
    for col, kl in enumerate(picks):
        for row, (fn, c) in enumerate(
            ((aniso_k4, style.COLORS["ave"]),
             (aniso_rand, style.COLORS["comparison"]))
        ):
            ax = axes[row, col]
            ax.plot(theta, fn(kl), color=c, lw=1.8)
            ax.set_theta_zero_location("E")
            ax.set_rmax(rmax)
            ax.grid(True, alpha=0.3)
            ax.set_xticklabels([])
            if row == 1:
                ax.set_xlabel(rf"$k\ell={kl:.2f}$")
    out = manuscript_path(*FIG_DIR_PARTS, "k4_bloch_anisotropy_sweep_panel.png")
    return style.save(fig, out)[1]


def main() -> None:
    style.apply()  # white-background print profile (house default)
    data = load_data()
    written = []
    written.append(fig1_dispersion(data))
    written.append(fig2_anisotropy_polar(data))
    written.append(fig3_k2_k4_fit(data))
    written.append(fig4_bz_surface(data))
    written.append(fig5_animation(data))
    print("\nFIGURES written:")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
