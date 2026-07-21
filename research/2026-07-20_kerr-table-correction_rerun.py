"""Frozen re-run — Kerr-table-correction lane (upstream of PR #772).

Executes the frozen plan in `research/2026-07-20_kerr-table-correction_prereg-FROZEN.md`
against the FROZEN adjudication bins. Deterministic, no network, no qnm import at run
time: the corrected Kerr (2,2,0) reference is hard-coded (qnm-verified this session,
cross-checked by the BCW-2006 fit and the PR #772 auditor's from-scratch Leaver).

Comparators (frozen prereg §1):
  C-1  dimensionless eigenvalue ratio  (omega_R*M)_AVE-v2 / (omega_R*M)_Kerr - 1
       — frame- AND mass-independent; depends only on the (well-measured) spin a*.
  C-2  detector-frame frequency        f_AVE-v2(M_det) vs f_obs   [M_det = M_src*(1+z)]
  C-3  GR sanity gate                   f_Kerr(M_det) vs f_obs     (must ~ reproduce obs)
  BANK reconstruction                   f_AVE-v2(M_src) vs f_obs   (must reproduce leaf -0.45%)

Run:
    python3 research/2026-07-20_kerr-table-correction_rerun.py
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ave.core.constants import C_0, G, M_SUN  # noqa: E402  canonical constants only

# --- corrected Kerr (2,2,0) reference, qnm-verified (prereg §0) -----------------
KERR_OMEGA_R_M = {
    0.00: 0.37367, 0.10: 0.38702, 0.20: 0.40215, 0.30: 0.41953, 0.40: 0.43984,
    0.50: 0.46412, 0.60: 0.49404, 0.64: 0.50819, 0.67: 0.51986, 0.70: 0.53260,
    0.74: 0.55163, 0.80: 0.58602, 0.90: 0.67161, 0.95: 0.74632,
}
# in-repo table BEFORE this lane's fix (for the BANK/GR-artifact reconstruction)
KERR_OMEGA_R_M_OLD = {
    0.00: 0.37368, 0.60: 0.46378, 0.64: 0.47133, 0.67: 0.47700, 0.70: 0.48267,
    0.74: 0.49146, 0.80: 0.50465, 0.90: 0.53039, 0.95: 0.54652,
}

NU_VAC = 2.0 / 7.0
X_SAT = 7.0
ELL = 2.0

# physical constants — canonical (ave.core.constants), never hard-coded
T_SUN = G * M_SUN / C_0**3  # s per solar mass


def ave_v2_omega_r_m(a):
    """Unchanged v2 formula: x_sat(a*) = 2 + 5*r_ph+(a*)/3M ; omega_R*M = l(1+nu)/x_sat."""
    r_ph_plus = 2.0 * (1.0 + math.cos((2.0 / 3.0) * math.acos(-a)))
    x_sat = X_SAT * (NU_VAC + (1.0 - NU_VAC) * r_ph_plus / 3.0)
    return ELL * (1.0 + NU_VAC) / x_sat


def f_hz(omega_r_m, m_msun):
    return (omega_r_m / (T_SUN * m_msun)) / (2.0 * math.pi)


# events: name, M_source(Msun), z, a*, f_obs_detector(Hz)  (imports per prereg §1 C-2)
EVENTS = [
    ("GW150914", 62.0, 0.09, 0.67, 251.0),
    ("GW170104", 48.7, 0.18, 0.64, 312.0),
    ("GW151226", 20.8, 0.09, 0.74, 750.0),
]


def main():
    print("=" * 100)
    print("Kerr-table-correction re-run — frozen bins in "
          "research/2026-07-20_kerr-table-correction_prereg-FROZEN.md")
    print("=" * 100)

    print("\nCold eigenvalue (NOT under adjudication; genuine zero-free-parameter result):")
    cold = ELL * (1.0 + NU_VAC) / X_SAT  # 18/49
    print(f"  a*=0: AVE 18/49 = {cold:.5f} vs Kerr {KERR_OMEGA_R_M[0.00]:.5f}  "
          f"= {100*(cold - KERR_OMEGA_R_M[0.00])/KERR_OMEGA_R_M[0.00]:+.2f}%  (SURVIVES)")

    print("\n--- C-1  dimensionless eigenvalue ratio (frame- & mass-independent) ---")
    print(f"{'event':10} {'a*':>5} {'AVEv2 wRM':>10} {'Kerr wRM':>10} {'C-1 dev':>9}")
    c1_devs = []
    for name, m_src, z, a, f_obs in EVENTS:
        ave = ave_v2_omega_r_m(a)
        kerr = KERR_OMEGA_R_M[a]
        dev = 100.0 * (ave - kerr) / kerr
        c1_devs.append(dev)
        print(f"{name:10} {a:>5.2f} {ave:>10.5f} {kerr:>10.5f} {dev:>+8.2f}%")
    c1_mean = sum(c1_devs) / len(c1_devs)
    print(f"{'MEAN':10} {'':>5} {'':>10} {'':>10} {c1_mean:>+8.2f}%   <-- honest deviation D-bar")

    print("\n--- C-2 detector-frame frequency  &  C-3 GR sanity  &  BANK reconstruction ---")
    print(f"{'event':10} {'M_det':>7} | {'BANK f(Msrc)':>12} {'HONEST f(Mdet)':>14} "
          f"{'Kerr f(Mdet)':>12} {'f_obs':>6} | {'BANK%':>7} {'HONEST%':>8} {'GRgate%':>8}")
    bank, honest = [], []
    for name, m_src, z, a, f_obs in EVENTS:
        m_det = m_src * (1.0 + z)
        ave = ave_v2_omega_r_m(a)
        kerr = KERR_OMEGA_R_M[a]
        f_bank = f_hz(ave, m_src)      # leaf's frame-mixed value
        f_honest = f_hz(ave, m_det)    # detector-frame honest
        f_kerr = f_hz(kerr, m_det)     # GR gate
        d_bank = 100.0 * (f_bank - f_obs) / f_obs
        d_honest = 100.0 * (f_honest - f_obs) / f_obs
        d_gr = 100.0 * (f_kerr - f_obs) / f_obs
        bank.append(d_bank)
        honest.append(d_honest)
        print(f"{name:10} {m_det:>7.1f} | {f_bank:>12.1f} {f_honest:>14.1f} "
              f"{f_kerr:>12.1f} {f_obs:>6.0f} | {d_bank:>+6.2f}% {d_honest:>+7.2f}% {d_gr:>+7.2f}%")
    print(f"\nMean BANK (leaf's frame-mixed v2@Msrc):   {sum(bank)/3:+.2f}%   "
          f"(leaf banked -0.45%; reproduction confirms the frame-mixing model)")
    print(f"Mean HONEST detector-frame (v2@Mdet):     {sum(honest)/3:+.2f}%")
    print(f"Mean C-1 dimensionless (D-bar):           {c1_mean:+.2f}%")

    print("\nGR-sanity note: the C-3 gate cleanly passes for GW150914 (Kerr@Mdet ~ 251 Hz "
          "obs);\nGW170104/GW151226 f_obs imports are low-quality (Kerr@Mdet misses them), so their\n"
          "per-event C-2 numbers are import-limited — the C-1 dimensionless comparator is authoritative.")

    print("\n" + "=" * 100)
    print("FROZEN-BIN ADJUDICATION")
    print("=" * 100)
    D = abs(c1_mean)
    if D < 3.0:
        verdict = "MATCH-SURVIVES"
    elif D >= 5.0:
        verdict = "MATCH-ARTIFACT"
    else:
        verdict = "MIXED / marginal"
    print(f"  |D-bar| = {D:.2f}%  ->  {verdict}")
    print(f"  Per-event C-1: " + ", ".join(f"{n} {d:+.2f}%" for (n, *_), d in zip(EVENTS, c1_devs)))
    print("  Cold a*=0 eigenvalue (-1.7%) SURVIVES independently of this verdict.")
    return verdict


if __name__ == "__main__":
    main()
