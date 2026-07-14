"""Stage-2 NATIVE-CAGE IMEX (implicit-stiff) time-domain stepper.

Prereg : research/2026-06-23_engine-stage2-native-cage_prereg.md (RE-FROZEN).
Companion explicit stepper : ave/solvers/native_cage_fdtd.py (G1-G8 validated).
  HISTORICAL NOTE (2026-07-13): the explicit companion `native_cage_fdtd.py` was
  built and G1-G8-validated on the Stage-2 branch (git commit 050f1088) but was
  NEVER LANDED to main — it is ABSENT from the repo at HEAD. Every reference to
  `native_cage_fdtd.py` in this module is a historical / git-provenance pointer
  (`git show 050f1088:src/ave/solvers/native_cage_fdtd.py`), NOT a live path.

═══════════════════════════════════════════════════════════════════════════════
WHY THIS EXISTS (the Rule-10 finding the explicit stepper hit)
═══════════════════════════════════════════════════════════════════════════════
The explicit nonlinear leapfrog (native_cage_fdtd.NativeCageFDTD — historical,
git 050f1088, absent at HEAD) goes SECULARLY
UNSTABLE in deep saturation: as the core self-focuses toward A→1, S=(1−A²)^p→0
so the bulk stiffness D=1/S DIVERGES (c_eff=c0/√S→∞) and ρ(L_native) GROWS during
the run — the seed-measured explicit CFL dt becomes invalid mid-run and the
leapfrog blows up (peak 5.5→15.6 as dt refines, results JSON dt_robustness). The
LINEAR (amp 0.02) and non-focusing GAUSSIAN runs stay bounded at the same dt, so
the instability is ISOLATED to self-focusing into the steep 1/S(A→1) kernel — a
numerical (integrator-time) failure, NOT a clean Mode-III. Verdict: INCONCLUSIVE.

This module treats the STIFF L_native term IMPLICITLY so stability no longer
depends on the blow-up CFL — dt is set by ACCURACY (resolving the t≈15 self-focus
transient) not by S→0.

═══════════════════════════════════════════════════════════════════════════════
THE SCHEME — frozen-D Crank–Nicolson (Newmark β=1/4, γ=1/2), NOT backward-Euler
═══════════════════════════════════════════════════════════════════════════════
The recommended frozen-D IMEX "(I + dt²c0²L_D)V^{n+1} = 2V^n − V^{n-1}" is the
BACKWARD-EULER form on the stiff term. It is unconditionally STABLE but strongly
DISSIPATIVE — in the lossless linear limit it bleeds energy (1-D prototype: 97%
energy loss over the run). That dissipation is exactly the artifact the IMEX
rigor guard forbids: it would FAKE a "bounded persistent core" (Mode-I) by
DAMPING. So backward-Euler is REJECTED by the energy-conservation gate.

The energy-conserving implicit choice is CRANK–NICOLSON / Newmark average-
acceleration (β=1/4, γ=1/2) — the stiff restoring term averaged across the three
time levels:

    V^{n+1} − 2V^n + V^{n-1} = − dt²·c0²·L_D · (V^{n+1} + 2V^n + V^{n-1}) / 4

i.e. solve the SPD system

    (I + ¼·dt²·c0²·L_D) V^{n+1} = 2V^n − V^{n-1} − ¼·dt²·c0²·L_D·(2V^n + V^{n-1})

with D = 1/S(A^n) FROZEN (the nonlinearity lagged explicitly). For the constant-
coefficient linear case this scheme is EXACTLY energy-conserving and A-stable
(1-D prototype: |dH/H| ≈ 1e-13 over thousands of steps, bounded at 5× explicit
CFL where explicit detonates). It adds NO numerical dissipation, so a "bounded
persistent core" it reports is the PHYSICS, not the integrator.

SOLVE : the SPD system is solved by conjugate gradient (scipy.sparse.linalg.cg)
to a tight tolerance. CG is an EXACT solve to tolerance — it adds no dissipation
(verified by the energy-conservation gate at the chosen tol).

═══════════════════════════════════════════════════════════════════════════════
OPERATOR — UNCHANGED (G1-G8 validated; IMEX only changes time-integration)
═══════════════════════════════════════════════════════════════════════════════
L_D = adjoint_tetrahedral_divergence( D · tetrahedral_gradient(V) ) on the
diamond-K4 TETRA_OFFSETS stencil, D=1/S(A) folded ONCE (single-1/S, CORRECTION 2).
The sparse geometry operators (Grad, Div) are assembled ONCE from TETRA_OFFSETS
(reusing the validated graded_vacuum_network sparse build); only the cheap
diag(D) re-weight changes each step. The MINUS restoring sign (CORRECTION 1) is
carried by the +¼dt²c0²L_D on the LHS (PSD L_D ⇒ restoring). NO Cartesian 7-pt.

α-CLEAN: pure (1−A²) kernel; NO ALPHA / Q_TANK / ELECTRON / RHO_BULK; κ̃ out of
scope (scalar cage). Same guard triad as native_cage_fdtd.py:58-61 (historical
companion, git 050f1088, absent at HEAD; the triad is reproduced live below at
the import-time asserts).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# α-FREE: reuse the VALIDATED native operator + kernel (G1-G8 unchanged).
from ave.solvers.graded_vacuum_network import (
    saturation_kernel,
    stiffness_profile,
)
from ave.topological.cosserat_field_3d import TETRA_OFFSETS

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time; historically mirrored native_cage_fdtd.py:58-61,
# git 050f1088 — that companion is absent at HEAD, this live triad stands on its own).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: bare RHO_BULK magnitude must NOT be imported"


# ═════════════════════════════════════════════════════════════════════════════
# GEOMETRY-FIXED sparse Grad / Div on the diamond-K4 TETRA_OFFSETS stencil.
# Assembled ONCE; the time-domain IMEX re-weights only diag(D) each step.
# Byte-identical to the factored build in graded_vacuum_network._build_sparse_
# stiffness (:359-401) — verified against the dense operator
# _native_laplacian_with_stiffness by test_stage2_native_cage_imex.py.
# ═════════════════════════════════════════════════════════════════════════════


def build_grad_div_periodic(N: int, *, instrument_scope: str | None = None):
    """Assemble the native tetrahedral Grad (3·ndof × ndof) and Div (ndof × 3·ndof)
    as scipy sparse operators on a periodic N³ cube, from TETRA_OFFSETS ONLY.

    tetrahedral_gradient : grad[...,j] += 0.25·p_j·(roll(V,−p) − V)  for each p.
    adjoint_div          : out += 0.25·p_j·(roll(T_j,+p) − T_j).
    L_D = Div · diag(tile(D,3)) · Grad reproduces adjoint_div(D·grad(V)) EXACTLY.

    The Cartesian 7-pt Laplacian is FORBIDDEN (HR1) and never built.

    CARRIER (ENGINE-HARDENING item 5): this is the DIAMOND-Z4 NON-CANONICAL
    INSTRUMENT stencil (TETRA_OFFSETS). New callers should pass
    `instrument_scope="…"` acknowledging WHY the non-canonical carrier is used;
    omitting it emits a DeprecationWarning (frozen-provenance: this build backs the
    Stage-2 native-cage DISPERSE merged verdict, so a missing ack does NOT raise —
    KEEP-BOTH). The srs-z3 production analog is srs_cage_winding.build_incidence.
    """
    from ave.core.carrier import Carrier, require_instrument_scope

    require_instrument_scope(
        Carrier.DIAMOND_Z4,
        instrument_scope,
        site="native_cage_imex.build_grad_div_periodic",
        frozen_provenance=True,
    )

    from scipy import sparse

    ndof = N**3
    lin = np.arange(ndof)

    def roll_perm(shift):
        idx3 = np.unravel_index(lin, (N, N, N))
        ri = (
            (idx3[0] - shift[0]) % N,
            (idx3[1] - shift[1]) % N,
            (idx3[2] - shift[2]) % N,
        )
        return np.ravel_multi_index(ri, (N, N, N))

    I = sparse.identity(ndof, format="csr")
    grad_blocks = [sparse.csr_matrix((ndof, ndof)) for _ in range(3)]
    for p in TETRA_OFFSETS:
        P = sparse.csr_matrix(
            (np.ones(ndof), (lin, roll_perm((-p[0], -p[1], -p[2])))),
            shape=(ndof, ndof),
        )
        delta = P - I  # roll(V,−p) − V
        for j in range(3):
            if p[j] != 0:
                grad_blocks[j] = grad_blocks[j] + 0.25 * p[j] * delta
    Grad = sparse.vstack(grad_blocks, format="csr")  # (3·ndof, ndof)

    div_blocks = [sparse.csr_matrix((ndof, ndof)) for _ in range(3)]
    for p in TETRA_OFFSETS:
        Pp = sparse.csr_matrix(
            (np.ones(ndof), (lin, roll_perm((p[0], p[1], p[2])))),
            shape=(ndof, ndof),
        )
        delta = Pp - I  # roll(T,+p) − T
        for j in range(3):
            if p[j] != 0:
                div_blocks[j] = div_blocks[j] + 0.25 * p[j] * delta
    Div = sparse.hstack(div_blocks, format="csr")  # (ndof, 3·ndof)
    return Grad, Div


def assemble_L_D(Grad, Div, D: np.ndarray):
    """L_D = Div · diag(tile(D,3)) · Grad — the divergence-form native stiffness
    with the per-site stiffness D=1/S(A) folded ONCE (single-1/S, CORRECTION 2).
    Symmetrised (machine-eps asymmetry from the periodic roll). SPD."""
    from scipy import sparse

    ndof = D.size
    Dexp = sparse.diags(np.tile(D.reshape(ndof), 3))
    L = (Div @ Dexp @ Grad).tocsr()
    return (0.5 * (L + L.T)).tocsr()


@dataclass(frozen=True)
class NativeCageIMEXConfig:
    """Frozen Stage-2 native-cage IMEX run config (α-free; v14 Mode-I defaults).

    Mirrors NativeCageConfig (native_cage_fdtd.py:64-90 — historical companion,
    git 050f1088, absent at HEAD) so the make-or-break
    driver uses the IMEX as a drop-in. The ONLY new fields are the implicit-solve
    controls (cg_tol, cg_maxiter) and dt_accuracy_factor — there is NO sign/
    operator/kernel knob beyond the validated explicit config.

    N             : cube edge (24 = v14 canonical).
    dx            : lattice pitch (0.5 = v14).
    c0            : reference speed (1.0; c_eff²/c0²=1/S folds into D).
    V_yield       : yield amplitude (1.0; A=|V|/V_yield).
    pml_thickness : absorbing sponge thickness (4 = v14).
    exponent      : Op14 saturation exponent (0.5 √S primary).
    S_min         : saturation floor (1e-3; stiffness ceiling 1/S_min=1e3).
    A_cap         : strain clip (0.999; avoids the S=0 singularity).
    dt_accuracy_factor : dt as a MULTIPLE of the explicit-CFL dt of the COLD
                    (vacuum) operator — IMEX is unconditionally stable, so dt is
                    set by ACCURACY (resolving the t≈15 transient), not the
                    blow-up CFL. 1.0 = match the cold explicit dt (≈0.66) which
                    cleanly resolves the transient (~hundreds of steps over the
                    600-step v14 window). Smaller = finer (convergence check).
    cg_tol        : CG relative tolerance (1e-10; exact-to-tolerance ⇒ no
                    spurious dissipation, verified by the energy gate).
    cg_maxiter    : CG iteration cap.
    """

    N: int = 24
    dx: float = 0.5
    c0: float = 1.0
    V_yield: float = 1.0
    pml_thickness: int = 4
    exponent: float = 0.5
    S_min: float = 1e-3
    A_cap: float = 0.999
    dt_accuracy_factor: float = 1.0
    cg_tol: float = 1e-10
    cg_maxiter: int = 2000
    port_sigma: float = 0.0  # EM radiative port strength (energy-consistent
    #   velocity-damping in the boundary shell; 0 = closed/lossless. See
    #   __init__: the OLD sponge-MULTIPLY PML was REJECTED — it injects energy
    #   under the implicit solve (142× gain, physically impossible for a passive
    #   absorber). This is a Newmark damping-matrix C = port_sigma·diag(shell),
    #   PSD ⇒ dissipative BY CONSTRUCTION (H monotone-decreasing).


def _strain(V: np.ndarray, V_yield: float, A_cap: float) -> np.ndarray:
    """A = |V|/V_yield, clipped to A_cap (avoids the S=0 singularity)."""
    return np.minimum(np.abs(V) / V_yield, A_cap)


def cold_explicit_cfl_dt(N: int, dx: float, c0: float, cfl_safety: float = 0.4) -> float:
    """The explicit-CFL dt of the COLD (vacuum, D=1) native operator: dt =
    cfl_safety·2/√(ρ_cold·c0²), ρ_cold≈1.0 (G5). Used ONLY as the accuracy SCALE
    for the IMEX dt (the IMEX is unconditionally stable; this is not its stability
    limit). Computed from the assembled cold operator's spectral radius."""
    from scipy.sparse.linalg import eigsh

    Grad, Div = build_grad_div_periodic(N, instrument_scope="stage-2 native-cage IMEX (merged provenance)")
    L_cold = assemble_L_D(Grad, Div, np.ones(N**3))
    rho = float(eigsh(L_cold, k=1, which="LM", return_eigenvectors=False)[0])
    return cfl_safety * 2.0 / np.sqrt(max(rho * c0**2, 1e-30))


class NativeCageIMEX:
    """Native tetrahedral-K4 IMEX (implicit-stiff) time-domain stepper for the A1
    scalar V-sector — the Rule-10 fix for the explicit stepper's deep-saturation
    secular instability.

    Same leapfrog STRUCTURE / observables / PML / reactance-pair recording as
    NativeCageFDTD, but the stiff L_native restoring term is integrated by
    frozen-D Crank–Nicolson (Newmark β=¼):
        (I + ¼·dt²·c0²·L_D) V^{n+1}
            = 2V^n − V^{n-1} − ¼·dt²·c0²·L_D·(2V^n + V^{n-1})
    with D=1/S(A^n) frozen (nonlinearity lagged). SPD solve by CG. Energy-
    conserving in the lossless linear limit (the rigor guard) — NO spurious
    damping that could fake Mode-I.
    """

    def __init__(self, cfg: NativeCageIMEXConfig):
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

        self.V = np.zeros((N, N, N), dtype=np.float64)
        self.V_prev = np.zeros((N, N, N), dtype=np.float64)

        # Geometry-fixed sparse Grad/Div assembled ONCE (TETRA_OFFSETS).
        self.Grad, self.Div = build_grad_div_periodic(
            N, instrument_scope="stage-2 native-cage IMEX (merged provenance)"
        )

        self._build_port_diag()
        self._build_interior_mask()

        self.time = 0.0
        self.step_count = 0
        self.dt = 0.0
        self.rho_cold = None
        self.dt_cold_cfl = None
        # EM port: closed (lossless) iff port_sigma==0 OR em_port_closed set.
        # The energy gate forces em_port_closed=True (lossless rigor guard).
        self.em_port_closed = cfg.port_sigma == 0.0
        self.last_cg_iters = 0

    # ── ENERGY-CONSISTENT radiative port (the REJECTED sponge-multiply's fix) ──
    def _build_port_diag(self):
        """Boundary-shell mask for the EM radiative port. The port enters the
        IMPLICIT update as a Newmark velocity-damping matrix C = port_sigma·
        diag(shell) — PSD, so the discrete energy is MONOTONE-DECREASING (a
        passive absorber BY CONSTRUCTION). This REPLACES the post-solve sponge-
        multiply (`V_new *= damping`), which — applied OUTSIDE the implicit solve
        — broke the discrete energy balance and INJECTED energy (142× gain at
        fine dt; verified physically-impossible-for-passive). Interior mask is
        unchanged (A-Rule 10 PML-exclusion)."""
        N, t = self.N, self.pml_thickness
        i, j, k = np.indices((N, N, N))
        d = np.minimum.reduce(
            [
                np.minimum(i, N - 1 - i),
                np.minimum(j, N - 1 - j),
                np.minimum(k, N - 1 - k),
            ]
        )
        # Quadratic ramp into the shell (0 at interior edge → 1 at the wall).
        shell = np.zeros((N, N, N), dtype=np.float64)
        if t > 0:
            in_shell = d < t
            shell[in_shell] = ((t - d[in_shell]) / t) ** 2
        self.port_shell = shell  # (N,N,N) ramp in [0,1]
        self.port_sigma = self.cfg.port_sigma

    def _build_interior_mask(self):
        """Interior mask: pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1
        (A-Rule 10 PML-exclusion). All field observables read THIS region only."""
        N, t = self.N, self.pml_thickness
        mask = np.zeros((N, N, N), dtype=bool)
        mask[t : N - t, t : N - t, t : N - t] = True
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
        Z_eff=√S→0 short ⇒ Γ=(Z_eff−1)/(Z_eff+1)→−1. Pure function of S — α-free."""
        Z_eff = self.saturation_S() ** 0.5
        gamma = (Z_eff - 1.0) / (Z_eff + 1.0)
        gi = gamma[self.interior]
        return {
            "gamma_min": float(gi.min()),
            "gamma_mean": float(gi.mean()),
            "frac_short": float((gi < -0.5).mean()),
        }

    # ── seed + dt (accuracy-set, NOT blow-up-CFL-set) ──
    def seed_sech(self, *, amplitude: float, radius: float):
        """v14 Mode-I sech seed (byte-identical to native_cage_fdtd.seed_sech —
        historical companion, git 050f1088, absent at HEAD /
        test_master_equation_v14_mode_i.py:57-64). At-rest (V_prev = V)."""
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

    def set_dt_accuracy(self) -> dict:
        """Freeze dt = dt_accuracy_factor · dt_cold_cfl, where dt_cold_cfl is the
        explicit-CFL dt of the COLD operator (accuracy SCALE, not the IMEX
        stability limit — IMEX is unconditionally stable). This resolves the
        t≈15 self-focus transient in ~hundreds of steps over the v14 window."""
        self.dt_cold_cfl = cold_explicit_cfl_dt(self.N, self.dx, self.c0)
        self.dt = self.cfg.dt_accuracy_factor * self.dt_cold_cfl
        return {
            "dt": self.dt,
            "dt_cold_cfl": self.dt_cold_cfl,
            "dt_accuracy_factor": self.cfg.dt_accuracy_factor,
        }

    # ── the IMEX (Crank–Nicolson, Newmark β=¼) step ──
    def step(self):
        """One frozen-D Crank–Nicolson step with an ENERGY-CONSISTENT radiative
        port (Newmark velocity-damping C = port_sigma·diag(shell)):

            (I + ¼·dt²·c0²·L_D + ½·dt·C) V^{n+1}
                = 2V^n − V^{n-1} − ¼·dt²·c0²·L_D·(2V^n + V^{n-1}) + ½·dt·C·V^{n-1}

        D=1/S(A^n) frozen (nonlinearity lagged). SPD (+PSD damping) solve by CG.
        C is PSD ⇒ the discrete energy is MONOTONE-DECREASING (passive absorber
        by construction). When port closed (port_sigma=0 / em_port_closed) the
        update is the exactly-energy-conserving lossless CN (the rigor guard)."""
        from scipy.sparse import diags, identity
        from scipy.sparse.linalg import cg

        if self.dt == 0.0:
            raise RuntimeError("dt not set — call set_dt_accuracy() after seeding.")
        N = self.N
        ndof = N**3
        D = self.stiffness_D()  # 1/S(A^n) — the ONLY 1/S application (single-1/S)
        L_D = assemble_L_D(self.Grad, self.Div, D)
        coef = 0.25 * (self.dt**2) * (self.c0**2)

        v = self.V.reshape(ndof)
        v_prev = self.V_prev.reshape(ndof)
        I = identity(ndof, format="csr")
        rhs = 2.0 * v - v_prev - coef * (L_D @ (2.0 * v + v_prev))
        A_sys = I + coef * L_D
        if not self.em_port_closed and self.port_sigma > 0.0:
            C = diags(self.port_sigma * self.port_shell.reshape(ndof))
            half_dtC = 0.5 * self.dt * C
            rhs = rhs + half_dtC @ v_prev
            A_sys = A_sys + half_dtC
        A_sys = A_sys.tocsr()
        v_new, info = cg(A_sys, rhs, rtol=self.cfg.cg_tol, maxiter=self.cfg.cg_maxiter, x0=v)
        self.last_cg_iters = self.cfg.cg_maxiter if info != 0 else self.last_cg_iters

        self.V_prev = self.V.copy()
        self.V = v_new.reshape(N, N, N)
        self.time += self.dt
        self.step_count += 1

    # ── observables (interior-only, PML-excluded; A-Rule 10) ──
    def interior_peak_abs_V(self) -> float:
        """Peak |V| over the PML-excluded interior (NOT centroid — §7.1)."""
        return float(np.abs(self.V[self.interior]).max())

    def interior_energy(self) -> float:
        """Σ|V|² over the PML-excluded interior."""
        return float(np.sum(self.V[self.interior] ** 2))

    # ── the IMEX-SPECIFIC rigor guard: total cage energy (the no-spurious-damping
    #    canary). H = ½‖∂_tV‖² + ½⟨V, c0²·L_D V⟩ (kinetic + native-stiffness
    #    potential). For the LOSSLESS LINEAR limit (EM port closed, small amp,
    #    D≈1) a non-dissipative scheme conserves H with NO secular decay. If H
    #    bleeds, the IMEX is over-damped and CANNOT be trusted to call Mode-I vs
    #    Mode-III. ──
    def total_energy(self) -> float:
        """Total cage energy H = ½‖∂_tV‖² + ½⟨V, c0²·L_D V⟩ over the FULL field
        (D frozen at the current strain). Velocity from the leapfrog midpoint
        (V−V_prev)/dt. Used by the energy-conservation gate."""
        N = self.N
        ndof = N**3
        D = self.stiffness_D()
        L_D = assemble_L_D(self.Grad, self.Div, D)
        v_dot = (self.V.reshape(ndof) - self.V_prev.reshape(ndof)) / self.dt
        v_mid = 0.5 * (self.V.reshape(ndof) + self.V_prev.reshape(ndof))
        kinetic = 0.5 * float(np.dot(v_dot, v_dot))
        potential = 0.5 * (self.c0**2) * float(np.dot(v_mid, L_D @ v_mid))
        return kinetic + potential

    def run_record(self, n_total: int, n_transient: int) -> dict:
        """Run n_total IMEX steps; record the reactance PAIR every step over the
        full window (A-Rule 10: C-state |V| AND L-state |∂_tV|) plus the post-
        transient persistence/breathing/Γ stats. Same return shape as
        NativeCageFDTD.run_record (drop-in for the make-or-break driver)."""
        v_peak_hist, dvdt_peak_hist, energy_hist = [], [], []
        gamma_min_hist, n_em_min_hist, max_abs_hist = [], [], []
        for _ in range(n_total):
            V_before = self.V.copy()
            self.step()
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
            "dt": self.dt,
        }


def energy_conservation_gate(
    *,
    N: int = 24,
    amplitude: float = 0.02,
    radius: float = 2.5,
    n_steps: int = 2000,
    dt_accuracy_factor: float = 1.0,
) -> dict:
    """THE IMEX-SPECIFIC RIGOR GUARD (the analog of the explicit sign-check).

    Run the IMEX on the LINEAR (small-amplitude) cage with the EM PORT CLOSED
    (no PML damping) and verify it CONSERVES energy — no secular decay over many
    periods. If the implicit scheme bleeds energy it is over-damped and CANNOT be
    trusted to call Mode-I vs Mode-III. Quantifies the effective numerical 1/Q.

    amplitude=0.02 keeps A≪1 so S≈1, D≈1 (the lossless linear limit, the same
    amplitude the explicit linear-control used: results JSON
    linear_control_amp0.02). EM port closed so the ONLY energy change a perfect
    scheme would see is zero — any decay is the integrator.

    Returns: H trend stats, secular decay rate, effective numerical 1/Q, and the
    PASS/FAIL verdict against the canary tolerance.
    """
    cfg = NativeCageIMEXConfig(N=N, dt_accuracy_factor=dt_accuracy_factor)
    eng = NativeCageIMEX(cfg)
    eng.em_port_closed = True  # lossless: no PML damping
    eng.seed_sech(amplitude=amplitude, radius=radius)
    eng.set_dt_accuracy()

    H_hist, t_hist, peak_hist = [], [], []
    H_hist.append(eng.total_energy())
    t_hist.append(eng.time)
    peak_hist.append(eng.interior_peak_abs_V())
    for _ in range(n_steps):
        eng.step()
        H_hist.append(eng.total_energy())
        t_hist.append(eng.time)
        peak_hist.append(eng.interior_peak_abs_V())
    H = np.array(H_hist)
    t = np.array(t_hist)
    H0 = H[0]
    rel_drift_end = float((H[-1] - H0) / H0)
    rel_swing = float((H.max() - H.min()) / H0)

    # Secular decay: least-squares slope of H/H0 vs t (a damping scheme has a
    # negative secular slope; a conservative one has ~0 slope, only oscillation).
    A_fit = np.vstack([t, np.ones_like(t)]).T
    slope, _ = np.linalg.lstsq(A_fit, H / H0, rcond=None)[0]
    secular_slope_per_time = float(slope)

    # Effective numerical 1/Q: model H(t) ≈ H0·exp(−ω·t/Q_num). Over the run,
    # ln(H_end/H0) = −ω·T/Q_num ⇒ 1/Q_num = −ln(H_end/H0)/(ω·T). Use the breathing
    # ω from the peak-envelope zero-crossings (number of half-periods / T).
    T_total = t[-1] - t[0]
    peak = np.array(peak_hist)
    # crude period estimate from peak-envelope sign changes about its mean.
    centred = peak - peak.mean()
    zero_cross = int(np.sum(np.diff(np.sign(centred)) != 0))
    n_periods = max(zero_cross / 2.0, 1e-9)
    omega_eff = 2.0 * np.pi * n_periods / max(T_total, 1e-30)
    if H[-1] > 0 and H0 > 0 and omega_eff > 0:
        inv_Q_numerical = float(-np.log(max(H[-1] / H0, 1e-30)) / (omega_eff * T_total))
    else:
        inv_Q_numerical = float("inf")

    # Canary tolerance: |dH/H| over many periods must stay small AND the secular
    # slope must be ≈0 (no monotone bleed). Tolerance band chosen to be far
    # tighter than any physical effect the make-or-break resolves (the Mode-I/III
    # amplitude separation is O(1) over the run; a trustworthy integrator must be
    # ≪ that). |dH/H| < 1e-3 over ~thousands of steps and |secular slope| small.
    CANARY_DRIFT = 1e-3
    CANARY_SLOPE = 1e-5
    passed = (abs(rel_drift_end) < CANARY_DRIFT) and (abs(secular_slope_per_time) < CANARY_SLOPE)
    return {
        "N": N,
        "amplitude": amplitude,
        "n_steps": n_steps,
        "dt": eng.dt,
        "n_periods_resolved": float(n_periods),
        "H0": float(H0),
        "H_end": float(H[-1]),
        "rel_drift_end": rel_drift_end,
        "rel_swing": rel_swing,
        "secular_slope_per_time": secular_slope_per_time,
        "omega_eff": float(omega_eff),
        "inv_Q_numerical": inv_Q_numerical,
        "Q_numerical": float(1.0 / inv_Q_numerical) if inv_Q_numerical > 0 else float("inf"),
        "canary_drift_tol": CANARY_DRIFT,
        "canary_slope_tol": CANARY_SLOPE,
        "passed": bool(passed),
    }
