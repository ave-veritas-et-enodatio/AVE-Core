"""
Cosserat-Master-Equation FDTD — Phase 2 coupled engine
=======================================================

Cosserat-coupled extension of MasterEquationFDTD per the Cosserat-Lagrangian
Engine Phase 2 pre-registration at
`research/2026-05-18_cosserat-lagrangian-engine-phase2-prereg.md` and Phase
2b refactor per `research/2026-05-18_phase2-validation-result.md`.

Adds scalar Cosserat microrotation field ω(r,t) alongside scalar V(r,t).
Two coupling modes:

  coupling_mode="forward" (Phase 2a MVP):
    Only V → ω forward coupling via K_eff(V) = K_omega_0/S(V) modulation.
    Does NOT reproduce Op14 bond-pair ρ ≈ -0.99 (test result: ρ = 0.06).

  coupling_mode="shared_flux" (Phase 2b canonical):
    Bidirectional velocity coupling per shared-inductive-flux Lagrangian
    L_coupling = -L_eff(V)·C·λ(V)·V̇·ω̇  (cross-term from
    (1/2)·L_eff(V)·(C·V̇ + λ·ω̇)² shared-flux expansion).

    V equation: V̈ = c_eff²·∇²V + α(V)·ω̇
    ω equation: I_ω·ω̈ = K·∇²ω - 2κω - α(V)·I_ω·V̇

    where α(V) = α_0·(1 - S(V)) so coupling vanishes at low amplitude
    (substrate is linear, V and ω decoupled) and engages at saturation
    (per Op14 leaf §2: "Energy flows from Cosserat into K4-inductive
    when Z_eff rises").

V wave equation (unchanged structure from MasterEquationFDTD):
    ∇²V - μ₀ ε₀ S(V) · ∂²V/∂t² = 0  +  bidirectional coupling term

Op14 forward AND back coupling per the canonical mechanism: bidirectional
shared-inductive-flux trading.

References:
- `manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md` §3.2 (gap closed
  analytically in Phase 1)
- `research/2026-05-18_dark-wake-tau-zx-op14-scaling-derivation.md` (Phase 1
  derivation using Op14 ρ = -0.990 as load-bearing assumption)
- `research/2026-05-18_phase2-validation-result.md` (Phase 2a FAIL diagnosis
  + Phase 2b refactor proposal)
- `manuscript/ave-kb/common/two-engine-architecture-a027.md` (engine
  architecture canonical)
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md`
  (Op14 canonical mechanism: "Cosserat ω field couples via ρ·u̇ + I_ω·ω̇
  kinetic terms that share the bond LC tank's inductive side")
"""

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
        coupling_mode: str = "shared_flux",
        alpha_0: float = 1.0,
    ):
        """
        Args (parent + Cosserat):
            I_omega: Cosserat microinertia (default 1.0)
            K_omega_0: Cosserat rotational stiffness baseline (default 1.0)
            kappa_0: Cosserat-K4 restoring coupling (default 0.1)
            coupling_mode: "forward" (Phase 2a MVP, fails ρ ≈ -0.99) or
                           "shared_flux" (Phase 2b bidirectional, canonical)
            alpha_0: shared-flux coupling strength baseline (default 1.0;
                     scaled by (1 - S(V)) so vanishes at low amplitude)
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
        if coupling_mode not in ("forward", "shared_flux"):
            raise ValueError(f"coupling_mode must be 'forward' or 'shared_flux'; got {coupling_mode!r}")
        self.coupling_mode = coupling_mode
        self.alpha_0 = float(alpha_0)

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
        """K_eff(V) = K_omega_0 / S(V) — Op14 forward modulation of ω-stiffness."""
        S = self.saturation_kernel(V)
        return self.K_omega_0 / np.maximum(S, self.S_min)

    def coupling_strength(self, V):
        """α(V) = α_0·(1 - S(V)) — shared-flux coupling strength.

        Vanishes at low amplitude (S → 1, decoupled); engages at saturation
        (S → 0, full coupling). Per Op14 mechanism: shared inductive flux
        L_eff(V)·(C·V̇ + λ·ω̇) couples V̇ and ω̇ bidirectionally.
        """
        S = self.saturation_kernel(V)
        return self.alpha_0 * (1.0 - S)

    def step(self):
        """One leapfrog timestep of coupled (V, ω) system.

        coupling_mode="forward" (Phase 2a):
          V dynamics: unchanged from MasterEquationFDTD (no ω back-coupling)
          ω dynamics: Cosserat wave equation with V-modulated K_eff(V)

        coupling_mode="shared_flux" (Phase 2b, canonical):
          V dynamics: V̈ = c_eff²·∇²V + α(V)·ω̇
          ω dynamics: I_ω·ω̈ = K_eff·∇²ω - 2κω - α(V)·I_ω·V̇

          Bidirectional velocity coupling: V driven by ω-velocity, ω driven
          by V-velocity. Coupling strength α(V) vanishes at low amplitude
          per Op14 leaf §2 (linear substrate is decoupled).
        """
        # Compute velocities at current half-step from (state - previous)
        # Used in shared_flux coupling terms
        if self.coupling_mode == "shared_flux":
            V_dot = (self.V - self.V_prev) / self.dt
            omega_dot = (self.omega - self.omega_prev) / self.dt
            alpha = self.coupling_strength(self.V)

        # V wave equation
        c_eff_sq = self.c_eff_squared(self.V)
        L_V = self._laplacian(self.V)
        if self.coupling_mode == "shared_flux":
            # V̈ = c_eff²·∇²V + α(V)·ω̇
            V_accel = c_eff_sq * L_V + alpha * omega_dot
        else:
            V_accel = c_eff_sq * L_V
        V_new = 2.0 * self.V - self.V_prev + (self.dt**2) * V_accel
        V_new *= self.damping

        # Cosserat wave equation (V-modulated moduli + restoring force)
        K_eff = self.cosserat_stiffness(self.V)
        L_omega = self._laplacian(self.omega)
        if self.coupling_mode == "shared_flux":
            # I_ω·ω̈ = K_eff·∇²ω - 2κω - α(V)·I_ω·V̇
            # → ω̈ = (K_eff/I_ω)·∇²ω - (2κ/I_ω)·ω - α(V)·V̇
            omega_accel = (
                (K_eff / self.I_omega) * L_omega - (2.0 * self.kappa_0 / self.I_omega) * self.omega - alpha * V_dot
            )
        else:
            omega_accel = (K_eff / self.I_omega) * L_omega - (2.0 * self.kappa_0 / self.I_omega) * self.omega
        omega_new = 2.0 * self.omega - self.omega_prev + (self.dt**2) * omega_accel
        omega_new *= self.damping  # same PML for ω

        # Update state
        self.V_prev = self.V.copy()
        self.V = V_new
        self.omega_prev = self.omega.copy()
        self.omega = omega_new
        self.time += self.dt
        self.step_count += 1

    def H_cosserat(self):
        """H_cos(t) = bare Cosserat energy (independent of V).

        H_cos = (1/2)·I_ω·ω̇² + (1/2)·K_omega_0·|∇ω|² + κ_0·ω²

        Uses K_omega_0 (BARE stiffness), NOT K_eff(V). This makes H_cos a
        function of ω state only, not V state. Required for Pearson
        correlation analysis to be meaningful — otherwise V-modulation of
        K_eff contaminates H_cos with V dependence.
        """
        # Kinetic energy
        omega_dot = (self.omega - self.omega_prev) / self.dt
        KE_omega = 0.5 * self.I_omega * np.sum(omega_dot**2)
        # Potential energy with BARE stiffness
        grad_omega_sq = np.zeros_like(self.omega)
        grad_omega_sq[1:-1, 1:-1, 1:-1] = (
            ((self.omega[2:, 1:-1, 1:-1] - self.omega[:-2, 1:-1, 1:-1]) / (2.0 * self.dx)) ** 2
            + ((self.omega[1:-1, 2:, 1:-1] - self.omega[1:-1, :-2, 1:-1]) / (2.0 * self.dx)) ** 2
            + ((self.omega[1:-1, 1:-1, 2:] - self.omega[1:-1, 1:-1, :-2]) / (2.0 * self.dx)) ** 2
        )
        PE_omega = 0.5 * self.K_omega_0 * np.sum(grad_omega_sq) + self.kappa_0 * np.sum(self.omega**2)
        return float(KE_omega + PE_omega)

    def Sigma_V_sq(self):
        """Σ|V|² — K4-CAPACITIVE energy proxy.

        Per op14-cross-sector-trading.md:15, ρ(H_cos, Σ|V_inc|²) = +1.000 —
        capacitive sector POSITIVELY correlates with H_cos (capacitive lock).
        """
        return float(np.sum(self.V**2))

    def Sigma_Phi_link_sq(self):
        """Σ|Φ_link|² — K4-INDUCTIVE energy proxy.

        Φ_link = L_eff(V)·I where I = C·V̇. So |Φ_link|² = L_eff²·C²·V̇².
        Stripping constants: Σ|Φ_link|² ∝ Σ(V̇²/S(V)) (since L_eff ∝ 1/√S).

        Per op14-cross-sector-trading.md:13, ρ(H_cos, Σ|Φ_link|²) = -0.990 —
        inductive sector ANTI-correlates with Cosserat via Op14 trading.
        """
        V_dot = (self.V - self.V_prev) / self.dt
        S = self.saturation_kernel(self.V)
        return float(np.sum(V_dot**2 / np.maximum(S, self.S_min)))

    def H_total(self):
        """H_total = H_cos + Σ|Φ_link|² (inductive proxy).

        Per Op14: this combination should be approximately conserved during
        Op14 trading (Cosserat ↔ K4-inductive reactive exchange).
        """
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
        """Run n_steps and probe Op14 observables at every probe_every step.

        Returns dict of arrays:
          times: time array
          H_cos: bare Cosserat energy time series
          Sigma_V_sq: K4-CAPACITIVE proxy (should ρ(H_cos)=+1.000 per Op14)
          Sigma_Phi_link_sq: K4-INDUCTIVE proxy (should ρ(H_cos)=-0.990 per Op14)
          H_total: H_cos + Σ|Φ_link|² (approx conserved per Op14)
        """
        times = []
        H_cos_series = []
        Sigma_V_sq_series = []
        Sigma_Phi_link_sq_series = []
        H_total_series = []
        for step_i in range(n_steps):
            self.step()
            if (step_i % probe_every) == 0:
                times.append(self.time)
                H_cos_series.append(self.H_cosserat())
                Sigma_V_sq_series.append(self.Sigma_V_sq())
                Sigma_Phi_link_sq_series.append(self.Sigma_Phi_link_sq())
                H_total_series.append(self.H_total())
        return {
            "times": np.array(times),
            "H_cos": np.array(H_cos_series),
            "Sigma_V_sq": np.array(Sigma_V_sq_series),
            "Sigma_Phi_link_sq": np.array(Sigma_Phi_link_sq_series),
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
