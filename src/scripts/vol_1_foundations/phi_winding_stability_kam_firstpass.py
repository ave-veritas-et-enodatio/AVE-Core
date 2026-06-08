"""phi-winding-stability / KAM lepton-tower: ALPHA-FREE first-pass (sanity-check).

SCOPE NOTE (2026-06-07, ave-driver-script-honesty + consistency-vs-emergence applied):
    This is NOT a forward-prediction of alpha and NOT a fit-to-1/4. It is the
    ALPHA-FREE first-pass for the prereg
        research/2026-06-07_phi-winding-stability-lepton-tower.md
    It probes the ONLY open alpha-route (epic-doc §20): is phi FORCED as the
    most-stable electron winding (=> R*r=1/4 pure geometry => alpha derived), or
    chosen? Two conjuncts must BOTH hold:
        (a) the electron picks the MOST-STABLE winding (KAM), and
        (b) the (2,3) winding FORCES R/r = phi^2 (the golden-torus geometry).

    What this script computes (all ALPHA-FREE):
      1. The route's load-bearing algebra: {R/r=phi^2, R-r=1/2} => R*r=1/4
         (confirms the algebra so the doc cites an engine-checked identity, not
         a hand-wave; this is the step that WOULD flip the section-18 FIT to a
         derivation IF R/r=phi^2 could be established as PRIMARY).
      2. The golden mean's continued-fraction convergents (Fibonacci ratios) and
         which torus knots (F_n, F_{n+1}) realize them -- the KAM "most-stable"
         ladder.
      3. The (2,q) family q in {3,5,7,9,11}: winding ratio q/p, geodesic aspect
         ratio R/r=q/p, distance to phi^2 and to phi, continued-fraction
         irrationality (Diophantine) proxy -- the KAM-stability ordering.
      4. The discriminator the brief proposed -- (2,5),(2,7) -> m_mu,m_tau -- is
         tested for an ALPHA-FREE (p,q)->mass relation. CODATA mass ratios are
         read ONLY for comparison (clearly labeled). NO formula is fit (that
         would be the coincidence-magnet the brief warns against).

    HONESTY GUARANTEES (verifiable below):
      * ALPHA / ALPHA_COLD_INV are NEVER read when constructing any winding,
        aspect-ratio, KAM-stability, or Fibonacci quantity. Those are built from
        integers + PHI (sqrt(5)) only.
      * ALPHA is read ONLY to print the corpus alpha-DEPENDENT lepton formulas
        for comparison (to show the corpus tower USES alpha; the alpha-free
        route does not exist). Comparison, not construction.
      * CODATA mass ratios (206.768, 3477.23) are READ-ONLY comparison targets;
        no function of (p,q) is fit to them.
      * No hardcoded 137.036 / alpha literal. PHI imported from ave.core.constants.

    DAG / anti-cheat: the only bare numbers are exact integers (winding/Fibonacci
    indices) and exact geometric factors (1/2, 2, the phi^2 algebra). No tuned
    constant; no alpha literal.

VERDICT (see doc for full reasoning): the route HITS THE UNFORCED-PHI WALL.
    KAM stability constrains the ROTATION NUMBER (winding/frequency ratio), not
    the geometric ASPECT RATIO R/r; these are independent DOF of the phasor
    Lissajous. The KAM-most-stable winding is the IRRATIONAL golden mean phi (a
    quasiperiodic orbit that never closes) -- in tension with the RATIONAL,
    closed (2,3)=3/2 torus knot the electron is identified as. The KAM-stable
    knot LADDER is the Fibonacci ladder (2,3)->(3,5)->(5,8), NOT the brief's
    proposed (2,5),(2,7) tower (which is the corpus BARYON ladder). No alpha-free
    (p,q)->mass relation exists. Conjunct (b) is NOT forced; section-18 FIT stands.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import (
    ALPHA,  # READ ONLY in the final comparison print (corpus alpha-DEPENDENT formulas)
    PHI,    # golden ratio = (1+sqrt5)/2, ALPHA-free
)

PHI2 = PHI * PHI  # phi^2 = phi + 1 ~ 2.618 (the golden-torus aspect ratio R/r)


# ----------------------------------------------------------------------------
# 1. Route load-bearing algebra: {R/r = phi^2, R - r = 1/2}  =>  R*r = 1/4
#    (ALPHA-free; this is the identity that WOULD derive alpha if R/r=phi^2
#     were established as PRIMARY, instead of falling out of R*r=1/4.)
# ----------------------------------------------------------------------------
def algebra_phi2_to_quarter() -> dict:
    # From R/r = phi^2 and R - r = 1/2:
    #   R = phi^2 * r ;  phi^2 r - r = 1/2 ; r (phi^2 - 1) = 1/2 ; phi^2-1 = phi
    #   => r = 1/(2 phi) = (phi-1)/2 ;  R = phi/2 ; R*r = 1/4
    r = 1.0 / (2.0 * PHI)
    R = PHI2 * r
    return {
        "R": R,
        "r": r,
        "R_minus_r": R - r,            # must be 1/2
        "R_over_r": R / r,             # must be phi^2
        "R_times_r": R * r,            # must be 1/4  <-- the alpha-absorbing knob
        "phi2": PHI2,
    }


# ----------------------------------------------------------------------------
# 2. Golden-mean continued-fraction convergents = Fibonacci ratios; the
#    torus knots (F_n, F_{n+1}) that realize the KAM "most-stable" ladder.
# ----------------------------------------------------------------------------
def fibonacci(n: int) -> list[int]:
    fibs = [1, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def golden_convergents(n_terms: int = 9) -> list[dict]:
    fibs = fibonacci(n_terms + 2)
    rows = []
    for i in range(1, n_terms + 1):
        p, q = fibs[i], fibs[i + 1]  # consecutive Fibonacci = (F_n, F_{n+1})
        ratio = q / p
        rows.append({
            "knot": (p, q),
            "ratio_q_over_p": ratio,
            "dist_to_phi": abs(ratio - PHI),
            "is_single_component_knot": (np.gcd(p, q) == 1 and p >= 2 and q >= 2),
        })
    return rows


# ----------------------------------------------------------------------------
# 3. The (2,q) family: KAM-stability ordering + geodesic aspect ratio vs phi^2.
#    Diophantine/irrationality proxy: a rational p/q has continued fraction
#    that TERMINATES -> it is a resonant (rational) torus -> breaks FIRST under
#    KAM perturbation (Poincare-Birkhoff). We report the closed-form ratio and
#    its distance from the golden mean as the "how-far-from-most-stable" proxy.
# ----------------------------------------------------------------------------
def two_q_family(qs=(3, 5, 7, 9, 11)) -> list[dict]:
    p = 2
    rows = []
    for q in qs:
        ratio = q / p                  # winding/frequency ratio (rational => resonant)
        geodesic_aspect = q / p        # geodesic (2,q) knot wants R/r = q/p
        rows.append({
            "knot": (p, q),
            "ratio_q_over_p": ratio,
            "geodesic_R_over_r": geodesic_aspect,
            "dist_geodesic_to_phi2": abs(geodesic_aspect - PHI2),
            "dist_ratio_to_phi": abs(ratio - PHI),
            "is_golden_convergent": False,  # set below
            "crossing_number_c": min(p * (q - 1), q * (p - 1)),
            "hopf_QH": p * q,
        })
    # mark which (2,q) are golden convergents (only (2,3) is: 3/2 = F_3/F_2)
    conv_knots = {row["knot"] for row in golden_convergents()}
    for row in rows:
        row["is_golden_convergent"] = row["knot"] in conv_knots
    return rows


# ----------------------------------------------------------------------------
# 4. Lepton-tower discriminator: is there an ALPHA-FREE (p,q)->mass relation?
#    CODATA ratios are comparison-only. Corpus formulas are alpha-DEPENDENT.
# ----------------------------------------------------------------------------
def lepton_tower_check() -> dict:
    # CODATA mass ratios (comparison targets ONLY; not fit to anything):
    m_mu_over_m_e_CODATA = 206.7682830
    m_tau_over_m_e_CODATA = 3477.23

    # Corpus (alpha-DEPENDENT) lepton formulas, for comparison -- these USE alpha:
    #   m_mu/m_e = 1 / (alpha * sqrt(3/7))     (lepton-spectrum.md:37)
    #   m_tau/m_e = p_c / alpha^2 = 8*pi / alpha  (lepton-spectrum.md:59)
    corpus_mu = 1.0 / (ALPHA * np.sqrt(3.0 / 7.0))
    corpus_tau = 8.0 * np.pi / ALPHA

    # ALPHA-FREE winding functions of the brief's proposed (2,5),(2,7):
    #   Pure topological invariants -- NO alpha. We REPORT them next to the
    #   CODATA ratios to show no alpha-free invariant lands near the masses.
    #   (We do NOT search for a fitting function: that is the coincidence-magnet.)
    def invariants(p, q):
        c = min(p * (q - 1), q * (p - 1))
        return {"c": c, "Q_H": p * q, "SL": p * q - p - q}

    return {
        "m_mu_over_m_e_CODATA": m_mu_over_m_e_CODATA,
        "m_tau_over_m_e_CODATA": m_tau_over_m_e_CODATA,
        "corpus_mu_ALPHA_DEPENDENT": corpus_mu,
        "corpus_tau_ALPHA_DEPENDENT": corpus_tau,
        "inv_2_5": invariants(2, 5),   # brief's "muon" winding (corpus: this is the PROTON)
        "inv_2_7": invariants(2, 7),   # brief's "tau"  winding (corpus: this is the Delta)
        "inv_2_3": invariants(2, 3),   # the actual electron winding
    }


def main() -> None:
    print("=" * 76)
    print("phi-winding-stability / KAM lepton-tower -- ALPHA-FREE first-pass")
    print("=" * 76)

    print("\n[1] ROUTE ALGEBRA  {R/r=phi^2, R-r=1/2} => R*r=1/4  (the would-be derivation)")
    alg = algebra_phi2_to_quarter()
    print(f"    R               = {alg['R']:.10f}   (expect phi/2 = {PHI/2:.10f})")
    print(f"    r               = {alg['r']:.10f}   (expect (phi-1)/2 = {(PHI-1)/2:.10f})")
    print(f"    R - r           = {alg['R_minus_r']:.10f}   (expect 0.5)")
    print(f"    R / r           = {alg['R_over_r']:.10f}   (expect phi^2 = {PHI2:.10f})")
    print(f"    R * r           = {alg['R_times_r']:.10f}   (expect 0.25)  <- alpha-absorbing knob")
    assert abs(alg["R_minus_r"] - 0.5) < 1e-12
    assert abs(alg["R_over_r"] - PHI2) < 1e-12
    assert abs(alg["R_times_r"] - 0.25) < 1e-12
    print("    => ALGEBRA CONFIRMED: IF R/r=phi^2 were PRIMARY, R*r=1/4 derives with NO alpha.")
    print("       (The open question is whether KAM can make R/r=phi^2 primary. See [3].)")

    print("\n[2] KAM MOST-STABLE LADDER = golden-mean convergents = Fibonacci knots (F_n,F_{n+1})")
    print("    knot     q/p        |q/p - phi|   single-component-knot?")
    for row in golden_convergents(8):
        p, q = row["knot"]
        print(f"    ({p:>2},{q:>2})  {row['ratio_q_over_p']:.6f}   {row['dist_to_phi']:.6f}      "
              f"{row['is_single_component_knot']}")
    print("    => The KAM-stable knot LADDER increases BOTH indices: (2,3)->(3,5)->(5,8)->...")
    print("       It is NOT the (2,q) ladder. Only (2,3) is a golden convergent.")

    print("\n[3] THE (2,q) FAMILY -- KAM stability + geodesic aspect ratio vs phi^2")
    print("    knot     q/p     geodesic R/r   |R/r - phi^2|   |q/p - phi|  golden-conv?  c   Q_H")
    for row in two_q_family():
        p, q = row["knot"]
        print(f"    ({p:>2},{q:>2})  {row['ratio_q_over_p']:.4f}   {row['geodesic_R_over_r']:.4f}"
              f"         {row['dist_geodesic_to_phi2']:.4f}        {row['dist_ratio_to_phi']:.4f}"
              f"      {str(row['is_golden_convergent']):>5}      {row['crossing_number_c']}  {row['hopf_QH']}")
    print(f"    phi^2 (golden-torus aspect R/r) = {PHI2:.6f}")
    print("    => NO (2,q) geodesic aspect ratio equals phi^2. (2,3)'s own geodesic R/r is 1.5,")
    print("       not phi^2=2.618. The (2,q) winding ratios MARCH AWAY from phi (5/2,7/2,...).")
    print("       KAM acts on q/p (winding); R/r=phi^2 (aspect) is an INDEPENDENT DOF -> unforced.")

    print("\n[4] LEPTON-TOWER DISCRIMINATOR -- is there an ALPHA-FREE (p,q)->mass relation?")
    lt = lepton_tower_check()
    print(f"    CODATA   m_mu/m_e  = {lt['m_mu_over_m_e_CODATA']:.4f}")
    print(f"    CODATA   m_tau/m_e = {lt['m_tau_over_m_e_CODATA']:.4f}")
    print(f"    corpus   m_mu/m_e  = {lt['corpus_mu_ALPHA_DEPENDENT']:.4f}   (= 1/(alpha*sqrt(3/7)) -- USES alpha)")
    print(f"    corpus   m_tau/m_e = {lt['corpus_tau_ALPHA_DEPENDENT']:.4f}   (= 8*pi/alpha          -- USES alpha)")
    print(f"    ALPHA-FREE invariants of brief's (2,5): {lt['inv_2_5']}  (corpus: this is the PROTON)")
    print(f"    ALPHA-FREE invariants of brief's (2,7): {lt['inv_2_7']}  (corpus: this is the Delta)")
    print(f"    ALPHA-FREE invariants of electron(2,3): {lt['inv_2_3']}")
    print("    => No ALPHA-FREE invariant of (2,5)/(2,7) lands near 206.77/3477.23. The corpus")
    print("       tower USES alpha and is NOT a (2,q) winding tower (leptons = (2,3)+Cosserat")
    print("       torsion; (2,5),(2,7) are BARYONS). No alpha-free (p,q)->mass relation exists;")
    print("       fitting one would be the coincidence-magnet. DISCRIMINATOR NOT COMPUTABLE.")

    print("\n" + "=" * 76)
    print("VERDICT: conjunct (b) -- (2,3) FORCES R/r=phi^2 -- is NOT forced by KAM.")
    print("  KAM stabilizes the IRRATIONAL winding phi (quasiperiodic, never closes), in")
    print("  tension with the RATIONAL closed (2,3)=3/2 knot. R/r=phi^2 (aspect) is an")
    print("  INDEPENDENT phasor DOF from the winding -> KAM cannot force it. The lepton-tower")
    print("  discriminator does not exist as a KAM object. Section-18 FIT verdict STANDS.")
    print("=" * 76)


if __name__ == "__main__":
    main()
