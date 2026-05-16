"""
Master Equation FDTD — direct numerical integration of eq:master_wave
======================================================================

Implements the canonical AVE Master Equation per
`AVE-Core/manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:46-77`:

    ∇²V - μ₀ ε₀ √(1 - (V/V_yield)²) · ∂²V/∂t² = 0

Equivalently:
    ∂²V/∂t² = (c₀²/S(A)) · ∇²V,   A = V/V_yield,  S(A) = √(1-A²)

with c_eff(V) = c₀ · (1 - A²)^(-1/4) → ∞ as A → 1.

Why this engine exists (per doc 111 §3): the K4-TLM engine implements
Z(V) modulation but NOT c_eff(V) modulation. The Master Equation requires
both. Without c_eff(V), the wave cannot self-trap at A → 1, which is why
v14a-e all returned Mode III on the K4-TLM engine. This FDTD engine
realizes the full Master Equation directly.

Three operating regimes (per Vol 1 Ch 4:138-159):
  I.   Linear Acoustic (A ≪ 1):    S ≈ 1, c_eff ≈ c₀ — standard Maxwell
  II.  Non-Linear Tensor (A → 1): S → 0, c_eff → ∞ — bound state forms
  III. Dielectric Rupture (A ≥ 1): substrate phase-transitions (clipped here)

A-034 (canonical 2026-05-15 evening): the S(A) = √(1−A²) kernel here IS
the universal A-034 mechanism — same kernel that governs 19 catalog
instances across 21 orders of magnitude (atomic pair creation, BCS 0.00%
error, BH ring-down 1.7% from GR, NOAA-validated solar flares, cosmic K4
crystallization). The vertical tangent at A=1 is what makes Regime III
rupture impulsive at every scale. See: research/L5/A-034;
backmatter/07_universal_saturation_kernel.tex.

The engine numerically caps A < A_cap (default 0.99) to stay in Regime II
and avoid Regime III where the substrate phase-transitions (out of scope
for FDTD on the scalar Master Equation).
"""

from __future__ import annotations

import numpy as np


class MasterEquationFDTD:
    """
    3D leapfrog FDTD for the scalar AVE Master Equation.

    State variables:
      V (nx, ny, nz)     — scalar substrate potential
      V_prev (nx, ny, nz) — V at the previous timestep (for 2nd-order
                            time discretization)

    Per-cell c_eff² = c₀² / S(|V|/V_yield), where S(A) = √(1-A²) clipped
    to S > S_min to avoid CFL blow-up in Regime II.

    Update rule (leapfrog):
      V^(n+1) = 2·V^n - V^(n-1) + dt² · c_eff²(V^n) · ∇²V^n

    With absorbing PML at the lattice boundary (sponge-layer attenuation).
    """

    def __init__(
        self,
        N: int,
        dx: float = 1.0,
        V_yield: float = 1.0,
        c0: float = 1.0,
        cfl_safety: float = 0.4,
        pml_thickness: int = 4,
        A_cap: float = 0.99,
        S_min: float = 0.05,
    ):
        """
        Args:
            N: lattice side length (3D cube N×N×N)
            dx: spatial step (natural units; default 1.0)
            V_yield: saturation field per node (natural units; default 1.0)
            c0: linear wave speed (natural units; default 1.0)
            cfl_safety: fraction of CFL limit to use (default 0.4 for margin)
            pml_thickness: PML layer thickness in cells (default 4)
            A_cap: max allowed strain (numerical stability cap; default 0.99
                   to stay in Regime II)
            S_min: floor on S(A) to bound c_eff² (default 0.05 → c_eff² ≤ 20·c₀²)
        """
        self.N = N
        self.dx = float(dx)
        self.V_yield = float(V_yield)
        self.c0 = float(c0)
        self.A_cap = float(A_cap)
        self.S_min = float(S_min)

        # CFL: for 3D wave equation ∂²V/∂t² = c²∇²V on N³ grid with
        # 7-point Laplacian, stability requires dt ≤ dx/(c·√3).
        # With c_eff_max ~ c₀/√S_min, we need additional safety.
        c_eff_max = self.c0 / np.sqrt(self.S_min)
        self.dt = cfl_safety * self.dx / (c_eff_max * np.sqrt(3.0))

        # State arrays
        self.V = np.zeros((N, N, N), dtype=np.float64)
        self.V_prev = np.zeros((N, N, N), dtype=np.float64)

        # PML damping (sponge layer)
        self.pml_thickness = pml_thickness
        self._build_damping_mask()

        self.time = 0.0
        self.step_count = 0

    def _build_damping_mask(self):
        """Quadratic damping factor that attenuates V in the PML region."""
        i, j, k = np.indices((self.N, self.N, self.N))
        d_x = np.minimum(i, self.N - 1 - i)
        d_y = np.minimum(j, self.N - 1 - j)
        d_z = np.minimum(k, self.N - 1 - k)
        d = np.minimum(np.minimum(d_x, d_y), d_z)
        damping = np.ones((self.N, self.N, self.N), dtype=np.float64)
        if self.pml_thickness > 0:
            in_pml = d < self.pml_thickness
            # Quadratic attenuation: 1.0 at interior, 0.7-ish at outermost
            attenuation = 1.0 - 0.05 * ((self.pml_thickness - d[in_pml]) / self.pml_thickness) ** 2
            damping[in_pml] = np.maximum(0.5, attenuation)
        self.damping = damping

    def _laplacian(self, V):
        """7-point 2nd-order central-difference Laplacian.

        Interior: ∇²V_{i,j,k} = (V_{i+1} + V_{i-1} + V_{j+1} + V_{j-1}
                                 + V_{k+1} + V_{k-1} - 6V_{i,j,k}) / dx²
        Boundary cells: zero (handled by damping mask).
        """
        L = np.zeros_like(V)
        L[1:-1, 1:-1, 1:-1] = (
            V[2:, 1:-1, 1:-1]
            + V[:-2, 1:-1, 1:-1]
            + V[1:-1, 2:, 1:-1]
            + V[1:-1, :-2, 1:-1]
            + V[1:-1, 1:-1, 2:]
            + V[1:-1, 1:-1, :-2]
            - 6 * V[1:-1, 1:-1, 1:-1]
        ) / (self.dx**2)
        return L

    def saturation_kernel(self, V):
        """S(A) = √(1 - A²) with A = |V|/V_yield, clipped to [S_min, 1]."""
        A = np.abs(V) / self.V_yield
        A_clipped = np.minimum(A, self.A_cap)
        S = np.sqrt(np.maximum(1.0 - A_clipped**2, self.S_min**2))
        return S

    def c_eff_squared(self, V):
        """c_eff²(V) = c₀² / S(V/V_yield) per Master Equation."""
        S = self.saturation_kernel(V)
        return (self.c0**2) / np.maximum(S, self.S_min)

    def strain_field(self):
        """Local strain A = |V|/V_yield at each cell."""
        return np.abs(self.V) / self.V_yield

    def refractive_index(self):
        """n(r) = c₀/c_eff(V) = S(A)^(1/4) → 0 as A → 1.

        This is the substrate-native refractive index from the Master
        Equation. In standard physics, this is the gravity-flavored
        refractive-index gradient n(r) = 1 + 2GM/(rc²).
        """
        S = self.saturation_kernel(self.V)
        return S**0.25

    def step(self):
        """One leapfrog timestep of the Master Equation."""
        c_eff_sq = self.c_eff_squared(self.V)
        L = self._laplacian(self.V)
        V_new = 2.0 * self.V - self.V_prev + (self.dt**2) * c_eff_sq * L
        # Apply PML damping
        V_new *= self.damping
        # Update state
        self.V_prev = self.V.copy()
        self.V = V_new
        self.time += self.dt
        self.step_count += 1

    def run(self, n_steps: int, source_fn=None, source_pos=None, probe_pos=None, source_mode="hard"):
        """
        Run n_steps; optionally inject a source and probe a location.

        source_fn: callable(t) → amplitude to inject at source_pos each step
        source_pos: (i, j, k) tuple for source injection
        probe_pos: (i, j, k) tuple to record V at each step (or None)
        source_mode: "hard" (replace V at source) or "soft" (add dt·source)

        Hard source is the correct mode for clean spectral analysis (no DC drift).
        Soft source is appropriate for current-density-like injection.
        """
        probe_data = [] if probe_pos is not None else None
        for _ in range(n_steps):
            if source_fn is not None and source_pos is not None:
                if source_mode == "hard":
                    self.V[source_pos] = source_fn(self.time)
                else:
                    self.V[source_pos] += self.dt * source_fn(self.time)
            self.step()
            if probe_pos is not None:
                probe_data.append(float(self.V[probe_pos]))
        return np.array(probe_data) if probe_data is not None else None

    def total_energy(self):
        """Crude energy proxy: ∫(V² + ε_eff²) dV.

        At linear regime, this ~ field intensity. At saturation, V dominates.
        """
        return float(np.sum(self.V**2))

    def inject_gaussian(self, center, sigma, amplitude):
        """Plant a Gaussian V profile at center with width sigma."""
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r_sq = (i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2
        self.V += amplitude * np.exp(-r_sq / (2.0 * sigma**2))
        # Set V_prev = V to give zero initial time derivative
        # (stationary initial state)
        self.V_prev = self.V.copy()

    def inject_localized_blob(self, center, radius, amplitude, profile="sech"):
        """Plant a localized blob at center with radius scale.

        profile:
          'sech'    : V(r) = amplitude · sech(r/radius)  (typical soliton shape)
          'gaussian': V(r) = amplitude · exp(-r²/(2·radius²))
          'lorentzian': V(r) = amplitude / (1 + (r/radius)²)
        """
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
        if profile == "sech":
            self.V += amplitude / np.cosh(r / radius)
        elif profile == "gaussian":
            self.V += amplitude * np.exp(-(r**2) / (2.0 * radius**2))
        elif profile == "lorentzian":
            self.V += amplitude / (1.0 + (r / radius) ** 2)
        else:
            raise ValueError(f"Unknown profile: {profile}")
        self.V_prev = self.V.copy()

    def __repr__(self):
        c_eff_max = self.c0 / np.sqrt(self.S_min)
        return (
            f"MasterEquationFDTD(N={self.N}, dx={self.dx}, V_yield={self.V_yield}, "
            f"c0={self.c0}, dt={self.dt:.4e}, "
            f"c_eff_max={c_eff_max:.2f}, A_cap={self.A_cap}, "
            f"step={self.step_count}, t={self.time:.4e})"
        )
