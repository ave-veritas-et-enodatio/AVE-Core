[↑ Up](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: 7tk051 -->

# First Ionization Energy Summary

The electronic ionization energy solver (`radial_eigenvalue.py`) computes first ionization energies for $Z = 1$ to $14$ (and $Z = 31$ to $36$) using a three-phase pipeline: (A) ODE cavity eigenvalue with axiom-derived CDF screening, (B) Hopf mode splitting with four corrections (A: hierarchical cascade for Be-type, B: SIR boundary for Mg-type, C: Op10 junction projection for Al-type co-resonant shells, D: Topo-Kinematic Polar Conjugate Mirror for Period-4+ elements), (C) crossing scattering. All values use zero free parameters.

| Element | Z | AVE (eV) | Exp (eV) | Error | Correction |
|---|:---:|---:|---:|---:|---|
| Hydrogen | 1 | 13.606 | 13.598 | $+0.06\%$ | --- |
| Helium | 2 | 24.370 | 24.587 | $-0.88\%$ | --- |
| Lithium | 3 | 5.525 | 5.392 | $+2.46\%$ | --- |
| Beryllium | 4 | 9.280 | 9.322 | $-0.45\%$ | A (cascade) |
| Boron | 5 | 8.065 | 8.298 | $-2.80\%$ | --- |
| Carbon | 6 | 11.406 | 11.260 | $+1.30\%$ | --- |
| Nitrogen | 7 | 14.465 | 14.534 | $-0.48\%$ | --- |
| Oxygen | 8 | 13.618 | 13.618 | $-0.00\%$ | --- |
| Fluorine | 9 | 17.194 | 17.423 | $-1.31\%$ | --- |
| Neon | 10 | 21.789 | 21.565 | $+1.04\%$ | --- |
| Sodium | 11 | 5.071 | 5.139 | $-1.33\%$ | --- |
| Magnesium | 12 | 7.591 | 7.646 | $-0.73\%$ | B (SIR) |
| Aluminum | 13 | 5.937 | 5.986 | $-0.82\%$ | C (Op10) |
| Silicon | 14 | 8.147 | 8.152 | $-0.06\%$ | C (Op10) |
| Gallium | 31 | 5.999 | 5.999 | $-0.00\%$ | D (Topo-Kinematic) |
| Germanium | 32 | 7.763 | 7.899 | $-1.72\%$ | D (Topo-Kinematic) |
| Arsenic | 33 | 9.742 | 9.788 | $-0.47\%$ | D (Topo-Kinematic) |
| Selenium | 34 | 9.907 | 9.752 | $+1.58\%$ | D (Topo-Kinematic) |
| Bromine | 35 | 11.911 | 11.814 | $+0.82\%$ | D (Topo-Kinematic) |
| Krypton | 36 | 14.446 | 13.999 | $+3.19\%$ | D (Topo-Kinematic) |

Correction A = hierarchical cascade. Correction B = SIR boundary reflection. Correction C = Op10 junction projection. Correction D = Topo-Kinematic Polar Conjugate Mirror ($\Gamma < 0$ TIR bounding via $3d^{10}$, $4d^{10}$, $5d^{10}$ shells). All elements evaluated rigidly with zero free parameters.

> ↗ See also: [Polar Conjugate Topo-Kinematic Bounding](polar-conjugate-bounding.md) — Correction D derivation for heavy elements
