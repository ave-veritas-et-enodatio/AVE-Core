"""
Entanglement Thread: Topological Phase Winding on the K₄ Graph
==============================================================

When an entangled pair (e⁻e⁺) is synthesised from a single lattice
deformation, a quantised phase winding (Δφ = 2π) persists along the
path connecting the two defects on the K₄ graph.  This winding forms
a LOSSLESS short-short resonator (Γ = −1 at both particle cores)
whose standing wave mode is the physical hardware of entanglement.

The mechanism is structurally identical to the Meissner effect:
both are instances of Kuramoto phase-locking on the LC lattice.

    Superconductor (Vol 3, Ch 9)     Entanglement Thread
    ────────────────────────────     ────────────────────
    N electrons in wire              N LC nodes along thread
    Kuramoto below Tc                Winding constraint Δφ = 2π
    Rigid gear train                 Rigid phase winding
    Applied B-field → resisted       Measurement → constrains partner
    Same operator: S(T/Tc)           Same operator: S(ε/α)

Axiom compliance:
    Axiom 1 — LC network, connected graph, lossless (no R)
    Axiom 3 — Born rule from Ohmic extraction (Joule heating)
    Axiom 4 — Saturation gives Γ = -1 boundaries, binary outcomes,
              and topological protection (pair creation threshold)

No external quantum postulates are used.
"""

import numpy as np

from ave.core.constants import C_0, HBAR, K_B, L_NODE, M_E, e_charge

# ═══════════════════════════════════════════════════════════════
# Thread geometry
# ═══════════════════════════════════════════════════════════════


def thread_node_count(d: float) -> int:
    """Number of LC nodes along the thread.

    Args:
        d: Separation distance [m].

    Returns:
        N = d / ℓ_node (integer).
    """
    return max(1, int(round(d / L_NODE)))


def phase_advance_per_node(d: float) -> float:
    """Phase advance per node along the thread.

    The total winding is 2π; it is distributed uniformly over N nodes:
        δφ = 2π / N = 2π ℓ_node / d

    As d → ∞, δφ → 0: the thread becomes locally invisible.

    Args:
        d: Separation distance [m].

    Returns:
        Phase advance per node [rad].
    """
    return 2.0 * np.pi * L_NODE / d


# ═══════════════════════════════════════════════════════════════
# Standing wave mode
# ═══════════════════════════════════════════════════════════════


def thread_mode_frequency(d: float) -> float:
    """Fundamental mode frequency of the short-short resonator.

    f₁ = c / (2d)

    The thread is lossless (Q = ∞) with Γ = −1 at both ends.

    Args:
        d: Separation distance [m].

    Returns:
        Frequency [Hz].
    """
    return C_0 / (2.0 * d)


def thread_mode_energy(d: float) -> float:
    """Energy of the fundamental standing wave mode.

    E₁ = ℏ ω₁ = ℏ π c / d

    Anti-confining: E ∝ 1/d (opposite of QCD flux tube E ∝ d).
    The thread becomes energetically lighter as particles separate.

    Args:
        d: Separation distance [m].

    Returns:
        Mode energy [J].
    """
    return HBAR * np.pi * C_0 / d


def thread_mode_energy_eV(d: float) -> float:
    """Mode energy in electronvolts.

    Args:
        d: Separation distance [m].

    Returns:
        Mode energy [eV].
    """
    return thread_mode_energy(d) / e_charge


# ═══════════════════════════════════════════════════════════════
# Impedance taper profile
# ═══════════════════════════════════════════════════════════════


def impedance_taper_profile(
    d: float, n_points: int = 200, r_opt: float | None = None, n_profile: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    """Impedance profile Z(x)/Z₀ along the thread axis.

    Each particle is a saturated defect with a Faddeev-Skyrme radial
    strain profile.  The strain from each defect decays into the bulk.
    Along the thread axis, the total strain is the sum of both:

        ε(x) = |dφ_A/dr|(x) + |dφ_B/dr|(d-x)

    The impedance follows from Axiom 4:
        Z(x) = Z₀ · √(1 − (ε/ε_max)²)

    Args:
        d: Separation distance [m] (or in ℓ_node units if < 1000).
        n_points: Number of sample points along the axis.
        r_opt: Soliton confinement radius [ℓ_node]. Default: 8.32.
        n_profile: Power-law exponent of the phase profile. Default: 1.0.

    Returns:
        (x_array, Z_array): positions along axis and Z/Z₀ values.
    """
    if r_opt is None:
        # Engine-derived value: electron (c=3), kappa_FS/3 ≈ 8.32
        r_opt = 8.32

    # Work in ℓ_node units for the profile
    d_nodes = d / L_NODE if d > 1000 else d

    x = np.linspace(0, d_nodes, n_points)
    Z_profile = np.zeros(n_points)
    dr = 1e-6

    for i, xi in enumerate(x):
        # Strain from particle A at x=0
        if xi > dr:
            phi_A = np.pi / (1.0 + (xi / r_opt) ** n_profile)
            phi_A2 = np.pi / (1.0 + ((xi + dr) / r_opt) ** n_profile)
            dphi_A = abs((phi_A2 - phi_A) / dr)
        else:
            dphi_A = 0.0

        # Strain from particle B at x=d
        r_B = d_nodes - xi
        if r_B > dr:
            phi_B = np.pi / (1.0 + (r_B / r_opt) ** n_profile)
            phi_B2 = np.pi / (1.0 + ((r_B + dr) / r_opt) ** n_profile)
            dphi_B = abs((phi_B2 - phi_B) / dr)
        else:
            dphi_B = 0.0

        # Total strain (opposite twists → strains add)
        total_strain = dphi_A + dphi_B
        ratio = min(total_strain / np.pi, 0.9999)
        Z_profile[i] = np.sqrt(1.0 - ratio**2)

    return x, Z_profile


# ═══════════════════════════════════════════════════════════════
# Topological protection
# ═══════════════════════════════════════════════════════════════


def decoherence_probability(T: float) -> float:
    """Probability of spontaneous thread destruction via pair creation.

    To destroy the 2π winding, a new pair must spontaneously appear
    along the thread, requiring energy ≥ 2mₑc².  The Boltzmann
    probability is exponentially suppressed:

        P ∼ exp(−2mₑc² / k_BT)

    At 300 K: P ∼ exp(−3.95 × 10⁷) ≈ 0.

    Args:
        T: Temperature [K].

    Returns:
        Decoherence probability (dimensionless, ≈ 0 at physical T).
    """
    if T <= 0:
        return 0.0
    exponent = 2.0 * M_E * C_0**2 / (K_B * T)
    # Avoid overflow: if exponent > 700, result is indistinguishable from 0
    if exponent > 700:
        return 0.0
    return np.exp(-exponent)


# ═══════════════════════════════════════════════════════════════
# Bell angular correlation
# ═══════════════════════════════════════════════════════════════


def bell_correlation(theta: float | np.ndarray) -> float | np.ndarray:
    """Angular correlation function for entangled pair.

    E(â, b̂) = −cos(θ_ab)

    Derived from:
        1. Möbius half-angle (Axiom 1, K₄ chirality) → cos²(θ/2)
        2. Binary outcome (Axiom 4, two antinodes) → ±1
        3. Anti-correlation (winding conservation) → n̂_B = −â
        4. Ohmic Born rule (Axiom 3) → probability weighting

    Args:
        theta: Angle between detector axes [rad].

    Returns:
        Correlation E ∈ [−1, +1].
    """
    return -np.cos(theta)


def chsh_parameter(delta: float | np.ndarray) -> float | np.ndarray:
    """CHSH parameter S as a function of detector angle spacing δ.

    S(δ) = E(a,b) − E(a,b') + E(a',b) + E(a',b')

    With a=0, b=δ, a'=2δ, b'=3δ:
        S(δ) = −3cos(δ) + cos(3δ)

    Maximised at δ = π/4:  |S| = 2√2 ≈ 2.828 (Tsirelson bound).

    Args:
        delta: Angular spacing between consecutive detector axes [rad].

    Returns:
        CHSH parameter S (dimensionless).
    """
    return -3.0 * np.cos(delta) + np.cos(3.0 * delta)


def chsh_max() -> float:
    """Maximum CHSH violation (Tsirelson bound).

    Returns:
        |S|_max = 2√2 ≈ 2.828.
    """
    return abs(chsh_parameter(np.pi / 4.0))


def no_signaling_marginal(theta: float | np.ndarray) -> float | np.ndarray:
    """Bob's marginal probability regardless of Alice's setting.

    P(B=+) = ½ sin²(θ/2) + ½ cos²(θ/2) = ½

    This holds for ALL θ, confirming no-signaling: Alice cannot
    encode information in Bob's outcome statistics.

    Args:
        theta: Any angle [rad] (included for API completeness).

    Returns:
        0.5 (always).
    """
    return 0.5 * np.ones_like(np.asarray(theta, dtype=float))
