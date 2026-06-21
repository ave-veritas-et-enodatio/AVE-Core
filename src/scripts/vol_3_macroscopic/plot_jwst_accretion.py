import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

# House style: white-background print profile + Okabe-Ito palette (single source
# of truth in ave.viz.style — no hand-set dark_background / facecolors / neon hex).
style.apply()


def plot_jwst_accretion() -> None:
    # Time vector in Million Years (Myr) from Big Bang
    t = np.linspace(0, 800, 500)

    # ---------------------------------------------------------
    # 1. Models
    # ---------------------------------------------------------
    # Seed mass (Arbitrary, say 10^6 solar masses for a primordial halo)
    M_seed = 1e6

    # AVE Exponential Model (Mutual Inductance)
    # τ_ind = 150 / ln(10) ≈ 65.1 Myr — derived in Vol 3 Ch 4 (generative cosmology),
    # see `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:112`.
    # (Citation corrected 2026-05-17 — previously said "Chapter 10" in error.)
    tau_ind = 65.1
    M_AVE = M_seed * np.exp(t / tau_ind)

    # Lambda-CDM Hierarchical Merging Model (Collisionless)
    # Slow power-law growth, M ~ t^(5/2)
    # Normalize so it starts at M_seed at t=10 (to avoid zero div/funny scaling)
    t_safe = np.clip(t, 10, None)
    k_lcdm = M_seed / (10**2.5)
    M_LCDM = k_lcdm * (t_safe**2.5)

    # ---------------------------------------------------------
    # 2. JWST Empirical Data Points
    # ---------------------------------------------------------
    # Empirical constraints:
    # ~10^10 M_sun by 350 Myr
    # ~10^11 M_sun by 500 Myr
    data_t = [350, 500]
    data_M = [1e10, 1e11]

    # ---------------------------------------------------------
    # 3. Plotting
    # ---------------------------------------------------------
    fig, ax = plt.subplots(figsize=style.figsize("single"))

    # Plot Models
    ax.plot(
        t,
        M_AVE,
        color=style.COLORS["ave"],
        linestyle="-",
        label=r"AVE Mutual Inductance ($M_{\mathrm{seed}}\, e^{t / 65.1}$)",
    )
    ax.plot(
        t,
        M_LCDM,
        color=style.COLORS["comparison"],
        linestyle="--",
        label=r"Standard $\Lambda$CDM ($M \propto t^{2.5}$)",
    )

    # Plot Data
    ax.scatter(
        data_t,
        data_M,
        color=style.COLORS["data"],
        s=110,
        zorder=5,
        marker="*",
        label=r"JWST empirical data ($z > 10$)",
    )

    # Formatting
    ax.set_yscale("log")
    ax.set_ylim(1e5, 1e12)
    ax.set_xlim(0, 800)

    ax.set_xlabel(style.axis_label("Time since Big Bang", "t", "Myr"))
    ax.set_ylabel(style.axis_label("Stellar mass", r"M", r"$M_\odot$"))

    # Annotate the JWST high-z observation window (guide band, behind data).
    ax.axvspan(300, 600, color=style.COLORS["muted"], alpha=0.12, zorder=0)
    ax.text(
        450,
        5e6,
        "JWST high-$z$\nobservation window",
        color=style.COLORS["muted"],
        fontsize=9,
        horizontalalignment="center",
        verticalalignment="center",
    )

    # Legend OUTSIDE the data (right of the axes).
    style.legend(ax, where="right")

    # Save (PDF + PNG via the house saver; title lives in the LaTeX \caption).
    paths = style.save(fig, sim_output("jwst_exponential_accretion.png"))
    print(f"Saved figure to: {', '.join(str(p) for p in paths)}")


if __name__ == "__main__":
    plot_jwst_accretion()
