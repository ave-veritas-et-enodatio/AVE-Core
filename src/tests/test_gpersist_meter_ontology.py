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
    SPONGE_GUARD,
    _cosserat_kinetic_density,
    _read_region,
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
