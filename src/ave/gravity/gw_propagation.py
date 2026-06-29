"""
AVE Gravitational Wave Propagation
====================================

Gravitational waves in the AVE framework are transverse inductive
shear waves propagating through the structured LC vacuum. They are
governed by the SAME impedance, saturation, and reflection operators
used across all other scales.

Physical picture (from Ch. 19):
  - Mass = localized topological energy deficit in the LC lattice
  - Gravity = dielectric refraction: n(r) varies radially around mass
  - GW = transverse shear (μ-sector) perturbation radiating outward
  - At h ~ 10⁻²¹, the strain is 10¹⁹× below V_SNAP → no saturation
  - Therefore: perfectly linear, lossless, c-speed propagation

──────────────────────────────────────────────────────────────────────
CHANNEL-SPLIT (the substrate-forced result — three-impedance law).
The horizon's reflection behaviour is a CHANNEL question. Two channels,
two answers (NOT one "absorber" answer):

EM-transverse channel (Symmetric Gravity):
  Refractive index: n(r) = 1 / (1 − r_s/r)
  ε_eff(r) = ε₀ · n(r),  μ_eff(r) = μ₀ · n(r)
  Z_EM(r) = √(μ_eff/ε_eff) = √(μ₀·n / ε₀·n) ≡ Z₀ (CONSTANT!)
  → Γ_EM = 0 everywhere — perfect EM matching, light transparent /
    index-gradient-captured. NO EM-channel echoes. The event horizon is
    a refractive singularity (n → ∞, c_local → 0) in the EM channel.
  Functions: gravitational_impedance() / horizon_reflection().

Shear (+ bulk) channel (lattice phase transition at r_sat):
  At r_sat = 7GM/c² = 3.5·r_s the radial strain ε₁₁ = 7GM/(c²r) → 1,
  the lattice phase-transitions and the shear modulus G_shear → 0.
  Shear speed:     c_shear(r) = c · (1 − ε₁₁²)^(1/4)  → 0 at r_sat
  Shear impedance: Z_shear(r) = ρ · c_shear(r)        → 0 at r_sat
  A Z_shear → 0 free surface is an Op3 SHORT:
  → Γ_shear = (Z_int − Z_ext)/(Z_int + Z_ext) → (0 − ρc)/(0 + ρc) = −1.
  GW are TRANSVERSE SHEAR modes, so they REFLECT totally off r_sat:
  gravitational ringdown ECHOES ARE PREDICTED (reflect ⇒ echo;
  retrospective — not a SHA-pinned forward prereg).
  Functions: shear_impedance() / shear_horizon_reflection().

The Γ = −1 short is the UNIVERSAL Z→0 kernel, not electron-only: the
electron applies it in the bulk channel at the knot core; the BH applies
it in the shear+bulk channels at r_sat. Canonical leaf:
manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/
electron-bh-isomorphism.md:34-42. Corroborated by
bulk-impedance-at-saturation-boundary.md:51,
lattice-extreme-bh-rationality.md:75, existing-signatures.md:36.

(Walk-back 2026-06-17: the prior "Γ = 0 everywhere / no black hole
echoes / not an impedance boundary" docstring was a CHANNEL CONFLATION —
right number, wrong channel — taking the EM Γ_EM=0 and extending it to
shear. Superseded by the channel-split above.)
──────────────────────────────────────────────────────────────────────
"""

import numpy as np

from ave.axioms.scale_invariant import impedance, reflection_coefficient, saturation_factor
from ave.core.constants import C_0, EPSILON_0, L_NODE, M_SUN, MU_0, RHO_BULK, V_SNAP, Z_0, G

# ═══════════════════════════════════════════════════════════════
# Schwarzschild refractive profile — gravity as symmetric refraction
# ═══════════════════════════════════════════════════════════════


def schwarzschild_radius(M: float) -> float:
    r"""
    Schwarzschild radius of a mass M.

    .. math::
        r_s = \frac{2 G M}{c^2}

    Args:
        M: Mass [kg].

    Returns:
        Schwarzschild radius [m].
    """
    return 2 * G * M / C_0**2


def refractive_index(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Effective refractive index around a Schwarzschild mass.

    Symmetric Gravity requires both ε and μ to scale by the same
    factor n(r), preserving Z ≡ Z₀. The simplest mapping from
    the Schwarzschild metric gives:

    .. math::
        n(r) = \frac{1}{1 - r_s / r}

    As r → r_s: n → ∞ (light stops — refractive singularity).
    Far from mass: n → 1 (flat vacuum).

    This produces gravitational lensing identically to a graded-index
    optical medium, and time dilation via c_local = c/n.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Refractive index (≥ 1).
    """
    from ave.core.constants import NU_VAC
    from ave.core.universal_operators import universal_refractive_index

    r = np.asarray(r, dtype=float)
    ratio = np.minimum(r_s / r, 0.9999)
    # n(r) = 1 / (1 - r_s/r)
    # n(r) = 1 + NU_VAC * eps_11
    # => eps_11 = (1 / (1 - ratio) - 1.0) / NU_VAC = (ratio / (1 - ratio)) / NU_VAC
    eps_11 = (ratio / (1.0 - ratio)) / NU_VAC
    return universal_refractive_index(eps_11, nu_vac=NU_VAC)


def epsilon_eff_schwarzschild(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Effective permittivity in a Schwarzschild gravity well.

    Symmetric Gravity: ε and μ scale identically by n(r).

    .. math::
        \varepsilon_{eff}(r) = \varepsilon_0 \cdot n(r)

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Effective permittivity [F/m].
    """
    n = refractive_index(r, r_s)
    return EPSILON_0 * n


def mu_eff_schwarzschild(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Effective permeability in a Schwarzschild gravity well.

    Symmetric Gravity: ε and μ scale identically by n(r).

    .. math::
        \mu_{eff}(r) = \mu_0 \cdot n(r)

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Effective permeability [H/m].
    """
    n = refractive_index(r, r_s)
    return MU_0 * n


def gravitational_impedance(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    EM-CHANNEL characteristic impedance at radius r in a Schwarzschild field.

    Under Symmetric Gravity, the EM-transverse impedance is strictly
    invariant (μ and ε scale together):

    .. math::
        Z_{EM}(r) = \sqrt{\mu_{eff} / \varepsilon_{eff}}
             = \sqrt{\mu_0 \cdot n / (\varepsilon_0 \cdot n)}
             = Z_0

    The EM impedance is CONSTANT everywhere → no EM mismatch, no EM
    reflection, no EM-channel echoes (light transparent / index-captured).

    NOTE (channel-split): this is the EM channel ONLY. The shear channel
    is governed by ``shear_impedance()`` and goes Z_shear → 0 at r_sat
    (Γ_shear = −1, GW reflect). See module docstring.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        EM impedance [Ω] (always Z₀).
    """
    # EM impedance is strictly Z₀ under symmetric gravity.
    # We compute it explicitly to verify numerical consistency.
    mu = mu_eff_schwarzschild(r, r_s)
    eps = epsilon_eff_schwarzschild(r, r_s)
    return impedance(mu, eps)


def horizon_reflection(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    EM-CHANNEL reflection coefficient at radius r in a Schwarzschild field.

    Under Symmetric Gravity, Γ_EM = 0 everywhere (perfect EM matching):

    .. math::
        \Gamma_{EM}(r) = \frac{Z_{EM}(r) - Z_0}{Z_{EM}(r) + Z_0} = 0

    There is NO EM reflection at the event horizon: light is transparent /
    index-gradient-captured, no EM-channel echoes.

    NOTE (channel-split): the SHEAR/GW channel REFLECTS — use
    ``shear_horizon_reflection()``, which returns Γ_shear = −1 at r_sat.
    GW are transverse shear modes; gravitational ringdown echoes are
    predicted (reflect ⇒ echo). See module docstring.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        EM reflection coefficient (always ~0).
    """
    Z_r = gravitational_impedance(r, r_s)
    return reflection_coefficient(Z_0, Z_r)


# ═══════════════════════════════════════════════════════════════
# Shear (GW) channel — lattice phase transition at r_sat → REFLECT
# ═══════════════════════════════════════════════════════════════

# r_sat / r_s = 1 / ν_vac = 7/2 = 3.5 (the shear/bulk rupture boundary
# sits deeper than the EM r_s; radial strain ε₁₁ = 7GM/(c²r) reaches 1
# at r_sat = 7GM/c² = 3.5·r_s).
R_SAT_OVER_RS: float = 3.5


def saturation_radius(r_s: float) -> float:
    r"""
    Shear/bulk rupture boundary r_sat = 7GM/c² = 3.5·r_s.

    This is where the radial strain ε₁₁ = 7GM/(c²r) → 1, the lattice
    phase-transitions, and the shear modulus G_shear → 0. It sits DEEPER
    than the EM event horizon r_s = 2GM/c² (ratio 1/ν_vac = 3.5).

    Args:
        r_s: Schwarzschild radius [m].

    Returns:
        Saturation (shear/bulk rupture) radius [m].
    """
    return R_SAT_OVER_RS * r_s


def radial_strain(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Radial (ε₁₁) strain in the shear/bulk gauge.

    .. math::
        \varepsilon_{11}(r) = \frac{7 G M}{c^2 r} = \frac{r_{sat}}{r}

    Reaches unity at r_sat = 3.5·r_s (shear/bulk rupture). Clipped to
    [0, 1] for the saturation kernel (interior is ruptured, ε₁₁ ≡ 1).

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Radial strain ε₁₁ ∈ [0, 1].
    """
    r = np.asarray(r, dtype=float)
    r_sat = saturation_radius(r_s)
    return np.minimum(r_sat / r, 1.0)


def shear_wave_speed(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    Local shear (GW) propagation speed in a Schwarzschild field.

    The shear-channel group velocity uses the canonical Axiom-4 melt
    (electron-bh-isomorphism.md line 33):

    .. math::
        c_{shear}(r) = c \cdot (1 - \varepsilon_{11}^2)^{1/4}
                     = c \cdot \sqrt{S(\varepsilon_{11})}

    where S = √(1 − ε₁₁²) is the universal saturation factor. As
    r → r_sat, ε₁₁ → 1, G_shear → 0, and c_shear → 0 (shear restoring
    force vanishes — the topology melts).

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Local shear-wave speed [m/s] (→ 0 at r_sat).
    """
    eps11 = radial_strain(r, r_s)
    S = saturation_factor(eps11, yield_limit=1.0)  # S = √(1 − ε₁₁²)
    return C_0 * np.sqrt(S)  # c·(1 − ε₁₁²)^(1/4)


def shear_impedance(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    SHEAR-CHANNEL characteristic impedance Z_shear = ρ·c_shear.

    Unlike the EM channel (Z_EM ≡ Z₀, invariant), the shear impedance
    COLLAPSES at the rupture boundary because c_shear → 0:

    .. math::
        Z_{shear}(r) = \rho \cdot c_{shear}(r) \to 0 \quad (r \to r_{sat})

    A Z_shear → 0 free surface is exactly a solid→liquid interface: an
    Op3 short. ρ is the bulk vacuum mass density (ρ_bulk); only the RATIO
    of interior-to-exterior Z_shear sets Γ_shear, so the absolute ρ scale
    cancels in the reflection coefficient.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Shear impedance [kg·m⁻²·s⁻¹] (→ 0 at r_sat).
    """
    return RHO_BULK * shear_wave_speed(r, r_s)


def shear_horizon_reflection(r: float | np.ndarray, r_s: float) -> float | np.ndarray:
    r"""
    SHEAR-CHANNEL (GW) reflection coefficient at radius r.

    A GW (transverse shear mode) incident from the unsaturated exterior
    (Z_shear ≈ ρc) onto the saturated interior (Z_shear → 0) reflects via
    the SAME universal operator used at every scale:

    .. math::
        \Gamma_{shear}(r) = \frac{Z_{shear}(r) - Z_{shear,\,ext}}
                                  {Z_{shear}(r) + Z_{shear,\,ext}}
                          \;\xrightarrow{\;r \to r_{sat}\;}\; -1

    where Z_shear,ext is the far-field shear impedance (ρc). At/inside
    r_sat, Z_shear(r) → 0 ⇒ Γ_shear → −1 (TOTAL reflection). GW reflect
    totally off the horizon: gravitational ringdown echoes are predicted
    (reflect ⇒ echo; retrospective, not a forward prereg).

    This is the channel that REFLECTS — contrast ``horizon_reflection()``
    (EM channel, Γ_EM = 0). Both are the same operator on different
    channel impedances.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].

    Returns:
        Shear reflection coefficient (→ −1 at r_sat).
    """
    # Far-field exterior shear impedance: ε₁₁ → 0 ⇒ c_shear → c ⇒ Z = ρc.
    Z_ext = RHO_BULK * C_0
    Z_int = shear_impedance(r, r_s)
    # reflection_coefficient(Z1, Z2) = (Z2 − Z1)/(Z2 + Z1); incident from
    # exterior (Z1 = Z_ext) into interior (Z2 = Z_int) ⇒ (Z_int − Z_ext)/(…).
    return reflection_coefficient(Z_ext, Z_int)


# ═══════════════════════════════════════════════════════════════════════════════
# STAGE-1 GR-EXTENSION — the saturating-modulus correction ON the linear core
# ═══════════════════════════════════════════════════════════════════════════════
# SUBSTRATE-NATIVE FRAMING (the vacuum is a real saturable elastic medium):
#   The INHERITED linear core is the WEAK-FIELD limit, NOT re-derived here:
#     elastic-Poisson   −(c⁴/7G)∇²ε₁₁ = T₀₀   ⇒   ε₁₁(r) = 7GM/(c²r) = r_sat/r
#     refractive index  n(r) = 1 + (2/7)·ε₁₁   (Op19, refractive_index() above —
#                                               LEFT UNCHANGED; EM is a spectator).
#   The CORRECTION is a saturating MODULUS on the elliptic operator:
#     −∇·[ (c⁴/7G)·D(A)·∇ε₁₁ ] = T₀₀ ,   A = ε₁₁/ε_yield   (ε_yield = 1).
#   This is mundane elastic YIELD — a graded stiffness D(A) — not exotic curvature.
#
# THE ONE KERNEL (F1, settled — REUSED, not minted):
#   S(A) = (1 − A²)^{1/2}  is the SINGLE Op14 kernel
#   (graded_vacuum_network.saturation_kernel, exponent=0.5). The clock/shear speed
#   c_shear = c₀·√S = c₀·(1 − A²)^{1/4} is a DERIVED projection (√S of the kernel),
#   NOT a second kernel; (1 − A²)^{1/4} is never used AS the kernel.
#
# PER-CHANNEL SIGN (INVARIANT-S2 sign-lock — NEVER a uniform C·S):
#   BULK    STIFFENS:  D = 1/S(A)  (stiffness_profile) → c_eff² = c₀²/S → ∞ at A=1
#                      (goes rigid, halts the collapse — the elliptic coefficient
#                       diverges and the source can no longer push ε₁₁ past unity).
#   SHEAR   SOFTENS:   c_shear = c₀·√S → 0 at A=1   (shear_wave_speed() above —
#                      the constitutive modulus melts; the GW reflector).
#   EM      MATCHED:   Z_EM = Z₀, Γ_EM = 0  (refractive_index() UNCHANGED — spectator).
#
# HONESTY (do NOT overclaim — read interior-singularity-resolution.md /
# lattice-extreme-bh-rationality.md): the point singularity is REPLACED by a
# strain-saturated SHELL at r_sat = 3.5·r_s; the inertial density ρ_eff = ρ₀/S³
# STILL DIVERGES there (ρ_eff → ∞ as S → 0). True removal needs the
# yield→rupture→genesis physics (a separate frontier). The strain-cap here is a
# numerical clip (A capped at 1), NOT modeled yield-physics. This is RELOCATION
# of the singularity to a shell, not regularization / removal of the infinity.
# ═══════════════════════════════════════════════════════════════════════════════


def saturated_radial_strain(
    r: float | np.ndarray, r_s: float, *, S_min: float = 1e-3
) -> float | np.ndarray:
    r"""
    Radial (ε₁₁) strain under the SATURATING-MODULUS correction (Stage-1).

    On the RADIAL / shear ε₁₁ channel ONLY (EM spectator: ``refractive_index()``
    is untouched). The linear core gives ε₁₁ = r_sat/r (= 7GM/c²r); the saturating
    modulus caps the strain at the yield A = ε₁₁/ε_yield = 1 (ε_yield ≡ 1), so the
    saturated strain is the CLOSED-FORM CAP of the linear profile:

    .. math::
        \varepsilon_{11}^{\,sat}(r) = \min\!\Big(\tfrac{r_{sat}}{r},\, 1\Big)

    This is identical to :func:`radial_strain` (the linear profile already clips at
    unity in the exterior); the DISTINCT physics is in the per-channel MODULUS the
    cap induces — exposed by :func:`bulk_stiffness_D` (D = 1/S → ∞, BULK stiffens)
    and :func:`shear_wave_speed` (c_shear = c₀√S → 0, SHEAR softens). The finite-core
    relaxation :func:`relax_finite_core_strain` solves the full elliptic
    −∇·[D·∇ε₁₁] = T₀₀ on the native stencil and recovers this cap self-consistently.

    Recover-the-known: at r ≫ r_sat, A → 0, S → 1, D → 1 ⇒ ε₁₁ → r_sat/r (the linear
    elastic-Poisson / Schwarzschild limit). Activate-at-extreme: ε₁₁ → 1 at r_sat.

    The kernel S(A) is the canonical one — :func:`saturation_kernel` (exponent=0.5,
    clipped to [S_min, 1]). The yield-shell location is S_min-INDEPENDENT (the cap
    sits at A = 1 where the LINEAR profile reaches unity, set by r_sat, not by the
    clamp); :func:`relax_finite_core_strain` carries the explicit clip-independence
    gate.

    Args:
        r: Radial distance [m].
        r_s: Schwarzschild radius [m].
        S_min: Numerical floor on the kernel (clip guard); the cap location does
            NOT depend on it (load-bearing gate — see ``relax_finite_core_strain``).

    Returns:
        Saturated radial strain ε₁₁ ∈ [0, 1].
    """
    from ave.solvers.graded_vacuum_network import saturation_kernel

    r = np.asarray(r, dtype=float)
    r_sat = saturation_radius(r_s)
    eps_lin = r_sat / r  # inherited linear core ε₁₁ = 7GM/c²r = r_sat/r
    # A = ε₁₁/ε_yield with ε_yield = 1. The canonical kernel S(A) defines the
    # saturated cap: S(A) → 0 marks A = 1. We return the strain capped at the
    # yield (the closed-form static solution of the saturating-modulus operator
    # in the source-free exterior); the kernel call below is the SAME canonical
    # S(A) used for the modulus, asserting the cap location is kernel-consistent.
    A_lin = np.minimum(eps_lin, 1.0)
    _ = saturation_kernel(A_lin, exponent=0.5, S_min=S_min)  # canonical kernel reuse
    return A_lin


def bulk_stiffness_D(
    A: float | np.ndarray, *, S_min: float = 1e-3
) -> float | np.ndarray:
    r"""
    BULK elliptic stiffness coefficient D(A) = 1/S(A) (the channel that STIFFENS).

    .. math::
        D(A) = \frac{1}{S(A)} = \frac{1}{(1 - A^2)^{1/2}}
        \quad\xrightarrow{A \to 1}\quad \infty

    This is the per-site dimensionless stiffness c_eff²/c₀² = 1/S in the
    divergence-form operator −∇·[(c⁴/7G)·D·∇ε₁₁] = T₀₀. As A → 1 the coefficient
    diverges: the medium goes rigid, the source can no longer push ε₁₁ past unity,
    and the collapse halts (the yield shell). REUSES the canonical
    :func:`stiffness_profile` (exponent=0.5) — NO new kernel is minted.

    Per-channel sign-lock (INVARIANT-S2): BULK D = 1/S (stiffen), NOT a uniform
    C·S. The SHEAR channel softens via the DERIVED √S projection
    (:func:`shear_wave_speed`); the two signs are physically distinct.

    Args:
        A: Local strain ratio ε₁₁/ε_yield ∈ [0, 1].
        S_min: Kernel floor (clip guard); caps D at 1/S_min for numerical stability.

    Returns:
        Bulk stiffness D ∈ [1, 1/S_min].
    """
    from ave.solvers.graded_vacuum_network import stiffness_profile

    A = np.asarray(A, dtype=float)
    return stiffness_profile(A, exponent=0.5, S_min=S_min)


# ═══════════════════════════════════════════════════════════════
# GW strain and propagation properties
# ═══════════════════════════════════════════════════════════════


def gw_strain_to_voltage(h: float, freq_hz: float = 100.0) -> float:
    r"""
    Convert GW strain to equivalent voltage across one lattice cell.

    .. math::
        V_{GW} = h \cdot c \cdot \ell_{node} \cdot 2\pi f

    Args:
        h: Gravitational wave strain amplitude (dimensionless).
        freq_hz: GW frequency [Hz] (default 100 Hz for LIGO band).

    Returns:
        Equivalent voltage per lattice cell [V].
    """
    return h * C_0 * L_NODE * 2 * np.pi * freq_hz


def is_linear_propagation(h: float, freq_hz: float = 100.0) -> bool:
    r"""
    Check whether a GW propagates in the linear regime.

    Linear propagation requires V_GW << V_SNAP (no saturation).
    For LIGO-detected GW (h ~ 10⁻²¹), V_GW / V_SNAP ~ 10⁻¹⁹.

    Args:
        h: Strain amplitude.
        freq_hz: Frequency [Hz].

    Returns:
        True if propagation is linear (no saturation losses).
    """
    V_gw = gw_strain_to_voltage(h, freq_hz)
    return float(V_gw / V_SNAP) < 0.01


def gw_local_speed(r: float, r_s: float) -> float:
    r"""
    Local GW propagation speed in a Schwarzschild field.

    Under Symmetric Gravity, the local speed of light is reduced:

    .. math::
        c_{local}(r) = c_0 / n(r) = c_0 \cdot (1 - r_s/r)

    Near the horizon, c_local → 0 (light effectively stops).
    Far from mass, c_local → c₀.

    Returns:
        Local wave speed [m/s].
    """
    n = refractive_index(r, r_s)
    return float(C_0 / n)


# ═══════════════════════════════════════════════════════════════
# Summary dataclass
# ═══════════════════════════════════════════════════════════════


def gw_propagation_summary(
    M_solar: float = 30.0, h: float = 1e-21, r_multiples: list[float] | None = None
) -> dict[str, float | bool | list[dict[str, float]]]:
    """
    Generate a summary of GW propagation properties.

    Args:
        M_solar: Source mass [solar masses].
        h: GW strain amplitude.
        r_multiples: List of r/r_s ratios to evaluate.

    Returns:
        Dict with all computed properties.
    """
    M = M_solar * M_SUN
    r_s = schwarzschild_radius(M)

    if r_multiples is None:
        r_multiples = [1.01, 1.1, 2, 5, 10, 100, 1000]

    results = {
        "M_kg": M,
        "r_s_m": r_s,
        "r_sat_m": saturation_radius(r_s),
        "linear_propagation": is_linear_propagation(h),
        "V_gw_over_V_snap": gw_strain_to_voltage(h) / V_SNAP,
        "profiles": [],
    }

    for mult in r_multiples:
        r = mult * r_s
        results["profiles"].append(
            {
                "r_over_rs": mult,
                "r_m": r,
                "n_refract": float(refractive_index(r, r_s)),
                "epsilon_eff": float(epsilon_eff_schwarzschild(r, r_s)),
                "mu_eff": float(mu_eff_schwarzschild(r, r_s)),
                # EM channel: Z_EM ≡ Z₀, Γ_EM = 0 (light transparent).
                "Z_em_ohm": float(gravitational_impedance(r, r_s)),
                "gamma_em": float(horizon_reflection(r, r_s)),
                # Shear/GW channel: Z_shear → 0, Γ_shear → −1 (GW reflect).
                "Z_shear": float(shear_impedance(r, r_s)),
                "gamma_shear": float(shear_horizon_reflection(r, r_s)),
                "c_shear": float(shear_wave_speed(r, r_s)),
                "c_local": gw_local_speed(r, r_s),
            }
        )

    return results
