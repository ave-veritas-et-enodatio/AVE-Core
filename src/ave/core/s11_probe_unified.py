"""
S11 small-signal probe RE-LAYERED on the v6 UnifiedGenesisEngine (de-novo).
==========================================================================

FLAG-B (prereg 2026-06-11_s11-de-novo §3): the canonical ``S11Probe`` subclasses
``CrystalGraftV2``, whose ``step`` has NO bulk-density rho_bar / u_adv sector, NO
self-limiting snap, NO chiral transducer — i.e. none of the v6 physics. Pointing
``S11Probe`` at the *made* object would probe a V2 object, not the v6 product.
This class re-instantiates the SAME #166 instrument on ``UnifiedGenesisEngine``
(<- CrystalGraftV4 <- V3 <- V2 <- CrystalEngine) so the probe drives the ACTUAL
made object, with the SAME two #166 probe terms and the SAME I/Q lock-in.

RE-LAYER METHOD (substrate-native-check: operator-re-derivation-on-a-different-
engine trigger; inherited physics UNCHANGED — the HARD constraint):

  The #166 ``S11Probe`` reproduces ``CrystalGraftV2.step`` VERBATIM and inserts
  the two probe terms INTO the sector acceleration BEFORE the leapfrog. Verbatim-
  copying the much deeper ``UnifiedGenesisEngine.step`` (V4 buckle + helicity lock
  + bulk RK2 + snap state-machine + chiral transducer) would be a divergence
  hazard. Instead this class CALLS ``super().step()`` (the full unified physics,
  byte-for-byte unchanged) and then ADDS the mathematically-EQUIVALENT post-step
  correction. For any leapfrog of the form

        X_new = (2*X - X_prev + dt**2 * a_phys) * damping            (parent)

  inserting the probe terms into the acceleration gives

        X_new' = (2*X - X_prev + dt**2 * (a_phys + a_drive + a_damp)) * damping
               = X_new + dt**2 * (a_drive + a_damp) * damping

  so adding ``dt**2 * (a_drive + a_damp) * damping`` to ``self.X`` AFTER
  ``super().step()`` is IDENTICAL to the #166 in-acceleration injection — provided
  the driven sector X is updated by exactly one leapfrog+PML in the parent step
  and nothing else touches it afterward. That holds here for the configs used:

    * V channel (the made-object bulk probe): self.V is touched ONLY by the
      leapfrog+PML in the unified step (the bulk RK2 acts on rho_bar/u_adv, the
      snap on rho_bar, the transducer on w_prev/u_adv/omega_prev, the lock on
      omega; vent_into_seed is OFF in the MAIN recipe -> V_prev untouched). So the
      V-channel post-step correction is EXACT regardless of snap/transducer/lock.
    * omega channel (the probe-capability gate): the gate config sets
      lock_on=False, buckle_on=False, bulk_density_on=False, so omega is a pure
      leapfrog -> the correction is EXACT.

  KNOWN-NULL (the inherited-physics-unchanged proof): with drive_amp == 0 AND
  gamma_probe <= 0 the correction is exactly zero and ``step`` is BYTE-IDENTICAL
  to ``UnifiedGenesisEngine.step``. The driver asserts this directly.

substrate-native-check CP6: BOTH lock-in quadratures (I in-phase / Q quadrature)
are recorded over the settled window. CP7: the read excludes PML cells. CP9: the
drive is a physical force density in the acceleration (no painted Lorentzian); the
response is the integrated field. CP10: the drive is a localized interior source
mask, not a global bulk forcing; the Gamma=-1 wall (c_eff trap) is untouched.
"""

from __future__ import annotations

import numpy as np

from ave.core.unified_genesis_engine import UnifiedGenesisEngine


class S11ProbeUnified(UnifiedGenesisEngine):
    """UnifiedGenesisEngine + the #166 small-signal sinusoidal drive + optional
    linear damping on the driven sector + the single-frequency I/Q lock-in. The
    probe terms are additive and behind ``_probe_active`` (default OFF)."""

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
        bulk_clip_on: bool = False,  # V-neutral numerical hygiene on the DECOUPLED bulk (default OFF)
        bulk_clip_val: float = 1.0e3,
        **kwargs,
    ):
        super().__init__(N, **kwargs)
        if drive_sector not in ("V", "omega"):
            raise ValueError("drive_sector must be 'V' or 'omega'")
        self.bulk_clip_on = bool(bulk_clip_on)
        self.bulk_clip_val = float(bulk_clip_val)
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

    @property
    def _probe_active(self) -> bool:
        return (self.drive_amp != 0.0) or (self.gamma_probe > 0.0)

    # ------------------------------------------------------------ step
    def step(self):
        """super().step() (FULL unified physics, UNCHANGED) + the equivalent
        post-step probe correction. drive_amp==0 and gamma_probe<=0 => byte-
        identical to UnifiedGenesisEngine.step (the known-null)."""
        if not self._probe_active:
            super().step()
            return

        # --- capture PRE-step quantities (the #166 explicit-forcing convention) ---
        t = self.time  # drive evaluated at the pre-step time
        if self.drive_sector == "V":
            vel = (self.V - self.V_prev) / self.dt
        else:
            vel = (self.omega - self.omega_prev) / self.dt

        # --- the FULL inherited unified step (V/w/omega/buckle/lock/bulk/snap/
        #     transducer), byte-for-byte unchanged ---
        super().step()

        # --- the two #166 probe terms, added as the equivalent post-step
        #     correction (see module docstring for the leapfrog-linearity proof) ---
        drive = self.drive_amp * np.sin(self.drive_omega * t)
        if self.drive_sector == "V":
            a_probe = drive * self._src_mask
            if self.gamma_probe > 0.0:
                a_probe = a_probe - self.gamma_probe * vel
            self.V = self.V + (self.dt**2) * a_probe * self.damping
        else:  # omega
            a_probe = (drive * self._src_mask)[..., None] * self.drive_dir
            if self.gamma_probe > 0.0:
                a_probe = a_probe - self.gamma_probe * vel
            self.omega = self.omega + (self.dt**2) * a_probe * self.damping[..., None]

        # --- V-NEUTRAL numerical hygiene on the DECOUPLED bulk-density sector ---
        # (FLAG-D; default OFF -> byte-identical known-null preserved). The made
        # object's rho_bar/u_adv overflow under free evolution (EOS 1-rho^2 singular-
        # ity + transducer re-feed). V/omega are EMPIRICALLY DECOUPLED from them
        # (decouple test V|live-zeroed|=0), so clamping the runaway bulk to a finite
        # value is MEASUREMENT-NEUTRAL for V/omega AND keeps the step on the fast
        # finite-arithmetic path (NaN/inf propagation is ~3x slower). For the build/
        # known-null the bulk stays well within +-bulk_clip_val so this is a no-op
        # (byte-identical); it only bites the post-settle runaway. Reported, not a
        # silent fix; does NOT alter any inherited sector's evolution of V/w/omega.
        if self.bulk_clip_on and getattr(self, "bulk_density_on", False):
            cv = self.bulk_clip_val
            np.nan_to_num(self.rho_bar, copy=False, nan=0.0, posinf=cv, neginf=-cv)
            np.nan_to_num(self.u_adv, copy=False, nan=0.0, posinf=cv, neginf=-cv)
            np.clip(self.rho_bar, -cv, cv, out=self.rho_bar)
            np.clip(self.u_adv, -cv, cv, out=self.u_adv)

    # --------------------------------------------------------- read probe
    def read_signal(self, read_mask: np.ndarray) -> float:
        """Scalar response read at the (PML-excluded) read mask. For a V-drive,
        the bulk field; for an omega-drive, the driven-direction projection.
        Verbatim from the #166 S11Probe.read_signal."""
        if self.drive_sector == "V":
            field = self.V
        else:
            field = self.omega @ self.drive_dir
        return float(np.sum(field * read_mask) / (np.sum(read_mask) + 1e-30))

    def lockin(self, read_mask: np.ndarray, n_settle: int, n_win: int) -> dict:
        """Single-frequency lock-in: settle the transient, then accumulate the
        in-phase (I) and quadrature (Q) projections of the read signal onto the
        drive frequency over the window. Returns amplitude, phase, and both
        quadratures (CP6 reactance pair). Verbatim from the #166 S11Probe.lockin."""
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
