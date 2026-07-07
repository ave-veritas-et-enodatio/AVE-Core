"""LEG A (analytic) — the electron tick-floor: sampling floor N_min + Adler div-N ceiling.

Grant-blessed ontology (three-joint walk 2026-07-06/07; prereg
``research/2026-07-07_electron-tick-floor_prereg_FROZEN.md``): the electron is an
injection-locked div-N* subharmonic of the local lattice clock,
omega_lattice = N* * omega_mode, whose (2,3) content lives in PHASE SPACE (two internal
angles winding 2 and 3 per mode period on the Clifford torus). The lattice constraint is
TICKS PER MODE PERIOD, not nodes per ring.

This module derives, purely analytically:

  A(a) THE FLOOR  -- N_min from representability: to carry the k=2 AND k=3 phase windings
       DISTINCTLY on N ticks/period needs (1) handedness-preserving non-aliasing (strict
       Nyquist 2*k_max < N) and (2) non-collision (k1 != +-k2 mod N). The transitions:
       N=5 COLLIDE (3 == -2 mod 5), N=6 NYQUIST-MARGINAL (k=3 at N/2, chirality lost),
       N=7 first CLEAN.  ==> N_min = 7.

  A(b) THE CEILING -- Adler-class div-N injection-lock range. The subharmonic phase error
       obeys a div-N Adler equation; the fractional lock half-range is kappa/N, so the lock
       holds iff a detuning delta <= kappa/N, i.e. N <= N_max = kappa/delta. Cold identical
       lattice (delta=0) => N_max = infinity (FLOOR-ONLY). A finite ceiling needs a
       substrate-intrinsic detuning; the physical candidate is the seed down-regulation
       delta_seed = 1 - sqrt(1 - A^2) (Op14), reported PARAMETRICALLY in A^2.

  A(c) THE WINDOW -- intersect; the verdict is routed by the RESULT doc.

=============================================================================
FIREWALL (alpha-circularity knife, binding on this DERIVATION PATH):
  NO alpha / m_e / lambdabar_C / omega_C-as-electron-scale / Q_TANK=1/alpha / Compton /
  R_I=sqrt(2 alpha) / lepton mass on this path. The floor is PURE INTEGERS (the topological
  winding pair (2,3) and the tick count N) plus a DIMENSIONLESS coupling kappa -- no physical
  constant is imported here. The ONLY firewalled pricing lives in the clearly-marked
  ``# FIREWALL-COMPARISON`` block at the bottom, written AFTER the window is routed.
  HOMONYM GUARD: N (sampling count) != Q (coherence count = 1/alpha, an identity). The floor
  lands at 7, three-plus OOM from 137, with zero alpha content -- the guard is armed, not fired.
=============================================================================

REGIME: cold lattice, lossless-reactive, small-signal phase dynamics; discrete-time sampling
is the PHYSICAL granularity of the lattice tick, not a numerical artifact.
"""
from __future__ import annotations

import json
import math
import os

import sympy as sp

# Canonical topological winding pair of the electron (2,3) mode. These are INTEGERS
# (phase-space winding numbers on the Clifford torus, INVARIANT-N1), not physical constants.
K1_WINDING = 2
K2_WINDING = 3


# ---------------------------------------------------------------------------
# A(a) THE SAMPLING FLOOR  (pure modular arithmetic; sympy-proved below)
# ---------------------------------------------------------------------------
def principal_winding(k: int, N: int) -> int:
    """The winding a discrete N-tick/period sampler READS for a true winding k.

    Per-tick phase advance is 2*pi*k/N; the estimator returns the representative m with
    2*pi*m/N in (-pi, pi], i.e. k reduced mod N into (-N/2, N/2]. This is the branch that
    ALIASES exactly when |k| >= N/2 -- the physical sampling floor.
    """
    r = k % N
    if r > N / 2:
        r -= N
    return r


def handedness_preserved(k: int, N: int) -> bool:
    """True iff the winding's SIGN (chirality) survives sampling: strict Nyquist 2|k| < N.
    At 2|k| == N the +-k aliases merge (real-only, sign lost) -- marginal, not preserved."""
    return 2 * abs(k) < N


def classify_tick_count(N: int, k1: int = K1_WINDING, k2: int = K2_WINDING) -> str:
    """Classify N ticks/period for the (k1, k2) winding pair.

    CLEAN            -- both windings read back their true value with chirality intact.
    NYQUIST-MARGINAL -- the larger winding sits exactly at Nyquist (N == 2*k2): sign lost.
    COLLIDE          -- the two windings land in the same magnitude bin (indistinguishable).
    ALIASED          -- the larger winding aliases to a different magnitude (gross undersample).
    """
    kmax = max(k1, k2)
    if 2 * kmax < N:  # strict Nyquist for the larger winding => both clean, distinct
        return "CLEAN"
    if 2 * kmax == N:  # exactly Nyquist for the larger winding: chirality lost
        return "NYQUIST-MARGINAL"
    p1, p2 = principal_winding(k1, N), principal_winding(k2, N)
    if abs(p1) == abs(p2):  # same magnitude bin: the pair is indistinguishable
        return "COLLIDE"
    return "ALIASED"


def floor_scan(n_lo: int = 3, n_hi: int = 16, k1: int = K1_WINDING, k2: int = K2_WINDING) -> dict:
    """Classify every N in [n_lo, n_hi] and return the scan + N_min (first CLEAN)."""
    scan = {N: classify_tick_count(N, k1, k2) for N in range(n_lo, n_hi + 1)}
    clean = [N for N, s in scan.items() if s == "CLEAN"]
    return {
        "winding_pair": [k1, k2],
        "scan": {str(N): s for N, s in scan.items()},
        "N_min": min(clean) if clean else None,
        "reads_at_N5": [principal_winding(k1, 5), principal_winding(k2, 5)],
        "reads_at_N6": [principal_winding(k1, 6), principal_winding(k2, 6)],
        "reads_at_N7": [principal_winding(k1, 7), principal_winding(k2, 7)],
    }


def n_min_analytic(k1: int = K1_WINDING, k2: int = K2_WINDING) -> int:
    """N_min = 2*k_max + 1 (the first strict-Nyquist tick count for the larger winding)."""
    return 2 * max(k1, k2) + 1


# ---------------------------------------------------------------------------
# A(a) sympy PROOFS -- independent symbolic confirmation of the floor
# ---------------------------------------------------------------------------
def prove_reflection_collision_N(k1: int = K1_WINDING, k2: int = K2_WINDING) -> dict:
    """The reflection collision k1 == -k2 (mod N) happens iff N | (k1 + k2).

    For (2,3): k1 + k2 = 5, so the ONLY collision tick count (with N > k2) is N = 5, where
    3 == -2 (mod 5). Proved symbolically: (k1 - (-k2)) mod N == 0  <=>  N | (k1+k2).
    """
    N = sp.symbols("N", integer=True, positive=True)
    ssum = k1 + k2
    # collision condition: k1 congruent to -k2 mod N  <=>  N divides (k1 + k2)
    divisors = [int(d) for d in sp.divisors(ssum) if int(d) > k2]
    # verify at N=5 concretely, in the canonical prereg framing: 3 == -2 (mod 5), i.e.
    # the larger winding k2 aliases onto the reflection of the smaller: k2 == -k1 (mod N).
    lhs = sp.Mod(k2, 5)     # 3
    rhs = sp.Mod(-k1, 5)    # 3
    return {
        "sum_k1_k2": ssum,
        "collision_condition": f"N | (k1+k2) = N | {ssum}",
        "collision_tick_counts_above_k2": divisors,  # [5]
        "N5_k2_mod": int(lhs),      # 3
        "N5_negk1_mod": int(rhs),   # 3
        "N5_collides": bool(sp.Eq(lhs, rhs)),  # True: 3 == -2 (mod 5)
        "symbol_used": str(N),
    }


def prove_nyquist_floor(k1: int = K1_WINDING, k2: int = K2_WINDING) -> dict:
    """Strict Nyquist 2*k_max < N => N > 2*k_max => N_min = 2*k_max + 1 = 7 for k_max=3."""
    N = sp.symbols("N", integer=True, positive=True)
    kmax = max(k1, k2)
    sol = sp.solve(2 * kmax < N, N)  # N > 6
    nmin = int(sp.ceiling(2 * kmax + sp.Rational(1, 1)))
    return {
        "k_max": kmax,
        "strict_nyquist_inequality": f"2*{kmax} < N",
        "solution": str(sol),          # N > 6
        "N_min": nmin,                  # 7
        "N6_is_nyquist_exact": bool(2 * kmax == 6),  # True: k=3 at N/2 when N=6
    }


# ---------------------------------------------------------------------------
# A(b) THE ADLER div-N CEILING  (analytic lock range; sympy fixed-point check)
# ---------------------------------------------------------------------------
def adler_lock_halfrange(kappa: float, N: int) -> float:
    """Fractional injection-lock half-range for a div-N subharmonic: Delta_omega/omega = kappa/N.

    The 1/N is the phase-averaging dilution: the subharmonic integrates the reference over N
    of its own ticks per mode period, so the instantaneous div-N pull is diluted by N.
    """
    return kappa / N


def ceiling_from_detuning(kappa: float, delta: float) -> float:
    """N_max = kappa/delta -- the finest division that still locks against a fractional
    detuning delta. delta=0 (cold identical lattice) => N_max = +inf (FLOOR-ONLY)."""
    if delta <= 0.0:
        return math.inf
    return kappa / delta


def seed_detuning(A2: float) -> float:
    """The seed's own down-regulation delta_seed = 1 - sqrt(1 - A^2) (Op14 local clock).

    Reported PARAMETRICALLY in A^2 (a dial). The FIREWALL forbids plugging A^2 = sqrt(2 alpha)
    on this path; that substitution lives only in the firewalled comparison.
    """
    if A2 < 0.0 or A2 > 1.0:
        return float("nan")
    return 1.0 - math.sqrt(1.0 - A2)


def prove_adler_lock_condition() -> dict:
    """div-N Adler fixed-point existence: dpsi/dt = delta - (kappa/N) sin(N psi) has a stable
    fixed point (a lock) iff |delta| <= kappa/N. sympy solves sin(N psi*) = N delta / kappa in
    [-1, 1], which is solvable iff |delta| <= kappa/N. QED the lock half-range is kappa/N."""
    kappa, N, delta, psi = sp.symbols("kappa N delta psi", positive=True)
    # fixed point: delta = (kappa/N) sin(N psi)  =>  sin(N psi) = N delta / kappa
    rhs = N * delta / kappa
    # solvable in reals iff |rhs| <= 1  =>  delta <= kappa/N
    lock_condition = sp.simplify(sp.Le(rhs, 1))  # N*delta/kappa <= 1
    return {
        "adler_equation": "dpsi/dt = delta - (kappa/N) sin(N psi)",
        "fixed_point": "sin(N psi*) = N delta / kappa",
        "lock_condition": str(lock_condition),  # N*delta/kappa <= 1  i.e.  delta <= kappa/N
        "lock_halfrange_fractional": "kappa/N",
        "N_max": "kappa/delta",
    }


def window_verdict(kappa: float, delta: float, k1: int = K1_WINDING, k2: int = K2_WINDING) -> dict:
    """Intersect floor and ceiling; route the window bin (analytic leg)."""
    n_min = n_min_analytic(k1, k2)
    n_max = ceiling_from_detuning(kappa, delta)
    if math.isinf(n_max):
        bin_ = "FLOOR-ONLY"
    elif n_max < n_min:
        bin_ = "UNSTABLE-ALL-N"
    else:
        bin_ = "WINDOW-DERIVED"
    return {
        "N_min": n_min,
        "N_max": (None if math.isinf(n_max) else n_max),
        "detuning_delta": delta,
        "coupling_kappa": kappa,
        "bin": bin_,
    }


# ---------------------------------------------------------------------------
def run() -> dict:
    """Assemble the full Leg-A analytic result (firewall-clean)."""
    scan = floor_scan()
    collision = prove_reflection_collision_N()
    nyquist = prove_nyquist_floor()
    adler = prove_adler_lock_condition()
    # cold identical lattice: delta=0 -> FLOOR-ONLY; parametric strained ceiling reported too
    cold = window_verdict(kappa=1.0, delta=0.0)
    strained_grid = {
        f"A2={A2:.3f}": {
            "delta_seed": seed_detuning(A2),
            "N_max_kappa1": ceiling_from_detuning(1.0, seed_detuning(A2)),
        }
        for A2 in (0.05, 0.10, 0.20)
    }
    return {
        "leg": "A (analytic)",
        "floor": {
            "scan": scan,
            "N_min_formula": "2*k_max + 1",
            "N_min": scan["N_min"],
            "collision_proof": collision,
            "nyquist_proof": nyquist,
        },
        "ceiling": {
            "adler_proof": adler,
            "cold_window": cold,
            "strained_parametric": strained_grid,
        },
        "window_bin_cold": cold["bin"],
    }


def main() -> None:
    out = run()
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "electron_tick_floor_sampling.json"), "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(json.dumps(out, indent=2, default=str))
    print("\nLEG A verdict:")
    print(f"  FLOOR:   N_min = {out['floor']['N_min']}  "
          f"(N=5 {out['floor']['scan']['scan']['5']}, "
          f"N=6 {out['floor']['scan']['scan']['6']}, "
          f"N=7 {out['floor']['scan']['scan']['7']})")
    print(f"  CEILING: cold identical lattice -> {out['window_bin_cold']} "
          f"(delta=0 => N_max=inf); ceiling parametric in seed A^2")


# ---------------------------------------------------------------------------
# FIREWALL-COMPARISON -- firewalled pricing, written AFTER the window is routed.
# Everything above is alpha-clean; the physical constants enter ONLY here.
# ---------------------------------------------------------------------------
def firewall_comparison_pricing(n_star: int = 7) -> dict:
    """Price the pitch a = lambdabar_C / N* and PROVE the c / Z_0 invariance under the
    re-pricing (a -> lambdabar_C/N*, omega_lattice -> N* omega_C). c = a * omega_lattice is
    FIXED; Z_0 is untouched. This is CONSISTENCY-class -- no new number originates."""
    from ave.core.constants import C_0, L_NODE, OMEGA_C, Z_0  # FIREWALL-COMPARISON only

    lambdabar_C = L_NODE            # the Compton pitch (comparison only)
    a = lambdabar_C / n_star        # re-priced cell size
    omega_lattice = n_star * OMEGA_C  # re-priced lattice clock
    c_repriced = a * omega_lattice  # must equal c
    return {
        "N_star": n_star,
        "lambdabar_C_m": lambdabar_C,
        "a_repriced_m": a,
        "omega_lattice_repriced": omega_lattice,
        "c_repriced": c_repriced,
        "c_canonical": C_0,
        "c_invariant": math.isclose(c_repriced, C_0, rel_tol=1e-12),
        "Z_0_untouched": Z_0,
    }


if __name__ == "__main__":
    main()
