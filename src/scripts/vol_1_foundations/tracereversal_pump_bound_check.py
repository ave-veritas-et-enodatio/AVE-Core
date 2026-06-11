#!/usr/bin/env python3
"""Trace-reversal V->omega pump: boundedness bound-check (ANALYTIC, not an engine run).

Companion to research/2026-06-09_tracereversal-pump-derivation_result.md.

WHAT THIS IS (ave-driver-script-honesty):
  A closed-form comparison of TWO candidate forms for the longitudinal-scalar ->
  microrotational (V->omega) "pump" at the |Gamma|=1 saturation wall, swept across
  the saturation amplitude A in [0, 1):

    (1) BOUNDARY-CONDITION form (Option-D, doc 54 sec 7 / sec 6a; the moving-Gamma=-1
        boundary of 2026-06-06_saturation-tir-moving-boundary-result.md sec 3):
        the V->omega transfer is governed by the reflection coefficient on the
        bounded unit disk. Op3  Gamma = (Z_eff - Z0)/(Z_eff + Z0)  with the
        asymmetric-Meissner impedance  Z_eff = Z0 * sqrt(S_mu/S_eps).  The confined
        (mode-converted) power fraction is the reflected fraction  R = Gamma^2 =
        1 - T^2  (Op17  T^2 = 1 - Gamma^2, operators.md:57).  Bounded in [0,1] for
        ALL A in [0,1] because |Gamma| <= 1 on the lossless unit circle
        (biquaternion null cone, 2026-06-06_biquaternion-node-algebra-result.md sec 5).

    (2) BULK-LAGRANGIAN-FORCE form (the engine's detonating A28 double-count,
        vacuum_engine.py:1605-1613 "runaway / 1700x growth in one step"; the
        energy-term blowup of moving-boundary-result.md sec 3, |omega|_max -> 2.2e5):
        a force proportional to the saturation-energy gradient
        F_bulk ~ |dS/dA| = A / sqrt(1 - A^2)  ->  diverges as A -> 1.

  This script does NOT host an electron, does NOT run the K4/Cosserat engine, and
  makes NO emergence claim. It ONLY demonstrates the analytic boundedness contrast
  that the derivation's load-bearing step asserts: the boundary-condition transfer
  stays finite through A->1; the bulk force detonates.

CANONICAL ANCHORS (verify-before-cite; imported, not fit):
  - Op17 power transmission  T^2 = 1 - Gamma^2           (operators.md:57)
  - Op3  reflection           Gamma = (Z2-Z1)/(Z2+Z1)    (operators.md:43)
  - asymmetric Meissner       Z_eff = Z0 sqrt(S_mu/S_eps) (doc 54 sec 6, eq Z_eff)
  - Axiom-4 kernel            S = sqrt(1 - A^2)           (CLAUDE.md INVARIANT-S2)
  - chirality coupling        kappa_chiral = 1.2 * alpha  (doc 54 sec 6, doc 20)
  - autoresonant lock window  delta_lock  = omega_0 * alpha (doc 54 sec 7, Q=1/alpha)
"""
from __future__ import annotations

import os
import sys

import numpy as np

# canonical constants (ave-canonical-source; no fitting to 137.036)
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "..", ".."))
try:
    from src.ave.core.constants import ALPHA  # type: ignore
except Exception:  # pragma: no cover - fallback if run outside package layout
    ALPHA = 7.2973525693e-3

KAPPA_CHIRAL = 1.2 * ALPHA          # electron (2,3): chi = alpha * pq/(p+q) = 1.2 alpha
DELTA_LOCK_OVER_W0 = ALPHA          # delta_lock = omega_0 * alpha (Q = 1/alpha)


def impedance_ratio(A: np.ndarray) -> np.ndarray:
    """Z_eff / Z0 for the asymmetric-Meissner wall (mu-sector saturates first).

    S_mu = sqrt(1 - A^2)  (magnetic sector reaches yield),  S_eps ~ 1 (electric lags)
    Z_eff/Z0 = sqrt(S_mu / S_eps) = (1 - A^2)^(1/4).
    A=0 -> 1 (matched, no wall);  A->1 -> 0 (short, Gamma->-1).
    """
    return (1.0 - A**2) ** 0.25


def gamma_op3(A: np.ndarray) -> np.ndarray:
    """Op3 reflection coefficient at the wall:  Gamma = (z - 1)/(z + 1)."""
    z = impedance_ratio(A)
    return (z - 1.0) / (z + 1.0)


def confined_fraction_op17(A: np.ndarray) -> np.ndarray:
    """BOUNDARY-CONDITION pump: confined (reflected, mode-converted) power fraction.

    R = Gamma^2 = 1 - T^2  (Op17).  This is the fraction of incident longitudinal V
    power that is reflected into the standing wave and mode-converted into omega at
    the wall.  Bounded in [0, 1] for all A because |Gamma| <= 1.
    """
    g = gamma_op3(A)
    return g**2  # = 1 - (1 - g**2) = 1 - T^2


def transmission_op17(A: np.ndarray) -> np.ndarray:
    """Op17 power transmission INTO the wall:  T^2 = 1 - Gamma^2.  -> 0 at the wall."""
    g = gamma_op3(A)
    return 1.0 - g**2


def bulk_force_dS_dA(A: np.ndarray) -> np.ndarray:
    """BULK-LAGRANGIAN-FORCE pump (detonating):  F ~ |dS/dA| = A / sqrt(1 - A^2)."""
    return A / np.sqrt(1.0 - A**2)


def main() -> None:
    print("=" * 74)
    print("Trace-reversal V->omega pump: boundedness bound-check (ANALYTIC)")
    print("=" * 74)
    print(f"alpha (canonical)        = {ALPHA:.10e}")
    print(f"kappa_chiral = 1.2 alpha = {KAPPA_CHIRAL:.6e}")
    print(f"delta_lock/omega_0 = alpha = {DELTA_LOCK_OVER_W0:.6e}")
    print()

    probes = np.array([0.0, 0.5, 0.9, 0.99, 0.999, 0.9999, 0.999999])
    print(f"{'A':>10} {'Z_eff/Z0':>10} {'Gamma':>10} "
          f"{'T^2(Op17)':>10} {'R=Gamma^2':>11} {'F_bulk~dS/dA':>14}")
    print("-" * 74)
    for A in probes:
        z = impedance_ratio(A)
        g = gamma_op3(A)
        T2 = transmission_op17(A)
        R = confined_fraction_op17(A)
        Fb = bulk_force_dS_dA(A)
        print(f"{A:>10.6f} {z:>10.6f} {g:>10.6f} "
              f"{T2:>10.6f} {R:>11.6f} {Fb:>14.4e}")
    print("-" * 74)

    # boundedness assertions (the load-bearing checks)
    A_dense = np.linspace(0.0, 1.0 - 1e-12, 200_001)
    R_dense = confined_fraction_op17(A_dense)
    T2_dense = transmission_op17(A_dense)
    Fb_dense = bulk_force_dS_dA(A_dense)

    R_max = float(np.nanmax(R_dense))
    R_at_wall = float(confined_fraction_op17(np.array([1.0 - 1e-12]))[0])
    Fb_at_wall = float(bulk_force_dS_dA(np.array([1.0 - 1e-12]))[0])
    power_residual = float(np.nanmax(np.abs(R_dense + T2_dense - 1.0)))

    print()
    print("BOUNDEDNESS VERDICT:")
    bc_bounded = R_max <= 1.0 + 1e-9
    print(f"  boundary-condition transfer  R=Gamma^2 in [0,1]?  "
          f"max(R) = {R_max:.10f}  -> {'BOUNDED' if bc_bounded else 'UNBOUNDED'}")
    print(f"    R(A->1) = {R_at_wall:.10f}  (total confinement at the null cone)")
    print(f"  Op17 power closes  R + T^2 = 1 ?  max|R+T^2-1| = {power_residual:.2e}"
          f"  -> {'CLOSED (no free energy)' if power_residual < 1e-9 else 'OPEN'}")
    print(f"  bulk-force  F~A/sqrt(1-A^2)  at A->1 = {Fb_at_wall:.4e}  -> DIVERGES")
    print()
    print("  => the boundary-condition (Option-D / Op17) form is FINITE through A->1;")
    print("     the bulk-Lagrangian-force form DETONATES at the wall. (cf engine A28")
    print("     runaway vacuum_engine.py:1605-1613; moving-boundary-result sec 3.)")

    # figure
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        A = A_dense
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))

        ax[0].plot(A, confined_fraction_op17(A), lw=2,
                   label=r"confined $R=\Gamma^2=1-T^2$ (Op17, bounded)")
        ax[0].plot(A, transmission_op17(A), lw=2, ls="--",
                   label=r"transmitted $T^2=1-\Gamma^2$ (Op17)")
        ax[0].axhline(1.0, color="k", lw=0.6, ls=":")
        ax[0].set_xlabel(r"saturation amplitude $A$  ($A\!\to\!1$ = $\Gamma=-1$ wall)")
        ax[0].set_ylabel("power fraction")
        ax[0].set_title("Boundary-condition pump (Op17): BOUNDED")
        ax[0].set_ylim(-0.05, 1.1)
        ax[0].legend(fontsize=8, loc="center left")

        ax[1].semilogy(A, bulk_force_dS_dA(A), lw=2, color="C3",
                       label=r"bulk force $\sim|dS/dA|=A/\sqrt{1-A^2}$")
        ax[1].semilogy(A, np.maximum(confined_fraction_op17(A), 1e-6), lw=2, color="C0",
                       label=r"boundary transfer $\Gamma^2$ (bounded $\leq 1$)")
        ax[1].axhline(1.0, color="k", lw=0.6, ls=":")
        ax[1].set_xlabel(r"saturation amplitude $A$")
        ax[1].set_ylabel("transfer magnitude (log)")
        ax[1].set_title("Bulk-force pump: DETONATES at the wall")
        ax[1].legend(fontsize=8, loc="upper left")

        fig.suptitle("V->omega trace-reversal pump: bounded boundary condition "
                     "vs detonating bulk force", fontsize=11)
        fig.tight_layout(rect=(0, 0, 1, 0.96))
        out = os.path.join(_HERE, "tracereversal_pump_bound_check.png")
        fig.savefig(out, dpi=130)
        print()
        print(f"figure saved: {out}")
    except Exception as e:  # pragma: no cover
        print(f"(figure skipped: {e})")


if __name__ == "__main__":
    main()
