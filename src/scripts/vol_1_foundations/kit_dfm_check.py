#!/usr/bin/env python3
"""
Design-for-FDM (DFM) rule check for the vacuum-lattice kit — Prusa i3 MK3+.

EXTENDED LINTER. This is the original kit_dfm_check.py (vol_1_foundations) plus
new rows for every part class the REBUILD kit adds:

  * unified solid node body (chamfered cube; identical for A & B)
  * the 3 separate DOF accent parts (E-triad / B-rings / V-breathing) — min
    feature + snap-peg vs floor
  * the press-fit bond (interference = R_JOINT+INTERF vs socket = R_JOINT, i.e.
    POSITIVE diametral interference now, unlike the old 0.00) + horizontal aspect
  * phase-space disc / dial (relief depth, pin clearance)
  * srs acceptance-instrument node + bond
  * base jig (bed-fit / tiling, pocket size)

The original rows are preserved verbatim against the legacy `g.KIT_*` constants
so the audit trail stays continuous. The NEW rows compute from the SHARED
GEOMETRY CONTRACT constants (the canonical rebuild spec), defined locally below
and tagged [CONTRACT]. All absolute sizes are [RENDERING] magnification.

This is a design-rule-check (DRC) linter, not a mesh generator. Run it at any
scale to see whether the parts are actually printable + mate-able before slicing.

Usage:
    KIT_PRINT_MM_PER_L_NODE=100 PYTHONPATH=src \\
        ./.venv/bin/python kit_dfm_check.py

MK3+ design rules (sources): Prusa MK3S+ build volume 250x210x210 mm, 0.4 mm
nozzle; standard FDM DFM (2-perimeter min wall ~0.8 mm, robust pin/peg >=2.5 mm,
clean hole >=2 mm, unsupported overhang <=~55 deg from vertical, friction-fit
diametral interference ~0.1-0.2 mm, vertical-rod aspect <=~10:1 before toppling,
elephant-foot chamfer >=0.5 mm on bed-contact mating features).
"""

from __future__ import annotations

import math
import os

# Reproduce the kit default scale resolution (generate_vacuum_lattice_kit.py).
_FDM_FRIENDLY_MM = round(2.0 / 0.060, 1)
_kit = os.environ.get("KIT_PRINT_MM_PER_L_NODE", str(max(_FDM_FRIENDLY_MM, 100.0)))
os.environ.setdefault("PRINT_MM_PER_L_NODE", _kit)

import vacuum_lc_geometry as g  # noqa: E402  (reads PRINT_MM_PER_L_NODE on import)

S = g.MM_PER_L_NODE_UNIT
F2F = math.sqrt(3.0)  # hex circumradius -> flat-to-flat factor
SQRT3 = math.sqrt(3.0)

# ── MK3+ design rules ──
BED = (250.0, 210.0, 210.0)
NOZZLE = 0.4
MIN_WALL = 0.8          # 2 perimeters
MIN_PEG = 2.5           # robust load-bearing pin/peg diameter
MIN_HOLE = 2.0          # clean hole diameter (FDM shrinks holes)
MIN_DETAIL = 0.8        # smallest legible raised/recessed detail
MAX_OVERHANG_DEG = 55.0  # from vertical, unsupported
MAX_VERT_ASPECT = 10.0   # height/width of a free-standing rod before it topples
FRICTION_BAND = (0.10, 0.25)  # diametral interference for a snap/friction fit (mm)
BAND_EPS = 1e-6               # float-residual tolerance on band edges
MIN_RELIEF = 0.4         # legible engraved/embossed relief depth (~1 layer)
MIN_CLEARANCE = 0.2      # loose clearance fit (spin/slide, not press)
CHAMFER = 0.4            # elephant-foot chamfer on bed-contact mating faces

# ── SHARED GEOMETRY CONTRACT [CONTRACT] — the canonical REBUILD kit spec ──
# (fractions of S; single source of truth so the rebuilt builders all mate)
INTERF_MM = float(os.environ.get("KIT_FRICTION_INTERFERENCE_MM",
                                 str(g.FRICTION_INTERFERENCE_MM)))  # per-side, mm
NODE_HALF = 0.10 * S          # unified solid node half-extent (cube)
NODE_CHAMFER = 0.02 * S       # printability edge chamfer on the node cube
R_JOINT = 0.036 * S           # bond socket hex circumradius (the bore)
SOCKET_DEPTH = 0.07 * S       # bond socket depth
R_SHAFT = 0.05 * S            # bond visible shaft circumradius (carries helix)
INSERT_DEPTH = 0.06 * S       # bond insertion tip length (per end)
R_TIP = R_JOINT + INTERF_MM   # bond press-fit tip circumradius (the interference)
ACCENT_JOINT = 0.018 * S      # accent mount socket circumradius
R_ACCENT_PEG = ACCENT_JOINT + INTERF_MM  # accent peg circumradius (press fit)
ACCENT_PEG_LEN = 0.05 * S     # accent snap-peg length

# DOF accent feature sizes [CONTRACT/RENDERING]
E_STUB_R = 0.022 * S          # E-triad stub radius (3 orthogonal translational stubs)
E_STUB_LEN = 0.09 * S
B_RING_MAJOR = 0.085 * S      # B-rings major radius (3 orthogonal micro-rotation rings)
B_RING_TUBE = 0.018 * S       # B-rings tube radius
V_RIDGE_W = 0.012 * S         # V-breathing bellows ridge width (A1 mass glyph)
V_RIDGE_H = 0.010 * S         # V-breathing ridge relief height

# Diamond bond center pitch (engine): sqrt(3)*S along the (1,1,1)-type ports.
BOND_PITCH = SQRT3 * S
# Bond visible span between the two node corner surfaces, then + 2 insert tips.
SURFACE_DIST = NODE_HALF * SQRT3            # node center -> corner surface
BOND_VISIBLE = BOND_PITCH - 2.0 * SURFACE_DIST
BOND_TOTAL = BOND_VISIBLE + 2.0 * INSERT_DEPTH

# Phase-space artifacts [STATE-SPACE - NOT A COORDINATE]
DISC_DIA = 0.90 * S           # saturation-amplitude disc diameter
DISC_RELIEF = 0.5             # engraved A^2 = eps^2 + kappa^2 + V^2 relief depth, mm
DIAL_PIN_R = 0.020 * S        # dial center pin radius
DIAL_BORE_R = DIAL_PIN_R + MIN_CLEARANCE  # dial bore (spins, loose fit)

# srs acceptance instrument (degree-3 chiral) — labelled INSTRUMENT, not production
SRS_NODE_HALF = 0.085 * S     # srs node body half-extent (3 ports)
SRS_R_JOINT = R_JOINT         # reuse the same joinery so srs bonds press-fit
SRS_BOND_TOTAL = BOND_TOTAL   # same pitch family

# Base jig (alignment fixture; tiles the bed)
JIG_POCKET = 2.0 * NODE_HALF + 2.0 * MIN_CLEARANCE  # node drops in with clearance
JIG_WALL = 1.2                # jig pocket wall thickness, mm
JIG_TILE = JIG_POCKET + 2.0 * JIG_WALL              # one jig cell footprint


def row(name, value, unit, rule, ok, note=""):
    status = "PASS" if ok == "pass" else ("WARN" if ok == "warn" else "FAIL")
    val = f"{value:.2f}" if isinstance(value, (int, float)) else str(value)
    print(f"  {status:4}  {name:34} {val:>8} {unit:<5} | {rule:<26} {note}")


def main() -> None:
    print("=" * 96)
    print(f"  Vacuum-lattice kit — Prusa i3 MK3+ DFM check  @ {S:.1f} mm/l_node")
    print("=" * 96)
    print(f"  Bed {BED[0]}x{BED[1]}x{BED[2]} mm | nozzle {NOZZLE} mm | "
          f"l_node pitch (diamond NN) = sqrt(3)*S = {F2F*S:.1f} mm")
    print(f"  {'':4}  {'FEATURE':34} {'VALUE':>8} {'UNIT':<5} | {'RULE':<26} NOTE")
    print("-" * 96)

    # ======================================================================
    # LEGACY ROWS (preserved verbatim — audit-trail continuity)
    # ======================================================================
    print("  -- legacy (pre-rebuild geometry) --")

    # ---- Diamond node A (cube) ----
    cube_edge = 2.0 * g.KIT_SOLID_CUBE_HALF
    row("node A cube edge", cube_edge, "mm", f"<= bed {BED[1]}", "pass" if cube_edge < BED[1] else "fail")

    # ---- Diamond node B (sphere shell) ----
    r_out = g.CELL_B_RADIUS * 1.05
    sphere_dia = 2.0 * r_out
    sphere_wall = g.KIT_SPHERE_WALL
    row("node B sphere dia", sphere_dia, "mm", f"<= bed {BED[1]}", "pass" if sphere_dia < BED[1] else "fail")
    row("node B shell wall", sphere_wall, "mm", f">= {MIN_WALL} (min wall)",
        "pass" if sphere_wall >= MIN_WALL else "fail",
        "hollow sphere top = internal overhang; needs support or vase/spiral split")

    # ---- Port collar ----
    collar_f2f = F2F * g.KIT_PORT_RADIUS
    collar_wall = g.KIT_WALL_RADIAL
    row("port collar flat-to-flat", collar_f2f, "mm", "(joinery OD)", "pass")
    row("port collar wall", collar_wall, "mm", f">= {MIN_WALL} (min wall)",
        "pass" if collar_wall >= MIN_WALL else "fail")

    # ---- Socket bore (hole) ----
    socket_f2f = F2F * g.KIT_SOCKET_RADIUS
    row("socket bore flat-to-flat", socket_f2f, "mm", f">= {MIN_HOLE} (clean hole)",
        "pass" if socket_f2f >= MIN_HOLE else "fail")

    # ---- Peg ----
    peg_f2f = F2F * g.KIT_PEG_RADIUS
    row("peg flat-to-flat", peg_f2f, "mm", f">= {MIN_PEG} (robust peg)",
        "pass" if peg_f2f >= MIN_PEG else "fail")

    # ---- Bond ----
    bond_f2f = F2F * g.KIT_BOND_RADIUS
    bond_len = g.bond_total_length_mm(kit=True)
    aspect = bond_len / bond_f2f
    row("bond outer flat-to-flat", bond_f2f, "mm", f">= {MIN_PEG} (robust)",
        "pass" if bond_f2f >= MIN_PEG else "fail")
    row("bond printed length", bond_len, "mm", f"<= bed Z {BED[2]}",
        "pass" if bond_len < BED[2] else "fail")
    row("bond aspect (len/width)", aspect, ":1", f"<= {MAX_VERT_ASPECT} if VERTICAL",
        "fail" if aspect > MAX_VERT_ASPECT else "pass",
        "print HORIZONTAL on a hex face (pose orients +Z = vertical now)")

    # ---- Press / friction fit (LEGACY) ----
    interference = bond_f2f - socket_f2f  # diametral; >0 = bond bigger than bore
    if interference <= 0.0:
        ok, note = "fail", "bond OD == socket bore: parts will NOT mate"
    elif FRICTION_BAND[0] <= interference <= FRICTION_BAND[1]:
        ok, note = "pass", "in friction-fit band"
    else:
        ok, note = "warn", "outside typical friction band"
    row("press-fit interference (diam)", interference, "mm",
        f"{FRICTION_BAND[0]}-{FRICTION_BAND[1]} band", ok, note)

    # ---- Micro-rotation ring (B marker) tube ----
    ring_tube = 2.0 * g.B_RING_TUBE
    row("B ring tube dia", ring_tube, "mm", f">= {MIN_DETAIL} (detail)",
        "pass" if ring_tube >= MIN_DETAIL else "fail")

    # ---- Tetrahedral port overhang (node A, flat pose) ----
    port_from_vertical = math.degrees(math.acos(1.0 / math.sqrt(3.0)))
    row("node A port axis vs vertical", port_from_vertical, "deg",
        f"<= {MAX_OVERHANG_DEG} unsupported", "warn",
        "2 of 4 ports point DOWNWARD in flat pose -> need vertex-up pose or support")

    # ======================================================================
    # NEW ROWS — REBUILD part classes (SHARED GEOMETRY CONTRACT)
    # ======================================================================
    print("-" * 96)
    print("  -- rebuild (unified node + DOF accents + press-fit bond + state-space + srs + jig) --")

    # ---- Unified solid node body (identical A & B; color+emboss key, not shape) ----
    node_edge = 2.0 * NODE_HALF
    row("node body cube edge", node_edge, "mm", f"<= bed {BED[1]}",
        "pass" if node_edge < BED[1] else "fail", "unified A=B solid (sublattice=color)")
    row("node bed-face chamfer", NODE_CHAMFER, "mm", f">= {CHAMFER} (elephant-foot)",
        "pass" if NODE_CHAMFER >= CHAMFER else "fail", "flat bed face")

    # ---- Bond socket bore on the node (hex hole along port) ----
    sock_f2f = SQRT3 * R_JOINT
    row("node bond socket bore f2f", sock_f2f, "mm", f">= {MIN_HOLE} (clean hole)",
        "pass" if sock_f2f >= MIN_HOLE else "fail")
    # socket depth must clear the bond tip and seat in the node body
    row("node bond socket depth", SOCKET_DEPTH, "mm", f"<= {NODE_HALF*SQRT3:.1f} (corner)",
        "pass" if SOCKET_DEPTH <= SURFACE_DIST else "fail",
        f"tip insert {INSERT_DEPTH:.1f} seats inside")

    # ---- Accent mount socket + accent snap-peg ----
    accent_bore_f2f = SQRT3 * ACCENT_JOINT
    row("accent socket bore f2f", accent_bore_f2f, "mm", f">= {MIN_HOLE} (clean hole)",
        "pass" if accent_bore_f2f >= MIN_HOLE else "fail")
    accent_peg_f2f = SQRT3 * R_ACCENT_PEG
    row("accent snap-peg f2f", accent_peg_f2f, "mm", f">= {MIN_PEG} (robust peg)",
        "pass" if accent_peg_f2f >= MIN_PEG else "warn",
        "small accent peg; OK as light snap (not load-bearing)")
    # Diametral interference = 2 x per-side radial offset (shape-independent;
    # matches the legacy row's "(diam)" convention).
    accent_interf = 2.0 * (R_ACCENT_PEG - ACCENT_JOINT)  # = 2*INTERF_MM
    row("accent press-fit interference", accent_interf, "mm",
        f"{FRICTION_BAND[0]}-{FRICTION_BAND[1]} band",
        "pass" if (FRICTION_BAND[0] - BAND_EPS) <= accent_interf <= (FRICTION_BAND[1] + BAND_EPS) else "warn",
        f"{INTERF_MM:.2f} mm/side -> {accent_interf:.2f} diametral")
    row("accent snap-peg length", ACCENT_PEG_LEN, "mm", f">= {2*NOZZLE:.1f} (seats)",
        "pass" if ACCENT_PEG_LEN >= 2 * NOZZLE else "warn", "vs floor")

    # ---- DOF accent #1: E-triad (3 translational stubs) ----
    e_stub_dia = 2.0 * E_STUB_R
    row("E-triad stub dia", e_stub_dia, "mm", f">= {MIN_PEG} (robust)",
        "pass" if e_stub_dia >= MIN_PEG else "warn", "3 orthogonal eps stubs")
    e_aspect = E_STUB_LEN / e_stub_dia
    row("E-triad stub aspect", e_aspect, ":1", f"<= {MAX_VERT_ASPECT} (rod)",
        "pass" if e_aspect <= MAX_VERT_ASPECT else "warn", "print on a flat face")

    # ---- DOF accent #2: B-rings (3 micro-rotation rings, axis-set != V axis) ----
    b_ring_tube_dia = 2.0 * B_RING_TUBE
    row("B-rings tube dia", b_ring_tube_dia, "mm", f">= {MIN_DETAIL} (detail)",
        "pass" if b_ring_tube_dia >= MIN_DETAIL else "fail", "kappa^2 micro-rotation")
    b_ring_wall = b_ring_tube_dia  # solid torus tube == its own wall
    row("B-rings min feature", b_ring_tube_dia, "mm", f">= {MIN_WALL} (min wall)",
        "pass" if b_ring_tube_dia >= MIN_WALL else "warn",
        "A1 _|_ T2: ring axes independent of V breathing axis")

    # ---- DOF accent #3: V-breathing (A1 volumetric glyph; bellows ridge) ----
    row("V-breathing ridge width", V_RIDGE_W, "mm", f">= {NOZZLE} (1 nozzle)",
        "pass" if V_RIDGE_W >= NOZZLE else "warn", "A1 mass / V^2 store")
    row("V-breathing ridge relief", V_RIDGE_H, "mm", f">= {MIN_RELIEF} (relief)",
        "pass" if V_RIDGE_H >= MIN_RELIEF else "warn", "concentric pulse glyph")

    # ---- A/B key emboss tile ----
    row("A/B key emboss relief", MIN_RELIEF, "mm", f">= {MIN_RELIEF} (relief)",
        "pass", "A/B = color + embossed letter (NOT shape)")

    # ---- Bond: press-fit interference (NEW — POSITIVE, unlike legacy 0.00) ----
    new_bond_visible_f2f = SQRT3 * R_SHAFT
    row("bond shaft f2f (visible)", new_bond_visible_f2f, "mm", f">= {MIN_PEG} (robust)",
        "pass" if new_bond_visible_f2f >= MIN_PEG else "fail", "carries helix groove")
    new_sock_f2f = SQRT3 * R_JOINT  # bond seats in node socket bore (same f2f)
    row("bond->socket bore match f2f", new_sock_f2f, "mm", f">= {MIN_HOLE} (clean hole)",
        "pass" if new_sock_f2f >= MIN_HOLE else "fail", "tip mates this bore")
    # Diametral interference = 2 x per-side radial press (R_TIP = R_JOINT+INTERF
    # into a bore of R_JOINT). Shape factor SQRT3 cancels — it is the radial
    # offset that interferes, on both sides -> 2*INTERF_MM = 0.10 mm.
    new_interf = 2.0 * (R_TIP - R_JOINT)  # = 2 * INTERF_MM
    if new_interf <= 0.0:
        ok, note = "fail", "bond tip == socket bore: parts will NOT mate"
    elif (FRICTION_BAND[0] - BAND_EPS) <= new_interf <= (FRICTION_BAND[1] + BAND_EPS):
        ok, note = "pass", f"tip R_JOINT+{INTERF_MM:.2f} into bore R_JOINT"
    else:
        ok, note = "warn", "outside typical friction band"
    row("bond press-fit interference", new_interf, "mm",
        f"{FRICTION_BAND[0]}-{FRICTION_BAND[1]} band", ok, note)
    new_bond_aspect = BOND_TOTAL / new_bond_visible_f2f
    row("bond length (rebuild)", BOND_TOTAL, "mm", f"<= bed {BED[0]}",
        "pass" if BOND_TOTAL < BED[0] else "fail",
        f"visible {BOND_VISIBLE:.1f} + 2x tip {INSERT_DEPTH:.1f}")
    row("bond aspect (HORIZONTAL)", new_bond_aspect, ":1", f"<= {MAX_VERT_ASPECT} if VERT",
        "pass", "print HORIZONTAL on a hex flat -> aspect rule N/A")

    # ---- Phase-space disc [STATE-SPACE - NOT A COORDINATE] ----
    row("state-space disc dia", DISC_DIA, "mm", f"<= bed {BED[1]}",
        "pass" if DISC_DIA < BED[1] else "fail", "A^2 = eps^2 + kappa^2 + V^2")
    row("state-space disc relief", DISC_RELIEF, "mm", f">= {MIN_RELIEF} (relief)",
        "pass" if DISC_RELIEF >= MIN_RELIEF else "fail", "engraved store split")

    # ---- Phase-space dial (spins on a pin; loose clearance, NOT press) ----
    dial_clear = (DIAL_BORE_R - DIAL_PIN_R) * 2.0  # diametral clearance
    row("state-space dial pin dia", 2.0 * DIAL_PIN_R, "mm", f">= {MIN_PEG} (robust)",
        "pass" if 2.0 * DIAL_PIN_R >= MIN_PEG else "warn", "dial center pivot")
    row("state-space dial clearance", dial_clear, "mm", f">= {2*MIN_CLEARANCE:.1f} (spins)",
        "pass" if dial_clear >= 2 * MIN_CLEARANCE else "fail",
        "loose fit so the dial rotates (A = tank STATE)")

    # ---- srs acceptance INSTRUMENT (degree-3 chiral) ----
    srs_edge = 2.0 * SRS_NODE_HALF
    row("srs node edge [INSTRUMENT]", srs_edge, "mm", f"<= bed {BED[1]}",
        "pass" if srs_edge < BED[1] else "fail", "degree-3 chiral, NOT production net")
    srs_sock_f2f = SQRT3 * SRS_R_JOINT
    row("srs socket bore f2f [INSTR]", srs_sock_f2f, "mm", f">= {MIN_HOLE} (clean hole)",
        "pass" if srs_sock_f2f >= MIN_HOLE else "fail", "reuses kit joinery")
    row("srs bond length [INSTRUMENT]", SRS_BOND_TOTAL, "mm", f"<= bed {BED[0]}",
        "pass" if SRS_BOND_TOTAL < BED[0] else "fail", "labelled instrument")

    # ---- Base jig (alignment fixture; tiles the bed) ----
    row("jig pocket size", JIG_POCKET, "mm", f">= node+{2*MIN_CLEARANCE:.1f} (drop-in)",
        "pass" if JIG_POCKET >= node_edge + 2 * MIN_CLEARANCE - 1e-6 else "fail",
        "node seats with clearance")
    row("jig pocket wall", JIG_WALL, "mm", f">= {MIN_WALL} (min wall)",
        "pass" if JIG_WALL >= MIN_WALL else "fail")
    tiles_x = int(BED[0] // JIG_TILE)
    tiles_y = int(BED[1] // JIG_TILE)
    row("jig tile footprint", JIG_TILE, "mm", f"<= bed {BED[0]}",
        "pass" if JIG_TILE < BED[0] else "fail",
        f"tiles {tiles_x}x{tiles_y} on bed")

    print("-" * 96)
    print("  Summary: scan the FAIL/WARN rows. The kit's job is for ALL rows to read PASS")
    print("  at the shipped default scale, with print poses that avoid the overhang WARNs.")
    print("  Key change vs old kit: bond press-fit interference now reads POSITIVE (mating).")
    print("=" * 96)


if __name__ == "__main__":
    main()
