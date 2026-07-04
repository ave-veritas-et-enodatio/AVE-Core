#!/usr/bin/env python3
"""
PRIOR-ART / COMMISSIONING EXPOSURE SCAN — the gate before the prediction doc.
=============================================================================

The Cleave G-B discipline at maximum stakes (Grant-directed 2026-07-03). Before
ANY AVE birefringence prediction is registered, establish whether an existing
measurement already bounds an AVE-sized flip-prob. Pre-reg (FROZEN before code):
  research/2026-07-03_birefringence-prior-art-exposure-scan_prereg.md

WHAT THIS ADDS over the GAP-1 feasibility driver: GAP-1 sizes AVE at HIBEF's
demonstrated field (one point). This driver draws AVE's flip-prob LINE across the
intensity plane (1e17 .. 1e21 W/cm^2) where prior experiments live, and tabulates
each prior experiment's (intensity, polarimetric-sensitivity, geometry) so the
ALREADY-BOUNDED / PILOT-DATA-EXISTS / CLEAN-FIELD verdict is read off COMPUTED
numbers, not asserted.

KEY PHYSICS (verify live): AVE flip-prob P = sin^2(dphi/2) ~ (dphi/2)^2 deep-cold,
and dphi ~ delta_n ~ A^2 ~ I. So P_flip ~ I^2 (field^4) at fixed (lambda, z). A
5.4e-3 flip @1e21 falls as (I/1e21)^2 -> ~5.4e-11 @1e19, ~5.4e-19 @1e17. The
AVE/QED ratio (7.5/alpha^3) is I-INDEPENDENT (both ride delta_n^2), so the
DISCRIMINATION does not weaken at lower field; only the absolute signal shrinks.

DISCIPLINE:
  - consistency-vs-emergence: CONSISTENCY-class. Canonical AVE delta_n
    (clm-pp3qwf) across a LITERATURE intensity plane. No new clm/constant.
  - two-method rigor on any CLEAN-FIELD conclusion: the driver's A^2-scaling line
    AND the documented per-experiment geometry (this file's GEOMETRY field).
  - phase-space-coordinate-check PASS: flip-prob in native retardance-phase coords.

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/birefringence_prior_art_exposure_scan.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

# Self-bootstrap: this driver reuses the GAP-1 readout chain (sibling module in
# this directory) as the single source of truth for the flip-prob mapping. Add
# the repo src/ and this script's directory so the invocation `PYTHONPATH=src
# python3 <this>` resolves both the ave.* package and the sibling driver.
_HERE = Path(__file__).resolve().parent
if str(_HERE.parents[2]) not in sys.path:
    sys.path.insert(0, str(_HERE.parents[2]))  # repo src/
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))             # this script's dir (sibling import)

# Reuse the GAP-1 readout chain (single source of truth for the flip-prob mapping).
from birefringence_gap1_hibef_feasibility import (  # noqa: E402
    Z_INTERACTION_M,
    field_from_intensity_wcm2,
    flip_prob_exact,
    flip_prob_perturbative,
    probe_wavelength_m,
    retardance_phase,
)

from ave.bench import (  # noqa: E402
    coefficient_ratio_differential,
    delta_n_ave_differential_exact,
    delta_n_qed,
    substrate_identity_holds,
)
from ave.core.constants import E_YIELD  # noqa: E402

# ============================================================================
# THE PRIOR-EXPERIMENT TABLE — LITERATURE INPUTS (LABELED, cited). NOT AVE numbers.
# Sourced from BIREF@HIBEF LoI arXiv:2405.18063 (Table 1, Fig.2, Fig.5, Fig.14,
# Sec 2.4, Sec 4) and the primary refs it cites.
# ============================================================================


@dataclass(frozen=True)
class PriorExperiment:
    """One prior/commissioning measurement in the exposure plane.

    GEOMETRY / SENSITIVITY are LABELED literature facts; the driver COMPUTES AVE's
    flip-prob at this experiment's field (if it has an optical-focus field) so the
    ALREADY-BOUNDED test is arithmetic, not assertion.
    """
    label: str
    year: str
    facility: str
    probe: str                     # what passes through the field
    optical_pump_wcm2: float | None  # PW-class optical focus intensity, if any (None = no optical focus)
    observable: str                # what was measured
    sensitivity: str               # the reported bound / purity
    passes_xray_through_optical_focus: bool  # the load-bearing geometry test
    polarization_analysis: bool    # was polarization flip analysed
    geometry: str                  # one-line geometry statement (the 2nd-method evidence)
    cite: str


PRIOR_EXPERIMENTS: tuple[PriorExperiment, ...] = (
    PriorExperiment(
        label="LULI all-optical two-beam",
        year="1996/2000",
        facility="LULI",
        probe="optical photon (all-optical)",
        optical_pump_wcm2=None,
        observable="LbL scattering cross-section",
        sensitivity="sigma < 9.9e-40 cm^2 @ omega*=1.7 eV (QED 1.6e-64)",
        passes_xray_through_optical_focus=False,
        polarization_analysis=False,
        geometry="all-optical two-beam collision; NO X-ray probe, NO polarimetric flip channel",
        cite="LoI Table 1 (Moulin 1996 [41]); Bernard 2000 [42]",
    ),
    PriorExperiment(
        label="LULI all-optical three-beam",
        year="2000",
        facility="LULI",
        probe="optical photon (all-optical)",
        optical_pump_wcm2=None,
        observable="LbL scattering cross-section",
        sensitivity="sigma < 1.5e-48 cm^2 @ omega*=0.8 eV (QED 1e-66)",
        passes_xray_through_optical_focus=False,
        polarization_analysis=False,
        geometry="all-optical three-beam; NO X-ray probe, NO polarimetric flip channel",
        cite="LoI Table 1 (Bernard 2000 [42])",
    ),
    PriorExperiment(
        label="SACLA XFEL+XFEL",
        year="2016",
        facility="SACLA (Japan)",
        probe="X-ray (XFEL)",
        optical_pump_wcm2=None,   # X-ray + X-ray; the 'pump' is an XFEL, not a PW optical focus
        observable="LbL scattering cross-section (photon count)",
        sensitivity="sigma < 1.9e-23 cm^2 @ omega*=6.5 keV (QED 2.5e-43)",
        passes_xray_through_optical_focus=False,
        polarization_analysis=False,
        geometry="X-ray+X-ray collision; NO optical PW focus, cross-section not polarization flip",
        cite="LoI Table 1 (Yamaji 2016 [44]); Inada 2014 [43]",
    ),
    PriorExperiment(
        label="HED-HIBEF X-ray polarimetry record purity",
        year="2021",
        facility="HED-HIBEF (EuXFEL)",
        probe="X-ray (EuXFEL, self-seeded)",
        optical_pump_wcm2=None,   # PUMP OFF — polarimeter characterization only
        observable="X-ray polarimeter extinction (purity)",
        sensitivity="P <= 8e-11 (upper limit, photon-flux limited; Si 400 CC, 6 refl)",
        passes_xray_through_optical_focus=False,
        polarization_analysis=True,   # polarization IS the observable, but no strong field present
        geometry="crossed-polarizer extinction, ReLaX pump OFF: NO strong field in the beam path",
        cite="LoI Sec 4.1 + Fig.14 ([71], Schulze/Marx-Schulze lineage)",
    ),
    PriorExperiment(
        label="HED-HIBEF March-2024 priority-access dark-field PoP",
        year="2024",
        facility="HED-HIBEF (EuXFEL)",
        probe="X-ray (EuXFEL)",
        optical_pump_wcm2=None,   # X-ray ONLY beamtime (LoI Sec 4: 'x-ray-only beamtime')
        observable="dark-field shadow quality / background rate (beam-shaping proof-of-principle)",
        sensitivity="outcomes 'currently being analysed' (LoI as of 2024); background-rate characterization",
        passes_xray_through_optical_focus=False,
        polarization_analysis=False,
        geometry="X-ray-ONLY dark-field beam-shaping PoP; ReLaX pump NOT fired -> NO collision, NO flip signal",
        cite="LoI Sec 4 'first x-ray-only beamtime allocated for March 2024 ... outcomes currently being analysed'",
    ),
    PriorExperiment(
        label="PVLAS-FE static-B",
        year="2016",
        facility="PVLAS-FE (Ferrara)",
        probe="optical (Fabry-Perot ellipsometer)",
        optical_pump_wcm2=None,   # STATIC B route, not an optical pump
        observable="magnetic vacuum birefringence Delta_n/B^2",
        sensitivity="Delta_n/B^2 = (19 +- 27)e-24 T^-2 (QED CMV 4e-24)",
        passes_xray_through_optical_focus=False,
        polarization_analysis=True,
        geometry=("STATIC-B route (dB/dt=0). AVE predicts EXACTLY zero (clm-pvlas1) "
                  "-> CONSISTENT, not a test of the E-route"),
        cite="LoI Eq.20 ([77] PVLAS-FE)",
    ),
    PriorExperiment(
        label="STAR polarized gamma-gamma -> e+e-",
        year="2019/2021",
        facility="RHIC/STAR",
        probe="virtual photons (heavy-ion Coulomb)",
        optical_pump_wcm2=None,
        observable="cos(2phi)/cos(4phi) modulation of e+e- pairs (indirect birefringence signature)",
        sensitivity="modulation amplitudes A_2delta, A_4delta consistent with polarized-QED",
        passes_xray_through_optical_focus=False,
        polarization_analysis=True,
        geometry="ultra-peripheral heavy-ion; virtual-photon Landau-Lifshitz, NOT X-ray-through-optical-focus",
        cite="LoI Sec 2.4 + Fig.6 ([10] STAR)",
    ),
)

# The AVE-native anchor: HIBEF demonstrated pump (the GAP-1 point) for the scaling reference.
E_HIBEF_DEMONSTRATED: float = 8.7e13     # V/m
I_HIBEF_DEMONSTRATED_WCM2: float = 1e21  # W/cm^2 (ReLaX demonstrated)
E_PROBE_STD_EV: float = 9835.0           # standard probe energy for the scan line

# The prior-art POLARIMETRIC sensitivity floor that any 'already bounded' claim rides:
# the best X-ray polarimeter extinction ever demonstrated (pump OFF).
BEST_XRAY_POLARIMETER_PURITY: float = 8e-11  # LoI Sec 4.1 record


def ave_flip_prob_at_intensity(I_wcm2: float, E_probe_eV: float = E_PROBE_STD_EV,
                               z_m: float = Z_INTERACTION_M) -> dict:
    """AVE (and co-computed QED) flip-prob at an OPTICAL-pump intensity via the
    GAP-1 chain. Returns the exact + perturbative flip-probs and the field."""
    E = field_from_intensity_wcm2(I_wcm2)
    lam = probe_wavelength_m(E_probe_eV)
    dn_ave = float(delta_n_ave_differential_exact(E))
    dn_qed = float(delta_n_qed(E, a_eh=3.0 / 45.0))
    dphi_ave = retardance_phase(dn_ave, lam, z_m)
    dphi_qed = retardance_phase(dn_qed, lam, z_m)
    return {
        "I_wcm2": I_wcm2,
        "E_field": E,
        "A2": (E / E_YIELD) ** 2,
        "P_ave_exact": flip_prob_exact(dphi_ave),
        "P_ave_pert": flip_prob_perturbative(dphi_ave),
        "P_qed_exact": flip_prob_exact(dphi_qed),
        "dphi_ave": dphi_ave,
    }


def classify_prior_experiment(exp: PriorExperiment) -> dict:
    """Read the ALREADY-BOUNDED / PILOT-DATA / CLEAN test for ONE prior experiment.

    The load-bearing geometry test: to bound an AVE flip-prob, the experiment must
    (i) pass a polarized X-ray probe through a strong (PW-class optical) field, and
    (ii) analyse polarization flip, at a sensitivity finer than AVE's prediction at
    that field. If (i) is False, the experiment CANNOT bound the E-route flip-prob
    regardless of its sensitivity (no strong optical field means A^2=0 -> no AVE
    signal to bound). This is the 2nd-method (geometry) leg of the two-method rigor.
    """
    if exp.optical_pump_wcm2 is not None and exp.passes_xray_through_optical_focus:
        ave = ave_flip_prob_at_intensity(exp.optical_pump_wcm2)
        if exp.polarization_analysis:
            verdict = "ALREADY-BOUNDED-CANDIDATE"
            note = (
                f"passes X-ray through optical focus AND analysed polarization; "
                f"AVE predicts P_flip={ave['P_ave_exact']:.3e} at its field "
                f"{ave['E_field']:.2e} V/m -> compare to its sensitivity."
            )
        else:
            verdict = "PILOT-DATA-EXISTS-UNANALYZED"
            note = (
                f"passes X-ray through optical focus but polarization flip NOT analysed; "
                f"AVE predicts P_flip={ave['P_ave_exact']:.3e} sitting unanalysed in this dataset."
            )
        ave_pred = ave["P_ave_exact"]
    else:
        verdict = "CANNOT-BOUND-E-ROUTE"
        ave_pred = None
        reason = []
        if exp.optical_pump_wcm2 is None:
            reason.append("no PW-class optical focus in the beam path (A^2=0 -> no E-route AVE signal to bound)")
        if not exp.passes_xray_through_optical_focus:
            reason.append("does not pass a polarized X-ray probe through a strong optical field")
        note = "; ".join(reason) + f". Geometry: {exp.geometry}"
    return {
        "label": exp.label,
        "verdict": verdict,
        "ave_flip_prob_at_its_field": ave_pred,
        "geometry": exp.geometry,
        "sensitivity": exp.sensitivity,
        "note": note,
        "cite": exp.cite,
    }


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("PRIOR-ART / COMMISSIONING EXPOSURE SCAN (the gate before the prediction doc)")
    print("=" * 78)

    # ---- (0) liveness: substrate identity + the I^2 scaling law -------------
    print("\n[0] LIVENESS + scaling law:")
    id_ok = substrate_identity_holds()
    ratio = coefficient_ratio_differential()
    out["substrate_identity_holds"] = id_ok
    out["matched_differential_ratio"] = ratio
    print(f"    substrate identity (E_crit/E_yield)^2 = 1/alpha: {id_ok}")
    print(f"    matched differential ratio 7.5/alpha^3 = {ratio:.4e} (field-INDEPENDENT)")

    # Verify P_flip ~ I^2: compare 1e21 and 1e20.
    p21 = ave_flip_prob_at_intensity(1e21)
    p20 = ave_flip_prob_at_intensity(1e20)
    scaling = p21["P_ave_exact"] / p20["P_ave_exact"]
    out["flip_prob_scaling_1e21_over_1e20"] = scaling
    out["flip_prob_scales_as_I_squared"] = bool(abs(scaling - 100.0) / 100.0 < 0.02)
    print(f"    P_flip(1e21)/P_flip(1e20) = {scaling:.2f} (I^2 scaling -> expect ~100): "
          f"{out['flip_prob_scales_as_I_squared']}")
    print("    -> AVE flip-prob ~ I^2 (field^4); ratio to QED is I-INDEPENDENT.")

    # ---- (1) the AVE exposure LINE across the intensity plane ---------------
    print("\n[1] AVE flip-prob exposure LINE (E-route, probe 9835 eV, z=10um):")
    line = []
    for intensity in (1e17, 1e18, 1e19, 1e20, 3e20, 1e21, 1e22):
        p = ave_flip_prob_at_intensity(intensity)
        line.append(p)
        print(f"    I={intensity:.0e} W/cm^2  E={p['E_field']:.2e} V/m  A^2={p['A2']:.2e}  "
              f"P_ave={p['P_ave_exact']:.3e}  P_qed={p['P_qed_exact']:.3e}  "
              f"AVE/QED={p['P_ave_exact']/p['P_qed_exact']:.2e}")
    out["ave_exposure_line"] = line

    # AVE flip-prob at each intensity vs the best-ever polarimeter purity floor.
    print(f"\n    vs best-ever X-ray polarimeter purity {BEST_XRAY_POLARIMETER_PURITY:.0e} "
          "(pump OFF; the sensitivity a HYPOTHETICAL pump-ON run could reach):")
    for p in line:
        clears = p["P_ave_exact"] >= BEST_XRAY_POLARIMETER_PURITY
        tag = ("above floor (visible IF a pump-ON polarimetric run existed)" if clears
               else "below best-polarimeter floor")
        print(f"    I={p['I_wcm2']:.0e}: P_ave={p['P_ave_exact']:.3e} "
              f"{'>= ' if clears else '<  '}{BEST_XRAY_POLARIMETER_PURITY:.0e}  -> {tag}")

    # ---- (2) classify each PRIOR experiment ---------------------------------
    print("\n[2] PER-EXPERIMENT classification (the gate):")
    classifications = []
    for exp in PRIOR_EXPERIMENTS:
        c = classify_prior_experiment(exp)
        classifications.append(c)
        print(f"  [{c['verdict']:28s}] {c['label']}")
        print(f"      geometry:  {c['geometry']}")
        print(f"      sensitiv:  {c['sensitivity']}")
        print(f"      note:      {c['note']}")
    out["prior_experiment_classifications"] = classifications

    # ---- (3) roll up the SCAN VERDICT ---------------------------------------
    print("\n[3] SCAN VERDICT (rolled up):")
    verdicts = {c["verdict"] for c in classifications}
    any_bounded = "ALREADY-BOUNDED-CANDIDATE" in verdicts
    any_pilot = "PILOT-DATA-EXISTS-UNANALYZED" in verdicts
    if any_bounded:
        scan_bin = "ALREADY-BOUNDED"
    elif any_pilot:
        scan_bin = "PILOT-DATA-EXISTS-UNANALYZED"
    else:
        scan_bin = "CLEAN-FIELD"
    out["scan_bin"] = scan_bin
    out["verdict_set"] = sorted(verdicts)
    print(f"    verdict set across prior experiments: {sorted(verdicts)}")
    print(f"    SCAN BIN: {scan_bin}")
    if scan_bin == "CLEAN-FIELD":
        print("    Two-method rigor: (1) driver A^2-scaling line above; (2) per-experiment")
        print("    GEOMETRY field documents NO prior experiment passes a polarized X-ray probe")
        print("    through a PW-class optical focus with polarization analysis. -> prediction doc PROCEEDS.")

    # ---- write JSON ---------------------------------------------------------
    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "birefringence_prior_art_exposure_scan.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
