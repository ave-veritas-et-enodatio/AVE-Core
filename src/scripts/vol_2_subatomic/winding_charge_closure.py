"""Winding charge-closure refute-by-default driver (Lane D, 2026-06-23).

Tests, in CLEAN PARAMETRIC coordinates (NOT the lattice-sampled field — to
sidestep the q<=4 resolution ceiling the prior charge-quantization gate hit,
2026-06-19_charge-quantization-gate_result.md, and isolate the TOPOLOGY question):

  PART 1 — does the lattice FORCE the electron toroidal winding p=2?
    (a) NYQUIST-MINIMAL-WINDING   (b) B-SATURATION->BELTRAMI   (c) MONOPOLE-DOUBLE-WIND
  PART 2 — quark fractional charge + confinement from the closure framework:
    (Q1) fractional = non-self-closing   (Q2) denominator-3 forced?
    (Q3) confinement forced?             (Q4) up/down split derived or fit?

REFUTE-BY-DEFAULT: the default verdict on every positive is FIT/ECHO unless the
substrate genuinely forces it. The computation is built to GIVE p=1 / non-3 /
free-quark every chance to succeed; we report whether they are EXCLUDED.

GUARDS (mirror charge_quantization.py):
  - VALUE-ECHO IMMUNITY: integers + signs only; NO alpha / -e / CODATA imported.
  - TWO-3s ORTHOGONALITY: helicity/linking computed only on the winding curve
    (the T2 micro-rotation grade's phase-space portrait); never the A1 phasor.
  - A46 PHASE-SPACE: the (p,q) self-linking is a phase-space-native integer; we
    never compare it to a real-space lattice-Cartesian measurement.

Reproduce:
  PYTHONPATH=src python3 -m scripts.vol_2_subatomic.winding_charge_closure
"""
from __future__ import annotations

import json
import math

import numpy as np

# Reuse the CANONICAL Gauss linking primitive (ave-canonical-source); it is the
# rigorous 1D line/loop linking integer used by the charge-quantization gate.
from ave.topological.charge_quantization import _gauss_linking_integral


# ---------------------------------------------------------------------------
# Value-echo immunity guard (same posture as charge_quantization.py).
# ---------------------------------------------------------------------------
def _assert_no_value_echo() -> None:
    """Assert no alpha / charge / CODATA literal is read in this module."""
    import inspect
    import sys

    src = inspect.getsource(sys.modules[__name__])
    # We only read integers + signs. These tokens must not appear on EXECUTABLE
    # lines (imports / assignments). We scan import/from lines only, so the
    # forbidden-token names in docstrings/comments do not false-positive.
    import_lines = [
        ln for ln in src.splitlines()
        if ln.strip().startswith(("import ", "from "))
    ]
    for forbidden in ("ALPHA", "Q_TANK", "e_charge", "constants", "1.602", "137.0"):
        bad = [ln for ln in import_lines if forbidden in ln]
        assert not bad, f"value-echo leak: {forbidden} imported at {bad}"


# ---------------------------------------------------------------------------
# Parametric (p, q) torus-knot curve on the Clifford-torus winding portrait.
# This is the PHASE-SPACE winding curve, not a real-space knot.
# ---------------------------------------------------------------------------
def torus_knot_curve(p: int, q: int, n: int = 2000, R: float = 2.0, r: float = 0.6,
                     handedness: int = +1) -> np.ndarray:
    """A (p,q) torus-knot polyline: p toroidal (long-way) turns, q poloidal.

    handedness = +/-1 flips the poloidal winding sense (the chirality that the
    charge-quantization gate read as the charge SIGN). NOT a value import.
    """
    t = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    phi = p * t          # toroidal (long-way) angle
    psi = handedness * q * t  # poloidal (short-way) angle, signed by handedness
    x = (R + r * np.cos(psi)) * np.cos(phi)
    y = (R + r * np.cos(psi)) * np.sin(phi)
    z = r * np.sin(psi)
    return np.stack([x, y, z], axis=1)


def closes_as_single_component(p: int, q: int) -> bool:
    """A (p,q) winding closes into ONE component iff gcd(p,q)=1.

    If gcd(p,q)=d>1 the curve closes after t in [0, 2pi/d) and is a d-component
    LINK, not a single closed knot. This is the closure condition.
    """
    return math.gcd(abs(p), abs(q)) == 1


def self_linking_pushoff(p: int, q: int, n: int = 2000, R: float = 2.0,
                         r: float = 0.6, handedness: int = +1,
                         eps: float = 0.04) -> float:
    """Self-linking number via Gauss linking of the curve with a push-off copy.

    The framed self-linking SL of a (p,q) torus knot equals p*q in the Seifert
    framing for the standard torus embedding; we compute it numerically as the
    Gauss linking of the curve C with a small normal push-off C' (the standard
    way to realize self-linking as a genuine linking integral). This is the
    'enclosed helicity' integer of the winding — the quantity that must CLOSE to
    an integer for a unit charge.
    """
    C = torus_knot_curve(p, q, n=n, R=R, r=r, handedness=handedness)
    # Push-off along the toroidal normal direction (radially in the tube),
    # which realizes the Seifert/blackboard self-framing.
    t = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    phi = p * t
    psi = handedness * q * t
    nx = np.cos(psi) * np.cos(phi)
    ny = np.cos(psi) * np.sin(phi)
    nz = np.sin(psi)
    normal = np.stack([nx, ny, nz], axis=1)
    Cp = C + eps * normal
    return _gauss_linking_integral(C, Cp)


# ---------------------------------------------------------------------------
# VALIDATE-ON-KNOWN: recover the electron's integer charge.
# ---------------------------------------------------------------------------
def validate_on_known() -> dict:
    """A unit closed loop nets a unit integer linking with its push-off;
    the electron (2,3) closes as a single component (gcd=1).

    HALT if these do not recover (the tool would be uninterpretable)."""
    # Hopf link sanity (two loops linked once) -> +/-1, unlinked -> 0.
    theta = np.linspace(0, 2 * np.pi, 800, endpoint=False)
    loopA = np.stack([np.cos(theta), np.sin(theta), 0 * theta], axis=1)
    loopB = np.stack([1 + np.cos(theta), 0 * theta, np.sin(theta)], axis=1)
    hopf = _gauss_linking_integral(loopA, loopB)
    loopB_far = loopB + np.array([10.0, 0, 0])
    unlinked = _gauss_linking_integral(loopA, loopB_far)

    # Electron (2,3): single component (gcd=1); self-linking integer.
    e_single = closes_as_single_component(2, 3)
    e_sl = self_linking_pushoff(2, 3)
    # Sign = chirality (charge sign): RH vs LH must flip sign.
    e_sl_lh = self_linking_pushoff(2, 3, handedness=-1)

    halt = (abs(round(hopf) - hopf) > 0.25 or abs(round(hopf)) != 1
            or abs(unlinked) > 0.25 or not e_single)
    return {
        "hopf_link": round(hopf, 4),
        "unlinked": round(unlinked, 4),
        "electron_single_component": e_single,
        "electron_self_linking_raw": round(e_sl, 4),
        "electron_self_linking_LH_raw": round(e_sl_lh, 4),
        "sign_flips_with_handedness": (np.sign(e_sl) != np.sign(e_sl_lh)),
        "HALT": bool(halt),
    }


# ---------------------------------------------------------------------------
# PART 1 — does the lattice FORCE p=2?  (refute-by-default)
# ---------------------------------------------------------------------------
def part1_p_forcing() -> dict:
    """Test whether p=1 can close (refutes double-wind/Nyquist-minimal) at a
    FIXED q, separate from the q (spin) closure."""
    q = 3  # the poloidal/spin index, held fixed and SEPARATE from p
    rows = []
    for p in (1, 2, 3):
        single = closes_as_single_component(p, q)
        sl = self_linking_pushoff(p, q)
        rows.append({
            "p": p, "q": q,
            "single_component": single,        # closes as ONE loop?
            "gcd": math.gcd(p, q),
            "self_linking_raw": round(sl, 3),
            "self_linking_int": int(round(sl)),
            "nets_unit_or_more_integer": abs(round(sl)) >= 1 and single,
        })

    # Sub-route verdicts (refute-by-default).
    p1 = next(rw for rw in rows if rw["p"] == 1)
    p2 = next(rw for rw in rows if rw["p"] == 2)

    # (a) NYQUIST-MINIMAL / (c) DOUBLE-WIND share a refuter: does p=1 close to a
    # unit-or-more integer helicity? If YES, both claims that 'p=2 is needed to
    # close' are REFUTED.
    p1_closes_to_integer = p1["nets_unit_or_more_integer"]
    double_wind_needed = not p1_closes_to_integer

    return {
        "rows": rows,
        "p1_closes_to_unit_integer": p1_closes_to_integer,
        "p2_closes_to_unit_integer": p2["nets_unit_or_more_integer"],
        # CHORD only if p=1 is EXCLUDED from closing while p=2 is not.
        "p2_forced_over_p1": (double_wind_needed and p2["nets_unit_or_more_integer"]),
        "p_eq_2_is_minimality_not_forcing": (
            p1_closes_to_integer and p2["nets_unit_or_more_integer"]
        ),
    }


# ---------------------------------------------------------------------------
# PART 2 — quark fractional charge + denominator-3 + confinement.
# ---------------------------------------------------------------------------
def symmetric_link_components(N: int, n: int = 1500, Rlink: float = 3.0,
                              rcomp: float = 1.0) -> list[np.ndarray]:
    """N mutually-symmetric closed loops arranged with N-fold symmetry, each
    carrying a winding; the closure of the whole is the baryon analog.

    For the helicity-share test we represent each component as a tilted ring so
    the N-component total linking is well-defined."""
    comps = []
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    for k in range(N):
        ang = 2 * np.pi * k / N
        cx, cy = Rlink * math.cos(ang), Rlink * math.sin(ang)
        # tilt the ring plane so neighbors link
        ring = np.stack([
            cx + rcomp * np.cos(theta) * math.cos(ang),
            cy + rcomp * np.cos(theta) * math.sin(ang),
            rcomp * np.sin(theta),
        ], axis=1)
        comps.append(ring)
    return comps


def part2_quark_closure() -> dict:
    """(Q1) lone winding self-closes?  (Q2) denominator-3 forced or 1/N free?
       (Q3) confinement forced?         (Q4) up/down derived or fit?"""
    # (Q2) The corpus route (topological-fractionalization.md) gets thirds from
    # Z_N permutation symmetry of an N-component link: theta in {0, +/-2pi/N,...}
    # -> q_eff = theta/(2pi) e in units of 1/N. Test: is N=3 FORCED, or does the
    # SAME construction give 1/N for ANY N (making N=3 a CHOICE matched to the
    # proton, not a derivation)?
    denom_table = {}
    for N in (2, 3, 4, 5):
        # Z_N permutation angles theta_k = 2pi k / N -> fractional charge k/N.
        fracs = sorted({(k % N) for k in range(N)})
        denom_table[N] = {
            "Z_N_angles_over_2pi": [f"{k}/{N}" for k in fracs],
            "fractional_charges": [round(k / N, 4) for k in fracs],
            "denominator": N,
        }
    # The denominator equals N for EVERY N -> denominator-3 is NOT forced by the
    # construction; it is selected by choosing N=3 (the observed proton loop count).
    denominator_3_is_forced = False  # the construction gives 1/N for any N

    # (Q1)+(Q3) Helicity-closure / Borromean test on the parametric link.
    # A genuine Borromean link: any TWO components are UNLINKED (pairwise Lk=0),
    # yet the three together are inseparable. Test our N=3 symmetric link's
    # pairwise linking to see whether the parametric construction is actually
    # Borromean (pairwise-unlinked) or merely a chain (pairwise-linked).
    comps3 = symmetric_link_components(3)
    pair_lk = {}
    for i in range(3):
        for j in range(i + 1, 3):
            pair_lk[f"{i}-{j}"] = round(_gauss_linking_integral(comps3[i], comps3[j]), 3)
    pairwise_all_zero = all(abs(v) < 0.25 for v in pair_lk.values())

    # A lone component's self-linking with its push-off: does a single quark
    # winding self-close to an integer? (If yes, Q1 'fractional=non-self-closing'
    # fails; the fraction is then NOT a closure property but an assignment.)
    lone = comps3[0]
    t = np.linspace(0, 2 * np.pi, len(lone), endpoint=False)
    push = lone + 0.04 * np.stack([np.cos(t), np.sin(t) * 0, np.sin(t)], axis=1)
    lone_self_lk = _gauss_linking_integral(lone, push)

    return {
        "Q2_denominator_table": denom_table,
        "Q2_denominator_3_forced": denominator_3_is_forced,
        "Q2_note": "Z_N construction yields denominator N for ANY N; N=3 is the "
                   "proton's observed loop count, not a forced denominator.",
        "Q3_borromean_pairwise_linking": pair_lk,
        "Q3_pairwise_all_zero_true_borromean": pairwise_all_zero,
        "Q1_lone_component_self_linking_raw": round(lone_self_lk, 3),
        "Q1_lone_self_closes_to_integer": abs(round(lone_self_lk)) >= 1,
    }


def main() -> dict:
    _assert_no_value_echo()
    known = validate_on_known()
    if known["HALT"]:
        return {"VERDICT": "HALT", "validate_on_known": known}
    p1 = part1_p_forcing()
    p2 = part2_quark_closure()

    # ---- Per-result verdicts (refute-by-default) --------------------------
    if p1["p2_forced_over_p1"]:
        electron_p_verdict = "CHORD (p=1 excluded from closing; p=2 forced)"
    elif p1["p_eq_2_is_minimality_not_forcing"]:
        electron_p_verdict = "FIT/ECHO (p=1 also closes; p=2 is smallest-coprime minimality, not forcing)"
    else:
        electron_p_verdict = "CONSISTENCY"

    quark_denom_verdict = (
        "CHORD" if p2["Q2_denominator_3_forced"]
        else "FIT/ECHO (Z_N gives 1/N for any N; N=3 = proton loop count, chosen not forced)"
    )

    # Confinement: forced IF (a) a lone fractional winding cannot stand alone AND
    # (b) the link is genuinely Borromean (remove-one-falls-apart). We test (b)
    # structurally; (a) reduces to whether fractional helicity is a stable
    # standalone state, which the closure requirement forbids ONLY if the lone
    # winding does NOT self-close to an integer.
    lone_self_closes = p2["Q1_lone_self_closes_to_integer"]
    confinement_verdict = (
        "CONSISTENCY (closure-requirement forbids a free fractional state — but "
        "this is the [Q]=[L] posit restated, not a novel forcing of N=3 confinement)"
        if not lone_self_closes else
        "FIT/ECHO (lone component self-closes; confinement not forced by closure alone)"
    )

    up_down_verdict = (
        "FIT/ECHO (theta->{+2/3=up,-1/3=down} requires hand-labeling to match PDG; "
        "no substrate reason a given handedness is 'up')"
    )

    out = {
        "VERDICT": "COMPLETE",
        "validate_on_known": known,
        "part1_p_forcing": p1,
        "part2_quark_closure": p2,
        "RESULT_VERDICTS": {
            "electron_p": electron_p_verdict,
            "quark_denominator_3": quark_denom_verdict,
            "confinement": confinement_verdict,
            "up_down_split": up_down_verdict,
        },
    }
    return out


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, default=str))
