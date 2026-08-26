"""LANE A3 REPAIR — EXACT-COLLAPSE OF THE TWO 0.9963 CLOCKS.
Run:  PYTHONPATH=/Users/grantlindblom/AVE-staging/AVE-Core/src python3 exact_collapse.py

Claim under test (canon's own definitions, strain-registers.md:63-66):
  STORAGE criterion  : A^2 = alpha                    -> clock (1-A^2)^(1/2)
  RESPONSE criterion : Delta_S = 1 - sqrt(1-A^2) = a  -> clock (1-A^2)^(1/4)
Canon quotes a NEAR-collision, Delta = 1.4e-5, between the two clock values.
Solve the response condition EXACTLY (no Taylor truncation) and the two clocks
are the SAME NUMBER, identically in alpha.
"""
import sympy as sp
from mpmath import mp, mpf, sqrt as msqrt
from ave.core.constants import ALPHA

print("=" * 74)
print("1. SYMBOLIC  (sympy)")
print("=" * 74)
a  = sp.symbols('alpha', positive=True)
A2 = sp.symbols('A2', positive=True)

sol = sp.solve(sp.Eq(1 - sp.sqrt(1 - A2), a), A2)[0]
print("  solve( 1 - sqrt(1-A^2) = alpha , A^2 )  ->  A^2 =", sp.expand(sol))
sq = sp.factor(sp.expand(1 - sol))
print("  1 - A^2  factors to  ", sq, "   <-- a PERFECT SQUARE")

# substitute b = 1 - alpha (> 0 for 0 < alpha < 1) so the 4th root denests
b = sp.symbols('b', positive=True)
response_clock = sp.powdenest((sq.subs(a, 1 - b)) ** sp.Rational(1, 4), force=True)
storage_clock  = sp.sqrt(1 - a).subs(a, 1 - b)
print("  response clock (1-A^2)^(1/4) at the EXACT contour =", sp.simplify(response_clock))
print("  storage  clock (1-A^2)^(1/2) at A^2 = alpha       =", sp.simplify(storage_clock))
d = sp.simplify(response_clock - storage_clock)
print("  difference =", d, "   IDENTITY HOLDS:", d == 0)

S_store = sp.simplify(storage_clock)          # S at the storage contour
S_resp  = sp.simplify(sp.powdenest(sp.sqrt(sq.subs(a, 1 - b)), force=True))
print("  kernel form:  S_resp =", S_resp, " ; S_store^2 =", sp.simplify(S_store ** 2),
      " ; S_resp - S_store^2 =", sp.simplify(S_resp - S_store ** 2))
print("  => the exact response criterion sets S = 1-alpha, i.e. S_resp = (S_store)^2,")
print("     so sqrt(S_resp) = S_store.  The 1/4-vs-1/2 exponent difference is EXACTLY")
print("     compensated by the alpha-vs-(2a-a^2) argument difference.")

ser = sp.series(sp.sqrt(1 - a) - (1 - 2 * a) ** sp.Rational(1, 4), a, 0, 4)
print("  series of  (1-a)^(1/2) - (1-2a)^(1/4)  [canon's TRUNCATED contour] =", ser)

print()
print("=" * 74)
print("2. NUMERIC  (mpmath, 50 dps, repo ALPHA = constants.py:163)")
print("=" * 74)
mp.dps = 50
al  = mpf(repr(float(ALPHA)))
A2x = 2 * al - al * al
sc  = (1 - al)  ** mpf('0.5')
rc  = (1 - A2x) ** mpf('0.25')
print("  ALPHA                                   =", float(ALPHA))
print("  exact response contour A^2 = 2a - a^2   =", mp.nstr(A2x, 20))
print("  storage  clock (1-a)^(1/2)              =", mp.nstr(sc, 42))
print("  response clock (1-A^2)^(1/4) [EXACT]    =", mp.nstr(rc, 42))
print("  |difference| =", mp.nstr(abs(sc - rc), 6), "   exactly zero at 50 dps:", abs(sc - rc) == 0)

rc_t = (1 - 2 * al) ** mpf('0.25')
gap  = sc - rc_t
print()
print("  response clock at canon's TRUNCATED contour A^2 = 2a =", mp.nstr(rc_t, 42))
print("  gap  = canon's quoted 'near-collision'               =", mp.nstr(gap, 12))
print("  leading term  a^2/4                                  =", mp.nstr(al * al / 4, 12))
print("  a^2/4 + 3a^3/8                                       =", mp.nstr(al*al/4 + 3*al**3/8, 12))
print("  residual after two terms                             =", mp.nstr(gap - (al*al/4 + 3*al**3/8), 6))
print("  deficit AT the operative contour A^2=2a: 1-sqrt(1-2a)=", mp.nstr(1 - msqrt(1 - 2*al), 14))
print("     vs alpha =", mp.nstr(al, 14), " ; excess =", mp.nstr((1 - msqrt(1-2*al)) - al, 8),
      "~ a^2/2 =", mp.nstr(al*al/2, 8))
print("  (quarter-power-map.md:250 already records this: 'Delta_S = alpha (exactly alpha+alpha^2/2)')")

print()
print("=" * 74)
print("3. CANON LABEL CHECK  (sqrt(S)-projection, cvr:50 / op14:61 / strain-registers:70)")
print("=" * 74)
print("  at A^2 = alpha  :  S =", mp.nstr(msqrt(1 - al), 10),
      "  sqrt(S) =", mp.nstr(msqrt(msqrt(1 - al)), 10))
print("  cvr-reflection-smith.md:50 calls 0.996345 'the sqrt(S)-projection' of A^2=alpha.")
print("  0.996345 is S at that contour, NOT sqrt(S) (sqrt(S) = 0.9981706482).  MISLABEL.")
print("  at A^2 = 2alpha :  S =", mp.nstr(msqrt(1 - 2*al), 10),
      "  sqrt(S) =", mp.nstr((1 - 2*al) ** mpf('0.25'), 10), " <- op14:61's label IS correct")

print()
print("=" * 74)
print("4. CIRCULARITY ARITHMETIC  (knee-contour-check_NOTE:110,:138,:143-144)")
print("=" * 74)
from ave.core.constants import R_I
import math
print("  R_I (constants.py:525) =", R_I, " ; sqrt(2*ALPHA) =", math.sqrt(2*float(ALPHA)),
      " ; identical:", R_I == math.sqrt(2*float(ALPHA)))
print("  NOTE:110 measures the radius where A(s) crosses sqrt(2a) (= R_I)  <-- the 2 is an INPUT")
print("  NOTE:138 reports A(s) = (d_sat/s)^2 to < 1e-4")
print("  => s_knee/d_sat = (2a)^(-1/4) =", (2*float(ALPHA))**-0.25, " is ALGEBRA, not a measurement")
print("  voltage-strain arm of the open fork: d_sat/sqrt(2a) =", 1/math.sqrt(2*float(ALPHA)))
