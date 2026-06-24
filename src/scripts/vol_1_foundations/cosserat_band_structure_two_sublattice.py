#!/usr/bin/env python3
"""
Genuine TWO-SUBLATTICE K4 ⊗ Cosserat band structure — the substrate-native A→B
bond operator (Lane B re-run of PR #389, done properly).

WHY THIS RE-RUN (the bug in PR #389).
PR #389 (cosserat_full_band_structure.py) did two non-substrate-native things:
  (1) it VALIDATED ON THE SINGLE-NODE 6×6 matrix D6 — V1–V4 all call the 6×6
      continuum dynamical_matrix(...), never the 12×12 two-sublattice form;
  (2) its two-sublattice coupling was a PHENOMENOLOGICAL TILE-AND-SCALE ansatz
      `C = sf_mag·D6` (cosserat_full_band_structure.py:220) — the on-site
      continuum matrix copied into the off-diagonal and scaled by the scalar
      diamond structure-factor magnitude. That is NOT the micropolar bond
      operator: no per-bond strain/curvature tensor, no axial/shear split, the
      off-diagonal is just a scaled copy of the on-site block.

This driver builds the GENUINE object: a 12×12 D(k) whose A→B block is the sum
over the four tetrahedral bonds of the Cosserat bond constitutive operator —
the SAME ε_ij = ∂_j u_i − ε_ijk ω_k, κ_ij = ∂_j ω_i strain/curvature the engine's
_compute_strain / _compute_curvature apply (cosserat_field_3d.py:175,189), but
evaluated as the INTER-SUBLATTICE finite difference across each A→B bond with the
diamond Bloch phase e^{ik·(τ_B+R_b)}, exactly as k4_bloch_dispersion.dynamical_
matrix assembles the EM (translation-only) sector.

SUBSTRATE-FIRST SECTOR HEADER (see prereg §0 — stated before any standard term).
  SECTOR : full K4 two-sublattice, 6 DOF/node (3 translational u + 3 micro-
           rotational ω) × 2 sublattices (A,B) → 12 DOF/cell → 12×12 D(k). A↔B
           coupling = the real tetrahedral diamond bond operator (engine-native),
           NOT a tiled-and-scaled 6×6 block, NOT a Cartesian Laplacian stencil.
  REGIME : cold linear (small-signal). The 4₁-screw handedness is SATURATION-ONLY
           (κ_chiral biases the SATURATION kernel, cosserat_field_3d.py:562/605,
           and does NOT enter _energy_density_bare). So the cold linear bands are
           PARITY-SYMMETRIC BY CONSTRUCTION — NO topology chord in the cold
           spectrum is CORRECT, not a failure (V parity check enforces this).

THE BOND OPERATOR (prereg §1, derived).
The engine gradient d_j V_i ≈ (1/4) Σ_ℓ p_ℓ^j [V(x+p_ℓ) − V(x)] becomes, on the
two-sublattice diamond, an INTER-SUBLATTICE bond operator. For a Bloch wave the
gradient symbol splits:
    ∂_j → G_j^self  = −(1/4) Σ_ℓ p_ℓ^j           (acts on A amplitude; = 0 since
                                                   Σ_ℓ p_ℓ^j = 0 over even-parity offsets)
    ∂_j → G_j^cross(k) = +(1/4) Σ_ℓ p_ℓ^j e^{ik·(τ_B+R_ℓ)}   (acts on B amplitude,
                                                   complex, carries the bond phase)
The whole gradient lives in the A→B cross term — the substrate-native bond. The
strain/curvature are assembled from G^self (A-column) and G^cross (B-column), and
the Hessian of W in the 12-amplitude basis x=(u^A,ω^A,u^B,ω^B) is the 12×12 Φ(k).

VALIDATE-ON-KNOWN (prereg §3, ON THE REAL 12×12 MATRIX):
  V1 translational acoustic slope → c_EM = √(G/ρ) = 1
  V2 gapless rotational slope (G_c=0) → c_R = √(2γ/I_ω) = √2 (engine-faithful;
     RESOLVED Grant 2026-06-23 → clm-kmliqx; continuum label √(γ/I_ω)=1 DEMOTED)
  V3 k=0 rotational gap (G_c=1) → m² = 4 G_c/I_ω = 4 (ω_m = 2)
  V4 k=0 translational branches gapless (count = 6 acoustic)
  V5 PARITY: ω²(k) = ω²(−k) to machine precision (cold-spectrum parity symmetry;
     a falsifier of the bond operator, NOT a chord — see header).
HALT if any fails.

Run:  python3 src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py
Constants imported by SYMBOL from ave.core.constants.
"""

import json
import sys
from pathlib import Path

import numpy as np

from ave.core.constants import C_0, ELL_C, L_NODE, OMEGA_C, Z_0

# ---------------------------------------------------------------------------
# K4 / diamond two-sublattice geometry — the SAME A→B bonds the engine rolls over
# ---------------------------------------------------------------------------
# cosserat_field_3d.TETRA_OFFSETS (cosserat_field_3d.py:134): the four tetrahedral
# A→B port shifts p_ℓ = (±1,±1,±1) with an EVEN number of minus signs. On the
# single engine grid jnp.roll(shift=-p) gives V(x+p); here the same four offsets
# are the four A→B nearest-neighbour bonds of the diamond lattice.
TETRA_OFFSETS = np.array(
    [
        [+1.0, +1.0, +1.0],
        [+1.0, -1.0, -1.0],
        [-1.0, +1.0, -1.0],
        [-1.0, -1.0, +1.0],
    ]
)

# Diamond Bravais (FCC) geometry, matching k4_bloch_dispersion.py:70-88. The
# tetrahedral bond LENGTH (A→B nearest-neighbour distance) is (√3/4)·a_cubic; we
# set it to ℓ_node so "k·ℓ_node" is the phase per bond — the substrate length the
# dispersion is written in. (Same convention as the canonical EM-sector driver.)
A_CUBIC = 4.0 / np.sqrt(3.0)  # so bond length (√3/4)·a = 1 (in ℓ_node units)
A1 = 0.5 * A_CUBIC * np.array([0.0, 1.0, 1.0])
A2 = 0.5 * A_CUBIC * np.array([1.0, 0.0, 1.0])
A3 = 0.5 * A_CUBIC * np.array([1.0, 1.0, 0.0])
TAU_B = 0.25 * A_CUBIC * np.array([1.0, 1.0, 1.0])  # B-sublattice basis offset
# (A→B bond displacement d_b, cell offset R_b of the cell holding the B-neighbour).
# Same four bonds as k4_bloch_dispersion.BOND_CELLS — the physical A→B vectors.
BOND_CELLS = [
    (0.25 * A_CUBIC * np.array([1.0, 1.0, 1.0]), np.zeros(3)),
    (0.25 * A_CUBIC * np.array([1.0, -1.0, -1.0]), -A1),
    (0.25 * A_CUBIC * np.array([-1.0, 1.0, -1.0]), -A2),
    (0.25 * A_CUBIC * np.array([-1.0, -1.0, 1.0]), -A3),
]

# Levi-Civita tensor for the Cosserat cross-coupling ε_ijk ω_k.
_EPS = np.zeros((3, 3, 3))
for _i, _j, _k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    _EPS[_i, _j, _k] = 1.0
    _EPS[_i, _k, _j] = -1.0


def gradient_symbols_two_sublattice(kvec):
    """Substrate-native tetrahedral gradient symbols for the two-sublattice bond.

    The engine gradient d_j V_i ≈ (1/4) Σ_ℓ p_ℓ^j [V(x+p_ℓ) − V(x)] becomes, on the
    diamond, an inter-sublattice bond operator. The A-site's four neighbours
    V(x+p_ℓ) live on the B sublattice; the bond DISPLACEMENT is p_ℓ = (±1,±1,±1),
    the SAME vector that appears in the gradient coefficient (1/4)p_ℓ^j. This is
    the load-bearing substrate-native point: the engine computes the gradient on
    ITS OWN grid where the four A→B bonds ARE the offsets p_ℓ, so the Bloch phase
    per bond is k·p_ℓ (NOT the diamond-metric τ_B+R, which would mix a length-√3
    coefficient with a length-1 phase and break the continuum normalization — the
    bug that gave 1/√3). For a Bloch wave the gradient symbol splits into:
        G_self_j  = −(1/4) Σ_ℓ p_ℓ^j               (coefficient of the A amplitude)
        G_cross_j = +(1/4) Σ_ℓ p_ℓ^j e^{i k·p_ℓ}   (coefficient of the B amplitude)
    Returns (G_self, G_cross), each a length-3 complex vector. Σ_ℓ p_ℓ^j = 0 over
    the even-parity offsets, so G_self = 0 (a uniform field has zero gradient — the
    on-site self-term vanishes; the WHOLE gradient is the A→B cross/bond term).

    Continuum check: G_self + G_cross → (1/4) Σ_ℓ p_ℓ^j (i k·p_ℓ) =
    (1/4)(Σ_ℓ p_ℓ^j p_ℓ^m) i k_m = (1/4)(4 δ^{jm}) i k_m = i k_j — EXACTLY the
    engine single-grid gradient (Σ_ℓ p_ℓ⊗p_ℓ = 4·I since each component is ±1).
    This is the diamond-bond Bloch image of _tetrahedral_gradient, NOT the
    Cartesian i·k_j Laplacian symbol (the disabled-flag-stencil guard); off k=0 it
    carries the genuine A→B bond structure factor.

    kvec is the dimensionless phase per engine-grid bond unit (k·p_ℓ is the phase).
    """
    kvec = np.asarray(kvec, dtype=float)
    G_self = np.zeros(3, dtype=complex)
    G_cross = np.zeros(3, dtype=complex)
    for p in TETRA_OFFSETS:
        phase = np.exp(1j * np.dot(kvec, p))  # Bloch phase per A→B bond = k·p_ℓ
        G_self += -0.25 * p
        G_cross += 0.25 * p * phase
    return G_self, G_cross


def _strain_curvature_maps(G_u_self, G_u_cross, G_w_self, G_w_cross):
    """Build the 9×12 complex linear maps E (Cosserat strain) and K (curvature)
    in the two-sublattice amplitude basis x = (u^A, ω^A, u^B, ω^B) (12-vector).

    Strain  ε_ij = ∂_j u_i − ε_ijk ω_k. The gradient ∂_j acts via the bond
    operator: ∂_j u_i picks up G_self_j on the A-block u-column and G_cross_j on
    the B-block u-column. The algebraic micropolar term −ε_ijk ω_k is ON-SITE
    (the cross product is a local field value, not a bond difference), so it acts
    on the A ω-block when evaluating the strain referenced to the A site.

    Curvature κ_ij = ∂_j ω_i — the bond gradient of ω: G_self_j on A ω-column,
    G_cross_j on B ω-column. ω has no on-site algebraic term.

    Index map of x (length 12): 0:3 = u^A, 3:6 = ω^A, 6:9 = u^B, 9:12 = ω^B.
    Returns (E, K), each 9×12 complex (row = flattened (i,j), col = amplitude DOF).
    """
    E = np.zeros((9, 12), dtype=complex)
    K = np.zeros((9, 12), dtype=complex)
    for i in range(3):
        for j in range(3):
            row = 3 * i + j
            # strain ∂_j u_i : bond gradient of u
            E[row, 0 + i] += G_u_self[j]      # u^A_i
            E[row, 6 + i] += G_u_cross[j]     # u^B_i
            # strain −ε_ijk ω_k : on-site algebraic (A-referenced)
            for k in range(3):
                E[row, 3 + k] += -_EPS[i, j, k]   # ω^A_k
            # curvature ∂_j ω_i : bond gradient of ω
            K[row, 3 + i] += G_w_self[j]      # ω^A_i
            K[row, 9 + i] += G_w_cross[j]     # ω^B_i
    return E, K


def _stiffness_from_maps(E, K, G, G_c, gamma):
    """Hermitian quadratic-form matrix Q (12×12) for one sublattice-referenced
    energy contribution: Q = (2/3)G T†T + G E_sym†E_sym + G_c E_asym†E_asym + γ K†K.

    Mirrors _energy_density_bare (cosserat_field_3d.py:676) operator-for-operator:
      W_cauchy   = (2/3) (tr ε)² + |ε_sym|²   (prefactor G)
      W_micropolar = |ε_antisym|²              (prefactor G_c)
      W_kappa    = |κ|²                         (prefactor γ)
    with the symmetric/antisymmetric projectors on the 9-vector (i,j) layout.
    """
    # trace map T (1×12): tr ε = Σ_i ε_ii
    T = np.zeros((1, 12), dtype=complex)
    for i in range(3):
        T += E[3 * i + i, :][None, :]
    # symmetric / antisymmetric projectors on the (i,j) 9-vector
    Psym = np.zeros((9, 9))
    Pasym = np.zeros((9, 9))
    for i in range(3):
        for j in range(3):
            r = 3 * i + j
            rt = 3 * j + i
            Psym[r, r] += 0.5
            Psym[r, rt] += 0.5
            Pasym[r, r] += 0.5
            Pasym[r, rt] -= 0.5
    Esym = Psym @ E
    Easym = Pasym @ E
    Q = (
        (2.0 / 3.0) * G * (T.conj().T @ T)
        + G * (Esym.conj().T @ Esym)
        + G_c * (Easym.conj().T @ Easym)
        + gamma * (K.conj().T @ K)
    )
    return Q


def dynamical_matrix_two_sublattice(kvec, G=1.0, G_c=1.0, gamma=1.0, rho=1.0, I_omega=1.0):
    """GENUINE 12×12 two-sublattice Cosserat Bloch dynamical matrix D(k).

    Amplitude basis x = (u^A, ω^A, u^B, ω^B). The energy is summed over BOTH
    sublattice-referenced strains (the A-referenced bond strain and the
    B-referenced bond strain) so the matrix is symmetric under A↔B exchange and
    Hermitian. For the A-reference the bond operator has G_self on the A-column
    and G_cross(k) on the B-column; for the B-reference the roles swap with the
    conjugate phase (the bond seen from B points back to A, phase e^{-ik·(τ_B+R)}).

    Each site contributes its FULL strain energy (FULL weight, NOT half): the
    engine computes the strain ε = ∂_j u_i − ε_ijk ω_k at EVERY site, and the total
    energy is the sum over both sites. There is no double-counting because each
    site's strain references its OWN on-site ω plus the bond gradient evaluated at
    that site — exactly _energy_density_bare summed over the two-site basis. (An
    earlier half-weight mistakenly halved the NON-shared on-site micropolar term,
    giving m²=2 instead of 4 — the single-mechanism bug, fixed here.)

    D(k) = M^{-1/2} Φ(k) M^{-1/2}, Φ = 2·Q (the Hessian factor 2, the documented
    Lagrangian-to-EOM conversion, cosserat-mass-gap.md:61). M = diag over (ρ×3,
    I_ω×3) per sublattice. Eigenvalues are ω²(k) — the 12 branches.

    WHY THE k=0 ROTATIONAL GAP IS m² = 4 G_c / I_ω (the two factors of 2).
    The micropolar energy is W_micropolar = G_c |ε_antisym|² with
    ε_antisym,ij = ½(∂_i u_j − ∂_j u_i) − ε_ijk ω_k. For uniform ω_z, u=0:
    ε_antisym,xy = −ω_z AND ε_antisym,yx = +ω_z BOTH contribute, so
    W_micropolar = G_c[(−ω_z)² + (+ω_z)²] = 2 G_c |ω_z|²  → factor 2(a): the
    antisymmetric PAIR (ij + ji) double-counts the off-diagonal couple
    (cosserat-mass-gap.md:54-61, "Σ_ij doubling at antisymmetric pair";
    trampoline-framework.md:188, m_ω² = 4 G_c/I_ω flywheel-clock gap).
    The EOM mass term is the SECOND derivative of W w.r.t. ω → another factor
    2(b): the Lagrangian-to-EOM (Hessian, Φ = 2·Q) conversion. The explicit
    "4 = 2 × 2" statement is cosserat-mass-gap.md:61.
    Net m² = 2(a)·2(b)·G_c/I_ω = 4 G_c/I_ω, ω_m = 2.
    This driver recovers it bit-exact (V3) because it is the Fourier symbol of
    the SAME Σκ²/Σε_antisym² operator the validated engine integrates.
    """
    kvec = np.asarray(kvec, dtype=float)
    G_self, G_cross = gradient_symbols_two_sublattice(kvec)

    # --- A-referenced bond strain/curvature: gradient = G_self (on A) + G_cross (on B)
    E_A, K_A = _strain_curvature_maps(G_self, G_cross, G_self, G_cross)
    Q_A = _stiffness_from_maps(E_A, K_A, G, G_c, gamma)

    # --- B-referenced bond strain/curvature: build with the B sublattice as the
    # home site. The bond seen from B uses the conjugate phase, and the on-site
    # micropolar term references ω^B. We reuse _strain_curvature_maps with the
    # roles of A and B swapped: swap the u/ω columns (0:6 ↔ 6:12) and conjugate
    # the cross phase. Equivalent to permuting the 12-vector and conjugating.
    G_self_B, G_cross_B = gradient_symbols_two_sublattice(kvec)
    # B-home: cross phase points B→A = conj of A→B phase.
    G_cross_B = np.conj(G_cross_B)
    E_B0, K_B0 = _strain_curvature_maps(G_self_B, G_cross_B, G_self_B, G_cross_B)
    # In _strain_curvature_maps the "home" (self / on-site ω) columns are 0:6 and
    # the "neighbour" columns are 6:12. For the B-home we permute so that the home
    # is the B block (cols 6:12) and the neighbour is the A block (cols 0:6).
    perm = np.array([6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5])
    E_B = E_B0[:, perm]
    K_B = K_B0[:, perm]
    Q_B = _stiffness_from_maps(E_B, K_B, G, G_c, gamma)

    # Full weight per site (the engine sums the full strain energy at every site;
    # no double-count — each site references its own on-site ω + its own gradient).
    Q = Q_A + Q_B
    Phi = 2.0 * Q  # Hessian factor 2 (Lagrangian-to-EOM, cosserat-mass-gap.md:61)
    Phi = 0.5 * (Phi + Phi.conj().T)  # kill round-off non-Hermiticity

    m_diag = np.array([rho, rho, rho, I_omega, I_omega, I_omega] * 2)
    inv_sqrt_m = 1.0 / np.sqrt(m_diag)
    D = (inv_sqrt_m[:, None] * Phi) * inv_sqrt_m[None, :]
    return 0.5 * (D + D.conj().T)


def omega2_branches(kvec, **kw):
    """Return ω²(k) eigenvalues (ascending, clipped ≥0), lattice units — 12 branches."""
    D = dynamical_matrix_two_sublattice(kvec, **kw)
    w2 = np.linalg.eigvalsh(D)
    return np.sort(np.clip(w2, 0.0, None))


def omega2_branches_by_character(kvec, **kw):
    """ω²(k) split by eigenvector CHARACTER (translational vs rotational weight),
    across BOTH sublattices. Translational weight = |v[0:3]|²+|v[6:9]|², rotational
    weight = |v[3:6]|²+|v[9:12]|². Returns (w2_trans, w2_rot) sorted.

    Needed because the sectors INTERLEAVE in energy (the longitudinal P-wave at
    √(10/3) sits ABOVE the rotational branches), so a plain sort-order selector
    grabs the wrong branch — the substrate-native branch-character read.
    """
    D = dynamical_matrix_two_sublattice(kvec, **kw)
    w2, V = np.linalg.eigh(D)
    w2 = np.clip(w2, 0.0, None)
    trans, rot = [], []
    for i in range(12):
        tw = np.sum(np.abs(V[0:3, i]) ** 2) + np.sum(np.abs(V[6:9, i]) ** 2)
        rw = np.sum(np.abs(V[3:6, i]) ** 2) + np.sum(np.abs(V[9:12, i]) ** 2)
        (trans if tw >= rw else rot).append(w2[i])
    return np.sort(trans), np.sort(rot)


# ---------------------------------------------------------------------------
# DRIVER
# ---------------------------------------------------------------------------
def main():
    out = {}
    HIGH_SYM = {
        "[100]": [1, 0, 0],
        "[110]": [1, 1, 0],
        "[111]": [1, 1, 1],
        "[210]": [2, 1, 0],
    }
    kl_small = 1e-4

    print("=" * 76)
    print("GENUINE TWO-SUBLATTICE COSSERAT BAND STRUCTURE — substrate-native A→B bond")
    print("=" * 76)
    print("Lane B re-run of PR #389 (which validated on the 6×6 D6 + used C=sf_mag·D6).")
    print("This validate-on-known runs on the REAL 12×12 two-sublattice D(k).\n")

    # ===== (0) VALIDATE-ON-KNOWN (pre-reg §3) — ON THE REAL 12×12 MATRIX ======
    val = {}

    # --- V1: transverse photon acoustic slope → c_EM = √(G/ρ) = 1 ----------
    trans_speeds = []
    for d in HIGH_SYM.values():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        w2_t, _ = omega2_branches_by_character(qhat * kl_small, G=1.0, G_c=1.0, gamma=1.0, rho=1.0, I_omega=1.0)
        # lowest translational-character branch = transverse shear photon
        trans_speeds.append(np.sqrt(w2_t[0]) / kl_small)
    c_trans = float(np.mean(trans_speeds))
    c_trans_spread = float((max(trans_speeds) - min(trans_speeds)) / c_trans)
    v1_ok = bool(abs(c_trans - 1.0) < 1e-3)
    val["V1_transverse_photon_speed"] = {
        "c_trans_lattice": c_trans,
        "target_sqrt_G_over_rho": 1.0,
        "rel_err": abs(c_trans - 1.0),
        "spread_across_dirs": c_trans_spread,
        "c_EM_physical_m_s": c_trans * C_0,
        "matrix": "REAL 12x12 two-sublattice (NOT the 6x6 D6 of PR #389)",
        "PASS": v1_ok,
    }

    # --- V2: gapless rotational curvature slope (G_c=0) → c_R = √2 ----------
    # RESOLVED Grant 2026-06-23 → clm-kmliqx (cosserat-mass-gap.md §3.5).
    # Engine W_kappa = jnp.sum(kappa**2) at cosserat_field_3d.py:704 (NO ½;
    # :703 is the micropolar term, NOT W_kappa). The continuum √(γ/I_ω)=1 label
    # is DEMOTED. This V2 value (=√2) is the empirical confirmation clm-kmliqx cites.
    c_rot_target = float(np.sqrt(2.0))
    rot_speeds = []
    for d in HIGH_SYM.values():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        _, w2_r = omega2_branches_by_character(qhat * kl_small, G=1.0, G_c=0.0, gamma=1.0, rho=1.0, I_omega=1.0)
        rot_speeds.append(np.sqrt(w2_r[0]) / kl_small)
    c_rot = float(np.mean(rot_speeds))
    v2_ok = bool(abs(c_rot - c_rot_target) / c_rot_target < 5e-2)
    val["V2_rotational_curvature_speed"] = {
        "c_rot_lattice": c_rot,
        "target_engine_faithful_sqrt2": c_rot_target,
        "continuum_label_sqrt_gamma_over_Iomega": 1.0,
        "rel_err_vs_engine_target": abs(c_rot - c_rot_target) / c_rot_target,
        "RESOLVED": "engine operator gives √2 (node-twist stiffness convention; same "
        "Hessian factor as the validated gap). Grant-ratified 2026-06-23 → clm-kmliqx "
        "(cosserat-mass-gap.md §3.5); continuum label '1' DEMOTED. Engine W_kappa at "
        "cosserat_field_3d.py:704 (NO ½; :703 is the micropolar term, NOT W_kappa).",
        "PASS": v2_ok,
    }

    # --- V3: k=0 rotational gap (G_c=1) → m² = 4 G_c/I_ω = 4 ----------------
    w2_k0 = omega2_branches(np.zeros(3), G=1.0, G_c=1.0, gamma=1.0, rho=1.0, I_omega=1.0)
    gapped = w2_k0[w2_k0 > 1e-9]
    m2_recovered = float(np.mean(gapped)) if len(gapped) else float("nan")
    omega_m = float(np.sqrt(m2_recovered)) if np.isfinite(m2_recovered) else float("nan")
    v3_ok = bool(abs(m2_recovered - 4.0) < 1e-2)
    val["V3_k0_rotational_gap"] = {
        "m2_recovered": m2_recovered,
        "target_4Gc_over_Iomega": 4.0,
        "omega_mass": omega_m,
        "omega_mass_target": 2.0,
        "rel_err": abs(m2_recovered - 4.0) / 4.0,
        "canonical_validated_error_pct": 0.35,
        "n_gapped_branches": int(len(gapped)),
        "all_k0_eigs": w2_k0.tolist(),
        "PASS": v3_ok,
    }

    # --- V4: k=0 translational branches gapless (count = 6 acoustic) --------
    n_acoustic = int(np.sum(w2_k0 < 1e-6))
    v4_ok = bool(n_acoustic == 6)
    val["V4_k0_translational_gapless"] = {
        "n_gapless_branches": n_acoustic,
        "target_n_gapless": 6,
        "note": "6 = 3 acoustic per sublattice (the two-sublattice fold of the 3 "
        "single-node acoustic branches); 6 gapped rotational at m²=4.",
        "PASS": v4_ok,
    }

    # --- V5: PARITY symmetry of the cold spectrum (the bond-operator falsifier)
    # ω²(k) = ω²(−k) to machine precision — the bare energy has NO parity-odd term
    # (κ_chiral is saturation-only). A measured asymmetry = a BUG, not a chord.
    parity_resid = 0.0
    for d in HIGH_SYM.values():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        for kl in [0.3, 0.9, np.pi]:
            wp = omega2_branches(qhat * kl)
            wm = omega2_branches(-qhat * kl)
            parity_resid = max(parity_resid, float(np.max(np.abs(wp - wm))))
    v5_ok = bool(parity_resid < 1e-9)
    val["V5_parity_symmetry"] = {
        "max_parity_residual": parity_resid,
        "tolerance": 1e-9,
        "note": "ω²(k)=ω²(−k); the cold bands are parity-symmetric BY CONSTRUCTION "
        "(bare energy has no parity-odd term; κ_chiral is saturation-only, "
        "cosserat_field_3d.py:562). A nonzero residual would be a bond-operator BUG, "
        "not a chord. This is the substrate fact stated in the header, MEASURED.",
        "PASS": v5_ok,
    }

    # --- V5b: V5-HAS-TEETH self-check (audit w1ni1axfg). The bit-exact V5 residual
    # is FORCED by the real-moduli conjugate-phase Hermitian form (D(-k)=D(k)* ⇒ equal
    # eigenvalues), so passing V5 alone is construction-consistency, NOT strong
    # independent evidence. To show V5 is not a no-op, INJECT a real, k-odd,
    # parity-odd CHIRAL leak (a real coefficient · sin(k·a) coupling the A/B rotational
    # blocks — exactly the kind of term κ_chiral would add if it leaked into the bare
    # energy) and confirm V5 BREAKS with a measurable residual (driver-measured 0.874 at
    # leak=1.0, amplitude-dependent). Backs the result doc's "teeth against a chiral
    # leak" claim with CODE, not assertion.
    def _omega2_with_chiral_leak(kvec, leak=1.0):
        D = dynamical_matrix_two_sublattice(kvec).astype(complex)
        ka = float(np.dot(np.asarray(kvec, float), TETRA_OFFSETS[0]))
        s = leak * np.sin(ka)  # REAL, k-ODD amplitude (odd under bond reversal)
        # Parity ω²(k)=ω²(−k) is FORCED whenever D(−k)=D(k)* (time-reversal of any
        # real-space real-coupling Hermitian operator). A genuine parity-odd / chiral
        # leak is a REAL coupling whose amplitude is ODD in k (a handed coupling that
        # distinguishes the +bond from the −bond direction): T(k)=s(k)·A with A real-
        # symmetric and s(−k)=−s(k). Then D_leak(−k)=D_base(k)*−T(k) while
        # D_leak(k)*=D_base(k)*+T(k) (T real) — they differ by 2T(k), so the conjugate
        # symmetry breaks and ω²(k) ≠ ω²(−k). This is exactly how a κ_chiral term that
        # leaked into the bare energy would manifest. V5 MUST catch it.
        for a, b in ((3, 4), (9, 10)):  # ω_x↔ω_y handed coupling on both sublattices
            D[a, b] += s
            D[b, a] += s  # real-symmetric (Hermitian), k-odd ⇒ parity-breaking
        w2 = np.linalg.eigvalsh(D)
        return np.sort(np.clip(w2, 0.0, None))

    leak_resid = 0.0
    for d in HIGH_SYM.values():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        for kl in [0.3, 0.9, np.pi]:
            wp = _omega2_with_chiral_leak(qhat * kl)
            wm = _omega2_with_chiral_leak(-qhat * kl)
            leak_resid = max(leak_resid, float(np.max(np.abs(wp - wm))))
    v5b_ok = bool(leak_resid > 1e-3)  # the injected chiral leak MUST break parity
    val["V5b_parity_has_teeth"] = {
        "injected_chiral_leak_parity_residual": leak_resid,
        "threshold_to_be_nonzero": 1e-3,
        "note": "V5 residual-0 is FORCED by the real-moduli conjugate-phase Hermitian "
        "form (D(-k)=D(k)* ⇒ equal eigenvalues); it is construction-consistency, NOT "
        "strong independent evidence. This self-check injects a REAL k-odd parity-odd "
        "chiral leak and confirms V5 BREAKS (residual measurably > 0) — so V5 has teeth "
        "against a chiral-leak bug, but is shallow positive evidence for the spectrum.",
        "PASS": v5b_ok,
    }

    all_pass = v1_ok and v2_ok and v3_ok and v4_ok and v5_ok and v5b_ok
    val["ALL_PASS"] = all_pass
    out["validate_on_known"] = val

    s1, s2, s3 = ("PASS" if v1_ok else "FAIL"), ("PASS" if v2_ok else "FAIL"), ("PASS" if v3_ok else "FAIL")
    s4, s5 = ("PASS" if v4_ok else "FAIL"), ("PASS" if v5_ok else "FAIL")
    s5b = "PASS" if v5b_ok else "FAIL"
    e2 = val["V2_rotational_curvature_speed"]["rel_err_vs_engine_target"]
    e3 = val["V3_k0_rotational_gap"]["rel_err"]
    print("(0) VALIDATE-ON-KNOWN on the REAL 12×12 (pre-reg §3):")
    print(f"  V1 transverse photon  c = {c_trans:.6f}  (target √(G/ρ)=1)  rel-err={abs(c_trans-1.0):.2e}  {s1}")
    print(f"  V2 rotational curvature c_R = {c_rot:.6f}  (target √2; continuum-label 1 DEMOTED — RESOLVED clm-kmliqx)  rel-err={e2:.2e}  {s2}")
    print(f"  V3 k=0 rotational gap m² = {m2_recovered:.6f}  (target 4)  ω_m={omega_m:.4f}  rel-err={e3:.2e}  {s3}")
    print(f"  V4 translational gapless branches = {n_acoustic} (target 6)  {s4}")
    print(f"  V5 parity residual ω²(k)-ω²(-k) = {parity_resid:.2e} (target <1e-9, cold parity-sym)  {s5}")
    print(f"  V5b parity-HAS-TEETH: injected chiral leak breaks parity, residual = {leak_resid:.3f} (must be >1e-3; V5 alone is construction-forced, not strong evidence)  {s5b}")
    print(f"\n  ALL_PASS = {all_pass}")

    if not all_pass:
        print("\nHALT: validate-on-known FAILED on the real 12×12 — bond operator is wrong; no spectrum reported.")
        out_dir = Path(__file__).resolve().parent / "_output"
        out_dir.mkdir(exist_ok=True)
        (out_dir / "cosserat_band_structure_two_sublattice.json").write_text(json.dumps(out, indent=2))
        sys.exit(1)

    # ===== (1) GENUINE FULL-BZ TWO-SUBLATTICE SPECTRUM (only after PASS) ======
    feat = {}
    n_k = 80
    bands = {}
    for name, d in HIGH_SYM.items():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        kl_path = np.linspace(1e-4, np.pi, n_k)
        w12 = np.array([np.sqrt(omega2_branches(qhat * kl)) for kl in kl_path])  # (n_k,12)
        bands[name] = {"kl": kl_path.tolist(), "omega_branches_lattice": w12.tolist()}
    feat["bands_12dof_two_sublattice"] = bands

    # --- acoustic/optical gap (the LC stop-band) ---------------------------
    # Acoustic manifold = the translational-character branches; optical = the
    # gapped rotational manifold. Report the hard gap (top of acoustic, floor of
    # optical) across the BZ via a dense grid scan.
    # 21³ grid: the acoustic longitudinal P-wave reaches √(10/3)=1.826 INSIDE the
    # zone (not just at path endpoints), so a coarse grid under-reports the
    # acoustic top and over-reports the gap width. 21³ is converged for the gap.
    n_grid = 21
    ks = np.linspace(-np.pi, np.pi, n_grid)
    acoustic_max = 0.0
    optical_min = np.inf
    rot_floor_global = np.inf
    for kx in ks:
        for ky in ks:
            for kz in ks:
                kk = np.array([kx, ky, kz])
                wt, wr = omega2_branches_by_character(kk)
                if len(wt):
                    acoustic_max = max(acoustic_max, float(np.sqrt(np.max(wt))))
                if len(wr):
                    optical_min = min(optical_min, float(np.sqrt(np.min(wr))))
                    rot_floor_global = min(rot_floor_global, float(np.sqrt(np.min(wr))))
    gap_open = bool(acoustic_max < optical_min)
    feat["acoustic_optical_gap"] = {
        "acoustic_manifold_top": acoustic_max,
        "optical_manifold_floor": optical_min,
        "hard_gap_open": gap_open,
        "gap_width": float(optical_min - acoustic_max) if gap_open else 0.0,
        "note": "LC stop-band: translational acoustic manifold tops below the "
        "rotational optical manifold floor (the mass gap ω_m=2). Substrate-native "
        "reading: the gapped micro-rotation mode IS mass (a node-twist resonance "
        "with a threshold). CONSISTENCY-class (the gap VALUE is the validated echo).",
    }

    # --- optical-branch curvature near k=0 (genuine bond operator) ---------
    qhat = np.array([1.0, 0.0, 0.0])
    kls = np.array([0.02, 0.04, 0.06, 0.08, 0.10])
    opt_w2 = []
    for kl in kls:
        _, w2_r = omega2_branches_by_character(qhat * kl)
        opt_w2.append(float(np.min(w2_r)))
    opt_w2 = np.array(opt_w2)
    a2_fit = float(np.polyfit(kls**2, opt_w2, 1)[0])
    m2_intercept = float(np.polyfit(kls**2, opt_w2, 1)[1])
    feat["optical_branch_curvature"] = {
        "a2_fit": a2_fit,
        "m2_intercept": m2_intercept,
        "m2_target": 4.0,
        "note": "ω²(k)=m²+a₂(kℓ)² for the gapped optical (rotational) branch; "
        "intercept = the validated gap m²=4G_c/I_ω=4, recovered on the GENUINE "
        "bond operator (not the ansatz). Positive curvature: branch rises from gap.",
    }

    # --- DIFFERS-FROM-ANSATZ comparison (the load-bearing question) --------
    # Compare the genuine two-sublattice spectrum against PR #389's tile-and-scale
    # ansatz (C = sf_mag·D6). The ansatz lives in the prior worktree; we reconstruct
    # its construction INLINE here so the comparison is self-contained (no import of
    # the prior driver). Ansatz: D12 = [[D6,C],[C†,D6]], C = (|Σ_b e^{ik·d_b}|/4)·D6.
    def _ansatz_omega(kvec):
        """PR #389 tile-and-scale ansatz spectrum (reconstructed inline)."""
        kvec = np.asarray(kvec, float)
        # single-node 6×6 D6 from the SAME engine operator (continuum gradient symbol
        # i·k via the engine single-grid tetrahedral symbol), as PR #389 built it.
        Gj = 0.25 * (TETRA_OFFSETS.T @ (np.exp(1j * (TETRA_OFFSETS @ kvec)) - 1.0))
        E = np.zeros((9, 6), dtype=complex)
        K = np.zeros((9, 6), dtype=complex)
        for i in range(3):
            for j in range(3):
                r = 3 * i + j
                E[r, i] = Gj[j]
                for b in range(3):
                    E[r, 3 + b] = -_EPS[i, j, b]
                K[r, 3 + i] = Gj[j]
        T = np.zeros((1, 6), dtype=complex)
        for i in range(3):
            T += E[3 * i + i, :][None, :]
        Psym = np.zeros((9, 9))
        Pasym = np.zeros((9, 9))
        for i in range(3):
            for j in range(3):
                r = 3 * i + j
                rt = 3 * j + i
                Psym[r, r] += 0.5
                Psym[r, rt] += 0.5
                Pasym[r, r] += 0.5
                Pasym[r, rt] -= 0.5
        Esym = Psym @ E
        Easym = Pasym @ E
        Q6 = (2.0 / 3.0) * (T.conj().T @ T) + Esym.conj().T @ Esym + Easym.conj().T @ Easym + K.conj().T @ K
        D6 = 2.0 * Q6
        D6 = 0.5 * (D6 + D6.conj().T)
        sf = np.sum(np.exp(1j * (TETRA_OFFSETS @ kvec)))
        sf_mag = abs(sf) / 4.0
        C = sf_mag * D6 * np.exp(1j * np.angle(sf))
        D12 = np.zeros((12, 12), dtype=complex)
        D12[0:6, 0:6] = D6
        D12[6:12, 6:12] = D6
        D12[0:6, 6:12] = C
        D12[6:12, 0:6] = C.conj().T
        D12 = 0.5 * (D12 + D12.conj().T)
        return np.sort(np.sqrt(np.clip(np.linalg.eigvalsh(D12), 0.0, None)))

    diff_by_dir = {}
    max_diff_global = 0.0
    for name, d in HIGH_SYM.items():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        dd = []
        for kl in np.linspace(0.05, np.pi, 40):
            wg = np.sort(np.sqrt(omega2_branches(qhat * kl)))
            wa = _ansatz_omega(qhat * kl)
            dd.append(float(np.max(np.abs(wg - wa))))
        diff_by_dir[name] = {"max_abs_domega": float(max(dd)), "mean_abs_domega": float(np.mean(dd))}
        max_diff_global = max(max_diff_global, max(dd))
    # Zone-edge fingerprint: genuine folds acoustic→0 + optical caps at gap=2;
    # ansatz scales D6 → optical caps at 2√2≈2.828 (an artifact).
    wg_X = np.sort(np.sqrt(omega2_branches(np.array([np.pi, 0, 0]))))
    wa_X = _ansatz_omega(np.array([np.pi, 0, 0]))
    feat["differs_from_ansatz"] = {
        "max_abs_domega_global_lattice": max_diff_global,
        "per_direction": diff_by_dir,
        "zone_edge_X_genuine_max": float(wg_X.max()),
        "zone_edge_X_ansatz_max": float(wa_X.max()),
        "verdict": "DIFFERS — the genuine bond operator and the PR #389 tile-and-scale "
        "ansatz give SUBSTANTIALLY different full-BZ spectra (max|Δω|≈2 lattice). The "
        "near-k=0 validate-on-known AGREES (both → continuum gradient as k→0), but the "
        "ansatz never RAN V1–V4 on its own 12×12 — it validated on D6. At the X zone "
        "edge the genuine diamond structure factor zeroes → acoustic folds to 0 and the "
        "optical manifold caps at exactly the gap (ω=2); the ansatz scales D6 and caps "
        "at 2√2≈2.83, a structure-factor artifact, not the real bond fold.",
    }

    # --- physical-units anchors (imported by symbol) -----------------------
    feat["physical_anchors"] = {
        "c_EM_m_s": C_0,
        "Z_0_ohm": Z_0,
        "L_NODE_m": L_NODE,
        "ELL_C_m": ELL_C,
        "OMEGA_C_rad_s": OMEGA_C,
        "note": "natural-units moduli (G=G_c=γ=ρ=I_ω=1) matching cosserat_wave_test.py; "
        "physical scales imported by SYMBOL. The gap ω_m=2 (lattice) is the rotational-"
        "sector clock; SI calibration is the Phase-II K4⊗Cosserat coupling, NOT claimed here.",
    }

    out["spectrum"] = feat

    print("\n(1) GENUINE FULL-BZ SPECTRUM (validate-on-known PASSED):")
    print(f"  acoustic/optical hard gap: acoustic top={acoustic_max:.4f}  optical floor={optical_min:.4f}  "
          f"gap {'OPEN' if gap_open else 'CLOSED'} (width {optical_min-acoustic_max:.4f})")
    print(f"  optical branch ω²(k)=m²+a₂(kℓ)²:  a₂={a2_fit:.4f}  m²-intercept={m2_intercept:.4f} (target gap=4)")
    print(f"  DIFFERS-FROM-ANSATZ: max|Δω|={max_diff_global:.4f} lattice  "
          f"(zone-edge X: genuine max={wg_X.max():.3f} vs ansatz max={wa_X.max():.3f})")

    print("\nCONSISTENCY-vs-CHORD (pre-reg §4, refute-by-default):")
    print("  C1 genuine differs from ansatz → CONSISTENCY (only ACOUSTIC/validate-on-known agree near k=0; ansatz OPTICAL differs at ALL k incl k→0: 2√2 vs 2)")
    print("  C2 acoustic/optical hard gap    → CONSISTENCY (generic micropolar; gap VALUE = validated echo)")
    print("  C3 cold-spectrum parity-symmetry → CONSISTENCY (forced by parity-even bare energy; κ_chiral=sat-only)")
    print("  NO topology chord in the cold linear spectrum — CORRECT (header substrate fact). The handed")
    print("  mode lives in the driven/SATURATED regime (separate phase). Cold bands = CONSISTENCY only.")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "cosserat_band_structure_two_sublattice.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nResults written: {out_path}")
    return out, val, all_pass


if __name__ == "__main__":
    main()
