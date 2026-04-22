"""
Regime Map: Universal Classification of Operating Regimes
==========================================================

Every physical domain in AVE reduces to a single dimensionless control
parameter r = A/Ac, where A is the local amplitude and Ac is the critical
(yield) threshold. The saturation operator S(r) = √(1-r²) changes
character at well-defined boundaries, defining 4 universal regimes.

The regime boundaries are DERIVED FROM FIRST PRINCIPLES:

    Regime I   LINEAR        r < √(2α)     Small-signal linearization
    Regime II  NONLINEAR     √(2α) ≤ r < √3/2  Large-signal operation
    Regime III YIELD         √3/2 ≤ r < 1  Avalanche / phase transition
    Regime IV  RUPTURED      r ≥ 1.0       Breakdown / topology destroyed

Boundary derivations:
    I→II:  r₁ = √(2α) ≈ 0.1208.
           The perturbative correction ΔS = r²/2 equals α (the lattice
           self-coupling constant) at this point. Below r₁, Axiom 4
           corrections are sub-α: smaller than the lattice's own
           coupling strength and therefore physically unresolvable.

    II→III: r₂ = √3/2 ≈ 0.8660.
            At this point Q(r) = 1/S(r) = 2, the minimum non-trivial
            quality factor (ℓ_min = 2, the lowest radiating multipole).
            The system traps more energy per cycle than it radiates.
            EE: onset of avalanche multiplication (Miller M ≥ 2).

    III→IV: r₃ = 1.0 (exact).
            Axiomatic: S(1) = 0. Topology destroyed.
            EE: junction breakdown, M → ∞.

This maps exactly to semiconductor device analysis:
    Regime I   = Small-Signal (DC bias, linearised g_m / r_π)
    Regime II  = Large-Signal (switching, saturation onset)
    Regime III = Avalanche (Miller multiplication, Q ≥ 2)
    Regime IV  = Breakdown (V_R = V_BR, device destroyed)

The regime classification is the PREREQUISITE GATE: no domain
analysis should proceed without first identifying its regime.
"""

from dataclasses import dataclass

import numpy as np

from ave.core.constants import ALPHA, B_SNAP, C_0, H_INFINITY, L_NODE, V_YIELD

# ══════════════════════════════════════════════════════════════════════════════
# Regime Boundaries — DERIVED FROM FIRST PRINCIPLES
# ══════════════════════════════════════════════════════════════════════════════
#
# I→II:  r₁ = √(2α)
#        The perturbative correction ΔS ≈ r²/2 equals α at this point.
#        Below r₁, nonlinear corrections are sub-α (unresolvable).
#        EE: small-signal linearization boundary.
#
# II→III: r₂ = √(3)/2
#         Q(r) = 1/S(r) reaches ℓ_min = 2 (lowest radiating multipole).
#         At Q ≥ 2, energy trapping exceeds radiation per cycle.
#         EE: onset of avalanche multiplication (Miller M = 2).
#
# III→IV: r₃ = 1.0 (Axiom 4)
#         S(1) = 0. Topology destroyed.
#         EE: junction breakdown, M → ∞.
#
R_LINEAR_MAX: float = np.sqrt(2.0 * ALPHA)  # √(2α) ≈ 0.1208
R_NONLINEAR_MAX: float = np.sqrt(3.0) / 2.0  # √3/2 ≈ 0.8660
R_YIELD_MAX: float = 1.0  # Axiom 4 (exact)

# Regime IDs
REGIME_LINEAR = 1
REGIME_NONLINEAR = 2
REGIME_YIELD = 3
REGIME_RUPTURED = 4

REGIME_NAMES = {
    REGIME_LINEAR: "I (LINEAR / Small-Signal)",
    REGIME_NONLINEAR: "II (NONLINEAR / Large-Signal)",
    REGIME_YIELD: "III (YIELD / Avalanche)",
    REGIME_RUPTURED: "IV (RUPTURED / Breakdown)",
}

REGIME_DESCRIPTIONS = {
    REGIME_LINEAR: "Small-signal: Axiom 4 corrections sub-α (ΔS < α ≈ 1/137)",
    REGIME_NONLINEAR: "Large-signal: full S(r) = √(1-r²) required",
    REGIME_YIELD: "Avalanche: Q ≥ 2, energy trapping exceeds radiation loss",
    REGIME_RUPTURED: "Breakdown: topology destroyed, S = 0, M → ∞",
}

# ══════════════════════════════════════════════════════════════════════════════
# Transition Boundaries — BETWEEN regimes
# ══════════════════════════════════════════════════════════════════════════════
#
# Physical objects near a regime boundary experience TRANSITIONAL physics:
# the simplified equations of neither regime fully apply.  The transition
# zone width is ±10% of the boundary value (the ≈ α fractional resolution
# of the lattice's own self-coupling).
#
# I↔II:   r₁ = √(2α) ≈ 0.1208  → transition zone [0.1087, 0.1329]
# II↔III: r₂ = √3/2  ≈ 0.8660  → transition zone [0.7794, 0.9526]
# III↔IV: r₃ = 1.0              → transition zone [0.9000, 1.0000]
#
# EE analog: the transition zones map to the "knee" of device curves —
# the region where simple models (small-signal, saturated) break down
# and full nonlinear SPICE simulation is required.

_BOUNDARY_TOLERANCE = 0.10  # 10% fractional width

TRANSITION_NAMES = {
    (REGIME_LINEAR, REGIME_NONLINEAR): "I↔II (Linear ↔ Nonlinear onset)",
    (REGIME_NONLINEAR, REGIME_YIELD): "II↔III (Nonlinear ↔ Yield onset)",
    (REGIME_YIELD, REGIME_RUPTURED): "III↔IV (Yield ↔ Rupture onset)",
}

TRANSITION_DESCRIPTIONS = {
    (REGIME_LINEAR, REGIME_NONLINEAR): (
        "Transition: ΔS ~ α. Perturbative and full S(r) both marginally valid. "
        "EE: biasing near V_BE — device entering active region."
    ),
    (REGIME_NONLINEAR, REGIME_YIELD): (
        "Transition: Q → 2. Energy trapping rising, avalanche onset. "
        "EE: approaching breakdown knee — Miller multiplication rising."
    ),
    (REGIME_YIELD, REGIME_RUPTURED): (
        "Transition: S → 0. Topology on verge of rupture. "
        "EE: Zener/avalanche knee — device at absolute maximum rating."
    ),
}


@dataclass
class RegimeInfo:
    """Result of regime classification."""

    regime: int
    name: str
    description: str
    r: float  # dimensionless ratio A/Ac
    S: float  # saturation factor
    A: float  # physical amplitude
    Ac: float  # critical threshold
    domain: str | None = None
    A_units: str | None = None
    Ac_units: str | None = None
    near_boundary: bool = False
    boundary_name: str | None = None
    boundary_description: str | None = None

    def __repr__(self) -> str:
        bnd = f", boundary='{self.boundary_name}'" if self.near_boundary else ""
        return (
            f"RegimeInfo(regime={self.name}, r={self.r:.6f}, " f"S={self.S:.6f}, A={self.A:.4e}, Ac={self.Ac:.4e}{bnd})"
        )

    def summary(self) -> str:
        """Human-readable summary for diagnostic printing."""
        lines = [
            "  ── REGIME CLASSIFICATION ──",
            f"  Domain:    {self.domain or 'unspecified'}",
            f"  Amplitude: A = {self.A:.4e}" + (f" {self.A_units}" if self.A_units else ""),
            f"  Threshold: Ac = {self.Ac:.4e}" + (f" {self.Ac_units}" if self.Ac_units else ""),
            f"  Ratio:     r = A/Ac = {self.r:.6f}",
            f"  Saturation: S(r) = {self.S:.6f}",
            f"  ▶ Regime:  {self.name}",
            f"  ▶ Physics: {self.description}",
        ]
        if self.near_boundary:
            lines.append(f"  ⚡ TRANSITION: {self.boundary_name}")
            lines.append(f"     {self.boundary_description}")
        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# Core Classification
# ══════════════════════════════════════════════════════════════════════════════


def classify_regime(
    A: float,
    Ac: float,
    domain: str | None = None,
    A_units: str | None = None,
    Ac_units: str | None = None,
) -> RegimeInfo:
    """
    Classify the operating regime from amplitude and critical threshold.

    Parameters
    ----------
    A : float
        Local amplitude (V, E, ε₁₁, T, B, h, etc.)
    Ac : float
        Critical threshold (V_yield, E_yield, 1.0, T_c, B_snap, etc.)
    domain : str, optional
        Domain name for diagnostic output.
    A_units, Ac_units : str, optional
        Physical units for diagnostic output.

    Returns
    -------
    RegimeInfo
        Complete regime classification with diagnostics.
    """
    r = abs(float(A)) / abs(float(Ac))
    S = np.sqrt(max(0.0, 1.0 - min(r, 1.0) ** 2))

    if r < R_LINEAR_MAX:
        regime = REGIME_LINEAR
    elif r < R_NONLINEAR_MAX:
        regime = REGIME_NONLINEAR
    elif r < R_YIELD_MAX:
        regime = REGIME_YIELD
    else:
        regime = REGIME_RUPTURED

    # Detect transition boundaries (within ±10% of any boundary)
    near_boundary = False
    boundary_name = None
    boundary_desc = None

    boundaries = [
        (R_LINEAR_MAX, (REGIME_LINEAR, REGIME_NONLINEAR)),
        (R_NONLINEAR_MAX, (REGIME_NONLINEAR, REGIME_YIELD)),
        (R_YIELD_MAX, (REGIME_YIELD, REGIME_RUPTURED)),
    ]
    for r_bnd, regime_pair in boundaries:
        if abs(r - r_bnd) / r_bnd < _BOUNDARY_TOLERANCE:
            near_boundary = True
            boundary_name = TRANSITION_NAMES[regime_pair]
            boundary_desc = TRANSITION_DESCRIPTIONS[regime_pair]
            break

    return RegimeInfo(
        regime=regime,
        name=REGIME_NAMES[regime],
        description=REGIME_DESCRIPTIONS[regime],
        r=r,
        S=S,
        A=float(A),
        Ac=float(Ac),
        domain=domain,
        A_units=A_units,
        Ac_units=Ac_units,
        near_boundary=near_boundary,
        boundary_name=boundary_name,
        boundary_description=boundary_desc,
    )


# ══════════════════════════════════════════════════════════════════════════════
# Domain-Specific Control Parameters
# ══════════════════════════════════════════════════════════════════════════════


def em_voltage_regime(V_local: float) -> RegimeInfo:
    """
    EM (dielectric) regime: r = V / V_yield.

    V_yield = √α × V_snap ≈ 43.65 kV is the kinetic onset of nonlinearity.
    Lab fields are typically deep in Regime I (r ~ 10⁻⁶ to 10⁻³).
    PONDER-05 at 30 kV operates at r = 0.687 (Regime II).
    """
    return classify_regime(
        V_local,
        float(V_YIELD),
        domain="EM (dielectric)",
        A_units="V",
        Ac_units="V",
    )


def em_field_regime(E_local: float) -> RegimeInfo:
    """
    EM (field strength) regime: r = E / E_yield.

    E_yield = V_yield / ℓ_node ≈ 1.13 × 10¹⁷ V/m.
    Lab fields (E ~ 10⁶ V/m) are in Regime I (r ~ 10⁻¹¹).
    """
    E_yield = float(V_YIELD) / float(L_NODE)  # ≈ 1.13 × 10¹⁷ V/m
    return classify_regime(
        E_local,
        E_yield,
        domain="EM (field)",
        A_units="V/m",
        Ac_units="V/m",
    )


def gravity_regime(M_kg: float, r_meters: float) -> RegimeInfo:
    """
    Gravitational regime: r = ε₁₁ = 7GM/(c²r).

    The principal radial strain of the lattice under Schwarzschild geometry.
    Solar surface: ε₁₁ ≈ 10⁻⁵ (Regime I).
    Neutron star: ε₁₁ ≈ 0.3 (Regime II).
    Black hole at r_s: ε₁₁ → 1 (Regime III/IV boundary).
    """
    from ave.core.constants import G

    epsilon_11 = 7.0 * G * M_kg / (C_0**2 * r_meters)
    return classify_regime(
        epsilon_11,
        1.0,
        domain="Gravity",
        A_units="(strain)",
        Ac_units="(unitary)",
    )


def bcs_regime(T_kelvin: float, T_c_kelvin: float) -> RegimeInfo:
    """
    BCS/superconducting regime: r = T/Tc.

    B_c(T) = B_c0 × √(1-(T/Tc)²) — same saturation operator.
    Below Tc: superconducting (S > 0). At Tc: normal (S → 0).
    """
    return classify_regime(
        T_kelvin,
        T_c_kelvin,
        domain="BCS (superconductor)",
        A_units="K",
        Ac_units="K",
    )


def magnetic_regime(B_local: float) -> RegimeInfo:
    """
    Magnetic regime: r = B / B_snap.

    B_snap = m_e²c²/(eℏ) ≈ 1.89 × 10⁹ T.
    Lab magnets (B ~ 10 T): r ~ 10⁻⁸ (Regime I).
    Magnetar surface (B ~ 10¹⁰ T): r ~ 5 (Regime IV, ruptured).
    """
    return classify_regime(
        B_local,
        float(B_SNAP),
        domain="Magnetic",
        A_units="T",
        Ac_units="T",
    )


def nuclear_regime(r_separation: float, d_sat: float) -> RegimeInfo:
    """
    Nuclear regime: r = d_sat / r_separation.

    d_sat is the saturation radius (proton diameter, Slater radius, etc.)
    At r_separation = d_sat: r = 1 (Pauli wall, Regime IV boundary).
    """
    ratio = d_sat / r_separation if r_separation > 0 else float("inf")
    return classify_regime(
        ratio,
        1.0,
        domain="Nuclear",
        A_units="(d_sat/r)",
        Ac_units="(unitary)",
    )


def gw_regime(h_strain: float) -> RegimeInfo:
    """
    Gravitational wave regime: r = h / h_yield.

    h_yield = √α ≈ 0.0854 (yield strain of the lattice).
    LIGO detections: h ~ 10⁻²¹ (Regime I, r ~ 10⁻²⁰).
    """
    h_yield = np.sqrt(ALPHA)
    return classify_regime(
        h_strain,
        h_yield,
        domain="GW strain",
        A_units="(strain)",
        Ac_units="(strain)",
    )


def protein_regime(d_bond: float, d_eq: float) -> RegimeInfo:
    """
    Protein backbone regime: r = |d - d_eq| / d_eq.

    d_eq is the equilibrium bond distance (e.g., 3.8 Å for Cα-Cα).
    Typical backbone fluctuations: r ~ 0.05 (Regime I).
    Unfolded: r ~ 0.3 (Regime II, nonlinear).
    """
    dr = abs(d_bond - d_eq)
    return classify_regime(
        dr,
        d_eq,
        domain="Protein backbone",
        A_units="Å",
        Ac_units="Å",
    )


def galactic_regime(g_newtonian: float, a_0: float | None = None) -> RegimeInfo:
    """
    Galactic regime: r = g_N / a₀.

    a₀ = cH∞/(2π) ≈ 1.07 × 10⁻¹⁰ m/s² (DERIVED, not empirical).
    H∞ = 28πm_e³cG/(ℏ²α²) is the asymptotic Hubble parameter.

    The saturation operator acts on LATTICE MUTUAL INDUCTANCE η:
        η_eff = η₀ × S(g_N/a₀)

    This is the SAME universal operator as every other domain:
        S(r→1) = medium compliance → 0.

    What differs is the OBSERVATIONAL CONSEQUENCE:
        EM:      ε→0 = pair production (dramatic)
        Gravity: G_shear→0 = event horizon (dramatic)
        Galaxy:  η→0 = drag vanishes → Newtonian (boring!)

    The galactic rotation curve problem IS the regime boundary
    transition. At r = g_N/a₀ ≈ 1 (Regime III→IV), the lattice
    drag switches off. "Dark matter" is the drag that exists
    on the Regime I–III side of this phase transition.

    Regime locations:
        Inner galaxy (g_N >> a₀): r >> 1 → Regime IV (Newtonian, no drag)
        Transition (g_N ≈ a₀): r ≈ 1 → Regime III (curve flattening)
        Outer galaxy (g_N << a₀): r << 1 → Regime I (deep MOND, full drag)
    """
    if a_0 is None:
        # Derived: a₀ = cH∞/(2π)
        a_0 = float(C_0) * float(H_INFINITY) / (2 * np.pi)
    return classify_regime(
        g_newtonian,
        a_0,
        domain="Galactic rotation",
        A_units="m/s²",
        Ac_units="m/s²",
    )


# ══════════════════════════════════════════════════════════════════════════════
# Regime-Specific Equation Forms
# ══════════════════════════════════════════════════════════════════════════════


def regime_equations(regime_id: int) -> dict[str, tuple[str, str]]:
    """
    Return the simplified equation forms valid in each regime.

    Returns a dict of {quantity: (formula_str, approximation_note)}.
    """
    if regime_id == REGIME_LINEAR:
        return {
            "ε_eff": ("ε₀", "S ≈ 1, standard Maxwell"),
            "μ_eff": ("μ₀", "S ≈ 1, standard Maxwell"),
            "c_eff": ("c₀", "No wave speed modification"),
            "Z_eff": ("Z₀", "Impedance invariant"),
            "S(r)": ("1 - r²/2 + O(r⁴)", "Perturbative expansion valid"),
        }
    elif regime_id == REGIME_NONLINEAR:
        return {
            "ε_eff": ("ε₀ × √(1 - r²)", "Full operator required"),
            "μ_eff": ("μ₀ × √(1 - r²)", "Full operator required"),
            "c_eff": ("c₀ × (1 - r²)^(1/4)", "Measurable slowdown"),
            "Z_eff": ("Z₀ / (1 - r²)^(1/4)", "Impedance rises"),
            "S(r)": ("√(1 - r²)", "No simplification"),
        }
    elif regime_id == REGIME_YIELD:
        return {
            "ε_eff": ("→ 0", "Compliance destroyed"),
            "μ_eff": ("→ 0", "Inductance shorts"),
            "c_eff": ("→ 0", "Wave packet freezes"),
            "Z_eff": ("→ ∞ or 0", "Depends on symmetric/asymmetric saturation"),
            "S(r)": ("→ 0", "Phase transition imminent"),
        }
    elif regime_id == REGIME_RUPTURED:
        return {
            "ε_eff": ("0", "Topology destroyed"),
            "μ_eff": ("0", "Topology destroyed"),
            "c_eff": ("0", "No propagation inside ruptured zone"),
            "Z_eff": ("undefined", "New physics: deconfinement, event horizon"),
            "S(r)": ("0", "Fully ruptured"),
        }
    else:
        raise ValueError(f"Unknown regime: {regime_id}")


# ══════════════════════════════════════════════════════════════════════════════
# Comprehensive Summary
# ══════════════════════════════════════════════════════════════════════════════


def print_regime_map() -> None:
    """Print the full regime map with all domain examples."""
    print("=" * 78)
    print("  UNIVERSAL REGIME MAP (Derived Boundaries)")
    print("  S(r) = √(1 - r²),  r = A/Ac")
    print(f"  r₁ = √(2α) = {R_LINEAR_MAX:.4f}   (small-signal limit)")
    print(f"  r₂ = √3/2  = {R_NONLINEAR_MAX:.4f}   (Q = ℓ_min = 2)")
    print("  r₃ = 1.0000          (Axiom 4)")
    print("=" * 78)

    S_at_r1 = np.sqrt(1 - R_LINEAR_MAX**2)
    S_at_r2 = np.sqrt(1 - R_NONLINEAR_MAX**2)

    print(f"\n  {'Regime':<24} {'r range':<20} {'S range':<20} {'EE Analog'}")
    print(f"  {'─'*80}")
    print(f"  {'I   LINEAR':<24} {'r < √(2α)':<20} {'S > ' + f'{S_at_r1:.4f}':<20} Small-Signal")
    print(f"  {'II  NONLINEAR':<24} {'√(2α) ≤ r < √3/2':<20} {f'{S_at_r2:.4f} < S':<20} Large-Signal")
    print(f"  {'III YIELD':<24} {'√3/2 ≤ r < 1':<20} {'S < 0.500':<20} Avalanche (M ≥ 2)")
    print(f"  {'IV  RUPTURED':<24} {'r ≥ 1.0':<20} {'S = 0':<20} Breakdown (M → ∞)")

    print("\n  ── DOMAIN EXAMPLES ──")

    examples = [
        (
            "EM (dielectric)",
            [
                ("Lab 1kV/m capacitor", 1e3, float(V_YIELD), "V"),
                ("PONDER-05 @ 30kV", 30e3, float(V_YIELD), "V"),
                ("PONDER-05 @ 43kV", 43e3, float(V_YIELD), "V"),
            ],
        ),
        (
            "Gravity",
            [
                ("Solar surface", 2.12e-6, 1.0, "strain"),
                ("White dwarf", 3.0e-4, 1.0, "strain"),
                ("Neutron star", 0.3, 1.0, "strain"),
                ("BH at r_s", 1.0, 1.0, "strain"),
            ],
        ),
        (
            "Magnetic",
            [
                ("MRI scanner (3T)", 3.0, float(B_SNAP), "T"),
                ("LHC dipole (8T)", 8.0, float(B_SNAP), "T"),
                ("Magnetar (10¹⁰ T)", 1e10, float(B_SNAP), "T"),
            ],
        ),
        (
            "GW strain",
            [
                ("LIGO detection", 1e-21, np.sqrt(ALPHA), "h"),
                ("NS merger surface", 0.01, np.sqrt(ALPHA), "h"),
            ],
        ),
    ]

    for domain, items in examples:
        print(f"\n  {domain}:")
        for name, A, Ac, units in items:
            info = classify_regime(A, Ac)
            print(f"    {name:<28s} r = {info.r:.2e}  S = {info.S:.6f}  → {info.name}")

    print(f"\n  {'='*72}")


# ══════════════════════════════════════════════════════════════════════════════
# identify_regime() — Convenience Startup Function
# ══════════════════════════════════════════════════════════════════════════════

_DOMAIN_DISPATCH = {
    "em_voltage": lambda kw: em_voltage_regime(kw["V_local"]),
    "em_field": lambda kw: em_field_regime(kw["E_local"]),
    "gravity": lambda kw: gravity_regime(kw["M_kg"], kw["r_meters"]),
    "bcs": lambda kw: bcs_regime(kw["T_kelvin"], kw["T_c_kelvin"]),
    "magnetic": lambda kw: magnetic_regime(kw["B_local"]),
    "nuclear": lambda kw: nuclear_regime(kw["r_separation"], kw["d_sat"]),
    "gw": lambda kw: gw_regime(kw["h_strain"]),
    "protein": lambda kw: protein_regime(kw["d_bond"], kw["d_eq"]),
    "galactic": lambda kw: galactic_regime(kw["g_newtonian"]),
    "generic": lambda kw: classify_regime(
        kw["A"],
        kw["Ac"],
        domain=kw.get("domain"),
        A_units=kw.get("A_units"),
        Ac_units=kw.get("Ac_units"),
    ),
}


def identify_regime(domain: str, verbose: bool = True, **kwargs) -> RegimeInfo:
    """
    Identify and print the operating regime at script startup.

    This is the PREREQUISITE GATE: every physics script should call this
    before proceeding with domain-specific analysis.

    Parameters
    ----------
    domain : str
        One of: 'em_voltage', 'em_field', 'gravity', 'bcs', 'magnetic',
        'nuclear', 'gw', 'protein', 'galactic', 'generic'.
    verbose : bool
        If True (default), print the regime summary to stdout.
    **kwargs
        Domain-specific parameters. See each domain classifier for details.
        Examples:
            identify_regime('em_voltage', V_local=30e3)
            identify_regime('gravity', M_kg=1.989e30, r_meters=6.96e8)
            identify_regime('gw', h_strain=1e-21)
            identify_regime('generic', A=0.5, Ac=1.0, domain='custom')

    Returns
    -------
    RegimeInfo
        Complete regime classification with transition boundary awareness.
    """
    if domain not in _DOMAIN_DISPATCH:
        valid = ", ".join(sorted(_DOMAIN_DISPATCH.keys()))
        raise ValueError(f"Unknown domain '{domain}'. Valid: {valid}")

    info = _DOMAIN_DISPATCH[domain](kwargs)

    if verbose:
        print(info.summary())

    return info


if __name__ == "__main__":
    print_regime_map()
