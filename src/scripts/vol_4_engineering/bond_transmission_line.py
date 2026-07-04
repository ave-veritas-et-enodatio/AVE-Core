#!/usr/bin/env python3
"""GAP-2 — the bond as a TRANSMISSION LINE (ABCD identity + periodically-loaded Bloch).

Branch: analysis/gap2-bond-transmission-line.

═══════════════════════════════════════════════════════════════════════════════
SECTOR HEADER (declare before any substrate statement)
═══════════════════════════════════════════════════════════════════════════════
  * SECTOR    : EM-transverse / translational-CAPACITIVE face (the ε–μ photon
                port). NOT the T2/Cosserat charge sector, NOT the A1 bulk-mass
                store. The bond here carries the transverse light-cone only.
  * REGIME    : COLD lattice, S(A)=1 (A=0). No Op14 saturation load. The
                loaded/biased line is the concurrent SPICE phase-1 arc's domain
                (research/2026-07-04_spice-phase1-ladder_result.md); this driver
                stays cold so the TL-vs-Bloch cross-check is a clean validate-on-
                known.
  * PHASE     : lossless-reactive (Axiom-3; no loss term). At the ρ_bond=1
                photon operating point the medium is K<0 (mechanically unstable,
                per clm-mfb2ax §3) — a lossless-reactive photon point, NOT a
                stable static solid. This driver does not read stability; it
                reads the transverse dispersion only.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS DRIVER DOES (three consistency-class re-expressions + one cross-check)
═══════════════════════════════════════════════════════════════════════════════
(1) THE CORE IDENTITY (ABCD). Each K4/srs bond is a lossless transmission-line
    segment of length ℓ_node with per-length μ₀, ε₀ ⇒ Z_0=√(μ₀/ε₀),
    delay τ=ℓ_node/c₀. Its EXACT ABCD matrix is the lossless-line ABCD. The #519
    lumped node model (L_CELL=μ₀ℓ_node, C_CELL=ε₀ℓ_node) is the LOW-FREQUENCY
    (ωτ≪1) limit — a single L–C section. We form both ABCDs symbolically-then-
    numerically and expand to 2nd order in θ=ωτ to show WHERE they diverge.

(2) THE PERIODICALLY-LOADED LINE (Bloch). The lattice = TL segments periodically
    loaded by node shunt admittances. The standard Bloch condition on the ABCD
    product is cos(qℓ_eff)=trace(ABCD_cell)/2. We derive the loaded-line
    dispersion and CROSS-CHECK it numerically against the existing engine srs
    Bloch eigensolve (srs_bloch_dispersion.acoustic_omega) at (a) small kℓ (the
    photon point) and (b) toward the zone edge.

(3) THE MATCHED-LINE READING (Ax3). At ρ_bond=1 the internal-boundary Γ vanishes
    (clm-mfb2ax): in TL language the line is MATCHED — no internal reflections,
    no mismatch-added dispersion = the Heaviside distortionless face. We report
    the matched-line Γ=0 numerically. This is a CONSISTENCY re-expression of
    clm-mfb2ax, NOT a new claim.

α-CLEAN: no α / Q_TANK on any path. c₀, Z₀, ℓ_node, L_CELL, C_CELL imported by
SYMBOL from ave.core.constants. Everything is CONSISTENCY-class; the only
potentially-adjudicable output is the TL-vs-Bloch zone-edge comparison, reported
verbatim (flag-don't-fix) against the existing weak-C zone-edge flag.

Run: PYTHONPATH=src python3 src/scripts/vol_4_engineering/bond_transmission_line.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.core.constants import C_0, C_CELL, EPSILON_0, L_CELL, L_NODE, MU_0, Z_0
from scripts.vol_4_engineering.srs_bloch_dispersion import (
    acoustic_omega,
    srs_primitive,
)


# ─────────────────────────────────────────────────────────────────────────────
# (1) THE CORE IDENTITY — lossless-line ABCD vs lumped-LC ABCD
# ─────────────────────────────────────────────────────────────────────────────
def abcd_lossless_line(theta: float, z0: float) -> np.ndarray:
    """Exact ABCD of a lossless TL segment of electrical length θ=βℓ=ωτ, Z_0=z0.

        [ cos θ         j Z0 sin θ ]
        [ j sin θ / Z0  cos θ      ]

    This is the DISTRIBUTED bond (Pozar / Collin lossless-line ABCD). Unimodular
    (det=1) and reciprocal (A=D); for a matched line it is the exact phase/delay
    element the Heaviside distortionless line requires."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, 1j * z0 * s], [1j * s / z0, c]], dtype=complex)


def abcd_lumped_lc_section(theta: float, z0: float) -> np.ndarray:
    """ABCD of the LUMPED L–C section that approximates ONE bond at θ=ωτ.

    Series L=L_CELL then shunt C=C_CELL (the #519 node model). With τ=√(LC) and
    Z0=√(L/C): ωL = θ·Z0 and ωC = θ/Z0. The L-section ABCD is the product

        [1  jωL] [ 1     0 ]   [ 1-θ²   jθZ0        ]
        [0   1 ]·[jωC    1 ] = [ jθ/Z0  1           ]

    NOT unimodular in general (det=1 only exactly), NOT symmetric (A≠D): a lumped
    L-section is the low-frequency stand-in for the distributed line and DIVERGES
    from it at O(θ²) (below)."""
    wl = theta * z0   # ωL_CELL
    wc = theta / z0   # ωC_CELL
    series = np.array([[1.0, 1j * wl], [0.0, 1.0]], dtype=complex)
    shunt = np.array([[1.0, 0.0], [1j * wc, 1.0]], dtype=complex)
    return series @ shunt


def core_identity():
    """(1) Identity check + the 2nd-order divergence of lumped-LC from the line."""
    # (a) The #519 lumped constants ARE the TL totals (machine-exact identities).
    id_checks = {
        "L_CELL_eq_mu0_lnode": {
            "L_CELL": float(L_CELL), "mu0_lnode": float(MU_0 * L_NODE),
            "rel_err": abs(L_CELL / (MU_0 * L_NODE) - 1.0),
        },
        "C_CELL_eq_eps0_lnode": {
            "C_CELL": float(C_CELL), "eps0_lnode": float(EPSILON_0 * L_NODE),
            "rel_err": abs(C_CELL / (EPSILON_0 * L_NODE) - 1.0),
        },
        "Z0_from_cell": {
            "sqrt_LC": float(np.sqrt(L_CELL / C_CELL)), "Z_0": float(Z_0),
            "rel_err": abs(np.sqrt(L_CELL / C_CELL) / Z_0 - 1.0),
        },
        "tau_bond_eq_lnode_over_c0": {
            "sqrt_LcCc": float(np.sqrt(L_CELL * C_CELL)),
            "lnode_over_c0": float(L_NODE / C_0),
            "rel_err": abs(np.sqrt(L_CELL * C_CELL) / (L_NODE / C_0) - 1.0),
        },
    }

    # (b) ABCD divergence: exact line vs lumped LC, per matrix element, vs θ.
    #     θ = ωτ = ω·ℓ_node/c₀ is the electrical length of one bond.
    thetas = np.array([1e-3, 1e-2, 3e-2, 0.1, 0.3, 1.0, np.pi / 2])
    div_rows = []
    for th in thetas:
        M_line = abcd_lossless_line(th, Z_0)
        M_lump = abcd_lumped_lc_section(th, Z_0)
        # normalize B by Z0 and C by 1/Z0 so all four entries are O(1) comparable
        dA = abs(M_lump[0, 0] - M_line[0, 0])
        dB = abs(M_lump[0, 1] - M_line[0, 1]) / Z_0
        dC = abs(M_lump[1, 0] - M_line[1, 0]) * Z_0
        dD = abs(M_lump[1, 1] - M_line[1, 1])
        div_rows.append({
            "theta": float(th),
            "dA": float(dA), "dB_over_Z0": float(dB),
            "dC_times_Z0": float(dC), "dD": float(dD),
            "max_abs_dev": float(max(dA, dB, dC, dD)),
        })

    # (c) The analytic 2nd-order divergence. Exact line A=cosθ=1−θ²/2+…, D=cosθ.
    #     Lumped A=1−θ², D=1. So:
    #        (A_lump − A_line) = −θ²/2 + O(θ⁴)   [half the curvature — the tell]
    #        (D_lump − D_line) = +θ²/2 + O(θ⁴)   [line has droop, lumped does not]
    #        B, C agree to O(θ³) (both jθZ0 / jθ/Z0 at leading + first order).
    # Verify the −θ²/2 coefficient numerically by finite difference at small θ.
    th_small = 1e-3
    A_lump = abcd_lumped_lc_section(th_small, Z_0)[0, 0].real
    A_line = abcd_lossless_line(th_small, Z_0)[0, 0].real
    D_lump = abcd_lumped_lc_section(th_small, Z_0)[1, 1].real
    D_line = abcd_lossless_line(th_small, Z_0)[1, 1].real
    coeff_A = (A_lump - A_line) / th_small ** 2   # → −1/2
    coeff_D = (D_lump - D_line) / th_small ** 2   # → +1/2
    second_order = {
        "A_divergence_coeff": float(coeff_A),   # expect −0.5
        "A_divergence_coeff_expected": -0.5,
        "D_divergence_coeff": float(coeff_D),   # expect +0.5
        "D_divergence_coeff_expected": +0.5,
        "note": "lumped-LC section and distributed line agree to O(θ); first "
        "divergence is O(θ²): A_lump−A_line=−θ²/2, D_lump−D_line=+θ²/2. B and C "
        "(the impedance/admittance off-diagonals) agree to O(θ³). The lumped LC "
        "node is the ωτ≪1 (low-frequency) limit of the distributed bond TL.",
    }
    return {
        "lumped_are_TL_totals": id_checks,
        "abcd_divergence_vs_theta": div_rows,
        "second_order_divergence": second_order,
    }


# ─────────────────────────────────────────────────────────────────────────────
# (2) THE PERIODICALLY-LOADED LINE — Bloch condition cos(qℓ)=tr(ABCD)/2
# ─────────────────────────────────────────────────────────────────────────────
def loaded_line_dispersion(kls: np.ndarray) -> dict:
    """The loaded-line Bloch dispersion from the ABCD cell trace.

    A periodic line of unit cells (here one lumped L–C node section per cell, the
    K4/srs bond) obeys the standard Bloch/Floquet condition on the cell ABCD:

        cos(q ℓ_eff) = (A + D) / 2 = tr(ABCD_cell) / 2.

    For the lumped L-section cell (A=1−θ², D=1, θ=ωτ):
        (A+D)/2 = 1 − θ²/2 = cos(qℓ)   ⇒   θ² = 2(1−cos qℓ) = 4 sin²(qℓ/2)
        ⇒  θ = ωτ = 2|sin(qℓ/2)|   ⇒   ω(q) = (2c₀/ℓ_node)|sin(qℓ_node/2)|.

    This RECOVERS the canonical LC-ladder dispersion (graded-network-response.md
    §1 resultbox) from the ABCD trace — the periodically-loaded-line reading of
    the same sine-law. Returns ω(q)/ω_max and the small-kℓ expansion residual."""
    # ω_max = 2c₀/ℓ_node = 2·OMEGA_C for the lumped-node cell.
    w_max = 2.0 * C_0 / L_NODE
    rows = []
    for kl in kls:
        # exact loaded-line band (sine-law) from the ABCD trace inversion
        w_bloch = w_max * abs(np.sin(kl / 2.0))
        # linear-continuum (dispersionless) reference ω=c₀·q ⇒ ω/c₀·ℓ = kl
        w_lin = (C_0 / L_NODE) * kl
        rows.append({
            "kl": float(kl),
            "w_bloch_over_wmax": float(w_bloch / w_max),
            "vphase_over_c0": float(w_bloch / w_lin) if kl > 0 else 1.0,
            "dispersion_deficit": float(1.0 - (w_bloch / w_lin)) if kl > 0 else 0.0,
        })
    return {"w_max_rad_s": float(w_max), "band": rows}


def tl_vs_bloch_crosscheck(kls: np.ndarray) -> dict:
    """CROSS-CHECK: the 1D loaded-line ABCD dispersion vs the genuine 24×24 srs
    Bloch eigensolve, at the ISOTROPIC-bond photon point k_s=k_a.

    COORDINATE MATCH (phase-space-coordinate-check): both are measured in the
    SAME k-space variable kℓ=|k|·ℓ_node (real-space Brillouin phase per bond).
    Coordinate-matched — the srs corpus claim is q-space dispersion, and so is
    the TL. NOT a phase-space-vs-real-space mismatch.

    SUBSTRATE-NATIVE SCOPE (the RANK-2 stencil guard): the 1D TL ABCD carries a
    SCALAR (direction-independent) dispersion by construction. The srs eigensolve
    carries the full RANK-2 Φ_b=k_a d̂⊗d̂+k_s(I−d̂⊗d̂) tensor on the z=3 bonds, so
    it ALSO carries the direction-dependent zone-edge anisotropy. We therefore
    cross-check the 1D TL scalar band against the srs DIRECTIONAL-MEAN acoustic
    speed (spherical average), and separately REPORT the srs directional spread
    (the anisotropy the scalar TL cannot host by construction). We do NOT force
    the scalar 1D TL to reproduce the rank-2 anisotropy — that would be the
    Cartesian-Laplacian disabled-flag error the srs driver warns against."""
    pos, a, bonds = srs_primitive("right")
    bond_len = float(np.linalg.norm(bonds[0][2]))  # NN bond length (ℓ_node units)

    # First-Brillouin-zone edge: the srs cubic primitive cell edge is a=2√2·ℓ_node,
    # so the [100] first-BZ boundary is at |k|=π/a ⇒ kℓ_edge = π·bond_len/a ≈ 1.11
    # (in kℓ=|k|·ℓ_node units). A 1D MONATOMIC chain's zone edge is kℓ=π — a
    # DIFFERENT zone. Comparing the scalar 1D band past kℓ_edge is comparing two
    # different Brillouin zones (the srs folds higher bands in), NOT a physics
    # discrepancy. We MARK the first-BZ boundary and label folded rows.
    kl_bz_edge = float(np.pi * bond_len / a)

    # srs directional set: high-symmetry axes to bound the anisotropy spread.
    dirs = {
        "[100]": [1, 0, 0], "[110]": [1, 1, 0], "[111]": [1, 1, 1],
        "[210]": [2, 1, 0],
    }
    dvecs = [np.array(d, float) / np.linalg.norm(d) for d in dirs.values()]

    # small-k isotropic acoustic speed of the srs net (the photon operating point);
    # this calibrates the srs ω(kℓ) to a c₀-normalized band directly comparable to
    # the TL band (both then run 0→1 in ω/ω_max within their small-k validity).
    kl_ref = 1e-5
    c_srs = float(np.mean([
        acoustic_omega(q, kl_ref, pos, a, bonds, bond_len=bond_len) / (kl_ref / bond_len)
        for q in dvecs
    ]))

    rows = []
    for kl in kls:
        # 1D TL scalar band, normalized so its small-k slope matches c_srs:
        #   ω_TL(kl) = (2 c_srs / bond_len)·|sin(kl/2)|  (uses srs bond_len + c_srs
        #   so the two bands share the SAME small-k slope → the deviation at large
        #   kl is a pure dispersion-shape comparison, not a speed-calibration one).
        w_tl = (2.0 * c_srs / bond_len) * abs(np.sin(kl / 2.0))
        # srs eigensolve band per direction:
        w_srs_dirs = np.array([
            acoustic_omega(q, kl, pos, a, bonds, bond_len=bond_len) for q in dvecs
        ])
        w_srs_mean = float(np.mean(w_srs_dirs))
        w_srs_spread = float((w_srs_dirs.max() - w_srs_dirs.min()) / w_srs_mean)
        rel_dev_mean = abs(w_tl / w_srs_mean - 1.0) if w_srs_mean > 0 else 0.0
        rows.append({
            "kl": float(kl),
            "w_tl": float(w_tl),
            "w_srs_dirmean": w_srs_mean,
            "tl_vs_bloch_rel_dev": float(rel_dev_mean),
            "srs_anisotropy_spread": w_srs_spread,
            "past_first_bz_edge": bool(kl > kl_bz_edge),
        })
    # summary: worst rel-dev WITHIN the first BZ (the honest agreement window)
    in_bz = [r["tl_vs_bloch_rel_dev"] for r in rows if not r["past_first_bz_edge"]]
    return {
        "c_srs_isotropic": c_srs,
        "bond_len_lnode_units": bond_len,
        "kl_first_bz_edge_100": kl_bz_edge,
        "worst_rel_dev_within_first_bz": float(max(in_bz)) if in_bz else None,
        "worst_aniso_within_first_bz": float(max(
            r["srs_anisotropy_spread"] for r in rows if not r["past_first_bz_edge"])),
        "rows": rows,
        "note": "1D TL scalar band vs srs directional-mean, SAME small-k slope. "
        "Within the first BZ (kℓ<%.3f) the sine-law tracks the srs acoustic "
        "branch; the growing srs-anisotropy-spread column is the rank-2 direction-"
        "dependent zone-edge term the scalar 1D TL cannot carry (reported, not "
        "forced). Rows with past_first_bz_edge=true compare DIFFERENT Brillouin "
        "zones (srs folds higher bands in at kℓ_edge; the 1D chain edge is kℓ=π) — "
        "not a physics discrepancy." % kl_bz_edge,
    }


# ─────────────────────────────────────────────────────────────────────────────
# (3) THE MATCHED-LINE READING — Ax3 Γ=0 at ρ_bond=1 (consistency re-expression)
# ─────────────────────────────────────────────────────────────────────────────
def matched_line_reading() -> dict:
    """(3) The TL-native statement of clm-mfb2ax: at ρ_bond=1 the line is MATCHED.

    A cascade of bond TL segments each of impedance Z_0 (the cold vacuum value,
    the same at every node — z0-derivation.md: ℓ_node cancels) presents NO
    impedance step at any internal node boundary, so Γ_internal = (Z−Z)/(Z+Z)=0
    at every bond join. This IS the Heaviside distortionless / matched-line
    condition: a matched line adds NO reflection and NO mismatch-dispersion. This
    is a CONSISTENCY re-expression of clm-mfb2ax (Ax3 forces ρ_bond=1 → Γ=0), NOT
    a new claim. K<0 honest flag carried (clm-mfb2ax §3): ρ_bond=1 is a lossless-
    reactive photon point, not a stable static solid."""
    # Cascade of N identical Z_0 sections: input impedance stays Z_0, Γ=0 exactly.
    N = 20
    z_sections = np.full(N, Z_0)  # every bond at the cold matched value
    # march input impedance from the far termination (matched load = Z_0) back:
    z_load = Z_0
    theta = 0.3  # arbitrary electrical length per section (matched ⇒ θ-independent)
    z_in = z_load
    for z_sec in z_sections[::-1]:
        z_in = z_sec * (z_load + 1j * z_sec * np.tan(theta)) / (
            z_sec + 1j * z_load * np.tan(theta))
        # for a matched section z_sec==z_load, z_in==z_sec identically
    gamma = (z_in - Z_0) / (z_in + Z_0)
    # contrast: a single mismatched bond (ρ_bond≠1 ⇒ Z_bond≠Z_0) DOES reflect.
    z_mismatch = Z_0 * 1.5  # illustrative internal step (NOT the cold value)
    gamma_mismatch = (z_mismatch - Z_0) / (z_mismatch + Z_0)
    return {
        "matched_cascade_N": N,
        "Gamma_internal_matched": float(abs(gamma)),
        "Gamma_matched_is_zero": bool(abs(gamma) < 1e-12),
        "Gamma_internal_mismatch_example": float(abs(gamma_mismatch)),
        "cites": "clm-mfb2ax (Ax3 forces ρ_bond=1 → Γ_internal=0); consistency-"
        "class re-expression, NOT a new claim.",
        "K_lt_0_honest_flag": "ρ_bond=1 is the lossless-reactive PHOTON operating "
        "point (K<0, mechanically unstable per clm-mfb2ax §3), NOT a stable static "
        "solid; the matter locus is a different ρ*≈9.77 (GR-imported).",
    }


def main():
    out = {}
    out["core_identity"] = core_identity()

    # loaded-line band over the full zone, plus the fine small-k / zone-edge grid
    kls_band = np.linspace(0.0, np.pi, 25)
    out["loaded_line_dispersion"] = loaded_line_dispersion(kls_band)

    # cross-check grid: dense small-k (photon point) THROUGH the first-BZ edge
    # (kℓ≈1.11 along [100]) AND past it (folded higher bands — labeled, not agreement)
    kls_cross = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.11,
                          1.5, 2.5, np.pi * 0.95])
    out["tl_vs_bloch_crosscheck"] = tl_vs_bloch_crosscheck(kls_cross)

    out["matched_line_reading"] = matched_line_reading()

    # ── report ────────────────────────────────────────────────────────────────
    ci = out["core_identity"]
    print("=" * 74)
    print("GAP-2 — THE BOND AS A TRANSMISSION LINE (ABCD identity + Bloch cross-check)")
    print("=" * 74)
    print("\n(1) CORE IDENTITY — #519 lumped constants ARE the TL totals:")
    for k, v in ci["lumped_are_TL_totals"].items():
        print(f"    {k:28s} rel-err {v['rel_err']:.2e}")
    so = ci["second_order_divergence"]
    print(f"\n    ABCD 2nd-order divergence (lumped-LC vs distributed line):")
    print(f"      A_lump−A_line coeff = {so['A_divergence_coeff']:+.4f} "
          f"(expect {so['A_divergence_coeff_expected']:+.1f}·θ²)")
    print(f"      D_lump−D_line coeff = {so['D_divergence_coeff']:+.4f} "
          f"(expect {so['D_divergence_coeff_expected']:+.1f}·θ²)")
    print(f"      ⇒ lumped LC node = ωτ≪1 limit of the distributed bond TL; "
          "first divergence at O(θ²).")

    print("\n(2) PERIODICALLY-LOADED LINE — Bloch cos(qℓ)=tr(ABCD)/2:")
    print("    ⇒ ω(q)=(2c₀/ℓ_node)|sin(qℓ_node/2)|  (recovers the canonical sine-law).")
    cc = out["tl_vs_bloch_crosscheck"]
    print(f"\n    TL-vs-srs-Bloch CROSS-CHECK (c_srs={cc['c_srs_isotropic']:.4f}, "
          f"bond_len={cc['bond_len_lnode_units']:.4f}, "
          f"1st-BZ edge kℓ≈{cc['kl_first_bz_edge_100']:.3f}):")
    print(f"    {'kℓ':>7s}  {'ω_TL':>10s}  {'ω_srs(mean)':>12s}  "
          f"{'|TL/Bloch−1|':>12s}  {'srs aniso':>10s}  BZ")
    for r in cc["rows"]:
        flag = "  <folded>" if r["past_first_bz_edge"] else ""
        print(f"    {r['kl']:7.3f}  {r['w_tl']:10.4f}  {r['w_srs_dirmean']:12.4f}  "
              f"{r['tl_vs_bloch_rel_dev']:12.2e}  {r['srs_anisotropy_spread']:10.2e}{flag}")
    print(f"    ⇒ WITHIN 1st BZ: worst |TL/Bloch−1|={cc['worst_rel_dev_within_first_bz']:.2e}, "
          f"worst srs-aniso={cc['worst_aniso_within_first_bz']:.2e}")
    print(f"    ⇒ folded rows (kℓ>{cc['kl_first_bz_edge_100']:.2f}) compare DIFFERENT "
          "Brillouin zones — labeled, not a discrepancy.")

    ml = out["matched_line_reading"]
    print("\n(3) MATCHED-LINE READING (clm-mfb2ax, consistency-class):")
    print(f"    Γ_internal (matched cascade, ρ_bond=1) = {ml['Gamma_internal_matched']:.2e}  "
          f"(=0: {ml['Gamma_matched_is_zero']})")
    print(f"    Γ_internal (mismatched bond example)   = {ml['Gamma_internal_mismatch_example']:.4f}")
    print(f"    K<0 honest flag: {ml['K_lt_0_honest_flag'][:70]}...")

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "bond_transmission_line.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nResults written: {out_path}")
    return out


if __name__ == "__main__":
    main()
