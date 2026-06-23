"""kit_jig.py — printed BASE JIG for the AVE vacuum-lattice 3D-print kit.

Solves the unkeyed-port / assembly-order problem: a flat locator plate with one
keyed pocket per node of a finite ``build_diamond_net`` chunk, so the builder
drops each node into exactly one location and can read off, around each pocket,
which of the 4 tetrahedral ports gets a bond.

WHY A FLAT LOCATOR PLATE (not a 3D nest)
----------------------------------------
The diamond chunk does NOT lie flat: a ``build_diamond_net(4)`` active set spans
300x300x300 mm at S=100 and stacks 4 node z-layers along the body diagonal. A
single bed-conformal 3D nest is therefore impossible. Per the kit DFM contract we
emit a flat XY node-LOCATOR plate (pockets at the *projected* XY footprint of the
active nodes) plus printed per-pocket legends; the real 3D crystal is then built
*upward* off the plate, layer by layer, using the node-id + sublattice + port
marks as the wiring key. Nodes that share an XY column (stacked in z) get one
pocket each, fanned on a short arc so every node still has a unique keyed home and
the builder stacks them in id order.

WATERTIGHT BY CONSTRUCTION
--------------------------
Every returned object is a ``trimesh.Trimesh`` assembled only from
``trimesh.creation`` primitives + ``trimesh.boolean`` (engine='manifold').
No round-trip through numpy-stl. Each builder calls merge_vertices/fix_normals and
the smoke test asserts ``is_watertight`` and ``is_volume``.

GLYPHS (no shapely/freetype in env => geometric marks, not font glyphs)
-----------------------------------------------------------------------
- Sublattice key: A = embossed (raised) triangular prism; B = embossed bar.
  (Color carries the rest per the kit contract; this is the tactile/visual A/B key.)
- Node id: a raised binary-pip row (LSB..MSB) read left-to-right beside the glyph.
- Port index 1..4: raised pip clusters (1,2,3,4 dots) placed at the XY-projected
  bearing of each of the node's 4 tetrahedral ports, around the pocket rim.

All absolute sizes are [RENDERING] magnification (~2.6e11x); S = MM_PER_L_NODE_UNIT.
"""

from __future__ import annotations

import os
from collections import defaultdict

import numpy as np
import trimesh

from ave.core import chiral_lattice as cl
from generate_vacuum_lattice_stl import (
    MM_PER_L_NODE_UNIT,
    active_nodes,
    finite_crystal_bonds,
    lattice_pos_to_mm,
)
import vacuum_lc_geometry as g

S = MM_PER_L_NODE_UNIT

# ----------------------------------------------------------------------------
# Shared geometry contract (mirror the node/bond builders so the jig pockets
# accept the printed nodes). [RENDERING] fractions of S.
# ----------------------------------------------------------------------------
NODE_HALF = 0.10 * S                      # unified solid-node half-extent
POCKET_CLEAR = 0.012 * S                  # XY clearance so a printed node drops in
POCKET_HALF = NODE_HALF + POCKET_CLEAR    # pocket half-extent (square)
POCKET_DEPTH = 0.06 * S                   # shallow nesting depth
PLATE_THICK = 0.05 * S                    # baseplate thickness under pocket floor
PLATE_MARGIN = 0.18 * S                   # border around outermost pockets
CHAMFER = 0.04 * S                        # [RENDERING] elephant-foot relief hint

# Emboss marks (raised, >= 0.8 mm legible detail at S=100).
EMBOSS_H = 0.012 * S                      # raised height (>=1.2 mm @ S=100)
PIP_R = 0.011 * S                         # id/port pip radius (>=1.1 mm @ S=100)
PIP_PITCH = 0.030 * S                     # spacing between adjacent pips
GLYPH_W = 0.05 * S                        # A/B glyph footprint
PORT_RING_R = POCKET_HALF + 0.045 * S     # radius at which port-index pips sit

# Bed (Prusa i3 MK3+). Reserve a little for skirt/clearance.
BED_X = 250.0
BED_Y = 210.0
BED_USABLE_X = BED_X - 8.0
BED_USABLE_Y = BED_Y - 8.0

FRICTION_INTERFERENCE_MM = float(
    os.environ.get("KIT_FRICTION_INTERFERENCE_MM", "0.05")
)


# ----------------------------------------------------------------------------
# Watertight primitive helpers
# ----------------------------------------------------------------------------
def _finalize(tm: trimesh.Trimesh) -> trimesh.Trimesh:
    """merge_vertices + fix_normals; return the cleaned manifold."""
    tm.merge_vertices()
    tm.fix_normals()
    return tm


def _box(extents, center) -> trimesh.Trimesh:
    b = trimesh.creation.box(extents=extents)
    b.apply_translation(np.asarray(center, dtype=float))
    return b


def _cyl(radius, height, center, axis=(0, 0, 1)) -> trimesh.Trimesh:
    c = trimesh.creation.cylinder(radius=radius, height=height, sections=24)
    axis = np.asarray(axis, dtype=float)
    axis = axis / (np.linalg.norm(axis) + 1e-12)
    z = np.array([0.0, 0.0, 1.0])
    if not np.allclose(axis, z):
        v = np.cross(z, axis)
        s = np.linalg.norm(v)
        if s > 1e-9:
            ang = np.arccos(np.clip(np.dot(z, axis), -1, 1))
            c.apply_transform(trimesh.transformations.rotation_matrix(ang, v))
    c.apply_translation(np.asarray(center, dtype=float))
    return c


def _tri_prism(center, width, height_z) -> trimesh.Trimesh:
    """Equilateral-ish triangular prism standing on the plate (A glyph)."""
    h = width * np.sqrt(3.0) / 2.0
    poly = np.array(
        [[-width / 2, -h / 3], [width / 2, -h / 3], [0.0, 2 * h / 3]]
    )
    import trimesh.creation as tc

    # extrude_triangulation is robust without shapely
    verts2d = poly
    faces2d = np.array([[0, 1, 2]])
    pr = tc.extrude_triangulation(verts2d, faces2d, height=height_z)
    pr.apply_translation(np.asarray(center, dtype=float))
    return pr


def _union(parts) -> trimesh.Trimesh:
    parts = [p for p in parts if p is not None and len(p.faces) > 0]
    if len(parts) == 1:
        return parts[0]
    out = trimesh.boolean.union(parts, engine="manifold")
    if out is None or len(out.faces) == 0:
        raise RuntimeError("union failed")
    return out


def _difference(a, b) -> trimesh.Trimesh:
    out = trimesh.boolean.difference([a, b], engine="manifold")
    if out is None or len(out.faces) == 0:
        raise RuntimeError("difference failed")
    return out


# ----------------------------------------------------------------------------
# Mark builders (all RAISED so they survive a flat-bottom plate boolean)
# ----------------------------------------------------------------------------
def _id_pips(n: int, origin_xy, top_z: float) -> list[trimesh.Trimesh]:
    """Raised binary-pip row encoding node id n (LSB first)."""
    bits = max(1, n.bit_length())
    pips = []
    for i in range(bits):
        if (n >> i) & 1:
            cx = origin_xy[0] + i * PIP_PITCH
            cy = origin_xy[1]
            pips.append(
                _cyl(PIP_R, EMBOSS_H, (cx, cy, top_z + EMBOSS_H / 2.0))
            )
    return pips


def _sublattice_glyph(sub: str, center_xy, top_z: float) -> trimesh.Trimesh:
    """A = raised triangular prism; B = raised bar."""
    if sub == "A":
        return _tri_prism(
            (center_xy[0], center_xy[1] - GLYPH_W / 4.0, top_z), GLYPH_W, EMBOSS_H
        )
    return _box(
        (GLYPH_W, GLYPH_W * 0.34, EMBOSS_H),
        (center_xy[0], center_xy[1], top_z + EMBOSS_H / 2.0),
    )


def _port_pips(port_dirs, center_xy, top_z: float) -> list[trimesh.Trimesh]:
    """For each tetrahedral port (1..4): raised dot-cluster at its XY bearing.

    Port index k gets k pips so the builder reads which bond goes where without a
    legend. Ports whose XY projection is ~degenerate (axis nearly vertical) are
    fanned onto distinct bearings so all 4 stay legible.
    """
    parts: list[trimesh.Trimesh] = []
    bearings = []
    for d in port_dirs:
        ang = np.arctan2(d[1], d[0]) if (abs(d[0]) + abs(d[1])) > 1e-6 else None
        bearings.append(ang)
    # assign fallback bearings for vertical ports
    used = [b for b in bearings if b is not None]
    fan = np.linspace(0, 2 * np.pi, 4, endpoint=False)
    fi = 0
    for k, ang in enumerate(bearings):
        if ang is None:
            ang = fan[fi]
            fi += 1
        bx = center_xy[0] + PORT_RING_R * np.cos(ang)
        by = center_xy[1] + PORT_RING_R * np.sin(ang)
        # k+1 pips in a short tangential row
        npips = k + 1
        for j in range(npips):
            off = (j - (npips - 1) / 2.0) * (PIP_R * 2.4)
            ox = bx - np.sin(ang) * off
            oy = by + np.cos(ang) * off
            parts.append(_cyl(PIP_R * 0.8, EMBOSS_H, (ox, oy, top_z + EMBOSS_H / 2)))
    return parts


# ----------------------------------------------------------------------------
# Net -> keyed pocket layout
# ----------------------------------------------------------------------------
def _net_layout(L: int = 4):
    """Return (node_records, bonds). Each record: id, sublattice, xy(centred),
    port_dirs(4). Stacked-in-z nodes sharing an XY column are fanned on a small
    arc so each gets a unique pocket."""
    net = cl.build_diamond_net(L)
    bonds = finite_crystal_bonds(net)
    act = sorted(active_nodes(bonds))
    pos = lattice_pos_to_mm(net)

    # group active nodes by XY column
    cols: dict[tuple, list[int]] = defaultdict(list)
    for i in act:
        key = (round(pos[i][0], 1), round(pos[i][1], 1))
        cols[key].append(i)

    records = []
    fan_r = POCKET_HALF * 1.4
    for (cx, cy), ids in cols.items():
        ids = sorted(ids)
        m = len(ids)
        for j, i in enumerate(ids):
            if m == 1:
                ox, oy = cx, cy
            else:
                a = (j - (m - 1) / 2.0) * (np.pi / 3.0)
                ox = cx + fan_r * np.cos(np.pi / 2 + a)
                oy = cy + fan_r * np.sin(np.pi / 2 + a)
            sub = g.diamond_sublattice(net, i)
            port_dirs = list(g.kit_port_directions(sub))  # 4 unit vectors
            records.append(
                {
                    "id": int(i),
                    "sub": sub,
                    "xy": np.array([ox, oy]),
                    "ports": port_dirs,
                    "col_z": int(j),  # build-up order in this column
                }
            )
    # recentre layout on origin
    allxy = np.array([r["xy"] for r in records])
    mid = (allxy.max(0) + allxy.min(0)) / 2.0
    for r in records:
        r["xy"] = r["xy"] - mid
    return records, bonds


def _build_plate(records, x0, x1, y0, y1) -> trimesh.Trimesh:
    """Build one watertight locator plate covering [x0,x1]x[y0,y1] with the
    pockets + marks for the records whose centre falls inside."""
    sel = [r for r in records if x0 <= r["xy"][0] <= x1 and y0 <= r["xy"][1] <= y1]
    if not sel:
        raise RuntimeError("no nodes in this tile range")

    xs = np.array([r["xy"][0] for r in sel])
    ys = np.array([r["xy"][1] for r in sel])
    px0, px1 = xs.min() - PLATE_MARGIN, xs.max() + PLATE_MARGIN
    py0, py1 = ys.min() - PLATE_MARGIN, ys.max() + PLATE_MARGIN
    ext_x = px1 - px0
    ext_y = py1 - py0
    plate_total_h = PLATE_THICK + POCKET_DEPTH
    cx = (px0 + px1) / 2.0
    cy = (py0 + py1) / 2.0
    top_z = plate_total_h  # marks sit on the top face

    plate = _box((ext_x, ext_y, plate_total_h), (cx, cy, plate_total_h / 2.0))

    # carve pockets (square pockets from the top)
    pockets = []
    for r in sel:
        pcx, pcy = r["xy"]
        pockets.append(
            _box(
                (2 * POCKET_HALF, 2 * POCKET_HALF, POCKET_DEPTH + 1.0),
                (pcx, pcy, plate_total_h - POCKET_DEPTH / 2.0 + 0.5),
            )
        )
    plate = _difference(plate, _union(pockets))

    # add raised marks per node
    marks = []
    for r in sel:
        pcx, pcy = r["xy"]
        # sublattice glyph + id pips placed just outside the +Y pocket edge
        glyph_xy = (pcx - GLYPH_W, pcy + POCKET_HALF + 0.03 * S)
        marks.append(_sublattice_glyph(r["sub"], glyph_xy, top_z))
        id_origin = (pcx, pcy + POCKET_HALF + 0.03 * S)
        marks.extend(_id_pips(r["id"], id_origin, top_z))
        marks.extend(_port_pips(r["ports"], (pcx, pcy), top_z))

    out = _union([plate, *marks])
    return _finalize(out)


# ----------------------------------------------------------------------------
# Public builders
# ----------------------------------------------------------------------------
def assembly_jig(L: int = 4) -> dict[str, trimesh.Trimesh]:
    """Tileable flat node-LOCATOR plate(s) for a build_diamond_net(L) chunk.

    Returns {tile_name: Trimesh}. The footprint is auto-tiled to fit the
    250x210 mm Prusa bed; each tile is a standalone watertight plate carrying
    the pockets + node-id/sublattice/port marks for the nodes inside it.

    The 3D crystal is built UPWARD off these plates: each pocket's id + 'col_z'
    order tells the builder the z-stacking sequence within an XY column; the
    port pips (1..4) tell which tetrahedral bond seats where.
    """
    records, _bonds = _net_layout(L)
    allxy = np.array([r["xy"] for r in records])
    span_x = allxy[:, 0].max() - allxy[:, 0].min() + 2 * PLATE_MARGIN
    span_y = allxy[:, 1].max() - allxy[:, 1].min() + 2 * PLATE_MARGIN

    nx = int(np.ceil(span_x / BED_USABLE_X))
    ny = int(np.ceil(span_y / BED_USABLE_Y))
    nx = max(nx, 1)
    ny = max(ny, 1)

    x_lo = allxy[:, 0].min() - PLATE_MARGIN
    y_lo = allxy[:, 1].min() - PLATE_MARGIN
    tile_w = span_x / nx
    tile_h = span_y / ny

    tiles: dict[str, trimesh.Trimesh] = {}
    for ix in range(nx):
        for iy in range(ny):
            x0 = x_lo + ix * tile_w
            x1 = x0 + tile_w + 1e-3
            y0 = y_lo + iy * tile_h
            y1 = y0 + tile_h + 1e-3
            try:
                plate = _build_plate(records, x0, x1, y0, y1)
            except RuntimeError:
                continue  # empty tile
            tiles[f"jig_tile_{ix}_{iy}"] = plate
    return tiles


def unit_cell_jig() -> trimesh.Trimesh:
    """Standalone hero-print jig: 2 keyed pockets (one A, one B) + 4 port-pip
    fans, sized for the 2-node + 4-bond unit cell. Single watertight plate, fits
    the bed easily."""
    net = cl.build_diamond_net(4)
    bonds = finite_crystal_bonds(net)
    # pick one bonded A-B pair
    u, v = bonds[0]
    pos = lattice_pos_to_mm(net)
    su = g.diamond_sublattice(net, u)
    sv = g.diamond_sublattice(net, v)
    a_id, a_sub = (u, su) if su == "A" else (v, sv)
    b_id, b_sub = (v, sv) if su == "A" else (u, su)

    sep = 2.4 * POCKET_HALF + 0.06 * S
    records = [
        {
            "id": int(a_id),
            "sub": "A",
            "xy": np.array([-sep / 2.0, 0.0]),
            "ports": list(g.kit_port_directions("A")),
            "col_z": 0,
        },
        {
            "id": int(b_id),
            "sub": "B",
            "xy": np.array([sep / 2.0, 0.0]),
            "ports": list(g.kit_port_directions("B")),
            "col_z": 0,
        },
    ]
    xs = [r["xy"][0] for r in records]
    ys = [r["xy"][1] for r in records]
    return _build_plate(records, min(xs) - 1, max(xs) + 1, min(ys) - 1, max(ys) + 1)


def standoff_posts(L: int = 4) -> dict[str, trimesh.Trimesh]:
    """Graded-height support posts (the 'stepped' tier of the jig).

    The flat base plate only locates the BOTTOM node layer; upper-layer nodes would
    otherwise float on oblique bonds while their glue sets. These posts hold an upper
    node at (approximately) its true Z during a progressive glue-up: one post per
    distinct above-base node z-level (the builder reuses a post for every node at that
    level), each a wide stable foot + square column + a top square cradle that seats a
    node. Build bottom-up: locate the bottom layer in the base plate, prop each next
    node on the matching standoff, press+glue its bonds, let it cure, move up.

    At S=100 the L4 chunk spans ~300 mm in Z, so the tallest posts exceed the Prusa
    bed Z; the driver flags this and recommends KIT_PRINT_MM_PER_L_NODE=60 for a
    jig-assisted full build (Z span ~180 mm, all posts printable).
    """
    net = cl.build_diamond_net(L)
    bonds = finite_crystal_bonds(net)
    act = sorted(active_nodes(bonds))
    pos = lattice_pos_to_mm(net)
    zs = sorted({round(float(pos[i][2]), 1) for i in act})
    zmin = zs[0]

    side = 2.0 * POCKET_HALF + 2.0 * (0.03 * S)   # square column around the cradle
    foot = side * 1.6                              # wide stable foot
    foot_h = 0.04 * S
    posts: dict[str, trimesh.Trimesh] = {}
    for lvl, z in enumerate(zs):
        h = z - zmin                               # height of this layer above the base
        if h <= 0.1:
            continue                               # bottom layer rides the base plate
        col_h = float(h)
        base = _box((foot, foot, foot_h), (0.0, 0.0, foot_h / 2.0))
        col = _box((side, side, col_h), (0.0, 0.0, foot_h + col_h / 2.0))
        post = _union([base, col])
        top_z = foot_h + col_h
        cradle = _box((2 * POCKET_HALF, 2 * POCKET_HALF, POCKET_DEPTH + 1.0),
                      (0.0, 0.0, top_z - POCKET_DEPTH / 2.0 + 0.5))
        post = _difference(post, cradle)
        posts[f"standoff_post_z{lvl}_h{int(round(h))}mm"] = _finalize(post)
    return posts


def jig_spec() -> dict:
    """Manifest-ready jig dimensions (mm)."""
    return {
        "pocket_half_mm": float(POCKET_HALF),
        "pocket_depth_mm": float(POCKET_DEPTH),
        "node_half_mm": float(NODE_HALF),
        "pocket_clearance_mm": float(POCKET_CLEAR),
        "plate_thickness_mm": float(PLATE_THICK + POCKET_DEPTH),
        "emboss_height_mm": float(EMBOSS_H),
        "pip_radius_mm": float(PIP_R),
        "bed_usable_mm": [BED_USABLE_X, BED_USABLE_Y],
        "friction_interference_mm": FRICTION_INTERFERENCE_MM,
        "fdm_target_printer": "Prusa i3 MK3+ (0.4 mm nozzle)",
    }
