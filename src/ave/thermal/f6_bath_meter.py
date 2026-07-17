#!/usr/bin/env python3
"""F6 bath meter — rebuilt mode-count detector (real bath DOF + back-reaction).

Charter: research/2026-07-16_f6-bath-meter_CHARTER.md
Gate: hardware-ratings-map §7 (JOINT detector-rebuild GATE, post-#711/#714).

SECTOR / REGIME (mandatory header):
  Sector    : R7 thermal / entropy-sink (T2 latent-heat channel; F6 ε→T2
              candidate). NOT A1 mass, NOT Cosserat (2,3) winding/charge.
  Mode      : classical reactive TLM lattice (K4, z=3 srs, 4 ports) coupled to
              a Caldeira-Leggett independent-oscillator bath.
  Regime    : linear-response / driven; small-amplitude collar tap.
  Phase-st. : cold plant (no Op14 saturation, no |Γ|→1 yield wall, no node mint).
  Coord.    : N_occ read in the bath's MODAL/spectral phase-space (A46) —
              per-oscillator energy over the {ω_m} comb, NOT a real-space read.

WHAT THIS FIXES (the voided-detector autopsies this module answers):
  - F-1: the old "bath" was `np.zeros(M_MODES)` written by `_credit_modes`, read
         only by `_n_occ`, with ZERO back-reaction (f6_mode_count_event_gated.py;
         Arm B ...arm-b..._prereg_FROZEN.md:139 A1). Here the bath is a genuine
         set of oscillator DOFs (own ω_m, own (x_m,p_m)), evolved every step,
         and the bath's stored field WRITES BACK to the lattice V_inc.
  - F-2: the old FRICTION control was a `credit_modes` flag readback, bit-
         identical to production (Arm A ...:137 A2). Here friction is a real
         Re(Z) termination that removes energy; the meter distinguishes it from
         reactive bath-transfer by a PHYSICAL signature (closed-ledger fraction
         + N_occ), not by which code path ran.
  - F-3: the old ΔN_occ ≡ M_MODES (twin-64 = one constant printed twice). Here
         ω_m = ω_min + m·Δω with FIXED Δω; M is a truncation count. Extra modes
         at larger M are off-resonance → N_occ does NOT track M.

Ax3 discipline: the PRODUCTION coupling is lossless-reactive (no Re(Z) term);
total E_lat + E_bath + E_int is conserved to integrator order. The irreversibility
is by mode-spreading (energy dispersed across many incommensurate ω_m), the honest
F6 ε→T2 mechanism made explicit.

CLEAN INTERFACE (sibling F1 lane owns k4_cosserat_coupling.py / k4_tlm.py — this
module does NOT edit them). It reads: `V_inc`, `mask_active`, `get_energy_density`,
`nx/ny/nz`, `step`. It writes: `V_inc` at the collar (the back-reaction). Rebase
onto the merged F1 fix and re-run V1-V6 before any downstream integration.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

# Canonical constants imported per rail (numerical epsilons are substrate-native).
from ave.core.constants import EPS_DIVZERO

# --- instrument design defaults (ENGINEERING CHOICES — tagged, not physics) ---
# Bath dispersion comb in lattice-step units. Δω and ω_min are FIXED physical
# properties of the bath; M is a truncation count. Operating point (validated):
# the comb starts at ω_min=0.30 and the M=32 range [0.30, 1.23] fully contains
# the collar drive's spectral content (dominant ω_q≈0.5-0.7, tail to ~1.1), so
# the resonantly-driven set is identical across all validated M ∈ {32, 64, 128}
# and the extra modes at larger M are off-resonance (undriven).
OMEGA_MIN_DEFAULT = 0.30
DELTA_OMEGA_DEFAULT = 0.03
G0_DEFAULT = 1.0
# Occupancy floor as a FRACTION of the peak mode energy (a fraction of the drive
# scale — charter §3). A mode is "occupied" if its energy exceeds FLOOR_FRAC×peak.
# Set an order of magnitude above the off-resonant mode sea so only resonantly-
# driven modes count → N_occ tracks the driven bandwidth, NOT the truncation M.
# Engineering choice; frozen for the battery. E_m is phase-invariant (it combines
# each mode's C-state x_m and L-state p_m), so it IS the cycle-averaged occupancy
# by construction — no windowing needed (free rotation preserves E_m exactly).
FLOOR_FRAC_DEFAULT = 0.02


@dataclass
class OscillatorBath:
    """A genuine set of harmonic-oscillator DOFs — the real bath DOF.

    Each mode m has its own frequency ω_m = omega_min + m·delta_omega (a FIXED
    dispersion comb), its own state (x_m, p_m), and is evolved every step. This
    is NOT a write-only accumulator: `free_rotate` advances the true oscillator
    phase and `coupling_kick` drives it via the coupled EOM; its dynamical energy
    change is what the coupler feeds back to the lattice (LatticeBathCoupler.step).
    Occupancy is read from the physical per-mode energy (spectral phase-space).
    """

    M: int
    omega_min: float = OMEGA_MIN_DEFAULT
    delta_omega: float = DELTA_OMEGA_DEFAULT
    g0: float = G0_DEFAULT
    omega: np.ndarray = field(init=False)
    g: np.ndarray = field(init=False)
    x: np.ndarray = field(init=False)
    p: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        m = np.arange(self.M, dtype=float)
        # FIXED-spacing comb: larger M extends the range, does NOT densify it.
        self.omega = self.omega_min + m * self.delta_omega
        # Spectral coupling density depends on ω_m only (NOT on M) so the driven
        # set is M-invariant. Flat density here (Ohmic-flat).
        self.g = np.full(self.M, self.g0, dtype=float)
        self.x = np.zeros(self.M, dtype=float)
        self.p = np.zeros(self.M, dtype=float)

    # --- physical reads (spectral phase-space; A46) ---
    def mode_energy(self) -> np.ndarray:
        """Per-mode energy E_m = ½ p_m² + ½ ω_m² x_m² (spectral occupancy)."""
        return 0.5 * self.p**2 + 0.5 * self.omega**2 * self.x**2

    def energy(self) -> float:
        return float(self.mode_energy().sum())

    def n_occ(self, floor_frac: float = FLOOR_FRAC_DEFAULT) -> int:
        """Physical occupancy: modes with energy above floor_frac × peak-mode-energy.

        Can genuinely fail: an undriven bath (all E_m = 0) reads 0; a narrowband
        drive reads few; and — because ω spacing is fixed and the floor sits above
        the off-resonant mode sea — the count tracks the driven bandwidth, NOT the
        truncation M. This is the read that kills the twin-64 (ΔN_occ ≡ M_MODES).
        """
        e = self.mode_energy()
        peak = float(e.max()) if e.size else 0.0
        if peak <= EPS_DIVZERO:
            return 0
        return int(np.count_nonzero(e > floor_frac * peak))

    def occupied_bandwidth(self, floor_frac: float = FLOOR_FRAC_DEFAULT) -> float:
        """Intensive read: N_occ × Δω (physical bandwidth of the transfer)."""
        return self.n_occ(floor_frac) * self.delta_omega

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
        content) build negligible amplitude → they do not populate above the floor.
        """
        self.p += dt * kappa * self.g * q


def make_collar_mask(lat, center, r_in: float, r_out: float) -> np.ndarray:
    """Active lattice sites in the shell r_in ≤ r ≤ r_out about `center`.

    The collar is the coupling port — a native set of active sites, no Cartesian
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

    Production mode (`friction=False`): lossless-reactive coupling. Each step
    advances the lattice, drives the bath from the collar field q via the coupled
    EOM (`coupling_kick` + exact `free_rotate`), then applies the BACK-REACTION as
    an energy-conserving reactive load: the collar (V_inc, V_ref) amplitude is
    scaled so the lattice gives up exactly the energy ΔE_bath the bath's own
    dynamics absorbed this step. This is genuine two-way coupling — when the bath
    phase drives energy back (ΔE_bath < 0) the collar scales UP — and it is
    exactly lossless-reactive (E_lat + E_bath conserved by construction; Ax3).
    The irreversibility is by mode-spreading: energy dispersed across many
    incommensurate ω_m does not return on relevant timescales.

    Rationale for the energy-matched back-reaction (vs a bilinear force law): a
    bare −∂H_int/∂q force written into V_inc does NOT conserve against the opaque
    TLM stepper (it pumps, requiring a large 1/ω² Caldeira-Leggett counter-term
    that destabilises and pollutes the ledger). The energy-matched reactive load
    is the honest lossless-reactive coupling and mirrors the friction plant's
    scaling exactly, so the two differ ONLY by physics (energy in a DOF vs gone).

    Friction mode (`friction=True`): the reactive bath coupling is REPLACED by a
    real Re(Z) lossy termination (V_inc, V_ref)[collar] ← (1−γ)·(...) of matched
    magnitude — a genuine dissipator (energy leaves the total ledger), not a flag.
    The bath is left undriven (n_occ stays 0; energy is gone, not stored). This is
    the physical FRICTION control the §7 gate requires.
    """

    lat: object
    bath: OscillatorBath
    collar: np.ndarray
    kappa: float = 0.02
    dt: float = 1.0
    friction: bool = False
    gamma: float = 0.0  # Re(Z) loss-per-step (friction mode only)
    # optional external drive q_ext(step) — used by the V3 known-transfer plant to
    # drive the bath directly (bypassing the lattice) with a hand-built tone.
    q_ext: object = None

    n_collar: int = field(init=False)
    n_port: int = field(init=False)

    def __post_init__(self) -> None:
        self.n_collar = int(np.count_nonzero(self.collar))
        self.n_port = self.lat.V_inc.shape[-1]

    # --- clean-interface reads/writes ---
    def read_q(self) -> float:
        """Collar collective coordinate q = Σ_{s∈collar} mean_p (V_inc + V_ref).

        (V_inc + V_ref) is the position-like (voltage) collar coordinate; its
        conjugate (V_inc − V_ref) is momentum-like (current). q drives the bath.
        """
        if self.n_collar == 0:
            return 0.0
        block = self.lat.V_inc[self.collar] + self.lat.V_ref[self.collar]
        return float(block.mean(axis=-1).sum())

    def _collar_energy(self) -> float:
        return float((self.lat.V_inc[self.collar] ** 2).sum() + (self.lat.V_ref[self.collar] ** 2).sum())

    def _scale_collar(self, energy_delta: float) -> None:
        """Scale collar (V_inc, V_ref) amplitude so its energy drops by energy_delta.

        energy_delta > 0 removes energy from the collar (bath absorbing);
        energy_delta < 0 adds energy (bath driving back — genuine two-way
        back-reaction). Phase-preserving amplitude scaling = a lossless-reactive
        load. This same op with a FIXED (1−γ)² factor is the friction plant, so
        reactive vs dissipative differ only by where the energy goes.
        """
        if self.n_collar == 0:
            return
        e_c = self._collar_energy()
        if e_c <= EPS_DIVZERO:
            return
        scale = np.sqrt(max((e_c - energy_delta) / e_c, 0.0))
        self.lat.V_inc[self.collar] *= scale
        self.lat.V_ref[self.collar] *= scale

    def _apply_friction(self) -> float:
        """Real Re(Z) termination: (V_inc, V_ref)[collar] ← (1−γ)·(...).

        Returns the energy removed this step (leaves the total ledger — gone).
        """
        if self.n_collar == 0 or self.gamma <= 0.0:
            return 0.0
        e_before = self._collar_energy()
        self.lat.V_inc[self.collar] *= 1.0 - self.gamma
        self.lat.V_ref[self.collar] *= 1.0 - self.gamma
        return e_before - self._collar_energy()

    # --- energy ledger accessors ---
    def e_lat(self) -> float:
        return float(self.lat.total_energy())

    def e_bath(self) -> float:
        return self.bath.energy()

    def step(self, istep: int) -> None:
        """One coupled step: lattice advance + bath evolve + back-reaction."""
        self.lat.step()

        if self.friction:
            # Real dissipator; bath left undriven (stays empty; energy gone).
            self._friction_removed = getattr(self, "_friction_removed", 0.0) + self._apply_friction()
            return

        # Reactive coupling: drive the bath via the coupled EOM (symmetric split).
        q = self.q_ext(istep) if self.q_ext is not None else self.read_q()
        half = 0.5 * self.dt
        e_bath_before = self.bath.energy()
        self.bath.coupling_kick(half, q, self.kappa)  # half kick (drive)
        self.bath.free_rotate(self.dt)  # exact free rotation
        self.bath.coupling_kick(half, q, self.kappa)  # half kick (drive)
        if self.q_ext is None:
            # Energy-conserving reactive back-reaction: the lattice gives up exactly
            # the energy the bath's dynamics absorbed this step. (Skipped for the
            # direct-drive V3 plant, which characterises the READ in isolation.)
            d_e_bath = self.bath.energy() - e_bath_before
            self._scale_collar(d_e_bath)
