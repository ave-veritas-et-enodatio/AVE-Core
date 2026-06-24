"""Coupled A1+winding EIGENSOLVE — validation gates + the committed-verdict gate.

FROZEN PRE-REG: research/2026-06-24_engine-coupled-eigensolve_prereg.md (54d605f8).
RESULT DOC    : research/2026-06-24_engine-coupled-eigensolve_result.md.

The conservative-existence keystone: eigensolve the COUPLED Hermitian generator H
(the SAME operator S3 time-evolved) and ask whether a confined stationary bound
mode carrying BOTH the A1 mass-amplitude AND the (2,3) winding-charge EXISTS. We
report EIGENPAIRS, NOT trajectories (NOT the twice-falsified self-formation slot).

  T0  α-CLEAN (FAST keeper): the chord path carries NO α-carrier (κ̃=6/5 via the
      winding host; the import-time guard triad). Stays in the gating lane.
  T1  HALT GATE: winding-OFF (Ω≡0) recovers the fork-b confined A1 mode
      (core_frac>=0.50, lossless). If not → broken instrument.
  T2  HERMITIAN ⇒ LOSSLESS (gate c): H is Hermitian ⇒ real spectrum ⇒ Im(ω)=0.
  T3  VALIDATE-ON-KNOWN: the SEEDED (2,3) winding reads (2,3) at this geometry
      (resolution ample, ~14.5 cells/turn) — so a winding-absent bound mode is a
      PHYSICS result, NOT a resolution artifact (rules out INCONCLUSIVE).
  T4  GATE (d) FAILS — the both-sectors winding is BLED OUT: the most-bound
      eigenstate's b_ω amplitude co-localizes at the A1 core (bw_on_torus ≈ 0),
      NOT on the winding torus; no bound-cluster member carries the (2,3) winding.
  T5  GATE (e) ARM-B DE-CONFINES: histogram-preserving strain scramble drops
      core_frac (NOT auto-void) — confinement is S-structure-decided.
  T6  COMMITTED VERDICT: the frozen verdict is DOES-NOT-EXIST (gates a/b/c/e pass,
      (d) fails) — the deeper negative (retract-not-refill). CI cannot silently flip.

The N=32 eigensolves (T1/T3/T4/T5/T6) are T2 resolution-dependent drivers ⇒
engine_sim (run via `make test-engine`); T0/T2 are FAST structural keepers in the
gating lane. Partition registered in conftest.py.
"""

from __future__ import annotations

import numpy as np

from ave.solvers.coupled_eigensolve import (
    CoupledEigenConfig,
    halt_gate,
    read_ladder,
    run_coupled_eigensolve,
    solve_arm_b_scramble,
    solve_coupled_spectrum,
)


# ── T0 — α-CLEAN (FAST keeper; gating lane) ──────────────────────────────────
def test_t0_alpha_clean_chord_path():
    """The chord-deciding path carries NO α-carrier (κ̃=6/5 via the winding host)."""
    import ave.solvers.coupled_eigensolve as M

    for sym in ("ALPHA", "Q_TANK", "ELECTRON", "V_SNAP", "KAPPA_CHIRAL_ELECTRON"):
        assert sym not in vars(M), f"α-leak: {sym} reachable on the chord path"
    assert abs(M.KAPPA_TILDE - 6.0 / 5.0) < 1e-12  # the α-free (2,3) factor
    M.assert_winding_host_globals_alpha_clean()


# ── T2 — HERMITIAN ⇒ LOSSLESS (FAST keeper; gating lane) ─────────────────────
def test_t2_operator_hermitian_lossless():
    """H is Hermitian ⇒ real spectrum ⇒ Im(ω)=0 (gate c structural). Small N."""
    from ave.solvers.coupled_eigensolve import _build_seeded_sim

    cfg = CoupledEigenConfig(N=12, pml_thickness=2, R=4.0, r=1.3, a1_radius=3.0)
    sim = _build_seeded_sim(cfg, winding_on=True)
    H = sim._assemble_H()
    assert np.allclose((H - H.getH()).toarray(), 0.0, atol=1e-10), "H must be Hermitian"


# ── T1 — HALT GATE (engine_sim) ──────────────────────────────────────────────
def test_t1_halt_winding_off_recovers_forkb():
    """winding-OFF (Ω≡0) recovers the fork-b confined A1 mode (core_frac>=0.50,
    lossless). The HALT gate — a broken instrument fails HERE."""
    h = halt_gate(CoupledEigenConfig())
    assert h["recovers_forkb"], f"HALT: did not recover fork-b A1 mode: {h}"
    assert h["a1_core_frac"] >= 0.50
    assert h["lossless"]
    # FORM cross-check (NOT a pass condition): near the cold-cage ω_cutoff≈2.87.
    assert h["near_cold_cage_anchor_2p87"], f"forkb_omega={h['forkb_omega']} not near 2.87"


# ── T3 — VALIDATE-ON-KNOWN: the seeded winding reads (2,3) (engine_sim) ───────
def test_t3_seeded_winding_reads_2_3():
    """The SEEDED (2,3) winding reads (2,3) at this geometry (resolution ample) —
    so a winding-ABSENT bound mode is PHYSICS, not a resolution artifact (this is
    what rules out the INCONCLUSIVE branch)."""
    from ave.solvers.coupled_eigensolve import _build_seeded_sim
    from ave.topological.charge_quantization import compute_Q_link

    cfg = CoupledEigenConfig()
    sim = _build_seeded_sim(cfg, winding_on=True)
    q = compute_Q_link(sim.omega_field(), cfg.R, cfg.r)
    assert (int(q["Q_link"]), int(q["w_tor"])) == (3, 2), f"seeded winding != (2,3): {q}"


# ── T4 — GATE (d) FAILS: the winding is bled out of the bound mode (engine_sim) ─
def test_t4_winding_bled_out_of_bound_mode():
    """The most-bound eigenstate carries the A1 mass-amplitude but the (2,3)
    winding is BLED OUT: bw_on_torus ≈ 0 and the winding integer is NOT (2,3). This
    is the gate-(d) failure — the deeper negative."""
    spec = solve_coupled_spectrum(CoupledEigenConfig(), winding_on=True)
    bm = spec["bound_mode"]
    assert bm["a1_core_frac"] >= 0.50, "the A1 mass mode IS confined"
    # gate (d) fails: the winding amplitude is NOT on the torus.
    assert bm["bw_on_torus"] < 0.20, f"expected winding bled out, got {bm['bw_on_torus']}"
    assert (bm["winding_Q_link"], bm["winding_w_tor"]) != (3, 2), \
        "the bound mode does NOT carry the (2,3) winding"


# ── T5 — GATE (e) ARM-B de-confines (engine_sim) ─────────────────────────────
def test_t5_arm_b_deconfines():
    """ARM-B (histogram-preserving strain scramble) DE-CONFINES the mode (NOT
    auto-void) ⇒ confinement is S-structure-decided, not a projector artifact."""
    a = solve_arm_b_scramble(CoupledEigenConfig())
    assert a["armB_histogram_preserved"]
    assert a["armB_deconfines"], f"ARM-B did not de-confine: {a}"
    assert not a["armB_survives_AUTO_VOID"]


# ── T6 — COMMITTED VERDICT (engine_sim) ──────────────────────────────────────
def test_t6_committed_verdict_does_not_exist():
    """The FROZEN verdict: DOES-NOT-EXIST. Gates a/b/c/e PASS; (d) both-sectors
    FAILS (winding bled out). CI cannot silently flip this committed negative."""
    out = run_coupled_eigensolve(CoupledEigenConfig())
    assert out["verdict"] == "DOES-NOT-EXIST", f"verdict drifted: {out['verdict']}"
    g = out["gates"]
    assert g["a_confined"] and g["c_lossless"] and g["e_nontautological"]
    assert not g["d_both_sectors"], "gate (d) must FAIL (the deeper negative)"
    # the ladder: the A1 mass cage binds at A*→1 (the V_snap cap), front at R_II.
    lad = out["ladder"]
    assert lad["A_star_is_at_V_snap_cap"], f"A*={lad['A_star_core']} not at V_snap cap"
    assert not lad["derives_m_e"], "must NOT claim to derive m_e (calibration input)"
    assert out["alpha_clean"]


# ── T7 — LADDER two-camps resolution is present (FAST keeper; gating lane) ────
def test_t7_ladder_two_camps_resolution_present():
    """The ladder readout carries the FORM-vs-calibration map + two-camps
    resolution (the deliverable Grant asked for). FAST (small N)."""
    lad = read_ladder(CoupledEigenConfig(N=16, pml_thickness=3, R=4.0, r=1.3, a1_radius=3.0))
    assert "V_snap_def" in lad and "V_yield_def" in lad
    assert "two_camps_resolution" in lad and len(lad["two_camps_resolution"]) > 50
    assert lad["derives_m_e"] is False
