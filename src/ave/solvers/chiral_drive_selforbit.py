"""Chiral-drive self-orbit harness — does a CURL-type chiral bias drive a
persistent, LOSSLESS self-orbit of the (2,3) loop? (Task #22, pre-reg
`research/2026-07-08_chiral-drive-selforbit_prereg.md`).

MINIMAL substrate-native apparatus: the smallest LOSSLESS (unitary) node network
that supports a (2,3) loop and a threadable loop flux — a tight-binding node RING
of N nodes embedded on the (2,3) torus knot. State ``psi ∈ ℂ^N`` is the per-node
LC analytic amplitude (``psi = q + i·p``: Re = C-state / displacement / voltage,
Im = L-state / momentum / flux-linkage — the reactance pair). The circulation is
read as the winding of ``arg(psi)`` around the loop, i.e. in the phase-space
LC-quadrature coordinate (A46), NOT a real-space Cartesian moment.

THE DISCRIMINATOR (Aharonov–Bohm / persistent-current-in-a-ring):
  * a CURL bias  = Peierls link phases whose loop sum ∮θ ≠ 0 (a genuine flux);
  * a GRADIENT bias = a pure gauge, ∮θ = 0 (a node-potential difference).
A flux drives a persistent lossless current; a pure gauge cannot. The ring is the
minimal system whose ONLY gauge-invariant content is exactly this one loop flux
Φ = ∮θ — computed around the PHYSICAL node ring (not a Cartesian square).

LOSSLESS BY CONSTRUCTION: the generator H is Hermitian and the integrator is the
Cayley / Crank–Nicolson transform, which is UNITARY for any Hermitian H (norm
exact to machine precision; energy exact for linear H). No damping term exists in
the scheme — a circulation that needed dissipation could not appear here (Ax3).

α-CLEAN: the verdict observables are pure ``arg()`` / current ratios. No
ALPHA / Q_TANK / m_e / V_SNAP on the verdict path. NU_VAC / OMEGA_C enter ONLY as
off-path scale anchors (the ``verify_constants`` cross-check in the driver).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

__all__ = [
    "ChiralDriveConfig",
    "torus_knot_positions",
    "peierls_link_phases",
    "loop_flux",
    "seed_uniform_real",
    "seed_localized_real",
    "build_hamiltonian",
    "cayley_step",
    "bond_current",
    "net_circulation",
    "internode_mismatch",
    "density_participation_ratio",
    "evolve",
    "chiral_drive_gate",
]

# ── VALUE-ECHO IMMUNITY (GUARD): the verdict path reads pure phases/currents.
# These dimensionful value-echoes must never enter this module's globals. ──
_FORBIDDEN_VALUE_ECHO = ("ALPHA", "Q_TANK", "M_E", "m_e", "V_SNAP", "E_CHARGE", "e_charge")
for _name in _FORBIDDEN_VALUE_ECHO:
    assert _name not in globals(), (
        f"VALUE-ECHO IMMUNITY violation: '{_name}' present in "
        f"chiral_drive_selforbit globals — the verdict reads only phase/current."
    )


@dataclass
class ChiralDriveConfig:
    """Frozen apparatus parameters (pre-reg §1)."""

    N: int = 64  # nodes on the (2,3) ring
    p: int = 2  # toroidal winding of the embedding knot
    q: int = 3  # poloidal winding of the embedding knot
    R: float = 3.0  # major radius (embedding only; dynamics is ring-topological)
    r: float = 1.0  # minor radius (embedding only)
    t_hop: float = 1.0  # nearest-neighbour loop coupling (engine-natural units)
    omega0: float = 1.0  # on-site clock frequency (drops out when saturation OFF)
    A_yield: float = np.inf  # saturation limit; inf ⇒ linear (√(1−A²)→1)
    dt: float = 0.02  # Crank–Nicolson step
    n_steps: int = 6000  # total steps
    record_frac: float = 0.5  # DC-average over the LAST record_frac of the window
    seed_width_frac: float = 0.25  # SEED-B localized-bump width (fraction of N)
    seed_kind: str = "localized"  # "localized" (SEED-B) or "uniform" (SEED-A)
    bias: str = "curl"  # "curl" (∮≠0), "gradient" (∮=0), or "off"
    flux: float = 0.0  # loop flux Φ = ∮θ (radians)


# ──────────────────────────────────────────────────────────────────────────
# Geometry — the (2,3) torus-knot embedding (for the figure + honest label;
# the DYNAMICS depends only on the ring topology + the link phases).
# ──────────────────────────────────────────────────────────────────────────


def torus_knot_positions(cfg: ChiralDriveConfig) -> np.ndarray:
    """(N,3) real-space node positions on the (p,q) torus knot.

    s ∈ [0,2π): x=(R+r cos qs)cos ps, y=(R+r cos qs)sin ps, z=r sin qs.
    The nodes are ordered along the knot ⇒ nearest-neighbour hopping traces the
    single closed (2,3) loop. Used for the embedding figure and to confirm the
    ring is a genuine (2,3) knot (does not self-intersect in 3-D).
    """
    s = np.linspace(0.0, 2.0 * np.pi, cfg.N, endpoint=False)
    rad = cfg.R + cfg.r * np.cos(cfg.q * s)
    x = rad * np.cos(cfg.p * s)
    y = rad * np.sin(cfg.p * s)
    z = cfg.r * np.sin(cfg.q * s)
    return np.stack([x, y, z], axis=-1)


# ──────────────────────────────────────────────────────────────────────────
# The bias — Peierls link phases (curl vs gradient), equal per-link magnitude.
# ──────────────────────────────────────────────────────────────────────────


def peierls_link_phases(cfg: ChiralDriveConfig) -> np.ndarray:
    """θ_n on link n→n+1 (length N, periodic). Equal per-link magnitude |Φ/N|;
    only the loop sum ∮θ differs between the arms.

      * "curl":     θ_n = Φ/N ∀n      ⇒ ∮θ = Φ  (a genuine flux)
      * "gradient": θ_n = (Φ/N)(−1)^n ⇒ ∮θ = 0  (a pure gauge; χ_n=−(Φ/2N)(−1)^n)
      * "off":      θ_n = 0
    """
    N = cfg.N
    per_link = cfg.flux / N
    if cfg.bias == "off" or cfg.flux == 0.0:
        return np.zeros(N)
    if cfg.bias == "curl":
        return np.full(N, per_link)
    if cfg.bias == "gradient":
        signs = np.where(np.arange(N) % 2 == 0, 1.0, -1.0)
        return per_link * signs
    raise ValueError(f"unknown bias {cfg.bias!r}")


def loop_flux(theta: np.ndarray) -> float:
    """The gauge-invariant Wilson loop Φ = ∮θ around the physical ring."""
    return float(np.sum(theta))


# ──────────────────────────────────────────────────────────────────────────
# Seeds — static, NON-circulating (the (2,3) loop at rest).
# ──────────────────────────────────────────────────────────────────────────


def seed_uniform_real(cfg: ChiralDriveConfig) -> np.ndarray:
    """SEED-A: the uniform real k=0 mode (flux-off ground state). Zero net
    circulation at Φ=0; the exact persistent-current anchor under flux."""
    psi = np.ones(cfg.N, dtype=np.complex128)
    return psi / np.linalg.norm(psi)


def seed_localized_real(cfg: ChiralDriveConfig) -> np.ndarray:
    """SEED-B: a localized REAL raised-cosine bump. Real ⇒ zero circulation at
    Φ=0; NOT an eigenstate ⇒ circulation must BUILD under the flux (emergence)."""
    N = cfg.N
    width = max(3, int(round(cfg.seed_width_frac * N)))
    n = np.arange(N)
    c = N // 4  # off-centre so no accidental symmetry with the bias pattern
    d = np.minimum(np.abs(n - c), N - np.abs(n - c))  # periodic distance
    env = np.where(d < width, 0.5 * (1.0 + np.cos(np.pi * d / width)), 0.0)
    psi = env.astype(np.complex128)
    return psi / np.linalg.norm(psi)


# ──────────────────────────────────────────────────────────────────────────
# The Hermitian generator + the UNITARY (Cayley/Crank–Nicolson) step.
# ──────────────────────────────────────────────────────────────────────────


def _saturation_onsite(psi: np.ndarray, cfg: ChiralDriveConfig) -> np.ndarray:
    """ε_n = ω_0·√(1 − (|ψ_n|/A_y)²) — the Op14/Ax4 saturation kernel as a local
    clock (real diagonal ⇒ H stays Hermitian). A_y=inf ⇒ ε_n=ω_0 (a global clock
    that drops out of the dynamics: the clean linear discriminator).

    REGISTER TAG (2026-07-14, quarter-power Family-E burn-down, Item 2;
    research/2026-07-14_quarter-power-map.md §Family-H, open-Q#4). This quantity
    is `ε_n = ω_0·S` where `S = √(1−A²)` is the Op2/Ax4 saturation kernel applied
    DIRECTLY as the on-site ENERGY modulation on the tight-binding diagonal — an
    S^1-power register (cf. varactor stored energy E = Q²/(2C_eff) ∝ S at fixed
    charge). It is NOT the same object as the op14 FREQUENCY clock, which rides
    `√S`: the ratified local clock (PR #690) is
        ω_local = ω_global·√S = ω_global·(1−A²)^{1/4}  (a QUARTER-power in A²)
    from `C_eff = C₀/S, ω = 1/√(LC_eff)`, whereas this on-site term is
        ε_n = ω_0·S = ω_0·(1−A²)^{1/2}                 (a HALF-power in A²).

    ⚑ DISCLOSED TENSION (flag-don't-fix — NOT silently reconciled): the docstring
    and the frozen prereg (research/2026-07-08_chiral-drive-selforbit_prereg.md
    §line 55/62) both LABEL this "local clock," yet implement the S^1 energy
    register, not the √S frequency clock. NOT auto-corrected to √S here because:
    (i) the math is frozen in the prereg; (ii) saturation is active ONLY in the
    OPTIONAL/secondary Arm-5 proxy (A_yield=1.0), which is NOT part of the frozen
    verdict (verdict = arms 1-4; see solver §"Verdict"); (iii) a change to √S
    would perturb the banked Arm-5 NULL (curl PR 0.5476 vs off PR 0.5380,
    research/2026-07-08_chiral-drive-selforbit_result.md:55). The semantic
    question — is ε_n the op14 frequency clock (⇒ √S) or a deliberate S^1 on-site
    energy register? — is routed to Grant/auditor (map open-Q#4)."""
    if not np.isfinite(cfg.A_yield):
        return np.full(cfg.N, cfg.omega0)
    ratio_sq = np.clip((np.abs(psi) / cfg.A_yield) ** 2, 0.0, 1.0 - 1e-12)
    # S^1 register (see REGISTER TAG above); √S would be the op14 frequency clock.
    return cfg.omega0 * np.sqrt(1.0 - ratio_sq)


def build_hamiltonian(psi: np.ndarray, theta: np.ndarray, cfg: ChiralDriveConfig) -> np.ndarray:
    """Dense Hermitian H (N,N):  (Hψ)_n = −t[e^{−iθ_n}ψ_{n+1}+e^{iθ_{n−1}}ψ_{n−1}] + ε_n ψ_n.

    H_{n,n+1} = −t e^{−iθ_n}, H_{n+1,n} = −t e^{+iθ_n} = conj(H_{n,n+1}) ⇒ Hermitian.
    ε_n depends on |ψ_n|² only through the saturation clock (mean-field); it is real
    so H is Hermitian for every ψ.
    """
    N = cfg.N
    H = np.zeros((N, N), dtype=np.complex128)
    idx = np.arange(N)
    nxt = (idx + 1) % N
    H[idx, nxt] = -cfg.t_hop * np.exp(-1j * theta)
    H[nxt, idx] = -cfg.t_hop * np.exp(+1j * theta)
    H[idx, idx] = _saturation_onsite(psi, cfg)
    return H


def cayley_step(psi: np.ndarray, H: np.ndarray, dt: float) -> np.ndarray:
    """One Crank–Nicolson / Cayley step: ψ←(I−iHΔt/2)(I+iHΔt/2)^{-1}ψ.

    The Cayley transform of a Hermitian H is UNITARY exactly (norm preserved to
    machine precision) — this is why the harness cannot fake a self-orbit with
    hidden damping.
    """
    N = H.shape[0]
    eye = np.eye(N, dtype=np.complex128)
    A = eye + 0.5j * dt * H
    B = eye - 0.5j * dt * H
    return np.linalg.solve(A, B @ psi)


def energy(psi: np.ndarray, theta: np.ndarray, cfg: ChiralDriveConfig) -> float:
    """⟨H⟩ = −2t Σ_n Re(e^{iθ_n} ψ*_{n+1} ψ_n) + Σ_n ε_n |ψ_n|²  (the conserved total)."""
    N = cfg.N
    nxt = (np.arange(N) + 1) % N
    hop = -2.0 * cfg.t_hop * np.sum(np.real(np.exp(1j * theta) * np.conj(psi[nxt]) * psi))
    eps = _saturation_onsite(psi, cfg)
    diag = float(np.sum(eps * np.abs(psi) ** 2))
    return float(hop) + diag


# ──────────────────────────────────────────────────────────────────────────
# Observers (all gauge-covariant, phase-space / current based).
# ──────────────────────────────────────────────────────────────────────────


def bond_current(psi: np.ndarray, theta: np.ndarray, cfg: ChiralDriveConfig) -> np.ndarray:
    """Per-link current j_n = 2t Im(e^{iθ_n} ψ*_{n+1} ψ_n) (gauge-covariant)."""
    N = cfg.N
    nxt = (np.arange(N) + 1) % N
    return 2.0 * cfg.t_hop * np.imag(np.exp(1j * theta) * np.conj(psi[nxt]) * psi)


def net_circulation(psi: np.ndarray, theta: np.ndarray, cfg: ChiralDriveConfig) -> float:
    """C = Σ_n j_n — the net circulation around the loop (= N·ring-current)."""
    return float(np.sum(bond_current(psi, theta, cfg)))


def internode_mismatch(psi: np.ndarray, theta: np.ndarray, cfg: ChiralDriveConfig) -> float:
    """M = mean over links of the NORMALIZED bond current
    Im(e^{iθ_n}ψ*_{n+1}ψ_n)/(|ψ_{n+1}||ψ_n|) — the DC-averaged inter-node
    mismatch (the ∮/node-potential asymmetry the network reads). ∈[−1,1];
    Φ=0 real state ⇒ 0."""
    N = cfg.N
    nxt = (np.arange(N) + 1) % N
    num = np.imag(np.exp(1j * theta) * np.conj(psi[nxt]) * psi)
    den = np.abs(psi[nxt]) * np.abs(psi) + 1e-30
    return float(np.mean(num / den))


def density_participation_ratio(psi: np.ndarray) -> float:
    """PR = (Σ|ψ|²)² / (N Σ|ψ|⁴) ∈ (0,1]. 1 = uniform, →0 = fully localized.
    The A1-dilatation (trapped-bulk) proxy: a persistent local density
    concentration under the circulation."""
    rho = np.abs(psi) ** 2
    N = psi.shape[0]
    return float((rho.sum() ** 2) / (N * np.sum(rho ** 2) + 1e-300))


# ──────────────────────────────────────────────────────────────────────────
# The evolution — ONE unitary run, records the reactance pair every step.
# ──────────────────────────────────────────────────────────────────────────


def evolve(cfg: ChiralDriveConfig) -> dict:
    """Evolve one configuration and return DC observables + drift diagnostics.

    Records, at every step over the window: the C-state (Re ψ) / L-state (Im ψ)
    reactance pair via the full complex ψ, the net circulation C(t), the
    inter-node mismatch M(t), ⟨H⟩(t), and the norm — so the DC-averages are over
    the whole recording window (never a single-phase snapshot).
    """
    theta = peierls_link_phases(cfg)
    Phi = loop_flux(theta)
    if cfg.seed_kind == "uniform":
        psi = seed_uniform_real(cfg)
    elif cfg.seed_kind == "localized":
        psi = seed_localized_real(cfg)
    else:
        raise ValueError(f"unknown seed_kind {cfg.seed_kind!r}")

    # Seed diagnostics (anti-tautology: seed circulation w.r.t. the ACTIVE bias).
    C_seed = net_circulation(psi, theta, cfg)
    M_seed = internode_mismatch(psi, theta, cfg)
    # Seed circulation w.r.t. ZERO bias (the "static loop at rest" check).
    zero = np.zeros(cfg.N)
    C_seed_fluxoff = net_circulation(psi, zero, cfg)

    H0 = build_hamiltonian(psi, theta, cfg)
    E0 = energy(psi, theta, cfg)
    norm0 = float(np.linalg.norm(psi))

    start_rec = int(round((1.0 - cfg.record_frac) * cfg.n_steps))
    C_series: list[float] = []
    M_series: list[float] = []
    E_series: list[float] = []
    norm_series: list[float] = []
    rho_accum = np.zeros(cfg.N)
    n_rec = 0

    for step in range(cfg.n_steps):
        if np.isfinite(cfg.A_yield):
            # saturation ON: midpoint-density Picard corrector (norm still exact
            # via Cayley; energy conserved to O(dt²)).
            H_pred = build_hamiltonian(psi, theta, cfg)
            psi_pred = cayley_step(psi, H_pred, cfg.dt)
            psi_mid = 0.5 * (psi + psi_pred)
            H = build_hamiltonian(psi_mid, theta, cfg)
        else:
            H = H0  # linear: H constant ⇒ Cayley is exactly energy-conserving
        psi = cayley_step(psi, H, cfg.dt)

        if step >= start_rec:
            C_series.append(net_circulation(psi, theta, cfg))
            M_series.append(internode_mismatch(psi, theta, cfg))
            E_series.append(energy(psi, theta, cfg))
            norm_series.append(float(np.linalg.norm(psi)))
            rho_accum += np.abs(psi) ** 2
            n_rec += 1

    C_arr = np.asarray(C_series)
    M_arr = np.asarray(M_series)
    E_arr = np.asarray(E_series)
    norm_arr = np.asarray(norm_series)
    rho_dc = rho_accum / max(n_rec, 1)
    rho_dc /= rho_dc.sum() + 1e-300

    E_ref = abs(E0) + 1e-30
    h_drift = float(np.max(np.abs(E_arr - E0)) / E_ref) if E_arr.size else 0.0
    norm_drift = float(np.max(np.abs(norm_arr - norm0)) / (norm0 + 1e-30)) if norm_arr.size else 0.0

    return {
        "config": {
            "N": cfg.N, "p": cfg.p, "q": cfg.q, "t_hop": cfg.t_hop,
            "A_yield": (None if not np.isfinite(cfg.A_yield) else cfg.A_yield),
            "dt": cfg.dt, "n_steps": cfg.n_steps, "record_frac": cfg.record_frac,
            "seed_kind": cfg.seed_kind, "bias": cfg.bias, "flux": cfg.flux,
        },
        "loop_flux_wilson": Phi,
        "seed_circulation_active_bias": C_seed,
        "seed_mismatch_active_bias": M_seed,
        "seed_circulation_fluxoff": C_seed_fluxoff,
        "C_dc": float(np.mean(C_arr)) if C_arr.size else 0.0,
        "C_dc_abs": float(np.abs(np.mean(C_arr))) if C_arr.size else 0.0,
        "C_rms": float(np.sqrt(np.mean(C_arr ** 2))) if C_arr.size else 0.0,
        "ring_current_dc": (float(np.mean(C_arr)) / cfg.N) if C_arr.size else 0.0,
        "M_dc": float(np.mean(M_arr)) if M_arr.size else 0.0,
        "M_dc_abs": float(np.abs(np.mean(M_arr))) if M_arr.size else 0.0,
        "E_mean": float(np.mean(E_arr)) if E_arr.size else E0,
        "E0": E0,
        "h_drift": h_drift,
        "norm_drift": norm_drift,
        "participation_ratio_dc": density_participation_ratio(np.sqrt(rho_dc)),
        "rho_dc_peak": float(rho_dc.max()),
        "rho_dc": rho_dc.tolist(),
    }


# ──────────────────────────────────────────────────────────────────────────
# The gate — run every arm and bin the verdict per the frozen prereg §3.
# ──────────────────────────────────────────────────────────────────────────


def chiral_drive_gate(
    base: ChiralDriveConfig | None = None,
    flux_ref: float = np.pi,
    flux_sweep: tuple[float, ...] | None = None,
    null_tol: float = 1e-9,
    drift_tol: float = 1e-8,
) -> dict:
    """Run all arms and bin per prereg §3.

    flux_ref  — the reference loop flux for the curl / gradient head-to-head.
    flux_sweep — the Φ values for the rate-∝-flux law (Arm 1) and the E_circ(M)
                 law (Arm 4). Defaults to a 0→2π sweep.
    """
    cfg0 = base or ChiralDriveConfig()
    if flux_sweep is None:
        flux_sweep = tuple(np.linspace(0.0, 2.0 * np.pi, 9))

    def _cfg(**kw) -> ChiralDriveConfig:
        d = dict(cfg0.__dict__)
        d.update(kw)
        return ChiralDriveConfig(**d)

    out: dict = {"config": dict(cfg0.__dict__)}

    # ── Arm 1: CURL — rate ∝ flux (both seeds) ──
    sweep_rows = []
    for Phi in flux_sweep:
        rB = evolve(_cfg(bias="curl", flux=float(Phi), seed_kind="localized"))
        rA = evolve(_cfg(bias="curl", flux=float(Phi), seed_kind="uniform"))
        sweep_rows.append({
            "flux": float(Phi),
            "C_dc_localized": rB["C_dc"],
            "C_dc_uniform": rA["C_dc"],
            "M_dc_localized": rB["M_dc"],
            "E_circ_localized": None,  # filled after Φ=0 baseline known
            "E_mean_localized": rB["E_mean"],
            "h_drift_localized": rB["h_drift"],
        })
    E0_base = next(row["E_mean_localized"] for row in sweep_rows if row["flux"] == 0.0)
    for row in sweep_rows:
        row["E_circ_localized"] = row["E_mean_localized"] - E0_base
    out["arm1_curl_sweep"] = sweep_rows

    # rate-∝-flux fit (small-Φ linear): C_dc vs sin(Φ/N) should be ∝, and vs Φ linear.
    fl = np.array([r["flux"] for r in sweep_rows])
    Cu = np.array([r["C_dc_uniform"] for r in sweep_rows])
    sin_perlink = 2.0 * cfg0.t_hop * np.sin(fl / cfg0.N)  # exact SEED-A anchor
    anchor_max_abs_err = float(np.max(np.abs(Cu - sin_perlink)))
    # linearity of the ring current in Φ at small flux (first non-zero points)
    nz = fl > 0
    slope = float(np.polyfit(fl[nz], Cu[nz], 1)[0]) if nz.sum() >= 2 else 0.0
    out["arm1_rate_law"] = {
        "anchor_formula": "C_dc(uniform) == 2*t*sin(Phi/N)",
        "anchor_max_abs_err": anchor_max_abs_err,
        "linear_slope_C_vs_flux": slope,
        "rate_set_by_flux": bool(anchor_max_abs_err < 1e-6),
    }

    # ── Arm 2: GRADIENT control at flux_ref (must be null) ──
    grad = evolve(_cfg(bias="gradient", flux=flux_ref, seed_kind="localized"))
    curl_ref = evolve(_cfg(bias="curl", flux=flux_ref, seed_kind="localized"))
    out["arm2_gradient_control"] = {
        "flux_ref": flux_ref,
        "gradient_loop_flux": grad["loop_flux_wilson"],
        "curl_loop_flux": curl_ref["loop_flux_wilson"],
        "gradient_C_dc": grad["C_dc"],
        "gradient_M_dc": grad["M_dc"],
        "curl_C_dc": curl_ref["C_dc"],
        "curl_M_dc": curl_ref["M_dc"],
        "gradient_is_null": bool(abs(grad["C_dc"]) < null_tol and abs(grad["M_dc"]) < null_tol),
        "curl_drives": bool(abs(curl_ref["C_dc"]) > 1e6 * max(abs(grad["C_dc"]), 1e-15)),
    }

    # ── Arm 3: CONSERVATIVE (H-drift for the curl run) ──
    out["arm3_conservative"] = {
        "curl_h_drift": curl_ref["h_drift"],
        "curl_norm_drift": curl_ref["norm_drift"],
        "lossless": bool(curl_ref["h_drift"] < drift_tol and curl_ref["norm_drift"] < drift_tol),
    }

    # ── Arm 4: MASS OBSERVABLE — E_circ vs M law + bias-off null ──
    M_vals = np.array([abs(r["M_dc_localized"]) for r in sweep_rows])
    E_vals = np.array([r["E_circ_localized"] for r in sweep_rows])
    off = evolve(_cfg(bias="off", flux=0.0, seed_kind="localized"))
    good = (M_vals > 1e-9) & (E_vals > 0)
    if good.sum() >= 3:
        expo = float(np.polyfit(np.log(M_vals[good]), np.log(E_vals[good]), 1)[0])
        coeffs = np.polyfit(np.log(M_vals[good]), np.log(E_vals[good]), 1)
        pred = np.polyval(coeffs, np.log(M_vals[good]))
        ss_res = float(np.sum((np.log(E_vals[good]) - pred) ** 2))
        ss_tot = float(np.sum((np.log(E_vals[good]) - np.log(E_vals[good]).mean()) ** 2))
        r2 = 1.0 - ss_res / (ss_tot + 1e-30)
    else:
        expo, r2 = float("nan"), float("nan")
    out["arm4_mass_observable"] = {
        "E_circ_vs_M_exponent": expo,
        "E_circ_vs_M_r2": r2,
        "expected_exponent": 2.0,
        "tracks": bool(np.isfinite(expo) and abs(expo - 2.0) < 0.25 and r2 > 0.95),
        "bias_off_C_dc": off["C_dc"],
        "bias_off_M_dc": off["M_dc"],
        "bias_off_null": bool(abs(off["C_dc"]) < null_tol and abs(off["M_dc"]) < null_tol),
    }

    # ── Arm 5: A1 sourcing (saturation ON — the √(1−A²) clock bites at A_yield=1) ──
    s_curl = evolve(_cfg(A_yield=1.0, bias="curl", flux=flux_ref, seed_kind="localized"))
    s_off = evolve(_cfg(A_yield=1.0, bias="off", flux=0.0, seed_kind="localized"))
    out["arm5_a1_sourcing"] = {
        "saturation_A_yield": 1.0,
        "curl_participation_ratio": s_curl["participation_ratio_dc"],
        "off_participation_ratio": s_off["participation_ratio_dc"],
        "curl_rho_peak": s_curl["rho_dc_peak"],
        "off_rho_peak": s_off["rho_dc_peak"],
        "curl_h_drift": s_curl["h_drift"],
        "localizes_more_than_off": bool(
            s_curl["participation_ratio_dc"] < s_off["participation_ratio_dc"] - 1e-4
        ),
        "note": "PROXY: density concentration, not the A1 scalar grade proper.",
    }

    # ── Anti-tautology gates ──
    seed_curl = evolve(_cfg(bias="curl", flux=flux_ref, seed_kind="localized"))
    out["anti_tautology"] = {
        "emergent_not_planted_localized": bool(abs(seed_curl["seed_circulation_fluxoff"]) < null_tol),
        "emergent_not_planted_uniform": bool(
            abs(evolve(_cfg(bias="curl", flux=flux_ref, seed_kind="uniform"))["seed_circulation_fluxoff"]) < null_tol
        ),
        "bias_off_null": out["arm4_mass_observable"]["bias_off_null"],
        "gradient_control_null": out["arm2_gradient_control"]["gradient_is_null"],
        "conservative": out["arm3_conservative"]["lossless"],
    }

    # ── Verdict (frozen prereg §3) ──
    curl_drives = out["arm2_gradient_control"]["curl_drives"] and out["arm1_rate_law"]["rate_set_by_flux"]
    gradient_null = out["arm2_gradient_control"]["gradient_is_null"]
    lossless = out["arm3_conservative"]["lossless"]
    mass_tracks = out["arm4_mass_observable"]["tracks"]

    if not lossless:
        verdict = "NOT-LOSSLESS"
    elif not curl_drives:
        verdict = "DISCRIMINATOR-FAILS"  # curl doesn't drive
    elif not gradient_null:
        verdict = "DISCRIMINATOR-FAILS"  # gradient also drives it
    elif curl_drives and gradient_null and mass_tracks:
        verdict = "CHIRAL-DRIVE-VIABLE"
    else:
        verdict = "DISCRIMINATOR-FAILS"
    out["verdict"] = verdict
    out["verdict_detail"] = {
        "curl_drives_rate_by_flux": bool(curl_drives),
        "gradient_control_null": bool(gradient_null),
        "conservative_lossless": bool(lossless),
        "mass_observable_tracks": bool(mass_tracks),
    }
    return out


if __name__ == "__main__":
    import json

    print("CHIRAL-DRIVE SELF-ORBIT GATE (Task #22)")
    print("=" * 60)
    res = chiral_drive_gate(ChiralDriveConfig(N=48, n_steps=3000))
    print(json.dumps({k: v for k, v in res.items() if k != "arm1_curl_sweep"}, indent=2, default=str))
    print("=" * 60)
    print(f"VERDICT: {res['verdict']}")
