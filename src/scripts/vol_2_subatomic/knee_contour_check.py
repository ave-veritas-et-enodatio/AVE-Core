#!/usr/bin/env python3
"""
KNEE-CONTOUR vs COLLAR-EDGE CHECK — registered check from Grant's F5 walk (2026-07-14).
======================================================================================

Research note (hypothesis-first, verdict classes declared BEFORE the numbers):
    research/2026-07-14_knee-contour-check_NOTE.md

THE ONE QUESTION: is the #693 screening-sum gate's COLLAR edge (its near-dress
structure — the region within ~10 d_sat of a probe carrying ~100% of the coupling
correction, with induced-dipole density falling ~s^-6 beyond) the KNEE CONTOUR — the
radius where a unit probe's local field amplitude crosses A = sqrt(2*alpha) (the
DeltaS=alpha proportional limit; engine authority `chiral_lattice_v10.py:29-30`
A_YIELD_SQ = 2*ALPHA, kernel S=sqrt(1-A^2) at `:56`; = constants.R_I, the
Linear->Non-Linear regime boundary)?

Sector header — MODE static two-body TRANSFER coupling through a self-consistent
polarizable medium (the #693 gate, unmodified); REGIME cold, KERNEL ON (Op14/Ax4
saturation sets per-cell polarizability); PHASE-STATE sub-yield perturbative;
SECTOR **E-sector static dielectric** (the induced-dipole screening cloud), TRANSFER
register. No new ENGINE — this is a pure re-analysis of the merged #693 solver
(imported unmodified). No physics constants are hard-coded: ALPHA / L_NODE / R_I come
from `ave.core.constants`, the yield amplitude from `constants.R_I`.

★ AMPLITUDE DISCIPLINE (load-bearing, do-not-invent-a-field-measure). The A(s) this
check measures is the SAME amplitude the #693 kernel consumes:
    driver `qed_trace_screening_sum_gate.py:236`  A = |E_total| / E_yield
    driver `:219`                                  E_yield = K / d_sat^2
so for a unit probe (|E_probe| = K/s^2) the kernel-consumed amplitude is the
FIELD-strain A = (d_sat/s)^2. The `_chi_sat` kernel (driver `:189-191`,
chi = 1/sqrt(1-A^2) - 1) and the S=sqrt(1-A^2) yield kernel both zero at A=1
(rupture, R_III); the KNEE at A=R_I=sqrt(2*alpha) is where S=sqrt(1-2*alpha)~=1-alpha,
i.e. DeltaS = alpha (the proportional limit).

★ FLAGGED FORK (flag-don't-fix, see NOTE): the canonical corpus leaf
`vol2/proofs-computation/ch09-computational-proof/methodological-contamination.md:48-52`
defines the strain as the VOLTAGE-strain A_V = V/V_snap = d_sat/r (~1/r) and compares
IT to the same sqrt(2*alpha) knee. Field-strain and voltage-strain give different knee
radii; this check reports BOTH but the PRIMARY is the driver's kernel-consumed
field-strain (per the amplitude-discipline rule above).

Run: PYTHONPATH=src python src/scripts/vol_2_subatomic/knee_contour_check.py
Fast: ... --smoke
"""
from __future__ import annotations

import argparse
import json

import numpy as np

from ave.core.constants import ALPHA, L_NODE, R_I
from ave_path_util import sim_output

# import the MERGED #693 solver UNMODIFIED (no re-implementation of any stencil/kernel)
from scripts.vol_2_subatomic.qed_trace_screening_sum_gate import (
    D_SAT,
    K,
    NEAR_R,
    _rand_rot,
    build_cells,
    solve,
    transfer_alpha,
)

# ── yield / knee amplitude (canonical, imported) ─────────────────────────────
A_YIELD = float(R_I)          # = sqrt(2*ALPHA); chiral_lattice_v10.py:29 A_YIELD_SQ=2*ALPHA
E_YIELD = K / D_SAT ** 2       # driver :219 — the field at which A=1 (rupture, R_III)

# ── UNIT MAP d_sat <-> ell_node (VERIFIED from corpus, NOT assumed) ───────────
# The #693 driver is scale-free in d_sat (d_sat=1 native; it never pins a physical
# length). The physical identification comes from the canonical corpus:
#   `methodological-contamination.md:46`: "The topological saturation radius of the
#    electron defines its structural limit as d_sat = l_node."
# so 1 d_sat = 1 ell_node exactly (a 1:1 map). L_NODE is imported for the SI readout.
DSAT_IN_LNODE = 1.0            # canonical: d_sat == ell_node (methodological-contamination.md:46)

# ── verdict-class thresholds (DECLARED BEFORE THE COMPUTATION; no answer-shaping) ─
# MATCH   : s_knee within a factor ~2 of the 90%-correction radius (the knee IS the
#           dress edge — the contour becomes a measured surface)
# PARTIAL : same order, factor 2-5 (related but not identical; report both numbers)
# NO-MATCH: >5x apart (the collar is set by something else; report what amplitude the
#           collar edge corresponds to)
MATCH_FACTOR = 2.0
PARTIAL_FACTOR = 5.0


def classify(s_knee: float, r_collar: float) -> str:
    """Verdict class from the ratio of the knee radius to the 90%-correction radius.
    Thresholds frozen above BEFORE any number was computed."""
    if s_knee <= 0 or r_collar <= 0:
        return "UNDEFINED"
    ratio = max(s_knee / r_collar, r_collar / s_knee)
    if ratio <= MATCH_FACTOR:
        return "MATCH"
    if ratio <= PARTIAL_FACTOR:
        return "PARTIAL"
    return "NO-MATCH"


# ── inverse read: S and Gamma at a given field-strain amplitude ──────────────
def kernel_S(A: float) -> float:
    """Axiom-4 saturation kernel S(A) = sqrt(1 - A^2) (same kernel the driver's
    _chi_sat consumes; chiral_lattice_v10.py:56). A here is the FIELD-strain."""
    return float(np.sqrt(1.0 - min(A, 1.0 - 1e-15) ** 2))


def reflection_Gamma(S: float) -> float:
    """E-SECTOR STATIC-DIELECTRIC reflection coefficient (Op14 Meissner-asymmetric).
    A static-E-only drive loads the epsilon sector only: eps_eff = eps_0 * S, mu
    unloaded, so Z_eff = sqrt(mu_0/(eps_0 S)) = Z_0 / sqrt(S) (AVE-KB CLAUDE.md
    INVARIANT-S2, `operators.md:54` asymmetric form). Then
        Gamma = (Z_eff - Z_0)/(Z_eff + Z_0) = (1 - sqrt(S)) / (1 + sqrt(S)).
    CONVENTION STATED (not corpus-quoted): the static-E asymmetric load, matching this
    check's E-sector sector header. At A->0, S->1, Gamma->0 (unsaturated => reflectionless)."""
    rS = np.sqrt(S)
    return float((1.0 - rS) / (1.0 + rS))


def _crossing(s_sorted: np.ndarray, y_sorted: np.ndarray, y_target: float) -> float:
    """First radius where the monotone-decreasing y(s) crosses y_target, log-log
    interpolated. Returns nan if no crossing in range."""
    below = y_sorted < y_target
    if not below.any() or below.all():
        return float("nan")
    i = int(np.argmax(below))  # first index where y < target
    if i == 0:
        return float("nan")
    x0, x1 = np.log(s_sorted[i - 1]), np.log(s_sorted[i])
    z0, z1 = np.log(y_sorted[i - 1]), np.log(y_sorted[i])
    zt = np.log(y_target)
    frac = (zt - z0) / (z1 - z0)
    return float(np.exp(x0 + frac * (x1 - x0)))


# ═════════════════════════════════════════════════════════════════════════════
# (1) A(s) PROFILE around a SINGLE unit probe + s_knee
# ─────────────────────────────────────────────────────────────────────────────
# A single probe is isolated by the driver's own q=(1,0) solve (only probe-1 sources
# the probe field; the mesh, kernel, SCF are the merged solver, unmodified). The
# amplitude read is A = |E_total|/E_yield at each cell (driver :236), restricted to
# probe-1's domain (cells nearer probe-1 than probe-2).
# ═════════════════════════════════════════════════════════════════════════════
def single_probe_profile(R: float, alpha0: float, *, n_r: int, n_ang: int,
                         rot: np.ndarray | None = None) -> dict:
    mesh = build_cells(R, n_r=n_r, n_ang=n_ang, rot=rot)
    sol = solve(mesh, R, alpha0, q=(1.0, 0.0))   # single probe-1 sources; SCF, kernel ON
    cells, E, p, spac = sol["cells"], sol["E"], sol["p"], sol["spac"]
    c1, c2 = mesh["centers"][0], mesh["centers"][1]
    d1 = np.linalg.norm(cells - c1, axis=1)
    d2 = np.linalg.norm(cells - c2, axis=1)
    own = d1 < d2                                 # probe-1's own cloud
    s = d1[own]
    A = np.linalg.norm(E, axis=1)[own] / E_YIELD  # EXACT kernel-consumed amplitude (:236)
    # induced-dipole DENSITY |p|/vol (the s^-6 quantity); vol recovered from shell spacing
    vol = spac[own] ** 3
    dens = np.linalg.norm(p, axis=1)[own] / np.maximum(vol, 1e-300)
    order = np.argsort(s)
    s, A, dens = s[order], A[order], dens[order]
    # de-duplicate shells (each shell has n_ang cells at ~identical s): average per shell
    us, inv = np.unique(np.round(np.log(s), 6), return_inverse=True)
    s_sh = np.array([s[inv == k].mean() for k in range(len(us))])
    A_sh = np.array([A[inv == k].mean() for k in range(len(us))])
    dens_sh = np.array([dens[inv == k].mean() for k in range(len(us))])
    return {"R": R, "converged": bool(sol["converged"]), "n_r": n_r, "n_ang": n_ang,
            "s": s_sh, "A": A_sh, "dens": dens_sh}


def knee_from_profile(prof: dict) -> dict:
    s, A = prof["s"], prof["A"]
    s_knee_meas = _crossing(s, A, A_YIELD)
    # bare-field reference A_bare = (d_sat/s)^2  -> s_knee = d_sat / (2a)^{1/4}
    s_knee_bare = float(D_SAT * A_YIELD ** -0.5)
    return {"s_knee_field_measured_dsat": s_knee_meas,
            "s_knee_field_bare_dsat": s_knee_bare,
            # canonical-corpus voltage-strain alternative (FLAGGED, not primary):
            # A_V = d_sat/s crosses sqrt(2a) at s = d_sat / sqrt(2a)
            "s_knee_voltage_dsat_FLAGGED": float(D_SAT / A_YIELD)}


def s6_onset(prof: dict, target_slope: float = -6.0, tol: float = 0.3) -> float:
    """Radius (from small s outward) where the local log-log slope of the induced-dipole
    DENSITY reaches the s^-6 asymptote within `tol`. Below this the response is saturated
    (chi diverges); at/above it chi->A^2/2 and density ~ s^-6."""
    s, d = prof["s"], prof["dens"]
    good = d > 0
    s, d = s[good], d[good]
    if len(s) < 3:
        return float("nan")
    ls, ld = np.log(s), np.log(d)
    slope = np.gradient(ld, ls)
    for k in range(len(slope) - 1):
        if abs(slope[k] - target_slope) <= tol:
            return float(s[k])
    return float("nan")


def _cross_up(x: np.ndarray, y: np.ndarray, y_target: float) -> float:
    """First x where the monotone-increasing y(x) reaches y_target, log-x interpolated.
    Returns x[0] if already at/above target at the innermost point (unresolved-at-wall),
    nan if never reached."""
    x, y = np.asarray(x), np.asarray(y)
    if y[-1] < y_target:
        return float("nan")
    if y[0] >= y_target:
        return float(x[0])
    i = int(np.argmax(y >= y_target))
    y0, y1 = y[i - 1], y[i]
    lx0, lx1 = np.log(x[i - 1]), np.log(x[i])
    frac = (y_target - y0) / (y1 - y0) if y1 != y0 else 0.0
    return float(np.exp(lx0 + frac * (lx1 - lx0)))


# ═════════════════════════════════════════════════════════════════════════════
# (3) ENCLOSED-CORRECTION profile -> collar radii (50/90/99%)
# ─────────────────────────────────────────────────────────────────────────────
# The coupling-correction contribution enclosed within radius s_cut of a probe, from the
# SAME decomposition machinery as the #693 genuineness_decomposition (driver
# transfer_alpha with a radial keep-mask dmin<=s_cut). enclosed(s_cut) =
# (alpha_eff(dmin<=s_cut) - 1)/(alpha_eff_full - 1). Orientation-averaged.
#
# ★ R + n_r are load-bearing for the near-wall RESOLUTION (the #693 review flagged
# resolution-dependence). The correction is carried by the near-SATURATED inner shell
# (A -> 1 at the Pauli wall, chi diverges), so R is chosen SMALL (30 = frozen-window
# minimum -> densest near-wall log-shells) and n_r is swept for the discretization report.
# ═════════════════════════════════════════════════════════════════════════════
def enclosed_correction(R: float, alpha0: float, *, n_orient: int, n_cut: int,
                        n_r: int = 16, n_ang: int = 24, seed: int = 20260714) -> dict:
    rng = np.random.default_rng(seed)
    s_cuts = np.geomspace(1.05 * D_SAT, 1.2 * R, n_cut)
    frac_acc = np.zeros(n_cut)
    dep_full_acc = 0.0
    for _ in range(n_orient):
        mesh = build_cells(R, n_r=n_r, n_ang=n_ang, rot=_rand_rot(rng))
        cells, cen = mesh["cells"], mesh["centers"]
        dmin = np.minimum(np.linalg.norm(cells - cen[0], axis=1),
                          np.linalg.norm(cells - cen[1], axis=1))
        a_full = transfer_alpha(mesh, R, alpha0)[0]
        dep_full = a_full - 1.0
        dep_full_acc += dep_full
        for j, sc in enumerate(s_cuts):
            mask = dmin <= sc
            a_in = transfer_alpha(mesh, R, alpha0, mask=mask)[0] if mask.any() else 1.0
            frac_acc[j] += (a_in - 1.0) / dep_full if abs(dep_full) > 1e-300 else 0.0
    frac = frac_acc / n_orient
    # enforce monotone-nondecreasing for a clean crossing (numerical guard)
    frac = np.maximum.accumulate(frac)
    return {"R": R, "n_r": n_r, "n_ang": n_ang, "dep_full": float(dep_full_acc / n_orient),
            "s_cuts_dsat": s_cuts.tolist(), "enclosed_frac": frac.tolist(),
            "r50_dsat": _cross_up(s_cuts, frac, 0.50),
            "r90_dsat": _cross_up(s_cuts, frac, 0.90),
            "r99_dsat": _cross_up(s_cuts, frac, 0.99)}


# ═════════════════════════════════════════════════════════════════════════════
def main() -> dict:
    ap = argparse.ArgumentParser(description="Knee-contour vs collar-edge check (F5-walk).")
    ap.add_argument("--smoke", action="store_true", help="fewer orientations / cuts")
    args = ap.parse_args()
    alpha0 = 0.03                       # #693 primary polarizability (FORM-firewalled)
    R_prof = 1000.0                     # profile separation (inside the frozen [30,3000] window)
    R_encl = 30.0                       # collar: frozen-window MINIMUM -> densest near-wall shells
    n_orient = 2 if args.smoke else 4
    n_cut = 24 if args.smoke else 40

    print(f"[knee] A_yield = R_I = sqrt(2a) = {A_YIELD:.6f}  (E_yield=K/d_sat^2={E_YIELD})", flush=True)

    # (1) A(s) profile + knee, at the frozen resolution AND a refined one (discretization)
    print("[knee] single-probe A(s) profile (frozen n_r=16,n_ang=24) ...", flush=True)
    prof16 = single_probe_profile(R_prof, alpha0, n_r=16, n_ang=24)
    print("[knee] single-probe A(s) profile (refined n_r=32,n_ang=48) ...", flush=True)
    prof32 = single_probe_profile(R_prof, alpha0, n_r=32, n_ang=48)
    knee16 = knee_from_profile(prof16)
    knee32 = knee_from_profile(prof32)
    onset16 = s6_onset(prof16)
    onset32 = s6_onset(prof32)
    s_knee = knee16["s_knee_field_measured_dsat"]       # PRIMARY: measured, frozen resolution
    if not np.isfinite(s_knee):
        s_knee = knee16["s_knee_field_bare_dsat"]
    disc_sens = (abs(knee32["s_knee_field_measured_dsat"] - knee16["s_knee_field_measured_dsat"])
                 / knee16["s_knee_field_measured_dsat"]) if np.isfinite(knee32["s_knee_field_measured_dsat"]) else None

    # (3) enclosed-correction collar radii — frozen (n_r=16) + refined (n_r=48) resolutions
    print(f"[knee] enclosed-correction (R={R_encl}, frozen n_r=16) ...", flush=True)
    encl = enclosed_correction(R_encl, alpha0, n_orient=n_orient, n_cut=n_cut, n_r=16, n_ang=24)
    print(f"[knee] enclosed-correction (R={R_encl}, refined n_r=48) ...", flush=True)
    encl_ref = enclosed_correction(R_encl, alpha0, n_orient=2, n_cut=n_cut, n_r=48, n_ang=24)
    r50, r90, r99 = encl["r50_dsat"], encl["r90_dsat"], encl["r99_dsat"]
    r90_ref = encl_ref["r90_dsat"]
    r90_disc_sens = (abs(r90_ref - r90) / r90) if (np.isfinite(r90) and np.isfinite(r90_ref) and r90 > 0) else None

    # (4) VERDICT — primary = field-strain s_knee vs 90%-correction radius
    verdict = classify(s_knee, r90) if np.isfinite(r90) else "UNDEFINED"
    verdict_vs_near = classify(s_knee, NEAR_R)          # vs the review's 10 d_sat cut
    verdict_voltage_vs_r90 = (classify(knee16["s_knee_voltage_dsat_FLAGGED"], r90)
                              if np.isfinite(r90) else "UNDEFINED")

    # (5) inverse read — what amplitude/S/Gamma the measured collar edge (r90) sits at
    A_at_r90 = float((D_SAT / r90) ** 2) if np.isfinite(r90) else float("nan")   # field-strain
    AV_at_r90 = float(D_SAT / r90) if np.isfinite(r90) else float("nan")         # voltage-strain
    S_at_r90 = kernel_S(A_at_r90) if np.isfinite(A_at_r90) else float("nan")
    G_at_r90 = reflection_Gamma(S_at_r90) if np.isfinite(S_at_r90) else float("nan")
    # reference: S,Gamma AT the field-strain knee (A=A_yield) for the contrast
    S_at_knee = kernel_S(A_YIELD)
    G_at_knee = reflection_Gamma(S_at_knee)

    result = {
        "check": "knee-contour vs collar-edge (F5-walk registered check)",
        "note": "research/2026-07-14_knee-contour-check_NOTE.md",
        "solver_imported_unmodified": "src/scripts/vol_2_subatomic/qed_trace_screening_sum_gate.py (#693)",
        "class": "CONSISTENCY (characterization of the #693 gate geometry; charge-agnostic "
                 "Op14 kernel; no emergence claim, no VALUE minted this wave)",
        "constants": {"ALPHA": ALPHA, "A_yield_R_I": A_YIELD, "L_NODE_m": L_NODE,
                      "d_sat_in_ell_node": DSAT_IN_LNODE, "E_yield": E_YIELD,
                      "unit_map_source": "methodological-contamination.md:46 (d_sat==ell_node)"},
        "amplitude_definition": "A = |E_total|/E_yield (driver :236); FIELD-strain (d_sat/s)^2 "
                                "for a unit probe (PRIMARY, kernel-consumed)",
        "knee_field_strain_PRIMARY": {
            "s_knee_measured_dsat": s_knee,
            "s_knee_measured_ell_node": s_knee * DSAT_IN_LNODE,
            "s_knee_bare_dsat": knee16["s_knee_field_bare_dsat"],
            "refined_res_s_knee_dsat": knee32["s_knee_field_measured_dsat"],
            "discretization_sensitivity_frac": disc_sens,
        },
        "knee_voltage_strain_FLAGGED": {
            "s_knee_dsat": knee16["s_knee_voltage_dsat_FLAGGED"],
            "s_knee_ell_node": knee16["s_knee_voltage_dsat_FLAGGED"] * DSAT_IN_LNODE,
            "source": "methodological-contamination.md:48-52 canonical voltage-strain A_V=d_sat/r",
        },
        "s6_dipole_density_onset_dsat": {"frozen_res": onset16, "refined_res": onset32},
        "collar_edge_enclosed_correction": {
            "R_dsat": R_encl, "dep_full": encl["dep_full"], "frozen_n_r": 16,
            "r50_dsat": r50, "r90_dsat": r90, "r99_dsat": r99,
            "r50_ell_node": (r50 * DSAT_IN_LNODE) if np.isfinite(r50) else None,
            "r90_ell_node": (r90 * DSAT_IN_LNODE) if np.isfinite(r90) else None,
            "r99_ell_node": (r99 * DSAT_IN_LNODE) if np.isfinite(r99) else None,
            "refined_n_r_48": {"r50_dsat": encl_ref["r50_dsat"], "r90_dsat": r90_ref,
                               "r99_dsat": encl_ref["r99_dsat"]},
            "r90_discretization_sensitivity_frac": r90_disc_sens,
            "review_NEAR_R_cut_dsat": NEAR_R,
            "s_cuts_dsat": encl["s_cuts_dsat"], "enclosed_frac": encl["enclosed_frac"],
        },
        "VERDICT": {
            "class": verdict,
            "basis": "field-strain s_knee vs 90%-correction radius r90",
            "s_knee_field_dsat": s_knee, "r90_dsat": r90,
            "ratio": (max(s_knee / r90, r90 / s_knee) if np.isfinite(r90) else None),
            "verdict_vs_NEAR_R_10dsat": verdict_vs_near,
            "verdict_voltage_knee_vs_r90_FLAGGED": verdict_voltage_vs_r90,
        },
        "inverse_read_at_collar_edge_r90": {
            "A_field_strain": A_at_r90, "A_voltage_strain": AV_at_r90,
            "S_kernel": S_at_r90, "Gamma_E_sector": G_at_r90,
            "note": "S~=1, Gamma~=0 => collar edge sits at a nearly-UNSATURATED amplitude "
                    "if r90 >> s_knee (collar NOT set by the saturation kernel)",
        },
        "reference_at_field_knee": {"A": A_YIELD, "S": S_at_knee, "Gamma_E_sector": G_at_knee,
                                    "note": "DeltaS = 1-S = alpha (proportional limit) at the knee"},
        "discretization_note": "single-resolution #693 lattice (log-radial shells); s_knee "
                               "reported at frozen (16,24) and refined (32,48) meshes.",
    }
    out = sim_output("knee_contour_check.json")
    out.write_text(json.dumps(result, indent=2))

    print("\n" + "=" * 72)
    print(f"  FIELD-STRAIN knee (PRIMARY, kernel-consumed A):")
    print(f"    s_knee = {s_knee:.3f} d_sat = {s_knee*DSAT_IN_LNODE:.3f} ell_node "
          f"(bare {knee16['s_knee_field_bare_dsat']:.3f}; refined {knee32['s_knee_field_measured_dsat']:.3f})")
    print(f"  VOLTAGE-STRAIN knee (FLAGGED, canonical corpus A_V=d_sat/r):")
    print(f"    s_knee = {knee16['s_knee_voltage_dsat_FLAGGED']:.3f} d_sat")
    print(f"  s^-6 dipole-density onset: {onset16} d_sat (refined {onset32})")
    print(f"  COLLAR edge (enclosed-correction, R={R_encl}, frozen n_r=16):")
    print(f"    r50={r50:.3f}  r90={r90:.3f}  r99={r99:.3f} d_sat   (review NEAR_R cut = {NEAR_R})")
    print(f"    refined n_r=48: r90={r90_ref:.3f} (r90 disc-sens {r90_disc_sens})")
    print(f"  -> VERDICT (field-knee vs r90): {verdict}  "
          f"(ratio {max(s_knee/r90, r90/s_knee):.2f})" if np.isfinite(r90) else "  -> VERDICT: UNDEFINED")
    print(f"     vs NEAR_R=10: {verdict_vs_near} | voltage-knee vs r90 (FLAGGED): {verdict_voltage_vs_r90}")
    print(f"  INVERSE READ at collar edge r90: A_field={A_at_r90:.4g} A_volt={AV_at_r90:.4g} "
          f"S={S_at_r90:.6f} Gamma={G_at_r90:.4g}")
    print(f"     (at the field knee: S={S_at_knee:.6f} Gamma={G_at_knee:.4g}, DeltaS=1-S={1-S_at_knee:.4g}=alpha)")
    print(f"  discretization sensitivity of s_knee: {disc_sens}")
    print("=" * 72)
    print(f"[knee] wrote {out}")
    _figure(result, prof16, encl)
    return result


def _figure(result, prof, encl):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply()

    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))
    s, A = np.array(prof["s"]), np.array(prof["A"])
    ax[0].loglog(s, A, "o-", color="#0072B2", label="A(s) measured (kernel-consumed |E|/E_yield)")
    ax[0].loglog(s, (D_SAT / s) ** 2, ":", color="#56B4E9", label=r"bare $(d_{sat}/s)^2$")
    ax[0].axhline(A_YIELD, color="#D55E00", ls="--", lw=1.0,
                  label=r"knee $A=\sqrt{2\alpha}=R_I$")
    sk = result["knee_field_strain_PRIMARY"]["s_knee_measured_dsat"]
    ax[0].axvline(sk, color="#D55E00", ls=":", lw=1.0)
    r90 = encl["r90_dsat"]
    if np.isfinite(r90):
        ax[0].axvline(r90, color="#009E73", ls="-.", lw=1.2, label=f"90%-correction r90={r90:.2f}")
    ax[0].axvline(NEAR_R, color="0.5", ls=":", lw=1.0, label=f"review NEAR_R={NEAR_R:g}")
    ax[0].set_xlabel(r"$s$  [$d_{\mathrm{sat}} = \ell_{\mathrm{node}}$]")
    ax[0].set_ylabel(r"field-strain amplitude $A$")
    ax[0].set_title("Single-probe A(s) and the knee contour", fontsize=9)
    ax[0].legend(fontsize=7, loc="best")

    sc = np.array(encl["s_cuts_dsat"])
    fr = np.array(encl["enclosed_frac"])
    ax[1].semilogx(sc, fr, "o-", color="#009E73", label="enclosed coupling-correction fraction")
    for f, lbl, c in [(0.5, "r50", "#0072B2"), (0.9, "r90", "#D55E00"), (0.99, "r99", "#CC79A7")]:
        rr = encl[f"{lbl}_dsat"]
        if np.isfinite(rr):
            ax[1].axvline(rr, color=c, ls=":", lw=1.0, label=f"{lbl}={rr:.2f}")
        ax[1].axhline(f, color=c, ls="--", lw=0.6, alpha=0.5)
    ax[1].axvline(sk, color="#D55E00", ls="-.", lw=1.2, label=f"field knee={sk:.2f}")
    ax[1].axvline(NEAR_R, color="0.5", ls=":", lw=1.0, label=f"NEAR_R={NEAR_R:g}")
    ax[1].set_xlabel(r"cut radius $s_{\mathrm{cut}}$  [$d_{\mathrm{sat}}$]")
    ax[1].set_ylabel("enclosed correction fraction")
    ax[1].set_title(f"Collar edge vs knee — verdict: {result['VERDICT']['class']}", fontsize=9)
    ax[1].legend(fontsize=7, loc="best")
    fig.suptitle("Knee-contour vs #693 collar-edge check (E-sector static dielectric, transfer register)",
                 fontsize=10, y=1.02)
    fig.tight_layout()
    out_png = sim_output("knee_contour_check.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    print(f"[knee] wrote {out_png}")


if __name__ == "__main__":
    main()
