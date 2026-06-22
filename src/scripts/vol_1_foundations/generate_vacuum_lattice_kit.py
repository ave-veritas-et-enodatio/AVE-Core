#!/usr/bin/env python3
"""
DIY vacuum-lattice kit — REBUILT representative + printable exporter (Prusa i3 MK3+).

Replaces the legacy cube/sphere kit. The vacuum cell is rendered faithfully:

  * REAL SPACE (isomorphic): degree-4 diamond production net (build_diamond_net) —
    identical solid node body for both A and B sublattices (A/B is a sublattice
    LABEL, not a storage split), 4 tetrahedral bond sockets, true sqrt(3)*l_node pitch.
  * DOF BASIS (oriented snap-on accents, one color each): triad_E (3 translational
    -> E / eps^2), rings_B (3 microrotational -> B / kappa^2), breathing_V (A1
    volumetric breathing -> V^2 = mass). A1 perp T2 kept (breathing axis independent).
  * PHASE SPACE (labeled proxy, never a coordinate): impedance disc + phasor dial,
    stamped [STATE-SPACE - NOT A COORDINATE].
  * CHIRAL srs ACCEPTANCE INSTRUMENT (degree-3, both enantiomorphs) — kept distinct
    from the production diamond.
  * BASE JIG: keyed baseplate that forces correct node placement and ports.

All parts are exported WATERTIGHT directly from trimesh (no numpy-stl round-trip —
that was the legacy non-manifold bug). saved QC is GATING (KIT_ALLOW_NONMANIFOLD=1
to override for WIP). Absolute sizes are [RENDERING] magnification (~2.6e11x).

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_vacuum_lattice_kit.py
    KIT_PRINT_MM_PER_L_NODE=60 ASSEMBLY_L=4 python ...
"""

from __future__ import annotations

import json
import os
import pathlib
import sys

from ave.core.constants import L_NODE

# Kit print scale must be set BEFORE the geometry modules read PRINT_MM_PER_L_NODE.
_FDM_FRIENDLY_MM = round(2.0 / 0.060, 1)
_KIT_MM = os.environ.get("KIT_PRINT_MM_PER_L_NODE") or str(max(_FDM_FRIENDLY_MM, 100.0))
os.environ["PRINT_MM_PER_L_NODE"] = _KIT_MM

import numpy as np  # noqa: E402
import trimesh  # noqa: E402

from ave.core import chiral_lattice as cl  # noqa: E402

from generate_vacuum_lattice_stl import (  # noqa: E402
    MM_PER_L_NODE_UNIT,
    active_nodes,
    finite_crystal_bonds,
    lattice_pos_to_mm,
)
from vacuum_lc_geometry import DIAMOND_PORT_HATS, diamond_sublattice  # noqa: E402

import kit_core_diamond as core  # noqa: E402
import kit_phase_space as ps  # noqa: E402
import kit_srs as srs  # noqa: E402
import kit_jig as jig  # noqa: E402

ASSEMBLY_L = int(os.environ.get("ASSEMBLY_L", "4"))
ALLOW_NONMANIFOLD = os.environ.get("KIT_ALLOW_NONMANIFOLD") == "1"
KIT_DIR_NAME = "kit"
S = MM_PER_L_NODE_UNIT
_CORPUS_MNEMONIC_MM = round(L_NODE * 1e15 / 10.0, 1)  # 386 fm -> 38.6 mm digit tie [reference only]
_MAGNIFICATION = S / (L_NODE * 1e3)  # mm-print per mm-physical


# ── watertight export + on-disk QC ─────────────────────────────────────────
def _lay_on_bed(tm: "trimesh.Trimesh") -> "trimesh.Trimesh":
    t = tm.copy()
    t.apply_translation([0.0, 0.0, -float(t.bounds[0][2])])
    return t


def export_part(tm, path: pathlib.Path, *, lay_flat: bool = True, gate: bool = True) -> dict:
    """Weld + fix normals, drop to bed, export, reload as a slicer would, report."""
    t = tm.copy()
    t.merge_vertices()
    t.fix_normals()
    if lay_flat:
        t = _lay_on_bed(t)
    t.export(str(path))
    r = trimesh.load(str(path), process=True, merge_vertices=True)
    ext = r.bounds[1] - r.bounds[0]
    return {
        "label": path.name,
        "watertight": bool(r.is_watertight),
        "is_volume": bool(r.is_volume),
        "faces": int(len(r.faces)),
        "bbox_mm": [round(float(x), 2) for x in ext],
        "gate": gate,
    }


# ── manifest helpers ───────────────────────────────────────────────────────
def _port_index(sublattice: str, direction: np.ndarray) -> int:
    """Which of the 4 tetrahedral ports (0-3) a bond leaves through."""
    hats = DIAMOND_PORT_HATS if sublattice == "A" else -DIAMOND_PORT_HATS
    d = direction / (np.linalg.norm(direction) + 1e-12)
    return int(np.argmax(hats @ d))


def _grid_index(net: cl.LatticeNet, node_idx: int) -> list[int]:
    a = net.a_cell if net.a_cell else 1.0
    return np.round(net.pos[node_idx] / a).astype(int).tolist()


def build_manifest(net: cl.LatticeNet, L: int, parts_qc: list[dict]) -> dict:
    bonds = finite_crystal_bonds(net)
    nodes = sorted(active_nodes(bonds))
    pos_mm = lattice_pos_to_mm(net)
    kd = core.key_dims()

    # node records with full port -> neighbor map
    neigh: dict[int, list[tuple[int, np.ndarray]]] = {u: [] for u in nodes}
    for u, v in bonds:
        neigh[u].append((v, net.pos[v] - net.pos[u]))
        neigh[v].append((u, net.pos[u] - net.pos[v]))

    node_records = []
    sub_counts = {"A": 0, "B": 0}
    for u in nodes:
        st = diamond_sublattice(net, u)
        sub_counts[st] += 1
        ports = [{"port": _port_index(st, d), "neighbor": int(v)} for v, d in neigh[u]]
        ports.sort(key=lambda p: p["port"])
        node_records.append({
            "id": int(u),
            "sublattice": st,
            "grid_ijk": _grid_index(net, u),
            "pos_mm": [round(float(x), 3) for x in pos_mm[u]],
            "ports": ports,  # port index 0-3 -> neighbor node id
        })

    bond_records = []
    for u, v in bonds:
        du = net.pos[v] - net.pos[u]
        st_u, st_v = diamond_sublattice(net, u), diamond_sublattice(net, v)
        bond_records.append({
            "u": int(u), "v": int(v),
            "u_sublattice": st_u, "v_sublattice": st_v,
            "u_port": _port_index(st_u, du), "v_port": _port_index(st_v, -du),
            "center_pitch_mm": round(float(np.linalg.norm(pos_mm[u] - pos_mm[v])), 3),
        })

    span = pos_mm[nodes].max(axis=0) - pos_mm[nodes].min(axis=0)
    return {
        "schema": "ave-vacuum-kit/v2",
        "substrate": "diamond production K4 / degree-4 / Fd-3m (build_diamond_net)",
        "rendering_only": True,
        "print_mm_per_l_node": S,
        "corpus_mnemonic_mm_per_l_node": _CORPUS_MNEMONIC_MM,
        "magnification_vs_physical": round(_MAGNIFICATION, 3),
        "l_node_fm": round(L_NODE * 1e15, 2),
        "representation_note": (
            "Real space (nodes/bonds/4 ports) is isomorphic; the DOF basis is shown by "
            "snap-on accents (triad_E/rings_B/breathing_V); phase space (LC-tank state) "
            "is the disc/dial ONLY, never a printed length. A/B is the bipartite "
            "sublattice label, NOT a storage split — node bodies are identical."
        ),
        "lattice_L": L,
        "finite_chunk": True,
        "assembled_bbox_mm": [round(float(x), 1) for x in span],
        "counts": {
            "nodes": len(nodes), "bonds": len(bonds),
            "node_A": sub_counts["A"], "node_B": sub_counts["B"],
        },
        "joinery": {
            "type": "friction_fit_hex_peg_socket",
            "press_fit_diametral_interference_mm": round(2.0 * kd.get("INTERF_MM", 0.05), 3),
            "tune_env": "KIT_FRICTION_INTERFERENCE_MM (per-side mm; default 0.05; try 0.03-0.08)",
            **{k: round(float(v), 3) for k, v in kd.items()},
        },
        "bom_tiers": {
            "structural_base_monochrome": [
                "vacuum_node_A.stl", "vacuum_node_B.stl", "vacuum_bond.stl",
            ],
            "dof_accents_color_per_store": [
                "accent_triad_E.stl  (E / translational / eps^2)",
                "accent_rings_B.stl  (B / microrotational / kappa^2)",
                "accent_breathing_V.stl  (A1 / mass / V^2)",
                "key_A.stl", "key_B.stl",
            ],
            "phase_space_state_space": [
                "phase_impedance_disc.stl", "phase_dial_body.stl",
                "phase_dial_pointer.stl", "phase_dial2_body.stl", "phase_dial2_pointer.stl",
            ],
            "chiral_srs_instrument": [
                "srs_node_right.stl", "srs_node_left.stl", "srs_bond.stl",
                "srs_handedness_right.stl", "srs_handedness_left.stl",
            ],
            "assembly_jig": ["jig_unit_cell.stl"] + [f"jig_tile_{i}.stl" for i in range(4)],
            "reference_only": ["reference_tetra_unit_cell.stl", "scale_plate.stl"],
        },
        "hero_first_print": {
            "name": "tetrahedral unit cell (degree-4 coordination shell)",
            "bom": "1x node_A + 4x node_B + 4x bond + accents + jig_unit_cell",
            "why": "shows z=4 coordination, A/B bipartiteness, tetrahedral ports in ~9 parts",
        },
        "prusa_mk3p_slicer_hints": {
            "nozzle_mm": 0.4, "layer_height_mm": 0.2,
            "perimeters": 3, "infill_pct": 20,
            "supports": "none — every part is posed flat / solid (bond prints horizontal)",
            "elephant_foot_compensation_mm": 0.15,
            "filament": "one color per part; assign accent colors per BOM tier",
        },
        "assembly_steps": [
            "Print the jig tiles; assemble the baseplate (snap/glue tile edges).",
            "Print node_A x counts.node_A, node_B x counts.node_B in two colors.",
            "Drop each node into its keyed jig pocket (pocket emboss = node id + A/B).",
            "Press bonds into sockets; pocket port-pips show which port -> which neighbor (manifest nodes[].ports).",
            "Optional: snap on DOF accents (triad_E / rings_B / breathing_V) + A/B key, color per store.",
            "Optional: set the phasor dial / read the impedance disc as the LC-tank STATE (not a position).",
            "Tune press-fit via KIT_FRICTION_INTERFERENCE_MM if loose/tight.",
        ],
        "parts_qc": parts_qc,
        "nodes": node_records,
        "bonds": bond_records,
        "canonical_port_hats_A": [h.tolist() for h in DIAMOND_PORT_HATS],
    }


# ── reference / scale parts ────────────────────────────────────────────────
def scale_plate() -> "trimesh.Trimesh":
    """Language-free [RENDERING] scale bar: a raised bar = 1 l_node print pitch (S)."""
    parts = [trimesh.creation.box(extents=(S * 1.1, 0.18 * S, 0.04 * S))]
    bar = trimesh.creation.box(extents=(S, 0.03 * S, 0.03 * S))
    bar.apply_translation([0, 0, 0.035 * S])
    parts.append(bar)
    for i in range(6):  # 5 intervals => the bar spans exactly 1 l_node
        t = trimesh.creation.box(extents=(0.008 * S, 0.10 * S, 0.04 * S))
        t.apply_translation([-S / 2 + i * S / 5, 0, 0.04 * S])
        parts.append(t)
    out = trimesh.boolean.union(parts, engine="manifold")
    out.merge_vertices()
    out.fix_normals()
    return out


def reference_tetra_unit_cell() -> "trimesh.Trimesh":
    """Fused VISUAL preview (NOT for printing): 1 A node + 4 bonds + 4 B nodes."""
    pitch = float(np.sqrt(3.0)) * S
    parts = [core.node_body("A")]
    for hat in DIAMOND_PORT_HATS:
        nb = core.node_body("B")
        nb.apply_translation(hat * pitch)
        parts.append(nb)
        b = core.bond(helix=False)  # smooth bonds keep the visual preview light
        b.apply_transform(trimesh.geometry.align_vectors([0, 0, 1.0], hat))
        b.apply_translation(hat * (pitch / 2.0))
        parts.append(b)
    return trimesh.util.concatenate(parts)


# ── main ───────────────────────────────────────────────────────────────────
def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[3]
    out_dir = root / "assets" / "3d_models" / KIT_DIR_NAME
    out_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("  Axiom-1 vacuum lattice — REBUILT DIY kit export (representative + printable)")
    print("=" * 80)
    print(f"  l_node            = {L_NODE*1e15:.2f} fm  ({L_NODE:.4e} m)")
    print(f"  Print scale       = {S:.1f} mm / l_node  [RENDERING]  (x{_MAGNIFICATION:.3e})")
    print(f"  Diamond NN pitch  = sqrt(3)*S = {np.sqrt(3)*S:.1f} mm")
    print(f"  Assembly target   = build_diamond_net(L={ASSEMBLY_L})")
    print()

    qc: list[dict] = []

    # Structural base (identical body A/B; A/B differ only by key + color).
    qc.append(export_part(core.node_body("A"), out_dir / "vacuum_node_A.stl"))
    qc.append(export_part(core.node_body("B"), out_dir / "vacuum_node_B.stl"))
    # Bond printed HORIZONTAL (long part; lay on a hex flat).
    qc.append(export_part(core.print_pose_horizontal(core.bond(helix=True)),
                          out_dir / "vacuum_bond.stl"))
    qc.append(export_part(core.print_pose_horizontal(core.bond(helix=True, left_handed=True)),
                          out_dir / "vacuum_bond_left.stl"))

    # DOF accents (snap-on, one color per store).
    qc.append(export_part(core.triad_E(), out_dir / "accent_triad_E.stl"))
    qc.append(export_part(core.rings_B(), out_dir / "accent_rings_B.stl"))
    qc.append(export_part(core.breathing_V(), out_dir / "accent_breathing_V.stl"))
    qc.append(export_part(core.ab_key("A"), out_dir / "key_A.stl"))
    qc.append(export_part(core.ab_key("B"), out_dir / "key_B.stl"))

    # Phase-space artifacts (LC-tank state; [STATE-SPACE - NOT A COORDINATE]).
    qc.append(export_part(ps.impedance_disc(), out_dir / "phase_impedance_disc.stl"))
    qc.append(export_part(ps.phasor_dial_body(), out_dir / "phase_dial_body.stl"))
    qc.append(export_part(ps.phasor_dial_pointer(), out_dir / "phase_dial_pointer.stl"))
    qc.append(export_part(ps.phasor_dial_two_indicator_body(), out_dir / "phase_dial2_body.stl"))
    qc.append(export_part(ps.phasor_dial_pointer_outer(), out_dir / "phase_dial2_pointer.stl"))

    # Chiral srs acceptance instrument (degree-3, both enantiomorphs).
    qc.append(export_part(srs.srs_node("right"), out_dir / "srs_node_right.stl"))
    qc.append(export_part(srs.srs_node("left"), out_dir / "srs_node_left.stl"))
    qc.append(export_part(core.print_pose_horizontal(srs.srs_bond()), out_dir / "srs_bond.stl"))
    qc.append(export_part(srs.handedness_marker("right"), out_dir / "srs_handedness_right.stl"))
    qc.append(export_part(srs.handedness_marker("left"), out_dir / "srs_handedness_left.stl"))

    # Base jig (keyed placement). Unit-cell jig + tiled full-chunk plate.
    qc.append(export_part(jig.unit_cell_jig(), out_dir / "jig_unit_cell.stl"))
    for name, tile in jig.assembly_jig(L=ASSEMBLY_L).items():
        qc.append(export_part(tile, out_dir / f"{name}.stl"))

    # Scale plate (gated — it's a solid).
    qc.append(export_part(scale_plate(), out_dir / "scale_plate.stl"))

    # Reference-only fused preview (NOT gated — concatenation, not a watertight solid).
    export_part(reference_tetra_unit_cell(), out_dir / "reference_tetra_unit_cell.stl", gate=False)

    # Manifest.
    net = cl.build_diamond_net(ASSEMBLY_L)
    manifest = build_manifest(net, ASSEMBLY_L, qc)
    (out_dir / f"vacuum_assembly_L{ASSEMBLY_L}.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Report + GATING QC.
    print(f"  Exported {len(qc) + 1} STLs -> {out_dir}")
    print(f"  {'PART':32} {'watertight':>10} {'is_volume':>10} {'faces':>7}  bbox(mm)")
    failed = []
    for q in qc:
        flag = "" if (q["watertight"] and q["is_volume"]) else "  <-- FAIL"
        if q["gate"] and not (q["watertight"] and q["is_volume"]):
            failed.append(q["label"])
        print(f"  {q['label']:32} {str(q['watertight']):>10} {str(q['is_volume']):>10} "
              f"{q['faces']:>7}  {q['bbox_mm']}{flag}")
    print()
    c = manifest["counts"]
    print(f"  Manifest L={ASSEMBLY_L}: {c['node_A']}xA + {c['node_B']}xB + {c['bonds']} bonds  "
          f"| assembled bbox {manifest['assembled_bbox_mm']} mm")
    print(f"  Press-fit interference = {manifest['joinery']['press_fit_diametral_interference_mm']} mm diametral")

    if failed:
        msg = f"GATING QC FAILED — non-manifold parts: {failed}"
        if ALLOW_NONMANIFOLD:
            print(f"  WARN {msg}  (KIT_ALLOW_NONMANIFOLD=1 set — not exiting)")
        else:
            print(f"  FAIL {msg}")
            sys.exit(1)
    else:
        print("  OK  All gated parts reload watertight + is_volume. Kit is print-ready.")


if __name__ == "__main__":
    main()
