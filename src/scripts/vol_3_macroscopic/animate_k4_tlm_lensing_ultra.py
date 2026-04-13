#!/usr/bin/env python3
"""
K4-TLM Gravitational Lensing Animation (Ultra version)
======================================================
Length: 20 seconds, 60 FPS (1200 frames).
Expanded lattice size to support the longer photon transit.
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

from ave.core.k4_tlm import K4Lattice2D, build_k4_scattering_matrix

def apply_lens_2d(lattice, cx, cy, n0, r_core):
    for i in range(lattice.nx):
        for j in range(lattice.ny):
            r = np.sqrt((i - cx)**2 + (j - cy)**2)
            n = 1.0 + n0 / (1.0 + (r / r_core)**2)
            if n > 1.001:
                chirality = lattice.nodes[i, j].chirality
                lattice.nodes[i, j].S_matrix = build_k4_scattering_matrix(
                    z_local=1.0 / n, chirality=chirality
                )

def inject_beam_2d(lattice, y_center, beam_width, amplitude, wavelength, x_inj=2):
    k = 2.0 * np.pi / wavelength
    phase = k * lattice.timestep
    for j in range(lattice.ny):
        dy = j - y_center
        envelope = amplitude * np.exp(-dy**2 / (2.0 * beam_width**2))
        if envelope > 1e-8:
            lattice.nodes[x_inj, j].V_inc[0] += envelope * np.sin(phase)

def main():
    print("=" * 60)
    print("  Generating 20s Gravitational Lensing Animation (Halved Res)")
    print("  [Optimized In-Memory FFmpeg Pipeline - 4x Physical Speed]")
    print("=" * 60)
    
    NX, NY = 550, 180
    N_STEPS = 2400     # 4x more time
    BEAM_Y = NY // 2 + 12
    BEAM_W = 3.0
    WAVELENGTH = 5.0
    AMPLITUDE = 0.2
    R_CORE = 10.0
    N0 = 0.85
    FPS = 30
    FRAME_INTERVAL = 4  # 600 frames @ 30fps = 20 seconds
    
    print(f"Lattice: {NX}x{NY}")
    print(f"Total Steps: {N_STEPS} (Outputting every {FRAME_INTERVAL} steps)")
    print(f"Total Frames: {N_STEPS // FRAME_INTERVAL}")
    
    lattice = K4Lattice2D(NX, NY, alternating_chirality=True)
    cx, cy = NX // 2, NY // 2
    apply_lens_2d(lattice, cx, cy, N0, R_CORE)
    
    frame_idx = 0
    plt.ioff()
    
    n_field = np.ones((NX, NY))
    for i in range(NX):
        for j in range(NY):
            r = np.sqrt((i - cx)**2 + (j - cy)**2)
            n_field[i, j] = 1.0 + N0 / (1.0 + (r / R_CORE)**2)
            
    vmax = 0.3

    # ── OPTIMIZATION: Create figure once and stream directly to FFmpeg ──
    fig, ax = plt.subplots(figsize=(16, 5.23), dpi=150)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    
    im = ax.imshow(
        np.zeros((NY, NX)), cmap='hot', origin='lower',
        extent=[0, NX, 0, NY],
        norm=PowerNorm(gamma=0.5, vmin=0, vmax=vmax)
    )
    
    circle = plt.Circle((cx, cy), R_CORE, color='#00E5FF', fill=False, lw=1.5, ls='--', alpha=0.7)
    ax.add_patch(circle)
    ax.plot(cx, cy, '+', color='#00E5FF', ms=12, mew=2.5)
    ax.axhline(BEAM_Y, color='white', ls=':', alpha=0.4, lw=1)
    
    ax.contour(np.arange(NX), np.arange(NY), n_field.T,
               levels=[1.1, 1.3, 1.5], colors='#00E5FF',
               linewidths=0.5, alpha=0.3)
               
    title_text = ax.set_title(f"", color='white', fontsize=12, pad=10)
    ax.axis('off')
    plt.tight_layout()
    
    # Get physical pixel dimensions for FFmpeg
    fig.canvas.draw()
    width, height = fig.canvas.get_width_height()
    width = (width // 2) * 2
    height = (height // 2) * 2

    out_mp4 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'manuscript', 'vol_3_macroscopic', 'figures', 'k4_tlm_gravitational_lensing_halvres.mp4'))
    print(f"\nStreaming directly to FFmpeg at {FPS} fps...")
    print(f"Output Path: {out_mp4}")
    
    cmd = [
        "ffmpeg", "-y", 
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}", 
        "-pix_fmt", "rgba",
        "-r", str(FPS), 
        "-i", "-",
        "-c:v", "libx264", 
        "-pix_fmt", "yuv420p", 
        "-crf", "18",
        out_mp4
    ]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for step in range(N_STEPS):
        inject_beam_2d(lattice, BEAM_Y, BEAM_W, AMPLITUDE, WAVELENGTH)
        lattice.step()
        
        if step % FRAME_INTERVAL == 0:
            field = lattice.get_field_array()
            im.set_data(field.T)
            title_text.set_text(f"Acoustic Gravitational Lensing (n₀={N0}) | Accelerated Physical Run | Step {step:04d}")
            
            fig.canvas.draw()
            rgba = np.asarray(fig.canvas.buffer_rgba())
            process.stdin.write(rgba.tobytes())
            
            frame_idx += 1
            if frame_idx % 50 == 0:
                print(f"Rendered {frame_idx} frames...")
                sys.stdout.flush()
                
    process.stdin.close()
    process.wait()
    plt.close(fig)
    print(f"Success! Animation strictly compiled into {out_mp4}")
    
if __name__ == "__main__":
    main()
