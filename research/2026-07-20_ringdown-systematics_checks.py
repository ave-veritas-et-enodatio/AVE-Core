#!/usr/bin/env python3
"""Ringdown-systematics organizers — numeric checks (frozen-first support).

Lane: RINGDOWN-SYSTEMATICS (research/ringdown-systematics). FORWARD-PREDICTION class.
Derives the two beyond-Kerr DEVIATION organizers from the AVE soft-mode BH picture:

  ORG-1  MODE-RATIO LOCKING   — multipole/overtone frequency RATIOS set by the FROZEN
                                dimensionless K4 elastic ratios (nu_vac = 2/7, Q = ell),
                                spin-independent, vs the (M,a)-drifting Kerr ratios.
  ORG-2  ARRESTED CRITICAL SLOWING — the soft-mode absolute scale slides as omega ~ sqrt(C44),
                                but the rigid nu_vac=2/7 Cosserat skeleton FLOORS the cavity,
                                so omega_R does NOT soften to the Kerr near-extremal value.

Substrate inputs (corpus-cited, NOT fitted here):
  * nu_vac = 2/7                              — K4 Poisson ratio (ave-merger-ringdown-eigenvalue.md)
  * omega_R M_g = ell (1+nu_vac) / x_sat      — AVE ringdown eigenvalue (same leaf, resultbox)
  * x_sat(a*) = 2 + 5 * r_ph_plus(a*)/(3M)    — Cosserat back-reaction v2 (same leaf, v2 resultbox)
  * r_ph_plus = 2M (1 + cos[(2/3) arccos(-a*)]) — prograde photon sphere (v2 resultbox)
  * C44 collapse 0.17661 -> 0.02536 -> 4e-5   — saturated-elastic-tensor_result.md sec4 (PR#521)

GR reference:
  * (2,2,0) Kerr M*omega_R : in-repo Berti table (ligo_ringdown_driver.py:122) — CANONICAL, verified.
  * Schwarzschild (a=0) l=3,4 n=0 and l=2 overtones: standard Leaver values
    [import — Berti-Cardoso-Will 2006 / Chandrasekhar-Detweiler], cross-checked against the
    in-repo Berti (2,2,0) a=0 anchor (0.373672) to 5 sig figs below.

No engine import; numpy/math only; every AVE number traces to a cited corpus formula.
"""

import math

NU_VAC = 2.0 / 7.0  # K4 vacuum Poisson ratio (corpus)
ELL_DOM = 2         # dominant quadrupole multipole


# ---------------------------------------------------------------------------
# GR reference QNM values
# ---------------------------------------------------------------------------
# In-repo canonical Berti (2,2,0) M*omega_R table (ligo_ringdown_driver.py:122).
BERTI_220_OMEGA_R = {
    0.00: 0.37368, 0.10: 0.38659, 0.20: 0.40005, 0.30: 0.41442,
    0.40: 0.42965, 0.50: 0.44597, 0.60: 0.46378, 0.70: 0.48267,
    0.80: 0.50465, 0.90: 0.53039, 0.95: 0.54652,
}

# Standard Schwarzschild (a=0) gravitational (s=2) Leaver QNM real parts M*omega_R
# [import — Berti-Cardoso-Will 2006 living review Table / Chandrasekhar-Detweiler].
# Cross-check: l=2,n=0 here (0.373672) vs in-repo Berti anchor (0.37368) => match to 5 sig figs.
SCHW_OMEGA_R = {
    (2, 0): 0.373672,
    (3, 0): 0.599443,
    (4, 0): 0.809178,
    (2, 1): 0.346711,   # l=2 first overtone
    (2, 2): 0.301053,   # l=2 second overtone
}


def report(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# CROSS-CHECK — in-repo Berti anchor vs imported Leaver value
# ---------------------------------------------------------------------------
report("CROSS-CHECK: imported Leaver (2,2,0) a=0 vs in-repo Berti table anchor")
anchor_repo = BERTI_220_OMEGA_R[0.00]
anchor_import = SCHW_OMEGA_R[(2, 0)]
print(f"  in-repo Berti (2,2,0) a=0 : {anchor_repo}")
print(f"  imported Leaver (2,0)     : {anchor_import}")
print(f"  rel diff                  : {abs(anchor_repo-anchor_import)/anchor_import:.2e}  "
      f"(< 1e-4 => the imported l=3,4/overtone values ride the same verified source)")


# ---------------------------------------------------------------------------
# ORG-1  MODE-RATIO LOCKING
# ---------------------------------------------------------------------------
report("ORG-1  MODE-RATIO LOCKING — multipole frequency ratios (spin-independent in AVE)")

print("\nAVE reading A (corpus form omega_R = ell * c / r_eff, LINEAR-ell; leaf line 16):")
print("   ratio_AVE_lin(l',l) = l'/l  — EXACT, x_sat cancels => spin-independent\n")
print("AVE reading B (spherical-membrane default omega ~ sqrt(l(l+1)); INTERNAL FORK, flagged):")
print("   ratio_AVE_sph(l',l) = sqrt(l'(l'+1) / (l(l+1)))\n")

print(f"  {'pair':>10} | {'AVE_lin':>8} | {'AVE_sph':>8} | {'GR_Schw':>8} | "
      f"{'lin-vs-GR':>9} | {'sph-vs-GR':>9}")
print("  " + "-" * 74)
pairs = [(3, 2), (4, 2), (4, 3)]
org1_rows = []
for lp, l in pairs:
    ave_lin = lp / l
    ave_sph = math.sqrt(lp * (lp + 1) / (l * (l + 1)))
    gr = SCHW_OMEGA_R[(lp, 0)] / SCHW_OMEGA_R[(l, 0)]
    dev_lin = (ave_lin - gr) / gr
    dev_sph = (ave_sph - gr) / gr
    org1_rows.append((lp, l, ave_lin, ave_sph, gr, dev_lin, dev_sph))
    print(f"  {f'{lp}/{l}':>10} | {ave_lin:8.4f} | {ave_sph:8.4f} | {gr:8.4f} | "
          f"{dev_lin*100:+8.2f}% | {dev_sph*100:+8.2f}%")

print("\n  ROBUST AVE statement (fork-independent): the multipole ratio is")
print("  BELOW the Kerr value AND spin-independent. Both AVE readings bracket")
print("  1.41-1.50 for l=3/l=2, vs Kerr 1.604 (Schw) -- a -6% to -12% deviation.")

# Damping-ratio locking: Q = ell (Schwarzschild anchor), so tau ratio locks too.
print("\n  Q-LOCKING (Schwarzschild anchor, qnm-quality-factor.md Q=ell):")
print(f"    Q_3/Q_2 = 3/2 = 1.5000 (AVE)   vs GR omega_I ratio "
      f"[import Leaver]: omega_I(3,0)/omega_I(2,0) = 0.092703/0.088962 = "
      f"{0.092703/0.088962:.4f}")
print("    AVE: damping-time ratio tau_2/tau_3 = Q_2 omega_3 / (Q_3 omega_2) "
      "locked to elastic ratios, not (M,a).")


# ---------------------------------------------------------------------------
# ORG-2  ARRESTED CRITICAL SLOWING  (omega ~ sqrt(C44); rigid-skeleton floor)
# ---------------------------------------------------------------------------
report("ORG-2  ARRESTED CRITICAL SLOWING — spin-excess of omega_R over Kerr near extremal")


def r_ph_plus_over_M(a):
    return 2.0 * (1.0 + math.cos((2.0 / 3.0) * math.acos(-a)))


def x_sat(a):
    return 2.0 + 5.0 * r_ph_plus_over_M(a) / 3.0


def ave_omega_r_M(a, ell=ELL_DOM):
    return ell * (1.0 + NU_VAC) / x_sat(a)


print(f"  {'a*':>5} | {'x_sat':>7} | {'AVE wRM':>8} | {'Kerr wRM':>8} | {'AVE-vs-Kerr':>11}")
print("  " + "-" * 52)
org2_rows = []
for a in [0.0, 0.30, 0.60, 0.70, 0.80, 0.90, 0.95]:
    ave = ave_omega_r_M(a)
    gr = BERTI_220_OMEGA_R[round(a, 2)]
    dev = (ave - gr) / gr
    org2_rows.append((a, x_sat(a), ave, gr, dev))
    print(f"  {a:5.2f} | {x_sat(a):7.4f} | {ave:8.4f} | {gr:8.4f} | {dev*100:+10.2f}%")

# Extremal floor (a*->1): x_sat -> 2 + 5/3 = 11/3
x_ext = 2.0 + 5.0 / 3.0
ave_ext = ELL_DOM * (1.0 + NU_VAC) / x_ext
print(f"\n  Extremal floor a*->1: x_sat -> 2 + 5/3 = {x_ext:.4f} = 11/3")
print(f"    AVE omega_R M -> 2*(9/7)/(11/3) = 54/77 = {54/77:.4f}  (= {ave_ext:.4f})")
print("    The cavity is FLOORED by the rigid nu_vac=2/7 Cosserat skeleton;")
print("    the soft mode does NOT fully soften (critical slowing is ARRESTED).")

# sqrt(C44) scaling law sanity (the mechanism behind ORG-2's absolute scale)
report("ORG-2 mechanism: omega ~ sqrt(C44) — soft-mode absolute-scale law")
C44 = {"loaded-cold": 0.17661, "nu=2/7 crossing": 0.02536, "A->1 wall": 4e-5}
base = C44["loaded-cold"]
print("  C44 collapse (saturated-elastic-tensor_result.md sec4, PR#521):")
for k, v in C44.items():
    print(f"    {k:>16}: C44={v:.5g}   sqrt(C44/C44_cold)={math.sqrt(v/base):.4f}")
print("  Interpretation: the ABSOLUTE mode scale rides sqrt(C44) toward zero,")
print("  but the FROZEN ratios (ORG-1) and the skeleton floor (ORG-2 excess) survive.")


# ---------------------------------------------------------------------------
# RANK-1 UNIFICATION — the two organizers are one single-parameter deformation
# ---------------------------------------------------------------------------
report("RANK-1 UNIFICATION — AVE beyond-Kerr deviation is single-parameter")
print("  omega_R(ell, a*) M_g = [ell * (1+nu_vac)]  x  [1 / x_sat(a*)]")
print("                          ^ frozen ratios (ORG-1)   ^ one scale, common to all modes (ORG-2)")
print("  => the deviation from Kerr across the whole multipole spectrum is RANK-1:")
print("     one overall scale 1/x_sat(a*) times frozen integer-ish ratios.")
print("  FALSIFIER: a spectroscopy analysis resolving INDEPENDENT per-mode deviations")
print("  (delta_f_220, delta_f_330 uncorrelated) rules out the soft-mode organizer.")


# ---------------------------------------------------------------------------
# FROZEN-NUMBER SUMMARY (the values that go into the prereg-FROZEN bins)
# ---------------------------------------------------------------------------
report("FROZEN-NUMBER SUMMARY")
print("  ORG-1 (linear-ell reading):  omega(3)/omega(2) = 1.5000  vs Kerr 1.6042  => -6.49%")
print("  ORG-1 (spherical reading) :  omega(3)/omega(2) = 1.4142  vs Kerr 1.6042  => -11.84%")
print("  ORG-1 robust             :  ratio < Kerr AND spin-independent (locked)")
print(f"  ORG-2 spin-excess a*=0.90:  +{(ave_omega_r_M(0.90)-BERTI_220_OMEGA_R[0.90])/BERTI_220_OMEGA_R[0.90]*100:.2f}%")
print(f"  ORG-2 spin-excess a*=0.95:  +{(ave_omega_r_M(0.95)-BERTI_220_OMEGA_R[0.95])/BERTI_220_OMEGA_R[0.95]*100:.2f}%")
print(f"  ORG-2 extremal floor     :  omega_R M -> 54/77 = {54/77:.4f} (never softens below skeleton floor)")
print("\n  Current-constraint context [import]: single-event QNM-deviation sensitivity")
print("  ~10-20% (Isi+2019 GW150914 overtone); population ~few-% to ~tens-of-%.")
print("  => BOTH organizers sit at or below current sensitivity => CONSISTENT-UNTESTED,")
print("     testable at next-gen (LISA/ET/CE ~1% ringdown) precision. NOT already-excluded.")


if __name__ == "__main__":
    pass
