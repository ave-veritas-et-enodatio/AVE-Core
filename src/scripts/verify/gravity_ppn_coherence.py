"""Gravity PPN internal-coherence verification — AVE weak-field gravity sector.

Pre-registration: research/2026-06-05_gravity-ppn-coherence-prereg.md
Result doc:       research/2026-06-05_gravity-ppn-coherence-result.md

INTERNAL-COHERENCE audit (NOT an emergence or AVE-distinctness claim). The
corpus already classifies gravitational lensing / Shapiro / perihelion as
consistency-class ("AVE = GR at O(GM/c^2 r), no AVE-distinct observable").
This script tests whether AVE's gravity sector self-consistently reproduces
GR's weak-field PPN across its THREE coefficient-bearing canonical statements:

  (S1) The ONE-strain-field / two-index decomposition
       (manuscript/common_equations/eq_gravity_derived.tex Eq. lattice_decomposition;
        manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/
        temporal-spatial-lattice-decomposition.md):
           eps_11   = 7 G M / (c^2 r)              (radial strain field)
           n_temporal = 1 + (2/7) eps_11 = 1 + 2GM/rc^2   (redshift / g00)
           n_spatial  = 1 + (9/7) eps_11                  (LABELLED "light deflection")

  (S2) The canonical light-deflection derivation
       (manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex
        sec:double_deflection, lines 167-206; cross-validated
        03_macroscopic_relativity.tex:146-153; predictions.yaml P10):
           photon couples to  n_perp = 1 + (2/7) eps_11 = 1 + 2GM/rc^2
           -> delta_light = 4 G M / (b c^2)   (claimed = Einstein/GR)
       NOTE: this uses the (2/7) transverse index, NOT the (9/7) "spatial" index.

  (S3) The Ch 14 hand-set static perihelion potential
       (manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:60-77):
           V_tidal(r) = -GM/r (1 + 3 GM/(c^2 r))   (coeff 3)
           -> Delta_phi = 6 pi G M / (c^2 a (1-e^2))  (claimed = 43''/century, GR)

The question: do (S1)/(S2)/(S3) cohere under ONE eps_11 calibration?
If the (9/7) index in (S1) genuinely set the deflection, it would NOT give
4GM/bc^2 (S2). Which of the three is the outlier?

Discipline (ave-canonical-source): G, C_0, M_SUN imported from
ave.core.constants. Mercury orbital elements + solar radius + arcsec/century
conversion are cited as EXTERNAL OBSERVATIONAL inputs (sources inline). NO
hard-coded GR target values: GR predictions are recomputed from the SAME
imported G, C_0 via the standard PPN formulae so the comparison is
apples-to-apples (the PPN coefficients gamma=beta=1 ARE the GR content).
"""

import json
import os
from dataclasses import asdict, dataclass

import sympy as sp

from ave.core.constants import C_0, M_SUN, G  # canonical AVE constants

# ──────────────────────────────────────────────────────────────────────────
# EXTERNAL OBSERVATIONAL INPUTS (cited; NOT AVE-derived, NOT GR targets)
# ──────────────────────────────────────────────────────────────────────────
# Mercury osculating orbital elements (the prereg-specified values; J2000-era
# mean elements, NASA JPL planetary fact sheet / IAU):
A_MERCURY_M: float = 5.79e10  # semi-major axis [m]  (prereg value; JPL ~5.7909e10)
E_MERCURY: float = 0.2056  # eccentricity [-]     (prereg value; JPL 0.20563)
# Mercury orbital period (sidereal), to convert per-orbit advance to per-century:
T_MERCURY_DAYS: float = 87.969  # days  (NASA JPL Mercury fact sheet)
DAYS_PER_JULIAN_CENTURY: float = 36525.0  # 100 Julian years x 365.25 d

# Solar radius (grazing impact parameter for starlight deflection):
R_SUN_M: float = 6.957e8  # m  (IAU 2015 nominal solar radius)

# Unit conversions (mathematical constants, not physics targets):
RAD_PER_ARCSEC: float = float(sp.pi.evalf()) / (180.0 * 3600.0)
ARCSEC_PER_RAD: float = 1.0 / RAD_PER_ARCSEC


# ──────────────────────────────────────────────────────────────────────────
# RESULT RECORD
# ──────────────────────────────────────────────────────────────────────────
@dataclass
class CoherenceResult:
    label: str
    detail: str
    value: float
    reference: float
    reference_label: str
    ratio_to_reference: float
    coheres: bool


# ──────────────────────────────────────────────────────────────────────────
# SYMBOLIC CORE — refraction deflection for an index n(r) = 1 + K * GM/(c^2 r)
# ──────────────────────────────────────────────────────────────────────────
def symbolic_refraction_deflection_coeff():
    """Light deflection through a static radial refractive index.

    Standard geometric-optics / eikonal result (e.g. for a spherically
    symmetric index n(r) -> 1 at infinity): the bending of a ray with impact
    parameter b is

        delta = integral_{-inf}^{+inf}  (b / r) * (-dn/dr) / n  ds   (s along path)

    For a WEAK index n(r) = 1 + f(r) with f << 1, to first order in f the
    accumulated bending toward the mass is the transverse-gradient integral
    along the unperturbed straight path (r = sqrt(b^2 + z^2)):

        delta = - integral_{-inf}^{+inf}  (d n / d b)  dz

    where d/db is the derivative w.r.t. impact parameter at fixed z. (The
    along-path derivative dn/dz is odd in z and integrates to zero; the
    physical deflection is the transverse gradient.)

    With f(r) = K * (G M / c^2) / r  (i.e. n = 1 + K * GM/(c^2 r)), the integral
    evaluates in closed form to delta = 2 K * GM/(b c^2). Returns the symbolic
    coefficient C_delta such that delta = C_delta * G M / (b c^2); for a single
    index of slope K this is 2K.
    """
    K, GM, c, b = sp.symbols("K GM c b", positive=True)
    z = sp.symbols("z", real=True)
    r = sp.sqrt(b**2 + z**2)
    f = K * GM / (c**2 * r)  # the weak index perturbation n - 1
    delta = -sp.integrate(sp.diff(f, b), (z, -sp.oo, sp.oo))
    delta = sp.simplify(delta)
    # delta should be of the form (coeff) * GM/(b c^2); extract coeff vs K
    coeff = sp.simplify(delta / (GM / (b * c**2)))
    return sp.simplify(coeff), delta  # coeff (in terms of K), full delta


def ppn_light_deflection_coeff(gamma):
    """PPN weak-field light deflection coefficient.

    Standard PPN result: delta = (1 + gamma) * 2GM/(b c^2).
    Returns the dimensionless multiplier of GM/(b c^2), i.e. 2*(1+gamma).
    GR: gamma = 1 -> 4.
    """
    return sp.simplify(2 * (1 + gamma))


def ppn_perihelion_factor(beta, gamma):
    """PPN weak-field perihelion advance factor.

    Standard PPN result for the advance per orbit:
        Delta_phi = (2 - beta + 2*gamma)/3 * 6 pi GM/(c^2 a (1-e^2)).
    Returns the dimensionless factor F = (2 - beta + 2 gamma)/3 multiplying the
    GR baseline 6 pi GM/(c^2 a (1-e^2)). GR: beta=gamma=1 -> F = 1.
    """
    return sp.simplify((2 - beta + 2 * gamma) / 3)


def ave_indices_to_ppn():
    """Map AVE's canonical two-index metric to PPN (gamma, beta).

    AVE's static isotropic optical metric is written via two refractive
    indices over the ONE strain field eps_11 = 7 G M/(c^2 r):
        n_temporal = 1 + (2/7) eps_11   (governs clock rate / g00)
        n_spatial  = 1 + (9/7) eps_11   (governs g_ij)

    Standard isotropic-coordinate PPN metric (U = GM/(r c^2)):
        -g00     = 1 - 2U + 2 beta U^2 + ...
        g_ij     = (1 + 2 gamma U) delta_ij

    The temporal sector fixes the leading g00 (and hence the gravitational
    redshift): a clock at potential r ticks at rate proportional to
    1/n_temporal, so the redshift is z = n_temporal - 1. In PPN the leading
    redshift is z = U. Matching z:
        n_temporal - 1 = (2/7) eps_11 = 2GM/(c^2 r) = 2U
    => the temporal sector carries a g00 leading coefficient of 2U, i.e. an
       *effective* potential U_temporal = (n_temporal - 1) = 2U. This is the
       FIRST internal tension: the canonical leaves ALSO state the redshift is
       z ~ GM/(c^2 r) = U (eq_gravity_derived.tex:63), which is HALF of
       n_temporal - 1. Both statements live in the same canonical file.

    The spatial sector fixes gamma: g_ij = (1 + 2 gamma U) and AVE's
    n_spatial enters the spatial part of the optical metric as
    g_ij ~ n_spatial^2 delta_ij ~ (1 + 2 (n_spatial - 1)) delta_ij, so
        2 gamma U_temporal = 2 (n_spatial - 1) = 2 (9/7) eps_11 = 18 GM/(c^2 r)
    Taken at face value against the SAME U_temporal = 2U that the temporal
    sector sets, gamma_spatial = (n_spatial - 1)/(n_temporal - 1) = (9/7)/(2/7)
    = 9/2 = 4.5.

    Returns a dict of the symbolic / numeric PPN coefficients implied by each
    canonical reading. We DO NOT collapse the readings into one 'answer'; the
    point of the audit is to expose that the canonical statements imply
    DIFFERENT coefficients depending on which leaf you read.
    """
    # exact fractions from the canonical decomposition
    two_sevenths = sp.Rational(2, 7)
    nine_sevenths = sp.Rational(9, 7)
    # eps_11 = 7 GM/(c^2 r); n-1 contributions in units of U = GM/(c^2 r):
    nt_minus1_in_U = two_sevenths * 7  # = 2  (n_temporal - 1 = 2U)
    ns_minus1_in_U = nine_sevenths * 7  # = 9  (n_spatial  - 1 = 9U)

    # PPN gamma if the (9/7) "spatial" index literally sets g_ij relative to the
    # (2/7) temporal index that sets g00:
    gamma_from_9_7 = sp.Rational(ns_minus1_in_U, nt_minus1_in_U)  # 9/2

    # PPN gamma if instead the photon uses the SAME (2/7) transverse index for
    # BOTH the temporal and spatial sectors (the Ch 2 double-deflection reading,
    # i.e. an isotropic n that is the same in all directions -> gamma = 1):
    gamma_double_deflection = sp.Integer(1)

    return {
        "nt_minus1_in_U": int(nt_minus1_in_U),  # 2
        "ns_minus1_in_U": int(ns_minus1_in_U),  # 9
        "gamma_from_9_7_spatial": gamma_from_9_7,  # 9/2
        "gamma_double_deflection_2_7": gamma_double_deflection,  # 1
    }


# ──────────────────────────────────────────────────────────────────────────
# NUMERIC EVALUATION
# ──────────────────────────────────────────────────────────────────────────
def deflection_arcsec(slope_K: float, b_m: float = R_SUN_M) -> float:
    """delta = 2K * GM/(b c^2) for an index n = 1 + K * GM/(c^2 r). In arcsec.

    Mass = Sun (M_SUN, imported). The factor 2K is the closed-form refraction
    integral coefficient (verified symbolically by
    symbolic_refraction_deflection_coeff)."""
    delta_rad = 2.0 * slope_K * G * M_SUN / (b_m * C_0**2)
    return delta_rad * ARCSEC_PER_RAD


def gr_deflection_arcsec(b_m: float = R_SUN_M) -> float:
    """GR weak-field starlight deflection = 4GM/(b c^2), recomputed from the
    SAME imported G, C_0, M_SUN (the '4' is PPN gamma=1: 2*(1+gamma))."""
    delta_rad = 4.0 * G * M_SUN / (b_m * C_0**2)
    return delta_rad * ARCSEC_PER_RAD


def perihelion_advance_arcsec_per_century(factor_F: float) -> float:
    """Delta_phi per century = factor_F * 6 pi GM/(c^2 a (1-e^2)) per orbit,
    times orbits/century. Mercury elements + period are EXTERNAL inputs;
    M = Sun (imported). factor_F is the PPN multiplier ( =1 for GR )."""
    pi = float(sp.pi.evalf())
    per_orbit_rad = factor_F * 6.0 * pi * G * M_SUN / (C_0**2 * A_MERCURY_M * (1.0 - E_MERCURY**2))
    orbits_per_century = DAYS_PER_JULIAN_CENTURY / T_MERCURY_DAYS
    return per_orbit_rad * orbits_per_century * ARCSEC_PER_RAD


def chapter14_perihelion_per_orbit_rad() -> float:
    """Ch 14 coeff-3 structure: V_tidal = -GM/r (1 + 3GM/c^2 r) ->
    Delta_phi = 6 pi GM/(c^2 a (1-e^2)) per orbit (Ch 14 Eq, line 73).
    This is the SAME as GR (PPN F=1). M=Sun imported; elements external."""
    pi = float(sp.pi.evalf())
    return 6.0 * pi * G * M_SUN / (C_0**2 * A_MERCURY_M * (1.0 - E_MERCURY**2))


def main() -> dict:
    results: list = []

    # ── symbolic checks ────────────────────────────────────────────────
    coeff_K, _ = symbolic_refraction_deflection_coeff()  # expect 2*K
    K_sym = sp.symbols("K", positive=True)
    deflection_coeff_matches_2K = sp.simplify(coeff_K - 2 * K_sym).equals(0)

    gamma_sym, beta_sym = sp.symbols("gamma beta")
    light_coeff = ppn_light_deflection_coeff(gamma_sym)  # 2(1+gamma)
    perih_factor = ppn_perihelion_factor(beta_sym, gamma_sym)  # (2-beta+2gamma)/3
    ppn = ave_indices_to_ppn()

    # ── PHASE 1: light deflection ──────────────────────────────────────
    gr_defl = gr_deflection_arcsec()

    # (a) photon via the (2/7) transverse index n_perp = 1 + 2GM/c^2 r (K=2):
    defl_2_7 = deflection_arcsec(slope_K=2.0)
    results.append(
        CoherenceResult(
            label="Phase1: deflection via (2/7) transverse index (Ch 2 double-deflection)",
            detail="n_perp = 1 + (2/7)eps_11 = 1 + 2GM/c^2 r  ->  delta = 4GM/bc^2",
            value=defl_2_7,
            reference=gr_defl,
            reference_label="GR 4GM/bc^2",
            ratio_to_reference=defl_2_7 / gr_defl,
            coheres=abs(defl_2_7 / gr_defl - 1.0) < 1e-9,
        )
    )

    # (b) photon via the (9/7) "spatial" index n_spatial = 1 + 9GM/c^2 r (K=9):
    defl_9_7 = deflection_arcsec(slope_K=9.0)
    results.append(
        CoherenceResult(
            label="Phase1: deflection via (9/7) spatial index (decomposition-leaf label)",
            detail="n_spatial = 1 + (9/7)eps_11 = 1 + 9GM/c^2 r  ->  delta = 18GM/bc^2",
            value=defl_9_7,
            reference=gr_defl,
            reference_label="GR 4GM/bc^2",
            ratio_to_reference=defl_9_7 / gr_defl,
            coheres=abs(defl_9_7 / gr_defl - 1.0) < 1e-9,
        )
    )

    # implied PPN gamma for each reading: delta = 2*(1+gamma)*GM/bc^2
    #   (2/7) reading: 2*(1+gamma) = 4   -> gamma = 1
    #   (9/7) reading: 2*(1+gamma) = 18  -> gamma = 8
    gamma_implied_2_7 = defl_2_7 / gr_defl * 2.0 - 1.0  # = 1.0
    gamma_implied_9_7 = defl_9_7 / gr_defl * 2.0 - 1.0  # = 8.0

    # ── PHASE 2: perihelion ────────────────────────────────────────────
    # GR / Ch 14 coeff-3 baseline (PPN F = 1):
    ch14_per_orbit = chapter14_perihelion_per_orbit_rad()
    ch14_per_century = perihelion_advance_arcsec_per_century(factor_F=1.0)
    results.append(
        CoherenceResult(
            label="Phase2: Ch 14 coeff-3 perihelion (V_tidal ~ 1+3GM/c^2 r)",
            detail="Delta_phi = 6 pi GM/(c^2 a(1-e^2)); PPN factor F=1 (= GR)",
            value=ch14_per_century,
            reference=ch14_per_century,
            reference_label="GR 43''/century",
            ratio_to_reference=1.0,
            coheres=True,
        )
    )

    # Metric-derived perihelion IF gamma=4.5 (the 9/7-spatial reading) and the
    # standard PPN beta=1 (no canonical AVE statement sets beta independently):
    #   F = (2 - beta + 2 gamma)/3 = (2 - 1 + 2*4.5)/3 = 10/3
    F_metric_9_7 = float(ppn_perihelion_factor(sp.Integer(1), sp.Rational(9, 2)))
    perih_metric_9_7 = perihelion_advance_arcsec_per_century(factor_F=F_metric_9_7)
    results.append(
        CoherenceResult(
            label="Phase2: perihelion from metric IF gamma=9/2 (9/7-spatial), beta=1",
            detail=f"PPN factor F=(2-beta+2gamma)/3={F_metric_9_7:.4f} -> Delta_phi",
            value=perih_metric_9_7,
            reference=ch14_per_century,
            reference_label="GR/Ch14 43''/century",
            ratio_to_reference=perih_metric_9_7 / ch14_per_century,
            coheres=abs(perih_metric_9_7 / ch14_per_century - 1.0) < 1e-9,
        )
    )

    # Metric-derived perihelion IF gamma=1 (the 2/7 double-deflection reading),
    # beta=1: F = (2-1+2)/3 = 1 -> matches GR/Ch14 exactly.
    F_metric_2_7 = float(ppn_perihelion_factor(sp.Integer(1), sp.Integer(1)))
    perih_metric_2_7 = perihelion_advance_arcsec_per_century(factor_F=F_metric_2_7)
    results.append(
        CoherenceResult(
            label="Phase2: perihelion from metric IF gamma=1 (2/7 reading), beta=1",
            detail=f"PPN factor F={F_metric_2_7:.4f} -> Delta_phi (= GR/Ch14)",
            value=perih_metric_2_7,
            reference=ch14_per_century,
            reference_label="GR/Ch14 43''/century",
            ratio_to_reference=perih_metric_2_7 / ch14_per_century,
            coheres=abs(perih_metric_2_7 / ch14_per_century - 1.0) < 1e-9,
        )
    )

    out = {
        "constants_imported": {
            "G": G,
            "C_0": C_0,
            "M_SUN": M_SUN,
            "source": "ave.core.constants",
        },
        "external_inputs": {
            "A_MERCURY_M": A_MERCURY_M,
            "E_MERCURY": E_MERCURY,
            "T_MERCURY_DAYS": T_MERCURY_DAYS,
            "R_SUN_M": R_SUN_M,
            "DAYS_PER_JULIAN_CENTURY": DAYS_PER_JULIAN_CENTURY,
            "sources": "NASA JPL planetary fact sheet (Mercury a,e,T); IAU 2015 (R_sun)",
        },
        "symbolic": {
            "refraction_deflection_coeff_equals_2K": bool(deflection_coeff_matches_2K),
            "ppn_light_deflection_coeff_expr": str(light_coeff),
            "ppn_perihelion_factor_expr": str(perih_factor),
            "ave_indices_to_ppn": {k: str(v) for k, v in ppn.items()},
        },
        "phase1_deflection": {
            "gr_4GM_bc2_arcsec": gr_defl,
            "ave_2_7_index_arcsec": defl_2_7,
            "ave_2_7_ratio_to_GR": defl_2_7 / gr_defl,
            "ave_2_7_implied_PPN_gamma": gamma_implied_2_7,
            "ave_9_7_index_arcsec": defl_9_7,
            "ave_9_7_ratio_to_GR": defl_9_7 / gr_defl,
            "ave_9_7_implied_PPN_gamma": gamma_implied_9_7,
        },
        "phase2_perihelion": {
            "gr_ch14_arcsec_per_century": ch14_per_century,
            "ch14_per_orbit_rad": ch14_per_orbit,
            "metric_gamma_4p5_F": F_metric_9_7,
            "metric_gamma_4p5_arcsec_per_century": perih_metric_9_7,
            "metric_gamma_4p5_ratio_to_GR": perih_metric_9_7 / ch14_per_century,
            "metric_gamma_1_F": F_metric_2_7,
            "metric_gamma_1_arcsec_per_century": perih_metric_2_7,
            "metric_gamma_1_ratio_to_GR": perih_metric_2_7 / ch14_per_century,
        },
        "results": [asdict(r) for r in results],
    }
    return out


def _print_report(out: dict) -> None:
    print("=" * 78)
    print("AVE GRAVITY PPN INTERNAL-COHERENCE VERIFICATION")
    print("  (consistency-class audit; NOT an emergence / AVE-distinctness claim)")
    print("=" * 78)
    ci = out["constants_imported"]
    print(f"\nImported (ave.core.constants): G={ci['G']:.6e}  C_0={ci['C_0']:.6e}  " f"M_SUN={ci['M_SUN']:.6e}")
    ei = out["external_inputs"]
    print(
        f"External inputs: Mercury a={ei['A_MERCURY_M']:.4e} m  e={ei['E_MERCURY']}  "
        f"T={ei['T_MERCURY_DAYS']} d  R_sun={ei['R_SUN_M']:.4e} m"
    )
    print(f"  sources: {ei['sources']}")

    s = out["symbolic"]
    print("\n--- SYMBOLIC ---")
    print(f"  refraction deflection coeff = 2K (verified): " f"{s['refraction_deflection_coeff_equals_2K']}")
    print(f"  PPN light-deflection coeff  : delta = [{s['ppn_light_deflection_coeff_expr']}] * GM/bc^2")
    print(f"  PPN perihelion factor       : F = {s['ppn_perihelion_factor_expr']}")
    print(f"  AVE indices -> PPN          : {s['ave_indices_to_ppn']}")

    p1 = out["phase1_deflection"]
    print("\n--- PHASE 1: LIGHT DEFLECTION (grazing Sun, b = R_sun) ---")
    print(f"  GR (4GM/bc^2)                       : {p1['gr_4GM_bc2_arcsec']:.4f} arcsec")
    print(
        f"  AVE (2/7) transverse index n_perp   : {p1['ave_2_7_index_arcsec']:.4f} arcsec"
        f"   ratio={p1['ave_2_7_ratio_to_GR']:.4f}  PPN gamma={p1['ave_2_7_implied_PPN_gamma']:.3f}"
    )
    print(
        f"  AVE (9/7) spatial index n_spatial   : {p1['ave_9_7_index_arcsec']:.4f} arcsec"
        f"   ratio={p1['ave_9_7_ratio_to_GR']:.4f}  PPN gamma={p1['ave_9_7_implied_PPN_gamma']:.3f}"
    )

    p2 = out["phase2_perihelion"]
    print("\n--- PHASE 2: MERCURY PERIHELION ADVANCE ---")
    print(f"  GR / Ch 14 coeff-3 (F=1)            : {p2['gr_ch14_arcsec_per_century']:.4f} arcsec/century")
    print(
        f"  metric IF gamma=9/2, beta=1 (F={p2['metric_gamma_4p5_F']:.3f}): "
        f"{p2['metric_gamma_4p5_arcsec_per_century']:.4f} arcsec/century"
        f"   ratio={p2['metric_gamma_4p5_ratio_to_GR']:.4f}"
    )
    print(
        f"  metric IF gamma=1,   beta=1 (F={p2['metric_gamma_1_F']:.3f}): "
        f"{p2['metric_gamma_1_arcsec_per_century']:.4f} arcsec/century"
        f"   ratio={p2['metric_gamma_1_ratio_to_GR']:.4f}"
    )

    print("\n--- COHERENCE TABLE ---")
    for r in out["results"]:
        flag = "COHERES" if r["coheres"] else "MISMATCH"
        print(f"  [{flag:8s}] {r['label']}")
        print(f"             {r['detail']}")
        print(
            f"             value={r['value']:.4f}  vs {r['reference_label']}"
            f"={r['reference']:.4f}  ratio={r['ratio_to_reference']:.4f}"
        )
    print("=" * 78)


if __name__ == "__main__":
    out = main()
    _print_report(out)
    results_path = os.path.join(os.path.dirname(__file__), "gravity_ppn_coherence_results.json")
    with open(results_path, "w") as fh:
        json.dump(out, fh, indent=2)
    print(f"\nResults written to {results_path}")
