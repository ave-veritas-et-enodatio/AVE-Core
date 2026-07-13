"""T1 — the atom-Q cascade gate: is the atom's wall loss-Q distinct, or an endpoint echo?

FROZEN prereg (gated on): research/2026-07-13_t1-atom-q-cascade-gate_prereg_FROZEN.md
(freeze commit pushed BEFORE this file — git ordering = freeze proof).
Brief (binding): _orchestration/2026-07-13_t1-atom-q-cascade-gate-handoff.md

THE GATE (verbatim from the brief). The atom is canonically "a wave trapped between its
own reflections in a well made of mismatch". This driver asks the cheapest discriminating
question the cascade-filter framing owes: does the substrate produce a DISTINCT intermediate
loss-Q for the atom rung (~1e7), or does it collapse onto a ladder ENDPOINT (electron
intrinsic Q->inf, loaded alpha^-1=137, BH QNM Q~few) — in which case "cascade filter" is the
homogeneous vacuum line relabeled, a vocabulary echo?

MODE: derivation-from-canon + numerical consistency driver. NOT engine-fire. NO new primitive.
The instrument evaluates a LOSS channel on x42's OWN de Broglie dispersion
(x42.local_wavenumber_sq), which x42 rendered but never used to compute a loss-Q.

WHICH-Q (declared in the prereg, binding): Q_wall(atom) = the loss-Q of the bound atomic
standing mode against its own graded Coulomb-dress turning-point walls = the cavity's
round-trip INSERTION LOSS of the trapped bulk-modulus (Z_bulk) matter-wave. It is NONE of the
>=4 electron-scale Q homonyms (loaded 137 / intrinsic inf / cold-cage 30.8 / radiation-floor
29.98 / per-mode ell), and NOT the transverse-EM radiative-decay Q.

SUBSTRATE-NATIVE (Ckpt-10, binding): the loss is rendered as a BOUNDARY TRANSMISSION T through
the wall surface (a Gamow/WKB reflection coefficient), NEVER as a bulk absorber term. The wall
is a reactive reflecting boundary (imaginary impedance -> |Gamma|=1, no Re(Z)). Coordinate
register = transmission/impedance plane (matched to the corpus Gamma/Z(r) claim), not
real-space localization.

RAIL (binding): NEVER seed or normalize from alpha^-1=137.036 (the electron tank's LOADED Q,
a Class-B echo). Leg A (the wall-Q) is alpha-INDEPENDENT by construction; the well scale
(a0, Ry) is x42-identical canonical geometry, not a Q-seed. Leg C (radiative diagnostic) uses
alpha ONLY to CLASSIFY the observed ~1e7 rung as the alpha-echo (the opposite of manufacturing
a distinct value); it is walled off from Legs A/B and is explicitly NOT a bin-(i) candidate.

Legs:
  A  wall_leakage_Q       -- Gamow round-trip leakage through the OUTER Coulomb wall (alpha-free).
  B  positive_control_Q   -- the SAME integrator on a planted FINITE barrier (proves the gate can
                             FIRE bin (i): a finite intermediate Q IS reportable; the atom's inf
                             is a physics verdict, not an instrument that cannot fire).
  C  radiative_diagnostic -- quarantined classical Lorentz Q_rad = 4*alpha^-3 (transverse-EM
                             Z_EM port; a DIFFERENT sector x42's longitudinal Hermitian
                             eigencavity does not express; alpha-sourced).

CONSTANTS: every value from ave.core.constants. Zero hard-coded physics numbers (the two frozen
control parameters -- barrier width 3 a0, height 4 Ry -- are prereg-declared synthetic knobs,
labelled as such).
"""

from __future__ import annotations

import math

import numpy as np

from ave.core.constants import A_0, ALPHA, C_0, HBAR, M_E, RY_EV, e_charge

# x42's OWN dispersion -- the SAME de Broglie k^2(r) it uses for the spectrum. Importing (not
# re-implementing) machine-guarantees the loss channel is evaluated on the identical profile.
from scripts.vol_2_subatomic.x42_atomic_eigencavity import M_R_H, local_wavenumber_sq

RY_J = RY_EV * e_charge  # Rydberg in Joules (canonical well SCALE, x42-identical; NOT a Q-seed)

# Frozen bin thresholds (from the prereg -- no post-run edits, Rule 11)
BIN_I_LO, BIN_I_HI = 1e5, 1e9  # (i) DISTINCT: finite alpha-free Q_wall in this window
BIN_II_HI = 1e12  # (ii) NO-DISTINCT: Q_wall >= this = collapse toward intrinsic endpoint (inf)
BIN_II_LO = 1e3  # (ii) NO-DISTINCT: Q_wall <= this = collapse toward loaded/cold-cage endpoint


# ---------------------------------------------------------------------------
# Bound-level energy = the canonical well GEOMETRY (x42-identical; NOT a Q-seed)
# ---------------------------------------------------------------------------
def bound_energy_J(Z: int, n: int, m_probe: float = M_E) -> float:
    """E_n = -(m_probe/m_e) Z^2 Ry / n^2  in Joules.

    This is the well's operating point (the eigenvalue x42 reproduces to -0.000%), used ONLY to
    place the turning point and set the evanescent decay -- the canonical GEOMETRY. The wall-Q
    that comes out is independent of this scale's alpha content (a lossless wall reflects
    perfectly whatever alpha, Z, n are).
    """
    return -(m_probe / M_E) * Z**2 * RY_J / n**2


# ---------------------------------------------------------------------------
# The SHARED Gamow integrator (Legs A and B both call this identical pipeline)
# ---------------------------------------------------------------------------
def gamow_Q(neg_k2, r_a: float, r_b: float, n_grid: int = 200_000):
    """Round-trip leakage Q through a forbidden region [r_a, r_b], as a BOUNDARY transmission.

        I     = INTEGRAL_{r_a}^{r_b} sqrt( max(-k2(r), 0) ) dr      (evanescent decay integral)
        T     = exp(-2 I)                                           (barrier transmission = leak)
        Q     = 2*pi / T                                            (round-trip-leak quality)

    `neg_k2(r)` returns -k^2(r) = +|k|^2 in the forbidden region (>0), <=0 where propagating.
    This is a WALL (a reflecting boundary) rendered as its transmission coefficient -- NOT a bulk
    absorber (substrate Ckpt-10). Returns (I, T, Q). Q is float('inf') if T underflows to 0
    (an infinitely thick barrier -> a perfect reflector -> Q -> inf).
    """
    r = np.linspace(r_a, r_b, n_grid)
    kappa = np.sqrt(np.maximum(neg_k2(r), 0.0))
    _trapz = getattr(np, "trapezoid", None) or np.trapz  # np.trapezoid (>=2.0) else np.trapz
    integ = float(_trapz(kappa, r))
    two_i = 2.0 * integ
    if two_i > 700.0:  # exp(-700) underflows to 0.0 in float64 -> transmission is (numerically) 0
        return integ, 0.0, float("inf")
    trans = math.exp(-two_i)
    return integ, trans, (2.0 * math.pi / trans if trans > 0.0 else float("inf"))


# ---------------------------------------------------------------------------
# LEG A -- the wall insertion-loss Q of the atom, on x42's own dispersion (alpha-free)
# ---------------------------------------------------------------------------
def outer_turning_point(Z: int, n: int, ell: int = 0, m_probe: float = M_E) -> float:
    """Outermost radius where k^2(r)=0 (the classical turning point / cavity wall).

    Found as the outward + -> - sign change of x42's local_wavenumber_sq (the SAME dispersion
    that defines the cavity), bisected. For ell=0 this is analytically r_turn = 2 a0 n^2 / Z; we
    locate it numerically to stay faithful to x42's profile.
    """
    E = bound_energy_J(Z, n, m_probe)

    def k2(r):
        return local_wavenumber_sq(r, E, Z, ell, m_probe=m_probe, saturate=False)

    r_lo = A_0 * n**2 / Z  # inside the allowed region (below the analytic 2 a0 n^2/Z wall)
    while k2(r_lo) <= 0:  # ensure we start in the classically-allowed region
        r_lo *= 0.5
    r_hi = 4.0 * A_0 * n**2 / Z  # safely outside the wall (forbidden)
    while k2(r_hi) > 0:
        r_hi *= 2.0
    for _ in range(200):  # bisection to the sign change
        r_mid = 0.5 * (r_lo + r_hi)
        if k2(r_mid) > 0:
            r_lo = r_mid
        else:
            r_hi = r_mid
    return 0.5 * (r_lo + r_hi)


def wall_leakage_Q(Z: int, n: int, ell: int = 0, m_probe: float = M_E,
                   R_factors=(5, 10, 20, 50, 100)):
    """Leg A: the atom's Q_wall = round-trip leakage through the OUTER Coulomb-dress wall.

    Integrates the evanescent decay from the turning point r_turn outward to R = factor * r_turn
    for a ladder of factors, on x42's OWN dispersion. Beyond r_turn the Coulomb tail vanishes so
    -k^2(r) -> (kappa_inf)^2 = (1/(n a0))^2 (const > 0): the forbidden region extends to infinity,
    the barrier is INFINITELY THICK, so I(R) grows linearly WITHOUT BOUND and Q_wall -> inf.

    Returns a dict with the I(R) growth table, the asymptotic decay slope, and the verdict Q.
    alpha-free: the result depends on no alpha-seed (the well scale cancels out of the divergence).
    """
    E = bound_energy_J(Z, n, m_probe)
    r_turn = outer_turning_point(Z, n, ell, m_probe)

    def neg_k2(r):
        return -local_wavenumber_sq(r, E, Z, ell, m_probe=m_probe, saturate=False)

    # asymptotic evanescent decay constant, computed honestly from the state:
    # sqrt(2 m|E|)/hbar -> 1/(n a0) for the electron probe (the known hydrogenic tail).
    kappa_inf = math.sqrt(2.0 * m_probe * abs(E)) / HBAR

    rows = []
    for f in R_factors:
        R = f * r_turn
        integ, trans, q = gamow_Q(neg_k2, r_turn, R)
        rows.append({"R_over_rturn": f, "R_over_a0": R / A_0, "I": integ, "T": trans, "Q_wall": q})

    # slope of I(R) at the largest window -> should approach kappa_inf (linear, unbounded growth)
    Rs = np.array([f * r_turn for f in R_factors])
    integs = np.array([gamow_Q(neg_k2, r_turn, R)[0] for R in Rs])
    slope = float((integs[-1] - integs[-2]) / (Rs[-1] - Rs[-2]))  # dI/dR

    return {
        "Z": Z, "n": n, "l": ell, "r_turn_over_a0": r_turn / A_0,
        "kappa_inf_a0": kappa_inf * A_0, "dI_dR_a0": slope * A_0,
        "rows": rows,
        "Q_verdict": rows[-1]["Q_wall"],  # at the widest window; grows without bound -> inf
        "diverges": bool(integs[-1] > integs[0] and slope > 0.0),
    }


# ---------------------------------------------------------------------------
# LEG B -- positive control: the SAME integrator on a FINITE barrier -> FINITE Q (fireability)
# ---------------------------------------------------------------------------
def positive_control_Q(width_in_a0: float = 3.0, height_in_Ry: float = 4.0):
    """Leg B (Step 3.8a positive control): a planted FINITE-width forbidden barrier, run through
    the IDENTICAL gamow_Q pipeline, returns a FINITE Q -- proving Leg A's inf is a physics verdict
    (infinite barrier), not an instrument that cannot fire bin (i).

    A rectangular barrier: -k^2(r) = 2 m dV / hbar^2 (const) on a window of width `width_in_a0`*a0,
    with dV = `height_in_Ry`*Ry. These two numbers are prereg-declared SYNTHETIC control knobs
    (not physics constants) chosen to land Q in the bin-(i) window [1e5, 1e9]; a propagating
    channel is understood to open beyond the barrier (a quasi-bound resonance).
    """
    dV = height_in_Ry * RY_J
    w = width_in_a0 * A_0
    kappa_sq = 2.0 * M_E * dV / HBAR**2  # >0 : finite forbidden barrier

    def neg_k2(r):
        return np.full_like(np.asarray(r, dtype=float), kappa_sq)

    integ, trans, q = gamow_Q(neg_k2, 0.0, w)
    return {"width_a0": width_in_a0, "height_Ry": height_in_Ry, "I": integ, "T": trans, "Q_control": q}


# ---------------------------------------------------------------------------
# LEG C -- quarantined RADIATIVE diagnostic: Q_rad = 4 alpha^-3 (NOT a bin-(i) candidate)
# ---------------------------------------------------------------------------
def radiative_diagnostic_Q():
    """Leg C (QUARANTINED, classification-only, NOT a bin-(i) candidate).

    The classical Lorentz radiative Q of the atomic transition dipole:
        Q_rad = (3/2) m_e c^2 / (alpha * hbar*omega),   hbar*omega_Lya = (3/4) Ry = (3/8) alpha^2 m_e c^2
             => Q_rad = 4 * alpha^-3   (Lyman-alpha, oscillator strength f=1).
    This is the TRANSVERSE-EM (Z_EM) loaded/radiative port -- a DIFFERENT sector than the
    longitudinal wall, one that x42's Hermitian eigencavity does not express (bin (iii)). It is
    alpha-SOURCED (alpha^-3: two powers from the Rydberg transition scale ~alpha^2, one from the
    radiative coupling) = the electron loaded-Q echo (alpha^-1) at a higher power. Reported ONLY
    to CLASSIFY the observed ~1e7 rung as the alpha-echo; it never feeds Q_wall.
    """
    mc2 = M_E * C_0**2
    hw_Lya = 0.75 * RY_J  # E_2 - E_1 = (1 - 1/4) Ry
    Q_rad_classical = 1.5 * mc2 / (ALPHA * hw_Lya)  # == 4 * alpha^-3
    f_Lya = 0.4162  # H Lyman-alpha absorption oscillator strength (external atomic datum)
    Q_rad_QM = Q_rad_classical / f_Lya  # ~ 9.6 alpha^-3 ~ 2.5e7 = the measured rung
    return {
        "Q_rad_classical": Q_rad_classical,
        "Q_rad_times_alpha3": Q_rad_classical * ALPHA**3,  # -> 4.0 : confirms Q_rad ∝ alpha^-3
        "Q_rad_QM_with_f": Q_rad_QM,
        "alpha_inv_cubed": ALPHA**-3,
    }


# ---------------------------------------------------------------------------
# Adjudication against the frozen bins
# ---------------------------------------------------------------------------
def adjudicate(Q_wall: float, Q_control: float) -> dict:
    """Apply the frozen bins to Leg A (with Leg B as the fireability witness)."""
    control_fires_i = BIN_I_LO <= Q_control <= BIN_I_HI  # instrument CAN report a finite in-window Q
    if BIN_I_LO <= Q_wall <= BIN_I_HI:
        bin_ = "(i) DISTINCT-Q-DERIVED"
        verdict = "cascade has content at the atom rung (chord) -- Q_wall is finite, alpha-free, in-window"
    elif Q_wall >= BIN_II_HI or Q_wall == float("inf") or Q_wall <= BIN_II_LO:
        bin_ = "(ii) NO-DISTINCT-VALUE"
        verdict = ("KILL-SHAPE FIRES: Q_wall collapses onto a ladder ENDPOINT "
                   "(intrinsic Q->inf) -- the cascade-filter framing is a vocabulary echo on "
                   "this rung. Honest verb: DEMONSTRATED (a sub-threshold bound state has no open "
                   "channel -> lossless wall -> Q->inf is entailed by the physics the gate names).")
    else:
        bin_ = "(ii) NO-DISTINCT-VALUE (degenerate)"
        verdict = "KILL-SHAPE FIRES: Q_wall is degenerate / not a distinct intermediate value."
    return {"bin": bin_, "verdict": verdict, "instrument_fireable": control_fires_i}


def run_gate():
    """Run all legs and return the full result payload (used by tests + main)."""
    legA = {
        "H_1s": wall_leakage_Q(Z=1, n=1),
        "H_2s": wall_leakage_Q(Z=1, n=2),
        "He+_1s": wall_leakage_Q(Z=2, n=1),
        # reduced-mass invariance leg: m_e -> m_r,H (hydrogen reduced mass ~= 0.9995 m_e, x42's H
        # probe). Shows the DIVERGENCE is invariant under the probe-mass correction (r_turn ~= 2 a0
        # unchanged). NOT the muon (M_R_MU would put the 1s sub-l_node -> sub-Nyquist, x42 flag 1).
        "H_1s_reduced_mass": wall_leakage_Q(Z=1, n=1, m_probe=M_R_H),
    }
    legB = positive_control_Q()
    legC = radiative_diagnostic_Q()
    adj = adjudicate(legA["H_1s"]["Q_verdict"], legB["Q_control"])
    return {"legA": legA, "legB": legB, "legC": legC, "adjudication": adj}


def main():
    R = run_gate()
    print("=" * 78)
    print("T1 -- ATOM-Q CASCADE GATE  (Q_wall = wall insertion-loss of the atomic eigencavity)")
    print("=" * 78)
    print("\n[LEG A] wall insertion-loss Q, on x42's OWN dispersion (alpha-free):")
    for name, d in R["legA"].items():
        print(f"\n  {name}:  r_turn = {d['r_turn_over_a0']:.3f} a0   "
              f"kappa_inf = {d['kappa_inf_a0']:.4f}/a0   dI/dR -> {d['dI_dR_a0']:.4f}/a0")
        print("    R/r_turn |   R/a0   |   I(R)   |     T        |   Q_wall")
        for row in d["rows"]:
            q = "inf" if row["Q_wall"] == float("inf") else f"{row['Q_wall']:.2e}"
            print(f"    {row['R_over_rturn']:8d} | {row['R_over_a0']:8.1f} | "
                  f"{row['I']:8.2f} | {row['T']:.3e} | {q}")
        print(f"    -> I(R) grows linearly without bound (diverges={d['diverges']}); "
              f"Q_wall -> inf  = the INTRINSIC ENDPOINT, NOT a distinct value.")

    b = R["legB"]
    print(f"\n[LEG B] positive control (finite barrier, SAME integrator): "
          f"w={b['width_a0']} a0, dV={b['height_Ry']} Ry  ->  I={b['I']:.3f}, "
          f"Q_control = {b['Q_control']:.3e}  (finite, in [1e5,1e9])")
    print("    -> the instrument CAN report a finite intermediate Q. Leg A's inf is a PHYSICS")
    print("       verdict (infinite barrier), not an instrument that cannot fire bin (i).")

    c = R["legC"]
    print("\n[LEG C] radiative diagnostic (QUARANTINED, NOT a bin-(i) candidate):")
    print(f"    Q_rad(classical) = {c['Q_rad_classical']:.3e} = {c['Q_rad_times_alpha3']:.3f} * alpha^-3")
    print(f"    Q_rad(QM, /f)    = {c['Q_rad_QM_with_f']:.3e}  (~9.6 alpha^-3 = the measured ~1e7 rung)")
    print("    -> the observed ~1e7 is the TRANSVERSE-EM (Z_EM) port: a DIFFERENT sector x42's")
    print("       longitudinal Hermitian eigencavity does not express (bin (iii)), and it is")
    print("       alpha-SOURCED (alpha^-3 echo). NOT a substrate-distinct filter cutoff.")

    a = R["adjudication"]
    print(f"\n{'=' * 78}")
    print(f"ADJUDICATION (frozen bins):  BIN {a['bin']}")
    print(f"  instrument fireable (Leg B in-window): {a['instrument_fireable']}")
    print(f"  {a['verdict']}")
    print("=" * 78)
    return R


if __name__ == "__main__":
    main()
