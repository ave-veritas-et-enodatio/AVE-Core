"""v7 D13 QUADRATURE-DEPOSIT keepers — PROBE-CAPABILITY (ave-apparatus-floor-
attribution v1.1): the poloidal-projecting δπ_ω/δω LC-quadrature deposit, its
winding-capability validated on a KNOWN reference (plant-at-scale + rigid-null),
its lock-survival mechanism validated at the substep level, and every new knob
defaulting to the v6 byte-identical OFF path (the D-INHERIT regression gate).

  K-OFF             quadrature_deposit defaults False ⇒ the engine reproduces the
                    v6 RIGID ω-deposit path BIT-for-BIT (no v7 knob perturbs the
                    inherited dynamics when off).
  K-PLANT-AT-SCALE  the deposit pattern (α_pol=1, q_dep) planted ONCE into a clean
                    ω field at the run scale ⇒ extract_2_3_omega_fast reads
                    w_pol = q_dep, rel > 0.1 (the deposit IS winding-capable in the
                    read coordinate — else WINDING-TAKES is CLIP). [F-WPOL known-positive]
  K-RIGID-NULL      the rigid pattern (n̂×r, the v6 mode) planted at scale ⇒ the
                    extractor reads w_pol = 0 (the read DISTINGUISHES poloidal from
                    rigid; the v6 mode is correctly non-winding).
  K-HELICITY-ODD    a fresh RH vs LH deposit ⇒ the poloidal content reverses sign;
                    achiral ⇒ exactly 0 (helicity-odd FROM the field, not dialed).
  K-AM-LEDGER       the rigid 1:1 AM transfer is UNTOUCHED by the poloidal add-on:
                    S_photon_removed ≡ L_transferred; E_absorbed ≥ 0 (passive — the
                    poloidal energy is drawn from the photon-loss budget).
  K-LOCK-PRESERVES  the planted poloidal L-state survives ONE _lock_relax substep
                    (net-L removal does not contract it) while a planted rigid Ω×r
                    contracts by EXACTLY (1−η) — the structural-block mechanism is
                    real at the substep level (§3.4).

DERIVATION NOTE (surfaced, flag-don't-fix): the w_pol read winds
arg((ω·d̂)+i(π_ω·d̂)) around ψ, which PROVABLY requires a C-state ω·d̂ — a pure
δπ_ω (the prereg §3.3 sketch) plants no ω·d̂ and reads w_pol=0. So the v7 deposit
is the FULL LC quadrature (δω cos(qψ) + δπ_ω sin(qψ)), a DERIVED strengthening of
the sketch. K-PLANT-AT-SCALE / K-RIGID-NULL encode exactly that distinction.

Engine: src/ave/core/unified_genesis_engine.py (v7 D13 additions)
Prereg: research/2026-06-10_genesis-v7-quadrature_prereg.md (§3, §9)
"""

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast

PHI2 = ((1.0 + np.sqrt(5.0)) / 2.0) ** 2


def _torus_window(N, R, r):
    """The reading-torus tube window (the SAME locus extract_2_3_omega_fast reads
    on) — the known reference the deposit pattern is planted onto at run scale."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    xs, ys, zs = i - c, j - c, k - c
    rho = np.sqrt(xs ** 2 + ys ** 2)
    rtube = np.sqrt((rho - R) ** 2 + zs ** 2)
    return np.exp(-(rtube ** 2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)


def _planted_engine(N=48, q=3, alpha_pol=1.0, s_h=1.0, amp=0.2):
    """A clean engine with the v7 deposit pattern (α_pol, q) planted ONCE onto the
    reading-torus locus — the plant-at-scale capability reference."""
    R = 0.22 * N
    r = R / PHI2
    e = UnifiedGenesisEngine(N, omega_sector_on=True, buckle_on=False,
                             quadrature_deposit=True, alpha_pol=alpha_pol,
                             q_dep=q, p_dep=2, pol_R=R, pol_r=r)
    win = _torus_window(N, R, r)
    # the poloidal amplitude scales with α_pol exactly as the engine deposit does
    d_om, d_pi = e._quadrature_deposit_pattern(amp * alpha_pol, s_h, win)
    e.omega = d_om
    e.omega_prev = d_om - d_pi * e.dt  # so π_ω = (ω − ω_prev)/dt = d_pi exactly
    return e, R, r


def _rigid_pattern(N, win):
    """The v6 RIGID azimuthal δπ_ω = (ẑ×r)·win as a π_ω-only L-state (no C-state)."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    xs, ys = i - c, j - c
    d_pi = np.zeros((N, N, N, 3))
    d_pi[..., 0] = -ys * win
    d_pi[..., 1] = xs * win
    return d_pi


def _build_run(hel, chi, alpha_pol, *, lock, quad, q=3, eta=0.08, N=28, n=200):
    """The transducer-ISOLATED smoke config (buckle OFF; ω the only transducer
    recipient) — the clean reference for the ω/poloidal channel."""
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=False, omega_sector_on=True,
        buckle_on=False, lock_on=lock, lock_eta=eta, transducer_on=(chi > 0.0),
        chi_exch=chi, omega_recipient_frac=1.0, quadrature_deposit=quad,
        alpha_pol=alpha_pol, q_dep=q, pol_R=0.30 * N, pol_r=0.30 * N / PHI2)
    c = (N - 1) / 2.0
    e.seed_bulk((c, c, c), sigma=5.0, frac=0.95, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=hel, sigma=5.0, wavelength=8.0,
                          amplitude=0.10, axis=2)
    for _ in range(n):
        e.step()
    return e


# ───────────────────────────────── K-OFF (D-INHERIT byte-identical) ──────────
def test_k_off_quadrature_defaults_off_byte_identical_to_v6():
    """quadrature_deposit defaults False; the v7 engine reproduces the v6 RIGID
    ω-deposit path bit-for-bit (the ω field is IDENTICAL after stepping)."""
    def mk(quad):
        e = UnifiedGenesisEngine(
            26, bulk_density_on=True, snap_on=False, omega_sector_on=True,
            buckle_on=False, lock_on=True, transducer_on=True, chi_exch=0.02,
            omega_recipient_frac=1.0, quadrature_deposit=quad, alpha_pol=1.0)
        c = (26 - 1) / 2.0
        e.seed_bulk((c, c, c), sigma=4.0, frac=0.95, helical=False)
        e.freeze_wall_window()
        e.drive_chiral_photon(helicity=1, sigma=4.0, wavelength=8.0, amplitude=0.10)
        for _ in range(120):
            e.step()
        return e
    e_off = UnifiedGenesisEngine(24, omega_sector_on=True)
    assert e_off.quadrature_deposit is False, "v7 deposit must DEFAULT off"
    a = mk(False)
    b = mk(True)  # quad=True but alpha_pol path only ADDS poloidal; the rigid path is the same
    # the v6 RIGID transfer (L_transferred_omega, the axial AM channel) is UNTOUCHED
    assert a.L_transferred_omega == b.L_transferred_omega, "v6 AM ledger must be byte-identical"
    assert a.S_photon_removed == b.S_photon_removed, "v6 photon-loss ledger untouched"
    # and the OFF engine added NOTHING to the poloidal channel
    off2 = UnifiedGenesisEngine(
        26, bulk_density_on=True, snap_on=False, omega_sector_on=True,
        buckle_on=False, lock_on=True, transducer_on=True, chi_exch=0.02,
        omega_recipient_frac=1.0, quadrature_deposit=False)
    c = (26 - 1) / 2.0
    off2.seed_bulk((c, c, c), sigma=4.0, frac=0.95, helical=False)
    off2.freeze_wall_window()
    off2.drive_chiral_photon(helicity=1, sigma=4.0, wavelength=8.0, amplitude=0.10)
    om0 = off2.omega.copy()
    for _ in range(120):
        off2.step()
    a_om = mk(False).omega
    assert np.array_equal(a_om, off2.omega), "quad-OFF must be byte-identical across builds"
    assert off2.pol_deposit_accum == 0.0 and off2.pol_deposit_events == 0


# ──────────────────────── K-PLANT-AT-SCALE (F-WPOL known-positive) ───────────
def test_k_plant_at_scale_deposit_reads_w_pol_q():
    """The deposit PATTERN (α_pol=1, q_dep) planted at the run scale reads w_pol =
    q_dep with rel > 0.1 — the deposit is winding-capable in the read coordinate."""
    for q in (2, 3, 4):
        e, R, r = _planted_engine(N=48, q=q, alpha_pol=1.0)
        out = extract_2_3_omega_fast(e.omega, (e.omega - e.omega_prev) / e.dt, R, r, e.N)
        assert out["w_pol"] == q, f"deposit q={q} must read w_pol={q}, got {out['w_pol']}"
        assert out["w_pol_rel"] > 0.1, f"w_pol read must clear the reliability floor (q={q})"


# ─────────────────────────── K-RIGID-NULL (representation contrast) ──────────
def test_k_rigid_null_rigid_pattern_reads_w_pol_zero():
    """The v6 RIGID pattern (α_pol=0 / pure n̂×r, no C-state) planted at scale reads
    w_pol = 0 — the extractor DISTINGUISHES poloidal from rigid (the v6 mode is
    correctly non-winding; the prereg §3.3 pure-δπ_ω sketch reads 0)."""
    N = 48
    R = 0.22 * N
    r = R / PHI2
    win = _torus_window(N, R, r)
    e = UnifiedGenesisEngine(N, omega_sector_on=True)
    # (a) the rigid azimuthal L-state alone, into a CLEAN ω
    d_pi_rig = _rigid_pattern(N, win)
    out_rig = extract_2_3_omega_fast(np.zeros((N, N, N, 3)), d_pi_rig, R, r, N)
    assert out_rig["w_pol"] == 0, "the rigid azimuthal mode must read w_pol=0"
    # (b) the deposit at α_pol=0 (no poloidal component) plants NOTHING ⇒ w_pol=0
    e0, R0, r0 = _planted_engine(N=N, q=3, alpha_pol=0.0)
    assert float(np.max(np.abs(e0.omega))) == 0.0, "α_pol=0 ⇒ no poloidal C-state planted"
    out0 = extract_2_3_omega_fast(e0.omega, (e0.omega - e0.omega_prev) / e0.dt, R0, r0, N)
    assert out0["w_pol"] == 0, "α_pol=0 (no poloidal) must read w_pol=0 (the v6 control)"


# ──────────────────────────── K-HELICITY-ODD (m-even keeper) ─────────────────
def test_k_helicity_odd_poloidal_content_reverses_and_achiral_null():
    """The net-field poloidal content reverses sign RH↔LH and is EXACTLY 0 for the
    achiral (linear-pol) drive (the structural known-null, FROM the field)."""
    e_rh = _build_run(+1, 0.02, 1.0, lock=True, quad=True)
    e_lh = _build_run(-1, 0.02, 1.0, lock=True, quad=True)
    e_ac = _build_run(0, 0.02, 1.0, lock=True, quad=True)
    c_rh = e_rh.poloidal_quadrature_content()
    c_lh = e_lh.poloidal_quadrature_content()
    c_ac = e_ac.poloidal_quadrature_content()
    assert c_rh * c_lh < 0.0, "poloidal content must reverse sign with helicity"
    odd = abs(c_rh - c_lh) / (abs(c_rh) + abs(c_lh) + 1e-30)
    assert odd > 0.9, f"near-perfect reversal expected, got odd_frac={odd}"
    assert c_ac == 0.0, "achiral arm deposits EXACTLY zero poloidal content (structural null)"
    # and the planted-pattern twin (no dynamics): RH vs LH C-state/L-state sign flip
    e_p, R, r = _planted_engine(N=44, q=3, s_h=+1.0)
    e_m, _, _ = _planted_engine(N=44, q=3, s_h=-1.0)
    assert e_p.poloidal_quadrature_content() * e_m.poloidal_quadrature_content() < 0.0


# ──────────────────────── K-AM-LEDGER (conservation-by-channel) ──────────────
def test_k_am_ledger_1to1_preserved_and_passive_with_poloidal_addon():
    """The poloidal winding is added ON TOP of the v6 1:1 rigid AM transfer, so the
    AM ledger STILL closes 1:1 (S_photon_removed ≡ L_transferred) and the wall stays
    PASSIVE (E_absorbed ≥ 0 — the poloidal energy is drawn from the photon-loss
    budget, never pumped)."""
    e = _build_run(+1, 0.02, 1.0, lock=True, quad=True)
    led = e.transducer_ledger()
    assert abs(led["ledger_ratio_removed_over_transferred"] - 1.0) < 1e-9, "1:1 AM closure"
    assert abs(led["L_transferred"] - (led["L_transferred_u"] + led["L_transferred_omega"])) < 1e-12
    assert led["E_photon_loss"] >= 0.0, "the photon only ever PAYS energy"
    assert led["passive_no_pump"], "E_absorbed ≥ 0 — passive even with the poloidal add-on"
    assert led["E_pol_deposit"] >= 0.0 and led["pol_deposit_events"] > 0


# ─────────────────── K-LOCK-PRESERVES (the D14 mechanism keeper) ─────────────
def test_k_lock_preserves_poloidal_and_contracts_rigid():
    """ONE _lock_relax substep: a planted POLOIDAL L-state survives (the net-L
    removal does NOT contract it — zero-net-L) while a planted RIGID Ω×r contracts
    by EXACTLY (1−η). The structural-block mechanism is real at the substep level."""
    N = 36
    R = 0.26 * N
    r = R / PHI2
    win = _torus_window(N, R, r)
    eta = 0.08

    def lock_ratio(d_pi):
        """|L_ω| after one _lock_relax / before, with π_ω planted as d_pi."""
        e = UnifiedGenesisEngine(N, omega_sector_on=True, lock_on=True, lock_eta=eta)
        e.omega = np.zeros((N, N, N, 3))
        omega_new = e.omega + d_pi * e.dt        # so provisional π_ω = d_pi
        rx, ry, rz = e._lock_rx, e._lock_ry, e._lock_rz
        pw0 = (omega_new - e.omega) / e.dt
        L0 = np.array([
            np.sum(ry * pw0[..., 2] - rz * pw0[..., 1]),
            np.sum(rz * pw0[..., 0] - rx * pw0[..., 2]),
            np.sum(rx * pw0[..., 1] - ry * pw0[..., 0])])
        om_d, _ = e._lock_relax(omega_new)
        pw1 = (om_d - e.omega) / e.dt
        L1 = np.array([
            np.sum(ry * pw1[..., 2] - rz * pw1[..., 1]),
            np.sum(rz * pw1[..., 0] - rx * pw1[..., 2]),
            np.sum(rx * pw1[..., 1] - ry * pw1[..., 0])])
        norm0 = float(np.sqrt(np.sum(pw0 ** 2)))
        norm1 = float(np.sqrt(np.sum(pw1 ** 2)))
        return L0, L1, norm0, norm1

    # RIGID Ω×r ⇒ net-L ≠ 0 ⇒ L contracts by EXACTLY (1−η)
    d_rig = _rigid_pattern(N, win)
    L0r, L1r, _, _ = lock_ratio(d_rig)
    assert np.linalg.norm(L0r) > 1e-6, "the rigid pattern must carry net L"
    # the ẑ×r net-L is purely axial (z); the off-axis components are machine noise
    ax = int(np.argmax(np.abs(L0r)))
    assert ax == 2, "the rigid azimuthal mode's net-L is axial (z)"
    np.testing.assert_allclose(L1r[ax], (1.0 - eta) * L0r[ax], rtol=1e-9,
                               err_msg="rigid net-L must contract by exactly (1−η)")

    # POLOIDAL quadrature L-state ⇒ net-L ≈ 0 ⇒ the L2 norm is PRESERVED (not drained)
    e = UnifiedGenesisEngine(N, omega_sector_on=True, quadrature_deposit=True,
                             q_dep=3, p_dep=2, pol_R=R, pol_r=r)
    _, d_pi_pol = e._quadrature_deposit_pattern(0.2, +1.0, win)
    L0p, L1p, n0p, n1p = lock_ratio(d_pi_pol)
    assert np.linalg.norm(L0p) < 0.05 * np.linalg.norm(L0r), "poloidal must be ~zero-net-L"
    assert n1p > 0.999 * n0p, f"poloidal L-state must SURVIVE the lock (norm {n1p}/{n0p})"
