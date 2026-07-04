"""Regression gate — LORENTZ-ON-SRS P1 acceptance gate (photon isotropy on srs-z3).

The srs-migration policy's P1 make-or-break: the photon-sector isotropy / emergent-
Lorentz chain must re-clear on the ratified chiral srs-z3 carrier. This test pins the
load-bearing FACTS of the [ISOTROPY-EMERGES] verdict so a future change to the srs
lattice, the micropolar machinery, or the anisotropy reader that would BREAK the P1
gate is caught here, not at post-merge review.

Driver: src/scripts/vol_4_engineering/lorentz_on_srs.py.
Prereg (FROZEN): research/2026-07-04_lorentz-on-srs_prereg_FROZEN.md.

Real-space / spatial-Brillouin coords (A46-clean); cold linear, sat OFF; α-CLEAN;
CONSISTENCY / FORM class. mass=A1 untouched. Carrier: srs-z3 (diamond ref
instrument-scoped).
"""

import sys
from pathlib import Path

import numpy as np
import pytest

# import the driver's library-grade functions (it lives in src/scripts/, not src/ave/)
_DRV = Path(__file__).resolve().parents[1] / "scripts" / "vol_4_engineering"
sys.path.insert(0, str(_DRV))
from lorentz_on_srs import (  # noqa: E402
    acoustic_branches, bond_moment_form, chiral_gyrotropy, chiral_parity_guard,
    diamond_lattice, direction_sphere_not_degenerate, leading_anisotropy,
    planted_order_reference, srs_lattice)


@pytest.fixture(scope="module")
def srs_R():
    pos, a, bonds = srs_lattice("right")
    return pos, bonds, float(np.linalg.norm(bonds[0][2]))


@pytest.fixture(scope="module")
def srs_L():
    pos, a, bonds = srs_lattice("left")
    return pos, bonds, float(np.linalg.norm(bonds[0][2]))


@pytest.fixture(scope="module")
def diamond():
    pos, a, bonds, bl = diamond_lattice()
    return pos, bonds, bl


# ── V0 — validate-on-known: isotropic light-cone ────────────────────────────────
def test_leading_order_c_is_isotropic_srs(srs_R):
    """Leading-order c is direction-INDEPENDENT at k→0 (both transverse branches),
    extrapolated to machine precision — the emergent-Lorentz light-cone on srs."""
    pos, bonds, bl = srs_R
    for br in ("Tmin", "Tmax"):
        r = leading_anisotropy(pos, bonds, bond_len=bl, branch=br)
        assert r["c_isotropy_spread_extrapolated_to_k0"] < 1e-6, (
            f"branch {br} c(k→0) not isotropic: "
            f"{r['c_isotropy_spread_extrapolated_to_k0']:.2e}")


def test_hs_direction_speeds_machine_isotropic(srs_R):
    """[100]/[110]/[111] acoustic speeds agree to machine precision at k→0 (the
    unit-normalized-direction guard: a bare Miller index must not fake a √3 split)."""
    pos, bonds, bl = srs_R
    speeds = [acoustic_branches(np.array(d, float), 1e-4, pos, bonds, bond_len=bl)[0]
              for d in ([1, 0, 0], [1, 1, 0], [1, 1, 1])]
    assert max(speeds) - min(speeds) < 1e-6, f"HS speeds not isotropic: {speeds}"


# ── cold-birefringence: the two transverse branches share c ─────────────────────
def test_no_cold_birefringence_transverse_pair_degenerate(srs_R):
    """The two transverse photon branches are DEGENERATE (share c) — no birefringence
    of the cold lattice. Measured by the absolute ω-splitting at a floor-clear kl."""
    pos, bonds, bl = srs_R
    kl = 0.05
    max_dw = 0.0
    for d in ([1, 0, 0], [1, 1, 0], [1, 1, 1], [2, 1, 0]):
        c = acoustic_branches(np.array(d, float), kl, pos, bonds, bond_len=bl)
        max_dw = max(max_dw, abs(c[0] - c[1]) * (kl / bl))
    assert max_dw < 1e-10, f"transverse pair NOT degenerate (cold birefringence): {max_dw:.2e}"


# ── the (qℓ)⁴ bond-moment FORM re-clears on srs identically to diamond ───────────
def test_bond_moment_quartic_form_reclears_srs(srs_R):
    """srs (432): <(q̂·d̂)²> isotropic (no angular dep), <(q̂·d̂)⁴> = pure cubic harmonic
    ⇒ first anisotropic invariant is QUARTIC — the corpus's (qℓ)⁴ FORM, carrier-native."""
    pos, bonds, bl = srs_R
    f = bond_moment_form(bonds)
    assert f["second_moment_isotropic_spread"] < 1e-10, "2nd bond moment not isotropic"
    assert f["fourth_moment_cubic_harmonic_residual"] < 1e-10, "4th moment not cubic harmonic"
    assert f["first_anisotropic_invariant_is_quartic"]
    assert abs(f["fourth_moment_kappa"] - (-1.0 / 12.0)) < 1e-6, (
        f"srs κ expected −1/12, got {f['fourth_moment_kappa']}")


def test_bond_moment_quartic_form_diamond(diamond):
    """diamond (m3̄m) validate-on-known: reproduces the corpus's OWN (qℓ)⁴ FORM
    (κ=−2/9 per-bond-normalized = the doc's −8/9 over 4 bonds)."""
    pos, bonds, bl = diamond
    f = bond_moment_form(bonds)
    assert f["first_anisotropic_invariant_is_quartic"]
    assert abs(f["fourth_moment_kappa"] - (-2.0 / 9.0)) < 1e-6, (
        f"diamond κ expected −2/9, got {f['fourth_moment_kappa']}")


# ── raw acoustic-branch order n = 2 (the O(k²) zone-edge; same on both carriers) ─
def test_raw_acoustic_branch_order_is_two(srs_R, diamond):
    """The raw lowest-transverse-branch dispersion anisotropy is O(k²) (the zone-edge
    term) on BOTH carriers — matching the merged srs_bloch_dispersion slope 1.9999.
    The (qℓ)⁴ photon-dispersion stays weak-C-conditional; this arc does NOT re-open it."""
    ps, bs, bls = srs_R
    pd, bd, bld = diamond
    ns = leading_anisotropy(ps, bs, bond_len=bls, branch="Tmin")["leading_anisotropic_order_n"]
    nd = leading_anisotropy(pd, bd, bond_len=bld, branch="Tmin")["leading_anisotropic_order_n"]
    assert abs(ns - 2.0) < 0.05, f"srs raw order n={ns} (expected ~2)"
    assert abs(nd - 2.0) < 0.05, f"diamond raw order n={nd} (expected ~2)"


# ── the chiral k-linear gyrotropy: srs-DISTINCT (432 permits, m3̄m forbids) ───────
def test_chiral_gyrotropy_srs_permits_parity_odd(srs_R, srs_L):
    """srs (432) carries a nonzero acoustic-gyrotropy scalar B_signed; it is parity-odd
    (flips sign under enantiomorph swap) — the srs-distinct chiral feature."""
    pr, br, _ = srs_R
    pl, bl_, _ = srs_L
    gR = chiral_gyrotropy(pr, br)["B_signed_gyrotropy"]
    gL = chiral_gyrotropy(pl, bl_)["B_signed_gyrotropy"]
    assert abs(gR) > 1e-6, f"srs gyrotropy vanished: {gR}"
    assert abs(gR + gL) / (abs(gR) + 1e-30) < 1e-4, f"not parity-odd: R={gR} L={gL}"


def test_chiral_gyrotropy_diamond_null(diamond):
    """diamond (m3̄m centrosymmetric) FORBIDS gyrotropy — the symmetry null control."""
    pos, bonds, bl = diamond
    gD = chiral_gyrotropy(pos, bonds)["B_signed_gyrotropy"]
    assert abs(gD) < 1e-8, f"diamond gyrotropy not null (centrosymmetry violated): {gD}"


# ── validation harness guards (V2/V3/V4 + the parity harness) ────────────────────
def test_planted_order_reader_reads_2_and_4():
    """The order-reader recovers a planted n=2 AND n=4 — the fit floor is not
    contaminated (the exact trap the srs_bloch_dispersion §2 caveat names)."""
    assert planted_order_reference(2)["reads_correctly"]
    assert planted_order_reference(4)["reads_correctly"]


def test_direction_sphere_fit_not_degenerate():
    assert direction_sphere_not_degenerate()["not_degenerate"]


def test_chiral_parity_harness_guard(srs_R, srs_L):
    """The detect_symmetry_forced_zero harness confirms B_signed is parity-odd ⇒ the
    diamond null is SYMMETRY-forced, the srs nonzero is a true signal (not hallucination)."""
    pr, br, _ = srs_R
    pl, bl_, _ = srs_L
    gR = chiral_gyrotropy(pr, br)["B_signed_gyrotropy"]
    gL = chiral_gyrotropy(pl, bl_)["B_signed_gyrotropy"]
    assert chiral_parity_guard(gR, gL)["chiral_scalar_is_parity_odd"]


def test_enantiomorph_order_parity_even(srs_R, srs_L):
    """The anisotropy order n is parity-EVEN (identical for right/left) — only the
    chiral k-linear term is parity-odd. A leak of a parity-odd term into n = a bug."""
    pr, br, blr = srs_R
    pl, bl_, bll = srs_L
    nr = leading_anisotropy(pr, br, bond_len=blr, branch="Tmin")["leading_anisotropic_order_n"]
    nl = leading_anisotropy(pl, bl_, bond_len=bll, branch="Tmin")["leading_anisotropic_order_n"]
    assert abs(nr - nl) < 1e-3, f"order not parity-even: R={nr} L={nl}"
