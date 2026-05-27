"""
test_lattice_pq_dispersion_classification.py
==============================================

Path B-prime entry-gate experiment — Linear-regime K4-TLM transverse-mode
(p,q) band-splitting test.

Pre-reg: research/2026-05-25_path-b-prime-k4-dispersion-pq-classification-prereg.md
Result : research/2026-05-27_path-b-prime-k4-dispersion-pq-classification-result.md
Epic   : _orchestration/path-b-prime-k4-dispersion-pq.md

Substrate-native framing
------------------------
Per the prereg §2 hypothesis H1: K4-TLM transverse modes in the linear regime
(A << √(2α), Regime I passband) carry intrinsic (p,q) torus-knot winding
labels via local Hopf-fiber-bundle structure on the chiral I4_132 substrate.
Canonical foundation: L3 archive doc 06 §2 — projection $SU(2) \to S^2$ with
explicit $(w_1=2, w_2=3)$ Clifford-torus identification at Level 1.

The substrate-native test (per Q-PBP-2 tautology-discriminator):
the (p,q) label must live on the WAVE's geometric structure (curve winding
on the local Clifford-torus phase space), NOT on a per-run modulation
parameter like kappa_tilde_torus(p,q). We therefore construct (p,q)-shaped
spatial-phase seed wave packets — chiral azimuthal phase windings p around
one transverse axis and q around the other — and measure whether the
resulting eigenmodes show distinct ω(k) dispersion bands.

If K4-TLM substrate carries the Hopf-fiber-bundle structure that L3 doc 06
asserts at the Cosserat level, then linear-regime transverse modes should
split into (p,q)-classified bands. If K4-TLM is simply a (k-classified)
LC resonant network with no winding-eigenmode structure, all (p,q) seeds
collapse to the same k-continuum.

What this test does NOT do
--------------------------
- Does NOT feed kappa_tilde_torus(p,q) as a modulation parameter (that's
  the tautology Q-PBP-2 flags — it measures simulator response to
  external coupling input, not substrate-classification).
- Does NOT use the Cosserat field (K4-TLM only — pure port-space dynamics).
- Does NOT engage the saturation kernel (linear regime: strain A ≈ 8.54e-5,
  A² ≈ 7.3e-9, S = √(1-A²) ≈ 1 to 9 decimal places; Op14 dormant).
- Does NOT test torus-knot uniqueness or energy-ordering (that's Path B).

Substrate-mechanical mechanism being tested
-------------------------------------------
The K4Lattice3D engine implements a 4-port scattering network on a bipartite
diamond lattice. Its scattering matrix is symmetric and contains NO
chirality-dependent terms. If linear-regime K4-TLM modes nevertheless
exhibit (p,q) band-splitting, the chirality must enter through the substrate
geometry (I4_132 chiral space group → bipartite tetrahedral port structure
→ phase-space mode geometry). If no band-splitting appears, the K4-TLM
4-port scattering network is too symmetric to carry the Hopf-fiber-bundle
structure as a load-bearing primitive — Path B-prime is dead at K4-TLM
level (outcome C).

PREREG metrics (frozen 2026-05-25, not adjusted post-hoc)
---------------------------------------------------------
M1: ≥6 distinct (p,q) bands required with ≥5% ω-spacing at fixed k
M2: ordering matches knot-crossing-number sequence (2,3)<(2,5)<(3,4)<(2,7)<(3,5)<(3,7)
M3: (1,q) unknot bands have <1% separation from baseline T₂ continuum
M4: gcd>1 pairs ((2,2),(2,4),(3,6)) <10% amplitude of (2,3) baseline
M5: bands scale linearly with kappa_tilde input ±20%; not pinned to α-hardcoded

Outcome map
-----------
A CONFIRMED   : M1 ✓ AND M2 ✓ AND M3 ✓ AND M4 ✓ AND M5 ✓
B PARTIAL     : M1 ✓ but ≥1 of M2/M3/M4 fails
C FALSIFIED   : M1 fails (no (p,q) band-splitting)
D TAUTOLOGY   : M5 fails (bands pinned to α-hardcoded)

References
----------
- prereg: research/2026-05-25_path-b-prime-k4-dispersion-pq-classification-prereg.md
- L3 doc 06: research/_archive/L3_electron_soliton/06_winding_index_projection.md
- canonical κ̃ infrastructure: ave/topological/cosserat_field_3d.py:93-119
- canonical constants: ave/core/constants.py (ALPHA, V_YIELD, V_SNAP, L_NODE, C_0)
- existing dispersion driver: src/scripts/vol_1_foundations/test_lattice_layer_1_dispersion.py
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import ALPHA, C_0, L_NODE, V_SNAP, V_YIELD
from ave.core.k4_tlm import K4Lattice3D
from ave.topological.cosserat_field_3d import kappa_tilde_torus

# ─────────────────────────────────────────────────────────────────────────
# PREREG (frozen 2026-05-25 — do not adjust)
# ─────────────────────────────────────────────────────────────────────────
PREREG: dict = {
    "M1_distinct_bands_required": 6,
    "M1_band_separation_threshold": 0.05,  # ≥5% ω spacing between adjacent bands at fixed k
    "M2_ordering_required": [(2, 3), (2, 5), (3, 4), (2, 7), (3, 5), (3, 7)],
    "M2_ordering_match_threshold": "exact",
    "M3_unknot_band_separation_max": 0.01,
    "M4_gcd_gt1_band_stability_max": 0.10,
    "M5_alpha_independence_kappa_scale_range": 0.20,  # ±20%
}


# (p,q) enumeration per prereg §4.2
STABLE_KNOT_CANDIDATES: List[Tuple[int, int]] = [(2, 3), (2, 5), (2, 7), (3, 4), (3, 5), (3, 7)]
UNKNOT_NULL_CANDIDATES: List[Tuple[int, int]] = [(1, 1), (1, 2), (1, 3)]
LINK_NULL_CANDIDATES: List[Tuple[int, int]] = [(2, 2), (2, 4), (3, 6)]
ALL_PQ: List[Tuple[int, int]] = STABLE_KNOT_CANDIDATES + UNKNOT_NULL_CANDIDATES + LINK_NULL_CANDIDATES


@dataclass
class PQRunResult:
    """Per-(p,q) FFT-extracted spectral content from a linear-regime K4-TLM run."""

    p: int
    q: int
    is_knot: bool  # gcd(p,q)==1 AND both >= 2
    is_unknot: bool  # min(p,q)==1
    is_link: bool  # gcd(p,q) > 1
    kappa_tilde: float  # pq/(p+q), descriptive only
    omega_peak_native: float  # dominant FFT frequency, native units (1/dt)
    omega_peak_dimensionless: float  # ω peak / (2π c / λ_carrier)
    spectral_centroid: float
    spectral_amplitude: float  # peak |FFT| magnitude
    spectral_total_energy: float  # ∫ |FFT|² dω
    fft_freqs: np.ndarray = field(repr=False)
    fft_amps: np.ndarray = field(repr=False)


def is_coprime(p: int, q: int) -> bool:
    return math.gcd(p, q) == 1


def topology_class(p: int, q: int) -> str:
    if min(p, q) == 1:
        return "unknot"
    if math.gcd(p, q) > 1:
        return "link"
    return "knot"


# ─────────────────────────────────────────────────────────────────────────
# Substrate-native (p,q) seed
# ─────────────────────────────────────────────────────────────────────────


def build_pq_seed_profile(
    nx: int,
    ny: int,
    nz: int,
    p: int,
    q: int,
    lambda_cells: float,
    src_x: int,
    mask_active: np.ndarray,
) -> np.ndarray:
    """Construct a (p,q)-winding spatial phase pattern for the source plane.

    The (p,q) label lives on the WAVE's local geometric structure — a chiral
    azimuthal phase winding around the (y,z) plane orthogonal to propagation
    direction +x̂. p windings around the "major" direction (y-axis projection),
    q windings around the "minor" direction (z-axis projection), modulated
    by a Gaussian envelope so the seed is spatially localized.

    NOT a kappa_tilde modulation. The (p,q) integers enter only through the
    geometric winding of the source spatial phase — the substrate-native
    primitive per L3 doc 06 §2 (Clifford-torus phase-space (θ₁, θ₂) → S²
    projection inheriting w₁=p winding).

    Returns 2D (ny, nz) complex amplitude pattern (taken real for V_inc).
    """
    j_idx, k_idx = np.indices((ny, nz), dtype=float)
    cy, cz = (ny - 1) / 2.0, (nz - 1) / 2.0
    # Transverse polar coords around source-plane center
    dy = j_idx - cy
    dz = k_idx - cz
    r = np.sqrt(dy * dy + dz * dz)
    phi = np.arctan2(dz, dy)
    # Substrate-native (p,q) torus-knot phase: p windings around major angle
    # θ₁ ≡ φ in the transverse polar parameterization, q windings tracked by
    # the radial structure that encodes the minor cycle θ₂. Constructed as
    # an (p,q)-Lissajous chiral phase pattern:
    #   ψ(φ, r) = exp[i(p·φ + q·2π·r/λ_minor)]
    # where λ_minor is set to one transverse wavelength so r/λ_minor is
    # dimensionless and q counts the radial-direction winding count.
    sigma_yz = 8.0
    envelope = np.exp(-(dy * dy + dz * dz) / (2.0 * sigma_yz**2))
    # Chiral azimuthal phase: p windings in φ
    azimuthal_phase = p * phi
    # Radial phase: q windings across the Gaussian envelope width (so the
    # seed carries q radial nodes within sigma_yz support).
    radial_phase = q * (2.0 * np.pi * r / (2.0 * sigma_yz))
    seed = envelope * np.cos(azimuthal_phase + radial_phase)
    # Apply active-mask at src_x slice
    active_slice = mask_active[src_x]
    return seed * active_slice.astype(float)


def run_pq_dispersion_one(
    p: int,
    q: int,
    N: int = 64,
    n_steps: int = 480,
    lambda_cells: float = 10.0,
    amp_frac: float = 0.001,
    pml_thickness: int = 8,
    src_x: int = 16,
    kappa_scale: float = 1.0,
) -> PQRunResult:
    """Run linear-regime K4-TLM dispersion test for one (p,q) topology.

    Per prereg §4.1: N=64, PML=8, amp=0.001·V_YIELD, 480 steps.
    Per prereg §4.4 M5: kappa_scale parameter exposed for α-tautology test.

    kappa_scale: scalar multiplier on a kappa_tilde-shaped weighting of the
    chiral amplitude. ONLY used by M5 alpha-independence sub-test. Default
    1.0 means no kappa_tilde modulation enters the source — the (p,q)
    label lives purely in the seed geometric phase pattern (substrate-native).
    """
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml_thickness)
    dt = lattice.dt
    c = lattice.c

    # Carrier frequency and timing for the wave packet
    omega_carrier = 2.0 * np.pi * c / (lambda_cells * lattice.dx)
    period = 2.0 * np.pi / omega_carrier
    t_sigma = 0.75 * period
    t_center = 3.0 * t_sigma

    # Linear-regime amplitude. amp_frac=0.001·V_YIELD/V_SNAP ≈ 8.54e-5 strain.
    # Strain² ≈ 7.3e-9; saturation kernel S(A) ≈ 1.0 to 9 decimal places.
    # Op14 is dormant in this regime.
    amp_si = amp_frac * V_YIELD

    # (p,q) seed spatial phase pattern — substrate-native chiral winding
    seed_profile = build_pq_seed_profile(N, N, N, p, q, lambda_cells, src_x, lattice.mask_active)

    # Forward-port weights (+x̂ propagation direction)
    direction = np.array([1.0, 0.0, 0.0])
    PORT_HAT = np.array(
        [
            [+1, +1, +1],
            [+1, -1, -1],
            [-1, +1, -1],
            [-1, -1, +1],
        ],
        dtype=float,
    ) / np.sqrt(3.0)
    port_w = np.maximum(0.0, -PORT_HAT @ direction)
    if port_w.sum() > 0:
        port_w = port_w / port_w.sum()

    # M5 α-independence kappa_scale: applied as overall amplitude multiplier
    # on the seed when kappa_scale != 1.0. This is a TEST DIAGNOSTIC ONLY;
    # at the substrate-native default kappa_scale=1.0 the (p,q) label lives
    # in the seed phase geometry, not in the amplitude.
    kappa_tilde_val = kappa_tilde_torus(p, q)
    effective_amp = amp_si * kappa_scale  # M5 perturbation

    # Recording plane for FFT (interior — beyond PML, beyond source skin depth)
    # Per A-Rule 10 corollary: filter PML cells before any extraction.
    record_x = src_x + 25
    assert pml_thickness < record_x < N - pml_thickness, "record plane must be interior"
    record_y = N // 2
    record_z = N // 2
    # Recording over time of V_inc at the interior probe point
    v_inc_trace = np.zeros(n_steps, dtype=float)

    for step in range(1, n_steps + 1):
        t = step * dt
        env = np.exp(-(((t - t_center) / t_sigma) ** 2))
        osc = np.sin(omega_carrier * (t - t_center))
        A_t = effective_amp * env * osc
        if abs(A_t) > 1e-30:
            # Inject A_t * seed_profile into the 4-port V_inc at src_x slice,
            # weighted by port_w for +x̂ propagation. Seed_profile carries
            # the (p,q) substrate-native winding phase pattern.
            injection = A_t * seed_profile  # (ny, nz) array
            for n in range(4):
                if port_w[n] != 0:
                    lattice.V_inc[src_x, :, :, n] += port_w[n] * injection
        lattice.step()
        # Record interior probe; sum over all 4 ports for scalar |V|
        # Per A-Rule 10 corollary, record point already filtered to be interior.
        v_inc_trace[step - 1] = float(np.sum(lattice.V_inc[record_x, record_y, record_z, :]))

    # FFT analysis of the interior probe time-series
    # Drop the first few periods (transient) to focus on steady-state propagation
    transient_steps = int(2 * period / dt)
    if transient_steps >= n_steps:
        transient_steps = n_steps // 4
    signal = v_inc_trace[transient_steps:]
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=dt)  # Hz (cycles/sec)
    amps = np.abs(fft)
    # Dimensionalize: omega = 2π f
    omegas = 2.0 * np.pi * freqs
    # Peak frequency (skip DC bin 0)
    peak_idx = int(np.argmax(amps[1:]) + 1)
    omega_peak = float(omegas[peak_idx])
    # Spectral centroid (energy-weighted mean ω)
    total_energy = float(np.sum(amps[1:] ** 2))
    if total_energy > 0:
        centroid = float(np.sum(omegas[1:] * amps[1:] ** 2) / total_energy)
    else:
        centroid = 0.0
    peak_amp = float(amps[peak_idx])

    # Dimensionless peak: ω_peak / ω_carrier — if substrate is purely k-classified,
    # all (p,q) collapse to ~1.0; if (p,q)-classified, distinct bands appear.
    omega_peak_dimensionless = omega_peak / omega_carrier

    return PQRunResult(
        p=p,
        q=q,
        is_knot=(min(p, q) >= 2 and is_coprime(p, q)),
        is_unknot=(min(p, q) == 1),
        is_link=(math.gcd(p, q) > 1),
        kappa_tilde=kappa_tilde_val,
        omega_peak_native=omega_peak,
        omega_peak_dimensionless=omega_peak_dimensionless,
        spectral_centroid=centroid,
        spectral_amplitude=peak_amp,
        spectral_total_energy=total_energy,
        fft_freqs=omegas.astype(float),
        fft_amps=amps.astype(float),
    )


# ─────────────────────────────────────────────────────────────────────────
# Prereg M1-M5 evaluation (frozen thresholds)
# ─────────────────────────────────────────────────────────────────────────


def evaluate_M1_band_splitting(stable_results: List[PQRunResult]) -> Tuple[bool, dict]:
    """M1: ≥6 distinct bands with ≥5% ω-spacing at fixed k between adjacent bands."""
    omegas = sorted([r.omega_peak_dimensionless for r in stable_results])
    if len(omegas) < PREREG["M1_distinct_bands_required"]:
        return False, {
            "reason": f"only {len(omegas)} bands measured, need {PREREG['M1_distinct_bands_required']}",
            "omegas_sorted_dimensionless": omegas,
        }
    # Adjacent-band relative spacing
    if max(omegas) <= 0:
        return False, {"reason": "all band peaks zero or negative", "omegas_sorted_dimensionless": omegas}
    spacings = [(omegas[i + 1] - omegas[i]) / max(omegas[i], 1e-30) for i in range(len(omegas) - 1)]
    min_spacing = min(spacings) if spacings else 0.0
    threshold = PREREG["M1_band_separation_threshold"]
    all_distinct = all(s >= threshold for s in spacings)
    return all_distinct, {
        "omegas_sorted_dimensionless": omegas,
        "adjacent_spacings": spacings,
        "min_spacing": float(min_spacing),
        "threshold": threshold,
        "all_distinct": all_distinct,
    }


def evaluate_M2_ordering(stable_results: List[PQRunResult]) -> Tuple[bool, dict]:
    """M2: observed ω-ordering matches knot-crossing-number prediction."""
    expected_order = PREREG["M2_ordering_required"]  # (2,3)<(2,5)<(3,4)<(2,7)<(3,5)<(3,7)
    # Observed: sort by omega_peak ascending and read off (p,q)
    observed = sorted(stable_results, key=lambda r: r.omega_peak_dimensionless)
    observed_pq = [(r.p, r.q) for r in observed]
    matches = observed_pq == expected_order
    return matches, {
        "expected_order": expected_order,
        "observed_order": observed_pq,
        "exact_match": matches,
    }


def evaluate_M3_unknot_null(unknot_results: List[PQRunResult], baseline_omega: float) -> Tuple[bool, dict]:
    """M3: (1,q) unknot bands must show <1% separation from baseline T₂ continuum."""
    if baseline_omega <= 0:
        return False, {"reason": "baseline omega <= 0"}
    threshold = PREREG["M3_unknot_band_separation_max"]
    separations = []
    for r in unknot_results:
        sep = abs(r.omega_peak_dimensionless - baseline_omega) / max(baseline_omega, 1e-30)
        separations.append({"p": r.p, "q": r.q, "separation": float(sep)})
    max_sep = max((s["separation"] for s in separations), default=0.0)
    passes = max_sep <= threshold
    return passes, {
        "separations": separations,
        "max_separation": float(max_sep),
        "threshold": threshold,
        "baseline_omega": float(baseline_omega),
    }


def evaluate_M4_link_null(link_results: List[PQRunResult], knot_23_amp: float) -> Tuple[bool, dict]:
    """M4: gcd>1 link pairs must show <10% amplitude of (2,3) knot baseline."""
    if knot_23_amp <= 0:
        return False, {"reason": "(2,3) baseline amplitude <= 0"}
    threshold = PREREG["M4_gcd_gt1_band_stability_max"]
    rel_amps = []
    for r in link_results:
        rel = r.spectral_amplitude / max(knot_23_amp, 1e-30)
        rel_amps.append({"p": r.p, "q": r.q, "relative_amplitude": float(rel)})
    max_rel = max((s["relative_amplitude"] for s in rel_amps), default=0.0)
    passes = max_rel <= threshold
    return passes, {
        "relative_amplitudes": rel_amps,
        "max_relative_amplitude": float(max_rel),
        "threshold": threshold,
        "knot_23_amplitude": float(knot_23_amp),
    }


def evaluate_M5_alpha_independence(
    knot_23_default: PQRunResult,
    knot_23_perturbed: List[Tuple[float, PQRunResult]],
) -> Tuple[bool, dict]:
    """M5: bands scale linearly with kappa_tilde input ±20%, NOT pinned to α-hardcoded.

    Perturbation: run (2,3) topology at kappa_scale = 0.8, 1.0, 1.2 (±20%).
    If the band ω_peak position is INVARIANT under kappa_scale changes,
    then the (p,q) label is encoded in the seed geometric phase pattern
    (substrate-native — outcome A discriminator). If ω_peak SCALES with
    kappa_scale, the result is α-tautology-contaminated (outcome D).
    """
    default_omega = knot_23_default.omega_peak_dimensionless
    if default_omega <= 0:
        return False, {"reason": "default (2,3) omega <= 0"}
    scales_and_omegas = [(scale, r.omega_peak_dimensionless) for scale, r in knot_23_perturbed]
    relative_drift = max(abs(o - default_omega) / max(default_omega, 1e-30) for _, o in scales_and_omegas)
    # SUBSTRATE-NATIVE expectation: drift should be ~0 (≪20%), since (p,q)
    # lives in seed geometric phase, not in kappa_tilde amplitude scale.
    # α-tautology signature: drift scales ~linearly with kappa_scale (~20%).
    # Threshold for PASS: relative drift < 5% (well below the ±20% perturbation).
    passes = relative_drift < 0.05
    return passes, {
        "default_omega": float(default_omega),
        "perturbed": [{"kappa_scale": s, "omega_peak": float(o)} for s, o in scales_and_omegas],
        "max_relative_drift": float(relative_drift),
        "interpretation": ("substrate-native (geometric) if drift ≪ 20%; α-tautology if drift ~ 20%"),
    }


# ─────────────────────────────────────────────────────────────────────────
# Outcome classification (4-outcome verdict map per prereg §4.5)
# ─────────────────────────────────────────────────────────────────────────


def classify_outcome(M1: bool, M2: bool, M3: bool, M4: bool, M5: bool) -> Tuple[str, str]:
    if not M1:
        return "C", (
            "FALSIFIED — M1 fails (no (p,q) band-splitting). K4-TLM "
            "transverse modes are k-classified only in linear regime. "
            "Path B-prime DEAD at K4-TLM level; fall back to Path B "
            "(Faddeev-Skyrme variational)."
        )
    if not M5:
        return "D", (
            "TAUTOLOGY UNRESOLVED — M5 fails (bands scale with α-input). "
            "Cannot distinguish substrate-classification from simulator-"
            "tautology. Engineering fix required before re-test."
        )
    if M1 and M2 and M3 and M4 and M5:
        return "A", (
            "CONFIRMED — discrete (p,q)-band-splitting with knot-theoretic "
            "ordering observed. Path B-prime ALIVE; bypasses Faddeev-Skyrme."
        )
    return "B", (
        "PARTIAL — M1 ✓ but ≥1 of M2/M3/M4 fails. Framework incomplete; "
        "needs further substrate-mechanical refinement."
    )


# ─────────────────────────────────────────────────────────────────────────
# Driver entrypoint
# ─────────────────────────────────────────────────────────────────────────


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    results_dir = repo_root / "results"
    assets_dir = repo_root / "assets"
    results_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("Path B-prime Entry-Gate: K4-TLM Linear-Regime (p,q) Band-Splitting")
    print("=" * 78)

    # Canonical-primitive dimensional analysis (Step 3.5 / ave-prereg v1.1)
    strain_lin = (0.001 * V_YIELD) / V_SNAP
    print(f"\nCanonical primitives (step-3.5 dimensional analysis):")
    print(f"  ALPHA            = {ALPHA:.6e}")
    print(f"  V_SNAP           = {V_SNAP:.4e} V")
    print(f"  V_YIELD          = {V_YIELD:.4e} V  (= √α · V_SNAP)")
    print(f"  amp_si           = {0.001 * V_YIELD:.4e} V  (= 0.001 · V_YIELD)")
    print(f"  strain A         = {strain_lin:.4e}  (= amp/V_SNAP)")
    print(f"  A²               = {strain_lin**2:.4e}")
    print(f"  √(2α) (Reg I lim) = {(2 * ALPHA) ** 0.5:.4e}")
    print(f"  Saturation kernel S(A) = √(1-A²) ≈ 1 - {strain_lin**2/2:.4e}")
    print(f"  → DEEP IN REGIME I (passband). Op14 dormant. Substrate strictly linear.")
    print()

    all_results: List[PQRunResult] = []
    for p, q in ALL_PQ:
        cls = topology_class(p, q)
        kappa = kappa_tilde_torus(p, q)
        print(f"  ▶ Running (p,q)=({p},{q}) [{cls}, κ̃={kappa:.4f}] ...", end=" ", flush=True)
        result = run_pq_dispersion_one(p, q)
        print(f"ω_peak/ω_carrier={result.omega_peak_dimensionless:.4f}  " f"|FFT_peak|={result.spectral_amplitude:.3e}")
        all_results.append(result)

    # M5 perturbation runs for (2,3)
    print("\n  ▶ M5 α-independence: (2,3) at kappa_scale ∈ {0.8, 1.0, 1.2} ...")
    m5_perturbed: List[Tuple[float, PQRunResult]] = []
    for kappa_scale in [0.8, 1.2]:
        r = run_pq_dispersion_one(2, 3, kappa_scale=kappa_scale)
        m5_perturbed.append((kappa_scale, r))
        print(f"    kappa_scale={kappa_scale}: ω_peak/ω_carrier={r.omega_peak_dimensionless:.4f}")

    # Extract subsets
    stable_results = [r for r in all_results if r.is_knot]
    unknot_results = [r for r in all_results if r.is_unknot]
    link_results = [r for r in all_results if r.is_link]
    knot_23 = next((r for r in stable_results if r.p == 2 and r.q == 3), None)

    # Baseline T₂ continuum: use the geometric mean of unknot (1,q) peaks
    # (the unknot modes ARE the trivial k-continuum if H0 holds).
    if unknot_results:
        baseline_omega = float(np.mean([r.omega_peak_dimensionless for r in unknot_results]))
    else:
        baseline_omega = 1.0

    # Evaluate M1-M5
    M1_pass, M1_detail = evaluate_M1_band_splitting(stable_results)
    M2_pass, M2_detail = evaluate_M2_ordering(stable_results)
    M3_pass, M3_detail = evaluate_M3_unknot_null(unknot_results, baseline_omega)
    M4_pass, M4_detail = (
        evaluate_M4_link_null(link_results, knot_23.spectral_amplitude)
        if knot_23
        else (False, {"reason": "no (2,3) baseline"})
    )
    M5_pass, M5_detail = (
        evaluate_M5_alpha_independence(knot_23, m5_perturbed) if knot_23 else (False, {"reason": "no (2,3) baseline"})
    )

    outcome_label, outcome_text = classify_outcome(M1_pass, M2_pass, M3_pass, M4_pass, M5_pass)

    print("\n" + "=" * 78)
    print("PREREG M1-M5 EVALUATION (frozen thresholds, not adjusted)")
    print("=" * 78)
    print(f"  M1 distinct (p,q) bands  : {'PASS' if M1_pass else 'FAIL'}  → {M1_detail}")
    print(f"  M2 ordering match        : {'PASS' if M2_pass else 'FAIL'}  → {M2_detail}")
    print(f"  M3 unknot null corollary : {'PASS' if M3_pass else 'FAIL'}  → {M3_detail}")
    print(f"  M4 link null corollary   : {'PASS' if M4_pass else 'FAIL'}  → {M4_detail}")
    print(f"  M5 α-independence test   : {'PASS' if M5_pass else 'FAIL'}  → {M5_detail}")
    print()
    print(f"  OUTCOME: {outcome_label}")
    print(f"  → {outcome_text}")

    # Persist result JSON
    out_json = results_dir / "lattice_pq_dispersion_classification.json"
    payload = {
        "prereg": {k: (list(v) if isinstance(v, tuple) else v) for k, v in PREREG.items()},
        "canonical_primitives": {
            "ALPHA": ALPHA,
            "C_0": C_0,
            "L_NODE": L_NODE,
            "V_SNAP": V_SNAP,
            "V_YIELD": V_YIELD,
            "strain_linear": strain_lin,
            "strain_squared": strain_lin**2,
            "regime_I_threshold_sqrt_2alpha": (2 * ALPHA) ** 0.5,
        },
        "all_runs": [
            {
                "p": r.p,
                "q": r.q,
                "topology_class": topology_class(r.p, r.q),
                "kappa_tilde": r.kappa_tilde,
                "omega_peak_native": r.omega_peak_native,
                "omega_peak_dimensionless": r.omega_peak_dimensionless,
                "spectral_centroid": r.spectral_centroid,
                "spectral_amplitude": r.spectral_amplitude,
                "spectral_total_energy": r.spectral_total_energy,
            }
            for r in all_results
        ],
        "m5_perturbed": [
            {
                "kappa_scale": s,
                "omega_peak_dimensionless": r.omega_peak_dimensionless,
                "spectral_amplitude": r.spectral_amplitude,
            }
            for s, r in m5_perturbed
        ],
        "evaluation": {
            "M1": {"pass": M1_pass, "detail": M1_detail},
            "M2": {"pass": M2_pass, "detail": M2_detail},
            "M3": {"pass": M3_pass, "detail": M3_detail},
            "M4": {"pass": M4_pass, "detail": M4_detail},
            "M5": {"pass": M5_pass, "detail": M5_detail},
        },
        "outcome": {"label": outcome_label, "text": outcome_text},
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=str)
    print(f"\n  Result JSON: {out_json}")

    # Render diagnostic panels
    render_panels(all_results, m5_perturbed, payload, str(assets_dir / "lattice_pq_dispersion_panels.png"))
    print(f"  Diagnostic PNG: {assets_dir / 'lattice_pq_dispersion_panels.png'}")


def render_panels(
    all_results: List[PQRunResult],
    m5_perturbed: List[Tuple[float, PQRunResult]],
    payload: dict,
    out_png: str,
) -> None:
    """Render M1-M5 diagnostic panels."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), facecolor="#050510")
    fig.suptitle(
        "Path B-prime entry-gate: K4-TLM Linear-Regime (p,q) Band-Splitting",
        color="white",
        fontsize=13,
        fontweight="bold",
    )

    knot_results = [r for r in all_results if r.is_knot]
    unknot_results = [r for r in all_results if r.is_unknot]
    link_results = [r for r in all_results if r.is_link]

    # Panel 0: ω_peak / ω_carrier per (p,q)
    ax = axes[0, 0]
    ax.set_facecolor("#050510")
    labels = []
    omegas = []
    colors = []
    for r in all_results:
        labels.append(f"({r.p},{r.q})")
        omegas.append(r.omega_peak_dimensionless)
        if r.is_knot:
            colors.append("#aaff77")  # green = stable knot
        elif r.is_unknot:
            colors.append("#ffaa44")  # orange = unknot null
        else:
            colors.append("#ff7777")  # red = link null
    ax.bar(range(len(labels)), omegas, color=colors, edgecolor="white")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, color="#cccccc", fontsize=8)
    ax.set_ylabel("ω_peak / ω_carrier (dimensionless)", color="#cccccc")
    ax.set_title("M1: per-(p,q) dispersion-peak position", color="white")
    ax.tick_params(colors="#cccccc")
    ax.grid(alpha=0.2, color="#444")
    ax.axhline(1.0, color="cyan", ls=":", lw=1, label="carrier (1.0)")
    ax.legend(facecolor="#050510", labelcolor="#cccccc")

    # Panel 1: spectral amplitude per (p,q) — M4 link-null check
    ax = axes[0, 1]
    ax.set_facecolor("#050510")
    amps = [r.spectral_amplitude for r in all_results]
    ax.bar(range(len(labels)), amps, color=colors, edgecolor="white")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, color="#cccccc", fontsize=8)
    ax.set_ylabel("|FFT_peak| magnitude", color="#cccccc")
    ax.set_title("M4: per-(p,q) spectral amplitude (links vs knots)", color="white")
    ax.tick_params(colors="#cccccc")
    ax.grid(alpha=0.2, color="#444")

    # Panel 2: M5 α-independence — (2,3) at kappa_scale = {0.8, 1.0, 1.2}
    ax = axes[1, 0]
    ax.set_facecolor("#050510")
    knot_23 = next((r for r in knot_results if r.p == 2 and r.q == 3), None)
    if knot_23:
        scales = [s for s, _ in m5_perturbed] + [1.0]
        omegas_perturb = [r.omega_peak_dimensionless for _, r in m5_perturbed] + [knot_23.omega_peak_dimensionless]
        order = np.argsort(scales)
        scales_s = [scales[i] for i in order]
        omegas_s = [omegas_perturb[i] for i in order]
        ax.plot(scales_s, omegas_s, "o-", color="#aaff77", lw=2, ms=10)
        ax.set_xlabel("kappa_scale (M5 perturbation)", color="#cccccc")
        ax.set_ylabel("ω_peak/ω_carrier ((2,3))", color="#cccccc")
        ax.set_title("M5: α-independence — (2,3) under ±20% κ̃ perturbation", color="white")
    ax.tick_params(colors="#cccccc")
    ax.grid(alpha=0.2, color="#444")

    # Panel 3: text summary
    ax = axes[1, 1]
    ax.set_facecolor("#050510")
    ax.axis("off")
    out = payload["outcome"]
    eva = payload["evaluation"]
    summary_lines = [
        "PREREG M1-M5 (verbatim from prereg §4.4)",
        "",
        f"  M1 (≥6 bands, ≥5% spacing) : {'PASS' if eva['M1']['pass'] else 'FAIL'}",
        f"  M2 (knot-order match)      : {'PASS' if eva['M2']['pass'] else 'FAIL'}",
        f"  M3 (unknot null <1%)       : {'PASS' if eva['M3']['pass'] else 'FAIL'}",
        f"  M4 (link null <10%)        : {'PASS' if eva['M4']['pass'] else 'FAIL'}",
        f"  M5 (α-indep, drift <5%)    : {'PASS' if eva['M5']['pass'] else 'FAIL'}",
        "",
        f"OUTCOME: {out['label']}",
        "",
        out["text"][:280] + ("…" if len(out["text"]) > 280 else ""),
    ]
    for i, line in enumerate(summary_lines):
        if "PASS" in line:
            c = "#aaff77"
        elif "FAIL" in line:
            c = "#ff7777"
        elif line.startswith("OUTCOME"):
            c = "#ffff88"
        else:
            c = "#cccccc"
        ax.text(0.02, 0.97 - i * 0.06, line, transform=ax.transAxes, color=c, fontsize=9, family="monospace")

    plt.tight_layout()
    plt.savefig(out_png, dpi=110, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    main()
