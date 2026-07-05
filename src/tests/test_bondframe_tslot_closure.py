"""Tests — the bond-frame T-slot closure on a CLEAN periodic-ring host.

FROZEN prereg: research/2026-07-05_bondframe-tslot-closure_prereg_FROZEN.md.
Verdict: [DC-ONLY-DERIVED] — the bond-frame O(y0^2) content of a traveling wave on the
clean ring is COLD (theorem); the lab-frame stiffening is the kinematic tilt.

Two INDEPENDENT code paths (the #531 tautology guard):
  - `bondframe_tslot_predictions.py` : SYMBOLIC (sympy) derivation of the coefficients.
  - `ring_bondframe_probe.py`        : NUMERIC static-relaxation ring confirmation.
The test asserts the tautology guard (no cross-import) and reconciles the two via the
#528 ReconcileGate (can-fire proven on dropped-term/sign-flip synthetics on real paths).

Tolerances DERIVED from the truncation orders (the #531/#532 lesson: no vacuous bands).
The numeric-ring tests are marked engine_sim (CI-partition convention); the
symbolic + gate tests are fast.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.validation.reconcile_gate import DiscrepantHalt, ReconcileGate
from scripts.vol_1_foundations import bondframe_tslot_predictions as pred

# ── DERIVED tolerance bands (frozen prereg §"THE DERIVED TOLERANCE BANDS") ─────
# Tilt gate: the derivation truncates at O(y0^2); the #532 measured tilt includes the
# O(y0^2) dispersion back-shift + window residual. Band = 3.5% of the leading value.
TILT_BAND_FRAC = 0.035
# Cycle-mean-COLD band: 3x the numeric relaxation/phase/delta residual floor.
COLD_BAND = 3.0e-3
# O(y0^4) kernel correction: ~1e-6 class at y0=0.1428.
KERNEL_O4_BOUND = 5.0e-6


# ═════════════════════════════════════════════════════════════════════════════
# SYMBOLIC BACKBONE — every derivation step sympy-verified (exact-zero residuals)
# ═════════════════════════════════════════════════════════════════════════════
def test_symbolic_backbone_all_exact_zero():
    """All 8 load-bearing identities are exactly 0 (sympy). Locks the derivation."""
    resid = pred.symbolic_backbone()
    assert len(resid) == 8
    for name, val in resid.items():
        assert val == 0, f"{name} = {val} (expected exact 0)"


# ═════════════════════════════════════════════════════════════════════════════
# PART 1 — the LAB-FRAME TILT gate (validation vs #532's measured +0.013969)
# ═════════════════════════════════════════════════════════════════════════════
MEASURED_532_TILT = 0.013969   # research/2026-07-05_pump-probe-tslot_result.md (the run's value)


def test_tilt_leading_is_mean_dy2():
    """Leading tilt = <dy^2> = y0^2(1-cos k). The k is dispersion-set (not tuned)."""
    y0, omega = pred.Y0_TENT, pred.OMEGA_PUMP
    k = pred.wave_number(omega)
    assert pred.wave_number(omega) == pytest.approx(1.2870022, abs=1e-6)   # cos k = 0.28
    assert pred.tilt_leading(y0, omega) == pytest.approx(y0**2 * (1 - np.cos(k)), rel=1e-12)


def test_tilt_exact_reproduces_532_within_derived_band():
    """The derived EXACT tilt integrand reproduces #532's measured +0.013969 within the
    DERIVED band (O(y0^2) dispersion back-shift + #532 window residual). Validation gate."""
    tilt = pred.tilt_exact()
    band = TILT_BAND_FRAC * pred.tilt_leading()   # 3.5% of leading, derived
    assert abs(tilt - MEASURED_532_TILT) <= band, (
        f"derived exact tilt {tilt:.6f} vs #532 measured {MEASURED_532_TILT} "
        f"exceeds derived band {band:.6f}")
    # and the exact is BELOW the leading (convexity pulls it down) — a structural check
    assert tilt < pred.tilt_leading()


def test_tilt_gate_is_informative_not_vacuous():
    """The tilt band is STRICTLY smaller than the leading value (the resolvable scale),
    so the gate could FAIL on a wrong derivation — not a vacuous band."""
    band = TILT_BAND_FRAC * pred.tilt_leading()
    assert band < pred.tilt_leading()             # band < signal
    assert band < 0.5 * pred.tilt_leading()       # comfortably informative


# ═════════════════════════════════════════════════════════════════════════════
# PART 2 — the MEAN CHORD STRETCH (ring-closure theorem <A_bond> = <dy^2>/2)
# ═════════════════════════════════════════════════════════════════════════════
def test_mean_chord_strain_is_half_mean_dy2():
    """<A_bond> = <dy^2>/2. The 1/2 is the DERIVED convexity coefficient (backbone R4),
    NOT an asserted 1/2 (KNIFE)."""
    y0, omega = pred.Y0_TENT, pred.OMEGA_PUMP
    assert pred.mean_chord_strain(y0, omega) == pytest.approx(0.5 * pred.tilt_leading(y0, omega), rel=1e-12)


def test_slot_tension_scalar_is_ac_not_dc():
    """<T>/ell (the per-snapshot AC slot scalar) ~ <A_bond> at leading order (Phi'(x)~x)
    — reported KEEP-BOTH. It is NONZERO (the #529-cousin) — and it is EXPLICITLY NOT the
    bond-frame DC deposit (which is 0, Part 3). Guards against reading the two as the same."""
    slot = pred.slot_tension_scalar()
    assert slot == pytest.approx(pred.mean_chord_strain(), rel=1e-2)   # ~ <A_bond>
    assert slot > 0                                                    # nonzero AC scalar
    assert pred.bondframe_deposit_predicted() == 0.0                   # DC deposit = 0


# ═════════════════════════════════════════════════════════════════════════════
# PART 4(a) — RECONCILIATION: why the kernel contributes ~1e-6 (high-order)
# ═════════════════════════════════════════════════════════════════════════════
def test_kernel_correction_is_high_order_tiny():
    """The kernel/nonlinearity correction to the TILT channel is O(y0^6) — even more
    negligible than the O(y0^4) mean-stretch channel. The tilt integrand is
    Phi''(A)*(dy/L)^2 with A=dy^2/2, so [Phi''(A)-1] ~ -A^2/2 ~ -dy^4/8, times (dy/L)^2
    ~ dy^2 -> ~ -dy^6/8 = O(y0^6). This is WHY a linear chain reproduces the tilt to
    ~1e-6 (#532 CRITICAL-1 saw ~2e-6 on the FULL lab-frame stiffness, which also carries
    the O(y0^4) mean-stretch tension channel)."""
    corr = pred.kernel_correction_o4()
    assert abs(corr) < KERNEL_O4_BOUND, f"kernel correction {corr:.3e} too large"
    # it scales as y0^6: halving y0 should cut it ~64x (the tilt-channel kernel term)
    c_half = pred.kernel_correction_o4(y0=pred.Y0_TENT / 2)
    ratio = abs(corr) / max(abs(c_half), 1e-30)
    assert 40.0 < ratio < 96.0, f"kernel-correction scales as {ratio:.1f}x, expected ~64x (O(y0^6))"


# ═════════════════════════════════════════════════════════════════════════════
# THE #531 TAUTOLOGY GUARD — the numeric module never imports the prediction module
# ═════════════════════════════════════════════════════════════════════════════
def test_tautology_guard_no_cross_import():
    """The numeric ring driver MUST NOT import the symbolic prediction module (the #531
    guard: the confirmation must not consume the formulas it confirms). The gate compares
    OUTPUTS only. Checks for an actual IMPORT statement (not the string in a comment)."""
    import re

    from scripts.vol_1_foundations import ring_bondframe_probe as ring
    with open(ring.__file__) as fh:
        for line in fh:
            code = line.split("#", 1)[0]   # strip comments — the docstring names it on purpose
            assert not re.search(r"\bimport\b.*bondframe_tslot_predictions", code), (
                f"TAUTOLOGY: the numeric ring module imports the prediction module: {line!r}")
            assert not re.search(r"\bfrom\b.*bondframe_tslot_predictions.*\bimport\b", code), (
                f"TAUTOLOGY: the numeric ring module imports the prediction module: {line!r}")


# ═════════════════════════════════════════════════════════════════════════════
# PART 3 — the DC-ONLY THEOREM confirmed numerically on the CLEAN ring (SLOW)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_ring_cyclemean_bondframe_reads_cold():
    """[DC-ONLY-DERIVED] core gate: the bond-frame tangent stiffness a slow probe feels
    AT the cycle-mean config reads COLD (ratio 1) within the derived band. The theorem:
    <y>=0 + ring closure => cold mean bond geometry => cold transverse stiffness."""
    from scripts.vol_1_foundations.ring_bondframe_probe import measure_ring
    r = measure_ring(n_nodes=120, n_phase=32, relax_iter=8000)   # fast-but-honest params
    assert abs(r["cyclemean_bondframe_k_ratio"] - 1.0) < COLD_BAND, (
        f"bond-frame cycle-mean stiffness {r['cyclemean_bondframe_k_ratio']} != cold")
    # the theorem's geometry witnesses: <dx>=1 (un-stretched), <A>~0 (straight mean bond)
    assert r["cyclemean_dx"] == pytest.approx(1.0, abs=1e-9)
    assert abs(r["cyclemean_A"]) < 1e-9
    # and the LAB-FRAME observable IS stiffer by ~the tilt (the artifact the ring exposes)
    assert r["labframe_k_ratio"] - 1.0 > 0.5 * pred.tilt_leading()


def test_ring_deposit_resolvable_from_cold_band():
    """The COLD reading is not a band artifact hiding a deposit: the slot-<T>/ell scalar
    (~0.0073 fractional) is ~2.4x the cold band (0.003), so a BULK-DEPOSIT of that size
    WOULD be resolvable from cold. The measured bond-frame reading is COLD (~1e-5), ~700x
    BELOW the band — so [DC-ONLY] and [BULK-DEPOSIT] are RESOLVABLE and the COLD verdict is
    not a resolution failure. (Fast test: uses only the derived scalar, no ring call.)"""
    slot_frac = pred.slot_tension_scalar() / pred.K_S
    assert slot_frac > 2.0 * COLD_BAND          # the would-be deposit is resolvably > band
    assert slot_frac == pytest.approx(0.00729, abs=1e-4)   # ~2.4x the 0.003 band


@pytest.mark.engine_sim
def test_ring_dc_only_is_N_convergent_not_constraint_dependent():
    """The ring bond-frame COLD reading is N-CONVERGENT (boundary-independent) — it does
    NOT drift with ring size. This rules out [CONSTRAINT-DEPENDENT] for the ring: the
    theorem is bulk, not a finite-N artifact."""
    from scripts.vol_1_foundations.ring_bondframe_probe import measure_ring
    r120 = measure_ring(n_nodes=120, n_phase=24, relax_iter=6000)
    r240 = measure_ring(n_nodes=240, n_phase=24, relax_iter=6000)
    assert abs(r120["cyclemean_bondframe_k_ratio"] - 1.0) < COLD_BAND
    assert abs(r240["cyclemean_bondframe_k_ratio"] - 1.0) < COLD_BAND
    # the mean chord strain (the ring theorem <dy^2>/2) is also stable across N
    assert r120["mean_chord_A"] == pytest.approx(r240["mean_chord_A"], rel=0.05)


# ═════════════════════════════════════════════════════════════════════════════
# PART 4(a) numeric — the LINEAR-axial ring reproduces the tilt to ~kernel_o4
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_ring_linear_reproduces_tilt_to_kernel_o4():
    """RECONCILIATION (a): a LINEAR-axial ring (no kernel, no Jensen) reproduces the
    lab-frame stiffening to ~the O(y0^4) kernel correction — confirming the effect is
    KINEMATIC, not the concave kernel (#532 CRITICAL-1, 2e-6)."""
    from scripts.vol_1_foundations.ring_bondframe_probe import measure_ring
    nl = measure_ring(n_nodes=120, n_phase=24, relax_iter=6000, linear_axial=False)
    lin = measure_ring(n_nodes=120, n_phase=24, relax_iter=6000, linear_axial=True)
    diff = abs(nl["labframe_k_ratio"] - lin["labframe_k_ratio"])
    assert diff < KERNEL_O4_BOUND, (
        f"linear vs nonlinear lab-frame differ by {diff:.3e}, expected ~kernel O(y0^4)")


# ═════════════════════════════════════════════════════════════════════════════
# PART 4(b) numeric — the OPEN-chain boundary POSITION-DEPENDENCE (the artifact)
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_open_chain_is_boundary_position_dependent():
    """RECONCILIATION (b): on the OPEN chain the mean chord strain is POSITION-DEPENDENT
    and BOUNDARY-CONFIG-SENSITIVE (pinned vs free give materially different profiles) —
    the #532 boundary artifact. Contrast: the RING is uniform + boundary-independent.
    SCOPE (flag-don't-fix): reproduces the #532 GRADIENT STRUCTURE, not the exact -0.0026
    node value (that needs #532's full traveling-wave time-domain dynamics)."""
    from scripts.vol_1_foundations.ring_bondframe_probe import (
        measure_ring,
        open_chain_strain_profile,
    )
    pinned = open_chain_strain_profile(n_nodes=200, n_phase=16, relax_iter=6000, free_end=False)
    free = open_chain_strain_profile(n_nodes=200, n_phase=16, relax_iter=6000, free_end=True)
    # the free end has a LARGE position gradient; the pinned end is nearly uniform
    assert free["position_gradient"] > 10 * pinned["position_gradient"], (
        "free-end open chain should be far more position-dependent than pinned")
    # boundary config MATTERS (whole-chain mean differs materially) — the artifact
    assert abs(free["mean_A_whole_chain"] - pinned["mean_A_whole_chain"]) > COLD_BAND / 3
    # CONTRAST: the ring is uniform (position gradient ~ machine zero in the mean strain)
    r = measure_ring(n_nodes=120, n_phase=16, relax_iter=6000)
    assert r["cyclemean_dx"] == pytest.approx(1.0, abs=1e-9)   # ring: no boundary freedom


# ═════════════════════════════════════════════════════════════════════════════
# PART 4(c/d) — #518 legs INTACT, and the cycle-mean-COLD consistency (structural)
# ═════════════════════════════════════════════════════════════════════════════
def test_dc_only_leaves_518_null_intact():
    """RECONCILIATION (c): [DC-ONLY-DERIVED] touches NEITHER #518 leg. The bond-frame
    content is COLD, consistent with the null; no revision to the field-mean leg or the
    channel-symmetry leg is warranted. Encoded as: the derived DC deposit is 0."""
    assert pred.bondframe_deposit_predicted() == 0.0
    # and the AC scalar <T> being nonzero does NOT constitute a stiffness deposit (the
    # distinction that #532's re-analysis established: <A_bond> lives in the AC snapshot)
    assert pred.slot_tension_scalar() > 0                    # AC scalar nonzero
    assert pred.bondframe_deposit_predicted() == 0.0         # DC deposit still zero


@pytest.mark.engine_sim
def test_reconciliation_d_ring_reproduces_532_cyclemean_cold():
    """RECONCILIATION (d): the ring REPRODUCES #532's cycle-mean-COLD reading (0.9973
    on the open chain) and PROMOTES it to a theorem — the ring's boundary-free cycle-mean
    config still reads COLD, so the COLD result is forced, not a boundary observation."""
    from scripts.vol_1_foundations.ring_bondframe_probe import measure_ring
    r = measure_ring(n_nodes=120, n_phase=24, relax_iter=6000)
    # #532 open-chain read 0.9973; the ring reads 1.0000 (cleaner — boundary removed)
    assert abs(r["cyclemean_bondframe_k_ratio"] - 1.0) < COLD_BAND
    assert r["cyclemean_bondframe_k_ratio"] >= 0.997 - COLD_BAND   # not below the #532 floor


# ═════════════════════════════════════════════════════════════════════════════
# THE #528 RECONCILE-GATE — symbolic vs numeric-ring, INDEPENDENT paths, can-fire proven
# ═════════════════════════════════════════════════════════════════════════════
@pytest.mark.engine_sim
def test_reconcile_gate_tilt_symbolic_vs_ring():
    """Reconcile the SYMBOLIC tilt (bondframe_tslot_predictions) against the NUMERIC-ring
    tilt (ring_bondframe_probe) — two INDEPENDENT code paths. The gate can-fire self-test
    runs FIRST (proves the halt plumbing is live), then reconciles. Band = the derived
    tilt band (ring-commensurate-k snap + phase discretization)."""
    from scripts.vol_1_foundations.ring_bondframe_probe import measure_ring
    ring_tilt = measure_ring(n_nodes=120, n_phase=24, relax_iter=6000)["tilt"]
    symbolic_tilt = pred.tilt_exact()
    # the ring snaps k to a commensurate value; band covers the k-snap + phase residual
    ReconcileGate(
        label="tilt_symbolic_vs_ring",
        claimed=ring_tilt,
        independent=symbolic_tilt,
        rtol=0.06, atol=0.0,        # ring-commensurate-k snap (~4%) + phase residual
    ).enforce()   # can-fire proven first (default), then the live reconcile


def test_reconcile_gate_can_fire_on_dropped_term():
    """PROVE the gate FIRES on a DROPPED-TERM synthetic (claim = cold=0 vs the real
    nonzero tilt) — on the real comparator + halt path. Retires the #521/#526/#527
    dead-gate class."""
    with pytest.raises(DiscrepantHalt):
        ReconcileGate(
            label="dropped_term_synthetic",
            claimed=0.0,                        # dropped the whole tilt (claim cold)
            independent=pred.tilt_exact(),      # the real nonzero tilt
            rtol=TILT_BAND_FRAC, atol=0.0,
        ).enforce(prove_first=False)


def test_reconcile_gate_can_fire_on_sign_flip():
    """PROVE the gate FIRES on a SIGN-FLIP synthetic (claim = -tilt vs +tilt)."""
    with pytest.raises(DiscrepantHalt):
        ReconcileGate(
            label="sign_flip_synthetic",
            claimed=-pred.tilt_exact(),         # flipped sign
            independent=pred.tilt_exact(),
            rtol=TILT_BAND_FRAC, atol=0.0,
        ).enforce(prove_first=False)


def test_reconcile_gate_prove_can_fire_self_test():
    """The gate's own can-fire self-test passes (the plumbing is live). A vacuous-band
    gate would raise DeadGateError; this asserts the LIVE gate proves reachability."""
    res = ReconcileGate(
        label="live_tilt_gate",
        claimed=pred.tilt_exact(),
        independent=pred.tilt_exact(),
        rtol=TILT_BAND_FRAC, atol=0.0,
    ).prove_can_fire()
    assert res.can_fire_proven is True


def test_reconcile_gate_refuses_vacuous_band():
    """A gate with an infinite/NaN tolerance is refused at registration (a vacuous band
    is a checklist by construction). This is the #531 no-vacuous-band discipline."""
    with pytest.raises(ValueError):
        ReconcileGate(label="vacuous", claimed=1.0, independent=1.0, rtol=float("inf"))


# ═════════════════════════════════════════════════════════════════════════════
# THE VERDICT BIN SELECTOR — no fall-through else; the DC-ONLY theorem is the verdict
# ═════════════════════════════════════════════════════════════════════════════
def test_bin_selector_dc_only_verdict():
    """The frozen bin selector returns [DC-ONLY-DERIVED] for the derived content, with a
    loud DISCREPANT-HALT (not a silent benign default) on internal contradiction."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import classify_bin
    binv = classify_bin(
        tilt_reproduces_532=True,
        bondframe_deposit=0.0,
        cold_band=COLD_BAND,
        N_convergent=True,
    )
    assert binv == "DC-ONLY-DERIVED"


def test_bin_selector_halts_on_bad_tilt():
    """If the derived tilt does NOT reproduce #532 (the validation gate fails), the bin
    selector HALTs (no verdict) — not a silent DC-ONLY default."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import BinHalt, classify_bin
    with pytest.raises(BinHalt):
        classify_bin(tilt_reproduces_532=False, bondframe_deposit=0.0,
                     cold_band=COLD_BAND, N_convergent=True)


def test_bin_selector_bulk_deposit_path_reachable():
    """A nonzero, N-convergent bond-frame deposit routes [BULK-DEPOSIT-DERIVED] — proving
    the DC-ONLY verdict is not a dead-end default (the path could have gone the other way)."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import classify_bin
    binv = classify_bin(tilt_reproduces_532=True, bondframe_deposit=0.02,
                        cold_band=COLD_BAND, N_convergent=True)
    assert binv == "BULK-DEPOSIT-DERIVED"


def test_bin_selector_constraint_dependent_path_reachable():
    """A deposit that is NOT N-convergent routes [CONSTRAINT-DEPENDENT] — the boundary
    question. Also a reachable non-default path."""
    from scripts.vol_1_foundations.bondframe_tslot_predictions import classify_bin
    binv = classify_bin(tilt_reproduces_532=True, bondframe_deposit=0.02,
                        cold_band=COLD_BAND, N_convergent=False)
    assert binv == "CONSTRAINT-DEPENDENT"
