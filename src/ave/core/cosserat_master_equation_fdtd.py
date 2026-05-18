"""
Cosserat-Master-Equation FDTD — Phase 2 coupled engine
=======================================================

Minimum-viable Cosserat-coupled extension of MasterEquationFDTD per the
Cosserat-Lagrangian Engine Phase 2 pre-registration at
`research/2026-05-18_cosserat-lagrangian-engine-phase2-prereg.md`.

Adds scalar Cosserat microrotation field ω(r,t) alongside scalar V(r,t).
Couples ω-wave-equation moduli to V via Op14 mechanism: K_ω(V) = K_ω₀/S(V)
where S(V) = sqrt(1-(V/V_yield)²) is the Axiom 4 saturation kernel.

As V drives S → 0 (saturation), Cosserat moduli K_ω/S(V) → ∞, freezing ω
locally. This is the substrate-native back-EMF mechanism that should
reproduce the Op14 bond-pair Pearson ρ(H_cos, Σ|Φ_link|²) = -0.990
signature per `ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/
op14-cross-sector-trading.md:7` (A-012 canonical).

Cosserat wave equation (simplified Eringen micropolar, 1-component):
    I_ω · ∂²ω/∂t² = (K_ω₀/S(V)) ∇²ω - 2 κ₀ ω

V wave equation (unchanged from MasterEquationFDTD):
    ∇²V - μ₀ ε₀ S(V) · ∂²V/∂t² = 0

Op14 coupling: forward V → ω only (K_ω moduli modulated by V via S(V)).
Back-coupling ω → V deferred to Phase 2b per pre-reg scope.

References:
- `manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md` §3.2 (gap closed
  analytically in Phase 1)
- `research/2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md` (Phase 1
  derivation using Op14 ρ = -0.990 as load-bearing assumption)
- `manuscript/ave-kb/common/two-engine-architecture-a027.md` (engine
  architecture canonical)
"""

from __future__ import annotations

import numpy as np

from ave.core.master_equation_fdtd import MasterEquationFDTD


class CosseratMasterEquationFDTD(MasterEquationFDTD):
    """
    Cosserat-coupled extension of MasterEquationFDTD.

    Adds ω(r,t) scalar Cosserat microrotation field with Op14 coupling
    to V dynamics via S(V) = sqrt(1-(V/V_yield)²) modulating ω-moduli.

    State variables (in addition to V, V_prev from parent):
      omega (N, N, N)      — scalar Cosserat microrotation field
      omega_prev (N, N, N) — ω at previous timestep

    Cosserat parameters:
      I_omega: microinertia (natural units; default 1.0)
      K_omega_0: baseline Cosserat rotational stiffness (default 1.0)
      kappa_0: Cosserat-K4 restoring coupling (default 0.1, sub-dominant
               to avoid swamping wave behavior)

    Update rule (leapfrog, same scheme as V):
      ω^(n+1) = 2·ω^n - ω^(n-1) + dt² · (K_eff(V)/I_ω · ∇²ω^n - 2 κ_0/I_ω · ω^n)
      where K_eff(V) = K_omega_0 / S(V), clipped at S_min for stability.
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
        I_omega: float = 1.0,
        K_omega_0: float = 1.0,
        kappa_0: float = 0.1,
    ):
        """
        Args (parent + Cosserat):
            I_omega: Cosserat microinertia (default 1.0)
            K_omega_0: Cosserat rotational stiffness baseline (default 1.0)
            kappa_0: Cosserat-K4 restoring coupling (default 0.1)
        See MasterEquationFDTD for inherited args.
        """
        super().__init__(
            N=N,
            dx=dx,
            V_yield=V_yield,
            c0=c0,
            cfl_safety=cfl_safety,
            pml_thickness=pml_thickness,
            A_cap=A_cap,
            S_min=S_min,
        )

        self.I_omega = float(I_omega)
        self.K_omega_0 = float(K_omega_0)
        self.kappa_0 = float(kappa_0)

        # Cosserat state arrays
        self.omega = np.zeros((N, N, N), dtype=np.float64)
        self.omega_prev = np.zeros((N, N, N), dtype=np.float64)

        # Re-tighten dt for Cosserat CFL: cosserat c²_eff,max = K_omega_0 / (I_omega · S_min)
        # If this is more restrictive than V CFL, use the tighter dt.
        c_omega_max = np.sqrt(self.K_omega_0 / (self.I_omega * self.S_min))
        dt_omega = cfl_safety * self.dx / (c_omega_max * np.sqrt(3.0))
        if dt_omega < self.dt:
            self.dt = dt_omega

    def cosserat_stiffness(self, V):
        """K_eff(V) = K_omega_0 / S(V) — Op14 forward coupling."""
        S = self.saturation_kernel(V)
        return self.K_omega_0 / np.maximum(S, self.S_min)

    def step(self):
        """One leapfrog timestep of coupled (V, ω) system.

        V dynamics: unchanged from MasterEquationFDTD (no ω back-coupling
        in MVP per Phase 2 pre-reg scope).
        ω dynamics: Cosserat wave equation with V-modulated K_eff.
        """
        # V wave equation (parent's leapfrog)
        c_eff_sq = self.c_eff_squared(self.V)
        L_V = self._laplacian(self.V)
        V_new = 2.0 * self.V - self.V_prev + (self.dt**2) * c_eff_sq * L_V
        V_new *= self.damping

        # Cosserat wave equation (V-modulated moduli + restoring force)
        K_eff = self.cosserat_stiffness(self.V)
        L_omega = self._laplacian(self.omega)
        omega_new = (
            2.0 * self.omega
            - self.omega_prev
            + (self.dt**2) * (
                (K_eff / self.I_omega) * L_omega
                - (2.0 * self.kappa_0 / self.I_omega) * self.omega
            )
        )
        omega_new *= self.damping  # same PML for ω

        # Update state
        self.V_prev = self.V.copy()
        self.V = V_new
        self.omega_prev = self.omega.copy()
        self.omega = omega_new
        self.time += self.dt
        self.step_count += 1

    def H_cosserat(self):
        """H_cos(t) = (1/2) · I_ω · ω² + (1/2) · K_eff(V) · |∇ω|² (per node, summed).

        Total Cosserat energy. Should anti-correlate with Σ|Φ_link|² ∝ Σ|V|²
        per Op14 ρ = -0.990.
        """
        # Kinetic energy: ω velocity = (ω - ω_prev)/dt, KE = (1/2)·I_ω·ω̇²
        omega_dot = (self.omega - self.omega_prev) / self.dt
        KE_omega = 0.5 * self.I_omega * np.sum(omega_dot**2)
        # Potential energy: (1/2)·K_eff(V)·|∇ω|² + (1/2)·2·κ_0·ω²
        # ∇ω via central difference (interior cells)
        grad_omega_sq = np.zeros_like(self.omega)
        grad_omega_sq[1:-1, 1:-1, 1:-1] = (
            ((self.omega[2:, 1:-1, 1:-1] - self.omega[:-2, 1:-1, 1:-1]) / (2.0 * self.dx)) ** 2
            + ((self.omega[1:-1, 2:, 1:-1] - self.omega[1:-1, :-2, 1:-1]) / (2.0 * self.dx)) ** 2
            + ((self.omega[1:-1, 1:-1, 2:] - self.omega[1:-1, 1:-1, :-2]) / (2.0 * self.dx)) ** 2
        )
        K_eff = self.cosserat_stiffness(self.V)
        PE_omega = 0.5 * np.sum(K_eff * grad_omega_sq) + self.kappa_0 * np.sum(self.omega**2)
        return float(KE_omega + PE_omega)

    def Sigma_Phi_link_sq(self):
        """Σ|Φ_link|² proxy via Σ|V|² (V is the K4-inductive-side observable).

        Per op14-cross-sector-trading.md:14, ρ(Σ|V_inc|², Σ|Φ_link|²) = -0.990
        also holds, so Σ|V|² is a valid proxy for Σ|Φ_link|².
        """
        return float(np.sum(self.V**2))

    def H_total(self):
        """H_total = H_cos + H_K4_inductive (approximately conserved per Op14)."""
        return self.H_cosserat() + self.Sigma_Phi_link_sq()

    def inject_cosserat_blob(self, center, radius, amplitude, profile="sech"):
        """Plant an ω blob at center (analogous to inject_localized_blob for V)."""
        cx, cy, cz = center
        i, j, k = np.indices((self.N, self.N, self.N))
        r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
        if profile == "sech":
            self.omega += amplitude / np.cosh(r / radius)
        elif profile == "gaussian":
            self.omega += amplitude * np.exp(-(r**2) / (2.0 * radius**2))
        else:
            raise ValueError(f"Unknown profile: {profile}")
        self.omega_prev = self.omega.copy()

    def run_with_probes(self, n_steps: int, probe_every: int = 1):
        """Run n_steps and probe (H_cos, Σ|V|², H_total) at every probe_every step.

        Returns dict of arrays for time-series analysis (Pearson correlation,
        FFT for trading frequency, etc.).
        """
        times = []
        H_cos_series = []
        Sigma_V_sq_series = []
        H_total_series = []
        for step_i in range(n_steps):
            self.step()
            if (step_i % probe_every) == 0:
                times.append(self.time)
                H_cos_series.append(self.H_cosserat())
                Sigma_V_sq_series.append(self.Sigma_Phi_link_sq())
                H_total_series.append(self.H_total())
        return {
            "times": np.array(times),
            "H_cos": np.array(H_cos_series),
            "Sigma_Phi_link_sq": np.array(Sigma_V_sq_series),
            "H_total": np.array(H_total_series),
        }

    def __repr__(self):
        return (
            f"CosseratMasterEquationFDTD(N={self.N}, dx={self.dx}, "
            f"V_yield={self.V_yield}, c0={self.c0}, dt={self.dt:.4e}, "
            f"I_omega={self.I_omega}, K_omega_0={self.K_omega_0}, "
            f"kappa_0={self.kappa_0}, "
            f"step={self.step_count}, t={self.time:.4e})"
        )
