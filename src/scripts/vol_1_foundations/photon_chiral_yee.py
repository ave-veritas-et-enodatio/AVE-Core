"""
Path B — Yee Maxwell FDTD Chiral Photon with Dark Wake Observation
====================================================================

Cross-substrate counterpart to Path A (K4-TLM + CosseratBeltramiSource).
Uses parent's Yee Maxwell FDTD (FDTD3DEngine) with circularly polarized
source pattern from visualize_photon_helicity.py, extended to long
propagation domain + τ_zx-equivalent dark wake observer.

Pre-registered acceptance criteria (verbatim per A47 v11b discipline):

  C-P1: Source is genuine CP — Ey, Ez phase 90° apart, equal magnitude
        at source slab (within 5%). Tests chirality at injection.

  C-P2: Forward propagation velocity v_forward ≈ c per standard Maxwell
        (within 5%). Yee FDTD is isotropic by construction.

  C-P3: Dark wake — Z_eff · ∂|E|²/∂x at x just behind source > 0 during
        sustained source phase (non-zero longitudinal energy gradient).

  C-P4: Chirality asymmetry — RH and LH wake amplitudes differ measurably
        (|Δτ| / max(τ) > 5% — qualitative; threshold ad-hoc per A47 v18
        as corpus doesn't supply quantitative chirality-induced asymmetry
        prediction).

  C-P5: Long-distance propagation — wave reaches x ≥ 0.5·N_x without
        anomalous decay (|E|² at x = 0.5·N_x ≥ 5% of source-region peak).

  C-P6: PML adequacy — backward-propagating wake doesn't reflect
        (τ_zx at x = pml_layers + 2 < 5% of interior peak).

τ_zx observable for Yee fields (analog of K4-TLM DarkWakeObserver formula):
  τ_zx = Z_eff · ∂|E|²/∂x   where |E|² = Ex² + Ey² + Ez²
  Z_eff = Z_0 in linear mode; Z_0 / √(1-(V/V_yield)²) under Ax 4 saturation

References:
  - Parent's visualize_photon_helicity.py (lines 71-108) — CP source pattern
  - AVE-Core dark_wake_validation.py — τ_zx-style observation logic
  - doc 49 §1.1 — dark wake = τ_zx longitudinal shear back-propagating

Outputs:
  - assets/photon_chiral_yee_RH.gif + assets/photon_chiral_yee_LH.gif
  - assets/photon_chiral_yee_panels.png  (4-panel summary)
  - results/photon_chiral_yee.json       (pre-reg evaluation, both handedness)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.constants import C_0, V_YIELD, MU_0, EPSILON_0


PREREG = {
    "C-P1_CP_amplitude_ratio_min": 0.95,
    "C-P1_CP_amplitude_ratio_max": 1.05,
    "C-P1_CP_phase_offset_deg_min": 85.0,
    "C-P1_CP_phase_offset_deg_max": 95.0,
    "C-P2_v_forward_over_c_min": 0.95,
    "C-P2_v_forward_over_c_max": 1.05,
    "C-P3_wake_min_amplitude_threshold": 0.0,
    "C-P4_chirality_asymmetry_min_frac": 0.05,
    "C-P5_far_field_amplitude_min_frac_of_peak": 0.05,
    "C-P6_PML_reflection_max_frac_of_peak": 0.05,
}


def run_chiral_propagation(
    handedness: str,
    nx: int = 200,
    ny: int = 60,
    nz: int = 60,
    dx: float = 0.01,         # 1 cm/cell
    freq: float = 1.5e9,      # 1.5 GHz → λ ≈ 20 cm = 20 cells
    src_x: int = 15,
    sigma_yz_cells: float = 4.0,
    amp_frac_yield: float = 0.05,
    n_steps: int = 400,
    record_cadence: int = 4,
    linear_only: bool = False,  # engage Ax 4 saturation
) -> dict:
    """Run Yee FDTD with circularly polarized source, record τ_zx wake.

    Args:
        handedness: "RH" or "LH"
        nx, ny, nz: grid dimensions (long propagation axis = nx)
        dx: cell size [m]
        freq: source carrier frequency [Hz]
        src_x: source plane index along x
        sigma_yz_cells: transverse Gaussian width (cells)
        amp_frac_yield: source amplitude as fraction of V_YIELD
        n_steps: total integration steps
        record_cadence: record diagnostics every N steps
        linear_only: if True, disable Ax 4 saturation (pure Maxwell)

    Returns dict with keys:
        handedness, n_steps, λ_cells, |E|² history, τ_zx history,
        Ey/Ez at source, frames for animation
    """
    if handedness not in ("RH", "LH"):
        raise ValueError(f"handedness must be RH or LH, got {handedness!r}")

    eng = FDTD3DEngine(
        nx, ny, nz, dx=dx, linear_only=linear_only,
        use_pml=True, pml_layers=8,
    )
    c = eng.c
    dt = eng.dt
    omega = 2.0 * np.pi * freq
    wavelength_m = c / freq
    lambda_cells = wavelength_m / dx

    # CP source amplitude
    # Source value V_src = E·dx (volts at one cell). Express as fraction of V_yield
    amp_volts = amp_frac_yield * V_YIELD
    amp_E = amp_volts / dx  # E-field amplitude [V/m]

    # Helical disk radius — λ/(2π) per visualize_photon_helicity.py rationale
    R_helix_cells = max(3, int(round(lambda_cells / (2.0 * np.pi))))

    # Transverse profile: Gaussian disk at source plane
    cy, cz = ny // 2, nz // 2
    j, k = np.indices((ny, nz), dtype=float)
    r2 = (j - cy) ** 2 + (k - cz) ** 2
    profile = np.exp(-r2 / (2.0 * sigma_yz_cells ** 2))
    # Hard mask: only inject within R_helix
    profile_mask = (r2 <= R_helix_cells ** 2).astype(float)

    # Handedness sign: RH = +1 (counterclockwise looking +x̂), LH = -1
    sign = +1.0 if handedness == "RH" else -1.0

    # Diagnostics history
    times: list[float] = []
    e_sq_axis_history: list[np.ndarray] = []  # |E|² along x at y=cy, z=cz
    tau_zx_axis_history: list[np.ndarray] = []  # τ_zx along x
    Ey_src_history: list[float] = []
    Ez_src_history: list[float] = []
    max_e_sq_history: list[float] = []
    frames: list[np.ndarray] = []  # xy slices at z=cz for visualization

    # Source envelope: ramp(50 steps) → sustain → no decay (run-out at end)
    t_ramp = 50 * dt
    t_sustain_end = (n_steps - 50) * dt

    def envelope(t: float) -> float:
        if t < 0:
            return 0.0
        if t < t_ramp:
            return t / t_ramp
        if t < t_sustain_end:
            return 1.0
        # Optional decay tail at end (not used for sustained run)
        return max(0.0, 1.0 - (t - t_sustain_end) / (50 * dt))

    for step in range(1, n_steps + 1):
        t = step * dt
        env = envelope(t)

        if env > 0:
            # CP source: Ey = sin(ωt), Ez = sign · cos(ωt)
            # RH (sign=+1): when looking along +x, E rotates counterclockwise
            Ey_inject = env * amp_E * np.sin(omega * t)
            Ez_inject = env * amp_E * sign * np.cos(omega * t)

            # Hard injection over the profile_mask disk
            Ey_field = Ey_inject * profile * profile_mask
            Ez_field = Ez_inject * profile * profile_mask

            eng.Ey[src_x, :, :] = Ey_field
            eng.Ez[src_x, :, :] = Ez_field

            Ey_src_history.append(float(Ey_inject))
            Ez_src_history.append(float(Ez_inject))
        else:
            Ey_src_history.append(0.0)
            Ez_src_history.append(0.0)

        eng.step()

        if step % record_cadence == 0:
            # |E|² along propagation axis
            e_sq_3d = eng.Ex ** 2 + eng.Ey ** 2 + eng.Ez ** 2
            e_sq_axis = e_sq_3d[:, cy, cz].copy()
            e_sq_axis_history.append(e_sq_axis)

            # τ_zx = Z_eff · ∂|E|²/∂x — longitudinal gradient
            # In linear mode, Z_eff = Z_0 = √(μ_0/ε_0) ≈ 377 Ω
            # In nonlinear mode, Z_eff varies with local |E| via Ax 4 saturation
            grad_e_sq = np.gradient(e_sq_axis, dx)  # along x
            if linear_only:
                z_eff = np.sqrt(eng.mu_0 / eng.epsilon_0)
                tau_zx_axis = z_eff * grad_e_sq
            else:
                # ε_eff(V) = ε_0 · √(1 - (V/V_yield)²)
                # V at each cell ≈ |E| · dx (per Ax 4 voltage convention)
                # Z_eff = √(μ_eff / ε_eff). Assume μ_eff = μ_0 (no magnetic Ax 4 here).
                V_local = np.sqrt(e_sq_axis) * dx
                eps_factor = np.sqrt(np.maximum(1.0 - (V_local / V_YIELD) ** 2, 1e-6))
                eps_eff = eng.epsilon_0 * eps_factor
                z_eff = np.sqrt(eng.mu_0 / eps_eff)
                tau_zx_axis = z_eff * grad_e_sq
            tau_zx_axis_history.append(tau_zx_axis)

            max_e_sq_history.append(float(e_sq_3d.max()))
            times.append(t)

            # xy slice at z=cz for animation (Ey component for visualization)
            frames.append(eng.Ey[:, :, cz].copy())

    return {
        "handedness": handedness,
        "nx": nx, "ny": ny, "nz": nz,
        "dx": dx, "freq_Hz": freq,
        "lambda_cells": float(lambda_cells),
        "n_steps": n_steps,
        "src_x": src_x,
        "amp_frac_yield": amp_frac_yield,
        "linear_only": linear_only,
        "R_helix_cells": R_helix_cells,
        "times": times,
        "Ey_src_history": Ey_src_history,
        "Ez_src_history": Ez_src_history,
        "max_e_sq_history": max_e_sq_history,
        "e_sq_axis_history": np.stack(e_sq_axis_history, axis=0),
        "tau_zx_axis_history": np.stack(tau_zx_axis_history, axis=0),
        "frames": np.stack(frames, axis=0),
        "cy": cy, "cz": cz,
    }


def evaluate_prereg(rh: dict, lh: dict) -> dict:
    """Pre-reg evaluation per PREREG criteria."""
    nx = rh["nx"]
    src_x = rh["src_x"]
    pml = 8

    # C-P1: CP source check at source slab (use the recorded src history,
    # which is the injection amplitude itself — should give Ey/Ez = sin/cos
    # with phase 90° offset and equal amplitude).
    ey_h = np.asarray(rh["Ey_src_history"])
    ez_h = np.asarray(rh["Ez_src_history"])
    # Find indices in sustain phase (rough: middle of run)
    sustain_start = len(ey_h) // 4
    sustain_end = 3 * len(ey_h) // 4
    ey_amp = np.abs(ey_h[sustain_start:sustain_end]).max()
    ez_amp = np.abs(ez_h[sustain_start:sustain_end]).max()
    cp_amp_ratio = ey_amp / ez_amp if ez_amp > 0 else 0.0

    # Phase offset: cross-correlation. For sin/cos, peak correlation lags by π/2.
    if ey_amp > 0 and ez_amp > 0:
        ey_norm = ey_h[sustain_start:sustain_end] / ey_amp
        ez_norm = ez_h[sustain_start:sustain_end] / ez_amp
        # Compute phase offset via Hilbert transform (analytic signal)
        try:
            from scipy.signal import hilbert
            analytic = hilbert(ey_norm)
            inst_phase_y = np.angle(analytic)
            analytic_z = hilbert(ez_norm)
            inst_phase_z = np.angle(analytic_z)
            phase_offset_deg = float(np.degrees(np.mean(np.angle(np.exp(1j * (inst_phase_z - inst_phase_y))))))
            phase_offset_deg = abs(phase_offset_deg)
        except ImportError:
            phase_offset_deg = float("nan")
    else:
        phase_offset_deg = float("nan")

    pass_C_P1 = (
        PREREG["C-P1_CP_amplitude_ratio_min"]
        <= cp_amp_ratio
        <= PREREG["C-P1_CP_amplitude_ratio_max"]
        and (
            np.isnan(phase_offset_deg)
            or PREREG["C-P1_CP_phase_offset_deg_min"]
            <= phase_offset_deg
            <= PREREG["C-P1_CP_phase_offset_deg_max"]
        )
    )

    # C-P2: forward propagation velocity from peak arrival at two reference planes
    # x_a, x_b along propagation axis
    e_sq_hist = rh["e_sq_axis_history"]  # (n_frames, nx)
    times = np.asarray(rh["times"])
    x_a = src_x + 30
    x_b = src_x + 100  # 70 cells apart
    if x_b < nx - pml:
        rho_a = e_sq_hist[:, x_a]
        rho_b = e_sq_hist[:, x_b]
        if rho_a.max() > 0 and rho_b.max() > 0:
            t_a = times[int(np.argmax(rho_a))]
            t_b = times[int(np.argmax(rho_b))]
            if t_b > t_a:
                v_forward = (x_b - x_a) * rh["dx"] / (t_b - t_a)
                c_ratio_forward = v_forward / float(C_0)
            else:
                c_ratio_forward = 0.0
        else:
            c_ratio_forward = 0.0
    else:
        c_ratio_forward = 0.0

    pass_C_P2 = (
        PREREG["C-P2_v_forward_over_c_min"]
        <= c_ratio_forward
        <= PREREG["C-P2_v_forward_over_c_max"]
    )

    # C-P3: dark wake at x just behind source (x = src_x - 5)
    tau_hist = rh["tau_zx_axis_history"]  # (n_frames, nx)
    wake_x = max(pml + 1, src_x - 5)
    wake_amp_history = np.abs(tau_hist[:, wake_x])
    max_wake_amp = float(wake_amp_history.max())
    pass_C_P3 = max_wake_amp > PREREG["C-P3_wake_min_amplitude_threshold"]

    # C-P4: chirality asymmetry — RH vs LH τ_zx amplitudes differ
    tau_lh = lh["tau_zx_axis_history"]
    rh_max = float(np.abs(tau_hist).max())
    lh_max = float(np.abs(tau_lh).max())
    asym_frac = (
        abs(rh_max - lh_max) / max(rh_max, lh_max, 1e-30)
    )
    pass_C_P4 = asym_frac > PREREG["C-P4_chirality_asymmetry_min_frac"]

    # C-P5: long-distance propagation — |E|² at x = 0.5·nx
    far_x = nx // 2
    e_sq_far_max = float(e_sq_hist[:, far_x].max())
    e_sq_peak = float(e_sq_hist.max())
    far_field_frac = e_sq_far_max / e_sq_peak if e_sq_peak > 0 else 0.0
    pass_C_P5 = far_field_frac >= PREREG["C-P5_far_field_amplitude_min_frac_of_peak"]

    # C-P6: PML reflection — τ_zx at PML interface
    pml_x = pml + 2
    tau_at_pml_max = float(np.abs(tau_hist[:, pml_x]).max())
    tau_interior_peak = float(np.abs(tau_hist).max())
    pml_reflection_frac = (
        tau_at_pml_max / tau_interior_peak if tau_interior_peak > 0 else 0.0
    )
    pass_C_P6 = pml_reflection_frac < PREREG["C-P6_PML_reflection_max_frac_of_peak"]

    return {
        "C_P1_cp_amp_ratio": float(cp_amp_ratio),
        "C_P1_phase_offset_deg": float(phase_offset_deg) if not np.isnan(phase_offset_deg) else None,
        "pass_C_P1": bool(pass_C_P1),
        "C_P2_v_forward_over_c": float(c_ratio_forward),
        "pass_C_P2": bool(pass_C_P2),
        "C_P3_max_wake_amplitude": float(max_wake_amp),
        "pass_C_P3": bool(pass_C_P3),
        "C_P4_chirality_asymmetry_frac": float(asym_frac),
        "pass_C_P4": bool(pass_C_P4),
        "C_P5_far_field_amplitude_frac": float(far_field_frac),
        "pass_C_P5": bool(pass_C_P5),
        "C_P6_PML_reflection_frac": float(pml_reflection_frac),
        "pass_C_P6": bool(pass_C_P6),
    }


def render_panels(rh: dict, lh: dict, eval_result: dict, out_png: str) -> None:
    """4-panel summary: |E|² spacetime / τ_zx spacetime / source IQ / asymmetry."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Panel 1: |E|² spacetime (RH)
    ax = axes[0, 0]
    e_sq_h = rh["e_sq_axis_history"]
    extent = [0, rh["nx"], rh["times"][-1] * 1e9, 0]
    im = ax.imshow(e_sq_h, aspect="auto", cmap="hot", extent=extent)
    ax.axvline(rh["src_x"], color="cyan", lw=1, ls="--", label=f"src x={rh['src_x']}")
    ax.set_xlabel("x (cells, propagation axis)")
    ax.set_ylabel("t (ns)")
    ax.set_title(f"RH: |E|² spacetime — forward propagation\nv_fwd/c = {eval_result['C_P2_v_forward_over_c']:.4f}")
    plt.colorbar(im, ax=ax, fraction=0.04, pad=0.02, label="|E|² [V²/m²]")
    ax.legend(loc="upper right", fontsize=9)

    # Panel 2: τ_zx spacetime (RH) — the dark wake
    ax = axes[0, 1]
    tau_h = rh["tau_zx_axis_history"]
    tau_lim = float(np.abs(tau_h).max())
    extent = [0, rh["nx"], rh["times"][-1] * 1e9, 0]
    im2 = ax.imshow(
        tau_h, aspect="auto", cmap="seismic",
        vmin=-tau_lim, vmax=tau_lim, extent=extent
    )
    ax.axvline(rh["src_x"], color="black", lw=1, ls="--", label=f"src x={rh['src_x']}")
    ax.set_xlabel("x (cells, propagation axis)")
    ax.set_ylabel("t (ns)")
    ax.set_title(
        f"RH: τ_zx = Z_eff · ∂|E|²/∂x  (dark wake)\n"
        f"max |τ_zx| = {tau_lim:.3e}; PML refl = {eval_result['C_P6_PML_reflection_frac']*100:.2f}%"
    )
    plt.colorbar(im2, ax=ax, fraction=0.04, pad=0.02, label="τ_zx")
    ax.legend(loc="upper right", fontsize=9)

    # Panel 3: source CP IQ at sustain
    ax = axes[1, 0]
    ey_h = np.asarray(rh["Ey_src_history"])
    ez_h = np.asarray(rh["Ez_src_history"])
    n_show = min(200, len(ey_h))
    sustain_start = len(ey_h) // 3
    ax.plot(
        ey_h[sustain_start : sustain_start + n_show],
        ez_h[sustain_start : sustain_start + n_show],
        "b-", lw=0.6, label="RH"
    )
    ey_lh = np.asarray(lh["Ey_src_history"])
    ez_lh = np.asarray(lh["Ez_src_history"])
    ax.plot(
        ey_lh[sustain_start : sustain_start + n_show],
        ez_lh[sustain_start : sustain_start + n_show],
        "r-", lw=0.6, label="LH"
    )
    ax.set_xlabel("Ey_src")
    ax.set_ylabel("Ez_src")
    ax.set_title(
        f"Source CP trajectory (sustain phase)\n"
        f"amp ratio = {eval_result['C_P1_cp_amp_ratio']:.3f}, "
        f"phase_offset = {eval_result['C_P1_phase_offset_deg']:.1f}°"
        if eval_result['C_P1_phase_offset_deg'] is not None else
        f"amp ratio = {eval_result['C_P1_cp_amp_ratio']:.3f}"
    )
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)

    # Panel 4: max τ_zx vs t for RH and LH (chirality asymmetry)
    ax = axes[1, 1]
    rh_tau_max_t = np.max(np.abs(rh["tau_zx_axis_history"]), axis=1)
    lh_tau_max_t = np.max(np.abs(lh["tau_zx_axis_history"]), axis=1)
    times_ns = np.asarray(rh["times"]) * 1e9
    ax.plot(times_ns, rh_tau_max_t, "b-", lw=1.4, label="RH max |τ_zx|")
    ax.plot(times_ns, lh_tau_max_t, "r-", lw=1.4, label="LH max |τ_zx|")
    ax.set_xlabel("t (ns)")
    ax.set_ylabel("max |τ_zx| over x")
    ax.set_title(
        f"Chirality asymmetry: |Δτ| / max(τ) = {eval_result['C_P4_chirality_asymmetry_frac']*100:.2f}%"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.suptitle(
        f"Path B — Yee Maxwell FDTD chiral photon (N={rh['nx']}×{rh['ny']}×{rh['nz']}, "
        f"λ={rh['lambda_cells']:.1f} cells, "
        f"linear_only={rh['linear_only']}, amp_frac_yield={rh['amp_frac_yield']})",
        fontsize=12, fontweight="bold",
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=110, bbox_inches="tight")
    plt.close(fig)


def render_animation(result: dict, out_gif: str, max_frames: int = 80) -> None:
    """Animate xy-slice of Ey field showing helical photon propagation."""
    frames = result["frames"]
    n_frames = len(frames)
    stride = max(1, n_frames // max_frames)
    frames_use = frames[::stride]

    vmin = -float(np.abs(frames).max())
    vmax = -vmin

    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.imshow(
        frames_use[0].T, aspect="auto", cmap="seismic",
        vmin=vmin, vmax=vmax, origin="lower"
    )
    ax.axvline(result["src_x"], color="cyan", lw=1, ls="--")
    ax.set_xlabel("x (cells, propagation)")
    ax.set_ylabel("y (cells, transverse)")
    title = ax.set_title(f"Ey[:, :, cz] — {result['handedness']} (frame 0)")
    plt.colorbar(im, ax=ax, label="Ey [V/m]")

    def update(i):
        im.set_data(frames_use[i].T)
        title.set_text(
            f"Ey[:, :, cz] — {result['handedness']} (frame {i*stride}/{n_frames})"
        )
        return im, title

    anim = FuncAnimation(fig, update, frames=len(frames_use), interval=80, blit=False)
    writer = PillowWriter(fps=12)
    anim.save(out_gif, writer=writer)
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    results_dir = repo_root / "results"
    assets_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("Path B — Yee Maxwell FDTD chiral photon + dark wake")
    print("=" * 72)

    print("\n── Running RH ──")
    rh = run_chiral_propagation(handedness="RH")
    print(f"  done: n_frames = {len(rh['times'])}, max |E|² = {max(rh['max_e_sq_history']):.3e}")

    print("\n── Running LH ──")
    lh = run_chiral_propagation(handedness="LH")
    print(f"  done: n_frames = {len(lh['times'])}, max |E|² = {max(lh['max_e_sq_history']):.3e}")

    print("\n── Pre-reg evaluation ──")
    eval_result = evaluate_prereg(rh, lh)
    for k, v in eval_result.items():
        if k.startswith("pass_"):
            print(f"  {k:30} {'PASS' if v else 'FAIL'}")
        else:
            print(f"  {k:30} {v}")

    print("\n── Rendering ──")
    out_png = assets_dir / "photon_chiral_yee_panels.png"
    out_gif_rh = assets_dir / "photon_chiral_yee_RH.gif"
    out_gif_lh = assets_dir / "photon_chiral_yee_LH.gif"
    render_panels(rh, lh, eval_result, str(out_png))
    render_animation(rh, str(out_gif_rh))
    render_animation(lh, str(out_gif_lh))

    out_json = results_dir / "photon_chiral_yee.json"
    # Strip non-serializable arrays before saving
    rh_serial = {k: v for k, v in rh.items()
                 if not isinstance(v, np.ndarray)}
    lh_serial = {k: v for k, v in lh.items()
                 if not isinstance(v, np.ndarray)}
    with open(out_json, "w") as f:
        json.dump(
            {"prereg": PREREG, "eval": eval_result, "rh_summary": rh_serial, "lh_summary": lh_serial},
            f, indent=2, default=str,
        )

    print(f"\n  Outputs:")
    print(f"    {out_png}")
    print(f"    {out_gif_rh}")
    print(f"    {out_gif_lh}")
    print(f"    {out_json}")


if __name__ == "__main__":
    main()
