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

The pre-stress adds a transverse "string-tension" force constant (T/l)(I - d^d^) per bond,
T=Phi'(A) the integrated bond tension.

  *** MECHANISM CORRECTION (2026-07-04, orchestrator 16-agent review, PR #526 fix round) ***
  The FIRST framing said "(T/l)(I-P) breaks the degree-1 homogeneity, the tensor leaves the cold
  family." That is FALSE (verifier-proved bit-exact). The (T/l)(I-P) term has the SAME PROJECTOR
  STRUCTURE as the shear spring k_s*(I-P), so the pre-stressed force-constant matrix is EXACTLY the
  COLD matrix with a SHIFTED SHEAR SPRING k_s -> k_s + T/l. On the srs net (uniform bond length l=1)
  a single scalar shift works. Verified: extract_prestress_Cij(k_a,k_s,T) == extract_cubic_Cij(k_a,
  k_s+T/l) to <=8e-16 at every probe point, both assignments (VS4 gate). The Born-Huang degree-1
  HOMOGENEITY IS INTACT; the tensor NEVER leaves the cold one-parameter family.
  WHAT BREAKS is ONLY #521's DICTIONARY rho_eff = S_ax/S_shear. The true family coordinate is
    rho' = S_ax / (S_shear + T/l),
  monotone in the swept channel and CAPPED: as A_wall->1 (S_shear->0) rho' -> rho'_max = S_ax*l/T,
  FINITE -- the yield wall no longer sends the coordinate to infinity. So the honest statement is:
  FAMILY SURVIVES, DICTIONARY BREAKS, COORDINATE CAPPED. The bin verdict [MAP-DEFORMED] is EARNED
  (the #521 map ties nu to S_ax/S_shear, and THAT tie breaks), but the physical narrative is the
  remap, not a new tensor family or new instability.

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
    extract_cubic_Cij,
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
        "DISCLOSURE_item_5b": "PC2 runs ONLY at l=1 (simple-cubic unit spacing), where all powers of "
        "l degenerate -- so PC2 validates the T/l FORM but does NOT independently pin the l-POWER "
        "(l^1 vs l^0 etc.). The srs bond length is ALSO l=1 (uniform), so the l-power does not affect "
        "THIS result's numbers; but a lattice with l!=1 bonds would need a separate l-power check. "
        "The l^1 (T/l) power is the standard string-tension form (Born-Huang/Wallace); disclosed, "
        "not independently validated by PC2.",
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

    # --- VS4 (added 2026-07-04, orchestrator fix round): EXACT-COLLAPSE. The load-bearing mechanism
    #     fact -- prestress(k_a, k_s, T) == cold(k_a, k_s + T/l) bit-exactly, because (T/l)(I-P) has
    #     the SAME PROJECTOR STRUCTURE as the shear spring k_s(I-P). This is what proves the tensor
    #     never leaves the cold one-parameter family (the corrected mechanism). srs bond length is
    #     uniform (l=1), so a single scalar shift works. HALT-gate.
    #     RETROFIT (reconcile-gate helper, follow-on flagged in the #527 fix round): the comparison
    #     now runs through ave.validation.ReconcileGate. claimed = the prestressed tensor
    #     (extract_prestress_Cij); independent = the cold tensor at the shifted spring
    #     (extract_cubic_Cij -- a DIFFERENT assembler, the #527-fix reference pattern, NOT the
    #     defining identity). prove_can_fire() live-fire proves the halt plumbing each run (raises
    #     DeadGateError loudly if the gate has gone dead); the PASS aggregation and 1e-9 criterion
    #     are unchanged, so the merged [MAP-DEFORMED] verdict flow is untouched. -------------------
    from ave.validation import ReconcileGate

    from scripts.vol_1_foundations.srs_elastic_tensor import extract_cubic_Cij  # (already imported)
    ell_srs = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))
    ell_unique = sorted(set(round(float(np.linalg.norm(d)), 12) for (_, _, d) in bonds))
    vs4_cases = []
    vs4_ok = bool(len(ell_unique) == 1)  # uniform bond length is required for a single scalar shift
    vs4_can_fire = None
    for i, (ka, ks, T) in enumerate([(0.996345, 0.10194, 0.08532), (9.7734, 1.0, 0.3), (0.5, 0.9, 0.7850)]):
        pre = extract_prestress_Cij(pos, bonds, k_axial=ka, k_shear=ks, T_per_bond=T, rho=rho)
        gate = ReconcileGate(
            label=f"VS4_exact_collapse k_a={ka} k_s={ks} T={T}",
            claimed=np.array([pre[k] for k in ("C11", "C12", "C44")]),
            independent=lambda ka=ka, ks=ks, T=T: np.array(
                [extract_cubic_Cij(pos, bonds, k_axial=ka, k_shear=ks + T / ell_srs, rho=rho)[k]
                 for k in ("C11", "C12", "C44")]),
            rtol=1e-9,
        )
        if i == 0:
            # one liveness proof per run: the comparator+halt plumbing is shared by every case
            vs4_can_fire = bool(gate.prove_can_fire().can_fire_proven)
        res = gate.check()
        err = res.max_rel_discrepancy
        ok = bool(res.passed)
        vs4_ok = vs4_ok and ok
        vs4_cases.append({"k_a": ka, "k_s": ks, "T": T, "k_s_shifted": ks + T / ell_srs,
                          "prestress_vs_cold_shifted_rel_err": err, "PASS": ok})
    val["VS4_exact_collapse_to_shifted_shear_spring"] = {
        "srs_bond_length_unique": ell_unique, "srs_bond_length_uniform": bool(len(ell_unique) == 1),
        "cases": vs4_cases,
        "note": "prestress(k_a,k_s,T) == cold(k_a, k_s+T/l) BIT-EXACTLY -- the (T/l)(I-P) string term "
        "has the same projector structure as the shear spring, so the pre-stress is a SHIFTED SHEAR "
        "SPRING, NOT a new tensor family. The Born-Huang degree-1 homogeneity is INTACT; only #521's "
        "dictionary rho_eff=S_ax/S_shear breaks (the true coordinate is rho'=S_ax/(S_shear+T/l)).",
        "reconcile_gate": {
            "library": "ave.validation.ReconcileGate", "rtol": 1e-9,
            "independent_reference": "extract_cubic_Cij at k_s+T/l (different assembler, not the "
            "defining identity)",
            "selftest_can_fire_proven": vs4_can_fire,
        },
        "PASS": vs4_ok,
    }

    val["ALL_PASS"] = bool(pc1_ok and pc2_ok and pc3_ok and vs4_ok)
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


def extract_cubic_Cij_wrap(pos, bonds, rho_eff, rho):
    """#521 no-prestress reference (swapped springs, T=0) at rho_eff, + nu_Hill. Same pipeline."""
    from scripts.vol_1_foundations.srs_elastic_tensor import extract_cubic_Cij
    r = extract_cubic_Cij(pos, bonds, k_axial=rho_eff, k_shear=1.0, rho=rho)
    return {**r, **moduli_from_Cij(r["C11"], r["C12"], r["C44"])}


def _channel_bias(A_wall, is_shear_loads):
    """(A_axial, A_shear) for a channel assignment (prereg §2, matches #518).

    SHEAR-LOADS: axial fixed sub-saturated at sqrt(alpha), shear swept to A_wall.
    AXIAL-LOADS: shear fixed at sqrt(alpha), axial swept to A_wall.
    """
    if is_shear_loads:
        return A_CORE_SQRT_ALPHA, A_wall
    return A_wall, A_CORE_SQRT_ALPHA


def _prestress_tensor_at(pos, bonds, rho, A_axial, A_shear):
    """Full pre-stressed tensor + moduli at an operating point.

    Swapped springs (softened stiffnesses, #521): k_axial=S(A_axial), k_shear=S(A_shear).
    Pre-stress transverse term: T = each bond's OWN axial-channel tension Phi'(A_axial) (standard
    central-pair-potential form, prereg §3). Uniform across bonds (uniform-loading, #518) => the
    tension self-balances at cold geometry (residual-force check, reading A). rho_eff = the SWAPPED-
    spring ratio S_axial/S_shear (the #521 map variable) -- pre-stress is the ADDED physics on top.
    """
    S_axial = float(saturation_factor(A_axial, yield_limit=1.0))
    S_shear = float(saturation_factor(A_shear, yield_limit=1.0))
    T = float(bond_tension(A_axial))     # each bond's own axial tension (uniform-loading)
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))  # srs bond length (=1)
    r = extract_prestress_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear,
                              T_per_bond=T, rho=rho)
    mo = moduli_from_Cij(r["C11"], r["C12"], r["C44"])
    rho_eff = RHO_COLD * (S_axial / S_shear)          # #521 DICTIONARY coordinate (the one that breaks)
    k_shear_eff = S_shear + T / ell                    # the shifted shear spring (corrected mechanism)
    rho_prime = (S_axial / k_shear_eff) if k_shear_eff > 0 else float("inf")  # TRUE family coordinate
    return {
        "A_axial": A_axial, "A_shear": A_shear, "S_axial": S_axial, "S_shear": S_shear,
        "T_axial_prestress": T, "rho_eff": rho_eff,
        "k_shear_eff": k_shear_eff, "rho_prime_true_coord": rho_prime,
        "C11": r["C11"], "C12": r["C12"], "C44": r["C44"],
        "min_acoustic_eig": r["min_acoustic_eig"], "max_rel_residual": r["max_rel_residual"], **mo,
    }


def run_sweep(pos, bonds, rho) -> dict:
    """Both channel assignments (blind), full A_wall ladder. NEW readout: Delta-nu map shift vs #521.

    The #521 no-prestress map is regenerated on the SAME pipeline (full-precision reference, T=0 =>
    the swapped-springs tensor #521 computed) at the MATCHED rho_eff, then Delta-nu = nu_prestress -
    nu_#521 and Delta-nu/nu are reported at every swept point. The pole region (|nu_#521|>1) is
    excluded from the tolerance test (a rel-err on a divergent nu is meaningless), exactly as #521 VS3.
    """
    from scripts.vol_1_foundations.srs_elastic_tensor import extract_cubic_Cij

    canon_rungs = [0.0, A_CORE_SQRT_ALPHA, 0.5, 0.9, 1.0 - ALPHA, A_WALL_518_CROSSING, 0.999, 0.99999]
    log_approach = [1.0 - 10.0 ** (-k) for k in range(1, 9)]
    A_wall_ladder = sorted(set(canon_rungs + log_approach))
    dense = np.linspace(0.0, 0.99999, 5000)

    out = {}
    for name, is_sl in [("SHEAR_LOADS", True), ("AXIAL_LOADS", False)]:
        ladder = []
        max_abs_dnu_over_nu = 0.0        # pole-free-nu metric (SHEAR-LOADS has pole-free points)
        worst_row = None
        max_abs_shape_dev = 0.0          # pole-FREE SHAPE metric (works even in the nu pole region)
        worst_shape_row = None
        n_dnu_polefree_points = 0
        n_destabilized = 0
        for A_wall in A_wall_ladder:
            A_axial, A_shear = _channel_bias(A_wall, is_sl)
            t = _prestress_tensor_at(pos, bonds, rho, A_axial, A_shear)
            # #521 no-prestress reference at the SAME rho_eff (swapped springs, T=0), same pipeline
            rho_eff = t["rho_eff"]
            r521 = extract_cubic_Cij(pos, bonds, k_axial=rho_eff, k_shear=1.0, rho=rho)
            m521 = moduli_from_Cij(r521["C11"], r521["C12"], r521["C44"])
            nu_521 = m521["nu_Hill"]
            dnu = t["nu_Hill"] - nu_521
            nu_pole = bool(abs(nu_521) > 1.0)   # exclude the divergent branch from the NU tolerance test
            dnu_over_nu = (None if nu_pole else abs(dnu) / (abs(nu_521) + 1e-30))
            if dnu_over_nu is not None:
                n_dnu_polefree_points += 1
                if dnu_over_nu > max_abs_dnu_over_nu:
                    max_abs_dnu_over_nu = dnu_over_nu
                    worst_row = {"A_wall": A_wall, "rho_eff": rho_eff, "nu_prestress": t["nu_Hill"],
                                 "nu_521": nu_521, "dnu": dnu, "dnu_over_nu": dnu_over_nu}
            # POLE-FREE SHAPE deformation (the #521 VS3 metric): C11/C44, C12/C44, Zener -- bounded,
            # valid EVERYWHERE incl the nu pole region. This is what gives AXIAL-LOADS (rho_eff<1,
            # nu always in the pole region) an HONEST deformation verdict rather than a spurious null.
            shape_pre = np.array([t["C11"] / t["C44"], t["C12"] / t["C44"], t["Zener_A"]])
            shape_521 = np.array([r521["C11"] / r521["C44"], r521["C12"] / r521["C44"], m521["Zener_A"]])
            shape_dev = float(np.max(np.abs(shape_pre - shape_521) / (np.abs(shape_521) + 1e-30)))
            if shape_dev > max_abs_shape_dev:
                max_abs_shape_dev = shape_dev
                worst_shape_row = {"A_wall": A_wall, "rho_eff": rho_eff,
                                   "C11_C44_pre": shape_pre[0], "C11_C44_521": shape_521[0],
                                   "Zener_pre": t["Zener_A"], "Zener_521": m521["Zener_A"],
                                   "shape_dev": shape_dev}
            if t["min_acoustic_eig"] <= 0.0:
                n_destabilized += 1
            ladder.append({
                "A_wall": A_wall, "S_axial": t["S_axial"], "S_shear": t["S_shear"],
                "T_axial_prestress": t["T_axial_prestress"], "rho_eff": rho_eff,
                "k_shear_eff": t["k_shear_eff"], "rho_prime_true_coord": t["rho_prime_true_coord"],
                "C11": t["C11"], "C12": t["C12"], "C44": t["C44"],
                "K_bulk": t["K_bulk"], "sign_K": int(np.sign(t["K_bulk"])),
                "G_Hill": t["G_Hill"], "nu_Hill": t["nu_Hill"],
                "nu_521_noprestress": nu_521, "delta_nu": dnu,
                "nu_in_pole_region": nu_pole, "delta_nu_over_nu": dnu_over_nu,
                "shape_dev_vs_521": shape_dev,
                "Zener_A": t["Zener_A"], "Zener_A_521": m521["Zener_A"], "KG_Hill": t["KG_Hill"],
                "min_acoustic_eig": t["min_acoustic_eig"], "max_rel_residual": t["max_rel_residual"],
            })
        # crossing of rho_eff=RHO_STAR_IMPORTED (the #521 swapped-spring ratio; pre-stress does not
        # change rho_eff, only the tensor AT it -- so the crossing amplitude is the #521 0.99479)
        r_dense = np.array([
            saturation_factor(_channel_bias(a, is_sl)[0], yield_limit=1.0)
            / saturation_factor(_channel_bias(a, is_sl)[1], yield_limit=1.0) for a in dense])
        cross = _cross_amplitude(dense, r_dense, RHO_STAR_IMPORTED)
        # pre-stressed nu/Zener/KG AT the crossing rho_eff (the [MAP-DEFORMED] knife readout)
        nu_at_cross = zener_at_cross = kg_at_cross = nu521_at_cross = None
        if cross is not None:
            A_ax_c, A_sh_c = _channel_bias(cross, is_sl)
            tc = _prestress_tensor_at(pos, bonds, rho, A_ax_c, A_sh_c)
            r521c = extract_cubic_Cij(pos, bonds, k_axial=tc["rho_eff"], k_shear=1.0, rho=rho)
            m521c = moduli_from_Cij(r521c["C11"], r521c["C12"], r521c["C44"])
            nu_at_cross, zener_at_cross, kg_at_cross = tc["nu_Hill"], tc["Zener_A"], tc["KG_Hill"]
            nu521_at_cross = m521c["nu_Hill"]
        direction = "STIFFENING" if r_dense[-1] > RHO_COLD else "SOFTENING"
        # NEW nu=2/7 locus in the OLD (rho_eff) coordinate, K>0-gated, by BISECTION (not linear
        # interpolation -- item 4 fix: interpolation on the sparse ladder gave 66.6; the true
        # bisected stable-branch locus is 59.93). nu diverges through the K=0 pole, so the search is
        # restricted to the stable K>0 branch. Uses the exact-collapse remap: prestress at rho_eff =
        # cold at k_shear=S_shear+T/l, so we bisect the COLD-family nu directly.
        new_nu27_rho_eff = _bisect_nu27_old_coord(pos, bonds, rho, is_sl)
        # the CAP on the true coordinate rho'_max = S_ax*l/T (finite; the yield wall no longer -> inf).
        # SHEAR-LOADS: axial fixed at sqrt(alpha) => T, S_ax both fixed => a single cap. AXIAL-LOADS:
        # axial is swept so T,S_ax both vary => rho' still bounded but not a single scalar; report the
        # SHEAR-LOADS cap (the physically-relevant matter branch).
        ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))
        if is_sl:
            S_ax_c = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=1.0))
            T_c = float(bond_tension(A_CORE_SQRT_ALPHA))
            rho_prime_cap = S_ax_c * ell / T_c
        else:
            rho_prime_cap = None  # axial swept -> no single scalar cap; reported on SHEAR-LOADS
        out[name] = {
            "fixed_channel": "axial@sqrt(alpha)" if is_sl else "shear@sqrt(alpha)",
            "swept_channel": "shear->yield" if is_sl else "axial->yield",
            "direction": direction, "ladder": ladder,
            "rho_eff_at_yield_limit": float(r_dense[-1]),
            "crosses_rho_star_9.77": cross is not None, "crossing_A_wall": cross,
            "nu_Hill_at_crossing_PRESTRESS": nu_at_cross,
            "nu_Hill_at_crossing_521_noprestress": nu521_at_cross,
            "Zener_at_crossing": zener_at_cross, "KG_Hill_at_crossing": kg_at_cross,
            "max_abs_delta_nu_over_nu": max_abs_dnu_over_nu, "worst_delta_nu_row": worst_row,
            "n_delta_nu_polefree_points": n_dnu_polefree_points,
            "max_abs_shape_dev_vs_521": max_abs_shape_dev, "worst_shape_dev_row": worst_shape_row,
            "n_destabilized_rungs": n_destabilized,
            "new_nu_2_7_locus_rho_eff_OLD_coord_bisected": new_nu27_rho_eff,
            "rho_prime_true_coord_at_yield_limit": float(ladder[-1]["rho_prime_true_coord"]),
            "rho_prime_cap": rho_prime_cap,
        }
    return out


def _bisect_nu27_old_coord(pos, bonds, rho, is_shear_loads, lo=2.5, hi=200.0, tol=1e-7, nmax=100):
    """Bisect the OLD-coordinate rho_eff where the PRE-STRESSED nu_Hill = 2/7, in the stable K>0
    branch (item 4 fix: bisection not linear interpolation). Uses the exact-collapse remap:
    prestress at a given rho_eff = cold at k_shear = S_shear + T/l. Returns rho_eff or None."""
    from scripts.vol_1_foundations.srs_elastic_tensor import extract_cubic_Cij
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))
    A_core = A_CORE_SQRT_ALPHA
    S_ax = float(saturation_factor(A_core, yield_limit=1.0))
    T = float(bond_tension(A_core))  # SHEAR-LOADS fixed axial tension

    def nu_and_K(rho_eff):
        # SHEAR-LOADS: axial fixed (S_ax, T), shear set to hit rho_eff = S_ax/S_shear
        if is_shear_loads:
            S_shear = S_ax / rho_eff
            k_shear_eff = S_shear + T / ell
            k_ax = S_ax
        else:  # AXIAL-LOADS: axial swept -> rho_eff<1 branch, nu in the pole region (no stable 2/7)
            return None, None
        r = extract_cubic_Cij(pos, bonds, k_axial=k_ax, k_shear=k_shear_eff, rho=rho)
        m = moduli_from_Cij(r["C11"], r["C12"], r["C44"])
        return m["nu_Hill"], m["K_bulk"]

    nlo, Klo = nu_and_K(lo)
    if nlo is None:
        return None
    nhi, _ = nu_and_K(hi)
    if nlo is None or nhi is None or (nlo - NU_2_7) * (nhi - NU_2_7) > 0:
        return None
    for _ in range(nmax):
        mid = 0.5 * (lo + hi)
        nm, Km = nu_and_K(mid)
        if abs(nm - NU_2_7) < tol:
            return mid if (Km is not None and Km > 0) else None
        if (nlo - NU_2_7) * (nm - NU_2_7) < 0:
            hi = mid
        else:
            lo, nlo = mid, nm
    return 0.5 * (lo + hi)


def _cross_amplitude(A_wall, profile, target):
    """Linear-interpolated A_wall (or rho_eff) where profile crosses target, or None."""
    r = np.asarray(profile, float)
    x = np.asarray(A_wall, float)
    for i in range(len(r) - 1):
        lo, hi = r[i], r[i + 1]
        if np.isnan(lo) or np.isnan(hi):
            continue
        if (lo - target) * (hi - target) <= 0 and lo != hi:
            frac = (target - lo) / (hi - lo)
            return float(x[i] + frac * (x[i + 1] - x[i]))
    return None


# ===========================================================================
# DRIVER
# ===========================================================================
def main():
    out = {
        "title": "THE PRE-STRESSED srs ELASTIC-TENSOR ARC (beyond-model test 1 of 2)",
        "scope": "initial/residual PRE-STRESS ONLY, at FIXED geometry; geometry-change is test 2",
        "tension_form": "T(A)=Phi'(A)=k0(A*sqrt(1-A^2)+arcsin A)/2 (Ax4 kernel integrated); "
        "transverse initial-stress term (T/l)(I-d^d^) (Born-Huang/Wallace)",
        "rho_star_imported_readoff_only": RHO_STAR_IMPORTED, "nu_2_7_target": NU_2_7,
        "A_core_sqrt_alpha": A_CORE_SQRT_ALPHA, "A_wall_518_crossing_readoff": A_WALL_518_CROSSING,
    }
    print("=" * 78)
    print("THE PRE-STRESSED srs ELASTIC-TENSOR ARC — beyond-model test 1 of 2 (PRE-STRESS)")
    print("=" * 78)

    pos_r, bonds_r, rho_r = srs_primitive("right")
    pos_l, bonds_l, rho_l = srs_primitive("left")

    # ---- (0) POSITIVE CONTROLS (HALT if fail) ----------------------------
    pc = run_positive_controls(pos_r, bonds_r, rho_r)
    out["positive_controls"] = pc
    print("(0) POSITIVE CONTROLS (HALT if fail):")
    print(f"  PC1 zero-bias recovery (T=0 => cold tensor): "
          f"{'PASS' if pc['PC1_zero_bias_recovery']['PASS'] else 'FAIL'} "
          f"(err={pc['PC1_zero_bias_recovery']['max_rel_err_vs_cold_same_pipeline']:.1e})")
    print(f"  PC2 analytic stressed simple-cubic (C44 shift=T/l): "
          f"{'PASS' if pc['PC2_analytic_stressed_lattice']['PASS'] else 'FAIL'}")
    print(f"  PC3 homogeneity re-check (T=0 => #521 deg-1): "
          f"{'PASS' if pc['PC3_homogeneity_T0']['PASS'] else 'FAIL'}")
    print(f"  VS4 exact-collapse (prestress == cold at shifted shear spring): "
          f"{'PASS' if pc['VS4_exact_collapse_to_shifted_shear_spring']['PASS'] else 'FAIL'}")
    print(f"  VS4 reconcile-gate can-fire self-test (synthetic discrepancy fired the halt): "
          f"{'PROVEN' if pc['VS4_exact_collapse_to_shifted_shear_spring']['reconcile_gate']['selftest_can_fire_proven'] else 'FAIL'}")
    print(f"  ALL_PASS = {pc['ALL_PASS']}")
    if not pc["ALL_PASS"]:
        print("\nHALT: positive controls FAILED — pre-stress insertion wrong; no verdict.")
        _write(out)
        import sys
        sys.exit(1)

    # ---- (1) GEOMETRY-COUPLED discriminator (prereg §6 branch ii, §9) -----
    # residual node force from the bias tensions at COLD geometry, at the near-yield crossing point.
    A_ax_c, A_sh_c = _channel_bias(A_WALL_518_CROSSING, True)  # SHEAR-LOADS crossing
    T_c = float(bond_tension(A_ax_c))   # axial channel tension (the pre-stress T entering (T/l))
    rf = residual_node_forces(pos_r, bonds_r, T_c)
    GEOM_FLOOR = 1e-9   # relative residual floor: above this = a real unbalanced force
    geometry_coupled = bool(rf["relative_residual"] > GEOM_FLOOR)
    out["geometry_coupled_discriminator"] = {
        **rf, "relative_floor": GEOM_FLOOR, "GEOMETRY_COUPLED": geometry_coupled,
        "reading": ("B (unbalanced -> [GEOMETRY-COUPLED]; tests 1&2 inseparable)" if geometry_coupled
                    else "A (self-balancing pre-stress at fixed geometry; test 1 is well-posed)"),
        "note": "net force at each node from the bias bond tensions at the COLD unrelaxed geometry. "
        "srs z=3 site symmetry makes uniform bond tensions self-cancel => reading A (machine zero). "
        "A nonzero residual above the floor => the fixed-geometry pre-stress is NOT an equilibrium "
        "=> [GEOMETRY-COUPLED].",
    }
    print(f"\n(1) GEOMETRY-COUPLED discriminator: max residual node force = "
          f"{rf['max_residual_node_force']:.2e} (relative {rf['relative_residual']:.2e}); "
          f"reading {'B [GEOMETRY-COUPLED]' if geometry_coupled else 'A (fixed-geometry OK)'}")

    # ---- (2) enantiomorph parity control ---------------------------------
    A_ax, A_sh = _channel_bias(A_WALL_518_CROSSING, True)
    t_r = _prestress_tensor_at(pos_r, bonds_r, rho_r, A_ax, A_sh)
    t_l = _prestress_tensor_at(pos_l, bonds_l, rho_l, A_ax, A_sh)
    hand_diff = max(abs(t_r[k] - t_l[k]) / (abs(t_r[k]) + abs(t_l[k]) + 1e-30)
                    for k in ("C11", "C12", "C44"))
    out["enantiomorph_parity"] = {"max_rel_hand_difference": hand_diff,
                                  "parity_symmetric": bool(hand_diff < 1e-6)}

    # ---- (3) the sweep (both assignments) --------------------------------
    sweep = run_sweep(pos_r, bonds_r, rho_r)
    out["sweep_both_assignments"] = sweep

    # ---- (3a) delta_y NORMALIZATION BAND (item 2, orchestrator fix round) --
    # T=Phi'(A) integrates over DIMENSIONLESS amplitude A; turning it into a FORCE that adds to
    # k_shear silently identifies the yield-DISPLACEMENT delta_y = 1 bond length (T_phys = delta_y*T,
    # k0=1). This is an ENGINEERING/NORMALIZATION choice (substrate-first-for-numbers), NOT canon-
    # forced. Canon's Ax4 residual-content (axiom-register.md:189) bounds the arc* yield anchor at
    # ~0.89-0.96 l_node (tent) and ~0.79x that under the continuum elastica -> delta_y in ~[0.70,0.96].
    # Every headline MAGNITUDE is a BAND over this range; the BINARY verdict is robust far beyond it.
    A_ax_c0, A_sh_c0 = _channel_bias(A_WALL_518_CROSSING, True)
    S_ax0 = float(saturation_factor(A_ax_c0, yield_limit=1.0))
    S_sh0 = float(saturation_factor(A_sh_c0, yield_limit=1.0))
    rho_eff0 = S_ax0 / S_sh0
    T0 = float(bond_tension(A_ax_c0))
    ell0 = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds_r]))
    band = []
    for dy in (0.70, 0.76, 0.89, 0.96, 1.0):
        rr = extract_cubic_Cij(pos_r, bonds_r, k_axial=S_ax0, k_shear=S_sh0 + dy * T0 / ell0, rho=rho_r)
        mm = moduli_from_Cij(rr["C11"], rr["C12"], rr["C44"])
        band.append({"delta_y_bond_lengths": dy, "T_phys": dy * T0,
                     "nu_at_crossing": mm["nu_Hill"], "cap_rho_prime": S_ax0 * ell0 / (dy * T0)})
    # binary robustness: smallest delta_y that still deforms past the 1e-4 nu tolerance
    thr_dy = None
    for dy in (1e-4, 1.5e-4, 1e-3, 1e-2):
        rr = extract_cubic_Cij(pos_r, bonds_r, k_axial=S_ax0, k_shear=S_sh0 + dy * T0 / ell0, rho=rho_r)
        mm = moduli_from_Cij(rr["C11"], rr["C12"], rr["C44"])
        if abs(mm["nu_Hill"] - NU_2_7) / NU_2_7 > 1e-4:
            thr_dy = dy
            break
    out["delta_y_normalization_band"] = {
        "STATUS": "ENGINEERING/NORMALIZATION-CHOICE (NOT canon-forced) -- ledger row added",
        "meaning": "T=Phi'(A) integrates over dimensionless A; force = delta_y*T with delta_y the "
        "yield displacement in bond lengths. delta_y=1 was the implicit default (T_phys=T).",
        "canon_arc_star_band": "0.89-0.96 (tent) / *0.79 (elastica) => delta_y ~ [0.70, 0.96] "
        "(axiom-register.md:189, Ax4 residual-content)",
        "nu_at_crossing_BAND": [band[0]["nu_at_crossing"], band[-2]["nu_at_crossing"]],
        "cap_BAND": [band[-2]["cap_rho_prime"], band[0]["cap_rho_prime"]],
        "band_table": band,
        "binary_verdict_deforms_for_delta_y_above": thr_dy,
        "binary_robustness_margin": f"~{0.70 / (thr_dy or 1e-4):.0f}x (physical delta_y>=0.70 is "
        f">{0.70 / (thr_dy or 1e-4):.0f}x the ~{thr_dy:.1e} deform threshold)",
        "note": "MAGNITUDES are BANDS: nu_at_crossing in ~[0.098, 0.151], cap in ~[12.2, 16.7]. "
        "The BINARY verdict [MAP-DEFORMED] holds for any delta_y > ~1.5e-4 -- a ~5000x margin below "
        "the physical delta_y. Six-digit headline numbers without the band are false precision.",
    }

    # ---- (3b) KEEP-BOTH tension-form sensitivity (prereg §3) --------------
    # standard form uses each bond's OWN AXIAL tension in (T/l)(I-P). The alternative uses the
    # CHANNEL (near-yield swept) tension. Both recorded at the SHEAR-LOADS crossing; the [MAP-DEFORMED]
    # verdict is robust to the choice (recorded, not silently picked).
    A_ax_c, A_sh_c = _channel_bias(A_WALL_518_CROSSING, True)
    S_ax_c = float(saturation_factor(A_ax_c, yield_limit=1.0))
    S_sh_c = float(saturation_factor(A_sh_c, yield_limit=1.0))
    rho_eff_c = S_ax_c / S_sh_c
    tform = {}
    for lbl, T in [("standard_axial_tension", float(bond_tension(A_ax_c))),
                   ("alt_channel_shear_tension", float(bond_tension(A_sh_c)))]:
        rr = extract_prestress_Cij(pos_r, bonds_r, k_axial=S_ax_c, k_shear=S_sh_c, T_per_bond=T, rho=rho_r)
        mm = moduli_from_Cij(rr["C11"], rr["C12"], rr["C44"])
        tform[lbl] = {"T": T, "nu_Hill": mm["nu_Hill"], "K_bulk": mm["K_bulk"],
                      "sign_K": int(np.sign(mm["K_bulk"])), "KG_Hill": mm["KG_Hill"],
                      "Zener_A": mm["Zener_A"], "min_acoustic_eig": rr["min_acoustic_eig"]}
    r5 = extract_cubic_Cij_wrap(pos_r, bonds_r, rho_eff_c, rho_r)
    out["tension_form_sensitivity_at_crossing"] = {
        "rho_eff": rho_eff_c, "nu_521_noprestress_target_2_7": r5["nu_Hill"],
        "forms": tform,
        "note": "BOTH tension-form choices feed the SAME axial string slot (item 5a: this KEEP-BOTH "
        "fork does NOT bracket a genuinely different carrier -- see keep_both_bracketing_note). Both "
        "deform the #521 dictionary. Verdict [MAP-DEFORMED] robust to the standard-vs-channel choice.",
    }

    # ---- (3c) THE SIGN FORK (item 3, GRANT-FORK -- report both arms, do NOT resolve) --
    # I assumed the STRETCHED-PAIR reading (T>0, taut string). Canon's Ax4 residual-content
    # (axiom-register.md:189) reads the SAME kernel as a fixed-arc-length BOWED STRUT (Euler
    # buckling) -- whose end-to-end AXIAL force is plausibly COMPRESSIVE (T<0). The bin verdict
    # survives either sign; the physical narrative INVERTS. Report both arms with the remap reading.
    ell_sf = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds_r]))
    sign_arms = {}
    for lbl, Tsign in [("T_positive_stretched_pair", +T0), ("T_negative_compressive_buckling", -T0)]:
        k_shear_eff = S_sh0 + Tsign / ell_sf
        rr = extract_prestress_Cij(pos_r, bonds_r, k_axial=S_ax0, k_shear=S_sh0, T_per_bond=Tsign, rho=rho_r)
        mm = moduli_from_Cij(rr["C11"], rr["C12"], rr["C44"])
        rho_prime = (S_ax0 / k_shear_eff) if k_shear_eff > 0 else float("inf")
        sign_arms[lbl] = {
            "T": Tsign, "nu_at_crossing": mm["nu_Hill"], "K_bulk": mm["K_bulk"],
            "sign_K": int(np.sign(mm["K_bulk"])), "Zener_A": mm["Zener_A"],
            "k_shear_eff": k_shear_eff, "rho_prime_remap": rho_prime,
            "remap_reading": ("k_s+T/l > 0 => rho' CAPPED at finite S_ax*l/T (yield wall finite)"
                              if Tsign > 0 else
                              "k_s+T/l -> 0 as |T| grows => rho' UNCAPPED -> +inf at finite amplitude "
                              "(the divergence direction)"),
        }
    out["sign_fork_GRANT"] = {
        "STATUS": "OPEN GRANT-FORK -- both arms reported, NOT resolved (flag-don't-fix)",
        "my_assumed_arm": "T_positive_stretched_pair (taut-string pair-potential analogy)",
        "canon_alternative_arm": "T_negative_compressive_buckling (Ax4 residual-content: the kernel "
        "is a fixed-arc-length BOWED STRUT / Euler buckling, axiom-register.md:189)",
        "arms": sign_arms,
        "verdict_survives_either_sign": True,
        "narrative_inverts": "T>0: nu DROPS 2/7->0.089 (rho' capped). T<0: nu RISES 2/7->0.466 toward "
        "1/2, approaches instability, rho' UNCAPPED (k_s+T/l->0 => rho'->inf at finite amplitude).",
        "fork_resolution_condition": "derive the END-TO-END axial force of the biased bond from the "
        "BUCKLING MICROFOUNDATION (fixed arc-length, A^2+S^2=arc*^2, Euler-strut), NOT the pair-"
        "potential Phi'(A) analogy. The sign of that end-to-end force decides the arm. Flagged for "
        "Grant alongside result-doc section 10.1.",
    }

    # ---- (3d) KEEP-BOTH does NOT bracket (item 5a) --------------------------
    out["keep_both_bracketing_note"] = {
        "STATUS": "the standard-vs-channel KEEP-BOTH does NOT bracket a different CARRIER",
        "why": "both the standard (axial-tension) and alt (channel/shear-tension) forms feed the SAME "
        "transverse (I-P) string slot -- they differ only in the SCALAR T magnitude, not in the "
        "force-constant STRUCTURE. Both collapse to a shifted shear spring (VS4). So KEEP-BOTH here "
        "brackets a MAGNITUDE choice, not a genuinely different pre-stress carrier.",
        "what_a_different_carrier_would_need": "a pre-stress term with a DIFFERENT projector structure "
        "-- e.g. an axial-tension contribution to the P (d^d^) block (a stretch-stiffening of the "
        "longitudinal spring), or a Cosserat couple-stress (Stage 2) transverse-BENDING term with an "
        "off-(I-P) structure. Such a carrier could leave the cold family (break VS4) and is the only "
        "way pre-stress could produce a genuinely NEW tensor -- untested here (fixed-geometry, "
        "Cauchy-only scope).",
    }

    # ---- (3e) CELL-STRESS honesty note (item 5g, Grant's question) ---------
    # The residual-force check (section 1) covers INTERNAL node DOFs only. The CELL VIRIAL under
    # uniform bond tension is NONZERO and is clamped by the FIXED geometry -- the uniform dilation/
    # compression (A1-owned) response is exactly test 2's leading mode.
    ell_cv = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds_r]))
    T_cv = float(bond_tension(A_CORE_SQRT_ALPHA))
    # cell virial (scalar) = sum over bonds of T * l (per-bond tension * length), a NONZERO dilational
    # stress that the fixed cell clamps. Central-pair form -> pure dilation; channel form -> +deviatoric.
    cell_virial = float(sum(T_cv * np.linalg.norm(d) for (_, _, d) in bonds_r))
    out["cell_stress_honesty_note"] = {
        "STATUS": "DISCLOSED -- the residual-force check covers INTERNAL node DOFs ONLY",
        "internal_node_residual": "self-balances to machine zero (section 1, reading A)",
        "cell_virial_under_uniform_tension": cell_virial,
        "meaning": "the CELL (macroscopic) virial under uniform bond tension is NONZERO -- a uniform "
        "dilational stress clamped by the FIXED cell geometry. That uniform dilation/compression is "
        "A1-owned and is EXACTLY test 2's (bias-geometry-change) leading mode: central-pair form -> "
        "pure dilation; channel form -> + deviatoric. So [GEOMETRY-COUPLED]=NOT-triggered is scoped "
        "to INTERNAL DOFs; the CELL-scale relaxation is deferred to test 2, honestly. This does NOT "
        "change test 1's fixed-geometry small-signal tensor (the internal DOFs are the ones the "
        "acoustic modes ride on), but it is stated so the scope boundary is exact.",
    }

    # ---- (4) two-hand cross-validation -----------------------------------
    crossval = _two_hand_crossval(pos_r, bonds_r, rho_r)
    out["two_hand_crossval"] = crossval

    # ---- (5) per-assignment bin verdicts (NO fall-through else) -----------
    DNU_TOL = 1e-4     # [MAP-UNDEFORMED] tolerance (frozen prereg §6): pole-free nu Delta-nu/nu
    SHAPE_TOL = 1e-4   # pole-free SHAPE realization of the SAME criterion (valid in the nu pole region)
    verdicts = {}
    for name, is_sl in [("SHEAR_LOADS", True), ("AXIAL_LOADS", False)]:
        d = sweep[name]
        max_dnu = d["max_abs_delta_nu_over_nu"]
        max_shape = d["max_abs_shape_dev_vs_521"]
        n_destab = d["n_destabilized_rungs"]
        # MAP-DEFORMED if EITHER the pole-free nu shifts OR (where nu is in the pole region) the
        # pole-free SHAPE (C11/C44, C12/C44, Zener) shifts. The SHAPE metric is what catches the
        # AXIAL-LOADS deformation (rho_eff<1 everywhere => nu always in the pole region).
        # item 5c -- prereg-fidelity: the FROZEN bin [MAP-UNDEFORMED] criterion is "nu(rho_eff)
        # matches the #521 map within tolerance". Report the PER-FROZEN-BINS verdict VERBATIM FIRST
        # (on the frozen nu-ratio metric), THEN the SHAPE metric as explicitly POST-HOC supplementary.
        n_polefree = d["n_delta_nu_polefree_points"]
        if n_polefree == 0:
            # the frozen nu-ratio metric is UNDEFINED here (nu in the pole region at every rung) --
            # do NOT read a verdict from an undefined metric; the SHAPE metric (post-hoc) decides.
            frozen_metric_verdict = ("FROZEN nu-ratio metric UNDEFINED (nu in the pole region at "
                                     "every rung; 0 pole-free points) -- no verdict from the frozen "
                                     "metric alone")
            deformed_by_frozen = None
        else:
            deformed_by_frozen = bool(max_dnu > DNU_TOL)
            frozen_metric_verdict = ("MAP-DEFORMED" if deformed_by_frozen else "MAP-UNDEFORMED") + \
                " (frozen nu-ratio metric, %d pole-free points)" % n_polefree
        deformed_by_shape_posthoc = bool(max_shape > SHAPE_TOL)  # POST-HOC supplementary metric
        map_deformed = bool((deformed_by_frozen is True) or deformed_by_shape_posthoc)
        # NOTE (mechanism correction): [MAP-DEFORMED] here means the #521 DICTIONARY tie nu<->
        # S_ax/S_shear breaks (the map, as #521 defined it, is deformed). It does NOT mean a new
        # tensor family or new instability (VS4 exact-collapse: the tensor stays in the cold family).
        # NOTE (item 5e -- reachability): the frozen prereg §6 bin logic is (ii) geom, (iii) destab,
        # (iv) deformed, (v) undeformed. Under the corrected mechanism the STANDARD form is NEVER
        # destabilized and ALWAYS deformed, so those branches would look dead on THIS run -- but the
        # else-branch and the destab branch ARE reachable (the alt-channel-form arm below drives K<0,
        # and the reconcile-contradiction below can fire the halt). Reachability proven, item 5e.
        # reconcile-don't-declare: a state that is map_deformed but VS4 exact-collapse FAILED would be
        # a self-contradiction (deformed map yet tensor in the cold family) -> loud DISCREPANT-HALT.
        destabilized = bool(n_destab > 0)
        vs4_pass = bool(out["positive_controls"]["VS4_exact_collapse_to_shifted_shear_spring"]["PASS"])
        if geometry_coupled:
            primary = "GEOMETRY-COUPLED"
        elif map_deformed and not vs4_pass:
            # deformed map AND tensor left the cold family -> the corrected mechanism is WRONG here;
            # this must never happen silently -- loud halt (item 5e: the halt is now REACHABLE).
            primary = ("DISCREPANT-HALT: map reads DEFORMED but VS4 exact-collapse FAILED "
                       "(the tensor left the cold family) -- these contradict; the shifted-shear-"
                       "spring mechanism does not hold here. NEEDS REVIEW.")
        elif destabilized and map_deformed:
            primary = "DESTABILIZED + MAP-DEFORMED"
        elif destabilized:
            primary = "DESTABILIZED"
        elif map_deformed:
            primary = "MAP-DEFORMED"
        elif max_dnu <= DNU_TOL and max_shape <= SHAPE_TOL:
            primary = "MAP-UNDEFORMED"
        else:
            primary = ("DISCREPANT-HALT: no frozen bin cleanly matched "
                       f"(max|dnu/nu|={max_dnu}, max|shape|={max_shape}, n_destab={n_destab}) "
                       "-- NEEDS REVIEW.")
        # KNIFE (re-aimed, item 5d): the crossing AMPLITUDE is analytically invariant (pre-stress
        # does not move rho_eff), so testing IT was testing a fixed quantity. Re-aim at the things
        # that DO move under pre-stress: (a) the true-coordinate cap rho'_max, and (b) the OLD-coord
        # nu=2/7 locus. A canon-distinguished landing on EITHER is a max-scrutiny would-be-chord flag.
        cap = d["rho_prime_cap"]
        locus = d["new_nu_2_7_locus_rho_eff_OLD_coord_bisected"]
        knife = {"cap_rho_prime": cap, "new_nu27_locus_OLD_coord": locus}
        if cap is not None:
            # cap ~ 1/sqrt(alpha) is the trivial small-A expansion (T~k0*A at A=sqrt(alpha)), NOT a
            # coincidence; documented in the result. Also test 9.7734/cap against ratio families.
            knife["cap_vs_inv_sqrt_alpha"] = cap * float(np.sqrt(ALPHA))  # ~0.9976
            knife["cap_is_small_A_expansion_not_coincidence"] = True
            r_9_cap = RHO_STAR_IMPORTED / cap
            knife["rho_star_over_cap"] = r_9_cap  # ~0.8369
            knife["rho_star_over_cap_near_5_6"] = bool(abs(r_9_cap - 5.0 / 6.0) < 5e-3)  # near-miss noise
        canon_hit = False
        for val_ in [locus, cap]:
            if val_ is not None:
                canon_hit = canon_hit or bool(
                    abs(val_ - RHO_STAR_IMPORTED) < 1e-2 or abs(val_ - 2.0) < 1e-2
                    or abs(val_ - 1.0 / np.sqrt(ALPHA)) < 1e-2)  # 1/sqrt(alpha) is the KNOWN expansion
        knife["lands_on_canon_distinguished_value"] = canon_hit
        verdicts[name] = {
            "PRIMARY_BIN": primary, "direction": d["direction"],
            "FROZEN_metric_verdict_VERBATIM": frozen_metric_verdict,        # item 5c: report first
            "SHAPE_metric_POST_HOC_supplementary": deformed_by_shape_posthoc,  # item 5c: post-hoc
            "prereg_fidelity_note": "the frozen bin criterion is the nu-ratio match; the SHAPE metric "
            "was ADDED post-freeze to give AXIAL-LOADS (nu in the pole region) an honest verdict -- "
            "reported as explicitly POST-HOC supplementary, not as the frozen criterion.",
            "max_abs_delta_nu_over_nu": max_dnu, "worst_delta_nu_row": d["worst_delta_nu_row"],
            "n_delta_nu_polefree_points": d["n_delta_nu_polefree_points"],
            "max_abs_shape_dev_vs_521": max_shape, "worst_shape_dev_row": d["worst_shape_dev_row"],
            "map_undeformed_tolerance_nu": DNU_TOL, "map_undeformed_tolerance_shape": SHAPE_TOL,
            "n_destabilized_rungs": n_destab,
            "crossing_A_wall_ANALYTICALLY_INVARIANT": d["crossing_A_wall"],
            "nu_at_crossing_PRESTRESS": d["nu_Hill_at_crossing_PRESTRESS"],
            "nu_at_crossing_521_noprestress": d["nu_Hill_at_crossing_521_noprestress"],
            "KG_at_crossing_PRESTRESS": d["KG_Hill_at_crossing"],
            "new_nu_2_7_locus_rho_eff_OLD_coord": locus,
            "rho_prime_cap": cap,
            "KNIFE_reaimed_at_movable_quantities": knife,
        }
    out["bin_verdicts_per_assignment"] = verdicts

    print(f"\n(2) enantiomorph parity: max hand-diff = {hand_diff:.2e} "
          f"({'symmetric' if hand_diff < 1e-6 else 'BROKEN — BUG'})")
    print("\n(3) THE SWEEP — Delta-nu(rho_eff) map shift vs #521, both assignments:")
    for name in ("SHEAR_LOADS", "AXIAL_LOADS"):
        d = sweep[name]
        print(f"  --- {name} ({d['fixed_channel']}, {d['direction']}) ---")
        print(f"      max|Delta-nu/nu| (pole-free nu, {d['n_delta_nu_polefree_points']} pts) = "
              f"{d['max_abs_delta_nu_over_nu']:.3e}; "
              f"max|shape-dev| (pole-FREE, all pts) = {d['max_abs_shape_dev_vs_521']:.3e}; "
              f"destabilized rungs = {d['n_destabilized_rungs']}")
        if d["crossing_A_wall"] is not None:
            print(f"      at rho_eff=9.77 crossing (A_wall={d['crossing_A_wall']:.5f}): "
                  f"nu_prestress={d['nu_Hill_at_crossing_PRESTRESS']:.5f} vs "
                  f"nu_#521={d['nu_Hill_at_crossing_521_noprestress']:.5f}")
    print("\n(4) TWO-HAND CROSS-VALIDATION (long-wave vs [100] direct):")
    for p in crossval["points"]:
        print(f"      {p['label']}: rho_eff={p['rho_eff']:.4f} C11 lw/direct err={p['rel_err_C11']:.1e} "
              f"AGREE={p['AGREE']}")
    print(f"      ALL_AGREE = {crossval['ALL_AGREE']}")
    print("\n(5) PER-ASSIGNMENT BIN VERDICTS:")
    for name, v in verdicts.items():
        kn = v["KNIFE_reaimed_at_movable_quantities"]
        print(f"      [{name}] PRIMARY BIN: {v['PRIMARY_BIN']} "
              f"(max|dnu/nu|={v['max_abs_delta_nu_over_nu']:.2e}, cap={v['rho_prime_cap']}, "
              f"nu=2/7 locus(OLD coord)={v['new_nu_2_7_locus_rho_eff_OLD_coord']}, "
              f"KNIFE lands-on-canon={kn['lands_on_canon_distinguished_value']})")

    _write(out)
    return out


def _two_hand_crossval(pos, bonds, rho) -> dict:
    """Full-direction least-squares long-wave C_ij vs independent [100] direct eigensolve of the
    PRE-STRESSED acoustic branches, at >=3 operating points INCLUDING the 9.77 crossing."""
    S_axial_core = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=1.0))
    T_core = float(bond_tension(A_CORE_SQRT_ALPHA))  # SHEAR-LOADS: axial channel fixed at sqrt(alpha)
    pts = []
    for label, rho_eff_target in [("cold_rho1", 1.0), ("stable_rho3", 3.0),
                                  ("nu2_7_crossing_rho9.7734", RHO_STAR_IMPORTED)]:
        S_axial = S_axial_core
        S_shear = S_axial / rho_eff_target
        r_lsq = extract_prestress_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear,
                                      T_per_bond=T_core, rho=rho)
        r_100 = extract_prestress_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear,
                                      T_per_bond=T_core, rho=rho, directions=[[1, 0, 0]])
        st = r_100["slope_table"]["100"]["rho_c2_eigs_ascending"]
        # [100] eigenvalues are {C11 (long, 1x), C44 (transverse, 2x)} but ascending-SORT mislabels
        # them at the near-iso-bond point where C11 approx C44 (pre-stress can push C44>C11). Match
        # by NEAREST VALUE to the lsq (C11, C44), not by ascending position -- this tests the actual
        # agreement without the branch-order assumption (the cold arc's [0]=C44,[2]=C11 only holds
        # when C11>C44). The transverse pair is the two nearest eigenvalues; C11 is the odd one out.
        eig = np.array(st, float)
        # the duplicated (transverse=C44) pair are the two closest eigenvalues; C11 is the remaining
        pair_gaps = [abs(eig[0] - eig[1]), abs(eig[1] - eig[2]), abs(eig[0] - eig[2])]
        if pair_gaps[0] <= pair_gaps[1] and pair_gaps[0] <= pair_gaps[2]:
            C44_direct, C11_direct = 0.5 * (eig[0] + eig[1]), eig[2]
        elif pair_gaps[1] <= pair_gaps[2]:
            C44_direct, C11_direct = 0.5 * (eig[1] + eig[2]), eig[0]
        else:
            C44_direct, C11_direct = 0.5 * (eig[0] + eig[2]), eig[1]
        err_C11 = abs(r_lsq["C11"] - C11_direct) / (abs(C11_direct) + 1e-30)
        err_C44 = abs(r_lsq["C44"] - C44_direct) / (abs(C44_direct) + 1e-30)
        pts.append({"label": label, "rho_eff": S_axial / S_shear,
                    "C11_longwave": r_lsq["C11"], "C11_direct_100": C11_direct, "rel_err_C11": err_C11,
                    "C44_longwave": r_lsq["C44"], "C44_direct_100": C44_direct, "rel_err_C44": err_C44,
                    "AGREE": bool(err_C11 < 1e-3 and err_C44 < 1e-3)})
    return {"points": pts, "ALL_AGREE": bool(all(p["AGREE"] for p in pts))}


def _write(out):
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / "prestress_elastic_tensor.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"\nResults written: {path}")


if __name__ == "__main__":
    main()
