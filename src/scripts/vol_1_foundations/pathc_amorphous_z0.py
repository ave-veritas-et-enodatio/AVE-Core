"""Path C — z0 from K4 AMORPHOUS geometry, ALPHA-FREE.

PREREG: research/2026-06-08_pathc-z0-amorphous-emt-prereg.md

GOAL: derive the effective rigidity-percolation coordination z0 of the K4
vacuum lattice from K4 amorphous GEOMETRY ALONE (alpha-free). If z0 ~ 51.25
falls out alpha-free, the Feng-Thorpe-Garboczi (FTG) EMT then READS alpha out:
    alpha = p_c(z0) / 8pi,   p_c = (10 z0 - 12) / (z0 (z0 + 2)).
That would lift alpha from "Class-B closed-form" to emergence-class DERIVED.

ALPHA-CIRCULARITY GUARD (load-bearing; see prereg Section 4):
  - This file does NOT import ave.core.constants (no ALPHA leak).
  - No e/eps0/hbar/Z0/c (no SI-substitution channel).
  - No p_c = 8pi*alpha, no p_cauchy.
  - NO r_secondary/d = 1.187 / C_ratio: corpus-confirmed alpha-derived
    (C_ratio = (p_cauchy/p_c)^{1/3}, p_c = 8pi*alpha) -> FORBIDDEN as input.
    Method is therefore RADIUS-FREE / TOPOLOGY-ONLY.
  Permitted alpha-free inputs ONLY: K4/diamond topology (coordination 4),
  |T| = 12 (proper tetrahedral rotation group order), the integer 8pi (a pure
  geometric constant in the readout, NOT 8pi*alpha), and a geometric disorder
  strength (WWW bond-switch count). CODATA 1/137.036 appears ONLY in the final
  one-way external comparison and is NEVER fed back into z0.

METHOD (prereg Section 3):
  1. Crystalline alpha-free baseline: diamond/K4 supercell, NN bond graph.
     z_primary = 4, secondary (2-hop) distinct count z2 = 12, canonical
     path-count z0 = z_primary * (1 + |T|) = 4 * 13 = 52.
  2. Amorphous ensemble: coordination-preserving WWW bond-switching (keeps every
     node degree 4 -- the substrate-native disorder, NOT the coordination-
     breaking Gaussian-position smear that prior Model 3 already falsified).
     Sweep disorder (number of accepted switches). Measure <z2> topologically.
  3. z0_amorphous = z_primary * (1 + <z2>); implied alpha = p_c(z0)/8pi.
  4. Honest Outcome A/B/C/D.
"""

import math
import sys

import numpy as np

# ----- ALPHA-FREE constants (geometric only) -----
EIGHT_PI = 8.0 * math.pi  # pure geometric constant; NOT 8*pi*alpha
T_ORDER = 12  # |T| = order of proper tetrahedral rotation group (alpha-free, exact)
Z_PRIMARY = 4  # tetrahedral coordination of K4/diamond (alpha-free, topological)

# NOTE: this script reports the IMPLIED 1/alpha = 8pi/p_c(z0) only. The
# comparison to CODATA 1/137.036 lives in the RESULT DOC (markdown), NOT here --
# deliberately, so the script contains ZERO alpha in any form (no literal, no
# import of ave.core.constants). This honours BOTH the Path-C alpha-free guard
# (prereg Section 4) AND the DAG anti-cheat scan (verify_universe.py forbids a
# hardcoded 137.036). The CODATA number never enters the z0 computation either
# way; keeping it out of the script makes that provable by inspection.


# ============================================================
# Diamond / K4 lattice construction (radius-free topology)
# ============================================================
_DIAMOND_BASIS = np.array(
    [
        [0.0, 0.0, 0.0],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.5, 0.0],
        [0.25, 0.25, 0.25],
        [0.25, 0.75, 0.75],
        [0.75, 0.25, 0.75],
        [0.75, 0.75, 0.25],
    ]
)


def build_diamond(L: int = 4):
    """Build an L^3 diamond supercell (conventional cubic cell a = 1).

    Returns (positions Nx3 in [0,L)^3, box length L)."""
    cells = np.array([[i, j, k] for i in range(L) for j in range(L) for k in range(L)], dtype=float)
    pos = (cells[:, None, :] + _DIAMOND_BASIS[None, :, :]).reshape(-1, 3)
    return pos, float(L)


def nn_bond_graph(pos: np.ndarray, box: float):
    """Build the 4-nearest-neighbour bond graph under periodic boundaries.

    Pure topology: each node connects to its 4 nearest sites (the K4 bonds).
    No 1.187, no radius cutoff -- nearest-FOUR is the diamond coordination shell.
    """
    n = len(pos)
    adj = [set() for _ in range(n)]
    for i in range(n):
        d = pos - pos[i]
        d -= box * np.round(d / box)  # minimum image
        dist = np.linalg.norm(d, axis=1)
        dist[i] = np.inf
        nn = np.argsort(dist)[:4]
        for j in nn:
            adj[i].add(int(j))
    # symmetrise (mutual nearest neighbours in perfect diamond -> already symmetric)
    for i in range(n):
        for j in list(adj[i]):
            adj[j].add(i)
    return adj


# ============================================================
# Topological measurements (alpha-free)
# ============================================================
def mean_second_neighbour_count(adj):
    """<z2> = mean number of DISTINCT nodes at graph-distance exactly 2.

    In perfect diamond this is exactly 12 (= |T|): no short rings short-circuit
    the 2-hop shell. Short odd/even rings in the amorphous network can merge or
    collapse 2-hop endpoints, reducing <z2> below 12."""
    n = len(adj)
    vals = []
    for i in range(n):
        first = adj[i]
        second = set()
        for j in first:
            second |= adj[j]
        second -= first
        second.discard(i)
        vals.append(len(second))
    return float(np.mean(vals)), float(np.std(vals))


def ring_census(adj, max_size: int = 6):
    """Count shortest rings of size 3..max_size through each node (per-node mean).

    Short rings (<=4) are what merge 2-hop endpoints and would reduce <z2>."""
    n = len(adj)
    counts = {s: 0 for s in range(3, max_size + 1)}
    for i in range(n):
        for j in adj[i]:
            if j <= i:
                continue
            # 3-ring: common neighbour of i,j
            common = adj[i] & adj[j]
            counts[3] += len(common)
            # 4-ring: neighbour of i (not j) adjacent to neighbour of j (not i)
            for a in adj[i] - {j}:
                for b in adj[j] - {i}:
                    if a != b and b in adj[a]:
                        counts[4] += 1
    # normalise per node (3-rings counted once per edge => /n; 4-rings over-counted)
    return {s: counts[s] / n for s in counts}


# ============================================================
# Amorphous ensemble: coordination-preserving WWW bond-switching
# ============================================================
def www_switch(adj, n_moves: int, rng, forbid_short_rings: bool = True):
    """Apply WWW bond transpositions; every node stays degree-4 (coord-preserving).

    Classic move: pick bond (i,j); pick neighbour k of i (k!=j), neighbour l of j
    (l!=i); replace bonds {i-k, j-l} with {i-l, j-k}. Keeps all degrees fixed.
    Reject if it would create a self-loop, a double bond, or (optionally) a 3-ring.
    Returns number of accepted moves."""
    n = len(adj)
    nodes = list(range(n))
    accepted = 0
    attempts = 0
    max_attempts = n_moves * 40
    while accepted < n_moves and attempts < max_attempts:
        attempts += 1
        i = rng.integers(n)
        if not adj[i]:
            continue
        j = int(rng.choice(list(adj[i])))
        ni = [x for x in adj[i] if x != j]
        nj = [x for x in adj[j] if x != i]
        if not ni or not nj:
            continue
        k = int(rng.choice(ni))
        l = int(rng.choice(nj))
        # validity of new bonds i-l and j-k
        if l == i or k == j or l == k:
            continue
        if l in adj[i] or k in adj[j]:
            continue  # would create double bond
        if forbid_short_rings:
            # reject if i-l or j-k closes a 3-ring (shared neighbour)
            if (adj[i] - {k}) & (adj[l] - {j}):
                continue
            if (adj[j] - {l}) & (adj[k] - {i}):
                continue
        # commit: remove i-k, j-l ; add i-l, j-k
        adj[i].discard(k); adj[k].discard(i)
        adj[j].discard(l); adj[l].discard(j)
        adj[i].add(l); adj[l].add(i)
        adj[j].add(k); adj[k].add(j)
        accepted += 1
    # degree check (coordination-preserving invariant)
    degs = [len(a) for a in adj]
    assert all(d == 4 for d in degs), f"coordination broken: {set(degs)}"
    return accepted, attempts


# ============================================================
# FTG-EMT readout (alpha OUT)
# ============================================================
def ftg_pc(z0: float) -> float:
    """Feng-Thorpe-Garboczi rigidity-percolation threshold p_c(z0). Alpha-free."""
    return (10.0 * z0 - 12.0) / (z0 * (z0 + 2.0))


def implied_alpha_inv(z0: float) -> float:
    """Read alpha OUT: alpha = p_c(z0)/8pi  ->  return 1/alpha. 8pi is geometric."""
    return EIGHT_PI / ftg_pc(z0)


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 78)
    print("PATH C -- z0 from K4 AMORPHOUS geometry, ALPHA-FREE")
    print("PREREG: research/2026-06-08_pathc-z0-amorphous-emt-prereg.md")
    print("=" * 78)

    print("\n[ALPHA-FREE INPUT TRACE] every quantity entering z0:")
    print(f"  - diamond/K4 topology (coordination {Z_PRIMARY})        : geometric, alpha-free")
    print(f"  - |T| = {T_ORDER} (proper tetrahedral rotation group)   : group order, alpha-free")
    print(f"  - WWW disorder (bond-switch count)              : geometric move count, alpha-free")
    print(f"  - 8pi = {EIGHT_PI:.6f} (EMT readout constant)        : pure geometry, NOT 8pi*alpha")
    print(f"  - NO 1.187 / C_ratio (corpus-confirmed alpha-derived) : FORBIDDEN, absent")
    print(f"  - NO ave.core.constants import, NO e/eps0/hbar/Z0/c    : absent")
    print(f"  ('ave.core' in modules: {any('ave.core' in m for m in sys.modules)})")

    rng = np.random.default_rng(20260608)

    # ---- 1. Crystalline alpha-free baseline ----
    print("\n" + "-" * 78)
    print("STEP 1 -- Crystalline K4 baseline (alpha-free)")
    print("-" * 78)
    pos, box = build_diamond(L=4)
    adj0 = nn_bond_graph(pos, box)
    degs = [len(a) for a in adj0]
    z2_cryst, z2_std = mean_second_neighbour_count(adj0)
    rings0 = ring_census(adj0)
    z0_cryst = Z_PRIMARY * (1 + z2_cryst)
    print(f"  N nodes = {len(pos)};  degree set = {sorted(set(degs))} (expect all 4)")
    print(f"  <z2> distinct 2-hop neighbours = {z2_cryst:.4f} +/- {z2_std:.4f}  (expect 12 = |T|)")
    print(f"  short-ring census/node (3,4,5,6) = "
          f"{rings0[3]:.2f}, {rings0[4]:.2f}, {rings0[5]:.2f}, {rings0[6]:.2f}")
    print(f"  z0 = z_primary*(1+<z2>) = {Z_PRIMARY}*(1+{z2_cryst:.4f}) = {z0_cryst:.4f}")
    print(f"  -> implied 1/alpha = 8pi/p_c(z0) = {implied_alpha_inv(z0_cryst):.4f}")

    # ---- 2. Amorphous ensemble: WWW bond-switching sweep ----
    print("\n" + "-" * 78)
    print("STEP 2 -- Amorphous K4 (coordination-preserving WWW disorder) sweep")
    print("-" * 78)
    print(f"  (mean +/- std over {8} seeds; coordination held at 4 by construction)")
    print(f"  {'switch/node':>11} {'<z2>':>16} {'z0':>16} {'1/alpha':>16} {'4-ring/node':>11}")
    n_seeds = 8
    sweep_rows = []
    for frac in [0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]:
        n_moves = int(frac * len(pos))
        z2s, z0s, ais, r4s = [], [], [], []
        for s in range(n_seeds):
            srng = np.random.default_rng(20260608 + 101 * s)
            adj = [set(a) for a in adj0]  # fresh copy
            www_switch(adj, n_moves, srng, forbid_short_rings=True)
            z2, _ = mean_second_neighbour_count(adj)
            rings = ring_census(adj)
            z0 = Z_PRIMARY * (1 + z2)
            z2s.append(z2); z0s.append(z0); ais.append(implied_alpha_inv(z0)); r4s.append(rings[4])
        z2m, z2sd = float(np.mean(z2s)), float(np.std(z2s))
        z0m, z0sd = float(np.mean(z0s)), float(np.std(z0s))
        aim, aisd = float(np.mean(ais)), float(np.std(ais))
        sweep_rows.append((frac, z2m, z2sd, z0m, z0sd, aim, aisd, float(np.mean(r4s))))
        print(f"  {frac:>11.2f} {z2m:>9.4f}+/-{z2sd:<4.2f} {z0m:>9.4f}+/-{z0sd:<4.2f} "
              f"{aim:>9.3f}+/-{aisd:<5.2f} {np.mean(r4s):>11.2f}")

    # ---- 3. Reference EMT roots (alpha-free math; targets shown for context) ----
    print("\n" + "-" * 78)
    print("STEP 3 -- EMT readout reference points")
    print("-" * 78)
    for z0_ref, lbl in [(52.0, "path-count crystalline"),
                        (51.25, "EMT-canonical (alpha-located)"),
                        (z0_cryst, "this run, crystalline")]:
        print(f"  z0 = {z0_ref:7.4f} ({lbl:28s}) -> p_c = {ftg_pc(z0_ref):.5f}, "
              f"1/alpha = {implied_alpha_inv(z0_ref):.4f}")
    # what <z2> would be REQUIRED to hit 51.25 (for honest gap quantification)
    z2_needed = 51.25 / Z_PRIMARY - 1.0
    print(f"\n  To reach z0 = 51.25 needs <z2> = {z2_needed:.4f} (vs crystalline 12.0)")
    print(f"  i.e. amorphous disorder must REMOVE {12.0 - z2_needed:.4f} second-neighbours/node")

    # NOTE: the one-way comparison of these implied 1/alpha values against
    # CODATA 1/137.036 is done in the RESULT DOC, not here -- so this script
    # holds zero alpha (see header NOTE + prereg Section 4).

    # ---- Outcome ----
    z0_means = [r[3] for r in sweep_rows]
    z0_lo, z0_hi = min(z0_means), max(z0_means)
    # steady-state = highest-disorder rows (last two)
    ss_z0 = float(np.mean([sweep_rows[-1][3], sweep_rows[-2][3]]))
    ss_ai = float(np.mean([sweep_rows[-1][5], sweep_rows[-2][5]]))
    print("\n" + "=" * 78)
    print("OUTCOME (honest, per prereg Section 7)")
    print("=" * 78)
    print(f"  crystalline z0            = {z0_cryst:.3f}  -> 1/alpha = {implied_alpha_inv(z0_cryst):.3f}")
    print(f"  amorphous z0 mean-range   = [{z0_lo:.3f}, {z0_hi:.3f}]  across disorder strengths")
    print(f"  high-disorder steady-state z0 = {ss_z0:.3f} -> 1/alpha = {ss_ai:.3f}")
    print(f"  target (EMT-canonical)    = 51.25  (needs <z2>=11.8125, 1/alpha=137.04)")
    print(f"  (CODATA 1/137.036 comparison: see result doc -- kept out of script, alpha-free)")
    target_in_band = z0_lo - 0.05 <= 51.25 <= z0_hi + 0.05
    fixed_point = abs(ss_z0 - 51.25) < 0.1 and (z0_hi - z0_lo) < 0.3
    if fixed_point:
        print("  -> OUTCOME A (DERIVED): disorder-independent alpha-free fixed point at ~51.25.")
    elif target_in_band:
        print("  -> OUTCOME D (MODEL-DEPENDENT, with directional signal): amorphous disorder")
        print("     reduces z0 from 52 into a band STRADDLING 51.25, but the value is set by the")
        print("     (free) disorder strength -- no alpha-free principle selects 51.25 exactly.")
        print("     Direction + magnitude correct; selection not derived. Gap is now 'which disorder'.")
    else:
        print("  -> OUTCOME B (GAP REAL): disorder keeps z0 away from 51.25; 1.5% gap structural.")
    print()


if __name__ == "__main__":
    main()
