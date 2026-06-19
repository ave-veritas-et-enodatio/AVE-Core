"""STAGE 2/3 gate tests for the graded-vacuum-network ISOLATION eigensolver.

Prereg: research/2026-06-19_electron-Q-coupled-network_prereg.md (commit 4ae50ba0).
Result: research/2026-06-19_electron-Q-coupled-network_result.md.

═══════════════════════════════════════════════════════════════════════════════
THE FROZEN-BIN OUTCOME (BRUTAL HONESTY -- Rule 11 honest closure)
═══════════════════════════════════════════════════════════════════════════════
GATE1 (MANDATORY validate-on-known): Q_isolation in [20,45]  ->  **FAIL**.
  The native eigenmode Q is LOSSLESS-CONFINED: Q >> 45, GROWING toward infinity
  with resolution (N=24->1.8e5, N=32->1.2e8, N=48->1.1e13). It is NOT ~137
  (no alpha leak -- proven alpha-invariant), NOT ~3 (no solver bug -- the bound
  mode is gapped, discrete, localised). It is a THIRD mode the prereg did not
  enumerate: the lossless-reactive standing-mode limit (Q->inf).

  ROOT CAUSE (single mechanism, Rule 11): the eigenmode-Q and the cold-cage
  time-domain ringdown-Q are DIFFERENT OBSERVABLES. The eigenmode is the intrinsic
  radiative linewidth of the confined mode; the matched EM port at the box boundary
  captures essentially no energy (port_frac -> 0 as the mu-load-short wall deepens),
  so Q -> inf. The cold-cage "Q_ringdown = 30.75" is a driven finite-grid ringdown
  (transient shedding + continuum coupling + Hilbert-envelope fit), NOT the intrinsic
  eigenmode linewidth. So the validate-on-known cross-check (reproduce ~30.8) is NOT
  satisfiable in the eigenframe -- not because of a leak, but because the two Qs are
  not the same quantity. This HALTS Build-A per the prereg (do NOT push to Build-B).

GATE2 (lossless, EM port CLOSED): Q=inf  ->  **PASS** (Q=1.4e16, Im(omega)=4e-17).
GATE4 (Nyquist / gapped / shear branch): **PASS** (omega_re>0 gapped; the cold-cage
  cross-check gives omega*dt=0.0157 << pi; vector/shear branch PSD-resolved).
anti-coincidence: Q != Z_RADIATION=29.98  ->  **PASS** (open-port Q ~ 1.8e5, computed).
alpha-free (grep + alpha->2alpha): **PASS** (|dQ/Q| = 2e-10 under alpha->2alpha).

These tests ASSERT the documented outcomes (the FAIL is a pinned scientific result,
not a relaxed bin). Re-tuning to force Q into [20,45] would be debugging-toward-a-
rescue (Rule 11 wrong-reaction) -- the lossless-confined Q is the honest finding.
"""

import numpy as np
import pytest

from ave.solvers.graded_vacuum_network import (
    IsolationConfig,
    saturation_kernel,
    solve_isolation_Q_sparse,
)

# Cold-cage isolation inputs (validate-on-known geometry, reduced N for tractable eig).
_COLD = dict(frac=0.9, S_min=1e-3, sigma_port=2.0)


def _cfg(N, exponent=0.5, em_closed=False):
    return IsolationConfig(
        N=N, sigma=N / 9.0, exponent=exponent, port_thickness=max(3, N // 12),
        em_port_closed=em_closed, **_COLD,
    )


# ─────────────────────────────────────────────────────────────────────────────
# GATE1 -- MANDATORY validate-on-known. Pinned outcome: FAIL (lossless-confined).
# ─────────────────────────────────────────────────────────────────────────────


def test_gate1_isolation_Q_is_lossless_confined_not_in_band():
    """GATE1 FAIL (pinned): the native eigen-Q is >> 45 (lossless-confined), NOT in
    the validate-on-known band [20,45], NOT ~137, NOT ~3. This is the honest
    discriminating-test outcome -- the eigenmode-Q is a different observable from the
    cold-cage ringdown-Q (which is 30.75)."""
    r = solve_isolation_Q_sparse(_cfg(24), omega_guess=2.87)
    assert r["ok"]
    Q = r["Q"]
    # gapped, discrete, localised bound mode (NOT the bin-1 ~3 artifact, NOT 137):
    assert r["omega_re"] > 0.1, "bound mode not gapped"
    assert r["core_frac"] > 0.5, "mode not localised on the core (solver/selection bug)"
    assert not (2.0 < Q < 4.0), f"Q in the bin-1-artifact band ~3 (solver bug): {Q}"
    assert not (117.0 < Q < 157.0), f"Q ~ 137 -- an alpha-leak would land here: {Q}"
    # the pinned outcome: Q is WAY above the [20,45] band (lossless-confined).
    assert Q > 45.0, f"GATE1 outcome moved: Q={Q} is now in/below band (re-run the prereg adjudication)"


def test_gate1_Q_grows_with_resolution_lossless_limit():
    """The eigen-Q GROWS with N (the lossless-confined limit): better resolution
    => less geometric leak => higher Q. Witnesses the mechanism, NOT a fixed Q."""
    q24 = solve_isolation_Q_sparse(_cfg(24), omega_guess=2.87)["Q"]
    q32 = solve_isolation_Q_sparse(_cfg(32), omega_guess=2.87)["Q"]
    assert q32 > q24 > 45.0, f"Q did not grow with resolution: N24={q24}, N32={q32}"


# ─────────────────────────────────────────────────────────────────────────────
# GATE2 -- lossless: EM port CLOSED => Q = inf.
# ─────────────────────────────────────────────────────────────────────────────


def test_gate2_closed_port_is_lossless():
    """GATE2 PASS: with the EM port CLOSED (Gamma_EM=-1, all confined), the operator
    is Hermitian => Im(omega)=0 => Q=inf. Loss enters ONLY via the matched port."""
    r = solve_isolation_Q_sparse(_cfg(24, em_closed=True), omega_guess=2.87)
    assert r["ok"]
    assert r["omega_im"] < 1e-10, f"closed port not lossless: Im(omega)={r['omega_im']}"
    assert r["Q"] > 1e9, f"closed-port Q not ~inf: {r['Q']}"


# ─────────────────────────────────────────────────────────────────────────────
# GATE4 -- Nyquist / gapped bound mode / shear branch resolved.
# ─────────────────────────────────────────────────────────────────────────────


def test_gate4_bound_mode_gapped_and_peaked():
    """GATE4 PASS: the bound mode is gapped (omega_re>0) and localised (peak bin>1
    analogue = core-localised, not the bin-1 DC artifact)."""
    r = solve_isolation_Q_sparse(_cfg(24), omega_guess=2.87)
    assert r["omega_re"] > 0.1, "mode not gapped"
    assert r["core_frac"] > r["port_frac"], "mode not interior-localised (peak at boundary)"


# ─────────────────────────────────────────────────────────────────────────────
# anti-coincidence (DEC-5): Q is computed dynamics, NOT a silent Z_RADIATION=29.98.
# ─────────────────────────────────────────────────────────────────────────────


def test_anti_coincidence_Q_is_not_Z_radiation():
    """DEC-5 anti-coincidence: confirm the solver computes Q from the dynamics and is
    NOT silently the constant Z_RADIATION = Z_0/(4pi) = 29.98 (which sits in the
    [20,45] band). The open-port Q is ~1e5, nowhere near 29.98."""
    r = solve_isolation_Q_sparse(_cfg(24), omega_guess=2.87)
    assert abs(r["Q"] - 29.98) > 1.0, f"Q suspiciously == Z_RADIATION 29.98: {r['Q']}"


# ─────────────────────────────────────────────────────────────────────────────
# alpha-INVARIANCE (CHORD-bin item 3) -- the STRONGEST gate. Pure mechanism check.
# ─────────────────────────────────────────────────────────────────────────────


def test_alpha_to_2alpha_invariance():
    """CHORD-bin item 3 / the strongest gate: doubling ALPHA in constants and
    re-solving must leave Q UNCHANGED (the network uses only alpha-free ratios; RHO_BULK
    cancels). |dQ/Q| ~ 0. (Here the outcome is moot for the CHORD because GATE1 failed,
    but the invariance is the load-bearing proof that there is NO alpha-leak.)"""
    import importlib

    import ave.core.constants as C
    import ave.solvers.graded_vacuum_network as G

    q1 = G.solve_isolation_Q_sparse(G.IsolationConfig(N=20, sigma=20 / 9.0, port_thickness=3, **_COLD), omega_guess=2.87)["Q"]
    saved = C.ALPHA
    try:
        C.ALPHA = 2.0 * saved
        importlib.reload(G)
        q2 = G.solve_isolation_Q_sparse(G.IsolationConfig(N=20, sigma=20 / 9.0, port_thickness=3, **_COLD), omega_guess=2.87)["Q"]
    finally:
        C.ALPHA = saved
        importlib.reload(G)
    rel = abs(q2 - q1) / abs(q1)
    assert rel < 1e-6, f"alpha-LEAK: Q moved under alpha->2alpha by |dQ/Q|={rel}"


# ─────────────────────────────────────────────────────────────────────────────
# DEC-1 -- exponent robustness (sqrt(S) primary, S^{1/4} sensitivity).
# ─────────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("exponent", [0.5, 0.25])
def test_dec1_gate1_fail_robust_to_op14_exponent(exponent):
    """DEC-1: the GATE1 lossless-confined FAIL holds for BOTH Op14 exponents
    (sqrt(S) primary AND S^{1/4} sensitivity) -- Q >> 45 for both."""
    r = solve_isolation_Q_sparse(_cfg(24, exponent=exponent), omega_guess=2.87)
    assert r["ok"]
    assert r["Q"] > 45.0, f"exponent={exponent}: Q={r['Q']} unexpectedly in/below band"


def test_saturation_kernel_both_exponents_alpha_free():
    """The Op14 kernel S(A)=(1-A^2)^p is alpha-free for both p; clipped to [S_min,1]."""
    A = np.linspace(0, 0.999, 50)
    for p in (0.5, 0.25):
        S = saturation_kernel(A, exponent=p, S_min=1e-3)
        assert S.min() >= 1e-3 - 1e-12 and S.max() <= 1.0 + 1e-12
        assert np.all(np.diff(S) <= 1e-12), "kernel not monotone decreasing in A"
