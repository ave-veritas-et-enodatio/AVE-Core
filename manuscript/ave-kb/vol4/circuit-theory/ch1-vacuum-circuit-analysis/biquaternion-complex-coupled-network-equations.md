[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Class-C CONSISTENCY synthesis — stacks node-up (clm-vca7r1), graded-network (clm-gvn4r1), three-channel law, biquaternion result, and engine doctrine into one five-layer equation block. Originates NO new substrate primitive, NO new clm-, NO value-prediction. Biquaternion = coupling-layer notation only (G1–G3 FAIL per research/2026-06-06_biquaternion-node-algebra-result.md)."
-->

## Biquaternion Complex Coupled Network Equations

This leaf is the **integrated equation block** the graded-vacuum network arc has been building toward:
one numbered stack that maps **static/dynamic stress** and **small/large-signal** operating points onto
the **three propagating wave channels** (EM-transverse, shear, bulk-longitudinal) **plus** the **mass
store** (the nonlinear A1 cavity at $\Gamma\to-1$).

It sits **above** the single-node layer ([`node-up-small-large-signal.md`](node-up-small-large-signal.md),
clm-vca7r1) and **beside** the network-response layer
([`graded-network-response.md`](graded-network-response.md), clm-gvn4r1), adding the **biquaternion
port/wall notation** and the **complex-frequency coupled-network operator** in one place.

> **Classification (do NOT lift).** Class-C **CONSISTENCY re-expression** — a routing synthesis that
> unifies already-canonical pieces. The biquaternion is **coupling-layer notation only**
> ([`unified-engine-design-doctrine.md`](unified-engine-design-doctrine.md) §F;
> [`research/2026-06-06_biquaternion-node-algebra-result.md`](../../../../../research/2026-06-06_biquaternion-node-algebra-result.md)
> §0). It does **not** derive $\alpha^{-1}$, does **not** promote a new substrate number system, and
> does **not** replace the keyed-argument duality (V vs $I$) or the two-domain N-port
> ([`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md) §6).

> **Epic tracker:** [`_orchestration/2026-06-27_biquaternion-coupled-network-integration.md`](../../../../../_orchestration/2026-06-27_biquaternion-coupled-network-integration.md)

---

## §0 — What this block is (and is not)

**GOAL:** a single published stack of equations a reader (or implementor) can follow from **lattice
stress** → **saturation operating point** → **channel admittances** → **waves vs mass**.

**IS:**

- Five layers (0–4 below), each with an explicit classification.
- A **stress dispatch table** (§2.3) tying drive class to channel and to wave vs cavity.
- Cross-links to the Build-A isolation spectral solver and the Build-B $H_{\mathrm{couple}}$ gap.

**IS NOT:**

- A claim that one biquaternion field $q(t,\mathbf x)$ is time-stepped instead of separate $V$, $\mathbf u$,
  $\boldsymbol\omega$ sectors ([`unified-engine-design-doctrine.md`](unified-engine-design-doctrine.md) §F).
- A derivation of loaded $Q=1/\alpha$ (adjudicated **CIRCULAR** — do not re-pose;
  [`electron-bound-resonator-coverage.md`](../../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md):161).
- A collapse of the **per-DOF translation tensor**
([`per-dof-vacuum-node-circuit.md`](../../../vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md))
into the **grade triple** — those axes stay orthogonal (seam-7).

---

## §1 — Layer 0: biquaternion port notation (coupling layer only)

A **biquaternion** is $\mathbb H\otimes\mathbb C$ — a quaternion with complex coefficients. Two
imaginaries: quaternion units $\{i,j,k\}$ (non-commutative) and central complex unit $\iota$ ($\iota^2=-1$,
commutes with $i,j,k$).

> **[Resultbox]** *Port coordinate (notation only — cores evolve separate fields)*
>
> $$
> q = w + F, \qquad F = \mathbf E + \iota \mathbf B, \qquad w = V_{A1} + \iota\,\mathcal Q_{\mathrm{wind}}
> $$

| Slot | Substrate object | Sector |
|---|---|---|
| $F = \mathbf E + \iota\mathbf B$ (6 real) | translational $\mathbf u$ + microrotational $\boldsymbol\omega$ as EM fields | EM transverse (T2) |
| $\mathrm{Re}(w) = V_{A1}$ | A1 dilatation / volumetric breathing | bulk / mass-"3" |
| $\mathrm{Im}(w) = \mathcal Q_{\mathrm{wind}}$ | charge = topological Link label (integer) | shear / charge-"3" |

**Algebraic facts (verified, consistency-class):**

- Vector product forces a **scalar slot**: $(a\hat{\mathbf i})(b\hat{\mathbf i}) = -(a\cdot b) + (a\times b)\hat{\mathbf i}$
  ([`research/2026-06-06_biquaternion-node-algebra-result.md`](../../../../../research/2026-06-06_biquaternion-node-algebra-result.md) §4.1).
- $\Gamma=(Z-Z_0)/(Z+Z_0)$ is **PSL(2,$\mathbb C$)** on the reflection sphere (Smith chart = spinor geometry of impedance) — ibid. §5.
- **Null cone:** $N(q)=0$ (zero divisors) $\Leftrightarrow$ $|\Gamma|=1$ lossless boundary — **why bi**quaternion, not real $\mathbb H$ — ibid. §5.4.

**Scope fence:** $\mathcal Q_{\mathrm{wind}}$ is a **static integer label**, not a wave amplitude — never wire it into the A1 $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ phasor ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).

**Prior art (biquaternion electrodynamics — the notation is not novel here).** The field slot $F = \mathbf E + \iota\mathbf B$ is the **Riemann–Silberstein vector**: Silberstein (1912/1914) cast Maxwell's equations in complex/biquaternion form (Silberstein L., *Ann. Phys.* 22/24, 1907; *The Theory of Relativity*, Macmillan 1914), and the biquaternion Maxwell program continues through Conway and Lanczos (Lanczos, *Die Funktionentheoretischen Beziehungen der Maxwellschen Aethergleichungen*, 1919; Conway's biquaternion electrodynamics, 1911). Algebraically the **unit biquaternions are isomorphic to $SL(2,\mathbb C)$**, whose adjoint action is the (proper orthochronous) Lorentz group — the same $SL(2,\mathbb C)$ that appears here as the $\Gamma$/Smith-chart PSL(2,$\mathbb C$) reflection geometry (§facts above). This connects the foreword's Thread 1 (the quaternion-era longitudinal/scalar channel) and Thread 3 (the emergent Lorentz structure) at the **algebra level**: a biquaternionic field carries both the scalar grade and the Lorentz action in one object. AVE adds no new algebra here — the biquaternion is coupling-layer notation (G1–G3 FAIL); the substrate content is the port assignment above, not the biquaternion structure itself.

---

## §2 — Layer 1: large-signal operating point (stress → saturation)

All sectors share **one** Axiom-4 kernel, keyed on **different arguments**:

> **[Resultbox]** *Keyed saturation (Grant-ratified sector split)*
>
> $$
> S_\bullet(A_\bullet) = \sqrt{1-(A_\bullet/A_{\mathrm{yield},\bullet})^2}
> $$
>
> $$
> C_{eff}(V)=\frac{C_0}{S(A_V)},\quad A_V=\frac{V}{V_{\mathrm{yield}}};
> \qquad
> L_{eff}(I)=\frac{L_0}{S(A_I)},\quad A_I=\frac{I_{\mathrm{vac}}}{I_{\max}}
> $$

Canonical at [`node-up-small-large-signal.md`](node-up-small-large-signal.md) §1–§2 and
[`relativistic-inductor.md`](relativistic-inductor.md):15,:18.

### §2.1 — Three regimes (static-field selectors)

| Regime | Drive | $S_\varepsilon$ | $S_\mu$ | Load-bearing consequence |
|---|---|---|---|---|
| **R1** | symmetric internal ($\mathbf E$ **and** $\mathbf B$) | $S$ | $S$ | $Z_{\mathrm{eff}}=Z_0$; achromatic $\Gamma=0$ |
| **R2** | static $\mathbf E$ only | $<1$ | $1$ | Op14 ASYM; $\Gamma\ne0$; E-route birefringence |
| **R3** | static $\mathbf B$ only | $1$ | $1$ | $\delta n_\mu=0$ **exactly** (circulation keyed, not $|\mathbf B|$) |

### §2.2 — Linear vs nonlinear (doctrine §C)

| Regime | $S(A)$ | Excitations | Object |
|---|---|---|---|
| **Linear waves** | $S\approx1$ | normal modes in three impedance channels + Cosserat rotation | propagating waves |
| **Nonlinear cavity** | $S\to0$ | bulk $Z_{\mathrm{bulk}}\to0$, $\Gamma_{\mathrm{bulk}}\to-1$ | **mass store** (A1 breather, $E=m_ec^2$ reactive energy) |

Every nonlinearity flows through **one** kernel $S(A)$ ([`unified-engine-design-doctrine.md`](unified-engine-design-doctrine.md) §C). Structurally, $|\Gamma|=1$ **is** the biquaternion null cone (Layer 4).

### §2.3 — Stress dispatch table (load-bearing map)

| Stress / drive class | Operating-point knobs | Primary channel(s) | Propagating wave? | Mass store? |
|---|---|---|---|---|
| Symmetric volumetric strain (R1 internal) | $S_\varepsilon=S_\mu=S$ | EM + bulk + shear co-grade | yes (all linear below saturation) | yes when $A\to1$ confines bulk |
| Static $\mathbf E$ / bench pump (R2) | $S_\varepsilon<1$, $S_\mu=1$ | EM $\varepsilon$ | EM transverse (+ birefringence) | no |
| Static $\mathbf B$ / magnet (R3) | $S_\mu=1$ identically | — | transparent ($\delta n_\mu=0$) | no |
| Bulk / A1 compression | $S_{\mathrm{bulk}}(A)$, $Z_{\mathrm{bulk}}\propto1/S$ | bulk | longitudinal bulk wave | **yes** at $\Gamma=-1$ wall |
| Deviatoric / shear strain | $S_{\mathrm{shear}}(A)$ | shear | shear / GW-class | no |
| Dynamic AC ($\partial_t\mathbf B\neq0$) | $S_\mu(A_I)$ active | EM $\mu$ + all channels | all + dispersion $\omega(q)$ | cavity eigenmode if confined |

Mechanical channel impedances (cold, $K/G=2$): [`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md).

---

## §3 — Layer 2: three-channel complex coupled network

### §3.1 — Channel admittances (two impedance domains)

**Mixed domains (do NOT collapse):** only $Z_{\mathrm{EM}}\equiv Z_0$ is electrical ($\Omega$).
$Z_{\mathrm{shear}}=\rho_{\mathrm{bulk}}c_{\mathrm{shear}}$ and
$Z_{\mathrm{bulk}}=\rho_{\mathrm{bulk}}c_{\mathrm{bulk}}=\sqrt2\,\rho_{\mathrm{bulk}}c_0$ at $K=2G$ are
mechanical (Pa·s/m). Join via **TKI transformer** $\mathsf T(\xi_{\mathrm{topo}})$, not a direct wire
([`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md):139).

At operating point $A_0$:

$$
Y_\alpha(j\omega) = \frac{1}{Z_{\alpha,\mathrm{eff}}(A_0)}, \qquad
\alpha \in \{\mathrm{EM},\mathrm{shear},\mathrm{bulk}\}
$$

Boundary reflections (Op3): $\Gamma_\alpha=(Z_{\alpha,\mathrm{in}}-Z_{\alpha,0})/(Z_{\alpha,\mathrm{in}}+Z_{\alpha,0})$ with
$\Gamma_{\mathrm{EM}}=0$ (matched port), $\Gamma_{\mathrm{shear/bulk}}\to-1$ (confined, $\mu$-load SHORT).

### §3.2 — Inter-grade coupling (dynamics coded; spectral Build-B open)

> **[Resultbox]** *Conserved chiral bulk↔shear coupling (α-free)*
>
> $$
> H_{\mathrm{couple}} = \tilde\kappa \int g\, V_{A1}\, \Omega_w\, d^3r,
> \qquad \Omega_w = (\nabla\times\boldsymbol\omega)\cdot\hat x,
> \qquad \tilde\kappa = \frac{pq}{p+q} = \frac{6}{5}
> $$

Canonical implementation: [`src/ave/core/cross_sector_coupling.py`](../../../../../src/ave/core/cross_sector_coupling.py).
Status: [`research/2026-06-20_h-couple-status.md`](../../../../../research/2026-06-20_h-couple-status.md) — term **exists** in dynamics; **not yet** in the spectral solver.

### §3.3 — Complex-$\omega$ spectral operator (Build-A landed)

Native spatial operator on the **tetrahedral K4 stencil** (NOT Cartesian 7-pt):

$$
L_{\mathrm{native}} = \mathrm{adjoint\_div}\circ D(A_0)\circ \mathrm{grad}
$$

Isolation-leg non-Hermitian problem (EM matched loss port):

$$
\bigl(L_{\mathrm{native}} - j\sigma_{\mathrm{port}}\,\mathrm{diag}(\mathrm{port})\bigr)\,\mathbf x = \omega^2 \mathbf x,
\qquad
Q = \frac{|\mathrm{Re}\,\omega|}{2|\mathrm{Im}\,\omega|}
$$

Implementation: [`src/ave/solvers/graded_vacuum_network.py`](../../../../../src/ave/solvers/graded_vacuum_network.py).
Prereg / α-free guards: [`research/2026-06-19_electron-Q-coupled-network_prereg.md`](../../../../../research/2026-06-19_electron-Q-coupled-network_prereg.md).

**Build-B gap:** assemble $H_{\mathrm{couple}}$ into the block operator for coupled mode-splitting /
avoided-crossing (Vol. 9 Fig. iii coupled arm — honestly deferred).

---

## §4 — Layer 3: small-signal linearization (probe at $A_0$)

Weak probe through a region at $(S_\varepsilon,S_\mu)$:

> **[Resultbox]** *Small-signal index and impedance (clm-vca7r1)*
>
> $$
> n = \sqrt{S_\varepsilon S_\mu}, \qquad
> Z_{\mathrm{eff}} = Z_0\sqrt{\frac{S_\mu}{S_\varepsilon}}, \qquad
> \Gamma = \frac{Z_{\mathrm{in}}-Z_0}{Z_{\mathrm{in}}+Z_0}
> $$

- **R1:** canonical ray index $n=1/\sqrt{S}$, $\delta n\approx+\tfrac14 A^2$; $Z_{\mathrm{eff}}=Z_0$.
- **R2:** $\delta n_{\mathrm{iso}}\approx-\tfrac14 A_V^2$; $\Gamma\ne0$.
- **R3:** $n=1$, $\delta n_\mu=0$ exactly.

Full sweep: [`node-up-small-large-signal.md`](node-up-small-large-signal.md) §2–§4.

Network-scale graded index and $\Gamma$ vs SYM/ASYM loading: [`graded-network-response.md`](graded-network-response.md) §2–§4.

---

## §5 — Layer 4: wall = null cone; mass = A1 cavity

> **[Resultbox]** *Saturation wall in two equivalent languages*
>
> $$
> |\Gamma| = 1 \;\Longleftrightarrow\; N(q)=0 \;\Longleftrightarrow\;
> \text{lossless reactive boundary (Op3 / Op14 wall)}
> $$

At the electron confinement wall: $\Gamma_{\mathrm{bulk}}\to-1$, $Z_{\mathrm{bulk}}\to0$ — the **mass-3**
A1 dilatation channel ([`three-channel-impedances.md`](../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md)).

**Mass identification (consistency):**

$$
E_{\mathrm{mass}} = \text{reactive energy trapped in the bulk A1 cavity at the } \Gamma=-1 \text{ wall}
$$

This is the work-doing $C\leftrightarrow L$ store ([`resonant-lc-solitons.md`](resonant-lc-solitons.md):17–23), **distinct** from the integer charge label on the shear channel.

**Scalar–vector coupling at the wall:** the grade-0 product forces a scalar↔vector channel; it is **dormant in free propagation** and **active on the null cone**
([`research/2026-06-09_tracereversal-pump-derivation_result.md`](../../../../../research/2026-06-09_tracereversal-pump-derivation_result.md) §3).

---

## §6 — Orthogonal axes (guards against false unification)

| Axis | This block | Orthogonal companion | Do NOT collapse |
|---|---|---|---|
| **Grade triple** (EM / shear / bulk) | §3 | Per-DOF $(L_i,C_i)$ tensor | directional anisotropy within EM translation |
| **Two impedance domains** | §3.1 transformer | Bare $\rho c$ vs $Z_0$ numerics | writing $Z_{\mathrm{bulk}}=\sqrt2\,Z_0$ |
| **Bulk-port vs P-wave ratio** | $\sqrt2=c_{\mathrm{bulk}}/c_0$ | $\sqrt{10/3}=c_L/c_T$ | prereg 2.582 double-count |
| **Charge integer vs A1 amplitude** | Layer 0 notation | Two-natured electron | genesis-24 phasor wire |

---

## §7 — Derived vs asserted ledger

| Element | Status |
|---|---|
| Five-layer stack as routing synthesis | **ASSERTED-STRUCTURAL** (this leaf) |
| Biquaternion port map + null cone ↔ $\|\Gamma\|=1$ | **CONSISTENCY** (biquaternion result) |
| Keyed $S_\bullet(A_\bullet)$, R1/R2/R3 | **DERIVED** (node-up, clm-vca7r1) |
| Three-channel $Z_{\mathrm{EM/shear/bulk}}$, $\Gamma$ map | **DERIVED** (three-channel law) |
| $H_{\mathrm{couple}}$ form, $\tilde\kappa=6/5$ | **DERIVED** (cross_sector_coupling; α-free) |
| Build-A $L_{\mathrm{native}}$, complex-$\omega$ isolation $Q$ | **IMPLEMENTED** (graded_vacuum_network) |
| Build-B coupled spectral $H_{\mathrm{couple}}$ block | **OPEN** (deferred) |
| Loaded $Q=1/\alpha$ from network | **FORBIDDEN** (circular) |
| Biquaternion as substrate primitive / $\alpha$ derivation | **FAIL** (G1–G3) |

> **Consistency-vs-emergence:** Class-C throughout. No solidity lift. Cross-link clm-vca7r1 and clm-gvn4r1 at their canonical ceilings; do not mint a new `clm-` without Grant adjudication.

---

## §8 — Implementation map

| Layer | Engine / script home |
|---|---|
| 0 | Notation at coupling ports (P1.3 target — [`unified-engine-design-doctrine.md`](unified-engine-design-doctrine.md) §F) |
| 1 | `vacuum_varactor_scatter.py`, `test_vca_node_regime_sweep.py` |
| 2 dynamics | `cross_sector_coupling.py`, `crystal_engine.py`, `k4_cosserat_coupling.py` |
| 2 spectral (isolation) | `graded_vacuum_network.py`, `test_graded_vacuum_network_*.py` |
| 2 spectral (coupled) | **Build-B** — wire `H_couple` into sparse eigenproblem |
| 3 | `node_2domain_nport.py`, graded-network figures driver |
| 4 | Op3/Op14 + saturation wall BCs in mass-cage / fork-b tests |

---
