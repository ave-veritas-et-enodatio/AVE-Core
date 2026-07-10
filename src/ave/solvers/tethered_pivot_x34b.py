"""TETHERED-PIVOT RE-RUN (x34b) — the CONTROL-SUBTRACTED excess detector FROZEN A PRIORI.

FROZEN PRE-REG: research/2026-07-10_tethered-pivot-rerun_prereg.md (SHA-freeze pushed
BEFORE this driver existed — the freeze is claimed by commit ordering).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS — a THIN driver over the MERGED x34 solver (Rule 14, NO fork-copy)
═══════════════════════════════════════════════════════════════════════════════
x34 (PR #612) returned a KEEP-BOTH two-axis verdict: the frozen-§6 ABSOLUTE detector
read PARTIAL (staircase_fraction 0.4286 == the free control's own 0.4286 — confounded by
a sweep-saturation artifact common to anchored AND free), while the POST-HOC
control-subtracted EXCESS axis read TRACK (excess_staircase 0.0714, track_R2 0.9799).
The #612 verdict rested on a POST-HOC axis. This re-run does what the #612 adversarial
review's consequence 2 prescribed: FREEZE the control-subtracted excess detector as THE
primary rule (a priori), DISCLOSE its saturation-zone blindness UP FRONT, and DESIGN the
sweep so the banked verdict does NOT rest on the blind zone.

  MODE = driven traversal on the anchored (2,3); REGIME = sub-yield lossless-reactive
  (lossy-Dirichlet Γ=−1 wall, removed-norm tracked, never pumping); SECTOR = T2/Cosserat
  winding host b_ω vs the A1 mass-carrier a_A1 (the two Clifford global phases).

FROZEN PRIMARY DETECTOR (prereg §1) — the CONTROL-SUBTRACTED EXCESS axis:
  LOCK  ⇔ excess_staircase ≥ 0.4  AND excess_jumps ≥ 1
  TRACK ⇔ track_R² ≥ 0.9          AND excess_staircase < 0.2
  else PARTIAL; INCONCLUSIVE if a validation gate fails (Rule 11).

LABEL PROVENANCE (flag-don't-fix): the merged solver returns the EXCESS axis under the key
`amended_verdict` and the ABSOLUTE axis under `frozen_verdict` — HISTORICAL to #612 (where
the ABSOLUTE axis was the prereg-frozen one). In x34b the roles are DELIBERATELY inverted:
the x34b-frozen PRIMARY = the EXCESS axis (`amended_verdict`); the ABSOLUTE axis
(`frozen_verdict`) is a COMPLEMENTARY disclosure read used only in the saturation zone. The
merged solver is NOT redefined-in-place (its two-axis output is preserved intact); this
driver only RE-LABELS which axis is banked.
"""

from __future__ import annotations

from dataclasses import replace

import numpy as np

# REUSE (Rule 14): the merged x34 solver VERBATIM. No fork-copy, no new engine/physics.
from ave.solvers.tethered_pivot_winding import (
    ClampedTrace,
    TetheredPivotConfig,
    dead_actuator_gate,
    detuning_sweep,
    energy_ledger,
    lock_detector,
    run_tethered_pivot,
    validate_lock_detector,
    _planted_locked,
)

# α-leak guard (import-time). The observable is a pure arg() ratio — α-free.
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"

# ─────────────────────────────────────────────────────────────────────────────
# The FRESH primary grid (prereg §3): ω_s ∈ [0.70, 1.40] step 0.025 → 29 points.
# A REFINEMENT of #612's 15-pt step-0.05 grid (the #612 points are a subset), so
# per-point reproduction is checkable and the verdict is shown stable under refinement.
# ─────────────────────────────────────────────────────────────────────────────
FRESH_SWEEP_OS: tuple[float, ...] = tuple(round(x, 3) for x in np.arange(0.70, 1.4001, 0.025))
FLAT_TOL: float = 0.03   # frozen detector flat tolerance (prereg §1/§2c)

# #612 reproduction marks (research/2026-07-09_..._result.md §3) — frozen expectations.
REPRO_MARKS = {
    "excess_staircase": 0.0714,
    "excess_jumps": 0,
    "track_R2": 0.9799,
    "staircase_fraction": 0.4286,
    "free_staircase_fraction": 0.4286,
}


# The MEASURED fresh-sweep free control ρ_free(ω_s) — the deterministic clamp-off output at
# the frozen config on FRESH_SWEEP_OS (committed research/2026-07-10_tethered-pivot-rerun_result.json,
# fresh_leg.sweep.rho_free; regenerable via `python -m ave.solvers.tethered_pivot_x34b`). Frozen
# here as a reference so the banked-pipeline LOCK-fireability proof (R2 / #626 review) can plant a
# genuine lock on the REAL free control's in-window quasi-plateau blindness (12/23 intervals
# staircase-blind, restricted free_staircase_fraction 0.5217) WITHOUT a 4-min live sweep — closing
# the gap that the §2a plant used an idealized never-flat free control.
MEASURED_FRESH_RHO_FREE: tuple[float, ...] = (
    1.572754, 1.517991, 1.480888, 1.447911, 1.422087, 1.389460, 1.351176, 1.297028,
    1.235543, 1.175453, 1.152753, 1.131491, 0.949268, 0.945150, 0.929440, 0.921261,
    0.968315, 0.990487, 0.997371, 0.996121, 0.991750, 0.985944, 0.987406, 0.936132,
    0.937694, 0.936530, 0.936153, 0.937831, 0.942001,
)


def fresh_config() -> TetheredPivotConfig:
    """The #612 config with ONLY the sweep grid refined (everything else identical —
    N=20, 500 steps, dt=0.066, z_anchor=1.0)."""
    return replace(TetheredPivotConfig(), sweep_os=FRESH_SWEEP_OS)


# ═════════════════════════════════════════════════════════════════════════════
# SATURATION-ONSET NON-SATURATED-ZONE RESTRICTION (prereg §2c — the ONE new mechanic)
# ═════════════════════════════════════════════════════════════════════════════
def saturation_onset(rho_free: np.ndarray, *, flat_tol: float = FLAT_TOL) -> int:
    """Frozen a-priori saturation-onset rule (prereg §2c). Using the clamp-off FREE
    control ρ_free(ω_s) on the ascending grid, with flat-mask f_flat[i]=|Δρ_free[i]|<flat_tol,
    the onset interval index i_sat = the smallest i such that f_flat[j] is True for EVERY
    interval j ≥ i (the onset of the TERMINAL flat plateau). If no terminal flat run exists
    the free control never saturates within the grid → i_sat = n_intervals (full sweep is the
    non-saturated window; conservative — no blind zone to exclude)."""
    rf = np.asarray(rho_free, float)
    ok = np.isfinite(rf)
    rf = rf[ok]
    if len(rf) < 2:
        return 0
    f_flat = np.abs(np.diff(rf)) < flat_tol      # length n-1
    n_int = len(f_flat)
    i_sat = n_int                                # default: no terminal saturation
    for i in range(n_int):
        if np.all(f_flat[i:]):
            i_sat = i
            break
    return int(i_sat)


def restricted_verdict(os: np.ndarray, rho_anch: np.ndarray, rho_free: np.ndarray,
                       *, flat_tol: float = FLAT_TOL) -> dict:
    """The banked x34b verdict (prereg §2c): the FROZEN excess axis applied to the
    NON-SATURATED window (ω_s below the free-control saturation onset), reported ALONGSIDE
    the full-sweep excess verdict and the complementary absolute-axis read in the saturation
    zone (the disclosure). Excess axis = solver key `amended_verdict`; absolute = `frozen_verdict`."""
    os = np.asarray(os, float)
    ra = np.asarray(rho_anch, float)
    rf = np.asarray(rho_free, float)
    ok = np.isfinite(ra) & np.isfinite(rf)
    os_r, ra_r, rf_r = os[ok], ra[ok], rf[ok]

    i_sat = saturation_onset(rf_r, flat_tol=flat_tol)
    n_pts = len(os_r)
    # non-saturated window = points with interval index < i_sat ⇒ indices [0 .. i_sat]
    ns_hi = min(i_sat + 1, n_pts)
    ns_os, ns_ra, ns_rf = os_r[:ns_hi], ra_r[:ns_hi], rf_r[:ns_hi]

    full = lock_detector(os_r, ra_r, rf_r, flat_tol=flat_tol)
    # FULL-sweep excess verdict (companion) — the solver's amended axis on the whole sweep.
    full_excess_verdict = full["amended_verdict"]

    # BANKED verdict = the EXCESS axis on the NON-SATURATED window (where the detector CAN
    # see a lock). If the window is too small (< 3 resolved pts) the read is INCONCLUSIVE
    # (Rule 11 — honest, no rescue).
    if ns_hi >= 3:
        restr = lock_detector(ns_os, ns_ra, ns_rf, flat_tol=flat_tol)
        banked_verdict = restr["amended_verdict"]
        banked_excess_staircase = restr["excess_staircase"]
        banked_excess_jumps = restr["excess_jumps"]
        banked_track_R2 = restr["track_R2"]
    else:
        restr = {"verdict": "INCONCLUSIVE",
                 "reason": f"non-saturated window has {ns_hi} pts (<3)"}
        banked_verdict = "INCONCLUSIVE"
        banked_excess_staircase = float("nan")
        banked_excess_jumps = -1
        banked_track_R2 = float("nan")

    saturated = i_sat < (n_pts - 1)   # a terminal flat plateau was found strictly inside
    onset_os = float(os_r[i_sat]) if i_sat < n_pts else None
    return {
        "i_sat": i_sat, "n_points": n_pts, "onset_omega_s": onset_os,
        "saturated": bool(saturated),
        "nonsat_window_omega_s": [float(x) for x in ns_os],
        "nonsat_n_points": int(ns_hi),
        # THE BANKED VERDICT (single frozen excess axis, non-saturated window)
        "banked_verdict": banked_verdict,
        "banked_excess_staircase": banked_excess_staircase,
        "banked_excess_jumps": banked_excess_jumps,
        "banked_track_R2": banked_track_R2,
        # companions (reported, NOT banked)
        "full_sweep_excess_verdict": full_excess_verdict,
        "full_sweep_excess_staircase": full["excess_staircase"],
        "full_sweep_track_R2": full["track_R2"],
        # complementary ABSOLUTE disclosure read (the confounded axis, saturation zone)
        "full_sweep_absolute_verdict": full["frozen_verdict"],
        "full_sweep_absolute_staircase": full["staircase_fraction"],
        "full_sweep_free_staircase": full["free_staircase_fraction"],
        "restricted_detector": restr,
        "full_detector": full,
    }


# ═════════════════════════════════════════════════════════════════════════════
# LOCK-FIREABILITY through the BANKED pipeline (R2 / #626 review) — plant a GENUINE
# lock on the REAL free control and confirm the frozen excess axis still fires LOCK
# ═════════════════════════════════════════════════════════════════════════════
def banked_pipeline_lock_proof(free_ref: tuple[float, ...] | None = None) -> dict:
    """Plant a GENUINE staircase LOCK (the canonical `_planted_locked`) as the ANCHORED
    curve on top of the REAL fresh-sweep free control (MEASURED_FRESH_RHO_FREE, with its
    in-window quasi-plateau blindness) and push it through the ACTUAL restricted_verdict
    pipeline (saturation_onset → non-saturated window slice → lock_detector). A genuine
    BC-quantized lock MUST still bin LOCK despite the 12/23 in-window staircase-blind
    intervals — its defining discrete jumps fire the excess_jumps channel (live wherever the
    free control does not itself jump), and its plateaus over the ~11 non-flat-free intervals
    clear excess_staircase ≥ 0.4. Closes the fireability gap that the §2a plant left open
    (that plant used an idealized never-flat free control)."""
    os = np.array(FRESH_SWEEP_OS, float)
    rf = np.array(MEASURED_FRESH_RHO_FREE if free_ref is None else free_ref, float)
    ra = _planted_locked(os)                           # genuine LOCK planted as the anchor
    r = restricted_verdict(os, ra, rf)
    return {
        "planted_anchored": "genuine staircase LOCK (_planted_locked)",
        "free_control": "MEASURED fresh-sweep ρ_free (real in-window blindness, 12/23 flat)",
        "banked_verdict": r["banked_verdict"],
        "banked_excess_staircase": r["banked_excess_staircase"],
        "banked_excess_jumps": r["banked_excess_jumps"],
        "nonsat_n_points": r["nonsat_n_points"],
        "fires_lock": bool(r["banked_verdict"] == "LOCK"),
    }


def _energy_gate_catches_pump(cfg: TetheredPivotConfig) -> dict:
    """Exercise the SHIPPED `energy_ledger` gate (not an inline copy of its criterion) on a
    PLANTED pump: patch the solver's trace so the clamp-ON leg has a monotone-growing energy
    and the clamp-OFF leg conserves, then run the real energy_ledger and confirm it reports
    on_non_pumping == False. (R3 / #626 review — the gate's own field access + threshold are
    what must catch the pump.)"""
    from unittest.mock import patch
    n = 10
    z = np.zeros(n + 1)
    tr_off = ClampedTrace(t=z, phi_tor=z, psi_pol=z, e_total=np.ones(n + 1),
                          removed_cum=z, var_re_anchor=z, var_im_anchor=z)
    tr_on = ClampedTrace(t=z, phi_tor=z, psi_pol=z,
                         e_total=np.linspace(1.0, 1.001, n + 1),   # +0.1% ⇒ a pump
                         removed_cum=z, var_re_anchor=z, var_im_anchor=z)

    def _fake_trace(_cfg, *, omega_b, omega_s, branch, n_steps=None):
        return tr_off if branch == "off" else tr_on

    with patch("ave.solvers.tethered_pivot_winding.trace_orbit_clamped", _fake_trace):
        return energy_ledger(cfg, branch="capacitive", n_steps=n)


# ═════════════════════════════════════════════════════════════════════════════
# PLANTED-VIOLATION PROOFS (prereg §8) — every gate is shown to CATCH a violation
# ═════════════════════════════════════════════════════════════════════════════
def planted_violation_proofs(cfg: TetheredPivotConfig | None = None) -> dict:
    """Prove each frozen gate CATCHES a planted violation (not just passes on real data).
      • detector separation (§2a): planted staircase→LOCK, planted line→TRACK, and a
        planted flat-SHARED case (anchored==free, both flat) → excess axis TRACK (NOT LOCK).
      • saturation disclosure (§2b): planted lock in the saturation zone → absolute LOCK,
        excess NOT-LOCK, lock_suppressed_by_excess==True.
      • dead-actuator: a degenerate clamp (branch="off" vs itself) → actuator_live==False.
      • energy: a planted monotone-growing E trace → the non-pumping criterion returns False.
    """
    cfg = cfg or TetheredPivotConfig()
    proofs: dict = {}

    # --- detector separation + shared-flatness violation ---------------------
    vlk = validate_lock_detector()
    os = np.linspace(0.7, 1.4, 15)
    flat_shared = np.where(os < 1.0, 1.2, 1.0)            # anchored == free, both flat
    d_flat = lock_detector(os, flat_shared, flat_shared.copy())
    proofs["detector_separation"] = {
        "planted_staircase_verdict": vlk["planted_locked_verdict"],   # must be LOCK
        "planted_line_verdict": vlk["planted_tracking_verdict"],      # must be TRACK
        "shared_flat_absolute_verdict": d_flat["frozen_verdict"],     # absolute bins LOCK
        "shared_flat_excess_verdict": d_flat["amended_verdict"],      # excess catches it → TRACK
        "shared_flat_excess_staircase": d_flat["excess_staircase"],
        "catches_violation": bool(
            vlk["planted_locked_verdict"] == "LOCK"
            and vlk["planted_tracking_verdict"] == "TRACK"
            and d_flat["amended_verdict"] == "TRACK"     # excess subtracts shared flatness
            and d_flat["frozen_verdict"] == "LOCK"),     # absolute would have false-positived
    }

    # --- saturation-zone disclosure (the excess axis is LOCK-suppressing there) ----
    sz = vlk["saturation_zone"]
    proofs["saturation_disclosure"] = {
        "absolute_verdict": sz["frozen_verdict"],        # must SEE the lock: LOCK
        "excess_verdict": sz["amended_verdict"],         # must NOT: != LOCK
        "excess_staircase": sz["excess_staircase"],      # subtracted to 0
        "lock_suppressed_by_excess": sz["lock_suppressed_by_excess"],
        "catches_violation": bool(
            sz["frozen_verdict"] == "LOCK"
            and sz["amended_verdict"] != "LOCK"
            and sz["lock_suppressed_by_excess"] is True),
    }

    # --- dead-actuator: branch="off" compared to itself is a DEAD clamp ------
    dead_off = dead_actuator_gate(cfg, branch="off", n_steps=40)
    proofs["dead_actuator"] = {
        "off_var_ratio": dead_off["var_ratio"],
        "off_actuator_live": dead_off["actuator_live"],  # must be False (dead)
        "catches_violation": bool(dead_off["actuator_live"] is False),
    }

    # --- energy: a planted pump routed through the SHIPPED energy_ledger gate (R3) -----
    eng_planted = _energy_gate_catches_pump(cfg)
    proofs["energy_non_pumping"] = {
        "shipped_gate": "energy_ledger",                 # the real gate, not an inline copy
        "planted_on_max_rel_gain": eng_planted["on_max_rel_energy_gain"],
        "on_non_pumping_flag": eng_planted["on_non_pumping"],   # must be False (a pump)
        "off_conserved_flag": eng_planted["off_conserved"],     # sanity: off leg conserves
        "catches_violation": bool(eng_planted["on_non_pumping"] is False),
    }

    # --- LOCK-fireability through the banked pipeline on the REAL free control (R2) ----
    lock_fire = banked_pipeline_lock_proof()
    proofs["banked_pipeline_lock_fires"] = {
        **lock_fire,
        # "catches" here = the pipeline DOES fire LOCK on a genuine lock (proves the
        # negative would not be a blind miss): a TRACK verdict is a real negative.
        "catches_violation": bool(lock_fire["fires_lock"]),
    }

    proofs["all_gates_catch_violations"] = bool(
        proofs["detector_separation"]["catches_violation"]
        and proofs["saturation_disclosure"]["catches_violation"]
        and proofs["dead_actuator"]["catches_violation"]
        and proofs["energy_non_pumping"]["catches_violation"]
        and proofs["banked_pipeline_lock_fires"]["catches_violation"])
    return proofs


# ═════════════════════════════════════════════════════════════════════════════
# THE X34b PROTOCOL — reproduction leg + fresh-grid banked verdict (single axis)
# ═════════════════════════════════════════════════════════════════════════════
def run_x34b() -> dict:
    """Run the frozen x34b protocol:
      LEG A (REPRODUCTION, #612 config) — full merged protocol; check the excess-axis
        metrics reproduce the #612 marks + collect the config-level gates.
      LEG B (FRESH primary, 29-pt refined grid) — Signature-1 sweep → the FROZEN excess
        detector on the NON-SATURATED window (the banked verdict), companions reported.
      + validate-on-known (gates a/b) + planted-violation proofs (§8).
    Verdict stated on the SINGLE FROZEN axis (the excess axis); the absolute axis appears
    only as the saturation-zone disclosure read."""
    out: dict = {"test_id": "x34b",
                 "frozen_prereg": "research/2026-07-10_tethered-pivot-rerun_prereg.md",
                 "frozen_primary_axis": "control-subtracted excess (solver key amended_verdict)"}

    # ── LEG A: reproduction of #612 (full protocol, default config) ──────────
    repro = run_tethered_pivot(TetheredPivotConfig())
    det_r = repro["signature_1_mode_locking"]["detector"]
    repro_metrics = {k: det_r[k] for k in
                     ("excess_staircase", "excess_jumps", "track_R2",
                      "staircase_fraction", "free_staircase_fraction",
                      "frozen_verdict", "amended_verdict")}
    repro_cmp = {k: {"x34b": float(det_r[k]), "x34_#612": float(v),
                     "abs_diff": abs(float(det_r[k]) - float(v))}
                 for k, v in REPRO_MARKS.items()}
    repro_ok = all(c["abs_diff"] < 5e-3 for c in repro_cmp.values())
    out["reproduction_leg"] = {
        "config": "x34 #612 default (N=20, 500 steps, 15-pt step-0.05 grid)",
        "metrics": repro_metrics,
        "comparison_to_612": repro_cmp,
        "reproduces_612": bool(repro_ok),
        # the supporting nulls (excess-subtracted, shared by the frozen axis)
        "hysteresis_excess_seen": bool(repro["signature_2_hysteresis"]["hysteresis_seen"]),
        "termination_flip_seen": bool(repro["signature_3_termination_flip"]["flip_seen"]),
        "rational_points": repro["signature_1_mode_locking"]["sweep"]["rational_points"],
    }

    # config-level gates (grid-independent → shared with the fresh leg; prereg §3/§5)
    out["gates"] = {
        "validate_on_known": repro["validate_on_known"],
        "dead_actuator": repro["dead_actuator"],
        "energy_ledger": repro["energy_ledger"],
    }

    # ── LEG B: fresh-grid primary — Signature-1 → frozen excess axis, restricted ──
    cfg_fresh = fresh_config()
    sweep = detuning_sweep(cfg_fresh, branch="capacitive")
    os = np.array(sweep["os"], float)
    ra = np.array(sweep["rho_anchored"], float)
    rf = np.array(sweep["rho_free"], float)
    restricted = restricted_verdict(os, ra, rf)
    out["fresh_leg"] = {
        "config": f"fresh 29-pt refined grid (step 0.025), branch=capacitive; "
                  f"N={cfg_fresh.N}, {cfg_fresh.n_steps} steps",
        "sweep": {"os": sweep["os"], "rho_anchored": sweep["rho_anchored"],
                  "rho_free": sweep["rho_free"],
                  "rational_points": sweep["rational_points"]},
        "restricted": restricted,
    }

    # ── planted-violation proofs (§8) ────────────────────────────────────────
    out["planted_violation_proofs"] = planted_violation_proofs(TetheredPivotConfig())

    # ── THE BANKED VERDICT (single frozen excess axis, non-saturated window) ──
    gates_ok = bool(
        out["gates"]["validate_on_known"]["ok"]
        and out["gates"]["dead_actuator"]["capacitive"]["actuator_live"]
        and out["gates"]["dead_actuator"]["magnetic"]["actuator_live"]
        and out["gates"]["energy_ledger"]["on_non_pumping"])
    proofs_ok = out["planted_violation_proofs"]["all_gates_catch_violations"]

    banked = restricted["banked_verdict"]
    if not (gates_ok and proofs_ok and repro_ok):
        verdict = "INCONCLUSIVE"
        reason = (f"gate/proof/repro pre-condition failed "
                  f"(gates_ok={gates_ok}, proofs_ok={proofs_ok}, repro_ok={repro_ok})")
    else:
        verdict = banked
        _abs_s = restricted["full_sweep_absolute_staircase"]
        _free_s = restricted["full_sweep_free_staircase"]
        _rel = ("free even flatter" if _free_s > _abs_s
                else "anchored flatter" if _abs_s > _free_s else "exactly equal")
        reason = (
            f"FROZEN excess axis (a priori), banked on the NON-SATURATED window "
            f"(ω_s ≤ {restricted['onset_omega_s']}, {restricted['nonsat_n_points']} pts): "
            f"excess_staircase={restricted['banked_excess_staircase']:.4f} "
            f"(<0.2 ⇒ TRACK / ≥0.4 ⇒ LOCK), track_R²={restricted['banked_track_R2']:.4f}. "
            f"Full-sweep excess axis={restricted['full_sweep_excess_verdict']} "
            f"(excess_staircase={restricted['full_sweep_excess_staircase']:.4f}). "
            f"Saturation-zone disclosure — complementary ABSOLUTE axis (confounded): "
            f"{restricted['full_sweep_absolute_verdict']} "
            f"(staircase={_abs_s:.4f} vs free {_free_s:.4f}, both confounded-flat — "
            f"{_rel}); the excess axis is LOCK-suppressing there (disclosed a priori, "
            f"prereg §2b). Reproduces #612: "
            f"{repro_ok}. Supporting nulls: no excess hysteresis "
            f"({not out['reproduction_leg']['hysteresis_excess_seen']}), no cap↔mag flip "
            f"({not out['reproduction_leg']['termination_flip_seen']}).")

    out["verdict"] = verdict
    out["reason"] = reason
    out["preconditions"] = {"gates_ok": gates_ok, "proofs_ok": proofs_ok,
                            "reproduces_612": repro_ok}
    return out


# ═════════════════════════════════════════════════════════════════════════════
# EMIT — JSON + WHITE figure
# ═════════════════════════════════════════════════════════════════════════════
def _to_jsonable(obj):
    import numpy as _np
    if isinstance(obj, dict):
        return {k: _to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_to_jsonable(v) for v in obj]
    if isinstance(obj, (_np.floating,)):
        return float(obj)
    if isinstance(obj, (_np.integer,)):
        return int(obj)
    if isinstance(obj, (_np.bool_,)):
        return bool(obj)
    if isinstance(obj, _np.ndarray):
        return obj.tolist()
    return obj


def emit_json(res: dict, path: str) -> None:
    import json
    with open(path, "w") as f:
        json.dump(_to_jsonable(res), f, indent=2)


def emit_figure(res: dict, path: str) -> None:
    """WHITE figure (ave.viz.style.apply('print')). Three panels:
      (1) fresh-grid ρ(ω_s): anchored / free control / carrier + saturation-zone shade
          + non-saturated window + the banked verdict;
      (2) validate-on-known tracking-zone separation (planted staircase LOCK vs line TRACK);
      (3) saturation-zone disclosure: a planted lock in the saturation zone the ABSOLUTE
          axis sees but the FROZEN excess axis does NOT (the a-priori-disclosed blindness)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    from ave.viz.style import COLORS, axis_label
    from ave.solvers.tethered_pivot_winding import (
        _planted_locked, _planted_tracking,
        _planted_saturating_free, _planted_lock_in_saturation,
    )

    style.apply("print")
    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.6))

    fresh = res["fresh_leg"]
    r = fresh["restricted"]
    os = np.array(fresh["sweep"]["os"], float)
    ra = np.array(fresh["sweep"]["rho_anchored"], float)
    rf = np.array(fresh["sweep"]["rho_free"], float)
    carrier = 1.0 / os

    # ── panel 1: the fresh sweep + saturation shading + banked window ─────────
    ax = axes[0]
    ax.plot(os, carrier, "--", color=COLORS["muted"], lw=1.3,
            label=r"carrier $\omega_b/\omega_s$", zorder=1)
    ax.plot(os, rf, "o-", color=COLORS["comparison"], ms=3.5, lw=1.4,
            label=r"$\rho_{\rm free}$ (clamp OFF)", zorder=2)
    ax.plot(os, ra, "s-", color=COLORS["ave"], ms=3.5, lw=1.6,
            label=r"$\rho_{\rm anchored}$ (capacitive)", zorder=3)
    if r["saturated"] and r["onset_omega_s"] is not None:
        ax.axvspan(r["onset_omega_s"], os.max(), color=COLORS["muted"], alpha=0.13,
                   zorder=0, label="free-control saturation zone\n(excess axis BLIND)")
        ax.axvline(r["onset_omega_s"], color=COLORS["muted"], lw=1.0, ls=":")
    ax.set_xlabel(axis_label(r"Poloidal detune", r"\omega_s", ""))
    ax.set_ylabel(axis_label(r"Rotation number", r"\rho", ""))
    ax.set_title(f"Fresh 29-pt sweep — BANKED: {res['verdict']}\n"
                 f"(non-sat window, excess axis frozen a priori)", fontsize=10)
    ax.legend(loc="upper right", fontsize=7.5, framealpha=0.9)
    _annot = (f"banked excess_staircase = {r['banked_excess_staircase']:.4f}\n"
              f"banked track_R² = {r['banked_track_R2']:.4f}\n"
              f"TRACK iff R²≥0.9 ∧ excess<0.2")
    ax.text(0.03, 0.05, _annot, transform=ax.transAxes, fontsize=7.5,
            va="bottom", ha="left",
            bbox=dict(boxstyle="round", fc="white", ec=COLORS["muted"], alpha=0.9))

    # ── panel 2: tracking-zone separation (planted staircase vs line) ────────
    ax = axes[1]
    osv = np.linspace(0.70, 1.40, 15)
    ax.plot(osv, _planted_locked(osv), "s-", color=COLORS["ave"], ms=4,
            label="planted LOCK (staircase)")
    ax.plot(osv, _planted_tracking(osv), "o-", color=COLORS["comparison"], ms=4,
            label="planted TRACK (line)")
    vsep = res["planted_violation_proofs"]["detector_separation"]
    ax.set_xlabel(axis_label(r"Poloidal detune", r"\omega_s", ""))
    ax.set_ylabel(axis_label(r"Rotation number", r"\rho", ""))
    ax.set_title("Gate (a): tracking-zone separation\n"
                 f"staircase→{vsep['planted_staircase_verdict']}, "
                 f"line→{vsep['planted_line_verdict']}", fontsize=10)
    ax.legend(loc="upper right", fontsize=8, framealpha=0.9)

    # ── panel 3: saturation-zone disclosure (excess LOCK-suppressed) ─────────
    ax = axes[2]
    ax.plot(osv, _planted_saturating_free(osv), "o-", color=COLORS["comparison"], ms=4,
            label=r"free control (saturates)")
    ax.plot(osv, _planted_lock_in_saturation(osv), "s-", color=COLORS["ave"], ms=4,
            label="genuine lock in sat. zone")
    ax.axvspan(1.0, 1.40, color=COLORS["muted"], alpha=0.13, zorder=0)
    vdisc = res["planted_violation_proofs"]["saturation_disclosure"]
    ax.set_xlabel(axis_label(r"Poloidal detune", r"\omega_s", ""))
    ax.set_ylabel(axis_label(r"Rotation number", r"\rho", ""))
    ax.set_title("Gate (b): saturation disclosure (a priori)\n"
                 f"absolute→{vdisc['absolute_verdict']}, "
                 f"excess→{vdisc['excess_verdict']} (suppressed)", fontsize=10)
    ax.legend(loc="lower left", fontsize=8, framealpha=0.9)

    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import os as _os

    print("TETHERED-PIVOT RE-RUN (x34b) — control-subtracted excess detector FROZEN a priori")
    print("=" * 82)
    res = run_x34b()

    r = res["fresh_leg"]["restricted"]
    print("REPRODUCTION LEG (#612 config):")
    for k, c in res["reproduction_leg"]["comparison_to_612"].items():
        print(f"  {k:24s} x34b={c['x34b']:.4f}  #612={c['x34_#612']:.4f}  "
              f"Δ={c['abs_diff']:.4f}")
    print(f"  reproduces #612: {res['reproduction_leg']['reproduces_612']}")
    print("-" * 82)
    print("FRESH LEG (29-pt refined grid) — FROZEN EXCESS AXIS (single axis):")
    print(f"  saturation onset at ω_s = {r['onset_omega_s']} (i_sat={r['i_sat']}, "
          f"saturated={r['saturated']})")
    print(f"  non-saturated window: {r['nonsat_n_points']} pts")
    print(f"  BANKED excess_staircase={r['banked_excess_staircase']:.4f} "
          f"track_R²={r['banked_track_R2']:.4f} excess_jumps={r['banked_excess_jumps']}")
    print(f"  full-sweep excess verdict (companion): {r['full_sweep_excess_verdict']} "
          f"(excess_staircase={r['full_sweep_excess_staircase']:.4f})")
    print(f"  saturation-zone ABSOLUTE disclosure: {r['full_sweep_absolute_verdict']} "
          f"(staircase={r['full_sweep_absolute_staircase']:.4f} vs "
          f"free {r['full_sweep_free_staircase']:.4f}, both confounded-flat)")
    print("-" * 82)
    p = res["planted_violation_proofs"]
    print(f"PLANTED-VIOLATION PROOFS: all_gates_catch_violations="
          f"{p['all_gates_catch_violations']}")
    for gate in ("detector_separation", "saturation_disclosure",
                 "dead_actuator", "energy_non_pumping"):
        print(f"  {gate:22s} catches_violation={p[gate]['catches_violation']}")
    print("=" * 82)
    print(f"BANKED VERDICT (single frozen excess axis): {res['verdict']}")
    print(f"REASON: {res['reason']}")

    # emit artifacts next to the driver output dir (research/)
    here = _os.path.dirname(_os.path.abspath(__file__))
    root = _os.path.abspath(_os.path.join(here, "..", "..", ".."))
    json_path = _os.path.join(root, "research", "2026-07-10_tethered-pivot-rerun_result.json")
    fig_dir = _os.path.join(root, "research", "figures", "2026-07-10-tethered-pivot-rerun")
    _os.makedirs(fig_dir, exist_ok=True)
    fig_path = _os.path.join(fig_dir, "x34b_frozen_excess_axis.png")
    emit_json(res, json_path)
    emit_figure(res, fig_path)
    print(f"wrote {json_path}")
    print(f"wrote {fig_path}")
