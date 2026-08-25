#!/usr/bin/env python3
"""Gating number check for the harmonic-balance-solver validation lane.

Re-verifies every verdict-bearing number in
research/drivers/data/harmonic_balance_validation/receipts.json with
independent arithmetic (math module — the second engine), and reconciles the
gate-2 targets against the measured Class-C source
(engine_gamma_meanstest_results.json) so the solver receipts cannot silently
drift from the measurement they claim to reproduce. Supports
--mutation-receipt (corrupts a verdict-bearing value in memory; the detectors
MUST fire). Auto-discovered by the make-verify umbrella
(verify-lane-number-checks). Pure arithmetic on committed JSON — never runs a
solve, never writes a file.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RECEIPTS = os.path.join(HERE, "data", "harmonic_balance_validation", "receipts.json")
MEASURED = os.path.join(HERE, "engine_gamma_meanstest_results.json")

MUTATE = "--mutation-receipt" in sys.argv


def fail(msg):
    print(f"HARMONIC-BALANCE NUMBER CHECK: FAIL — {msg}")
    sys.exit(1)


def close(a, b, rel=1e-9, absolute=1e-12):
    return abs(a - b) <= max(absolute, rel * max(abs(a), abs(b)))


def main():
    with open(RECEIPTS) as f:
        r = json.load(f)
    with open(MEASURED) as f:
        meas = json.load(f)

    if MUTATE:
        # corrupt a verdict-bearing solver value; the abs_dev detector MUST fire
        r["gate2"]["points"][0]["gamma_solver"] += 0.05

    checks = []
    g1, g2, g3 = r["gate1"], r["gate2"], r["gate3"]

    # ── gate 1 ───────────────────────────────────────────────────────────────
    anf = 1.0 / math.sqrt(3.0)  # independent arithmetic
    checks.append(("g1 stored analytic factor == 1/sqrt(3)",
                   close(g1["analytic_network_factor"], anf, rel=1e-12)))
    vel = abs(g1["c_smallest_theta"] - anf) / anf
    checks.append(("g1 velocity_rel_dev recomputes", close(vel, g1["velocity_rel_dev"])))
    checks.append(("g1 velocity_pass recomputes",
                   (vel < g1["velocity_tol"]) == g1["velocity_pass"]))
    dev = max(abs(p["theta_arccos"] - p["theta"]) for p in g1["points"])
    checks.append(("g1 max_arccos_dev recomputes", close(dev, g1["max_arccos_dev"])))
    checks.append(("g1 arccos_pass recomputes", (dev < g1["arccos_tol"]) == g1["arccos_pass"]))
    checks.append(("g1 k_edge reconciles vs measured cold gate",
                   close(g1["k_edge_measured"], meas["sanity"]["CS2_k_edge"], rel=1e-12)))
    in_band = [p for p in g1["points"] if p["k_fit"] <= g1["k_edge_measured"]]
    checks.append(("g1 n_points_in_band recomputes", len(in_band) == g1["n_points_in_band"]))
    if in_band:
        bmax = max(abs(p["c"] - anf) / anf for p in in_band)
        checks.append(("g1 band_edge_max_rel_dev recomputes",
                       close(bmax, g1["band_edge_max_rel_dev"])))
        checks.append(("g1 band_edge_pass recomputes",
                       (bmax < g1["band_edge_tol"]) == g1["band_edge_pass"]))
    checks.append(("g1 pass composes",
                   g1["pass"] == (g1["velocity_pass"] and g1["arccos_pass"] and g1["band_edge_pass"])))

    # ── gate 2 ───────────────────────────────────────────────────────────────
    meas_gj = {row["A"]: row for row in meas["table"]["GJ"]}
    checks.append(("g2 geometry L reconciles", g2["L"] == meas["params"]["L"]))
    checks.append(("g2 geometry x_I reconciles", close(g2["x_I"], meas["params"]["x_I"], rel=1e-12)))
    checks.append(("g2 geometry x_B reconciles", close(g2["x_B"], meas["params"]["x_B"], rel=1e-12)))
    n_valid_measured = sum(1 for row in meas["table"]["GJ"] if row["valid"])
    checks.append(("g2 covers every measured-VALID G-J point", g2["n_points"] == n_valid_measured))
    all_pt_ok = True
    worst = 0.0
    for p in g2["points"]:
        row = meas_gj.get(p["A"])
        if row is None or not row["valid"]:
            all_pt_ok = False
            break
        if not close(p["gamma_measured"], row["gamma"], rel=1e-12):
            all_pt_ok = False
            break
        d = abs(p["gamma_solver"] - p["gamma_measured"])
        if not close(d, p["abs_dev"]):
            all_pt_ok = False
            break
        tol_pt = max(g2["tol_abs_floor"], g2["tol_rel"] * abs(p["gamma_measured"]))
        if not close(tol_pt, p["tol_point"]):
            all_pt_ok = False
            break
        if (d <= tol_pt) != p["pass"]:
            all_pt_ok = False
            break
        worst = max(worst, d)
    checks.append(("g2 every point reconciles (measured value, dev, tol, verdict)", all_pt_ok))
    checks.append(("g2 max_abs_dev recomputes", close(worst, g2["max_abs_dev"])))
    checks.append(("g2 pass composes", g2["pass"] == all(p["pass"] for p in g2["points"])))
    checks.append(("g2 cold-null receipt recorded and sane",
                   0.0 <= g2["cold_null_abs_gamma"] < g2["tol_abs_floor"]))
    # the raw single-load artifact receipt behind the note's ~10% claim: real
    # (well above the de-embedded null) and sane (well below total reflection)
    checks.append(("g2 single-load artifact receipt recorded and O(10%)",
                   all(0.01 < g < 0.5 for g in g2["cold_single_load_gamma_raw"])
                   and len(g2["cold_single_load_gamma_raw"]) == len(g2["load_planes"])))

    # ── gate 3 ───────────────────────────────────────────────────────────────
    thr = g3["thresholds"]

    def idle(obs):
        return (obs["max_source_amp"] <= thr["source_tol"]
                and obs["max_exchange_amp"] <= thr["exchange_tol"]
                and obs["max_r_auto"] <= thr["r_auto_tol"])

    checks.append(("g3 ring idle recomputes", idle(g3["ring"]) == g3["ring"]["idle"]))
    checks.append(("g3 tank idle recomputes", idle(g3["driven_tank"]) == g3["driven_tank"]["idle"]))
    checks.append(("g3 pass composes",
                   g3["pass"] == (g3["ring"]["idle"] and not g3["driven_tank"]["idle"])))
    checks.append(("g3 ring theta == 2 pi m / N",
                   close(g3["ring"]["theta"], 2.0 * math.pi * g3["ring"]["m"] / g3["ring"]["N"], rel=1e-12)))

    # ── composition ──────────────────────────────────────────────────────────
    checks.append(("all_pass composes", r["all_pass"] == (g1["pass"] and g2["pass"] and g3["pass"])))
    checks.append(("receipts of record are PASSING (the landed instrument claim)",
                   r["all_pass"] is True))

    bad = [name for name, ok in checks if not ok]
    if MUTATE:
        if bad:
            print(f"HARMONIC-BALANCE NUMBER CHECK: mutation receipt FIRES "
                  f"({len(bad)} detector(s): {bad[:2]}) — checker is live")
            sys.exit(0)
        fail("mutation receipt did NOT fire — checker is dead")
    if bad:
        fail(f"{len(bad)} check(s) failed: {bad}")
    print(f"HARMONIC-BALANCE NUMBER CHECK: PASS ({len(checks)} checks green)")


if __name__ == "__main__":
    main()
