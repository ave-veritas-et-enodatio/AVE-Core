"""
Smoke ladder — COMPONENT 5: the D6 longitudinal-burst detector (calibrated F0d).

  CALIB     an excited free run (mild rotation, no snap) yields a positive finite
            acoustic-scatter floor (the F0d calibration on a known-null).
  GATE      scan() before calibration RAISES (the F0d gate — uncalibrated reads
            cannot be binned as positives).
  DETECT    a hand-snap (known case) releases a latent BURST that clears the floor
            (RESOLVED) and whose magnitude == the known hand-snap latent.
  NULL      a free run with NO snap produces NO bursts above the floor.
  THRESHOLD the burst-count is monotone in the N4 threshold (a count that tracks
            the threshold is apparatus — the CLIP telltale is exposed, not hidden).
  PHASE-SPC the detector frame reads BULK-ledger scalars only (p_integral,
            released-energy), not a transverse w/V Cartesian spike.

Engine:   src/ave/core/unified_genesis_engine.py
Detector: src/ave/core/longitudinal_burst_detector.py
Prereg:   research/2026-06-10_genesis-v5-seeded-snap_prereg.md (D6, F0d, N4)
"""

import numpy as np
import pytest

from ave.core.unified_genesis_engine import UnifiedGenesisEngine
from ave.core.longitudinal_burst_detector import LongitudinalBurstDetector


def _ball(N, rad):
    cc = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    r = np.sqrt((i - cc) ** 2 + (j - cc) ** 2 + (k - cc) ** 2)
    return r <= rad


def _excited(N):
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               nu_art_bulk=2e-3, rho_diff=5e-4)
    eng.energize_rotation_column(M_edge=0.6, R_core=0.18 * N * eng.dx, axis=2)
    return eng


def test_calib_floor_positive_and_finite():
    floor = LongitudinalBurstDetector.calibrate_floor(_excited(28), steps=60)
    assert floor > 0.0 and np.isfinite(floor)


def test_gate_scan_requires_calibration():
    det = LongitudinalBurstDetector()
    det.record(_excited(24))
    with pytest.raises(RuntimeError):
        det.scan()


def test_detect_handsnap_burst_clears_floor_and_matches_latent():
    N = 28
    floor = LongitudinalBurstDetector.calibrate_floor(_excited(N), steps=60)
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               chi_shock=1.0, snap_payback_rate=0.0)
    det = LongitudinalBurstDetector(floor=floor, threshold_mult=3.0)
    det.record(eng)
    latent = eng.hand_snap_region(_ball(N, 3.0))
    det.record(eng)
    bursts = det.scan()
    assert len(bursts) == 1, f"expected one snap burst, got {bursts}"
    idx, mag = bursts[0]
    assert mag > floor * 3.0, "burst must clear the calibrated floor (RESOLVED)"
    # the burst magnitude equals the known hand-snap latent (held, payback=0)
    assert abs(mag - latent) < 1e-9 * (latent + 1e-30), (mag, latent)


def test_null_free_run_no_bursts():
    N = 28
    floor = LongitudinalBurstDetector.calibrate_floor(_excited(N), steps=60)
    eng = _excited(N)  # excited but no snap reaches the floor at this M/steps
    det = LongitudinalBurstDetector(floor=floor, threshold_mult=3.0)
    for _ in range(80):
        eng.step()
        det.record(eng)
    assert eng.pocket_cells() == 0, "setup: no spontaneous snap expected here"
    assert det.scan() == [], "free run must yield no bursts above floor"


def _count(history, floor, t):
    det = LongitudinalBurstDetector(floor=floor, threshold_mult=t)
    det.history = history
    return len(det.scan())


def test_threshold_is_a_clip_knob():
    """The burst-count must be monotone non-increasing in the N4 threshold — the
    apparatus telltale (a count that TRACKS the threshold is CLIP)."""
    N = 28
    floor = 1e-6
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0,
                               snap_payback_rate=0.0)
    det = LongitudinalBurstDetector(floor=floor)
    det.record(eng)
    eng.hand_snap_region(_ball(N, 3.0))
    det.record(eng)
    counts = [_count(det.history, floor, t) for t in (1.0, 10.0, 1e12)]
    assert counts[0] >= counts[1] >= counts[2], counts
    assert counts[-1] == 0, "an absurd threshold must suppress all bursts"


def test_phase_space_detector_reads_bulk_only():
    N = 24
    eng = UnifiedGenesisEngine(N, bulk_density_on=True, snap_on=True, c2_floor=0.0)
    det = LongitudinalBurstDetector(floor=1e-9)
    frame = det.record(eng)
    assert set(frame.keys()) == {"t", "p_integral", "released", "pocket_cells"}
    # 'released' and 'p_integral' are bulk-ledger scalars (no w/V transverse spike)
