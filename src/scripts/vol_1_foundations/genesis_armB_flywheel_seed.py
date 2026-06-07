"""
Genesis Arm B — the minimal-IC flywheel seed (electron in three numbers).

Prereg (FROZEN): research/2026-06-06_genesis-armB-flywheel-seed-prereg.md
Parallel to Arm A (two-photon collision). Branch: analysis/2026-06-06-genesis-armB-flywheel-seed.

THE QUESTION (Grant 2026-06-06): does the minimal IC {ω, R of the collimated
B-flywheel, chirality of the E field} relax — under the engine's force-free
(Beltrami) dynamics — into the electron: the (2,3) winding at J×B→0, charge =
the chirality input, mass = ½LI²? I.e., is the electron just three numbers,
with the (2,3) emerging as the force-free attractor of a bare collimated
B-flywheel?

────────────────────────────────────────────────────────────────────────────
substrate-native-check (v1.1) — the walk, BEFORE the code (operating principle 1)
────────────────────────────────────────────────────────────────────────────
CP8 (emergence/hosting — load-bearing). The test is "does the engine
  autonomously host the electron (2,3) from the bare flywheel?". So we seed the
  GENERATIVE PRECURSOR — a bare collimated B-flywheel parameterized by exactly
  {ω, R, chirality} — and let the engine's OWN dynamics build (or fail to build)
  the (2,3). We do NOT plant the (2,3) end-state. `initialize_flywheel_seed`
  below is provably DISTINCT from `initialize_2_3_voltage_ansatz`
  (tlm_electron_soliton_eigenmode.py:34): NO θ=2φ+3ψ winding, NO (2,3)
  knot-tangent port projection, NO toroidal shell — a cylindrical single-helicity
  Lundquist force-free flux rope (a flywheel). Matched-distribution baseline
  (`make_matched_baseline`): SAME per-cell amplitude statistics, collimation +
  chirality DESTROYED (randomized ω directions, zero net helicity). Emergence
  must beat the baseline BECAUSE OF STRUCTURE. Each non-hostable layer
  (collimation / winding / charge / spin) is a STRUCTURAL-CAPABILITY finding,
  not a failure → discriminators (II)/(III) are valid (ave-evidence-framing).

CP1 (substrate dynamics = wave, NOT minimization). The "force-free relaxation"
  is `engine.step()` running K4-TLM scatter+connect + Cosserat velocity-Verlet.
  This IS wave propagation. We do NOT call relax_s11 / any gradient-descent /
  energy-functional minimizer. No SM energy-basin language.

CP2 (sector). The B-flywheel lives in the Cosserat ω sector (the inductive /
  microrotation-B flywheel — 3 microrotational-B DOF, dual-reactance taxonomy).
  The (2,3) emergence read lives in the V-sector (K4-TLM) phase-space (V_inc =
  C-state, Φ_link = L-state). Cross-coupled via Op14. A bare ω seed alone does
  NOT source V_inc under this config (verified: |V_inc|max stays 0) — so the
  flywheel precursor deposits BOTH the magnetic (Cosserat ω) AND electric (K4
  V_inc) halves of one coherent single-helicity Beltrami EM blob.

CP3 (objective = AVE-native). "Collimate" = force-free = J×B→0, the substrate-
  native Beltrami residual (∇×ω)×ω → 0, NOT an energy minimum. Read forward,
  no fit (ave-driver-script-honesty).

CP4 (phase-space coordinates). The (2,3) is read by the coordinate-correct
  extractor `extract_2_3_spatial` (r10_2_3_winding_extractor_coordinate.py) on
  the Clifford torus (internal U(1) phase from V_inc/Φ_link) — phase-space, NOT
  real-space (R,r). Reused verbatim. The J×B / mass / spin readouts are
  real-space Cosserat diagnostics, tagged consistency (not the load-bearing
  emergence claim).

CP5 (local clock). Op14 saturation active: ω_local(r)=ω_global·√(1−A²(r)). We
  report A²_max at the flywheel core so the local-clock modulation is on record.

CP6 (reactance pair). Time-domain LC test → we record BOTH the C-state
  (capacitive: K4 V_inc + Cosserat ω) AND the L-state (inductive: K4 Φ_link +
  Cosserat ω_dot) energy at every recording step, plus H=T+V, over the whole
  window. A one-phase snapshot cannot distinguish static from oscillator-at-peak.

CP7 (sampling). PML cells excluded (PML ≤ idx ≤ N−PML−1) before any top-K /
  shell read (the reused extractor already does this; our shell read inherits
  it). Shell density located at energy-density crest, not centroid+offset.

consistency-vs-emergence: mass=½LI²=½I_ω|ω|², spin=I_ω·∫ω, charge=winding-sign
  vs chirality → CONSISTENCY-class readouts (the amplitude is PINNED by the mass,
  so reading it back is self-consistency, not emergence). The (2,3)-from-bare-
  flywheel is the EMERGENCE-class claim.

ave-canonical-source: ω_C, ℓ_node, m_e, ALPHA, V_yield from ave.core.constants.
  Native units: c=ℏ=m_e=ℓ_node=1, V_SNAP=1 ⇒ ω_C=c/ℓ_node=1, spin ℏ/2=0.5,
  electron rest energy m_ec²=1.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.special import j0, j1

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import jax.numpy as jnp  # noqa: E402
from r10_2_3_winding_extractor_coordinate import (  # noqa: E402
    extract_2_3_spatial,
    is_2_3,
    shell_params_from_field,
)

from ave.core.constants import ALPHA, V_SNAP, V_YIELD  # noqa: E402
from ave.topological.cosserat_field_3d import (  # noqa: E402
    _beltrami_helicity,
    _tetrahedral_curl,
)
from ave.topological.vacuum_engine import VacuumEngine3D  # noqa: E402

# ── Substrate-derived constants (ave-canonical-source; NO hardcoded literals) ──
DT = 1.0 / np.sqrt(2.0)  # K4-TLM 4-port junction timestep
COMPTON_PERIOD = 2.0 * np.pi  # ω_C = 1 native ⇒ one Compton period = 2π
OMEGA_C = 1.0  # ring frequency ω_C = c/ℓ_node = 1 (native)
SPIN_HALF = 0.5  # ℏ/2 in native units (ℏ = 1)
M_E_C2 = 1.0  # electron rest energy m_ec² = 1 (native)
V_YIELD_FRAC = float(V_YIELD / V_SNAP)  # √α ≈ 0.0854 (Regime-II onset, A²=√(2α))

# K4 tetrahedral A→B port directions (unit). The E-field flywheel is projected
# onto these (T₂ photon pattern: subtract the per-cell mean = A₁ projection).
PORT_DIRS = np.array(
    [
        [+1.0, +1.0, +1.0],
        [+1.0, -1.0, -1.0],
        [-1.0, +1.0, -1.0],
        [-1.0, -1.0, +1.0],
    ]
) / np.sqrt(3.0)


# ══════════════════════════════════════════════════════════════════════════════
# The flywheel seeder (CP8 generative precursor — DISTINCT from the (2,3) ansatz)
# ══════════════════════════════════════════════════════════════════════════════
def initialize_flywheel_seed(engine, R, omega, chirality, mass_target=M_E_C2):
    """Seed a bare collimated B-flywheel parameterized by EXACTLY {ω, R, chirality}.

    The flywheel is a localized single-helicity Lundquist force-free flux rope
    (a Beltrami "flywheel" spinning about ẑ): in cylindrical (ρ, φ, z) about the
    lattice centre, with twist wavenumber k = ω/c (native c=1 ⇒ k = ω):

        ω_z(ρ)  = A · env(ρ,z) · J₀(k ρ)          (collimated axial spin)
        ω_φ(ρ)  = A · chirality · env(ρ,z) · J₁(k ρ)   (azimuthal circulation)
        ω_ρ     = 0

    J₀/J₁ make ∇×ω = k ω EXACTLY in the unwindowed column (the Lundquist /
    Gold-Hoyle constant-pitch force-free field); the localizing envelope `env`
    (radial scale R, gentle z-column) is what makes it a *flywheel* (finite) and
    introduces the only departure from exact force-free. `chirality` ∈ {+1, −1}
    flips ω_φ → flips the Beltrami helicity sign h = ω·(∇×ω)/(|ω||∇×ω|) → the
    seeded handedness (LH = e⁻, RH = e⁺ per pair-production-axiom:77).

    The electron point is ω·R = c (Compton, prereg §1): with R in cells and
    ω = c/R native, k·R = 1 — ONE helical twist per flywheel radius.

    The E-field half of the flywheel (the "chirality of the E field") is the SAME
    Beltrami vector field projected onto the K4 ports (T₂ photon pattern) into
    V_inc, so the precursor deposits a coherent single-helicity EM blob in BOTH
    reactance sectors. Amplitude A is PINNED so ½·I_ω·Σ|ω|² = mass_target
    (= m_ec² = 1; prereg §1 ½LI² = m_ec²). The K4 V_inc inherits A (same field).

    DISTINCTNESS (CP8, vs initialize_2_3_voltage_ansatz): no θ=2φ+3ψ, no (2,3)
    knot-tangent chirality_weight, no toroidal shell. A cylindrical Bessel flux
    rope. The (2,3), if it is the force-free attractor, must EMERGE.

    Returns a dict of the seeded IC (R, omega, chirality, amplitude, masses).
    """
    N = engine.N
    c = (N - 1) / 2.0
    ii, jj, kk = np.indices((N, N, N))
    x, y, z = ii - c, jj - c, kk - c
    rho = np.sqrt(x * x + y * y) + 1e-9
    phi = np.arctan2(y, x)
    k = float(omega)  # k = ω/c, c = 1 native

    # Flywheel envelope: radial scale R, gentle z-column (2.5R) → a localized
    # spinning disk/rope. (Verified: a pure column is closer to force-free; the
    # taper is the finite-flywheel departure the test probes.)
    env = np.exp(-(rho * rho) / (2.0 * R * R)) * np.exp(-(z * z) / (2.0 * (2.5 * R) ** 2))

    w_z = env * j0(k * rho)
    w_phi = float(chirality) * env * j1(k * rho)
    w_x = -w_phi * np.sin(phi)
    w_y = w_phi * np.cos(phi)
    omega_vec = np.stack([w_x, w_y, w_z], axis=-1) * engine.cos.mask_alive[..., None]

    # Pin amplitude by the mass condition ½·I_ω·Σ|ω|² = mass_target (prereg §1).
    raw_mass = 0.5 * engine.cos.I_omega * float(np.sum(omega_vec**2))
    A = np.sqrt(mass_target / raw_mass) if raw_mass > 0 else 0.0
    omega_vec *= A
    engine.cos.omega[:] = omega_vec
    engine.cos.omega_dot[:] = 0.0  # flywheel born at rest in the L-state (ω̇=0)

    # E-field half: the SAME Beltrami vector field projected onto K4 ports,
    # T₂-projected (subtract per-cell mean = A₁ photon pattern), into V_inc.
    proj = omega_vec @ PORT_DIRS.T  # (N,N,N,4) = ω·p̂ per port
    proj -= proj.mean(axis=-1, keepdims=True)  # T₂ projection (remove A₁/mean)
    engine.k4.V_inc[:] = proj * engine.k4.mask_active[..., None]
    engine.k4.V_ref[:] = 0.0
    engine.k4.Phi_link[:] = 0.0

    return {
        "R": float(R),
        "omega": float(omega),
        "k_twist": k,
        "kR": float(k * R),
        "chirality": int(chirality),
        "amplitude": float(A),
        "mass_seed": float(0.5 * engine.cos.I_omega * np.sum(engine.cos.omega**2)),
        "V_inc_max_seed": float(np.abs(engine.k4.V_inc).max()),
        "omega_max_seed": float(np.abs(engine.cos.omega).max()),
    }


def make_matched_baseline(engine, R, omega, chirality, mass_target=M_E_C2, seed=0):
    """Matched-distribution baseline (CP8 MANDATORY). Same per-cell |ω| amplitude
    statistics as the flywheel, but collimation + chirality DESTROYED: the ω
    direction at each cell is randomized on S² (isotropic), so the net Beltrami
    helicity → 0 and there is no coherent twist. Same envelope, same total mass
    (½I_ω Σ|ω|² = mass_target), same V_inc projection. Emergence (the (2,3))
    must beat THIS — anything it produces is amplitude/saturation, not structure.
    """
    N = engine.N
    c = (N - 1) / 2.0
    ii, jj, kk = np.indices((N, N, N))
    x, y, z = ii - c, jj - c, kk - c
    rho = np.sqrt(x * x + y * y) + 1e-9
    k = float(omega)
    env = np.exp(-(rho * rho) / (2.0 * R * R)) * np.exp(-(z * z) / (2.0 * (2.5 * R) ** 2))
    # per-cell magnitude matched to the flywheel: |ω|(ρ) = env·√(J0²+J1²)
    mag = env * np.sqrt(j0(k * rho) ** 2 + j1(k * rho) ** 2)
    rng = np.random.default_rng(seed)
    dirs = rng.standard_normal((N, N, N, 3))
    dirs /= np.linalg.norm(dirs, axis=-1, keepdims=True) + 1e-12
    omega_vec = (mag[..., None] * dirs) * engine.cos.mask_alive[..., None]
    raw_mass = 0.5 * engine.cos.I_omega * float(np.sum(omega_vec**2))
    A = np.sqrt(mass_target / raw_mass) if raw_mass > 0 else 0.0
    omega_vec *= A
    engine.cos.omega[:] = omega_vec
    engine.cos.omega_dot[:] = 0.0
    proj = omega_vec @ PORT_DIRS.T
    proj -= proj.mean(axis=-1, keepdims=True)
    engine.k4.V_inc[:] = proj * engine.k4.mask_active[..., None]
    engine.k4.V_ref[:] = 0.0
    engine.k4.Phi_link[:] = 0.0
    return {
        "R": float(R),
        "omega": float(omega),
        "chirality": int(chirality),
        "amplitude": float(A),
        "mass_seed": float(raw_mass * A * A),
        "baseline": True,
    }


# ══════════════════════════════════════════════════════════════════════════════
# Substrate-native diagnostics (forward reads, NO fit)
# ══════════════════════════════════════════════════════════════════════════════
def force_free_residual(engine):
    """Check-1 metric — the substrate-native J×B residual. The "current" J is the
    Cosserat curl κ = ∇×ω; the "field" B is ω. Force-free / collimated ⟺
    J×B = (∇×ω)×ω → 0. We report the field-strength-weighted misalignment

        ff_res = Σ |(∇×ω)×ω| / Σ (|∇×ω|·|ω|)  ∈ [0,1]

    (0 = perfectly force-free/collimated, 1 = J⊥B everywhere). PML/inactive
    excluded via mask_alive. Returns (ff_res, mean|h_local|), where h_local is the
    normalized Beltrami helicity (|h|→1 ⟺ Beltrami)."""
    w = jnp.asarray(engine.cos.omega)
    curl = np.asarray(_tetrahedral_curl(w, engine.cos.dx))
    cross = np.cross(curl, engine.cos.omega)
    wsq = np.sum(engine.cos.omega**2, axis=-1)
    cn = np.linalg.norm(curl, axis=-1)
    wn = np.sqrt(wsq)
    m = engine.cos.mask_alive & (wsq > 1e-12)
    if not m.any():
        return float("nan"), float("nan")
    ff = float(np.sum(np.linalg.norm(cross, axis=-1)[m]) / (np.sum((cn * wn)[m]) + 1e-12))
    h = np.asarray(_beltrami_helicity(w, engine.cos.dx))
    return ff, float(np.abs(h[m]).mean())


def signed_helicity(engine):
    """Check-3 readout — the seeded handedness as it survives. Field-strength-
    weighted SIGNED Beltrami helicity h = ω·(∇×ω)/(|ω||∇×ω|), weighted by |ω|².
    Sign = charge polarity (LH<0 = e⁻, RH>0 = e⁺ convention here follows the
    seeded ω_φ sign = chirality). Returns the |ω|²-weighted mean signed h."""
    w = jnp.asarray(engine.cos.omega)
    h = np.asarray(_beltrami_helicity(w, engine.cos.dx))
    wsq = np.sum(engine.cos.omega**2, axis=-1)
    m = engine.cos.mask_alive & (wsq > 1e-12)
    if not m.any():
        return float("nan")
    return float(np.sum(h[m] * wsq[m]) / (np.sum(wsq[m]) + 1e-30))


def flywheel_mass(engine):
    """Check-4 readout (CONSISTENCY) — mass = ½LI² = ½·I_ω·Σ|ω|² (the inductive-
    flywheel rotational energy). Native m_ec² = 1."""
    return float(0.5 * engine.cos.I_omega * np.sum(engine.cos.omega**2 * engine.cos.mask_alive[..., None]))


def flywheel_spin(engine):
    """Check-5 readout (CONSISTENCY) — spin = I_ω·∫ω (the net microrotation
    angular momentum). We report the axial component S_z = I_ω·Σω_z (the flywheel
    spin axis) and |S|. Native ℏ/2 = 0.5."""
    msk = engine.cos.mask_alive[..., None]
    S = engine.cos.I_omega * np.sum(engine.cos.omega * msk, axis=(0, 1, 2))  # (3,)
    return float(S[2]), float(np.linalg.norm(S))


def reactance_pair(engine):
    """CP6 — the LC reactance pair, recorded at every step over the window.
    C-state (capacitive): K4 V_inc + Cosserat ω. L-state (inductive): K4 Φ_link +
    Cosserat ω_dot. Plus H = T + V (conservation/anti-correlation check)."""
    mA = engine.k4.mask_A[..., None]
    mAl = engine.cos.mask_alive[..., None]
    E_C = float(0.5 * np.sum((engine.k4.V_inc) ** 2) + 0.5 * engine.cos.I_omega * np.sum((engine.cos.omega * mAl) ** 2))
    E_L = float(
        0.5 * np.sum((engine.k4.Phi_link * mA) ** 2)
        + 0.5 * engine.cos.I_omega * np.sum((engine.cos.omega_dot * mAl) ** 2)
    )
    T = float(engine.cos.kinetic_energy())
    V = float(engine.cos.total_energy())
    return {"E_C": E_C, "E_L": E_L, "T_cos": T, "V_cos": V, "H_cos": T + V}


def a2_core(engine):
    """CP5 — peak K4 saturation A²=V²/V_SNAP² at the flywheel core (local clock
    ω_local=ω_global·√(1−A²)). PML excluded."""
    N = engine.N
    PML = engine.config.pml
    vsq = np.sum(engine.k4.V_inc**2, axis=-1) / (engine.V_SNAP**2)
    interior = np.zeros_like(vsq, dtype=bool)
    interior[PML : N - PML, PML : N - PML, PML : N - PML] = True
    a2 = vsq[interior & engine.k4.mask_active]
    a2max = float(a2.max()) if a2.size else 0.0
    return a2max, float(np.sqrt(max(0.0, 1.0 - min(a2max, 1.0 - 1e-12))))


# ══════════════════════════════════════════════════════════════════════════════
# Single run: seed the precursor, evolve under force-free relaxation, read battery
# ══════════════════════════════════════════════════════════════════════════════
def _new_engine(N, PML):
    """Coupled K4+Cosserat engine, Arm-C-matched config (the validated coupled
    config: asymmetric μ/ε saturation, Cosserat self-terms, A28 LC-force off)."""
    return VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def run_one(label, N, PML, n_periods, R, omega, chirality, baseline=False, mass_target=M_E_C2, rec_every=28, seed=0):
    """Seed the flywheel precursor (or matched baseline), evolve under the
    engine's own wave/force-free dynamics (CP1 — NO gradient descent), and read
    the 6-check battery forward (NO fit). Returns the full per-run record."""
    eng = _new_engine(N, PML)
    if baseline:
        ic = make_matched_baseline(eng, R, omega, chirality, mass_target, seed=seed)
    else:
        ic = initialize_flywheel_seed(eng, R, omega, chirality, mass_target)

    n_steps = int(n_periods * COMPTON_PERIOD / DT)
    # time-resolved traces (CP6 reactance pair + check-1 collimation + mass)
    ff0, h0 = force_free_residual(eng)
    rp0 = reactance_pair(eng)
    traj = {
        "step": [0],
        "ff_res": [ff0],
        "mean_abs_h": [h0],
        "mass": [flywheel_mass(eng)],
        "E_C": [rp0["E_C"]],
        "E_L": [rp0["E_L"]],
        "H_cos": [rp0["H_cos"]],
    }
    t0 = time.time()
    for s in range(n_steps):
        eng.step()
        if (s + 1) % rec_every == 0 or (s + 1) == n_steps:
            ff, h = force_free_residual(eng)
            rp = reactance_pair(eng)
            traj["step"].append(s + 1)
            traj["ff_res"].append(ff)
            traj["mean_abs_h"].append(h)
            traj["mass"].append(flywheel_mass(eng))
            traj["E_C"].append(rp["E_C"])
            traj["E_L"].append(rp["E_L"])
            traj["H_cos"].append(rp["H_cos"])
    elapsed = time.time() - t0

    # ── final-state battery (forward reads) ──
    ff_final, h_final = force_free_residual(eng)
    S_z, S_mag = flywheel_spin(eng)
    a2max, omega_local = a2_core(eng)
    # Check-2/3: the (2,3) extractor on the converged FULL field (phase-space, CP4)
    R2, r2, cx, cy, cz, kz = shell_params_from_field(eng.k4.V_inc, eng.k4.mask_A, N)
    ext = extract_2_3_spatial(eng.k4.V_inc, eng.k4.Phi_link, eng.k4.mask_A, N, PML, R2, r2, (cx, cy, cz), kz)
    ext.pop("_curve", None)
    cents = eng.cos.find_soliton_centroids(threshold_frac=0.3)

    rec = {
        "label": label,
        "baseline": bool(baseline),
        "ic": ic,
        "config": {
            "N": N,
            "PML": PML,
            "n_periods": n_periods,
            "n_steps": n_steps,
            "R": R,
            "omega": omega,
            "kR": float(omega * R),
            "chirality": int(chirality),
        },
        "elapsed_s": round(elapsed, 1),
        # Check 1 — collimate / J×B→0
        "check1_ff_res_seed": traj["ff_res"][0],
        "check1_ff_res_final": ff_final,
        "check1_collimated": bool(ff_final < 0.20),  # force-free pass bar
        "check1_ff_decreased": bool(ff_final < traj["ff_res"][0] - 0.02),
        "mean_abs_h_final": h_final,
        # Check 2 — (2,3) emerges (phase-space extractor; EMERGENCE-class)
        "check2_w1_base": ext["w1_base"],
        "check2_w2_fibre": ext["w2_fibre"],
        "check2_crossing_c": ext["crossing_count_c"],
        "check2_is_2_3": bool(is_2_3(ext)),
        "check2_n_shell_sites": ext.get("n_shell_sites", 0),
        # Check 3 — charge = chirality (signed helicity sign vs seeded handedness)
        "check3_signed_helicity_final": signed_helicity(eng),
        "check3_chirality_seed": int(chirality),
        # Check 4 — mass = ½LI² (CONSISTENCY)
        "check4_mass_seed": traj["mass"][0],
        "check4_mass_final": flywheel_mass(eng),
        # Check 5 — spin = Iω (CONSISTENCY)
        "check5_spin_Sz": S_z,
        "check5_spin_mag": S_mag,
        # Check 6 — sub-V_yield ring at ω_C, size ≈ ℓ_node (carry-forward gate)
        "check6_shell_R_cells": float(R2),
        "check6_shell_r_cells": float(r2),
        "check6_a2_core": a2max,
        "check6_sub_v_yield": bool(np.sqrt(a2max) < V_YIELD_FRAC),
        "check6_omega_local_over_global": omega_local,
        "n_centroids": len(cents),
        "ext_full": ext,
        "trace": traj,
    }
    return rec, eng


def _verdict_for(rec):
    """Per-run discriminator (prereg §4): (I) collimates → (2,3); (II) stable
    non-(2,3); (III) never collimates."""
    collimated = rec["check1_collimated"] or rec["check1_ff_decreased"]
    is23 = rec["check2_is_2_3"]
    if collimated and is23:
        return "I"
    if collimated and not is23:
        return "II"
    return "III"


def main():
    print("=" * 80, flush=True)
    print("  GENESIS ARM B — minimal-IC flywheel seed (electron in 3 numbers)")
    print("  Does the bare collimated B-flywheel {ω,R,chirality} relax into the")
    print("  (2,3) at J×B→0?  Forward reads, NO fit (ave-driver-script-honesty).")
    print("=" * 80, flush=True)
    print(
        f"  ALPHA={ALPHA}  V_yield/V_snap=√α={V_YIELD_FRAC:.4f}  "
        f"ω_C={OMEGA_C} ℏ/2={SPIN_HALF} m_ec²={M_E_C2} (native)\n",
        flush=True,
    )

    N, PML, n_periods = 40, 4, 36
    R_e = 9.0  # electron-scale flywheel radius (cells; ~0.22N,
    # matching the prior-art Arm-C hosted shell 0.22N)
    om_e = 1.0 / R_e  # electron point: ω·R = c ⇒ k·R = 1 (Compton)

    runs = []
    # ── PRIMARY: the electron point, both chiralities ──
    plan = [
        ("electron_LH", R_e, om_e, -1, False),  # LH Beltrami = e⁻
        ("electron_RH", R_e, om_e, +1, False),  # RH Beltrami = e⁺
        # ── MANDATORY matched-distribution baseline (same |ω| stats, no structure) ──
        ("matched_baseline", R_e, om_e, +1, True),
        # ── collimation control: a WELL-collimated seed (k·R=3) — does IT collimate? ──
        ("collimated_kR3", R_e, 3.0 / R_e, +1, False),
        # ── scale sweep: is (2,3)-emergence special at any R? ──
        ("sweep_R7", 7.0, 1.0 / 7.0, +1, False),
        ("sweep_R11", 11.0, 1.0 / 11.0, +1, False),
    ]
    for label, R, om, chir, base in plan:
        print(
            f"  ── {label}: R={R} ω={om:.4f} kR={om*R:.2f} chir={chir:+d}" f"{' [BASELINE]' if base else ''} ──",
            flush=True,
        )
        rec, _ = run_one(label, N, PML, n_periods, R, om, chir, baseline=base)
        v = _verdict_for(rec)
        rec["verdict"] = v
        runs.append(rec)
        print(
            f"     {rec['elapsed_s']}s | check1 ff_res {rec['check1_ff_res_seed']:.2f}"
            f"→{rec['check1_ff_res_final']:.2f} (collimate={rec['check1_collimated']}"
            f"/dec={rec['check1_ff_decreased']}) | check2 (2,3) w1={rec['check2_w1_base']}"
            f" w2={rec['check2_w2_fibre']} c={rec['check2_crossing_c']}"
            f" is23={rec['check2_is_2_3']} | check4 mass {rec['check4_mass_seed']:.2f}"
            f"→{rec['check4_mass_final']:.2f} | check5 Sz={rec['check5_spin_Sz']:.3f}"
            f" | check3 h̄={rec['check3_signed_helicity_final']:+.2f}"
            f" | → ({v})",
            flush=True,
        )

    # ── overall adjudication ──
    elec = [r for r in runs if r["label"].startswith("electron")]
    base = [r for r in runs if r["baseline"]]
    any_23_flywheel = any(r["check2_is_2_3"] for r in runs if not r["baseline"])
    any_23_baseline = any(r["check2_is_2_3"] for r in base)
    any_collimate = any(r["check1_collimated"] or r["check1_ff_decreased"] for r in runs if not r["baseline"])
    if any_23_flywheel and not any_23_baseline and any_collimate:
        overall = "I"
    elif any_collimate:
        overall = "II"
    else:
        overall = "III"

    summary = {
        "overall_verdict": overall,
        "any_2_3_from_flywheel": any_23_flywheel,
        "any_2_3_from_baseline": any_23_baseline,
        "any_collimation": any_collimate,
        "electron_point_verdicts": {r["label"]: r["verdict"] for r in elec},
        "discriminator_legend": {
            "I": "bare flywheel → (2,3) at J×B→0: {ω,R,chirality} IS the complete electron IC",
            "II": "relaxes to a stable non-(2,3) state: the IC underdetermines",
            "III": "never collimates (J×B stays finite): no force-free state from this seed",
        },
    }
    print("\n" + "=" * 80)
    print(f"  OVERALL VERDICT: ({overall}) — {summary['discriminator_legend'][overall]}")
    print(
        f"  (2,3) from flywheel: {any_23_flywheel} | from matched baseline: "
        f"{any_23_baseline} | any collimation: {any_collimate}"
    )
    print("=" * 80)

    out = {
        "config": {
            "N": N,
            "PML": PML,
            "n_periods": n_periods,
            "DT": DT,
            "ALPHA": ALPHA,
            "V_yield_frac": V_YIELD_FRAC,
            "omega_C": OMEGA_C,
            "spin_half": SPIN_HALF,
        },
        "summary": summary,
        "runs": runs,
    }
    op = Path(__file__).parent / "genesis_armB_flywheel_seed_results.json"
    op.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {op.name}")
    return out


if __name__ == "__main__":
    main()
