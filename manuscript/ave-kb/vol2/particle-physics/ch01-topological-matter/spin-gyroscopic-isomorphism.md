[↑ Ch.1 Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-salw2h]
-->

# Spin ↔ Gyroscopic Precession Isomorphism

**Volume:** 2 (Subatomic Scale)
**Chapter:** 1

## The Isomorphism

Quantum mechanical spin — historically treated as an intrinsically non-classical, abstract Hilbert space rotation — is shown to be **mathematically identical** to classical macroscopic gyroscopic precession.  The two systems share the same ODE, the same trajectory on the Bloch/unit sphere, and the same time-domain evolution to machine precision.

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

In the AVE framework, this isomorphism is expected: "quantum spin" is a macroscopic topological gyroscopic mode of the $0_1$ unknot soliton.  The Pauli matrices are the 2D projection of 3D Lenz's law cross-product dynamics.  There is no quantum-classical boundary for angular momentum — the same deterministic mechanics operates at all scales.

## Key Results

| Result | Statement |
|---|---|
| Classical ODE | $d\mathbf{L}/dt = \gamma\,\mathbf{L} \times \mathbf{B}$ |
| Quantum ODE | $id|\psi\rangle/dt = -\frac{1}{2}\gamma\,\boldsymbol{\sigma}\cdot\mathbf{B}\,|\psi\rangle$ |
| Maximum deviation | $\sim 10^{-8}$ (machine precision) |
| Physical interpretation | Spin is macroscopic gyroscopic precession of the topological unknot defect |

*Cross-references*:
- `src/scripts/vol_2_subatomic/simulate_gyroscopic_spin.py`
- `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex`
- [Newtonian Inertia as Lenz's Law](./newtonian-inertia-as-lenz.md) — inductance-to-mass mapping
- [Electron Unknot](./electron-unknot.md) — the $0_1$ defect whose precession mode produces spin
