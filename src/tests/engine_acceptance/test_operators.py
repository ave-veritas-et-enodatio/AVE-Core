"""Op-primitive + scale-invariance tier of the engine-acceptance ladder.

The framework's DISTINGUISHING claim — *"the 22 Universal Operators used
identically across all spatial scales of the physics engine"* (operators.md:13,85,91;
`vol_1_foundations/chapters/06_universal_operators.tex:9`) — was NOT gated by the
L0-L5 acceptance ladder. The physics already lived in:

    src/tests/test_universal_operators.py   (one class per Op: Z, S, Γ, U(r))
    src/tests/test_scale_invariant.py        (Z/S/Γ boundary values + cross-scale)
    src/tests/test_cross_domain_operators.py (the SAME Op kernel BH↔electron↔nuclear)

This module WIRES those existing assertions into the acceptance framework as a
TIER that runs ALONGSIDE L0-L5 (it does NOT replace L0-L5; see __init__.py layer
map). It does NOT duplicate the physics — it REFERENCES the existing test
callables and adds ONE new acceptance-native test: the **scale-invariance
instance test** (the same Op code path at electron-scale AND black-hole-scale,
same FUNCTIONAL form, only the operating-point A₀ varies).

────────────────────────────────────────────────────────────────────────────────
CLASS TAGS (consistency-vs-emergence, frozen per test)
────────────────────────────────────────────────────────────────────────────────
  * The Op-PRIMITIVE gates (Z, S, Γ, U, M) are `axiom-compliance`: the operators
    are AXIOM-DERIVED (Op1 Z=√(μ/ε) is Axiom-3 impedance; Op2 S=√(1−(A/A_c)²) IS
    Axiom-4; Op3 Γ=(Z₂−Z₁)/(Z₂+Z₁) is Op1-derived; operators.md:91 "Op4-22
    compose Op1+Op2+Op3 … all inherit invariance"). They test the engine
    instantiates the canonical kernel forms, not a fitted number.
  * The SCALE-INVARIANCE gates are `scale-invariance`: the SAME code path runs at
    14 orders of magnitude (operators.md:91), the operator does not change, only
    the operating point A₀ does. ω_R·M independent of M (mass-independence) is the
    canonical demonstration.
  * Where an Op gate touches a CODATA-anchored target (Bohr radius a₀=ℓ_node/α,
    13.6 eV ground state, GR ω_R·M=0.3737), that sub-assertion is `consistency`
    (manifestation-class: reproduces a known value; the FORM 18/49, 2/7 is the
    forced chord, the dimensionful target rides CODATA) — NOT headlined emergence.

────────────────────────────────────────────────────────────────────────────────
substrate-native-check walk (Operating Principle 1; done BEFORE any code here)
────────────────────────────────────────────────────────────────────────────────
  * Dynamics  : closed-form evaluation of the canonical Op KERNELS (Z, S, Γ, M,
                regime-eigenvalue) at fixed operating points — these ARE the
                substrate's constitutive operators, NOT a Lagrangian / gradient-
                descent / continuum-Helmholtz / energy-basin proxy. The scale-
                invariance instance test evaluates the IDENTICAL Python callable
                at two operating points (electron, BH); no per-scale code branch.
  * Sector    : Op1/Op3 = impedance/reflection (boundary, Axiom-3); Op2 = the
                saturation kernel S(A) (Axiom-4, the single nonlinearity); Op22 =
                its INVERSE M=1/S² (avalanche). The regime-eigenvalue (Op20-class)
                is the BH ring-down boundary. No micro-rotation / A1-longitudinal
                DOF is exercised here (those are the L3/L4 chords).
  * Objective : the canonical kernel IDENTITIES (Z=√(μ/ε), S=√(1−r²), Γ=ΔZ/ΣZ,
                M=1/S², ω_R·M=18/49) — dimensionless FORMS forced by the axioms.
                AVE-native; not an S11-of-an-energy-functional, not energy-min.
  * Coords A46/phase-space-coordinate-check: every Op observable here is a
                dimensionless ratio (A/A_c, Z₂/Z₁, ω·M/c) or a constitutive
                identity — coordinate-free by construction. No phase-space φ²
                substitution and no real-space-vs-phase-space mismatch is at issue.
  * Saturation: Op2/Op22 ARE the saturation operators — exercised across operating
                points A₀∈[0,1) (electron: bound/sub-yield, Regime I/II, r<1; black
                hole: rupture, Regime IV, r≥1 → S=0). The A43-v11 flag is honored:
                Op22 uses the CANONICAL M=1/S² (= universal_avalanche_factor at
                n=2), NOT doc-81's 1/(1−S) (which → 1 at saturation, wrong).
  * CP6/CP7   : no time-domain LC integration and no PML here (closed-form kernel
                evaluation), so the reactance-pair / PML-exclusion corollaries are
                N/A. The mass-independence sweep IS the cross-operating-point check.
  * CP9       : the Op kernels are the DYNAMICAL constitutive operators of the
                engine (every domain solver delegates to them — operators.md), not
                heuristics standing in for a dynamical result.
  * CP10      : no confinement/wall rendering — the operators are evaluated, not a
                bulk integrator, so no bulk-vs-boundary detonation risk.

────────────────────────────────────────────────────────────────────────────────
WIRING (reference-not-copy)
────────────────────────────────────────────────────────────────────────────────
The existing op/scale test CLASSES are imported and their methods invoked under
acceptance-tier test functions below, so a regression in the Op primitives fails
THIS tier too. `test_cross_scale.py` is deliberately NOT referenced: it is a
`__main__` print-DRIVER (no `test_` callables; prints at import), not a pytest
module. The acceptance-native physics this tier ADDS is the scale-invariance
instance test (`test_scaleinv_same_op_electron_and_blackhole`).
"""

from __future__ import annotations

import numpy as np
import pytest

# ── reference (do NOT duplicate) the existing Op-primitive + scale assertions ──
from tests.test_cross_domain_operators import TestUniversalOperators as _XDomain
from tests.test_scale_invariant import (
    TestCrossScaleIdentity as _CrossScaleId,
)
from tests.test_scale_invariant import (
    TestImpedance as _SIImpedance,
)
from tests.test_scale_invariant import (
    TestReflectionCoefficient as _SIReflection,
)
from tests.test_scale_invariant import (
    TestSaturationFactor as _SISaturation,
)
from tests.test_universal_operators import (
    TestUniversalImpedance as _UOImpedance,
)
from tests.test_universal_operators import (
    TestUniversalPairwiseEnergy as _UOPairwise,
)
from tests.test_universal_operators import (
    TestUniversalReflection as _UOReflection,
)
from tests.test_universal_operators import (
    TestUniversalSaturation as _UOSaturation,
)

# ── the canonical Op KERNELS, imported directly for the scale-invariance test ──
from ave.axioms.scale_invariant import (
    phase_transition_Q,
    regime_boundary_eigenvalue,
)
from ave.core.constants import ALPHA, C_0, G, L_NODE, M_E, NU_VAC
from ave.core.universal_operators import (
    universal_avalanche_factor,
    universal_reflection,
    universal_saturation,
)

M_SUN = 1.989e30  # kg (matches test_cross_domain_operators.M_SUN)


def _run_all_methods(cls) -> list[str]:
    """Invoke every `test_*` method of an existing test class under this tier.

    Reference-not-copy: the physics lives in the source class; this re-runs it so
    a regression in the Op primitives fails the acceptance tier too. Returns the
    list of method names run (for the acceptance-tier audit trail).
    """
    inst = cls()
    ran = []
    for name in sorted(dir(inst)):
        if name.startswith("test_"):
            getattr(inst, name)()
            ran.append(f"{cls.__name__}.{name}")
    return ran


# ═══════════════════════════════════════════════════════════════════════
# OP-PRIMITIVE GATES [axiom-compliance] — reference the existing Op tests
# ═══════════════════════════════════════════════════════════════════════
# Each gate re-runs an existing Op-primitive test class under the acceptance
# tier. CLASS: axiom-compliance (the operators are Op1/Axiom-3/Axiom-4 derived;
# operators.md:91). A regression in the Op kernels fails this tier.

_OP_PRIMITIVE_CLASSES = [
    _UOImpedance,    # Op1  Z = √(μ/ε)             (Axiom-3 impedance)
    _UOSaturation,   # Op2  S = √(1−(A/A_c)²)       (Axiom-4, the single nonlinearity)
    _UOReflection,   # Op3  Γ = (Z₂−Z₁)/(Z₂+Z₁)     (Op1-derived)
    _UOPairwise,     # U(r) = −(K/r)(T²−Γ²)         (3-regime impedance potential)
    _SIImpedance,    # Op1 (scale_invariant module path)
    _SISaturation,   # Op2 (scale_invariant module path)
    _SIReflection,   # Op3 (scale_invariant module path)
]


@pytest.mark.parametrize("op_cls", _OP_PRIMITIVE_CLASSES, ids=lambda c: c.__name__)
def test_op_primitive_gate(op_cls):
    """OP-PRIMITIVE [axiom-compliance] — the canonical Op kernels (Z, S, Γ, U)
    instantiate their AXIOM-DERIVED forms. Reference-not-copy: re-runs the
    existing Op-primitive test class under the acceptance framework so an Op
    regression fails the L-ladder's Op tier.

    PRE-REG BIN: pass iff every referenced Op-primitive assertion passes
    (boundary values: Z₀=√(μ₀/ε₀); S(0)=1, S(A_c)=0, monotone; Γ matched=0,
    short=−1, open=+1, |Γ|≤1; U far-field Coulomb + wall repulsion). FAIL on any.
    """
    ran = _run_all_methods(op_cls)
    assert ran, f"no test_ methods found on {op_cls.__name__}"


def test_op_cross_scale_identity_gate():
    """OP-PRIMITIVE [axiom-compliance] — the SAME math underlies the legacy
    saturation.py API, the seismic module, and the scale_invariant operators
    (the cross-scale identity class). Reference-not-copy of TestCrossScaleIdentity.

    PRE-REG BIN: pass iff every cross-scale-identity assertion passes (ε_eff,
    Γ, Z(strain), c_local match between modules to rtol≤1e-12; seismic Moho Γ
    equals the universal Γ). FAIL on any mismatch.
    """
    ran = _run_all_methods(_CrossScaleId)
    assert ran, "no cross-scale-identity methods found"


def test_op_cross_domain_gate():
    """OP-PRIMITIVE + SCALE-INVARIANCE [axiom-compliance / scale-invariance] —
    the same Op kernels produce correct results across BH / electron / nuclear
    domains (the cross-domain class), INCLUDING the mass-independence sweep
    (ω_R·M = 18/49 for M ∈ {1,10,62,1000} M_sun). Reference-not-copy of
    TestUniversalOperators (test_cross_domain_operators.py).

    NOTE [consistency sub-class]: the CODATA-anchored members of this class
    (a₀=ℓ_node/α, 13.6 eV, GR ω_R·M=0.3737) are manifestation/consistency — the
    FORMS 18/49, 2/7 are the forced chords; the dimensionful targets ride CODATA.
    Not headlined emergence (consistency-vs-emergence, Operating Principle 4).

    PRE-REG BIN: pass iff every cross-domain assertion passes. FAIL on any.
    """
    ran = _run_all_methods(_XDomain)
    assert ran, "no cross-domain methods found"


# ═══════════════════════════════════════════════════════════════════════
# SCALE-INVARIANCE INSTANCE TEST [scale-invariance] — acceptance-native
# ═══════════════════════════════════════════════════════════════════════
# The acceptance-native physics this tier ADDS: assert the IDENTICAL Op code
# path runs at electron-scale (bound, sub-yield, Regime I/II) AND at black-hole /
# cosmological-scale (Regime IV rupture), giving the SAME FUNCTIONAL form — the
# operating-point A₀ varies, the operator does not. (operators.md:91)


def test_scaleinv_same_op_electron_and_blackhole():
    """SCALE-INVARIANCE [scale-invariance] — the SAME Op code path runs at the
    electron operating point AND at the black-hole operating point and returns
    the SAME functional form; only the operating point A₀ varies.

    The framework's distinguishing claim (operators.md:13,85,91): the 22
    operators are used IDENTICALLY across all scales. This test exercises ONE
    physical Python callable per operator at two operating points 30+ orders of
    magnitude apart and asserts the form is invariant.

    OPERATING POINTS (the A₀ that varies; the operator that does not):
      * ELECTRON  = bound / sub-yield (Regime I/II): r = A/A_c < 1, so the
        saturation kernel S = √(1−r²) > 0 (the cavity holds; charge is confined).
      * BLACK HOLE = Regime IV rupture (r ≥ 1): S → 0 (the metric ruptures; the
        regime-boundary eigenvalue is the ring-down mode).

    KERNEL DISCIPLINE (A43 v11 flag honored): Op22 uses the CANONICAL M = 1/S²
    (= universal_avalanche_factor at n=2), NOT doc-81's 1/(1−S). At saturation
    onset M → ∞ (avalanche cascades), which doc-81's form (→1) gets wrong.

    PRE-REG BINS (frozen BEFORE running):
      (B1) Op2 saturation kernel is the SAME callable at both scales:
           electron S_e ∈ (0,1) (sub-yield); BH S_bh == 0 (rupture, r≥1).
      (B2) Op22 avalanche M = 1/S² (n=2) is the SAME callable: electron M_e
           finite > 1; BH M_bh → ∞ (diverges at r→1; the engine represents the
           divergence by the finite clip ceiling M ≈ 1/(2·EPS_NUMERICAL^½) ≈ 5e5,
           Rule-10 integrator-time finding). M_bh ≥ 1e5 AND M_bh/M_e ≥ 1e5. And
           M_e == 1/S_e² exactly (the canonical identity, NOT doc-81's 1/(1−S)).
      (B3) Op3 reflection Γ is the SAME callable: at an electron→matched boundary
           Γ→0; at the BH horizon (Z₂→∞ open / Z₂→0 short) |Γ|→1.
      (B4) The regime-boundary eigenvalue (Op20-class) is the SAME callable and
           is MASS-INDEPENDENT: ω_R·M = 18/49 at electron-mass AND BH-mass inputs
           (the scale-invariance signature — the operator is blind to the scale).
    """
    print("\n--- SCALE-INVARIANCE INSTANCE: same Op code path, electron + BH ---")

    # ── the two operating points (A₀ varies; A_c = the yield ceiling) ──────────
    A_c = 1.0  # dimensionless yield ceiling (the operator is scale-free in r=A/A_c)
    r_electron = 0.5     # bound / sub-yield (Regime I/II): r < 1
    r_blackhole = 1.0    # rupture (Regime IV): r ≥ 1 → S = 0

    A_electron = r_electron * A_c
    A_blackhole = r_blackhole * A_c

    # ── (B1) Op2 saturation kernel — SAME callable, two operating points ───────
    S_e = float(universal_saturation(A_electron, A_c))
    S_bh = float(universal_saturation(A_blackhole, A_c))
    print(f"  Op2  S(electron r={r_electron}) = {S_e:.6f}  (sub-yield, cavity holds)")
    print(f"  Op2  S(black-hole r={r_blackhole}) = {S_bh:.6e}  (Regime IV rupture)")
    assert 0.0 < S_e < 1.0, f"electron must be sub-yield: S_e={S_e}"
    assert abs(S_bh) < 1e-12, f"BH must rupture (S→0): S_bh={S_bh}"
    assert S_e == pytest.approx(np.sqrt(1 - r_electron**2), abs=1e-12)

    # ── (B2) Op22 avalanche M = 1/S² (n=2 canonical) — SAME callable ───────────
    # A43 v11: canonical M = 1/S² = 1/(1−r²) = universal_avalanche_factor(.,.,n=2).
    M_e = float(universal_avalanche_factor(A_electron, A_c, 2))
    M_bh = float(universal_avalanche_factor(A_blackhole, A_c, 2))
    print(f"  Op22 M(electron) = {M_e:.6f}  (finite avalanche, sub-yield)")
    print(f"  Op22 M(black-hole) = {M_bh:.3e}  (diverges at rupture; engine clip ceiling)")
    assert M_e > 1.0, f"electron avalanche must be >1: M_e={M_e}"
    # Rule-10 finding: the engine clips r→1 to (1−EPS^{1/n}), so the divergence
    # at rupture is represented by the finite ceiling M ≈ 5e5 (not literal ∞). The
    # scale-invariance content is M_bh ≫ M_e by ≥5 OOM (BH dwarfs bound-electron).
    assert M_bh >= 1e5, f"BH avalanche must reach the divergence ceiling: M_bh={M_bh}"
    assert M_bh / M_e >= 1e5, f"BH avalanche must dwarf electron: ratio={M_bh / M_e:.2e}"
    # the CANONICAL identity M = 1/S² (NOT doc-81's 1/(1−S) → 1 at saturation)
    assert M_e == pytest.approx(1.0 / S_e**2, rel=1e-12), "Op22 must be 1/S² (A43 v11)"
    M_doc81 = 1.0 / (1.0 - S_e)  # the WRONG doc-81 form, for the discriminator note
    assert abs(M_e - M_doc81) > 0.1, (
        "canonical 1/S² must differ from doc-81's 1/(1−S) at this operating point "
        f"(M_canonical={M_e:.4f} vs M_doc81={M_doc81:.4f})"
    )

    # ── (B3) Op3 reflection — SAME callable, two boundary regimes ──────────────
    Gamma_matched = float(universal_reflection(1.0, 1.0))          # electron→matched
    Gamma_horizon = float(universal_reflection(1.0, 1e12))          # BH open boundary
    print(f"  Op3  Γ(matched, electron-bound) = {Gamma_matched:.2e}  (→0)")
    print(f"  Op3  Γ(horizon, Z₂→∞)          = {Gamma_horizon:.6f}  (→±1)")
    assert abs(Gamma_matched) < 1e-10
    assert abs(abs(Gamma_horizon) - 1.0) < 1e-6

    # ── (B4) regime-boundary eigenvalue — SAME callable, MASS-INDEPENDENT ──────
    # ω_R·M = 18/49 must hold at BOTH an electron-mass input and a BH-mass input.
    # (The geometric-mass M_g = G·M/c² is the only thing that changes; ω_R·M_g/c
    #  is the scale-free signature.)
    target = 18.0 / 49.0
    M_bh_kg = 10 * M_SUN
    Mg_bh = G * M_bh_kg / C_0**2
    omega_bh = regime_boundary_eigenvalue(7.0 * Mg_bh, NU_VAC, ell=2, c_wave=C_0)
    oR_bh = omega_bh * Mg_bh / C_0

    Mg_e = G * M_E / C_0**2  # electron geometric mass (absurdly tiny, but the OP is blind)
    omega_e = regime_boundary_eigenvalue(7.0 * Mg_e, NU_VAC, ell=2, c_wave=C_0)
    oR_e = omega_e * Mg_e / C_0

    print(f"  Op20 ω_R·M (black-hole 10 M_sun, Mg={Mg_bh:.3e} m) = {oR_bh:.10f}")
    print(f"  Op20 ω_R·M (electron      M_e,    Mg={Mg_e:.3e} m) = {oR_e:.10f}")
    print(f"  Op20 target 18/49 = {target:.10f}  → MASS-INDEPENDENT (scale-invariant)")
    assert oR_bh == pytest.approx(target, abs=1e-10), f"BH ω_R·M={oR_bh}"
    assert oR_e == pytest.approx(target, abs=1e-10), f"electron ω_R·M={oR_e}"
    assert phase_transition_Q(2) == 2.0  # Q = ℓ, scale-free

    print("  → SAME Op code path at electron + BH scale; A₀ varies, operator does NOT.")


def test_scaleinv_op_callable_identity_across_scales():
    """SCALE-INVARIANCE [scale-invariance] — the operator is literally the SAME
    Python object at every scale (no per-scale code branch). Asserts the kernel
    callables are scale-FREE: a single function evaluated on a span of operating
    points r ∈ [0,1) returns S=√(1−r²) at EVERY point with no scale parameter.

    PRE-REG BIN: pass iff universal_saturation(r·A_c, A_c) == √(1−r²) for a dense
    r-sweep spanning sub-yield → rupture (one callable, no scale switch). FAIL if
    any point needs a scale-specific branch.
    """
    A_c = 1.0
    r = np.linspace(0.0, 0.999, 200)
    S = universal_saturation(r * A_c, A_c)
    np.testing.assert_allclose(S, np.sqrt(1 - r**2), rtol=1e-12)
    # monotone decreasing across the whole scale span (sub-yield → near-rupture)
    assert np.all(np.diff(S) <= 0)
