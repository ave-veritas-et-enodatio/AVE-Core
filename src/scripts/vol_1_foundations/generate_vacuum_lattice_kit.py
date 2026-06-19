#!/usr/bin/env python3
"""
DIY vacuum lattice kit — separate printable parts + assembly manifest.

Corpus-faithful Axiom-1 diamond K4 kit (D1 production substrate):
  * 2 node molds: Type-A capacitive (ε) + Type-B inductive (μ)
  * 1 TL bond insert (port-tip to port-tip along tetrahedral NN)
  * JSON manifest for finite-crystal assembly at configurable L

Scale presets (KIT_PRINT_MM_PER_L_NODE env — defaults to FDM-friendly, not mnemonic):
  * 100  — kit default (~10.5 mm hex flat-to-flat; Prusa MK3+)
  * 80   — prior scale
  * 60   — compact kit (~3.8 mm port OD)
  * 38.6 — corpus mnemonic only (too fine for most FDM printers)

STLs are exported in print pose (flat/vertical on build plate). Assembly coordinates
in the JSON manifest remain engineering-frame — rotate parts back mentally when placing.

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
    KIT_PRINT_MM_PER_L_NODE=60 ASSEMBLY_L=8 python ...
"""

from __future__ import annotations

import json
import os
import pathlib

from ave.core.constants import L_NODE

# FDM floor: port collar outer radius ≥ this (mm) → ~2× for comfortable peg/socket.
FDM_MIN_PORT_RADIUS_MM = 2.0
_FDM_FRIENDLY_MM = round(FDM_MIN_PORT_RADIUS_MM / 0.060, 1)  # KIT_PORT_RADIUS fraction
_CORPUS_MNEMONIC_MM = round(L_NODE * 1e15 / 10.0, 1)
_KIT_DEFAULT_MM = float(os.environ.get("KIT_PRINT_MM_PER_L_NODE", str(max(_FDM_FRIENDLY_MM, 100.0))))
# Kit scale must be set before geometry modules read PRINT_MM_PER_L_NODE.
os.environ["PRINT_MM_PER_L_NODE"] = os.environ.get("KIT_PRINT_MM_PER_L_NODE", str(_KIT_DEFAULT_MM))

import numpy as np

from ave.core import chiral_lattice as cl

from generate_vacuum_lattice_stl import (  # noqa: E402
    PRINT_MM_PER_L_NODE,
    active_nodes,
    combine_meshes,
    finite_crystal_bonds,
    lattice_pos_to_mm,
    print_scale_banner,
    write_mesh,
)
from vacuum_lc_geometry import (  # noqa: E402
    DIAMOND_CENTER_PITCH_MM,
    DIAMOND_PORT_HATS,
    MM_PER_L_NODE_UNIT,
    KIT_PORT_RADIUS,
    PORT_RADIUS,
    bond_insert_length_mm,
    bond_total_length_mm,
    cell_body_mesh,
    diamond_sublattice,
    joinery_spec,
    kit_bond_insert_mesh,
    kit_node_mesh,
    kit_port_directions,
    kit_port_mouth,
    tl_bond_mesh,
)
from kit_print_pose import (  # noqa: E402
    PRINT_POSE_SPEC,
    orient_bond_for_print,
    orient_node_a_for_print,
    orient_node_b_for_print,
)

ASSEMBLY_L = int(os.environ.get("ASSEMBLY_L", "4"))
KIT_DIR_NAME = "kit"


def _grid_index(net: cl.LatticeNet, node_idx: int) -> list[int]:
    a = net.a_cell if net.a_cell else 1.0
    return np.round(net.pos[node_idx] / a).astype(int).tolist()


def build_assembly_manifest(net: cl.LatticeNet, L: int) -> dict:
    bonds = finite_crystal_bonds(net)
    nodes = sorted(active_nodes(bonds))
    pos_mm = lattice_pos_to_mm(net)

    node_records = []
    sub_counts = {"A": 0, "B": 0}
    for u in nodes:
        st = diamond_sublattice(net, u)
        sub_counts[st] += 1
        node_records.append({
            "id": int(u),
            "sublattice": st,
            "grid_ijk": _grid_index(net, u),
            "pos_mm": [float(x) for x in pos_mm[u]],
        })

    bond_records = []
    for u, v in bonds:
        du = net.pos[v] - net.pos[u]
        st_u = diamond_sublattice(net, u)
        st_v = diamond_sublattice(net, v)
        hat = du / (np.linalg.norm(du) + 1e-12)
        bond_records.append({
            "u": int(u),
            "v": int(v),
            "u_sublattice": st_u,
            "v_sublattice": st_v,
            "center_pitch_mm": float(np.linalg.norm(pos_mm[u] - pos_mm[v])),
            "insert_length_mm": float(bond_insert_length_mm(kit=True)),
            "direction_unit": [float(x) for x in hat],
            "port_tip_u_mm": [float(x) for x in kit_port_mouth(pos_mm[u], du, st_u)],
            "port_tip_v_mm": [float(x) for x in kit_port_mouth(pos_mm[v], -du, st_v)],
        })

    span = pos_mm.max(axis=0) - pos_mm.min(axis=0)
    return {
        "schema": "ave-vacuum-kit/v1",
        "substrate": "diamond production K4 (build_diamond_net)",
        "rendering_only": True,
        "print_mm_per_l_node": PRINT_MM_PER_L_NODE,
        "corpus_mnemonic_mm_per_l_node": _CORPUS_MNEMONIC_MM,
        "stl_export_frame": "print_pose",
        "print_pose": PRINT_POSE_SPEC,
        "prusa_mk3p_slicer_hints": {
            "nozzle_mm": 0.4,
            "layer_height_mm": 0.2,
            "perimeters_nodes": 3,
            "perimeters_bonds": 4,
            "infill_nodes_pct": 20,
            "infill_bonds_pct": 40,
            "supports": "none (parts are print-pose oriented)",
            "brim": "optional on node A port overhangs",
        },
        "lattice_L": L,
        "finite_chunk": True,
        "assembled_bbox_mm": [float(x) for x in span],
        "counts": {
            "nodes": len(nodes),
            "bonds": len(bonds),
            "node_A_print": sub_counts["A"],
            "node_B_print": sub_counts["B"],
            "bond_insert_print": len(bonds),
        },
        "part_skus": {
            "node_A": "vacuum_node_A_capacitive.stl",
            "node_B": "vacuum_node_B_inductive.stl",
            "bond": "vacuum_tl_bond_diamond.stl",
        },
        "joinery": {
            "type": "friction_fit_peg_socket",
            "bond_center_pitch_mm": DIAMOND_CENTER_PITCH_MM,
            "orientation_key": "A=solid cube vs B=hollow sphere+ring; match manifest sublattice labels",
            **joinery_spec(kit=True),
        },
        "assembly_steps": [
            "Print node_A × counts.node_A_print, node_B × counts.node_B_print, bond × counts.bond_insert_print.",
            "Place nodes at manifest.nodes[].pos_mm (A/B type per sublattice).",
            "Press bond pegs into port sockets from outside; bore is open through collar into cell pocket.",
            "Distinguish A (solid cube) vs B (sphere shell + L-ring) per manifest sublattice.",
            "Tune press-fit: KIT_FRICTION_INTERFERENCE_MM env (default 0.05 mm radial; try 0.03–0.08 for your filament).",
        ],
        "nodes": node_records,
        "bonds": bond_records,
        "canonical_port_hats_A": [h.tolist() for h in DIAMOND_PORT_HATS],
    }


def export_demo_one_bond(out_dir: pathlib.Path) -> None:
    """Single A–B link in assembly pose (reference for how ports mate)."""
    hat = DIAMOND_PORT_HATS[0]
    half_pitch = 0.5 * DIAMOND_CENTER_PITCH_MM
    pos_a = -hat * half_pitch
    pos_b = hat * half_pitch
    parts = [
        cell_body_mesh(pos_a, "A", kit_port_directions("A"), kit_mode=True),
        cell_body_mesh(pos_b, "B", kit_port_directions("B"), kit_mode=True),
        tl_bond_mesh(
            kit_port_mouth(pos_a, hat, "A"),
            kit_port_mouth(pos_b, -hat, "B"),
            kit=True,
        ),
    ]
    write_mesh(
        combine_meshes(parts),
        out_dir / "vacuum_kit_demo_one_bond_assembly.stl",
        report=None,
    )


def saved_qc(stl_paths: dict[str, pathlib.Path]) -> None:
    """Report the REAL on-disk manifold state of each saved STL (NON-GATING).

    Loads each written .stl back from disk the way a slicer would (trimesh,
    process=True + merge_vertices) and prints the true is_watertight /
    is_volume. The kit is WORK-IN-PROGRESS: this is report-only and never
    raises or sys.exits. The shipped meshes are not yet welded watertight —
    see Vol 9 Ch 18 known limitations + the kit README.
    """
    import trimesh

    print("  On-disk mesh QC (PROVISIONAL — WIP, report-only, non-gating):")
    for label, path in stl_paths.items():
        try:
            tm = trimesh.load(str(path), process=True, merge_vertices=True)
            watertight = bool(tm.is_watertight)
            is_volume = bool(tm.is_volume)
            print(
                f"  {label}: watertight={watertight}, is_volume={is_volume} "
                f"— PROVISIONAL (WIP; see Vol 9 Ch 18 known limitations)"
            )
        except Exception as exc:  # report-only; never fail the WIP kit
            print(f"  {label}: on-disk QC could not run ({exc}) — PROVISIONAL (WIP)")
    print()


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[3]
    out_dir = root / "assets" / "3d_models" / KIT_DIR_NAME
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("  Axiom-1 vacuum lattice — DIY kit export")
    print("=" * 74)
    print_scale_banner()
    print(f"  Kit default scale  = {PRINT_MM_PER_L_NODE} mm/ℓ_node  (corpus mnemonic {_CORPUS_MNEMONIC_MM} mm)")
    port_od = 2.0 * KIT_PORT_RADIUS
    if KIT_PORT_RADIUS < FDM_MIN_PORT_RADIUS_MM:
        print(f"  ⚠ Port collar OD ≈ {port_od:.2f} mm — below FDM floor (~{2*FDM_MIN_PORT_RADIUS_MM:.1f} mm).")
        print(f"    Raise KIT_PRINT_MM_PER_L_NODE (try {_FDM_FRIENDLY_MM} or 80).")
        print()
    else:
        print(f"  Port collar OD      ≈ {port_od:.2f} mm  (FDM OK)")
    print(f"  Assembly target: build_diamond_net(L={ASSEMBLY_L}) finite crystal")
    print(f"  Bond center pitch: {DIAMOND_CENTER_PITCH_MM:.1f} mm  |  "
          f"shaft: {bond_insert_length_mm(kit=True):.1f} mm  |  "
          f"total (with pegs): {bond_total_length_mm(kit=True):.1f} mm")
    j = joinery_spec(kit=True)
    print(f"  Joinery: bond hex flat {j['bond_outer_flat_to_flat_mm']:.2f} mm "
          f"(matches socket bore; collar flat {j['port_collar_flat_to_flat_mm']:.2f} mm)")
    print()

    node_a_raw = kit_node_mesh("A")
    node_b_raw = kit_node_mesh("B")
    bond_raw = kit_bond_insert_mesh()

    node_a = orient_node_a_for_print(node_a_raw)
    node_b = orient_node_b_for_print(node_b_raw)
    bond = orient_bond_for_print(bond_raw)

    stl_paths = {
        "node_A": out_dir / "vacuum_node_A_capacitive.stl",
        "node_B": out_dir / "vacuum_node_B_inductive.stl",
        "bond": out_dir / "vacuum_tl_bond_diamond.stl",
    }
    write_mesh(node_a, stl_paths["node_A"], report=None)
    write_mesh(node_b, stl_paths["node_B"], report=None)
    write_mesh(bond, stl_paths["bond"], report=None)
    export_demo_one_bond(out_dir)

    # PROVISIONAL on-disk QC (WIP — report-only, NON-GATING).
    # We check the SAVED .stl as a slicer would reload it, not the in-memory
    # boolean object. The in-memory mesh is internally watertight, but the
    # exported STLs reload non-manifold (boolean-CSG export is not yet welded
    # watertight). Reporting the in-memory state would LIE about the shipped
    # kit. See Vol 9 Ch 18 known limitations + kit README. Mesh remediation
    # is deferred/tracked, so this never raises or exits.
    saved_qc(stl_paths)

    net = cl.build_diamond_net(ASSEMBLY_L)
    manifest = build_assembly_manifest(net, ASSEMBLY_L)
    manifest_path = out_dir / f"vacuum_assembly_L{ASSEMBLY_L}.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    c = manifest["counts"]
    bbox = manifest["assembled_bbox_mm"]
    print(f"  Manifest → {manifest_path.name}")
    print(f"    Print: {c['node_A_print']}× A  +  {c['node_B_print']}× B  +  {c['bond_insert_print']}× bond")
    print(f"    Assembled bbox ≈ {bbox[0]:.0f}×{bbox[1]:.0f}×{bbox[2]:.0f} mm")
    print()
    print(f"  Output directory: {out_dir.resolve()}")
    print("  Export frame: print pose (parts on build plate; see manifest print_pose)")


if __name__ == "__main__":
    main()
