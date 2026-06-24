"""S2 — a conservative skew-Hermitian H_couple locking A1↔ω (winding stays independent).

FROZEN PRE-REG: research/2026-06-24_engine-s2-hcouple_prereg.md (commit 38066fd2).
Gate code: src/ave/core/s2_hcouple_gate.py.

S2 make-or-break (pre-reg §Make-or-break): a FIELD-RESOLVED skew-Hermitian H_couple
in the A1↔ω sector pair (A1 bulk-dilatation breather = mass ↔ Cosserat micro-rotation
ω = charge winding), S(A)-gated (FORK A=(a), intra-mechanical, NO TKI transducer),
on the α-clean host. NO existing field-resolved coupling in that exact pair (ADD-2
is V↔w, the WRONG pair — recovering it does NOT count).

════════════════════════════════════════════════════════════════════════════════
S2 FROZEN-BIN OUTCOMES (BRUTAL HONESTY — Rule 11; the four make-or-break criteria)
════════════════════════════════════════════════════════════════════════════════
  (1) CONSERVATION   PASS — joint H=E_A1+E_ω+H_couple drifts |dH/H|≈4.7e-11 ≪ 1e-8
                     over a 40k-step CLOSED-system window (no loss port — T2 guard);
                     late pump-slope ≈3e-14. The generator is skew-Hermitian.
  (2) NON-VACUITY    PASS — A1 loaded / ω EMPTY (0.0), ω fills 83% (42× the failed
                     2% inert arm), oscillates (134 crossings); the |L_ω| pump
                     canary stays BOUNDED (secular ratio 1.02; max 5.7 < ceiling 28).
  (3) INDEPENDENCE   PASS — real arm (2,3)==(2,3) robust under a V-perturbation
                     (FORK B=(b)); the SLAVED arm (ω:=F(V)) returns
                     independence=False (reachable-False, NOT AUTO_VOID). Normal-mode
                     SPLITTING (split=0.6=2Ω) is DECLARED EXPECTED, NOT a violation.
  (4) REDUCED-LIMIT  PASS — H_couple EXACTLY recovers the PR#321 node_circulator
                     2-mode generator (generator + trajectory + Rabi anchor) in its
                     M=1 / hop=0 limit (NOT ADD-2 V↔w).

DUAL CANARY (each leg reachable-FAIL, T6): the |L_ω| pump FIRES on a detonating
non-Hermitian arm (26× vs the bounded real arm — NEVER photon_deplete on the real
arm, T5); the |dH/H| canary FIRES on an open/lossy arm (86% drift vs 3.6e-12 closed).

PASS  = all four criteria + both negative controls fire + α-clean + skew-Hermitian.
FAIL  = any criterion fails; OR a PASS no negative control can break; OR the slaved
        arm is NOT reachable-False (AUTO_VOID).
INCONCLUSIVE = the integrator cannot carry the dynamics to a clean verdict
        (non-finite drift/transfer). Report, do NOT rescue (Rule 11).

SCOPE CAVEATS (pre-reg §Scope-lock): CONSISTENCY-class, NOT the α-free chord (the
chord-decider is S4); the Q=137 slot stays EMPTY. S2 does NOT test confinement (S3),
boundary observables (S4), or the non-reciprocity MAGNITUDE (corpus-flagged ECHO).
"""

from __future__ import annotations

import numpy as np
import pytest

# Importing the gate executes the α-clean host load-time guard triad (an α-leak on
# the readout path fails HERE). The gate routes the readout through κ̃=6/5 (NO α).
from ave.core import s2_hcouple_gate as S2


# ──────────────────────────────────────────────────────────────────────────────
# FAST STRUCTURAL GATES (default-gating; pure-numpy skew-Hermitian dynamics).
# ──────────────────────────────────────────────────────────────────────────────
def test_s2_alpha_clean_readout_path():
    """α-CLEAN (pre-reg §α-clean discipline): κ̃=6/5 (NOT α·κ̃), θ_χ=2π·ν_vac, no
    α-carrier bound in the gate globals, κ̃ ∉ the 117–157 α⁻¹ landing band. NEVER
    ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK."""
    ac = S2.assert_alpha_clean()
    print("\n[S2 α-clean]", ac)
    assert ac["kappa_is_six_fifths"]
    assert ac["theta_chi_is_2pi_nu_vac"]
    assert ac["no_forbidden_in_globals"]
    g = vars(S2)
    for sym in ("ALPHA", "KAPPA_CHIRAL_ELECTRON", "V_SNAP", "L_NODE", "M_E", "Q_TANK",
                "ALPHA_COLD_INV"):
        assert sym not in g, f"α-leak: '{sym}' must NOT be a bound name in the S2 gate"


def test_s2_skew_hermitian_by_construction():
    """The field-resolved H_couple is skew-Hermitian-by-construction (H Hermitian ⇒
    −iH anti-Hermitian ⇒ e^{-iHt} unitary). This is the load-bearing property that
    forbids the indefinite-trilinear detonation pump (pre-reg T5)."""
    A = np.linspace(0.1, 0.9, 6)
    H = S2.build_hcouple(A, hop_b=0.05, hop_s=0.07, gate="front")
    assert np.allclose(H, H.conj().T), "H_couple must be Hermitian"
    assert S2.is_skew_hermitian_generator(H), "−iH must be anti-Hermitian (skew)"


def test_s2_validate_on_known_node_circulator():
    """VALIDATE-ON-KNOWN floor: the PR#321 node_circulator generator the reduced
    limit recovers is itself sound (Hermitian, unitary, norm-conserving)."""
    vk = S2._validate_node_circulator()
    print("\n[S2 validate-on-known]", vk)
    assert vk["PASS"], f"node_circulator anchor must hold: {vk}"


def test_s2_criterion_4_reduced_limit_recovers_2mode():
    """CRITERION 4 — REDUCED-LIMIT: build_hcouple(M=1, front-center A) EXACTLY equals
    the node_circulator 2-mode generator (generator + trajectory + Rabi anchor). NOT
    ADD-2 (V↔w) — the A1↔ω 2-mode generator (pre-reg WRONG-SECTOR-PAIR guard)."""
    c4 = S2.criterion_4_reduced_limit()
    print("\n[S2 (4) reduced-limit]", c4)
    assert c4["generator_equals_node_circulator"], "reduced generator must == node_circulator"
    assert c4["trajectory_equals_node_circulator"], "reduced trajectory must == node_circulator"
    assert c4["rabi_anchor_match"], "reduced transfer must match the analytic Rabi anchor"
    assert c4["PASS"]


def test_s2_criterion_1_conservation_closed_system():
    """CRITERION 1 — CONSERVATION: |dH/H| < 1e-8 over a closed-system window (no loss
    port — T2 guard; precedent test_l1_photon.py:285). PR#321 target ≈1.1e-12."""
    c1 = S2.criterion_1_conservation(n_steps=20000)
    print("\n[S2 (1) conservation]", c1)
    assert c1["skew_hermitian"], "the generator must be skew-Hermitian"
    assert c1["closed_system"], "the conservation window must be a CLOSED system (no loss port)"
    assert c1["dH_over_H_max"] < S2.CONS_TOL, f"|dH/H| must be < {S2.CONS_TOL}: {c1}"
    assert abs(c1["late_pump_slope_per_step"]) < 1e-12, "no late-time pump slope"
    assert c1["PASS"]


def test_s2_criterion_2_non_vacuity_transfer_and_Lomega_bounded():
    """CRITERION 2 — NON-VACUITY (load-bearing): ω starts EMPTY and fills measurably
    (≫ the 2% inert arm) AND oscillates AND the |L_ω| pump canary stays BOUNDED (no
    secular growth)."""
    c2 = S2.criterion_2_non_vacuity(n_steps=20000)
    print("\n[S2 (2) non-vacuity]", c2)
    assert c2["omega_initial_energy"] < 1e-15, "ω must start EMPTY (transfer = measured flow)"
    assert c2["transfer_fraction"] > S2.TRANSFER_MIN, f"ω must fill ≫ 2%: {c2['transfer_fraction']}"
    assert c2["omega_oscillation_crossings"] >= 1, "ω must oscillate (not a static offset)"
    assert c2["L_omega_bounded"], f"|L_ω| pump must be BOUNDED (no secular growth): {c2}"
    assert c2["transfer_measured"]
    assert c2["PASS"]


def test_s2_negative_control_conservation_fires():
    """DUAL-CANARY (ii) — the |dH/H| conservation canary FIRES on an open/lossy arm
    (T2 guard + T6 reachable-FAIL). The real closed arm conserves; the open arm leaks
    measurably."""
    nc = S2.negative_control_conservation()
    print("\n[S2 neg-ctrl conservation]", nc)
    assert nc["dH_over_H_real_closed"] < S2.CONS_TOL, "real closed arm must conserve"
    assert nc["dH_over_H_open_lossy"] > S2.NEG_CTRL_DH_FLOOR, "open/lossy arm must FIRE |dH/H|"
    assert not nc["open_is_hermitian"], "the lossy arm must be non-Hermitian (anti-Hermitian loss)"
    assert nc["dh_negative_control_fired"]
    assert nc["PASS"]


def test_s2_negative_control_L_omega_pump_fires():
    """DUAL-CANARY (i) — the |L_ω| pump canary FIRES on a detonating non-Hermitian arm
    (the field analogue of photon_deplete=True — NEVER on the real arm, T5). The real
    skew-Hermitian arm keeps |L_ω| bounded; the detonator pumps ≥ NEG_CTRL_PUMP_RATIO×."""
    nc = S2.negative_control_L_omega_pump()
    print("\n[S2 neg-ctrl |L_ω| pump]", nc)
    assert nc["is_skew_real_arm"], "the real arm must be skew-Hermitian"
    assert not nc["is_skew_detonating_arm"], "the detonating arm must be non-Hermitian"
    assert nc["pump_ratio"] >= S2.NEG_CTRL_PUMP_RATIO, f"the |L_ω| pump must FIRE: {nc}"
    assert nc["L_omega_negative_control_fired"]
    assert nc["PASS"]


# ──────────────────────────────────────────────────────────────────────────────
# DYNAMICAL GATE (engine_sim — slow; criterion 3 invokes the REAL CrystalGraftV4).
# ──────────────────────────────────────────────────────────────────────────────
def test_s2_criterion_3_independence_slaved_arm_reachable_false():
    """CRITERION 3 — INDEPENDENCE (FORK B=(b)): the real arm keeps its (2,3) winding
    robust under a V-perturbation while the SLAVED arm (ω:=F(V)) returns
    independence=False (reachable-False, NOT AUTO_VOID) — the EXISTING S1
    discriminator on the real engine (anti-rebuild, Rule 14). Normal-mode SPLITTING
    is EXPECTED + bounded (split=2Ω), explicitly NOT scored as a violation."""
    c3 = S2.criterion_3_independence()
    print("\n[S2 (3) independence]", c3)
    assert not c3["AUTO_VOID"], "the slaved arm MUST be reachable-False (else AUTO-VOID)"
    assert c3["slaved_arm_independence_false"], "the slaved arm must flag independence=False"
    assert c3["real_arm_independent"], "the real arm must keep its winding independent"
    assert c3["split_equals_2Omega_EXPECTED"], "normal-mode split must be the EXPECTED 2Ω"
    assert c3["splitting_is_violation"] is False, "splitting is EXPECTED (FORK B=(b)), NOT a violation"
    assert c3["PASS"]


def test_s2_full_gate_verdict_pass():
    """THE HEADLINE (pre-reg §Make-or-break): all four criteria + both negative
    controls fire + α-clean + skew-Hermitian → verdict PASS, with the immune system
    healthy (slaved_arm_independence_false, both canaries fired, transfer measured,
    real dynamics ran). INCONCLUSIVE / AUTO_VOID / FAIL are surfaced (Rule 11)."""
    out = S2.run_s2_gate()
    print(f"\n[S2 VERDICT] {out['verdict']}  failing={out['failing_criteria']}")
    print(f"  immune: {out['immune_system']}")
    assert out["verdict"] == "PASS", (
        f"S2 verdict={out['verdict']} failing={out['failing_criteria']} "
        f"inconclusive={out['inconclusive_reason']}"
    )
    imm = out["immune_system"]
    assert imm["slaved_arm_independence_false"] is True
    assert imm["dh_negative_control_fired"] is True, "PASS must be non-vacuous (|dH/H| canary fires)"
    assert imm["l_omega_negative_control_fired"] is True, "PASS must be non-vacuous (|L_ω| canary fires)"
    assert imm["transfer_measured"] is True
    assert imm["real_dynamics_ran"] is True
    assert out["skew_hermitian"] is True
    assert out["reduced_limit_recovers_2mode"] is True
    assert out["alpha_clean_flag"] is True
