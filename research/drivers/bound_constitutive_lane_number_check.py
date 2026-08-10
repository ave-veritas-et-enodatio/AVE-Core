#!/usr/bin/env python3
"""Gating number check for the bound-constitutive lane (R41).

Re-verifies every verdict-bearing numeral of the lane against the driver JSON,
with independent arithmetic (math module — the second engine). Supports
--mutation-receipt: perturbs a loaded value in memory and MUST detect it,
proving the checker is live. Auto-discovered by the make-verify umbrella.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(HERE, "bound_constitutive_lane_results.json")

MUTATE = "--mutation-receipt" in sys.argv


def fail(msg):
    print(f"BOUND-CONSTITUTIVE NUMBER CHECK: FAIL — {msg}")
    sys.exit(1)


def main():
    with open(JSON) as f:
        r = json.load(f)

    if MUTATE:
        # deliberately corrupt one verdict-bearing numeral; the checks below MUST catch it
        r["R3"]["longitudinal_K2G_control"]["front_speed"] = 1.0

    checks = []

    # frozen banked ratios, independent arithmetic
    checks.append(("nu(K=2G) == 2/7", r["R6"]["nu_at_K2G"]["exact"] == "2/7"
                   and abs(r["R6"]["nu_at_K2G"]["float"] - 2 / 7) < 1e-15))
    checks.append(("1-2nu == 3/7", r["R6"]["trace_factor_1_minus_2nu"]["exact"] == "3/7"))
    checks.append(("cP2/cT2(K=0) == 4/3", r["R6"]["cP2_over_cT2_at_K0"]["exact"] == "4/3"))
    checks.append(("cP2/cT2(K=2G) == 10/3", r["R6"]["cP2_over_cT2_at_K2G"]["exact"] == "10/3"))
    checks.append(("sqrt(10/3) frozen digits", abs(r["R3"]["sqrt_10_3_frozen"]
                                                   - math.sqrt(10 / 3)) < 1e-15))

    # symmetry algebra
    checks.append(("R0a residual symmetry exact", r["R0"]["R0a_residual_symmetry_exact_zero"] is True))
    checks.append(("R0b remainder form matches", r["R0"]["R0b_timedep_remainder_matches"] is True))
    checks.append(("R0c Noether identity", r["R0"]["R0c_noether_density_identity"] is True))
    checks.append(("R0c div-curl-curl == 0", r["R0"]["R0c_div_curl_curl_zero_symbolic"] is True))

    # flat direction + conservation
    checks.append(("R1 linear drift <= 1e-10", r["R1"]["numeric_linear_drift_residual"] <= 1e-10))
    checks.append(("R2 vacuum ddt div pi <= 1e-12", r["R2"]["vacuum_max_abs_ddt_div_pi"] <= 1e-12))
    checks.append(("R2 sourced continuity <= 1e-12", r["R2"]["sourced_max_abs_continuity_defect"] <= 1e-12))

    # fronts: receipted transverse ~ c; receipted longitudinal STATIC; control detects phantom
    t = r["R3"]["transverse_receipted"]["front_speed"]
    checks.append(("transverse front within 3% of c", abs(t - 1.0) <= 0.03))
    checks.append(("longitudinal receipted static <= 1e-12",
                   r["R3"]["longitudinal_receipted"]["max_displacement_change"] <= 1e-12))
    ctrl = r["R3"]["longitudinal_K2G_control"]["front_speed"]
    checks.append(("control front >= 1.5c (liveness)", ctrl >= 1.5))
    checks.append(("control front within 3% of sqrt(10/3)",
                   abs(ctrl - math.sqrt(10 / 3)) / math.sqrt(10 / 3) <= 0.03))

    # energy + response
    checks.append(("R4 Coulomb integral float", abs(r["R4"]["float_value_Bin2out50"]
                                                    - 4 * math.pi * (0.5 - 0.02)) < 1e-12))
    checks.append(("R5 receipted transports nothing",
                   r["R5"]["flux_proxy_time_avg_udot2_at_rmid_receipted"] == 0.0))
    checks.append(("R5 control radiates", r["R5"]["flux_proxy_time_avg_udot2_at_rmid_K2G"] > 1e-10))
    checks.append(("all driver gates green", r["all_pass"] is True or MUTATE))

    bad = [name for name, ok in checks if not ok]
    if MUTATE:
        if bad:
            print(f"BOUND-CONSTITUTIVE NUMBER CHECK: mutation receipt OK — corrupted value "
                  f"detected by {len(bad)} check(s): {bad}")
            sys.exit(0)
        fail("mutation receipt DID NOT FIRE — checker is dead")
    if bad:
        fail(f"{len(bad)} check(s) failed: {bad}")
    print(f"BOUND-CONSTITUTIVE NUMBER CHECK: PASS — {len(checks)} checks green")
    sys.exit(0)


if __name__ == "__main__":
    main()
