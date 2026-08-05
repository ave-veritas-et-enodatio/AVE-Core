"""
Solar System Impedance: Heliosphere, 'Oumuamua, and Orbital Resonances
=======================================================================

Models the solar system as a radial impedance profile extending from the
solar surface through the heliosphere to the interstellar medium.

Physical basis:
  The Sun drives a fast, hot plasma wind outward.  The solar wind creates
  a radially varying electron density n_e(r) and magnetic field B(r):

      n_e(r) ≈ n₀ · (r₀/r)²     [Parker spiral, continuity]
      B(r)   ≈ B₀ · (r₀/r)²     [radial component]
      T(r)   ≈ T₀ · (r₀/r)^(2/3) [adiabatic cooling]

  The impedance of the solar wind plasma is:
      Z_sw(r) = Z₀ / √(1 - (ω_p(r)/ω)²)

  At the heliopause (~120 AU), the solar wind rams into the interstellar
  medium (ISM) — a sharp impedance boundary analogous to the stellar
  tachocline.

Key predictions:
  1. 'Oumuamua's anomalous acceleration = radiation pressure coupling
     to the impedance gradient (no outgassing required)
  2. Solar Axiom-4 onset radius = the g_N = a₀ isocline (outer edge of the
     Newtonian region), under INTERNAL-FIELD keying.
     🔴 RETRACTED + RELABELED 2026-08-03. This bullet formerly read, verbatim:
     "Oort Cloud inner edge ≈ radius where g_N ≈ a₀ (saturation onset)".
     That is a *population* claim and it is retracted — the only bridge from
     a field isocline to a population edge was the Ax3-forbidden dissipative
     stall (04_continuum_electrodynamics.tex:272, MECHANISM-RETRACTED
     2026-07-19). What survives is a solar-FIELD radius, whose existence is
     itself gated by the unadjudicated internal-vs-total-field keying fork.
     See solar_axiom4_onset_summary() below for the full retraction record
     (that function was named oort_cloud_prediction() until 2026-08-03).
     🔴 DISSOLVED 2026-08-04: the T4 keying fork named above is RULED —
     the Axiom-4 kernel keys on the TOTAL LOCAL FIELD. Under that keying
     the Sun already sits at g_ext ≈ 1.8-2.0 a₀, so no saturation
     transition exists anywhere in the solar system and this is not a
     boundary at any radius. The formula is RETAINED as an internal-field
     COUNTERFACTUAL/diagnostic (the isocline of the solar monopole taken
     in isolation), not as a prediction. Nothing numeric changed.
  3. Kirkwood gaps = destructive interference in Jupiter's impedance cavity

References:
    - Parker (1958): Solar wind model
    - Micheli et al. (2018): 'Oumuamua non-gravitational acceleration
    - Bialy & Loeb (2018): Radiation pressure on thin body
"""

from dataclasses import dataclass

import numpy as np

from ave.axioms.scale_invariant import reflection_coefficient, saturation_factor
from ave.core.constants import C_0, EPSILON_0, M_E, M_SUN, Z_0, G, e_charge
from ave.regime_3_saturated.galactic_rotation import A0_LATTICE

# Alias for readability in formulas
E_CHARGE = e_charge


# ═══════════════════════════════════════════════════════════════
# Solar system constants
# ═══════════════════════════════════════════════════════════════

R_SUN = 6.957e8  # Solar radius [m]
AU = 1.496e11  # Astronomical unit [m]
KPC = 3.0857e19  # Kiloparsec [m]

# Solar wind at 1 AU (typical slow wind)
N_E_1AU = 5e6  # electrons/m³ at 1 AU
V_SW_1AU = 400e3  # Solar wind speed at 1 AU [m/s]
T_SW_1AU = 1e5  # Temperature at 1 AU [K]
B_SW_1AU = 5e-9  # Magnetic field at 1 AU [T]

# ISM properties
N_E_ISM = 0.1e6  # electrons/m³ in local ISM
T_ISM = 7000  # ISM temperature [K]

# Heliopause distance
R_HELIOPAUSE = 120 * AU  # ~120 AU (Voyager 1 crossed at ~121.6 AU)


# ═══════════════════════════════════════════════════════════════
# Heliospheric impedance profile
# ═══════════════════════════════════════════════════════════════


def solar_wind_density(r_m: float) -> float:
    """
    Solar wind electron density at distance r from Sun.

    n_e(r) = n₀ · (1 AU / r)² [continuity equation for radial flow]

    Args:
        r_m: Distance from Sun [m]. Must be > R_SUN.

    Returns:
        Electron density [m⁻³].
    """
    if r_m <= R_SUN:
        raise ValueError("r must be > R_SUN")
    return N_E_1AU * (AU / r_m) ** 2


def solar_wind_plasma_frequency(r_m: float) -> float:
    """
    Plasma frequency of the solar wind at distance r.

    ω_p(r) = √(n_e(r) · e² / (m_e · ε₀))

    Args:
        r_m: Distance from Sun [m].

    Returns:
        Plasma frequency [rad/s].
    """
    n_e = solar_wind_density(r_m)
    return np.sqrt(n_e * E_CHARGE**2 / (M_E * EPSILON_0))


def solar_wind_impedance(r_m: float, freq_hz: float = 1e6) -> float:
    """
    Impedance of the solar wind plasma at distance r.

    Z_sw(r) = Z₀ / √(1 - (f_p/f)²)

    Below the plasma frequency: Z is imaginary (evanescent).
    Above the plasma frequency: Z is real (propagating).

    Args:
        r_m: Distance from Sun [m].
        freq_hz: Observation frequency [Hz].

    Returns:
        Solar wind impedance [Ω]. Returns Z₀ if well above cutoff.
    """
    omega_p = solar_wind_plasma_frequency(r_m)
    omega = 2 * np.pi * freq_hz
    ratio2 = (omega_p / omega) ** 2
    if ratio2 >= 1.0:
        return 0.0  # Evanescent — total reflection
    return Z_0 / np.sqrt(1.0 - ratio2)


def heliospheric_impedance_profile(
    n_points: int = 500,
    r_min_au: float = 0.1,
    r_max_au: float = 300.0,
    freq_hz: float = 1e6,
) -> dict[str, np.ndarray | float]:
    """
    Build a full radial impedance profile from near-Sun to beyond heliopause.

    Returns:
        Dict with arrays: 'r_au', 'r_m', 'n_e', 'f_p', 'Z_sw',
        'g_solar', 'sigma_sat', 'Gamma_heliopause'.
    """
    r_au = np.logspace(np.log10(r_min_au), np.log10(r_max_au), n_points)
    r_m = r_au * AU

    n_e = np.array([solar_wind_density(r) for r in r_m])
    f_p = np.array([solar_wind_plasma_frequency(r) / (2 * np.pi) for r in r_m])
    Z_sw = np.array([solar_wind_impedance(r, freq_hz) for r in r_m])

    # Solar gravitational acceleration
    g_solar = G * M_SUN / r_m**2

    # Saturation factor (Axiom 4)
    sigma = np.array([saturation_factor(g, A0_LATTICE) if g > 0 else 1.0 for g in g_solar])

    # Heliopause reflection coefficient
    Z_heliopause = solar_wind_impedance(R_HELIOPAUSE, freq_hz)
    Z_ism = Z_0  # ISM is effectively vacuum at most frequencies
    Gamma_hp = float(reflection_coefficient(Z_heliopause, Z_ism))

    return {
        "r_au": r_au,
        "r_m": r_m,
        "n_e": n_e,
        "f_p_hz": f_p,
        "Z_sw": Z_sw,
        "g_solar": g_solar,
        "sigma_sat": sigma,
        "Gamma_heliopause": Gamma_hp,
    }


# ═══════════════════════════════════════════════════════════════
# 'Oumuamua anomalous acceleration
# ═══════════════════════════════════════════════════════════════


@dataclass
class InterstellarObject:
    """Properties of an interstellar object."""

    name: str
    mass_kg: float
    area_m2: float  # Cross-sectional area
    thickness_m: float  # Thickness (for radiation pressure)
    perihelion_au: float
    v_inf_km_s: float  # Velocity at infinity

    @property
    def area_to_mass(self) -> float:
        """Area-to-mass ratio [m²/kg]."""
        return self.area_m2 / self.mass_kg


# 'Oumuamua properties (Bialy & Loeb 2018 thin-body estimate)
# For radiation pressure to explain ~5×10⁻⁶ m/s², need A/m ≈ 1-1.5 m²/kg
# A thin disc/sheet: A~1.2×10⁵ m², thickness~0.5mm, density~2000 kg/m³
#   → mass ≈ A × thickness × density = 1.2e5 × 5e-4 × 2000 = 1.2×10⁵ kg
OUMUAMUA = InterstellarObject(
    name="1I/'Oumuamua",
    mass_kg=1.2e5,  # ~1.2×10⁵ kg (thin sheet, Bialy & Loeb)
    area_m2=1.2e5,  # ~120,000 m² (if pancake ~115m × ~111m)
    thickness_m=0.5e-3,  # ~0.5 mm (if light sail)
    perihelion_au=0.2553,
    v_inf_km_s=26.33,
)


def solar_radiation_pressure(r_m: float) -> float:
    """
    Solar radiation pressure at distance r.

    P_rad = L_sun / (4π r² c)

    Args:
        r_m: Distance from Sun [m].

    Returns:
        Radiation pressure [Pa].
    """
    L_SUN = 3.828e26  # Solar luminosity [W]
    return L_SUN / (4 * np.pi * r_m**2 * C_0)


def oumuamua_radiation_acceleration(r_m: float, obj: InterstellarObject = OUMUAMUA) -> float:
    """
    Non-gravitational acceleration from solar radiation pressure.

    a_rad = P_rad × A / m = (L_sun / (4π r² c)) × (A/m)

    For 'Oumuamua with A/m ≈ 1.2 m²/kg:
        a_rad(1 AU) ≈ 4.6×10⁻⁶ m/s²  (observed: ~5×10⁻⁶)

    Args:
        r_m: Distance from Sun [m].
        obj: Interstellar object properties.

    Returns:
        Radiation acceleration [m/s²].
    """
    P_rad = solar_radiation_pressure(r_m)
    return P_rad * obj.area_to_mass


def oumuamua_impedance_acceleration(r_m: float, obj: InterstellarObject = OUMUAMUA) -> float:
    """
    Total non-gravitational acceleration in the AVE framework.

    In AVE, the radiation pressure IS the impedance gradient force:
    the photon field exerts a ∇Z-mediated force on any object with
    a cross-section.  For a thin body:

        a_AVE = a_radiation × (1 + dZ/Z · dr/r)

    The correction is negligible for 'Oumuamua (Z varies by < 0.01%
    across its extent), confirming that the mainstream radiation
    pressure interpretation is the correct AVE interpretation.

    Args:
        r_m: Distance from Sun [m].
        obj: Interstellar object properties.

    Returns:
        Total non-gravitational acceleration [m/s²].
    """
    # Base radiation pressure acceleration
    a_rad = oumuamua_radiation_acceleration(r_m, obj)

    # Impedance gradient correction (solar wind Z variation across object)
    # dZ/dr at r: Z_sw ≈ Z₀(1 + ½(ωp/ω)²), so dZ/dr ≈ Z₀ ωp² / ω² × (1/r)
    # This correction is < 10⁻⁸ for 'Oumuamua's ~100m extent → negligible
    # The acceleration IS from radiation pressure (photon momentum transfer)
    return a_rad


def oumuamua_summary(obj: InterstellarObject = OUMUAMUA) -> dict[str, float | bool | str]:
    """
    Complete 'Oumuamua analysis at perihelion and 1 AU.

    Returns:
        Dict with key predictions vs observations.
    """
    r_peri = obj.perihelion_au * AU
    r_1au = AU

    a_peri = oumuamua_radiation_acceleration(r_peri, obj)
    a_1au = oumuamua_radiation_acceleration(r_1au, obj)

    # Observed (Micheli et al. 2018): a ∝ 1/r² with a(1AU) ≈ 5×10⁻⁶ m/s²
    a_obs_1au = 5.01e-6  # m/s²

    # Gravitational acceleration for comparison
    g_peri = G * M_SUN / r_peri**2
    g_1au = G * M_SUN / r_1au**2

    return {
        "name": obj.name,
        "area_to_mass_m2_kg": obj.area_to_mass,
        "a_rad_perihelion_m_s2": a_peri,
        "a_rad_1au_m_s2": a_1au,
        "a_obs_1au_m_s2": a_obs_1au,
        "ratio_predicted_observed": a_1au / a_obs_1au,
        "g_perihelion_m_s2": g_peri,
        "g_1au_m_s2": g_1au,
        "a_rad_over_g_at_1au": a_1au / g_1au,
        "scales_as_1_over_r2": True,  # Both P_rad and observation scale as 1/r²
    }


# ═══════════════════════════════════════════════════════════════
# Solar Axiom-4 onset radius (internal-field keying) — COUNTERFACTUAL as of
# 2026-08-04: the T4 keying fork is RULED total-local-field, so this block
# computes a diagnostic isocline, NOT a solar-system boundary. See
# saturation_radius_au() for the ruling record.
# 🔴 RELABELED 2026-08-03 (Oort containment retraction, Rule 12).
# This banner formerly read, verbatim: "Oort Cloud as impedance boundary".
# Same relabel as the section title, figure caption and the two functions
# below: what this block computes is a solar-FIELD radius, and the "Oort
# Cloud" identification was the retracted population claim.
# ═══════════════════════════════════════════════════════════════


def saturation_radius_au() -> float:
    """
    Radius where solar gravitational acceleration equals a₀ (MOND scale).

    The radius at which the Axiom-4 kernel turns on for the solar monopole
    under INTERNAL-FIELD keying — equivalently, the outer edge of the Sun's
    Newtonian region. This is a property of the solar FIELD and carries no
    claim about where any body sits (see solar_axiom4_onset_summary(): the
    Oort containment claim was retracted 2026-08-03).

    g(r) = GM/r² = a₀  →  r = √(GM/a₀)

    Value on canonical constants: 7438.9 AU, with a₀ = c·H_∞/2π =
    1.0719e-10 m/s² (galactic_rotation.py:56). Honest accuracy band: a₀ is
    itself 10.7% below the empirical MOND a₀ = 1.2e-10 (disclosed at
    manuscript/ave-kb/vol3/claim-quality.md:259), and r ∝ a₀^(-1/2), so the
    a₀-provenance band on this number is -5.5% (7030.7 AU on the empirical
    a₀). Pinned in src/tests/test_solar_impedance.py.

    🔴 THE BOUNDARY DISSOLVES — T4 RULED 2026-08-04 (total local field).
    The gate below fired. Under the ruled total-local-field keying the Sun
    already sits at g_ext ≈ 1.8-2.0 a₀ (2.1e-10/1.0719e-10 = 1.959 and
    2.1e-10/1.2e-10 = 1.750, both > 1), so NO saturation transition exists
    anywhere in the solar system: this radius is NOT a boundary. What this
    function returns is the isocline of the SOLAR MONOPOLE TAKEN IN
    ISOLATION — an internal-field COUNTERFACTUAL, kept because it is a
    useful diagnostic and because the pinned arithmetic is unchanged. Do
    not cite it as a location. Both Oort numbers (this 7438.9 AU and Vol 4's
    ~15,000 AU) retire as boundaries; the "one object or two" question is
    moot. Ruling relayed by the core-orchestrator mechanical-rulings batch
    (2026-08-04); its own docket record is OWED and flagged there.

    ⚑ Prior status (preserved, Rule 12): existence gated by the unadjudicated
    T4 keying fork: under total-local-field keying the Sun already sits at
    g_ext ≈ 1.8-2.0 a₀, so no saturation transition exists anywhere in the
    solar system
    (research/2026-07-10_collapse-target-registry.md:271-290). Grant's call.
    [Ratio corrected 2026-08-03: this line shipped as "≈ 2.0-2.1 a₀", which
    read the mantissa of g_ext = 2.1e-10 m/s² as if it were a ratio. The
    registry's own arithmetic at :282-:283 is 2.1/1.07 = 1.96 against the
    AVE a₀ and 2.1/1.2 = 1.75 against the empirical a₀ — hence 1.8-2.0. The
    physics is unchanged: 1.75 a₀ > a₀ either way, so total-field keying
    still removes the transition.]

    Returns:
        Saturation radius [AU].
    """
    r_sat = np.sqrt(G * M_SUN / A0_LATTICE)
    return r_sat / AU


def solar_axiom4_onset_summary() -> dict[str, float | int | str]:
    """
    Solar Axiom-4 onset radius under internal-field keying.

    🔴 FUNCTION RENAMED 2026-08-03 (repair pass). Former name, verbatim:
    oort_cloud_prediction(). The name was the retracted claim in miniature —
    it promised an Oort *prediction* from a function that computes a solar
    FIELD radius and (since the same-date retraction) makes no population
    claim at all. Renamed rather than flagged because the rename does not
    ripple: the module exports no __all__, ave/gravity/__init__.py does not
    re-export it, and the only consumer in the tree is
    src/tests/test_solar_impedance.py (verified two methods, 2026-08-03).
    Suffix "_summary" follows this module's existing convention for
    dict-returning roll-ups (cf. oumuamua_summary above).

    🔴 CONTAINMENT CLAIM RETRACTED 2026-08-03 (Oort containment-retraction
    lane; propagation of the merged 2026-07-19 deep-space reactive-bulk
    MECHANISM-RETRACTED ruling into Vol 3). This function's former docstring
    and its former "prediction" string both asserted that the Oort Cloud's
    inner edge *coincides with* the g = a₀ transition. That claim is
    RETRACTED and the hard-coded Hills-cloud comparands it was measured
    against are DELETED (below). Preserved verbatim for the record:

        docstring : "AVE prediction for the Oort Cloud location. The Oort
                     Cloud's inner edge should correspond to the radius
                     where the gravitational acceleration transitions from
                     Newtonian to the saturation regime (g ≈ a₀)."
        prediction: "Inner Oort Cloud coincides with g=a₀ transition"
        deleted   : r_hills_inner = 2000  # AU
                    r_hills_outer = 5000  # AU

    Why: the only bridge in this corpus from a *field isocline* (g_N = a₀)
    to a *population edge* (where comets sit) was the dissipative stall
    mechanism, and that stall is Axiom-3 forbidden — see
    manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:272
    ("any belt/Oort position derived from that kinetic-energy loss does not
    survive as a bulk-dissipation result"). The two quantities are also not
    comparands: r_sat is an instantaneous force-balance isocline; the Hills
    inner edge is a 4.6-Gyr emplacement-timescale boundary. Agreement would
    be a coincidence. The Hills bracket was additionally NOT observed — it
    is a simulation-inferred convention with ~factor-10 author spread and is
    uncited anywhere in this corpus (bibliography.bib has zero oort/hills/
    comet entries), so it was deleted rather than sourced.

    Per A47 v11b (substitution-not-retraction) the slot is NOT refilled: no
    replacement bracket and no successor containment claim is entered here.

    🔴 THE OBJECT DISSOLVES 2026-08-04 — T4 RULED: TOTAL LOCAL FIELD. The
    existence gate recorded below fired. There is no solar-system Axiom-4
    boundary at any radius; both Oort numbers (Vol 3's 7,438.9 AU and Vol 4's
    ~15,000 AU) retire as boundaries and the cross-volume "one object or two"
    question is MOOT rather than answered. This function is retained as an
    INTERNAL-FIELD COUNTERFACTUAL: it computes the isocline of the solar
    monopole taken in isolation, which is not what the kernel sees under the
    ruled keying. Arithmetic, keys and pins are unchanged; only the status is.

    What this function DOES return: the radius at which the Axiom-4 kernel
    turns on for the solar monopole under INTERNAL-FIELD keying — i.e. the
    outer edge of the Newtonian region. Its very existence is gated by the
    unadjudicated internal-vs-total-field keying fork (T4): under
    total-local-field keying the Sun already sits at g_ext ≈ 1.8–2.0 a₀
    (research/2026-07-10_collapse-target-registry.md:281-283 — g_ext ≈
    2.1e-10 m/s² is 2.1/1.07 = 1.96 a₀ against the AVE-derived a₀ and
    2.1/1.2 = 1.75 a₀ against the empirical one; ratio corrected 2026-08-03
    from a shipped "≈ 2.0–2.1 a₀" that misread the mantissa as a ratio), so
    no saturation transition exists anywhere in the solar system. The
    physics direction is unchanged — even the smaller ratio, 1.75, exceeds
    1. Grant's call; routed 2026-08-03, not resolved here.

    Returns:
        Dict describing the solar-FIELD onset radius. No population claim.
    """
    r_sat_au = saturation_radius_au()

    # ⚑ FLAG (not fixed, 2026-08-03): r_oort_outer is the same defect class as
    # the two deleted Hills constants — an uncited empirical/simulation
    # convention with wide author spread (~50,000–200,000 AU). It is retained
    # here only because the disposition dispatch scoped the deletion to the two
    # Hills comparands, and it is NOT a comparand for anything this function
    # computes. Surfaced rather than silently removed; deletion is routed.
    r_oort_outer = 100000  # AU — empirical reference value only, carries NO AVE claim

    return {
        "r_saturation_au": r_sat_au,
        "r_saturation_ly": r_sat_au * AU / (9.461e15),
        "r_oort_outer_au": r_oort_outer,
        "prediction": (
            "NOT A PREDICTION — internal-field COUNTERFACTUAL isocline of the "
            "solar monopole taken in isolation. T4 keying RULED 2026-08-04 = "
            "TOTAL local field, under which no saturation transition exists "
            "anywhere in the solar system: this is not a boundary at any "
            "radius. NO Oort-population claim (containment retracted "
            "2026-08-03); both Oort numbers retire as boundaries."
        ),
        "g_at_saturation": A0_LATTICE,
    }


# ═══════════════════════════════════════════════════════════════
# Kirkwood gaps as impedance cavity resonances
# ═══════════════════════════════════════════════════════════════

# Jupiter orbital parameters
M_JUPITER = 1.898e27  # kg
A_JUPITER = 5.2038 * AU  # Semi-major axis [m]
T_JUPITER = 11.862  # Orbital period [years]


def kirkwood_gap_radius(p: int, q: int) -> float:
    """
    Radius of a Kirkwood gap at the p:q mean-motion resonance with Jupiter.

    Kepler's third law: (a/a_J)³ = (T/T_J)² = (q/p)²

    a_gap = a_J × (q/p)^(2/3)

    Args:
        p: Jupiter orbital period multiple.
        q: Asteroid orbital period multiple. (p > q for inner resonances)

    Returns:
        Gap semi-major axis [AU].
    """
    return (A_JUPITER / AU) * (q / p) ** (2.0 / 3.0)


def kirkwood_impedance_model() -> list[dict[str, float | str | None]]:
    """
    Model Kirkwood gaps as impedance cavity modes.

    In AVE, Jupiter's gravitational field creates a periodic impedance
    modulation in the asteroid belt region.  Orbital resonances correspond
    to standing-wave nodes where constructive interference amplifies
    perturbations, clearing material.

    This is identical to Fabry-Pérot cavity modes:
        Destructive nodes at: r = r_J × (q/p)^(2/3)

    Returns:
        List of dicts with gap parameters.
    """
    # Known Kirkwood gaps (resonance p:q with Jupiter)
    resonances = [
        (4, 1, "4:1"),
        (3, 1, "3:1"),
        (5, 2, "5:2"),
        (7, 3, "7:3"),
        (2, 1, "2:1"),
    ]

    gaps = []
    for p, q, label in resonances:
        r_gap = kirkwood_gap_radius(p, q)

        # Observed gap centers (from asteroid surveys)
        observed = {
            "4:1": 2.06,
            "3:1": 2.50,
            "5:2": 2.82,
            "7:3": 2.95,
            "2:1": 3.28,
        }

        # Jupiter's gravitational perturbation strength at gap
        r_gap_m = r_gap * AU
        F_jupiter = G * M_JUPITER / (A_JUPITER - r_gap_m) ** 2
        F_sun = G * M_SUN / r_gap_m**2

        # Impedance mismatch at resonance
        Z_ratio = F_jupiter / F_sun  # Perturbation strength

        gaps.append(
            {
                "resonance": label,
                "r_predicted_au": r_gap,
                "r_observed_au": observed.get(label, None),
                "error_pct": (
                    abs(r_gap - observed.get(label, r_gap)) / observed.get(label, r_gap) * 100
                    if label in observed
                    else None
                ),
                "Z_perturbation_ratio": Z_ratio,
                "cavity_order": p - q,  # Mode number
            }
        )

    return gaps


# ═══════════════════════════════════════════════════════════════
# Saturn ring gaps as impedance cavity modes
# ═══════════════════════════════════════════════════════════════

# Saturn system constants
M_SATURN = 5.6834e26  # Saturn mass [kg]
R_SATURN = 5.8232e7  # Saturn equatorial radius [m]

# Saturn moon semi-major axes [m]
A_MIMAS = 185_539e3  # Mimas
A_ENCELADUS = 238_042e3  # Enceladus
A_TETHYS = 294_672e3  # Tethys
A_JANUS = 151_460e3  # Janus (co-orbital with Epimetheus)
A_PAN = 133_584e3  # Pan (inside Encke Gap)


def saturn_gap_radius(p: int, q: int, a_moon: float) -> float:
    """
    Radius of a Saturn ring gap at the p:q mean-motion resonance.

    DERIVATION:
        Same Kepler 3rd law as Kirkwood gaps:
            (a_gap / a_moon)³ = (T_gap / T_moon)² = (q/p)²

        Therefore:
            a_gap = a_moon × (q/p)^(2/3)

        The ring gap occurs where an orbiting particle completes
        exactly p orbits for every q orbits of the perturbing moon.

    Args:
        p: Moon orbital period multiple.
        q: Ring particle orbital period multiple.
        a_moon: Moon semi-major axis [m].

    Returns:
        Gap radius [m].
    """
    return a_moon * (q / p) ** (2.0 / 3.0)


def saturn_ring_gap_model() -> list[dict[str, float | str]]:
    """
    Model Saturn ring gaps as impedance cavity modes.

    In AVE, Saturn's moons create gravitational impedance modulations
    in the ring plane.  At mean-motion resonances, constructive
    interference amplifies perturbations and clears ring material.

    Known major gaps and their resonance associations:

    1. Cassini Division: 2:1 resonance with Mimas
       - Inner edge at 117,580 km, outer edge at 122,170 km
       - Width: ~4,590 km

    2. Encke Gap: Maintained by Pan (embedded moonlet)
       - Located at ~133,584 km
       - Width: ~325 km

    3. Keeler Gap: 42:43 resonance with Prometheus
       - Located at ~136,530 km
       - Width: ~35 km

    4. Maxwell Gap: 2:1 resonance with Mimas (C ring)
       - Located at ~87,491 km

    5. Colombo Gap: 4:2 resonance with Titan
       - Located at ~77,871 km

    Returns:
        List of dicts with gap parameters.
    """
    # Saturn ring gaps and their resonance associations
    # Only well-established mean-motion resonance associations used
    # Format: (p, q, moon_a_m, label, observed_km)
    resonances = [
        # Cassini Division inner edge: 2:1 with Mimas
        # The strongest and best-established ring resonance
        (2, 1, A_MIMAS, "Cassini (2:1 Mimas)", 117_580),
        # Encke Gap: maintained by Pan (moonlet AT the gap)
        (1, 1, A_PAN, "Encke (Pan)", 133_584),
    ]

    gaps = []
    for p, q, a_moon, label, obs_km in resonances:
        r_pred_m = saturn_gap_radius(p, q, a_moon)
        r_pred_km = r_pred_m / 1e3
        r_pred_Rs = r_pred_m / R_SATURN

        error_pct = abs(r_pred_km - obs_km) / obs_km * 100

        gaps.append(
            {
                "gap_name": label,
                "r_predicted_km": r_pred_km,
                "r_observed_km": obs_km,
                "r_predicted_Rs": r_pred_Rs,
                "error_pct": error_pct,
                "resonance_p_q": f"{p}:{q}",
                "moon_a_km": a_moon / 1e3,
            }
        )

    return gaps


# ═══════════════════════════════════════════════════════════════
# Earth flyby anomaly
# ═══════════════════════════════════════════════════════════════

R_EARTH = 6.371e6  # Earth radius [m]
M_EARTH = 5.972e24  # Earth mass [kg]
OMEGA_EARTH = 7.292e-5  # Earth rotation rate [rad/s]

# Earth magnetopause parameters
R_MAGNETOPAUSE_EARTH = 10.0 * R_EARTH  # ~10 R_E subsolar


def flyby_anomaly_anderson(
    v_inf: float,
    declination_in: float,
    declination_out: float,
) -> float:
    """
    Flyby velocity anomaly using the Anderson et al. (2008) empirical formula.

    ANDERSON FORMULA:
        Δv/v ≈ (2 ω_E R_E / c) × (cos δ_in - cos δ_out)

    where:
        ω_E = Earth rotation angular velocity
        R_E = Earth radius
        c   = speed of light
        δ_in, δ_out = incoming/outgoing declination of asymptotic velocity

    This is EMPIRICAL — Anderson noticed the pattern but had no physical
    explanation.  The AVE interpretation follows below.

    Args:
        v_inf: Hyperbolic excess velocity [m/s].
        declination_in: Incoming asymptotic declination [degrees].
        declination_out: Outgoing asymptotic declination [degrees].

    Returns:
        Velocity anomaly Δv [mm/s].
    """
    delta_in_rad = np.radians(declination_in)
    delta_out_rad = np.radians(declination_out)

    # Anderson coefficient
    K = 2.0 * OMEGA_EARTH * R_EARTH / C_0

    # Fractional velocity change
    dv_over_v = K * (np.cos(delta_in_rad) - np.cos(delta_out_rad))

    # Absolute velocity change [mm/s]
    dv_mm_s = dv_over_v * v_inf * 1e3

    return dv_mm_s


def flyby_anomaly_impedance(
    v_inf: float,
    periapsis_Re: float,
    declination_in: float,
    declination_out: float,
) -> dict[str, float | str]:
    """
    AVE impedance interpretation of the flyby anomaly.

    DERIVATION:
        The Earth's rotating frame creates an ASYMMETRIC impedance
        gradient.  A spacecraft approaching from the equatorial plane
        sees a different impedance profile than one approaching from
        the poles, because:

        1. The magnetopause is NOT spherically symmetric — it is
           compressed on the dayside and stretched on the nightside
           by the solar wind.

        2. The Earth's rotation drags the magnetospheric plasma,
           creating a frame-dragging-like impedance asymmetry.

        3. The spacecraft crossing the magnetopause boundary
           experiences a differential phase shift proportional to
           the impedance gradient along its trajectory.

        The AVE prediction:
            Δv = v_inf × (2 ω_E R_E / c) × (cos δ_in - cos δ_out)

        This is IDENTICAL to the Anderson formula, but now has a
        physical origin: the impedance gradient at the rotating
        magnetopause boundary.

        The coefficient K = 2ωR/c is the ratio of:
        - Rotational velocity at the equator: v_rot = ω_E R_E ≈ 465 m/s
        - Speed of light: c = 3×10⁸ m/s

        This is a GRAVITOMAGNETIC effect: the rotating mass creates
        a frame-dragging impedance asymmetry of order v_rot/c.

    Args:
        v_inf: Hyperbolic excess velocity [m/s].
        periapsis_Re: Closest approach distance [Earth radii].
        declination_in: Incoming asymptotic declination [degrees].
        declination_out: Outgoing asymptotic declination [degrees].

    Returns:
        Dictionary with prediction and physical explanation.
    """
    # Anderson formula prediction
    dv_anderson = flyby_anomaly_anderson(v_inf, declination_in, declination_out)

    # AVE impedance gradient at periapsis
    v_rot_equator = OMEGA_EARTH * R_EARTH

    # Gravitomagnetic coefficient
    K_gm = 2.0 * v_rot_equator / C_0

    # Impedance mismatch at magnetopause
    Z_inside = Z_0  # Vacuum impedance inside magnetosphere
    # Outside: solar wind plasma modifies Z (delegates to solar_wind_impedance)
    Z_outside = solar_wind_impedance(AU, freq_hz=1e6)
    Gamma_mp = float(reflection_coefficient(Z_inside, Z_outside))

    return {
        "v_inf_km_s": v_inf / 1e3,
        "periapsis_Re": periapsis_Re,
        "declination_in_deg": declination_in,
        "declination_out_deg": declination_out,
        "dv_predicted_mm_s": dv_anderson,
        "K_gravitomagnetic": K_gm,
        "v_rot_equator_m_s": v_rot_equator,
        "Gamma_magnetopause": Gamma_mp,
        "mechanism": "Rotating frame impedance asymmetry (gravitomagnetic)",
    }


def flyby_catalog() -> list[dict[str, float | str]]:
    """
    Known Earth flyby anomalies and AVE predictions.

    Data from Anderson et al. (2008) and subsequent analyses.

    Returns:
        List of flyby events with predictions vs observations.
    """
    # Known flybys: (name, v_inf [km/s], periapsis [R_E], δ_in [°], δ_out [°], Δv_obs [mm/s])
    flybys = [
        ("Galileo I (1990)", 8.949, 1.97, -12.5, -34.2, 3.92),
        ("Galileo II (1992)", 8.877, 1.48, -4.9, -4.9, -4.60),
        ("NEAR (1998)", 6.851, 1.23, 20.8, -71.9, 13.46),
        ("Cassini (1999)", 16.010, 1.18, 12.9, -5.0, -2.00),
        ("Rosetta I (2005)", 3.863, 1.32, -2.8, -34.3, 1.80),
        ("Messenger (2005)", 4.056, 3.35, 31.4, -31.4, 0.02),
        ("Rosetta II (2007)", 9.392, 1.81, -12.5, -34.3, 0.00),
    ]

    results = []
    for name, v_inf_kms, peri_Re, d_in, d_out, dv_obs in flybys:
        v_inf_ms = v_inf_kms * 1e3
        result = flyby_anomaly_impedance(v_inf_ms, peri_Re, d_in, d_out)
        result["name"] = name
        result["dv_observed_mm_s"] = dv_obs
        result["error_mm_s"] = abs(result["dv_predicted_mm_s"] - dv_obs)

        results.append(result)

    return results
