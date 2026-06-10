"""
Smoke ladder — COMPONENT 3: the D2 Lane-1 seed + the vent-into-seed coupling.

  CERT       seed_lane1 plants a topology-NULL standing-V seed (CP8 precursor-
             only): |H_bel|≈0, ω≡0, A²_seed≈frac². The certificate PASSES.
  STANDING   the seed carries a nonzero standing V with ∂_tV≈0 at t=0 (energized
             + locked once, not pumped).
  VENT-ON    with vent_into_seed armed, a hand-snap near the seed DELIVERS the
             shock energy into the seed (E_vent_to_seed>0, seed V-energy rises),
             and does NOT dissipate it (E_diss_snap stays 0).
  VENT-OFF   default (vent off): the same hand-snap DISSIPATES (E_diss_snap>0,
             E_vent_to_seed=0) — the component-2 behavior.
  ACCOUNT    near + radiated == total shock energy (vent_near_frac split exact).

Engine:  src/ave/core/unified_genesis_engine.py (seed_lane1, seed_certificate)
Prereg:  research/2026-06-10_genesis-v5-seeded-snap_prereg.md (D2, CP8)
"""

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine


def _ball(N, rad, ctr=None):
    cc = (N - 1) / 2.0 if ctr is None else ctr
    i, j, k = np.indices((N, N, N))
    r = np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2)
    return r <= rad


def test_cert_seed_is_topology_null_standing_v():
    N = 27  # odd ⇒ the seed center lands ON a cell (env_peak=1, exact A²_peak)
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0)
    eng.seed_lane1(frac=0.85, sigma=4.0)
    cert = eng.seed_certificate()
    assert cert["topology_null"] is True, f"seed not topology-null: {cert}"
    assert cert["omega_max"] == 0.0 and cert["H_bel_abs"] < 1e-12
    # the CORE depth (peak A²) = frac² (genesis-24 deep-saturation); the window-
    # weighted average is smaller (the Gaussian env falls off) — both reported
    assert abs(cert["A2_peak"] - cert["frac2"]) < 1e-9, cert
    assert 0.0 < cert["A2_seed"] < cert["A2_peak"], cert
    assert cert["passes"] is True


def test_standing_v_energized_not_pumped():
    """The seed V is nonzero and stationary (∂_tV≈0) at t=0 — energized+locked
    once. It is a real field (breathes when stepped), not a frozen artifact."""
    N = 24
    eng = UnifiedGenesisEngine(N, bulk_density_on=True)
    eng.seed_lane1(frac=0.6, sigma=4.0)
    assert float(np.max(np.abs(eng.V))) > 0.0
    assert float(np.max(np.abs(eng.V - eng.V_prev))) == 0.0  # stationary start
    for _ in range(20):
        eng.step()
    assert np.all(np.isfinite(eng.V))


def test_vent_on_delivers_energy_into_seed():
    N = 28
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               chi_shock=1.0)
    eng.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=True, vent_near_frac=0.5)
    e_before = eng.bulk_energy(interior_only=True)
    region = _ball(N, 3.0) & eng.interior_mask()
    eng.u_adv[region, 0] = 0.4  # advective KE for the shock to vent
    eng.hand_snap_region(region)
    assert eng.E_vent_to_seed > 0.0, "vent delivered no energy into the seed"
    assert eng.E_diss_snap == 0.0, "vent_on must route the shock to the seed, not dissipate"
    e_after = eng.bulk_energy(interior_only=True)
    # the seed V-energy rose by ~the near-field vented energy
    assert e_after - e_before > 0.5 * eng.E_vent_to_seed, (
        f"seed V-energy did not rise with the vent (Δ={e_after - e_before:.4e}, "
        f"vent={eng.E_vent_to_seed:.4e})")


def test_vent_off_dissipates():
    N = 28
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               chi_shock=1.0)
    eng.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=False)
    region = _ball(N, 3.0) & eng.interior_mask()
    eng.u_adv[region, 0] = 0.4
    eng.hand_snap_region(region)
    assert eng.E_diss_snap > 0.0
    assert eng.E_vent_to_seed == 0.0


def test_vent_accounting_near_plus_radiated_equals_shock():
    N = 28
    near_frac = 0.3
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               chi_shock=1.0)
    eng.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=True, vent_near_frac=near_frac)
    region = _ball(N, 3.0) & eng.interior_mask()
    eng.u_adv[region, 0] = 0.5
    eng.hand_snap_region(region)
    total = eng.E_vent_to_seed + eng.E_vent_radiated
    assert total > 0.0
    # the split is exact: near = near_frac·total, radiated = (1−near_frac)·total
    assert abs(eng.E_vent_to_seed - near_frac * total) < 1e-9 * total
