"""
Phase C2 — photon at saturation amplitude, Axiom-4 engagement.

Side-by-side comparison:
  Top:    linear-regime photon   (amp = 0.01 · V_SNAP, Regime I passband)
  Bottom: saturation-regime     (amp = 0.30 · V_SNAP, Regime II transition)

Both lattices run with identical geometry and launcher. The difference:
  - Top uses nonlinear=False (Axiom 1 only)
  - Bottom uses nonlinear=True + op3_bond_reflection=True (Axiom 1 + 4)

The saturation photon should display:
  · self-induced impedance gradients at the packet crest (A² → 1 regions)
  · spatially-varying Op3 bond reflection → wave distortion / local trapping
  · visibly different envelope evolution than its linear counterpart

Honest scope statement
----------------------
The K4-TLM alone CANNOT form the electron soliton. Per research §32
(Phase-3b axiom-compliant redesign), node-level saturation on a
symmetric 4-port K4 junction is a *no-op* because y_total = N·y and
S_{ij} = 2y/(N·y) becomes independent of the local impedance. The
electron requires the Cosserat micropolar field (u, ω), which encodes
rotational degrees of freedom the scalar K4-TLM does not carry.

What this animation DOES show is the VACUUM-SIDE precursor: how a
high-amplitude photon begins to see its own non-trivial impedance
field via the bond-level Op3 reflection. The soliton convergence —
the photon→electron transition — requires the Cosserat channel and is
deferred to 40_modeling_roadmap.

AVE fidelity (no SM/QED leakage)
-------------------------------
  · Amplitude set in units of V_SNAP (Axiom 4 scale) — no Planck,
    no electron mass coupling, no QED constants.
  · Nonlinear mode uses the code's documented 3-regime convention:
    Regime I < √(2α)·V_SNAP, Regime II √(2α) to √3/2·V_SNAP,
    Regime III > √3/2·V_SNAP. We sit in Regime II.
  · Op3 bond reflection uses Γ = (Z_B − Z_A)/(Z_B + Z_A) with
    Z_eff = Z_0/√(1 − A²)^(1/2) per Op14.
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import colors as mcolors

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import C_0, V_SNAP

from photon_propagation import PlaneSource, xy_slice


def _run_single(
    amp_frac: float,
    nonlinear: bool,
    op3: bool,
    N: int,
    pml: int,
    lambda_cells: float,
    sigma_yz: float,
    t_sigma_periods: float,
    source_x: int,
    n_steps: int,
    steps_per_frame: int,
) -> dict:
    lattice = K4Lattice3D(
        N, N, N,
        dx=1.0,
        nonlinear=nonlinear,
        pml_thickness=pml,
        op3_bond_reflection=op3,
    )
    c = float(C_0)
    dt = lattice.dt
    omega = 2.0 * np.pi * c / (lambda_cells * lattice.dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma
    amp_volts = amp_frac * float(V_SNAP)

    src = PlaneSource(
        x0=source_x,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0),
        sigma_yz=sigma_yz,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_volts,
    )

    z_slice = N // 2
    rho_frames: list[np.ndarray] = []
    A2_frames: list[np.ndarray] = []   # local A² saturation field (z=N/2 slice)
    times: list[float] = []

    for step in range(n_steps + 1):
        if step > 0:
            t_pre = step * dt
            src.apply(lattice, t_pre)
            lattice.step()
        if step % steps_per_frame == 0:
            # |V|² energy density slice
            rho_xy = xy_slice(lattice, z_slice).copy()
            rho_frames.append(rho_xy)
            # Local A² on same slice: A = |V_inc|_total / V_SNAP
            v_tot = np.sqrt(np.sum(lattice.V_inc ** 2, axis=-1))
            A2 = (v_tot / float(V_SNAP)) ** 2
            A2_frames.append(A2[:, :, z_slice].copy())
            times.append(lattice.timestep * dt)

    return {
        "rho": np.stack(rho_frames, axis=0),
        "A2": np.stack(A2_frames, axis=0),
        "t": np.asarray(times),
        "amp_volts": amp_volts,
        "amp_frac": amp_frac,
        "nonlinear": nonlinear,
        "op3": op3,
        "dt": dt,
        "omega": omega,
        "period": period,
        "t_sigma": t_sigma,
        "t_center": t_center,
    }


def run(
    N: int = 96,
    pml: int = 8,
    lambda_cells: float = 14.0,
    sigma_yz: float = 5.0,        # tighter focus → higher local A² at crest
    t_sigma_periods: float = 1.2, # longer pulse → higher accumulated amplitude
    amp_frac_low: float = 0.01,
    # Very aggressive: amp near V_SNAP to overcome dispersion.  At the
    # source plane local A exceeds 1; we want the downstream packet
    # crest to reach A² in [0.121, 0.866] (Regime II).
    amp_frac_high: float = 0.95,
    source_x: int = 16,
    n_steps: int = 240,
    steps_per_frame: int = 3,
    out_gif: str = "/tmp/photon_saturation.gif",
    out_npz: str = "/tmp/photon_saturation.npz",
) -> dict:
    print(f"Running linear (amp_frac = {amp_frac_low})…")
    lin = _run_single(
        amp_frac=amp_frac_low, nonlinear=False, op3=False,
        N=N, pml=pml, lambda_cells=lambda_cells, sigma_yz=sigma_yz,
        t_sigma_periods=t_sigma_periods, source_x=source_x,
        n_steps=n_steps, steps_per_frame=steps_per_frame,
    )
    print(f"Running saturation (amp_frac = {amp_frac_high}, nonlinear+op3 ON)…")
    sat = _run_single(
        amp_frac=amp_frac_high, nonlinear=True, op3=True,
        N=N, pml=pml, lambda_cells=lambda_cells, sigma_yz=sigma_yz,
        t_sigma_periods=t_sigma_periods, source_x=source_x,
        n_steps=n_steps, steps_per_frame=steps_per_frame,
    )

    np.savez(out_npz,
             rho_lin=lin["rho"], rho_sat=sat["rho"],
             A2_lin=lin["A2"], A2_sat=sat["A2"],
             t=lin["t"], amp_lin=lin["amp_volts"], amp_sat=sat["amp_volts"])

    _render(lin, sat, N, pml, source_x, amp_frac_low, amp_frac_high, out_gif)

    return {
        "n_frames": len(lin["t"]),
        "amp_lin": lin["amp_volts"],
        "amp_sat": sat["amp_volts"],
        "max_A2_lin": float(lin["A2"].max()),
        "max_A2_sat": float(sat["A2"].max()),
        "total_time_s": float(lin["t"][-1]),
    }


def _render(
    lin: dict, sat: dict, N: int, pml: int, source_x: int,
    amp_frac_low: float, amp_frac_high: float, out_path: str,
) -> None:
    fig = plt.figure(figsize=(13, 9))
    fig.patch.set_facecolor("#111")
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.25)
    ax_lin = fig.add_subplot(gs[0, 0])
    ax_sat = fig.add_subplot(gs[0, 1])
    ax_A2 = fig.add_subplot(gs[1, 0])
    ax_prof = fig.add_subplot(gs[1, 1])

    for ax in (ax_lin, ax_sat, ax_A2, ax_prof):
        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="#ccc")
        for spine in ax.spines.values():
            spine.set_edgecolor("#666")

    # Per-panel normalization so both linear (weak) and saturated (strong)
    # are separately readable. Comparison is of STRUCTURE not amplitude.
    vmax_lin = max(lin["rho"].max(), 1e-30)
    vmin_lin = max(vmax_lin * 1e-4, 1e-30)
    vmax_sat = max(sat["rho"].max(), 1e-30)
    vmin_sat = max(vmax_sat * 1e-4, 1e-30)
    im_lin = ax_lin.imshow(
        lin["rho"][0].T, origin="lower", cmap="inferno",
        norm=mcolors.LogNorm(vmin=vmin_lin, vmax=vmax_lin),
    )
    im_sat = ax_sat.imshow(
        sat["rho"][0].T, origin="lower", cmap="inferno",
        norm=mcolors.LogNorm(vmin=vmin_sat, vmax=vmax_sat),
    )
    ax_lin.axvline(source_x, color="cyan", ls="--", lw=0.6, alpha=0.6)
    ax_sat.axvline(source_x, color="cyan", ls="--", lw=0.6, alpha=0.6)
    ax_lin.set_title(
        f"LINEAR   amp = {amp_frac_low:.2f}·V_SNAP   (Regime I)",
        color="#eee", fontsize=10,
    )
    ax_sat.set_title(
        f"SATURATED   amp = {amp_frac_high:.2f}·V_SNAP   (Regime II)",
        color="#f90", fontsize=10,
    )
    for ax in (ax_lin, ax_sat):
        ax.set_xlabel("x (cells)", color="#ccc")
        ax.set_ylabel("y (cells)", color="#ccc")

    # A² field for the saturation case (linear scale, 0 to 1.2)
    vmax_A2 = max(sat["A2"].max() * 1.1, 0.15)
    im_A2 = ax_A2.imshow(
        sat["A2"][0].T, origin="lower", cmap="viridis",
        vmin=0, vmax=vmax_A2,
    )
    ax_A2.axvline(source_x, color="cyan", ls="--", lw=0.6, alpha=0.6)
    ax_A2.set_title(
        "Saturation amplitude A² = |V_inc|²/V_SNAP²\n"
        "(A²→1 = Axiom 4 rupture)",
        color="#eee", fontsize=9,
    )
    ax_A2.set_xlabel("x (cells)", color="#ccc")
    ax_A2.set_ylabel("y (cells)", color="#ccc")

    # Profile panel: x-marginal of |V|² for both
    x_axis = np.arange(N)
    ax_prof.set_yscale("log")
    # compute x profiles
    prof_lin = lin["rho"].sum(axis=2)     # (frames, x)
    prof_sat = sat["rho"].sum(axis=2)
    ax_prof.set_ylim(max(prof_lin.max(), prof_sat.max()) * 1e-4,
                     max(prof_lin.max(), prof_sat.max()) * 2)
    ax_prof.set_xlim(0, N)
    ax_prof.axvline(source_x, color="cyan", ls="--", lw=0.6, alpha=0.6)
    ax_prof.axvspan(0, pml, color="#444", alpha=0.3)
    ax_prof.axvspan(N - pml, N, color="#444", alpha=0.3)
    (line_lin,) = ax_prof.plot(
        x_axis, prof_lin[0], color="#7af", lw=1.4, label="linear"
    )
    (line_sat,) = ax_prof.plot(
        x_axis, prof_sat[0], color="#f90", lw=1.4, label="saturated"
    )
    ax_prof.legend(loc="upper right", fontsize=9)
    ax_prof.set_xlabel("x (cells)", color="#ccc")
    ax_prof.set_ylabel("Σ|V|² (z=N/2 slice)", color="#ccc")
    ax_prof.set_title("x-marginal packet profile", color="#eee", fontsize=10)
    ax_prof.grid(alpha=0.2, color="#666")

    # Suptitle
    suptitle = fig.suptitle(
        "", color="#eee", fontsize=13,
    )

    def update(i):
        im_lin.set_data(lin["rho"][i].T)
        im_sat.set_data(sat["rho"][i].T)
        im_A2.set_data(sat["A2"][i].T)
        line_lin.set_ydata(prof_lin[i])
        line_sat.set_ydata(prof_sat[i])
        t_ns = lin["t"][i] * 1e9
        max_A2 = sat["A2"][i].max()
        suptitle.set_text(
            f"Phase C2 — photon in linear vs saturation regime    "
            f"t = {t_ns:6.1f} ns    max A² (sat) = {max_A2:.3f}"
        )
        return im_lin, im_sat, im_A2, line_lin, line_sat, suptitle

    anim = FuncAnimation(fig, update, frames=len(lin["t"]),
                         interval=100, blit=False)
    writer = PillowWriter(fps=10)
    anim.save(out_path, writer=writer, savefig_kwargs={"facecolor": "#111"})
    plt.close(fig)


if __name__ == "__main__":
    import json
    summary = run()
    print(json.dumps(summary, indent=2))
    print(f"\nAnimation: /tmp/photon_saturation.gif")
    print(f"  max A² linear   = {summary['max_A2_lin']:.3e}")
    print(f"  max A² saturated = {summary['max_A2_sat']:.3e}")
    thresh = np.sqrt(2.0 * (1 / 137.036))    # √(2α), Regime I edge
    print(f"  Regime thresholds: √(2α) = {thresh:.3f},  √3/2 = {np.sqrt(3)/2:.3f}")
    if summary["max_A2_sat"] > thresh:
        print(f"  ✓ Saturation run IS in Regime II (A² > √(2α) = {thresh:.3f})")
    else:
        print(f"  ⚠ Saturation run stayed in Regime I — bump amp_frac_high")
