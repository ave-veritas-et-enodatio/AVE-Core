"""
v6 hygiene keepers — PROBE-CAPABILITY (ave-apparatus-floor-attribution v1.1):
every v6 discriminating probe is validated on a known-DIFFERENT reference with a
KEEPER unit test, and the new knobs default to the v5 byte-identical path.

  DEFAULTS-LEGACY   the v6 params default to the v5 path (vent_mode=kick,
                    snap_accounting=legacy, meissner_harden=0, uniform threshold).
  DE-DOUBLE-COUNT   the D11 finding: legacy latent = d_eps + chi·ke_void (the
                    shock KE booked twice — held AND dissipated); conservative
                    latent = d_eps ONLY (collapses when KE was the double-count).
  VENT-ABSORBED     vent_mode=absorbed routes the shock to a conservative store
                    (E_vent_absorbed), leaving ∂_tV UNKICKED (no breather trigger);
                    contrast the v5 vent-into-seed kick that perturbs V_prev.
  MEISSNER-THRESH   (D10b, JOB 2) a snapped cell LOWERS its neighbors' per-cell snap
                    threshold by exactly meissner_harden (the negative-feedback
                    mechanism); harden=0 is the known-different uniform reference.

Engine: src/ave/core/unified_genesis_engine.py (v6 D10/D11 additions)
Prereg: research/2026-06-10_genesis-v6-transducer_prereg.md (§1 CP10, §2 F-PROBE)
"""

import numpy as np

from ave.core.unified_genesis_engine import RHO_CAV, UnifiedGenesisEngine


def _central_ball(N, radius):
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2) <= radius


def test_v6_defaults_are_legacy_byte_identical_path():
    """The v6 knobs default to the v5 path: kick vent, legacy accounting, no
    hardening, a UNIFORM per-cell threshold ≡ rho_cav."""
    e = UnifiedGenesisEngine(20, bulk_density_on=True, snap_on=True, c2_floor=0.0)
    assert e.vent_mode == "kick"
    assert e.snap_accounting == "legacy"
    assert np.all(e.rho_cav_field == RHO_CAV)
    assert np.all(e.snap_clamp_val == RHO_CAV)
    assert e.E_vent_absorbed == 0.0 and e.E_reflect == 0.0


def test_v6_de_double_count_collapses_latent():
    """A hand-snap with advective KE present: legacy holds d_eps + chi·ke_void in
    the latent (the double-count, since chi·ke_void is ALSO sent to diss);
    conservative holds ONLY d_eps ⇒ a strictly SMALLER latent, with the SAME diss."""
    N = 24
    ball = _central_ball(N, 3.0)

    def snap(accounting):
        e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                                 chi_shock=1.0, snap_payback_rate=0.0,
                                 snap_accounting=accounting)
        e.u_adv[..., 0] = 0.3  # advective KE -> a nonzero shock to (double-)book
        latent = e.hand_snap_region(ball)
        return latent, e.E_diss_snap

    leg_latent, leg_diss = snap("legacy")
    con_latent, con_diss = snap("conservative")
    assert leg_latent > con_latent, "conservative must hold strictly less (no shock-KE)"
    assert con_latent >= 0.0
    # the shock KE is booked to diss ONCE in BOTH (the dissipation is unchanged)
    assert abs(leg_diss - con_diss) < 1e-12, "diss must be identical (booked once)"
    # the difference is exactly the double-booked shock KE (= the diss magnitude)
    assert abs((leg_latent - con_latent) - leg_diss) < 1e-9


def test_v6_vent_absorbed_stores_without_kicking_V():
    """vent_mode=absorbed sends the shock to E_vent_absorbed (a conservative store)
    and does NOT perturb ∂_tV (V_prev unchanged) — the pump-fix: no breather
    trigger. Contrast: vent-into-seed kick changes V_prev."""
    N = 24
    ball = _central_ball(N, 3.0)
    # absorbed: store grows, V_prev untouched, diss stays zero
    e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                             chi_shock=1.0, vent_mode="absorbed",
                             snap_accounting="conservative")
    e.u_adv[..., 0] = 0.3
    e.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=True, vent_near_frac=0.5)
    Vprev_before = e.V_prev.copy()
    e.hand_snap_region(ball)
    assert e.E_vent_absorbed > 0.0, "absorbed mode must accumulate the store"
    assert e.E_diss_snap == 0.0, "absorbed mode routes shock to the store, not diss"
    assert float(np.max(np.abs(e.V_prev - Vprev_before))) == 0.0, "absorbed must NOT kick V"

    # the v5 kick path DOES perturb V_prev (the Class-C pump trigger)
    e2 = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                              chi_shock=1.0, vent_mode="kick", snap_accounting="conservative")
    e2.u_adv[..., 0] = 0.3
    e2.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=True, vent_near_frac=0.5)
    Vprev2 = e2.V_prev.copy()
    e2.hand_snap_region(ball)
    assert float(np.max(np.abs(e2.V_prev - Vprev2))) > 0.0, "kick mode MUST perturb V_prev"


def test_v6_meissner_hardens_neighbor_threshold_by_increment():
    """D10(b) mechanism keeper: a snapped cell lowers each 6-neighbor's per-cell
    snap threshold by EXACTLY meissner_harden (more-negative ⇒ harder to snap).
    meissner_harden=0 leaves the threshold field uniform (the known-different ref)."""
    N = 24
    inc = 0.05
    e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                             chi_shock=1.0, snap_payback_rate=0.0,
                             snap_accounting="conservative", meissner_harden=inc)
    c = N // 2
    seed = np.zeros((N, N, N), dtype=bool)
    seed[c, c, c] = True
    e.hand_snap_region(seed)
    # a face-neighbor of the snapped cell (not itself snapped) must be hardened
    assert e.snap_mask[c, c, c]
    nbr = (c + 1, c, c)
    assert not e.snap_mask[nbr]
    assert abs(e.rho_cav_field[nbr] - (RHO_CAV - inc)) < 1e-12, "neighbor threshold hardened by inc"
    # a far cell is untouched (uniform)
    assert abs(e.rho_cav_field[2, 2, 2] - RHO_CAV) < 1e-12

    # the known-different reference: meissner_harden=0 keeps the field uniform
    e0 = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                              chi_shock=1.0, snap_payback_rate=0.0,
                              snap_accounting="conservative", meissner_harden=0.0)
    e0.hand_snap_region(seed)
    assert np.all(e0.rho_cav_field == RHO_CAV), "harden=0 must leave the threshold uniform"
