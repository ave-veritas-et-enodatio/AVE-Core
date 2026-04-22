import numpy as np

Ry = 13.605693
print("Goal IE: 24.59 eV")

def eval_gap(eff_dist_factor: float) -> float:
    # original V_rep = Z_eff * Ry (eff_dist_factor = 2)
    C = 2.0 / eff_dist_factor
    Z_eff = (8.0 - C) / 4.0
    E = 2 * (Z_eff**2) - (8.0 - C) * Z_eff
    IE = E + 4.0
    return -IE * Ry

for i in np.arange(1.0, 5.0, 0.05):
    print(f"dist_factor={i:.2f} -> IE={eval_gap(i):.2f} eV")
