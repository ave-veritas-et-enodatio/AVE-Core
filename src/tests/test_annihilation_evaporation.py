"""
Annihilation/evaporation PROBE-CAPABILITY keepers (prereg §9.2, F-PROBE §3)
===========================================================================

`research/2026-06-11_annihilation-evaporation_prereg.md` (frozen @ b883c9b4):
every discriminating probe is validated on a KNOWN-DIFFERENT reference BEFORE
the Phase-2 verdict leans on it (the v6 m-even lesson). Plus the engine-lineage
HARD CONSTRAINT: the additions default to the v6 byte-identical path.

  BYTE-IDENTITY   AnnihilationEngine with NO new calls steps bit-identically to
                  UnifiedGenesisEngine (no step() override exists; this keeper
                  pins it against regression).
  K-DRIVE-EQUIV   one drive_chiral_photon_at on a fresh engine == the inherited
                  drive_chiral_photon (the additive w_prev form is value-
                  identical when w starts 0).
  K-HANDED        the windowed photon-spin probe separates the two objects'
                  OPPOSITE helicity on the freshly-built RH/LH pair, BEFORE any
                  dynamics; ≈0 for an achiral pair.
  K-BURST         the LongitudinalBurstDetector FIRES on a known hand-opened
                  snap (the v6 D6 known-positive) and stays SILENT on the
                  two-static-masses no-approach null.
  K-MASS          the residual-mass probe reads the FULL seed energy on an
                  isolated object and ≈0 (background) on an empty box.
  K-TRANSPORT     imprint_drift is exact bookkeeping (KE_approach = the
                  conserved-functional delta, > 0, localized to the masked
                  object) and a short coast conserves H_total^cons (the
                  transport addition does not itself pump/leak).

Scale note (honest): keepers run at reduced N/steps — they validate PROBE
CAPABILITY on known references, not the Phase-2 headline (which runs at the
frozen N=48 scale in the driver).
"""

import copy

import numpy as np

from ave.core.annihilation_engine import AnnihilationEngine
from ave.core.longitudinal_burst_detector import LongitudinalBurstDetector
from ave.core.unified_genesis_engine import UnifiedGenesisEngine


def _mk(N=32, cls=AnnihilationEngine, **kw):
    base = dict(bulk_density_on=True, snap_on=True, c2_floor=0.0,
                vent_mode="absorbed", snap_accounting="conservative",
                meissner_harden=0.05, omega_sector_on=True, buckle_on=True,
                photon_coupling=True, lock_on=True, lock_eta=0.08,
                transducer_on=True, chi_exch=0.02, omega_recipient_frac=0.5)
    base.update(kw)
    return cls(N, **base)


def _two_object_build(N=32, hA=+1, hB=-1, frac=0.85, sep_frac=18.0 / 48.0):
    """The §4.1 two-object placement (no stepping): seeds at c_A/c_B + frozen
    wall window + per-object chiral drives."""
    e = _mk(N)
    c = (N - 1) / 2.0
    half = sep_frac * N / 2.0
    cA = (c - half, c, c)
    cB = (c + half, c, c)
    e.seed_lane1(center=cA, sigma=4.0, frac=frac, vent_into_seed=False)
    e.seed_lane1(center=cB, sigma=4.0, frac=frac, vent_into_seed=False)
    e.freeze_wall_window()
    e.drive_chiral_photon_at(cA, helicity=hA, sigma=4.0, wavelength=8.0, amplitude=0.10, axis=2)
    e.drive_chiral_photon_at(cB, helicity=hB, sigma=4.0, wavelength=8.0, amplitude=0.10, axis=2)
    return e, cA, cB


# --------------------------------------------------------------- BYTE-IDENTITY
def test_defaults_byte_identical_to_v6_engine():
    """No new calls => AnnihilationEngine steps bit-identically to the v6
    engine (the engine-lineage HARD CONSTRAINT)."""
    cfg = dict(N=24)
    ea = _mk(cls=AnnihilationEngine, **cfg)
    eu = _mk(cls=UnifiedGenesisEngine, **cfg)
    c = (24 - 1) / 2.0
    for e in (ea, eu):
        e.seed_lane1(center=(c, c, c), sigma=4.0, frac=0.85, vent_into_seed=False)
        e.freeze_wall_window()
        e.drive_chiral_photon(helicity=1, sigma=4.0, wavelength=8.0, amplitude=0.10, axis=2)
        for _ in range(30):
            e.step()
    assert np.array_equal(ea.V, eu.V)
    assert np.array_equal(ea.w, eu.w)
    assert np.array_equal(ea.omega, eu.omega)
    assert np.array_equal(ea.rho_bar, eu.rho_bar)


# --------------------------------------------------------------- K-DRIVE-EQUIV
def test_single_additive_drive_matches_inherited():
    """One drive_chiral_photon_at on a fresh engine == drive_chiral_photon
    (additive == assignment when w starts at 0)."""
    c = (24 - 1) / 2.0
    ea = _mk(N=24)
    ea.seed_lane1(center=(c, c, c), sigma=4.0, frac=0.85, vent_into_seed=False)
    ea.freeze_wall_window()
    ea.drive_chiral_photon_at((c, c, c), helicity=1, sigma=4.0, wavelength=8.0,
                              amplitude=0.10, axis=2)
    eu = _mk(N=24)
    eu.seed_lane1(center=(c, c, c), sigma=4.0, frac=0.85, vent_into_seed=False)
    eu.freeze_wall_window()
    eu.drive_chiral_photon(helicity=1, sigma=4.0, wavelength=8.0, amplitude=0.10,
                           axis=2, center=(c, c, c))
    assert np.allclose(ea.w, eu.w, atol=0.0)
    # w_prev: inherited path copies w then assigns the two transverse comps;
    # additive path adds onto zeros — identical when nothing else seeded w.
    assert np.allclose(ea.w_prev, eu.w_prev, atol=1e-15)


# -------------------------------------------------------------------- K-HANDED
def test_k_handed_probe_separates_opposite_helicity():
    """The per-object photon-spin probe reads OPPOSITE signs on the fresh
    RH/LH pair and ≈0 on the achiral pair (probe validated on a known-
    different reference BEFORE any dynamics)."""
    e, _, _ = _two_object_build(hA=+1, hB=-1)
    mA, mB = e.half_masks(axis=0)
    sA = e.windowed_photon_spin(mA, axis=2)
    sB = e.windowed_photon_spin(mB, axis=2)
    assert sA != 0.0 and sB != 0.0
    assert np.sign(sA) == -np.sign(sB), (sA, sB)

    e0, _, _ = _two_object_build(hA=0, hB=0)
    s0A = e0.windowed_photon_spin(e0.half_masks(axis=0)[0], axis=2)
    assert abs(s0A) < 1e-9 * abs(sA)


# --------------------------------------------------------------------- K-BURST
def test_k_burst_fires_on_known_snap_and_silent_on_static_null():
    """Detector FIRES on a hand-opened pocket (v6 D6 known-positive) and stays
    SILENT (<= floor·mult) on the two-static-masses no-approach null."""
    # silent half: static pair, floor calibrated on itself, then scan a window
    e, _, _ = _two_object_build()
    e_floor = copy.deepcopy(e)
    floor = LongitudinalBurstDetector.calibrate_floor(e_floor, steps=40)
    det = LongitudinalBurstDetector(floor=max(floor, 1e-30), threshold_mult=3.0)
    det.record(e)
    for _ in range(40):
        e.step()
        det.record(e)
    assert det.scan() == [], "detector fired on the no-approach known-null"

    # firing half: hand-open a pocket (the known case) — released jumps
    e2, _, _ = _two_object_build()
    det2 = LongitudinalBurstDetector(floor=max(floor, 1e-30), threshold_mult=3.0)
    det2.record(e2)
    mask = np.zeros_like(e2.snap_mask)
    c = e2.N // 2
    mask[c - 1:c + 1, c - 1:c + 1, c - 1:c + 1] = True
    latent = e2.hand_snap_region(mask)
    det2.record(e2)
    assert latent > 0.0
    assert det2.scan(), "detector did NOT fire on the known hand-opened snap"


# ---------------------------------------------------------------------- K-MASS
def test_k_mass_probe_full_on_object_background_on_empty():
    """Interior conserved-functional mass: FULL (>0, ~seed-scale) on an isolated
    object; ≈0 on an empty box (so 'trapped → background' is a real read)."""
    c = (32 - 1) / 2.0
    e = _mk(N=32)
    e.seed_lane1(center=(c, c, c), sigma=4.0, frac=0.85, vent_into_seed=False)
    m = e.interior_mask()
    full = e.windowed_mass_cons(m)
    assert full > 1.0  # a frac=0.85, sigma=4 seed carries O(10) gradient energy

    e_empty = _mk(N=32)
    bg = e_empty.windowed_mass_cons(e_empty.interior_mask())
    assert bg < 1e-12 * full


# ----------------------------------------------------------------- K-TRANSPORT
def test_k_transport_imprint_bookkeeping_and_no_pump():
    """imprint_drift: (i) KE_approach equals the conserved-functional delta and
    is > 0; (ii) the imprint is localized to the masked object; (iii) the
    imprint's MARGINAL effect on the coast does not PUMP H_total^cons — the
    imprinted copy's positive excursion matches a no-imprint baseline of the
    SAME quiet config (photonless, so the live drive/converter transient of a
    fresh placement does not contaminate the transport-addition read)."""
    e, cA, _ = _two_object_build()
    mA, mB = e.half_masks(axis=0)
    massB_before = e.windowed_mass_cons(mB)
    ev_before = e.bulk_energy_conserved(True)
    book = e.imprint_drift((0.10, 0.0, 0.0), region_mask=mA)
    ev_after = e.bulk_energy_conserved(True)
    assert book["KE_approach"] > 0.0
    assert abs((ev_after - ev_before) - book["KE_approach"]) <= 1e-9 * max(ev_after, 1.0)
    # localized: the un-imprinted object's windowed mass is unchanged
    massB_after = e.windowed_mass_cons(mB)
    assert abs(massB_after - massB_before) <= 1e-9 * max(massB_before, 1e-30)

    # no-pump (marginal): QUIET config — seeds only, NO photon drive
    def _quiet():
        eq = _mk(N=32)
        c = (32 - 1) / 2.0
        eq.seed_lane1(center=(c - 6.0, c, c), sigma=4.0, frac=0.85, vent_into_seed=False)
        eq.seed_lane1(center=(c + 6.0, c, c), sigma=4.0, frac=0.85, vent_into_seed=False)
        eq.freeze_wall_window()
        return eq

    def _max_pos_excursion(eng, n=60):
        H0 = eng.total_energy_unified(conserved=True)
        Hmax = H0
        for _ in range(n):
            eng.step()
            Hmax = max(Hmax, eng.total_energy_unified(conserved=True))
        return (Hmax - H0) / (abs(H0) + 1e-30)

    base = _max_pos_excursion(_quiet())
    ei = _quiet()
    ei.imprint_drift((0.10, 0.0, 0.0), region_mask=ei.half_masks(axis=0)[0])
    imp = _max_pos_excursion(ei)
    assert imp <= base + 0.01, (
        f"transport imprint pumped H_total^cons: baseline {base:.4f} vs imprinted {imp:.4f}")
