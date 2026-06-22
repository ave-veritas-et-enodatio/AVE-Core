#!/usr/bin/env python3
"""
Design-for-FDM (DFM) rule check for the vacuum-lattice kit — Prusa i3 MK3+.

Pulls the REAL kit geometry constants at the chosen print scale and checks every
printed feature against the MK3+ design-for-additive floor. PASS / WARN / FAIL.

This is a design-rule-check (DRC) linter, not a mesh generator. Run it at any
scale to see whether the parts are actually printable + mate-able before slicing.

Usage:
    KIT_PRINT_MM_PER_L_NODE=100 PYTHONPATH=src \\
        ./.venv/bin/python src/scripts/vol_1_foundations/kit_dfm_check.py

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

    # ---- Press / friction fit ----
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
    # Ports along body diagonals (1,1,1)-type. In a cube-face-down pose the port
    # axis makes 54.7 deg with vertical; TWO of the four ports have -z component
    # (point downward) -> unprintable without support.
    port_from_vertical = math.degrees(math.acos(1.0 / math.sqrt(3.0)))
    row("node A port axis vs vertical", port_from_vertical, "deg",
        f"<= {MAX_OVERHANG_DEG} unsupported", "warn",
        "2 of 4 ports point DOWNWARD in flat pose -> need vertex-up pose or support")

    print("-" * 96)
    print("  Summary: scan the FAIL/WARN rows. The kit's job is for ALL rows to read PASS")
    print("  at the shipped default scale, with print poses that avoid the overhang WARNs.")
    print("=" * 96)


if __name__ == "__main__":
    main()
