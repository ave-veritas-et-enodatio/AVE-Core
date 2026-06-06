"""Observable-Battery sweep harness — runs the engine over an N-D parameter
cube with NO axis pre-judged (PREREG ``research/2026-06-05_observable-battery-
infrastructure-prereg.md`` §4).

``SweepSpec`` declares ``parameter_grid: dict[str, list]``; ``expand_grid`` is
``itertools.product`` over the declared axes (amplitude, n_periods, N, arm,
chirality, seed, temperature, op14_mode — **the driver declares which it
varies; none privileged**). ``run_one_config`` builds the engine, attaches a
``BatteryObserver``, runs, then ``extract_full`` on the converged state →
``ObservableReport``. Per config:

  * ``sim_{id}.json`` — full battery + config + per-sim analysis + metadata
    (honesty tags + engine flags)
  * a columnar ``{name}_results.npz`` (rows=configs, cols=all scalar channels)
    for cube-slicing
  * ``{name}_manifest.json`` — the run manifest (every config, its json path,
    its verdicts, the honesty tags)

**Which axis discriminates is read OFF the cube, not decided up front.**

This harness COMPOSES the validated Arm-C imposed-(2,3) engine builder from
the r10 driver (``_run_armC_full_field`` / ``_run_armB_full_field``) as the
default engine factory — KEEP-BOTH (the existing bespoke sweeps untouched). A
caller may pass any ``engine_builder(**config) -> (engine, build_meta)``.

Constants strictly from ``ave.core.constants`` (``ave-canonical-source``).
This is measurement infrastructure + tool-validation (``consistency-vs-
emergence``) — NOT an emergence / α claim; forward reads only.
"""

from __future__ import annotations

import itertools
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

import numpy as np

from ave.core.observable_battery import (
    ObservableBattery,
    ObservableReport,
    analyze_report,
    make_battery_observer,
    _jsonify,
    CHANNEL_TAGS,
    SUBCHANNEL_TAGS,
)


# ─────────────────────────────────────────────────────────────────────────────
# SweepSpec — the declarative cube. No axis privileged.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class SweepSpec:
    """A parameter-cube sweep specification.

    ``parameter_grid`` maps each varied axis → its list of values; the cube is
    the itertools.product of ALL declared axes (none privileged). ``cadence``
    is the per-step observer cadence. ``output_dir`` receives the per-sim json,
    the columnar npz, and the manifest.
    """

    name: str
    parameter_grid: dict[str, list]
    output_dir: str
    cadence: int = 5
    reactance_omega: float = 1.0
    # axes that are engine-builder kwargs (vs battery/analysis knobs). The
    # default builder (Arm-C) takes N / PML / n_periods / amplitude / arm.
    builder_axes: tuple[str, ...] = ("N", "PML", "n_periods", "amplitude", "arm")

    def expand_grid(self) -> list[dict[str, Any]]:
        """itertools.product over the declared axes → list of config dicts.
        Deterministic ordering (sorted axis names) so a run is reproducible."""
        if not self.parameter_grid:
            return [{}]
        axes = sorted(self.parameter_grid.keys())
        value_lists = [self.parameter_grid[a] for a in axes]
        configs = []
        for combo in itertools.product(*value_lists):
            configs.append({a: v for a, v in zip(axes, combo)})
        return configs


# ─────────────────────────────────────────────────────────────────────────────
# Default engine builder — COMPOSES the validated Arm-C / Arm-B imposed-(2,3)
# builders from the r10 driver (KEEP-BOTH; redefines neither).
# ─────────────────────────────────────────────────────────────────────────────
def default_engine_builder(arm: str = "C", N: int = 32, PML: int = 4,
                           n_periods: int = 16, amplitude: float = 0.40,
                           **_ignored) -> tuple[Any, dict]:
    """Build + run an engine for one config (COMPOSED from r10):

      * ``arm="C"`` → ``_run_armC_full_field`` (imposed-(2,3) KNOWN-signal control)
      * ``arm="B"`` → ``_run_armB_full_field`` (matched baseline, trivial topology)

    Returns ``(engine, build_meta)`` with the engine ALREADY STEPPED to
    convergence. (The r10 builders run their own loop; this default factory
    therefore returns a converged engine — ``run_one_config`` then re-runs the
    BatteryObserver via a thin re-attach pass to populate the scalar history,
    OR uses ``attach_and_run`` for a from-scratch instrumented run; see below.)

    NOTE: because the r10 builders step internally with their own observer, the
    default factory is used in the ``prebuilt`` path of ``run_one_config`` —
    the converged engine is instrumented post-hoc for ``extract_full`` + a final
    ``sample_cheap`` snapshot. For a fully per-step-instrumented run use
    ``attach_and_run`` with a from-scratch builder.
    """
    import sys
    from pathlib import Path as _Path
    here = _Path(__file__).resolve()
    scripts_dir = here.parents[2] / "scripts" / "vol_1_foundations"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    from r10_2_3_winding_extractor_coordinate import (   # COMPOSED builders
        _run_armC_full_field, _run_armB_full_field,
    )
    if str(arm).upper() == "B":
        engine, meta = _run_armB_full_field(N=N, PML=PML, n_periods=n_periods,
                                            amplitude=amplitude)
        meta["arm"] = "B"
    else:
        engine, meta = _run_armC_full_field(N=N, PML=PML, n_periods=n_periods,
                                            amplitude=amplitude)
        meta["arm"] = "C"
    meta.update({"N": N, "PML": PML, "n_periods": n_periods, "amplitude": amplitude})
    return engine, meta


# ─────────────────────────────────────────────────────────────────────────────
# run_one_config — build, instrument, run, extract → ObservableReport.
# ─────────────────────────────────────────────────────────────────────────────
def run_one_config(
    config: dict[str, Any],
    sim_id: str,
    spec: SweepSpec,
    engine_builder: Callable[..., tuple[Any, dict]] = default_engine_builder,
    prebuilt: bool = True,
) -> ObservableReport:
    """Run one cube config end-to-end.

    ``prebuilt=True`` (default, for the r10 Arm-C/Arm-B builders that step
    internally): the builder returns a CONVERGED engine; we attach the battery
    for a final ``sample_cheap`` snapshot + ``extract_full`` heavy walk. The
    scalar-history then holds the converged snapshot (1 record) — sufficient
    for the forward verdicts, which read the converged state.

    ``prebuilt=False``: the builder returns a FRESH engine + an ``n_steps``;
    we attach the BatteryObserver and step it ourselves, so the scalar history
    is the full per-step series (enables the dispersion FFT + retention curve).
    """
    builder_kwargs = {k: v for k, v in config.items() if k in spec.builder_axes}
    t0 = time.time()
    battery = ObservableBattery(
        pml_thickness=int(config.get("PML", 0)),
        reactance_omega=float(spec.reactance_omega),
    )

    if prebuilt:
        engine, build_meta = engine_builder(**builder_kwargs)
        # final converged snapshot (1 cheap record) + heavy walk
        snap = battery.sample_cheap(engine)
        scalar_history = {ch: [val] for ch, val in snap.items()
                          if ch not in ("t", "step_count")}
        # seed a probe sample so dispersion has something (single-snapshot run
        # has no series → dispersion will honestly report INCONCLUSIVE)
        full = battery.extract_full(engine)
        drive_off_step = None
    else:
        engine, build_meta = engine_builder(**builder_kwargs)
        n_steps = int(build_meta.get("n_steps", 0))
        obs = make_battery_observer(battery, cadence=int(spec.cadence))
        engine.add_observer(obs)
        for _ in range(n_steps):
            engine.step()
        scalar_history = {}
        for rec in obs.history:
            for ch, val in rec.items():
                if ch in ("t", "step_count"):
                    continue
                scalar_history.setdefault(ch, []).append(val)
        full = battery.extract_full(engine)
        drive_off_step = build_meta.get("drive_off_step")

    report = ObservableReport(
        name=sim_id,
        config=dict(config),
        scalar_history=scalar_history,
        full=full,
    )
    report.inconclusive = list(full.get("_inconclusive", []))

    # forward per-sim analysis (prereg §4)
    report.analysis = analyze_report(report, drive_off_step=drive_off_step)

    # metadata: engine flags so a Γ≈0 is never misread (prereg §2 #1)
    k4 = getattr(engine, "k4", None)
    report.metadata.update({
        "sim_id": sim_id,
        "elapsed_s": round(time.time() - t0, 3),
        "engine_class": type(engine).__name__,
        "engine_kind": "vacuum-engine-3d",
        "op3_bond_reflection": bool(getattr(k4, "op3_bond_reflection", False))
                               if k4 is not None else None,
        "use_asymmetric_saturation": bool(getattr(
            getattr(engine, "_coupled", None), "use_asymmetric_saturation", False)),
        "V_SNAP": float(getattr(engine, "V_SNAP", 1.0)),
        "N": int(getattr(engine, "N", 0)),
        "PML": int(config.get("PML", 0)),
        "build_meta": _jsonify(build_meta),
        "prebuilt": prebuilt,
        "constants": _jsonify(ObservableBattery.CONSTANTS),
        "honesty_tags": {"channels": CHANNEL_TAGS, "subchannels": SUBCHANNEL_TAGS},
        "scope": "measurement-infrastructure (consistency-vs-emergence: tool "
                 "validation, NOT an emergence/α claim); forward reads only",
    })
    return report


# ─────────────────────────────────────────────────────────────────────────────
# run_sweep — the full cube → per-sim json + columnar npz + manifest.
# ─────────────────────────────────────────────────────────────────────────────
def run_sweep(
    spec: SweepSpec,
    engine_builder: Callable[..., tuple[Any, dict]] = default_engine_builder,
    prebuilt: bool = True,
    verbose: bool = True,
) -> dict[str, Any]:
    """Run the full parameter cube. Writes per-sim json + a columnar npz +
    a manifest into ``spec.output_dir``. Returns the manifest dict.

    No axis privileged: ``expand_grid`` is the itertools.product of every
    declared axis. The npz lets a caller slice the cube along ANY axis after
    the fact (which axis discriminates is read OFF the cube, prereg §4)."""
    out = Path(spec.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    configs = spec.expand_grid()

    manifest: dict[str, Any] = {
        "name": spec.name,
        "n_configs": len(configs),
        "parameter_grid": spec.parameter_grid,
        "cadence": spec.cadence,
        "axes": sorted(spec.parameter_grid.keys()),
        "scope": "measurement-infrastructure — no axis pre-judged",
        "sims": [],
    }

    column_rows: list[dict] = []  # for the columnar npz

    for i, config in enumerate(configs):
        sim_id = f"sim_{i:04d}"
        if verbose:
            print(f"[{i + 1}/{len(configs)}] {sim_id}  {config}", flush=True)
        try:
            report = run_one_config(config, sim_id, spec,
                                    engine_builder=engine_builder,
                                    prebuilt=prebuilt)
            json_path = out / f"{sim_id}.json"
            json_path.write_text(json.dumps(report.to_dict(), indent=2))
            row = _columnar_row(report)
            column_rows.append(row)
            manifest["sims"].append({
                "sim_id": sim_id,
                "config": _jsonify(config),
                "json": json_path.name,
                "verdicts": {k: report.analysis.get(k, {}).get("verdict")
                             for k in ("boundary_condition", "mode_class",
                                       "topology_class", "lc_class", "regime_class")},
                "inconclusive": report.inconclusive,
                "elapsed_s": report.metadata.get("elapsed_s"),
            })
        except Exception as exc:   # one bad config doesn't kill the cube
            if verbose:
                print(f"    ! {sim_id} FAILED: {type(exc).__name__}: {exc}", flush=True)
            manifest["sims"].append({
                "sim_id": sim_id, "config": _jsonify(config),
                "error": f"{type(exc).__name__}: {exc}",
            })

    # columnar npz: rows=configs, cols=all scalar channels (cube-slicing)
    npz_path = out / f"{spec.name}_results.npz"
    _write_columnar_npz(npz_path, column_rows, configs)
    manifest["npz"] = npz_path.name

    manifest_path = out / f"{spec.name}_manifest.json"
    manifest_path.write_text(json.dumps(_jsonify(manifest), indent=2))
    manifest["manifest_path"] = str(manifest_path)

    if verbose:
        ok = sum(1 for s in manifest["sims"] if "error" not in s)
        print(f"\nSWEEP DONE: {ok}/{len(configs)} ok → {out}", flush=True)
    return manifest


# ─────────────────────────────────────────────────────────────────────────────
# Columnar extraction — flatten the scalar channels into a row for the npz.
# ─────────────────────────────────────────────────────────────────────────────
def _columnar_row(report: ObservableReport) -> dict:
    """Flatten the converged-state scalar channels + the headline verdicts into
    a flat numeric row for the columnar npz (cube-slicing)."""
    row: dict[str, Any] = {}
    # config axes
    for k, v in report.config.items():
        row[f"cfg_{k}"] = v
    # headline Γ
    refl = report.latest_scalar("reflection") or {}
    row["gamma_at_max_A2"] = refl.get("gamma_at_max_A2", np.nan)
    row["sign_gamma_at_max_A2"] = refl.get("sign_gamma_at_max_A2", 0)
    row["A2_at_max_bond"] = refl.get("A2_at_max_bond", np.nan)
    row["gamma_abs_max"] = refl.get("gamma_abs_max", np.nan)
    # reactances
    rx = report.latest_scalar("reactances") or {}
    row["XL_over_XC_median"] = rx.get("XL_over_XC_median", np.nan)
    row["XL_over_XC_closest_to_1"] = rx.get("XL_over_XC_closest_to_1", np.nan)
    # regime
    reg = report.latest_scalar("regime") or {}
    row["max_A2_total"] = reg.get("max_A2_total", np.nan)
    row["rupture_cells"] = reg.get("rupture", 0)
    # energy7
    e7 = report.latest_scalar("energy7") or {}
    row["C_over_L"] = e7.get("C_over_L", np.nan)
    row["E_K4"] = e7.get("E_K4", np.nan)
    # helicity
    hel = report.latest_scalar("helicity") or {}
    row["h_K4_abs_mean"] = hel.get("h_K4_abs_mean", np.nan)
    # boundary M/Q/J (from full)
    mqj = report.full.get("boundary_MQJ", {})
    row["M"] = mqj.get("M", np.nan)
    row["Q_proxy"] = mqj.get("Q", np.nan)
    row["J_proxy"] = mqj.get("J", np.nan)
    # (2,3) winding (from full)
    w = report.full.get("winding_2_3", {})
    row["w1_base"] = w.get("w1_base", np.nan)
    row["w2_fibre"] = w.get("w2_fibre", np.nan)
    row["crossing_count_c"] = w.get("crossing_count_c", np.nan)
    row["is_2_3"] = int(bool(w.get("is_2_3", False)))
    # theta_RP (from full)
    th = report.full.get("theta_RP", {})
    row["theta_RP_circular_R"] = th.get("theta_RP_circular_R", np.nan)
    # verdict codes (categorical → string column kept separately)
    row["_verdict_boundary"] = report.analysis.get("boundary_condition", {}).get("verdict", "")
    row["_verdict_mode"] = report.analysis.get("mode_class", {}).get("verdict", "")
    row["_verdict_topology"] = report.analysis.get("topology_class", {}).get("verdict", "")
    row["_verdict_lc"] = report.analysis.get("lc_class", {}).get("verdict", "")
    row["_verdict_regime"] = report.analysis.get("regime_class", {}).get("verdict", "")
    return row


def _write_columnar_npz(path: Path, rows: list[dict], configs: list[dict]) -> None:
    """Write the columnar npz: numeric cols as float arrays, verdict cols as
    string arrays. rows=configs (sim order), cols=channels."""
    if not rows:
        np.savez(path, empty=np.array([]))
        return
    # union of all keys (configs may have heterogeneous axes)
    keys: list[str] = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    arrays: dict[str, np.ndarray] = {}
    for k in keys:
        vals = [r.get(k, np.nan) for r in rows]
        if k.startswith("_verdict") or any(isinstance(v, str) for v in vals):
            arrays[k] = np.array([str(v) for v in vals], dtype=object)
        else:
            arrays[k] = np.array([float(v) if v is not None else np.nan
                                  for v in vals], dtype=float)
    np.savez(path, **arrays)


# ─────────────────────────────────────────────────────────────────────────────
# Aggregator + summary (Step 8 fills the rendering; the structural aggregate is
# here so run_sweep + aggregate share the same npz schema).
# ─────────────────────────────────────────────────────────────────────────────
def aggregate_sweep(output_dir: str, name: str) -> dict[str, Any]:
    """Load the columnar npz + manifest and produce the cross-config aggregate
    (Γ-sign distribution, verdict tallies, channel-population coverage). The
    rendering (heatmaps / bars) is added in Step 8; this is the structural
    aggregate the renderer consumes."""
    out = Path(output_dir)
    npz_path = out / f"{name}_results.npz"
    manifest_path = out / f"{name}_manifest.json"
    if not npz_path.exists():
        return {"error": f"no npz at {npz_path}"}
    data = np.load(npz_path, allow_pickle=True)
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

    agg: dict[str, Any] = {"name": name, "n_configs": len(manifest.get("sims", []))}
    # Γ-sign distribution
    if "sign_gamma_at_max_A2" in data:
        signs = data["sign_gamma_at_max_A2"].astype(float)
        agg["gamma_sign"] = {
            "n_open_plus1": int(np.sum(signs > 0)),
            "n_short_minus1": int(np.sum(signs < 0)),
            "n_zero": int(np.sum(signs == 0)),
        }
    # verdict tallies
    for vcol, label in (("_verdict_boundary", "boundary"),
                        ("_verdict_mode", "mode"),
                        ("_verdict_topology", "topology"),
                        ("_verdict_lc", "lc"),
                        ("_verdict_regime", "regime")):
        if vcol in data:
            verdicts = [str(v) for v in data[vcol]]
            tally: dict[str, int] = {}
            for v in verdicts:
                tally[v] = tally.get(v, 0) + 1
            agg[f"verdict_{label}"] = tally
    # channel-population coverage: which channels are non-NaN across the cube
    coverage: dict[str, float] = {}
    for k in data.files:
        if k.startswith("_verdict") or k.startswith("cfg_"):
            continue
        arr = data[k]
        if arr.dtype == object:
            continue
        coverage[k] = float(np.mean(~np.isnan(arr.astype(float))))
    agg["channel_coverage"] = coverage
    return agg


# ─────────────────────────────────────────────────────────────────────────────
# render_sweep_summary — the cube-slice visuals (Γ-sign matrix, Θ_RP heatmap,
# (2,3) grid, E7 bars, retention). Forward visualization only; no fit overlays.
# ─────────────────────────────────────────────────────────────────────────────
def render_sweep_summary(output_dir: str, name: str) -> Optional[str]:
    """Render the sweep summary PNG: per-config Γ-sign (OPEN/SHORT) bar, the
    Γ-vs-A² scatter across the cube, the X_L/X_C distribution, and the verdict
    tally. Returns the PNG path (or None if matplotlib unavailable). Forward
    visualization — no fits, no target lines."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:   # pragma: no cover
        return None

    out = Path(output_dir)
    npz_path = out / f"{name}_results.npz"
    if not npz_path.exists():
        return None
    data = np.load(npz_path, allow_pickle=True)
    n = len(data["sign_gamma_at_max_A2"]) if "sign_gamma_at_max_A2" in data else 0
    if n == 0:
        return None

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    fig.suptitle(f"Observable-Battery sweep summary — {name}  (n={n})  "
                 f"[forward reads; measurement infrastructure]", fontsize=11)

    idx = np.arange(n)

    # (0,0) Γ_at_max_A2 per config, colored by sign (OPEN +1 / SHORT −1).
    ax = axes[0, 0]
    g = data["gamma_at_max_A2"].astype(float) if "gamma_at_max_A2" in data else np.full(n, np.nan)
    signs = data["sign_gamma_at_max_A2"].astype(float) if "sign_gamma_at_max_A2" in data else np.zeros(n)
    colors = np.where(signs > 0, "tab:red", np.where(signs < 0, "tab:blue", "0.6"))
    ax.bar(idx, g, color=colors)
    ax.axhline(0.0, color="k", lw=0.8)
    ax.set_title("Γ_at_max_A2_bond  (red=+1 OPEN, blue=−1 SHORT)")
    ax.set_xlabel("config index"); ax.set_ylabel("Γ at most-saturated bond")
    ax.set_ylim(-1.05, 1.05)

    # (0,1) max_A2_total per config (how close to a boundary).
    ax = axes[0, 1]
    a2 = data["max_A2_total"].astype(float) if "max_A2_total" in data else np.full(n, np.nan)
    ax.bar(idx, a2, color="tab:green")
    ax.axhline(1.0, color="0.4", ls="--", lw=0.8, label="A²=1 (wall forms)")
    ax.set_title("max_A²_total  (regime — boundary formation)")
    ax.set_xlabel("config index"); ax.set_ylabel("max A²"); ax.legend(fontsize=8)

    # (1,0) X_L/X_C distribution (LC-matched → 1).
    ax = axes[1, 0]
    if "XL_over_XC_median" in data:
        r = data["XL_over_XC_median"].astype(float)
        ax.bar(idx, r, color="tab:purple")
        ax.axhline(1.0, color="0.4", ls="--", lw=0.8, label="X_L/X_C=1 (LC-matched)")
        ax.set_title("X_L/X_C median  (ω=drive, engineering-input)")
        ax.set_xlabel("config index"); ax.set_ylabel("X_L/X_C"); ax.legend(fontsize=8)

    # (1,1) (2,3) winding read per config (w1_base, w2_fibre, is_2_3 marker).
    ax = axes[1, 1]
    if "w1_base" in data and "w2_fibre" in data:
        w1 = data["w1_base"].astype(float); w2 = data["w2_fibre"].astype(float)
        is23 = data["is_2_3"].astype(float) if "is_2_3" in data else np.zeros(n)
        ax.plot(idx, w1, "o-", label="w1_base (expect 2)", color="tab:orange")
        ax.plot(idx, w2, "s-", label="w2_fibre (expect 3)", color="tab:cyan")
        hit = idx[is23 > 0]
        if hit.size:
            ax.scatter(hit, np.full(hit.size, 3.2), marker="*", s=120,
                       color="gold", edgecolor="k", label="is_2_3", zorder=5)
        ax.set_title("(2,3) winding read  (confidence-gated)")
        ax.set_xlabel("config index"); ax.set_ylabel("winding"); ax.legend(fontsize=8)

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    png_path = out / f"{name}_summary.png"
    fig.savefig(png_path, dpi=110)
    plt.close(fig)
    return str(png_path)
