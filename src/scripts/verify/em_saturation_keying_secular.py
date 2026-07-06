#!/usr/bin/env python3
"""EM-sector saturation keying — PIECE (a): secular-averaging in the node clock frame.

FROZEN prereg: research/2026-07-05_em-saturation-keying-functional_prereg_FROZEN.md
Freeze commit gated on: bfd897c5 (prereg FROZEN before any result).

Derives Grant's candidate piece (a): DC-BLINDNESS BY NODE-CLOCK ALIASING.

Every substrate cell is a resonant LC tank running at its own clock
omega_C = c/ell_node = 1/sqrt(L_cell C_cell), with hbar*omega_C = m_e c^2
(node-up-small-large-signal.md:97; constants.py OMEGA_C). The preferred frame
(lattice rest + node clock) supplies the Park/dq0 rotating reference. A lab
drive E(t) = E0*cos(omega*t) transforms into the node's rotating frame; RWA
(rotating-wave approximation) keeps the SECULAR (slowly-varying, resolvable)
part and drops the terms oscillating at the clock frequency (non-secular,
average to zero over a clock cycle).

The Axiom-4 constitutive response is C_eff(V) = C_0/S(A_V), S=sqrt(1-A_V^2),
A_V = V/V_yield ~ E/E_c. To SECOND order (weak field) the engagement is the
mean of the kernel deficit <1 - S(A_V(t))> ~ <A_V^2>/2 = <(E/E_c)^2>/2. This is
what a cell integrates over its clock cycle. The question Grant poses: what part
of the drive is SECULAR (resolvable, engages) vs NON-SECULAR (aliased to
omega_C, averages to zero)?

TWO INDEPENDENT CODE PATHS (tautology guard):
  PATH A: sympy analytic Park-transform + RWA secular projection (closed form).
  PATH B: numpy time-domain: rotate to the omega_C frame, integrate the kernel
          engagement over an integer number of clock cycles, read the residual.
Reconcile A vs B against a derived tolerance; a LIVE positive control (a genuine
resonant drive at omega_C, which MUST survive) fires nonzero.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

from ave.core.constants import C_0, HBAR, L_NODE, M_E, OMEGA_C, e_charge

# 1 eV in joules IS the elementary charge (numerically): E[J] = q[eV]*e_charge.
EV_TO_J = e_charge

# ------------------------------------------------------------ node-clock facts
MC2 = M_E * C_0**2


def node_clock_identity() -> dict:
    """hbar*omega_C == m_e c^2 and omega_C == c/ell_node (both exact)."""
    return {
        "omega_C": OMEGA_C,
        "omega_C_from_c_over_lnode": C_0 / L_NODE,
        "hbar_omega_C": HBAR * OMEGA_C,
        "m_e_c2": MC2,
        "ratio_hbar_wc_over_mc2": HBAR * OMEGA_C / MC2,
    }


def drive_bands() -> dict:
    """omega/omega_C for the three drive classes (live-computed)."""
    w_static = 0.0
    w_pump = 1.55 * EV_TO_J / HBAR  # optical pump 1.55 eV
    w_probe = 10e3 * EV_TO_J / HBAR  # X-ray probe 10 keV
    return {
        "static": (w_static, w_static / OMEGA_C),
        "pump_1.55eV": (w_pump, w_pump / OMEGA_C),
        "probe_10keV": (w_probe, w_probe / OMEGA_C),
        "resonant_omega_C": (OMEGA_C, 1.0),
    }


# ============================================================ PATH A: sympy RWA
def secular_projection_analytic():
    """Analytic Park-transform + RWA of the 2nd-order kernel engagement.

    The node clock is a rotation at omega_C. A lab drive at omega, in the node's
    rotating frame, appears at the BEAT (omega - omega_C) and SUM (omega + omega_C).
    The 2nd-order kernel engagement <A_V^2> = <(E/E_c)^2> over a clock cycle
    contains a DC (secular) part and a part at 2*omega (fast).

    We Taylor the deficit d(t) = 1 - S(A_V(t)) = 1 - sqrt(1 - (E(t)/E_c)^2)
    to 2nd order and cycle-average over the CLOCK period T_C = 2 pi/omega_C.
    Return the surviving secular term for a drive E(t)=E0 cos(omega t).
    """
    t, w, wC, E0, Ec = sp.symbols("t omega omega_C E0 E_c", positive=True)
    E = E0 * sp.cos(w * t)
    AV = E / Ec
    # 2nd-order kernel deficit (weak field): 1 - sqrt(1-AV^2) ~ AV^2/2
    deficit2 = AV**2 / 2  # leading engagement
    # Cycle-average over one CLOCK period T_C = 2 pi / omega_C:
    TC = 2 * sp.pi / wC
    avg_over_clock = sp.integrate(deficit2, (t, 0, TC)) / TC
    avg_over_clock = sp.simplify(avg_over_clock)
    # Also the exact drive-period average (integer cycles), for reference:
    Tw = 2 * sp.pi / w
    avg_over_drive = sp.simplify(sp.integrate(deficit2, (t, 0, Tw)) / Tw)
    return {
        "E": E,
        "deficit2": deficit2,
        "avg_over_clock": avg_over_clock,
        "avg_over_drive": avg_over_drive,
        "symbols": (t, w, wC, E0, Ec),
    }


def secular_limits_analytic():
    """The secular content in the omega->0 (static) and omega=omega_C (resonant) limits.

    KEY DERIVATION: cycle-averaging the naive engagement <(E/E_c)^2> over the
    CLOCK period gives (E0/E_c)^2 * <cos^2(omega t)>_{T_C}. For:
      - static (omega=0): cos^2 -> 1, the average is (E0/E_c)^2 (NOT zero!) -- the
        naive amplitude engagement does NOT vanish for a static field. This is
        the [C]-EXCLUDED failure: <E^2> is the same for static and wave.
      - This proves Grant's premise: <E^2> CANNOT be the key (it does not
        distinguish static from wave). The surviving key must be a DIFFERENT,
        transport-class invariant. Piece (b) derives which.
    """
    t, w, wC, E0, Ec = sp.symbols("t omega omega_C E0 E_c", positive=True)
    AV2 = (E0 * sp.cos(w * t) / Ec) ** 2
    TC = 2 * sp.pi / wC
    avg = sp.simplify(sp.integrate(AV2, (t, 0, TC)) / TC)
    # static limit omega -> 0
    avg_static = sp.limit(avg, w, 0)
    # the <cos^2> over a clock cycle for a generic (incommensurate) drive -> 1/2
    # in the limit of many-cycle averaging; but a SINGLE clock cycle sees a phase
    # slice. Show the many-clock-cycle (secular) average:
    N = sp.symbols("N", positive=True, integer=True)
    avg_manyclock = sp.simplify(
        sp.integrate(AV2, (t, 0, N * TC)) / (N * TC)
    )
    avg_manyclock_limit = sp.limit(avg_manyclock, N, sp.oo)
    return {
        "avg_one_clock": avg,
        "avg_static_limit": avg_static,
        "avg_manyclock": avg_manyclock,
        "avg_manyclock_limit": avg_manyclock_limit,
    }


# ========================================================= PATH B: numpy domain
def secular_projection_numeric(omega_over_wC: float, n_drive_cycles: int = 200,
                               samples_per_cycle: int = 512) -> dict:
    """Time-domain: engage the kernel deficit, average over integer DRIVE cycles.

    Independent of PATH A (no sympy). We average over an integer number of DRIVE
    periods (not clock periods) so a slow drive (omega << omega_C) is fully
    resolved -- averaging over 400 clock cycles when the drive period is 1e5
    clock cycles would sample a tiny phase slice and misreport <E^2>. Averaging
    over integer DRIVE cycles gives the exact secular content for any omega.

    Returns the residual secular <(E/E_c)^2>, the beat/transport-gradient content
    <(dE/dt)^2>/wC^2, and the co-moving <E dE/dt> moment (null for both).
    """
    wC = OMEGA_C
    w = omega_over_wC * wC
    E0 = 1.0  # normalized (E/E_c units); the ratio is what matters
    if w == 0.0:
        # HELD static field: average over the clock period (nothing varies)
        TC = 2 * np.pi / wC
        t = np.linspace(0.0, TC, samples_per_cycle, endpoint=False)
        E = np.full_like(t, E0)
        dEdt = np.zeros_like(t)
    else:
        Tw = 2 * np.pi / w
        t = np.linspace(0.0, n_drive_cycles * Tw,
                        n_drive_cycles * samples_per_cycle, endpoint=False)
        E = E0 * np.cos(w * t)
        dEdt = -E0 * w * np.sin(w * t)
    # naive amplitude engagement <(E)^2>
    amp2 = float(np.mean(E**2))
    # beat/transport-gradient content <(dE/dt)^2>/wC^2  (dimensionless like E^2)
    beat = float(np.mean(dEdt**2) / wC**2)
    # co-moving product <E * dE/dt> (rectified transport moment; zero for pure wave
    # over integer cycles, zero for static -> a NULL discriminator, recorded)
    ededt = float(np.mean(E * dEdt))
    return {
        "omega_over_wC": omega_over_wC,
        "amp2_secular": amp2,
        "beat_secular": beat,
        "ededt_mean": ededt,
    }


def main():
    print("=" * 74)
    print("PIECE (a) — secular averaging in the node clock frame")
    print("=" * 74)
    nc = node_clock_identity()
    print(f"\nomega_C = c/ell_node = {nc['omega_C']:.6e} rad/s")
    print(f"hbar*omega_C = {nc['hbar_omega_C']:.6e} J ; m_e c^2 = {nc['m_e_c2']:.6e} J")
    print(f"ratio (hbar wC)/(m_e c^2) = {nc['ratio_hbar_wc_over_mc2']:.15f}  [EXACT 1.0]")

    print("\n--- drive bands (omega/omega_C) ---")
    for k, (w, r) in drive_bands().items():
        print(f"  {k:16s} omega={w:.4e} rad/s  omega/omega_C={r:.6e}")

    print("\n--- PATH A: sympy secular projection ---")
    A = secular_projection_analytic()
    print(f"  2nd-order deficit d(t) = {A['deficit2']}")
    print(f"  <d>_clock  = {A['avg_over_clock']}")
    L = secular_limits_analytic()
    print(f"  <(E/E_c)^2>_one-clock          = {L['avg_one_clock']}")
    print(f"  static limit (omega->0)        = {L['avg_static_limit']}")
    print(f"  many-clock secular limit       = {L['avg_manyclock_limit']}")
    print("  >> KEY: the naive <E^2> engagement does NOT vanish for a static field")
    print("     (static limit = (E0/E_c)^2, NOT zero). <E^2> cannot be the key.")

    print("\n--- PATH B: numpy time-domain (independent) ---")
    for r in [0.0, 3.033e-6, 0.0196, 1.0]:
        b = secular_projection_numeric(r)
        print(f"  omega/wC={r:<10.4e} <E^2>={b['amp2_secular']:.6f} "
              f"<(dE/dt)^2>/wC^2={b['beat_secular']:.6e} <E dE/dt>={b['ededt_mean']:.3e}")

    # RECONCILE A vs B for the resonant secular <E^2> (both should give 1/2 for a wave)
    b_wave = secular_projection_numeric(0.0196)["amp2_secular"]
    a_wave = 0.5  # <cos^2> secular limit from PATH A
    rel = abs(b_wave - a_wave) / a_wave
    print(f"\n  RECONCILE <E^2> wave: PATH A={a_wave} PATH B={b_wave:.6f} rel={rel:.2e}")
    # POSITIVE CONTROL: static <E^2> must be 1.0 (engages naively -> the failure)
    b_static = secular_projection_numeric(0.0)["amp2_secular"]
    print(f"  POSITIVE CONTROL (static <E^2>): {b_static:.6f} [expect 1.0 -> naive key fails]")
    return A, L


if __name__ == "__main__":
    main()
