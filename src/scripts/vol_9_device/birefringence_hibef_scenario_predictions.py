#!/usr/bin/env python3
"""
BIREF@HIBEF SCENARIO PREDICTIONS — the frozen per-scenario AVE/QED prediction table.
====================================================================================

Computes the AVE (canonical clm-pp3qwf differential) and QED (differenced
Euler-Heisenberg) polarization-flip prediction for the EXACT scenarios of the
BIREF@HIBEF Letter of Intent (arXiv:2405.18063, Table 2 + Sec 3-4), for the
frozen pre-registered prediction document:
  research/2026-07-03_birefringence-hibef-prediction_registered.md

GATE: this driver only runs after the prior-art exposure scan returned CLEAN-FIELD
(research/2026-07-03_birefringence-prior-art-exposure-scan_result.md). It reuses the
GAP-1 readout chain (single source of truth) so every number traces to the same
delta_n -> dphi -> flip mapping validated in the GAP-1 result (PR #496).

DISCIPLINE:
  - consistency-vs-emergence: CONSISTENCY-class. Canonical clm-pp3qwf through the
    LoI's stated readout. No new clm/constant/emergence. Magnitude rides alpha-echo.
  - no-strawman: QED co-computed through the IDENTICAL chain; only delta_n differs.
  - frozen-prereg: predictions computed BEFORE any HIBEF pump-on data exists.

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/birefringence_hibef_scenario_predictions.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

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

from ave.bench import coefficient_ratio_differential_pvlas, substrate_identity_holds  # noqa: E402
from ave.core.constants import E_YIELD  # noqa: E402

# ============================================================================
# LoI SCENARIO PARAMETERS — LITERATURE INPUTS (LABELED). arXiv:2405.18063.
# ============================================================================
# ReLaX: W = 4.8 J, tau_FWHM = 30 fs, lambda = 800 nm (omega_L = 1.55 eV),
#   f/# focusing -> w_FWHM = #*1.3 um. Demonstrated peak intensity ~1e21 W/cm^2
#   (survey :71); LoI Eq.19 uses I_L = 1e21 for its N'/N ~ 1e-12 estimate; the
#   petawatt-upgrade DESIGN reaches ~1e22-1e23. We compute at BOTH.
# Probe X-ray (EuXFEL, Table 2): 8766 eV (Ge-440 dark-field analyser, Sec 4.2),
#   9835 eV (conventional-scenario Eq.27/28 standard, Sec 3.1), 12914 eV (high).
# Interaction length z ~ 10 um (single-pass focal overlap; survey :67).
Z_M: float = Z_INTERACTION_M

I_DEMONSTRATED_WCM2: float = 1e21   # ReLaX demonstrated peak (LoI Eq.19 estimate field)
I_DESIGN_LOW_WCM2: float = 1e22     # petawatt-upgrade design (LoI Sec 2.2 "additional challenges")
I_DESIGN_HIGH_WCM2: float = 1e23    # petawatt-upgrade design upper


@dataclass(frozen=True)
class LoIScenario:
    """One frozen BIREF@HIBEF LoI scenario (probe energy x pump intensity)."""
    name: str
    probe_eV: float
    pump_wcm2: float
    pump_class: str          # 'demonstrated' or 'design (petawatt-upgrade)'
    loi_ref: str


# The frozen scenario grid: the LoI's stated probe energies x (demonstrated, design) pump.
LOI_SCENARIOS: tuple[LoIScenario, ...] = (
    LoIScenario("conventional-9835eV-demonstrated", 9835.0, I_DEMONSTRATED_WCM2,
                "demonstrated", "LoI Sec 3.1 Eq.27/28 (standard self-seeded probe); Eq.19 field"),
    LoIScenario("darkfield-8766eV-demonstrated", 8766.0, I_DEMONSTRATED_WCM2,
                "demonstrated", "LoI Sec 4.2 (Ge-440 dark-field analyser fixes 8766 eV)"),
    LoIScenario("high-12914eV-demonstrated", 12914.0, I_DEMONSTRATED_WCM2,
                "demonstrated", "LoI Table 2 high-energy self-seeded band (12-13 keV)"),
    LoIScenario("conventional-9835eV-design-1e22", 9835.0, I_DESIGN_LOW_WCM2,
                "design (petawatt-upgrade)", "LoI Sec 2.2 petawatt-upgrade design intensity"),
    LoIScenario("conventional-9835eV-design-1e23", 9835.0, I_DESIGN_HIGH_WCM2,
                "design (petawatt-upgrade)", "LoI Sec 2.2 petawatt-upgrade design upper"),
)

# The LoI's own binding number: the record X-ray polarimeter purity floor.
P_POLARIMETER_RECORD: float = 8e-11    # LoI Sec 4.1 record (upper limit, photon-flux limited)
P_REQUIRED_1EM12: float = 1e-12        # LoI Sec 4.1 conclusion: '~1e-12 extinction must be shown'


def predict_scenario(sc: LoIScenario) -> dict:
    """Compute AVE + QED flip-prob for one LoI scenario through the GAP-1 chain."""
    E = field_from_intensity_wcm2(sc.pump_wcm2)
    pt = hibef_point(E, sc.probe_eV, z_m=Z_M)
    # margins vs the LoI's own floors
    m_record = pt.P_ave_exact / P_POLARIMETER_RECORD
    m_req = pt.P_ave_exact / P_REQUIRED_1EM12
    return {
        "name": sc.name,
        "probe_eV": sc.probe_eV,
        "pump_wcm2": sc.pump_wcm2,
        "pump_class": sc.pump_class,
        "loi_ref": sc.loi_ref,
        "E_field": E,
        "A2": (E / E_YIELD) ** 2,
        "wavelength_pm": pt.wavelength_m * 1e12,
        "dn_ave_differential": pt.dn_ave,
        "dn_qed_differenced": pt.dn_qed,
        "dphi_ave_rad": pt.dphi_ave,
        "P_ave_exact": pt.P_ave_exact,
        "P_ave_perturbative": pt.P_ave_pert,
        "P_qed_exact": pt.P_qed_exact,
        "ave_over_qed": pt.P_ave_exact / pt.P_qed_exact,
        "margin_vs_record_8e-11": m_record,
        "margin_vs_required_1e-12": m_req,
        "ave_clears_record_floor": bool(pt.P_ave_exact >= P_POLARIMETER_RECORD),
        "qed_clears_record_floor": bool(pt.P_qed_exact >= P_POLARIMETER_RECORD),
        "ave_perturbative_breaks_over_unity": pt.ave_perturbative_breaks,
    }


def main() -> None:
    out: dict = {}
    print("=" * 78)
    print("BIREF@HIBEF SCENARIO PREDICTIONS (frozen forward prediction, pre-data)")
    print("=" * 78)

    # liveness
    id_ok = substrate_identity_holds()
    # CORRECTED (2026-07-03): PVLAS-anchored ratio (propagating/LoI-matched
    # 7.5 pi/alpha^2 ~ 4.42e5; static 15 pi/alpha^2 ~ 8.85e5). The old
    # 7.5/alpha^3 ~ 1.93e7 was too large by 1/(2 pi alpha) (understated QED denom).
    ratio = coefficient_ratio_differential_pvlas(geometry="propagating")
    out["substrate_identity_holds"] = id_ok
    out["matched_differential_ratio_7.5pi_over_alpha2_propagating"] = ratio
    out["matched_differential_ratio_15pi_over_alpha2_static"] = (
        coefficient_ratio_differential_pvlas(geometry="static"))
    print(f"\nsubstrate identity (E_crit/E_yield)^2=1/alpha: {id_ok}")
    print(f"matched differential ratio (CORRECTED, propagating) 7.5 pi/alpha^2 = "
          f"{ratio:.4e} (field-independent)")
    print(f"LoI floors: record polarimeter purity {P_POLARIMETER_RECORD:.0e}, "
          f"required-to-show {P_REQUIRED_1EM12:.0e}")

    print("\nPER-SCENARIO PREDICTION (AVE canonical differential vs QED differenced, "
          "z=10um single-pass):")
    scenarios = []
    for sc in LOI_SCENARIOS:
        p = predict_scenario(sc)
        scenarios.append(p)
        print(f"\n  [{p['name']}]  ({p['pump_class']})")
        print(f"    probe {p['probe_eV']:.0f} eV (lambda={p['wavelength_pm']:.1f} pm), "
              f"pump {p['pump_wcm2']:.0e} W/cm^2 -> E={p['E_field']:.2e} V/m, A^2={p['A2']:.2e}")
        print(f"    dn_ave(diff) = {p['dn_ave_differential']:.3e}   "
              f"dn_qed(3/45)  = {p['dn_qed_differenced']:.3e}")
        print(f"    dphi_ave = {p['dphi_ave_rad']:.3e} rad")
        print(f"    P_ave(exact) = {p['P_ave_exact']:.3e}   "
              f"P_ave(pert) = {p['P_ave_perturbative']:.3e}   "
              f"(breaks>1: {p['ave_perturbative_breaks_over_unity']})")
        print(f"    P_qed(exact) = {p['P_qed_exact']:.3e}   AVE/QED = {p['ave_over_qed']:.3e}")
        print(f"    margin vs record 8e-11: {p['margin_vs_record_8e-11']:.3e}  "
              f"(AVE clears record: {p['ave_clears_record_floor']}, "
              f"QED clears record: {p['qed_clears_record_floor']})")
    out["scenarios"] = scenarios

    # roll-up: the kill logic both ways
    print("\nKILL LOGIC (frozen, both ways):")
    print("  - null-above-floor (measured flip-prob at or below the QED co-prediction, i.e. no")
    print("    AVE-sized signal where the polarimeter can resolve it) KILLS clm-pp3qwf + the")
    print("    E-route falsifier (leaf :55: 'a QED-sized differential coefficient falsifies AVE').")
    print("  - signal at AVE level (flip-prob ~ P_ave, ~7 OOM above QED and above floor) = the")
    print("    chord (leaf :55: 'an AVE-sized coefficient falsifies QED at this observable').")
    out["kill_logic"] = {
        "null_above_floor_kills": "clm-pp3qwf + E-route falsifier (leaf :55)",
        "signal_at_ave_level": "chord confirmed (leaf :55)",
        "e2_slope_alone": "does NOT falsify AVE (QED is also E^2-leading; coefficient is the discriminator)",
    }

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "birefringence_hibef_scenario_predictions.json"
    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nResults written: {out_path}")
    print("=" * 78)


if __name__ == "__main__":
    main()
