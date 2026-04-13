"""
Kolmogorov Cascade Visualization
================================

Generates a three-panel figure demonstrating:
    1. The topological Nyquist cutoff vs the classical Kolmogorov microscale
    2. Enstrophy bounds over the cascade process
    3. The derivation of the macroscopic avalanche exponent from 3D Poisson scaling.
"""

import os
import pathlib
import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import L_NODE
from ave.regime_3_saturated.kolmogorov_cutoff import (
    lattice_nyquist_wavenumber,
    avalanche_exponent_3d,
    axiomatic_energy_spectrum,
    kolmogorov_microscale,
    spectral_cascade_demo
)

def build_visualization():
    print("[*] Generating Kolmogorov Cascade Topology Visualizations...")
    project_root = pathlib.Path(__file__).parent.parent.parent.parent.absolute()
    
    # Typical water parameters
    nu_water = 1.0e-6    # m^2/s kinematic viscosity
    epsilon = 1.0e-3     # typical dissipation in pipe flow
    
    k_max = lattice_nyquist_wavenumber()
    eta_K = kolmogorov_microscale(nu_water, epsilon)
    k_K = 1.0 / eta_K    # Dissipation wavenumber
    
    # -------------------------------------------------------------
    # Render Panels
    # -------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.patch.set_facecolor('#111111')
    
    for ax in axes:
        ax.set_facecolor('#111111')
        ax.grid(color='#333333', linestyle='--', alpha=0.5)
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        for spine in ax.spines.values():
            spine.set_edgecolor('#555555')

    # Panel 1: Energy Spectrum
    ax1 = axes[0]
    
    # Span from large eddy (1m) down to past Nyquist limit
    k_range = np.logspace(0, np.log10(k_max * 10), 1000)
    
    # Classical E(k) ~ k^(-5/3) with exponential viscous rolloff
    C_K_empirical = 1.5
    E_classical = C_K_empirical * (epsilon**(2.0/3.0)) * (k_range**(-5.0/3.0)) * np.exp(-1.5 * k_range / k_K)
    
    # Axiomatic E(k) with Saturation cutoff
    E_axiomatic = axiomatic_energy_spectrum(k_range, epsilon, nu_water)
    
    ax1.loglog(k_range, E_classical, color='#aaaaaa', linestyle='--', lw=2, label='Classical w/ Viscous Rolloff')
    ax1.loglog(k_range, E_axiomatic, color='#00ffcc', lw=3, label='Axiomatic Saturation Cutoff')
    
    ax1.axvline(k_K, color='#ff9933', linestyle=':', lw=2, label=r'Classical Dissipation ($k_\eta$)')
    ax1.axvline(k_max, color='#ff3333', linestyle='-', lw=2, label=r'Topological Nyquist ($k_{\max}$)')
    
    ax1.set_title("Energy Spectrum $E(k)$ vs Lattice Cutoff")
    ax1.set_xlabel("Wavenumber $k$ $[m^{-1}]$")
    ax1.set_ylabel("$E(k)$")
    ax1.set_ylim(bottom=1e-35)  # Let high energy parts stay visible
    ax1.legend(loc='lower left')

    # Panel 2: Enstrophy / Demonstration
    ax2 = axes[1]
    # We use a 1D shell simulation proxy
    N_modes = 100
    Re_proxy = 1e5
    demo_data = spectral_cascade_demo(N_modes, Re_proxy)
    
    ax2.plot(demo_data['k'], demo_data['E_k'], 'o-', color='#ff33ff', markersize=3, label='Discrete Modal Cascade')
    ax2.axvline(demo_data['k_max'], color='#ff3333', lw=2, label='Lattice Yield')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_title("Shell Model Cascade Demonstration")
    ax2.set_xlabel("Wavenumber $k$")
    ax2.set_ylabel("Modal Energy Distribution")
    ax2.legend()
    
    # Panel 3: Avalanche Factor (Strain divergence)
    ax3 = axes[2]
    
    r_strain = np.linspace(0, 0.999, 500)
    
    # S^2 = 1 - r^2
    # M_1D = 1 / S^2 (n=2)
    M_1D = 1.0 / (1.0 - r_strain**2)
    
    # M_3D_isotropic = 1 / (1 - r^n_3d)
    n_3d = avalanche_exponent_3d()
    M_3D = 1.0 / (1.0 - r_strain**n_3d)
    
    # Empirical
    M_empirical = 1.0 / (1.0 - r_strain**1.8)
    
    ax3.plot(r_strain, M_1D, color='#aaaaaa', linestyle='--', lw=2, label='1D Axiom 4: Lorentz $\gamma^2$ ($n=2$)')
    ax3.plot(r_strain, M_empirical, color='#ff9933', linestyle='-.', lw=2, label='Empirical Solar Forecast ($n=1.8$)')
    ax3.plot(r_strain, M_3D, color='#ffcc00', lw=3, label=f'3D Isotropic Axiom 4 ($n={n_3d:.4f}$)')
    
    ax3.set_yscale('log')
    ax3.set_xlim(0, 1.05)
    ax3.set_ylim(1, 1000)
    ax3.set_title("Op22 Avalanche Factor $M(r)$")
    ax3.set_xlabel("Topological Shear Strain $r$ (Ratio to Yield)")
    ax3.set_ylabel("$M(r)$ Growth Factor")
    ax3.legend(loc='upper left')
    
    plt.tight_layout()
    
    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "kolmogorov_spectral_cutoff.png"
    plt.savefig(target, dpi=300)
    print(f"[*] Visualized Kolmogorov Cascade: {target}")

if __name__ == "__main__":
    build_visualization()
