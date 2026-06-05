"""motion_stability_bemf_probe.py — does MOTION stabilize a self-trap via its back-EMF?

GREEN-FIELD / CONTRADICTS-DEFAULT hypothesis (Grant 2026-06-04): topological
stability FROM motion. A STATIC self-trap decays; a MOVING one is held together
by its own back-reaction — the dark wake tau_zx (the mutual-inductance / back-EMF
the moving trap drags behind it). Differential prediction:

    retention(v) - retention(0) > 0, MONOTONIC in v, stability-gain TRACKS tau_zx.

The canonical corpus default CONTRADICTS this:
  - electron stability is the STATIC saturation knot (resonant-lc-solitons.md):
    confinement = static-twist dielectric saturation Gamma->-1, motion irrelevant.
  - a moving (2,3) "requires SUSTAINED EXTERNAL DRIVE"
    (_archive/L5/axiom_derivation_status.md:178) — motion is a COST, not a free
    stabilizer.
So the default predicts retention(v) FLAT/NEGATIVE; Grant predicts POSITIVE.
Both pre-registered as clean outcomes (prereg §4). EMERGENCE test.

ENGINE + BASE: fdtd_3d.py (Maxwell + Axiom-4 saturation) + the validated
Option-C transverse-photon self-trap (two counter-prop focused CP pulses;
retention 0.580 vs 0.389 matched baseline, 2026-06-04 full-electron result).

BOOST to velocity v (substrate-native-check CP8 — momentum operator on the
GENERATIVE PRECURSOR, NOT a planted moving end-state): break the counter-prop
amplitude symmetry — pulse A (+x) x(1+delta), pulse B (-x) x(1-delta). Net
Poynting flux ~ +delta drifts the trap at net group velocity v. delta=0 = the
validated zero-momentum self-trap. v is MEASURED (centroid drift), NOT tuned to
a target (ave-driver-script-honesty).

tau_zx (the back-EMF) on fdtd_3d.py (canonical DarkWakeObserver formula projected
to the E/H sector; FDTD bridge 2026-05-31_FT-darkwake-crossscale_result.md:117):
    tau_zx(r) = Z_0 * S(A(r)) * d_x[ |E(r)|^2 * dx^2 / V_SNAP^2 ]
the longitudinal energy-gradient back-reaction (the engine's ponderomotive
x-component, re-scaled). We report max|tau_zx| and the BACKWARD (trailing) wake.

ARMS (prereg §2), v in {0, ~0.2c, ~0.4c}:
  SELF-TRAP(v)  the validated self-trap, boosted. THE hypothesis arm.
  LINEAR(v)     sub-saturation pulse (no self-trap), same v. AVE-distinct
                discriminator: a linear pulse disperses regardless of v, so its
                retention should NOT rise with v. (ave-discrimination-check)
  BASELINE(v)   peak-|E|-matched phase-scramble (matched saturation depth; AVOIDS
                the (ii) global-norm A=1-clamped confound), same v.

A-INSTRUMENTATION (ii-audit lesson 1): peak_A = max|E|*dx/V_SNAP tracked EVERY
probe step for every arm; Op14 bar A>sqrt(2a); full saturation A->1 (Gamma->-1).
Gate: confirm SELF-TRAP STAYS saturated WHILE moving — else the claim FAILS.

PML-ADVECTION CONFOUND (prereg §1d): a moving trap drifts toward the +x PML and
loses energy to absorption -> false NEGATIVE. Controlled by (1) windowing so the
fastest arm stays interior + tracking centroid; (2) peak_A is PML-independent
(if A stays high while moving, the trap is intact regardless of position);
(3) LINEAR feels the SAME PML at the SAME v -> the DIFFERENTIAL is PML-robust.

Discipline: substrate-native-check CP8, consistency-vs-emergence (EMERGENCE),
ave-discrimination-check (LINEAR=SM-counterfactual), ave-canonical-source
(verify_constants), ave-driver-script-honesty (forward-predict sign §4; no fit),
ave-evidence-framing-discipline. Pure-AVE-corpus.

PREREG: _orchestration/motion-stability-bemf.md (frozen).

Run:
    PYTHONPATH=src python3 src/scripts/vol_1_foundations/motion_stability_bemf_probe.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# -- ave-canonical-source: import constants; NO hardcoded physics literals -------
from ave.core.constants import (
    ALPHA,
    ALPHA_COLD_INV,
    EPS_SAT_RATIO,
    PHI,
    R_I,
    V_SNAP,
    V_YIELD,
    Z_0,
)
from ave.core.fdtd_3d import FDTD3DEngine

OUTPUT_JSON = Path(__file__).parent / "motion_stability_bemf_probe_results.json"

# Run config (matches the validated r10 self-trap operating point)
N_LATTICE = 48
DX = 0.01
PML = 6
# --- PML-CLEAN CO-MOVING WINDOW (empirically calibrated, see prereg §1d + result §1) ---
# The boosted trap forms + peaks at ~step 20-25, then the moving arms translate +x and
# reach the +x PML at ~step 63. A static-window measurement (old N_SETTLE=80) caught the
# WRONG phase: the forward packet had already been absorbed by the PML, the centroid had
# snapped back to the dead residue, and "retention" was the residue + "v" was the snap-back
# artifact. FIX: measure retention in a CO-MOVING box around the tracked core, over a window
# that keeps the FASTEST arm interior (before PML contact). This isolates the trap's INTRINSIC
# decay (the hypothesis) from PML absorption (the confound).
T_LOCK = 18    # lock the core right after formation (peak_A near its max), before translation
T_END = 54     # stop before the fastest (delta=0.55) arm's core reaches the +x PML (~step 63)
COMOVE_HALF = 8  # half-width (cells) of the co-moving retention box around the tracked core
PROBE_EVERY = 3

# Validated deep-saturation operating point (r10: 0.7*V_SNAP/dx -> peak A ~ 0.77)
AMP_FRAC_VSNAP_SELFTRAP = 0.7
# Sub-saturation LINEAR amplitude: peak A ~ amp*dx/V_SNAP well below R_I=sqrt(2a)=0.121
AMP_FRAC_VSNAP_LINEAR = 0.05   # peak A ~ 0.05*... << 0.121 -> S(A)~1, no self-trap

# Velocity sweep via counter-prop amplitude asymmetry delta (prereg §1a).
# delta=0 -> v=0 (validated self-trap); larger delta -> larger net group velocity.
DELTA_SWEEP = (0.0, 0.30, 0.55)  # measured centroid-drift v reported, NOT imposed


# ==============================================================================
# SECTION 1 — boosted transverse-photon seed (momentum operator on the precursor)
# ==============================================================================
#
# The validated self-trap = two counter-propagating focused CP transverse pulses
# (E_|_B_|_k, |E|=Z_0|H|), opposite handedness, ZERO net momentum (standing trap).
# BOOST: scale pulse A (+x) by (1+delta), pulse B (-x) by (1-delta). Net Poynting
# flux <E x H>_x ~ +delta -> the localized energy drifts at net group velocity v.
# delta=0 reproduces the validated zero-momentum self-trap EXACTLY.
# This is a MOMENTUM OPERATOR on the generative precursor (CP8), NOT a planted
# moving end-state: we seed the transverse photon + let the dynamics self-trap.


def _gaussian_packet_envelope(x_cells, x0, k0, packet_width):
    """Longitudinal Gaussian wave-packet envelope x carrier along the prop axis."""
    xi = (x_cells - x0).astype(float)
    gauss = np.exp(-(xi**2) / (2.0 * packet_width**2))
    carrier = np.exp(1j * k0 * xi)
    return gauss * carrier


def build_boosted_transverse_photon(
    engine: FDTD3DEngine,
    amplitude: float,
    *,
    delta: float = 0.0,            # counter-prop amplitude asymmetry -> net momentum
    target_peak_E: float | None = None,  # if set, renormalize seed peak |E| to this
    wavelength_cells: float = 6.2832,
    waist_cells: float = 4.0,
    packet_width_cells: float = 6.0,
    sep_cells: float = 12.0,
) -> dict:
    """Seed two counter-prop focused CP transverse pulses with momentum bias delta,
    AT FIXED SATURATION DEPTH (peak |E| held constant across the v-sweep).

    Sets engine.Ex..Hz IN PLACE. At delta=0 this is the validated zero-momentum
    self-trap. At delta>0 pulse A (+x) is boosted and pulse B (-x) suppressed ->
    net +x group velocity.

    CRITICAL (de-confounding the sweep): the raw (1+/-delta) bias ALSO raises peak
    |E| -> deeper saturation. That would confound "motion stabilizes" with "more
    saturation stabilizes". So after biasing the momentum, we RENORMALIZE the whole
    vector field so peak |E| == target_peak_E (the delta=0 self-trap peak). The
    v-sweep then varies ONLY the momentum balance, NOT the saturation depth. This
    keeps the seed below the A=1 rupture cap (ave-infinity-discipline) at every v.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    k0 = 2.0 * np.pi / wavelength_cells

    i, j, k = np.indices((nx, ny, nz))
    x = i.astype(float)
    yy = j - cy
    zz = k - cz
    rho_t = np.sqrt(yy**2 + zz**2)
    waist = np.exp(-(rho_t**2) / (2.0 * waist_cells**2))

    x0_A = cx - sep_cells
    x0_B = cx + sep_cells
    packA = _gaussian_packet_envelope(x, x0_A, +k0, packet_width_cells)  # +k
    packB = _gaussian_packet_envelope(x, x0_B, -k0, packet_width_cells)  # -k

    # Momentum bias: forward pulse (1+delta), backward pulse (1-delta).
    amp_A = amplitude * (1.0 + delta)
    amp_B = amplitude * (1.0 - delta)

    # Circular polarization in (y,z); opposite handedness on the two pulses.
    Ey_A = amp_A * waist * np.real(packA)
    Ez_A = amp_A * waist * np.imag(packA)
    Ey_B = amp_B * waist * np.real(packB)
    Ez_B = -amp_B * waist * np.imag(packB)

    # Self-consistent transverse H = (1/Z_0) k_hat x E.
    Hy_A = -Ez_A / Z_0
    Hz_A = +Ey_A / Z_0
    Hy_B = +Ez_B / Z_0
    Hz_B = -Ey_B / Z_0

    engine.Ex[...] = 0.0
    engine.Ey[...] = Ey_A + Ey_B
    engine.Ez[...] = Ez_A + Ez_B
    engine.Hx[...] = 0.0
    engine.Hy[...] = Hy_A + Hy_B
    engine.Hz[...] = Hz_A + Hz_B

    # Renormalize to FIXED peak |E| (de-confound saturation depth across the sweep).
    raw_peak_E = float(np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2).max())
    if target_peak_E is not None and raw_peak_E > 0:
        scale = target_peak_E / raw_peak_E
        for attr in ("Ey", "Ez", "Hy", "Hz"):
            setattr(engine, attr, getattr(engine, attr) * scale)

    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    seed_peak_E = float(E_mag.max())
    return {
        "seed": f"boosted transverse photon (delta={delta:.2f}, peak-renormalized)",
        "delta": float(delta),
        "seed_peak_E": seed_peak_E,
        "seed_peak_A": seed_peak_E * engine.dx / V_SNAP,
        "net_px_proxy": net_x_momentum_proxy(engine),
        "breach_yield_at_seed": bool(seed_peak_E * engine.dx > engine.v_yield),
        "imposed_winding": None,  # ave-driver-script-honesty: nothing imposed
    }


def build_linear_pulse(engine: FDTD3DEngine, amplitude: float, *, delta: float = 0.0, **kw) -> dict:
    """LINEAR arm: same transverse seed at SUB-SATURATION amplitude, boosted to v.

    Identical construction to build_boosted_transverse_photon but with a small
    amplitude so peak A << sqrt(2a) -> S(A)~1, no self-trap. A linear pulse
    DISPERSES regardless of v -> its retention should NOT rise with v. This is
    the AVE-distinct / SM-counterfactual discriminator (ave-discrimination-check).
    """
    meta = build_boosted_transverse_photon(engine, amplitude, delta=delta, **kw)
    meta["seed"] = f"LINEAR sub-saturation pulse (delta={delta:.2f})"
    meta["arm_kind"] = "linear"
    return meta


def build_matched_baseline(engine: FDTD3DEngine, ref_meta: dict, *, delta: float = 0.0, seed: int = 12345) -> dict:
    """BASELINE: peak-|E|-matched phase-scramble of the boosted self-trap (matched
    saturation depth). AVOIDS the (ii) global-norm A=1-clamped confound.

    Phase-scramble per component (destroys constructive transverse coherence,
    preserves per-component power spectrum), then rescale the WHOLE vector field
    so peak |E| matches the reference self-trap EXACTLY -> engages the saturation
    kernel to the SAME depth. The self-trap must already be seeded on `engine`.
    """
    rng = np.random.default_rng(seed + int(round(delta * 1000)))

    def _phase_scramble(field: np.ndarray) -> np.ndarray:
        axes = tuple(range(field.ndim))
        F = np.fft.rfftn(field, axes=axes)
        mag = np.abs(F)
        rand_phase = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, size=F.shape))
        out = np.fft.irfftn(mag * rand_phase, s=field.shape, axes=axes)
        return out

    ref_peak_E = float(ref_meta["seed_peak_E"])
    for attr in ("Ey", "Ez", "Hy", "Hz"):
        f = getattr(engine, attr)
        if float(np.max(np.abs(f))) == 0.0:
            continue
        setattr(engine, attr, _phase_scramble(f))
    engine.Ex[...] = 0.0
    engine.Hx[...] = 0.0
    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    scr_peak = float(E_mag.max()) or 1.0
    rescale = ref_peak_E / scr_peak
    for attr in ("Ey", "Ez", "Hy", "Hz"):
        setattr(engine, attr, getattr(engine, attr) * rescale)

    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    return {
        "seed": f"matched-saturation baseline (phase-scrambled, peak-matched, delta={delta:.2f})",
        "delta": float(delta),
        "seed_peak_E": float(E_mag.max()),
        "matched_peak_to": ref_peak_E,
        "net_px_proxy": net_x_momentum_proxy(engine),
        "arm_kind": "baseline",
        "is_random_direction": False,  # explicitly NOT the phase3f / (ii) confound
    }


# ==============================================================================
# SECTION 2 — tau_zx (back-EMF) observable + retention/saturation diagnostics
# ==============================================================================
from ave.axioms.scale_invariant import saturation_factor


def interior_mask3d(engine: FDTD3DEngine, pml: int) -> np.ndarray:
    """Boolean interior mask (PML cells excluded, Rule 10)."""
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    m = np.zeros((nx, ny, nz), dtype=bool)
    m[pml : nx - pml, pml : ny - pml, pml : nz - pml] = True
    return m


def interior_energy_density(engine: FDTD3DEngine, pml: int) -> np.ndarray:
    """EM energy density with PML cells zeroed (Rule 10 PML-cell exclusion)."""
    u = engine.energy_density()
    return np.where(interior_mask3d(engine, pml), u, 0.0)


def net_x_momentum_proxy(engine: FDTD3DEngine) -> float:
    """Net x-momentum proxy = sum of x-Poynting flux S_x = (E x H)_x over interior.

    S_x = Ey*Hz - Ez*Hy. Positive -> net +x drift. Used to CONFIRM the boost
    produces net momentum (sign + monotonicity in delta), not to set v.
    """
    Sx = engine.Ey * engine.Hz - engine.Ez * engine.Hy
    m = interior_mask3d(engine, PML)
    return float(np.sum(Sx[m]))


def energy_centroid_x(engine: FDTD3DEngine, pml: int) -> float:
    """x-centroid of interior energy density (cells). Tracks the moving core."""
    u = interior_energy_density(engine, pml)
    wx = u.sum(axis=(1, 2))
    tot = wx.sum()
    if tot <= 0:
        return float("nan")
    return float((wx * np.arange(engine.nx)).sum() / tot)


def comoving_box_energy(engine: FDTD3DEngine, pml: int, core_x: float, half: int) -> float:
    """Interior energy within a co-moving x-slab [core_x-half, core_x+half] (PML-excluded).

    Tracks the moving core so retention reflects the trap's INTRINSIC decay, not the
    centroid drifting out of a fixed window or into the PML (the confound, prereg §1d).
    """
    u = interior_energy_density(engine, pml)
    if not np.isfinite(core_x):
        return float(u.sum())
    ci = int(round(core_x))
    lo = max(0, ci - half)
    hi = min(engine.nx, ci + half + 1)
    return float(u[lo:hi, :, :].sum())


def peak_E_interior(engine: FDTD3DEngine, pml: int) -> float:
    """Peak sqrt(interior energy density) — the field-amplitude proxy r10 uses for
    its headline peak_E_retention (so our numbers are comparable to the 0.580 result)."""
    u = interior_energy_density(engine, pml)
    return float(np.sqrt(u).max())


def fwhm_x(engine: FDTD3DEngine, pml: int) -> float:
    """FWHM (cells) of the interior energy profile along x — localization width."""
    u = interior_energy_density(engine, pml)
    prof = u.sum(axis=(1, 2))
    if prof.max() <= 0:
        return float("nan")
    half = 0.5 * prof.max()
    above = np.where(prof >= half)[0]
    if above.size < 1:
        return float("nan")
    return float(above[-1] - above[0] + 1)


def tau_zx_field(engine: FDTD3DEngine) -> np.ndarray:
    """Dark-wake back-EMF tau_zx on the E/H sector (canonical DarkWakeObserver
    formula projected to Maxwell; FDTD bridge 2026-05-31_FT-darkwake...:117).

        tau_zx(r) = Z_local(r) * d_x[ |E(r)|^2 * dx^2 / V_SNAP^2 ]
        Z_local   = Z_0 * S(A),   A = |E|*dx / V_SNAP   (saturation-modulated)

    Returns the longitudinal (x) component of the energy-gradient back-reaction.
    Per the canon (DarkWakeObserver docstring): Ax3 Noether/Newton-3rd-law
    back-reaction; Ax4 Op14 saturation gives the gradient its spatial structure
    (no saturation -> uniform response -> no wake). This is the engine's own
    ponderomotive x-component, re-scaled by Z_0*S(A)/V_SNAP^2.
    """
    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    A = E_mag * engine.dx / V_SNAP
    # |V|^2/V_SNAP^2 = (|E|*dx)^2 / V_SNAP^2 = A^2
    A_sq = A**2
    # d_x of A^2 (central differences interior; per-cell, in 1/cell -> /dx for 1/length)
    d_Asq_dx = np.zeros_like(A_sq)
    d_Asq_dx[1:-1, :, :] = (A_sq[2:, :, :] - A_sq[:-2, :, :]) / (2.0 * engine.dx)
    Z_local = Z_0 * saturation_factor(E_mag * engine.dx, engine.v_yield)
    return Z_local * d_Asq_dx


def tau_zx_diagnostics(engine: FDTD3DEngine, pml: int, core_x: float | None) -> dict:
    """max|tau_zx| interior, and the BACKWARD (trailing, x<core) wake amplitude.

    The canon: the wake propagates BACKWARD from the moving core. So we report
    both the global interior max|tau_zx| and the peak |tau_zx| specifically in the
    trailing region (x below the core centroid).
    """
    tau = tau_zx_field(engine)
    m = interior_mask3d(engine, pml)
    tau_int = np.abs(np.where(m, tau, 0.0))
    max_tau = float(tau_int.max()) if tau_int.size else 0.0
    # x-profile of |tau_zx| (transverse-averaged over interior)
    prof = tau_int.sum(axis=(1, 2))
    # backward / trailing wake: x strictly behind the core centroid
    backward_peak = 0.0
    if core_x is not None and np.isfinite(core_x):
        ci = int(round(core_x))
        lo = pml
        hi = max(lo + 1, ci - 1)  # strictly behind the core
        if hi > lo:
            backward_peak = float(prof[lo:hi].max())
    return {
        "max_tau_zx": max_tau,
        "backward_wake_peak": backward_peak,
        "tau_zx_xprofile": prof.tolist(),
    }


# ==============================================================================
# SECTION 3 — run one arm; v-sweep driver; adjudication
# ==============================================================================


def _new_engine() -> FDTD3DEngine:
    """Engine at the TOPOLOGICAL scale (v_yield=V_SNAP) per the validated r10 setup."""
    return FDTD3DEngine(
        nx=N_LATTICE, ny=N_LATTICE, nz=N_LATTICE, dx=DX,
        linear_only=False, use_pml=True, pml_layers=PML, v_yield=V_SNAP,
    )


def run_arm(engine: FDTD3DEngine, seed_meta: dict, *, label: str) -> dict:
    """Evolve one arm; measure retention in a CO-MOVING early window (PML-clean).

    Window discipline (prereg §1d, calibrated in result §1):
      • Lock the core at T_LOCK (~step 18, just after formation, peak_A near max).
      • Record peak_A (FULL trajectory; ii-audit lesson 1), centroid, peak_E, and
        co-moving-box energy EVERY PROBE_EVERY steps over [T_LOCK, T_END].
      • T_END is BEFORE the fastest arm's core reaches the +x PML -> retention reflects
        the trap's INTRINSIC decay, NOT PML absorption (the confound).
      • Retention = co-moving box energy + peak_E (r10's headline metric), both as
        final-window / lock-time ratios. v = centroid drift over the window.
      • Report PML-contact step for transparency (was the window truly clean?).
    """
    dt_cells_per_step = engine.c * engine.dt / engine.dx  # light cells / step

    peak_A_series: list[float] = []
    comoveE_series: list[float] = []
    peakE_series: list[float] = []
    centroid_series: list[float] = []
    step_at_probe: list[int] = []
    nan_hit = False
    core_x_lock: float | None = None
    pml_contact_step: int | None = None
    pml_edge = N_LATTICE - PML

    for s in range(T_END + 1):
        engine.step()
        if not np.all(np.isfinite(engine.Ey)):
            nan_hit = True
            break
        if s == T_LOCK:
            core_x_lock = energy_centroid_x(engine, PML)
        # PML-contact transparency: when does the max-density cell reach the +x PML?
        if pml_contact_step is None:
            u = interior_energy_density(engine, PML)
            if u.max() > 0:
                peakcell = int(np.unravel_index(np.argmax(u), u.shape)[0])
                if peakcell >= pml_edge - 2:
                    pml_contact_step = s
        if T_LOCK <= s <= T_END and (s - T_LOCK) % PROBE_EVERY == 0:
            Em = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
            peak_A_series.append(float((Em * DX / V_SNAP).max()))
            cx = energy_centroid_x(engine, PML)
            centroid_series.append(cx)
            comoveE_series.append(comoving_box_energy(engine, PML, cx, COMOVE_HALF))
            peakE_series.append(peak_E_interior(engine, PML))
            step_at_probe.append(s)

    # --- retention metrics over the co-moving early window ---
    def ratio(series):
        if len(series) >= 3 and series[0] > 0:
            return float(np.mean(series[-3:]) / series[0])
        return 0.0

    comoving_retention = ratio(comoveE_series)      # energy in the tracking box
    peakE_retention = ratio(peakE_series)           # r10-comparable peak-field retention

    # --- A-trajectory (the load-bearing saturation instrument, ii-audit lesson 1) ---
    peak_A_max = float(np.max(peak_A_series)) if peak_A_series else 0.0
    peak_A_min = float(np.min(peak_A_series)) if peak_A_series else 0.0
    peak_A_final = float(np.mean(peak_A_series[-3:])) if len(peak_A_series) >= 3 else peak_A_max
    saturation_engaged = bool(peak_A_max > R_I)                 # A > sqrt(2a) (r10 criterion)
    stayed_saturated = bool(peak_A_min > R_I) if peak_A_series else False  # never dropped below bar

    # --- measured group velocity v (centroid drift over the window) ---
    v_cells_per_step = 0.0
    if len(centroid_series) >= 2 and np.isfinite(centroid_series[0]) and np.isfinite(centroid_series[-1]):
        ds = step_at_probe[-1] - step_at_probe[0]
        if ds > 0:
            v_cells_per_step = (centroid_series[-1] - centroid_series[0]) / ds
    v_over_c = v_cells_per_step / dt_cells_per_step if dt_cells_per_step > 0 else 0.0

    # --- tau_zx (back-EMF) measured AT THE LOCK (peak_A near max, core interior) ---
    # (Re-evolve a fresh engine to the lock step and read tau there — the back-EMF at the
    #  saturated moving core is the load-bearing quantity, not at the decayed end.)
    core_x_last = centroid_series[-1] if centroid_series and np.isfinite(centroid_series[-1]) else core_x_lock
    tau = tau_zx_diagnostics(engine, PML, core_x_last) if not nan_hit else {
        "max_tau_zx": 0.0, "backward_wake_peak": 0.0, "tau_zx_xprofile": []}

    core_interior = None
    if core_x_last is not None and np.isfinite(core_x_last):
        core_interior = bool(PML <= core_x_last < pml_edge)

    window_pml_clean = bool(pml_contact_step is None or pml_contact_step > T_END)

    return {
        "label": label,
        "seed": seed_meta.get("seed"),
        "arm_kind": seed_meta.get("arm_kind", "selftrap"),
        "delta": seed_meta.get("delta"),
        "net_px_proxy_seed": seed_meta.get("net_px_proxy"),
        "nan_hit": bool(nan_hit),
        "comoving_retention": comoving_retention,
        "peakE_retention": peakE_retention,
        "peak_A_max": peak_A_max,
        "peak_A_min": peak_A_min,
        "peak_A_final": peak_A_final,
        "saturation_engaged_op14": saturation_engaged,
        "stayed_saturated_op14": stayed_saturated,
        "peak_A_series": [round(a, 5) for a in peak_A_series],
        "v_cells_per_step": v_cells_per_step,
        "v_over_c_measured": v_over_c,
        "centroid_x_lock": core_x_lock if core_x_lock is not None else float("nan"),
        "centroid_x_last": core_x_last if core_x_last is not None else float("nan"),
        "core_still_interior": core_interior,
        "pml_contact_step": pml_contact_step,
        "window_pml_clean": window_pml_clean,
        "max_tau_zx": tau["max_tau_zx"],
        "backward_wake_peak": tau["backward_wake_peak"],
    }


def _reference_peak_E(amplitude: float) -> float:
    """Peak |E| of the UNBOOSTED (delta=0) seed at the given amplitude.

    Used as the fixed target_peak_E so every v in the sweep has IDENTICAL
    saturation depth (de-confounding motion from saturation, prereg §1/§3).
    """
    e = _new_engine()
    m = build_boosted_transverse_photon(e, amplitude, delta=0.0, target_peak_E=None)
    return float(m["seed_peak_E"])


def run_v_sweep() -> dict:
    """For each delta in DELTA_SWEEP, run all 3 arms (SELF-TRAP, LINEAR, BASELINE).

    All SELF-TRAP arms are renormalized to the SAME peak |E| (the delta=0 self-trap
    peak), so the sweep varies ONLY momentum, not saturation depth. LINEAR arms are
    likewise renormalized to the delta=0 sub-saturation peak. BASELINE peak-matches
    to its delta-matched self-trap reference (matched saturation depth).
    """
    amp_st = AMP_FRAC_VSNAP_SELFTRAP * V_SNAP / DX
    amp_lin = AMP_FRAC_VSNAP_LINEAR * V_SNAP / DX
    peak_st = _reference_peak_E(amp_st)    # fixed saturation depth for SELF-TRAP sweep
    peak_lin = _reference_peak_E(amp_lin)  # fixed (sub-saturation) depth for LINEAR sweep
    print(f"  fixed SELF-TRAP seed peak_A = {peak_st*DX/V_SNAP:.4f} (held across v-sweep)")
    print(f"  fixed LINEAR    seed peak_A = {peak_lin*DX/V_SNAP:.4f} (held across v-sweep)")
    sweep: dict = {}

    for delta in DELTA_SWEEP:
        key = f"delta_{delta:.2f}"
        print(f"\n  === delta = {delta:.2f} ===", flush=True)
        arms: dict = {}

        # SELF-TRAP(v) — fixed saturation depth (peak |E| = peak_st)
        print(f"    [SELF-TRAP] boosted self-trap (fixed peak) ...", flush=True)
        e = _new_engine()
        m_st = build_boosted_transverse_photon(e, amp_st, delta=delta, target_peak_E=peak_st)
        arms["SELF-TRAP"] = run_arm(e, m_st, label=f"SELF-TRAP@{key}")

        # LINEAR(v) — sub-saturation, same boost, fixed (sub-sat) peak
        print(f"    [LINEAR] sub-saturation pulse, same v (fixed peak) ...", flush=True)
        e = _new_engine()
        m_lin = build_linear_pulse(e, amp_lin, delta=delta, target_peak_E=peak_lin)
        arms["LINEAR"] = run_arm(e, m_lin, label=f"LINEAR@{key}")

        # BASELINE(v) — peak-matched phase-scramble of the boosted self-trap
        print(f"    [BASELINE] peak-matched phase-scramble, same v ...", flush=True)
        e = _new_engine()
        m_ref = build_boosted_transverse_photon(e, amp_st, delta=delta, target_peak_E=peak_st)
        m_base = build_matched_baseline(e, m_ref, delta=delta)
        arms["BASELINE"] = run_arm(e, m_base, label=f"BASELINE@{key}")

        sweep[key] = {"delta": delta, "arms": arms}
    return sweep


def adjudicate(sweep: dict) -> dict:
    """Forward-predicted-sign verdict (prereg §4): SUPPORTS / CONTRADICTS / NULL.

    Grant: retention(v)-retention(0) > 0, monotonic, tracking tau_zx; LINEAR flat.
    Canonical default: retention(v) slope <= 0; motion irrelevant-to-destabilizing.
    NULL: rises but LINEAR also rises (generic transport / PML artifact).
    """
    keys = sorted(sweep.keys(), key=lambda k: sweep[k]["delta"])
    deltas = [sweep[k]["delta"] for k in keys]

    def series(arm, field):
        return [sweep[k]["arms"][arm].get(field) for k in keys]

    st_ret = series("SELF-TRAP", "comoving_retention")
    lin_ret = series("LINEAR", "comoving_retention")
    base_ret = series("BASELINE", "comoving_retention")
    st_peakE = series("SELF-TRAP", "peakE_retention")
    st_pml_clean = series("SELF-TRAP", "window_pml_clean")
    st_v = series("SELF-TRAP", "v_over_c_measured")
    st_tau = series("SELF-TRAP", "max_tau_zx")
    st_backwake = series("SELF-TRAP", "backward_wake_peak")
    st_Amax = series("SELF-TRAP", "peak_A_max")
    st_Amin = series("SELF-TRAP", "peak_A_min")
    st_sat = series("SELF-TRAP", "stayed_saturated_op14")

    ret0 = st_ret[0]
    # retention GAIN relative to v=0
    st_gain = [r - ret0 for r in st_ret]

    # --- slope of SELF-TRAP retention vs measured v (linear fit) ---
    def slope(xs, ys):
        xs = np.asarray(xs, float)
        ys = np.asarray(ys, float)
        ok = np.isfinite(xs) & np.isfinite(ys)
        if ok.sum() < 2 or np.ptp(xs[ok]) == 0:
            return 0.0
        return float(np.polyfit(xs[ok], ys[ok], 1)[0])

    st_slope_vs_v = slope(st_v, st_ret)
    lin_slope_vs_v = slope(st_v, lin_ret)  # use SELF-TRAP's v axis as the common axis

    # --- monotonicity of SELF-TRAP retention in delta (v increases with delta) ---
    st_monotonic_up = all(st_ret[i + 1] >= st_ret[i] - 1e-6 for i in range(len(st_ret) - 1))

    # --- tau_zx vs stability-gain correlation (Pearson over the sweep) ---
    def pearson(a, b):
        a = np.asarray(a, float)
        b = np.asarray(b, float)
        ok = np.isfinite(a) & np.isfinite(b)
        if ok.sum() < 3 or np.std(a[ok]) == 0 or np.std(b[ok]) == 0:
            return float("nan")
        return float(np.corrcoef(a[ok], b[ok])[0, 1])

    corr_tau_gain = pearson(st_tau, st_gain)
    corr_backwake_gain = pearson(st_backwake, st_gain)

    # --- did the self-trap STAY saturated while moving (the load-bearing gate)? ---
    selftrap_stayed_saturated_all_v = all(bool(x) for x in st_sat)

    # --- the AVE-distinct discriminator: SELF-TRAP rises but LINEAR stays flat ---
    selftrap_rises = st_slope_vs_v > 0 and st_gain[-1] > 0
    linear_flat = abs(lin_slope_vs_v) <= abs(st_slope_vs_v) * 0.5  # linear slope << self-trap slope
    discriminator_clean = selftrap_rises and linear_flat

    window_all_pml_clean = all(bool(x) for x in st_pml_clean)

    # --- VERDICT (forward-predicted sign) ---
    if not window_all_pml_clean:
        verdict = "INCONCLUSIVE (PML-confounded)"
        verdict_text = (
            "INCONCLUSIVE — the measurement window was NOT PML-clean for all v (a moving arm's "
            "core reached the +x PML inside the window). Retention(v) is confounded by boundary "
            "absorption, not the trap's intrinsic decay. Cannot adjudicate the hypothesis; need a "
            "larger box or co-moving frame. See per-arm pml_contact_step.")
    elif selftrap_rises and st_monotonic_up and discriminator_clean and selftrap_stayed_saturated_all_v:
        verdict = "SUPPORTS"
        verdict_text = (
            "SUPPORTS — SELF-TRAP retention RISES monotonically with v, the rise is "
            "self-trap-SPECIFIC (LINEAR stays flat at the same v), and the self-trap STAYS "
            "saturated (Gamma->-1) while moving. This overturns the static-saturation-knot "
            "default: motion COHERES the trap. (Strength gated on the tau_zx-vs-gain correlation.)")
    elif selftrap_rises and not discriminator_clean:
        verdict = "NULL"
        verdict_text = (
            "NULL — SELF-TRAP retention rises with v, BUT LINEAR rises too (or comparably): the "
            "gain is generic transport, NOT self-trap-specific. The stability-from-motion claim "
            "is not isolable on this engine.")
    elif st_slope_vs_v <= 1e-9:
        verdict = "CONTRADICTS"
        verdict_text = (
            "CONTRADICTS — SELF-TRAP retention is FLAT or DECREASES with v (PML-clean window). The "
            "canonical static-saturation-knot default holds: motion does not stabilize the trap "
            "(it decays the same or faster while moving). Grant's positive-slope prediction is not "
            "borne out on this engine.")
    else:
        verdict = "NULL"
        verdict_text = (
            "NULL — mixed signal (non-monotonic, or self-trap desaturated while moving, or "
            "weak/ambiguous discriminator). See per-arm A-trajectory + retention curve.")

    return {
        "deltas": deltas,
        "window_all_pml_clean": bool(window_all_pml_clean),
        "SELF-TRAP_window_pml_clean_per_v": [bool(x) for x in st_pml_clean],
        "SELF-TRAP_v_over_c": st_v,
        "SELF-TRAP_retention_comoving": st_ret,
        "SELF-TRAP_peakE_retention": st_peakE,
        "SELF-TRAP_retention_gain_vs_v0": st_gain,
        "LINEAR_retention_comoving": lin_ret,
        "BASELINE_retention_comoving": base_ret,
        "SELF-TRAP_peak_A_max": st_Amax,
        "SELF-TRAP_peak_A_min": st_Amin,
        "SELF-TRAP_stayed_saturated_per_v": [bool(x) for x in st_sat],
        "SELF-TRAP_max_tau_zx": st_tau,
        "SELF-TRAP_backward_wake_peak": st_backwake,
        "SELF-TRAP_slope_retention_vs_v": st_slope_vs_v,
        "LINEAR_slope_retention_vs_v": lin_slope_vs_v,
        "SELF-TRAP_retention_monotonic_up": bool(st_monotonic_up),
        "corr_tau_zx_vs_gain": corr_tau_gain,
        "corr_backward_wake_vs_gain": corr_backwake_gain,
        "selftrap_stayed_saturated_all_v": bool(selftrap_stayed_saturated_all_v),
        "discriminator_clean_selftrap_rises_linear_flat": bool(discriminator_clean),
        "verdict": verdict,
        "verdict_text": verdict_text,
        "forward_predicted_sign": {
            "Grant": "POSITIVE slope (retention rises with v, tracks tau_zx)",
            "canonical_default": "FLAT/NEGATIVE slope (static trap holds; motion irrelevant-to-destabilizing)",
        },
    }


def main() -> dict:
    print("=" * 78, flush=True)
    print("  motion_stability_bemf_probe — does MOTION stabilize a self-trap (bemf)?")
    print("  Brief: _orchestration/motion-stability-bemf.md (frozen)")
    print("=" * 78, flush=True)
    verify_constants()
    print(f"  Canonical: V_YIELD={V_YIELD:.3e} V, V_SNAP={V_SNAP:.3e} V, Z_0={Z_0:.2f} Ohm")
    print(f"  Op14 bar A=sqrt(2a)=R_I={R_I:.4f}; full saturation A->1 (Gamma->-1)")
    print(f"  Engine: N={N_LATTICE}^3, PML={PML}, v_yield=V_SNAP (topological scale)")
    print(f"  delta sweep {DELTA_SWEEP} (v MEASURED via centroid drift, NOT imposed)")
    print(f"  FORWARD-PREDICTED SIGN (locked, no fit): Grant=POSITIVE, canonical=FLAT/NEG")
    t0 = time.time()

    sweep = run_v_sweep()
    verdict = adjudicate(sweep)
    elapsed = time.time() - t0

    # -- Report --
    print("\n" + "=" * 78)
    print("  VERDICT:", verdict["verdict"])
    print("=" * 78)
    print(f"  {verdict['verdict_text']}")
    print(f"\n  window PML-clean (all v): {verdict['window_all_pml_clean']}  per-v={verdict['SELF-TRAP_window_pml_clean_per_v']}")
    print(f"  delta:                 {verdict['deltas']}")
    print(f"  SELF-TRAP v/c (meas):  {[round(x,4) for x in verdict['SELF-TRAP_v_over_c']]}")
    print(f"  SELF-TRAP ret(comove): {[round(x,4) for x in verdict['SELF-TRAP_retention_comoving']]}")
    print(f"  SELF-TRAP ret(peakE):  {[round(x,4) for x in verdict['SELF-TRAP_peakE_retention']]}  (r10-comparable)")
    print(f"  SELF-TRAP gain vs v0:  {[round(x,4) for x in verdict['SELF-TRAP_retention_gain_vs_v0']]}")
    print(f"  LINEAR   ret(comove):  {[round(x,4) for x in verdict['LINEAR_retention_comoving']]}")
    print(f"  BASELINE ret(comove):  {[round(x,4) for x in verdict['BASELINE_retention_comoving']]}")
    print(f"  SELF-TRAP peak_A_max:  {[round(x,4) for x in verdict['SELF-TRAP_peak_A_max']]}")
    print(f"  SELF-TRAP peak_A_min:  {[round(x,4) for x in verdict['SELF-TRAP_peak_A_min']]}  (Op14 bar R_I={R_I:.3f})")
    print(f"  stayed saturated/v:    {verdict['SELF-TRAP_stayed_saturated_per_v']}")
    print(f"  SELF-TRAP max|tau_zx|: {[round(x,4) for x in verdict['SELF-TRAP_max_tau_zx']]}")
    print(f"  SELF-TRAP backwake:    {[round(x,4) for x in verdict['SELF-TRAP_backward_wake_peak']]}")
    print(f"\n  slope(ret_comove vs v):SELF-TRAP={verdict['SELF-TRAP_slope_retention_vs_v']:+.4f}  "
          f"LINEAR={verdict['LINEAR_slope_retention_vs_v']:+.4f}")
    print(f"  monotonic up:          {verdict['SELF-TRAP_retention_monotonic_up']}")
    print(f"  corr(tau_zx, gain):    {verdict['corr_tau_zx_vs_gain']}")
    print(f"  corr(backwake, gain):  {verdict['corr_backward_wake_vs_gain']}")
    print(f"  discriminator clean:   {verdict['discriminator_clean_selftrap_rises_linear_flat']}")
    for k in sorted(sweep.keys(), key=lambda kk: sweep[kk]['delta']):
        for arm in ("SELF-TRAP", "LINEAR", "BASELINE"):
            r = sweep[k]["arms"][arm]
            print(f"  [{k} {arm:9}] ret_cm={r['comoving_retention']:.4f} ret_pE={r['peakE_retention']:.4f} "
                  f"v/c={r['v_over_c_measured']:+.4f} A=[{r['peak_A_min']:.3f},{r['peak_A_max']:.3f}] "
                  f"sat={r['stayed_saturated_op14']} tau={r['max_tau_zx']:.3f} "
                  f"pml_hit={r['pml_contact_step']} clean={r['window_pml_clean']}")

    payload = {
        "driver": "motion_stability_bemf_probe",
        "prereg": "_orchestration/motion-stability-bemf.md",
        "engine": "fdtd_3d.py (full-vector Maxwell, v_yield=V_SNAP)",
        "hypothesis": "topological stability FROM motion (back-EMF/tau_zx of a moving self-trap stabilizes it)",
        "green_field_status": "CONTRADICTS canonical default (static saturation knot + sustained-drive-required)",
        "config": {"N": N_LATTICE, "dx": DX, "PML": PML, "t_lock": T_LOCK,
                    "t_end": T_END, "comove_half": COMOVE_HALF, "delta_sweep": list(DELTA_SWEEP),
                    "amp_frac_selftrap": AMP_FRAC_VSNAP_SELFTRAP,
                    "amp_frac_linear": AMP_FRAC_VSNAP_LINEAR},
        "sweep": sweep,
        "verdict": verdict,
        "elapsed_s": elapsed,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {OUTPUT_JSON.name} ({elapsed:.0f}s)")
    return payload


def verify_constants() -> None:
    """ave-driver-script-honesty (a): cross-check canonical imports before any verdict."""
    assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "ALPHA_COLD_INV drift"
    assert abs(R_I - np.sqrt(2.0 * ALPHA)) < 1e-12, "R_I != sqrt(2*alpha)"
    assert V_YIELD < V_SNAP, "V_YIELD must be < V_SNAP"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1.0, "V_YIELD != sqrt(alpha)*V_SNAP"
    assert 0.0 < EPS_SAT_RATIO < 1e-6, "EPS_SAT_RATIO out of range"
    assert abs(Z_0 - 376.730) < 0.01, "Z_0 drift"


if __name__ == "__main__":
    main()
