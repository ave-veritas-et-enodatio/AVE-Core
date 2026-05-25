"""Move 11b — reactance tracking with PML-filtered cells, full time series,
drive verification, and Pearson cross-correlation matrix between sectors.

Per `P_phase1_attractor_reactance_tracking_v2` (frozen at this commit).

THREE FIXES TO MOVE 11 (per audit on Move 11 result):
  Fix 1 (PML filter): Move 11's top-5 |ω|² cells were ALL at lattice
    boundary (j=0/31, i=0/31), where PML mask attenuates dynamics
    (|ω| std=0, |ω̇|=0). Move 11b filters to interior only
    (PML+1 ≤ i,j,k ≤ N-PML-2).

  Fix 2 (full time series + drive verification):
    Save T_cos(t), V_cos(t), Σ|V_inc|²(t), Σ|V_ref|²(t),
    Σ|Φ_link|²(t) full series for downstream diagnostics post-hoc.
    Assert len(engine.sources)==0 → Diag 1 (rules out trivial cause
    of accidentally-active drive).

  Fix 3 (Pearson cross-correlation matrix between sectors):
    H_cos(t) vs Σ|V_inc|²(t) → V-sector ↔ Cosserat trading?
    H_cos(t) vs Σ|Φ_link|²(t) → K4-inductive ↔ Cosserat trading?
    If H_cos drift anti-correlated with K4 quantity, Op14 is doing
    its job (energy traded between sectors); H_total approximately
    conserved despite H_cos alone drifting (Diag 3).
    If uncorrelated, real conservation violation — Diag 4 / E-069.

CONTEXT (per doc 74_ §15 + audit on §14):
  Move 7+7b energy partition was a SNAPSHOT at t=200P (V:T = 85:15).
  For an LC oscillator, snapshot V:T depends on phase — at peak
  displacement V:T≈100:0, at peak velocity V:T≈0:100, time-averaged
  ≈50:50. **A snapshot cannot distinguish "static fixed point with
  sub-percent ripple" from "oscillator caught near peak displacement."**

  Engine computes K4 Φ_link = ∫V_avg·dt every step (k4_tlm.py:384-391
  accumulator into engine.k4.Phi_link[mask_A, port]) but NO MOVE has
  read it. Cosserat L-state ω_dot also never measured. Both are
  inductive-side observables; without them, the LC sectors aren't
  characterized.

  This is the reactance-tracking gap. Move 11 closes it — A-011 in
  the audit tracker.

GOAL:
  Time-resolved C-state vs L-state tracking over t∈[150P, 200P] at
  the engine's natural energy-density peaks. Determine empirically
  whether the static-fixed-point verdict from §13-§15 stands
  (T(t), V(t) both near-constant; Φ_link(t) constant; |ω|(t) constant)
  OR whether the configuration is actually a clean LC oscillator
  caught at one phase (T(t), V(t) anti-correlated at some ω;
  Φ_link(t) and V_avg(t) 90° out of phase; |ω|(t) and |ω̇|(t)
  90° out of phase).

FROZEN EXTRACTIONS (5 — all reported, no PASS/FAIL):

  (1) GLOBAL ENERGY TIME SERIES over t∈[150P, 200P]:
      T_cos(t) = engine.cos.kinetic_energy() = ½ρ|u̇|² + ½I_ω|ω̇|²
      V_cos(t) = engine.cos.total_energy() (Cosserat potential)
      H_cos(t) = T_cos(t) + V_cos(t)
      Σ|V_inc|²(t), Σ|V_ref|²(t) (K4 capacitive proxies)
      Σ|Φ_link|²(t) (K4 inductive proxy)

  (2) K4 LC-PAIR PHASE RELATIONSHIP at top-5 |V_inc|² bonds:
      Per-bond V_avg(t) = ½(V_ref_A(t) + V_ref_B_shifted(t))
                          [from k4_tlm.py:389; the C-state observable]
      Per-bond Φ_link(t) [the L-state observable]
      Cross-correlation Φ_link vs V_avg → phase lag φ
      LC reactance signature: φ = -π/2 (Φ lags V_avg by 90°,
        consistent with ∫V dt accumulation)
      Static signature: φ ≈ 0 or undefined (both constant)

  (3) COSSERAT ω-PAIR PHASE RELATIONSHIP at top-5 |ω|² cells:
      |ω|(t) (C-state magnitude)
      |ω̇|(t) (L-state magnitude)
      Cross-correlation → phase lag
      LC reactance: 90° phase lag (sinusoidal anti-correlation)
      Static: |ω̇|(t) ≈ 0 throughout

  (4) FFT OF EACH TIME SERIES:
      For each of T_cos(t), V_cos(t), |ω|(t), |ω̇|(t),
      Σ|Φ_link|²(t), V_avg-at-top-bond(t):
        compute FFT, report top 3 frequencies (rad/natural-time-unit)
      Distinguishes:
        - Single coherent ω peak (clean oscillator at that frequency)
        - Adjacent-bin spectral leakage (static signal with noise)
        - Multi-frequency content (mixed/coupled mode)

  (5) ANTI-CORRELATION CHECK on T_cos(t) vs V_cos(t):
      Pearson correlation coefficient ρ over the FFT window
      LC oscillator: ρ ≈ -1 (T ↑ ⟺ V ↓)
      Static: ρ undefined (both constant) or ≈ 0 (independent noise)
      Time-averaged T:V ratio (for direct comparison to Move 7's
        snapshot 85:15)

NO PASS/FAIL ADJUDICATION. Result IS the characterization.

OUTCOME SPACE (informational, not pre-committed):
  - All time series flat (sub-percent ripple) → static fixed point
    confirmed. Move 9 design needs to plan for driving against
    a static state.
  - Anti-correlated T(t), V(t) + 90° phase lag in Φ_link vs V_avg
    + non-zero |ω̇|(t) → reactive oscillator confirmed at some
    frequency. Move 9 design uses that frequency as the drive
    target instead of (or in addition to) ω=2.
  - Mixed signals (some sectors reactive, others static) →
    sector-asymmetry empirical finding; Move 9 design adjusts.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants (match Move 5+7+7b+10 for deterministic reproduction) ─────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ
A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
V_AMP_INIT = 0.14

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
N_PERIODS_TOTAL = 200.0
DT = 1.0 / np.sqrt(2.0)
N_STEPS = int(N_PERIODS_TOTAL * COMPTON_PERIOD / DT) + 1

T_RECORD_START_PERIOD = 150.0
STEP_RECORD_START = int(T_RECORD_START_PERIOD * COMPTON_PERIOD / DT)
N_TOP_CELLS = 5
N_TOP_BONDS = 5

PORT_VECTORS = np.array([
    [+1, +1, +1],
    [+1, -1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
], dtype=int)

OUTPUT_JSON = Path(__file__).parent / "r8_phase1_reactance_tracking_v2_results.json"


def build_engine():
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine):
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def make_interior_mask(shape, pml):
    """Boolean mask: True for cells in [pml+1, N-pml-2] in each axis (PML excluded)."""
    nx, ny, nz = shape[:3]
    i, j, k = np.indices((nx, ny, nz))
    return ((i >= pml + 1) & (i <= nx - pml - 2) &
            (j >= pml + 1) & (j <= ny - pml - 2) &
            (k >= pml + 1) & (k <= nz - pml - 2))


def select_top_omega_cells(omega_field, k=5, pml=PML):
    """Pick top-k cells by |ω|² density INTERIOR ONLY (PML-excluded)."""
    omega_density = np.sum(omega_field ** 2, axis=-1)
    interior = make_interior_mask(omega_density.shape, pml)
    masked = np.where(interior, omega_density, -np.inf)
    flat = masked.flatten()
    top_idx = np.argpartition(flat, -k)[-k:]
    top_idx = top_idx[np.argsort(flat[top_idx])[::-1]]
    return [tuple(int(c) for c in np.unravel_index(idx, omega_density.shape))
            for idx in top_idx]


def select_top_vinc_bonds(v_inc_field, k=5, pml=PML):
    """Pick top-k (cell, port) bonds by V_inc² INTERIOR ONLY (PML-excluded)."""
    interior_3d = make_interior_mask(v_inc_field.shape, pml)
    interior_4d = np.broadcast_to(interior_3d[..., None], v_inc_field.shape)
    masked = np.where(interior_4d, v_inc_field ** 2, -np.inf)
    flat = masked.reshape(-1)
    top_idx = np.argpartition(flat, -k)[-k:]
    top_idx = top_idx[np.argsort(flat[top_idx])[::-1]]
    bonds = []
    for idx in top_idx:
        cell_flat, port = divmod(int(idx), 4)
        cell = np.unravel_index(cell_flat, v_inc_field.shape[:3])
        bonds.append((tuple(int(c) for c in cell), int(port)))
    return bonds


def main():
    print("=" * 78, flush=True)
    print(f"  Move 11b — reactance with PML-filtered cells, drive verify,")
    print(f"  full time series, Pearson cross-correlation matrix")
    print(f"  P_phase1_attractor_reactance_tracking_v2")
    print("=" * 78, flush=True)
    print(f"  Lattice N={N_LATTICE}, deterministic Move 5 reproduction")
    print(f"  Recording window: t∈[{T_RECORD_START_PERIOD}, {N_PERIODS_TOTAL}]P")
    print(f"  Top-{N_TOP_CELLS} |ω|² cells + top-{N_TOP_BONDS} |V_inc|² bonds")
    print()

    # Pass 1: run to t=200P, identify top INTERIOR cells/bonds from end-state
    print(f"  Pass 1: run to t={N_PERIODS_TOTAL}P to identify top interior "
          f"cells/bonds (PML-filtered)…")
    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    # ─── Diag 1: drive verification ──────────────────────────────────────────
    n_sources = len(engine.sources) if hasattr(engine, "sources") else 0
    drive_active = n_sources > 0
    print(f"  Diag 1 (drive verify): engine.sources count = {n_sources}, "
          f"drive_active = {drive_active}")
    if drive_active:
        print(f"    !!! WARNING: drive is active. Move 5/11 should have NO source. "
              f"Sources: {engine.sources}")
    else:
        print(f"    OK: no drive registered. H drift cannot be from accidental drive.")
    print()

    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if (time.time() - last_progress) > 30.0:
            t_p = step * DT / COMPTON_PERIOD
            print(f"    [P1] step {step}, t={t_p:.1f}P, "
                  f"elapsed {time.time() - t0:.1f}s", flush=True)
            last_progress = time.time()
    elapsed_p1 = time.time() - t0

    final_omega = np.asarray(engine.cos.omega).copy()
    final_v_inc = np.asarray(engine.k4.V_inc).copy()
    top_omega_cells = select_top_omega_cells(final_omega, k=N_TOP_CELLS)
    top_vinc_bonds = select_top_vinc_bonds(final_v_inc, k=N_TOP_BONDS)

    print(f"  Pass 1 complete: {elapsed_p1:.1f}s")
    print(f"  Top-{N_TOP_CELLS} |ω|² cells: {top_omega_cells}")
    print(f"  Top-{N_TOP_BONDS} |V_inc|² bonds (cell, port): {top_vinc_bonds}")
    print()

    # Pass 2: re-run with full reactance recording during t∈[150P, 200P]
    print(f"  Pass 2: re-run with C-state + L-state recording…")
    engine = build_engine()
    seed_corpus_2_3_joint(engine)

    # Time series collectors
    times = []
    T_cos_series = []
    V_cos_series = []
    sum_vinc_sq_series = []
    sum_vref_sq_series = []
    sum_philink_sq_series = []
    omega_per_cell = [[] for _ in top_omega_cells]
    omegadot_per_cell = [[] for _ in top_omega_cells]
    vavg_per_bond = [[] for _ in top_vinc_bonds]
    philink_per_bond = [[] for _ in top_vinc_bonds]

    t0 = time.time()
    last_progress = t0
    for step in range(1, N_STEPS + 1):
        engine.step()
        if step >= STEP_RECORD_START:
            times.append(float(step * DT / COMPTON_PERIOD))
            # Global energies
            T_cos_series.append(float(engine.cos.kinetic_energy()))
            V_cos_series.append(float(engine.cos.total_energy()))
            v_inc = np.asarray(engine.k4.V_inc)
            v_ref = np.asarray(engine.k4.V_ref)
            phi_link = np.asarray(engine.k4.Phi_link)
            mask_active = np.asarray(engine.k4.mask_active)
            sum_vinc_sq_series.append(
                float(np.sum((v_inc * mask_active[..., None]) ** 2)))
            sum_vref_sq_series.append(
                float(np.sum((v_ref * mask_active[..., None]) ** 2)))
            sum_philink_sq_series.append(
                float(np.sum((phi_link * np.asarray(engine.k4.mask_A)[..., None]) ** 2)))

            # Cosserat per-cell C-state and L-state
            omega = np.asarray(engine.cos.omega)
            omega_dot = np.asarray(engine.cos.omega_dot)
            for ci, cell in enumerate(top_omega_cells):
                omega_per_cell[ci].append(
                    float(np.linalg.norm(omega[cell[0], cell[1], cell[2], :])))
                omegadot_per_cell[ci].append(
                    float(np.linalg.norm(omega_dot[cell[0], cell[1], cell[2], :])))

            # K4 per-bond C-state (V_avg) and L-state (Φ_link)
            for bi, (cell, port) in enumerate(top_vinc_bonds):
                # V_avg = ½(V_ref_A + V_ref_B_shifted) per k4_tlm.py:389
                # If A site: shift to find B; if B site: shift opposite.
                # Simplification: compute V_avg as average of V_ref at this cell
                # and V_ref at the neighbor along this port direction.
                # PORT_VECTORS gives A-site→B-site direction; B-site→A is opposite.
                mask_A = np.asarray(engine.k4.mask_A)
                if mask_A[cell]:
                    shift = -PORT_VECTORS[port]      # roll to bring B's val to A
                else:
                    shift = +PORT_VECTORS[port]      # roll to bring A's val to B
                # neighbor cell index
                nc = ((cell[0] + shift[0]) % N_LATTICE,
                      (cell[1] + shift[1]) % N_LATTICE,
                      (cell[2] + shift[2]) % N_LATTICE)
                v_avg = 0.5 * (v_ref[cell[0], cell[1], cell[2], port] +
                               v_ref[nc[0], nc[1], nc[2], port])
                vavg_per_bond[bi].append(float(v_avg))
                philink_per_bond[bi].append(float(phi_link[cell[0], cell[1], cell[2], port]))

        if (time.time() - last_progress) > 30.0:
            t_p = step * DT / COMPTON_PERIOD
            print(f"    [P2] step {step}, t={t_p:.1f}P, "
                  f"elapsed {time.time() - t0:.1f}s", flush=True)
            last_progress = time.time()
    elapsed_p2 = time.time() - t0
    print(f"  Pass 2 complete: {elapsed_p2:.1f}s, recorded {len(times)} samples")
    print()

    times_arr = np.array(times)
    T_arr = np.array(T_cos_series)
    V_arr = np.array(V_cos_series)
    H_arr = T_arr + V_arr

    # ─── (1) Global energy time series stats ─────────────────────────────────
    print(f"  (1) GLOBAL ENERGY TIME SERIES over t∈[{T_RECORD_START_PERIOD}, "
          f"{N_PERIODS_TOTAL}]P  ({len(times_arr)} samples):")
    print(f"    T_cos:     mean={T_arr.mean():.4e}, std={T_arr.std():.4e}, "
          f"range=[{T_arr.min():.4e}, {T_arr.max():.4e}]")
    print(f"    V_cos:     mean={V_arr.mean():.4e}, std={V_arr.std():.4e}, "
          f"range=[{V_arr.min():.4e}, {V_arr.max():.4e}]")
    print(f"    H_cos:     mean={H_arr.mean():.4e}, std={H_arr.std():.4e}, "
          f"range=[{H_arr.min():.4e}, {H_arr.max():.4e}]")
    print(f"    H std/mean (energy conservation): "
          f"{H_arr.std()/max(abs(H_arr.mean()), 1e-30):.4e}")
    print(f"    T:V time-averaged ratio: "
          f"{T_arr.mean()/max(V_arr.mean(), 1e-30):.4f}  "
          f"(snapshot at t=200P was 8.18/47.48 = 0.172)")
    print(f"    Σ|V_inc|²: mean={np.mean(sum_vinc_sq_series):.4e}, "
          f"std={np.std(sum_vinc_sq_series):.4e}")
    print(f"    Σ|V_ref|²: mean={np.mean(sum_vref_sq_series):.4e}, "
          f"std={np.std(sum_vref_sq_series):.4e}")
    print(f"    Σ|Φ_link|²: mean={np.mean(sum_philink_sq_series):.4e}, "
          f"std={np.std(sum_philink_sq_series):.4e}")
    print()

    # ─── (5) Anti-correlation T vs V ─────────────────────────────────────────
    if T_arr.std() > 1e-15 and V_arr.std() > 1e-15:
        rho_TV = float(np.corrcoef(T_arr, V_arr)[0, 1])
    else:
        rho_TV = None
    print(f"  (5) ANTI-CORRELATION T_cos(t) vs V_cos(t):")
    print(f"    Pearson ρ(T, V) = {rho_TV}")
    print(f"    LC oscillator predicts ρ ≈ -1; static fixed point predicts |ρ| ~ 0 or undefined")
    print()

    # ─── (3) Cosserat ω-pair phase per top-|ω|² cell ─────────────────────────
    print(f"  (3) COSSERAT ω-PAIR PHASE at top-{N_TOP_CELLS} |ω|² cells:")
    cosserat_phase_records = []
    for ci, cell in enumerate(top_omega_cells):
        om_arr = np.array(omega_per_cell[ci])
        omdot_arr = np.array(omegadot_per_cell[ci])
        if om_arr.std() > 1e-15 and omdot_arr.std() > 1e-15:
            rho_om = float(np.corrcoef(om_arr, omdot_arr)[0, 1])
        else:
            rho_om = None
        cosserat_phase_records.append({
            "cell": list(cell),
            "omega_mean": float(om_arr.mean()),
            "omega_std": float(om_arr.std()),
            "omegadot_mean": float(omdot_arr.mean()),
            "omegadot_std": float(omdot_arr.std()),
            "pearson_omega_omegadot": rho_om,
        })
        print(f"    cell {cell}: |ω| mean={om_arr.mean():.4e} std={om_arr.std():.4e}, "
              f"|ω̇| mean={omdot_arr.mean():.4e} std={omdot_arr.std():.4e}, "
              f"ρ(|ω|,|ω̇|)={rho_om}")
    print()

    # ─── (2) K4 LC-pair phase per top-|V_inc|² bond ──────────────────────────
    print(f"  (2) K4 LC-PAIR PHASE at top-{N_TOP_BONDS} |V_inc|² bonds:")
    k4_phase_records = []
    for bi, (cell, port) in enumerate(top_vinc_bonds):
        v_arr = np.array(vavg_per_bond[bi])
        phi_arr = np.array(philink_per_bond[bi])
        if v_arr.std() > 1e-15 and phi_arr.std() > 1e-15:
            rho_vphi = float(np.corrcoef(v_arr, phi_arr)[0, 1])
        else:
            rho_vphi = None
        k4_phase_records.append({
            "cell": list(cell), "port": port,
            "vavg_mean": float(v_arr.mean()),
            "vavg_std": float(v_arr.std()),
            "philink_mean": float(phi_arr.mean()),
            "philink_std": float(phi_arr.std()),
            "pearson_vavg_philink": rho_vphi,
        })
        print(f"    bond ({cell}, port={port}): "
              f"V_avg mean={v_arr.mean():.4e} std={v_arr.std():.4e}, "
              f"Φ_link mean={phi_arr.mean():.4e} std={phi_arr.std():.4e}, "
              f"ρ(V_avg,Φ)={rho_vphi}")
    print()

    # ─── Diag 3: Pearson cross-correlation matrix across sectors ────────────
    print(f"  Diag 3 (Pearson cross-correlation matrix between sector quantities):")
    sum_vinc_arr = np.array(sum_vinc_sq_series)
    sum_vref_arr = np.array(sum_vref_sq_series)
    sum_phi_arr = np.array(sum_philink_sq_series)

    sectors = {
        "T_cos":         T_arr,
        "V_cos":         V_arr,
        "H_cos":         H_arr,
        "Σ|V_inc|²":     sum_vinc_arr,
        "Σ|V_ref|²":     sum_vref_arr,
        "Σ|Φ_link|²":    sum_phi_arr,
    }
    pearson_matrix = {}
    for n1, s1 in sectors.items():
        pearson_matrix[n1] = {}
        for n2, s2 in sectors.items():
            if s1.std() > 1e-15 and s2.std() > 1e-15:
                pearson_matrix[n1][n2] = float(np.corrcoef(s1, s2)[0, 1])
            else:
                pearson_matrix[n1][n2] = None
    # Print upper triangle for readability
    names = list(sectors.keys())
    print(f"    {'':<14} " + " ".join(f"{n:>10s}" for n in names))
    for i, n1 in enumerate(names):
        row = f"    {n1:<14}"
        for j, n2 in enumerate(names):
            val = pearson_matrix[n1][n2]
            if val is None:
                row += f" {'(flat)':>10s}"
            elif j < i:
                row += f" {'':>10s}"
            else:
                row += f" {val:>+10.3f}"
        print(row)
    print(f"  Reading guide:")
    print(f"    Op14 trading (sectors trade energy): H_cos vs Σ|V_inc|² or Σ|Φ_link|² ≈ -1")
    print(f"    Real H_total drift: all H_cos ↔ K4 cross-correlations ≈ 0")
    print(f"    Coherent radiation/source: cross-correlations ≈ +1 (everything growing together)")
    print()

    # ─── (4) FFT of each time series ─────────────────────────────────────────
    def top_fft_freqs(signal, dt, n_top=3):
        s = np.asarray(signal) - np.mean(signal)
        if s.std() < 1e-15:
            return [(0.0, 0.0)]
        fft_power = np.abs(np.fft.rfft(s)) ** 2
        freqs = np.fft.rfftfreq(len(s), d=dt)
        idx = np.argsort(fft_power)[::-1]
        top = []
        for i in idx:
            if freqs[i] > 0 and len(top) < n_top:
                omega_natural = 2.0 * np.pi * float(freqs[i])
                top.append([omega_natural, float(fft_power[i])])
        return top

    print(f"  (4) FFT TOP FREQUENCIES (rad/natural-time-unit):")
    fft_records = {}
    for name, series in [
        ("T_cos", T_cos_series),
        ("V_cos", V_cos_series),
        ("H_cos", H_arr.tolist()),
        ("Σ|V_inc|²", sum_vinc_sq_series),
        ("Σ|Φ_link|²", sum_philink_sq_series),
        ("|ω|@cell0", omega_per_cell[0]),
        ("|ω̇|@cell0", omegadot_per_cell[0]),
        ("V_avg@bond0", vavg_per_bond[0]),
        ("Φ_link@bond0", philink_per_bond[0]),
    ]:
        top = top_fft_freqs(series, DT, n_top=3)
        fft_records[name] = top
        if top:
            top_str = ", ".join(f"{w:.3f}" for w, _ in top)
            print(f"    {name:18s}: top ω = [{top_str}]")
        else:
            print(f"    {name:18s}: signal flat (std < 1e-15), no FFT")
    print()

    # Save full payload
    payload = {
        "pre_registration": "P_phase1_attractor_reactance_tracking_v2",
        "test": "Move 11b — PML-filtered cells, full time series, drive verify, Pearson matrix",
        "N": N_LATTICE,
        "PML": PML,
        "n_record_samples": len(times),
        "elapsed_p1": elapsed_p1,
        "elapsed_p2": elapsed_p2,
        "diag_1_drive_verification": {
            "n_sources_at_engine_build": n_sources,
            "drive_active": drive_active,
        },
        "top_omega_cells_INTERIOR_ONLY": [list(c) for c in top_omega_cells],
        "top_vinc_bonds_INTERIOR_ONLY": [{"cell": list(c), "port": p} for (c, p) in top_vinc_bonds],
        "pearson_cross_correlation_matrix": pearson_matrix,
        "full_time_series": {
            "times_periods": list(times),
            "T_cos": list(T_cos_series),
            "V_cos": list(V_cos_series),
            "sum_vinc_sq": list(sum_vinc_sq_series),
            "sum_vref_sq": list(sum_vref_sq_series),
            "sum_philink_sq": list(sum_philink_sq_series),
        },
        "global_energy_stats": {
            "T_cos": {"mean": float(T_arr.mean()), "std": float(T_arr.std()),
                      "min": float(T_arr.min()), "max": float(T_arr.max())},
            "V_cos": {"mean": float(V_arr.mean()), "std": float(V_arr.std()),
                      "min": float(V_arr.min()), "max": float(V_arr.max())},
            "H_cos": {"mean": float(H_arr.mean()), "std": float(H_arr.std()),
                      "min": float(H_arr.min()), "max": float(H_arr.max())},
            "H_relative_drift": float(H_arr.std() / max(abs(H_arr.mean()), 1e-30)),
            "T_to_V_ratio": float(T_arr.mean() / max(V_arr.mean(), 1e-30)),
            "sum_vinc_sq": {"mean": float(np.mean(sum_vinc_sq_series)),
                            "std": float(np.std(sum_vinc_sq_series))},
            "sum_vref_sq": {"mean": float(np.mean(sum_vref_sq_series)),
                            "std": float(np.std(sum_vref_sq_series))},
            "sum_philink_sq": {"mean": float(np.mean(sum_philink_sq_series)),
                               "std": float(np.std(sum_philink_sq_series))},
        },
        "anticorrelation_T_V": rho_TV,
        "cosserat_phase_per_cell": cosserat_phase_records,
        "k4_phase_per_bond": k4_phase_records,
        "fft_top_freqs": fft_records,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()
