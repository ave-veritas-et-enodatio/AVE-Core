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
  * (2,2,0) Kerr M*omega_R : the in-repo Berti table (ligo_ringdown_driver.py:122) is
    *** WRONG AT NON-ZERO SPIN *** (PR#772 adversarial review, 2026-07-20): it reads
    -9.4/-13.9/-21.0/-26.8% LOW at a*=0.70/0.80/0.90/0.95 (only the a*=0 anchor is right).
    Verified two independent ways (from-scratch Leaver + the qnm package, agreeing to all
    digits; BCW-2006 fit corroborates) plus the exact ZDM extremal limit (co-rotating
    (2,2,0) rises toward m*Omega_H*M=1.0; qnm@0.999=0.9559, NOT the table's ~0.55 plateau).
    This script therefore uses KERR_220_CORRECTED (review-produced) for the (2,2,0) spin
    comparison; BERTI_220_OMEGA_R is KEPT ONLY to exhibit the error. The upstream canon
    table is the canon-correction lane's job (routed separately) — NOT edited here.
  * Schwarzschild (a=0) l=3,4 n=0 and l=2 overtones: standard Leaver values
    [import — Berti-Cardoso-Will 2006 / Chandrasekhar-Detweiler], cross-checked against the
    in-repo Berti (2,2,0) a=0 anchor (0.373672, the ONE correct row) to 5 sig figs — and
    independently reproduced by the qnm package this review (0.373672/0.599443/0.809178).

No engine import; numpy/math only; every AVE number traces to a cited corpus formula.
"""

import math

NU_VAC = 2.0 / 7.0  # K4 vacuum Poisson ratio (corpus)
ELL_DOM = 2         # dominant quadrupole multipole


# ---------------------------------------------------------------------------
# GR reference QNM values
# ---------------------------------------------------------------------------
# In-repo "canonical" Berti (2,2,0) M*omega_R table (ligo_ringdown_driver.py:122).
# *** WRONG AT NON-ZERO SPIN (PR#772 review) *** — kept only to exhibit the error.
BERTI_220_OMEGA_R = {
    0.00: 0.37368, 0.10: 0.38659, 0.20: 0.40005, 0.30: 0.41442,
    0.40: 0.42965, 0.50: 0.44597, 0.60: 0.46378, 0.70: 0.48267,
    0.80: 0.50465, 0.90: 0.53039, 0.95: 0.54652,
}

# CORRECTED (2,2,0) prograde Kerr M*omega_R  [review-produced — two-method:
# from-scratch Leaver continued-fraction + qnm package (Stein 2019), agreeing to all
# digits; corroborated by the Berti-Cardoso-Will 2006 fit; ZDM extremal limit respected].
# This is the reference the ORG-2 spin comparison uses. a*=0 matches the (correct) in-repo row.
KERR_220_CORRECTED = {
    0.00: 0.373672, 0.30: 0.41953, 0.60: 0.49404, 0.70: 0.53260,
    0.80: 0.58602, 0.90: 0.67161, 0.95: 0.74632,
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
report("CROSS-CHECK: in-repo Berti (2,2,0) table vs CORRECTED two-method Kerr")
anchor_repo = BERTI_220_OMEGA_R[0.00]
anchor_import = SCHW_OMEGA_R[(2, 0)]
print(f"  a*=0 anchor: in-repo {anchor_repo} vs Leaver {anchor_import} "
      f"=> rel diff {abs(anchor_repo-anchor_import)/anchor_import:.2e}  (the ONE correct row)")
print("  BUT the in-repo table is WRONG at spin (only a*=0 is right):")
print(f"    {'a*':>5} | {'in-repo':>8} | {'corrected':>9} | {'in-repo err':>11}")
for a in [0.30, 0.60, 0.70, 0.80, 0.90, 0.95]:
    ir = BERTI_220_OMEGA_R[a]
    corr = KERR_220_CORRECTED[a]
    print(f"    {a:5.2f} | {ir:8.5f} | {corr:9.5f} | {(ir-corr)/corr*100:+9.2f}%")
print("  => the shipped 'two-method cross-check' validated ONLY a*=0; the load-bearing")
print("     spinning rows were single-method on a -9% to -27%-wrong table (PR#772 review).")


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

# Damping-ratio locking: Q = ell (Schwarzschild anchor ONLY), so tau ratio locks at a*=0.
# R4/finding-4: LIKE-FOR-LIKE comparator. GR's Q-ratio is Q=omega_R/(2 omega_I), NOT the
# bare omega_I ratio (the old printout compared AVE's Q-ratio 1.5 to GR's omega_I ratio 1.04).
SCHW_OMEGA_I = {(2, 0): 0.088962, (3, 0): 0.092703}  # [import Leaver, qnm-confirmed]
gr_Q2 = SCHW_OMEGA_R[(2, 0)] / (2 * SCHW_OMEGA_I[(2, 0)])
gr_Q3 = SCHW_OMEGA_R[(3, 0)] / (2 * SCHW_OMEGA_I[(3, 0)])
gr_Qratio = gr_Q3 / gr_Q2
print("\n  Q-LOCKING (Schwarzschild anchor ONLY, qnm-quality-factor.md Q=ell, clm-395gps 0.55):")
print(f"    AVE:  Q_2=2, Q_3=3  =>  Q_3/Q_2 = 3/2 = 1.5000")
print(f"    GR (like-for-like): Q_2={gr_Q2:.4f}, Q_3={gr_Q3:.4f} => Q_3/Q_2 = {gr_Qratio:.4f}"
      f"  (AVE lock is only {(1.5-gr_Qratio)/gr_Qratio*100:+.1f}% from GR's Schwarzschild Q-ratio)")
print(f"    [the OLD printout mis-compared AVE 1.5 to GR's omega_I ratio "
      f"{SCHW_OMEGA_I[(3,0)]/SCHW_OMEGA_I[(2,0)]:.4f} — wrong comparator, finding 4]")
print("    DISCRIMINATOR is NOT the Schwarzschild ratio (GR nearly satisfies l'/l too);")
print("    it would be the SPIN-DRIFT of Q -- but the corpus derives Q=ell only at a*=0")
print("    (leaf: Q=omega_R/2omega_I 'increases with spin'), so the all-spin tau-lock is")
print("    Schwarzschild-anchored, NOT spin-independent (R4/finding-3 reconciliation).")


# ---------------------------------------------------------------------------
# ORG-2  ARRESTED CRITICAL SLOWING  (omega ~ sqrt(C44); rigid-skeleton floor)
# ---------------------------------------------------------------------------
report("ORG-2  [RETRACTED PR#772] — AVE v2 vs CORRECTED Kerr: sign INVERTS (AVE BELOW)")


def r_ph_plus_over_M(a):
    return 2.0 * (1.0 + math.cos((2.0 / 3.0) * math.acos(-a)))


def x_sat(a):
    return 2.0 + 5.0 * r_ph_plus_over_M(a) / 3.0


def ave_omega_r_M(a, ell=ELL_DOM):
    return ell * (1.0 + NU_VAC) / x_sat(a)


print("  ORG-2 (frozen: 'positive excess, AVE ABOVE Kerr for a*>~0.8') is RETRACTED:")
print("  against the CORRECTED two-method Kerr reference, AVE v2 sits BELOW at every spin.\n")
print(f"  {'a*':>5} | {'x_sat':>7} | {'AVE wRM':>8} | {'Kerr(corr)':>10} | {'in-repo(WRONG)':>13} | {'AVE-vs-corr':>11}")
print("  " + "-" * 74)
org2_rows = []
for a in [0.0, 0.30, 0.60, 0.70, 0.80, 0.90, 0.95]:
    ave = ave_omega_r_M(a)
    gr = KERR_220_CORRECTED[round(a, 2)]
    gr_wrong = BERTI_220_OMEGA_R[round(a, 2)]
    dev = (ave - gr) / gr
    org2_rows.append((a, x_sat(a), ave, gr, dev))
    print(f"  {a:5.2f} | {x_sat(a):7.4f} | {ave:8.4f} | {gr:10.5f} | {gr_wrong:13.5f} | {dev*100:+10.2f}%")

print("\n  => AVE v2 is monotonically BELOW true Kerr, deviation GROWING with spin")
print("     (-9.9% @0.70 -> -20.1% @0.95) — the OPPOSITE sign of the frozen ORG-2.")
print("     The prereg falsifier ('a*>~0.9 ringdown AT or BELOW Kerr => ALREADY-EXCLUDED')")
print("     describes exactly what AVE actually predicts. RULE-11 DISCARD, no refill.")

# Extremal floor (a*->1): x_sat -> 2 + 5/3 = 11/3.  Survives independently but sits BELOW Kerr.
x_ext = 2.0 + 5.0 / 3.0
ave_ext = ELL_DOM * (1.0 + NU_VAC) / x_ext
# True Kerr l=m=2 extremal: M*omega_R -> m*Omega_H*M = 2*(1/2) = 1.0 (ZDM limit).
print(f"\n  Extremal floor a*->1: x_sat -> 2 + 5/3 = {x_ext:.4f} = 11/3")
print(f"    AVE omega_R M -> 2*(9/7)/(11/3) = 54/77 = {54/77:.4f}  (= {ave_ext:.4f})")
print(f"    vs TRUE Kerr l=m=2 extremal ZDM limit m*Omega_H*M = {2*0.5:.4f}")
print("    => the AVE floor (0.7013) sits BELOW extremal Kerr (1.0), NOT above it.")
print("    The skeleton floor SURVIVES corpus-internally as a POSSIBLE FUTURE below-Kerr")
print("    organizer, but needs a fresh frozen derivation AFTER the upstream canon fix.")

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
report("RE-GRADED-NUMBER SUMMARY (PR#772 review — supersedes the frozen bins)")
print("  ORG-1 (linear-ell) : omega(3)/omega(2) = 1.5000 vs Kerr 1.6042 (a*=0) => -6.50%")
print("  ORG-1 (spherical)  : omega(3)/omega(2) = 1.4142 vs Kerr 1.6042 (a*=0) => -11.84%")
print("  ORG-1 spin caveat  : Kerr DRIFTS toward AVE (1.6042 -> 1.5554 @0.9 -> 1.5192 @0.99);")
print("                       linear-fork sep drops below ~5% for a*>~0.75 (only -5.3% @0.7);")
print("                       spherical fork stays -8% to -12% robust. => TESTABLE-with-")
print("                       REDUCED-SEPARATION (spin-conditioned).")
print(f"  ORG-2 [RETRACTED]  : a*=0.90 AVE-vs-corrected-Kerr = "
      f"{(ave_omega_r_M(0.90)-KERR_220_CORRECTED[0.90])/KERR_220_CORRECTED[0.90]*100:+.2f}%  "
      f"(frozen claimed +5.48% ABOVE; sign INVERTS)")
print(f"                       a*=0.95 AVE-vs-corrected-Kerr = "
      f"{(ave_omega_r_M(0.95)-KERR_220_CORRECTED[0.95])/KERR_220_CORRECTED[0.95]*100:+.2f}%  "
      f"(frozen claimed +9.16% ABOVE)")
print(f"  ORG-2 floor (survives corpus-internal): omega_R M -> 54/77 = {54/77:.4f}, BELOW")
print(f"                       extremal Kerr {2*0.5:.4f} -- possible FUTURE below-Kerr organizer.")
print("\n  Confrontation [import]: against corrected Kerr the AVE v2 eigenvalue deviates")
print("  -4% to -13% at the attested catalog spins (a*=0.30-0.80, all events a*<0.85),")
print("  AT/ABOVE the imported delta_f_220 sensitivity (~few-% to ~10%).")
print("  => AVE-eigenvalue-vs-Kerr axis = POTENTIAL LIVE TENSION, UNSAFE-PENDING-UPSTREAM-FIX")
print("     (contaminated by the corrupted canon table + a detector-vs-source-frame mass")
print("     question; both routed to the canon-correction lane). NO negative fired here.")


if __name__ == "__main__":
    pass
