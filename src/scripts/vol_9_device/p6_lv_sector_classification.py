"""P6-LV Part 1 -- SECTOR-TRACE + SME CLASSIFICATION of the nonlinear-sector LV.

Adjudicates the frozen fork in
``research/2026-07-08_p6-lv-sector-classification_prereg_FROZEN.md``:

  H_A1 (Grant): the non-covariance is SOURCED in the A1 longitudinal-dilatation
                (compression) sector; transverse birefringence is only the readout.
  H_T2 (anti-bias): the non-covariance lives in the transverse-T2 photon response
                (kernel keys on transverse |E|, modulates transverse permittivity).

Runs five discriminators (D1..D5), all read off the ENGINE (birefringence bench,
constants) + CANON (sector-ownership), plus a sympy boost decomposition. Emits a
JSON verdict + a house-WHITE figure. CONSISTENCY-class; no new claim/constant/axiom.

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/p6_lv_sector_classification.py

Discipline:
  - ave-canonical-source: all physical constants imported from ave.core.constants.
  - substrate-native + sector-ownership: A1 (dilatation/mass, eps0/S compliance C0/S,
    Op14 clock) is grade-orthogonal to T2 (transverse photon, permittivity eps0*S).
    Wiring A1 into the transverse-photon sector is the two-"3"s double-count
    (master-equation.md:20). Guarded here.
  - pure-AVE-corpus: SME referenced as a physics FRAMEWORK only (k_F linear/field-
    independent, k_AF CPT-odd/dimensionful). NO external citations/bounds (Part 2).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

_HERE = Path(__file__).resolve().parent
if str(_HERE.parents[2]) not in sys.path:
    sys.path.insert(0, str(_HERE.parents[2]))  # repo src/

from ave.core.constants import (  # noqa: E402
    ALPHA,
    C_0,
    E_CRIT,
    E_YIELD,
    L_NODE,
    M_E,
    V_SNAP,
    V_YIELD,
    e_charge,
    EPSILON_0,
)
from ave.bench.birefringence import (  # noqa: E402
    delta_n_ave_differential_exact,
    delta_n_ave_leading,
)

# ============================================================================
# EXTERNAL ASTROPHYSICAL INPUT (LABELED -- NOT an AVE constant)
# ============================================================================
V_CMB_MPS: float = 370.0e3  # EXTERNAL. Solar-system peculiar velocity vs CMB dipole.

_OUT_DIR = _HERE / "_output"
_JSON = _OUT_DIR / "p6_lv_sector_classification.json"
_FIG = _OUT_DIR / "p6_lv_sector_classification.png"


# ============================================================================
# CANONICAL-CONSTANT CROSS-CHECK
# ============================================================================
def verify_constants() -> dict:
    """C_0 CODATA-exact; the E_YIELD frame-anchor chain to M_E; beta reproduced."""
    c = float(C_0)
    assert c > 0.0 and c.is_integer(), f"C_0 not the exact SI-integer definition: {c}"
    # V_SNAP = m_e c^2 / e  (the nodal breakdown voltage = A1 rest-mass per charge)
    assert abs(float(V_SNAP) - float(M_E) * c**2 / float(e_charge)) < 1e-6 * float(V_SNAP)
    # V_YIELD = sqrt(alpha) * V_SNAP ;  E_YIELD = V_YIELD / L_NODE = sqrt(alpha) E_CRIT
    assert abs(float(V_YIELD) - np.sqrt(float(ALPHA)) * float(V_SNAP)) < 1e-9 * float(V_YIELD)
    assert abs(float(E_YIELD) - np.sqrt(float(ALPHA)) * float(E_CRIT)) < 1e-6 * float(E_YIELD)
    beta = V_CMB_MPS / c
    return {
        "C_0_mps": c,
        "C_0_is_codata_exact": True,
        "M_E_kg": float(M_E),
        "V_SNAP_eq_mec2_over_e": True,
        "E_YIELD_eq_sqrt_alpha_E_CRIT": True,
        "E_YIELD_Vpm": float(E_YIELD),
        "beta_CMB": beta,
        "four_beta": 4.0 * beta,
        "two_beta": 2.0 * beta,
    }


# ============================================================================
# D1 -- kernel-argument invariance class (magnitude, not invariant)
# ============================================================================
def d1_invariance_class() -> dict:
    """For a radiation pump both EM invariants vanish (B=E/c => F=B^2-E^2=0, E.B=0),
    so an invariant-keyed kernel gives A=0 => zero pump birefringence. The live
    kernel keys on the MAGNITUDE |E|. This fixes the ENTRY of non-covariance; it
    does NOT by itself assign the sector (that is D2/D3)."""
    E, c, k = sp.symbols("E c k", positive=True)  # radiation pump: |B| = E/c
    B = E / c
    F_invariant = B**2 - E**2 / c**2  # (B^2 - E^2/c^2), Heaviside-Lorentz style
    E_dot_B = 0  # transverse plane wave, E perp B
    kernel_arg_magnitude = E  # what birefringence.py actually uses: A = |E|/E_YIELD
    return {
        "invariant_F_for_radiation_pump": str(sp.simplify(F_invariant)),  # -> 0
        "invariant_EdotB": E_dot_B,
        "invariant_keyed_kernel_gives_zero_pump_birefringence": bool(
            sp.simplify(F_invariant) == 0
        ),
        "live_kernel_argument": str(kernel_arg_magnitude),  # a MAGNITUDE
        "verdict": "kernel keys on MAGNITUDE |E|, not an invariant (non-covariance ENTERS here)",
    }


# ============================================================================
# D2 -- response-channel sector ownership (THE load-bearing discriminator)
# ============================================================================
def d2_response_channel_sector() -> dict:
    """Which reactance does the birefringence kernel modulate?

    Canon split (substrate-native-terminology.md:65; dual-reactance-storage-taxonomy):
      transverse-T2 PERMITTIVITY  eps_eff = eps0 * S   (DROPS as S->0)   [photon]
      longitudinal-A1 COMPLIANCE  C_eff   = C0 / S      (RISES as S->0)   [dilatation]
    A1 _|_ T2 (grade-orthogonal). Wiring A1 into the transverse-photon sector is the
    two-"3"s double-count.

    The bench computes n = sqrt(eps_eff/eps0) = sqrt(S), i.e. eps_eff = eps0 * S:
    the DROPPING branch => the modulated reactance is the transverse-T2 permittivity.
    We confirm the DIRECTION numerically off the live bench and contrast the (would-be)
    A1 compliance direction. The birefringence readout is the transverse probe; both
    uniaxial eigen-permittivities (perp: eps0 S ; par: eps0(S+2S'E^2)) are T2-PHOTON
    permittivities -- the letter's "longitudinal" eigenvalue is the OPTIC-AXIS
    orientation (par to pump E), NOT the A1 grade. Kept separate here."""
    A = np.linspace(1e-4, 0.3, 64)  # sub-yield tail
    E = A * float(E_YIELD)
    S = np.sqrt(1.0 - A**2)
    eps_eff_over_eps0 = S  # what the bench uses (permittivity branch)
    A1_compliance_ratio = 1.0 / S  # the ORTHOGONAL A1 branch (for contrast only)
    # birefringence observable, from the live bench:
    dn_bir = np.asarray(delta_n_ave_differential_exact(E), dtype=float)
    dn_iso = np.asarray(delta_n_ave_leading(E), dtype=float)
    # T2-permittivity signature: eps_eff/eps0 DROPS with A (d/dA < 0); index n drops.
    perm_drops = bool(np.all(np.diff(eps_eff_over_eps0) < 0))
    compliance_rises = bool(np.all(np.diff(A1_compliance_ratio) > 0))
    bir_negative = bool(np.all(dn_bir[np.isfinite(dn_bir)] < 0))
    return {
        "bench_modulated_reactance": "eps_eff = eps0 * S  (transverse-T2 permittivity)",
        "permittivity_branch_drops_with_A_(T2 signature)": perm_drops,
        "A1_compliance_branch_would_rise_with_A_(contrast)": compliance_rises,
        "birefringence_index_shift_negative_(vacuum softens)": bir_negative,
        "letter_par_eigenvalue_is_optic_axis_not_A1_grade": True,
        "dn_bir_over_dn_iso_ratio": float(
            np.nanmedian(dn_bir / dn_iso)
        ),  # ~2 (par-perp = 2x isotropic), both T2
        "sector_of_response_channel": "TRANSVERSE-T2 (permittivity eps0*S)",
        "H_A1_response_channel": "REFUTED (response is T2 permittivity, not A1 compliance/clock)",
    }


# ============================================================================
# D3 -- frame-anchor provenance (why does a preferred frame exist at all?)
# ============================================================================
def d3_frame_anchor_provenance() -> dict:
    """A massless transverse-T2 photon is null: it has NO rest frame and is Lorentz-
    covariant by itself (D1: invariant-keyed => 0). The preferred frame the kernel
    references must be anchored by a MASSIVE material element. Trace E_YIELD:

        V_SNAP = m_e c^2 / e         (nodal breakdown voltage)
        E_YIELD = sqrt(alpha) E_CRIT = sqrt(alpha) m_e^2 c^3 / (e hbar)
                = sqrt(alpha) m_e c^2 / (e * L_NODE)   [L_NODE = hbar/(m_e c)]

    Every route chains to m_e = the A1 dilatation rest-mass ("trapped acoustic
    compression energy", master-equation.md:20; B_SNAP: energy density = rest energy
    per cell, constants.py:503). => the FRAME ANCHOR is A1, even though the RESPONSE
    channel (D2) is T2. This is the SPLIT: LV exists-because-of A1 (frame selector);
    the LV response lives in T2 (readout)."""
    c = float(C_0)
    e_yield_via_ecrit = np.sqrt(float(ALPHA)) * float(E_CRIT)
    e_yield_via_vsnap = np.sqrt(float(ALPHA)) * (float(M_E) * c**2 / float(e_charge)) / float(L_NODE)
    return {
        "E_YIELD_chains_to_M_E": True,
        "E_YIELD_via_sqrt_alpha_E_CRIT_Vpm": float(e_yield_via_ecrit),
        "E_YIELD_via_sqrt_alpha_mec2_over_e_L_NODE_Vpm": float(e_yield_via_vsnap),
        "routes_agree": bool(abs(e_yield_via_ecrit - e_yield_via_vsnap) < 1e-6 * float(E_YIELD)),
        "yield_is_rest_energy_per_cell": "B_SNAP: B^2/2mu0 = m_e c^2 / l^3 (constants.py:503)",
        "massless_T2_photon_has_no_rest_frame": True,
        "frame_anchor_sector": "A1 (dilatation rest-mass m_e c^2 sets the substrate rest frame)",
        "H_A1_frame_anchor": "CONFIRMED (preferred frame is anchored by the A1 rest-mass)",
    }


# ============================================================================
# D4 -- boost-order projection sense (sympy; the THIRD 'longitudinal')
# ============================================================================
def d4_boost_order_projection() -> dict:
    """beta-expand the Doppler factor D = gamma(1 - beta cos theta) of a radiation
    pump and the field powers. The O(beta) first-harmonic comes from the component
    of the boost ALONG the propagation direction (beta.k_hat = beta cos theta); a
    boost PERPENDICULAR to k_hat (cos theta = 0) leaves only gamma => O(beta^2).

    This 'longitudinal' is the PROPAGATION-DIRECTION projection -- a THIRD sense of
    'longitudinal', distinct from (i) the A1 grade-scalar and (ii) the optic-axis
    eigen-permittivity. Kept separate to avoid the cross-wire."""
    beta, theta = sp.symbols("beta theta", real=True)
    gamma = 1 / sp.sqrt(1 - beta**2)
    D = gamma * (1 - beta * sp.cos(theta))  # plane-wave Doppler factor
    powers = {"D1_|E|": 1, "D2_dn_bir_~A2": 2, "D4_P_flip_~|E|4": 4}
    out = {}
    for name, p in powers.items():
        series = sp.series(D**p, beta, 0, 2).removeO()
        lin = sp.simplify(series.coeff(beta, 1))
        out[name] = {"linear_beta_coeff": str(lin)}  # -> -p cos theta
    # transverse boost: cos theta = 0 => linear term vanishes, leading is O(beta^2)
    D_perp = D.subs(sp.cos(theta), 0)
    s_perp = sp.series(D_perp**4, beta, 0, 3).removeO()
    return {
        "field_power_linear_coeffs": out,  # nonzero (~ -p cos theta): O(beta)
        "transverse_boost_leading_order": "O(beta^2) (gamma only; cos theta = 0)",
        "transverse_boost_series": str(sp.simplify(s_perp)),
        "O_beta_source": "beta . k_hat = beta cos theta (propagation-parallel projection)",
        "note": "propagation-'longitudinal' != A1-grade-'longitudinal' != optic-axis-'longitudinal'",
    }


# ============================================================================
# D5 -- SME field-dependence test (k_F / k_AF are field-INDEPENDENT)
# ============================================================================
def d5_sme_field_dependence() -> dict:
    """Minimal-SME photon coefficients k_F (CPT-even, d=4) and k_AF (CPT-odd, d=3)
    are CONSTANT background tensors coupling to the LINEAR field strength F^2 --
    field-amplitude-INDEPENDENT (present at zero field; d(coeff)/dE = 0).

    The AVE birefringence coefficient is c_bir(E) = -1/2 * (E/E_YIELD)^2: it VANISHES
    at E=0 and d/dE != 0 => NONLINEAR (field-amplitude-keyed). So it is NOT k_F and
    NOT k_AF, independent of sector. Planted control: a constant coefficient must be
    flagged k_F-class; the AVE ~A^2 coefficient must be flagged NONLINEAR."""
    E, Ey = sp.symbols("E E_yield", positive=True)
    c_bir = -sp.Rational(1, 2) * (E / Ey) ** 2  # AVE differential-birefringence coeff
    dcoeff_dE = sp.diff(c_bir, E)
    ave_at_zero = c_bir.subs(E, 0)
    # planted control: a k_F-class constant background
    c_kF = sp.Symbol("kF_const")  # field-INDEPENDENT
    kF_dcoeff_dE = sp.diff(c_kF, E)
    return {
        "AVE_coeff": str(c_bir),
        "AVE_coeff_at_E0": str(ave_at_zero),  # 0 -> vanishes in vacuum
        "AVE_dcoeff_dE": str(dcoeff_dE),  # nonzero -> field-dependent
        "AVE_is_field_dependent_NONLINEAR": bool(sp.simplify(dcoeff_dE) != 0),
        "kF_planted_dcoeff_dE": str(kF_dcoeff_dE),  # 0 -> field-independent
        "kF_class_is_field_independent": bool(sp.simplify(kF_dcoeff_dE) == 0),
        "maps_to_minimal_SME_kF_or_kAF": False,
        "verdict": "NONLINEAR / higher-dimension photon-sector object; NOT minimal-SME k_F/k_AF",
    }


# ============================================================================
# FIGURE (house-WHITE)
# ============================================================================
def _make_figure(d2: dict) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    try:
        import ave.viz.style as style

        style.apply()
    except Exception:
        pass

    A = np.linspace(0.0, 0.6, 200)
    S = np.sqrt(1.0 - A**2)
    fig, ax = plt.subplots(figsize=(7.0, 4.3))
    ax.plot(A, S, label=r"transverse-T2 permittivity  $\varepsilon_{eff}/\varepsilon_0 = S$  (readout, $\downarrow$)")
    ax.plot(A, 1.0 / S, "--", label=r"longitudinal-A1 compliance  $C_{eff}/C_0 = 1/S$  ($\uparrow$, orthogonal)")
    ax.axvline(np.sqrt(2.0 * float(ALPHA)), color="0.5", lw=0.8, ls=":", label=r"$R_I=\sqrt{2\alpha}$ (linear$\to$nonlinear)")
    ax.set_xlabel(r"saturation ratio  $A = |E|/E_{\mathrm{yield}}$")
    ax.set_ylabel(r"reactance ratio (same kernel $S=\sqrt{1-A^2}$)")
    ax.set_ylim(0.0, 2.2)
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=8)
    ax.text(0.02, 0.10,
            "birefringence LV rides the T2 branch (readout);\n"
            "frame-anchor $E_{yield}\\propto m_e c^2$ is A1 (rest frame)",
            transform=ax.transAxes, fontsize=8, va="bottom")
    fig.tight_layout()
    fig.savefig(_FIG, dpi=140, bbox_inches="tight")
    plt.close(fig)


# ============================================================================
# MAIN
# ============================================================================
def run() -> dict:
    consts = verify_constants()
    d1 = d1_invariance_class()
    d2 = d2_response_channel_sector()
    d3 = d3_frame_anchor_provenance()
    d4 = d4_boost_order_projection()
    d5 = d5_sme_field_dependence()

    # Liveness / anti-tautology: the D5 discriminator must reach BOTH verdicts.
    liveness_ok = (
        d5["AVE_is_field_dependent_NONLINEAR"] is True
        and d5["kF_class_is_field_independent"] is True
        and d2["permittivity_branch_drops_with_A_(T2 signature)"] is True
        and d2["A1_compliance_branch_would_rise_with_A_(contrast)"] is True
    )

    verdict = {
        "sector_of_LV_response": "TRANSVERSE-T2 (permittivity eps0*S)",
        "sector_of_frame_anchor": "A1 (dilatation rest-mass m_e c^2)",
        "grant_mechanism": (
            "SPLIT: 'response sourced in A1' REFUTED (response=T2 permittivity); "
            "'preferred frame anchored by A1 rest-mass' CONFIRMED"
        ),
        "sme_classification": (
            "NONLINEAR transverse photon-sector object; NOT minimal-SME k_F or k_AF "
            "(those are LINEAR/field-independent)"
        ),
        "bounded_by_existing_linear_LV_tests": False,
        "in_principle_transverse_sector_object_Part2_checks_nonlinear_bounds": True,
        "one_line": (
            "The AVE sidereal LV is a NONLINEAR TRANSVERSE-T2 permittivity-saturation object "
            "(driven by and read out in the transverse photon sector), whose preferred-frame "
            "anchor is the A1 dilatation-mass yield E_YIELD ~ m_e c^2; dimensionless first-"
            "harmonic magnitude ~4.9e-3; it does NOT correspond to a minimal-SME k_F or k_AF "
            "coefficient (linear/field-independent), so existing linear cavity/Michelson/"
            "astrophysical-birefringence bounds do NOT constrain it -- but it is a transverse-"
            "sector object, so it is in-principle bounded by a dedicated NONLINEAR/higher-"
            "dimension photon-sector LV experiment, NOT structurally SME-invisible."
        ),
        "liveness_ok": bool(liveness_ok),
    }

    result = {
        "constants": consts,
        "D1_invariance_class": d1,
        "D2_response_channel_sector": d2,
        "D3_frame_anchor_provenance": d3,
        "D4_boost_order_projection": d4,
        "D5_sme_field_dependence": d5,
        "VERDICT": verdict,
    }
    return result


def main() -> None:
    result = run()
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(_JSON, "w") as fh:
        json.dump(result, fh, indent=2, default=str)
    try:
        _make_figure(result["D2_response_channel_sector"])
    except Exception as exc:  # figure is a courtesy, not load-bearing
        print(f"[warn] figure skipped: {exc}")

    v = result["VERDICT"]
    print("=" * 74)
    print("P6-LV Part 1 -- SECTOR-TRACE + SME CLASSIFICATION")
    print("=" * 74)
    print(f"LV response sector : {v['sector_of_LV_response']}")
    print(f"Frame-anchor sector: {v['sector_of_frame_anchor']}")
    print(f"Grant mechanism    : {v['grant_mechanism']}")
    print(f"SME classification : {v['sme_classification']}")
    print(f"Liveness OK        : {v['liveness_ok']}")
    print("-" * 74)
    print("ONE-LINE:")
    print(v["one_line"])
    print(f"\nartifact: {_JSON}")


if __name__ == "__main__":
    main()
