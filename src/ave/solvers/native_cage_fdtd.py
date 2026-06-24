"""Stage-2 NATIVE-CAGE time-domain leapfrog stepper (the §14.1 scaffold).

Prereg : research/2026-06-23_engine-stage2-native-cage_prereg.md
         (RE-FROZEN 2026-06-23, three corrections from rigor gate wg9rsjep8).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (and the load-bearing sign that nearly hid here)
═══════════════════════════════════════════════════════════════════════════════
The native tetrahedral-K4 time-domain leapfrog for the A1 longitudinal scalar V.
It composes the VERIFIED native variable-coefficient operator
    L_native[V] = adjoint_tetrahedral_divergence( D · tetrahedral_gradient(V) )
with D = 1/S(A) the per-site bulk stiffness c_eff²/c0² (graded_vacuum_network:
stiffness_profile :245-252, _native_laplacian_with_stiffness :255-265), driven in
TIME — the new piece (no native leapfrog existed; the production engines
MasterEquationFDTD / CrystalEngine are Cartesian 7-pt).

THE SIGN (CORRECTION 1, the blocker rigor gate wg9rsjep8 caught):
    L_native is POSITIVE-semidefinite (L(const)=0, L(linear)=0, L(r²)=−6 EXACT,
    ⟨u,L_native u⟩=+‖grad u‖²≥0, adjoint ratio +1). So L_native = +gradᵀgrad =
    −(continuum Laplacian). The physical wave eqn ∂²V/∂t² = +c_eff²∇²V with
    ∇²=−L_native gives ∂²V/∂t² = −c0²·L_native[V] (c_eff²/c0²=1/S folded into D),
    so the leapfrog restoring term carries a MINUS:
        V^{n+1} = 2·V^n − V^{n-1} − dt²·c0²·L_native[V^n]      (c0=1)
    PLUS would be anti-restoring → exponential blowup (empirically 1.02→inf in
    ~20 steps); MINUS → bounded.

SINGLE-1/S (CORRECTION 2, code-enforced):
    D = 1/S(A) is folded into L_native ONCE (inside _native_laplacian_with_
    stiffness). This stepper does NOT additionally multiply by c_eff²/(1/S).
    Copying the Cartesian step() (which DOES multiply by c_eff_squared,
    master_equation_fdtd.py:202-204) would apply 1/S twice = 1/S_min²=1e6.

CFL (CORRECTION 3, measured-ρ):
    dt = cfl_safety · 2/√(ρ_measured·c0²), ρ_measured by power-iteration on the
    assembled SATURATED native operator. Cartesian √3 is a lower-bound sanity
    cross-check only.

α-CLEAN: pure (1−A²) kernel; NO ALPHA / Q_TANK / ELECTRON / RHO_BULK import; κ̃
out of scope (scalar cage, no winding). Same guard triad as
graded_vacuum_network.py:111-114.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.solvers.graded_vacuum_network import (
    _native_laplacian_with_stiffness,
    saturation_kernel,
    stiffness_profile,
)

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time, same as graded_vacuum_network.py:111-114).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: bare RHO_BULK magnitude must NOT be imported"


@dataclass(frozen=True)
class NativeCageConfig:
    """Frozen Stage-2 native-cage run config (α-free; v14 Mode-I defaults).

    N            : cube edge (lattice sites per side); 24 = v14 canonical.
    dx           : lattice pitch (0.5 = v14).
    c0           : reference speed (1.0; c_eff²/c0²=1/S folds into D).
    V_yield      : yield amplitude (1.0; A = |V|/V_yield).
    cfl_safety   : leapfrog safety factor (0.4 = v14).
    pml_thickness: absorbing sponge thickness (4 = v14).
    exponent     : Op14 saturation exponent (0.5 √S primary, 0.25 sensitivity).
    S_min        : saturation floor (1e-3; stiffness ceiling 1/S_min=1e3).
    A_cap        : strain clip (0.999; avoids the S=0 singularity).
    sign         : restoring sign of L_native (-1.0 = the CORRECT MINUS;
                   +1.0 ONLY for the deliberate negative-control blowup test).
    """

    N: int = 24
    dx: float = 0.5
    c0: float = 1.0
    V_yield: float = 1.0
    cfl_safety: float = 0.4
    pml_thickness: int = 4
    exponent: float = 0.5
    S_min: float = 1e-3
    A_cap: float = 0.999
    sign: float = -1.0


def _strain(V: np.ndarray, V_yield: float, A_cap: float) -> np.ndarray:
    """A = |V|/V_yield, clipped to A_cap (avoids the S=0 singularity)."""
    return np.minimum(np.abs(V) / V_yield, A_cap)


def power_iteration_rho(
    D: np.ndarray, *, c0: float = 1.0, n_iter: int = 200, seed: int = 0
) -> float:
    """Spectral radius ρ(c0²·L_native) by power-iteration on the assembled
    SATURATED native operator (CORRECTION 3). D is the per-site stiffness field
    1/S(A); ρ scales as ρ_cold/S_min in the saturated core.

    L_native is symmetric PSD, so the dominant eigenvalue is the spectral radius.
    Returns the Rayleigh-quotient estimate λ_max of (c0²·L_native).
    """
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(D.shape)
    x /= np.linalg.norm(x)
    lam = 0.0
    for _ in range(n_iter):
        # c0²·L_native[x] = c0² · adjoint_div(D·grad(x)); L_native is PSD.
        y = (c0**2) * _native_laplacian_with_stiffness(x, D)
        lam = float(np.vdot(x, y).real)  # Rayleigh quotient (x is unit-norm)
        ny = np.linalg.norm(y)
        if ny == 0.0:
            return 0.0
        x = y / ny
    # Final Rayleigh quotient on the converged vector.
    y = (c0**2) * _native_laplacian_with_stiffness(x, D)
    return float(np.vdot(x, y).real)


class NativeCageFDTD:
    """Native tetrahedral-K4 time-domain leapfrog for the A1 scalar V-sector.

    The §14.1 scaffold. Same leapfrog STRUCTURE as MasterEquationFDTD but:
      (1) native L_native (PSD) swapped for the Cartesian 7-pt _laplacian (NSD),
      (2) the restoring sign is MINUS (cfg.sign=-1) NOT plus (CORRECTION 1),
      (3) D=1/S folded into L_native ONCE; no extra c_eff² multiply (CORRECTION 2),
      (4) dt by measured-ρ on the SATURATED operator (CORRECTION 3).
    """

    def __init__(self, cfg: NativeCageConfig):
        self.cfg = cfg
        N = cfg.N
        self.N = N
        self.dx = cfg.dx
        self.c0 = cfg.c0
        self.V_yield = cfg.V_yield
        self.pml_thickness = cfg.pml_thickness
        self.exponent = cfg.exponent
        self.S_min = cfg.S_min
        self.A_cap = cfg.A_cap
        self.sign = cfg.sign

        self.V = np.zeros((N, N, N), dtype=np.float64)
        self.V_prev = np.zeros((N, N, N), dtype=np.float64)

        self._build_damping_mask()
        self._build_interior_mask()

        self.time = 0.0
        self.step_count = 0
        # dt is set by set_dt_from_seed() once the seed is planted (measured-ρ).
        self.dt = 0.0
        self.rho_measured = None
        self.dt_cartesian_sanity = None

    # ── PML sponge (verbatim structure from master_equation_fdtd:107-120) ──
    def _build_damping_mask(self):
        N = self.N
        i, j, k = np.indices((N, N, N))
        d = np.minimum.reduce([
            np.minimum(i, N - 1 - i),
            np.minimum(j, N - 1 - j),
            np.minimum(k, N - 1 - k),
        ])
        damping = np.ones((N, N, N), dtype=np.float64)
        t = self.pml_thickness
        if t > 0:
            in_pml = d < t
            atten = 1.0 - 0.05 * ((t - d[in_pml]) / t) ** 2
            damping[in_pml] = np.maximum(0.5, atten)
        self.damping = damping

    def _build_interior_mask(self):
        """Interior mask: pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1
        (A-Rule 10 PML-exclusion). All field observables read THIS region only."""
        N, t = self.N, self.pml_thickness
        mask = np.zeros((N, N, N), dtype=bool)
        mask[t:N - t, t:N - t, t:N - t] = True
        self.interior = mask

    # ── kernel readouts (α-free; D=1/S folded once) ──
    def strain(self) -> np.ndarray:
        return _strain(self.V, self.V_yield, self.A_cap)

    def saturation_S(self) -> np.ndarray:
        return saturation_kernel(self.strain(), exponent=self.exponent, S_min=self.S_min)

    def stiffness_D(self) -> np.ndarray:
        """D = c_eff²/c0² = 1/S(A). The ONLY place 1/S enters (CORRECTION 2)."""
        return stiffness_profile(self.strain(), exponent=self.exponent, S_min=self.S_min)

    def n_em_index(self) -> np.ndarray:
        """EM-transverse group index n_EM = √S (→0 as A→1). Saturation gauge."""
        return self.saturation_S() ** 0.5

    def gamma_bulk_min(self) -> dict:
        """μ-load Smith-Γ on the bulk branch, interior-masked (diagnostic, §8b).
        Z_eff = √S → 0 short ⇒ Γ=(Z_eff−1)/(Z_eff+1) → −1 (crystal_engine.
        gamma_bulk:460-491). Pure function of S — α-free, anti-self-validation."""
        Z_eff = self.saturation_S() ** 0.5
        gamma = (Z_eff - 1.0) / (Z_eff + 1.0)
        gi = gamma[self.interior]
        return {
            "gamma_min": float(gi.min()),
            "gamma_mean": float(gi.mean()),
            "frac_short": float((gi < -0.5).mean()),
        }

    # ── seed + CFL ──
    def seed_sech(self, *, amplitude: float, radius: float):
        """v14 Mode-I sech seed (byte-identical to test_master_equation_v14_
        mode_i.py:57-64). At-rest (V_prev = V; ∂_tV=0)."""
        N, dx = self.N, self.dx
        center = N // 2
        coords = np.arange(N) - center
        X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
        r = np.sqrt(X**2 + Y**2 + Z**2) * dx
        seed = amplitude * (1.0 / np.cosh(r / radius))
        self.V[:] = seed
        self.V_prev[:] = seed.copy()

    def seed_field(self, V_seed: np.ndarray):
        """Plant an arbitrary at-rest seed (∂_tV=0)."""
        self.V[:] = V_seed
        self.V_prev[:] = np.asarray(V_seed).copy()

    def set_dt_from_seed(self, *, n_iter: int = 200) -> dict:
        """CORRECTION 3: freeze dt = cfl_safety·2/√(ρ_measured·c0²), ρ measured by
        power-iteration on the SATURATED operator (the current V seed → D=1/S).
        Records the Cartesian √3 heuristic dt as a lower-bound sanity only."""
        D = self.stiffness_D()  # saturated operator on the planted seed
        rho = power_iteration_rho(D, c0=self.c0, n_iter=n_iter)
        self.rho_measured = rho
        self.dt = self.cfg.cfl_safety * 2.0 / np.sqrt(max(rho, 1e-30))
        # Cartesian √3 heuristic (lower-bound sanity only; ~7× over-conservative).
        c_eff_max = self.c0 / np.sqrt(self.S_min)
        self.dt_cartesian_sanity = self.cfg.cfl_safety * self.dx / (c_eff_max * np.sqrt(3.0))
        return {
            "rho_measured": rho,
            "dt": self.dt,
            "dt_cartesian_sanity": self.dt_cartesian_sanity,
            "dt_le_cartesian_sanity": self.dt <= self.dt_cartesian_sanity,
        }

    # ── the leapfrog step (CORRECTION 1: MINUS; CORRECTION 2: single 1/S) ──
    def step(self):
        """One native leapfrog step:
            V^{n+1} = 2·V^n − V^{n-1} + sign·dt²·c0²·L_native[V^n]
        with sign = −1 (CORRECT MINUS). D=1/S folded into L_native (single 1/S).
        NO extra c_eff² multiply. PML sponge applied to V_new."""
        if self.dt == 0.0:
            raise RuntimeError("dt not set — call set_dt_from_seed() after seeding.")
        D = self.stiffness_D()  # 1/S(A) — the ONLY 1/S application
        L = _native_laplacian_with_stiffness(self.V, D)  # = adjoint_div(D·grad V)
        V_new = (
            2.0 * self.V
            - self.V_prev
            + self.sign * (self.dt**2) * (self.c0**2) * L
        )
        V_new *= self.damping
        self.V_prev = self.V.copy()
        self.V = V_new
        self.time += self.dt
        self.step_count += 1

    # ── observables (interior-only, PML-excluded; A-Rule 10) ──
    def interior_peak_abs_V(self) -> float:
        """Mean-time observable building block: peak |V| over the PML-excluded
        interior (NOT centroid — §7.1, centroid of a shell is the empty middle)."""
        return float(np.abs(self.V[self.interior]).max())

    def interior_energy(self) -> float:
        """Σ|V|² over the PML-excluded interior."""
        return float(np.sum(self.V[self.interior] ** 2))

    def run_record(self, n_total: int, n_transient: int) -> dict:
        """Run n_total steps; record the reactance PAIR every step over the full
        window (A-Rule 10: C-state |V| AND L-state |∂_tV|), and the post-
        transient persistence/breathing/Γ stats."""
        v_peak_hist, dvdt_peak_hist, energy_hist = [], [], []
        gamma_min_hist, n_em_min_hist, max_abs_hist = [], [], []
        for n in range(n_total):
            V_before = self.V.copy()
            self.step()
            # C-state: |V|; L-state: |∂_tV| ≈ |V−V_before|/dt (DC-free breathing).
            dvdt = (self.V - V_before) / self.dt
            v_peak_hist.append(self.interior_peak_abs_V())
            dvdt_peak_hist.append(float(np.abs(dvdt[self.interior]).max()))
            energy_hist.append(self.interior_energy())
            gamma_min_hist.append(self.gamma_bulk_min()["gamma_min"])
            n_em_min_hist.append(float(self.n_em_index()[self.interior].min()))
            max_abs_hist.append(float(np.abs(self.V).max()))
        v_peak = np.array(v_peak_hist)
        post = v_peak[n_transient:]
        mean_post = float(post.mean()) if post.size else float("nan")
        std_post = float(post.std()) if post.size else float("nan")
        return {
            "v_peak_hist": v_peak,
            "dvdt_peak_hist": np.array(dvdt_peak_hist),
            "energy_hist": np.array(energy_hist),
            "gamma_min_hist": np.array(gamma_min_hist),
            "n_em_min_hist": np.array(n_em_min_hist),
            "max_abs_hist": np.array(max_abs_hist),
            "v_peak_mean_post": mean_post,
            "v_peak_std_post": std_post,
            "v_peak_std_over_mean_post": std_post / max(mean_post, 1e-9),
            "n_em_min_over_window": float(np.array(n_em_min_hist).min()),
            "gamma_bulk_min_over_run": float(np.array(gamma_min_hist).min()),
            "max_abs_over_run": float(np.array(max_abs_hist).max()),
            "rho_measured": self.rho_measured,
            "dt": self.dt,
        }
