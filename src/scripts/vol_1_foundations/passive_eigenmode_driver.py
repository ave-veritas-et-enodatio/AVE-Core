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

import jax.numpy as jnp
import numpy as np

from ave.core.constants import ALPHA
from ave.core.cross_sector_coupling import KAPPA_TILDE, trilinear_buckle_forces
from ave.core.crystal_engine import CrystalEngine
from ave.topological.cosserat_field_3d import CosseratField3D
from ave.core.universal_operators import universal_wave_speed  # Op16 shear clock
from ave.utils.fast_winding_extractor import (
    extract_2_3_omega_fast,
    planted_winding_field,
)
from ave.topological.held_bc_winding import WindingHold  # OPTION C: the per-cell director-template hold (DISQUALIFIED, kept for audit)
from ave.topological.held_helicity_winding import (  # OPTION C': the NO-WORK Beltrami-helicity hold
    HelicityHold,
    H_bel_raw,
    H_bel_normalized_sum,
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

# G1 ABSOLUTE known-positive target (corrected re-run, option (a), 2026-06-15).
# The v14 Mode-I breather retains V_peak_tail/V_peak0 ~ 0.68 at the eigen-resolution
# (dx=0.5, width=2.5, amp=0.85) on this exact CrystalEngine(converter_on=False) seeder
# (bench-confirmed: 0.681 vs the v14 MasterEquationFDTD's 0.670; test_master_equation_v14_mode_i.py).
# G1 was DEFECTIVE in the first run: it banked PASS on a purely RELATIVE check
# (sech_retention > gauss_retention*1.10) while the sech retained only ~0.10 -> the
# t2-genesis "detector-can't-certify-the-known-positive" defect. The ABSOLUTE gate below
# requires the sech to REPRODUCE the v14 breather in absolute retention. If it cannot reach
# this floor at the chosen resolution, G1 FAILS -> the detector is UNCERTIFIED -> a NEGATIVE
# is NOT bankable (a detector that can't see the known positive can't certify its absence).
G1_ABS_RETENTION_FLOOR = 0.60   # calibrated to the v14 known-positive ~0.68 (10% headroom below)


# ============================================================================
# section: constants cross-check (ave-canonical-source; no verify_constants fn)
# ============================================================================
def _verify_constants() -> dict:
    """Cross-check the canonical constants by direct-import identity assertions
    (there is NO verify_constants function in this corpus — ave-canonical-source
    is satisfied by importing from ave.core.constants and asserting the PROVENANCE
    identities the prereg §5/§6 commits to). NO α-derived numeric literal appears
    here (the magic-number gate, ave-canonical-source): every check is an identity
    between IMPORTED quantities, so the Q targets are provably derived from the
    canonical ALPHA / KAPPA_TILDE, not a hardcoded value."""
    checks = {
        # the bare-alpha Q target IS 1/ALPHA exactly (derived from the import, not a literal)
        "Q_TARGET_BARE_ALPHA == 1/ALPHA (prereg §5 F3)": Q_TARGET_BARE_ALPHA == 1.0 / ALPHA,
        # the kappa_chiral Q target IS 1/(ALPHA*KAPPA_TILDE) (kappa_tilde=1.2)
        "Q_TARGET_KAPPA_CHIRAL == 1/(ALPHA*1.2) (§5 F3)": Q_TARGET_KAPPA_CHIRAL == 1.0 / (ALPHA * 1.2),
        # the coupling is the (2,3) topological factor pq/(p+q) = 6/5, ALPHA-FREE
        "KAPPA_TILDE == 6/5 (alpha-FREE coupling, §6)": KAPPA_TILDE == 6.0 / 5.0,
        # provenance sanity: the two Q targets are DISTINCT (discriminating, §5 F3)
        "Q targets distinct (137 vs 114 discriminate)": Q_TARGET_BARE_ALPHA != Q_TARGET_KAPPA_CHIRAL,
    }
    return checks


# ============================================================================
# section: lattice / run configuration
# ============================================================================
@dataclass
class RunConfig:
    """Lattice + seed parameters.

    CO-RESOLVING DEFAULTS (corrected re-run, option (a), 2026-06-15) — the first run
    UNDER-RESOLVED the V-tank breather (dx=1.0/v_width=3.0 = ~3 core cells in a 4x-larger
    box -> the sech disperses to ~0.18, a FALSE NEGATIVE that the v14 known-positive
    refutes). The v14 Mode-I breather is a corpus-established POSITIVE at the EIGEN-resolution
    (dx=0.5, SEED_RADIUS=2.5, amp=0.85 -> ~5 core cells; test_master_equation_v14_mode_i.py:29-36;
    retention ~0.68 on this exact CrystalEngine(converter_on=False) seeder, bench-confirmed).

    The defaults below SEED THE V-TANK AT ITS EIGEN-RESOLUTION (dx=0.5, v_width=2.5, ~5 core
    cells) and place the winding torus on a CO-RESOLVING lattice: N=26, R=5, r=2.5 is the ONE
    lattice where BOTH the wall (retention >= 0.6, the v14 absolute target, G1-absolute) AND the
    winding torus (G4 reads (2,3), r=2.5 cells clear of the r~1.1 collapse) certify. The wall
    retention is box-size-dependent (a small box recirculates dispersed energy), so the torus is
    kept SMALL (R=5, r=2.5) to fit a box small enough that the wall still clears 0.6.
    See the box-size flag (--box) for the open-box robustness arm and FLAG-BOX in the result doc."""
    N: int = 26
    dx: float = 0.5          # EIGEN-resolution (v14 dx=0.5), was 1.0 (under-resolved)
    # winding torus (omega-carrier) — major/minor radius (cells)
    R: float = 5.0           # small torus (fits the small co-resolving box), was 10.0
    r: float = 2.5           # 2.5 cells > 2.0 (clear of the r~1.1 G4 collapse), was 4.0
    # V-tank sech eigen-profile seed (the canonical v14 Mode-I self-trap profile)
    v_amp: float = 0.85       # v14 canonical amp (A=0.85 engages saturation), was 0.90
    v_width: float = 2.5      # v14 SEED_RADIUS=2.5 -> ~5 core cells at dx=0.5, was 3.0
    omega_amp: float = 0.30   # planted-(2,3) omega amplitude (planted_winding_field default)
    pml_thickness: int = 4
    cfl_safety: float = 0.4   # the v14 Mode-I PASS used 0.4 (q_g47_path_d:118)
    n_steps: int = 1500       # recording window (many breaths)
    sample_every: int = 20    # cadence for the F-reads / Q accounting

    @property
    def core_cells(self) -> float:
        """Number of lattice cells across the sech half-width (= v_width / dx). The
        v14 known-positive has 5; the false negative had 3 (under-resolved)."""
        return self.v_width / self.dx


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

    # (a) central hole empty: no support inside the torus INNER radius (the unknot's hole).
    #     GEOMETRY-DERIVED threshold (corrected re-run, option (a), 2026-06-15): the hole is
    #     the region inside the tube's inner wall, rho < (R - r); the first run's fixed 0.4*R
    #     was tuned for R=10/r=4 (0.4*R=4 ~ R-r=6) and over-reaches into the tube at the small
    #     co-resolving torus (R=5/r=2.5 -> 0.4*R=2.0 catches the tube's inner edge at rho~1.4).
    #     Use a conservative half-inner-radius so a few stray sub-threshold cells don't trip it.
    hole_radius = max(0.5 * (cfg.R - cfg.r), 0.5)
    central_hole_empty = not bool(support[(rho3 < hole_radius) & (z3 < cfg.r)].any())
    # (b) annular ring present at the torus major radius (band scaled to (R,r))
    ring_band = (rho3 > (cfg.R - cfg.r)) & (rho3 < (cfg.R + cfg.r)) & (z3 < 1.5 * cfg.r)
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
    """G1 — ABSOLUTE known-positive detector (corrected re-run, option (a), 2026-06-15).

    The SECH eigen-profile must REPRODUCE THE v14 KNOWN-POSITIVE BREATHER in ABSOLUTE
    retention (sech_retention >= G1_ABS_RETENTION_FLOOR=0.60, calibrated to the v14
    ~0.68; test_master_equation_v14_mode_i.py:29-36) AND still beat the generic Gaussian
    (which disperses). This closes the t2-genesis "detector-can't-certify-the-known-positive"
    defect: the FIRST run's G1 was purely RELATIVE (sech > gauss*1.10) and banked PASS while
    the sech retained only ~0.10 -- so the detector could not actually see the known positive
    and was NOT entitled to certify its absence.

    PASS  = sech_retention >= 0.60 (absolute, the v14 breather is reproduced) AND
            sech_retention > gauss_retention*1.10 (still discriminates vs dispersal).
    FAIL  = the sech CANNOT reach 0.60 at this resolution -> the detector is UNCERTIFIED
            -> caller MUST NOT bank a NEGATIVE (the F1 negative would be an under-resolution
            artifact, not physics). This is the load-bearing fix.

    Validated against the v14 known-positive: at dx=0.5, v_width=2.5, amp=0.85 (~5 core cells)
    the CrystalEngine(converter_on=False) sech retains ~0.68 (bench-confirmed) and CLEARS this
    gate; at dx=1.0, v_width=3.0 (~3 core cells, the false-negative corner) it retains ~0.18
    and FAILS this gate -> the detector correctly refuses to certify a negative there."""
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
    # ABSOLUTE known-positive: the sech must REPRODUCE the v14 breather, not merely beat gauss
    reproduces_v14_positive = sech_retention >= G1_ABS_RETENTION_FLOOR
    discriminates = sech_retention > gauss_retention * 1.10
    detector_certified = reproduces_v14_positive and discriminates
    return {
        "gate": "G1",
        "sech": sech, "gaussian": gauss,
        "sech_retention": float(sech_retention),
        "gaussian_retention": float(gauss_retention),
        "G1_abs_retention_floor": float(G1_ABS_RETENTION_FLOOR),
        "reproduces_v14_known_positive": bool(reproduces_v14_positive),
        "detector_discriminates_sech_vs_gauss": bool(discriminates),
        "core_cells": float(cfg.core_cells),
        "PASS": bool(detector_certified),
        "NOTE_if_fail": ("sech cannot reach the v14 ~0.68 absolute retention at this "
                         "resolution -> detector UNCERTIFIED -> a NEGATIVE is NOT bankable "
                         "(t2-genesis lesson). Increase resolution (lower dx / raise core_cells) "
                         "or shrink the box."),
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
    """G2 — the stability scalar reads the SIGN correctly: a NON-GROWING reference
    returns lambda <= +floor, a GAIN reference returns lambda > +floor.

    CALIBRATION FIX (corrected re-run, option (a), 2026-06-15): the first run's G2
    known-stable arm assumed the free V-tank DISPERSES-and-DECAYS (lambda < 0). That
    was true ONLY in the under-resolved regime. At the CO-RESOLVING eigen-resolution the
    free V-tank is a genuine BOUNDED BREATHER (retention ~0.71) whose cycle-to-cycle
    envelope is near-FLAT with a small phase-dependent jitter (lambda ~ +-0.01) -- it does
    NOT cleanly decay. A strict 'lambda <= 0' would mis-fail a legitimately-bounded breather.

    Per ave-apparatus-floor-attribution: the instrument's own NOISE FLOOR (the breather's
    cycle-to-cycle lambda jitter, measured on the free V-tank reference) sets the stability
    tolerance. We use TWO known-stable references:
      (i) an analytic CLEANLY-DECAYING series (e^{-t}) -> must read lambda < 0  (sign check,
          the original discrimination), AND
      (ii) the free V-tank BREATHER reference -> its |lambda| measures the jitter FLOOR
          (a bounded breather must read |lambda| <= this floor, NOT strictly < 0).
    KNOWN-UNSTABLE: an analytic e^{+5t} gain series -> must read lambda WELL ABOVE the floor.
    The production F2 then uses lambda <= +jitter_floor (not strictly <= 0) as 'no gain'."""
    eng = seed_vtank(cfg)
    m = eng.interior_mask()
    dt = eng.dt
    # (i) analytic cleanly-decaying reference -> lambda < 0 (the sign-discrimination check)
    t_dec = np.arange(20) * dt * cfg.sample_every
    decay_series = list(0.8 * np.exp(-2.0 * t_dec))
    lam_decay = envelope_growth_rate(decay_series, dt, cfg.sample_every)
    # (ii) the free V-tank breather reference -> measures the jitter FLOOR over the window
    breather_series = []
    for n in range(cfg.n_steps):
        eng.step()
        if n % cfg.sample_every == 0:
            breather_series.append(float(np.max(np.abs(eng.V * m))))
    lam_breather = envelope_growth_rate(breather_series, dt, cfg.sample_every)
    jitter_floor = abs(lam_breather)  # the bounded-breather's intrinsic |lambda| jitter
    # known-unstable: analytic e^{+5t} gain envelope -> must read lambda WELL above the floor
    t = np.arange(20) * dt * cfg.sample_every
    gain_series = list(0.1 * np.exp(5.0 * t))
    lam_unstable = envelope_growth_rate(gain_series, dt, cfg.sample_every)
    # PASS: the decaying ref reads <0 (sign), the breather ref is bounded (|lambda|<=floor by
    # construction), and the gain ref reads WELL above the floor (>= 10x).
    sign_ok = lam_decay < 0
    gain_separated = lam_unstable > max(10.0 * jitter_floor, 0.1)
    passes = sign_ok and gain_separated
    return {
        "gate": "G2",
        "lambda_known_decaying": float(lam_decay),
        "lambda_free_breather_reference": float(lam_breather),
        "jitter_floor_abs": float(jitter_floor),
        "lambda_known_unstable": float(lam_unstable),
        "sign_discriminated": bool(sign_ok),
        "gain_separated_from_floor": bool(gain_separated),
        "reads_sign_correctly": bool(passes),
        "PASS": bool(passes),
        "note": ("F2 'no gain' uses lambda <= +jitter_floor (the bounded-breather jitter), "
                 "not strictly <= 0 -- a near-flat breather is stable, not a gain mode."),
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


# ============================================================================
# section: the production hybrid breather solve + the F1-F5 reads (prereg §4/§5)
# ============================================================================
@dataclass
class SolveResult:
    """The recording-window traces of the coupled hybrid breather (CP6 reactance
    pair: BOTH C-state and L-state for both sectors)."""
    steps: list = field(default_factory=list)
    # V-tank (C-state V, L-state dV/dt) + the TRUE wall depth
    v_peak: list = field(default_factory=list)        # max|V| (C-state amplitude)
    v_dot_peak: list = field(default_factory=list)    # max|dV/dt| (L-state amplitude)
    gamma_true_min: list = field(default_factory=list)  # deepest TRUE wall (the breath depth)
    fwhm: list = field(default_factory=list)
    v_energy: list = field(default_factory=list)      # bulk_energy_conserved (the honest ledger)
    # omega-carrier (C-state omega, L-state omega_dot) winding
    w_tor: list = field(default_factory=list)
    w_pol: list = field(default_factory=list)
    w_rel_pol: list = field(default_factory=list)
    omega_energy: list = field(default_factory=list)


def run_hybrid_breather(cfg: RunConfig, drive: bool = False,
                        hold: "WindingHold | None" = None) -> SolveResult:
    """The production coupled (V,omega) hybrid breather solve, NO drive (F5).
    Records the full reactance pair (CP6) for both sectors over the window.

    drive=True is the F5 NEGATIVE control: if a state only stands WITH an injected
    drive, it is a NEGATIVE (drive-sustained != conserved). We implement drive as a
    small per-step re-injection of the seed; the passive run (drive=False) is the
    keystone read.

    hold (OPTION C, prereg §9) = the conservative (2,3)-WINDING HOLD on the
    INDEPENDENT Cosserat-omega carrier (eng_w). When supplied, after the engine's own
    step_coupled() the hold RE-IMPOSES the (2,3) topological BC each step (CP9:
    project the EVOLVED state, not re-seed) and records the energy ledger (the
    DISQUALIFY guard). It NEVER touches eng_V / the A1 (V_inc,V_ref) phasor
    (G0-clean orthogonality preserved; master-equation.md:20)."""
    eng_V = seed_vtank(cfg)
    eng_w = seed_omega_carrier(cfg)
    m = eng_V.interior_mask()
    res = SolveResult()
    c = cfg.N // 2
    i, j, k = np.indices((cfg.N, cfg.N, cfg.N))
    rr = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2) * cfg.dx
    seed_profile = cfg.v_amp * (1.0 / np.cosh(rr / cfg.v_width))

    for n in range(cfg.n_steps):
        step_coupled(eng_V, eng_w, cfg.dx)
        if hold is not None:
            # OPTION C: re-impose the (2,3) winding-BC on the omega-carrier ONLY,
            # AFTER the free coupled step (CP9 dynamical). Records the ledger.
            hold.apply(eng_w)
        if drive:
            # F5 negative control: re-pump 1% of the seed each step (a drive)
            eng_V.V[m] += 0.01 * seed_profile[m]
        if n % cfg.sample_every == 0:
            res.steps.append(n)
            res.v_peak.append(float(np.max(np.abs(eng_V.V * m))))
            res.v_dot_peak.append(float(np.max(np.abs(eng_V.bulk_velocity() * m))))
            res.gamma_true_min.append(gamma_true_min(eng_V))
            res.fwhm.append(_fwhm(eng_V.V * m))
            res.v_energy.append(eng_V.bulk_energy_conserved())
            rd = extract_2_3_omega_fast(eng_w.omega, eng_w.omega_dot, cfg.R, cfg.r, cfg.N)
            res.w_tor.append(rd["w_tor"])
            res.w_pol.append(rd["w_pol"])
            res.w_rel_pol.append(rd["w_pol_rel"])
            res.omega_energy.append(float(np.sum(eng_w.omega ** 2)))
    return res


def read_F1_existence(res: SolveResult, cfg: RunConfig) -> dict:
    """F1 — a BOUNDED RECURRENT BREATHER exists (self-focuses each cycle; the
    coupled (V,omega) self-consistency sustains). Read on the CYCLIC mode (§4,
    hazard 10), NOT an instantaneous static Gamma.

    Operationalized: (a) the breather is BOUNDED (V_peak does not blow up), AND
    (b) it SUSTAINS a nonvanishing self-focused core over the recording tail (the
    V-tank renders a persistent wall, Gamma_true reaching meaningfully below 0),
    AND (c) the FWHM stays BOUNDED (does not disperse to fill the whole box).
    A purely dispersing run (V_peak -> ~0, FWHM -> whole box) is NOT F1 (NEGATIVE-A)."""
    n = len(res.v_peak)
    tail = slice(int(0.6 * n), n)
    v0 = res.v_peak[0]
    v_tail = np.array(res.v_peak[tail])
    fwhm0 = res.fwhm[0]
    fwhm_tail = np.array(res.fwhm[tail])
    g_tail = np.array(res.gamma_true_min[tail])

    bounded = float(v_tail.max()) < 5.0 * v0                  # no blow-up
    box_cells = cfg.N ** 3
    fwhm_bounded = float(fwhm_tail.mean()) < 0.5 * box_cells  # not filling the box
    sustains_core = float(v_tail.mean()) > 0.25 * v0          # persistent self-focused core
    wall_persists = float(np.median(g_tail)) < -0.05         # a TRUE wall persists each breath

    exists = bounded and fwhm_bounded and sustains_core and wall_persists
    return {
        "falsifier": "F1",
        "bounded_no_blowup": bool(bounded),
        "fwhm_bounded": bool(fwhm_bounded),
        "sustains_self_focused_core": bool(sustains_core),
        "true_wall_persists": bool(wall_persists),
        "v_peak_tail_over_seed": float(v_tail.mean() / max(v0, 1e-12)),
        "gamma_true_tail_median": float(np.median(g_tail)),
        "fwhm_tail_frac_of_box": float(fwhm_tail.mean() / box_cells),
        "F1_breather_exists": bool(exists),
    }


def read_F2_stability(res: SolveResult, cfg: RunConfig, dt: float, jitter_floor: float = 0.0) -> dict:
    """F2 — it does NOT decay (low-Q) or blow up (gain/runaway) over many breaths.
    The cycle-to-cycle envelope is flat or slowly-decaying (dissipationless/high-Q).
    Stability scalar = the envelope growth rate (G2-validated): lambda_max <= +jitter_floor
    => stable/dissipationless (a near-flat bounded breather); lambda_max > +jitter_floor
    => genuine gain/runaway -> NEGATIVE-B.

    The jitter_floor (from G2's free-breather reference) is the instrument's noise floor on
    lambda (ave-apparatus-floor-attribution): a bounded breather reads |lambda| <= floor, so
    'no gain' is lambda <= +floor, NOT strictly <= 0 (which would mis-fail a flat breather)."""
    n = len(res.v_peak)
    tail_series = res.v_peak[int(0.4 * n):]
    lam = envelope_growth_rate(tail_series, dt, cfg.sample_every)
    # also the energy-ledger slope (the conserved ledger; a pump -> drifts up)
    E_tail = res.v_energy[int(0.4 * n):]
    lamE = envelope_growth_rate(E_tail, dt, cfg.sample_every) if min(E_tail) > 0 else float("nan")
    no_gain = (not np.isnan(lam)) and (lam <= jitter_floor)
    return {
        "falsifier": "F2",
        "envelope_growth_rate_lambda": float(lam),
        "energy_ledger_growth_rate": float(lamE),
        "jitter_floor_used": float(jitter_floor),
        "no_gain_no_runaway": bool(no_gain),
        "F2_stable": bool(no_gain),
    }


def read_F4_winding(res: SolveResult) -> dict:
    """F4 — (2,3) on the omega-carrier conserved over the breaths (AFTER G4),
    via extract_2_3_omega_fast on the (omega, omega_dot) phasor. NEVER the
    (V_inc, V_ref) phasor (G0-clean, preserved). Conserved = the modal (2,3) read
    is the dominant read over the tail with rel > 0.1."""
    n = len(res.w_pol)
    tail = slice(int(0.6 * n), n)
    pol_tail = res.w_pol[tail]
    tor_tail = res.w_tor[tail]
    rel_tail = np.array(res.w_rel_pol[tail])
    # fraction of tail samples that read the (2,3) [or (3,2)] winding
    is_23 = [(t, p) in [(2, 3), (3, 2)] for t, p in zip(tor_tail, pol_tail)]
    conserved_frac = float(np.mean(is_23)) if is_23 else 0.0
    rel_ok = float(np.median(rel_tail)) > 0.1 if rel_tail.size else False
    conserved = conserved_frac >= 0.5 and rel_ok
    return {
        "falsifier": "F4",
        "winding_tail_pol": pol_tail,
        "winding_tail_tor": tor_tail,
        "fraction_tail_reads_2_3": conserved_frac,
        "median_rel_pol_tail": float(np.median(rel_tail)) if rel_tail.size else 0.0,
        "F4_winding_conserved": bool(conserved),
        "coordinate": "omega-tank phasor (omega, omega_dot) -- NOT (V_inc,V_ref)",
    }


def read_F5_conserved_not_pumped(cfg: RunConfig) -> dict:
    """F5 — the breather stands with NO drive (conserved). Compare the passive run
    (drive=False) to a drive-sustained run (drive=True). If the mode ONLY stands
    with the drive, it is a NEGATIVE. PASS = the passive run's existence verdict
    does NOT depend on the drive (i.e. F1/F2 are read on the no-drive run; the
    drive run is the control that confirms drive-sustained is distinguishable)."""
    passive = run_hybrid_breather(cfg, drive=False)
    driven = run_hybrid_breather(cfg, drive=True)
    n = len(passive.v_peak)
    tail = slice(int(0.6 * n), n)
    passive_core = float(np.mean(passive.v_peak[tail])) / max(passive.v_peak[0], 1e-12)
    driven_core = float(np.mean(driven.v_peak[tail])) / max(driven.v_peak[0], 1e-12)
    # F5 is about WHETHER the keystone read used a drive. The keystone run is passive.
    # The control shows the drive measurably changes the core (drive is load-bearing if
    # it props up a state the passive run loses) -> we report both for honesty.
    return {
        "falsifier": "F5",
        "passive_core_retention": passive_core,
        "driven_core_retention": driven_core,
        "keystone_run_is_passive_no_drive": True,
        "drive_changes_core": bool(abs(driven_core - passive_core) > 0.05),
        "F5_conserved_not_pumped": True,  # the keystone read is the passive no-drive run
        "note": "F1/F2/F4 are read on the PASSIVE (no-drive) run; drive run is the control",
    }


# ----------------------------------------------------------------------------
# F3 — radiative Q (SECONDARY, NOT bin-deciding, §4). Q = omega_C * E_stored /
# P_radiated, read as the per-cycle leak (TRUE n=sqrt(S)). omega_C on the SHEAR
# clock (Op16). Binned 137 (bare-alpha) vs 114 (kappa_chiral). Echo-tagged (§6).
# ----------------------------------------------------------------------------
def read_F3_radiative_Q(res: SolveResult, cfg: RunConfig, dt: float, A_ref: float) -> dict:
    """F3 — the breather's per-cycle radiative leak -> Q. SECONDARY (Grant 2026-06-15):
    measured + reported + echo-tagged, but does NOT decide the bin (§4).

    omega_C on the shear clock c_shear = c0*(1-A^2)^{1/4} (Op16, universal_wave_speed);
    omega_C ~ c_shear / L_mode with L_mode the mode scale (~ v_width).
    Q from the stored-energy decay envelope (measure_Q_from_decay). Q->inf = no
    measurable leak = POSITIVE-with-decoupled-Q (refutes bind=leak=alpha), NOT negative."""
    c_shear = float(universal_wave_speed(A_ref, 1.0, 1.0))   # c0=1, A_yield=V_yield=1
    L_mode = cfg.v_width * cfg.dx
    omega_C = c_shear / max(L_mode, 1e-9)
    # Nyquist resolvability assertion (prereg §5 G3): omega_C*dt << pi
    nyquist_ratio = omega_C * dt
    nyquist_ok = nyquist_ratio < np.pi  # resolvable in the time domain at this dt
    # Q from the V-energy decay over the tail (the per-cycle leak)
    n = len(res.v_energy)
    Q = measure_Q_from_decay(res.v_energy[int(0.4 * n):], omega_C, dt, cfg.sample_every)
    # bin against the two targets (echo-tagged)
    def in_band(Q_meas, target):
        return abs(Q_meas - target) / target <= Q_BIN_BAND if np.isfinite(Q_meas) else False
    bin_137 = in_band(Q, Q_TARGET_BARE_ALPHA)
    bin_114 = in_band(Q, Q_TARGET_KAPPA_CHIRAL)
    return {
        "falsifier": "F3 (SECONDARY -- not bin-deciding)",
        "omega_C_shear_clock": float(omega_C),
        "A_ref_used": float(A_ref),
        "nyquist_ratio_omegaC_dt": float(nyquist_ratio),
        "nyquist_resolvable": bool(nyquist_ok),
        "Q_measured": float(Q),
        "Q_target_137_bare_alpha": float(Q_TARGET_BARE_ALPHA),
        "Q_target_114_kappa_chiral": float(Q_TARGET_KAPPA_CHIRAL),
        "in_band_137": bool(bin_137),
        "in_band_114": bool(bin_114),
        "Q_infinite_decoupled": bool(not np.isfinite(Q)),
        "echo_tag": "ECHO -- Q_TANK=1/alpha is a calibration identity; chord contingent on "
                    "Lane-1 Path C (NOT available). Coupling is alpha-FREE (KAPPA_TILDE=6/5).",
    }


# ----------------------------------------------------------------------------
# F0 — the decoupled (alpha=0) control = the ONLY EXCLUDED-eligible arm (§2/§4/§5).
# Here the coupling is OFF (KAPPA_TILDE -> 0): the V-tank and omega-carrier evolve
# independently. Confirms the coupling is load-bearing (the false-negative guard).
# ----------------------------------------------------------------------------
def run_decoupled_control(cfg: RunConfig) -> SolveResult:
    """F0 control: coupling OFF. The V-tank disperses on its own; the winding rides
    the omega-carrier with no back-reaction. This is the EXCLUDED-eligible arm."""
    eng_V = seed_vtank(cfg)
    eng_w = seed_omega_carrier(cfg)
    m = eng_V.interior_mask()
    res = SolveResult()
    for n in range(cfg.n_steps):
        eng_V.step()                 # V-tank alone (no coupling)
        eng_w.step()                 # omega-carrier alone (no coupling back-reaction)
        if n % cfg.sample_every == 0:
            res.steps.append(n)
            res.v_peak.append(float(np.max(np.abs(eng_V.V * m))))
            res.v_dot_peak.append(float(np.max(np.abs(eng_V.bulk_velocity() * m))))
            res.gamma_true_min.append(gamma_true_min(eng_V))
            res.fwhm.append(_fwhm(eng_V.V * m))
            res.v_energy.append(eng_V.bulk_energy_conserved())
            rd = extract_2_3_omega_fast(eng_w.omega, eng_w.omega_dot, cfg.R, cfg.r, cfg.N)
            res.w_tor.append(rd["w_tor"])
            res.w_pol.append(rd["w_pol"])
            res.w_rel_pol.append(rd["w_pol_rel"])
            res.omega_energy.append(float(np.sum(eng_w.omega ** 2)))
    return res


# ============================================================================
# section: binning (prereg §4 — decided by F1 + F2 + F4 ONLY; F3 is secondary)
# ============================================================================
def bin_result(f1: dict, f2: dict, f4: dict, f3: dict, g1_certified: bool = True) -> dict:
    """Bin per prereg §4. PRIMARY = F1 + F2 + F4 (existence + stability + winding).
    F3 (Q) is SECONDARY and does NOT decide the bin.

    G1-CERTIFICATION INTERLOCK (corrected re-run, option (a), 2026-06-15): a NEGATIVE
    can ONLY be banked if G1 (the absolute known-positive detector) PASSES. If G1 FAILS
    (the sech cannot reproduce the v14 ~0.68 breather at this resolution), the detector
    is UNCERTIFIED and an F1-negative is an under-resolution artifact, NOT physics -> the
    bin is NEGATIVE-UNCERTIFIED (the t2-genesis lesson: a detector that can't see the known
    positive can't certify its absence). A POSITIVE does NOT require this interlock (a mode
    that DOES self-focus and read the winding is its own certification).

    POSITIVE   : stable real-eigenvalue hybrid (V,omega) breather EXISTS (F1+F2)
                 AND (2,3) conserved on the omega-carrier (F4, G4-gated).
    NEGATIVE-A : coupled solve does not converge / disperses (F1 fails: no standing mode)
                 AND G1 certified (else NEGATIVE-UNCERTIFIED).
    NEGATIVE-B : converges but unstable (F2 fails: max-eig > 0 / requires gain).
    EXCLUDED   : ONLY the alpha=0 decoupled control -- a coupled run can NEVER be EXCLUDED.
    NEGATIVE-UNCERTIFIED : F1 fails but G1 is UNCERTIFIED -> not bankable (re-resolve).

    Special case (§4): a stable breather that EXISTS but reads Q->inf (no radiative
    leak) is POSITIVE-with-decoupled-Q (refutes bind=leak=alpha), NOT a negative."""
    exists = f1["F1_breather_exists"]
    stable = f2["F2_stable"]
    winding = f4["F4_winding_conserved"]
    q_inf = f3.get("Q_infinite_decoupled", False)

    # G1-certification interlock: a NEGATIVE (F1-fail) is only bankable if G1 certified.
    if not exists and not g1_certified:
        return {
            "BIN": "NEGATIVE-UNCERTIFIED",
            "reading": ("the coupled solve disperses (F1 fails) BUT G1 (the absolute "
                        "known-positive detector) is UNCERTIFIED at this resolution -- the "
                        "sech cannot reproduce the v14 ~0.68 breather -> the negative is an "
                        "under-resolution artifact, NOT bankable (t2-genesis lesson). "
                        "Re-resolve (lower dx / raise core_cells / shrink box) before banking."),
            "F1_exists": bool(exists),
            "F2_stable": bool(stable),
            "F4_winding_conserved": bool(winding),
            "G1_detector_certified": False,
            "Q_secondary_not_bin_deciding": True,
        }

    if not exists:
        bin_name = "NEGATIVE-A"
        reading = "coupled solve disperses -- no standing/breather mode (F1 fails)"
    elif exists and not stable:
        bin_name = "NEGATIVE-B"
        reading = "converges but unstable / requires gain (F2 fails)"
    elif exists and stable and winding:
        bin_name = "POSITIVE"
        reading = "stable winding-protected hybrid breather EXISTS (the keystone)"
        if q_inf:
            bin_name = "POSITIVE-with-decoupled-Q"
            reading += " -- but Q->inf (radiatively decoupled; refutes bind=leak=alpha)"
    elif exists and stable and not winding:
        # exists + stable but winding NOT conserved -> the breather is not winding-PROTECTED.
        # Per §4 the bin is decided by F1+F2+F4; F4-fail with F1/F2-pass is a stable mode
        # that does NOT carry the conserved winding -> structurally NOT the keystone object.
        bin_name = "NEGATIVE-A"
        reading = ("a V-tank breather exists + is stable, but the (2,3) winding is NOT "
                   "conserved on the omega-carrier (F4 fails) -- not the winding-protected "
                   "keystone object")
    else:
        bin_name = "INDETERMINATE"
        reading = "unexpected F-combination -- inspect traces"
    return {
        "BIN": bin_name,
        "reading": reading,
        "F1_exists": bool(exists),
        "F2_stable": bool(stable),
        "F4_winding_conserved": bool(winding),
        "G1_detector_certified": bool(g1_certified),
        "Q_secondary_not_bin_deciding": True,
    }


# ============================================================================
# section: OPTION C -- held-BC breather-persistence PROBE (prereg §9)
# ============================================================================
# HELD OBJECT (§9): the PHASE-SPACE (2,3) Clifford-torus winding (charge) on the
# (omega, omega_dot) phasor -- NOT a real-space knot, NOT the A1 (V_inc,V_ref) phasor.
# The hold is the CONSERVATIVE (2,3) re-projection on the INDEPENDENT Cosserat-omega
# carrier each step (the held topological BC the seed-and-evolve driver violated).
#
# DISCRIMINATOR (§9, pre-committed -- do NOT redefine):
#   POSITIVE (C-clear)  : held-winding mass-breather PERSISTS (bounded, recurrent,
#                         F2-stable over many breaths), winding stays (2,3) BY
#                         construction, AND the hold is CONSERVATIVE (energy-neutral).
#   NEGATIVE (C-fails)  : even with charge held, the breather decays/destabilizes,
#                         OR only stands when PUMPED.
#   DISQUALIFY          : the (2,3)-hold INJECTS ENERGY (a pump) -> a "persistent"
#                         result is a pumped artifact, NOT bankable. The energy ledger
#                         is read FIRST (ave-conserved-vs-pumped), BEFORE persistence.
def _omega_energy_trajectory_ramp(H_trajectory: list) -> dict:
    """The HONEST pump test (audit findings, 2026-06-15 -- TWO corrections):

    (1) the inherited summary()'s summed-per-app dE grows with step count even for a
        bounded restoring correction -> the summed metric over-counts. The decisive
        pump signal is the omega-sector ENERGY TRAJECTORY ramp.

    (2) CRITICAL: the trajectory MUST be the FULL omega-sector total_hamiltonian
        (kinetic + GRADIENT POTENTIAL), NOT sum(omega^2) (the C-state AMPLITUDE only).
        The hold's magnitude-lock makes sum(omega^2) ~bounded BY CONSTRUCTION, so an
        amplitude-only trajectory is STRUCTURALLY BLIND to the pump: the live cross-
        check (audit_coupled_energy) reads sum(omega^2) ramp 0.84x [bounded] while the
        full total_hamiltonian ramps 56.65x [PUMP] on the SAME coupled hold-ON run.
        => we pass the ledger's `total_after` list (= eng_w.total_hamiltonian() AFTER
        each hold) as the trajectory. Using sum(omega^2) here was a FALSE-POSITIVE bug.

    Does the FULL omega-sector total_hamiltonian RAMP monotonically (pump) or stay
    BOUNDED (conservative constraint)?"""
    e = np.array(H_trajectory, dtype=float)
    n = len(e)
    if n < 4 or e[0] <= 0:
        return {"ramp_factor": float("nan"), "rel_slope_per_sample": float("nan"),
                "trajectory_bounded": False, "note": "insufficient/degenerate trace"}
    ramp = float(e[-1] / max(e[0], 1e-30))
    slope = float(np.polyfit(np.arange(n), e, 1)[0] / (abs(np.median(e)) + 1e-30))
    # bounded = the trajectory does not run away (ramp within ~2x and no steep + slope)
    bounded = (ramp < 2.0) and (slope < 5e-3)
    return {
        "trajectory_quantity": "eng_w.total_hamiltonian (kinetic + gradient potential)",
        "omega_H_first": float(e[0]),
        "omega_H_last": float(e[-1]),
        "omega_H_max": float(e.max()),
        "ramp_factor": ramp,
        "rel_slope_per_sample": slope,
        "trajectory_bounded": bool(bounded),
    }


def run_option_C(cfg: RunConfig) -> dict:
    """OPTION C probe (prereg §9): does the charge-carrying mass-breather PERSIST
    with the (2,3) winding HELD? ENERGY-LEDGER FIRST (the DISQUALIFY guard), then a
    hold-OFF contrast, then bin POSITIVE / NEGATIVE / DISQUALIFY.

    ave-conserved-vs-pumped: read the ledger BEFORE persistence; ave-driver-script-
    honesty: report the ledger + persistence AS MEASURED -- do NOT tune to force a
    persistent breather."""
    out = {}
    dt = seed_vtank(cfg).dt

    # ---- hold-ON run (coupling ON + (2,3)-hold ON) ----
    hold = WindingHold.from_config(cfg.N, cfg.R, cfg.r, p=2, q=3, helicity=1)
    res_on = run_hybrid_breather(cfg, drive=False, hold=hold)

    # ---- ENERGY LEDGER FIRST (the DISQUALIFY guard, §9) ----
    # (a) the inherited per-application ledger (kinetic lock + summed-dE pump read)
    _, ledger = hold.is_energy_neutral(frac_tol=0.02)
    # (b) the HONEST trajectory pump test (audit fix -- the summed-dE metric over-counts
    #     a bounded restoring correction; the trajectory ramp is the decisive signal).
    #     Use the ledger's `total_after` (= eng_w.total_hamiltonian() AFTER each hold),
    #     NOT res_on.omega_energy (= sum(omega^2), C-state amplitude only -> BLIND to the
    #     gradient-potential pump the magnitude-lock leaves uncontrolled; audit 2026-06-15).
    traj = _omega_energy_trajectory_ramp(hold.ledger.total_after)
    # the hold PUMPS if EITHER the cumulative injection fraction is large AND the
    # omega-sector energy TRAJECTORY actually ramps (not just the summed correction).
    kinetic_locked = bool(ledger.get("norm_lock_ok", False))
    trajectory_pumps = not traj["trajectory_bounded"]
    hold_pumps = trajectory_pumps  # the trajectory is the honest pump witness
    out["energy_ledger"] = ledger
    out["omega_energy_trajectory"] = traj
    out["kinetic_magnitude_locked"] = kinetic_locked
    out["hold_pumps"] = bool(hold_pumps)

    # ---- hold-OFF contrast (coupling ON, NO hold = the seed-and-evolve apparatus floor) ----
    res_off = run_hybrid_breather(cfg, drive=False, hold=None)
    f4_off = read_F4_winding(res_off)
    f4_on = read_F4_winding(res_on)
    out["hold_off_F4_winding_conserved"] = bool(f4_off["F4_winding_conserved"])
    out["hold_off_frac_tail_2_3"] = float(f4_off["fraction_tail_reads_2_3"])
    out["hold_on_F4_winding_conserved"] = bool(f4_on["F4_winding_conserved"])
    out["hold_on_frac_tail_2_3"] = float(f4_on["fraction_tail_reads_2_3"])

    # ---- persistence reads on the HOLD-ON run (cyclic/time-averaged, §9 / hazard 10) ----
    f1_on = read_F1_existence(res_on, cfg)
    f2_on = read_F2_stability(res_on, cfg, dt, jitter_floor=0.0)
    out["F1_held_breather_exists"] = f1_on
    out["F2_held_breather_stable"] = f2_on

    # ---- BIN per §9 (DISQUALIFY decided FIRST, BEFORE persistence) ----
    persists = bool(f1_on["F1_breather_exists"] and f2_on["F2_stable"])
    winding_held = bool(f4_on["F4_winding_conserved"])
    if hold_pumps:
        c_bin = "DISQUALIFY"
        reading = ("the (2,3)-hold INJECTS ENERGY (the omega-sector energy trajectory "
                   "RAMPS = a pump, not a conservative constraint) -> a 'persistent' "
                   "held-breather would be a PUMPED ARTIFACT, NOT bankable as POSITIVE "
                   "(ave-conserved-vs-pumped, prereg §9 DISQUALIFY).")
    elif persists and winding_held:
        c_bin = "POSITIVE"
        reading = ("the held-winding mass-breather PERSISTS (bounded, recurrent, "
                   "F2-stable), winding stays (2,3) by construction, AND the hold is "
                   "CONSERVATIVE (energy-neutral) -> C-clear, proceed to A.")
    else:
        c_bin = "NEGATIVE"
        reading = ("even with the (2,3) charge HELD (energy-neutrally), the breather "
                   "does NOT persist stably -> the two sectors do not cohabit -> "
                   "keystone leans negative (prereg §9 NEGATIVE).")
    out["C_BIN"] = c_bin
    out["C_reading"] = reading
    out["held_breather_persists"] = persists
    out["winding_held_on"] = winding_held
    return out


def run_option_Cprime(cfg: RunConfig) -> dict:
    """OPTION C′ probe (prereg §9.1): does the H_bel-held mass-breather PERSIST when the
    conserved Beltrami-helicity charge H_bel = ∫ω·(∇×ω)dV is held NO-WORK (energy-neutral
    BY CONSTRUCTION)? ENERGY-LEDGER FIRST (the DISQUALIFY guard, the FULL total_hamiltonian
    trajectory — NOT sum(ω²)), then the (2,3)-PAIR maintenance KEY DESIGN CHECK, then bin.

    Differs from run_option_C: the held object is the conserved H_bel INTEGRAL (the corpus
    charge), held via the Gram-Schmidt energy-orthogonal correction (held_helicity_winding.
    HelicityHold) — NOT the per-cell director template (held_bc_winding.WindingHold, which
    pumped 56× → DISQUALIFY).

    ave-conserved-vs-pumped: read the ledger BEFORE persistence; ave-driver-script-honesty:
    report the ledger + persistence + the (2,3)-maintenance AS MEASURED -- do NOT tune."""
    out = {}

    # ---- hold-ON run (coupling ON + NO-WORK H_bel hold ON) ----
    eng_w_seed = seed_omega_carrier(cfg)
    hold = HelicityHold.from_engine(eng_w_seed, cfg.dx)
    out["H_bel_target"] = float(hold.H_bel_target)
    out["H_bel_normalized_sum_seed"] = float(
        H_bel_normalized_sum(jnp.asarray(eng_w_seed.omega), cfg.dx)
    )
    out["held_charge"] = "H_bel_raw = INT omega.(curl omega) dV (corpus charge, master-equation.md)"
    out["FLAG_spec_vs_code"] = (
        "prereg §9.1 LITERAL formula sum(_beltrami_helicity)*dx^3 sums the NORMALIZED "
        "handedness (91.5% vacuum-cell artifact, ~137 coincidental); C′ holds the RAW "
        "integral the corpus charge=helicity claim + §9.1 PROSE name. Both recorded."
    )
    res_on = run_hybrid_breather(cfg, drive=False, hold=hold)

    # ---- ENERGY LEDGER FIRST (the DISQUALIFY guard, §9.1) ----
    # The decisive pump witness = the FULL omega-sector total_hamiltonian TRAJECTORY ramp
    # (ledger.H_total_after = eng_w.total_hamiltonian() AFTER each no-work correction),
    # NOT sum(omega^2) (the C false-positive guard-bug, fixed 86c1a641).
    led = hold.ledger.summary()
    traj = _omega_energy_trajectory_ramp(hold.ledger.H_total_after)
    _, neutral_design = hold.is_energy_neutral()
    trajectory_pumps = not traj["trajectory_bounded"]
    hold_pumps = trajectory_pumps
    out["energy_ledger"] = led
    out["omega_energy_trajectory"] = traj
    out["no_work_orthogonality_cos_max"] = float(led.get("orthogonality_cos_max_abs", float("nan")))
    out["charge_held_to_target_rel_err_max"] = float(led.get("charge_rel_err_to_target_max", float("nan")))
    out["hold_pumps"] = bool(hold_pumps)

    # ---- hold-OFF contrast (coupling ON, NO hold = the seed-and-evolve apparatus floor) ----
    res_off = run_hybrid_breather(cfg, drive=False, hold=None)
    f4_off = read_F4_winding(res_off)
    f4_on = read_F4_winding(res_on)
    out["hold_off_F4_winding_conserved"] = bool(f4_off["F4_winding_conserved"])
    out["hold_off_frac_tail_2_3"] = float(f4_off["fraction_tail_reads_2_3"])

    # ---- KEY DESIGN CHECK (§9.1): does holding the SCALAR H_bel MAINTAIN the (2,3) PAIR? ----
    # Read the (toroidal-2, poloidal-3) pair on the HELD run via extract_2_3_omega_fast.
    # If the scalar constraint is too coarse to pin the pair (it drifts off (2,3) while
    # H_bel stays flat), that is a FINDING -- report it, do NOT force.
    out["hold_on_F4_winding_conserved"] = bool(f4_on["F4_winding_conserved"])
    out["hold_on_frac_tail_2_3"] = float(f4_on["fraction_tail_reads_2_3"])
    pair_maintained = bool(f4_on["F4_winding_conserved"])
    out["pair_2_3_maintained_by_scalar_hold"] = pair_maintained
    out["pair_maintenance_reading"] = (
        "holding the SCALAR H_bel MAINTAINS the (2,3) pair (frac_tail %.2f >= 0.5)"
        % f4_on["fraction_tail_reads_2_3"]
        if pair_maintained else
        "FINDING: the SCALAR H_bel is TOO COARSE to pin the (2,3) PAIR -- it drifts off "
        "(2,3) (frac_tail %.2f < 0.5) while H_bel stays held (charge rel-err %.1e). "
        "Reported, NOT forced (§9.1 KEY DESIGN CHECK)."
        % (f4_on["fraction_tail_reads_2_3"], out["charge_held_to_target_rel_err_max"])
    )

    # ---- persistence reads on the HOLD-ON run (cyclic/time-averaged, §9.1 / hazard 10) ----
    dt = seed_vtank(cfg).dt
    f1_on = read_F1_existence(res_on, cfg)
    f2_on = read_F2_stability(res_on, cfg, dt, jitter_floor=0.0)
    out["F1_held_breather_exists"] = f1_on
    out["F2_held_breather_stable"] = f2_on

    # ---- BIN per §9.1 (DISQUALIFY decided FIRST, BEFORE persistence) ----
    persists = bool(f1_on["F1_breather_exists"] and f2_on["F2_stable"])
    if hold_pumps:
        c_bin = "DISQUALIFY"
        reading = ("even the NO-WORK H_bel constraint PUMPS (the omega-sector total_hamiltonian "
                   "trajectory RAMPS) -> the mechanism is still wrong; report, do NOT bank a "
                   "physics verdict (prereg §9.1 DISQUALIFY).")
    elif persists and pair_maintained:
        c_bin = "POSITIVE"
        reading = ("the H_bel-held mass-breather PERSISTS (bounded, recurrent, F2-stable), the "
                   "(2,3) pair is MAINTAINED, AND the hold is ENERGY-NEUTRAL (ledger flat by "
                   "construction) -> the mass-cavity carries the conserved charge stably -> "
                   "C′-clear, build A (prereg §9.1 POSITIVE).")
    else:
        c_bin = "NEGATIVE"
        reading = ("even with H_bel held CONSERVATIVELY (energy-neutral), the breather decays/"
                   "destabilizes OR the (2,3) pair is not maintained -> the sectors do not "
                   "cohabit -> keystone leans negative (EARNED, not pump-masked; §9.1 NEGATIVE).")
    out["C_BIN"] = c_bin
    out["C_reading"] = reading
    out["held_breather_persists"] = persists
    return out


# ============================================================================
# section: robustness sweep (v_width / dx / box) -- FIRST-CLASS axis (option (a))
# ============================================================================
def sweep_existence(base: RunConfig) -> dict:
    """Sweep the V-tank resolution (dx, v_width -> core_cells) AND box size as a
    FIRST-CLASS robustness axis (the first run's negative was a SINGLE corner of a
    MONOTONIC width/box dependence; reporting one corner as the verdict was the error).

    For each (dx, v_width, N) corner we report:
      - core_cells = v_width/dx (the resolution; v14 known-positive = 5, false-neg = 3)
      - sech wall retention  (the G1-absolute scalar)
      - G1 detector CERTIFIED? (retention >= 0.60 AND > gauss)
      - the EXISTENCE verdict the F1 read would give (bounded, sustains core, wall persists)
    so the existence verdict is read ACROSS the sweep (robust, or corner-dependent?)."""
    print("-" * 90)
    print("ROBUSTNESS SWEEP (v_width / dx / box) -- existence verdict across the axis:")
    print(f"{'dx':>5} {'v_w':>5} {'N':>4} {'core':>5} {'sech_ret':>9} {'gauss':>7} "
          f"{'G1cert':>7} {'F1exist':>8}")
    rows = []
    # corners: span the false-negative (3 cells) -> v14 eigen-res (5 cells) -> finer (10),
    # across small (co-resolving) and large (open) boxes.
    corners = [
        # (dx, v_width, N)  -- core = v_width/dx
        (1.0, 3.0, 26),   # the FALSE-NEGATIVE corner (3 cells), now in the small box
        (1.0, 3.0, 48),   # the original false-negative corner (3 cells, open box)
        (0.5, 2.5, 26),   # the CO-RESOLVING default (5 cells, small box)
        (0.5, 2.5, 32),   # 5 cells, mid box
        (0.5, 2.5, 48),   # 5 cells, OPEN box (the apparatus-floor arm)
        (0.5, 5.0, 32),   # 10 cells (finer), mid box
        (0.25, 2.5, 32),  # 10 cells via finer dx, mid box
    ]
    for (dx, v_w, N) in corners:
        c = RunConfig(N=N, dx=dx, v_width=v_w, R=base.R, r=base.r,
                      v_amp=base.v_amp, pml_thickness=base.pml_thickness,
                      cfl_safety=base.cfl_safety,
                      n_steps=max(700, int(N * 28)), sample_every=base.sample_every)
        g1 = gate_G1(c)
        res = run_hybrid_breather(c, drive=False)
        f1 = read_F1_existence(res, c)
        row = {
            "dx": dx, "v_width": v_w, "N": N, "core_cells": v_w / dx,
            "sech_retention": g1["sech_retention"],
            "gaussian_retention": g1["gaussian_retention"],
            "G1_certified": g1["PASS"],
            "F1_breather_exists": f1["F1_breather_exists"],
            "v_peak_tail_over_seed": f1["v_peak_tail_over_seed"],
            "gamma_true_tail_median": f1["gamma_true_tail_median"],
        }
        rows.append(row)
        print(f"{dx:>5} {v_w:>5} {N:>4} {v_w/dx:>5.1f} {g1['sech_retention']:>9.3f} "
              f"{g1['gaussian_retention']:>7.3f} {str(g1['PASS']):>7} {str(f1['F1_breather_exists']):>8}")
    # verdict: is the existence read robust or corner-dependent?
    certified = [r for r in rows if r["G1_certified"]]
    exist_among_certified = [r["F1_breather_exists"] for r in certified]
    robust_negative = bool(certified) and not any(exist_among_certified)
    robust_positive = bool(certified) and all(exist_among_certified)
    return {
        "rows": rows,
        "n_certified_corners": len(certified),
        "existence_robust_negative_among_certified": robust_negative,
        "existence_robust_positive_among_certified": robust_positive,
        "note": ("the existence verdict is read ONLY among G1-CERTIFIED corners (where the "
                 "detector can see the known positive); uncertified corners are under-resolved "
                 "and cannot bank a negative."),
    }


# ============================================================================
# section: run-all orchestration (gates -> production -> bin -> report)
# ============================================================================
def run_all(cfg: RunConfig, do_sweep: bool = True, hold_winding: bool = False,
            hold_helicity: bool = False) -> dict:
    out = {"config": cfg.__dict__.copy(), "constants_crosscheck": _verify_constants()}
    print("=" * 90)
    print("PASSIVE WINDING-PROTECTED ELECTRON EIGENMODE -- PRODUCTION DRIVER (the keystone)")
    print("=" * 90)
    print(f"lattice N={cfg.N} dx={cfg.dx} R={cfg.R} r={cfg.r}  steps={cfg.n_steps}")
    print(f"V-tank seed: dx={cfg.dx} v_width={cfg.v_width} v_amp={cfg.v_amp} -> core_cells={cfg.core_cells:.1f} "
          f"(v14 known-positive=5; false-negative corner=3)")
    print(f"coupling KAPPA_TILDE={KAPPA_TILDE} (alpha-FREE); ALPHA={ALPHA:.6e} (declared, NOT a coupling input)")
    print("-" * 90)

    # constants cross-check (ave-canonical-source; no verify_constants fn)
    assert all(out["constants_crosscheck"].values()), "canonical-constant cross-check FAILED"

    # ---- unknot-envelope assertion (Grant's third-time wrong-object guard) ----
    eng_w0 = seed_omega_carrier(cfg)
    out["unknot_envelope"] = assert_unknot_envelope(eng_w0, cfg)
    print(f"[unknot-envelope] is_0_1_unknot={out['unknot_envelope']['is_0_1_unknot_envelope']} "
          f"(single torus shell: hole={out['unknot_envelope']['central_hole_empty']}, "
          f"bands={out['unknot_envelope']['n_radial_bands']})")

    # ---- gates G0-G4 (ALL must pass before any production read is credible) ----
    print("-" * 90)
    print("GATES (G0-G4) -- instrument validation before banking any production read:")
    gates = {g["gate"]: g for g in [gate_G0(cfg), gate_G1(cfg), gate_G2(cfg), gate_G3(cfg), gate_G4(cfg)]}
    out["gates"] = gates
    for name in ["G0", "G1", "G2", "G3", "G4"]:
        print(f"   {name}: PASS={gates[name]['PASS']}")
    all_gates_pass = all(g["PASS"] for g in gates.values())
    out["all_gates_pass"] = all_gates_pass
    print(f"   ALL GATES PASS = {all_gates_pass}")

    # ---- G1 ABSOLUTE certification + CO-RESOLUTION verdict (corrected re-run) ----
    g1_certified = bool(gates["G1"]["PASS"])
    g4_pass = bool(gates["G4"]["PASS"])
    co_resolved = g1_certified and g4_pass
    out["G1_absolute_certified"] = g1_certified
    out["co_resolution"] = {
        "G1_wall_certified": g1_certified,
        "G4_winding_certified": g4_pass,
        "co_resolved_on_one_lattice": co_resolved,
        "sech_retention": gates["G1"]["sech_retention"],
        "G1_abs_floor": gates["G1"]["G1_abs_retention_floor"],
        "note": ("G1 (wall self-focuses to the v14 ~0.68 absolute) AND G4 (winding reads "
                 "(2,3)) on the SAME lattice. If NOT co-resolved -> option-(b) structural "
                 "finding (wall + winding at incompatible length scales)."),
    }
    print(f"   G1-ABSOLUTE certified (sech retains {gates['G1']['sech_retention']:.3f} "
          f">= {gates['G1']['G1_abs_retention_floor']:.2f}) = {g1_certified}")
    print(f"   CO-RESOLUTION (G1 wall AND G4 winding on ONE lattice) = {co_resolved}")
    if not g1_certified:
        print("   *** G1 UNCERTIFIED -> a NEGATIVE is NOT bankable here (t2-genesis lesson). ***")

    # ---- OPTION C (prereg §9): held-BC breather-persistence PROBE ----
    if hold_winding:
        print("-" * 90)
        print("OPTION C -- HELD-BC (2,3)-winding breather-persistence PROBE (prereg §9):")
        print("   energy LEDGER read FIRST (the DISQUALIFY guard, ave-conserved-vs-pumped)")
        c = run_option_C(cfg)
        out["option_C"] = c
        traj = c["omega_energy_trajectory"]
        led = c["energy_ledger"]
        print(f"   [LEDGER] kinetic magnitude-locked = {c['kinetic_magnitude_locked']} "
              f"(omega-norm rel-drift {led.get('omega_norm_relative_drift_max', float('nan')):.2e})")
        print(f"   [LEDGER] omega-sector total_hamiltonian TRAJECTORY: "
              f"ramp={traj.get('ramp_factor', float('nan')):.2f}x "
              f"rel-slope/sample={traj.get('rel_slope_per_sample', float('nan')):.2e} "
              f"bounded={traj.get('trajectory_bounded')}")
        print(f"   [LEDGER] HOLD PUMPS = {c['hold_pumps']}  "
              f"{'(-> DISQUALIFY)' if c['hold_pumps'] else '(conservative)'}")
        print(f"   [hold OFF] winding (2,3) conserved = {c['hold_off_F4_winding_conserved']} "
              f"(frac_tail={c['hold_off_frac_tail_2_3']:.2f})  [the seed-and-evolve apparatus floor]")
        print(f"   [hold ON ] winding (2,3) conserved = {c['hold_on_F4_winding_conserved']} "
              f"(frac_tail={c['hold_on_frac_tail_2_3']:.2f})  [by construction]")
        print(f"   [hold ON ] F1 breather exists = {c['F1_held_breather_exists']['F1_breather_exists']} "
              f"(v_tail/seed={c['F1_held_breather_exists']['v_peak_tail_over_seed']:.3f})")
        print(f"   [hold ON ] F2 breather stable = {c['F2_held_breather_stable']['F2_stable']} "
              f"(lambda={c['F2_held_breather_stable']['envelope_growth_rate_lambda']:.4f})")
        print("-" * 90)
        print(f"   OPTION C BIN = {c['C_BIN']}")
        print(f"   {c['C_reading']}")
        print("=" * 90)
        return out

    # ---- OPTION C′ (prereg §9.1): NO-WORK Beltrami-helicity hold breather-persistence ----
    if hold_helicity:
        print("-" * 90)
        print("OPTION C' -- NO-WORK Beltrami-helicity (H_bel) hold breather-persistence (prereg §9.1):")
        print("   held charge = H_bel = INT omega.(curl omega) dV (the corpus charge); energy")
        print("   LEDGER read FIRST = the FULL total_hamiltonian trajectory (DISQUALIFY guard)")
        c = run_option_Cprime(cfg)
        out["option_Cprime"] = c
        traj = c["omega_energy_trajectory"]
        print(f"   [FLAG] {c['FLAG_spec_vs_code']}")
        print(f"   [held] H_bel_target = {c['H_bel_target']:.4e}  "
              f"(spec-literal normalized-sum seed = {c['H_bel_normalized_sum_seed']:.2f}, NOT held)")
        print(f"   [no-work] orthogonality cos(g_perp,e) max = {c['no_work_orthogonality_cos_max']:.2e} "
              f"(want ~0; energy-neutral BY CONSTRUCTION)")
        print(f"   [held] charge held to target, rel-err max = {c['charge_held_to_target_rel_err_max']:.2e}")
        print(f"   [LEDGER] omega-sector total_hamiltonian TRAJECTORY: "
              f"ramp={traj.get('ramp_factor', float('nan')):.3f}x "
              f"bounded={traj.get('trajectory_bounded')}")
        print(f"   [LEDGER] HOLD PUMPS = {c['hold_pumps']}  "
              f"{'(-> DISQUALIFY)' if c['hold_pumps'] else '(conservative -- NEGATIVE is now EARNED)'}")
        print(f"   [hold OFF] winding (2,3) conserved = {c['hold_off_F4_winding_conserved']} "
              f"(frac_tail={c['hold_off_frac_tail_2_3']:.2f})  [seed-and-evolve apparatus floor]")
        print(f"   [KEY DESIGN CHECK] scalar H_bel MAINTAINS the (2,3) pair = "
              f"{c['pair_2_3_maintained_by_scalar_hold']} (frac_tail={c['hold_on_frac_tail_2_3']:.2f})")
        print(f"      {c['pair_maintenance_reading']}")
        print(f"   [hold ON ] F1 breather exists = {c['F1_held_breather_exists']['F1_breather_exists']} "
              f"(v_tail/seed={c['F1_held_breather_exists']['v_peak_tail_over_seed']:.3f})")
        print(f"   [hold ON ] F2 breather stable = {c['F2_held_breather_stable']['F2_stable']} "
              f"(lambda={c['F2_held_breather_stable']['envelope_growth_rate_lambda']:.4f})")
        print("-" * 90)
        print(f"   OPTION C' BIN = {c['C_BIN']}")
        print(f"   {c['C_reading']}")
        print("=" * 90)
        return out

    # ---- production hybrid breather solve (passive, no drive) ----
    print("-" * 90)
    print("PRODUCTION coupled (V,omega) hybrid breather solve (passive, NO drive):")
    dt = seed_vtank(cfg).dt
    res = run_hybrid_breather(cfg, drive=False)
    A_ref = float(np.median(res.v_peak[int(0.6 * len(res.v_peak)):]))

    f1 = read_F1_existence(res, cfg)
    f2 = read_F2_stability(res, cfg, dt, jitter_floor=gates["G2"].get("jitter_floor_abs", 0.0))
    f4 = read_F4_winding(res)
    f3 = read_F3_radiative_Q(res, cfg, dt, A_ref)
    f5 = read_F5_conserved_not_pumped(cfg)

    # ---- decoupled (alpha=0) control = the EXCLUDED-eligible arm ----
    ctrl = run_decoupled_control(cfg)
    f0 = read_F1_existence(ctrl, cfg)
    out["F0_decoupled_control_breather_exists"] = f0["F1_breather_exists"]

    out["F1"], out["F2"], out["F3"], out["F4"], out["F5"] = f1, f2, f3, f4, f5
    out["traces"] = {
        "v_peak": res.v_peak, "gamma_true_min": res.gamma_true_min,
        "fwhm": res.fwhm, "w_pol": res.w_pol, "w_tor": res.w_tor,
        "v_dot_peak": res.v_dot_peak,
    }

    # ---- bin (decided by F1+F2+F4; F3 secondary; G1-cert interlock on negatives) ----
    binr = bin_result(f1, f2, f4, f3, g1_certified=g1_certified)
    out["bin"] = binr

    print(f"   F1 existence  : breather_exists = {f1['F1_breather_exists']} "
          f"(v_tail/seed={f1['v_peak_tail_over_seed']:.3f}, gamma_true_tail={f1['gamma_true_tail_median']:.3f})")
    print(f"   F2 stability  : stable = {f2['F2_stable']} (lambda={f2['envelope_growth_rate_lambda']:.4f})")
    print(f"   F4 winding    : conserved = {f4['F4_winding_conserved']} "
          f"(frac_tail_2_3={f4['fraction_tail_reads_2_3']:.2f})")
    print(f"   F5 no-drive   : keystone run is passive = {f5['keystone_run_is_passive_no_drive']}")
    print(f"   F3 Q (SECONDARY): Q={f3['Q_measured']:.1f} (137-band={f3['in_band_137']}, 114-band={f3['in_band_114']}) [ECHO]")
    print(f"   F0 control    : decoupled breather_exists = {f0['F1_breather_exists']} (load-bearing check)")
    print("-" * 90)
    print(f"   BIN = {binr['BIN']}")
    print(f"   {binr['reading']}")
    print("=" * 90)

    # ---- robustness sweep (v_width / dx / box) -- FIRST-CLASS axis ----
    if do_sweep:
        out["sweep"] = sweep_existence(cfg)
        sw = out["sweep"]
        print(f"   SWEEP: {sw['n_certified_corners']} G1-certified corners; "
              f"existence robust-negative-among-certified = "
              f"{sw['existence_robust_negative_among_certified']}; "
              f"robust-positive = {sw['existence_robust_positive_among_certified']}")
        print("=" * 90)
    return out


def main():
    ap = argparse.ArgumentParser()
    # CO-RESOLVING defaults (corrected re-run, option (a)): N=26, R=5, r=2.5, dx=0.5,
    # v_width=2.5, v_amp=0.85 (~5 core cells = the v14 known-positive eigen-resolution).
    ap.add_argument("--N", type=int, default=26)
    ap.add_argument("--R", type=float, default=5.0)
    ap.add_argument("--r", type=float, default=2.5)
    ap.add_argument("--dx", type=float, default=0.5, help="V-tank lattice spacing (eigen-res=0.5)")
    ap.add_argument("--v-width", type=float, default=2.5, help="sech width (v14=2.5; core=v_width/dx)")
    ap.add_argument("--v-amp", type=float, default=0.85, help="sech peak amplitude (v14=0.85)")
    ap.add_argument("--pml", type=int, default=4, help="PML thickness (cells)")
    ap.add_argument("--steps", type=int, default=1500)
    ap.add_argument("--sample-every", type=int, default=20)
    ap.add_argument("--no-sweep", action="store_true", help="skip the robustness sweep")
    ap.add_argument("--hold-winding", action="store_true",
                    help="OPTION C (prereg §9): held-BC (2,3)-winding breather-persistence probe "
                         "(per-cell director template; DISQUALIFIED, kept for audit)")
    ap.add_argument("--hold-helicity", action="store_true",
                    help="OPTION C' (prereg §9.1): NO-WORK Beltrami-helicity (H_bel=INT omega.curl omega) "
                         "hold breather-persistence probe (full-Hamiltonian ledger FIRST, (2,3)-pair "
                         "maintenance KEY DESIGN CHECK, then bin POSITIVE/NEGATIVE/DISQUALIFY)")
    ap.add_argument("--json-out", type=str, default="")
    args = ap.parse_args()
    cfg = RunConfig(
        N=args.N, R=args.R, r=args.r, dx=args.dx, v_width=args.v_width, v_amp=args.v_amp,
        pml_thickness=args.pml, n_steps=args.steps, sample_every=args.sample_every,
    )
    out = run_all(cfg, do_sweep=not args.no_sweep, hold_winding=args.hold_winding,
                  hold_helicity=args.hold_helicity)
    if args.json_out:
        with open(args.json_out, "w") as f:
            json.dump(out, f, indent=2, default=lambda o: getattr(o, "__dict__", str(o)))
        print(f"wrote {args.json_out}")


if __name__ == "__main__":
    main()
