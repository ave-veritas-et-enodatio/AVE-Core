"""The RESONANT TIME-AVERAGED TENSION LAW + the make-or-break radiation control.

Resolves the OPEN plucking-mechanism fork left by PR #527
(research/2026-07-04_bond-force-sign-rule_result.md): the arm-(a) tent law needs a
PLUCKER. GRANT'S RULING (ratified 2026-07-04): the bond is NOT plucked -- it
AUTO-RESONATES. The electron is a resonant LC tank at a self-set Q-point
(resonant-lc-solitons.md:10); its bonds carry a standing transverse oscillation with
<y>=0 but <y^2>>0, and because the pluck law is QUADRATIC the time-averaged tension
survives -- the tank's own hum IS the bias.

PREREG (FROZEN, committed BEFORE this driver):
  research/2026-07-04_resonant-tension-law_prereg_FROZEN.md

═══════════════════════════════════════════════════════════════════════════════
SECTOR HEADER (declare before any substrate statement)
═══════════════════════════════════════════════════════════════════════════════
  * SECTOR : the MECHANICAL transverse bow DOF on the K4/srs bond (the #527 arm-(a)
             tent-geometry pluck response). NOT the Cosserat (2,3) winding. T2
             HOMONYM GUARD (binding, cite #527): the static winding carries NO real
             power (resonant-lc-solitons.md:128) and canNOT be the plucker; the
             resonance is the mechanical bow, never re-welded to the winding.
             mass=A1; charge=Cosserat-winding; the bow=T2-mechanical-response.
  * MODE   : cycle-averaged QUASI-STATIC about the resonant Q-point. The bond hums
             at w_resonant; the tensor probe reads the DC-biased small-signal
             network around that Q-point.
  * TIMESCALE-SEPARATION (declared assumption): resonance period 2pi/w << the
             tensor-probe timescale, so the tensor sees the CYCLE-AVERAGED tension
             <T>, not the instantaneous T(t). The time-average factor is <sin^2>=1/2,
             DERIVED (sympy), never asserted.
  * REGIME : Op14 ON. PHASE-STATE = the resonant Q-point (a standing reactive mode,
             Ax3 lossless; closed-EM-port eigenframe Im(w)->0, Q->inf,
             resonant-lc-solitons.md:104). y0->0 is the no-hum limit (<T>->0).

PART 1: derive <T> of the standing hum on the #527 tent bond (leading + exact),
        feed through the #526 remap, re-band the matter track.
PART 2 (make-or-break): the radiation control -- a traveling wave on an Ax3-matched
        line (clm-mfb2ax) exerts NO time-averaged axial reaction (respect #518 s7
        rho_eff=rho_cold / clm-clvchn null); a standing wave between Gamma=-1
        reflecting terminations recovers the Part-1 law.

CONSUMES (import only; NEVER edits -- concurrency-safe):
  #527 bond_force_sign_rule (tent law, in-regime bow, four-track remap),
  #526 prestress_elastic_tensor (bond_tension, extract_prestress_Cij, moduli),
  #525 bond_transmission_line (cascade_gamma, abcd_lossless_line).

α-CLEAN: no alpha / Q_TANK on any computed path. alpha enters ONLY via the imported
A1 op-point A=sqrt(alpha) (Class-C echo, def-vyvsn1), read-off, never tuned.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/resonant_tension_law.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

# CONSUME #527 (tent law, in-regime bow, four-track remap) -- import only.
from scripts.vol_1_foundations.bond_force_sign_rule import (  # noqa: E402
    arm_a_pluck_tension,           # exact tent law k_a*l*(1-l/sqrt(l^2+4y^2))
    arm_a_pluck_tension_leading,   # leading 2 k_a y^2 / l
    in_regime_pluck_bow,           # the fixed-arc premise's own displacement ceiling
    _remap_at_signed_T,            # feed a SIGNED per-bond axial force through #526
    ARC_STAR_BAND,                 # (0.70, 0.96) delta_y band
    A_CORE_SQRT_ALPHA,             # A1 mass-core op-point sqrt(alpha) (read-off)
)
from scripts.vol_1_foundations.srs_elastic_tensor import srs_primitive  # noqa: E402

# CONSUME #525 TL machinery (matched-line reflection + traveling-wave phase) -- import only.
from scripts.vol_4_engineering.bond_transmission_line import (  # noqa: E402
    cascade_gamma,
    abcd_lossless_line,
)
from ave.core.constants import Z_0  # noqa: E402


# ===========================================================================
# PART 1 -- THE RESONANT TIME-AVERAGED TENSION LAW
# ===========================================================================
def symbolic_backbone() -> dict:
    """Sympy verification of the two DERIVED time-average facts (prereg Part 1a).

    Returns a dict of exact-zero residuals; main()/PC HALTs if any is not exactly 0.
    The ONE ½ this arc introduces (⟨sin²⟩) is DERIVED here, not asserted (knife).
    """
    import sympy as sp

    t, w, y0, k_a, ell = sp.symbols("t omega y0 k_a ell", positive=True)
    out = {}
    period = 2 * sp.pi / w

    # (1) ⟨sin²⟩ = ½ over a full period -- the ONE derived-half of this arc.
    s2 = sp.integrate(sp.sin(w * t) ** 2, (t, 0, period)) / period
    out["sin2_avg_minus_half"] = sp.simplify(s2 - sp.Rational(1, 2))          # == 0

    # (2) ⟨y²⟩ = y0²/2 for y=y0 sin(wt).
    y = y0 * sp.sin(w * t)
    y2 = sp.integrate(y ** 2, (t, 0, period)) / period
    out["y2_avg_minus_y0sq_over_2"] = sp.simplify(y2 - y0 ** 2 / 2)           # == 0

    # (3) leading-tent time-average ⟨T_lead⟩ = (2 k_a/ℓ)⟨y²⟩ = (k_a/ℓ) y0².
    T_lead = 2 * k_a / ell * y ** 2
    T_lead_avg = sp.integrate(T_lead, (t, 0, period)) / period
    out["T_lead_avg_minus_ka_y0sq_over_ell"] = sp.simplify(
        T_lead_avg - k_a * y0 ** 2 / ell
    )                                                                        # == 0

    # (4) the ⟨T⟩ = (2 k_a/ℓ)⟨y²⟩ identity chain (the substitution the noun rests on).
    out["T_lead_avg_minus_2ka_over_ell_times_y2avg"] = sp.simplify(
        T_lead_avg - 2 * k_a / ell * y2
    )                                                                        # == 0

    # (5) the leading tent law IS the 2nd-order series of the EXACT tent law (ties the
    #     resonant law to the #527 exact tent geometry, not a fresh guess).
    T_exact = k_a * ell * (1 - ell / sp.sqrt(ell ** 2 + 4 * y0 ** 2))
    lead_coeff = sp.limit(sp.series(T_exact, y0, 0, 4).removeO() / y0 ** 2, y0, 0)
    out["exact_leading_coeff_minus_2ka_over_ell"] = sp.simplify(
        lead_coeff - 2 * k_a / ell
    )                                                                        # == 0

    return out


def resonant_tension_leading(y0: float, k_a: float = 1.0, ell: float = 1.0) -> float:
    """Leading-order time-averaged tension ⟨T⟩ = (2 k_a/ℓ)·⟨y²⟩ = (k_a/ℓ) y0².

    ⟨y²⟩ = y0²·⟨sin²⟩ = y0²/2 (⟨sin²⟩=½ DERIVED in symbolic_backbone). The ½ is the
    ONLY declared-derived half of this arc; no other un-derived ½/¼ enters.
    """
    return float(k_a * y0 ** 2 / ell)


def resonant_tension_exact(y0: float, k_a: float = 1.0, ell: float = 1.0,
                           n_theta: int = 200_000) -> float:
    """Exact tent law, cycle-averaged over one period (numeric quadrature).

    ⟨T_a⟩ = (1/2π)∮ T_a(y0·sinθ) dθ with T_a the #527 exact tent law (imported, NOT
    reimplemented). Concave in y² ⟹ this is ≤ the leading law (the leading is an
    upper bound); the gap is the quadratic-approximation breakdown (prereg Part 1b).
    """
    theta = np.linspace(0.0, 2.0 * np.pi, n_theta, endpoint=False)
    y = y0 * np.sin(theta)
    # arm_a_pluck_tension is even in y and vectorizes elementwise; call the imported fn
    T = np.array([arm_a_pluck_tension(float(yy), k_a=k_a, ell=ell) for yy in y])
    return float(np.mean(T))


def part1_law_and_band(pos, bonds, rho) -> dict:
    """The Part-1 law (leading + exact), banded over arc* and the in-regime y0 range,
    fed through the #526 remap. Re-bands the matter track.

    - The in-regime y0 ceiling per arc* is the #527 in_regime_pluck_bow(arc*) (the
      fixed-arc premise's own displacement ceiling) -- IMPORTED, not re-derived.
    - ⟨T⟩>0 (tension) ⟹ caps ρ' (grows k_shear_eff), matching #527 arm (a) sign.
    - The matter track ρ'/ν is read through the #526 _remap_at_signed_T at the A1
      op-point A_axial=√α (S≈0.996) and the #518 shear operating amplitude, exactly
      as #527's arm (a) -- the ONLY change is that T is now the RESONANT ⟨T⟩ instead
      of the #527 static in-regime-bow tension.
    """
    A_axial = A_CORE_SQRT_ALPHA
    A_shear_op = 0.99479  # #518 crossing amplitude (read-off; sets k_shear at crossing)
    ell = float(np.mean([np.linalg.norm(d) for (_, _, d) in bonds]))  # =1 on srs
    lo, hi = ARC_STAR_BAND

    band = {}
    lead_vs_exact_rows = []
    for edge, arc_star in (("lo_elastica", lo), ("hi_tent", hi)):
        y0_max = in_regime_pluck_bow(arc_star, ell)      # in-regime bow ceiling
        # MAJOR-3 (honest grid): the old linear 0.25·y0_max first sample was arbitrary,
        # making the band top (9.65 / +0.283 → 2/7) a GRID ARTIFACT of the sample step
        # rather than the y0→0 IDENTITY it approaches. LOG-space toward y0→0 so the band
        # top is explicitly the identity endpoint (⟨T⟩→0 ⟹ unstressed #518 crossing:
        # ρ'→9.7734, ν→2/7), plus the y0_max ceiling. The identity endpoints are LABELED
        # (rows carry is_identity_limit); the reportable interior band excludes them.
        y0_grid = np.concatenate([[0.0], y0_max * np.logspace(-4, 0, 9)])
        rows = []
        for y0 in y0_grid:
            T_lead = resonant_tension_leading(float(y0), ell=ell)
            T_exact = resonant_tension_exact(float(y0), ell=ell)
            rel = (T_lead - T_exact) / T_exact if T_exact > 0 else 0.0
            # feed the RESONANT ⟨T⟩ (tension, +) through the #526 remap -- both laws
            rem_lead = _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, +T_lead)
            rem_exact = _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, +T_exact)
            # MAJOR-3: label the y0→0 identity limit (⟨T⟩→0 ⟹ unstressed #518 crossing,
            # ρ'→9.7734 AND ν→2/7 BOTH by identity -- the symmetric twins).
            is_identity = bool(y0 <= 1e-3 * y0_max)
            rows.append({
                "y0": float(y0),
                "is_identity_limit": is_identity,
                "T_avg_leading": float(T_lead),
                "T_avg_exact": float(T_exact),
                "leading_over_exact_rel_dev": float(rel),
                "rho_prime_leading": rem_lead["rho_prime"],
                "rho_prime_exact": rem_exact["rho_prime"],
                "nu_leading": rem_lead["nu"],
                "nu_exact": rem_exact["nu"],
                "k_shear_eff_leading": rem_lead["k_shear_eff"],
            })
            if not is_identity:
                lead_vs_exact_rows.append({"arc_star": arc_star, "y0": float(y0),
                                           "rel_dev": float(rel)})
        band[edge] = {"arc_star": arc_star, "y0_in_regime_max": float(y0_max),
                      "rows": rows}

    # the reportable INTERIOR matter track EXCLUDES the y0→0 identity rows (their
    # ρ'→9.7734 / ν→2/7 are the unstressed-crossing IDENTITY, not a re-banded landing).
    def _interior(field):
        return [r[field] for e in band.values() for r in e["rows"]
                if not r["is_identity_limit"] and np.isfinite(r[field])]
    all_rp = _interior("rho_prime_exact")
    all_rp_lead = _interior("rho_prime_leading")
    all_nu = _interior("nu_exact")
    matter_track = {
        "rho_prime_band_exact": [float(min(all_rp)), float(max(all_rp))] if all_rp else None,
        "rho_prime_band_leading": [float(min(all_rp_lead)), float(max(all_rp_lead))]
        if all_rp_lead else None,
        "nu_band": [float(min(all_nu)), float(max(all_nu))] if all_nu else None,
        "identity_limit_rho_prime": 9.7734,   # the y0→0 twin (labeled, EXCLUDED from band)
        "identity_limit_nu": 2.0 / 7.0,        # the y0→0 twin (labeled, EXCLUDED from band)
        "worst_leading_over_exact_rel_dev": float(max(r["rel_dev"] for r in lead_vs_exact_rows))
        if lead_vs_exact_rows else 0.0,
        "note": "matter track re-banded over the in-regime hum amplitude y0 in "
        "(0, in_regime_pluck_bow(arc*)] for arc* in [0.70, 0.96], INTERIOR only. The "
        "y0→0 identity twins (ρ'→9.7734 AND ν→2/7, both the unstressed #518 crossing) "
        "are LABELED and EXCLUDED from the reported band (symmetric identity treatment, "
        "MAJOR-3). VALUE inherits #526 GR-imported status; EMERGENCE grade FORBIDDEN. "
        "NB (MAJOR-4b): the ρ'/ν VALUES here are from a 1D-linear + srs-tensor remap "
        "readout; the fork-resolution CONCLUSION is drawn from the 1D linear ladder "
        "control (Part 2) -- the full srs-lattice generalization is UNTESTED.",
    }
    return {"band": band, "matter_track": matter_track,
            "op_point": {"A_axial_sqrt_alpha": float(A_axial), "A_shear_op": A_shear_op,
                         "ell": ell}}


# ===========================================================================
# PART 2 -- THE RADIATION CONTROL (make-or-break)
# ===========================================================================
def matched_line_reflection(theta: float, n_sections: int = 20) -> float:
    """(i) traveling wave on a MATCHED chain: |Gamma| via the imported cascade_gamma.

    A cascade of N identical Z_0 sections terminated in Z_0 presents no impedance
    step at any interior node ⟹ Γ→0 (clm-mfb2ax, the Ax3 matched line). This is the
    REFLECTION-read reference path for arm (i). PC-matched HALT-gates |Γ|<1e-12.
    """
    return float(abs(cascade_gamma(np.full(n_sections, Z_0), Z_0, theta)))


def reflecting_termination_reflection(theta: float, kind: str, n_sections: int = 20) -> float:
    """(ii) standing wave between reflecting terminations: |Gamma| (short/open).

    A reflecting termination (short Z_term→0, the Γ=−1 self-trap wall; or open
    Z_term→∞) gives |Γ|=1 through the SAME Z_0-uniform cascade -- the DIFFERENT
    boundary condition that makes the wave a confined standing mode. PC-reflect
    HALT-gates |Γ|=1 (proves the instrument reads a reflecting wall -- liveness).
    """
    z_term = 0.0 if kind == "short" else 1e18  # short = Γ=−1 wall; open = Γ=+1
    return float(abs(cascade_gamma(np.full(n_sections, Z_0), z_term, theta)))


def field_from_phasor(gamma: complex, theta: float, n_cells: int = 40,
                      y0: float = 1.0, k_a: float = 1.0, ell: float = 1.0) -> dict:
    """Field-space tension ⟨T⟩(x) from the incident+reflected PHASOR (Γ-parameterized).

    y(x,t) = Re{ y0 [ e^{-jβx} + Γ e^{+jβx} ] e^{jωt} }; cycle-averaged
    ⟨y²(x)⟩ = ½ y0² |e^{-jβx}+Γe^{+jβx}|²; the LOCAL tent tension is
    ⟨T⟩(x) = (2 k_a/ℓ)·⟨y²(x)⟩ (the Part-1 law applied pointwise, uses the DERIVED ½).

    🔴 RETRACTED-AS-INDEPENDENT (2026-07-04, orchestrator MAJOR-1): this path is
    BUILT FROM Γ, so it is NOT independent of the Γ-read. The gradient RMS it reports
    equals 1.4244·|Γ| identically (verified across 6 decades). The genuinely Γ-free
    reference is field_from_abcd_propagation (below); THAT is the independent path.

    Returns the per-bond ⟨T⟩ (mean over the mode shape) -- the quantity the mechanism
    CONSUMES (_remap_at_signed_T reads T, not d⟨T⟩/dx). The gradient/uniformity fields
    are kept for the mode-shape diagnostic only; they are NOT the control observable
    (that was the CRITICAL error -- see part2_radiation_control).
    """
    beta_x = np.linspace(0.0, n_cells * theta, 400)
    phasor = y0 * (np.exp(-1j * beta_x) + gamma * np.exp(+1j * beta_x))
    y2_avg = 0.5 * np.abs(phasor) ** 2
    T_local = (2.0 * k_a / ell) * y2_avg
    dT = np.gradient(T_local, beta_x)
    norm = (2.0 * k_a / ell) * y0 ** 2 + 1e-30
    # ANALYTIC antinode ⟨T⟩ = (k_a/ℓ) y0² (1+|Γ|)²; bond-averaged over a full mode
    # period is (k_a/ℓ) y0² (1+|Γ|²) (the |e^{-jβx}+Γe^{+jβx}|² spatial mean).
    T_antinode_analytic = float((k_a / ell) * y0 ** 2 * (1.0 + abs(gamma)) ** 2)
    T_bond_avg_analytic = float((k_a / ell) * y0 ** 2 * (1.0 + abs(gamma) ** 2))
    return {
        "T_local_mean": float(T_local.mean()),
        "T_local_max": float(T_local.max()),
        "T_local_peak_to_peak": float(T_local.max() - T_local.min()),
        "T_antinode_analytic": T_antinode_analytic,
        "T_bond_avg_analytic": T_bond_avg_analytic,
        "grad_rms_norm": float(np.sqrt(np.mean(dT ** 2)) / norm),  # = 1.4244|Γ| (NOT indep)
        "is_uniform": bool((T_local.max() - T_local.min()) < 1e-9 * (T_local.mean() + 1e-30)),
    }


def field_from_abcd_propagation(theta: float, n_cells: int = 40, y0: float = 1.0,
                                k_a: float = 1.0, ell: float = 1.0) -> dict:
    """GENUINELY Γ-FREE traveling-wave field: propagate a PURE FORWARD state through N
    cascaded abcd_lossless_line segments (imported #525). NO Γ input ANYWHERE.

    A forward-only wave has I = V/Z_0 (the matched-line forward-wave relation). Seeding
    (V,I)=(y0, y0/Z_0) at x=0 and cascading the lossless-line ABCD M(θ,Z_0) advances the
    PHASE of V while |V(x)| stays constant along the matched line (Ax3 lossless: no loss,
    no reflection). The cycle-averaged transverse energy density is ⟨y²(x)⟩=½|V(x)|² and
    the per-bond tent tension is ⟨T⟩(x)=(2k_a/ℓ)⟨y²(x)⟩.

    This is the prereg-promised Γ-free construction (MAJOR-1 fix): it computes the
    per-bond ⟨T⟩ from the propagated FIELD directly, so it can GENUINELY disagree with
    the phasor/Γ path. If a bug made one nonzero while the other stayed zero they'd
    diverge -- the reconcile is now real.

    RESULT (the honest negative): a pure forward traveling wave carries a PERSISTENT,
    UNIFORM ⟨T⟩ = (k_a/ℓ)y0² per bond -- it does NOT vanish. Same as the confined hum's
    per-bond ⟨T⟩. The mechanism, which consumes ⟨T⟩, would stiffen radiation too.
    """
    state = np.array([y0, y0 / Z_0], dtype=complex)   # pure FORWARD wave (I=V/Z_0)
    M = abcd_lossless_line(theta, Z_0)
    Vs = [state[0]]
    for _ in range(n_cells):
        state = M @ state
        Vs.append(state[0])
    Vs = np.asarray(Vs)
    y2 = 0.5 * np.abs(Vs) ** 2                          # ⟨y²⟩(x) = ½|V(x)|² (derived ½)
    T_local = (2.0 * k_a / ell) * y2                    # per-bond ⟨T⟩(x)
    return {
        "T_bond_mean": float(T_local.mean()),           # the per-bond ⟨T⟩ the remap eats
        "T_peak_to_peak": float(T_local.max() - T_local.min()),
        "is_uniform": bool((T_local.max() - T_local.min()) < 1e-9 * (T_local.mean() + 1e-30)),
        "gamma_free": True,   # NO Γ was input on this path -- genuinely independent
    }


def part2_radiation_control(pos, bonds, rho, theta: float = 0.3) -> dict:
    """The make-or-break control (prereg Part 2), RE-GATED on the quantity the
    mechanism CONSUMES: the per-bond ⟨T⟩ (and its remap consequence), NOT the gradient.

    🔴 CRITICAL RE-GATE (2026-07-04, orchestrator): the original gate read the field
    GRADIENT (d⟨T⟩/dx), which is trivially zero for a uniform traveling wave, and
    called that "vanishes." But the stiffening path _remap_at_signed_T reads T ITSELF
    (k_shear_eff = S_shear + T/ℓ). The matched CW traveling wave carries a PERSISTENT,
    UNIFORM per-bond ⟨T⟩ = (k_a/ℓ)y0² -- identical in kind to the confined hum -- and
    fed through the SAME remap it stiffens ρ' identically. So control (i) does NOT
    vanish in the consumed observable. Rule 11: report the negative, no rescue.

    (i) traveling wave on a MATCHED chain -- gated on the per-bond ⟨T⟩, TWO GENUINELY
        INDEPENDENT paths:
          path A (phasor, Γ=0):        ⟨T⟩_bond from field_from_phasor
          path B (Γ-FREE ABCD-propag): ⟨T⟩_bond from field_from_abcd_propagation (no Γ)
        Both must AGREE on the per-bond ⟨T⟩ value (real reconcile). The vanish test is
        on ⟨T⟩ (does the traveling wave leave a persistent per-bond tension?), NOT on
        the gradient. The remap consequence (ρ' shift) is reported.
    (ii) standing wave between reflecting terminations -- gated on the FIELD-INTEGRAND
        antinode value (not the |Γ|=1 tautology): the sampled antinode ⟨T⟩ must reach
        the constructive-interference value 4·(k_a/ℓ)y0² (MAJOR-2 fix).
    """
    y0 = 1.0  # unit hum amplitude for the control (the RATIO is the datum)
    ell = 1.0
    A_axial = A_CORE_SQRT_ALPHA
    A_shear_op = 0.99479

    # -- (i) traveling wave on the MATCHED chain, RE-GATED on ⟨T⟩ ----------------
    gamma_matched = complex(cascade_gamma(np.full(20, Z_0), Z_0, theta))
    # path A: phasor (Γ=0) per-bond ⟨T⟩
    fieldA = field_from_phasor(gamma_matched, theta, y0=y0, ell=ell)
    T_bond_phasor = fieldA["T_local_mean"]
    # path B: GENUINELY Γ-FREE ABCD propagation per-bond ⟨T⟩ (no Γ input)
    fieldB = field_from_abcd_propagation(theta, y0=y0, ell=ell)
    T_bond_gamma_free = fieldB["T_bond_mean"]

    # REAL reconcile (MAJOR-1): the phasor path and the Γ-FREE ABCD-propagation path
    # must agree on the per-bond ⟨T⟩ value. These are DIFFERENT assemblies (a Γ-
    # parameterized phasor vs a forward-state ABCD cascade); a genuine bug diverges
    # them. Both report ⟨T⟩ = 1.0 -- and CRUCIALLY, they agree it is NONZERO.
    tol = 1e-9
    reconcile_rel = abs(T_bond_phasor - T_bond_gamma_free) / (abs(T_bond_gamma_free) + 1e-30)
    if not reconcile_matched_T(T_bond_phasor, T_bond_gamma_free, tol):
        raise DiscrepantHalt(
            f"matched-line per-bond ⟨T⟩ RECONCILE FAILED: phasor path ⟨T⟩="
            f"{T_bond_phasor:.9f} vs Γ-FREE ABCD-propagation ⟨T⟩={T_bond_gamma_free:.9f} "
            f"(rel={reconcile_rel:.2e}>{tol:.0e}) -- the two independent paths diverge"
        )

    # the CONSUMED consequence: feed the matched-wave per-bond ⟨T⟩ through the SAME
    # remap the mechanism uses. If the traveling wave stiffens ρ' like the hum does,
    # the carrier as formulated cannot distinguish matter from radiation.
    rem_cold = _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, 0.0)
    rem_travel = _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, +T_bond_gamma_free)
    T_vanishes = bool(abs(T_bond_gamma_free) < tol)   # the HONEST gate: ⟨T⟩→0?

    # -- (ii) standing wave between reflecting terminations, gated on the FIELD ------
    gamma_short = complex(cascade_gamma(np.full(20, Z_0), 0.0, theta))   # Γ=−1 wall
    field_short = field_from_phasor(gamma_short, theta, y0=y0, ell=ell)
    # MAJOR-2: gate on the FIELD-INTEGRAND antinode (sampled + analytic agree), not the
    # algebraic |Γ|=1 restatement. The analytic antinode feeds the check; the sampled
    # grid value is reported alongside to show the field integrand actually reaches it.
    T_part1_unit = resonant_tension_leading(y0)          # (k_a/ℓ) y0²
    T_antinode_expected = 4.0 * T_part1_unit             # constructive |Γ|=1 antinode
    recovers = (abs(field_short["T_antinode_analytic"] - T_antinode_expected)
                < 1e-9 * T_antinode_expected
                and abs(field_short["T_local_max"] - T_antinode_expected)
                < 1e-3 * T_antinode_expected)

    return {
        "theta": theta,
        # (i) matched line -- HONESTLY gated on the CONSUMED per-bond ⟨T⟩
        "i_matched": {
            "T_bond_phasor": T_bond_phasor,
            "T_bond_gamma_free": T_bond_gamma_free,
            "T_bond_reconcile_rel": float(reconcile_rel),
            "T_vanishes": T_vanishes,           # the HONEST gate -- does ⟨T⟩→0?
            "rho_prime_cold": rem_cold["rho_prime"],
            "rho_prime_under_traveling_wave": rem_travel["rho_prime"],
            "radiation_stiffens": bool(
                abs(rem_travel["rho_prime"] - rem_cold["rho_prime"]) > 1e-3),
            "note": "the matched traveling wave carries a PERSISTENT per-bond ⟨T⟩ that "
            "the remap consumes -> ρ' shifts (radiation stiffens). ⟨T⟩ does NOT vanish.",
        },
        # (ii) standing wave -- gated on the field-integrand antinode (MAJOR-2)
        "ii_standing": {
            "gamma_mag_short": float(abs(gamma_short)),
            "T_antinode_field_analytic": field_short["T_antinode_analytic"],
            "T_antinode_field_grid": field_short["T_local_max"],
            "T_antinode_expected_part1": float(T_antinode_expected),
            "T_bond_avg_standing": field_short["T_bond_avg_analytic"],
            "recovers_part1_law": bool(recovers),
        },
    }


# ===========================================================================
# GATES -- positive controls (HALT-gated) + the DISCREPANT-HALT reconcile
# ===========================================================================
class DiscrepantHalt(RuntimeError):
    """Raised when the two INDEPENDENT matched-line reaction paths disagree beyond tol.

    A REAL reconcile (not a re-check of a defining identity): the Gamma-read and the
    field-space momentum integral are different assemblies. Synthetic-trigger tested.
    """


def reconcile_matched_T(T_phasor: float, T_gamma_free: float, tol: float = 1e-9) -> bool:
    """The DISCREPANT-HALT reconcile core (extracted so synthetic tests can trigger it).

    The two GENUINELY INDEPENDENT matched-line per-bond ⟨T⟩ paths must AGREE on the VALUE
    (relative), not merely on a shared boolean: |T_phasor − T_gamma_free|/|T_gamma_free|
    ≤ tol. A genuine bug diverging them ⟹ returns False ⟹ HALT. These are DIFFERENT
    assemblies: T_phasor is the Γ-parameterized incident+reflected phasor mean;
    T_gamma_free is a forward-state abcd_lossless_line CASCADE with NO Γ input.

    🔴 SUPERSEDES the old reconcile_matched_reaction (2026-07-04, MAJOR-1): that gate
    reconciled the Γ-read against a field path that was ALGEBRAICALLY 1.4244·|Γ| -- i.e.
    the SAME Γ, rescaled. It could never disagree (the 4th recurrence of the reconcile-
    gate defect). This value-reconcile on two genuinely-independent ⟨T⟩ computations
    can disagree.
    """
    return abs(T_phasor - T_gamma_free) / (abs(T_gamma_free) + 1e-30) <= tol


def run_positive_controls() -> dict:
    """PC-half / PC-lead-vs-exact / PC-noload / PC-matched / PC-reflect (HALT-gated)."""
    results = {}

    # PC-half: the DERIVED ½ + ⟨T⟩ law, every sympy residual exact-zero
    bb = symbolic_backbone()
    results["PC_half_residuals"] = {k: str(v) for k, v in bb.items()}
    results["PC_half_ok"] = bool(all(v == 0 for v in bb.values()))

    # PC-lead-vs-exact: leading ⟨T⟩ tracks the exact cycle-average at small y0 (→0),
    # and is a strict UPPER BOUND everywhere in-regime (concavity in y²).
    ys = np.array([1e-3, 1e-2, 0.05, 0.14, 0.42])
    lead = np.array([resonant_tension_leading(float(y)) for y in ys])
    exact = np.array([resonant_tension_exact(float(y)) for y in ys])
    results["PC_lead_vs_exact_smally_rel_dev"] = float((lead[0] - exact[0]) / exact[0])
    results["PC_lead_is_upper_bound"] = bool(np.all(lead >= exact - 1e-12))
    results["PC_lead_vs_exact_ok"] = bool(
        (lead[0] - exact[0]) / exact[0] < 1e-4 and np.all(lead >= exact - 1e-12)
    )

    # PC-noload: y0→0 ⟹ ⟨T⟩→0 (both laws), the no-hum anchor
    results["PC_noload_lead"] = float(resonant_tension_leading(0.0))
    results["PC_noload_exact"] = float(resonant_tension_exact(0.0))
    results["PC_noload_ok"] = bool(
        resonant_tension_leading(0.0) == 0.0 and resonant_tension_exact(0.0) == 0.0
    )

    # PC-matched: cascade_gamma on a Z_0-uniform matched chain ⟹ |Γ|<1e-12 (KNOWN-zero
    # reflection through the imported callable -- the matched-line positive control)
    gm = matched_line_reflection(0.3)
    results["PC_matched_gamma_mag"] = float(gm)
    results["PC_matched_ok"] = bool(gm < 1e-12)

    # PC-reflect: cascade_gamma on a shorted/open termination ⟹ |Γ|=1 (KNOWN-nonzero
    # reflection -- proves the instrument reads a reflecting wall; liveness Step 3.8a)
    gs = reflecting_termination_reflection(0.3, "short")
    go = reflecting_termination_reflection(0.3, "open")
    results["PC_reflect_gamma_short"] = float(gs)
    results["PC_reflect_gamma_open"] = float(go)
    results["PC_reflect_ok"] = bool(abs(gs - 1.0) < 1e-9 and abs(go - 1.0) < 1e-9)

    # PC-gammafree-live: the Γ-free ABCD-propagation path returns a NONZERO per-bond ⟨T⟩
    # for a traveling wave -- proves the CONSUMED observable (⟨T⟩) can be nonzero on this
    # path (the liveness that makes an "⟨T⟩ vanishes" verdict meaningful). If this were
    # forced to zero by construction, the (i)-vanish test would be blind (Step 3.8a).
    tbf = field_from_abcd_propagation(0.3, y0=1.0)["T_bond_mean"]
    results["PC_gammafree_travel_T"] = float(tbf)
    results["PC_gammafree_live_ok"] = bool(tbf > 0.9)   # ⟨T⟩=(k_a/ℓ)y0²=1.0 expected

    results["ALL_PC_PASS"] = bool(all(results[k] for k in results if k.endswith("_ok")))
    return results


# ===========================================================================
# BIN SELECTOR (no fall-through else) + main()
# ===========================================================================
def select_bin(part2: dict) -> dict:
    """Frozen bins (prereg): RESONANT-CARRIER-DERIVED / RADIATION-CONTAMINATED /
    DISCRIMINATOR-UNDERDETERMINED. No fall-through else.

    Routing (verbatim from the FROZEN prereg; the bins stay frozen, only the
    OBSERVABLE they read was corrected per the orchestrator CRITICAL -- that is not a
    bin edit):
      (i)-vanishes-in-⟨T⟩ AND (ii)-recovers  -> RESONANT-CARRIER-DERIVED
      (i)-does-NOT-vanish-in-⟨T⟩              -> RADIATION-CONTAMINATED
      separation-ill-defined                 -> DISCRIMINATOR-UNDERDETERMINED

    🔴 The (i) test now reads the CONSUMED per-bond ⟨T⟩ (i_matched["T_vanishes"]), NOT
    the gradient. The matched traveling wave leaves a persistent ⟨T⟩ ⟹ (i) does NOT
    vanish ⟹ [RADIATION-CONTAMINATED] (the honest negative; Rule 11, no rescue).
    """
    i = part2["i_matched"]
    ii = part2["ii_standing"]

    i_vanishes = bool(i["T_vanishes"])          # the CONSUMED observable (⟨T⟩), not grad
    ii_recovers = bool(ii["recovers_part1_law"])

    if not i_vanishes:
        verdict = "RADIATION-CONTAMINATED"
        reason = ("the traveling-wave control (i) does NOT vanish in the CONSUMED "
                  "observable: a matched CW traveling wave carries a PERSISTENT per-bond "
                  "⟨T⟩ (both independent paths agree, phasor & Γ-free ABCD) that the "
                  "#526 remap consumes (k_shear_eff=S_shear+T/ℓ), stiffening ρ' "
                  "identically in kind to the confined hum -> the resonant-tension "
                  "carrier as formulated cannot distinguish matter from radiation and "
                  "CONTRADICTS #518 §7 -> the mechanism DIES (Rule 11, no rescue)")
    elif i_vanishes and ii_recovers:
        verdict = "RESONANT-CARRIER-DERIVED"
        reason = ("(i) matched-line per-bond ⟨T⟩ vanishes (both independent paths) AND "
                  "(ii) reflecting-termination antinode recovers the Part-1 tent-law "
                  "⟨T⟩ -> the plucking fork RESOLVES: carrier = the confined resonance")
    else:
        verdict = "DISCRIMINATOR-UNDERDETERMINED"
        reason = ("(i) vanishes in ⟨T⟩ but (ii) does not cleanly recover the Part-1 law "
                  "-- the standing/traveling separation needs structure the linear #525 "
                  "TL does not supply; defer")

    return {"verdict": verdict, "reason": reason,
            "i_vanishes_in_T": i_vanishes, "ii_recovers": ii_recovers}


def _write(out: dict) -> None:
    outdir = Path(__file__).resolve().parent / "_output"
    outdir.mkdir(exist_ok=True)
    path = outdir / "resonant_tension_law.json"
    path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nwrote {path}")


def _knife_check(part1: dict) -> dict:
    """Knife: any re-banded matter-track edge landing ON a canon value gets coincidence
    treatment. Visible targets: 2/7, 9.7734, 7.10 cap, ρ'=2, arc* edges, 1/√α."""
    mt = part1["matter_track"]
    rp_band = mt["rho_prime_band_exact"] or [float("nan"), float("nan")]
    nu_band = mt["nu_band"] or [float("nan"), float("nan")]
    targets = {"nu_2_7": 2.0 / 7.0, "rho_star_9p7734": 9.7734, "rho_2": 2.0,
               "cap_7p10": 7.10}
    lands = {}
    for name, tgt in targets.items():
        in_rp = rp_band[0] - 1e-3 <= tgt <= rp_band[1] + 1e-3
        in_nu = nu_band[0] - 1e-3 <= tgt <= nu_band[1] + 1e-3
        lands[name] = {"target": tgt, "in_rho_prime_band": bool(in_rp),
                       "in_nu_band": bool(in_nu)}
    return {
        "rho_prime_band_exact": rp_band, "nu_band": nu_band, "targets": lands,
        "identity_twins": {
            "rho_prime": 9.7734, "nu": 2.0 / 7.0,
            "caveat": "SYMMETRIC (MAJOR-3): BOTH the y0→0 ρ'→9.7734 AND ν→2/7 are the "
            "SAME identity -- ⟨T⟩→0 recovers the unstressed #518 crossing, where ρ*=9.7734 "
            "and ν=2/7 co-locate by construction. Neither is a re-banded landing; both are "
            "LABELED identities and EXCLUDED from the reported interior band. (The prior "
            "doc caveated ρ' but not ν -- asymmetric knife, now corrected.)",
        },
        "note": "the y0→0 twins ρ'→9.7734 / ν→2/7 are the unstressed-crossing IDENTITY "
        "(T→0 ⟹ unshifted cold remap), NOT re-banded landings -- symmetrically knifed and "
        "excluded from the band. The reported INTERIOR (y0>0) rho' band does not reach "
        "rho'=2. KNIFE=noise on both identity twins; no interior edge lands on a "
        "distinguished value. (Moot for the verdict: the carrier DIED at Part 2 -- the "
        "matter re-band is reported for completeness, not as a live result.)",
    }


def main() -> int:
    out = {
        "title": "THE RESONANT TIME-AVERAGED TENSION LAW + the radiation control",
        "prereg": "research/2026-07-04_resonant-tension-law_prereg_FROZEN.md",
        "grant_ruling": "the bond AUTO-RESONATES (not plucked); the tank's own hum "
        "(⟨y⟩=0, ⟨y²⟩>0) IS the bias; quadratic pluck law ⟹ time-averaged tension "
        "survives (resonant-lc-solitons.md:10).",
        "scope": "Part 1: the resonant ⟨T⟩ law + matter re-band. Part 2: the "
        "make-or-break radiation control (matched-line vanish vs standing-wave recover).",
    }
    print("=" * 78)
    print("THE RESONANT TENSION LAW + RADIATION CONTROL (resolves the #527 plucker fork)")
    print("=" * 78)

    # ---- (0) POSITIVE CONTROLS (HALT if fail) ----------------------------
    pc = run_positive_controls()
    out["positive_controls"] = pc
    print("(0) POSITIVE CONTROLS (HALT if fail):")
    for k in ("PC_half_ok", "PC_lead_vs_exact_ok", "PC_noload_ok",
              "PC_matched_ok", "PC_reflect_ok", "PC_gammafree_live_ok"):
        print(f"  {k:22s} = {pc[k]}")
    print(f"  ALL_PC_PASS = {pc['ALL_PC_PASS']}")
    if not pc["ALL_PC_PASS"]:
        print("\nHALT: positive controls FAILED — no verdict.")
        _write(out)
        return 1

    pos_r, bonds_r, rho_r = srs_primitive("right")

    # ---- (1) PART 1 — the resonant tension law + matter re-band ----------
    part1 = part1_law_and_band(pos_r, bonds_r, rho_r)
    out["part1"] = part1
    mt = part1["matter_track"]
    print("\n(1) PART 1 — the resonant ⟨T⟩ law (leading + exact), matter re-banded:")
    print(f"    ⟨T⟩ = (2k_a/ℓ)⟨y²⟩ = (k_a/ℓ)y0²  (⟨sin²⟩=½ DERIVED)")
    print(f"    leading law is an UPPER BOUND; worst over-prediction "
          f"{mt['worst_leading_over_exact_rel_dev']:+.1%} (elastica edge)")
    print(f"    matter track ρ' (exact) band: {mt['rho_prime_band_exact']}")
    print(f"    matter track ν band:          {mt['nu_band']}")
    for edge in ("lo_elastica", "hi_tent"):
        b = part1["band"][edge]
        print(f"    -- {edge} (arc*={b['arc_star']}, y0_max={b['y0_in_regime_max']:.4f}) --")
        for r in b["rows"]:
            rp = r["rho_prime_exact"]
            rps = "inf" if not np.isfinite(rp) else f"{rp:.4f}"
            print(f"       y0={r['y0']:.4f}: ⟨T⟩_lead={r['T_avg_leading']:.5e} "
                  f"⟨T⟩_exact={r['T_avg_exact']:.5e} dev={r['leading_over_exact_rel_dev']:+.2%} "
                  f"ρ'={rps:>8s} ν={r['nu_exact']:+.5f}")

    # ---- (2) PART 2 — the radiation control (DISCREPANT-HALT reachable) --
    # RE-GATED (CRITICAL) on the CONSUMED per-bond ⟨T⟩, not the gradient.
    try:
        part2 = part2_radiation_control(pos_r, bonds_r, rho_r)
    except DiscrepantHalt as e:
        out["verdict"] = {"verdict": "DISCREPANT-HALT", "detail": str(e)}
        print(f"\nDISCREPANT-HALT: {e}")
        _write(out)
        return 2
    out["part2"] = part2
    i, ii = part2["i_matched"], part2["ii_standing"]
    print("\n(2) PART 2 — the radiation control (make-or-break; RE-GATED on ⟨T⟩):")
    print(f"    (i)  MATCHED line per-bond ⟨T⟩: phasor={i['T_bond_phasor']:.6f}, "
          f"Γ-FREE ABCD={i['T_bond_gamma_free']:.6f} "
          f"(reconcile rel={i['T_bond_reconcile_rel']:.1e}) ⟹ ⟨T⟩ vanishes={i['T_vanishes']}")
    print(f"         remap consequence: ρ'_cold={i['rho_prime_cold']:.4f} → "
          f"ρ'_under_traveling_wave={i['rho_prime_under_traveling_wave']:.4f} "
          f"(radiation stiffens={i['radiation_stiffens']})")
    print(f"    (ii) STANDING wave (Γ=−1): antinode ⟨T⟩={ii['T_antinode_field_analytic']:.4f} "
          f"(grid={ii['T_antinode_field_grid']:.4f}) vs 4×Part-1="
          f"{ii['T_antinode_expected_part1']:.4f} ⟹ recovers={ii['recovers_part1_law']}")

    # ---- (3) THE BIN (no fall-through else) ------------------------------
    verdict = select_bin(part2)
    out["verdict"] = verdict
    print(f"\n(3) VERDICT: [{verdict['verdict']}] — {verdict['reason']}")

    # ---- (4) THE KNIFE (symmetric identity twins; moot — carrier died) --
    out["knife"] = _knife_check(part1)
    print(f"\n(4) KNIFE: interior ρ' band {out['knife']['rho_prime_band_exact']}; "
          f"ρ'=2 in band: {out['knife']['targets']['rho_2']['in_rho_prime_band']}; "
          f"y0→0 twins ρ'→9.7734 AND ν→2/7 are the SAME identity (symmetric, labeled).")
    print("    (moot for the verdict: the carrier DIED at Part 2 — matter re-band "
          "reported for completeness only.)")

    _write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
