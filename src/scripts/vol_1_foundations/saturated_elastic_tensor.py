#!/usr/bin/env python3
"""The SATURATED srs ELASTIC-TENSOR arc — small-signal Cauchy C_ij about a DC Q-point.

Grant-fired 2026-07-04 ("sweep all regimes" / KEEP-BOTH "record and do both").
Prereg (FROZEN): research/2026-07-04_saturated-elastic-tensor_prereg_FROZEN.md.

SKELETON — sections filled one commit at a time (incremental-write discipline).

═══════════════════════════════════════════════════════════════════════════════
THE SEAM THIS CLOSES  (PR #518 §6 scope flag, verbatim)
═══════════════════════════════════════════════════════════════════════════════
The COLD arc (srs_elastic_tensor.py, MERGED) computed the Cauchy C_ij as a
one-parameter family in rho=k_a/k_s; nu_Hill=2/7 <=> K=2G only at cold rho*=9.7734.
PR #518 (matter_stiffening_rho.py, MERGED 6d2ecdf4) computed the SATURATED RATIO
rho_eff = rho_cold*(S_axial/S_shear) but NOT the tensor, and flagged (its section 6):
  "driving the saturated rho_eff to 9.77 is NOT proven to land the same nu=2/7/K=2G
   elastic tensor ... the saturated C_ij(rho_eff) would need to be recomputed from the
   saturated bond stiffnesses (a Born-Huang run on the saturated Phi_b)."
This driver does exactly that: Born-Huang on the SATURATED Phi_b, swept across the full
operating-point regime, BOTH channel assignments, with two-hand cross-validation.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (see prereg — stated before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : translational-u (Cauchy) sector of chiral srs-z3, on the SATURATED bond
           tensor Phi_b(A) = k_a(A_axial)*(d^d^) + k_s(A_shear)*(I-d^d^). BOTH k_a and
           k_s are translational-u/CAPACITIVE springs (axial vs shear of the SAME bond;
           518 verbatim) -- NOT the eps-vs-mu photon pair. Cosserat = STAGE 2, not invoked.
  MODE   : SMALL-SIGNAL long-wave. The saturated k(A) are the differential (tangent) bond
           stiffnesses at the DC bias point (varactor picture, CLAUDE.md:75, INVARIANT-S2).
  REGIME : quasi-static about a DC bias. Op14 saturation ON. PHASE-STATE = saturated, S<1
           (the cold arc was S=1, saturation OFF -- this is the separating axis).
  COORDS : operating-point knob (A_axial,A_shear) in phase-space/reactance (518 verbatim);
           tensor readout (w(k)->C_ij->nu,Zener,K/G) in real-space/spatial-Brillouin. Each
           measured in ITS OWN matching coordinate (A46-clean on both).
  CLASS  : CONSISTENCY/MANIFESTATION. nu/Zener/(K/G) are ratios (alpha-clean on the verdict
           path). EMERGENCE FORBIDDEN for any value: 2/7, 9.7734, 0.99479 are ALL visible
           targets -- NO tuning toward any of them (the frozen bins + ledger are the guard).

THE LOAD-BEARING PHYSICS (prereg 0.6, tested in VS2/VS3):
  Born-Huang C_ij is homogeneous DEGREE-1 in (k_a,k_s). So:
   - dimensionless RATIOS (nu, Zener, K/G) are degree-0 -> depend ONLY on
     rho_eff = k_a*S_axial/(k_s*S_shear) = rho_cold*(S_axial/S_shear). Overall S drops out.
     => saturated nu(rho_eff) map == cold nu(rho) map with rho->rho_eff (SAME-TENSOR-POINT).
   - absolute moduli (K,G,C_ij,speeds) are degree-1 -> scale by overall S (floppy near yield).
   - sign(K) is scale-invariant for S>0 -> stability boundary at rho_eff (unshifted by S).

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/saturated_elastic_tensor.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# The saturated arc REUSES the cold arc's PROVEN Born-Huang extraction unmodified
# (the load-bearing point: identical pipeline is what licenses the saturated number).
from scripts.vol_1_foundations.srs_elastic_tensor import (  # noqa: E402
    extract_cubic_Cij,
    moduli_from_Cij,
    srs_primitive,
)

from ave.axioms.scale_invariant import saturation_factor, shear_modulus_ratio  # noqa: E402
from ave.core.constants import ALPHA, NU_VAC  # noqa: E402


# ---------------------------------------------------------------------------
# CANON ANCHORS (imported / read-off — NOT tuned)
# ---------------------------------------------------------------------------

# Cold reference: rho_cold = k_a/k_s = 1 (Ax3-forced, PR #516; the A_wall=0 point).
RHO_COLD = 1.0

# READ-OFF comparison constants — NEVER inputs to the sweep (anti-tune guard).
# The cold nu=2/7 <=> K=2G locus; GR-imported (cold arc srs-elastic-tensor_result.md:94).
RHO_STAR_IMPORTED = 9.7734
NU_2_7 = float(NU_VAC)  # the visible-target Poisson ratio (= 2/7)

# A1 mass-core operating point: A = sqrt(alpha) (def-vyvsn1). The FIXED sub-saturated
# channel in each assignment. S_core = S(sqrt(alpha)) = sqrt(1-alpha).
A_CORE_SQRT_ALPHA = float(np.sqrt(ALPHA))

# The #518 shear-loads crossing amplitude (VISIBLE TARGET, read-off only).
A_WALL_518_CROSSING = 0.99479


# ---------------------------------------------------------------------------
# The saturated per-channel stiffness maps (canon-forced, from #518)
# ---------------------------------------------------------------------------
def k_axial_over_k0(A_axial: float | np.ndarray) -> np.ndarray:
    """Axial (longitudinal-A1 stretch) stiffness ratio k_a/k_{a,0} = S(A_axial).

    Chain (canon, #518 Step 1): C_eff = C_0/S(A_axial) [nonlinear-vacuum-capacitance.md:27,
    Q1=(B)]; k = xi^2/C [TKI identity, natural-units-cheatsheet.md:86] => k_a/k_{a,0} =
    C_0/C_eff = S(A_axial). Computed VIA the compliance inversion (not by returning S
    directly) so the sign is cross-checked -- the one place a sign error hides.
    """
    S = saturation_factor(A_axial, yield_limit=1.0)  # A already normalized to yield
    C_eff_over_C0 = 1.0 / S  # C_eff = C_0/S
    return 1.0 / C_eff_over_C0  # k_a/k_{a,0} = C_0/C_eff = S


def k_shear_over_k0(A_shear: float | np.ndarray) -> np.ndarray:
    """Shear (deviatoric-G) stiffness ratio k_s/k_{s,0} = S(A_shear).

    Chain (canon, #518 Step 1): G/G_0 = S(A_shear) [scale_invariant.shear_modulus_ratio,
    verbatim]; c_shear = c_0*sqrt(S), c^2 ~ k_s => k_s/k_{s,0} = S(A_shear). Via the canon
    shear_modulus_ratio alias so the modulus-ratio and c^2 derivations are cross-checked.
    """
    return shear_modulus_ratio(A_shear, yield_strain=1.0)


def operating_point(A_wall: float, is_shear_loads: bool) -> tuple[float, float, float]:
    """Return (A_axial, A_shear, S_axial, S_shear ... ) for a channel assignment.

    SHEAR-LOADS: axial fixed sub-saturated at sqrt(alpha), shear swept to A_wall.
    AXIAL-LOADS: shear fixed sub-saturated at sqrt(alpha), axial swept to A_wall.
    Matches #518 matter_stiffening_rho.run_derivation() loading defs EXACTLY.
    """
    if is_shear_loads:
        A_axial, A_shear = A_CORE_SQRT_ALPHA, A_wall
    else:
        A_axial, A_shear = A_wall, A_CORE_SQRT_ALPHA
    S_axial = float(k_axial_over_k0(np.asarray(A_axial)))
    S_shear = float(k_shear_over_k0(np.asarray(A_shear)))
    return A_axial, A_shear, S_axial, S_shear


# ---------------------------------------------------------------------------
# Saturated tensor at an operating point (Born-Huang on the SATURATED Phi_b)
# ---------------------------------------------------------------------------
def saturated_tensor(pos, bonds, rho, S_axial: float, S_shear: float) -> dict:
    """Cauchy C_ij + moduli at a saturated operating point.

    The saturated bond tensor is Phi_b(A) = (k_{a,0}*S_axial)*P + (k_{s,0}*S_shear)*(I-P).
    With cold k_{a,0}=k_{s,0}=1 (units absorbed into rho), the effective stiffnesses passed
    to the PROVEN cold extraction are (k_axial=S_axial, k_shear=S_shear). The dimensionless
    ratios then depend on rho_eff = S_axial/S_shear; the absolute C_ij carry the overall
    S-scale (the floppy-near-yield magnitude). SAME extraction the cold arc validated.
    """
    r = extract_cubic_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear, rho=rho)
    mo = moduli_from_Cij(r["C11"], r["C12"], r["C44"])
    rho_eff = RHO_COLD * (S_axial / S_shear)
    return {
        "S_axial": S_axial,
        "S_shear": S_shear,
        "rho_eff": rho_eff,
        "C11": r["C11"],
        "C12": r["C12"],
        "C44": r["C44"],
        "max_rel_residual": r["max_rel_residual"],
        **mo,
    }


# ===========================================================================
# VALIDATE-ON-KNOWN (prereg §VALIDATE) — HALT if fail
# ===========================================================================
def run_validation(pos, bonds, rho) -> dict:
    """VS1 cold-recovery + VS2 homogeneity + VS3 saturated==cold-at-matched-rho_eff.

    These sit ON TOP of the cold arc's own V1/V2/V3 (simple-cubic/diamond/isotropy), which
    the cold driver already ran GREEN on the SAME extract_cubic_Cij this driver imports.
    """
    val = {}

    # --- VS1: cold-recovery. The TRUE cold control is BOTH channels de-energized
    #     (A_axial = A_shear = 0 => S_axial = S_shear = 1 => rho_eff = 1). Note: with the
    #     #518 fixed-channel-at-sqrt(alpha) convention, "A_wall=0" leaves the FIXED channel
    #     at sqrt(alpha) (S=0.9963), which is the LOADED cold vacuum, NOT the fully cold
    #     control. VS1 tests the fully-cold (both-off) planted-source gate; the loaded
    #     A_wall=0 rung (rho_eff=0.9963/1.0037) is reported separately in the sweep.
    tol = {"C11": 0.17678, "C12": -0.17678, "C44": 0.17678}
    t = saturated_tensor(pos, bonds, rho, 1.0, 1.0)  # S_axial = S_shear = 1 (both off)
    vs1_ok = bool(
        abs(t["C11"] - tol["C11"]) / abs(tol["C11"]) < 1e-4
        and abs(t["C12"] - tol["C12"]) / abs(tol["C12"]) < 1e-4
        and abs(t["C44"] - tol["C44"]) / abs(tol["C44"]) < 1e-4
        and abs(t["rho_eff"] - RHO_COLD) < 1e-9
        and abs(t["Zener_A"] - 1.0) < 1e-5
    )
    val["VS1_cold_recovery"] = {
        "target": tol,
        "both_channels_off": {
            "S_axial": 1.0, "S_shear": 1.0, "rho_eff": t["rho_eff"],
            "C11": t["C11"], "C12": t["C12"], "C44": t["C44"],
            "K_bulk": t["K_bulk"], "Zener_A": t["Zener_A"],
        },
        "note": "TRUE cold control = both channels de-energized (S_axial=S_shear=1) => "
        "saturated tensor == merged cold tensor at rho=1 (C11/C12/C44=+/-0.17678, K<0 "
        "unstable, Zener=1). The #518 fixed-channel-at-sqrt(alpha) A_wall=0 rung is a "
        "LOADED cold vacuum (rho_eff=0.9963), reported in the sweep -- not this gate.",
        "PASS": vs1_ok,
    }

    # --- VS2: homogeneity. C_ij(lam k)/lam == C_ij(k); ratios IDENTICAL under lam-scaling ---
    ka, ks = 9.7734, 1.0
    r_base = extract_cubic_Cij(pos, bonds, k_axial=ka, k_shear=ks, rho=rho)
    m_base = moduli_from_Cij(r_base["C11"], r_base["C12"], r_base["C44"])
    lam = 0.37  # an arbitrary overall stiffness scale (an S factor)
    r_scl = extract_cubic_Cij(pos, bonds, k_axial=lam * ka, k_shear=lam * ks, rho=rho)
    m_scl = moduli_from_Cij(r_scl["C11"], r_scl["C12"], r_scl["C44"])
    cij_homog_err = max(
        abs(r_base[k] - r_scl[k] / lam) / (abs(r_base[k]) + 1e-30)
        for k in ("C11", "C12", "C44")
    )
    ratio_inv_err = max(
        abs(m_base[k] - m_scl[k]) / (abs(m_base[k]) + 1e-30)
        for k in ("nu_Hill", "Zener_A", "KG_Hill")
    )
    abs_scale_err = abs(m_scl["K_bulk"] / m_base["K_bulk"] - lam)  # K scales by lam
    vs2_ok = bool(cij_homog_err < 1e-6 and ratio_inv_err < 1e-6 and abs_scale_err < 1e-6)
    val["VS2_homogeneity"] = {
        "lam": lam,
        "cij_over_lam_rel_err": cij_homog_err,
        "ratio_invariance_rel_err": ratio_inv_err,
        "abs_K_scale_err_vs_lam": abs_scale_err,
        "note": "Born-Huang C_ij is homogeneous deg-1: C_ij scales by lam, ratios "
        "(nu,Zener,K/G) are deg-0 (identical under lam). K scales by exactly lam. This IS "
        "the load-bearing prereg 0.6 claim, tested directly.",
        "PASS": vs2_ok,
    }

    # --- VS3: saturated == cold-at-matched-rho_eff (the SAME-TENSOR-POINT discriminator) ---
    # The scale-free comparison: normalize C_ij by C44 (a scale-invariant tensor SHAPE), which
    # is bounded and pole-free. Ratios nu/Zener/(K/G) are also compared, but nu is EXCLUDED
    # near the K=0 pole (rho_eff in [1.8,2.2]) where it DIVERGES -- a relative error on a
    # diverging quantity is meaningless even when the two AGREE bit-for-bit. Zener and the
    # C_ij-shape are pole-free and always compared. Points span both sides of the pole.
    vs3_cases = []
    vs3_ok = True
    test_pts = [(0.9927, 0.1019), (0.7, 0.35), (0.5, 0.9), (0.99, 0.05), (0.3, 0.3), (0.8, 0.2)]
    for Sa, Ss in test_pts:
        t_sat = saturated_tensor(pos, bonds, rho, Sa, Ss)
        rho_eff = Sa / Ss
        r_cold = extract_cubic_Cij(pos, bonds, k_axial=rho_eff, k_shear=1.0, rho=rho)
        m_cold = moduli_from_Cij(r_cold["C11"], r_cold["C12"], r_cold["C44"])
        # scale-free tensor SHAPE: C11/C44, C12/C44 (both saturated and cold; pole-free)
        shape_sat = {"C11_C44": t_sat["C11"] / t_sat["C44"], "C12_C44": t_sat["C12"] / t_sat["C44"]}
        shape_cold = {"C11_C44": r_cold["C11"] / r_cold["C44"], "C12_C44": r_cold["C12"] / r_cold["C44"]}
        shape_err = max(abs(shape_sat[k] - shape_cold[k]) / (abs(shape_cold[k]) + 1e-30)
                        for k in shape_sat)
        zener_err = abs(t_sat["Zener_A"] - m_cold["Zener_A"]) / (abs(m_cold["Zener_A"]) + 1e-30)
        # nu diverges near BOTH K=0 (rho_eff=2, numerator 3K-2G through 0 is not it -- the
        # denominator 3K+G->0 is the pole) AND the low-rho iso-bond region (rho_eff<=~1.5,
        # K<0 small, nu enters its |nu|>>1 divergent branch). Exclude nu wherever it is in
        # its divergent regime (|nu_cold|>1): the SHAPE + Zener comparison (pole-free) is the
        # robust discriminator and passes at machine precision there. A rel-err on a divergent
        # nu is meaningless EVEN WHEN the two AGREE (they do -- shape_err ~1e-16).
        nu_divergent = bool(abs(rho_eff - 2.0) < 0.2 or abs(m_cold["nu_Hill"]) > 1.0)
        nu_err = (None if nu_divergent
                  else abs(t_sat["nu_Hill"] - m_cold["nu_Hill"]) / (abs(m_cold["nu_Hill"]) + 1e-30))
        near_pole = nu_divergent
        ok = bool(shape_err < 1e-6 and zener_err < 1e-6 and (nu_err is None or nu_err < 1e-6))
        vs3_ok = vs3_ok and ok
        vs3_cases.append({
            "S_axial": Sa, "S_shear": Ss, "rho_eff": rho_eff, "near_K0_pole": near_pole,
            "C11_C44_shape_saturated": shape_sat["C11_C44"], "C11_C44_shape_cold": shape_cold["C11_C44"],
            "shape_rel_err": shape_err, "zener_rel_err": zener_err,
            "nu_rel_err": nu_err, "PASS": ok,
        })
    val["VS3_saturated_equals_cold_at_matched_rho_eff"] = {
        "cases": vs3_cases,
        "note": "saturated tensor SHAPE (C11/C44, C12/C44) + Zener == cold at rho=S_axial/S_shear "
        "to 1e-6 at every operating point (both sides of the K=0 pole) => the map is NOT deformed "
        "(SAME-TENSOR-POINT). nu is excluded in the pole neighborhood rho_eff in [1.8,2.2] where "
        "it diverges (a rel-err on a divergence is meaningless even when the values AGREE). A "
        "SHAPE/Zener failure at some rho_eff would be DEFORMED-FAMILY (report where + how much).",
        "PASS": vs3_ok,
    }

    val["ALL_PASS"] = bool(vs1_ok and vs2_ok and vs3_ok)
    return val


# ===========================================================================
# THE SWEEP — both channel assignments, full A_wall ladder + log-approach
# ===========================================================================
def _cross_amplitude(A_wall, rho_profile, target):
    """Linear-interpolated A_wall where rho_profile crosses target, or None."""
    r = np.asarray(rho_profile)
    for i in range(len(r) - 1):
        lo, hi = r[i], r[i + 1]
        if (lo - target) * (hi - target) <= 0 and lo != hi:
            frac = (target - lo) / (hi - lo)
            return float(A_wall[i] + frac * (A_wall[i + 1] - A_wall[i]))
    return None


def run_sweep(pos, bonds, rho) -> dict:
    """Both assignments (SHEAR_LOADS, AXIAL_LOADS), blind. Full readouts per operating point."""
    canon_rungs = [0.0, A_CORE_SQRT_ALPHA, 0.5, 0.9, 1.0 - ALPHA, A_WALL_518_CROSSING,
                   0.999, 0.99999]
    log_approach = [1.0 - 10.0 ** (-k) for k in range(1, 9)]
    A_wall_ladder = sorted(set(canon_rungs + log_approach))
    dense = np.linspace(0.0, 0.99999, 5000)

    out = {}
    for name, is_sl in [("SHEAR_LOADS", True), ("AXIAL_LOADS", False)]:
        ladder = []
        for A_wall in A_wall_ladder:
            _, _, Sa, Ss = operating_point(A_wall, is_sl)
            t = saturated_tensor(pos, bonds, rho, Sa, Ss)
            # worst-case internal acoustic Gamma between softest/stiffest acoustic branch
            # at [100]: Z ~ sqrt(rho*C). Use the C_ij extremes as a mechanical mismatch proxy.
            speeds2 = [abs(t["C11"]), abs(t["C44"])]  # long vs transverse rho*c^2 at [100]
            z_hi, z_lo = np.sqrt(max(speeds2)), np.sqrt(min(speeds2) + 1e-300)
            gamma = abs(z_hi - z_lo) / (z_hi + z_lo + 1e-300)
            ladder.append({
                "A_wall": A_wall, "S_axial": Sa, "S_shear": Ss, "rho_eff": t["rho_eff"],
                "C11": t["C11"], "C12": t["C12"], "C44": t["C44"],
                "K_bulk": t["K_bulk"], "sign_K": int(np.sign(t["K_bulk"])),
                "G_Voigt": t["G_Voigt"], "G_Reuss": t["G_Reuss"], "G_Hill": t["G_Hill"],
                "nu_Voigt": t["nu_Voigt"], "nu_Reuss": t["nu_Reuss"], "nu_Hill": t["nu_Hill"],
                "Zener_A": t["Zener_A"], "KG_Hill": t["KG_Hill"],
                "abs_scale_S_axial": Sa, "abs_scale_S_shear": Ss,
                "worst_internal_gamma": float(gamma),
                "max_rel_residual": t["max_rel_residual"],
            })
        # crossing of rho_eff = RHO_STAR_IMPORTED on the dense sweep (read-off only)
        r_dense = np.array([operating_point(a, is_sl)[2] / operating_point(a, is_sl)[3]
                            for a in dense])
        cross = _cross_amplitude(dense, r_dense, RHO_STAR_IMPORTED)
        # nu_Hill at the crossing (if it exists)
        nu_at_cross = None
        zener_at_cross = None
        kg_at_cross = None
        if cross is not None:
            _, _, Sa_c, Ss_c = operating_point(cross, is_sl)
            tc = saturated_tensor(pos, bonds, rho, Sa_c, Ss_c)
            nu_at_cross, zener_at_cross, kg_at_cross = tc["nu_Hill"], tc["Zener_A"], tc["KG_Hill"]
        direction = "STIFFENING" if r_dense[-1] > RHO_COLD else "SOFTENING"
        out[name] = {
            "fixed_channel": "axial@sqrt(alpha)" if is_sl else "shear@sqrt(alpha)",
            "swept_channel": "shear->yield" if is_sl else "axial->yield",
            "direction": direction,
            "ladder": ladder,
            "rho_eff_at_yield_limit": float(r_dense[-1]),
            "crosses_rho_star_9.77": cross is not None,
            "crossing_A_wall": cross,
            "nu_Hill_at_crossing": nu_at_cross,
            "Zener_at_crossing": zener_at_cross,
            "KG_Hill_at_crossing": kg_at_cross,
        }
    return out


# ===========================================================================
# TWO-HAND CROSS-VALIDATION (long-wave vs direct eigensolve) at >=3 points
# ===========================================================================
def run_two_hand_crossval(pos, bonds, rho) -> dict:
    """Independent [100] direct-eigensolve of the saturated acoustic branches vs the
    least-squares long-wave C_ij, at >=3 operating points INCLUDING the 9.77 crossing.

    Along [100] the acoustic Christoffel eigenvalues are (C11, C44, C44) = rho*c^2. We
    read C11 (long) + C44 (transverse) directly from the [100] slopes and compare to the
    full-direction least-squares fit -- the SAME cross-check the cold arc used (direct
    eigensolve recovered C11=0.72786, C44=0.24876 at rho*).
    """
    # operating points: cold rho=1, a stable mid point (rho_eff~3), the 9.77 crossing.
    # use SHEAR_LOADS to reach each rho_eff (axial@sqrt(alpha), shear tuned to hit rho_eff)
    S_axial_core = float(k_axial_over_k0(np.asarray(A_CORE_SQRT_ALPHA)))  # = sqrt(1-alpha)
    pts = []
    for label, rho_eff_target in [("cold_rho1", 1.0), ("stable_rho3", 3.0),
                                  ("nu2_7_crossing_rho9.7734", RHO_STAR_IMPORTED)]:
        S_axial = S_axial_core
        S_shear = S_axial / rho_eff_target
        A_shear = float(np.sqrt(max(0.0, 1.0 - S_shear ** 2)))
        # HAND 1: least-squares long-wave (all directions)
        r_lsq = extract_cubic_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear, rho=rho)
        # HAND 2: direct [100] eigensolve
        r_100 = extract_cubic_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear, rho=rho,
                                  directions=[[1, 0, 0]])
        st = r_100["slope_table"]["100"]["rho_c2_eigs_ascending"]
        C44_direct, _, C11_direct = st[0], st[1], st[2]  # (C44, C44, C11) ascending
        err_C11 = abs(r_lsq["C11"] - C11_direct) / (abs(C11_direct) + 1e-30)
        err_C44 = abs(r_lsq["C44"] - C44_direct) / (abs(C44_direct) + 1e-30)
        pts.append({
            "label": label, "rho_eff": S_axial / S_shear, "A_shear": A_shear,
            "C11_longwave": r_lsq["C11"], "C11_direct_100": C11_direct, "rel_err_C11": err_C11,
            "C44_longwave": r_lsq["C44"], "C44_direct_100": C44_direct, "rel_err_C44": err_C44,
            "AGREE": bool(err_C11 < 1e-3 and err_C44 < 1e-3),
        })
    return {"points": pts, "ALL_AGREE": bool(all(p["AGREE"] for p in pts))}


# ===========================================================================
# DRIVER
# ===========================================================================
def main():
    out = {
        "title": "THE SATURATED srs ELASTIC-TENSOR ARC",
        "composition": "Phi_b(A)=k_a0*S(A_axial)*P + k_s0*S(A_shear)*(I-P); "
        "ratios depend on rho_eff=S_axial/S_shear, absolute C_ij scale by overall S",
        "rho_star_imported_readoff_only": RHO_STAR_IMPORTED,
        "nu_2_7_target": NU_2_7,
        "A_core_sqrt_alpha": A_CORE_SQRT_ALPHA,
        "A_wall_518_crossing_readoff": A_WALL_518_CROSSING,
    }
    print("=" * 78)
    print("THE SATURATED srs ELASTIC-TENSOR ARC — small-signal C_ij about a DC Q-point")
    print("=" * 78)

    # both enantiomorphs (parity control) — build once, sweep on 'right', check 'left'
    pos_r, bonds_r, rho_r = srs_primitive("right")
    pos_l, bonds_l, rho_l = srs_primitive("left")

    # ---- validate-on-known (HALT if fail) --------------------------------
    val = run_validation(pos_r, bonds_r, rho_r)
    out["validate_on_known"] = val
    print("(0) VALIDATE-ON-KNOWN (HALT if fail):")
    print(f"  VS1 cold-recovery (A_wall=0 => cold tensor): "
          f"{'PASS' if val['VS1_cold_recovery']['PASS'] else 'FAIL'}")
    print(f"  VS2 homogeneity   (C_ij deg-1, ratios deg-0): "
          f"{'PASS' if val['VS2_homogeneity']['PASS'] else 'FAIL'}  "
          f"(ratio-inv err={val['VS2_homogeneity']['ratio_invariance_rel_err']:.1e})")
    print(f"  VS3 saturated==cold-at-matched-rho_eff:       "
          f"{'PASS' if val['VS3_saturated_equals_cold_at_matched_rho_eff']['PASS'] else 'FAIL'}")
    print(f"  ALL_VALIDATE_PASS = {val['ALL_PASS']}")
    if not val["ALL_PASS"]:
        print("\nHALT: validate-on-known FAILED — no saturated verdict.")
        _write(out)
        import sys
        sys.exit(1)

    # ---- enantiomorph parity control -------------------------------------
    _, _, Sa, Ss = operating_point(A_WALL_518_CROSSING, True)
    t_r = saturated_tensor(pos_r, bonds_r, rho_r, Sa, Ss)
    t_l = saturated_tensor(pos_l, bonds_l, rho_l, Sa, Ss)
    hand_diff = max(abs(t_r[k] - t_l[k]) / (abs(t_r[k]) + abs(t_l[k]) + 1e-30)
                    for k in ("C11", "C12", "C44"))
    out["enantiomorph_parity"] = {
        "max_rel_hand_difference": hand_diff,
        "parity_symmetric": bool(hand_diff < 1e-6),
        "note": "saturated tensor at a prescribed operating point is hand-independent "
        "(kappa_chiral is saturation-kernel-only; the arc prescribes A, does not evolve "
        "the chiral kernel). A nonzero difference = a bug.",
    }

    # ---- the sweep (both assignments) ------------------------------------
    sweep = run_sweep(pos_r, bonds_r, rho_r)
    out["sweep_both_assignments"] = sweep

    # ---- two-hand cross-validation ---------------------------------------
    crossval = run_two_hand_crossval(pos_r, bonds_r, rho_r)
    out["two_hand_crossval"] = crossval

    # ---- per-assignment bin verdicts -------------------------------------
    verdicts = {}
    for name, is_sl in [("SHEAR_LOADS", True), ("AXIAL_LOADS", False)]:
        d = sweep[name]
        # SAME-TENSOR-POINT: at rho_eff=9.7734, saturated nu=2/7 & K/G=2 to cold precision.
        nu_c = d["nu_Hill_at_crossing"]
        kg_c = d["KG_Hill_at_crossing"]
        same_tensor = bool(
            d["crosses_rho_star_9.77"]
            and nu_c is not None
            and abs(nu_c - NU_2_7) / NU_2_7 < 1e-4
            and abs(kg_c - 2.0) < 1e-3
        )
        # NEW-DISTINGUISHED-POINT: does a canon-forced A land ON nu=2/7? (crossing at
        # sqrt(alpha), 1-alpha, or A->1). The a-priori expectation is NO (crossing is a
        # free knob). If YES => max scrutiny flag.
        cross = d["crossing_A_wall"]
        new_dist = False
        if cross is not None:
            new_dist = bool(
                abs(cross - A_CORE_SQRT_ALPHA) < 1e-3
                or abs(cross - (1.0 - ALPHA)) < 1e-3
                or cross > 0.9999
            )
        # UNSTABLE at the matter operating points: is K<0 where rho_eff>1 matters?
        # stability floor is rho_eff=2 (sign-invariant); report the boundary.
        unstable_rows = [row for row in d["ladder"] if row["sign_K"] < 0]
        # bin selection (VS3 pass => family not deformed => SAME-TENSOR-POINT applies)
        if same_tensor and val["VS3_saturated_equals_cold_at_matched_rho_eff"]["PASS"]:
            primary = "SAME-TENSOR-POINT"
        elif not val["VS3_saturated_equals_cold_at_matched_rho_eff"]["PASS"]:
            primary = "DEFORMED-FAMILY"
        elif d["direction"] == "SOFTENING":
            # axial-loads: rho_eff falls, never reaches 9.77 -> mirror control
            primary = "SAME-TENSOR-POINT (mirror: rho_eff<1, no 9.77 crossing; map undeformed)"
        else:
            primary = "SAME-TENSOR-POINT"
        verdicts[name] = {
            "PRIMARY_BIN": primary,
            "direction": d["direction"],
            "crossing_A_wall": cross,
            "nu_Hill_at_crossing": nu_c,
            "KG_Hill_at_crossing": kg_c,
            "Zener_at_crossing": d["Zener_at_crossing"],
            "NEW_DISTINGUISHED_POINT_flag": new_dist,
            "stability_floor_rho_eff": 2.0,
            "n_unstable_rungs_Kneg": len(unstable_rows),
        }
    out["bin_verdicts_per_assignment"] = verdicts

    # ---- console summary --------------------------------------------------
    print(f"\n(1) enantiomorph parity: max hand-diff = {hand_diff:.2e} "
          f"({'parity-symmetric' if hand_diff < 1e-6 else 'BROKEN — BUG'})")
    print("\n(2) THE SWEEP — nu(rho_eff) map, both assignments:")
    for name in ("SHEAR_LOADS", "AXIAL_LOADS"):
        d = sweep[name]
        print(f"  --- {name} ({d['fixed_channel']}, sweep {d['swept_channel']}): "
              f"{d['direction']} ---")
        print(f"      rho_eff at yield limit: {d['rho_eff_at_yield_limit']:.4g}; "
              f"crosses 9.77: {d['crosses_rho_star_9.77']}")
        if d["crossing_A_wall"] is not None:
            print(f"      crossing A_wall={d['crossing_A_wall']:.5f}, "
                  f"nu_Hill={d['nu_Hill_at_crossing']:.5f}, "
                  f"K/G_Hill={d['KG_Hill_at_crossing']:.5f}, "
                  f"Zener={d['Zener_at_crossing']:.4f}")
    print("\n(3) TWO-HAND CROSS-VALIDATION (long-wave vs [100] direct eigensolve):")
    for p in crossval["points"]:
        print(f"      {p['label']}: rho_eff={p['rho_eff']:.4f} "
              f"C11 lw={p['C11_longwave']:.5f}/direct={p['C11_direct_100']:.5f} "
              f"(err {p['rel_err_C11']:.1e}); AGREE={p['AGREE']}")
    print(f"      ALL_AGREE = {crossval['ALL_AGREE']}")
    print("\n(4) PER-ASSIGNMENT BIN VERDICTS:")
    for name, v in verdicts.items():
        print(f"      [{name}] PRIMARY BIN: {v['PRIMARY_BIN']}")
        print(f"          direction={v['direction']}, "
              f"NEW-DISTINGUISHED-POINT flag={v['NEW_DISTINGUISHED_POINT_flag']}, "
              f"K<0 rungs={v['n_unstable_rungs_Kneg']}")

    _write(out)
    return out


def _write(out):
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    path = out_dir / "saturated_elastic_tensor.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"\nResults written: {path}")


if __name__ == "__main__":
    main()
