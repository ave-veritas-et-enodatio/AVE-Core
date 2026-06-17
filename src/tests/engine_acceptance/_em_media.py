"""L2 — EM-in-a-biased-medium helpers: the Axiom-4 operating-point varactor.

A region at saturation operating-point ``A0 = |V|/V_yield`` modulates the local
effective EM parameters via the CANONICAL Axiom-4 saturation kernel
``S(A) = sqrt(1 - A^2)`` (constants.py:46; master_equation_fdtd.py:11,142). The
EM/transverse-sector varactor forms (CLAUDE.md:60-64; cvr-dc-operating-point.md:22-29):

    eps_eff = eps0 * S_eps      mu_eff = mu0 * S_mu
    c_EM    = 1/sqrt(mu_eff*eps_eff) = c0 / sqrt(S_mu*S_eps)
    Z_EM    = sqrt(mu_eff/eps_eff)   = Z0 * sqrt(S_mu/S_eps)
    n_EM    = c0/c_EM                = sqrt(S_mu*S_eps)

Two loading classes (CLAUDE.md:60, W6 2026-06-05):
  * SYM  (S_mu == S_eps == S): both sectors co-scale. Z_EM = Z0 (INVARIANT ->
         Gamma = 0, reflectionless), c_EM = c0/S (FASTER). This is the
         gravity-class / Symmetric-Gravity operating point.
  * ASYM (static-E-only: S_eps = S, S_mu = 1): loads the capacitive/eps sector
         only (a static field has no dB/dt to load mu). Z_EM = Z0/sqrt(S) != Z0
         -> Gamma != 0: the vacuum-impedance MIRROR (Op14 Meissner-asymmetric,
         Vol 4 Ch 11).

substrate-native-check walk (done before this code, Operating Principle 1):
  * Dynamics  : discrete TLM / telegrapher scatter+connect on the canonical
                bond-LC (chiral_lattice.bond_lc, the SAME medium T0.2 validates)
                graded by the per-cell operating-point S(A0(x)). NOT Maxwell-
                vector FDTD, NOT a Lagrangian, NOT gradient-descent.
  * Sector    : EM / TRANSVERSE (the photon's permittivity/permeability), NOT
                the longitudinal-A1 bond-compliance C_eff=C0/S (cvr §6, the
                genesis-24 double-count): those are ORTHOGONAL reactances
                (master-equation.md:20). L2 tests the transverse photon, so the
                canonical pair is eps_eff=eps0*S, mu_eff=mu0*S (c_EM=c0/S).
  * Objective : per-cell phase velocity c_EM, impedance Z_EM, S-parameter Gamma
                via the exact ABCD cascade (V-sector transmission) + the
                time-domain x-t band. AVE-native; not S11-of-an-energy-functional.
  * Coords A46/phase-space-coordinate-check: the L2 corpus claims live in the
                EM-sector IMPEDANCE-PLANE / phase-velocity coordinates
                (c_EM, Z_EM, Gamma, group delay vs frequency) — NOT in the
                3D-irregular-srs real-space lattice (where a localized index step
                washes out, verified empirically 2026-06-17). The 1D graded line
                on the canonical bond-LC measures in EXACTLY the corpus
                coordinates: phase velocity, impedance, Gamma, frequency-resolved
                group delay. This is the matching-coordinate substrate.
  * Saturation: this IS the operating-point modulation (Op14), rendered as the
                per-cell constitutive S(A0(x)) of a graded line.
  * CP10      : the ASYM mirror is rendered as a BOUNDARY reflection Gamma at the
                impedance step (Op3 / S-parameter), NOT a bulk confining force.
                Gamma = (Z2-Z1)/(Z2+Z1), R = Gamma^2 <= 1 (bounded by construction).

consistency-vs-emergence tags (frozen per test):
  * T2.1 refractive index            : CONSISTENCY (reproduces n=c0/c_EM via the
                                       canonical varactor; inputs are the kernel
                                       S(A) + canonical eps0/mu0/Z0).
  * T2.2 achromatic lensing          : CONSISTENCY-of-MECHANISM (reproduces the
                                       achromatic deflection of gravitational
                                       lensing via a frequency-INDEPENDENT c_EM=c0/S;
                                       the AVE-distinct mechanism). The deflection
                                       MAGNITUDE is form-derived (path integral of
                                       S-1), not a fitted number; if it turned out
                                       forced/non-fit it would be FLAGGED as a
                                       CHORD-candidate, not asserted.
  * T2.3 asymmetric mirror           : CONSISTENCY (vacuum-impedance mirror; the
                                       ASYM Z mismatch reproduces a partial
                                       reflector, contrast with the SYM Gamma=0).
  * T2.4 alpha-invariance under SYM  : CONSISTENCY of the canonical claim
                                       (clm-3zz0f6): eps_eff*c_EM = eps0*c0 so the
                                       S cancels in alpha = e^2/(4 pi eps_eff hbar
                                       c_EM); a numeric identity check, NOT an
                                       emergence (alpha itself is calibration).
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.constants import EPSILON_0, MU_0, Z_0, C_0


# ── canonical Axiom-4 saturation kernel (constants.py:46) ────────────────────
def S_of_A(A) -> np.ndarray:
    """Canonical kernel S(A) = sqrt(1 - A^2) (Axiom 4; constants.py:46).

    Clipped at the rupture wall A -> 1 to a tiny floor for numerical safety;
    L2 operates in Regime I/II (A0 < 1), well below rupture.
    """
    A = np.asarray(A, dtype=float)
    return np.sqrt(np.maximum(1e-12, 1.0 - A * A))


# ── EM-sector varactor projections (CLAUDE.md:60-64; cvr §2) ─────────────────
def em_params(A_eps, A_mu):
    """EM/transverse-sector effective parameters for per-cell operating points.

    Returns a dict of arrays: eps_eff, mu_eff, c_EM, Z_EM, n_EM — all from the
    canonical varactor eps_eff=eps0*S(A_eps), mu_eff=mu0*S(A_mu). SI-valued from
    canonical constants (Z_0, C_0, EPSILON_0, MU_0); the per-cell RATIOS to the
    cold-lattice values are the substrate-native observables.
    """
    Se = S_of_A(A_eps)
    Sm = S_of_A(A_mu)
    eps_eff = EPSILON_0 * Se
    mu_eff = MU_0 * Sm
    c_EM = 1.0 / np.sqrt(mu_eff * eps_eff)
    Z_EM = np.sqrt(mu_eff / eps_eff)
    return {
        "S_eps": Se,
        "S_mu": Sm,
        "eps_eff": eps_eff,
        "mu_eff": mu_eff,
        "c_EM": c_EM,            # = c0 / sqrt(Se*Sm)
        "Z_EM": Z_EM,            # = Z0 * sqrt(Sm/Se)
        "n_EM": C_0 / c_EM,      # = sqrt(Se*Sm)
    }


def gamma_step(Z1: float, Z2: float) -> float:
    """Reflection coefficient at an impedance step (Op3 / TIR boundary form)."""
    return (Z2 - Z1) / (Z2 + Z1)


# ── exact ABCD cascade for a graded EM line (V-sector transmission) ──────────
def _abcd_segment(Z: float, theta: float) -> np.ndarray:
    """ABCD matrix of one transmission-line segment of impedance Z, e-length theta."""
    return np.array(
        [[np.cos(theta), 1j * Z * np.sin(theta)],
         [1j * np.sin(theta) / Z, np.cos(theta)]],
        dtype=complex,
    )


def abcd_cascade(Z_cells, c_cells, dx: float, w: float) -> np.ndarray:
    """Cascade ABCD of a graded line: per-cell Z, phase velocity c, length dx."""
    M = np.eye(2, dtype=complex)
    for Zi, ci in zip(Z_cells, c_cells):
        M = M @ _abcd_segment(float(Zi), w * dx / float(ci))
    return M


def s_parameters(M: np.ndarray, Z0: float):
    """(S11, S21) of an ABCD two-port terminated in source/load Z0."""
    A, B, C, D = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    den = A + B / Z0 + C * Z0 + D
    return (A + B / Z0 - C * Z0 - D) / den, 2.0 / den


def group_delay_excess(A_eps_profile, A_mu_profile, dx: float, w_grid):
    """Excess group delay of a graded EM line vs the cold-lattice line, per ω.

    Group delay = -d(arg S21)/dw (unwrapped). For the EM varactor c_EM=c0/sqrt
    (S_mu*S_eps) which has NO w dependence, so the excess group delay is FLAT
    across the band (achromatic) and equals the path integral
        sum dx (1/c_EM - 1/c0)
    by construction. Returns (excess_group_delay[w], gamma[w], path_integral).

    Computed in NORMALIZED units (cold lattice c0=1, Z0=1) so the dimensionless
    w-grid gives O(1) electrical lengths; the per-cell normalized phase velocity
    is c_EM/c0 = 1/sqrt(S_mu*S_eps) and normalized impedance is Z_EM/Z0 =
    sqrt(S_mu/S_eps) -- the substrate-native RATIO observables (the SI scale
    factors C_0/Z_0 cancel out of every ratio and out of the group delay).
    """
    p = em_params(A_eps_profile, A_mu_profile)
    Z = p["Z_EM"] / Z_0           # normalized impedance ratio (Z0 := 1)
    c = p["c_EM"] / C_0           # normalized phase-velocity ratio (c0 := 1)
    Zv = np.ones_like(Z)
    cv = np.ones_like(c)
    w_grid = np.asarray(w_grid, dtype=float)
    ph = np.empty(len(w_grid))
    ph0 = np.empty(len(w_grid))
    gam = np.empty(len(w_grid))
    for i, w in enumerate(w_grid):
        M = abcd_cascade(Z, c, dx, w)
        M0 = abcd_cascade(Zv, cv, dx, w)
        s11, s21 = s_parameters(M, 1.0)
        _, s21_0 = s_parameters(M0, 1.0)
        ph[i] = np.angle(s21)
        ph0[i] = np.angle(s21_0)
        gam[i] = abs(s11)
    excess_phase = np.unwrap(ph) - np.unwrap(ph0)
    gd = -np.gradient(excess_phase, w_grid)
    # path-integral excess delay in normalized units: sum dx*(1/c_EM - 1/c0)
    path_integral = float(np.sum(dx * (1.0 / c - 1.0)))
    return gd, gam, path_integral


# ── time-domain graded EM line (the x-t band) ───────────────────────────────
def run_em_line(
    N: int,
    A_eps_profile,
    A_mu_profile,
    n_steps: int,
    freq: float,
    *,
    src: int = 12,
    t0: int = 120,
    tw: int = 45,
    cfl: float = 0.5,
    record_every: int = 4,
):
    """Time-domain leapfrog telegrapher on a graded EM line (normalized units).

    Normalized so the cold lattice has c0=1, Z0=1 (engine-natural units, like the
    srs L0-L1 tests). Per-cell C = S(A_eps), L = S(A_mu) -> c_cell=1/sqrt(L C)=
    c0/sqrt(S_mu S_eps), Z_cell=sqrt(L/C)=Z0 sqrt(S_mu/S_eps): the EM varactor.
    Injects a Gaussian-windowed tone burst at carrier `freq` at node `src`.

    Returns a dict with the x-t energy-density spacetime, the per-step total
    energy, the per-cell Z/c profiles, dt, and the recorded times. The stepper is
    a scatter-connect telegrapher (TLM-class), read dynamically each step (CP9).
    """
    C = S_of_A(A_eps_profile)
    L = S_of_A(A_mu_profile)
    c = 1.0 / np.sqrt(L * C)
    dt = cfl / c.max()
    Ll = 0.5 * (L[:-1] + L[1:])
    V = np.zeros(N)
    I = np.zeros(N - 1)
    spacetime = []
    times = []
    energy = []
    for t in range(n_steps):
        if t < t0 + 3 * tw:
            V[src] += np.sin(2.0 * np.pi * freq * t * dt) * np.exp(-((t - t0) / tw) ** 2)
        I += -(dt / Ll) * (V[1:] - V[:-1])
        V[1:-1] += -(dt / C[1:-1]) * (I[1:] - I[:-1])
        V[0] = 0.0
        V[-1] = 0.0
        e = C * V * V
        energy.append(float(e.sum()))
        if t % record_every == 0:
            spacetime.append(e.copy())
            times.append(t)
    return {
        "spacetime": np.array(spacetime),
        "times": np.array(times),
        "energy": np.array(energy),
        "Z": np.sqrt(L / C),
        "c": c,
        "dt": dt,
        "N": N,
    }


def reflected_fraction_flux(
    N: int,
    A_eps_profile,
    A_mu_profile,
    n_steps: int,
    freq: float,
    *,
    src: int = 12,
    probe: int = 250,
    t0: int = 120,
    tw: int = 45,
    src_off: int = 255,
    cfl: float = 0.5,
):
    """Reflected/incident power fraction at an impedance step, via flux sign.

    Integrates the Poynting-like flux P = V_node * I_link at a probe BETWEEN the
    source and the step. Right-going (incident) power has P>0, left-going
    (reflected) power has P<0; the returned ratio Σ|P<0| / Σ|P>0| is the measured
    reflection fraction R. This is robust to the open-end BCs that swamp a
    time-gated probe (it separates by propagation DIRECTION, not arrival time),
    and is the time-domain confirmation of the analytic Γ²=(ΔZ/ΣZ)² (CP10 boundary
    reflection). The SYM control returns the grid-back-scatter floor (~1e-3); the
    ASYM step returns ≈ the analytic R, so the ASYM/SYM contrast is the load.
    """
    C = S_of_A(A_eps_profile)
    L = S_of_A(A_mu_profile)
    c = 1.0 / np.sqrt(L * C)
    dt = cfl / c.max()
    Ll = 0.5 * (L[:-1] + L[1:])
    V = np.zeros(N)
    I = np.zeros(N - 1)
    p_right = 0.0
    p_left = 0.0
    for t in range(n_steps):
        if t < src_off:
            V[src] += np.sin(2.0 * np.pi * freq * t * dt) * np.exp(-((t - t0) / tw) ** 2)
        I += -(dt / Ll) * (V[1:] - V[:-1])
        V[1:-1] += -(dt / C[1:-1]) * (I[1:] - I[:-1])
        V[0] = 0.0
        V[-1] = 0.0
        P = V[probe] * I[probe]
        if P > 0:
            p_right += P
        else:
            p_left += -P
    return float(p_left / (p_right + 1e-30))


def assert_canonical_constants() -> None:
    """Fail loudly if ave.core.constants is not the worktree's canonical source."""
    import ave.core.constants as _avc

    assert _avc.__file__.endswith("ave/core/constants.py"), (
        f"ave.core.constants is not the AVE-Core canonical source: {_avc.__file__}"
    )


def bond_lc_z0() -> float:
    """The canonical bond-LC characteristic impedance (the SAME medium as T0.2)."""
    return float(cl.bond_lc()["Z_0"])
