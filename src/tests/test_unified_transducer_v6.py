"""
v6 D9 TRANSDUCER keepers — PROBE-CAPABILITY (ave-apparatus-floor-attribution
v1.1): the chiral-boundary spin-orbit exchange BC, its probe validated on a
known-DIFFERENT reference, and the new knobs default to the OFF byte-identical
path.

  DEFAULTS-OFF      transducer_on defaults False ⇒ no transfer, ledgers zero,
                    u_adv unsourced (the inherited byte-identical path).
  F-PROBE (m-even)  the spin probe S_φ MUST separate ±helicity on a KNOWN seed:
                    RH ⇒ S_φ<0, LH ⇒ S_φ>0 (opposite sign), achiral ⇒ S_φ≈0.
                    A probe that cannot distinguish ±h is DISQUALIFIED.
  HELICITY-ODD      after stepping, ΔL_bulk(RH) = −ΔL_bulk(LH) (sign reversal);
                    achiral ΔL_bulk ≡ 0 (the structural null, from the field).
  CONSERVATION (C)  the AM channel closes 1:1 BY CONSTRUCTION (L_transferred ≡
                    S_photon_removed); the wall is PASSIVE (E_absorbed ≥ 0 ⇒ no
                    pump — ave-conserved-vs-pumped on the transducer).
  KNOWN-NULL        chi_exch=0 ⇒ ΔL_bulk ≡ 0 (the F-EXCHANGE floor reference).

Engine: src/ave/core/unified_genesis_engine.py (v6 D9 additions)
Prereg: research/2026-06-10_genesis-v6-transducer_prereg.md (§6 the smoke gate)
"""

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine


def _build(helicity, chi, *, N=28, wall_width=0.12, axis=2):
    """A planted saturated pocket (the g_wall chiral wall) + a chiral photon
    packet; bulk sector ON (u_adv receives), buckle OFF (D9 isolated)."""
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=False, omega_sector_on=False,
        buckle_on=False, transducer_on=(chi > 0.0), chi_exch=chi, wall_width=wall_width)
    c = (N - 1) / 2.0
    e.seed_bulk((c, c, c), sigma=5.0, frac=0.95, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=helicity, sigma=5.0, wavelength=8.0,
                          amplitude=0.10, axis=axis)
    return e


def _run(e, n):
    axis = e._transduce_axis()
    L0 = e.angular_momentum_bulk(axis)
    for _ in range(n):
        e.step()
    return e.angular_momentum_bulk(axis) - L0


def test_v6_transducer_defaults_off_byte_identical():
    """transducer_on defaults False; with it off the ledgers stay zero and u_adv
    is unsourced (the inherited path) even though a chiral photon is present."""
    e = UnifiedGenesisEngine(24, bulk_density_on=True, snap_on=False,
                             omega_sector_on=False, buckle_on=False)
    assert e.transducer_on is False
    e.drive_chiral_photon(helicity=1, sigma=4.0, wavelength=8.0, amplitude=0.1)
    for _ in range(40):
        e.step()
    assert e.L_transferred == 0.0 and e.S_photon_removed == 0.0
    assert e.transduce_events == 0
    assert float(np.max(np.abs(e.u_adv))) == 0.0, "no transducer ⇒ u_adv unsourced"


def test_v6_transducer_probe_separates_helicity_m_even_keeper():
    """F-PROBE keeper (the m-even lesson): the axial-spin probe S_φ distinguishes
    ±helicity on a KNOWN freshly-seeded photon BEFORE any dynamics — opposite
    signs for ±h, ≈0 for achiral. This is the capability gate for the whole smoke."""
    s_rh = _build(+1, 0.0).photon_spin_axial()
    s_lh = _build(-1, 0.0).photon_spin_axial()
    s_ac = _build(0, 0.0).photon_spin_axial()
    assert s_rh * s_lh < 0.0, "the probe MUST give opposite signs for ±helicity"
    assert abs(s_rh + s_lh) < 1e-9 * (abs(s_rh) + abs(s_lh)), "the seed is symmetric in ±h"
    assert abs(s_ac) < 1e-9 * abs(s_rh), "achiral (linear-pol) ⇒ zero axial spin"


def test_v6_transducer_helicity_odd_and_achiral_null():
    """ΔL_bulk reverses sign with photon handedness (helicity-odd), and the
    achiral arm transfers ZERO (the structural known-null)."""
    dL_rh = _run(_build(+1, 0.02), 200)
    dL_lh = _run(_build(-1, 0.02), 200)
    dL_ac = _run(_build(0, 0.02), 200)
    assert dL_rh * dL_lh < 0.0, "ΔL_bulk must reverse sign with helicity"
    odd_frac = abs(dL_rh - dL_lh) / (abs(dL_rh) + abs(dL_lh) + 1e-30)
    assert odd_frac > 0.9, f"near-perfect reversal expected, got odd_frac={odd_frac}"
    assert dL_ac == 0.0, "achiral arm transfers exactly zero (structural null)"


def test_v6_transducer_am_ledger_closes_1to1_and_passive():
    """Conservation-by-channel: L_transferred ≡ S_photon_removed (1:1 by
    construction) AND the wall is PASSIVE (E_absorbed ≥ 0 ⇒ never pumps)."""
    e = _build(+1, 0.02)
    _run(e, 200)
    led = e.transducer_ledger()
    assert abs(led["ledger_ratio_removed_over_transferred"] - 1.0) < 1e-9
    assert led["E_photon_loss"] >= 0.0, "the photon only ever PAYS energy"
    assert led["passive_no_pump"], "E_absorbed ≥ 0 — the wall absorbs, never pumps"
    assert led["transduce_events"] == 200


def test_v6_transducer_chi0_is_the_known_null_floor():
    """chi_exch=0 ⇒ no transfer (ΔL_bulk ≡ 0) — the F-EXCHANGE floor reference."""
    e = UnifiedGenesisEngine(24, bulk_density_on=True, snap_on=False,
                             omega_sector_on=False, buckle_on=False,
                             transducer_on=True, chi_exch=0.0)
    c = (24 - 1) / 2.0
    e.seed_bulk((c, c, c), sigma=4.0, frac=0.95, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=1, sigma=4.0, wavelength=8.0, amplitude=0.10)
    assert _run(e, 100) == 0.0
    assert float(np.max(np.abs(e.u_adv))) == 0.0


def test_v6_transducer_depletes_photon_beyond_free_drift():
    """The photon's MEASURED axial |spin| depletes under the transducer FAR beyond
    the free-propagation drift (the chi=0 baseline) — genuine depletion, not a
    ledger artifact."""
    e_on = _build(+1, 0.02)
    s0 = e_on.photon_spin_axial()
    _run(e_on, 200)
    drop_on = abs(s0) - abs(e_on.photon_spin_axial())

    e_off = _build(+1, 0.0)
    s0o = e_off.photon_spin_axial()
    _run(e_off, 200)
    drift = abs(abs(s0o) - abs(e_off.photon_spin_axial()))

    assert drop_on > 0.0, "the photon |spin| must DEPLETE under the transducer"
    assert drop_on > 50.0 * drift, "depletion must dominate the free-drift floor"


# ===================================================================== PHASE 3
# The ω-recipient (the Cosserat winding channel wired back on, prereg §7.2) + the
# sharpened-T5 chiral-twin probe. NEW knob omega_recipient_frac ⇒ keeper-validated.

def _build_omega(helicity, chi, frac, *, N=28, axis=2):
    """Transducer-ISOLATED config (buckle OFF) but ω sector ON, so the ONLY ω
    source is the transducer deposit — the clean known reference for the ω
    channel + the chiral-twin probe (PROBE-CAPABILITY, ave-apparatus-floor-attr)."""
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=False, omega_sector_on=True,
        buckle_on=False, lock_on=False, transducer_on=(chi > 0.0),
        chi_exch=chi, omega_recipient_frac=frac)
    c = (N - 1) / 2.0
    e.seed_bulk((c, c, c), sigma=5.0, frac=0.95, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=helicity, sigma=5.0, wavelength=8.0,
                          amplitude=0.10, axis=axis)
    return e


def test_v6_omega_recipient_frac0_is_byte_identical_pure_u_adv():
    """frac=0 (default) ⇒ NOTHING goes to the ω carrier — the PHASE-2 byte-identical
    path (the Meissner-zero keeper analogue): L_transferred_omega ≡ 0, the ω L-state
    is untouched by the transducer."""
    e = _build_omega(+1, 0.02, 0.0)
    om_prev0 = e.omega_prev.copy()
    _run(e, 150)
    assert e.L_transferred_omega == 0.0, "frac=0 ⇒ no ω deposit"
    assert e.L_transferred_u == e.L_transferred, "frac=0 ⇒ all δL into u_adv"
    # the ω L-state evolves only under its own wave eq (buckle off), never the transducer
    assert e.E_transduce_omega_gain == 0.0


def test_v6_omega_recipient_helicity_odd_and_achiral_null():
    """The ω-channel AM the transducer deposits (L_ω,axial) is HELICITY-ODD —
    reverses sign RH↔LH — and ZERO for the achiral (linear-pol) drive (the
    structural known-null from the field). The PROBE-CAPABILITY gate for T2/T3."""
    e_rh = _build_omega(+1, 0.02, 0.5); _run(e_rh, 200)
    e_lh = _build_omega(-1, 0.02, 0.5); _run(e_lh, 200)
    e_ac = _build_omega(0, 0.02, 0.5); _run(e_ac, 200)
    Lr = e_rh.L_transferred_omega
    Ll = e_lh.L_transferred_omega
    assert Lr * Ll < 0.0, "ω-channel deposit must reverse sign with helicity"
    odd = abs(Lr - Ll) / (abs(Lr) + abs(Ll) + 1e-30)
    assert odd > 0.9, f"near-perfect ω reversal expected, got {odd}"
    assert e_ac.L_transferred_omega == 0.0, "achiral ⇒ zero ω deposit (structural null)"


def test_v6_omega_split_conserves_combined_AM_ledger_1to1():
    """Conservation-by-channel under the split: the COMBINED ledger still closes
    1:1 (L_transferred ≡ L_u + L_ω ≡ S_photon_removed) and the wall stays PASSIVE
    (E_absorbed ≥ 0 across BOTH recipient channels)."""
    e = _build_omega(+1, 0.02, 0.5)
    _run(e, 200)
    led = e.transducer_ledger()
    assert abs(led["L_transferred"] - (led["L_transferred_u"] + led["L_transferred_omega"])) < 1e-12
    assert abs(led["ledger_ratio_removed_over_transferred"] - 1.0) < 1e-9
    assert led["passive_no_pump"], "E_absorbed ≥ 0 — the wall absorbs across both channels"


def test_v6_sharpened_T5_chiral_twin_probe_zero_on_achiral_m_even_keeper():
    """The sharpened-T5 keeper (the m-even / v5-geometric-false-positive lesson):
    the chiral-twin probe = the transducer-DRIVEN signed inner-disk circulation of
    u_adv (core_sense). It MUST flip sign RH↔LH AND read ≈0 on the achiral arm. A
    probe that reports a 'twin' on the achiral arm is reading the rotation-column
    GEOMETRY (the v5 RH=2608/LH=1040 false positive) and is DISQUALIFIED."""
    e_rh = _build_omega(+1, 0.02, 0.5); _run(e_rh, 200)
    e_lh = _build_omega(-1, 0.02, 0.5); _run(e_lh, 200)
    e_ac = _build_omega(0, 0.02, 0.5); _run(e_ac, 200)
    twin_rh = e_rh.core_sense(axis=2)
    twin_lh = e_lh.core_sense(axis=2)
    twin_ac = e_ac.core_sense(axis=2)
    assert twin_rh * twin_lh < 0.0, "the chiral twin must reverse sign RH↔LH"
    # achiral has NO transducer deposit (S_φ≡0) ⇒ the probe reads the structural null
    assert abs(twin_ac) < 1e-9 * (abs(twin_rh) + abs(twin_lh)), \
        "a twin on the achiral arm = the v5 GEOMETRIC false positive — DISQUALIFIED"
