"""r10_fdtd3d_transverse_photon_selftrap.py — Option C: transverse-photon self-trap.

PRIMARY (Option C, brief §0 REDIRECT): seed a STRUCTURED TRANSVERSE PHOTON (two
counter-propagating focused circularly-polarized transverse pulses, E⊥B⊥k,
multi-node), drive the constructive-interference point past V_yield toward
V_snap, and watch for an AUTONOMOUS self-trap into a bound electron. This is the
canonical pair-production ORIGIN (pair-production-axiom-derivation.md §2 seven
steps: c_local->0 closes the longitudinal channel, blocked KE shatters sideways
into the transverse curl). We seed the ORIGIN (the transverse photon), NOT the
END-state (the compressed knot) — the phase3f end-state seed dispersed because
it omitted the transverse structure that defines + stabilizes the knot.

HEADLINE (emerge-vs-impose): does the (2,3)-signature EMERGE from the transverse
self-trap, or must it be IMPOSED (Option-D nucleation rule)?

LOAD-BEARING SCOPE (prereg §1, surfaced to Grant): fdtd_3d.py carries ONLY six
real-space Yee fields (Ex..Hz). It has NO Cosserat microrotation sector and NO
native V_inc/V_ref ports. Per 06_winding_index_projection.md §4 the poloidal "3"
of the (2,3) is the SU(2) U(1)-fibre phase — the information LOST projecting to
the E-field — so the "3" has no Maxwell-field carrier here. This driver tests
what the continuum engine CAN host: the transverse self-trap, the toroidal "2"
(E-polarization winding), and the (V_inc,V_ref)=(E±Z_0·H) phasor limit cycle
(aspect + chirality). Poloidal-"3" emergence is OUT OF SCOPE for this engine and
reported as a fork verdict, NOT forced.

PREREG: research/2026-06-04_full-electron-transverse-selftrap-result.md (frozen).

Arms:
  C-EMERGE   (primary, emergence-class): transverse photon, NO (2,3) imposed.
  C-NUCLEATE (control, consistency):     transverse photon + Option-D chirality.
  A-CONTROL  (control, the demoted seed): single-bond planted-(2,3) phasor seed.
  BASELINE   (matched, phase3f Factor-2 fix): phase-scrambled, amplitude-matched,
             topologically-trivial — NOT random-direction.

Discipline applied: ave-prereg, substrate-native-check, phase-space-coordinate-
check, ave-canonical-source, ave-canonical-leaf-pull, ave-driver-script-honesty
(emergence arm imposes nothing), consistency-vs-emergence, ave-fundamental-
ground-up-implementation (matched baseline; substrate-derived PASS bars),
ave-evidence-framing-discipline, ave-ee-first-mapping, ave-infinity-discipline
(S_min floor / NaN guard), pre-test-physics-check (the §1 finding).

Run:
    PYTHONPATH=src python3 src/scripts/vol_1_foundations/r10_fdtd3d_transverse_photon_selftrap.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# ── ave-canonical-source: import constants; NO hardcoded physics literals ──────
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

# Derived dimensionless targets (substrate-derived PASS bars, prereg §6.1)
PHI_SQ = PHI * PHI  # ≈ 2.618 — Golden-Torus phasor aspect (P5 diagnostic)
A2_OP14 = R_I**2  # = 2α ≈ 0.0146 onset (R_I = √(2α)); P3 saturation-engagement bar
# NOTE on P3 + operating point (validated during build, prereg §5.1 amendment):
# The engine is instantiated with v_yield=V_SNAP — the TOPOLOGICAL scale, per
# constants.py:42-43 ("Use V_SNAP only for subatomic/topological simulations").
# Then the engine strain is A = V_local/V_SNAP, the Op14 engagement bar is
# A² = R_I² = 2α (A ≈ 0.121), and full saturation (Γ→−1) is A→1. Stable amplitude
# sweep that engages deep saturation WITHOUT the A→1 c_eff-divergence NaN:
# {0.3, 0.5, 0.7}·V_SNAP/dx → peak A ≈ {0.40, 0.61, 0.77} (all past √(2α), all
# stable). 0.85·V_SNAP/dx breaches A>1 and NaNs (ave-infinity-discipline cap).
# Had we left v_yield=V_YIELD (43.65 kV default), the field would rupture at
# V→V_yield (A=V/V_snap≈0.085) — BELOW the √(2α) Op14 bar — and NaN at the focus
# (the phase3f Factor-3 blowup). Operating at V_SNAP is the fix.
AMP_SWEEP_FRAC_VSNAP = (0.3, 0.5, 0.7)  # × V_SNAP/dx; validated stable + saturating

OUTPUT_JSON = Path(__file__).parent / "r10_fdtd3d_transverse_photon_selftrap_results.json"


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — transverse-photon seed construction (C-EMERGE)
# ══════════════════════════════════════════════════════════════════════════════
#
# Two counter-propagating focused circularly-polarized transverse pulses along
# ±x, meeting at the lattice center. Each is a proper propagating Maxwell mode:
# E⊥B⊥k with |E| = Z_0·|H| (self-consistent; fixes phase3f Factor-1 H=0 gap).
# Opposite handedness on the two pulses → the constructive-interference region
# carries a rotating multi-node transverse field (structured/Hopfion-like). NO
# (2,3) winding, NO Beltrami tangent, NO torus-knot is placed — emergence is the
# question (ave-driver-script-honesty: the emergence arm imposes nothing).


def _gaussian_packet_envelope(x_cells, x0, k0, packet_width):
    """Longitudinal Gaussian wave-packet envelope × carrier along propagation axis.

    Returns the complex carrier exp(i k0 (x - x0)) × Gaussian(|x-x0|/packet_width).
    The real/imag parts seed the two quadratures of a propagating transverse mode.
    """
    xi = (x_cells - x0).astype(float)
    gauss = np.exp(-(xi**2) / (2.0 * packet_width**2))
    carrier = np.exp(1j * k0 * xi)
    return gauss * carrier


def build_transverse_photon_seed(
    engine: FDTD3DEngine,
    amplitude: float,
    *,
    wavelength_cells: float = 6.2832,  # λ ≈ 2π cells (Compton-scale on the grid)
    waist_cells: float = 4.0,  # transverse Gaussian σ_yz (focused beam)
    packet_width_cells: float = 6.0,  # longitudinal packet σ
    sep_cells: float = 12.0,  # initial ± separation of the two packets from center
) -> dict:
    """Seed two counter-propagating focused CP transverse pulses (C-EMERGE).

    Sets engine.Ex..Hz IN PLACE. The fields are transverse (E,B in y-z plane;
    k along x). Self-consistent |E| = Z_0|H|. Opposite handedness on the two
    pulses. Returns a metadata dict (seed peak |E|, breach flag).

    NO (2,3) / Beltrami / torus-knot is imposed.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    k0 = 2.0 * np.pi / wavelength_cells

    i, j, k = np.indices((nx, ny, nz))
    x = i.astype(float)
    yy = j - cy
    zz = k - cz
    rho_t = np.sqrt(yy**2 + zz**2)  # transverse radius from x-axis

    # Transverse focusing envelope (Gaussian beam waist), shared by both pulses.
    waist = np.exp(-(rho_t**2) / (2.0 * waist_cells**2))

    # Pulse A: propagates +x, launched left-of-center; RH circular transverse.
    # Pulse B: propagates -x, launched right-of-center; LH circular transverse.
    # Center positions
    x0_A = cx - sep_cells
    x0_B = cx + sep_cells

    packA = _gaussian_packet_envelope(x, x0_A, +k0, packet_width_cells)  # +k
    packB = _gaussian_packet_envelope(x, x0_B, -k0, packet_width_cells)  # -k

    # Circular polarization in the transverse (y,z) plane:
    #   RH (pulse A, +x): E_y = Re(pack), E_z = Im(pack)  (rotates one sense)
    #   LH (pulse B, -x): E_y = Re(pack), E_z = -Im(pack) (opposite sense)
    Ey_A = amplitude * waist * np.real(packA)
    Ez_A = amplitude * waist * np.imag(packA)
    Ey_B = amplitude * waist * np.real(packB)
    Ez_B = -amplitude * waist * np.imag(packB)

    # Self-consistent H for a transverse mode: H = (1/Z_0) k_hat × E.
    # For +x propagation: H_y = -E_z/Z_0, H_z = +E_y/Z_0.
    # For -x propagation: H_y = +E_z/Z_0, H_z = -E_y/Z_0.
    Hy_A = -Ez_A / Z_0
    Hz_A = +Ey_A / Z_0
    Hy_B = +Ez_B / Z_0
    Hz_B = -Ey_B / Z_0

    # Superpose the two counter-propagating packets (E is longitudinally Ex=0).
    engine.Ex[...] = 0.0
    engine.Ey[...] = Ey_A + Ey_B
    engine.Ez[...] = Ez_A + Ez_B
    engine.Hx[...] = 0.0
    engine.Hy[...] = Hy_A + Hy_B
    engine.Hz[...] = Hz_A + Hz_B

    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    seed_peak_E = float(E_mag.max())
    V_local_peak = seed_peak_E * engine.dx
    breach_yield = V_local_peak > engine.v_yield
    return {
        "seed": "C-EMERGE transverse photon (two counter-prop CP packets)",
        "seed_peak_E": seed_peak_E,
        "V_local_peak": V_local_peak,
        "V_yield": float(engine.v_yield),
        "breach_yield_at_seed": bool(breach_yield),
        "wavelength_cells": wavelength_cells,
        "waist_cells": waist_cells,
        "packet_width_cells": packet_width_cells,
        "sep_cells": sep_cells,
        "imposed_winding": None,  # ave-driver-script-honesty: nothing imposed
    }


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — matched baseline + C-NUCLEATE + A-CONTROL seeds
# ══════════════════════════════════════════════════════════════════════════════


def build_matched_trivial_baseline(engine: FDTD3DEngine, c_emerge_meta: dict, *, seed: int = 12345) -> dict:
    """Matched-distribution topologically-trivial baseline (phase3f Factor-2 FIX).

    Takes the SAME amplitude distribution + power spectrum as the C-EMERGE field
    (which must already be seeded on `engine`), but SCRAMBLES the Fourier phase
    per component — destroying the constructive transverse coherence while
    preserving the per-component amplitude histogram. This isolates the
    topology/coherence effect from the saturation-amplitude effect.

    NOT a random-direction seed (the phase3f confound where random gave larger
    single-component amplitudes → more saturation → spurious better retention).
    Operates IN PLACE on engine.Ey/Ez/Hy/Hz (the active components of C-EMERGE).
    """
    rng = np.random.default_rng(seed)

    def _phase_scramble(field: np.ndarray) -> np.ndarray:
        # FFT, randomize phase, preserve magnitude spectrum (Hermitian-symmetric
        # so the inverse is real), inverse FFT. Preserves the amplitude
        # distribution's power spectrum; destroys spatial phase coherence.
        axes = tuple(range(field.ndim))
        F = np.fft.rfftn(field, axes=axes)
        mag = np.abs(F)
        rand_phase = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, size=F.shape))
        F_scr = mag * rand_phase
        out = np.fft.irfftn(F_scr, s=field.shape, axes=axes)
        return out

    # Phase3f Factor-2 fix is two-sided: the baseline must match BOTH (a) the
    # per-component amplitude distribution AND (b) the PEAK |E| (so it engages the
    # saturation kernel to the SAME depth — otherwise whichever seed has the
    # larger peak gets spurious saturation-driven retention, the original
    # phase3f confound, in either direction). We phase-scramble (preserve power
    # spectrum → topology-trivial) then rescale the WHOLE vector field so peak |E|
    # matches C-EMERGE's peak |E| exactly.
    ce_peak_E = float(c_emerge_meta["seed_peak_E"])
    for attr in ("Ey", "Ez", "Hy", "Hz"):
        f = getattr(engine, attr)
        if float(np.max(np.abs(f))) == 0.0:
            continue
        setattr(engine, attr, _phase_scramble(f))
    engine.Ex[...] = 0.0
    engine.Hx[...] = 0.0
    # Rescale vector field so peak |E| matches C-EMERGE peak (match saturation depth)
    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    scr_peak = float(E_mag.max()) or 1.0
    rescale = ce_peak_E / scr_peak
    for attr in ("Ey", "Ez", "Hy", "Hz"):
        setattr(engine, attr, getattr(engine, attr) * rescale)

    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    return {
        "seed": "matched-distribution trivial baseline (phase-scrambled, peak-matched)",
        "seed_peak_E": float(E_mag.max()),
        "matched_to": c_emerge_meta.get("seed"),
        "matched_peak_to": ce_peak_E,
        "imposed_winding": None,
        "is_random_direction": False,  # explicitly NOT the phase3f confound
    }


def apply_option_d_chirality(engine: FDTD3DEngine, trap_xyz, *, radius_cells: float = 4.0, bias: float = 0.15) -> dict:
    """C-NUCLEATE: Option-D nucleation rule (chirality bias) at the trap site.

    Per pair-production-axiom-derivation.md:121: when C1 (A²≥1) is met, impose
    the Beltrami handedness BC. On fdtd_3d.py (no Cosserat ω sector, prereg §1)
    the imposable part is the chiral TRANSVERSE rotation sense — bias the (Ey,Ez)
    transverse field toward a fixed circular handedness (LH) within a sphere of
    `radius_cells` around the trap. This is a CONTROL (clearly labeled), testing
    persistence-when-imposed, NOT emergence.
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    tx, ty, tz = trap_xyz
    i, j, k = np.indices((nx, ny, nz))
    r2 = (i - tx) ** 2 + (j - ty) ** 2 + (k - tz) ** 2
    mask = r2 <= radius_cells**2
    # LH circular bias: rotate (Ey,Ez) toward (cosθ, sinθ) handedness by mixing.
    Ey, Ez = engine.Ey.copy(), engine.Ez.copy()
    engine.Ey[mask] = Ey[mask] - bias * Ez[mask]
    engine.Ez[mask] = Ez[mask] + bias * Ey[mask]
    # Keep H self-consistent-ish for the standing trap (no propagation imposed).
    return {
        "rule": "Option-D chirality bias (LH), fdtd_3d-representable subset",
        "trap_xyz": [int(v) for v in trap_xyz],
        "radius_cells": radius_cells,
        "bias": bias,
        "note": "no Cosserat ω sector — full Beltrami BC not representable (prereg §1)",
        "is_control_not_emergence": True,
    }


def build_single_bond_phasor_seed(
    engine: FDTD3DEngine,
    amplitude: float,
    *,
    R_cells: float = 8.0,
    r_cells: float = 3.0,
    p: int = 2,
    q: int = 3,
) -> dict:
    """A-CONTROL: single-bond planted-(2,3) seed, re-seeded in PHASOR coords (A46 fix).

    The phase3f bug placed the (2,3) tangent in REAL-space field direction. Here
    we place a phasor-trajectory seed: at toroidal-shell sites, set (E, H) so the
    derived (V_inc, V_ref) = (E ± Z_0·H) traces a (p,q) winding — the corpus
    placement (theory.md:16). This is the demoted CONTROL arm; imposed end-state,
    fork-verdict output (continuum-vs-discrete).
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    i, j, k = np.indices((nx, ny, nz))
    x = i - cx
    y = j - cy
    z = k - cz
    rho_xy = np.sqrt(x**2 + y**2 + 1e-12)
    rho_tube = np.sqrt((rho_xy - R_cells) ** 2 + z**2 + 1e-12)
    phi = np.arctan2(y, x)  # toroidal angle
    psi = np.arctan2(z, rho_xy - R_cells)  # poloidal angle
    envelope = amplitude / (1.0 + (rho_tube / 2.0) ** 2)  # hedgehog (AVE-canonical)

    # (p,q) winding PHASE: the phasor angle advances p× toroidally, q× poloidally.
    winding_phase = p * phi + q * psi
    # Encode in the (V_inc, V_ref) split: V_inc ∝ cos(phase), V_ref ∝ sin(phase),
    # i.e. E = (V_inc+V_ref)/2 carries the in-phase part, Z_0·H = (V_inc−V_ref)/2
    # the quadrature. Map onto the transverse (Ey,Ez) with the poloidal frame.
    V_inc = envelope * np.cos(winding_phase)
    V_ref = envelope * np.sin(winding_phase)
    E_par = 0.5 * (V_inc + V_ref)
    ZH_par = 0.5 * (V_inc - V_ref)
    # Project onto transverse poloidal direction (so it lives off-axis, shell-like)
    ey_hat = -np.sin(phi)
    ez_hat = np.cos(phi)
    engine.Ex[...] = 0.0
    engine.Ey[...] = E_par * ey_hat
    engine.Ez[...] = E_par * ez_hat
    engine.Hx[...] = 0.0
    engine.Hy[...] = (ZH_par / Z_0) * (-ez_hat)  # H ⟂ E, transverse
    engine.Hz[...] = (ZH_par / Z_0) * (ey_hat)

    E_mag = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
    return {
        "seed": f"A-CONTROL single-bond planted-({p},{q}) phasor seed (A46-corrected)",
        "seed_peak_E": float(E_mag.max()),
        "R_cells": R_cells,
        "r_cells": r_cells,
        "p": p,
        "q": q,
        "imposed_winding": [p, q],  # THIS arm imposes — it is a control
        "placement": "phasor (V_inc,V_ref)=(E±Z_0·H), NOT real-space tangent",
    }


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — phasor observable: (V_inc,V_ref)=(E±Z_0·H), aspect+chirality
# ══════════════════════════════════════════════════════════════════════════════
#
# phase-space-coordinate-check (A46): the (2,3) lives in the (V_inc,V_ref) phasor.
# We compute V_inc = E + Z_0·H, V_ref = E − Z_0·H as DERIVED observables from the
# engine's real-space E, H (the transmission-line characteristic split). The
# observable lives in phasor coordinates — NOT real-space field direction (the
# phase3f failure). Sampling: PML-excluded, energy-density-PEAK (not centroid —
# centroid of a shell is the empty middle, Rule 10).


def interior_energy_density(engine: FDTD3DEngine, pml: int) -> np.ndarray:
    """EM energy density with PML cells zeroed (Rule 10 PML-cell exclusion)."""
    u = engine.energy_density()
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    out = np.zeros_like(u)
    out[pml : nx - pml, pml : ny - pml, pml : nz - pml] = u[pml : nx - pml, pml : ny - pml, pml : nz - pml]
    return out


def top_k_density_peaks(engine: FDTD3DEngine, pml: int, k: int = 4) -> list[tuple[int, int, int]]:
    """Top-K energy-density PEAK cells (NOT centroid+offset), PML-excluded (Rule 10)."""
    u = interior_energy_density(engine, pml)
    flat = u.ravel()
    if np.count_nonzero(flat) < k:
        k = max(1, int(np.count_nonzero(flat)))
    idx = np.argpartition(flat, -k)[-k:]
    idx = idx[np.argsort(-flat[idx])]
    return [tuple(int(v) for v in np.unravel_index(i, u.shape)) for i in idx]


def phasor_pair_at(engine: FDTD3DEngine, xyz, *, component: str = "y") -> tuple[float, float]:
    """(V_inc, V_ref) = (E ± Z_0·H) at a cell, for one transverse component.

    The characteristic / Riemann-invariant split of the (E, H) pair. component
    'y' uses (Ey, Hz) — the (E_y, H_z) pair that propagates along x (E×H ∝ +x):
    V_inc = E_y + Z_0·H_z, V_ref = E_y − Z_0·H_z. component 'z' uses (Ez, -Hy).
    """
    i, j, k = xyz
    if component == "y":
        E = engine.Ey[i, j, k]
        H = engine.Hz[i, j, k]
    else:
        E = engine.Ez[i, j, k]
        H = -engine.Hy[i, j, k]
    v_inc = float(E + Z_0 * H)
    v_ref = float(E - Z_0 * H)
    return v_inc, v_ref


def fit_ellipse_pca(v_inc_traj, v_ref_traj) -> tuple[float, float]:
    """PCA on the (V_inc, V_ref) point cloud → (R_phase, r_phase) ellipse semi-axes.

    Canonical phase-space methodology (r9_canonical_phase_space_phasor.py).
    """
    pts = np.column_stack([np.asarray(v_inc_traj), np.asarray(v_ref_traj)])
    pts = pts - pts.mean(axis=0)
    if pts.shape[0] < 3:
        return 0.0, 0.0
    cov = np.cov(pts.T)
    evals = np.sort(np.linalg.eigvalsh(cov))  # ascending
    r_phase = float(np.sqrt(max(evals[0], 1e-30)))
    R_phase = float(np.sqrt(max(evals[1], 1e-30)))
    return R_phase, r_phase


def chirality_sign(v_inc_traj, v_ref_traj) -> tuple[float, int]:
    """Mean angular momentum P×dP/dt of the phasor trajectory; sign = rotation sense."""
    vi = np.asarray(v_inc_traj) - np.mean(v_inc_traj)
    vr = np.asarray(v_ref_traj) - np.mean(v_ref_traj)
    if len(vi) < 3:
        return 0.0, 0
    dvi = np.diff(vi)
    dvr = np.diff(vr)
    vim = 0.5 * (vi[:-1] + vi[1:])
    vrm = 0.5 * (vr[:-1] + vr[1:])
    cross = vim * dvr - vrm * dvi
    m = float(np.mean(cross))
    return m, int(np.sign(m))


def toroidal_polarization_winding(engine: FDTD3DEngine, *, R_cells: float, n_phi: int = 72) -> float:
    """Toroidal-"2" observable: E-field polarization winding around the major loop.

    Samples the transverse E-polarization angle θ_pol = atan2(Ez, Ey) at n_phi
    points around a circle of radius R_cells in the z=center plane, and counts the
    total 2π-windings of θ_pol as φ goes 0→2π. This is the w₁ that survives the
    Hopf projection to the E-field (06_winding_index_projection.md §3). Returns the
    (real-valued) winding number; ≈ 2 is the toroidal-"2" PASS. The poloidal-"3"
    is NOT computable here (Cosserat fibre absent, prereg §1/§6.1 P6).
    """
    nx, ny, nz = engine.nx, engine.ny, engine.nz
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    phis = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
    theta = np.zeros(n_phi)
    for a, ph in enumerate(phis):
        xi = int(round(cx + R_cells * np.cos(ph)))
        yi = int(round(cy + R_cells * np.sin(ph)))
        zi = int(round(cz))
        xi = np.clip(xi, 0, nx - 1)
        yi = np.clip(yi, 0, ny - 1)
        ey = engine.Ey[xi, yi, zi]
        ez = engine.Ez[xi, yi, zi]
        theta[a] = np.arctan2(ez, ey)
    # Unwrap and count total winding over the closed loop
    unwrapped = np.unwrap(theta)
    total = unwrapped[-1] - unwrapped[0]
    # add the closing step (last → first)
    closing = np.angle(np.exp(1j * (theta[0] - theta[-1])))
    total += closing
    return float(total / (2.0 * np.pi))


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — run-and-probe + adjudication
# ══════════════════════════════════════════════════════════════════════════════

# Run config (substrate-scale; modest for tractability — convergence noted in result)
N_LATTICE = 48
DX = 0.01
PML = 6
N_SETTLE = 80  # steps to let the two packets collide before locking the trap cell
N_RECORD = 240  # recording-window steps (phasor trajectory + persistence)
PROBE_EVERY = 4


def run_arm(engine: FDTD3DEngine, seed_meta: dict, *, label: str, nucleate: bool = False) -> dict:
    """Evolve one arm; record localization, retention, saturation, phasor, winding.

    Returns the per-arm observable dict. PML-excluded, density-peak sampling.
    """
    R_major = float(seed_meta.get("R_cells", 8.0))
    # Seed interior energy for the retention baseline (PML-excluded)
    interior0 = float(interior_energy_density(engine, PML).sum())

    trap = None
    vi_traj: list[float] = []
    vr_traj: list[float] = []
    peak_E_series: list[float] = []
    interiorE_series: list[float] = []
    peak_A_series: list[float] = []
    nan_hit = False

    for s in range(N_SETTLE + N_RECORD):
        engine.step()
        if not np.all(np.isfinite(engine.Ey)):
            nan_hit = True
            break
        if s == N_SETTLE:
            # Lock the trap cell at the post-collision interior density peak
            pk = top_k_density_peaks(engine, PML, k=1)
            trap = pk[0] if pk else None
            if nucleate and trap is not None:
                seed_meta["option_d"] = apply_option_d_chirality(engine, trap)
        if s >= N_SETTLE and (s - N_SETTLE) % PROBE_EVERY == 0:
            u_int = interior_energy_density(engine, PML)
            peak_E_series.append(float(np.sqrt(u_int).max()))
            interiorE_series.append(float(u_int.sum()))
            Em = np.sqrt(engine.Ex**2 + engine.Ey**2 + engine.Ez**2)
            peak_A_series.append(float((Em * DX / V_SNAP).max()))
            if trap is not None:
                vi, vr = phasor_pair_at(engine, trap, component="y")
                vi_traj.append(vi)
                vr_traj.append(vr)

    # Observables
    R_phase, r_phase = fit_ellipse_pca(vi_traj, vr_traj) if len(vi_traj) > 3 else (0.0, 0.0)
    aspect = R_phase / max(r_phase, 1e-30)
    cm, csign = chirality_sign(vi_traj, vr_traj) if len(vi_traj) > 3 else (0.0, 0)
    tor_wind = toroidal_polarization_winding(engine, R_cells=R_major) if not nan_hit else float("nan")

    # localization: did the energy stay interior + bounded, or leak/disperse?
    interiorE_final = float(interior_energy_density(engine, PML).sum()) if not nan_hit else 0.0
    interior_retention = interiorE_final / max(interior0, 1e-30)
    # peak-field retention over the recording window (mean-V_peak breather criterion)
    if len(peak_E_series) > 2:
        peak_E_retention = float(np.mean(peak_E_series[-3:]) / max(peak_E_series[0], 1e-30))
        peak_E_breather_mean = float(np.mean(peak_E_series))
    else:
        peak_E_retention = 0.0
        peak_E_breather_mean = 0.0
    peak_A_max = float(np.max(peak_A_series)) if peak_A_series else 0.0

    # is the trap cell still interior (self-trapped) or did it migrate to the PML edge?
    trap_interior = None
    if trap is not None:
        ti = all(PML <= trap[d_] < (N_LATTICE - PML) for d_ in range(3))
        trap_interior = bool(ti)

    return {
        "label": label,
        "seed": seed_meta.get("seed"),
        "imposed_winding": seed_meta.get("imposed_winding"),
        "nan_hit": bool(nan_hit),
        "trap_cell": list(trap) if trap is not None else None,
        "trap_still_interior": trap_interior,
        "peak_E_retention": peak_E_retention,
        "peak_E_breather_mean": peak_E_breather_mean,
        "interior_energy_retention": interior_retention,
        "peak_A_max": peak_A_max,
        "saturation_engaged_op14": bool(peak_A_max > R_I),  # A > √(2α)
        "phasor_aspect_R_over_r": aspect,
        "phasor_aspect_vs_phi2": aspect / PHI_SQ if aspect > 0 else 0.0,
        "phasor_chirality_sign": csign,
        "phasor_chirality_cross_mean": cm,
        "toroidal_polarization_winding": tor_wind,
        "n_phasor_samples": len(vi_traj),
        "option_d": seed_meta.get("option_d"),
    }


def adjudicate(results: dict) -> dict:
    """Apply prereg §6 PASS criteria + fork verdict + emergence headline."""
    cE = results["C-EMERGE"]
    base = results["BASELINE"]
    cN = results.get("C-NUCLEATE", {})
    aC = results.get("A-CONTROL", {})

    # P1 localization: trap stayed interior + peak field did not collapse
    p1 = bool(cE["trap_still_interior"]) and cE["peak_E_retention"] > 0.5
    # P2 retention > matched baseline
    p2 = cE["peak_E_retention"] > base["peak_E_retention"]
    # P3 saturation engaged
    p3 = cE["saturation_engaged_op14"]
    # P4 toroidal-2 winding (|w − 2| < 0.5 → integer 2)
    tw = cE["toroidal_polarization_winding"]
    p4 = (not np.isnan(tw)) and abs(abs(tw) - 2.0) < 0.5
    # P5 phasor limit-cycle present (closed cloud, finite aspect, nonzero chirality)
    p5 = cE["phasor_aspect_R_over_r"] > 1.05 and cE["phasor_chirality_sign"] != 0
    # P6 poloidal-3: structurally out of scope (Cosserat absent) — recorded, not PASS/FAIL
    p6 = "OUT_OF_SCOPE (no Cosserat sector on fdtd_3d.py — prereg §1)"

    # Fork verdict. P4 (toroidal-2 winding) is the load-bearing structural
    # observable; P5 (phasor limit-cycle aspect) is NECESSARY-BUT-NOT-SUFFICIENT
    # (prereg §3) — a closed phasor cloud is not the (2,3) winding. So Mode I
    # requires P4; P5-alone with P4-fail is Mode II (self-trap without the "2").
    self_trapped = p1 and p3
    if self_trapped and p4 and p5 and p2:
        fork = "Mode I (self-traps; toroidal-2 + phasor limit-cycle present) — continuum hosts the testable structure; CAVEAT: poloidal-3 untested (P6 out of scope)"
    elif self_trapped:
        fork = ("Mode II (self-traps but the (2,3) winding observable is OFF: toroidal-2 absent) "
                "— the continuum engine hosts a localized self-trapped photon but NOT the (2,3) "
                "winding structure. Even the testable '2' does not emerge here. Strong support "
                "that the discrete K4 4-port + Cosserat is load-bearing for the WINDING "
                "(path forward = K4-TLM + Cosserat, r10_v8_t_st_self_trap.py).")
    else:
        fork = "Mode III (disperses even with transverse-photon origin seed across sweep) — strong evidence the discrete K4 4-port + Cosserat is load-bearing; continuum engine cannot host the (2,3); path forward = K4-TLM + Cosserat (r10_v8_t_st_self_trap.py)"

    # Emergence headline. The (2,3) winding is the headline subject. P4 (toroidal-2)
    # is the only WINDING observable fdtd_3d.py can carry; P5 alone is not winding.
    # So "(2,3) emergent" requires at minimum P4. P5-only = self-trap-emerges-but-
    # winding-does-not.
    p23_winding_emerged = p4  # the only winding signature this engine can test
    if p2 and self_trapped and p23_winding_emerged:
        emergence = ("EMERGENT (toroidal-2 component) — C-EMERGE (no imposed winding) self-traps, "
                     "out-retains matched baseline, AND autonomously winds the toroidal-2. "
                     "CAVEAT: poloidal-3 not assessable on this engine (Cosserat absent).")
    elif p2 and self_trapped:
        emergence = ("SELF-TRAP EMERGES but the (2,3) WINDING DOES NOT — C-EMERGE (no imposed "
                     "winding) autonomously self-traps a localized photon + out-retains the matched "
                     "baseline (a real emergence result for LOCALIZATION), but the toroidal-2 "
                     "winding does NOT emerge (P4 fail) and poloidal-3 is out of scope. The (2,3) "
                     "winding is NEITHER emergent NOR (on this engine) testable-to-emerge — it needs "
                     "the Cosserat sector + discrete 4-port (prereg §1). Honest partial.")
    elif cN and cN.get("trap_still_interior") and cN.get("peak_E_retention", 0) > cE["peak_E_retention"]:
        emergence = "IMPOSED-but-persists (partial) — C-EMERGE disperses; C-NUCLEATE (Option-D imposed) persists better → structure imposed, not emergent, on this engine"
    else:
        emergence = "DISPERSES — transverse seed insufficient on the continuum engine; missing the Cosserat sector + discrete 4-port (prereg §1)"

    return {
        "P1_localization": p1,
        "P2_retention_gt_matched_baseline": p2,
        "P3_saturation_engaged": p3,
        "P4_toroidal_2_winding": p4,
        "P5_phasor_limit_cycle": p5,
        "P6_poloidal_3": p6,
        "C-EMERGE_peak_E_retention": cE["peak_E_retention"],
        "BASELINE_peak_E_retention": base["peak_E_retention"],
        "A-CONTROL_peak_E_retention": aC.get("peak_E_retention"),
        "C-NUCLEATE_peak_E_retention": cN.get("peak_E_retention"),
        "fork_verdict": fork,
        "emergence_headline": emergence,
    }


def verify_constants() -> None:
    """ave-driver-script-honesty (a): cross-check canonical imports before any verdict."""
    assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "ALPHA_COLD_INV drift"
    assert abs(PHI_SQ - 2.6180339887) < 1e-6, "PHI_SQ drift"
    assert V_YIELD < V_SNAP, "V_YIELD must be < V_SNAP"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1.0, "V_YIELD ≠ √α·V_SNAP"
    assert 0.0 < EPS_SAT_RATIO < 1e-6, "EPS_SAT_RATIO out of range"
    assert abs(A2_OP14 - 2.0 * ALPHA) < 1e-9, "A2_OP14 ≠ 2α"


def _new_engine() -> FDTD3DEngine:
    """Engine at the TOPOLOGICAL scale (v_yield=V_SNAP) per prereg §5.1 amendment."""
    return FDTD3DEngine(
        nx=N_LATTICE, ny=N_LATTICE, nz=N_LATTICE, dx=DX,
        linear_only=False, use_pml=True, pml_layers=PML, v_yield=V_SNAP,
    )


def _pick_stable_amplitude() -> tuple[float, float]:
    """Sweep {0.3,0.5,0.7}·V_snap/dx; return the HIGHEST that does not NaN over a
    short collision run (ave-infinity-discipline: deepest stable saturation)."""
    best_frac = AMP_SWEEP_FRAC_VSNAP[0]
    for frac in AMP_SWEEP_FRAC_VSNAP:
        e = _new_engine()
        build_transverse_photon_seed(e, amplitude=frac * V_SNAP / DX)
        ok = True
        for _ in range(N_SETTLE + 20):
            e.step()
            if not np.all(np.isfinite(e.Ey)):
                ok = False
                break
        if ok:
            best_frac = frac
    return best_frac, best_frac * V_SNAP / DX


def main() -> dict:
    print("=" * 78, flush=True)
    print("  r10 — Transverse-photon self-trap on fdtd_3d.py (Option C primary)")
    print("  Brief: _orchestration/2026-06-04_full-electron-binding-reseed-probe.md §0")
    print("=" * 78, flush=True)
    verify_constants()
    print(f"  Canonical: V_YIELD={V_YIELD:.3e} V, V_SNAP={V_SNAP:.3e} V, Z_0={Z_0:.2f} Ω")
    print(f"  PASS bars: α⁻¹={ALPHA_COLD_INV:.4f}, φ²={PHI_SQ:.4f}, A_Op14=√(2α)={R_I:.4f}")
    print(f"  Engine: N={N_LATTICE}³, PML={PML}, v_yield=V_SNAP (topological scale)")
    print("  SCOPE (prereg §1): fdtd_3d.py carries E/H only — toroidal-2 + phasor")
    print("    limit-cycle testable; poloidal-3 OUT OF SCOPE (Cosserat absent).")
    t0 = time.time()

    # Pick the deepest stable amplitude across the sweep
    amp_frac, amplitude = _pick_stable_amplitude()
    print(f"\n  Amplitude (deepest stable in sweep {AMP_SWEEP_FRAC_VSNAP}): "
          f"{amp_frac:.2f}·V_snap/dx", flush=True)

    results: dict = {}

    # --- C-EMERGE (primary, emergence-class): transverse photon, NO winding imposed
    print("\n  [C-EMERGE] transverse photon, no (2,3) imposed ...", flush=True)
    e = _new_engine()
    mE = build_transverse_photon_seed(e, amplitude=amplitude)
    results["C-EMERGE"] = run_arm(e, mE, label="C-EMERGE")
    results["C-EMERGE"]["seed_meta"] = mE

    # --- BASELINE (matched-distribution trivial; phase3f Factor-2 fix)
    print("  [BASELINE] matched-distribution trivial (phase-scrambled, peak-matched) ...", flush=True)
    e = _new_engine()
    mE_for_base = build_transverse_photon_seed(e, amplitude=amplitude)
    mB = build_matched_trivial_baseline(e, mE_for_base)
    results["BASELINE"] = run_arm(e, mB, label="BASELINE")

    # --- C-NUCLEATE (control, consistency): transverse photon + Option-D chirality
    print("  [C-NUCLEATE] transverse photon + Option-D chirality (control) ...", flush=True)
    e = _new_engine()
    mN = build_transverse_photon_seed(e, amplitude=amplitude)
    mN["seed"] = "C-NUCLEATE transverse photon + Option-D chirality"
    results["C-NUCLEATE"] = run_arm(e, mN, label="C-NUCLEATE", nucleate=True)

    # --- A-CONTROL (the demoted single-bond planted-(2,3) phasor seed)
    print("  [A-CONTROL] single-bond planted-(2,3) phasor seed (A46-corrected) ...", flush=True)
    e = _new_engine()
    mA = build_single_bond_phasor_seed(e, amplitude=amplitude)
    results["A-CONTROL"] = run_arm(e, mA, label="A-CONTROL")

    verdict = adjudicate(results)
    elapsed = time.time() - t0

    # ── Report ────────────────────────────────────────────────────────────────
    print("\n" + "=" * 78)
    print("  VERDICT")
    print("=" * 78)
    print(f"  Fork: {verdict['fork_verdict']}")
    print(f"  Emergence headline: {verdict['emergence_headline']}")
    print(f"\n  PASS criteria (C-EMERGE):")
    for kk in ("P1_localization", "P2_retention_gt_matched_baseline", "P3_saturation_engaged",
               "P4_toroidal_2_winding", "P5_phasor_limit_cycle", "P6_poloidal_3"):
        print(f"    {kk}: {verdict[kk]}")
    print(f"\n  Retention (peak |field|): C-EMERGE={verdict['C-EMERGE_peak_E_retention']:.3f}  "
          f"BASELINE={verdict['BASELINE_peak_E_retention']:.3f}  "
          f"A-CONTROL={verdict['A-CONTROL_peak_E_retention']}  "
          f"C-NUCLEATE={verdict['C-NUCLEATE_peak_E_retention']}")
    for arm in ("C-EMERGE", "BASELINE", "C-NUCLEATE", "A-CONTROL"):
        r = results[arm]
        print(f"  [{arm}] trap_interior={r['trap_still_interior']} peak_A_max={r['peak_A_max']:.4f} "
              f"sat_op14={r['saturation_engaged_op14']} aspect={r['phasor_aspect_R_over_r']:.3f} "
              f"tor_wind={r['toroidal_polarization_winding']:.3f} nan={r['nan_hit']}")

    payload = {
        "driver": "r10_fdtd3d_transverse_photon_selftrap",
        "prereg": "research/2026-06-04_full-electron-transverse-selftrap-result.md",
        "engine": "fdtd_3d.py (full-vector Maxwell, v_yield=V_SNAP)",
        "config": {"N": N_LATTICE, "dx": DX, "PML": PML, "n_settle": N_SETTLE,
                    "n_record": N_RECORD, "amp_frac_vsnap": amp_frac},
        "scope_note": "poloidal-3 OUT OF SCOPE on fdtd_3d.py (no Cosserat sector, prereg §1)",
        "arms": results,
        "verdict": verdict,
        "elapsed_s": elapsed,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {OUTPUT_JSON.name} ({elapsed:.0f}s)")
    return payload


if __name__ == "__main__":
    main()
