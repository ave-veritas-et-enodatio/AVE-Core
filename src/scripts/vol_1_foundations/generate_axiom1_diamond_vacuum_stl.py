#!/usr/bin/env python3
"""
Axiom-1 production vacuum lattice — the lattice AVE actually theorizes.

Per eq_axiom_1.tex (D1 adjudication, 2026-06-12):
  * Production net: z=4 DIAMOND (build_diamond_net) — NOT bare srs (chirality instrument).
  * Bipartite FCC: Type A / Type B sublattices (k4_tlm.py K4Lattice3D).
  * Each node: Cosserat micropolar LC oscillator (6+1 modes); EE map:
      A-sublattice cells → capacitive store (E / ε) — cubic tank body
      B-sublattice cells → inductive store (B / μ) — ring-collared tank body
  * Four tetrahedral Op5 ports per node (_DIAMOND_PORTS).
  * Bonds: transmission-line segments between port collars (ℓ_node pitch; L_cell along bond).

This is NOT generic graph tubes. Nodes are AVE_VACUUM_CELL bodies; bonds are TL corridors.

Output:
  assets/3d_models/vacuum_axiom1_diamond_lc_full_lattice.stl
  assets/3d_models/vacuum_axiom1_diamond_lc_with_particles.stl

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_axiom1_diamond_vacuum_stl.py
"""

from __future__ import annotations

import pathlib
import sys

import numpy as np
from stl import mesh as stl_mesh

from ave.core import chiral_lattice as cl

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "vol_2_subatomic"))
from generate_particle_stl import sweep_tube, sweep_tube_open  # noqa: E402

from generate_vacuum_lattice_stl import (  # noqa: E402
    MM_PER_L_NODE_UNIT,
    PRINT_MM_PER_L_NODE,
    active_nodes,
    combine_meshes,
    finite_crystal_bonds,
    lattice_pos_to_mm,
    print_scale_banner,
    write_mesh,
)

from lattice_particle_embed import PARTICLE_ZOO, embed_particles_on_lattice  # noqa: E402

OUT_NAME = "vacuum_axiom1_diamond_lc_full_lattice.stl"
OUT_WITH_PARTICLES = "vacuum_axiom1_diamond_lc_with_particles.stl"
DIAMOND_L = 8

# Particle embed radii as fractions of ℓ_node print pitch [RENDERING]
LEPTON_EMBED_RADIUS = 0.11 * MM_PER_L_NODE_UNIT
BARYON_EMBED_RADIUS = 0.14 * MM_PER_L_NODE_UNIT
ALPHA_EMBED_RADIUS = 0.22 * MM_PER_L_NODE_UNIT

# Geometry as fractions of ℓ_node print pitch [RENDERING — topology from engine]
CELL_A_HALF = 0.085 * MM_PER_L_NODE_UNIT
CELL_B_RADIUS = 0.075 * MM_PER_L_NODE_UNIT
B_RING_MAJOR = 0.11 * MM_PER_L_NODE_UNIT
B_RING_TUBE = 0.022 * MM_PER_L_NODE_UNIT
PORT_LEN = 0.055 * MM_PER_L_NODE_UNIT
PORT_RADIUS = 0.032 * MM_PER_L_NODE_UNIT
TL_RADIUS = 0.026 * MM_PER_L_NODE_UNIT


def diamond_sublattice(net: cl.LatticeNet, node_idx: int) -> str:
    """A = all-even FCC coords; B = all-odd (k4_tlm K4Lattice3D).

    Must use raw lattice indices — centering for print destroys parity.
    """
    a = net.a_cell if net.a_cell else 1.0
    idx = np.round(net.pos[node_idx] / a).astype(int)
    if np.all(idx % 2 == 0):
        return "A"
    if np.all(idx % 2 == 1):
        return "B"
    raise ValueError(f"non-bipartite diamond coord {idx}")


def _box_mesh(center: np.ndarray, half: float) -> stl_mesh.Mesh:
    x0, x1 = center[0] - half, center[0] + half
    y0, y1 = center[1] - half, center[1] + half
    z0, z1 = center[2] - half, center[2] + half
    verts = np.array([
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1],
    ])
    faces = [
        [verts[0], verts[2], verts[1]], [verts[0], verts[3], verts[2]],
        [verts[4], verts[5], verts[6]], [verts[4], verts[6], verts[7]],
        [verts[0], verts[1], verts[5]], [verts[0], verts[5], verts[4]],
        [verts[2], verts[3], verts[7]], [verts[2], verts[7], verts[6]],
        [verts[0], verts[4], verts[7]], [verts[0], verts[7], verts[3]],
        [verts[1], verts[2], verts[6]], [verts[1], verts[6], verts[5]],
    ]
    arr = np.zeros(len(faces), dtype=stl_mesh.Mesh.dtype)
    arr["vectors"] = np.array(faces)
    return stl_mesh.Mesh(arr)


def _sphere_mesh(center: np.ndarray, radius: float, n_lat: int = 14, n_lon: int = 22) -> stl_mesh.Mesh:
    u = np.linspace(0, np.pi, n_lat)
    v = np.linspace(0, 2 * np.pi, n_lon, endpoint=False)
    uu, vv = np.meshgrid(u, v, indexing="ij")
    x = center[0] + radius * np.sin(uu) * np.cos(vv)
    y = center[1] + radius * np.sin(uu) * np.sin(vv)
    z = center[2] + radius * np.cos(uu)
    verts = np.stack([x, y, z], axis=-1)
    faces = []
    for i in range(verts.shape[0] - 1):
        for j in range(verts.shape[1]):
            jn = (j + 1) % verts.shape[1]
            faces.append([verts[i, j], verts[i, jn], verts[i + 1, jn]])
            faces.append([verts[i, j], verts[i + 1, jn], verts[i + 1, j]])
    arr = np.zeros(len(faces), dtype=stl_mesh.Mesh.dtype)
    arr["vectors"] = np.array(faces)
    return stl_mesh.Mesh(arr)


def _port_collar(base: np.ndarray, direction: np.ndarray, length: float, radius: float) -> stl_mesh.Mesh:
    d = direction / (np.linalg.norm(direction) + 1e-12)
    tip = base + d * length
    return sweep_tube_open(np.array([base, tip]), radius, n_radial=14, cap=True)


def _inductive_ring(center: np.ndarray, normal: np.ndarray, major_r: float, tube_r: float) -> stl_mesh.Mesh:
    n = normal / (np.linalg.norm(normal) + 1e-12)
    ref = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(n, ref)) > 0.9:
        ref = np.array([0.0, 1.0, 0.0])
    u = np.cross(n, ref)
    u /= np.linalg.norm(u) + 1e-12
    v = np.cross(n, u)
    t = np.linspace(0, 2 * np.pi, 64, endpoint=False)
    curve = center + major_r * (np.cos(t)[:, None] * u + np.sin(t)[:, None] * v)
    return sweep_tube(curve, tube_r, n_radial=12, twist_turns=0)


def _cell_body_mesh(center: np.ndarray, sublattice: str, bond_dirs: list[np.ndarray]) -> stl_mesh.Mesh:
    parts: list[stl_mesh.Mesh] = []
    if sublattice == "A":
        parts.append(_box_mesh(center, CELL_A_HALF))
        shell = CELL_A_HALF * 1.05
    else:
        parts.append(_sphere_mesh(center, CELL_B_RADIUS))
        # Equatorial L-ring (microrotational / μ store) — plane ⊥ first bond
        n = bond_dirs[0] if bond_dirs else np.array([0, 0, 1.0])
        parts.append(_inductive_ring(center, n, B_RING_MAJOR, B_RING_TUBE))
        shell = CELL_B_RADIUS * 1.08

    for d in bond_dirs:
        du = d / (np.linalg.norm(d) + 1e-12)
        base = center + du * shell
        parts.append(_port_collar(base, du, PORT_LEN, PORT_RADIUS))

    return combine_meshes(parts)


def _port_tip(center: np.ndarray, direction: np.ndarray, sublattice: str) -> np.ndarray:
    d = direction / (np.linalg.norm(direction) + 1e-12)
    shell = CELL_A_HALF * 1.05 if sublattice == "A" else CELL_B_RADIUS * 1.08
    return center + d * (shell + PORT_LEN)


def _tl_bond(p0: np.ndarray, p1: np.ndarray) -> stl_mesh.Mesh:
    return sweep_tube_open(np.array([p0, p1]), TL_RADIUS, n_radial=14, cap=True)


def make_axiom1_diamond_vacuum( L: int = DIAMOND_L) -> tuple[stl_mesh.Mesh, dict]:
    net = cl.build_diamond_net(L)
    bonds = finite_crystal_bonds(net)
    nodes = active_nodes(bonds)
    pos_mm = lattice_pos_to_mm(net)

    # Port directions per node (engine bond_unit, toward neighbors in chunk)
    port_dirs: dict[int, list[np.ndarray]] = {u: [] for u in nodes}
    for u, v in bonds:
        port_dirs[u].append(net.pos[v] - net.pos[u])
        port_dirs[v].append(net.pos[u] - net.pos[v])

    parts: list[stl_mesh.Mesh] = []
    sub_types: dict[int, str] = {}
    for u in nodes:
        st = diamond_sublattice(net, u)
        sub_types[u] = st
        dirs = port_dirs[u]
        parts.append(_cell_body_mesh(pos_mm[u], st, dirs))

    for u, v in bonds:
        du = net.pos[v] - net.pos[u]
        dv = net.pos[u] - net.pos[v]
        p0 = _port_tip(pos_mm[u], du, sub_types[u])
        p1 = _port_tip(pos_mm[v], dv, sub_types[v])
        parts.append(_tl_bond(p0, p1))

    n_a = sum(1 for s in sub_types.values() if s == "A")
    n_b = len(sub_types) - n_a
    bond_mm = float(np.linalg.norm(pos_mm[bonds[0][0]] - pos_mm[bonds[0][1]])) if bonds else 0.0

    meta = {
        "nodes": len(nodes),
        "bonds": len(bonds),
        "sublattice_A": n_a,
        "sublattice_B": n_b,
        "degree": 4,
        "name": "diamond production K4",
        "bond_mm_min": bond_mm,
        "bond_mm_max": bond_mm,
        "finite_chunk": True,
    }
    return combine_meshes(parts), meta


def make_axiom1_diamond_vacuum_with_particles(
    L: int = DIAMOND_L,
) -> tuple[stl_mesh.Mesh, dict]:
    lattice_mesh, meta = make_axiom1_diamond_vacuum(L)
    net = cl.build_diamond_net(L)
    particle_meshes, manifest = embed_particles_on_lattice(
        net,
        scale_mm=MM_PER_L_NODE_UNIT,
        lepton_radius_mm=LEPTON_EMBED_RADIUS,
        baryon_radius_mm=BARYON_EMBED_RADIUS,
        alpha_radius_mm=ALPHA_EMBED_RADIUS,
    )
    combined = combine_meshes([lattice_mesh, *particle_meshes])
    meta = {
        **meta,
        "particles": manifest,
        "particle_count": len(manifest),
    }
    return combined, meta


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[3]
    out_dir = root / "assets" / "3d_models"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("  Axiom-1 PRODUCTION vacuum — diamond LC lattice (single STL)")
    print("=" * 74)
    print_scale_banner()
    print(f"  Lattice: build_diamond_net(L={DIAMOND_L})  |  z=4 tetrahedral Op5 ports")
    print(f"  Node bodies: A-sublattice=C-tank (cube), B-sublattice=L-tank (sphere+ring)")
    print(f"  Bonds: TL corridors between port collars (not center-to-center tubes)")
    print()

    mesh, meta = make_axiom1_diamond_vacuum()
    print(f"  Bipartite: {meta['sublattice_A']} type-A (ε) + {meta['sublattice_B']} type-B (μ) cells")
    write_mesh(mesh, out_dir / OUT_NAME, meta)
    print()

    print("  Embedding particle zoo on spread interior nodes:")
    for key, label, _ in PARTICLE_ZOO:
        print(f"    · {label}")
    mesh_p, meta_p = make_axiom1_diamond_vacuum_with_particles()
    write_mesh(mesh_p, out_dir / OUT_WITH_PARTICLES, meta_p)
    for entry in meta_p["particles"]:
        c = entry["center_mm"]
        print(
            f"      {entry['particle']:8s} → node {entry['node']:3d}  "
            f"at ({c[0]:+.0f}, {c[1]:+.0f}, {c[2]:+.0f}) mm"
        )
    print()
    print("  This is the D1 production substrate. srs showpiece = chirality instrument only.")
    print("  Particle meshes = topology demos [RENDERING]; see ACCURATE_SCALING.md.")


if __name__ == "__main__":
    main()
