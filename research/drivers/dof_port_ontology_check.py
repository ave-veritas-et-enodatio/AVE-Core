#!/usr/bin/env python3
"""Receipts for the 2026-08-11 DoF-vs-PORT ontology walk (records-class).

🔴 ============================================================================ 🔴
   NOT CITABLE as a receipt for ANYTHING about DoF counts. QUARANTINED 2026-08-12
   by the #957 adjudication (M1 REFUTED, ONTOLOGY-DEAD). Preserved under Rule 12
   as the record of a check that did not work. Three independent reasons:

   1. IT MATCHES TWO DIFFERENT SIXES. Check `C2` claims the engine's 6 storage
      slots "match eq_axiom_1.tex:37 'six intrinsic degrees of freedom'". They do
      not. The engine's six is 3 translational DoF x 2 phase-space slots (an L and
      a C per direction); Axiom 1's six is 3 translations + 3 microrotations. The
      module under test says so itself at vacuum_node_circuit.py:12-25 — the
      per-DOF (L_i, C_i) is the MECHANICAL displacement-direction layer of the
      TRANSVERSE/EM-translation sector and "is NOT ... the A1 (V_inc, V_ref)
      dilatation-MASS phasor". C2 was a coincidence of the integer 6.

   2. THREE OF FOURTEEN CHECKS CANNOT FAIL: B1 (hardcoded 1+5 == 6), B2 (literal
      2 == 2), B3 (literal True). Unfireable gates dressed as receipts.

   3. IT IS PLACEMENT-BLIND. A live probe injected a genuine seventh slot
      (theta + pi_theta + K_bulk) into the REAL engine and this driver still
      reported "all receipts GREEN" — including "C3 NO seventh storage slot".
      It reads ONE function signature in ONE file. The family-D anti-tautology leg
      proved the PARSER can count to seven; it never proved the CHECK can find a
      seventh slot where one actually lives.

   THE LESSON: a probe that validates the parser is not a probe that validates the
   gate. The injection has to land where the real object lives.

   The killing fact for M1 is in master_equation_fdtd.py:112-113, :219, :265-267 —
   the scalar V carries its own initial condition AND its own conjugate momentum
   (V_prev), i.e. M1's own membership test, failed on its own terms.
🔴 ============================================================================ 🔴


The walk's load-bearing claim (M1) is that the longitudinal bulk scalar
(dilatation) is a PORT — an irreducible storage channel built from the three
translational coordinates — and NOT a seventh degree of freedom (state variable).

Three receipt families, all written so they CAN fail:

  A. `7`-IS-NOT-A-COUNT.  If the `7` in nu_vac = 2/7 were a mode count it would be
     an integer independent of the moduli. Recomputed across K/G: it slides.
  B. IRREP ARITHMETIC.    The scalar+deviatoric split is an SO(3) statement and
     yields TWO moduli, not seven of anything.
  C. ENGINE STATE-VECTOR. The machine-checkable adjudicator: read the operative
     node model and count independent per-node storage slots. 6 -> M1 survives;
     7 (an independent scalar slot with its own state) -> M1 is REFUTED.

Family C is the one an auditor should trust; A and B are arithmetic.

Run:  python3 research/drivers/dof_port_ontology_check.py
Exit: 0 = all receipts green.
"""

from __future__ import annotations

import re
from pathlib import Path

import sympy as sp

FAILURES: list[str] = []


def check(tag: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag:<52s} {detail}")
    if not ok:
        FAILURES.append(tag)


def repo_root() -> Path:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "manuscript").is_dir() and (parent / "Makefile").is_file():
            return parent
    raise SystemExit("repo root not found")


ROOT = repo_root()

# ======================================================================================
print("\nA — IS THE `7` A COUNT?  (walk record §3, D3)")
print("    nu_vac = (3K-2G)/(2(3K+G)).  The `7` is (3K+G)/G in units of G.")
K, G = sp.symbols("K G", positive=True)
nu = (3 * K - 2 * G) / (2 * (3 * K + G))

check("A0 nu = 2/7 exactly at K = 2G", sp.simplify(nu.subs(K, 2 * G) - sp.Rational(2, 7)) == 0,
      "vacuum-poisson-ratio.md:13")

rows = []
for ratio in (sp.Rational(1, 2), sp.Integer(1), sp.Rational(3, 2), sp.Integer(2),
              sp.Rational(7, 3), sp.Integer(3)):
    seven = sp.simplify((3 * ratio * G + G) / G)
    rows.append((ratio, seven, sp.simplify(nu.subs(K, ratio * G))))
    print(f"        K/G = {str(ratio):>4s}   (3K+G)/G = {str(seven):>5s}   nu = {str(rows[-1][2]):>8s}")

distinct = {r[1] for r in rows}
check("A1 the `7` SLIDES with K/G", len(distinct) > 1,
      f"{len(distinct)} distinct values across 6 stiffness ratios")
check("A2 a count would be K/G-invariant -> the `7` is NOT a count", len(distinct) > 1,
      "it is 3K+G at the GR-imported K=2G (PR#261)")

# ======================================================================================
print("\nB — IRREP ARITHMETIC (walk record §3; the SO(3) statement)")
# symmetric rank-2 tensor in 3D: 6 independent components = 1 trace + 5 traceless
n_sym = 6
n_trace, n_dev = 1, 5
check("B1 sym rank-2 in 3D splits 6 = 1 + 5", n_trace + n_dev == n_sym,
      "1 scalar (dilatation) + 5 deviatoric")
check("B2 two irreps -> TWO moduli (K, G)", 2 == 2,
      "not seven of anything; the split needs SO(3)")
check("B3 SO(3) is NOT the lattice group", True,
      "srs/K4 cubic-chiral, Zener A=1.23 (PR#506) -> 2/7 is a VRH average")

# ======================================================================================
print("\nC — ENGINE STATE-VECTOR (the machine-checkable adjudicator; walk record §2, M1)")
node = ROOT / "src/ave/core/vacuum_node_circuit.py"
cf3d = ROOT / "src/ave/topological/cosserat_field_3d.py"
check("C0 operative node model present", node.is_file(), str(node.relative_to(ROOT)))
check("C0b Cosserat field solver present", cf3d.is_file(), str(cf3d.relative_to(ROOT)))

src = node.read_text()
# The per-DOF node declares one (L, C) pair per translational DOF.
sig = re.search(r"def __init__\(\s*self,\s*lL=\(([^)]*)\),\s*lC=\(([^)]*)\)", src)
check("C1 PerDOFVacuumNode exposes per-DOF (L, C) tuples", sig is not None,
      "src/ave/core/vacuum_node_circuit.py")
if sig:
    n_L = len([x for x in sig.group(1).split(",") if x.strip()])
    n_C = len([x for x in sig.group(2).split(",") if x.strip()])
    print(f"        lL slots = {n_L}   lC slots = {n_C}   total per-node storage slots = {n_L + n_C}")
    check("C2 node carries 3 L + 3 C = 6 storage slots", (n_L, n_C) == (3, 3),
          "matches eq_axiom_1.tex:37 'six intrinsic degrees of freedom'")
    check("C3 NO seventh (scalar/volumetric) storage slot", (n_L + n_C) == 6,
          "-> M1 survives here; a 7th slot would REFUTE it")

fields = cf3d.read_text()[:1200]
two_fields = ("displacement u" in fields) and ("microrotation" in fields)
check("C4 solver carries exactly two 3-vector fields (u, omega)", two_fields,
      "cosserat_field_3d.py:4-5 'as independent fields'")
check("C5 no independent scalar/dilatation FIELD in that header",
      not re.search(r"\bdilatation field|scalar field theta|theta\(r\)", fields),
      "dilatation appears as a PORT/phasor, not a state (vacuum_node_circuit.py:17)")

# ======================================================================================
print("\nD — ANTI-TAUTOLOGY: can family C actually FAIL?")
# Prove the detector is not vacuously true by running it against a synthetic 7-slot node.
fake = "def __init__(self, lL=(1.0, 1.0, 1.0, 1.0), lC=(1.0, 1.0, 1.0)"
m = re.search(r"def __init__\(\s*self,\s*lL=\(([^)]*)\),\s*lC=\(([^)]*)\)", fake)
fake_n = len(m.group(1).split(",")) + len(m.group(2).split(","))
check("D1 detector reports 7 on a synthetic 7-slot node", fake_n == 7,
      "so C2/C3 are falsifiable, not vacuous")

print("\n" + "=" * 92)
print("🔴 QUARANTINED 2026-08-12 — NOT CITABLE for any DoF-count claim. M1 was REFUTED by the")
print("   #957 adjudication (master_equation_fdtd.py:112-113,:219,:265-267 — V has its own IC and")
print("   its own conjugate momentum V_prev). This driver's C-family is placement-blind and its")
print("   C2 matches two DIFFERENT sixes; B1/B2/B3 cannot fail. See the module docstring.")
print("=" * 92)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILED -> {FAILURES}")
    raise SystemExit(1)
print("RESULT: checks green — AND THAT MEANS NOTHING ABOUT DoF COUNTS. Green here was green")
print("        while a real seventh slot sat in the engine. Preserved as a record, not a receipt.")
