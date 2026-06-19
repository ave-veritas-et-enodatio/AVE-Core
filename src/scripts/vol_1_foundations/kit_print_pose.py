"""Print-pose transforms for vacuum lattice kit STLs (bed-ready orientation)."""

from __future__ import annotations

import numpy as np
from stl import mesh as stl_mesh

from vacuum_lc_geometry import DIAMOND_PORT_HATS  # noqa: E402


def rotation_align(v_from: np.ndarray, v_to: np.ndarray) -> np.ndarray:
    """3×3 rotation matrix mapping unit vector v_from → v_to."""
    a = np.asarray(v_from, dtype=float)
    b = np.asarray(v_to, dtype=float)
    a /= np.linalg.norm(a) + 1e-12
    b /= np.linalg.norm(b) + 1e-12
    cross = np.cross(a, b)
    dot = float(np.dot(a, b))
    if np.linalg.norm(cross) < 1e-9:
        if dot > 0.0:
            return np.eye(3)
        # 180° flip around any axis perpendicular to a
        perp = np.array([1.0, 0.0, 0.0])
        if abs(np.dot(a, perp)) > 0.9:
            perp = np.array([0.0, 1.0, 0.0])
        axis = np.cross(a, perp)
        axis /= np.linalg.norm(axis) + 1e-12
        x, y, z = axis
        K = np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]])
        return np.eye(3) + 2.0 * (K @ K)
    vx = np.array(
        [[0.0, -cross[2], cross[1]], [cross[2], 0.0, -cross[0]], [-cross[1], cross[0], 0.0]]
    )
    c = dot
    s2 = float(np.dot(cross, cross))
    return np.eye(3) + vx + vx @ vx * ((1.0 - c) / s2)


def transform_mesh(mesh: stl_mesh.Mesh, rotation: np.ndarray, translation: np.ndarray) -> stl_mesh.Mesh:
    out = stl_mesh.Mesh(np.copy(mesh.data))
    out.vectors = np.einsum("ij,...j->...i", rotation, out.vectors) + translation
    return out


def lay_on_bed(mesh: stl_mesh.Mesh, rotation: np.ndarray) -> stl_mesh.Mesh:
    """Apply rotation then translate so min-Z sits on the build plate (Z=0)."""
    rotated = np.einsum("ij,...j->...i", rotation, mesh.vectors)
    z_min = float(rotated[..., 2].min())
    return transform_mesh(mesh, rotation, np.array([0.0, 0.0, -z_min]))


def orient_node_a_for_print(mesh: stl_mesh.Mesh) -> stl_mesh.Mesh:
    """
    Type-A capacitive cube: one cube face flat on the bed (axis-aligned body).
    Port collars overhang at ~55° — short collars are FDM-tolerable without supports.
    """
    return lay_on_bed(mesh, np.eye(3))


def orient_node_b_for_print(mesh: stl_mesh.Mesh) -> stl_mesh.Mesh:
    """
    Type-B inductive sphere: equatorial L-ring in the XY plane (normal = +Z).
    Port 0 socket points up for key-fin visibility; sphere mass above the ring.
    """
    port0 = -DIAMOND_PORT_HATS[0]  # B sublattice flips port signs
    r = rotation_align(port0, np.array([0.0, 0.0, 1.0]))
    return lay_on_bed(mesh, r)


def orient_bond_for_print(mesh: stl_mesh.Mesh) -> stl_mesh.Mesh:
    """TL bond: uniform hex tube, axis vertical (+Z) for end-on printing."""
    r = rotation_align(DIAMOND_PORT_HATS[0], np.array([0.0, 0.0, 1.0]))
    return lay_on_bed(mesh, r)


PRINT_POSE_SPEC = {
    "node_A": {
        "bed_face": "solid cube, one face on XY",
        "notes": "Exterior port collars at 4 corners; no wireframe weak joints.",
    },
    "node_B": {
        "bed_face": "equatorial L-ring in XY; port sockets radiate from hollow sphere",
        "notes": "Sphere shell; lowest ring point on bed.",
    },
    "bond": {
        "bed_face": "bond axis vertical (+Z); uniform solid hex",
        "notes": "Print standing; bond OD matches collar socket bore ID.",
    },
}
