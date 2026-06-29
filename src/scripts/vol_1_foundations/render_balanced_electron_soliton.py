#!/usr/bin/env python3
"""Render side-by-side animation of the stable electron soliton on the vacuum lattice.

Simulates the balanced flywheel lock (gain=0.12, damping_rate=0.01, n=1.8095)
and exports K4 Voltage and Cosserat Microrotation slice profiles over time.
"""

import sys
import json
import math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Ground sys.path against workspace directory
sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")

from back_emf_feedback_v3 import apply_dark_wake_back_emf_v3  # noqa: E402
from native_electron_model import (  # noqa: E402
    N_LATTICE,
    PML,
    SHELL_RADIUS,
    _find_central_bond,
    _seed_canonical,
)
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

# Output paths in the artifacts directory
ARTIFACTS_DIR = Path("/Users/grantlindblom/.gemini/antigravity-ide/brain/ce76ca34-02ed-4ece-846a-998648642049")
GIF_PATH = ARTIFACTS_DIR / "balanced_electron_soliton.gif"
PNG_PATH = ARTIFACTS_DIR / "balanced_electron_soliton.png"

def main():
    print("Initializing engine for stable electron animation...", flush=True)
    engine = VacuumEngine3D.from_args(
        N=N_LATTICE,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
        use_lagrangian_emf_coupling=False,
    )
    _seed_canonical(engine, amplitude=0.92)

    n_steps = 400
    cadence = 10
    
    times = []
    e_slices = []
    w_slices = []
    
    # Samples
    for step in range(n_steps + 1):
        if step % cadence == 0:
            print(f"Step {step}/{n_steps}...", flush=True)
            v_sq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
            omega = np.asarray(engine.cos.omega)
            omega_mag = np.linalg.norm(omega, axis=-1)
            
            # Central slice at z = N // 2
            e_slices.append(v_sq[:, :, N_LATTICE // 2].copy())
            w_slices.append(omega_mag[:, :, N_LATTICE // 2].copy())
            times.append(step)
            
        if step < n_steps:
            engine.step()
            apply_dark_wake_back_emf_v3(
                engine,
                gain=0.12,
                damping_rate=0.01,
                n=1.8095
            )
            # Apply boundary leak
            cy0 = cz0 = N_LATTICE // 2
            from radiation_leak_boundary import apply_radiation_leak_boundary
            # Use N_LATTICE//2 since it is canonical seed (no drive)
            apply_radiation_leak_boundary(engine, (N_LATTICE // 2, cy0, cz0), SHELL_RADIUS)

    print("Generating figures...", flush=True)
    # 1. Render static panel
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor("#0a0a12")
    
    # Final state index
    final_idx = len(e_slices) - 1
    
    for ax, data, title, cmap in zip(
        axes,
        [e_slices[final_idx], w_slices[final_idx]],
        ["K4 Voltage ($V^2$)", "Cosserat Microrotation ($\|\\omega\|$)"],
        ["magma", "viridis"],
        strict=True
    ):
        ax.set_facecolor("#111118")
        im = ax.imshow(data, cmap=cmap, origin="lower")
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        ax.set_title(title, color="#ddd", fontsize=11)
        ax.axis("off")
        
    fig.suptitle(f"Balanced Flywheel Electron Soliton @ Step {n_steps}\n(Stable Confinement with Persistent Spin, $\\eta = 0.01$, Gain = 0.12)", color="#eee", fontsize=13)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved static summary to {PNG_PATH}", flush=True)

    # 2. Render animation
    print("Generating animation...", flush=True)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    fig.patch.set_facecolor("#0a0a12")
    
    im_e = axes[0].imshow(e_slices[0], cmap="magma", origin="lower")
    im_w = axes[1].imshow(w_slices[0], cmap="viridis", origin="lower")
    
    axes[0].axis("off")
    axes[1].axis("off")
    axes[0].set_title("K4 Voltage ($V^2$)", color="#ddd")
    axes[1].set_title("Cosserat Microrotation ($\|\\omega\|$)", color="#ddd")
    
    cb_e = plt.colorbar(im_e, ax=axes[0], fraction=0.046, pad=0.04)
    cb_w = plt.colorbar(im_w, ax=axes[1], fraction=0.046, pad=0.04)
    
    title_text = fig.suptitle("", color="#eee", fontsize=13)
    
    def update(frame):
        im_e.set_data(e_slices[frame])
        im_w.set_data(w_slices[frame])
        
        # update colors limit
        im_e.set_clim(vmin=0, vmax=max(e_slices[frame].max(), 1e-6))
        im_w.set_clim(vmin=0, vmax=max(w_slices[frame].max(), 1e-6))
        
        title_text.set_text(f"Balanced Flywheel Electron Soliton — Step {times[frame]}\n(Stable Confinement with Persistent Spin)")
        return im_e, im_w, title_text
        
    anim = FuncAnimation(fig, update, frames=len(times), interval=100, blit=False)
    writer = PillowWriter(fps=10)
    anim.save(GIF_PATH, writer=writer)
    plt.close(fig)
    print(f"Saved animation to {GIF_PATH}", flush=True)

if __name__ == "__main__":
    main()
