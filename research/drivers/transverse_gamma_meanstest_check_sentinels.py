#!/usr/bin/env python
"""Per-run V3 sentinel check for the transverse reciprocal-loading Gamma(A)
means-test (static-existence Stage 1).

Frozen in the prereg from the start (SS4.4/SS8 V3 — the Class-C AMD-3
reconcile-don't-declare lesson adopted into the freeze, not added post-verify):
the driver derives the window close from the COLD run's sentinel only; THIS
script is the per-run receipt. It consumes the shipped sentinel series of all
32 graded runs, recomputes every projected contaminant arrival, applies the
STRICT and GUARDED gates per run, and reconciles its own earliest arrival
against the driver's cold-run projection.

VOID consequences (prereg SS8 V3): STRICT failure on ANY run => VOID; a
reconcile mismatch > 1e-9 => VOID (the reconcile is what gives STRICT
independent fireability — the close is CONSTRUCTED from the cold projection).
GUARDED is the construction rule; its per-run margin is reported.

Exit code 0 iff every run passes STRICT at its config's frozen close AND the
reconcile holds; 1 otherwise. Deterministic: pure arithmetic on shipped JSON.

Usage:  python transverse_gamma_meanstest_check_sentinels.py [--data DIR]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def first_crossing(series, thresh):
    idx = np.where(np.asarray(series) > thresh)[0]
    return int(idx[0]) if len(idx) else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None, help="directory holding raw_*.json")
    args = ap.parse_args()

    raw_dir = Path(args.data).resolve() if args.data else \
        HERE / "data" / "transverse_gamma_meanstest"
    res_path = HERE / "transverse_gamma_meanstest_results.json"
    res = json.loads(res_path.read_text())
    P, S, W = res["params"], res["sanity"], res["windows"]
    configs = ("TMAG", "TELEC")
    raw = {c: json.loads((raw_dir / f"raw_{c}.json").read_text()) for c in configs}

    sys.path.insert(0, str(REPO / "src"))
    from ave.core import chiral_lattice as cl  # noqa: E402

    a_cell = cl.build_srs_net(L=2, enantiomorph=P["enantiomorph"]).a_cell
    c = S["c_meas"]
    sigma_t = S["sigma_t"]
    guard = P["guard_sigmas"] * sigma_t
    thresh = P["sentinel_thresh"]
    x_p, x_s, box = P["x_p"], P["sentinel_x"], float(P["L"])
    dists = {"sent_bwd": x_s - x_p, "sent_fwd": box - x_s + x_p}

    print("=" * 78)
    print("PER-RUN V3 SENTINEL CHECK — 32 graded runs, shipped sentinel series")
    print("=" * 78)
    print(f"  data      : {raw_dir}")
    print(f"  results   : {res_path}")
    print(f"  a_cell    : {a_cell:.12f} (engine value, build_srs_net)")
    print(f"  c_meas    : {c:.12f}; sigma_t = {sigma_t:.6f}; guard = {guard:.6f}")
    print(f"  threshold : {thresh}; projection bwd {dists['sent_bwd']:.1f} / "
          f"fwd {dists['sent_fwd']:.1f} cells")
    print()
    hdr = (f"  {'cfg':<6}{'A':<8}{'t_bwd':>6}{'t_fwd':>6}{'arr_bwd':>9}"
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
                arr[key] = None if t0 is None else t0 + dists[key] * a_cell / c
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
            ab = "  none" if arr["sent_bwd"] is None else f"{arr['sent_bwd']:9.3f}"
            af = "  none" if arr["sent_fwd"] is None else f"{arr['sent_fwd']:9.3f}"
            print(f"  {cfg:<6}{A:<8}{str(tt['sent_bwd']):>6}{str(tt['sent_fwd']):>6}"
                  f"{ab:>9}{af:>9}{e:10.3f}{close:7d}{e - close:8.3f}"
                  f"{('PASS' if ok_strict else 'FAIL'):>8}"
                  f"{('PASS' if ok_guard else 'FAIL'):>9}")

    print()
    print(f"  runs checked                     : {n}")
    print(f"  earliest projected arrival (all) : {earliest_all:.5f} steps")
    print(f"  guarded bound (earliest - guard) : {earliest_all - guard:.5f}")
    print(f"  STRICT failures                  : {len(strict_fail)}")
    print(f"  GUARDED failures                 : {len(guard_fail)}")

    # Reconcile vs the driver's cold-run projections (per config; identical cold
    # run, so both configs carry the same t_wrap_probe)
    recon_bad = False
    for cfg in configs:
        drv = W[cfg]["t_wrap_probe"]
        delta = abs(earliest_all - drv)
        ok = delta < 1e-9
        recon_bad = recon_bad or not ok
        print(f"  driver t_wrap_probe [{cfg}]        : {drv:.11f}  "
              f"|check - driver| = {delta:.3e} "
              f"({'RECONCILED' if ok else 'MISMATCH -> VOID'})")

    bad = len(strict_fail) > 0 or recon_bad
    print()
    print("  VERDICT: " + (
        "PASS — no projected contaminant arrival precedes any window close in "
        "any of the 32 runs, and the reconcile holds"
        if not bad else
        f"FAIL (VOID per prereg SS8 V3) — strict_fail={strict_fail[:3]} "
        f"recon_bad={recon_bad}"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
