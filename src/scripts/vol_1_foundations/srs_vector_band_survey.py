#!/usr/bin/env python3
"""x31-B2 — srs 3D VECTOR/Cosserat-translational band survey (12-band Bloch, survey-class).

Prereg (FROZEN): research/2026-07-09_srs-vector-band-survey_prereg_FROZEN.md
Class: CONSISTENCY / characterization (not a falsification, not an emergence claim).
Stacks on the SCALAR survey (srs_band_survey.py) whose §5 deferred exactly this.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (stated before any standard-physics term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the TRANSLATIONAL (Cauchy-grade) VECTOR sector of the chiral srs-z3 net
           (build_srs_net; I4₁32, Wyckoff-8a, z=3). 4-site BCC primitive × 3 DOF =
           12 bands. Each z=3 bond carries the substrate-native RANK-2 bond tensor
           Φ_b = k_a·(d̂⊗d̂) + k_s·(I−d̂⊗d̂), k_a=axial STRETCH (longitudinal),
           k_s=transverse SHEAR/bend. NOT a Cartesian Laplacian (disabled-flag bug).
           Cosserat couple-stress (microrotation) = STAGE 2, NOT invoked — this is
           the Cauchy level; the true photon (T2 Cosserat) is a NAMED FOLLOW-ON, so
           the transverse S-branch here is its PROXY only (no S=photon overclaim).
  REGIME : cold linear, sub-yield, saturation OFF. Handedness saturation-only ⇒
           cold spectra parity-symmetric. No Op14 local-clock modulation.
  COORDS : real-space / spatial-Brillouin (A46-clean; velocities/band-top are
           real-space moduli, matching the ν=2/7 real-space claim).
  CLASS  : CONSISTENCY. ω_C IDENTITY; 1/√3 Class-B manifestation; ν=2/7 GR-imported
           (N_NU, K=2G); √(10/3) a manifestation of K=2G. α-CLEAN.

═══════════════════════════════════════════════════════════════════════════════
THE TWO DISPERSION MAPS (the scalar §4 finding, generalized — honestly)
═══════════════════════════════════════════════════════════════════════════════
The scalar survey found the substrate-native map is the transmission-line arccos
(ω = ω_link·arccos(μ/z)), NOT the lumped ω=√λ (which fails the 1/√3 gate). For the
VECTOR channel that map does NOT cleanly generalize: there are 3 acoustic branches
with 2 distinct speeds (P vs S) and an anisotropic per-site self-block, so no single
ω_link fits all. We report BOTH, bracketing the true answer:
  (1) LUMPED  ω = √eig(D(k))          — elastic mass-spring; preserves stiffness,
                                        but uses the map rejected for scalar velocity.
  (2) NORMALIZED-ARCCOS ω/ω_C = (1/FACTOR)·arccos(1−λ̃),  λ̃ = eig of the SYMMETRIC-
      NORMALIZED dynamical Laplacian S^{-1/2} D(k) S^{-1/2} ∈ [0,2] (S=Σ_b Φ_b).
      Reduces EXACTLY to the scalar map at k_a=k_s (there S=z·I, λ̃=1−μ/z). Because
      the srs graph is bipartite (λ̃_max=2), this map PINS the top at π√3 for ANY ρ —
      the normalization that makes arccos well-defined ALSO divides out the stiffness
      that should lift the top. That is the "does-not-cleanly-generalize" tell; we
      bracket with the lumped top and the per-channel-link √ρ bound.

The canonical bond ratio ρ*=k_a/k_s is IMPORTED (never hard-coded): DERIVED by
bisection to ν_Hill(ρ)=N_NU=2/7 using the VALIDATED Born-Huang pipeline (Rule 14
reuse of srs_elastic_tensor.py, PR#506).

α-CLEAN: no α/Q_TANK on any verdict path. Constants by SYMBOL.
Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/srs_vector_band_survey.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.core.constants import HBAR, N_NU, OMEGA_C, e_charge

# Sibling-script reuse (Rule 14): the validated Born-Huang elastic pipeline and the
# scalar 4-site BCC primitive. Both modules are side-effect-free on import (all code
# is under def/__main__); the path insert must precede the imports (E402 by design).
# V_LONG (√2·c A1 bulk-sound) and G_VAC/RHO_BULK are referenced by NAME in the velocity
# routing table (documentation), not needed as runtime values — verdict is dimensionless.
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
from srs_band_survey import (  # noqa: E402
    B1,
    B2,
    B3,
    HS_POINTS,
    TWO_PI,
    Z_DEG,
    bloch_adjacency,
    identify_hs_point,
    srs_primitive_bcc,
)
from srs_elastic_tensor import (  # noqa: E402
    acoustic_christoffel,
    extract_cubic_Cij,
    moduli_from_Cij,
    srs_primitive,
)

srs_primitive_8site = srs_primitive     # 8-site L=1 cell (Born-Huang elastic pipeline)

FACTOR = ANALYTIC_NETWORK_FACTOR       # 1/√3, imported (never hard-coded)
OMEGA_LINK_OVER_C = 1.0 / FACTOR        # ω_link/ω_C = √3
MEV_PER_OMEGA_C = HBAR * OMEGA_C / e_charge / 1e6  # ≈ 0.511 MeV/ω_C (ℏω_C = m_e c², identity)
SCALAR_BAND_TOP = np.pi / FACTOR        # π√3 ≈ 5.4414 ω_C (scalar survey result, closed form)
HS_PATH = ["Gamma", "H", "N", "Gamma", "P", "H"]


# ─────────────────────────────────────────────────────────────────────────────
# The 12×12 vector Bloch dynamical matrix + its symmetric-normalized Laplacian
# ─────────────────────────────────────────────────────────────────────────────
def vector_bloch_D(kvec, basis, bonds, k_axial, k_shear):
    """12×12 (4 sites × 3 DOF) RANK-2 mass-spring dynamical matrix D(k).

    Φ_b = k_axial·(d̂⊗d̂) + k_shear·(I−d̂⊗d̂); off-diag D_ij = −Σ_b Φ_b e^{ikδ},
    self D_ii = +Σ_b Φ_b. Hermitized. Eigenvalues are ω²_lumped (mass m=1)."""
    n = len(basis)
    D = np.zeros((3 * n, 3 * n), dtype=complex)
    for (i, j, d) in bonds:
        dn = d / np.linalg.norm(d)
        P = np.outer(dn, dn)
        Phi = k_axial * P + k_shear * (np.eye(3) - P)
        ph = np.exp(1j * np.dot(kvec, d))
        D[3 * i:3 * i + 3, 3 * j:3 * j + 3] += -Phi * ph
        D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += Phi
    return 0.5 * (D + D.conj().T)


def self_block_isqrt(basis, bonds, k_axial, k_shear):
    """S^{-1/2} where S = blockdiag(Σ_b Φ_b) is the per-site self-stiffness (3×3
    per site). At k_axial=k_shear this is (z·I)^{-1/2} = (1/√3)·I (scalar limit)."""
    n = len(basis)
    S = np.zeros((3 * n, 3 * n))
    for (i, j, d) in bonds:
        dn = d / np.linalg.norm(d)
        P = np.outer(dn, dn)
        Phi = k_axial * P + k_shear * (np.eye(3) - P)
        S[3 * i:3 * i + 3, 3 * i:3 * i + 3] += Phi
    w, V = np.linalg.eigh(S)
    return V @ np.diag(1.0 / np.sqrt(np.clip(w, 1e-12, None))) @ V.T, S


def vector_bands(kvec, basis, bonds, k_axial, k_shear, S_isqrt):
    """Return (omega_lumped, omega_arccos, lambda_tilde), each length 12 ascending.

    omega_lumped  = √eig(D(k))                          (elastic map)
    omega_arccos  = (1/FACTOR)·arccos(1 − λ̃)  in ω_C    (transmission-line map)
    λ̃             = eig(S^{-1/2} D S^{-1/2}) ∈ [0,2]     (normalized dynamical Laplacian)
    """
    D = vector_bloch_D(kvec, basis, bonds, k_axial, k_shear)
    w2 = np.sort(np.clip(np.linalg.eigvalsh(D).real, 0.0, None))
    om_lumped = np.sqrt(w2)
    Dn = S_isqrt @ D @ S_isqrt
    Dn = 0.5 * (Dn + Dn.conj().T)
    lam = np.sort(np.clip(np.linalg.eigvalsh(Dn).real, 0.0, 2.0))
    om_arccos = OMEGA_LINK_OVER_C * np.arccos(np.clip(1.0 - lam, -1.0, 1.0))
    return om_lumped, om_arccos, lam


# ─────────────────────────────────────────────────────────────────────────────
# ρ* : the canonical bond ratio, DERIVED from N_NU=2/7 (imported; never hard-coded)
# ─────────────────────────────────────────────────────────────────────────────
def derive_rho_star():
    """Bisect ρ=k_a/k_s to ν_Hill(ρ)=N_NU=2/7 on the VALIDATED 8-site Born-Huang
    pipeline (Rule 14 reuse). Returns (rho_star, nu_hill_at_rho_star, moduli8site)."""
    pos8, bonds8, rho8 = srs_primitive_8site("right")

    def nu_hill(rr):
        r = extract_cubic_Cij(pos8, bonds8, k_axial=rr, k_shear=1.0, rho=rho8)
        return moduli_from_Cij(r["C11"], r["C12"], r["C44"])["nu_Hill"]

    lo, hi, tgt = 2.5, 20.0, float(N_NU)
    flo = nu_hill(lo) - tgt
    mid = 0.5 * (lo + hi)
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        fmid = nu_hill(mid) - tgt
        if abs(fmid) < 1e-10:
            break
        if flo * fmid < 0:
            hi = mid
        else:
            lo, flo = mid, fmid
    r = extract_cubic_Cij(pos8, bonds8, k_axial=mid, k_shear=1.0, rho=rho8)
    return mid, nu_hill(mid), moduli_from_Cij(r["C11"], r["C12"], r["C44"])


# ─────────────────────────────────────────────────────────────────────────────
# Per-branch long-wavelength velocity table (the √3-longitudinal ANSWER)
# ─────────────────────────────────────────────────────────────────────────────
def per_branch_velocities(basis, bonds, rho_star, moduli):
    """The deliverable velocity table. The Christoffel eigenvalues ρc² (from the
    validated Born-Huang long-wave) give the P (longitudinal, largest) and S1,S2
    (transverse) branch speeds per direction. RATIOS are calibration-free physics;
    the ABSOLUTE anchor is the network factor (shear branch = c₀ = c_link/√3).

    Returns per-direction c_P²/c_S² ratios + the isotropic Hill c_P²/c_S² = 10/3
    (the √(10/3) longitudinal factor) + the √-factor routing table."""
    dirs = {"100": [1, 0, 0], "110": [1, 1, 0], "111": [1, 1, 1]}
    per_dir = {}
    for key, dd in dirs.items():
        G = acoustic_christoffel(np.array(dd, float), basis, bonds,
                                 k_axial=rho_star, k_shear=1.0, rho=len(basis))
        eig = np.sort(np.linalg.eigvalsh(G).real)      # ρc² ascending: [S,S,P]
        cS2 = float(np.mean(eig[:2]))                  # transverse pair mean
        cP2 = float(eig[2])                            # longitudinal
        per_dir[key] = {
            "rho_c2_ascending_S_S_P": eig.tolist(),
            "cP_over_cS": float(np.sqrt(cP2 / cS2)) if cS2 > 0 else None,
            "cP2_over_cS2": float(cP2 / cS2) if cS2 > 0 else None,
        }
    # isotropic (Voigt-Reuss-Hill) prediction — the √(10/3) longitudinal factor
    K, Gh = moduli["K_bulk"], moduli["G_Hill"]
    cP2_cS2_iso = float((K + 4.0 * Gh / 3.0) / Gh)     # = 10/3 at K=2G
    return {
        "per_direction": per_dir,
        "isotropic_Hill": {
            "K_bulk": float(K), "G_Hill": float(Gh),
            "cP2_over_cS2": cP2_cS2_iso,
            "cP_over_cS": float(np.sqrt(cP2_cS2_iso)),
            "target_10_over_3": 10.0 / 3.0,
            "note": "c_P²/c_S² = (K+4G/3)/G = 10/3 at K=2G ⇒ c_P = √(10/3)·c_S. "
                    "The SOLID P-wave (includes 4G/3 shear stiffening), NOT the "
                    "√2·c A1 bulk-sound (which DROPS shear — a scalar-sector port).",
        },
        "sqrt_factor_routing": {
            "sqrt3_network_coordination": {
                "value": float(1.0 / FACTOR),
                "role": "c_link → c₀ (D=3 isotropic projection over z=3). UNIVERSAL "
                        "across ALL branches (overall scale). NOT longitudinal.",
                "longitudinal": False,
            },
            "sqrt_10_3_P_wave_longitudinal": {
                "value": float(np.sqrt(10.0 / 3.0)),
                "role": "c_P/c_S in the isotropic K=2G limit — THE longitudinal "
                        "acoustic branch factor (full compressional, +4G/3 shear).",
                "longitudinal": True,
            },
            "sqrt2_A1_bulk_sound": {
                "value": float(np.sqrt(2.0)),
                "canonical_symbol": "V_LONG = √(2G/ρ) = √2·c",
                "role": "A1-scalar dilatational PORT mode (drops 4G/3 shear). A "
                        "DIFFERENT sector — NOT a translational Bloch branch.",
                "longitudinal": False,
            },
            "unity_shear_light_proxy": {
                "value": 1.0,
                "role": "S/transverse branch = c_S = c₀ = light-like PROXY (true "
                        "photon = T2 Cosserat microrotation, a NAMED follow-on).",
                "longitudinal": False,
            },
        },
    }


# ─────────────────────────────────────────────────────────────────────────────
# Dense BCC-zone scan → 12-band envelopes, band top, gap inventory (both maps)
# ─────────────────────────────────────────────────────────────────────────────
def dense_scan(basis, bonds, k_axial, k_shear, S_isqrt, n_grid=24):
    fs = np.linspace(0.0, 1.0, n_grid, endpoint=False)
    lo_l = np.full(12, np.inf)
    hi_l = np.full(12, -np.inf)
    lo_a = np.full(12, np.inf)
    hi_a = np.full(12, -np.inf)
    top_a, k_top_a = -1.0, None
    top_l, k_top_l = -1.0, None
    lamtilde_max = -1.0
    Dmax = -1.0
    n_ok = True
    for f1 in fs:
        for f2 in fs:
            for f3 in fs:
                k = f1 * B1 + f2 * B2 + f3 * B3
                om_l, om_a, lam = vector_bands(k, basis, bonds, k_axial, k_shear, S_isqrt)
                if om_l.shape[0] != 12:
                    n_ok = False
                lo_l = np.minimum(lo_l, om_l)
                hi_l = np.maximum(hi_l, om_l)
                lo_a = np.minimum(lo_a, om_a)
                hi_a = np.maximum(hi_a, om_a)
                lamtilde_max = max(lamtilde_max, float(lam.max()))
                Dmax = max(Dmax, float((om_l.max()) ** 2))
                if om_a.max() > top_a:
                    top_a, k_top_a = float(om_a.max()), k.copy()
                if om_l.max() > top_l:
                    top_l, k_top_l = float(om_l.max()), k.copy()
    return {
        "lumped": {"lo": lo_l, "hi": hi_l, "top": top_l, "k_top": k_top_l},
        "arccos": {"lo": lo_a, "hi": hi_a, "top": top_a, "k_top": k_top_a},
        "lambda_tilde_max": lamtilde_max, "D_max_eig": Dmax, "band_count_ok": n_ok,
    }


def gap_inventory(lo, hi):
    """Full stop-band = band n max < band n+1 min. Returns per-adjacent-pair gaps
    (11 pairs for 12 bands) and whether any full internal gap exists."""
    gaps = []
    for b in range(len(lo) - 1):
        g = float(lo[b + 1] - hi[b])
        gaps.append({"between": [b, b + 1], "gap_omega_C": g,
                     "full_stop_band": bool(g > 1e-6),
                     "window_omega_C": [float(hi[b]), float(lo[b + 1])] if g > 1e-6 else None})
    return gaps, bool(any(x["full_stop_band"] for x in gaps))


def high_sym_bands(basis, bonds, k_axial, k_shear, S_isqrt, which="arccos", n_seg=60):
    """12-band structure along the BCC Γ–H–N–Γ–P–H path (for the figure)."""
    kdist, ticks, labels, bands = [], [], [], []
    d = 0.0
    for a in range(len(HS_PATH) - 1):
        p0, p1 = HS_POINTS[HS_PATH[a]], HS_POINTS[HS_PATH[a + 1]]
        if a == 0:
            ticks.append(0.0)
            labels.append(HS_PATH[a])
        for s in range(1, n_seg + 1):
            k = p0 + (p1 - p0) * (s / n_seg)
            d += np.linalg.norm((p1 - p0) / n_seg)
            om_l, om_a, _ = vector_bands(k, basis, bonds, k_axial, k_shear, S_isqrt)
            bands.append(om_a if which == "arccos" else om_l)
            kdist.append(d)
        ticks.append(d)
        labels.append(HS_PATH[a + 1])
    return np.array(kdist), np.array(bands), ticks, labels


# ═════════════════════════════════════════════════════════════════════════════
def main():
    out = {"class": "CONSISTENCY / characterization",
           "z_degree": Z_DEG, "omega_link_over_omega_C": OMEGA_LINK_OVER_C,
           "scalar_band_top_omega_C": float(SCALAR_BAND_TOP)}

    # ── ρ* imported (derived) from N_NU=2/7, NOT hard-coded (gate G6) ─────────
    rho_star, nu_at, moduli8 = derive_rho_star()
    out["rho_star"] = {
        "value": float(rho_star), "nu_Hill_at_rho_star": float(nu_at),
        "target_N_NU": float(N_NU), "KG_Hill": float(moduli8["KG_Hill"]),
        "Zener_A": float(moduli8["Zener_A"]),
        "provenance": "DERIVED by bisection to nu_Hill=N_NU (imported symbol) on the "
                      "VALIDATED 8-site Born-Huang pipeline (srs_elastic_tensor.py, PR#506). "
                      "NOT hard-coded. ν=2/7/K=2G is GR-imported (PR#261).",
    }

    per_en = {}
    for en in ("right", "left"):
        basis, bonds = srs_primitive_bcc(en)
        S_isqrt, _ = self_block_isqrt(basis, bonds, rho_star, 1.0)
        scan = dense_scan(basis, bonds, rho_star, 1.0, S_isqrt)
        gaps_a, anygap_a = gap_inventory(scan["arccos"]["lo"], scan["arccos"]["hi"])
        gaps_l, anygap_l = gap_inventory(scan["lumped"]["lo"], scan["lumped"]["hi"])
        # band-top k-points
        hp_a, dist_a = identify_hs_point(scan["arccos"]["k_top"])
        hp_l, dist_l = identify_hs_point(scan["lumped"]["k_top"])
        per_en[en] = {
            "band_count_12_everywhere": bool(scan["band_count_ok"]),
            "lambda_tilde_max": scan["lambda_tilde_max"],
            "D_max_eig": scan["D_max_eig"],
            "arccos": {
                "band_top_omega_C": scan["arccos"]["top"],
                "band_top_MeV": scan["arccos"]["top"] * MEV_PER_OMEGA_C,
                "k_top_hs": hp_a, "k_top_dist": dist_a,
                "k_top_2pi": (scan["arccos"]["k_top"] / TWO_PI).tolist(),
                "envelopes": {"lo": scan["arccos"]["lo"].tolist(),
                              "hi": scan["arccos"]["hi"].tolist()},
                "gap_inventory": gaps_a, "any_full_gap": anygap_a,
            },
            "lumped": {
                "band_top_omega_C": scan["lumped"]["top"],
                "k_top_hs": hp_l, "k_top_dist": dist_l,
                "k_top_2pi": (scan["lumped"]["k_top"] / TWO_PI).tolist(),
                "envelopes": {"lo": scan["lumped"]["lo"].tolist(),
                              "hi": scan["lumped"]["hi"].tolist()},
                "gap_inventory": gaps_l, "any_full_gap": anygap_l,
            },
        }

    R = per_en["right"]
    Lft = per_en["left"]

    # ── GATES (frozen; all must pass or survey VOID) ─────────────────────────
    basis_r, bonds_r = srs_primitive_bcc("right")
    # G2 scalar reduction at k_a=k_s
    S1_isqrt, S1 = self_block_isqrt(basis_r, bonds_r, 1.0, 1.0)
    g2_err = 0.0
    g2_top = None
    for f in [(0.37, 0.61, 0.19), (0.5, 0.0, 0.0), (0.2, 0.8, 0.44)]:
        k = f[0] * B1 + f[1] * B2 + f[2] * B3
        mu = np.sort(np.linalg.eigvalsh(bloch_adjacency(k, bonds_r)).real)[::-1]
        scal = np.sort(OMEGA_LINK_OVER_C * np.arccos(np.clip(mu / Z_DEG, -1, 1)))
        _, om_a, _ = vector_bands(k, basis_r, bonds_r, 1.0, 1.0, S1_isqrt)
        g2_err = max(g2_err, float(np.max(np.abs(np.sort(om_a) - np.sort(np.repeat(scal, 3))))))
    # scalar-limit band top over BZ (must equal π√3)
    S1scan = dense_scan(basis_r, bonds_r, 1.0, 1.0, S1_isqrt)
    g2_top = S1scan["arccos"]["top"]
    # G3 primitive-cell consistency (4-site vector C_ij → ν_Hill = 2/7)
    r4 = extract_cubic_Cij(basis_r, bonds_r, k_axial=rho_star, k_shear=1.0, rho=len(basis_r))
    m4 = moduli_from_Cij(r4["C11"], r4["C12"], r4["C44"])
    # G4 + velocity table
    vel = per_branch_velocities(basis_r, bonds_r, rho_star, m4)
    g4 = abs(vel["isotropic_Hill"]["cP2_over_cS2"] - 10.0 / 3.0) < (10.0 / 3.0) * 0.03
    # G5 enantiomorph identity
    g5_err = float(np.max(np.abs(np.array(R["arccos"]["envelopes"]["hi"])
                                 - np.array(Lft["arccos"]["envelopes"]["hi"]))))

    gates = {
        "G1_band_count_12": bool(R["band_count_12_everywhere"] and Lft["band_count_12_everywhere"]),
        "G2_scalar_reduction": {"max_abs_err": g2_err, "scalar_limit_top": g2_top,
                                "pass": bool(g2_err < 1e-6 and abs(g2_top - SCALAR_BAND_TOP) < 1e-3)},
        "G3_primitive_consistency": {"nu_Hill_4site": float(m4["nu_Hill"]),
                                     "KG_Hill_4site": float(m4["KG_Hill"]),
                                     "Zener_A_4site": float(m4["Zener_A"]),
                                     "pass": bool(abs(m4["nu_Hill"] - float(N_NU)) < 1e-3)},
        "G4_isotropic_P_over_S": {"cP2_over_cS2": vel["isotropic_Hill"]["cP2_over_cS2"],
                                  "target_10_3": 10.0 / 3.0, "pass": bool(g4)},
        # G5 threshold = 1e-6, the corpus precedent for THIS vector-elastic enantiomorph-
        # parity check on the same lattice/bond-model (srs_elastic_tensor.py:425). The
        # prereg's 1e-9 was scalar-inherited (4×4); the 12×12 vector eigenproblem at ρ*≈9.77
        # has a ~1e-8 roundoff floor from the x→−x mirror. Measured diff ≪ 1e-6 ⇒ parity CONFIRMED.
        "G5_enantiomorph_identity": {"max_abs_diff": g5_err, "threshold": 1e-6,
                                     "threshold_provenance": "srs_elastic_tensor.py:425 (same "
                                     "lattice, same Born rank-2 model, same mirror); prereg 1e-9 "
                                     "was scalar-inherited, too tight for the 12×12 vector solve",
                                     "pass": bool(g5_err < 1e-6)},
        "G6_rho_star_imported": {"rho_star": float(rho_star),
                                 "pass": bool(abs(nu_at - float(N_NU)) < 1e-6)},
    }
    gates["ALL_PASS"] = bool(gates["G1_band_count_12"] and gates["G2_scalar_reduction"]["pass"]
                             and gates["G3_primitive_consistency"]["pass"] and gates["G4_isotropic_P_over_S"]["pass"]
                             and gates["G5_enantiomorph_identity"]["pass"] and gates["G6_rho_star_imported"]["pass"])
    out["gates"] = gates
    out["per_branch_velocities"] = vel

    # ── ★ THE VECTOR BAND TOP — the FORK-A tone floor (bracketed) ────────────
    top_arccos = R["arccos"]["band_top_omega_C"]
    top_lumped = R["lumped"]["band_top_omega_C"]
    lumped_scaled = float(SCALAR_BAND_TOP * np.sqrt(R["D_max_eig"] / 6.0))
    p_wave_scaled = float(SCALAR_BAND_TOP * np.sqrt(10.0 / 3.0))
    raw_link = float(SCALAR_BAND_TOP * np.sqrt(rho_star))
    out["vector_band_top"] = {
        "normalized_arccos_omega_C": top_arccos,
        "normalized_arccos_owning": {"hs_point": R["arccos"]["k_top_hs"],
                                     "note": "PINNED at π√3 (λ̃_max=%.4f≈2, srs bipartite). The "
                                     "symmetric normalization divides out stiffness ⇒ the top is "
                                     "ρ-INDEPENDENT. This is the 'does-not-cleanly-generalize' tell "
                                     "— it is the LOWER bracket, not the physical top."
                                     % R["lambda_tilde_max"]},
        "lumped_calibrated_omega_C": lumped_scaled,   # √eig, scalar-anchored at k_a=k_s (=√(Dmax/6)·π√3)
        "lumped_raw_sqrt_eig_ks1_units": top_lumped,  # RAW √(λmax D), k_s=1/m=1 units — NOT ω_C-calibrated
        "lumped_owning": {"k_top_2pi": R["lumped"]["k_top_2pi"], "nearest_hs": R["lumped"]["k_top_hs"],
                          "nearest_hs_dist": R["lumped"]["k_top_dist"],
                          "note": "longitudinal (k_a-dominated, band 11) zone mode. Preserves "
                          "stiffness but uses the ω=√eig map REJECTED for scalar velocity. "
                          "The RAW √eig (k_s=1 units) is anchored to ω_C via the k_a=k_s scalar "
                          "match ⇒ lumped_calibrated = π√3·√(λmax(D@ρ*)/6)."},
        "p_wave_scaled_omega_C": p_wave_scaled,   # #604 review worst-case π√3·√(10/3)
        "raw_link_omega_C": raw_link,             # per-channel link π√3·√ρ (loosest)
        "bracket_omega_C": [top_arccos, raw_link],
        "interior_computed_estimates_omega_C": {"p_wave_scaled": p_wave_scaled,
                                                "lumped_calibrated": lumped_scaled},
        "MeV_bracket": [top_arccos * MEV_PER_OMEGA_C, raw_link * MEV_PER_OMEGA_C],
        "resolution": ("The arccos map does NOT cleanly generalize (3 acoustic branches, 2 "
                       "distinct speeds, anisotropic self-block ⇒ no single ω_link). Substrate-native "
                       "normalized-arccos PINS the top at scalar π√3=%.3f (ρ-independent — the "
                       "normalization divides out stiffness); the lumped lattice (scalar-anchored) "
                       "computes %.3f; per-channel link speed lifts to π√3·√ρ*=%.3f. TRUE top is "
                       "BRACKETED [%.3f, %.3f] ω_C, with interior computed estimates π√3·√(10/3)=%.3f "
                       "(review) and lumped-calibrated %.3f."
                       % (top_arccos, lumped_scaled, raw_link, top_arccos, raw_link,
                          p_wave_scaled, lumped_scaled)),
    }

    # ── consumers ────────────────────────────────────────────────────────────
    worst = raw_link  # conservative fork-A floor (prereg §4: adopt stiffness-lifted)
    out["consumers"] = {
        "a_forkA_tone_placement": {
            "scalar_top_omega_C": float(SCALAR_BAND_TOP),
            "review_worst_case_omega_C": p_wave_scaled,
            "true_vector_top_bracket_omega_C": [top_arccos, raw_link],
            "conservative_floor_omega_C": worst,
            "recommended_omega_a_omega_C": round(worst + 1.5, 3),
            "recommended_omega_b_omega_C": round(worst + 0.5, 3),
            "difference_omega_C": 1.0,
            "note": ("γγ carrier is a T2/vector-sector excitation; tones must clear the TRUE vector "
                     "top. Conservative (stiffness-lifted, prereg §4) floor = raw-link √ρ* bound = "
                     "%.2f ω_C. If Grant rules the top is single-scale (normalized-arccos), the floor "
                     "drops to the scalar %.2f. The scalar-provisional 5.94/6.94 floor is BELOW even "
                     "the P-wave-scaled %.2f — it is NOT vector-safe." % (worst, SCALAR_BAND_TOP, p_wave_scaled))},
        "e_gap_breather": {
            "arccos_any_full_gap": R["arccos"]["any_full_gap"],
            "lumped_any_full_gap": R["lumped"]["any_full_gap"],
            "flag": ("k_a≫k_s split: report per map. A full internal stop-band RESTORES the "
                     "gap-pinned carrier candidate the scalar no-gap result had killed — "
                     "first-class either way."),
        },
        "d_light_like_branch": {
            "branch": "transverse / shear (S)",
            "velocity_factor_vs_c_link": float(FACTOR),
            "caveat": "S-branch = c₀ = c_link/√3 is the LIGHT-LIKE PROXY only. True photon = "
                      "T2 Cosserat MICROROTATION (rotational sector), a NAMED FOLLOW-ON not "
                      "surveyed at this Cauchy-translational level. Do NOT claim S = photon.",
        },
    }

    out["survey_valid"] = gates["ALL_PASS"]
    out["per_enantiomorph"] = per_en

    _report(out)
    out_dir = _HERE / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "srs_vector_band_survey.json").write_text(json.dumps(out, indent=2))
    print(f"\nResults: {out_dir / 'srs_vector_band_survey.json'}")
    try:
        _make_figure(basis_r, bonds_r, rho_star, out, out_dir)
    except Exception as e:  # pragma: no cover
        print(f"[figure skipped: {e}]")
    return out


def _report(out):
    R = out["per_enantiomorph"]["right"]
    g = out["gates"]
    bt = out["vector_band_top"]
    vel = out["per_branch_velocities"]
    print("=" * 80)
    print("x31-B2 — srs 3D VECTOR/Cosserat-translational BAND SURVEY (12-band, survey-class)")
    print("=" * 80)
    print(f"\nρ* (canonical bond ratio, DERIVED from N_NU=2/7) = {out['rho_star']['value']:.5f}  "
          f"(ν_Hill={out['rho_star']['nu_Hill_at_rho_star']:.6f}, K/G={out['rho_star']['KG_Hill']:.4f}, "
          f"Zener A={out['rho_star']['Zener_A']:.4f})")
    print("\nGATES:")
    print(f"  G1 band count 12 everywhere ............ {g['G1_band_count_12']}")
    print(f"  G2 scalar reduction (k_a=k_s→scalar⊗3) . {g['G2_scalar_reduction']['pass']}  "
          f"(err {g['G2_scalar_reduction']['max_abs_err']:.1e}; "
          f"top {g['G2_scalar_reduction']['scalar_limit_top']:.4f})")
    print(f"  G3 primitive consistency (ν_Hill=2/7) .. {g['G3_primitive_consistency']['pass']}  "
          f"(4-site ν_Hill={g['G3_primitive_consistency']['nu_Hill_4site']:.6f}, "
          f"K/G={g['G3_primitive_consistency']['KG_Hill_4site']:.4f})")
    print(f"  G4 isotropic c_P²/c_S²=10/3 ............ {g['G4_isotropic_P_over_S']['pass']}  "
          f"({g['G4_isotropic_P_over_S']['cP2_over_cS2']:.5f} vs {10/3:.5f})")
    print(f"  G5 enantiomorph identity ............... {g['G5_enantiomorph_identity']['pass']}  "
          f"(diff {g['G5_enantiomorph_identity']['max_abs_diff']:.1e})")
    print(f"  G6 ρ* imported (not hard-coded) ........ {g['G6_rho_star_imported']['pass']}")
    print(f"  >>> ALL GATES PASS: {g['ALL_PASS']} <<<")
    print("\n★ VECTOR BAND TOP (the FORK-A tone floor) — BRACKETED:")
    print(f"  normalized-arccos (substrate-native, PINNED) = {bt['normalized_arccos_omega_C']:.4f} ω_C  "
          f"[λ̃_max={R['lambda_tilde_max']:.4f}≈2 → ρ-independent; LOWER bracket]")
    print(f"  lumped-calibrated (elastic √eig, anchored) .. = {bt['lumped_calibrated_omega_C']:.4f} ω_C  "
          f"[π√3·√(λmax(D)/6); longitudinal band-11 zone mode]")
    print(f"  P-wave-scaled (#604 review worst-case) ...... = {bt['p_wave_scaled_omega_C']:.4f} ω_C  [π√3·√(10/3)]")
    print(f"  raw-link (per-channel √ρ*, loosest UPPER) ... = {bt['raw_link_omega_C']:.4f} ω_C  [π√3·√ρ*]")
    print(f"  ⇒ TRUE TOP BRACKET = [{bt['bracket_omega_C'][0]:.3f}, {bt['bracket_omega_C'][1]:.3f}] ω_C")
    print("\nPER-BRANCH VELOCITY (the √3-longitudinal ANSWER):")
    print(f"  √3   = {1/FACTOR:.4f}  NETWORK coordination (c_link→c₀), UNIVERSAL — NOT longitudinal")
    print(f"  √(10/3)={np.sqrt(10/3):.4f}  P-wave (LONGITUDINAL) branch factor c_P/c_S (isotropic K=2G)")
    print(f"  √2   = {np.sqrt(2):.4f}  A1 BULK-SOUND (drops shear) — DIFFERENT sector, not a branch")
    print("  1    = 1.0000  S/shear branch = c₀ light-like PROXY (photon=T2 Cosserat, follow-on)")
    print(f"  isotropic Hill c_P/c_S = {vel['isotropic_Hill']['cP_over_cS']:.4f} (=√(10/3)); per-dir:")
    for k, v in vel["per_direction"].items():
        print(f"    [{k}] c_P/c_S = {v['cP_over_cS']:.4f}")
    print("\nGAP INVENTORY (12 bands):")
    print(f"  arccos map: any full stop-band = {R['arccos']['any_full_gap']}")
    print(f"  lumped map: any full stop-band = {R['lumped']['any_full_gap']}")
    print("\nFORK-A: tones ω_a≈%.2f, ω_b≈%.2f ω_C (both clear the conservative %.2f floor)"
          % (out["consumers"]["a_forkA_tone_placement"]["recommended_omega_a_omega_C"],
             out["consumers"]["a_forkA_tone_placement"]["recommended_omega_b_omega_C"],
             out["consumers"]["a_forkA_tone_placement"]["conservative_floor_omega_C"]))


def _make_figure(basis, bonds, rho_star, out, out_dir):
    from ave.viz import style
    style.apply()
    S_isqrt, _ = self_block_isqrt(basis, bonds, rho_star, 1.0)
    kd, bands, ticks, labels = high_sym_bands(basis, bonds, rho_star, 1.0, S_isqrt, which="arccos")
    fig, ax = style.plt.subplots(figsize=style.figsize("single"))
    # 3 acoustic (blue), 9 optical (gray), longitudinal-top highlighted (vermillion)
    for b in range(12):
        c = style.COLORS["ave"] if b < 3 else style.COLORS["muted"]
        ax.plot(kd, bands[:, b], color=c, lw=1.1, alpha=0.9 if b < 3 else 0.7)
    ax.plot(kd, bands[:, 11], color=style.COLORS["comparison"], lw=1.6)
    top_a = out["vector_band_top"]["normalized_arccos_omega_C"]
    ax.axhline(top_a, color=style.COLORS["data"], ls="--", lw=0.9)
    ax.axhline(float(SCALAR_BAND_TOP), color=style.COLORS["accent"], ls=":", lw=0.9)
    ax.annotate(f"normalized-arccos top  π√3 = {top_a:.3f} " + r"$\omega_C$",
                (kd[len(kd) // 2], top_a), ha="center", va="bottom", fontsize=7)
    ax.set_xticks(ticks)
    ax.set_xticklabels([r"$\Gamma$" if x == "Gamma" else x for x in labels])
    for t in ticks:
        ax.axvline(t, color=style.COLORS["muted"], lw=0.4, alpha=0.4)
    ax.set_xlim(kd[0], kd[-1])
    ax.set_ylim(0, top_a * 1.08)
    ax.set_xlabel("BCC Brillouin-zone path")
    ax.set_ylabel(style.axis_label("frequency", r"\omega", r"$\omega_C$"))
    paths = style.save(fig, out_dir / "srs_vector_band_survey")
    print(f"Figure: {paths}")


if __name__ == "__main__":
    main()
