#!/usr/bin/env python3
"""Q1 pulsar-timing budget + exact bulk/shear quadrupole flux prefactor.

Reproducible arithmetic for the derivation
    research/2026-07-20_q1-pulsar-hardening.md

This driver HARDENS the scalar-GW bulk-channel exposure (#750,
research/2026-07-20_scalar-gw-bulk-channel_derivation.md) against the
binary-pulsar radiative test, and pins the O(1) angular prefactor that #750
FLAG-B left bracketed.

Discipline
----------
* FORMS are derived analytically in the companion doc; every dimensionful VALUE
  printed is CODATA/astro/observation-IMPORTED and tagged in the JSON
  `provenance` field (consistency-vs-emergence: consistency-class, NOT
  emergence). Mints no canon; computes no new physics primitive.
* Channel speeds are DERIVED from the canon constitutive constants
  (`ave.core.constants`, K = 2G magic angle) read-only; not hardcoded ratios.
* The pulsar-timing agreement figures (HT, double pulsar) are IMPORTED with
  citations and tagged [import]; exact-figure re-verification is an owed check
  (see companion doc §OWED).

What it computes
----------------
1. The three channel speeds from canon (K = 2G):
     c_shear = sqrt(G/rho)           = c        (observed-GW / T2 shear channel)
     c_bulk  = sqrt(2 G/rho)         = sqrt2 c   (A1 bulk PORT mode; V_LONG)
     c_P     = sqrt((K + 4G/3)/rho)  = sqrt(10/3) c (radiative P-wave; FLAG-A)
2. The EXACT bulk/shear quadrupole flux prefactor (the #750 owed FLAG-B follow-on):
     F_bulk/F_shear = A_ang * (c_shear/c_long)^5
   where A_ang = 2/3 is the isotropic-elastic P-vs-S angular-partition factor of
   a mass-quadrupole moment tensor (derived in the companion doc; the P/S
   projection integrals give 8pi/15 and 4pi/5 respectively, ratio 2/3).
3. The pulsar-timing exclusion significance for Reading A (bulk radiates):
   an extra flux fraction F over-predicts Pbdot by (1+F); compared to the
   observed GR agreement (fractional precision `delta`), the tension is F/delta.
"""
from __future__ import annotations

import json
import math
import os

from ave.core import constants as C

# ---------------------------------------------------------------------------
# 1. Channel speeds derived from canon constitutive constants (K = 2G).
# ---------------------------------------------------------------------------
G = C.G_VAC          # shear modulus  [canon]
RHO = C.RHO_BULK     # bulk density   [canon]
K = 2.0 * G          # K = 2G magic-angle bulk modulus (GR-imported; PR#261) [canon]

c_shear = math.sqrt(G / RHO)                 # = C_0
c_bulk_port = math.sqrt(K / RHO)             # = V_LONG = sqrt(2) c   (A1 port mode)
c_P = math.sqrt((K + 4.0 * G / 3.0) / RHO)   # = sqrt(10/3) c  (radiative P-wave)

# Sanity: dimensionless speed ratios (must be 1, sqrt2, sqrt(10/3)).
r_bulk_port = c_bulk_port / c_shear
r_P = c_P / c_shear

# ---------------------------------------------------------------------------
# 2. Exact bulk/shear quadrupole flux prefactor.
#    Isotropic-elastic P-vs-S angular partition of a mass-quadrupole source:
#      P-channel angular integral  : oint |gamma_i gamma_j Q_ij|^2 dOmega = (8pi/15)|Q|^2
#      S-channel angular integral  : oint |(delta-gamma gamma) . (gamma.Q)|^2 = (4pi/5)|Q|^2
#      ratio  A_ang = (8pi/15)/(4pi/5) = 2/3
#    Full flux ratio (same moment tensor, equal coupling):
#      F_bulk/F_shear = A_ang * (c_shear/c_long)^5
# ---------------------------------------------------------------------------
A_ANG = (8.0 / 15.0) / (4.0 / 5.0)  # = 2/3, derived P/S angular-partition factor


def speed_factor(c_long: float) -> float:
    """(c_shear/c_long)^5 -- the calibration-free multipole speed suppression."""
    return (c_shear / c_long) ** 5


def flux_ratio(c_long: float, a_ang: float = A_ANG, coupling_sq: float = 1.0) -> float:
    """F_bulk/F_shear = coupling^2 * A_ang * (c_shear/c_long)^5."""
    return coupling_sq * a_ang * speed_factor(c_long)


# Headline set: A_ang = 2/3 (derived), equal coupling (elastic-medium default).
F_port = flux_ratio(c_bulk_port)   # sqrt(2) c  port speed
F_pwave = flux_ratio(c_P)          # sqrt(10/3) c  radiative P-wave speed

# Honest bracket over the O(1) angular/coupling uncertainty (consensus knife both ways):
#   low  : A_ang = 0.3 (spin-structure conservative) * P-wave speed
#   high : A_ang = 1.0 * port speed
F_min = flux_ratio(c_P, a_ang=0.30)
F_max = flux_ratio(c_bulk_port, a_ang=1.0)

# ---------------------------------------------------------------------------
# 3. Pulsar-timing exclusion significance.
#    Observed Pbdot / GR-Pbdot agreement, fractional 1-sigma precision `delta`.
#    An extra radiative channel makes Pbdot -> (1 + F) * Pbdot_GR, so an
#    admixture F is in tension at F/delta sigma-equivalent.
# ---------------------------------------------------------------------------
# [import] Hulse-Taylor B1913+16: Weisberg & Huang 2016, ApJ 829, 55
#   (arXiv:1606.02744): observed/GR = 0.9983 +/- 0.0016  -> 1-sigma frac = 0.0016.
HT_RATIO = 0.9983
HT_SIGMA = 0.0016
# [import] Double pulsar J0737-3039A/B: Kramer et al. 2021, PRX 11, 041050
#   (arXiv:2112.06795): GR quadrupolar GW prediction validated at 1.3e-4 (95% conf).
#   Treated as a fractional bound; presented as "factor over the bound" to avoid a
#   1-sigma-vs-2-sigma ambiguity (95% conf ~ 2 sigma, so a 1-sigma read is tighter).
DP_BOUND = 1.3e-4


def ht_sigma(F: float) -> float:
    return F / HT_SIGMA


def dp_factor(F: float) -> float:
    return F / DP_BOUND


results = {
    "provenance": {
        "class": "research-driver (Q1 pulsar hardening); mints no canon; no engine edit",
        "speeds": "DERIVED from ave.core.constants (K=2G); dimensionless ratios",
        "A_ang": "DERIVED (isotropic-elastic P/S angular partition = 2/3)",
        "coupling": "equal-coupling = elastic-medium default; O(1) per #750 (K=2G, no 1/omega_BD)",
        "HT": "[import] Weisberg & Huang 2016 arXiv:1606.02744 (WebFetch-verified 2026-07-20)",
        "DP": "[import] Kramer et al. 2021 arXiv:2112.06795 (WebFetch-verified 2026-07-20)",
    },
    "speeds_over_c": {
        "c_shear": c_shear / C.C_0,
        "c_bulk_port_over_c": r_bulk_port,
        "c_P_over_c": r_P,
        "check_sqrt2": math.sqrt(2.0),
        "check_sqrt_10_3": math.sqrt(10.0 / 3.0),
    },
    "speed_factor_power": {
        "sqrt2_port": speed_factor(c_bulk_port),      # 2^-2.5
        "sqrt_10_3_pwave": speed_factor(c_P),         # (3/10)^2.5
    },
    "A_ang": A_ANG,
    "A_ang_mc": None,  # filled in main()
    "flux_ratio_F_bulk_over_F_shear": {
        "headline_port_sqrt2": F_port,
        "headline_pwave_sqrt_10_3": F_pwave,
        "bracket_min": F_min,
        "bracket_max": F_max,
    },
    "exclusion_hulse_taylor_sigma": {
        "port_sqrt2": ht_sigma(F_port),
        "pwave_sqrt_10_3": ht_sigma(F_pwave),
        "bracket_min": ht_sigma(F_min),
        "bracket_max": ht_sigma(F_max),
    },
    "exclusion_double_pulsar_factor_over_bound": {
        "port_sqrt2": dp_factor(F_port),
        "pwave_sqrt_10_3": dp_factor(F_pwave),
        "bracket_min": dp_factor(F_min),
        "bracket_max": dp_factor(F_max),
    },
}




def mc_a_ang(n: int = 4_000_000, seed: int = 424242) -> float:
    """Monte-Carlo verification of A_ang = I_P/I_S (review-repair R1: the shipped
    second method for the 2/3 angular partition; analytic value at A_ANG above)."""
    import numpy as np
    rng = np.random.default_rng(seed)
    # generic traceless-symmetric test tensor (asymmetric entries)
    M = np.array([[0.7, 0.31, -0.12], [0.31, -0.45, 0.53], [-0.12, 0.53, -0.25]])
    M = 0.5 * (M + M.T)
    M -= np.eye(3) * np.trace(M) / 3.0
    v = rng.normal(size=(n, 3))
    g = v / np.linalg.norm(v, axis=1, keepdims=True)
    Mg = g @ M
    long_amp = np.einsum("ij,ij->i", g, Mg)          # γ·M·γ  (P projection)
    full_sq = np.einsum("ij,ij->i", Mg, Mg)          # |M·γ|²
    i_p = float(np.mean(long_amp ** 2))
    i_s = float(np.mean(full_sq - long_amp ** 2))
    return i_p / i_s

def main() -> None:
    results["A_ang_mc"] = mc_a_ang()
    print("Q1 pulsar-timing budget + exact bulk/shear flux prefactor")
    print("=" * 64)
    print(f"c_bulk_port/c   = {r_bulk_port:.6f}  (expect sqrt2   = {math.sqrt(2):.6f})")
    print(f"c_P/c           = {r_P:.6f}  (expect sqrt10/3 = {math.sqrt(10/3):.6f})")
    print(f"A_ang (P/S)     = {A_ANG:.6f}  (= 2/3)")
    print("-" * 64)
    print(f"speed factor (c_s/c_long)^5 : sqrt2 = {speed_factor(c_bulk_port):.6f}"
          f" | sqrt10/3 = {speed_factor(c_P):.6f}")
    print(f"F_bulk/F_shear headline     : port(sqrt2) = {F_port:.5f}"
          f" | P-wave(sqrt10/3) = {F_pwave:.5f}")
    print(f"F_bulk/F_shear bracket      : [{F_min:.5f}, {F_max:.5f}]")
    print("-" * 64)
    print("Reading-A exclusion (extra flux F over-predicts Pbdot by 1+F):")
    print(f"  Hulse-Taylor (1sig={HT_SIGMA}):  "
          f"port={ht_sigma(F_port):.1f}sig  P-wave={ht_sigma(F_pwave):.1f}sig  "
          f"bracket=[{ht_sigma(F_min):.1f},{ht_sigma(F_max):.1f}]sig")
    print(f"  Double pulsar (bound={DP_BOUND:g}): "
          f"port={dp_factor(F_port):.0f}x  P-wave={dp_factor(F_pwave):.0f}x  "
          f"bracket=[{dp_factor(F_min):.0f},{dp_factor(F_max):.0f}]x the bound")

    out = os.path.join(os.path.dirname(__file__), "q1_pulsar_timing_budget_results.json")
    with open(out, "w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
