"""
Detector sector - the honest part: clicks from threshold-crossing, NOT Born.

A detector screen is a row of cells. Each cell accumulates absorbed field
ENERGY under fluctuation-dissipation (FDT) noise and SELF-TRAPS (one click)
the instant its accumulated amplitude crosses the Axiom-4 saturation yield

        S(A) = sqrt(1 - (A / A_yield)^2)  ->  0     (A -> A_yield).

That is the ENTIRE click rule: stochastic energy loading + a first-passage
threshold. There is deliberately:

    * NO Born rule,
    * NO  p = |psi|^2,
    * NO sampling from |psi|^2  (no rng.choice(p=...), no inverse-CDF of |E|^2),
    * NO probability normalisation of the field anywhere.

The only field quantity the detector consumes is the PHYSICAL absorbed-power
density (the FDTD field energy density, == |E|^2). It enters as an absorption
RATE - "a cell absorbs energy at a rate set by the local field power" - which
is detector physics + energy conservation, not a probability postulate.

Why the Born exponent (the "2") is then recovered, honestly:
  A real detector responds to ENERGY, and field energy density is |E|^2
  (Poynting / Maxwell - computed by the FDTD, not chosen here). So the
  per-cell absorption rate is proportional to |E|^2. Independent first-passage
  threshold-crossings then fire cell i first with probability proportional to
  its rate (competing first-passage / shot statistics) -> p(cell i) ∝ |E|^2.
  The exponent 2 is "energy ∝ amplitude^2", not the Born postulate. If a
  detector instead responded to amplitude |E|^1, the recovered law would be
  p ∝ |E|^1 - which would NOT match the wave-optics fringe pattern. The match
  to |E|^2 is forced by energy absorption (see ``validate.exponent_scan``).

Classification (consistency-vs-emergence):
  * discrete localized clicks from a continuous field  -> Class-2 emergence
  * histogram of clicks reproducing |psi|^2 (Born)      -> Class-2 emergence
  * agreement with the QM Born rule + Fraunhofer fringe -> Class-4 consistency
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.axioms.scale_invariant import saturation_factor

from .config import DetectorConfig

# Saturation-kernel collapse threshold: a cell self-traps when S(A) falls below
# this (i.e. the Axiom-4 kernel has gone impulsive at its vertical tangent).
_TRAP_EPS = 1.0e-3


@dataclass
class ClickResult:
    click_cells: np.ndarray  # detector-cell index of every click, in arrival order
    n_cells: int
    histogram: np.ndarray  # counts per detector cell (len n_cells)
    mean_micro_steps: float  # mean first-passage time per electron [micro-steps]
    cfg: DetectorConfig


def accumulate_clicks(
    intensity: np.ndarray,
    cfg: DetectorConfig | None = None,
    *,
    verbose: bool = False,
) -> ClickResult:
    """Fire ``cfg.n_clicks`` electrons at the screen; return where each clicked.

    Parameters
    ----------
    intensity:
        The PHYSICAL absorbed-power density along the detector row (== |E|^2
        from the FDTD). Consumed as an absorption RATE per cell - never as a
        probability. Only its relative shape matters; the absolute scale is
        absorbed into ``coupling`` (detector quantum efficiency), so it is
        rescaled to unit mean. This rescale is a units choice, NOT a
        normalisation-to-a-probability (it does not sum to 1).
    """
    cfg = cfg or DetectorConfig()
    intensity = np.asarray(intensity, dtype=float)
    intensity = np.clip(intensity, 0.0, None)
    n = intensity.size

    # Rescale to unit MEAN (a units/efficiency choice). NOT a probability:
    # sum(rate) != 1; this is W/m^2 absorbed-power in detector units.
    mean_i = intensity.mean()
    rate = intensity / mean_i if mean_i > 0 else np.zeros_like(intensity)

    rng = np.random.default_rng(cfg.seed)
    a_yield = cfg.a_yield
    dt = cfg.dt
    sigma_thermal = np.sqrt(2.0 * cfg.thermal_kT * dt)
    rate_dt = cfg.coupling * rate * dt  # mean shot-quanta absorbed per micro-step

    click_cells = np.empty(cfg.n_clicks, dtype=np.int64)
    total_micro = 0

    for e in range(cfg.n_clicks):
        accum = np.zeros(n)  # accumulated absorbed energy per cell
        winner = -1
        for _ in range(cfg.max_micro_steps):
            # FDT shot noise: discrete energy quanta absorbed this micro-step,
            # mean delivery rate proportional to local field POWER (rate).
            shot = rng.poisson(rate_dt) * cfg.quantum
            # Johnson-Nyquist thermal (FDT) Langevin jitter.
            thermal = rng.normal(0.0, sigma_thermal, n)
            accum += shot + thermal
            np.maximum(accum, 0.0, out=accum)

            amp = np.sqrt(accum)
            # Axiom-4 self-trap gate: collapse where the canonical saturation
            # kernel has driven to its (impulsive) vertical tangent.
            s = saturation_factor(amp, a_yield)
            crossed = np.nonzero(s <= _TRAP_EPS)[0]
            total_micro += 1
            if crossed.size:
                # First-passage: a cell self-traps the instant it crosses yield.
                # With the small per-step crossing probability used here, a
                # single cell crosses per micro-step; on the rare simultaneous
                # tie we pick uniformly among the crossers (NOT weighted by the
                # field - that would smuggle in Born). Both crossed because each
                # independently absorbed a yield-quantum, so they are equally
                # "first".
                winner = int(crossed[0] if crossed.size == 1 else rng.choice(crossed))
                break

        if winner < 0:  # safety: no crossing within the cap -> brightest realised
            winner = int(np.argmax(accum))
        click_cells[e] = winner

        if verbose and (e + 1) % 1000 == 0:
            print(f"  [clicks] {e + 1}/{cfg.n_clicks} electrons fired")

    histogram = np.bincount(click_cells, minlength=n).astype(float)
    return ClickResult(
        click_cells=click_cells,
        n_cells=n,
        histogram=histogram,
        mean_micro_steps=total_micro / max(cfg.n_clicks, 1),
        cfg=cfg,
    )


if __name__ == "__main__":  # pragma: no cover - manual smoke run
    # A toy two-bump "intensity" just to exercise the loop.
    y = np.linspace(-1, 1, 200)
    toy = np.exp(-((y - 0.3) ** 2) / 0.02) + np.exp(-((y + 0.3) ** 2) / 0.02)
    res = accumulate_clicks(toy, DetectorConfig(n_clicks=500))
    print("clicks:", res.click_cells.size, "mean micro-steps:", round(res.mean_micro_steps, 1))
