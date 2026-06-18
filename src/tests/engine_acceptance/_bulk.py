"""L3 longitudinal-BULK medium extension — the A1 dilatation scalar grade.

THE MEDIUM EXTENSION (substrate-native, NOT a bolt-on)
─────────────────────────────────────────────────────────────────────────────
T1.7 (`test_l1_multiwave.py`) recorded the precise gap: the srs vector-TLM
carries only 2 TRANSVERSE DOF (the photon) — there is NO longitudinal-bulk
compression mode. It named the three missing pieces:
  (a) a LONGITUDINAL (bond-axial) field grade carrying compression ALONG the
      bond direction (the A1 dilatation / Heaviside-Gibbs-excised scalar grade —
      PHYSICAL, NOT Gauss-deleted: the "no-QED-garbage longitudinal scalar");
  (b) a BULK constitutive — K=2G bulk modulus + ρ density so c_bulk = √(K/ρ) is
      defined (the EM ε,μ and the shear G do NOT set the dilatation speed);
  (c) a longitudinal scatter/connect that PROPAGATES the dilatation.

This module supplies all three substrate-natively by REUSING the canonical
Master-Equation engine `ave.core.master_equation_fdtd.MasterEquationFDTD`, which
is *already* the canonical engine for exactly this scalar longitudinal grade
(its module docstring, master_equation_fdtd.py:5-19, derives the longitudinal
scalar wave ∇²V − μ₀ε₀·S(A)·∂²V/∂t² = 0 ⇔ ∂²V/∂t² = (c₀²/S)·∇²V). The scalar V
IS the bond-axial dilatation amplitude (compression along the propagation axis),
the 7-point Laplacian + leapfrog IS the longitudinal scatter/connect, and the
c_eff²=c₀²/S kernel (c_eff_squared, :148-151) IS the bulk-modulus stiffening.
So the extension is: ADD the longitudinal scalar grade to the acceptance medium
by wrapping the canonical scalar engine the same way `_medium.py` wraps the
transverse vector-TLM and `_em_media.py` wraps the graded EM line.

WHY THIS IS THE RIGHT SUBSTRATE (substrate-native-check, done BEFORE any code):
  * Dynamics  : the canonical Master-Equation leapfrog (∂²u/∂t²=c_eff²∇²u) — a
                discrete time-domain scatter+connect of the dilatation field, NOT
                a Lagrangian / gradient-descent / energy-basin solve. The lattice
                IS the computation.
  * Sector    : the SCALAR V-sector = the A1 longitudinal-dilatation grade (the
                "mass-3"; def-9a4f07 longitudinal). This is ORTHOGONAL to the
                transverse photon (master-equation.md:20, the genesis-24
                double-count caution): we exercise ONLY the longitudinal grade
                here, never wire it into the transverse V_inc phasor.
  * Objective : a propagating compression mode — dispersion ω=c_bulk·k, energy
                transport, a well-defined dilatational speed c_bulk=√(K/ρ). NOT
                S₁₁ minimisation, NOT energy-min.
  * Coords A46: real-space / spectral observables (field energy density, front
                position, ω(k)). The T3.1/T3.2 corpus claims (longitudinal mode
                EXISTS + c_eff(V) stiffening) live in real-space / kernel-strain
                coordinates — matching. No phase-space φ²/Clifford-torus claim is
                at issue at the longitudinal-existence + stiffening rung.
  * Saturation: T3.1 runs LINEAR (A≪1, S→1, the FREE bulk mode — Regime I); T3.2
                drives the kernel across A→A_yield (Regime II near-yield, the
                stiffening). The kernel is the canonical S(A)=√(1−A²).
  * CP8       : the cage PRECURSOR. T3.2 measures the c_eff(V) stiffening that is
                the GENERATIVE precursor of the self-formed wall (T3.3/T3.4,
                DEFERRED). We do NOT plant a finished cage; we drive the kernel
                and READ the stiffening it produces.
  * CP10      : boundary-not-bulk. T3.1/T3.2 are FREE propagation + a CONSTITUTIVE
                kernel sweep — no confined detonating bulk well is rendered here.
                The closed-form c_eff(V) read in T3.2 evaluates the kernel at fixed
                operating points (no time-domain runaway). The Γ=−1 bounded
                BOUNDARY (the TIR cage) is T3.3 — DEFERRED to a ratified pass.

CANONICAL SOURCES (ave-canonical-source; constants imported, never hard-coded):
  * S(A)=√(1−A²) kernel + c_eff²=c₀²/S   master_equation_fdtd.py:11,141-151
  * c_bulk = √(K/ρ) = √(2G/ρ) via K=2G   constants.py:674-676 (V_LONG); K=2G
                                          provenance MERGED PR#261
  * c_bulk/c₀ = √2 (linear)               G_VAC=ρ·c₀² (transverse √(G/ρ)=c₀);
                                          K=2G ⇒ c_bulk=√(2G/ρ)=√2·c₀
  * Z_bulk=ρ·c_bulk, c_bulk→0 ⇒ Γ_bulk→−1 bulk-impedance-at-saturation-boundary.md:21,31,39

⚑ FLAG (flag-don't-fix; surfaced, NOT silently reconciled) — the #278 base-state
  contradiction. The orchestration brief states current main 04bcb4ac "has the
  merged #277 acceptance suite + #278 wave-typed-index/Γ fix". VERIFIED FALSE:
  `gh pr view 278` reports baseRefName=analysis/2026-06-16-engine-acceptance-l0l1
  (NOT main), and `git merge-base --is-ancestor 57a8400f origin/main` returns
  NON-ANCESTOR — so PR#278 (commits bbc08838 FIX-1/2, 65b4bc17 load-guard) is NOT
  on main 04bcb4ac and is NOT in this worktree. CONSEQUENCE FOR THIS BUILD: the
  brief said "use the CORRECTED #278 convention (c_eff²=c₀²/S; NOT the old
  S^0.25)". The c_eff STIFFENING kernel `c_eff_squared` (:148-151) = c₀²/S is
  ALREADY correct on this base and is unchanged by #278 — so T3.2 reads
  `c_eff_squared()` DIRECTLY (the authoritative source) and is INDEPENDENT of the
  #278 state. The S^0.25 defect lives ONLY in `refractive_index()` (:157-169),
  which #278 fixed to S^0.5 (n_em_index) — but this module DOES NOT CALL
  refractive_index() at all, so the build is correct regardless. The brief's
  premise that #278 is on the base is the contradiction; the physics is unaffected.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import C_0, G_VAC, RHO_BULK, V_LONG
from ave.core.master_equation_fdtd import MasterEquationFDTD


# ── canonical-source verification (ave-canonical-source Step 4) ──────────────
def assert_canonical_constants() -> None:
    """Fail loudly if ave.core.constants is not the worktree's canonical source."""
    import ave.core.constants as _avc

    assert _avc.__file__.endswith("ave/core/constants.py"), (
        f"ave.core.constants is not the AVE-Core canonical source: {_avc.__file__}"
    )


# ── the bulk constitutive (K=2G; the dilatational speed) ─────────────────────
def c_bulk_over_c0_linear() -> float:
    """c_bulk/c₀ in the LINEAR (S=1) regime = √(K/ρ)/√(G/ρ) = √(K/G) = √2 (K=2G).

    Reads V_LONG=√(2G/ρ) (constants.py:676) and C_0; the transverse photon speed
    is √(G/ρ)=c₀ on the LC lattice (constants.py:670-671). So the longitudinal
    dilatation is √2 FASTER than the transverse photon in the linear regime — the
    canonical bulk-vs-shear speed split (§2.6 MODE×REGIME grid: bulk lin ≈√2·c₀).
    """
    return float(V_LONG / C_0)


def Z_bulk(c_bulk: float, rho: float = RHO_BULK) -> float:
    """Bulk-longitudinal acoustic impedance Z_bulk = ρ·c_bulk
    (bulk-impedance-at-saturation-boundary.md:21). c_bulk→0 ⇒ Z_bulk→0 ⇒ Γ_bulk→−1
    (the T3.3 wall — DEFERRED)."""
    return float(rho * c_bulk)


# ── the canonical longitudinal-scalar engine, minimally constructed ──────────
def make_bulk_engine(
    N: int = 48,
    *,
    c0: float = 1.0,
    V_yield: float = 1.0,
    A_cap: float = 0.99,
    S_min: float = 1e-3,
    pml_thickness: int = 4,
    cfl_safety: float = 0.4,
) -> MasterEquationFDTD:
    """A 3D MasterEquationFDTD = the canonical longitudinal-DILATATION scalar engine.

    The scalar field V IS the bond-axial dilatation amplitude (compression along
    the propagation axis = the A1 grade T1.7 named missing). The 7-point Laplacian
    + leapfrog IS the longitudinal scatter/connect; c_eff²=c₀²/S IS the bulk
    stiffening. Natural units (c0=1, V_yield=1) so S=√(1−A²) sweeps cleanly; the
    physical c_bulk/c₀=√2 split is asserted separately via the K=2G constitutive
    (`c_bulk_over_c0_linear`). S_min is the c_eff² ceiling (S_min=1e-3 ⇒
    c_eff²≤1000·c₀²) so the stiffening can be read up to a deep near-yield point.
    """
    return MasterEquationFDTD(
        N=N,
        c0=c0,
        V_yield=V_yield,
        A_cap=A_cap,
        S_min=S_min,
        pml_thickness=pml_thickness,
        cfl_safety=cfl_safety,
    )


def _interior_slice(eng: MasterEquationFDTD):
    """The PML-EXCLUDED interior index window (A-Rule 10 corollary): cells with
    pml_thickness ≤ {i,j,k} ≤ N−pml_thickness−1. PML cells are frozen-absorbing
    artifact, not interior physics — any field observable must filter them first.
    """
    t = eng.pml_thickness
    return slice(t, eng.N - t)


def seed_longitudinal_plane_wave(
    eng: MasterEquationFDTD, *, amplitude: float, m: int = 2, axis: int = 2
) -> None:
    """Seed a LONGITUDINAL compression plane wave: a sinusoidal dilatation along
    `axis`, uniform in the transverse plane (a pure bond-axial compression mode).

    Sets V and V_prev for a +axis traveling wave so the leapfrog launches a
    cleanly-propagating longitudinal packet. amplitude is in V_yield units (so
    A=amplitude is the strain). The wave lives on the INTERIOR (PML-excluded);
    the envelope is centred away from the absorbing layer.
    """
    N = eng.N
    i, j, k = np.indices((N, N, N))
    coord = (i, j, k)[axis].astype(np.float64)
    L = N - 2 * eng.pml_thickness
    kx = 2.0 * np.pi * m / L
    # interior envelope (zero in the PML so nothing is launched into the sponge)
    t = eng.pml_thickness
    env = np.ones((N, N, N))
    env[:t, :, :] = env[-t:, :, :] = 0.0
    env[:, :t, :] = env[:, -t:, :] = 0.0
    env[:, :, :t] = env[:, :, -t:] = 0.0
    phase = kx * (coord - t)
    c_eff0 = eng.c0  # linear regime
    # traveling wave: V(t)=A cos(kx−ωt), V_prev=A cos(kx−ω(−dt))=A cos(kx+ω dt)
    omega = c_eff0 * kx
    eng.V = (amplitude * np.cos(phase) * env).astype(np.float64)
    eng.V_prev = (amplitude * np.cos(phase + omega * eng.dt) * env).astype(np.float64)


def interior_energy(eng: MasterEquationFDTD) -> float:
    """Σ V² over the PML-EXCLUDED interior — the longitudinal field energy proxy
    (A-Rule 10 PML-exclusion corollary applied)."""
    s = _interior_slice(eng)
    Vi = eng.V[s, s, s]
    return float(np.sum(Vi * Vi))


def seed_longitudinal_pulse(
    eng: MasterEquationFDTD, *, amplitude: float, width: float = 4.0, axis: int = 2
) -> float:
    """Seed a LOCALIZED, ONE-WAY longitudinal compression PULSE traveling +axis.

    A Gaussian dilatation envelope (interior-only; zero in the PML so nothing is
    launched into the sponge), with V_prev set one c₀·dt step BEHIND so the
    leapfrog launches it forward — the longitudinal analog of the transverse
    `oneway_packet`. Returns the seed peak-position along `axis` (interior cell
    index) so the test can measure the propagation DISPLACEMENT. This is the
    substrate-native "does the compression mode PROPAGATE" probe on the (open,
    PML-bounded) Master-Equation engine: track the energy-density PEAK, not the
    closed-box energy (the PML is an absorbing boundary by design — energy
    conservation is the wrong observable on it; propagation distance is right).
    """
    N = eng.N
    t = eng.pml_thickness
    i, j, k = np.indices((N, N, N))
    coord = (i, j, k)[axis].astype(np.float64)
    z0 = N * 0.35  # well inside the −axis interior so it can travel before the sponge
    env = np.exp(-0.5 * ((coord - z0) / width) ** 2)
    m = np.ones((N, N, N))
    m[:t, :, :] = m[-t:, :, :] = 0.0
    m[:, :t, :] = m[:, -t:, :] = 0.0
    m[:, :, :t] = m[:, :, -t:] = 0.0
    eng.V = (amplitude * env * m).astype(np.float64)
    env_back = np.exp(-0.5 * ((coord - (z0 - eng.c0 * eng.dt)) / width) ** 2)
    eng.V_prev = (amplitude * env_back * m).astype(np.float64)
    return float(z0)


def track_longitudinal_peak(
    eng: MasterEquationFDTD, n_steps: int, *, axis: int = 2
) -> dict:
    """Track the interior energy-density PEAK position of a propagating
    longitudinal pulse → fitted propagation SPEED (interior cells per unit time)
    and net displacement. The genuine "does the dilatation mode translate"
    observable (substrate-native; reads the dynamically-evolved field each step,
    CP9). Energy-density profile is the PML-EXCLUDED interior sum over the two
    transverse planes (A-Rule 10 corollary).
    """
    N, t = eng.N, eng.pml_thickness

    def _peak():
        Vi = eng.V[t : N - t, t : N - t, :]
        prof = np.sum(Vi * Vi, axis=(0, 1))
        return int(np.argmax(prof))

    zt = [_peak()]
    for _ in range(n_steps):
        eng.step()
        zt.append(_peak())
    zt = np.asarray(zt, dtype=np.float64)
    tt = np.arange(len(zt)) * eng.dt
    A = np.vstack([tt, np.ones_like(tt)]).T
    slope = float(np.linalg.lstsq(A, zt, rcond=None)[0][0])
    return {"peak_traj": zt, "speed": slope, "displacement": float(zt[-1] - zt[0])}


def measure_bulk_dispersion(
    eng_factory, *, m_values=(1, 2, 3, 4), n_steps: int = 600, axis: int = 2
) -> list[tuple[float, float]]:
    """Measure ω(k) of the FREE (linear, A≪1) longitudinal mode by tracking the
    temporal frequency of a single-m plane wave at an interior probe. Returns
    [(k, ω), ...] in lattice units. `eng_factory()` returns a fresh engine each
    call — it MUST use a sane S_min (not the deep T3.2 ceiling): the free-mode
    dispersion needs a sane dt so the FFT has enough cycles to RESOLVE distinct ω
    per m (a tiny dt from S_min≪1 collapses every m into one FFT bin = a
    measurement artifact, NOT a flat branch). The default factory in the test uses
    S_min=0.5. n_steps≥600 gives the rfft enough length to separate the low-k tones.
    """
    out = []
    for m in m_values:
        eng = eng_factory()
        L = eng.N - 2 * eng.pml_thickness
        k = 2.0 * np.pi * m / L
        seed_longitudinal_plane_wave(eng, amplitude=1e-3, m=m, axis=axis)
        # probe at an interior plane; track the dominant temporal frequency
        s = eng.pml_thickness + 4
        probe = []
        for _ in range(n_steps):
            eng.step()
            probe.append(float(eng.V[s, s, s]))
        probe = np.asarray(probe)
        probe -= probe.mean()
        # dominant FFT frequency → ω = 2π f / dt; use the per-step phase rate
        spec = np.abs(np.fft.rfft(probe * np.hanning(len(probe))))
        freqs = np.fft.rfftfreq(len(probe), d=1.0)  # cycles per step
        f_peak = freqs[1:][np.argmax(spec[1:])] if len(spec) > 2 else 0.0
        omega = 2.0 * np.pi * f_peak / eng.dt  # rad per unit time
        out.append((k / eng.dx, omega))
    return out


def run_free_bulk(
    eng: MasterEquationFDTD, n_steps: int, *, record_every: int = 0
) -> dict:
    """Evolve the FREE (linear) longitudinal mode n_steps; record interior energy
    each step + (optionally) interior x-t snapshots. The energy is the PML-excluded
    interior sum, so PML absorption is NOT counted as physical loss — the FREE-mode
    energy should be flat to the leapfrog floor on the interior over a short window
    before any packet reaches the sponge.
    """
    N, t = eng.N, eng.pml_thickness

    def _axial_profile():
        # 1D interior energy-density profile along the propagation axis (z): sum
        # |V|² over the two transverse interior planes → shape (interior_z,).
        Vi = eng.V[t : N - t, t : N - t, t : N - t]
        return np.sum(Vi * Vi, axis=(0, 1))

    e_trace = [interior_energy(eng)]
    snaps = []
    if record_every:
        snaps.append(_axial_profile())
    for n in range(n_steps):
        eng.step()
        e_trace.append(interior_energy(eng))
        if record_every and (n + 1) % record_every == 0:
            snaps.append(_axial_profile())
    return {"energy": np.asarray(e_trace), "snaps": snaps}


def c_eff_over_c0_at(A: float, *, S_min: float = 1e-3, A_cap: float = 0.99) -> float:
    """The longitudinal-bulk c_eff/c₀ at strain A, read from the CANONICAL engine
    kernel `MasterEquationFDTD.c_eff_squared` (master_equation_fdtd.py:148-151) —
    the AUTHORITATIVE source, NOT a re-derivation. c_eff²=c₀²/S(A), S=√(1−A²), so
    c_eff/c₀=S^(−1/2)=(1−A²)^(−1/4) → ∞ as A→A_yield (the #278-corrected ½-power
    convention; this is the kernel, untouched by #278, see the module FLAG). The
    S_min floor caps c_eff²≤1/S_min·c₀² (the engine ceiling)."""
    lat = MasterEquationFDTD.__new__(MasterEquationFDTD)
    lat.c0 = 1.0
    lat.V_yield = 1.0
    lat.S_min = S_min
    lat.A_cap = A_cap
    V = np.array([A * lat.V_yield], dtype=np.float64)
    c_eff_sq_over_c0sq = float(lat.c_eff_squared(V)[0] / lat.c0**2)  # = 1/S (clipped)
    return float(np.sqrt(c_eff_sq_over_c0sq))


# ═════════════════════════════════════════════════════════════════════════════
# RUNG-1 EXISTENCE CAGE helpers (T3.3 / T3.4) — POSIT the cage; A1 SCALAR ONLY.
# ═════════════════════════════════════════════════════════════════════════════
# We POSIT a high-A saturated longitudinal-bulk core (consistency-class; positing
# is legitimate here — this is NOT self-formation, that is rung-2 / DEFERRED). The
# cage is carried by the canonical two-branch CrystalEngine driven on its BULK
# (A1 scalar V) branch ONLY: converter_on=False (no (2,3) winding wired in — the
# two-3s guard, master-equation.md:20: never read charge/spin/μ off the scalar
# cage). CrystalEngine is chosen over the Master-Equation engine here because its
# `gamma_bulk()` provides the α-FREE impedance-routed Γ_bulk (Z_eff=√S; NOT the
# α-baked gamma_em_sq at cvr_model.py:364) that T3.3 requires, on the SAME S(A)
# kernel. The bulk branch IS the validated Master-Equation engine (CrystalEngine
# docstring: "the bulk branch IS that validated engine").
from ave.core.crystal_engine import CrystalEngine


def make_cage_engine(
    N: int = 40, *, S_min: float = 1e-3, A_cap: float = 0.999, pml_thickness: int = 4
) -> CrystalEngine:
    """A CrystalEngine driven on its A1-SCALAR BULK branch ONLY (converter_on=False
    ⇒ no (2,3) micro-rotation winding) — the posited-cage host. Same S(A)=√(1−A²)
    kernel as the Master-Equation engine; exposes the α-FREE gamma_bulk()."""
    return CrystalEngine(
        N=N, S_min=S_min, A_cap=A_cap, pml_thickness=pml_thickness, converter_on=False
    )


def posit_saturated_cage(
    eng: CrystalEngine, *, frac: float, sigma: float = 4.0, center=None
) -> float:
    """POSIT a saturated longitudinal-bulk core at strain A=frac (a Gaussian
    dilatation well, CP8 generative-precursor style — but PLANTED, since this is
    the consistency-class POSIT, not self-formation). Returns the interior A_max."""
    if center is None:
        c = eng.N // 2
        center = (c, c, c)
    eng.seed_bulk(center=center, sigma=sigma, frac=frac, helical=False)
    m = eng.interior_mask()
    return float(eng.strain_field()[m].max())


def gamma_bulk_min_on_cage(eng: CrystalEngine) -> dict:
    """Read Γ_bulk on the posited cage via the α-FREE impedance route Z_eff=√S
    (crystal_engine.gamma_bulk(), :455-486). NOT gamma_em_sq (the 1−α bake,
    cvr_model.py:364). Returns {gamma_min, gamma_mean, frac_short} on the
    PML-excluded interior (A-Rule 10)."""
    return eng.gamma_bulk()


def breathing_kick_cage(
    eng: CrystalEngine,
    *,
    frac: float,
    core_sigma: float,
    kick_width: float = 2.0,
    kick_amp: float = 0.01,
    center=None,
) -> int:
    """Posit a saturated core, then apply a RADIAL-SHELL BREATHING velocity kick
    (∂_t V on the wall, NO monopole DC) to excite the bound longitudinal breathing
    eigenmode. A pure monopole/DC kick excites only the slow continuum-relaxation
    (an FFT-bin-1 artifact, NOT a mode); the shell-breathing kick is what couples
    to the discrete bound oscillation. Returns the off-center probe index (an
    antinode at r≈core_sigma, PML-excluded). converter_on=False (A1 scalar only)."""
    cx = eng.N // 2
    if center is None:
        center = (cx, cx, cx)
    eng.seed_bulk(center=center, sigma=core_sigma, frac=frac, helical=False)
    i, j, k = np.indices((eng.N, eng.N, eng.N))
    r = np.sqrt((i - center[0]) ** 2 + (j - center[1]) ** 2 + (k - center[2]) ** 2)
    shell = (r - core_sigma) * np.exp(-((r - core_sigma) ** 2) / (2.0 * kick_width**2))
    # V_prev = V − amp·shell ⇒ ∂_t V ≈ +amp·shell/dt: a breathing velocity kick
    eng.V_prev = eng.V - kick_amp * shell
    probe_off = int(round(core_sigma))
    return int(min(cx + probe_off, eng.N - eng.pml_thickness - 1))


def record_breathing_dVdt(eng: CrystalEngine, probe_idx: int, n_steps: int) -> np.ndarray:
    """Evolve n_steps and record ∂_t V at the off-center antinode (the L-state of
    the bulk reactance pair, CP6; DC-free — kills the slow core-offset relaxation
    component so the breathing eigenmode is the resolvable signal)."""
    p = probe_idx
    dV = np.empty(n_steps, dtype=np.float64)
    for n in range(n_steps):
        v_before = float(eng.V[p, p, p])
        eng.step()
        dV[n] = (float(eng.V[p, p, p]) - v_before) / eng.dt
    return dV


def cutoff_eigenfrequency(eng: CrystalEngine, dVdt: np.ndarray) -> dict:
    """Extract the bound-mode cutoff eigenfrequency ω_cutoff from the breathing
    ∂_t V time-series: the dominant rfft tone (excluding DC). Returns ω_cutoff
    (rad/time), the FFT bin index (ipk; >1 ⇒ NOT the bin-1 slow-relaxation
    artifact), the peak/mean spectral ratio (discreteness ⇒ gapped bound mode),
    the FWHM linewidth → Q_linewidth, and the zero-crossing count (oscillation
    witness). α-FREE: pure rfft of the cold/finite dynamics — NO Q_TANK, NO
    M.ELECTRON, NO gamma_em_sq routing."""
    s = dVdt - dVdt.mean()
    spec = np.abs(np.fft.rfft(s * np.hanning(len(s))))
    freqs = np.fft.rfftfreq(len(s), d=1.0)  # cycles per step
    ipk = 1 + int(np.argmax(spec[1:]))
    f_peak = float(freqs[ipk])
    omega_cutoff = 2.0 * np.pi * f_peak / eng.dt
    peak_mean = float(spec[ipk] / spec[1:].mean())
    # FWHM linewidth → Q = f0 / Δf
    half = spec[ipk] / np.sqrt(2.0)
    lo = ipk
    while lo > 1 and spec[lo] > half:
        lo -= 1
    hi = ipk
    while hi < len(spec) - 1 and spec[hi] > half:
        hi += 1
    fwhm_bins = hi - lo
    fwhm_f = fwhm_bins * (freqs[1] - freqs[0])
    q_linewidth = f_peak / fwhm_f if fwhm_f > 0 else float("inf")
    zero_crossings = int(np.sum(np.diff(np.sign(s)) != 0))
    return {
        "omega_cutoff": float(omega_cutoff),
        "ipk": int(ipk),
        "peak_mean": peak_mean,
        "fwhm_bins": int(fwhm_bins),
        "q_linewidth": float(q_linewidth),
        "zero_crossings": zero_crossings,
    }


def ringdown_Q(eng: CrystalEngine, dVdt: np.ndarray, omega0: float) -> dict:
    """Cold/α-FREE Q from the breathing-mode ENVELOPE ring-down: fit an exponential
    to |Hilbert(∂_t V)| after the initial transient → decay time τ → Q=ω₀·τ/2. If
    the envelope does NOT decay (lossless reactive cage), τ=∞ ⇒ Q=∞ (reported
    honestly). α-FREE by construction: the decay rate is read from the cold
    dynamics, NEVER from Q_TANK (cvr_model.py:72=1/α) or the ELECTRON instance."""
    s = dVdt - dVdt.mean()
    try:
        from scipy.signal import hilbert

        env = np.abs(hilbert(s))
    except ImportError:  # pragma: no cover — scipy is a hard dep here
        env = np.abs(s)
    t = np.arange(len(env)) * eng.dt
    i0 = int(0.2 * len(env))  # skip the launch transient
    seg_e, seg_t = env[i0:], t[i0:]
    msk = seg_e > seg_e.max() * 0.1
    if msk.sum() < 50:
        return {"tau": float("inf"), "Q_ringdown": float("inf")}
    slope = float(np.polyfit(seg_t[msk], np.log(seg_e[msk] + 1e-30), 1)[0])
    if slope >= 0:
        return {"tau": float("inf"), "Q_ringdown": float("inf")}
    tau = -1.0 / slope
    return {"tau": float(tau), "Q_ringdown": float(omega0 * tau / 2.0)}


def cage_persistence_trace(
    eng: CrystalEngine, n_steps: int, *, record_every: int = 1
) -> dict:
    """Zero-drive: evolve the posited cage with NO drive for n_steps; record the
    PML-EXCLUDED interior peak |V| each step. Returns the trace + the mid-window
    (50–75%) and late-window (75–100%) means — the steady-state persistence
    observable AFTER the initial non-eigen transient sheds (a non-radiating
    standing mode holds; a radiating/decaying one does not). The interior peak (not
    the centroid) is the density-peak observable for a shell-structured field."""
    m = eng.interior_mask()
    amps = np.empty(n_steps, dtype=np.float64)
    for n in range(n_steps):
        eng.step()
        amps[n] = float(np.abs(eng.V[m]).max())
    a0 = float(amps[0])
    mid = amps[int(0.5 * n_steps) : int(0.75 * n_steps)]
    late = amps[int(0.75 * n_steps) :]
    return {
        "amps": amps,
        "amp0": a0,
        "mid_mean": float(mid.mean()),
        "late_mean": float(late.mean()),
        "late_min": float(late.min()),
        "late_over_mid": float(late.mean() / mid.mean()) if mid.mean() else float("inf"),
    }
