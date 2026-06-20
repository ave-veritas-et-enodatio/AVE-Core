"""Tests for the charge-quantization structural gate (#43, GATE #2).

Validates the rigorous boundary topological charge 𝒬 = Link(∂Ω, F) built in
`ave.topological.charge_quantization`:

  - VALIDATE-ON-KNOWN anchors: ω≡0 null → 𝒬=0; planted (2,3) → 𝒬=3.
  - The Gauss linking integrator on KNOWN curves (Hopf link → ±1, unlinked → 0,
    orientation-reversal → sign flip).
  - The full gate verdict = PASS (integer + equals winding + robust under
    continuous deformation + jumps on topology change).
  - 𝒬 is amplitude-INDEPENDENT (not an amplitude-count artifact).
  - 𝒬's SIGN is the chirality (RH → +, LH → −).
  - FALSIFIABILITY: a STRONG deformation eventually unwinds 𝒬 in discrete steps
    (the invariance at gate strengths is real topological protection, not a
    numerically-frozen readout).
  - The Moffatt helicity = linking cross-check: self-linking = w_tor·w_pol = p·q.
  - GUARD 1 value-echo immunity: ALPHA / Q_TANK / e_charge absent from globals.

Prereg: research/2026-06-19_charge-quantization-gate_prereg.md
"""

import numpy as np
import pytest

from ave.topological.charge_quantization import (
    _gauss_linking_integral,
    charge_quantization_gate,
    compute_F_curl,
    compute_Q_hopf,
    compute_Q_link,
    deform_continuous,
    seed_pq_winding,
    unwind_topology,
)

N = 32
R = 7.0
R_MINOR = 2.3


# ──────────────────────────────────────────────────────────────────────────
# Gauss linking integrator — validated on KNOWN curves
# ──────────────────────────────────────────────────────────────────────────


def _circle(center, plane_axes, normal_axis, radius=1.0, n=300):
    t = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    pts = np.zeros((n, 3))
    pts[:, plane_axes[0]] = center[plane_axes[0]] + radius * np.cos(t)
    pts[:, plane_axes[1]] = center[plane_axes[1]] + radius * np.sin(t)
    pts[:, normal_axis] = center[normal_axis]
    return pts


def test_gauss_linking_hopf_link_is_plus_minus_one():
    """KNOWN-POSITIVE: a genuine Hopf link has |Lk| = 1."""
    t = np.linspace(0.0, 2.0 * np.pi, 300, endpoint=False)
    C1 = np.stack([np.cos(t), np.sin(t), 0 * t], axis=1)
    C2 = np.stack([1.0 + np.cos(t), 0 * t, np.sin(t)], axis=1)
    lk = _gauss_linking_integral(C1, C2)
    assert abs(abs(lk) - 1.0) < 1e-2, f"Hopf link Lk={lk} should be ±1"


def test_gauss_linking_unlinked_is_zero():
    """KNOWN-NEGATIVE: far-apart circles are unlinked → Lk = 0."""
    t = np.linspace(0.0, 2.0 * np.pi, 300, endpoint=False)
    C1 = np.stack([np.cos(t), np.sin(t), 0 * t], axis=1)
    C3 = np.stack([5.0 + np.cos(t), 0 * t, np.sin(t)], axis=1)
    lk = _gauss_linking_integral(C1, C3)
    assert abs(lk) < 1e-2, f"unlinked Lk={lk} should be 0"


def test_gauss_linking_orientation_reversal_flips_sign():
    """Reversing one curve's orientation flips the linking sign."""
    t = np.linspace(0.0, 2.0 * np.pi, 300, endpoint=False)
    C1 = np.stack([np.cos(t), np.sin(t), 0 * t], axis=1)
    C2 = np.stack([1.0 + np.cos(t), 0 * t, np.sin(t)], axis=1)
    lk = _gauss_linking_integral(C1, C2)
    lk_rev = _gauss_linking_integral(C1, C2[::-1])
    assert np.sign(lk) == -np.sign(lk_rev), "orientation reversal must flip sign"


# ──────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN anchors (the gate's HALT poles)
# ──────────────────────────────────────────────────────────────────────────


def test_known_negative_null_gives_zero_charge():
    """KNOWN-NEGATIVE anchor: unstrained vacuum ω≡0 → 𝒬 = 0."""
    omega_null = np.zeros((N, N, N, 3), dtype=np.float64)
    q = compute_Q_link(omega_null, R, R_MINOR)
    assert q["Q_link"] == 0
    assert q["Q_link_raw"] == 0.0


def test_known_positive_planted_recovers_winding_integer():
    """KNOWN-POSITIVE anchor: planted (2,3) → 𝒬 (poloidal linking) = 3."""
    omega = seed_pq_winding(N, 2, 3, R, R_MINOR)
    q = compute_Q_link(omega, R, R_MINOR)
    assert q["Q_link"] == 3
    assert abs(q["Q_link_raw"] - 3.0) < 0.25
    assert q["w_tor"] == 2  # toroidal winding recovers p = 2
    assert q["sign"] == 1


def test_flux_field_F_curl_omega_is_nontrivial():
    """F = curl ω is non-vanishing where the planted winding lives."""
    omega = seed_pq_winding(N, 2, 3, R, R_MINOR)
    F = compute_F_curl(omega)
    assert np.abs(F).max() > 1e-6


# ──────────────────────────────────────────────────────────────────────────
# Charge is an INTEGER and INDEPENDENT of amplitude (not an amplitude count)
# ──────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("amplitude", [0.1, 0.5, 1.0, 3.0])
def test_charge_is_amplitude_independent(amplitude):
    """𝒬 does NOT track the planted amplitude → not an amplitude-count artifact."""
    omega = seed_pq_winding(N, 2, 3, R, R_MINOR, amplitude_scale=amplitude)
    q = compute_Q_link(omega, R, R_MINOR)
    assert q["Q_link"] == 3, f"𝒬 changed with amplitude {amplitude}"


@pytest.mark.parametrize("p,q_pol,expect_hopf", [(1, 1, 1), (2, 3, 6), (1, 2, 2), (3, 2, 6)])
def test_charge_counts_the_actual_winding_integer(p, q_pol, expect_hopf):
    """𝒬 reads the actual (p, q) winding; self-linking = w_tor·w_pol = p·q."""
    omega = seed_pq_winding(N, p, q_pol, R, R_MINOR)
    link = compute_Q_link(omega, R, R_MINOR)
    hopf = compute_Q_hopf(omega, R, R_MINOR)
    assert link["Q_link"] == q_pol
    assert link["w_tor"] == p
    assert hopf["Q_hopf"] == expect_hopf  # Moffatt helicity = linking


# ──────────────────────────────────────────────────────────────────────────
# SIGN = chirality (the charge sign)
# ──────────────────────────────────────────────────────────────────────────


def test_charge_sign_tracks_chirality():
    """RH winding → 𝒬 = +3; LH winding → 𝒬 = −3 (the charge sign)."""
    q_rh = compute_Q_link(seed_pq_winding(N, 2, 3, R, R_MINOR), R, R_MINOR)
    q_lh = compute_Q_link(seed_pq_winding(N, 2, -3, R, R_MINOR), R, R_MINOR)
    assert q_rh["Q_link"] == 3 and q_rh["sign"] == 1
    assert q_lh["Q_link"] == -3 and q_lh["sign"] == -1


# ──────────────────────────────────────────────────────────────────────────
# TOPOLOGICAL PROTECTION (the load-bearing Stage-2 demonstration)
# ──────────────────────────────────────────────────────────────────────────


@pytest.mark.parametrize("kind,strength", [
    ("smooth_noise", 0.15), ("local_scale", 0.25), ("swirl", 0.20), ("warp", 0.30),
])
def test_charge_invariant_under_continuous_deformation(kind, strength):
    """𝒬 is INVARIANT under continuous topology-preserving deformation."""
    omega = seed_pq_winding(N, 2, 3, R, R_MINOR)
    Q0 = compute_Q_link(omega, R, R_MINOR)["Q_link"]
    om_def = deform_continuous(omega, kind, strength, seed=7)
    Qd = compute_Q_link(om_def, R, R_MINOR)["Q_link"]
    assert Qd == Q0 == 3, f"{kind}@{strength}: 𝒬 {Q0}→{Qd} under continuous deform"


def test_charge_jumps_on_topology_change_unwind():
    """The topology-CHANGING unwind makes 𝒬 jump to 0 (amplitude preserved)."""
    omega = seed_pq_winding(N, 2, 3, R, R_MINOR)
    Q0 = compute_Q_link(omega, R, R_MINOR)["Q_link"]
    om_unwound = unwind_topology(omega, R, R_MINOR)
    Qu = compute_Q_link(om_unwound, R, R_MINOR)["Q_link"]
    # amplitude/energy preserved by the unwind (envelope re-laid at constant phase)
    e0 = float(np.sum(omega[..., 0] ** 2 + omega[..., 1] ** 2))
    eu = float(np.sum(om_unwound[..., 0] ** 2 + om_unwound[..., 1] ** 2))
    assert Q0 == 3 and Qu == 0, f"unwind: 𝒬 {Q0}→{Qu} (must jump to 0)"
    assert abs(eu - e0) / e0 < 1e-9, "unwind must preserve the |ω_⊥| energy budget"


def test_strong_deformation_eventually_unwinds_charge():
    """FALSIFIABILITY: a STRONG deformation DOES break 𝒬 in discrete steps.

    The invariance at gate strengths is real topological protection — NOT a
    numerically-frozen readout. A sufficiently strong perturbation actually cuts
    the winding and 𝒬 steps down 3→2→1→0, confirming the readout CAN change —
    and changes ONLY in integer steps (never a continuous drift). This is the
    load-bearing "a frozen readout could not do this" evidence; it is CI-gated
    here so the headline "discrete steps" claim cannot silently rot.

    Seed/strengths reproduce the result-doc quote (smooth_noise seed=1):
    0.5→3, 1.0→2, 2.0→1, 5.0→0, 10.0→0.
    """
    omega = seed_pq_winding(N, 2, 3, R, R_MINOR)
    strengths = [0.5, 1.0, 2.0, 5.0, 10.0]  # the result-doc's quoted sweep
    Qs = [
        compute_Q_link(deform_continuous(omega, "smooth_noise", s, seed=1), R, R_MINOR)["Q_link"]
        for s in strengths
    ]
    # 1. starts at the topological integer, ends fully unwound
    assert Qs[0] == 3, f"weak deformation preserves topology, got {Qs}"
    assert Qs[-1] == 0, f"strongest deformation must fully unwind, got {Qs}"
    # 2. MONOTONE non-increasing across the sweep (steps DOWN, never back up)
    assert all(Qs[i + 1] <= Qs[i] for i in range(len(Qs) - 1)), (
        f"𝒬 must be non-increasing under increasing deformation, got {Qs}"
    )
    # 3. passes through at least 2 DISTINCT integer values before reaching 0
    #    (3→2→1→0 = a discrete step-down ladder, not a single 3→0 cliff that a
    #    frozen/binary readout could fake)
    distinct_before_zero = sorted(set(q for q in Qs if q != 0))
    assert len(distinct_before_zero) >= 2, (
        f"step-down must pass through ≥2 distinct integers before 0, got {Qs}"
    )


# ──────────────────────────────────────────────────────────────────────────
# Full gate verdict
# ──────────────────────────────────────────────────────────────────────────


def test_full_gate_verdict_is_pass():
    """End-to-end gate: VERDICT = PASS (all four conditions met)."""
    result = charge_quantization_gate()
    assert result["verdict"] == "PASS", result.get("verdict_detail", result)
    cond = result["pass_conditions"]
    assert cond["is_integer"]
    assert cond["equals_planted_winding"]
    assert cond["robust_under_continuous_deformation"]
    assert cond["jumps_on_topology_change"]
    # known anchors held (no HALT)
    assert result["known_negative_null"]["Q_link"] == 0
    assert result["known_positive_planted"]["Q_link"] == 3
    assert result["known_positive_planted"]["Q_hopf_selflink"] == 6


# ──────────────────────────────────────────────────────────────────────────
# GUARD 1 — value-echo immunity (read only the integer + sign, never -e / α)
# ──────────────────────────────────────────────────────────────────────────


def test_guard_value_echo_immunity_no_alpha_or_e_in_globals():
    """Forbidden value-echo names are ABSENT from the module globals (GUARD 1).

    Widened (2026-06-19) beyond the original (ALPHA, Q_TANK, e_charge, E_CHARGE)
    to cover the docstring's full stated intent ("NEVER read α/m_e/137"):
    kappa_chiral / V_SNAP / m_e and case variants.
    """
    import ave.topological.charge_quantization as cq

    g = vars(cq)
    for name in (
        "ALPHA", "Q_TANK", "e_charge", "E_CHARGE",
        "kappa_chiral", "KAPPA_CHIRAL", "V_SNAP",
        "MASS_ELECTRON", "m_e", "M_E",
    ):
        assert name not in g, f"value-echo leak: {name} in charge_quantization globals"


def test_guard_no_alpha_literal_in_verdict_code_path():
    """The α value (137 / 0.00729) does NOT appear in the verdict-determining
    code path (source-level guard, GUARD 1 widened 2026-06-19)."""
    import inspect

    import ave.topological.charge_quantization as cq

    code_path = (
        inspect.getsource(cq.charge_quantization_gate)
        + inspect.getsource(cq.compute_Q_link)
        + inspect.getsource(cq.compute_Q_hopf)
    )
    for lit in ("137", "0.00729"):
        assert lit not in code_path, f"α-literal {lit!r} leaked into verdict code path"
    # the import-time guard must have run (helper present + callable)
    assert callable(cq._assert_no_alpha_literal_in_code_path)


def test_guard_module_does_not_import_constants():
    """The module imports tetrahedral operators only — NOT ave.core.constants."""
    import inspect

    import ave.topological.charge_quantization as cq

    src = inspect.getsource(cq)
    # the only mentions of ALPHA/e_charge are in the forbidden-list + docstrings;
    # there must be NO import of ave.core.constants.
    assert "ave.core.constants" not in src
    assert "from ave.core import" not in src
