#!/usr/bin/env python3
"""
P6-FRAME — does the vacuum birefringence RESPONSE reference a preferred frame?
==============================================================================

THREE-CORNER boost-dependence test for the birefringence Letter's THIRD (sidereal)
falsifier. PR #574 settled the ORDER *given the CMB-frame premise* (radiation
Doppler -> O(beta)); this driver settles the UPSTREAM question it deferred to
Grant: WHICH FRAME does the saturation response reference? That selects the corner
and hence whether the sidereal falsifier exists at all.

  LOCAL   : response covariant OR keyed on the lab-frame field -> boost-INDEPENDENT
            -> sidereal ~ 0 (the registered falsifier is spurious).
  LATTICE : response references the node rest frame only through discreteness
            -> boost-dependence suppressed at O((q*l_node)^n) -> tiny.
  BULK    : response is the substrate/CMB-frame field magnitude (continuum)
            -> full O(beta) -> ~4.9e-3, CMB-dipole-phased.

THE LOAD-BEARING SUB-QUESTION (settled analytically, in symbolic_kernel_transform):
the kernel argument A = |E|/E_YIELD is a field MAGNITUDE, not a Lorentz invariant
(main.tex:404-405; saturation.py; bench/birefringence.py). For a radiation pump
BOTH EM invariants vanish (B = E/c => F = B^2 - E^2 = 0), so a covariant
invariant-keyed kernel gives A = 0 = ZERO pump birefringence -> the covariant
LOCAL route is inconsistent with the Letter's own central prediction. The live
fork is therefore lab-frame magnitude (LOCAL, 0) vs substrate-frame magnitude
(BULK, O(beta)).

ANTI-TAUTOLOGY. The boost acts on the REAL EM field 4-tensor (E, B) via the exact
Lorentz transform; the observable is computed through the REAL Axiom-4 kernel
(ave.bench.birefringence.delta_n_ave_differential_exact). The kernel's
frame-reference is a CONFIGURABLE `response_frame`; the harness REACHES ALL THREE
bins by construction (liveness controls below). It does NOT hardcode a Doppler
factor -- |E_substrate| is READ OFF the transformed field vector and cross-checked
against the closed-form Doppler factor.

DISCIPLINE
  - ave-canonical-source: C_0, E_YIELD, E_CRIT, L_NODE from ave.core.constants;
    NEVER hardcoded. v_CMB = 370 km/s is an EXTERNAL astrophysical input, tagged.
  - substrate-native: a real Lorentz transform of the substrate EM mode's (E,B);
    the Axiom-4 saturation kernel. No Lagrangian, no gradient-descent.
  - consistency-vs-emergence: CONSISTENCY class. No new clm / constant / axiom.
  - phase-space-coordinate-check (A46): observable in P_flip/Delta-n coordinates;
    boost on (E,B). Coordinates MATCH.
  - pure-AVE-corpus: our own re-derivation. No external attribution anywhere.

Run:  PYTHONPATH=src python3 src/scripts/vol_9_device/p6_frame_boost_dependence.py
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

from ave.core.constants import C_0, E_YIELD, L_NODE  # noqa: E402
from ave.bench.birefringence import delta_n_ave_differential_exact  # noqa: E402

# ============================================================================
# EXTERNAL ASTROPHYSICAL INPUT (LABELED -- NOT an AVE constant)
# ============================================================================
V_CMB_MPS: float = 370.0e3  # EXTERNAL. Solar-system peculiar velocity vs CMB dipole.

# Lattice-discreteness suppression channels (q*l_node), the emergent-Lorentz cubic-
# symmetry channel of preferred-frame-and-emergent-lorentz.md:21-22. The PHYSICAL
# optical value (633 nm) is q*l_node ~ 3.86e-6, so (q*l_node)^4 ~ 2.2e-22 is BELOW
# float64 resolution when carried as a fractional change; we therefore (a) report
# the physical optical number ANALYTICALLY, and (b) DEMONSTRATE the LATTICE bin is
# reachable/distinct at a RESOLVABLE suppression (an X-ray probe, q*l_node ~ 2.4e-2,
# supp ~ 3.5e-7) where the O(beta)*supp scaling is visible above the float floor.
Q_LN_OPTICAL: float = (2.0 * np.pi / 633e-9) * float(L_NODE)  # ~3.86e-6
Q_LN_XRAY_DEMO: float = (2.0 * np.pi / 1.0e-10) * float(L_NODE)  # ~2.43e-2 (resolvable demo)

_OUT_DIR = _HERE / "_output"
_JSON = _OUT_DIR / "p6_frame_boost_dependence.json"
_FIG = _OUT_DIR / "p6_frame_boost_dependence.png"


# ============================================================================
# CANONICAL-CONSTANT CROSS-CHECK
# ============================================================================
def verify_constants() -> dict:
    """Assert C_0 is the exact SI-integer definition and reproduce beta, beta^2."""
    c = float(C_0)
    assert c > 0.0 and c.is_integer(), f"C_0 is not the exact SI-integer definition: {c}"
    beta = V_CMB_MPS / c
    return {
        "C_0_mps": c,
        "C_0_is_codata_exact": True,
        "E_YIELD_Vpm": float(E_YIELD),
        "L_NODE_m": float(L_NODE),
        "V_CMB_mps_EXTERNAL": V_CMB_MPS,
        "beta_CMB": beta,
        "beta_CMB_squared": beta * beta,
    }


# ============================================================================
# THE ANALYTIC SUB-QUESTION -- kernel-argument Lorentz transform (sympy)
# ============================================================================
def symbolic_kernel_transform() -> dict:
    """Symbolically expose (i) that both EM invariants vanish for a radiation pump,
    (ii) the boost of |E|^2 for that pump = the Doppler factor D^2, first-order in
    beta, and (iii) the observable powers P_flip ~ |E|^4 ~ D^4."""
    beta, ct = sp.symbols("beta costheta", real=True)
    gamma = 1 / sp.sqrt(1 - beta**2)

    # --- radiation-pump EM invariants (Heaviside-Lorentz, c = 1 units for the
    #     scalar identity): a plane wave has |E| = |B| and E . B = 0, so
    #     F = B^2 - E^2 = 0 and G = E . B = 0. An invariant-keyed kernel -> A = 0.
    E_amp, B_amp = sp.symbols("E B", positive=True)
    F_invariant = (B_amp**2 - E_amp**2).subs(B_amp, E_amp)  # radiation: B = E -> 0
    G_invariant = sp.Integer(0)  # E perpendicular B for a plane wave

    # --- Doppler factor for a plane-wave amplitude under a boost of the OBSERVER
    #     (response frame) by beta at angle theta to k-hat. Longitudinal aligned
    #     case is the standard sqrt((1-beta)/(1+beta)); general angle:
    D = 1 / (gamma * (1 - beta * ct))  # amplitude scale |E'| = D |E|
    D_series = sp.series(D, beta, 0, 3).removeO()

    out = {}
    for label, expr, power in (
        ("D_field^1   (|E| ~ pump amplitude)", D, 1),
        ("D^2  (delta_n_bir ~ A^2 ~ |E|^2)", D**2, 2),
        ("D^4  (P_flip ~ |E|^4)", D**4, 4),
    ):
        s = sp.series(expr, beta, 0, 3).removeO()
        p = sp.Poly(sp.expand(s), beta)
        c1 = p.coeff_monomial(beta)  # linear-in-beta coefficient
        c2 = p.coeff_monomial(beta**2)
        out[label] = {
            "series_to_beta2": sp.sstr(sp.expand(s)),
            "linear_in_beta_coeff": sp.sstr(sp.simplify(c1)),
            "linear_is_nonzero": bool(sp.simplify(c1) != 0),
            "quadratic_coeff": sp.sstr(sp.simplify(c2)),
        }
    # static-field control: transverse magnitude picks up only gamma (no linear term)
    gamma_series = sp.series(gamma, beta, 0, 3).removeO()
    return {
        "radiation_pump_invariant_F_eq_B2_minus_E2": sp.sstr(F_invariant),  # == 0
        "radiation_pump_invariant_G_eq_EdotB": sp.sstr(G_invariant),  # == 0
        "invariant_keyed_kernel_gives_zero_pump_birefringence": True,
        "doppler_D_series": sp.sstr(D_series),
        "field_powers": out,
        "static_field_gamma_series": sp.sstr(gamma_series),
        "static_field_linear_in_beta_coeff": sp.sstr(
            sp.Poly(gamma_series, beta).coeff_monomial(beta)
        ),  # == 0  (static branch is O(beta^2))
    }


# ============================================================================
# SUBSTRATE-NATIVE EM-FIELD LORENTZ TRANSFORM (the boost acts on REAL (E,B))
# ============================================================================
def boost_EB(E_lab: np.ndarray, B_lab: np.ndarray, beta_vec: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Lorentz-transform the EM field (E,B) from the lab frame to a frame moving at
    velocity w = beta_vec * c relative to the lab (here: the substrate frame, which
    moves at -v relative to the lab; caller passes beta_vec = -v/c).

    Standard field transform (SI, boost velocity w, bw = w/c, g = 1/sqrt(1-bw^2)):
        E'_par = E_par
        E'_perp = g (E + w x B)_perp
        B'_par = B_par
        B'_perp = g (B - (w/c^2) x E)_perp
    Returns (E_sub, B_sub) in V/m and T. This is the honest vector transform; the
    kernel magnitude |E_sub| is read off it (NOT a plugged-in Doppler factor)."""
    b = np.asarray(beta_vec, dtype=float)
    bmag = np.linalg.norm(b)
    if bmag < 1e-18:
        return np.array(E_lab, float), np.array(B_lab, float)
    bhat = b / bmag
    g = 1.0 / np.sqrt(1.0 - bmag**2)
    w = b * C_0  # velocity vector [m/s]

    E = np.asarray(E_lab, float)
    B = np.asarray(B_lab, float)
    E_par = np.dot(E, bhat) * bhat
    E_perp = E - E_par
    B_par = np.dot(B, bhat) * bhat
    B_perp = B - B_par

    E_sub = E_par + g * (E_perp + np.cross(w, B))
    B_sub = B_par + g * (B_perp - np.cross(w, E) / C_0**2)
    # np.cross(w,B) may carry a parallel piece; project the transformed perp part
    # cleanly by recombining par + gamma*(perp + cross)_perp:
    cross_EB = np.cross(w, B)
    cross_EB_perp = cross_EB - np.dot(cross_EB, bhat) * bhat
    E_sub = E_par + g * (E_perp + cross_EB_perp)
    cross_BE = -np.cross(w, E) / C_0**2
    cross_BE_perp = cross_BE - np.dot(cross_BE, bhat) * bhat
    B_sub = B_par + g * (B_perp + cross_BE_perp)
    return E_sub, B_sub


def pump_fields(E0: float, khat: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """A linearly-polarized plane-wave pump: E0 along a transverse axis, B = (k x E)/c."""
    khat = np.asarray(khat, float)
    khat = khat / np.linalg.norm(khat)
    # pick a transverse polarization axis
    ref = np.array([1.0, 0.0, 0.0]) if abs(khat[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    pol = ref - np.dot(ref, khat) * khat
    pol = pol / np.linalg.norm(pol)
    E = E0 * pol
    B = np.cross(khat, E) / C_0
    return E, B


# ============================================================================
# THE CONFIGURABLE RESPONSE-FRAME KERNEL ARGUMENT  (reaches ALL THREE bins)
# ============================================================================
def response_field_magnitude(
    E0: float,
    khat: np.ndarray,
    beta_vec: np.ndarray,
    response_frame: str,
    *,
    q_ln: float = Q_LN_OPTICAL,
    lattice_order: int = 4,
) -> float:
    """|E| the SATURATION KERNEL keys on, per the response-frame hypothesis.

    response_frame:
      "lab"       (LOCAL) : lab-frame magnitude, boost-independent -> flat in beta.
      "substrate" (BULK)  : substrate-frame magnitude from the REAL boosted (E,B)
                            -> full O(beta).
      "invariant" (LOCAL, covariant control): sqrt|E^2 - c^2 B^2| -> 0 for a pump.
      "lattice"   (LATTICE): NOT a field magnitude -- see observable_frac, which
                            reduces the SUBSTRATE fractional response by the discreteness
                            factor (q*l_node)^n (the emergent-Lorentz cubic-symmetry
                            channel). Handled there, not here.
    """
    E_lab, B_lab = pump_fields(E0, khat)
    lab_mag = float(np.linalg.norm(E_lab))
    if response_frame in ("lab", "lattice"):
        return lab_mag
    if response_frame == "invariant":
        inv = np.dot(E_lab, E_lab) - C_0**2 * np.dot(B_lab, B_lab)
        return float(np.sqrt(abs(inv)))  # radiation: E^2 = c^2 B^2 -> 0
    E_sub, _B_sub = boost_EB(E_lab, B_lab, beta_vec)
    sub_mag = float(np.linalg.norm(E_sub))
    if response_frame == "substrate":
        return sub_mag
    raise ValueError(f"unknown response_frame {response_frame!r}")


def observable_frac(
    E0: float, khat: np.ndarray, beta_vec: np.ndarray, response_frame: str, *, q_ln: float = Q_LN_OPTICAL
) -> tuple[float, float]:
    """Fractional modulation of (delta_n_bir, P_flip) relative to beta = 0, at the
    kernel's response-frame field. P_flip ~ (delta_n * L)^2, so frac_P = (dn/dn0)^2 - 1
    (the probe path/frequency factors are common-mode to both polarizations; their
    own O(beta) Doppler REINFORCES, per PR #574, and is not needed for the corner)."""
    if response_frame == "lattice":
        # LATTICE = the substrate boost-sensitivity REDUCED by the discreteness factor
        # (q*l_node)^n (order-preserving, exact -- no nested subtraction). This is the
        # emergent-Lorentz cubic-symmetry channel: the boost enters only through the
        # discrete node stencil at O((q*l_node)^n * beta).
        supp = q_ln**4
        fdn_sub, fP_sub = observable_frac(E0, khat, beta_vec, "substrate")
        return supp * fdn_sub, supp * fP_sub
    E_ref = response_field_magnitude(E0, khat, beta_vec, response_frame, q_ln=q_ln)
    E_ref0 = response_field_magnitude(E0, khat, np.zeros(3), response_frame, q_ln=q_ln)
    dn = float(delta_n_ave_differential_exact(E_ref))
    dn0 = float(delta_n_ave_differential_exact(E_ref0))
    if dn0 == 0.0:
        return 0.0, 0.0  # covariant kernel: zero pump birefringence (the anti-test)
    frac_dn = dn / dn0 - 1.0
    frac_P = (dn / dn0) ** 2 - 1.0
    return frac_dn, frac_P


# ============================================================================
# SLOPE READER + PLANTED-ORDER GUARD
# ============================================================================
def fit_order(betas: np.ndarray, fracs: np.ndarray) -> float:
    """Log-log slope of |frac| vs beta = the boost-dependence order n. Returns nan if
    |frac| is at the float floor across the sweep (a FLAT / boost-independent response)."""
    a = np.abs(np.asarray(fracs, float))
    b = np.asarray(betas, float)
    mask = a > 1e-14
    if mask.sum() < 3:
        return float("nan")  # flat -> LOCAL
    return float(np.polyfit(np.log(b[mask]), np.log(a[mask]), 1)[0])


def planted_order_guard() -> dict:
    """Feed the slope-reader synthetic responses of KNOWN order; confirm recovery."""
    b = np.logspace(-6, -2, 40)
    return {
        "planted_n1_reads": round(fit_order(b, 3.0 * b), 4),
        "planted_n2_reads": round(fit_order(b, 3.0 * b**2), 4),
        "planted_flat_reads_nan": bool(np.isnan(fit_order(b, 0.0 * b + 1e-18))),
    }


# ============================================================================
# THE THREE-CORNER SWEEP
# ============================================================================
def corner_sweep() -> dict:
    consts = verify_constants()
    beta_cmb = consts["beta_CMB"]
    E0 = 1e-3 * float(E_YIELD)  # weak-field pump, A ~ 1e-3 (radiative-sector regime)
    khat = np.array([0.0, 0.0, 1.0])  # pump along z
    v_hat = np.array([0.0, 0.0, 1.0])  # aligned boost (max projection, cos theta = 1)

    # --- MAGNITUDE sweep: fit the boost-order per corner (substrate frame moves at
    #     -v relative to lab -> beta_vec = -beta * v_hat) ---
    betas = np.logspace(-6, -2, 40)
    corners: dict[str, dict] = {}
    for frame in ("lab", "invariant", "substrate", "lattice"):
        # lattice bin is DEMONSTRATED at the resolvable X-ray q_ln (optical underflows);
        # its physical optical magnitude is reported analytically in lattice_physical.
        q_ln = Q_LN_XRAY_DEMO if frame == "lattice" else Q_LN_OPTICAL
        fr_dn, fr_P = [], []
        for bmag in betas:
            fdn, fP = observable_frac(E0, khat, -bmag * v_hat, frame, q_ln=q_ln)
            fr_dn.append(fdn)
            fr_P.append(fP)
        corners[frame] = {
            "order_delta_n": fit_order(betas, np.array(fr_dn)),
            "order_P_flip": fit_order(betas, np.array(fr_P)),
            "frac_P_at_beta_cmb": float(np.interp(beta_cmb, betas, np.array(fr_P)))
            if not np.all(np.array(fr_P) == 0.0)
            else 0.0,
            "q_ln_used": q_ln if frame == "lattice" else None,
        }

    # LATTICE physical (optical) magnitude -- reported analytically because
    # (q_ln_optical)^4 * 4 beta underflows a float64 subtraction. The lattice corner,
    # IF it were the physical one, gives O(beta) suppressed by (q*l_node)^4:
    supp_opt = Q_LN_OPTICAL**4
    lattice_physical = {
        "q_ln_optical": Q_LN_OPTICAL,
        "supp_qln4_optical": supp_opt,
        "P_flip_1st_harmonic_if_lattice": 4.0 * beta_cmb * supp_opt,
        "note": "O(beta) * (q*l_node)^4 ~ 1e-24 -- ~21 OOM below the BULK value; unobservable.",
    }

    # --- DIRECTION (sidereal) sweep at |beta| = beta_cmb, substrate (BULK) config:
    #     harmonic content of P_flip over one apparatus rotation ---
    thetas = np.linspace(0.0, 2.0 * np.pi, 720, endpoint=False)
    frac_P_theta, frac_dn_theta = [], []
    for th in thetas:
        v = np.array([np.sin(th), 0.0, np.cos(th)])  # boost direction sweeps vs k=z
        fdn, fP = observable_frac(E0, khat, -beta_cmb * v, "substrate")
        frac_P_theta.append(fP)
        frac_dn_theta.append(fdn)
    frac_P_theta = np.array(frac_P_theta)
    frac_dn_theta = np.array(frac_dn_theta)
    # harmonic amplitudes via projection onto cos(k*theta)
    def harm(sig, k):
        return 2.0 * np.abs(np.mean(sig * np.exp(-1j * k * thetas)))

    sidereal = {
        "P_flip_1st_harmonic_amp": float(harm(frac_P_theta, 1)),
        "P_flip_2nd_harmonic_amp": float(harm(frac_P_theta, 2)),
        "delta_n_1st_harmonic_amp": float(harm(frac_dn_theta, 1)),
        "expected_4beta": 4.0 * beta_cmb,
        "expected_2beta": 2.0 * beta_cmb,
        "beta_squared_ref": beta_cmb**2,  # the 2nd harmonic is O(beta^2); exact ~3 beta^2
        "note_2nd_harmonic": "O(beta^2), exact angular projection ~3 beta^2; PR #574's 5 beta^2 was an order estimate",
        "period": "one sidereal day (apparatus rotation vs fixed CMB dipole)",
    }

    # --- cross-check: |E_substrate| read off the vector transform == Doppler factor ---
    E_sub_mag = response_field_magnitude(E0, khat, -beta_cmb * v_hat, "substrate")
    ratio = E_sub_mag / (1e-3 * float(E_YIELD))
    # boost velocity w = -v (substrate moves at -v rel to lab) with v = +z, so the
    # aligned Doppler is the BLUE branch sqrt((1+beta)/(1-beta)) ~ 1 + beta:
    doppler = np.sqrt((1 + beta_cmb) / (1 - beta_cmb))
    dop_check = {
        "E_sub_over_E_lab_from_vector_transform": ratio,
        "closed_form_doppler_aligned": float(doppler),
        "rel_err": abs(ratio - doppler) / doppler,
    }

    return {
        "constants": consts,
        "symbolic_kernel_transform": symbolic_kernel_transform(),
        "planted_order_guard": planted_order_guard(),
        "magnitude_sweep_corners": corners,
        "lattice_physical_optical": lattice_physical,
        "sidereal_direction_sweep_BULK": sidereal,
        "doppler_vector_crosscheck": dop_check,
        "_sweep_arrays": {  # for the figure
            "betas": betas.tolist(),
            "thetas": thetas.tolist(),
            "frac_P_theta_BULK": frac_P_theta.tolist(),
        },
    }


# ============================================================================
# LIVENESS + VERDICT
# ============================================================================
def assess(res: dict) -> dict:
    c = res["magnitude_sweep_corners"]
    guard = res["planted_order_guard"]
    # liveness: LOCAL bins flat (nan order), BULK slope ~1, LATTICE slope ~1 suppressed
    lab_flat = bool(np.isnan(c["lab"]["order_P_flip"]))
    inv_flat = bool(np.isnan(c["invariant"]["order_P_flip"]))
    bulk_lin = abs(c["substrate"]["order_P_flip"] - 1.0) < 0.05
    lat_lin = abs(c["lattice"]["order_P_flip"] - 1.0) < 0.05
    bulk_amp = abs(c["substrate"]["frac_P_at_beta_cmb"])
    lat_amp = abs(c["lattice"]["frac_P_at_beta_cmb"])
    # LATTICE is DISTINCT from BULK: same O(beta) order, but suppressed amplitude
    # (demonstrated at the X-ray q_ln, supp = (q*l_node)^4 ~ 3.5e-7).
    lattice_suppressed = 0.0 < lat_amp < 1e-3 * bulk_amp
    liveness = {
        "LOCAL_lab_reachable_flat": lab_flat,
        "LOCAL_invariant_reachable_zero_pump_birefringence": inv_flat,
        "BULK_substrate_reachable_order1": bulk_lin,
        "LATTICE_reachable_order1_suppressed": lat_lin and lattice_suppressed,
        "planted_order_guard_ok": (
            abs(guard["planted_n1_reads"] - 1.0) < 0.02
            and abs(guard["planted_n2_reads"] - 2.0) < 0.02
            and guard["planted_flat_reads_nan"]
        ),
    }
    all_three = lab_flat and bulk_lin and (lat_lin and lattice_suppressed)
    return {
        "liveness_all_three_bins_reachable": bool(all_three),
        "liveness_detail": liveness,
        "substrate_native_verdict": "BULK",
        "substrate_native_verdict_basis": (
            "kernel keys on |E| (a frame-dependent MAGNITUDE, not an invariant; a "
            "covariant kernel gives zero pump birefringence); the saturating nodes are "
            "at rest in the substrate = CMB rest frame (preferred-frame leaf, detectable "
            "in principle); the boost-Doppler of the pump amplitude is a CONTINUUM effect "
            "(not (q*l_node)^n-suppressed), so LATTICE does not apply -> substrate-frame "
            "magnitude -> BULK, O(beta)."
        ),
        "BULK_sidereal_P_flip_1st_harmonic": res["sidereal_direction_sweep_BULK"][
            "P_flip_1st_harmonic_amp"
        ],
        "LOCAL_alternative_note": (
            "main.tex:404-406 evaluates the kernel in the LAB frame -> sidereal exactly 0. "
            "This is an operational EVALUATION choice with no substrate mechanism (the "
            "medium responds in its own rest frame, not the source's); it contradicts "
            "main.tex:420-421. Flagged for Grant, not silently chosen."
        ),
    }


def make_figure(res: dict) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    try:
        import ave.viz.style as style

        style.apply("print")
    except Exception:
        pass

    betas = np.array(res["_sweep_arrays"]["betas"])
    thetas = np.array(res["_sweep_arrays"]["thetas"])
    frac_theta = np.array(res["_sweep_arrays"]["frac_P_theta_BULK"])
    c = res["magnitude_sweep_corners"]
    beta_cmb = res["constants"]["beta_CMB"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4), facecolor="white")

    # panel 1: boost-order per corner
    okabe = {"lab": "#0072B2", "invariant": "#009E73", "substrate": "#D55E00", "lattice": "#CC79A7"}
    for frame, label in (
        ("lab", "LOCAL (lab-frame magnitude)"),
        ("invariant", "LOCAL (covariant invariant -> 0)"),
        ("substrate", "BULK (substrate/CMB magnitude)"),
        ("lattice", "LATTICE ((q l_node)^4-gated, X-ray demo)"),
    ):
        q_ln = Q_LN_XRAY_DEMO if frame == "lattice" else Q_LN_OPTICAL
        fr = []
        for bmag in betas:
            _, fP = observable_frac(
                1e-3 * float(E_YIELD), np.array([0, 0, 1.0]), -bmag * np.array([0, 0, 1.0]), frame, q_ln=q_ln
            )
            fr.append(abs(fP))
        fr = np.array(fr)
        floor = 3e-18  # plot floor: LOCAL configs are EXACTLY 0 -> shown flat at floor
        fr_plot = np.where(fr > floor, fr, floor)
        ax1.loglog(betas, fr_plot, "o-", ms=3, color=okabe[frame], label=label)
    ax1.set_ylim(1e-18, 1e-1)
    ax1.axvline(beta_cmb, color="0.4", ls=":", lw=1)
    ax1.text(beta_cmb, 2e-18, r"$\beta_{\rm CMB}$", rotation=90, va="bottom", fontsize=8, color="0.3")
    ax1.text(1.3e-6, 5e-18, "LOCAL configs $\\equiv 0$ (at floor)", fontsize=7, color="0.35")
    ax1.set_xlabel(r"boost $\beta$ (apparatus through substrate)")
    ax1.set_ylabel(r"$|P_{\rm flip}(\beta)/P_{\rm flip}(0)-1|$")
    ax1.set_title("Boost-dependence order per response-frame corner")
    ax1.legend(fontsize=7, loc="upper left", framealpha=0.9)
    ax1.grid(True, which="both", alpha=0.3)

    # panel 2: sidereal harmonic (BULK)
    ax2.plot(np.degrees(thetas), 1e3 * frac_theta, color=okabe["substrate"], lw=1.6)
    ax2.axhline(1e3 * 4 * beta_cmb, color="0.4", ls="--", lw=1, label=r"$+4\beta$")
    ax2.axhline(-1e3 * 4 * beta_cmb, color="0.4", ls="--", lw=1)
    ax2.set_xlabel(r"apparatus angle vs CMB dipole $\theta$ (deg)")
    ax2.set_ylabel(r"$P_{\rm flip}$ fractional modulation $\times 10^{-3}$")
    ax2.set_title(r"BULK sidereal signature (1st harmonic $\approx 4\beta \approx 4.9\times10^{-3}$)")
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(_FIG, dpi=130, facecolor="white")
    plt.close(fig)


def main() -> None:
    res = corner_sweep()
    res["assessment"] = assess(res)
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    serialisable = {k: v for k, v in res.items() if k != "_sweep_arrays"}
    with open(_JSON, "w") as f:
        json.dump(serialisable, f, indent=2, default=str)
    make_figure(res)

    a = res["assessment"]
    print("=" * 74)
    print("P6-FRAME — three-corner boost-dependence of the birefringence response")
    print("=" * 74)
    print(f"beta_CMB = {res['constants']['beta_CMB']:.6e}")
    print("\n-- ANALYTIC SUB-QUESTION (kernel argument transform) --")
    st = res["symbolic_kernel_transform"]
    print(f"  radiation-pump invariant F = B^2 - E^2 : {st['radiation_pump_invariant_F_eq_B2_minus_E2']}  (=> covariant kernel gives A=0, zero pump birefringence)")
    for k, v in st["field_powers"].items():
        print(f"  {k:34s}: linear-in-beta coeff = {v['linear_in_beta_coeff']:>8s}  (nonzero={v['linear_is_nonzero']})")
    print(f"  static-field control gamma linear coeff: {st['static_field_linear_in_beta_coeff']}  (=> static branch is O(beta^2))")
    print("\n-- MAGNITUDE SWEEP: boost-order per corner --")
    for frame, d in res["magnitude_sweep_corners"].items():
        print(f"  {frame:10s}: order(P_flip)={d['order_P_flip']!s:>7}  frac_P(beta_cmb)={d['frac_P_at_beta_cmb']:+.4e}")
    print("\n-- SIDEREAL (BULK config) harmonic content --")
    s = res["sidereal_direction_sweep_BULK"]
    print(f"  P_flip  1st harmonic = {s['P_flip_1st_harmonic_amp']:.4e}   (expected 4 beta = {s['expected_4beta']:.4e})")
    print(f"  P_flip  2nd harmonic = {s['P_flip_2nd_harmonic_amp']:.4e}   (O(beta^2); ~3 beta^2, beta^2 = {s['beta_squared_ref']:.4e})")
    print(f"  delta_n 1st harmonic = {s['delta_n_1st_harmonic_amp']:.4e}   (expected 2 beta = {s['expected_2beta']:.4e})")
    print("\n-- DOPPLER vector cross-check --")
    dc = res["doppler_vector_crosscheck"]
    print(f"  |E_sub|/|E_lab| (vector transform) = {dc['E_sub_over_E_lab_from_vector_transform']:.8f}")
    print(f"  closed-form Doppler (aligned)      = {dc['closed_form_doppler_aligned']:.8f}   rel_err={dc['rel_err']:.2e}")
    print("\n-- LIVENESS (all three bins reachable?) --")
    for k, v in a["liveness_detail"].items():
        print(f"  {k}: {v}")
    print(f"  ALL THREE REACHABLE: {a['liveness_all_three_bins_reachable']}")
    print("\n-- VERDICT --")
    print(f"  substrate-native corner: {a['substrate_native_verdict']}")
    print(f"  BULK sidereal P_flip 1st harmonic: {a['BULK_sidereal_P_flip_1st_harmonic']:.4e}")
    print(f"  LOCAL alternative: {a['LOCAL_alternative_note']}")
    print(f"\nJSON: {_JSON}")
    print(f"FIG : {_FIG}")


if __name__ == "__main__":
    main()
