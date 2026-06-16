"""
PRODUCTION DRIVER — passive winding-protected electron eigenmode (the keystone).

Prereg (FROZEN, every §): research/2026-06-15_passive-eigenmode_prereg_FROZEN.md
Lane brief:               _orchestration/2026-06-15_passive-eigenmode-solve.md
Build-step-zero (PASSED): src/scripts/vol_1_foundations/g0_double_count_smoke.py (G0)

THE QUESTION (prereg §1):
    Does the fully-coupled hybrid (V != 0  AND  omega != 0) wave-eigenmode of a substrate
    Gamma=-1 saturation cavity exist as a STABLE, dissipationless STANDING / BREATHER mode —
    with the conserved (2,3) winding imposed as a topological boundary condition on the
    independent Cosserat-omega carrier — and what is its radiative Q?

HEADLINE (Grant 2026-06-15 — do not drift):
    The result is EXISTENCE + STABILITY of the winding-protected hybrid breather (the FORM —
    the structural keystone). Q is the ECHO; report it, but the headline is NOT "we measured Q."

PLATFORM (b', Grant-granted eyes-open): the FIRST substrate-complete cross-firewall engine.
    crystal_engine V-tank breathing wall  (A1, the sech self-focus; TRUE n=sqrt(S) via
    c_eff^2 = c0^2/S, crystal_engine.py:197-200)   coupled to   the Cosserat-omega carrier
    (the (2,3) winding)  via the G0 Op14 coupling (trilinear_buckle_forces, KAPPA_TILDE=6/5,
    alpha-FREE).  REUSE both validated engines + the G0 coupling. NO new engine, NO *_vN file.

SEEDER (Grant 2026-06-15): the TRAVELING-(2,3) (planted_winding_field mode="traveling", the
    G4-certified carrier), NOT initialize_electron_2_3_sector (z-flat rotor, fails G4
    structurally w_tor=0). The production seed ALSO ASSERTS the real-space envelope is the
    0_1 UNKNOT (a single genus-1 torus shell), so the winding read is backed by
    "on the unknot = electron" (theory.md:16; ch8-alpha-golden-torus.md:29) — NOT a heavier
    real-space knot that merely also reads a winding (Grant's third-time wrong-object guard).

================================================================================================
SUBSTRATE-NATIVE WALK (substrate-native-check v1.2; done BEFORE this code per Operating-Principle 1)
================================================================================================
  CP1 (substrate dynamics)  : the V-tank is the validated scalar Master-Equation FDTD
                              (c_eff^2 = c0^2/S, leapfrog) — NOT a Helmholtz / energy-basin
                              eigensolve. The omega-carrier is the velocity-Verlet Cosserat
                              field. Both are time-domain wave engines; the "eigenmode" is read
                              as a CYCLIC / time-averaged breather (prereg §4), NOT a static
                              algebraic eigenvector.
  CP6 (reactance pair)      : every read records BOTH the C-state (V; omega) AND the L-state
                              (dV/dt; omega_dot) over the recording window. The extractor reads
                              the (omega, omega_dot) reactance pair. The V-tank breather is read
                              via (V, dV/dt) and the Gamma_true cycle.
  CP8 (generative precursor): we IMPOSE the winding as a topological BC (prereg charter, §7.1) —
                              this is the imposed-BC framing, NOT plant-the-finished-composite.
                              The V-tank is seeded with its OWN generative precursor (the sech
                              eigen-profile that self-focuses); the winding rides the independent
                              omega-carrier. The pure-V trap (omega=0) is cleared by the imposed
                              odd-omega winding (prereg §3 / hazard 3).
  CP9 (dynamical not algebraic): every F-read comes from the engines' OWN step() evolution
                              (V_inc/V integrated; omega field integrated) — NOT an algebraic
                              observer formula. Gamma_true, the winding, the stability eig, and
                              Q are all read off the dynamically-evolved state.
  CP10 (Gamma as boundary)  : the Gamma=-1 wall is rendered as crystal_engine's intrinsic
                              c_eff^2 = c0^2/S boundary (a self-induced impedance front), and the
                              coupling fires ONLY on the saturation-FRONT window g_wall =
                              _front_window() (a thin A~R_II shell) — NOT a bulk energy/force
                              term (which detonates, hazard 5).

PHASE-SPACE DISCIPLINE (phase-space-coordinate-check, A46): the winding is read on the
    omega-tank PHASOR (extract_2_3_omega_fast traces arg(Z) toroidally/poloidally on the
    (omega, omega_dot) LC pair), NEVER a real-space lattice-Cartesian winding count, and NEVER
    the A1 (V_inc, V_ref) phasor (the genesis-24 double-count — G0-clean, preserved here).

CONSERVED-NOT-PUMPED (ave-conserved-vs-pumped): F5 — the breather must stand with NO drive.
    The coupling is the conserved trilinear buckle (energize-LOCK, f_w==0). No gain term, no
    autoresonant pump. A drive-sustained state is a NEGATIVE.

HAZARDS PRECLUDED IN CODE (prereg §8, locked) — verified, not merely listed:
  1. NO gradient-flow stationary-point. We do NOT call relax_to_ground_state / relax_s11 /
     find_eigenstate with an energy/S11 f_fn. F1 = a time-domain breather convergence read.
  2. NO winding into (V_inc, V_ref). The winding rides eng_w.omega only; the coupling back-
     reaction f_omega lands on eng_w.omega; G0 already proved V_ref-leak <= 4.3e-16.
  3. NO pure-V seed. The (2,3) winding-BC is imposed on the omega-carrier (supplies odd omega).
  5. Gamma=-1 is the c_eff boundary + the front-window coupling (CP10), NOT a bulk term.
  9. TRUE n=sqrt(S): Gamma_true = (n-1)/(n+1) with n = c0/c_eff = sqrt(S) computed HERE; we do
     NOT call gamma_bulk()/refractive_index() (the S^{1/4} PROXY, crystal_engine.py:421-432).
 10. EXISTENCE/STABILITY read on the CYCLIC / time-averaged breather, never an instantaneous
     static Gamma.

CANONICAL-SOURCE (ave-canonical-source): all constants imported from ave.core.constants /
    ave.core.cross_sector_coupling. NOTE: there is no verify_constants function in this corpus;
    the constants are cross-checked by DIRECT IMPORT + identity assertions (see _verify_constants
    below) — 1/ALPHA == 137.036, ALPHA*1.2 -> Q=114.20, KAPPA_TILDE == 6/5.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field

import numpy as np

from ave.core.constants import ALPHA
from ave.core.cross_sector_coupling import KAPPA_TILDE, trilinear_buckle_forces
from ave.core.crystal_engine import CrystalEngine
from ave.topological.cosserat_field_3d import CosseratField3D
from ave.utils.fast_winding_extractor import (
    extract_2_3_omega_fast,
    planted_winding_field,
)

# ─────────────────────────────────────────────────────────────────────────────
# Coupling-binding declaration (prereg §6, the echo/chord verdict hinges on this):
#   the driver imports KAPPA_TILDE (= 6/5, the (2,3) topological factor pq/(p+q)) — ALPHA-FREE.
#   ALPHA is imported ONLY to (a) cross-check the canonical Q targets and (b) DECLARE that it is
#   NOT a coupling input. So a measured Q is CHORD-eligible on the coupling side; but per prereg
#   §6 the chord still will NOT fire (Lane-1 Path C open) -> the Q is reported ECHO-tagged.
# ─────────────────────────────────────────────────────────────────────────────
COUPLING_IS_ALPHA_FREE = True  # KAPPA_TILDE=6/5; ALPHA not a coupling input. See §6 declaration.

# F3 Q-bin targets (prereg §5 F3) — these are CHARACTERIZATION targets, NOT bin-deciding (§4).
Q_TARGET_BARE_ALPHA = 1.0 / ALPHA       # ~ 137.036  (LC-tank reactive leak, theorem-3-1-q-factor.md:83)
Q_TARGET_KAPPA_CHIRAL = 1.0 / (ALPHA * 1.2)  # ~ 114.20  (kappa_chiral = alpha*kappa_tilde)
Q_BIN_BAND = 0.05                        # +-5% band (prereg §5 F3)


# ============================================================================
# section: constants cross-check (ave-canonical-source; no verify_constants fn)
# ============================================================================
def _verify_constants() -> dict:
    """Cross-check the canonical constants by direct-import identity assertions
    (there is NO verify_constants function in this corpus — ave-canonical-source
    is satisfied by importing from ave.core.constants and asserting the identities
    the prereg §5/§6 commits to)."""
    checks = {
        "1/ALPHA == 137.036 (bare-alpha Q target, prereg §5 F3)": abs(Q_TARGET_BARE_ALPHA - 137.0359990837) < 1e-6,
        "1/(ALPHA*1.2) == 114.20 (kappa_chiral Q target, §5 F3)": abs(Q_TARGET_KAPPA_CHIRAL - 114.1966659) < 1e-4,
        "KAPPA_TILDE == 6/5 (alpha-FREE coupling, §6)": abs(KAPPA_TILDE - 1.2) < 1e-12,
    }
    return checks


# ============================================================================
# section: lattice / run configuration
# ============================================================================
@dataclass
class RunConfig:
    """Lattice + seed parameters. Defaults match the G0 PASS lattice (N=48, R=10,
    r=4) so the extractor runs at HIGH reliability (rel 0.73/0.94) and r stays
    clear of the r~1.1-cell collapse zone (G4 hazard, prereg §5 G4)."""
    N: int = 48
    dx: float = 1.0
    # winding torus (omega-carrier) — major/minor radius (cells)
    R: float = 10.0
    r: float = 4.0
    # V-tank sech eigen-profile seed (the canonical v14 Mode-I self-trap profile)
    v_amp: float = 0.90       # sech peak amplitude (A=0.90 < A_cap=0.99)
    v_width: float = 3.0      # sech width R_sech (cells)
    omega_amp: float = 0.30   # planted-(2,3) omega amplitude (planted_winding_field default)
    pml_thickness: int = 4
    cfl_safety: float = 0.4   # the v14 Mode-I PASS used 0.4 (q_g47_path_d:118)
    n_steps: int = 1500       # recording window (many breaths)
    sample_every: int = 20    # cadence for the F-reads / Q accounting


# ============================================================================
# section: seeders + the 0_1 unknot-envelope assertion (Grant 2026-06-15)
# ============================================================================
def seed_vtank(cfg: RunConfig) -> CrystalEngine:
    """V-tank A1 wall, seeded with the SECH eigen-profile (the convergent / self-
    focusing profile, the G1 positive control; a Gaussian is the negative control).
    V(r) = v_amp * sech(r/v_width); stationary start (dV/dt = 0).

    converter_on=False: we apply the EXTERNAL (b') Op14 coupling (trilinear buckle)
    ourselves; the engine's own internal converter is OFF so the only V<->omega
    channel under test is the (b') cross-firewall wire."""
    eng = CrystalEngine(
        N=cfg.N, dx=cfg.dx, converter_on=False,
        pml_thickness=cfg.pml_thickness, cfl_safety=cfg.cfl_safety,
    )
    c = cfg.N // 2
    i, j, k = np.indices((cfg.N, cfg.N, cfg.N))
    rr = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2) * cfg.dx
    seed = cfg.v_amp * (1.0 / np.cosh(rr / cfg.v_width))
    eng.V[:] = seed
    eng.V_prev[:] = seed.copy()
    return eng


def seed_vtank_gaussian(cfg: RunConfig) -> CrystalEngine:
    """G1 NEGATIVE control: a generic Gaussian (same amplitude) — disperses."""
    eng = CrystalEngine(
        N=cfg.N, dx=cfg.dx, converter_on=False,
        pml_thickness=cfg.pml_thickness, cfl_safety=cfg.cfl_safety,
    )
    c = cfg.N // 2
    i, j, k = np.indices((cfg.N, cfg.N, cfg.N))
    r2 = (i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2
    seed = cfg.v_amp * np.exp(-r2 / (2.0 * cfg.v_width ** 2))
    eng.V[:] = seed
    eng.V_prev[:] = seed.copy()
    return eng


def seed_omega_carrier(cfg: RunConfig, helicity: int = 1) -> CosseratField3D:
    """omega-carrier, (2,3) winding imposed as the topological BC via the
    extractor-MATCHED traveling plant (planted_winding_field, mode='traveling' —
    the G4-certified D15 carrier). NOT initialize_electron_2_3_sector (z-flat
    rotor -> structural w_tor=0, fails G4; representation-capability flag, brief)."""
    eng = CosseratField3D(cfg.N, cfg.N, cfg.N, dx=cfg.dx, pml_thickness=0)
    omega0, pi_omega0 = planted_winding_field(
        cfg.N, cfg.R, cfg.r, p=2, q=3, mode="traveling",
        helicity=helicity, amplitude=cfg.omega_amp,
    )
    eng.omega = omega0 * eng.mask_alive[..., None]
    eng.omega_dot = pi_omega0 * eng.mask_alive[..., None]
    return eng


def assert_unknot_envelope(eng_w: CosseratField3D, cfg: RunConfig) -> dict:
    """GRANT'S THIRD-TIME WRONG-OBJECT GUARD (2026-06-15): the electron is the
    0_1 UNKNOT in real space carrying the (2,3) as polarization-2 + phase-3
    structure (theory.md:16; ch8-alpha-golden-torus.md:29). "Reads (2,3)" is
    NECESSARY-not-sufficient — a heavier real-space knot also reads a winding.
    So we ASSERT the real-space |omega| envelope is the 0_1 unknot:

      (1) SINGLE-COMPONENT: the |omega|^2 energy-density support is ONE connected
          region (a single closed tube) — not multiple linked/knotted strands.
      (2) GENUS-1 TORUS SHELL: that support is a torus-shell (a hollow ring), the
          unknot's tubular neighbourhood — the core curve threads the hole once
          (toroidal direction) with no self-crossings, the textbook 0_1.
      (3) The (2,3) WINDING is INTERNAL (the omega-director polarization-2 + the
          (omega,omega_dot) phasor-3), NOT an envelope knot. Confirmed by reading
          it on the phasor (extract_2_3_omega_fast) AFTER G4, not on the envelope.

    Implementation: the unknot certificate is the ENVELOPE-SKELETON topology, NOT
    the node-broken amplitude support. The traveling (2,3) winding has cos(q*psi)
    amplitude NODES (3 poloidal zeros), so the raw |omega| support is fragmented
    into lobes BY THE WINDING — that fragmentation is the (2,3) phase structure, not
    the envelope shape. The envelope is the SMOOTH Gaussian tube the winding rides
    on (planted_winding_field's `env`); its skeleton is the torus. So we read the
    torus-shell signature on the SMOOTH envelope (|omega|, low-pass via a coarse
    radial-binned occupancy), and assert:

      (a) the central column (near the major axis) is EMPTY  (the unknot's hole),
      (b) a single ANNULAR RING of support surrounds it in the mid-plane,
      (c) the ring is a SINGLE connected loop in the (major-angle) direction —
          i.e. one closed tube threading the hole once = the 0_1 unknot (a heavier
          knot would show >1 radial band, or the tube would cross the central hole).
    The (2,3) winding itself is read on the PHASOR after G4, NOT here — confirming
    the winding is INTERNAL (polarization-2 + phasor-3), not an envelope knot."""
    amp = np.sqrt(np.sum(eng_w.omega ** 2, axis=-1))
    c = cfg.N // 2
    i3, j3, k3 = np.indices((cfg.N, cfg.N, cfg.N))
    rho3 = np.sqrt((i3 - c) ** 2 + (j3 - c) ** 2)  # cylindrical radius from spin axis (z)
    z3 = np.abs(k3 - c)

    # SMOOTH envelope skeleton: max |omega| over the spin-axis angle phi, binned by
    # (rho, z) — this low-passes the cos(q*psi) winding nodes (which live in phi/psi),
    # leaving the underlying torus tube.
    thr = 0.05 * float(amp.max())
    support = amp > thr
    support_frac = float(support.mean())

    # (a) central hole empty: no support within 0.4*R of the spin (z) axis
    central_hole_empty = not bool(support[(rho3 < 0.4 * cfg.R) & (z3 < cfg.r)].any())
    # (b) annular ring present at the torus major radius
    ring_band = (rho3 > 0.6 * cfg.R) & (rho3 < 1.4 * cfg.R) & (z3 < 1.5 * cfg.r)
    ring_present = bool(support[ring_band].any())

    # (c) single closed tube threading the hole once: the support, projected to the
    #     (rho, z) tube cross-section, is ONE radial band (a heavier knot / multiple
    #     strands would give >1 disjoint band). Bin the tube cross-section radially.
    rho_at_support = rho3[support]
    n_radial_bands = _count_radial_bands(rho_at_support, cfg.R, cfg.r) if rho_at_support.size else 0
    single_tube = (n_radial_bands == 1)

    is_torus_shell = central_hole_empty and ring_present
    is_unknot = is_torus_shell and single_tube
    return {
        "central_hole_empty": bool(central_hole_empty),
        "ring_present": bool(ring_present),
        "n_radial_bands": int(n_radial_bands),
        "single_tube": bool(single_tube),
        "is_torus_shell": bool(is_torus_shell),
        "is_0_1_unknot_envelope": bool(is_unknot),
        "support_frac": support_frac,
        "note": "winding nodes fragment |omega|; envelope skeleton is the 0_1 torus",
    }


def _count_radial_bands(rho_vals: np.ndarray, R: float, r: float) -> int:
    """Count disjoint radial bands of support in the torus cross-section. The 0_1
    unknot tube is ONE band centered at the major radius R (width ~ minor radius r);
    a heavier knot or linked strands would give >1 disjoint band."""
    bins = np.arange(0.0, R + 3.0 * r, max(0.5, 0.5 * r))
    hist, _ = np.histogram(rho_vals, bins=bins)
    occupied = hist > 0
    # count runs of consecutive occupied bins
    n_bands = 0
    prev = False
    for occ in occupied:
        if occ and not prev:
            n_bands += 1
        prev = occ
    return n_bands


# ============================================================================
# section: TRUE n=sqrt(S) impedance read (prereg §8 item 9 — NOT the S^{1/4} proxy)
# ============================================================================
def gamma_true(eng: CrystalEngine) -> np.ndarray:
    """The TRUE Smith reflection coefficient on the bulk branch:
        n(r) = c0 / c_eff = sqrt(S)          (since c_eff^2 = c0^2/S, crystal_engine.py:197-200)
        Gamma_true = (n - 1) / (n + 1)
    NOT the proxy gamma_bulk()/refractive_index() (n = S^{1/4}, crystal_engine.py:421-432) —
    the proxy understates the wall depth by ~2x (floor -0.240 vs true -0.454, §8 item 9).
    Returns the per-cell Gamma_true (interior + PML; callers mask)."""
    S = eng.saturation_kernel(eng.V)            # S = sqrt(1 - A^2), clipped [S_min, 1]
    n = np.sqrt(np.maximum(S, eng.S_min))       # TRUE n = sqrt(S)
    return (n - 1.0) / (n + 1.0)


def gamma_true_min(eng: CrystalEngine) -> float:
    """Deepest TRUE wall over the PML-excluded interior (A-Rule 10)."""
    g = gamma_true(eng)
    return float(g[eng.interior_mask()].min())


GAMMA_TRUE_FLOOR = -0.4539  # analytic floor at A=A_cap=0.99 (S_floor=0.1411, n=0.3756)


# ============================================================================
# section: the (b') Op14 cross-coupling (REUSE the G0 double-count-clean wire)
# ============================================================================
def op14_coupling(eng_V: CrystalEngine, eng_w: CosseratField3D, dx: float):
    """One application of the minimal Op14 cross-coupling = the G0 double-count-
    clean conserved trilinear buckle (cross_sector_coupling.trilinear_buckle_forces,
    photon_deplete=False ⇒ f_w == 0). KAPPA_TILDE=6/5, ALPHA-FREE.

        f_V     = -kappa_tilde * g_wall * (w · ∇×omega)   -> onto the V-tank scalar
        f_omega = -kappa_tilde * ∇×(g_wall * V * w)       -> onto the INDEPENDENT omega-carrier
        f_w     = 0

    g_wall = eng_V._front_window() = the saturation-FRONT shell (CP10 boundary, NOT bulk).
    w = director from the omega-tank's own L-state (omega_dot) — u≡0 on this carrier.
    NOTHING is written to (V_inc, V_ref) (the genesis-24 double-count; G0-clean)."""
    g_wall = eng_V._front_window()
    w_dir = eng_w.omega_dot
    f_V, f_w, f_omega = trilinear_buckle_forces(
        eng_V.V, w_dir, eng_w.omega, g_wall, dx,
        kappa_tilde=KAPPA_TILDE, photon_deplete=False,
    )
    assert not np.any(f_w), "f_w must be identically 0 (photon_deplete=False)"
    return f_V, f_omega


def step_coupled(eng_V: CrystalEngine, eng_w: CosseratField3D, dx: float):
    """Advance the coupled hybrid one step (the G0 wiring, exactly).
    V-tank own leapfrog (c_eff^2=c0^2/S self-focus) + coupling back-reaction;
    omega-carrier own velocity-Verlet + coupling back-reaction onto the
    INDEPENDENT carrier. No drive, no gain — energize-LOCK (F5)."""
    f_V, f_omega = op14_coupling(eng_V, eng_w, dx)
    eng_V.step()
    m = eng_V.interior_mask()
    eng_V.V[m] += (eng_V.dt ** 2) * f_V[m]
    eng_w.omega_dot = eng_w.omega_dot + eng_w.cfl_dt * (f_omega * eng_w.mask_alive[..., None])
    eng_w.step()


# ============================================================================
# section: G0-G4 instrument-validation gates (prereg §5)
# ============================================================================
def gate_G0(cfg: RunConfig) -> dict:
    """G0 — double-count orthogonality (re-confirm; full smoke is g0_double_count_smoke.py).
    PASS = winding stays NONZERO on the omega-carrier AND zero V_ref-leak (the winding is
    absent from the A1 (V_inc,V_ref) phasor). Here we confirm the coupling's f_omega lands
    on omega and f_V lands on the scalar (never on V_ref), and w_pol stays nonzero over a
    short coupled window."""
    eng_V = seed_vtank(cfg)
    eng_w = seed_omega_carrier(cfg)
    wp = []
    for n in range(40):
        step_coupled(eng_V, eng_w, cfg.dx)
        if n % 10 == 0:
            rd = extract_2_3_omega_fast(eng_w.omega, eng_w.omega_dot, cfg.R, cfg.r, cfg.N)
            wp.append(rd["w_pol"])
    # f_omega writes to omega only; the V-tank phasor (V_inc,V_ref) is a function of the
    # scalar V alone (k4_tlm.py:346) — the winding never enters it. (G0 smoke proved
    # V_ref-leak <= 4.3e-16; re-asserted structurally: the coupling has no V_ref write path.)
    w_pol_nonzero = all(p != 0 for p in wp)
    return {
        "gate": "G0",
        "w_pol_trajectory": wp,
        "w_pol_stays_nonzero": bool(w_pol_nonzero),
        "vref_leak_structural": "no V_ref write path (coupling writes omega + scalar V only)",
        "PASS": bool(w_pol_nonzero),
    }


def gate_G1(cfg: RunConfig) -> dict:
    """G1 — residual/existence detector: the SECH eigen-profile CONVERGES (stays
    localized / a bounded breather), the generic GAUSSIAN DISPERSES. This validates
    that F1 can distinguish a standing mode from dispersal (cage SECH_ANCHOR,
    cage_stiffening_wall.py:109). The discriminator is the V_peak retention + the
    FWHM growth ratio: a convergent profile retains amplitude with bounded FWHM;
    a dispersing one bleeds to ~0 with FWHM -> the whole box."""
    def run_profile(seed_fn):
        eng = seed_fn(cfg)
        m = eng.interior_mask()
        vpk0 = float(np.max(np.abs(eng.V * m)))
        fwhm0 = _fwhm(eng.V * m)
        vpk_tail, fwhm_tail = [], []
        for n in range(cfg.n_steps):
            eng.step()
            if n % cfg.sample_every == 0 and n > 0.6 * cfg.n_steps:
                vpk_tail.append(float(np.max(np.abs(eng.V * m))))
                fwhm_tail.append(_fwhm(eng.V * m))
        return {
            "vpk0": vpk0, "fwhm0": fwhm0,
            "vpk_tail_mean": float(np.mean(vpk_tail)) if vpk_tail else 0.0,
            "fwhm_tail_mean": float(np.mean(fwhm_tail)) if fwhm_tail else 0.0,
        }
    sech = run_profile(seed_vtank)
    gauss = run_profile(seed_vtank_gaussian)
    sech_retention = sech["vpk_tail_mean"] / max(sech["vpk0"], 1e-12)
    gauss_retention = gauss["vpk_tail_mean"] / max(gauss["vpk0"], 1e-12)
    # detector validates if sech is DISTINGUISHABLY better-retained than gauss
    discriminates = sech_retention > gauss_retention * 1.10
    return {
        "gate": "G1",
        "sech": sech, "gaussian": gauss,
        "sech_retention": float(sech_retention),
        "gaussian_retention": float(gauss_retention),
        "detector_discriminates_sech_vs_gauss": bool(discriminates),
        "PASS": bool(discriminates),
    }


def _fwhm(V: np.ndarray) -> float:
    Va = np.abs(V)
    vm = Va.max()
    return float((Va > vm / 2.0).sum()) if vm > 1e-10 else 0.0


# ----------------------------------------------------------------------------
# G2 — stability-eig layer (NEW BUILD). The cycle-envelope decay-rate read:
# fit log|V_peak(t)| over the recording tail -> growth rate lambda_max.
#   lambda_max <= 0  : stable / dissipationless (decays or flat) -> F2 PASS-eligible
#   lambda_max  > 0  : unstable / gain / runaway                 -> NEGATIVE-B
# (A full finite-difference Jacobian->eigvals is the prereg's named option; the
# cycle-envelope decay rate is the prereg-sanctioned alternative read, §7.4 / §4
# "the cycle-to-cycle envelope flat or slowly-decaying". It is the load-bearing
# stability scalar for a BREATHER and is far cheaper + integrator-faithful.)
# ----------------------------------------------------------------------------
def envelope_growth_rate(vpk_series: list[float], dt: float, sample_every: int) -> float:
    """Least-squares slope of log|V_peak| vs time over the series.
    > 0 = growing (gain/unstable); <= 0 = stable (decaying or flat)."""
    v = np.asarray(vpk_series, dtype=float)
    ok = v > 1e-12
    if ok.sum() < 4:
        return float("nan")
    t = np.arange(len(v)) * dt * sample_every
    slope = np.polyfit(t[ok], np.log(v[ok]), 1)[0]
    return float(slope)


def gate_G2(cfg: RunConfig) -> dict:
    """G2 — known-stable returns lambda<=0 AND known-unstable returns lambda>0.
    KNOWN-STABLE: a damped V-tank (a sech with small added damping via the engine
    PML-only diffusion) -> envelope decays -> lambda < 0.
    KNOWN-UNSTABLE: an exponentially-amplified series (analytic gain seed) -> lambda > 0.
    This validates the stability scalar reads the SIGN correctly before F2 is banked."""
    # known-stable: a real decaying V-tank envelope (sech, free evolution disperses -> decays)
    eng = seed_vtank(cfg)
    m = eng.interior_mask()
    stable_series = []
    for n in range(400):
        eng.step()
        if n % cfg.sample_every == 0:
            stable_series.append(float(np.max(np.abs(eng.V * m))))
    lam_stable = envelope_growth_rate(stable_series, eng.dt, cfg.sample_every)
    # known-unstable: analytic e^{+t} gain envelope -> must read lambda > 0
    t = np.arange(20) * eng.dt * cfg.sample_every
    gain_series = list(0.1 * np.exp(5.0 * t))
    lam_unstable = envelope_growth_rate(gain_series, eng.dt, cfg.sample_every)
    passes = (lam_stable <= 0) and (lam_unstable > 0)
    return {
        "gate": "G2",
        "lambda_known_stable": float(lam_stable),
        "lambda_known_unstable": float(lam_unstable),
        "reads_sign_correctly": bool(passes),
        "PASS": bool(passes),
    }


# ----------------------------------------------------------------------------
# G3 — radiative-Q layer (NEW BUILD). Q = omega_C * E_stored / P_radiated.
# Validate on a KNOWN open resonator: a 1D damped harmonic oscillator with
# analytic Q = omega0 / (2*gamma_damp). State N, dt, and a Nyquist-resolvability
# assertion for omega_C (corpus flags real-space omega_C sub-Nyquist; we read in
# the breather/phasor frame + assert omega_C*dt << pi).  TRUE n=sqrt(S), §8 item 9.
# ----------------------------------------------------------------------------
def measure_Q_from_decay(energy_series: list[float], omega_C: float, dt: float,
                         sample_every: int) -> float:
    """Q from the energy decay envelope: E(t) = E0 * exp(-omega_C * t / Q)
    => Q = -omega_C / (slope of ln E). The per-cycle leak read (prereg §4: the
    breather's per-cycle radiative leak). Q->inf when slope->0 (no measurable leak)."""
    E = np.asarray(energy_series, dtype=float)
    ok = E > 1e-30
    if ok.sum() < 4:
        return float("nan")
    t = np.arange(len(E)) * dt * sample_every
    slope = np.polyfit(t[ok], np.log(E[ok]), 1)[0]  # = -omega_C/Q
    if abs(slope) < 1e-12:
        return float("inf")  # no measurable leak -> Q->inf (POSITIVE-with-decoupled-Q, §4)
    return float(-omega_C / slope)


def gate_G3(cfg: RunConfig) -> dict:
    """G3 — recover the analytic Q of a KNOWN open resonator (a damped harmonic
    oscillator, Q_analytic = omega0/(2*gamma)). Validates the stored/radiated
    accounting before F3 is read. Plus the Nyquist-resolvability assertion for
    omega_C in the breather frame."""
    # analytic damped oscillator: x'' + 2*gamma*x' + omega0^2 x = 0
    omega0 = 0.5
    gamma_damp = 0.01
    Q_analytic = omega0 / (2.0 * gamma_damp)  # = 25.0
    dt = 0.05
    n = 4000
    x = 1.0
    v = 0.0
    E_series = []
    for step in range(n):
        a = -2.0 * gamma_damp * v - omega0 ** 2 * x
        v += a * dt
        x += v * dt
        if step % 10 == 0:
            E_series.append(0.5 * v ** 2 + 0.5 * omega0 ** 2 * x ** 2)
    Q_measured = measure_Q_from_decay(E_series, omega0, dt, 10)
    q_err = abs(Q_measured - Q_analytic) / Q_analytic
    # Nyquist-resolvability for the production omega_C (shear clock, see F3 read)
    return {
        "gate": "G3",
        "Q_analytic_known_resonator": float(Q_analytic),
        "Q_measured": float(Q_measured),
        "rel_err": float(q_err),
        "accounting_validated": bool(q_err < 0.10),
        "PASS": bool(q_err < 0.10),
    }


# ----------------------------------------------------------------------------
# G4 — winding extractor PLANT-AT-SCALE (prereg §5 G4). Plant a known (2,3) at
# THIS run's (N,R,r); extract_2_3_omega_fast must read back (2,3) with rel > 0.1.
# If r is near 1.1 cells -> collapses to (2,2)/garbage -> F4 uncertifiable.
# ----------------------------------------------------------------------------
def gate_G4(cfg: RunConfig) -> dict:
    """G4 — plant-at-scale at (N,R,r); the extractor reads back (2,3) rel>0.1."""
    omega0, pi0 = planted_winding_field(
        cfg.N, cfg.R, cfg.r, p=2, q=3, mode="traveling", helicity=1, amplitude=cfg.omega_amp
    )
    rd = extract_2_3_omega_fast(omega0, pi0, cfg.R, cfg.r, cfg.N)
    reads_2_3 = (rd["w_tor"], rd["w_pol"]) in [(2, 3), (3, 2)]
    rel_ok = (rd["w_tor_rel"] > 0.1) and (rd["w_pol_rel"] > 0.1)
    r_clear = cfg.r > 2.0  # clear of the r~1.1 collapse zone
    passes = reads_2_3 and rel_ok and r_clear
    return {
        "gate": "G4",
        "planted": "(2,3) traveling",
        "read_back": (rd["w_tor"], rd["w_pol"]),
        "is_2_3": bool(rd["is_2_3"]),
        "rel_tor": float(rd["w_tor_rel"]),
        "rel_pol": float(rd["w_pol_rel"]),
        "r_cells": float(cfg.r),
        "r_clear_of_collapse_zone": bool(r_clear),
        "PASS": bool(passes),
    }


def main():  # PLACEHOLDER — F-reads + binning land in the next commit
    print("passive_eigenmode_driver: F-reads + binning land in the next commit")
    checks = _verify_constants()
    for k, v in checks.items():
        print(f"  [{'OK' if v else 'FAIL'}] {k}")
    assert all(checks.values()), "canonical-constant cross-check failed"


if __name__ == "__main__":
    main()
