"""CI sign-gate for the Γ-convention / wave-typed-index fix (A47 v11c/d).

Locks the SIGN of the reflection coefficient against the load type, and the
RECIPROCITY of the two wave-typed indices, so a future edit cannot silently
flip a Γ=−1 matter short into a Γ=+1 anti-trap (both live at |Γ|=1, so a sign
flip is invisible to any magnitude-only assertion).

THE LOCKED CONVENTION (sign-lock w35sn2bq3, 2026-06-17 — task #12):
    n = √(εμ)         tracks the εμ PRODUCT  (the index)
    Z = Z0·√(μ/ε)     tracks the μ/ε RATIO    (the impedance)
  ── load ──────────── Z_eff ──────── Γ = (Z_eff−Z0)/(Z_eff+Z0) ── geometry ──
  magnetic μ-load      Z0·√S → 0       Γ → −1  (SHORT)            matter wall
  symmetric (SYM)      Z0 (invariant)  Γ = 0   (matched)          lens, no wall
  electric ε-load      Z0/√S → ∞       Γ → +1  (OPEN)             anti-trap
  ──────────────────────────────────────────────────────────────────────────
  EM-transverse index  n_EM   = S^{+1/2} → 0   (photon; core stiffens)
  shear / grav index   n_shear= S^{−1/2} → ∞   (Shapiro/lensing; light slows)
                       RECIPROCAL: n_EM · n_shear ≡ 1.

WHY SIGN-NOT-MAGNITUDE: the matter short (Γ=−1) and the ε-load anti-trap (Γ=+1)
have IDENTICAL |Γ|=1. The legacy mode-degenerate n-based Γ=(n−1)/(n+1) was
sign-correct ONLY by coincidence for a μ-load; an ε-load reusing the same form
silently builds the WRONG-sign wall. These asserts catch that flip.

SHA-PINNED to HEAD 65b4bc17 (the FIX-3 load-guard commit). Re-pin on rebase.

consistency-vs-emergence: CONSISTENCY-class — reproduces the boundary-operator
Γ-sign law (universal, every scale) and the wave-speed-identity index split; no
forced dimensionless number, no CODATA-derived target.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.universal_operators import universal_dynamic_impedance
from ave.core.crystal_engine import CrystalEngine
from ave.core.master_equation_fdtd import MasterEquationFDTD

# canonical Γ = (Z2 − Z1)/(Z2 + Z1) with the incident medium = vacuum (Z1 = Z0),
# Z2 = the strained-medium Z_eff. Z0 ≡ 1 in engine units.
Z0 = 1.0


def _gamma(z_eff: float, z0: float = Z0) -> float:
    """Smith Γ reflecting from vacuum (Z0) INTO the strained medium (z_eff)."""
    return (z_eff - z0) / (z_eff + z0)


# ── (i) μ-load → Γ → −1 (the matter SHORT) ───────────────────────────────────
def test_mu_load_gamma_short_minus_one():
    """A magnetic μ-load (Z_eff = Z0·√S → 0) reflects with Γ → −1 (the short).

    Asserts the SIGN: deep saturation drives Γ strictly negative and toward −1,
    never toward +1. A sign flip (the ε-load form leaking in) would FAIL here
    even though |Γ| is unchanged."""
    for S in (0.5, 0.1, 0.01, 1e-4):
        z_eff = float(universal_dynamic_impedance(Z0, S, load="magnetic"))  # Z0·√S
        g = _gamma(z_eff)
        assert g < 0.0, f"μ-load must give Γ<0 (short), got Γ={g:.4f} at S={S}"
    # the deep limit approaches −1 (not +1)
    z_deep = float(universal_dynamic_impedance(Z0, 1e-8, load="magnetic"))
    assert _gamma(z_deep) == pytest.approx(-1.0, abs=1e-3), "μ-load deep limit must be Γ→−1"


# ── (ii) ε-load → Γ → +1 (the OPEN anti-trap) ────────────────────────────────
def test_eps_load_gamma_open_plus_one():
    """An electric ε-load (Z_eff = Z0/√S → ∞) reflects with Γ → +1 (the open).

    Asserts the SIGN: the OPEN form drives Γ strictly positive and toward +1.
    This is the wrong wall for matter — the guard exists so this form is never
    silently grabbed for a μ-load short."""
    for S in (0.5, 0.1, 0.01, 1e-4):
        z_eff = float(universal_dynamic_impedance(Z0, S, load="electric"))  # Z0/√S
        g = _gamma(z_eff)
        assert g > 0.0, f"ε-load must give Γ>0 (open), got Γ={g:.4f} at S={S}"
    z_deep = float(universal_dynamic_impedance(Z0, 1e-8, load="electric"))
    assert _gamma(z_deep) == pytest.approx(1.0, abs=1e-3), "ε-load deep limit must be Γ→+1"


# ── (iii) SYM → Γ = 0 (the matched lens) ─────────────────────────────────────
def test_sym_gamma_matched_zero():
    """The symmetric case (S_μ = S_ε ⇒ Z_eff = Z0 invariant) is reflectionless,
    Γ = 0 — the Achromatic Impedance Lens, no confinement wall regardless of how
    deep S is driven (the ratio, not the product, sets Z)."""
    for S in (0.9, 0.5, 0.1, 0.01):
        z_eff = Z0 * np.sqrt(S / S)  # S_μ = S_ε = S ⇒ √(S_μ/S_ε) = 1
        assert _gamma(float(z_eff)) == pytest.approx(0.0, abs=1e-12), f"SYM must give Γ=0 at S={S}"


# ── gamma_bulk() is the μ-load branch (Γ→−1), end-to-end on the engine ───────
def test_gamma_bulk_is_mu_load_short():
    """CrystalEngine.gamma_bulk() routes the bulk μ-load and drives Γ_min<0
    (toward the short), never positive — the end-to-end sign check on the
    engine's own diagnostic, not just the operator."""
    e = CrystalEngine(N=16)
    c = e.N // 2
    coords = np.arange(e.N) - c
    xx, yy, zz = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(xx**2 + yy**2 + zz**2)
    e.V[:] = 0.85 * (1.0 / np.cosh(r / 2.0))  # localized strained core
    g = e.gamma_bulk()
    assert g["gamma_min"] < 0.0, f"gamma_bulk must be a short (Γ<0), got {g['gamma_min']:.4f}"
    assert g["gamma_mean"] <= 0.0 + 1e-12, "bulk μ-load Γ is never positive (no anti-trap)"


# ── EM/shear index reciprocity: n_EM · n_shear ≡ 1, opposite directions ──────
@pytest.mark.parametrize("Engine", [CrystalEngine, MasterEquationFDTD])
def test_em_shear_index_reciprocity(Engine):
    """n_EM = S^{+1/2} → 0 and n_shear = S^{−1/2} → ∞ are RECIPROCAL: their
    product is identically 1 everywhere, and they move in OPPOSITE directions
    in the saturated core (EM falls below 1, shear rises above 1). A single
    overloaded scalar could not satisfy both — this is the wave-typing lock."""
    e = Engine(N=12) if Engine is CrystalEngine else Engine(N=12, dx=1.0, V_yield=1.0, c0=1.0)
    c = e.N // 2
    e.V[:] = 0.0
    e.V[c, c, c] = 0.7  # one strained cell

    n_em = np.asarray(e.n_em_index())
    n_shear = np.asarray(e.n_shear_index())

    # reciprocity everywhere
    assert np.allclose(n_em * n_shear, 1.0, atol=1e-10), "n_EM · n_shear must be ≡ 1"
    # opposite directions at the strained core
    core = (c, c, c)
    assert n_em[core] < 1.0, f"n_EM must fall below 1 in the core, got {n_em[core]:.4f}"
    assert n_shear[core] > 1.0, f"n_shear must rise above 1 in the core, got {n_shear[core]:.4f}"
    # back-compat alias tracks the EM index
    assert np.allclose(np.asarray(e.refractive_index()), n_em), "refractive_index() must alias n_em_index()"


# ── the ½-power magnitude (sign-safe deepening, not a flip) ──────────────────
def test_half_power_deepens_not_flips():
    """The ¼→½ index magnitude correction DEEPENS the μ-load wall (more negative
    Γ) without flipping its sign — the regression anchor for sign-safety."""
    S = float(np.sqrt(1.0 - 0.99**2))  # A_cap=0.99 floor
    z_quarter = S ** 0.25  # legacy
    z_half = S ** 0.5  # corrected μ-load Z_eff = Z0·√S
    g_quarter = _gamma(z_quarter)
    g_half = _gamma(z_half)
    assert g_half < g_quarter < 0.0, "½ power must deepen the short, both negative"
    assert g_half == pytest.approx(-0.4539, abs=1e-3), "corrected floor (S^{1/2}) = −0.4539"
    assert g_quarter == pytest.approx(-0.2400, abs=1e-3), "legacy floor (S^{1/4}) = −0.2400"
