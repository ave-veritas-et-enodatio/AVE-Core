#!/usr/bin/env python3
"""
Axiom-1 chiral vacuum lattice — single flagship showpiece STL.

ONE file that shows the FULL interconnected lattice with VISIBLE chirality.

Why straight-strut STLs hide chirality
---------------------------------------
* **Production diamond K4** (D1 adjudication) is achiral Fd-3m — no handedness to see.
* **Chirality** lives on the **srs** Sunada-K4 net (I4₁32) + the **Cosserat micropolar ω**
  sector (A1a: 3 microrotational DOF alongside 3 translational). The translational skeleton
  alone is mirror-symmetric under straight cylinders; ω is the "hard" part.

This showpiece (100 % engine-isomorphic on the graph; micropolar ribs are labeled RENDERING)
  GRAPH     build_srs_net(L=3, right) — 215 nodes, 270 finite NN bonds
  E-channel thick straight struts along exact bond vectors (LC / translational carrier)
  B-channel helical ribbons on every bond — ω micropolar visualization, twist sign from
            cl.net_ring_writhe() (Smoke-B discriminator; flips for left enantiomorph)
  3-port asymmetric turbine caps at nodes (degree-3, not 4-fold diamond)

Corpus anchors: chiral_lattice.py, L0-axioms A1b/T1.5, engine-capability-map srs grid,
trampoline-framework Step 2 frozen buckling chirality.

Output:
  assets/3d_models/vacuum_axiom1_chiral_micropolar_full_lattice.stl

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_axiom1_lattice_showpiece_stl.py
"""

from __future__ import annotations

import pathlib
import sys

import numpy as np
from stl import mesh as stl_mesh

from ave.core import chiral_lattice as cl
from ave.core.constants import L_NODE

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "vol_2_subatomic"))
from generate_particle_stl import sweep_tube_open  # noqa: E402

from generate_vacuum_lattice_stl import (  # noqa: E402
    BOND_RADIUS_MM,
    MM_PER_L_NODE_UNIT,
    NODE_RADIUS_MM,
    PRINT_MM_PER_L_NODE,
    active_nodes,
    combine_meshes,
    finite_crystal_bonds,
    lattice_pos_to_mm,
    print_scale_banner,
    sphere_mesh,
    write_mesh,
)

OUT_NAME = "vacuum_axiom1_chiral_micropolar_full_lattice.stl"
SRS_L = 3
ENANTIOMORPH = "right"

# Micropolar ω ribbon [RENDERING — makes B-channel visible on Prusa]
MICROPOLAR_TURNS_PER_BOND = 0.62
MICROPOLAR_RIBBON_RADIUS = 0.024 * MM_PER_L_NODE_UNIT
MICROPOLAR_OFFSET = 0.020 * MM_PER_L_NODE_UNIT  # offset from bond axis
TURBINE_BLADE_LEN = 0.11 * MM_PER_L_NODE_UNIT
TURBINE_BLADE_R = 0.016 * MM_PER_L_NODE_UNIT
CORE_BOND_SCALE = 1.15


def _bond_frame(p0: np.ndarray, p1: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    axis = p1 - p0
    length = float(np.linalg.norm(axis))
    if length < 1e-9:
        raise ValueError("degenerate bond")
    t = axis / length
    ref = np.array([0.0, 0.0, 1.0])
    if abs(np.dot(t, ref)) > 0.9:
        ref = np.array([0.0, 1.0, 0.0])
    n = np.cross(t, ref)
    n /= np.linalg.norm(n) + 1e-12
    b = np.cross(t, n)
    b /= np.linalg.norm(b) + 1e-12
    return t, n, b


def _micropolar_helix_curve(
    p0: np.ndarray,
    p1: np.ndarray,
    *,
    sign: float,
    turns: float,
    offset: float,
    n_pts: int = 36,
) -> np.ndarray:
    """Offset helical centerline along bond — ω carrier visualization."""
    t, n, b = _bond_frame(p0, p1)
    s = np.linspace(0.0, 1.0, n_pts)
    base = p0[None, :] + s[:, None] * (p1 - p0)[None, :]
    phase = sign * 2.0 * np.pi * turns * s
    lateral = offset * (np.cos(phase)[:, None] * n + np.sin(phase)[:, None] * b)
    return base + lateral


def _sweep_open_twist(
    curve: np.ndarray,
    tube_radius: float,
    *,
    twist_turns: float = 0.0,
    n_radial: int = 14,
) -> stl_mesh.Mesh:
    """Open tube sweep with Frenet-frame torsional twist (micropolar ribbon)."""
    m = len(curve)
    t = np.zeros_like(curve)
    t[0] = curve[1] - curve[0]
    t[-1] = curve[-1] - curve[-2]
    t[1:-1] = curve[2:] - curve[:-2]
    t /= np.maximum(np.linalg.norm(t, axis=1, keepdims=True), 1e-12)

    dt = np.zeros_like(curve)
    dt[0] = t[1] - t[0]
    dt[-1] = t[-1] - t[-2]
    dt[1:-1] = t[2:] - t[:-2]
    proj = np.sum(dt * t, axis=1, keepdims=True)
    n = dt - proj * t
    n_norm = np.linalg.norm(n, axis=1, keepdims=True)
    bad = n_norm.flatten() < 1e-8
    if np.any(bad):
        for i in np.where(bad)[0]:
            ref = np.array([0.0, 0.0, 1.0])
            if abs(t[i, 2]) > 0.9:
                ref = np.array([0.0, 1.0, 0.0])
            nn = np.cross(t[i], ref)
            nn /= np.linalg.norm(nn) + 1e-12
            n[i] = nn
            n_norm[i] = 1.0
    n /= np.maximum(n_norm, 1e-12)
    b = np.cross(t, n)
    b /= np.maximum(np.linalg.norm(b, axis=1, keepdims=True), 1e-12)

    phi = np.linspace(0, 2 * np.pi, n_radial, endpoint=False)
    verts = np.zeros((m, n_radial, 3))
    for i in range(m):
        frac = i / max(m - 1, 1)
        twist = 2.0 * np.pi * twist_turns * frac
        for j in range(n_radial):
            ang = phi[j] + twist
            verts[i, j] = curve[i] + tube_radius * (np.cos(ang) * n[i] + np.sin(ang) * b[i])

    faces = []
    for i in range(m - 1):
        for j in range(n_radial):
            jn = (j + 1) % n_radial
            faces.append([verts[i, j], verts[i, jn], verts[i + 1, jn]])
            faces.append([verts[i, j], verts[i + 1, jn], verts[i + 1, j]])
    arr = np.zeros(len(faces), dtype=stl_mesh.Mesh.dtype)
    arr["vectors"] = np.array(faces)
    return stl_mesh.Mesh(arr)


def _micropolar_ribbon(
    p0: np.ndarray,
    p1: np.ndarray,
    *,
    sign: float,
) -> stl_mesh.Mesh:
    curve = _micropolar_helix_curve(
        p0, p1, sign=sign, turns=MICROPOLAR_TURNS_PER_BOND, offset=MICROPOLAR_OFFSET
    )
    return _sweep_open_twist(
        curve,
        MICROPOLAR_RIBBON_RADIUS,
        twist_turns=sign * MICROPOLAR_TURNS_PER_BOND * 0.35,
        n_radial=14,
    )


def _omega_turbine_cap(
    center: np.ndarray,
    bond_dirs: list[np.ndarray],
    *,
    sign: float,
) -> stl_mesh.Mesh:
    """Asymmetric 3-blade cap — breaks 4-fold symmetry, cues optical-activity source."""
    parts: list[stl_mesh.Mesh] = []
    for k, d in enumerate(bond_dirs):
        d = d / (np.linalg.norm(d) + 1e-12)
        t, n, b = _bond_frame(center, center + d * 10.0)
        lateral = (n * (sign * 0.85) + b * (0.4 * ((-1) ** k))) * MICROPOLAR_OFFSET * 2.5
        tip = center + d * TURBINE_BLADE_LEN + lateral
        mid = center + d * (TURBINE_BLADE_LEN * 0.45) + lateral * 0.6
        curve = np.array([center + lateral * 0.25, mid, tip])
        parts.append(sweep_tube_open(curve, TURBINE_BLADE_R, n_radial=10, cap=True))
    return combine_meshes(parts)


def make_axiom1_showpiece(enantiomorph: str = ENANTIOMORPH) -> tuple[stl_mesh.Mesh, dict]:
    net = cl.build_srs_net(SRS_L, enantiomorph)
    bonds = finite_crystal_bonds(net)
    nodes = active_nodes(bonds)
    pos_mm = lattice_pos_to_mm(net)

    writhe_mean, writhe_std, n_rings, girth = cl.net_ring_writhe(net)
    sign = -1.0 if writhe_mean < 0 else 1.0  # right → negative writhe in engine convention

    parts: list[stl_mesh.Mesh] = []
    hub_r = NODE_RADIUS_MM * 1.35

    for u in nodes:
        parts.append(sphere_mesh(pos_mm[u], hub_r))

    for u, v in bonds:
        p0, p1 = pos_mm[u], pos_mm[v]
        parts.append(
            sweep_tube_open(
                np.array([p0, p1]),
                BOND_RADIUS_MM * CORE_BOND_SCALE,
                n_radial=18,
                cap=True,
            )
        )
        parts.append(_micropolar_ribbon(p0, p1, sign=sign))

    for u in nodes:
        nb_set = {v for a, v in bonds if a == u} | {a for a, v in bonds if v == u}
        dirs = [net.pos[nb] - net.pos[u] for nb in net.neighbors[u] if nb in nb_set]
        if len(dirs) >= 3:
            parts.append(_omega_turbine_cap(pos_mm[u], dirs[:3], sign=sign))

    meta = {
        "name": net.name,
        "handedness": net.handedness,
        "nodes": len(nodes),
        "bonds": len(bonds),
        "writhe_mean": writhe_mean,
        "writhe_std": writhe_std,
        "n_rings": n_rings,
        "girth": girth,
        "chirality_sign": sign,
        "bond_mm": MM_PER_L_NODE_UNIT,
        "finite_chunk": True,
        "bond_mm_min": MM_PER_L_NODE_UNIT,
        "bond_mm_max": MM_PER_L_NODE_UNIT,
    }
    return combine_meshes(parts), meta


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[3]
    out_dir = root / "assets" / "3d_models"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("  Axiom-1 Chiral Vacuum — micropolar showpiece (single STL)")
    print("=" * 74)
    print_scale_banner()
    print(f"  Substrate: srs L={SRS_L} enantiomorph={ENANTIOMORPH} (I4₁32 chiral net)")
    print(f"  Micropolar: {MICROPOLAR_TURNS_PER_BOND:.2f} turns/bond, "
          f"ribbon r={MICROPOLAR_RIBBON_RADIUS:.2f} mm [RENDERING]")
    print()

    mesh, meta = make_axiom1_showpiece(ENANTIOMORPH)
    print(
        f"  Engine writhe: {meta['writhe_mean']:+.4f} ± {meta['writhe_std']:.4f} "
        f"({meta['n_rings']} rings, girth {meta['girth']})"
    )
    print(f"  Twist sign applied to ω ribbons: {meta['chirality_sign']:+.0f}")
    print()

    write_mesh(mesh, out_dir / OUT_NAME, meta)
    print()
    print("  Print THIS file for full lattice + visible chirality.")
    print("  Diamond K4 (production) is achiral — chirality requires srs + micropolar ω.")


if __name__ == "__main__":
    main()
