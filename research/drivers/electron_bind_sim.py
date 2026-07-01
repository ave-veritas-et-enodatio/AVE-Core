"""electron_bind_sim — MEASURE the deep-core pull slope `p` vs the r^{-3} brace.

FROZEN PRE-REG: research/2026-06-30_electron-bind-sim_prereg_FROZEN.md (commit f678b0fc).
Confirms the merged port-map derivation (PR #441,
research/2026-06-30_electron-portmap-derivation_result.md §5.1): binding reduces to

    STABLE  iff  p < 3       sign(dF_net/dr|_{r*}) = sign(3 - p)
    P(r) = c_P r^{-p}   (ponderomotive pull, derivation §2)
    B(r) = c_B r^{-3}   (conserved DC-circulation centrifugal brace, derivation §3.1)

at the A1-mass-core operating point A = V_YIELD/V_SNAP = √α ≈ 0.0854 (Grant def-vyvsn1=T2 ruling).

This is a TRAP-not-CREATE existence measurement: the (2,3) winding PRE-EXISTS (seeded, conserved by
construction on the frozen ê_w template) and we read the radial FORCE BALANCE off the DYNAMICALLY-
EVOLVED fields. It is NOT the static eigensolve (#415/#417 DOES-NOT-EXIST) and NOT genesis.

Discipline (prereg §MEASUREMENT + derivation §7.3):
  * reactance-pair tracking (C-state |b_ω| AND L-state Im(b_ω)) over a recording window,
  * energy-density-peak sampling (top-K |field|²), NOT the shell centroid,
  * PML-cell exclusion BEFORE any top-K extraction,
  * local-clock ω_local(r) = ω_global·√(1 − A²(r)),
  * Tellegen-LOSSLESS (unitary CN step; NO dissipative term — |dH/H| is the certificate),
  * resolution-robustness (≥2 grids).

All slopes are FORM (Class-C); m_e/α/A=√α are imported/echo, NOT claimed.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import constants as C
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
)

# ── operating point (canonical source; ave-canonical-source) ──────────────────
ALPHA = C.ALPHA                      # 7.2973525693e-3
A_STAR = float(np.sqrt(ALPHA))       # A = V_YIELD/V_SNAP = √α ≈ 0.0854  (def-vyvsn1=T2)


# ══════════════════════════════════════════════════════════════════════════════
#  §1  RADIAL BINNING + PEAK-DENSITY SAMPLING (PML-excluded)
# ══════════════════════════════════════════════════════════════════════════════
def _radii(N: int, dx: float) -> np.ndarray:
    """Real-space radius of every cell from the box centre (native length units)."""
    c = N // 2
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2).astype(float) * dx


def radial_profile(field2: np.ndarray, radii: np.ndarray, interior: np.ndarray,
                   *, nbins: int, r_max: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Bin a per-cell scalar (e.g. an energy density) into radial shells, INTERIOR only
    (PML excluded via `interior`). Returns (r_centers, shell_mean, shell_count). Empty
    shells are NaN. This is the density-PEAK-respecting read: each shell's value is the
    MEAN over the cells at that radius, and the slope fit runs over shells where the
    density actually lives (low-count / empty-hole shells drop out of the fit)."""
    mask = interior & (radii <= r_max) & (radii > 0)
    r = radii[mask]
    v = field2[mask]
    edges = np.linspace(0.0, r_max, nbins + 1)
    idx = np.digitize(r, edges) - 1
    centers = 0.5 * (edges[:-1] + edges[1:])
    means = np.full(nbins, np.nan)
    counts = np.zeros(nbins, dtype=int)
    for b in range(nbins):
        sel = idx == b
        counts[b] = int(sel.sum())
        if counts[b] > 0:
            means[b] = float(v[sel].mean())
    return centers, means, counts


def top_k_peak_radius(field2: np.ndarray, radii: np.ndarray, interior: np.ndarray,
                      *, k: int) -> float:
    """Energy-density PEAK radius: the mean radius of the top-K |field|² cells, INTERIOR
    only (PML excluded). For a shell distribution this lands ON the shell, NOT the empty
    centroid middle (prereg CP7)."""
    vals = np.where(interior, field2, -np.inf)
    flat = vals.ravel()
    k = min(k, int(np.isfinite(flat).sum()))
    top = np.argpartition(flat, -k)[-k:]
    return float(radii.ravel()[top].mean())


# ══════════════════════════════════════════════════════════════════════════════
#  §2  REACTANCE-PAIR TRACKING (C-state |b_ω| AND L-state Im(b_ω)) over a window
# ══════════════════════════════════════════════════════════════════════════════
@dataclass
class ReactanceTrace:
    """The recorded reactance pair over the window — the discipline that lets a
    time-domain run distinguish the static brace from an oscillator caught at peak
    (prereg CP6). Both quadratures of the winding LC amplitude b_ω on the fixed ê_w
    template, per interior cell, sampled every step over `n_window` steps.

    C-state: |b_ω|(t)  — the winding AC/DC amplitude (capacitive quadrature magnitude).
    L-state: Im(b_ω)(t) — the momentum quadrature (inductive; ω_dot proxy).
    A_of_t : peak interior strain |a_A1|/V_yield over the window (operating-point check).
    """
    r_centers: np.ndarray
    A_bar: np.ndarray          # DC (time-mean) strain per shell
    dA_ac: np.ndarray          # AC swing amplitude per shell (half peak-to-peak of A(t))
    S_bar: np.ndarray          # DC (time-mean) saturation S(A) per shell
    Sdd_bar: np.ndarray        # time-mean S''(A_bar) per shell (rectification kernel)
    bw_absmean: np.ndarray     # DC (time-mean) |b_ω| per shell (C-state)
    bw_imstd: np.ndarray       # RMS Im(b_ω) per shell (L-state activity)
    A_peak_series: np.ndarray  # peak interior strain per step (operating-point trace)
    dH_over_H: float           # |ΔH/H| over the window (losslessness certificate)
    reactive_pair_active: bool # True if BOTH C-state varies AND L-state is nonzero


def _Spp(A: np.ndarray) -> np.ndarray:
    """S''(A) for S(A)=√(1−A²):  S'' = −(1−A²)^(−3/2) < 0 everywhere (derivation §2.2).
    This is the concave rectification kernel that turns the AC swing into a DC softening.
    Clipped away from the A→1 singularity (we operate at A=√α ≪ 1 anyway)."""
    one_m = np.clip(1.0 - A * A, 1e-9, 1.0)
    return -(one_m ** (-1.5))


def record_reactance_window(sim: CoupledCageWinding, *, n_window: int, nbins: int,
                            r_max: float) -> ReactanceTrace:
    """Evolve `n_window` steps, recording the reactance PAIR every step, and reduce to
    per-shell DC + AC profiles. The DC (time-mean) strain A_bar and the AC swing dA_ac
    are BOTH needed for the rectified ponderomotive pull (derivation §2.1/§2.2):
        ⟨S⟩ = S(A_bar) + ¼ S''(A_bar) dA_ac²   (the ¼ = ½ Taylor × ⟨cos²⟩=½)
    Losslessness is certified by |ΔH/H| over the window (unitary CN ⇒ ~solver tol)."""
    N, dx = sim.N, sim.dx
    radii = _radii(N, dx)
    interior = sim.interior

    H0 = sim.total_energy()
    A_series = []          # per-step interior peak strain (operating point)
    A_stack = []           # per-step full strain field (for DC mean + AC swing)
    bw_abs_stack = []      # per-step |b_ω|
    bw_im_stack = []       # per-step Im(b_ω)
    Hs = [H0]
    for _ in range(n_window):
        sim.step()
        A = sim.strain()
        A_stack.append(A)
        A_series.append(float(A[interior].max()))
        bw_abs_stack.append(np.abs(sim.b_w))
        bw_im_stack.append(np.imag(sim.b_w))
        Hs.append(sim.total_energy())

    A_stack = np.stack(A_stack)              # (T,N,N,N)
    bw_abs_stack = np.stack(bw_abs_stack)
    bw_im_stack = np.stack(bw_im_stack)

    A_bar_field = A_stack.mean(axis=0)                       # DC strain
    dA_field = 0.5 * (A_stack.max(axis=0) - A_stack.min(axis=0))  # AC swing amplitude
    S_bar_field = np.sqrt(np.clip(1.0 - A_bar_field ** 2, 1e-9, 1.0))
    Sdd_field = _Spp(A_bar_field)
    bw_absmean_field = bw_abs_stack.mean(axis=0)
    bw_imstd_field = bw_im_stack.std(axis=0)

    def _prof(f):
        return radial_profile(f, radii, interior, nbins=nbins, r_max=r_max)[1]

    rc = radial_profile(A_bar_field, radii, interior, nbins=nbins, r_max=r_max)[0]

    dH = float(abs(Hs[-1] - Hs[0]) / max(abs(Hs[0]), 1e-30))
    # reactive pair "active" iff the C-state actually swings (dA nonzero) AND the L-state
    # (Im b_ω) is nonzero somewhere interior — i.e. it IS an oscillator, not a frozen snap.
    dA_max = float(dA_field[interior].max())
    im_max = float(np.abs(bw_im_stack).max())
    reactive = (dA_max > 1e-8) and (im_max > 1e-8)

    return ReactanceTrace(
        r_centers=rc,
        A_bar=_prof(A_bar_field),
        dA_ac=_prof(dA_field),
        S_bar=_prof(S_bar_field),
        Sdd_bar=_prof(Sdd_field),
        bw_absmean=_prof(bw_absmean_field),
        bw_imstd=_prof(bw_imstd_field),
        A_peak_series=np.asarray(A_series),
        dH_over_H=dH,
        reactive_pair_active=reactive,
    )


# ══════════════════════════════════════════════════════════════════════════════
#  §3  THE INWARD PULL  P(r)  (rectified ponderomotive DC compression, derivation §2)
# ══════════════════════════════════════════════════════════════════════════════
def ponderomotive_potential(trace: ReactanceTrace) -> np.ndarray:
    """U_pond(r) ∝ ⟨S(A)⟩(r) = S(A_bar) + ¼ S''(A_bar) dA²   (derivation §2.1(i)+§2.2).

    The rectified DC softening: the AC swing dA, run through the concave kernel S''<0,
    DEPRESSES ⟨S⟩ below S(A_bar). U_C = ½Q²S/C_0 (fixed-charge varactor); the constant
    ½Q²/C_0 prefactor does NOT affect the r-SLOPE, so we track ⟨S⟩(r) itself as the
    potential-shape proxy. The pull is the inward gradient of this potential.

    NOTE (CP10 — boundary not bulk): this is a BOUNDED read — S∈[S_min,1], at A=√α
    S≈0.996, far from the A→1 wall. It is NOT the singular dS/dA→∞ bulk force at the
    wall (which only detonates in the Regime-II core the electron never reaches)."""
    return trace.S_bar + 0.25 * trace.Sdd_bar * (trace.dA_ac ** 2)


def pull_profile(trace: ReactanceTrace) -> tuple[np.ndarray, np.ndarray]:
    """P(r) = |d U_pond/dr|   — the inward ponderomotive pull magnitude per shell.
    Returns (r_centers, P) over the shells where the potential is finite. The SLOPE of
    P(r) vs r on a log-log fit is the deep-core exponent `p` (the make-or-break)."""
    r = trace.r_centers
    U = ponderomotive_potential(trace)
    good = np.isfinite(U)
    r_g, U_g = r[good], U[good]
    # central-difference gradient of the potential vs radius; |·| = inward magnitude.
    dUdr = np.gradient(U_g, r_g)
    return r_g, np.abs(dUdr)


# ══════════════════════════════════════════════════════════════════════════════
#  §4  THE OUTWARD BRACE  B(r) ∝ r^{-3}  (conserved DC circulation, derivation §3.1)
# ══════════════════════════════════════════════════════════════════════════════
def measure_L_w(sim: CoupledCageWinding) -> dict:
    """Measure the winding circulation quantum L_w (the (2,3) DC circulation).

    Two reads (prereg deliverable 5):
      * TOPOLOGICAL (the hypothesis L_w = Link): the (2,3) winding integer Q_link, w_tor
        — the phase-space-home invariant carried by the frozen ê_w (conserved by
        construction). |Link| = 1 for the electron (the poloidal linking integer).
      * MEASURED reactive circulation: the total flux Σ|F| = Σ|curl ω| over the interior
        (the substrate circulation content that supplies the centrifugal reactive pressure).
    """
    from ave.topological.charge_quantization import compute_F_curl

    wi = sim.winding_integer()
    omega = sim.omega_field()
    F = compute_F_curl(omega)
    Fmag = np.linalg.norm(F, axis=-1)
    circ_total = float(Fmag[sim.interior].sum())
    return {
        "Q_link": wi["Q_link"], "w_tor": wi["w_tor"], "Q_link_raw": wi["Q_link_raw"],
        "circulation_total": circ_total,
    }


def brace_profile(sim: CoupledCageWinding, *, nbins: int, r_max: float) -> tuple[np.ndarray, np.ndarray]:
    """B(r) = |d U_rot/dr|  from the winding's centrifugal reactive-energy density.

    U_rot(r) = L_w²/(2 m_eff r²)  (derivation §3.1: conserved circulation confined to r).
    We build the MEASURED radial profile of the winding's circulation-energy density
    (|F|² weighted, the reactive store of the DC circulation) as the U_rot(r) shape, then
    take its inward gradient. Fitting B(r)∝r^{-b} recovers the brace exponent (expect −3).

    Substrate read: the circulation reactive energy density is the curl-flux magnitude
    squared, |F|²=|curl ω|², binned radially INTERIOR-only. This is a genuine reactive
    (lossless) store — no dissipative port (Ax3-clean)."""
    from ave.topological.charge_quantization import compute_F_curl

    N, dx = sim.N, sim.dx
    radii = _radii(N, dx)
    omega = sim.omega_field()
    F = compute_F_curl(omega)
    Fmag2 = np.sum(F * F, axis=-1)     # |curl ω|² — the circulation reactive-energy density
    rc, U_rot, counts = radial_profile(Fmag2, radii, sim.interior, nbins=nbins, r_max=r_max)
    good = np.isfinite(U_rot) & (counts > 0)
    rc_g, U_g = rc[good], U_rot[good]
    dUdr = np.gradient(U_g, rc_g)
    return rc_g, np.abs(dUdr)


# ══════════════════════════════════════════════════════════════════════════════
#  §5  SLOPE FIT + STABILITY  (log-log power-law fit; sign(dF_net/dr) at crossing)
# ══════════════════════════════════════════════════════════════════════════════
def fit_power_law(r: np.ndarray, y: np.ndarray, *, r_lo: float, r_hi: float) -> dict:
    """Fit y ∝ r^{-p} over the deep-core window r∈[r_lo, r_hi] where y>0 and finite.
    Returns {p, intercept_logc, r2, npts} with p = −slope of log y vs log r. The window
    restricts to the DEEP-CORE shells (small r) where the derivation's slope claim lives
    and where the density actually sits (empty-hole shells are y≈0 and drop out)."""
    m = np.isfinite(r) & np.isfinite(y) & (y > 0) & (r >= r_lo) & (r <= r_hi)
    if int(m.sum()) < 3:
        return {"p": float("nan"), "intercept_logc": float("nan"),
                "r2": float("nan"), "npts": int(m.sum())}
    lr, ly = np.log(r[m]), np.log(y[m])
    A_ = np.vstack([lr, np.ones_like(lr)]).T
    (slope, intercept), *_ = np.linalg.lstsq(A_, ly, rcond=None)
    pred = A_ @ np.array([slope, intercept])
    ss_res = float(np.sum((ly - pred) ** 2))
    ss_tot = float(np.sum((ly - ly.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else float("nan")
    return {"p": float(-slope), "intercept_logc": float(intercept),
            "r2": float(r2), "npts": int(m.sum())}


def stability_at_crossing(p_pull: float) -> dict:
    """sign(dF_net/dr|_{r*}) = sign(3 − p)  (derivation §5.1, exact for P=c_P r^{-p},
    B=c_B r^{-3}). STABLE iff dF_net/dr > 0 iff p < 3. Returns the sign + verdict."""
    d = 3.0 - p_pull
    return {"three_minus_p": float(d),
            "dFnet_dr_sign": int(np.sign(d)) if np.isfinite(d) else 0,
            "stable": bool(np.isfinite(d) and d > 0)}


# ══════════════════════════════════════════════════════════════════════════════
#  §6  RUN HARNESS  (seed A=√α operating point, evolve, measure the full balance)
# ══════════════════════════════════════════════════════════════════════════════
@dataclass
class BindConfig:
    """One binding-measurement run at a chosen operating point A_op (= √α_eff)."""
    N: int = 32
    dx: float = 0.5
    A_op: float = A_STAR          # peak interior strain = the operating point
    a1_radius: float = 3.0        # sech core radius (native)
    winding_amp: float = 0.5      # (2,3) winding seed amplitude
    R: float = 7.0
    r: float = 2.3
    n_settle: int = 20            # settle steps before the recording window
    n_window: int = 40            # reactance-pair recording window
    dt: float = 0.05
    nbins: int = 16
    top_k: int = 64
    # deep-core fit window as fractions of r_max (small r = deep core)
    fit_lo_frac: float = 0.10
    fit_hi_frac: float = 0.55


def _calibrate_a1_amplitude(cfg: BindConfig) -> float:
    """Pick the sech amplitude so the PEAK interior strain = cfg.A_op with V_yield=1.
    The sech peak |a_A1|(0) = amplitude ⇒ peak strain = amplitude/V_yield = amplitude.
    (V_yield defaults to 1.0 in the solver cfg; A = |a_A1|/V_yield.)"""
    return float(cfg.A_op)


def run_binding_measurement(cfg: BindConfig) -> dict:
    """Full single-operating-point measurement: seed A=A_op core + pre-existing (2,3)
    winding, settle, record the reactance-pair window, and read P(r), B(r), the slopes,
    stability, L_w, losslessness. TRAP-not-CREATE: the winding pre-exists and is conserved
    by construction (rigid_template ê_w). NOT genesis, NOT the static eigensolve."""
    amp = _calibrate_a1_amplitude(cfg)
    scfg = CoupledCageWindingConfig(
        N=cfg.N, dx=cfg.dx, V_yield=1.0, dt=cfg.dt,
        R=cfg.R, r=cfg.r, winding_on=True, winding_mode="rigid_template",
        port_sigma=0.0,  # closed/lossless — the Tellegen rigor (NO dissipative port)
    )
    sim = CoupledCageWinding(scfg)
    sim.seed_A1_sech(amplitude=amp, radius=cfg.a1_radius)
    sim.seed_winding(amplitude=cfg.winding_amp)

    wi0 = sim.winding_integer()
    Lw0 = measure_L_w(sim)
    H_seed = sim.total_energy()

    for _ in range(cfg.n_settle):
        sim.step()

    A_op_measured = float(sim.strain()[sim.interior].max())
    r_max = 0.5 * (cfg.N // 2) * cfg.dx  # interior radial extent (native)
    peak_r = top_k_peak_radius(np.abs(sim.a_A1) ** 2, _radii(cfg.N, cfg.dx),
                               sim.interior, k=cfg.top_k)

    trace = record_reactance_window(sim, n_window=cfg.n_window, nbins=cfg.nbins, r_max=r_max)

    # ── pull P(r) + slope p ──
    r_P, P = pull_profile(trace)
    r_lo, r_hi = cfg.fit_lo_frac * r_max, cfg.fit_hi_frac * r_max
    pull_fit = fit_power_law(r_P, P, r_lo=r_lo, r_hi=r_hi)

    # ── brace B(r) + slope b ──
    r_B, B = brace_profile(sim, nbins=cfg.nbins, r_max=r_max)
    brace_fit = fit_power_law(r_B, B, r_lo=r_lo, r_hi=r_hi)

    # ── stability from the measured pull slope ──
    stab = stability_at_crossing(pull_fit["p"])

    # ── L_w conservation (winding integer must not unwind under lossless evolution) ──
    wi1 = sim.winding_integer()
    Lw1 = measure_L_w(sim)
    winding_conserved = (wi0["Q_link"] == wi1["Q_link"]) and (wi0["w_tor"] == wi1["w_tor"])

    # ── local-clock at the peak-density site (Op14 modulation) ──
    A_peak = float(A_op_measured)
    omega_local_frac = float(np.sqrt(max(1.0 - A_peak ** 2, 0.0)))

    return {
        "cfg": cfg,
        "A_op_target": cfg.A_op,
        "A_op_measured": A_op_measured,
        "peak_density_radius": peak_r,
        "r_max": r_max,
        "fit_window": (r_lo, r_hi),
        # slopes (the deliverable)
        "pull_slope_p": pull_fit["p"],
        "pull_fit_r2": pull_fit["r2"],
        "pull_fit_npts": pull_fit["npts"],
        "brace_slope_b": brace_fit["p"],
        "brace_fit_r2": brace_fit["r2"],
        "brace_fit_npts": brace_fit["npts"],
        # stability
        "three_minus_p": stab["three_minus_p"],
        "dFnet_dr_sign": stab["dFnet_dr_sign"],
        "stable": stab["stable"],
        # losslessness certificate (NO dissipative term)
        "dH_over_H": trace.dH_over_H,
        "reactive_pair_active": trace.reactive_pair_active,
        # winding / L_w
        "winding_integer_seed": wi0,
        "winding_integer_final": wi1,
        "winding_conserved": winding_conserved,
        "L_w_seed": Lw0,
        "L_w_final": Lw1,
        # local clock
        "omega_local_over_global": omega_local_frac,
        # raw profiles (for plotting / audit)
        "_r_P": r_P.tolist(), "_P": P.tolist(),
        "_r_B": r_B.tolist(), "_B": B.tolist(),
        "_A_bar": trace.A_bar.tolist(), "_r_centers": trace.r_centers.tolist(),
        "_dA_ac": trace.dA_ac.tolist(),
        "H_seed": H_seed,
    }


# ══════════════════════════════════════════════════════════════════════════════
#  §7  COLLECTIVE-ENVELOPE-RADIUS SWEEP  (THE corpus-claim-matching coordinate)
# ──────────────────────────────────────────────────────────────────────────────
#  COORDINATE DISCIPLINE CORRECTION (phase-space-coordinate-check, caught at §6 pilot):
#  the derivation's P(r)=c_P r^{-p}, B(r)=c_B r^{-3}, and dF_net/dr|_{r*} are ALL in the
#  COLLECTIVE ENVELOPE RADIUS r (the soliton SIZE), NOT a within-soliton radial profile
#  (derivation §4: r* = (c_P/c_B)^{1/(p-3)} is the equilibrium SIZE). The §6 within-soliton
#  profile read is the WRONG coordinate — a sech core has A FLAT at its centre (dA/dr=0),
#  so no clean r-power law lives inside one fixed soliton. THIS section sweeps the
#  envelope SIZE (compress/expand the whole core at fixed enclosed charge + circulation)
#  and reads how the pull and brace magnitudes scale with the collective radius — the
#  coordinate the derivation's p and the stability criterion actually live in.
# ══════════════════════════════════════════════════════════════════════════════
def _enclosed_charge_proxy(sim: CoupledCageWinding) -> float:
    """The reactive-charge proxy Q = Σ|a_A1| over the interior (the enclosed A1 store).
    Held ~fixed across the envelope-radius sweep by rescaling the seed amplitude (the
    'fixed reactive charge Q in a shell of radius r' of derivation §3.4)."""
    return float(np.abs(sim.a_A1[sim.interior]).sum())


def measure_at_envelope(r_env: float, *, N: int, dx: float, A_op: float,
                        winding_amp: float, R: float, r_wind: float,
                        n_settle: int, n_window: int, dt: float,
                        nbins: int, top_k: int,
                        Q_fixed: float | None = None) -> dict:
    """Seed a soliton of collective envelope radius `r_env` and a pre-existing (2,3)
    winding, settle (lossless), and read the SCALAR pull + brace magnitude for THIS
    envelope size. The SWEEP over r_env gives P(r_env), B(r_env).

    FIXED-CHARGE mode (derivation §3.4, 'fixed reactive charge Q in a shell of radius r'):
    if `Q_fixed` is given, the seed amplitude is rescaled so Σ|a_A1| ≈ Q_fixed at every
    size (so A_peak ~ Q/r RISES as the envelope shrinks — the derivation's actual model).
    If `Q_fixed` is None, peak strain is held at A_op instead (the operating-point-fixed
    read; NOTE this lets Q grow with size, which INFLATES U_pond — use fixed-Q for the p
    slope). The A1↔winding loop-radius coupling caveat (winding template R,r is a fixed
    seed param, not dynamically compressed by the A1 envelope) is handled by the SEPARATE
    winding_loop_radius_sweep() for the brace — see the §7 note + prereg Grant-flag."""
    scfg = CoupledCageWindingConfig(
        N=N, dx=dx, V_yield=1.0, dt=dt, R=R, r=r_wind,
        winding_on=True, winding_mode="rigid_template", port_sigma=0.0,
    )
    sim = CoupledCageWinding(scfg)
    if Q_fixed is None:
        # operating-point-fixed: sech peak |a_A1|(0)=amplitude ⇒ peak A=amplitude=A_op.
        sim.seed_A1_sech(amplitude=A_op, radius=r_env)
    else:
        # fixed-charge: calibrate amplitude so Σ|a_A1| ≈ Q_fixed at this envelope size.
        sim.seed_A1_sech(amplitude=A_op, radius=r_env)
        Q_now = _enclosed_charge_proxy(sim)
        scale = Q_fixed / max(Q_now, 1e-30)
        sim.seed_A1_sech(amplitude=A_op * scale, radius=r_env)
    sim.seed_winding(amplitude=winding_amp)
    wi0 = sim.winding_integer()
    H0 = sim.total_energy()

    for _ in range(n_settle):
        sim.step()

    # ── the reactance-pair window at THIS envelope size ──
    trace = record_reactance_window(sim, n_window=n_window, nbins=nbins,
                                    r_max=0.5 * (N // 2) * dx)

    A_peak = float(sim.strain()[sim.interior].max())
    Q = _enclosed_charge_proxy(sim)

    # ── PULL magnitude at this envelope size (derivation §2.1(i)) ──
    #   U_pond = ½ Q² ⟨S(A_peak)⟩ / C_0 ; the r_env-dependence enters via A_peak(r_env)
    #   (strain rises as the envelope shrinks at ~fixed Q) AND via Q. Track the
    #   ponderomotive ENERGY U(r_env) ∝ Q²·⟨S(A_peak)⟩ ; the pull is |dU/dr_env| (fit below).
    #   ⟨S⟩ rectified by the measured AC swing at the core (CP9: measured δA, not plugged).
    Sbar_core = float(np.sqrt(max(1.0 - A_peak ** 2, 1e-9)))
    dA_core = float(np.nanmax(trace.dA_ac)) if np.isfinite(trace.dA_ac).any() else 0.0
    Spp_core = float(_Spp(np.array([A_peak]))[0])
    S_rect = Sbar_core + 0.25 * Spp_core * dA_core ** 2
    U_pond = (Q ** 2) * S_rect         # ∝ ½Q²S/C_0 (prefactor ½/C_0 drops from the slope)

    # ── BRACE magnitude at this envelope size (derivation §3.1) ──
    #   U_rot = L_w²/(2 m_eff r_env²) ; brace B = -dU_rot/dr_env = L_w²/(m_eff r_env³).
    #   L_w = the conserved circulation (measured); m_eff ∝ enclosed inertia. Track the
    #   MEASURED circulation store U_rot ∝ Σ|curl ω|² over the interior at this size, whose
    #   dependence on r_env IS the brace's r-scaling.
    Lw = measure_L_w(sim)
    from ave.topological.charge_quantization import compute_F_curl
    Fmag2 = np.sum(compute_F_curl(sim.omega_field()) ** 2, axis=-1)
    U_rot = float(Fmag2[sim.interior].sum())

    wi1 = sim.winding_integer()
    dH = float(abs(sim.total_energy() - H0) / max(abs(H0), 1e-30))
    return {
        "r_env": r_env, "A_peak": A_peak, "Q": Q,
        "U_pond": U_pond, "U_rot": U_rot,
        "S_rect": S_rect, "dA_core": dA_core, "Lw_circ": Lw["circulation_total"],
        "winding_conserved": (wi0["Q_link"] == wi1["Q_link"]) and (wi0["w_tor"] == wi1["w_tor"]),
        "Q_link": wi1["Q_link"], "w_tor": wi1["w_tor"],
        "dH_over_H": dH, "reactive_pair_active": trace.reactive_pair_active,
    }


def winding_loop_radius_sweep(loop_rs: list[float], *, N: int = 32, dx: float = 0.5,
                              A_op: float = A_STAR, winding_amp: float = 0.5,
                              R: float = 7.0, n_settle: int = 12, dt: float = 0.05) -> dict:
    """THE BRACE measurement in ITS coordinate: sweep the WINDING LOOP radius r_wind (the
    (2,3) template minor radius — the loop the conserved circulation is confined to), and
    read the centrifugal reactive store U_rot ∝ Σ|curl ω|² vs loop radius. The derivation
    §3.1 brace is U_rot = L_w²/(2 m_eff r²) ⇒ B = -dU_rot/dr = L_w²/(m_eff r³) ∝ r^{-3},
    so U_rot ∝ r^{-2} and B ∝ r^{-3}. This is the coordinate the r^{-3} brace lives in —
    the A1-envelope sweep does NOT compress this loop (fixed template; §7 note + prereg
    Grant-flag). Winding conservation checked at each loop size (must hold (2,3))."""
    from ave.topological.charge_quantization import compute_F_curl
    rows = []
    for rw in loop_rs:
        scfg = CoupledCageWindingConfig(N=N, dx=dx, V_yield=1.0, dt=dt, R=R, r=rw,
                                        winding_on=True, winding_mode="rigid_template",
                                        port_sigma=0.0)
        sim = CoupledCageWinding(scfg)
        sim.seed_A1_sech(amplitude=A_op, radius=3.0)
        sim.seed_winding(amplitude=winding_amp)
        wi0 = sim.winding_integer()
        H0 = sim.total_energy()
        for _ in range(n_settle):
            sim.step()
        Fmag2 = np.sum(compute_F_curl(sim.omega_field()) ** 2, axis=-1)
        U_rot = float(Fmag2[sim.interior].sum())
        Lw = measure_L_w(sim)
        wi1 = sim.winding_integer()
        rows.append({
            "r_loop": rw, "U_rot": U_rot, "Lw_circ": Lw["circulation_total"],
            "winding_conserved": (wi0["Q_link"] == wi1["Q_link"]) and (wi0["w_tor"] == wi1["w_tor"]),
            "Q_link": wi1["Q_link"], "w_tor": wi1["w_tor"],
            "dH_over_H": float(abs(sim.total_energy() - H0) / max(abs(H0), 1e-30)),
        })
    r = np.array([x["r_loop"] for x in rows])
    U_rot = np.array([x["U_rot"] for x in rows])
    B = np.abs(np.gradient(U_rot, r))
    urot_fit = fit_power_law(r, U_rot, r_lo=r.min(), r_hi=r.max())
    brace_fit = fit_power_law(r, B, r_lo=r.min(), r_hi=r.max())
    return {
        "rows": rows, "_r_loop": r.tolist(), "_U_rot": U_rot.tolist(), "_B": B.tolist(),
        "U_rot_slope": urot_fit["p"], "U_rot_r2": urot_fit["r2"],
        "brace_slope_b": brace_fit["p"], "brace_r2": brace_fit["r2"], "brace_npts": brace_fit["npts"],
        "all_winding_conserved": all(x["winding_conserved"] for x in rows),
        "max_dH_over_H": max(x["dH_over_H"] for x in rows),
        "A_op": A_op, "N": N,
    }


def envelope_radius_sweep(r_envs: list[float], *, N: int = 32, dx: float = 0.5,
                          A_op: float = A_STAR, winding_amp: float = 0.5,
                          R: float = 7.0, r_wind: float = 2.3, n_settle: int = 20,
                          n_window: int = 30, dt: float = 0.05, nbins: int = 16,
                          top_k: int = 64, Q_fixed: float | None = None) -> dict:
    """Sweep the collective envelope radius; fit P(r_env)∝r^{-p} and B(r_env)∝r^{-b}; read
    the stability sign from the MEASURED crossing and from sign(3-p). This is the
    corpus-claim-matching coordinate (the derivation's r is the envelope SIZE). Pass
    `Q_fixed` to hold the enclosed reactive charge fixed (the derivation §3.4 model — the
    only read from which the pull slope p is meaningful)."""
    rows = [measure_at_envelope(re, N=N, dx=dx, A_op=A_op, winding_amp=winding_amp,
                                R=R, r_wind=r_wind, n_settle=n_settle, n_window=n_window,
                                dt=dt, nbins=nbins, top_k=top_k, Q_fixed=Q_fixed) for re in r_envs]
    r = np.array([x["r_env"] for x in rows])
    U_pond = np.array([x["U_pond"] for x in rows])
    U_rot = np.array([x["U_rot"] for x in rows])

    # pull P = |dU_pond/dr_env|, brace B = |dU_rot/dr_env|, on the swept envelope radius.
    P = np.abs(np.gradient(U_pond, r))
    B = np.abs(np.gradient(U_rot, r))
    # fit over the DEEP-CORE (small envelope) half of the sweep where the derivation's
    # deep-core claim lives; require the fit to span real dynamic range.
    r_lo, r_hi = r.min(), 0.6 * r.max() + 0.4 * r.min()
    pull_fit = fit_power_law(r, P, r_lo=r_lo, r_hi=r_hi)
    brace_fit = fit_power_law(r, B, r_lo=r_lo, r_hi=r_hi)
    # also fit the ENERGIES directly (U_pond∝r^{-(p-1)}, U_rot∝r^{-2}) as a cross-check
    up_fit = fit_power_law(r, U_pond, r_lo=r_lo, r_hi=r_hi)
    ur_fit = fit_power_law(r, U_rot, r_lo=r_lo, r_hi=r_hi)

    stab = stability_at_crossing(pull_fit["p"])
    all_lossless = all(x["dH_over_H"] < 1e-8 for x in rows)
    all_conserved = all(x["winding_conserved"] for x in rows)
    return {
        "rows": rows,
        "pull_slope_p": pull_fit["p"], "pull_r2": pull_fit["r2"], "pull_npts": pull_fit["npts"],
        "brace_slope_b": brace_fit["p"], "brace_r2": brace_fit["r2"], "brace_npts": brace_fit["npts"],
        "U_pond_slope": up_fit["p"], "U_pond_r2": up_fit["r2"],
        "U_rot_slope": ur_fit["p"], "U_rot_r2": ur_fit["r2"],
        "three_minus_p": stab["three_minus_p"], "dFnet_dr_sign": stab["dFnet_dr_sign"],
        "stable": stab["stable"],
        "all_lossless": all_lossless, "all_winding_conserved": all_conserved,
        "max_dH_over_H": max(x["dH_over_H"] for x in rows),
        "_r_env": r.tolist(), "_U_pond": U_pond.tolist(), "_U_rot": U_rot.tolist(),
        "_P": P.tolist(), "_B": B.tolist(),
        "A_op": A_op, "N": N,
    }


def run_alpha_robustness_sweep(alphas: list[float], *, N: int = 32,
                               base: BindConfig | None = None) -> list[dict]:
    """The KEYSTONE test: vary α ⇒ the operating point A=√α slides. Confirm the electron
    stays bound WITH MARGIN (p<3, dF/dr>0) across small-α — i.e. α only SLIDES the
    operating point, it does NOT sit on the p=3 knife-edge (keystone, not fine-tune).

    A knife-edge (p→3 as α→0) is a FINE-TUNE finding, reported as such (prereg anti-rescue
    guard). α is a KNOB here (not computed) — Class-C, no emergence claim."""
    base = base or BindConfig(N=N)
    out = []
    for a in alphas:
        cfg = BindConfig(**{**base.__dict__, "A_op": float(np.sqrt(a)), "N": N})
        res = run_binding_measurement(cfg)
        res["alpha_eff"] = a
        out.append(res)
    return out


