#!/usr/bin/env python3
"""PILOT — the DC-biased small-signal elastic tensor AT the iso-bond point rho_bond = 1.

SCOPING-GRADE PILOT (bins NOT frozen; the follow-on prereg freezes them).
Deliverable of `research/2026-08-02_biased-tensor-scoping.md`.

WHAT THIS ANSWERS
-----------------
The ratified W1 resolution places the vacuum at the energetics-derived iso-bond point
rho_bond = k_a/k_s = 1 (Ax3 |Gamma|^2-min, knob-free, PR #516), whose reported bulk
modulus K = -0.0589 is NEGATIVE (PR #506). The stabilization hypothesis under test is a
DC operating-point pre-stress ("the pressurized vessel"). This pilot runs five arms, all
on the MERGED, VALIDATED cold Born-Huang pipeline (imported unmodified from
`srs_elastic_tensor.py`; no new stencil, no new solver -- Rule-14 anti-rebuild):

  P0  COLD RECOVERY      -- reproduce the merged #506 rho=1 row (to its 5-s.f. literals).
  P1  PRE-STRESS IDENTITY-- the Born shear spring k_s IS a bond pre-tension tau = k_s*l:
                            (a) a rigid rotation costs energy 0.5*k_s*sum|Omega r|^2 != 0,
                                so the Born rank-2 bond model is NOT rotationally invariant
                                unless the k_s term is the transverse projection of a bond
                                TENSION whose first-order work cancels it;
                            (b) at rho=1 the whole acoustic tensor is PURE pre-stress:
                                C11 = C44 = -C12 = sigma_0 = (1/3V) sum_b k_s l_b^2 ;
                            (c) the Birch/Wallace split C_thermo = C_acoustic -+ sigma_0
                                gives the closed form K_thermo = (rho_bond - 1)*sigma_0/3,
                                exact at every rho -- ZERO, not negative, at rho = 1.
  P2  SYMMETRIC BIAS     -- A_0 sweep with S_axial = S_shear = S(A_0). Tracks sign(K) on
                            BOTH readings + the Zener ratio. (Prediction from #519's
                            degree-1 homogeneity: sign(K) is INVARIANT; Zener stays 1.)
  P3  ASYMMETRIC PRICE   -- the anisotropy price of buying K > 0 with S_axial != S_shear.
                            The K_thermodynamic threshold is reported TWICE (KEEP-BOTH,
                            added 2026-08-02 in review): the original numeric secant gate
                            (`> 1e-12`, retained UNCHANGED but disclosed as sitting ~3 OOM
                            BELOW this arm's own noise floor, so it does not resolve the
                            threshold) AND the resolution-independent analytic form
                            K_th = (rho_eff - 1)*sigma_0/3 > 0 iff rho_eff > 1.
  P4  BZ-WIDE DEGENERACY -- at rho_bond = 1 the 24x24 D(q) factorizes EXACTLY as
                            L(q) (x) I_3 (scalar graph Laplacian tensor the 3x3 identity),
                            so all three polarizations are degenerate at EVERY q, and
                            D(q) >= 0 everywhere (no dynamical instability at any k).

SUBSTRATE-FIRST SECTOR HEADER (as run)
--------------------------------------
SECTOR:  translational-u (Cauchy) sector of the RATIFIED chiral srs-z3 net (I4_1 32,
         Wyckoff-8a, 8 sublattices x 3 DOF, z = 3). BORN rank-2 bond tensor
         Phi_b = k_a d^ (x) d^ + k_s (I - d^ (x) d^). NOT a Cartesian Laplacian.
         Cosserat couple-stress = Stage 2, NOT invoked (k->0 Cauchy grade only).
MODE:    SMALL-SIGNAL long-wave about a DC bias point (varactor picture, INVARIANT-S2).
REGIME:  quasi-static about a DC bias; Op14/Ax4 saturation ON in P2/P3, OFF in P0/P1/P4.
COORDS:  operating-point knob (A_axial, A_shear) in phase-space/reactance; tensor readout
         omega(k) -> C_ij -> K, Zener in real-space/spatial-Brillouin. A46-clean on both.
CLASS:   CONSISTENCY (P0, P2, P3, P4) + MECHANISM/IDENTITY (P1). NO emergence claim: no
         value is derived here; sigma_0, rho*, 2/7, sqrt(10/3) are read-off comparisons
         the sweep never fits to.

Determinism: all random-q sampling uses a fixed seed (SEED). No CODATA on the verdict
path (alpha enters only via the read-off A_CORE = sqrt(alpha) comparison row).

Run:
    PYTHONPATH=src ./.venv/bin/python src/scripts/vol_1_foundations/biased_tensor_iso_bond_pilot.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

_REPO = Path(__file__).resolve().parents[3]
if str(_REPO / "src") not in sys.path:
    sys.path.insert(0, str(_REPO / "src"))
if str(_REPO / "src" / "scripts" / "vol_1_foundations") not in sys.path:
    sys.path.insert(0, str(_REPO / "src" / "scripts" / "vol_1_foundations"))

# The MERGED, VALIDATED cold pipeline -- imported unmodified (Rule-14 anti-rebuild).
from srs_elastic_tensor import (  # noqa: E402
    acoustic_christoffel,
    cauchy_bloch_D,
    extract_cubic_Cij,
    moduli_from_Cij,
    srs_primitive,
)

from ave.axioms.scale_invariant import saturation_factor  # noqa: E402
from ave.core.constants import ALPHA  # noqa: E402

SEED = 20260802

# ---------------------------------------------------------------------------
# READ-OFF comparison constants (anti-tune: NEVER inputs to any sweep)
# ---------------------------------------------------------------------------
RHO_ISO_BOND = 1.0          # the Ax3 |Gamma|^2-min iso-bond point (#516, knob-free)
RHO_STAR_IMPORTED = 9.7734  # the GR-imported nu=2/7 <=> K=2G matter point (#506)
RHO_K0_FLOOR = 2.0          # where the ACOUSTIC K combination changes sign (#506)
A_CORE_SQRT_ALPHA = float(np.sqrt(ALPHA))  # def-vyvsn1 A1 core amplitude
# Merged rho=1 row literals, for the cold-recovery receipt.
#
# ⚑ RE-ATTRIBUTED 2026-08-02 IN REVIEW (finding 4). The previous comment read
#   "# Merged #506 rho=1 row literals (5 s.f.)"
# and the K entry was -0.058926. That attribution does NOT hold: -0.058926 appears NOWHERE
# in the corpus at any precision. Per-cell provenance, byte-verified:
#   C11 / C12 / C44 / Zener  -- 5 s.f. at `research/2026-07-04_saturated-elastic-tensor_result.md`
#     :57 and :117, verbatim "C11=C44=+0.17678, C12=-0.17678, ... Zener=1.0000". The merged
#     #506 row (`research/2026-07-04_srs-elastic-tensor_result.md`:125) prints the same cells
#     to 4 s.f. (+0.1768) and #506:198 prints the collapsed iso-bond value "0.17678".
#   K  -- 5 s.f. -0.05893 at `saturated-elastic-tensor_result.md`:57 and :117, verbatim
#     "K=-0.05893". #506:125 prints -0.0589 (4 s.f.), which this gate would FAIL
#     (|computed - (-0.0589)| = 2.56e-5 > 5e-6); the 5-s.f. #519 literal PASSES at 4.43e-6,
#     and 4.43e-6 is now the arm's max deviation. Gate left UNCHANGED at 5e-6; disclosed here,
#     in the JSON provenance block, and in the doc's Receipt 1.
MERGED_RHO1_LITERALS = {"C11": 0.17678, "C12": -0.17678, "C44": 0.17678, "K": -0.05893, "Zener": 1.0}
MERGED_RHO1_PROVENANCE = {
    "C11": "saturated-elastic-tensor_result.md:57,:117 (5 s.f.); srs-elastic-tensor_result.md:125 (4 s.f.), :198",
    "C12": "saturated-elastic-tensor_result.md:57,:117 (5 s.f.); srs-elastic-tensor_result.md:125 (4 s.f.)",
    "C44": "saturated-elastic-tensor_result.md:57,:117 (5 s.f.); srs-elastic-tensor_result.md:125 (4 s.f.), :198",
    "K": ("saturated-elastic-tensor_result.md:57,:117 (5 s.f. -0.05893); "
          "srs-elastic-tensor_result.md:125 prints -0.0589 (4 s.f.)"),
    "Zener": "saturated-elastic-tensor_result.md:57,:117; srs-elastic-tensor_result.md:125",
}


# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------
def undirected_bonds(bonds):
    """Collapse the directed bond list (i->j and j->i) to one entry per bond."""
    seen, und = set(), []
    for (i, j, d) in bonds:
        key = (min(i, j), max(i, j), tuple(np.round(np.abs(d), 9)))
        if key in seen:
            continue
        seen.add(key)
        und.append((i, j, d))
    return und


def prestress_tensor(und, cell_volume, k_shear):
    """sigma^0_ij = (1/V) sum_b (tau_b) l_b d^_i d^_j  with tau_b = k_shear * l_b.

    This is the reference-state Cauchy stress carried by a bond network whose transverse
    stiffness is the geometric consequence of a bond TENSION (the taut-string term).
    """
    sig = np.zeros((3, 3))
    for (_i, _j, d) in und:
        ell = float(np.linalg.norm(d))
        dh = d / ell
        sig += k_shear * ell ** 2 * np.outer(dh, dh) / cell_volume
    return sig


def affine_acoustic_tensor(und, cell_volume, k_axial, k_shear):
    """The UNRELAXED (affine) acoustic tensor B_ijkl = C2_ijkl + sigma^0_jl delta_ik.

    C2_ijkl = (1/V) sum_b (k_a - k_s) l^2 d^_i d^_j d^_k d^_l   (Brugger 2nd-order, from
    the pair-potential expansion with U'' = k_a and U'(l)/l = k_s), and the sigma^0 term is
    the standard initial-stress contribution to wave propagation. Returned for the P1
    identity check ONLY; every verdict number uses the RELAXED merged pipeline.
    """
    C2 = np.zeros((3, 3, 3, 3))
    for (_i, _j, d) in und:
        ell = float(np.linalg.norm(d))
        dh = d / ell
        C2 += (k_axial - k_shear) * ell ** 2 * np.einsum("i,j,k,l->ijkl", dh, dh, dh, dh) / cell_volume
    sig = prestress_tensor(und, cell_volume, k_shear)
    return C2 + np.einsum("jl,ik->ijkl", sig, np.eye(3)), C2, sig


def rigid_rotation_energy(und, k_axial, k_shear):
    """Harmonic energy of an infinitesimal RIGID ROTATION under the Born bond tensor.

    A rotationally invariant force-constant model must return exactly 0. The Born rank-2
    model returns 0.5*k_s*sum_b |Omega r_b|^2 > 0 -- the k_s term alone is NOT rotationally
    invariant. It becomes invariant only if k_s is the transverse projection of a bond
    TENSION tau = k_s*l, whose first-order work -tau*(second-order shortening) cancels it.
    """
    Om = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    e_model, e_tension_form = 0.0, 0.0
    for (_i, _j, d) in und:
        ell = float(np.linalg.norm(d))
        dh = d / ell
        P = np.outer(dh, dh)
        Phi = k_axial * P + k_shear * (np.eye(3) - P)
        du = Om @ d
        e_model += 0.5 * float(du @ Phi @ du)
        e_tension_form += 0.5 * k_shear * float(du @ du)
    return e_model, e_tension_form


def branch_speeds(pos, bonds, rho, k_axial, k_shear, dirs=((1, 0, 0), (1, 1, 0), (1, 1, 1))):
    """Per-direction sqrt(rho c^2) for the two transverse and one longitudinal branch."""
    tr, lo = [], []
    for dd in dirs:
        G = acoustic_christoffel(np.array(dd, float), pos, bonds,
                                 k_axial=k_axial, k_shear=k_shear, rho=rho)
        e = np.sort(np.linalg.eigvalsh(G))
        tr += [float(np.sqrt(max(e[0], 0.0))), float(np.sqrt(max(e[1], 0.0)))]
        lo.append(float(np.sqrt(max(e[2], 0.0))))
    t_spread = (max(tr) - min(tr)) / float(np.mean(tr)) if np.mean(tr) > 0 else float("nan")
    return {
        "T_branch_fractional_spread": t_spread,
        "cL_over_cT_dir_avg": float(np.mean(lo) / np.mean(tr)) if np.mean(tr) > 0 else float("nan"),
        "T_min": min(tr), "T_max": max(tr), "L_min": min(lo), "L_max": max(lo),
    }


def operating_point_row(pos, bonds, rho, und, V, S_axial, S_shear):
    """One small-signal operating point: the RELAXED tensor + BOTH bulk-modulus readings."""
    f = extract_cubic_Cij(pos, bonds, k_axial=S_axial, k_shear=S_shear, rho=rho)
    m = moduli_from_Cij(f["C11"], f["C12"], f["C44"])
    sig0 = float(np.trace(prestress_tensor(und, V, S_shear)) / 3.0)
    return {
        "S_axial": float(S_axial), "S_shear": float(S_shear),
        "rho_eff": float(S_axial / S_shear),
        "C11": f["C11"], "C12": f["C12"], "C44": f["C44"],
        "max_rel_residual": f["max_rel_residual"],
        "sigma_0": sig0,
        "K_acoustic_Birch": m["K_bulk"],          # the #506 "K" column
        "K_thermodynamic": m["K_bulk"] + sig0 / 3.0,  # Birch -> Brugger 2nd-order
        "Zener_A": m["Zener_A"],
        "C44_abs": f["C44"],
    }


# ===========================================================================
# P0 -- COLD RECOVERY (positive control; HALT-gated)
# ===========================================================================
def arm_P0(pos, bonds, rho):
    f = extract_cubic_Cij(pos, bonds, k_axial=1.0, k_shear=1.0, rho=rho)
    m = moduli_from_Cij(f["C11"], f["C12"], f["C44"])
    dev = {
        "C11": abs(f["C11"] - MERGED_RHO1_LITERALS["C11"]),
        "C12": abs(f["C12"] - MERGED_RHO1_LITERALS["C12"]),
        "C44": abs(f["C44"] - MERGED_RHO1_LITERALS["C44"]),
        "K": abs(m["K_bulk"] - MERGED_RHO1_LITERALS["K"]),
        "Zener": abs(m["Zener_A"] - MERGED_RHO1_LITERALS["Zener"]),
    }
    ok = max(dev.values()) < 5e-6  # every literal is quoted to 5 s.f.
    return {
        "computed": {"C11": f["C11"], "C12": f["C12"], "C44": f["C44"],
                     "K_acoustic_Birch": m["K_bulk"], "Zener_A": m["Zener_A"]},
        "merged_reference_row": MERGED_RHO1_LITERALS,
        "merged_reference_row_provenance": MERGED_RHO1_PROVENANCE,
        "per_cell_abs_deviation": dev,
        "max_abs_deviation": max(dev.values()),
        "PASS": bool(ok),
    }


# ===========================================================================
# P1 -- THE PRE-STRESS IDENTITY (the load-bearing arm)
# ===========================================================================
def arm_P1(pos, bonds, rho, und, V):
    # (a) rotational invariance receipt
    e_model, e_tension = rigid_rotation_energy(und, 1.0, 1.0)
    e_central_only, _ = rigid_rotation_energy(und, 1.0, 0.0)

    # (b) at rho=1: the acoustic tensor is pure pre-stress
    sig = prestress_tensor(und, V, 1.0)
    sigma_0 = float(np.trace(sig) / 3.0)
    sig_offdiag = float(np.max(np.abs(sig - np.diag(np.diag(sig)))))
    f1 = extract_cubic_Cij(pos, bonds, k_axial=1.0, k_shear=1.0, rho=rho)
    pure_prestress_dev = max(abs(f1["C11"] - sigma_0), abs(f1["C44"] - sigma_0),
                             abs(f1["C12"] + sigma_0))

    # relaxation contribution at rho=1 (affine vs internal-strain-relaxed)
    B_aff, _C2, _s = affine_acoustic_tensor(und, V, 1.0, 1.0)
    relax_dev = 0.0
    for dd in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (3, 1, 2)):
        n = np.array(dd, float)
        n /= np.linalg.norm(n)
        G_aff = np.einsum("ijkl,j,l->ik", B_aff, n, n)
        G_rel = acoustic_christoffel(n, pos, bonds, k_axial=1.0, k_shear=1.0, rho=rho)
        relax_dev = max(relax_dev, float(np.max(np.abs(G_aff - G_rel))))

    # (c) the Birch <-> Brugger split, and the closed form K_thermo = (rho-1)*sigma_0/3
    rows, worst = [], 0.0
    for r in (0.5, 1.0, 1.52, 2.0, 3.0, 5.0, 7.0, RHO_STAR_IMPORTED, 10.0):
        f = extract_cubic_Cij(pos, bonds, k_axial=r, k_shear=1.0, rho=rho)
        m = moduli_from_Cij(f["C11"], f["C12"], f["C44"])
        K_th = m["K_bulk"] + sigma_0 / 3.0
        closed = (r - 1.0) * sigma_0 / 3.0
        worst = max(worst, abs(K_th - closed))
        rows.append({
            "rho_bond": r, "C11": f["C11"], "C12": f["C12"], "C44": f["C44"],
            "K_acoustic_Birch": m["K_bulk"], "K_thermodynamic": K_th,
            "closed_form_(rho-1)sigma0/3": closed,
            "C11_thermo": f["C11"] - sigma_0, "C12_thermo": f["C12"] + sigma_0,
            "C44_thermo": f["C44"] - sigma_0, "Zener_A": m["Zener_A"],
            "Cauchy_violation_C12_minus_C44": f["C12"] - f["C44"],
        })
    return {
        "rotational_invariance": {
            "rigid_rotation_energy_born_model": e_model,
            "predicted_0.5_k_s_sum_|Omega r|^2": e_tension,
            "rigid_rotation_energy_central_force_only_k_s=0": e_central_only,
            "VERDICT": ("the k_s term is NOT rotationally invariant on its own; it is the "
                        "transverse projection of a bond TENSION tau = k_s*l"),
        },
        "prestress": {
            "sigma_0_closed_form_(1/3V)sum_k_s_l^2": sigma_0,
            "sigma_tensor_max_offdiagonal": sig_offdiag,
            "isotropic": bool(sig_offdiag < 1e-12),
        },
        "pure_prestress_at_rho1": {
            "C11": f1["C11"], "C12": f1["C12"], "C44": f1["C44"],
            "max_dev_from_(sigma0, -sigma0, sigma0)": pure_prestress_dev,
            "internal_relaxation_contribution_max": relax_dev,
            "PASS": bool(pure_prestress_dev < 1e-7),
        },
        "birch_to_brugger": {
            "relation": "C11_th = C11 - sigma_0 ; C12_th = C12 + sigma_0 ; C44_th = C44 - sigma_0",
            "equivalent_to_Wallace_with_P": "P = -sigma_0 (the reference state is in TENSION)",
            "closed_form_max_abs_error": worst,
            "PASS": bool(worst < 1e-7),
            "rows": rows,
        },
    }


# ===========================================================================
# P2 -- SYMMETRIC DC BIAS SWEEP (the task's arm: does symmetric bias flip sign K?)
# ===========================================================================
def arm_P2(pos, bonds, rho, und, V, a_max=0.999):
    amps = [0.0, 0.05, A_CORE_SQRT_ALPHA, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99, a_max]
    rows = []
    for A0 in amps:
        S = float(saturation_factor(A0, yield_limit=1.0))
        row = operating_point_row(pos, bonds, rho, und, V, S, S)
        row["A_0"] = float(A0)
        row["S"] = S
        row.update(branch_speeds(pos, bonds, rho, S, S))
        rows.append(row)
    sign_flip = any(r["K_acoustic_Birch"] > 0 for r in rows)
    thermo_nonzero = max(abs(r["K_thermodynamic"]) for r in rows)
    zener_dev = max(abs(r["Zener_A"] - 1.0) for r in rows)
    rho_eff_dev = max(abs(r["rho_eff"] - 1.0) for r in rows)
    cl_ct_dev = max(abs(r["cL_over_cT_dir_avg"] - 1.0) for r in rows)
    return {
        "rows": rows,
        "sign_K_acoustic_ever_flips": bool(sign_flip),
        "max_|K_thermodynamic|": thermo_nonzero,
        "max_|Zener-1|": zener_dev,
        "max_|rho_eff-1|": rho_eff_dev,
        "max_|cL/cT - 1|": cl_ct_dev,
        "VERDICT": ("SYMMETRIC BIAS CANNOT STABILIZE: K_acoustic = S*K_cold stays negative "
                    "for every S>0 (degree-1 homogeneity, #519), and K_thermodynamic is "
                    "identically ZERO. Zener stays 1.000 and cL/cT stays 1.000 exactly."),
    }


# ===========================================================================
# P3 -- ASYMMETRIC BIAS: the ANISOTROPY PRICE of buying K > 0
# ===========================================================================
def arm_P3(pos, bonds, rho, und, V):
    rows = []
    grid = [1.0, 1.000001, 1.001, 1.01, 1.05, 1.1, 1.25, 1.5, 1.75, 2.0, 2.5,
            3.0, 5.0, RHO_STAR_IMPORTED]
    for r in grid:
        # hold the shear (tension) channel at the cold value; stiffen the axial channel
        row = operating_point_row(pos, bonds, rho, und, V, r, 1.0)
        row.update(branch_speeds(pos, bonds, rho, r, 1.0))
        rows.append(row)
    # local slopes at the iso-bond point
    h = 1e-4
    zp = moduli_from_Cij(**{k: v for k, v in extract_cubic_Cij(
        pos, bonds, k_axial=1.0 + h, k_shear=1.0, rho=rho).items()
        if k in ("C11", "C12", "C44")})["Zener_A"]
    zm = moduli_from_Cij(**{k: v for k, v in extract_cubic_Cij(
        pos, bonds, k_axial=1.0 - h, k_shear=1.0, rho=rho).items()
        if k in ("C11", "C12", "C44")})["Zener_A"]
    dZ = (zp - zm) / (2 * h)
    # The T-spread is a max-minus-min: it is V-shaped through rho=1, so a CENTRED
    # difference across the cusp is meaningless. Use one-sided secants and report both.
    dS_secants = [rw["T_branch_fractional_spread"] / (rw["rho_eff"] - 1.0)
                  for rw in rows if 1.0005 < rw["rho_eff"] < 1.02]
    dS = float(np.mean(dS_secants))
    thr_birch = next(r for r in rows if r["K_acoustic_Birch"] > 0)
    thr_thermo = next(r for r in rows if r["K_thermodynamic"] > 1e-12)

    # --- SUPPLEMENTARY ANALYTIC THRESHOLD (added 2026-08-02 in review, finding 12) --------
    # DISCLOSURE, stated before the number. The numeric secant gate `> 1e-12` immediately
    # above sits ~3 OOM BELOW this arm's own measured K_thermodynamic noise floor at
    # rho_eff = 1 (|K_th| ~ 4e-10 here, ~5e-10 across the P2 sweep). It is therefore NOT
    # resolving a threshold: which row it first fires on is decided by the SIGN of a
    # numerical residual, not by physics -- had the rho_eff = 1 residual come out positive,
    # the gate would have fired at rho_eff = 1.0. The gate is deliberately RETAINED
    # UNCHANGED (KEEP-BOTH; this is a post-result gate-QUALITY note, not a retune, and
    # retuning a gate after seeing its result is exactly what Rule 11 forbids). What
    # follows is the resolution-independent statement the document's threshold claim
    # actually rests on -- the P1 closed form, which is exact to 1.1e-08 over rho in
    # [0.5, 10]:
    #     K_th(rho_eff) = (rho_eff - 1) * sigma_0 / 3 ,  sigma_0 > 0
    #  => K_th > 0  IF AND ONLY IF  rho_eff > 1 ,  with NO finite threshold and no
    #     resolution floor. The measured rows are checked against it below wherever the
    #     predicted magnitude clears 10x the noise floor.
    sigma_0_p3 = float(np.trace(prestress_tensor(und, V, 1.0)) / 3.0)
    noise_floor = max([abs(rw["K_thermodynamic"]) for rw in rows if rw["rho_eff"] == 1.0]
                      or [0.0])
    closed_err, sign_ok, n_checked = 0.0, True, 0
    for rw in rows:
        pred = (rw["rho_eff"] - 1.0) * sigma_0_p3 / 3.0
        closed_err = max(closed_err, abs(rw["K_thermodynamic"] - pred))
        if abs(pred) > 10.0 * max(noise_floor, 1e-30):
            n_checked += 1
            sign_ok = sign_ok and (np.sign(rw["K_thermodynamic"]) == np.sign(pred))
    analytic_threshold = {
        "closed_form": "K_thermodynamic(rho_eff) = (rho_eff - 1) * sigma_0 / 3",
        "sigma_0": sigma_0_p3,
        "threshold_rho_eff_ANALYTIC": 1.0,
        "assertion": "K_thermodynamic > 0 if and only if rho_eff > 1 (sigma_0 > 0)",
        "sigma_0_positive": bool(sigma_0_p3 > 0.0),
        "max_abs_error_of_closed_form_over_P3_grid": closed_err,
        "measured_noise_floor_|K_th|_at_rho_eff=1": noise_floor,
        "rows_above_10x_noise_floor_checked": n_checked,
        "sign_agrees_with_closed_form_on_every_resolved_row": bool(sign_ok),
        "PASS": bool(sigma_0_p3 > 0.0 and sign_ok and closed_err < 1e-7),
        "DISCLOSURE": ("the numeric secant gate `K_thermodynamic > 1e-12` reported in "
                       "`threshold_K_thermodynamic_positive` is ~3 OOM BELOW the measured "
                       "noise floor at rho_eff = 1 and cannot resolve the threshold; it is "
                       "RETAINED UNCHANGED for the frozen record (KEEP-BOTH). This analytic "
                       "form is the resolution-independent statement."),
    }
    return {
        "rows": rows,
        "dZener_drho_at_iso_bond": float(dZ),
        "dTspread_drho_at_iso_bond_onesided_secant": float(abs(dS)),
        "threshold_K_acoustic_positive": {"rho_eff": thr_birch["rho_eff"],
                                          "Zener_A": thr_birch["Zener_A"],
                                          "T_spread": thr_birch["T_branch_fractional_spread"]},
        "threshold_K_thermodynamic_positive": {"rho_eff": thr_thermo["rho_eff"],
                                               "Zener_A": thr_thermo["Zener_A"],
                                               "T_spread": thr_thermo["T_branch_fractional_spread"],
                                               "GATE_IS_NOISE_FLOOR_LIMITED": True},
        "threshold_K_thermodynamic_positive_ANALYTIC": analytic_threshold,
        "VERDICT": ("ASYMMETRIC BIAS CAN buy K>0, and the price is anisotropy: near the "
                    "iso-bond point Zener-1 ~ (rho_eff-1)/8 and the transverse-branch "
                    "fractional speed spread ~ (rho_eff-1)/16."),
    }


# ===========================================================================
# P4 -- BZ-WIDE STRUCTURE AT rho_bond = 1 (the Laplacian factorization)
# ===========================================================================
def arm_P4(pos, bonds, n_q=2000):
    rng = np.random.default_rng(SEED)
    n = len(pos)
    a = float(np.max(np.abs(np.array([d for (_i, _j, d) in bonds])))) * 0.0 + 2.0 * np.pi
    worst_triple, min_eig, worst_fact = 0.0, np.inf, 0.0
    for _ in range(n_q):
        q = rng.uniform(-1.0, 1.0, 3) * a  # covers and over-covers the BZ
        D = cauchy_bloch_D(q, pos, bonds, k_axial=1.0, k_shear=1.0)
        w = np.sort(np.linalg.eigvalsh(D))
        trip = w.reshape(-1, 3)
        scale = float(np.max(np.abs(w))) + 1e-30
        worst_triple = max(worst_triple, float(np.max(trip.max(axis=1) - trip.min(axis=1))) / scale)
        min_eig = min(min_eig, float(w.min()))
    # exact factorization check D(q) == L(q) (x) I_3
    for _ in range(25):
        q = rng.uniform(-1.0, 1.0, 3) * a
        D = cauchy_bloch_D(q, pos, bonds, k_axial=1.0, k_shear=1.0)
        L = np.zeros((n, n), dtype=complex)
        for (i, j, d) in bonds:
            L[i, j] += -np.exp(1j * np.dot(q, d))
            L[i, i] += 1.0
        L = 0.5 * (L + L.conj().T)
        worst_fact = max(worst_fact, float(np.linalg.norm(D - np.kron(L, np.eye(3)))
                                           / (np.linalg.norm(D) + 1e-30)))
    # control at rho_bond = 3: the instrument must SEE the difference
    ctrl = 0.0
    for _ in range(50):
        q = rng.uniform(-1.0, 1.0, 3) * a
        w = np.sort(np.linalg.eigvalsh(cauchy_bloch_D(q, pos, bonds, k_axial=3.0, k_shear=1.0)))
        trip = w.reshape(-1, 3)
        ctrl = max(ctrl, float(np.max(trip.max(axis=1) - trip.min(axis=1)))
                   / (float(np.max(np.abs(w))) + 1e-30))
    return {
        "n_q_sampled": n_q, "seed": SEED,
        "worst_relative_intra_triple_spread_rho1": worst_triple,
        "min_eigenvalue_D(q)_rho1": min_eig,
        "exact_factorization_||D - L(x)I3||/||D||": worst_fact,
        "control_rho3_worst_intra_triple_spread": ctrl,
        "VERDICT": ("At rho_bond=1 the vector elastic problem COLLAPSES to a SCALAR graph-"
                    "Laplacian problem: D(q) = L(q) (x) I_3 exactly, so all three polarizations "
                    "are degenerate at EVERY q and D(q) >= 0 everywhere -- no dynamical "
                    "instability at any wavevector. Cubic symmetry then forces the rank-2 "
                    "long-wave coefficient to be isotropic, so Zener A = 1 is a SYMMETRY "
                    "THEOREM at this point, not a numerical coincidence."),
    }


def main():
    pos, bonds, rho = srs_primitive("right")
    und = undirected_bonds(bonds)
    # cell volume from the srs builder convention (rho = n_nodes / a^3)
    V = float(len(pos) / rho)
    a_cell = float(V ** (1.0 / 3.0))

    p0 = arm_P0(pos, bonds, rho)
    if not p0["PASS"]:
        raise SystemExit(f"HALT: P0 cold recovery FAILED: {p0}")
    p1 = arm_P1(pos, bonds, rho, und, V)
    if not (p1["pure_prestress_at_rho1"]["PASS"] and p1["birch_to_brugger"]["PASS"]):
        raise SystemExit(f"HALT: P1 pre-stress identity FAILED: {p1}")
    p2 = arm_P2(pos, bonds, rho, und, V)
    p3 = arm_P3(pos, bonds, rho, und, V)
    if not p3["threshold_K_thermodynamic_positive_ANALYTIC"]["PASS"]:
        raise SystemExit("HALT: P3 ANALYTIC K_thermodynamic threshold FAILED: "
                         f"{p3['threshold_K_thermodynamic_positive_ANALYTIC']}")
    p4 = arm_P4(pos, bonds)

    out = {
        "driver": "src/scripts/vol_1_foundations/biased_tensor_iso_bond_pilot.py",
        "scoping_doc": "research/2026-08-02_biased-tensor-scoping.md",
        "grade": "SCOPING PILOT -- bins NOT frozen",
        "carrier": {"net": "chiral srs-z3 (I4_1 32, Wyckoff-8a)", "enantiomorph": "right",
                    "n_nodes": len(pos), "n_bonds_undirected": len(und),
                    "cell_edge_a": a_cell, "cell_volume": V, "mass_density_rho": rho},
        "read_off_constants_never_fitted": {
            "RHO_ISO_BOND": RHO_ISO_BOND, "RHO_K0_FLOOR": RHO_K0_FLOOR,
            "RHO_STAR_IMPORTED": RHO_STAR_IMPORTED,
            "A_CORE_SQRT_ALPHA": A_CORE_SQRT_ALPHA},
        "P0_cold_recovery": p0,
        "P1_prestress_identity": p1,
        "P2_symmetric_bias_sweep": p2,
        "P3_asymmetric_price_curve": p3,
        "P4_brillouin_zone_structure": p4,
    }
    dest = _REPO / "research" / "2026-08-02_biased-tensor-scoping_pilot.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=False) + "\n")
    print(f"wrote {dest}")
    print(f"P0 cold recovery PASS (max dev {p0['max_abs_deviation']:.2e})")
    print(f"P1 sigma_0 = {p1['prestress']['sigma_0_closed_form_(1/3V)sum_k_s_l^2']:.9f}; "
          f"pure-prestress dev {p1['pure_prestress_at_rho1']['max_dev_from_(sigma0, -sigma0, sigma0)']:.2e}; "
          f"closed-form K_thermo err {p1['birch_to_brugger']['closed_form_max_abs_error']:.2e}")
    print(f"P1 rigid-rotation energy (Born, k_s=1) = "
          f"{p1['rotational_invariance']['rigid_rotation_energy_born_model']:.6f} "
          f"(central-force-only = {p1['rotational_invariance']['rigid_rotation_energy_central_force_only_k_s=0']:.2e})")
    print(f"P2 sign(K_acoustic) ever flips: {p2['sign_K_acoustic_ever_flips']}; "
          f"max|K_thermo| {p2['max_|K_thermodynamic|']:.2e}; max|Zener-1| {p2['max_|Zener-1|']:.2e}")
    print(f"P3 dZener/drho at iso-bond = {p3['dZener_drho_at_iso_bond']:.6f}; "
          f"dTspread/drho = {p3['dTspread_drho_at_iso_bond_onesided_secant']:.6f}; "
          f"K_acoustic>0 first at rho_eff={p3['threshold_K_acoustic_positive']['rho_eff']}")
    _an = p3["threshold_K_thermodynamic_positive_ANALYTIC"]
    _an_err = _an["max_abs_error_of_closed_form_over_P3_grid"]
    print(f"P3 ANALYTIC K_thermo>0 iff rho_eff>1 (closed-form err {_an_err:.2e}; "
          f"sign OK on {_an['rows_above_10x_noise_floor_checked']} resolved rows) PASS={_an['PASS']}; "
          f"the numeric secant gate 1e-12 is NOISE-FLOOR-LIMITED "
          f"(floor {_an['measured_noise_floor_|K_th|_at_rho_eff=1']:.1e}), retained unchanged")
    print(f"P4 ||D - L(x)I3||/||D|| = {p4['exact_factorization_||D - L(x)I3||/||D||']:.2e}; "
          f"worst triple spread {p4['worst_relative_intra_triple_spread_rho1']:.2e} "
          f"(control rho=3: {p4['control_rho3_worst_intra_triple_spread']:.3f}); "
          f"min eig D(q) = {p4['min_eigenvalue_D(q)_rho1']:.4e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
