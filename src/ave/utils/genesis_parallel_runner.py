"""Generic ProcessPool harness for the embarrassingly-parallel genesis matrix.

The crystal-graft / electron-genesis sweeps are a matrix of INDEPENDENT runs
(arms × saturation-fracs × run-length-doublings). `crystal_graft_v2_run.full_run`
executes its three arms (`e_main` / `e_chir` / `e_null`) SERIALLY even though
nothing couples them — wall-clock is the sum, not the max. This harness fans the
matrix out across cores and returns results keyed by the caller's spec id.

Design constraints (why it is shaped this way):

* **Spawn-safe on macOS.** The default start method on darwin/py3.8+ is ``spawn``
  (re-imports the module in each worker). Specs therefore carry *top-level*
  callables and pickleable kwargs ONLY — no lambdas, no closures, no bound
  methods. `_execute_spec` is module-level so the pool can import it.
* **Determinism is preserved, parallel OR serial.** Each spec carries an explicit
  integer ``seed``. The worker re-seeds ``random`` + ``numpy.random`` from it
  immediately before the call, so the result depends only on (func, kwargs, seed)
  — never on worker identity, dispatch order, or pool reuse. ``serial=True`` runs
  the exact same re-seed-then-call loop in-process; same seed ⇒ same result.
* **Headroom for live workflows.** Default worker count is ``cpu_count() - 2`` so
  a sweep launched next to an interactive driver does not starve it.
* **Reproducible debugging.** ``serial=True`` collapses to a single process with
  identical seeding, so a crash can be reproduced and stepped without the pool.

Example — wiring the graft-v2 arm × frac matrix
-----------------------------------------------
The runner needs a *top-level* worker function (spawn-pickleable). Define one
that builds an engine, steps it, and reads the winding — then enumerate the
matrix as specs::

    # in some driver module `crystal_graft_v4_sweep.py`
    from ave.utils.genesis_parallel_runner import RunSpec, run_specs

    def denovo_arm(*, N, helicity, with_photon, k_wind, n_steps, seed):
        # seed is already applied to the global RNGs by the runner; passed in
        # too so the body can build a local Generator if it prefers.
        from crystal_graft_v2_run import _denovo_run, find_shell, extract_2_3_omega
        e = _denovo_run(N, helicity, with_photon, k_wind, n_steps)
        R, r, r_meas = find_shell(e.omega, N, return_r_meas=True)
        res = extract_2_3_omega(e.omega, e.omega_velocity(), R, r, N)
        res["r_meas"] = r_meas
        return res

    specs = []
    for arm, (hel, phot, kw) in {
        "photon_radial": (1.0, True, 0),
        "photon_1twist": (1.0, True, 1),
        "no_photon_null": (0.0, False, 0),
    }.items():
        for frac_steps in (700, 1400, 2800):          # run-length doublings
            key = f"{arm}@{frac_steps}"
            specs.append(RunSpec(
                key=key,
                func=denovo_arm,
                kwargs=dict(N=52, helicity=hel, with_photon=phot,
                            k_wind=kw, n_steps=frac_steps),
                seed=hash(key) & 0xFFFFFFFF,           # explicit per-run seed
            ))

    results = run_specs(specs)                          # {key: res-dict}
    # results == run_specs(specs, serial=True)           # bit-identical
"""

from __future__ import annotations

import inspect
import os
import random
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, Optional

try:  # numpy is a hard dep of every caller, but keep the seeding optional-safe
    import numpy as _np
except Exception:  # pragma: no cover - numpy always present in AVE
    _np = None


__all__ = ["RunSpec", "run_specs", "default_workers"]


def default_workers() -> int:
    """``cpu_count() - 2`` clamped to ``>= 1`` — leave 2 cores for live work."""
    n = os.cpu_count() or 2
    return max(1, n - 2)


@dataclass(frozen=True)
class RunSpec:
    """One independent run in the matrix.

    Attributes
    ----------
    key:
        Hashable id the result is returned under. Must be unique within a batch.
    func:
        A TOP-LEVEL (module-importable) callable. No lambdas / closures / bound
        methods — they are not spawn-pickleable.
    kwargs:
        Pickleable keyword args passed straight to ``func``.
    seed:
        Explicit RNG seed. Applied to ``random`` + ``numpy.random`` immediately
        before the call. ``None`` ⇒ the runner does not touch global RNG state
        (the func is expected to be deterministic on its own, or to seed itself).
    """

    key: Any
    func: Callable[..., Any]
    kwargs: Dict[str, Any] = field(default_factory=dict)
    seed: Optional[int] = None


def _apply_seed(seed: Optional[int]) -> None:
    """Deterministically seed the legacy global RNGs (same in worker or serial)."""
    if seed is None:
        return
    random.seed(seed)
    if _np is not None:
        _np.random.seed(seed & 0xFFFFFFFF)


def _declares_seed(func: Callable) -> bool:
    """True iff ``func`` has an EXPLICIT parameter named ``seed`` (so the runner
    can pass the spec seed through for the modern local-``Generator(seed)`` idiom).
    A bare ``**kwargs`` does NOT count — injection must be unambiguous."""
    try:
        params = inspect.signature(func).parameters
    except (TypeError, ValueError):
        return False
    p = params.get("seed")
    return p is not None and p.kind in (p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)


def _execute_spec(spec: RunSpec):
    """Worker entry point — MUST be top-level for spawn pickling.

    Seeds the global RNGs from ``spec.seed`` AND, if ``spec.func`` declares an
    explicit ``seed`` parameter (and the caller did not already supply one), passes
    the seed through — so both the global-``np.random`` idiom and the local
    ``np.random.default_rng(seed)`` idiom are deterministic.

    Returns ``(key, result)`` on success or ``(key, _Err(...))`` on failure so the
    parent can attribute every outcome to its spec without losing the batch.
    """
    _apply_seed(spec.seed)
    call_kwargs = dict(spec.kwargs)
    if spec.seed is not None and "seed" not in call_kwargs and _declares_seed(spec.func):
        call_kwargs["seed"] = spec.seed
    t0 = time.perf_counter()
    try:
        result = spec.func(**call_kwargs)
    except Exception as exc:  # noqa: BLE001 - re-surfaced to the parent with key
        import traceback

        return spec.key, _Err(repr(exc), traceback.format_exc())
    return spec.key, _Timed(result, time.perf_counter() - t0)


@dataclass
class _Err:
    repr: str
    traceback: str


@dataclass
class _Timed:
    value: Any
    seconds: float


def run_specs(
    specs: Iterable[RunSpec],
    *,
    serial: bool = False,
    max_workers: Optional[int] = None,
    raise_on_error: bool = True,
    return_timings: bool = False,
) -> Dict[Any, Any]:
    """Execute ``specs`` across processes (or in-process if ``serial``).

    Parameters
    ----------
    specs:
        Iterable of :class:`RunSpec`. Keys must be unique.
    serial:
        Run in-process with the identical re-seed-then-call loop. Same seeds ⇒
        bit-identical results to the parallel path; use for debugging.
    max_workers:
        Pool size. Defaults to :func:`default_workers` (``cpu_count() - 2``).
    raise_on_error:
        If True (default) re-raise a combined error after the batch completes,
        naming every spec that failed (fail-loud, deterministic ordering by the
        spec sequence — not by completion order). If False, the result dict holds
        ``_Err`` objects for the failed keys and the caller inspects them.
    return_timings:
        If True, the result dict maps ``key -> (value, wall_seconds)``.

    Returns
    -------
    dict
        ``{spec.key: result}`` (or ``{key: (result, seconds)}`` if
        ``return_timings``). Insertion order follows the input spec order so a
        serial and a parallel run iterate identically.
    """
    specs = list(specs)
    keys = [s.key for s in specs]
    if len(set(keys)) != len(keys):
        dupes = sorted({k for k in keys if keys.count(k) > 1}, key=repr)
        raise ValueError(f"RunSpec keys must be unique; duplicates: {dupes}")

    raw: Dict[Any, Any] = {}
    if serial:
        for spec in specs:
            k, payload = _execute_spec(spec)
            raw[k] = payload
    else:
        workers = max_workers if max_workers is not None else default_workers()
        workers = max(1, min(workers, len(specs))) if specs else 1
        # chunksize=1: every run is heavy + we want per-spec seeding isolation.
        with ProcessPoolExecutor(max_workers=workers) as pool:
            for k, payload in pool.map(_execute_spec, specs, chunksize=1):
                raw[k] = payload

    # Re-key in INPUT order (deterministic iteration regardless of completion).
    ordered = {s.key: raw[s.key] for s in specs}

    errors = {k: p for k, p in ordered.items() if isinstance(p, _Err)}
    if errors and raise_on_error:
        lines = [f"  [{k!r}] {p.repr}" for k, p in errors.items()]
        first_tb = next(iter(errors.values())).traceback
        raise RuntimeError(
            f"{len(errors)}/{len(specs)} run(s) failed:\n"
            + "\n".join(lines)
            + f"\n\nFirst traceback:\n{first_tb}"
        )

    out: Dict[Any, Any] = {}
    for key, payload in ordered.items():
        if isinstance(payload, _Err):
            out[key] = payload  # raise_on_error=False path: surface the error obj
        elif return_timings:
            out[key] = (payload.value, payload.seconds)
        else:
            out[key] = payload.value
    return out
