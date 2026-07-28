"""Programmatic number check for the continuum radial-solver stage-1 result doc.

★WHY THIS EXISTS.  The PR #801 adversarial review found THREE separate cases of
numbers RETYPED rather than read from the shipped JSON (F5 the G4 per-decade
values, F13 the illustration values, F14 `_runtime_sec`) — all of them inside
sections that declared their numbers were read from the JSON.  Care is not a
remedy for that; a check is.

WHAT IT DOES.  It scans every inline-code token in
`research/2026-07-28_continuum-radial-solver-stage1_result.md` that parses as a
number, and requires each one to be either

  (a) REGISTERED — mapped to a path in a shipped JSON (this lane's results, the
      #796 vessel-state bench, or the #782 RVE bench), or to a derived quantity
      computed FROM those JSONs by an explicit formula.  The token must be the
      correctly-rounded value at its own quoted precision; or
  (b) ALLOW-LISTED — a frozen tolerance / threshold, a geometry constant, a
      digest, a section or PR number, or a plain integer, each with a reason.

Anything else FAILS.  So a number cannot enter the result doc by being typed:
it enters by being registered against its source.

★A THIRD CATEGORY, added by the #801 re-verify (R3 / WARN-4): NON_REGISTRABLE.
`_runtime_sec` is machine-dependent and is excluded from the frozen determinism
digest by the prereg's own §7 (vi) definition.  Registering a doc token against
it made this tool go MISMATCH -> FAIL on every honest re-run on every machine —
a self-defeating check.  The runtime numeral is DROPPED from the result doc
(not allow-listed: an allow-listed numeral is a typed number that is never
verified, which is the exact defect this tool exists to remove), and `main()`
now refuses any future attempt to register or allow-list it.

★WIRING (R4 / WARN-5): this runs as a GATING step of `make verify` via the
`verify-lane-number-checks` target, so it protects the doc continuously rather
than only at the moment someone runs it by hand.  It is hermetic — stdlib only,
three in-tree JSONs, one in-tree doc, no `ave` import, no network, no RNG,
sub-second — so it is safe in CI.

Run:  python3 research/drivers/continuum_radial_solver_number_check.py
      (or `make verify-lane-number-checks`)
"""

from __future__ import annotations

import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(REPO, "research",
                   "2026-07-28_continuum-radial-solver-stage1_result.md")

SOURCES = {
    "stage1": os.path.join(HERE, "continuum_radial_solver_stage1_results.json"),
    "vessel796": os.path.join(HERE, "vessel_state_rve_results.json"),
    "rve782": os.path.join(HERE, "rve_aggregation_bench_results.json"),
}

J = {k: json.load(open(v)) for k, v in SOURCES.items()}


def path(src: str, dotted: str):
    """Walk a shipped JSON.  Separator is '>>' because some result keys (e.g.
    'displacement|kr=0.001') contain a pipe."""
    node = J[src]
    for part in dotted.split(">>"):
        node = node[int(part)] if part.lstrip("-").isdigit() else node[part]
    return node


def S(p):
    return path("stage1", p)


G = "gates>>"
LV = "liveness_demonstration>>"
SH = "grade_shape_scope>>rows>>"

# ---------------------------------------------------------------------------
# (a) REGISTERED tokens: doc token -> value drawn from a shipped JSON.
#     A `lambda` entry is a DERIVED quantity with its formula visible here.
# ---------------------------------------------------------------------------
REGISTERED = {
    # --- gate worst-case values (as quoted, and at full precision) ---
    "2.7003e-14": lambda: S(G + "G1_lame_static>>lame_ratio_worst"),
    "2.7002675694072622e-14": lambda: S(G + "G1_lame_static>>lame_ratio_worst"),
    "6.0687e-03": lambda: S(G + "G1_lame_static>>shell_agreement_worst"),
    "1.8763e-13": lambda: S(G + "G2_uniform_null>>worst_deviation"),
    "0.0000e+00": lambda: S(G + "G3_ortho_to_iso_reduction>>rel_worst"),
    "4.8581e-07": lambda: S(G + "G4_TM_vs_matched_asymptotics>>worst_rel"),
    "4.858126515168571e-07": lambda: S(G + "G4_TM_vs_matched_asymptotics>>worst_rel"),
    "1.4062e-13": lambda: S(G + "G5_ax3_lossless>>worst_rel_imbalance"),
    "1.406175503036591e-13": lambda: S(G + "G5_ax3_lossless>>worst_rel_imbalance"),
    "1.0433e-04": lambda: S(G + "G6_layer_refinement>>worst_rel"),
    "1.0432960302206345e-04": lambda: S(G + "G6_layer_refinement>>worst_rel"),
    "2.9550e-13": lambda: S(G + "G7_drive_amplitude_independence>>worst_rel"),
    "2.9550062722232135e-13": lambda: S(G + "G7_drive_amplitude_independence>>worst_rel"),
    "5.0136e-11": lambda: S(G + "G8_matching_radius_independence>>worst_rel"),
    "5.0136185296992416e-11": lambda: S(G + "G8_matching_radius_independence>>worst_rel"),
    "5.0202e+10": lambda: S(G + "G9_band_conditioning>>worst_cond"),
    "5.02e10": lambda: S(G + "G9_band_conditioning>>worst_cond"),
    "50202390756.2205": lambda: S(G + "G9_band_conditioning>>worst_cond"),
    "0.0": lambda: S(G + "G3_ortho_to_iso_reduction>>rel_worst"),
    # --- G4 per-decade scaling (the F5 retype) ---
    "4.858127e-07": lambda: S(G + "G4_TM_vs_matched_asymptotics>>rows>>"
                                  "displacement|kr=0.001>>rel"),
    "4.856897e-09": lambda: S(G + "G4_TM_vs_matched_asymptotics>>rows>>"
                                  "displacement|kr=0.0001>>rel"),
    "2.048368e-13": lambda: S(G + "G4_TM_vs_matched_asymptotics>>rows>>"
                                  "displacement|kr=1e-06>>rel"),
    "100.0253": lambda: (S(G + "G4_TM_vs_matched_asymptotics>>rows>>displacement|kr=0.001>>rel")
                         / S(G + "G4_TM_vs_matched_asymptotics>>rows>>displacement|kr=0.0001>>rel")),
    # --- self-tests ---
    "4.6477e-03": lambda: S("selftests>>FT1_lame_fireability>>"
                            "lame_ratio_graded_exterior_q0p10"),
    "3.3669e-03": lambda: S("selftests>>FT1_lame_fireability>>"
                            "lame_ratio_orthotropic_exterior_1p02_0p99"),
    "1.0120e-04": lambda: S("selftests>>FT2_null_liveness>>rho_S"),
    "1.011991659e-04": lambda: S("selftests>>FT2_null_liveness>>rho_S"),
    "2.9181e-01": lambda: S("selftests>>FT3_ax3_fireability>>rel_imbalance"),
    "6.2850e+00": lambda: S("selftests>>FT4_TM_MA_nonvacuity>>rel"),
    "3.1829e-04": lambda: S("selftests_repair_added>>"
                            "FT5_G3_ortho_normalization>>rel_worst"),
    "4.9127e-02": lambda: S("selftests_repair_added>>"
                            "FT6_G6_refinement_fireability>>rel"),
    "4.8706e-01": lambda: S("selftests_repair_added>>"
                            "FT7_G8_matching_radius_fireability>>rel_spread"),
    "1.5875e+15": lambda: S("selftests_repair_added>>"
                            "FT8_G9_band_floor_fireability>>cond_worst"),
    # --- FT-9 (#801 re-verify R1): the G7 fireability test + its R_match sweep ---
    "1.1932e-11": lambda: S("selftests_repair_added>>"
                            "FT9_G7_amplitude_fireability>>rel_worst"),
    "3.3556e-14": lambda: S("selftests_repair_added>>FT9_G7_amplitude_fireability"
                            ">>R_match_conditioning_sweep>>R_match=2.0"),
    "3.2399e-12": lambda: S("selftests_repair_added>>FT9_G7_amplitude_fireability"
                            ">>R_match_conditioning_sweep>>R_match=8.0"),
    "11.9": lambda: S("selftests_repair_added>>"
                      "FT9_G7_amplitude_fireability>>breaches_G7_by_factor"),
    "1.2": lambda: S("selftests_repair_added>>"
                     "FT9_G7_amplitude_fireability>>rel_worst") / 1e-11,
    # --- FT-1's G1b shell-agreement coverage (#801 re-verify R5) ---
    "2.2530": lambda: S("selftests>>FT1_lame_fireability>>"
                        "shell_agreement_graded_exterior_q0p10"),
    "2.1454": lambda: S("selftests>>FT1_lame_fireability>>"
                        "shell_agreement_orthotropic_exterior_1p02_0p99"),
    "9.0": lambda: S("selftests>>FT1_lame_fireability>>"
                     "shell_agreement_graded_exterior_q0p10") / 0.25,
    "8.6": lambda: S("selftests>>FT1_lame_fireability>>"
                     "shell_agreement_orthotropic_exterior_1p02_0p99") / 0.25,
    # --- runtime: DELIBERATELY ABSENT.  See NON_REGISTRABLE below (re-verify R3).
    # --- margins: tolerance / measured, computed here, never typed ---
    "3.7e3": lambda: 1e-10 / S(G + "G1_lame_static>>lame_ratio_worst"),
    "3.6": lambda: math.log10(1e-10 / S(G + "G1_lame_static>>lame_ratio_worst")),
    "41": lambda: 0.25 / S(G + "G1_lame_static>>shell_agreement_worst"),
    "5.3": lambda: 1e-12 / S(G + "G2_uniform_null>>worst_deviation"),
    "2.1": lambda: 1e-6 / S(G + "G4_TM_vs_matched_asymptotics>>worst_rel"),
    "0.3": lambda: math.log10(1e-6 / S(G + "G4_TM_vs_matched_asymptotics>>worst_rel")),
    "7.1e2": lambda: 1e-10 / S(G + "G5_ax3_lossless>>worst_rel_imbalance"),
    "9.6": lambda: 1e-3 / S(G + "G6_layer_refinement>>worst_rel"),
    "3.4": lambda: 1e-12 / S(G + "G7_drive_amplitude_independence>>worst_rel"),
    "20": lambda: 1e-9 / S(G + "G8_matching_radius_independence>>worst_rel"),
    # --- self-test margins ---
    "4.6": lambda: S("selftests>>FT1_lame_fireability>>"
                     "lame_ratio_graded_exterior_q0p10") / 1e-3,
    "10": lambda: S("selftests>>FT2_null_liveness>>rho_S") / 1e-5,
    "29": lambda: S("selftests>>FT3_ax3_fireability>>rel_imbalance") / 1e-2,
    "63": lambda: S("selftests>>FT4_TM_MA_nonvacuity>>rel") / 1e-1,
    "6.3": lambda: S("selftests>>FT4_TM_MA_nonvacuity>>rel"),
    "318": lambda: S("selftests_repair_added>>"
                     "FT5_G3_ortho_normalization>>rel_worst") / 1e-6,
    "4.9": lambda: S("selftests_repair_added>>"
                     "FT6_G6_refinement_fireability>>rel") / 1e-2,
    "49": lambda: S("selftests_repair_added>>"
                    "FT6_G6_refinement_fireability>>rel") / 1e-3,
    "4.9e7": lambda: S("selftests_repair_added>>"
                       "FT7_G8_matching_radius_fireability>>rel_spread") / 1e-8,
    "159": lambda: S("selftests_repair_added>>"
                     "FT8_G9_band_floor_fireability>>cond_worst") / 1e13,
    "4.6e7": lambda: S("selftests>>FT1_lame_fireability>>"
                       "lame_ratio_graded_exterior_q0p10") / 1e-10,
    "3.4e7": lambda: S("selftests>>FT1_lame_fireability>>"
                       "lame_ratio_orthotropic_exterior_1p02_0p99") / 1e-10,
    "1.7e11": lambda: (S("selftests>>FT1_lame_fireability>>"
                         "lame_ratio_graded_exterior_q0p10")
                       / S(G + "G1_lame_static>>lame_ratio_worst")),
    # --- D1 lever / cold medium ---
    "3.2864": lambda: S("two_term_rho_report>>c2_lever>>"
                        "candidate_swap_ratio_cP2_over_cS2"),
    "0.30429": lambda: S("two_term_rho_report>>c2_lever>>"
                         "candidate_swap_ratio_cS2_over_cP2"),
    "0.51884": lambda: S("cold_medium>>cP"),
    "0.28621": lambda: S("cold_medium>>cS"),
    "0.281313": lambda: S("cold_medium>>nu_implied_from_lattice_speeds"),
    "0.285714": lambda: S("cold_medium>>nu_Hill_canon_N_NU"),
    "−1.54": lambda: 100.0 * S("cold_medium>>nu_rel_dev_vs_canon"),
    # --- D5 profile (read from the #796 JSON at driver runtime) ---
    "0.35299364830704594": lambda: path("vessel796", "verdict>>"
                                        "fixed_budget_headline>>min_kse"),
    "0.13946745063352736": lambda: path("vessel796", "verdict>>"
                                        "fixed_budget_headline>>peak_A"),
    "9.77337": lambda: path("vessel796", "provenance>>constants>>k_a_RHO_STAR"),
    "0.352994": lambda: S("d5_profile>>radial_gain"),
    "2.363067": lambda: S("d5_profile>>hoop_gain"),
    "−0.0662009": lambda: S("d5_profile>>eps_radial_extremum"),
    "0.1394675": lambda: S("d5_profile>>eps_hoop_extremum"),
    "0.2954759": lambda: S("d5_profile>>K_tan_over_K0_796"),
    # --- R2 two-term report ---
    "0.489462": lambda: S("two_term_rho_report>>rows>>0>>phi_sf_lattice"),
    "0.000000": lambda: S("two_term_rho_report>>rows>>0>>"
                          "term_ii_trapped_energy_rho_over_rho0"),
    "1.468386": lambda: S("two_term_rho_report>>rows>>2>>"
                          "term_ii_trapped_energy_rho_over_rho0"),
    "0.543577": lambda: S("two_term_rho_report>>rows>>0>>r_Z_family"),
    "0.663400": lambda: S("two_term_rho_report>>rows>>1>>r_Z_family"),
    "0.854019": lambda: S("two_term_rho_report>>rows>>2>>r_Z_family"),
    # --- liveness demonstration ---
    "0.413549": lambda: S(LV + "isotropic_baseline>>displacement>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.586451": lambda: S(LV + "isotropic_baseline>>displacement>>"
                               "rho_S_matched_asymptotics_k_to_0"),
    "0.431136": lambda: S(LV + "isotropic_baseline>>displacement>>"
                               "rho_N_by_k_r_core>>0.3"),
    "3.012703": lambda: S(LV + "isotropic_baseline>>displacement>>"
                               "rho_N_by_k_r_core>>3.0"),
    "0.439371": lambda: S(LV + "isotropic_baseline>>traction>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.560629": lambda: S(LV + "isotropic_baseline>>traction>>"
                               "rho_S_matched_asymptotics_k_to_0"),
    "0.457842": lambda: S(LV + "isotropic_baseline>>traction>>"
                               "rho_N_by_k_r_core>>0.3"),
    "1.244858": lambda: S(LV + "isotropic_baseline>>traction>>"
                               "rho_N_by_k_r_core>>3.0"),
    "0.026520": lambda: S(LV + "D5_orthotropic_measured>>displacement>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.973480": lambda: S(LV + "D5_orthotropic_measured>>displacement>>"
                               "rho_S_matched_asymptotics_k_to_0"),
    "0.028321": lambda: S(LV + "D5_orthotropic_measured>>displacement>>"
                               "rho_N_by_k_r_core>>0.3"),
    "0.232244": lambda: S(LV + "D5_orthotropic_measured>>displacement>>"
                               "rho_N_by_k_r_core>>3.0"),
    "0.028433": lambda: S(LV + "D5_orthotropic_measured>>traction>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.971567": lambda: S(LV + "D5_orthotropic_measured>>traction>>"
                               "rho_S_matched_asymptotics_k_to_0"),
    "0.030268": lambda: S(LV + "D5_orthotropic_measured>>traction>>"
                               "rho_N_by_k_r_core>>0.3"),
    "1.159893": lambda: S(LV + "D5_orthotropic_measured>>traction>>"
                               "rho_N_by_k_r_core>>3.0"),
    "3.2e-08": lambda: S(LV + "isotropic_baseline>>displacement>>"
                              "fitted_exponent_p_over_subresonant_tail"),
    "5.1e-08": lambda: S(LV + "D5_orthotropic_measured>>displacement>>"
                              "fitted_exponent_p_over_subresonant_tail"),
    "5e-8": lambda: S(LV + "D5_orthotropic_measured>>displacement>>"
                           "fitted_exponent_p_over_subresonant_tail"),
    "0.41": lambda: S(LV + "isotropic_baseline>>displacement>>"
                           "rho_N_matched_asymptotics_k_to_0"),
    "4.8e-08": lambda: S(LV + "D5_orthotropic_measured>>traction>>"
                              "fitted_exponent_p_over_subresonant_tail"),
    # --- grade-shape scope (F6) ---
    "0.6478": lambda: S(SH + "grade_power=0.1>>band_fraction_with_S_le_0p1"),
    "0.018165": lambda: S(SH + "grade_power=0.1>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.0991": lambda: S(SH + "grade_power=1.0>>band_fraction_with_S_le_0p1"),
    "0.247949": lambda: S(SH + "grade_power=1.0>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.0508": lambda: S(SH + "grade_power=2.0>>band_fraction_with_S_le_0p1"),
    "5.1": lambda: 100.0 * S(SH + "grade_power=2.0>>band_fraction_with_S_le_0p1"),
    "0.0130": lambda: S(SH + "grade_power=8.0>>band_fraction_with_S_le_0p1"),
    "0.748953": lambda: S(SH + "grade_power=8.0>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "0.0033": lambda: S(SH + "grade_power=32.0>>band_fraction_with_S_le_0p1"),
    "0.923793": lambda: S(SH + "grade_power=32.0>>"
                               "rho_N_matched_asymptotics_k_to_0"),
    "1.7063": lambda: S("grade_shape_scope>>"
                        "rho_N_orders_of_magnitude_moved_by_shape_alone"),
    "50.9": lambda: (S("grade_shape_scope>>rho_N_span_over_shape_family")[1]
                     / S("grade_shape_scope>>rho_N_span_over_shape_family")[0]),
    "1.8": lambda: 100.0 * S("grade_shape_scope>>rho_N_span_over_shape_family")[0],
    # --- #782, the F10 correction: the numbers that actually belong to it ---
    "0.6261": lambda: path("rve782", "leg2_lame_gate>>bulk_only_cold>>"
                                     "frozen_shell_agreement_rel"),
    "0.5853": lambda: path("rve782", "leg2_lame_gate>>bulk_only_compressed>>"
                                     "frozen_shell_agreement_rel"),
    "0.5680": lambda: path("rve782", "leg2_lame_gate>>symmetric_cold>>"
                                     "frozen_shell_agreement_rel"),
    "0.036": lambda: path("rve782", "leg2_lame_gate>>bulk_only_cold>>"
                                    "deliverable_exterior_over_interior_max"),
}

# ---------------------------------------------------------------------------
# (b) ALLOW-LIST: numeric tokens that are NOT measurements, with the reason.
# ---------------------------------------------------------------------------
ALLOWED = {
    # frozen tolerances / thresholds quoted from the prereg
    "1e-10": "frozen G1 tolerance", "0.25": "frozen G1b tolerance",
    "1e-12": "frozen G2/G3/G7 tolerance", "1e-6": "frozen G4 tolerance",
    "1e-14": "frozen G5b tolerance", "1e-3": "frozen G6 tol / FT-1 thr / absorb",
    "1e-9": "frozen G8 tolerance", "1e12": "frozen G9 tolerance",
    "1e-5": "frozen FT-2 threshold", "1e-2": "frozen FT-3 / FT-6 threshold",
    "1e-1": "frozen FT-4 threshold", "1e13": "FT-8 repair threshold",
    "1e-8": "FT-7 repair threshold / band bottom", "1e7": "prereg FT-1 headroom",
    "1e6": "FT-5 headroom statement", "0.10": "#782 deliverable tol / FT-1 grade q",
    # geometry / configuration constants
    "1.0": "unit gain", "0.99": "FT-2 contrast / FT-1 exterior ortho",
    "1.02": "FT-1 exterior ortho", "0.30": "source surface r_s",
    "3.0": "band point", "1e-11": "FT-8 evaluation point",
    "1e-4": "band point", "0.3": "band point", "1e+6": "G7 amplitude top",
    "1e-06": "band point", "0.001": "band point", "0.0001": "band point",
    "2": "layer/section counts", "4": "R_match / order counts",
    "8": "exterior layers / counts", "16": "R_match sweep",
    "192": "FT-6 layer count", "384": "FT-6 layer count", "256": "frozen n_shell",
    "265": "layer count of the caged stack", "512": "2x n_shell",
    "0.1": "grade_power probe point", "32": "grade_power probe point",
    "2.0": "frozen grade_power", "4.0": "band top / R_match",
    "8.0": "grade_power probe point", "32.0": "grade_power probe point",
    "−1": "Gamma_bulk = -1, the pressure-release wall",
    "−3": "basis dynamic-range exponent x^(-3)",
    "600": "frozen runtime budget", "0.5": "interior probe radius",
    "1.5": "exterior probe radius", "2.5": "exterior probe radius",
    "3.5": "exterior probe radius", "1e-25": "the unsatisfiable regime",
    "1e75": "basis dynamic range at 1e-25", "2.20e-16": "float64 epsilon scale",
    "2.2204e-16": "pre-repair G2 under the transfer-kernel mutation",
    "5.2800e-07": "repaired G2 under the transfer-kernel mutation (out-of-tree)",
    "1.9100e-04": "repaired G3 under the ortho_layer mutation (out-of-tree)",
    "0.05788": "reviewer's mutation receipt, B_ortho before",
    "0.05824": "reviewer's mutation receipt, B_ortho after",
    "1e-9)": "guard", "0.519": "charter I8 verbatim quote", "0.286": "charter I8 verbatim quote",
    "1.011991657e-04": "the PRE-repair FT-2 value, quoted as the before-state",
    "0.059": "#796 C-V flatness, quoted from its result doc",
    "0.65": "#770 transient value quoted from #782",
    "0.038": "#782 internal validation, quoted",
    "0.014": "#782 RVE-size gap, quoted",
    "0.026": "#782 quoted", "0.019": "#782 quoted", "0.007": "#782 quoted",
    "2.90": "#775 rho_N band top", "0.26": "#775 rho_N band bottom",
    "5": "section / count", "3": "count", "1": "count", "0": "count",
    "9": "gate count", "13": "significant figures", "7": "percent, scouting",
    "2/7": "canonical nu_Hill", "1e+0": "unit",
    "efea5059a98d0503b094737d9e7477b1d737dccba87bf9545916c6993cb25576": "digest",
    # out-of-tree mutation receipts (the mutated driver is never committed)
    "2.999999999997": "G7 under the wiring-error mutation (out-of-tree)",
    "5.665625e-13": "G7 under the common-mode mutation (out-of-tree)",
    "1e-11)": "guard",
}

# ---------------------------------------------------------------------------
# (c) NON-REGISTRABLE: shipped JSON fields that must NEVER back a doc token.
#     ★#801 re-verify R3 (WARN-4) — a self-defeating tool.
# ---------------------------------------------------------------------------
NON_REGISTRABLE = {
    "_runtime_sec": (
        "MACHINE-DEPENDENT, and excluded by the frozen determinism definition "
        "itself: prereg §7 (vi) freezes the digest as a SHA-256 over the "
        "results object MINUS timing fields, so the runtime is deliberately "
        "outside the reproducible surface. It changes on every run and on "
        "every machine. Registering a doc token against it made this tool FAIL "
        "on every re-run everywhere — the re-verify audit re-ran the driver, "
        "got 1.52 s against the doc's 1.47, and the tool went MISMATCH -> FAIL. "
        "A check that fails on every honest re-run is worse than no check: it "
        "trains its reader to ignore it. "
        "DISPOSITION = DROP THE TOKEN, not allow-list it. Allow-listing would "
        "leave a runtime numeral in the doc that entered by being TYPED and is "
        "then never verified against anything — precisely the property this "
        "tool exists to remove (F5/F13/F14 were three instances of it). The "
        "result doc therefore quotes NO runtime numeral; it cites the shipped "
        "field `_runtime_sec` and the frozen 600 s budget verdict "
        "`runtime_within_budget` instead."),
}


def self_check() -> list:
    """Refuse a future re-registration of a non-registrable field."""
    src = open(os.path.abspath(__file__)).read()
    reg_block = src.split("REGISTERED = {", 1)[1].split("\n}\n", 1)[0]
    allow_block = src.split("ALLOWED = {", 1)[1].split("\n}\n", 1)[0]
    out = []
    for key, why in NON_REGISTRABLE.items():
        if key in reg_block:
            out.append(f"SELF-CHECK  REGISTERED references the non-registrable "
                       f"field `{key}`. {why}")
        if key in allow_block:
            out.append(f"SELF-CHECK  ALLOWED references the non-registrable "
                       f"field `{key}`. {why}")
    return out


NUM = re.compile(r"^[−-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
TOKEN = re.compile(r"`([^`]+)`")


def sig_digits(tok: str) -> int:
    m = tok.lstrip("−-").split("e")[0].split("E")[0]
    d = m.replace(".", "").lstrip("0")
    return max(len(d), 1)


def as_float(tok: str) -> float:
    return float(tok.replace("−", "-"))


def rounds_to(value: float, tok: str) -> bool:
    n = sig_digits(tok)
    try:
        return float("%.{}g".format(n) % float(value)) == as_float(tok)
    except (TypeError, ValueError):
        return False


def main() -> int:
    text = open(DOC).read()
    seen, checked, allowed_n, unaccounted = set(), 0, 0, 0
    bad = list(self_check())
    for raw in TOKEN.findall(text):
        for tok in re.split(r"[\s,;:()\[\]{}=<>×/]+", raw):
            tok = tok.strip("`*_.'\"")
            if not tok or tok in seen:
                continue
            if not NUM.match(tok):
                continue
            seen.add(tok)
            if tok in REGISTERED:
                val = REGISTERED[tok]()
                checked += 1
                if not rounds_to(val, tok):
                    bad.append(f"MISMATCH  `{tok}`  <-  JSON value {val!r} "
                               f"(rounds to {float('%.{}g'.format(sig_digits(tok)) % float(val))!r})")
            elif tok in ALLOWED:
                allowed_n += 1
            else:
                unaccounted += 1
                bad.append(f"UNREGISTERED  `{tok}`  — not mapped to a JSON path "
                           f"and not allow-listed. Register it or justify it.")
    print(f"[number-check] doc: {os.path.relpath(DOC, REPO)}")
    print(f"[number-check] distinct numeric tokens: {len(seen)}  |  "
          f"registered-and-verified: {checked}  |  "
          f"allow-listed: {allowed_n}  |  unaccounted: {unaccounted}")
    for b in bad:
        print("  " + b)
    if bad:
        print(f"[number-check] FAIL — {len(bad)} finding(s)")
        return 1
    print("[number-check] PASS — every quoted number is the correctly-rounded "
          "value of its registered JSON source, or an allow-listed constant")
    return 0


if __name__ == "__main__":
    sys.exit(main())
