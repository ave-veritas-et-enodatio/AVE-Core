"""Half-flux selection test, framing 1 of 3: k4-flux-quantization.

Does DISCRETE K4 structure quantize the flux the odd-q texture threads through the
2pi rotation loop to exactly 1/2 (mod 1) -- i.e. does the electron's fermion sign
FALL OUT of K4 discreteness (A4 C3 order-3, 2T double cover) ALONE, vs pi/3, vs a
continuous/fitted value?

Committed, self-contained version (the small substrate-native helpers texture_class
and spin_loop_monodromy are inlined here so the driver runs against `main`; they are
the same full-angle-SO(3) + Shepperd-continuity constructions as the pi1 topology
script electron_pi1_spinhalf_topology.py, PR #584).

ANTI-TAUTOLOGY GATES (all must be clean for FORCED):
  (1) NO alpha on the path.
  (2) NO half-angle lift exp(i*sigma.omega/2) as an INPUT (uses_analytic_qbody False).
  (3) NO fitted coefficient (k_hopf=pi/3 matched to Q_H=6 FORBIDDEN as input).
  (4) the 1/2 (or pi) must come OUT of the K4 discrete structure ALONE.

DISCRIMINATOR (chord vs echo): a flux term is a CHORD iff it gives half-flux (1/2)
for ODD-q (2,3) AND integer flux (0) for EVEN-q (2,2). If half-flux for BOTH -> it
is the generic winding-INDEPENDENT belt-trick Z2 that pi1 already found -> ECHO.

DECISIVE K4-LOAD-BEARING TEST: run every flux computation BOTH on the K4 lattice
(k4_lattice_holonomy, A4 port-permutation rotations) AND in the continuum SO(3)
sigma-model (full-angle rot_z, np.linspace). If the 1/2 is IDENTICAL in both, the
1/2 is a property of SO(3)'s Z2 double cover (present in the featureless continuum),
NOT of K4 discreteness -> gate (4) FAILS -> the 1/2 is not K4-forced.

RESULT: [HALF-FLUX-ECHO]. See research/2026-07-08_electron-halfflux-selection_result.md
"""

from __future__ import annotations

import numpy as np

from ave.core.chiral_lattice import build_diamond_net
from ave.topological import k4_lattice_holonomy as k4h


# ----------------------------------------------------------------------------
# Inlined substrate-native helpers (full-angle SO(3), Shepperd continuity lift;
# NO half-angle input). Identical to electron_pi1_spinhalf_topology.py.
# ----------------------------------------------------------------------------
def rot_z(theta: float) -> np.ndarray:
    """SO(3) rotation by the FULL angle theta about z (cos theta, sin theta)."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def loop_lift_monodromy(mats: list[np.ndarray]) -> float:
    """Continuity-tracked SU(2)-lift monodromy of a closed loop of SO(3) matrices."""
    q0 = k4h.rotation_matrix_to_quaternion(mats[0])
    qp = q0.copy()
    for R in mats[1:]:
        q = k4h.rotation_matrix_to_quaternion(R)
        if np.dot(q, qp) < 0.0:
            q = -q
        qp = q
    return float(np.dot(qp, q0))


def texture_class(p: int, q: int, n: int = 8000) -> dict:
    """psi-cycle SU(2)-lift monodromy (-1)^q and the [T2,SO(3)] liftability."""
    m_psi = loop_lift_monodromy([rot_z(q * a) for a in np.linspace(0.0, 2.0 * np.pi, n)])
    return {"psi_cycle_monodromy": m_psi, "su2_liftable": (p % 2 == 0 and q % 2 == 0)}


def spin_loop_monodromy(p: int, q: int, n: int = 8000) -> dict:
    """Monodromy of a global 2pi rigid frame-rotation applied to the whole (p,q) field."""
    r0 = rot_z(p * 0.7 + q * 1.9)
    m = loop_lift_monodromy([rot_z(2.0 * np.pi * t) @ r0 for t in np.linspace(0.0, 1.0, n)])
    return {"spin_monodromy_2pi": m}


# ----------------------------------------------------------------------------
# Flux reading: a CLOSED-loop SU(2) holonomy that is +/-I (scalar) carries a
# quantized flux.  U = +I -> Phi/Phi0 = 0 ;  U = -I -> Phi/Phi0 = 1/2.
# The "1/2" is arg(-1)/2pi -- a naming convention (Aharonov-Bohm/Berry), NOT an
# h/e flux quantum. This reader does not manufacture the -1; it only reads the
# sign. WHERE the -1 comes from (K4 vs SO(3)-Z2) is the whole question.
# ----------------------------------------------------------------------------
def flux_from_scalar_holonomy(sign: float) -> float:
    """Phi/Phi0 from a scalar SU(2) holonomy sign in {+1,-1}. -1 -> 1/2, +1 -> 0."""
    return 0.0 if sign > 0 else 0.5


# ============================================================================
# PART A -- the K4 disclination 2pi loop: where does pi/3 and the 1/2 come from?
# ============================================================================
def k4_disclination_flux(L: int = 8) -> dict:
    """Compute, on the REAL diamond ('K4') net, the SU(2) flux of a disclination-
    encircling loop as a function of encircle count. Reads the A4 C3 vertex rotation
    (order 3 in SO(3), order 6 in SU(2) = 2T double cover) from lattice connectivity.

    Returns the single-encircle SU(2) half-angle (pi/3 = the C3 phase -- the SAME
    number the engine FITTED as k_hopf, here FORCED by A4), and the flux after
    1/2/3/6 encircles."""
    net = build_diamond_net(L=L)
    loop = k4h.shortest_closed_loop(net, 0)
    centroid, normal, in_plane = k4h.loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    frank_perm = k4h.disclination_frank_permutation(0)
    R_c3 = k4h.rotation_from_port_permutation(frank_perm)
    q_c3 = k4h.rotation_matrix_to_quaternion(R_c3)
    su2_halfangle = float(np.arccos(np.clip(q_c3[0], -1.0, 1.0)))  # pi/3 for C3 (120deg)
    so3_angle = float(np.arccos(np.clip((np.trace(R_c3) - 1.0) / 2.0, -1.0, 1.0)))

    out = {
        "su2_halfangle_per_encircle": su2_halfangle,  # pi/3 (FORCED by A4 C3)
        "so3_angle_per_encircle": so3_angle,          # 2pi/3 = 120deg (z=3)
        "c3_order_so3": None,
    }
    Rn = np.eye(3)
    for n in range(1, 13):
        Rn = R_c3 @ Rn
        if np.allclose(Rn, np.eye(3), atol=1e-9):
            out["c3_order_so3"] = n
            break

    for n in (1, 2, 3, 6):
        h = k4h.holonomy_of_path(net, k4h.repeat_loop(loop, n), defect=defect)
        scalar = bool(h["so3_is_identity"])
        out[f"encircle{n}"] = {
            "so3_is_identity": scalar,
            "su2_sign": h["holonomy_sign"],
            "flux_over_flux0": flux_from_scalar_holonomy(h["holonomy_sign"]) if scalar else None,
            "accumulated_su2_phase": n * su2_halfangle,  # n * pi/3
        }
    out["uses_analytic_qbody"] = k4h.uses_analytic_qbody()
    return out


# ============================================================================
# PART B -- the texture flux: (p,q) psi-cycle, on K4 lattice AND continuum.
# The decisive gate: if K4 == continuum, the 1/2 is SO(3)-Z2, not K4.
# ============================================================================
def texture_flux_continuum(p: int, q: int) -> dict:
    """psi-cycle SU(2)-lift monodromy of R_z(p*phi + q*psi) in the CONTINUUM."""
    tc = texture_class(p, q)
    m_psi = tc["psi_cycle_monodromy"]  # (-1)^q
    return {
        "psi_monodromy": m_psi,
        "flux_over_flux0": flux_from_scalar_holonomy(m_psi),  # 1/2 odd, 0 even
        "su2_liftable": tc["su2_liftable"],
    }


def texture_flux_k4(p: int, q: int) -> dict:
    """psi-cycle SU(2)-lift monodromy computed with a DISCRETE K4-native walk.

    q full turns = 3*q C3 steps (C3 order 3). Continuity-track the SU(2) lift.
    If this K4-discrete monodromy EQUALS the continuum (-1)^q, the 1/2 is NOT
    K4-specific."""
    frank_perm = k4h.disclination_frank_permutation(0)
    R_c3 = k4h.rotation_from_port_permutation(frank_perm)
    q_c3 = k4h.rotation_matrix_to_quaternion(R_c3)

    n_steps = 3 * q
    q_run = k4h._IDENTITY_QUAT.copy()
    q_prev = q_run.copy()
    R_run = np.eye(3)
    for _ in range(n_steps):
        q_next = k4h.quat_mul(q_c3, q_run)
        if np.dot(q_next, q_prev) < 0.0:
            q_next = -q_next
        q_prev = q_next.copy()
        q_run = q_next
        R_run = R_c3 @ R_run
    so3_id = bool(np.allclose(R_run, np.eye(3), atol=1e-9))
    sign = float(np.sign(q_run[0])) if abs(q_run[0]) > 1e-9 else 0.0
    return {
        "psi_monodromy": sign,
        "flux_over_flux0": flux_from_scalar_holonomy(sign),
        "so3_is_identity": so3_id,
        "n_c3_steps": n_steps,
    }


# ============================================================================
# PART C -- the WELD test: is the flux threaded through the SPATIAL 2pi ROTATION
# loop texture-dependent?  (spin_loop_monodromy is the ground truth.)
# ============================================================================
def spatial_2pi_loop_flux(p: int, q: int) -> dict:
    """Flux threaded by a global 2pi SPATIAL rotation of the whole (p,q) field --
    the actual spin loop."""
    s = spin_loop_monodromy(p, q)
    return {
        "spin_monodromy_2pi": s["spin_monodromy_2pi"],
        "flux_over_flux0": flux_from_scalar_holonomy(s["spin_monodromy_2pi"]),
    }


def main() -> None:
    WINDINGS = [(2, 3), (2, 2), (1, 1), (3, 5), (1, 2)]

    print("=" * 80)
    print("HALF-FLUX / k4-flux-quantization  -- does K4 discreteness FORCE the 1/2?")
    print("=" * 80)

    print("\n[A] K4 DISCLINATION 2pi LOOP  (A4 C3 vertex rotation from lattice connectivity)")
    A = k4_disclination_flux(L=8)
    print(f"  single-encircle SO(3) angle    = {A['so3_angle_per_encircle']:.6f}  "
          f"(= 2pi/3 = 120deg ; C3 order in SO(3) = {A['c3_order_so3']}  -> z=3)")
    print(f"  single-encircle SU(2) halfangle = {A['su2_halfangle_per_encircle']:.6f}  "
          f"(pi/3 = {np.pi/3:.6f})  <-- the FITTED k_hopf, here FORCED by A4 C3")
    for n in (1, 2, 3, 6):
        e = A[f"encircle{n}"]
        print(f"  encircle x{n}: SO(3)=I? {e['so3_is_identity']!s:5}  SU(2)sign={e['su2_sign']:+.0f}  "
              f"flux/flux0={e['flux_over_flux0']}")
    print(f"  uses_analytic_qbody (must be False) = {A['uses_analytic_qbody']}")
    print("  -> half-flux(1/2) = 3 encircles x (pi/3 per encircle) = pi.  BUT this is the")
    print("     DISCLINATION/spin loop -- winding-INDEPENDENT (Part C).")

    print("\n[B] TEXTURE psi-cycle FLUX  --  K4-lattice walk  vs  continuum sigma-model")
    print(f"  {'winding':>10} | {'cont flux':>9} | {'K4 flux':>8} | {'match?':>6} | liftable")
    print("  " + "-" * 58)
    b_rows = {}
    for (p, q) in WINDINGS:
        c = texture_flux_continuum(p, q)
        k = texture_flux_k4(p, q)
        match = np.isclose(c["flux_over_flux0"], k["flux_over_flux0"])
        b_rows[(p, q)] = (c, k, match)
        print(f"  ({p},{q})      | {c['flux_over_flux0']:>9} | {k['flux_over_flux0']:>8} | "
              f"{str(match):>6} | {c['su2_liftable']}")
    all_match = all(v[2] for v in b_rows.values())
    print(f"  -> K4-walk flux == continuum flux for ALL windings?  {all_match}")
    print("     If True: the 1/2 is SO(3)-Z2 (belt trick), NOT sourced by K4 discreteness.")

    print("\n[C] WELD TEST -- flux through the SPATIAL 2pi ROTATION loop (the real spin loop)")
    print(f"  {'winding':>10} | spin-loop flux/flux0 | texture psi-flux/flux0")
    print("  " + "-" * 50)
    for (p, q) in WINDINGS:
        sp = spatial_2pi_loop_flux(p, q)
        tex = b_rows[(p, q)][0]["flux_over_flux0"]
        print(f"  ({p},{q})      | {sp['flux_over_flux0']:>18} | {tex:>18}")
    print("  -> spatial spin-loop flux is 1/2 for EVERY winding (winding-INDEPENDENT).")
    print("     texture psi-flux is q-keyed but lives on a DIFFERENT loop; no weld.")

    print("\n" + "=" * 80)
    print("VERDICT: [HALF-FLUX-ECHO] -- the q-keyed 1/2 is SO(3)-Z2 (K4==continuum),")
    print("the spin loop is winding-independent, no K4 term welds the two.")
    print("=" * 80)


if __name__ == "__main__":
    main()
