[↑ Ch.1 Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-salw2h]
-->

# Spin ↔ Gyroscopic Precession Isomorphism

**Volume:** 2 (Subatomic Scale)
**Chapter:** 1

## The Isomorphism

Quantum mechanical spin — historically treated as an intrinsically non-classical, abstract Hilbert space rotation — is shown to be **mathematically identical** to classical gyroscopic precession.  The two systems share the same ODE, the same trajectory on the Bloch/unit sphere, and the same time-domain evolution to machine precision.  *This gyroscope-ODE $\leftrightarrow$ Bloch-sphere equivalence is standard mathematics — **peer-with-SM**, not an AVE-distinct chord (see the guard under AVE Interpretation).*

## Classical Gyroscope

The angular momentum vector $\mathbf{L}$ of a mechanical gyroscope in an external field $\mathbf{B}$ obeys:

$$\frac{d\mathbf{L}}{dt} = \gamma\,\mathbf{L} \times \mathbf{B}$$

Under a circularly polarised RF pulse at the Larmor frequency $\omega_{RF} = \gamma B_0$, the gyroscope executes a $\pi$-flip from spin-up to spin-down in time $t_\pi = \pi / (\gamma B_1)$.

## Quantum Dirac Spinor

The SU(2) spinor $|\psi\rangle = \begin{pmatrix} c_0 \\ c_1 \end{pmatrix}$ evolves under:

$$i\,\frac{d|\psi\rangle}{dt} = H\,|\psi\rangle, \qquad H = -\tfrac{1}{2}\gamma\,\boldsymbol{\sigma} \cdot \mathbf{B}$$

where $\boldsymbol{\sigma}$ are the Pauli matrices.  Projecting onto the Bloch sphere:

$$\langle S_z \rangle = |c_0|^2 - |c_1|^2$$

## Zero Deviation

Numerically integrating both ODEs with identical external field $\mathbf{B}(t) = (B_1\cos\omega t,\; B_1\sin\omega t,\; B_0)$:

$$\max_t \left| L_z(t) - \langle S_z \rangle(t) \right| \sim 10^{-8}$$

The deviation is at numerical integration tolerance — the two models are **mathematically identical**, not merely analogous.

## AVE Interpretation

In the AVE framework, this isomorphism is expected: "quantum spin" is a $\sim\ell_{node}$-scale topological gyroscopic mode of the $0_1$ unknot soliton (the extended core is $\sim\ell_{node} \approx 3.86\times10^{-13}$ m — subatomic, **not** macroscopic).  The Pauli matrices are the 2D projection of 3D Lenz's law cross-product dynamics.  There is no quantum-classical boundary for angular momentum — the same deterministic precession mechanics operates at all scales.

> **Selection-import + symmetric-standard guard (clm-salw2h, [SPIN-HALF-POSITED]).** The gyroscope-ODE $\leftrightarrow$ Bloch-sphere $SU(2)$ equivalence is *standard mathematics* — a mechanical gyroscope and a spin-½ in a field obey the same precession ODE, so the $\sim 10^{-8}$ agreement is a consistency check reproducing standard single-particle QM, **PEER-WITH-SM, not an AVE-distinct chord**. What AVE contributes is the *mechanism* (the precessing rotor is the Cosserat microrotational DOF of the extended $\sim\ell_{node}$-scale $0_1$ unknot — subatomic, not macroscopic), and only the double-cover **STRUCTURE** ($2T \subset SU(2)$) is substrate-native. The fermionic spin-½ **SELECTION** over integer spin is a disclosed action-level **import** ($\pi_1 = \mathbb{Z}_2$ admits both statistics, forces neither). Split canonical at clm-salw2h / clm-rkisb8.

## Key Results

| Result | Statement |
|---|---|
| Classical ODE | $d\mathbf{L}/dt = \gamma\,\mathbf{L} \times \mathbf{B}$ |
| Quantum ODE | $id|\psi\rangle/dt = -\frac{1}{2}\gamma\,\boldsymbol{\sigma}\cdot\mathbf{B}\,|\psi\rangle$ |
| Maximum deviation | $\sim 10^{-8}$ (machine precision) |
| Physical interpretation | Spin is $\sim\ell_{node}$-scale gyroscopic precession of the extended $0_1$ unknot defect — *mechanism*-AVE; gyro$\equiv$Bloch equivalence peer-with-SM; spin-½ SELECTION imported (clm-salw2h) |

*Cross-references*:
- `src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py`
- `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex`
- [Newtonian Inertia as Lenz's Law](./newtonian-inertia-as-lenz.md) — inductance-to-mass mapping
- [Electron Unknot](./electron-unknot.md) — the $0_1$ defect whose precession mode produces spin
- [Finkelstein-Misner Spin-½ Derivation on the K4 Substrate](./finkelstein-misner-spin-half-derivation.md) — explicit K4-native FM-kink derivation + group-theoretic $K_4 \to A_4 \to 2T \subset SU(2)$ chain (the gyroscopic-isomorphism in this leaf is the §4 numerical anchor of that derivation)
