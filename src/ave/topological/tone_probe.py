"""
tone_probe.py — runner-level probe recorder for CosseratField3D.

Records field values at probe sites by wrapping the engine's step() method
and copying the public u / omega / u_dot / omega_dot arrays at chosen alive
sites. The engine itself is NOT modified — this is purely additive runner code.

Default OFF: probe_every=0 means no recording and step() is a thin pass-through.
Default behavior of all existing runs is bit-for-bit unchanged.

WRAP-UNRESOLVED convention (envd_u4_b2.py after PR #1060):
  max |omega| = max over alive sites of sqrt(wx² + wy² + wz²).
  Readouts cannot be trusted once max |omega| > π. Samples beyond π are
  recorded but flagged (wrap_flags array in the saved .npz).

Probe placement (default, based on seeder torus geometry):
  Sheath (outer tube, ρ_t ≈ r_t): 8 probes distributed in toroidal angle φ
    at ψ=0 (outer-equator), ρ_tube = r_t. This is the classically allowed
    region for in-window tones (s_tan ∈ [(ω²−2)/4, ω²/4]; anatomy §3.1).
  Radial rake: probes at ρ_t ∈ {0.5, 1.0, 1.5, 2.0, 3.0}·r_t at φ=0.
  Far-field: 6 probes in ±x/y/z directions from the box centre,
    at distance ≥ max(5, 3·r_t) cells.
  Bulk reference: 2 probes on the opposite side of the box from the knot.
  Sponge monitor: 1 probe just inside the sponge (if pml_thickness > 0).

All probe sites are snapped to the nearest alive site.

Math page reference: Math tone-reader backing page, 2026-10-06, sha1 b0cdef5db22f.
"""

from __future__ import annotations

import json
import platform
import subprocess
from pathlib import Path
from typing import Optional

import numpy as np


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _git_head_sha() -> str:
    """Return the current git HEAD SHA or 'unknown'."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return "unknown"


def _jax_version() -> str:
    try:
        import jax
        return jax.__version__
    except ImportError:
        return "not installed"


def _find_nearest_alive(
    i_all: np.ndarray, j_all: np.ndarray, k_all: np.ndarray,
    tx: float, ty: float, tz: float,
) -> tuple[int, int, int]:
    """Find the alive site (i, j, k) nearest to (tx, ty, tz)."""
    d2 = (i_all - tx) ** 2 + (j_all - ty) ** 2 + (k_all - tz) ** 2
    idx = int(np.argmin(d2))
    return int(i_all[idx]), int(j_all[idx]), int(k_all[idx])


def _default_probe_sites(
    solver,
    R: float,
    r: float,
    n_sheath: int = 8,
) -> list[tuple[int, int, int]]:
    """Compute default probe sites from torus geometry (R, r).

    Args:
        solver:   CosseratField3D instance (for alive site masks and _i/_j/_k).
        R:        major (ring) radius.
        r:        tube radius (sheath at ρ_t ≈ r).
        n_sheath: number of toroidal positions on the outer tube.

    Returns:
        List of (i, j, k) alive site indices.
    """
    mask_alive = solver.mask_alive
    i_all = solver._i[mask_alive].astype(float)
    j_all = solver._j[mask_alive].astype(float)
    k_all = solver._k[mask_alive].astype(float)

    nx, ny, nz = solver.nx, solver.ny, solver.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0

    sites: list[tuple[int, int, int]] = []
    seen: set[tuple[int, int, int]] = set()

    def add(tx, ty, tz):
        site = _find_nearest_alive(i_all, j_all, k_all, tx, ty, tz)
        if site not in seen:
            seen.add(site)
            sites.append(site)

    # --- Sheath shell: ρ_t ≈ r, ψ = 0 (outer equator of the tube)
    # Position: x = cx + (R + r·cos(ψ))·cos(φ), y = cy + (R + r·cos(ψ))·sin(φ), z = cz + r·sin(ψ)
    # At ψ=0: rho_xy = R + r, z = cz
    rho_outer = R + r
    for k in range(n_sheath):
        phi = 2.0 * np.pi * k / n_sheath
        tx = cx + rho_outer * np.cos(phi)
        ty = cy + rho_outer * np.sin(phi)
        add(tx, ty, cz)

    # Also sample top and bottom of tube (ψ = π/2, −π/2) at φ = 0
    add(cx + R, cy, cz + r)   # ψ = π/2
    add(cx + R, cy, cz - r)   # ψ = −π/2

    # --- Radial rake: several ρ_t values at φ = 0
    for frac in (0.5, 1.0, 1.5, 2.0, 3.0):
        rho_t = frac * r
        psi = 0.0
        rho_xy = R + rho_t * np.cos(psi)
        z_t = cz + rho_t * np.sin(psi)
        tx = cx + rho_xy
        add(tx, cy, z_t)

    # --- Far-field probes: 6 directions, at distance ≥ max(5, 3·r) from cx,cy,cz
    ff_dist = max(5.0, 3.0 * r)
    for axis in range(3):
        for sign in (+1, -1):
            p = [cx, cy, cz]
            p[axis] += sign * ff_dist
            # Clamp to grid interior
            p[0] = max(0.5, min(nx - 1.5, p[0]))
            p[1] = max(0.5, min(ny - 1.5, p[1]))
            p[2] = max(0.5, min(nz - 1.5, p[2]))
            add(*p)

    # --- Bulk reference: opposite side of box from knot
    add(nx - 1 - cx, cy, cz)
    add(cx, ny - 1 - cy, cz)

    # --- Sponge monitor: one probe just inside the sponge (if sponge present)
    pml = getattr(solver, "pml_thickness", 0)
    if pml > 0:
        # One cell inside the sponge edge
        sponge_depth = max(1, pml - 1)
        add(sponge_depth, ny // 2, nz // 2)

    return sites


# ---------------------------------------------------------------------------
# ToneProbe class
# ---------------------------------------------------------------------------

class ToneProbe:
    """Runner-level probe recorder; wraps CosseratField3D.step().

    Default OFF (probe_every=0): step() is a pass-through to solver.step()
    with no recording. Existing runs are bit-for-bit unchanged.

    Usage::

        from ave.topological.cosserat_field_3d import CosseratField3D
        from ave.topological.tone_probe import ToneProbe

        solver = CosseratField3D(32, 32, 32)
        solver.initialize_electron_2_3_sector(R_target=8.0, r_target=2.5)
        probe = ToneProbe(solver, R=8.0, r=2.5, probe_every=4)

        for _ in range(n_steps):
            probe.step()   # calls solver.step() and records every 4th step

        probe.save("probes.npz")
    """

    def __init__(
        self,
        solver,
        R: Optional[float] = None,
        r: Optional[float] = None,
        probe_every: int = 0,
        probe_sites: Optional[list[tuple[int, int, int]]] = None,
        n_sheath: int = 8,
        label: str = "",
    ) -> None:
        """
        Args:
            solver:       CosseratField3D instance (not copied; shared reference).
            R:            major (ring) radius for default probe placement.
                          If None and probe_sites is None, uses extract_shell_radii().
            r:            tube radius. Same fallback as R.
            probe_every:  record every this many steps. 0 = disabled (default).
            probe_sites:  explicit list of (i, j, k) alive sites. If None,
                          default placement is used (requires R and r).
            n_sheath:     number of sheath probes around the toroidal circle.
            label:        optional string embedded in metadata.
        """
        self._solver = solver
        self._probe_every = int(probe_every)
        self._label = label
        self._step_count = 0

        if self._probe_every == 0:
            # Disabled: nothing to set up
            self._probe_sites: list[tuple[int, int, int]] = []
            self._R: float = 0.0
            self._r: float = 0.0
            self._n_probes: int = 0
            self._times: list[float] = []
            self._u_data: list[np.ndarray] = []
            self._omega_data: list[np.ndarray] = []
            self._u_dot_data: list[np.ndarray] = []
            self._omega_dot_data: list[np.ndarray] = []
            self._omega_max_data: list[float] = []
            self._wrap_flags: list[bool] = []
            return

        # Resolve probe sites
        if probe_sites is not None:
            self._probe_sites = list(probe_sites)
        else:
            if R is None or r is None:
                R_est, r_est = solver.extract_shell_radii()
                R = R if R is not None else R_est
                r = r if r is not None else r_est
            self._probe_sites = _default_probe_sites(solver, R, r, n_sheath=n_sheath)

        self._R = float(R) if R is not None else 0.0
        self._r = float(r) if r is not None else 0.0
        self._n_probes = len(self._probe_sites)

        # Storage for recorded samples
        self._times: list[float] = []
        self._u_data: list[np.ndarray] = []         # each: (n_probes, 3)
        self._omega_data: list[np.ndarray] = []     # each: (n_probes, 3)
        self._u_dot_data: list[np.ndarray] = []     # each: (n_probes, 3)
        self._omega_dot_data: list[np.ndarray] = [] # each: (n_probes, 3)
        self._omega_max_data: list[float] = []      # max |omega| over all alive sites
        self._wrap_flags: list[bool] = []            # True if omega_max > pi

    # ------------------------------------------------------------------
    # Step wrapper
    # ------------------------------------------------------------------

    def step(self, dt: Optional[float] = None, apply_pml: bool = True) -> None:
        """Call solver.step() and optionally record probe data.

        Args:
            dt:         timestep passed to solver.step(). None → solver.cfl_dt.
            apply_pml:  passed through to solver.step().
        """
        self._solver.step(dt=dt, apply_pml=apply_pml)
        if self._probe_every > 0 and self._step_count % self._probe_every == 0:
            self._record()
        self._step_count += 1

    def _record(self) -> None:
        """Snapshot field values at all probe sites."""
        t = float(self._solver.time)
        u = np.asarray(self._solver.u)
        omega = np.asarray(self._solver.omega)
        u_dot = np.asarray(self._solver.u_dot)
        omega_dot = np.asarray(self._solver.omega_dot)

        n = self._n_probes
        u_snap = np.zeros((n, 3))
        omega_snap = np.zeros((n, 3))
        u_dot_snap = np.zeros((n, 3))
        omega_dot_snap = np.zeros((n, 3))

        for k, (si, sj, sk) in enumerate(self._probe_sites):
            u_snap[k] = u[si, sj, sk]
            omega_snap[k] = omega[si, sj, sk]
            u_dot_snap[k] = u_dot[si, sj, sk]
            omega_dot_snap[k] = omega_dot[si, sj, sk]

        # WRAP-UNRESOLVED: max |omega| = sqrt(wx²+wy²+wz²) per site, then max
        mask = self._solver.mask_alive[..., None]
        omega_mag_sq = np.sum(omega ** 2, axis=-1) * self._solver.mask_alive
        omega_max = float(np.sqrt(np.max(omega_mag_sq)))

        self._times.append(t)
        self._u_data.append(u_snap)
        self._omega_data.append(omega_snap)
        self._u_dot_data.append(u_dot_snap)
        self._omega_dot_data.append(omega_dot_snap)
        self._omega_max_data.append(omega_max)
        self._wrap_flags.append(omega_max > np.pi)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def n_samples(self) -> int:
        """Number of recorded samples so far."""
        return len(self._times)

    @property
    def enabled(self) -> bool:
        return self._probe_every > 0

    @property
    def probe_sites(self) -> list[tuple[int, int, int]]:
        return list(self._probe_sites)

    # ------------------------------------------------------------------
    # Save / load
    # ------------------------------------------------------------------

    def save(self, path: str) -> None:
        """Write probe data to .npz and JSON metadata files.

        Args:
            path: path for the .npz file. Metadata written to path + '.meta.json'.
        """
        p = Path(path)
        n_s = self.n_samples

        if n_s == 0:
            raise RuntimeError("No samples recorded yet; call step() with probe_every > 0 first.")

        times = np.array(self._times)
        # Stack: (n_samples, n_probes, 3)
        u_arr = np.stack(self._u_data, axis=0)
        omega_arr = np.stack(self._omega_data, axis=0)
        u_dot_arr = np.stack(self._u_dot_data, axis=0)
        omega_dot_arr = np.stack(self._omega_dot_data, axis=0)
        omega_max_arr = np.array(self._omega_max_data)
        wrap_flags = np.array(self._wrap_flags, dtype=bool)

        # Tetrahedral neighbor coords for offline strain computation
        # TETRA_OFFSETS = (+1,+1,+1), (+1,−1,−1), (−1,+1,−1), (−1,−1,+1)
        tetra = [(+1,+1,+1), (+1,-1,-1), (-1,+1,-1), (-1,-1,+1)]
        nx, ny, nz = self._solver.nx, self._solver.ny, self._solver.nz
        neighbor_coords = np.zeros((self._n_probes, 4, 3), dtype=int)
        for pi_, (si, sj, sk) in enumerate(self._probe_sites):
            for ti, (di, dj, dk) in enumerate(tetra):
                ni = (si + di) % nx
                nj = (sj + dj) % ny
                nk = (sk + dk) % nz
                neighbor_coords[pi_, ti] = [ni, nj, nk]

        np.savez_compressed(
            str(p),
            times=times,
            u=u_arr,
            omega=omega_arr,
            u_dot=u_dot_arr,
            omega_dot=omega_dot_arr,
            omega_max=omega_max_arr,
            wrap_flags=wrap_flags,
            probe_sites=np.array(self._probe_sites, dtype=int),
            neighbor_coords=neighbor_coords,
        )

        # JSON metadata
        meta = {
            "dt_cfl": float(self._solver.cfl_dt),
            "probe_every": int(self._probe_every),
            "n_samples": int(n_s),
            "n_probes": int(self._n_probes),
            "R": float(self._R),
            "r": float(self._r),
            "label": self._label,
            "probe_sites": [[int(x) for x in s] for s in self._probe_sites],
            "grid": [int(self._solver.nx), int(self._solver.ny), int(self._solver.nz)],
            "dx": float(self._solver.dx),
            "damping_gamma": float(getattr(self._solver, "damping_gamma", 0.0)),
            "pml_thickness": int(getattr(self._solver, "pml_thickness", 0)),
            "k_op10": float(getattr(self._solver, "k_op10", 1.0)),
            "k_hopf": float(getattr(self._solver, "k_hopf", 1.0)),
            "k_refl": float(getattr(self._solver, "k_refl", 1.0)),
            "use_saturation": bool(getattr(self._solver, "use_saturation", True)),
            "omega_yield": float(getattr(self._solver, "omega_yield", float(np.pi))),
            "omega_max_final": float(omega_max_arr[-1]),
            "n_wrap_flags": int(np.sum(wrap_flags)),
            "wrap_caution": (
                "Readouts above π are recorded but flagged as WRAP-UNRESOLVED. "
                "Field readouts cannot be trusted once max |omega| > π. "
                "Convention from envd_u4_b2.py after PR #1060."
            ),
            "git_sha": _git_head_sha(),
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "jax_version": _jax_version(),
            "dtype": str(self._solver.omega.dtype),
        }
        meta_path = str(p) + ".meta.json"
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=2)

    @classmethod
    def load(cls, path: str):
        """Load probe data from a saved .npz file.

        Returns a dict with arrays: times, u, omega, u_dot, omega_dot,
        omega_max, wrap_flags, probe_sites, neighbor_coords.
        """
        data = dict(np.load(str(path) + (".npz" if not path.endswith(".npz") else ""),
                            allow_pickle=False))
        meta_path = path.rstrip(".npz") + ".meta.json"
        if path.endswith(".npz"):
            meta_path = path[:-4] + ".meta.json"
        try:
            with open(meta_path) as f:
                data["meta"] = json.load(f)
        except FileNotFoundError:
            data["meta"] = {}
        return data
