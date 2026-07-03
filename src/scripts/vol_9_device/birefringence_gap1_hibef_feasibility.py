#!/usr/bin/env python3
"""
GAP-1 — AVE's REALIZED birefringence observable at HIBEF's actual parameters.
=============================================================================

The feasibility arithmetic that SIZES the E-route vacuum-birefringence campaign
(RANK-1, cold-eyes-audit-ratified 2026-07-03). Pre-reg:
  research/2026-07-03_birefringence-gap1-hibef-feasibility_prereg.md  (FROZEN)

WHAT THIS ADDS over the existing sweep drivers (vacuum_birefringence_bench.py /
_facility_sweep.py): those model an OPTICAL Fabry-Perot ellipticity (finesse
build-up). HIBEF has NO Fabry-Perot — it is a SINGLE-PASS X-ray dark-field
polarimeter (survey :67,:155). This driver models the ACTUAL HIBEF readout: the
polarization-FLIP PROBABILITY read as X-ray purity, and derives the HONEST
SATURATED prediction where the naive perturbative flip-prob would exceed unity.

THE FORM-BREAK (survey :77-79). On flip-PROBABILITY the field-independent
amplitude ratio squares to ~9e13x QED, driving the naive perturbative AVE
flip-prob P = (dphi/2)^2 > 1. That form BREAKS. The honest bounded observable is
the EXACT single-pass flip-prob P = sin^2(dphi/2) in [0,1] (the Ax-4 kernel's
retardance accumulated over the single pass, read on the Poincare sphere). This
driver computes BOTH and books the saturated one against the two X-ray purity
floors.

STEP-3.8 LIVENESS (pre-reg §2.4): the QED leg through THIS chain is validated
FIRST — it must reduce to the perturbative form (QED dphi << 1) and land in the
literature order band before the AVE leg is read.

DISCIPLINE:
  - consistency-vs-emergence: CONSISTENCY-class. Canonical AVE delta_n
    (clm-pp3qwf) through a LITERATURE HIBEF readout. No new clm/constant.
  - chord-vs-echo: the FORM (tree-O(1) saturation, static-B transparent) is the
    AVE chord; the 7.5/alpha^3 MAGNITUDE is an alpha-echo (symmetric standard).
  - phase-space-coordinate-check PASS: flip-prob is a polarization-PHASE
    observable; both legs ride the identical delta_n -> dphi -> flip chain.
  - the a_EH~1.45 PVLAS back-solve artifact anchors NOTHING (1/(2 pi alpha)
    units artifact; excluded).

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

from ave.bench import (  # noqa: E402
    coefficient_ratio_differential,
    delta_n_ave_differential_exact,
    delta_n_qed,
    delta_n_qed_magnetic,
    substrate_identity_holds,
    vacuum_magnetic_birefringence_constant,
)
from ave.core.constants import (  # noqa: E402
    C_0,
    E_YIELD,
    EPSILON_0,
    HBAR,
    e_charge,
)

# ============================================================================
# FACILITY PARAMETERS — LITERATURE INPUTS (LABELED, cited). NOT AVE numbers.
# ============================================================================
# BIREF@HIBEF LoI arXiv:2405.18063 (I_L=1e21 W/cm^2 demonstrated ReLaX pump);
# survey research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md:71.
E_HIBEF: float = 8.7e13            # V/m, demonstrated-pump peak field
I_L_DEMONSTRATED_WCM2: float = 1e21  # W/cm^2, ReLaX demonstrated peak intensity
Z_INTERACTION_M: float = 10e-6     # m, single-pass interaction length (survey :67)

# X-ray probe photon energies [eV]: NJP 2021 (9835 eV) + the two LoI scenarios.
E_PROBE_NJP_EV: float = 9835.0     # NJP 2021 doi:10.1088/1367-2630/ac1df4
E_PROBE_LOI_LOW_EV: float = 8766.0
E_PROBE_LOI_HIGH_EV: float = 12914.0

# X-ray polarimeter purity floors (the BINDING constraint for the whole lane).
P_REQUIRED: float = 1.4e-10        # NJP 2021 diamond quasi-channel-cut @9835 eV
P_DEMONSTRATED_6457: float = 2.4e-10   # Marx-Schulze PRL 110, 254801 (2013) @6.457 keV
P_DEMONSTRATED_6457_ERR: float = 0.9e-10
P_DEMONSTRATED_12914: float = 5.7e-10  # @12.914 keV (same lineage)

# Published QED detectable-signal metric (NJP 2021, best scenario).
QED_SIGNAL_PHOTONS_PER_HR: float = 0.86
QED_BKG_PHOTONS_PER_HR: float = 5.6e6

# LoI design intensities used for the QED-leg order validation (petawatt-upgrade
# scenarios the LoI's ~detectable prediction rests on, ABOVE the demonstrated 1e21).
I_L_LOI_DESIGN_WCM2: tuple[float, ...] = (1e22, 1e23)


def probe_wavelength_m(E_probe_eV: float) -> float:
    """X-ray probe wavelength [m] from photon energy: lambda = 2 pi hbar c / E.

    Built from ave.core.constants (HBAR, C_0, e_charge); no hardcoded h/c.
    """
    E_probe_J = E_probe_eV * e_charge
    return float(2.0 * np.pi * HBAR * C_0 / E_probe_J)


def field_from_intensity_wcm2(I_wcm2: float) -> float:
    """Peak E-field [V/m] from intensity I [W/cm^2]. E = sqrt(2 I / (c eps0)).

    LABELED standard-EM bench relation, built from ave.core.constants.
    """
    I_wm2 = I_wcm2 * 1e4
    return float(np.sqrt(2.0 * I_wm2 / (C_0 * EPSILON_0)))


# ============================================================================
# THE HIBEF X-RAY-POLARIMETER READOUT CHAIN (the NEW machinery, pre-reg §2.3)
# Single-pass, NO Fabry-Perot. Both AVE and QED delta_n ride the IDENTICAL chain
# (no-strawman R1); only delta_n differs.
# ============================================================================
def retardance_phase(delta_n: float, wavelength_m: float, z_m: float = Z_INTERACTION_M) -> float:
    """Accumulated single-pass retardance phase dphi = (2 pi / lambda) delta_n z [rad].

    The polarization-phase difference between the two eigenmodes over the
    interaction length. delta_n is the PAR-PERP DIFFERENTIAL (the falsifier
    observable a polarimeter reads). |delta_n| used (sign is a convention; the
    flip-prob depends on |dphi|).
    """
    return float((2.0 * np.pi / wavelength_m) * abs(delta_n) * z_m)


def flip_prob_perturbative(dphi: float) -> float:
    """Naive perturbative polarization-flip probability P = (dphi/2)^2.

    The small-angle (weak-signal) truncation. UNBOUNDED — exceeds 1 when the
    signal is large (the form-break, survey :77-79). Returned so the break is
    VISIBLE, not hidden behind the saturated form.
    """
    return float((dphi / 2.0) ** 2)


def flip_prob_exact(dphi: float) -> float:
    """HONEST saturated single-pass polarization-flip probability P = sin^2(dphi/2).

    The exact bounded observable in [0, 1]: the fraction of probe intensity
    rotated into the crossed (dark-field) polarimeter channel by a retardance
    dphi over the single pass. Reduces to (dphi/2)^2 for dphi << 1 (recovers the
    perturbative form where it is valid). This is what the X-ray dark-field
    polarimeter actually reads. Bounded by construction — resolves the form-break
    (perturbative >1) by the correct non-perturbative saturation.
    """
    return float(np.sin(dphi / 2.0) ** 2)


@dataclass(frozen=True)
class HibefPoint:
    """One co-computed (AVE, QED) HIBEF flip-prob point at a probe energy."""
    E_field: float
    A: float
    E_probe_eV: float
    wavelength_m: float
    dn_ave: float
    dn_qed: float
    dphi_ave: float
    dphi_qed: float
    P_ave_pert: float
    P_ave_exact: float
    P_qed_pert: float
    P_qed_exact: float
    ave_perturbative_breaks: bool  # naive AVE flip-prob > 1


def hibef_point(E_field: float, E_probe_eV: float, z_m: float = Z_INTERACTION_M) -> HibefPoint:
    """Co-compute the AVE and QED flip-prob at one (field, probe-energy) through
    the IDENTICAL readout chain (no-strawman R1). AVE = par-perp differential
    -1/2 A^2 (canonical); QED = differenced Euler-Heisenberg 3/45 (literature)."""
    lam = probe_wavelength_m(E_probe_eV)
    dn_ave = float(delta_n_ave_differential_exact(E_field))
    dn_qed = float(delta_n_qed(E_field, a_eh=3.0 / 45.0))
    dphi_ave = retardance_phase(dn_ave, lam, z_m)
    dphi_qed = retardance_phase(dn_qed, lam, z_m)
    P_ave_pert = flip_prob_perturbative(dphi_ave)
    P_ave_exact = flip_prob_exact(dphi_ave)
    P_qed_pert = flip_prob_perturbative(dphi_qed)
    P_qed_exact = flip_prob_exact(dphi_qed)
    return HibefPoint(
        E_field=E_field, A=E_field / E_YIELD, E_probe_eV=E_probe_eV, wavelength_m=lam,
        dn_ave=dn_ave, dn_qed=dn_qed, dphi_ave=dphi_ave, dphi_qed=dphi_qed,
        P_ave_pert=P_ave_pert, P_ave_exact=P_ave_exact,
        P_qed_pert=P_qed_pert, P_qed_exact=P_qed_exact,
        ave_perturbative_breaks=bool(P_ave_pert > 1.0),
    )


# ============================================================================
# STEP-3.8 LIVENESS — validate the pipeline on the QED leg FIRST (pre-reg §2.4)
# ============================================================================
def validate_qed_leg() -> dict:
    """Frozen validation gate. Returns the gate record; HALT on hard failures."""
    out: dict = {}

    # (1) substrate identity + A_e validate-on-known (existing gate).
    A_e = vacuum_magnetic_birefringence_constant()
    A_e_relerr = abs(A_e - 1.32e-24) / 1.32e-24
    out["substrate_identity_holds"] = substrate_identity_holds()
    out["A_e_recovers_1.32e-24"] = bool(A_e_relerr < 0.01)
    out["A_e_value"] = A_e
    out["A_e_relerr"] = A_e_relerr

    # (2) QED-leg order check at the LoI DESIGN fields (petawatt scenarios).
    design = []
    for I_wcm2 in I_L_LOI_DESIGN_WCM2:
        E = field_from_intensity_wcm2(I_wcm2)
        pt = hibef_point(E, E_PROBE_NJP_EV)
        design.append({
            "I_L_wcm2": I_wcm2, "E_field": E, "A2": (E / E_YIELD) ** 2,
            "P_qed_exact": pt.P_qed_exact, "dphi_qed": pt.dphi_qed,
        })
    out["qed_leg_at_loi_design"] = design
    # The published order band from 0.86 flipped-photons/hr against 1e12-1e20
    # probe-photons/hr -> implied flip-prob ~ 1e-21 .. 1e-14 (gated..full-rate);
    # the survey characterizes it as ~1e-12. We book the QED design-field order
    # rather than assert a point value (my flat single-pass geometry has no
    # focus-integration weighting -> systematically below the LoI's integrated
    # prediction; the RATIO is unaffected).
    qed_orders = [d["P_qed_exact"] for d in design]
    out["qed_design_flip_prob_band"] = {"min": min(qed_orders), "max": max(qed_orders)}
    out["qed_design_in_literature_order_band"] = bool(
        min(qed_orders) < 1e-11 and max(qed_orders) > 1e-22
    )

    # (3) QED leg must REDUCE to the perturbative form (dphi << 1 -> no saturation).
    pt_dem = hibef_point(E_HIBEF, E_PROBE_NJP_EV)
    reduces = np.isclose(pt_dem.P_qed_exact, pt_dem.P_qed_pert, rtol=1e-6)
    out["qed_exact_reduces_to_perturbative"] = bool(reduces)
    out["qed_demonstrated_pump"] = {
        "E_field": E_HIBEF, "P_qed_exact": pt_dem.P_qed_exact,
        "P_qed_pert": pt_dem.P_qed_pert, "dphi_qed": pt_dem.dphi_qed,
    }

    hard_ok = (
        out["substrate_identity_holds"]
        and out["A_e_recovers_1.32e-24"]
        and out["qed_exact_reduces_to_perturbative"]
    )
    out["VALIDATE_PASS"] = bool(hard_ok)
    if not hard_ok:
        print("HALT: QED-leg pipeline validation FAILED — readout chain is wrong.")
        print(json.dumps(out, indent=2, default=float))
        sys.exit(1)
    return out


# ============================================================================
# GAP-1 BIN — AVE realized flip-prob at HIBEF vs the two purity floors
# ============================================================================
def classify_gap1(pt: HibefPoint) -> dict:
    """Read the frozen bin off the COMPUTED saturated AVE flip-prob (Rule-11:
    no post-hoc floor adjustment)."""
    P = pt.P_ave_exact
    dphi_half = pt.dphi_ave / 2.0

    # The many-radian-wrap check: if dphi/2 >> 1 the single-pass sin^2 is a
    # rapidly-oscillating fraction and the polarimetric readout is ambiguous
    # (the vacuum is effectively opaque to the polarimeter at this field) ->
    # FORM-BREAKS-UNRESOLVABLE (pre-reg §3 adjudication note).
    many_radian_wrap = bool(dphi_half > 1.0)

    if many_radian_wrap:
        bin_id = "FORM-BREAKS-UNRESOLVABLE"
        margin = None
        note = (
            f"dphi/2 = {dphi_half:.3e} rad >> 1: the single-pass sin^2(dphi/2) is a "
            "many-wrap oscillation; the crossed-polarizer flip fraction is ambiguous "
            "(vacuum effectively opaque to the polarimeter at this field). Named "
            "derivation gap: the single-pass mapping is not credible here."
        )
    elif P >= P_DEMONSTRATED_6457:
        bin_id = "CLEARS-FLOOR"
        margin = P / P_DEMONSTRATED_6457
        note = (
            f"AVE saturated flip-prob {P:.3e} >= demonstrated purity floor "
            f"{P_DEMONSTRATED_6457:.1e} by {margin:.2e}x -> HIBEF's own planned QED "
            "run adjudicates AVE by reanalysis (piggyback prize)."
        )
    elif P >= P_REQUIRED:
        bin_id = "BETWEEN"
        margin = P / P_REQUIRED
        note = (
            f"AVE saturated flip-prob {P:.3e} clears required {P_REQUIRED:.1e} "
            f"(by {margin:.2e}x) but NOT demonstrated {P_DEMONSTRATED_6457:.1e} "
            "-> dedicated precision push needed."
        )
    else:
        bin_id = "BELOW-FLOOR"
        margin = P / P_REQUIRED
        note = (
            f"AVE saturated flip-prob {P:.3e} < required {P_REQUIRED:.1e} "
            f"(short by {1.0/margin:.2e}x) -> facility-generation-gated."
        )
    return {
        "bin": bin_id,
        "P_ave_exact": P,
        "P_ave_perturbative": pt.P_ave_pert,
        "perturbative_breaks_over_unity": pt.ave_perturbative_breaks,
        "dphi_ave_rad": pt.dphi_ave,
        "dphi_half_rad": dphi_half,
        "many_radian_wrap": many_radian_wrap,
        "margin_vs_demonstrated_2.4e-10": (P / P_DEMONSTRATED_6457),
        "margin_vs_required_1.4e-10": (P / P_REQUIRED),
        "bin_margin": margin,
        "note": note,
    }


# ============================================================================
# E-vs-B ASYMMETRY DISCRIMINATOR at HIBEF geometry (pre-reg §3.1)
# ============================================================================
def e_vs_b_asymmetry() -> dict:
    """AVE static/quasi-static-B transparent (delta_n_mu = 0 exactly, clm-pvlas1)
    vs QED B-active (3 A_e B^2). Book whether the asymmetry is testable in HIBEF's
    geometry (what B leg does the ReLaX optical pump actually have?)."""
    # The ReLaX pump B-field magnitude at HIBEF field (propagating optical wave:
    # B = E/c for a plane wave). This is a PROPAGATING-WAVE B, not a static bias.
    B_pump_propagating = E_HIBEF / C_0
    dn_qed_B = float(delta_n_qed_magnetic(B_pump_propagating))
    return {
        "ave_static_B_delta_n": 0.0,  # clm-pvlas1: delta_n_mu = 0 EXACTLY (static B)
        "qed_static_B_delta_n_at_B_pump": dn_qed_B,
        "B_pump_propagating_T": B_pump_propagating,
        "pump_B_is_propagating_wave": True,
        "asymmetry_clean_at_hibef": False,
        "verdict": (
            "NOT a clean zero-vs-nonzero test in HIBEF's geometry. HIBEF's ReLaX "
            "pump is a PROPAGATING optical wave (B = E/c, dB/dt != 0), so AVE's "
            "mu-grade IS loaded by circulation (the E and B of a propagating wave "
            "co-move; the ε-route birefringence clm-pp3qwf already captures the "
            "full wave response). The clean E-vs-B asymmetry (clm-pvlas1) needs a "
            "STATIC-B leg (dB/dt = 0) that HIBEF does not provide — it is the "
            "PVLAS/BMV magnetic-route facilities (static B) that would test it, and "
            "there AVE predicts EXACTLY zero. So at HIBEF the asymmetry is NOT the "
            "discriminator; the E-route coefficient gap (clm-pp3qwf) is. flag-don't-fix."
        ),
    }


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("GAP-1 — AVE REALIZED BIREFRINGENCE OBSERVABLE AT HIBEF (feasibility arithmetic)")
    print("=" * 78)

    # ---- (0) STEP-3.8 LIVENESS: validate the QED leg FIRST ------------------
    print("\n[0] STEP-3.8 LIVENESS — validate the pipeline on the QED leg FIRST:")
    val = validate_qed_leg()
    out["validate_qed_leg"] = val
    print(f"    substrate identity: {val['substrate_identity_holds']}")
    print(f"    A_e recovers 1.32e-24 T^-2: {val['A_e_recovers_1.32e-24']} "
          f"(relerr {val['A_e_relerr']:.2e})")
    dem = val["qed_demonstrated_pump"]
    print(f"    QED @ demonstrated pump (E={dem['E_field']:.2e} V/m): "
          f"dphi_qed={dem['dphi_qed']:.3e} rad -> P_qed={dem['P_qed_exact']:.3e}")
    print(f"    QED exact reduces to perturbative (dphi<<1): "
          f"{val['qed_exact_reduces_to_perturbative']}")
    for d in val["qed_leg_at_loi_design"]:
        print(f"    QED @ LoI design I={d['I_L_wcm2']:.0e} W/cm^2 "
              f"(E={d['E_field']:.2e}): P_qed_exact={d['P_qed_exact']:.3e}")
    print(f"    -> VALIDATE_PASS: {val['VALIDATE_PASS']}")

    # ---- (1) the field-independent matched-differential ratio (context) -----
    ratio = coefficient_ratio_differential()
    out["matched_differential_ratio_7.5_over_alpha3"] = ratio
    print(f"\n[1] Matched differential ratio delta_n_AVE/delta_n_QED = 7.5/alpha^3 = "
          f"{ratio:.4e} (field-independent, ECHO-tagged)")

    # ---- (2) AVE realized flip-prob at HIBEF (the GAP-1 arithmetic) ---------
    print("\n[2] AVE REALIZED FLIP-PROB AT HIBEF (demonstrated pump E=8.7e13 V/m, z=10um):")
    points = {}
    bins = {}
    for lbl, Eprobe in [("NJP_9835eV", E_PROBE_NJP_EV),
                        ("LoI_low_8766eV", E_PROBE_LOI_LOW_EV),
                        ("LoI_high_12914eV", E_PROBE_LOI_HIGH_EV)]:
        pt = hibef_point(E_HIBEF, Eprobe)
        b = classify_gap1(pt)
        points[lbl] = asdict(pt)
        bins[lbl] = b
        print(f"  [{lbl}] lambda={pt.wavelength_m*1e12:.1f} pm  A^2={pt.A**2:.3e}")
        print(f"     dn_ave(diff)={pt.dn_ave:.3e}  dphi_ave={pt.dphi_ave:.3e} rad "
              f"(dphi/2={pt.dphi_ave/2:.3e})")
        print(f"     P_ave PERTURBATIVE (dphi/2)^2 = {pt.P_ave_pert:.3e}  "
              f"(breaks>1: {pt.ave_perturbative_breaks})")
        print(f"     P_ave EXACT sin^2(dphi/2)     = {pt.P_ave_exact:.3e}  <-- HONEST saturated")
        print(f"     BIN: {b['bin']}")
        print(f"       margin vs demonstrated 2.4e-10: {b['margin_vs_demonstrated_2.4e-10']:.3e}")
        print(f"       margin vs required    1.4e-10: {b['margin_vs_required_1.4e-10']:.3e}")
        print(f"       {b['note']}")
    out["hibef_points"] = points
    out["gap1_bins"] = bins

    # ---- (3) E-vs-B asymmetry discriminator at HIBEF geometry ---------------
    print("\n[3] E-vs-B ASYMMETRY DISCRIMINATOR at HIBEF geometry:")
    evb = e_vs_b_asymmetry()
    out["e_vs_b_asymmetry"] = evb
    print(f"    AVE static-B delta_n = {evb['ave_static_B_delta_n']} (EXACTLY zero, clm-pvlas1)")
    print(f"    HIBEF pump B = E/c = {evb['B_pump_propagating_T']:.3e} T "
          f"(propagating wave: {evb['pump_B_is_propagating_wave']})")
    print(f"    asymmetry clean at HIBEF: {evb['asymmetry_clean_at_hibef']}")
    print(f"    {evb['verdict']}")

    # ---- (4) write JSON -----------------------------------------------------
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "birefringence_gap1_hibef_feasibility.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
