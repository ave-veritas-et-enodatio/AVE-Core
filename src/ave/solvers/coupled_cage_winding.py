"""S3 — the COUPLED real-space A1↔ω PDE on the native tetrahedral K4 stencil.

FROZEN PRE-REG: research/2026-06-24_engine-s3-cavity-pinning_prereg.md (commit 0b5691cd).

LOCUS DISAMBIGUATION + RESULT (2026-06-24, supersedes the bare "real-space (2,3)"
seed framing below): the canonical (2,3) is a PHASE-SPACE winding portrait on the
bond-pair LC tank's Clifford torus (ave-kb/CLAUDE.md:22); the electron's REAL-SPACE
body is the 0_1 unknot. This module seeds and evolves a REAL-SPACE (2,3) phase
field — i.e. it tests the REAL-SPACE locus. That locus read NEGATIVE: S3 is
DISPERSE-FALSIFIED (winding + H_couple does NOT pin the dispersing A1 core) and the
coupled eigensolve (#415) bled the winding off the bound mode (gate-d FAIL). The
canonical PHASE-SPACE locus was then tested separately by phase_space_winding.py and
ALSO read NEGATIVE (BREAK, #417): the dynamical orbit carries the LC carrier ratio,
not the topological (2,3). NET: both internal dynamical loci negative; charge =
Link(∂Ω,F) ∈ ℤ is STATIC topology and STANDS (un-walked-back). mass = A1 (#260)
untouched. See research/2026-06-24_engine-reroute-epic-summary.md.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the S3 make-or-break instrument — the re-route payoff)
═══════════════════════════════════════════════════════════════════════════════
Stage-2 FALSIFIED the bulk self-trap: a seeded A1 precursor DISPERSES (Mode-III,
energy-conservation-certified) on the native K4 stencil (A1-ALONE does NOT
localize, research/2026-06-24_engine-stage2-native-cage_result.md). S3 tests the
SANCTIONED successor: does the now-conserved (2,3) Cosserat winding ω (S1, #407)
+ the conservative skew-Hermitian A1↔ω lock H_couple (S2, #409) PIN the dispersing
A1 core?

This module is the GENUINE NEW WORK the pre-reg §5 names: a REAL-SPACE coupled
A1↔ω PDE on the native TETRA_OFFSETS stencil. It EXTENDS the Stage-2
native_cage_imex host (native + α-clean + energy-gated scalar A1 cage) with:
  (A) the ω Cosserat winding DOF as its OWN real-space field (genesis-24 guard:
      ω is NEVER grad(V); it is seeded by seed_pq_winding and evolves by its own
      native wave operator);
  (B) the S2 conservative skew-Hermitian H_couple A1↔ω lock, lifted from the S2
      C^{2M} chain GENERATOR/FORM onto the real-space lattice (the S2 2-mode
      machinery has NO real space and CANNOT carry this — pre-reg §5);
  (C) the closed-box energy gate + GX3/GX5 negative controls on the COUPLED
      object (NO PML, NO damping — damping-bought localization is the top trap).

═══════════════════════════════════════════════════════════════════════════════
THE COUPLED STATE + GENERATOR (real-space, native stencil)
═══════════════════════════════════════════════════════════════════════════════
Two analytic-signal fields live on the same native K4 lattice:

  a_A1(x) ∈ C        — the A1 BULK-DILATATION breather analytic signal (q + i·p):
                       |a_A1|² = trapped bulk = MASS, the longitudinal "3"
                       (the DISPERSING scalar Stage-2 falsified A1-alone).
  a_ω(x) ∈ C^3       — the Cosserat micro-rotation ω LC-quadrature analytic signal
                       (Re = the winding-carrying ω config seeded by
                       seed_pq_winding; Im = its momentum quadrature, the L-state):
                       the poloidal/toroidal (2,3) winding = CHARGE/helicity,
                       a SEPARATELY-conserved real-space DOF (S1).

The A1↔ω coupling acts on the SCALAR PROJECTION of ω onto the seeded winding
template ê_w(x) (a fixed unit field): a_ω,s(x) = ê_w(x)·a_ω(x). This is the S2
on-node 2×2 block, lifted to a per-site real-space block:

  i ∂_t a_A1   = ω_b·a_A1                              (A1 breather frequency)
               − c_A1²·L_native·a_A1                   (A1 disperses on K4)
               + Ω(x)·e^{+iχθ_χ}·a_ω,s                 (THE S2 COUPLING)
  i ∂_t a_ω    = ω_s·a_ω                               (ω-tank LC frequency)
               − c_ω² ·L_native·a_ω                    (ω disperses on K4)
               + Ω(x)·e^{−iχθ_χ}·a_A1·ê_w(x)           (= conj coupling ⇒ Hermitian)

with the SATURATION-FRONT-GATED rate (the S2 FORK A=(a) coupling PORT):
      Ω(x) = rate · g_front(A) · S(A) ,   A = |a_A1|/V_yield
and L_native = adjoint_tetrahedral_divergence(D · tetrahedral_gradient(·)),
D = 1/S(A) the native saturated stiffness (the Stage-2 operator, UNCHANGED).

The full generator H (native-Laplacian blocks + on-site conjugate-pair coupling)
is HERMITIAN ⇒ the propagator e^{-iHdt} is UNITARY ⇒ the JOINT energy
‖a_A1‖² + ‖a_ω‖² is conserved EXACTLY (the rigor guard — no damping can fake a
pin). Integrated by CRANK–NICOLSON (the Cayley transform, the energy-conserving
unitary scheme, the coupled analog of the Stage-2 IMEX), D and Ω lagged (frozen)
each step. Solved by GMRES (the generator is non-symmetric complex).

═══════════════════════════════════════════════════════════════════════════════
GENESIS-24 GUARD (pre-reg §4) — ω is its OWN DOF, NEVER grad(V)
═══════════════════════════════════════════════════════════════════════════════
A1 (= MASS) and ω (= CHARGE/helicity winding) are SEPARATELY initialized,
SEPARATELY conserved. ω is seeded by seed_pq_winding (a real-space (2,3) phase
field), NEVER read off a_A1. H_couple's chirality phase χ·θ_χ is STRUCTURAL
(lattice handedness, θ_χ = 2π·ν_vac), NOT read off V. The energy gate certifies
BOTH the A1-norm AND the ω-winding — a "pin" cannot be bought by bleeding the
winding into the scalar.

α-CLEAN: the coupling rate scale uses κ̃=6/5 (the host-certified α-free winding
factor) and the chirality phase uses θ_χ=2π·ν_vac (ν_vac=2/7, α-free). NO ALPHA
/ KAPPA_CHIRAL_ELECTRON / V_SNAP / Q_TANK on the chord-deciding path. The
_winding_host forbidden-name guard is extended into the coupled step (the load-
time guard triad re-asserted below).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# α-FREE: reuse the VALIDATED native operator + kernel (Stage-2, G1-G8 unchanged).
from ave.solvers.graded_vacuum_network import (
    saturation_kernel,
    stiffness_profile,
)
from ave.solvers.native_cage_imex import assemble_L_D, build_grad_div_periodic

# the real-space (2,3) winding seed + the α-free winding-host coupling inputs.
from ave.topological.charge_quantization import seed_pq_winding

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time; extends the native_cage_imex + winding-host
# guards into the COUPLED step). An α-carrier leaking here fails the import.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "α-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"

# ── the α-FREE coupling inputs (named once; both routed via the winding host) ──
# κ̃ = 6/5 (the host-certified α-free (2,3) winding factor; NOT α·κ̃).
from tests.engine_acceptance._winding_host import winding_kappa_tilde  # noqa: E402

KAPPA_TILDE: float = winding_kappa_tilde(2, 3)  # = 6/5, α-free
# the lattice chirality PHASE θ_χ = 2π·ν_vac, ν_vac = 2/7 (α-free). Hard-coded as
# a rational so NO constants-module import (no α-carrier) on the chord path.
NU_VAC: float = 2.0 / 7.0
THETA_CHI: float = 2.0 * np.pi * NU_VAC


@dataclass(frozen=True)
class CoupledCageWindingConfig:
    """Frozen S3 coupled-cage config (α-free; Stage-2 v14 cage defaults + the
    ω-DOF + H_couple controls). The cage half mirrors NativeCageIMEXConfig."""

    N: int = 24
    dx: float = 0.5
    V_yield: float = 1.0
    pml_thickness: int = 4
    exponent: float = 0.5            # Op14 saturation (√S primary)
    S_min: float = 1e-3
    A_cap: float = 0.999
    # A1 + ω wave speeds (c_eff folds 1/S into D; these are the cold speeds).
    c_A1: float = 1.0
    c_omega: float = 1.0
    # H_couple (the S2 FORM): breather/tank frequencies + the gated rate + χ.
    omega_b: float = 1.0
    omega_s: float = 1.0             # resonant ⇒ strongest A1↔ω exchange
    rate: float = 0.3               # the S2 coupling rate scale (× g_front × S)
    chi: int = +1                   # lattice handedness (matter)
    gate: str = "front"             # saturation-front-gated coupling PORT (FORK A=(a))
    # the winding seed geometry (the (2,3) eigen-precursor torus).
    R: float = 7.0
    r: float = 2.3
    # ω winding representation (genesis-24 + S1-fidelity, see class docstring):
    #   "rigid_template" (DEFAULT) — ω = b_ω(x)·ê_w(x): a complex LC-quadrature
    #       amplitude b_ω on the FIXED seeded winding template ê_w. The (2,3)
    #       winding integer is carried by the frozen ê_w ⇒ CONSERVED BY
    #       CONSTRUCTION (faithful to S1's separately-conserved winding DOF; the
    #       integer does not change under the engine step). The dynamical b_ω
    #       carries the charge-sector LC energy that disperses on the native
    #       stencil and couples to A1. This is the production representation.
    #   "dispersive_vector" — ω = a_w(x)∈C³ evolved as a free analytic-signal
    #       vector field. The Schrödinger spatial operator SMEARS the direction
    #       field ⇒ the winding integer UNWINDS even uncoupled (an instrument
    #       artifact: it does NOT represent S1's topological conservation). KEPT
    #       as a documented negative control (the winding-NOT-conserved arm).
    winding_mode: str = "rigid_template"
    c_omega_b: float = 1.0          # b_ω LC-amplitude dispersion speed (rigid_template)
    dt: float = 0.066               # accuracy-set (Stage-2 production dt)
    gmres_tol: float = 1e-10
    gmres_maxiter: int = 2000
    winding_on: bool = True          # winding OFF (False) ⇒ Ω≡0 ⇒ A1-alone control
    port_sigma: float = 0.0          # 0 = closed/lossless (the energy-gate rigor)


def front_gate(A: np.ndarray, *, center: float = 4.0 / 7.0, width: float = 0.18) -> np.ndarray:
    """g_front(A): a thin shell at the Non-Linear→Saturated boundary (CP10) — the
    saturation-FRONT window where the A1↔ω coupling ENGAGES (zero in cold vacuum
    A→0 AND in the deep frozen core A→1). center = R_II = 4/7 (α-free; the SAME
    shell s2_hcouple_gate.front_gate uses). This is the S(A)-gating that makes the
    coupling a saturation-FRONT effect (S2 FORK A=(a)), not a bulk-volume coupling."""
    return np.exp(-((A - center) ** 2) / (2.0 * width**2))


def _strain(absV: np.ndarray, V_yield: float, A_cap: float) -> np.ndarray:
    """A = |V|/V_yield, clipped to A_cap (avoids the S=0 singularity)."""
    return np.minimum(absV / V_yield, A_cap)


class CoupledCageWinding:
    """The S3 coupled real-space A1↔ω PDE on the native tetrahedral K4 stencil.

    State (complex analytic signals, on the periodic N³ native lattice):
      self.a_A1 : (N,N,N) complex      — the A1 bulk-dilatation breather (MASS).
      self.b_w  : (N,N,N) complex      — the ω LC-quadrature AMPLITUDE on the fixed
                                         winding template (rigid_template mode); the
                                         CHARGE/helicity winding's dynamical content.
      self.a_w  : (N,N,N,3) complex    — the full ω vector field (dispersive_vector
                                         mode only — the documented unwinding control).
      self.e_w  : (N,N,N,3) real unit  — the FIXED seeded winding template ê_w(x).
                                         In rigid_template mode the (2,3) winding
                                         integer is carried by THIS frozen template ⇒
                                         CONSERVED BY CONSTRUCTION (faithful to S1).
                                         The reconstructed ω = b_w·ê_w; the coupling
                                         is the on-site A1↔b_w scalar block.

    Integration: Crank–Nicolson / Cayley (I + i·dt/2·H) a^{n+1} = (I − i·dt/2·H)
    a^n with H Hermitian ⇒ exactly UNITARY ⇒ joint energy ‖a_A1‖²+‖ω‖²
    conserved to solver tolerance (the rigor guard — no damping fakes a pin).
    D = 1/S(A^n) and Ω(x) = rate·g_front·S frozen each step (nonlinearity lagged).
    """

    def __init__(self, cfg: CoupledCageWindingConfig):
        self.cfg = cfg
        N = cfg.N
        self.N = N
        self.ndof = N**3
        self.dx = cfg.dx
        self.V_yield = cfg.V_yield
        self.exponent = cfg.exponent
        self.S_min = cfg.S_min
        self.A_cap = cfg.A_cap
        self.c_A1 = cfg.c_A1
        self.c_omega = cfg.c_omega
        self.c_omega_b = cfg.c_omega_b
        self.winding_mode = cfg.winding_mode
        self.dt = cfg.dt
        self.winding_on = cfg.winding_on

        # the native geometry-fixed sparse Grad/Div (assembled ONCE, Stage-2).
        self.Grad, self.Div = build_grad_div_periodic(N)

        # fields (complex analytic signals).
        self.a_A1 = np.zeros((N, N, N), dtype=np.complex128)
        self.b_w = np.zeros((N, N, N), dtype=np.complex128)  # rigid_template amplitude
        self.a_w = np.zeros((N, N, N, 3), dtype=np.complex128)  # dispersive_vector control
        self.e_w = np.zeros((N, N, N, 3), dtype=np.float64)  # FIXED winding template
        self.w_amp0 = np.zeros((N, N, N), dtype=np.float64)  # seeded |ω| (template scale)

        self._build_interior_mask()
        self.time = 0.0
        self.step_count = 0
        self.last_gmres_info = 0

    def _build_interior_mask(self):
        """Interior mask: pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1 (A-Rule 10
        PML-exclusion). All field observables read THIS region only."""
        N, t = self.N, self.cfg.pml_thickness
        mask = np.zeros((N, N, N), dtype=bool)
        mask[t:N - t, t:N - t, t:N - t] = True
        self.interior = mask

    # ── kernel readouts (α-free; A from the A1 breather magnitude) ──
    def strain(self) -> np.ndarray:
        return _strain(np.abs(self.a_A1), self.V_yield, self.A_cap)

    def saturation_S(self) -> np.ndarray:
        return saturation_kernel(self.strain(), exponent=self.exponent, S_min=self.S_min)

    def stiffness_D(self) -> np.ndarray:
        """D = c_eff²/c0² = 1/S(A). The native saturated stiffness (Stage-2)."""
        return stiffness_profile(self.strain(), exponent=self.exponent, S_min=self.S_min)

    def coupling_Omega(self) -> np.ndarray:
        """Ω(x) = rate · g_front(A) · S(A) — the saturation-front-gated A1↔ω rate
        (S2 FORK A=(a) coupling PORT). winding_on=False ⇒ Ω≡0 (the A1-alone
        Mode-III negative control)."""
        if not self.winding_on:
            return np.zeros((self.N, self.N, self.N), dtype=np.float64)
        A = self.strain()
        S = self.saturation_S()
        if self.cfg.gate == "front":
            g = front_gate(A)
        elif self.cfg.gate == "saturation":
            g = S
        elif self.cfg.gate == "front_times_S":
            g = front_gate(A) * S
        elif self.cfg.gate == "off":
            g = np.zeros_like(A)
        else:
            raise ValueError(f"unknown gate '{self.cfg.gate}'")
        return self.cfg.rate * g * S

    # ── seeding (A1 + ω separately initialized — genesis-24 guard) ──
    def seed_A1_sech(self, *, amplitude: float, radius: float):
        """v14 Mode-I sech A1 breather (byte-identical to native_cage_imex.seed_sech
        real part; analytic signal at-rest ⇒ p=0 ⇒ a_A1 = q (real seed)). This is
        the already-localized A1 eigen-precursor (POSITED persistence, pre-reg §0)."""
        self.a_A1[:] = _sech_profile(self.N, self.dx, amplitude, radius).astype(np.complex128)

    def seed_A1_gaussian(self, *, amplitude: float, sigma: float):
        """Gaussian A1 breather seed (the seed-robustness control, pre-reg §3 trap 5)."""
        self.a_A1[:] = _gaussian_profile(self.N, self.dx, amplitude, sigma).astype(np.complex128)

    def seed_A1_field(self, V_seed: np.ndarray):
        """Plant an arbitrary at-rest A1 seed (∂_t a=0 ⇒ a_A1 = V_seed real)."""
        self.a_A1[:] = np.asarray(V_seed, dtype=np.complex128)

    def seed_winding(self, *, amplitude: float = 1.0):
        """Seed the ω winding DOF with the real-space (2,3) phase field
        (seed_pq_winding — the SAME coordinate compute_Q_link reads). This is the
        SEPARATELY-initialized charge winding; NEVER grad(V) (genesis-24 guard).

        rigid_template (production): the FIXED winding template ê_w(x) =
        normalized seeded ω carries the (2,3) winding integer (conserved by
        construction, faithful to S1); the dynamical amplitude b_ω starts at the
        seeded |ω| (at-rest LC C-state, Im=0). The reconstructed ω = b_ω·ê_w.

        dispersive_vector (control): the full ω vector analytic signal evolves
        freely (Re = ω config, Im = 0) — the documented unwinding control."""
        om = seed_pq_winding(self.N, 2, 3, self.cfg.R, self.cfg.r) * amplitude
        nrm = np.sqrt(np.sum(om**2, axis=-1))  # (N,N,N) seeded |ω|
        self.w_amp0[:] = nrm
        self.e_w[:] = np.where(nrm[..., None] > 1e-12,
                               om / np.maximum(nrm[..., None], 1e-30), 0.0)
        self.b_w[:] = nrm.astype(np.complex128)   # LC C-state amplitude
        self.a_w[:] = om.astype(np.complex128)    # dispersive_vector control state


    # ── the Hermitian generator H (native-Laplacian blocks + on-site coupling) ──
    def _state_dim(self) -> int:
        return 2 if self.winding_mode == "rigid_template" else 4

    def _assemble_H(self):
        """Assemble the sparse Hermitian generator H. D=1/S(A^n) and Ω(x) frozen at
        the current strain (nonlinearity lagged). The native L_D is the Stage-2
        operator UNCHANGED (NO Cartesian 7-pt; HR1). H is Hermitian ⇒ e^{-iHdt}
        unitary ⇒ joint energy conserved EXACTLY.

        rigid_template (production), state x = [a_A1 (ndof), b_ω (ndof)]:
          A1 block  : ω_b·I − c_A1²·L_D
          b_ω block : ω_s·I − c_omega_b²·L_D   (b_ω LC amplitude on fixed ê_w)
          coupling  : a_A1 ← Ω·e^{+iχθ_χ}·b_ω ,  b_ω ← Ω·e^{−iχθ_χ}·a_A1
                      (on-site scalar conjugate pair ⇒ Hermitian; the winding
                      integer is carried by the frozen ê_w ⇒ separately conserved).

        dispersive_vector (control), state x = [a_A1, a_w0, a_w1, a_w2] (4·ndof):
          the full ω vector field, coupled via the ê_w projection (the documented
          unwinding control — the Schrödinger spatial op smears the winding)."""
        from scipy import sparse

        nd = self.ndof
        D = self.stiffness_D().reshape(nd)
        L_D = assemble_L_D(self.Grad, self.Div, D)  # real SPD native stiffness
        I = sparse.identity(nd, format="csr", dtype=complex)
        H_A1 = self.cfg.omega_b * I - (self.c_A1**2) * L_D.astype(complex)
        Omega = self.coupling_Omega().reshape(nd)
        phase = self.cfg.chi * THETA_CHI
        cpl = Omega * np.exp(1j * phase)  # A1 ← ω,  e^{+iφ}

        if self.winding_mode == "rigid_template":
            H_b = self.cfg.omega_s * I - (self.c_omega_b**2) * L_D.astype(complex)
            blocks = [
                [H_A1, sparse.diags(cpl, format="csr")],
                [sparse.diags(np.conj(cpl), format="csr"), H_b],
            ]
            return sparse.bmat(blocks, format="csr")

        # dispersive_vector control
        H_w = self.cfg.omega_s * I - (self.c_omega**2) * L_D.astype(complex)
        blocks = [[None, None, None, None] for _ in range(4)]
        blocks[0][0] = H_A1
        for c in range(3):
            ew_c = self.e_w[..., c].reshape(nd)
            blocks[1 + c][1 + c] = H_w
            blocks[0][1 + c] = sparse.diags(cpl * ew_c, format="csr")
            blocks[1 + c][0] = sparse.diags(np.conj(cpl) * ew_c, format="csr")
        return sparse.bmat(blocks, format="csr")

    def _stack(self) -> np.ndarray:
        nd = self.ndof
        if self.winding_mode == "rigid_template":
            x = np.empty(2 * nd, dtype=np.complex128)
            x[:nd] = self.a_A1.reshape(nd)
            x[nd:] = self.b_w.reshape(nd)
            return x
        x = np.empty(4 * nd, dtype=np.complex128)
        x[:nd] = self.a_A1.reshape(nd)
        for c in range(3):
            x[(1 + c) * nd:(2 + c) * nd] = self.a_w[..., c].reshape(nd)
        return x

    def _unstack(self, x: np.ndarray):
        nd = self.ndof
        N = self.N
        self.a_A1 = x[:nd].reshape(N, N, N)
        if self.winding_mode == "rigid_template":
            self.b_w = x[nd:].reshape(N, N, N)
            return
        for c in range(3):
            self.a_w[..., c] = x[(1 + c) * nd:(2 + c) * nd].reshape(N, N, N)

    def step(self):
        """One Crank–Nicolson / Cayley step (the energy-conserving unitary scheme):
            (I + i·dt/2·H) x^{n+1} = (I − i·dt/2·H) x^n
        with H Hermitian (D, Ω frozen this step). Solved by GMRES. Exactly
        norm-preserving to solver tolerance — NO spurious damping fakes a pin."""
        from scipy.sparse import identity
        from scipy.sparse.linalg import gmres

        H = self._assemble_H()
        nd_tot = self._state_dim() * self.ndof
        I = identity(nd_tot, format="csr", dtype=complex)
        half = 0.5j * self.dt
        A_sys = (I + half * H).tocsr()
        x = self._stack()
        rhs = (I - half * H) @ x
        x_new, info = gmres(A_sys, rhs, rtol=self.cfg.gmres_tol,
                            maxiter=self.cfg.gmres_maxiter, x0=x)
        self.last_gmres_info = info
        self._unstack(x_new)
        self.time += self.dt
        self.step_count += 1

    def omega_field(self) -> np.ndarray:
        """The reconstructed real-space ω vector field for the winding read.
        rigid_template: ω = |b_ω|·ê_w — the QUADRATURE-INVARIANT magnitude on the
        fixed winding template. The winding integer lives in ê_w (the direction
        field); |b_ω| (≥0, dispersion+breathing-robust) only modulates it. Reading
        off Re(b_ω) instead would be corrupted by the LC L-state quadrature zeros
        (Re→0 every quarter period) — an instrument artifact, NOT a topology change
        (verified: |b_ω| read holds (2,3) to t=600; Re(b_ω) read spuriously
        unwinds). dispersive_vector: Re(a_w) (the unwinding control)."""
        if self.winding_mode == "rigid_template":
            return np.abs(self.b_w)[..., None] * self.e_w
        return np.real(self.a_w)

    def omega_momentum(self) -> np.ndarray:
        """The ω momentum quadrature (L-state) for the S1 LC extractor.
        rigid_template: Im(b_ω)·ê_w; dispersive_vector: Im(a_w)."""
        if self.winding_mode == "rigid_template":
            return np.imag(self.b_w)[..., None] * self.e_w
        return np.imag(self.a_w)

    def winding_integer(self) -> dict:
        """Read the (2,3) winding integer off the reconstructed ω field
        (compute_Q_link — the SAME coordinate S1 uses). The genesis-24 BOTH-
        conserved certification reads this AND the per-grade energy split."""
        from ave.topological.charge_quantization import compute_Q_link
        q = compute_Q_link(self.omega_field(), self.cfg.R, self.cfg.r)
        return {"Q_link": int(q["Q_link"]), "w_tor": int(q["w_tor"]),
                "Q_link_raw": float(q["Q_link_raw"])}

    # ── energy observables (the rigor guard: BOTH A1-norm AND ω-winding) ──
    def total_energy(self) -> float:
        """Joint energy H = ‖a_A1‖² + ‖ω‖² over the FULL field (the conserved norm
        of the unitary map). The energy-conservation gate certifies BOTH grades
        together — a pin bought by bleeding ω into A1 would still have to keep THIS
        conserved, and the per-grade split (a1_energy / omega_energy) certifies
        neither grade is silently drained into the other."""
        return self.a1_energy() + self.omega_energy()

    def a1_energy(self) -> float:
        """‖a_A1‖² over the full field (the A1-norm — genesis-24 separate-cert)."""
        return float(np.sum(np.abs(self.a_A1) ** 2))

    def omega_energy(self) -> float:
        """‖ω‖² over the full field (the ω-charge-sector grade norm — genesis-24
        separate-cert; this is the conserved unitary grade norm). rigid_template:
        ‖b_ω‖² (the full b_ω field, the half of the unitary norm); dispersive_
        vector: ‖a_w‖². The WINDING-INTEGER conservation (winding_integer()) is the
        separate topological certification — distinct from this energy norm."""
        if self.winding_mode == "rigid_template":
            return float(np.sum(np.abs(self.b_w) ** 2))
        return float(np.sum(np.abs(self.a_w) ** 2))

    # ── A1-core real-space localization observables (A46; interior-only) ──
    def interior_peak_abs_A1(self) -> float:
        """Peak |a_A1| over the PML-excluded interior (NOT centroid — pre-reg §3)."""
        return float(np.abs(self.a_A1[self.interior]).max())

    def interior_A1_energy(self) -> float:
        """Σ|a_A1|² over the PML-excluded interior (the localized-mass content)."""
        return float(np.sum(np.abs(self.a_A1[self.interior]) ** 2))

    def a1_centroid_spread(self) -> float:
        """RMS real-space spread of the A1 energy density about its centroid (the
        DELTA observable, A46 — real-space 3-D, NOT a 2-mode proxy). A pinned core
        keeps this BOUNDED; a dispersing core's spread grows toward the box size."""
        N = self.N
        i, j, k = np.indices((N, N, N))
        w = np.abs(self.a_A1) ** 2
        W = float(w.sum())
        if W < 1e-30:
            return float("nan")
        ci = float((i * w).sum() / W)
        cj = float((j * w).sum() / W)
        ck = float((k * w).sum() / W)
        var = float((((i - ci) ** 2 + (j - cj) ** 2 + (k - ck) ** 2) * w).sum() / W)
        return float(np.sqrt(var)) * self.dx


def _sech_profile(N: int, dx: float, amplitude: float, radius: float) -> np.ndarray:
    c = N // 2
    coords = np.arange(N) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * dx
    return amplitude * (1.0 / np.cosh(r / radius))


def _gaussian_profile(N: int, dx: float, amplitude: float, sigma: float) -> np.ndarray:
    c = N // 2
    i, j, k = np.indices((N, N, N))
    r2 = ((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2) * (dx**2)
    return amplitude * np.exp(-r2 / (2.0 * sigma**2))
