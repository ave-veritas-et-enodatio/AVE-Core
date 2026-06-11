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

from ave.utils.topology_genus import (
    measure_topology,
    derive_read_torus_from_channel,
    make_sphere_shell_mask,
    make_torus_shell_mask,
)


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
