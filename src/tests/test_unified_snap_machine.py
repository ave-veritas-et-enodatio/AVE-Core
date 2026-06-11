"""
Smoke ladder — COMPONENT 2: the D1 snap state machine (per-cell, latent tally,
re-entry-requires-payback; hysteresis-by-BOOKKEEPING).

Known-null + known-positive per the prereg / directive smoke-ladder mandate:

  NULL-HEAL   snap_on=False: a sub-floor deficit blob REFILLS/heals (the medium
              has no boundary state — the 'no-snap engine reproduces sonic-horizon
              healing' smoke).
  NULL-BYTE   snap_on + bulk_density_on but NO bulk excitation ⇒ V/w/ω still
              byte-identical to the parent (the snap touches only ρ̄/u).
  POS-PERSIST a HAND-OPENED snapped shell (payback_rate=0) PERSISTS indefinitely
              and DEMANDS its tally (E_latent_held>0, pocket_cells constant) — the
              lock-by-bookkeeping ('persist and demand its tally').
  POS-PAYBACK with over-pressure + payback_rate>0 the tally is PAID BACK and the
              cells UN-SNAP (re-enter); the energy ledger CLOSES exactly
              (held+restored invariant; the conservation-by-bookkeeping guarantee).
  CTRL-CHI    χ_shock=0 is the ELASTIC control: no void-KE dissipated
              (E_diss_snap=0); χ_shock=1 dissipates (E_diss_snap>0). The N3 CLIP
              telltale.

Engine:  src/ave/core/unified_genesis_engine.py (UnifiedGenesisEngine, snap_on)
Prereg:  research/2026-06-10_genesis-v5-seeded-snap_prereg.md (D1, §5 N1/N2/N3)
"""

import numpy as np

from ave.core.crystal_graft_v4 import CrystalGraftV4
from ave.core.unified_genesis_engine import UnifiedGenesisEngine, RHO_CAV


def _central_ball(N, radius):
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    r = np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2)
    return r <= radius


def test_null_heal_no_snap_reversible_void_recovers():
    """snap_on=False: a shallow void in the REVERSIBLE regime (ρ̄>ρ̄_cav, c²>0)
    RECOVERS toward 0 (the sonic-horizon reversible-spring healing) and forms NO
    held pocket. The full refill timescale is acoustic (~R/c0, many steps — dt is
    bounded by the stiff inherited V branch); the smoke asserts the healing
    DIRECTION + the absence of a boundary-held pocket, the qualitative contrast
    with the snap's one-way pinned hold."""
    N = 32
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=False,
                               nu_art_bulk=1e-3, rho_diff=5e-4)
    ball = _central_ball(N, 2.0) & eng.interior_mask()
    eng.rho_bar[ball] = -0.30  # above the floor (reversible), no snap state at all
    rc0, _ = eng.rho_core()
    assert rc0 > RHO_CAV, "setup: void must be in the reversible regime (above floor)"
    for _ in range(300):
        eng.step()
    rc1, _ = eng.rho_core()
    assert rc1 > rc0 + 0.005, f"reversible void did not recover (ρ̄ {rc0:.3f} -> {rc1:.3f})"
    assert eng.pocket_cells() == 0, "no-snap engine must hold NO boundary pocket"


def test_null_byte_identical_under_snap_when_no_crossing():
    """snap_on + bulk_density_on but ρ̄≡0, u≡0 (no crossing): the inherited
    V/w/ω evolution is byte-identical to the parent. The snap addition does not
    perturb the inherited sectors."""
    N = 24
    parent = CrystalGraftV4(N, lock_on=True, lock_eta=0.08)
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               lock_on=True, lock_eta=0.08)
    c = (N - 1) / 2.0
    for e in (parent, eng):
        e.seed_bulk((c, c, c), sigma=4.0, frac=0.6, helical=False)
        e.seed_photon((c, c, c), sigma=5.0, wavelength=8.0, amplitude=0.05,
                      helicity=1.0, direction=(0, 0, 1))
    for _ in range(30):
        parent.step()
        eng.step()
    assert float(np.max(np.abs(eng.V - parent.V))) == 0.0
    assert float(np.max(np.abs(eng.w - parent.w))) == 0.0
    assert float(np.max(np.abs(eng.omega - parent.omega))) == 0.0
    assert eng.pocket_cells() == 0, "no crossing ⇒ no snap"


def test_pos_persist_handsnap_holds_and_demands_tally():
    """A hand-opened snapped shell with payback_rate=0 PERSISTS and DEMANDS its
    tally — it never re-enters because nothing pays it back."""
    N = 28
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               chi_shock=1.0, snap_payback_rate=0.0)
    ball = _central_ball(N, 3.0)
    latent = eng.hand_snap_region(ball)
    p0 = eng.pocket_cells()
    assert p0 > 0 and latent > 0.0, "hand-snap must open a pocket and tally a latent"
    held0 = eng.E_latent_held
    for _ in range(200):
        eng.step()
    assert eng.pocket_cells() == p0, "pocket must PERSIST (no payback ⇒ no re-entry)"
    assert eng.unsnap_events == 0, "nothing paid ⇒ no un-snap"
    assert abs(eng.E_latent_held - held0) < 1e-12, "held tally must be unchanged"


def test_pos_payback_unsnaps_and_ledger_closes():
    """With over-pressure (surrounding compression) + payback_rate>0 the tally is
    paid back: cells UN-SNAP, and the energy ledger CLOSES exactly
    (E_latent_held + E_latent_restored invariant once no new snaps)."""
    N = 28
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               chi_shock=1.0, snap_payback_rate=1.0, nu_art_bulk=1e-3)
    ball = _central_ball(N, 3.0)
    eng.hand_snap_region(ball)
    L0 = eng.E_latent_held + eng.E_latent_restored
    # surround with compressed (high-pressure) medium to drive payback
    shell = _central_ball(N, 7.0) & ~_central_ball(N, 4.0) & eng.interior_mask()
    eng.rho_bar[shell] = 0.4
    for _ in range(400):
        eng.step()
        if eng.unsnap_events > 0:
            break
    assert eng.unsnap_events > 0, "over-pressure should eventually pay the tally"
    # the bookkeeping closes: total latent is conserved across held<->restored
    L1 = eng.E_latent_held + eng.E_latent_restored
    assert abs(L1 - L0) < 1e-9, f"ledger did not close: {L0} -> {L1}"
    assert eng.E_latent_restored > 0.0


def test_ctrl_chi_shock_zero_is_elastic():
    """χ_shock=0 dissipates NO void KE (elastic control, the N3 telltale);
    χ_shock=1 dissipates (E_diss_snap>0). Same hand-snap with the same advective
    KE present."""
    N = 24
    ball = _central_ball(N, 3.0)

    def diss_for(chi):
        eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                                   chi_shock=chi)
        eng.u_adv[..., 0] = 0.3  # give the medium advective KE to (maybe) dissipate
        eng.hand_snap_region(ball)
        return eng.E_diss_snap

    d0 = diss_for(0.0)
    d1 = diss_for(1.0)
    assert d0 == 0.0, f"χ_shock=0 must dissipate nothing (got {d0})"
    assert d1 > 0.0, f"χ_shock=1 must dissipate the void KE (got {d1})"
