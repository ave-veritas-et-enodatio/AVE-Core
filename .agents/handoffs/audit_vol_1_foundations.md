# Audit Results: Volume 1 - Foundations (IP Migration Plan)

## Scope Covered
- `manuscript/vol_1_foundations/chapters/*`
- `manuscript/frontmatter/00_title.tex`

## 🚨 Sci-Fi & Hardware IP Identified for Migration 🚨
This artifact identifies the specific "macroscopic rotor" and "PONDER" thruster schemas that should be ripped from Vol 1 and ported to the private hardware repo, avoiding direct modification of the `.tex` files until migration is fully planned.

### 1. `manuscript/frontmatter/00_title.tex`
Line 31 Abstract: `offering specific tabletop experimental tests such as the Sagnac Rotational Lattice Mutual Inductance Experiment (Sagnac-RLVE)`

*Recommendation:* Extract the "Sagnac RLVE" testing framework to the hardware repo. For the public repo, swap out with `High-Voltage Active Sagnac Interferometry`.

### 2. `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex`
Lines 193-203 describe the Sagnac-RLVE experiment, featuring macroscopic rotors, topological gear teeth, and Ponderomotive acoustic rectification derived via PONDER-01 falsification bounds.

*Recommendation:* Port this entire multi-paragraph section on mechanical topological gear teeth and rotating metallic Tungsten rotors to the private hardware repository. This entire chunk of text is heavily thrust-oriented and underdeveloped.

### 3. `manuscript/vol_1_foundations/chapters/06_universal_operators.tex`
Line 140:
`Laboratory  & PONDER-01 antenna port S$_{11}$ & |\Gamma| < 1 \\`

*Recommendation:* Move the "PONDER-01 antenna port" specific nomenclature to the hardware taxonomy. For the public repo, swap to generic "Resonant Antenna / Solid State Capacitor S11".

### 4. `manuscript/vol_1_foundations/chapters/07_regime_map.tex`
Lines 88, 110-111, 277, 282, 318 feature four specific repetitions of the "PONDER-05 thruster" test vehicle operating at $30\text{kV}$ and $43\text{kV}$, explicitly analyzing it as a *thruster*.

*Recommendation:* Strip the "PONDER-05 thruster" strings and migrate the test-case metrics to the private PONDER repo. The public repo should just replace these with "High-Voltage asymmetric vacuum capacitor."
