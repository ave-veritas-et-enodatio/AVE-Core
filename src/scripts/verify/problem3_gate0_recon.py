#!/usr/bin/env python3
"""GATE 0 — reproduce the FROZEN fork-memo's Problem-1/2 reconnaissance numbers
from canonical constants.py, establishing the E_c normalization the memo used.

This is verification of DISCLOSED inputs (the memo §1 tables), NOT the Problem-3
shift. It is the first gate of the Problem-3 arc (METHOD prereg:
research/2026-07-05_problem3-muonic-lamb_METHOD-prereg.md, frozen on the fork-memo
freeze commit 4747630b).

FROZEN-MEMO TARGETS (verbatim, research/2026-07-05_electrostatic-sector-fork-memo_FROZEN.md §1):
  ell_node = 386.16 fm
  no-solution radii r_ns (E=E_c): Z=1 -> 112.9 fm, Z=29 -> 607.8, Z=92 -> 1082.6
  muonic-H  Z=1 r=285 fm  E_coul=1.77e16 V/m  A^2=0.0246  r/ell=0.738
  U91+      Z=92 r=575 fm E_coul=4.01e17 V/m  A^2=12.6            r/ell=1.489
  Cu K-edge Z=29 r=1.8 pm E_coul=1.29e16 V/m  A^2=0.0130  r/ell=4.661

E_c NORMALIZATION (derived + stated): the memo's saturation field is the canonical
E_YIELD = V_YIELD/L_NODE = sqrt(alpha)*(m_e c^2)/(e*ell_node) = sqrt(alpha)*E_crit
(constants.py:489,500; Letter Eq.(Ec) papers/2026_birefringence_letter/main.tex:186).
"""
import numpy as np

from ave.core.constants import (
    E_YIELD,
    L_NODE,
    EPSILON_0,
    e_charge,
    V_YIELD,
    V_SNAP,
)

E_C = E_YIELD  # the memo's saturation field E_c


def E_coul(Z: int, r: float) -> float:
    return Z * e_charge / (4.0 * np.pi * EPSILON_0 * r**2)


def r_ns(Z: int) -> float:
    # radius where E_coul = E_c  ->  r = sqrt(Z e / (4 pi eps0 E_c))
    return np.sqrt(Z * e_charge / (4.0 * np.pi * EPSILON_0 * E_C))


def main() -> None:
    print("=== E_c NORMALIZATION (the memo's saturation field) ===")
    print(f"  V_SNAP  = m_e c^2 / e            = {V_SNAP:.6e} V")
    print(f"  V_YIELD = sqrt(alpha)*V_SNAP     = {V_YIELD:.6e} V")
    print(f"  E_c = E_YIELD = V_YIELD/L_NODE   = {E_C:.6e} V/m   (memo: ~1.13e17)")
    print(f"  ell_node = HBAR/(m_e c)          = {L_NODE*1e15:.4f} fm  (memo: 386.16)")
    print()

    print("=== PROBLEM 1 — no-solution radii (E = E_c) ===")
    for Z in (1, 29, 92):
        r = r_ns(Z)
        print(f"  Z={Z:3d}  r_ns = {r*1e15:8.2f} fm   r_ns/ell = {r/L_NODE:.3f}")
    print()

    print("=== PROBLEM 2 — Z-table of Coulomb fields at landmarks ===")
    landmarks = [("muonic-H", 1, 285e-15), ("U91+", 92, 575e-15), ("Cu K-edge", 29, 1.8e-12)]
    for name, Z, r in landmarks:
        E = E_coul(Z, r)
        A2 = (E / E_C) ** 2
        print(f"  {name:10s} Z={Z:3d} r={r*1e15:8.2f} fm  E={E:.3e} V/m  A^2={A2:.4g}  r/ell={r/L_NODE:.3f}")


if __name__ == "__main__":
    main()
