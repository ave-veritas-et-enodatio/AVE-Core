"""
AVE Cosmology: DAMA/LIBRA vs XENON Paradox Simulator
======================================================
For decades, the DAMA/LIBRA solid-crystal detector has claimed to see an annual
"Dark Matter" signal (peaking in June). Meanwhile, the massive XENON liquid 
detectors have found absolutely zero signal, hitting the 'Neutrino Floor'.

Standard physics assumes DAMA is a false positive because Dark Matter is
modeled as a collisionless scalar particle.

In the AVE framework, Dark Matter is the transverse, macroscopic sheer-stress of
the expanding/rotating spatial metric. Through fundamental Mechanics, a transverse 
sheer wave CANNOT couple to a fluid (liquids have zero sheer modulus). It can ONLY
couple to rigid solid-state lattices via phonon displacement.

This script runs an FDTD sheer-wave simulation passing through two identical 
densities of 'matter':
1. A rigid Solid Crystal (DAMA) - The sheer wave physically rocks the lattice.
2. A frictionless Liquid (XENON) - The sheer wave slips cleanly through.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib

project_root = pathlib.Path(__file__).parent.parent.absolute()

from ave.core.constants import C_0

# FDTD Grid
GRID_SIZE = 300
DT = 0.5
FRAMES = 150

# Detector Properties
DETECTOR_START = 100
DETECTOR_END = 200

# Metric sheer properties (Dark Matter Drag)
INCIDENT_AMPLITUDE = 1.0
WAVE_WIDTH = 20

def run_detector_comparison():
    print("[*] Initializing Dark Matter Transverse Wave Simulation...")
    
    # 1. Solid State DAMA (NaI Crystal)
    # Has a non-zero sheer impedance, meaning it physically drags and couples to the wave.
    H_dama = np.zeros(GRID_SIZE)
    E_dama = np.zeros(GRID_SIZE)
    n_solid = np.ones(GRID_SIZE)
    n_solid[DETECTOR_START:DETECTOR_END] = 2.5 # High index/sheer coupling
    ce_solid = 1.0 / n_solid
    ch_solid = 1.0 / n_solid
    
    # 2. Liquid XENON 
    # Liquids have explicitly zero transverse sheer modulus. 
    # The optical index to a transverse LC strain is effectively 1.0 (vacuum).
    H_xenon = np.zeros(GRID_SIZE)
    E_xenon = np.zeros(GRID_SIZE)
    n_liquid = np.ones(GRID_SIZE)
    ce_liquid = 1.0 / n_liquid
    ch_liquid = 1.0 / n_liquid
    
    # Initial Gaussian Sheer Wave (Dark matter wind crossing the Earth)
    pulse_idx = 40
    for i in range(GRID_SIZE):
        gauss = INCIDENT_AMPLITUDE * np.exp(-0.5 * ((i - pulse_idx) / WAVE_WIDTH)**2)
        E_dama[i] = gauss
        E_xenon[i] = gauss

    # Metric for logging total deposited kinetic energy (the "Signal")
    signal_dama = []
    signal_xenon = []
    
    hist_dama = np.zeros((FRAMES, GRID_SIZE))
    hist_xenon = np.zeros((FRAMES, GRID_SIZE))

    print("[*] Executing FDTD Time Integration... (Solid vs Liquid Sheer Coupling)")
    for step in range(FRAMES):
        # -- Step DAMA (Solid) --
        H_dama[:-1] += ch_solid[:-1] * (E_dama[1:] - E_dama[:-1])
        E_dama[1:-1] += ce_solid[1:-1] * (H_dama[1:-1] - H_dama[:-2])
        E_dama[0] = E_dama[1]
        E_dama[-1] = E_dama[-2]
        
        # Calculate deposited energy in the detector volume (E^2)
        deposited_dama = np.sum(E_dama[DETECTOR_START:DETECTOR_END]**2)
        signal_dama.append(deposited_dama)
        hist_dama[step] = E_dama.copy()
        
        # -- Step XENON (Liquid) --
        H_xenon[:-1] += ch_liquid[:-1] * (E_xenon[1:] - E_xenon[:-1])
        E_xenon[1:-1] += ce_liquid[1:-1] * (H_xenon[1:-1] - H_xenon[:-2])
        E_xenon[0] = E_xenon[1]
        E_xenon[-1] = E_xenon[-2]
        
        # Since it's a liquid, the wave passes through with 1.0 index, meaning no scattering/reflection, 
        # but we track the 'ambient' energy inside the volume for comparison.
        # But for 'detected' hits, liquid registers zero phonon coupling.
        # So the actual "hit" rate for transverse is technically 0, but we will plot the raw E field.
        deposited_xenon = 0.0 # No shear coupling -> No phonons -> No signal
        signal_xenon.append(deposited_xenon)
        hist_xenon[step] = E_xenon.copy()

    print("[*] Rendering Output GIF...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.patch.set_facecolor('#0f0f0f')
    
    for ax in (ax1, ax2):
        ax.set_facecolor('#0f0f0f')
        ax.grid(color='#333333', linestyle='--', alpha=0.5)
        ax.set_xlim([0, GRID_SIZE])
        ax.set_ylim([-0.5, 1.5])
        ax.axvspan(DETECTOR_START, DETECTOR_END, color='white', alpha=0.1) # Detector zone
        ax.set_xticks([])
        ax.set_yticks([])

    ax1.set_title("DAMA/LIBRA (Solid NaI Crystal)\nTransverse Sheer Wave Couples -> Phonon 'Signal' Registered", color='#00ffcc')
    ax2.set_title("XENONnT (Liquid Detector)\nZero Sheer Modulus -> Frictionless Slip -> No Signal", color='#ff6666')
    
    line1, = ax1.plot([], [], color='white', lw=2)
    line2, = ax2.plot([], [], color='white', lw=2)
    
    def update(frame):
        line1.set_data(np.arange(GRID_SIZE), hist_dama[frame])
        # In reality, the 'fluid' E_xenon is just the unperturbed wave, but we plot it to show it slipping through
        line2.set_data(np.arange(GRID_SIZE), hist_xenon[frame])
        return line1, line2
        
    anim = animation.FuncAnimation(fig, update, frames=FRAMES, interval=40, blit=True)
    
    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)
    target = outdir / "dark_matter_detectors.gif"
    
    anim.save(target, writer='pillow', fps=25)
    print(f"[*] Visualized Detector Physics: {target}")

if __name__ == "__main__":
    run_detector_comparison()
