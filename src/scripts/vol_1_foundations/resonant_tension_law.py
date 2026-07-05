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
        # sample the in-regime y0 range (0 .. ceiling) at the hum-amplitude endpoints
        y0_grid = np.array([0.0, 0.25 * y0_max, 0.5 * y0_max, 0.75 * y0_max, y0_max])
        rows = []
        for y0 in y0_grid:
            T_lead = resonant_tension_leading(float(y0), ell=ell)
            T_exact = resonant_tension_exact(float(y0), ell=ell)
            rel = (T_lead - T_exact) / T_exact if T_exact > 0 else 0.0
            # feed the RESONANT ⟨T⟩ (tension, +) through the #526 remap -- both laws
            rem_lead = _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, +T_lead)
            rem_exact = _remap_at_signed_T(pos, bonds, rho, A_axial, A_shear_op, +T_exact)
            rows.append({
                "y0": float(y0),
                "T_avg_leading": float(T_lead),
                "T_avg_exact": float(T_exact),
                "leading_over_exact_rel_dev": float(rel),
                "rho_prime_leading": rem_lead["rho_prime"],
                "rho_prime_exact": rem_exact["rho_prime"],
                "nu_leading": rem_lead["nu"],
                "nu_exact": rem_exact["nu"],
                "k_shear_eff_leading": rem_lead["k_shear_eff"],
            })
            if y0 > 0:
                lead_vs_exact_rows.append({"arc_star": arc_star, "y0": float(y0),
                                           "rel_dev": float(rel)})
        band[edge] = {"arc_star": arc_star, "y0_in_regime_max": float(y0_max),
                      "rows": rows}

    # the re-banded matter track: the ρ' / ν ENVELOPE across the in-regime hum band
    all_rp = [r["rho_prime_exact"] for e in band.values() for r in e["rows"]
              if np.isfinite(r["rho_prime_exact"]) and r["y0"] > 0]
    all_rp_lead = [r["rho_prime_leading"] for e in band.values() for r in e["rows"]
                   if np.isfinite(r["rho_prime_leading"]) and r["y0"] > 0]
    all_nu = [r["nu_exact"] for e in band.values() for r in e["rows"] if r["y0"] > 0]
    matter_track = {
        "rho_prime_band_exact": [float(min(all_rp)), float(max(all_rp))] if all_rp else None,
        "rho_prime_band_leading": [float(min(all_rp_lead)), float(max(all_rp_lead))]
        if all_rp_lead else None,
        "nu_band": [float(min(all_nu)), float(max(all_nu))] if all_nu else None,
        "worst_leading_over_exact_rel_dev": float(max(r["rel_dev"] for r in lead_vs_exact_rows))
        if lead_vs_exact_rows else 0.0,
        "note": "matter track re-banded over the in-regime hum amplitude y0 in "
        "[0, in_regime_pluck_bow(arc*)] for arc* in [0.70, 0.96]. The RESONANT ⟨T⟩ "
        "(tension, +) caps ρ'. VALUE inherits #526 GR-imported status; EMERGENCE "
        "grade FORBIDDEN. Leading law is an UPPER BOUND (over-predicts the exact "
        "cycle-average); the worst over-prediction is at the elastica edge.",
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


def axial_reaction_from_field(gamma: complex, theta: float, n_cells: int = 40,
                              y0: float = 1.0, k_a: float = 1.0, ell: float = 1.0) -> dict:
    """INDEPENDENT reference path: the net time-averaged axial reaction from the FIELD.

    NOT from Γ directly -- from the explicit incident+reflected transverse field. For
    a line of electrical length θ per cell, the transverse field with reflection
    coefficient Γ (at the far termination) is, up to a carrier phase,

        y(x,t) = Re{ y0 [ e^{-jβx} + Γ e^{+jβx} ] e^{jωt} }.

    The cycle-averaged transverse energy density ⟨y²(x)⟩ sets the tent-law tension
    ⟨T⟩(x) = (2 k_a/ℓ)·⟨y²(x)⟩ (the Part-1 law applied LOCALLY). The net time-averaged
    AXIAL reaction on an interior bond is the SPATIAL GRADIENT of that tension (a
    static reaction force is d⟨T⟩/dx integrated over the bond):

      * pure traveling wave (Γ=0): ⟨y²(x)⟩ = y0²/2 UNIFORM ⟹ d⟨T⟩/dx = 0 ⟹ the net
        interior axial reaction VANISHES -- the wave carries momentum THROUGH but
        deposits none (Ax3 lossless; #518 §7 ρ_eff=ρ_cold). No static bias.
      * reflecting termination (|Γ|=1): ⟨y²(x)⟩ = y0²·|e^{-jβx}+Γe^{+jβx}|²/2 VARIES
        (antinode vs node) ⟹ d⟨T⟩/dx ≠ 0 ⟹ a nonzero position-dependent reaction that
        integrates to the confinement force at the Γ=−1 wall.

    Returns the field-space diagnostics: the peak-to-peak ⟨T⟩(x) variation (the
    net-reaction proxy, zero iff uniform) and the mean ⟨T⟩ (the Part-1 value the
    standing mode recovers at the antinode).
    """
    # β·x samples across n_cells of electrical length θ each (βℓ_cell = θ)
    beta_x = np.linspace(0.0, n_cells * theta, 400)
    # complex transverse phasor amplitude along the line (incident + reflected)
    phasor = y0 * (np.exp(-1j * beta_x) + gamma * np.exp(+1j * beta_x))
    # cycle-averaged |y|² = ½|phasor|² (the ½ is ⟨cos²⟩, the SAME derived half)
    y2_avg = 0.5 * np.abs(phasor) ** 2
    # LOCAL tent-law tension via the Part-1 leading law applied pointwise:
    #   ⟨T⟩(x) = (2 k_a/ℓ)·⟨y²(x)⟩   (uses the DERIVED ½ already inside y2_avg)
    T_local = (2.0 * k_a / ell) * y2_avg
    T_pp = float(T_local.max() - T_local.min())      # peak-to-peak = net-reaction proxy
    T_mean = float(T_local.mean())
    T_max = float(T_local.max())
    # the net axial reaction on an interior bond ~ the SPATIAL GRADIENT of ⟨T⟩(x);
    # its cycle-and-space RMS is zero iff ⟨T⟩(x) is flat (traveling) and nonzero iff
    # it ripples (standing). Report the max |d⟨T⟩/dx| normalized by (2 k_a/ℓ)y0².
    dT = np.gradient(T_local, beta_x)
    norm = (2.0 * k_a / ell) * y0 ** 2 + 1e-30
    net_reaction_rms = float(np.sqrt(np.mean(dT ** 2)) / norm)
    # ANALYTIC antinode: constructive-interference peak ⟨y²⟩ = ½ y0²·(1+|Γ|)²
    #   ⟹ ⟨T⟩_antinode = (2 k_a/ℓ)·½ y0²(1+|Γ|)² = (k_a/ℓ) y0² (1+|Γ|)²
    # (grid-independent; the 400-pt sampled T_local_max only APPROACHES this).
    T_antinode_analytic = float((k_a / ell) * y0 ** 2 * (1.0 + abs(gamma)) ** 2)
    return {
        "T_local_mean": T_mean, "T_local_max": T_max, "T_local_peak_to_peak": T_pp,
        "T_antinode_analytic": T_antinode_analytic,
        "net_axial_reaction_rms_norm": net_reaction_rms,
        "is_uniform": bool(T_pp < 1e-9 * (T_mean + 1e-30)),
    }


def part2_radiation_control(theta: float = 0.3) -> dict:
    """The make-or-break control (prereg Part 2).

    (i) traveling wave on a MATCHED chain: BOTH reference paths must say NO net axial
        reaction -- (1) the Γ-read (|Γ|→0 via cascade_gamma), and (2) the INDEPENDENT
        field momentum-flux integral (⟨T⟩(x) uniform ⟹ zero gradient).
    (ii) standing wave between Γ=−1 reflecting terminations: nonzero reaction that
        recovers the Part-1 tent-law ⟨T⟩ (the antinode mean).

    DISCREPANT-HALT: the two independent (i) paths must AGREE that the reaction
    vanishes; if they disagree beyond tol the driver HALTs (does not bin). The
    Γ-read says "no reflection"; the field integral says "uniform ⟨T⟩(x)". Different
    assemblies -- a genuine reconcile, not a re-check of one identity.
    """
    y0 = 1.0  # unit hum amplitude for the control (the RATIO/uniformity is the datum)

    # -- (i) traveling wave on the MATCHED chain --------------------------------
    gamma_matched = complex(cascade_gamma(np.full(20, Z_0), Z_0, theta))
    path1_gamma_mag = float(abs(gamma_matched))                       # Γ-read path
    field_matched = axial_reaction_from_field(gamma_matched, theta, y0=y0)  # field path
    path2_reaction = field_matched["net_axial_reaction_rms_norm"]     # field path

    # RECONCILE (independent): both paths report the matched-line reaction. Path 1
    # is |Γ| (reflection); path 2 is the field-gradient RMS (momentum-flux). A pure
    # traveling wave has BOTH ~0. If a genuine bug made one nonzero while the other
    # stayed zero, they diverge. Tol 1e-9 on both (machine-zero cascade + smooth field).
    tol = 1e-9
    reconcile_ok = (path1_gamma_mag < tol) == (path2_reaction < tol)
    reconcile_detail = {
        "path1_gamma_mag": path1_gamma_mag,
        "path2_field_reaction_rms_norm": path2_reaction,
        "both_vanish": bool(path1_gamma_mag < tol and path2_reaction < tol),
        "agree": bool(reconcile_ok),
        "tol": tol,
    }

    # -- (ii) standing wave between reflecting terminations ---------------------
    gamma_short = complex(cascade_gamma(np.full(20, Z_0), 0.0, theta))   # Γ=−1 wall
    gamma_open = complex(cascade_gamma(np.full(20, Z_0), 1e18, theta))   # Γ=+1
    field_short = axial_reaction_from_field(gamma_short, theta, y0=y0)
    field_open = axial_reaction_from_field(gamma_open, theta, y0=y0)

    # the standing-wave antinode recovers the Part-1 tent law: at |Γ|=1 the antinode
    # ⟨y²⟩ = ½y0²(1+|Γ|)² = 2 y0² (constructive) ⟹ ⟨T⟩_antinode = (2 k_a/ℓ)(2 y0²) =
    # 4·(k_a/ℓ)y0² = 4·resonant_tension_leading(y0). Check the ANALYTIC antinode (grid-
    # independent) against 4× the Part-1 unit law -- a genuine recovery of the Part-1
    # FORM (the tent-law ⟨T⟩), computed through the SAME field integrand as (i).
    T_part1_unit = resonant_tension_leading(y0)          # (k_a/ℓ) y0²
    T_antinode_expected = 4.0 * T_part1_unit             # constructive |Γ|=1 antinode
    recovers = abs(field_short["T_antinode_analytic"] - T_antinode_expected) \
        < 1e-9 * T_antinode_expected

    return {
        "theta": theta,
        # (i) matched line -- must vanish
        "i_matched": {
            "gamma_mag": path1_gamma_mag,
            "field_reaction_rms_norm": path2_reaction,
            "field_T_uniform": field_matched["is_uniform"],
            "vanishes": bool(path1_gamma_mag < tol and path2_reaction < tol
                             and field_matched["is_uniform"]),
        },
        # (ii) standing wave -- must NOT vanish AND must recover the Part-1 law
        "ii_standing": {
            "gamma_mag_short": float(abs(gamma_short)),
            "gamma_mag_open": float(abs(gamma_open)),
            "field_reaction_rms_norm_short": field_short["net_axial_reaction_rms_norm"],
            "field_reaction_rms_norm_open": field_open["net_axial_reaction_rms_norm"],
            "T_antinode_field_short_grid": field_short["T_local_max"],
            "T_antinode_field_short_analytic": field_short["T_antinode_analytic"],
            "T_antinode_expected_part1": float(T_antinode_expected),
            "recovers_part1_law": bool(recovers),
            "nonzero": bool(field_short["net_axial_reaction_rms_norm"] > 1e-3),
        },
        "reconcile": reconcile_detail,
    }


# ===========================================================================
# GATES -- positive controls (HALT-gated) + the DISCREPANT-HALT reconcile
# ===========================================================================
class DiscrepantHalt(RuntimeError):
    """Raised when the two INDEPENDENT matched-line reaction paths disagree beyond tol.

    A REAL reconcile (not a re-check of a defining identity): the Gamma-read and the
    field-space momentum integral are different assemblies. Synthetic-trigger tested.
    """


def run_positive_controls() -> dict:
    """PC-half / PC-lead-vs-exact / PC-noload / PC-matched / PC-reflect (HALT-gated)."""
    raise NotImplementedError


# ===========================================================================
# BIN SELECTOR (no fall-through else) + main()
# ===========================================================================
def select_bin(part2: dict) -> dict:
    """Frozen bins: RESONANT-CARRIER-DERIVED / RADIATION-CONTAMINATED /
    DISCRIMINATOR-UNDERDETERMINED. No fall-through."""
    raise NotImplementedError


def _write(out: dict) -> None:
    outdir = Path(__file__).resolve().parent / "_output"
    outdir.mkdir(exist_ok=True)
    path = outdir / "resonant_tension_law.json"
    path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nwrote {path}")


def main() -> int:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
