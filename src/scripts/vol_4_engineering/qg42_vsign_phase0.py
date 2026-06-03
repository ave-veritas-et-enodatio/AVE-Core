"""Q-G42 Phase-0 resume: tree-level V^2-coefficient SIGN test — magnitude gate.

RESUME of AVE-QED/docs/analysis/2026-05-13_Q-G42_v_yield_apparatus_scaling_prereg.md
(its section 4, Q1-Q3) and research/2026-06-03_yield-knee-map-prereg.md (the
reframe-to-V^2-sign spec). This script is the green-field Phase-0 calculator the
prereg demanded: it derives, FROM CANONICAL CONSTANTS ONLY, the numbers the
result doc reports.

THE REFRAME (settled, not re-litigated here):
  The literal saturation knee at V_yield is bench-unreachable — V_yield = 43.65 kV
  is the PER-NODE voltage (across l_node = 3.86e-13 m), not per-apparatus. A bench
  reaches a local saturation amplitude A ~ 3.8e-3 at best (PONDER Ch1:51: beta=1e3
  tip x Q=1e4 build-up). So the bench measures the SMALL-A TREE-LEVEL kernel, not
  the knee. The reachable AVE-distinct observable is the SIGN of the V^2 coefficient:

    AVE  : delta_eps/eps0 = sqrt(1 - A^2) - 1  ~  -A^2/2   (vacuum SOFTENS, negative)
    QED  : delta_eps/eps0 = +(4 alpha^2 / 9)(E/E_S)^2       (vacuum STIFFENS, positive)

  The two-sided binary (soften vs stiffen) discriminates without needing the knee
  or a magnitude match. Discrimination ratio ~8.38e12 (re-verified, IVIM adversarial
  doc 2026-06-03). Plus the even-2w harmonic (canonical parametric-coupling-kernel.md).

WHAT THIS SCRIPT COMPUTES (all from ave.core.constants — no hard-coded physics):
  1. Local hot-spot kernel delta_eps/eps0 at the bench A_hot, per beta-catalog tip.
  2. Method-B (autoresonant) BULK fractional resonance shift Df0/f0, accounting for
     (a) saturated-volume-fraction dilution in the bulk resonator,
     (b) the relation Df0/f0 ~= -1/2 * <Deps/eps>_bulk,
     (c) the resonator-Q resolution floor (Q sets what is RESOLVABLE, not signal size).
  3. Method-A (C-V) small-signal DC-bias dC/C and the even-2w parametric dC/C
     (canonical form dC = 1/4 C0 (V/V_yield)^2).
  4. The QED Euler-Heisenberg counterpart in the SAME observable + the sign + ratio.
  5. Per-architecture SNR vs the three resolution floors (1e-9 / 1e-12 / 1e-15).

NOTE on Q (load-bearing, flag-don't-fix): there are TWO distinct "Q"s here.
  - Q_build  : the resonant FIELD build-up that raises the local A_hot (PONDER's Q=1e4).
               This enters the SIGNAL (larger A_hot -> larger delta_eps).
  - Q_meas   : the resonator line-Q that sets the minimum RESOLVABLE Df0/f0 ~ 1/(Q*SNR).
               This enters the FLOOR, not the signal. The three architectures are
               distinguished by their resolvable-Df0/f0 floor, NOT by a multiplicative
               signal gain. The prereg's "resonator-Q amplification" is physically the
               resolution-floor mechanism; this script reports it that way (see report).
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA, E_CRIT, E_YIELD, L_NODE, V_YIELD

# ----------------------------------------------------------------------------
# Canonical anchors (ALL derived from ave.core.constants — zero hard-coded physics)
# ----------------------------------------------------------------------------
# E_YIELD == V_YIELD / L_NODE ~ 1.13e17 V/m   (per-node saturation field)
# E_CRIT  == Schwinger field  ~ 1.32e18 V/m
# sqrt(ALPHA) * E_CRIT == E_YIELD  (cross-check below)


def kernel_deltaeps(A: float | np.ndarray) -> float | np.ndarray:
    """AVE local dielectric kernel: delta_eps/eps0 = S(A) - 1 = sqrt(1-A^2) - 1.

    Exact (not the -A^2/2 small-A expansion), so the SIGN and the magnitude are
    both honest at any A < 1. Negative for all 0 < A < 1 -> the vacuum SOFTENS.
    """
    return np.sqrt(1.0 - np.asarray(A, dtype=float) ** 2) - 1.0


def kernel_deltaeps_qed(E: float | np.ndarray) -> float | np.ndarray:
    """QED Euler-Heisenberg + DC-Kerr static-field dielectric shift.

    delta_eps/eps0 = +(4 alpha^2 / 9)(E / E_Schwinger)^2.
    Same convention as the IVIM SM baseline (03_sm_baseline.tex / IVIM re-verify
    2026-06-03). POSITIVE -> the QED vacuum STIFFENS. This is the sign the AVE
    softening discriminates against.
    """
    return (4.0 * ALPHA**2 / 9.0) * (np.asarray(E, dtype=float) / E_CRIT) ** 2


def a_hot(beta: float, v_app: float, d_gap: float, q_build: float = 1.0) -> float:
    """Local saturation amplitude at the field-concentration hot spot.

    A_hot = (field-build-up Q) * beta * V_app / (d_gap * E_YIELD).
    beta = geometric field-enhancement; q_build = resonant field build-up (PONDER Q).
    """
    return q_build * beta * v_app / (d_gap * E_YIELD)


# ----------------------------------------------------------------------------
# beta / G_geom catalog (Q-G42 section 2.3) + the bench operating point
# ----------------------------------------------------------------------------
# Three corpus beta values, each defensible for a DIFFERENT geometry:
BETA_CATALOG = {
    "hemispherical-tip (curvature-only)": 30.0,        # bench-VM Paschen ch09:140
    "tip-array + Q-build (PONDER)": 1.0e3,             # PONDER ch1:51 operating pt
    "combined geom x resonant x ferro (App F)": 1.0e5,  # App F caption (no derivation)
}
G_FERRO = 3000.0  # BaTiO3 eps_r (Q-G42 section 2.5) — ferroelectric interface concentration

# The canonical bench operating point (PONDER ch1:51, verified to source):
#   30 kV across 1 mm, beta=1e3 tip, Q_build=1e4 -> A_local ~ 3.8e-3.
V_BENCH = 30.0e3      # 30 kV applied (PONDER ch1 operating point)
D_BENCH = 1.0e-3      # 1 mm gap
Q_BUILD_BENCH = 1.0e4  # resonant field build-up (PONDER Q=1e4)

# ----------------------------------------------------------------------------
# Saturated-volume-fraction dilution (the load-bearing bulk factor)
# ----------------------------------------------------------------------------
# The hot spot occupies a tiny fraction of the resonator volume. Away from it the
# tip-dipole field falls as E ~ 1/r^2, so A^2 ~ 1/r^4 and delta_eps ~ 1/r^4 — steeply
# localized. The BULK eigenfrequency shift is the volume-weighted local shift:
#
#   <delta_eps/eps0>_bulk = (1/V_res) * integral( delta_eps/eps0 dV )
#                         = -1/2 * A_hot^2 * eta_eff
#
# eta_eff = (1/V_res) * integral( A(r)^2 / A_hot^2 dV )  is the effective FIELD-FILLING
# fraction. For a hot feature of scale r_feat in a resonator of scale L_res with a
# 1/r^2 field falloff, integral(A^2 dV) ~ A_hot^2 * r_feat^3 * O(1) (the 1/r^4 integrand
# converges within a few r_feat), so eta_eff ~ (r_feat / L_res)^3 * (geometry O(1)).
#
# This is a PARAMETERIZED systematic (geometry-dependent), bracketed across a
# defensible range; the SIGN of the signal is geometry-INVARIANT (always negative).
ETA_EFF_RANGE = {
    "optimistic (tight resonator, r_feat/L_res ~ 1e-2)": (1.0e-2) ** 3,   # 1e-6
    "nominal    (r_feat/L_res ~ 1e-3)": (1.0e-3) ** 3,                    # 1e-9
    "conservative (large resonator, r_feat/L_res ~ 1e-4)": (1.0e-4) ** 3,  # 1e-12
}

# ----------------------------------------------------------------------------
# Detection-architecture resolution floors (Q-G42 section 4 Q3)
# ----------------------------------------------------------------------------
ARCHITECTURES = {
    "precision-bridge": 1.0e-9,    # precision capacitance bridge / commercial PLL
    "cryo-lock-in": 1.0e-12,       # cryogenic lock-in, next-gen
    "resonant-Q": 1.0e-15,         # resonant Q-enhanced, ultimate (Allan-floor class)
}


def df0_over_f0_bulk(deps_bulk: float) -> float:
    """Df0/f0 = -1/2 * <Deps/eps>_bulk  (LC: f0 = 1/(2 pi sqrt(LC)), C ~ eps)."""
    return -0.5 * deps_bulk


def dc_over_c_parametric(v_pump: float) -> float:
    """Even-2w parametric modulation amplitude: dC/C0 = 1/4 (V_pump/V_yield)^2.

    Canonical (parametric-coupling-kernel.md:70). The C_eff modulation rides at
    2*w_drive because cos^2 -> 1/2(1+cos 2wt). This is the AVE-distinct EVEN harmonic.
    """
    return 0.25 * (v_pump / V_YIELD) ** 2


def report() -> None:
    print("=" * 78)
    print("Q-G42 Phase-0 RESUME — tree-level V^2-coefficient SIGN test (magnitude gate)")
    print("=" * 78)

    # --- 0. Canonical cross-checks (no hidden free parameter) -----------------
    eyield_check = np.sqrt(ALPHA) * E_CRIT
    dratio = 9.0 / (8.0 * ALPHA**2) * (L_NODE * E_CRIT / V_YIELD) ** 2
    print("\n[0] Canonical anchors (all from ave.core.constants):")
    print(f"    V_YIELD = {V_YIELD:.6g} V    (per-node, across l_node)")
    print(f"    E_YIELD = {E_YIELD:.6g} V/m  (== V_YIELD/L_NODE)")
    print(f"    E_CRIT  = {E_CRIT:.6g} V/m  (Schwinger)")
    print(f"    sqrt(ALPHA)*E_CRIT = {eyield_check:.6g}  ==? E_YIELD  "
          f"[{'OK' if np.isclose(eyield_check, E_YIELD) else 'MISMATCH'}]")
    print(f"    discrimination ratio (delta_eps) = {dratio:.6g}  (expect 2.895e6)")
    print(f"    Gamma ratio = ratio^2 = {dratio**2:.6g}  (expect 8.381e12)")

    # --- 1. Local hot-spot kernel per beta catalog ----------------------------
    print("\n[1] Local hot-spot saturation amplitude A_hot + LOCAL delta_eps/eps0:")
    print(f"    bench operating point: V={V_BENCH/1e3:.0f} kV, d={D_BENCH*1e3:.0f} mm, "
          f"Q_build={Q_BUILD_BENCH:.0e}")
    for name, beta in BETA_CATALOG.items():
        A = a_hot(beta, V_BENCH, D_BENCH, Q_BUILD_BENCH)
        de = kernel_deltaeps(A)
        # QED counterpart at the same LOCAL field:
        E_local = Q_BUILD_BENCH * beta * V_BENCH / D_BENCH
        de_qed = kernel_deltaeps_qed(E_local)
        sign = "SOFTEN(-)" if de < 0 else "stiffen(+)"
        ratio = abs(de / de_qed) if de_qed != 0 else float("inf")
        print(f"    beta={beta:>8.0e}  A_hot={A:.3e}  "
              f"deps_AVE={de:+.3e} [{sign}]  deps_QED={de_qed:+.3e}  |AVE/QED|={ratio:.3e}")

    # Headline bench A (PONDER beta=1e3 case) — the canonical operating point:
    A_bench = a_hot(1.0e3, V_BENCH, D_BENCH, Q_BUILD_BENCH)
    de_bench_local = kernel_deltaeps(A_bench)
    print(f"\n    >>> CANONICAL bench A_hot = {A_bench:.3e}  (PONDER ch1:51 quotes ~3.8e-3)")
    print(f"    >>> LOCAL hot-spot delta_eps/eps0 = {de_bench_local:+.3e}  "
          f"(PONDER quotes 1-S ~ 7e-6)")

    # --- 2. Method B: BULK Df0/f0 with volume-fraction dilution ---------------
    print("\n[2] METHOD B (autoresonant) — bulk Df0/f0 = -1/2 <Deps/eps>_bulk:")
    print("    <Deps/eps>_bulk = -1/2 * A_hot^2 * eta_eff   (eta_eff = field-filling frac)")
    print(f"    using CANONICAL bench A_hot = {A_bench:.3e}")
    df0_by_eta: dict[str, float] = {}
    for eta_name, eta in ETA_EFF_RANGE.items():
        deps_bulk = -0.5 * A_bench**2 * eta
        df0 = df0_over_f0_bulk(deps_bulk)
        df0_by_eta[eta_name] = df0
        print(f"    eta_eff={eta:.1e}  <deps>_bulk={deps_bulk:+.3e}  "
              f"Df0/f0={df0:+.3e}")

    # --- 3. Method A: small-signal C-V + even-2w parametric --------------------
    print("\n[3] METHOD A (C-V) — small-signal dC/C and even-2w parametric:")
    # DC-bias small-signal: dC/C ~ -deps/eps = +1/2 A^2 (C = C0/S, so C RISES as eps softens)
    dC_dcbias_local = -de_bench_local  # +A^2/2 to leading order (C rises)
    print(f"    LOCAL DC-bias small-signal dC/C0 (hot spot) = {dC_dcbias_local:+.3e}  "
          f"(C RISES; eps softens)")
    # Even-2w parametric at a representative sub-yield bulk pump (canonical 18.7 kV pt):
    for vp_name, vp in {"bench bulk V (30 kV)": V_BENCH,
                        "canonical pump (18.7 kV)": 18.7e3}.items():
        dC2w = dc_over_c_parametric(vp)
        print(f"    even-2w dC/C0 @ {vp_name}: (V/V_yield)={vp/V_YIELD:.3f} -> "
              f"dC/C0={dC2w:.3e}")
    print("    NOTE: the 4.57% canonical figure is at V/V_yield=0.428 (18.7 kV pump),")
    print("          a BULK-pump operating point, NOT the diluted small-A bench shift.")

    # --- 4. Per-architecture SNR (Method B Df0/f0 vs resolution floors) --------
    print("\n[4] Per-architecture SNR = |Df0/f0| / resolution_floor   (Method B):")
    print("    (signal = nominal-eta bulk Df0/f0; floor = architecture resolvable Df0/f0)")
    df0_nominal = abs(df0_by_eta["nominal    (r_feat/L_res ~ 1e-3)"])
    df0_optimistic = abs(df0_by_eta["optimistic (tight resonator, r_feat/L_res ~ 1e-2)"])
    for arch, floor in ARCHITECTURES.items():
        snr_nom = df0_nominal / floor
        snr_opt = df0_optimistic / floor
        verdict = "DETECT" if snr_nom >= 1.0 else ("DETECT(opt)" if snr_opt >= 1.0 else "below")
        print(f"    {arch:<16s} floor={floor:.0e}  "
              f"SNR_nominal={snr_nom:.2e}  SNR_optimistic={snr_opt:.2e}  [{verdict}]")

    # --- 5. The sign discrimination (geometry-invariant) ----------------------
    print("\n[5] SIGN DISCRIMINATION (the AVE-distinct observable):")
    print("    AVE delta_eps/eps0 < 0 for ALL 0<A<1  -> vacuum SOFTENS  -> Df0/f0 > 0 "
          "(f0 RISES, C RISES)")
    print("    QED delta_eps/eps0 > 0                 -> vacuum STIFFENS -> Df0/f0 < 0 "
          "(f0 falls)")
    print("    The SIGN is geometry/material-INVARIANT for the vacuum component; the")
    print(f"    discrimination ratio |AVE/QED| ~ {dratio**2:.2e} on the V^4 (reflectance)")
    print(f"    observable, ~{dratio:.2e} on the V^2 (Df0/f0, deps-linear) observable.")
    print("=" * 78)


if __name__ == "__main__":
    report()
