"""Benchmark + live-fire validation for the genesis performance utilities.

Three sections:

  (A) EQUIVALENCE + extractor speedup — proves the vectorized
      ``fast_winding_extractor.extract_2_3_omega_fast`` is bit-identical to the
      driver's ``crystal_graft_v2_run.extract_2_3_omega`` (the MEASUREMENT
      INSTRUMENT must not drift, ave-driver-script-honesty) and times both on a
      real evolved N=52 ω field.

  (B) Parallel-runner demo — 6 dummy 10-second runs, serial vs ProcessPool;
      asserts the parallel results are IDENTICAL to the serial results (same
      seeds ⇒ same output) before reporting the wall-clock speedup.

  (C) One-table summary.

Run:  python src/scripts/vol_1_foundations/perf_utils_benchmark.py
      (flags: --dummy-seconds, --extractor-reps)

IMPORTANT (spawn safety): ``_dummy_run`` is defined at MODULE scope, not inside
the ``__main__`` guard, so the spawned workers can import it by qualified name
without re-running the benchmark body.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
import time
from pathlib import Path

import numpy as np

_SRC = Path(__file__).resolve().parents[2]
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from ave.utils.fast_winding_extractor import (  # noqa: E402
    extract_2_3_omega_fast,
    verify_equivalence,
)
from ave.utils.genesis_parallel_runner import (  # noqa: E402
    RunSpec,
    default_workers,
    run_specs,
)


def _load_driver():
    """Load the graft-v2 driver as a module by file path (it is a script, not a
    package) to borrow the ORIGINAL extractor + find_shell + the engine seed."""
    drv = _SRC / "scripts" / "vol_1_foundations" / "crystal_graft_v2_run.py"
    spec = importlib.util.spec_from_file_location("crystal_graft_v2_run", drv)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ── top-level (spawn-pickleable) dummy worker for the parallel demo ──────────
def _dummy_run(*, seconds: float, seed: int) -> float:
    """A stand-in for one genesis arm: sleeps ``seconds`` (the I/O+step wall) then
    returns a SEEDED draw via a local Generator (the runner passes ``seed`` through
    because this signature declares it), so the return value is deterministic and
    identical serial-or-parallel."""
    time.sleep(seconds)
    return float(np.random.default_rng(seed).random())


def bench_extractor(driver, reps: int = 8, N: int = 52):
    """Time original vs fast extractor on a real evolved N=52 ω field."""
    print("\n" + "=" * 74)
    print(f"  (A) EXTRACTOR — equivalence gate + speedup (N={N})")
    print("=" * 74, flush=True)

    # bit-equivalence gate first (planted / null / random)
    print("  equivalence gate:", flush=True)
    verify_equivalence(driver.extract_2_3_omega, N=N, tol=1e-12)

    # build a REAL evolved field: seed a known (2,3), step the leapfrog so π_ω is
    # the genuine velocity (not the analytic seed), then read the shell.
    eng = driver.CrystalGraftV2(N=N, S_min=1e-3, omega_gap=1.0, buckle_on=False)
    R0 = 0.22 * N
    eng.seed_omega_known_2_3(R0, R0 / driver.PHI2, amplitude=0.3, p=2, q=3)
    for _ in range(20):
        eng.step()
    omega = eng.omega
    pi_omega = eng.omega_velocity()
    R, r = driver.find_shell(omega, N)

    # correctness on THIS field
    ref = driver.extract_2_3_omega(omega, pi_omega, R, r, N)
    fast = extract_2_3_omega_fast(omega, pi_omega, R, r, N)
    assert ref["w_tor"] == fast["w_tor"] and ref["w_pol"] == fast["w_pol"]

    # warm up (JIT-free numpy, but page caches / first-touch)
    driver.extract_2_3_omega(omega, pi_omega, R, r, N)
    extract_2_3_omega_fast(omega, pi_omega, R, r, N)

    t0 = time.perf_counter()
    for _ in range(reps):
        driver.extract_2_3_omega(omega, pi_omega, R, r, N)
    t_old = (time.perf_counter() - t0) / reps

    t0 = time.perf_counter()
    for _ in range(reps):
        extract_2_3_omega_fast(omega, pi_omega, R, r, N)
    t_new = (time.perf_counter() - t0) / reps

    speedup = t_old / t_new if t_new > 0 else float("inf")
    print(
        f"  evolved field read: (w_tor,w_pol)=({ref['w_tor']},{ref['w_pol']}) "
        f"shell R={R:.2f} r={r:.2f}",
        flush=True,
    )
    print(
        f"  old extract_2_3_omega   : {t_old*1e3:8.2f} ms / call",
        flush=True,
    )
    print(
        f"  new extract_2_3_omega_fast: {t_new*1e3:8.2f} ms / call  "
        f"→  {speedup:.1f}x",
        flush=True,
    )
    return {"t_old_ms": t_old * 1e3, "t_new_ms": t_new * 1e3, "speedup": speedup}


def bench_parallel(dummy_seconds: float = 10.0, n_runs: int = 6):
    """Serial vs ProcessPool on ``n_runs`` dummy runs; assert determinism first."""
    print("\n" + "=" * 74)
    print(f"  (B) PARALLEL RUNNER — {n_runs} dummy {dummy_seconds:g}s runs")
    print("=" * 74, flush=True)

    specs = [
        RunSpec(key=f"arm_{i}", func=_dummy_run,
                kwargs={"seconds": dummy_seconds}, seed=1000 + i)
        for i in range(n_runs)
    ]
    workers = min(default_workers(), n_runs)

    t0 = time.perf_counter()
    serial_res = run_specs(specs, serial=True)
    t_serial = time.perf_counter() - t0

    t0 = time.perf_counter()
    par_res = run_specs(specs, max_workers=workers)
    t_parallel = time.perf_counter() - t0

    # determinism gate: same seeds ⇒ identical results, parallel or serial
    same = all(serial_res[k] == par_res[k] for k in serial_res)
    assert set(serial_res) == set(par_res)
    assert same, f"determinism FAILED: serial={serial_res} parallel={par_res}"

    speedup = t_serial / t_parallel if t_parallel > 0 else float("inf")
    print(f"  workers used           : {workers}  (cpu_count-2 = {default_workers()})", flush=True)
    print(f"  serial   wall          : {t_serial:7.2f} s", flush=True)
    print(f"  parallel wall          : {t_parallel:7.2f} s  →  {speedup:.1f}x", flush=True)
    print(f"  determinism (serial==parallel): {same}", flush=True)
    return {
        "t_serial_s": t_serial,
        "t_parallel_s": t_parallel,
        "speedup": speedup,
        "workers": workers,
        "deterministic": bool(same),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dummy-seconds", type=float, default=10.0)
    ap.add_argument("--extractor-reps", type=int, default=8)
    ap.add_argument("--n-runs", type=int, default=6)
    args = ap.parse_args()

    t_start = time.perf_counter()
    driver = _load_driver()
    ext = bench_extractor(driver, reps=args.extractor_reps)
    par = bench_parallel(dummy_seconds=args.dummy_seconds, n_runs=args.n_runs)

    print("\n" + "=" * 74)
    print("  (C) SUMMARY")
    print("=" * 74)
    print(f"  {'metric':<34}{'old/serial':>14}{'new/parallel':>16}{'speedup':>10}")
    print("  " + "-" * 72)
    print(
        f"  {'winding extractor (ms/call)':<34}"
        f"{ext['t_old_ms']:>14.2f}{ext['t_new_ms']:>16.2f}{ext['speedup']:>9.1f}x"
    )
    print(
        f"  {f'{args.n_runs} runs x {args.dummy_seconds:g}s (wall s)':<34}"
        f"{par['t_serial_s']:>14.2f}{par['t_parallel_s']:>16.2f}{par['speedup']:>9.1f}x"
    )
    print("  " + "-" * 72)
    print(f"  determinism (serial==parallel): {par['deterministic']}")
    print(f"  total benchmark wall: {time.perf_counter() - t_start:.1f}s", flush=True)


if __name__ == "__main__":
    main()
