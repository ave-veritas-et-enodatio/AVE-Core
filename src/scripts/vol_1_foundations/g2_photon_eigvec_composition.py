#!/usr/bin/env python3
"""
STEP-1 VERIFICATION RIDER for the G2 photon-family relabel (Grant-adjudicated
2026-07-03, "a it is!"): the eigenvector-COMPOSITION check.

WHY (fork-to-computable, cheap). The G2 ruling relabels the photon as the two
massless transverse-TRANSLATIONAL branches (u-family) and reassigns the node
micro-rotation ω to the GAPPED mechanical Cosserat sector. Before ANY doc gets
relabeled, this rider READS the actual DOF composition of the massless branches
off the genuine two-sublattice band structure and checks it against the ruling.
Grant's ruling was made on an evidence stack; a contradicting eigenvector read
is NEW evidence he must see — so if the massless branches come back ω-dominated,
this driver HALTs and does NOT authorize the relabel.

WHAT IT MEASURES (substrate-native, no new physics). It imports the EXISTING
genuine 12×12 A→B bond operator dynamical_matrix_two_sublattice from
cosserat_band_structure_two_sublattice.py (the driver behind
research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md,
validate-on-known PASS: V1 c_EM=1, V2 c_R=√2, V3 gap m²=4 bit-exact, V4 6 gapless,
V5 parity). For each of the 12 eigenvectors v at k→0 it reads the Cosserat DOF
partition already used inside omega2_branches_by_character:
    u-fraction = (|v[0:3]|² + |v[6:9]|²) / |v|²      (translational, both sublattices)
    ω-fraction = (|v[3:6]|² + |v[9:12]|²) / |v|²      (micro-rotational, both sublattices)
No transverse/longitudinal Helmholtz split is imposed — this is the discrete
substrate DOF amplitude read directly off the eigenvector, the native micropolar
partition. Real-space / spatial-Brillouin (A46-matched; the ruling is a real-space
DOF-composition claim, not a phase-space φ² claim).

SUBSTRATE-FIRST SECTOR HEADER.
  SECTOR : full K4 two-sublattice, 6 DOF/node (3 translational u + 3 micro-
           rotational ω) × 2 sublattices → 12×12 D(k). The A↔B coupling is the
           real tetrahedral diamond bond operator (engine-native), imported
           verbatim — NOT re-derived, NOT a Cartesian stencil.
  REGIME : cold linear (small-signal). Saturation OFF. The node-ω GAPPED sector
           (the ruling's home of the static winding, Yukawa-screened) is the COLD
           mass gap m²=4G_c/I_ω probed here; the transverse-translational photon
           pair is the massless acoustic-shear family.
  op14   : OFF. This is a cold-band eigenvector read; no local-clock modulation.

FROZEN PREREG-EXPECTATION (the ruling as prereg, both results recorded):
  E1 the 2 massless TRANSVERSE branches are u-DOMINATED: ω-fraction → 0 as k→0.
  E2 the 6 GAPPED (ω_m=2) branches are ω-DOMINATED: ω-fraction → 1 as k→0.
  E3 (structure) the massless family splits 2 transverse-u (the photon pair) + 1
     longitudinal-u P-wave per sublattice-phase — all u-dominated.
CONTRADICTION HANDLING: if the massless branches come back ω-dominated,
ALL_CONFIRM=False, ruling_confirmed=False → HALT, surface to Grant, do NOT relabel.

Run:  PYTHONPATH=src python3 src/scripts/vol_1_foundations/g2_photon_eigvec_composition.py
"""

import json
from pathlib import Path

import numpy as np

# Import the GENUINE two-sublattice bond operator + the character machinery
# VERBATIM from the validated driver — do not re-derive the operator here.
from cosserat_band_structure_two_sublattice import (  # noqa: E402
    dynamical_matrix_two_sublattice,
)

# Index map of the 12-amplitude eigenvector x = (u^A, ω^A, u^B, ω^B):
#   0:3 = u^A (translational A) · 3:6 = ω^A (micro-rotational A)
#   6:9 = u^B (translational B) · 9:12 = ω^B (micro-rotational B)
U_IDX = np.r_[0:3, 6:9]
W_IDX = np.r_[3:6, 9:12]


def dof_composition(kvec, **kw):
    """Return, for each of the 12 branches at k=kvec, a dict with ω², the
    u-fraction and ω-fraction of the eigenvector (Cosserat DOF partition).

    u_frac = (|v_uA|²+|v_uB|²)/|v|², w_frac = (|v_wA|²+|v_wB|²)/|v|². Each
    eigenvector is unit-norm from eigh, so the two fractions sum to 1.
    """
    D = dynamical_matrix_two_sublattice(np.asarray(kvec, float), **kw)
    w2, V = np.linalg.eigh(D)
    w2 = np.clip(w2, 0.0, None)
    rows = []
    for i in range(12):
        v = V[:, i]
        nrm = float(np.sum(np.abs(v) ** 2))
        u_frac = float(np.sum(np.abs(v[U_IDX]) ** 2) / nrm)
        w_frac = float(np.sum(np.abs(v[W_IDX]) ** 2) / nrm)
        rows.append({"omega2": float(w2[i]), "u_fraction": u_frac, "w_fraction": w_frac})
    return rows


def main():
    out = {}
    # Small-but-finite k (k→0 limit; a hair off Γ so the massless-branch
    # eigenvectors are the genuine long-wavelength shear/compression modes, not a
    # degenerate-at-exactly-Γ arbitrary rotation of the null space). Average the
    # composition over several directions to avoid a direction-specific accident.
    DIRS = {
        "[100]": [1, 0, 0],
        "[110]": [1, 1, 0],
        "[111]": [1, 1, 1],
        "[210]": [2, 1, 0],
    }
    kl = 1e-3
    GAP_TARGET = 4.0  # m² = 4 G_c/I_ω (V3, bit-exact on this operator)
    moduli = dict(G=1.0, G_c=1.0, gamma=1.0, rho=1.0, I_omega=1.0)

    print("=" * 78)
    print("STEP-1 RIDER — G2 photon-family eigenvector-composition check")
    print("Reads u-fraction vs ω-fraction of the 12 branches at k→0 on the GENUINE")
    print("two-sublattice A→B bond operator (imported from the validated driver).")
    print("=" * 78)

    # ---- gather per-direction composition, then classify massless vs gapped ----
    per_dir = {}
    massless_w_fracs = []   # ω-fraction of the massless (photon-family) branches
    massless_u_fracs = []
    gapped_w_fracs = []     # ω-fraction of the gapped (mechanical Cosserat) branches
    gapped_u_fracs = []
    n_massless_seen = []
    n_gapped_seen = []
    for name, d in DIRS.items():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        rows = dof_composition(qhat * kl, **moduli)
        rows_sorted = sorted(rows, key=lambda r: r["omega2"])
        # massless = ω² well below the gap; gapped = ω² near/above the gap.
        # midpoint of [0, m²] as the classifier threshold (gap floor is m²=4 → 2).
        thr = 0.5 * GAP_TARGET
        massless = [r for r in rows_sorted if r["omega2"] < thr]
        gapped = [r for r in rows_sorted if r["omega2"] >= thr]
        per_dir[name] = {
            "n_massless": len(massless),
            "n_gapped": len(gapped),
            "massless_branches": massless,
            "gapped_branches": gapped,
        }
        n_massless_seen.append(len(massless))
        n_gapped_seen.append(len(gapped))
        massless_w_fracs += [r["w_fraction"] for r in massless]
        massless_u_fracs += [r["u_fraction"] for r in massless]
        gapped_w_fracs += [r["w_fraction"] for r in gapped]
        gapped_u_fracs += [r["u_fraction"] for r in gapped]

    massless_w = np.array(massless_w_fracs)
    massless_u = np.array(massless_u_fracs)
    gapped_w = np.array(gapped_w_fracs)
    gapped_u = np.array(gapped_u_fracs)

    # ---- the two TRANSVERSE massless branches per direction (the photon pair) ----
    # The massless family is 6 branches (2 transverse-u photon + 1 longitudinal-u
    # P-wave, per sublattice phase). The photon pair = the 2 LOWEST-ω massless
    # branches per direction (transverse shear, c=1) — isolate them and report
    # their ω-fraction, the decisive number for the ruling (E1).
    photon_pair_w = []
    photon_pair_u = []
    for name, d in DIRS.items():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        rows = sorted(dof_composition(qhat * kl, **moduli), key=lambda r: r["omega2"])
        # the 2 lowest-ω branches with translational character = transverse photons
        trans = [r for r in rows if r["u_fraction"] >= r["w_fraction"]]
        trans_sorted = sorted(trans, key=lambda r: r["omega2"])[:2]
        photon_pair_w += [r["w_fraction"] for r in trans_sorted]
        photon_pair_u += [r["u_fraction"] for r in trans_sorted]
    photon_pair_w = np.array(photon_pair_w)
    photon_pair_u = np.array(photon_pair_u)

    # ---- verdicts ----
    # E1: massless / photon-pair branches u-DOMINATED (ω-fraction → 0).
    e1_photon_pair_max_wfrac = float(np.max(photon_pair_w))
    e1_photon_pair_mean_ufrac = float(np.mean(photon_pair_u))
    E1 = bool(e1_photon_pair_max_wfrac < 1e-2)  # ω-fraction of the photon pair ≪ 1
    # E2: gapped branches ω-DOMINATED (ω-fraction → 1).
    e2_gapped_min_wfrac = float(np.min(gapped_w)) if gapped_w.size else float("nan")
    e2_gapped_mean_wfrac = float(np.mean(gapped_w)) if gapped_w.size else float("nan")
    E2 = bool(gapped_w.size and np.min(gapped_w) > 0.99)
    # E3: structure — 6 massless + 6 gapped per direction (the two-sublattice fold).
    E3 = bool(all(n == 6 for n in n_massless_seen) and all(n == 6 for n in n_gapped_seen))

    ruling_confirmed = bool(E1 and E2 and E3)

    out["step1_eigvec_composition"] = {
        "k_lattice": kl,
        "gap_target_m2": GAP_TARGET,
        "moduli": moduli,
        "per_direction": per_dir,
        "E1_photon_pair_u_dominated": {
            "photon_pair_max_w_fraction": e1_photon_pair_max_wfrac,
            "photon_pair_mean_u_fraction": e1_photon_pair_mean_ufrac,
            "massless_family_max_w_fraction": float(np.max(massless_w)),
            "massless_family_mean_u_fraction": float(np.mean(massless_u)),
            "tolerance_w_frac": 1e-2,
            "PASS": E1,
            "note": "The 2 transverse-translational photon-family branches carry "
            "essentially ALL their amplitude in u (translational); ω-fraction → 0 at "
            "k→0. This is the DECISIVE number for the G2 ruling: the photon lives in "
            "the translational-u sector, NOT the node micro-rotation ω sector.",
        },
        "E2_gapped_w_dominated": {
            "gapped_min_w_fraction": e2_gapped_min_wfrac,
            "gapped_mean_w_fraction": e2_gapped_mean_wfrac,
            "tolerance_w_frac_floor": 0.99,
            "PASS": E2,
            "note": "The 6 gapped branches (ω_m=2) carry essentially ALL their amplitude "
            "in ω (micro-rotational); ω-fraction → 1. This is the GAPPED mechanical "
            "Cosserat sector — the home of the static winding topology (Yukawa-screened, "
            "short-range, clm-wcoul2), NOT the photon.",
        },
        "E3_two_sublattice_fold_structure": {
            "n_massless_per_dir": n_massless_seen,
            "n_gapped_per_dir": n_gapped_seen,
            "expected_each": 6,
            "PASS": E3,
        },
        "RULING_CONFIRMED": ruling_confirmed,
        "ruling_verbatim": "the photon = the two massless transverse-TRANSLATIONAL "
        "branches (u-family); its magnetic content = the EM-inductive circulation of "
        "the u-wave (bond-level curl), NOT the node micro-rotation; the node ω = the "
        "GAPPED mechanical Cosserat sector (home of the static winding topology, "
        "Yukawa-screened, short-range). Grant 2026-07-03.",
    }

    # ---- print ----
    print("\n(read at k = %.0e, averaged over %d directions)\n" % (kl, len(DIRS)))
    print("  E1 PHOTON PAIR (2 transverse-translational, the photon):")
    print(f"     ω-fraction  max = {e1_photon_pair_max_wfrac:.3e}   (target ≪ 1 → u-dominated)")
    print(f"     u-fraction mean = {e1_photon_pair_mean_ufrac:.6f}   (target → 1)")
    print(f"     → {'PASS (u-dominated, photon = translational-u family)' if E1 else 'FAIL (NOT u-dominated!)'}")
    print("  E2 GAPPED branches (mechanical Cosserat ω, the mass gap):")
    print(f"     ω-fraction  min = {e2_gapped_min_wfrac:.6f}   mean = {e2_gapped_mean_wfrac:.6f}   (target → 1 → ω-dominated)")
    print(f"     → {'PASS (ω-dominated, node ω = gapped mechanical sector)' if E2 else 'FAIL (NOT ω-dominated!)'}")
    print("  E3 two-sublattice fold: 6 massless + 6 gapped per direction")
    print(f"     n_massless = {n_massless_seen}   n_gapped = {n_gapped_seen}")
    print(f"     → {'PASS' if E3 else 'FAIL'}")
    print()
    if ruling_confirmed:
        print("  RULING CONFIRMED: massless transverse branches are u-DOMINATED, gapped")
        print("  branches are ω-DOMINATED. The G2 relabel is AUTHORIZED — proceed to Step 2.")
    else:
        print("  RULING NOT CONFIRMED by the eigenvector read. HALT — do NOT relabel.")
        print("  Surface to Grant: the composition CONTRADICTS the ruling (new evidence).")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "g2_photon_eigvec_composition.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nResults written: {out_path}")
    return out, ruling_confirmed


if __name__ == "__main__":
    main()
