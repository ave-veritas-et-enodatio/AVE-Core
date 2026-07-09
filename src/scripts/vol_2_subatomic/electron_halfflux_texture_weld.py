"""Half-flux selection test, framing 2 of 3: texture-holonomy-weld.

Does a substrate-native K4 term WELD the odd-q texture -1 (the (0,1) [T2,SO(3)]
class) to the 2pi spin-rotation double-cover -1 (belt trick), and is the weld / the
1/2 FORCED by K4 discreteness or does it require an imported coupling/defect-choice?

Anti-tautology gates enforced by construction:
  (1) NO alpha anywhere.
  (2) NO half-angle lift exp(i*sigma.omega/2). Rotations built from FULL-angle SO(3)
      matrices (abelian reading) or from A4 port-permutations (lattice reading); SU(2)
      sign read by Shepperd matrix->quaternion, resolved by continuity. Verified:
      k4_lattice_holonomy.uses_analytic_qbody() == False.
  (3) NO fitted coefficient. k_hopf=pi/3 is NEVER imported here.
  (4) The 1/2 must fall out of K4 alone -- this is exactly what we test.

RESULT: [HALF-FLUX-ECHO]. The abelian reading gives a clean odd/even texture
discriminator ((-1)^q) but the spin loop is winding-independent; the lattice reading
shows -I at n=3 is K4-forced but tracks the Frank-rotation ORDER (a C2 edge defect
puts -I at even n), so it is NOT an odd-q selector. The two Z2's stay independent.
See research/2026-07-08_electron-halfflux-selection_result.md
"""

from __future__ import annotations

import numpy as np

from ave.core.chiral_lattice import build_diamond_net
from ave.topological.k4_lattice_holonomy import (
    holonomy_of_path,
    loop_plane,
    repeat_loop,
    rotation_from_port_permutation,
    rotation_matrix_to_quaternion,
    shortest_closed_loop,
    uses_analytic_qbody,
)


# ---- abelian (upstream) reading: FULL-angle SO(3), no half-angle ---------------
def rot_z(theta: float) -> np.ndarray:
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def loop_lift_monodromy(mats: list[np.ndarray]) -> float:
    q0 = rotation_matrix_to_quaternion(mats[0])
    qp = q0.copy()
    for R in mats[1:]:
        q = rotation_matrix_to_quaternion(R)
        if np.dot(q, qp) < 0.0:
            q = -q
        qp = q
    return float(np.dot(qp, q0))


def texture_psi_monodromy(q: int, n: int = 8000) -> float:
    """psi-cycle monodromy (-1)^q -- the (0,1)-vs-(0,0) texture class as a sign."""
    return loop_lift_monodromy([rot_z(q * a) for a in np.linspace(0.0, 2.0 * np.pi, n)])


def spin_loop_monodromy(p: int, q: int, n: int = 8000) -> float:
    """Global 2pi rotation-loop monodromy -- the statistics sign (belt trick)."""
    r0 = rot_z(p * 0.7 + q * 1.9)
    return loop_lift_monodromy([rot_z(2 * np.pi * t) @ r0 for t in np.linspace(0, 1, n)])


def main() -> None:
    print("=" * 78)
    print("GATE CHECK: uses_analytic_qbody() =", uses_analytic_qbody(), "(must be False)")
    print("=" * 78)

    # ---- TEST C: abelian Z2 texture vs winding-independent spin loop ----------
    print("\n[C] ABELIAN reading -- texture psi-cycle (-1)^q  vs  2pi spin loop")
    print(f"{'(p,q)':>8} | {'texture psi':>12} | {'spin 2pi':>10} | {'spin 4pi':>10}")
    for (p, q) in [(2, 3), (2, 2), (1, 1), (3, 5), (1, 2)]:
        tm = texture_psi_monodromy(q)
        sm2 = spin_loop_monodromy(p, q)
        r0 = rot_z(p * 0.7 + q * 1.9)
        sm4 = loop_lift_monodromy([rot_z(4 * np.pi * t) @ r0 for t in np.linspace(0, 1, 8000)])
        print(f"{str((p, q)):>8} | {tm:>+12.3f} | {sm2:>+10.3f} | {sm4:>+10.3f}")

    # ---- TEST D: independence -> the two Z2's are NOT welded by the engine ----
    print("\n[D] WELD/INDEPENDENCE: does the spin sign CO-VARY with texture parity?")
    print("    welded => spin follows (-1)^q ; independent => spin=-1 regardless.")
    print("    (a per-row equal-sign is a COINCIDENCE; the discriminator is the even-q control.)")
    for (p, q) in [(2, 3), (2, 2)]:
        tex = texture_psi_monodromy(q)
        spin = spin_loop_monodromy(p, q)
        # NOTE: for (2,3) both happen to be -1 -- that is a coincident sign, NOT a weld.
        # The (2,2) control (texture +1, spin -1) is what proves independence.
        label = "coincident-sign (see even-q control)" if np.isclose(tex, spin) \
            else "INDEPENDENT (spin -1 even when texture +1)"
        print(f"    ({p},{q}): texture={tex:+.0f}  spin2pi={spin:+.0f}  -> {label}")

    # ---- TEST A: SUBSTRATE-NATIVE lattice reading -- C3 disclination -----------
    print("\n[A] LATTICE reading -- C3 vertex disclination, encircle n times (Z6 lift):")
    net = build_diamond_net(L=8)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect_c3 = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}
    print(f"{'n':>3} | {'net_wind':>8} | {'R=I?':>6} | {'sign(w)':>8} | clean Z2 statistics sign")
    for n in range(1, 7):
        h = holonomy_of_path(net, repeat_loop(loop, n), defect=defect_c3)
        RI = h["so3_is_identity"]
        z2 = f"{h['holonomy_sign']:+.0f}" if RI else "-- (R != I, not a statistics sign)"
        print(f"{n:>3} | {h['net_winding']:>8} | {str(RI):>6} | {h['holonomy_sign']:>+8.2f} | {z2}")

    # ---- TEST B: DISCRIMINATOR -- C3 (order3) -> C2 edge (order2) --------------
    print("\n[B] DISCRIMINATOR -- swap C3 (order3) -> C2 edge (order2) disclination:")
    C2_edge = (1, 0, 3, 2)  # even perm (double transposition) = 180 deg edge rotation
    R_c2 = rotation_from_port_permutation(C2_edge)
    print(f"    C2 edge perm {C2_edge}: SO(3) order = "
          f"{'2' if np.allclose(R_c2 @ R_c2, np.eye(3)) else '>2'}; "
          f"lift w={rotation_matrix_to_quaternion(R_c2)[0]:+.3f} (90deg -> order-4 lift)")
    print(f"{'n':>3} | {'R=I?':>6} | clean Z2 statistics sign (C2 defect)")
    for n in range(1, 5):
        h = holonomy_of_path(net, repeat_loop(loop, n), defect=defect_c3, frank_override=C2_edge)
        RI = h["so3_is_identity"]
        z2 = f"{h['holonomy_sign']:+.0f}" if RI else "-- (R != I)"
        print(f"{n:>3} | {str(RI):>6} | {z2}")
    print("    => -I now lands at n=2 (EVEN). 'winding=Frank-order' -> -I is GENERIC,")
    print("       reachable by even winding on a C2 defect. Not an odd-q selector.")


if __name__ == "__main__":
    main()
