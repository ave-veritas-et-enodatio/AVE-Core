"""Driver + engine_sim tests for the moving-front freeze-in make-or-break.

Frozen prereg: research/2026-06-30_moving-front-freezein_prereg_FROZEN.md
(SHA-pinned 7b97e76d).

Two arms (Guard 2): bare-EOS (must LOCK/heal) vs memristive-engine (must FREEZE
for fast v_front). Discriminator sweep over Δt_cross/τ_relax (prereg §2.3:
fast→freeze, slow→heal). Real-space ω-defect persistence only (Guard 3).

The heavy full-resolution two-arm + sweep is `run_full()` (called by the
standalone `__main__`, and by the engine_sim harness at reduced resolution). The
non-engine_sim smoke tests below pin the wiring cheaply.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pytest

from ave.core import constants as C
from ave.topological.moving_front_freezein import (
    FrontConfig,
    MovingFrontFreezeIn,
    bare_dispersion_baseline,
    lossless_defect_check,
    seed_omega_defect,
)


# =====================================================================
# Cheap wiring tests (default lane — not engine_sim)
# =====================================================================
def test_front_config_discriminator_direction():
    """The Δt_cross/τ discriminator and mechanism-predicted regime label
    (prereg §2.3): fast (≤1) → FREEZE, slow (>1) → HEAL."""
    fast = FrontConfig(ell_front=2.0, v_front=4.0)
    slow = FrontConfig(ell_front=2.0, v_front=0.25)
    assert fast.dt_cross_over_tau < 1.0 and fast.regime == "FAST→FREEZE"
    assert slow.dt_cross_over_tau > 1.0 and slow.regime == "SLOW→HEAL"


def test_tau_relax_native_is_one():
    """τ_relax = ℓ_node/c = 1 in native units (canonical, ave.core.constants)."""
    assert C.TAU_RELAX_NATIVE == 1.0
    assert abs(C.TAU_RELAX_SI - C.L_NODE / C.C_0) < 1e-30


def test_seed_defect_is_detected():
    """Guard 1 (existence): the seeded real-space ω-defect is topologically
    nontrivial (extract_crossing_count Q0 >= 1) at seeding."""
    from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat

    sim = CoupledK4Cosserat(N=20, pml=0, disable_cosserat_lc_force=True,
                            couple_v_sector=False)
    seed_omega_defect(sim, R_major=5.0, amp=0.6, sigma=2.0)
    assert sim.total_topological_charge() >= 1


# =====================================================================
# engine_sim: Guard 1 (trap-not-create) + bare dispersion baseline
# =====================================================================
@pytest.mark.engine_sim
def test_guard1_lossless_not_front_sourced():
    """Guard 1 / G1: defect exists at seed AND is not front-sourced (energy
    conserved under lossless front-off evolution). PML=0 avoids the PML-absorption
    confound (Rule-10 corollary)."""
    g1 = lossless_defect_check(N=20, pml=0, n_steps=6, R_major=5.0, amp=0.3, sigma=2.0)
    assert g1["Q0"] >= 1
    assert g1["rel_drift"] <= 1e-2
    assert g1["passes_G1"]


# =====================================================================
# The make-or-break driver
# =====================================================================
def run_full(*, N: int = 24, pml: int = 3, n_post_compton: float = 100.0,
             v_fronts: tuple[float, ...] = (0.25, 0.5, 1.0, 2.0, 4.0),
             ell_front: float = 2.0, out_path: str | None = None) -> dict:
    """The two-arm make-or-break + discriminator sweep.

    For each v_front: run arm A (bare) and arm B (memristive); record whether the
    defect persists past the bare-dispersion baseline τ_disperse. The
    pre-registered prediction (prereg §2.3): arm B persistence RISES with v_front
    (Δt_cross falls below τ_relax → FREEZE); arm A never persists past τ_disperse
    (LOCK/heal, Guard 2). The two-arm contrast IS the proof (G4).
    """
    t_start = time.time()
    seed_kw = dict(R_major=min(6.0, 0.30 * N), amp=0.3, sigma=2.5)

    disp = bare_dispersion_baseline(N=N, pml=pml, n_steps=40, **seed_kw)
    tau_disperse = disp["tau_disperse_compton"]

    sweep = []
    for v in v_fronts:
        cfg = FrontConfig(N=N, pml=pml, ell_front=ell_front, v_front=v,
                          x0_frac=0.12, r_ahead=1.2, r_behind=0.3,
                          n_post_compton=n_post_compton)
        row = {
            "v_front": v,
            "dt_cross_over_tau": cfg.dt_cross_over_tau,
            "regime_predicted": cfg.regime,
        }
        for arm in ("bare", "memristive"):
            mf = MovingFrontFreezeIn(cfg, arm=arm, seed_kw=seed_kw)
            res = mf.run()
            row[f"{arm}_Q_pre"] = res.Q_pre
            row[f"{arm}_Q_end"] = res.Q_end
            row[f"{arm}_persist_compton"] = res.persisted_compton
            row[f"{arm}_beats_dispersion"] = bool(
                res.persisted_compton > max(tau_disperse, 1e-9) * 1.5
            )
            row[f"{arm}_S_at_defect_min"] = (
                float(min(res.S_min_at_defect)) if res.S_min_at_defect else None
            )
        sweep.append(row)

    # Adjudication against the pre-registered gates.
    bare_ever_freezes = any(r["bare_beats_dispersion"] for r in sweep)
    memr_fast = [r for r in sweep if r["dt_cross_over_tau"] <= 1.0]
    memr_slow = [r for r in sweep if r["dt_cross_over_tau"] > 1.0]
    memr_fast_freezes = any(r["memristive_beats_dispersion"] for r in memr_fast)
    memr_slow_heals = all(
        not r["memristive_beats_dispersion"] for r in memr_slow
    ) if memr_slow else None
    # G5: persistence monotone-increasing with v_front (freeze-fraction sense).
    persist_by_v = [(r["v_front"], r["memristive_persist_compton"]) for r in sweep]
    persist_sorted = [p for _, p in sorted(persist_by_v)]
    monotone_up = all(
        persist_sorted[i] <= persist_sorted[i + 1] + 1e-9
        for i in range(len(persist_sorted) - 1)
    )

    result = {
        "prereg": "research/2026-06-30_moving-front-freezein_prereg_FROZEN.md",
        "grid_N": N,
        "pml": pml,
        "tau_disperse_compton": tau_disperse,
        "sweep": sweep,
        "adjudication": {
            # G2 (arm A LOCK): bare never persists past dispersion.
            "G2_bare_locks": (not bare_ever_freezes),
            # G3 (arm B FREEZE fast): memristive freezes for fast v_front.
            "G3_memristive_freezes_fast": memr_fast_freezes,
            # slow arm heals (mechanism direction check).
            "memristive_slow_heals": memr_slow_heals,
            # G4: two-arm contrast (freeze in B AND absence in A).
            "G4_two_arm_contrast": (memr_fast_freezes and not bare_ever_freezes),
            # G5: monotone persistence vs v_front (freeze-direction §2.3).
            "G5_monotone_freeze_direction": monotone_up,
        },
        "runtime_s": time.time() - t_start,
    }
    if out_path:
        Path(out_path).write_text(json.dumps(result, indent=2))
    return result


@pytest.mark.engine_sim
def test_moving_front_two_arm_reduced():
    """Reduced-resolution two-arm make-or-break for the harness. Asserts only the
    WIRING invariants that must hold at any resolution (not the full-res physics
    verdict, which the standalone run + result doc adjudicate):
      - both arms run end-to-end and read a real-space winding;
      - the memristive arm's lagged S floors ABOVE the bare arm's (lag active).
    The full-res physics verdict lives in the result JSON / result doc."""
    out = run_full(N=16, pml=3, n_post_compton=2.0, v_fronts=(0.5, 4.0),
                   ell_front=2.0)
    assert len(out["sweep"]) == 2
    for row in out["sweep"]:
        assert row["bare_Q_pre"] >= 1 and row["memristive_Q_pre"] >= 1
        # Memristive lag active: floors S above bare's full-collapse (0).
        assert row["memristive_S_at_defect_min"] >= row["bare_S_at_defect_min"]


if __name__ == "__main__":
    import os

    N = int(os.environ.get("FREEZEIN_N", "24"))
    npc = float(os.environ.get("FREEZEIN_NPOST", "100"))
    out = os.environ.get(
        "FREEZEIN_OUT",
        "research/2026-06-30_moving-front-freezein_results.json",
    )
    res = run_full(N=N, pml=3, n_post_compton=npc, out_path=out)
    print(json.dumps(res["adjudication"], indent=2))
    print(f"tau_disperse={res['tau_disperse_compton']:.3f} Cp  runtime={res['runtime_s']:.1f}s")
    for r in res["sweep"]:
        print(f"  v={r['v_front']:.2f} dtc/tau={r['dt_cross_over_tau']:.2f} "
              f"[{r['regime_predicted']}] bareQ={r['bare_Q_end']} "
              f"memrQ={r['memristive_Q_end']} "
              f"memr_persist={r['memristive_persist_compton']:.2f}Cp "
              f"beats_disp={r['memristive_beats_dispersion']}")
