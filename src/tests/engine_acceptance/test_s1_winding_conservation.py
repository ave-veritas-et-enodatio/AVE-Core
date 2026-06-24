"""S1 — the (2,3) winding as a separately-conserved DOF: the DYNAMICAL GATE.

FROZEN PRE-REG: research/2026-06-24_engine-s1-winding-dof_prereg.md (commit bed0b2d3).
Gate code: src/ave/core/s1_winding_conservation_gate.py.

S1 make-or-break (pre-reg §3 SUB-CLAIM A): single-knot (2,3)-winding conservation
under the engine's ACTUAL `step()` (NOT static `deform_continuous`) + a LOCAL
winding-current continuity law. Two-soliton TRANSFER is DEFERRED (§3 (d), §6).

════════════════════════════════════════════════════════════════════════════════
S1 FROZEN-BIN OUTCOMES (BRUTAL HONESTY — Rule 11; reads from the EVOLVED field)
════════════════════════════════════════════════════════════════════════════════
The pre-stated falsifier (pre-reg §3) is ALL of (a)-(c),(e),(f) + validate-on-known
+ α-clean. Empirically (this run, N=48 R=11 r=4, the LC-quadrature breathing knot):

  (a) NON-VACUITY              PASS — ω evolved under its OWN wave eq (own π_ω
                              momentum; max|Δω|≈0.51 over 400 steps); not frozen.
  (b) KNOWN-SIGNAL RECOVERY   PASS — compute_Q_link reads Q_link=3 (poloidal),
                              w_tor=2 (toroidal) on the seeded canonical (2,3).
  (c) CONSERVATION + CONTINUITY PASS — the winding INTEGER (2,3) held across the
                              whole trajectory on the RAW float read; alias_frac=0.0
                              ≤ 0.34; the lock conserves H_bel EXACTLY (drift=0.0);
                              local continuity ∂_t W = src+flux closes (rel≈0.04);
                              8.4 cells/turn ≥ 3-4 (resolution held throughout).
  (e) LIVE NEGATIVE CONTROL   FIRES — the lock-OFF arm pumps |L_ω| 9.5× (the v3
                              t^0.43 runaway) AND the unwind breaks the integer
                              3→0. The conservation PASS is NOT vacuous.
  (f) GENESIS-24 POS-CONTROL  PASS — the slaved_omega arm (ω:=F(V)) returns
                              independence=False (reachable-False PROVEN; the
                              gate is NOT AUTO-VOID). The real arm is independent
                              ((2,3)==(2,3) under a V-perturbation, fields coupled).

PASS  = all of (a)-(c),(e),(f) hold, validate-on-known floor met, readout α-clean,
        the negative control FIRES (non-vacuous), the slaved arm is reachable-False.
        → "A1-sustains-rotation" upgrades asserted-CLASS → derived-REAL for the
        declared real-space ω coordinate + single-knot conservation ONLY.
FAIL  = any sub-gate fails; OR a PASS the negative control cannot break; OR a PASS
        on the snapped int that fails on the raw float.
INCONCLUSIVE = the integrator cannot carry the dynamics to a clean verdict
        (detonation / alias saturation / NaN continuity). Report, do NOT rescue
        (Rule 11; the Stage-2 precedent).

SCOPE CAVEATS (pre-reg §8): CONSISTENCY-class, NOT the α-free chord (S4); the
Q=137 slot stays EMPTY. mass=A1 (PR#260) UNTOUCHED. No two-soliton transfer.

CLASSIFICATION (consistency-vs-emergence): CONSISTENCY. The α-clean readout +
the immune-system controls ARE the discipline; no emergence headline, no
α-readout, no Q-derivation.
"""

from __future__ import annotations

import numpy as np
import pytest

# Importing the gate executes the α-clean host load-time guard triad (an α-leak
# on the readout path fails HERE). The gate itself imports ONLY α-free symbols.
from ave.core import s1_winding_conservation_gate as S1

N, R, r = 48, 11.0, 4.0


# ──────────────────────────────────────────────────────────────────────────────
# FAST STRUCTURAL GATES (default-gating; no heavy evolution).
# ──────────────────────────────────────────────────────────────────────────────
def test_s1_alpha_clean_readout_path():
    """α-CLEAN (pre-reg §0, §5 trap 8): the readout path carries κ̃=6/5 (NOT α·κ̃),
    the host globals carry NO α-carrier, no '137'/'0.00729' literal, κ̃ ∉ 117-157.
    NEVER ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK."""
    S1.HOST.assert_winding_host_globals_alpha_clean()
    S1.HOST.assert_no_alpha_literal_in_chord_path()
    S1.HOST.assert_not_in_landing_zone(S1._KAPPA_TILDE, "S1 winding κ̃")
    assert S1._KAPPA_TILDE == pytest.approx(6.0 / 5.0)
    g = vars(S1)
    for sym in ("ALPHA", "KAPPA_CHIRAL_ELECTRON", "V_SNAP", "L_NODE", "M_E", "Q_TANK",
                "ALPHA_COLD_INV"):
        assert sym not in g, f"α-leak: '{sym}' must NOT be a bound name in the S1 gate"
    print("\n[S1 α-clean] κ̃ =", S1._KAPPA_TILDE, "(=6/5, α-FREE); no α-carrier on the readout path.")


def test_s1_b_validate_on_known_floor():
    """(b) KNOWN-SIGNAL + §4 PRIMARY validate-on-known floor: compute_Q_link reads
    Q_link=3 (poloidal) and w_tor=2 (toroidal) on a seeded canonical (2,3); the
    ω≡0 null reads 0. 'An extractor that cannot see a known-imposed (2,3) cannot
    certify its absence.'"""
    vk = S1.validate_on_known()
    print("\n[S1 (b)/validate-on-known]", vk)
    assert vk["known_positive_recovers_2_3"], f"compute_Q_link must read (2,3): {vk}"
    assert vk["known_negative_null_is_zero"], f"null must read 0: {vk}"
    assert vk["Q_link_poloidal"] == 3 and vk["w_tor_toroidal"] == 2


def test_s1_e_negative_control_unwind_breaks_integer():
    """(e) NEGATIVE CONTROL, fast path: the topology-CHANGING unwind of a planted
    SPATIAL-PHASE (2,3) (compute_Q_link's coordinate) must JUMP the integer 3→0.
    A conservation claim is vacuous if the readout cannot register a destroyed
    winding (the readout is not an amplitude artifact)."""
    from ave.topological.charge_quantization import seed_pq_winding, unwind_topology, compute_Q_link
    om = seed_pq_winding(N, 2, 3, R, r)
    q_wound = compute_Q_link(om, R, r)
    q_unwound = compute_Q_link(unwind_topology(om, R, r), R, r)
    print(f"\n[S1 (e) unwind] Q_wound={q_wound['Q_link']} -> Q_unwound={q_unwound['Q_link']}")
    assert q_wound["Q_link"] == 3, "the planted spatial-phase (2,3) must read 3 first"
    assert q_unwound["Q_link"] == 0, "unwinding the topology must JUMP the integer to 0 (readout is topological)"


def test_s1_frozen_limit_reproduces_integer():
    """§8.3 FROZEN LIMIT: with NO evolution the dynamical LC read reproduces the
    static (2,3) integer (the bridge between the §4 static floor and the §3(c)
    dynamical conservation)."""
    e = S1._build_isolated_knot(N, R, r, lock_on=True)
    w = S1._read_winding_lc(e, R, r)
    print(f"\n[S1 frozen-limit] (w_tor,w_pol)=({w['w_tor']},{w['w_pol']}) is_2_3={w['is_2_3']}")
    assert (w["w_tor"], w["w_pol"]) == (2, 3), "frozen-limit LC read must reproduce (2,3)"


# ──────────────────────────────────────────────────────────────────────────────
# DYNAMICAL GATES (engine_sim — slow; the make-or-break under genuine step()).
# ──────────────────────────────────────────────────────────────────────────────
@pytest.mark.engine_sim
def test_s1_a_non_vacuity_real_dynamics_ran():
    """(a) NON-VACUITY (pre-reg §3(a), §5 trap 1): ω genuinely evolved under its
    OWN wave eq with its OWN momentum (real_dynamics_ran). Frozen-field
    'conservation' = AUTO-FAIL."""
    a = S1.gate_a_non_vacuity(N, R, r)
    print(f"\n[S1 (a)] real_dynamics_ran={a['real_dynamics_ran']} max|Δω|={a['max_delta_omega']:.4f} "
          f"max|π_ω(0)|={a['max_pi_omega_init']:.4f}")
    assert a["real_dynamics_ran"], f"ω must evolve under its own dynamics (non-vacuity): {a}"
    assert a["PASS"]


@pytest.mark.engine_sim
def test_s1_c_conservation_under_evolution_and_continuity():
    """(c) CONSERVATION-UNDER-EVOLUTION + LOCAL CONTINUITY (pre-reg §3(c)) — the
    S1 make-or-break. The winding INTEGER is conserved on the RETAINED RAW float
    trajectory (alias_frac ≤ 0.34, NOT the snapped int alone); |ΔH_bel|/H_bel
    conserved across the lock substep; ∂_t W = source + flux closes; resolution
    ≥ 3-4 cells/turn held throughout."""
    c = S1.gate_c_conservation_continuity(N, R, r)
    print(f"\n[S1 (c)] reads={c['reads_along_trajectory']} integer_conserved={c['integer_conserved']} "
          f"alias={c['alias_frac_max']} lock_drift={c['lock_helicity_drift_max']:.2e} "
          f"continuity_rel={c['continuity']['rel_residual_window']:.3f} cells/turn={c['cells_per_turn']}")
    assert c["frozen_limit_reads_2_3"], "frozen limit must read (2,3)"
    assert c["integer_conserved"], f"winding integer must be conserved on the raw trajectory: {c['reads_along_trajectory']}"
    assert c["alias_ok"], f"alias_frac {c['alias_frac_max']} must be ≤ {S1.ALIAS_TOL} (raw-float not snapped-int)"
    assert c["lock_conserves_Hbel"], f"the lock must conserve H_bel (drift={c['lock_helicity_drift_max']:.2e})"
    assert c["continuity_closed"], f"local continuity must close: rel={c['continuity']['rel_residual_window']:.3f}"
    assert c["resolution_ok"], f"resolution {c['cells_per_turn']} cells/turn must be ≥ {S1.MIN_CELLS_PER_TURN}"
    assert c["PASS"]


@pytest.mark.engine_sim
def test_s1_e_negative_control_fires_under_evolution():
    """(e) LIVE NEGATIVE CONTROL (pre-reg §3(e), §5 trap 6 — the GX3 analogue): the
    lock-OFF arm MUST pump |L_ω| (≥ NEG_CTRL_PUMP_RATIO×) under genuine evolution
    OR the unwind must break the integer. A conservation PASS the negative control
    cannot break is a FAIL, not a PASS."""
    e = S1.gate_e_negative_control(N, R, r)
    print(f"\n[S1 (e)] |L_ω| lock-ON={e['Lomega_max_lockON']} lock-OFF={e['Lomega_max_lockOFF']} "
          f"ratio={e['pump_ratio']} pump_fires={e['pump_fires']} unwind_breaks={e['unwind_breaks_topology']} "
          f"-> negative_control_fired={e['negative_control_fired']}")
    assert e["negative_control_fired"], f"the negative control MUST fire (else the canary is vacuous): {e}"
    assert e["PASS"]


@pytest.mark.engine_sim
def test_s1_f_positive_control_slaved_arm_independence_false():
    """(f) GENESIS-24 POSITIVE CONTROL (pre-reg §3(f), §5 trap 3): the slaved_omega
    arm (ω:=F(V)) MUST return independence=False (reachable-False). A gate that
    cannot fail on the slaved arm = AUTO-VOID. The REAL arm must be independent."""
    f = S1.gate_f_positive_control(N, R, r)
    print(f"\n[S1 (f)] real={f['real']['w_ref']}=={f['real']['w_pert']}? robust={f['real']['winding_robust']} "
          f"| slaved {f['slaved']['w_ref']} vs {f['slaved']['w_pert']} robust={f['slaved']['winding_robust']} "
          f"-> slaved_arm_independence_false={f['slaved_arm_independence_false']} AUTO_VOID={f['AUTO_VOID']}")
    assert not f["AUTO_VOID"], "the slaved arm MUST be reachable-False (else AUTO-VOID)"
    assert f["slaved_arm_independence_false"], f"the genesis-24 slaved arm must flag independence=False: {f['slaved']}"
    assert f["real_arm_independent"], f"the real arm must be independent: {f['real']}"
    assert f["PASS"]


@pytest.mark.engine_sim
def test_s1_full_gate_verdict_pass():
    """THE HEADLINE (pre-reg §3): all of (a)-(c),(e),(f) + validate-on-known +
    α-clean → verdict PASS, with the immune system healthy (real_dynamics_ran,
    negative_control_fired, slaved_arm_independence_false). INCONCLUSIVE /
    AUTO_VOID / FAIL are surfaced (Rule 11 — no rescue)."""
    out = S1.run_s1_gate(N, R, r)
    print(f"\n[S1 VERDICT] {out['verdict']}  failing={out['failing_gates']}")
    print(f"  immune: {out['immune_system']}")
    assert out["verdict"] == "PASS", (
        f"S1 verdict={out['verdict']} failing={out['failing_gates']} "
        f"inconclusive={out['inconclusive_reason']}"
    )
    imm = out["immune_system"]
    assert imm["real_dynamics_ran"] is True
    assert imm["negative_control_fired"] is True, "PASS must be non-vacuous (neg-control fires)"
    assert imm["slaved_arm_independence_false"] is True, "slaved arm must be reachable-False"
    assert float(imm["alias_frac"]) <= S1.ALIAS_TOL
