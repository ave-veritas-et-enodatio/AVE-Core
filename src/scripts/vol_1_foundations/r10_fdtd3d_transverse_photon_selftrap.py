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
        F = np.fft.rfftn(field)
        mag = np.abs(F)
        rand_phase = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi, size=F.shape))
        F_scr = mag * rand_phase
        out = np.fft.irfftn(F_scr, s=field.shape)
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
# SECTION 3 — phasor observable: (V_inc,V_ref)=(E±Z_0·H), aspect+chirality [stub]
# ══════════════════════════════════════════════════════════════════════════════
# Built in commit 4.


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — run-and-probe + adjudication                               [stub]
# ══════════════════════════════════════════════════════════════════════════════
# Built in commit 5.


def verify_constants() -> None:
    """ave-driver-script-honesty (a): cross-check canonical imports before any verdict."""
    assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "ALPHA_COLD_INV drift"
    assert abs(PHI_SQ - 2.6180339887) < 1e-6, "PHI_SQ drift"
    assert V_YIELD < V_SNAP, "V_YIELD must be < V_SNAP"
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1.0, "V_YIELD ≠ √α·V_SNAP"
    assert 0.0 < EPS_SAT_RATIO < 1e-6, "EPS_SAT_RATIO out of range"
    assert abs(A2_OP14 - 2.0 * ALPHA) < 1e-9, "A2_OP14 ≠ 2α"


def main() -> dict:
    print("=" * 78, flush=True)
    print("  r10 — Transverse-photon self-trap on fdtd_3d.py (Option C primary)")
    print("  Brief: _orchestration/2026-06-04_full-electron-binding-reseed-probe.md §0")
    print("=" * 78, flush=True)
    verify_constants()
    print(f"  Canonical: V_YIELD={V_YIELD:.3e} V, V_SNAP={V_SNAP:.3e} V, Z_0={Z_0:.2f} Ω")
    print(f"  PASS bars: α⁻¹={ALPHA_COLD_INV:.4f}, φ²={PHI_SQ:.4f}, A²_Op14=2α={A2_OP14:.4f}")
    print("  SCOPE (prereg §1): fdtd_3d.py carries E/H only — toroidal-2 + phasor")
    print("    limit-cycle testable; poloidal-3 OUT OF SCOPE (Cosserat absent).")
    print("\n  [skeleton — seeds + observables + adjudication built in commits 2-5]")
    return {"status": "skeleton", "prereg": "research/2026-06-04_full-electron-transverse-selftrap-result.md"}


if __name__ == "__main__":
    main()
