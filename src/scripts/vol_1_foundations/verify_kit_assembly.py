#!/usr/bin/env python3
"""
As-BUILT assembly check for the vacuum-lattice kit (complements kit_dfm_check.py).

kit_dfm_check.py checks the SPEC dimensions against the FDM floor. This checks the
actual BUILT trimesh geometry: it seats a bond into a node socket at the lattice
position and boolean-intersects them to confirm a real press-fit (an interference
shell, not a gap and not a gross clash), confirms the length chain closes to the
lattice pitch, and re-confirms the parts are watertight.

This closes the gap the 2026-06-21 review exposed — "the linter says 0.10 mm" was
checking the contract constants, not whether the as-built tip actually seats in the
as-built bore. Run after any geometry change to the kit core.

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/verify_kit_assembly.py
Exit code 1 on any failure (regression gate); exits 0 (skip) if trimesh/manifold3d
are unavailable.
"""

from __future__ import annotations

import os
import sys

os.environ.setdefault("PRINT_MM_PER_L_NODE",
                      os.environ.get("KIT_PRINT_MM_PER_L_NODE", "100"))

import numpy as np

try:
    import trimesh  # noqa: F401
    import manifold3d  # noqa: F401
except ImportError as exc:  # pragma: no cover
    print(f"verify_kit_assembly: skipped — requires trimesh + manifold3d ({exc})")
    sys.exit(0)

import trimesh
import kit_core_diamond as core

SQRT3 = np.sqrt(3.0)
fails: list[str] = []


def check(name: str, ok: bool, detail: str) -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {name:36} {detail}")
    if not ok:
        fails.append(name)


def main() -> None:
    kd = core.key_dims()
    S = kd["S_mm_per_node"]
    pitch = SQRT3 * S
    print("=" * 84)
    print(f"  Vacuum-lattice kit — as-built ASSEMBLY check @ {S:.1f} mm/l_node")
    print("=" * 84)

    node = core.node_body("A")
    bond = core.bond(helix=False)

    # as-built bond tip radius (vertices near one end)
    z = bond.vertices[:, 2]
    tip = bond.vertices[np.abs(z - z.min()) < 0.6]
    tip_r = float(np.max(np.hypot(tip[:, 0], tip[:, 1])))
    bore_r = kd["R_JOINT_socket_mm"]
    diam_interf = 2.0 * (tip_r - bore_r)
    check("press-fit interference present", 0.06 <= diam_interf <= 0.30,
          f"{diam_interf:.3f} mm diametral (tip R {tip_r:.3f} > bore R {bore_r:.3f})")

    # length chain: two seated tips + bond span == lattice pitch
    seat = kd["node_corner_dist_mm"] - kd["insert_depth_mm"]
    node_node = 2.0 * seat + kd["bond_total_len_mm"]
    check("length chain closes to pitch", abs(node_node - pitch) < 0.05,
          f"{node_node:.3f} vs sqrt(3)*S {pitch:.3f} mm")
    check("insertion fits inside bore depth", kd["insert_depth_mm"] <= kd["socket_depth_mm"],
          f"insert {kd['insert_depth_mm']:.1f} <= bore depth {kd['socket_depth_mm']:.1f} mm")

    # As-built press-fit with ROUND joinery (clocking-free). Seat a bond between this node
    # and its neighbour; measure the interference shell at BOTH ends across several bond
    # spins. Round tip-in-round-bore is rotation-symmetric, so a rigid bond seats clean in
    # both independently-oriented sockets — unlike the original HEX joinery, where a rigid
    # bond could not face-flush both ends at once (two-end clocking constraint; the old
    # align-vectors check measured a 6.19 mm^3 corner gouge on one end — RETRACTED).
    from vacuum_lc_geometry import DIAMOND_PORT_HATS  # noqa: E402
    hat = DIAMOND_PORT_HATS[0]
    nbr = core.node_body("B"); nbr.apply_translation(hat * pitch)
    vols_A, vols_B = [], []
    for spin in (0.0, 30.0, 47.0):
        bs = bond.copy()
        bs.apply_transform(trimesh.transformations.rotation_matrix(np.radians(spin), [0, 0, 1.0]))
        bs.apply_transform(core._rotmat_z_to(hat))
        bs.apply_translation(hat * pitch / 2.0)
        iA = trimesh.boolean.intersection([node, bs], engine="manifold")
        iB = trimesh.boolean.intersection([nbr, bs], engine="manifold")
        vols_A.append(float(iA.volume) if iA is not None and len(iA.faces) else 0.0)
        vols_B.append(float(iB.volume) if iB is not None and len(iB.faces) else 0.0)
    check("both ends press-fit (interference shell > 0, no gap/clash)",
          min(vols_A) > 0.2 and min(vols_B) > 0.2 and max(vols_A + vols_B) < 0.5 * (3.0 * SQRT3 / 2.0) * tip_r**2 * kd["insert_depth_mm"],
          f"A-end {vols_A[0]:.2f} mm^3, B-end {vols_B[0]:.2f} mm^3 (round shells)")
    check("clocking-free (interference rotation-invariant across bond spin)",
          (max(vols_A) - min(vols_A) < 0.05) and (max(vols_B) - min(vols_B) < 0.05),
          f"A spin-spread {max(vols_A) - min(vols_A):.3f}, B {max(vols_B) - min(vols_B):.3f} mm^3 (round tips => no clock dependence)")

    # headline watertight re-confirm
    for nm, m in (("node_A", node), ("node_B", core.node_body("B")), ("bond", bond)):
        check(f"{nm} watertight + is_volume", bool(m.is_watertight and m.is_volume),
              f"watertight={m.is_watertight} is_volume={m.is_volume}")

    print()
    if fails:
        print(f"  FAIL — {len(fails)} check(s) failed: {fails}")
        sys.exit(1)
    print("  OK — kit assembles: bond press-fits the node socket, lengths close to the "
          "lattice pitch, parts watertight.")


if __name__ == "__main__":
    main()
