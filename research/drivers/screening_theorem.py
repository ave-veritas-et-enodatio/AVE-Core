#!/usr/bin/env python3
"""Screening-theorem lane driver — the NUMERIC ARM (Method 2) of the frozen prereg
`research/2026-08-09_screening-theorem_prereg-FROZEN.md`.

Computes, with every input pinned and sourced:
  1. NS-WALL arm (gate G-NSWALL): per-star r_sat = 7GM/c^2 from the FROZEN masses,
     the wall condition R_NS < r_sat against the declared radius-import band, and
     the per-star flip-point radius.
  2. Orbital kinematics per comparator (Kepler from frozen masses + periods).
  3. RESIDUE channels (gate G-RESIDUE-2M, method b): numeric evaluation of each
     candidate compression-sourcing channel of the exterior configuration,
     including a direct ODE integration of the graded-equilibrium volumetric
     response theta(r) (the G-DIV numeric receipt) and its moment integral,
     compared against the closed forms of the result doc's Method 1.
  4. Comparator arithmetic (gate G-COMP): F_res vs delta_DP and delta_HT.

Engine `src/ave` byte-untouched. No RNG anywhere. All outputs shipped to
`screening_theorem_results.json`; the gating number check verifies the result
doc's numerals against that JSON (with a mutation receipt).

Physical constants (named imports, CODATA/IAU nominal):
  GM_sun/c^2 = 1.476625 km  (IAU nominal solar mass parameter / c^2)
  c = 299792.458 km/s
"""

import json
import math
import os

import numpy as np
from scipy.integrate import solve_ivp, quad

# ----------------------------------------------------------------------------
# Frozen inputs (prereg section 4; sources named there)
# ----------------------------------------------------------------------------
GM_SUN_OVER_C2_KM = 1.476625      # km, IAU nominal
C_KM_S = 299792.458               # km/s

COMPARATORS = {
    "HT": {
        # Weisberg & Huang 2016 (arXiv:1606.02744) — frozen prereg section 4
        "m_p": 1.438, "m_c": 1.390,          # M_sun
        "P_b_s": 27906.98,                    # s (7.751939 h, W&H 2016)
        "e": 0.6171,                          # frozen via #927
        "delta": 0.0016,                      # 1-sigma fractional
    },
    "DP": {
        # Kramer et al. 2021 (PRX 11, 041050) — frozen prereg section 4
        "m_p": 1.338185, "m_c": 1.248868,     # M_sun (A, B)
        "P_b_s": 8834.534,                    # s (0.10225156 d, Kramer 2021)
        "e": 0.088,                           # frozen via #927
        "delta": 1.3e-4,                      # 95% fractional bound
    },
}

# NS radius import band (prereg section 4: NICER-class, declared import)
R_NS_BAND_KM = (11.4, 13.7)

# Speed ratio (canon, #927 section 0 row 4: isotropic re-expression sqrt(10/3))
C_P_OVER_C_S = math.sqrt(10.0 / 3.0)   # 1.8257
A_ANG = 2.0 / 3.0                      # #919 angular factor (cited structure)

# ----------------------------------------------------------------------------
# 1. NS-wall arm
# ----------------------------------------------------------------------------

def ns_wall_arm():
    out = {}
    stars = [
        ("HT_pulsar", COMPARATORS["HT"]["m_p"]),
        ("HT_companion", COMPARATORS["HT"]["m_c"]),
        ("DP_A", COMPARATORS["DP"]["m_p"]),
        ("DP_B", COMPARATORS["DP"]["m_c"]),
    ]
    lo, hi = R_NS_BAND_KM
    for name, m in stars:
        r_sat = 7.0 * m * GM_SUN_OVER_C2_KM
        out[name] = {
            "mass_msun": m,
            "r_sat_km": round(r_sat, 4),
            # wall exists iff R_NS < r_sat  (vacuum grade A(r)=r_sat/r reaches 1
            # outside the surface); flip point IS r_sat.
            "flip_radius_km": round(r_sat, 4),
            "walled_at_band_low": bool(lo < r_sat),
            "walled_at_band_high": bool(hi < r_sat),
            "straddled_by_band": bool(lo < r_sat < hi),
        }
    return out

# ----------------------------------------------------------------------------
# 2. Orbital kinematics (Kepler, frozen masses + periods)
# ----------------------------------------------------------------------------

def kepler(comp):
    m_tot = comp["m_p"] + comp["m_c"]
    gm_tot_km3_s2 = m_tot * GM_SUN_OVER_C2_KM * C_KM_S**2   # GM in km^3/s^2
    P = comp["P_b_s"]
    a_km = (gm_tot_km3_s2 * P**2 / (4.0 * math.pi**2)) ** (1.0 / 3.0)
    v_rel_km_s = 2.0 * math.pi * a_km / P                    # circular-equivalent
    beta = v_rel_km_s / C_KM_S
    beta_P = beta / C_P_OVER_C_S
    return {
        "m_tot_msun": m_tot,
        "a_km": a_km,
        "v_rel_km_s": v_rel_km_s,
        "beta": beta,
        "beta_P": beta_P,
    }

# ----------------------------------------------------------------------------
# 3. G-DIV numeric receipt: graded-equilibrium volumetric response theta(r)
# ----------------------------------------------------------------------------
# Static spherically-symmetric equilibrium in the graded medium around one star.
# Perturbative closure (Method 1, result doc section on G-DIV):
#   base dress   u0 = B / r^2        (theta = 0 exactly; homogeneous Lame)
#   grade        S(A) = sqrt(1 - A^2), A = r_sat / r
#   moduli       G(r) = G0 * S(A)    [softening branch]
#                K(r) = K0 / S(A)    [stiffening branch]  (FLAG-W: BOTH branches
#                run; the theta-response magnitude class must be branch-robust)
#   induced      (K + 4G/3) dtheta/dr = 4 B G'(r) / r^3   (leading residual)
# Numeric arm: integrate dtheta/dr from r_out down to r_in for both branches,
# report theta(r)/eps_dev(r) at sample radii and the moment-ratio integrals.
# Units: r in r_sat; B = 1 (cancels in every ratio). K0 = 2*G0 (K=2G canon).

def theta_ode(branch, r_in=1.05, r_out=1e4, n=4000):
    G0, K0 = 1.0, 2.0
    rs = np.geomspace(r_out, r_in, n)   # integrate inward

    def moduli(r):
        A = 1.0 / r
        S = math.sqrt(max(1.0 - A * A, 1e-12))
        if branch == "soft":
            G, K = G0 * S, K0 * S
        elif branch == "stiff_K":
            G, K = G0 * S, K0 / S
        else:
            raise ValueError(branch)
        return G, K

    def dG_dr(r, h=1e-6):
        return (moduli(r + h)[0] - moduli(r - h)[0]) / (2 * h)

    def rhs(r, y):
        G, K = moduli(r)
        return [4.0 * dG_dr(r) / ((K + 4.0 * G / 3.0) * r**3)]

    sol = solve_ivp(rhs, (r_out, r_in), [0.0], t_eval=rs, rtol=1e-10,
                    atol=1e-14, method="RK45")
    theta = sol.y[0]
    eps_dev = 1.0 / rs**3          # |u0'| class, B=1
    ratio = theta / eps_dev
    samples = {}
    for r_probe in (1.5, 2.0, 5.0, 10.0, 100.0):
        i = int(np.argmin(np.abs(rs - r_probe)))
        samples[f"r={r_probe}"] = {
            "theta": float(theta[i]),
            "theta_over_epsdev": float(ratio[i]),
            "closed_form_A2": float(1.0 / r_probe**2),
        }
    return {"samples": samples,
            "max_abs_theta_over_epsdev": float(np.max(np.abs(ratio)))}

# Moment-ratio integrals (per-star wall-shell compression moment vs the
# orbit-scale shear moment; a/r_sat from kinematics):
#   M_P / M_S ~ [int_{1}^{a} |theta(r)| r^4 dr] / [int_{1}^{a} eps_dev r^4 dr]
# with theta ~ c_th / r^5 asymptotically (c_th from the ODE) and
# eps_dev = 1/r^3.  Numerator ~ c_th*ln(a), denominator ~ a^2/2.

def moment_ratio(branch, a_over_rsat):
    res = theta_ode(branch)
    # asymptotic theta coefficient: theta ~ c_th / r^5; read at r=5
    c_th = abs(res["samples"]["r=5.0"]["theta"]) * 5.0**5
    num, _ = quad(lambda r: (c_th / r**5) * r**4, 1.05, a_over_rsat, limit=200)
    den, _ = quad(lambda r: (1.0 / r**3) * r**4, 1.05, a_over_rsat, limit=200)
    return {"c_theta": c_th, "moment_ratio": num / den,
            "closed_form": 2.0 * c_th * math.log(a_over_rsat) / a_over_rsat**2,
            "theta_receipt": res}

# ----------------------------------------------------------------------------
# 4. Residue channels + comparator arithmetic
# ----------------------------------------------------------------------------

def residue(comp_key):
    comp = COMPARATORS[comp_key]
    kin = kepler(comp)
    r_sat_mean = 7.0 * 0.5 * (comp["m_p"] + comp["m_c"]) * GM_SUN_OVER_C2_KM
    a_over_rsat = kin["a_km"] / r_sat_mean

    # CH-1 retardation/kinematic mismatch: moment suppression beta_P^2
    #   -> flux suppression beta_P^4, times the channel speed/angular factor.
    speed_factor = A_ANG * (1.0 / C_P_OVER_C_S) ** 5
    ch1 = kin["beta_P"] ** 4 * speed_factor

    # CH-2 graded-shell conversion: per-star wall-shell moment ratio (both
    # FLAG-W branches; take the LARGER = conservative), squared for flux,
    # times the speed/angular factor.
    mr_soft = moment_ratio("soft", a_over_rsat)
    mr_stiff = moment_ratio("stiff_K", a_over_rsat)
    mr = max(abs(mr_soft["moment_ratio"]), abs(mr_stiff["moment_ratio"]))
    ch2 = (2.0 * mr) ** 2 * speed_factor          # 2 stars, coherent worst case

    # CH-0 (Tier-2 repair): the enclosed-charge orbital quadrupole — the
    # residue-setting channel. Moment ratio 1 by #767's receipted structure.
    ch0 = ch0_enclosed_charge_channel(comp)

    # CH-3 interaction-energy (A1 field-energy) EXTRA moment (the smooth
    # field-energy distribution's own l=2 content, distinct from CH-0's
    # source-charge term). METHOD (a): exact closed form kappa = 1/6
    # ((3/2)|kappa| = 1/4). METHOD (b): independent midpoint-centered
    # full-domain quadrature (reproduces 1/6; the defective mass-centered
    # doubling that gave 5/24 is retained above as the disclosed exhibit).
    comp_orbit = (comp["m_p"] + comp["m_c"]) * GM_SUN_OVER_C2_KM / kin["a_km"]
    quad = ch3_field_moment_quadrature_midpoint(comp["m_p"], comp["m_c"])
    coef = quad["moment_ratio_coefficient_1p5_kappa"]   # = 1/4, exact-anchored
    ch3 = (coef * comp_orbit) ** 2 * speed_factor
    ch3_scaling_envelope = comp_orbit ** 2 * speed_factor

    f_res = max(ch0["flux"], ch1, ch2, ch3)
    f_res_smooth_only = max(ch1, ch2, ch3)   # the pre-repair (defective) scope
    f_res_envelope = max(ch1, ch2, ch3_scaling_envelope)
    return {
        "kinematics": {k: float(v) for k, v in kin.items()},
        "a_over_rsat": float(a_over_rsat),
        "comp_orbit": float(comp_orbit),
        "dress_div_at_orbit_scale": float(1.0 / a_over_rsat**2),
        "speed_angular_factor": float(speed_factor),
        "CH1_retardation_flux": float(ch1),
        "CH2_graded_shell_flux": float(ch2),
        "CH2_moment_ratio_soft": float(mr_soft["moment_ratio"]),
        "CH2_moment_ratio_stiff": float(mr_stiff["moment_ratio"]),
        "CH2_closed_vs_numeric_soft": {
            "numeric": float(mr_soft["moment_ratio"]),
            "closed": float(mr_soft["closed_form"]),
        },
        "CH0_enclosed_charge": ch0,
        "CH3_field_energy_flux": float(ch3),
        "CH3_moment_ratio": float(coef * comp_orbit),
        "CH3_quadrature": quad,
        "CH3_scaling_envelope_flux": float(ch3_scaling_envelope),
        "F_res": float(f_res),
        "F_res_over_delta": float(f_res / comp["delta"]),
        "F_res_smooth_only": float(f_res_smooth_only),
        "F_res_smooth_only_over_delta": float(f_res_smooth_only
                                              / comp["delta"]),
        "F_res_envelope": float(f_res_envelope),
        "F_res_envelope_over_delta": float(f_res_envelope / comp["delta"]),
        "delta": comp["delta"],
        "dominant_channel": ["CH1", "CH2", "CH3"][
            int(np.argmax([ch1, ch2, ch3]))],
    }

# ----------------------------------------------------------------------------

def ch0_enclosed_charge_channel(comp):
    """CH-0 (Tier-2 PK-01/PK-02 repair): the ENCLOSED-CHARGE orbital
    quadrupole. The exterior dress u0 = B/r^2 is a center of dilatation:
    div u = 4*pi*B*delta^3(x) -- div-free in the exterior with NONZERO
    enclosed compression charge (the Coulomb structure), measurable purely
    on the cold side (surface flux at any r > r_sat). The compression-source
    second moment is therefore the MOVING-CHARGE quadrupole q_a X_a X_a with
    q_a proportional to m_a -- i.e. the orbital MATTER quadrupole, moment
    ratio exactly 1 relative to the shear anchor (#767's receipted multipole
    ladder: int x_i x_j div u = Q_ij, monopole/dipole conservation-killed,
    quadrupole radiates). The seal (an AC-transmission statement at the wall)
    does not screen it: per-star self-screening cannot cancel a two-body
    quadrupole formed of two separated monopoles, and canon's deep-rail
    measurement records the mass 'EXPLICITLY untouched by the image'.
    Flux = kappa_env^2 = (2/3)(c_S/c_P)^5 -- the #919 uncaged partition
    (anchored-floor structure; R24-contested anchor inherited)."""
    speed_factor = A_ANG * (1.0 / C_P_OVER_C_S) ** 5
    return {
        "moment_ratio": 1.0,
        "flux": float(speed_factor),
        "flux_over_delta": float(speed_factor / comp["delta"]),
        "flux_over_delta_sigma_form": float(speed_factor / comp["delta"]),
    }


def kappa_exact():
    """CH-3 moment coefficient, EXACT closed form (Tier-2 R-N-01 repair).

    grad A1 . grad A2 = (1/2) Lap(A1 A2) + 2*pi*(k2 A1 delta_2 + k1 A2 delta_1)
    with W = z^2 - r^2/3 harmonic and the boundary terms vanishing (the
    leading angular content of A1*A2*W has zero average), so
      num = 2*pi*(k2 * A1(x2) * W(x2) + k1 * A2(x1) * W(x1))
          = 2*pi * 2 * (k1 k2 / d) * (d^2/6) = (2*pi/3) k1 k2 d,
      den = 4*pi*k1*k2/d,   kappa = num/(d^2 den) = 1/6 EXACTLY.
    """
    return 1.0 / 6.0


def ch3_field_moment_quadrature_midpoint(m1, m2, n_mu=400, n_r=1200,
                                         r_max_over_d=2000.0):
    """CH-3 moment coefficient, INDEPENDENT numeric method: full-domain
    quadrature on a MIDPOINT-centered ball (symmetric truncation).

    Tier-2 R-N-01 (CONFIRMED CRITICAL): the original implementation doubled
    the z>0 half evaluated on a MASS-1-centered truncated ball. The halves
    are equal for the exact integral, but the mass-centered truncation
    boundary is displaced d/2 from the symmetric one, and the crescent
    between the two spheres contributes an R-INDEPENDENT artifact of exactly
    +1/24 to kappa -- which is why the defective run 'converged' to the
    clean rational 5/24 = 1/6 + 1/24. The midpoint-centered domain has no
    crescent; kappa(R) -> 1/6 with the O(d^2/R^2) truncation tail only.
    The defective implementation is retained below (renamed *_masscentered)
    as the disclosed defect exhibit; it is not consumed.
    """
    d = 1.0
    k1, k2 = 7.0 * m1, 7.0 * m2
    mu_nodes, mu_w = np.polynomial.legendre.leggauss(n_mu)
    s_nodes, s_w = np.polynomial.legendre.leggauss(n_r)
    # log-graded radial map from the midpoint, r in (0, R]
    R = r_max_over_d * d
    L = math.log1p(R / (0.01 * d))
    t = 0.5 * (s_nodes + 1.0)
    r = 0.01 * d * np.expm1(L * t)
    jac_r = 0.5 * L * 0.01 * d * np.exp(L * t) * s_w

    num = 0.0
    den = 0.0
    for ri, wr in zip(r, jac_r):
        r1sq = ri * ri - d * ri * mu_nodes + 0.25 * d * d
        r2sq = ri * ri + d * ri * mu_nodes + 0.25 * d * d
        g = k1 * k2 * (ri * ri - 0.25 * d * d) / (r1sq * r2sq) ** 1.5
        W = ri * ri * (mu_nodes * mu_nodes - 1.0 / 3.0)
        num += wr * np.sum(mu_w * g * W * ri * ri)
        den += wr * np.sum(mu_w * g * ri * ri)
    num *= 2.0 * math.pi
    den *= 2.0 * math.pi
    den_exact = 4.0 * math.pi * k1 * k2 / d
    kappa = num / (den_exact * d * d)   # exact-den normalization
    return {
        "kappa": float(kappa),
        "kappa_exact_closed_form": kappa_exact(),
        "kappa_rel_err_vs_exact": float(abs(kappa / kappa_exact() - 1.0)),
        "denominator_numeric": float(den),
        "denominator_exact_4pi_k1k2_over_d": float(den_exact),
        "denominator_rel_err": float(abs(den / den_exact - 1.0)),
        "moment_ratio_coefficient_1p5_kappa": float(1.5 * abs(kappa_exact())),
        "n_mu": n_mu, "n_r": n_r, "r_max_over_d": r_max_over_d,
    }


def ch3_field_moment_quadrature_masscentered_DEFECTIVE(
        m1, m2, n_mu=500, n_r=1600, r_max_over_d=100000.0):
    """RETAINED AS THE DISCLOSED DEFECT EXHIBIT (Tier-2 R-N-01) — NOT CONSUMED.

    Doubles the z>0 half on a MASS-1-centered truncated ball. The truncation
    crescent (displaced d/2 from the symmetric boundary) contributes exactly
    +1/24 to kappa, so this converges to 5/24 instead of the true 1/6.

    Direct spatial quadrature of the l=2 (traceless zz) moment of the two-body
    A1-sector INTERACTION field-energy density, normalized by that density's
    own volume integral. The normalization makes the result independent of the
    field-energy prefactor (the /7 chain, 4-pi conventions) -- only the
    weak-field identification of the interaction energy magnitude with
    G*m1*m2/d is imported, which canon already commits to.

        kappa = [ Int (grad A1 . grad A2) (z^2 - r^2/3) d3x ]
                / [ d^2 * Int (grad A1 . grad A2) d3x ]

    Moment ratio (compression field moment / matter shear moment):
        Q_field / (c^2 * (2/3) mu d^2) = (3/2) |kappa| * G M_tot / (d c^2)

    Instrument check (the certification of this quadrature): the DENOMINATOR
    has the exact closed value 4 pi k1 k2 / d, reproduced by the same mesh.

    Geometry: masses on the z-axis at z = +-d/2 (d = 1). The integrand is
    exactly symmetric under z -> -z, so the integral is twice the half-space
    z > 0 contribution, evaluated in spherical coordinates centred ON mass 1 --
    where the 1/r1^2 singularity is cancelled exactly by the r1^2 Jacobian and
    the mass-2 singularity lies outside the domain. No excision, no RNG.
    """
    d = 1.0
    k1, k2 = 7.0 * m1, 7.0 * m2

    # RADIAL OUTER / ANGULAR INNER. The half-space cut mu > -d/(2 r1) is a
    # boundary layer of width d/(2 r1) that narrows as r1 grows; putting mu
    # INSIDE lets its Gauss-Legendre panel span the exact interval
    # [mu_min(r1), 1] at every radius, so the O(a) angular cancellation that
    # makes the tail convergent is resolved rather than aliased.
    mu_nodes, mu_w = np.polynomial.legendre.leggauss(n_mu)
    s_nodes, s_w = np.polynomial.legendre.leggauss(n_r)

    L = math.log1p(r_max_over_d * d / d)
    t = 0.5 * (s_nodes + 1.0)
    r1_grid = d * np.expm1(L * t)
    jac_r = 0.5 * L * d * np.exp(L * t) * s_w

    num = 0.0
    den = 0.0
    for r1, wr in zip(r1_grid, jac_r):
        mu_min = max(-1.0, -d / (2.0 * r1)) if r1 > 0 else -1.0
        half = 0.5 * (1.0 - mu_min)
        mu = mu_min + half * (mu_nodes + 1.0)
        wmu = mu_w * half

        r2 = np.sqrt(d * d + 2.0 * d * r1 * mu + r1 * r1)
        # (grad A1 . grad A2) * r1^2  -- regular at r1 = 0
        f = k1 * k2 * (d * mu + r1) / r2**3
        z = 0.5 * d + r1 * mu
        rsq = 0.25 * d * d + d * r1 * mu + r1 * r1
        W = z * z - rsq / 3.0

        num += wr * np.sum(wmu * f * W)
        den += wr * np.sum(wmu * f)

    # 2 (both half-spaces) * 2*pi (azimuth)
    num *= 4.0 * math.pi
    den *= 4.0 * math.pi
    den_exact = 4.0 * math.pi * k1 * k2 / d
    kappa = num / (den * d * d)
    return {
        "kappa": float(kappa),
        "denominator_numeric": float(den),
        "denominator_exact_4pi_k1k2_over_d": float(den_exact),
        "denominator_rel_err": float(abs(den / den_exact - 1.0)),
        "moment_ratio_coefficient_1p5_kappa": float(1.5 * abs(kappa)),
        "n_mu": n_mu, "n_r": n_r, "r_max_over_d": r_max_over_d,
    }


def dpb_subwall_reversion():
    """SUPERSEDED BY CH-0 (Tier-2 PK-01): under the repaired accounting the
    enclosed-charge quadrupole fires on BOTH the walled and sub-wall branches,
    so the walled/sub-wall asymmetry this function priced no longer moves the
    verdict. Retained (with the Tier-2 R-N-09/FW-09 level-error repair: a
    MOMENT share entering a FLUX bracket enters SQUARED) as the record of the
    superseded conditional arithmetic. NOT verdict-consumed."""
    dp = COMPARATORS["DP"]
    m_a, m_b = dp["m_p"], dp["m_c"]
    share = m_a / (m_a + m_b)
    share_sq = share * share
    lo, hi = 0.0152 * share_sq, 0.0455 * share_sq
    return {
        "moment_share_mA_over_M": share,
        "flux_share_squared": share_sq,
        "reverted_floor": [lo, hi],
        "reverted_floor_over_deltaDP": [lo / dp["delta"], hi / dp["delta"]],
        "superseded_by": "CH0_enclosed_charge (fires on both branches)",
    }


def main():
    theta_soft = theta_ode("soft")
    theta_stiff = theta_ode("stiff_K")
    results = {
        "_driver": "screening_theorem.py",
        "_prereg": "research/2026-08-09_screening-theorem_prereg-FROZEN.md",
        "constants": {
            "GM_sun_over_c2_km": GM_SUN_OVER_C2_KM,
            "c_km_s": C_KM_S,
            "c_P_over_c_S": C_P_OVER_C_S,
            "A_ang": A_ANG,
            "R_NS_band_km": list(R_NS_BAND_KM),
        },
        "ns_wall": ns_wall_arm(),
        "theta_receipt_soft": theta_soft,
        "theta_receipt_stiff": theta_stiff,
        "residue_HT": residue("HT"),
        "residue_DP": residue("DP"),
        "dpb_subwall_reversion": dpb_subwall_reversion(),
    }
    out = os.path.join(os.path.dirname(__file__),
                       "screening_theorem_results.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=1, sort_keys=True)
    print(json.dumps({
        "ns_wall_flip_radii_km": {k: v["r_sat_km"]
                                  for k, v in results["ns_wall"].items()},
        "F_res_DP": results["residue_DP"]["F_res"],
        "F_res_DP_over_deltaDP": results["residue_DP"]["F_res_over_delta"],
        "F_res_HT": results["residue_HT"]["F_res"],
        "theta_over_epsdev_at_2rsat_soft":
            theta_soft["samples"]["r=2.0"]["theta_over_epsdev"],
        "dominant_channel_DP": results["residue_DP"]["dominant_channel"],
    }, indent=1))


if __name__ == "__main__":
    main()
