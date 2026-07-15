#!/usr/bin/env python3
"""BLOB-ABLATION — core-holding mechanism fork (kernel-OFF + amplitude sweep).

FROZEN NOTE (freeze-by-push BEFORE any battery result): research/2026-07-15_blob-ablation_NOTE.md

Question (Grant-walked, fired in-chat 2026-07-15): is the #698 PML-box
core-holding datum (fixed 33-site geom-center core ball 0.611 → 0.920, +50.6 %
phase-averaged, while the interior drains −17.5 % and H falls −12.2 %)
  (A) LINEAR MODE-SORTING — the sponge sieves the radiative components, leaving
      the bound core-concentrated fraction (survives S≡1; ~amplitude-invariant), or
  (B) NONLINEAR SELF-TRAPPING — the live saturation kernel makes the core a
      slow-wave region (a self-dug index well) that gathers the interior's
      residual energy once the wake stops stirring (dies with the kernel OFF;
      hold-fraction grows disproportionately with amplitude).

Rule-14 anti-rebuild: the METER is the corrected #698 instrument
(`gpersist_localization_observable`) imported verbatim — `_meter_snapshot`,
`_core_holding`, `_classify_cell`, `_trend`. No re-implemented meter, no new
engine, no retune. This driver only (i) builds the engine in a kernel VARIANT
(ON / OFF-mem native toggle / OFF-lin disclosed S≡1 disabled-flag), (ii) scales
the seed amplitude self-similarly, (iii) tracks max_A²_local for the sub-yield
guard. The ON / amp 1.0 / no-ablation path is asserted byte-parity vs the #698
`run_instrumented` (--parity).

Kernel conditions (NOTE §Kernel-OFF; DISCLOSURE):
  on       — rank-4 production, use_memristive_saturation=True (baseline).
  off_mem  — native toggle use_memristive_saturation=False; removes ONLY the
             memristive lag (the stateful "live kernel"); instantaneous S=√(1−A²)
             index remains.
  off_lin  — DISCLOSED minimal disabled-flag: pin the saturation index to the
             unsaturated limit S≡1 by overriding three bound methods on the built
             instance (z_local≡Z₀ at BOTH the coupling and k4 update sites →
             matched, Γ=0, linear TLM; ω-clamp shared-front Γ≡0 → Ω₀≡0 → inert
             wall). Converter / bulk / geometry / seed / sponge byte-identical to
             baseline. Validated by the torus energy-conservation sanity (run 10).

Usage:
  python blob_ablation_kernel_off.py --parity  N PML MODE FID
  python blob_ablation_kernel_off.py --run     N PML MODE KERNEL AMP FID
  python blob_ablation_kernel_off.py --battery  FID
  python blob_ablation_kernel_off.py --sweep    FID   # disclosed working amp sweep
  python blob_ablation_kernel_off.py --diag     FID   # inertness probe + F1 patched-ordering
  python blob_ablation_kernel_off.py --aggregate
(run with PYTHONPATH=src so `scripts.vol_1_foundations.*` imports resolve.)
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

from ave.core.constants import ALPHA
from ave.core.genesis_v18_coupled import snapshot_op14, tau_steps_k4
from ave.core.loop_gap_harness import PHI_BASELINE_FLOOR, make_engine
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, A_YIELD, apply_seed
from ave.topological.k4_cosserat_coupling import _v_squared_per_site

# Reuse the corrected #698 meter verbatim (Rule-14). Package import (pytest
# pythonpath=["src"] / PYTHONPATH=src) with a direct-script fallback.
try:
    from scripts.vol_1_foundations.gpersist_localization_observable import (
        CORE_RADII,
        PRIMARY_R,
        SECTORS,
        _classify_cell,
        _core_holding,
        _meter_snapshot,
        _trend,
        run_instrumented,
    )
except ModuleNotFoundError:  # invoked as a bare script from its own dir
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from vol_1_foundations.gpersist_localization_observable import (  # type: ignore
        CORE_RADII,
        PRIMARY_R,
        SECTORS,
        _classify_cell,
        _core_holding,
        _meter_snapshot,
        _trend,
        run_instrumented,
    )

NOTE = "research/2026-07-15_blob-ablation_NOTE.md"
OUT_DIR = Path("assets/sim_outputs/blob_ablation_kernel_off")

KERNELS = ("on", "off_mem", "off_lin")
AMP_MARKS = {"sqrt_alpha": float(np.sqrt(ALPHA)), "sqrt_2alpha": float(np.sqrt(2.0 * ALPHA)), "yield": 1.0}
A2_YIELD = 1.0  # sub-yield guard: abort + INSTRUMENT-for-that-run if max_A²_local >= 1

# ---------------------------------------------------------------------------
# Kernel-OFF S≡1 ablation (DISCLOSED minimal disabled-flag; NOTE §Kernel-OFF)
# ---------------------------------------------------------------------------
def _ablate_to_linear(coupled) -> None:
    """Pin the saturation index to the unsaturated limit S≡1 on the built engine.

    Three bound-method overrides on the instance (visible, local, no engine
    source edit):
      1. coupled._update_z_local_total     -> z_local ≡ 1 (=Z₀, matched, Γ=0)
      2. coupled.k4._update_z_local_field  -> z_local ≡ 1 (defeats the in-k4.step
         V_inc-keyed memristive/instantaneous recompute)
      3. coupled._freeze_clamp_omega0_shared -> 0 (shared-front Γ≡0 ⇒ Ω₀≡0 ⇒ the
         moving Γ=−1 ω-wall is inert)
    Everything else (trilinear converter, linear-elastic Cosserat bulk, geometry,
    seed, sponge, schedule) is byte-identical to baseline. Single-variable
    ablation: only the amplitude-dependent saturation index is removed.
    """
    N = coupled.N

    def _z_unsat():
        coupled.k4.z_local_field = np.ones((N, N, N), dtype=float)

    _z_unsat()  # pin the initial state too
    coupled._update_z_local_total = _z_unsat
    coupled.k4._update_z_local_field = _z_unsat

    _zeros = np.zeros((N, N, N), dtype=float)

    def _omega0_unsat():
        coupled.cos._clamp_weight = _zeros.copy()
        return _zeros.copy()

    coupled._freeze_clamp_omega0_shared = _omega0_unsat


def _linear_pin_ok(coupled) -> float:
    """Max |z_local − 1| over the grid — 0 iff the S≡1 pin holds this step."""
    return float(np.max(np.abs(np.asarray(coupled.k4.z_local_field, dtype=float) - 1.0)))


# ---------------------------------------------------------------------------
# Instrumented mirror loop with the kernel VARIANT + self-similar amplitude
# (mirrors #698 run_instrumented; only the build + amp + A²-guard added).
# ---------------------------------------------------------------------------
def _build_variant(
    N: int, pml: int, mode: str, kernel: str, amp_scale: float, field_scale: float = 1.0
):
    """Build the rank-4 engine in a kernel VARIANT.

    `amp_scale` is the FROZEN pair-seed amp knob (multiplies the seed `amp`). NB
    the pair seed front-normalizes to R_II (genesis_v18_coupled.pair_seed_cosserat:
    scale_cosserat_to_front target=R_II), so `amp_scale` is a NO-OP for pair mode —
    this is a disclosed INSTRUMENT defect on the frozen sweep axis (Rule-10 caught
    at integrator time; see the RESULT addendum §Instrument).

    `field_scale` is the DISCLOSED WORKING amplitude knob (supplementary axis, NOT
    the frozen one): a post-seed multiply of the Cosserat pair field, applied
    BEFORE the wall freeze so the frozen converter wall matches the scaled field.
    It genuinely scales the front A²_cos ∝ field_scale² (0.75·field_scale²), so it
    probes the (B) superlinear-hold signature the frozen knob could not.
    """
    assert kernel in KERNELS, kernel
    memristive = kernel == "on"
    engine = make_engine(
        4, N=N, bulk_density_on=True, pml=pml, use_memristive_saturation=memristive
    )
    apply_seed(
        engine,
        mode,
        amp=amp_scale * float(np.sqrt(ALPHA)),
        a_lock=A_LOCK_DEFAULT,
        front_target=A_YIELD,
    )
    if field_scale != 1.0:  # disclosed working amplitude knob (post-seed, pre-freeze)
        engine._coupled.cos.u *= field_scale
        engine._coupled.cos.omega *= field_scale
    engine.apply_bulk_probe_ic(amp=amp_scale * 0.08)
    engine.freeze_converter_wall()
    if kernel == "off_lin":
        _ablate_to_linear(engine._coupled)
    return engine


def run_ablation(
    N: int, pml: int, mode: str, kernel: str, amp_scale: float, fast: bool,
    field_scale: float = 1.0,
) -> dict:
    """One cell: mirror the #670/#698 drive/quiet schedule, record the corrected
    meter per quiet step, track max_A²_local, enforce the sub-yield guard."""
    t0 = time.time()
    engine = _build_variant(N, pml, mode, kernel, amp_scale, field_scale=field_scale)
    coupled = engine._coupled

    tau = tau_steps_k4(coupled, fast=fast)
    n_drive = max(6 if fast else 10, int(round(0.5 * tau)))
    n_quiet = max(10 if fast else 20, int(round(1.5 * tau)))
    n_total = n_drive + n_quiet

    obs0 = snapshot_op14(coupled)
    obs_driveoff = obs0
    phi_baseline = max(obs0["phi_link_sq"], PHI_BASELINE_FLOOR)
    max_a2 = float(coupled.max_A_squared())
    linear_pin_max = _linear_pin_ok(coupled) if kernel == "off_lin" else 0.0
    aborted = False
    series: list[dict] = []
    for t in range(1, n_total + 1):
        engine.step()
        a2 = float(coupled.max_A_squared())
        max_a2 = max(max_a2, a2)
        if kernel == "off_lin":
            linear_pin_max = max(linear_pin_max, _linear_pin_ok(coupled))
        obs_t = snapshot_op14(coupled)
        if t == 1:
            phi_baseline = max(obs_t["phi_link_sq"], PHI_BASELINE_FLOOR)
        if t <= n_drive:
            obs_driveoff = obs_t
        if t >= n_drive:
            m = _meter_snapshot(coupled, periodic=(pml == 0))
            m["t"] = t
            m["phase"] = "drive_off" if t == n_drive else "quiet"
            m["H"] = float(obs_t["H"])
            m["phi_link_sq"] = float(obs_t["phi_link_sq"])
            m["max_A2_local"] = a2
            series.append(m)
        if max_a2 >= A2_YIELD:  # sub-yield guard (frozen): abort this run
            aborted = True
            break
    obs_end = obs_t

    H_drive = max(obs_driveoff["H"], 1e-30)
    E_persist = obs_end["H"] / H_drive
    phi_drive = max(obs_driveoff["phi_link_sq"], phi_baseline)
    phi_persist = obs_end["phi_link_sq"] / phi_drive if phi_drive > 0 else 0.0

    trend = {}
    stats = ["PR", "PR_frac"] + [f"CF_peak_{r}" for r in CORE_RADII] + [
        f"CF_geom_{r}" for r in CORE_RADII
    ]
    for sec in SECTORS:
        trend[sec] = {stat: _trend(series, sec, stat) for stat in stats}

    res = {
        "N": N,
        "pml": pml,
        "boundary": "torus" if pml == 0 else "PML",
        "seed_mode": mode,
        "kernel": kernel,
        "amp_scale": amp_scale,
        "field_scale": field_scale,
        "fidelity": "smoke" if fast else "production",
        "n_drive": n_drive,
        "n_quiet": n_quiet,
        "E_persist": float(E_persist),
        "phi_persist": float(phi_persist),
        "max_A2_local": max_a2,
        "A2_marks": AMP_MARKS,
        "sub_yield": bool(max_a2 < A2_YIELD),
        "aborted_over_yield": bool(aborted),
        "linear_pin_max_abs": float(linear_pin_max),
        "M_interior": series[-1]["M"],
        "trend": trend,
        "series": series,
        "wall_seconds": round(time.time() - t0, 1),
        "note": NOTE,
    }
    res["classification"] = _classify_cell(res)
    res["core_holding"] = _core_holding(res)
    return res


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _cell_path(N, pml, mode, kernel, amp_scale, fast) -> Path:
    fid = "smoke" if fast else "prod"
    a = f"{amp_scale:.2f}".replace(".", "p")
    return OUT_DIR / f"cell_N{N}_pml{pml}_{mode}_{kernel}_amp{a}_{fid}.json"


def _write(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True))


def _fmt_ch(ch: dict) -> str:
    return (
        f"core {ch['E_core_full_driveoff']:.3f}->{ch['E_core_full_quietavg']:.3f} "
        f"({ch['E_core_full_rel']:+.1%}) | rest-int {ch['E_rest_interior_rel']:+.1%} | "
        f"H {ch['H_rel']:+.1%}"
    )


def cmd_parity(argv) -> None:
    """ON / amp 1.0 / no-ablation must reproduce #698 run_instrumented byte-for-byte."""
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    fast = fid == "smoke"
    ref = run_instrumented(N, pml, mode, fast, plant=False)
    ref["classification"] = _classify_cell(ref)
    ref_ch = _core_holding(ref)
    mine = run_ablation(N, pml, mode, "on", 1.0, fast)
    my_ch = mine["core_holding"]
    keys = ["E_core_full_driveoff", "E_core_full_quietavg", "E_core_full_rel",
            "E_rest_interior_rel", "H_rel"]
    dmax = max(abs(ref_ch[k] - my_ch[k]) for k in keys)
    de = abs(mine["E_persist"] - ref["E_persist"]) / max(abs(ref["E_persist"]), 1e-30)
    ok = dmax <= 1e-9 and de <= 1e-9
    print(
        f"[parity] N={N} pml={pml} {mode} {fid}: core-holding maxΔ={dmax:.2e} "
        f"relΔE_persist={de:.2e} -> {'PASS' if ok else 'FAIL'}\n"
        f"    ref  : {_fmt_ch(ref_ch)}\n    mine : {_fmt_ch(my_ch)}",
        flush=True,
    )
    _write(OUT_DIR / f"parity_N{N}_pml{pml}_{mode}_{fid}.json",
           {"ref": ref_ch, "mine": my_ch, "maxDelta": dmax, "relDeltaE": de,
            "parity_pass": bool(ok), "note": NOTE})
    if not ok:
        raise SystemExit("PARITY FAILED — mirror loop drifted from the #698 instrument")


def cmd_run(argv) -> None:
    N, pml, mode, kernel, amp, fid = (
        int(argv[0]), int(argv[1]), argv[2], argv[3], float(argv[4]), argv[5]
    )
    fast = fid == "smoke"
    res = run_ablation(N, pml, mode, kernel, amp, fast)
    _write(_cell_path(N, pml, mode, kernel, amp, fast), res)
    ch = res["core_holding"]
    c = res["classification"]
    yflag = "ABORT>=yield" if res["aborted_over_yield"] else ("sub-yield" if res["sub_yield"] else "?")
    pin = f" pin|z-1|max={res['linear_pin_max_abs']:.1e}" if kernel == "off_lin" else ""
    print(
        f"[run] N={N} {res['boundary']:5s} {mode} {kernel:7s} amp={amp:.2f} {fid:5s}: "
        f"{_fmt_ch(ch)} | banked={c['signature_banked_qmean']}->full={c['signature_qmean']} "
        f"| maxA2={res['max_A2_local']:.4f} ({yflag}){pin} [{res['wall_seconds']}s]",
        flush=True,
    )


BATTERY = [
    # (N, pml, mode, kernel, amp_scale)  — the frozen grid (NOTE §THE BATTERY)
    (14, 3, "pair", "on", 1.0),       # 1  baseline / datum
    (14, 3, "pair", "off_mem", 1.0),  # 2  native toggle
    (14, 3, "pair", "off_lin", 1.0),  # 3  primary discriminator (S≡1)
    (14, 3, "pair", "on", 0.5),       # 4  sweep-lo
    (14, 3, "pair", "on", 1.5),       # 6  sweep-hi (5 == run 1)
    (14, 0, "pair", "on", 1.0),       # 7  torus datum
    (14, 0, "pair", "on", 0.5),       # 8  torus twin lo
    (14, 0, "pair", "on", 1.5),       # 9  torus twin hi
    (14, 0, "pair", "off_lin", 1.0),  # 10 conservation sanity
    (14, 0, "pair", "off_mem", 1.0),  # 11 off-mem torus cross-check
]


def cmd_battery(argv) -> None:
    fid = argv[0] if argv else "prod"
    fast = fid == "smoke"
    for (N, pml, mode, kernel, amp) in BATTERY:
        res = run_ablation(N, pml, mode, kernel, amp, fast)
        _write(_cell_path(N, pml, mode, kernel, amp, fast), res)
        ch = res["core_holding"]
        yflag = "ABORT" if res["aborted_over_yield"] else "ok"
        print(
            f"[battery] {res['boundary']:5s} {kernel:7s} amp={amp:.2f}: {_fmt_ch(ch)} "
            f"| maxA2={res['max_A2_local']:.4f}({yflag}) [{res['wall_seconds']}s]",
            flush=True,
        )


# DISCLOSED working amplitude sweep (supplementary axis; the frozen pair-seed amp
# knob was a no-op — front-normalized). field_scale post-scales the Cosserat seed
# ⇒ A²_cos = 0.75·field_scale² (sub-yield for field_scale < 1.155). NOT the frozen
# knob; reported as a disclosed amendment (KEEP-BOTH). Probes the (B) signature.
SWEEP_FIELD = (0.50, 0.75, 1.0, 1.10)  # A²_cos ≈ 0.19 / 0.42 / 0.75 / 0.91


def _sweep_path(N, pml, kernel, fs, fast) -> Path:
    fid = "smoke" if fast else "prod"
    f = f"{fs:.2f}".replace(".", "p")
    return OUT_DIR / f"sweep_N{N}_pml{pml}_{kernel}_fs{f}_{fid}.json"


def cmd_sweep(argv) -> None:
    """Disclosed working amplitude sweep: kernel-ON PML across field_scale, plus
    torus twins at the endpoints (wake-stirring contrast). Probes whether the
    core-hold-fraction grows disproportionately with amplitude (the (B) signature)."""
    fid = argv[0] if argv else "prod"
    fast = fid == "smoke"
    plan = [(14, 3, "on", fs) for fs in SWEEP_FIELD]
    plan += [(14, 0, "on", fs) for fs in (SWEEP_FIELD[0], SWEEP_FIELD[-1])]
    for (N, pml, kernel, fs) in plan:
        res = run_ablation(N, pml, "pair", kernel, 1.0, fast, field_scale=fs)
        _write(_sweep_path(N, pml, kernel, fs, fast), res)
        ch = res["core_holding"]
        yflag = "ABORT" if res["aborted_over_yield"] else "ok"
        print(
            f"[sweep] {res['boundary']:5s} {kernel:7s} field_scale={fs:.2f}: {_fmt_ch(ch)} "
            f"| A2cos_front={res['max_A2_local']:.4f}({yflag}) [{res['wall_seconds']}s]",
            flush=True,
        )


# ---------------------------------------------------------------------------
# Inertness probe + F1 patched-ordering diagnostic (regenerable evidence for the
# post-review amendments; findings 1/4/7). Ships the numbers the "why the kernel
# is inert" section previously carried as prose-only one-off measurements.
# ---------------------------------------------------------------------------
def _a2_k4_max(coupled) -> float:
    v_sq = _v_squared_per_site(coupled.k4.V_inc)
    a2 = np.asarray(v_sq, dtype=float) / (coupled.V_SNAP**2)
    alive = np.asarray(coupled.k4.mask_active, dtype=bool)
    return float(a2[alive].max()) if alive.any() else 0.0


def run_inertness_probe(N: int, pml: int, fast: bool) -> dict:
    """Per-step trajectory scan of the three saturation-kernel channels on the
    datum cell (ON, amp 1.0): A²_k4 (V-sector Op14 short), Γ_shared (asymmetric
    front), Ω₀ (moving Γ=−1 ω-clamp wall). Regenerates the numbers the RESULT
    §'Why the kernel is inert' reports; the review found they were prose-only."""
    engine = _build_variant(N, pml, "pair", "on", 1.0)
    coupled = engine._coupled
    tau = tau_steps_k4(coupled, fast=fast)
    n_total = max(6 if fast else 10, int(round(0.5 * tau))) + max(
        10 if fast else 20, int(round(1.5 * tau))
    )

    def _probe():
        g = np.asarray(coupled._impedance_gamma_shared(), dtype=float)
        w = np.asarray(coupled._freeze_clamp_omega0_shared(), dtype=float)
        return _a2_k4_max(coupled), float(g.min()), float(g.max()), float(w.max())

    seed = _probe()
    a2k4_run = seed[0]
    g_min_run, g_max_run = seed[1], seed[2]
    w_max_run, w_max_t = seed[3], 0
    for t in range(1, n_total + 1):
        engine.step()
        a2k4, gmn, gmx, wmx = _probe()
        a2k4_run = max(a2k4_run, a2k4)
        g_min_run = min(g_min_run, gmn)
        g_max_run = max(g_max_run, gmx)
        if wmx > w_max_run:
            w_max_run, w_max_t = wmx, t
    return {
        "cell": f"N{N}_pml{pml}_pair_on_amp1.0",
        "n_total": n_total,
        "seed_t0": {"A2_k4": seed[0], "gamma_min": seed[1], "gamma_max": seed[2], "omega0_max": seed[3]},
        "run": {
            "A2_k4_max": a2k4_run,
            "gamma_shared_min": g_min_run,
            "gamma_shared_max": g_max_run,
            "omega0_max": w_max_run,
            "omega0_argmax_t": w_max_t,
        },
        "note": NOTE,
    }


def run_patched_ordering_diag(N: int, pml: int, fast: bool) -> dict:
    """F1 patched-ordering diagnostic: no-op k4's V-only z_local recompute so the
    coupling's Cosserat-informed z_local (`_update_z_local_total`) SURVIVES into
    the bond-Γ consumer, then compare core-hold-rel to the shipped-ordering datum.
    +0.0000% ⇒ restoring the F1-defeated bond-short leg is immaterial at this
    config (the channel gates the ~0-energy V-sector)."""
    ref = run_ablation(N, pml, "pair", "on", 1.0, fast)
    ref_rel = ref["core_holding"]["E_core_full_rel"]

    # patched build: identical to the datum cell, but the k4 V-only recompute is
    # disabled so the coupling short is not overwritten before _connect_all.
    engine = _build_variant(N, pml, "pair", "on", 1.0)
    coupled = engine._coupled
    coupled.k4._update_z_local_field = lambda: None  # keep the coupling z_local live
    tau = tau_steps_k4(coupled, fast=fast)
    n_drive = max(6 if fast else 10, int(round(0.5 * tau)))
    n_quiet = max(10 if fast else 20, int(round(1.5 * tau)))
    obs0 = snapshot_op14(coupled)
    obs_driveoff = obs0
    z_live_max = 0.0
    series: list[dict] = []
    for t in range(1, n_drive + n_quiet + 1):
        engine.step()
        z_live_max = max(z_live_max, float(np.max(np.abs(np.asarray(coupled.k4.z_local_field) - 1.0))))
        obs_t = snapshot_op14(coupled)
        if t <= n_drive:
            obs_driveoff = obs_t
        if t >= n_drive:
            m = _meter_snapshot(coupled, periodic=(pml == 0))
            m["t"] = t
            m["H"] = float(obs_t["H"])
            m["phi_link_sq"] = float(obs_t["phi_link_sq"])
            series.append(m)
    patched = {"series": series}
    pch = _core_holding(patched)
    return {
        "cell": f"N{N}_pml{pml}_pair_on_amp1.0",
        "shipped_core_rel": ref_rel,
        "patched_core_rel": pch["E_core_full_rel"],
        "delta_core_rel": pch["E_core_full_rel"] - ref_rel,
        "coupling_zlocal_max_abs_dev": z_live_max,
        "shipped_core": [ref["core_holding"]["E_core_full_driveoff"], ref["core_holding"]["E_core_full_quietavg"]],
        "patched_core": [pch["E_core_full_driveoff"], pch["E_core_full_quietavg"]],
        "note": NOTE,
    }


def cmd_diag(argv) -> None:
    fid = argv[0] if argv else "prod"
    fast = fid == "smoke"
    probe = run_inertness_probe(14, 3, fast)
    diag = run_patched_ordering_diag(14, 3, fast)
    _write(OUT_DIR / f"inertness_probe_{'smoke' if fast else 'prod'}.json", probe)
    _write(OUT_DIR / f"patched_ordering_diag_{'smoke' if fast else 'prod'}.json", diag)
    s, r = probe["seed_t0"], probe["run"]
    print("=== inertness probe (datum cell, per-step over the full trajectory) ===")
    print(f"  SEED t=0 : A2_k4={s['A2_k4']:.3e}  gamma=[{s['gamma_min']:+.3e},{s['gamma_max']:+.3e}]  omega0={s['omega0_max']:.3e}")
    print(f"  RUN      : A2_k4_max={r['A2_k4_max']:.3e}  gamma=[{r['gamma_shared_min']:+.3e},{r['gamma_shared_max']:+.3e}]  "
          f"omega0_max={r['omega0_max']:.3e} @t={r['omega0_argmax_t']}")
    print("=== F1 patched-ordering diagnostic (coupling z_local kept live) ===")
    print(f"  coupling |z-1| max in-run = {diag['coupling_zlocal_max_abs_dev']:.3e} (channel genuinely live)")
    print(f"  shipped core-rel = {diag['shipped_core_rel']:+.6f}  patched core-rel = {diag['patched_core_rel']:+.6f}  "
          f"delta = {diag['delta_core_rel']:+.6f} ({diag['delta_core_rel']:+.4%})")


# --- frozen decision rule (NOTE §FROZEN verdict classes) -------------------
def _superlinear(lo: float, mid: float, hi: float) -> tuple[bool, str]:
    convex = (hi - mid) > (mid - lo)
    threshold = lo <= 0.0 < mid
    monotone = hi >= mid >= lo
    sig = "SUPERLINEAR" if ((convex and monotone) or threshold) else (
        "FRACTION-PRESERVING" if max(abs(lo - mid), abs(hi - mid), abs(lo - hi)) <= 0.10
        else "OTHER"
    )
    return (sig == "SUPERLINEAR"), sig


def _disc_sweep_signature(sweeps: list) -> tuple[str | None, dict, list]:
    """Signature of the DISCLOSED working field_scale sweep — the REAL amplitude
    axis (the frozen amp knob is a no-op / front-normalized). Returns
    (disc_sig, disc_map, rels). disc_sig is None when the sweep is absent."""
    pml_s = sorted([s for s in sweeps if s["pml"] == 3], key=lambda s: s["field_scale"])
    if not pml_s:
        return None, {}, []
    rels = [s["core_holding"]["E_core_full_rel"] for s in pml_s]
    disc_map = {f"fs_{s['field_scale']:.2f}": s["core_holding"]["E_core_full_rel"] for s in pml_s}
    if len(rels) < 3:
        return "SWEEP-INCOMPLETE", disc_map, rels
    spread = max(rels) - min(rels)
    convex = (rels[-1] - rels[-2]) > (rels[1] - rels[0])
    thresh = rels[0] <= 0.0 < rels[-1]
    if thresh or (convex and rels == sorted(rels) and spread > 0.10):
        sig = "SUPERLINEAR"
    elif spread <= 0.10:
        sig = "FRACTION-PRESERVING"
    else:
        sig = "AMPLITUDE-DEPENDENT-OTHER"
    return sig, disc_map, rels


def cmd_aggregate() -> None:
    cells = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("cell_*.json"))]
    prod = [c for c in cells if c["fidelity"] == "production"]
    sweeps = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("sweep_*.json"))
              if json.loads(p.read_text())["fidelity"] == "production"]

    def _find(pml, kernel, amp):
        for c in prod:
            if c["pml"] == pml and c["kernel"] == kernel and abs(c["amp_scale"] - amp) < 1e-9:
                return c
        return None

    base = _find(3, "on", 1.0)
    off_mem = _find(3, "off_mem", 1.0)
    off_lin = _find(3, "off_lin", 1.0)
    swp = {a: _find(3, "on", a) for a in (0.5, 1.0, 1.5)}
    cons = _find(0, "off_lin", 1.0)  # torus conservation sanity

    # The REAL amplitude axis (disclosed field_scale sweep). The MODE-SORTING /
    # SELF-TRAPPING amplitude conjunct GATES ON THIS (review findings 2/8: the
    # frozen amp cells are a structural no-op and can never fire SUPERLINEAR).
    disc_sig, disc, disc_rels = _disc_sweep_signature(sweeps)
    # The frozen amp axis is computed for DISCLOSURE ONLY and does not gate.
    frozen_sweep_sig = None
    if all(swp[a] is not None for a in (0.5, 1.0, 1.5)):
        lo, mid, hi = (swp[a]["core_holding"]["E_core_full_rel"] for a in (0.5, 1.0, 1.5))
        _, frozen_sweep_sig = _superlinear(lo, mid, hi)

    verdict = "INCOMPLETE"
    reasons: list[str] = []
    split = None
    if base is None:
        verdict, reasons = "INSTRUMENT", ["baseline (run 1) missing"]
    else:
        bch = base["core_holding"]
        repro = (
            0.40 <= bch["E_core_full_rel"] <= 0.60
            and -0.22 <= bch["E_rest_interior_rel"] <= -0.13
            and -0.16 <= bch["H_rel"] <= -0.08
            and not base["aborted_over_yield"]
        )
        if not repro:
            verdict = "INSTRUMENT"
            reasons.append(
                f"reproduction-gate FAIL: core_rel={bch['E_core_full_rel']:+.3f} "
                f"int_rel={bch['E_rest_interior_rel']:+.3f} H_rel={bch['H_rel']:+.3f} "
                f"aborted={base['aborted_over_yield']}"
            )
        cons_ok = cons is not None and abs(cons["core_holding"]["H_rel"]) <= 0.02 and not cons["aborted_over_yield"]
        if cons is None:
            verdict = "INSTRUMENT"; reasons.append("conservation sanity (run 10) missing")
        elif not cons_ok:
            verdict = "INSTRUMENT"
            reasons.append(f"conservation-gate FAIL: torus OFF-lin |H_rel|={abs(cons['core_holding']['H_rel']):.4f} > 0.02")
        if verdict != "INSTRUMENT" and off_lin is not None:
            olch = off_lin["core_holding"]
            ol = olch["E_core_full_rel"]
            split = (ol / bch["E_core_full_rel"]) if abs(bch["E_core_full_rel"]) > 1e-12 else None
            mem_cls = None
            if off_mem is not None:
                omr = off_mem["core_holding"]["E_core_full_rel"]
                mem_cls = "KILL" if omr <= 0.10 else ("PRESERVE" if omr >= 0.40 else "PARTIAL")
            if disc_sig is None or disc_sig == "SWEEP-INCOMPLETE":
                # the working amplitude axis is absent → do NOT let the vacuous
                # frozen axis silently satisfy the conjunct (findings 2/8).
                lean = "MODE-SORTING" if ol >= 0.40 else ("SELF-TRAPPING" if ol <= 0.10 else "MIXED")
                verdict = f"{lean}-PENDING-SWEEP"
                reasons.append(
                    "SWEEP-INCOMPLETE: disclosed field_scale sweep absent — amplitude axis "
                    "un-adjudicated (the frozen amp knob is a no-op; run `--sweep`)"
                )
            elif ol <= 0.10 and disc_sig == "SUPERLINEAR":
                verdict = "SELF-TRAPPING"
            elif ol >= 0.40 and disc_sig == "FRACTION-PRESERVING":
                verdict = "MODE-SORTING"
            else:
                verdict = "MIXED"
                reasons.append(
                    f"OFF-lin core_rel={ol:+.3f} (split={split if split is None else round(split,3)}) "
                    f"disclosed_sweep={disc_sig} off_mem={mem_cls}"
                )
        elif verdict != "INSTRUMENT":
            verdict = "INSTRUMENT"; reasons.append("primary discriminator (run 3 off_lin) missing")

    print("\n=== BLOB-ABLATION — kernel-OFF + amplitude sweep ===")
    print(f"NOTE: {NOTE}")
    hdr = f"{'boundary':6s} {'kernel':7s} {'amp':>4s} | {'core drive->quiet (rel)':28s} | {'int':>7s} {'H':>7s} | banked->full(qmean) | maxA2"
    print(hdr)
    for c in sorted(prod, key=lambda c: (c["pml"], c["kernel"], c["amp_scale"])):
        ch = c["core_holding"]; cl = c["classification"]
        print(
            f"{c['boundary']:6s} {c['kernel']:7s} {c['amp_scale']:>4.1f} | "
            f"{ch['E_core_full_driveoff']:.3f}->{ch['E_core_full_quietavg']:.3f} "
            f"({ch['E_core_full_rel']:+.1%})".ljust(38)
            + f"| {ch['E_rest_interior_rel']:+6.1%} {ch['H_rel']:+6.1%} | "
            f"{cl['signature_banked_qmean']}->{cl['signature_qmean']} | "
            f"{c['max_A2_local']:.4f}{'*ABORT' if c['aborted_over_yield'] else ''}"
        )
    # --- DISCLOSED working amplitude sweep (field_scale; the frozen pair-seed amp
    # sweep was a no-op — front-normalized). Real (A)-vs-(B) sweep evidence; this
    # is the axis the verdict conjunct gates on above (review findings 2/8). ------
    if sweeps:
        print("\n=== DISCLOSED working amplitude sweep (field_scale; kernel-ON) — the GATING axis ===")
        print("     (the FROZEN pair-seed amp sweep is a NO-OP — R_II front-normalized — and does NOT gate)")
        for s in sorted(sweeps, key=lambda s: (s["pml"], s["field_scale"])):
            ch = s["core_holding"]
            print(f"  {s['boundary']:5s} field_scale={s['field_scale']:.2f} "
                  f"(A2cos~{0.75 * s['field_scale']**2:.3f}): {_fmt_ch(ch)} "
                  f"| maxA2={s['max_A2_local']:.4f}{'*ABORT' if s['aborted_over_yield'] else ''}")
        if disc_rels:
            print(f"  core-hold-rel across field_scale = {[round(r, 4) for r in disc_rels]} "
                  f"(spread={max(disc_rels) - min(disc_rels):.4f}) -> DISCLOSED sweep signature = {disc_sig}")

    print(f"\nsplit (OFF-lin plateau ÷ ON plateau) = {split if split is None else round(split, 3)}")
    print(f"FROZEN sweep signature = {frozen_sweep_sig}  [VACUOUS: frozen amp knob is a no-op — does NOT gate]")
    print(f"DISCLOSED sweep signature = {disc_sig}  [the real amplitude probe — GATES the verdict]")
    print(f"VERDICT = {verdict}  (kernel-OFF split axis + the disclosed-sweep amplitude axis)")
    for r in reasons:
        print(f"  - {r}")
    _write(OUT_DIR / "blob_ablation_summary.json",
           {"verdict": verdict, "reasons": reasons, "split_off_lin_over_on": split,
            "frozen_sweep_signature_VACUOUS": frozen_sweep_sig,
            "disclosed_sweep_signature_GATING": disc_sig, "disclosed_sweep_core_rel": disc,
            "note": NOTE,
            "cells": [{k: c[k] for k in ("boundary", "kernel", "amp_scale", "E_persist",
                                          "max_A2_local", "sub_yield", "aborted_over_yield",
                                          "linear_pin_max_abs", "core_holding", "classification")}
                      for c in sorted(prod, key=lambda c: (c["pml"], c["kernel"], c["amp_scale"]))]})
    print(f"\nsummary -> {OUT_DIR / 'blob_ablation_summary.json'}")


def main(argv) -> None:
    if not argv:
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "--parity":
        cmd_parity(rest)
    elif cmd == "--run":
        cmd_run(rest)
    elif cmd == "--battery":
        cmd_battery(rest)
    elif cmd == "--sweep":
        cmd_sweep(rest)
    elif cmd == "--diag":
        cmd_diag(rest)
    elif cmd == "--aggregate":
        cmd_aggregate()
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
