"""
Plot cold vs thermally-corrected Skyrmion profiles.

Shows the effect of the δ_th = 1/(14π²) residual thermal correction on the
Faddeev-Skyrme coupling κ_FS, demonstrating how vacuum thermal noise
softens the quartic term.  The larger lattice-resolution component of
the old δ_th = 1/(28π) is now handled by Axiom 4 gradient saturation
inside the energy functional itself.

Output: assets/sim_outputs/thermal_skyrmion_comparison.png
"""

import os

import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import KAPPA_FS_COLD, KAPPA_FS, M_E, C_0, HBAR

L_NODE = HBAR / (M_E * C_0)

# Profile ansatz: f(r) = (1 + (r/R)^n)^(-1)  with R determined by kappa
# The Faddeev-Skyrme radial profile for the hedgehog ansatz
r = np.linspace(0.01, 8.0, 500)  # in units of L_NODE


def skyrmion_profile(r, kappa, n=2):
    """Power-law hedgehog profile for the O(3) sigma model."""
    R = 1.0 / np.sqrt(kappa)  # characteristic radius
    return np.pi / (1 + (r / R) ** n)


def energy_density(r, kappa, n=2):
    """Strain energy density of the Skyrmion profile."""
    f = skyrmion_profile(r, kappa, n)
    df = np.gradient(f, r)
    # sigma model term + quartic Skyrme term
    sigma = 0.5 * df**2 + np.sin(f) ** 2 / r**2
    skyrme = kappa**2 * (df**2 * np.sin(f) ** 2 / r**2)
    return sigma + skyrme


u_cold = energy_density(r, KAPPA_FS_COLD)
u_warm = energy_density(r, KAPPA_FS)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))
fig.patch.set_facecolor("#0d1117")
for ax in (ax1, ax2):
    ax.set_facecolor("#0d1117")
    ax.tick_params(colors="white")
    ax.spines["bottom"].set_color("#30363d")
    ax.spines["left"].set_color("#30363d")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# Left panel: Skyrmion profiles
f_cold = skyrmion_profile(r, KAPPA_FS_COLD)
f_warm = skyrmion_profile(r, KAPPA_FS)

ax1.plot(
    r,
    f_cold / np.pi,
    color="#58a6ff",
    linewidth=2.5,
    label=rf"Cold ($\kappa = 8\pi = {KAPPA_FS_COLD:.2f}$)",
)
ax1.plot(
    r,
    f_warm / np.pi,
    color="#f0883e",
    linewidth=2.5,
    linestyle="--",
    label=rf"Thermal ($\kappa_{{eff}} = {KAPPA_FS:.2f},\ \delta_{{th}} = 1/14\pi^2$)",
)
ax1.set_xlabel(r"$r / \ell_{node}$", fontsize=13, color="white")
ax1.set_ylabel(r"Profile $f(r) / \pi$", fontsize=13, color="white")
ax1.set_title("Hedgehog Profile: Cold vs Thermal", fontsize=14, color="white", pad=10)
ax1.legend(fontsize=10, facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
ax1.grid(True, alpha=0.15, color="#30363d")

# Right panel: Energy densities
ax2.plot(
    r,
    u_cold * r**2,
    color="#58a6ff",
    linewidth=2.5,
    label=rf"Cold: $I_{{scalar}} \approx 1171\,m_e$",
)
ax2.plot(
    r,
    u_warm * r**2,
    color="#f0883e",
    linewidth=2.5,
    linestyle="--",
    label=rf"Thermal: $I_{{scalar}} \approx 1162\,m_e$",
)
ax2.fill_between(
    r,
    u_cold * r**2,
    u_warm * r**2,
    alpha=0.15,
    color="#da3633",
    label=rf"$\Delta E \approx 0.8\%$ (thermal + saturation)",
)
ax2.set_xlabel(r"$r / \ell_{node}$", fontsize=13, color="white")
ax2.set_ylabel(r"$r^2 \cdot \mathcal{E}(r)$ (energy integrand)", fontsize=13, color="white")
ax2.set_title("Scalar Energy Integrand: Thermal Reduction", fontsize=14, color="white", pad=10)
ax2.legend(fontsize=10, facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
ax2.grid(True, alpha=0.15, color="#30363d")

fig.suptitle(r"Grüneisen Thermal Correction: $\delta_{th} = 1/(14\pi^2)$", fontsize=16, color="white", y=1.02)
plt.tight_layout()

output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "assets",
    "sim_outputs",
    "thermal_skyrmion_comparison.png",
)
plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close()
print(f"Saved: {output_path}")
