"""Tests for the ELECTRON-LOCK RECONNECTION-BARRIER test (pre-reg 2026-07-08).

Time-evolution arms are marked @pytest.mark.engine_sim (research-tier, off the
PR-blocking gate). The fast discipline-gate/classifier units run on the default
gate — they are load-bearing (the classifier + firewall MUST hold before any
verdict is trusted).

VERDICT (committed): ECHO. Even with a genuine, lossless (energy-conserving)
moving-Γ=−1 confinement wall ON and a reconnection-CAPABLE (dispersive_vector)
director, the phase-space (2,3) winding ratio STILL tracks the LC carrier ratio
ω_b:ω_s (correlation-based kill-gate), the real-space winding disperses like the
free control, and there is NO energy barrier against unwinding (the reactive wall
is diagonal and cannot oppose the off-diagonal hopping that smears the director).
Confinement does NOT rescue the topology. Reading B closes NEGATIVE. Per Rule 12
this RETRACTS to "confinement installs no reconnection barrier" — it does NOT walk
back charge=Link(∂Ω,F) nor mass=A1 (#260).
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.solvers.electron_lock_barrier import (
    BarrierConfig,
    ConfinedCageWinding,
    _route_verdict,
    _winding_homotopy_field,
    arm1_liveness,
    bin_liveness,
    build_sim,
    classify_detuning,
    detuning_can_fire,
    evolve_and_trace,
    firewall_ast_scan,
    measure_barrier,
    run_electron_lock_barrier,
)
from ave.solvers.coupled_cage_winding import CoupledCageWindingConfig


# ─────────────────────────────────────────────────────────────────────────────
# FAST UNITS (default gate) — the firewall, the classifier, the routing.
# ─────────────────────────────────────────────────────────────────────────────
def test_firewall_no_alpha_on_verdict_path():
    """AST firewall: NO ALPHA/M_E/m_e NAME token in any verdict-path function."""
    out = firewall_ast_scan()
    assert out["clean"], f"α/m_e leaked onto the verdict path: {out['hits']}"
    assert len(out["scanned"]) >= 10


def test_classifier_reports_tracks_for_carrier_locked():
    """A ratio series that FOLLOWS the carrier (ratio == carrier) must classify
    'tracks' (ECHO) — the #417 signature."""
    carriers = [1.0, 0.667, 1.5, 0.5]
    cls = classify_detuning(carriers, carriers)  # ratio == carrier exactly
    assert cls["classification"] == "tracks"
    assert cls["correlation"] > 0.99


def test_classifier_reports_tracks_even_when_wall_compresses_slope():
    """MASQUERADE-PROOF: a strong wall COMPRESSES the ratio slope (small spread) but
    keeps the carrier-DEPENDENCE (monotonic). This must STILL classify 'tracks',
    not a false 'pinned'."""
    carriers = [1.0, 0.667, 1.5, 0.5]
    compressed = [0.798, 0.780, 0.875, 0.636]  # real wall-ON K=30 data (N=24)
    cls = classify_detuning(compressed, carriers)
    assert cls["classification"] == "tracks", (
        f"wall-compressed but carrier-monotonic ratios misread as {cls['classification']} "
        f"(corr={cls['correlation']:.3f})")


def test_classifier_reports_pinned_for_carrier_invariant():
    """A carrier-INVARIANT (constant) ratio must classify 'pinned' (the topological
    signature) — the gate CAN fire that way."""
    carriers = [1.0, 0.667, 1.5, 0.5]
    cls = classify_detuning([0.667] * 4, carriers)
    assert cls["classification"] == "pinned"
    assert abs(cls["correlation"]) < 0.3


def test_verdict_routing_all_bins_reachable():
    """Each verdict bin must be REACHABLE (bin-liveness): the negative is
    informative, not a dead branch."""
    bl = bin_liveness()
    assert bl["ECHO_reachable"]
    assert bl["PROTECTED_reachable"]
    assert bl["NOT_PROTECTED_reachable"]
    # and the routing is exactly as pre-registered (Arm 3 decisive)
    assert _route_verdict("tracks", True, True) == "ECHO"
    assert _route_verdict("pinned", True, True) == "PROTECTED"
    assert _route_verdict("pinned", False, True) == "NOT-PROTECTED"


def test_wall_is_hermitian_unitary_energy_conserving():
    """The confinement wall is a REAL diagonal ⇒ H Hermitian ⇒ CN/Cayley exactly
    unitary ⇒ the joint norm is conserved (Ax3-lossless: no damping fakes a pin).
    A few steps at tiny N must conserve to ≪1e-5."""
    cfg = CoupledCageWindingConfig(N=12, pml_thickness=3, R=4.0, r=1.6, dt=0.066,
                                   winding_mode="dispersive_vector", winding_on=True)
    sim = ConfinedCageWinding(cfg, clamp_strength=50.0, wall_form="omega_front")
    sim.seed_A1_sech(amplitude=0.60, radius=3.0)
    sim.seed_winding(amplitude=1.0)
    e0 = sim.total_energy()
    for _ in range(20):
        sim.step()
    drift = abs(sim.total_energy() - e0) / e0
    assert drift < 1e-8, f"wall broke unitarity: H-drift={drift:.2e}"
    assert sim.wall_energy() > 0.0, "reactive wall must store energy"


def test_homotopy_endpoints_wound_and_unwound():
    """The barrier homotopy field is the fully-wound (2,3) at λ=0 and the unwound
    (θ≡0, no gradient winding) at λ=1."""
    bc = BarrierConfig(N=16, R=5.0, r=2.0)
    w0 = _winding_homotopy_field(bc, 0.0)
    w1 = _winding_homotopy_field(bc, 1.0)
    # at λ=1 the winding phase θ=0 ⇒ the field points along e0 everywhere it is alive
    amp1 = np.sqrt(np.sum(w1 ** 2, axis=-1))
    alive = amp1 > 1e-9
    # component-1 (sin θ) must be ~0 everywhere unwound; component-0 (cos θ) carries it
    assert np.max(np.abs(w1[..., 1][alive])) < 1e-9
    assert np.max(np.abs(w0[..., 1])) > 1e-3  # the wound field DOES have a sin-θ part


def test_barrier_measure_can_report_protected_synthetically():
    """BIN-LIVENESS: injecting a SYNTHETIC unwound-penalty makes barrier>budget —
    proving the barrier-measure CAN route to PROTECTED (not a dead branch)."""
    bc = BarrierConfig(N=14, R=4.5, r=1.8, a1_radius=3.5, barrier_n_lambda=9)
    out = measure_barrier(bc, wall_form="omega_front", clamp_strength=30.0,
                          budget=1.0, synthetic_barrier=1e6)
    assert out["barrier_gt_budget"], "synthetic barrier failed to route PROTECTED"
    assert out["barrier_height"] > out["budget"]


# ─────────────────────────────────────────────────────────────────────────────
# ENGINE_SIM (research-tier time evolution) — the arms.
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_arm1_liveness_channel_opens():
    """Arm 1: the free (dispersive_vector) director MUST unwind (the reconnection
    channel is open) — else the whole test is vacuous."""
    bc = BarrierConfig(N=16, R=5.0, r=2.0, a1_radius=4.0, n_steps=180, qlink_stride=20)
    a1 = arm1_liveness(bc)
    assert a1["channel_open"], f"reconnection channel did not open (drop {a1['q_raw_drop']:.3f})"
    assert a1["conserved"], f"Arm-1 energy leak H-drift={a1['h_drift']:.2e}"


@pytest.mark.engine_sim
def test_detuning_gate_can_fire_both_ways():
    """The detuning gate CAN report 'tracks' (frozen-template #417 config) AND
    'pinned' (synthetic phase-locked) — it is not rigged to one bin."""
    bc = BarrierConfig(N=16, R=5.0, r=2.0, a1_radius=4.0, detune_steps=120)
    cf = detuning_can_fire(bc)
    assert cf["can_report_tracks"], "gate cannot report 'tracks' on the #417 config"
    assert cf["can_report_pinned"], "gate cannot report 'pinned' on a synthetic pin"


@pytest.mark.engine_sim
def test_wall_does_not_convert_tracking_into_pinning():
    """DECISIVE: turning the confinement wall ON does NOT convert the phase-space
    carrier-tracking (echo) into a topological pin — the rigid #417 read stays
    'tracks' both wall-OFF and wall-ON (the wall only compresses the slope)."""
    bc = BarrierConfig(N=16, R=5.0, r=2.0, a1_radius=4.0, detune_steps=140)
    res = run_electron_lock_barrier(bc)
    if res["verdict"] == "HALT":
        pytest.skip("liveness under-resolved at this reduced N; covered by arm1 test")
    a3 = res["arm3_detuning_killgate"]
    assert a3["rigid_wall_off_reference"]["classification"] == "tracks"
    assert a3["rigid_wall_on"]["classification"] == "tracks"


@pytest.mark.engine_sim
def test_full_driver_routes_echo_not_protected():
    """The full driver, at a reduced but non-vacuous scale, routes to a NEGATIVE bin
    (ECHO or NOT-PROTECTED) with all discipline gates clean — never a spurious
    PROTECTED, and never an energy leak."""
    bc = BarrierConfig(N=16, R=5.0, r=2.0, a1_radius=4.0, n_steps=180,
                       detune_steps=140, qlink_stride=20, barrier_n_lambda=9)
    res = run_electron_lock_barrier(bc)
    assert res["verdict"] in ("ECHO", "NOT-PROTECTED"), f"unexpected verdict {res['verdict']}"
    g = res["gates"]
    assert g["firewall"]["clean"]
    assert g["energy_conservation"]["all_below_1e-5"]
    assert g["scale_invariance"]["scale_invariant"]
    # the barrier must be absent (downhill) — the reactive wall installs no barrier
    assert res["arm4_barrier"]["downhill"]
