#!/usr/bin/env python3
"""VISUAL 3 — "The lattice vs. the projected strain" (engine-driven video).

A 70-second MP4 that draws the 2026-08-29 picture-lock P1 with the engine's own
state. Scenes: (1) the srs lattice itself; (2) a released voltage bump, seen
tank by tank; (3) the same state smoothed for display, and (3b) a sweep of the
smoothing width; (4) the AC readout at two single tanks; (5) one tank's
(V_inc, V_ref) chart; then a provenance card.

WHAT IS ENGINE-EXACT vs DISPLAY CHOICE (full ledger: viz/README.md, Visual 3):
  ENGINE-EXACT: srs net geometry (ave.core.chiral_lattice.build_srs_net; z=3,
    right-handed I4_1 32; degree asserted); the dynamics
    (ave.core.chiral_lattice_vector.vector_tlm_step: Op5 shunt scatter
    S = (2/3)J - I plus the CONNECT permutation, optical activity OFF -- the
    kappa=0 channel acceptance test T1.1 runs); the tank voltage
    V_i = (2/3) sum_p V_inc; the per-port pair (V_inc, V_ref = S V_inc);
    the shortest-ring writhe (ring_writhe) for both enantiomorphs.
  DISPLAY CHOICES: the seed voltage bump (sigma 1.5 l_node, all ports equal); the
    Gaussian smoothing window (sigma 1.5 l_node; swept 0.4-3.5 in scene 3b);
    the drawn slab; per-step colour scaling; the 3D camera; the readout and
    chart tank placement; the radial dot subsample.

RECEIPTS, computed on every run and written to lvps_meta.json: energy drift;
the unused polarization component staying exactly 0; a wrap-around guard (every
displayed node is compared with the same run in a 32-cell box: <=1e-12 relative
through step 36, within 1e-3 through step 47, where the guard stops the run); the
readout lag (peak-to-peak and cross-correlation); the smoothing-width retention
numbers quoted in scene 3b; the seed's uniform-mode energy share.

DISCIPLINE
  * consistency-vs-emergence: a VISUALIZATION of certified engine behaviour
    (energy-conserving propagation in a closed srs box, engine acceptance suite
    L1). It asserts nothing new and tests nothing: any energy-conserving network with these
    junctions and lines draws the same movie (claim-quality.md:1382, "AC
    agreement cannot distinguish"; Hertz's razor).
  * graded captions. The picture drawn (P1) is Grant-agreed in chat,
    walk-grade, unaudited. On-frame wording passed an ave-auditor pass
    (2026-09-29): "projected strain" is the AC readout (picture-lock :27), not
    the smoothing; the node voltage is the port-sum (A1) grade and a stress
    under the impedance analogy, never labelled strain -- voltage-vs-strain at
    a node is an open question (common-mode derivation :464).
  * alpha-clean: imports only chiral_lattice{,_dynamics,_vector} (asserted below).
  * INTERNAL-REVIEW visual: on-frame text carries corpus ids (def- ids, file:line cites, Op5)
    for audit. A public cut must strip them (viz/README.md public-naming rule).

Run:
    cd src
    PYTHONPATH=. python3 scripts/viz/lattice_vs_projected_strain.py            # engine + video
    PYTHONPATH=. python3 scripts/viz/lattice_vs_projected_strain.py --stills   # + key-frame PNGs
Needs ffmpeg on PATH for the video.

Writes:
    build/viz/lattice_vs_projected_strain/lattice_vs_projected_strain.mp4 (gitignored, regenerate ~3 min)
    viz/lattice_vs_projected_strain/lvps_meta.json      (receipts; deterministic)
    viz/lattice_vs_projected_strain/lvps_*.png          (with --stills)
    build/viz/lattice_vs_projected_strain/lvps_run.npz  (engine arrays; gitignored cache)
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.collections import LineCollection  # noqa: E402
from matplotlib.patches import Circle  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Line3DCollection  # noqa: E402
from scipy.ndimage import gaussian_filter, map_coordinates  # noqa: E402

# ── repo import wiring (driver runs from src/ with PYTHONPATH=.) ──
_REPO_ROOT = Path(__file__).resolve().parents[3]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core import chiral_lattice_dynamics as cld  # noqa: E402
from ave.core import chiral_lattice_vector as clv  # noqa: E402
from ave.viz import style  # noqa: E402

for _m in (cl, cld, clv):  # alpha-clean guard: the same triad as the transverse acceptance path
    for _sym in ("ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "RHO_BULK"):
        assert _sym not in vars(_m), f"alpha-leak: {_sym} reachable in {_m.__name__}"

OUT_DIR = _REPO_ROOT / "viz" / "lattice_vs_projected_strain"
CACHE_DIR = _REPO_ROOT / "build" / "viz" / "lattice_vs_projected_strain"  # gitignored (build/)
META_NAME = "lvps_meta.json"
VIDEO_NAME = "lattice_vs_projected_strain.mp4"
VIDEO_OUT_DIR = CACHE_DIR  # Video written to gitignored build/ (repo owner decision, not tracked)


# =============================================================================
# ENGINE PASS
# =============================================================================
@dataclass(frozen=True)
class Config:
    L: int = 24  # srs cubic cells per side (N = 8 L^3 nodes)
    sig_seed: float = 1.5  # seed voltage-bump width        [l_node]  DISPLAY CHOICE
    sig_proj: float = 1.5  # smoothing-window width         [l_node]  DISPLAY CHOICE
    slab_half: float = 0.75  # half-thickness of drawn slab   [l_node]  DISPLAY CHOICE
    grid: int = 360  # smoothed-display raster (per side)       DISPLAY CHOICE
    sweep_step: int = 30  # step at which the smoothing-width sweep is shown  DISPLAY CHOICE
    sweep_lo: float = 0.4  # smoothing-width sweep range [l_node]              DISPLAY CHOICE
    sweep_hi: float = 3.5
    sweep_n: int = 60
    readout_r: tuple = (10.0, 20.0)  # target radii of the two readout tanks, along +y [l_node]
    chart_r: float = 12.0  # radius of the chart node [l_node]
    L_check: int = 32  # bigger box for the wrap-contamination receipt


def _min_image(d: np.ndarray, box: float) -> np.ndarray:
    return d - box * np.round(d / box)


def build(cfg: Config):
    net = cl.build_srs_net(cfg.L, "right")
    assert net.degree == 3 and net.carrier == "srs-z3"
    c = np.full(3, net.box / 2.0)
    d = _min_image(net.pos - c, net.box)
    return net, d


def seed_bump(d: np.ndarray, sig: float, n_ports: int = 3) -> np.ndarray:
    """All-ports-equal Gaussian voltage bump on component 0: every tank raised in voltage, zero port
    current (V_inc == V_ref at t=0), released at step 0. PRESENTATION choice.

    The bump's box mean is a uniform, stationary mode (S @ 1 = 1): it never
    leaves the closed box. Kept (not subtracted -- subtracting it breaks the
    larger-box wrap comparison); its energy share is reported as a receipt."""
    r = np.linalg.norm(d, axis=1)
    g = np.exp(-0.5 * (r / sig) ** 2)
    V = np.zeros((len(d), n_ports, 2))
    V[:, :, 0] = g[:, None]
    return V


def node_voltage(V: np.ndarray) -> np.ndarray:
    """Op5 shunt-node voltage, component 0: V_i = (2/n) sum_p V_inc[i,p]."""
    n = V.shape[1]
    return (2.0 / n) * V[:, :, 0].sum(axis=1)


def project_plane(d: np.ndarray, Vn: np.ndarray, sig: float, ext: float, ng: int) -> np.ndarray:
    """Gaussian coarse-graining of node values, evaluated on the plane x=0.

    Normalized convolution: P(y,z) = sum_i w_i V_i / sum_i w_i with
    w_i = exp(-|r - r_i|^2 / 2 sig^2). Separable: x-weight per node, then a 2D
    histogram in (y,z) blurred by the same Gaussian. Returns P[z, y] (image rows=z).
    DISPLAY CHOICE: the smoothing window -- an illustration, not a measurement."""
    x, y, z = d[:, 0], d[:, 1], d[:, 2]
    keep = np.abs(x) < 4.0 * sig
    wx = np.exp(-0.5 * (x[keep] / sig) ** 2)
    rng = [[-ext, ext], [-ext, ext]]
    H, _, _ = np.histogram2d(y[keep], z[keep], bins=ng, range=rng, weights=wx * Vn[keep])
    W, _, _ = np.histogram2d(y[keep], z[keep], bins=ng, range=rng, weights=wx)
    px = 2.0 * ext / ng
    Hs = gaussian_filter(H, sig / px, mode="wrap")
    Ws = gaussian_filter(W, sig / px, mode="wrap")
    return (Hs / np.maximum(Ws, 1e-300)).T


def sample_plane(P: np.ndarray, ext: float, pts_yz: np.ndarray) -> np.ndarray:
    """Bilinear sample of P[z, y] at (y, z) points."""
    ng = P.shape[0]
    px = 2.0 * ext / ng
    cols = (pts_yz[:, 0] + ext) / px - 0.5
    rows = (pts_yz[:, 1] + ext) / px - 0.5
    return map_coordinates(P, [rows, cols], order=1, mode="nearest")


def evolve(net, V0: np.ndarray, n_steps: int, on_step):
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    V = V0.copy()
    for k in range(n_steps + 1):
        on_step(k, V, S)
        if k < n_steps:
            V = clv.vector_tlm_step(net, V, S, conn, None)
    return V


def _key(dd: np.ndarray) -> list:
    return [tuple(v) for v in np.round(dd, 5)]


def wrap_guard_dev(cfg: Config, ext: float, n_max: int) -> np.ndarray:
    """Per-step max relative deviation between this box and the same run in the
    L_check box, over EVERY node whose voltage reaches a frame: the drawn slab,
    the radial-panel sphere (r < ext), and the smoothing input (|x| < 4 sigma,
    the kernel support in project_plane, for the widest sigma used). ENGINE receipt."""
    net_a, d_a = build(cfg)
    net_b = cl.build_srs_net(cfg.L_check, "right")
    d_b = _min_image(net_b.pos - np.full(3, net_b.box / 2.0), net_b.box)
    inplane = (np.abs(d_a[:, 1]) < ext) & (np.abs(d_a[:, 2]) < ext)
    x_half = max(cfg.slab_half, 4.0 * max(cfg.sig_proj, cfg.sweep_hi))
    win_a = ((np.abs(d_a[:, 0]) < x_half) & inplane) | (np.linalg.norm(d_a, axis=1) < ext)
    idx_b = {k: i for i, k in enumerate(_key(d_b))}
    ia = np.where(win_a)[0]
    ib = np.array([idx_b[k] for k in _key(d_a[ia])])
    Va = seed_bump(d_a, cfg.sig_seed)
    Vb = seed_bump(d_b, cfg.sig_seed)
    Sa, ca = cl.scatter_matrix(3), net_a.connect_index()
    Sb, cb = cl.scatter_matrix(3), net_b.connect_index()
    dev = []
    for k in range(n_max + 1):
        na, nb = node_voltage(Va)[ia], node_voltage(Vb)[ib]
        dev.append(np.max(np.abs(na - nb)) / max(np.max(np.abs(nb)), 1e-300))
        Va = clv.vector_tlm_step(net_a, Va, Sa, ca, None)
        Vb = clv.vector_tlm_step(net_b, Vb, Sb, cb, None)
    dev = np.array(dev)
    return dev


VISUAL_TOL = 1e-3  # 1/8 of one colour level of a 256-level map spanning +-max  DISPLAY CHOICE
EXACT_TOL = 1e-12  # engine-identical horizon (reported, not used to stop)


def horizon(dev: np.ndarray, tol: float) -> int:
    bad = np.where(dev > tol)[0]
    return int(bad[0] - 1) if len(bad) else len(dev) - 1


def run_engine(cfg: Config) -> dict:
    t0 = time.time()
    net, d = build(cfg)
    ext = net.box / 2.0
    dev = wrap_guard_dev(cfg, ext, n_max=int(1.2 * ext / cld.ANALYTIC_NETWORK_FACTOR))
    n_steps = horizon(dev, VISUAL_TOL)
    r = np.linalg.norm(d, axis=1)
    slab = np.where(np.abs(d[:, 0]) < cfg.slab_half)[0]
    # radial-scatter sample: every node within the sphere of radius ext (all of them)
    rad = np.where(r < ext)[0]
    # chart node: slab node nearest (y,z) = chart_r * (cos 45, sin 45)
    tgt = np.array([0.0, cfg.chart_r / np.sqrt(2), cfg.chart_r / np.sqrt(2)])
    chart = int(slab[np.argmin(np.linalg.norm(d[slab] - tgt, axis=1))])
    readout_targets = np.array([[pr, 0.0] for pr in cfg.readout_r])
    ro_nodes = [int(slab[np.argmin(np.hypot(d[slab, 1] - py, d[slab, 2] - pz))]) for py, pz in readout_targets]
    # rings for the projected radial profile
    rr = np.linspace(0.0, ext, 220)
    th = np.linspace(0, 2 * np.pi, 180, endpoint=False)
    ring_pts = np.stack([np.outer(rr, np.cos(th)).ravel(), np.outer(rr, np.sin(th)).ravel()], axis=1)

    rec = {k: [] for k in ("Vslab", "P", "Vrad", "ro", "chart_inc", "chart_ref", "energy", "comp1", "prof", "prof_sd")}
    receipts = {}

    def on_step(k, V, S):
        Vn = node_voltage(V)
        P = project_plane(d, Vn, cfg.sig_proj, ext, cfg.grid)
        rec["Vslab"].append(Vn[slab].astype(np.float32))
        rec["P"].append(P.astype(np.float32))
        rec["Vrad"].append(Vn[rad].astype(np.float32))
        rec["ro"].append(Vn[ro_nodes].copy())
        rec["chart_inc"].append(V[chart, :, 0].copy())
        rec["chart_ref"].append((S @ V[chart, :, 0]).copy())
        rec["energy"].append(float(np.sum(V * V)))
        rec["comp1"].append(float(np.max(np.abs(V[:, :, 1]))))
        ring = sample_plane(P, ext, ring_pts).reshape(len(rr), len(th))
        rec["prof"].append(ring.mean(axis=1))
        rec["prof_sd"].append(ring.std(axis=1))

    sweep = {}

    def on_step_all(k, V, S):
        on_step(k, V, S)
        if k == cfg.sweep_step:
            Vn = node_voltage(V)
            sig = np.linspace(cfg.sweep_lo, cfg.sweep_hi, cfg.sweep_n)
            Ps, prof, psd = [], [], []
            for sp in sig:
                P = project_plane(d, Vn, sp, ext, cfg.grid)
                ring = sample_plane(P, ext, ring_pts).reshape(len(rr), len(th))
                Ps.append(P.astype(np.float32))
                prof.append(ring.mean(axis=1))
                psd.append(ring.std(axis=1))
            sweep.update(sweep_sig=sig, sweep_P=np.array(Ps), sweep_prof=np.array(prof), sweep_sd=np.array(psd))
            # retention receipts at EXACT window widths (these numbers are quoted on frame in 3b)
            r_lobe = float(rr[int(np.argmax(prof[0]))])
            tank_ref = float(Vn[np.abs(r - r_lobe) < 0.5].mean())
            rows = []
            for sp in (cfg.sweep_lo, 1.0, 1.5, 2.0, cfg.sweep_hi):
                ring = sample_plane(project_plane(d, Vn, sp, ext, cfg.grid), ext, ring_pts)
                ring = ring.reshape(len(rr), len(th))
                pm, ps = ring.mean(axis=1), ring.std(axis=1)
                j = int(np.argmax(pm))
                rows.append(
                    {
                        "sigma_l_node": float(sp),
                        "lobe_peak_over_tank_shell_mean": float(pm[j] / tank_ref),
                        "direction_spread_rel": float(ps[j] / abs(pm[j])),
                        "lobe_r_l_node": float(rr[j]),
                    }
                )
            receipts["sweep"] = {
                "step": int(k),
                "reference": "mean voltage of all tanks with |r - r_lobe| < 0.5 l_node (3D shell); r_lobe = "
                "radius of the leading-lobe peak through the narrowest window",
                "r_lobe_l_node": r_lobe,
                "tank_shell_mean": tank_ref,
                "rows": rows,
            }

    V_seed = seed_bump(d, cfg.sig_seed)
    ubar = V_seed[:, :, 0].mean()  # projection onto the uniform (all-ports, all-nodes) mode
    uniform_frac = float(ubar**2 * V_seed[:, :, 0].size / np.sum(V_seed * V_seed))
    evolve(net, V_seed, n_steps, on_step_all)
    E = np.array(rec["energy"])
    data = {k: np.array(v) for k, v in rec.items()}
    data.update(sweep)
    data.update(
        slab_yz=d[slab][:, 1:].astype(np.float32),
        slab_idx=slab,
        rad_r=r[rad].astype(np.float32),
        chart_yz=d[chart, 1:],
        chart_node=chart,
        readout_targets_yz=readout_targets,
        ring_r=rr,
        wrap_dev=dev,
        ro_yz=d[ro_nodes, 1:],
        ro_r=r[ro_nodes],
    )
    # slab bonds (both ends in slab) for drawing
    in_slab = np.zeros(net.n_nodes, bool)
    in_slab[slab] = True
    segs = []
    for u in slab:
        for v in net.neighbors[u]:
            if v > u and in_slab[v]:
                a, b = d[u, 1:], d[v, 1:]
                if np.linalg.norm(a - b) < 1.5:  # skip min-image wrap bonds
                    segs.append([a, b])
    data["slab_bonds"] = np.array(segs, dtype=np.float32)
    # arrival receipt at the two readout tanks: leading-lobe peak + cross-correlation lag
    ro = data["ro"]
    ro_peak = [int(np.argmax(ro[:, j])) for j in range(ro.shape[1])]
    a2, b2 = ro[:, 0] - ro[:, 0].mean(), ro[:, 1] - ro[:, 1].mean()
    ro_lag_xc = int(np.argmax(np.correlate(b2, a2, mode="full")) - (len(a2) - 1))
    ro_dr = float(r[ro_nodes[1]] - r[ro_nodes[0]])
    meta = {
        "config": asdict(cfg),
        "N": net.n_nodes,
        "box_l_node": net.box,
        "ext": ext,
        "n_steps": n_steps,
        "slab_nodes": int(len(slab)),
        "radial_nodes": int(len(rad)),
        "bond_length_mean": float(cld.mean_bond_length(net)),
        "energy_drift_max": float(np.max(np.abs(E - E[0])) / E[0]),
        "comp1_max": float(np.max(data["comp1"])),
        "visual_tol": VISUAL_TOL,
        "wrap_dev_at_n_steps": float(dev[n_steps]),
        "wrap_dev_first_over_visual_tol": float(dev[n_steps + 1]) if n_steps + 1 < len(dev) else None,
        "exact_tol": EXACT_TOL,
        "exact_horizon_steps": horizon(dev, EXACT_TOL),
        "wrap_guard_window": "every displayed node: drawn slab, radial-panel sphere r < ext, smoothing input "
        "|x| < 4 max(sig_proj, sweep_hi)",
        "c_net_analytic": float(cld.ANALYTIC_NETWORK_FACTOR * cld.mean_bond_length(net)),
        "readout_nodes": ro_nodes,
        "readout_r": [float(r[i]) for i in ro_nodes],
        "readout_dr": ro_dr,
        "readout_peak_steps": ro_peak,
        "readout_xcorr_lag": ro_lag_xc,
        "uniform_mode_energy_frac": uniform_frac,
        "sweep_receipts": receipts["sweep"],
        "chart_node_yz": d[chart, 1:].tolist(),
        "chart_node_x": float(d[chart, 0]),
    }
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(CACHE_DIR / "lvps_run.npz", **data)
    (OUT_DIR / META_NAME).write_text(json.dumps(meta, indent=2) + "\n")
    print(f"engine pass: {time.time() - t0:.1f} s, {n_steps} steps, drift {meta['energy_drift_max']:.1e}")
    return meta


# =============================================================================
# RENDER PASS (presentation only; reads the engine arrays)
# =============================================================================
W, H, DPI, FPS = 1920, 1080, 100, 30
FRAMES_PER_STEP = 5
HOLD = 36

OI = {
    "blue": "#0072B2",
    "green": "#009E73",
    "orange": "#E69F00",
    "verm": "#D55E00",
    "sky": "#56B4E9",
    "purple": "#CC79A7",
}
CMAP = style.CMAP_DIV  # RdBu_r, zero-centred (house style)
GREY = "#555555"
LN = r"$\ell_{node}$"

# layout (figure fractions)
TITLE_Y, SUB_Y = 0.955, 0.915
P_BOT, P_TOP = 0.36, 0.84
P_H = P_TOP - P_BOT
P_W = P_H * H / W  # square panel width
CAP_TOP = 0.29

FOOTER = (
    "ENGINE: srs net (degree 3, chiral I4$_1$32) \u00b7 Op5 scatter\u2013connect, one polarization of the vector-TLM "
    "\u00b7 cold & linear, S(A) = 1 \u00b7 energy conserved in this closed box (drift {drift:.0e})\n"
    "SHOWN: node voltage = port-sum (all-ports-symmetric) grade; canon names it the A1 grade (common-mode sense d); "
    "no independent A1 field here.  NOT MODELED: $\\omega$ / (2,3) winding, saturation, DC prestress."
)


def load():
    d = np.load(CACHE_DIR / "lvps_run.npz")
    meta = json.loads((OUT_DIR / META_NAME).read_text())
    return d, meta


def new_fig():
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, layout="none")
    fig.patch.set_facecolor("white")
    return fig


def rgb(fig) -> bytes:
    fig.canvas.draw()
    buf = np.asarray(fig.canvas.buffer_rgba())
    assert buf.shape[0] == H and buf.shape[1] == W, buf.shape
    return buf[:, :, :3].tobytes()


def header(fig, title: str, sub: str = ""):
    fig.text(0.02, TITLE_Y, title, fontsize=26, weight="bold", ha="left", va="center")
    if sub:
        fig.text(0.02, SUB_Y, sub, fontsize=15, color=GREY, ha="left", va="center")


def footer(fig, meta):
    fig.text(
        0.02,
        0.032,
        FOOTER.format(drift=meta["energy_drift_max"]),
        fontsize=10.5,
        color=GREY,
        ha="left",
        va="center",
        linespacing=1.5,
    )


def caption(fig, lines, top=CAP_TOP, x=0.02):
    """Each caption line in black, its grade tag in small grey beneath it."""
    y = top
    for text, tag in lines:
        fig.text(x, y, text, fontsize=16, ha="left", va="top")
        y -= 0.034
        if tag:
            fig.text(x + 0.012, y, f"[{tag}]", fontsize=12, color=GREY, ha="left", va="top")
            y -= 0.030
        y -= 0.006


def step_badge(fig):
    return fig.text(0.98, TITLE_Y, "", fontsize=20, ha="right", va="center", family="monospace", color="#222222")


def panel_title(fig, ax, text):
    b = ax.get_position()
    fig.text(b.x0 + b.width / 2, P_TOP + 0.012, text, ha="center", va="bottom", fontsize=14.5, weight="bold")


# ───────────────────────────── S0 title ─────────────────────────────
def scene_title(meta):
    fig = new_fig()
    fig.text(0.5, 0.63, "The lattice vs. the projected strain", fontsize=46, weight="bold", ha="center")
    fig.text(
        0.5, 0.545, "what the lattice holds, and what an observer inside it reads", fontsize=26, color=GREY, ha="center"
    )
    fig.text(
        0.5,
        0.41,
        f"Dynamics: engine output, unedited — srs net, Op5 scatter–connect, {meta['N']:,} tanks, "
        f"{meta['n_steps']} steps.\nEvery caption carries a grade. The picture drawn is picture-lock P1 "
        "(2026-08-29): Grant-agreed in chat, walk-grade, unaudited.",
        fontsize=17,
        ha="center",
        linespacing=1.7,
    )
    fig.text(
        0.5,
        0.2,
        "INTERNAL REVIEW BUILD \u2014 corpus ids kept on frame for audit; a public cut strips them",
        fontsize=14,
        color=OI["verm"],
        ha="center",
    )
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(4.5 * FPS)):
        yield frame


# ───────────────────────────── S1 3D intro ─────────────────────────────
def _chunk():
    net = cl.build_srs_net(4, "right")
    c = np.full(3, net.box / 2.0)
    d = net.pos - c
    d -= net.box * np.round(d / net.box)
    ctr = int(np.argmin(np.linalg.norm(d, axis=1)))
    ring = cl.shortest_ring(net, ctr)
    R = 3.4
    while True:
        rel = net.pos - net.pos[ctr]
        rel -= net.box * np.round(rel / net.box)
        chunk = np.where(np.linalg.norm(rel, axis=1) < R)[0]
        if set(ring) <= set(chunk.tolist()):
            break
        R += 0.2
    inch = set(chunk.tolist())
    # star tank: off the ring, all 3 neighbours inside the chunk, nearest the centre
    cands = [u for u in chunk if u not in ring and all(v in inch for v in net.neighbors[u])]
    star_u = min(cands, key=lambda u: np.linalg.norm(rel[u]))
    segs = [[rel[u], rel[v]] for u in chunk for v in net.neighbors[u] if v > u and v in inch]
    rp = np.array([rel[u] for u in ring])
    ring_segs = [[rp[i], rp[(i + 1) % len(rp)]] for i in range(len(rp))]
    star = [[rel[star_u], rel[v]] for v in net.neighbors[star_u]]
    w = cl.ring_writhe(cl.ring_coords(net, ring))
    netL = cl.build_srs_net(4, "left")
    wL = cl.ring_writhe(cl.ring_coords(netL, cl.shortest_ring(netL, 0)))
    return rel[chunk], np.array(segs), np.array(ring_segs), np.array(star), rel[star_u], len(ring), (w, wL)


def scene_intro3d(meta):
    pts, segs, ring_segs, star, star_p, nring, wr = _chunk()
    fig = new_fig()
    header(fig, "1 · The lattice", "the graph is the space; every node is a tank")
    ax = fig.add_axes([0.01, 0.12, 0.55, 0.76], projection="3d")
    ax.set_axis_off()
    ax.add_collection3d(Line3DCollection(segs, colors="#a0a0a0", linewidths=1.6))
    ax.add_collection3d(Line3DCollection(ring_segs, colors=OI["verm"], linewidths=4.2))
    ax.add_collection3d(Line3DCollection(star, colors=OI["blue"], linewidths=6.0))
    ax.scatter(
        pts[:, 0], pts[:, 1], pts[:, 2], s=70, c="#e3e9f0", edgecolors="#4a4a4a", linewidths=0.8, depthshade=True
    )
    ax.scatter([star_p[0]], [star_p[1]], [star_p[2]], s=240, c=OI["blue"], edgecolors="black", linewidths=1.2)
    lim = np.abs(pts).max() * 0.82
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1))
    lines = [
        (f"Every node has 3 bonds, one {LN} long, coplanar at 120\u00b0 (blue).", "engine geometry"),
        (
            "Node = LC tank; per channel, a bond is modelled as a line.",
            "eq_axiom_1.tex:37 (node LC tank) \u00b7 def-b0nd01 (per-channel model)",
        ),
        (
            "The tank is the line's long-wave limit, not a second store.",
            "z0-derivation.md:129 \u00b7 this engine runs the line form",
        ),
        (f"Shortest closed loop: {nring} bonds (red), writhe {wr[0]:+.3f}.", "engine: ring_writhe"),
        (f"Mirror-image net: writhe {wr[1]:+.3f}.  The net is chiral (I4$_1$32).", "engine: left enantiomorph"),
        (
            "P1: the lattice graph IS the space.",
            "picture-lock P1 \u00b7 Grant-agreed in chat \u00b7 walk-grade \u00b7 unaudited",
        ),
    ]
    txts, y = [], 0.80
    for t, g in lines:
        txts.append([fig.text(0.575, y, t, fontsize=17, ha="left", va="top", alpha=0.0)])
        y -= 0.045
        if g:
            txts[-1].append(fig.text(0.585, y, f"[{g}]", fontsize=12.5, color=GREY, ha="left", va="top", alpha=0.0))
            y -= 0.07
    footer(fig, meta)
    n = int(11.0 * FPS)
    for i in range(n):
        ax.view_init(elev=18 + 8 * np.sin(2 * np.pi * i / n), azim=25 + 160 * i / n)
        for j, grp in enumerate(txts):
            a = float(np.clip((i - 20 - 48 * j) / 15.0, 0, 1))
            for t in grp:
                t.set_alpha(a)
        yield rgb(fig)
    plt.close(fig)


# ───────────────────────────── shared run view ─────────────────────────────
class RunView:
    def __init__(self, d, meta):
        self.meta = meta
        self.n = int(meta["n_steps"])
        self.ext = float(meta["ext"])
        self.yz, self.Vs, self.P, self.bonds = d["slab_yz"], d["Vslab"], d["P"], d["slab_bonds"]
        self.V0 = float(np.abs(self.Vs[0]).max())  # seed peak on the slab
        self.vmax = np.array([max(np.abs(v).max(), 1e-30) for v in self.Vs])
        self.rad_r, self.Vrad = d["rad_r"], d["Vrad"]
        rng = np.random.default_rng(7)  # fixed subsample (presentation)
        self.rad_sel = rng.choice(len(self.rad_r), size=min(16000, len(self.rad_r)), replace=False)
        self.ring_r, self.prof, self.prof_sd = d["ring_r"], d["prof"], d["prof_sd"]
        self.ro, self.ro_yz = d["ro"], d["ro_yz"]
        self.chart_inc, self.chart_ref = d["chart_inc"], d["chart_ref"]
        self.chart_yz, self.chart_node = d["chart_yz"], int(d["chart_node"])
        self.sw_sig, self.sw_P = d["sweep_sig"], d["sweep_P"]
        self.sw_prof, self.sw_sd = d["sweep_prof"], d["sweep_sd"]
        self.sig_p = float(meta["config"]["sig_proj"])

    def schedule(self):
        ks = [k for k in range(self.n + 1) for _ in range(FRAMES_PER_STEP)]
        return ks + [self.n] * HOLD


def lattice_axes(ax, rv, s=16):
    ax.add_collection(LineCollection(rv.bonds, colors="#d0d0d0", linewidths=0.7, zorder=1))
    sc = ax.scatter(
        rv.yz[:, 0], rv.yz[:, 1], c=rv.Vs[0] / rv.vmax[0], cmap=CMAP, vmin=-1, vmax=1, s=s, edgecolors="none", zorder=2
    )
    ax.set_xlim(-rv.ext, rv.ext)
    ax.set_ylim(-rv.ext, rv.ext)
    ax.set_aspect("equal")
    ax.set_xlabel(style.axis_label("Position", "y", LN), fontsize=13)
    ax.set_ylabel(style.axis_label("Position", "z", LN), fontsize=13)
    ax.tick_params(labelsize=11)
    return sc


def projected_axes(ax, rv, P0, ylabel=True):
    im = ax.imshow(
        P0,
        origin="lower",
        extent=[-rv.ext, rv.ext, -rv.ext, rv.ext],
        cmap=CMAP,
        vmin=-1,
        vmax=1,
        interpolation="bilinear",
    )
    ax.set_xlabel(style.axis_label("Position", "y", LN), fontsize=13)
    if ylabel:
        ax.set_ylabel(style.axis_label("Position", "z", LN), fontsize=13)
    ax.tick_params(labelsize=11)
    return im


def colour_key(fig, x, rv):
    """Static diverging key + live scale readout (colour range auto-scaled each step)."""
    cax = fig.add_axes([x, P_BOT + 0.17, 0.011, 0.26])
    cax.imshow(np.linspace(-1, 1, 256)[:, None], aspect="auto", cmap=CMAP, origin="lower", extent=[0, 1, -1, 1])
    cax.set_xticks([])
    cax.yaxis.tick_right()
    cax.set_yticks([-1, 0, 1])
    cax.set_yticklabels(["−max", "0", "+max"], fontsize=11)
    return fig.text(
        x + 0.022,
        P_BOT + 0.13,
        "",
        ha="center",
        va="top",
        fontsize=11.5,
        color=GREY,
        family="monospace",
        linespacing=1.35,
    )


def set_scale(t, rv, vmax):
    t.set_text(f"max =\n{vmax / rv.V0:.3f} V₀\n\nauto-scaled\neach step")


def radial_axes(ax, rv, with_curve):
    ax.axhline(0, color="#bbbbbb", lw=0.8, zorder=0)
    dots = ax.scatter(
        rv.rad_r[rv.rad_sel],
        rv.Vrad[0][rv.rad_sel] / rv.V0,
        s=2.5,
        alpha=0.25,
        color=OI["blue"],
        edgecolors="none",
        label=r"one dot per tank: node voltage $V_i$",
    )
    band = curve = None
    if with_curve:
        band = ax.fill_between(
            rv.ring_r,
            0 * rv.ring_r,
            0 * rv.ring_r,
            color="#777777",
            alpha=0.35,
            lw=0,
            label="smoothed display: spread over direction (\u00b11 sd)",
        )
        (curve,) = ax.plot(
            rv.ring_r, rv.prof[0] / rv.V0, color="black", lw=2.4, label="smoothed display, mean over direction"
        )
    ax.set_xlim(0, rv.ext)
    ax.set_xlabel(style.axis_label("Distance from release point", "r", LN), fontsize=13)
    ax.set_ylabel(r"Voltage / seed peak  $V/V_0$  [dimensionless]", fontsize=13)
    ax.tick_params(labelsize=11)
    leg = ax.legend(loc="lower left", bbox_to_anchor=(0.0, 1.01), fontsize=12, frameon=False, markerscale=6)
    for h in leg.legend_handles:
        if hasattr(h, "set_alpha"):
            h.set_alpha(1.0)
    return dots, band, curve


def update_radial(ax, rv, y_nodes, prof, sd, scale):
    dots, band, curve = ax._lvps
    dots.set_offsets(np.column_stack([rv.rad_r[rv.rad_sel], y_nodes[rv.rad_sel] / rv.V0]))
    ax.set_ylim(-1.2 * scale / rv.V0, 1.2 * scale / rv.V0)
    if curve is not None:
        curve.set_ydata(prof / rv.V0)
        lo, hi = (prof - sd) / rv.V0, (prof + sd) / rv.V0
        band.set_paths([np.column_stack([np.r_[rv.ring_r, rv.ring_r[::-1]], np.r_[lo, hi[::-1]]])])


# ───────────────────────────── captions (graded) ─────────────────────────────
def caps(rv):
    """On-frame captions, revised per the ave-auditor passes of 2026-09-29 and 2026-09-30 (README, Visual 3).
    Every number is read off this run; every line carries a stand-alone grade."""
    m = rv.meta
    s = rv.sig_p
    sw = m["sweep_receipts"]  # computed in the engine pass at exact widths; tracked in lvps_meta.json
    k = sw["step"]
    rows = {round(row["sigma_l_node"], 3): row for row in sw["rows"]}
    k1, s1 = rows[1.0]["lobe_peak_over_tank_shell_mean"], rows[1.0]["direction_spread_rel"]
    k2, s2 = rows[2.0]["lobe_peak_over_tank_shell_mean"], rows[2.0]["direction_spread_rel"]
    pk = m["readout_peak_steps"]
    lag_p, lag_x = pk[1] - pk[0], m["readout_xcorr_lag"]
    lo, hi = sorted((lag_p, lag_x))
    dr = m["readout_dr"]
    lag_txt = f"{lo}" if lo == hi else f"{lo}–{hi}"
    v_txt = f"{dr / lo:.2f}" if lo == hi else f"{dr / hi:.2f}–{dr / lo:.2f}"
    WALK = "Grant-agreed in chat · walk-grade · unaudited"
    return {
        "A": [
            (
                r"Each dot is one tank's node voltage $V_i$: colour = sign and size.  Under the impedance analogy "
                "a voltage is a stress.",
                "engine output · def-1mpanl (voltage ↔ stress, current ↔ velocity)",
            ),
            (
                "Strain is not a second field laid over the lattice; it is carried by the network's own voltages and currents.",
                f"picture-lock Round 3 · {WALK}",
            ),
            (
                "Open: is a node's voltage the compression itself, or the running total of compression current flowing in?",
                "open question for Grant \u00b7 common-mode derivation :464 (\u00a76a)",
            ),
        ],
        "B": [
            (
                rf"Right panel: the same tank voltages smoothed over a {s:g} {LN} window — a picture of the long-wave "
                "description.  Smoothing is a display choice.",
                "ILLUSTRATION",
            ),
            (
                "Canon's continuum field is the band-limited reconstruction of the same samples, with nothing lost; "
                "this blur does drop the short-wave part.",
                "paley-wiener-hilbert.md:12 (Whittaker–Shannon)",
            ),
            (
                "Tank values scatter widely at fixed r (dots); the smoothed field barely varies with direction (grey band).",
                "engine output, this run",
            ),
        ],
        "S": [
            (
                "How wide is the window?  Narrow: the display keeps tank-to-tank texture and the lattice's square-ish "
                "anisotropy.  Wide: round and smooth, but weaker.",
                "display choice on engine output",
            ),
            (
                rf"Here the leading lobe reads {k1:.0%} of the tanks' own shell mean through a 1 {LN} window "
                rf"(direction spread {s1:.0%}), {k2:.0%} through a 2 {LN} window ({s2:.0%}).",
                f"engine-derived, step {k} \u00b7 receipts in lvps_meta.json",
            ),
            (
                "For a pulse this short the picture depends on window width; for wavelengths much longer than the window it does not.",
                "math of the averaging kernel",
            ),
        ],
        "C": [
            (
                rf"Two ringed tanks, at r = {m['readout_r'][0]:.1f} and {m['readout_r'][1]:.1f} {LN}, each read their own "
                "voltage over time: raw tank voltages, no smoothing.",
                "engine output",
            ),
            (
                rf"What is read is a difference: lag {lag_txt} steps over {dr:.1f} {LN} → {v_txt} {LN}/step "
                rf"(long-wave $c_{{link}}/\sqrt{{3}}$ = {m['c_net_analytic']:.3f}).",
                "engine-derived \u00b7 peak-to-peak and cross-correlation",
            ),
            (
                "An observer made of the lattice reads differences; a uniform level shifts its rulers and clocks too, so goes unread.",
                "claim-quality.md:1380 (i) \u00b7 organizing principle, not a theorem (:1386)",
            ),
        ],
        "D": [
            (
                r"Phase space is a chart, not a place: the graph stays fixed while each port's $(V_{inc}, V_{ref})$ "
                "traces a path in its chart.",
                f"def-69f472 coordinate sense · P2 sentence, {WALK}",
            ),
            (
                r"Diagonals: $V_{inc}+V_{ref}$ = tank voltage (shared by all 3 ports);  $V_{inc}-V_{ref}$ = $Z_0$ × port "
                "current.",
                "engine (Op5 wave variables; the photon-port form, S9 walk :17, :70) \u00b7 port-sum sector: open",
            ),
            (
                "A passing wave draws an open path.  The (2,3) label belongs to the electron's bond-pair chart, a different "
                "one; no engine run produces it yet.",
                "def-kn0t01 · #417 under re-adjudication",
            ),
        ],
    }


# ───────────────────────────── S2 / S3 / sweep ─────────────────────────────
def pass_A(rv, C):
    fig = new_fig()
    header(
        fig,
        "2 · Every tank has its own value",
        rf"release a voltage bump at the centre and let the network run  (slab |x| < 0.75 {LN} shown)",
    )
    ax = fig.add_axes([0.055, P_BOT, P_W, P_H])
    sc = lattice_axes(ax, rv)
    key = colour_key(fig, 0.338, rv)
    ax2 = fig.add_axes([0.44, P_BOT + 0.02, 0.54, P_H - 0.09])
    ax2._lvps = radial_axes(ax2, rv, with_curve=False)
    caption(fig, C["A"])
    badge = step_badge(fig)
    footer(fig, rv.meta)
    for k in rv.schedule():
        sc.set_array(rv.Vs[k] / rv.vmax[k])
        set_scale(key, rv, rv.vmax[k])
        update_radial(ax2, rv, rv.Vrad[k], None, None, rv.vmax[k])
        badge.set_text(f"step {k:2d} / {rv.n}")
        yield rgb(fig)
    plt.close(fig)


def _two_panel(rv, title, sub):
    fig = new_fig()
    header(fig, title, sub)
    axL = fig.add_axes([0.045, P_BOT, P_W, P_H])
    axR = fig.add_axes([0.045 + P_W + 0.03, P_BOT, P_W, P_H])
    sc = lattice_axes(axL, rv)
    panel_title(fig, axL, "LATTICE STATE (each tank)")
    key = colour_key(fig, axR.get_position().x1 + 0.008, rv)
    ax2 = fig.add_axes([0.742, P_BOT + 0.02, 0.245, P_H - 0.13])
    ax2._lvps = radial_axes(ax2, rv, with_curve=True)
    return fig, axL, axR, sc, key, ax2


def pass_B(rv, C):
    fig, axL, axR, sc, key, ax2 = _two_panel(
        rv, "3 \u00b7 The long-wave picture", "the same data, smoothed for display (an illustration)"
    )
    im = projected_axes(axR, rv, rv.P[0] / rv.vmax[0], ylabel=False)
    panel_title(fig, axR, rf"SMOOTHED DISPLAY (window $\sigma$ = {rv.sig_p:g} {LN})")
    caption(fig, C["B"])
    badge = step_badge(fig)
    footer(fig, rv.meta)
    for k in rv.schedule():
        sc.set_array(rv.Vs[k] / rv.vmax[k])
        im.set_data(rv.P[k] / rv.vmax[k])
        set_scale(key, rv, rv.vmax[k])
        update_radial(ax2, rv, rv.Vrad[k], rv.prof[k], rv.prof_sd[k], rv.vmax[k])
        badge.set_text(f"step {k:2d} / {rv.n}")
        yield rgb(fig)
    plt.close(fig)


def pass_sweep(rv, C):
    k = int(rv.meta["config"]["sweep_step"])
    fig, axL, axR, sc, key, ax2 = _two_panel(
        rv, "3b \u00b7 How wide is the window?", f"hold at step {k}; change only the averaging width"
    )
    sc.set_array(rv.Vs[k] / rv.vmax[k])
    set_scale(key, rv, rv.vmax[k])
    im = projected_axes(axR, rv, rv.sw_P[0] / rv.vmax[k], ylabel=False)
    ptitle_ax = axR.get_position()
    ptitle = fig.text(
        ptitle_ax.x0 + ptitle_ax.width / 2, P_TOP + 0.012, "", ha="center", va="bottom", fontsize=14.5, weight="bold"
    )
    r_show = float(rv.ring_r[np.argmax(rv.sw_prof[0])])
    circ = Circle((0.0, -r_show), rv.sw_sig[0], fill=False, ec="black", lw=2.2, ls="--")
    axR.add_patch(circ)
    circ_lbl = axR.text(0.0, -r_show - rv.sw_sig[0] - 1.5, "", ha="center", va="top", fontsize=12)
    caption(fig, C["S"])
    badge = step_badge(fig)
    badge.set_text(f"step {k:2d} / {rv.n}")
    footer(fig, rv.meta)
    ns = len(rv.sw_sig)
    i_def = int(np.argmin(np.abs(rv.sw_sig - rv.sig_p)))
    seq = [0] * 20 + list(range(ns)) * 1 + [ns - 1] * 15
    seq += list(np.round(np.linspace(ns - 1, i_def, 40)).astype(int)) + [i_def] * 40
    for i in seq:
        im.set_data(rv.sw_P[i] / rv.vmax[k])
        circ.set_radius(rv.sw_sig[i])
        circ_lbl.set_position((0.0, -r_show - rv.sw_sig[i] - 1.2))
        circ_lbl.set_text(rf"window 1$\sigma$ = {rv.sw_sig[i]:.2f} {LN}")
        ptitle.set_text(rf"SMOOTHED (window $\sigma$ = {rv.sw_sig[i]:.2f} {LN}, same colour scale)")
        update_radial(ax2, rv, rv.Vrad[k], rv.sw_prof[i], rv.sw_sd[i], rv.vmax[k])
        yield rgb(fig)
    plt.close(fig)


# ───────────────────────────── S4 observer readout ─────────────────────────────
def pass_C(rv, C):
    m = rv.meta
    fig = new_fig()
    header(
        fig,
        "4 \u00b7 The projected strain: an AC readout",
        "P1, verbatim: \u201cObserved / \u2018projected\u2019 strain is the AC readout (and the real-space envelope "
        "S(A(r)))\u201d   [Grant-agreed in chat \u00b7 walk-grade \u00b7 unaudited]",
    )
    ax = fig.add_axes([0.055, P_BOT, P_W, P_H])
    sc = lattice_axes(ax, rv)
    cols = [OI["orange"], OI["green"]]
    names = ["near", "far"]
    for j, (py, pz) in enumerate(rv.ro_yz):
        ax.plot([py], [pz], marker="o", ms=17, mfc="none", mec=cols[j], mew=3, zorder=5)
        ax.text(
            py,
            pz + 2.9,
            names[j],
            color=cols[j],
            fontsize=14,
            weight="bold",
            ha="center",
            zorder=6,
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9),
        )
    key = colour_key(fig, 0.338, rv)
    ax2 = fig.add_axes([0.44, P_BOT + 0.02, 0.54, P_H - 0.09])
    ax2.axhline(0, color="#bbbbbb", lw=0.8)
    lines = [
        ax2.plot([], [], color=cols[j], lw=2.6, label=f"{names[j]} tank  (r = {m['readout_r'][j]:.1f} " + LN + ")")[0]
        for j in range(2)
    ]
    ax2.set_xlim(0, rv.n)
    pk = np.abs(rv.ro).max() / rv.V0
    ax2.set_ylim(-1.3 * pk, 1.3 * pk)
    ax2.set_xlabel(style.axis_label("Time", "k", "engine steps"), fontsize=13)
    ax2.set_ylabel(r"That tank's own voltage / seed peak  $V/V_0$  [dimensionless]", fontsize=13)
    ax2.tick_params(labelsize=11)
    ax2.legend(loc="lower left", bbox_to_anchor=(0.0, 1.01), ncol=2, fontsize=12, frameon=False)
    caption(fig, C["C"])
    kp = m["readout_peak_steps"]
    shown = False
    badge = step_badge(fig)
    footer(fig, rv.meta)
    for k in rv.schedule():
        sc.set_array(rv.Vs[k] / rv.vmax[k])
        set_scale(key, rv, rv.vmax[k])
        t = np.arange(k + 1)
        for j in range(2):
            lines[j].set_data(t, rv.ro[: k + 1, j] / rv.V0)
        if k >= max(kp) and not shown:
            y = 1.12 * pk
            ax2.annotate(
                "", xy=(kp[1], y), xytext=(kp[0], y), arrowprops=dict(arrowstyle="<->", color="#333333", lw=1.8)
            )
            ax2.text(
                0.5 * (kp[0] + kp[1]),
                y * 1.03,
                f"peak-to-peak lag {kp[1] - kp[0]} steps",
                ha="center",
                va="bottom",
                fontsize=12.5,
            )
            for j in range(2):
                ax2.axvline(kp[j], color=cols[j], lw=1, ls=":")
            shown = True
        badge.set_text(f"step {k:2d} / {rv.n}")
        yield rgb(fig)
    plt.close(fig)


# ───────────────────────────── S5 tank-state chart ─────────────────────────────
def pass_D(rv, C):
    net = cl.build_srs_net(rv.meta["config"]["L"], "right")  # deterministic build -> same node indices
    u = rv.chart_node
    bu = np.array(net.bond_unit[u])
    pcols = [OI["blue"], OI["verm"], OI["purple"]]
    fig = new_fig()
    header(fig, "5 · Phase space is not space", "each tank's state lives in its own chart")
    ax = fig.add_axes([0.055, P_BOT, P_W, P_H])
    sc = lattice_axes(ax, rv, s=70)
    cy, cz = rv.chart_yz
    zoom = 8.0
    ax.set_xlim(cy - zoom, cy + zoom)
    ax.set_ylim(cz - zoom, cz + zoom)
    for p in range(3):
        ax.plot([cy, cy + bu[p, 1]], [cz, cz + bu[p, 2]], color=pcols[p], lw=4.5, zorder=3, solid_capstyle="round")
    ax.plot([cy], [cz], marker="o", ms=28, mfc="none", mec="black", mew=2.5, zorder=4)
    panel_title(fig, ax, rf"zoom: the ringed tank, r = {np.hypot(cy, cz):.1f} {LN}")
    key = colour_key(fig, 0.338, rv)
    ax2 = fig.add_axes([0.46, P_BOT, P_W, P_H])
    vin, vre = rv.chart_inc / rv.V0, rv.chart_ref / rv.V0
    lim = 1.15 * max(np.abs(vin).max(), np.abs(vre).max())
    ax2.set_xlim(-lim, lim)
    ax2.set_ylim(-lim, lim)
    ax2.set_aspect("equal")
    ax2.axhline(0, color="#dddddd", lw=0.8)
    ax2.axvline(0, color="#dddddd", lw=0.8)
    sgrid = np.linspace(-lim, lim, 2)
    ax2.plot(sgrid, sgrid, ls="--", color="#999999", lw=1.2)
    ax2.plot(sgrid, -sgrid, ls="--", color="#999999", lw=1.2)
    ax2.text(0.95 * lim, 0.83 * lim, "tank-voltage\naxis", ha="right", va="top", fontsize=11, color="#666666")
    ax2.text(0.95 * lim, -0.83 * lim, "port-current\naxis", ha="right", va="bottom", fontsize=11, color="#666666")
    ax2.set_xlabel(r"Incident wave  $V_{inc}/V_0$  [dimensionless]", fontsize=13)
    ax2.set_ylabel(r"Reflected wave  $V_{ref}/V_0$  [dimensionless]", fontsize=13)
    ax2.tick_params(labelsize=11)
    panel_title(fig, ax2, r"TANK-STATE CHART  $(V_{inc}, V_{ref})$")
    trails = [ax2.plot([], [], color=pcols[p], lw=2.2, label=f"port {p + 1}")[0] for p in range(3)]
    heads = [ax2.plot([], [], "o", color=pcols[p], ms=9)[0] for p in range(3)]
    ax2.legend(
        loc="upper left",
        bbox_to_anchor=(1.03, 1.0),
        fontsize=12.5,
        frameon=False,
        title="bond colour = port",
        title_fontsize=12,
    )
    caption(fig, C["D"])
    badge = step_badge(fig)
    footer(fig, rv.meta)
    for k in rv.schedule():
        sc.set_array(rv.Vs[k] / rv.vmax[k])
        set_scale(key, rv, rv.vmax[k])
        for p in range(3):
            trails[p].set_data(vin[: k + 1, p], vre[: k + 1, p])
            heads[p].set_data([vin[k, p]], [vre[k, p]])
        badge.set_text(f"step {k:2d} / {rv.n}")
        yield rgb(fig)
    plt.close(fig)


# ───────────────────────────── S6 end card ─────────────────────────────
def scene_end(meta):
    fig = new_fig()
    header(fig, "What this is, and what it is not", "provenance ledger for every frame above")
    cfg = meta["config"]
    blocks = [
        (
            "ENGINE-EXACT",
            OI["blue"],
            [
                f"srs net (degree 3, chiral I4$_1$32): {meta['N']:,} tanks in a periodic box {meta['box_l_node']:.1f} {LN} wide;  "
                "dynamics = vector_tlm_step (Op5), optical activity OFF",
                r"tank voltage $V_i = (2/3)\,\Sigma_p V_{inc}$;  per port $(V_{inc},\ V_{ref}=S\,V_{inc})$;  "
                f"energy drift {meta['energy_drift_max']:.0e};  unused polarization stays exactly {meta['comp1_max']:.0f}",
            ],
        ),
        (
            "DISPLAY CHOICES",
            OI["orange"],
            [
                rf"seed: voltage bump $\sigma$ = {cfg['sig_seed']:g} {LN} (its box mean is a stationary uniform mode: "
                f"{meta['uniform_mode_energy_frac']:.2%} of the energy);  smoothing window $\\sigma$ = {cfg['sig_proj']:g} {LN} "
                f"(swept {cfg['sweep_lo']:g}–{cfg['sweep_hi']:g} in 3b)",
                f"slab |x| < {cfg['slab_half']:g} {LN};  colour range rescaled each step (zero = quiescent level);  3D camera;  "
                "readout / chart tank placement;  radial dot subsample",
            ],
        ),
        (
            "RECEIPTS",
            OI["green"],
            [
                f"agrees with a {cfg['L_check']}-cell box to \u22641e-12 through step {meta['exact_horizon_steps']} and within "
                f"{meta['visual_tol']:.0e} (below one colour level) through step {meta['n_steps']}, where the guard stops the run",
                "medium validity: engine acceptance suite L1 (T1.1 photon on srs); dated re-run receipt in viz/README.md",
            ],
        ),
        (
            "OPEN, SURFACED",
            OI["purple"],
            [
                "is a node's voltage the compression itself, or the running total of compression current flowing in? "
                "(common-mode derivation §6a)",
                "which physical sector the displayed port-sum channel is, inside an engine labelled transverse-only",
            ],
        ),
        (
            "NOT SHOWN",
            OI["verm"],
            [r"micro-rotation $\omega$ and the (2,3) winding;  saturation S(A) < 1;  DC prestress / gravity"],
        ),
        (
            "CAUTION",
            "#222222",
            [
                "A picture, not a test: any energy-conserving network with these junctions and lines draws the same movie.",
                "Agreement here cannot discriminate (claim-quality.md:1382; Hertz's razor, physics-lineage-map.md:534).",
            ],
        ),
    ]
    y = 0.85
    for name, col, rows in blocks:
        fig.text(0.03, y, name, fontsize=16, weight="bold", color=col, ha="left", va="top")
        for r in rows:
            fig.text(0.175, y, r, fontsize=14, ha="left", va="top")
            y -= 0.047
        y -= 0.025
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(12.0 * FPS)):
        yield frame


def scenes(d, meta):
    rv = RunView(d, meta)
    C = caps(rv)
    return [
        ("title", scene_title(meta)),
        ("intro3d", scene_intro3d(meta)),
        ("A", pass_A(rv, C)),
        ("B", pass_B(rv, C)),
        ("S", pass_sweep(rv, C)),
        ("C", pass_C(rv, C)),
        ("D", pass_D(rv, C)),
        ("end", scene_end(meta)),
    ]


# =============================================================================
# OUTPUTS
# =============================================================================
STILLS = {  # scene -> [(frame index, file name)]: the tracked quick-look renders
    "intro3d": [(329, "lvps_1_lattice.png")],
    "B": [(239, "lvps_3_lattice_vs_smoothed.png")],
    "S": [(10, "lvps_3b_narrow_window.png")],
    "C": [(275, "lvps_4_ac_readout.png")],
    "D": [(275, "lvps_5_tank_chart.png")],
}
STILL_WIDTH = 1280


def write_stills(d, meta) -> None:
    from PIL import Image

    for name, gen in scenes(d, meta):
        want = dict(STILLS.get(name, []))
        if not want:
            continue
        for i, fr in enumerate(gen):
            if i in want:
                img = Image.frombytes("RGB", (W, H), fr)
                img = img.resize((STILL_WIDTH, STILL_WIDTH * H // W), Image.LANCZOS)
                img.save(OUT_DIR / want[i], optimize=True)
            if i >= max(want):
                break
        plt.close("all")
    print("stills ->", OUT_DIR)


def encode_video(d, meta, crf: int) -> None:
    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg not found on PATH; install it or run with --no-video")
    VIDEO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = VIDEO_OUT_DIR / VIDEO_NAME
    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgb24",
        "-s",
        f"{W}x{H}",
        "-r",
        str(FPS),
        "-i",
        "-",
        "-c:v",
        "libx264",
        "-preset",
        "slow",
        "-crf",
        str(crf),
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        "-metadata",
        "title=The lattice vs. the projected strain (internal review build)",
        str(out),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = 0
    for name, gen in scenes(d, meta):
        for fr in gen:
            proc.stdin.write(fr)
            n += 1
        print(f"  scene {name}: done ({n} frames, {n / FPS:.1f} s)", flush=True)
    proc.stdin.close()
    if proc.wait() != 0:
        raise SystemExit("ffmpeg failed")
    print(f"video -> {out}  ({n} frames, {n / FPS:.1f} s)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--stills", action="store_true", help="also write the key-frame PNGs")
    ap.add_argument("--no-video", action="store_true", help="skip the MP4 encode")
    ap.add_argument("--render-only", action="store_true", help="reuse the cached engine arrays if present")
    ap.add_argument("--crf", type=int, default=25, help="x264 quality (lower = larger file); 25 = tracked MP4")
    args = ap.parse_args()
    if not (args.render_only and (CACHE_DIR / "lvps_run.npz").exists()):
        run_engine(Config())
    style.apply()
    d, meta = load()
    if args.stills:
        write_stills(d, meta)
    if not args.no_video:
        encode_video(d, meta, args.crf)


if __name__ == "__main__":
    main()
