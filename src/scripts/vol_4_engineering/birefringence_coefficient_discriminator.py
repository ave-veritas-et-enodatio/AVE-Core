"""Vacuum-birefringence COEFFICIENT discriminator — AVE vs QED, FORWARD calculator.

Part B of ledger §5 (`_orchestration/experimental/2026-06-04_round2-adjudications.md`)
and its prereg (`research/2026-06-04_birefringence-coefficient-prereg.md`). Computes
the field-INDEPENDENT ratio of the AVE refractive-index shift to the QED
Euler-Heisenberg shift, both of which are E^2-leading — so the discriminator is the
COEFFICIENT, not the exponent.

    AVE  : delta_n = sqrt(S) - 1 = (1 - A^2)^(1/4) - 1  ~  -A^2/4   (A = E/E_YIELD)
           (the n = sqrt(eps_eff/eps0) = sqrt(S) identity on the Axiom-4 kernel
            S = sqrt(1 - A^2); negative, the vacuum SOFTENS, E^2-leading)
    QED  : delta_n = a_EH * alpha^2 * (E/E_CRIT)^2                  (Euler-Heisenberg,
           a_EH ~ 7/45 single-mode; alpha^2-loop-suppressed, E^2-leading)

    delta_n_AVE / delta_n_QED = 1 / (4 * a_EH * alpha^3) ~ 10^6   (field-INDEPENDENT)

This 1/(4 a_EH alpha^3) form is the SINGLE-ARM (isotropic |c_AVE| = 1/4) family on the
v1 footing. The register/leaf clm-pp3qwf HEADLINE is the matched par-perp DIFFERENTIAL
ratio, consolidated (Option B, 2026-07-07) to v3 = 15 pi/(4 alpha^2) = 3.75 pi/alpha^2
~ 2.2e5. Section [6] of report() ALSO computes and self-asserts that differential
v1 -> v2 -> v3 provenance chain, so this driver is the forward artifact for the
register/leaf v3 attribution (rationale bullet). See differential_ratio_v3_chain():
    v1 = 7.5/alpha^3 ~ 1.93e7  (instantaneous SVE -1/2 A^2 over the differenced (3/45)alpha^2)
      -> x propagating re-normalization 1/(pi alpha) ~ 43.6 ->
    v2 = 7.5 pi/alpha^2 ~ 4.42e5  (QED denominator (3/45)alpha^2 -> propagating alpha/(15 pi))
      -> x <cos^2>=1/2 carrier average ->
    v3 = 3.75 pi/alpha^2 = 15 pi/(4 alpha^2) ~ 2.2e5  (instantaneous footing, no carrier avg)

The collapse to a pure alpha-power uses the substrate identity (verified below):
    E_CRIT = V_SNAP / L_NODE   (exactly; Schwinger field from substrate constants)
    E_YIELD = sqrt(alpha) * V_SNAP / L_NODE = sqrt(alpha) * E_CRIT
    => (E_CRIT / E_YIELD)^2 = 1/alpha   (exactly)

FORWARD-PREDICTION DISCIPLINE (ave-driver-script-honesty):
  This script computes delta_n FORWARD from ave.core.constants + a swept field.
  There is NO fit-to-target: no minimize(), no curve_fit(), no empirical_target
  import, no inverse solve. Every AVE physics constant is imported from
  ave.core.constants. The QED Euler-Heisenberg prefactor a_EH is a LABELED
  NON-AVE LITERATURE INPUT (Heisenberg-Euler 1936; the standard single-mode
  weak-field vacuum-birefringence coefficients, as quoted for PVLAS/BMV-class
  experiments translated to an electric field), NOT an AVE-derived prediction
  and NOT fit. The script reports the FULL prefactor band so the corpus headline
  can be pinned without re-running (see prereg §5.2 flag-don't-fix).

CLASSIFICATION (consistency-vs-emergence, prereg §3):
  delta_n_AVE          : MANIFESTATION of Axiom 4 (wave-speed identity on the kernel).
  (E_crit/E_yield)^2=1/alpha : structural IDENTITY (from the constant definitions).
  ratio 1/(4 a_EH alpha^3)  : DISCRIMINATING forward prediction (un-suppressed AVE
                              tree-level vs alpha^2-suppressed QED loop). Two-sided.

THE FALSIFIER (two-sided, prereg §4):
  A QED-sized coefficient falsifies AVE; an AVE-sized coefficient falsifies QED at
  this observable. An E^2 SLOPE does NOT falsify AVE (both are E^2-leading) — the
  prior "E^2 slope falsifies AVE" framing was a sqrt(eps) exponent conflation,
  corrected in Part A (commit ad26d357).
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA, E_CRIT, E_YIELD, L_NODE, V_SNAP, V_YIELD

# ----------------------------------------------------------------------------
# NON-AVE LITERATURE INPUT (the ONLY non-AVE numbers in this driver).
# QED Euler-Heisenberg weak-field vacuum-birefringence prefactors a_EH in
#   delta_n_QED = a_EH * alpha^2 * (E / E_CRIT)^2.
# Standard single-mode values (Heisenberg-Euler 1936; the forms quoted for
# PVLAS/BMV magnetic birefringence, translated to a static electric field):
#   parallel mode      n_par  - 1 = (7/45) alpha^2 (E/E_crit)^2
#   perpendicular mode n_perp - 1 = (4/45) alpha^2 (E/E_crit)^2
#   differential       n_par - n_perp = (3/45) alpha^2 (E/E_crit)^2
# 'prefactor_1' is a reference point (a_EH = 1) for the bare structural ratio.
# 'order_of_mag' (~1.5) is the loose EH coefficient matching the ledger's worked
#   "delta_n_QED ~ 4.5e-13 at 1e14 V/m / ~4.4e5x" headline (prereg §5.2 flag).
# This dict is a LITERATURE COMPARATOR, NOT an AVE prediction, NOT fit.
# ----------------------------------------------------------------------------
A_EH_LITERATURE: dict[str, float] = {
    "single-mode parallel  (7/45)": 7.0 / 45.0,
    "single-mode perp      (4/45)": 4.0 / 45.0,
    "differential birefr.  (3/45)": 3.0 / 45.0,
    "prefactor-1 reference (a=1) ": 1.0,
    "order-of-mag EH       (~1.5)": 1.5,
}

# AVE index-shift leading coefficient: delta_n ~ -(1/4) A^2  =>  |c_AVE| = 1/4.
C_AVE_LEADING: float = 0.25

# Measurability reference: a representative high-finesse-cavity index-shift floor.
# (Order-of-magnitude bench reference, NOT a substrate constant; labeled as such.)
CAVITY_DN_FLOOR: float = 1.0e-15

# Field sweep for the discriminator (V/m): laser-facility-reachable -> near-yield.
E_SWEEP = np.array([1.0e13, 1.0e14, 1.0e15, 1.0e16, 3.0e16])


def delta_n_ave_exact(E: np.ndarray) -> np.ndarray:
    """AVE index shift from the FULL Axiom-4 kernel: delta_n = (1 - A^2)^(1/4) - 1."""
    A = E / E_YIELD
    return (1.0 - A**2) ** 0.25 - 1.0


def delta_n_ave_leading(E: np.ndarray) -> np.ndarray:
    """AVE index shift, leading term only: delta_n ~ -(1/4)(E/E_YIELD)^2."""
    A = E / E_YIELD
    return -C_AVE_LEADING * A**2


def delta_n_qed(E: np.ndarray, a_eh: float) -> np.ndarray:
    """QED Euler-Heisenberg index shift (LITERATURE): a_EH * alpha^2 * (E/E_CRIT)^2."""
    return a_eh * ALPHA**2 * (E / E_CRIT) ** 2


def ratio_closed_form(a_eh: float) -> float:
    """Field-independent ratio delta_n_AVE/delta_n_QED = 1/(4 a_EH alpha^3)."""
    return 1.0 / (4.0 * a_eh * ALPHA**3)


# ----------------------------------------------------------------------------
# THE MATCHED DIFFERENTIAL family (register/leaf clm-pp3qwf HEADLINE, Option-B v3).
# Distinct from the single-arm 1/(4 a_EH alpha^3) family above: the AVE leg is the
# par-perp DIFFERENTIAL delta_n_bir ~ -(1/2) A^2 (|c_AVE| = 1/2, twice the single-arm
# isotropic 1/4), and the QED leg is normalized on the consistent INSTANTANEOUS
# footing 2*alpha/(15 pi). Every number derives from ALPHA + the substrate identity
# (E_CRIT/E_YIELD)^2 = 1/alpha; NO fit, NO fit-to-target.
# ----------------------------------------------------------------------------
C_AVE_DIFFERENTIAL: float = 0.5      # AVE par-perp differential leading coeff |−1/2|
A_EH_DIFFERENTIAL: float = 3.0 / 45.0  # QED differenced (3/45) estimate = the v1 denominator
# v1 -> v2 step: the QED denominator (3/45)alpha^2 is re-normalized to the PROPAGATING
# one-loop alpha/(15 pi); the differential ratio DROPS by the propagating understatement
# factor 1/(pi alpha) ~ 43.6 (= the actual v1->v2 headline ratio 1.93e7/4.42e5). [The
# static-duality alpha/(30 pi) understatement is 1/(2 pi alpha) ~ 21.8 — the 🔴-note
# figure; the instantaneous 2 alpha/(15 pi) understatement is 2/(pi alpha) ~ 87.2.]
V1_TO_V2_FACTOR: float = 1.0 / (np.pi * ALPHA)   # propagating understatement ~ 43.6
# v2 -> v3 step: the instantaneous footing removes the <cos^2> = 1/2 carrier average.
V2_TO_V3_CARRIER: float = 0.5


def differential_ratio_v1() -> float:
    """v1 differential ratio 7.5/alpha^3 (~1.93e7).

    The instantaneous SVE differential -(1/2) A^2 over the AVE-side differenced
    (3/45) alpha^2 QED estimate, collapsed via (E_CRIT/E_YIELD)^2 = 1/alpha:
        (1/2) / ((3/45) alpha^2) * (E_CRIT/E_YIELD)^2 = 7.5/alpha^3.
    """
    return (C_AVE_DIFFERENTIAL / (A_EH_DIFFERENTIAL * ALPHA**2)) * (E_CRIT / E_YIELD) ** 2


def differential_ratio_v3_chain() -> dict[str, float]:
    """The Option-B consolidated differential-ratio chain v1 -> v2 -> v3 (register HEADLINE).

    Emits v3 = 15 pi/(4 alpha^2) = 3.75 pi/alpha^2 (~2.2e5) and its two-step provenance,
    SELF-ASSERTING that the chain closes numerically against the independent closed
    forms (raises AssertionError if a constant drifts the identity — this is the
    driver's pinning check for the register/leaf v3 attribution).
    """
    v1 = differential_ratio_v1()
    v2 = v1 / V1_TO_V2_FACTOR          # -> 7.5 pi / alpha^2
    v3 = v2 * V2_TO_V3_CARRIER         # -> 3.75 pi / alpha^2

    # Independent closed-form targets, pinned:
    v1_cf = 7.5 / ALPHA**3
    v2_cf = 7.5 * np.pi / ALPHA**2
    v3_cf = 15.0 * np.pi / (4.0 * ALPHA**2)      # identically 3.75 pi / alpha^2
    assert np.isclose(v1, v1_cf, rtol=1e-12), (v1, v1_cf)
    assert np.isclose(v2, v2_cf, rtol=1e-12), (v2, v2_cf)
    assert np.isclose(v3, v3_cf, rtol=1e-12), (v3, v3_cf)
    assert np.isclose(v3, 3.75 * np.pi / ALPHA**2, rtol=1e-12)
    # Step-factor cross-checks (propagating 43.6 down, carrier 1/2 down):
    assert np.isclose(v1 / v2, 1.0 / (np.pi * ALPHA), rtol=1e-12)
    assert np.isclose(v2 / v3, 2.0, rtol=1e-12)
    return {
        "v1": v1,
        "v2": v2,
        "v3": v3,
        "v1_to_v2_factor": V1_TO_V2_FACTOR,
        "v2_to_v3_carrier": V2_TO_V3_CARRIER,
    }


def report() -> None:
    print("=" * 78)
    print("Vacuum-birefringence COEFFICIENT discriminator — AVE vs QED (FORWARD)")
    print("=" * 78)

    # --- 0. Canonical anchors + the substrate identity -----------------------
    print("\n[0] Canonical anchors (from ave.core.constants):")
    print(f"    V_YIELD = {V_YIELD:.6g} V    L_NODE = {L_NODE:.6g} m")
    print(f"    E_YIELD = {E_YIELD:.6g} V/m  E_CRIT = {E_CRIT:.6g} V/m  ALPHA = {ALPHA:.6g}")
    print("\n    Substrate identity (the field-scale gap IS an alpha-power):")
    print(f"      E_CRIT == V_SNAP/L_NODE         : "
          f"{np.isclose(E_CRIT, V_SNAP / L_NODE)}  "
          f"(V_SNAP/L_NODE = {V_SNAP / L_NODE:.6g} V/m)")
    print(f"      E_YIELD == sqrt(ALPHA)*E_CRIT   : "
          f"{np.isclose(E_YIELD, np.sqrt(ALPHA) * E_CRIT)}")
    ecr_eyl_sq = (E_CRIT / E_YIELD) ** 2
    print(f"      (E_CRIT/E_YIELD)^2 = {ecr_eyl_sq:.6g}   vs   1/ALPHA = {1.0 / ALPHA:.6g}"
          f"   [match: {np.isclose(ecr_eyl_sq, 1.0 / ALPHA)}]")

    # --- 1. AVE index shift (manifestation of Axiom 4) -----------------------
    print("\n[1] AVE index shift  delta_n = sqrt(S) - 1 = (1-A^2)^(1/4) - 1  (Ax-4, eps-only):")
    print("    (NEGATIVE: the vacuum softens, n drops; E^2-leading, leading coeff -1/4)")
    dn_ave_x = delta_n_ave_exact(E_SWEEP)
    dn_ave_l = delta_n_ave_leading(E_SWEEP)
    print(f"    {'E (V/m)':>10}  {'A=E/E_yield':>12}  {'dn_AVE(exact)':>14}  {'dn_AVE(lead)':>13}")
    for E, dx, dl in zip(E_SWEEP, dn_ave_x, dn_ave_l):
        print(f"    {E:>10.2e}  {E / E_YIELD:>12.4e}  {dx:>14.4e}  {dl:>13.4e}")

    # --- 2. QED Euler-Heisenberg baseline (LITERATURE, single-mode) ----------
    a_eh_ref = A_EH_LITERATURE["single-mode parallel  (7/45)"]
    print(f"\n[2] QED Euler-Heisenberg baseline (LITERATURE, a_EH={a_eh_ref:.4f} single-mode):")
    print("    delta_n_QED = a_EH * alpha^2 * (E/E_CRIT)^2  (alpha^2-loop-suppressed)")
    dn_qed = delta_n_qed(E_SWEEP, a_eh_ref)
    print(f"    {'E (V/m)':>10}  {'dn_QED':>14}  {'dn_AVE/dn_QED':>14}")
    for E, dq, dx in zip(E_SWEEP, dn_qed, dn_ave_x):
        print(f"    {E:>10.2e}  {dq:>14.4e}  {abs(dx) / dq:>14.4e}")

    # --- 3. The discriminator: field-INDEPENDENT ratio = 1/(4 a_EH alpha^3) ---
    print("\n[3] THE DISCRIMINATOR — field-INDEPENDENT ratio  1/(4 a_EH alpha^3):")
    print("    (both responses E^2-leading => the ratio is the COEFFICIENT, constant in E)")
    # Verify field-independence using the leading-term AVE shift (exact arc bends
    # the ratio only as E -> E_yield; the discriminator is the leading coefficient).
    ratio_leading = abs(delta_n_ave_leading(E_SWEEP)) / delta_n_qed(
        E_SWEEP, a_eh_ref
    )
    print(f"    leading-term ratio across the sweep (a_EH={a_eh_ref:.4f}): "
          f"min={ratio_leading.min():.4e}  max={ratio_leading.max():.4e}")
    print(f"    field-INDEPENDENT (leading): {np.allclose(ratio_leading, ratio_leading[0])}"
          f"  ->  constant = {ratio_closed_form(a_eh_ref):.4e} = 1/(4 a_EH alpha^3)")

    print("\n    FULL prefactor band (flag-don't-fix, prereg §5.2 — corpus headline pins one):")
    print(f"    {'a_EH convention':<30}  {'a_EH':>8}  {'ratio 1/(4 a alpha^3)':>22}")
    for label, a in A_EH_LITERATURE.items():
        print(f"    {label:<30}  {a:>8.4f}  {ratio_closed_form(a):>22.4e}")
    band = [ratio_closed_form(a) for a in A_EH_LITERATURE.values()]
    print(f"    => headline band: [{min(band):.2e}, {max(band):.2e}]  "
          f"(robust verdict: AVE ~10^5-10^6x QED, ~6 OOM gap, AVE-distinct at ALL fields)")

    # --- 4. Measurability verdict --------------------------------------------
    print("\n[4] MEASURABILITY (delta_n_AVE vs a high-finesse-cavity floor "
          f"~{CAVITY_DN_FLOOR:.0e}):")
    for E, dx in zip(E_SWEEP, dn_ave_x):
        verdict = "MEASURABLE" if abs(dx) >= CAVITY_DN_FLOOR else "below floor"
        print(f"    E={E:.2e} V/m -> |dn_AVE|={abs(dx):.3e}  "
              f"(SNR vs floor {abs(dx) / CAVITY_DN_FLOOR:.2e})  [{verdict}]")
    print("    => at facility-class E ~ 1e14 V/m, dn_AVE ~ 2e-7 is high-finesse-cavity")
    print("       MEASURABLE; the ~10^6 coefficient gap to QED is present at ALL fields.")

    # --- 5. The two-sided falsifier ------------------------------------------
    print("\n[5] FALSIFIER (two-sided, prereg §4 — frozen, Rule 11):")
    print("    AVE-confirming : measured coeff ~ -1/4 (O(1)), ~10^6x the QED baseline.")
    print("    AVE-falsifying : a QED-SIZED coefficient (~alpha^2, ~10^6x smaller).")
    print("    QED-falsifying : an AVE-SIZED coefficient (at this observable).")
    print("    NOT a falsifier: an E^2 slope (both are E^2-leading; the prior")
    print("       'E^2 slope falsifies AVE' was a sqrt(eps) exponent conflation,")
    print("       corrected Part A, commit ad26d357).")

    # --- 6. The matched DIFFERENTIAL family: v3 consolidated chain (HEADLINE) --
    print("\n[6] MATCHED DIFFERENTIAL family — register/leaf clm-pp3qwf HEADLINE (Option-B v3):")
    print("    (distinct from the single-arm 1/(4 a_EH alpha^3) family in [3]; AVE leg is the")
    print("     par-perp DIFFERENTIAL -1/2 A^2, QED on the consistent INSTANTANEOUS footing)")
    chain = differential_ratio_v3_chain()
    print(f"    v1 = 7.5/alpha^3          = {chain['v1']:.4e}  "
          f"(SVE -1/2 A^2 over differenced (3/45)alpha^2)")
    print(f"      / (v1->v2 factor {chain['v1_to_v2_factor']:.4g})  "
          f"[propagating re-normalization 1/(pi alpha)]")
    print(f"    v2 = 7.5 pi/alpha^2       = {chain['v2']:.4e}  "
          f"(QED denom -> propagating alpha/(15 pi))")
    print(f"      x carrier {chain['v2_to_v3_carrier']:.3g}          "
          f"[<cos^2>=1/2 removed -> instantaneous footing]")
    print(f"    v3 = 3.75 pi/alpha^2      = {chain['v3']:.4e}  "
          f"= 15 pi/(4 alpha^2)  <-- THE HEADLINE (~2.2e5)")
    print(f"    chain closes: v1*(pi alpha)*(1/2) == 15 pi/(4 alpha^2): "
          f"{np.isclose(chain['v1'] * (np.pi * ALPHA) * 0.5, 15.0 * np.pi / (4.0 * ALPHA**2))}")
    print("    CLASSIFICATION: v3 magnitude is an alpha-ECHO (symmetric standard: QED equally")
    print("       alpha-rooted); the CHORD is tree-level O(1) saturation existence, not the number.")
    print("=" * 78)


if __name__ == "__main__":
    report()
