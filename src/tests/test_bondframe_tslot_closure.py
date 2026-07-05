"""Tests — the bond-frame T-slot adjudication (CORRECTED verdict, orchestrator review #533).

FROZEN prereg: research/2026-07-05_bondframe-tslot-closure_prereg_FROZEN.md.
CORRECTED VERDICT (2026-07-05, orchestrator review of PR #533): [CONSTRAINT-DEPENDENT],
NOT [DC-ONLY-DERIVED]. The cross-host table (ring COLD / pinned COLD / free SOFT by
<dy^2>/2) is the frozen bin (iv) signature. The DC-ONLY theorem was overclaimed: it holds
only for a SINGLE TRAVELING MODE on a FIXED-CONTOUR host (item 2), and the FREE host reads
SOFT (item 1).

Two INDEPENDENT code paths (the #531 tautology guard):
  - `bondframe_tslot_predictions.py` : SYMBOLIC (sympy) derivation of the coefficients.
  - `ring_bondframe_probe.py`        : NUMERIC static-relaxation cross-host confirmation.
The test asserts the tautology guard (no cross-import) and reconciles via the #528
ReconcileGate (can-fire proven on dropped-term/sign-flip synthetics on real paths).

The numeric-ring tests are marked engine_sim (CI-partition convention); the symbolic +
gate tests are fast.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.validation.reconcile_gate import DiscrepantHalt, ReconcileGate
from scripts.vol_1_foundations import bondframe_tslot_predictions as pred

# ── DERIVED tolerance bands ───────────────────────────────────────────────────
# Cold band: 3x the numeric relaxation/phase/delta residual floor (a host reading within
# [1-band, 1+band] is COLD).
COLD_BAND = 3.0e-3
# Kernel correction: O(y0^6) ~ 1e-6 class at y0=0.1428 (item-4c erratum: was mislabeled O4).
KERNEL_BOUND = 5.0e-6
# Static-vs-dynamical modeling gap for the tilt order-of-magnitude validation (item-4a).
TILT_ORDERMAG_GAP = 0.05


# ═════════════════════════════════════════════════════════════════════════════
# SYMBOLIC BACKBONE — every derivation step sympy-verified (exact-zero residuals)
# ═════════════════════════════════════════════════════════════════════════════
def test_symbolic_backbone_all_exact_zero():
    """All 8 load-bearing identities are exactly 0 (sympy). Locks the derivation.
    R6 is now a REAL closure derivation (item-4d: was a tautology); R8 is the free-host
    contraction coefficient (item-4d: was a duplicate of R3)."""
    resid = pred.symbolic_backbone()
    assert len(resid) == 8
    for name, val in resid.items():
        assert val == 0, f"{name} = {val} (expected exact 0)"
    # item-4d: R6 must be the closure-DERIVED identity, R8 the free-host contraction
    assert "R6_ring_closure_derives_mean" in resid
    assert "R8_free_host_contraction" in resid


# ═════════════════════════════════════════════════════════════════════════════
# PART 1 — the LAB-FRAME TILT (item-4a: honest anchor + honest band, gate-failure honest)
# ═════════════════════════════════════════════════════════════════════════════
def test_tilt_leading_is_mean_dy2():
    """Leading tilt = <dy^2> = y0^2(1-cos k). The k is dispersion-set (not tuned)."""
    y0, omega = pred.Y0_TENT, pred.OMEGA_PUMP
    k = pred.wave_number(omega)
    assert pred.wave_number(omega) == pytest.approx(1.2870022, abs=1e-6)   # cos k = 0.28
    assert pred.tilt_leading(y0, omega) == pytest.approx(y0**2 * (1 - np.cos(k)), rel=1e-12)


def test_tilt_truncation_band_fails_honestly():
    """ITEM-4a (honest gate failure): the PURE-TRUNCATION band (derived from the dispersion
    shift + #532's numeric floor) does NOT cover the static-vs-dynamical discrepancy. We
    report this HONESTLY rather than inflating the band to force a pass. The residual gap is
    the static-single-mode-vs-#532's-sponge-terminated-finite-chain MODELING difference."""
    band = pred.tilt_truncation_band()
    # the pure-truncation band is smaller than the leading->exact convexity gap (informative)
    assert band < abs(pred.tilt_leading() - pred.tilt_exact())
    # and it does NOT cover the exact-vs-leading gap fully — the honest failure the review found
    # (the band is ~1.1% of leading; the derivation is validated at order-mag level instead)
    assert band < 0.02 * pred.tilt_leading()          # ~1.1%, not inflated


@pytest.mark.engine_sim
def test_tilt_order_of_magnitude_validation():
    """ITEM-4a: the derivation IS validated at the ORDER-OF-MAGNITUDE + DOMINANT-CHANNEL
    level — the static tilt matches #532's in-branch tilt_decomposition within the static-
    vs-dynamical modeling gap (~5%). The anchor is RECOMPUTED in-branch (the 5-digit value
    is NOT in #532's result doc, which reports '+1.40%'). This is the validation the
    corrected verdict uses (the tilt is NOT the load-bearing quantity for the re-bin)."""
    assert pred.tilt_reproduces_532_ordermag() is True
    anchor = pred.tilt_anchor_532()
    assert anchor == pytest.approx(0.01397, abs=1e-4)   # #532's dynamical tilt, in-branch
    # honest: the discrepancy exceeds the pure-truncation band (the gate-failure is real)
    assert abs(pred.tilt_exact() - anchor) > pred.tilt_truncation_band()


# ═════════════════════════════════════════════════════════════════════════════
# PART 2 — the MEAN CHORD STRETCH + the item-4c/4d kernel & closure derivations
# ═════════════════════════════════════════════════════════════════════════════
def test_mean_chord_strain_is_half_mean_dy2():
    """<A_bond> = <dy^2>/2 for a single traveling mode. The 1/2 is the DERIVED convexity
    coefficient (backbone R4), NOT an asserted 1/2 (KNIFE)."""
    y0, omega = pred.Y0_TENT, pred.OMEGA_PUMP
    assert pred.mean_chord_strain(y0, omega) == pytest.approx(0.5 * pred.tilt_leading(y0, omega), rel=1e-12)


def test_kernel_correction_is_o6_not_o4():
    """ITEM-4c erratum: the kernel/nonlinearity correction is O(y0^6), NOT the frozen
    'O(y0^4)'. Both channels: tilt = -dy^6/8, tension = -dy^6/48 (sympy). It scales as y0^6
    (halving y0 cuts it ~64x). The PHYSICS (kernel negligible) is unchanged; the ORDER label
    is corrected."""
    corr = pred.kernel_correction_o4()
    assert abs(corr) < KERNEL_BOUND
    c_half = pred.kernel_correction_o4(y0=pred.Y0_TENT / 2)
    ratio = abs(corr) / max(abs(c_half), 1e-30)
    assert 40.0 < ratio < 96.0, f"kernel correction scales {ratio:.1f}x, expected ~64x (O(y0^6))"


def test_R6_is_real_closure_derivation_not_tautology():
    """ITEM-4d: R6 must DERIVE A* = <dy^2>/2 from the ring closure Sum(du)=0 + equilibrium
    on an EXPLICIT 4-bond ring (sympy solves the closure for A*), not restate it. Verified
    by re-running the derivation symbolically and checking the solved A* equals <dy^2>/2."""
    import sympy as sp
    dys = sp.symbols("d0 d1 d2 d3", real=True)
    Astar = sp.symbols("Astar", real=True)
    dus = [Astar - d**2 / 2 for d in dys]
    sol = sp.solve(sp.Eq(sum(dus), 0), Astar)[0]      # the closure derives A*
    assert sp.simplify(sol - sum(d**2 for d in dys) / 8) == 0    # A* = <dy^2>/2 (mean of 4)


def test_free_host_contraction_coefficient():
    """ITEM-4d R8: on the free host, the bond x-span contracts as <dx> = sqrt(1-dy^2) =
    1 - dy^2/2 + O(dy^4). The -1/2 contraction coefficient is what makes the free host SOFT."""
    import sympy as sp
    dyv = sp.symbols("dyv", real=True)
    series = sp.series(sp.sqrt(1 - dyv**2), dyv, 0, 3).removeO()
    assert sp.simplify(series - (1 - dyv**2 / 2)) == 0


# ═════════════════════════════════════════════════════════════════════════════
# PART 3 — the CONSTRAINT-DEPENDENT verdict (the re-bin; predictions are host-keyed)
# ═════════════════════════════════════════════════════════════════════════════
def test_bondframe_deposit_is_host_keyed():
    """ITEM-1: the bond-frame deposit is CONSTRAINT-DEPENDENT, not a single value:
    ring/pinned -> 0 (cold); free -> -<dy^2>/2 (soft). This is the re-bin core."""
    assert pred.bondframe_deposit_predicted("ring") == 0.0
    assert pred.bondframe_deposit_predicted("pinned") == 0.0
    assert pred.bondframe_deposit_predicted("free") == pytest.approx(-pred.mean_chord_strain(), rel=1e-12)
    # the free-host softness is resolvable from the cold band (materially different)
    assert abs(pred.bondframe_deposit_predicted("free")) > 2 * COLD_BAND


# ═════════════════════════════════════════════════════════════════════════════
# THE #531 TAUTOLOGY GUARD — the numeric module never imports the prediction module
# ═════════════════════════════════════════════════════════════════════════════
def test_tautology_guard_no_cross_import():
    """The numeric ring driver MUST NOT import the symbolic prediction module (the #531
    guard). Checks for an actual IMPORT statement (not the string in a comment/docstring)."""
    import re

    from scripts.vol_1_foundations import ring_bondframe_probe as ring
    with open(ring.__file__) as fh:
        for line in fh:
            code = line.split("#", 1)[0]
            assert not re.search(r"\bimport\b.*bondframe_tslot_predictions", code), (
                f"TAUTOLOGY: numeric module imports the prediction module: {line!r}")
            assert not re.search(r"\bfrom\b.*bondframe_tslot_predictions.*\bimport\b", code), (
                f"TAUTOLOGY: numeric module imports the prediction module: {line!r}")


# ═════════════════════════════════════════════════════════════════════════════
# THE CROSS-HOST TABLE (item-1: the [CONSTRAINT-DEPENDENT] signature) — SLOW
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_three_host_table_constraint_dependent():
    """ITEM-1 CORE: ring COLD, pinned COLD, free SOFT (soft by <dy^2>/2). Materially
    different bond-frame readings across the prereg's own named hosts = the frozen bin (iv)
    [CONSTRAINT-DEPENDENT] signature. This is the measurement #533 never ran."""
    from scripts.vol_1_foundations.ring_bondframe_probe import three_host_table
    t = three_host_table(n_nodes=200, n_phase=24)
    assert abs(t["ring"] - 1.0) < COLD_BAND               # ring COLD
    assert abs(t["pinned"] - 1.0) < COLD_BAND             # pinned COLD
    assert t["free"] < 1.0 - COLD_BAND                    # free SOFT (below cold band)
    assert t["free"] == pytest.approx(t["free_pred_soft"], abs=2e-4)   # soft by <dy^2>/2
    assert t["spread"] > COLD_BAND                        # MATERIALLY different across hosts


@pytest.mark.engine_sim
def test_free_host_softness_is_bulk_N_independent():
    """ITEM-1: the free-host SOFT reading is BULK (N-independent) — the T=0 equilibrium is
    analytic and reads soft by <dy^2>/2 at every N. This is what routes [CONSTRAINT-DEPENDENT]
    (a BULK deposit that is CONSTRAINT-SET), not a finite-N artifact (which would HALT)."""
    from scripts.vol_1_foundations.ring_bondframe_probe import open_chain_cyclemean
    r120 = open_chain_cyclemean(n_nodes=120, host="free", n_phase=24)
    r480 = open_chain_cyclemean(n_nodes=480, host="free", n_phase=24)
    assert r120["cyclemean_bondframe_k_ratio"] == pytest.approx(
        r480["cyclemean_bondframe_k_ratio"], abs=1e-6)   # N-independent (BULK)
    assert r120["max_A_at_equil"] < 1e-12                 # genuine T=0 equilibrium


# ═════════════════════════════════════════════════════════════════════════════
# ITEM-2 — the SCOPED theorem: standing-wave counterexample (KEEP-BOTH)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_standing_wave_deposits_per_bond_pattern():
    """ITEM-2: the DC-ONLY reading needs THREE premises: <y>=0 + fixed contour + SPATIAL
    HOMOGENEITY of <dy^2>_j. A STANDING wave satisfies the first two but VIOLATES the third:
    it deposits a per-bond +/-O(y0^2) strain PATTERN (~0.0038), while the MEAN-over-bonds
    geometry witness still reads cold. A traveling mode is uniform (range ~0)."""
    from scripts.vol_1_foundations.ring_bondframe_probe import measure_ring
    trav = measure_ring(n_nodes=120, n_phase=32, relax_iter=8000, standing=False)
    stand = measure_ring(n_nodes=120, n_phase=32, relax_iter=8000, standing=True)
    # traveling: spatially homogeneous (per-bond uniform)
    assert trav["A_per_bond_range"] < 1e-6
    # standing: per-bond STRUCTURED (the counterexample), ~O(y0^2)
    assert stand["A_per_bond_max_abs"] > 1e-3
    # but the MEAN-over-bonds witness reads cold for BOTH (item-2 mean-vs-per-bond honesty)
    assert stand["cyclemean_dx"] == pytest.approx(1.0, abs=1e-6)


# ═════════════════════════════════════════════════════════════════════════════
# ITEM-4b — the bin selector restores the N-convergence conjunct; routes honestly
# ═════════════════════════════════════════════════════════════════════════════
def test_bin_selector_constraint_dependent_verdict():
    """The frozen bin selector routes [CONSTRAINT-DEPENDENT] on the cross-host table (ring
    cold, free soft, spread>band, N-convergent). Item-4b: the N-convergence conjunct is
    RESTORED (a spread that is NOT N-convergent HALTs, not routes CONSTRAINT-DEPENDENT)."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import classify_bin
    binv = classify_bin(
        tilt_reproduces_532=True,
        host_readings={"ring": 1.0, "pinned": 0.99998, "free": 0.99256},
        cold_band=COLD_BAND, host_deposit_N_convergent=True)
    assert binv == "CONSTRAINT-DEPENDENT"


def test_bin_selector_halts_on_non_convergent_spread():
    """ITEM-4b: a host spread that is NOT N-convergent (a finite-N artifact) HALTs — it does
    NOT silently route CONSTRAINT-DEPENDENT. The restored N-convergence conjunct guards this."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import BinHalt, classify_bin
    with pytest.raises(BinHalt):
        classify_bin(tilt_reproduces_532=True,
                     host_readings={"ring": 1.0, "pinned": 0.998, "free": 0.990},
                     cold_band=COLD_BAND, host_deposit_N_convergent=False)


def test_bin_selector_dc_only_path_reachable():
    """If ALL hosts read cold, the verdict IS [DC-ONLY-DERIVED] — a reachable non-default
    path (proves the CONSTRAINT-DEPENDENT verdict was earned, not a dead-end default)."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import classify_bin
    binv = classify_bin(tilt_reproduces_532=True,
                        host_readings={"ring": 1.0, "pinned": 1.0, "free": 1.0},
                        cold_band=COLD_BAND, host_deposit_N_convergent=True)
    assert binv == "DC-ONLY-DERIVED"


def test_bin_selector_bulk_deposit_path_reachable():
    """If ALL hosts show the SAME nonzero N-convergent deposit -> [BULK-DEPOSIT-DERIVED].
    Reachable non-default path."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import classify_bin
    binv = classify_bin(tilt_reproduces_532=True,
                        host_readings={"ring": 1.02, "pinned": 1.02, "free": 1.02},
                        cold_band=COLD_BAND, host_deposit_N_convergent=True)
    assert binv == "BULK-DEPOSIT-DERIVED"


def test_bin_selector_halts_on_bad_tilt():
    """If the derived tilt does NOT reproduce #532 at all, the bin selector HALTs (no
    verdict) — not a silent default."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import BinHalt, classify_bin
    with pytest.raises(BinHalt):
        classify_bin(tilt_reproduces_532=False,
                     host_readings={"ring": 1.0, "pinned": 1.0, "free": 0.99},
                     cold_band=COLD_BAND, host_deposit_N_convergent=True)


# ═════════════════════════════════════════════════════════════════════════════
# THE #528 RECONCILE-GATE — symbolic vs numeric-ring, INDEPENDENT paths, can-fire proven
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_reconcile_gate_free_softness_symbolic_vs_ring():
    """Reconcile the SYMBOLIC free-host softness prediction (-<dy^2>/2) against the NUMERIC
    ring/open measurement — two INDEPENDENT code paths. Can-fire self-test runs FIRST."""
    from scripts.vol_1_foundations.ring_bondframe_probe import open_chain_cyclemean
    measured_soft = 1.0 - open_chain_cyclemean(n_nodes=120, host="free", n_phase=24)["cyclemean_bondframe_k_ratio"]
    symbolic_soft = -pred.bondframe_deposit_predicted("free")   # +<dy^2>/2
    ReconcileGate(
        label="free_softness_symbolic_vs_ring",
        claimed=measured_soft,
        independent=symbolic_soft,
        rtol=0.05, atol=0.0,        # the k-value + convexity residual
    ).enforce()


def test_reconcile_gate_can_fire_on_dropped_term():
    """PROVE the gate FIRES on a DROPPED-TERM synthetic (claim=cold=0 vs the real nonzero
    free softness). Retires the #521/#526/#527 dead-gate class."""
    with pytest.raises(DiscrepantHalt):
        ReconcileGate(
            label="dropped_term_synthetic",
            claimed=0.0,
            independent=-pred.bondframe_deposit_predicted("free"),
            rtol=0.05, atol=0.0,
        ).enforce(prove_first=False)


def test_reconcile_gate_can_fire_on_sign_flip():
    """PROVE the gate FIRES on a SIGN-FLIP synthetic (claim stiffens vs measured softens)."""
    soft = -pred.bondframe_deposit_predicted("free")
    with pytest.raises(DiscrepantHalt):
        ReconcileGate(label="sign_flip_synthetic", claimed=-soft, independent=soft,
                      rtol=0.05, atol=0.0).enforce(prove_first=False)


def test_reconcile_gate_refuses_vacuous_band():
    """A gate with an infinite tolerance is refused at registration (#531 no-vacuous-band)."""
    with pytest.raises(ValueError):
        ReconcileGate(label="vacuous", claimed=1.0, independent=1.0, rtol=float("inf"))


# ── UPSTREAM REGRESSION GUARD (PR #535 review): RingChain nonlinear tension scales with k_a ──
def test_nonlinear_tension_scales_with_ka_regression_guard():
    """REGRESSION GUARD (PR #535 review): the nonlinear (kernel) tension MUST scale with
    k_a. Before the fix it returned _phi_prime(A) with k0=1 BAKED IN, ignoring k_a on the
    nonlinear (default) path — a silent k_a-inert branch a static read could not catch (it
    only surfaced at integrator time when a k_long/k_shear sonic sweep gave bit-identical
    dynamics across k_a). k_a IS the A=0 axial tangent stiffness (derived: dT/dA|_0 = k0 for
    Phi'(A) = k0*(A*sqrt(1-A^2)+asin A)/2), so the nonlinear tension is k_a*_phi_prime(A)."""
    from scripts.vol_1_foundations.ring_bondframe_probe import RingChain

    A = np.array([0.1])
    r05 = RingChain(10, k_a=0.5)
    r40 = RingChain(10, k_a=4.0)
    # the nonlinear tension now scales linearly in k_a (was IDENTICAL before the fix)
    assert float(r40.tension(A)[0]) == pytest.approx(8.0 * float(r05.tension(A)[0]), rel=1e-12)
    # dT/dA at A=0 equals k_a (the axial tangent stiffness = k_a semantics)
    for ka in (0.5, 1.0, 4.0):
        r = RingChain(10, k_a=ka)
        eps = 1e-6
        dTdA = (float(r.tension(np.array([eps]))[0]) - float(r.tension(np.array([-eps]))[0])) / (2 * eps)
        assert dTdA == pytest.approx(ka, rel=1e-4)


def test_ka_fix_blast_radius_cleared_at_ka1():
    """BLAST-RADIUS CLEARANCE (PR #535 review): every merged consumer (#533/#534 and this
    module's drivers) runs the nonlinear branch at k_a=1, where the pre-fix baked k0=1 is
    coincidentally correct. So the fix is a NO-OP at k_a=1 — no merged result changes."""
    from scripts.vol_1_foundations.ring_bondframe_probe import RingChain, _phi_prime

    A = np.linspace(-0.3, 0.3, 13)
    r = RingChain(10, k_a=1.0)
    # at k_a=1 the fixed nonlinear tension is bit-identical to the pre-fix _phi_prime(A)
    assert np.allclose(r.tension(A), _phi_prime(A), rtol=0, atol=0)
    # the three-host table (all merged computations at k_a=1) is unchanged
    from scripts.vol_1_foundations.ring_bondframe_probe import three_host_table
    t = three_host_table()
    assert t["ring"] == pytest.approx(1.0, abs=3e-3)
    assert t["free"] == pytest.approx(0.992563, abs=1e-4)
