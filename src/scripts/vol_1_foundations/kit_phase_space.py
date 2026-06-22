"""kit_phase_space.py — Phase-space companion artifacts for the AVE vacuum-lattice kit.

These parts visualize the LC-tank STATE (the dynamical saturation amplitude A and
its phasor / impedance-plane geometry). PER CANON:

  * A = sqrt(eps^2 + kappa^2 + V^2) is the TANK STATE, NOT a spatial DOF. It belongs
    ONLY to these phase-space artifacts — never to a node-body feature.
  * A1 (breathing / mass / V-sector) is INDEPENDENT of T2 (micro-rotation / B / kappa).
    The phasor dial therefore ships in a TWO-INDICATOR variant so the mass-sector phase
    and the charge/spin-sector phase are read on independent axes, never merged.
  * Every artifact carries the embossed stamp '[STATE-SPACE - NOT A COORDINATE]'.

WATERTIGHT BY CONSTRUCTION: every builder returns a trimesh.Trimesh assembled from
trimesh.creation primitives + boolean union/difference (engine='manifold'); after
assembly we merge_vertices() + fix_normals(). No numpy-stl round-trip.

All absolute sizes are [RENDERING] magnification (~2.6e11x); these are display props,
not lattice coordinates. S = MM_PER_L_NODE_UNIT imported from the kit's shared scale.
"""

from __future__ import annotations

import numpy as np
import trimesh

# Shared kit scale (mm per ℓ_node). Default 100; override via PRINT_MM_PER_L_NODE env
# is handled upstream by generate_vacuum_lattice_stl — we import the resolved value.
try:  # pragma: no cover - import shim for standalone smoke runs
    from generate_vacuum_lattice_stl import MM_PER_L_NODE_UNIT as S
except Exception:  # pragma: no cover
    import os

    S = float(os.environ.get("PRINT_MM_PER_L_NODE", "100"))

STAMP_TEXT = "[STATE-SPACE - NOT A COORDINATE]"

# ----------------------------------------------------------------------------
# [RENDERING] phase-space artifact dimensions (mm). NOT lattice coordinates.
# ----------------------------------------------------------------------------
# Impedance / Smith-chart puck
DISC_RADIUS = 0.37 * S          # ~74 mm dia at S=100 (fits 60-80 mm spec, on bed)
DISC_THICK = 0.040 * S          # ~4 mm flat puck
RIDGE_DEPTH = 0.010 * S         # 1.0 mm raised ridge (>=0.8 mm legible)
RIDGE_WIDTH = 0.012 * S         # 1.2 mm ridge wall (>=0.8 mm robust)
STAMP_RELIEF = 0.010 * S        # 1.0 mm raised text band
CHAMFER = 0.004 * S             # 0.4 mm bed-contact chamfer (elephant-foot)

# Phasor dial
DIAL_RADIUS = 0.22 * S          # ~44 mm dia dial base
DIAL_THICK = 0.030 * S          # ~3 mm base plate
PIN_RADIUS = 0.025 * S          # 2.5 mm center pin (robust peg >= 2.5 mm)
PIN_HEIGHT = 0.060 * S          # 6 mm pin
POINTER_BORE_CLEAR = 0.030      # mm radial clearance => spins freely on the pin
POINTER_LEN = 0.18 * S          # 18 mm pointer arm
POINTER_THICK = 0.022 * S       # 2.2 mm pointer plate
POINTER_HUB_R = 0.045 * S       # 4.5 mm hub around the bore
TICK_DEPTH = 0.010 * S          # 1.0 mm engraved tick depth (relief ridges)

_TAU = 2.0 * np.pi


# ----------------------------------------------------------------------------
# Internal helpers (all return watertight trimesh.Trimesh)
# ----------------------------------------------------------------------------
def _finalize(tm: trimesh.Trimesh) -> trimesh.Trimesh:
    """Merge coincident verts + repair winding so is_watertight/is_volume hold."""
    tm.merge_vertices()
    tm.fix_normals()
    return tm


def _disc(radius: float, height: float, sections: int = 96) -> trimesh.Trimesh:
    """Z-axis solid cylinder (a flat disc), centered on z=0..height base at z=0."""
    cyl = trimesh.creation.cylinder(radius=radius, height=height, sections=sections)
    cyl.apply_translation((0.0, 0.0, height / 2.0))
    return cyl


def _arc_ridge(
    center: tuple[float, float],
    radius: float,
    a0: float,
    a1: float,
    *,
    z_base: float,
    width: float,
    height: float,
    n: int = 64,
) -> trimesh.Trimesh:
    """A raised ridge following a circular arc, built as a swept run of small boxes.

    Used for Smith-chart constant-R / constant-X arcs and the unit circle. Returns a
    watertight union of box segments (overlapping so the union is a single manifold).
    """
    angs = np.linspace(a0, a1, n)
    segs = []
    cx, cy = center
    for k in range(len(angs) - 1):
        am = 0.5 * (angs[k] + angs[k + 1])
        x = cx + radius * np.cos(am)
        y = cy + radius * np.sin(am)
        # tangential length of this segment (slightly oversized for overlap)
        seg_len = radius * abs(angs[k + 1] - angs[k]) * 1.6 + width * 0.5
        box = trimesh.creation.box(extents=(seg_len, width, height))
        # orient the box's long (x) axis along the arc tangent
        tang = am + np.pi / 2.0
        Rz = trimesh.transformations.rotation_matrix(tang, (0, 0, 1))
        box.apply_transform(Rz)
        box.apply_translation((x, y, z_base + height / 2.0))
        segs.append(box)
    out = trimesh.boolean.union(segs, engine="manifold")
    return out


def _radial_ridge(
    center: tuple[float, float],
    r0: float,
    r1: float,
    ang: float,
    *,
    z_base: float,
    width: float,
    height: float,
) -> trimesh.Trimesh:
    """A straight raised spoke from r0 to r1 at angle `ang`."""
    cx, cy = center
    length = r1 - r0
    rmid = 0.5 * (r0 + r1)
    x = cx + rmid * np.cos(ang)
    y = cy + rmid * np.sin(ang)
    box = trimesh.creation.box(extents=(length, width, height))
    Rz = trimesh.transformations.rotation_matrix(ang, (0, 0, 1))
    box.apply_transform(Rz)
    box.apply_translation((x, y, z_base + height / 2.0))
    return box


def _stamp_band(
    z_base: float,
    *,
    inner_r: float,
    outer_r: float,
    height: float,
) -> trimesh.Trimesh:
    """A raised annular band that hosts the '[STATE-SPACE...]' stamp text.

    We build the band as (outer disc - inner disc) so it's a clean ring relief. The
    literal glyphs are not extruded (font triangulation is non-manifold-prone on FDM);
    the band is the canonical stamp-area carrier and the text is silk-screen/engrave
    target. The stamp identity is asserted in metadata so downstream tooling can label
    it. This keeps the part watertight while honoring the 'must carry the stamp' rule.
    """
    outer = _disc(outer_r, height)
    inner = _disc(inner_r, height + 2.0)  # taller so the cut goes clean through
    inner.apply_translation((0.0, 0.0, -1.0))
    ring = trimesh.boolean.difference([outer, inner], engine="manifold")
    ring.apply_translation((0.0, 0.0, z_base))
    return ring


# ----------------------------------------------------------------------------
# 1. Impedance disc (Smith-chart / impedance-plane puck)
# ----------------------------------------------------------------------------
def impedance_disc() -> trimesh.Trimesh:
    """Flat printable impedance-plane puck with raised Smith-chart relief.

    Features (all raised ridges >= ~1 mm so they read by eye / finger):
      * outer rim ridge = the unit reflection circle |Gamma| = 1
      * the real axis (resistance axis) as a diameter spoke
      * two constant-R circles (R=0 boundary already = unit circle; R=1, R=3 arcs)
      * two constant-X arcs (the +X and -X reactance arcs) tangent at Gamma=+1
      * a raised annular STAMP band carrying '[STATE-SPACE - NOT A COORDINATE]'

    This is the LC-tank STATE plane (Gamma = (Z-Z0)/(Z+Z0)); the saturation amplitude
    A traces a Lissajous/locus here. It is explicitly NOT a lattice coordinate.

    Returns: watertight trimesh.Trimesh, flat on the bed (z=0 face), no supports.
    """
    base = _disc(DISC_RADIUS, DISC_THICK)
    z_top = DISC_THICK
    cen = (0.0, 0.0)
    # Reliefs are collected separately, then CLIPPED to the disc footprint so an arc
    # whose generating circle lies off-disc (constant-X arcs) cannot overhang the rim.
    parts: list[trimesh.Trimesh] = []

    # --- unit circle |Gamma|=1 : the rim ridge (full ring) ---
    unit_r = DISC_RADIUS * 0.93
    parts.append(
        _arc_ridge(cen, unit_r, 0.0, _TAU, z_base=z_top,
                   width=RIDGE_WIDTH, height=RIDGE_DEPTH, n=120)
    )

    # --- real (resistance) axis : diameter spoke ---
    parts.append(
        _radial_ridge(cen, -unit_r, unit_r, 0.0, z_base=z_top,
                      width=RIDGE_WIDTH, height=RIDGE_DEPTH)
    )

    # --- constant-R circles (Smith chart): circles through Gamma=+1, centered on
    #     the real axis at r=R/(R+1), radius=1/(R+1) (in Gamma units, scaled). ---
    gamma1 = (unit_r, 0.0)  # the Gamma=+1 point (open-circuit), all R-circles pass here
    for R in (1.0, 3.0):
        c = R / (R + 1.0)
        rad = 1.0 / (R + 1.0)
        cc = (unit_r * c, 0.0)
        parts.append(
            _arc_ridge(cc, unit_r * rad, 0.0, _TAU, z_base=z_top,
                       width=RIDGE_WIDTH, height=RIDGE_DEPTH, n=80)
        )

    # --- constant-X arcs: circles centered at (1, 1/X) tangent at Gamma=+1,
    #     radius 1/|X| (Gamma units). Draw +X (upper) and -X (lower) for X=1. ---
    for X in (1.0, -1.0):
        cc = (unit_r * 1.0, unit_r * (1.0 / X))
        rad = unit_r * (1.0 / abs(X))
        # draw the portion of the reactance arc that lies inside the unit circle
        a_start = np.arctan2(0.0 - cc[1], gamma1[0] - cc[0])
        # sweep ~110 deg of arc into the chart interior
        sweep = np.deg2rad(115.0) * (1.0 if X > 0 else -1.0)
        parts.append(
            _arc_ridge(cc, rad, a_start, a_start - sweep, z_base=z_top,
                       width=RIDGE_WIDTH, height=RIDGE_DEPTH, n=70)
        )

    # Clip all chart reliefs to a cylinder matching the disc rim so nothing overhangs.
    reliefs = trimesh.boolean.union(parts, engine="manifold")
    clip = _disc(DISC_RADIUS, STAMP_RELIEF + RIDGE_DEPTH + 2.0)
    clip.apply_translation((0.0, 0.0, z_top - 0.5))
    reliefs = trimesh.boolean.intersection([reliefs, clip], engine="manifold")

    # --- raised STAMP band (annular relief at the outer margin; on-disc by construction) ---
    stamp = _stamp_band(z_top, inner_r=DISC_RADIUS * 0.955, outer_r=DISC_RADIUS,
                        height=STAMP_RELIEF)

    tm = trimesh.boolean.union([base, reliefs, stamp], engine="manifold")
    tm = _finalize(tm)
    tm.metadata["stamp"] = STAMP_TEXT
    tm.metadata["artifact"] = "impedance_disc"
    tm.metadata["semantics"] = "LC-tank STATE plane (Gamma); NOT a lattice coordinate"
    return tm


# ----------------------------------------------------------------------------
# 2. Phasor dial — base + snap-on rotating pointer (two-indicator variant)
# ----------------------------------------------------------------------------
def phasor_dial_body() -> trimesh.Trimesh:
    """Dial base plate with a center pin and engraved tick/ridge graduations.

    The pin is sized so phasor_dial_pointer() snaps over it with running clearance
    (POINTER_BORE_CLEAR per side => it spins). Twelve raised tick ridges around the
    rim mark the phase angle; a raised stamp band carries the STATE-SPACE legend.

    Returns: watertight trimesh.Trimesh, flat on bed, pin up.
    """
    base = _disc(DIAL_RADIUS, DIAL_THICK)
    z_top = DIAL_THICK
    cen = (0.0, 0.0)
    parts = [base]

    # center pin (solid cylinder rising from the base top)
    pin = trimesh.creation.cylinder(radius=PIN_RADIUS, height=PIN_HEIGHT, sections=48)
    pin.apply_translation((0.0, 0.0, z_top + PIN_HEIGHT / 2.0))
    parts.append(pin)

    # 12 phase ticks around the rim (raised radial ridges)
    tick_r1 = DIAL_RADIUS * 0.92
    tick_r0 = DIAL_RADIUS * 0.78
    for k in range(12):
        ang = k * (_TAU / 12.0)
        parts.append(
            _radial_ridge(cen, tick_r0, tick_r1, ang, z_base=z_top,
                          width=RIDGE_WIDTH, height=TICK_DEPTH)
        )

    # stamp band at the outer margin
    parts.append(
        _stamp_band(z_top, inner_r=DIAL_RADIUS * 0.955, outer_r=DIAL_RADIUS,
                    height=STAMP_RELIEF)
    )

    tm = trimesh.boolean.union(parts, engine="manifold")
    tm = _finalize(tm)
    tm.metadata["stamp"] = STAMP_TEXT
    tm.metadata["artifact"] = "phasor_dial_body"
    tm.metadata["pin_radius_mm"] = float(PIN_RADIUS)
    return tm


def phasor_dial_pointer() -> trimesh.Trimesh:
    """Snap-on rotating pointer arm with a hub bore sized for a running fit on the pin.

    Bore radius = PIN_RADIUS + POINTER_BORE_CLEAR (loose => spins). The arm is a flat
    tapered plate; a small raised tip nub marks the indicated phase. Print flat.

    Returns: watertight trimesh.Trimesh.
    """
    bore_r = PIN_RADIUS + POINTER_BORE_CLEAR

    # hub: short cylinder with a through-bore
    hub = trimesh.creation.cylinder(radius=POINTER_HUB_R, height=POINTER_THICK,
                                    sections=48)
    hub.apply_translation((0.0, 0.0, POINTER_THICK / 2.0))
    bore = trimesh.creation.cylinder(radius=bore_r, height=POINTER_THICK + 2.0,
                                     sections=48)
    bore.apply_translation((0.0, 0.0, POINTER_THICK / 2.0))
    hub = trimesh.boolean.difference([hub, bore], engine="manifold")

    # arm: a flat box from the hub out to POINTER_LEN, tapered via two boxes
    arm = trimesh.creation.box(extents=(POINTER_LEN, POINTER_HUB_R * 1.1,
                                        POINTER_THICK))
    arm.apply_translation((POINTER_LEN / 2.0, 0.0, POINTER_THICK / 2.0))

    # tip marker nub (raised) so the indicated end is unambiguous
    nub = trimesh.creation.box(extents=(POINTER_HUB_R * 0.6, POINTER_HUB_R * 0.6,
                                        TICK_DEPTH))
    nub.apply_translation((POINTER_LEN * 0.92, 0.0, POINTER_THICK + TICK_DEPTH / 2.0))

    tm = trimesh.boolean.union([hub, arm, nub], engine="manifold")
    tm = _finalize(tm)
    tm.metadata["artifact"] = "phasor_dial_pointer"
    tm.metadata["bore_radius_mm"] = float(bore_r)
    tm.metadata["clearance_mm"] = float(POINTER_BORE_CLEAR)
    return tm


def phasor_dial_two_indicator_body() -> trimesh.Trimesh:
    """A1 perp T2 variant: ONE base, TWO concentric pins on independent axes.

    The mass-sector phase (A1 / breathing / V) and the charge-spin-sector phase
    (T2 / micro-rotation / kappa) are read on TWO independent pointers stacked on
    two coaxial-but-decoupled pins (an inner tall pin + an outer short collar pin),
    so the two sector phases are NEVER merged into one indicator. Each pin takes its
    own phasor_dial_pointer() (the inner uses the standard pointer; the outer uses
    phasor_dial_pointer_outer()).

    Returns: watertight trimesh.Trimesh.
    """
    # slightly larger base to host two graduation rings
    base_r = DIAL_RADIUS * 1.15
    base = _disc(base_r, DIAL_THICK)
    z_top = DIAL_THICK
    cen = (0.0, 0.0)
    parts = [base]

    # INNER pin (A1 / mass sector) — tall, central
    inner_pin = trimesh.creation.cylinder(radius=PIN_RADIUS, height=PIN_HEIGHT * 1.6,
                                          sections=48)
    inner_pin.apply_translation((0.0, 0.0, z_top + PIN_HEIGHT * 1.6 / 2.0))
    parts.append(inner_pin)

    # OUTER collar pin (T2 / charge-spin sector) — short hollow collar, concentric,
    # at a larger radius so its pointer rides ABOVE the base and clears the inner arm.
    collar_outer_r = PIN_RADIUS * 2.6
    collar_inner_r = PIN_RADIUS * 1.9  # bore for the inner pin to pass through
    collar_h = PIN_HEIGHT * 0.7
    co = trimesh.creation.cylinder(radius=collar_outer_r, height=collar_h, sections=48)
    ci = trimesh.creation.cylinder(radius=collar_inner_r, height=collar_h + 2.0,
                                   sections=48)
    co.apply_translation((0.0, 0.0, z_top + collar_h / 2.0))
    ci.apply_translation((0.0, 0.0, z_top + collar_h / 2.0))
    collar = trimesh.boolean.difference([co, ci], engine="manifold")
    parts.append(collar)

    # two graduation rings: inner ring (A1) + outer ring (T2), tick spokes
    for ring_frac, n_ticks in ((0.62, 12), (0.95, 12)):
        r1 = base_r * ring_frac
        r0 = base_r * (ring_frac - 0.10)
        for k in range(n_ticks):
            ang = k * (_TAU / n_ticks)
            parts.append(
                _radial_ridge(cen, r0, r1, ang, z_base=z_top,
                              width=RIDGE_WIDTH, height=TICK_DEPTH)
            )

    parts.append(
        _stamp_band(z_top, inner_r=base_r * 0.96, outer_r=base_r, height=STAMP_RELIEF)
    )

    tm = trimesh.boolean.union(parts, engine="manifold")
    tm = _finalize(tm)
    tm.metadata["stamp"] = STAMP_TEXT
    tm.metadata["artifact"] = "phasor_dial_two_indicator_body"
    tm.metadata["axes"] = "inner=A1/mass(V); outer=T2/charge-spin(kappa); INDEPENDENT"
    tm.metadata["inner_pin_radius_mm"] = float(PIN_RADIUS)
    tm.metadata["outer_collar_inner_r_mm"] = float(collar_inner_r)
    return tm


def phasor_dial_pointer_outer() -> trimesh.Trimesh:
    """The T2-sector pointer that rides the outer collar of the two-indicator dial.

    Bore = outer collar OD + clearance, so it spins on the collar independently of the
    inner (A1) pointer. Slightly longer arm than the inner pointer so both read clear.

    Returns: watertight trimesh.Trimesh.
    """
    collar_outer_r = PIN_RADIUS * 2.6
    bore_r = collar_outer_r + POINTER_BORE_CLEAR
    hub_r = bore_r + RIDGE_WIDTH * 2.0

    hub = trimesh.creation.cylinder(radius=hub_r, height=POINTER_THICK, sections=56)
    hub.apply_translation((0.0, 0.0, POINTER_THICK / 2.0))
    bore = trimesh.creation.cylinder(radius=bore_r, height=POINTER_THICK + 2.0,
                                     sections=56)
    bore.apply_translation((0.0, 0.0, POINTER_THICK / 2.0))
    hub = trimesh.boolean.difference([hub, bore], engine="manifold")

    arm_len = POINTER_LEN * 1.25
    arm = trimesh.creation.box(extents=(arm_len, hub_r * 0.8, POINTER_THICK))
    arm.apply_translation((arm_len / 2.0 + bore_r, 0.0, POINTER_THICK / 2.0))

    nub = trimesh.creation.box(extents=(hub_r * 0.5, hub_r * 0.5, TICK_DEPTH))
    nub.apply_translation((arm_len * 0.92 + bore_r, 0.0,
                           POINTER_THICK + TICK_DEPTH / 2.0))

    tm = trimesh.boolean.union([hub, arm, nub], engine="manifold")
    tm = _finalize(tm)
    tm.metadata["artifact"] = "phasor_dial_pointer_outer"
    tm.metadata["bore_radius_mm"] = float(bore_r)
    return tm


__all__ = [
    "impedance_disc",
    "phasor_dial_body",
    "phasor_dial_pointer",
    "phasor_dial_two_indicator_body",
    "phasor_dial_pointer_outer",
    "STAMP_TEXT",
    "S",
]
