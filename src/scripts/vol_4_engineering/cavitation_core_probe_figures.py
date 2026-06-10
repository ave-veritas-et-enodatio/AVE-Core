"""Figures for the cavitation-core probe (data-derived captions in the result doc).
Reads _output/cavitation_core_probe_results.json; regenerates the de-spin time series.
"""
from __future__ import annotations

import json
import os
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
from cavitation_core_probe import run_probe  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "_output")
D = json.load(open(os.path.join(OUT, "cavitation_core_probe_results.json")))
FLOOR = D["floor_rho_cav"]
RHO_FLOOR = -0.95


def fig1_timeseries():
    fig, ax = plt.subplots(figsize=(8, 5))
    for M, col in zip([0.5, 0.7, 0.8, 0.9, 1.0], ["#2c7", "#29c", "#92c", "#d72", "#c22"]):
        ts = D["C_probe"]["series"][f"M={M}"]
        ax.plot(ts["t"], ts["rho_core"], color=col, lw=1.6, label=f"M_edge={M}")
    ax.axhline(FLOOR, color="k", ls="--", lw=1.2, label=r"candidate floor $\bar\rho_{cav}=-1/\varphi=-0.618$")
    ax.axhline(RHO_FLOOR, color="grey", ls=":", lw=1.2, label=r"apparatus clip rho_floor=$-0.95$")
    ax.set_xlabel("time (natural units)"); ax.set_ylabel(r"$\bar\rho_{core}(t)$ (interior density minimum)")
    ax.set_title("Cavitation-core probe: core density vs time (reach, cross, rebound)")
    ax.legend(fontsize=8, loc="lower right"); ax.set_ylim(-1.0, 0.05); ax.grid(alpha=0.3)
    p = os.path.join(OUT, "cavprobe_fig1_rhocore_timeseries.png"); fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    return p


def fig2_gate():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, regime, title in zip(axes, ["sub_floor", "super_floor"], ["sub-floor drive (M=0.5)", "super-floor drive (M=1.0)"]):
        g = D["B_gate"][regime]
        for knob, mark in zip(["c2_floor", "rho_floor", "nu_art", "rho_diff"], ["o", "s", "^", "v"]):
            vals = [r["val"] for r in g[knob]]; dep = [r["deepest"] for r in g[knob]]
            ax.plot(range(len(vals)), dep, marker=mark, label=knob)
        ax.axhline(FLOOR, color="k", ls="--", lw=1)
        ax.axhline(RHO_FLOOR, color="grey", ls=":", lw=1)
        ax.set_title(f"Apparatus gate — {title}"); ax.set_xlabel("knob sweep index (4 values, see doc)")
        ax.set_ylabel(r"deepest $\bar\rho_{core}$"); ax.legend(fontsize=8); ax.grid(alpha=0.3)
    p = os.path.join(OUT, "cavprobe_fig2_apparatus_gate.png"); fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    return p


def fig3_drivecurve():
    rows = D["C_probe"]["rows"]
    M = [r["M_edge"] for r in rows]; dep = [r["deepest_rho_core"] for r in rows]
    clipped = [r["clip_rho_hits"] > 1000 for r in rows]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(M, dep, "-o", color="#225", lw=2, label=r"vortex deepest $\bar\rho_{core}$ (physics where unclipped)")
    for mi, di, cl in zip(M, dep, clipped):
        if cl:
            ax.plot(mi, di, "x", color="red", ms=11, mew=2)
    ax.plot([], [], "x", color="red", label="rho_floor-CLIP (apparatus)")
    # matched control + beam prior art
    for r in D["D_control"]:
        ax.plot(r["M_edge"], r["breather_deepest"], "D", color="orange")
    ax.plot([], [], "D", color="orange", label="curl-free breather (same KE) — clip-pinned")
    ax.axhline(FLOOR, color="k", ls="--", lw=1.2, label=r"candidate floor $-1/\varphi=-0.618$")
    ax.axhline(RHO_FLOOR, color="grey", ls=":", lw=1.2, label="apparatus clip $-0.95$")
    ax.axhline(-0.26, color="green", ls="-.", lw=1.2, label="prior-art beam floor $-0.26$")
    ax.set_xlabel(r"drive amplitude $M_{edge}=v_{\theta,edge}/c_0$"); ax.set_ylabel(r"deepest $\bar\rho_{core}$")
    ax.set_title("Deepest core density vs drive: crossing at M*~0.8, CLIP at M>=1.1")
    ax.legend(fontsize=8, loc="lower left"); ax.grid(alpha=0.3); ax.set_ylim(-1.0, 0.02)
    p = os.path.join(OUT, "cavprobe_fig3_drive_curve.png"); fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    return p


def fig4_hysteresis_and_energy():
    # regenerate de-spin time series for M=1.0
    res0, _ = run_probe(1.0, N=160, nsteps=3200, record_every=20, nu_art=5e-4, rho_diff=5e-4)
    ds = min(res0["deepest_step"] + 100, 2800)
    res, _ = run_probe(1.0, N=160, nsteps=3600, record_every=20, despin_at=ds, nu_art=5e-4, rho_diff=5e-4)
    ts = res["ts"]; t = np.array(ts["t"]); rc = np.array(ts["rho_core"])
    t_despin = ds * (t[1] - t[0]) / 20.0 if len(t) > 1 else 0
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))
    ax = axes[0]
    ax.plot(t, rc, color="#225", lw=1.8)
    ax.axhline(FLOOR, color="k", ls="--", lw=1, label=r"$-1/\varphi$")
    ax.axvline(t_despin, color="red", ls="-", lw=1.5, label="de-spin (kill circulation)")
    ax.set_xlabel("time"); ax.set_ylabel(r"$\bar\rho_{core}$"); ax.set_title("HYSTERESIS: de-spin -> core REFILLS (reversible)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    ax = axes[1]
    tsM = D["C_probe"]["series"]["M=0.9"]; t2 = np.array(tsM["t"]); rc2 = np.array(tsM["rho_core"])
    KE2 = np.array(tsM["KE"]); PE2 = np.array(tsM["PE"])
    ax.plot(t2, KE2, color="#c22", lw=1.6, label="KE (L-state)")
    ax.plot(t2, PE2, color="#22c", lw=1.6, label="PE (C-state)")
    ax.plot(t2, KE2 + PE2, color="k", lw=1.2, ls="--", label="KE+PE")
    ic = next((i for i, x in enumerate(rc2) if x < FLOOR), None)
    if ic: ax.axvline(t2[ic], color="green", ls=":", lw=1.5, label=r"$\bar\rho_{core}$ crosses $-1/\varphi$")
    ax.set_xlabel("time"); ax.set_ylabel("energy (natural units)")
    ax.set_title("Energy partition across crossing (M=0.9): SMOOTH, no latent release")
    ax.legend(fontsize=9); ax.grid(alpha=0.3); ax.set_xlim(0, t2[min(len(t2)-1, 60)])
    p = os.path.join(OUT, "cavprobe_fig4_hysteresis_energy.png"); fig.tight_layout(); fig.savefig(p, dpi=130); plt.close(fig)
    return p


if __name__ == "__main__":
    print(fig1_timeseries()); print(fig2_gate()); print(fig3_drivecurve()); print(fig4_hysteresis_and_energy())
