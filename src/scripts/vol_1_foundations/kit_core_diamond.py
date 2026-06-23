"""kit_core_diamond.py — AVE vacuum-lattice 3D-print kit: the DIAMOND MATING SYSTEM.

This module authors the load-bearing mating parts of the production net (degree-4
diamond, achiral Fd-3m). One author owns all of these so the press-fit geometry
mates exactly:

    1. node_body(sublattice)  -> the unified solid chamfered-cube node, with 4 hex
                                  bond sockets along the tetrahedral ports, 3 round
                                  accent sockets (E / B / V DOF accents) and 1 A/B-key
                                  accent socket.
    2. bond(helix=...)        -> full-length true-pitch hex rod with a helical groove,
                                  stepping to press-fit hex insertion tips at each end.
    3. triad_E()              -> E-store DOF accent: 3 orthogonal stubs (eps^2 store).
       rings_B()              -> B-store DOF accent: 3 orthogonal micro-rotation rings.
       breathing_V()          -> V-store DOF accent: concentric breathing bellows ridge.
    4. ab_key(sublattice)     -> small embossed 'A'/'B' tile/plug.

CANONICAL HONORINGS
-------------------
* Production substrate is DEGREE-4 diamond. 4 tetrahedral ports per node along
  DIAMOND_PORT_HATS; Type-A node uses +ports, Type-B uses -ports. Bond center pitch
  = sqrt(3)*S along these directions.
* EVERY node is an IDENTICAL full LC oscillator. A vs B is the bipartite SUBLATTICE
  label ONLY -> the node BODY is byte-for-byte identical for A and B except for the
  port SIGN (which only relabels which corners the sockets sit on) and the embossed
  A/B key. No A=cap / B=inductor shape split.
* Node mode content = 7 kinematic modes: 3 translational -> E (eps^2), 3
  microrotational -> B (kappa^2), 1 A1 volumetric breathing -> V^2 = the MASS.
  These live ONLY in the three SEPARATE DOF accent parts, never baked into the body.
* A1 perp T2: the breathing (V / mass) axis of breathing_V() is INDEPENDENT of the
  micro-rotation ring axes of rings_B() -> they are never merged into one feature.
* The dynamical saturation amplitude A is the LC-tank STATE, not a spatial DOF -> it
  is NOT represented here at all (it belongs to the phase-space disc/dial artifacts).

WATERTIGHT RULE
---------------
Every builder returns a trimesh.Trimesh that is watertight by construction: built
from trimesh.creation primitives + manifold booleans, then merge_vertices() +
fix_normals(). NO round-trip through numpy-stl. The integrator owns final export.

All absolute sizes are [RENDERING] magnification (~2.6e11x); S = MM_PER_L_NODE_UNIT.
"""

from __future__ import annotations

import os

import numpy as np
import trimesh

# Canonical scale + port directions imported from the engine geometry module.
from generate_vacuum_lattice_stl import MM_PER_L_NODE_UNIT as S  # noqa: E402
from vacuum_lc_geometry import DIAMOND_PORT_HATS  # noqa: E402

# --------------------------------------------------------------------------------------
# SHARED GEOMETRY CONTRACT (exact conventions so all kit parts mate)
# --------------------------------------------------------------------------------------
SQRT3 = float(np.sqrt(3.0))

# Press-fit interference (absolute mm per side). Single source of truth; env override.
INTERF_MM = float(os.environ.get("KIT_FRICTION_INTERFERENCE_MM", "0.05"))

# Node body --------------------------------------------------------------------------
NODE_HALF = 0.10 * S          # unified solid node half-extent (chamfered cube)
CHAMFER = 0.02 * S            # [RENDERING] edge chamfer for printability (elephant-foot)

# Bond socket on node (hex bore along the port direction) ------------------------------
R_JOINT = 0.036 * S           # socket bore circumradius (and bond-tip nominal)
SOCKET_DEPTH = 0.07 * S       # bore depth into the node along the port axis
# Surface distance from node center to the cube corner along the (1,1,1)-type diagonal:
NODE_CORNER_DIST = NODE_HALF * SQRT3

# Bond (hex rod) ----------------------------------------------------------------------
R_SHAFT = 0.05 * S            # visible shaft circumradius (carries the helix groove)
INSERT_DEPTH = 0.06 * S       # length of each press-fit insertion tip
R_TIP = R_JOINT + INTERF_MM   # insertion-tip circumradius (press fit into the bore)
# Bond visible span between the two node corner mouths on an A-B pair:
BOND_VISIBLE_SPAN = SQRT3 * S - 2.0 * NODE_CORNER_DIST
BOND_TOTAL_LEN = BOND_VISIBLE_SPAN + 2.0 * INSERT_DEPTH

# Helix groove [RENDERING] (handedness encodes chirality; production net is achiral so
# the groove is decorative pitch only -- a single right-handed turn over the shaft).
HELIX_TURNS = 1.0
HELIX_GROOVE_R = 0.012 * S    # cutter tube radius for the groove
HELIX_OFFSET = R_SHAFT - 0.006 * S  # radial position of the groove centerline

# Accent mount (small hex socket on the node; accents carry matching peg) --------------
ACCENT_JOINT = 0.018 * S      # accent socket circumradius
ACCENT_PEG_R = ACCENT_JOINT + INTERF_MM  # accent peg circumradius (press fit)
ACCENT_SOCKET_DEPTH = 0.05 * S
ACCENT_PEG_LEN = 0.045 * S

HEX_SIDES = 6


# --------------------------------------------------------------------------------------
# Low-level watertight helpers
# --------------------------------------------------------------------------------------
def _finalize(tm: trimesh.Trimesh) -> trimesh.Trimesh:
    """Merge coincident verts + fix winding so the part is watertight & a solid volume."""
    tm.merge_vertices()
    tm.update_faces(tm.nondegenerate_faces())
    tm.update_faces(tm.unique_faces())
    tm.remove_unreferenced_vertices()
    tm.fix_normals()
    return tm


def _union(parts: list[trimesh.Trimesh]) -> trimesh.Trimesh:
    out = trimesh.boolean.union(parts, engine="manifold")
    if out is None or len(out.faces) == 0:
        raise RuntimeError("boolean union failed")
    return out


def _difference(a: trimesh.Trimesh, b: trimesh.Trimesh) -> trimesh.Trimesh:
    out = trimesh.boolean.difference([a, b], engine="manifold")
    if out is None or len(out.faces) == 0:
        raise RuntimeError("boolean difference failed")
    return out


def _rotmat_z_to(direction: np.ndarray) -> np.ndarray:
    """4x4 rotation taking +Z onto `direction`."""
    d = np.asarray(direction, dtype=float)
    d = d / (np.linalg.norm(d) + 1e-12)
    z = np.array([0.0, 0.0, 1.0])
    if np.allclose(d, z):
        return np.eye(4)
    if np.allclose(d, -z):
        return trimesh.transformations.rotation_matrix(np.pi, [1.0, 0.0, 0.0])
    axis = np.cross(z, d)
    axis /= np.linalg.norm(axis) + 1e-12
    angle = float(np.arccos(np.clip(np.dot(z, d), -1.0, 1.0)))
    return trimesh.transformations.rotation_matrix(angle, axis)


def _hex_prism(circumradius: float, height: float) -> trimesh.Trimesh:
    """Solid regular hexagonal prism, axis = +Z, centered at origin (height along Z).

    Built directly from vertices + faces (no shapely dependency): two hex rings (top
    bottom) + side quads + fan-triangulated caps. Watertight by construction.
    """
    ang = np.pi / 6.0 + np.arange(HEX_SIDES) * (2.0 * np.pi / HEX_SIDES)
    ring = np.column_stack([np.cos(ang), np.sin(ang)]) * circumradius
    hz = height / 2.0
    bottom = np.column_stack([ring, np.full(HEX_SIDES, -hz)])
    top = np.column_stack([ring, np.full(HEX_SIDES, +hz)])
    verts = np.vstack([bottom, top])              # 0..5 bottom, 6..11 top
    cb = len(verts); verts = np.vstack([verts, [0, 0, -hz]])  # bottom center
    ct = len(verts); verts = np.vstack([verts, [0, 0, +hz]])  # top center

    faces = []
    for k in range(HEX_SIDES):
        kn = (k + 1) % HEX_SIDES
        b0, b1 = k, kn
        t0, t1 = 6 + k, 6 + kn
        # side wall (outward normals)
        faces.append([b0, b1, t1])
        faces.append([b0, t1, t0])
        # bottom cap (normal -Z)
        faces.append([cb, b1, b0])
        # top cap (normal +Z)
        faces.append([ct, t0, t1])
    prism = trimesh.Trimesh(vertices=verts, faces=np.array(faces), process=True)
    prism.fix_normals()
    return prism


def _hex_prism_along(p0: np.ndarray, p1: np.ndarray, circumradius: float) -> trimesh.Trimesh:
    """Solid hex prism spanning p0->p1, hex axis along the segment."""
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    axis = p1 - p0
    h = float(np.linalg.norm(axis))
    prism = _hex_prism(circumradius, h)
    prism.apply_transform(_rotmat_z_to(axis))
    prism.apply_translation((p0 + p1) / 2.0)
    return prism


def _cyl_along(p0: np.ndarray, p1: np.ndarray, radius: float, sections: int = 32) -> trimesh.Trimesh:
    p0 = np.asarray(p0, float)
    p1 = np.asarray(p1, float)
    return trimesh.creation.cylinder(radius=radius, segment=[p0, p1], sections=sections)


def _chamfered_cube(half: float, chamfer: float) -> trimesh.Trimesh:
    """Chamfered solid cube via intersection of a cube with a corner-clipping octahedron-ish
    blocky cut. We approximate edge-chamfer by intersecting with a slightly larger cube and
    differencing 8 corner wedges is fiddly; instead use trimesh box + bevel through a
    Minkowski-free approach: box intersect with an enlarged octahedron to clip the 8 corners
    only lightly. For robust manifold printing we simply chamfer the 12 edges by intersecting
    the cube with a stack of 3 rotated boxes (a rounded-ish prism). Simpler + robust: return a
    box; printability chamfer handled at integrator slicing. Here we provide a real geometric
    chamfer on the bed face only (anti elephant-foot) by clipping the bottom edge ring."""
    box = trimesh.creation.box(extents=(2 * half, 2 * half, 2 * half))
    # Bed-contact chamfer: clip the bottom 4 edges with 45-deg planes (elephant-foot relief).
    # Build a small frustum-like cutter: intersect box with an octagon-ish chamfer along -Z.
    c = chamfer
    # Bottom face is at z = -half. Cut a 45-deg bevel of size c around its perimeter by
    # differencing 4 long triangular prisms hugging the bottom edges.
    cutters = []
    for sign_axis, perp in ((0, 1), (1, 0)):
        for s in (-1.0, 1.0):
            # a wedge along the bottom edge parallel to `perp` axis
            wedge = trimesh.creation.box(extents=(2 * half + 2 * c, 2 * half + 2 * c, 2 * half + 2 * c))
            # rotate 45 deg about the perp axis, place so it only clips the bottom edge
            axis_vec = [0, 0, 0]
            axis_vec[perp] = 1.0
            R = trimesh.transformations.rotation_matrix(np.pi / 4.0, axis_vec)
            wedge.apply_transform(R)
            # translate the rotated box so one of its faces beveling the bottom edge
            t = [0.0, 0.0, 0.0]
            t[sign_axis] = s * (half + (2 * half + 2 * c) / np.sqrt(2) / 2.0 - c)
            t[2] = -half - (2 * half + 2 * c) / np.sqrt(2) / 2.0 + c
            wedge.apply_translation(t)
            cutters.append(wedge)
    out = box
    for w in cutters:
        try:
            out = _difference(out, w)
        except RuntimeError:
            pass
    return out


# --------------------------------------------------------------------------------------
# Port geometry
# --------------------------------------------------------------------------------------
def _port_dirs(sublattice: str) -> list[np.ndarray]:
    """Canonical Op5 tetrahedral port unit vectors. A:+hats, B:-hats."""
    sign = 1.0 if sublattice.upper() == "A" else -1.0
    return [sign * np.asarray(h, float) for h in DIAMOND_PORT_HATS]


def _accent_dirs() -> list[np.ndarray]:
    """Three accent-socket face directions for the E/B/V DOF accents -- on the +X,+Y,+Z
    cube faces (orthogonal, away from the tetrahedral port corners)."""
    return [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]


def _ab_key_dir() -> np.ndarray:
    """A/B key accent socket -- on the -Z (bed-up) face so it reads clearly and prints flat."""
    return np.array([0.0, 0.0, -1.0])


# --------------------------------------------------------------------------------------
# 1. NODE BODY  (IDENTICAL for A & B except port sign + key)
# --------------------------------------------------------------------------------------
def node_body(sublattice: str = "A") -> trimesh.Trimesh:
    """Unified solid chamfered-cube node with 4 round bond sockets, 3 accent sockets, and
    one A/B-key accent socket. Identical body for A and B; only port SIGN + key differ.

    Returns a watertight, is_volume trimesh.Trimesh centered at the origin.
    """
    body = _chamfered_cube(NODE_HALF, CHAMFER)

    cutters: list[trimesh.Trimesh] = []

    # 4 ROUND bond sockets along the tetrahedral ports, mouth at the cube corner.
    # Round (not hex): a rigid bond cannot face-flush a HEX tip in two independently-
    # clocked sockets at once (the two-end clocking constraint fails — verified by boolean:
    # both ends gouge at 2-3 mm^3 instead of the clean 1 mm^3 face-flush). A round bore +
    # round tip is rotation-symmetric, so the press-fit seats clean at ANY rotation, both
    # ends. (Anti-rotation is unneeded for a pressed/glued display lattice; the hex SHAFT
    # is retained for grip + the helix groove.)
    for d in _port_dirs(sublattice):
        mouth = d * NODE_CORNER_DIST          # surface point on the body diagonal
        inner = mouth - d * SOCKET_DEPTH      # bottom of the bore (toward center)
        outer = mouth + d * (0.02 * S)        # slight overshoot so the mouth opens cleanly
        bore = _cyl_along(inner, outer, R_JOINT)
        cutters.append(bore)

    # 3 round accent sockets (E / B / V DOF accents) on the +X/+Y/+Z faces.
    for d in _accent_dirs():
        mouth = d * NODE_HALF
        inner = mouth - d * ACCENT_SOCKET_DEPTH
        outer = mouth + d * (0.02 * S)
        bore = _cyl_along(inner, outer, ACCENT_JOINT)
        cutters.append(bore)

    # A/B-key accent socket on the -Z face.
    d = _ab_key_dir()
    mouth = d * NODE_HALF
    inner = mouth - d * ACCENT_SOCKET_DEPTH
    outer = mouth + d * (0.02 * S)
    cutters.append(_cyl_along(inner, outer, ACCENT_JOINT))

    body = _difference(body, _union(cutters))
    return _finalize(body)


# --------------------------------------------------------------------------------------
# 2. BOND  (hex shaft, helix groove, round press-fit tips)
# --------------------------------------------------------------------------------------
def bond(*, helix: bool = True, left_handed: bool = False) -> trimesh.Trimesh:
    """Full-length true-pitch rod: hex visible shaft (R_SHAFT) carrying a helical groove;
    each end steps to a ROUND press-fit insertion tip (R_TIP = R_JOINT + INTERF) of length
    INSERT_DEPTH. Round tips so the rigid bond seats clean in both node sockets regardless
    of clocking. Total length = BOND_TOTAL_LEN; axis along +Z, centered at origin.

    helix       : cut the helical groove into the shaft (True) or leave it smooth (False).
    left_handed : flip the groove handedness (chirality marker for the instrument net).
    """
    half_total = BOND_TOTAL_LEN / 2.0
    half_vis = BOND_VISIBLE_SPAN / 2.0

    # Visible hex shaft.
    shaft = _hex_prism(R_SHAFT, BOND_VISIBLE_SPAN)

    # Two ROUND press-fit tips stepping down from each shaft end. Round (not hex) so the
    # rigid bond seats face-flush in BOTH node sockets regardless of relative clocking —
    # a rotation-symmetric round tip in a round bore has no two-end clocking constraint.
    tip_a = _cyl_along([0.0, 0.0, half_vis], [0.0, 0.0, half_vis + INSERT_DEPTH], R_TIP)
    tip_b = _cyl_along([0.0, 0.0, -half_vis], [0.0, 0.0, -(half_vis + INSERT_DEPTH)], R_TIP)

    rod = _union([shaft, tip_a, tip_b])

    if helix:
        # Helical groove: a thin tube swept along a helix on the shaft, then differenced.
        n = 160
        frac = np.linspace(0.0, 1.0, n)
        z = -half_vis + frac * BOND_VISIBLE_SPAN
        sign = -1.0 if left_handed else 1.0
        theta = sign * 2.0 * np.pi * HELIX_TURNS * frac
        x = HELIX_OFFSET * np.cos(theta)
        y = HELIX_OFFSET * np.sin(theta)
        helix_curve = np.column_stack([x, y, z])
        groove = _sweep_round_tube(helix_curve, HELIX_GROOVE_R)
        rod = _difference(rod, groove)

    return _finalize(rod)


def _sweep_round_tube(curve: np.ndarray, radius: float, sections: int = 10) -> trimesh.Trimesh:
    """Watertight round tube swept along an open polyline (segment cylinders + joint
    spheres, unioned via manifold)."""
    parts = [
        _cyl_along(curve[i], curve[i + 1], radius, sections=sections)
        for i in range(len(curve) - 1)
    ]
    for p in curve:
        sph = trimesh.creation.icosphere(subdivisions=1, radius=radius)
        sph.apply_translation(p)
        parts.append(sph)
    return _union(parts)


def print_pose_horizontal(tm: trimesh.Trimesh) -> trimesh.Trimesh:
    """Lay a Z-axis hex rod flat on the bed, resting on a hex FLAT (not a vertex edge),
    and drop it so its lowest point sits at z=0. Returns a copy."""
    out = tm.copy()
    # Rotate hex-rod axis (Z) onto X so it lies flat.
    out.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2.0, [0.0, 1.0, 0.0]))
    # Rotate about X so a hex FLAT faces down (hex vertices start at pi/6, so a flat is
    # centered between vertices; rotate by pi/6 to put a flat at the bottom).
    out.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 6.0, [1.0, 0.0, 0.0]))
    out.apply_translation([0.0, 0.0, -out.bounds[0][2]])
    return out


# --------------------------------------------------------------------------------------
# Accent peg (shared by all DOF accents + key) — round press-fit peg along -Z so the
# accent body sits above the node face.
# --------------------------------------------------------------------------------------
def _accent_peg(base_z: float = 0.0) -> trimesh.Trimesh:
    """Round press-fit peg, axis +Z, top flush at z=base_z, extending downward (-Z)."""
    peg = _cyl_along(
        np.array([0.0, 0.0, base_z]),
        np.array([0.0, 0.0, base_z - ACCENT_PEG_LEN]),
        ACCENT_PEG_R,
    )
    return peg


# --------------------------------------------------------------------------------------
# 3a. E-store DOF accent: 3 orthogonal stubs (eps^2 translational store)
# --------------------------------------------------------------------------------------
def triad_E() -> trimesh.Trimesh:
    """E-triad accent: 3 orthogonal stubs on a small hub, snapping onto a node accent
    socket via a round peg. Represents the 3 translational modes (eps^2 -> E store).
    """
    hub_r = 0.03 * S
    stub_len = 0.075 * S          # [RENDERING]
    stub_r = 0.012 * S
    hub = trimesh.creation.icosphere(subdivisions=2, radius=hub_r)

    dirs = (np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([0, 0, 1.0]))
    parts = [hub]
    # +X, +Y, +Z stubs (the three orthogonal translational directions) + rounded caps.
    for d in dirs:
        end = d * (hub_r + stub_len)
        parts.append(_cyl_along(d * (hub_r * 0.5), end, stub_r, sections=20))
        cap = trimesh.creation.icosphere(subdivisions=1, radius=stub_r)
        cap.apply_translation(end)
        parts.append(cap)

    # Snap peg on the -Z side, below the hub.
    parts.append(_accent_peg(base_z=-hub_r * 0.6))

    body = _union(parts)
    return _finalize(body)


# --------------------------------------------------------------------------------------
# 3b. B-store DOF accent: 3 orthogonal rings (kappa^2 micro-rotation store)
# --------------------------------------------------------------------------------------
def rings_B() -> trimesh.Trimesh:
    """B-rings accent: 3 orthogonal micro-rotation rings fused at a small hub, snapping
    onto a node accent socket. Represents the 3 microrotational modes (kappa^2 -> B store).

    A1 perp T2: these ring axes are the micro-rotation axes ONLY; the V (breathing/mass)
    axis lives in breathing_V() and is never merged with these rings.
    """
    hub_r = 0.022 * S
    ring_major = 0.07 * S         # [RENDERING]
    ring_tube = 0.012 * S
    parts = [trimesh.creation.icosphere(subdivisions=2, radius=hub_r)]

    # Three rings normal to X, Y, Z respectively (orthogonal axis set).
    for normal in (np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([0, 0, 1.0])):
        ring = trimesh.creation.torus(major_radius=ring_major, minor_radius=ring_tube,
                                      major_sections=48, minor_sections=16)
        # default torus lies in XY (axis +Z); rotate axis +Z -> normal
        ring.apply_transform(_rotmat_z_to(normal))
        parts.append(ring)

    # Snap peg downward.
    parts.append(_accent_peg(base_z=-hub_r * 0.5))

    body = _union(parts)
    return _finalize(body)


# --------------------------------------------------------------------------------------
# 3c. V-store DOF accent: concentric breathing bellows ridge (A1 volumetric -> V^2 = MASS)
# --------------------------------------------------------------------------------------
def breathing_V() -> trimesh.Trimesh:
    """V-breathing accent: concentric bellows ridges (a radial-pulse glyph) on a single
    breathing axis, snapping onto a node accent socket. Represents the A1 volumetric
    breathing mode (V^2 store = the MASS).

    A1 perp T2: the breathing axis here is a single independent axis (+Z), explicitly NOT
    coupled to the micro-rotation ring axis-set of rings_B().
    """
    axis = np.array([0.0, 0.0, 1.0])
    base_r = 0.020 * S
    parts = []

    # Stacked concentric ridges of decreasing radius => "breathing" bellows along +Z.
    ridge_radii = [0.060 * S, 0.044 * S, 0.030 * S]   # [RENDERING]
    ridge_tube = 0.010 * S
    z = 0.0
    dz = 0.018 * S
    # central column tying the ridges together (the breathing axis)
    col_r = base_r * 0.6
    col_top = axis * (z + dz * (len(ridge_radii)))
    parts.append(_cyl_along(np.array([0, 0, -0.01 * S]), col_top, col_r, sections=24))
    spoke_r = 0.7 * ridge_tube
    for k, rr in enumerate(ridge_radii):
        zc = z + dz * k
        ring = trimesh.creation.torus(major_radius=rr, minor_radius=ridge_tube,
                                      major_sections=48, minor_sections=14)
        ring.apply_translation([0.0, 0.0, zc])
        parts.append(ring)
        # radial spokes tying each ridge to the central column (so it prints as ONE solid).
        for a in np.linspace(0.0, 2 * np.pi, 4, endpoint=False):
            p_out = np.array([rr * np.cos(a), rr * np.sin(a), zc])
            p_in = np.array([col_r * 0.5 * np.cos(a), col_r * 0.5 * np.sin(a), zc])
            parts.append(_cyl_along(p_in, p_out, spoke_r, sections=12))

    # Snap peg downward (single breathing axis, collinear with the ridge stack).
    parts.append(_accent_peg(base_z=-0.01 * S))

    body = _union(parts)
    return _finalize(body)


# --------------------------------------------------------------------------------------
# 4. A/B KEY  (small embossed 'A'/'B' tile with a snap peg)
# --------------------------------------------------------------------------------------
def ab_key(sublattice: str = "A") -> trimesh.Trimesh:
    """Small tile with an embossed 'A' or 'B' glyph and a round snap peg, keying the
    node's sublattice identity. Color carries the rest; this carries the letter.
    """
    letter = "A" if sublattice.upper() == "A" else "B"
    tile_half = 0.05 * S          # [RENDERING]
    tile_thick = 0.02 * S
    emboss_h = 0.008 * S          # >= legible-detail floor (0.8 mm @ S=100)

    tile = trimesh.creation.box(extents=(2 * tile_half, 2 * tile_half, tile_thick))
    # tile top face at z = +tile_thick/2
    top_z = tile_thick / 2.0

    parts = [tile]

    # Embossed glyph built from blocky strokes (robust, font-free, manifold).
    strokes = _letter_strokes(letter, tile_half * 1.3, emboss_h)
    for stroke in strokes:
        stroke.apply_translation([0.0, 0.0, top_z + emboss_h / 2.0 - 1e-4])
        parts.append(stroke)

    # Snap peg under the tile (-Z).
    peg = _cyl_along(
        np.array([0.0, 0.0, -tile_thick / 2.0]),
        np.array([0.0, 0.0, -tile_thick / 2.0 - ACCENT_PEG_LEN]),
        ACCENT_PEG_R,
    )
    parts.append(peg)

    body = _union(parts)
    return _finalize(body)


def _letter_strokes(letter: str, extent: float, height: float) -> list[trimesh.Trimesh]:
    """Blocky 'A' or 'B' as a list of box strokes (centered at origin in XY, base at z=0).
    extent ~ overall glyph size; height = emboss height (Z)."""
    t = 0.10 * extent      # stroke thickness
    h = 0.55 * extent      # glyph half-height
    w = 0.30 * extent      # glyph half-width
    boxes: list[trimesh.Trimesh] = []

    def bar(cx, cy, sx, sy, angle=0.0):
        b = trimesh.creation.box(extents=(sx, sy, height))
        if angle != 0.0:
            b.apply_transform(trimesh.transformations.rotation_matrix(angle, [0, 0, 1]))
        b.apply_translation([cx, cy, 0.0])
        return b

    if letter == "A":
        # two diagonals + a crossbar
        boxes.append(bar(-0.10 * extent, 0.0, t, 2 * h, angle=+0.32))
        boxes.append(bar(+0.10 * extent, 0.0, t, 2 * h, angle=-0.32))
        boxes.append(bar(0.0, -0.05 * h, 1.1 * w, t))
    else:  # 'B'
        # vertical spine + two bumps approximated by stacked horizontal + vertical bars
        boxes.append(bar(-w * 0.6, 0.0, t, 2 * h))           # spine
        boxes.append(bar(0.0, +h * 0.85, 1.1 * w, t))        # top
        boxes.append(bar(0.0, 0.0, 1.1 * w, t))              # middle
        boxes.append(bar(0.0, -h * 0.85, 1.1 * w, t))        # bottom
        boxes.append(bar(+w * 0.55, +h * 0.42, t, h))        # upper right
        boxes.append(bar(+w * 0.55, -h * 0.42, t, h))        # lower right
    return boxes


# --------------------------------------------------------------------------------------
# Key mm dimensions (manifest helper)
# --------------------------------------------------------------------------------------
def key_dims() -> dict[str, float]:
    return {
        "S_mm_per_node": float(S),
        "NODE_HALF_mm": float(NODE_HALF),
        "node_corner_dist_mm": float(NODE_CORNER_DIST),
        "R_JOINT_socket_mm": float(R_JOINT),
        "socket_depth_mm": float(SOCKET_DEPTH),
        "R_SHAFT_mm": float(R_SHAFT),
        "R_TIP_mm": float(R_TIP),
        "insert_depth_mm": float(INSERT_DEPTH),
        "bond_visible_span_mm": float(BOND_VISIBLE_SPAN),
        "bond_total_len_mm": float(BOND_TOTAL_LEN),
        "ACCENT_JOINT_mm": float(ACCENT_JOINT),
        "ACCENT_PEG_R_mm": float(ACCENT_PEG_R),
        "INTERF_MM": float(INTERF_MM),
    }
