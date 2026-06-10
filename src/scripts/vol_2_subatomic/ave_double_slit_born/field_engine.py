"""
Field sector - the REAL FDTD interference field.

A wavepacket through two slits, solved with the *canonical* AVE Maxwell engine
``ave.core.fdtd_3d.FDTD3DEngine`` (Yee-cell TLM lattice). NO Maxwell update is
re-implemented here: we drive the engine's public soft-source / step API and
impose a PEC slit wall by zeroing the tangential field Ez at wall cells each
step (a boundary condition layered on the canonical engine).

A z-thin slab (nz=3) carries a TM_z 2D slice: with a z-uniform Ez source and a
z-uniform wall, only (Ez, Hx, Hy) are populated and the field stays z-uniform,
so the mid-plane z=1 is a faithful 2D Maxwell solution.

Outputs (all REAL FDTD products):
  * ``intensity_y`` : time-integrated |Ez|^2 along the detector row == |psi|^2
                      (the energy-density landing profile of one wavepacket).
  * ``snapshots``   : 2D |Ez|^2 frames for the smooth-field still + animation.
  * ``wall_mask2d`` : the barrier geometry for plotting.
  * ``wavelength``  : carrier wavelength [cells], MEASURED from the propagating
                      field, plus the analytic estimate.
  * ``fringe_spacing_pred`` : Fraunhofer / de-Broglie prediction lambda*L/d.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine

from .config import FieldConfig


@dataclass
class FieldResult:
    intensity_y: np.ndarray  # |psi|^2 along the detector row (len ny)
    intensity2d: np.ndarray  # time-averaged |Ez|^2 over the whole 2D slice (nx, ny)
    snapshots: list[np.ndarray]  # list of 2D |Ez|^2 frames (nx, ny)
    snapshot_steps: tuple[int, ...]
    anim_frames: list[np.ndarray]  # subsampled 2D |Ez|^2 frames for animation
    anim_steps: list[int]
    wall_mask2d: np.ndarray  # bool (nx, ny)
    slit_centres: tuple[int, int]
    x_det: int
    wavelength_measured: float
    wavelength_analytic: float
    fringe_spacing_pred: float
    z_uniformity: float  # max relative std across z (should be ~0)
    cfg: FieldConfig


def _build_wall_mask(cfg: FieldConfig) -> np.ndarray:
    """PEC barrier (nx, ny): True where Ez is clamped to 0; slits are gaps."""
    mask = np.zeros((cfg.nx, cfg.ny), dtype=bool)
    mask[cfg.wall_x : cfg.wall_x + cfg.wall_thickness, :] = True
    for cy in cfg.slit_centres:
        lo = cy - cfg.slit_width // 2
        hi = cy + cfg.slit_width // 2
        mask[cfg.wall_x : cfg.wall_x + cfg.wall_thickness, lo:hi] = False
    return mask


def _build_sponge(cfg: FieldConfig) -> np.ndarray:
    """Perimeter absorbing multiplier (nx, ny). Boundary aid, NOT a Maxwell edit.

    This damps outgoing radiation near the grid edges so 1st-order Mur ABC
    reflections do not contaminate the interior fringe pattern. It is applied
    multiplicatively to the engine's public field arrays after each step - the
    canonical Yee update itself is untouched.
    """
    w = cfg.sponge_width
    damp = np.ones((cfg.nx, cfg.ny))
    for i in range(w):
        d = 1.0 - cfg.sponge_damp * ((w - i) / w) ** 2
        damp[i, :] *= d
        damp[cfg.nx - 1 - i, :] *= d
        damp[:, i] *= d
        damp[:, cfg.ny - 1 - i] *= d
    return damp


def _measure_wavelength(ez2d: np.ndarray, cfg: FieldConfig) -> float:
    """Measure carrier wavelength [cells] from a horizontal cut in free space.

    Cut along x on the source row, between the source and the wall, FFT it, and
    take the dominant spatial period.
    """
    cy = cfg.ny // 2
    x0 = cfg.x_src + 6
    x1 = cfg.wall_x - 4
    line = ez2d[x0:x1, cy]
    line = line - line.mean()
    if line.size < 8 or not np.any(line):
        return float("nan")
    spec = np.abs(np.fft.rfft(line * np.hanning(line.size)))
    freqs = np.fft.rfftfreq(line.size, d=1.0)  # cycles per cell
    spec[0] = 0.0
    k = int(np.argmax(spec))
    if freqs[k] <= 0:
        return float("nan")
    return float(1.0 / freqs[k])


def run_field(cfg: FieldConfig | None = None, *, verbose: bool = True) -> FieldResult:
    cfg = cfg or FieldConfig()
    engine = FDTD3DEngine(
        nx=cfg.nx,
        ny=cfg.ny,
        nz=cfg.nz,
        dx=cfg.dx,
        linear_only=True,  # field is far below V_yield: linear Maxwell is exact here
        use_pml=False,  # Mur ABC + perimeter sponge for the z-thin slab
    )
    wall = _build_wall_mask(cfg)
    wall3d = np.repeat(wall[:, :, None], cfg.nz, axis=2)
    sponge = _build_sponge(cfg)[:, :, None]

    z_mid = cfg.nz // 2
    cy = cfg.ny // 2

    intensity_y = np.zeros(cfg.ny)
    intensity2d = np.zeros((cfg.nx, cfg.ny))
    n_record = 0
    # I/Q (phasor) accumulators - coherent amplitude at the carrier frequency.
    qc_y = np.zeros(cfg.ny)
    qs_y = np.zeros(cfg.ny)
    qc2d = np.zeros((cfg.nx, cfg.ny))
    qs2d = np.zeros((cfg.nx, cfg.ny))
    record_end = cfg.record_start + cfg.phasor_window if cfg.phasor else cfg.n_steps
    snapshots: list[np.ndarray] = []
    anim_frames: list[np.ndarray] = []
    anim_steps: list[int] = []
    wavelength_snapshot: np.ndarray | None = None
    z_uniformity = 0.0

    anim_stride = max(1, cfg.n_steps // 90)

    for t in range(cfg.n_steps):
        # --- soft source: z-uniform point launcher ---
        # CW mode: a coherent wave train (the long-flux limit of a stream of
        # identical electron wavepackets) with a smooth turn-on ramp.
        # Pulsed mode: a single Gaussian-enveloped tone burst (one wavepacket).
        if cfg.cw:
            ramp = min(1.0, t / cfg.ramp_steps)
            s = cfg.amplitude * ramp * np.sin(cfg.omega * t)
        else:
            env = np.exp(-(((t - cfg.burst_center) / cfg.burst_tau) ** 2))
            s = cfg.amplitude * env * np.sin(cfg.omega * t)
        for z in range(cfg.nz):
            engine.inject_soft_source("Ez", cfg.x_src, cy, z, s)

        engine.step()

        # --- PEC slit barrier: clamp tangential Ez at wall cells ---
        engine.Ez[wall3d] = 0.0

        # --- perimeter absorbing sponge (boundary aid) ---
        engine.Ex *= sponge
        engine.Ey *= sponge
        engine.Ez *= sponge
        engine.Hx *= sponge
        engine.Hy *= sponge
        engine.Hz *= sponge

        # --- record detector-row intensity (the |psi|^2 landing profile) ---
        if cfg.record_start <= t < record_end:
            ez2d = engine.Ez[:, :, z_mid]
            ez_det = ez2d[cfg.x_det, :]
            if cfg.phasor:
                # Coherent I/Q demodulation at the carrier: |amplitude|^2 isolates
                # the coherent interference pattern from any incoherent floor and
                # avoids the moving-fringe smear of a raw time-integral.
                c, s = np.cos(cfg.omega * t), np.sin(cfg.omega * t)
                qc_y += ez_det * c
                qs_y += ez_det * s
                qc2d += ez2d * c
                qs2d += ez2d * s
            else:
                intensity_y += ez_det**2
                intensity2d += ez2d**2
            n_record += 1

        # --- z-uniformity diagnostic ---
        ez_slab = engine.Ez[cfg.x_det, cy, :]
        denom = np.max(np.abs(engine.Ez[:, :, z_mid])) + 1e-30
        z_uniformity = max(z_uniformity, float(np.std(ez_slab) / denom))

        # --- snapshots for stills ---
        if t in cfg.snapshot_steps:
            snapshots.append(engine.Ez[:, :, z_mid].copy() ** 2)
            if wavelength_snapshot is None:
                wavelength_snapshot = engine.Ez[:, :, z_mid].copy()

        # --- subsampled animation frames ---
        if t % anim_stride == 0:
            anim_frames.append(engine.Ez[:, :, z_mid].copy() ** 2)
            anim_steps.append(t)

        if verbose and t % 200 == 0:
            print(f"  [field] step {t:4d}/{cfg.n_steps}  |Ez|max={np.max(np.abs(engine.Ez)):.3e}")

    if wavelength_snapshot is None:
        wavelength_snapshot = engine.Ez[:, :, z_mid].copy()

    lam_meas = _measure_wavelength(wavelength_snapshot, cfg)
    # Analytic Yee phase speed estimate: c*dt/dx cells/step = 0.80/sqrt(3).
    cells_per_step = (engine.c * engine.dt) / cfg.dx
    lam_analytic = cells_per_step * (2.0 * np.pi / cfg.omega)

    lam_for_pred = lam_meas if np.isfinite(lam_meas) else lam_analytic
    fringe_pred = lam_for_pred * cfg.L / cfg.slit_sep

    if verbose:
        print(
            f"  [field] lambda measured={lam_meas:.2f} cells, analytic={lam_analytic:.2f} cells; "
            f"L={cfg.L}, d={cfg.slit_sep} -> fringe spacing pred={fringe_pred:.2f} cells; "
            f"z-uniformity={z_uniformity:.2e}"
        )

    if cfg.phasor and n_record > 0:
        scale = (2.0 / n_record) ** 2
        intensity_y = (qc_y**2 + qs_y**2) * scale
        intensity2d = (qc2d**2 + qs2d**2) * scale
    elif n_record > 0:
        intensity2d /= n_record

    return FieldResult(
        intensity_y=intensity_y,
        intensity2d=intensity2d,
        snapshots=snapshots,
        snapshot_steps=cfg.snapshot_steps,
        anim_frames=anim_frames,
        anim_steps=anim_steps,
        wall_mask2d=wall,
        slit_centres=cfg.slit_centres,
        x_det=cfg.x_det,
        wavelength_measured=lam_meas,
        wavelength_analytic=lam_analytic,
        fringe_spacing_pred=fringe_pred,
        z_uniformity=z_uniformity,
        cfg=cfg,
    )


if __name__ == "__main__":  # pragma: no cover - manual smoke run
    res = run_field()
    print("intensity_y peak at y =", int(np.argmax(res.intensity_y)))
    print("fringe spacing prediction =", res.fringe_spacing_pred)
