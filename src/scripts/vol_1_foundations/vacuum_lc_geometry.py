"""Shared Axiom-1 diamond LC cell + TL bond mesh geometry for vacuum STL exporters."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import numpy as np
from stl import mesh as stl_mesh

from ave.core import chiral_lattice as cl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "vol_2_subatomic"))
from generate_particle_stl import sweep_tube, sweep_tube_open  # noqa: E402

from generate_vacuum_lattice_stl import MM_PER_L_NODE_UNIT, combine_meshes  # noqa: E402

# Canonical tetrahedral Op5 port directions (engine: chiral_lattice._DIAMOND_PORTS)
DIAMOND_PORTS = np.array(
    [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], dtype=float
)
DIAMOND_PORT_HATS = DIAMOND_PORTS / np.linalg.norm(DIAMOND_PORTS[0])

# Geometry as fractions of ℓ_node print pitch [RENDERING — topology from engine]
CELL_A_HALF = 0.085 * MM_PER_L_NODE_UNIT
CELL_B_RADIUS = 0.075 * MM_PER_L_NODE_UNIT
B_RING_MAJOR = 0.11 * MM_PER_L_NODE_UNIT
B_RING_TUBE = 0.022 * MM_PER_L_NODE_UNIT
PORT_LEN = 0.055 * MM_PER_L_NODE_UNIT
PORT_RADIUS = 0.032 * MM_PER_L_NODE_UNIT
TL_RADIUS = 0.026 * MM_PER_L_NODE_UNIT
KEY_FIN_THICK = 0.008 * MM_PER_L_NODE_UNIT  # legacy monolith only (unused in kit)

# Friction-fit joinery (FDM press-fit; override via KIT_FRICTION_INTERFERENCE_MM)
PEG_LEN = 0.42 * PORT_LEN
FRICTION_INTERFERENCE_MM = float(os.environ.get("KIT_FRICTION_INTERFERENCE_MM", "0.05"))
PEG_RADIUS = PORT_RADIUS * 0.78
SOCKET_RADIUS = max(PEG_RADIUS - FRICTION_INTERFERENCE_MM, TL_RADIUS * 0.85)
# Solid kit cube uses full box; port collars embed into surface then extend outward.
KIT_SOLID_CUBE_HALF = CELL_A_HALF

# --- Kit reinforcement: Prusa i3 MK3+ / hex cross-section joinery ---
# Default scale 100 mm/ℓ_node; hex circumradius; wall = PORT - SOCKET (~2× prior).
KIT_PEG_RADIUS = 0.036 * MM_PER_L_NODE_UNIT
KIT_WALL_RADIAL = 0.024 * MM_PER_L_NODE_UNIT
KIT_PORT_RADIUS = KIT_PEG_RADIUS + KIT_WALL_RADIAL
KIT_SOCKET_RADIUS = KIT_PEG_RADIUS - FRICTION_INTERFERENCE_MM
KIT_PORT_LEN = 0.065 * MM_PER_L_NODE_UNIT
KIT_COLLAR_EMBED = 0.032 * MM_PER_L_NODE_UNIT
# Type-A: stem starts inside cube body and extrudes out through the corner (not perched on tip).
KIT_A_COLLAR_INBOARD = 1.20 * KIT_SOLID_CUBE_HALF
KIT_PEG_LEN = 0.40 * KIT_PORT_LEN
# Kit bond OD = collar socket bore ID (male insert); uniform solid hex, no barbell.
KIT_BOND_RADIUS = KIT_SOCKET_RADIUS
KIT_TL_RADIUS = KIT_PEG_RADIUS * 0.88  # monolith / legacy only
KIT_HEX_SIDES = 6
# Legacy monolith / pre-kit names (unused by kit exporters)
COLLAR_EMBED = KIT_COLLAR_EMBED
SOCKET_POCKET_DEPTH = 0.045 * MM_PER_L_NODE_UNIT
KIT_SPHERE_WALL = 0.026 * MM_PER_L_NODE_UNIT

DIAMOND_CENTER_PITCH_MM = float(np.sqrt(3.0) * MM_PER_L_NODE_UNIT)


def diamond_sublattice(net: cl.LatticeNet, node_idx: int) -> str:
    """A = all-even FCC coords; B = all-odd (k4_tlm K4Lattice3D)."""
    a = net.a_cell if net.a_cell else 1.0
    idx = np.round(net.pos[node_idx] / a).astype(int)
    if np.all(idx % 2 == 0):
        return "A"
    if np.all(idx % 2 == 1):
        return "B"
    raise ValueError(f"non-bipartite diamond coord {idx}")


def shell_radius(sublattice: str) -> float:
    return CELL_A_HALF * 1.05 if sublattice == "A" else CELL_B_RADIUS * 1.08


def kit_attach_radius(sublattice: str) -> float:
    """Exterior mount radius for kit ports (bond sockets face outward from the cell)."""
    if sublattice == "A":
        # Cube corner along a tetrahedral body diagonal.
        return KIT_SOLID_CUBE_HALF * float(np.sqrt(3.0))
    return CELL_B_RADIUS * 1.05


def kit_port_mouth(center: np.ndarray, direction: np.ndarray, sublattice: str) -> np.ndarray:
    """Outer socket mouth — bond peg inserts here (exterior-facing)."""
    d = direction / (np.linalg.norm(direction) + 1e-12)
    return center + d * (kit_attach_radius(sublattice) + KIT_PORT_LEN)


def kit_port_directions(sublattice: str) -> list[np.ndarray]:
    """Canonical Op5 port unit vectors for a kit node mold at the origin."""
    sign = 1.0 if sublattice == "A" else -1.0
    return [sign * hat for hat in DIAMOND_PORT_HATS]


def bond_insert_length_mm(*, kit: bool = False) -> float:
    """TL shaft span between exterior port mouths on an A–B pair."""
    if kit:
        return (
            DIAMOND_CENTER_PITCH_MM
            - kit_attach_radius("A")
            - kit_attach_radius("B")
            - 2.0 * KIT_PORT_LEN
        )
    return (
        DIAMOND_CENTER_PITCH_MM
        - shell_radius("A")
        - shell_radius("B")
        - 2.0 * PORT_LEN
    )


def bond_total_length_mm(*, kit: bool = False) -> float:
    """Printed bond insert length including both friction-fit pegs."""
    return bond_insert_length_mm(kit=kit) + 2.0 * (KIT_PEG_LEN if kit else PEG_LEN)


def joinery_spec(*, kit: bool = False) -> dict[str, float]:
    """Manifest-ready friction-fit dimensions (mm)."""
    if kit:
        flat = float(np.sqrt(3.0) * KIT_PORT_RADIUS)
        peg_flat = float(np.sqrt(3.0) * KIT_PEG_RADIUS)
        return {
            "cross_section": "hexagon",
            "port_collar_circumradius_mm": float(KIT_PORT_RADIUS),
            "port_collar_flat_to_flat_mm": flat,
            "socket_inner_circumradius_mm": float(KIT_SOCKET_RADIUS),
            "socket_inner_flat_to_flat_mm": float(np.sqrt(3.0) * KIT_SOCKET_RADIUS),
            "bond_outer_circumradius_mm": float(KIT_BOND_RADIUS),
            "bond_outer_flat_to_flat_mm": float(np.sqrt(3.0) * KIT_BOND_RADIUS),
            "bond_matches": "socket_inner_bore",
            "peg_circumradius_mm": float(KIT_PEG_RADIUS),
            "peg_flat_to_flat_mm": peg_flat,
            "wall_radial_mm": float(KIT_WALL_RADIAL),
            "peg_length_mm": float(KIT_PEG_LEN),
            "collar_embed_mm": float(KIT_COLLAR_EMBED),
            "collar_embed_A_mm": float(KIT_A_COLLAR_INBOARD),
            "attach_radius_A_mm": float(kit_attach_radius("A")),
            "attach_radius_B_mm": float(kit_attach_radius("B")),
            "friction_interference_mm": float(FRICTION_INTERFERENCE_MM),
            "bond_shaft_length_mm": float(bond_insert_length_mm(kit=True)),
            "bond_total_length_mm": float(bond_total_length_mm(kit=True)),
            "fdm_target_printer": "Prusa i3 MK3+ (0.4 mm nozzle)",
        }
    return {
        "port_collar_radius_mm": float(PORT_RADIUS),
        "tl_shaft_radius_mm": float(TL_RADIUS),
        "peg_radius_mm": float(PEG_RADIUS),
        "socket_inner_radius_mm": float(SOCKET_RADIUS),
        "peg_length_mm": float(PEG_LEN),
        "socket_pocket_depth_mm": float(COLLAR_EMBED),
        "attach_radius_A_mm": float(kit_attach_radius("A")),
        "attach_radius_B_mm": float(kit_attach_radius("B")),
        "friction_interference_mm": float(FRICTION_INTERFERENCE_MM),
        "bond_shaft_length_mm": float(bond_insert_length_mm(kit=False)),
        "bond_total_length_mm": float(bond_total_length_mm(kit=False)),
    }


def _frenet_frame_open(curve: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Frenet-style T/N/B along an open polyline (matches sweep_tube_open)."""
    m = len(curve)
    t = np.zeros_like(curve)
    t[0] = curve[1] - curve[0]
    t[-1] = curve[-1] - curve[-2]
    t[1:-1] = curve[2:] - curve[:-2]
    t_norm = np.maximum(np.linalg.norm(t, axis=1, keepdims=True), 1e-12)
    t = t / t_norm

    dt = np.zeros_like(curve)
    dt[0] = t[1] - t[0]
    dt[-1] = t[-1] - t[-2]
    dt[1:-1] = t[2:] - t[:-2]
    proj = np.sum(dt * t, axis=1, keepdims=True)
    n = dt - proj * t
    n_norm = np.linalg.norm(n, axis=1, keepdims=True)

    degenerate = n_norm.flatten() < 1e-8
    if np.any(degenerate):
        for i in np.where(degenerate)[0]:
            abs_t = np.abs(t[i])
            min_axis = int(np.argmin(abs_t))
            perp = np.zeros(3)
            perp[min_axis] = 1.0
            nn = perp - t[i] * t[i, min_axis]
            n[i] = nn / (np.linalg.norm(nn) + 1e-30)
            n_norm[i] = 1.0
    n_norm = np.maximum(n_norm, 1e-12)
    n = n / n_norm
    b = np.cross(t, n)
    b_norm = np.maximum(np.linalg.norm(b, axis=1, keepdims=True), 1e-12)
    b = b / b_norm
    return t, n, b


def _hex_ring(center: np.ndarray, n: np.ndarray, b: np.ndarray, circumradius: float) -> np.ndarray:
    """Regular hexagon vertices in the plane spanned by n, b (circumradius to vertex)."""
    angles = np.pi / 6.0 + np.arange(KIT_HEX_SIDES) * (2.0 * np.pi / KIT_HEX_SIDES)
    offsets = (np.cos(angles)[:, None] * n + np.sin(angles)[:, None] * b) * circumradius
    return center + offsets


def _mesh_from_faces(faces: list[list[np.ndarray]]) -> stl_mesh.Mesh:
    arr = np.zeros(len(faces), dtype=stl_mesh.Mesh.dtype)
    arr["vectors"] = np.array(faces)
    return stl_mesh.Mesh(arr)


def sweep_hex_prism_open(
    curve: np.ndarray,
    circumradius: float,
    *,
    cap: bool = True,
) -> stl_mesh.Mesh:
    """Solid hexagonal prism extruded along an open polyline."""
    m = len(curve)
    _, n, b = _frenet_frame_open(curve)
    rings = np.array([_hex_ring(curve[i], n[i], b[i], circumradius) for i in range(m)])
    faces: list[list[np.ndarray]] = []
    for i in range(m - 1):
        for k in range(KIT_HEX_SIDES):
            kn = (k + 1) % KIT_HEX_SIDES
            v0, v1 = rings[i, k], rings[i, kn]
            v2, v3 = rings[i + 1, kn], rings[i + 1, k]
            faces.append([v0, v1, v2])
            faces.append([v0, v2, v3])
    if cap:
        hub0 = np.mean(rings[0], axis=0)
        hub1 = np.mean(rings[-1], axis=0)
        for k in range(KIT_HEX_SIDES):
            kn = (k + 1) % KIT_HEX_SIDES
            faces.append([rings[0, k], rings[0, kn], hub0])
            faces.append([rings[-1, k], hub1, rings[-1, kn]])
    return _mesh_from_faces(faces)


def sweep_hex_annulus_open(
    curve: np.ndarray,
    r_outer: float,
    r_inner: float,
    *,
    cap_base: bool = False,
    cap_tip: bool = False,
) -> stl_mesh.Mesh:
    """Hexagonal tube (outer hex − inner hex) along an open polyline."""
    m = len(curve)
    _, n, b = _frenet_frame_open(curve)
    outer = np.array([_hex_ring(curve[i], n[i], b[i], r_outer) for i in range(m)])
    inner = np.array([_hex_ring(curve[i], n[i], b[i], r_inner) for i in range(m)])
    faces: list[list[np.ndarray]] = []
    for i in range(m - 1):
        for k in range(KIT_HEX_SIDES):
            kn = (k + 1) % KIT_HEX_SIDES
            faces.append([outer[i, k], outer[i, kn], outer[i + 1, kn]])
            faces.append([outer[i, k], outer[i + 1, kn], outer[i + 1, k]])
            faces.append([inner[i, k], inner[i + 1, kn], inner[i, kn]])
            faces.append([inner[i, k], inner[i + 1, k], inner[i + 1, kn]])
    if cap_base:
        for k in range(KIT_HEX_SIDES):
            kn = (k + 1) % KIT_HEX_SIDES
            faces.append([outer[0, k], inner[0, k], inner[0, kn]])
            faces.append([outer[0, k], inner[0, kn], outer[0, kn]])
    if cap_tip:
        for k in range(KIT_HEX_SIDES):
            kn = (k + 1) % KIT_HEX_SIDES
            faces.append([outer[-1, k], outer[-1, kn], inner[-1, kn]])
            faces.append([outer[-1, k], inner[-1, kn], inner[-1, k]])
    return _mesh_from_faces(faces)


def sweep_annulus_open(
    curve: np.ndarray,
    r_outer: float,
    r_inner: float,
    *,
    n_radial: int = 14,
    cap_base: bool = True,
    cap_tip: bool = False,
) -> stl_mesh.Mesh:
    """Hollow tube (annulus) along an open curve; tip may stay open as a socket mouth."""
    m = len(curve)
    _, n, b = _frenet_frame_open(curve)
    phi = np.linspace(0, 2 * np.pi, n_radial, endpoint=False)

    outer = np.zeros((m, n_radial, 3))
    inner = np.zeros((m, n_radial, 3))
    for i in range(m):
        offset = np.cos(phi)[:, None] * n[i] + np.sin(phi)[:, None] * b[i]
        outer[i] = curve[i] + r_outer * offset
        inner[i] = curve[i] + r_inner * offset

    faces: list[list[np.ndarray]] = []
    for i in range(m - 1):
        for j in range(n_radial):
            jn = (j + 1) % n_radial
            faces.append([outer[i, j], outer[i, jn], outer[i + 1, jn]])
            faces.append([outer[i, j], outer[i + 1, jn], outer[i + 1, j]])
            faces.append([inner[i, j], inner[i + 1, jn], inner[i, jn]])
            faces.append([inner[i, j], inner[i + 1, j], inner[i + 1, jn]])
    if cap_base:
        for j in range(n_radial):
            jn = (j + 1) % n_radial
            faces.append([outer[0, j], inner[0, j], inner[0, jn]])
            faces.append([outer[0, j], inner[0, jn], outer[0, jn]])
    if cap_tip:
        for j in range(n_radial):
            jn = (j + 1) % n_radial
            faces.append([outer[-1, j], outer[-1, jn], inner[-1, jn]])
            faces.append([outer[-1, j], inner[-1, jn], inner[-1, j]])

    arr = np.zeros(len(faces), dtype=stl_mesh.Mesh.dtype)
    arr["vectors"] = np.array(faces)
    return stl_mesh.Mesh(arr)


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


def _sphere_shell_mesh(
    center: np.ndarray,
    r_outer: float,
    r_inner: float,
    n_lat: int = 14,
    n_lon: int = 22,
) -> stl_mesh.Mesh:
    """Spherical shell (hollow sphere) between r_inner and r_outer."""
    u = np.linspace(0, np.pi, n_lat)
    v = np.linspace(0, 2 * np.pi, n_lon, endpoint=False)
    uu, vv = np.meshgrid(u, v, indexing="ij")
    sin_u = np.sin(uu)
    dirs = np.stack([sin_u * np.cos(vv), sin_u * np.sin(vv), np.cos(uu)], axis=-1)
    outer = center + r_outer * dirs
    inner = center + r_inner * dirs
    faces: list[list[np.ndarray]] = []
    for i in range(outer.shape[0] - 1):
        for j in range(outer.shape[1]):
            jn = (j + 1) % outer.shape[1]
            faces.append([outer[i, j], outer[i, jn], outer[i + 1, jn]])
            faces.append([outer[i, j], outer[i + 1, jn], outer[i + 1, j]])
            faces.append([inner[i, j], inner[i + 1, jn], inner[i, jn]])
            faces.append([inner[i, j], inner[i + 1, j], inner[i + 1, jn]])
    arr = np.zeros(len(faces), dtype=stl_mesh.Mesh.dtype)
    arr["vectors"] = np.array(faces)
    return stl_mesh.Mesh(arr)


def _cube_frame_mesh(center: np.ndarray, half: float) -> stl_mesh.Mesh:
    """Hollow cube frame (12 edge beams) — interior void for port through-bores."""
    cx, cy, cz = center
    h = half
    corners = np.array([
        [cx - h, cy - h, cz - h],
        [cx + h, cy - h, cz - h],
        [cx + h, cy + h, cz - h],
        [cx - h, cy + h, cz - h],
        [cx - h, cy - h, cz + h],
        [cx + h, cy - h, cz + h],
        [cx + h, cy + h, cz + h],
        [cx - h, cy + h, cz + h],
    ])
    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    )
    beam = KIT_FRAME_BEAM_RADIUS
    parts = [
        sweep_tube_open(np.array([corners[i], corners[j]]), beam, n_radial=10, cap=True)
        for i, j in edges
    ]
    return combine_meshes(parts)


def _mesh_to_trimesh(mesh: stl_mesh.Mesh):
    import trimesh

    verts = mesh.vectors.reshape(-1, 3)
    faces = np.arange(len(verts)).reshape(-1, 3)
    tm = trimesh.Trimesh(vertices=verts, faces=faces, process=True)
    tm.merge_vertices()
    tm.fix_normals()
    return tm


def _trimesh_to_mesh(tm) -> stl_mesh.Mesh:
    out = stl_mesh.Mesh(np.zeros(len(tm.faces), dtype=stl_mesh.Mesh.dtype))
    out.vectors = tm.vertices[tm.faces]
    return out


def kit_trimesh_report(tm, label: str) -> dict[str, object]:
    """Manifold check on trimesh before STL export."""
    return {
        "label": label,
        "faces": int(len(tm.faces)),
        "watertight": bool(tm.is_watertight),
        "volume": bool(tm.is_volume),
    }


def _kit_box_trimesh(center: np.ndarray, half: float):
    import trimesh

    box = trimesh.creation.box(extents=(2.0 * half, 2.0 * half, 2.0 * half))
    box.apply_translation(center)
    return box


def _mesh_boolean_difference_tm(a, b):
    import trimesh

    result = trimesh.boolean.difference([a, b], engine="manifold")
    if result is None or len(result.faces) == 0:
        raise RuntimeError("mesh boolean difference failed")
    return result


def _mesh_boolean_union_tm(parts: list):
    import trimesh

    result = trimesh.boolean.union(parts, engine="manifold")
    if result is None or len(result.faces) == 0:
        raise RuntimeError("mesh boolean union failed")
    return result


def _kit_port_span(
    center: np.ndarray,
    direction: np.ndarray,
    sublattice: str,
) -> tuple[np.ndarray, np.ndarray, float]:
    """Return (stem_root, outer_mouth, attach) along a kit port axis."""
    d = direction / (np.linalg.norm(direction) + 1e-12)
    attach = kit_attach_radius(sublattice)
    embed = KIT_A_COLLAR_INBOARD if sublattice == "A" else KIT_COLLAR_EMBED
    stem_root = center + d * (attach - embed)
    outer_mouth = center + d * (attach + KIT_PORT_LEN)
    return stem_root, outer_mouth, attach


def _kit_bore_prism_trimesh(p0: np.ndarray, p1: np.ndarray, radius: float):
    return _mesh_to_trimesh(sweep_hex_prism_open(np.array([p0, p1]), radius, cap=True))


def _kit_collar_solid_wall_trimesh(
    center: np.ndarray,
    direction: np.ndarray,
    sublattice: str,
):
    """Closed hex collar wall (outer prism minus socket bore)."""
    stem_root, outer_mouth, _ = _kit_port_span(center, direction, sublattice)
    curve = np.array([stem_root, outer_mouth])
    outer = _mesh_to_trimesh(sweep_hex_prism_open(curve, KIT_PORT_RADIUS, cap=True))
    inner = _mesh_to_trimesh(sweep_hex_prism_open(curve, KIT_SOCKET_RADIUS, cap=True))
    return _mesh_boolean_difference_tm(outer, inner)


def _kit_sphere_shell_trimesh(center: np.ndarray, r_outer: float, r_inner: float, *, subdivisions: int = 4):
    import trimesh

    outer = trimesh.creation.icosphere(subdivisions=subdivisions, radius=r_outer)
    inner = trimesh.creation.icosphere(subdivisions=subdivisions, radius=r_inner)
    outer.apply_translation(center)
    inner.apply_translation(center)
    return _mesh_boolean_difference_tm(outer, inner)


def _kit_node_A_body_trimesh(center: np.ndarray, bond_dirs: list[np.ndarray]):
    """Watertight Type-A: bored cube + hex collar walls (single manifold)."""
    cube_tm = _kit_box_trimesh(center, KIT_SOLID_CUBE_HALF)
    for d in bond_dirs:
        stem_root, outer_mouth, _ = _kit_port_span(center, d, "A")
        bore_tm = _kit_bore_prism_trimesh(stem_root, outer_mouth, KIT_SOCKET_RADIUS)
        cube_tm = _mesh_boolean_difference_tm(cube_tm, bore_tm)
    walls = [_kit_collar_solid_wall_trimesh(center, d, "A") for d in bond_dirs]
    return _mesh_boolean_union_tm([cube_tm, *walls])


def _kit_node_B_body_trimesh(center: np.ndarray, bond_dirs: list[np.ndarray]):
    """Watertight Type-B: bored sphere shell + L-ring + hex collar walls."""
    r_out = CELL_B_RADIUS * 1.05
    r_in = max(r_out - KIT_SPHERE_WALL, CELL_B_RADIUS * 0.55)
    body_tm = _kit_sphere_shell_trimesh(center, r_out, r_in)
    for d in bond_dirs:
        stem_root, outer_mouth, _ = _kit_port_span(center, d, "B")
        bore_tm = _kit_bore_prism_trimesh(stem_root, outer_mouth, KIT_SOCKET_RADIUS)
        body_tm = _mesh_boolean_difference_tm(body_tm, bore_tm)
    n = bond_dirs[0] if bond_dirs else np.array([0.0, 0.0, 1.0])
    ring_tm = _mesh_to_trimesh(_inductive_ring(center, n, B_RING_MAJOR, B_RING_TUBE))
    walls = [_kit_collar_solid_wall_trimesh(center, d, "B") for d in bond_dirs]
    return _mesh_boolean_union_tm([body_tm, ring_tm, *walls])


def _kit_node_body_mesh(center: np.ndarray, sublattice: str, bond_dirs: list[np.ndarray]) -> stl_mesh.Mesh:
    if sublattice == "A":
        tm = _kit_node_A_body_trimesh(center, bond_dirs)
    else:
        tm = _kit_node_B_body_trimesh(center, bond_dirs)
    return _trimesh_to_mesh(tm)


def kit_mesh_report(mesh: stl_mesh.Mesh, label: str) -> dict[str, object]:
    """Quick manifold sanity check for exported kit STLs."""
    tm = _mesh_to_trimesh(mesh)
    return {
        "label": label,
        "faces": int(len(tm.faces)),
        "watertight": bool(tm.is_watertight),
        "volume": bool(tm.is_volume),
    }


def _port_collar(
    base: np.ndarray,
    direction: np.ndarray,
    length: float,
    radius: float,
    *,
    friction_fit: bool = True,
) -> stl_mesh.Mesh:
    """Monolith port collar (solid stem + tip socket)."""
    d = direction / (np.linalg.norm(direction) + 1e-12)
    tip = base + d * length
    parts: list[stl_mesh.Mesh] = []
    if friction_fit:
        stem_len = max(length - PEG_LEN, 0.0)
        if stem_len > 1e-6:
            stem_tip = base + d * stem_len
            parts.append(sweep_tube_open(np.array([base, stem_tip]), radius, n_radial=14, cap=True))
            parts.append(
                sweep_annulus_open(
                    np.array([stem_tip, tip]),
                    radius,
                    SOCKET_RADIUS,
                    cap_base=False,
                    cap_tip=False,
                )
            )
        else:
            parts.append(
                sweep_annulus_open(
                    np.array([base, tip]),
                    radius,
                    SOCKET_RADIUS,
                    cap_base=False,
                    cap_tip=False,
                )
            )
    else:
        parts.append(sweep_tube_open(np.array([base, tip]), radius, n_radial=14, cap=True))
    return combine_meshes(parts)


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


def cell_body_mesh(
    center: np.ndarray,
    sublattice: str,
    bond_dirs: list[np.ndarray],
    *,
    kit_mode: bool = False,
) -> stl_mesh.Mesh:
    if kit_mode:
        return _kit_node_body_mesh(center, sublattice, bond_dirs)

    parts: list[stl_mesh.Mesh] = []
    if sublattice == "A":
        parts.append(_box_mesh(center, CELL_A_HALF))
        shell = shell_radius("A")
    else:
        parts.append(_sphere_mesh(center, CELL_B_RADIUS))
        n = bond_dirs[0] if bond_dirs else np.array([0, 0, 1.0])
        parts.append(_inductive_ring(center, n, B_RING_MAJOR, B_RING_TUBE))
        shell = shell_radius("B")

    for d in bond_dirs:
        du = d / (np.linalg.norm(d) + 1e-12)
        base = center + du * shell
        parts.append(_port_collar(base, du, PORT_LEN, PORT_RADIUS))

    return combine_meshes(parts)


def port_tip(center: np.ndarray, direction: np.ndarray, sublattice: str) -> np.ndarray:
    d = direction / (np.linalg.norm(direction) + 1e-12)
    return center + d * (shell_radius(sublattice) + PORT_LEN)


def tl_bond_mesh(
    p0: np.ndarray,
    p1: np.ndarray,
    *,
    friction_fit: bool = True,
    kit: bool = False,
) -> stl_mesh.Mesh:
    """TL bond between port mouths; kit = uniform solid hex (OD = collar socket bore ID)."""
    tl_r = KIT_TL_RADIUS if kit else TL_RADIUS
    peg_r = KIT_PEG_RADIUS if kit else PEG_RADIUS
    peg_len = KIT_PEG_LEN if kit else PEG_LEN

    if kit:
        return sweep_hex_prism_open(np.array([p0, p1]), KIT_BOND_RADIUS, cap=True)

    if not friction_fit:
        return sweep_tube_open(np.array([p0, p1]), tl_r, n_radial=16, cap=True)

    axis = p1 - p0
    gap = float(np.linalg.norm(axis))
    if gap < 1e-9:
        return sweep_tube_open(np.array([p0, p1]), tl_r, n_radial=16, cap=True)
    hat = axis / gap
    tip_a = p0
    tip_b = p1
    peg_a_far = tip_a - hat * peg_len
    peg_b_far = tip_b - hat * peg_len
    parts = [
        sweep_tube_open(np.array([peg_a_far, tip_a]), peg_r, n_radial=16, cap=True),
        sweep_tube_open(np.array([tip_a, tip_b]), tl_r, n_radial=16, cap=False),
        sweep_tube_open(np.array([tip_b, peg_b_far]), peg_r, n_radial=16, cap=True),
    ]
    return combine_meshes(parts)


def kit_node_mesh(sublattice: str) -> stl_mesh.Mesh:
    """Single node mold centered at origin; hollow body + through-bore port sockets."""
    dirs = kit_port_directions(sublattice)
    return cell_body_mesh(np.zeros(3), sublattice, dirs, kit_mode=True)


def kit_bond_insert_mesh(
    axis: np.ndarray | None = None,
    length_mm: float | None = None,
) -> stl_mesh.Mesh:
    """TL bridge insert between two port mouths (centered for printing; pegs included)."""
    hat = DIAMOND_PORT_HATS[0] if axis is None else axis / (np.linalg.norm(axis) + 1e-12)
    gap = bond_insert_length_mm(kit=True) if length_mm is None else length_mm
    half_gap = 0.5 * gap
    tip_a = -hat * half_gap
    tip_b = hat * half_gap
    return tl_bond_mesh(tip_a, tip_b, friction_fit=True, kit=True)
