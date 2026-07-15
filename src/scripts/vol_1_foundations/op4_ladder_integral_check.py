#!/usr/bin/env python3
"""
OP4 LADDER-INTEGRAL CHECK — registered check closing Ruling-11's last loose end (2026-07-15).
=============================================================================================

Research note (hypothesis-first; verdict classes declared BEFORE the numbers):
    research/2026-07-15_op4-ladder-integral-check_NOTE.md

THE ONE QUESTION: is Op4/Op14's pairwise impedance dress
    Z(r)/Z0 = 1 / (1 - (d_sat/r)^2)^{1/4}        (universal_operators.py:229 ; pairwise-potential.md:20)
the correct INTEGRATED PORT EXPRESSION of a radial ladder whose cells are individually
biased by the LOCAL FIELD-strain  A_E(s) = (d_sat/s)^2  (the Ruling-11 constitutive
register, #693/knee-check convention) -- or is its voltage-form argument a genuine
register defect in a canonical operator?

Sector header -- MODE static two-body REACTIVE register (the local impedance DRESS Z(r),
NOT the through-coupling force). REGIME cold, KERNEL ON (Op14/Ax4 saturation S=sqrt(1-A^2)
sets each cell's line impedance). PHASE-STATE sub-yield / dynamic (r > d_sat over the whole
window r/d_sat in [2,300]; the Pauli wall r<=d_sat is out of scope). SECTOR E-sector static
reactive transmission line (graded radial LC line, Z_local = sqrt(L/C) per cell). No new
ENGINE: the canonical Ax4 kernel `universal_saturation` is imported UNMODIFIED; this check
re-expresses the existing operator as a ladder and integrates it.

Consistency-vs-emergence: CONSISTENCY / CHARACTERIZATION. No value minted, no emergence
headlined; the comparison is K-independent (only the dimensionless dress Z/Z0 vs r/d_sat).
No physics constants are hard-coded: Z_0, EPS_CLIP come from ave.core.constants; the kernel
S from ave.core.universal_operators. d_sat = 1.0 is a NATIVE scale normalization (the
operator is scale-free in d_sat; the window is the dimensionless r/d_sat).

STRAIN DISCIPLINE (load-bearing): the FIELD-strain A_E = (d_sat/s)^2 (~1/s^2, the #693
kernel-consumed amplitude) is Ruling-11's per-cell bias; the VOLTAGE-strain A_V = d_sat/s
(~1/s, Op4's OWN docstring :160) is Op4's argument. Both are run; Op4's own register is the
CONTROL. The +-1/2 sign (Q3) is PARAMETERIZED, not resolved (cosserat_field_3d.py:419-423
flag; qed_trace RESULT:108 register-flip).
"""
from __future__ import annotations

import argparse
import json

import numpy as np

from ave.core.constants import EPS_CLIP, Z_0
from ave.core.universal_operators import universal_saturation
from ave_path_util import sim_output

# ── native scale + test window (declared) ────────────────────────────────────
D_SAT = 1.0          # native yield scale (operator is scale-free in d_sat; window is r/d_sat)
A_YIELD = 1.0        # native strain yield (S = sqrt(1 - (A/A_yield)^2), A_yield=1 in native units)
R_LO, R_HI = 2.0, 300.0
SAMPLE_RADII = (2.0, 5.0, 10.0, 30.0, 300.0)
R_FAR = 3.0e3        # far-field termination radius (A_E, A_V ~ 0 => Z_local ~ Z_0)

# ── FROZEN verdict-class thresholds (declared BEFORE any run) ─────────────────
MATCH_P_TOL = 0.3        # |p - 2| for Op4-form (p=2) match
FIELD_P_TOL = 0.4        # |p - 4| for field-strain form (p=4)
MATCH_REL = 2.0e-2       # pointwise |Z_in/Z_Op4 - 1| tolerance (~ discretization band)
PARTIAL_NEAR_REL = 1.0e-2
FAR_CUT = 30.0           # d_sat: r >= FAR_CUT is the "far zone"
NEAR_CUT = 5.0           # d_sat: r <= NEAR_CUT is the "near zone"


# ═════════════════════════════════════════════════════════════════════════════
# STRAIN REGISTERS + LOCAL DRESS
# ═════════════════════════════════════════════════════════════════════════════
def strain_field(s):
    """Ruling-11 / #693 FIELD-strain A_E(s) = (d_sat/s)^2  (~1/s^2)."""
    return (D_SAT / np.asarray(s, dtype=float)) ** 2


def strain_voltage(s):
    """Op4-docstring VOLTAGE/displacement-strain A_V(s) = d_sat/s  (~1/s)."""
    return D_SAT / np.asarray(s, dtype=float)


def kernel_S(A):
    """Canonical Ax4/Op2 saturation kernel, imported UNMODIFIED. S = sqrt(1 - (A/A_yield)^2)."""
    return universal_saturation(np.asarray(A, dtype=float), A_YIELD)


def z_local(s, strain, sign):
    """Per-cell local characteristic impedance Z_local(s)/Z_0 ... returned WITH the Z_0 factor.

    sign = -1 : rising S^{-1/2}  (the Op4 direction, Z -> inf at the wall)
    sign = +1 : falling S^{+1/2} (the eps-load C_eff=C0/S => Z=Z0*sqrt(S), Z -> 0)
    """
    S = np.clip(kernel_S(strain(s)), EPS_CLIP, 1.0)
    return Z_0 * S ** (sign * 0.5)


def op4_dress(r):
    """Op4's documented dress Z_Op4(r)/Z_0 * Z_0, reconstructed via the CANONICAL kernel:
    Z_Op4/Z_0 = S(A_V)^{-1/2} = 1/(1-(d_sat/r)^2)^{1/4}   (the universal_operators.py:229 identity)."""
    return z_local(r, strain_voltage, sign=-1)


# ═════════════════════════════════════════════════════════════════════════════
# (a) EXACT LADDER RECURSION  (graded lossless transmission-line cascade)
# ═════════════════════════════════════════════════════════════════════════════
def ladder_zin(r, strain, sign, n_cells, theta, r_far=R_FAR):
    """Input impedance looking into the graded radial line from r out to r_far.

    Log-spaced nodes r -> r_far; matched far-field termination Z_L = Z_local(r_far);
    march INWARD with the lossless line impedance transform
        Z_in = Z_c (Z_L + i Z_c tan theta) / (Z_c + i Z_L tan theta)
    Z_c = Z_local(cell midpoint); theta = per-cell electrical length (adiabaticity knob).
    Returns complex Z_in(r).
    """
    nodes = np.geomspace(r, r_far, n_cells + 1)
    Z_load = complex(z_local(r_far, strain, sign))
    t = np.tan(theta)
    for k in range(n_cells - 1, -1, -1):
        s_mid = np.sqrt(nodes[k] * nodes[k + 1])
        Zc = complex(z_local(s_mid, strain, sign))
        Z_load = Zc * (Z_load + 1j * Zc * t) / (Zc + 1j * Z_load * t)
    return Z_load


def ladder_convergence(r, strain, sign, grids=None):
    """Refine (n_cells, theta) and return the sequence + the finest Re(Z_in) and its
    residual vs the analytic WKB port z_local(r)."""
    if grids is None:
        grids = [(400, 0.30), (1200, 0.30), (4000, 0.30), (12000, 0.30)]
    local = float(z_local(r, strain, sign))
    seq = []
    for (n, th) in grids:
        z = ladder_zin(r, strain, sign, n, th)
        seq.append({"n_cells": n, "theta": th, "Re_Zin": z.real, "Im_Zin": z.imag,
                    "resid_vs_local": abs(z.real - local)})
    return {"local_wkb": local, "grid": seq,
            "finest_Re_Zin": seq[-1]["Re_Zin"], "finest_resid": seq[-1]["resid_vs_local"]}


# ═════════════════════════════════════════════════════════════════════════════
# EXPONENT FIT  p in (1 - (d_sat/r)^p)^q
# ═════════════════════════════════════════════════════════════════════════════
def fit_exponent(strain, sign, q, r_lo=R_LO, r_hi=R_HI, n=120):
    """Recover p in (1-(d_sat/r)^p)^q that best reproduces the analytic ladder port
    z_local (which step (a) confirms the exact recursion converges to). Log-space LSQ."""
    r = np.geomspace(r_lo, r_hi, n)
    y = np.asarray(z_local(r, strain, sign) / Z_0, dtype=float)  # dimensionless dress
    p_grid = np.linspace(0.5, 6.0, 1101)
    best_p, best_sse = None, np.inf
    for p in p_grid:
        arg = np.clip(1.0 - (D_SAT / r) ** p, EPS_CLIP, 1.0)
        yhat = arg ** q
        sse = float(np.sum((np.log(y) - np.log(yhat)) ** 2))
        if sse < best_sse:
            best_p, best_sse = float(p), sse
    return {"p": best_p, "q": q, "sse": best_sse}


# ═════════════════════════════════════════════════════════════════════════════
# VERDICT  (frozen thresholds above)
# ═════════════════════════════════════════════════════════════════════════════
def classify(p_rise, dev_rise, p_fall, dev_fall, near_dev_best, far_dev_best, p_best):
    """Return the verdict class for the FIELD-strain ladder vs Op4.

    p_rise/p_fall : recovered exponent of the field ladder, S^{-1/2} / S^{+1/2} variants.
    dev_*         : max |Z_in/Z_Op4 - 1| over the window for that variant.
    p_best        : the exponent of the variant closest to Op4's direction (rise, sign=-1).
    near/far_dev_best : max deviation of the best variant in the near / far zone.
    """
    rise_match = (abs(p_rise - 2.0) <= MATCH_P_TOL) and (dev_rise <= MATCH_REL)
    fall_match = (abs(p_fall - 2.0) <= MATCH_P_TOL) and (dev_fall <= MATCH_REL)
    if rise_match and fall_match:
        return "MATCH-FORM"
    if rise_match or fall_match:
        return "MATCH-UP-TO-SIGN"
    # far zone agrees with Op4 (same p=2 family) but near zone diverges
    if (far_dev_best <= MATCH_REL) and (near_dev_best > PARTIAL_NEAR_REL) and (abs(p_best - 2.0) <= MATCH_P_TOL):
        return "PARTIAL"
    # field-strain ladder is structurally p=4 (or clearly not p=2) => different form
    if (abs(p_best - 4.0) <= FIELD_P_TOL) or (abs(p_best - 2.0) > MATCH_P_TOL):
        return "NO-MATCH"
    return "AMBIGUOUS"


# ═════════════════════════════════════════════════════════════════════════════
# MAIN
# ═════════════════════════════════════════════════════════════════════════════
def _max_reldev(strain, sign, r_lo=R_LO, r_hi=R_HI, n=120):
    """Max |Z_ladder_port/Z_Op4 - 1| over the window (ladder port = z_local, the WKB limit)."""
    r = np.geomspace(r_lo, r_hi, n)
    zl = np.asarray(z_local(r, strain, sign), dtype=float)
    zo = np.asarray(op4_dress(r), dtype=float)
    rel = np.abs(zl / zo - 1.0)
    i = int(np.argmax(rel))
    return {"max_reldev": float(rel[i]), "r_at_max": float(r[i]),
            "near_dev": float(np.max(rel[r <= NEAR_CUT])) if np.any(r <= NEAR_CUT) else 0.0,
            "far_dev": float(np.max(rel[r >= FAR_CUT])) if np.any(r >= FAR_CUT) else 0.0}


def main() -> dict:
    # exponents (analytic WKB ports; step (a) confirms the exact ladder converges to them)
    fit_field_rise = fit_exponent(strain_field, sign=-1, q=-0.25)
    fit_field_fall = fit_exponent(strain_field, sign=+1, q=+0.25)
    fit_volt_ctrl = fit_exponent(strain_voltage, sign=-1, q=-0.25)  # CONTROL: Op4's own register

    dev_field_rise = _max_reldev(strain_field, sign=-1)
    dev_field_fall = _max_reldev(strain_field, sign=+1)

    # exact-ladder convergence to the WKB port, at the deepest near-zone sample radius
    conv_field_rise = ladder_convergence(SAMPLE_RADII[0], strain_field, sign=-1)
    conv_volt_ctrl = ladder_convergence(SAMPLE_RADII[0], strain_voltage, sign=-1)

    # pointwise table at the 5 sample radii: exact ladder Zin vs Op4, both field sign variants
    table = []
    for r in SAMPLE_RADII:
        zl_rise = float(z_local(r, strain_field, -1))
        zl_fall = float(z_local(r, strain_field, +1))
        zo = float(op4_dress(r))
        lad_rise = ladder_zin(r, strain_field, -1, 4000, 0.30).real
        lad_fall = ladder_zin(r, strain_field, +1, 4000, 0.30).real
        lad_volt = ladder_zin(r, strain_voltage, -1, 4000, 0.30).real
        table.append({
            "r_over_dsat": r,
            "Z_Op4_over_Z0": zo / Z_0,
            "field_rise_wkb_over_Z0": zl_rise / Z_0,
            "field_fall_wkb_over_Z0": zl_fall / Z_0,
            "field_rise_ladder_over_Z0": lad_rise / Z_0,
            "field_fall_ladder_over_Z0": lad_fall / Z_0,
            "voltage_ladder_ctrl_over_Z0": lad_volt / Z_0,
            "reldev_field_rise_vs_Op4": abs(zl_rise / zo - 1.0),
            "reldev_field_fall_vs_Op4": abs(zl_fall / zo - 1.0),
        })

    verdict = classify(
        p_rise=fit_field_rise["p"], dev_rise=dev_field_rise["max_reldev"],
        p_fall=fit_field_fall["p"], dev_fall=dev_field_fall["max_reldev"],
        near_dev_best=dev_field_rise["near_dev"], far_dev_best=dev_field_rise["far_dev"],
        p_best=fit_field_rise["p"],
    )

    result = {
        "check": "op4_ladder_integral_check",
        "question": "Is Op4's Z=Z0/(1-(d/r)^2)^{1/4} the integrated port of a FIELD-strain-biased radial ladder?",
        "sector": "E-sector static reactive transmission line; REACTIVE register; cold KERNEL-ON; sub-yield r>d_sat",
        "class_consistency_vs_emergence": "CONSISTENCY/CHARACTERIZATION",
        "kernel_imported_unmodified": "ave.core.universal_operators.universal_saturation",
        "op4_under_test": "ave.core.universal_operators.universal_pairwise_energy (docstring :160-163, :229)",
        "ruling11_register": "FIELD-strain A_E(s)=(d_sat/s)^2 (branch docs/2026-07-15-walk-batch, UNMERGED)",
        "window_r_over_dsat": [R_LO, R_HI],
        "thresholds": {
            "MATCH_P_TOL": MATCH_P_TOL, "FIELD_P_TOL": FIELD_P_TOL, "MATCH_REL": MATCH_REL,
            "PARTIAL_NEAR_REL": PARTIAL_NEAR_REL, "FAR_CUT": FAR_CUT, "NEAR_CUT": NEAR_CUT,
        },
        "fit_field_rise_Sm12": fit_field_rise,
        "fit_field_fall_Sp12": fit_field_fall,
        "fit_voltage_control_Op4_register": fit_volt_ctrl,
        "op4_target_exponent": 2.0,
        "dev_field_rise_vs_op4": dev_field_rise,
        "dev_field_fall_vs_op4": dev_field_fall,
        "ladder_convergence_field_rise_r2": conv_field_rise,
        "ladder_convergence_voltage_ctrl_r2": conv_volt_ctrl,
        "sample_table": table,
        "VERDICT": verdict,
    }

    out = sim_output("op4_ladder_integral_check.json")
    out.write_text(json.dumps(result, indent=2))
    result["_json"] = str(out)
    return result


def _figure(result: dict) -> str:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply()

    r = np.geomspace(R_LO, R_HI, 400)
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.plot(r, op4_dress(r) / Z_0, lw=2.4, label=r"Op4  $Z/Z_0=(1-(d/r)^2)^{-1/4}$  ($p{=}2$, voltage)")
    ax.plot(r, z_local(r, strain_field, -1) / Z_0, lw=2.0, ls="--",
            label=r"field ladder (rise)  $(1-(d/r)^4)^{-1/4}$  ($p{=}4$)")
    ax.plot(r, z_local(r, strain_field, +1) / Z_0, lw=2.0, ls=":",
            label=r"field ladder (fall)  $(1-(d/r)^4)^{+1/4}$  ($p{=}4$)")
    ax.set_xscale("log")
    ax.set_xlabel(r"$r/d_{\mathrm{sat}}$")
    ax.set_ylabel(r"port impedance dress  $Z_{\mathrm{in}}/Z_0$")
    ax.set_title("")
    ax.legend(loc="upper right", frameon=False, fontsize=8, bbox_to_anchor=(1.0, 1.0))
    out_png = sim_output("op4_ladder_integral_check.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return str(out_png)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Op4 ladder-integral check (Ruling-11 registered check).")
    ap.add_argument("--figure", action="store_true", help="also emit the white-style PNG")
    args = ap.parse_args()

    res = main()
    print(f"VERDICT: {res['VERDICT']}")
    print(f"  field ladder (rise, S^-1/2): p = {res['fit_field_rise_Sm12']['p']:.3f}  "
          f"(Op4 target p=2)   max reldev vs Op4 = {res['dev_field_rise_vs_op4']['max_reldev']:.3e} "
          f"at r/d_sat = {res['dev_field_rise_vs_op4']['r_at_max']:.2f}")
    print(f"  field ladder (fall, S^+1/2): p = {res['fit_field_fall_Sp12']['p']:.3f}   "
          f"max reldev vs Op4 = {res['dev_field_fall_vs_op4']['max_reldev']:.3e}")
    print(f"  VOLTAGE control (Op4 register): p = {res['fit_voltage_control_Op4_register']['p']:.3f}  "
          f"(recovers Op4 p=2)")
    print("  sample table (Z_in/Z_0):")
    for row in res["sample_table"]:
        print(f"    r={row['r_over_dsat']:6.1f}  Op4={row['Z_Op4_over_Z0']:.6f}  "
              f"field_rise_ladder={row['field_rise_ladder_over_Z0']:.6f}  "
              f"field_fall_ladder={row['field_fall_ladder_over_Z0']:.6f}  "
              f"volt_ctrl_ladder={row['voltage_ladder_ctrl_over_Z0']:.6f}")
    print(f"  json: {res['_json']}")
    if args.figure:
        print(f"  png:  {_figure(res)}")
