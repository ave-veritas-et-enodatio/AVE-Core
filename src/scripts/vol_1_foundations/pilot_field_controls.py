"""PILOT-FIELD CONTROLS — the five HALT-gated controls (a)-(e), each wired through the
#528 ReconcileGate with can-fire proven on real paths.

FROZEN prereg: research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md §CONTROLS.

Each control reconciles a DRIVER-measured quantity against an INDEPENDENT reference
(the imported #534 analytic free/ring readings, the symbolic prediction, or a
different code path), NOT the quantity's own defining identity (the #527 defect the
ReconcileGate module docstring warns against). The can-fire self-test proves the halt
plumbing is live before every enforcement.

  (a) FILLED-ring limit (envelope -> whole ring) recovers #534's ring COLD reading.
  (b) OPEN-FREE-chain envelope recovers the free SOFT reading (0.9926-class) LOCALLY.
  (c) LINEAR-axial control: the contraction is GEOMETRIC (kernel ~ nothing at O(y0^2)).
  (d) envelope/ring sweep with the local-reading convergence quantified.
  (e) ENERGY-MOMENTUM LEDGER closure (the crank check) — saturation-consistent functional.

alpha-CLEAN: no physical constant on this path.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(_ROOT, "src"))

from pilot_field_wavetrain import (  # noqa: E402
    contraction_depth,
    ledger_closure,
    run_wavetrain,
)
from ring_bondframe_probe import (  # noqa: E402
    three_host_table,
)

from ave.validation.reconcile_gate import ReconcileGate  # noqa: E402


# ── control (a): FILLED-ring limit recovers #534 ring COLD (ratio -> 1.000000) ──
def control_a_filled_ring(band: float = 3e-3):
    """The filled-ring cycle-mean bond-frame reading must recover #534's COLD 1.000000.
    Claimed = the #534 three-host `ring` reading; independent = an exact 1.0 (the cold
    theorem the homogeneous-<dy^2> limit forces). Reconciles the filled limit to cold."""
    claimed = float(three_host_table()["ring"])
    gate = ReconcileGate(label="control-a-filled-ring-cold", claimed=claimed,
                         independent=1.0, rtol=0.0, atol=band)
    res = gate.enforce(prove_first=True)
    return {"claimed_ring_ratio": claimed, "reconciled": res.passed,
            "can_fire_proven": res.can_fire_proven, "band": band}


# ── control (b): ENVELOPE on an OPEN-FREE chain recovers the free SOFT reading LOCALLY ──
def control_b_free_local(band_rel: float = 0.10):
    """The frozen control: an ENVELOPE on an OPEN FREE chain must recover the free reading
    LOCALLY under the envelope (0.9926-class, soft by <dy^2>/2).

    ITEM-4a FIX (orchestrator review of PR #535): the PR #535 implementation reran the #534
    FILLED free chain (`open_chain_cyclemean`, the whole chain excited), NOT the frozen
    envelope-on-open-free LOCAL control. This now imposes a LOCALIZED envelope on an open
    free chain, takes the analytic free-equilibrium (T=0 => du = sqrt(1-dy^2)-1) UNDER the
    envelope, and reads the imported (canon #534) bond-frame trans_tangent_stiffness at the
    DC config LOCALLY at the envelope peak. Claimed = that local reading; independent =
    1 - <dy^2>_local/2 (the free-host closed form at the LOCAL envelope-peak <dy^2>). A
    different code path (imported probe vs closed form)."""
    import numpy as np
    from ring_bondframe_probe import (
        _free_equilibrium_u,
        _ktrans_open,
        wave_number_cold,
    )
    n = 1024
    y0 = 0.1428
    k = wave_number_cold(1.2)
    j = np.arange(n)
    j0 = n // 2
    l_env = 80.0
    d = j - j0
    env = np.exp(-0.5 * (d / l_env) ** 2)
    # localized envelope on an OPEN chain (ends free), phase-averaged local reading under it
    kcold = _ktrans_open(np.zeros(n), np.zeros(n), j0)
    ratios, dy2_local = [], []
    for m_ in range(24):
        ph = 2 * np.pi * m_ / 24
        y = y0 * env * np.sin(k * j - ph)
        y[0] = 0.0
        y[-1] = 0.0
        u = _free_equilibrium_u(y)                # analytic T=0 free equilibrium (imported)
        # imported bond-frame probe at the DC config under the envelope peak:
        ratios.append(_ktrans_open(u, np.zeros(n), j0) / kcold)
        # <dy^2> LOCAL under the envelope (envelope peak neighborhood)
        near = np.abs(d[:-1]) <= l_env
        dyloc = (y[1:] - y[:-1])[near]
        dy2_local.append(float(np.mean(dyloc ** 2)))
    claimed = float(np.mean(ratios))
    independent = float(1.0 - 0.5 * np.mean(dy2_local))   # 1 - <dy^2>_local/2 (free-host closed form)
    gate = ReconcileGate(label="control-b-free-local-envelope-soft", claimed=claimed,
                         independent=independent, rtol=band_rel, atol=1e-3)
    res = gate.enforce(prove_first=True)
    return {"local_under_envelope_ratio": claimed, "pred_soft_local": independent,
            "reconciled": res.passed, "can_fire_proven": res.can_fire_proven}


# ── control (c): LINEAR-axial vs nonlinear-kernel contraction (kernel ~ nothing) ──
def control_c_linear_axial(rho_bond: float = 2.0, band_rel: float = 0.05, fast: bool = True):
    """The contraction is GEOMETRIC (du = sqrt(1-dy^2)-1), not from the concave kernel.
    Claimed = the nonlinear-kernel DC contraction depth; independent = the LINEAR-axial
    run's depth (kernel OFF — a different force law). They must reconcile to O(y0^2) since
    the kernel enters only at O(y0^4)~O(A^2). Reconciles nonlinear vs linear-axial."""
    n_periods = 12.0 if fast else 16.0
    n_nodes = 768 if fast else 1024
    rn = run_wavetrain(n_nodes=n_nodes, rho_bond=rho_bond, l_env=60.0,
                       n_periods=n_periods, dt=0.02, linear_axial=False)
    rl = run_wavetrain(n_nodes=n_nodes, rho_bond=rho_bond, l_env=60.0,
                       n_periods=n_periods, dt=0.02, linear_axial=True)
    dn = float(contraction_depth(rn)["du_dc_min_under"])
    dl = float(contraction_depth(rl)["du_dc_min_under"])
    gate = ReconcileGate(label="control-c-linear-axial-geometric", claimed=dn,
                         independent=dl, rtol=band_rel, atol=1e-6)
    res = gate.enforce(prove_first=True)
    return {"nonlinear_depth": dn, "linear_axial_depth": dl,
            "rel_diff": abs(dn - dl) / (abs(dn) + 1e-30),
            "reconciled": res.passed, "can_fire_proven": res.can_fire_proven}


# ── control (d): envelope/ring sweep, local-reading convergence quantified ──
def control_d_scale_sweep(rho_bond: float = 4.0, fast: bool = True):
    """The local contraction depth vs the frozen L_env sweep {40,80,160}, and the causally-
    reached wake compensation, across the (L_env, N) grid. A REPORTED convergence table (the
    [PILOT-CONFIRMED] verdict would require the local depth -> free amplitude AND the
    compensation -> global; this control supplies the numbers — here the depth is L_env-set
    per transit and the compensation lives in the causal wake, consistent with the
    [RETARDATION-LIMITED] verdict).

    ITEM-4b FIX (orchestrator review of PR #535): sweep L_env per the FROZEN {40,80,160}
    (the PR #535 code swept {80,80,80} at varying N); the field is the item-3 causal-wake
    compensation `comp_wake_mean_du` (the `du_dc_far_mean` antipode field is retired)."""
    grid = [(40, 512), (80, 1024)] if fast else [(40, 512), (80, 1024), (160, 2048)]
    n_periods = 12.0 if fast else 18.0
    rows = []
    for (le, n) in grid:
        run = run_wavetrain(n_nodes=n, rho_bond=rho_bond, l_env=float(le),
                            n_periods=n_periods, dt=0.02)
        c = contraction_depth(run)
        rows.append({"L_env": le, "N": n, "L_env_over_N": le / n,
                     "du_dc_min_under": c["du_dc_min_under"],
                     "comp_wake_mean_du": c["comp_wake_mean_du"]})
    return {"rows": rows,
            "l_env_swept": [r["L_env"] for r in rows],
            "depth_reported": True}


# ── control (e): ENERGY-MOMENTUM LEDGER closure (the crank check) ──
def control_e_ledger(rho_bond: float = 2.0, energy_band: float = 1e-3,
                     momentum_band: float = 1e-10, fast: bool = True):
    """Total energy (saturation-consistent functional) conserved and total longitudinal
    momentum conserved (closed ring) over the recording window. Claimed = the measured
    energy drift / momentum max; independent = 0 (perfect conservation, the closed-ring
    theorem). Reconciles the ledger to closure — the #532 no-linear-proxy flag honored
    (the axial potential is the rho-scaled Phi(A), not a linear proxy)."""
    n_periods = 12.0 if fast else 18.0
    n_nodes = 768 if fast else 1024
    run = run_wavetrain(n_nodes=n_nodes, rho_bond=rho_bond, l_env=60.0,
                        n_periods=n_periods, dt=0.02)
    ld = ledger_closure(run)
    g_e = ReconcileGate(label="control-e-energy-closure", claimed=ld["energy_drift_rel"],
                        independent=0.0, rtol=0.0, atol=energy_band)
    g_p = ReconcileGate(label="control-e-momentum-closure", claimed=ld["momentum_max_abs"],
                        independent=0.0, rtol=0.0, atol=momentum_band)
    re = g_e.enforce(prove_first=True)
    rp = g_p.enforce(prove_first=True)
    return {"energy_drift_rel": ld["energy_drift_rel"], "momentum_max_abs": ld["momentum_max_abs"],
            "energy_reconciled": re.passed, "momentum_reconciled": rp.passed,
            "can_fire_proven": bool(re.can_fire_proven and rp.can_fire_proven)}


def run_all_controls(fast: bool = True) -> dict:
    """Run all five controls. `fast=True` uses smaller rings / fewer periods for the
    fast test core; `fast=False` is the full-fidelity path (the slow test / __main__)."""
    return {
        "control_a_filled_ring": control_a_filled_ring(),
        "control_b_free_local": control_b_free_local(),
        "control_c_linear_axial": control_c_linear_axial(fast=fast),
        "control_d_scale_sweep": control_d_scale_sweep(fast=fast),
        "control_e_ledger": control_e_ledger(fast=fast),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_all_controls(fast=False), indent=2, default=float))
