"""Shared configuration + output-path anchoring for the double-slit capstone."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# This file lives at
#   <repo-root>/src/scripts/vol_2_subatomic/ave_double_slit_born/config.py
# so parents[4] is the repo root regardless of the launching CWD.
REPO_ROOT: Path = Path(__file__).resolve().parents[4]

# Deliverables land in research/figures/ per the capstone spec (NOT the generic
# assets/sim_outputs tree). The directory is a generated-output tree, so it is
# created on demand.
FIG_DIR: Path = REPO_ROOT / "research" / "figures" / "2026-06-08-ave-double-slit"


def fig_path(name: str) -> Path:
    """Return a path under the capstone figure directory, creating the dir."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    return FIG_DIR / name


@dataclass(frozen=True)
class FieldConfig:
    """Geometry + drive for the REAL FDTD field (canonical FDTD3DEngine).

    All lengths are in grid cells; ``dx`` only sets the (irrelevant) absolute
    metric - the physics is scale-free here because the field is linear Maxwell
    well below V_yield. The interference fringe spacing obeys the Fraunhofer /
    de-Broglie relation  dy = lambda * L / d  in these same cell units.
    """

    nx: int = 320
    ny: int = 400
    nz: int = 3  # z-thin slab -> TM_z 2D slice; mid-plane z=1 is physical
    dx: float = 1.0e-3

    x_src: int = 24  # point source column (cylindrical wavepacket launcher)
    wall_x: int = 88  # double-slit barrier column
    wall_thickness: int = 4
    slit_width: int = 8
    slit_sep: int = 72  # centre-to-centre slit separation d [cells]
    x_det: int = 280  # detector row column; L = x_det - wall_x

    omega: float = 0.16  # source angular frequency [rad/step]
    cw: bool = False  # True: coherent wave train (long-flux limit); False: pulsed wavepacket
    phasor: bool = True  # extract coherent |amplitude|^2 via I/Q demod over a few carrier periods
    phasor_window: int = 120  # phasor integration window [steps] (~3 carrier periods)
    ramp_steps: float = 120.0  # CW smooth turn-on [steps] (avoids transient shock)
    burst_center: float = 360.0  # pulsed mode: Gaussian envelope centre t0 [steps]
    burst_tau: float = 150.0  # pulsed mode: Gaussian envelope width [steps]
    amplitude: float = 1.0  # arbitrary (linear regime)

    n_steps: int = 1300
    # Pulse peak reaches the detector at ~ burst_center + (x_det - x_src)/(0.8/sqrt(3)) ~ 914.
    record_start: int = 854  # phasor window start (pulse arrival minus ~half window)

    sponge_width: int = 16  # perimeter absorbing layer (boundary aid, not Maxwell)
    sponge_damp: float = 0.05

    snapshot_steps: tuple[int, ...] = (480, 660, 800, 914)

    @property
    def slit_centres(self) -> tuple[int, int]:
        c = self.ny // 2
        return (c - self.slit_sep // 2, c + self.slit_sep // 2)

    @property
    def L(self) -> int:
        """Slit-to-detector distance [cells]."""
        return self.x_det - self.wall_x


@dataclass(frozen=True)
class DetectorConfig:
    """FDT threshold-crossing click model.

    The detector consumes the PHYSICAL field intensity (absorbed power density,
    = |E|^2 from the FDTD) as an absorption RATE - never as a probability. A
    cell self-traps (one click) when its accumulated amplitude crosses the
    Axiom-4 saturation yield. See ``click_detector`` for the (Born-free) logic.
    """

    a_yield: float = 1.0  # saturation-yield amplitude S(a_yield)=0 (units of accum. amplitude)
    # Single-quantum-sensitive regime: one absorbed yield-quantum self-traps the
    # cell (m = a_yield^2 / quantum ~ 1). Competing Poisson absorption then fires
    # cell i first with probability proportional to its rate (= |E|^2) -> Born.
    coupling: float = 2.0e-4  # absorption-rate constant (small -> rare ties, genuine first-passage)
    quantum: float = 1.0  # accumulated-energy per absorbed shot quantum
    thermal_kT: float = 3.0e-4  # Johnson-Nyquist (FDT) sub-threshold jitter
    dt: float = 1.0  # detector micro-step
    max_micro_steps: int = 60000  # safety cap per electron
    seed: int = 20260608

    n_clicks: int = 6000  # total electrons fired (clicks accumulated)
    snapshot_counts: tuple[int, ...] = field(default_factory=lambda: (12, 120, 800, 6000))
