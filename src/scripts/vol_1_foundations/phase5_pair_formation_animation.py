#!/usr/bin/env python3
"""
Phase 5 pair-formation animation driver.

Runs a STRESS-config head-on collision (above P_phase5 registration)
with the PairNucleationGate observer and produces two animations:

  (A) /tmp/phase5_pair_formation.gif
      2D slice of |ω|² magnitude + h_local sign (chirality color-coded).
      Gate firings marked with yellow stars.
      Shows: two sources inject from opposite ends → Cosserat ω builds
      at the collision region → chirality develops → gate fires →
      counter-rotating Beltrami pair appears on one K4 bond.

  (B) /tmp/phase5_dark_wake.gif
      2D slice of τ_zx shear field showing the BEMF back-EMF wave
      propagating backward from the pair-creation event. Per doc 49_,
      the dark wake IS the AVE-native Lenz-law back-EMF of the K4
      mutual-inductance network — Newton's 3rd law in lattice form.

**This is a STRESS config, not a P_phase5 validation:**
- N=32, pml=3, T=0.1, amp=1.0·V_SNAP (above registered 0.5)
- Goal is to FORCE C1 crossing and produce visible dynamics
- Not for pre-registered adjudication; for visualization only.

Usage:
  python src/scripts/vol_1_foundations/phase5_pair_formation_animation.py
    → writes both gifs to /tmp/
    → exits 0 unless simulation crashes
"""
from __future__ import annotations

import sys
import time
from dataclasses import dataclass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import TwoSlopeNorm

from ave.topological.vacuum_engine import (
    AutoresonantCWSource,
    PairNucleationGate,
    RegimeClassifierObserver,
    VacuumEngine3D,
)


@dataclass
class RunConfig:
    wavelength: float = 3.5
    amplitude: float = 0.7           # V_SNAP units (STRESS, above P_phase5's 0.5)
    temperature: float = 0.1
    N: int = 32
    pml: int = 3
    t_ramp_periods: float = 2.0
    t_sustain_periods: float = 12.0
    t_observe_post_drive_periods: float = 8.0
    record_cadence: int = 2          # Frame every N steps

    @property
    def omega_carrier(self) -> float:
        return 2.0 * np.pi / self.wavelength

    @property
    def period(self) -> float:
        return 2.0 * np.pi / self.omega_carrier

    @property
    def n_outer_steps(self) -> int:
        total_time = (
            self.t_ramp_periods + self.t_sustain_periods
            + self.t_observe_post_drive_periods
        ) * self.period
        return int(total_time * np.sqrt(2.0)) + 1

    @property
    def drive_end_time(self) -> float:
        return (self.t_ramp_periods + self.t_sustain_periods + 1.0) * self.period


def _compute_h_local_slice(omega_slice: np.ndarray, dx: float) -> np.ndarray:
    """Approx local helicity h = ω·(∇×ω)/(|ω|·|∇×ω|) on 2D slice.

    omega_slice: (N, N, 3) — a 2D slice of the 3D ω field.
    Returns: (N, N) field in [-1, +1].

    Uses centered differences on the 2D slice for ∂x, ∂y components of
    curl; the third curl component needs out-of-slice info which we
    approximate as zero (this is a visualization, not a physics calc).
    """
    # Partials of ω components w.r.t. 2D slice axes
    dwx_dy = np.gradient(omega_slice[..., 0], dx, axis=1)
    dwy_dx = np.gradient(omega_slice[..., 1], dx, axis=0)
    dwz_dx = np.gradient(omega_slice[..., 2], dx, axis=0)
    dwz_dy = np.gradient(omega_slice[..., 2], dx, axis=1)

    # curl z-component = ∂_x ω_y − ∂_y ω_x
    curl_z = dwy_dx - dwx_dy
    # curl x-component = ∂_y ω_z − ∂_z ω_y ≈ ∂_y ω_z (drop ∂_z)
    curl_x = dwz_dy
    # curl y-component = ∂_z ω_x − ∂_x ω_z ≈ -∂_x ω_z
    curl_y = -dwz_dx

    curl = np.stack([curl_x, curl_y, curl_z], axis=-1)
    w_dot_curl = np.sum(omega_slice * curl, axis=-1)
    w_norm = np.sqrt(np.sum(omega_slice ** 2, axis=-1)) + 1e-12
    c_norm = np.sqrt(np.sum(curl ** 2, axis=-1)) + 1e-12
    h = w_dot_curl / (w_norm * c_norm)
    return np.clip(h, -1.0, 1.0)


def _compute_tau_zx_slice(engine, slice_axis=2, slice_idx=None) -> np.ndarray:
    """Return 2D τ_zx slice (y, z) if slice_axis=0 etc.

    τ_zx = z_local · ∂|V|²/∂x per DarkWakeObserver formula.
    """
    from ave.topological.cosserat_field_3d import tetrahedral_gradient
    from ave.topological.vacuum_engine import _v_squared_per_site

    if slice_idx is None:
        slice_idx = engine.N // 2

    V_sq = _v_squared_per_site(engine.k4.V_inc)
    A_sq = V_sq / (engine.V_SNAP ** 2)
    grad_A_sq = tetrahedral_gradient(A_sq) / engine.k4.dx
    grad_x = grad_A_sq[..., 0]  # propagation axis = 0
    z_local = engine.k4.z_local_field
    tau_zx = z_local * grad_x

    alive = engine.k4.mask_active.astype(float)
    tau_on_active = tau_zx * alive

    if slice_axis == 0:
        return tau_on_active[slice_idx, :, :]
    elif slice_axis == 1:
        return tau_on_active[:, slice_idx, :]
    else:
        return tau_on_active[:, :, slice_idx]


def run_collision(cfg: RunConfig) -> dict:
    engine = VacuumEngine3D.from_args(
        N=cfg.N, pml=cfg.pml,
        temperature=cfg.temperature,
        amplitude_convention="V_SNAP",
    )
    period = cfg.period
    t_ramp = cfg.t_ramp_periods * period
    t_sustain = cfg.t_sustain_periods * period
    src_offset = cfg.pml + 3

    engine.add_source(AutoresonantCWSource(
        x0=src_offset, direction=(1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
    ))
    engine.add_source(AutoresonantCWSource(
        x0=cfg.N - src_offset, direction=(-1.0, 0.0, 0.0),
        amplitude=cfg.amplitude, omega=cfg.omega_carrier,
        sigma_yz=3.0, t_ramp=t_ramp, t_sustain=t_sustain,
        t_decay=period,
    ))

    gate = PairNucleationGate(cadence=cfg.record_cadence)
    regime_obs = RegimeClassifierObserver(cadence=cfg.record_cadence)
    engine.add_observer(gate)
    engine.add_observer(regime_obs)

    # Record state at each cadence step — 2D slice at z = N/2
    slice_idx = cfg.N // 2
    dx = engine.cos.dx

    frame_times = []
    frame_omega_sq = []      # |ω|² in the z-slice
    frame_h_local = []       # h_local in the z-slice
    frame_tau_zx = []        # τ_zx in the z-slice
    frame_firings = []       # list of fired-bond keys so far at this frame
    fired_so_far: list = []

    t0 = time.time()
    for step in range(cfg.n_outer_steps):
        engine.step()
        if engine.step_count % cfg.record_cadence != 0:
            continue

        # Snapshot ω at z-slice
        omega_slice = np.asarray(engine.cos.omega[:, :, slice_idx, :]).copy()
        omega_sq = np.sum(omega_slice ** 2, axis=-1)
        h_local = _compute_h_local_slice(omega_slice, dx)
        tau_slice = _compute_tau_zx_slice(engine, slice_axis=2, slice_idx=slice_idx)

        # Update firings list
        if gate.history and gate.history[-1]["n_fired_this_step"] > 0:
            for key in gate.history[-1]["fired_bonds"]:
                fired_so_far.append(key)

        frame_times.append(engine.time)
        frame_omega_sq.append(omega_sq)
        frame_h_local.append(h_local)
        frame_tau_zx.append(tau_slice)
        # Only keep firings whose z coordinate is within 1 cell of the slice
        # (so they'd be visible in this slice)
        visible_firings = []
        for (Ai, Aj, Ak, port) in fired_so_far:
            if abs(Ak - slice_idx) <= 1:
                visible_firings.append((Ai, Aj, Ak, port))
        frame_firings.append(visible_firings.copy())

    elapsed = time.time() - t0

    return {
        "config": cfg,
        "elapsed_s": elapsed,
        "gate_history": gate.history,
        "regime_history": regime_obs.history,
        "frame_times": frame_times,
        "frame_omega_sq": frame_omega_sq,
        "frame_h_local": frame_h_local,
        "frame_tau_zx": frame_tau_zx,
        "frame_firings": frame_firings,
        "total_firings": gate._total_firings,
        "slice_idx": slice_idx,
    }


def make_pair_formation_gif(result: dict, out: str = "/tmp/phase5_pair_formation.gif") -> None:
    """Animation A — |ω|² magnitude + h_local sign + gate firings."""
    cfg = result["config"]
    period = cfg.period
    times = np.array(result["frame_times"])
    omega_sq_frames = result["frame_omega_sq"]
    h_local_frames = result["frame_h_local"]
    firings_frames = result["frame_firings"]
    drive_end = cfg.drive_end_time

    if not omega_sq_frames:
        print("No frames to animate — skipping pair_formation gif.")
        return

    # Fixed colormap limits (from max across all frames)
    omega_sq_max = max(np.max(f) for f in omega_sq_frames) + 1e-12

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    im1 = axes[0].imshow(
        omega_sq_frames[0].T, origin="lower", cmap="hot",
        vmin=0, vmax=omega_sq_max, aspect="equal",
    )
    axes[0].set_title("|ω|² magnitude (Cosserat energy density)", fontsize=11)
    axes[0].set_xlabel("x (lattice cells)")
    axes[0].set_ylabel("y (lattice cells)")
    plt.colorbar(im1, ax=axes[0], fraction=0.046, pad=0.04)

    im2 = axes[1].imshow(
        h_local_frames[0].T, origin="lower", cmap="RdBu_r",
        vmin=-1.0, vmax=1.0, aspect="equal",
    )
    axes[1].set_title("h_local sign (chirality: blue=LH, red=RH)", fontsize=11)
    axes[1].set_xlabel("x (lattice cells)")
    axes[1].set_ylabel("y (lattice cells)")
    plt.colorbar(im2, ax=axes[1], fraction=0.046, pad=0.04)

    # Firing markers (empty initially)
    fire_scatter_1 = axes[0].scatter([], [], marker="*", s=120, color="yellow",
                                     edgecolor="black", linewidth=0.5, zorder=10)
    fire_scatter_2 = axes[1].scatter([], [], marker="*", s=120, color="yellow",
                                     edgecolor="black", linewidth=0.5, zorder=10)

    title_text = fig.suptitle("", fontsize=12)

    def update(frame_idx):
        omega_sq = omega_sq_frames[frame_idx]
        h = h_local_frames[frame_idx]
        firings = firings_frames[frame_idx]
        t = times[frame_idx]

        im1.set_data(omega_sq.T)
        im2.set_data(h.T)

        # Mark firings: scatter at (Ai, Aj) — project into 2D slice
        if firings:
            xs = [fk[0] for fk in firings]
            ys = [fk[1] for fk in firings]
            fire_scatter_1.set_offsets(np.column_stack([xs, ys]))
            fire_scatter_2.set_offsets(np.column_stack([xs, ys]))
        else:
            fire_scatter_1.set_offsets(np.empty((0, 2)))
            fire_scatter_2.set_offsets(np.empty((0, 2)))

        phase_str = "DRIVE" if t < drive_end else "POST-DRIVE"
        title_text.set_text(
            f"Phase 5 pair formation (N={cfg.N}, amp={cfg.amplitude}·V_SNAP [STRESS])\n"
            f"t={t/period:.2f} T_Compton | {phase_str} | firings={len(firings)}"
        )
        return im1, im2, fire_scatter_1, fire_scatter_2, title_text

    n_frames = len(omega_sq_frames)
    anim = FuncAnimation(fig, update, frames=n_frames, interval=100, blit=False)
    plt.tight_layout()
    anim.save(out, writer="pillow", fps=10, dpi=90)
    plt.close(fig)
    print(f"Saved {out}  ({n_frames} frames)")


def make_dark_wake_gif(result: dict, out: str = "/tmp/phase5_dark_wake.gif") -> None:
    """Animation B — τ_zx shear field (BEMF dark wake)."""
    cfg = result["config"]
    period = cfg.period
    times = np.array(result["frame_times"])
    tau_frames = result["frame_tau_zx"]
    drive_end = cfg.drive_end_time

    if not tau_frames:
        print("No frames — skipping dark_wake gif.")
        return

    # Symmetric diverging colormap for signed shear
    tau_abs_max = max(np.max(np.abs(f)) for f in tau_frames) + 1e-12

    fig, ax = plt.subplots(figsize=(9, 8))
    # TwoSlopeNorm requires vmin < vcenter < vmax; if all-zero, use small epsilon
    vmin = -tau_abs_max if tau_abs_max > 1e-10 else -1e-10
    vmax = tau_abs_max if tau_abs_max > 1e-10 else 1e-10
    norm = TwoSlopeNorm(vmin=vmin, vcenter=0.0, vmax=vmax)
    im = ax.imshow(
        tau_frames[0].T, origin="lower", cmap="PuOr", norm=norm,
        aspect="equal",
    )
    ax.set_title("τ_zx shear field — back-EMF dark wake (BEMF from K4 mutual inductance)",
                 fontsize=11)
    ax.set_xlabel("x (lattice cells, propagation axis)")
    ax.set_ylabel("y (lattice cells)")
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="τ_zx (signed shear)")

    title_text = fig.text(0.5, 0.95, "", ha="center", fontsize=12)

    def update(frame_idx):
        tau = tau_frames[frame_idx]
        t = times[frame_idx]
        im.set_data(tau.T)
        phase_str = "DRIVE" if t < drive_end else "POST-DRIVE"
        title_text.set_text(
            f"Phase 5 dark wake (N={cfg.N}, amp={cfg.amplitude}·V_SNAP)\n"
            f"t={t/period:.2f} T_Compton | {phase_str} | "
            f"max |τ_zx|={np.max(np.abs(tau)):.3e}"
        )
        return im, title_text

    n_frames = len(tau_frames)
    anim = FuncAnimation(fig, update, frames=n_frames, interval=100, blit=False)
    plt.tight_layout()
    anim.save(out, writer="pillow", fps=10, dpi=90)
    plt.close(fig)
    print(f"Saved {out}  ({n_frames} frames)")


if __name__ == "__main__":
    print("── Phase 5 pair-formation animation driver ──\n")
    cfg = RunConfig()
    print(f"Config: N={cfg.N}, pml={cfg.pml}, T={cfg.temperature}")
    print(f"        λ={cfg.wavelength}, amp={cfg.amplitude}·V_SNAP (STRESS)")
    print(f"        Drive: ramp={cfg.t_ramp_periods}p, sustain={cfg.t_sustain_periods}p, "
          f"post={cfg.t_observe_post_drive_periods}p")
    print(f"        n_steps={cfg.n_outer_steps}, cadence={cfg.record_cadence} "
          f"→ ~{cfg.n_outer_steps // cfg.record_cadence} frames")
    print("(Expected runtime ~5-10 min at N=32)\n")

    result = run_collision(cfg)
    print(f"\nSim elapsed: {result['elapsed_s']:.1f} s")
    print(f"Total gate firings: {result['total_firings']}")
    print(f"Frames captured: {len(result['frame_times'])}\n")

    # Per-frame max A² for sanity
    gate_hist = result["gate_history"]
    regime_hist = result["regime_history"]
    if regime_hist:
        max_A2_ever = max(h["max_A2_total"] for h in regime_hist)
        print(f"Max A²_total achieved: {max_A2_ever:.4f}")
        print(f"  (sat_frac=0.95 for gate C1 firing)")

    print("\nRendering gifs…")
    make_pair_formation_gif(result)
    make_dark_wake_gif(result)

    if result["total_firings"] == 0:
        print("\n⚠ Gate never fired at this config.")
        print(f"  Max A² = {max_A2_ever:.3f} (needed ≥ 0.95)")
        print("  Animations still produced — will show approach to C1")
        print("  but no actual nucleation events.")
    else:
        print(f"\n✓ Gate fired {result['total_firings']} time(s).")
        print("  pair_formation gif shows the nucleation events (yellow stars).")

    print("\nArtifacts:")
    print("  /tmp/phase5_pair_formation.gif  — |ω|² + chirality + gate firings")
    print("  /tmp/phase5_dark_wake.gif       — τ_zx shear (BEMF dark wake)")
    sys.exit(0)
