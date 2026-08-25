#!/usr/bin/env python
"""Per-run V3 sentinel check for the graded-region Gamma(A) means-test.

WHY THIS FILE EXISTS
--------------------
The result doc asserted (sec 3 / sec 7 / deviation D3) that "no projected
contaminant arrival precedes any window close in any of the 48 runs (verified
per-run from the saved sentinel series)".  The driver did NOT implement that:
`derive_windows` consumes only the COLD run's sentinel series, and the 48 graded
runs' sentinel series were saved to raw_*.json and never re-checked.  That is a
declared-not-computed gate (reconcile-don't-declare).  This script IS the check:
it recomputes the projection for every graded run from the shipped raw series
and reconciles it against the window actually used.

METHOD (deviation D3 as declared in the result doc, applied per run)
-------------------------------------------------------------------
  * sentinel plane x_sent = 19.5 cells, direction-resolved port sums;
  * contaminant front = first step at which max|V| on the sentinel ports of a
    direction exceeds `sentinel_thresh` (1% of the unit launch envelope);
  * projection to the probe plane x_p along that direction:
        backward (-x): (x_sent - x_p) cells
        forward  (+x): (box - x_sent + x_p) cells
    at the measured cold small-k speed c_meas (Cartesian length / step),
    cells -> Cartesian via a_cell (engine value, not hard-coded);
  * earliest projected probe arrival over the two directions binds the run.

TWO GATES ARE REPORTED, both per run:
  STRICT  : arrival > close                      (the sentence in the doc)
  GUARDED : arrival - guard_sigmas*sigma_t >= close   (the rule the driver used
            to DERIVE the close; guard = 2 sigma_t)

A cross-check reconciles this script's own earliest-arrival value against the
driver's `windows[*]['t_wrap_probe']` (which the driver derived from the COLD
run): the two must agree to 1e-9, which is what makes this an independent
re-derivation of the SAME quantity rather than a different one.

Exit code 0 iff every graded run passes the STRICT gate at the frozen window
close; 1 otherwise.  Deterministic: pure arithmetic on shipped JSON.

Usage:  python check_sentinels.py [--data DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent

# --- engine resolution (same policy as the driver; never hard-code a_cell) ---
ENGINE_FALLBACK = Path("/Users/grantlindblom/AVE-staging/AVE-Core/src")


def resolve_engine_src() -> Path:
    """The enclosing checkout's src/, else the run-workspace fallback."""
    for parent in (HERE, *HERE.parents):
        cand = parent / "src" / "ave" / "core" / "chiral_lattice.py"
        if cand.is_file():
            return parent / "src"
    return ENGINE_FALLBACK


def resolve_data_dirs(explicit: str | None):
    """(results.json path, raw dir) for the in-tree and run-workspace layouts."""
    if explicit:
        d = Path(explicit).resolve()
        res = d / "results.json"
        if not res.is_file():
            sib = d.parent / "engine_gamma_meanstest_results.json"
            res = sib if sib.is_file() else res
        return res, d
    if HERE.name == "drivers" and HERE.parent.name == "research":
        return (HERE / "engine_gamma_meanstest_results.json",
                HERE / "data" / "engine_gamma_meanstest")
    return HERE / "data" / "results.json", HERE / "data"


def first_crossing(series, thresh):
    idx = np.where(np.asarray(series) > thresh)[0]
    return int(idx[0]) if len(idx) else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None, help="directory holding raw_*.json")
    args = ap.parse_args()

    res_path, raw_dir = resolve_data_dirs(args.data)
    res = json.loads(res_path.read_text())
    P, S, W = res["params"], res["sanity"], res["windows"]
    configs = ("GJ", "GB", "GT")
    raw = {c: json.loads((raw_dir / f"raw_{c}.json").read_text()) for c in configs}

    sys.path.insert(0, str(resolve_engine_src()))
    from ave.core import chiral_lattice as cl  # noqa: E402

    a_cell = cl.build_srs_net(L=2, enantiomorph=P["enantiomorph"]).a_cell
    c = S["c_meas"]
    sigma_t = S["sigma_t"]
    guard = P["guard_sigmas"] * sigma_t
    thresh = P["sentinel_thresh"]
    x_p, x_s, box = P["x_p"], P["sentinel_x"], float(P["L"])
    dists = {"sent_bwd": x_s - x_p, "sent_fwd": box - x_s + x_p}

    print("=" * 78)
    print("PER-RUN V3 SENTINEL CHECK — 48 graded runs, shipped sentinel series")
    print("=" * 78)
    print(f"  data           : {raw_dir}")
    print(f"  results        : {res_path}")
    print(f"  engine src     : {resolve_engine_src()}")
    print(f"  a_cell         : {a_cell:.12f}  (engine value, build_srs_net)")
    print(f"  c_meas         : {c:.12f} Cartesian length / step (CS-2 small-k)")
    print(f"  sigma_t        : {sigma_t:.6f} steps; guard = {P['guard_sigmas']}"
          f"*sigma_t = {guard:.6f}")
    print(f"  threshold      : {thresh} of the unit launch envelope")
    print(f"  projection     : bwd {dists['sent_bwd']:.1f} cells, "
          f"fwd {dists['sent_fwd']:.1f} cells (x_sent={x_s}, x_p={x_p}, box={box})")
    print()
    hdr = (f"  {'cfg':<4}{'A':<8}{'t_bwd':>6}{'t_fwd':>6}{'arr_bwd':>9}"
           f"{'arr_fwd':>9}{'earliest':>10}{'close':>7}{'margin':>8}"
           f"{'STRICT':>8}{'GUARDED':>9}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    earliest_all, strict_fail, guard_fail, n = None, [], [], 0
    for cfg in configs:
        close = W[cfg]["w_refl"][1]
        for A in P["A_grid"]:
            r = raw[cfg][str(A)]
            tt, arr = {}, {}
            for key in ("sent_bwd", "sent_fwd"):
                t0 = first_crossing(r[key], thresh)
                tt[key] = t0
                arr[key] = (None if t0 is None
                            else t0 + dists[key] * a_cell / c)
            cand = [v for v in arr.values() if v is not None]
            e = min(cand) if cand else float("inf")
            ok_strict = e > close
            ok_guard = (e - guard) >= close
            if earliest_all is None or e < earliest_all:
                earliest_all = e
            if not ok_strict:
                strict_fail.append((cfg, A, e, close))
            if not ok_guard:
                guard_fail.append((cfg, A, e, close))
            n += 1
            print(f"  {cfg:<4}{A:<8}{str(tt['sent_bwd']):>6}{str(tt['sent_fwd']):>6}"
                  f"{arr['sent_bwd']:9.3f}{arr['sent_fwd']:9.3f}{e:10.3f}"
                  f"{close:7d}{e - close:8.3f}"
                  f"{('PASS' if ok_strict else 'FAIL'):>8}"
                  f"{('PASS' if ok_guard else 'FAIL'):>9}")

    print()
    print(f"  runs checked                     : {n}")
    print(f"  earliest projected arrival (all) : {earliest_all:.5f} steps")
    print(f"  frozen window close              : {W['GJ']['w_refl'][1]}")
    print(f"  guarded bound (earliest - guard) : {earliest_all - guard:.5f}")
    print(f"  STRICT  failures                 : {len(strict_fail)}")
    print(f"  GUARDED failures                 : {len(guard_fail)}")

    # Reconciliation: this script's independent earliest vs the driver's own
    # cold-run projection recorded in results.json.
    drv = W["GJ"]["t_wrap_probe"]
    delta = abs(earliest_all - drv)
    print(f"  driver t_wrap_probe (cold run)   : {drv:.11f}")
    print(f"  |this check - driver|            : {delta:.3e} "
          f"({'RECONCILED' if delta < 1e-9 else 'MISMATCH'})")

    # Amendment cross-check: the extended close used for the taper convergence
    # re-extraction is NOT guard-protected; state that explicitly rather than
    # letting the STRICT pass imply it is.
    amd_close = 85
    print()
    print(f"  [amendment] extended close {amd_close}: STRICT "
          f"{'PASS' if earliest_all > amd_close else 'FAIL'} "
          f"(margin {earliest_all - amd_close:+.3f} steps); GUARDED "
          f"{'PASS' if earliest_all - guard >= amd_close else 'FAIL'} "
          f"(needs {guard:.2f} steps of guard, has "
          f"{earliest_all - amd_close:.2f}) — the extended window is a "
          f"convergence probe only, cross-validated against the L=32 rerun "
          f"whose window is not wrap-bound; it is NOT the frozen extraction.")

    bad = len(strict_fail) > 0 or delta >= 1e-9
    print()
    print("  VERDICT: " + ("PASS — no projected contaminant arrival precedes "
                           "any window close in any of the 48 runs"
                           if not bad else f"FAIL — {strict_fail[:3]}"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
