#!/usr/bin/env python3
"""
Higher-Order Anomalous Magnetic Moment (C2) — Peer-Review Remediation P2.1
==========================================================================

EXPLORATORY: per peer-review remediation P2.1 (commit 908b077, 2026-04-15),
"P2.1 C_2 anomaly reframed as an open measurement vs integration limits."
Schwinger's 1st-order term a_e = α/(2π) is derived elsewhere (Vol 2 Ch 6,
manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/higgs-mass.md);
the 2nd-order C_2 coefficient via K4 structural reflection is currently OPEN —
the script outputs the 97% gap as findings data, not as a passing prediction.

Status: open per Rule 11 falsification record (committed in honest framing).
Per Rule 12 retraction-preserves-body: prose updated 2026-04-30 to honestly
report 97% gap; computation unchanged.

Computes the K4 lattice Green's function reflection (S_11) strictly from the
discrete admittance topology, utilizing the universal nodal admittance solver.
The corpus question this exploratory script addresses: does the K4 structural
reflection at finite radial depth quantitatively reproduce the QED 2nd-order
C_2 coefficient (-0.328478965)? Answer empirically: NO at depth=3, branch=NU_VAC,
boundary=1.0 (gap 97%). Whether the gap closes at different depth/branch/boundary
parameters, OR whether the K4 structural reflection is a different physical
quantity than QED's 2nd-order loop coefficient, is the open question.
"""

import numpy as np
import sys
from pathlib import Path

# Add src to path to allow direct execution
src_path = str(Path(__file__).parent.parent.parent)
if src_path not in sys.path:
    sys.path.append(src_path)

from ave.core.constants import NU_VAC
from ave.solvers.transmission_line import s11_from_y_matrix, build_radial_tree_admittance

def compute_c2_structural() -> float:
    """
    Computes C2 as the structural reflection S_11 of the K4 topology.
    """
    # 3-hop depth captures the exact local structural deviations of the Diamond lattice
    # before reaching the effective infinite continuum regime.
    # We use tracking parameters for the K4 geometry (coordination_z=4).
    Y = build_radial_tree_admittance(depth=3, branch_y=NU_VAC, boundary_y=1.0, coordination_z=4)
    
    # The source injects from the origin (port 0) with vacuum characteristic impedance
    s11 = s11_from_y_matrix(Y, port=0, Y0=1.0)
    
    return float(np.real(s11))

if __name__ == "__main__":
    c2 = compute_c2_structural()
    c2_pdg = -0.328478965
    
    error = abs(c2 - c2_pdg) / abs(c2_pdg) * 100
    
    print("==========================================================")
    print("  AVE ENGINE: 2ND-ORDER g-2 (C2) — PEER-REVIEW P2.1 OPEN  ")
    print("==========================================================")
    print(f"Lattice Derived C2:  {c2:.9f}")
    print(f"QED/PDG Target C2:   {c2_pdg:.9f}")
    print(f"Deviation:           {error:.2f}%   (NOT a passing match)")
    print("==========================================================")
    print()
    print("Status: P2.1 OPEN — committed 2026-04-15 (commit 908b077) as")
    print("  'C_2 anomaly reframed as an open measurement vs integration limits.'")
    print("  Schwinger 1st-order a_e = α/(2π) is derived in Vol 2 Ch 6.")
    print("  This script's 2nd-order C_2 via K4 structural reflection at")
    print("  depth=3, branch=NU_VAC, boundary=1.0 does NOT reproduce QED's")
    print("  C_2 coefficient. Two open candidate explanations:")
    print("    (a) The K4 structural reflection at this depth/boundary is a")
    print("        different physical quantity than QED's 2nd-order loop")
    print("        coefficient; comparison is structurally mismatched.")
    print("    (b) Different (depth, branch_y, boundary_y, coordination_z)")
    print("        parameters would close the gap; this default invocation")
    print("        is one of many possible computations, not the canonical one.")
    print("  Pending Grant adjudication. Currently NOT a corpus-canonical")
    print("  electron-physics anchor; recorded as exploratory empirical data.")
