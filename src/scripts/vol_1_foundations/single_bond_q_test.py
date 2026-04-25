"""F17-K bootstrap calibration — single-bond LC tank Q-factor at the unknot O₁ level.

Per Vol 1 Ch 1:18 the electron mass is derived as the ground-state energy of the
SIMPLEST topological defect — the unknot O₁ (single closed flux tube at minimum
ropelength = 2π). Per doc 28_ §3 the electron's REAL-SPACE structure is "two
adjacent nodes + one bond." The (2,3) torus knot lives in PHASE-SPACE, not
real space.

Per Vol 4 Ch 1 + doc 16_/17_ Q-factor reframe:
    Q_tank = ω·L_e / R_TIR
           = (ℏ/e²) / (Z_0/(4π))
           = 4πℏ / (e²·Z_0)
           = 1/α = 137.036

This test verifies the bootstrap chain at the SIMPLEST possible level:
  1. Two K4 nodes (A and B) with one bond between them
  2. Inject V_inc on A toward B (small sub-yield amplitude — linear regime)
  3. Run K4-TLM scatter+connect for many steps
  4. Measure resonance frequency ω_bond from FFT of V_inc(t)
  5. Verify ω_bond·dt matches Compton-frequency expectation

In engine natural units (dx=1 = ℓ_node, c=1, m_e=1, ℏ=1):
  ω_Compton = 1
  dt        = 1/√2 ≈ 0.707
  Period    = 2π/(ω·dt) = 2π·√2 ≈ 8.89 steps
  Peak frequency in cycles/step ≈ 0.112

If the engine reproduces this period at the bond level, the AVE bootstrap
chain (m_e from unknot ropelength + Vol 4 Ch 1 LC tank + doc 16_/17_ Q-factor)
is numerically self-consistent at the simplest level. Q = 137 then follows
algebraically from the corpus formula.
"""
from __future__ import annotations
import sys
import time
import numpy as np

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import (
    C_0 as C_SI, M_E as M_E_SI,
    ALPHA, Z_0, L_NODE as ELL_NODE,
)


def find_ab_bond_center(lattice: K4Lattice3D) -> tuple[tuple, tuple, int]:
    """Find an interior A-B bond pair. Returns (A_idx, B_idx, port_AB).

    Port directions on A (per K4 convention):
      port 0: (+1, +1, +1) → B
      port 1: (+1, -1, -1) → B
      port 2: (-1, +1, -1) → B
      port 3: (-1, -1, +1) → B
    """
    nx = lattice.nx
    cx = nx // 2
    # Find an A site near center
    for di in [0, 1, 2, -1, -2]:
        for dj in [0, 1, 2, -1, -2]:
            for dk in [0, 1, 2, -1, -2]:
                i, j, k = cx + di, cx + dj, cx + dk
                if 1 <= i < nx - 1 and 1 <= j < nx - 1 and 1 <= k < nx - 1:
                    if lattice.mask_A[i, j, k]:
                        # Check port-0 neighbor is a B-site
                        ib, jb, kb = i + 1, j + 1, k + 1
                        if ib < nx and jb < nx and kb < nx:
                            if lattice.mask_B[ib, jb, kb]:
                                return (i, j, k), (ib, jb, kb), 0
    raise RuntimeError("Could not find a viable A-B bond near center")


def main(N: int = 8, n_steps: int = 200, V_amp: float = 0.05) -> None:
    print("=" * 78)
    print(f"  Single-bond Q-test: unknot O₁ resonance at simplest AVE level")
    print("=" * 78)

    # Engine natural units: pass V_SNAP=1.0; dx=1 (= ℓ_node convention)
    lattice = K4Lattice3D(
        nx=N, ny=N, nz=N, dx=1.0,
        pml_thickness=0,         # no PML — closed lattice, lossless
        op3_bond_reflection=False,  # linear regime, no Op3 yet
        V_SNAP=1.0,              # natural units
    )

    # Engine timestep, derived: dt = dx/(c·√2) — c is SI C_0 in K4Lattice3D
    print(f"  Engine constants:")
    print(f"    dx     = {lattice.dx:.6e} (lattice units)")
    print(f"    c      = {lattice.c:.6e} (SI: should be {C_SI:.4e})")
    print(f"    dt     = {lattice.dt:.6e}")
    print(f"    dt·c/dx (dispersion factor) = {lattice.dt * lattice.c / lattice.dx:.4f}")
    print(f"    Expected dt·c/dx = 1/√2 = {1/np.sqrt(2):.4f}")

    # Find an A-B bond near center
    A, B, port = find_ab_bond_center(lattice)
    print(f"  A site:  {A}  (mask_A={lattice.mask_A[A]})")
    print(f"  B site:  {B}  (mask_B={lattice.mask_B[B]})")
    print(f"  Port:    {port} (A→B direction)")

    # Inject V_inc on A's port=0 toward B (linear sub-yield amplitude)
    lattice.V_inc[A][port] = V_amp
    print(f"  Initial V_inc[A][port={port}] = {V_amp}")
    print()

    # Run the engine and trace the bond field
    print(f"  Running {n_steps} steps...")
    t0 = time.time()
    V_inc_A = np.zeros(n_steps + 1)
    V_ref_A = np.zeros(n_steps + 1)
    V_inc_B = np.zeros(n_steps + 1)
    V_ref_B = np.zeros(n_steps + 1)
    energy_lattice = np.zeros(n_steps + 1)

    V_inc_A[0] = float(lattice.V_inc[A][port])
    V_ref_A[0] = float(lattice.V_ref[A][port])
    V_inc_B[0] = float(lattice.V_inc[B][port])
    V_ref_B[0] = float(lattice.V_ref[B][port])
    energy_lattice[0] = float(np.sum(lattice.V_inc ** 2 + lattice.V_ref ** 2))

    for step in range(1, n_steps + 1):
        lattice.step()
        V_inc_A[step] = float(lattice.V_inc[A][port])
        V_ref_A[step] = float(lattice.V_ref[A][port])
        V_inc_B[step] = float(lattice.V_inc[B][port])
        V_ref_B[step] = float(lattice.V_ref[B][port])
        energy_lattice[step] = float(np.sum(lattice.V_inc ** 2 + lattice.V_ref ** 2))

    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.2f}s")
    print()

    # Energy conservation diagnostic
    E0 = energy_lattice[0]
    Ef = energy_lattice[-1]
    Emax = energy_lattice.max()
    Emin = energy_lattice.min()
    print(f"  Energy diagnostic (closed lattice, lossless TLM):")
    print(f"    E(0)   = {E0:.4e}")
    print(f"    E(end) = {Ef:.4e}")
    print(f"    E_max  = {Emax:.4e}")
    print(f"    E_min  = {Emin:.4e}")
    print(f"    ΔE/E₀  = {(Ef-E0)/max(E0,1e-30):.3e}")

    # FFT of V_inc(t) at A — find resonance frequency
    print()
    print(f"  Resonance analysis (FFT of V_inc[A][port={port}](t)):")
    signal = V_inc_A
    # Detrend
    signal = signal - np.mean(signal)
    fft = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n_steps + 1, d=1.0)  # cycles per step
    spectrum = np.abs(fft) ** 2
    # Find peak (skip DC)
    peak_idx = int(np.argmax(spectrum[1:])) + 1
    peak_freq = float(freqs[peak_idx])
    peak_period = 1.0 / max(peak_freq, 1e-12)
    omega_dt = 2 * np.pi * peak_freq  # rad per step

    print(f"    Peak frequency    = {peak_freq:.5f} cycles/step")
    print(f"    Peak period       = {peak_period:.4f} steps")
    print(f"    ω·dt              = {omega_dt:.5f} rad/step")
    print(f"    Engine dt·c/dx    = {lattice.dt * lattice.c / lattice.dx:.4f} (= 1/√2 ≈ 0.707)")

    # Expected: in natural units (m_e=c=ℏ=ℓ_node=1), ω_Compton=1, dt=1/√2
    # → ω·dt = 1/√2 ≈ 0.707 rad/step → period = 2π/(1/√2) = 2π·√2 ≈ 8.89 steps
    expected_period_natural = 2 * np.pi * np.sqrt(2)
    print(f"    Expected period (natural-units Compton) = {expected_period_natural:.4f} steps")
    period_ratio = peak_period / expected_period_natural
    print(f"    Period ratio (measured/expected) = {period_ratio:.4f}")

    # SI-units interpretation
    omega_measured_SI = omega_dt / lattice.dt  # rad/s in SI
    omega_compton_SI = M_E_SI * C_SI ** 2 / (1.054571817e-34)  # ℏ in SI
    print()
    print(f"  SI-units cross-check:")
    print(f"    ω_measured     = {omega_measured_SI:.4e} rad/s")
    print(f"    ω_Compton (SI) = {omega_compton_SI:.4e} rad/s")
    print(f"    ratio          = {omega_measured_SI/omega_compton_SI:.4e}")
    print(f"    (this should be near 1 IF dx is interpreted as ℓ_node = {ELL_NODE:.4e} m)")

    # Q-factor (algebraic from corpus formula, NOT measured from envelope decay
    # since closed lossless lattice has no leak)
    print()
    print(f"  Q-factor (algebraic, per doc 16_/17_ formula at measured ω):")
    print(f"    Q_corpus = 1/α = {1/ALPHA:.3f}")
    print(f"    Z_0 = {Z_0:.4f} Ω")
    print(f"    α   = {ALPHA:.6e}")
    print(f"    [Q at the bond level requires R_TIR = Z_0/(4π) = {Z_0/(4*np.pi):.4f} Ω]")
    print(f"    [closed lossless lattice → numerical Q is infinite by construction;")
    print(f"     algebraic Q from corpus formula is the comparison target]")

    # Sample trajectory for visual inspection
    print()
    print(f"  V_inc[A] trajectory (first 20 steps):")
    print(f"    {'step':<6}{'V_inc[A]':<14}{'V_ref[A]':<14}{'V_inc[B]':<14}{'V_ref[B]':<14}{'E_total':<14}")
    for step in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 25, 50, 100, 150, n_steps]:
        if step <= n_steps:
            print(f"    {step:<6}{V_inc_A[step]:<+14.4e}{V_ref_A[step]:<+14.4e}"
                  f"{V_inc_B[step]:<+14.4e}{V_ref_B[step]:<+14.4e}{energy_lattice[step]:<14.4e}")


if __name__ == "__main__":
    main(N=8, n_steps=200, V_amp=0.05)
