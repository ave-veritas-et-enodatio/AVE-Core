"""GAP-2 tests — the bond as a transmission line (ABCD identity + Bloch cross-check).

Gates the CONSISTENCY-class claims of the bond-TL leaf:
  (1) the #519 lumped constants ARE the TL totals (machine-exact identities);
  (2) lumped-LC and distributed-line ABCD agree to O(θ), diverge at O(θ²) with
      the −1/2, +1/2 curvature coefficients;
  (3) the periodically-loaded-line ABCD trace recovers the canonical sine-law;
  (4) TL-vs-srs-Bloch small-k agreement (positive control) + the first-BZ window;
  (5) the matched-line Γ_internal=0 reading of clm-mfb2ax.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import C_0, C_CELL, EPSILON_0, L_CELL, L_NODE, MU_0, Z_0
from scripts.vol_4_engineering.bond_transmission_line import (
    abcd_lossless_line,
    abcd_lumped_lc_section,
    cascade_gamma,
    core_identity,
    loaded_line_dispersion,
    matched_line_reading,
    tl_vs_bloch_crosscheck,
)


# ── (1) the #519 lumped constants ARE the TL totals ──────────────────────────
def test_lumped_constants_are_tl_totals():
    assert L_CELL == pytest.approx(MU_0 * L_NODE, rel=1e-15)
    assert C_CELL == pytest.approx(EPSILON_0 * L_NODE, rel=1e-15)
    # Z_0 = √(L_CELL/C_CELL) and τ_bond = √(L_CELL·C_CELL) = ℓ_node/c₀
    assert np.sqrt(L_CELL / C_CELL) == pytest.approx(Z_0, rel=1e-14)
    assert np.sqrt(L_CELL * C_CELL) == pytest.approx(L_NODE / C_0, rel=1e-14)


# ── (2) ABCD identity + 2nd-order divergence ─────────────────────────────────
def test_abcd_lossless_line_is_unimodular_and_reciprocal():
    for th in (0.01, 0.3, 1.0):
        M = abcd_lossless_line(th, Z_0)
        assert np.linalg.det(M) == pytest.approx(1.0, abs=1e-12)  # unimodular
        assert M[0, 0] == pytest.approx(M[1, 1])                  # reciprocal A=D


def test_lumped_lc_matches_line_to_first_order():
    # at small θ the lumped L-section and the distributed line agree to O(θ)
    th = 1e-3
    Ml = abcd_lossless_line(th, Z_0)
    Mp = abcd_lumped_lc_section(th, Z_0)
    # off-diagonals (normalized) agree to O(θ³): rel dev ~ θ²
    assert abs(Mp[0, 1] / Ml[0, 1] - 1.0) < 1e-5
    assert abs(Mp[1, 0] / Ml[1, 0] - 1.0) < 1e-5


def test_second_order_divergence_coefficients():
    res = core_identity()["second_order_divergence"]
    # A_lump − A_line = −θ²/2 ; D_lump − D_line = +θ²/2
    assert res["A_divergence_coeff"] == pytest.approx(-0.5, abs=1e-3)
    assert res["D_divergence_coeff"] == pytest.approx(+0.5, abs=1e-3)


# ── (3) periodically-loaded-line Bloch recovers the sine-law ─────────────────
def test_loaded_line_recovers_sine_law():
    # ω_max = 2c₀/ℓ_node ; at kℓ=π the band tops out at ω_max
    band = loaded_line_dispersion(np.array([0.0, np.pi / 2, np.pi]))
    assert band["w_max_rad_s"] == pytest.approx(2.0 * C_0 / L_NODE, rel=1e-14)
    # kℓ=π/2 ⇒ ω/ω_max = sin(π/4) = 1/√2
    mid = [r for r in band["band"] if abs(r["kl"] - np.pi / 2) < 1e-9][0]
    assert mid["w_bloch_over_wmax"] == pytest.approx(1.0 / np.sqrt(2.0), rel=1e-12)
    # kℓ=π ⇒ ω/ω_max = 1
    edge = [r for r in band["band"] if abs(r["kl"] - np.pi) < 1e-9][0]
    assert edge["w_bloch_over_wmax"] == pytest.approx(1.0, rel=1e-12)


# ── (4) TL-vs-Bloch cross-check (positive control) ───────────────────────────
def test_tl_vs_bloch_small_k_agreement():
    # POSITIVE CONTROL: at the photon point (small kℓ) the 1D loaded-line band
    # matches the genuine srs acoustic eigensolve to <1e-4.
    cc = tl_vs_bloch_crosscheck(np.array([0.01, 0.02, 0.05, 0.1]))
    for r in cc["rows"]:
        assert r["tl_vs_bloch_rel_dev"] < 1e-4


def test_tl_vs_bloch_within_first_bz_and_anisotropy_grows():
    # within the first BZ the sine-law tracks the srs branch to <1%; the srs
    # rank-2 anisotropy spread grows toward the zone edge (the existing weak-C
    # zone-edge flag the scalar TL cannot host — reported, not forced).
    cc = tl_vs_bloch_crosscheck(np.array([0.1, 0.4, 0.8, 1.11, 2.5]))
    assert cc["worst_rel_dev_within_first_bz"] < 1e-2
    # anisotropy is monotone-increasing over the first-BZ window
    in_bz = [r for r in cc["rows"] if not r["past_first_bz_edge"]]
    aniso = [r["srs_anisotropy_spread"] for r in in_bz]
    assert all(b >= a for a, b in zip(aniso, aniso[1:]))
    assert aniso[-1] > aniso[0]
    # the kℓ=2.5 row is past the first BZ edge (folded — not an agreement row)
    assert any(r["past_first_bz_edge"] and abs(r["kl"] - 2.5) < 1e-9 for r in cc["rows"])


# ── (5) matched-line Γ=0 reading of clm-mfb2ax ───────────────────────────────
def test_matched_line_gamma_zero():
    ml = matched_line_reading()
    assert ml["Gamma_matched_is_zero"] is True
    assert ml["Gamma_internal_matched"] < 1e-12
    # a mismatched internal bond DOES reflect (the functional genuinely sees it)
    assert ml["Gamma_internal_mismatch_example"] > 0.1
    # the heterogeneous-Z cascade ACCUMULATES reflection (proves the march runs,
    # not the old one-section-×-20 artifact)
    assert ml["heterogeneous_accumulates"] is True
    assert ml["Gamma_internal_heterogeneous_cascade"] > 1e-3


def test_cascade_march_is_genuine():
    """The cascade must MARCH (each section's load = the running Z_in), which the
    old fixed-z_load bug could not do. Two independent witnesses:
      (i)  a uniform-Z_0 line off a MISMATCHED load: |Γ| is length-invariant
           (standard lossless-matched-line result) but the PHASE advances 2θ per
           section — so the march is visible in arg(Γ), N=1 vs N=8 must differ;
      (ii) a HETEROGENEOUS-Z cascade: |Γ| genuinely accumulates with length (the
           old one-section-×-20 artifact gave a length-independent single step)."""
    theta = 0.3
    # N matched sections off a matched load stay Γ=0 for any N
    for N in (1, 50):
        assert abs(cascade_gamma(np.full(N, Z_0), Z_0, theta)) < 1e-12
    # (i) uniform-Z line, mismatched load: |Γ| invariant, phase marches
    g1 = cascade_gamma(np.full(1, Z_0), 2.0 * Z_0, theta)
    g8 = cascade_gamma(np.full(8, Z_0), 2.0 * Z_0, theta)
    assert abs(abs(g1) - abs(g8)) < 1e-9              # |Γ| length-invariant (matched)
    assert abs(np.angle(g1) - np.angle(g8)) > 1e-3    # but the PHASE marches
    assert abs(g1) <= 1.0 + 1e-9 and abs(g8) <= 1.0 + 1e-9
    # (ii) heterogeneous cascade: |Γ| depends on how many interior mismatches — a
    # longer run of the SAME mismatch pattern is not equal to one section
    z5 = np.array([1.5 * Z_0, 0.7 * Z_0, 1.5 * Z_0, 0.7 * Z_0, 1.5 * Z_0])
    z1 = np.array([1.5 * Z_0])
    assert abs(abs(cascade_gamma(z5, Z_0, theta)) - abs(cascade_gamma(z1, Z_0, theta))) > 1e-3
