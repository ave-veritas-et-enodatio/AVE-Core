"""theta route-1 — srs carrier geometry + the corpus scale ladder (READ-ONLY).

Class: CHARACTERIZATION driver for the research doc pair
  research/2026-08-23_theta-route1-embedding-obstruction_{prereg,result}.md

It computes, from the CERTIFIED constructor and the CANONICAL constants module
(no hard-coded lengths, no CODATA re-entry):

  (A) the ratified z=3 srs carrier's local port geometry — degree, bond-angle
      set, coplanarity of the three bonds at a node, and the net's girth
      (shortest closed cycle) — the three facts the "one-per-port" and
      "extended-lattice-cycle" formalizations both rest on;
  (B) the SCALE LADDER: every corpus-stated real-space length of the electron
      and proton bodies expressed in units of the srs nearest-neighbour bond
      length, which the constructor pins to L_NODE.

NOTHING here is a physics claim. Every number is either read from
`ave.core.constants` or measured on `ave.core.chiral_lattice.build_srs_net`.
The corpus statements the ladder is compared against are quoted (with
file:line) in the result doc, never restated here as fact.

Run:  PYTHONPATH=<worktree>/src python research/drivers/theta_route1_srs_scale_ladder.py
"""

from __future__ import annotations

import itertools
import json
from collections import deque

import numpy as np

from ave.core.chiral_lattice import build_srs_net
from ave.core.constants import D_PROTON, L_NODE, PROTON_ELECTRON_RATIO


def bond_geometry(net) -> dict:
    """Degree census + the pairwise bond-angle set + coplanarity residual."""
    degrees = sorted({len(nb) for nb in net.neighbors})
    angles: list[float] = []
    sum_residual: list[float] = []
    for u in range(len(net.neighbors)):
        dirs = np.array(net.bond_unit[u], dtype=float)
        # coplanarity of the z=3 star: three unit vectors summing to 0 are
        # necessarily coplanar; report the residual |sum| as the measurement.
        sum_residual.append(float(np.linalg.norm(dirs.sum(axis=0))))
        for a, b in itertools.combinations(range(len(dirs)), 2):
            c = float(np.clip(np.dot(dirs[a], dirs[b]), -1.0, 1.0))
            angles.append(float(np.degrees(np.arccos(c))))
    angles_arr = np.array(angles)
    return {
        "degrees_present": degrees,
        "n_nodes": len(net.neighbors),
        "bond_angle_deg_min": float(angles_arr.min()),
        "bond_angle_deg_max": float(angles_arr.max()),
        "bond_star_sum_norm_max": float(max(sum_residual)),
    }


def girth(net, probes: int = 24) -> int:
    """Shortest cycle length, by BFS from a sample of roots (unweighted graph)."""
    nbrs = net.neighbors
    n = len(nbrs)
    best = 10**9
    rng = np.random.default_rng(0)
    roots = rng.choice(n, size=min(probes, n), replace=False)
    for root in roots:
        dist = {int(root): 0}
        parent = {int(root): -1}
        q = deque([int(root)])
        while q:
            u = q.popleft()
            for v in nbrs[u]:
                v = int(v)
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif v != parent[u]:
                    best = min(best, dist[u] + dist[v] + 1)
    return int(best)


def scale_ladder() -> dict:
    """Corpus-stated body lengths in units of the srs bond length (= L_NODE).

    Each entry's PROVENANCE is the corpus quote cited in the result doc; here we
    only evaluate the arithmetic the quote specifies, from canonical constants.
    """
    # AVE-derived ratio (NOT CODATA M_PROTON): constants.py:987 _X_CORE + 1.0
    lam_p = L_NODE / PROTON_ELECTRON_RATIO  # proton reduced Compton wavelength
    d_p = D_PROTON * 1e-15  # canonical constants.py:1147, D_p = 4*lambda_p [fm -> m]
    e_circ_13 = L_NODE  # electron-unknot.md:13 reading: C_loop = l_node
    e_circ_59 = 2.0 * np.pi * L_NODE  # :59 reading: ropelength 2pi with d = l_node
    return {
        "L_NODE_m": float(L_NODE),
        "L_NODE_fm": float(L_NODE * 1e15),
        "m_p_over_m_e_AVE_derived": float(PROTON_ELECTRON_RATIO),
        "lambda_p_fm": float(lam_p * 1e15),
        "D_p_fm": float(d_p * 1e15),
        "D_p_over_L_NODE": float(d_p / L_NODE),
        "L_NODE_over_D_p": float(L_NODE / d_p),
        "electron_C_loop_over_L_NODE_reading13": float(e_circ_13 / L_NODE),
        "electron_C_loop_over_L_NODE_reading59": float(e_circ_59 / L_NODE),
        "electron_loop_diameter_over_L_NODE_reading13": float(
            (e_circ_13 / np.pi) / L_NODE
        ),
        "electron_tube_diameter_over_L_NODE_reading13": float(
            (2.0 * L_NODE / (2.0 * np.pi)) / L_NODE
        ),
    }


def main() -> None:
    out: dict = {}
    for hand in ("right", "left"):
        net = build_srs_net(L=4, enantiomorph=hand)
        g = bond_geometry(net)
        g["girth"] = girth(net)
        # a_cell default is 2*sqrt(2) (dimensionless) so NN bond == 1 pitch unit.
        # Minimum-image is required: raw pos-differences wrap under PBC.
        box = 4.0 * net.a_cell
        d = net.pos[[nb[0] for nb in net.neighbors]] - net.pos
        d -= box * np.round(d / box)
        g["nn_bond_in_pitch_units"] = float(np.linalg.norm(d, axis=1).max())
        out[f"srs_{hand}"] = g

    ladder = scale_ladder()
    out["scale_ladder"] = ladder

    girth_val = out["srs_right"]["girth"]
    out["derived_ratios"] = {
        "min_lattice_cycle_perimeter_in_L_NODE": float(girth_val),
        "min_lattice_cycle_over_electron_loop_reading13": float(girth_val),
        "min_lattice_cycle_over_proton_D_p": float(
            girth_val / ladder["D_p_over_L_NODE"]
        ),
        "port_pairs_available_per_z3_node": 3 // 2,
    }

    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
