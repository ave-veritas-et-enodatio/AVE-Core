"""
REAL photon-propagation engine output — K4-TLM (scatter+connect) + FDTD Yee.
============================================================================

Purpose
-------
Produce GENUINE engine field output of a free photon (transverse wave-packet)
propagating along the vacuum, to replace the analytic illustration in
`research/figures/photon_vs_electron_cells.gif` (a hand-drawn translating
`exp(-x²)·cos(kx)` curve at a made-up speed — zero engine involvement). The
companion commit message for that figure explicitly named "real K4-TLM
scatter+connect engine output is the next step if wanted" — this IS that step.

Two canonical engines, two complementary roles (substrate-native-check)
----------------------------------------------------------------------
1. K4-TLM (`ave.core.k4_tlm.K4Lattice3D`) — the SUBSTRATE-FAITHFUL engine.
   Discrete 4-port LC junctions on the bipartite diamond lattice (Axiom 1).
   The photon is launched as the T₂ transverse port-mode via the canonical
   `PlaneSource` / `forward_port_weights` launcher in `photon_propagation.py`
   (reused, NOT re-rolled). Native observable = port-amplitude energy density
   |V_inc|² — the genuine "vacuum cells light up as the packet rides along
   them" picture. This is phase-space (port-voltage) data, not E/B.

2. FDTD Yee (`ave.core.fdtd_3d.FDTD3DEngine`, linear_only) — the CONTINUUM
   Maxwell baseline. Standard staggered Yee grid: E uses ε_eff, H uses μ_eff,
   CFL dt = 0.80·dx/(c√3). Gives the LITERAL transverse E_z and H_y fields the
   task asks for, and recovers c isotropically by construction (consistency
   check, NOT emergence: c = 1/√(μ₀ε₀) is baked into the timestep + constants).

c-recovery classification (consistency-vs-emergence)
----------------------------------------------------
Recovering c is a CONSISTENCY CHECK, not an emergence result. Both engines
have c baked in (K4: dt = dx/(c√2); FDTD: dt ∝ dx/(c√3) and the update
coefficients carry ε₀, μ₀). Reproducing c verifies the numerical scheme is
stable + non-dispersive; it does NOT derive c from anything deeper.

The K4 cardinal-axis SIGNAL speed is ≈ √2·c (anisotropic lattice kinematics:
the connect step advances one cardinal cell per step at dt = dx/(c√2)). That
anisotropy ratio (transverse vs longitudinal mode structure) is a STRUCTURAL
manifestation of the K4 elastic moduli (Axiom 1), but the absolute c is still
consistency, not emergence.

Outputs (all REAL engine field arrays, no analytic curves)
----------------------------------------------------------
  research/figures/photon_engine_real.gif        — animated multi-panel
  research/figures/photon_engine_real_strip.png  — static snapshot strip
  research/figures/photon_engine_real_results.json
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.colors as mcolors
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.core.constants import C_0, EPSILON_0, MU_0, V_SNAP
from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.k4_tlm import K4Lattice3D
from scripts.vol_1_foundations.photon_propagation import PlaneSource

C = float(C_0)
C_ANALYTIC = 1.0 / np.sqrt(float(MU_0) * float(EPSILON_0))  # = C_0 identically


# ─────────────────────────────────────────────────────────────────────
# Shared diagnostic: +x packet GROUP speed via envelope cross-correlation
# ─────────────────────────────────────────────────────────────────────
# Why cross-correlation and not centroid-fit or single-plane peak-arrival:
#   - A Gaussian-MODULATED soft source emits a multi-cycle wavetrain whose
#     spatial length (~ v·6σ_t) is comparable to the domain, so an energy
#     CENTROID over a fixed window barely drifts (underestimates v).
#   - A two-plane PEAK-ARRIVAL with the near plane close to the source is
#     biased by the source's own temporal peak (overestimates v).
#   Cross-correlating the transverse-summed intensity TIME-SERIES at two
#   planes BOTH well downstream of the source returns the envelope group
#   delay τ directly, independent of train length and source leakage.
#   v = (x_b − x_a)·dx / τ.  Sub-frame parabolic refinement on the corr peak.
def _parabolic_peak(y: np.ndarray, i: int) -> float:
    if 0 < i < len(y) - 1:
        denom = y[i - 1] - 2.0 * y[i] + y[i + 1]
        if denom != 0:
            return i + 0.5 * (y[i - 1] - y[i + 1]) / denom
    return float(i)


def measure_propagation(
    intensity: np.ndarray,
    times: np.ndarray,
    dx: float,
    x_a: int,
    x_b: int,
) -> dict:
    """
    intensity: (n_frame, nx, ny) non-negative field intensity (|V|² or E_z²).
    x_a, x_b: two interior planes downstream of the source (x_b > x_a).
    Returns group velocity v (m/s), the envelope lag (frames), and the
    temporal RMS pulse-width at each plane (dispersion diagnostic).
    """
    sa = intensity[:, x_a, :].sum(axis=1).astype(float)
    sb = intensity[:, x_b, :].sum(axis=1).astype(float)
    dt_frame = float(times[1] - times[0])
    a = sa - sa.mean()
    b = sb - sb.mean()
    if a.std() == 0 or b.std() == 0:
        return {"v_meas": 0.0, "lag_frames": 0.0, "tw_a": 0.0, "tw_b": 0.0, "tw_growth_frac": 0.0}
    corr = np.correlate(b, a, mode="full")
    k = int(np.argmax(corr))
    lag_frames = _parabolic_peak(corr, k) - (len(a) - 1)
    tau = lag_frames * dt_frame
    v = (x_b - x_a) * dx / tau if tau > 0 else 0.0

    def _temporal_rms(s: np.ndarray) -> float:
        tot = s.sum()
        if tot <= 0:
            return 0.0
        tc = float((times * s).sum() / tot)
        return float(np.sqrt(((times - tc) ** 2 * s).sum() / tot))

    tw_a, tw_b = _temporal_rms(sa), _temporal_rms(sb)
    return {
        "v_meas": float(v),
        "lag_frames": float(lag_frames),
        "tw_a": tw_a,
        "tw_b": tw_b,
        "tw_growth_frac": (tw_b - tw_a) / tw_a if tw_a > 0 else 0.0,
    }


# ─────────────────────────────────────────────────────────────────────
# K4-TLM run (substrate-faithful — reuses canonical PlaneSource launcher)
# ─────────────────────────────────────────────────────────────────────
def run_k4(
    N: int,
    pml: int,
    lambda_cells: float,
    sigma_yz: float,
    t_sigma_periods: float,
    amp_frac: float,
    source_x: int,
    n_steps: int,
    steps_per_frame: int,
) -> dict:
    lat = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    dt, dx = lat.dt, lat.dx
    omega = 2.0 * np.pi * C / (lambda_cells * dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma

    src = PlaneSource(
        x0=source_x,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0),
        sigma_yz=sigma_yz,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_frac * float(V_SNAP),
    )

    z_slice = N // 2
    rho_frames: list[np.ndarray] = [lat.get_energy_density()[:, :, z_slice].copy()]
    times: list[float] = [0.0]
    for step in range(1, n_steps + 1):
        src.apply(lat, step * dt)
        lat.step()
        if step % steps_per_frame == 0:
            rho_frames.append(lat.get_energy_density()[:, :, z_slice].copy())
            times.append(lat.timestep * dt)

    rho = np.stack(rho_frames)  # (nf, nx, ny)
    t = np.asarray(times)
    x_a, x_b = source_x + 24, source_x + 52
    m = measure_propagation(rho, t, dx, x_a, x_b)
    return {
        "engine": "K4-TLM (scatter+connect, diamond lattice, T₂ photon)",
        "field_label": r"$|V_{\rm inc}|^2$  energy density (port amplitudes)",
        "frames": rho,
        "times": t,
        "dt": dt,
        "dx": dx,
        "source_x": source_x,
        "x_a": x_a,
        "x_b": x_b,
        "v_meas": m["v_meas"],
        "v_ratio": m["v_meas"] / C,
        "lag_frames": m["lag_frames"],
        "tw_growth_frac": m["tw_growth_frac"],
        "omega": omega,
        "lambda_cells": lambda_cells,
    }


# ─────────────────────────────────────────────────────────────────────
# FDTD Yee run (continuum baseline — literal E_z, H_y; recovers c)
# ─────────────────────────────────────────────────────────────────────
def run_fdtd(
    N: int,
    pml: int,
    lambda_cells: float,
    sigma_yz: float,
    t_sigma_periods: float,
    amp_E: float,
    source_x: int,
    n_steps: int,
    steps_per_frame: int,
) -> dict:
    eng = FDTD3DEngine(N, N, N, dx=0.01, linear_only=True, use_pml=True, pml_layers=pml)
    dt, dx = eng.dt, eng.dx
    omega = 2.0 * np.pi * C / (lambda_cells * dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma

    # Transverse Gaussian apodization of the source plane (beam, not full plane).
    j, k = np.indices((N, N), dtype=float)
    yc = zc = (N - 1) / 2.0
    yz = np.exp(-((j - yc) ** 2 + (k - zc) ** 2) / (2.0 * sigma_yz**2))

    z_slice = N // 2
    Ez_frames: list[np.ndarray] = [eng.Ez[:, :, z_slice].copy()]
    Hy_frames: list[np.ndarray] = [eng.Hy[:, :, z_slice].copy()]
    times: list[float] = [0.0]
    for step in range(1, n_steps + 1):
        t_pre = step * dt
        env = np.exp(-((t_pre - t_center) ** 2) / (2.0 * t_sigma**2))
        osc = np.sin(omega * (t_pre - t_center))
        # Soft transverse-E_z source plane → linearly polarized +x packet.
        eng.Ez[source_x, :, :] += amp_E * env * osc * yz
        eng.step()
        if step % steps_per_frame == 0:
            Ez_frames.append(eng.Ez[:, :, z_slice].copy())
            Hy_frames.append(eng.Hy[:, :, z_slice].copy())
            times.append(eng.timestep * dt)

    Ez = np.stack(Ez_frames)
    Hy = np.stack(Hy_frames)
    t = np.asarray(times)
    x_a, x_b = source_x + 24, source_x + 52
    m = measure_propagation(Ez**2, t, dx, x_a, x_b)

    return {
        "engine": "FDTD Yee (continuum Maxwell, linear vacuum)",
        "field_label_E": r"$E_z$  (transverse electric field)",
        "field_label_H": r"$H_y$  (transverse magnetic field)",
        "Ez": Ez,
        "Hy": Hy,
        "times": t,
        "dt": dt,
        "dx": dx,
        "source_x": source_x,
        "x_a": x_a,
        "x_b": x_b,
        "v_meas": m["v_meas"],
        "v_ratio": m["v_meas"] / C,
        "lag_frames": m["lag_frames"],
        "omega": omega,
        "lambda_cells": lambda_cells,
        "rms_width_growth_frac": m["tw_growth_frac"],
    }


# ─────────────────────────────────────────────────────────────────────
# Visualization (REAL engine arrays only)
# ─────────────────────────────────────────────────────────────────────
def _sym_norm(arr: np.ndarray) -> mcolors.Normalize:
    a = float(np.max(np.abs(arr))) or 1.0
    return mcolors.Normalize(vmin=-a, vmax=a)


def render_gif(k4: dict, fd: dict, out_path: str) -> None:
    nf = min(len(k4["times"]), len(fd["times"]))
    Ez, Hy = fd["Ez"][:nf], fd["Hy"][:nf]
    rho = k4["frames"][:nf]

    fig, axes = plt.subplots(2, 2, figsize=(12.5, 9.0))
    fig.suptitle(
        "REAL photon-propagation engine output — transverse wave-packet in linear vacuum\n"
        "K4-TLM scatter+connect (substrate cells)  ·  FDTD Yee (continuum Maxwell E & H)",
        fontsize=12.5,
        fontweight="bold",
    )
    ax_ez, ax_hy, ax_k4, ax_ln = axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]

    norm_ez = _sym_norm(Ez)
    norm_hy = _sym_norm(Hy)
    im_ez = ax_ez.imshow(Ez[0].T, origin="lower", cmap="RdBu_r", norm=norm_ez)
    im_hy = ax_hy.imshow(Hy[0].T, origin="lower", cmap="PuOr_r", norm=norm_hy)
    rho_max = max(rho.max(), 1e-30)
    cmap_k4 = matplotlib.colormaps["inferno"].copy()
    cmap_k4.set_under("black")
    cmap_k4.set_bad("black")
    ax_k4.set_facecolor("black")
    im_k4 = ax_k4.imshow(
        rho[0].T,
        origin="lower",
        cmap=cmap_k4,
        norm=mcolors.LogNorm(vmin=max(rho_max * 1e-4, 1e-30), vmax=rho_max),
    )
    for ax, ttl in (
        (ax_ez, "FDTD Yee — $E_z$ (electric)"),
        (ax_hy, "FDTD Yee — $H_y$ (magnetic)"),
        (ax_k4, "K4-TLM — $|V_{\\rm inc}|^2$ along cells"),
    ):
        ax.set_title(ttl, fontsize=10)
        ax.set_xlabel("x (cells)")
        ax.set_ylabel("y (cells)")
        ax.axvline(fd["source_x"], color="cyan", lw=0.7, ls="--", alpha=0.5)
    plt.colorbar(im_ez, ax=ax_ez, fraction=0.046, pad=0.04)
    plt.colorbar(im_hy, ax=ax_hy, fraction=0.046, pad=0.04)
    plt.colorbar(im_k4, ax=ax_k4, fraction=0.046, pad=0.04)

    # 1D lineout: real FDTD E_z(x) at transverse center — the genuine packet
    # riding along the cells (engine analog of the analytic gif's curve).
    yc = Ez.shape[2] // 2
    ez_line0 = Ez[0, :, yc]
    xs = np.arange(Ez.shape[1])
    (ln,) = ax_ln.plot(xs, ez_line0, color="crimson", lw=1.6)
    ax_ln.set_ylim(norm_ez.vmin * 1.05, norm_ez.vmax * 1.05)
    ax_ln.set_xlim(0, Ez.shape[1] - 1)
    ax_ln.set_xlabel("x (cells)")
    ax_ln.set_ylabel("$E_z$ (engine)")
    ax_ln.axhline(0, color="0.7", lw=0.6)
    ax_ln.set_title(
        f"FDTD $E_z(x)$ lineout — REAL engine packet\n"
        f"v/c (FDTD) = {fd['v_ratio']:.3f}   ·   v/c (K4 cardinal) = {k4['v_ratio']:.3f}",
        fontsize=9.5,
    )
    ax_ln.grid(alpha=0.25)

    def update(i: int):
        im_ez.set_data(Ez[i].T)
        im_hy.set_data(Hy[i].T)
        im_k4.set_data(rho[i].T)
        ln.set_ydata(Ez[i, :, yc])
        ax_ez.set_title(f"FDTD Yee — $E_z$  (t = {fd['times'][i]*1e12:.2f} ps)", fontsize=10)
        ax_k4.set_title(f"K4-TLM — $|V_{{\\rm inc}}|^2$  (t = {k4['times'][i]*1e9:.2f} ns)", fontsize=10)
        return im_ez, im_hy, im_k4, ln

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    anim = FuncAnimation(fig, update, frames=nf, interval=1000 / 15, blit=False)
    anim.save(out_path, writer=PillowWriter(fps=15))
    plt.close(fig)


def render_strip(k4: dict, fd: dict, out_path: str) -> None:
    nf = min(len(k4["times"]), len(fd["times"]))
    cols = [int(0.30 * (nf - 1)), int(0.55 * (nf - 1)), int(0.80 * (nf - 1))]
    Ez, Hy, rho = fd["Ez"], fd["Hy"], k4["frames"]
    norm_ez, norm_hy = _sym_norm(Ez), _sym_norm(Hy)
    rho_max = max(rho.max(), 1e-30)
    lnorm = mcolors.LogNorm(vmin=max(rho_max * 1e-4, 1e-30), vmax=rho_max)
    cmap_k4 = matplotlib.colormaps["inferno"].copy()
    cmap_k4.set_under("black")
    cmap_k4.set_bad("black")

    fig, axes = plt.subplots(3, 3, figsize=(13.5, 10.5))
    fig.suptitle(
        "REAL engine snapshot strip — photon transverse wave-packet propagating (+x)\n"
        "rows: FDTD $E_z$ · FDTD $H_y$ · K4-TLM $|V_{\\rm inc}|^2$    columns: increasing time",
        fontsize=12.5,
        fontweight="bold",
    )
    for ci, fi in enumerate(cols):
        axes[0, ci].imshow(Ez[fi].T, origin="lower", cmap="RdBu_r", norm=norm_ez)
        axes[1, ci].imshow(Hy[fi].T, origin="lower", cmap="PuOr_r", norm=norm_hy)
        axes[2, ci].set_facecolor("black")
        axes[2, ci].imshow(rho[fi].T, origin="lower", cmap=cmap_k4, norm=lnorm)
        axes[0, ci].set_title(f"FDTD $E_z$   t={fd['times'][fi]*1e12:.2f} ps", fontsize=9.5)
        axes[1, ci].set_title(f"FDTD $H_y$   t={fd['times'][fi]*1e12:.2f} ps", fontsize=9.5)
        axes[2, ci].set_title(f"K4 $|V_{{\\rm inc}}|^2$   t={k4['times'][fi]*1e9:.2f} ns", fontsize=9.5)
        for r in range(3):
            axes[r, ci].set_xticks([])
            axes[r, ci].set_yticks([])
            axes[r, ci].axvline(fd["source_x"], color="cyan", lw=0.6, ls="--", alpha=0.4)
    axes[0, 0].set_ylabel("y", fontsize=9)
    axes[1, 0].set_ylabel("y", fontsize=9)
    axes[2, 0].set_ylabel("y", fontsize=9)
    fig.text(
        0.5,
        0.015,
        f"FDTD v/c = {fd['v_ratio']:.3f} (recovers c, consistency)   ·   "
        f"K4 cardinal-axis signal v/c = {k4['v_ratio']:.3f} (≈√2, anisotropic lattice kinematics)   ·   "
        f"FDTD packet RMS-width growth = {fd['rms_width_growth_frac']*100:.1f}% (numerical dispersion)",
        ha="center",
        fontsize=9.5,
        color="0.2",
    )
    plt.tight_layout(rect=[0, 0.03, 1, 0.94])
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ─────────────────────────────────────────────────────────────────────
def main() -> None:
    fig_dir = Path(__file__).resolve().parents[3] / "research" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    N, pml = 96, 8
    k4 = run_k4(
        N=N,
        pml=pml,
        lambda_cells=16.0,
        sigma_yz=10.0,
        t_sigma_periods=0.7,
        amp_frac=0.01,
        source_x=16,
        n_steps=150,
        steps_per_frame=3,
    )
    fd = run_fdtd(
        N=N,
        pml=pml,
        lambda_cells=16.0,
        sigma_yz=10.0,
        t_sigma_periods=0.7,
        amp_E=1.0,
        source_x=16,
        n_steps=300,
        steps_per_frame=6,
    )

    gif_path = fig_dir / "photon_engine_real.gif"
    strip_path = fig_dir / "photon_engine_real_strip.png"
    render_gif(k4, fd, str(gif_path))
    render_strip(k4, fd, str(strip_path))

    results = {
        "purpose": "REAL engine field output of a free photon (transverse wave-packet) — replaces analytic illustration",
        "c_analytic_mps": C_ANALYTIC,
        "c_constants_mps": C,
        "c_classification": "CONSISTENCY CHECK (c baked into dt + update coeffs; not emergence)",
        "K4_TLM": {
            "engine": k4["engine"],
            "v_meas_mps": k4["v_meas"],
            "v_ratio_to_c": k4["v_ratio"],
            "xcorr_lag_frames": k4["lag_frames"],
            "note": "cardinal-axis group speed ≈ √2·c — anisotropic diamond-lattice kinematics (connect advances 1 cardinal cell/step at dt=dx/(c√2)). Structural manifestation of K4 elastic moduli; absolute c still consistency.",
            "dt_s": k4["dt"],
            "lambda_cells": k4["lambda_cells"],
        },
        "FDTD_Yee": {
            "engine": fd["engine"],
            "v_meas_mps": fd["v_meas"],
            "v_ratio_to_c": fd["v_ratio"],
            "xcorr_lag_frames": fd["lag_frames"],
            "note": "isotropic continuum Maxwell — recovers c within Yee numerical dispersion.",
            "dt_s": fd["dt"],
            "lambda_cells": fd["lambda_cells"],
            "envelope_temporal_width_growth_frac": fd["rms_width_growth_frac"],
            "dispersion_note": "Yee numerical dispersion: forward-packet group velocity at/below c at finite points-per-wavelength; envelope temporal width grows by the reported fraction between the two downstream planes.",
        },
        "figures": {
            "gif": str(gif_path),
            "strip_png": str(strip_path),
        },
        "faithful_vs_illustrative": "ALL panels are real engine arrays (K4 V_inc energy density; FDTD E_z, H_y). No analytic curve. The only non-physical choices are visualization params (λ=16 cells, σ_yz, pulse width) — propagation, speed, and field structure are pure engine output.",
    }
    out_json = fig_dir / "photon_engine_real_results.json"
    out_json.write_text(json.dumps(results, indent=2))
    print(json.dumps({k: v for k, v in results.items() if k not in ()}, indent=2))


if __name__ == "__main__":
    main()
