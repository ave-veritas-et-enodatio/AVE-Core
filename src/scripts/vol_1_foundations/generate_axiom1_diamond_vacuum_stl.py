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

Kit parts (separate script):
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
"""

from __future__ import annotations

import pathlib

import numpy as np
from stl import mesh as stl_mesh

from ave.core import chiral_lattice as cl

from generate_vacuum_lattice_stl import (  # noqa: E402
    MM_PER_L_NODE_UNIT,
    active_nodes,
    combine_meshes,
    finite_crystal_bonds,
    lattice_pos_to_mm,
    print_scale_banner,
    write_mesh,
)
from lattice_particle_embed import PARTICLE_ZOO, embed_particles_on_lattice  # noqa: E402
from vacuum_lc_geometry import (  # noqa: E402
    cell_body_mesh,
    diamond_sublattice,
    port_tip,
    tl_bond_mesh,
)

OUT_NAME = "vacuum_axiom1_diamond_lc_full_lattice.stl"
OUT_WITH_PARTICLES = "vacuum_axiom1_diamond_lc_with_particles.stl"
DIAMOND_L = 8

LEPTON_EMBED_RADIUS = 0.11 * MM_PER_L_NODE_UNIT
BARYON_EMBED_RADIUS = 0.14 * MM_PER_L_NODE_UNIT
ALPHA_EMBED_RADIUS = 0.22 * MM_PER_L_NODE_UNIT


def make_axiom1_diamond_vacuum(L: int = DIAMOND_L) -> tuple[stl_mesh.Mesh, dict]:
    net = cl.build_diamond_net(L)
    bonds = finite_crystal_bonds(net)
    nodes = active_nodes(bonds)
    pos_mm = lattice_pos_to_mm(net)

    port_dirs: dict[int, list[np.ndarray]] = {u: [] for u in nodes}
    for u, v in bonds:
        port_dirs[u].append(net.pos[v] - net.pos[u])
        port_dirs[v].append(net.pos[u] - net.pos[v])

    parts: list[stl_mesh.Mesh] = []
    sub_types: dict[int, str] = {}
    for u in nodes:
        st = diamond_sublattice(net, u)
        sub_types[u] = st
        parts.append(cell_body_mesh(pos_mm[u], st, port_dirs[u]))

    for u, v in bonds:
        du = net.pos[v] - net.pos[u]
        dv = net.pos[u] - net.pos[v]
        p0 = port_tip(pos_mm[u], du, sub_types[u])
        p1 = port_tip(pos_mm[v], dv, sub_types[v])
        parts.append(tl_bond_mesh(p0, p1))

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
