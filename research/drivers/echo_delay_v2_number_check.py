#!/usr/bin/env python3
"""Gating numeral check for the echo-delay v2 rerun + Y8 reach-through result doc.

Every BACKTICKED numeral in ``research/2026-08-05_echo-delay-v2-reach-through_result.md``
must either be REGISTERED against a value in the shipped
``research/drivers/echo_delay_v2_reach_through_results.json`` (or recomputed from
it) or be ALLOW-LISTED with a stated reason.  An unregistered numeral is a FAIL.

ALL SIX ACCUMULATED CHECKER LESSONS, PLUS THIS LANE'S SEVENTH
-------------------------------------------------------------
Prereg section 10, frozen: the checker implements from the first commit
(i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced at BOTH the
configuration and document ends; (ii) PER-SITE rather than global dedup;
(iii) LIST-VALUED REGISTRATION; (iv) a NEWLINE-EXCLUDING token pattern;
(v) a COMPLETENESS GUARD making any registered key the document never
exercises a hard configuration FAIL; (vi) a DIGEST CLASSIFIER; and
(vii) -- NEW IN THIS LANE -- a MUTATION RECEIPT: ``--mutation-receipt``
perturbs a registered value and asserts the checker returns non-zero, so the
checker itself is demonstrated FIREABLE rather than assumed to be.

SCOPE, NARROWED DELIBERATELY (prereg section 10, frozen): "the gating number
check scans the RESULT DOC only; no claim is made anywhere in this lane that
this prereg is machine-checked".
"""
from __future__ import annotations

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research",
                   "2026-08-05_echo-delay-v2-reach-through_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "echo_delay_v2_reach_through_results.json")

with open(JSON_PATH, encoding="utf-8") as _fh:
    J = json.load(_fh)

MIN_SIG_DIGITS = 3
_MUTATE = False


def P(path):
    """Read a '/'-separated path out of the shipped object."""
    cur = J
    for part in path.strip("/").split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    if _MUTATE and isinstance(cur, str):
        try:
            return repr(float(cur) * 1.5)
        except ValueError:
            return cur
    if _MUTATE and isinstance(cur, (int, float)):
        return cur * 1.5
    return cur


def _cfgrow(tag, i, key):
    return P(f"configurations/{tag}/rows/{i}/{key}")


# --- REGISTERED: token -> a callable returning the shipped value ------------
REGISTERED = {
    '170': lambda: P('/self_tests/FT-W/rows/0/W'),
    '171': lambda: P('/gates/G-NC-V1B/compared'),
    '-0.21936446048145797': lambda: P('/self_tests/FT-W/rows/1/junction_B_over_Z1/im'),
    '-1.0283538461528556': lambda: P('/self_tests/FT-W/rows/1/junction_C_times_Z1/im'),
    '0.00034240195625884296': lambda: P('/bins/BIN-DISC/rows/1/tau_ring_s'),
    '0.000453': lambda: P('/self_tests/FT-TURN/S_turn'),
    '0.0010000000000004532': lambda: P('/gates/G-KWIN/z_plane_over_z1_primary_cfg_per_K/1000000'),
    '0.0013207349980956485': lambda: P('/bins/BIN-DISC/rows/0/abs_diff_s'),
    '0.0021228921288048263': lambda: P('/bins/BIN-DISC/rows/2/tau_ring_s'),
    '0.0021382974966202216': lambda: P('/configurations/CFG-A/rows/2/r_sat_over_c0_s'),
    '0.0031622776601685281': lambda: P('/gates/G-KWIN/z_plane_over_z1_primary_cfg_per_K/100000'),
    '0.0034240195625884296': lambda: P('/bins/BIN-DISC/rows/3/tau_ring_s'),
    '0.0049751243781094578': lambda: P('/self_tests/FT-RT-C/abs_gamma'),
    '0.0050831705640662639': lambda: P('/y8/reach_through/per_configuration/5/T_squared_min'),
    '0.00694444': lambda: P('/self_tests/FT-U/measured'),
    '0.007833389253405541': lambda: P('/y8/reach_through/R_min_over_all'),
    '0.0097563731927808699': lambda: P('/y8/reach_through/per_configuration/2/R_matched_min'),
    '0.010000000000000047': lambda: P('/gates/G-KWIN/z_plane_over_z1_primary_cfg_per_K/10000'),
    '0.014001480939037623': lambda: P('/bins/BIN-DISC/rows/1/abs_diff_s'),
    '0.0167407': lambda: P('/self_tests/FT-UNIT/measured_abs_dev'),
    '0.024143643391219775': lambda: P('/y8/reach_through/per_configuration/0/R_matched_min'),
    '0.024786408263925783': lambda: P('/y8/reach_through/per_configuration/4/R_matched_min'),
    '0.0487309': lambda: P('/self_tests/FT-EVAN/max_omega_max_over_omega'),
    '0.049373451650013084': lambda: P('/y8/reach_through/per_configuration/1/R_matched_min'),
    '0.055207950189327304': lambda: P('/bins/BIN-CUTOFF/CFG-B/spread'),
    '0.060897604264343763': lambda: P('/y8/reach_through/per_configuration/5/contact_spread_max'),
    '0.06477165384496919': lambda: P('/y8/reach_through/per_configuration/4/T_squared_min'),
    '0.085629935420768133': lambda: P('/y8/reach_through/per_configuration/2/R_matched_band_centre'),
    '0.087147754287058579': lambda: P('/gates/G-KWIN/abs_gamma_at_band_centre_primary_cfg_per_K/1000000'),
    '0.090710611005686024': lambda: P('/bins/BIN-DISC/rows/2/abs_diff_s'),
    '0.103205': lambda: P('/self_tests/FT-PEAK/measured'),
    '0.12470968062705699': lambda: P('/self_tests/FT-W/rows/0/junction_A/abs'),
    '0.14795611897118914': lambda: P('/bins/BIN-DISC/rows/3/abs_diff_s'),
    '0.190451': lambda: P('/self_tests/FT-SUM/measured'),
    '0.19595488353083484': lambda: P('/self_tests/FT-W/rows/0/junction_B_over_Z1/abs'),
    '0.21689588446181859': lambda: P('/gates/G-KWIN/abs_gamma_at_band_centre_primary_cfg_per_K/100000'),
    '0.27889663204515402': lambda: P('/gates/G-KWIN/abs_gamma_at_band_centre_primary_cfg_per_K/10000'),
    '0.28860783245076643': lambda: P('/gates/G-DISC/rows/0/derived_K_disc_oneway'),
    '0.28860783245078786': lambda: P('/gates/G-DISC/rows/0/measured_K_disc_oneway'),
    '0.38460541760664846': lambda: P('/self_tests/FT-W/rows/1/junction_A/abs'),
    '0.39672783364561331': lambda: P('/y8/reach_through/per_configuration/5/D_mirror_over_rsat_c0_min'),
    '0.4009298826322039': lambda: P('/configurations/CFG-A/J_A_closed'),
    '0.55985042457310985': lambda: P('/y8/reach_through/per_configuration/2/R_matched_max'),
    '0.57201415970765805': lambda: P('/gates/G-PEAK/per_branch/RHO-B/A_peak'),
    '0.57721566490153286': lambda: P('/gates/G-DISC/rows/0/round_trip_2K_disc'),
    '0.58274452584183356': lambda: P('/y8/reach_through/per_configuration/3/R_matched_max'),
    '0.59977908389481405': lambda: P('/y8/reach_through/per_configuration/0/R_matched_max'),
    '0.60897740865752781': lambda: P('/y8/reach_through/per_configuration/1/R_matched_max'),
    '0.62914651574476244': lambda: P('/y8/reach_through/per_configuration/1/T_squared_min'),
    '0.63518142273073909': lambda: P('/gates/G-DISC/rows/1/derived_K_disc_oneway'),
    '0.63518142273075926': lambda: P('/gates/G-DISC/rows/1/measured_K_disc_oneway'),
    '0.64026505052229754': lambda: P('/y8/reach_through/per_configuration/0/T_squared_min'),
    '0.641547': lambda: P('/gates/G-KWIN/worst_abs_spread'),
    '0.6604088176013766': lambda: P('/y8/reach_through/per_configuration/3/T_squared_min'),
    '0.68656750210530859': lambda: P('/y8/reach_through/per_configuration/2/T_squared_min'),
    '0.72197046380103953': lambda: P('/gates/G-PEAK/per_branch/RHO-A/A_peak'),
    '0.80185976526437822': lambda: P('/configurations/CFG-A/rows/2/T_return_over_r_sat_c0'),
    '0.80185976526440779': lambda: P('/configurations/CFG-A/two_J_A'),
    '0.80185976526520965': lambda: P('/self_tests/FT-V1/mutated'),
    '0.8961659577662765': lambda: P('/y8/reach_through/per_configuration/5/D_mirror_over_rsat_c0_max'),
    '0.93910239573572574': lambda: P('/y8/reach_through/per_configuration/5/R_matched_min'),
    '0.9506265483502403': lambda: P('/y8/reach_through/per_configuration/1/contact_spread_max'),
    '0.96706167946642363': lambda: P('/self_tests/FT-W/rows/1/T_squared_through_depleted'),
    '0.96707204806830749': lambda: P('/y8/reach_through/per_configuration/4/R_matched_max'),
    '0.96960978625117666': lambda: P('/self_tests/FT-W/rows/0/T_squared_through_depleted'),
    '0.97521359173624567': lambda: P('/y8/reach_through/per_configuration/4/contact_spread_max'),
    '0.97585635660957626': lambda: P('/y8/reach_through/per_configuration/0/contact_spread_max'),
    '0.9902436268074265': lambda: P('/y8/reach_through/per_configuration/2/contact_spread_max'),
    '0.9921666107469662': lambda: P('/y8/reach_through/per_configuration/3/contact_spread_max'),
    '0.99216661074696622': lambda: P('/y8/reach_through/per_configuration/3/contact_spread_max'),
    '0.99745517665503836': lambda: P('/y8/reach_through/per_configuration/5/R_matched_max'),
    '0.99745517665503847': lambda: P('/y8/reach_through/R_max_over_all'),
    '0.99800199800199796': lambda: P('/self_tests/FT-RT-E/abs_gamma'),
    '0.999991': lambda: P('/self_tests/FT-DECADE/measured'),
    '1.0000000000000655': lambda: P('/y8/reach_through/per_configuration/8/contact_spread_max'),
    '1.00002e-12': lambda: P('/self_tests/FT-CANON/measured'),
    '1.07488e-11': lambda: P('/gates/G-DECADE/rows/3/derived_leading'),
    '1.07488e-13': lambda: P('/gates/G-DECADE/rows/4/derived_leading'),
    '1.07488e-5': lambda: P('/gates/G-DECADE/rows/0/derived_leading'),
    '1.07488e-7': lambda: P('/gates/G-DECADE/rows/1/derived_leading'),
    '1.07488e-9': lambda: P('/gates/G-DECADE/rows/2/derived_leading'),
    '1.07492e-5': lambda: P('/gates/G-DECADE/limb_a_worst_rel'),
    '1.09762e-9': lambda: P('/self_tests/FT-TURN/S_last'),
    '1.11022e-16': lambda: P('/gates/G-ABCD/worst_structural_dev'),
    '1.12595': lambda: P('/self_tests/FT-DISP/measured'),
    '1.2703628454614782': lambda: P('/gates/G-DISC/rows/1/round_trip_2K_disc'),
    '1.3850982140393763': lambda: P('/gates/G-PEAK/per_branch/RHO-A/r_peak_over_r_sat'),
    '1.39999e-13': lambda: P('/gates/G-UNIT/worst_abs_dev_per_K/100000'),
    '1.44774e-11': lambda: P('/gates/G-MFREE/worst_abs_spread'),
    '1.5965e-13': lambda: P('/gates/G-XTIE/worst_rel_sep'),
    '1.7482084718166324': lambda: P('/gates/G-PEAK/per_branch/RHO-B/r_peak_over_r_sat'),
    '1.8536552108408788': lambda: P('/gates/G-BAND/Omega_R'),
    '1.9019809107871689': lambda: P('/y8/depletion_width/crossing/2/margin_Omega_crit_over_band_top'),
    '10.764560991913617': lambda: P('/y8/reach_through/per_configuration/1/D_mirror_over_rsat_c0_min'),
    '10.8828': lambda: P('/y8/depletion_width/crossing/0/Omega_crit_for_W_ge_1'),
    '11.892081990477307': lambda: P('/y8/depletion_width/crossing/1/margin_Omega_crit_over_band_top'),
    '12.237459302716427': lambda: P('/gates/G-PEAK/per_branch/RHO-B/r_peak_over_GM_c2'),
    '123.93391710141162': lambda: P('/y8/reach_through/per_configuration/3/CHIRP_MEASURE_over_rsat_c0'),
    '14.392726722864362': lambda: P('/y8/reach_through/per_configuration/8/D_mirror_over_rsat_c0_min'),
    '14.392726722868321': lambda: P('/y8/reach_through/per_configuration/8/D_mirror_over_rsat_c0_max'),
    '146.5562313792023': lambda: P('/y8/reach_through/per_configuration/2/CHIRP_MEASURE_over_rsat_c0'),
    '147.45550145435237': lambda: P('/y8/reach_through/per_configuration/0/CHIRP_MEASURE_over_rsat_c0'),
    '169.13420557105463': lambda: P('/observational_pointer_diagnostic/RHO_A_ratio_pointer_over_T'),
    '17.0111': lambda: P('/y8/depletion_width/crossing/3/Omega_crit_for_W_ge_1'),
    '176.4903551176059': lambda: P('/y8/reach_through/per_configuration/1/CHIRP_MEASURE_over_rsat_c0'),
    '18.354114509011853': lambda: P('/bins/BIN-EVAN/CFG-B_beta_17.0111/omega_max_over_omega_innermost'),
    '2.0135330338655648': lambda: P('/self_tests/FT-W/rows/1/junction_D/abs'),
    '2.02048e-15': lambda: P('/gates/G-PREC/abs_diff'),
    '2.3675520776118169': lambda: P('/self_tests/FT-W/rows/0/junction_D/abs'),
    '2.58337e-18': lambda: P('/gates/G-BAND/rel_sep'),
    '2.84495e-16': lambda: P('/gates/G-ABCD/route_worst_abs_sep_under_FT_W'),
    '2.9339625207595943': lambda: P('/y8/reach_through/per_configuration/5/CHIRP_MEASURE_over_rsat_c0'),
    '2.96043': lambda: P('/self_tests/FT-CUT/measured'),
    '2.9604330615961116': lambda: P('/regulator_sweep/CFG-SYN/spread'),
    '2.9730467331100634': lambda: P('/y8/reach_through/per_configuration/4/D_mirror_over_rsat_c0_min'),
    '209.4048218578591': lambda: P('/y8/reach_through/per_configuration/4/CHIRP_MEASURE_over_rsat_c0'),
    '22.66459827655336': lambda: P('/y8/reach_through/per_configuration/3/D_mirror_over_rsat_c0_max'),
    '25.109318900017641': lambda: P('/y8/reach_through/per_configuration/2/D_mirror_over_rsat_c0_max'),
    '25.19290950500849': lambda: P('/y8/reach_through/per_configuration/0/D_mirror_over_rsat_c0_max'),
    '25.509196883896756': lambda: P('/y8/reach_through/per_configuration/4/D_mirror_over_rsat_c0_max'),
    '28.410321483614396': lambda: P('/y8/reach_through/per_configuration/1/D_mirror_over_rsat_c0_max'),
    '3.1376715360522114': lambda: P('/observational_pointer_diagnostic/RHO_B_ratio_pointer_over_T'),
    '3.17573e-14': lambda: P('/gates/G-DISC/rows/1/rel_sep'),
    '3.4240195625884296e-5': lambda: P('/bins/BIN-DISC/rows/0/tau_ring_s'),
    '3.5964571223467896': lambda: P('/self_tests/FT-W/rows/0/junction_C_times_Z1/abs'),
    '3.68818e-14': lambda: P('/configurations/CFG-A/rows/2/rel_sep_from_closed'),
    '3.7711e-50': lambda: P('/gates/G-DISP/worst_abs_sep'),
    '3.7875e-11': lambda: P('/gates/G-DECADE/rows/3/residual_vs_derived'),
    '3.7875e-13': lambda: P('/gates/G-DECADE/rows/4/residual_vs_derived'),
    '3.7875e-7': lambda: P('/gates/G-DECADE/rows/1/residual_vs_derived'),
    '3.7875e-9': lambda: P('/gates/G-DECADE/rows/2/residual_vs_derived'),
    '3.78771e-5': lambda: P('/gates/G-DECADE/limb_b_worst_residual'),
    '3.8039618215743379': lambda: P('/y8/depletion_width/crossing/0/margin_Omega_crit_over_band_top'),
    '3.83653e-29': lambda: P('/y8/rho_a/S_dep_over_S_last_at_band_centre'),
    '3.8615926772428334e-13': lambda: P('/canonical_inputs/l_node_m'),
    '3.93019e-14': lambda: P('/gates/G-UNIT/worst_abs_dev_per_K/10000'),
    '34.0222': lambda: P('/y8/depletion_width/crossing/1/Omega_crit_for_W_ge_1'),
    '38.572647555121522': lambda: P('/bins/BIN-DISC/rows/0/diff_over_tau'),
    '4.0093e-10': lambda: P('/self_tests/FT-JA/measured'),
    '4.22103e-42': lambda: P('/gates/G-JA/sep'),
    '4.72977e-12': lambda: P('/gates/G-UNIT/worst_abs_dev'),
    '4.95172e-12': lambda: P('/self_tests/FT-CF/measured'),
    '40.891942008803921': lambda: P('/bins/BIN-DISC/rows/1/diff_over_tau'),
    '42.729731659401589': lambda: P('/bins/BIN-DISC/rows/2/diff_over_tau'),
    '43.211236462486767': lambda: P('/bins/BIN-DISC/rows/3/diff_over_tau'),
    '48.757416585255579': lambda: P('/bins/BIN-DISC/rows/0/T_B_over_T_A'),
    '4c7926fd9954dfc7': lambda: P('/_digest'),
    '5.34553e-50': lambda: P('/gates/G-U/worst_abs_sep'),
    '5.4414': lambda: P('/y8/depletion_width/crossing/2/Omega_crit_for_W_ge_1'),
    '5.8709947439811122': lambda: P('/bins/BIN-EVAN/CFG-B_beta_5.4414/omega_max_over_omega_innermost'),
    '5.9460409952386536': lambda: P('/y8/depletion_width/crossing/3/margin_Omega_crit_over_band_top'),
    '51.62897242670489': lambda: P('/bins/BIN-DISC/rows/1/T_B_over_T_A'),
    '53.904369411419553': lambda: P('/bins/BIN-DISC/rows/2/T_B_over_T_A'),
    '54.500528268180376': lambda: P('/bins/BIN-DISC/rows/3/T_B_over_T_A'),
    '6.0238983090250982e-19': lambda: P('/reference/l_node_over_r_sat'),
    '641045.46244702291': lambda: P('/reference/r_sat_m'),
    '7.1262679104721422e-13': lambda: P('/gates/G-NC/worst_rel'),
    '7.42451e-14': lambda: P('/gates/G-DISC/rows/0/rel_sep'),
    '7.5252419456313015e-14': lambda: P('/bins/BIN-CUTOFF/CFG-A/spread'),
    '7.7050596147068955e-11': lambda: P('/y8/reach_through/per_configuration/8/CHIRP_MEASURE_over_rsat_c0'),
    '7.76344071105011e+20': lambda: P('/canonical_inputs/omega_C_rad_s'),
    '8.3316675133448825': lambda: P('/y8/reach_through/per_configuration/3/D_mirror_over_rsat_c0_min'),
    '866.88368375810832': lambda: P('/reference/omega_ringdown_rad_s'),
    '9.4838190349435383': lambda: P('/y8/reach_through/per_configuration/2/D_mirror_over_rsat_c0_min'),
    '9.6010822264111564': lambda: P('/y8/reach_through/per_configuration/0/D_mirror_over_rsat_c0_min'),
    '9.62997e-14': lambda: P('/gates/G-SUM/per_branch/RHO-B/max_rel_sep'),
    '9.6956874982756338': lambda: P('/gates/G-PEAK/per_branch/RHO-A/r_peak_over_GM_c2'),
    '9.99999e-7': lambda: P('/self_tests/FT-XTIE/measured'),
}

REGISTERED_LISTS = {
    "[0.2334174292085989, 0.58365895340449818]":
        lambda: [P("bins/BIN-DB/min_S_turn_over_S_last"),
                 P("bins/BIN-DB/max_S_turn_over_S_last")],
}

ALLOWED = {
    '+1': 'a FROZEN far-contact reading Gamma_L = +1 (CONTACT-CLAMPED) and the FT-DEP mutation offset -- a structural label, one significant digit',
    '0': "an exact zero: the G-CF separation and the Y-STEPSOFF control's identically-zero matched reflection",
    '0.0': 'the same exact zero written with a trailing zero by the driver',
    '0.0196078': 'the FT-DISC RESULTING gate separation, machine-tied below; also quoted in prose',
    '0.02': 'the FROZEN FT-DISC mutation size (prereg section 6.2), two significant digits',
    '0.1': 'the frozen FT-DECADE threshold',
    '0.10': 'the frozen BIN-CUTOFF threshold and the frozen BIN-RT-CONTACT boundary (prereg sections 7.2 / 7Y.2)',
    '0.1716': "(sqrt2-1)/(sqrt2+1), the DERIVED bound on the innermost Schur reflection coefficient -- an analytic value computed in the prereg's own numerical-conditioning row, deliberately not machine-tied",
    '0.29': 'the in-repo Abedi-Dykaar-Afshordi echo-spacing POINTER -- an EXTERNAL observational number, cited not computed, deliberately NOT tied to a shipped value',
    '0.5': 'theta = 1/2, the half-node sub-cell placement, and the exact FT-RT-I synthetic-ladder reflection',
    '0.90': 'the frozen BIN-RT-EDGE boundary',
    '0.95': 'a lower BOUND quoted to two figures on the three-way contact spread across the E1 variants',
    '1': 'the M = 1 solar-mass grid point, theta = 1, the exact |T|^2 of an identity two-port, the unit comparison |Gamma_in| = 1, and the v1 comparison scale for CHIRP-MEASURE',
    '1.0': 'the same exact unit values written with a trailing zero by the driver',
    '1.02': "the FT-DISC mutation factor 1 + 0.02, an analytic quantity in this document's own text",
    '1.0e-6': 'the FT-NC mutation size, a frozen 1e-6 scaling written with a trailing zero; two significant digits',
    '1.2e18': "the ORDER of the cell count from the wall to the barrier peak -- an analytic scoping estimate in this document's own text, deliberately not machine-tied",
    '1.41': "(1+rho)/(1-rho) at the innermost step, the DERIVED Euclidean amplification bound of the Mobius map -- an analytic value in this document's own diagnosis, deliberately not machine-tied",
    '1.90': 'the closest-corner BIN-W margin quoted to three figures in the headline; the machine-tied value is registered at its full precision',
    '1.96': 'the FT-DISC gate-separation margin over the frozen 1 per cent tolerance, quoted to three figures',
    '10': 'the M = 10 solar-mass grid point and the BIN-W-THIN/THICK boundary',
    '100': 'the M = 100 solar-mass grid point and the mass lever factor',
    '122': 'a FILE LINE NUMBER -- vol3/claim-quality.md:122',
    '124': 'a FILE LINE NUMBER -- vol3/claim-quality.md:124',
    '14': 'the approximate samples per derived ripple period, and the approximate digits of cancellation in the artanh decade difference -- both quoted to two figures',
    '1e-10': 'frozen G-NC and G-XTIE tolerances / FT-JA threshold',
    '1e-12': 'frozen G-SUM, G-UNIT, G-PREC and G-ABCD two-route tolerances',
    '1e-13': 'frozen FT-CF threshold, and the order of the decade-sweep deviation quoted in the conditioning disclosure',
    '1e-14': 'frozen G-ABCD structural tolerance',
    '1e-15': 'frozen G-DISP and G-BAND tolerances and the FT-CANON threshold',
    '1e-16': 'the float64 per-operation rounding scale quoted in the G-UNIT diagnosis -- an analytic scale, not a measurement',
    '1e-2': "frozen FT-DISP threshold and the shallowest G-DECADE rung's S",
    '1e-20': 'frozen G-JA tolerance',
    '1e-25': 'frozen G-CF tolerance',
    '1e-3': 'frozen FT-SUM and FT-UNIT thresholds and the frozen G-KWIN tolerance',
    '1e-30': 'frozen G-U tolerance',
    '1e-4': "frozen FT-PEAK threshold, a G-DECADE rung's S, and the RESIZED G-DECADE limb-(a) tolerance",
    '1e-5': "a G-DECADE rung's S",
    '1e-6': "frozen FT-U threshold, a G-DECADE rung's S, and the frozen G-MFREE tolerance",
    '1e-7': "frozen FT-NC and FT-XTIE thresholds and a G-DECADE rung's S",
    '1e6': 'the primary frozen N_split and the primary frozen Y8 window K',
    '2': 'the multipole index ell = 2, the RHO-B branch exponent p = 2, the 2x2 two-port dimension, and the per-cent scale of the Y-MID and R4 shifts',
    '208': "the TOTAL negative-control comparison count, 37 + 171, computed in this document's own text from two registered counts",
    '27': 'the round-trip accumulated phase in radians over the frozen window, quoted to two figures in the conditioning disclosure',
    '294': 'a FILE LINE NUMBER -- the STALE constants.py cite carried forward in FLAG-CITE-SHIFT',
    '3': 'the CFG-SYN synthetic branch exponent p = 3, the FT-RT-I synthetic impedance ratio, and the count of consecutive lanes in the FLAG-FREEZE-SIZING pattern',
    '3.56': 'the measured G-UNIT growth factor over the first decade of K, quoted to three figures from two registered values',
    '3.75e-5': "the DERIVED next-order decade residual (3/8) S_hi^2 -- an analytic value computed in this document's own text, deliberately not machine-tied because it is the derivation the residual limb tests against",
    '305': 'a FILE LINE NUMBER -- constants.py:305, where OMEGA_C actually is',
    '33.8': 'the measured G-UNIT growth factor over the second decade of K, quoted to three figures from two registered values',
    '37': 'the G-NC-V1A comparison count, two significant digits',
    '38.6': 'the lower end of the BIN-DISC separation in tau_ring, quoted to three figures',
    '4': 'a SECTION NUMBER, the count of adjudicated PART 1 bins, and the count of masses on the frozen grid',
    '40': 'the order of the artanh values being differenced in the decade sweep, quoted to one figure',
    '43.2': 'the upper end of the same, three figures',
    '5': 'a SECTION NUMBER',
    '50': 'the branch-ratio order of magnitude quoted to one figure, and the mpmath working precision dps = 50',
    '54': 'the FT-W depleted-cell count at the upper bracket end, two significant digits',
    '6': 'a SECTION NUMBER',
    '62': 'the reference remnant mass in solar masses',
    '65': 'the frozen band sampling count N_band',
    '7': 'x_sat = 7, the r_sat coefficient in r_sat = 7 GM/c^2',
    '8': 'a SECTION NUMBER',
    '99': 'the approximate per-cent power reflected at the stiffness-lifted bracket end, quoted to two figures',
}

# Machine-dependent values may NEVER be registered or allow-listed: an honest
# re-run on another machine must not fail this gate (the #801 R3 lesson).
NON_REGISTRABLE = {"_runtime_sec"}

# FIX (iv): the newline exclusion is load-bearing.  A bare [^`]+ swallows a
# fenced code block whole, consumes one of its three closing back-ticks, and
# inverts delimiter parity for the entire remainder of the file.
TOKEN_RE = re.compile(r"`([^`\n]+)`")
NUM_RE = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")
LIST_RE = re.compile(r"^\[\s*[-+0-9.eE]+(\s*,\s*[-+0-9.eE]+)*\s*\]$")
# FIX (vi): a run digest is a 16-hex-character token; NUM_RE never matches one.
DIGEST_RE = re.compile(r"^[0-9a-f]{16}$")


def is_number(tok: str) -> bool:
    return bool(NUM_RE.match(tok.strip()))


def is_digest(tok: str) -> bool:
    return bool(DIGEST_RE.match(tok.strip()))


def is_numlist(tok: str) -> bool:
    return bool(LIST_RE.match(tok.strip()))


def sig_digits(token: str) -> int:
    t = token.strip().lstrip("+-")
    if "e" in t.lower():
        t = t.lower().split("e")[0]
    t = t.replace(".", "").lstrip("0")
    return len(t.rstrip()) if t else 1


def matches(token: str, value) -> bool:
    """The token must be the correctly-rounded value at its own precision."""
    t = token.strip()
    if isinstance(value, str):
        if t == value.strip():
            return True
        try:
            value = float(value)
        except ValueError:
            return False
    try:
        tv = float(t)
    except ValueError:
        return False
    v = float(value)
    if "e" in t.lower():
        mant = t.lower().split("e")[0]
        digits = len(mant.replace("-", "").replace("+", "")
                     .replace(".", "").lstrip("0")) or 1
        return f"{v:.{max(digits - 1, 0)}e}" == f"{tv:.{max(digits - 1, 0)}e}"
    if "." in t:
        dec = len(t.split(".")[1])
        return f"{v:.{dec}f}" == f"{tv:.{dec}f}"
    return abs(v - tv) <= 0.5


def matches_list(token: str, value) -> bool:
    parts = [p.strip() for p in token.strip()[1:-1].split(",")]
    if not isinstance(value, list) or len(parts) != len(value):
        return False
    return all(matches(p, v) for p, v in zip(parts, value))


def run() -> int:
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED or bad in REGISTERED_LISTS:
            print(f"[echo-delay-v2-number-check] FAIL - {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered")
            return 1
    low = sorted(k for k in REGISTERED
                 if is_number(k) and sig_digits(k) < MIN_SIG_DIGITS)
    if low:
        print(f"[echo-delay-v2-number-check] FAIL - these REGISTERED keys carry "
              f"fewer than {MIN_SIG_DIGITS} significant digits and must be "
              f"allow-listed instead: {low}")
        return 1

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    seen_sites, tokens = set(), set()
    bad_rows, n_reg, n_allow = [], 0, 0
    exercised = set()
    # A back-ticked span may be a bare numeral, OR an expression that CONTAINS
    # numerals (e.g. "l_node = 3.86e-13").  A checker that only reads bare
    # spans silently skips every numeral written inside an expression, which is
    # exactly the coverage overstatement the completeness guard exists to
    # catch.  Spans are therefore SPLIT on separators and each piece is tested.
    candidates = []
    for m in TOKEN_RE.finditer(text):
        span = m.group(1).strip()
        line = text.count("\n", 0, m.start()) + 1
        if is_number(span) or is_numlist(span) or is_digest(span):
            candidates.append((span, line))
            continue
        for piece in re.split(r"[\s,;:()\[\]{}=<>×/|·]+", span):
            piece = piece.strip("`*_'\"±%^²³").rstrip(".")
            if piece and (is_number(piece) or is_digest(piece)):
                candidates.append((piece, line))
    for tok, line in candidates:
        numeric, listy, digesty = is_number(tok), is_numlist(tok), is_digest(tok)
        if not (numeric or listy or digesty):
            continue
        if (tok, line) in seen_sites:
            continue
        seen_sites.add((tok, line))
        tokens.add(tok)

        if listy:
            if tok in REGISTERED_LISTS:
                exercised.add(tok)
                try:
                    val = REGISTERED_LISTS[tok]()
                except Exception as exc:  # noqa: BLE001
                    bad_rows.append((tok, line, f"list lookup raised {exc!r}"))
                    continue
                if matches_list(tok, val):
                    n_reg += 1
                else:
                    bad_rows.append((tok, line,
                                     f"registered list source reads {val!r}"))
            elif tok in ALLOWED:
                n_allow += 1
            else:
                bad_rows.append((tok, line, "UNREGISTERED list"))
            continue

        if not digesty and sig_digits(tok) < MIN_SIG_DIGITS:
            if tok in ALLOWED:
                n_allow += 1
            else:
                bad_rows.append((tok, line,
                                 f"carries {sig_digits(tok)} significant "
                                 f"digit(s), below the floor of "
                                 f"{MIN_SIG_DIGITS}, so it MUST be "
                                 f"allow-listed with a reason"))
            continue

        if tok in REGISTERED:
            exercised.add(tok)
            try:
                val = REGISTERED[tok]()
            except Exception as exc:  # noqa: BLE001
                bad_rows.append((tok, line, f"source lookup raised {exc!r}"))
                continue
            if matches(tok, val):
                n_reg += 1
            else:
                bad_rows.append((tok, line, f"registered source reads {val!r}"))
        elif tok in ALLOWED:
            n_allow += 1
        else:
            bad_rows.append((tok, line, "UNREGISTERED - not in the shipped "
                                        "JSON and not allow-listed"))

    print(f"[echo-delay-v2-number-check] doc: {os.path.relpath(DOC, REPO)}")
    print("[echo-delay-v2-number-check] scope: BACKTICKED numerals in the RESULT "
          "DOC only; the prereg is NOT scanned (prereg section 10, frozen)")
    print(f"[echo-delay-v2-number-check] min significant digits for "
          f"registration: {MIN_SIG_DIGITS} | dedup: PER-SITE")
    print(f"[echo-delay-v2-number-check] SITES {len(seen_sites)} "
          f"(distinct tokens {len(tokens)}) | registered {n_reg} | "
          f"allow-listed {n_allow} | unregistered {len(bad_rows)}")
    if bad_rows:
        for tok, line, why in bad_rows:
            print(f"  FAIL  line {line}  `{tok}`  {why}")
        return 1

    unexercised = sorted((set(REGISTERED) | set(REGISTERED_LISTS)) - exercised)
    if unexercised:
        print(f"[echo-delay-v2-number-check] FAIL - {len(unexercised)} of "
              f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys were "
              f"NEVER EXERCISED by the document.  A registration the scan never "
              f"reaches checks nothing and overstates coverage: {unexercised}")
        return 1

    print(f"[echo-delay-v2-number-check] completeness: all "
          f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys "
          f"exercised")
    print("[echo-delay-v2-number-check] OK")
    return 0


def main() -> int:
    global _MUTATE
    if "--mutation-receipt" in sys.argv:
        # FIX (vii), THIS LANE'S ADDITION: a checker that cannot FAIL is not a
        # checker.  Perturb every shipped value by 1.5x and assert non-zero.
        _MUTATE = True
        rc = run()
        print(f"[echo-delay-v2-number-check] MUTATION RECEIPT: perturbed sources "
              f"by 1.5x, checker returned {rc}")
        if rc == 0:
            print("[echo-delay-v2-number-check] FAIL - the checker PASSED on "
                  "mutated sources; it is not fireable")
            return 1
        print("[echo-delay-v2-number-check] MUTATION RECEIPT OK - the checker is "
              "demonstrated FIREABLE")
        return 0
    return run()


if __name__ == "__main__":
    sys.exit(main())
