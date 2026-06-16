#!/usr/bin/env python3
"""
K=2G constitutive-provenance driver (Phase 2 of PR #261, lane 2026-06-15).

Last route to a substrate-FORCED K=2G: does the chiral LC tank's OWN constitutive law pin the bond-
stiffness ratio rho = k_a/k_s to the K=2G value? Two outputs from one constitutive law:
  (i)  saturation monotonicity (C_eff vs eps_eff) -- the OPEN crio Branch-R-vs-F Grant Q;
  (ii) rho = k_a/k_s -> read K/G off the validated lattice-dynamics moduli.

THE BRIDGE (derived; see prereg). Canonical EE identity translation-circuit.md:23:
    C = xi^2 * compliance = xi^2 / stiffness   =>  k_a = xi^2 / C_eff   (capacitive elastance)
EE dual (the new step):  inductive 'stiffness' = magnetic reluctance R = 1/permeance ~ 1/L_eff
    =>  k_s ~ 1/L_eff
    =>  rho = k_a/k_s ~ L_eff/C_eff = Z_eff^2   (the bond-stiffness ratio IS local impedance squared).

VERDICT LOGIC: rho = G_geo * (Z_eff/Z0)^2.  K=2G is the SYM (impedance-matched, Gamma=0 gravity-null)
operating point where eps,mu co-scale -> Z_eff=Z0 -> the operating-point factor is INVARIANT (=1) all
along the K=2G branch. So the operating point CANNOT tune rho to the K=2G value; that value would have
to be baked into the cold geometric prefactor G_geo -- which Phase 1 showed is an unforced one-param
family. => K=2G is NOT constitutively forced (GR-imported, end of line).

Model choice (Grant's flag): Cosserat micropolar (Axiom 1) is substrate-native; Keating (central-force,
Phase-1, validated vs diamond to -0.36%) is the cross-check. Verdict robust to the choice.
"""
import numpy as np
import sympy as sp

rho = sp.symbols('rho', positive=True)            # rho = k_a/k_s  (= Z_eff^2 in natural units)

def nu_of_KG(KG):                                  # isotropic Poisson ratio from K/G
    return sp.simplify((3*KG - 2)/(2*(3*KG + 1)))

# ---------------------------------------------------------------------------------------------------
# 1. Two elasticity models, K/G as a function of rho. Both sub-isostatic (G -> 0 as bend-stiffness->0).
# ---------------------------------------------------------------------------------------------------
# (a) Cosserat micropolar -- SUBSTRATE-NATIVE (Axiom 1). Corpus q-g47-...closure.md:58 / session-12:
K_cos = 4*rho + 8                                  # K0 = 4 k_a + 8 k_s  (k_s=1)
G_cos = 8                                           # G0 = 8 k_s          (k_s=1) -- bend-only (sub-isostatic)
KG_cos = sp.simplify(K_cos/G_cos)                  # = rho/2 + 1
# (b) Keating central-force -- VALIDATED CROSS-CHECK (Phase-1, diamond C44 to -0.36%):
K_kea  = rho + sp.Rational(1,3)                    # K = k_a + k_s/3
G_kea  = sp.simplify(4*(4*rho + 1)/(5*(rho + 1)))  # Voigt(relaxed), k_s=1
KG_kea = sp.simplify(K_kea/G_kea)

print("="*88)
print("K/G(rho) IN BOTH MODELS  (rho = k_a/k_s = Z_eff^2 in natural units)")
print("="*88)
print(f"  Cosserat (native): K/G = {KG_cos}      ->  K=2G at rho* = {sp.solve(sp.Eq(KG_cos,2),rho)[0]}")
ks = [s for s in sp.solve(sp.Eq(KG_kea,2),rho) if s.is_real and s>0]
print(f"  Keating  (x-check): K/G = {sp.nsimplify(KG_kea)}  ->  K=2G at rho* = {float(ks[0]):.3f} (Voigt)")
print(f"  [Phase-1: Keating K=2G also at rho*=3.667 (C'), 6.616 (C44) -- averaging-dependent]")

# ---------------------------------------------------------------------------------------------------
# 2. The constitutive operating-point factor.  rho = G_geo * (Z_eff/Z0)^2.
#    SYM branch (K=2G / gravity-null): eps_eff=eps0*S, mu_eff=mu0*S  -> Z_eff=Z0  -> factor=1, ALL S.
#    Demonstrate rho is INVARIANT along the SYM operating-point family (the common S cancels).
# ---------------------------------------------------------------------------------------------------
print("\n" + "-"*88)
print("SYM-INVARIANCE (the K=2G branch): rho = L_eff/C_eff with eps,mu co-scaling by S")
print(f"  {'S (operating pt)':>16} | {'C_eff~eps0*S':>12} | {'L_eff~mu0*S':>12} | {'rho=L/C (/Z0^2)':>16}")
S = sp.symbols('S', positive=True)
C_eff = S            # C_eff ~ eps_eff = eps0*S   (Z0 normalized out)
L_eff = S            # L_eff ~ mu_eff  = mu0*S
rho_sym = sp.simplify(L_eff/C_eff)                  # = 1, independent of S
for Sv in [1.0, 0.8, 0.5, 0.2, 0.05]:
    print(f"  {Sv:>16.2f} | {Sv:>12.3f} | {Sv:>12.3f} | {float(rho_sym):>16.3f}")
print(f"  => rho_SYM = {rho_sym} for ALL S. The operating point CANNOT tune rho on the K=2G branch.")
print(f"     (Off-SYM/ASYM: eps,mu scale differently so rho DOES move, but its sign is tied to the")
print(f"      OPEN crio Branch-R-vs-F monotonicity Q, and K=2G is undefined off-SYM (Z!=Z0). Not used.)")

# ---------------------------------------------------------------------------------------------------
# 3. The decisive read: plug the constitutive cold/impedance-matched rho into each model.
#    Substrate is impedance-matched to itself (Axiom 1: Z0 IS the substrate impedance) -> Z_eff=Z0
#    -> operating-point factor = 1 -> rho_cold = G_geo. The natural BALANCED point is rho=1.
# ---------------------------------------------------------------------------------------------------
print("\n" + "-"*88)
print("DECISIVE READ -- rho = G_geo * (Z_eff/Z0)^2; operating-point FACTOR=1 on SYM, so rho=G_geo.")
print("(The sweep is over the COLD GEOMETRIC ratio G_geo; the operating point is NOT a knob on it.)")
f_nu_cos = sp.lambdify(rho, nu_of_KG(KG_cos), 'numpy')
f_nu_kea = sp.lambdify(rho, nu_of_KG(KG_kea), 'numpy')
f_KG_cos = sp.lambdify(rho, KG_cos, 'numpy')
f_KG_kea = sp.lambdify(rho, KG_kea, 'numpy')
print(f"  {'rho=G_geo':>9} | {'Cosserat K/G':>13} {'nu':>8} | {'Keating K/G':>12} {'nu':>8} | note")
for rv, note in [(1.0,  "G_geo=1 REFERENCE: pure balanced LC (no geo asymmetry); illustrative, NOT the substrate"),
                 (1.52, "real z=4 diamond (Phase-1): G_geo~1.5"),
                 (2.0,  "Cosserat K=2G: corpus-ASSERTED point (k_a=2/7,k_s=1/7); needs G_geo=2"),
                 (5.305,"Keating K=2G (Voigt): needs G_geo=5.3")]:
    print(f"  {rv:>9.2f} | {f_KG_cos(rv):>13.3f} {f_nu_cos(rv):>8.4f} | "
          f"{f_KG_kea(rv):>12.3f} {f_nu_kea(rv):>8.4f} | {note}")
print(f"\n  nu(2/7) = {2/7:.4f}. The operating-point factor is pinned to 1 (SYM), so rho=G_geo. K=2G needs")
print(f"  G_geo=2 (Cosserat) / 5.3 (Keating) -- the Phase-1 cold-geometry question, answered NEGATIVE")
print(f"  (unforced; real z=4 gives G_geo~1.5). The corpus's rho=2 is ASSERTED, not forced by either the")
print(f"  operating point (factor=1) or the geometry (Phase-1). The rho=1 row is the G_geo=1 limit only.")

# ---------------------------------------------------------------------------------------------------
# 4. Verdict.
# ---------------------------------------------------------------------------------------------------
print("\n" + "="*88)
print("VERDICT: rho = k_a/k_s = G_geo * (Z_eff/Z0)^2.")
print("  - Operating-point factor (Z_eff/Z0)^2 = 1 (INVARIANT) on the SYM / K=2G / gravity-null branch")
print("    -> the saturation operating point CANNOT select K=2G. Independent constitutive-side")
print("    corroboration of the u0*~0.187 ECHO retraction (2026-06-14): u0* is not a K=2G selector.")
print("  - Geometric prefactor G_geo = the Phase-1 UNFORCED one-parameter family (Cosserat rho*=2,")
print("    Keating rho*=3.67-6.62). The chiral coupling does not pin it (corpus: lambda_G=4/21")
print("    chirality-blind; '01_appendices.tex:131 emergent-from-chiral-LC' is a bare assertion).")
print("  => K=2G is NOT constitutively forced. Both the geometry (Phase 1) and the constitutive law")
print("     (Phase 2) fail to force it. K=2G is GR-imported -- END OF LINE. (Forks a & the constitutive")
print("     route both resolve to IMPORTED.)")
print("="*88)
