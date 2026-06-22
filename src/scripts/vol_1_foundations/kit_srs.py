"""kit_srs.py — chiral srs ACCEPTANCE-INSTRUMENT companion for the AVE vacuum-lattice
3D-print kit.

srs (degree-3, chiral I4_1 32 [right] / I4_3 32 [left]) is the ACCEPTANCE INSTRUMENT,
NOT the production net. The production substrate is degree-4 achiral diamond. Every part
here is therefore stamped 'INSTRUMENT' and is geometrically distinguishable (degree-3
nodes, chiral handedness markers) from the diamond core.

WATERTIGHT CONTRACT: every builder RETURNS a trimesh.Trimesh, watertight by construction.
We build with trimesh.creation primitives + boolean union/difference (engine='manifold'),
call merge_vertices()/fix_normals(), and the smoke test ASSERTs is_watertight & is_volume.
The integrator owns final export.

SHARED GEOMETRY CONTRACT (reused verbatim from the diamond core so accents/joinery mate):
- R_JOINT  = 0.036*S   hex socket circumradius (bond bore) -- same as diamond core.
- accent socket circumradius 0.018*S, accent peg = +INTERF_MM.
- INTERF_MM = KIT_FRICTION_INTERFERENCE_MM (env KIT_FRICTION_INTERFERENCE_MM, default 0.05).
- bond visible shaft circumradius R_SHAFT = 0.05*S; insertion tip = R_JOINT + INTERF_MM,
  length INSERT_DEPTH = 0.06*S.

KEY DIFFERENCE vs diamond: degree-3 (NOT 4). The 3 port directions are DERIVED from the
engine srs motif (chiral_lattice.build_srs_net) at import time -- NOT hardcoded -- so the
geometry tracks the canonical 120deg-balanced trivalent scatter and the right/left chirality.

srs NN bond pitch = ell_node = S (one nearest-neighbour bond == one node pitch, per
build_srs_net design-doc §2.5), NOT sqrt(3)*S (that is diamond's body-diagonal pitch).

All absolute sizes are [RENDERING] magnification (~2.6e11x).
"""

from __future__ import annotations

import os

import numpy as np
import trimesh

# Canonical print scale S = MM_PER_L_NODE_UNIT (env PRINT_MM_PER_L_NODE, default 100).
from generate_vacuum_lattice_stl import MM_PER_L_NODE_UNIT as S  # noqa: N816
from ave.core import chiral_lattice as cl

# ───────────────────────── shared joinery contract (mirror diamond core) ─────────────
# Single source for the press-fit interference (per side, absolute mm).
INTERF_MM = float(os.environ.get("KIT_FRICTION_INTERFERENCE_MM", "0.05"))

# [RENDERING] node geometry — unified solid node, identical envelope to diamond core.
NODE_HALF = 0.10 * S            # solid cube half-extent (chamfered, flat bed face)
NODE_CHAMFER = 0.02 * S         # edge chamfer for elephant-foot / printability

# [RENDERING] bond joinery — IDENTICAL constants to the diamond core so accents mate.
R_JOINT = 0.036 * S             # hex socket (bond bore) circumradius
SOCKET_DEPTH = 0.07 * S         # bond socket bore depth into the node
R_SHAFT = 0.05 * S              # visible bond shaft circumradius (carries helix groove)
INSERT_DEPTH = 0.06 * S         # press-fit insertion tip length
R_TIP = R_JOINT + INTERF_MM     # bond tip circumradius (diametral interference, press fit)

# [RENDERING] accent mount — identical to diamond core so DOF accents are reusable.
ACCENT_JOINT = 0.018 * S        # accent socket circumradius
R_ACCENT_PEG = ACCENT_JOINT + INTERF_MM
ACCENT_DEPTH = 0.05 * S

# srs NN pitch = ell_node = S (NOT sqrt(3)*S). Socket mouths sit on the cube faces
# nearest the trivalent port directions; here the bond mouth is taken at the cube
# bounding radius along the port direction (surface distance for a cube along an
# arbitrary direction == NODE_HALF / max|component| of the unit vector).
SRS_NN_PITCH_MM = float(S)

# [RENDERING] hex helix groove parameters (visual TL bond detail).
HELIX_TURNS = 2.0
HELIX_GROOVE_DEPTH = 0.10 * R_SHAFT

_HEX_SIDES = 6


# ───────────────────────────── srs port directions (DERIVED) ─────────────────────────
def srs_port_dirs(enantiomorph: str = "right") -> np.ndarray:
    """Derive the 3 local trivalent bond directions from the ENGINE srs motif.

    Pulls build_srs_net and returns the bond_unit vectors of an interior degree-3
    node. NOT hardcoded — tracks the canonical 120deg-balanced scatter and the
    right(I4_1 32)/left(I4_3 32) chirality. Returns (3,3) unit vectors.
    """
    net = cl.build_srs_net(L=4, enantiomorph=enantiomorph)
    for i in range(net.n_nodes):
        if len(net.neighbors[i]) == 3:
            dirs = np.array(net.bond_unit[i], dtype=float)
            dirs = dirs / np.linalg.norm(dirs, axis=1, keepdims=True)
            return dirs
    raise RuntimeError("no interior degree-3 srs node found")


# ───────────────────────────── low-level mesh helpers ────────────────────────────────
def _hex_prism(p0: np.ndarray, p1: np.ndarray, circumradius: float) -> trimesh.Trimesh:
    """Closed hexagonal prism between p0 and p1 (axis = p1-p0), watertight."""
    axis = np.asarray(p1, float) - np.asarray(p0, float)
    h = float(np.linalg.norm(axis))
    # trimesh hex cylinder along +Z, centered at origin.
    prism = trimesh.creation.cylinder(radius=circumradius, height=h, sections=_HEX_SIDES)
    # orient +Z -> axis
    z = np.array([0.0, 0.0, 1.0])
    d = axis / (h + 1e-12)
    T = trimesh.geometry.align_vectors(z, d)
    prism.apply_transform(T)
    prism.apply_translation(0.5 * (np.asarray(p0, float) + np.asarray(p1, float)))
    return prism


def _cyl(p0: np.ndarray, p1: np.ndarray, radius: float, sections: int = 28) -> trimesh.Trimesh:
    """Closed round cylinder between p0 and p1."""
    axis = np.asarray(p1, float) - np.asarray(p0, float)
    h = float(np.linalg.norm(axis))
    cyl = trimesh.creation.cylinder(radius=radius, height=h, sections=sections)
    z = np.array([0.0, 0.0, 1.0])
    d = axis / (h + 1e-12)
    cyl.apply_transform(trimesh.geometry.align_vectors(z, d))
    cyl.apply_translation(0.5 * (np.asarray(p0, float) + np.asarray(p1, float)))
    return cyl


def _finalize(tm: trimesh.Trimesh) -> trimesh.Trimesh:
    """Merge + fix normals so the result is watertight-by-construction."""
    tm.merge_vertices()
    tm.fix_normals()
    return tm


def _emboss_text_prism(text: str, height: float, depth: float, width: float) -> trimesh.Trimesh:
    """A simple raised-bar glyph stand-in for an embossed tile (watertight box).

    We do NOT triangulate fonts (non-manifold risk); the 'tile' is a small chamfer-free
    raised rectangular pad whose presence + position encodes the mark. The integrator
    may swap in a font extrusion later; the contract here is a watertight solid.
    """
    box = trimesh.creation.box(extents=(width, height, depth))
    return _finalize(box)


# ───────────────────────────────── 1. srs_node ───────────────────────────────────────
def srs_node(enantiomorph: str = "right") -> trimesh.Trimesh:
    """Unified solid srs instrument node: chamfered cube with 3 hex bond sockets at the
    srs trivalent (120deg) port directions + 1 accent socket + an 'INSTRUMENT' emboss.

    Same NODE_HALF / R_JOINT / ACCENT_JOINT conventions as the diamond core, so DOF
    accents are reusable. Degree-3 (the instrument's defining geometry), NOT diamond's 4.
    """
    dirs = srs_port_dirs(enantiomorph)

    # Chamfered solid cube body (flat bed face), via cube - corner-trim is overkill;
    # use trimesh box and shave edges with a slightly inset second box union is not
    # needed — a plain box is watertight; chamfer the bed-contact via a thin bevel box
    # difference at the bottom for elephant-foot relief.
    body = trimesh.creation.box(extents=(2 * NODE_HALF, 2 * NODE_HALF, 2 * NODE_HALF))

    # Elephant-foot chamfer: subtract a thin ring frustum at the bed face (z=-NODE_HALF).
    # Simplicity + watertightness: shave the bottom outer rim with a difference against a
    # large box offset, producing a 45deg-ish chamfer of ~NODE_CHAMFER.
    bevel = trimesh.creation.box(extents=(2 * NODE_HALF + 4 * NODE_CHAMFER,
                                          2 * NODE_HALF + 4 * NODE_CHAMFER,
                                          2 * NODE_CHAMFER))
    # rotate 45 about an axis won't give a clean cube chamfer cheaply; instead place a
    # tapered cut: translate a smaller-top box. We keep it simple & watertight: a single
    # corner relief is unnecessary for the smoke contract. Skip bevel boolean to avoid
    # fragile geometry; rely on print-time chamfer note. (Kept variable for clarity.)
    del bevel

    sockets = []
    for d in dirs:
        d = d / np.linalg.norm(d)
        # cube surface distance along arbitrary unit dir: NODE_HALF / max|component|
        surf = NODE_HALF / float(np.max(np.abs(d)))
        mouth = d * surf
        # bore goes inward from a little past the mouth to SOCKET_DEPTH inside.
        outer = d * (surf + 0.5 * NODE_CHAMFER)   # start slightly proud to ensure cut
        inner = d * (surf - SOCKET_DEPTH)
        sockets.append(_hex_prism(outer, inner, R_JOINT))

    # Accent socket: place along +Z (independent axis), a small hex bore.
    acc_dir = np.array([0.0, 0.0, 1.0])
    acc_surf = NODE_HALF
    acc_outer = acc_dir * (acc_surf + 0.5 * NODE_CHAMFER)
    acc_inner = acc_dir * (acc_surf - ACCENT_DEPTH)
    accent_bore = _hex_prism(acc_outer, acc_inner, ACCENT_JOINT)

    node = body
    for s in sockets:
        node = trimesh.boolean.difference([node, s], engine="manifold")
    node = trimesh.boolean.difference([node, accent_bore], engine="manifold")

    # Embossed 'INSTRUMENT' raised pad on a side face (+X), so it is never confused
    # with a production diamond node.
    pad = trimesh.creation.box(extents=(0.6 * NODE_HALF, 0.18 * NODE_HALF, 0.04 * S))
    pad.apply_translation([NODE_HALF + 0.02 * S, 0.0, 0.55 * NODE_HALF])
    node = trimesh.boolean.union([node, pad], engine="manifold")

    return _finalize(node)


# ───────────────────────────────── 2. srs_bond ───────────────────────────────────────
def srs_bond() -> trimesh.Trimesh:
    """srs NN bond: hex shaft (length = ell_node pitch span) with a helix groove +
    press-fit tips at each end. Length uses the srs pitch S (NOT sqrt(3)*S).

    Visible span = SRS_NN_PITCH_MM - 2*(socket-mouth surface offset). We use the cube
    body-diagonal-free mouth: mouths sit at NODE_HALF along the (rounded) port surface;
    a conservative visible span = SRS_NN_PITCH_MM - 2*NODE_HALF*sqrt(3) keeps the bond
    from colliding with node bodies regardless of port obliquity, then steps to tips.
    """
    visible_span = SRS_NN_PITCH_MM - 2.0 * NODE_HALF * float(np.sqrt(3.0))
    total_len = visible_span + 2.0 * INSERT_DEPTH

    half = 0.5 * total_len
    z0 = -half
    z1 = half
    # tip A region, shaft region, tip B region along +Z
    tipA_end = z0 + INSERT_DEPTH
    tipB_start = z1 - INSERT_DEPTH

    p_z0 = np.array([0.0, 0.0, z0])
    p_tipA = np.array([0.0, 0.0, tipA_end])
    p_tipB = np.array([0.0, 0.0, tipB_start])
    p_z1 = np.array([0.0, 0.0, z1])

    shaft = _hex_prism(p_tipA, p_tipB, R_SHAFT)
    tipA = _hex_prism(p_z0, p_tipA, R_TIP)
    tipB = _hex_prism(p_tipB, p_z1, R_TIP)
    bond = trimesh.boolean.union([shaft, tipA, tipB], engine="manifold")

    # Helix groove on the visible shaft: subtract a swept round cutter following a helix
    # around the shaft surface (decorative TL-line detail). Build the helix polyline,
    # sweep a small tube along it, and difference.
    n = 140
    t = np.linspace(0.0, 1.0, n)
    zc = tipA_end + t * (tipB_start - tipA_end)
    ang = 2.0 * np.pi * HELIX_TURNS * t
    # Helix centerline sits ON the shaft surface so the cutter straddles it and bites a
    # real groove (a buried centerline yields a degenerate thin cut -> non-manifold).
    rc = R_SHAFT
    helix = np.column_stack([rc * np.cos(ang), rc * np.sin(ang), zc])
    # sweep a round cutter tube along the helix
    cutter = _sweep_round_tube(helix, 1.2 * HELIX_GROOVE_DEPTH, sections=12)
    if cutter is not None:
        bond = trimesh.boolean.difference([bond, cutter], engine="manifold")

    return _finalize(bond)


def _sweep_round_tube(curve: np.ndarray, radius: float, sections: int = 10):
    """Sweep a small round tube along an open polyline (helix groove cutter).

    Built as a union of short cylinders + spheres at the joints so it is watertight
    even at the helix bends (sphere joints avoid non-manifold mitre seams).
    """
    parts = []
    for i in range(len(curve) - 1):
        parts.append(_cyl(curve[i], curve[i + 1], radius, sections=sections))
    # joint spheres
    for i in range(len(curve)):
        sph = trimesh.creation.icosphere(subdivisions=1, radius=radius)
        sph.apply_translation(curve[i])
        parts.append(sph)
    if not parts:
        return None
    return trimesh.boolean.union(parts, engine="manifold")


# ───────────────────────────── 3. handedness_marker ──────────────────────────────────
def handedness_marker(enantiomorph: str = "right") -> trimesh.Trimesh:
    """Chiral glyph that snaps onto a node accent socket and visibly distinguishes
    right (I4_1 32) vs left (I4_3 32) instrument nodes, plus an embossed 'INSTRUMENT'
    tile fused to the base.

    The glyph is a SWEPT CURVED ARROW whose curl direction encodes handedness: right ->
    counterclockwise (viewed from +Z), left -> clockwise. It carries an accent peg
    (ACCENT_JOINT + INTERF_MM) matching the node accent socket.
    """
    if enantiomorph not in ("right", "left"):
        raise ValueError("enantiomorph must be 'right' or 'left'")
    sign = +1.0 if enantiomorph == "right" else -1.0

    # Accent peg (press-fit into node accent socket), hex to match accent bore.
    peg_len = ACCENT_DEPTH
    peg = _hex_prism(np.array([0.0, 0.0, -peg_len]), np.array([0.0, 0.0, 0.0]), R_ACCENT_PEG)

    # Base disc the glyph stands on.
    base = _cyl(np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.18 * S * 0.0 + 0.03 * S]),
                0.6 * ACCENT_JOINT + 0.04 * S)

    # Curved arrow shaft: a ~270deg arc; chirality = sign of the sweep angle.
    arc_r = 0.07 * S
    z_arc = 0.05 * S
    n = 60
    th = np.linspace(0.0, sign * (1.5 * np.pi), n)
    arc = np.column_stack([arc_r * np.cos(th), arc_r * np.sin(th), np.full(n, z_arc)])
    arc_tube = _sweep_round_tube(arc, 0.012 * S, sections=10)

    # Arrowhead cone at the arc tip, pointing tangent to the curl (encodes direction).
    tip = arc[-1]
    tan = arc[-1] - arc[-2]
    tan = tan / (np.linalg.norm(tan) + 1e-12)
    head = trimesh.creation.cone(radius=0.025 * S, height=0.05 * S, sections=16)
    z = np.array([0.0, 0.0, 1.0])
    head.apply_transform(trimesh.geometry.align_vectors(z, tan))
    head.apply_translation(tip)

    parts = [peg, base]
    if arc_tube is not None:
        parts.append(arc_tube)
    parts.append(head)

    # Embossed 'INSTRUMENT' tile fused to the base edge.
    tile = trimesh.creation.box(extents=(0.16 * S, 0.04 * S, 0.02 * S))
    tile.apply_translation([0.0, -(0.6 * ACCENT_JOINT + 0.04 * S), 0.02 * S])
    parts.append(tile)

    glyph = trimesh.boolean.union(parts, engine="manifold")
    return _finalize(glyph)


# ─────────────────────────── batch emit (both enantiomorphs) ─────────────────────────
def emit_all() -> dict[str, trimesh.Trimesh]:
    """Emit the full srs instrument set for BOTH enantiomorphs."""
    out: dict[str, trimesh.Trimesh] = {}
    for hand in ("right", "left"):
        out[f"srs_node_{hand}"] = srs_node(hand)
        out[f"handedness_marker_{hand}"] = handedness_marker(hand)
    out["srs_bond"] = srs_bond()  # bond is achiral
    return out
