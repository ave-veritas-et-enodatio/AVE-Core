"""S3 cavity-pinning — VALIDATION GATES + the committed-verdict result gate.

FROZEN PRE-REG: research/2026-06-24_engine-s3-cavity-pinning_prereg.md (0b5691cd).
RESULT DOC    : research/2026-06-24_engine-s3-cavity-pinning_result.md.

These tests bind the S3 instrument (the coupled real-space A1↔ω PDE on the native
K4 stencil) and the FROZEN make-or-break verdict:

  T1  OPERATOR VALIDITY (HALT GATE 1): the coupled generator H is Hermitian AND
      its A1-block reproduces the VALIDATED Stage-2 native operator (the spatial
      op is unchanged; only the ω DOF + H_couple are added).
  T2  ENERGY CONSERVATION (HALT GATE 2, the hero): the COUPLED object conserves
      energy on a CLOSED box (NO PML, NO damping) to |rel_drift| ≤ 1e-5 — the
      rigor guard against damping-bought localization (pre-reg §3 trap 1).
  T3  GENESIS-24 BOTH-CONSERVED: ω is its OWN DOF (never grad(V)); BOTH the joint
      energy AND the ω-winding integer (3,2) are separately certified conserved
      over the winding-ON run (a "pin" bought by bleeding ω into A1 would fail).
  T4  WINDING-OFF REPRODUCES MODE-III (the HERO-CANARY, fast window): A1-alone
      (Ω≡0) sheds its core in this harness — the live negative control the DELTA
      is measured against.
  T5  DISPERSIVE-VECTOR ω UNWINDS (the documented winding-NOT-conserved control):
      a free analytic-signal vector ω smears the winding integer — proving the
      rigid-template (winding-conserved) representation is load-bearing.
  T6  α-CLEAN: the coupled solver carries NO α-carrier on the chord-deciding path
      (κ̃=6/5 via the winding host; θ_χ=2π·ν_vac; the import-time guard triad).
  T7  COMMITTED VERDICT: the frozen result JSON records DISPERSE-FALSIFIED with
      the full immune system green (the result gate — CI cannot silently flip it).

The full make-or-break (sech+gaussian × winding ON/OFF, N=24, 600 steps) is the
HEADLINE run (ave.core.s3_cavity_pinning_gate.run_s3_gate) — too heavy for CI;
its disposition is pinned by T7 against the committed JSON.
"""

import json
from pathlib import Path

import numpy as np
import pytest

from ave.core.s3_cavity_pinning_gate import (
    ENERGY_DRIFT_TOL,
    genesis24_both_conserved,
    halt_gate_1_operator_validity,
    halt_gate_2_energy_conservation,
    run_coupled,
)
from ave.solvers.coupled_cage_winding import (
    KAPPA_TILDE,
    THETA_CHI,
    CoupledCageWinding,
    CoupledCageWindingConfig,
)


# ── T1: operator validity (HALT GATE 1) ──
def test_T1_operator_validity_hermitian_and_native_op():
    g = halt_gate_1_operator_validity()
    assert g["H_hermitian"], f"coupled generator must be Hermitian, asym={g['H_hermitian_asym']:.2e}"
    assert g["A1_block_matches_native"], (
        f"A1-block must reproduce the Stage-2 native operator, "
        f"err={g['A1_block_matches_native_op_err']:.2e}"
    )


# ── T2: energy conservation on the COUPLED object (HALT GATE 2, the hero) ──
def test_T2_energy_conservation_coupled_closed_box():
    """The COUPLED object conserves energy on a CLOSED box (no PML, no damping):
    |rel_drift| ≤ 1e-5. A FAIL means the verdict could be damping-bought (the top
    trap). Run on a small box for CI speed (the production N=24 drift is in the
    committed JSON / result doc)."""
    r = run_coupled(N=16, winding_on=True, seed="sech", n_total=120, n_transient=40)
    assert abs(r["rel_drift_max"]) <= ENERGY_DRIFT_TOL, (
        f"COUPLED energy not conserved: |rel_drift_max|={r['rel_drift_max']:.2e} "
        f"> {ENERGY_DRIFT_TOL:.0e} — damping-bought-localization risk (HALT)."
    )
    assert r["last_gmres_info"] == 0, "GMRES did not converge"


# ── T3: genesis-24 BOTH-conserved (energy AND winding integer) ──
def test_T3_genesis24_both_conserved():
    """ω is its OWN DOF (never grad(V)); BOTH the joint energy AND the ω-winding
    integer (3,2) are separately conserved over the winding-ON run. A pin bought
    by bleeding ω into A1 would break the winding-integer conservation."""
    on = run_coupled(N=24, winding_on=True, seed="sech", n_total=240, n_transient=80)
    g = genesis24_both_conserved(on)
    assert g["energy_conserved"], f"energy not conserved: {g['rel_drift_max']:.2e}"
    assert g["winding_integer_conserved"], (
        f"ω-winding integer NOT conserved (genesis-24 bleed): {g['winding_history']}"
    )
    assert g["both_conserved"]


# ── T4: winding-OFF reproduces Mode-III in-harness (the HERO-CANARY) ──
def test_T4_winding_off_disperses_in_harness():
    """A1-alone (winding OFF, Ω≡0) sheds its core in this harness — the live
    negative control the DELTA is measured against. Over the production window the
    interior peak → seed then sheds below the radiation floor and the spread
    grows (the committed JSON has the full N=24/600-step numbers; here a sufficient
    window to see the shed direction)."""
    off = run_coupled(N=24, winding_on=False, seed="sech", n_total=400, n_transient=120)
    assert off["spread_end"] > off["spread0"] * 1.10, (
        f"winding-OFF spread must GROW (disperse): {off['spread0']:.2f}→{off['spread_end']:.2f}"
    )
    assert off["ie_end"] < off["ie0"], (
        f"winding-OFF interior energy must DRAIN: {off['ie0']:.1f}→{off['ie_end']:.1f}"
    )


# ── T5: dispersive-vector ω UNWINDS (the winding-NOT-conserved control) ──
def test_T5_dispersive_vector_omega_unwinds():
    """A free analytic-signal vector ω (dispersive_vector mode) smears the winding
    integer (it does NOT represent S1's topological conservation) — the documented
    control proving the rigid-template (winding-conserved) representation is
    load-bearing. The winding integer must DEPART from (3,2)."""
    dv = run_coupled(N=24, winding_on=True, seed="sech", winding_mode="dispersive_vector",
                     n_total=300, n_transient=100)
    assert not dv["winding_conserved"], (
        f"dispersive_vector ω must UNWIND (control): history {dv['winding_history']}"
    )


# ── T6: α-clean (the chord-deciding path carries no α-carrier) ──
def test_T6_coupled_solver_alpha_clean():
    """κ̃=6/5 (NOT α·κ̃), θ_χ=2π·ν_vac, and NO forbidden α-carrier is a bound name
    in the coupled solver module globals."""
    assert KAPPA_TILDE == 6.0 / 5.0, f"κ̃ must be 6/5 (α-free), got {KAPPA_TILDE}"
    assert np.isclose(THETA_CHI, 2.0 * np.pi * (2.0 / 7.0))
    assert not (117.0 < KAPPA_TILDE < 157.0), "κ̃ must not land in the α⁻¹ band"
    import ave.solvers.coupled_cage_winding as M
    forbidden = ("ALPHA", "Q_TANK", "ELECTRON", "V_SNAP", "KAPPA_CHIRAL_ELECTRON",
                 "ALPHA_COLD_INV", "RHO_BULK")
    leaked = [s for s in forbidden if s in vars(M)]
    assert not leaked, f"α-leak: forbidden symbol(s) {leaked} bound in the coupled solver globals"


# ── T7: the committed verdict (the result gate — CI cannot silently flip it) ──
def test_T7_committed_verdict_disperse_falsified():
    """The frozen result JSON records DISPERSE-FALSIFIED with the full immune
    system green. Pins the disposition against silent flips."""
    p = Path(__file__).resolve().parents[2] / "results" / "engine_s3_cavity_pinning_results.json"
    if not p.exists():
        pytest.skip("results JSON not present (run ave.core.s3_cavity_pinning_gate.main)")
    res = json.loads(p.read_text())
    assert res["verdict"] == "DISPERSE-FALSIFIED", f"committed verdict changed: {res['verdict']}"
    imm = res["immune_system"]
    assert imm["winding_off_disperses_modeIII"]
    assert imm["energy_gate_passed"]
    assert imm["both_conserved_A1_and_winding"]
    assert imm["slaved_arm_independence_false"]
    assert imm["negative_controls_fired"]
    assert res["seed_robust"]
    # the DELTA failed on the localization (spread) bins, not on instrument bins.
    assert res["primary_delta_sech"]["verdict"] == "DISPERSE"
    assert res["primary_delta_gaussian"]["verdict"] == "DISPERSE"


# ── structural: rigid-template winding is conserved by construction (sanity) ──
def test_winding_conserved_rigid_template_uncoupled():
    """rigid_template ω with NO coupling (winding_on but A1=0 ⇒ Ω=0) keeps the
    (2,3) winding integer (read off the quadrature-invariant |b_ω|·ê_w) — the
    S1-faithful separately-conserved DOF."""
    cfg = CoupledCageWindingConfig(N=24, winding_on=True, winding_mode="rigid_template")
    eng = CoupledCageWinding(cfg)
    eng.seed_winding()  # A1 stays 0 ⇒ Ω≡0 ⇒ ω evolves alone
    assert (eng.winding_integer()["Q_link"], eng.winding_integer()["w_tor"]) == (3, 2)
    for _ in range(200):
        eng.step()
    w = eng.winding_integer()
    assert (w["Q_link"], w["w_tor"]) == (3, 2), f"rigid-template winding must hold (3,2), got {w}"
