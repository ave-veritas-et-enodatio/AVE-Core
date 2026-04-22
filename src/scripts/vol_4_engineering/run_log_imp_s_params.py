import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import Z_0


# --- Standard AVE output directory ---
def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "pyproject.toml")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(__file__))


OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# --- End standard output directory ---


def simulate_log_scale_s_parameters():
    r = np.logspace(0, 5, 1000)
    n_r = 1.0 + 1.0 / r
    Z_base = Z_0  # Derived from √(μ₀/ε₀)

    # AVE EFT MODEL
    L_eft, C_eft = 1.0 * n_r, 1.0 * n_r
    Z_eft = np.sqrt(L_eft / C_eft) * Z_base

    # UNMATCHED MODEL
    L_flawed, C_flawed = np.ones_like(r), 1.0 * n_r
    Z_flawed = np.sqrt(L_flawed / C_flawed) * Z_base

    Gamma_eft = np.zeros_like(r) + 1e-15
    Gamma_flawed = np.abs((Z_flawed - Z_base) / (Z_flawed + Z_base))

    S11_eft = 20 * np.log10(Gamma_eft)
    S11_flawed = 20 * np.log10(Gamma_flawed + 1e-15)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9), dpi=150)
    fig.patch.set_facecolor("#0a0a12")
    ax1.set_facecolor("#0a0a12")
    ax2.set_facecolor("#0a0a12")

    ax1.set_xlim(1e5, 1e0)
    ax2.set_xlim(1e5, 1e0)

    ax1.plot(r, n_r, color="#FFD54F", lw=3, label=r"Refractive Index ($n \propto \rho_{bulk}$)")
    ax1.plot(
        r,
        Z_eft / Z_base,
        color="#4FC3F7",
        lw=4,
        linestyle="--",
        label=r"EFT Impedance ($Z_0$ Perfectly Matched)",
    )
    ax1.plot(
        r,
        Z_flawed / Z_base,
        color="#E57373",
        lw=2,
        linestyle="-.",
        label=r"Unmatched Dielectric Model ($Z_0$ Drops)",
    )

    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_title(
        "Macroscopic Gravitational Component Divergence (Log-Log Scale)",
        color="white",
        fontsize=14,
        weight="bold",
    )
    ax1.set_ylabel(r"Component Scaling Factor", color="white", weight="bold")
    ax1.legend(loc="upper right", facecolor="#111111", edgecolor="gray", labelcolor="white")

    ax2.plot(
        r,
        S11_flawed,
        color="#E57373",
        lw=3,
        label=r"Standard Optical Dielectric Reflection ($S_{11} \gg -10$ dB)",
    )
    ax2.plot(r, S11_eft, color="#4FC3F7", lw=4, label=r"AVE Condensate Match ($S_{11} \to -\infty$ dB)")

    ax2.set_xscale("log")
    ax2.set_ylim(-160, 0)
    ax2.set_title("Condensate Return Loss Profile ($S_{11}$)", color="white", fontsize=14, weight="bold")
    ax2.set_xlabel("Radial Distance from Mass Center ($r/R_s$)", color="white", weight="bold")
    ax2.set_ylabel("Reflected Power $S_{11}$ (dB)", color="white", weight="bold")
    ax2.legend(loc="center right", facecolor="#111111", edgecolor="gray", labelcolor="white")

    textstr = (
        r"$\mathbf{The~S{-}Parameters~of~Analog~Gravity:}$"
        + "\n"
        + r"If the metric acted like a standard unmatched dielectric, the"
        + "\n"
        + r"impedance mismatch would cause the gravity well to reflect light."
        + "\n"
        + r"Because macroscopic gravity acts as volumetric compression, it scales $\mu$ and $\epsilon$ symmetrically."
        + "\n"
        + r"This keeps $Z_0$ invariant, pushing Return Loss to absolute zero."
    )
    ax2.text(
        1e4,
        -130,
        textstr,
        color="white",
        fontsize=11,
        bbox=dict(facecolor="#111111", edgecolor="gray", alpha=0.9, pad=10),
    )

    for ax in [ax1, ax2]:
        ax.grid(True, which="both", ls=":", color="#333333")
        ax.tick_params(colors="lightgray")
        for spine in ax.spines.values():
            spine.set_color("#333333")

    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_DIR, "log_impedance_s_parameters.png"),
        facecolor=fig.get_facecolor(),
        bbox_inches="tight",
    )
    plt.close()


if __name__ == "__main__":
    simulate_log_scale_s_parameters()
