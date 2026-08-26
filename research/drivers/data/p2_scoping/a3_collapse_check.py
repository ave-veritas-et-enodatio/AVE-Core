"""LANE A3 envelope-fork collapse check. Run:
   PYTHONPATH=$PWD/src python3 <this>"""
import math
from ave.core.constants import ALPHA
a = float(ALPHA)
refl = lambda A2: (1.0 - A2) ** 0.5    # CVR |Gamma| readout, storage family
clk  = lambda A2: (1.0 - A2) ** 0.25   # c_shear clock readout, response family

N1, N2, N3, N4 = refl(a), refl(2*a), clk(a), clk(2*a)
print(f"ALPHA={a!r}")
print(f"N1 storage @C-state (native)   = {N1:.10f}")
print(f"N2 storage @full-tank (mapped) = {N2:.10f}")
print(f"N3 response @C-state (mapped)  = {N3:.10f}")
print(f"N4 response @full-tank(native) = {N4:.10f}")
print(f"collision |N1-N4| = {abs(N1-N4):.6e}")
print(f"envelope-on-storage |N1-N2| = {abs(N1-N2):.6e}  ({abs(N1-N2)/abs(N1-N4):.1f}x collision)")
print(f"envelope-on-response |N4-N3| = {abs(N4-N3):.6e}  ({abs(N4-N3)/abs(N1-N4):.1f}x collision)")
print(f"exact deficit-alpha A^2 = 2a-a^2 = {2*a-a*a:.12f}; code 2a = {2*a:.12f}; sep = a^2 = {a*a:.6e} ({100*a/2:.4f}% of A^2)")
print(f"electron: envelope-fork leak {a:.6e} vs {2*a:.6e} (x2); contour-fork rate gap {abs(N1-N4):.6e}; ratio {a/abs(N1-N4):.1f}")
print("A_C^2   S_C        S_F        S_F/S_C   |dZ|/Z")
for A2 in (a, 0.10, 0.20, 0.30, 0.40, 0.49):
    Sc, Sf = math.sqrt(1-A2), math.sqrt(max(1-2*A2, 0.0))
    dz = abs(1/math.sqrt(Sf) - 1/math.sqrt(Sc)) / (1/math.sqrt(Sc)) if Sf > 0 else float('inf')
    print(f"{A2:6.4f} {Sc:10.6f} {Sf:10.6f} {Sf/Sc:9.4f} {dz:8.4f}")
