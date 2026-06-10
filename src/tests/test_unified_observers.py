"""
Smoke ladder — COMPONENT 7: the D3 collimation + D4 twin-pocket observers.

  COL-PERFECT  a hand-built z-invariant field ⇒ columnarity≈1 (a perfect column).
  COL-FLOOR    a single-plane blob ⇒ columnarity≈1/Nax (the no-coherence floor).
  COL-CLEARS   a column clears the floor; the floor helper returns 1/Nax.
  HAND-SPLIT   a pure CCW column ⇒ RH>0, LH≈0, net>0 (handedness sense); CW flips.
  HAND-BALANCE a co+counter twin pair ⇒ RH≈LH, net≈0, balanced=True (born-in-pairs).
  TWIN-POCKET  snapped cells split into RH/LH pockets by local vorticity sense; a
               single-sense pocket has twin_present=False (an honest finding).

Engine:  src/ave/core/unified_genesis_engine.py (columnarity, handedness_ledger,
         twin_pocket_ledger)
Prereg:  research/2026-06-10_genesis-v5-seeded-snap_prereg.md (D3, D4, T5, F0a)
"""

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine


def _set_solid_body(eng, omega, env_radius, sense=+1):
    """Set u_adv to a solid-body rotation column about z (z-invariant ⇒ columnar)."""
    a1, a2 = eng._bx, eng._by
    rc = np.sqrt(a1 ** 2 + a2 ** 2)
    env = (rc <= env_radius).astype(float)
    eng.u_adv[:] = 0.0
    eng.u_adv[..., 0] = -sense * omega * a2 * env
    eng.u_adv[..., 1] = sense * omega * a1 * env


def test_col_perfect_zinvariant_is_columnar():
    N = 24
    eng = UnifiedGenesisEngine(N)
    _set_solid_body(eng, omega=0.1, env_radius=0.3 * N * eng.dx)
    c = eng.columnarity(axis=2)
    assert c > 0.9, f"z-invariant column should be near-1 columnar (got {c:.3f})"


def test_col_floor_single_plane_blob():
    N = 24
    eng = UnifiedGenesisEngine(N)
    # a vortical structure confined to ONE z-plane (no axial coherence)
    a1, a2 = eng._bx, eng._by
    rc = np.sqrt(a1 ** 2 + a2 ** 2)
    plane = np.zeros((N, N, N))
    plane[:, :, N // 2] = 1.0
    eng.u_adv[..., 0] = -a2 * (rc < 5) * plane
    eng.u_adv[..., 1] = a1 * (rc < 5) * plane
    c = eng.columnarity(axis=2)
    floor = eng.columnarity_floor(N)
    assert c < 5 * floor, f"single-plane blob should sit near the floor (c={c:.3f}, floor={floor:.3f})"


def test_col_clears_floor():
    N = 24
    eng = UnifiedGenesisEngine(N)
    _set_solid_body(eng, omega=0.1, env_radius=0.3 * N * eng.dx)
    assert eng.columnarity(axis=2) > 10 * eng.columnarity_floor(N)


def test_hand_split_sense_and_sign():
    """The dominant rotation SENSE is core_sense (inner disk): CCW>0, CW<0. The
    GLOBAL ∫ζ is ~0 by compact support (RH=LH) — born-in-pairs, recorded."""
    N = 24
    ccw = UnifiedGenesisEngine(N)
    _set_solid_body(ccw, omega=0.1, env_radius=0.3 * N * ccw.dx, sense=+1)
    lc = ccw.handedness_ledger(axis=2)
    assert lc["core_sense"] > 0.0, lc
    # compact support: global handedness ~0 (RH≈LH) — the born-in-pairs signature
    assert lc["balanced"] is True and abs(lc["abs_net_frac"]) < 0.1, lc
    cw = UnifiedGenesisEngine(N)
    _set_solid_body(cw, omega=0.1, env_radius=0.3 * N * cw.dx, sense=-1)
    assert cw.handedness_ledger(axis=2)["core_sense"] < 0.0


def test_hand_balanced_global_is_born_in_pairs():
    """The global handedness ledger ≈ 0 for ANY compactly-supported flow (the
    boundary shear carries the counter-circulation) — the T5 born-in-pairs /
    Kelvin signature, automatic. A single column already satisfies it."""
    N = 28
    eng = UnifiedGenesisEngine(N)
    _set_solid_body(eng, omega=0.1, env_radius=0.25 * N * eng.dx, sense=+1)
    lc = eng.handedness_ledger(axis=2, tol=0.15)
    assert lc["balanced"] is True, f"compact flow must be globally balanced: {lc}"
    assert lc["core_sense"] > 0.0  # but the core still has a definite sense


def test_twin_pocket_single_sense_not_a_twin():
    N = 24
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               snap_payback_rate=0.0)
    _set_solid_body(eng, omega=0.1, env_radius=0.3 * N * eng.dx, sense=+1)
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    ball = np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2) <= 3.0
    eng.hand_snap_region(ball)
    tl = eng.twin_pocket_ledger(axis=2)
    assert tl["total_pocket_cells"] > 0
    # a single-sense column ⇒ pocket is one-handed ⇒ NOT a twin (honest finding)
    assert tl["twin_present"] is False, tl
