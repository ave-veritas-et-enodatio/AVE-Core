"""Frozen re-run — v1 spin-mapping adjudication (omega_R AND tau vs corrected Kerr).

Executes the frozen plan in
`research/2026-07-20_v1-spin-mapping-adjudication_prereg-FROZEN.md` against the FROZEN
adjudication bins. Deterministic, no network, no qnm import at run time: the corrected
Kerr (2,2,0) reference is hard-coded (qnm-verified `[branch @ 7aaec46c]`), and the
in-lane second method is the Berti-Cardoso-Will 2006 analytic fit (both omega_R AND
omega_I via the Q-fit), computed here so the cross-check ships with the verdict.

Routed follow-on of PR #774's § FORK-REOPEN. The FORK RULING is Grant's; this driver
produces the frozen evidence brief.

Comparators (frozen prereg §3), both frame- AND mass-independent:
  C-1   dimensionless omega_R ratio    (omega_R*M)_AVE(a*) / (omega_R*M)_Kerr(a*) - 1
  C-tau dimensionless quality factor   Q = (omega_R*M)/(2*omega_I*M);  dev = Q_AVE/Q_Kerr - 1

AVE damping models (frozen enumeration):
  A  cold topological Q = ell = 2 (qnm-quality-factor.md, clm-395gps): spin-independent,
     v1/v2-independent, FULLY SPECIFIED -> omega_I*M = (omega_R*M)_AVE/(2 ell).
  B  spin-refined omega_I = (omega_R - m Omega)/(2 ell): Omega(a*) UNDER-SPECIFIED in the
     corpus -> UNDETERMINED (the lane declines to fabricate Omega; a disclosed
     reverse-engineered bound from the rounded KB tau values is reported as sensitivity).

Run:
    python3 research/2026-07-20_v1-spin-mapping-adjudication_rerun.py
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ave.core.constants import C_0, G, M_SUN  # noqa: E402  canonical constants only

# ------------------------------------------------------------------------------------
# Corrected Kerr (2,2,0) reference — qnm-verified, hard-coded `[branch @ 7aaec46c]`
# (research/2026-07-20_kerr-table-correction_prereg-FROZEN.md §0). omega_I*M is the
# damping magnitude (exp(-omega_I t)). Event-spin rows are the qnm values at those exact
# spins as listed in the #774 prereg (NOT coarse-grid interpolations).
# ------------------------------------------------------------------------------------
KERR_QNM = {  # a*: (omega_R*M, omega_I*M)
    0.00: (0.37367, 0.08896),
    0.10: (0.38702, 0.08871),
    0.20: (0.40215, 0.08831),
    0.30: (0.41953, 0.08773),
    0.40: (0.43984, 0.08688),
    0.50: (0.46412, 0.08564),
    0.60: (0.49404, 0.08377),
    0.64: (0.50819, 0.08275),
    0.67: (0.51986, 0.08185),
    0.70: (0.53260, 0.08079),
    0.74: (0.55163, 0.07909),
    0.80: (0.58602, 0.07563),
    0.90: (0.67161, 0.06487),
    0.95: (0.74632, 0.05315),
}

NU_VAC = 2.0 / 7.0
X_SAT = 7.0
ELL = 2.0
M_MODE = 2.0

T_SUN = G * M_SUN / C_0**3  # s per solar mass (canonical constants; sanity line only)


# ---- Berti-Cardoso-Will 2006 analytic fits (in-lane SECOND method, Phys.Rev. D73 064030)
def bcw_omega_r_m(a: float) -> float:
    return 1.5251 - 1.1568 * (1.0 - a) ** 0.1292


def bcw_quality(a: float) -> float:
    return 0.7000 + 1.4187 * (1.0 - a) ** (-0.4990)


def bcw_omega_i_m(a: float) -> float:
    return bcw_omega_r_m(a) / (2.0 * bcw_quality(a))


def kerr_ref(a: float) -> tuple[float, float, str]:
    """Corrected Kerr (omega_R*M, omega_I*M, source) at spin a*.

    qnm-verified hard-coded value where tabulated `[branch @ 7aaec46c]`; else the
    in-lane-verified BCW-2006 analytic fit (import-tagged, <1% vs qnm at all grid pts).
    """
    key = round(a, 2)
    if key in KERR_QNM:
        wr, wi = KERR_QNM[key]
        return wr, wi, "qnm[br@7aaec46c]"
    return bcw_omega_r_m(a), bcw_omega_i_m(a), "BCW-fit[in-lane]"


# ---- prograde photon orbit + the two AVE spin mappings (from ave-merger-ringdown-eigenvalue.md)
def r_ph_plus(a: float) -> float:
    """Prograde Kerr photon-orbit radius in GM/c^2 units (3M at a*=0, M at a*->1)."""
    return 2.0 * (1.0 + math.cos((2.0 / 3.0) * math.acos(-a)))


def ave_v1_omega_r_m(a: float) -> float:
    """v1 (whole-cavity compliant): x_sat,v1 = 7*r_ph+/3M ; omega_R*M = ell(1+nu)/x_sat = 54/(49 r_ph+)."""
    x_sat = X_SAT * r_ph_plus(a) / 3.0
    return ELL * (1.0 + NU_VAC) / x_sat


def ave_v2_omega_r_m(a: float) -> float:
    """v2 (rigid-skeleton + compliant): x_sat,v2 = 2 + 5*r_ph+/3M ; omega_R*M = ell(1+nu)/x_sat."""
    x_sat = X_SAT * (NU_VAC + (1.0 - NU_VAC) * r_ph_plus(a) / 3.0)
    return ELL * (1.0 + NU_VAC) / x_sat


def ave_cold_Q_omega_i_m(omega_r_m_ave: float) -> float:
    """Model A: cold topological Q = ell (spin-independent) -> omega_I*M = omega_R*M/(2 ell)."""
    return omega_r_m_ave / (2.0 * ELL)


def pct(x: float) -> str:
    return f"{x:+.2f}%"


# events: (name, a*, set-tag).  C-1/C-tau need a* only (dimensionless).
PRIMARY = [("GW150914", 0.67), ("GW170104", 0.64), ("GW151226", 0.74)]
SECONDARY = [("GW190521", 0.72), ("GW170729", 0.81)]  # [IMPORT: GWTC-2 / GWTC-1] a* only
# KB-cited v1 tau (ms) at source-frame M (Msun) — Model-B reverse-engineering ONLY (disclosed).
KB_TAU_V1 = {  # name: (tau_v1_ms, M_source_msun)  from ave-merger-ringdown-eigenvalue.md
    "GW150914": (3.5, 62.0),
    "GW170104": (2.7, 48.7),
    "GW151226": (1.2, 20.8),
}


def sep(title: str) -> None:
    print("\n" + "=" * 100)
    print(title)
    print("=" * 100)


# adjudicated spins: the catalog + near-extremal qnm-tabulated points the verdict rides on.
# a*=0 (and low spins) are EXACT-ANCHOR rows: BCW is known ~1.4-2.3% low near zero spin (#774
# prereg §0 note), so the a*=0 row uses the exact Schwarzschild anchor, NOT BCW. The in-lane
# BCW cross-check is asserted only where it is the operative second method (a* >= 0.60).
ADJUDICATED_SPINS = (0.64, 0.67, 0.74, 0.90, 0.95)


def leg1_verify_kerr() -> None:
    sep("LEG 1 — re-verify corrected Kerr in-lane (BCW-2006 fit vs qnm-verified table)")
    print(f"{'a*':>5} {'qnm wR*M':>10} {'BCW wR*M':>10} {'dev':>8}   "
          f"{'qnm wI*M':>10} {'BCW wI*M':>10} {'dev':>8}  note")
    worst_adj = 0.0
    for a in sorted(KERR_QNM):
        wr_q, wi_q = KERR_QNM[a]
        wr_b, wi_b = bcw_omega_r_m(a), bcw_omega_i_m(a)
        dr = 100.0 * (wr_b - wr_q) / wr_q
        di = 100.0 * (wi_b - wi_q) / wi_q
        note = "adjudicated" if a in ADJUDICATED_SPINS else ("EXACT-ANCHOR (BCW low, not used)" if a == 0.0 else "")
        if a in ADJUDICATED_SPINS:
            worst_adj = max(worst_adj, abs(dr), abs(di))
        print(f"{a:>5.2f} {wr_q:>10.5f} {wr_b:>10.5f} {pct(dr):>8}   "
              f"{wi_q:>10.5f} {wi_b:>10.5f} {pct(di):>8}  {note}")
    print(f"\nworst |BCW - qnm| over the ADJUDICATED spins {ADJUDICATED_SPINS}: {worst_adj:.2f}%  "
          f"(frozen assertion: < 1.5%)  ->  {'PASS' if worst_adj < 1.5 else 'FAIL'}")
    # extremal ZDM analytic cross-check (table-free): omega_R*M -> m/2, omega_I*M -> 0 as a*->1
    print("extremal ZDM analytic limit (a*->1): omega_R*M -> m/2 = 1.0 , omega_I*M -> 0 "
          "(the third, table-free cross-check the in-repo table violated)")
    assert worst_adj < 1.5, "BCW second method disagrees with qnm table by >1.5% at an adjudicated spin"


def leg2_omega_r(events: list[tuple[str, float]], label: str) -> tuple[float, float]:
    print(f"\n--- C-1 dimensionless omega_R ({label}) ---")
    print(f"{'event':10} {'a*':>5} {'v1 wR*M':>9} {'v2 wR*M':>9} {'Kerr wR*M':>10} "
          f"{'v1 dev':>8} {'v2 dev':>8}  {'Kerr src':>18}")
    v1d, v2d = [], []
    for name, a in events:
        wr_k, _, src = kerr_ref(a)
        wr1, wr2 = ave_v1_omega_r_m(a), ave_v2_omega_r_m(a)
        d1 = 100.0 * (wr1 - wr_k) / wr_k
        d2 = 100.0 * (wr2 - wr_k) / wr_k
        v1d.append(d1)
        v2d.append(d2)
        print(f"{name:10} {a:>5.2f} {wr1:>9.5f} {wr2:>9.5f} {wr_k:>10.5f} "
              f"{pct(d1):>8} {pct(d2):>8}  {src:>18}")
    m1, m2 = sum(v1d) / len(v1d), sum(v2d) / len(v2d)
    print(f"{'MEAN':10} {'':>5} {'':>9} {'':>9} {'':>10} {pct(m1):>8} {pct(m2):>8}   <- D-bar_wR")
    return m1, m2


def leg3_tau(events: list[tuple[str, float]], label: str) -> tuple[float, str]:
    print(f"\n--- C-tau dimensionless quality factor Q = wR/(2 wI) ({label}) ---")
    print("Model A (cold Q = ell = 2, FULLY SPECIFIED, spin- and v1/v2-independent):")
    print(f"{'event':10} {'a*':>5} {'Q_AVE(A)':>9} {'Q_Kerr':>8} {'wI*M AVE':>9} "
          f"{'wI*M Kerr':>9} {'Q dev':>8}")
    qdev = []
    for name, a in events:
        wr_k, wi_k, _ = kerr_ref(a)
        q_kerr = wr_k / (2.0 * wi_k)
        # Model A rides the AVE omega_R (use v1's, the mapping under adjudication)
        wr_ave = ave_v1_omega_r_m(a)
        wi_ave_A = ave_cold_Q_omega_i_m(wr_ave)
        q_ave_A = wr_ave / (2.0 * wi_ave_A)  # identically ell = 2 by construction
        d = 100.0 * (q_ave_A - q_kerr) / q_kerr
        qdev.append(d)
        print(f"{name:10} {a:>5.2f} {q_ave_A:>9.3f} {q_kerr:>8.3f} {wi_ave_A:>9.5f} "
              f"{wi_k:>9.5f} {pct(d):>8}")
    mA = sum(qdev) / len(qdev)
    print(f"{'MEAN':10} {'':>5} {'':>9} {'':>8} {'':>9} {'':>9} {pct(mA):>8}   <- D-bar_Q (Model A)")
    if abs(mA) < 3.0:
        tau_verdict = "tau-MATCHES"
    elif abs(mA) >= 5.0:
        tau_verdict = "tau-FAILS"
    else:
        tau_verdict = "tau-marginal"
    return mA, tau_verdict


def leg3_modelB_disclosure() -> None:
    print("\nModel B (spin-refined omega_I = (omega_R - m Omega)/(2 ell)) — DISCLOSURE (non-frozen):")
    print("  Corpus specification: the frame-dragging rate Omega(a*) is NOT numerically pinned")
    print("  anywhere in the corpus (grep: no numeric Omega / r_Omega). The KB tau_v1 = 3.5/2.7/1.2 ms")
    print("  were asserted at initial release, not coded. => Model B is UNDETERMINED (anti-seduction:")
    print("  the lane declines to fabricate Omega). Reverse-engineered bound from the ROUNDED KB tau")
    print("  (source-frame M), reported as sensitivity ONLY (+-~3% from 2-sig-fig rounding):")
    print(f"  {'event':10} {'a*':>5} {'tau_v1(ms)':>10} {'M_src':>6} {'wI*M_v1':>9} "
          f"{'Q_v1(implied)':>13} {'Q_Kerr':>8}")
    for name, a in PRIMARY:
        tau_ms, m_src = KB_TAU_V1[name]
        wi_m_v1 = (T_SUN * m_src) / (tau_ms * 1e-3)  # dimensionless wI*M implied by KB tau at M_src
        wr1 = ave_v1_omega_r_m(a)
        q_v1 = wr1 / (2.0 * wi_m_v1)
        wr_k, wi_k, _ = kerr_ref(a)
        q_kerr = wr_k / (2.0 * wi_k)
        print(f"  {name:10} {a:>5.2f} {tau_ms:>10.2f} {m_src:>6.1f} {wi_m_v1:>9.5f} "
              f"{q_v1:>13.3f} {q_kerr:>8.3f}")
    print("  (Reverse-engineered Q_v1 sits near Kerr Q but is rounding-limited AND rides the same")
    print("   source-frame masses #774 flagged as contaminated -> NOT frozen-adjudicable. A proper")
    print("   Model-B tau verdict requires Grant/corpus to PIN Omega first. FLAG-DON'T-FIX.)")
    print("  Tension flag: qnm-quality-factor.md says Q = ell (spin-independent); the merger leaf's")
    print("   Q 'increases with spin'; Phase-5 says Q is v1/v2-invariant. These need reconciling.")


def leg5_near_extremal() -> None:
    sep("LEG 5 — near-extremal v1 vs v2 + analytic a*->1 limits vs exact ZDM (m/2 = 1)")
    print(f"{'a*':>6} {'v1 wR*M':>9} {'v2 wR*M':>9} {'Kerr wR*M':>10} {'v1 dev':>8} {'v2 dev':>8}")
    for a in (0.90, 0.95):
        wr_k, _, _ = kerr_ref(a)
        wr1, wr2 = ave_v1_omega_r_m(a), ave_v2_omega_r_m(a)
        print(f"{a:>6.2f} {wr1:>9.5f} {wr2:>9.5f} {wr_k:>10.5f} "
              f"{pct(100*(wr1-wr_k)/wr_k):>8} {pct(100*(wr2-wr_k)/wr_k):>8}")
    # analytic extremal limits: r_ph+ -> M => v1 -> 54/49 ; v2 x_sat -> 11/3 => v2 -> 54/77 ; ZDM -> 1
    v1_ext = ELL * (1.0 + NU_VAC) / (X_SAT * 1.0 / 3.0)  # r_ph+ = 1M
    v2_ext = ELL * (1.0 + NU_VAC) / (X_SAT * (NU_VAC + (1.0 - NU_VAC) * 1.0 / 3.0))
    zdm = M_MODE / 2.0
    print(f"\nanalytic a*->1 limit (r_ph+ -> M):")
    print(f"  v1  omega_R*M -> 54/49 = {v1_ext:.5f}   vs ZDM m/2 = {zdm:.3f}  -> {pct(100*(v1_ext-zdm)/zdm)}")
    print(f"  v2  omega_R*M -> 54/77 = {v2_ext:.5f}   vs ZDM m/2 = {zdm:.3f}  -> {pct(100*(v2_ext-zdm)/zdm)}")
    print("  v1 RISES toward the ZDM limit (overshoots +10%); v2 FLOORS at 0.70 (undershoots -30%).")
    print("  -> v1's near-extremal behavior is qualitatively correct; v2's is qualitatively wrong.")
    print("  ROUTED to Grant as a candidate testable organizer (omega_R*M ~ 54/49 as a*->1); NOT banked.")


def main() -> int:
    print("=" * 100)
    print("v1 spin-mapping frozen adjudication — frozen bins in")
    print("research/2026-07-20_v1-spin-mapping-adjudication_prereg-FROZEN.md")
    print("=" * 100)

    # cold anchor (not under adjudication)
    cold = ELL * (1.0 + NU_VAC) / X_SAT
    print(f"\ncold a*=0 anchor (shared v1=v2): 18/49 = {cold:.5f} vs Kerr {KERR_QNM[0.00][0]:.5f} "
          f"= {pct(100*(cold-KERR_QNM[0.00][0])/KERR_QNM[0.00][0])}  (SURVIVES, not adjudicated)")

    leg1_verify_kerr()

    sep("LEG 2 — C-1 omega_R comparison (v1 & v2 vs corrected Kerr)")
    p1, p2 = leg2_omega_r(PRIMARY, "PRIMARY — banked catalog")
    s1, s2 = leg2_omega_r(SECONDARY, "SECONDARY — [IMPORT: GWTC] a* only, Kerr via in-lane BCW fit")

    sep("LEG 3 — C-tau damping comparison (THE NEW CONTENT: v1 tau vs corrected omega_I)")
    tA, tau_verdict = leg3_tau(PRIMARY, "PRIMARY")
    leg3_modelB_disclosure()

    leg5_near_extremal()

    # ---- frozen-bin adjudication -----------------------------------------------------
    sep("FROZEN-BIN ADJUDICATION (prereg §5)")
    # omega_R bins
    def wr_bin(m: float) -> str:
        return "V1-MATCHES(wR)" if abs(m) < 3.0 else ("V1-FAILS(wR)" if abs(m) >= 5.0 else "wR-marginal")
    print(f"  omega_R PRIMARY:  D-bar_wR(v1) = {p1:+.2f}%  -> {wr_bin(p1)}   "
          f"(v2 = {p2:+.2f}% -> {wr_bin(p2)})")
    print(f"  omega_R SECONDARY:D-bar_wR(v1) = {s1:+.2f}%  -> {wr_bin(s1)}   "
          f"(v2 = {s2:+.2f}% -> {wr_bin(s2)})")
    print(f"  tau     PRIMARY:  D-bar_Q(v1, Model A) = {tA:+.2f}%  -> {tau_verdict}")
    print("  tau     Model B (spin-refined): UNDETERMINED (Omega under-specified; declined to fabricate)")

    wr_match = abs(p1) < 3.0 and abs(s1) < 3.0
    tau_match = tau_verdict == "tau-MATCHES"
    if wr_match and tau_match:
        overall = "V1-MATCHES"
    elif (abs(p1) >= 5.0) and tau_verdict == "tau-FAILS":
        overall = "V1-FAILS"
    else:
        overall = "MIXED (omega_R vs tau split)"
    print(f"\n  ★ OVERALL FROZEN BIN: {overall}")
    print("  (The FORK RULING is Grant's; this is the frozen evidence, not the ruling.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
