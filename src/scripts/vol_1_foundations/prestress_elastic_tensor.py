#!/usr/bin/env python3
"""The PRE-STRESSED srs ELASTIC-TENSOR arc — small-signal C_ij about a PRE-STRESSED DC Q-point.

[SAME-TENSOR-POINT] beyond-model TEST 1 of 2 — the initial/residual PRE-STRESS contribution.
Geometry-change (test 2) is HELD FIXED here (out of scope, the follow-on arc).

Prereg (FROZEN): research/2026-07-04_prestress-tensor_prereg_FROZEN.md (committed 6dba078e).

SKELETON — sections filled one commit at a time (incremental-write discipline).

═══════════════════════════════════════════════════════════════════════════════
THE SEAM THIS OPENS  (PR #521 § MODEL SCOPE, verbatim)
═══════════════════════════════════════════════════════════════════════════════
#521 closed [SAME-TENSOR-POINT] MODEL-BOUNDED: the saturated small-signal tensor is the cold tensor
at rho_eff, because Born-Huang (k_a,k_s)->C_ij is homogeneous degree-1 (overall S cancels in ratios).
Its MODEL SCOPE names two OMITTED, OPEN contributions a real DC-biased lattice carries:
  (a) initial/residual PRE-STRESS (bias pre-loads the bonds -> nonzero reference stress);
  (b) bias-induced GEOMETRY change (node/bond relaxation off the cold geometry).
THIS DRIVER computes (a) ONLY, at FIXED geometry. (b) is test 2 of 2.

The pre-stress term is NOT spring-softening: it adds a NEW transverse "string-tension" force constant
(T/l)(I - d^d^) per bond, T=Phi'(A) the integrated bond tension. That term does NOT scale as the
overall S factor, so it CAN break the degree-1 homogeneity that made #521 hold. That is why the test
is informative.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (see prereg §1 — stated before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : translational-u (Cauchy) sector of chiral srs-z3, PRE-STRESSED bond tensor.
           BOTH k_a, k_s are translational-u/CAPACITIVE (518 verbatim). Cosserat = STAGE 2.
  MODE   : SMALL-SIGNAL long-wave about a PRE-STRESSED DC Q-point (reference bond tension
           T=Phi'(A) != 0; cold ref had Phi'(0)=0 -- the separating axis from #521).
  REGIME : quasi-static about a STATIC DC bias. Op14 ON. PHASE-STATE = saturated S<1 WITH bias tension.
  DC/AC  : A is a STATIC DC bias (R2 varactor, node-up:118,:40,:145) -> NO <sin^2>=1/2 factor;
           reference tension = Phi'(A) at the static bias, factor 1 (derived, not hand-set).
  COORDS : operating-point knob (A_axial,A_shear) phase-space/reactance; tensor readout real-space.
           A46-clean on both.
  CLASS  : CONSISTENCY/MANIFESTATION. nu/Zener/(K/G) ratios (alpha-clean). EMERGENCE FORBIDDEN for
           any value: 2/7, 9.7734, 0.99479 are ALL visible targets -- NO tuning toward any.

THE DERIVED TENSION (prereg §2, sympy-verified):
  Phi''(a) = k0*S(a) = k0*sqrt(1-a^2)   (Ax4 kernel AS DIFFERENTIAL STIFFNESS)
  T(A) = Phi'(A) = INT_0^A k0*sqrt(1-a^2) da = k0*( A*sqrt(1-A^2) + arcsin A ) / 2,  Phi'(0)=0.
  Phi'(A) -> k0*pi/4 as A->1 (FINITE tension at the yield wall; tangent stiffness -> 0).

THE INITIAL-STRESS FORM (prereg §3, Born-Huang/Wallace, validated PC2):
  Phi_bond = Phi''*(d^d^) + (T/l)*(I - d^d^),  l = per-bond |d| (read from geometry).
  The (T/l)(I-d^d^) transverse "string tension" term IS the pre-stress physics at lattice level.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/prestress_elastic_tensor.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# REUSE the cold arc's PROVEN Born-Huang extraction pieces unmodified where possible
# (identical pipeline is what licenses the pre-stressed number).
from scripts.vol_1_foundations.srs_elastic_tensor import (  # noqa: E402
    _cubic_gamma_row,
    moduli_from_Cij,
    simple_cubic_ref,
    srs_primitive,
)

from ave.axioms.scale_invariant import saturation_factor  # noqa: E402
from ave.core.constants import ALPHA, NU_VAC  # noqa: E402


# ---------------------------------------------------------------------------
# CANON ANCHORS (imported / read-off -- NOT tuned)
# ---------------------------------------------------------------------------
RHO_COLD = 1.0
RHO_STAR_IMPORTED = 9.7734          # cold nu=2/7 <=> K=2G locus, GR-imported (read-off only)
NU_2_7 = float(NU_VAC)              # the visible-target Poisson ratio (= 2/7)
A_CORE_SQRT_ALPHA = float(np.sqrt(ALPHA))   # A1 mass-core operating point (def-vyvsn1)
A_WALL_518_CROSSING = 0.99479       # #518 shear-loads crossing amplitude (VISIBLE TARGET, read-off)


# ===========================================================================
# THE DERIVED BOND TENSION (prereg §2) -- Phi'(A), sympy-verified
# ===========================================================================
def bond_tension(A: float | np.ndarray, k0: float = 1.0) -> np.ndarray:
    """Integrated bond tension T(A)=Phi'(A)=k0*(A*sqrt(1-A^2)+arcsin A)/2, Phi'(0)=0.

    From Phi''(a)=k0*sqrt(1-a^2) (Ax4 kernel as DIFFERENTIAL stiffness) by direct integration
    (prereg §2, symbolically verified). No hand-set factor; the DC-bias convention (node-up:118)
    sets the time-average factor to 1. Phi'(A)->k0*pi/4 as A->1 (finite tension at yield).
    """
    Aa = np.asarray(A, dtype=float)
    # arcsin domain guard (A in [0,1]); the sweep never exceeds 1 (sub-yield to the wall)
    Aa = np.clip(Aa, 0.0, 1.0)
    return k0 * (Aa * np.sqrt(np.clip(1.0 - Aa ** 2, 0.0, 1.0)) + np.arcsin(Aa)) / 2.0


# ===========================================================================
# PLACEHOLDERS -- filled in subsequent commits (incremental-write discipline)
# ===========================================================================
# ===========================================================================
# THE PRE-STRESSED FORCE-CONSTANT MATRIX (prereg §3) -- adds (T/l)(I-P) per bond
# ===========================================================================
def _prestress_phi_of_k(kv, pos, bonds, k_axial, k_shear, T_per_bond):
    """Force-constant Bloch matrix Phi(k) with the INITIAL-STRESS transverse term.

    Each directed bond (i,j,d) of length l=|d| carries (prereg §3, Born-Huang/Wallace):
        Phi_bond = Phi''*(d^d^)  +  (k_shear + T/l)*(I - d^d^)
    where Phi'' = k_axial is the axial (swapped-spring softened) stiffness and (T/l) is the
    ADDED transverse string-tension term (T = this bond's own axial-channel tension Phi'(A_axial)).
    The pre-stress term is ADDITIVE to the transverse block; it is NOT an overall scale, so it
    can break the #521 degree-1 homogeneity. T_per_bond is a dict {bond_index: T} or a scalar T
    applied to every bond (the uniform-loading convention, #518).
    """
    n = len(pos)
    D = np.zeros((3 * n, 3 * n), dtype=complex)
    for bidx, (i, j, d) in enumerate(bonds):
        ell = np.linalg.norm(d)
        dn = d / ell
        P = np.outer(dn, dn)
        T = T_per_bond[bidx] if hasattr(T_per_bond, "__getitem__") and not np.isscalar(T_per_bond) else float(T_per_bond)
        k_shear_eff = k_shear + T / ell          # <-- the pre-stress addition to the transverse block
        Phi = k_axial * P + k_shear_eff * (np.eye(3) - P)
        ph = np.exp(1j * np.dot(kv, d))
        D[3 * i:3 * i + 3, 3 * j:3 * j + 3] += -Phi * ph
        D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += Phi
    return 0.5 * (D + D.conj().T)


def prestress_christoffel(qhat, pos, bonds, *, k_axial=1.0, k_shear=1.0, T_per_bond=0.0,
                          rho=1.0, m=1.0, h=1e-4):
    """Internal-strain-RELAXED 3x3 acoustic Christoffel Gamma(q^)=rho*c^2 WITH the pre-stress term.

    Identical Born-Huang method-of-long-waves as the cold acoustic_christoffel (Gamma = Phi2_aa -
    Phi1_ao.Phi0_oo^-1.Phi1_oa), but on the PRE-STRESSED Phi(k) (transverse block gains (T/l)).
    Reduces EXACTLY to the cold acoustic_christoffel when T_per_bond=0 (PC1/PC3 gate this).
    """
    qhat = np.asarray(qhat, float)
    qhat = qhat / np.linalg.norm(qhat)
    n = len(pos)

    def phi(kv):
        return _prestress_phi_of_k(kv, pos, bonds, k_axial, k_shear, T_per_bond)

    P0 = phi(np.zeros(3))
    Pp = phi(qhat * h)
    Pm = phi(-qhat * h)
    P1 = (Pp - Pm) / (2.0 * h)
    P2 = (Pp - 2.0 * P0 + Pm) / (h ** 2) / 2.0

    Ea = np.zeros((3 * n, 3), dtype=complex)
    for al in range(3):
        v = np.zeros(3 * n)
        v[al::3] = 1.0
        v /= np.linalg.norm(v)
        Ea[:, al] = v
    w0, U0 = np.linalg.eigh(P0)
    optic = U0[:, w0 > 1e-9]

    Paa = Ea.conj().T @ P2 @ Ea
    P1ao = Ea.conj().T @ P1 @ optic
    P0oo = optic.conj().T @ P0 @ optic
    P1oa = optic.conj().T @ P1 @ Ea
    Gamma = Paa - P1ao @ np.linalg.inv(P0oo) @ P1oa
    Gamma = 0.5 * (Gamma + Gamma.conj().T)
    return (rho / m) * Gamma.real


def extract_prestress_Cij(pos, bonds, *, k_axial=1.0, k_shear=1.0, T_per_bond=0.0,
                          m=1.0, rho=1.0, directions=None):
    """Fit cubic (C11,C12,C44) on the PRE-STRESSED internal-strain-relaxed acoustic tensor.

    Same polarization-free least-squares assembly as the cold extract_cubic_Cij (_cubic_gamma_row
    reused unmodified), over the same over-determined direction set. The ONLY change vs the cold
    pipeline is the pre-stress transverse term inside prestress_christoffel. Also returns the
    smallest acoustic eigenvalue min over directions (the [DESTABILIZED] readout: an acoustic
    Christoffel eigenvalue going <=0 = a lost sound mode).
    """
    if directions is None:
        directions = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1],
                      [0, 1, 1], [1, 1, 1], [2, 1, 0], [1, 2, 0], [3, 1, 2]]
    A, b = [], []
    slope_table = {}
    min_acoustic_eig = np.inf
    for dd in directions:
        q = np.array(dd, float)
        q /= np.linalg.norm(q)
        G = prestress_christoffel(q, pos, bonds, k_axial=k_axial, k_shear=k_shear,
                                  T_per_bond=T_per_bond, m=m, rho=rho)
        eigs = np.sort(np.linalg.eigvalsh(G))
        min_acoustic_eig = min(min_acoustic_eig, float(eigs[0]))
        key = "".join(str(int(x)) for x in dd)
        slope_table[key] = {"rho_c2_eigs_ascending": eigs.tolist()}
        for i in range(3):
            for jl in range(i, 3):
                A.append(_cubic_gamma_row(q, i, jl))
                b.append(G[i, jl])
    A = np.array(A, float)
    b = np.array(b, float)
    x, _res, *_ = np.linalg.lstsq(A, b, rcond=None)
    fit = A @ x
    resid_rel = float(np.max(np.abs(fit - b)) / (np.max(np.abs(b)) + 1e-30))
    C11, C12, C44 = (float(v) for v in x)
    return {
        "C11": C11, "C12": C12, "C44": C44,
        "max_rel_residual": resid_rel,
        "min_acoustic_eig": min_acoustic_eig,
        "slope_table": slope_table,
    }


# ===========================================================================
# POSITIVE CONTROLS (prereg §4) -- HALT-gated, run BEFORE any adjudicated number
# ===========================================================================
def run_positive_controls(pos, bonds, rho) -> dict:
    """PC1 zero-bias recovery + PC2 analytic stressed-lattice limit + PC3 homogeneity re-check.

    All against full-precision references on the SAME pipeline (never rounded literals).
    """
    from scripts.vol_1_foundations.srs_elastic_tensor import extract_cubic_Cij

    val = {}

    # --- PC1: zero-bias recovery. A=0 => T=Phi'(0)=0 => (T/l) term vanishes => the pre-stress
    #     driver with tension OFF IS the cold/#521 driver. Must match to machine precision (1e-9). --
    cold_ref = extract_cubic_Cij(pos, bonds, k_axial=RHO_STAR_IMPORTED, k_shear=1.0, rho=rho)
    pre0 = extract_prestress_Cij(pos, bonds, k_axial=RHO_STAR_IMPORTED, k_shear=1.0,
                                 T_per_bond=0.0, rho=rho)
    pc1_err = max(abs(cold_ref[k] - pre0[k]) / (abs(cold_ref[k]) + 1e-30) for k in ("C11", "C12", "C44"))
    pc1_ok = bool(pc1_err < 1e-9 and abs(bond_tension(0.0)) < 1e-15)
    val["PC1_zero_bias_recovery"] = {
        "T_at_A0": float(bond_tension(0.0)),
        "max_rel_err_vs_cold_same_pipeline": pc1_err,
        "gated_rel_tol": 1e-9,
        "note": "A=0 => T=Phi'(0)=0 => (T/l)(I-P) vanishes => pre-stress tensor == cold tensor "
        "at rho=9.7734 to MACHINE PRECISION. Full-precision cold ref on the SAME pipeline "
        "(NOT the rounded literal). This is the identity control.",
        "PASS": pc1_ok,
    }

    # --- PC2: analytic stressed-lattice limit. Uniformly-tensioned SIMPLE CUBIC: the transverse
    #     (shear) branch gains C44 = k_shear + T/l EXACTLY (string-tension term adds to the
    #     transverse force constant along a cubic axis; no cross-coupling by cubic symmetry).
    #     Gate: extracted (C44_stressed - C44_unstressed) == T/l to numerical tolerance. This
    #     validates the (T/l)(I-d^d^) FORM on a lattice where the answer is closed-form. ------------
    pos_sc, bonds_sc, rho_sc = simple_cubic_ref()  # 6 axial bonds, ell=1
    ka_sc, ks_sc = 1.0, 0.4
    pc2_cases = []
    pc2_ok = True
    for T in (0.0, 0.15, 0.3):
        r_un = extract_prestress_Cij(pos_sc, bonds_sc, k_axial=ka_sc, k_shear=ks_sc,
                                     T_per_bond=0.0, rho=rho_sc)
        r_st = extract_prestress_Cij(pos_sc, bonds_sc, k_axial=ka_sc, k_shear=ks_sc,
                                     T_per_bond=T, rho=rho_sc)
        ell = 1.0  # simple-cubic bond length in pipeline units
        c44_shift = r_st["C44"] - r_un["C44"]
        predicted = T / ell
        err = abs(c44_shift - predicted)
        ok = bool(err < 1e-6 and r_st["max_rel_residual"] < 1e-3)
        pc2_ok = pc2_ok and ok
        pc2_cases.append({
            "T": T, "T_over_ell": predicted, "C44_shift_measured": c44_shift,
            "abs_err": err, "max_rel_residual": r_st["max_rel_residual"], "PASS": ok,
        })
    val["PC2_analytic_stressed_lattice"] = {
        "cases": pc2_cases,
        "note": "uniformly-tensioned simple-cubic: transverse acoustic speed shift is analytic, "
        "C44_stressed - C44_unstressed = T/l EXACTLY (string-tension adds to the transverse force "
        "constant). Validates the (T/l)(I-d^d^) initial-stress FORM on a KNOWN case BEFORE srs.",
        "PASS": pc2_ok,
    }

    # --- PC3: homogeneity re-check (the #521 VS2) with T=0. Confirms the pipeline still gives the
    #     #521 degree-1 homogeneity when tension is off => any homogeneity BREAK with T!=0 is
    #     attributable to the pre-stress term, not a pipeline change. -----------------------------
    ka, ks = 9.7734, 1.0
    r_base = extract_prestress_Cij(pos, bonds, k_axial=ka, k_shear=ks, T_per_bond=0.0, rho=rho)
    m_base = moduli_from_Cij(r_base["C11"], r_base["C12"], r_base["C44"])
    lam = 0.37
    r_scl = extract_prestress_Cij(pos, bonds, k_axial=lam * ka, k_shear=lam * ks,
                                  T_per_bond=0.0, rho=rho)
    m_scl = moduli_from_Cij(r_scl["C11"], r_scl["C12"], r_scl["C44"])
    cij_homog_err = max(abs(r_base[k] - r_scl[k] / lam) / (abs(r_base[k]) + 1e-30)
                        for k in ("C11", "C12", "C44"))
    ratio_inv_err = max(abs(m_base[k] - m_scl[k]) / (abs(m_base[k]) + 1e-30)
                        for k in ("nu_Hill", "Zener_A", "KG_Hill"))
    pc3_ok = bool(cij_homog_err < 1e-7 and ratio_inv_err < 1e-7)
    val["PC3_homogeneity_T0"] = {
        "lam": lam, "cij_over_lam_rel_err": cij_homog_err, "ratio_invariance_rel_err": ratio_inv_err,
        "note": "the #521 VS2 degree-1 homogeneity re-run WITH pre-stress OFF (T=0). Passing here "
        "means any homogeneity break seen with T!=0 is the pre-stress term, not a pipeline change.",
        "PASS": pc3_ok,
    }

    val["ALL_PASS"] = bool(pc1_ok and pc2_ok and pc3_ok)
    return val


# ===========================================================================
# THE GEOMETRY-COUPLED DISCRIMINATOR (prereg §6 branch ii, §9)
# ===========================================================================
def residual_node_forces(pos, bonds, T_per_bond) -> dict:
    """Net force at each node from the bias bond tensions T, at the COLD (unrelaxed) geometry.

    Reading A (prereg §9): srs site symmetry makes the vector sum of bond tensions at each node
    ZERO at cold geometry => the pre-stress is a genuine fixed-geometry state => the small-signal
    tensor about it is well-defined. Reading B: a nonzero residual node force appears => the
    "pre-stressed at fixed geometry" state is NOT a mechanical equilibrium => [GEOMETRY-COUPLED]
    (tests 1 and 2 inseparable).

    A central-bond tension T along d^ pulls node i toward node j with force +T*d^ (and -T*d^ on i
    from the reverse). We sum the tension force contributions at each node over its bonds and report
    the max |net force|. The directed-bond list contains BOTH (i,j,d) and (j,i,-d), so a
    self-balanced site has the two contributions cancel.
    """
    n = len(pos)
    Fnet = np.zeros((n, 3))
    for bidx, (i, j, d) in enumerate(bonds):
        ell = np.linalg.norm(d)
        dn = d / ell
        T = T_per_bond[bidx] if hasattr(T_per_bond, "__getitem__") and not np.isscalar(T_per_bond) else float(T_per_bond)
        # tension pulls node i toward node j (along +d^): force on i is +T*d^
        Fnet[i] += T * dn
    per_node = np.linalg.norm(Fnet, axis=1)
    max_res = float(np.max(per_node))
    total_scale = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds])) * (
        float(np.max([abs(T_per_bond[b]) if (hasattr(T_per_bond, "__getitem__") and not np.isscalar(T_per_bond)) else abs(float(T_per_bond))
                      for b in range(len(bonds))])) + 1e-30)
    return {
        "max_residual_node_force": max_res,
        "per_node_residual": per_node.tolist(),
        "tension_scale": total_scale,
        "relative_residual": max_res / (total_scale + 1e-30),
    }


def run_sweep(*args, **kwargs):  # noqa: D401
    """[filled next commit] both channel assignments, full A_wall ladder, Delta-nu map readout."""
    raise NotImplementedError


def main():  # noqa: D401
    """[filled last commit] validate-on-known HALT gate, residual-force check, sweep, bin verdict."""
    print("SKELETON -- sections fill in subsequent commits.")


if __name__ == "__main__":
    main()
