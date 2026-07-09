"""Analytical topology: π₁ of the electron (2,3) soliton's configuration space
from the substrate's OWN SO(3) Cosserat order parameter — settling ℤ₂-vs-ℤ₃ and
the forced-vs-admitted spin-½ SELECTION question.

Prereg: research/2026-07-08_electron-pi1-spinhalf_prereg.md
Result: research/2026-07-08_electron-pi1-spinhalf_result.md

★ HARD ANTI-TAUTOLOGY RULE (load-bearing — the whole game):
The half-angle spinor lift U = exp(iσ·ω/2) is FORBIDDEN on the π₁ path. Any ℤ₂
that appears MUST trace to SO(3)'s OWN intrinsic π₁ (the belt trick / RP³), never
to an inserted spinor. This module therefore NEVER supplies cos(φ/2) as an INPUT.
Every rotation is built as an SO(3) MATRIX from the FULL angle (cos θ, sin θ); the
SU(2) double-cover sign is read by the Shepperd matrix→quaternion map
(`k4_lattice_holonomy.rotation_matrix_to_quaternion`) and resolved by CONTINUITY
along the path. The −I emerges from the SO(3) loop's own non-contractibility, not
from a half-angle convention. (Same discipline as
`src/ave/topological/k4_lattice_holonomy.py:8-11,92,136`.)

WHAT THIS COMPUTES (dimensionless homotopy — no α, no m_e, no CODATA):
  1. π₁(SO(3)) = ℤ₂ demonstrated by the continuity-tracked lift monodromy of the
     SO(3) loop R_z(θ): 2π ↦ −I, 4π ↦ +I.  (belt trick, intrinsic)
  2. π₁(Q) of the SO(3)-field configuration space, via the free-loop-space
     splitting of the topological group SO(3), for both modeling domains:
       Domain-A (real-space S³):  π₁ = π₁(SO(3)) ⊕ π₄(SO(3)) = ℤ₂ ⊕ ℤ₂
       Domain-B (phase-space T²): π₁ = ℤ₂ ⊕ ℤ   (ℤ₂ from π₁(SO(3)); ℤ from π₃(SO(3)))
     The 2π-rotation loop is the π₁(SO(3)) = ℤ₂ factor in BOTH.
  3. SELECTION: the class of the 2π global-rotation loop is WINDING-INDEPENDENT
     (−I for every (p,q)); the (2,3) parity does NOT change it. The character set
     Hom(ℤ₂,U(1)) has TWO elements ⇒ boson AND fermion quantizations both admitted.
  4. TEXTURE class (distinct from spin): the (p,q) winding parities give the
     [T²,SO(3)] component (p mod 2, q mod 2); the ODD q=3 cycle is NON-liftable to
     SU(2). This is the field's own ℤ₂ charge — winding-parity-dependent — but it
     is NOT the spin-under-rotation loop.
  5. ℤ₃ reconciliation: the lens space L(3,1) (double BRANCHED cover of S³ along the
     (2,3) trefoil, |Δ_trefoil(−1)| = 3) is a DIFFERENT space measuring the knot's
     ambient embedding, NOT the field configuration space. Spin is governed by ℤ₂.

VERDICT: [SPIN-HALF-POSITED] — ℤ₂ is real and lift-free (belt trick), spin-½ is
ADMITTED/representable, but SELECTION into the fermion sector is NOT forced by the
(2,3) winding parity; it requires an action-level ℤ₂ term (Wess-Zumino / θ) that the
corpus imports via exp(iσ·ω/2). Confirms the audit (clm-rkisb8 rationale).
"""

from __future__ import annotations

import numpy as np
import sympy as sp

# Reuse the EXISTING anti-tautology lift: matrix→quaternion (Shepperd), NOT an
# analytic cos(φ/2) rotor. Importing it inherits that module's guard.
from ave.topological.k4_lattice_holonomy import rotation_matrix_to_quaternion


# ─────────────────────────────────────────────────────────────────────────────
# SO(3) rotation MATRICES from the FULL angle (never a half-angle input).
# ─────────────────────────────────────────────────────────────────────────────
def rot_z(theta: float) -> np.ndarray:
    """SO(3) rotation by the FULL angle θ about ẑ. Uses cos θ, sin θ — NOT cos(θ/2).

    This is the substrate's own micro-rotation frame R(ω) ∈ SO(3) for ω = θ ẑ
    (Rodrigues image; cf. cosserat_field_3d.py:91-119). No spinor, no half-angle.
    """
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def loop_lift_monodromy(matrices: list[np.ndarray]) -> float:
    """Continuity-tracked SU(2)-lift monodromy of a CLOSED loop of SO(3) matrices.

    `matrices[0]` and `matrices[-1]` are the same rotation (the loop closes in
    SO(3)). Each matrix is lifted to a unit quaternion by the Shepperd map; the
    double-cover sign is fixed by CONTINUITY (pick the representative nearest the
    previous one). The returned monodromy = ⟨q_end, q_start⟩ ∈ {+1, −1}:
      +1  ⇒  the lift closed  (+I)  — loop contractible in SO(3)
      −1  ⇒  the lift flipped (−I)  — loop is the non-trivial π₁(SO(3)) element

    The −I is therefore a property of the SO(3) loop's non-contractibility (the
    belt trick), read off the matrices — NOT inserted via cos(φ/2).
    """
    q_start = rotation_matrix_to_quaternion(matrices[0])
    q_prev = q_start.copy()
    for R in matrices[1:]:
        q = rotation_matrix_to_quaternion(R)
        if np.dot(q, q_prev) < 0.0:
            q = -q
        q_prev = q
    return float(np.dot(q_prev, q_start))


# ─────────────────────────────────────────────────────────────────────────────
# (1) π₁(SO(3)) = ℤ₂ — intrinsic, lift-free.
# ─────────────────────────────────────────────────────────────────────────────
def pi1_so3_monodromy(n: int = 20000) -> dict[str, float]:
    """Belt trick: 2π SO(3) loop ↦ −I, 4π ↦ +I. Demonstrates π₁(SO(3)) = ℤ₂."""
    loop_2pi = [rot_z(t) for t in np.linspace(0.0, 2.0 * np.pi, n)]
    loop_4pi = [rot_z(t) for t in np.linspace(0.0, 4.0 * np.pi, n)]
    return {
        "monodromy_2pi": loop_lift_monodromy(loop_2pi),  # −1
        "monodromy_4pi": loop_lift_monodromy(loop_4pi),  # +1
    }


# ─────────────────────────────────────────────────────────────────────────────
# (3) SELECTION — the 2π global-rotation loop class is winding-INDEPENDENT.
# ─────────────────────────────────────────────────────────────────────────────
def spin_loop_monodromy(p: int, q: int, n: int = 20000) -> dict[str, float]:
    """Monodromy of a global 2π (and 4π) rigid frame-rotation applied to the whole
    (p,q) field. The loop is t ↦ R_z(2πt)·R0, where R0 is the field frame at an
    arbitrary base point. Returns −1 (2π) / +1 (4π) for ANY (p,q) — the spin sign
    does NOT depend on the winding parity."""
    phi, psi = 0.7, 1.9  # arbitrary base point on T²
    r0 = rot_z(p * phi + q * psi)
    loop_2pi = [rot_z(2.0 * np.pi * t) @ r0 for t in np.linspace(0.0, 1.0, n)]
    loop_4pi = [rot_z(4.0 * np.pi * t) @ r0 for t in np.linspace(0.0, 1.0, n)]
    return {
        "spin_monodromy_2pi": loop_lift_monodromy(loop_2pi),  # −1 ∀ (p,q)
        "spin_monodromy_4pi": loop_lift_monodromy(loop_4pi),  # +1 ∀ (p,q)
    }


def character_set_z2() -> list[int]:
    """Hom(ℤ₂, U(1)): the two 1-dim reps of the spin factor π₁ = ℤ₂ = {1, τ}.
    χ(τ) = +1 (boson/integer) and χ(τ) = −1 (fermion/spin-½). |Hom| = 2 ⇒ both
    quantizations are topologically ADMITTED; π₁ alone does not FORCE either."""
    return [+1, -1]


# ─────────────────────────────────────────────────────────────────────────────
# (4) TEXTURE class — winding-parity dependent, but NOT the spin loop.
# ─────────────────────────────────────────────────────────────────────────────
def texture_class(p: int, q: int, n: int = 20000) -> dict[str, object]:
    """Monodromy of the lift AROUND each field cycle of R(φ,ψ) = R_z(pφ + qψ).
    φ-cycle ↦ (−1)^p, ψ-cycle ↦ (−1)^q. The [T²,SO(3)] component is (p mod 2,
    q mod 2). Non-zero ⇒ the SO(3) field does NOT lift globally to SU(2). For (2,3)
    the class is (0,1): the ODD q=3 cycle is the non-liftable one."""
    phi_cycle = [rot_z(p * a) for a in np.linspace(0.0, 2.0 * np.pi, n)]
    psi_cycle = [rot_z(q * a) for a in np.linspace(0.0, 2.0 * np.pi, n)]
    m_phi = loop_lift_monodromy(phi_cycle)
    m_psi = loop_lift_monodromy(psi_cycle)
    return {
        "phi_cycle_monodromy": m_phi,  # (−1)^p
        "psi_cycle_monodromy": m_psi,  # (−1)^q
        "H1_class_mod2": (p % 2, q % 2),
        "su2_liftable": (p % 2 == 0 and q % 2 == 0),
    }


# ─────────────────────────────────────────────────────────────────────────────
# (5) ℤ₃ reconciliation — L(3,1) is the branched cover of AMBIENT space, not Q.
# ─────────────────────────────────────────────────────────────────────────────
def z3_branched_cover_order(p: int = 2, q: int = 3) -> dict[str, int]:
    """|H₁(double branched cover of S³ along the (p,q) torus knot)| = |Δ(−1)|,
    Δ = Alexander polynomial. For the (2,3) trefoil Δ(t) = t²−t+1, Δ(−1) = 3, so the
    branched cover is the lens space L(3,1) with π₁ = ℤ₃ (matches doc36:49). This is
    a property of the KNOT's embedding in ambient S³, NOT the field configuration
    space Q — hence it governs the knot's monodromy, not the soliton's spin."""
    t = sp.symbols("t")
    if (p, q) == (2, 3):
        alexander = t**2 - t + 1
    else:  # general (2, n) torus knot Alexander polynomial (2-bridge)
        alexander = sum((-1) ** k * t**k for k in range(q))
    det_h1 = int(abs(sp.simplify(alexander.subs(t, -1))))
    return {"alexander_at_minus1": det_h1, "pi1_branched_cover_order": det_h1}


def _report() -> dict[str, object]:
    out: dict[str, object] = {}
    out["pi1_so3"] = pi1_so3_monodromy()
    out["spin_23"] = spin_loop_monodromy(2, 3)
    out["spin_controls"] = {f"{p}{q}": spin_loop_monodromy(p, q) for (p, q) in [(2, 2), (1, 1), (3, 5)]}
    out["characters"] = character_set_z2()
    out["texture_23"] = texture_class(2, 3)
    out["texture_controls"] = {f"{p}{q}": texture_class(p, q) for (p, q) in [(2, 2), (1, 1)]}
    out["z3"] = z3_branched_cover_order(2, 3)
    return out


if __name__ == "__main__":
    r = _report()
    print("=" * 74)
    print("ELECTRON π₁ / SPIN-½ SELECTION — analytical topology (no half-angle lift)")
    print("=" * 74)
    print("\n(1) π₁(SO(3)) = ℤ₂  [belt trick, continuity-tracked Shepperd lift, no cos(φ/2) input]")
    print(f"    2π SO(3) loop → monodromy {r['pi1_so3']['monodromy_2pi']:+.3f}  (−I: non-contractible)")
    print(f"    4π SO(3) loop → monodromy {r['pi1_so3']['monodromy_4pi']:+.3f}  (+I: contractible)")
    print("\n(2) π₁(Q) via free-loop-space splitting of the topological group SO(3):")
    print("    Domain-A (real-space S³):  π₁ = π₁(SO(3)) ⊕ π₄(SO(3)) = ℤ₂ ⊕ ℤ₂")
    print("    Domain-B (phase-space T²): π₁ = ℤ₂ ⊕ ℤ  [ℤ₂ = π₁(SO(3)); ℤ = π₃(SO(3))]")
    print("    → the 2π-rotation (spin) loop = the π₁(SO(3)) = ℤ₂ factor in BOTH.")
    print("\n(3) SELECTION — global 2π rotation loop is WINDING-INDEPENDENT:")
    print(
        f"    (2,3): spin monodromy 2π = {r['spin_23']['spin_monodromy_2pi']:+.3f}, "
        f"4π = {r['spin_23']['spin_monodromy_4pi']:+.3f}"
    )
    for k, v in r["spin_controls"].items():
        print(
            f"    ({k[0]},{k[1]}): spin monodromy 2π = {v['spin_monodromy_2pi']:+.3f}, "
            f"4π = {v['spin_monodromy_4pi']:+.3f}"
        )
    print(f"    Hom(ℤ₂,U(1)) = {r['characters']}  → |Hom| = 2 ⇒ BOTH boson & fermion admitted; π₁ does NOT force.")
    print("\n(4) TEXTURE class (field's own ℤ₂ charge — winding-parity dependent, ≠ spin):")
    t23 = r["texture_23"]
    print(
        f"    (2,3): φ-cycle {t23['phi_cycle_monodromy']:+.2f} [(−1)^2]  "
        f"ψ-cycle {t23['psi_cycle_monodromy']:+.2f} [(−1)^3]  "
        f"→ [T²,SO(3)] class {t23['H1_class_mod2']}  SU(2)-liftable={t23['su2_liftable']}"
    )
    for k, v in r["texture_controls"].items():
        print(f"    ({k[0]},{k[1]}): class {v['H1_class_mod2']}  SU(2)-liftable={v['su2_liftable']}")
    print("\n(5) ℤ₃ reconciliation — L(3,1) = branched cover of AMBIENT S³ along the trefoil:")
    print(
        f"    |Δ_trefoil(−1)| = {r['z3']['alexander_at_minus1']} ⇒ π₁(L(3,1)) = "
        f"ℤ_{r['z3']['pi1_branched_cover_order']}  (a DIFFERENT space from Q; governs the knot, not spin)"
    )
    print("\n" + "=" * 74)
    print("VERDICT: [SPIN-HALF-POSITED] — ℤ₂ real & lift-free; spin-½ ADMITTED/representable;")
    print("SELECTION into the fermion sector NOT forced by the (2,3) winding parity.")
    print("=" * 74)
