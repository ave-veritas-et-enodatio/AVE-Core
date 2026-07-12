"""Nordtvedt-η acceptance test (engine-derived η, strain-field register).

FROZEN prereg: research/2026-07-11_nordtvedt-eta_prereg_FROZEN.md
(frozen by push BEFORE this driver existed; the EP-CMRR pattern).

SECTOR = A1 dilatation / gravity, sub-yield. The equivalence principle = ONE
identity (energy gravitates exactly as energy resists acceleration — one ledger),
probed here in REGISTER-2: strain-field-distributed energy (the gravitational
binding energy `U_bind = ∫½g|∇ε₁₁|²`, in the substrate strain field, in no knot).
Register-1 (knot / WEP composition) is the EP-CMRR test's domain (#650). The
Nordtvedt parameter η measures whether register-2 energy carries the SAME
identity: `(m_g/m_i − 1) = η·f`, `f = E_grav/E_total = U_bind/(M+U_bind)`.

CLASS = consistency / CERTIFICATION. NO chord mint. Per P10 (below) η=0 is
ENTAILED by the solver's single-T₀₀ Gauss construction; the test CERTIFIES-AND-
EXPOSES the installed gravity ledger's Nordtvedt-status (X36 install-tautology,
`research/2026-07-09_x36-node-bottleneck_result.md:54,89,215`). VALUE = converting
A7's Nordtvedt leg (`_orchestration/2026-07-10_rulings-docket.md`, "A7 · queued")
from a retrieval ASSUMPTION into an engine-CERTIFIED prediction.

INVARIANT-S9/S10: a certification/consistency test — a `sup-`-class simulation,
NEVER an `exp-`. It mints no chord, so (like T0.2/T0.3 in `test_l0_medium.py`) it
has no clm-/def- beneficiary and is tracked by test-id.

P10 (binding, verbatim from the frozen prereg): the solver sources the far field
from a SINGLE energy density T₀₀^total = T₀₀^matter + ½g|∇ε₁₁|². By the discrete
divergence theorem (Gauss) on the native-K4 operator L, the far-field monopole
charge = ∫T₀₀^total = the total energy content, so reading BOTH registers off this
one ledger gives η=0 by construction (CERTIFICATION-class, not a free measurement).
It is still risked-in-principle: the two registers are computed by DIFFERENT routes
(field-operator flux vs energy-functional ledger), and the P11 plant proves the
detector FIRES on a genuine two-ledger coupling (η=ε).

flag-don't-fix — a LATENT #86 DEFECT EXPOSURE (surfaced, NOT resolved; Rule-14 no
engine edit; the engine repair is a SEPARATE named future arc). The binding-deficit
`M_eff = M − U_bind` is the engine's OWN-DESIGNATED inertial/ADM mass
(`backreaction.py:33`), yet its far field provably reads M + U_bind (the +u_field
source ADD, `backreaction.py:303-304`). So the as-built engine's far field disagrees
with its own designated ADM mass at O(2f), and the mixed-register η=2.2792 IS the
engine's current far-field-vs-inertial-mass statement — NOT a free convention choice.
#86's own at-risk checks never reconciled the two (all ratio/shape, sign-agnostic —
`test_grqed_stage3_backreaction.py::test_binding_deficit_subtracts_not_adds` asserts
only the M_eff DEFINITION; `…grqed-stage3-backreaction_result.md:339` admits the
sign-agnosticism); this arc is the FIRST reconciliation and it FAILS at O(2f). The
resolution (★RULED (c) — Grant 2026-07-12, reading his own 2026-06-29 ruling text "the
positive strain energy is not a separate ledger to ADD — it is already accounted in
the down-regulated frequency"): source = REDSHIFT/KOMAR-weighted T₀₀^matter (no
separately-added u_field; the local clock ω√S down-regulates in the well; no
double-count) → the far field then reads the deficit mass, reconciling with M_eff.
The three-way {keep-ADD · bare −u_field (Picard source sign-indefinite, likely
unstable) · ★RULED Komar-weighted} stays recorded (KEEP-BOTH); implementing the ruled
weighting + the #86 gate re-runs + this η re-run = the NAMED + AUTHORIZED follow-on arc
X44, which fires AFTER #651 merges — not this PR (Rule-14).
"""

from __future__ import annotations

import time

import numpy as np
import pytest

from . import _nordtvedt as NV

# ── frozen parameters (from the prereg; NOT tuned to output) ──────────────────
_N = 24
_M_TARGET = 4.0
_SIGMAS = (1.4, 1.8, 2.2, 2.6)
_G_SELF = 1.0
_S_MIN = 1e-3
_RADII = (6, 7, 8, 9)          # enclosing radii for the monopole-plateau read (N=24)
_ETA_TOL = 1e-3                 # certification null; RESOLUTION-LIMITED floor (review R1:
                               # |η| systematic ~5-6.5e-4 at N=32/40; margin ~1.5-2×),
                               # NOT truncation-limited. Banking basis = analytic entailment.
_EPS_PLANT = 0.10             # P11 SYNTHETIC ledger-level injection (not a solver-fed coupling)
_PLANT_TOL = 0.02             # |η_planted − ε| (probe recovered to ~6e-4)
_FLUX_PLATEAU_TOL = 0.05      # monopole radius-independence (outer two radii)
_FLUX_IDENTITY_TOL = 1e-4     # field-side Gauss: flux(R) == source(R)
_MIXED_ETA_MIN = 1.0          # mixed-register pairing gives η≈2.3 (flag teeth)
_LLR_BOUND = 4.4e-4           # imported-observational (LLR Nordtvedt; bin-ii comparator)


def _solve_family() -> list[dict]:
    """Solve the fixed-rest-energy, varying-binding-fraction family ONCE.

    Holds `Σ T₀₀^matter == _M_TARGET` for every member; sweeps σ tight→diffuse so
    only f = U_bind/(M+U_bind) varies (f DERIVED from the solver's own ledger)."""
    Grad, Div = NV.build_grad_div(_N)
    rr = NV.radius_grid(_N)
    mask = NV.interior_mask(_N)
    r_in, r_out = 0.16 * _N, _N / 2.0 - 3
    rows = []
    for sg in _SIGMAS:
        T00 = NV.normalized_blob(_N, sg, _M_TARGET)
        res = NV.solve_config(_N, T00, g_self=_G_SELF, s_min=_S_MIN)
        eps = res["eps11"]
        L = NV.stiffness_operator(_N, eps, Grad, Div, s_min=_S_MIN)
        led = NV.energy_ledger(T00, eps, Grad, g_self=_G_SELF)
        m_g = NV.gravitating_charge_flux(eps, L, mask)
        flux, src = NV.enclosed_flux_vs_radius(eps, L, res["T00_total"], rr, _RADII)
        K, r2 = NV.naive_monopole_K(eps, rr, r_in=r_in, r_out=r_out)
        U = led["U_bind"]
        rows.append(
            {
                "sigma": sg,
                "M": led["M_matter"],
                "U": U,
                "M_eff": led["M_eff"],
                "m_i": led["m_i"],          # ENERGY ledger  = M + U
                "m_g": m_g,                  # FIELD-side flux = Σ_interior(L@ε)
                "f": U / (led["M_matter"] + U),
                "flux": flux,
                "src": src,
                "K": K,
                "r2": r2,
                "converged": bool(res["converged"]),
                "max_A": float(res["max_A"]),
                "Delta_clock": float(res["Delta_clock"]),
                "source_mode": res["source_mode"],
                "T00_src_sum": float(res["T00_total"].sum()),
            }
        )
    return rows


@pytest.fixture(scope="module")
def family() -> list[dict]:
    """Module-scoped: the heavy family solve runs ONCE and is shared across the
    engine_sim leg-tests (the `test-engine` lane is serial by design)."""
    t0 = time.time()
    rows = _solve_family()
    print(f"\n[nordtvedt] family solve ({len(rows)} configs, N={_N}) : {time.time() - t0:.2f}s")
    return rows


# ─────────────────────────────────────────────────────────────────────────────
# LEG-1 — X44 CERTIFICATION: far-field Gauss flux tracks M_eff (ruled Komar source)
# ─────────────────────────────────────────────────────────────────────────────
def test_nordtvedt_leg1_certification_one_ledger(family):
    """LEG-1 [X44 MEASUREMENT] — under ruled Komar source, measure η_mixed =
    slope of (m_g/M_eff − 1) vs f across the family.

    Frozen bins (X44 prereg):
      * (i) RECONCILED: |η_mixed| < _ETA_TOL + plateau + Gauss + weak + Δ_clock MATCH
      * (ii) RECONCILED-PARTIAL: |η_mixed| < _ETA_TOL but Δ_clock mismatch ≥ 30%
      * (iii) UNRECONCILED: |η_mixed| ≥ _ETA_TOL
      * (iv) INSTABILITY: non-convergence / non-contractive

    This gate RECORDS the frozen bin. It does NOT retune √S. Structural
    prerequisites (Gauss identity, monopole plateau, convergence, weak regime)
    still hard-fail if broken — those are install integrity, not reconciliation.
    """
    f = np.array([r["f"] for r in family])
    m_g = np.array([r["m_g"] for r in family])
    M_eff = np.array([r["M_eff"] for r in family])
    U = np.array([r["U"] for r in family])
    dclock = np.array([r["Delta_clock"] for r in family])
    eta = NV.eta_slope(f, m_g / M_eff)

    plateau_ok = True
    identity_ok = True
    for r in family:
        rel_plateau = abs(r["flux"][-1] - r["flux"][-2]) / max(abs(r["flux"][-1]), 1e-30)
        rel_ident = max(
            abs(fl - sc) / max(abs(sc), 1e-30) for fl, sc in zip(r["flux"], r["src"])
        )
        plateau_ok = plateau_ok and (rel_plateau < _FLUX_PLATEAU_TOL)
        identity_ok = identity_ok and (rel_ident < _FLUX_IDENTITY_TOL)
    converged_ok = all(r["converged"] for r in family)
    weak_ok = all(r["max_A"] < 0.2 for r in family)
    assert all(r["source_mode"] == "komar" for r in family)

    rel_clock = np.abs(dclock - U) / np.maximum(U, 1e-30)
    clock_match = bool(np.all(rel_clock < 0.30))

    if abs(eta) < _ETA_TOL and clock_match:
        bin_id = "i_RECONCILED"
    elif abs(eta) < _ETA_TOL:
        bin_id = "ii_RECONCILED_PARTIAL"
    else:
        bin_id = "iii_UNRECONCILED"

    print("\n--- LEG-1 X44 measurement (Komar: flux vs M_eff) ---")
    print(f"  f range (E_grav/E_total)  : [{f.min():.4f}, {f.max():.4f}]")
    for r, rc in zip(family, rel_clock):
        print(
            f"  σ={r['sigma']:.2f} f={r['f']:.4f}  m_g={r['m_g']:.5f}  "
            f"M_eff={r['M_eff']:.5f}  rel={(r['m_g'] - r['M_eff']) / r['M_eff']:+.2e}  "
            f"Δclk/U_rel={rc:.3f}  maxA={r['max_A']:.3f}"
        )
    print(f"  η_mixed (flux/M_eff)      : {eta:+.3e}   (reconcile tol |η| < {_ETA_TOL})")
    print(f"  Δ_clock↔U_bind MATCH(<30%): {clock_match}  max_rel={rel_clock.max():.3f}")
    print(f"  FROZEN BIN                : {bin_id}")

    assert converged_ok, "FAIL [bin iv]: a family member did not converge"
    assert weak_ok, "FAIL [bin iv]: a member left the weak/contractive regime (max A ≥ 0.2)"
    assert identity_ok, "FAIL: field-side flux ≠ ∫T₀₀^src (Gauss broken on native K4)"
    assert plateau_ok, "FAIL: enclosed flux is not a radius-independent monopole"
    # Bin (iii) is a VALID frozen outcome — assert the measurement is O(1), not
    # accidentally near zero after a silent retune. |η| must stay ≥ reconcile tol.
    assert abs(eta) >= _ETA_TOL, (
        f"UNEXPECTED: |η_mixed|={abs(eta):.3e} < {_ETA_TOL} — if reconciliation "
        f"now lands, re-bin to (i)/(ii) and update the result doc; do not leave "
        f"this assert as a false UNRECONCILED keeper"
    )
    assert bin_id == "iii_UNRECONCILED"
    assert not clock_match, "Δ_clock↔U_bind unexpectedly MATCH under current √S form"


def test_nordtvedt_p11_planted_two_ledger_teeth(family):
    """P11 [TEETH — SYNTHETIC injection-recovery] on the live X44 ratio m_g/M_eff.

    Plant ε into the gravitating register: m_g_planted = m_g + ε·U, hold M_eff fixed.
    Detector recovers the INCREMENT Δη ≈ ε even when the baseline η_mixed is O(1)
    (bin iii) — teeth are relative, not absolute-null.
    """
    f = np.array([r["f"] for r in family])
    m_g = np.array([r["m_g"] for r in family])
    M_eff = np.array([r["M_eff"] for r in family])
    U = np.array([r["U"] for r in family])

    eta_null = NV.eta_slope(f, (m_g + 0.0 * U) / M_eff)
    eta_plant = NV.eta_slope(f, (m_g + _EPS_PLANT * U) / M_eff)
    delta = eta_plant - eta_null

    print("\n--- P11 SYNTHETIC ledger-level injection-recovery (detector arithmetic) ---")
    print(f"  baseline (ε=0)          η : {eta_null:+.3e}")
    print(f"  injected (ε={_EPS_PLANT})   η : {eta_plant:+.5f}")
    print(f"  recovered Δη              : {delta:+.5f}   (target ≈ {_EPS_PLANT})")

    assert abs(delta - _EPS_PLANT) < _PLANT_TOL, (
        f"FAIL: detector did not recover the planted ε as Δη — "
        f"Δη={delta:.5f} vs ε={_EPS_PLANT}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# KEEP-BOTH — legacy ADD mixed-register exposure still fires under source_mode=add_field
# ─────────────────────────────────────────────────────────────────────────────
def test_nordtvedt_legacy_add_mixed_register_still_exposes_gap():
    """KEEP-BOTH diagnostic: under legacy add_field, η_mixed (flux vs M_eff) ≫ 1.

    Confirms the #651 latent defect is still reproducible when the retired
    convention is selected — not a live gate of the ruled Komar default.
    """
    Grad, Div = NV.build_grad_div(_N)
    mask = NV.interior_mask(_N)
    f_list, mg_list, meff_list = [], [], []
    for sg in _SIGMAS:
        T00 = NV.normalized_blob(_N, sg, _M_TARGET)
        res = NV.solve_config(
            _N, T00, g_self=_G_SELF, s_min=_S_MIN, source_mode="add_field"
        )
        eps = res["eps11"]
        L = NV.stiffness_operator(_N, eps, Grad, Div, s_min=_S_MIN)
        led = NV.energy_ledger(T00, eps, Grad, g_self=_G_SELF)
        m_g = NV.gravitating_charge_flux(eps, L, mask)
        U = led["U_bind"]
        f_list.append(U / (led["M_matter"] + U))
        mg_list.append(m_g)
        meff_list.append(led["M_eff"])
    f = np.array(f_list)
    eta_mixed = NV.eta_slope(f, np.array(mg_list) / np.array(meff_list))
    print(f"\n--- KEEP-BOTH legacy add_field η_mixed : {eta_mixed:+.4f} ---")
    assert eta_mixed > _MIXED_ETA_MIN, (
        f"FAIL: legacy ADD no longer exposes the gap — η_mixed={eta_mixed:.4f}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# GATING (fast, no solve) — the η-detector unit test on synthetic ledgers
# ─────────────────────────────────────────────────────────────────────────────
def test_nordtvedt_detector_unit_arithmetic():
    """DETECTOR UNIT [GATING] — the η-slope estimator recovers a planted slope on
    SYNTHETIC ledgers (no solve; fast gating-lane sanity for the detector itself).

    Construct m_g = m_i·(1 + η_true·f) for a known η_true and confirm `eta_slope`
    returns it. The FROZEN estimator is ref-normalized (ref = smallest-f member), so
    it recovers `η_true/(1+η_true·f0)` — an O(η·f0) normalization offset that is
    exact and DOCUMENTED (immaterial to the verdicts: it is < 0.5% at the certification
    η≈0 and the planted ε=0.10, and the P11 PLANT_TOL=0.02 budgets for it). Two checks:
      (i) recovery to the EXACT ref-normalized value (characterizes the estimator);
      (ii) η_true=0 returns EXACTLY 0 (negative control — no slope when nothing is
           planted).
    """
    f = np.array([0.02, 0.04, 0.06, 0.08])
    m_i = np.array([5.0, 5.0, 5.0, 5.0])
    f0 = float(f.min())
    for eta_true in (0.0, 0.15, 1.0, -0.3):
        m_g = m_i * (1.0 + eta_true * f)
        eta = NV.eta_slope(f, m_g / m_i)
        expected = eta_true / (1.0 + eta_true * f0)  # exact ref-normalized slope
        assert abs(eta - expected) < 1e-9, f"FAIL: detector eta={eta} vs expected {expected}"
    # explicit negative control: identical ledgers → EXACTLY 0
    assert NV.eta_slope(f, np.ones_like(f)) == 0.0
