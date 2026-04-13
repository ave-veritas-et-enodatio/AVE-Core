#!/usr/bin/env python3
"""
K4-TLM Gravitational Lensing Animation (10-second run)
======================================================
Generates a sequence of frames for a highly-resolved 2D K4-TLM simulation,
then compiles them into an MP4 video using ffmpeg.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm
import shutil
import subprocess

from ave.core.k4_tlm import K4Lattice2D, build_scattering_matrix

def apply_lens_2d(lattice, cx, cy, n0, r_core):
    if not lattice.nonlinear:
        pass
    for i in range(lattice.nx):
        for j in range(lattice.ny):
            r = np.sqrt((i - cx)**2 + (j - cy)**2)
            n = 1.0 + n0 / (1.0 + (r / r_core)**2)
            if n > 1.001:
                lattice._S_field[i, j, lattice.my_z] = build_scattering_matrix(z_local=1.0 / n)

def inject_beam_2d(lattice, y_center, beam_width, amplitude, wavelength, x_inj=2):
    k = 2.0 * np.pi / wavelength
    phase = k * lattice.timestep
    j_indices = np.arange(lattice.ny)
    dy = j_indices - y_center
    envelope = amplitude * np.exp(-dy**2 / (2.0 * beam_width**2))
    pulse = envelope * np.sin(phase)
    lattice.V_inc[x_inj, :, lattice.my_z, 0] += pulse

def main():
    print("=" * 60)
    print("  Generating 10s Gravitational Lensing Animation")
    print("=" * 60)
    
    NX, NY = 600, 240
    N_STEPS = 700
    BEAM_Y = NY // 2 + 15
    BEAM_W = 5.0
    WAVELENGTH = 10.0
    AMPLITUDE = 0.2
    R_CORE = 15.0
    N0 = 0.8
    FPS = 30
    FRAME_INTERVAL = 2  # capture every 2 steps -> 350 frames -> ~11.6 seconds

    frame_dir = "/tmp/k4_tlm_frames"
    if os.path.exists(frame_dir):
        shutil.rmtree(frame_dir)
    os.makedirs(frame_dir)

    print(f"Lattice: {NX}x{NY}")
    print(f"Total Steps: {N_STEPS}")
    print(f"Frames to generate: {N_STEPS // FRAME_INTERVAL}")
    
    lattice = K4Lattice2D(NX, NY, alternating_chirality=True, pml_thickness=20, nonlinear=True)
    cx, cy = NX // 2, NY // 2
    apply_lens_2d(lattice, cx, cy, N0, R_CORE)
    
    frame_idx = 0
    plt.ioff()
    
    # Pre-compute n_field for contours
    n_field = np.ones((NX, NY))
    for i in range(NX):
        for j in range(NY):
            r = np.sqrt((i - cx)**2 + (j - cy)**2)
            n_field[i, j] = 1.0 + N0 / (1.0 + (r / R_CORE)**2)
            
    vmax = 0.3 # fixed peak amplitude for color stability

    for step in range(N_STEPS):
        inject_beam_2d(lattice, BEAM_Y, BEAM_W, AMPLITUDE, WAVELENGTH)
        lattice.step()
        
        if step % FRAME_INTERVAL == 0:
            field = lattice.get_field_array().copy()
            
            fig, ax = plt.subplots(figsize=(12, 4.8), dpi=150)
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
            
            im = ax.imshow(
                field.T, cmap='hot', origin='lower',
                extent=[0, NX, 0, NY],
                norm=PowerNorm(gamma=0.5, vmin=0, vmax=vmax)
            )
            
            # Draw lens
            circle = plt.Circle((cx, cy), R_CORE, color='#00E5FF', fill=False, lw=1.5, ls='--', alpha=0.7)
            ax.add_patch(circle)
            ax.plot(cx, cy, '+', color='#00E5FF', ms=12, mew=2.5)
            
            # Draw reference trajectory
            ax.axhline(BEAM_Y, color='white', ls=':', alpha=0.4, lw=1)
            
            # n(r) contours
            ax.contour(np.arange(NX), np.arange(NY), n_field.T,
                       levels=[1.1, 1.3, 1.5], colors='#00E5FF',
                       linewidths=0.5, alpha=0.3)
                       
            ax.set_title(f"Acoustic Gravitational Lensing (n₀={N0}) | Step {step:04d}", 
                         color='white', fontsize=12, pad=10)
            ax.axis('off')
            plt.tight_layout()
            
            filename = os.path.join(frame_dir, f"frame_{frame_idx:04d}.png")
            plt.savefig(filename, facecolor='black', bbox_inches='tight')
            plt.close(fig)
            
            frame_idx += 1
            if frame_idx % 50 == 0:
                print(f"Rendered {frame_idx} frames...")

    out_mp4 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'sim_outputs', 'k4_tlm_gravitational_lensing_10s.mp4'))
    print(f"\nCompiling frames to MP4 at 30 fps using ffmpeg...")
    cmd = [
        "ffmpeg", "-y", "-framerate", str(FPS), 
        "-i", os.path.join(frame_dir, "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
        out_mp4
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Success! Animation saved to {out_mp4}")
    except Exception as e:
        print(f"ffmpeg failed: {e}")
        print("Saving as GIF fallback...")
        import imageio.v3 as iio
        frames = []
        for i in range(frame_idx):
            frames.append(iio.imread(os.path.join(frame_dir, f"frame_{i:04d}.png")))
        out_gif = out_mp4.replace('.mp4', '.gif')
        iio.imwrite(out_gif, frames, duration=1000/FPS, loop=0)
        print(f"Success! Animation saved to {out_gif}")

if __name__ == "__main__":
    main()
