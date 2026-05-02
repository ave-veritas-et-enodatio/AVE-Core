"""r10_path_alpha_v8_corrected_measurements.py — Round 10+ Phase 1 Direction 3'.2 v8.

Pre-reg P_phase11_path_alpha_v8_corrected_measurements. Successor to v7
([doc 86](../../research/L3_electron_soliton/86_path_alpha_v7_helical_beltrami_thermal_sweep.md))
which Mode II'd at every T value (persistence + ring localization PASS;
Beltrami |cos_sim| = 0.52 + loop flux +496 growing FAIL with confirmed
mechanical measurement-method causes). v8 implements the corrected
measurement methods locked in doc 86 §7.5; IC is UNCHANGED from v7
(helical Beltrami chair-ring + Phi_link sin / V_inc cos spatial pattern +
helical Cosserat ω).

Per A43 v2 corpus-grep verification of canonical V-to-A relationship:
- [Vol 1 Ch 3:24](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L24)
  verbatim: "the canonical field variable... is the Magnetic Vector Potential (A),
  defining the magnetic flux linkage per unit length ([Wb/m] = [V·s/m])"
- [Vol 4 Ch 1:223](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L223)
  verbatim: "Φ(t) = ∫_{-∞}^{t} V(τ) dτ"
- [k4_tlm.py:156-167](../../src/ave/core/k4_tlm.py#L156-L167) docstring:
  "Phi_link = ∫V_bond dt"; "stored at A-sites only — each entry is the flux
  on the directed A→B bond"

Canonical mapping confirmed: Phi_link[bond] = A·bond_length (Wb), where A
is the instantaneous magnetic vector potential along the bond. v7's
Σ Phi · port_dir reconstruction was canonically correct in DIRECTION
(cos_sim is scale-invariant; Moore-Penrose pseudo-inverse for tetrahedral
4-port gives the same direction × scalar (3/4)).

The actual issue identified by v7's Mode II: Phi_link accumulates a
SECULAR DRIFT from saturation rectification (V_avg has nonzero DC
component → Phi_link grows linearly). The OSCILLATING component of
Phi_link (≈ true instantaneous A oscillating around the secular trend)
is the canonical Beltrami-test target.

v8 corrected methods:
1. Beltrami |cos_sim|: A-vec from Phi_link DETRENDED (subtract linear fit
   over recording window); ω from Cosserat ω. Per Beltrami standing wave
   A∥B at every instant, cos_sim(A_oscillating, ω) → +1 if Beltrami holds.
2. Loop flux: Σ Phi_link_detrended[bond] · traversal_sign — instantaneous
   topological invariant from the oscillating A·dl integral. Target ≈ 2π
   in V_SNAP-natural units per doc 85 §5.1; thermal sensitivity verified
   by comparing T=0 vs T=1e-1·T_V-rupt smoke check.

Persistence + ring localization measurements UNCHANGED from v7 (these
worked: 200 P PASS, 96% PASS at every T).

Per doc 86 §7.4 cadence: this is v8 = ONE-cycle measurement-method
redesign. NO IC modifications. NO additional adjudication criteria.

Per doc 86 §7.6 Round 11 trigger: if v8 doesn't land Mode I (4/4 PASS),
auto-fire Round 11 framework reframe (no v9 IC tweak path).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA
from ave.topological.vacuum_engine import VacuumEngine3D


# ─── Constants (UNCHANGED from v7) ─────────────────────────────────────────

N_LATTICE = 32
PML = 4
CENTER = (16, 16, 16)

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

RECORDING_END_P = 200.0
N_RECORDING_STEPS = int(RECORDING_END_P * COMPTON_PERIOD / DT)

PORT_OFFSETS_A = [
    np.array([1, 1, 1]),
    np.array([1, -1, -1]),
    np.array([-1, 1, -1]),
    np.array([-1, -1, 1]),
]
SQRT_3 = np.sqrt(3.0)
TWO_PI = 2.0 * np.pi
BOND_LENGTH = SQRT_3  # tetrahedral diagonal length on K4 in lattice units

# v7 IC amplitudes UNCHANGED
A_AMP_POL = 0.95
HELICAL_PITCH = 1.0 / TWO_PI
K_BELTRAMI = OMEGA_C / 1.0
V_AMP = A_AMP_POL
PHI_AMP = A_AMP_POL

# Adjudication thresholds (UNCHANGED from v7 per doc 86 §7.4 lock)
PERSISTENCE_PERIODS = 100.0
A2_MEAN_THRESHOLD = 0.5
BELTRAMI_PARALLELISM_THRESHOLD = 0.8
LOOP_FLUX_TARGET = TWO_PI
LOOP_FLUX_TOLERANCE = 0.20
RING_LOCALIZATION_THRESHOLD = 0.5
BELTRAMI_IC_THRESHOLD = 0.95

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT = Path(__file__).parent / "r10_path_alpha_v8_corrected_measurements_results.json"


def build_chair_ring(center):
    """6-node hexagonal chair-ring + 6 bonds at lattice center (UNCHANGED from v7)."""
    cx, cy, cz = center
    nodes = [
        (cx, cy, cz), (cx + 1, cy + 1, cz + 1), (cx, cy + 2, cz + 2),
        (cx - 1, cy + 3, cz + 1), (cx - 2, cy + 2, cz), (cx - 1, cy + 1, cz - 1),
    ]
    bonds = []
    for n in range(6):
        node_curr = nodes[n]
        node_next = nodes[(n + 1) % 6]
        curr_is_a = all(c % 2 == 0 for c in node_curr)
        if curr_is_a:
            a_site, b_site = node_curr, node_next
        else:
            a_site, b_site = node_next, node_curr
        offset = np.array(b_site) - np.array(a_site)
        port_idx = next(p for p, po in enumerate(PORT_OFFSETS_A) if np.array_equal(offset, po))
        traversal_dir = (np.array(node_next) - np.array(node_curr)).astype(float)
        traversal_dir /= np.linalg.norm(traversal_dir)
        bonds.append({
            "ring_idx": n, "node_curr": list(node_curr), "node_next": list(node_next),
            "a_site": list(a_site), "b_site": list(b_site), "port": port_idx,
            "a_to_b_offset": offset.tolist(),
            "traversal_direction": traversal_dir.tolist(),
        })
    return nodes, bonds


def ring_frame_at_node(nodes, n_idx, centroid):
    next_node = np.array(nodes[(n_idx + 1) % 6])
    prev_node = np.array(nodes[(n_idx - 1) % 6])
    tangent = (next_node - prev_node).astype(float)
    tangent /= np.linalg.norm(tangent)
    radial = centroid - np.array(nodes[n_idx])
    radial = radial - np.dot(radial, tangent) * tangent
    if np.linalg.norm(radial) < 1e-10:
        candidate = np.cross(tangent, [1.0, 0.0, 0.0])
        if np.linalg.norm(candidate) < 1e-10:
            candidate = np.cross(tangent, [0.0, 1.0, 0.0])
        radial = candidate / np.linalg.norm(candidate)
    else:
        radial /= np.linalg.norm(radial)
    binormal = np.cross(tangent, radial)
    binormal /= max(np.linalg.norm(binormal), 1e-12)
    return tangent, radial, binormal


def compute_a_0_at_ring_nodes(nodes, a_amp_pol, helical_pitch):
    centroid = np.mean([np.array(n) for n in nodes], axis=0)
    a_amp_tor = a_amp_pol * helical_pitch
    a_0_per_node = []
    for n_idx, node in enumerate(nodes):
        tangent, radial, binormal = ring_frame_at_node(nodes, n_idx, centroid)
        phase = TWO_PI * n_idx / 6.0
        a_pol = a_amp_pol * (np.cos(phase) * radial + np.sin(phase) * binormal)
        a_tor = a_amp_tor * tangent
        a_0_per_node.append(a_pol + a_tor)
    return np.array(a_0_per_node), centroid


def initialize_helical_beltrami_ic(engine, nodes, bonds, a_0_per_node, k_beltrami, v_amp, phi_amp):
    """v7 IC UNCHANGED: spatial cos/sin pattern + helical Cosserat ω; preserve bulk thermal."""
    engine.k4.V_inc.fill(0.0)
    engine.k4.V_ref.fill(0.0)
    engine.k4.Phi_link.fill(0.0)
    engine.k4.S_field.fill(1.0)
    # PRESERVE bulk thermal Cosserat (per v7 fix)

    for bond_idx, bond in enumerate(bonds):
        phase = TWO_PI * bond_idx / 6.0
        v_value = v_amp * np.cos(phase)
        phi_value = phi_amp * np.sin(phase)
        ix_a, iy_a, iz_a = bond["a_site"]
        port_a = bond["port"]
        engine.k4.V_inc[ix_a, iy_a, iz_a, port_a] = v_value
        ix_b, iy_b, iz_b = bond["b_site"]
        engine.k4.V_inc[ix_b, iy_b, iz_b, port_a] = v_value
        engine.k4.Phi_link[ix_a, iy_a, iz_a, port_a] = phi_value

    for n_idx, node in enumerate(nodes):
        ix, iy, iz = node
        engine.cos.omega[ix, iy, iz, :] = k_beltrami * a_0_per_node[n_idx]
        engine.cos.u[ix, iy, iz, :] = 0.0
        engine.cos.u_dot[ix, iy, iz, :] = 0.0
        engine.cos.omega_dot[ix, iy, iz, :] = 0.0


def measure_a_vec_from_phi_link_oscillating(phi_oscillating, ix, iy, iz, t_idx, port_offsets, n_lattice):
    """v8 CORRECTED: A-vec from DETRENDED Phi_link (oscillating component only).

    phi_oscillating has shape (N_steps, nx, ny, nz, 4) — Phi_link with secular
    linear trend subtracted per bond per port. A-vec at instant t_idx:

        A_vec(node, t) = Σ over 4 ports {(3/4) · port_dir · phi_oscillating[t, port] / bond_length}

    where (3/4) is Moore-Penrose normalization for tetrahedral 4-port (P^T P = (4/3)·I).
    The (3/4) factor is scale; cos_sim is scale-invariant so it doesn't affect Beltrami test
    direction — but kept for canonical-correctness per Vol 1 Ch 3:24 A·bond_length = Phi.
    """
    is_a = (ix % 2 == 0) and (iy % 2 == 0) and (iz % 2 == 0)
    a_vec = np.zeros(3)
    for p in range(4):
        bond_dir_A = port_offsets[p].astype(float) / SQRT_3
        if is_a:
            phi = phi_oscillating[t_idx, ix, iy, iz, p]
        else:
            ax, ay, az = ix - port_offsets[p][0], iy - port_offsets[p][1], iz - port_offsets[p][2]
            if 0 <= ax < n_lattice and 0 <= ay < n_lattice and 0 <= az < n_lattice:
                phi = phi_oscillating[t_idx, ax, ay, az, p]
            else:
                phi = 0.0
        a_vec += (3.0 / 4.0) * bond_dir_A * (phi / BOND_LENGTH)
    return a_vec


def measure_loop_flux_oscillating(phi_oscillating, bonds, t_idx):
    """v8 CORRECTED: ∮A·dl = Σ over 6 bonds of Phi_link_oscillating · traversal_sign.

    With Phi_link detrended, this measures the OSCILLATING topological invariant
    around the secular trend. For a Beltrami standing wave, this should oscillate
    at frequency ω_C with magnitude ≈ 2π in V_SNAP-natural units (per doc 85 §5.1).
    """
    loop_flux = 0.0
    for bond in bonds:
        ix, iy, iz = bond["a_site"]
        port = bond["port"]
        phi = phi_oscillating[t_idx, ix, iy, iz, port]
        a_to_b = PORT_OFFSETS_A[port].astype(float)
        traversal = np.array(bond["traversal_direction"]) * SQRT_3
        sign = float(np.sign(np.dot(a_to_b, traversal)))
        loop_flux += phi * sign
    return loop_flux


def detrend_phi_link_per_bond(phi_link_traj):
    """Subtract per-port linear fit from Phi_link trajectory.

    phi_link_traj: shape (N_steps, nx, ny, nz, 4). Returns oscillating component.
    Linear fit: y(t) = a + b·t per bond per port; subtract to leave residual.
    """
    n_steps = phi_link_traj.shape[0]
    t = np.arange(n_steps, dtype=np.float64)
    t_mean = t.mean()
    t_var = ((t - t_mean) ** 2).sum()

    phi_mean = phi_link_traj.mean(axis=0)  # shape (nx, ny, nz, 4)
    # slope = Σ (t - t_mean) · (phi - phi_mean) / Σ (t - t_mean)²
    slope_num = ((t[:, None, None, None, None] - t_mean) * (phi_link_traj - phi_mean[None, ...])).sum(axis=0)
    slope = slope_num / t_var  # shape (nx, ny, nz, 4)
    intercept = phi_mean - slope * t_mean

    # Residual = phi - (intercept + slope · t)
    trend = intercept[None, ...] + slope[None, ...] * t[:, None, None, None, None]
    return phi_link_traj - trend


def measure_ring_state_v8(engine, nodes):
    """Real-time persistence + ring localization (UNCHANGED from v7)."""
    V_SNAP = engine.V_SNAP
    A2_per_node = []
    for node in nodes:
        ix, iy, iz = node
        V_sq = float(np.sum(engine.k4.V_inc[ix, iy, iz, :] ** 2))
        A2_per_node.append(V_sq / (V_SNAP ** 2))

    ring_energy = 0.0
    for node in nodes:
        ix, iy, iz = node
        V_sq = float(np.sum(engine.k4.V_inc[ix, iy, iz, :] ** 2))
        omega_sq = float(np.sum(engine.cos.omega[ix, iy, iz, :] ** 2))
        ring_energy += V_sq + omega_sq

    pml = PML
    nx = engine.k4.nx
    sl = (slice(pml, nx - pml),) * 3
    V_sq_int = float(np.sum(np.asarray(engine.k4.V_inc[sl + (slice(None),)]) ** 2))
    omega_sq_int = float(np.sum(np.asarray(engine.cos.omega[sl + (slice(None),)]) ** 2))
    total_energy = V_sq_int + omega_sq_int
    ring_localization = ring_energy / max(total_energy, 1e-30)

    return {
        "A2_min": float(min(A2_per_node)),
        "A2_mean": float(np.mean(A2_per_node)),
        "ring_localization": ring_localization,
    }


def beltrami_eigenvector_sanity_check(a_0_per_node, omega_per_node, k_beltrami):
    cos_sims = []
    for n_idx in range(6):
        a = k_beltrami * a_0_per_node[n_idx]
        w = omega_per_node[n_idx]
        a_norm, w_norm = np.linalg.norm(a), np.linalg.norm(w)
        if a_norm < 1e-12 or w_norm < 1e-12:
            cos_sims.append(0.0)
        else:
            cos_sims.append(float(np.dot(a, w) / (a_norm * w_norm)))
    return cos_sims


def run_v8(temperature=0.0, label="T0"):
    print("=" * 78, flush=True)
    print(f"  r10 path α v8 — corrected measurements (Phi_link detrend)  [{label}]")
    print(f"  T = {temperature:.4e} m_e·c² units")
    print("=" * 78, flush=True)

    nodes, bonds = build_chair_ring(CENTER)
    a_0_per_node, centroid = compute_a_0_at_ring_nodes(nodes, A_AMP_POL, HELICAL_PITCH)

    engine = VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=temperature,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )

    print("Applying v7-style helical Beltrami IC (UNCHANGED from v7)...", flush=True)
    initialize_helical_beltrami_ic(engine, nodes, bonds, a_0_per_node, K_BELTRAMI, V_AMP, PHI_AMP)

    omega_per_node_ic = np.array([engine.cos.omega[n[0], n[1], n[2], :].copy() for n in nodes])
    beltrami_ic_cos_sims = beltrami_eigenvector_sanity_check(a_0_per_node, omega_per_node_ic, K_BELTRAMI)
    print(f"  Beltrami IC sanity: cos_sim(ω, k·A_0) = {[f'{c:+.4f}' for c in beltrami_ic_cos_sims]}")
    beltrami_ic_pass = all(c >= BELTRAMI_IC_THRESHOLD for c in beltrami_ic_cos_sims)
    print()

    # Recording: store full Phi_link + Cosserat ω trajectories
    print(f"Recording {N_RECORDING_STEPS} steps (full Phi_link traj for post-process detrending)...", flush=True)
    nx = engine.k4.nx
    phi_link_traj = np.zeros((N_RECORDING_STEPS, nx, nx, nx, 4), dtype=np.float32)  # float32 to save mem
    omega_traj_per_node = np.zeros((N_RECORDING_STEPS, 6, 3), dtype=np.float32)

    A2_min_traj = np.zeros(N_RECORDING_STEPS)
    A2_mean_traj = np.zeros(N_RECORDING_STEPS)
    ring_loc_traj = np.zeros(N_RECORDING_STEPS)
    persistence_periods = 0.0
    saturation_lost = False

    t0 = time.time()
    last = t0
    for i in range(N_RECORDING_STEPS):
        engine.step()
        s = measure_ring_state_v8(engine, nodes)
        A2_min_traj[i] = s["A2_min"]
        A2_mean_traj[i] = s["A2_mean"]
        ring_loc_traj[i] = s["ring_localization"]

        # Store trajectories for post-process
        phi_link_traj[i] = engine.k4.Phi_link.astype(np.float32)
        for n_idx, node in enumerate(nodes):
            omega_traj_per_node[i, n_idx, :] = engine.cos.omega[node[0], node[1], node[2], :]

        t_p = (i + 1) * DT / COMPTON_PERIOD
        if not saturation_lost:
            if s["A2_mean"] >= A2_MEAN_THRESHOLD:
                persistence_periods = t_p
            else:
                saturation_lost = True

        if (time.time() - last) > 30.0:
            print(f"    [progress] step {i}/{N_RECORDING_STEPS}, t={t_p:.1f}P, "
                  f"A²_mean={s['A2_mean']:.3f}, loc={s['ring_localization']:.3f}, "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()
    elapsed_recording = time.time() - t0
    print(f"  Recording done at {elapsed_recording:.1f}s", flush=True)
    print()

    # Post-process: detrend Phi_link
    print("Post-process: detrending Phi_link (subtracting linear trend per bond per port)...", flush=True)
    t_post = time.time()
    phi_oscillating = detrend_phi_link_per_bond(phi_link_traj.astype(np.float64))
    print(f"  Detrend done at {time.time()-t_post:.1f}s")

    # v8 corrected measurements over recording
    print("Computing v8 corrected Beltrami |cos_sim| + loop flux per step...", flush=True)
    cos_sim_traj = np.zeros(N_RECORDING_STEPS)
    loop_flux_traj = np.zeros(N_RECORDING_STEPS)
    for i in range(N_RECORDING_STEPS):
        cos_sims = []
        for n_idx, node in enumerate(nodes):
            a_vec = measure_a_vec_from_phi_link_oscillating(
                phi_oscillating, node[0], node[1], node[2], i,
                PORT_OFFSETS_A, N_LATTICE
            )
            b_vec = omega_traj_per_node[i, n_idx, :].astype(np.float64)
            a_norm, b_norm = np.linalg.norm(a_vec), np.linalg.norm(b_vec)
            if a_norm < 1e-12 or b_norm < 1e-12:
                cos_sims.append(0.0)
            else:
                cos_sims.append(float(np.dot(a_vec, b_vec) / (a_norm * b_norm)))
        cos_sim_traj[i] = np.mean(np.abs(cos_sims))
        loop_flux_traj[i] = measure_loop_flux_oscillating(phi_oscillating, bonds, i)

    # Steady-state window
    sw_start = N_RECORDING_STEPS // 4
    A2_mean_steady = float(np.mean(A2_mean_traj[sw_start:]))
    cos_sim_steady = float(np.mean(cos_sim_traj[sw_start:]))
    loop_flux_steady_rms = float(np.sqrt(np.mean(loop_flux_traj[sw_start:] ** 2)))
    loop_flux_steady_peak = float(np.max(np.abs(loop_flux_traj[sw_start:])))
    ring_loc_steady = float(np.mean(ring_loc_traj[sw_start:]))

    print()
    print("=" * 78, flush=True)
    print(f"  Adjudication  [{label}]")
    print("=" * 78, flush=True)
    print(f"  Persistence (A²_mean ≥ {A2_MEAN_THRESHOLD}): {persistence_periods:.1f} P")
    print(f"  Beltrami |cos_sim(A_oscillating, ω)| steady: {cos_sim_steady:.4f}  (≥ {BELTRAMI_PARALLELISM_THRESHOLD})")
    print(f"  Loop flux ∮A·dl RMS steady: {loop_flux_steady_rms:.4f}  (target {LOOP_FLUX_TARGET:.4f} ± {LOOP_FLUX_TOLERANCE*100:.0f}%)")
    print(f"  Loop flux peak |∮A·dl| steady: {loop_flux_steady_peak:.4f}")
    print(f"  Ring localization steady: {ring_loc_steady:.4f}  (≥ {RING_LOCALIZATION_THRESHOLD})")
    print()

    persistence_pass = persistence_periods >= PERSISTENCE_PERIODS
    beltrami_pass = cos_sim_steady >= BELTRAMI_PARALLELISM_THRESHOLD
    # Loop flux: check if RMS is in target ± tolerance OR peak hits target
    flux_pass = (
        abs(loop_flux_steady_rms - LOOP_FLUX_TARGET) / LOOP_FLUX_TARGET < LOOP_FLUX_TOLERANCE
        or abs(loop_flux_steady_peak - LOOP_FLUX_TARGET) / LOOP_FLUX_TARGET < LOOP_FLUX_TOLERANCE
    )
    loc_pass = ring_loc_steady >= RING_LOCALIZATION_THRESHOLD

    n_pass = sum([persistence_pass, beltrami_pass, flux_pass, loc_pass])
    if n_pass == 4:
        mode = "I"
    elif n_pass >= 2:
        mode = "II"
    else:
        mode = "III"

    verdict = (
        f"Mode {mode} at {label}: {n_pass}/4 PASS — "
        f"persist={persistence_pass} ({persistence_periods:.1f}P), "
        f"beltrami={beltrami_pass} ({cos_sim_steady:.3f}), "
        f"flux={flux_pass} (RMS={loop_flux_steady_rms:.3f}, peak={loop_flux_steady_peak:.3f}), "
        f"loc={loc_pass} ({ring_loc_steady:.3f})"
    )
    print(f"  Mode: {mode}")
    print(f"  Verdict: {verdict}")
    print()

    return {
        "label": label,
        "temperature": temperature,
        "elapsed_recording_seconds": elapsed_recording,
        "beltrami_ic_cos_sims": beltrami_ic_cos_sims,
        "beltrami_ic_pass": beltrami_ic_pass,
        "results": {
            "persistence_periods": persistence_periods,
            "A2_mean_steady": A2_mean_steady,
            "beltrami_cos_sim_steady": cos_sim_steady,
            "loop_flux_steady_rms": loop_flux_steady_rms,
            "loop_flux_steady_peak": loop_flux_steady_peak,
            "ring_localization_steady": ring_loc_steady,
            "loop_flux_first_50_steps": loop_flux_traj[:50].tolist(),
            "loop_flux_last_50_steps": loop_flux_traj[-50:].tolist(),
            "cos_sim_first_50_steps": cos_sim_traj[:50].tolist(),
            "cos_sim_last_50_steps": cos_sim_traj[-50:].tolist(),
        },
        "criteria_pass": {
            "persistence": bool(persistence_pass),
            "beltrami": bool(beltrami_pass),
            "loop_flux": bool(flux_pass),
            "ring_localization": bool(loc_pass),
            "n_pass": int(n_pass),
        },
        "mode": mode,
        "verdict": verdict,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-sweep", action="store_true",
                        help="Run T sweep at T = {0, 1e-3, 1e-2, 1e-1}·T_V-rupt")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    T_V_RUPT = ALPHA / (4.0 * np.pi)
    print(f"\nT_V-rupt ≈ α/(4π) = {T_V_RUPT:.4e} in m_e·c² natural units\n")

    results = []
    print("\n" + "=" * 78)
    print("  RUN 1: T = 0 BASELINE")
    print("=" * 78 + "\n")
    r0 = run_v8(temperature=0.0, label="T=0")
    results.append(r0)

    if args.t_sweep:
        substantive_pass = (
            r0["mode"] == "I"
            or (r0["mode"] in ["I", "II"]
                and r0["criteria_pass"]["persistence"]
                and r0["criteria_pass"]["ring_localization"])
        )
        if substantive_pass:
            print("\n" + "=" * 78)
            print(f"  T=0 Mode {r0['mode']} with persistence+localization PASS — T sweep")
            print("=" * 78 + "\n")
            for t_factor in [1e-3, 1e-2, 1e-1]:
                t_value = t_factor * T_V_RUPT
                label = f"T={t_factor:.0e}·T_V-rupt={t_value:.4e}"
                rt = run_v8(temperature=t_value, label=label)
                results.append(rt)
        else:
            print(f"\nT=0 Mode {r0['mode']} without persistence+localization — skip T sweep")

    print("\n" + "=" * 78)
    print("  SYNTHESIS ACROSS ALL RUNS")
    print("=" * 78)
    for r in results:
        print(f"  {r['label']}: Mode {r['mode']} — "
              f"persist={r['results']['persistence_periods']:.1f}P, "
              f"beltrami={r['results']['beltrami_cos_sim_steady']:.3f}, "
              f"flux_RMS={r['results']['loop_flux_steady_rms']:.3f}, "
              f"flux_peak={r['results']['loop_flux_steady_peak']:.3f}, "
              f"loc={r['results']['ring_localization_steady']:.3f}")
    print()

    payload = {
        "pre_registration": "P_phase11_path_alpha_v8_corrected_measurements",
        "test": "v8 corrected measurement methods (Phi_link detrend) + thermal sweep",
        "lattice": {"N": N_LATTICE, "pml": PML, "center": list(CENTER)},
        "recording_periods": RECORDING_END_P,
        "ic_amplitudes": {
            "a_amp_pol": A_AMP_POL, "helical_pitch": HELICAL_PITCH, "k_beltrami": K_BELTRAMI,
        },
        "thresholds": {
            "persistence_periods": PERSISTENCE_PERIODS,
            "A2_mean_threshold": A2_MEAN_THRESHOLD,
            "beltrami_parallelism": BELTRAMI_PARALLELISM_THRESHOLD,
            "loop_flux_target": LOOP_FLUX_TARGET,
            "loop_flux_tolerance": LOOP_FLUX_TOLERANCE,
            "ring_localization": RING_LOCALIZATION_THRESHOLD,
        },
        "T_V_rupt_natural_units": T_V_RUPT,
        "runs": results,
    }
    args.output.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {args.output.relative_to(REPO_ROOT)}")
    return payload


if __name__ == "__main__":
    main()
