#!/usr/bin/env python3
"""F6 bath meter — rebuilt mode-count detector (real bath DOF + back-reaction).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md (+ amendment §A, 2026-07-17,
recording the post-#717-review repairs — read it: the shipped back-reaction is a
GLOBAL energy-matched reactive load, not the charter §2 bilinear force law).
Gate: hardware-ratings-map §7 (JOINT detector-rebuild GATE, post-#711/#714).

SECTOR / REGIME (mandatory header):
  Sector    : R7 thermal / entropy-sink (T2 latent-heat channel; F6 ε→T2
              candidate). NOT A1 mass, NOT Cosserat (2,3) winding/charge.
  Mode      : classical reactive TLM lattice (K4, z=3 srs, 4 ports) coupled to
              a modal oscillator bath.
  Regime    : linear-response / driven; small-amplitude collar tap.
  Phase-st. : cold plant (LINEAR lattice: nonlinear=False — no Op14 saturation,
              consistent with charter §0; no |Γ|→1 yield wall, no node mint).
  Coord.    : N_occ read in the bath's MODAL/spectral phase-space (A46) —
              per-oscillator energy over the {ω_m} comb, NOT a real-space read.

WHAT THIS FIXES (the voided-detector autopsies this module answers):
  - F-1: the old "bath" was `np.zeros(M_MODES)` written by `_credit_modes`, read
         only by `_n_occ`, with ZERO back-reaction (f6_mode_count_event_gated.py;
         Arm B ...arm-b..._prereg_FROZEN.md:139 A1). Here the bath is a genuine
         set of oscillator DOFs (own ω_m, own (x_m,p_m)), evolved every step,
         and the bath's dynamical energy demand WRITES BACK to the lattice.
  - F-2: the old FRICTION control was a `credit_modes` flag readback, bit-
         identical to production (Arm A ...:137 A2). Here friction is a real
         Re(Z) damping on a LIVE, driven bath; the meter distinguishes it from
         reactive storage by a PHYSICAL signature (closed-ledger fraction R:
         stored vs dissipated/gone), genuinely measured on both plants.
  - F-3: the old ΔN_occ ≡ M_MODES (twin-64 = one constant printed twice). Here
         ω_m = ω_min + m·Δω with FIXED Δω; M is a truncation count. Within the
         Nyquist envelope (ω_max·dt < π, enforced) extra modes are off-resonance
         → N_occ does NOT track M. (Beyond the envelope, discrete-time aliasing
         re-drives modes at ω ≡ ±ω_drive (mod 2π) — hence the hard cap.)

Ax3 discipline: the PRODUCTION back-reaction is a GLOBAL, phase-preserving,
energy-matched reactive load (the whole cavity amplitude is rescaled by the ΔE
the bath's own coupled EOM absorbs). Because a scalar multiple of an on-shell
TLM state stays on-shell, total E_lat + E_bath is conserved to ~1e-15 over 3000
steps (measured — see V6; NOT a per-step collar rescale, which drove the lattice
OFF-SHELL and pumped +4%/3000-steps, the #717-review CRITICAL). The irreversible
F6 candidate mechanism is mode-spreading; the meter reads it, does not assert it.

CLEAN INTERFACE (sibling F1 lane owns k4_cosserat_coupling.py / k4_tlm.py — this
module does NOT edit them). It reads: `V_inc`, `V_ref`, `mask_active`,
`total_energy`, `nx/ny/nz`, `step`. It writes: `V_inc`/`V_ref` (global amplitude
rescale). Rebase onto the merged F1 fix and re-run V1-V6 before integration.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

# Canonical constants imported per rail (numerical epsilons are substrate-native).
from ave.core.constants import EPS_DIVZERO

# --- instrument design defaults (ENGINEERING CHOICES — tagged, not physics) ---
# Bath dispersion comb in lattice-step units. Δω and ω_min are FIXED physical
# properties of the bath; M is a truncation count. Operating point (validated):
# the comb starts at ω_min=0.30 and covers the collar drive's spectral content
# (dominant ω_q≈0.5-0.7). Within the Nyquist envelope (ω_max·dt < π ⇒ M ≤ 95 at
# this comb) the extra modes at larger M are off-resonance (undriven).
OMEGA_MIN_DEFAULT = 0.30
DELTA_OMEGA_DEFAULT = 0.03
G0_DEFAULT = 1.0
# Occupancy floor: ABSOLUTE per-mode energy threshold (charter §3: a fixed fraction
# of the drive scale). Calibrated ONE order of magnitude above the off-resonant
# mode sea of the production plant (median E_m ~ 8e-5, peak ~1.4) so only
# resonantly-populated modes count and N_occ reads 0 on detuned/near-dead spectra.
# (Restores the frozen ABSOLUTE semantics; the shipped relative-to-peak floor was
# the #717-review MAJOR — it counted the off-resonant sea on collapsed transfer.)
FLOOR_ABS_DEFAULT = 1e-2
# Minimum TOTAL bath energy for any nonzero N_occ read — belt-and-suspenders gate
# so eps-level crosstalk cannot register occupancy (the #717-review robustness hole).
E_BATH_MIN_DEFAULT = 1e-2


@dataclass
class OscillatorBath:
    """A genuine set of harmonic-oscillator DOFs — the real bath DOF.

    Each mode m has its own frequency ω_m = omega_min + m·delta_omega (a FIXED
    dispersion comb), its own state (x_m, p_m), and is evolved every step. This
    is NOT a write-only accumulator: `free_rotate` advances the true oscillator
    phase and `coupling_kick` drives it via the coupled EOM; its dynamical energy
    change is what the coupler feeds back to the lattice (LatticeBathCoupler.step).
    Occupancy is read from the physical per-mode energy (spectral phase-space).

    NYQUIST ENVELOPE (enforced): the coupling kicks sample the collar drive at
    dt=1.0, so a mode at ω_m is resonantly driven whenever ω_m ≡ ±ω_drive (mod 2π)
    — discrete-time aliasing. `__post_init__` asserts ω_max·dt < π so the comb
    stays below Nyquist and the M-invariance (twin-64 kill) holds structurally
    rather than by accident of where the aliases land.
    """

    M: int
    omega_min: float = OMEGA_MIN_DEFAULT
    delta_omega: float = DELTA_OMEGA_DEFAULT
    g0: float = G0_DEFAULT
    dt: float = 1.0
    omega: np.ndarray = field(init=False)
    g: np.ndarray = field(init=False)
    x: np.ndarray = field(init=False)
    p: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        m = np.arange(self.M, dtype=float)
        # FIXED-spacing comb: larger M extends the range, does NOT densify it.
        self.omega = self.omega_min + m * self.delta_omega
        omega_max = float(self.omega[-1]) if self.M else 0.0
        # Nyquist guard — coupling kicks alias above ω·dt = π (the #717-review
        # CRITICAL: twin-64 resurrects at M≥~184 via 2π−ω_drive re-entering the comb).
        if omega_max * self.dt >= np.pi:
            raise ValueError(
                f"OscillatorBath comb exceeds the Nyquist envelope: "
                f"omega_max*dt = {omega_max * self.dt:.3f} >= pi. "
                f"At omega_min={self.omega_min}, delta_omega={self.delta_omega}, dt={self.dt} "
                f"the alias-free cap is M <= {int((np.pi / self.dt - self.omega_min) / self.delta_omega) + 1}. "
                f"Reduce M or dt (see charter amendment §A / Nyquist envelope)."
            )
        # Spectral coupling density depends on ω_m only (NOT on M) so the driven
        # set is M-invariant. Flat density here (Ohmic-flat).
        self.g = np.full(self.M, self.g0, dtype=float)
        self.x = np.zeros(self.M, dtype=float)
        self.p = np.zeros(self.M, dtype=float)

    # --- physical reads (spectral phase-space; A46) ---
    def mode_energy(self) -> np.ndarray:
        """Per-mode energy E_m = ½ p_m² + ½ ω_m² x_m² (spectral occupancy).

        E_m is phase-invariant (it combines each mode's C-state x_m and L-state
        p_m; free rotation preserves it exactly) — so it IS the cycle-averaged
        occupancy by construction, no windowing needed.
        """
        return 0.5 * self.p**2 + 0.5 * self.omega**2 * self.x**2

    def energy(self) -> float:
        return float(self.mode_energy().sum())

    def n_occ(
        self,
        floor_abs: float = FLOOR_ABS_DEFAULT,
        e_bath_min: float = E_BATH_MIN_DEFAULT,
    ) -> int:
        """Physical occupancy: modes whose energy exceeds the ABSOLUTE floor.

        Two gates, both tied to the fixed drive scale (charter §3):
          - total-bath gate: if Σ E_m < e_bath_min the bath is effectively empty →
            0 (kills eps-level / detuned-tail false positives);
          - per-mode gate: count modes with E_m > floor_abs.
        Can genuinely fail: an undriven bath reads 0; a narrowband drive reads few;
        a collapsed (detuned) transfer reads 0; and — within the Nyquist envelope,
        because ω spacing is fixed and the floor is above the off-resonant sea —
        the count does NOT track M. This is the read that kills the twin-64.
        """
        e = self.mode_energy()
        if e.size == 0 or float(e.sum()) < e_bath_min:
            return 0
        return int(np.count_nonzero(e > floor_abs))

    def occupied_bandwidth(self, floor_abs: float = FLOOR_ABS_DEFAULT) -> float:
        """Intensive read: N_occ × Δω (physical bandwidth of the transfer).

        M-invariant AND the right quantity under Δω-variation: refining Δω raises
        N_occ but leaves the occupied bandwidth ~fixed (tracks the driven band,
        not the truncation) — the V2 Δω-hardening check.
        """
        return self.n_occ(floor_abs) * self.delta_omega

    def participation_number(self) -> float:
        """N_eff = (Σ E_m)² / (Σ E_m²) — M-invariant spectral-spread cross-check."""
        e = self.mode_energy()
        num = float(e.sum()) ** 2
        den = float((e**2).sum())
        return num / den if den > EPS_DIVZERO else 0.0

    # --- dynamics (evolved every step) ---
    def free_rotate(self, dt: float) -> None:
        """Exact free-oscillator rotation (energy-exact for the free part)."""
        theta = self.omega * dt
        c, s = np.cos(theta), np.sin(theta)
        x_new = c * self.x + (s / np.maximum(self.omega, EPS_DIVZERO)) * self.p
        p_new = -self.omega * s * self.x + c * self.p
        self.x, self.p = x_new, p_new

    def coupling_kick(self, dt: float, q: float, kappa: float) -> None:
        """Half/whole coupling kick: ṗ_m += κ g_m q · dt (the lattice drives bath).

        From H_int = −κ q Σ_m g_m x_m, the force on x_m is −∂H_int/∂x_m = κ g_m q.
        The bath EOM ṗ_m = −ω_m² x_m + κ g_m q is a genuine coupled equation, not a
        credit-to-a-side-array. Off-resonant modes (ω_m far from q's spectral
        content, within the Nyquist envelope) build negligible amplitude → they do
        not populate above the floor.
        """
        self.p += dt * kappa * self.g * q

    def damp(self, beta: float) -> float:
        """Real Re(Z) dissipation on the bath modes: (x,p) ← (1−β)(x,p).

        Returns the energy removed (dissipated — GONE from all tracked DOF). Used
        by the FRICTION plant to turn a LIVE, driven bath into a dissipating one,
        so N_occ and R are genuinely measured on a driven-but-lossy bath rather
        than forced by a code-path flag (the #717-review MAJOR on V4).
        """
        if beta <= 0.0:
            return 0.0
        e_before = self.energy()
        self.x *= 1.0 - beta
        self.p *= 1.0 - beta
        return e_before - self.energy()


def make_collar_mask(lat, center, r_in: float, r_out: float) -> np.ndarray:
    """Active lattice sites in the shell r_in ≤ r ≤ r_out about `center`.

    The collar is the drive-read port — a native set of active sites, no Cartesian
    stencil imposed. Read-only construction from lat.mask_active.
    """
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = np.asarray(center, dtype=float)
    r2 = (ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2
    shell = (r2 >= r_in**2) & (r2 <= r_out**2)
    return shell & lat.mask_active


@dataclass
class LatticeBathCoupler:
    """Couples an OscillatorBath to a K4 lattice through the clean interface.

    Production (`friction=False`): lossless-reactive coupling. Each step advances
    the lattice, reads the collar drive q, drives the bath via the coupled EOM
    (`coupling_kick` + exact `free_rotate`), then applies the BACK-REACTION as a
    GLOBAL, phase-preserving, energy-matched reactive load — the whole active-cell
    amplitude (V_inc, V_ref) is rescaled so the lattice gives up exactly the ΔE the
    bath's own dynamics absorbed this step. Genuine two-way, bath-EOM-gated
    coupling: when the bath is off-resonance ΔE≈0 and the rescale is ~1 (no back-
    reaction); when resonant it modulates the cavity (detuning collapses the
    transfer ~3000× — the resonance gate). It conserves E_lat + E_bath to ~1e-15
    over 3000 steps because a scalar multiple of an on-shell TLM state stays on
    shell (measured by V6).

    NOTE (charter amendment §A): this is NOT the charter §2 bilinear force law
    F_q = κΣg_m x_m − counter-term written into V_inc. That force law does not
    conserve against the opaque TLM stepper (pumps, needs a destabilising 1/ω²
    counter-term); a LOCAL collar rescale drove the lattice off-shell and pumped
    +4%/3000-steps (the #717-review CRITICAL). The GLOBAL rescale is the honest
    lossless-reactive realisation. It returns AMOUNT (bidirectional, bath-EOM-
    gated) but not PHASE (spatially-uniform, phase-blind) — stated as a known
    limitation.

    Friction (`friction=True`): the bath coupling stays LIVE (same reactive drive
    + rescale) but the bath modes carry a real Re(Z) damping β so the transferred
    energy is DISSIPATED (gone), not stored. N_occ and R are genuinely MEASURED on
    a driven-but-dissipating bath (they can fail); the discriminator is the closed-
    ledger fraction R (reactive: stored ⇒ R≈0; friction: dissipated ⇒ R→1).
    """

    lat: object
    bath: OscillatorBath
    collar: np.ndarray
    kappa: float = 0.012
    dt: float = 1.0
    friction: bool = False
    beta: float = 0.0  # bath Re(Z) damping-per-step (friction mode only)
    # optional external drive q_ext(step) — used by the V3 known-transfer plant to
    # drive the bath directly (bypassing the lattice) with a hand-built tone.
    q_ext: object = None

    n_collar: int = field(init=False)
    active: np.ndarray = field(init=False)
    friction_removed: float = field(init=False, default=0.0)

    def __post_init__(self) -> None:
        self.n_collar = int(np.count_nonzero(self.collar))
        self.active = self.lat.mask_active

    # --- clean-interface reads/writes ---
    def read_q(self) -> float:
        """Collar collective coordinate q = Σ_{s∈collar} mean_p (V_inc + V_ref).

        (V_inc + V_ref) is the position-like (voltage) collar coordinate. q drives
        the bath (read-only extraction).
        """
        if self.n_collar == 0:
            return 0.0
        block = self.lat.V_inc[self.collar] + self.lat.V_ref[self.collar]
        return float(block.mean(axis=-1).sum())

    def _global_rescale(self, energy_delta: float) -> None:
        """Rescale the whole active cavity amplitude so E_lat drops by energy_delta.

        energy_delta > 0 removes energy (bath absorbing); < 0 adds it (bath driving
        back — genuine two-way). Global uniform scaling keeps the TLM state on-shell,
        so the next step() conserves (no off-shell pump). Phase-preserving ⇒
        lossless-reactive (Ax3).
        """
        e_lat = float(self.lat.total_energy())
        if e_lat <= EPS_DIVZERO:
            return
        scale = np.sqrt(max((e_lat - energy_delta) / e_lat, 0.0))
        self.lat.V_inc[self.active] *= scale
        self.lat.V_ref[self.active] *= scale

    # --- energy ledger accessors ---
    def e_lat(self) -> float:
        return float(self.lat.total_energy())

    def e_bath(self) -> float:
        return self.bath.energy()

    def step(self, istep: int) -> None:
        """One coupled step: lattice advance + bath evolve + back-reaction."""
        self.lat.step()

        # Drive the bath via the coupled EOM (symmetric split). LIVE in both modes.
        q = self.q_ext(istep) if self.q_ext is not None else self.read_q()
        half = 0.5 * self.dt
        e_bath_before = self.bath.energy()
        self.bath.coupling_kick(half, q, self.kappa)
        self.bath.free_rotate(self.dt)
        self.bath.coupling_kick(half, q, self.kappa)
        d_e_bath = self.bath.energy() - e_bath_before

        if self.q_ext is None:
            # Energy-matched GLOBAL reactive back-reaction (skipped for the direct-
            # drive V3 plant, which characterises the READ in isolation).
            self._global_rescale(d_e_bath)

        if self.friction:
            # Real Re(Z) damping on the LIVE bath — the transferred energy is
            # dissipated (gone), turning storage into dissipation.
            self.friction_removed += self.bath.damp(self.beta)
