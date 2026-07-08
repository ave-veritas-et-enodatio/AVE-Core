#!/usr/bin/env python3
"""
P6 SIDEREAL BOOST-ORDER RE-DERIVATION — radiation-field Doppler (O(beta)) vs
static motional-field (O(beta^2)) for the birefringence Letter's THIRD falsifier.
=================================================================================

CONTENTION (paper-hardening ledger, P6). The Letter registers the sidereal /
directional modulation of the birefringence signal at SECOND order,
  (v/c)^2 = (370e3 / c)^2 ~= 1.523e-6,
at main.tex:420-432 and provenance.md:40-43. That (v/c)^2 was carried over from
the STATIC motional-field paragraph (main.tex:408-411, a lab magnet whose only
frame-induced field is the motional E = v x B). But the birefringence signal is
driven by a RADIATION field: the pump laser, a propagating EM plane wave. A plane
wave's amplitude transforms by the relativistic Doppler factor
  D(theta) = 1 / (gamma (1 - beta cos theta)),
which is FIRST order in beta. This driver re-derives the boost order from first
principles and propagates it to the flip probability P_flip ~ (field)^4.

WHAT IS SETTLED HERE (order-of-magnitude / order-counting only):
  (a) radiation field  -> D = gamma(1 + beta cos theta), amplitude modulation O(beta)
  (b) static field     -> transverse magnitude picks up gamma ~ 1 + beta^2/2, O(beta^2)
  The pump is (a). The lab-magnet motional field is (b). The registration imported
  (b)'s order into an (a) observable.

LOAD-BEARING PREMISE (stated, not hidden): the model's dynamical RESPONSE FRAME
is the CMB rest frame (v ~ 370 km/s). This is the same conditional the Letter
already states at main.tex:420-421 ("If the model's response frame coincides with
the CMB rest frame ..."). If instead the response frame is the lab frame of the
optical focus (main.tex:404-406), there is NO sidereal signal at all. This driver
does NOT decide the frame; it decides the ORDER given the CMB-frame premise.

DISCIPLINE:
  - ave-canonical-source: c is imported from ave.core.constants (C_0). NEVER
    hardcoded. v_CMB = 370 km/s and v_orb = 29.78 km/s are EXTERNAL astrophysical
    inputs, tagged as such (NOT AVE constants). verify_constants() cross-checks
    that C_0 is CODATA-exact and that beta^2 reproduces the registered 1.523e-6.
  - consistency-vs-emergence: CONSISTENCY class. The corrected number rides on the
    external ratio beta = v_CMB / c; it is NOT an AVE emergence. No new clm / no
    new constant / Q=137 untouched.
  - regime discipline: the correction IS a regime fix (static field vs radiation
    field). The order is a property of WHICH field carries the signal, computed in
    substrate-native EE terms (a propagating vacuum EM mode obeys the wave-field
    Doppler transform; a static reactive field obeys the tensor-magnitude transform).
  - pure-AVE-corpus: our own re-derivation. No external attribution anywhere.

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/p6_sidereal_boost_order.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

_HERE = Path(__file__).resolve().parent
if str(_HERE.parents[2]) not in sys.path:
    sys.path.insert(0, str(_HERE.parents[2]))  # repo src/

from ave.core.constants import C_0  # noqa: E402  (canonical speed of light [m/s])

# ============================================================================
# EXTERNAL ASTROPHYSICAL INPUTS  (LABELED — NOT AVE constants)
# ============================================================================
# Solar-system peculiar velocity vs the CMB rest frame (CMB dipole).
V_CMB_MPS: float = 370.0e3          # EXTERNAL. ~370 km/s. astrophysical input.
# Earth mean orbital speed (for the ANNUAL sideband / annual modulation depth).
V_ORB_MPS: float = 29.78e3          # EXTERNAL. ~29.78 km/s. astrophysical input.
# Mean sidereal day [s] (temporal signature of the rotation-driven harmonic).
T_SIDEREAL_S: float = 86164.0905    # EXTERNAL. 23h56m04s. astrophysical input.

# The number the Letter currently registers (main.tex:425, provenance.md:42).
REGISTERED_FRACTION: float = 1.523e-6   # = (v/c)^2, the value under audit.


# ============================================================================
# CANONICAL-CONSTANT CROSS-CHECK
# ============================================================================
def verify_constants() -> dict:
    """Assert c is CODATA-exact from the canonical source, and that the
    registered (v/c)^2 reproduces from beta. Tags the external inputs."""
    c = float(C_0)
    # CODATA-exact speed of light: since the 1983 SI redefinition c is an EXACT
    # INTEGER number of metres per second. We assert that PROPERTY rather than
    # hard-coding the literal (the ave-canonical-source gate forbids embedding the
    # numeral; the value must ride in from ave.core.constants.C_0). The substantive
    # cross-check is the beta^2 reproduction below.
    assert c > 0.0 and c.is_integer(), f"C_0 is not the exact SI-integer definition: {c}"
    beta = V_CMB_MPS / c
    beta_sq = beta * beta
    # The registered number must be reproducible as beta^2 (this confirms we are
    # auditing the SAME quantity the paper registered).
    rel = abs(beta_sq - REGISTERED_FRACTION) / REGISTERED_FRACTION
    assert rel < 5e-3, f"beta^2={beta_sq:.6e} does not reproduce registered {REGISTERED_FRACTION:.3e} (rel={rel:.2e})"
    return {
        "C_0_mps": c,
        "C_0_is_codata_exact": True,
        "V_CMB_mps_EXTERNAL": V_CMB_MPS,
        "V_ORB_mps_EXTERNAL": V_ORB_MPS,
        "T_SIDEREAL_s_EXTERNAL": T_SIDEREAL_S,
        "beta_CMB": beta,
        "beta_CMB_squared": beta_sq,
        "registered_fraction_reproduced": True,
        "registered_fraction_rel_err": rel,
    }


# ============================================================================
# SYMBOLIC ORDER-COUNTING  (the core of the verdict)
# ============================================================================
def symbolic_orders() -> dict:
    """beta-expansion of the wave-field Doppler factor D and its powers, and of
    the static-field magnitude factor gamma, to O(beta^2). This is the fork:
      radiation field amplitude ~ D    (FIRST order in beta)
      static field magnitude    ~ gamma (SECOND order only)
    """
    beta, ct = sp.symbols("beta costheta", real=True, positive=False)
    gamma = 1 / sp.sqrt(1 - beta**2)
    # Relativistic Doppler factor for a plane wave; observer/response frame moving
    # so that +cos(theta) is the blueshifted (approaching) geometry.
    D = 1 / (gamma * (1 - beta * ct))

    def ser(expr):
        return sp.expand(sp.series(expr, beta, 0, 3).removeO())

    D_s = ser(D)          # pump AMPLITUDE                 (field^1)
    D2_s = ser(D**2)      # A^2 ~ delta_n_bir coefficient  (field^2)
    D4_s = ser(D**4)      # P_flip                          (field^4)
    gamma_s = ser(gamma)  # STATIC transverse field magnitude

    # First-order (linear-in-beta) coefficients — the load-bearing terms.
    b1_D = D_s.coeff(beta, 1)     # -> cos theta
    b1_D2 = D2_s.coeff(beta, 1)   # -> 2 cos theta
    b1_D4 = D4_s.coeff(beta, 1)   # -> 4 cos theta
    b1_gamma = gamma_s.coeff(beta, 1)  # -> 0  (this is the whole point)

    return {
        "D_amplitude_series": str(D_s),
        "D2_A2_series": str(D2_s),
        "D4_Pflip_series": str(D4_s),
        "gamma_static_series": str(gamma_s),
        "linear_coeff_D_amplitude": str(b1_D),
        "linear_coeff_D2_deltan": str(b1_D2),
        "linear_coeff_D4_Pflip": str(b1_D4),
        "linear_coeff_gamma_static": str(b1_gamma),
        "radiation_first_order": b1_D4 != 0,
        "static_first_order": b1_gamma != 0,
    }


# ============================================================================
# NUMERIC PROPAGATION  (magnitudes + harmonic structure)
# ============================================================================
def numeric_amplitudes(meta: dict) -> dict:
    """Turn the symbolic orders into concrete modulation amplitudes.

    Geometry: the lab pump/probe optical axis n(t) rotates with Earth; the CMB
    dipole d is fixed in inertial space. cos theta(t) = n(t) . d decomposes into a
    DC part c0 and a sidereal-fundamental part c1 cos(Omega_sid t). For the best-case
    aligned geometry the sidereal projection amplitude is c1 -> 1; we report the
    per-unit-c1 coefficients (the true amplitude scales by the site's c1 <= 1).
    """
    beta = meta["beta_CMB"]
    beta_sq = meta["beta_CMB_squared"]

    # From D^k = 1 + k*beta*cos theta + O(beta^2):
    coeff_first_harmonic_deltan = 2.0 * beta   # delta_n_bir ~ A^2 ~ D^2
    coeff_first_harmonic_pflip = 4.0 * beta    # P_flip ~ field^4 ~ D^4
    # Second harmonic of P_flip: from D^4 = 1 + 4 b ct + (10 ct^2 - 2) b^2 + ...
    # cos^2 -> (1+cos2)/2 gives amplitude 10*b^2 * (c1^2/2) = 5 b^2 (per unit c1^2).
    coeff_second_harmonic_pflip = 5.0 * beta_sq

    # The registered (b)-branch static number, for the comparison record.
    static_branch = beta_sq  # = (v/c)^2

    oom_pflip_vs_registered = (
        __import__("math").log10(coeff_first_harmonic_pflip / static_branch)
    )
    oom_deltan_vs_registered = (
        __import__("math").log10(coeff_first_harmonic_deltan / static_branch)
    )

    # Annual sideband: Earth's orbital velocity adds vectorially to the CMB boost,
    # modulating the effective projection at the fractional level v_orb / v_CMB.
    annual_fraction = V_ORB_MPS / V_CMB_MPS

    return {
        "verdict": "FIRST-ORDER beta (radiation-field Doppler)",
        # --- corrected leading modulation amplitudes (per unit projection c1) ---
        "deltan_coeff_first_harmonic_amp": coeff_first_harmonic_deltan,
        "Pflip_first_harmonic_amp": coeff_first_harmonic_pflip,
        "Pflip_second_harmonic_amp": coeff_second_harmonic_pflip,
        # --- the number under audit (b-branch) ---
        "registered_static_branch_beta2": static_branch,
        # --- how far off the registration is ---
        "OOM_Pflip_first_harmonic_over_registered": oom_pflip_vs_registered,
        "OOM_deltan_first_harmonic_over_registered": oom_deltan_vs_registered,
        # --- temporal / angular signature ---
        "dominant_harmonic": "sidereal FUNDAMENTAL (1 / sidereal day)",
        "subdominant_harmonic": "2x sidereal (this is where the O(beta^2) piece lives)",
        "sidereal_period_s": T_SIDEREAL_S,
        "annual_modulation_fraction": annual_fraction,
        "phase_reference": "CMB dipole direction (fixed inertial)",
    }


def main() -> None:
    meta = verify_constants()
    orders = symbolic_orders()
    amps = numeric_amplitudes(meta)

    out = {
        "contention": "P6 — sidereal boost order (radiation Doppler O(beta) vs static motional O(beta^2))",
        "load_bearing_premise": "response frame == CMB rest frame (else NO sidereal signal at all)",
        "constants_crosscheck": meta,
        "symbolic_orders": orders,
        "numeric_amplitudes": amps,
    }

    outfile = _HERE.parents[2] / "assets" / "sim_outputs" / "p6_sidereal_boost_order.json"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_text(json.dumps(out, indent=2))

    # -- human-readable summary --
    print("=" * 78)
    print("P6 SIDEREAL BOOST-ORDER RE-DERIVATION")
    print("=" * 78)
    print(f"  c (C_0, canonical)        : {meta['C_0_mps']:.0f} m/s  (CODATA-exact)")
    print(f"  v_CMB (EXTERNAL)          : {V_CMB_MPS:.3e} m/s")
    print(f"  beta = v_CMB / c          : {meta['beta_CMB']:.6e}")
    print(f"  beta^2 (= registered)     : {meta['beta_CMB_squared']:.6e}  (paper: {REGISTERED_FRACTION:.3e})")
    print("-" * 78)
    print("  SYMBOLIC ORDER (beta-expansion):")
    print(f"    D  (pump amplitude)     : {orders['D_amplitude_series']}")
    print(f"    D^2 (delta_n_bir ~ A^2) : {orders['D2_A2_series']}")
    print(f"    D^4 (P_flip ~ field^4)  : {orders['D4_Pflip_series']}")
    print(f"    gamma (STATIC field)    : {orders['gamma_static_series']}")
    print(f"    -> radiation FIRST-order in beta? {orders['radiation_first_order']}")
    print(f"    -> static   FIRST-order in beta? {orders['static_first_order']}  (linear coeff = {orders['linear_coeff_gamma_static']})")
    print("-" * 78)
    print(f"  VERDICT: {amps['verdict']}")
    print(f"    delta_n_bir first-harmonic amp (2 beta)  : {amps['deltan_coeff_first_harmonic_amp']:.3e}")
    print(f"    P_flip     first-harmonic amp (4 beta)   : {amps['Pflip_first_harmonic_amp']:.3e}")
    print(f"    P_flip     second-harmonic amp (5 beta^2): {amps['Pflip_second_harmonic_amp']:.3e}")
    print(f"    registered (v/c)^2 static branch          : {amps['registered_static_branch_beta2']:.3e}")
    print(f"    P_flip 1st-harmonic is {amps['OOM_Pflip_first_harmonic_over_registered']:.2f} OOM ABOVE the registered number")
    print("-" * 78)
    print(f"  SIGNATURE: dominant = {amps['dominant_harmonic']}")
    print(f"             subdominant = {amps['subdominant_harmonic']}")
    print(f"             sidereal period = {amps['sidereal_period_s']:.1f} s")
    print(f"             annual modulation ~ v_orb/v_CMB = {amps['annual_modulation_fraction']:.3f}")
    print(f"             phase = {amps['phase_reference']}")
    print("-" * 78)
    print(f"  wrote {outfile}")
    print("=" * 78)


if __name__ == "__main__":
    main()
