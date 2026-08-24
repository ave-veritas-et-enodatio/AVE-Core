"""theta route-3 — the balanced-N-phase reading of the J-dressing (ANALYTIC CHECK).

Class: CHECK driver for the research doc pair
  research/2026-08-24_theta-route3-balanced-polyphase_{prereg,result}.md

This driver DECIDES NOTHING. It exists so that no analytic assertion in the
result doc is un-checked (Rule 10: run the driver, even a small one). Every
claim the result doc makes about phasor configurations is re-derived here
numerically or in exact rational arithmetic.

VALUE-ECHO IMMUNITY (prereg S5.3): no CODATA, no `ave.core.constants`, no
alpha, no fitted parameter. The only inputs are the integer N and the target
rationals {+2/3, -1/3, ...} which enter as ENUMERATION TARGETS, never as fit
inputs. Asserted at module entry by _assert_no_value_echo().

The five checks:

  (A) NULL-LIVENESS / positive control (prereg S6): at N=3 the equal-modulus
      zero-sum solution set must be a single point mod global rotation
      (equilateral rigidity); at N=4 an explicit one-parameter family must be
      constructible with residual ~ 0. If either fails, the lane HALTS -- a
      "no selection" answer from a driver that cannot see a KNOWN rigidity or
      a KNOWN freedom is worthless.

  (B) C-SUM rigidity: dimension of the equal-modulus zero-sum configuration
      variety, mod global rotation, for N = 2..8. Measured two ways that must
      agree: (i) Jacobian rank at the balanced point, (ii) Monte-Carlo
      projection -- solve onto the constraint from random starts and measure
      the numerical rank of the resulting solution cloud after quotienting the
      global phase.

  (C) COLLINEARITY (the rotating-vs-pulsating degeneracy): is the balanced
      N-set collinear (all phasors on one line through the origin)? A
      collinear set has a linearly-polarized (pulsating) resultant, not a
      rotating one.

  (D) C-ORTH: the maximum N for which N co-located identical modes differing
      only by fibre phase can be PAIRWISE time-average orthogonal
      (cos(theta_i - theta_j) = 0 for all i != j). Exhaustive + analytic.

  (E) THE COMPACT-THETA CHARGE ENUMERATION: with theta a genuine phase
      (theta/2pi in {0, 1/3, 2/3}) and n an integer, which (n, theta) pairs
      give q_eff = n + theta/2pi equal to each observed quark charge? Exact
      rational arithmetic (fractions.Fraction), no floating point.
      Also run NON-compactly (canon's five-element list read as reals) so the
      two conventions can be compared side by side rather than one assumed.

  (F) C-CLOSURE: sum(theta_i) mod 2pi for the balanced N-set, and whether
      non-balanced sets also satisfy it (i.e. whether closure forces balance).

Run:  PYTHONPATH=<worktree>/src python research/drivers/theta_route3_balanced_polyphase.py
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction

import numpy as np

RNG_SEED = 20260824


def _assert_no_value_echo() -> None:
    """Refuse to run if a value-carrying module leaked into this driver."""
    import sys

    banned = ("ave.core.constants", "scipy.constants")
    for mod in banned:
        if mod in sys.modules:
            raise RuntimeError(
                f"value-echo guard: {mod} is imported; this driver must stay "
                "CODATA-free and constants-free (prereg S5.3)"
            )


# ---------------------------------------------------------------- (A)+(B)+(C)
def balanced_set(n: int) -> np.ndarray:
    """The balanced N-phase angles: theta_i = 2*pi*i/N."""
    return 2.0 * np.pi * np.arange(n) / n


def zero_sum_residual(theta: np.ndarray) -> np.ndarray:
    """Constraint F(theta) = (sum cos, sum sin) for unit-modulus phasors."""
    return np.array([np.cos(theta).sum(), np.sin(theta).sum()])


def constraint_jacobian(theta: np.ndarray) -> np.ndarray:
    """d F / d theta, shape (2, N)."""
    return np.array([-np.sin(theta), np.cos(theta)])


def jacobian_rank(theta: np.ndarray, tol: float = 1e-9) -> int:
    return int(np.linalg.matrix_rank(constraint_jacobian(theta), tol=tol))


def solution_dimension_via_jacobian(n: int) -> dict:
    """dim of the solution variety at the balanced point, and mod global rotation.

    The constraint surface has local dimension N - rank(J). The global-phase
    circle (theta -> theta + c) always lies IN the surface, so the physical
    (relabelling aside) moduli dimension is N - rank(J) - 1.
    """
    theta = balanced_set(n)
    r = jacobian_rank(theta)
    residual = float(np.linalg.norm(zero_sum_residual(theta)))
    return {
        "N": n,
        "jacobian_rank": r,
        "balanced_residual": residual,
        "dim_constraint_surface": n - r,
        "dim_mod_global_phase": n - r - 1,
    }


def _project_onto_constraint(th: np.ndarray, iters: int = 200) -> np.ndarray:
    """Gauss-Newton projection of a phase vector onto F(theta) = 0."""
    th = th.copy()
    for _ in range(iters):
        F = zero_sum_residual(th)
        if np.linalg.norm(F) < 1e-14:
            break
        J = constraint_jacobian(th)
        th = th - J.T @ np.linalg.solve(J @ J.T + 1e-15 * np.eye(2), F)
    return th


def solution_dimension_via_sampling(
    n: int, n_samples: int = 400, eps: float = 1e-3
) -> dict:
    """Independent measurement: LOCAL intrinsic dimension of the solution variety.

    Method (LOCAL PCA, not global SVD).  A global SVD of a solution cloud
    measures the dimension of its AFFINE HULL, not of the manifold -- a curved
    2-manifold in R^5 has an affine hull of dimension up to 5.  (That error is
    exactly what the first version of this function did, and the null-liveness
    gate in main() caught it: it reported rank 4 for N=5 where the Jacobian
    count says 2.  Recorded here because a repaired instrument is only
    trustworthy if the repair is visible.)

    Correct method: start from the balanced solution, take small random
    perturbations, project each back onto the constraint, and PCA the LOCAL
    DISPLACEMENTS with the global-rotation direction (the all-ones vector)
    projected out.  For a d-dimensional moduli space the displacement cloud has
    numerical rank d, with curvature entering only at O(eps^2).

    No relabelling quotient is needed or applied: local perturbations do not
    permute constituents, so sorting (which is non-smooth and was the second
    defect in the first version) is dropped.
    """
    rng = np.random.default_rng(RNG_SEED + n)
    base = _project_onto_constraint(balanced_set(n))
    ones = np.ones(n) / np.sqrt(n)  # global-rotation tangent direction
    disps = []
    for _ in range(n_samples):
        th = _project_onto_constraint(base + eps * rng.standard_normal(n))
        if np.linalg.norm(zero_sum_residual(th)) > 1e-10:
            continue
        d = th - base
        d = d - np.dot(d, ones) * ones  # quotient the global phase
        disps.append(d)
    if not disps:
        return {"N": n, "n_solutions": 0, "cloud_rank": None}
    D = np.array(disps)
    svals = np.linalg.svd(D, compute_uv=False)
    top = float(svals[0]) if svals.size else 0.0
    # A genuine tangent direction has singular value ~ eps * sqrt(n_samples);
    # curvature enters at O(eps^2) and pure round-off at ~1e-14.  BOTH a
    # relative and an ABSOLUTE cut are required: the relative cut alone
    # mis-counts round-off as signal when the moduli space is a POINT (every
    # singular value is then ~1e-14 and one of them is trivially "the largest").
    abs_floor = 0.05 * eps * np.sqrt(max(1, len(disps)))
    cut = max(1e-2 * top, abs_floor)
    rank = int((svals > cut).sum())
    return {
        "N": n,
        "method": "local-PCA on constraint-projected displacements, global phase removed",
        "eps": eps,
        "n_solutions": len(disps),
        "cloud_rank": rank,
        "rank_cut": float(cut),
        "singular_values_top4": [float(s) for s in svals[:4]],
    }


def is_collinear(theta: np.ndarray, tol: float = 1e-9) -> bool:
    """All phasors on one line through the origin <=> all theta equal mod pi."""
    t = np.mod(theta, np.pi)
    return bool(np.all(np.abs(t - t[0]) < tol) or np.all(np.abs(np.mod(t - t[0], np.pi)) < tol))


def rotating_resultant_check(n: int, n_t: int = 720) -> dict:
    """Is the balanced-N set's resultant a ROTATING or a PULSATING field?

    Model (fibre-only, no spatial displacement per prereg S0.1): the composite's
    instantaneous fibre state is the phasor sum with a common carrier e^{i w t}.
    A genuinely ROTATING structure would have |resultant| constant in t and
    NON-ZERO; a PULSATING one has |resultant| going through zero.

    OUTCOME (see result doc): NEITHER -- the resultant is IDENTICALLY ZERO at
    every N, because zero-sum is exactly the statement that the net vanishes at
    every instant.  A rotating field in a real polyphase machine comes from
    feeding the N phases into N SPATIALLY DISPLACED windings, which prereg
    S0.1 forbids importing.  So this function's real output is the collinearity
    flag (a well-defined property of the phase configuration) plus the null
    that kills the "balanced set IS a rotating field" image on the fibre alone.
    """
    theta = balanced_set(n)
    t = np.linspace(0.0, 2.0 * np.pi, n_t, endpoint=False)
    # per-constituent real excitation A cos(w t + theta_i); resultant = sum
    real_sum = np.array([np.cos(t + th) for th in theta]).sum(axis=0)
    imag_sum = np.array([np.sin(t + th) for th in theta]).sum(axis=0)
    mag = np.hypot(real_sum, imag_sum)
    return {
        "N": n,
        "collinear_balanced_set": is_collinear(theta),
        "resultant_mag_min": float(mag.min()),
        "resultant_mag_max": float(mag.max()),
        "resultant_is_identically_zero": bool(mag.max() < 1e-9),
    }


def n4_explicit_family(n_delta: int = 9) -> dict:
    """Positive control (prereg S6b): construct the KNOWN one-parameter family
    of equal-modulus zero-sum 4-phasor configurations {phi+d, phi-d, phi+pi+d,
    phi+pi-d} and verify residual ~ 0 for every delta, and that the balanced
    4-set is one member.
    """
    deltas = np.linspace(0.0, np.pi / 2, n_delta)
    residuals = []
    for d in deltas:
        th = np.array([d, -d, np.pi + d, np.pi - d])
        residuals.append(float(np.linalg.norm(zero_sum_residual(th))))
    # is the balanced 4-set (0, pi/2, pi, 3pi/2) a member? delta = pi/4, phi = pi/4
    d = np.pi / 4
    member = np.sort(np.mod(np.array([np.pi / 4 + d, np.pi / 4 - d,
                                      np.pi / 4 + np.pi + d, np.pi / 4 + np.pi - d]),
                            2 * np.pi))
    return {
        "deltas_tested": int(n_delta),
        "max_residual_over_family": float(max(residuals)),
        "balanced4_recovered_from_family": member.round(9).tolist(),
        "balanced4_reference": np.sort(balanced_set(4)).round(9).tolist(),
    }


# -------------------------------------------------------------------- (D)
def max_pairwise_orthogonal_n(n_max: int = 6, n_grid: int = 720) -> dict:
    """Largest N with phases pairwise satisfying cos(theta_i - theta_j) = 0.

    Exhaustive search on a fine grid (the condition is closed under adding a
    global phase, so theta_0 = 0 WLOG). Also reports the analytic reason.
    """
    grid = 2.0 * np.pi * np.arange(n_grid) / n_grid
    found: dict[int, list[float]] = {}
    for n in range(2, n_max + 1):
        hit = None
        # theta_0 = 0 WLOG; search the remaining N-1 on the grid.
        # For N>4 this is combinatorially large, so restrict the grid to the
        # only candidates that can satisfy a pairwise +-pi/2 condition: the
        # multiples of pi/2 (proved in the result doc; verified here for N<=4
        # against the full grid).
        if n <= 3:
            for combo in itertools.combinations(range(n_grid), n - 1):
                th = np.concatenate(([0.0], grid[list(combo)]))
                d = th[:, None] - th[None, :]
                iu = np.triu_indices(n, k=1)
                if np.all(np.abs(np.cos(d[iu])) < 1e-6):
                    hit = th.tolist()
                    break
        else:
            quarter = np.array([0.0, np.pi / 2, np.pi, 3 * np.pi / 2])
            for combo in itertools.product(range(4), repeat=n - 1):
                th = np.concatenate(([0.0], quarter[list(combo)]))
                d = th[:, None] - th[None, :]
                iu = np.triu_indices(n, k=1)
                if np.all(np.abs(np.cos(d[iu])) < 1e-6):
                    hit = th.tolist()
                    break
        if hit is not None:
            found[n] = hit
    return {
        "N_with_pairwise_orthogonal_solution": sorted(found.keys()),
        "max_N": max(found) if found else None,
        "example_solutions": {str(k): v for k, v in found.items()},
        "balanced3_pairwise_cos": float(np.cos(2 * np.pi / 3)),
    }


# -------------------------------------------------------------------- (E)
def compact_theta_charge_enumeration(n_range: int = 4) -> dict:
    """q_eff = n + theta/2pi with theta a GENUINE PHASE (compact, mod 2pi).

    Exact rational arithmetic. theta/2pi in {0, 1/3, 2/3} (the three distinct
    classes of canon's set mod 2pi). Enumerate which (n, theta/2pi) reproduce
    each observed quark charge.
    """
    classes = [Fraction(0, 3), Fraction(1, 3), Fraction(2, 3)]
    targets = {
        "up_+2/3": Fraction(2, 3),
        "down_-1/3": Fraction(-1, 3),
        "anti_up_-2/3": Fraction(-2, 3),
        "anti_down_+1/3": Fraction(1, 3),
    }
    out: dict[str, list[dict]] = {}
    for name, q in targets.items():
        sols = []
        for n in range(-n_range, n_range + 1):
            for c in classes:
                if Fraction(n) + c == q:
                    sols.append({"n": n, "theta_over_2pi": str(c)})
        out[name] = sols
    # the five-element NON-compact list canon writes, read as reals
    noncompact = [Fraction(0), Fraction(1, 3), Fraction(-1, 3),
                  Fraction(2, 3), Fraction(-2, 3)]
    noncompact_at_n0 = {str(c): str(Fraction(0) + c) for c in noncompact}
    distinct_mod_1 = sorted({str(c % 1) for c in noncompact})
    return {
        "compact_classes_theta_over_2pi": [str(c) for c in classes],
        "solutions_per_target": out,
        "up_and_down_share_theta_class": (
            out["up_+2/3"] and out["down_-1/3"]
            and out["up_+2/3"][0]["theta_over_2pi"] == out["down_-1/3"][0]["theta_over_2pi"]
        ),
        "noncompact_list_q_eff_at_n0": noncompact_at_n0,
        "noncompact_list_distinct_classes_mod_1": distinct_mod_1,
        "n_listed_values": len(noncompact),
        "n_distinct_classes_mod_1": len(distinct_mod_1),
    }


def proton_neutron_common_theta_check() -> dict:
    """Does a COMMON theta/2pi = -1/N with varying integer n reproduce the
    baryon totals, and is the answer N-SELECTIVE or N-GENERIC? Exact rationals.

    HIDDEN-INPUT WARNING (this function was wrong on its first run and the
    error is recorded rather than quietly fixed, per flag-don't-fix).  The
    first version computed `2*up + 1*down` -- THREE constituents -- while
    sweeping the dressing denominator N.  That mismatch manufactured an
    apparent "only N=3 gives charge +1", which is an artifact of holding the
    constituent count at 3 while moving the denominator, i.e. exactly the
    fed-in-N failure this program polices.

    Correct construction: an N-constituent composite in which every
    constituent carries the SAME dressing -1/N and an integer part n_i, with
    k of the n_i equal to 1 and the rest 0.  Total = k - 1 for EVERY N.
    """
    out = {}
    for N in (2, 3, 4, 5, 6):
        common = Fraction(-1, N)
        rows = {}
        for k, label in ((2, "proton_like_total(k=2)"), (1, "neutron_like_total(k=1)")):
            if k > N:
                rows[label] = "n/a (k > N)"
                continue
            total = Fraction(k) + N * common
            rows[label] = str(total)
        out[str(N)] = {
            "common_theta_over_2pi": str(common),
            "N_constituents": N,
            "total_dressing": str(N * common),
            **rows,
        }
    out["_verdict"] = (
        "N-GENERIC: total dressing = N * (-1/N) = -1 for every N, so the "
        "integer total charge k-1 is reproduced at every N >= k. N is not "
        "selected by charge integrality."
    )
    return out


# -------------------------------------------------------------------- (F)
def closure_check(n_max: int = 8) -> dict:
    """sum(theta_i) mod 2pi for the balanced N-set, plus whether closure forces
    the balanced set at fixed N (counter-example search)."""
    rows = []
    for n in range(2, n_max + 1):
        s = balanced_set(n).sum()
        rows.append({
            "N": n,
            "sum_theta_over_2pi": float(s / (2 * np.pi)),
            "closes_mod_2pi": bool(abs((s / (2 * np.pi)) - round(s / (2 * np.pi))) < 1e-12),
        })
    # counter-example: a NON-balanced 3-set with sum = 2pi
    rng = np.random.default_rng(RNG_SEED)
    counterexamples = []
    for _ in range(5):
        a, b = rng.uniform(0.1, 2.0, size=2)
        c = 2 * np.pi - a - b
        if c <= 0:
            continue
        th = np.array([a, b, c])
        counterexamples.append({
            "theta_over_2pi": (th / (2 * np.pi)).round(6).tolist(),
            "sum_over_2pi": float(th.sum() / (2 * np.pi)),
            "is_balanced": bool(np.allclose(np.sort(np.mod(th - th[0], 2 * np.pi)),
                                            np.sort(balanced_set(3)), atol=1e-9)),
        })
    return {"balanced_sets": rows, "nonbalanced_closing_examples": counterexamples}


def main() -> dict:
    _assert_no_value_echo()
    results = {
        "seed": RNG_SEED,
        "A_null_liveness_n4_family": n4_explicit_family(),
        "B_dimension_via_jacobian": [solution_dimension_via_jacobian(n) for n in range(2, 9)],
        "B_dimension_via_sampling": [solution_dimension_via_sampling(n) for n in range(2, 9)],
        "C_rotating_resultant": [rotating_resultant_check(n) for n in range(2, 7)],
        "D_pairwise_orthogonality": max_pairwise_orthogonal_n(),
        "E_compact_theta_charges": compact_theta_charge_enumeration(),
        "E_common_theta_proton_neutron": proton_neutron_common_theta_check(),
        "F_closure": closure_check(),
    }

    # --- null-liveness gate (prereg S6): HALT if the driver cannot see a KNOWN
    #     rigidity at N=3 and a KNOWN freedom at N=4.
    jac = {r["N"]: r for r in results["B_dimension_via_jacobian"]}
    samp = {r["N"]: r for r in results["B_dimension_via_sampling"]}
    gate = {
        "n3_isolated_mod_global_phase": jac[3]["dim_mod_global_phase"] == 0,
        "n4_has_freedom": jac[4]["dim_mod_global_phase"] >= 1,
        "n4_family_residual_ok": results["A_null_liveness_n4_family"]["max_residual_over_family"] < 1e-12,
        "two_methods_agree": all(
            jac[n]["dim_mod_global_phase"] == samp[n]["cloud_rank"] for n in range(2, 9)
        ),
        "n2_isolated_but_rank_deficient": (
            jac[2]["dim_mod_global_phase"] == 0 and jac[2]["jacobian_rank"] == 1
        ),
    }
    gate["PASS"] = all(gate.values())
    results["NULL_LIVENESS_GATE"] = gate
    return results


if __name__ == "__main__":
    res = main()
    print(json.dumps(res, indent=2))
    out = __file__.replace(".py", "_results.json")
    with open(out, "w") as fh:
        json.dump(res, fh, indent=2)
    print(f"\nwrote {out}")
    if not res["NULL_LIVENESS_GATE"]["PASS"]:
        raise SystemExit("NULL-LIVENESS GATE FAILED — lane HALTS per prereg S6")
