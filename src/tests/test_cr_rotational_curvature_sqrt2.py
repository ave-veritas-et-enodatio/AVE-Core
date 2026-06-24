"""CI gate for clm-kmliqx: the rotational-curvature wave speed c_R = √2.

Locks in the empirical confirmation the canonical claim cites
(`manuscript/ave-kb/vol1/claim-quality.md`, clm-kmliqx; Grant-ratified
2026-06-23). Before this gate existed, the kmliqx claim cited
"Confirmed #392 V2" (c_R = 1.414214, rel-err 2.0e-9) but the genuine
two-sublattice band-structure driver lived on a SEPARATE un-merged branch —
the SHA-pin was dangling. This test makes the V2 measurement a CI-gated
ancestor of the cite.

=== SECTOR HEADER (substrate-native, do-not-fuse the three speeds) ===
The Cosserat micro-rotation (T2) sector carries TWO distinct wave modes:
  - a transverse SHEAR mode  (G-modulus,  speed c   = √(G/ρ) = 1)  — the photon
  - a CURVATURE/wryness mode (γ-modulus, speed √2  = √(2γ/I_ω))   — THIS test
A1/bulk is a THIRD mode (K-modulus, speed √2 = √(K/ρ), K=2G). All three live in
the same 12×12 spectrum; the two √2's (bulk-K and curvature-γ) are numerically
coincident but PHYSICALLY DISTINCT moduli — see the disambiguation table in
cosserat-mass-gap.md §3.5 ("three speeds, do not fuse").

This gate asserts the CURVATURE-γ mode only (G_c = 0, cold-linear). The √2
arises because the engine's curvature energy W_kappa = γ·Σκ² carries NO ½ and
NO symmetrization (`cosserat_field_3d.py:704`, copy `:739`), unlike the
symmetrized Cauchy strain W_cauchy — the SAME no-½ convention that yields the
bit-exact m²=4 mass gap (clm-jz0xaw). ASYMMETRIC convention → {c_R=√2, m²=4};
the SYMMETRIC convention would give {1, m²=2}. Locked together; not separable.

Reference:
  research/2026-06-23_cosserat-band-structure-two-sublattice_prereg-result.md (PR #392)
  src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py (V2 block)
"""

import numpy as np

from scripts.vol_1_foundations.cosserat_band_structure_two_sublattice import (
    omega2_branches_by_character,
)

# High-symmetry directions sampled by the #392 V2 validate-on-known block.
HIGH_SYM = {
    "[100]": [1.0, 0.0, 0.0],
    "[110]": [1.0, 1.0, 0.0],
    "[111]": [1.0, 1.0, 1.0],
    "[210]": [2.0, 1.0, 0.0],
}

# Small-|k| acoustic-slope probe (same kl as the driver's validate-on-known).
KL_SMALL = 1e-4

# Engine-faithful target and the claim's adjudication tolerance.
C_R_TARGET = np.sqrt(2.0)
REL_ERR_TOL = 5e-2  # the §3 V2 PASS tolerance the claim is canonicalized at


def _measure_curvature_speed():
    """Replicate the #392 V2 measurement: G_c=0 gapless rotational slope.

    Returns the lattice rotational-curvature speed averaged over the four
    high-symmetry directions, exactly as `main()` computes c_rot.
    """
    speeds = []
    for d in HIGH_SYM.values():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        # character split: rotational branch w2_r; lowest = the curvature mode.
        _, w2_r = omega2_branches_by_character(
            qhat * KL_SMALL, G=1.0, G_c=0.0, gamma=1.0, rho=1.0, I_omega=1.0
        )
        speeds.append(np.sqrt(w2_r[0]) / KL_SMALL)
    return float(np.mean(speeds))


def test_curvature_speed_is_sqrt2():
    """clm-kmliqx CI gate: the curvature-γ rotational mode propagates at √2.

    The genuine 12×12 two-sublattice bond operator recovers c_R = √2 from the
    no-½ W_kappa Fourier symbol, well within the canonicalized 5e-2 tolerance.
    A measured c_R ≈ 1 here would mean the engine had silently acquired a ½
    elastic prefactor on the curvature term (the demoted continuum label),
    contradicting the source operator and the m²=4 gap it is locked to.
    """
    c_rot = _measure_curvature_speed()
    rel_err = abs(c_rot - C_R_TARGET) / C_R_TARGET
    assert rel_err < REL_ERR_TOL, (
        f"rotational-curvature speed c_R={c_rot:.6f} deviates from √2 by "
        f"rel-err={rel_err:.2e} (tol {REL_ERR_TOL:.0e}); clm-kmliqx canonical "
        f"value is c_R=√2 from the no-½ W_kappa operator."
    )


def test_curvature_speed_is_not_the_continuum_label_one():
    """Guard: c_R is NOT the demoted continuum idealization c_R=√(γ/I_ω)=1.

    Distinguishes the engine-faithful √2 from the prior continuum '1' label so a
    future regression that re-symmetrizes W_kappa (folding the ½ back in) fails
    loudly rather than silently passing a now-wrong claim.
    """
    c_rot = _measure_curvature_speed()
    assert abs(c_rot - 1.0) > 0.3, (
        f"c_R={c_rot:.6f} collapsed toward the DEMOTED continuum label 1 — the "
        f"engine curvature operator may have re-acquired a ½ prefactor; the "
        f"substrate value is √2 (clm-kmliqx)."
    )


def test_curvature_sqrt2_distinct_from_shear_photon_c():
    """Do-not-fuse: the curvature-γ √2 is a DIFFERENT mode than the shear photon c.

    Same T2 micro-rotation sector, two moduli: the transverse SHEAR mode (V1,
    G-modulus) sits at c=1 while the CURVATURE mode (V2, γ-modulus) sits at √2.
    Asserting both in one test pins the speed SPLIT, not just the √2 value, so
    no future reader manufactures a false identity between the two T2 speeds.
    """
    # V1: transverse shear photon (lowest translational-character branch).
    shear_speeds = []
    for d in HIGH_SYM.values():
        qhat = np.asarray(d, float)
        qhat /= np.linalg.norm(qhat)
        w2_t, _ = omega2_branches_by_character(
            qhat * KL_SMALL, G=1.0, G_c=1.0, gamma=1.0, rho=1.0, I_omega=1.0
        )
        shear_speeds.append(np.sqrt(w2_t[0]) / KL_SMALL)
    c_shear = float(np.mean(shear_speeds))
    c_curv = _measure_curvature_speed()
    assert abs(c_shear - 1.0) < 1e-2, f"shear photon c={c_shear:.6f} ≠ 1"
    # the split must be a genuine √2 ratio, not a coincidence of one number
    assert abs((c_curv / c_shear) - np.sqrt(2.0)) < 5e-2, (
        f"curvature/shear speed ratio {c_curv / c_shear:.4f} ≠ √2 — the two T2 "
        f"modes are not split as the substrate requires."
    )
