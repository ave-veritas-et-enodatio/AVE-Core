[↑ Ch.1 Vacuum Circuit Analysis](index.md)
<!-- leaf: verbatim -->

# Q-G22 Strain Convention: Topological-Geometric vs Coulomb-Field Ratio

The corpus uses two distinct strain measures, $A_{\text{geom}}(r) = \ell_{\text{node}}/r$ and $A_{\text{field}}(r) = E(r)/E_{\text{yield}}$. **Both are valid**; each measures a different physical quantity. The apparent "four-way conflict" in $A(r)$ definitions across chapters is resolved by recognizing this convention split — the canonical corpus $V/V_{\text{snap}}$ in kernel applications is the **topological geometric strain**, not the literal Coulomb potential ratio.

This is a clarification leaf, not a new physics result. It documents the canonical convention to prevent future cross-chapter ambiguity.

## The two strain measures

| Measure | Expression | Scaling | Physical meaning |
|---|---|---|---|
| **Geometric confinement ratio** $A_{\text{geom}}$ | $A_{\text{geom}}(r) = d_{\text{sat}}/r = \ell_{\text{node}}/r$ | $\propto 1/r$ | Relative size of soliton vs interaction distance (two point-like nodes' separation ratio) |
| **Field ratio** $A_{\text{field}}$ | $A_{\text{field}}(r) = E(r) \ell_{\text{node}} / V_{\text{yield}}$ | $\propto 1/r^2$ | Electric field strength relative to yield (Coulomb-derived measure) |

The two have **different units and different scaling** with $r$; they cannot be reconciled to a single formula because they measure different physics.

## Canonical convention: kernel applications use $A_{\text{geom}}$

In all corpus kernel applications $C_{\text{eff}}(\Delta\phi) = C_0/\sqrt{1 - A^2}$, $S(A) = \sqrt{1-A^2}$, $V/V_{\text{snap}}$, and Q-G19α Petermann derivation, the strain $A$ is the **topological geometric strain** $A_{\text{geom}}$, NOT the Coulomb field ratio.

Multiple corpus locations confirm this convention:

### Vol 2 Ch 6 (g-2 derivation, lines 402–404)

> *"Solving for the peak electric strain: $(V_{\text{peak}}/V_{\text{snap}})^2 = 4\pi\alpha$ [EXACT] — this is an identity: $\alpha$ IS the on-site electric strain."*

The factor $\alpha$ is absorbed into the corpus $V_{\text{snap}}$ definition; the literal Coulomb potential at distance $r$ from an electron gives $V_0/V_{\text{snap}} = \alpha\,\ell_{\text{node}}/r$, but the corpus $A = \ell_{\text{node}}/r$ (the $\alpha$ is folded into a different parametrization).

### Vol 2 Ch 7 (explicit distinction, lines 923–924)

> *"This is a **field ratio** ($\propto 1/r^2$), distinct from Op4's pairwise strain $A = d_{\text{sat}}/r$ ($\propto 1/r$), which is a **geometric confinement ratio** for two point-like nodes."*

This is the load-bearing canonical statement: two distinct strain measures coexist, neither is "wrong," but they measure different things.

### Vol 2 Ch 7 (Regime I example, lines 1205–1206)

> *"At atomic scales, $r \sim a_0 \gg \ell_{\text{node}} = d_{\text{sat}}$. The strain amplitude is $A = d_{\text{sat}}/r \approx \alpha/(2\pi) \approx 10^{-3}$ — deep in Regime I (linear)."*

At $r = 2\pi a_0$ (atomic orbital circumference): $A = \ell_{\text{node}}/(2\pi a_0) = \ell_{\text{node}}/(2\pi \cdot \ell_{\text{node}}/\alpha) = \alpha/(2\pi) \approx 10^{-3}$. Consistent with geometric-ratio convention.

## Bench convention: IVIM uses $A_{\text{field}}$

The IVIM (asymmetric-electrode vacuum-mirror bench, Vol 4 Ch 11 + Vol 4 Ch 15) uses the **field ratio** $A_{\text{field}} = E\ell_{\text{node}}/V_{\text{yield}}$ for its tree-level discrimination test. This is the natural bench-measurement quantity (apparatus geometry determines $E$ from $V_{\text{DC}}$, and the test discriminates AVE vs SM at $\Gamma_{\text{bench}} \sim 1.94 \times 10^{-11}$ at 43.65 kV).

**Both conventions yield internally-consistent predictions.** The corpus uses $A_{\text{geom}}$ for kernel-amplitude calculations (where the geometric ratio is the load-bearing input) and $A_{\text{field}}$ for apparatus calculations (where the field strength is the load-bearing input). The IVIM bench's $10^{12}$ tree-vs-loop discrimination is convention-robust.

## Status

**Partial closure.** The convention is internally consistent and documented; the **open piece** is deriving WHY the topological strain equals $\ell_{\text{node}}/r$ rather than $\alpha\ell_{\text{node}}/r$ from first principles (a scale-cascade of $V_{\text{yield}}$ across regimes). This is a multi-week analytical work item; the partial closure suffices for cross-chapter consistency now.

## Cross-references

- **Canonical manuscript anchors:**
  - [Vol 2 Ch 6 (Electroweak)](../../../../vol_2_subatomic/chapters/06_electroweak_and_higgs.tex) lines 402–404 — $(V_{\text{peak}}/V_{\text{snap}})^2 = 4\pi\alpha$ identity
  - [Vol 2 Ch 7 (Quantum Mechanics and Orbitals)](../../../../vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex) lines 923–924, 1205–1206 — explicit distinction
  - [Vol 4 Ch 11 (Experimental Falsification)](../../../../vol_4_engineering/chapters/11_experimental_falsification.tex) — IVIM bench uses field-ratio convention
- **Related KB leafs:**
  - [Topological Kinematics](topological-kinematics.md) — VCA dimensional isomorphism
  - [Nonlinear Vacuum Capacitance](nonlinear-vacuum-capacitance.md) — $C_{\text{eff}}(V) = C_0/\sqrt{1-(V/V_{\text{yield}})^2}$ uses geometric-ratio convention
  - [Q-G24 Newtonian-Limit Closure](relativistic-inductor-newtonian-limit.md) — relativistic inductor uses geometric-ratio convention
  - [Q-G19α Petermann (Vol 2 Ch 6)](../../../vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) — kernel-amplitude calculation uses geometric-ratio
