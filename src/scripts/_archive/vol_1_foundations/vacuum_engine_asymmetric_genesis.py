"""
Phase III-B — pair-creation sweep using VacuumEngine3D (Stage 3 of plan
`document-list-for-next-chat-compressed-thunder.md`).

Configuration matrix (per plan):
  Wavelength λ ∈ {3.5, 5, 7, 10} cells   — spans ω·τ_relax ∈ {1.80, 1.26, 0.90, 0.63}
  Amplitude  A ∈ {0.3, 0.5, 0.7}·V_SNAP   — anti-node peaks at 0.6, 1.0, 1.4·V_SNAP
  Temperature T ∈ {0, 1.7e-2 m_e c²}       — cold null + pair-regime (~10⁸ K equiv)

Pre-registered outcomes:
  P_IIIb-α:  T=0 cold vacuum gives NO pair creation at ANY (λ, amp) (C1 control).
  P_IIIb-β:  T>0 classical regime (λ=10, ω·τ=0.63) gives amplitude-scaling pairs.
  P_IIIb-γ:  T>0 high-freq regime (λ=3.5, ω·τ=1.80) gives ENHANCED rate vs λ=10.
  P_IIIb-δ:  Sharp ω threshold near ω·τ_relax ≈ 1 (cascade signature).

Key observable: σ(ω) at fixed amplitude (specifically max A²_cos reached, which
proxies for the Cosserat-response strength / pair-creation amplitude).

Outputs:
  /tmp/phase_iiib_sweep.npz           — raw data for all 24 runs
  /tmp/phase_iiib_sweep_summary.png    — 4-panel summary plot
  /tmp/phase_iiib_sigma_omega.png      — σ(ω) curve (the key falsifiable prediction)
  /tmp/phase_iiib_sweep_log.txt        — per-run log
"""

import json
import time
from dataclasses import dataclass
import imageio
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.topological.vacuum_engine import (
    CWSource,
    EnergyBudgetObserver,
    RegimeClassifierObserver,
    TopologyObserver,
    VacuumEngine3D,
)


@dataclass
class RunConfig:
    wavelength: float  # cells
    amplitude: float  # V_SNAP-units (left source)
    amplitude2: float # V_SNAP-units (right source)
    temperature: float  # m_e c² units
    N: int = 48
    pml: int = 6
    t_ramp: float = 20.0
    t_sustain: float = 150.0
    n_outer_steps: int = 240
    record_cadence: int = 5
    seed: int = 42

    @property
    def omega_carrier(self) -> float:
        """ω = 2π·c / λ, natural units (c = 1, ℓ_node = 1)."""
        return 2.0 * np.pi / self.wavelength

    @property
    def omega_tau(self) -> float:
        """ω·τ_relax product (τ_relax = 1 in natural units)."""
        return self.omega_carrier


def run_one_config(cfg: RunConfig) -> dict:
    """Run a single (λ, amp, T) configuration through the engine."""
    engine = VacuumEngine3D.from_args(
        N=cfg.N,
        pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        use_lagrangian_emf_coupling=True,
    )

    # Two CW sources, counter-propagating, ASYMMETRIC amplitude
    source_offset = 8  # cells from boundary
    engine.add_source(
        CWSource(
            x0=source_offset,
            direction=(1.0, 0.0, 0.0),
            amplitude=cfg.amplitude,
            omega=cfg.omega_carrier,
            sigma_yz=4.0,
            t_ramp=cfg.t_ramp,
            t_sustain=cfg.t_sustain,
        )
    )
    engine.add_source(
        CWSource(
            x0=cfg.N - source_offset,
            direction=(-1.0, 0.0, 0.0),
            amplitude=cfg.amplitude2,
            omega=cfg.omega_carrier,
            sigma_yz=4.0,
            t_ramp=cfg.t_ramp,
            t_sustain=cfg.t_sustain,
        )
    )

    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    # threshold_frac=0.7 filters out thermal-noise peaks; only strong
    # (pair-candidate) centroids pass. Reraise to 0.5 if too aggressive.
    topo_obs = TopologyObserver(cadence=cfg.record_cadence, threshold_frac=0.7)
    energy_obs = EnergyBudgetObserver(cadence=cfg.record_cadence)
    engine.add_observer(regime_obs)
    engine.add_observer(topo_obs)
    engine.add_observer(energy_obs)

    t0 = time.time()
    
    # Custom run loop to capture frames for animation
    frames = []
    z_mid = cfg.N // 2
    for step in range(cfg.n_outer_steps):
        engine.step()
        if step % 2 == 0:
            # Capture the Cosserat spin amplitude slice
            from ave.topological.k4_cosserat_coupling import _cosserat_A_squared
            A2_cos = _cosserat_A_squared(
                engine._coupled.cos.u,
                engine._coupled.cos.omega,
                engine._coupled.cos.dx,
                engine._coupled.cos.omega_yield,
                engine._coupled.cos.epsilon_yield,
            )
            # Take a slice at z = mid, and extract the real values
            slice_data = np.asarray(A2_cos[:, :, z_mid])
            
            # Create an RGB image from the array (mapped with a colormap)
            fig, ax = plt.subplots(figsize=(5,5))
            ax.imshow(slice_data, vmin=0, vmax=1.0, cmap="magma", origin="lower")
            ax.set_title(f"Step {step}")
            ax.axis('off')
            fig.canvas.draw()
            image_from_plot = np.asarray(fig.canvas.buffer_rgba())[..., :3]
            frames.append(image_from_plot)
            plt.close(fig)
            
    elapsed = time.time() - t0
    
    # Save the animation to the artifacts directory
    artifact_dir = "/Users/grantlindblom/.gemini/antigravity-ide/brain/ce76ca34-02ed-4ece-846a-998648642049/"
    gif_path = os.path.join(artifact_dir, "asymmetric_genesis.gif")
    imageio.mimsave(gif_path, frames, fps=15)
    print(f"Saved animation to {gif_path}")

    regime_hist = regime_obs.history
    topo_hist = topo_obs.history
    energy_hist = energy_obs.history

    # Extract key scalars
    max_A2_total = max((h["max_A2_total"] for h in regime_hist), default=0.0)
    max_A2_cos = max((h["max_A2_cos"] for h in regime_hist), default=0.0)
    max_A2_k4 = max((h["max_A2_k4"] for h in regime_hist), default=0.0)
    max_centroids = max((h["n_centroids"] for h in topo_hist), default=0)
    max_Q_hopf = max((abs(h["Q_hopf"]) for h in topo_hist), default=0.0)
    final_centroids = topo_hist[-1]["n_centroids"] if topo_hist else 0
    max_rupture_cells = max((h["rupture"] for h in regime_hist), default=0)

    # Verdict
    if max_A2_cos >= 0.5 and max_centroids >= 2:
        verdict = "P_IIIb-pair"
    elif max_A2_cos > 1e-3:
        verdict = "P_IIIb-partial"
    else:
        verdict = "P_IIIb-no-response"

    return {
        "config": {
            "wavelength": cfg.wavelength,
            "amplitude": cfg.amplitude,
            "temperature": cfg.temperature,
            "N": cfg.N,
            "omega_tau": cfg.omega_tau,
            "n_steps": cfg.n_outer_steps,
        },
        "elapsed_s": elapsed,
        "max_A2_total": max_A2_total,
        "max_A2_cos": max_A2_cos,
        "max_A2_k4": max_A2_k4,
        "max_centroids": int(max_centroids),
        "final_centroids": int(final_centroids),
        "max_Q_hopf": float(max_Q_hopf),
        "max_rupture_cells": int(max_rupture_cells),
        "verdict": verdict,
        # Drop full histories to save memory; keep scalars only
    }


def run_sweep() -> list[dict]:
    """Run a single Asymmetric Genesis test."""
    results = []
    
    print(f"Path A: Asymmetric Genesis Collision")
    print(f"Left photon: 0.8 V_SNAP, Right photon: 0.4 V_SNAP")
    
    cfg = RunConfig(
        wavelength=10.0, 
        amplitude=0.8, 
        amplitude2=0.4, 
        temperature=0.1,
        n_outer_steps=300
    )
    
    r = run_one_config(cfg)
    results.append(r)
    print(
        f"Result: {r['max_A2_cos']:>11.3e} max A2_cos | "
        f"{r['max_centroids']} centroids | {r['verdict']}"
    )
    return results


def render_summary(results: list[dict], out: str = "/tmp/phase_iiib_sweep_summary.png") -> None:
    """4-panel summary: max A²_cos heatmaps at T=0 and T>0, amplitude scaling, ω-dependence."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    temps = sorted(set(r["config"]["temperature"] for r in results))

    # Heatmap: max_A²_cos vs (λ, amp) at each T
    for col, T in enumerate(temps):
        ax = axes[0, col]
        wls = sorted(set(r["config"]["wavelength"] for r in results))
        amps = sorted(set(r["config"]["amplitude"] for r in results))
        grid = np.zeros((len(amps), len(wls)))
        for r in results:
            if r["config"]["temperature"] != T:
                continue
            i = amps.index(r["config"]["amplitude"])
            j = wls.index(r["config"]["wavelength"])
            grid[i, j] = r["max_A2_cos"]
        im = ax.imshow(
            grid,
            origin="lower",
            cmap="viridis",
            aspect="auto",
            extent=[wls[0] - 0.5, wls[-1] + 0.5, amps[0] - 0.05, amps[-1] + 0.05],
        )
        ax.set_xticks(wls)
        ax.set_yticks(amps)
        ax.set_xlabel("λ (cells)")
        ax.set_ylabel("amp (V_SNAP)")
        ax.set_title(f"max A²_Cosserat  (T = {T:.2e} m_e c²)")
        plt.colorbar(im, ax=ax)
        # Annotate each cell
        for i, a in enumerate(amps):
            for j, w in enumerate(wls):
                ax.text(
                    w,
                    a,
                    f"{grid[i, j]:.1e}",
                    ha="center",
                    va="center",
                    fontsize=7,
                    color="white" if grid[i, j] < grid.max() / 2 else "black",
                )

    # σ(ω) plot at each amp, finite T
    ax = axes[1, 0]
    T_hot = temps[-1] if len(temps) > 1 else temps[0]
    wls = sorted(set(r["config"]["wavelength"] for r in results))
    amps = sorted(set(r["config"]["amplitude"] for r in results))
    for a_idx, amp in enumerate(amps):
        omega_taus = []
        sigmas = []
        for wl in wls:
            for r in results:
                if (
                    r["config"]["temperature"] == T_hot
                    and r["config"]["amplitude"] == amp
                    and r["config"]["wavelength"] == wl
                ):
                    omega_taus.append(r["config"]["omega_tau"])
                    sigmas.append(r["max_A2_cos"])
                    break
        ax.plot(
            omega_taus,
            sigmas,
            "o-",
            lw=1.4,
            label=f"amp = {amp:.2f}·V_SNAP",
            color=plt.cm.plasma(a_idx / max(len(amps) - 1, 1)),
        )
    ax.axvline(1.0, color="red", ls="--", lw=1, alpha=0.5, label="ω·τ_relax = 1")
    ax.set_xlabel("ω·τ_relax (natural units)")
    ax.set_ylabel("max A²_Cosserat (at T = %.1e m_ec²)" % T_hot)
    ax.set_yscale("log")
    ax.set_title("σ(ω): Cosserat response vs. photon frequency")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    # Verdict matrix
    ax = axes[1, 1]
    verdict_colors = {
        "P_IIIb-pair": "#2a7",
        "P_IIIb-partial": "#f90",
        "P_IIIb-no-response": "#c33",
    }
    for r in results:
        T_val = r["config"]["temperature"]
        T_idx = temps.index(T_val)
        wl = r["config"]["wavelength"]
        amp = r["config"]["amplitude"]
        color = verdict_colors.get(r["verdict"], "gray")
        # Plot as scatter: x = ω·τ, y = amp, color = verdict, size = T_idx
        ax.scatter(
            r["config"]["omega_tau"],
            amp,
            color=color,
            s=200 if T_idx > 0 else 80,
            alpha=0.7,
            edgecolors="black",
            linewidths=0.5,
        )
    ax.axvline(1.0, color="red", ls="--", lw=1, alpha=0.5)
    ax.set_xlabel("ω·τ_relax")
    ax.set_ylabel("amplitude (V_SNAP)")
    ax.set_title("Verdict matrix — green=pair, orange=partial, red=no-response\n" "small=cold, large=hot")
    ax.grid(alpha=0.3)

    plt.suptitle(
        "Phase III-B — Two-photon pair creation sweep " f"(4λ × 3amp × {len(temps)}T = {len(results)} configs)",
        fontsize=12,
    )
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def render_sigma_omega(results: list[dict], out: str = "/tmp/phase_iiib_sigma_omega.png") -> None:
    """The KEY falsifiable-prediction plot: σ(ω) at fixed amp, finite T."""
    fig, ax = plt.subplots(1, 1, figsize=(9, 6))

    temps = sorted(set(r["config"]["temperature"] for r in results))
    T_hot = temps[-1] if len(temps) > 1 else temps[0]
    wls = sorted(set(r["config"]["wavelength"] for r in results))
    amps = sorted(set(r["config"]["amplitude"] for r in results))

    for a_idx, amp in enumerate(amps):
        omega_taus = []
        cos_responses = []
        for wl in wls:
            for r in results:
                if (
                    r["config"]["temperature"] == T_hot
                    and r["config"]["amplitude"] == amp
                    and r["config"]["wavelength"] == wl
                ):
                    omega_taus.append(r["config"]["omega_tau"])
                    cos_responses.append(r["max_A2_cos"])
                    break
        if omega_taus:
            # Sort by ω·τ
            order = np.argsort(omega_taus)
            omega_taus = np.array(omega_taus)[order]
            cos_responses = np.array(cos_responses)[order]
            ax.plot(
                omega_taus,
                cos_responses,
                "o-",
                lw=2.0,
                markersize=8,
                label=f"amp = {amp:.2f}·V_SNAP",
                color=plt.cm.plasma(a_idx / max(len(amps) - 1, 1)),
            )

    # Mark τ_relax = 1 crossover
    ax.axvline(1.0, color="red", ls="--", lw=1.5, alpha=0.7, label="ω·τ_relax = 1 (cascade onset?)")

    ax.set_xlabel(r"$\omega \cdot \tau_{relax}$  (natural units)", fontsize=11)
    ax.set_ylabel(r"max $A^2_{Cosserat}$  (proxy for pair-creation rate)", fontsize=11)
    ax.set_yscale("log")
    ax.set_title(
        f"σ(ω): Cosserat response vs photon frequency at T = {T_hot:.1e} m_ec²\n"
        "AVE-native falsifiable prediction (C5 from doc 46_): "
        "knee expected near ω·τ = 1 if cascade mechanism active",
        fontsize=11,
    )
    ax.legend(fontsize=10, loc="best")
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase III-B vacuum-engine Asymmetric Genesis ──\n")
    results = run_sweep()
    r = results[0]
    print("\n── Verdict Summary ──")
    print(f"Verdict: {r['verdict']}")
    print(f"Max A2_cos: {r['max_A2_cos']:.3e}")
    print(f"Max Centroids: {r['max_centroids']}")
    print(f"Max Q_hopf: {r['max_Q_hopf']:.3e}")
