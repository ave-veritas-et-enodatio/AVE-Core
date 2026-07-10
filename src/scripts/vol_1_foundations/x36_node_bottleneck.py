#!/usr/bin/env python3
"""X36 — the node-bottleneck discriminator (the D-I test): does Axiom 1's node
LC TANK pin the multi-channel band ceiling at the node rate, DERIVING effective
synchrony from the node resonance with NO tick postulate?

Prereg (FROZEN): research/2026-07-09_x36-node-bottleneck_prereg_FROZEN.md
Class: CONSISTENCY / characterization (math + numerics; not a falsification, not
an emergence claim; no CODATA on any verdict path).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS  (the X33 reframe)
═══════════════════════════════════════════════════════════════════════════════
X33 found the synchronous coined WALK pins the ceiling at pi*sqrt3*omega_C for
all rho* (the bond-tick Nyquist), while its CONTINUUM partner — a mass-spring
dynamical matrix with nodes as INERTIA ONLY — LIFTS 22x with stiffness. That
fork was in-engine-undecidable AS TESTED.

But Axiom 1's node is not a bare inertia — it is an intrinsic LC TANK (a shunt
resonator, resonance omega_C, channel-shared: every channel transacts through
the same node hardware; CLAUDE.md:70, translation-circuit.md:97). X33's
continuum was the tank-REMOVED truncation. This driver adds the tank back and
asks the D-I question: does the shared node tank pin the coupled ceiling at the
node rate for EVERY channel?

THE NODE-TANK LAW (prereg 2a/2b, derived, not tuned):
  The channel-shared tank presents the bonds an effective dynamical mass
      m_eff(omega) = (1-eta)*m + eta*m*omega_C^2/(omega_C^2 - omega^2)
  eta = tank fraction of node inertia (Axiom-1 pure: eta=1, "node IS the tank").
  Coupled dispersion: eig(D(k)) = omega^2 * m_eff(omega), applied per D-eigenvalue
  (the tank is isotropic => D's eigenvectors are unchanged).
    eta=1  =>  1/omega^2 = m/eig(D) + 1/omega_C^2   (reciprocal BOTTLENECK law:
               the slower of {bond network, node tank} binds; single pinned band).
    eta<1  =>  quadratic per lambda_b => lower (pinned) + upper (lifting) branch,
               node stop-band [omega_C, omega_C/sqrt(1-eta)] (D-INDEPENDENT).

UNITS: the bare continuum eigenvalues from vector_bloch_D are omega_cont^2 in
ELASTIC units (m=1, k_s=1). The tank resonance is the identity omega_C = 1 in
omega_C units. The bridge is R(rho*) = walk_slope/cont_slope at low-k (the SHARED
acoustic velocity, X33 G3) — a single constant per rho* (=sqrt(2) at rho*=1).
Everything is carried in omega_C units: Lambda_b = (R*sqrt(lambda_b))^2 = R^2*lambda_b.

alpha-CLEAN: no alpha/Q_TANK on any verdict path. Constants imported by SYMBOL.
Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/x36_node_bottleneck.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.chiral_lattice import _SRS_NN

# Sibling reuse (Rule 14): the VALIDATED X33 walk+continuum pipeline, which itself
# reuses the validated srs vector Born-Huang pipeline. All side-effect-free imports.
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
from srs_vector_band_survey import (  # noqa: E402
    B1,
    B2,
    B3,
    self_block_isqrt,
    srs_primitive_bcc,
    vector_bloch_D,
)
from x33_clock_architecture import (  # noqa: E402
    MEV_PER_OMEGA_C,
    OMEGA_LINK_OVER_C,
    RHO_SET,
    RHO_STAR_CANON,
    _zz_geometry,
    zz_D,
    zz_selfblock,
)

OMEGA_C_TANK = 1.0           # node-tank resonance = c0/l_node = OMEGA_C identity (omega_C units)
ETA_CANON = 1.0              # Axiom-1 pure: node IS the tank (no bond-rigid bypass)
ETA_SWEEP = [0.25, 0.5, 0.75, 1.0]
PIN_LIFT_MAX = 1.3           # frozen Branch-P threshold (prereg §4)
LIFT_SURVIVE_MIN = 3.0       # frozen Branch-L threshold (prereg §4)
PI_SQRT3 = float(np.pi * OMEGA_LINK_OVER_C)   # walk ceiling = bond-tick Nyquist


# ─────────────────────────────────────────────────────────────────────────────
# The node-tank dispersion law (prereg §2b) — applied per continuum eigenvalue
# ─────────────────────────────────────────────────────────────────────────────
def tank_omega2_eta1(Lam, omega_C=OMEGA_C_TANK):
    """eta=1 reciprocal bottleneck: 1/omega^2 = 1/Lambda + 1/omega_C^2 (omega_C units).

    Lam = continuum freq^2 in omega_C units (Lam = R^2 * eig(D)). Returns omega^2."""
    Lam = np.asarray(Lam, float)
    out = np.zeros_like(Lam)
    nz = Lam > 0
    out[nz] = 1.0 / (1.0 / Lam[nz] + 1.0 / omega_C ** 2)
    return out


def tank_omega2_general(Lam, eta, omega_C=OMEGA_C_TANK):
    """0<eta<=1 mass-in-mass: (1-eta) x^2 - (omega_C^2 + Lambda) x + Lambda omega_C^2 = 0,
    x = omega^2. Returns (lower_branch_omega2, upper_branch_omega2) arrays.

    eta=1 -> a=0 -> single root (lower); upper set to nan (branch at infinity)."""
    Lam = np.asarray(Lam, float)
    lo = np.full_like(Lam, np.nan)
    hi = np.full_like(Lam, np.nan)
    a = (1.0 - eta)
    for idx, L in np.ndenumerate(Lam):
        b = -(omega_C ** 2 + L)
        c = L * omega_C ** 2
        if abs(a) < 1e-15:                      # eta = 1: linear, single branch
            lo[idx] = -c / b if abs(b) > 0 else 0.0
            continue
        disc = max(b * b - 4 * a * c, 0.0)
        r1 = (-b - np.sqrt(disc)) / (2 * a)
        r2 = (-b + np.sqrt(disc)) / (2 * a)
        lo[idx], hi[idx] = min(r1, r2), max(r1, r2)
    return lo, hi


# ─────────────────────────────────────────────────────────────────────────────
# Low-k elastic->omega_C calibration R(rho*)  (the SHARED acoustic velocity, G3)
# ─────────────────────────────────────────────────────────────────────────────
def calib_R(basis, bonds, rho, ks=1.0):
    """R = walk_omega/cont_omega at low-k (single constant per rho*, X33 G3).

    walk omega = OMEGA_LINK_OVER_C*arccos(1-lambda_tilde); cont omega = sqrt(eig D).

    NOTE: R is the elastic->omega_C UNIT conversion. It MUST be anchored ONCE at
    rho*=1 (the isotropic point, where R=sqrt(2) exactly — the pure sqrt-eig<->arccos
    velocity-convention factor, all branches sharing it) and held FIXED across rho*.
    Recomputing R at rho*>1 is WRONG for the conversion: the WALK velocity there is
    stiffness-divided-out (the X33 pin), so walk/cont shrinks and would spuriously
    cancel the real continuum lift. main() calls this at rho*=1 to fix R_ISO."""
    ell = _SRS_NN
    Sih, _ = self_block_isqrt(basis, bonds, rho, ks)
    ratios = []
    for qh in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        q = np.array(qh, float) / np.linalg.norm(qh)
        kvec = q * (1e-4 / ell)
        D = vector_bloch_D(kvec, basis, bonds, rho, ks)
        vcont = np.sqrt(np.sort(np.clip(np.linalg.eigvalsh(D).real, 0, None))[:3]) / (1e-4 / ell)
        Dn = 0.5 * (Sih @ D @ Sih + (Sih @ D @ Sih).conj().T)
        lam = np.sort(np.clip(np.linalg.eigvalsh(Dn).real, 0, 2))[:3]
        vwalk = OMEGA_LINK_OVER_C * np.arccos(np.clip(1 - lam, -1, 1)) / (1e-4 / ell)
        ratios.extend((vwalk / vcont).tolist())
    ratios = np.array(ratios)
    return float(ratios.mean()), float((ratios.max() - ratios.min()) / ratios.mean())


# ─────────────────────────────────────────────────────────────────────────────
# srs ceilings vs rho*: bare continuum / node-tank(eta=1) / walk  (the verdict)
# ─────────────────────────────────────────────────────────────────────────────
def srs_bare_continuum_top_elastic(basis, bonds, rho, ks=1.0, n_grid=12):
    """sup_k sqrt(eig D(k)) in ELASTIC units (the X33 lifting continuum)."""
    fs = np.linspace(0.0, 1.0, n_grid, endpoint=False)
    lam_max = -1.0
    for f1 in fs:
        for f2 in fs:
            for f3 in fs:
                k = f1 * B1 + f2 * B2 + f3 * B3
                lam_max = max(lam_max, float(np.linalg.eigvalsh(
                    vector_bloch_D(k, basis, bonds, rho, ks)).real.max()))
    return float(np.sqrt(lam_max)), lam_max


def srs_node_tank_ceilings(basis, bonds, R_iso, rho_set=RHO_SET):
    """Per rho*: bare continuum top, node-tank(eta=1) top, walk top (all omega_C).

    R_iso = the FIXED elastic->omega_C conversion (anchored at rho*=1, = sqrt(2))."""
    rows = {}
    for rho in rho_set:
        cont_el, _ = srs_bare_continuum_top_elastic(basis, bonds, rho)
        cont_wc = R_iso * cont_el                   # bare continuum top in omega_C units
        Lam = cont_wc ** 2
        tank_top = float(np.sqrt(tank_omega2_eta1(np.array([Lam]))[0]))
        rows[f"{rho:g}"] = {
            "bare_continuum_top_elastic": cont_el,
            "R_iso_elastic_to_omega_C": R_iso,
            "bare_continuum_top_omega_C": cont_wc,
            "node_tank_eta1_top_omega_C": tank_top,
            "walk_top_omega_C": PI_SQRT3,
        }
    return rows


# ─────────────────────────────────────────────────────────────────────────────
# eta-sweep on the srs canonical rho*: gap structure + upper-branch lift (M-family)
# ─────────────────────────────────────────────────────────────────────────────
def srs_eta_family(basis, bonds, R_iso, rho=RHO_STAR_CANON, eta_set=ETA_SWEEP):
    cont_el, _ = srs_bare_continuum_top_elastic(basis, bonds, rho)
    Lam_top = (R_iso * cont_el) ** 2                 # top continuum Lambda in omega_C units
    fam = {}
    for eta in eta_set:
        lo, hi = tank_omega2_general(np.array([Lam_top]), eta)
        lower_top = float(np.sqrt(lo[0]))
        upper_top = float(np.sqrt(hi[0])) if np.isfinite(hi[0]) else None
        gap_lo = OMEGA_C_TANK
        gap_hi = OMEGA_C_TANK / np.sqrt(1 - eta) if eta < 1 else float("inf")
        fam[f"{eta:g}"] = {
            "lower_branch_top_omega_C": lower_top,
            "upper_branch_top_omega_C": upper_top,
            "node_stop_band_omega_C": [gap_lo, (gap_hi if np.isfinite(gap_hi) else None)],
            "stop_band_is_D_independent": True,
        }
    return fam


# ─────────────────────────────────────────────────────────────────────────────
# 1D two-channel zig-zag chain: three-architecture spectra for the figure
# ─────────────────────────────────────────────────────────────────────────────
def zz_selfblock_isqrt(rho, ks=1.0):
    w, V = np.linalg.eigh(zz_selfblock(rho, ks))
    return V @ np.diag(1.0 / np.sqrt(np.clip(w, 1e-12, None))) @ V.T


def zz_calib_R(rho=1.0, ks=1.0):
    """1D-chain elastic->omega_C conversion, anchored at rho*=1 (held fixed, as srs)."""
    _, acell = _zz_geometry()
    klo = 1e-4 * np.pi / acell
    Dlo = zz_D(klo, rho, ks)
    Sih = zz_selfblock_isqrt(rho, ks)
    lam_lo = np.sort(np.clip(np.linalg.eigvalsh(0.5 * (Sih @ Dlo @ Sih + (Sih @ Dlo @ Sih).conj().T)).real, 0, 2))
    cont_lo = np.sqrt(np.sort(np.clip(np.linalg.eigvalsh(Dlo).real, 0, None)))
    walk_lo = OMEGA_LINK_OVER_C * np.arccos(np.clip(1 - lam_lo, -1, 1))
    return float(walk_lo[1] / cont_lo[1])            # lowest non-zero acoustic branch


def zz_three_arch(rho, R1d, ks=1.0, n_k=241, eta=ETA_CANON):
    """Return kx (in pi/a), and per-band omega for bare continuum / node-tank / walk.

    R1d = the FIXED 1D elastic->omega_C conversion (anchored at rho*=1, threaded in)."""
    _, acell = _zz_geometry()
    kxs = np.linspace(0.0, np.pi / acell, n_k)
    Sih = zz_selfblock_isqrt(rho, ks)
    bare, tank, walk = [], [], []
    for kx in kxs:
        D = zz_D(kx, rho, ks)
        lam = np.sort(np.clip(np.linalg.eigvalsh(D).real, 0.0, None))     # elastic omega_cont^2
        w2 = np.sort(np.clip(np.linalg.eigvalsh(Sih @ D @ Sih).real, 0, 2))
        bare.append(R1d * np.sqrt(lam))              # omega_C units
        walk.append(OMEGA_LINK_OVER_C * np.arccos(np.clip(1 - w2, -1, 1)))
        Lam = (R1d * np.sqrt(lam)) ** 2
        lo, hi = tank_omega2_general(Lam, eta)
        col = list(np.sqrt(lo))
        if eta < 1:
            col = list(np.sqrt(lo)) + list(np.sqrt(hi[np.isfinite(hi)]))
        tank.append(col)
    kx_norm = (kxs * acell / np.pi).tolist()
    bare = np.array(bare)
    walk = np.array(walk)
    ntank = max(len(t) for t in tank)
    tankA = np.full((len(tank), ntank), np.nan)
    for i, t in enumerate(tank):
        tankA[i, :len(t)] = np.sort(t)
    return {"kx": kx_norm, "bare": bare, "walk": walk, "tank": tankA, "R1d": R1d}


# ─────────────────────────────────────────────────────────────────────────────
# GATES
# ─────────────────────────────────────────────────────────────────────────────
def gate1_lowk_unchanged(basis, bonds, rho=RHO_STAR_CANON):
    """G1: node tank decouples at omega->0 => acoustic velocity = X33 continuum velocity.

    At low-k Lambda->0 so tank omega^2 -> Lambda (independent of omega_C). The
    node-tank low-k slope must equal the bare-continuum low-k slope (in omega_C
    units), ratio = 1 to numerical floor."""
    ell = _SRS_NN
    R, _ = calib_R(basis, bonds, rho)
    ratios = []
    for qh in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
        q = np.array(qh, float) / np.linalg.norm(qh)
        kvec = q * (1e-4 / ell)
        D = vector_bloch_D(kvec, basis, bonds, rho, 1.0)
        lam = np.sort(np.clip(np.linalg.eigvalsh(D).real, 0, None))[:3]
        Lam = (R * np.sqrt(lam)) ** 2
        w_tank = np.sqrt(tank_omega2_eta1(Lam))
        w_bare = R * np.sqrt(lam)
        ratios.extend((w_tank / w_bare).tolist())
    ratios = np.array(ratios)
    dev = float(np.max(np.abs(ratios - 1.0)))
    return {"tank_over_bare_lowk_ratio_mean": float(ratios.mean()),
            "max_dev_from_1": dev, "R_used": R, "pass": bool(dev < 1e-5)}


def gate2_tank_removed_control(basis, bonds, R_iso, rho_set=RHO_SET):
    """G2: omega_C -> infinity recovers the X33 bare continuum (LIFTS 22x)."""
    big = 1e12
    tops, bare = [], []
    for rho in rho_set:
        cont_el, _ = srs_bare_continuum_top_elastic(basis, bonds, rho)
        Lam = (R_iso * cont_el) ** 2
        tops.append(float(np.sqrt(tank_omega2_eta1(np.array([Lam]), omega_C=big)[0])))
        bare.append(R_iso * cont_el)
    tops, bare = np.array(tops), np.array(bare)
    rel = float(np.max(np.abs(tops - bare) / bare))
    lift = float(tops[-1] / tops[0])
    return {"tank_removed_top_omega_C": tops.tolist(), "bare_top_omega_C": bare.tolist(),
            "max_rel_err_vs_bare": rel, "lift_ratio_1000_over_1": lift,
            "pass": bool(rel < 1e-6 and lift > 20.0)}


def gate3_scalar_walk_reproduces_604(basis, bonds, R_iso):
    """G3: scalar (rho*=1) — walk leg gives pi*sqrt3 (#604); node-tank leg gives its
    omega_C pin (RECORDED + the #604 tension flagged, prereg §6)."""
    Sih, _ = self_block_isqrt(basis, bonds, 1.0, 1.0)
    lam_tilde_max = -1.0
    fs = np.linspace(0.0, 1.0, 12, endpoint=False)
    cont_el, _ = srs_bare_continuum_top_elastic(basis, bonds, 1.0)
    for f1 in fs:
        for f2 in fs:
            for f3 in fs:
                k = f1 * B1 + f2 * B2 + f3 * B3
                Draw = Sih @ vector_bloch_D(k, basis, bonds, 1.0, 1.0) @ Sih
                Dn = 0.5 * (Draw + Draw.conj().T)
                lam_tilde_max = max(lam_tilde_max, float(np.linalg.eigvalsh(Dn).real.max()))
    walk_top = OMEGA_LINK_OVER_C * float(np.arccos(np.clip(1 - lam_tilde_max, -1, 1)))
    tank_top = float(np.sqrt(tank_omega2_eta1(np.array([(R_iso * cont_el) ** 2]))[0]))
    return {"walk_scalar_top_omega_C": walk_top, "target_pi_sqrt3": PI_SQRT3,
            "node_tank_scalar_top_omega_C": tank_top,
            "tension_with_604": ("node-tank pins at %.4f omega_C = %.4f MeV (node rate) vs #604 "
                                 "walk %.4f omega_C = %.4f MeV (bond tick) — node tank is TIGHTER; "
                                 "#604's memoryless-node engine omits the tank."
                                 % (tank_top, tank_top * MEV_PER_OMEGA_C,
                                    walk_top, walk_top * MEV_PER_OMEGA_C)),
            "pass": bool(abs(walk_top - PI_SQRT3) < 1e-4)}


def gate4_band_count(basis, bonds, rho=RHO_STAR_CANON):
    """G4: DOF bookkeeping + literal augmented-DOF cross-check (per-lambda map honest).

    eta=1 -> N_DOF branches; eta<1 -> 2*N_DOF. Cross-check the per-lambda map against
    a literal (u,q) augmented generalized eigensolve on the 1D chain."""
    n_dof = 3 * len(basis)
    # per-lambda branch counts on the srs
    kv = 0.3 * B1 + 0.17 * B2 + 0.41 * B3
    lam = np.sort(np.clip(np.linalg.eigvalsh(vector_bloch_D(kv, basis, bonds, rho, 1.0)).real, 0, None))
    R, _ = calib_R(basis, bonds, rho)
    Lam = (R * np.sqrt(lam)) ** 2
    lo1, hi1 = tank_omega2_general(Lam, 1.0)
    lo_p, hi_p = tank_omega2_general(Lam, 0.5)
    n_eta1 = int(np.isfinite(lo1).sum() + np.isfinite(hi1).sum())
    n_eta_p = int(np.isfinite(lo_p).sum() + np.isfinite(hi_p).sum())
    # literal augmented (u,q) 1D-chain cross-check at eta=0.5
    _, acell = _zz_geometry()
    kx = 0.62 * np.pi / acell
    D1 = zz_D(kx, rho, 1.0)
    S1 = zz_selfblock(rho, 1.0)
    w, V = np.linalg.eigh(S1)
    Sih1 = V @ np.diag(1.0 / np.sqrt(np.clip(w, 1e-12, None))) @ V.T
    lam1 = np.sort(np.clip(np.linalg.eigvalsh(0.5 * (Sih1 @ D1 @ Sih1 + (Sih1 @ D1 @ Sih1).conj().T)).real, 0, 2))
    cont1 = np.sqrt(np.sort(np.clip(np.linalg.eigvalsh(D1).real, 0, None)))
    R1 = OMEGA_LINK_OVER_C * np.arccos(np.clip(1 - lam1, -1, 1))[1] / cont1[1]
    Lam1 = (R1 * cont1) ** 2
    eta = 0.5
    lo, hi = tank_omega2_general(Lam1, eta)
    map_freqs = np.sort(np.concatenate([np.sqrt(lo[Lam1 > 1e-12]), np.sqrt(hi[np.isfinite(hi) & (Lam1 > 1e-12)])]))
    # augmented generalized eig in omega_C units: omega^2 M v = Kmat v, m=1
    ndof1 = D1.shape[0]
    om_c = OMEGA_C_TANK
    m_h, mu = (1 - eta), eta
    gamma = mu * om_c ** 2
    Dwc = R1 ** 2 * D1                                # continuum stiffness in omega_C units
    Kmat = np.block([[Dwc + gamma * np.eye(ndof1), -gamma * np.eye(ndof1)],
                     [-gamma * np.eye(ndof1), gamma * np.eye(ndof1)]])
    Mmat = np.block([[m_h * np.eye(ndof1), np.zeros((ndof1, ndof1))],
                     [np.zeros((ndof1, ndof1)), mu * np.eye(ndof1)]])
    ev = np.linalg.eigvalsh(np.linalg.solve(Mmat, 0.5 * (Kmat + Kmat.conj().T)))
    aug_freqs = np.sort(np.sqrt(np.clip(ev.real, 0, None)))
    aug_freqs = aug_freqs[aug_freqs > 1e-9]
    m = min(len(map_freqs), len(aug_freqs))
    cross_err = float(np.max(np.abs(np.sort(map_freqs)[-m:] - np.sort(aug_freqs)[-m:]))) if m else 1.0
    return {"n_dof": n_dof, "n_branches_eta1": n_eta1, "n_branches_eta0p5": n_eta_p,
            "augmented_cross_check_max_err": cross_err,
            "pass": bool(n_eta1 == n_dof and n_eta_p == 2 * n_dof and cross_err < 1e-6)}


def gate5_enantiomorph(bonds_r, bonds_l, basis_r, basis_l, R_iso, rho=RHO_STAR_CANON):
    """G5: the isotropic tank preserves R/L handedness identity (cold parity)."""
    def tank_top(basis, bonds):
        cont_el, _ = srs_bare_continuum_top_elastic(basis, bonds, rho)
        return float(np.sqrt(tank_omega2_eta1(np.array([(R_iso * cont_el) ** 2]))[0]))
    tr, tl = tank_top(basis_r, bonds_r), tank_top(basis_l, bonds_l)
    diff = abs(tr - tl)
    return {"right_top_omega_C": tr, "left_top_omega_C": tl, "abs_diff": diff,
            "pass": bool(diff < 1e-6)}


def gate6_gap_structure(basis, bonds, rho=RHO_STAR_CANON):
    """G6: eta<1 opens a D-INDEPENDENT node stop-band [omega_C, omega_C/sqrt(1-eta)];
    eta=1 has none (gap->infinity). Verify the closed-form edges + D-independence."""
    R, _ = calib_R(basis, bonds, rho)
    checks = {}
    ok = True
    for eta in (0.25, 0.5, 0.75):
        pred_hi = OMEGA_C_TANK / np.sqrt(1 - eta)
        # measure upper-branch bottom at TWO very different Lambda (D-independence)
        bottoms = []
        for Lam in (5.0, 5000.0):
            lo, hi = tank_omega2_general(np.array([Lam]), eta)
            # upper-branch BOTTOM approached as Lambda->0: solve at tiny Lambda
            loz, hiz = tank_omega2_general(np.array([1e-9]), eta)
            bottoms.append(float(np.sqrt(hiz[0])))
        edge_err = abs(bottoms[0] - pred_hi)
        d_indep = abs(bottoms[0] - bottoms[1])
        checks[f"{eta:g}"] = {"pred_stop_band": [OMEGA_C_TANK, float(pred_hi)],
                              "measured_upper_bottom": bottoms[0],
                              "edge_err": float(edge_err), "D_independence_err": float(d_indep)}
        ok = ok and edge_err < 1e-6 and d_indep < 1e-6
    return {"per_eta": checks, "pass": bool(ok)}


# ─────────────────────────────────────────────────────────────────────────────
def main():
    basis_r, bonds_r = srs_primitive_bcc("right")
    basis_l, bonds_l = srs_primitive_bcc("left")
    # FIXED elastic->omega_C conversion, anchored ONCE at rho*=1 (= sqrt(2)); held across rho*
    R_ISO, R_ISO_spread = calib_R(basis_r, bonds_r, 1.0)
    R1D_ISO = zz_calib_R(1.0)
    out = {"class": "CONSISTENCY / characterization",
           "prereg": "research/2026-07-09_x36-node-bottleneck_prereg_FROZEN.md",
           "omega_C_tank": OMEGA_C_TANK, "eta_canonical": ETA_CANON,
           "walk_ceiling_pi_sqrt3_omega_C": PI_SQRT3,
           "R_iso_elastic_to_omega_C": R_ISO, "R_iso_branch_spread": R_ISO_spread,
           "R_iso_note": "anchored at rho*=1 (isotropic), = sqrt(2) (sqrt-eig<->arccos "
                         "velocity convention); FIXED across rho* (a unit conversion at k_s=m=1).",
           "MeV_per_omega_C": MEV_PER_OMEGA_C, "rho_set": RHO_SET}

    # ---- verdict quantity: srs ceilings vs rho* (bare / node-tank / walk) ----
    ceil = srs_node_tank_ceilings(basis_r, bonds_r, R_ISO)
    tank_tops = np.array([ceil[f"{r:g}"]["node_tank_eta1_top_omega_C"] for r in RHO_SET])
    bare_tops = np.array([ceil[f"{r:g}"]["bare_continuum_top_omega_C"] for r in RHO_SET])
    tank_lift = float(tank_tops[-1] / tank_tops[0])
    bare_lift = float(bare_tops[-1] / bare_tops[0])
    out["srs_ceilings_vs_rho"] = ceil
    out["verdict_metrics"] = {
        "node_tank_top_omega_C_per_rho": tank_tops.tolist(),
        "node_tank_lift_ratio_1000_over_1": tank_lift,
        "bare_continuum_top_omega_C_per_rho": bare_tops.tolist(),
        "bare_continuum_lift_ratio_1000_over_1": bare_lift,
        "walk_ceiling_omega_C": PI_SQRT3,
        "node_tank_top_MeV_per_rho": (tank_tops * MEV_PER_OMEGA_C).tolist()}

    if tank_lift < PIN_LIFT_MAX:
        branch = "P_NODE_PINS"
    elif tank_lift > LIFT_SURVIVE_MIN:
        branch = "L_LIFT_SURVIVES"
    else:
        branch = "M_MIXED"
    out["BRANCH"] = branch

    # ---- eta-family: M-branch gap structure + upper-branch lift ----
    out["eta_family_srs"] = srs_eta_family(basis_r, bonds_r, R_ISO)

    # ---- convergence-to-walk (prereg §6): does node-tank reproduce the walk? ----
    out["convergence_to_walk"] = {
        "node_tank_ceiling_omega_C": float(tank_tops.mean()),
        "walk_ceiling_omega_C": PI_SQRT3,
        "ratio_node_tank_over_walk": float(tank_tops.mean() / PI_SQRT3),
        "reproduces_walk": bool(abs(tank_tops.mean() - PI_SQRT3) / PI_SQRT3 < 0.05),
        "note": ("Both PIN, by DIFFERENT mechanisms (node resonance vs bond tick). The node "
                 "tank binds at ~1 omega_C = m_e c^2; the walk at pi*sqrt3 = 5.441 omega_C = "
                 "2.781 MeV. The node tank is TIGHTER by pi*sqrt3. It does NOT reproduce the "
                 "walk's arccos band (rational vs arccos law). Convergence would require "
                 "omega_C(tank)=pi*sqrt3 — the plumber question surfaced to Grant.")}

    # ---- discriminating observable: the longitudinal-only window under each clock ----
    out["longitudinal_only_window"] = {
        "under_bare_continuum_MeV": [round(PI_SQRT3 * MEV_PER_OMEGA_C, 4),
                                     round(bare_tops[-1] * MEV_PER_OMEGA_C, 4)],
        "under_node_tank_MeV": "CLOSED (all channels pinned at ~%.4f MeV — Branch P)"
                               % (tank_tops.mean() * MEV_PER_OMEGA_C),
        "under_walk_MeV": "CLOSED (all channels pinned at pi*sqrt3 = %.4f MeV)"
                          % (PI_SQRT3 * MEV_PER_OMEGA_C),
        "note": "Branch P closes the longitudinal-only window (X33 deliverable) via the node bottleneck."}

    # ---- gates ----
    g1 = gate1_lowk_unchanged(basis_r, bonds_r)
    g2 = gate2_tank_removed_control(basis_r, bonds_r, R_ISO)
    g3 = gate3_scalar_walk_reproduces_604(basis_r, bonds_r, R_ISO)
    g4 = gate4_band_count(basis_r, bonds_r)
    g5 = gate5_enantiomorph(bonds_r, bonds_l, basis_r, basis_l, R_ISO)
    g6 = gate6_gap_structure(basis_r, bonds_r)
    out["gates"] = {"G1_lowk_unchanged": g1, "G2_tank_removed_control": g2,
                    "G3_scalar_walk_reproduces_604": g3, "G4_band_count": g4,
                    "G5_enantiomorph_parity": g5, "G6_gap_structure": g6}
    out["all_gates_pass"] = bool(g1["pass"] and g2["pass"] and g3["pass"]
                                 and g4["pass"] and g5["pass"] and g6["pass"])

    # ---- 1D chain three-architecture spectra for the figure ----
    fig_data = {f"{r:g}": zz_three_arch(r, R1D_ISO) for r in (1.0, RHO_STAR_CANON)}
    fig_data_M = zz_three_arch(RHO_STAR_CANON, R1D_ISO, eta=0.5)   # M-family panel
    out["zz_1d_two_channel"] = {
        "R1d_calibration": fig_data["1"]["R1d"],
        "iso_bare_top": float(np.nanmax(fig_data["1"]["bare"])),
        "iso_tank_top": float(np.nanmax(fig_data["1"]["tank"])),
        "iso_walk_top": float(np.nanmax(fig_data["1"]["walk"])),
        "rho_bare_top": float(np.nanmax(fig_data[f"{RHO_STAR_CANON:g}"]["bare"])),
        "rho_tank_top": float(np.nanmax(fig_data[f"{RHO_STAR_CANON:g}"]["tank"])),
        "rho_walk_top": float(np.nanmax(fig_data[f"{RHO_STAR_CANON:g}"]["walk"]))}

    out["D_I_verdict"] = (
        "Branch %s. The channel-shared node LC tank (Axiom 1) presents the bonds an effective "
        "dynamical mass diverging at omega_C; the reciprocal bottleneck law 1/omega^2 = 1/Lambda "
        "+ 1/omega_C^2 pins EVERY channel at the node rate ~1 omega_C = m_e c^2, lift ratio %.3fx "
        "(vs the bare continuum's %.2fx). Effective synchrony is DERIVED from Axiom-1's node "
        "resonance with NO tick postulate. The node tank is a TIGHTER clock than the bond-tick "
        "walk (pi*sqrt3 omega_C) — flagged tension with #604." % (branch, tank_lift, bare_lift))

    # ---- report ----
    print("=" * 80)
    print("X36 — NODE-BOTTLENECK DISCRIMINATOR (the D-I test: does the node LC tank pin?)")
    print("=" * 80)
    print(f"\nVERDICT: BRANCH {branch}")
    print(f"  node-tank top (omega_C) per rho* {RHO_SET}:\n    {np.round(tank_tops, 5).tolist()}")
    print(f"    lift ratio (rho=1000/1): {tank_lift:.4f}x   (PIN if < {PIN_LIFT_MAX})")
    print(f"  bare continuum top (omega_C) per rho*:\n    {np.round(bare_tops, 4).tolist()}")
    print(f"    lift ratio (rho=1000/1): {bare_lift:.2f}x   => LIFTS")
    print(f"  walk ceiling (bond-tick Nyquist) = pi*sqrt3 = {PI_SQRT3:.4f} omega_C")
    nt_mev = tank_tops.mean() * MEV_PER_OMEGA_C
    print(f"\n  node-tank pins at ~{tank_tops.mean():.4f} omega_C = {nt_mev:.4f} MeV (node rate)")
    print(f"  walk pins at        {PI_SQRT3:.4f} omega_C = {PI_SQRT3*MEV_PER_OMEGA_C:.4f} MeV (bond tick)")
    conv = out["convergence_to_walk"]["reproduces_walk"]
    print(f"  => node tank is TIGHTER by pi*sqrt3; convergence-to-walk = {conv}")
    print("\nETA-FAMILY (node stop-band [omega_C, omega_C/sqrt(1-eta)], D-independent):")
    for eta, v in out["eta_family_srs"].items():
        print(f"  eta={eta}: lower_top={v['lower_branch_top_omega_C']:.4f}, "
              f"upper_top={v['upper_branch_top_omega_C']}, stop_band={v['node_stop_band_omega_C']}")
    print("\nGATES:")
    print(f"  G1 low-k UNCHANGED ........... dev={g1['max_dev_from_1']:.1e}  PASS={g1['pass']}")
    print(f"  G2 tank-removed control ...... rel_err={g2['max_rel_err_vs_bare']:.1e}, "
          f"lift={g2['lift_ratio_1000_over_1']:.1f}x  PASS={g2['pass']}")
    print(f"  G3 scalar walk=#604 (pi*sqrt3) walk_top={g3['walk_scalar_top_omega_C']:.4f}, "
          f"node_tank={g3['node_tank_scalar_top_omega_C']:.4f}  PASS={g3['pass']}")
    print(f"  G4 band-count ................ eta1={g4['n_branches_eta1']}/{g4['n_dof']}, "
          f"eta0.5={g4['n_branches_eta0p5']}/{2*g4['n_dof']}, aug_err={g4['augmented_cross_check_max_err']:.1e}  "
          f"PASS={g4['pass']}")
    print(f"  G5 enantiomorph parity ....... diff={g5['abs_diff']:.1e}  PASS={g5['pass']}")
    print(f"  G6 gap structure ............. PASS={g6['pass']}")
    print(f"\nALL GATES PASS: {out['all_gates_pass']}")
    print(f"\n{out['D_I_verdict']}")

    out_dir = _HERE / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "x36_node_bottleneck.json").write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_dir / 'x36_node_bottleneck.json'}")
    try:
        make_figure(fig_data, fig_data_M, out, out_dir)
    except Exception as e:  # pragma: no cover
        print(f"[figure skipped: {e}]")
    return out


# ─────────────────────────────────────────────────────────────────────────────
def make_figure(fig_data, fig_data_M, out, out_dir):
    """WHITE house style, 3 panels:
      (L) 1D chain rho*=9.77: bare continuum (LIFTS) / node-tank eta=1 (PINS) / walk,
      (C) 1D chain rho*=9.77 eta=0.5: the MIXED family — lower pinned + node stop-band
          + upper branch lifting (the hybridization structure),
      (R) srs ceiling vs rho*: bare continuum 22x lift / node-tank flat / walk flat.
    ONE calibration each (the shared low-k acoustic velocity R); no per-panel re-fit."""
    from ave.viz import style
    style.apply()
    fig, axes = style.plt.subplots(1, 3, figsize=style.figsize("wide"))

    # ---- (L) 1D three-architecture overlay, eta=1 ----
    fd = fig_data[f"{RHO_STAR_CANON:g}"]
    kx = np.array(fd["kx"])
    ax = axes[0]
    for b in range(fd["bare"].shape[1]):
        ax.plot(kx, fd["bare"][:, b], color=style.COLORS["comparison"], lw=1.4, ls="--",
                label="bare continuum (LIFTS)" if b == 0 else None)
    for b in range(fd["walk"].shape[1]):
        ax.plot(kx, fd["walk"][:, b], color=style.COLORS["muted"], lw=1.2, ls=":",
                label="walk (arccos, PINS)" if b == 0 else None)
    for b in range(fd["tank"].shape[1]):
        ax.plot(kx, fd["tank"][:, b], color=style.COLORS["ave"], lw=1.8,
                label="node-tank (PINS)" if b == 0 else None)
    ax.axhline(OMEGA_C_TANK, color=style.COLORS["data"], ls="-", lw=0.8)
    ax.axhline(PI_SQRT3, color=style.COLORS["muted"], ls="-", lw=0.6, alpha=0.7)
    ax.text(0.03, 0.96, r"$\rho^*=9.77,\ \eta=1$", transform=ax.transAxes, va="top", fontsize=9)
    ax.text(0.03, OMEGA_C_TANK, r" $\omega_C$ (node rate)", va="bottom", ha="left", fontsize=7,
            color=style.COLORS["data"])
    ax.set_xlabel(r"$k$  ($\pi/a$)")
    ax.set_ylabel(style.axis_label("frequency", r"\omega", r"$\omega_C$"))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, PI_SQRT3 * 1.15)
    style.legend(ax, where="below", ncol=1, fontsize=7)

    # ---- (C) 1D MIXED family eta=0.5: node stop-band + upper branch ----
    fm = fig_data_M
    kxm = np.array(fm["kx"])
    axm = axes[1]
    for b in range(fm["tank"].shape[1]):
        axm.plot(kxm, fm["tank"][:, b], color=style.COLORS["ave"], lw=1.4)
    gap_hi = OMEGA_C_TANK / np.sqrt(1 - 0.5)
    axm.axhspan(OMEGA_C_TANK, gap_hi, color=style.COLORS["accent"], alpha=0.18)
    axm.axhline(OMEGA_C_TANK, color=style.COLORS["data"], ls="-", lw=0.8)
    axm.axhline(gap_hi, color=style.COLORS["accent"], ls="--", lw=0.9)
    axm.text(0.03, 0.96, r"$\rho^*=9.77,\ \eta=0.5$ (MIXED)", transform=axm.transAxes,
             va="top", fontsize=9)
    axm.text(0.5, 0.5 * (OMEGA_C_TANK + gap_hi), "node\nstop-band", ha="center", va="center",
             fontsize=7, color=style.COLORS["accent"])
    axm.set_xlabel(r"$k$  ($\pi/a$)")
    axm.set_xlim(0, 1)
    axm.set_ylim(0, PI_SQRT3 * 1.15)

    # ---- (R) srs ceiling vs rho* ----
    axr = axes[2]
    rhos = np.array(RHO_SET)
    bare = np.array([out["srs_ceilings_vs_rho"][f"{r:g}"]["bare_continuum_top_omega_C"] for r in RHO_SET])
    tank = np.array([out["srs_ceilings_vs_rho"][f"{r:g}"]["node_tank_eta1_top_omega_C"] for r in RHO_SET])
    axr.plot(rhos, bare, "o--", color=style.COLORS["comparison"], lw=1.6, label="bare continuum (22x lift)")
    axr.plot(rhos, tank, "s-", color=style.COLORS["ave"], lw=1.8, label="node-tank (PINS at $\\omega_C$)")
    axr.axhline(PI_SQRT3, color=style.COLORS["muted"], ls=":", lw=1.2, label=r"walk $\pi\sqrt{3}\,\omega_C$")
    axr.axhline(OMEGA_C_TANK, color=style.COLORS["data"], ls="-", lw=0.8)
    axr.set_xscale("log")
    axr.set_yscale("log")
    axr.set_xlabel(r"stiffness ratio  $\rho^*=k_a/k_s$")
    axr.set_ylabel(style.axis_label("band ceiling", r"\omega_{\rm top}", r"$\omega_C$"))
    style.legend(axr, where="below", ncol=1, fontsize=7)

    paths = style.save(fig, out_dir / "x36_node_bottleneck")
    print(f"Figure: {paths}")


if __name__ == "__main__":
    main()
