"""
S11 small-signal probe on the crystal-graft carrier (electron datasheet).
==========================================================================

A network-analyzer-style instrument layered on ``CrystalGraftV2``: inject a
small sinusoidal drive force into one sector at a source mask, optionally apply
a controllable linear damping to that sector (for the KNOWN-resonator gate), and
read the steady-state response with a single-frequency lock-in (in-phase I and
quadrature Q over a settled window). NO change to the inherited bulk-V / shear-w
/ micro-rotation-omega / buckle dynamics — the ``step`` below reproduces the
parent 3-sector leapfrog verbatim and ADDS exactly two probe terms.

Governing prereg (FROZEN, committed alone first):
    research/2026-06-10_electron-s11-sweep_prereg.md
The probe is validated on a KNOWN resonator (the omega mass-gap driven-damped
oscillator, c_omega=0 => f0=omega_gap/2pi exactly, Q=omega_gap/gamma_probe)
BEFORE it is pointed at the unknown locked state (ave-apparatus-floor-attribution
probe-capability gate). substrate-native-check CP6: BOTH lock-in quadratures are
recorded; CP7: the read excludes PML cells; CP9: the drive is a physical force in
the acceleration, the response is the integrated field (no painted Lorentzian).
"""

from __future__ import annotations

import numpy as np

from ave.core.crystal_graft_v2 import CrystalGraftV2


class S11Probe(CrystalGraftV2):
    """CrystalGraftV2 + a small-signal sinusoidal drive + optional linear damping
    on the driven sector + a single-frequency lock-in read."""

    def __init__(
        self,
        N: int,
        *,
        drive_sector: str = "V",  # "V" (bulk) or "omega" (winding carrier)
        drive_omega: float = 1.0,  # angular drive frequency
        drive_amp: float = 0.0,  # small-signal amplitude (linearity-gated)
        src_center: tuple | None = None,
        src_sigma: float = 3.0,
        gamma_probe: float = 0.0,  # uniform linear damping on the driven sector (GATE only)
        drive_dir: tuple = (0.0, 0.0, 1.0),  # omega-sector drive direction
        **kwargs,
    ):
        super().__init__(N, **kwargs)
        if drive_sector not in ("V", "omega"):
            raise ValueError("drive_sector must be 'V' or 'omega'")
        self.drive_sector = drive_sector
        self.drive_omega = float(drive_omega)
        self.drive_amp = float(drive_amp)
        self.gamma_probe = float(gamma_probe)
        self.drive_dir = np.asarray(drive_dir, dtype=float)
        n = np.linalg.norm(self.drive_dir)
        if n > 0:
            self.drive_dir = self.drive_dir / n
        c = (self.N - 1) / 2.0
        cx, cy, cz = src_center if src_center is not None else (c, c, c)
        i, j, k = np.indices((self.N, self.N, self.N))
        r2 = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
        self._src_mask = np.exp(-r2 / (2.0 * src_sigma**2))

    # ------------------------------------------------------------ step
    def step(self):
        """One leapfrog step: inherited 3-sector physics + probe drive + (gate)
        probe damping. The two probe lines are the ONLY additions."""
        t = self.time  # evaluate the drive at the pre-step time (explicit forcing)

        # ---- inherited accelerations (verbatim from CrystalGraftV2.step) ----
        c_eff_sq = self.c_eff_squared(self.V)
        a_V = c_eff_sq * self._laplacian(self.V, self.dx)
        a_w = np.empty_like(self.w)
        for comp in range(3):
            a_w[..., comp] = (self.c_T**2) * self._laplacian(self.w[..., comp], self.dx)
        a_omega = np.empty_like(self.omega)
        if self.omega_sector_on:
            for comp in range(3):
                a_omega[..., comp] = (
                    self.c_omega**2 * self._laplacian(self.omega[..., comp], self.dx)
                    - self.omega_gap**2 * self.omega[..., comp]
                )
        else:
            a_omega[:] = 0.0
        if self.omega_sector_on and self.buckle_on:
            f_V, f_omega = self._buckle_forces()
            a_V = a_V + f_V
            a_omega = a_omega + f_omega

        # ---- PROBE TERM 1: the small-signal sinusoidal drive force ----
        drive = self.drive_amp * np.sin(self.drive_omega * t)
        if self.drive_sector == "V":
            a_V = a_V + drive * self._src_mask
        else:  # omega
            a_omega = a_omega + (drive * self._src_mask)[..., None] * self.drive_dir

        # ---- PROBE TERM 2 (GATE only): uniform linear damping -gamma*velocity ----
        if self.gamma_probe > 0.0:
            if self.drive_sector == "V":
                vel = (self.V - self.V_prev) / self.dt
                a_V = a_V - self.gamma_probe * vel
            else:
                vel = (self.omega - self.omega_prev) / self.dt
                a_omega = a_omega - self.gamma_probe * vel

        # ---- leapfrog update (verbatim) ----
        V_new = 2.0 * self.V - self.V_prev + (self.dt**2) * a_V
        w_new = 2.0 * self.w - self.w_prev + (self.dt**2) * a_w
        omega_new = 2.0 * self.omega - self.omega_prev + (self.dt**2) * a_omega

        V_new *= self.damping
        w_new *= self.damping[..., None]
        omega_new *= self.damping[..., None]

        self.V_prev, self.V = self.V, V_new
        self.w_prev, self.w = self.w, w_new
        self.omega_prev, self.omega = self.omega, omega_new
        self.time += self.dt
        self.step_count += 1

    # --------------------------------------------------------- read probe
    def read_signal(self, read_mask: np.ndarray) -> float:
        """Scalar response read at the (PML-excluded) read mask. For a V-drive,
        the bulk field; for an omega-drive, the driven-direction projection."""
        if self.drive_sector == "V":
            field = self.V
        else:
            field = self.omega @ self.drive_dir
        return float(np.sum(field * read_mask) / (np.sum(read_mask) + 1e-30))

    def lockin(self, read_mask: np.ndarray, n_settle: int, n_win: int) -> dict:
        """Single-frequency lock-in: settle the transient, then accumulate the
        in-phase (I) and quadrature (Q) projections of the read signal onto the
        drive frequency over the window. Returns amplitude, phase, and both
        quadratures (CP6 reactance pair — both recorded)."""
        for _ in range(n_settle):
            self.step()
        I = 0.0
        Qd = 0.0
        T = 0.0
        for _ in range(n_win):
            self.step()
            t = self.time
            sig = self.read_signal(read_mask)
            I += sig * np.sin(self.drive_omega * t) * self.dt
            Qd += sig * np.cos(self.drive_omega * t) * self.dt
            T += self.dt
        if T <= 0:
            return {"amp": 0.0, "phase": 0.0, "I": 0.0, "Q": 0.0}
        I *= 2.0 / T
        Qd *= 2.0 / T
        return {
            "amp": float(np.hypot(I, Qd)),
            "phase": float(np.arctan2(Qd, I)),
            "I": float(I),
            "Q": float(Qd),
        }
