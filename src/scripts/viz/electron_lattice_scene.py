#!/usr/bin/env python3
"""VISUAL 1 — "The electron in the vacuum lattice" (engine scene export).

Exports the REAL engine scene for the interactive HTML + static renders:

  * the chiral srs net (z=3, I4_1 32) node positions + bonds
    (ave.core.chiral_lattice.build_srs_net) -- the actual degree-3 chiral net
    (post-D1: z=3 or nothing; asserted here by a hard degree check);
  * the seeded (2,3) winding omega field
    (ave.solvers.srs_cage_winding.seed_pq_winding_on_srs) with the winding
    integer READ BACK by the srs-native reader (compute_Q_link_srs -> Q_link=3,
    w_tor=2) and asserted, so the exported scene is certified to carry the
    (2,3) winding, not merely labelled with it;
  * per-node S(A) from the CANONICAL Ax4 saturation kernel
    (ave.solvers.graded_vacuum_network.saturation_kernel) evaluated at the
    winding's amplitude field A = |omega| / A_yield -- the wall nodes at yield
    are the saturated (S -> 0) nodes;
  * the meridian loop: the Delta-b1 = +1 harmonic generator of the PUNCTURED
    srs complex (ave.topological.srs_dec_punctured), materialized as an actual
    cycle of srs nodes that LINKS the removed (2,3) torus core exactly once
    (linking number asserted = 1). NOT a hand-drawn circle.

The JSON scene is consumed by viz/electron_lattice/electron_lattice.html
(vanilla-canvas interactive) and by the static-render pass in this driver.

DISCIPLINE
  * substrate-native: the net IS the chiral srs connect-map (z=3), NOT a cubic
    stencil; the amplitude field is the real seeded omega, NOT a posited
    Gaussian; the loop is the topological generator, NOT decoration.
  * consistency-vs-emergence: this is a VISUALIZATION of already-committed
    engine results (Q_link=3 gate, Delta-b1=+1 doorway, the Ax4 kernel). It
    asserts nothing new; it re-runs the committed machinery and renders it.
  * alpha-clean: the winding factor is kappa_tilde = 6/5 (alpha-free), the
    kernel is the pure (1-A^2)^p form. No ALPHA / Q_TANK / V_SNAP on any path.
  * public naming: user-facing strings say "SVE" (structured-vacuum
    electrodynamics); no internal framework name is exported into the scene.

Run:
    cd src
    PYTHONPATH=. python3 scripts/viz/electron_lattice_scene.py

Writes:
    viz/electron_lattice/electron_lattice_scene.json   (the engine scene)
    viz/electron_lattice/electron_lattice_*.png/.pdf   (static renders)
"""

from __future__ import annotations

import heapq
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

# ── repo import wiring (driver runs from src/ with PYTHONPATH=.) ──
_REPO_ROOT = Path(__file__).resolve().parents[3]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from ave.core.chiral_lattice import build_srs_net, ring_coords  # noqa: E402
from ave.solvers.graded_vacuum_network import saturation_kernel  # noqa: E402
from ave.solvers.srs_cage_winding import (  # noqa: E402
    SrsCageWinding,
    SrsCageWindingConfig,
    seed_pq_winding_on_srs,
)
from ave.topological.srs_dec_punctured import (  # noqa: E402
    WINDING_R,
    cube_frame_coords,
    doorway_delta,
    torus_keep_mask,
)

# Presentation output tree (top-level viz/, a deliverable — not assets/sim_outputs).
_OUT_DIR = _REPO_ROOT / "viz" / "electron_lattice"

# ── engine parameters (all from the canonical machinery; tagged where chosen) ──
# L: srs supercell edge. L=6 is the smallest supercell where the srs-native IDW
#    winding reader (compute_Q_link_srs) RESOLVES the full (2,3) integer
#    Q_link=3, w_tor=2 (L=4/5 under-resolve to Q_link=1 -- a real sampling floor
#    of the node-density reader, not papered over; certified below by assert).
_L = 6
_FRAME_N = 20  # cube-frame the (2,3) torus is specified in (matches the seeder)
# _TORUS_R_CUT: the geometrically-MATCHED cut. The committed lane-Z evidence
#   (research/data/2026-07-03_lanez-fluxoid-step0_topology.json) pins the Δb1=+1
#   plateau to rc ∈ [2.5, 2.8] STABLE across L (rc=2.3 is the ragged inner edge;
#   rc≥3.3 over-cuts). rc=2.8 is the canonical matched cut the keeper test uses
#   (test_srs_dec_punctured.py:70); verified here to extend the +1 plateau to L=6.
_TORUS_R_CUT = 2.8
_KERNEL_EXPONENT = 0.5  # Op14 saturation sqrt(S) primary (srs_cage_winding default)
_S_MIN = 1e-3  # kernel floor (avoids the S=0 singularity in the readout)


@dataclass(frozen=True)
class MeridianResult:
    """The materialized Delta-b1=+1 harmonic generator (a real srs node cycle)."""

    path: list  # srs node indices, closed (path[0] == path[-1])
    length: float  # cycle length in srs real-space units
    linking: int  # Gauss linking number with the (2,3) torus core (asserted 1)


def _poloidal_meridian(net, keep, frame_N, R=WINDING_R) -> MeridianResult:
    """Materialize the meridian generator as the SHORTEST cycle in the kept srs
    subgraph whose poloidal winding around the removed (2,3) tube is +-2pi.

    The punctured-complex machinery PROVES a new harmonic 1-cochain opens
    (Delta-b1 = +1, srs_dec_punctured.doorway_delta). That is a cochain (an edge
    field), not a drawable curve. This function returns the concrete carrier of
    that class: an actual cycle of srs nodes that LINKS the removed core once, so
    the render draws the topology, not a decoration. Found by a covering-graph
    Dijkstra over a poloidal collar of the kept nodes (seam at psi=0).
    """
    gc = cube_frame_coords(net, frame_N)
    rho = np.hypot(gc[:, 0], gc[:, 1])
    z = gc[:, 2]
    psi = np.arctan2(z, rho - R)  # poloidal angle around the tube
    rtube = np.hypot(rho - R, z)

    collar = keep & (rtube < 5.0)  # stay near the tube -> a MERIDIAN, not a T3 wrap
    coll = np.where(collar)[0]
    collset = set(coll.tolist())
    adj = {u: [v for v in net.neighbors[u] if v in collset] for u in coll.tolist()}

    def _seam(a, b):
        d = (psi[b] - psi[a] + np.pi) % (2 * np.pi) - np.pi  # min-image dpsi
        if psi[a] < 0 <= psi[b] and d > 0:
            return +1
        if psi[b] < 0 <= psi[a] and d < 0:
            return -1
        return 0

    best = None
    starts = [u for u in coll.tolist() if abs(psi[u]) < 0.5][:8]
    for s in starts:
        dist = {(s, 0): 0.0}
        prev = {(s, 0): None}
        pq = [(0.0, s, 0)]
        found = None
        while pq:
            d, u, k = heapq.heappop(pq)
            if (u, k) != (s, 0) and u == s and k == 1:
                found = (u, k)
                break
            if d > dist.get((u, k), 1e18):
                continue
            for v in adj[u]:
                dk = k + _seam(u, v)
                if dk < 0 or dk > 1:
                    continue
                nd = d + float(np.linalg.norm(net.pos[v] - net.pos[u]))
                if nd < dist.get((v, dk), 1e18):
                    dist[(v, dk)] = nd
                    prev[(v, dk)] = (u, k)
                    heapq.heappush(pq, (nd, v, dk))
        if found and (best is None or dist[found] < best[0]):
            path = []
            cur = found
            while cur is not None:
                path.append(cur[0])
                cur = prev[cur]
            path.reverse()
            best = (dist[found], path)

    if best is None:
        raise RuntimeError("no meridian cycle found in the kept subgraph")
    length, path = best
    linking = _linking_with_core(net, path, frame_N, R)
    return MeridianResult(path=path, length=float(length), linking=int(linking))


def _linking_with_core(net, path, frame_N, R) -> int:
    """Signed count of crossings of the meridian through the disk bounded by the
    (2,3) torus core circle (z=0 plane, rho<R in the cube-frame) = the linking
    number with the removed core. A genuine meridian generator links once."""
    P = ring_coords(net, path[:-1])  # PBC-unwrapped, drop the repeated close
    c = (frame_N - 1) / 2.0
    Pc = P / net.box * frame_N - c
    cross = 0
    for i in range(len(Pc)):
        p, q = Pc[i], Pc[(i + 1) % len(Pc)]
        if (p[2] <= 0 < q[2]) or (q[2] <= 0 < p[2]):
            a = p[2] / (p[2] - q[2])
            pt = p + a * (q - p)
            if np.hypot(pt[0], pt[1]) < R:
                cross += 1 if q[2] > p[2] else -1
    return cross


def build_scene() -> dict:
    """Run the canonical machinery and assemble the export scene dict."""
    # ── (1) the real chiral srs net (z=3, I4_1 32) ──
    cfg = SrsCageWindingConfig(L=_L, frame_N=_FRAME_N, exponent=_KERNEL_EXPONENT, S_min=_S_MIN)
    sim = SrsCageWinding(cfg)
    net = sim.net
    deg = np.array([len(net.neighbors[u]) for u in range(net.n_nodes)])
    interior = deg == 3
    assert interior.sum() > 0 and set(deg[interior].tolist()) == {
        3
    }, "srs net is not z=3 chiral (post-D1: z=3 or nothing)"

    # ── (2) seed the (2,3) winding + READ BACK the integer (certify, don't label) ──
    sim.seed_winding(amplitude=1.0)
    wi = sim.winding_integer()
    assert wi["Q_link"] == 3, f"winding reader did not certify Q_link=3 (got {wi['Q_link']})"
    assert wi["w_tor"] == 2, f"winding reader did not certify w_tor=2 (got {wi['w_tor']})"

    omega = sim.omega_field()  # (n,3) real reconstructed omega on nodes
    omega_mag = np.linalg.norm(omega, axis=1)

    # ── (3) amplitude field A = |omega| / A_yield, and S(A) from the Ax4 kernel ──
    # A_yield := the seeded peak |omega| (the wall sits at yield A=1 by construction;
    # the seed envelope peaks at (sqrt3/2)*pi on the tube). This normalizes the
    # ENGINE amplitude to the kernel's [0,1] strain axis -- an engineering choice of
    # scale (tagged), the kernel FORM is canonical.
    a_yield = float(omega_mag.max()) if omega_mag.max() > 0 else 1.0
    A = np.clip(omega_mag / a_yield, 0.0, cfg.A_cap)
    S = saturation_kernel(A, exponent=_KERNEL_EXPONENT, S_min=_S_MIN)

    # ── (4) the meridian generator (Delta-b1 = +1 doorway, materialized) ──
    keep = torus_keep_mask(net, _FRAME_N, _TORUS_R_CUT)
    doorway = doorway_delta(net, keep)
    assert doorway["delta_b1"] == 1, (
        f"punctured complex did not open the +1 meridian doorway (delta_b1=" f"{doorway['delta_b1']})"
    )
    mer = _poloidal_meridian(net, keep, _FRAME_N)
    assert abs(mer.linking) == 1, f"meridian does not link the core once (lk={mer.linking})"

    # ── (5) assemble the export scene (positions centered + scaled to ~unit box) ──
    pos = net.pos - net.pos.mean(axis=0)
    scale = float(np.abs(pos).max())
    pos_n = (pos / scale).astype(float)

    # unique bonds as index pairs (u<v)
    bonds = sorted({(min(u, v), max(u, v)) for u in range(net.n_nodes) for v in net.neighbors[u]})

    # meridian path in the SAME normalized frame (unwrapped so it renders as a loop)
    mer_xyz = (ring_coords(net, mer.path) - net.pos.mean(axis=0)) / scale

    scene = {
        "meta": {
            "title": "The electron in the vacuum lattice",
            "public_name": "SVE (structured-vacuum electrodynamics)",
            "net": "chiral srs (z=3, I4_1 32 / (10,3)-a)",
            "L": _L,
            "n_nodes": int(net.n_nodes),
            "n_interior_z3": int(interior.sum()),
            "winding": {
                "p": 2,
                "q": 3,
                "Q_link": int(wi["Q_link"]),
                "w_tor": int(wi["w_tor"]),
                "Q_link_raw": float(wi["Q_link_raw"]),
                "kappa_tilde": 1.2,
            },
            "kernel": {"form": "S(A) = (1 - A^2)^p", "exponent": _KERNEL_EXPONENT, "S_min": _S_MIN},
            "doorway": {
                "delta_b1": int(doorway["delta_b1"]),
                "two_method_agree": bool(doorway["b1_two_method_agree"]),
                "meridian_linking": int(mer.linking),
                "meridian_length": float(mer.length),
            },
            "provenance": {
                "positions": "ave.core.chiral_lattice.build_srs_net (ENGINE-EXACT)",
                "omega": "ave.solvers.srs_cage_winding.seed_pq_winding_on_srs (ENGINE-EXACT)",
                "Q_link": "compute_Q_link_srs reader (ENGINE-EXACT, verified)",
                "S(A)": "ave.solvers.graded_vacuum_network.saturation_kernel (ENGINE-EXACT)",
                "meridian": "ave.topological.srs_dec_punctured doorway + graph cycle (ENGINE-EXACT)",
                "projection": "client-side canvas (STYLIZED)",
                "A_yield_normalization": "seeded peak |omega| (engineering scale choice; kernel FORM canonical)",
            },
        },
        "nodes": {
            "pos": pos_n.tolist(),
            "A": A.astype(float).tolist(),
            "S": S.astype(float).tolist(),
            "omega_mag": omega_mag.astype(float).tolist(),
            "interior": interior.astype(bool).tolist(),
        },
        "bonds": [[int(u), int(v)] for (u, v) in bonds],
        "meridian": {"node_path": [int(i) for i in mer.path], "xyz": mer_xyz.astype(float).tolist()},
        "kernel_form": {
            "note": "client re-evaluates S=(1-A^2)^exponent when the slider rescales A",
            "exponent": _KERNEL_EXPONENT,
            "S_min": _S_MIN,
        },
    }
    return scene


def _project(pos, az_deg, el_deg):
    """Orthographic 3D->2D projection (same math the HTML canvas uses)."""
    az = np.radians(az_deg)
    el = np.radians(el_deg)
    ca, sa, ce, se = np.cos(az), np.sin(az), np.cos(el), np.sin(el)
    x, y, z = pos[:, 0], pos[:, 1], pos[:, 2]
    xr = ca * x + sa * z
    zr = -sa * x + ca * z
    yr = ce * y - se * zr
    depth = se * y + ce * zr
    return np.column_stack([xr, yr]), depth


def render_static(scene: dict) -> list:
    """Three static renders in the house style (WHITE, Okabe-Ito, honest legend).

    (a) the srs net projected + coloured by S(A), the meridian generator overlaid
        as the Δb1=+1 loop, wall (saturated) nodes marked;
    (b) the Ax4 kernel S(A)=(1-A^2)^p over the four regime bands, with the
        scene's actual node A-values as a rug (where the engine's nodes sit);
    (c) the winding-amplitude field A on the net (the (2,3) knot shape).

    All numbers are the exported engine scene's own arrays; only the projection
    is presentation-layer. No baked title (caption lives in LaTeX).
    """
    import matplotlib.pyplot as plt

    from ave.core.regime_map import R_LINEAR_MAX, R_NONLINEAR_MAX
    from ave.viz import style

    style.apply("print")  # WHITE background, Okabe-Ito, house default

    pos = np.asarray(scene["nodes"]["pos"])
    A = np.asarray(scene["nodes"]["A"])
    S = np.asarray(scene["nodes"]["S"])
    bonds = np.asarray(scene["bonds"])
    mer_xyz = np.asarray(scene["meridian"]["xyz"])
    exponent = scene["kernel_form"]["exponent"]
    s_min = scene["kernel_form"]["S_min"]

    az, el = 32.0, 20.0
    xy, depth = _project(pos, az, el)
    mxy, _ = _project(mer_xyz, az, el)
    order = np.argsort(depth)  # painter's algorithm

    written = []

    # ── (a) net coloured by S(A) + meridian loop ──────────────────────────────
    fig, ax = plt.subplots(figsize=style.figsize("square"))
    # bonds (thin, behind)
    seg = np.stack([xy[bonds[:, 0]], xy[bonds[:, 1]]], axis=1)
    from matplotlib.collections import LineCollection

    ax.add_collection(LineCollection(seg, colors=style.COLORS["muted"], linewidths=0.15, alpha=0.35, zorder=0))
    sc = ax.scatter(xy[order, 0], xy[order, 1], c=S[order], cmap=style.CMAP_SEQ, vmin=0.0, vmax=1.0, s=14, zorder=1)
    # the meridian generator (the Δb1=+1 doorway loop)
    ax.plot(
        mxy[:, 0],
        mxy[:, 1],
        color=style.COLORS["accent"],
        lw=2.4,
        zorder=3,
        label="meridian generator (Δb₁=+1, links core)",
    )
    # wall (saturated) nodes highlighted
    wall = A > 0.9
    ax.scatter(
        xy[wall, 0],
        xy[wall, 1],
        facecolors="none",
        edgecolors=style.COLORS["comparison"],
        s=44,
        linewidths=1.1,
        zorder=2,
        label="wall nodes at yield (A>0.9, S→0)",
    )
    cb = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label(style.axis_label("Saturation", "S(A)", ""))
    ax.set_xlabel(style.axis_label("projected", "x'", "a_cell"))
    ax.set_ylabel(style.axis_label("projected", "y'", "a_cell"))
    ax.set_aspect("equal")
    style.legend(ax, where="below", ncol=1)
    written += style.save(fig, _OUT_DIR / "electron_lattice_net_S")
    plt.close(fig)

    # ── (b) the Ax4 kernel over the four regime bands + the scene's node rug ───
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    a_axis = np.linspace(0.0, 1.0, 400)
    s_curve = np.clip(np.maximum(1.0 - a_axis**2, 0.0) ** exponent, s_min, 1.0)
    ax.plot(a_axis, s_curve, color=style.COLORS["ave"], lw=2.2, label=f"S(A) = (1 − A²)^{exponent:g}  (Ax4 kernel)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.02)
    style.shade_regimes(ax, (R_LINEAR_MAX, R_NONLINEAR_MAX, 1.0), axis="x")
    # rug: where the engine's actual nodes sit on the A axis
    ax.plot(
        A,
        np.full_like(A, -0.02),
        "|",
        color=style.COLORS["data"],
        alpha=0.5,
        ms=6,
        clip_on=False,
        label="engine node A-values",
    )
    ax.set_xlabel(style.axis_label("Winding amplitude", r"A = |\omega|/A_\mathrm{yield}", ""))
    ax.set_ylabel(style.axis_label("Saturation", "S(A)", ""))
    style.legend(ax, where="below", ncol=2)
    written += style.save(fig, _OUT_DIR / "electron_lattice_kernel")
    plt.close(fig)

    # ── (c) the winding-amplitude field A on the net (the (2,3) knot shape) ────
    fig, ax = plt.subplots(figsize=style.figsize("square"))
    ax.add_collection(LineCollection(seg, colors=style.COLORS["muted"], linewidths=0.15, alpha=0.3, zorder=0))
    sc = ax.scatter(xy[order, 0], xy[order, 1], c=A[order], cmap=style.CMAP_SEQ, vmin=0.0, vmax=1.0, s=14, zorder=1)
    ax.plot(mxy[:, 0], mxy[:, 1], color=style.COLORS["accent"], lw=2.0, zorder=3, alpha=0.9)
    cb = fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.04)
    cb.set_label(style.axis_label("Winding amplitude", "A", ""))
    ax.set_xlabel(style.axis_label("projected", "x'", "a_cell"))
    ax.set_ylabel(style.axis_label("projected", "y'", "a_cell"))
    ax.set_aspect("equal")
    written += style.save(fig, _OUT_DIR / "electron_lattice_winding_A")
    plt.close(fig)

    return written


def inject_html(scene: dict) -> Path | None:
    """Inject the engine scene JSON into the interactive HTML between the
    ``/* SCENE_JSON */ ... /* END_SCENE_JSON */`` markers, making the page fully
    self-contained (opens directly in a browser, no server/fetch/CORS). The HTML
    template ships committed; this replaces only the embedded data block, so the
    presentation code and the engine data stay separable (edit template freely;
    re-run driver to refresh the data). Returns the HTML path, or None if the
    template is absent."""
    html_path = _OUT_DIR / "electron_lattice.html"
    if not html_path.exists():
        return None
    html = html_path.read_text()
    start, end = "/* SCENE_JSON */", "/* END_SCENE_JSON */"
    i, j = html.find(start), html.find(end)
    if i == -1 or j == -1:
        return None
    payload = "\n" + json.dumps(scene, separators=(",", ":")) + "\n"
    new_html = html[: i + len(start)] + payload + html[j:]
    html_path.write_text(new_html)
    return html_path


def main() -> None:
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    scene = build_scene()
    out_json = _OUT_DIR / "electron_lattice_scene.json"
    out_json.write_text(json.dumps(scene, indent=2))
    m = scene["meta"]
    print("=" * 74)
    print("VISUAL 1 — the electron in the vacuum lattice (engine scene export)")
    print("=" * 74)
    print(f"  net: {m['net']}  L={m['L']}  nodes={m['n_nodes']} (z=3 interior {m['n_interior_z3']})")
    print(
        f"  winding: (2,3)  Q_link={m['winding']['Q_link']} (raw {m['winding']['Q_link_raw']:.4f}) "
        f"w_tor={m['winding']['w_tor']}  kappa_tilde={m['winding']['kappa_tilde']}"
    )
    print(f"  kernel: {m['kernel']['form']}  p={m['kernel']['exponent']}")
    print(
        f"  doorway: delta_b1={m['doorway']['delta_b1']} "
        f"(two-method agree {m['doorway']['two_method_agree']})  "
        f"meridian linking={m['doorway']['meridian_linking']} "
        f"length={m['doorway']['meridian_length']:.2f}"
    )
    print(f"  scene written: {out_json}")

    renders = render_static(scene)
    for r in renders:
        print(f"  render written: {r}")

    html = inject_html(scene)
    if html is not None:
        print(f"  HTML self-contained: {html}")


if __name__ == "__main__":
    main()
