#!/usr/bin/env python3
r"""Moving-defect double-slit HARNESS — slit geometry + per-channel readouts +
keepers for the bulk-vs-transverse pilot fork.

Prereg: research/2026-06-11_moving-defect-doubleslit_prereg.md
  §5 observables (obs-1 slit-balance, obs-2 per-channel fringe, obs-3 λ_dB
  period, obs-4 visibility) · §6 capability gate · §7 controls.

STATUS — the FORK-READ IS GATED OFF. The Phase-2 capability gate
(moving_defect_transport_gate.py) returned **ENGINE-GAP**: no engine hosts a
self-consistent bounded-spread translating defect with per-channel readout, so
there is no valid translating pilot to read through these slits yet. Running a
fork-read now would measure a dispersing blob (sim-2 blur regime), not a pilot.

This module is therefore the ROADMAP-READY APPARATUS: engine-agnostic slit
geometry, PML-excluded per-channel extractors, and the reactance-pair keeper,
ALL validated on KNOWN synthetic fields via `--selfcheck` (C4
validate-on-known-positive / ave-apparatus-floor-attribution). When an engine
closes the transport gap (boost-covariant multi-channel bound state), wire its
per-channel field maps into these same extractors — the apparatus is calibrated.

  python moving_defect_doubleslit_harness.py --selfcheck   # validate extractors
  python moving_defect_doubleslit_harness.py               # prints GATED notice
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np


# --------------------------------------------------------------------------
# Slit geometry (sim-2 convention: deactivated cells = perfect reflector wall;
# x = propagation axis, y = slit-separation axis). prereg §1.3 / §5.
# --------------------------------------------------------------------------
@dataclass
class SlitGeometry:
    NX: int = 120
    NY: int = 96
    NZ: int = 16
    pml: int = 6
    guard: int = 8  # PML+guard exclusion band (prereg CP7 / A-Rule-10)
    wall_x: int = 60
    wall_thick: int = 3
    slit_sep: int = 30  # centre-to-centre aperture separation d
    slit_w: int = 3
    screen_x: int = 104
    lambda_cells: float = 12.0  # de-Broglie λ in cells (forward-set per obs-3)

    @property
    def slit1_y(self) -> int:
        return self.NY // 2 - self.slit_sep // 2

    @property
    def slit2_y(self) -> int:
        return self.NY // 2 + self.slit_sep // 2

    @property
    def L(self) -> int:
        """Wall-to-screen distance."""
        return self.screen_x - self.wall_x

    def fraunhofer_spacing(self) -> float:
        """Two-slit fringe spacing Δy = λ·L/d (small-angle). prereg obs-3."""
        return self.lambda_cells * self.L / self.slit_sep

    def aperture_window(self, which: int):
        """(x-slice, y-slice) just downstream of the wall at aperture `which`∈{1,2}."""
        y0 = self.slit1_y if which == 1 else self.slit2_y
        xs = slice(self.wall_x + self.wall_thick, self.wall_x + self.wall_thick + 4)
        ys = slice(y0 - self.slit_w // 2, y0 + self.slit_w // 2 + 1)
        return xs, ys


def build_active_mask(g: SlitGeometry, two_slit: bool = True) -> np.ndarray:
    """Boolean active-cell mask (False = reflecting wall). One or two apertures."""
    mask = np.ones((g.NX, g.NY, g.NZ), dtype=bool)
    wall = slice(g.wall_x, g.wall_x + g.wall_thick)
    mask[wall, :, :] = False  # solid wall
    # reopen aperture(s)
    s1 = slice(g.slit1_y - g.slit_w // 2, g.slit1_y + g.slit_w // 2 + 1)
    mask[wall, s1, :] = True
    if two_slit:
        s2 = slice(g.slit2_y - g.slit_w // 2, g.slit2_y + g.slit_w // 2 + 1)
        mask[wall, s2, :] = True
    return mask


def interior_mask(g: SlitGeometry) -> np.ndarray:
    """PML+guard-excluded interior (A-Rule-10 / prereg CP7)."""
    m = np.zeros((g.NX, g.NY, g.NZ), dtype=bool)
    lo = g.pml + g.guard
    m[lo : g.NX - lo, lo : g.NY - lo, :] = True
    return m


# --------------------------------------------------------------------------
# Per-channel readouts (prereg §5). Each takes a real-space |field| map for ONE
# channel (longitudinal div u / V_inc, OR transverse w / τ_zx) — engine-agnostic.
# --------------------------------------------------------------------------
def slit_balance(field_abs: np.ndarray, g: SlitGeometry, transited: int = 1, top_k: int = 5) -> float:
    """obs-1 — flood ratio = amp(non-transited slit) / amp(transited slit).

    Density-peak sampled (top-K |field|², NOT centroid — A-Rule-10). A channel
    that floods BOTH slits → ratio ≈ 1; a channel confined to the transited slit
    → ratio ≈ 0.
    """
    other = 2 if transited == 1 else 1

    def _peak(which):
        xs, ys = g.aperture_window(which)
        window = (field_abs[xs, ys, :] ** 2).ravel()
        if window.size == 0:
            return 0.0
        k = min(top_k, window.size)
        return float(np.sqrt(np.mean(np.partition(window, -k)[-k:])))

    a_t = _peak(transited)
    a_o = _peak(other)
    return a_o / a_t if a_t > 0 else float("nan")


def screen_pattern(field_abs: np.ndarray, g: SlitGeometry) -> np.ndarray:
    """obs-2 — |field|²(y) along the screen row, PML+guard excluded, z-summed."""
    lo = g.pml + g.guard
    row = (field_abs[g.screen_x, :, :] ** 2).sum(axis=-1)
    out = np.zeros_like(row)
    out[lo : g.NY - lo] = row[lo : g.NY - lo]
    return out


def fringe_period(pattern: np.ndarray, min_period: float = 3.0) -> float:
    """obs-3 — dominant fringe spacing (cells) via real-FFT peak. Compared
    forward to Δy=λ_dB·L/d (validity gate vs blur). Returns nan if no peak."""
    y = np.asarray(pattern, dtype=float)
    y = y - y.mean()
    if not np.any(y):
        return float("nan")
    spec = np.abs(np.fft.rfft(y))
    freqs = np.fft.rfftfreq(y.size, d=1.0)
    valid = freqs > (1.0 / (y.size))  # drop DC
    valid &= freqs < (1.0 / min_period)
    if not np.any(valid):
        return float("nan")
    f_peak = freqs[valid][np.argmax(spec[valid])]
    return 1.0 / f_peak if f_peak > 0 else float("nan")


def visibility(pattern: np.ndarray) -> float:
    """obs-4 — fringe visibility V=(Imax−Imin)/(Imax+Imin) over the lit region."""
    y = np.asarray(pattern, dtype=float)
    lit = y[y > 0.02 * y.max()] if y.max() > 0 else y
    if lit.size == 0 or (lit.max() + lit.min()) == 0:
        return float("nan")
    return float((lit.max() - lit.min()) / (lit.max() + lit.min()))


# --------------------------------------------------------------------------
# Keeper — reactance-pair recorder (A-Rule-10): C-state (V_inc / ω) AND L-state
# (Φ_link / ω_dot) every step. A single-phase snapshot cannot distinguish a
# translating pilot from an oscillator caught at peak (prereg §2 PHASE-STATE).
# --------------------------------------------------------------------------
class ReactancePairRecorder:
    """Engine-agnostic: call `record(c_state, l_state)` each step over the window."""

    def __init__(self):
        self.c_state: list[float] = []  # capacitive: V_inc / ω
        self.l_state: list[float] = []  # inductive: Φ_link / ω_dot

    def record(self, c_state: float, l_state: float) -> None:
        self.c_state.append(float(c_state))
        self.l_state.append(float(l_state))

    def both_live(self) -> bool:
        """Both reactances must vary over the window (not a frozen snapshot)."""
        if len(self.c_state) < 2:
            return False
        return float(np.std(self.c_state)) > 0.0 and float(np.std(self.l_state)) > 0.0


# --------------------------------------------------------------------------
# Self-check (C4 validate-on-known-positive) — calibrate the extractors on
# SYNTHETIC fields with KNOWN answers before any engine field is read.
# --------------------------------------------------------------------------
def _gaussian2d(g: SlitGeometry, cx, cy, sigma, amp=1.0) -> np.ndarray:
    i, j, _ = np.indices((g.NX, g.NY, g.NZ))
    return amp * np.exp(-((i - cx) ** 2 + (j - cy) ** 2) / (2.0 * sigma**2))


def selfcheck() -> bool:
    g = SlitGeometry()
    ok = True

    # (1) both-slit FLOOD field: two equal lobes at the apertures -> slit_balance ≈ 1
    flood = _gaussian2d(g, g.wall_x + g.wall_thick + 1, g.slit1_y, 2.0) + _gaussian2d(
        g, g.wall_x + g.wall_thick + 1, g.slit2_y, 2.0
    )
    sb_flood = slit_balance(flood, g, transited=1)
    p1 = abs(sb_flood - 1.0) < 0.1
    ok &= p1
    print(f"[selfcheck] obs-1 both-slit flood: slit_balance={sb_flood:.3f} (expect ~1)  {'PASS' if p1 else 'FAIL'}")

    # (2) single-slit CONFINED field: lobe only at slit 1 -> slit_balance ≈ 0
    confined = _gaussian2d(g, g.wall_x + g.wall_thick + 1, g.slit1_y, 2.0)
    sb_conf = slit_balance(confined, g, transited=1)
    p2 = sb_conf < 0.1
    ok &= p2
    print(f"[selfcheck] obs-1 single-slit:     slit_balance={sb_conf:.3f} (expect ~0)  {'PASS' if p2 else 'FAIL'}")

    # (3) known two-beam interference at the screen -> fringe_period recovers it
    period = 12.0
    y = np.arange(g.NY)
    env = np.exp(-((y - g.NY / 2) ** 2) / (2.0 * 22.0**2))
    pat = (1.0 + np.cos(2 * np.pi * y / period)) * env
    pr = fringe_period(pat)
    p3 = abs(pr - period) / period < 0.12
    ok &= p3
    print(f"[selfcheck] obs-3 fringe period:   measured={pr:.2f} cells (expect {period})  {'PASS' if p3 else 'FAIL'}")

    # (4) visibility of a known-contrast pattern
    vis = visibility(pat)
    p4 = vis > 0.9
    ok &= p4
    print(f"[selfcheck] obs-4 visibility:      V={vis:.3f} (expect ~1 for full-contrast)  {'PASS' if p4 else 'FAIL'}")

    # (5) PML+guard exclusion: a source planted IN the PML must not reach extractors
    pml_only = _gaussian2d(g, 2, 2, 1.0)  # corner, inside PML
    sp = screen_pattern(pml_only, g)
    p5 = float(np.abs(sp).max()) == 0.0
    ok &= p5
    print(f"[selfcheck] CP7 PML exclusion:     screen leak={np.abs(sp).max():.3e} (expect 0)  {'PASS' if p5 else 'FAIL'}")

    # (6) keeper: both reactances must be flagged live only when both vary
    rec = ReactancePairRecorder()
    for t in range(10):
        rec.record(np.sin(t), np.cos(t))
    p6 = rec.both_live()
    rec_dead = ReactancePairRecorder()
    for t in range(10):
        rec_dead.record(np.sin(t), 1.0)  # L-state frozen
    p6 &= not rec_dead.both_live()
    ok &= p6
    print(f"[selfcheck] keeper reactance-pair: live-detect + frozen-reject  {'PASS' if p6 else 'FAIL'}")

    # (7) geometry sanity: Fraunhofer spacing positive + apertures inside interior
    p7 = g.fraunhofer_spacing() > 0 and (g.pml + g.guard) < g.slit1_y < g.slit2_y < (g.NY - g.pml - g.guard)
    ok &= p7
    print(f"[selfcheck] geometry: Δy={g.fraunhofer_spacing():.2f} cells, apertures interior  {'PASS' if p7 else 'FAIL'}")

    print(f"\n[selfcheck] {'ALL PASS — apparatus calibrated on known fields' if ok else 'FAILURES PRESENT'}")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selfcheck", action="store_true", help="validate extractors on known synthetic fields (C4)")
    args = ap.parse_args()
    if args.selfcheck:
        raise SystemExit(0 if selfcheck() else 1)
    print(
        "FORK-READ GATED OFF — transport capability gate returned ENGINE-GAP\n"
        "  (see moving_defect_transport_gate.py: no engine hosts a self-consistent\n"
        "   bounded-spread translating defect with per-channel readout).\n"
        "  This harness is the roadmap-ready apparatus; run --selfcheck to validate\n"
        "  the extractors. Wire engine per-channel maps in once the gap is closed."
    )


if __name__ == "__main__":
    main()
