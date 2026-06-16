#!/usr/bin/env python3
"""
K=2G crystalline-provenance driver (lane 2026-06-15).

Question: does the trace-reversal identity K = 2G (vacuum Poisson ratio nu_vac = 2/7)
re-derive from the CRYSTALLINE z=4 K4 / diamond lattice elastic structure via lattice
dynamics -- or is it amorphous-only (FTG-EMT) / GR-imported?

Method: the standard diamond Keating model (the canonical lattice-dynamics tool for a
z=4 tetrahedral crystal; the corpus's own q_g47_path_b uses a "Born-Huang K4 unit cell"
KeatingBond). Two force constants:
    k_a  -- bond STRETCH (axial) stiffness
    k_s  -- bond BEND   (angular/shear) stiffness
With the diamond two-atom basis, C44 carries an INTERNAL-STRAIN (Kleinman) relaxation:
optic modes displace under macroscopic shear -> the physical (relaxed) C44 < clamped C44.

Everything here is a RATIO (K/G, nu); the common Keating prefactor (sqrt3/4a) cancels, so
no canonical SI constants are needed (dimensionless by construction). The model is VALIDATED
against carbon diamond's measured C_ij to <0.5% before any provenance claim is made.

Output: K/G and nu as functions of rho = k_a/k_s (a SINGLE constitutive ratio). If K/G is a
one-parameter family not pinned to 2, K=2G is NOT a crystalline geometric inevitability.
"""
import numpy as np
import sympy as sp

# ----------------------------------------------------------------------------------------
# 1. Keating elastic constants of the diamond / z=4 K4 lattice (prefactor set to 1; ratios
#    are prefactor-independent). a=k_a (stretch), b=k_s (bend), in common elastic units.
#    Standard diamond Keating results (Keating 1966; Martin 1970; Cousins):
#        C11 = a + 3b
#        C12 = a -  b
#        C44(clamped)  = a + b
#        C44(relaxed)  = C44(clamped) - (a-b)^2/(a+b) = 4ab/(a+b)   [internal strain]
#    Bulk and the two cubic shear moduli follow; bulk K has NO internal-strain term
#    (hydrostatic compression preserves the local Td site symmetry -> no optic displacement).
# ----------------------------------------------------------------------------------------
a, b = sp.symbols('k_a k_s', positive=True)

C11 = a + 3*b
C12 = a - b
C44_clamped  = a + b
C44_relaxed  = sp.simplify(C44_clamped - (a - b)**2/(a + b))   # = 4ab/(a+b)

K        = sp.simplify((C11 + 2*C12)/3)        # bulk
Cp       = sp.simplify((C11 - C12)/2)          # tetragonal shear (C11-C12)/2
G_voigt  = sp.simplify((C11 - C12 + 3*C44_relaxed)/5)  # isotropic Voigt average (relaxed)

print("="*84)
print("KEATING z=4 K4 / DIAMOND ELASTIC CONSTANTS  (k_a=stretch, k_s=bend; prefactor=1)")
print("="*84)
print(f"  C11            = {C11}")
print(f"  C12            = {C12}")
print(f"  C44 (clamped)  = {C44_clamped}")
print(f"  C44 (relaxed)  = {C44_relaxed}        <- internal-strain (Kleinman) relaxed; PHYSICAL")
print(f"  K  (bulk)      = {K}")
print(f"  C' = (C11-C12)/2 = {Cp}")
print(f"  G  (Voigt,relaxed) = {sp.nsimplify(G_voigt)}")

# ----------------------------------------------------------------------------------------
# 2. VALIDATE the model against carbon diamond's measured single-crystal C_ij (GPa).
#    Measured: C11=1079, C12=124, C44=578. Invert C11,C12 for (k_a,k_s) [prefactor folded
#    into the units], predict the RELAXED C44, and the isotropic averages -> nu.
# ----------------------------------------------------------------------------------------
C11_d, C12_d, C44_d = 1079.0, 124.0, 578.0      # carbon diamond, GPa
b_d = (C11_d - C12_d)/4.0                        # from C11-C12 = 4b
a_d = C12_d + b_d                                # from C12 = a - b
C44_pred = 4*a_d*b_d/(a_d + b_d)
K_d  = (C11_d + 2*C12_d)/3.0
# Voigt-Reuss-Hill isotropic shear averages from measured cubic C_ij (the spread IS Outcome C):
Gv_d = (C11_d - C12_d + 3*C44_d)/5.0                                   # Voigt
Gr_d = 5*(C11_d - C12_d)*C44_d/(4*C44_d + 3*(C11_d - C12_d))           # Reuss
Gh_d = 0.5*(Gv_d + Gr_d)                                               # Hill
def nu_of(K, G): return (3*K - 2*G)/(2*(3*K + G))
rho_d = a_d/b_d
A_zener = 2*C44_d/(C11_d - C12_d)
print("\n" + "-"*84)
print("VALIDATION vs carbon diamond (z=4 reference crystal):")
print(f"  inferred k_a={a_d:.1f}, k_s={b_d:.1f}  ->  rho=k_a/k_s = {rho_d:.3f}")
print(f"  C44 relaxed: predicted {C44_pred:.1f} GPa  vs measured {C44_d:.1f} GPa "
      f"(err {100*(C44_pred-C44_d)/C44_d:+.2f}%)  <- model validated")
print(f"  Zener anisotropy A = 2*C44/(C11-C12) = {A_zener:.3f}  (!=1 -> 'a single G' is a choice)")
print(f"  K={K_d:.1f};  isotropic-avg shear spread (Outcome C, quantified):")
print(f"    Voigt: K/G={K_d/Gv_d:.3f}, nu={nu_of(K_d,Gv_d):.4f}  |  "
      f"Reuss: K/G={K_d/Gr_d:.3f}, nu={nu_of(K_d,Gr_d):.4f}  |  "
      f"Hill: K/G={K_d/Gh_d:.3f}, nu={nu_of(K_d,Gh_d):.4f}")
print(f"  *** real z=4 diamond gives nu~{nu_of(K_d,Gh_d):.3f} (K<G, bending-dominated) -- "
      f"FAR from K=2G (nu=2/7={2/7:.4f}) ***")

# ----------------------------------------------------------------------------------------
# 3. K/G as a function of the SINGLE control ratio rho = k_a/k_s. Set k_s=1, k_a=rho.
#    Show it is a smooth one-parameter family. Find rho* where K=2G for EACH choice of
#    "the" shear modulus (C44, C', Voigt) -- they DISAGREE, because cubic K4 is anisotropic
#    so "a single G" is itself a choice (Outcome C door).
# ----------------------------------------------------------------------------------------
rho = sp.symbols('rho', positive=True)
sub = {a: rho, b: 1}
K_r   = K.subs(sub)
C44_r = C44_relaxed.subs(sub)
Cp_r  = Cp.subs(sub)
Gv_r  = G_voigt.subs(sub)

def solve_Keq2G(Gexpr):
    sols = sp.solve(sp.Eq(K_r, 2*Gexpr), rho)
    val = sorted(float(s) for s in sols if s.is_real and s > 0)
    return val

print("\n" + "-"*84)
print("K = 2G  REQUIRES  rho* = k_a/k_s =  (depends on WHICH shear modulus you call G):")
for Gexpr, lab in [(C44_r, "G = C44 (relaxed)"),
                   (Cp_r,  "G = C' = (C11-C12)/2"),
                   (Gv_r,  "G = Voigt isotropic avg")]:
    val = solve_Keq2G(Gexpr)
    roots = ", ".join(f"{v:.3f}" for v in val)
    print(f"   {lab:28s}:  rho* in {{{roots}}}")

print("\n  -> the 'K=2G' ratio sits at DIFFERENT (and for C44, non-unique) rho* depending on")
print("     the averaging choice; NONE is a geometrically distinguished value. Because cubic")
print("     K4 is anisotropic (A=1.21!=1), 'a single G' is itself a choice. K=2G is not a")
print("     bare crystalline output.")

# ----------------------------------------------------------------------------------------
# 4. The sub-isostatic floppy limit: k_s -> 0 (central-force-only z=4). All shear moduli
#    vanish (G -> 0) while K stays finite -> K/G -> infinity. Confirms z=4 < 2d=6 (Maxwell):
#    shear rigidity is ENTIRELY a bond-bending object; K/G is a stiffness-ratio knob.
# ----------------------------------------------------------------------------------------
print("\n" + "-"*84)
print("SUB-ISOSTATIC CHECK (central-force only, k_s -> 0):")
for Gexpr, lab in [(C44_r,"C44(relaxed)"), (Cp_r,"C'"), (Gv_r,"G_voigt")]:
    lim = sp.limit(Gexpr, rho, sp.oo) # large rho = stiff stretch rel. to bend; check k_s->0 below
print(f"  G(k_s->0): C44_relaxed -> {sp.limit(C44_relaxed.subs(a,1), b, 0)},  "
      f"C' -> {sp.limit(Cp.subs(a,1), b, 0)},  "
      f"G_voigt -> {sp.limit(G_voigt.subs(a,1), b, 0)}")
print(f"  K(k_s->0) -> {sp.limit(K.subs(a,1), b, 0)}  (bulk survives on stretching alone)")
print("  => z=4 central-force lattice is FLOPPY in shear (G=0): rigidity needs bond-bending.")
print("     Therefore K/G is set by the constitutive ratio k_a/k_s, NOT by K4 topology.")

# ----------------------------------------------------------------------------------------
# 5. Numerical K/G(rho) and nu(rho) table (Voigt G) across the physical range.
# ----------------------------------------------------------------------------------------
print("\n" + "-"*84)
print("ONE-PARAMETER FAMILY  K/G(rho) and nu(rho)  [Voigt isotropic G]:")
print(f"  {'rho=k_a/k_s':>12} | {'K/G':>8} | {'nu':>8}")
f_KG = sp.lambdify(rho, K_r/Gv_r, 'numpy')
f_nu = sp.lambdify(rho, (3*K_r-2*Gv_r)/(2*(3*K_r+Gv_r)), 'numpy')
for rv in [0.5, 1.0, 1.52, 2.0, 3.0, 5.305, 7.0, 10.0]:
    tag = ""
    if abs(rv-1.52) < 1e-2: tag = "  <- carbon diamond"
    if abs(rv-5.305) < 1e-2: tag = "  <- K=2G (nu=2/7), Voigt"
    print(f"  {rv:>12.3f} | {f_KG(rv):>8.3f} | {f_nu(rv):>8.4f}{tag}")

# ----------------------------------------------------------------------------------------
# 6. ν=2/7 <=> K=2G algebraic identity (the ONE firm link) -- confirm, but note it is a
#    CONSEQUENCE of K=2G, not a derivation of it.
# ----------------------------------------------------------------------------------------
Ks = sp.symbols('K', positive=True); Gs = sp.symbols('G', positive=True)
nu_at_K2G = ((3*Ks - 2*Gs)/(2*(3*Ks + Gs))).subs(Ks, 2*Gs)
print("\n" + "-"*84)
print(f"FIRM LINK (given K=2G):  nu = (3K-2G)/(2(3K+G)) | K=2G  =  {sp.nsimplify(nu_at_K2G)}  = 2/7")
print("   ^ exact, but this is the CONSEQUENT of K=2G, not a crystalline derivation of K=2G.")

print("\n" + "="*84)
print("VERDICT: K/G is a smooth ONE-PARAMETER family in rho=k_a/k_s. z=4 is sub-isostatic so")
print("G is a bond-bending object and K/G is a free stiffness ratio. K=2G needs a specific,")
print("averaging-dependent rho* (3.67 / 5.30 / 6.62) -- none geometrically forced. The real")
print("z=4 crystal (diamond) gives nu~0.067, not 2/7. => K=2G is NOT crystalline-geometric")
print("(Outcome A): it is GR-imported (trace-reversal) and/or amorphous-only (FTG-EMT).")
print("="*84)
