"""Single-substrate-scale consistency web (Vol 1 Foundations).

ONE imported lattice scale (m_e, via the calibration identity
ell_node = hbar/(m_e c)) appears as five algebraic faces, four of which
collapse to m_e c^2 (the fifth, the inductor rest energy, is 1/2 m_e c^2 by
the Virial pairing). This script is a SELF-CONSISTENCY check of the corpus
bookkeeping -- NOT a derivation of m_e and NOT a multi-quantity consistency
between independent measurements.

  HONEST SCOPE (frame-check 2026-06-22, claim_survives=false):
  --------------------------------------------------------------------------
  At the VALUE level the five appearances are a pure chain of definitions
  rooted in the single literal M_E. Only M_E is an independent literal in
  src/ave/core/constants.py; everything else is M_E downstream:

      L_NODE   = HBAR / (M_E * C_0)              (defined VIA M_E)
      OMEGA_C  = C_0 / L_NODE                    => hbar*OMEGA_C == m_e c^2
                                                    BY the definition of ell_node
      B_SNAP   = sqrt(2*MU_0 * M_E*C_0^2 / L_NODE^3)
                                                 (m_e c^2 INSERTED by hand)
      XI_TOPO  = e_charge / L_NODE
      I_max    = XI_TOPO * c     (relativistic-inductor.md)
      L_0      = XI_TOPO^-2 * m_0 (Topo-Kinematic map)

  So "all five = m_e c^2" is m_e = m_e, a MULTI-DEFINITION TAUTOLOGY, not a
  consistency between independent quantities. This driver therefore LABELS
  each face as DEFINITION-CIRCULAR (CD) vs INDEPENDENTLY-SET (IS); exactly
  ONE quantity (M_E) is IS, the other five are CD.

  What this driver legitimately establishes:
    (a) VALIDATE-ON-KNOWN: m_e c^2 -> 510.999 keV from the imported scale
        (peer-with-QED: QED equally ties Compton length / Schwinger field to
        m_e; no SM-distinct content at the VALUE level).
    (b) The corpus is INTERNALLY CONSISTENT: the five defining equations in
        constants.py + relativistic-inductor.md do reduce to m_e c^2 to the
        stated tolerance, with no factor errors. A failure here is a
        load-bearing bug in the constants chain.
    (c) The HONEST differentiator (recorded in the KB leaf, NOT a chord):
        PARAMETER ECONOMY -- AVE imports ONE dimensionful scale and expresses
        five faces algebraically; the SM imports the electron Yukawa as one
        of ~19+ independent dials. Economy != prediction.

  Forbidden framings (do NOT print or imply): "structural unification the SM
  lacks", "AVE forces these to coincide", "five independent quantities agree",
  "the SM has nothing relating its EM cutoff to m_e".

  Canonical home: vol1/axioms-and-lattice/ch1-fundamental-axioms/
                  single-substrate-scale.md  (clm-sw5oao, solidity 0.25)
  Sibling driver: bootstrap_constants_check.py (the Q=1/alpha chain).
"""

import os
import sys

# Import the constants module from THIS repo checkout (the branch the driver
# lives on), not a hardcoded sibling checkout: OMEGA_C / B_SNAP / XI_TOPO are
# branch-state-sensitive, so resolve src/ relative to this file.
_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
sys.path.insert(0, _SRC)

from ave.core.constants import (  # noqa: E402
    B_SNAP,
    C_0,
    HBAR,
    L_NODE,
    M_E,
    MU_0,
    OMEGA_C,
    XI_TOPO,
    e_charge,
)

# Tolerance for the "collapses to m_e c^2" assertions. The faces are exact by
# construction; any deviation above this is a constants-chain factor bug.
TOL = 1e-12


def _relerr(value: float, target: float) -> float:
    return abs(value - target) / abs(target)


def main() -> int:  # noqa: PLR0915
    print("=" * 78)
    print("  Single-substrate-scale consistency web")
    print("  ONE imported scale (m_e via ell_node) -> five algebraic faces")
    print("=" * 78)

    # ---- The single independent literal (the ONLY IS quantity) -------------
    m_e_c2 = M_E * C_0**2
    print()
    print("INDEPENDENTLY-SET (IS) literal -- the one imported dimensionful scale:")
    print(f"  M_E              = {M_E:.10e} kg   [constants.py M_E: CODATA literal]")
    print(f"  => m_e c^2       = {m_e_c2:.10e} J")
    print(f"                   = {m_e_c2 / e_charge / 1e3:.6f} keV   "
          "[VALIDATE-ON-KNOWN: 510.999 keV, peer-with-QED]")

    # ---- The five faces, each labeled CD (definition-circular) -------------
    # Each face is m_e c^2 (or 1/2 m_e c^2) BY the definition of the symbols it
    # is built from; none is an independent measurement AVE postdicts.
    faces = []

    # (1) EM temporal cutoff: hbar * OMEGA_C, OMEGA_C = C_0 / L_NODE.
    #     hbar*OMEGA_C = hbar c / ell_node = hbar c (m_e c / hbar) = m_e c^2
    #     identically, since ell_node = hbar/(m_e c). True BY definition of
    #     ell_node (constants.py comment at OMEGA_C: "since ell_node = hbar/(m_e c)").
    face1 = HBAR * OMEGA_C
    faces.append(("(1) EM cutoff   hbar*OMEGA_C", face1, m_e_c2, "CD",
                  "OMEGA_C=C_0/L_NODE, L_NODE=HBAR/(M_E*C_0) -> hbar*OMEGA_C "
                  "== m_e c^2 by def of ell_node"))

    # (2) Node saturation energy: (B_SNAP^2 / 2 mu0) * ell_node^3.
    #     B_SNAP is DEFINED by solving (B^2/2mu0) = m_e c^2/ell^3 for B, i.e.
    #     m_e c^2 is inserted into the numerator by hand. Recovers its own input.
    face2 = (B_SNAP**2 / (2.0 * MU_0)) * L_NODE**3
    faces.append(("(2) node sat.   (B_SNAP^2/2mu0)*ell^3", face2, m_e_c2, "CD",
                  "B_SNAP=sqrt(2 mu0 m_e c^2/ell^3): m_e c^2 inserted by hand"))

    # (4) Compton length: ell_node itself == hbar/(m_e c). The DEFINITIONAL
    #     calibration identity (form-deriving-value-importing.md m_e/ell_node row:
    #     "an input by construction, not a value the substrate is asked to select").
    face4 = L_NODE
    face4_target = HBAR / (M_E * C_0)
    faces.append(("(4) Compton     ell_node", face4, face4_target, "CD",
                  "ell_node == hbar/(m_e c): the calibration identity (DEFINITIONAL)"))

    # ---- Assert the m_e c^2 faces (1,2) and the identity face (4) ----------
    print()
    print("Faces that collapse to m_e c^2 (faces 1,2) / to ell_node (face 4):")
    print(f"  {'face':<40} {'kind':<4} {'rel-err':>12}")
    ok = True
    for label, val, tgt, kind, why in faces:
        re = _relerr(val, tgt)
        flag = "OK " if re <= TOL else "BAD"
        if re > TOL:
            ok = False
        print(f"  {label:<40} {kind:<4} {re:>12.2e}  {flag}")
        print(f"      why CD: {why}")
        # A failure here is a constants-chain factor bug, not physics.
        assert re <= TOL, f"{label}: rel-err {re:.2e} > TOL {TOL:.0e}"

    # (3) Relativistic-inductor rest energy: E_0 = 1/2 L_0 I_max^2.
    #     L_0 = XI_TOPO^-2 * m_0, I_max = XI_TOPO * c (relativistic-inductor.md).
    #     => E_0 = 1/2 (xi^-2 m0)(xi c)^2 = 1/2 m0 c^2 -- the xi_topo factors
    #     CANCEL identically; true for ANY xi_topo. This is the HALF; the
    #     Virial pairing with the capacitive half recovers the full m_e c^2.
    m0 = M_E
    L_0 = XI_TOPO**-2 * m0
    I_max = XI_TOPO * C_0
    face3 = 0.5 * L_0 * I_max**2
    re3 = _relerr(face3, 0.5 * m_e_c2)
    print()
    print("(3) inductor    E_0 = 1/2 L_0 I_max^2   (the HALF; Virial-pairs to full)")
    print(f"      E_0 = {face3:.10e} J   target 1/2 m_e c^2 = {0.5 * m_e_c2:.10e} J"
          f"   rel-err {re3:.2e}  CD")
    print("      why CD: L_0=xi^-2 m0, I_max=xi c -> E_0=1/2 m0 c^2; "
          "xi_topo CANCELS (true for ANY xi/ell_node) -- carries ZERO scale info")
    assert re3 <= TOL, f"face(3) rel-err {re3:.2e} > TOL"
    print(f"      I_max = XI_TOPO * c = {I_max:.6f} A   "
          "(the topological current ceiling, face 5)")
    if re3 > TOL:
        ok = False

    # (5) Topological current ceiling: I_max = XI_TOPO * c, with
    #     XI_TOPO = e/ell_node. NOT itself equal to m_e c^2 (it has units of A);
    #     it is the magnetic-sector projection of the same saturation scale and
    #     it sets the inductor rest energy in face (3). Reported, not asserted=m_e c^2.
    print()
    print(f"(5) current     I_max = XI_TOPO*c = {I_max:.6f} A   CD")
    print("      why CD: XI_TOPO=e/L_NODE, L_NODE=HBAR/(M_E*C_0) -- M_E downstream")

    # ---- The circularity verdict (the honest headline) ---------------------
    print()
    print("-" * 78)
    print("CIRCULARITY LABELING (frame-check circularity_verdict):")
    print("  INDEPENDENTLY-SET (IS): 1  -> M_E only")
    print("  DEFINITION-CIRCULAR (CD): 5 -> OMEGA_C, B_SNAP, ell_node, I_max, L_0")
    print("  'All five = m_e c^2' is m_e = m_e: a MULTI-DEFINITION TAUTOLOGY,")
    print("  NOT a consistency between independent quantities.")
    print("  This is a SELF-CONSISTENCY artifact (one-import economy), not a")
    print("  derivation of m_e and not an SM-distinct forced coincidence:")
    print("  QED equally ties the Compton length / Schwinger field to m_e.")
    print("-" * 78)

    if ok:
        print("RESULT: PASS -- the five-face consistency web is internally consistent")
        print("        (constants chain carries no factor error). Honest scope:")
        print("        one-import economy + same-substrate-event ONTOLOGY (explanatory),")
        print("        VALUE=echo, multi-face IDENTITY=definitional-by-construction.")
        return 0
    print("RESULT: FAIL -- a face did not reduce to its definitional target;")
    print("        load-bearing constants-chain bug.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
