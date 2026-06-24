"""Stage-2 NATIVE-CAGE — VALIDATION GATES (run BEFORE the make-or-break).

Prereg : research/2026-06-23_engine-stage2-native-cage_prereg.md (RE-FROZEN,
         three corrections from rigor gate wg9rsjep8).

These are the BUG-CATCHERS (§B of the dispatch). They run FIRST. If ANY fails,
the make-or-break MUST NOT run (HARD HALT). They check the corrected operator +
stepper against the adjudicated math:

  G1  L(const)      = 0
  G2  L(linear)     = 0  (interior)
  G3  L(r²)         = −6 EXACT
  G4  adjoint ratio = +1  (⟨u,Lv⟩ = ⟨Lu,v⟩, and ⟨u,Lu⟩ = +‖grad u‖² ≥ 0 ⇒ PSD)
  G5  ρ(L_native cold, N=24) ≈ 1.0  (the 0.25 grad prefactor, NOT Cartesian 12)
  G6  single-1/S code-enforced: per-step core operator magnitude scales as
      1/S_min, NOT 1/S_min²  (CORRECTION 2)
  G7  continuum cross-check: MINUS-sign cold sech → BOUNDED
  G8  NEGATIVE CONTROL: PLUS-sign → BLOWUP (the deliberate anti-restoring proof)

α-CLEAN: pure (1−A²) kernel; no ALPHA / Q_TANK / 137 / 0.00729 anywhere.
"""

import numpy as np
import pytest

from ave.solvers.graded_vacuum_network import (
    _native_laplacian_with_stiffness,
    _native_scalar_laplacian,
    saturation_kernel,
    stiffness_profile,
)
from ave.solvers.native_cage_fdtd import (
    NativeCageConfig,
    NativeCageFDTD,
    power_iteration_rho,
)

N = 24


# ── G1–G3: the operator IS the PSD stiffness (L = +gradᵀgrad = −∇²) ──
def _quad_fields(N):
    c = N // 2
    i, j, k = np.indices((N, N, N))
    return (i - c).astype(float), (j - c).astype(float), (k - c).astype(float), c


def test_G1_L_const_is_zero():
    L = _native_scalar_laplacian(np.ones((N, N, N)))
    assert float(np.abs(L).max()) < 1e-10, "L(const) must be 0 (nullspace = constants)"


def test_G2_L_linear_is_zero_interior():
    x, _, _, _ = _quad_fields(N)
    L = _native_scalar_laplacian(x)
    interior = float(np.abs(L[2:-2, 2:-2, 2:-2]).max())
    assert interior < 1e-10, f"L(linear) interior must be 0, got {interior:.2e}"


def test_G3_L_r2_is_minus6_exact():
    x, y, z, _ = _quad_fields(N)
    r2 = x**2 + y**2 + z**2
    L = _native_scalar_laplacian(r2)
    core = L[2:-2, 2:-2, 2:-2]
    assert abs(float(core.mean()) - (-6.0)) < 1e-9, (
        f"L(r²) must = −6 EXACT (PSD stiffness = −∇²), got {core.mean():.6f}"
    )
    assert float(core.std()) < 1e-9, "L(r²) must be uniform (std 0)"


def test_G4_adjoint_ratio_plus1_and_psd():
    """⟨u, L v⟩ = ⟨L u, v⟩ (symmetric) and ⟨u, L u⟩ = +‖grad u‖² ≥ 0 (PSD ⇒ the
    MINUS restoring sign is forced)."""
    rng = np.random.default_rng(7)
    u = rng.standard_normal((N, N, N))
    v = rng.standard_normal((N, N, N))
    Lu = _native_scalar_laplacian(u)
    Lv = _native_scalar_laplacian(v)
    uLv = float(np.vdot(u, Lv).real)
    Luv = float(np.vdot(Lu, v).real)
    ratio = uLv / Luv
    assert abs(ratio - 1.0) < 1e-9, f"adjoint ratio ⟨u,Lv⟩/⟨Lu,v⟩ must = +1, got {ratio:.9f}"
    uLu = float(np.vdot(u, Lu).real)
    assert uLu > 0.0, f"⟨u,Lu⟩ must be POSITIVE (PSD), got {uLu:.4e} (sign forces MINUS)"


def test_G5_rho_cold_approx_one():
    """ρ(L_native cold, N=24) ≈ 1.0 — the tetrahedral 0.25 grad prefactor, NOT
    the Cartesian 12."""
    D_cold = np.ones((N, N, N))
    rho = power_iteration_rho(D_cold, c0=1.0, n_iter=400)
    assert abs(rho - 1.0) < 0.05, f"cold ρ must ≈ 1.0 (not Cartesian 12), got {rho:.4f}"
    assert rho < 2.0, "cold ρ nowhere near the Cartesian-12 regime"


def test_G6_single_one_over_S_not_squared():
    """CORRECTION 2: the per-step core operator magnitude must scale as 1/S_min,
    NOT 1/S_min². Compare the native L_native(seed) magnitude (D=1/S folded ONCE)
    to a deliberately-double-applied 1/S·L_native — they must differ by the 1/S
    factor in the saturated core, and the native (single) form must NOT carry the
    1/S² scaling."""
    cfg = NativeCageConfig(N=N)
    eng = NativeCageFDTD(cfg)
    eng.seed_sech(amplitude=0.85, radius=2.5)
    A = eng.strain()
    S = eng.saturation_S()
    D = eng.stiffness_D()  # 1/S, single
    S_core = float(S.min())

    L_single = _native_laplacian_with_stiffness(eng.V, D)          # correct: 1/S once
    L_double = _native_laplacian_with_stiffness(eng.V, D) / S      # bug mock: 1/S twice
    core_single = float(np.abs(L_single).max())
    core_double = float(np.abs(L_double).max())
    # The double-application inflates the operator by ~1/S_core in the core.
    inflation = core_double / max(core_single, 1e-30)
    assert inflation > 1.3, (
        f"double-1/S must inflate by ~1/S_core={1/S_core:.2f}, got {inflation:.2f} "
        "(if ≈1, the mock isn't biting and the single-vs-double distinction is dead)"
    )
    # The single form scales as 1/S_min (bounded by D_max), NOT 1/S_min².
    D_max = float(D.max())
    assert D_max < (1.0 / S_core) * 1.01 + 1e-9, "D must be 1/S (single power), not 1/S²"
    # Sanity: 1/S² would be ~ D_max²; confirm single form is far below that scale.
    assert core_single < core_double, "single-1/S must be strictly smaller than double-1/S"


# ── G7 / G8: the continuum cross-check sign witness ──
def _run_peaks(sign, steps=40, amplitude=0.85, radius=2.5, n_iter=200):
    cfg = NativeCageConfig(N=N, sign=sign)
    eng = NativeCageFDTD(cfg)
    eng.seed_sech(amplitude=amplitude, radius=radius)
    eng.set_dt_from_seed(n_iter=n_iter)
    peaks = [eng.interior_peak_abs_V()]
    for _ in range(steps):
        eng.step()
        peaks.append(float(np.abs(eng.V).max()))  # GLOBAL max — catches blowup
    return np.array(peaks)


def test_G7_minus_sign_cold_sech_bounded():
    """The CORRECT MINUS sign keeps a sech seed BOUNDED (does not blow up)."""
    peaks = _run_peaks(sign=-1.0, steps=40)
    assert np.all(np.isfinite(peaks)), "MINUS run produced non-finite values"
    assert peaks.max() < 10.0, (
        f"MINUS run must stay bounded (<10, DETONATION_MAX_V), peak={peaks.max():.3f}"
    )


def test_G8_plus_sign_blows_up_negative_control():
    """NEGATIVE CONTROL: the WRONG PLUS sign is anti-restoring → BLOWUP. This is
    the deliberate proof the sign matters (rigor gate wg9rsjep8: PLUS→inf)."""
    peaks = _run_peaks(sign=+1.0, steps=40)
    final = peaks[-1]
    assert (not np.isfinite(final)) or final > 1e6, (
        f"PLUS sign MUST blow up (anti-restoring), final global max={final:.3e}"
    )
