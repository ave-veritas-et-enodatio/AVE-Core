"""
D6 — the LONGITUDINAL-BURST detector (genesis-v5 component 5)
============================================================

The snap's signature is an IMPULSIVE latent release in the exact-EOS BULK ledger
(the pressure() integral / the per-cell latent tally) — NOT a transverse-Cartesian
field spike (phase-space-coordinate-check: the FLASH lives in the bulk ρ̄/p(ρ̄)
channel, measured in its own coordinate).

ave-apparatus-floor-attribution / F0d (HARD CONSTRAINT): the detector is CALIBRATED
on a KNOWN CASE FIRST — its floor is the free-run scatter of the bulk ledger (the
acoustic noise a real burst must clear). A burst below the floor is UNRESOLVED, NOT
a positive. The burst-detection threshold (N4) is itself a CLIP suspect: a burst-
count that tracks the threshold is apparatus.

The detector watches the cumulative snap-released energy (all destinations: held
latent + restored + dissipated + vented) whose per-step INCREMENT is the impulsive
longitudinal release, and gates it against the bulk pressure-integral's free-run
scatter floor.
"""

from __future__ import annotations


class LongitudinalBurstDetector:
    """Watches the BULK exact-EOS ledger for impulsive snap-latent bursts, gated by
    a free-run-calibrated floor (F0d)."""

    def __init__(self, floor: float | None = None, threshold_mult: float = 3.0):
        self.floor = floor                  # the F0d acoustic scatter floor (calibrated)
        self.threshold_mult = float(threshold_mult)  # N4 burst threshold (CLIP suspect)
        self.history: list[dict] = []

    @staticmethod
    def _released(engine) -> float:
        """Total snap-released energy (all destinations) — its increment is the
        impulsive longitudinal release. Reads ONLY bulk-ledger scalars."""
        return (engine.E_latent_held + engine.E_latent_restored
                + engine.E_diss_snap + getattr(engine, "E_vent_to_seed", 0.0)
                + getattr(engine, "E_vent_radiated", 0.0))

    def record(self, engine) -> dict:
        """Append one detector frame (BULK observables only; phase-space-correct)."""
        frame = {
            "t": float(engine.time),
            "p_integral": float(engine.bulk_pressure_integral()),
            "released": float(self._released(engine)),
            "pocket_cells": int(engine.pocket_cells()),
        }
        self.history.append(frame)
        return frame

    @staticmethod
    def calibrate_floor(engine, steps: int) -> float:
        """F0d: run the KNOWN-NULL (the supplied free/excited engine) and return the
        max per-step |Δ(bulk pressure-integral)| — the acoustic scatter floor a real
        burst must clear. Mutates the engine (steps it)."""
        prev = float(engine.bulk_pressure_integral())
        floor = 0.0
        for _ in range(steps):
            engine.step()
            cur = float(engine.bulk_pressure_integral())
            floor = max(floor, abs(cur - prev))
            prev = cur
        return floor

    def scan(self) -> list[tuple[int, float]]:
        """Return [(frame_index, burst_magnitude)] where the per-step released-energy
        increment exceeds floor·threshold_mult. floor=None ⇒ raises (must calibrate
        first — the F0d gate)."""
        if self.floor is None:
            raise RuntimeError("detector floor not calibrated (F0d gate): call "
                               "calibrate_floor on a known-null first")
        bar = self.floor * self.threshold_mult
        bursts = []
        for i in range(1, len(self.history)):
            d = self.history[i]["released"] - self.history[i - 1]["released"]
            if d > bar:
                bursts.append((i, d))
        return bursts

    def total_burst_energy(self) -> float:
        if not self.history:
            return 0.0
        return self.history[-1]["released"] - self.history[0]["released"]
