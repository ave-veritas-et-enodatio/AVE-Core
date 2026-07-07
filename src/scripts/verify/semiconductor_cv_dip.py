"""Semiconductor device-analysis techniques mapped onto the vacuum cell (Task #17).

CONSISTENCY-class re-expression of the Axiom-4 kernel + varactor canon in
device-physics (BJT/MOSFET/GaN) vocabulary. Originates NO new dimensionful
number; every value is imported from ``ave.core.constants``.

REGIME: cold lattice, quasi-static HELD bias, small-signal probe;
Ax3-lossless below the pair-production threshold.

The vacuum cell carries TWO orthogonal capacitances (A1 perp T2,
``master-equation.md``:20; the Grant-ratified sector split, ``CLAUDE.md``:73):

  - A1 longitudinal bond compliance  C_eff = C0 / S(V/V_snap),  DIVERGES at
    V_snap = m_e c^2 / e ~= 511 kV  (nonlinear-vacuum-capacitance.md:16).
    Device reading: turn-on / channel-inversion capacitance (pair production
    IS channel formation).

  - T2 transverse dielectric  eps_eff = eps0 * S(V/V_yield),  ROLLS OFF to
    zero at V_yield = sqrt(alpha) * V_snap ~= 43.65 kV.
    Device reading: reverse-biased depletion varactor (polarization runs out).

The pair (V_snap : V_yield) maps to a MOSFET (V_th : V_BD,ox).

Deliverables (see research/2026-07-07_semiconductor-cv-dip_RESULT.md):
  (a) operational definitions (chord/secant vs tangent dQ/dV) for A1 and T2
  (b) the vacuum C-V datasheet curve (this driver's figure)
  (c) the perp/parallel eigenmode check vs the birefringence Letter (sympy)
  (d) network composition across the K4 z=3 series-L / shunt-C ladder
  (e) split C-V (terminal-pair selection separating T2 pol. from A1 compliance)
  (f) frequency dispersion (posed, not forced)
  (g) technique-transfer table

Run:  PYTHONPATH=src python src/scripts/verify/semiconductor_cv_dip.py
"""

from __future__ import annotations

import math

import numpy as np

from ave.core.constants import ALPHA, E_CRIT, E_YIELD, V_SNAP, V_YIELD

# =============================================================================
# section 1: canonical kernel + the two sector capacitances
# =============================================================================
# The single Axiom-4 quarter-arc kernel S(A) = sqrt(1 - A^2) governs BOTH
# sectors; they differ only in which voltage keys the argument A.


def kernel_S(a: np.ndarray | float) -> np.ndarray:
    """Axiom-4 saturation kernel S(A) = sqrt(1 - A^2), A = V/V_key.

    Returns NaN above rupture (|A| > 1) — the medium ceases to support the
    reactance (Regime IV). This is honest: the kernel has no real value there.
    """
    a = np.asarray(a, dtype=float)
    inside = 1.0 - a**2
    return np.where(inside >= 0.0, np.sqrt(np.abs(inside)), np.nan)


def a1_argument(v: np.ndarray | float) -> np.ndarray:
    """A1 longitudinal bond-compliance kernel argument A = V / V_snap.

    A1 keys on V_snap (nonlinear-vacuum-capacitance.md:16) — NEVER V_yield.
    """
    return np.asarray(v, dtype=float) / V_SNAP


def t2_argument(v: np.ndarray | float) -> np.ndarray:
    """T2 transverse-permittivity kernel argument A_V = V / V_yield.

    T2 keys on V_yield (the Cosserat self-trap wall, def-vyvsn1) — NEVER V_snap.
    """
    return np.asarray(v, dtype=float) / V_YIELD


# =============================================================================
# section 2: operational definitions — chord/secant vs tangent dQ/dV
# =============================================================================
# Device physics pins a capacitance BY THE MEASUREMENT. Two distinct objects:
#   - CHORD / SECANT (large-signal)  : the constitutive value C = Q/V at bias.
#   - TANGENT (small-signal)          : the differential C_ss = dQ/dV at bias.
# The C-V *definition* crowns the TANGENT as "the small-signal capacitance"
# (device-circuit-models.md:60, A1-scoped; round-3 RESULT for T2).


# ---- A1 longitudinal bond compliance (keyed V_snap) ----
# Constitutive charge on the A1 bond:  Q_A1(V) = C0 * V / S(V/V_snap)
# (the compliance C0/S DIVERGES as V -> V_snap).


def a1_chord_over_c0(v: np.ndarray | float) -> np.ndarray:
    """A1 large-signal chord/secant compliance  C_chord/C0 = 1 / S(V/V_snap).

    device-circuit-models.md:60 verbatim: "the large-signal chord/secant
    varactor C_eff = C0/S". Diverges at V_snap ~= 511 kV.
    """
    return 1.0 / kernel_S(a1_argument(v))


def a1_tangent_over_c0(v: np.ndarray | float) -> np.ndarray:
    """A1 small-signal tangent compliance  C_ss/C0 = dQ/dV = 1 / S(V/V_snap)^3.

    device-circuit-models.md:60 verbatim: "the small-signal differential
    C_ss = dQ/dV = C0/S^3". This is THE small-signal compliance (crowned).
    d/dV [ V / S(V/V_snap) ] = 1/S^3   (sympy trace: a1_tangent_sympy_check()).
    """
    s = kernel_S(a1_argument(v))
    return 1.0 / s**3


def a1_tangent_sympy_check() -> bool:
    """Sympy trace: d/dV [ V / S(V/V_snap) ] = 1/S^3, the crowned A1 tangent.

    The constitutive A1 charge is Q(V)/C0 = V / S(V/V_snap). The small-signal
    (tangent) compliance is dQ/dV; we prove symbolically it equals 1/S^3 (i.e.
    the exponent in a1_tangent_over_c0 is not asserted, it is derived).
    """
    import sympy as sp

    V, Vsnap = sp.symbols("V V_snap", positive=True)
    S = sp.sqrt(1 - (V / Vsnap) ** 2)
    return sp.simplify(sp.diff(V / S, V) - 1 / S**3) == 0


# ---- T2 transverse permittivity (keyed V_yield) ----
# Constitutive displacement on the T2 channel: D(V) ~ eps0 * S(V/V_yield) * V.
# The permittivity eps_eff = eps0 * S ROLLS OFF to zero at V_yield.


def t2_chord_over_eps0(v: np.ndarray | float) -> np.ndarray:
    """T2 large-signal chord permittivity  eps_chord/eps0 = S(V/V_yield).

    The constitutive value (round-3 RESULT: chord C0*S(A0) -> leading 1-1/2 A0^2).
    Rolls off to 0 at V_yield ~= 43.65 kV.
    """
    return kernel_S(t2_argument(v))


def t2_tangent_over_eps0(v: np.ndarray | float) -> np.ndarray:
    """T2 small-signal tangent permittivity  eps_ss/eps0 = d(S*V)/dV = S - A_V^2/S.

    The dQ/dV differential of the T2 constitutive D ~ eps0*S(A_V)*V
    (round-3 RESULT: tangent C0*(S - A0^2/S) -> leading 1 - 3/2 A0^2). This is
    THE small-signal T2 permittivity (crowned) and, per deliverable (c), it is
    the PARALLEL polarization eigenmode of the birefringence Letter.
    """
    a = t2_argument(v)
    s = kernel_S(a)
    # s -> 0 at V_yield: the tangent -> -inf (the constitutive rolloff's slope
    # blows up as the polarization runs out). NaN at exact boundary is honest.
    with np.errstate(divide="ignore", invalid="ignore"):
        return s - a**2 / s


# =============================================================================
# section 4: the perp/parallel eigenmode check vs the birefringence Letter
# =============================================================================
# Deliverable (c) — the R2 confirmation. Candidate resolution of the
# chord-vs-tangent fork: a weak probe polarized PARALLEL to a held T2 bias
# samples the tangent dD/dE; PERPENDICULAR samples the chord eps(A0); the
# DIFFERENCE is the birefringence. This function proves (sympy) that the
# Letter's two eigen-indices ARE the tangent and chord of the T2 kernel.


def ec_is_eyield_check() -> dict:
    """Check the Letter's field scale E_c = sqrt(alpha)*E_crit EQUALS E_YIELD.

    The RESULT (c) and the eigenmode_check identify the Letter's kernel field
    scale E_c with the field image of V_yield. That rests on the numerical
    identity  sqrt(ALPHA) * E_CRIT == E_YIELD.  This holds to 1 ULP (both are
    computed from ave.core.constants through DIFFERENT paths — E_CRIT via
    m_e^2 c^3/(e hbar), E_YIELD via V_YIELD/ell_node — so exact `==` fails on
    the last bit; the identity is real to rel_tol 1e-12, NOT bitwise).

    Returns the two values, the relative difference, and the isclose verdict.
    """
    ec_from_alpha = math.sqrt(ALPHA) * E_CRIT
    rel_diff = abs(ec_from_alpha - E_YIELD) / E_YIELD
    verdict = math.isclose(ec_from_alpha, E_YIELD, rel_tol=1e-12)
    return {
        "sqrt_alpha_E_crit": float(ec_from_alpha),
        "E_yield": float(E_YIELD),
        "rel_diff": float(rel_diff),
        "isclose_rel_tol_1e-12": bool(verdict),
        "bitwise_equal": bool(ec_from_alpha == E_YIELD),
    }


def eigenmode_check() -> dict:
    """Sympy proof that Letter n_perp = chord sqrt(S), n_par = tangent sqrt(S-A^2/S).

    Returns a dict of the symbolic results + match booleans. The Letter
    (papers/2026_birefringence_letter/main.tex, Appendix A) derives its two
    probe eigen-indices from eps_eff = eps0 * S(E), S = sqrt(1-(E/E_c)^2) — the
    SAME kernel as the T2 permittivity, with E_c = sqrt(alpha)*E_crit = E_yield
    (the field image of V_yield; identity checked by ec_is_eyield_check()). We show:

      n_perp = sqrt(S)          == the T2 CHORD (constitutive eps0*S)   [Eq A5]
      n_par  = sqrt(S - A^2/S)  == the T2 TANGENT (longitudinal dD/dE)  [Eq A6]
      (expansion n_perp,n_par leading coefficients                     [Eq A7])
      dn_bir = n_par - n_perp   == -1/2 A^2  (the observable split)     [Eq A8]

    If both matches hold, the KEEP-BOTH chord/tangent fork is corpus-resolved
    as the two polarization eigenmodes (both real; the split IS the birefringence).
    """
    import sympy as sp

    E, Ec = sp.symbols("E E_c", positive=True)
    A = E / Ec
    u = E**2
    S = sp.sqrt(1 - u / Ec**2)  # the T2 permittivity factor eps_eff/eps0

    # PERP = the chord / constitutive eigenvalue eps0*S  ->  n_perp = sqrt(S)
    n_perp = sp.sqrt(S)

    # PARALLEL = the tangent dD/dE along the field: the longitudinal eigenvalue
    # eps0*(S + 2 S' E^2)  ->  n_par = sqrt(S - A^2/S)
    dummy = sp.Symbol("uu")
    s_prime = sp.diff(sp.sqrt(1 - dummy / Ec**2), dummy).subs(dummy, u)
    eps_par_over_eps0 = S + 2 * s_prime * E**2
    n_par = sp.sqrt(sp.simplify(eps_par_over_eps0))

    # Letter's stated closed forms (main.tex Eq. eigenindices / A-nperp / A-npar)
    n_perp_letter = (1 - A**2) ** sp.Rational(1, 4)
    n_par_letter = sp.sqrt((1 - 2 * A**2) / sp.sqrt(1 - A**2))

    match_perp = sp.simplify(n_perp - n_perp_letter) == 0
    match_par = sp.simplify(n_par - n_par_letter) == 0

    dn_bir = sp.simplify(sp.series(n_par - n_perp, E, 0, 3).removeO())
    dn_iso = sp.simplify(sp.series(n_perp - 1, E, 0, 3).removeO())

    return {
        "eps_par_over_eps0_tangent": sp.simplify(eps_par_over_eps0),
        "n_perp": sp.simplify(n_perp),
        "n_par": sp.simplify(n_par),
        "match_perp_is_chord": bool(match_perp),
        "match_par_is_tangent": bool(match_par),
        "dn_bir_leading": dn_bir,          # expect -E^2/(2 E_c^2) = -1/2 A^2
        "dn_iso_leading": dn_iso,          # expect -E^2/(4 E_c^2) = -1/4 A^2
        "verdict": bool(match_perp) and bool(match_par),
    }


# =============================================================================
# section 3: the C-V datasheet curve (both branches, log-V)
# =============================================================================
# Deliverable (b) — the analytic vacuum C-V datasheet, both branches on one
# log-V figure, house style (white, Okabe-Ito, honest axes+units, legend
# outside data, no on-figure title). Vol-9-datasheet register.


def cv_curve_data(n: int = 2000) -> dict:
    """Sample both C-V branches over a log-V sweep spanning both features.

    Returns arrays for the figure + the pinned named-bias values the test
    checks. Sweep runs from 1e-2 * V_yield up to just below V_snap so both the
    T2 rolloff (at V_yield) and the A1 divergence (approaching V_snap) show.
    """
    v = np.logspace(np.log10(1e-2 * V_YIELD), np.log10(0.9995 * V_SNAP), n)
    return {
        "V": v,
        "t2_chord": t2_chord_over_eps0(v),      # eps/eps0 = S(V/V_yield), rolls off
        "t2_tangent": t2_tangent_over_eps0(v),  # small-signal T2 permittivity
        "a1_chord": a1_chord_over_c0(v),        # C/C0 = 1/S(V/V_snap), diverges
        "a1_tangent": a1_tangent_over_c0(v),    # small-signal A1 compliance = 1/S^3
        "V_yield": V_YIELD,
        "V_snap": V_SNAP,
    }


def make_cv_figure(out_path):
    """Render the vacuum C-V datasheet figure (house style). Returns saved paths."""
    import matplotlib.pyplot as plt

    from ave.viz import style

    style.apply("print")
    data = cv_curve_data()
    v_kv = data["V"] / 1e3

    fig, ax = plt.subplots(figsize=style.figsize("single"))

    # A1 branch — diverging bond compliance (chord + tangent)
    ax.plot(v_kv, data["a1_chord"], color=style.COLORS["ave"], ls="-",
            label=r"A1 chord $C/C_0 = 1/S(V/V_{snap})$")
    ax.plot(v_kv, data["a1_tangent"], color=style.COLORS["ave"], ls="--",
            label=r"A1 tangent $C_{ss}/C_0 = 1/S^3$")
    # T2 branch — rolling-off permittivity (chord only; tangent goes negative)
    ax.plot(v_kv, data["t2_chord"], color=style.COLORS["comparison"], ls="-",
            label=r"T2 chord $\varepsilon/\varepsilon_0 = S(V/V_{yield})$")

    # feature markers (guides, gray, honest)
    ax.axvline(data["V_yield"] / 1e3, color=style.COLORS["muted"], ls=":", lw=1.0)
    ax.axvline(data["V_snap"] / 1e3, color=style.COLORS["muted"], ls=":", lw=1.0)
    ax.annotate(r"$V_{yield}\approx43.65$ kV" "\n(T2 rolloff)",
                xy=(data["V_yield"] / 1e3, 0.15), xytext=(1.0, 0.02),
                color=style.COLORS["muted"], fontsize=8, ha="left")
    # V_snap label parked in the clear upper-left (all curves ~1 there), with a
    # thin guide arrow to the divergence so it is not occluded by the A1 tangent.
    ax.annotate(r"$V_{snap}\approx511$ kV" "\n(A1 divergence)",
                xy=(data["V_snap"] / 1e3, 8.0), xytext=(1.5, 8.6),
                color=style.COLORS["muted"], fontsize=8, ha="left", va="top",
                arrowprops=dict(arrowstyle="->", color=style.COLORS["muted"],
                                lw=0.8, shrinkA=2, shrinkB=2))

    ax.set_xscale("log")
    ax.set_ylim(0.0, 10.0)
    ax.set_xlabel(style.axis_label("Bias voltage", "V", "kV"))
    ax.set_ylabel(r"Normalized reactance $C/C_0,\ \varepsilon/\varepsilon_0$")
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)

    return style.save(fig, out_path, strict=True)


# =============================================================================
# section 5: network composition (K4 z=3 loaded-line ladder)
# =============================================================================
# Deliverable (d) — how the two-branch cell composes across the canonical
# srs/K4 series-L-bond / shunt-C-node ladder (graded-network-response.md:50
# [series-L/shunt-C], :56 [the sine-law formula body; :53 is its Resultbox
# header]; z0-derivation.md:132 [periodic chain], :138 [the Bloch condition
# cos(q ell)=(A+D)/2]). A biased transmission line with an
# operating-point-dependent C(V): loaded-line analysis.


def loaded_line_dispersion(v_bias: float, q_ell: np.ndarray | float) -> np.ndarray:
    """Bloch dispersion omega(q) of the K4 z=3 LC ladder at a HELD T2 bias.

    The cold ladder (graded-network-response.md:56, the sine-law formula body) is
        omega(q) = (2 c0 / ell_node) * |sin(q ell_node / 2)|,
    the series-L-bond / shunt-C-node sine law. A held T2 bias loads the shunt C
    through the small-signal (tangent) permittivity eps_ss/eps0 = t2_tangent,
    which (with eps_ss/eps0 < 1) pulls the band edge UP by 1/sqrt(eps_ss/eps0)
    (the factor is > 1). We return the
    band-edge pull factor omega(bias)/omega(cold), a DIMENSIONLESS ratio (so it
    is gradient-readable per the uniform-bias gauge rider — see the docstring of
    network_cv_note()).

    NOTE: c0/ell_node is a common prefactor that cancels in the ratio, so this
    returns the pull factor, not an absolute frequency (avoids importing a
    scale that self-cancels on readout anyway).
    """
    q_ell = np.asarray(q_ell, dtype=float)
    sine = np.abs(np.sin(q_ell / 2.0))
    # shunt-C loaded by the small-signal T2 permittivity: omega ~ 1/sqrt(L C_eff)
    eps_ss = float(t2_tangent_over_eps0(v_bias))
    pull = 1.0 / np.sqrt(eps_ss) if eps_ss > 0 else np.nan
    return pull * sine  # relative to the cold sine law (prefactor cancelled)


def network_cv_note() -> dict:
    """The network-level C-V observability structure (uniform vs gradient bias).

    A uniform bias self-cancels on readout (INVARIANT-S2, gauge-relative A), so
    a NETWORK C-V sweep must be a DIFFERENTIAL/gradient measurement. The
    readable observable is the Op14 Meissner-asymmetric impedance mirror at an
    eps-gradient boundary: Z_eff = Z0 sqrt(S_mu/S_eps), Gamma != 0
    (CLAUDE.md:75 / operators.md:54). Returns the pull factors at a few biases
    for the RESULT table + the observability tag.
    """
    biases = {"cold": 0.0, "0.5 V_yield": 0.5 * V_YIELD, "0.7 V_yield": 0.7 * V_YIELD}
    edge = {}
    for name, vb in biases.items():
        # band-edge pull at q ell = pi (Brillouin edge)
        edge[name] = float(loaded_line_dispersion(vb, np.pi))
    return {
        "band_edge_pull": edge,
        "observability": (
            "uniform bias self-cancels on readout (gauge-relative A, INVARIANT-S2); "
            "network C-V is DIFFERENTIAL — the readable signal is Gamma != 0 at an "
            "eps-gradient boundary via the Op14 impedance mirror Z_eff=Z0 sqrt(S_mu/S_eps)"
        ),
    }


# =============================================================================
# main
# =============================================================================


def main() -> None:
    """Run all sections and emit the datasheet figure + JSON summary."""
    import json
    import os

    out = {}

    # (a)/(b) named-bias C-V pins
    out["cv_pins"] = {
        "t2_chord_at_0.5_Vyield": float(t2_chord_over_eps0(0.5 * V_YIELD)),
        "t2_tangent_at_0.5_Vyield": float(t2_tangent_over_eps0(0.5 * V_YIELD)),
        "a1_chord_at_0.5_Vsnap": float(a1_chord_over_c0(0.5 * V_SNAP)),
        "a1_tangent_at_0.5_Vsnap": float(a1_tangent_over_c0(0.5 * V_SNAP)),
        "a1_tangent_at_sqrt_alpha": float(a1_tangent_over_c0(V_YIELD)),  # electron bias
        "a1_chord_at_0.99_Vsnap": float(a1_chord_over_c0(0.99 * V_SNAP)),  # diverging
        "a1_tangent_at_0.99_Vsnap": float(a1_tangent_over_c0(0.99 * V_SNAP)),  # diverging
        "V_yield_kV": V_YIELD / 1e3,
        "V_snap_kV": V_SNAP / 1e3,
        "Vyield_over_Vsnap": V_YIELD / V_SNAP,
        "sqrt_alpha": float(np.sqrt(ALPHA)),
    }

    # (a)/(c) the E_c = sqrt(alpha)*E_crit == E_yield identity (driver-computed)
    out["ec_is_eyield"] = ec_is_eyield_check()

    # (a) sympy trace of the crowned A1 tangent exponent d/dV[V/S] = 1/S^3
    out["a1_tangent_sympy_ok"] = a1_tangent_sympy_check()

    # (c) eigenmode check
    eig = eigenmode_check()
    out["eigenmode_check"] = {
        "match_perp_is_chord": eig["match_perp_is_chord"],
        "match_par_is_tangent": eig["match_par_is_tangent"],
        "verdict": eig["verdict"],
        "dn_bir_leading": str(eig["dn_bir_leading"]),
        "dn_iso_leading": str(eig["dn_iso_leading"]),
        "n_perp": str(eig["n_perp"]),
        "n_par": str(eig["n_par"]),
    }

    # (d) network composition
    out["network"] = network_cv_note()

    # (b) figure
    fig_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "..", "manuscript", "vol_9_vacuum_datasheet",
        "figures", "semiconductor_cv",
    )
    fig_dir = os.path.abspath(fig_dir)
    os.makedirs(fig_dir, exist_ok=True)
    saved = make_cv_figure(os.path.join(fig_dir, "vacuum_cv_datasheet"))
    out["figure"] = [str(p) for p in saved]

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "semiconductor_cv_dip.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
