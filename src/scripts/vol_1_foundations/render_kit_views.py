#!/usr/bin/env python3
"""
Render presentation figures of the vacuum-lattice kit (reproducible).

Produces three matplotlib views from the actual builder geometry:
  * joint_xsection.png   — cross-section: bond tip seated in the node socket (press-fit)
  * coordination.png     — one A node with its 4 bonds plugged in + 4 B neighbours (z=4)
  * lattice_L4.png       — the assembled L4 diamond chunk (8 A + 8 B + 14 bonds)

Figures are generated artifacts (written to dist/, gitignored) — this script is the
source of truth. Requires matplotlib + trimesh.

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/render_kit_views.py [--out dist]
"""

from __future__ import annotations

import argparse
import os
import pathlib

os.environ.setdefault("PRINT_MM_PER_L_NODE",
                      os.environ.get("KIT_PRINT_MM_PER_L_NODE", "100"))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.colors as mc  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402
import trimesh  # noqa: E402

import kit_core_diamond as core  # noqa: E402

SQRT3 = np.sqrt(3.0)
LIGHT = np.array([0.3, 0.45, 0.85]); LIGHT /= np.linalg.norm(LIGHT)
A_COL, B_COL, BOND_COL = "#1f6fe0", "#e8743b", "#9aa0a6"


def _coll(m, col):
    tris = m.vertices[m.faces]
    inten = 0.4 + 0.6 * np.clip(np.abs(m.face_normals @ LIGHT), 0, 1)
    base = np.array(mc.to_rgb(col))
    return Poly3DCollection(tris, facecolors=np.clip(inten[:, None] * base, 0, 1), edgecolors="none")


def _box(ax, meshes, pad=1.05):
    v = np.vstack([m.vertices for m in meshes]); c = v.mean(0); r = np.ptp(v, 0).max() / 2 * pad
    ax.set_xlim(c[0] - r, c[0] + r); ax.set_ylim(c[1] - r, c[1] + r); ax.set_zlim(c[2] - r, c[2] + r)
    ax.set_box_aspect((1, 1, 1)); ax.set_axis_off()


def _seat(bond, hat, pitch):
    b = bond.copy()
    b.apply_transform(trimesh.geometry.align_vectors([0, 0, 1.0], hat))
    b.apply_translation(hat * pitch / 2.0)
    return b


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist")
    out = pathlib.Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)

    S = core.key_dims()["S_mm_per_node"]; pitch = SQRT3 * S
    node, nodeB, bond = core.node_body("A"), core.node_body("B"), core.bond(helix=False)
    hats = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], float); hats /= np.linalg.norm(hats[0])

    # 1. joint cross-section
    hat = hats[0]; bs = _seat(bond, hat, pitch)
    nperp = np.cross(hat, [0, 0, 1.0]); nperp /= np.linalg.norm(nperp)
    fig, ax = plt.subplots(figsize=(8, 5), facecolor="white")
    for m, col, lab in ((node, A_COL, "node A (bored solid)"), (bs, "#d11f1f", "seated bond")):
        s = m.section(plane_origin=[0, 0, 0], plane_normal=nperp)
        if s is not None:
            p2 = s.to_2D()[0]
            for e in p2.entities:
                v = p2.vertices[e.points]; ax.plot(v[:, 0], v[:, 1], color=col, lw=2.2)
            ax.plot([], [], color=col, lw=2.2, label=lab)
    ax.set_aspect("equal"); ax.legend(loc="lower left", fontsize=10); ax.grid(alpha=0.3)
    ax.set_title("joint cross-section — bond tip seated in node socket (0.10 mm press-fit)", fontsize=10)
    fig.tight_layout(); fig.savefig(out / "joint_xsection.png", dpi=110, facecolor="white"); plt.close(fig)

    # 2. coordination unit
    fig = plt.figure(figsize=(7, 7), facecolor="white"); ax = fig.add_subplot(111, projection="3d")
    meshes = [node]; ax.add_collection3d(_coll(node, A_COL))
    for h in hats:
        b = _seat(bond, h, pitch); nb = nodeB.copy(); nb.apply_translation(h * pitch)
        ax.add_collection3d(_coll(b, BOND_COL)); ax.add_collection3d(_coll(nb, B_COL)); meshes += [b, nb]
    _box(ax, meshes); ax.view_init(elev=16, azim=-52)
    ax.set_title("z=4 coordination — A node + 4 bonds plugged in + 4 B neighbours", fontsize=10)
    fig.tight_layout(); fig.savefig(out / "coordination.png", dpi=100, facecolor="white"); plt.close(fig)

    # 3. assembled L4
    from ave.core import chiral_lattice as cl
    from generate_vacuum_lattice_stl import finite_crystal_bonds, active_nodes, lattice_pos_to_mm
    from vacuum_lc_geometry import diamond_sublattice
    net = cl.build_diamond_net(4); bonds = finite_crystal_bonds(net); pos = lattice_pos_to_mm(net)
    fig = plt.figure(figsize=(8, 8), facecolor="white"); ax = fig.add_subplot(111, projection="3d")
    meshes = []
    for u in sorted(active_nodes(bonds)):
        st = diamond_sublattice(net, u); nb = (node if st == "A" else nodeB).copy(); nb.apply_translation(pos[u])
        ax.add_collection3d(_coll(nb, A_COL if st == "A" else B_COL)); meshes.append(nb)
    for u, v in bonds:
        d = pos[v] - pos[u]; b = bond.copy()
        b.apply_transform(trimesh.geometry.align_vectors([0, 0, 1.0], d / np.linalg.norm(d)))
        b.apply_translation((pos[u] + pos[v]) / 2.0); ax.add_collection3d(_coll(b, BOND_COL)); meshes.append(b)
    _box(ax, meshes); ax.view_init(elev=18, azim=35)
    ax.set_title("assembled L4 diamond chunk — 8 A + 8 B nodes, 14 bonds (true sqrt(3) pitch)", fontsize=10)
    fig.tight_layout(); fig.savefig(out / "lattice_L4.png", dpi=110, facecolor="white"); plt.close(fig)

    print(f"wrote {out}/joint_xsection.png, coordination.png, lattice_L4.png")


if __name__ == "__main__":
    main()
