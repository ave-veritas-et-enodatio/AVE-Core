"""Q-G42 Phase-1: small-signal autoresonant Df0/f0 V^2-sign FORWARD calculator.

PHASE-1 hardening of the tree-level V^2-coefficient SIGN test. Extends the
Phase-0 magnitude gate (qg42_vsign_phase0.py) with:
  (1) the closed-form small-signal autoresonant Df0/f0 = +1/4 * A_RMS^2 * eta_eff,
      hardened against the canonical four-regime map (regimes-of-operation.md),
  (2) the beta/G_geom reconciliation against the canonical Fowler-Nordheim
      ELECTRODE-DESTRUCTION limit (17_noise_floor_boundary.tex: beta_crit ~ 6,
      FN-safe local-field ceiling ~1.3e9 V/m), decomposing G_geom = beta * Q_build
      and computing the FN-safe A ceiling,
  (3) the DUAL-CAMP reachability columns (honest camp: bench in Regime I,
      E/E_yield ~ 2.7e-10; conflated camp: apparatus V read as per-node V_yield,
      V/V_yield ~ 0.85). The corpus contradiction is FLAGGED, not resolved
      (flag-don't-fix; see research/2026-06-04_qg42-phase1-prereg.md §4).

FORWARD-PREDICTION DISCIPLINE (ave-driver-script-honesty):
  This script computes Df0/f0 FORWARD from ave.core.constants + a swept geometry
  (G_geom = beta*Q_build, eta_eff). There is NO fit-to-target: no minimize(),
  no curve_fit(), no empirical_target import, no inverse solve. Every physics
  constant is imported from ave.core.constants. The empirical FN coefficients
  (A_FN, B_FN, phi) are labeled inputs from the canonical experimental chapter
  (17_noise_floor_boundary.tex), NOT AVE-derived predictions. The QED counterfactor
  is a labeled other-framework (Euler-Heisenberg) reference, not an AVE result.

THE OBSERVABLE + ITS CLASSIFICATION (consistency-vs-emergence, prereg §3):
  Df0/f0 MAGNITUDE: Class B (axiom manifestation) — IS the Axiom-4 kernel at the
    resonator scale; inherits the sqrt(alpha) kernel-magnitude Class-B status
    (honest-alpha relabel 2026-06-02).
  Df0/f0 SIGN: the load-bearing AVE-distinct content, ROBUST to the sqrt(alpha)
    magnitude uncertainty. AVE: Df0/f0 > 0 (resonance RISES, vacuum softens).
    QED: Df0/f0 < 0 (resonance falls, vacuum stiffens). A two-sided forward binary.

THE KERNEL (Axiom 4, A-034 row 1):
    AVE  : delta_eps/eps0 = sqrt(1 - A^2) - 1  ~  -A^2/2   (SOFTENS, negative)
    QED  : delta_eps/eps0 = +(4 alpha^2 / 9)(E/E_S)^2       (STIFFENS, positive)
  A = E_local / E_YIELD is the local saturation amplitude on the quarter-arc.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA, E_CRIT, E_YIELD, EPSILON_0, L_NODE, V_YIELD

# ----------------------------------------------------------------------------
# Canonical AVE kernel + QED counterfactor (all physics from ave.core.constants)
# ----------------------------------------------------------------------------


def kernel_deltaeps(A: float | np.ndarray) -> float | np.ndarray:
    """AVE local dielectric kernel: delta_eps/eps0 = S(A) - 1 = sqrt(1-A^2) - 1.

    Exact (not the -A^2/2 small-A expansion). Negative for all 0 < A < 1 ->
    the vacuum SOFTENS. This is the canonical Axiom-4 form (A-034 row 1).
    """
    return np.sqrt(1.0 - np.asarray(A, dtype=float) ** 2) - 1.0


def kernel_deltaeps_qed(E: float | np.ndarray) -> float | np.ndarray:
    """QED Euler-Heisenberg + DC-Kerr static-field dielectric shift (REFERENCE).

    delta_eps/eps0 = +(4 alpha^2 / 9)(E / E_Schwinger)^2. POSITIVE -> the QED
    vacuum STIFFENS. Labeled other-framework reference, not an AVE result.
    """
    return (4.0 * ALPHA**2 / 9.0) * (np.asarray(E, dtype=float) / E_CRIT) ** 2


# ----------------------------------------------------------------------------
# Closed-form small-signal autoresonant Df0/f0 (the Phase-1 green-field deliverable)
# ----------------------------------------------------------------------------


def a_rms_local(g_geom: float, v_app: float, d_gap: float) -> float:
    """Local hot-spot RMS saturation amplitude A_RMS = G_geom * V_app / (d * E_YIELD).

    G_geom is the TOTAL field-concentration factor = beta (geometric tip) *
    Q_build (resonant field build-up). Returns the RMS-convention amplitude
    (peak A_peak = sqrt(2) * A_RMS per PONDER ch1:122 peak convention).
    """
    return g_geom * v_app / (d_gap * E_YIELD)


def df0_over_f0(a_rms: float, eta_eff: float) -> float:
    """Closed-form small-signal autoresonant fractional resonance shift.

        <delta_eps/eps0>_bulk = -1/2 * A_RMS^2 * eta_eff   (volume-weighted, Ax 4)
        Df0/f0 = -1/2 * <delta_eps/eps0>_bulk = +1/4 * A_RMS^2 * eta_eff

    POSITIVE (resonance RISES) because the softening (eps down) raises f0 of the
    LC tank f0 = 1/(2 pi sqrt(LC)), C proportional to eps. This is the AVE-distinct
    SIGN. eta_eff is the field-filling fraction (geometry-dependent dilution).
    """
    return 0.25 * a_rms**2 * eta_eff


def df0_over_f0_exact(a_rms: float, eta_eff: float) -> float:
    """Exact-kernel version (no small-A expansion), for the conflated-camp regime.

    Uses the volume-weighted EXACT kernel S(A_RMS)-1 instead of the -A_RMS^2/2
    leading term. Agrees with df0_over_f0 to <1% for A_RMS < 0.1; diverges as
    A_RMS -> 1 (the knee). Df0/f0 = -1/2 * eta_eff * (sqrt(1-A_RMS^2) - 1).
    """
    deps_bulk = eta_eff * (np.sqrt(1.0 - a_rms**2) - 1.0)
    return -0.5 * deps_bulk


# ----------------------------------------------------------------------------
# Canonical Fowler-Nordheim ELECTRODE-DESTRUCTION limit (the beta-reconcile)
# ----------------------------------------------------------------------------
# From 17_noise_floor_boundary.tex eq:fowler_nordheim. These are LABELED INPUTS
# from the canonical experimental chapter, NOT AVE-derived. They reproduce the
# tex table (beta=3 SAFE, beta=6 MARGINAL, beta=50 DESTRUCTIVE) exactly.
A_FN: float = 1.54e-6   # A*eV/V^2  (input: 17_noise_floor_boundary.tex:32)
B_FN: float = 6.83e9    # eV^-3/2 V/m (input: same)
PHI_W: float = 4.5      # eV, tungsten work function (input: same)
# The canonical FN-safe local-field ceiling: beta=3 (E_local=1.31e9 V/m) is SAFE
# (J_FN ~ 1.4e-18 A); beta=6 (2.62e9 V/m) is MARGINAL. We take 1.31e9 V/m as the
# FN-safe DC surface-field ceiling per the tex table verdict.
E_FN_SAFE_CEILING: float = 1.31e9   # V/m (DC surface field, electropolished beta~3)


def j_fn(beta: float, e_gap: float) -> float:
    """Fowler-Nordheim dark-current density [A/m^2] (LABELED experimental input).

    J_FN = A_FN (beta E)^2 / phi * exp(-B_FN phi^1.5 / (beta E)). Reproduces
    17_noise_floor_boundary.tex table. NOT an AVE prediction.
    """
    b_e = beta * e_gap
    return A_FN * b_e**2 / PHI_W * np.exp(-B_FN * PHI_W**1.5 / b_e)


def a_fn_safe_max() -> float:
    """Max FN-safe local saturation amplitude A_max = E_FN_SAFE_CEILING / E_YIELD.

    The DC field-emission destruction limit caps the sustained local surface
    field at ~1.31e9 V/m (electropolished, beta~3). The corresponding A ceiling
    is the hard constraint on any DC-enhancement architecture.
    """
    return E_FN_SAFE_CEILING / E_YIELD


# ----------------------------------------------------------------------------
# Dual-camp reachability (FLAGGED corpus contradiction — prereg §4, NOT resolved)
# ----------------------------------------------------------------------------
# HONEST camp (regimes-of-operation.md:32, claim-quality.md:158, Q-G42):
#   V_yield is PER-NODE. 30 kV / 1 mm -> E/E_yield ~ 2.7e-10 (Regime I). The bench
#   reaches A ~ 1e-3 ONLY via aggressive concentration (G_geom = beta*Q_build).
# CONFLATED camp (measurement-hierarchy-snr.md:66, 17_noise_floor_boundary.tex,
#   nonlinear-vacuum-capacitance.md C-V table):
#   apparatus voltage 30-43 kV read AS the per-node V_yield -> V/V_yield ~ 0.85,
#    delta_C/C0 ~ 90% (macroscopic, any LCR meter).
# The two camps differ by ~12 OOM in predicted signal. NOT adjudicated here.

# Detection-architecture resolution floors (Q-G42 §4 Q3):
ARCHITECTURES = {
    "precision-bridge": 1.0e-9,
    "cryo-lock-in": 1.0e-12,
    "resonant-Q": 1.0e-15,
}

# The honest-camp PONDER operating point (regimes-of-operation.md:32, PONDER ch1:122):
V_BENCH: float = 30.0e3      # 30 kV applied
D_BENCH: float = 1.0e-3      # 1 mm gap
BETA_TIP: float = 1.0e3      # geometric tip enhancement (PONDER ch1:116, beta=h/r)
Q_BUILD: float = 1.0e4       # resonant field build-up (PONDER ch1:122)
G_GEOM_PONDER: float = BETA_TIP * Q_BUILD   # total concentration = 1e7

# eta_eff field-filling fraction bracket (geometry-dependent dilution):
ETA_EFF = {
    "optimistic (r_feat/L_res ~ 1e-2)": (1.0e-2) ** 3,   # 1e-6
    "nominal    (r_feat/L_res ~ 1e-3)": (1.0e-3) ** 3,   # 1e-9
    "conservative (r_feat/L_res ~ 1e-4)": (1.0e-4) ** 3,  # 1e-12
}


def report() -> None:
    print("=" * 78)
    print("Q-G42 Phase-1 — small-signal autoresonant Df0/f0 V^2-sign FORWARD calc")
    print("=" * 78)

    # --- 0. Canonical anchors -------------------------------------------------
    eyield_check = np.sqrt(ALPHA) * E_CRIT
    dratio = 9.0 / (8.0 * ALPHA**2) * (L_NODE * E_CRIT / V_YIELD) ** 2
    print("\n[0] Canonical anchors (from ave.core.constants):")
    print(f"    V_YIELD={V_YIELD:.6g} V  E_YIELD={E_YIELD:.6g} V/m  E_CRIT={E_CRIT:.6g} V/m")
    print(f"    sqrt(ALPHA)*E_CRIT == E_YIELD : "
          f"{'OK' if np.isclose(eyield_check, E_YIELD) else 'MISMATCH'}")
    print(f"    C0 = eps0*L_NODE = {EPSILON_0 * L_NODE:.6g} F  (per-node)")
    print(f"    discrimination ratio (V^2) = {dratio:.6g}  (expect 2.895e6)")
    print(f"    Gamma ratio (V^4)          = {dratio**2:.6g}  (expect 8.381e12)")

    # --- 1. The closed-form Df0/f0 (honest camp, PONDER operating point) ------
    a_rms = a_rms_local(G_GEOM_PONDER, V_BENCH, D_BENCH)
    print("\n[1] CLOSED-FORM Df0/f0 = +1/4 * A_RMS^2 * eta_eff  (HONEST camp, Regime I/II):")
    print(f"    G_geom = beta*Q_build = {BETA_TIP:.0e}*{Q_BUILD:.0e} = {G_GEOM_PONDER:.0e}")
    print(f"    A_RMS = G_geom*V/(d*E_YIELD) = {a_rms:.4e}  "
          f"(peak = sqrt2*A_RMS = {np.sqrt(2) * a_rms:.4e}, PONDER ch1:122 ~3.8e-3)")
    print(f"    LOCAL delta_eps/eps0 = {kernel_deltaeps(a_rms):+.3e}  (A_RMS^2/2)")
    for name, eta in ETA_EFF.items():
        df = df0_over_f0(a_rms, eta)
        df_x = df0_over_f0_exact(a_rms, eta)
        print(f"    eta_eff={eta:.0e}  Df0/f0={df:+.3e}  (exact-kernel {df_x:+.3e})  "
              f"[{'RISES' if df > 0 else 'falls'}]")

    # --- 2. beta-reconcile: Fowler-Nordheim electrode-destruction limit -------
    print("\n[2] BETA/G_geom RECONCILE vs canonical FN electrode-destruction limit:")
    e_gap_43 = V_YIELD / 100e-6
    print(f"    FN table reproduction (17_noise_floor_boundary.tex, E_gap={e_gap_43:.3g} V/m):")
    for b, status in [(3, "SAFE"), (6, "MARGINAL"), (50, "DESTRUCTIVE")]:
        print(f"      beta={b:>3}: E_local={b * e_gap_43:.2e} V/m  "
              f"J_FN={j_fn(b, e_gap_43):.1e} A/m^2  [{status}]")
    a_max = a_fn_safe_max()
    print(f"    FN-safe DC surface-field ceiling = {E_FN_SAFE_CEILING:.3g} V/m (beta~3)")
    print(f"    => FN-safe MAX local A (DC) = {a_max:.3e}")
    e_local_ponder = G_GEOM_PONDER * V_BENCH / D_BENCH
    print(f"    PONDER E_local (beta*Q*E_macro) = {e_local_ponder:.3e} V/m  "
          f"=> {e_local_ponder / E_FN_SAFE_CEILING:.1e}x the FN-safe DC ceiling")
    print("    *** CONTRADICTION (flag-don't-fix): the PONDER beta*Q operating point's")
    print("        local field is ~5 OOM above the FN-safe DC ceiling. PONDER ch1:126")
    print("        argues the tips are 'regime-bouncing' (transient RF peak, not")
    print("        sustained DC) => FN-destruction may be evaded per-half-cycle, but")
    print("        PONDER ch1:168 itself flags this as an OPEN engineering question.")

    # --- 3. Dual-camp reachability (FLAGGED, not resolved) --------------------
    print("\n[3] DUAL-CAMP reachability (corpus contradiction — flag-don't-fix):")
    e_macro = V_BENCH / D_BENCH
    print(f"    HONEST camp (per-node V_yield): E_macro/E_YIELD = {e_macro / E_YIELD:.2e} "
          "(Regime I; regimes-of-operation.md:32)")
    print(f"      -> bench A reaches ~{a_rms:.1e} ONLY via G_geom={G_GEOM_PONDER:.0e}")
    print("    CONFLATED camp (apparatus V read as per-node V_yield):")
    a_conflated = 0.85
    print(f"      V/V_yield ~ {a_conflated} -> delta_C/C0 = "
          f"{1.0 / np.sqrt(1 - a_conflated**2) - 1.0:+.1%} "
          "(macroscopic; 17_noise_floor_boundary.tex:84)")
    print("      The two camps differ by ~12 OOM in signal. NOT adjudicated (needs Grant).")

    # --- 4. Per-architecture SNR (honest camp) --------------------------------
    print("\n[4] Per-architecture SNR (HONEST camp, signal = Df0/f0 vs floor):")
    df_nom = df0_over_f0(a_rms, ETA_EFF["nominal    (r_feat/L_res ~ 1e-3)"])
    df_opt = df0_over_f0(a_rms, ETA_EFF["optimistic (r_feat/L_res ~ 1e-2)"])
    for arch, floor in ARCHITECTURES.items():
        snr_n, snr_o = abs(df_nom) / floor, abs(df_opt) / floor
        verdict = "DETECT" if snr_n >= 1 else ("DETECT(opt)" if snr_o >= 1 else "below")
        print(f"    {arch:<16s} floor={floor:.0e}  "
              f"SNR_nom={snr_n:.2e}  SNR_opt={snr_o:.2e}  [{verdict}]")

    # --- 5. The SIGN discrimination (the AVE-distinct content) -----------------
    print("\n[5] SIGN DISCRIMINATION (robust to sqrt(alpha) magnitude uncertainty):")
    print("    AVE: delta_eps/eps0 < 0 (all 0<A<1) -> Df0/f0 > 0 -> resonance RISES")
    print("    QED: delta_eps/eps0 > 0             -> Df0/f0 < 0 -> resonance FALLS")
    print(f"    Two-sided forward binary; discrimination ratio {dratio:.2e} (V^2) / "
          f"{dratio**2:.2e} (V^4).")
    print("    The SIGN is fixed by the kernel FORM (Ax 4), independent of the")
    print("    sqrt(alpha) kernel-magnitude (Class-B). This is the forward discriminator.")
    print("=" * 78)


if __name__ == "__main__":
    report()
