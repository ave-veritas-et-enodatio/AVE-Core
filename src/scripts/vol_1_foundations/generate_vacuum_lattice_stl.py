#!/usr/bin/env python3
"""
AVE vacuum lattice — engine-isomorphic 3D-printable STL meshes.

Each output is a DIRECT graph isomorphism of a live ``LatticeNet`` from
``ave.core.chiral_lattice``:

  * vertices  = lattice nodes at ``net.pos`` (centered for printing)
  * edges     = ``net.neighbors`` (undirected, no missing/extra bonds)
  * geometry  = straight cylinders along exact engine bond vectors

Two corpus substrates:

  PRODUCTION (Axiom 1 / D1 adjudication):
    ``build_diamond_net(L)`` — degree-4 diamond / engine-"K4", achiral Fd-3m.
    Tetrahedral ports from ``_DIAMOND_PORTS`` (k4_tlm.py), NOT distance heuristic.

  CHIRAL (acceptance / optical-activity instrument):
    ``build_srs_net(L, enantiomorph)`` — degree-3 srs / Sunada-K4 / I4₁32|I4₃32.
    NN graph from executable motif + PBC (girth-10, 120° bonds).

Scale (corpus → Prusa print):
  Physical ℓ_node = ``constants.L_NODE`` ≈ 3.862×10⁻¹³ m (386 fm).
  Topology is engine-exact; absolute size is a RENDERING magnification only.

  Default export: ``PRINT_MM_PER_L_NODE = 25`` mm per ℓ_node
    → L8 diamond ≈ 181 mm cube (fits Prusa MK3/MK4 250×210 mm bed)
    → L3 srs     ≈ 201 mm cube
    → srs NN bond = 25 mm; diamond tetrahedral bond = 25√3 ≈ 43.3 mm

  Reference (legacy particle-STL convention): 10 mm per ℓ_node.

Usage (repo root):
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_stl.py
    PRINT_MM_PER_L_NODE=10 python ...   # smaller desk scale

Outputs (assets/3d_models/):
    vacuum_diamond_k4_L8_network.stl
    vacuum_diamond_k4_L6_network.stl
    vacuum_srs_chiral_L3_right_network.stl
    vacuum_srs_chiral_L3_left_network.stl
    vacuum_diamond_k4_unit_cell.stl
    vacuum_diamond_k4_unit_cell_with_electron.stl
"""

from __future__ import annotations

import pathlib
import sys

import numpy as np
from stl import mesh as stl_mesh

from ave.core import chiral_lattice as cl
from ave.core.constants import L_NODE
from ave.topological.borromean import FundamentalTopologies

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "vol_2_subatomic"))
from generate_particle_stl import sweep_tube, sweep_tube_open  # noqa: E402

# ── Print scale (override via env PRINT_MM_PER_L_NODE) ──
REFERENCE_MM_PER_L_NODE = 10.0  # legacy particle-STL reference
PRINT_MM_PER_L_NODE = float(__import__("os").environ.get("PRINT_MM_PER_L_NODE", "25"))

MM_PER_L_NODE_UNIT = PRINT_MM_PER_L_NODE
NODE_RADIUS_MM = 0.052 * MM_PER_L_NODE_UNIT  # [RENDERING] ~5% of ℓ_node pitch
BOND_RADIUS_MM = 0.034 * MM_PER_L_NODE_UNIT
ELECTRON_VISUAL_SCALE = 2.5  # [RENDERING]


def combine_meshes(meshes: list[stl_mesh.Mesh]) -> stl_mesh.Mesh:
    if not meshes:
        raise ValueError("no meshes to combine")
    return stl_mesh.Mesh(np.concatenate([m.data for m in meshes]))


def lattice_pos_to_mm(net: cl.LatticeNet) -> np.ndarray:
    """net.pos already includes a_cell; 1 unit = ℓ_node pitch."""
    return (net.pos - net.pos.mean(axis=0)) * MM_PER_L_NODE_UNIT


def sphere_mesh(center: np.ndarray, radius: float, n_lat: int = 14, n_lon: int = 22) -> stl_mesh.Mesh:
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


def bond_mesh(p0: np.ndarray, p1: np.ndarray, radius: float, n_radial: int = 18) -> stl_mesh.Mesh:
    return sweep_tube_open(np.array([p0, p1], dtype=float), radius, n_radial=n_radial, cap=True)


def unique_bonds(net: cl.LatticeNet) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for u in range(net.n_nodes):
        for v in net.neighbors[u]:
            if u < v:
                out.append((u, v))
    return out


def finite_crystal_bonds(net: cl.LatticeNet, *, tol: float = 1.08) -> list[tuple[int, int]]:
    """Keep only geometric nearest-neighbour edges (drop PBC wrap-around links).

    The engine LatticeNet is periodic; for a printable finite crystal chunk we
    export the induced subgraph of minimum-length bonds (true NN ≈ ℓ_node for srs,
    √3·ℓ_node along tetrahedral ports for diamond).
    """
    bonds = unique_bonds(net)
    lengths = [float(np.linalg.norm(net.pos[u] - net.pos[v])) for u, v in bonds]
    r_min = min(lengths)
    return [b for b, r in zip(bonds, lengths) if r <= tol * r_min]


def active_nodes(bonds: list[tuple[int, int]]) -> set[int]:
    nodes: set[int] = set()
    for u, v in bonds:
        nodes.add(u)
        nodes.add(v)
    return nodes


def mesh_from_lattice_net(
    net: cl.LatticeNet,
    *,
    node_indices: set[int] | None = None,
    bonds: list[tuple[int, int]] | None = None,
    finite_chunk: bool = True,
    node_radius: float = NODE_RADIUS_MM,
    bond_radius: float = BOND_RADIUS_MM,
) -> stl_mesh.Mesh:
    """Watertight strut mesh isomorphic to a ``LatticeNet`` subgraph."""
    pos_mm = lattice_pos_to_mm(net)
    if bonds is None:
        bonds = finite_crystal_bonds(net) if finite_chunk else unique_bonds(net)

    if node_indices is None:
        node_indices = active_nodes(bonds)

    parts: list[stl_mesh.Mesh] = []
    for u in node_indices:
        parts.append(sphere_mesh(pos_mm[u], node_radius))

    for u, v in bonds:
        if u in node_indices and v in node_indices:
            parts.append(bond_mesh(pos_mm[u], pos_mm[v], bond_radius))

    return combine_meshes(parts)


def lattice_report(net: cl.LatticeNet, label: str, *, finite_chunk: bool = True) -> dict:
    bonds_all = unique_bonds(net)
    bonds = finite_crystal_bonds(net) if finite_chunk else bonds_all
    nodes = active_nodes(bonds)
    pos_mm = lattice_pos_to_mm(net)
    lengths = [float(np.linalg.norm(pos_mm[u] - pos_mm[v])) for u, v in bonds]
    span = pos_mm[list(nodes)].max(axis=0) - pos_mm[list(nodes)].min(axis=0) if nodes else pos_mm.max(axis=0) - pos_mm.min(axis=0)
    return {
        "label": label,
        "name": net.name,
        "handedness": net.handedness,
        "nodes": len(nodes),
        "nodes_engine": net.n_nodes,
        "bonds": len(bonds),
        "bonds_pbc": len(bonds_all),
        "degree": net.degree,
        "bond_mm_min": min(lengths) if lengths else 0.0,
        "bond_mm_max": max(lengths) if lengths else 0.0,
        "bond_mm_mean": float(np.mean(lengths)) if lengths else 0.0,
        "bbox_mm": span,
        "finite_chunk": finite_chunk,
    }


def pick_interior_node(net: cl.LatticeNet) -> int:
    mask = net.interior_mask
    if mask is None or not mask.any():
        return net.n_nodes // 2
    idx = np.where(mask)[0]
    ctr = net.pos.mean(axis=0)
    d = np.linalg.norm(net.pos[idx] - ctr, axis=1)
    return int(idx[np.argmin(d)])


def unit_cell_nodes(net: cl.LatticeNet, center: int) -> set[int]:
    nodes = {center, *net.neighbors[center]}
    return nodes


def electron_torus_mesh(center_mm: np.ndarray) -> stl_mesh.Mesh:
    r_mm = (1.0 / (2.0 * np.pi)) * MM_PER_L_NODE_UNIT * ELECTRON_VISUAL_SCALE
    tube_r = max(r_mm * 0.42, 0.035 * MM_PER_L_NODE_UNIT)
    curve = FundamentalTopologies.generate_unknot_0_1(radius=r_mm, resolution=720) + center_mm
    return sweep_tube(curve, tube_r, n_radial=22)


def print_scale_banner() -> None:
    mag = MM_PER_L_NODE_UNIT / (L_NODE * 1e3)  # mm per metre physical
    print(f"  Corpus ℓ_node     = {L_NODE*1e15:.2f} fm  ({L_NODE:.4e} m)")
    print(f"  Print scale       = {MM_PER_L_NODE_UNIT:.1f} mm per ℓ_node  [RENDERING]")
    print(f"  vs physical       = ×{mag:.3e} magnification (topology unchanged)")
    print(f"  Bond lengths      = srs {MM_PER_L_NODE_UNIT:.1f} mm  |  "
          f"diamond {MM_PER_L_NODE_UNIT * np.sqrt(3):.1f} mm")
    print(f"  Strut radii       = node {NODE_RADIUS_MM:.2f} mm, bond {BOND_RADIUS_MM:.2f} mm")


def write_mesh(mesh: stl_mesh.Mesh, path: pathlib.Path, report: dict | None = None) -> None:
    mesh.save(str(path))
    xs = mesh.vectors.reshape(-1, 3)
    bbox = xs.max(axis=0) - xs.min(axis=0)
    extra = ""
    if report:
        chunk = "finite" if report.get("finite_chunk", True) else "PBC"
        extra = (
            f"  |  {report['nodes']} nodes, {report['bonds']} {chunk} bonds, "
            f"length {report['bond_mm_min']:.1f}–{report['bond_mm_max']:.1f} mm"
        )
    print(
        f"  → {path.name}: {len(mesh.vectors):,} tris, "
        f"bbox {bbox[0]:.1f}×{bbox[1]:.1f}×{bbox[2]:.1f} mm{extra}"
    )


def build_and_export(
    net: cl.LatticeNet,
    label: str,
    filename: str,
    out_dir: pathlib.Path,
    *,
    node_indices: set[int] | None = None,
    finite_chunk: bool = True,
) -> None:
    rep = lattice_report(net, label, finite_chunk=finite_chunk)
    bonds = finite_crystal_bonds(net) if finite_chunk else unique_bonds(net)
    if node_indices is not None:
        bonds = [(u, v) for u, v in bonds if u in node_indices and v in node_indices]
    mesh = mesh_from_lattice_net(
        net, node_indices=node_indices, bonds=bonds, finite_chunk=finite_chunk
    )
    write_mesh(mesh, out_dir / filename, rep)


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[3]
    out_dir = root / "assets" / "3d_models"
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("  AVE Vacuum Lattice — engine-isomorphic STL export")
    print("=" * 74)
    print_scale_banner()
    print(f"  Output: {out_dir}")
    print()

    # ── Production diamond K4 (interconnected 3D networks) ──
    print("  PRODUCTION diamond K4 (build_diamond_net)")
    for L, fname in ((8, "vacuum_diamond_k4_L8_network.stl"), (6, "vacuum_diamond_k4_L6_network.stl")):
        net = cl.build_diamond_net(L)
        build_and_export(net, f"diamond L={L}", fname, out_dir)

    # ── Chiral srs (full interconnected networks, both enantiomorphs) ──
    print("  CHIRAL srs (build_srs_net)")
    for hand, fname in (
        ("right", "vacuum_srs_chiral_L3_right_network.stl"),
        ("left", "vacuum_srs_chiral_L3_left_network.stl"),
    ):
        net = cl.build_srs_net(3, hand)
        build_and_export(net, f"srs L=3 {hand}", fname, out_dir)

    # ── Pedagogical excerpts (still engine subgraphs) ──
    print("  Subgraph excerpts")
    net4 = cl.build_diamond_net(4)
    center = pick_interior_node(net4)
    build_and_export(
        net4,
        "diamond unit cell",
        "vacuum_diamond_k4_unit_cell.stl",
        out_dir,
        node_indices=unit_cell_nodes(net4, center),
    )
    cell_nodes = unit_cell_nodes(net4, center)
    cell_bonds = finite_crystal_bonds(net4)
    cell_bonds = [(u, v) for u, v in cell_bonds if u in cell_nodes and v in cell_nodes]
    cell_mesh = mesh_from_lattice_net(net4, node_indices=cell_nodes, bonds=cell_bonds)
    pos_mm = lattice_pos_to_mm(net4)
    combined = combine_meshes([cell_mesh, electron_torus_mesh(pos_mm[center])])
    rep = lattice_report(net4, "diamond unit cell + electron")
    write_mesh(combined, out_dir / "vacuum_diamond_k4_unit_cell_with_electron.stl", rep)

    print()
    print("  Finite crystal chunks (PBC wrap bonds excluded). Fully interconnected.")
    if MM_PER_L_NODE_UNIT >= 20:
        print("  Prusa MK3/MK4: print L8 diamond (~180 mm) flat or elevated; L3 srs (~200 mm).")
    else:
        print("  Desk scale — set PRINT_MM_PER_L_NODE=25 for Prusa-sized export.")


if __name__ == "__main__":
    main()
