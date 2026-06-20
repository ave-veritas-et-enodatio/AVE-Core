"""Fork-B "Saturation-Tank Mass Confinement" gate tests.

Prereg: research/2026-06-20_fork-b-saturation-tank-confinement_prereg.md
Result: research/2026-06-20_fork-b-saturation-tank-confinement_result.md

═══════════════════════════════════════════════════════════════════════════════
THE FROZEN-BIN OUTCOME (BRUTAL HONESTY — Rule 11 honest closure)
═══════════════════════════════════════════════════════════════════════════════
VERDICT = ECHO (the PRE-COMMITTED, EXPECTED, SUCCESSFUL outcome).

  GATE1 (CONFINEMENT, necessary): PASS — the connect-map stiffness operator has a
    gapped, discrete, core-localized (core_frac>=0.50) A1-scalar bound mode; Im(ω)
    sign resolved (bound/lossless branch, convention-anchored).
  GATE2 (SCRAMBLE, anti-tautology): PASS — ARM-A (S->1) AND ARM-B (histogram-
    preserving permutation) BOTH de-confine (margin >= 0.30); the negative control
    is a no-op; ARM-B does NOT survive => NOT a tautology (NOT VOID). HONEST-SCOPE:
    the ARM-B NOT-VOID verdict is PREDOMINANTLY (measured ~94%, pooled srs L4+L6)
    S-structure-decided, NOT a single-seed binary — ~6% of histogram-preserving
    shuffles accidentally re-confine; the rate-sweep test pins it below 0.20.
  GATE3 (QUARTER-ARC SHAPE): shape_gap ~ 0.000 BELOW 10% (generic saturable-NLS;
    the canonical quarter-arc and the norm+depth-matched same-family comparator
    give IDENTICAL Delta/L). Null-control passes (metric reads shape not depth).
  ELECTRON ANCHOR (CHORD-required, NOT expected): NOT reproduced — the connect-map
    bound-mode ω is lattice-band-structure-set (2.70->3.26->3.56, diverging with L),
    NOT a converged universal 2.87.

=> confined + real S-dependent de-confinement BUT shape-generic and no anchor
   => ECHO (FORM-chord/consistency), peer-mapped no-worse-than-SM.

These tests ASSERT the documented ECHO outcome. Re-tuning to force a CHORD would
be debugging-toward-a-rescue (Rule 11 wrong-reaction). A clean ECHO is the honest
discriminating-test result.
"""

import numpy as np
import pytest

from ave.solvers.fork_b_saturation_tank import (
    ConfinementConfig,
    alpha_free_invariance,
    dec5_anti_coincidence,
    electron_anchor_check,
    gamma_from_S_floor,
    norm_match_p,
    run_fork_b_gate,
    scramble_rate_sweep,
    solve_confinement,
    solve_quarter_arc_shape,
    solve_scramble,
    solve_scramble_rate,
)

# ─────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (i): the PR#305 varactor kernel source-of-truth is sound.
# ─────────────────────────────────────────────────────────────────────────────


def test_validate_on_known_varactor_pass():
    """The S(A) kernel source-of-truth (PR#305) returns PASS — the operator the
    Fork-B gate imports its kernel from is sound."""
    from ave.solvers.vacuum_varactor_scatter import varactor_validate_on_known

    assert varactor_validate_on_known()["status"] == "PASS"


# ─────────────────────────────────────────────────────────────────────────────
# GATE 1 — CONFINEMENT (necessary). Pinned outcome: CONFINED.
# ─────────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("net,L", [("diamond", 8), ("srs", 4), ("srs", 6)])
def test_gate1_confined(net, L):
    """GATE1 PASS: a gapped, discrete, core-localized (>=0.50) A1-scalar bound mode
    with the Im(ω) bound-branch resolved."""
    r = solve_confinement(ConfinementConfig(net=net, L=L))
    assert r["ok"]
    assert r["confined"], f"{net} L={L} not confined: {r}"
    assert r["core_frac"] >= 0.50  # RF-1 floor (NOT the live >0.05)
    assert r["discrete"]  # RF-2 spectral-gap + discreteness witness (eigensolve, not FFT)
    assert r["gap_above_sq"] > r["continuum_spacing_sq"]
    assert r["a1_scalar_resident"]  # CP2 sector-projection guard
    assert r["bound_branch_confirmed"]  # RF-3 Im(ω) sign resolved (not assumed)


def test_gate1_im_omega_sign_convention_anchored():
    """RF-3: the Im(ω) sign convention is RESOLVED (anchored by a known port-coupled
    continuum mode that decays, Im<0), NOT assumed. The bound mode is lossless
    (Im~0, not growing)."""
    r = solve_confinement(ConfinementConfig(net="diamond", L=8))
    assert r["convention_decay_is_negative_im"]  # the anchor decays => Im<0 = bound
    assert r["omega_im_open"] <= 1e-6  # bound mode lossless/decaying, NOT growing


def test_gate1_gamma_depth_canonical_floor():
    """RF-3 DEPTH: the binding operator's S_min=1e-3 gives the canonical reachable
    Γ≈−0.94 (near-total short), NOT the scatter's A_cap=0.99 (Γ≈−0.45). gamma_bulk
    convention Γ=(√S−1)/(√S+1)."""
    g = gamma_from_S_floor(1e-3)
    assert -0.95 < g < -0.93, f"Γ at S_min=1e-3 should be ~-0.94, got {g}"
    # a deeper floor binds harder (Γ->-1); a shallow partial short is weaker.
    assert gamma_from_S_floor(1e-6) < g  # deeper floor = harder short


def test_gate1_floor_drop_vs_partial_short():
    """RF-3 DEPTH: report whether a PARTIAL short binds or binding needs floor-
    dropping. At the scatter's shallow A_cap=0.99 floor (S~0.14, Γ~-0.43) the well
    is shallower; at S_min=1e-3 (Γ~-0.94) it is deep. We confirm confinement at the
    canonical deep floor (the binding operator's own floor, NOT floor-dropped to 0)."""
    r = solve_confinement(ConfinementConfig(net="diamond", L=8, S_min=1e-3))
    assert r["confined"], "does NOT bind at the canonical binding-operator floor 1e-3"


# ─────────────────────────────────────────────────────────────────────────────
# GATE 2 — SCRAMBLE (anti-tautology, necessary). Pinned: de-confines, NOT VOID.
# ─────────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("net,L", [("diamond", 8), ("srs", 4), ("srs", 6)])
def test_gate2_scramble_deconfines_not_void(net, L):
    """GATE2 PASS: ARM-A (S->1) AND ARM-B (histogram-preserving permutation) BOTH
    de-confine; the negative control is a no-op; ARM-B does NOT survive => NOT a
    BC/projector tautology (NOT VOID)."""
    r = solve_scramble(ConfinementConfig(net=net, L=L))
    assert r["armA_deconfines"], f"ARM-A did not de-confine: {r}"
    assert r["armB_deconfines"], f"ARM-B did not de-confine: {r}"
    assert r["armB_histogram_preserved"]  # the load-bearing ARM-B invariant
    assert not r["armB_survives_AUTO_VOID"], "ARM-B survived => tautology (VOID)"
    assert r["negative_control_is_noop"]  # permuting a constant field is a no-op
    assert r["deconfines_both_arms"]
    assert not r["auto_void"]


def test_gate2_deconfinement_margin_exceeds_threshold():
    """The de-confinement margin (baseline core_frac − arm core_frac) exceeds the
    frozen 0.30 threshold for BOTH arms."""
    r = solve_scramble(ConfinementConfig(net="diamond", L=8))
    assert r["armA_margin"] >= 0.30
    assert r["armB_margin"] >= 0.30


def test_gate2_armB_predominantly_deconfines_rate_pinned():
    """HONEST-SCOPE DISCLOSURE (CI-protected): the single-seed ARM-B NOT-VOID verdict
    is PREDOMINANTLY S-structure-decided, NOT 100%. Over an N-permutation sweep of
    histogram-preserving shuffles, the measured RE-CONFINE rate (a random shuffle
    accidentally reconstituting a confining core: core_frac>=0.50 AND gapped) is
    pinned BELOW a frozen 0.20 threshold on srs L=4 (the fast verdict net).

    This PROTECTS the 'predominantly de-confines' claim from silently drifting up
    toward a tautology (rate -> 1 would mean ARM-B is BC/projector-decided = VOID).
    The MEASURED rate at the frozen seed is ~0.05 (well below 0.20). alpha-FREE."""
    rr = solve_scramble_rate(ConfinementConfig(net="srs", L=4), n_perm=100, seed=20260620)
    assert rr["ok"]
    assert rr["n_perm"] == 100
    # the load-bearing regression guard: the measured re-confine rate is a MINORITY.
    assert rr["reconfine_rate"] < 0.20, (
        f"ARM-B re-confine rate {rr['reconfine_rate']:.3f} drifted >= 0.20 — the "
        "NOT-VOID verdict is no longer predominantly S-structure-decided (tautology risk)"
    )
    assert rr["predominantly_deconfines"]
    # the binding constraint is core_frac>=0.50 (gapped is ~always satisfied).
    assert rr["n_gapped"] >= rr["n_reconfine"]


def test_gate2_armB_pooled_reconfine_rate_sweep():
    """The POOLED (srs L=4 + L=6) measured re-confine rate — the headline disclosure
    number reported in the result doc GATE-2 section — is a minority (< 0.20), so the
    NOT-VOID / S-structure-decided verdict carries a measured majority (>= ~0.80)
    de-confine margin, not a single-seed binary. alpha-FREE."""
    out = scramble_rate_sweep(nets=(("srs", 4), ("srs", 6)), n_perm=100, seed=20260620)
    assert out["ok"]
    assert out["pooled_n_perm"] == 200
    assert out["pooled_reconfine_rate"] < 0.20, (
        f"pooled ARM-B re-confine rate {out['pooled_reconfine_rate']:.3f} >= 0.20 "
        "— 'predominantly de-confines' no longer holds"
    )
    assert out["pooled_deconfine_rate"] >= 0.80
    assert out["predominantly_deconfines"]


# ─────────────────────────────────────────────────────────────────────────────
# GATE 3 — QUARTER-ARC SHAPE (headline). Pinned: shape-generic (gap < 10%).
# ─────────────────────────────────────────────────────────────────────────────


def test_gate3_brentq_norm_match_succeeds():
    """RF-5: the norm-feasible same-family comparator's brentq norm-match SUCCEEDS
    (the retired endpoint-tanh was norm-INFEASIBLE). The canonical π/4 target
    recovers p=0.5 exactly."""
    nm = norm_match_p(np.pi / 4.0)
    assert nm["ok"]
    assert abs(nm["p"] - 0.5) < 1e-3, f"π/4 should recover p=0.5, got {nm['p']}"


def test_gate3_null_shape_control_passes():
    """RF / GATE3: two same-family shapes matched norm+depth give Δ/L within <<10%
    (the metric reads SHAPE not DEPTH) — the gate BEFORE any cross-family gap counts."""
    r = solve_quarter_arc_shape(ConfinementConfig(net="diamond", L=8))
    assert r["null_control_passes"], f"null control failed (metric reads depth): {r['null_gap']}"
    assert r["depth_matched"]  # canon/comparator min-S matched


@pytest.mark.parametrize("net,L", [("diamond", 8), ("srs", 4), ("srs", 6)])
def test_gate3_shape_gap_below_10pct_echo(net, L):
    """GATE3 pinned ECHO: the quarter-arc Δ/L is shape-GENERIC — the depth-matched
    same-family comparator gives the SAME Δ/L (gap < 10%). The quarter-arc is NOT
    special (generic saturable-NLS)."""
    r = solve_quarter_arc_shape(ConfinementConfig(net=net, L=L))
    assert r["norm_match_ok"]
    assert not r["shape_gap_exceeds_10pct"], f"shape gap unexpectedly >10%: {r['shape_gap']}"


# ─────────────────────────────────────────────────────────────────────────────
# ELECTRON ANCHOR — CHORD-required, NOT expected. Pinned: NOT reproduced.
# ─────────────────────────────────────────────────────────────────────────────


def test_electron_anchor_not_reproduced():
    """The electron anchor (ω_cutoff≈2.87 reproduced α-free, converged) is NOT
    reproduced: the connect-map ω is lattice-band-structure-set (diverges with L),
    NOT a converged universal 2.87. This caps the verdict at ECHO (pre-committed)."""
    a = electron_anchor_check("srs", [2, 4, 6])
    assert not a["anchor_reproduced"], "anchor UNEXPECTEDLY reproduced — re-run adjudication"


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (iii)(iv): DEC-5 anti-coincidence + α-free structural.
# ─────────────────────────────────────────────────────────────────────────────


def test_dec5_anti_coincidence_not_Z_radiation():
    """DEC-5: the bound-mode ω is NOT silently Z_RADIATION=29.98 (the only ~30 is
    band-consistent Z_RADIATION, never an identity)."""
    d = dec5_anti_coincidence(ConfinementConfig(net="diamond", L=8))
    assert d["not_Z_radiation"]
    assert abs(d["omega_bound"] - 29.98) > 1.0


def test_alpha_free_structural_invariance():
    """VALIDATE-ON-KNOWN (iv): α cancels in the dimensionless A=|V|/V_yield. ALPHA
    is NOT reachable in the module; doubling α leaves ω and Δ/L EXACTLY unchanged."""
    afi = alpha_free_invariance(ConfinementConfig(net="diamond", L=8))
    assert not afi["alpha_reachable_in_module"]
    assert afi["rel_d_omega"] < 1e-6
    assert afi["rel_d_delta_over_L"] < 1e-6
    assert afi["alpha_free_pass"]


def test_no_alpha_carrier_imported():
    """Import-guard: no ALPHA / Q_TANK / ELECTRON / RHO_BULK / Q_TANK=1/alpha carrier
    is reachable in the Fork-B module globals (anti-circularity HR2)."""
    import ave.solvers.fork_b_saturation_tank as F

    for tok in ("ALPHA", "Q_TANK", "ELECTRON", "RHO_BULK"):
        assert tok not in vars(F), f"alpha-leak: {tok} reachable in fork_b module"


# ─────────────────────────────────────────────────────────────────────────────
# TOP-LEVEL VERDICT — pinned: ECHO.
# ─────────────────────────────────────────────────────────────────────────────


def test_top_level_verdict_is_echo():
    """The frozen-binned verdict is ECHO (pre-committed, expected, successful):
    confined + scramble-de-confines (real, S-dependent) BUT shape-generic + no
    anchor => FORM-chord/consistency. NOT a manufactured CHORD; NOT VOID; NOT REFUTE."""
    out = run_fork_b_gate()
    assert out["verdict"] == "ECHO", f"verdict moved: {out['verdict']} — {out['reason']}"
    b = out["binning"]
    assert b["confined"]
    assert b["scramble_deconfines_both_arms"]
    assert not b["auto_void"]
    assert not b["shape_gap_chord"]  # shape-generic
    assert not b["electron_anchor_reproduced"]  # no anchor => no CHORD
