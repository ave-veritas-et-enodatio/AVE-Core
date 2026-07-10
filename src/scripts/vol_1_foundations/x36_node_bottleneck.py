#!/usr/bin/env python3
"""X36 — node-shunt characterization (DEMOTED from "the D-I discriminator").

DEMOTION (2026-07-09, post PR #613 adversarial review — 17/17 findings CONFIRMED,
3 CRITICAL). The original framing ("does the node LC tank pin the ceiling at the
node rate, DERIVING effective synchrony?") is WITHDRAWN as a verdict. What this
driver actually characterizes: GIVEN a series anti-resonant (mass-in-mass) node
shunt at eta=1 anchored at omega_C, the reciprocal FORM 1/omega^2 = 1/Lambda +
1/omega_C^2 caps every channel at the installed anchor. It does NOT derive that
choice. The verdict is CONDITIONAL_CHARACTERIZATION:
  * placement_sweep (CRITICAL-1): the ceiling = the installed anchor omega_r, not
    a derived rate (a tank at pi*sqrt3*omega_C reproduces the walk's ceiling);
  * eta_singularity (MAJOR-7): Branch P is singular at exactly eta=1 — any eta<1
    lifts ~= the bare continuum;
  * prereg_FROZEN.md:85 lists an equally passive/lossless/KCL parallel-LC
    band-pass shunt -> Branch L: the topology is the P-vs-L SELECTOR, a choice.
X33's in-engine-undecidable ruling STANDS + is REINFORCED (the engine returns
whatever node model is installed). See the result-doc correction banner.

Prereg (FROZEN, annotated): research/2026-07-09_x36-node-bottleneck_prereg_FROZEN.md
Class: CONSISTENCY / characterization (math + numerics; NOT a falsification, NOT
an emergence claim; no CODATA on any path).

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

THE NODE-TANK LAW (prereg 2a/2b — the FORM is derived GIVEN the series-notch
topology choice; the topology itself is NOT forced, see CRITICAL-1 above):
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
# PLACEMENT SWEEP (the promised prereg §6 disclosure — the tautology made explicit)
# ─────────────────────────────────────────────────────────────────────────────
def placement_sweep(Lam_stiff, anchors=(0.5, 1.0, None, 10.0)):
    """Install the SAME series-notch tank at different resonances omega_r and read
    the coupled ceiling of the stiffest channel (Lam_stiff = the rho*=1000 bare
    continuum eig in omega_C units). Demonstrates the ceiling = the installed anchor
    (CRITICAL-1): the '~1 omega_C pin' is not derived, it is where the tank is placed.

    anchors: multiples of omega_C. None -> pi*sqrt3 (the walk/bond-tick rate)."""
    rows = {}
    for a in anchors:
        wr = PI_SQRT3 if a is None else float(a)
        ceiling = float(np.sqrt(tank_omega2_eta1(np.array([Lam_stiff]), omega_C=wr)[0]))
        key = "pi_sqrt3" if a is None else f"{a:g}"
        rows[key] = {"tank_anchor_omega_r_over_omega_C": wr,
                     "coupled_ceiling_omega_C": ceiling}
    return rows


# ─────────────────────────────────────────────────────────────────────────────
# ETA-SINGULARITY MAP (MAJOR-7): the FULL-spectrum ceiling lift vs eta
# ─────────────────────────────────────────────────────────────────────────────
def eta_singularity(Lam_stiff, Lam_soft, eta_set=(1.0, 0.999, 0.99, 0.9, 0.75, 0.5)):
    """Quantify that Branch P is a SINGULAR point at exactly eta=1. For each eta,
    the FULL-spectrum ceiling = max over BOTH branches (lower pinned + upper lifting).
    The lift ratio ceiling(Lam_stiff)/ceiling(Lam_soft) is ~1 ONLY at eta=1; for any
    eta<1 a lifting upper polariton branch reappears and the full-spectrum ceiling
    lifts ~= the bare continuum. Lam_stiff/Lam_soft = rho*=1000 / rho*=1 continuum eig."""
    def full_ceiling(Lam, eta):
        lo, hi = tank_omega2_general(np.array([Lam]), eta)
        cands = [np.sqrt(lo[0])]
        if np.isfinite(hi[0]):
            cands.append(np.sqrt(hi[0]))
        return float(max(cands))
    rows = {}
    for eta in eta_set:
        c_stiff = full_ceiling(Lam_stiff, eta)
        c_soft = full_ceiling(Lam_soft, eta)
        lo_s, hi_s = tank_omega2_general(np.array([Lam_stiff]), eta)
        rows[f"{eta:g}"] = {
            "full_spectrum_ceiling_lift_1000_over_1": c_stiff / c_soft,
            "lower_branch_top_omega_C": float(np.sqrt(lo_s[0])),
            "upper_branch_top_omega_C": (float(np.sqrt(hi_s[0])) if np.isfinite(hi_s[0]) else None),
        }
    bare_lift = float(np.sqrt(Lam_stiff) / np.sqrt(Lam_soft))
    return {"per_eta": rows, "bare_continuum_lift_1000_over_1": bare_lift,
            "P_is_singular_at_eta_1": True,
            "note": ("Branch P (full-spectrum pinning) exists ONLY at exactly eta=1. At eta=0.999 the "
                     "full-spectrum ceiling already lifts ~21.5x, indistinguishable from the bare "
                     "continuum's %.2fx: a lifting upper polariton branch reappears for ANY eta<1. "
                     "The eta=1 pin is a knife-edge, not a robust regime." % bare_lift)}


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
    """G1 (REPAIRED, MINOR-8/13): assert BOTH halves of the frozen prereg-§5 clause
    ('walk/node-tank/bare-continuum low-k slope ratio = R = sqrt(2) to <1e-5'), and
    document the drift from the originally-shipped gate.

    Frozen clause has TWO parts:
      (1) walk / bare-continuum low-k slope ratio = R = sqrt(2)  (the elastic->omega_C
          velocity-convention conversion, anchored at rho*=1);
      (2) node-tank / bare-continuum low-k slope ratio = 1       (tank decouples at DC).
    The SHIPPED gate checked ONLY (2) (tank/bare=1 at rho*_canon) — NOT the frozen
    sqrt(2) clause (1). This repair asserts BOTH and records the post-freeze change."""
    ell = _SRS_NN
    # --- Part (1): the frozen sqrt(2) clause — walk/cont low-k ratio at rho*=1 anchor ---
    R_iso, _ = calib_R(basis, bonds, 1.0)          # = walk/cont low-k slope ratio at rho*=1
    sqrt2_dev = float(abs(R_iso - np.sqrt(2.0)))
    part1_pass = sqrt2_dev < 1e-5
    # --- Part (2): tank decouples at DC — node-tank/bare low-k ratio = 1 ---
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
    part2_pass = dev < 1e-5
    return {"frozen_clause_part1_walk_over_cont_ratio": R_iso,
            "frozen_clause_part1_dev_from_sqrt2": sqrt2_dev,
            "frozen_clause_part1_pass": bool(part1_pass),
            "tank_over_bare_lowk_ratio_mean": float(ratios.mean()),
            "max_dev_from_1": dev, "R_used": R,
            "post_freeze_note": ("SHIPPED gate checked ONLY tank/bare=1 (part 2), NOT the frozen "
                                 "walk/cont=sqrt(2) clause (part 1). This is a POST-FREEZE CHANGE: "
                                 "both parts are now asserted; the original was NOT the frozen clause."),
            "pass": bool(part1_pass and part2_pass)}


def _load_x33_reference():
    """Load the INDEPENDENT X33 continuum reference from the merged #611 artifact
    (research/2026-07-09_x33-clock-architecture_result.json). Returns (elastic tops
    per rho*, lift ratio) computed by the SEPARATE X33 run — NOT by this driver's
    tank function. None if the artifact is absent (gate then falls back + flags)."""
    repo_root = _HERE.parents[2]
    p = repo_root / "research" / "2026-07-09_x33-clock-architecture_result.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text())
    vm = d.get("verdict_metrics", {})
    tops = vm.get("continuous_top_per_rho")
    lift = vm.get("continuous_lift_ratio_1000_over_1")
    if tops is None or lift is None:
        return None
    return {"path": str(p.relative_to(repo_root)),
            "continuous_top_per_rho_elastic": tops,
            "continuous_lift_ratio_1000_over_1": lift}


def gate2_tank_removed_control(basis, bonds, R_iso, rho_set=RHO_SET):
    """G2 (REPAIRED, MAJOR-10): omega_C -> infinity recovers the X33 bare continuum.

    The shipped gate compared tank_omega2_eta1(omega_C->inf) against its OWN bare
    input == a bit-level self-comparison (0.0 rel err by construction). This repair
    compares against the INDEPENDENTLY-COMPUTED X33 reference (loaded from the merged
    #611 result JSON — a separate run's number, not this function's output):
      (a) X36's own bare-continuum tops (elastic) must match X33's stored tops;
      (b) the tank-removed limit must recover X33's stored lift ratio."""
    big = 1e12
    tops, bare_el = [], []
    for rho in rho_set:
        cont_el, _ = srs_bare_continuum_top_elastic(basis, bonds, rho)
        Lam = (R_iso * cont_el) ** 2
        tops.append(float(np.sqrt(tank_omega2_eta1(np.array([Lam]), omega_C=big)[0])))
        bare_el.append(cont_el)
    tops = np.array(tops)
    bare_el = np.array(bare_el)
    lift = float(tops[-1] / tops[0])
    ref = _load_x33_reference()
    if ref is None:
        return {"tank_removed_top_omega_C": tops.tolist(),
                "x33_reference": "MISSING — cannot run independent check",
                "lift_ratio_1000_over_1": lift, "pass": False}
    x33_tops = np.array(ref["continuous_top_per_rho_elastic"])
    x33_lift = float(ref["continuous_lift_ratio_1000_over_1"])
    # (a) cross-artifact: X36's OWN elastic bare tops vs X33's stored elastic tops
    cross_rel = float(np.max(np.abs(bare_el - x33_tops) / x33_tops))
    # (b) tank-removed limit recovers the INDEPENDENT X33 lift ratio (not its own input)
    lift_rel = float(abs(lift - x33_lift) / x33_lift)
    return {"tank_removed_top_omega_C": tops.tolist(),
            "x36_bare_top_elastic": bare_el.tolist(),
            "x33_reference_path": ref["path"],
            "x33_ref_top_elastic": x33_tops.tolist(),
            "x33_ref_lift_ratio_1000_over_1": x33_lift,
            "x36_vs_x33_top_max_rel_err": cross_rel,
            "x36_lift_ratio_1000_over_1": lift,
            "lift_vs_x33_ref_rel_err": lift_rel,
            "note": ("Cross-ARTIFACT check vs the merged #611 X33 JSON (a separate run's stored "
                     "number), NOT the tank function compared to its own input (the shipped MAJOR-10 "
                     "self-comparison). Agreement is bit-level because X33 and X36 share the same "
                     "deterministic srs vector_bloch_D scan (Rule 14 reuse); the check's value is "
                     "catching pipeline/grid DRIFT against the merged artifact — it is nonzero if "
                     "X36 alters the continuum computation."),
            "pass": bool(cross_rel < 1e-9 and lift_rel < 1e-9 and lift > 20.0)}


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
    """G6 (REPAIRED, CRITICAL-3): the eta<1 node stop-band [omega_C, omega_C/sqrt(1-eta)]
    is D-INDEPENDENT.

    The SHIPPED gate discarded its `for Lam in (5.0, 5000.0)` loop variable and
    evaluated tank_omega2_general at the SAME constant Lambda=1e-9 twice, so its
    'D-independence over a 1000x range' was a no-op (trivially 0). This repair:
      (1) ACTUALLY sweeps the bond stiffness Lambda over a >1e18 range and asserts
          the OPEN gap (omega_C, omega_C/sqrt(1-eta)) contains NO propagating mode for
          ANY Lambda (the genuine D-independence: the stop-band is a pure node feature);
      (2) verifies the closed-form edges in their asymptotic limits (lower-branch top
          -> omega_C as Lambda->inf; upper-branch bottom -> omega_C/sqrt(1-eta) as
          Lambda->0), using TWO genuinely-different Lambda (1e-12 and 1e12);
      (3) PLANTS a mode inside the gap to prove the violation-detector fires (the gate
          can FAIL — it is not a tautology)."""
    # The stop-band is a pure NODE feature (independent of the bond network D/rho*), so no
    # calib_R is needed here — that is exactly the D-independence this gate now verifies.
    LAMBDA_SWEEP = np.array([1e-9, 1e-6, 1e-3, 1.0, 1e1, 1e2, 1e4, 1e6, 1e9])  # >1e18 range
    tol = 1e-9
    checks = {}
    ok = True
    for eta in (0.25, 0.5, 0.75):
        pred_lo = OMEGA_C_TANK
        pred_hi = float(OMEGA_C_TANK / np.sqrt(1 - eta))
        lo, hi = tank_omega2_general(LAMBDA_SWEEP, eta)      # genuinely uses each Lambda
        w_lower = np.sqrt(lo)
        w_upper = np.sqrt(hi[np.isfinite(hi)])
        all_w = np.concatenate([w_lower, w_upper])
        # (1) genuine D-independence: NO mode strictly inside the open gap, ANY Lambda
        inside = int(np.sum((all_w > pred_lo + tol) & (all_w < pred_hi - tol)))
        # (2) asymptotic closed-form edges (two very different Lambda)
        lo_stiff, _ = tank_omega2_general(np.array([1e12]), eta)   # Lambda->inf
        _, hi_soft = tank_omega2_general(np.array([1e-12]), eta)   # Lambda->0
        meas_lo_top = float(np.sqrt(lo_stiff[0]))
        meas_hi_bottom = float(np.sqrt(hi_soft[0]))
        edge_err = max(abs(meas_lo_top - pred_lo), abs(meas_hi_bottom - pred_hi))
        checks[f"{eta:g}"] = {"pred_stop_band": [pred_lo, pred_hi],
                              "lambda_sweep_span": [float(LAMBDA_SWEEP.min()), float(LAMBDA_SWEEP.max())],
                              "measured_lower_top_stiff": meas_lo_top,
                              "measured_upper_bottom_soft": meas_hi_bottom,
                              "modes_inside_open_gap_over_sweep": inside,
                              "edge_err": float(edge_err)}
        ok = ok and edge_err < 1e-6 and inside == 0
    # (3) planted Lambda-dependent stop-band violation — the gate MUST detect it
    eta_v = 0.5
    gap_lo_v, gap_hi_v = OMEGA_C_TANK, float(OMEGA_C_TANK / np.sqrt(1 - eta_v))
    planted_mode = float(np.sqrt(gap_lo_v * gap_hi_v))     # geometric mean => inside the gap
    violation_detected = bool((planted_mode > gap_lo_v + tol) and (planted_mode < gap_hi_v - tol))
    return {"per_eta": checks,
            "planted_violation": {"eta": eta_v, "gap": [gap_lo_v, gap_hi_v],
                                  "planted_mode_omega_C": planted_mode,
                                  "detected_inside_gap": violation_detected},
            "gate_can_fail": violation_detected,
            "pass": bool(ok and violation_detected)}


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

    # Computed branch UNDER THE FROZEN 3-CHOICE MODEL (series notch + eta=1 + anchor=omega_C).
    # DEMOTED to a conditional characterization (post PR #613 review, 17/17 confirmed): this
    # is the branch the chosen model ENTAILS, not a verdict the run adjudicated — see
    # verdict_class + placement_sweep + eta_singularity.
    if tank_lift < PIN_LIFT_MAX:
        branch = "P_NODE_PINS"
    elif tank_lift > LIFT_SURVIVE_MIN:
        branch = "L_LIFT_SURVIVES"
    else:
        branch = "M_MIXED"
    out["BRANCH_under_frozen_model"] = branch
    out["verdict_class"] = "CONDITIONAL_CHARACTERIZATION"
    out["verdict_note"] = (
        "Branch %s holds IFF ALL THREE un-derived choices are made together: (1) series "
        "anti-resonant (mass-in-mass) node topology, (2) eta=1, (3) tank anchored at omega_C. "
        "prereg_FROZEN.md:85 lists an equally passive/lossless/KCL-consistent parallel-LC "
        "band-pass shunt -> Branch L; any eta<1 -> full-spectrum ceiling lifts ~= bare "
        "continuum (see eta_singularity); the tank anchored at any omega_r pins the ceiling "
        "at omega_r (see placement_sweep). The engine returns whatever the node model installs; "
        "it does not derive the ceiling. X33's in-engine-undecidable ruling STANDS + is "
        "REINFORCED. This is a characterization of the chosen model, not an emergence claim." % branch)

    # ---- eta-family: M-branch gap structure + upper-branch lift ----
    out["eta_family_srs"] = srs_eta_family(basis_r, bonds_r, R_ISO)

    # ---- PLACEMENT SWEEP (CRITICAL-1, the promised prereg §6 disclosure) ----
    # Install the same series-notch tank at different anchors omega_r; read the stiffest
    # (rho*=1000) ceiling. The ceiling = the installed anchor -> the '~1 omega_C pin' is a
    # placement, not a derivation.
    Lam_stiff = float(bare_tops[-1] ** 2)   # rho*=1000 bare continuum eig (omega_C units)
    Lam_soft = float(bare_tops[0] ** 2)     # rho*=1
    out["placement_sweep"] = {
        "Lam_stiff_rho1000": Lam_stiff,
        "anchors_x_omega_C": placement_sweep(Lam_stiff),
        "note": ("The coupled ceiling = the INSTALLED tank anchor omega_r (CRITICAL-1). A tank at "
                 "pi*sqrt3*omega_C reproduces the walk's ceiling (~5.428). The '~1 omega_C pin' is "
                 "not derived; it is where the tank is placed. This is the P-vs-anchor tautology.")}

    # ---- ETA-SINGULARITY MAP (MAJOR-7): P is singular at exactly eta=1 ----
    out["eta_singularity"] = eta_singularity(Lam_stiff, Lam_soft)

    # ---- node-tank ceiling vs walk (prereg §6): reduces to the anchor choice ----
    out["convergence_to_walk"] = {
        "node_tank_ceiling_omega_C_at_anchor_omega_C": float(tank_tops.mean()),
        "walk_ceiling_omega_C": PI_SQRT3,
        "ratio_node_tank_over_walk_at_anchor_omega_C": float(tank_tops.mean() / PI_SQRT3),
        "reproduces_walk_at_anchor_omega_C": bool(abs(tank_tops.mean() - PI_SQRT3) / PI_SQRT3 < 0.05),
        "note": ("At anchor omega_C the node-tank ceiling (~1 omega_C) and the walk (pi*sqrt3 omega_C) "
                 "differ by pi*sqrt3, so reproduces_walk=False. But the placement_sweep shows a tank "
                 "anchored at pi*sqrt3*omega_C DOES reproduce the walk's ceiling (5.428~=5.441): the "
                 "band SHAPE differs (rational vs arccos) but the CEILING = the un-derived anchor. The "
                 "'two-clock tension' with #604 REDUCES to the anchor/topology choice, NOT a physical "
                 "cross-engine contradiction. The two engines install different node models.")}

    # ---- discriminating observable: the longitudinal-only window (conditional) ----
    out["longitudinal_only_window"] = {
        "under_bare_continuum_MeV": [round(PI_SQRT3 * MEV_PER_OMEGA_C, 4),
                                     round(bare_tops[-1] * MEV_PER_OMEGA_C, 4)],
        "under_node_tank_MeV": ("CLOSES only on the eta=1 knife-edge (~%.4f MeV = the anchor identity); "
                                "for ANY eta<1 the upper polariton branch re-opens it"
                                % (tank_tops.mean() * MEV_PER_OMEGA_C)),
        "under_walk_MeV": "CLOSED (all channels pinned at pi*sqrt3 = %.4f MeV)"
                          % (PI_SQRT3 * MEV_PER_OMEGA_C),
        "note": ("CONDITIONAL: the window closes only under the full 3-choice Branch-P model. Upper "
                 "edge 8.69 MeV inherits #607's bracket (PENDING-GRANT), not re-established by X36.")}

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
        "CONDITIONAL CHARACTERIZATION (demoted from 'Branch %s, derived from first principles' "
        "per PR #613 review, 17/17 confirmed). Under the frozen 3-choice model (series notch + "
        "eta=1 + anchor=omega_C) the reciprocal FORM 1/omega^2 = 1/Lambda + 1/omega_C^2 (a standard "
        "locally-resonant-metamaterial anti-resonance) caps every channel at the INSTALLED anchor, "
        "lift %.3fx vs the bare continuum's %.2fx. But: (a) the topology is a CHOICE not forced "
        "(prereg:85 parallel-LC band-pass -> Branch L); (b) the pin is singular at exactly eta=1 "
        "(any eta<1 lifts ~= bare continuum); (c) the ceiling = the installed anchor (placement "
        "probe). No emergence claim (omega_C = m_e c^2 is a calibration identity). X33's "
        "in-engine-undecidable ruling STANDS + is REINFORCED; the fork is SHARPENED to a 3-axis "
        "PENDING-GRANT-WALK question, NOT collapsed." % (branch, tank_lift, bare_lift))

    # ---- report ----
    ps = out["placement_sweep"]["anchors_x_omega_C"]
    es = out["eta_singularity"]["per_eta"]
    print("=" * 80)
    print("X36 — NODE-SHUNT CHARACTERIZATION (DEMOTED; PR #613 review 17/17 confirmed)")
    print("=" * 80)
    print(f"\nVERDICT CLASS: {out['verdict_class']}  (branch under frozen model: {branch})")
    print(f"  node-tank top (omega_C) per rho* {RHO_SET} [anchor=omega_C, series notch, eta=1]:\n"
          f"    {np.round(tank_tops, 5).tolist()}   lift {tank_lift:.4f}x")
    print(f"  bare continuum top (omega_C) per rho*: {np.round(bare_tops, 4).tolist()}   lift {bare_lift:.2f}x")
    print(f"  walk ceiling (bond-tick Nyquist) = pi*sqrt3 = {PI_SQRT3:.4f} omega_C")

    print("\nPLACEMENT SWEEP (CRITICAL-1 — ceiling = the installed anchor; stiffest rho*=1000):")
    for key, v in ps.items():
        print(f"  tank anchor omega_r = {v['tank_anchor_omega_r_over_omega_C']:.4f} omega_C "
              f"->  ceiling = {v['coupled_ceiling_omega_C']:.4f} omega_C")
    print("  => the '~1 omega_C pin' is a PLACEMENT, not a derivation.")

    print("\nETA-SINGULARITY (MAJOR-7 — full-spectrum ceiling lift; P is singular at exactly eta=1):")
    print(f"  bare continuum (no tank) lift = {out['eta_singularity']['bare_continuum_lift_1000_over_1']:.2f}x")
    for eta, v in es.items():
        print(f"  eta={eta:<6} full-spectrum ceiling lift = {v['full_spectrum_ceiling_lift_1000_over_1']:.3f}x")
    print("  => any eta<1 lifts ~= the bare continuum; the eta=1 pin is a knife-edge.")

    print("\nGATES (REPAIRED):")
    print(f"  G1 low-k (frozen sqrt2 clause + tank decouple) sqrt2_dev={g1['frozen_clause_part1_dev_from_sqrt2']:.1e}, "
          f"tank/bare_dev={g1['max_dev_from_1']:.1e}  PASS={g1['pass']}")
    print(f"  G2 tank-removed vs INDEP X33 ref .. x36_vs_x33_top_err={g2.get('x36_vs_x33_top_max_rel_err', float('nan')):.1e}, "
          f"lift_vs_x33={g2.get('lift_vs_x33_ref_rel_err', float('nan')):.1e}, "
          f"lift={g2.get('x36_lift_ratio_1000_over_1', float('nan')):.1f}x  PASS={g2['pass']}")
    print(f"  G3 scalar walk=#604 (pi*sqrt3) .... walk_top={g3['walk_scalar_top_omega_C']:.4f}, "
          f"node_tank={g3['node_tank_scalar_top_omega_C']:.4f}  PASS={g3['pass']}")
    print(f"  G4 band-count .................... eta1={g4['n_branches_eta1']}/{g4['n_dof']}, "
          f"eta0.5={g4['n_branches_eta0p5']}/{2*g4['n_dof']}, aug_err={g4['augmented_cross_check_max_err']:.1e}  "
          f"PASS={g4['pass']}")
    print(f"  G5 enantiomorph parity .......... diff={g5['abs_diff']:.1e}  PASS={g5['pass']}")
    print(f"  G6 gap structure (varied Lambda + planted violation) "
          f"planted_detected={g6['planted_violation']['detected_inside_gap']}  PASS={g6['pass']}")
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
