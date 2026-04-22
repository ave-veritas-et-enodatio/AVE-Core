import pathlib

"""
Modeling Acoustic Cavity Sonoluminescence (Axiom 4 Vacuum Saturation)

In standard physics, sonoluminescence involves complex, ad-hoc plasma models
to explain why acoustic sound waves in water produce flashes of optical light.
In Applied Vacuum Engineering (AVE), the explanation is structurally explicit:

1. A circular bounded cavity drives a standing acoustic wave (pressure antinode).
2. The pressure antinode traps a microscopic cavitation void.
3. The acoustic wave collapses the bubble, geometrically amplifying the fluid kinetic energy.
4. When the collapse radius approaches atomic scales (~1 Å), the kinetic energy density
   is deposited against the water molecules at the center.
5. This physical force translates directly into topological voltage on the underlying LC lattice.
6. When V_topo crosses the universal Dielectric Yield Limit (V_yield = 43.65 kV), the
   local LC lattice saturates (ε_eff → 0).
7. The energy has nowhere to go but to rupture the structural impedance, emitting
   broad-spectrum optical photons via Op7 bend loss.

This script elegantly models the exact amplitude and angle of that saturation point.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from ave.core.constants import EPSILON_0, L_NODE, V_YIELD

# ---------------------------------------------------------
# Cavity & Fluid Parameters
# ---------------------------------------------------------
RHO_WATER = 998.0  # Density of water (kg/m^3)
SIGMA_WATER = 0.072  # Surface tension (N/m)
MU_WATER = 0.001  # Dynamic viscosity (Pa·s)
P_ATMO = 101325.0  # Atmospheric pressure (Pa)

# Acoustic Cavity Drive
F_AC = 26500.0  # Acoustic frequency (Hz)
OMEGA_AC = 2.0 * np.pi * F_AC
N_CYCLES = 30  # Simulate 30 cycles to ramp up and down
T_TOTAL = N_CYCLES / F_AC

# Initial Bubble State
R_0 = 5.0e-6  # Equilibrium radius (5 microns)
P_GAS_0 = P_ATMO + 2.0 * SIGMA_WATER / R_0  # Assume internal gas is air, isothermal for this demo
GAMMA = 1.33  # Polytropic index for gas


def get_P_AC(t):
    # Ramp up and down: 1.05 atm base, up to 1.45 atm peak
    envelope = np.sin(np.pi * t / T_TOTAL)
    return (1.05 + 0.40 * envelope) * P_ATMO


# ---------------------------------------------------------
# AVE Topological Mapping Constants
# ---------------------------------------------------------
# Vacuum Capacitance per node = ε₀ * ℓ_node
C_NODE = EPSILON_0 * L_NODE

# Yield energy threshold per node
E_NODE_YIELD = 0.5 * C_NODE * V_YIELD**2
# Critical volumetric energy density that triggers vacuum rupture
U_YIELD_CRIT = E_NODE_YIELD / (L_NODE**3)

print("=== AVE Sonoluminescence: Swept Amplitude Challenge ===")
print(f"Vacuum Node Capacitance:  {C_NODE:.3e} F")
print(f"Node Yield Energy:        {E_NODE_YIELD:.3e} J")
print(f"Critical Energy Density:  {U_YIELD_CRIT:.3e} J/m^3")
print("=======================================================\n")


# ---------------------------------------------------------
# Rayleigh-Plesset Equation Solver
# ---------------------------------------------------------
def rayleigh_plesset(t, y):
    R, R_dot = y

    if R < 1e-10:
        return [0, 0]

    # Dynamically ramped driving acoustic field
    P_drive = -get_P_AC(t) * np.sin(OMEGA_AC * t)

    # Gas pressure inside bubble
    P_gas = P_GAS_0 * (R_0 / R) ** (3.0 * GAMMA)

    sum_pressures = P_gas - P_drive - P_ATMO - 2.0 * SIGMA_WATER / R - 4.0 * MU_WATER * R_dot / R
    R_ddot = (sum_pressures / RHO_WATER - 1.5 * R_dot**2) / R

    return [R_dot, R_ddot]


t_span = (0, T_TOTAL)
# We need high resolution to catch the 30 collapse spikes
t_eval = np.linspace(0, T_TOTAL, 200000)

print(f"Solving Rayleigh-Plesset bubble collapse over {N_CYCLES} acoustic cycles...")
sol = solve_ivp(rayleigh_plesset, t_span, [R_0, 0.0], t_eval=t_eval, method="Radau", rtol=1e-6, atol=1e-9)

t = sol.t
R = sol.y[0]
R_dot = sol.y[1]

# ---------------------------------------------------------
# Map to AVE Topological Voltage
# ---------------------------------------------------------
K_fluid = 2.0 * np.pi * RHO_WATER * R**3 * R_dot**2

# We map transient kinetic energy into a convergent $1/r^2$ spherical shockwave
# that focuses at r = 1 Ångström. We will plot the instantaneous V_topo at this focal point.
ETA_SHOCK = 0.50
R_focal = 1e-10  # 1 Ångström focal cluster
V_focal = (4.0 / 3.0) * np.pi * R_focal**3

# The energy in the shockwave at the moment of collapse is 50% of kinetic energy
U_focal = (K_fluid * ETA_SHOCK) / V_focal
V_topo_focal = np.sqrt(2.0 * U_focal * L_NODE**2 / EPSILON_0)

# ---------------------------------------------------------
# Plotting the Phase-Locked Challenge Validation
# ---------------------------------------------------------
plt.style.use("dark_background")
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)
fig.suptitle("AVE Sonoluminescence: Phase-Locked Topological Yield", fontsize=16, color="white")

# 1. Acoustic Drive Envelope
P_drive = -get_P_AC(t) * np.sin(OMEGA_AC * t)
axes[0].plot(t * 1e3, P_drive / P_ATMO, color="#00ffcc", lw=1)
axes[0].plot(t * 1e3, get_P_AC(t) / P_ATMO, color="white", linestyle="--", alpha=0.5, label="Envelope")
axes[0].plot(t * 1e3, -get_P_AC(t) / P_ATMO, color="white", linestyle="--", alpha=0.5)
axes[0].set_ylabel("Cavity Pressure (atm)", fontsize=12)
axes[0].set_title("Modulated Standing Wave Drive", color="white")
axes[0].legend(loc="upper right")
axes[0].grid(color="#333333", linestyle="--")

# 2. Bubble Radius (Phase Lock)
axes[1].plot(t * 1e3, R * 1e6, color="#ff33cc", lw=1)
axes[1].set_ylabel("Bubble Radius (μm)", fontsize=12)
axes[1].set_title("Phase-Locked Spherical Collapse", color="white")
axes[1].grid(color="#333333", linestyle="--")

# 3. Topological Strain (V_topo) at Focus
axes[2].plot(t * 1e3, V_topo_focal / 1e3, color="#eebb00", lw=1)
axes[2].axhline(
    V_YIELD / 1e3,
    color="red",
    linestyle="--",
    lw=2,
    label=f"AVE Yield Limit ({V_YIELD/1e3:.2f} kV)",
)
axes[2].set_yscale("log")
axes[2].set_ylim(1e-1, 1e4)
axes[2].set_ylabel("Topological Voltage (kV)", fontsize=12)
axes[2].set_xlabel("Time (ms)", fontsize=12)
axes[2].set_title("Vacuum Strain & Optical Rupture Point (Sonoluminescence Flashes)", color="white")
axes[2].legend(loc="upper left")
axes[2].grid(color="#333333", linestyle="--")

plt.tight_layout()
plt.savefig(
    f"{str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())}/manuscript/vol_4_engineering/figures/sonoluminescence_challenge.png",
    dpi=150,
)
print(f"Simulation completed. Exact peak V_topo reached at focal scalar: {np.nanmax(V_topo_focal)/1e3:.2f} kV")
print("Visuals saved to: manuscript/vol_4_engineering/figures/sonoluminescence_challenge.png")
