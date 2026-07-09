"""Standing tests for the CHIRAL-DRIVE SELF-ORBIT harness (Task #22).

Live-fire regression of the curl-vs-gradient discriminator built in
`ave.solvers.chiral_drive_selforbit`. Re-derives (does NOT read a committed JSON):

  - GEOMETRY: the (2,3) knot embedding does not self-intersect in 3-D.
  - GAUGE: the curl bias has Wilson loop ∮θ=Φ; the gradient bias has ∮θ=0 at
    EQUAL per-link magnitude (a genuine pure gauge).
  - DISCRIMINATOR: the curl flux drives a persistent circulation; the gradient
    (pure gauge) does NOT (ratio ≫ 1e6). The kill-test.
  - LOSSLESS: the Cayley/CN evolution is unitary — H-drift + norm-drift ≪ 1e-8
    (no damping term exists in the scheme).
  - EMERGENT-not-PLANTED: the static seed carries zero circulation at flux-off.
  - BIAS-OFF NULL (liveness): Φ=0 ⇒ circulation and mismatch ≈ 0.
  - RATE ∝ FLUX: the uniform-seed persistent current == 2t·sin(Φ/N) exactly.
  - MASS OBSERVABLE: the circulation energy tracks the DC inter-node mismatch via
    E_circ ∝ M² (kinetic-from-circulation).
  - VERDICT: CHIRAL-DRIVE-VIABLE at the frozen scale.

Prereg: research/2026-07-08_chiral-drive-selforbit_prereg.md
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.solvers.chiral_drive_selforbit import (
    ChiralDriveConfig,
    chiral_drive_gate,
    evolve,
    loop_flux,
    peierls_link_phases,
    torus_knot_positions,
)

FAST = ChiralDriveConfig(N=32, n_steps=900, dt=0.02)


def _cfg(**kw) -> ChiralDriveConfig:
    d = dict(FAST.__dict__)
    d.update(kw)
    return ChiralDriveConfig(**d)


# ── Geometry ────────────────────────────────────────────────────────────────


def test_torus_knot_embedding_no_selfintersection():
    pos = torus_knot_positions(FAST)
    # min pairwise distance between non-adjacent nodes stays well above 0 (a
    # genuine (2,3) knot does not cross itself in 3-D).
    N = FAST.N
    dmin = np.inf
    for i in range(N):
        for j in range(i + 2, N):
            if (i, j) == (0, N - 1):
                continue
            dmin = min(dmin, float(np.linalg.norm(pos[i] - pos[j])))
    assert dmin > 0.1


# ── Gauge: curl vs gradient Wilson loop ──────────────────────────────────────


def test_curl_is_flux_gradient_is_pure_gauge():
    Phi = np.pi
    theta_curl = peierls_link_phases(_cfg(bias="curl", flux=Phi))
    theta_grad = peierls_link_phases(_cfg(bias="gradient", flux=Phi))
    # equal per-link magnitude
    assert np.allclose(np.abs(theta_curl), np.abs(theta_grad))
    # only the loop sum differs
    assert loop_flux(theta_curl) == pytest.approx(Phi, abs=1e-12)
    assert loop_flux(theta_grad) == pytest.approx(0.0, abs=1e-12)


# ── The discriminator (kill-test) ────────────────────────────────────────────


def test_curl_drives_gradient_does_not():
    Phi = np.pi
    curl = evolve(_cfg(bias="curl", flux=Phi, seed_kind="localized"))
    grad = evolve(_cfg(bias="gradient", flux=Phi, seed_kind="localized"))
    assert abs(curl["C_dc"]) > 1e-3  # curl drives a real circulation
    assert abs(grad["C_dc"]) < 1e-9  # pure gauge cannot
    assert abs(curl["C_dc"]) > 1e6 * max(abs(grad["C_dc"]), 1e-15)


# ── Lossless (Ax3): no damping term exists in the Cayley scheme ───────────────


def test_lossless_no_hidden_damping():
    curl = evolve(_cfg(bias="curl", flux=np.pi, seed_kind="localized"))
    assert curl["h_drift"] < 1e-8
    assert curl["norm_drift"] < 1e-8


# ── Anti-tautology: emergent, not planted; bias-off null ─────────────────────


def test_emergent_not_planted():
    curl = evolve(_cfg(bias="curl", flux=np.pi, seed_kind="localized"))
    # the seed carries ZERO circulation with the flux OFF (a static loop at rest)
    assert abs(curl["seed_circulation_fluxoff"]) < 1e-9


def test_bias_off_null_liveness():
    off = evolve(_cfg(bias="off", flux=0.0, seed_kind="localized"))
    assert abs(off["C_dc"]) < 1e-9
    assert abs(off["M_dc"]) < 1e-9


# ── Rate ∝ flux: the exact persistent-current anchor ─────────────────────────


def test_rate_set_by_flux_uniform_anchor():
    for Phi in (0.5, 1.0, 2.0):
        uni = evolve(_cfg(bias="curl", flux=Phi, seed_kind="uniform"))
        expected = 2.0 * FAST.t_hop * np.sin(Phi / FAST.N)
        assert uni["C_dc"] == pytest.approx(expected, abs=1e-9)


# ── Mass observable: E_circ ∝ M² ─────────────────────────────────────────────


def test_mass_observable_square_law():
    res = chiral_drive_gate(
        FAST, flux_ref=np.pi, flux_sweep=tuple(np.linspace(0.0, 2.0 * np.pi, 6))
    )
    a4 = res["arm4_mass_observable"]
    assert a4["E_circ_vs_M_exponent"] == pytest.approx(2.0, abs=0.15)
    assert a4["E_circ_vs_M_r2"] > 0.99
    assert a4["bias_off_null"]


# ── The frozen verdict ───────────────────────────────────────────────────────


def test_verdict_chiral_drive_viable():
    res = chiral_drive_gate(
        FAST, flux_ref=np.pi, flux_sweep=tuple(np.linspace(0.0, 2.0 * np.pi, 6))
    )
    assert res["verdict"] == "CHIRAL-DRIVE-VIABLE"
    at = res["anti_tautology"]
    assert at["emergent_not_planted_localized"]
    assert at["gradient_control_null"]
    assert at["conservative"]
    assert at["bias_off_null"]
