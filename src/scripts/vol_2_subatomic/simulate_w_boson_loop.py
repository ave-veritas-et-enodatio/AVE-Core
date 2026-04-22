#!/usr/bin/env python3
"""
W-Boson Self-Consistent Loop Correction (P2.7)
===============================================

Runs the full depth-1 → self-consistent back-saturation iteration and
prints the convergence table.  All values derived from AVE axioms; zero
free parameters.

Engine files:
  src/ave/topological/cosserat.py              — M_W constants + w_boson_self_consistent_correction()
  src/ave/solvers/transmission_line.py         — build_radial_tree_admittance_graded()
"""

import sys
from pathlib import Path

src_path = str(Path(__file__).parent.parent.parent.parent)
if src_path not in sys.path:
    sys.path.append(src_path)

from ave.topological.cosserat import (
    M_W_TREE,
    M_W,
    M_W_MEV,
    M_Z,
    M_Z_MEV,
    MISMATCH_LOSS,
    MISMATCH_LOSS_SC,
    S11_W_BOUND,
    S11_W_SC,
    w_boson_self_consistent_correction,
)
from ave.core.constants import C_0, e_charge

_J_PER_MEV = float(e_charge) * 1e6
PDG_MW = 80_379.0  # MeV  (PDG 2022)
PDG_MZ = 91_188.0  # MeV  (PDG 2022)

# ─── Headers ──────────────────────────────────────────────────────────────────
BAR = "=" * 66


def pct(got, pdg):
    return (got / pdg - 1.0) * 100.0


# ─── Block 1: Derivation chain ────────────────────────────────────────────────
print(BAR)
print("  AVE ENGINE: W-BOSON SELF-CONSISTENT LOOP CORRECTION (P2.7)")
print(BAR)

m_w_tree_mev = M_W_TREE * C_0**2 / _J_PER_MEV
print(f"\n  M_W (tree-level)         = {m_w_tree_mev:>10.4f} MeV   ({pct(m_w_tree_mev, PDG_MW):+.4f}%)")

# ─── Block 2: Self-consistent iteration ───────────────────────────────────────
print(f"\n  Self-Consistent Back-Saturation (Axiom 1 + Axiom 4):")
print(f"  {'iter':>5}  {'Y[0,0]':>12}  {'S11':>12}  {'|S11|^2':>12}  {'M_W (MeV)':>12}  {'dev%':>8}")
print(f"  " + "-" * 63)

sc = w_boson_self_consistent_correction(max_iter=50, tol=1e-12)

# Re-run iteration visibly for display
import math
import numpy as np
from ave.core.constants import NU_VAC
from ave.solvers.transmission_line import build_radial_tree_admittance, s11_from_y_matrix

Z = 4
Y_origin_base = Z * float(NU_VAC)
Y_d1 = build_radial_tree_admittance(depth=1, branch_y=NU_VAC, boundary_y=0.0, coordination_z=Z)
s11_d1 = float(s11_from_y_matrix(Y_d1, port=0, Y0=1.0).real)

total_delta = s11_d1**2 * Y_origin_base
s11_prev = s11_d1

for i in range(1, 15):
    Y_iter = Y_d1.copy()
    Y_iter[0, 0] -= total_delta
    s11_i = float(s11_from_y_matrix(Y_iter, port=0, Y0=1.0).real)
    back_sat = s11_i**2
    ml = 1.0 - back_sat
    mw_i = m_w_tree_mev / ml
    print(
        f"  {i:>5}  {Y_iter[0,0].real:>12.8f}  {s11_i:>12.8f}  {back_sat:>12.8f}  {mw_i:>12.4f}  {pct(mw_i, PDG_MW):>+8.4f}%"
    )
    if abs(s11_i - s11_prev) < 1e-12:
        print(f"  [CONVERGED at iteration {i}]")
        break
    total_delta = s11_i**2 * Y_origin_base
    s11_prev = s11_i

# ─── Block 3: Final comparison ────────────────────────────────────────────────
print(f"\n  Summary")
print(f"  {'':40}  {'MeV':>10}  {'dev%':>8}")
print(f"  " + "-" * 63)
print(f"  {'Tree-level M_W':40}  {m_w_tree_mev:>10.2f}  {pct(m_w_tree_mev, PDG_MW):>+8.4f}%")
print(f"  {'Depth-1 hard saturation':40}  {sc['M_W_d1_MeV']:>10.2f}  {pct(sc['M_W_d1_MeV'], PDG_MW):>+8.4f}%")
print(f"  {'Self-consistent (converged)':40}  {sc['M_W_sc_MeV']:>10.2f}  {pct(sc['M_W_sc_MeV'], PDG_MW):>+8.4f}%")
print(f"  {'PDG (CODATA 2022)':40}  {PDG_MW:>10.2f}  {'±0.000%':>8}")
print(f"\n  M_Z (from M_W × 3/√7)   = {M_Z_MEV:>10.2f} MeV   ({pct(M_Z_MEV, PDG_MZ):+.4f}%)")
print(f"  M_Z PDG                  = {PDG_MZ:>10.2f} MeV")

print(f"\n  Convergence: {sc['n_iter']} iterations, converged={sc['CONVERGED']}")
print(f"  delta_Y_origin = {sc['delta_Y_origin']:.10f}  (reduction to Y[0,0])")

print(f"\n{BAR}")
print("  PHYSICAL INTERPRETATION")
print(BAR)
print(
    """
  The W-boson occupies a single lattice node.  Its energy density
  immediately saturates the 4 nearest-neighbour nodes (open-circuit,
  Y_boundary = 0).  This produces S11 ≈ -0.0588 at depth 1.

  Self-consistent correction (P2.7):
    The reflected power |S11|² back-enters the origin node.  Under
    Axiom 4 (C_eff = C0 / √(1 − (V/Vs)²)), this second excitation
    reduces the origin's effective self-admittance by |S11|² × Y_origin.
    The fixed-point solution satisfies:

        Y[0,0]* = Y[0,0]^(0) − |S11(Y[0,0]*)|² × (z × ν_vac)

    Solved iteratively; ratio |S11|² ≈ 0.00375 ≪ 1 → geometric convergence.

  Result:  S11_sc ≈ -0.06123  →  M_W = 80,224 MeV  (-0.19%)
  Improved from depth-1 hard:  M_W = 80,201 MeV  (-0.22%)
"""
)
print(BAR)
