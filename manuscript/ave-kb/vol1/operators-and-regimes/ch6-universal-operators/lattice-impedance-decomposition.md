[↑ Ch.6 Universal Operators](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol4 ch1 + photon-identification + pair-production as canonical impedance decomposition -->

# Lattice Impedance from First Principles: $Z_0 / Z_{\text{cell}} / Z_{\text{eff}}(r) / Z_{\text{local}}$

The AVE corpus uses "impedance" in multiple distinct senses that are numerically related but physically distinct. This leaf is the canonical decomposition: classical free-space $Z_0$, per-cell lattice $Z_{\text{cell}}$, position-dependent saturation-modulated $Z_{\text{eff}}(r)$, mutual-inductance $\eta_{\text{vac}}$ at node-to-node coupling, mechanical $Z_{\text{mech}}$ via topo-kinematic dual, and event-horizon $Z_{\text{EH}}$ at full saturation. **Numerical equality of $Z_{\text{cell}} = Z_0$ is from cancellation of $\ell_{\text{node}}$; conceptual distinction matters for engine implementation and dimensional analysis.**

## Key Results

| Quantity | Symbol | SI value | Physical meaning |
|---|---|---|---|
| Classical free-space impedance | $Z_0$ | $\mu_0 c = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω | Ratio of $\|E\|/\|H\|$ in plane EM wave in classical vacuum |
| Per-cell lattice impedance | $Z_{\text{cell}}$ | $\sqrt{L_{\text{cell}}/C_{\text{cell}}} = \sqrt{\mu_0 \ell_{\text{node}} / (\varepsilon_0 \ell_{\text{node}})} = Z_0$ | Characteristic impedance of single LC bond in K4 lattice |
| Local effective impedance | $Z_{\text{eff}}(r)$ | $Z_0 / \sqrt{S}$, $S = \sqrt{1 - A^2(r)}$ | Position-dependent under Axiom 4 local saturation |
| Mutual inductance | $\eta_{\text{vac}}$ (no canonical symbol yet) | derived from $R_{\text{vac}} = \xi_{\text{topo}}^{-2} \eta_{\text{vac}}$ | Inductive coupling between adjacent K4 nodes |
| Mechanical impedance | $Z_{\text{mech}}$ | $\xi_{\text{topo}}^2 \cdot Z_0 \approx 6.485 \times 10^{-11}$ kg/s | Force-per-velocity via topo-kinematic Axiom 2 dual |
| Event-horizon impedance | $Z_{\text{EH}}$ | $\to 0$ Ω | Full saturation, $\Gamma = -1$ TIR mirror |

## §1 — The six impedance concepts

### Classical free-space impedance $Z_0$

$$Z_0 = \mu_0 c = \sqrt{\mu_0/\varepsilon_0} \approx 376.73 \text{ Ω}$$

**Physical meaning:** ratio of $\|E\|/\|H\|$ in a plane EM wave in classical vacuum.

**Scale:** continuum / field-theoretic.

**In AVE:** derived from Axiom 1 via the equivalence (Vol 4 Ch 1:283): *"$Z_0$ is a property of the node-to-node impedance ratio of the lattice, independent of the absolute scale $\ell_{\text{node}}$."*

### Per-cell lattice impedance $Z_{\text{cell}}$

$$Z_{\text{cell}} = \sqrt{\frac{L_{\text{cell}}}{C_{\text{cell}}}} = \sqrt{\frac{\mu_0 \ell_{\text{node}}}{\varepsilon_0 \ell_{\text{node}}}} = Z_0$$

**Physical meaning:** characteristic impedance of a SINGLE LC bond in the K4 lattice. Ratio of voltage to current for wave passing through one bond.

**Scale:** discrete / circuit element.

**Note:** **NUMERICALLY equal to classical $Z_0$** because the lattice pitch $\ell_{\text{node}}$ cancels (appears in both $L_{\text{cell}}$ and $C_{\text{cell}}$); **CONCEPTUALLY distinct** because $Z_{\text{cell}}$ refers to a physical bond, $Z_0$ refers to a continuum field ratio. The numerical equality is the substrate's signature of being "internally consistent at every scale" — Axiom 2 (TKI) scale invariance.

### Local effective impedance $Z_{\text{eff}}(r)$ (Axiom-4-modulated)

From Op14:

$$Z_{\text{eff}}(r) = \frac{Z_0}{\sqrt{S}}, \quad S = \sqrt{1 - A^2(r)}$$

**Physical meaning:** position-dependent impedance under local dielectric saturation. **Diverges as $A^2 \to 1$** (rupture / TIR limit).

**Scale:** per-cell, dynamical.

**Engine implementation:** `k4.z_local_field` in `src/ave/core/k4_tlm.py` (nonlinear mode) and explicitly in `_update_z_local_total` in the coupling module.

### Mutual inductance $\eta_{\text{vac}}$ (drag coefficient at node-to-node coupling)

From Vol 4 Ch 1:240 (mechanical duality):

$$R_{\text{vac}} \equiv \xi_{\text{topo}}^{-2} \cdot \eta_{\text{vac}}$$

**Physical meaning:** **inductive COUPLING between adjacent K4 nodes.** Sets how fast one node's current change induces current change in its neighbor. Related to mechanical drag coefficient $\eta$ (kg/s) via topo-kinematic mapping.

**Scale:** between-node / coupling coefficient.

**Engine status:** IMPLICITLY encoded in the K4 scattering matrix $S_{ij} = 0.5 - \delta_{ij}$ (the off-diagonal 0.5 IS the coupling strength), but **NOT explicitly as a separate symbol or derivable quantity.**

**Flag:** this is the **missing operator symbol** Grant flagged in doc 45. Cascade-saturation mechanism (the AVE-native bootstrap for pair creation) depends on this coupling; the engine carries it implicitly via S-matrix but cannot independently tune the cascade-coupling strength. Would benefit from an explicit symbol + named operator in a future axiom-homologation pass.

### Mechanical impedance $Z_{\text{mech}}$

From Vol 4 Ch 1:118-120:

$$Z_{\text{mech}} = \xi_{\text{topo}}^2 \cdot Z_0 \approx 6.485 \times 10^{-11} \text{ kg/s}$$

**Physical meaning:** force-per-velocity at a single node (via topo-kinematic Axiom 2 map).

**Scale:** per-node, macroscopic mechanical dual.

**Relevance:** not directly used in Phase III coupling but establishes that the electrical / mechanical / acoustic identities are all numerically equivalent under the Axiom-2 conversion constant $\xi_{\text{topo}}$.

### Event-horizon impedance $Z_{\text{EH}}$

From Vol 4 Ch 1:364:

$$Z_{\text{EH}} \to 0 \text{ Ω}$$

**Physical meaning:** impedance at Axiom-4 full-saturation limit (both $\mu$ and $\varepsilon$ collapse asymmetrically). The TIR mirror at $\Gamma = -1$.

**Relevance:** the pair-creation endpoint per L3 doc 37 — $A^2 = 1$ at two adjacent nodes is locally a "mini-event-horizon" where $Z$ drops to 0 and the topology snaps to closure ([pair-production-axiom-derivation](../../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md)).

## §2 — Dimensional analysis table (lattice-native units)

All Phase III simulator quantities in SI + lattice-native ($\ell_{\text{node}} = 1$, $m_e = 1$, $c = 1$, $\hbar = 1$):

| Symbol | SI units | Lattice-native | Meaning |
|---|---|---|---|
| $\ell_{\text{node}}$ | m | $1$ | spatial unit |
| $c$ | m/s | $1$ | light speed |
| $m_e$ | kg | $1$ | mass unit |
| $\hbar$ | J·s | $1$ | action unit |
| $\tau_{\text{relax}} = \ell_{\text{node}}/c$ | s | $1$ | fundamental time unit |
| $e$ (charge) | C | $\sqrt{\alpha} \approx 0.0854$ | unit charge |
| $\xi_{\text{topo}} = e/\ell_{\text{node}}$ | C/m | $\sqrt{\alpha}$ | topo-kinematic scale |
| $V_{\text{SNAP}} = m_e c^2/e$ | V | $1/\sqrt{\alpha} \approx 11.7$ | rupture voltage |
| $V_{\text{YIELD}} = \sqrt{\alpha} \cdot V_{\text{SNAP}}$ | V | $1.0$ (!) | engineering yield |
| $I_{\max} = \xi_{\text{topo}} \cdot c$ | A | $\sqrt{\alpha}$ | max current |
| $Z_0 = \mu_0 c$ | Ω | $1$ | characteristic impedance |
| $L_{\text{cell}} = \mu_0 \cdot \ell_{\text{node}}$ | H | depends on $\mu_0$ choice | per-bond inductance |
| $C_{\text{cell}} = \varepsilon_0 \cdot \ell_{\text{node}}$ | F | depends on $\varepsilon_0$ choice | per-bond capacitance |
| $V$ (scalar K4 voltage) | V | ratio to $V_{\text{SNAP}}$ | wave amplitude |
| $u$ (Cosserat translation) | m | ratio to $\ell_{\text{node}}$ | Cosserat translation |
| $\omega$ (Cosserat microrotation) | rad/m | dimensionless | Cosserat rotation |
| $A^2 = \|V\|^2/V_{\text{SNAP}}^2$ | dimensionless | dimensionless | saturation amplitude squared |

### Critical observation: $V_{\text{YIELD}} = 1$ in lattice natural units

In lattice units, the **engineering yield threshold is $V_{\text{YIELD}} = 1$**, NOT $V_{\text{SNAP}} = 1$. Engine code typically uses $V_{\text{SNAP}} = 1.0$ as the user-facing normalization. When the user sees `amp = 0.5·V_SNAP`, that's effectively $\text{amp} = 0.5/\sqrt{\alpha} = 5.85$ in units where $V_{\text{YIELD}} = 1$. **At $0.5 \cdot V_{\text{SNAP}}$, the lattice is massively above yield, below rupture.**

The Axiom 4 operator uses $V_{\text{SNAP}}$ as the normalization for $A$, so the "$\sqrt{2\alpha}$ Regime I/II boundary" corresponds to $A = \sqrt{2\alpha} = 0.121$ in $V/V_{\text{SNAP}}$ units. In $V_{\text{YIELD}}$ units this is $A_{\text{yield-units}} = 0.121/\sqrt{\alpha} = 1.42$.

This normalization choice (engineer-facing $V_{\text{SNAP}}$ vs. native $V_{\text{YIELD}}$) is **load-bearing for amplitude scoping** in engine experiments. Always verify which normalization is active.

## §3 — Axiom → Operator → Engine mapping

| Axiom | Operator(s) | In engine |
|---|---|---|
| **Axiom 1** (Chiral Laves K4 Cosserat Crystal) | Op5 (4-port scatter matrix) | `build_scattering_matrix` in `k4_tlm.py` |
| | Op1 (bond propagation) | `_connect_all` (np.roll) |
| **Axiom 2** (Topo-Kinematic Isomorphism, $[Q] \equiv [L]$) | Op12 (topological invariant) | `extract_crossing_count`, `extract_hopf_charge` |
| | Op20 (self-consistent amplitude) | NOT implemented |
| **Axiom 3** (Minimum Reflection Principle / Effective Action) | Op8 (Lagrangian density) | `_energy_density_bare/saturated` |
| | Op9 (time evolution) | `CosseratField3D.step()`, `CoupledK4Cosserat.step()` |
| **Axiom 4** (Dielectric Saturation) | Op14 ($Z_{\text{eff}}$ from $A^2$) | `_update_z_local_total` (coupling module) |
| | Op3 (bond reflection $\Gamma$) | `op3_bond_reflection=True` in `k4_tlm.py` |

### Operators NOT directly represented

- **Op21** (multipole decomposition): used statically in Vol 1 Ch 8, no simulator analog.
- **Op7** (projection loss at 90°): captured indirectly via scatter matrix, not as a named operator.
- **Mutual inductance $\eta_{\text{vac}} / R_{\text{vac}}$ duality**: **NO named operator or symbol** in the simulator. The 0.5 off-diagonal elements of the scatter matrix implicitly encode it. **This is the missing piece for cascade-saturation tuning.**

## §4 — The cascade-saturation timescale gap

Per L3 doc 45 §4.2: the AVE-native pair-creation mechanism requires mutual-inductance backpressure — as $Z_{\text{eff}}$ at node $i$ diverges, the scattering matrix elements change, and the reflected wave from node $i$ propagates back to node $i-1$, triggering cascade saturation.

**The engine DOES this** via scatter matrix updating $z_{\text{local}}$. **But the timescale is the OUTER `dt` (K4 step). Within a single step, the cascade is frozen.**

If the cascade mechanism operates on a **sub-step timescale** — say, the bond-traversal time $\tau_{\text{relax}} = \ell_{\text{node}}/c$ — then the current integrator is missing it.

**Concrete check:** in natural units $\tau_{\text{relax}} = 1$, outer $dt = 1/\sqrt{2} \approx 0.707$. These are COMPARABLE timescales. So a single K4 step advances by roughly one $\tau_{\text{relax}}$ — barely enough to resolve cascade dynamics, but possibly missing fast sub-step rebound effects.

This is a **known engine limitation** flagged for future work, not a framework gap.

## Cross-references

- **Canonical manuscript:**
  - Vol 4 Ch 1:118-120 — mechanical impedance dual via Axiom 2
  - Vol 4 Ch 1:240 — mutual inductance / $R_{\text{vac}}$ dual
  - Vol 4 Ch 1:278 — per-cell $Z_{\text{cell}} = Z_0$
  - Vol 4 Ch 1:283 — $Z_0$ as node-to-node impedance ratio (Axiom 1 derivation)
  - Vol 4 Ch 1:364 — $Z_{\text{EH}} \to 0$ at full saturation
- **KB cross-cutting:**
  - [Substrate-Perspective Electron](../../../vol2/particle-physics/ch01-topological-matter/substrate-perspective-electron.md) — operational use of $Z_{\text{eff}}(r)$ at canonical electron configuration
  - [Photon Identification](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md) — $\Gamma = -1$ TIR mechanism using $Z_{\text{eff}} \to \infty$ then $Z_{\text{core}} \to 0$
  - [Pair Production Axiom Derivation](../../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — cascade-saturation mechanism via mutual inductance $\eta_{\text{vac}}$
  - [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) — independent Cosserat-side impedance content (mass from $G_c, I_\omega$)
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — Op14 $Z_{\text{eff}}$ as scale-invariant kernel application
- **Canonical engine:**
  - `src/ave/core/k4_tlm.py:196-221` — $z_{\text{local\_field}}$ implementation (nonlinear mode)
  - `src/ave/core/constants.py:222` — $Z_0$ definition
