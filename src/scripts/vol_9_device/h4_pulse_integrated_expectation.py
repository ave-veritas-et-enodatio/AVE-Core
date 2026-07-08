#!/usr/bin/env python3
"""
H4 — Table I PULSE-INTEGRATED EXPECTATION for the BIREF@HIBEF Letter.
=====================================================================

Table I of the Letter (papers/2026_birefringence_letter/main.tex) quotes the
polarization-flip probability P_flip on the PEAK-FIELD (envelope-maximum)
convention: the peak carrier amplitude E = sqrt(2 I / (c eps0)) at the pump peak
intensity. A pump-probe shot does not sit at the peak everywhere; it integrates
the flip probability over the pump's Gaussian temporal and transverse focal
envelope. This driver supplies the OWED pulse-integrated expectation so no
experimentalist chases a spurious factor.

METHOD (stated so it is auditable, not adopted from any external estimate):
  * The flip probability is P_flip = sin^2(dphi/2) with dphi proportional to the
    index shift dn ~ -1/2 A^2 ~ I. In the small-angle (demonstrated-pump) regime
    P_flip ~ (dphi/2)^2 ~ I^2, so the pulse-integrated expectation is the PEAK
    value scaled by a dimensionless ENVELOPE FORM FACTOR
        F_env = <I^2> / I_peak^2 ,
    the fluence-weighted (probe-photon-weighted, co-focused) average over the
    pump envelope.
  * For a Gaussian temporal profile and a Gaussian transverse (2D) focal profile
    the envelope is a 3-dimensional Gaussian. The fluence-weighted mean of any
    power of the intensity over a D-dimensional Gaussian is width-INDEPENDENT:
        <I^n>_fluence / I_peak^n = (n+1)^(-D/2)   (weight w = I, so n->n+1 below),
    giving F_env = <I^2>_w / I_peak^2 = 3^(-D/2). For D = 3 (temporal + 2D focal),
        F_env = 3^(-3/2) = 1/(3 sqrt 3) ~ 0.19245  (EXACT, closed form).
  * A numerical quadrature of the EXACT fluence-weighted <sin^2(dphi(I)/2)>
    cross-checks the small-angle F_env method (they agree to <1% because the
    demonstrated-pump peak retardance dphi/2 <~ 0.074 is deep in the small-angle
    regime).

DISCIPLINE:
  * ave-canonical-source: E-field, wavelength, dn, dphi, P_flip all flow through
    the SAME GAP-1 readout chain (single source of truth,
    birefringence_gap1_hibef_feasibility) that produced Table I; every constant
    imports from ave.core.constants. No hardcoded physics.
  * consistency-vs-emergence: CONSISTENCY-class. This is a readout-convention
    audit of an existing prediction, not a new claim/constant/emergence. The
    envelope form factor is a pure geometry number (Gaussian moment ratio).
  * OUR number is the peak column x F_env computed here; no external estimate is
    adopted.

Run: PYTHONPATH=src python3 src/scripts/vol_9_device/h4_pulse_integrated_expectation.py
Artifact: src/scripts/vol_9_device/_output/h4_pulse_integrated_expectation.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy import integrate

_HERE = Path(__file__).resolve().parent
if str(_HERE.parents[2]) not in sys.path:
    sys.path.insert(0, str(_HERE.parents[2]))  # repo src/
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))             # sibling import

from birefringence_gap1_hibef_feasibility import (  # noqa: E402
    Z_INTERACTION_M,
    field_from_intensity_wcm2,
    hibef_point,
)

from ave.core.constants import E_YIELD  # noqa: E402

# The three DEMONSTRATED-pump scenarios frozen in Table I (probe energy [eV]).
# Pump = 1e21 W/cm^2 (ReLaX demonstrated). Peak-field convention.
I_DEMONSTRATED_WCM2: float = 1e21
DEMONSTRATED_PROBES_EV: tuple[tuple[str, float], ...] = (
    ("conventional", 9835.0),
    ("dark-field", 8766.0),
    ("high-energy", 12914.0),
)

# Envelope dimensionality: temporal (1) + transverse focal (2D Gaussian beam).
ENVELOPE_DIM: int = 3


def envelope_form_factor_analytic(dim: int = ENVELOPE_DIM) -> float:
    """Fluence-weighted <I^2>/I_peak^2 over a matched dim-D Gaussian envelope.

    Width-independent: for a positive-definite quadratic form Q,
    integral exp(-a Q) d^dim x ~ a^(-dim/2), so with fluence weight w = I ~ exp(-Q),
    <I^2>_w / I_peak^2 = (integral exp(-3Q)) / (integral exp(-Q)) = 3^(-dim/2).
    """
    return float(3.0 ** (-dim / 2.0))


def envelope_form_factor_quadrature(dim: int = ENVELOPE_DIM) -> float:
    """Same F_env by 1D quadrature over the intensity variable g = I/I_peak.

    Over a dim-D isotropic Gaussian the co-area density of the level set g is
        rho(g) = g^(-1) (-ln g)^(dim/2 - 1)     (the 1/g is the level-set Jacobian).
    A fluence-weighted (weight w = I = g) average of a quantity Q(g) is then
        <Q>_w = integral_0^1 Q(g) * g * rho(g) dg / integral_0^1 g * rho(g) dg .
    For Q = I^2 = g^2 this gives 3^(-dim/2); computed numerically here as a
    cross-check of the closed form.
    """
    p = dim / 2.0 - 1.0

    def num(g: float) -> float:  # Q = g^2 : integral g^2 (-ln g)^p dg
        return (g ** 2) * ((-np.log(g)) ** p)

    def den(g: float) -> float:  # integral (-ln g)^p dg
        return (-np.log(g)) ** p

    n_val, _ = integrate.quad(num, 0.0, 1.0)
    d_val, _ = integrate.quad(den, 0.0, 1.0)
    return float(n_val / d_val)


def pulse_integrated_exact(dphi_peak: float, dim: int = ENVELOPE_DIM) -> float:
    """EXACT fluence-weighted <sin^2(dphi(I)/2)> over the dim-D Gaussian envelope.

    dphi(I) = dphi_peak * g with g = I/I_peak in (0, 1]. Cross-checks the
    small-angle P_peak * F_env method through the same co-area density as above.
    """
    p = dim / 2.0 - 1.0

    def num(g: float) -> float:  # Q = sin^2(dphi g/2)
        return np.sin(dphi_peak * g / 2.0) ** 2 * ((-np.log(g)) ** p)

    def den(g: float) -> float:
        return (-np.log(g)) ** p

    n_val, _ = integrate.quad(num, 0.0, 1.0)
    d_val, _ = integrate.quad(den, 0.0, 1.0)
    return float(n_val / d_val)


def main() -> None:
    print("=" * 78)
    print("H4 — TABLE I PULSE-INTEGRATED EXPECTATION (envelope form factor)")
    print("=" * 78)

    f_env = envelope_form_factor_analytic()
    f_env_quad = envelope_form_factor_quadrature()
    print(f"\nEnvelope dimensionality D = {ENVELOPE_DIM} (temporal + 2D transverse focal)")
    print(f"Envelope form factor  F_env = 3^(-D/2)  (closed form) = {f_env:.6f}")
    print(f"Envelope form factor  F_env  (quadrature cross-check) = {f_env_quad:.6f}")
    assert abs(f_env - f_env_quad) < 1e-6, "closed-form vs quadrature F_env mismatch"

    E = field_from_intensity_wcm2(I_DEMONSTRATED_WCM2)
    print(f"\nDemonstrated pump {I_DEMONSTRATED_WCM2:.0e} W/cm^2 -> peak E = {E:.3e} V/m, "
          f"A^2 = {(E / E_YIELD) ** 2:.3e}")
    print(f"Interaction length z = {Z_INTERACTION_M*1e6:.0f} um\n")

    rows = []
    print(f"{'scenario':<14}{'probe[eV]':>10}{'P_peak':>12}{'dphi/2':>10}"
          f"{'P_int(F_env)':>14}{'P_int(exact)':>14}{'rel.diff':>10}")
    for name, probe_eV in DEMONSTRATED_PROBES_EV:
        pt = hibef_point(E, probe_eV, z_m=Z_INTERACTION_M)
        p_peak = pt.P_ave_exact
        dphi_half = pt.dphi_ave / 2.0
        p_int_form = p_peak * f_env               # small-angle P_peak * F_env
        p_int_exact = pulse_integrated_exact(pt.dphi_ave)  # exact <sin^2>
        rel = abs(p_int_form - p_int_exact) / p_int_exact
        rows.append({
            "scenario": name,
            "probe_eV": probe_eV,
            "P_flip_peak": p_peak,
            "dphi_over_2": dphi_half,
            "P_flip_pulse_integrated_form_factor": p_int_form,
            "P_flip_pulse_integrated_exact": p_int_exact,
            "form_vs_exact_rel_diff": rel,
        })
        print(f"{name:<14}{probe_eV:>10.0f}{p_peak:>12.3e}{dphi_half:>10.4f}"
              f"{p_int_form:>14.3e}{p_int_exact:>14.3e}{rel:>10.2%}")

    p_ints = [r["P_flip_pulse_integrated_form_factor"] for r in rows]
    print(f"\nPulse-integrated expectation range: "
          f"{min(p_ints):.2e} .. {max(p_ints):.2e}")
    print("(peak column x F_env; small-angle exact agrees to <1%)")

    out = {
        "class": "CONSISTENCY (readout-convention audit; no new claim/constant/emergence)",
        "envelope_dim": ENVELOPE_DIM,
        "envelope_form_factor_analytic_3pow_minus_Dhalf": f_env,
        "envelope_form_factor_quadrature": f_env_quad,
        "pump_wcm2": I_DEMONSTRATED_WCM2,
        "peak_field_Vpm": E,
        "z_interaction_m": Z_INTERACTION_M,
        "rows": rows,
        "note": (
            "Table I quotes peak-field P_flip; the pulse-integrated expectation "
            "is peak x F_env with F_env = 3^(-3/2) ~ 0.19245 (matched co-focused "
            "3D Gaussian, fluence-weighted). Exact <sin^2> cross-checks it to <1%."
        ),
    }
    out_dir = _HERE / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "h4_pulse_integrated_expectation.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
