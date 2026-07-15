"""G-PERSIST meter circuit-ontology completion — unit tests (Ruling 2, 2026-07-14).

Two guards on the two NEW meter paths added when the frozen #689 potential-only
meter was completed to the full two-register (potential + Cosserat kinetic) meter:

  1. attribution convention — the ENGINE-NATIVE per-node kinetic density
     (½ρ|u̇|² + ½I_ω|ω̇|²) sums EXACTLY to the engine scalar cos.kinetic_energy(),
     so no synthetic bond-to-endpoint split is introduced (convention disclosure #2).
  2. sponge exclusion — the full-register read region erodes `guard` kinetic-transit
     rings per face on the PML box and is a strict subset of the interior mask;
     on the torus (pml=0, no sponge) it equals the interior mask for every guard
     (convention disclosure #3).

Ref: research/2026-07-14_gpersist-meter-circuit-ontology.md ;
driver src/scripts/vol_1_foundations/gpersist_localization_observable.py.
"""

from __future__ import annotations

import numpy as np

from ave.core.loop_gap_harness import make_engine
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, A_YIELD, apply_seed
from scripts.vol_1_foundations.gpersist_localization_observable import (
    PRIMARY_R,
    SPONGE_GUARD,
    THETA,
    _cosserat_kinetic_density,
    _nonmonotone_flag,
    _read_region,
    _sector_signature,
    _trend,
)


def _seeded_engine(N: int, pml: int, mode: str = "pair"):
    engine = make_engine(
        4, N=N, bulk_density_on=True, pml=pml, use_memristive_saturation=True
    )
    apply_seed(engine, mode, amp=None, a_lock=A_LOCK_DEFAULT, front_target=A_YIELD)
    engine.apply_bulk_probe_ic(amp=0.08)
    engine.freeze_converter_wall()
    return engine


# --------------------------------------------------------------------------
# Convention disclosure #2 — bond-energy attribution (engine-native per-node)
# --------------------------------------------------------------------------
def test_kinetic_density_sums_to_engine_scalar():
    """Per-node kinetic density is the engine-native register: its interior-mask
    sum reproduces cos.kinetic_energy() to machine precision — no bond split."""
    engine = _seeded_engine(N=10, pml=0)
    coupled = engine._coupled
    for _ in range(3):  # populate u_dot / omega_dot with a real dynamical state
        engine.step()
    cos = coupled.cos
    dens = _cosserat_kinetic_density(cos)
    assert dens.shape == (10, 10, 10)
    assert np.all(dens >= 0.0)  # kinetic energy density is nonnegative
    scalar = float(cos.kinetic_energy())
    assert scalar > 0.0  # the seeded+stepped state actually has kinetic energy
    rel = abs(float(dens.sum()) - scalar) / max(abs(scalar), 1e-30)
    assert rel < 1e-12, f"kinetic density sum vs engine scalar rel-diff {rel:.2e}"


def test_kinetic_density_respects_mask_alive():
    """The kinetic register uses the SAME mask_alive gate the engine applies:
    dead sites carry zero kinetic density."""
    engine = _seeded_engine(N=10, pml=0)
    coupled = engine._coupled
    for _ in range(2):
        engine.step()
    cos = coupled.cos
    dens = _cosserat_kinetic_density(cos)
    dead = ~np.asarray(cos.mask_alive, dtype=bool)
    if dead.any():
        assert np.allclose(dens[dead], 0.0)


# --------------------------------------------------------------------------
# Convention disclosure #3 — sponge exclusion (kinetic-transit guard band)
# --------------------------------------------------------------------------
def test_sponge_exclusion_torus_is_noop():
    """On the torus (pml=0) there is no sponge: the full read region equals the
    interior mask for EVERY guard (the fork-scored cells are untouched)."""
    engine = _seeded_engine(N=12, pml=0)
    coupled = engine._coupled
    interior = np.asarray(coupled._interior_mask(), dtype=bool)
    for guard in (0, 1, 2, SPONGE_GUARD):
        region = _read_region(coupled, guard)
        assert np.array_equal(region, interior)


def test_sponge_exclusion_pml_erodes_guard_rings():
    """On the PML box the full read region is a strict subset of the interior
    mask, eroding exactly `guard` extra rings per face (a centered (N-2(pml+g))³
    block), and shrinks monotonically with guard."""
    N, pml = 14, 3
    engine = _seeded_engine(N=N, pml=pml, mode="pair")
    coupled = engine._coupled
    interior = np.asarray(coupled._interior_mask(), dtype=bool)
    assert int(interior.sum()) == (N - 2 * pml) ** 3  # 8³ = 512

    g0 = _read_region(coupled, 0)
    assert np.array_equal(g0, interior)  # guard 0 == interior mask

    prev = int(g0.sum())
    for guard in (1, 2):
        region = _read_region(coupled, guard)
        # strict subset of the interior mask
        assert np.all(interior[region])
        assert int(region.sum()) < prev
        # exact centered-block geometry
        side = N - 2 * (pml + guard)
        assert int(region.sum()) == side**3
        block = np.zeros((N, N, N), dtype=bool)
        p = pml + guard
        block[p : N - p, p : N - p, p : N - p] = True
        assert np.array_equal(region, block)
        prev = int(region.sum())


def test_shipped_guard_default_is_one_ring():
    """The shipped forward sponge exclusion is a single transit ring (disclosed
    engineering choice); guard>0 only bites on the PML box."""
    assert SPONGE_GUARD == 1
    engine = _seeded_engine(N=12, pml=3)
    coupled = engine._coupled
    shipped = _read_region(coupled, SPONGE_GUARD)
    interior = np.asarray(coupled._interior_mask(), dtype=bool)
    assert int(shipped.sum()) < int(interior.sum())


# --------------------------------------------------------------------------
# Phase-robust statistic — quiet-window mean + non-monotone guard (MAJOR 1)
# --------------------------------------------------------------------------
def _series(sector: str, stat: str, vals):
    return [{sector: {stat: v}} for v in vals]


def test_quiet_window_mean_inverts_an_endpoint_phase_moment():
    """A series whose settled window sits ABOVE its start but whose final step
    dips to a phase minimum: the endpoint rel_trend reads negative while the
    quiet-window mean rel_qmean reads positive (the review MAJOR 1 mirage)."""
    # 8 settled reads ~1.4 (above start 1.0), then a final-step slosh dip to 0.7.
    vals = [1.0, 1.5, 1.3, 1.5, 1.35, 1.5, 1.3, 1.45, 1.4, 0.7]
    tr = _trend(_series("e", "CF", vals), "e", "CF")
    assert tr["rel_trend"] < 0.0  # endpoint (0.7 vs 1.0) reads negative
    assert tr["rel_qmean"] > 0.0  # quiet-window mean sits above start
    # the last-half window is averaged, not the single final step
    assert tr["qmean_window"] == max(2, (len(vals) + 1) // 2)
    assert tr["qmean"] > vals[-1]


def test_nonmonotone_flag_fires_when_endpoint_opposes_drift():
    """The slope_norm guard (previously consumed by nothing) fires when a
    resolvable endpoint points OPPOSITE the window drift, and stays silent
    when endpoint and drift agree."""
    cf = f"CF_peak_{PRIMARY_R}"
    # CF: endpoint strongly negative (<= -THETA) but the window drifts UP (slope>0)
    flag_sector = {
        "PR": {"rel_trend": 0.0, "slope_norm": 0.0},
        cf: {"rel_trend": -3 * THETA, "slope_norm": +0.05},
    }
    assert cf in _nonmonotone_flag(flag_sector)
    # endpoint and drift agree (both down) -> no flag
    clean_sector = {
        "PR": {"rel_trend": 0.0, "slope_norm": 0.0},
        cf: {"rel_trend": -3 * THETA, "slope_norm": -0.05},
    }
    assert _nonmonotone_flag(clean_sector) == []


def test_sector_signature_stat_selector():
    """_sector_signature gates on the requested statistic; endpoint and quiet-
    window mean can yield different leaves on a phase-moment series."""
    cf = f"CF_peak_{PRIMARY_R}"
    sector = {
        "PR": {"rel_trend": 0.0, "rel_qmean": 0.0},
        cf: {"rel_trend": -0.42, "rel_qmean": +0.30},
    }
    assert _sector_signature(sector, "rel_trend") == "LOOP-FILLING"
    assert _sector_signature(sector, "rel_qmean") == "CONCENTRATING"
