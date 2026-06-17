"""Shared visual-debug layer for the L0-L1 engine-acceptance suite.

INSTRUMENTATION ONLY — additive on top of the functional acceptance suite. These
helpers DO NOT change any pass/fail logic or bin; they record observables off the
SAME engine stepper (`chiral_lattice_vector.vector_tlm_step` /
`chiral_lattice.scalar_tlm_step`) the tests already run, then render a consistent
debug-figure set so Grant can eyeball each test.

The standard debug-figure set (per the 2026-06-16 viz brief):
  * x-t spacetime heatmap — propagation-axis position (x, here the srs z-axis)
    horizontal, timestep vertical, field energy density as color. A lossless
    constant-speed photon = a clean straight diagonal band; dispersion broadens
    it; loss fades it; reflection bends it.
  * filmstrip — the 1D field profile (energy vs position) at t=0,1/4,1/2,3/4,T.
  * energy-vs-time — total energy vs step, annotated with max relative drift.
  * per-test extras (dispersion omega(k), causal-cone slope) bolted on by the
    caller via the returned axes / dedicated panel helpers.

FIGURE EMISSION is OFF for the normal `pytest` run and ON when the suite is run
as the figure-regeneration script (`python -m tests.engine_acceptance.regen` —
see __init__.py) or when env KF_VIZ=1 is set. `viz_enabled()` gates every test's
figure call so the physics path is untouched when viz is off.

substrate-native-check / A46: every recorded quantity (energy density per z-plane,
total energy, front position) is a real-space / spectral observable read off the
DYNAMICALLY-evolved field — the same coordinates the L0-L1 corpus claims live in.
No phase-space substitution. The stepper called here is byte-identical to the one
the functional test runs; the figure is a passive recorder.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv

# matplotlib is import-gated so a viz-off pytest run never pays for it and never
# fails if a headless box lacks a display (Agg backend forced when we do import).
_MPL = None


def _mpl():
    global _MPL
    if _MPL is None:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        _MPL = plt
    return _MPL


# ── output location + gating ─────────────────────────────────────────────────
FIG_DIR = (
    Path(__file__).resolve().parents[3] / "research" / "figures" / "engine_acceptance"
)


def viz_enabled() -> bool:
    """Figures emit when KF_VIZ is truthy (the regen entrypoint sets it)."""
    return os.environ.get("KF_VIZ", "0") not in ("", "0", "false", "False")


def _fig_path(test_id: str) -> Path:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    return FIG_DIR / f"{test_id}_debug.png"


# ── recorders (reuse the engine stepper — no physics rebuild) ────────────────
def record_axis_profile(
    net: cl.LatticeNet,
    V0: np.ndarray,
    n_steps: int,
    *,
    axis: int = 2,
    chiral_rotation: bool = False,
    every: int = 1,
):
    """Step the field and record the 1D energy-density profile along `axis`.

    Bins nodes by their (discrete) axis coordinate into the lattice's natural
    z-planes and sums per-node energy into each plane every `every` steps. Returns
    a dict with the spacetime array and the per-step total energy. Calls the
    IDENTICAL `clv.vector_tlm_step` the functional test runs — this is a passive
    recorder, not a re-simulation.
    """
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    rot = clv._optical_activity_per_node(net) if chiral_rotation else None

    coord = net.pos[:, axis]
    # the srs lattice sits on a small number of discrete axis-planes; use them
    planes = np.unique(np.round(coord, 6))
    plane_idx = np.searchsorted(planes, np.round(coord, 6))

    def profile(V):
        e = np.sum(V * V, axis=(1, 2))
        prof = np.zeros(len(planes))
        np.add.at(prof, plane_idx, e)
        return prof

    V = V0.copy()
    times = [0]
    spacetime = [profile(V)]
    energy = [clv.vector_energy(V)]
    for t in range(1, n_steps + 1):
        V = clv.vector_tlm_step(net, V, S, conn, rot)
        if t % every == 0 or t == n_steps:
            spacetime.append(profile(V))
            times.append(t)
        energy.append(clv.vector_energy(V))
    return {
        "planes": planes,
        "spacetime": np.array(spacetime),  # (n_recorded, n_planes)
        "times": np.array(times),          # recorded timesteps
        "energy": np.array(energy),        # total energy EVERY step
        "axis": axis,
    }


def record_crosspol(
    net: cl.LatticeNet, V0: np.ndarray, n_steps: int, *, chiral_rotation: bool = False
):
    """Per-step total energy in pol-0 vs pol-1 (the cross-pol leak trace)."""
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    rot = clv._optical_activity_per_node(net) if chiral_rotation else None
    V = V0.copy()
    e0 = [float(np.sum(V[..., 0] ** 2))]
    e1 = [float(np.sum(V[..., 1] ** 2))]
    for _ in range(n_steps):
        V = clv.vector_tlm_step(net, V, S, conn, rot)
        e0.append(float(np.sum(V[..., 0] ** 2)))
        e1.append(float(np.sum(V[..., 1] ** 2)))
    return np.array(e0), np.array(e1)


def record_scalar_energy(net: cl.LatticeNet, V0: np.ndarray, n_steps: int):
    """Scalar-TLM total-energy trace (for L0 tests) using `cl.scalar_tlm_step`."""
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    V = V0.copy()
    energy = [cl.lattice_energy(V)]
    for _ in range(n_steps):
        V = cl.scalar_tlm_step(net, V, S, conn)
        energy.append(cl.lattice_energy(V))
    return np.array(energy)


# ── panel primitives (consistent format across all tests) ────────────────────
def _panel_spacetime(ax, rec, *, axis_label="z", front=None):
    st = rec["spacetime"]
    planes = rec["planes"]
    times = rec["times"]
    im = ax.imshow(
        st,
        origin="lower",
        aspect="auto",
        extent=[planes.min(), planes.max(), times.min(), times.max()],
        cmap="magma",
    )
    ax.set_xlabel(f"{axis_label} (propagation axis, cartesian)")
    ax.set_ylabel("timestep")
    ax.set_title("x-t spacetime: energy density (color)")
    cb = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label("|V|^2 per plane")
    if front is not None:
        ax.plot(front["z"], front["t"], color="cyan", lw=1.4, ls="--",
                label=front.get("label", "info front"))
        ax.legend(loc="upper left", fontsize=7, framealpha=0.5)
    return im


def _panel_filmstrip(ax, rec, *, axis_label="z"):
    st = rec["spacetime"]
    planes = rec["planes"]
    times = rec["times"]
    n = len(times) - 1
    fracs = [0.0, 0.25, 0.5, 0.75, 1.0]
    for f in fracs:
        i = int(round(f * n))
        ax.plot(planes, st[i], lw=1.3, label=f"t={times[i]}")
    ax.set_xlabel(f"{axis_label} (cartesian)")
    ax.set_ylabel("|V|^2 per plane")
    ax.set_title("filmstrip: waveform shape at t=0,1/4,1/2,3/4,T")
    ax.legend(fontsize=7, ncol=2)


def _panel_energy(ax, energy, *, drift_floor_label=None):
    e0 = energy[0]
    rel = np.abs(energy - e0) / abs(e0)
    max_drift = float(rel.max())
    ax.plot(np.arange(len(energy)), energy, color="#1f77b4", lw=1.0)
    ax.set_xlabel("timestep")
    ax.set_ylabel("total energy H = sum |V|^2", color="#1f77b4")
    ax.set_title("energy conservation")
    ax2 = ax.twinx()
    ax2.plot(np.arange(len(rel)), np.maximum(rel, 1e-18), color="#d62728", lw=0.8)
    ax2.set_yscale("log")
    ax2.set_ylabel("relative drift |H-H0|/H0 (log)", color="#d62728")
    note = f"max rel. drift = {max_drift:.3e}"
    if drift_floor_label:
        note += f"\n{drift_floor_label}"
    ax.annotate(
        note,
        xy=(0.5, 0.04),
        xycoords="axes fraction",
        ha="center",
        fontsize=8,
        bbox=dict(boxstyle="round", fc="#ffe9b3", ec="#caa24a", alpha=0.9),
    )
    return max_drift


# ── the standard 3-panel figure used by every propagation test ───────────────
def save_propagation_figure(
    test_id: str,
    title: str,
    rec: dict,
    *,
    axis_label="z",
    front=None,
    drift_floor_label=None,
    extra=None,
):
    """Render + save the standard {spacetime, filmstrip, energy} debug figure.

    `extra` (optional callable(ax)) draws a 4th per-test panel (e.g. T1.2's
    omega(k) dispersion curve). Returns the saved path.
    """
    plt = _mpl()
    ncols = 4 if extra is not None else 3
    fig, axes = plt.subplots(1, ncols, figsize=(5.2 * ncols, 4.6))
    fig.suptitle(f"{test_id} — {title}", fontsize=12, y=1.02)
    _panel_spacetime(axes[0], rec, axis_label=axis_label, front=front)
    _panel_filmstrip(axes[1], rec, axis_label=axis_label)
    _panel_energy(axes[2], rec["energy"], drift_floor_label=drift_floor_label)
    if extra is not None:
        extra(axes[3])
    fig.tight_layout()
    path = _fig_path(test_id)
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    return path


def localized_envelope(net: cl.LatticeNet, V0: np.ndarray, *, axis=2, width_frac=0.08):
    """Multiply a seed by a Gaussian envelope (centred on the interior median).

    SUPERSEDED 2026-06-17 by `_medium.oneway_packet`: localizing the OLD
    `directional_packet` (a delocalized cos(k·z) Bloch wave) with this envelope
    still leaves the equal ±k counter-propagating content underneath, so the
    localized companion DISPERSED bidirectionally rather than translating one-way.
    The hardened T1.1 seed instead suppresses the counter-propagating partner at
    SEED time (single-sign port occupancy in `oneway_packet`), giving a genuine
    one-way translating diagonal. Retained for callers that want a quick envelope
    multiply; not used by the hardened T1.1 path.
    """
    coord = net.pos[:, axis]
    z0 = float(np.median(coord[net.interior_mask]))
    env = np.exp(-0.5 * ((coord - z0) / (width_frac * net.box)) ** 2)
    return V0 * env[:, None, None]


def save_t1_1_flagship_figure(
    test_id: str,
    rec_oneway: dict,
    rec_bloch: dict,
    *,
    centroid=None,
    speed=None,
    c_net=None,
    r2=None,
    drift_floor_label=None,
):
    """The flagship T1.1 composite: TWO rows on the SAME medium / stepper.

    HARDENED 2026-06-17 — row 1 is now the ACTUAL hardened test seed.

      row 1 — the HARDENED one-way localized packet (`M.oneway_packet`, what the
              pass/fail test now asserts on): the x-t view is a SINGLE clean
              diagonal photon-path band translating at constant speed, with the
              measured energy-centroid line overlaid (slope = c_net), the
              filmstrip of the translating envelope, and the energy trace.
      row 2 — the OLD delocalized directional Bloch seed (the standing fringe it
              replaced): kept as the side-by-side contrast so the fix is visible.

    Energy conservation is annotated on row 1 (the test's seed). Returns the path.
    """
    plt = _mpl()
    fig, axes = plt.subplots(2, 3, figsize=(16.0, 9.4))
    sub = "photon PROPAGATION (lossless, kappa=0): HARDENED one-way packet (top) vs OLD Bloch fringe (bottom)"
    fig.suptitle(f"{test_id} — {sub}", fontsize=12, y=1.005)

    # row 1 — hardened one-way packet (the clean diagonal photon-path band)
    _panel_spacetime(axes[0, 0], rec_oneway)
    ttl = "x-t: HARDENED one-way packet — SINGLE clean diagonal"
    if speed is not None and c_net is not None:
        ttl += f"\nspeed {speed:+.4f} ≈ c_net {c_net:.4f}"
        if r2 is not None:
            ttl += f"  (R²={r2:.4f})"
    axes[0, 0].set_title(ttl, fontsize=10)
    # overlay the measured energy-centroid line (the propagation-distance check).
    # Plot only the segment BEFORE the packet first wraps the box, so the cyan
    # line is a single clean diagonal (no fold-back rungs) showing centroid ≈ c·t.
    if centroid is not None:
        planes = rec_oneway["planes"]
        span = planes.max() - planes.min()
        c = np.asarray(centroid)
        wrapped = np.abs(c - c[0]) >= span
        last = int(np.argmax(wrapped)) if wrapped.any() else len(c)
        if last <= 1:
            last = len(c)
        seg = c[:last]
        axes[0, 0].plot(seg, np.arange(last), color="cyan", lw=1.6, ls="--",
                        label="measured energy-centroid (≈ c·t, pre-wrap)")
        axes[0, 0].legend(loc="upper right", fontsize=7, framealpha=0.5)
    _panel_filmstrip(axes[0, 1], rec_oneway)
    axes[0, 1].set_title("filmstrip: one-way envelope translating")
    _panel_energy(axes[0, 2], rec_oneway["energy"], drift_floor_label=drift_floor_label)

    # row 2 — old delocalized directional Bloch seed (the standing fringe)
    _panel_spacetime(axes[1, 0], rec_bloch)
    axes[1, 0].set_title("x-t: OLD seed (delocalized Bloch = standing fringe)")
    _panel_filmstrip(axes[1, 1], rec_bloch)
    axes[1, 1].set_title("filmstrip: OLD directional Bloch seed")
    _panel_energy(axes[1, 2], rec_bloch["energy"])

    fig.tight_layout()
    path = _fig_path(test_id)
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    return path


def save_simple_figure(test_id: str, title: str, draw):
    """Render + save a single-/multi-panel figure built by `draw(fig)`.

    For L0 tests that want an energy trace + a field snapshot rather than the full
    propagation triptych. `draw` receives the Figure and owns its axes.
    """
    plt = _mpl()
    fig = plt.figure(figsize=(11, 4.6))
    fig.suptitle(f"{test_id} — {title}", fontsize=12, y=1.02)
    draw(fig)
    fig.tight_layout()
    path = _fig_path(test_id)
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    return path


# ── L2 (EM-in-media) panels: the 1D graded EM-line x-t + the achromatic plot ──
def _panel_em_spacetime(ax, line: dict, *, region=None, title="x-t spacetime"):
    """x-t of a 1D graded EM line (run_em_line output): cell index × step, color
    = energy density. A constant-speed band whose SLOPE changes in the biased
    region; the optional `region`=(lo,hi) cell window is outlined."""
    st = line["spacetime"]
    N = line["N"]
    times = line["times"]
    im = ax.imshow(
        st, origin="lower", aspect="auto",
        extent=[0, N, times.min(), times.max()], cmap="magma",
    )
    ax.set_xlabel("cell index (propagation axis)")
    ax.set_ylabel("timestep")
    ax.set_title(title)
    cb = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label("energy density |V|²·C")
    if region is not None:
        lo, hi = region
        ax.axvline(lo, color="cyan", lw=1.0, ls="--")
        ax.axvline(hi, color="cyan", lw=1.0, ls="--")
        ax.text(0.5 * (lo + hi), times.max() * 0.96, "biased region",
                color="cyan", ha="center", va="top", fontsize=8)
    return im


def save_l2_figure(test_id: str, title: str, draw):
    """Generic L2 figure composer — `draw(fig)` owns its axes/panels."""
    plt = _mpl()
    fig = plt.figure(figsize=(15.5, 4.8))
    fig.suptitle(f"{test_id} — {title}", fontsize=12, y=1.03)
    draw(fig)
    fig.tight_layout()
    path = _fig_path(test_id)
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    return path
