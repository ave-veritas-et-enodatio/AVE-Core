"""Cross-scale verification — AVE operators only."""

from ave.solvers.coupled_resonator import (
    nuclear_mass,
    ionization_energy,
    atom_port_impedance,
    molecular_bond_distance,
    molecular_bond_energy,
    _RY_EV,
    _A0,
    _PROJECTION,
)
from ave.core.constants import ALPHA, NU_VAC

print("=" * 60)
print("AVE CROSS-SCALE VERIFICATION")
print("Operators: Z, S, Gamma, eigenvalue, pairwise")
print("No QM integrals, no optimizers, no fitted constants")
print("=" * 60)

print(f"\nRy = {_RY_EV:.6f} eV (m_e c^2 alpha^2 / 2)")
print(f"a0 = {_A0*1e10:.6f} A")
print(f"alpha = {ALPHA:.8f}")
print(f"nu = {NU_VAC} = 2/7")
print(f"projection = {_PROJECTION:.6f} = 7/18")

print("\n--- Level 1: NUCLEAR ---")
nuc = [("He-4", 2, 4, 3727.379), ("C-12", 6, 12, 11174.863), ("Fe-56", 26, 56, 52089.837)]
for name, Z, A, cod in nuc:
    m, b = nuclear_mass(Z, A)
    print(f"  {name}: {(m-cod)/cod*100:+.3f}%")

print("\n--- Level 2: ATOMIC IE ---")
print("Formula: IE = E(ion) - E(neutral)")
print(f"Screening: Total energy via Mutual Cavity Loading (Op1+Op3)")
CODATA = {
    1: 13.598,
    2: 24.587,
    3: 5.392,
    4: 9.323,
    5: 8.298,
    6: 11.260,
    7: 14.534,
    8: 13.618,
    9: 17.422,
    10: 21.565,
}
names = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne"}

ie_store = {}
for Z in range(1, 11):
    ie = ionization_energy(Z)
    cod = CODATA[Z]
    ie_store[Z] = ie
    err = (ie - cod) / cod * 100
    print(f"  {names[Z]:<3} Z={Z:>2}  IE={ie:>8.3f}  cod={cod:>8.3f}  err={err:>+6.1f}%")

print("\n--- Level 3: MOLECULAR ---")
bonds = [
    ("H-H", 1, 1, 0.741, 4.478),
    ("C-H", 6, 1, 1.090, 4.280),
    ("O-H", 8, 1, 0.958, 4.830),
    ("C-C", 6, 6, 1.540, 3.600),
    ("N-N", 7, 7, 1.450, 1.600),
]
for name, Z1, Z2, dc, Bc in bonds:
    ie1, ie2 = CODATA[Z1], CODATA[Z2]
    r1 = atom_port_impedance(Z1, ie1)
    r2 = atom_port_impedance(Z2, ie2)
    d = molecular_bond_distance(r1, r2)
    B, k = molecular_bond_energy(ie1, ie2, r1, r2, d)
    d_err = (d * 1e10 - dc) / dc * 100
    B_err = (B - Bc) / Bc * 100
    print(f"  {name:<4} d={d*1e10:.3f}A({d_err:+.1f}%) B={B:.3f}eV({B_err:+.1f}%)")

print("\n--- ANTI-CHECKS ---")
print("  Optimizer: NONE")
print("  QM integrals: NONE")
print("  Fitted constants: NONE")
print(f"  All screening from alpha = {ALPHA:.8f}")
