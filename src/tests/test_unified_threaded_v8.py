"""genesis-v8 THREADED keepers — PROBE-CAPABILITY (ave-apparatus-floor-attribution
v1.1): every discriminating v8 probe validated on a known-different reference and
a known-positive BEFORE the matrix; every new knob defaults to the v6/v7 byte-
identical path.

This file is built INCREMENTALLY across the Phase-2 component commits (the prereg
§9 keeper table), one keeper block per component:

  D16 (this commit) — K-TOPOLOGY: the topology gate distinguishes a known genus-0
                      sphere-shell (NO-PENETRATION) from a known genus-1 torus-shell
                      (THREADED), and the field-derived read torus recovers the
                      planted wall ring (the A46 fix). REAL topology on knowns.
  D17 — K-CASCADE-EACH-RENDER (the feedstock-sparing must not reopen the v5
        deflagration; F-CASCADE).
  D15 — K-TRAVEL-VS-STANDING (the HEART of v8: a planted STANDING quadrature reads
        w_pol=0, a planted TRAVELING quadrature reads its integer) + K-PLANT-IN-
        CHANNEL + K-OFF byte-identity.

A probe that fails its known-positive/known-null keeper DISQUALIFIES the
corresponding verdict (CLIP), per the m-even lesson.
"""

from __future__ import annotations

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine, RHO_CAV
from ave.utils.topology_genus import (
    measure_topology,
    derive_read_torus_from_channel,
    make_sphere_shell_mask,
    make_torus_shell_mask,
)

F_EV = 13.0          # the quiet-build E_V plateau (v5 §0; the deflagration floor)
F_EV_GATE = 10.0     # F-CASCADE bound: deflagration = E_V >= 10x F-EV


def _cascade_engine(snap_u_mode, *, N=32, channel=False, seed=1):
    """A v6-conservative bubble carrying circulation, with a forced snapped pocket
    that holds the column swirl — the executable cascade probe (the natural snap
    onset is too slow for a unit test; this forces the snapped-cell-with-circulation
    state the D17 rendering governs)."""
    np.random.seed(seed)
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
        nu_art_bulk=5e-4, rho_diff=5e-4, rho_cav=RHO_CAV, lock_on=True,
        lock_eta=0.08, vent_mode="absorbed", snap_accounting="conservative",
        meissner_harden=0.05, snap_u_mode=snap_u_mode)
    e.seed_lane1(frac=0.85, sigma=4.0, vent_into_seed=True, vent_near_frac=0.5)
    e.energize_rotation_column(M_edge=2.5, R_core=0.18 * e.N * e.dx, axis=2)
    e.freeze_wall_window()
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    rho = np.sqrt((i - cc) ** 2 + (j - cc) ** 2)
    if channel:
        e.channel_mask = (rho < 3.0)
    ball = (rho < 5.0) & (np.abs(k - cc) < 6.0)
    e.hand_snap_region(ball, rho_set=e.rho_cav - 0.05)
    return e


def _interior(N, pad=2):
    m = np.zeros((N, N, N), dtype=bool)
    m[pad:-pad, pad:-pad, pad:-pad] = True
    return m


# ==================================================================== D16 K-TOPOLOGY
def test_ktopology_sphere_reads_no_penetration():
    """A watertight genus-0 spherical snap shell MUST bin NO-PENETRATION — the
    central cavity is sealed by the polar caps; no un-snapped channel threads the
    axis. (If this read THREADED, every genus-0 bubble would be a false torus.)"""
    N = 48
    sph = make_sphere_shell_mask(N, r_in=8.0, r_out=12.0, axis=2)
    res = measure_topology(sph, _interior(N), axis=2, f_shell=200)
    assert res["bin"] == "NO-PENETRATION", res["reason"]
    # corroboration: a genus-0 hollow sphere encloses exactly one cavity (b2=1)
    assert res["b2_cavities"] == 1, res


def test_ktopology_torus_reads_threaded():
    """A known genus-1 torus-shell MUST bin THREADED — the central hole is open
    through the axis, exterior-below and exterior-above are the same un-snapped
    component within the bounding cylinder (b1>=1 tunnel). The load-bearing
    ball->torus discriminator."""
    N = 48
    tor = make_torus_shell_mask(N, R=12.0, a=4.0, axis=2)
    res = measure_topology(tor, _interior(N), axis=2, f_shell=200)
    assert res["bin"] == "THREADED", res["reason"]
    assert res["channel_cells"] > 0
    # a solid torus encloses no isolated cavity (the hole is open, not enclosed)
    assert res["b2_cavities"] == 0, res


def test_ktopology_threaded_on_every_axis():
    """The gate is not z-special — a torus about each axis reads THREADED about
    that axis (the spin axis is a run-config choice, not baked in)."""
    N = 48
    for axis in (0, 1, 2):
        tor = make_torus_shell_mask(N, R=12.0, a=4.0, axis=axis)
        res = measure_topology(tor, _interior(N), axis=axis, f_shell=200)
        assert res["bin"] == "THREADED", (axis, res["reason"])


def test_ktopology_sphere_about_wrong_axis_still_no_penetration():
    """A sphere is genus-0 about EVERY axis — measuring about any axis still reads
    NO-PENETRATION (the gate does not manufacture a tunnel from a symmetric void)."""
    N = 48
    sph = make_sphere_shell_mask(N, r_in=8.0, r_out=12.0)
    for axis in (0, 1, 2):
        res = measure_topology(sph, _interior(N), axis=axis, f_shell=200)
        assert res["bin"] == "NO-PENETRATION", (axis, res["reason"])


def test_ktopology_shell_never_forms_floor():
    """Below F-SHELL (a sparse cavitation cloud, no coherent connected shell) the
    gate bins SHELL-NEVER-FORMS — the floor case, evaluated first. A handful of
    scattered specks is not a shell to thread."""
    N = 48
    rng = np.random.default_rng(0)
    speck = rng.random((N, N, N)) < 0.002  # ~440 isolated cells, no big component
    res = measure_topology(speck, _interior(N), axis=2, f_shell=200)
    assert res["bin"] == "SHELL-NEVER-FORMS", res["reason"]


def test_ktopology_fragmented_cloud_fails_dominance():
    """A shell that fragments into many disconnected pieces (no single component
    holding the dominance fraction) is NOT a coherent shell — SHELL-NEVER-FORMS,
    guarding the v8-observed scattered-cavitation regime even when total snapped
    cells are many."""
    N = 48
    rng = np.random.default_rng(1)
    # many small clusters, none dominant: lots of snapped cells, no coherent shell
    cloud = rng.random((N, N, N)) < 0.05
    res = measure_topology(cloud, _interior(N), axis=2, f_shell=200,
                           dominance_frac=0.30)
    # a random 5% cloud at 6-connectivity percolates or fragments; either way it
    # must NOT be called a clean THREADED torus (the false-positive guard)
    assert res["bin"] in ("SHELL-NEVER-FORMS", "NO-PENETRATION"), res["reason"]


# ============================================ D16 read-torus (the A46 field-derive)
def test_read_torus_recovers_planted_wall_ring():
    """The field-derived read torus (the A46 fix) recovers the PLANTED wall ring:
    for a torus at major radius R=12, tube a=4, derive_read_torus must return
    R ~ 12 (the wall midline), NOT the bounding-cylinder rim. (The earlier
    chan_plane_r.max() returned ~18 — the cylinder edge — flagged + fixed.)"""
    N = 48
    tor = make_torus_shell_mask(N, R=12.0, a=4.0, axis=2)
    res = measure_topology(tor, _interior(N), axis=2, f_shell=200)
    rd = derive_read_torus_from_channel(res, axis=2)
    assert rd is not None
    assert 10.5 <= rd["R"] <= 13.5, rd
    assert rd["r"] >= 3.0, rd  # F0b minor-circle floor


def test_read_torus_tracks_major_radius():
    """The derived R tracks the planted major radius across two tori — it is
    field-derived, not a fixed convention (the v7 pol_R N-collapse the fix kills)."""
    N = 52
    rd_big = derive_read_torus_from_channel(
        measure_topology(make_torus_shell_mask(N, R=14.0, a=4.0), _interior(N),
                         axis=2, f_shell=200))
    rd_small = derive_read_torus_from_channel(
        measure_topology(make_torus_shell_mask(N, R=10.0, a=3.0), _interior(N),
                         axis=2, f_shell=200))
    assert rd_big["R"] > rd_small["R"] + 2.0, (rd_big, rd_small)


def test_read_torus_none_for_non_threaded():
    """No read torus exists for a non-threaded bin (the field provides no major
    radius — exactly the v7 SPHERE obstruction; derive returns None, not a guess)."""
    N = 48
    sph = make_sphere_shell_mask(N, r_in=8.0, r_out=12.0)
    res = measure_topology(sph, _interior(N), axis=2, f_shell=200)
    assert derive_read_torus_from_channel(res) is None


# ============================================ D17 SPARE-THE-FEEDSTOCK (F-CASCADE)
def test_d17_inherited_is_byte_identical_default():
    """The snap_u_mode default ("inherited") quenches u_adv to EXACTLY 0 in snapped
    cells — the v6 byte-identical path (no v8 knob perturbs the inherited dynamics
    when off; the D-INHERIT regression gate's u-channel half)."""
    e = UnifiedGenesisEngine(16, bulk_density_on=True, snap_on=True,
                             snap_accounting="conservative")
    assert e.snap_u_mode == "inherited"
    e.energize_rotation_column(M_edge=2.0, R_core=2.0, axis=2)
    cm = np.zeros((16, 16, 16), dtype=bool)
    cm[6:10, 6:10, 6:10] = True
    q = e._snap_quench_u(cm)
    assert np.allclose(q, 0.0), "inherited must fully quench u_adv (byte-identical)"


def test_d17_renderings_spare_circulation_at_levels():
    """The three D17 renderings preserve DIFFERENT amounts of the circulation
    feedstock (the sparing machinery is LIVE, not a no-op): inherited removes all;
    wall_normal preserves the tangential swirl where the wall normal is degenerate
    (a flat deep-void interior — nothing to remove); channel_live preserves the
    channel-border feedstock. (Validates the rendering axis is real before the
    matrix sweeps it; §5 row 2.)"""
    N = 32
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    rho = np.sqrt((i - cc) ** 2 + (j - cc) ** 2)
    ball = (rho < 5.0) & (np.abs(k - cc) < 6.0)

    def quench_mag(mode, channel):
        e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True,
                                 snap_accounting="conservative", snap_u_mode=mode)
        e.energize_rotation_column(M_edge=2.5, R_core=0.18 * N * e.dx, axis=2)
        if channel:
            e.channel_mask = (rho < 3.0)
        cm = ball & e.interior_mask()
        return float(np.sqrt((e._snap_quench_u(cm) ** 2).sum(-1)).mean())

    m_inh = quench_mag("inherited", False)
    m_wn = quench_mag("wall_normal", False)
    m_ch = quench_mag("channel_live", True)
    assert m_inh == 0.0, "inherited must remove all circulation"
    assert m_wn > 0.5, f"wall_normal must spare the tangential swirl, got {m_wn}"
    assert m_ch > 0.5, f"channel_live must spare the channel feedstock, got {m_ch}"


def test_d17_channel_live_falls_back_to_inherited_without_mask():
    """channel_live with NO channel mask set (the topology gate has not run) is a
    fail-safe: it quenches fully, exactly as inherited (no silent sparing without a
    field-derived channel)."""
    N = 32
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    rho = np.sqrt((i - cc) ** 2 + (j - cc) ** 2)
    ball = (rho < 5.0) & (np.abs(k - cc) < 6.0)
    e = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True,
                             snap_accounting="conservative", snap_u_mode="channel_live")
    e.energize_rotation_column(M_edge=2.5, R_core=0.18 * N * e.dx, axis=2)
    assert e.channel_mask is None
    cm = ball & e.interior_mask()
    assert np.allclose(e._snap_quench_u(cm), 0.0)


def test_d17_cascade_bounded_each_rendering():
    """K-CASCADE-EACH-RENDER (F-CASCADE): NO D17 rendering reopens the v5
    deflagration. With a circulating snapped pocket carrying the column swirl,
    every rendering keeps E_V bounded (< 10x F-EV), the field finite, and does NOT
    pump the conserved total (H never rises above its start) — the feedstock-
    sparing does not become an energy source (ave-conserved-vs-pumped)."""
    for mode, channel in (("inherited", False), ("wall_normal", False),
                          ("channel_live", True)):
        e = _cascade_engine(mode, channel=channel)
        H0 = float(e.total_energy_unified(conserved=True))
        ev_max, H_max = 0.0, -1e30
        for _ in range(500):
            e.step()
            ev_max = max(ev_max, float(e.bulk_energy(True)))
            H_max = max(H_max, float(e.total_energy_unified(conserved=True)))
        assert np.all(np.isfinite(e.rho_bar)), f"{mode}: field went non-finite"
        assert ev_max < F_EV * F_EV_GATE, f"{mode}: E_V={ev_max} reopened the cascade"
        # no pump: the conserved total must not RISE (a passive lossy mirror only
        # sinks; sparing circulation must not manufacture energy)
        assert H_max <= H0 + 1e-6 * abs(H0) + 1e-6, f"{mode}: H pumped {H_max-H0:+.4e}"


def test_d17_reflect_ledger_honest_only_removed():
    """The removed-KE ledger (E_reflect) is honest: it tallies ONLY what the
    rendering actually removes. A sparing rendering removes <= what inherited
    removes, so its E_reflect is <= inherited's (never more) — the ledger cannot
    over-count a sink to hide spared energy."""
    e_inh = _cascade_engine("inherited", channel=False)
    e_wn = _cascade_engine("wall_normal", channel=False)
    for _ in range(200):
        e_inh.step()
        e_wn.step()
    assert e_inh.E_reflect >= -1e-12
    assert e_wn.E_reflect >= -1e-12
    # the spared rendering's reflector sink is no larger than inherited's
    assert e_wn.E_reflect <= e_inh.E_reflect + 1e-9, (e_wn.E_reflect, e_inh.E_reflect)
