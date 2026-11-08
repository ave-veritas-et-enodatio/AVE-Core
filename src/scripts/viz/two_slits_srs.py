#!/usr/bin/env python3
"""VISUAL 4 -- "Two slits in the srs lattice" (engine-driven video, scored against a converged wave-equation reference).

A plane-wave packet in the engine's T1.1 channel runs through a two-slit screen cut into the chiral
srs net. The video shows the wave crossing the lattice, the intensity it deposits on a screen 15
wavelengths downstream, and the far-field (lens) pattern. Every pattern is SCORED: against an
independent, converged solver of the scalar wave equation in the same geometry (near field) and against
the textbook minima sin(theta) = (m + 1/2) lambda / d (far field). A placement scene shows where the
bond-cut slits are too coarse: the near-field pattern depends on where the slit edges fall in the crystal,
by up to several percent even at 32 bond lengths per wavelength; the far field does not.

WHAT IS ENGINE-EXACT vs REFERENCE vs DISPLAY CHOICE (full ledger: viz/README.md, Visual 4):
  ENGINE-EXACT: srs geometry (chiral_lattice srs motif and bond rule, degree 3, right-handed I4_1 32),
    in a slab two cells thick (periodic along the slits, x); the step = Op5 shunt scatter
    S = (2/3)J - I plus the CONNECT permutation, in one function (tlm_step) that the run loop calls and
    that is checked bit for bit against chiral_lattice_vector.vector_tlm_step (optical activity OFF, the
    kappa=0 channel acceptance test T1.1 runs) on every run. Tank voltage V_i = (2/3) sum_p V_inc. The
    lock-in frequency is the lattice's acoustic-band frequency at the seed wavenumber (Bloch, computed).
  BOUNDARIES (driver-added, not engine features): the screen = every bond crossing the wall plane
    outside the slits is shorted at its midpoint (reflection -1, the standard TLM short); graded
    absorbing layers on the y and z faces; the y/z periodic-wrap bonds are dropped (a matched edge),
    so nothing re-enters the box. Energy bookkeeping closes to round-off.
  REFERENCE (no engine import): leapfrog finite-difference solution of the 2D scalar wave equation,
    same geometry in units of lambda, Dirichlet zero-thickness screen, 128 points per wavelength.
  DISPLAY CHOICES: geometry (slit width 2 lambda, separation 8 lambda, screen 15 lambda, lambda = 32
    bond lengths); the packet length; colour scale (clipped); the raster smoothing; the inset window.

RECEIPTS (computed every run, written to ts_meta.json): operator identity vs vector_tlm_step; energy
closure; the acoustic frequency (Bloch eigenphase; the Grover relation cos w = mu_max is an identity
check, equal by theorem); the incident wavenumber measured off the field; lock-in convergence; the
wall's normal-incidence reflection and the short plane's offset; the screen signal's spectral purity;
the seed's stationary (flat-band) remainder; the near- and far-field scores, both sides of the screen;
a placement sweep at lambda = 16 and 32 bond lengths: the wall plane at 4 positions in the cubic cell
(exhaustive: the cut set changes only when the plane crosses a node layer) x the slit pair at 4 offsets
along y (0, 1/8, 1/4, 3/8 of the cell).

DISCIPLINE
  * consistency-vs-emergence: a CONSISTENCY check of certified engine behaviour (the T1.1 channel
    obeys the wave equation at long wavelength). It discriminates nothing: any medium whose long waves
    obey the wave equation draws these fringes (common/claim-quality.md:1382, "AC agreement cannot
    distinguish"; Hertz's razor, common/physics-lineage-map.md:534).
  * wave only. The single-quantum, dot-by-dot double slit is NOT simulated (the moving-defect
    double-slit pre-reg is an ENGINE-GAP; its pilot-channel fork is open).
  * sector: the displayed quantity is the port-sum tank voltage of one polarization of the T1.1
    channel; which physical sector that port-sum channel is, inside an engine labelled
    transverse-only, is open (same flag as Visual 3).
  * alpha-clean: imports only chiral_lattice{,_vector} (asserted below).
  * INTERNAL-REVIEW visual: on-frame text keeps corpus ids for audit; a public cut strips them.

Run:
    cd src
    PYTHONPATH=. python3 scripts/viz/two_slits_srs.py               # engine + reference + sweep + video
    PYTHONPATH=. python3 scripts/viz/two_slits_srs.py --stills      # + key-frame PNGs
    PYTHONPATH=. python3 scripts/viz/two_slits_srs.py --render-only # re-render from the cache
Needs ffmpeg on PATH for the video. Full run: about 30 min wall on 8 cores (the lambda = 32 lattice has
2.96 M tanks; each run is about 10 min single-core).

Writes:
    viz/two_slits_srs/two_slits_srs.mp4
    viz/two_slits_srs/ts_meta.json        (receipts and scores)
    viz/two_slits_srs/ts_*.png            (with --stills)
    build/viz/two_slits_srs/*.npz         (engine and reference arrays; gitignored cache)
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass, replace
from itertools import product
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.collections import LineCollection  # noqa: E402
from scipy.ndimage import gaussian_filter  # noqa: E402

# -- repo import wiring (driver runs from src/ with PYTHONPATH=.) --
_REPO_ROOT = Path(__file__).resolve().parents[3]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core import chiral_lattice_vector as clv  # noqa: E402
from ave.viz import style  # noqa: E402

for _m in (cl, clv):  # alpha-clean guard
    for _sym in ("ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "RHO_BULK"):
        assert _sym not in vars(_m), f"alpha-leak: {_sym} reachable in {_m.__name__}"

OUT_DIR = _REPO_ROOT / "viz" / "two_slits_srs"
CACHE_DIR = _REPO_ROOT / "build" / "viz" / "two_slits_srs"  # gitignored (build/)
META_NAME = "ts_meta.json"
VIDEO_NAME = "two_slits_srs.mp4"
A_CELL = 2.0 * np.sqrt(2.0)  # srs cubic cell [l_node]; one bond = one l_node (build_srs_net default)


# =============================================================================
# ENGINE PASS
# =============================================================================
@dataclass(frozen=True)
class Geometry:
    """Lengths in units of the wavelength unless marked [l_node]. All DISPLAY CHOICES except lam's role."""

    lam: float = 32.0  # wavelength [l_node]
    w: float = 2.0  # slit width
    d: float = 8.0  # slit separation, centre to centre
    D: float = 15.0  # wall -> screen
    sig_z: float = 3.0  # packet envelope sigma (about 5% bandwidth)
    y_in: float = 9.375  # half-width of the absorber-free region (1.25 x the central diffraction lobe)
    absorb: float = 6.0  # absorbing-layer thickness
    s_max: float = 0.1  # absorber: per-step amplitude loss exp(-s_max * depth^3), depth in [0, 1]
    up: float = 18.0  # upstream room (6 sigma); packet starts 3 sigma before the wall
    wall_shift: float = 0.0  # shift of the wall plane [l_node] (registration sweep)
    slit_dy: float = 0.0  # shift of the slit pair (and the beam) along y [fraction of the cubic cell]
    Lx: int = 2  # slab thickness along the slits [cells]; field is x-periodic (kx = 0)

    @property
    def slit_shift(self) -> float:
        return self.slit_dy * A_CELL

    @property
    def wall_frac(self) -> float:
        return ((self.absorb + self.up) * self.lam + self.wall_shift) / A_CELL % 1.0


def shift_for_frac(geo: Geometry, frac: float) -> float:
    """Wall shift [l_node] that puts the wall plane at the given fraction of the cubic cell (smallest move)."""
    cur = ((geo.absorb + geo.up) * geo.lam) / A_CELL % 1.0
    dfr = (frac - cur) % 1.0
    return float(dfr * A_CELL - (A_CELL if dfr > 0.5 else 0.0))


def acoustic_omega(kz: float) -> dict:
    """The lattice's acoustic (lowest-band) frequency at wavenumber kz along z, two independent ways.

    (1) eigenphases of the Bloch one-step operator U(k) = P(k) (I (x) S) on a 2-cell srs supercell:
        the smallest non-zero |phase|; (2) the Grover relation cos w = mu_max(A(k)/3). (1) = (2) is a theorem
        for this walk: an IDENTITY check, not an independent measurement. Also counts the flat bands (phase
        exactly 0 or pi): one third of all port states for any degree-3 net (also a theorem).
    """
    net = cl.build_srs_net(2, "right")
    n = net.n_nodes
    src, dst = net.connect_index()
    bu = np.asarray(net.bond_unit)
    u, p, v = src // 3, src % 3, dst // 3
    k = np.array([0.0, 0.0, kz])
    P = np.zeros((3 * n, 3 * n), complex)
    P[dst, src] = np.exp(-1j * (bu[u, p] @ k))
    ph = np.abs(np.angle(np.linalg.eigvals(P @ np.kron(np.eye(n), cl.scatter_matrix(3)))))
    Amat = np.zeros((n, n), complex)
    np.add.at(Amat, (u, v), np.exp(1j * (bu[u, p] @ k)))
    w_grover = float(np.arccos(np.clip(np.linalg.eigvalsh(Amat / 3.0).max(), -1, 1)))
    w_bloch = float(np.sort(ph[ph > 1e-9])[0])

    def w_of(kv):
        Am = np.zeros((n, n), complex)
        np.add.at(Am, (u, v), np.exp(1j * (bu[u, p] @ kv)))
        return float(np.arccos(np.clip(np.linalg.eigvalsh(Am / 3.0).max(), -1, 1)))

    iso = 0.0  # isotropy in the slab's plane (kx = 0): |k| at fixed w0 versus direction, 0..90 deg from z
    for th in np.radians(np.arange(0, 91, 10)):
        dvec = np.array([0.0, np.sin(th), np.cos(th)])
        lo, hi = 0.5 * kz, 1.5 * kz
        for _ in range(50):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if w_of(mid * dvec) < w_bloch else (lo, mid)
        iso = max(iso, abs(0.5 * (lo + hi) / kz - 1.0))
    return {
        "w0": w_bloch,
        "w_grover": w_grover,
        "flat_frac": float(np.mean((ph < 1e-9) | (np.abs(ph - np.pi) < 1e-9))),
        "c_ratio": w_bloch / (kz / np.sqrt(3.0)),
        "isotropy_max_dk_over_k": iso,
    }


def tlm_step(V: np.ndarray, S: np.ndarray, src: np.ndarray, dst: np.ndarray):
    """One Op5 scatter + connect step for ONE polarization, V shape (N, 3). Returns (V_ref, V_new), both flat.
    run_lattice calls exactly this function; the boundaries act on its outputs afterwards."""
    Vr = (V @ S.T).reshape(-1)
    Vn = np.empty_like(Vr)
    Vn[dst] = Vr[src]
    return Vr, Vn


def operator_identity_receipt(n_steps: int = 50) -> float:
    """Max |tlm_step - vector_tlm_step| (polarization 0) after n_steps from random port voltages, on a periodic srs
    net. Note: S is symmetric and the connect permutation is its own inverse, so a transposed S or a reversed
    permutation would be no-ops; what this checks is that the run loop's operator IS the engine's operator."""
    net = cl.build_srs_net(4, "right")
    S = cl.scatter_matrix(3)
    conn = net.connect_index()
    s4, d4 = conn
    rng = np.random.default_rng(0)
    V = rng.standard_normal((net.n_nodes, 3))
    Wv = np.zeros((net.n_nodes, 3, 2))
    Wv[..., 0] = V
    for _ in range(n_steps):
        V = tlm_step(V, S, s4, d4)[1].reshape(-1, 3)
        Wv = clv.vector_tlm_step(net, Wv, S, conn, None)
    return float(max(np.abs(V - Wv[..., 0]).max(), np.abs(Wv[..., 1]).max()))


def short_plane_offset(z_wall: float) -> float:
    """Offset [l_node] of the plane of the shorts (the midpoints of the bonds crossing the wall plane) from the
    nominal wall plane. srs node layers sit at 1/8, 3/8, 5/8, 7/8 of the cell; bonds join adjacent layers."""
    q = (z_wall / A_CELL - 0.125) * 4.0
    z_lo = (np.floor(q) / 4.0 + 0.125) * A_CELL
    return float(z_lo + A_CELL / 8 - z_wall)


def build_slab(geo: Geometry):
    """srs slab: Lx x Ly x Lz cubic cells, periodic box; returns the net and centred coordinates."""
    lam = geo.lam
    ly = int(np.ceil(2 * (geo.y_in + geo.absorb) * lam / A_CELL))
    lz = int(np.ceil((2 * geo.absorb + geo.up + geo.D + 2.0) * lam / A_CELL))
    motif = cl.srs_motif("right")
    pts = np.array(
        [
            m + np.array([cx, cy, cz], float)
            for cx, cy, cz in product(range(geo.Lx), range(ly), range(lz))
            for m in motif
        ]
    )
    net = cl._build_net_from_points(  # same builder as build_srs_net, with a non-cubic periodic box
        pts,
        np.array([geo.Lx, ly, lz], float),
        cl._SRS_NN,
        3,
        "srs slab",
        "right (I4_1 32)",
        a_cell=A_CELL,
        carrier="srs-z3",
    )
    src, dst = net.connect_index()
    assert all(len(nb) == 3 for nb in net.neighbors), "srs slab: degree != 3"
    assert np.array_equal(np.sort(dst), np.arange(3 * net.n_nodes)), "connect is not a permutation"
    bu = np.asarray(net.bond_unit)
    dv = net.pos[dst // 3] - net.pos[src // 3]
    dv -= net.box * np.round(dv / net.box)
    blen = np.linalg.norm(dv, axis=1)
    assert np.allclose(blen, 1.0, atol=1e-9), f"bond length {blen.min()}..{blen.max()} != 1 l_node"
    assert np.allclose(dv, bu[src // 3, src % 3], atol=1e-9), "bond_unit disagrees with neighbour positions"
    return net, src, dst, bu


def wall_arcs(geo: Geometry, y, z, src, bu, open_: str, z_wall: float):
    """Directed arcs crossing the wall plane: cut (outside the slits) and open (inside slit 1 / slit 2)."""
    lam = geo.lam
    u, p = src // 3, src % 3
    za, zb = z[u] - z_wall, z[u] + bu[u, p, 2] - z_wall
    cross = (za * zb) < 0
    t = np.where(cross, (z_wall - z[u]) / np.where(bu[u, p, 2] == 0, 1, bu[u, p, 2]), 0.0)
    yc = y[u] + bu[u, p, 1] * t  # where the bond pierces the wall plane
    yc = yc - geo.slit_shift  # the slits' own frame
    s1 = cross & (np.abs(yc + geo.d * lam / 2) < geo.w * lam / 2) & ("1" in open_)
    s2 = cross & (np.abs(yc - geo.d * lam / 2) < geo.w * lam / 2) & ("2" in open_)
    cut = cross & ~s1 & ~s2 if open_ != "free" else np.zeros_like(cross)
    return cut, s1 | s2, cross


def run_lattice(geo: Geometry, open_: str, w0: float, tag: str, frames: bool = False) -> str:
    """One lattice run. open_: '12' | '1' | '2' | 'free' (no screen). Saves an npz in CACHE_DIR; returns its path."""
    t0 = time.time()
    lam = geo.lam
    net, src, dst, bu = build_slab(geo)
    n = net.n_nodes
    box = net.box
    pos = net.pos
    y = pos[:, 1] - box[1] / 2
    z = pos[:, 2]
    S = cl.scatter_matrix(3)
    absorb = geo.absorb * lam
    z_wall = (geo.absorb + geo.up) * lam + geo.wall_shift
    z_scr_target = z_wall + geo.D * lam
    cut, opened, cross = wall_arcs(geo, y, z, src, bu, open_, z_wall)
    cut_idx = src[cut]
    # matched edge: the y/z periodic-wrap arcs are dropped (absorbed), so nothing re-enters the box
    dv = pos[dst // 3] - pos[src // 3] - bu[src // 3, src % 3]
    wrap = (np.abs(dv[:, 1]) > 0.5) | (np.abs(dv[:, 2]) > 0.5)
    drop_src, drop_dst = src[wrap], dst[wrap]
    # graded absorbing layers on the y and z faces
    ey = np.clip(np.abs(y) - (box[1] / 2 - absorb), 0, None) / absorb
    ez = np.maximum(np.clip(absorb - z, 0, None), np.clip(z - (box[2] - absorb), 0, None)) / absorb
    f_node = np.exp(-geo.s_max * np.maximum(ey, ez) ** 3)
    sponge = np.where(f_node < 1.0)[0]
    fs = f_node[sponge, None]
    # seed: the T1.1 one-way rule (single-sign port occupancy, weight = |bond . z| on -z ports -> +z motion),
    # Gaussian envelope x carrier, centred 3 sigma before the wall; zero inside the y absorbers
    k0 = 2 * np.pi / lam
    z0 = z_wall - geo.up * lam / 2
    env = np.exp(-0.5 * ((z - z0) / (geo.sig_z * lam)) ** 2) * np.cos(k0 * z)
    y_mask = box[1] / 2 - absorb
    env[np.abs(y - geo.slit_shift) > y_mask] = 0.0  # the beam is centred on the slit pair
    V = np.clip(-bu[:, :, 2], 0, None) * env[:, None]
    E0 = float(np.sum(V * V))
    # readout sets (one x-cell: the field is x-periodic with kx = 0)
    zl = np.unique(np.round(z, 4))
    z_scr = float(zl[np.argmin(np.abs(zl - z_scr_target))])
    z_ff = float(zl[np.argmin(np.abs(zl - (z_wall + 2.0 * lam)))])
    xc0 = pos[:, 0] < A_CELL
    keep = xc0 & ((np.abs(z - z_scr) < 1e-3) | (np.abs(z - z_ff) < 1e-3) | (np.abs(z - z_wall) < 1.5 * lam))
    sel = np.where(keep)[0]
    scr = np.where(np.abs(z - z_scr) < 1e-3)[0]  # both x-cells, for the dose
    n_steps = int(1.30 * (geo.up / 2 + geo.D + 3 * geo.sig_z + 0.5 * (geo.y_in + geo.absorb)) * lam / 0.5)
    acc = np.zeros(len(sel), complex)
    snap = None
    dose = np.zeros(len(scr))
    ts = np.zeros((n_steps, len(scr)), np.float32)
    ab_s = ab_d = 0.0
    fr = {}
    if frames:
        fr = _frame_setup(geo, y, z, xc0, z_wall, opened, cut, src, dst, pos)
        fr["every"] = max(1, int(round(lam / 6.4)))
        fr["until"] = int((geo.up / 2 + geo.D + 3.4 * geo.sig_z) * lam / (1 / np.sqrt(3.0)))
        fr["frames"], fr["inset_v"], fr["dose_t"], fr["steps"] = [], [], [], []
    for it in range(n_steps):
        tank = (2.0 / 3.0) * V.sum(axis=1)
        acc += tank[sel] * np.exp(-1j * w0 * it)
        ts[it] = tank[scr]
        dose += tank[scr] ** 2
        if frames and it % fr["every"] == 0 and it <= fr["until"]:
            fr["frames"].append(_raster(fr, tank).astype(np.float16))
            fr["inset_v"].append(tank[fr["inset_nodes"]].astype(np.float32))
            fr["dose_t"].append(dose.astype(np.float32).copy())
            fr["steps"].append(it)
        if it == int(n_steps / 1.30):
            snap = acc.copy()
        Vr, Vn = tlm_step(V, S, src, dst)
        if len(cut_idx):
            Vn[cut_idx] = -Vr[cut_idx]  # short at the bond midpoint: the wave returns, inverted
        ab_d += float(np.sum(Vr[drop_src] ** 2))
        Vn[drop_dst] = 0.0
        Vn = Vn.reshape(n, 3)
        ab_s += float(np.sum((1 - fs**2) * Vn[sponge] ** 2))
        Vn[sponge] *= fs
        V = Vn
    E = float(np.sum(V * V))
    tank_end = (2.0 / 3.0) * V.sum(axis=1)
    e_node = np.sum(V * V, axis=1)
    near_seed = (np.abs(z - z0) < 3 * geo.sig_z * lam) & (np.abs(y - geo.slit_shift) <= y_mask)  # seed region
    spec = np.abs(np.fft.rfft(ts.astype(float), axis=0)) ** 2
    fq = 2 * np.pi * np.fft.rfftfreq(n_steps)
    band = np.abs(fq - w0) < 0.15 * w0
    out = dict(
        slit_shift=geo.slit_shift,
        screen_lowfreq=float(spec[fq < 0.5 * w0].sum() / spec.sum()),
        ys=y[sel],
        zs=z[sel],
        acc=acc,
        snap=snap,
        scr_y=y[scr],
        dose=dose,
        z_wall=z_wall,
        z_scr=z_scr,
        z_ff=z_ff,
        y_mask=y_mask,
        n_nodes=n,
        n_steps=n_steps,
        E0=E0,
        closure=(E + ab_s + ab_d) / E0,
        left_frac=E / E0,
        left_tank_frac=float(np.sum(0.75 * tank_end**2) / max(E, 1e-300)),
        left_near_seed_frac=float(e_node[near_seed].sum() / max(E, 1e-300)),
        screen_purity=float(spec[band].sum() / spec.sum()),
        lockin_late=float(np.abs(acc - snap).max() / np.abs(acc).max()),
        open_bonds=int(opened.sum() // 2),
        cut_bonds=int(cut.sum() // 2),
        wall_frac=geo.wall_frac,
        runtime_s=time.time() - t0,
    )
    if frames:
        for key in ("frames", "inset_v", "dose_t", "steps"):
            out[key] = np.asarray(fr[key])
        for key in ("extent", "inset_pos", "inset_bonds", "inset_kind", "inset_box"):
            out[key] = fr[key]
    path = CACHE_DIR / f"{tag}.npz"
    np.savez(path, **out)
    return str(path)


def _frame_setup(geo, y, z, xc0, z_wall, opened, cut, src, dst, pos) -> dict:
    """Raster window and the node-level inset (outer edge of the upper slit)."""
    lam = geo.lam
    px = lam / 20.0
    y_lo, y_hi = -geo.y_in * lam, geo.y_in * lam
    z_lo, z_hi = z_wall - 5.0 * lam, z_wall + (geo.D + 1.0) * lam
    ny, nz = int((y_hi - y_lo) / px), int((z_hi - z_lo) / px)
    m = xc0 & (y >= y_lo) & (y < y_hi) & (z >= z_lo) & (z < z_hi)
    nodes = np.where(m)[0]
    iy = np.clip(((y[nodes] - y_lo) / px).astype(int), 0, ny - 1)
    iz = np.clip(((z[nodes] - z_lo) / px).astype(int), 0, nz - 1)
    flat = iy * nz + iz
    cnt = gaussian_filter(np.bincount(flat, minlength=ny * nz).reshape(ny, nz).astype(float), 1.0)
    ye = (geo.d / 2 + geo.w / 2) * lam  # outer edge of the upper slit
    hy, hz = 0.6 * lam, 0.45 * lam
    mi = xc0 & (np.abs(y - ye) < hy) & (np.abs(z - z_wall) < hz)
    ins = np.where(mi)[0]
    loc = {g: i for i, g in enumerate(ins)}
    bonds, kind = [], []
    u_all, v_all = src // 3, dst // 3
    for a in np.where(mi[u_all] & mi[v_all] & (u_all < v_all))[0]:
        bonds.append((loc[u_all[a]], loc[v_all[a]]))
        kind.append(2 if cut[a] else (1 if opened[a] else 0))  # 2 = shorted (wall), 1 = open slit bond, 0 = bulk
    return dict(
        nodes=nodes,
        flat=flat,
        ny=ny,
        nz=nz,
        cnt=cnt,
        extent=np.array([z_lo, z_hi, y_lo, y_hi]),
        inset_nodes=ins,
        inset_pos=np.c_[y[ins], z[ins]],
        inset_bonds=np.array(bonds),
        inset_kind=np.array(kind),
        inset_box=np.array([ye - hy, ye + hy, z_wall - hz, z_wall + hz]),
    )


def _raster(fr: dict, tank: np.ndarray) -> np.ndarray:
    """Normalized-convolution raster of the tank voltages (Gaussian, 1 pixel = lam/20): DISPLAY CHOICE."""
    s = np.bincount(fr["flat"], weights=tank[fr["nodes"]], minlength=fr["ny"] * fr["nz"]).reshape(fr["ny"], fr["nz"])
    return gaussian_filter(s, 1.0) / np.maximum(fr["cnt"], 1e-12)


# =============================================================================
# REFERENCE PASS -- independent exact solver of the same 2D problem (imports nothing from ave.core)
# =============================================================================
def run_reference(geo: Geometry, open_: str, y_mask: float, d_scr: float, tag: str, ppw: int = 64) -> str:
    """2D scalar wave equation u_tt = c^2 lap u (leapfrog, h = lam/ppw, c dt = h/2), Dirichlet zero-thickness screen.

    Same incident packet (envelope, carrier, one-way, truncated at |y| = y_mask), same wall/screen distances.
    Damping layers sit OUTSIDE the lattice's absorber-free region.
    Lock-in at w = c k over the whole run = the exact single-frequency response; dose = time-integrated u^2.
    """
    t0 = time.time()
    lam = geo.lam
    h = lam / ppw
    c = 1.0
    dt = 0.5 * h / c
    absorb = 3.0 * lam  # z origin offset only (the reference's own layers are LAY thick, outside the region)
    z_wall = absorb + geo.up * lam
    z_scr = z_wall + d_scr
    z_lo_in, z_hi_in = absorb, z_wall + (geo.D + 2.0) * lam
    lay = 6.0 * lam
    # grid ALIGNED so the slit edges and the wall / screen planes fall exactly on grid lines (lam = ppw * h)
    ny = int(np.ceil((y_mask + lay) / h))
    yv = h * np.arange(-ny, ny + 1)
    zv = z_wall + h * np.arange(
        -int(np.ceil((z_wall - z_lo_in + lay) / h)), int(np.ceil((z_hi_in + lay - z_wall) / h)) + 1
    )
    Y, Z = np.meshgrid(yv, zv, indexing="ij")
    k = 2 * np.pi / lam
    w = c * k
    ey = np.clip(np.abs(Y) - y_mask, 0, None) / lay
    ez = np.maximum(np.clip(z_lo_in - Z, 0, None), np.clip(Z - z_hi_in, 0, None)) / lay
    damp = (18.0 * c / lay) * np.maximum(ey, ez) ** 2 * dt
    z0 = z_wall - geo.up * lam / 2
    mask = (np.abs(Y) <= y_mask).astype(float)

    def g(zz):
        return np.exp(-0.5 * ((zz - z0) / (geo.sig_z * lam)) ** 2) * np.cos(k * zz)

    u_prev, u = g(Z + c * dt) * mask, g(Z) * mask  # one-way: u(z - c t)
    iw = int(np.argmin(np.abs(zv - z_wall)))
    e = 1e-6 * h  # grid points exactly on a slit edge belong to the screen (Dirichlet edge at the nominal position)
    ap = ((np.abs(yv + geo.d * lam / 2) < geo.w * lam / 2 - e) & ("1" in open_)) | (
        (np.abs(yv - geo.d * lam / 2) < geo.w * lam / 2 - e) & ("2" in open_)
    )
    wall = ~ap if open_ != "free" else np.zeros(len(yv), bool)
    isc = int(np.argmin(np.abs(zv - z_scr)))
    band = np.where(np.abs(zv - z_scr) <= 0.1 * lam)[0]
    iff = int(np.argmin(np.abs(zv - (z_wall + 2.0 * lam))))
    n_steps = int(1.30 * (geo.up / 2 + geo.D + 3 * geo.sig_z + 0.5 * (geo.y_in + geo.absorb)) * lam / c / dt)
    acc_band = np.zeros((len(yv), len(band)), complex)
    acc_ff = np.zeros(len(yv), complex)
    acc_inc = np.zeros(len(yv), complex)
    dose = np.zeros(len(yv))
    r2 = (c * dt / h) ** 2
    lap = np.zeros_like(u)
    for it in range(n_steps):
        lap[1:-1, 1:-1] = u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4 * u[1:-1, 1:-1]
        u_next = (2 * u - (1 - damp) * u_prev + r2 * lap) / (1 + damp)
        u_next[wall, iw] = 0.0
        u_next[0, :] = u_next[-1, :] = 0.0
        u_next[:, 0] = u_next[:, -1] = 0.0
        u_prev, u = u, u_next
        ph = np.exp(-1j * w * (it + 1) * dt) * dt
        acc_band += u[:, band] * ph
        acc_ff += u[:, iff] * ph
        acc_inc += u[:, iw] * ph
        dose += u[:, isc] ** 2 * dt
    path = CACHE_DIR / f"{tag}.npz"
    np.savez(
        path,
        yv=yv,
        zband=zv[band] - zv[iw],
        acc_band=acc_band,
        acc_ff=acc_ff,
        z_ff=zv[iff] - zv[iw],
        acc_inc=acc_inc,
        dose=dose,
        d_scr=zv[isc] - zv[iw],
        ppw=ppw,
        runtime_s=time.time() - t0,
    )
    return str(path)


# =============================================================================
# SCORING -- everything in units of the wavelength; no fitted parameters anywhere
# =============================================================================
def _loess(y, f, yg, sig):
    """Local quadratic regression (Gaussian weights, width sig): unbiased at extrema on IRREGULAR samples.

    The screen tanks sit at an irregular spacing (0.71 / 2.12 l_node within a cell); a plain kernel average
    would bias extremum positions by up to a few percent at lambda = 16 l_node (measured), local quadratic does not.
    """
    dy = y[None, :] - yg[:, None]
    wk = np.exp(-0.5 * (dy / sig) ** 2)
    m = [np.sum(wk * dy**j, axis=1) for j in range(5)]
    r = [np.sum(wk * f[None, :] * dy**j, axis=1) for j in range(3)]
    M = np.stack(
        [np.stack([m[0], m[1], m[2]], -1), np.stack([m[1], m[2], m[3]], -1), np.stack([m[2], m[3], m[4]], -1)], -2
    )
    return np.linalg.solve(M, np.stack(r, -1)[..., None])[..., 0, 0]


def _extrema(yg, I, ymax, prom=0.01):
    """Extrema of I(yg) for |yg| < ymax with prominence >= prom * max(I), refined by a local parabola."""
    from scipy.signal import find_peaks

    m = np.abs(yg) < ymax
    yy, ii = yg[m], I[m]
    out = []
    for sign, kind in ((1.0, "max"), (-1.0, "min")):
        idx, _ = find_peaks(sign * ii, prominence=prom * ii.max())
        for i in idx:
            if 3 <= i < len(ii) - 3:
                c = np.polyfit(yy[i - 3 : i + 4] - yy[i], ii[i - 3 : i + 4], 2)
                out.append((yy[i] - c[1] / (2 * c[0]), kind, ii[i]))
    return sorted(out)


def _visibility(yg, I):
    """Central fringe visibility: central maximum vs the mean of the two adjacent minima (yg in lambda)."""
    ex = _extrema(yg, I, 3.75)
    mx = [v for y, t, v in ex if t == "max" and abs(y) < 0.2]
    mn = [v for y, t, v in ex if t == "min" and abs(y) < 1.6]
    return (mx[0] - np.mean(mn)) / (mx[0] + np.mean(mn))


def _pair(xl, xf, n=8, tol=0.45):
    """Pair each of the first n reference extrema (y > 0) with the nearest lattice extremum of the same type within
    tol lambda. Returns [(y_lat, y_ref, type)], the number of reference extrema left unpaired, and the number of
    lattice extrema in the same range that no reference extremum claimed."""
    pairs, miss = [], 0
    xf = [e for e in xf if e[0] > 0.02][:n]
    for yf, tf, _ in xf:
        cand = [e for e in xl if e[1] == tf and abs(e[0] - yf) < tol]
        if cand:
            pairs.append((min(cand, key=lambda e: abs(e[0] - yf))[0], yf, tf))
        else:
            miss += 1
    used = {p[0] for p in pairs}
    ymax = xf[-1][0] + tol if xf else 0.0
    extra = sum(1 for e in xl if 0.02 < e[0] < ymax and e[0] not in used)
    return pairs, miss, extra


def _lat_inc(free) -> float:
    m = (np.abs(free["zs"] - free["z_wall"]) < 1.5) & (np.abs(free["ys"]) < 10)
    return float(np.mean(np.abs(free["acc"][m])))


def lat_screen(run, free, yg_lam, lam):
    """Lattice INTENSITY on the screen layer: each tank's |lock-in amplitude|^2 / incident^2, then local quadratic
    regression (width 1.5 l_node). Intensities, not complex amplitudes, are combined: tanks of different sublattices
    carry slightly different phases at finite k, and averaging complex values across them biases the fringes."""
    s = np.abs(run["zs"] - run["z_scr"]) < 1e-3
    I = np.abs(run["acc"][s] / _lat_inc(free)) ** 2
    return _loess((run["ys"][s] - _shift(run)) / lam, I, yg_lam, 1.5 / lam)


def _shift(run) -> float:
    return float(run["slit_shift"]) if "slit_shift" in run else 0.0


def ref_screen(ref, ref_free, d_lam, yg_lam, lam_ref):
    """Exact INTENSITY at wall->screen distance d_lam (linear across the band of rows, cubic along y)."""
    from scipy.interpolate import CubicSpline

    zb = ref["zband"] / lam_ref
    j = int(np.clip(np.searchsorted(zb, d_lam) - 1, 0, len(zb) - 2))
    assert (
        zb[0] - 1e-9 <= d_lam <= zb[-1] + 1e-9
    ), f"screen distance {d_lam} outside the reference band {zb[0]}..{zb[-1]}"
    t = (d_lam - zb[j]) / (zb[j + 1] - zb[j])
    E = (1 - t) * ref["acc_band"][:, j] + t * ref["acc_band"][:, j + 1]
    E = E / np.mean(np.abs(ref_free["acc_inc"][np.abs(ref_free["yv"]) < 10]))
    return CubicSpline(ref["yv"] / lam_ref, np.abs(E) ** 2)(yg_lam)


def lat_dose(run, free, yg_lam, lam):
    """Screen dose (sum over steps of V_tank^2, both x-cells), normalized by the free run's dose near the axis."""
    inc = np.mean(free["dose"][np.abs(free["scr_y"]) < 10])
    return _loess((run["scr_y"] - _shift(run)) / lam, run["dose"] / inc, yg_lam, 1.5 / lam)


def ref_dose(ref, ref_free, yg_lam, lam_ref):
    from scipy.interpolate import CubicSpline

    inc = np.mean(ref_free["dose"][np.abs(ref_free["yv"]) < 10])
    return CubicSpline(ref["yv"] / lam_ref, ref["dose"] / inc)(yg_lam)


def _spectrum(yu, Eu, s, k):
    edges = np.concatenate([[yu[0] - (yu[1] - yu[0]) / 2], (yu[1:] + yu[:-1]) / 2, [yu[-1] + (yu[-1] - yu[-2]) / 2]])
    F = (Eu[None, :] * np.diff(edges)[None, :] * np.exp(-1j * k * s[:, None] * yu[None, :])).sum(1)
    I = np.abs(F) ** 2 * (1 - s**2)  # 2D far field ~ cos^2(theta) |E~(k sin theta)|^2
    return I / I.max()


def lat_far(run, s, lam):
    """Far-field (lens) intensity from the lattice field on the layer 2 lambda past the wall (angular spectrum)."""
    ys = run["ys"] - _shift(run)
    sl = (np.abs(run["zs"] - run["z_ff"]) < 1e-3) & (np.abs(ys) < run["y_mask"])
    yu, inv = np.unique(np.round(ys[sl], 6), return_inverse=True)
    E = run["acc"][sl]
    cnt = np.bincount(inv)
    Eu = np.bincount(inv, E.real) / cnt + 1j * np.bincount(inv, E.imag) / cnt
    return _spectrum(yu, Eu, s, 2 * np.pi / lam)


def ref_far(ref, s, lam_ref, y_mask):
    m = np.abs(ref["yv"]) < y_mask
    return _spectrum(ref["yv"][m], ref["acc_ff"][m], s, 2 * np.pi / lam_ref)


def _minima(x, I, lo, hi):
    """Far-field minima in (lo, hi): local minima of log10(I) at least one decade deep, parabola-refined in log."""
    from scipy.signal import find_peaks

    li = np.log10(np.maximum(I, 1e-14))
    out = []
    for i in find_peaks(-li, prominence=1.0)[0]:
        if lo < x[i] < hi and 3 <= i < len(x) - 3:
            c = np.polyfit(x[i - 3 : i + 4] - x[i], li[i - 3 : i + 4], 2)
            out.append((x[i] - c[1] / (2 * c[0]), float(I[i])))
    return out


def score(lat12, lat1, free, ref12, ref1, rfree, lam, lam_ref, d_over_lam) -> dict:
    """Near field (screen) and far field (lens) scores of one lattice registration against the exact solution."""
    yg = np.linspace(-8.75, 8.75, 2801)
    d_lam = float(lat12["z_scr"] - lat12["z_wall"]) / lam
    out = {"lam": lam, "wall_frac": float(lat12["wall_frac"]), "D_over_lam": d_lam}
    for key, lat, ref in (("two", lat12, ref12), ("one", lat1, ref1)):
        if lat is None:
            continue
        Il, If = lat_screen(lat, free, yg, lam), ref_screen(ref, rfree, d_lam, yg, lam_ref)
        pairs, miss, extra = _pair(_extrema(yg, Il, 7.8), _extrema(yg, If, 7.8))
        # the mirrored side (y < 0): needed once the slit pair is offset from a lattice symmetry
        pn, mn, xn = _pair(_extrema(yg, Il[::-1], 7.8), _extrema(yg, If[::-1], 7.8)) if key == "two" else ([], 0, 0)
        both = pairs + pn
        out[key] = {
            "extrema_type": [t for _, _, t in pairs],
            "extrema_lat": [round(a, 4) for a, _, _ in pairs],
            "extrema_exact": [round(b, 4) for _, b, _ in pairs],
            "err_pct": [round(100 * (a - b) / b, 3) for a, b, _ in pairs],
            "err_pct_neg_side": [round(100 * (a - b) / b, 3) for a, b, _ in pn],
            "max_abs_err_pct": round(max(abs(100 * (a - b) / b) for a, b, _ in both), 3) if both else None,
            "unpaired": miss + mn,
            "unmatched_lat": extra + xn,
            "peak_ratio": round(float(Il.max() / If.max()), 4),
            "rms_peak_norm": round(float(np.sqrt(np.mean((Il / Il.max() - If / If.max())[np.abs(yg) < 7.5] ** 2))), 4),
        }
        if key == "two":
            out[key]["V_lat"], out[key]["V_exact"] = round(float(_visibility(yg, Il)), 4), round(
                float(_visibility(yg, If)), 4
            )
    # the time-integrated dose (what the screen accumulates; same packet in both) -- the curve the video draws
    dl, df = lat_dose(lat12, free, yg, lam), ref_dose(ref12, rfree, yg, lam_ref)
    pairs, miss, extra = _pair(_extrema(yg, dl, 7.8), _extrema(yg, df, 7.8))
    pn, mn, xn = _pair(_extrema(yg, dl[::-1], 7.8), _extrema(yg, df[::-1], 7.8))
    both = pairs + pn
    out["dose"] = {
        "err_pct": [round(100 * (a - b) / b, 3) for a, b, _ in pairs],
        "err_pct_neg_side": [round(100 * (a - b) / b, 3) for a, b, _ in pn],
        "max_abs_err_pct": round(max(abs(100 * (a - b) / b) for a, b, _ in both), 3) if both else None,
        "unpaired": miss + mn,
        "unmatched_lat": extra + xn,
        "V_lat": round(float(_visibility(yg, dl)), 4),
        "V_exact": round(float(_visibility(yg, df)), 4),
        "peak_ratio": round(float(dl.max() / df.max()), 4),
    }
    s = np.linspace(-0.62, 0.62, 4961)  # symmetric grid: s[::-1] = -s
    Fl = lat_far(lat12, s, lam)
    Ff = ref_far(ref12, s, lam_ref, float(lat12["y_mask"]) / lam * lam_ref)
    ml, mf = _minima(s, Fl, 0.02, 0.48), _minima(s, Ff, 0.02, 0.48)
    mln, mfn = _minima(s, Fl[::-1], 0.02, 0.48), _minima(s, Ff[::-1], 0.02, 0.48)
    ideal = [(m + 0.5) / d_over_lam for m in range(int(0.48 * d_over_lam - 0.5) + 1)]

    def near(xs, ys, tol=0.02):  # pair each target y with the nearest x within tol (minima are 1/d_over_lam apart)
        out_ = []
        for y_ in ys:
            c = [x_ for x_ in xs if abs(x_ - y_) < tol]
            if c:
                out_.append((min(c, key=lambda x_: abs(x_ - y_)), y_))
        return out_

    pe = near([a for a, _ in ml], [b for b, _ in mf])
    pen = near([a for a, _ in mln], [b for b, _ in mfn])
    pt = near([a for a, _ in ml], ideal)
    out["far"] = {
        "minima_lat": [round(a, 5) for a, _ in ml],
        "minima_exact": [round(a, 5) for a, _ in mf],
        "minima_textbook": [round(a, 5) for a in ideal],
        "err_vs_textbook_pct": [round(100 * (a - b) / b, 3) for a, b in pt],
        "err_vs_exact_pct": [round(100 * (a - b) / b, 3) for a, b in pe],
        "err_vs_exact_pct_neg_side": [round(100 * (a - b) / b, 3) for a, b in pen],
        "exact_vs_textbook_pct": [round(100 * (a - b) / b, 3) for a, b in near([b for b, _ in mf], ideal)],
        "unpaired": (len(mf) - len(pe)) + (len(mfn) - len(pen)) + (len(ideal) - len(pt)),
        "depth_lat": [float(f"{v:.2e}") for _, v in ml + mln],
    }
    return out


# =============================================================================
# ORCHESTRATION -- every lattice / reference run is a cached npz; runs fan out over processes
# =============================================================================
SWEEP_FRACS = (0.0, 0.25, 0.5, 0.75)  # wall-plane positions in the cubic cell (plus each lambda's natural one)
SWEEP_DY = (0.125, 0.25, 0.375)  # slit-pair offsets along y [fraction of the cell]; 1/2 repeats 0 (body centring)


def _job(kind: str, geo: Geometry, open_: str, tag: str, extra: dict):
    path = CACHE_DIR / f"{tag}.npz"
    if path.exists():
        return tag, str(path), 0.0
    t0 = time.time()
    if kind == "lattice":
        run_lattice(geo, open_, extra["w0"], tag, frames=extra.get("frames", False))
    else:
        run_reference(geo, open_, extra["y_mask"], extra["d_scr"], tag, ppw=extra.get("ppw", 64))
    return tag, str(path), time.time() - t0


def run_all(main_lam: float, sweep: bool, workers: int, ref_ppw: int = 128) -> dict:
    """Plan and execute every run; returns {tag: path} plus the Bloch receipts per lambda."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    lams = sorted({main_lam, 16.0, 32.0} if sweep else {main_lam})
    bloch = {lam: acoustic_omega(2 * np.pi / lam) for lam in lams}
    jobs = []
    for lam in lams:
        g0 = Geometry(lam=lam)
        nat = g0.wall_frac
        regs = [("nat", g0)]
        if sweep:
            regs += [(f"f{fr:.2f}", replace(g0, wall_shift=shift_for_frac(g0, fr))) for fr in SWEEP_FRACS]
        jobs.append(("lattice", g0, "free", f"lat_l{lam:g}_free", {"w0": bloch[lam]["w0"]}))
        for name, g in regs:
            for o in ("12", "1"):
                fr = lam == main_lam and name == "nat" and o == "12"
                jobs.append(("lattice", g, o, f"lat_l{lam:g}_{name}_o{o}", {"w0": bloch[lam]["w0"], "frames": fr}))
        if sweep:  # the slit pair offset along y, two-slit runs only (the single-slit row is outside the bar)
            for fr_ in SWEEP_FRACS:
                for dy in SWEEP_DY:
                    g = replace(g0, wall_shift=shift_for_frac(g0, fr_), slit_dy=dy)
                    jobs.append(
                        ("lattice", g, "12", f"lat_l{lam:g}_f{fr_:.2f}_y{dy:.3f}_o12", {"w0": bloch[lam]["w0"]})
                    )
        _ = nat
    # the exact reference is solved once, at the main lambda (the problem is scale-free in units of lambda)
    g0 = Geometry(lam=main_lam)
    y_mask = np.ceil(2 * (g0.y_in + g0.absorb) * main_lam / A_CELL) * A_CELL / 2 - g0.absorb * main_lam
    for o in ("free", "12", "1"):
        jobs.append(
            (
                "reference",
                g0,
                o,
                f"ref_l{main_lam:g}_p{ref_ppw}_o{o}",
                {"y_mask": y_mask, "d_scr": g0.D * main_lam, "ppw": ref_ppw},
            )
        )
    for o in ("free", "12"):  # convergence receipt: the same reference at half the resolution
        jobs.append(
            (
                "reference",
                g0,
                o,
                f"ref_l{main_lam:g}_p{ref_ppw // 2}_o{o}",
                {"y_mask": y_mask, "d_scr": g0.D * main_lam, "ppw": ref_ppw // 2},
            )
        )
    jobs.sort(key=lambda j: -j[1].lam)  # longest first
    paths = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(_job, *j) for j in jobs]
        for f in futs:
            tag, path, dt = f.result()
            paths[tag] = path
            print(f"  {tag}: {'cached' if dt == 0 else f'{dt:.0f} s'}", flush=True)
    return {"paths": paths, "bloch": bloch, "lams": lams, "y_mask_ref": float(y_mask), "ref_ppw": ref_ppw}


def _load(path):
    with np.load(path, allow_pickle=False) as z:
        return {k: z[k] for k in z.files}


def kirchhoff_vs_exact(g0: Geometry, I_ex, yg, d_lam) -> list:
    """Extremum errors (%) of Rayleigh-Sommerfeld-I with a uniform (Kirchhoff) aperture field, vs the exact solution."""
    from scipy.special import hankel1

    k = 2 * np.pi
    P = np.zeros_like(yg, dtype=complex)
    for c in (-g0.d / 2, g0.d / 2):
        ap = np.linspace(c - g0.w / 2, c + g0.w / 2, 801)
        rho = np.sqrt((yg[:, None] - ap[None, :]) ** 2 + d_lam**2)
        P += ((d_lam / rho) * hankel1(1, k * rho)).sum(1)
    I_k = np.abs(P) ** 2
    pr, miss, extra = _pair(_extrema(yg, I_k, 7.8), _extrema(yg, I_ex, 7.8))
    return {"err_pct": [round(100 * (a - b) / b, 2) for a, b, _ in pr], "unpaired": miss, "unmatched": extra}


def write_meta(plan: dict, main_lam: float) -> dict:
    """Receipts and scores -> ts_meta.json (deterministic content; runtimes excluded)."""
    P = plan["paths"]
    g0 = Geometry(lam=main_lam)
    ref = {o: _load(P[f"ref_l{main_lam:g}_p{plan['ref_ppw']}_o{o}"]) for o in ("free", "12", "1")}
    meta = {
        "geometry": asdict(g0),
        "receipts": {"operator_identity_max_abs_diff": operator_identity_receipt()},
        "bloch": {f"{lam:g}": {k: round(v, 8) for k, v in b.items()} for lam, b in plan["bloch"].items()},
        "scores": {},
        "runs": {},
    }
    for lam in plan["lams"]:
        free = _load(P[f"lat_l{lam:g}_free"])
        ym_lam = float(free["y_mask"]) / lam
        assert (
            abs(ym_lam - plan["y_mask_ref"] / main_lam) < 0.01
        ), f"beam half-width differs from the reference at lam={lam}"
        pre = f"lat_l{lam:g}_"
        names = [t[len(pre) : -len("_o12")] for t in P if t.startswith(pre) and t.endswith("_o12")]
        for name in sorted(names):
            r12 = _load(P[f"{pre}{name}_o12"])
            r1 = _load(P[f"{pre}{name}_o1"]) if f"{pre}{name}_o1" in P else None
            key = f"lam{lam:g}_{name}"
            meta["scores"][key] = score(r12, r1, free, ref["12"], ref["1"], ref["free"], lam, main_lam, g0.d)
            meta["scores"][key]["slit_dy"] = round(_shift(r12) / A_CELL, 4)
            meta["runs"][key] = {
                k: (float(r12[k]) if k in r12 and np.ndim(r12[k]) == 0 else None)
                for k in (
                    "closure",
                    "left_frac",
                    "left_tank_frac",
                    "screen_purity",
                    "screen_lowfreq",
                    "lockin_late",
                    "open_bonds",
                    "cut_bonds",
                    "n_nodes",
                    "n_steps",
                )
            }
        meta["runs"][f"lam{lam:g}_free"] = {
            k: float(free[k])
            for k in ("closure", "left_frac", "left_tank_frac", "left_near_seed_frac", "lockin_late", "n_nodes")
        }
        # incident wave: wavenumber measured off the field, and the wall's normal-incidence reflection
        m = (np.abs(free["ys"]) < 6) & (np.abs(free["zs"] - free["z_wall"]) < 1.5 * lam)
        o = np.argsort(free["zs"][m])
        slope = np.polyfit(free["zs"][m][o], np.unwrap(np.angle(free["acc"][m][o])), 1)[0]
        meta["runs"][f"lam{lam:g}_free"]["k_measured_over_k0"] = round(abs(slope) / (2 * np.pi / lam), 6)
        r12 = _load(P[f"lat_l{lam:g}_nat_o12"])
        k0 = 2 * np.pi / lam
        sgn = np.sign(slope)  # incident field ~ exp(i sgn k z) in the lock-in convention
        mi = (np.abs(free["ys"]) < 20) & (np.abs(free["zs"] - free["z_wall"]) < 1.0 * lam)
        a_inc = np.mean(free["acc"][mi] * np.exp(-1j * sgn * k0 * (free["zs"][mi] - free["z_wall"])))
        mw = (np.abs(r12["ys"]) < 20) & (r12["zs"] < r12["z_wall"]) & (r12["zs"] > r12["z_wall"] - 1.5 * lam)
        zz = r12["zs"][mw] - r12["z_wall"]
        refl = r12["acc"][mw] / a_inc - np.exp(1j * sgn * k0 * zz)
        G = complex(np.mean(refl * np.exp(1j * sgn * k0 * zz)))
        meta["runs"][f"lam{lam:g}_nat"]["wall_reflection"] = [round(G.real, 4), round(G.imag, 4)]
        dlt = short_plane_offset(float(r12["z_wall"]))
        meta["runs"][f"lam{lam:g}_nat"]["short_plane_offset_l_node"] = round(dlt, 4)
        meta["runs"][f"lam{lam:g}_nat"]["short_plane_phase_2k_delta"] = round(abs(2 * k0 * dlt), 4)
        meta["runs"][f"lam{lam:g}_nat"]["wall_reflection_phase"] = round(abs(np.angle(-G)), 4)
        # receipt: the screen readout applied to the reference sampled at THIS lambda's own screen tanks
        ygr = np.linspace(-8.75, 8.75, 2801)
        sl = np.abs(r12["zs"] - r12["z_scr"]) < 1e-3
        dl_ = float(r12["z_scr"] - r12["z_wall"]) / lam
        I_ex_ = ref_screen(ref["12"], ref["free"], dl_, ygr, main_lam)
        from scipy.interpolate import CubicSpline

        I_rd_ = _loess(r12["ys"][sl] / lam, CubicSpline(ygr, I_ex_)(r12["ys"][sl] / lam), ygr, 1.5 / lam)
        prb, _, _ = _pair(_extrema(ygr, I_rd_, 7.8), _extrema(ygr, I_ex_, 7.8))
        meta["receipts"][f"readout_bias_max_pct_lam{lam:g}"] = round(max(abs(100 * (a - b) / b) for a, b, _ in prb), 3)
    meta["reference"] = {"ppw": int(ref["12"]["ppw"]), "y_mask_over_lam": round(plan["y_mask_ref"] / main_lam, 5)}
    # receipt: the reference at half resolution moves the near-field extrema by at most this much
    half = plan["ref_ppw"] // 2
    rh = {o: _load(P[f"ref_l{main_lam:g}_p{half}_o{o}"]) for o in ("free", "12")}
    yg = np.linspace(-8.75, 8.75, 2801)
    pr, _, _ = _pair(
        _extrema(yg, ref_screen(rh["12"], rh["free"], g0.D, yg, main_lam), 7.8),
        _extrema(yg, ref_screen(ref["12"], ref["free"], g0.D, yg, main_lam), 7.8),
    )
    meta["reference"]["extrema_shift_pct_vs_half_ppw"] = round(max(abs(100 * (a - b) / b) for a, b, _ in pr), 3)
    prd, _, _ = _pair(
        _extrema(yg, ref_dose(rh["12"], rh["free"], yg, main_lam), 7.8),
        _extrema(yg, ref_dose(ref["12"], ref["free"], yg, main_lam), 7.8),
    )
    meta["reference"]["dose_extrema_shift_pct_vs_half_ppw"] = round(max(abs(100 * (a - b) / b) for a, b, _ in prd), 3)
    # receipt: the screen readout itself, applied to the EXACT intensity sampled at the lattice's own screen tanks
    r12 = _load(P[f"lat_l{main_lam:g}_nat_o12"])
    sl = np.abs(r12["zs"] - r12["z_scr"]) < 1e-3
    d_lam = float(r12["z_scr"] - r12["z_wall"]) / main_lam
    I_ex = ref_screen(ref["12"], ref["free"], d_lam, yg, main_lam)
    from scipy.interpolate import CubicSpline

    samp = CubicSpline(yg, I_ex)(r12["ys"][sl] / main_lam)
    I_rd = _loess(r12["ys"][sl] / main_lam, samp, yg, 1.5 / main_lam)
    pr, _, _ = _pair(_extrema(yg, I_rd, 7.8), _extrema(yg, I_ex, 7.8))
    meta["receipts"]["readout_bias_max_pct"] = round(
        max(
            [abs(100 * (a - b) / b) for a, b, _ in pr]
            + [v for k, v in meta["receipts"].items() if k.startswith("readout_bias_max_pct_")]
        ),
        3,
    )
    # receipt for the bar history: Rayleigh-Sommerfeld / Kirchhoff (uniform aperture field) against the exact solution
    meta["reference"]["kirchhoff_vs_exact_pct"] = kirchhoff_vs_exact(g0, I_ex, yg, d_lam)
    # receipt: two line sources at the slit centres (distance and 1/sqrt(r) only) -- what distance alone does to V
    r1 = np.hypot(yg + g0.d / 2, d_lam)
    r2 = np.hypot(yg - g0.d / 2, d_lam)
    I_ps = np.abs(np.exp(2j * np.pi * r1) / np.sqrt(r1) + np.exp(2j * np.pi * r2) / np.sqrt(r2)) ** 2
    meta["reference"]["point_source_visibility"] = round(float(_visibility(yg, I_ps)), 5)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / META_NAME).write_text(json.dumps(meta, indent=1, sort_keys=True) + "\n")
    return meta


# =============================================================================
# RENDER PASS (presentation only; reads the cached runs and ts_meta.json)
# =============================================================================
W, H, DPI, FPS = 1920, 1080, 100, 30
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
TITLE_Y, SUB_Y = 0.955, 0.915
CAP_TOP = 0.255
FOOTER = (
    "ENGINE: srs slab (degree 3, chiral I4$_1$32), Op5 scatter–connect, one polarization (bit-identical to "
    "vector_tlm_step, optical activity OFF) · cold & linear, S(A) = 1\n"
    "BOUNDARIES (driver-added): shorted bonds form the screen · graded absorbers + matched edges · "
    "energy closes to {clo:.0e}.   REFERENCE: 2D wave equation, converged, independent code.   SHOWN: port-sum, sector open."
)


def new_fig():
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, layout="none")
    fig.patch.set_facecolor("white")
    return fig


def rgb(fig) -> bytes:
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    for t in fig.texts:  # no on-frame text may run off the frame
        bb = t.get_window_extent(rend)
        assert bb.x0 >= 0 and bb.x1 <= W - 4, f"text overflows the frame ({bb.x1:.0f} px): {t.get_text()[:60]!r}"
    buf = np.asarray(fig.canvas.buffer_rgba())
    assert buf.shape[0] == H and buf.shape[1] == W, buf.shape
    return buf[:, :, :3].tobytes()


def header(fig, title: str, sub: str = ""):
    fig.text(0.02, TITLE_Y, title, fontsize=26, weight="bold", ha="left", va="center")
    if sub:
        fig.text(0.02, SUB_Y, sub, fontsize=15, color=GREY, ha="left", va="center")


def footer(fig, meta):
    clo = max(abs(r["closure"] - 1.0) for r in meta["runs"].values())
    fig.text(0.02, 0.035, FOOTER.format(clo=clo), fontsize=10.5, color=GREY, ha="left", va="center", linespacing=1.5)


def caption(fig, lines, top=CAP_TOP, x=0.02, size=15.5):
    """Each caption line in black, its grade tag in small grey beneath it."""
    y = top
    for text, tag in lines:
        fig.text(x, y, text, fontsize=size, ha="left", va="top")
        y -= 0.032
        if tag:
            fig.text(x + 0.012, y, f"[{tag}]", fontsize=11.5, color=GREY, ha="left", va="top")
            y -= 0.028
        y -= 0.006


class View:
    """Everything the scenes read: the main run (frames), the reference, the sweep."""

    def __init__(self, meta):
        self.meta = meta
        paths = json.loads((CACHE_DIR / "paths.json").read_text())
        self.paths = paths
        g = meta["geometry"]
        self.g = g
        self.lam = g["lam"]
        lam = self.lam
        self.main = _load(paths[f"lat_l{lam:g}_nat_o12"])
        self.free = _load(paths[f"lat_l{lam:g}_free"])
        ppw = meta["reference"]["ppw"]
        self.ref = {o: _load(paths[f"ref_l{lam:g}_p{ppw}_o{o}"]) for o in ("free", "12", "1")}
        self.sc = meta["scores"][f"lam{lam:g}_nat"]
        fr = self.main["frames"].astype(np.float32)
        self.frames = fr
        self.steps = self.main["steps"]
        self.extent = self.main["extent"]
        self.z_wall = float(self.main["z_wall"])
        self.z_scr = float(self.main["z_scr"])
        # colour range = the incident packet's displayed peak: upstream columns, before the packet centre is within
        # 2 lambda of the wall (so the reflected wave has not yet piled onto it)
        zc = np.linspace(self.extent[0], self.extent[1], fr.shape[2]) - self.z_wall
        early = self.steps / np.sqrt(3.0) < (g["up"] / 2 - 2.0) * lam
        self.a_inc = float(np.abs(fr[early][:, :, zc < -1.0 * lam]).max())
        self.clip = self.a_inc


def _wall_segments(ax, v, lw=3.0):
    """Draw the screen (wall) as solid segments with the two slit gaps, in lambda units from the wall."""
    g = v.g
    yl = g["y_in"]
    gaps = sorted(
        [(-g["d"] / 2 - g["w"] / 2, -g["d"] / 2 + g["w"] / 2), (g["d"] / 2 - g["w"] / 2, g["d"] / 2 + g["w"] / 2)]
    )
    edges = [-yl] + [e for gp in gaps for e in gp] + [yl]
    for a, b in zip(edges[0::2], edges[1::2]):
        ax.plot([0, 0], [a, b], color="k", lw=lw, solid_capstyle="butt", zorder=5)


def field_axes(fig, v, rect):
    ax = fig.add_axes(rect)
    z_lo, z_hi, y_lo, y_hi = (v.extent - np.array([v.z_wall, v.z_wall, 0, 0])) / v.lam
    im = ax.imshow(
        v.frames[0],
        origin="lower",
        extent=[z_lo, z_hi, y_lo, y_hi],
        cmap=CMAP,
        vmin=-v.clip,
        vmax=v.clip,
        aspect="equal",
        interpolation="bilinear",
    )
    _wall_segments(ax, v)
    ds = (v.z_scr - v.z_wall) / v.lam
    ax.axvline(ds, color=OI["green"], lw=2.0, ls="--", zorder=5)
    ax.text(ds - 0.25, y_hi - 0.5, "screen", color=OI["green"], fontsize=12, ha="right", va="top", weight="bold")
    ax.set_xlabel(r"distance past the wall  $z/\lambda$", fontsize=13)
    ax.set_ylabel(r"$y/\lambda$", fontsize=13)
    ax.tick_params(labelsize=11)
    return ax, im


def inset_axes(fig, v, rect):
    ax = fig.add_axes(rect)
    P = v.main["inset_pos"]
    B = v.main["inset_bonds"]
    K = v.main["inset_kind"]
    yz = np.c_[(P[:, 1] - v.z_wall), P[:, 0]]
    cols = {0: "#9A9A9A", 1: OI["blue"], 2: OI["verm"]}
    for kind in (0, 1, 2):
        segs = [[yz[a], yz[b]] for (a, b), kk in zip(B, K) if kk == kind]
        if segs:
            ax.add_collection(LineCollection(segs, colors=cols[kind], linewidths=3.0 if kind else 1.0, zorder=2 + kind))
    sc = ax.scatter(
        yz[:, 0],
        yz[:, 1],
        c=v.main["inset_v"][0],
        cmap=CMAP,
        vmin=-v.clip,
        vmax=v.clip,
        s=30,
        edgecolors="none",
        zorder=6,
    )
    bx = v.main["inset_box"]
    ax.set_xlim(bx[2] - v.z_wall, bx[3] - v.z_wall)
    ax.set_ylim(bx[0], bx[1])
    ax.axvline(0, color="k", lw=1.0, ls=":", zorder=1)
    ax.set_aspect("equal")
    ax.set_xlabel(f"z past the wall [{LN}]", fontsize=12)
    ax.set_ylabel(f"y [{LN}]", fontsize=12)
    ax.tick_params(labelsize=10)
    return ax, sc


def colour_key(fig, v, rect):
    cax = fig.add_axes(rect)
    sm = plt.cm.ScalarMappable(cmap=CMAP, norm=plt.Normalize(-v.clip, v.clip))
    cb = fig.colorbar(sm, cax=cax, orientation="horizontal")
    cb.set_ticks([-v.clip, 0, v.clip])
    cb.set_ticklabels([r"$-A_{inc}$", "0 (quiescent)", r"$+A_{inc}$"])
    cb.ax.tick_params(labelsize=10.5)
    cb.set_label("tank voltage;  $A_{inc}$ = the incident packet's displayed peak", fontsize=11)


def _loess_operator(y, yg, sig):
    """The LOESS readout as a matrix L (len(yg) x len(y)): curve = L @ values (linear in the values)."""
    dy = y[None, :] - yg[:, None]
    wk = np.exp(-0.5 * (dy / sig) ** 2)
    m = [np.sum(wk * dy**j, axis=1) for j in range(5)]
    M = np.stack(
        [np.stack([m[0], m[1], m[2]], -1), np.stack([m[1], m[2], m[3]], -1), np.stack([m[2], m[3], m[4]], -1)], -2
    )
    row = np.linalg.inv(M)[:, 0, :]  # first row of M^-1 per grid point
    return wk * (row[:, 0:1] + row[:, 1:2] * dy + row[:, 2:3] * dy**2)


def sweep_stats(m: dict, lam: float) -> dict:
    """Near/far-field scores over the 16 sweep placements of one lambda (the video's own placement excluded: it
    coincides with one of them). 'met' = both near-field readouts within the 2 % bar."""
    ks = sorted(k for k in m["scores"] if k.startswith(f"lam{lam:g}_") and not k.endswith("_nat"))
    sc = [m["scores"][k] for k in ks]
    one = [x["two"]["max_abs_err_pct"] for x in sc]
    dose = [x["dose"]["max_abs_err_pct"] for x in sc]
    far = [max(abs(e) for e in x["far"]["err_vs_exact_pct"] + x["far"]["err_vs_exact_pct_neg_side"]) for x in sc]
    vis = [abs(x["two"]["V_lat"] / x["two"]["V_exact"] - 1) * 100 for x in sc]
    signs = [e for x in sc for e in x["two"]["err_pct"] + x["two"]["err_pct_neg_side"] + x["dose"]["err_pct"]]
    return {
        "keys": ks,
        "n": len(ks),
        "one": (min(one), max(one)),
        "dose": (min(dose), max(dose)),
        "met": sum(1 for a, b in zip(one, dose) if a <= 2 and b <= 2),
        "far": max(far),
        "far_met": sum(1 for f in far if f <= 2),
        "vis": max(vis),
        "vis_met": sum(1 for x in vis if x <= 2),
        "unpaired": sum(x["two"]["unpaired"] + x["dose"]["unpaired"] for x in sc),
        "inward": sum(1 for e in signs if e < 0),
        "n_err": len(signs),
    }


# ----------------------------- S0 title -----------------------------
def scene_title(v):
    m = v.meta
    fig = new_fig()
    fig.text(0.5, 0.66, "Two slits in the srs lattice", fontsize=46, weight="bold", ha="center")
    fig.text(
        0.5,
        0.58,
        "a wave in the engine's T1.1 channel, scored against a converged 2D wave-equation solution",
        fontsize=25,
        color=GREY,
        ha="center",
    )
    n = int(m["runs"][f"lam{v.lam:g}_nat"]["n_nodes"])
    fig.text(
        0.5,
        0.43,
        f"Dynamics: engine output, unedited — {n:,} tanks, {int(m['runs'][f'lam{v.lam:g}_nat']['n_steps'])} steps.  "
        f"Wavelength = {v.lam:g} bond lengths.\nShown: the port-sum tank voltage (canon's A\u2081 grade; its physical "
        "sector is open).  Cold & linear, S(A) = 1; one polarization; optical activity off.\n"
        "Every measured number on frame is read from ts_meta.json; every caption line carries a grade.",
        fontsize=17,
        ha="center",
        linespacing=1.7,
    )
    fig.text(
        0.5,
        0.2,
        "INTERNAL REVIEW BUILD — corpus ids kept on frame for audit; a public cut strips them",
        fontsize=14,
        color=OI["verm"],
        ha="center",
    )
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(4.5 * FPS)):
        yield frame


# ----------------------------- S1 setup -----------------------------
def scene_setup(v):
    m, g = v.meta, v.g
    fig = new_fig()
    header(fig, "The set-up", "a slab of the srs crystal, two slits cut into a screen of shorted bonds")
    ax = fig.add_axes([0.05, 0.33, 0.50, 0.55])
    _wall_segments(ax, v, lw=4)
    z0 = -g["up"] / 2
    zz = np.linspace(z0 - 3 * g["sig_z"], z0 + 3 * g["sig_z"], 1200)
    env = np.exp(-0.5 * ((zz - z0) / g["sig_z"]) ** 2)
    ax.imshow(
        (env * np.cos(2 * np.pi * zz))[None, :],
        extent=[zz[0], zz[-1], -g["y_in"], g["y_in"]],
        cmap=CMAP,
        vmin=-1.6,
        vmax=1.6,
        aspect="auto",
        interpolation="bilinear",
        zorder=0,
    )
    ax.axvline(g["D"], color=OI["green"], lw=2.2, ls="--")
    ax.text(
        g["D"] - 0.3, g["y_in"] - 0.4, "screen", color=OI["green"], fontsize=13, ha="right", va="top", weight="bold"
    )
    ax.annotate(
        "", xy=(0.0, -g["y_in"] + 0.8), xytext=(g["D"], -g["y_in"] + 0.8), arrowprops=dict(arrowstyle="<->", lw=1.4)
    )
    ax.text(g["D"] / 2, -g["y_in"] + 1.1, f"D = {g['D']:g} λ", ha="center", fontsize=14)
    ax.annotate("", xy=(1.0, -g["d"] / 2), xytext=(1.0, g["d"] / 2), arrowprops=dict(arrowstyle="<->", lw=1.4))
    ax.text(1.3, 0.0, f"d = {g['d']:g} λ  (centre to centre)", fontsize=14, va="center")
    ax.annotate(
        "",
        xy=(-1.0, g["d"] / 2 - g["w"] / 2),
        xytext=(-1.0, g["d"] / 2 + g["w"] / 2),
        arrowprops=dict(arrowstyle="<->", lw=1.4),
    )
    ax.text(-1.3, g["d"] / 2, f"w = {g['w']:g} λ", fontsize=14, va="center", ha="right")
    ax.text(
        z0,
        g["y_in"] - 0.4,
        "incoming packet →",
        color=OI["blue"],
        fontsize=13,
        ha="center",
        va="top",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=2),
    )
    ax.set_xlim(-g["up"] + 2, g["D"] + 1)
    ax.set_ylim(-g["y_in"], g["y_in"])
    ax.set_aspect("equal")
    ax.set_xlabel(r"$z/\lambda$ (from the wall)", fontsize=13)
    ax.set_ylabel(r"$y/\lambda$", fontsize=13)
    ax.tick_params(labelsize=11)
    ax.text(
        0.01,
        0.015,
        f"SCHEMATIC, to scale; \u03bb = {v.lam:g} bond lengths",
        transform=ax.transAxes,
        fontsize=12,
        color=GREY,
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.85, pad=2),
    )
    ai, sc = inset_axes(fig, v, [0.62, 0.36, 0.35, 0.50])
    sc.set_array(np.zeros(len(v.main["inset_pos"])))
    sc.set_cmap("Greys")
    fig.text(
        0.795, 0.895, "the actual tanks and bonds at the upper slit's outer edge", fontsize=13, color=GREY, ha="center"
    )
    from matplotlib.lines import Line2D

    ai.legend(
        handles=[
            Line2D([], [], color=OI["verm"], lw=2.2, label="shorted bond (the screen)"),
            Line2D([], [], color=OI["blue"], lw=2.2, label="open bond (the slit)"),
            Line2D([], [], color="#B0B0B0", lw=1.0, label="bond"),
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, -0.13),
        ncol=3,
        fontsize=11,
        frameon=False,
    )
    run = m["runs"][f"lam{v.lam:g}_nat"]
    G = run["wall_reflection"]
    caption(
        fig,
        [
            (
                f"A slab of {int(run['n_nodes']):,} tanks, two cells thick along the slits (periodic there).  The screen: "
                f"{int(run['cut_bonds'])} bonds crossing the wall plane, each shorted at its midpoint.",
                f"ENGINE-EXACT geometry (srs, z = 3, I4₁32) · BOUNDARY (driver-added): reflection {G[0]:+.3f}{G[1]:+.3f}i "
                f"· bond = line is MODEL-OF (vocabulary-register.md:958; ωτ = {m['bloch'][f'{v.lam:g}']['w0']:.2f})",
            ),
            (
                f"The packet: the T1.1 one-way seed rule, λ = {v.lam:g} bond lengths, envelope σ = {g['sig_z']:g} λ.  Its "
                f"carrier on the lattice, ω₀ = {m['bloch'][f'{v.lam:g}']['w0']:.5f} rad/step, is the lock-in reference.",
                "ENGINE-EXACT: ω₀ from the Bloch one-step operator; the Grover relation cos ω = μ_max gives "
                + (
                    "the same value"
                    if m["bloch"][f"{v.lam:g}"]["w0"] == m["bloch"][f"{v.lam:g}"]["w_grover"]
                    else f"{m['bloch'][f'{v.lam:g}']['w_grover']:.6f}"
                ),
            ),
        ],
        top=0.235,
    )
    footer(fig, m)
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(9.0 * FPS)):
        yield frame


# ----------------------------- S2 propagation + screen buildup -----------------------------
FIELD_RECT = [0.045, 0.33, 0.40, 0.55]
DOSE_RECT = [0.455, 0.33, 0.13, 0.55]
INSET_RECT = [0.635, 0.40, 0.34, 0.47]


def _dose_axes(fig, v):
    ax = fig.add_axes(DOSE_RECT)
    ax.set_ylim(-v.g["y_in"], v.g["y_in"])
    ax.set_yticklabels([])
    ax.set_xlabel("screen dose\n(÷ incident dose)", fontsize=12)
    ax.tick_params(labelsize=10)
    ax.grid(alpha=0.25)
    return ax


class DoseCurve:
    def __init__(self, v):
        self.yg = np.linspace(-v.g["y_in"], v.g["y_in"], 1201)
        y = v.main["scr_y"] / v.lam
        self.L = _loess_operator(y, self.yg, 1.5 / v.lam)
        self.inc = float(np.mean(v.free["dose"][np.abs(v.free["scr_y"]) < 10]))
        self.final = self.L @ (v.main["dose"] / self.inc)

    def at(self, f, v):
        return self.L @ (v.main["dose_t"][f] / self.inc)


def scene_propagate(v, C):
    m = v.meta
    fig = new_fig()
    header(
        fig,
        "The wave crosses the lattice",
        "tank voltages in one x-cell, smoothed for display (Gaussian, σ = λ/20); one frame per 5 engine steps",
    )
    ax, im = field_axes(fig, v, FIELD_RECT)
    axd = _dose_axes(fig, v)
    dc = DoseCurve(v)
    (ln,) = axd.plot(np.zeros_like(dc.yg), dc.yg, color=OI["blue"], lw=1.8)
    axd.set_xlim(0, 1.08 * dc.final.max())
    ai, sc = inset_axes(fig, v, INSET_RECT)
    fig.text(
        INSET_RECT[0] + INSET_RECT[2] / 2,
        0.895,
        "inset: the tanks at the upper slit's outer edge",
        fontsize=13,
        color=GREY,
        ha="center",
    )
    colour_key(fig, v, [0.645, 0.30, 0.32, 0.022])
    badge = fig.text(0.98, TITLE_Y, "", fontsize=20, ha="right", va="center", family="monospace", color="#222222")
    caption(fig, C["propagate"], top=0.235)
    footer(fig, m)
    n = len(v.steps)
    for f in range(n):
        im.set_data(v.frames[f])
        sc.set_array(v.main["inset_v"][f])
        ln.set_xdata(dc.at(f, v))
        badge.set_text(f"step {int(v.steps[f]):5d}")
        yield rgb(fig)
    last = rgb(fig)
    plt.close(fig)
    for _ in range(int(1.0 * FPS)):
        yield last


# ----------------------------- S3 the verdict on the screen -----------------------------
def scene_screen(v, C):
    m = v.meta
    sc = v.sc
    st = sweep_stats(m, v.lam)
    fig = new_fig()
    header(
        fig,
        "What the screen records, against a converged wave-equation reference",
        f"screen {v.g['D']:g} λ behind the slits; the same geometry solved by independent leapfrog code",
    )
    ax = fig.add_axes([0.07, 0.36, 0.58, 0.52])
    dc = DoseCurve(v)
    yg = dc.yg
    rd = ref_dose(v.ref["12"], v.ref["free"], yg, v.lam)
    band = np.array(
        [lat_dose(_load(v.paths[f"lat_l{v.lam:g}_{k.split('_', 1)[1]}_o12"]), v.free, yg, v.lam) for k in st["keys"]]
    )
    ax.fill_between(
        yg,
        band.min(0),
        band.max(0),
        color=OI["sky"],
        alpha=0.45,
        lw=0,
        zorder=1,
        label=f"srs lattice, range over {st['n']} slit placements",
    )
    ax.plot(yg, rd, color=OI["verm"], lw=3.0, label="2D wave equation, converged reference", zorder=2)
    ax.plot(yg, dc.final, color=OI["blue"], lw=1.6, label="srs lattice, the video's placement", zorder=3)
    ax.set_xlim(-v.g["y_in"], v.g["y_in"])
    ax.set_xlabel(r"position on the screen  $y/\lambda$", fontsize=13)
    ax.set_ylabel("dose ÷ incident dose", fontsize=13)
    ax.tick_params(labelsize=11)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=3, fontsize=11.5, frameon=False)
    ds = sc["dose"]
    tw = sc["two"]
    box = (
        f"the video's placement, vs reference\n  worst extremum {ds['max_abs_err_pct']:.2f} % (dose)\n"
        f"  {tw['max_abs_err_pct']:.2f} % (single frequency)\n"
        f"  visibility {ds['V_lat']:.3f} vs {ds['V_exact']:.3f}\n\n"
        f"all {st['n']} slit placements\n  worst extremum {st['dose'][0]:.1f}–{st['dose'][1]:.1f} % (dose)\n"
        f"  {st['one'][0]:.1f}–{st['one'][1]:.1f} % (single frequency)\n"
        f"  2 % bar met at {st['met']} of {st['n']}"
    )
    fig.text(0.69, 0.86, box, fontsize=15, va="top", ha="left", family="monospace", linespacing=1.45)
    caption(fig, C["screen"], top=0.235)
    footer(fig, m)
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(8.0 * FPS)):
        yield frame


# ----------------------------- S4 far field (lens) -----------------------------
def scene_far(v, C):
    m = v.meta
    fr = v.sc["far"]
    fig = new_fig()
    header(fig, "Through a lens: the far field", "two-beam fringes; dotted lines: the textbook minima (m+½)λ/d")
    ax = fig.add_axes([0.07, 0.36, 0.58, 0.52])
    s = np.linspace(0.0, 0.55, 2201)
    Fl = lat_far(v.main, s, v.lam)
    Ff = ref_far(v.ref["12"], s, v.lam, float(v.main["y_mask"]))
    for mm in [(j + 0.5) / v.g["d"] for j in range(int(0.55 * v.g["d"] - 0.5) + 1)]:
        ax.axvline(mm, color=style.COLORS["muted"], ls=":", lw=1.4, zorder=1)
    ax.semilogy(s, Ff + 1e-7, color=OI["verm"], lw=3.2, label="2D wave equation, converged reference", zorder=2)
    ax.semilogy(s, Fl + 1e-7, color=OI["blue"], lw=1.6, label="srs lattice (this run)", zorder=3)
    ax.set_ylim(1e-6, 2)
    ax.set_xlim(0, 0.55)
    ax.set_xlabel(r"$\sin\theta$   (dotted: textbook minima $(m+\frac{1}{2})\,\lambda/d$)", fontsize=13)
    ax.set_ylabel(r"far field $|\tilde V|^2$ (tank voltage, peak = 1)", fontsize=13)
    ax.tick_params(labelsize=11)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=2, fontsize=12, frameon=False)
    ref_tb = [100 * (a - b) / b for a, b in zip(fr["minima_exact"], fr["minima_textbook"])]
    box = (
        f"lattice minima vs the reference's, %\n  {'  '.join(f'{e:+.2f}' for e in fr['err_vs_exact_pct'])}\n\n"
        f"lattice minima vs (m+1/2)λ/d, %\n  {'  '.join(f'{e:+.2f}' for e in fr['err_vs_textbook_pct'])}\n"
        f"reference minima vs (m+1/2)λ/d, %\n  {'  '.join(f'{e:+.2f}' for e in ref_tb)}\n\n"
        f"depth of the lattice minima\n  {max(fr['depth_lat']):.0e} of the peak or less"
    )
    fig.text(0.69, 0.86, box, fontsize=15, va="top", ha="left", family="monospace", linespacing=1.45)
    caption(fig, C["far"], top=0.235)
    footer(fig, m)
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(8.0 * FPS)):
        yield frame


# ----------------------------- S5 resolution: where the bond-cut slits are too coarse -----------------------------
def scene_resolution(v, C):
    m = v.meta
    fig = new_fig()
    header(
        fig,
        "Where the bond-cut slit edges fall in the crystal",
        "same geometry in units of λ; the wall plane at 4 positions in the cell × the slit pair at 4 offsets along y",
    )
    yg = np.linspace(-v.g["y_in"], v.g["y_in"], 1201)
    for i, lam in enumerate((16.0, 32.0)):
        st = sweep_stats(m, lam)
        ax = fig.add_axes([0.06 + i * 0.47, 0.43, 0.42, 0.36])
        free = _load(v.paths[f"lat_l{lam:g}_free"])
        for j, key in enumerate(st["keys"]):
            run = _load(v.paths[f"lat_l{lam:g}_{key.split('_', 1)[1]}_o12"])
            ax.plot(
                yg,
                lat_screen(run, free, yg, lam),
                color=OI["blue"],
                lw=0.8,
                alpha=0.45,
                label=f"srs lattice, {st['n']} placements" if j == 0 else None,
            )
        d_lam = m["scores"][st["keys"][0]]["D_over_lam"]
        ax.plot(
            yg,
            ref_screen(v.ref["12"], v.ref["free"], d_lam, yg, v.lam),
            color=OI["verm"],
            lw=2.4,
            zorder=3,
            label="converged reference",
        )
        ax.set_xlim(-v.g["y_in"], v.g["y_in"])
        ax.set_xlabel(r"screen position $y/\lambda$", fontsize=12)
        ax.set_ylabel(r"$|\hat V|^2/|\hat V_{inc}|^2$ (single frequency)", fontsize=12)
        ax.tick_params(labelsize=10)
        fig.text(
            0.06 + i * 0.47,
            0.885,
            f"λ = {lam:g} bond lengths  (slit = {lam * v.g['w']:g} bonds wide)",
            fontsize=15,
            weight="bold",
            ha="left",
        )
        fig.text(
            0.06 + i * 0.47,
            0.862,
            f"near field: worst extremum {st['one'][0]:.1f}–{st['one'][1]:.1f} % (single freq.), "
            f"{st['dose'][0]:.1f}–{st['dose'][1]:.1f} % (dose)\n"
            f"2 % bar met at {st['met']} of {st['n']} placements;  far field within {st['far']:.2f} % of the reference",
            fontsize=13,
            ha="left",
            va="top",
            linespacing=1.5,
        )
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=10, frameon=False)
    caption(fig, C["resolution"], top=0.235)
    footer(fig, m)
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(11.0 * FPS)):
        yield frame


# ----------------------------- S6 ledger -----------------------------
def scene_end(v):
    m, g = v.meta, v.g
    L = f"{v.lam:g}"
    run, fr = m["runs"][f"lam{L}_nat"], m["runs"][f"lam{L}_free"]
    b = m["bloch"][L]
    sc = v.sc
    st16, st32 = sweep_stats(m, 16.0), sweep_stats(m, v.lam)
    clo = max(abs(r["closure"] - 1.0) for r in m["runs"].values())
    fig = new_fig()
    header(fig, "What this is, and what it is not", "provenance ledger for every frame above")
    kmax = max(abs(e) for e in m["reference"]["kirchhoff_vs_exact_pct"]["err_pct"])
    grover = (
        "the Grover relation gives the same value"
        if b["w0"] == b["w_grover"]
        else f"Grover relation: {b['w_grover']:.6f}"
    )
    blocks = [
        (
            "ENGINE-EXACT",
            OI["blue"],
            [
                f"srs slab, {int(run['n_nodes']):,} tanks; Op5 scatter\u2013connect, bit-identical to vector_tlm_step "
                + (
                    "(max |\u0394| = 0, exactly)"
                    if m["receipts"]["operator_identity_max_abs_diff"] == 0
                    else f"(max |\u0394| = {m['receipts']['operator_identity_max_abs_diff']:.0e})"
                )
                + "; tank voltage (2/3) \u03a3 V$_{inc}$ (the port-sum; sector open)",
                f"cold & linear, S(A) = 1; one polarization, optical activity off;  \u03c9\u2080 = {b['w0']:.6f} rad/step "
                f"from the Bloch one-step operator ({grover})",
            ],
        ),
        (
            "BOUNDARIES",
            OI["orange"],
            [
                f"driver-added: the screen = shorted bonds (normal-incidence reflection {run['wall_reflection'][0]:+.3f}"
                f"{run['wall_reflection'][1]:+.3f}i); graded absorbers + matched edges",
                f"energy closes to {clo:.0e};  single-frequency readout converged to {run['lockin_late']:.0e};  "
                f"(engine-derived) wavenumber read off the field: {fr['k_measured_over_k0']:.5f} k\u2080",
            ],
        ),
        (
            "REFERENCE",
            OI["verm"],
            [
                f"2D scalar wave equation, leapfrog, {m['reference']['ppw']} points/\u03bb, grid on the slit edges, Dirichlet "
                "zero-thickness screen; independent code",
                f"halving its resolution moves the near-field extrema \u2264 {m['reference']['extrema_shift_pct_vs_half_ppw']:.1f} %;  "
                f"Kirchhoff theory is off it by up to {kmax:.1f} %",
            ],
        ),
        (
            "SCORES",
            OI["green"],
            [
                f"the video's placement: worst near-field extremum {sc['dose']['max_abs_err_pct']:.2f} % (dose), "
                f"{sc['two']['max_abs_err_pct']:.2f} % (single frequency); 2 % bar "
                + ("met" if max(sc["dose"]["max_abs_err_pct"], sc["two"]["max_abs_err_pct"]) <= 2 else "NOT met"),
                f"{st32['n']} placements at {L} bonds/\u03bb: {st32['one'][0]:.1f}\u2013{st32['one'][1]:.1f} % (single freq.), "
                f"{st32['dose'][0]:.1f}\u2013{st32['dose'][1]:.1f} % (dose): bar met at {st32['met']} of {st32['n']};  "
                f"at 16: met at {st16['met']} of {st16['n']}",
                f"far field: lattice minima within {st32['far']:.2f} % of the reference's at every placement at {L} "
                f"({st16['far']:.2f} % at 16);  readout bias \u2264 {m['receipts']['readout_bias_max_pct']:.2f} %",
            ],
        ),
        (
            "RECEIPTS",
            "#222222",
            [
                f"{fr['left_frac']:.0%} of the seed's energy never leaves: {fr['left_near_seed_frac']:.1%} of it stays within "
                f"\u00b13\u03c3 of where the seed started, only {fr['left_tank_frac']:.2%} of it in the tank-voltage readout;",
                f"consistent with the lattice's flat bands (zero group velocity, zero port-sum: "
                f"{b['flat_frac']:.0%} of port states), matched by these properties, not by projection",
                f"screen signal within \u00b115 % of \u03c9\u2080: {run['screen_purity']:.1%}",
            ],
        ),
        (
            "NOT SHOWN",
            OI["purple"],
            [
                "the moving-defect double slit (a self-transported particle): its transport gate returned ENGINE-GAP",
                "(vol_1_foundations/moving_defect_transport_gate.py:8); it must EARN its interference (physics-lineage-map.md:463)",
                "a click-by-click screen was simulated separately, with no defect (2026-06-08);  also not shown: which-path, polarization",
                "OPEN: the sector of the displayed port-sum channel, inside an engine labelled transverse-only (as in Visual 3)",
            ],
        ),
        (
            "CAUTION",
            "#222222",
            [
                "A consistency check, not a discriminator: any medium whose long waves obey the wave equation draws these fringes",
                '(common/claim-quality.md:1382, "AC agreement cannot distinguish"; Hertz\'s razor, common/physics-lineage-map.md:534).',
            ],
        ),
    ]
    y = 0.86
    for name, col, rows in blocks:
        fig.text(0.03, y, name, fontsize=14.5, weight="bold", color=col, ha="left", va="top")
        for r in rows:
            fig.text(0.16, y, r, fontsize=13.0, ha="left", va="top")
            y -= 0.04
        y -= 0.018
    frame = rgb(fig)
    plt.close(fig)
    for _ in range(int(13.0 * FPS)):
        yield frame


def captions(v) -> dict:
    m = v.meta
    L = f"{v.lam:g}"
    st16, st32 = sweep_stats(m, 16.0), sweep_stats(m, v.lam)
    iso = 100 * m["bloch"][L]["isotropy_max_dk_over_k"]
    fr0 = m["scores"][f"lam{L}_nat"]["far"]
    ref_off = max(abs(100 * (a - b) / b) for a, b in zip(fr0["minima_exact"], fr0["minima_textbook"]))
    lat_ref = max(abs(e) for e in fr0["err_vs_exact_pct"])
    kir = [abs(e) for e in m["reference"]["kirchhoff_vs_exact_pct"]["err_pct"]]
    kmin, kmax = min(kir), max(kir)
    return {
        "propagate": [
            (
                "Colour: tank voltage V = (2/3) Σ V$_{inc}$ in one x-cell of the slab, smoothed for display.  Right edge: the "
                "dose (Σ V² over steps) piling up on the screen tanks.",
                "ENGINE-EXACT values · DISPLAY CHOICE: Gaussian smoothing σ = λ/20, colour range ± the incident packet's displayed "
                "peak, dose read by local quadratic regression over 1.5 bond lengths",
            ),
            (
                "Inset: the same voltages on the actual tanks; at the shorted bonds the wave comes back inverted.",
                "ENGINE-EXACT",
            ),
        ],
        "screen": [
            (
                f"Vermillion: the same set-up as the 2D scalar wave equation, solved by independent code at "
                f"{m['reference']['ppw']} points per λ.  Blue: the lattice; shaded: its range over {st32['n']} slit placements.",
                f"REFERENCE · halving its resolution moves these dose extrema by ≤ "
                f"{m['reference']['dose_extrema_shift_pct_vs_half_ppw']:.2f} % (single frequency: "
                f"{m['reference']['extrema_shift_pct_vs_half_ppw']:.2f} %)",
            ),
            (
                "No fitted parameters.  Visibility < 1 even in the reference: the two slits see each screen point at "
                "different angles, where their own patterns differ.",
                f"MEASURED · readout bias ≤ {m['receipts']['readout_bias_max_pct']:.2f} % (the readout applied to the reference) · "
                f"distance differences alone would give visibility {m['reference']['point_source_visibility']:.4f}",
            ),
        ],
        "far": [
            (
                "The angular spectrum of the lattice's own field 2 λ past the wall: what a lens shows at its focal plane.",
                f"ENGINE-DERIVED (Fourier transform of the single-frequency field) · free propagation beyond that plane assumed: "
                f"the lattice's |k| varies ≤ {iso:.2f} % with direction at this λ (Bloch)",
            ),
            (
                f"Uncoupled, symmetric slits put zeros exactly at sin θ = (m+½)λ/d.  Here the reference itself sits up to "
                f"{ref_off:.2f} % off them; the lattice within {lat_ref:.2f} % of the reference.",
                f"TEXTBOOK (uncoupled, symmetric slits) · MEASURED · at all {st32['n']} slit placements: within "
                f"{st32['far']:.2f} % of the reference's",
            ),
        ],
        "resolution": [
            (
                f"The slit edges are only as sharp as the bonds, so where they fall in the crystal matters.  At {L} bond lengths "
                f"per λ the near field meets the 2 % bar at {st32['met']} of {st32['n']} placements.",
                f"MEASURED: 4 wall-plane positions × 4 slit offsets along y, per λ · worst extremum {st32['dose'][1]:.1f} % (dose) "
                f"at {L}, {st16['dose'][1]:.1f} % at 16 · {st32['inward'] + st16['inward']} of "
                f"{st32['n_err'] + st16['n_err']} extremum errors point inward",
            ),
            (
                f"The far field is within {st32['far']:.2f} % of the reference at every placement at {L}.  The near field needs "
                "finer slits than this video has.",
                f"MEASURED · bar restated after the first λ = 16 run failed it: the Kirchhoff reference is itself "
                f"{kmin:.1f}–{kmax:.1f} % off the solver, and the ≥ 0.95 visibility test moved to the far field (README)",
            ),
        ],
    }


def scenes(v):
    C = captions(v)
    return [
        ("title", scene_title(v)),
        ("setup", scene_setup(v)),
        ("propagate", scene_propagate(v, C)),
        ("screen", scene_screen(v, C)),
        ("far", scene_far(v, C)),
        ("resolution", scene_resolution(v, C)),
        ("end", scene_end(v)),
    ]


STILLS = {  # scene -> [(frame index, file name)]: the tracked quick-look renders
    "setup": [(10, "ts_1_setup.png")],
    "propagate": [(150, "ts_2_crossing.png")],
    "screen": [(10, "ts_3_screen_vs_exact.png")],
    "far": [(10, "ts_4_far_field.png")],
    "resolution": [(10, "ts_5_resolution.png")],
}
STILL_WIDTH = 1280


def write_stills(v) -> None:
    from PIL import Image

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, gen in scenes(v):
        want = dict(STILLS.get(name, []))
        if not want:
            continue
        for i, frame in enumerate(gen):
            if i in want:
                img = Image.frombytes("RGB", (W, H), frame)
                img = img.resize((STILL_WIDTH, STILL_WIDTH * H // W), Image.LANCZOS)
                img.save(OUT_DIR / want[i], optimize=True)
            if i >= max(want):
                break
        plt.close("all")
    print("stills ->", OUT_DIR)


def encode_video(v, crf: int) -> None:
    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg not found on PATH; install it or run with --no-video")
    out = OUT_DIR / VIDEO_NAME
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
        "title=Two slits in the srs lattice (internal review build)",
        str(out),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = 0
    for name, gen in scenes(v):
        for frame in gen:
            proc.stdin.write(frame)
            n += 1
        print(f"  scene {name}: done ({n} frames, {n / FPS:.1f} s)", flush=True)
    proc.stdin.close()
    if proc.wait() != 0:
        raise SystemExit("ffmpeg failed")
    print(f"video -> {out}  ({n} frames, {n / FPS:.1f} s)")


def render(meta, args) -> None:
    v = View(meta)
    if args.stills:
        write_stills(v)
    if not args.no_video:
        encode_video(v, args.crf)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--lam", type=float, default=32.0, help="main wavelength [l_node] (32 = validated build)")
    ap.add_argument("--no-sweep", action="store_true", help="skip the wall-registration sweep (quick look only)")
    ap.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 1))
    ap.add_argument(
        "--ref-ppw", type=int, default=128, help="reference resolution, points per wavelength (128 = validated)"
    )
    ap.add_argument("--stills", action="store_true", help="also write the key-frame PNGs")
    ap.add_argument("--no-video", action="store_true", help="skip the MP4 encode")
    ap.add_argument("--render-only", action="store_true", help="re-render from the cached runs and ts_meta.json")
    ap.add_argument("--crf", type=int, default=25, help="x264 quality (lower = larger file); 25 = tracked MP4")
    args = ap.parse_args()
    if args.render_only:
        meta = json.loads((OUT_DIR / META_NAME).read_text())
    else:
        plan = run_all(args.lam, not args.no_sweep, args.workers, args.ref_ppw)
        meta = write_meta(plan, args.lam)
        meta["_paths"] = plan["paths"]
        (CACHE_DIR / "paths.json").write_text(json.dumps(plan["paths"], indent=1))
    print(json.dumps({k: v for k, v in meta.items() if k in ("receipts", "bloch")}, indent=1))
    if args.stills or not args.no_video:
        style.apply()
        render(meta, args)


if __name__ == "__main__":
    main()
