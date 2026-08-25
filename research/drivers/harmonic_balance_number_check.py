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

WHAT THIS CHECKER DOES AND DOES NOT DO (bounded honestly, 2026-08-25):
  * It reconciles receipts AGAINST EVIDENCE — the measured Class-C table, the
    frozen driver constants, and internal arithmetic. It never runs a solve, so
    it cannot detect a receipts file whose gate-2 OUTPUTS were fabricated
    self-consistently; the defence against that is re-running the driver (the
    run of record reproduces bit-for-bit).
  * TOLERANCE RECONCILIATION (added 2026-08-25, adversarial round 2 — the
    reconcile-don't-declare rule at the tolerance layer). Every gate tolerance
    in the receipts USED to be a self-declared field no detector checked: the
    file could be edited to `gate2.tol_abs_floor = 1.0` — a gate that cannot
    mathematically fail — with `parameters.g2_tol_abs_floor` still reading 0.01
    in the same file, and every check stayed green. Each tolerance, threshold
    and declared geometry constant is now reconciled against its FROZEN SOURCE:
    the driver's own `P = {...}` literal, read out of the driver SOURCE with
    ast.literal_eval (never imported, never executed). Contradiction = FAIL.
  * The mutation receipt now covers ONE VERDICT-BEARING VALUE PER GATE FAMILY
    plus the tolerance layer, and the total check count is PINNED
    (EXPECTED_CHECKS): deleting a detector family fails loud instead of
    silently shrinking the gate.
"""
import ast
import copy
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RECEIPTS = os.path.join(HERE, "data", "harmonic_balance_validation", "receipts.json")
MEASURED = os.path.join(HERE, "engine_gamma_meanstest_results.json")
DRIVER = os.path.join(HERE, "harmonic_balance_validation.py")

MUTATE = "--mutation-receipt" in sys.argv

# Pinned so a dropped detector family cannot silently shrink this gate
# (adversarial round 2: the checker previously passed with 12 of its 26
# detectors deleted, and still certified itself "live").
EXPECTED_CHECKS = 46


def fail(msg):
    print(f"HARMONIC-BALANCE NUMBER CHECK: FAIL — {msg}")
    sys.exit(1)


def close(a, b, rel=1e-9, absolute=1e-12):
    return abs(a - b) <= max(absolute, rel * max(abs(a), abs(b)))


def same(a, b):
    """Structural equality for a declared-constant reconciliation: floats by
    `close`, sequences elementwise, everything else by ==."""
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return close(float(a), float(b), rel=1e-12)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def frozen_driver_params():
    """The driver's `P = {...}` block, read from the driver SOURCE.

    This is the FROZEN SOURCE the receipts' tolerances are reconciled against.
    Parsed with ast.literal_eval — the driver is never imported and never
    executed by this checker (importing it would run nothing here, but it would
    also make the 'never runs a solve' promise depend on the driver's own
    import-time behaviour rather than on this file)."""
    with open(DRIVER) as f:
        tree = ast.parse(f.read(), filename=DRIVER)
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "P"
        ):
            try:
                return ast.literal_eval(node.value)
            except (ValueError, SyntaxError) as exc:
                # A non-literal P (a computed constant, an import) would make the
                # frozen source unreadable. Fail loud rather than fall through to
                # `None`, which the caller would report as a missing block.
                fail(f"the driver's `P` block is no longer a literal ({exc}) — the "
                     "tolerance reconciliation cannot read its frozen source. Keep P a "
                     "literal dict, or point the reconciler at whatever replaced it.")
    return None


def build_checks(r, meas, P):
    """Every detector, as (name, ok) pairs. Name prefixes are the FAMILIES the
    mutation receipt requires to fire: 'g1 ', 'g2 ', 'g3 ', 'tol '."""
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
        ok_bmax = close(bmax, g1["band_edge_max_rel_dev"])
        ok_bpass = (bmax < g1["band_edge_tol"]) == g1["band_edge_pass"]
    else:
        # no in-band point: the driver records None / False by construction.
        # Kept as CHECKS (not skipped) so the detector count is invariant.
        ok_bmax = g1["band_edge_max_rel_dev"] is None
        ok_bpass = g1["band_edge_pass"] is False
    checks.append(("g1 band_edge_max_rel_dev recomputes", ok_bmax))
    checks.append(("g1 band_edge_pass recomputes", ok_bpass))
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
        # the MATCHED-FILTER column `gamma` is the adjudicating estimator (the
        # frozen prereg's); `gammaE` is the unsigned energy cross-check and is
        # deliberately NOT what this gate reproduces — declared in the driver.
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
    # the raw single-load artifact receipt behind the note's "~0.10 per load
    # plane" claim — BINDING, not a wide bracket (re-audit hardening): the
    # note's band, plus the load-position-independence the note asserts
    craw = g2["cold_single_load_gamma_raw"]
    checks.append(("g2 single-load artifact receipt in the note's ~0.10 band",
                   all(0.05 < g < 0.2 for g in craw)
                   and len(craw) == len(g2["load_planes"]) and len(craw) > 0))
    checks.append(("g2 artifact is load-position-independent (< 1e-5 spread)",
                   len(craw) > 0 and (max(craw) - min(craw)) < 1e-5))

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
    # The ring is solved with term=None, where source_idle_report returns
    # LITERAL zeros for source/exchange (structurally guaranteed, not measured
    # — module docstring). So the ring's idle verdict rests on r_auto alone;
    # this detector says so out loud rather than letting 0.0 <= 1e-12 read as
    # two independent measurements.
    checks.append(("g3 ring idle is r_auto-ONLY (source/exchange are structural zeros)",
                   g3["ring"]["max_source_amp"] == 0.0
                   and g3["ring"]["max_exchange_amp"] == 0.0
                   and g3["ring"]["max_r_auto"] > 0.0))
    # ...whereas the tank side IS three-observable: its termination is real, so
    # its source amplitude is a measured non-zero. That asymmetry is the
    # gate's actual content and is now pinned.
    checks.append(("g3 tank not-idle is measured (source amplitude strictly positive)",
                   g3["driven_tank"]["max_source_amp"] > 0.0))

    # ── tolerance reconciliation vs the FROZEN driver constants ─────────────
    # reconcile-don't-declare at the tolerance layer: a tolerance in the
    # receipts that contradicts the driver's own frozen P literal is a FAIL,
    # not a self-declaration to be consumed.
    checks.append(("tol receipts.parameters reconciles vs driver P (every key, value-for-value)",
                   P is not None
                   and set(r["parameters"]) == set(P)
                   and all(same(r["parameters"][k], P[k]) for k in P)))
    for name, val, key in (
        ("gate1.L", g1["L"], "g1_L"),
        ("gate1.velocity_tol", g1["velocity_tol"], "g1_velocity_tol"),
        ("gate1.arccos_tol", g1["arccos_tol"], "g1_arccos_tol"),
        ("gate1.band_edge_tol", g1["band_edge_tol"], "g1_band_edge_tol"),
        ("gate2.theta", g2["theta"], "g2_theta"),
        ("gate2.load_planes", g2["load_planes"], "g2_load_planes"),
        ("gate2.tol_abs_floor", g2["tol_abs_floor"], "g2_tol_abs_floor"),
        ("gate2.tol_rel", g2["tol_rel"], "g2_tol_rel"),
        ("gate3.thresholds.source_tol", thr["source_tol"], "g3_source_tol"),
        ("gate3.thresholds.exchange_tol", thr["exchange_tol"], "g3_exchange_tol"),
        ("gate3.thresholds.r_auto_tol", thr["r_auto_tol"], "g3_r_auto_tol"),
        ("gate3.ring.N", g3["ring"]["N"], "g3_ring_N"),
        ("gate3.ring.m", g3["ring"]["m"], "g3_ring_m"),
        ("gate3.driven_tank.L", g3["driven_tank"]["L"], "g3_tank_L"),
        ("gate3.driven_tank.theta", g3["driven_tank"]["theta"], "g3_tank_theta"),
    ):
        checks.append((f"tol {name} == driver P[{key!r}]",
                       P is not None and key in P and same(val, P[key])))
    checks.append(("tol gate1 swept thetas == driver P['g1_theta_sweep']",
                   P is not None
                   and same([p["theta"] for p in g1["points"]], P["g1_theta_sweep"])))
    checks.append(("tol receipts name the driver this checker parsed",
                   r.get("driver") == "research/drivers/harmonic_balance_validation.py"))

    # ── composition ──────────────────────────────────────────────────────────
    checks.append(("all_pass composes", r["all_pass"] == (g1["pass"] and g2["pass"] and g3["pass"])))
    checks.append(("receipts of record are PASSING (the landed instrument claim)",
                   r["all_pass"] is True))
    return checks


def _mut_g1(r):
    r["gate1"]["c_smallest_theta"] *= 1.01


def _mut_g2(r):
    r["gate2"]["points"][0]["gamma_solver"] += 0.05


def _mut_g3(r):
    r["gate3"]["ring"]["max_r_auto"] = 1.0


def _mut_tol(r):
    """The exact on-disk tamper the round-2 review demonstrated: widen the gate-2
    floor to a value at which |dGamma| <= tol is unfalsifiable, and recompute
    every tol_point consistently so no arithmetic detector notices. Only the
    tolerance reconciliation can catch this one."""
    g2 = r["gate2"]
    g2["tol_abs_floor"] = 1.0
    for p in g2["points"]:
        p["tol_point"] = max(1.0, g2["tol_rel"] * abs(p["gamma_measured"]))
        p["pass"] = abs(p["gamma_solver"] - p["gamma_measured"]) <= p["tol_point"]


MUTATIONS = (
    ("g1 ", _mut_g1),
    ("g2 ", _mut_g2),
    ("g3 ", _mut_g3),
    ("tol ", _mut_tol),
)


def main():
    with open(RECEIPTS) as f:
        r = json.load(f)
    with open(MEASURED) as f:
        meas = json.load(f)
    P = frozen_driver_params()
    if P is None:
        fail(f"could not read the frozen `P` parameter literal out of {DRIVER} — "
             "the tolerance reconciliation has no frozen source to check against, "
             "and a reconciler with no source is a checklist. Refusing to pass.")

    if MUTATE:
        # One verdict-bearing mutation PER FAMILY: each must fire at least one
        # detector IN ITS OWN family. A single-path receipt would certify the
        # checker "live" while a whole family sat dead.
        base_bad = [n for n, ok in build_checks(r, meas, P) if not ok]
        if base_bad:
            fail(f"mutation receipt cannot run: the UNMUTATED receipts already fail {base_bad}")
        fired = []
        for family, mutate in MUTATIONS:
            rm = copy.deepcopy(r)
            mutate(rm)
            bad = [n for n, ok in build_checks(rm, meas, P) if not ok]
            in_family = [n for n in bad if n.startswith(family)]
            if not in_family:
                fail(f"mutation receipt DEAD in family {family.strip()!r}: "
                     f"a verdict-bearing value was corrupted and no {family.strip()} "
                     f"detector fired (other detectors that fired: {bad})")
            fired.append(f"{family.strip()}:{len(in_family)}")
        print("HARMONIC-BALANCE NUMBER CHECK: mutation receipt FIRES in every family "
              f"({', '.join(fired)}) — checker is live across all {len(MUTATIONS)} families")
        sys.exit(0)

    checks = build_checks(r, meas, P)
    if len(checks) != EXPECTED_CHECKS:
        fail(f"detector count is {len(checks)}, pinned at {EXPECTED_CHECKS} — a detector "
             "family was added or dropped. Update EXPECTED_CHECKS deliberately; a gate "
             "that can silently shrink is not a gate.")
    bad = [name for name, ok in checks if not ok]
    if bad:
        fail(f"{len(bad)} check(s) failed: {bad}")
    print(f"HARMONIC-BALANCE NUMBER CHECK: PASS ({len(checks)} checks green)")


if __name__ == "__main__":
    main()
