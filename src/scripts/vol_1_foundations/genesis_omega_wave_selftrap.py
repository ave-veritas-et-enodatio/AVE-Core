"""
GENESIS (canonical) — self-trap the ω-shear photon.

Prereg (FROZEN): research/2026-06-06_genesis-omega-wave-prereg.md

THE QUESTION (Grant re-aim, audit §8): does the CANONICAL photon — the transverse
Cosserat-ω shear WAVE (u=0, ω≠0, pure ω, sub-saturation, Z-matched;
photon-identification.md:11,24) — self-trap into the electron when driven across
yield, by the engine's own Axiom-4 saturation TIR confinement (S_κ→0 ⇒ Z→0 ⇒
Γ=−1; :25), NOT force-free relaxation? "The electron is a self-trapped photon."

WHY THIS IS THE THIRD ATTEMPT (audit §8):
  • Arm A seeded a V-WAVE → ω≡0 (wrong sector — the photon IS ω).
  • Arm B seeded an ω-FLYWHEEL under FORCE-FREE relaxation → de-collimates
    (wrong geometry + wrong mechanism).
  • Here: the right object (transverse Cosserat-ω shear WAVE) + the right
    mechanism (saturation confinement). CP8 generative precursor = the ω-WAVE.

ENGINE CHOICE (load-bearing — flag-don't-fix). The saturation-confinement
mechanism is wired into the ω dynamics ONLY in the STANDALONE CosseratField3D
(use_saturation=True): its step() (cosserat_field_3d.py:1528) uses the SATURATED
energy gradient (:1343) so S_κ=√(1−κ²/ω_yield²) softens the curvature energy as
κ→ω_yield → self-focusing/trap. The COUPLED VacuumEngine3D config used by Arm
A/B/C (disable_cosserat_lc_force=True) builds the Cosserat field with
use_saturation=FALSE (k4_cosserat_coupling.py:297) AND returns a ZERO coupling
force on ω (:427-428) — so saturation there modulates ONLY the K4 V-sector
z_local, NEVER the ω dynamics. → PRIMARY run = standalone (the faithful
mechanism test); a SECONDARY coupled probe demonstrates the architecture finding
empirically (the ω-photon in the coupled config sees no saturation + leaves V
dark; audit §8).

THE SEED (the canonical photon): two counter-propagating, SAME-chirality,
transverse Cosserat-ω shear wavepackets (built on the engine's forward-prop
ω-wave seeder cosserat_field_3d.py:1586-1646, extended to circular polarization
+ a focusing pair). u=0 (pure ω). They FOCUS at the centre, amplitude RAMPS
until κ=|∇×ω|→ω_yield=π, engaging S_κ→0 in step()'s own dynamics → self-trap.
NO V-injection (Arm A), NO flywheel (Arm B), NO gradient descent (CP1; the
:1384 settle is NOT used).

DISCIPLINE: substrate-native-check CP1 (wave dynamics; step(), damping=0), CP4
(phase-space (2,3) read in matched Cosserat-ω coords + V-sector probe), CP5
(ω_local from A²_local), CP6 (reactance pair every window step), CP7 (PML-excl,
density-peak), CP8 (generative precursor + matched baseline). phase-space-
coordinate-check · consistency-vs-emergence (checks 1-3 EMERGENCE, 4-5
CONSISTENCY native-unit readouts — NO CODATA) · ave-canonical-source (constants
imported) · ave-driver-script-honesty (forward reads, NO minimize/fit; amplitude
is IC design, achieved A² reported) · flag-don't-fix (engine-choice + the two
prereg §3 coordinate flags are surfaced, not reconciled).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from r10_2_3_winding_extractor_coordinate import (  # noqa: E402
    extract_2_3_spatial,
    is_2_3,
    shell_params_from_field,
)

from ave.core.constants import ALPHA, V_SNAP, V_YIELD  # noqa: E402
from ave.topological.cosserat_field_3d import (  # noqa: E402
    CosseratField3D,
    _beltrami_helicity,
    _compute_curvature,
    _compute_strain,
    _update_saturation_kernels,
)

# ── Substrate-derived constants (ave-canonical-source; NO hardcoded literals) ──
DT = 1.0 / np.sqrt(2.0)  # reference timestep (loop-period bookkeeping)
COMPTON_PERIOD = 2.0 * np.pi  # ω_C = 1 native ⇒ one Compton period = 2π
STEPS_PER_PERIOD = COMPTON_PERIOD / DT  # ≈ 8.886 loop-steps per Compton period
OMEGA_C = 1.0  # ring frequency ω_C = c/ℓ_node = 1 (native; ℓ_node = 1 cell)
SPIN_HALF = 0.5  # ℏ/2 in native units (ℏ = 1)
M_E_C2 = 1.0  # electron rest energy m_ec² = 1 (native)
ELL_NODE = 1.0  # ℓ_node = 1 lattice cell (native)
V_YIELD_FRAC = float(V_YIELD / V_SNAP)  # √α ≈ 0.0854 (V-phasor yield; cross-check only)
A2_RUPTURE = 5.0  # curvature A²_μ past which the saturated dynamics have ruptured (A²=1 is yield)
DT_DIV = 8  # sub-CFL factor: the saturated dynamics are stiffer than the linear-calibrated cfl_dt


# ══════════════════════════════════════════════════════════════════════════════
# The canonical-photon seed (CP8 generative precursor): chiral transverse
# Cosserat-ω shear WAVE, counter-propagating same-χ focusing pair (PURE ω).
# ══════════════════════════════════════════════════════════════════════════════
def seed_chiral_omega_shear_pair(
    field, amplitude, chirality, wavelength=4.0, sigma_perp=3.0, sigma_z=4.0, offset_frac=0.18
):
    """Seed TWO counter-propagating, same-chirality, transverse Cosserat-ω shear
    wavepackets into `field` (the canonical photon: u=0, ω≠0, sub-saturation).

    Propagation along z; ω in the transverse (x,y) plane; spatial chirality χ=±1
    sets the Beltrami helicity sign h (the seeded charge polarity). Built on
    initialize_gaussian_wavepacket_omega (cosserat_field_3d.py:1586-1646),
    extended to circular polarization + a focusing pair. Per packet at z0 with
    propagation sign s (toward centre):

        ω      = A·env·[cos(k z'),  χ·sin(k z'),  0]
        ω_dot  = s·A·Ω·env·[sin(k z'), −χ·cos(k z'), 0],  Ω = c_T·k,  c_T=√(G/ρ)=1
        env    = exp(−ρ²/2σ⊥²)·exp(−z'²/2σ_z²),  z' = k_idx − z0

    The two packets (z0 = centre ± offset, s = ∓1) converge → amplitude RAMPS at
    the focus → κ crosses ω_yield → saturation self-traps. Same χ ⇒ coherent net
    helicity (charge) with zero net linear momentum (electron at rest).

    `amplitude` is the single-packet peak |ω| (declared drive; the ACHIEVED peak
    A² at the focus is MEASURED during evolution, not pinned to a target)."""
    N = field.nx
    c = (N - 1) / 2.0
    ii, jj, kk = np.indices((N, N, N))
    x, y = ii - c, jj - c
    rho2 = x * x + y * y  # transverse radius² about the z propagation axis
    k = 2.0 * np.pi / float(wavelength)
    c_T = float(np.sqrt(field.G / max(field.rho, 1e-30)))
    Omega = c_T * k

    omega_vec = np.zeros((N, N, N, 3), dtype=np.float64)
    omega_dot = np.zeros((N, N, N, 3), dtype=np.float64)
    dz = offset_frac * N
    for z0, s in ((c - dz, +1.0), (c + dz, -1.0)):  # +z-going from below, −z-going from above
        zp = kk - z0
        env = np.exp(-rho2 / (2.0 * sigma_perp**2)) * np.exp(-(zp * zp) / (2.0 * sigma_z**2))
        cos_kz = np.cos(k * zp)
        sin_kz = np.sin(k * zp)
        omega_vec[..., 0] += amplitude * env * cos_kz
        omega_vec[..., 1] += amplitude * float(chirality) * env * sin_kz
        omega_dot[..., 0] += s * amplitude * Omega * env * sin_kz
        omega_dot[..., 1] += -s * amplitude * float(chirality) * Omega * env * cos_kz

    mask = field.mask_alive[..., None]
    field.omega[:] = omega_vec * mask
    field.omega_dot[:] = omega_dot * mask
    field.u[:] = 0.0  # PURE Cosserat-ω: no translation sector
    field.u_dot[:] = 0.0
    field.time = 0.0
    return {
        "amplitude": float(amplitude),
        "chirality": int(chirality),
        "wavelength": float(wavelength),
        "k": float(k),
        "Omega": float(Omega),
        "offset_cells": float(dz),
        "omega_max_seed": float(np.abs(field.omega).max()),
        "a2_curv_seed": _peak_a2_curvature(field),
        "h_seed": signed_helicity(field),
    }


def make_matched_baseline(
    field, amplitude, chirality, wavelength=4.0, sigma_perp=3.0, sigma_z=4.0, offset_frac=0.18, seed=0
):
    """Matched-distribution baseline (CP8 MANDATORY): SAME per-cell |ω| amplitude
    statistics as the chiral pair, but coherence + chirality DESTROYED — the ω
    direction at each cell is randomized isotropically on S² → net Beltrami
    helicity h→0, no coherent twist, no coherent propagation. Same envelope, same
    Σ|ω|² (same mass). Emergence (self-trap + winding + helicity) must beat THIS,
    so anything it produces is amplitude/saturation, not structure."""
    N = field.nx
    c = (N - 1) / 2.0
    ii, jj, kk = np.indices((N, N, N))
    x, y = ii - c, jj - c
    rho2 = x * x + y * y
    dz = offset_frac * N
    mag = np.zeros((N, N, N), dtype=np.float64)
    for z0 in (c - dz, c + dz):
        zp = kk - z0
        env = np.exp(-rho2 / (2.0 * sigma_perp**2)) * np.exp(-(zp * zp) / (2.0 * sigma_z**2))
        mag += amplitude * env  # scalar magnitude envelope (matches |ω| scale)
    rng = np.random.default_rng(seed)
    dirs = rng.standard_normal((N, N, N, 3))
    dirs /= np.linalg.norm(dirs, axis=-1, keepdims=True) + 1e-12
    vel = rng.standard_normal((N, N, N, 3))
    vel /= np.linalg.norm(vel, axis=-1, keepdims=True) + 1e-12
    mask = field.mask_alive[..., None]
    field.omega[:] = (mag[..., None] * dirs) * mask
    field.omega_dot[:] = (mag[..., None] * vel * (2.0 * np.pi / float(wavelength))) * mask
    field.u[:] = 0.0
    field.u_dot[:] = 0.0
    field.time = 0.0
    return {
        "amplitude": float(amplitude),
        "chirality": int(chirality),
        "baseline": True,
        "omega_max_seed": float(np.abs(field.omega).max()),
        "a2_curv_seed": _peak_a2_curvature(field),
        "h_seed": signed_helicity(field),
    }


# ══════════════════════════════════════════════════════════════════════════════
# Substrate-native diagnostics (forward reads, NO fit) — all in the Cosserat-ω
# sector (the correct coordinates for the ω-photon self-trap + helicity).
# ══════════════════════════════════════════════════════════════════════════════
def _interior_mask(field, PML):
    """Alive Cosserat sites with PML excluded (Rule 10 / CP7)."""
    N = field.nx
    box = np.zeros((N, N, N), dtype=bool)
    box[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return field.mask_alive & box


def _a2_field(field):
    """The full Axiom-4 saturation amplitude A²(x) = ε²/ε_yield² + κ²/ω_yield²
    (cosserat_field_3d.py:332). For pure ω, ε is the antisymmetric Cosserat
    strain (∝|ω|); κ is the curvature (∝|∇ω|)."""
    eps = np.asarray(_compute_strain(field.u, field.omega, field.dx))
    kappa = np.asarray(_compute_curvature(field.omega, field.dx))
    eps_sq = np.sum(eps * eps, axis=(-1, -2))
    kappa_sq = np.sum(kappa * kappa, axis=(-1, -2))
    return eps_sq / field.epsilon_yield**2 + kappa_sq / field.omega_yield**2


def _peak_a2_curvature(field):
    """Peak curvature-sector A²_μ = κ²/ω_yield² over alive sites (the inductive
    drive toward the Γ=−1 TIR). Reported as the achieved drive level."""
    kappa = np.asarray(_compute_curvature(field.omega, field.dx))
    kappa_sq = np.sum(kappa * kappa, axis=(-1, -2))
    a2 = kappa_sq / field.omega_yield**2
    m = field.mask_alive
    return float(a2[m].max()) if m.any() else 0.0


def gamma_field(field, PML):
    """Check-1 — the asymmetric-saturation reflection Γ. The engine's own Z path:
    Z_eff/Z_0 = √(S_μ/S_ε) (cosserat_field_3d.py:583-585), Γ=(Z_eff−Z_0)/(Z_eff+Z_0).
    For pure ω, ε_sym=0 ⇒ S_ε=1, so Γ is curvature(+helicity)-driven: S_μ→0 ⇒
    Z→0 ⇒ Γ→−1 (the canonical inductive-sector TIR). Returns (min_gamma_interior,
    frac_TIR), TIR = Γ<−0.9. PML excluded."""
    N = field.nx
    V_sq = np.zeros((N, N, N), dtype=np.float64)  # pure ω ⇒ V=0
    S_mu, S_eps = _update_saturation_kernels(
        field.u, field.omega, V_sq, field.dx, float(V_SNAP), field.omega_yield, field.epsilon_yield
    )
    S_mu = np.asarray(S_mu)
    S_eps = np.asarray(S_eps)
    Z = np.sqrt(np.clip(S_mu, 1e-12, None) / np.clip(S_eps, 1e-12, None))
    gamma = (Z - 1.0) / (Z + 1.0)
    interior = _interior_mask(field, PML)
    if not interior.any():
        return float("nan"), 0.0
    g = gamma[interior]
    return float(g.min()), float(np.mean(g < -0.9))


def localization(field, PML, r_loc=3.0):
    """Check-1 — does the ω-energy stay localized (trap) or spread/radiate
    (disperse)? Fraction of interior (PML-excl) |ω|² within r_loc cells of the
    energy-density PEAK (CP7 density-peak, NOT centroid). Returns
    (loc_frac, peak_xyz, n_centroids)."""
    wsq = np.sum(field.omega**2, axis=-1)
    interior = _interior_mask(field, PML)
    wsq_i = np.where(interior, wsq, 0.0)
    total = float(wsq_i.sum())
    if total <= 1e-30:
        return 0.0, (np.nan, np.nan, np.nan), 0
    pk = np.unravel_index(int(np.argmax(wsq_i)), wsq_i.shape)  # density peak (CP7)
    ii, jj, kk = np.indices(wsq.shape)
    r2 = (ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2
    near = (r2 <= r_loc**2) & interior
    loc_frac = float(wsq[near].sum() / total)
    cents = field.find_soliton_centroids(threshold_frac=0.3)
    return loc_frac, (float(pk[0]), float(pk[1]), float(pk[2])), len(cents)


def signed_helicity(field):
    """Check-3 — charge = helicity, read in the COSSERAT-ω sector (NOT the
    V-phasor; audit A3.1). |ω|²-weighted SIGNED Beltrami helicity
    h = ω·(∇×ω)/(|ω||∇×ω|). Sign = seeded chirality; |h|→1 ⟺ Beltrami."""
    h = np.asarray(_beltrami_helicity(field.omega, field.dx))
    wsq = np.sum(field.omega**2, axis=-1)
    m = field.mask_alive & (wsq > 1e-12)
    if not m.any():
        return float("nan")
    return float(np.sum(h[m] * wsq[m]) / (np.sum(wsq[m]) + 1e-30))


def omega_mass(field):
    """Check-5 (CONSISTENCY) — mass = ½LI² = ½·I_ω·Σ|ω|² (inductive rotational
    energy). Native m_ec² = 1; amplitude-pinned readout, NOT a CODATA prediction."""
    msk = field.mask_alive[..., None]
    return float(0.5 * field.I_omega * np.sum((field.omega * msk) ** 2))


def omega_spin(field):
    """Check-5 (CONSISTENCY) — spin. S_rot = I_ω·Σ(ω×ω̇)_z is the intrinsic
    rotational angular momentum of the microrotation field (CARRIES the helicity
    sign — flips with χ); S_axial = I_ω·Σω_z is the flywheel-style axial spin
    (~0 for a pure transverse wave). Native ℏ/2 = 0.5. Returns
    (S_rot_z, S_axial_z, |S_axial|)."""
    msk = field.mask_alive[..., None]
    w = field.omega * msk
    wdot = field.omega_dot * msk
    cross = np.cross(w, wdot, axis=-1)
    S_rot_z = float(field.I_omega * np.sum(cross[..., 2]))
    S_ax = field.I_omega * np.sum(w, axis=(0, 1, 2))
    return S_rot_z, float(S_ax[2]), float(np.linalg.norm(S_ax))


def a2_local_cosserat(field, PML):
    """Check-4 (CP5) — the sub-yield core + thin A→1 skin. From the full A²(x):
    skin fraction (A²>0.99), interior median A², core peak A², and
    ω_local/ω_global = √(1−A²) at the peak. PML excluded."""
    a2 = _a2_field(field)
    interior = _interior_mask(field, PML)
    if not interior.any():
        return {
            "skin_frac": float("nan"),
            "interior_median_a2": float("nan"),
            "core_a2": float("nan"),
            "omega_local_over_global": float("nan"),
        }
    a2_i = a2[interior]
    pk = np.unravel_index(int(np.argmax(np.where(interior, a2, -1.0))), a2.shape)
    core_a2 = float(min(a2[pk], 1.0))
    return {
        "skin_frac": float(np.mean(a2_i > 0.99)),
        "interior_median_a2": float(np.median(a2_i)),
        "core_a2": core_a2,
        "omega_local_over_global": float(np.sqrt(max(0.0, 1.0 - core_a2))),
    }


def cosserat_winding(field):
    """Check-2 (Cosserat-ω sector — the load-bearing, coordinate-matched read of
    the "2"): the ω-field's own topology. c (extract_crossing_count), Hopf charge
    Q_H (→6 for the (2,3) electron), and shell radii (R, r)."""
    R, r = field.extract_shell_radii()
    try:
        c = int(field.extract_crossing_count())
    except Exception:
        c = -1
    try:
        q_h = float(field.extract_hopf_charge())
    except Exception:
        q_h = float("nan")
    return {"c_cosserat": c, "Q_H": q_h, "shell_R": float(R), "shell_r": float(r)}


def reactance_pair(field):
    """CP6 — the Cosserat LC reactance pair, recorded every window step. C-state
    (capacitive: ω amplitude) E_C = ½I_ω Σ|ω|²; L-state (inductive: ω̇ rate)
    E_L = ½I_ω Σ|ω̇|². Plus H = T + V (conservation / anti-correlation)."""
    mAl = field.mask_alive[..., None]
    E_C = float(0.5 * field.I_omega * np.sum((field.omega * mAl) ** 2))
    E_L = float(0.5 * field.I_omega * np.sum((field.omega_dot * mAl) ** 2))
    T = float(field.kinetic_energy())
    V = float(field.total_energy())
    return {"E_C": E_C, "E_L": E_L, "T_cos": T, "V_cos": V, "H_cos": T + V}


def _center_alive_cell(field):
    """Nearest alive A-site to the grid centre (the focus) for the core ω-series
    ring-FFT (check 4)."""
    N = field.nx
    c = int(round((N - 1) / 2.0))
    c += c % 2  # snap to even (A-site: all-even)
    c = min(c, N - 2)
    return (c, c, c)


def _ring_frequency(series, times):
    """Check-4 ring: dominant oscillation period of the core ω_x(t). Returns
    (period_in_steps, period_in_Compton_units). ω_C=1 ⇒ ~1 Compton period."""
    y = np.asarray(series, dtype=float)
    y = y - y.mean()
    if y.size < 16 or np.allclose(y, 0.0):
        return float("nan"), float("nan")
    spec = np.abs(np.fft.rfft(y * np.hanning(y.size)))
    freqs = np.fft.rfftfreq(y.size, d=1.0)  # cycles per loop-step
    spec[0] = 0.0
    kpk = int(np.argmax(spec))
    if freqs[kpk] <= 0:
        return float("nan"), float("nan")
    period_steps = 1.0 / freqs[kpk]
    t = np.asarray(times, dtype=float)
    dt_phys = (t[-1] - t[0]) / max(1, (t.size - 1)) if t.size > 1 and t[-1] > t[0] else DT
    return float(period_steps), float(period_steps * dt_phys / COMPTON_PERIOD)


def _effective_radius(field, PML):
    """RMS radius (cells) of the interior |ω|² distribution about its density peak
    — the soliton size vs ℓ_node = 1 (CP7 density-peak)."""
    wsq = np.sum(field.omega**2, axis=-1)
    interior = _interior_mask(field, PML)
    wsq_i = np.where(interior, wsq, 0.0)
    tot = float(wsq_i.sum())
    if tot <= 1e-30:
        return float("nan")
    pk = np.unravel_index(int(np.argmax(wsq_i)), wsq_i.shape)
    ii, jj, kk = np.indices(wsq.shape)
    r2 = (ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2
    return float(np.sqrt(np.sum(r2 * wsq_i) / tot))


def _frame(field):
    """Capture a (real |ω| slice, helicity slice) frame at mid-z for the
    real+phase animation (verdict-I render only)."""
    N = field.nx
    kz = N // 2
    wmag = np.sqrt(np.sum(field.omega**2, axis=-1))[:, :, kz]
    h = np.asarray(_beltrami_helicity(field.omega, field.dx))[:, :, kz]
    return wmag.copy(), h.copy()


# ══════════════════════════════════════════════════════════════════════════════
# Single run: seed the ω-shear photon, evolve under the STANDALONE saturated
# Cosserat dynamics (CP1 — field.step(), damping=0, NO descent), read the battery.
# ══════════════════════════════════════════════════════════════════════════════
def run_one(
    label,
    N,
    PML,
    n_periods,
    amplitude,
    chirality,
    baseline=False,
    wavelength=4.0,
    rec_every=14,
    seed=0,
    capture_frames=False,
):
    """Seed the ω-shear photon (or matched baseline) into a standalone
    CosseratField3D(use_saturation=True) and evolve under field.step() (CP1 wave
    dynamics with the SATURATED gradient — NO descent). Forward reads, NO fit."""
    field = CosseratField3D(N, N, N, dx=1.0, use_saturation=True, pml_thickness=PML, damping_gamma=0.0)
    assert field.use_saturation, "Axiom-4 saturation must be ON for the self-trap mechanism"
    if baseline:
        ic = make_matched_baseline(field, amplitude, chirality, wavelength, seed=seed)
    else:
        ic = seed_chiral_omega_shear_pair(field, amplitude, chirality, wavelength)

    # Sub-CFL dt: the saturated curvature energy is stiffer than the linear cfl_dt
    # calibration; integrate at cfl_dt/DT_DIV so a collapse/disperse verdict is the
    # PHYSICS (non-convex energy), not a CFL artifact (verified: smaller dt at fixed
    # physical time makes the blow-up WORSE, not better — it is finite-time collapse).
    dt = field.cfl_dt / DT_DIV
    n_steps = int(n_periods * STEPS_PER_PERIOD * DT_DIV)
    core = _center_alive_cell(field)
    g0, tir0 = gamma_field(field, PML)
    loc0, _, _ = localization(field, PML)
    rp0 = reactance_pair(field)
    H0 = rp0["H_cos"]
    collapsed = False
    collapse_step = -1
    traj = {
        "step": [0],
        "time": [float(field.time)],
        "a2_peak": [ic["a2_curv_seed"]],
        "min_gamma": [g0],
        "frac_tir": [tir0],
        "loc_frac": [loc0],
        "signed_h": [ic["h_seed"]],
        "mass": [omega_mass(field)],
        "E_C": [rp0["E_C"]],
        "E_L": [rp0["E_L"]],
        "H_cos": [rp0["H_cos"]],
    }
    core_series = [float(field.omega[core][0])]
    core_time = [float(field.time)]
    frames = []

    t0 = time.time()
    for s in range(n_steps):
        field.step(dt=dt)
        core_series.append(float(field.omega[core][0]))
        core_time.append(float(field.time))
        if (s + 1) % rec_every == 0 or (s + 1) == n_steps:
            g, tir = gamma_field(field, PML)
            loc, _, _ = localization(field, PML)
            rp = reactance_pair(field)
            a2p = _peak_a2_curvature(field)
            traj["step"].append(s + 1)
            traj["time"].append(float(field.time))
            traj["a2_peak"].append(a2p)
            traj["min_gamma"].append(g)
            traj["frac_tir"].append(tir)
            traj["loc_frac"].append(loc)
            traj["signed_h"].append(signed_helicity(field))
            traj["mass"].append(omega_mass(field))
            traj["E_C"].append(rp["E_C"])
            traj["E_L"].append(rp["E_L"])
            traj["H_cos"].append(rp["H_cos"])
            # Collapse detection (Rule 11 honest closure): the non-convex saturated
            # energy blows up in finite time. Halt + flag rather than integrate to
            # numerical garbage — the collapse IS the result (NOT a self-trap).
            if a2p > A2_RUPTURE or (abs(H0) > 1e-12 and rp["H_cos"] > 100.0 * abs(H0)):
                collapsed = True
                collapse_step = s + 1
                break
        if capture_frames and ((s + 1) % max(1, n_steps // 60) == 0):
            frames.append(_frame(field))
    elapsed = time.time() - t0

    # ── final-state battery (forward reads) ──
    min_g, frac_tir = gamma_field(field, PML)
    loc_frac, peak_xyz, n_cent = localization(field, PML)
    a2c = a2_local_cosserat(field, PML)
    S_rot, S_ax, S_mag = omega_spin(field)
    wind = cosserat_winding(field)
    ring_steps, ring_periods = _ring_frequency(core_series, core_time)
    a2_peak_max = float(np.max(traj["a2_peak"]))
    h_final = signed_helicity(field)
    h_ratio = abs(traj["H_cos"][-1] / traj["H_cos"][0]) if abs(traj["H_cos"][0]) > 1e-12 else float("inf")
    h_conserved = 0.5 < h_ratio < 2.0
    crossed_yield = a2_peak_max >= 1.0
    localized = bool(loc_frac > 1.5 * loc0 and loc_frac > 0.10)
    # A clean self-trap = crosses yield, localizes, AND conserves energy (a bounded
    # standing wave). A collapse crosses yield + "localizes" to a blow-up point but
    # does NOT conserve energy → it is NOT a self-trap.
    self_trapped_clean = bool((not collapsed) and crossed_yield and localized and h_conserved)
    outcome = "collapse" if collapsed else ("self_trap" if self_trapped_clean else "disperse")

    rec = {
        "label": label,
        "baseline": bool(baseline),
        "ic": ic,
        "config": {
            "N": N,
            "PML": PML,
            "n_periods": n_periods,
            "n_steps": n_steps,
            "amplitude": amplitude,
            "wavelength": wavelength,
            "chirality": int(chirality),
        },
        "elapsed_s": round(elapsed, 1),
        # Stability / outcome (Rule 11): the saturated ω-wave dynamics either
        # DISPERSE (sub-threshold, H-conserved, energy spreads) or COLLAPSE
        # (super-threshold, finite-time blow-up of the non-convex energy) — never
        # confine into a stable self-trapped soliton.
        "collapsed": bool(collapsed),
        "collapse_step": int(collapse_step),
        "dt": float(dt),
        "cfl_dt": float(field.cfl_dt),
        "H_cos_blowup_ratio": (
            float(traj["H_cos"][-1] / traj["H_cos"][0]) if abs(traj["H_cos"][0]) > 1e-12 else float("nan")
        ),
        "H_cos_conserved": bool(h_conserved),
        "outcome": outcome,
        "self_trapped_clean": self_trapped_clean,
        # Check 1 — self-trap (Γ=−1 TIR + localization, EMERGENCE)
        "check1_a2_peak_max": a2_peak_max,
        "check1_crossed_yield": bool(a2_peak_max >= 1.0),
        "check1_min_gamma": min_g,
        "check1_frac_TIR": frac_tir,
        "check1_tir_forms": bool(min_g < -0.9),
        "check1_loc_frac_seed": loc0,
        "check1_loc_frac_final": loc_frac,
        "check1_localized": bool(loc_frac > 1.5 * loc0 and loc_frac > 0.10),
        "check1_n_centroids": n_cent,
        "check1_peak_xyz": peak_xyz,
        # Check 2 — (2,3): Cosserat-ω sector (load-bearing). V-sector handled by the coupled probe.
        "check2_cosserat": wind,
        "check2_cosserat_is_2_3": bool(wind["c_cosserat"] == 3 or round(wind["Q_H"]) == 6),
        # Check 3 — charge = helicity (Cosserat-ω, EMERGENCE)
        "check3_signed_h_seed": ic["h_seed"],
        "check3_signed_h_final": h_final,
        "check3_chirality_seed": int(chirality),
        # carries coherent helicity (charge) if |h| is large (vs baseline ~0); the
        # SIGN↔χ correspondence is the separate χ-flips-h discriminator (h ≈ −χ here).
        "check3_helicity_carried": bool(np.isfinite(h_final) and abs(h_final) > 0.3),
        "check3_sign_tracks_seed": bool(np.isfinite(h_final) and np.sign(h_final) == -np.sign(chirality)),
        # Check 4 — sub-V_yield core + ring at ω_C (CP5, CONSISTENCY)
        "check4_skin_frac": a2c["skin_frac"],
        "check4_interior_median_a2": a2c["interior_median_a2"],
        "check4_core_a2": a2c["core_a2"],
        "check4_sub_yield_core": bool(a2c["core_a2"] < 1.0 and a2c["skin_frac"] < 0.5),
        "check4_omega_local_over_global": a2c["omega_local_over_global"],
        "check4_ring_period_steps": ring_steps,
        "check4_ring_periods_compton": ring_periods,
        "check4_ring_at_omega_C": bool(0.5 < ring_periods < 2.0) if np.isfinite(ring_periods) else False,
        # Check 5 — size ≈ ℓ_node, mass = ½LI², spin = Iω (CONSISTENCY)
        "check5_eff_radius_cells": _effective_radius(field, PML),
        "check5_mass_seed": traj["mass"][0],
        "check5_mass_final": omega_mass(field),
        "check5_spin_rot_z": S_rot,
        "check5_spin_axial_z": S_ax,
        "check5_spin_axial_mag": S_mag,
        # CP6 / conservation
        "H_cos_drift": float(traj["H_cos"][-1] - traj["H_cos"][0]),
        "trace": traj,
    }
    return rec, frames


def coupled_architecture_probe(N, PML, n_periods, amplitude, chirality, wavelength=4.0):
    """SECONDARY (audit §8 architecture probe): seed the SAME ω-shear photon into
    the COUPLED VacuumEngine3D config used by Arm A/B/C, evolve engine.step(), and
    measure (a) whether the ω-wave self-traps there (it should NOT — the coupled
    config builds the Cosserat field use_saturation=False and disables the
    coupling force on ω, so saturation never touches the ω dynamics) and (b)
    whether the K4 V-sector "3" lights up (extract_2_3_spatial on k4.V_inc;
    expected dark — the pure-ω seed does not source V via the even-in-ω coupling,
    A1.1). This DEMONSTRATES the architecture finding empirically."""
    from ave.topological.vacuum_engine import VacuumEngine3D

    eng = VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )
    cos_use_sat = bool(eng.cos.use_saturation)
    ic = seed_chiral_omega_shear_pair(eng.cos, amplitude, chirality, wavelength)
    eng.k4.V_inc[:] = 0.0
    eng.k4.V_ref[:] = 0.0
    eng.k4.Phi_link[:] = 0.0
    a2_peak0 = _peak_a2_curvature(eng.cos)
    loc0, _, _ = localization(eng.cos, PML)
    n_steps = int(n_periods * STEPS_PER_PERIOD)
    for _ in range(n_steps):
        eng.step()
    a2_peak = _peak_a2_curvature(eng.cos)
    loc_f, _, _ = localization(eng.cos, PML)
    v_inc_max = float(np.abs(eng.k4.V_inc).max())
    vprobe = {
        "v_sector_dark": v_inc_max < 1e-9,
        "v_inc_max": v_inc_max,
        "w1_base": 0,
        "w2_fibre": 0,
        "crossing_count_c": 0,
        "is_2_3": False,
    }
    if v_inc_max >= 1e-9:
        R2, r2, cx, cy, cz, kz = shell_params_from_field(eng.k4.V_inc, eng.k4.mask_A, N)
        ext = extract_2_3_spatial(eng.k4.V_inc, eng.k4.Phi_link, eng.k4.mask_A, N, PML, R2, r2, (cx, cy, cz), kz)
        ext.pop("_curve", None)
        vprobe.update(
            {
                "w1_base": ext["w1_base"],
                "w2_fibre": ext["w2_fibre"],
                "crossing_count_c": ext["crossing_count_c"],
                "is_2_3": bool(is_2_3(ext)),
            }
        )
    return {
        "cos_use_saturation": cos_use_sat,  # expected False (saturation NOT in ω dynamics)
        "coupling_force_on_omega": "disabled (disable_cosserat_lc_force=True)",
        "a2_peak_seed": a2_peak0,
        "a2_peak_final": a2_peak,
        "loc_frac_seed": loc0,
        "loc_frac_final": loc_f,
        "self_trapped": bool(loc_f > 1.5 * loc0 and loc_f > 0.10),
        "h_seed": ic["h_seed"],
        "v_sector": vprobe,
    }


def _verdict_for(rec):
    """Per-run discriminator (prereg §5). (I) CLEAN self-trap (crosses yield,
    localizes, energy-CONSERVED — NOT a collapse) AND (2,3) (Cosserat c=3/Q_H≈6)
    AND charge=helicity. (II) clean self-trap but no (2,3)/charge. (III) no clean
    self-trap (disperses sub-threshold, or COLLAPSES super-threshold)."""
    self_trap = rec["self_trapped_clean"]
    is23 = rec["check2_cosserat_is_2_3"]
    charge = rec["check3_helicity_carried"]
    if self_trap and is23 and charge:
        return "I"
    if self_trap:
        return "II"
    return "III"


def render_animation(frames, out_path):
    """Real (|ω| mid-z slice) + phase (Beltrami helicity mid-z slice) side-by-side
    animation — rendered ONLY on verdict (I) per the prereg."""
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.animation as animation
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover
        print(f"  [anim] matplotlib unavailable ({exc}); skipping render")
        return None
    if not frames:
        return None
    fig, (axr, axp) = plt.subplots(1, 2, figsize=(10, 4.6))
    wmax = max(float(f[0].max()) for f in frames) or 1.0
    im_r = axr.imshow(frames[0][0].T, origin="lower", cmap="inferno", vmin=0, vmax=wmax)
    im_p = axp.imshow(frames[0][1].T, origin="lower", cmap="twilight", vmin=-1, vmax=1)
    axr.set_title("real:  |ω|  (ω-shear photon)")
    axp.set_title("phase: Beltrami helicity h (charge)")
    for ax in (axr, axp):
        ax.set_xticks([])
        ax.set_yticks([])
    fig.colorbar(im_r, ax=axr, fraction=0.046)
    fig.colorbar(im_p, ax=axp, fraction=0.046)
    sup = fig.suptitle("genesis: ω-shear photon self-trapping")

    def update(i):
        im_r.set_data(frames[i][0].T)
        im_p.set_data(frames[i][1].T)
        sup.set_text(f"genesis: ω-shear photon self-trapping (frame {i + 1}/{len(frames)})")
        return im_r, im_p, sup

    anim = animation.FuncAnimation(fig, update, frames=len(frames), interval=120, blit=False)
    try:
        anim.save(str(out_path), writer="ffmpeg", dpi=110)
    except Exception:
        out_path = out_path.with_suffix(".gif")
        anim.save(str(out_path), writer="pillow", dpi=90)
    plt.close(fig)
    print(f"  [anim] saved {out_path.name}")
    return out_path


def _chirality_flips_helicity(runs):
    """Charge=helicity discriminator: do RH and LH critical seeds yield
    opposite-sign carried helicity? (The seeded ± handedness IS the charge.)"""
    rh = next((r for r in runs if r["label"] == "photon_RH_subyield"), None)
    lh = next((r for r in runs if r["label"] == "photon_LH_subyield"), None)
    if not rh or not lh:
        return False
    hr, hl = rh["check3_signed_h_final"], lh["check3_signed_h_final"]
    if not (np.isfinite(hr) and np.isfinite(hl)):
        return False
    return bool(np.sign(hr) != np.sign(hl) and abs(hr) > 0.2 and abs(hl) > 0.2)


def main():
    print("=" * 80, flush=True)
    print("  GENESIS (canonical) — self-trap the ω-shear photon")
    print("  Does the transverse Cosserat-ω shear WAVE self-trap into the electron")
    print("  via Axiom-4 saturation TIR (Γ=−1)?  Forward reads, NO fit.")
    print("=" * 80, flush=True)
    print(
        f"  ALPHA={ALPHA}  √α(V-phasor yield)={V_YIELD_FRAC:.4f}  ω_yield(curv)=π  "
        f"ω_C={OMEGA_C} ℏ/2={SPIN_HALF} m_ec²={M_E_C2} ℓ_node={ELL_NODE} (native)\n",
        flush=True,
    )

    N, PML, n_periods, wl = 40, 4, 20, 4.0
    # Drive bracket along the single-packet peak |ω|: a stable sub-threshold pair
    # (carries the seeded ± helicity, disperses) + the matched baseline + the
    # threshold/overdrive runs that engage saturation (→ collapse, NOT confinement).
    plan = [
        ("photon_RH_subyield", 0.2, +1, False),  # stable; carries +helicity; disperses
        ("photon_LH_subyield", 0.2, -1, False),  # stable; carries −helicity; disperses
        ("matched_baseline", 0.2, +1, True),  # matched stats, no coherent helicity
        ("photon_RH_threshold", 0.5, +1, False),  # engages saturation → collapse
        ("photon_RH_overdrive", 1.0, +1, False),  # deeper saturation → collapse
    ]
    runs = []
    for label, amp, chir, base in plan:
        print(f"  ── {label}: A={amp} χ={chir:+d}{' [BASELINE]' if base else ''} ──", flush=True)
        capture = (not base) and abs(amp - 0.2) < 1e-9 and chir > 0  # capture the cleanest (stable) run
        rec, frames = run_one(label, N, PML, n_periods, amp, chir, baseline=base, wavelength=wl, capture_frames=capture)
        v = _verdict_for(rec)
        rec["verdict"] = v
        rec["_frames"] = frames if capture else []
        runs.append(rec)
        w = rec["check2_cosserat"]
        print(
            f"     {rec['elapsed_s']}s | outcome={rec['outcome'].upper()} | "
            f"A²peak={rec['check1_a2_peak_max']:.3g}(cross={rec['check1_crossed_yield']}) "
            f"H×{rec['H_cos_blowup_ratio']:.2g}(cons={rec['H_cos_conserved']}) "
            f"Γmin={rec['check1_min_gamma']:+.2f} loc {rec['check1_loc_frac_seed']:.2f}"
            f"→{rec['check1_loc_frac_final']:.2f} | cos c={w['c_cosserat']} Q_H={w['Q_H']:.1f}"
            f" is23={rec['check2_cosserat_is_2_3']} | h {rec['check3_signed_h_seed']:+.2f}"
            f"→{rec['check3_signed_h_final']:+.2f} | → ({v})",
            flush=True,
        )

    # ── coupled-engine architecture probe (audit §8) ──
    print("\n  ── coupled-engine architecture probe (VacuumEngine3D, Arm A/B/C config) ──", flush=True)
    probe = coupled_architecture_probe(N, PML, n_periods, 1.0, +1, wl)
    print(
        f"     cos.use_saturation={probe['cos_use_saturation']} "
        f"(coupling force on ω: {probe['coupling_force_on_omega']}) | "
        f"a2_peak {probe['a2_peak_seed']:.2f}→{probe['a2_peak_final']:.2f} | "
        f"self_trapped={probe['self_trapped']} | V-sector dark={probe['v_sector']['v_sector_dark']}"
        f" (V_inc_max={probe['v_sector']['v_inc_max']:.2e})",
        flush=True,
    )

    # ── overall adjudication (on the standalone mechanism runs) ──
    phot = [r for r in runs if not r["baseline"]]
    base = [r for r in runs if r["baseline"]]
    any_selftrap = any(r["self_trapped_clean"] for r in phot)
    any_23 = any(r["check2_cosserat_is_2_3"] for r in phot)
    base_23 = any(r["check2_cosserat_is_2_3"] for r in base)
    any_charge = any(r["check3_helicity_carried"] for r in phot)
    chir_flips = _chirality_flips_helicity(runs)
    outcomes = {r["label"]: r["outcome"] for r in runs}
    n_collapse = sum(1 for r in phot if r["outcome"] == "collapse")
    n_disperse = sum(1 for r in phot if r["outcome"] == "disperse")
    if any_selftrap and any_23 and not base_23 and any_charge:
        overall = "I"
    elif any_selftrap:
        overall = "II"
    else:
        overall = "III"

    summary = {
        "overall_verdict": overall,
        "any_clean_self_trap": any_selftrap,
        "n_collapse": n_collapse,
        "n_disperse": n_disperse,
        "outcomes": outcomes,
        "any_2_3_from_photon": any_23,
        "any_2_3_from_baseline": base_23,
        "any_charge_helicity_carried": any_charge,
        "chirality_flips_helicity": chir_flips,
        "per_run_verdicts": {r["label"]: r["verdict"] for r in runs},
        "architecture_probe": probe,
        "mechanism_note": (
            "Saturated Cosserat-ω energy is NON-CONVEX (S_κ²=1−κ²/ω_yield² softens "
            "high-curvature energy): energy-conserving wave dynamics DISPERSE "
            "(sub-threshold) or COLLAPSE in finite time (super-threshold) — never "
            "confine. Confinement requires the gradient-DESCENT settle (CP1-forbidden; "
            "audit §8 A1.6). The COUPLED engine routes saturation only to the K4 "
            "V-sector (cos use_saturation=False + zero coupling force), never ω."
        ),
        "discriminator_legend": {
            "I": "ω-shear wave self-traps → (2,3) + charge=helicity + sub-V_yield ring",
            "II": "self-traps (Γ→−1 skin) but no (2,3)/charge — carrier does not assemble",
            "III": "does not self-trap (ω-wave disperses sub-threshold / COLLAPSES super-threshold)",
        },
    }
    print("\n" + "=" * 80)
    print(f"  OVERALL VERDICT: ({overall}) — {summary['discriminator_legend'][overall]}")
    print(
        f"  clean-self-trap={any_selftrap} | photon outcomes: {n_disperse} disperse + "
        f"{n_collapse} collapse | (2,3) photon={any_23} | χ-flips-h={chir_flips}"
    )
    print("=" * 80)

    anim_path = None
    if overall == "I":
        frames = next((r["_frames"] for r in runs if r["_frames"]), [])
        anim_path = render_animation(frames, Path(__file__).parent / "genesis_omega_wave_selftrap_animation.mp4")

    for r in runs:
        r.pop("_frames", None)
    out = {
        "config": {
            "N": N,
            "PML": PML,
            "n_periods": n_periods,
            "wavelength": wl,
            "DT": DT,
            "ALPHA": ALPHA,
            "V_yield_frac_vphasor": V_YIELD_FRAC,
            "omega_yield_curv": float(np.pi),
            "omega_C": OMEGA_C,
            "spin_half": SPIN_HALF,
            "ell_node": ELL_NODE,
        },
        "summary": summary,
        "animation": str(anim_path) if anim_path else None,
        "runs": runs,
    }
    op = Path(__file__).parent / "genesis_omega_wave_selftrap_results.json"
    op.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {op.name}")
    return out


if __name__ == "__main__":
    main()
