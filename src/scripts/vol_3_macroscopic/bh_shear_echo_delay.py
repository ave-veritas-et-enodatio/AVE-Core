"""BH shear-echo round-trip delay — forward-prereg driver.

Backs PRONG 1 of `research/2026-06-17_bh-shear-echo-forward-prereg.md`
(FROZEN, SHA-pinned to main @ 04bcb4ac).

Physics (settled, cited — not re-derived here):
  - shear/GW reflector at  r_sat = 7 G M / c^2 = 3.5 r_s = r_s / nu_vac
        (ave-bh-horizon-area-theorem.md:16; nu_vac = 2/7)
  - principal radial strain  eps_11(r) = 7 G M /(c^2 r) = r_sat / r
        (electron-bh-isomorphism.md:19), so eps_11(r_sat) = 1 exactly
  - shear group velocity  c_shear(r) = c (1 - eps_11^2)^(1/4) -> 0 at r_sat
        (electron-bh-isomorphism.md:33)

The round-trip ("tortoise") echo delay between the inner Gamma_shear = -1 wall
at r_sat and an outer turning point r_out:

    Dt = 2 * integral_{r_sat}^{r_out}  dr / c_shear(r)

The integrand diverges at r_sat (c_shear -> 0) but the integral is FINITE
(integrand ~ x^{-1/4} near the wall, exponent > -1 => integrable). This driver
evaluates Dt for the GW150914 remnant and reports the parameter-free delay band
+ the r_out required to reach the retrospective Abedi+ 0.29 s spacing.

substrate-first: G, C_0, M_SUN come from ave.core.constants (CODATA / IAU inputs,
tagged consistency-class); nu_vac = 2/7 is the parameter-free substrate input.
"""

from __future__ import annotations

import json

import numpy as np
from scipy import integrate, optimize

from ave.core import constants as K

# --- canonical constants (ave-canonical-source: import, never hard-code) ---
G = K.G            # 6.67430e-11  m^3/(kg s^2)  [CODATA input]
C = K.C_0          # 299792458.0  m/s            [defined]
MSUN = K.M_SUN     # 1.989e30 kg                 [IAU nominal input]
NU_VAC = K.NU_VAC  # 2/7                          [substrate, parameter-free]

# GW150914 final remnant mass (corpus value, ave-merger-ringdown-eigenvalue.md:58)
M_GW150914 = 62.0 * MSUN

# Retrospective Abedi-Dykaar-Afshordi echo spacing (existing-experimental-signatures.md:42)
DT_OBSERVED = 0.290  # s


def r_g(M: float) -> float:
    """Gravitational radius GM/c^2."""
    return G * M / C**2


def r_sat(M: float) -> float:
    """AVE shear/bulk reflector radius = 7 GM/c^2 = r_s / nu_vac."""
    return (2.0 / NU_VAC) * r_g(M)  # 2/nu_vac = 7


def eps11(r: float, M: float) -> float:
    """Principal radial strain = r_sat / r; equals 1 at r_sat."""
    return r_sat(M) / r


def c_shear(r: float, M: float) -> float:
    """Shear group velocity c (1 - eps_11^2)^(1/4); -> 0 at r_sat."""
    e = np.clip(eps11(r, M), 0.0, 1.0)
    return C * (1.0 - e**2) ** 0.25


def echo_delay(M: float, r_out_over_r_sat: float) -> float:
    """Round-trip shear-echo delay r_sat -> r_out -> r_sat (seconds).

    Quadrature handles the integrable x^{-1/4} singularity at the inner wall
    via the `points` hint at r_sat.
    """
    rs = r_sat(M)
    r_out = r_out_over_r_sat * rs
    val, _ = integrate.quad(
        lambda r: 1.0 / c_shear(r, M), rs, r_out, points=[rs], limit=400
    )
    return 2.0 * val


def r_out_for_target(M: float, target_dt: float) -> float:
    """Solve for r_out/r_sat that reproduces target_dt (the 'what it would take' number)."""
    return optimize.brentq(
        lambda fac: echo_delay(M, fac) - target_dt, 1.0001, 1.0e6, xtol=1e-6
    )


def main() -> None:
    M = M_GW150914
    rg = r_g(M)
    rs = r_sat(M)
    flat = 2.0 * rs / C  # naive light-crossing reference

    band = {f"{fac:g}": echo_delay(M, fac) for fac in (1.1, 1.5, 2.0, 3.0)}
    fac_for_obs = r_out_for_target(M, DT_OBSERVED)

    out = {
        "remnant_mass_Msun": M / MSUN,
        "r_g_m": rg,
        "r_s_m": 2.0 * rg,
        "r_sat_m": rs,
        "r_sat_over_r_s": rs / (2.0 * rg),
        "flat_light_crossing_2rsat_over_c_s": flat,
        "echo_delay_band_s": band,
        "echo_delay_band_ms": {k: v * 1e3 for k, v in band.items()},
        "observed_abedi_spacing_s": DT_OBSERVED,
        "ratio_observed_over_flat": DT_OBSERVED / flat,
        "r_out_over_r_sat_for_0p29s": fac_for_obs,
        "r_out_over_r_g_for_0p29s": fac_for_obs * rs / rg,
        "verdict": (
            "FORCED (parameter-free ~3-10 ms); DISAGREES with retrospective "
            "0.29 s by ~68x; no free knob to bridge the gap (cf GR-ECO "
            "log-divergent tunable delay)."
        ),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
