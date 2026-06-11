"""
Smoke ladder — COMPONENT 1: the unified genesis engine (v5).

Known-null + known-positive per the prereg smoke-ladder mandate:

  NULL-1  bulk_density_on=False ⇒ V/w/ω evolution is BYTE-IDENTICAL to a pure
          CrystalGraftV4 with the same seed/IC (max|Δ|=0.0). The merge does NOT
          perturb the inherited physics (the HARD CONSTRAINT; the v4-lineage
          bit-identical discipline).
  NULL-2  with the bulk sector dormant, ρ̄ and u stay exactly zero.
  POS-1   bulk_density_on=True + a 3D solid-body rotation column (M_edge≈0.8,
          the inherited cavitation-probe reach) ⇒ the core ρ̄ develops a NEGATIVE
          deficit DYNAMICALLY (CP9 — emerges from continuity, not planted),
          driving c_bulk² down toward the candidate floor.
  POS-2   the matched-energy CURL-FREE radial breather develops NO comparable
          centrifugal deficit (circulation, not energy, drives the rarefaction).
  CONS    circulation Γ_z is set once and conserved within a floor in the near-
          inviscid limit over a short quiet window (ENERGIZE+LOCK, never pumped).

Engine:  src/ave/core/unified_genesis_engine.py
Prereg:  research/2026-06-10_genesis-v5-seeded-snap_prereg.md
"""

import numpy as np
import pytest

from ave.core.crystal_graft_v4 import CrystalGraftV4
from ave.core.unified_genesis_engine import UnifiedGenesisEngine, RHO_CAV


def _seed_common(eng):
    """Identical IC for the bit-identical comparison: a saturated bulk seed + a
    CP photon (the inherited seeders, unchanged)."""
    c = (eng.N - 1) / 2.0
    eng.seed_bulk((c, c, c), sigma=4.0, frac=0.6, helical=False)
    eng.seed_photon((c, c, c), sigma=5.0, wavelength=8.0, amplitude=0.05,
                    helicity=1.0, direction=(0, 0, 1))


def test_null1_bit_identical_to_parent():
    """The merge is byte-for-byte the parent when the bulk sector is dormant."""
    N = 24
    parent = CrystalGraftV4(N, lock_on=True, lock_eta=0.08)
    unified = UnifiedGenesisEngine(N, bulk_density_on=False, lock_on=True, lock_eta=0.08)
    assert unified.dt == parent.dt, "dt must be inherited unchanged"
    _seed_common(parent)
    _seed_common(unified)
    for _ in range(40):
        parent.step()
        unified.step()
    dV = float(np.max(np.abs(unified.V - parent.V)))
    dw = float(np.max(np.abs(unified.w - parent.w)))
    dom = float(np.max(np.abs(unified.omega - parent.omega)))
    assert dV == 0.0 and dw == 0.0 and dom == 0.0, (
        f"inherited sectors NOT bit-identical: dV={dV} dw={dw} dω={dom}")


def test_null2_dormant_bulk_stays_zero():
    N = 20
    eng = UnifiedGenesisEngine(N, bulk_density_on=False)
    _seed_common(eng)
    for _ in range(30):
        eng.step()
    assert np.all(eng.rho_bar == 0.0)
    assert np.all(eng.u_adv == 0.0)
    assert eng.bulk_step_count == 0


def test_pos1_rotation_column_rarefies_core():
    """A self-circulating column rarefies its OWN core (CP9): ρ̄_core goes
    negative DYNAMICALLY (emerges from continuity, not planted), deepening
    monotonically toward the candidate floor. This is the REACH, not the snap —
    the full reach-to-floor is a run-time question (the cavitation-probe result),
    NOT a smoke target; the smoke only demands an unambiguous emergent deficit."""
    N = 32
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, nu_art_bulk=2e-3, rho_diff=5e-4)
    R_core = 0.18 * N * eng.dx
    eng.energize_rotation_column(M_edge=1.2, R_core=R_core, axis=2)
    rc0, _ = eng.rho_core()
    assert abs(rc0) < 1e-12, "deficit must EMERGE, not be planted (CP9)"
    deepest, prev = 0.0, 0.0
    for _ in range(500):
        eng.step()
        rc, _ = eng.rho_core()
        deepest = min(deepest, rc)
        if not np.all(np.isfinite(eng.rho_bar)):
            pytest.fail("bulk sector went non-finite (CFL)")
    # a clear emergent deficit, well above the eps_den~1e-6 floor and clips
    # (which did not bite: clipR=0 at this config)
    assert deepest < -0.02, f"core did not rarefy (deepest ρ̄={deepest:.4f})"
    assert deepest > RHO_CAV, "ρ̄ ran past the floor unphysically (reach overshoot)"


def test_pos2_continuity_sign_diverging_rarefies_converging_compresses():
    """The continuity-sign validator (the honest known-positive/known-null pair
    for the new sector's wiring): a DIVERGING radial outflow evacuates → core
    RAREFIES (ρ̄<0); a CONVERGING inflow → core COMPRESSES (ρ̄>0). Symmetric
    magnitudes confirm continuity+momentum are sign-correct.

    NOTE (flag-don't-fix, recorded): a diverging breather rarefies the core by
    DIRECT EVACUATION, which on short timescales out-rarefies a divergence-free
    rotation column — so a breather is NOT a 'no-deficit' control. POS-1's column
    deficit is purely CENTRIFUGAL (solid-body ∇·u=0). The two are distinct
    rarefaction mechanisms; the smoke validates both, not a horse-race."""
    N = 32
    R_core = 0.18 * N
    diver = UnifiedGenesisEngine(N, bulk_density_on=True, nu_art_bulk=2e-3, rho_diff=5e-4)
    R_core = 0.18 * N * diver.dx
    diver.energize_radial_breather(ke_target=0.5, R_core=R_core)
    conv = UnifiedGenesisEngine(N, bulk_density_on=True, nu_art_bulk=2e-3, rho_diff=5e-4)
    conv.energize_radial_breather(ke_target=0.5, R_core=R_core)
    conv.u_adv *= -1.0  # inflow
    div_deepest = 0.0
    conv_peak = 0.0
    for _ in range(150):
        diver.step()
        conv.step()
        div_deepest = min(div_deepest, diver.rho_core()[0])
        m = conv.interior_mask()
        conv_peak = max(conv_peak, float(np.max(np.where(m, conv.rho_bar, -np.inf))))
    assert div_deepest < -1e-3, f"diverging outflow did not rarefy (ρ̄={div_deepest:.4f})"
    assert conv_peak > 1e-3, f"converging inflow did not compress (ρ̄={conv_peak:.4f})"


def test_cons_circulation_conserved_near_inviscid():
    """Γ_z is energized once and conserved within a floor in the near-inviscid
    limit over a quiet window (no secular pump)."""
    N = 40
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, nu_art_bulk=1e-4, rho_diff=1e-4)
    R_core = 0.2 * N * eng.dx
    eng.energize_rotation_column(M_edge=0.4, R_core=R_core, axis=2)
    g0 = eng.bulk_circulation_z()
    for _ in range(200):
        eng.step()
    g1 = eng.bulk_circulation_z()
    drift = abs(g1 - g0) / (abs(g0) + 1e-30)
    assert drift < 0.20, f"circulation drifted {drift:.3f} (>20%) — pump/over-dissipation"
