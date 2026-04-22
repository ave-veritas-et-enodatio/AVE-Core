"""
Plot the Axiom 4 saturation observables: ε_eff(A) and C_eff(A).

Under the universal saturation kernel S(A) = sqrt(1 - (A/A_yield)^2):
  - Constitutive permittivity: ε_eff = ε_0 · S(A)  → 0  (collapse)
  - Measurable capacitance:    C_eff = C_0 / S(A)  → ∞  (divergence)

These are physically distinct:
  ε  is the material compliance (drops as the lattice stiffens).
  C  is the stored charge per volt (rises as the medium shorts).

Output: assets/sim_outputs/vacuum_dielectric_saturation.png
"""

import os

import matplotlib.pyplot as plt
import numpy as np

# Normalised field variable: A / A_yield  (0 to 0.999)
x = np.linspace(0, 0.999, 2000)

# Universal saturation kernel  S(A)
S = np.sqrt(1 - x**2)

# Constitutive permittivity (collapses):  ε_eff / ε_0 = S
eps_eff = S

# Measurable capacitance (diverges):  C_eff / C_0 = 1/S
C_eff = 1.0 / S

# Taylor expansion to E^4 order for ε: ε ≈ ε_0 [1 - (1/2)(A/A_yield)^2]
eps_taylor = 1.0 - 0.5 * x**2

# Linear regime: ε = ε_0
eps_linear = np.ones_like(x)

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(10, 10), sharex=True, gridspec_kw={"height_ratios": [1, 1], "hspace": 0.12}
)
for ax in (ax1, ax2):
    ax.set_facecolor("#0d1117")
fig.patch.set_facecolor("#0d1117")

# --- Top panel: ε_eff (collapse) ---
ax1.plot(
    x,
    eps_eff,
    color="#58a6ff",
    linewidth=2.5,
    label=r"AVE exact: $\varepsilon_{eff} = \varepsilon_0 \cdot S(A)$",
)
ax1.plot(
    x,
    eps_taylor,
    color="#f0883e",
    linewidth=2.0,
    linestyle="--",
    label=r"Euler-Heisenberg ($E^4$ Taylor): $\varepsilon_0[1 - \frac{1}{2}(A/A_y)^2]$",
)
ax1.plot(
    x,
    eps_linear,
    color="#8b949e",
    linewidth=1.5,
    linestyle=":",
    label=r"Linear: $\varepsilon = \varepsilon_0$",
)

# Shade the three regimes
ax1.axvspan(0, 0.3, alpha=0.08, color="#238636", label="Regime I: Linear")
ax1.axvspan(0.3, 0.8, alpha=0.08, color="#f0883e", label="Regime II: Euler-Heisenberg")
ax1.axvspan(0.8, 1.0, alpha=0.12, color="#da3633", label="Regime III: Saturation")

ax1.axvline(x=1.0, color="#da3633", linewidth=1.5, linestyle="-", alpha=0.5)
ax1.annotate(
    r"$A \to A_{yield}$: $\varepsilon \to 0$",
    xy=(0.96, 0.08),
    fontsize=10,
    color="#58a6ff",
    ha="right",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a2e", edgecolor="#58a6ff"),
)

ax1.set_ylabel(r"Constitutive Permittivity $\varepsilon_{eff} / \varepsilon_0$", fontsize=13, color="white")
ax1.set_title(
    r"Axiom 4: Saturation Observables — $\varepsilon$ Collapse vs $C$ Divergence",
    fontsize=15,
    color="white",
    pad=15,
)
ax1.set_ylim(-0.05, 1.15)
ax1.legend(fontsize=8.5, loc="lower left", facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
ax1.tick_params(colors="white")
ax1.spines["bottom"].set_color("#30363d")
ax1.spines["left"].set_color("#30363d")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.grid(True, alpha=0.15, color="#30363d")

# --- Bottom panel: C_eff (divergence) ---
ax2.plot(x, C_eff, color="#f778ba", linewidth=2.5, label=r"AVE exact: $C_{eff} = C_0 / S(A)$")
ax2.plot(x, eps_linear, color="#8b949e", linewidth=1.5, linestyle=":", label=r"Linear: $C = C_0$")

ax2.axvspan(0, 0.3, alpha=0.08, color="#238636")
ax2.axvspan(0.3, 0.8, alpha=0.08, color="#f0883e")
ax2.axvspan(0.8, 1.0, alpha=0.12, color="#da3633")

ax2.axvline(x=1.0, color="#da3633", linewidth=1.5, linestyle="-", alpha=0.5)
ax2.annotate(
    r"$A \to A_{yield}$: $C \to \infty$",
    xy=(0.96, 6.5),
    fontsize=10,
    color="#f778ba",
    ha="right",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1a2e", edgecolor="#f778ba"),
)

ax2.set_xlabel(r"Normalised Field Strain $A / A_{yield}$", fontsize=13, color="white")
ax2.set_ylabel(r"Measurable Capacitance $C_{eff} / C_0$", fontsize=13, color="white")
ax2.set_ylim(0.8, 8)
ax2.set_xlim(-0.02, 1.02)
ax2.legend(fontsize=9, loc="upper left", facecolor="#161b22", edgecolor="#30363d", labelcolor="white")
ax2.tick_params(colors="white")
ax2.spines["bottom"].set_color("#30363d")
ax2.spines["left"].set_color("#30363d")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(True, alpha=0.15, color="#30363d")

plt.tight_layout()
output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "assets",
    "sim_outputs",
    "vacuum_dielectric_saturation.png",
)
plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor())
plt.close()
print(f"Saved: {output_path}")
