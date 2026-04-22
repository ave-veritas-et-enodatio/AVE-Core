"""
Phase C — chirality matching diagnostic on the K4 vacuum.

Question (Grant, 2026-04-21)
---------------------------
Is the photon launched by our Phase A/B infrastructure chirally
impedance-matched to the K4 vacuum? The Phase B GIF showed visible
wavefront spreading. That could be:
  (a) diffraction from a finite transverse envelope,
  (b) K4 dispersion (frequency-dependent group velocity),
  (c) chirality mismatch — a linearly polarized photon splitting into
      RH + LH helicity components that propagate at different rates on
      the intrinsically chiral bipartite K4 lattice.

This diagnostic isolates (c) by launching three photons with identical
spatial envelope but different port polarizations:

   Linear  : port pattern  −T_a = (−½,−½,+½,+½)           (h=0)
   RH-circ : T_b·cos(ωt) + T_c·sin(ωt)                    (h>0)
   LH-circ : T_b·cos(ωt) − T_c·sin(ωt)                    (h<0)

For each, we measure:
  (i)  peak helicity density and its sign along the packet
  (ii) energy surviving at x = source_x + 40 (far-from-source plane)
  (iii) transverse RMS spreading σ_y(t) in the slice z = N/2

AVE-native expectation
---------------------
The K4 bipartite A/B sublattice structure has intrinsic handedness
(per Axiom 1 — port vectors for A→B are (+,+,+), (+,−,−), (−,+,−),
(−,−,+); the handedness flips on B sites). Per §30 the photon is T₂
chiral-transverse. If ONE helicity (RH or LH) propagates with higher
fidelity (less dispersion, more energy surviving) than its mirror, the
K4 vacuum preferentially admits that handedness — the photon is
chirally impedance-matched. If both helicities behave identically, the
K4 is non-chiral at long wavelength despite bipartite substructure.

No SM/QED leakage
-----------------
Helicity here is defined by the K4-TLM port arithmetic (k4_tlm.py
:407–420): h = (V[0]+V[2])² − (V[1]+V[3])². This is a substrate
observable on Axiom 1, not a spin-angular-momentum operator. Amplitude
is ≪ V_YIELD → linear vacuum regime (Axiom 4 off).
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import C_0, V_SNAP

from photon_propagation import T2_LINEAR_A, T2_LINEAR_B, T2_LINEAR_C


class CircularChiralSource:
    """
    Inject a time-phased superposition of two T₂ basis modes to produce
    a photon with definite helicity.

    Port pattern at time t:
        port_w[n] = α·T_b[n] · cos(ω(t − t_c)) + β·T_c[n] · sin(ω(t − t_c))

    amplitude modulated by a spatial Gaussian in (y,z) and the familiar
    Gaussian time envelope.

    helicity_sign = +1  → RH (α=β=+1)
    helicity_sign = −1  → LH (α=+1, β=−1)
    helicity_sign =  0  → linear along T_a (unchanged from Phase A/B)
    """

    def __init__(
        self,
        x0: int,
        y_c: float,
        z_c: float,
        sigma_yz: float,
        omega: float,
        t_center: float,
        t_sigma: float,
        amplitude: float,
        helicity_sign: int,
    ):
        self.x0 = x0
        self.y_c = y_c
        self.z_c = z_c
        self.sigma_yz = sigma_yz
        self.omega = omega
        self.t_center = t_center
        self.t_sigma = t_sigma
        self.amplitude = amplitude
        self.helicity_sign = helicity_sign
        self._yz_profile_cache: tuple[int, int, np.ndarray] | None = None

    def _yz_profile(self, ny: int, nz: int) -> np.ndarray:
        if self._yz_profile_cache and self._yz_profile_cache[:2] == (ny, nz):
            return self._yz_profile_cache[2]
        j, k = np.indices((ny, nz), dtype=float)
        r2 = (j - self.y_c) ** 2 + (k - self.z_c) ** 2
        profile = np.exp(-r2 / (2.0 * self.sigma_yz ** 2))
        self._yz_profile_cache = (ny, nz, profile)
        return profile

    def apply(self, lattice: K4Lattice3D, t: float) -> None:
        env = np.exp(-((t - self.t_center) ** 2) / (2.0 * self.t_sigma ** 2))
        if abs(env) < 1e-30:
            return
        phase = self.omega * (t - self.t_center)
        if self.helicity_sign == 0:
            # Linear polarization: single T₂ basis mode modulated by a
            # sinusoidal carrier (matches Phase A/B infrastructure).
            port_w = -T2_LINEAR_A * np.sin(phase)
        else:
            # Circular polarization: two T₂ basis modes in time quadrature.
            # The port pattern ROTATES at ω, producing sustained non-zero
            # helicity when averaged over a cycle.  The sin-modulated factor
            # ensures the pulse amplitude is zero at t=t_center (no DC).
            port_w = (
                T2_LINEAR_B * np.sin(phase)
                + self.helicity_sign * T2_LINEAR_C * np.cos(phase)
            )
        amp = self.amplitude * env
        yz = self._yz_profile(lattice.ny, lattice.nz)
        active = lattice.mask_active[self.x0].astype(float)
        injection_spatial = amp * yz * active
        for n in range(4):
            if abs(port_w[n]) > 0:
                lattice.V_inc[self.x0, :, :, n] += port_w[n] * injection_spatial


def run_one_polarization(
    helicity_sign: int,
    N: int = 96,
    pml: int = 8,
    lambda_cells: float = 14.0,
    sigma_yz: float = 8.0,
    t_sigma_periods: float = 1.0,
    amp_frac: float = 0.005,
    source_x: int = 16,
    n_steps: int = 240,
    record_every: int = 3,
) -> dict:
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=pml)
    c = float(C_0)
    dt = lattice.dt
    omega = 2.0 * np.pi * c / (lambda_cells * lattice.dx)
    period = 2.0 * np.pi / omega
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma
    amp_volts = amp_frac * float(V_SNAP)

    src = CircularChiralSource(
        x0=source_x,
        y_c=(N - 1) / 2.0,
        z_c=(N - 1) / 2.0,
        sigma_yz=sigma_yz,
        omega=omega,
        t_center=t_center,
        t_sigma=t_sigma,
        amplitude=amp_volts,
        helicity_sign=helicity_sign,
    )

    z_slice = N // 2
    history: dict[str, list] = {
        "t": [],
        "total_energy": [],
        "total_helicity_signed": [],
        "total_helicity_abs": [],
        "energy_at_x80": [],
        "sigma_y": [],
        "x_profile": [],
        "xy_slice": [],
    }

    reference_plane = min(N - pml - 8, source_x + 60)

    for step in range(n_steps + 1):
        if step > 0:
            t_pre = step * dt
            src.apply(lattice, t_pre)
            lattice.step()
        if step % record_every == 0:
            t_now = lattice.timestep * dt
            rho = lattice.get_energy_density()
            h_density = lattice.get_helicity_density()
            total_E = float(rho.sum())
            total_h_signed = float(h_density.sum())
            total_h_abs = float(np.abs(h_density).sum())
            # Energy at the reference plane (sum over y,z at x = reference_plane)
            E_plane = float(rho[reference_plane, :, :].sum())
            # Transverse RMS width in the z=N/2 slice, weighted by rho
            sl = rho[:, :, z_slice]
            # Restrict to "downstream" portion to avoid source dominance
            down = sl[source_x + 6 : N - pml]
            if down.sum() > 0:
                iy = np.arange(N, dtype=float)
                weight = down.sum(axis=0)
                y_mean = (weight * iy).sum() / weight.sum()
                sigma_y = np.sqrt(
                    (weight * (iy - y_mean) ** 2).sum() / weight.sum()
                )
            else:
                sigma_y = np.nan
            history["t"].append(t_now)
            history["total_energy"].append(total_E)
            history["total_helicity_signed"].append(total_h_signed)
            history["total_helicity_abs"].append(total_h_abs)
            history["energy_at_x80"].append(E_plane)
            history["sigma_y"].append(sigma_y)
            history["x_profile"].append(rho.sum(axis=(1, 2)))
            history["xy_slice"].append(sl.copy())

    return {
        "helicity_sign": helicity_sign,
        "N": N,
        "pml": pml,
        "source_x": source_x,
        "reference_plane": reference_plane,
        "lambda_cells": lambda_cells,
        "sigma_yz": sigma_yz,
        "t_sigma_periods": t_sigma_periods,
        "amp_frac_vsnap": amp_frac,
        "omega_rad_s": omega,
        "period_s": period,
        "t": np.asarray(history["t"]),
        "total_energy": np.asarray(history["total_energy"]),
        "total_helicity_signed": np.asarray(history["total_helicity_signed"]),
        "total_helicity_abs": np.asarray(history["total_helicity_abs"]),
        "energy_at_reference": np.asarray(history["energy_at_x80"]),
        "sigma_y": np.asarray(history["sigma_y"]),
        "x_profile": np.stack(history["x_profile"], axis=0),
        "xy_slice": np.stack(history["xy_slice"], axis=0),
    }


def main() -> None:
    labels = ["Linear (T_a)", "RH circular", "LH circular"]
    signs = [0, +1, -1]
    results = []

    for label, sign in zip(labels, signs):
        print(f"Running: {label}  (helicity_sign = {sign})")
        res = run_one_polarization(helicity_sign=sign)
        results.append(res)
        peak_h_signed = res["total_helicity_signed"][
            np.argmax(np.abs(res["total_helicity_signed"]))
        ] if len(res["total_helicity_signed"]) > 0 else 0.0
        peak_h_abs = res["total_helicity_abs"].max()
        E_plane_peak = res["energy_at_reference"].max()
        print(
            f"  peak |h|_signed = {peak_h_signed:+.3e}, "
            f"peak Σ|h| = {peak_h_abs:.3e}, "
            f"peak E at ref plane = {E_plane_peak:.3e}"
        )

    # ── Plot comparison ──
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle(
        "Phase C — chirality matching: RH vs LH vs linear photon on K4 vacuum",
        fontsize=12,
    )

    ax = axes[0, 0]
    for res, label in zip(results, labels):
        ax.plot(res["t"] * 1e9, res["total_helicity_signed"], label=label, lw=1.4)
    ax.axhline(0, color="gray", lw=0.5)
    ax.set_xlabel("t (ns)")
    ax.set_ylabel("Σ h(r)  (signed total helicity)")
    ax.set_title("Signed total helicity vs time")
    ax.grid(alpha=0.3)
    ax.legend()

    ax = axes[0, 1]
    for res, label in zip(results, labels):
        ax.plot(res["t"] * 1e9, res["total_energy"], label=label, lw=1.4)
    ax.set_xlabel("t (ns)")
    ax.set_ylabel("Σ |V|² (total energy)")
    ax.set_title("Total energy vs time")
    ax.grid(alpha=0.3)
    ax.legend()

    ax = axes[1, 0]
    ref_plane = results[0]["reference_plane"]
    for res, label in zip(results, labels):
        ax.plot(res["t"] * 1e9, res["energy_at_reference"], label=label, lw=1.4)
    ax.set_xlabel("t (ns)")
    ax.set_ylabel(f"|V|² at x = {ref_plane} (reference plane)")
    ax.set_title(
        f"Transmitted energy at reference plane x={ref_plane}\n"
        "(higher = better vacuum matching)"
    )
    ax.grid(alpha=0.3)
    ax.legend()

    ax = axes[1, 1]
    for res, label in zip(results, labels):
        ax.plot(res["t"] * 1e9, res["sigma_y"], label=label, lw=1.4)
    ax.set_xlabel("t (ns)")
    ax.set_ylabel("σ_y of downstream packet (cells)")
    ax.set_title("Transverse RMS spreading (less = better matching)")
    ax.grid(alpha=0.3)
    ax.legend()

    plt.tight_layout()
    out_png = "/tmp/photon_chirality_diagnostic.png"
    plt.savefig(out_png, dpi=110)
    plt.close()
    print(f"\nSaved comparison plot to {out_png}")

    # Also save raw data
    out_npz = "/tmp/photon_chirality_diagnostic.npz"
    np.savez(
        out_npz,
        **{
            f"{prefix}_{key}": res[key]
            for prefix, res in zip(["lin", "rh", "lh"], results)
            for key in ["t", "total_energy", "total_helicity_signed",
                        "total_helicity_abs", "energy_at_reference",
                        "sigma_y"]
        },
    )
    print(f"Saved raw data to {out_npz}")

    # Verdict
    print("\n── Verdict ──")
    # Compare peak energy at reference plane across polarizations
    E_lin = results[0]["energy_at_reference"].max()
    E_rh = results[1]["energy_at_reference"].max()
    E_lh = results[2]["energy_at_reference"].max()
    print(f"Peak transmitted |V|² at reference plane:")
    print(f"  Linear    : {E_lin:.3e}")
    print(f"  RH circ.  : {E_rh:.3e}  ({(E_rh/E_lin-1)*100:+.1f}% vs linear)")
    print(f"  LH circ.  : {E_lh:.3e}  ({(E_lh/E_lin-1)*100:+.1f}% vs linear)")

    # Peak |helicity| (absolute, integrated over space)
    h_lin = np.abs(results[0]["total_helicity_signed"]).max()
    h_rh = np.abs(results[1]["total_helicity_signed"]).max()
    h_lh = np.abs(results[2]["total_helicity_signed"]).max()
    print(f"\nPeak |Σ h(r)| (signed-integrated helicity):")
    print(f"  Linear    : {h_lin:.3e}")
    print(f"  RH circ.  : {h_rh:.3e}")
    print(f"  LH circ.  : {h_lh:.3e}")

    asymmetry = (E_rh - E_lh) / (E_rh + E_lh) if (E_rh + E_lh) > 0 else 0.0
    print(f"\nRH/LH asymmetry (energy throughput): {asymmetry*100:+.2f}%")
    if abs(asymmetry) > 0.03:
        winner = "RH" if asymmetry > 0 else "LH"
        print(f"  → K4 vacuum preferentially transmits {winner} helicity "
              f"(chirally matched).")
    else:
        print("  → K4 vacuum transmits RH and LH symmetrically at this "
              "wavelength/amplitude (not chirally selective on empty "
              "linear vacuum; chirality selection likely arises in the "
              "Axiom-4-engaged regime or at the soliton shell).")


if __name__ == "__main__":
    main()
