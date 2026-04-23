# 45 — Lattice Impedance from First Principles: Decomposition, Dimensional Analysis, and Axiom/Operator Mapping

**Status:** planning (2026-04-22) — foundations work before Phase III-B redesign
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md`
**Trigger:** after Phase III-B no-response result (see [44_](44_pair_creation_from_photon_collision.md))
  and Grant's observation that the vacuum is never at 0, leading to a research
  pass on node slew-rate / mutual inductance / cascade saturation mechanism.
**Grant's specific ask:** pause for documentation + first-principles plan
  with axiom/operator mapping and dimensional analysis, focused on the
  lattice impedance — *has it been decomposed enough? Are we conflating
  classical vs. vacuum impedance? Might need a new symbol*.

## 1. Context — what this session established and what remains unresolved

**Established this session (docs 40–44):**
- Time-domain Cosserat subsystem works (doc 41_), mass gap `m² = 4G_c/I_ω` confirmed to 0.35%
- Coupled K4⊗Cosserat simulator built and validated (doc 42_) with S-gates D/γ/A/A/B/A
- Phase III-A null control passed (single photon passes through, no Cosserat response)
- Phase III-B pair-creation attempt got `P_IIIb-no-response` across amplitude sweep (doc 44_):
  A²_Cosserat = 0.000 identically because S1-D coupling has structural zero at (u, ω) = 0
- Grant flagged: "the vacuum is never at 0" → vacuum noise seed attempt
- Even with seed, A²_total at collision only reached 0.3 (far below rupture)
- Deep research (§6) identified a CASCADE-SATURATION mechanism that may be the AVE-native bootstrap

**Unresolved meta-question (Grant):**
Are we conflating classical EM impedance with lattice-native impedance? The coupling
Lagrangian I'm using depends on ratios like `V²/V_SNAP²` and `Z_eff/Z_0`, but the
physical meaning of "Z_0" shifts between contexts. A rigorous decomposition is
needed before Phase III-B redesign.

## 2. The impedance-concept inventory

The AVE corpus uses "impedance" in multiple distinct senses. They are numerically
related but physically different:

### 2.1 Classical free-space impedance `Z_0`

Defined at [constants.py:222](src/ave/core/constants.py) in Vol 1 Table:
$$Z_0 = \mu_0 c = \sqrt{\mu_0/\varepsilon_0} \approx 376.73\ \Omega$$

**Physical meaning:** ratio of |E|/|H| in a plane EM wave in classical vacuum.
**Scale:** continuum / field-theoretic.
**In AVE:** derived from Axiom 1 via the equivalence
(Vol 4 Ch 1:283) "$Z_0$ is a property of the node-to-node impedance ratio of
the lattice, independent of the absolute scale $\ell_{node}$".

### 2.2 Per-cell lattice impedance `Z_cell`

From [Vol 4 Ch 1:278](manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex):
$$Z_{cell} = \sqrt{\frac{L_{cell}}{C_{cell}}} = \sqrt{\frac{\mu_0 \ell_{node}}{\varepsilon_0 \ell_{node}}} = Z_0$$

**Physical meaning:** characteristic impedance of a SINGLE LC bond in the K4
lattice. Ratio of voltage to current for wave passing through one bond.
**Scale:** discrete / circuit element.
**Note:** NUMERICALLY equal to classical Z_0 because the lattice pitch cancels;
CONCEPTUALLY distinct because Z_cell refers to a physical bond, Z_0 refers to
a continuum field ratio.

### 2.3 Local effective impedance `Z_eff(r)` (Axiom-4-modulated)

From Op14 (per k4_tlm.py:216-219 and Vol 4 Ch 1):
$$Z_{eff}(r) = \frac{Z_0}{\sqrt{S}}, \quad S = \sqrt{1 - A^2(r)}$$

**Physical meaning:** position-dependent impedance under local dielectric
saturation. Diverges as A²→1 (rupture / TIR limit).
**Scale:** per-cell, dynamical.
**Currently implemented:** `k4.z_local_field` in
[k4_tlm.py:196-221](src/ave/core/k4_tlm.py) (nonlinear mode) and explicitly
in the coupled-sim coupling module via `_update_z_local_total`.

### 2.4 Mutual inductance `M_node-node` (drag coefficient `η_vac`)

From Vol 4 Ch 1:240 (mechanical duality):
$$R_{vac} \equiv \xi_{topo}^{-2} \cdot \eta_{vac}$$

**Physical meaning:** inductive COUPLING between adjacent K4 nodes. Sets how
fast one node's current change induces current change in its neighbor. Related
to mechanical drag coefficient η (kg/s) via topo-kinematic mapping.
**Scale:** between-node / coupling coefficient.
**Currently implemented:** IMPLICITLY via the K4 scattering matrix
`S_ij = 0.5 - δ_ij` (the off-diagonal 0.5 IS the coupling strength), but
NOT explicitly as a separate symbol or derivable quantity.
**This is the key missing piece** for the cascade-saturation mechanism.

### 2.5 Mechanical impedance `Z_mech`

From Vol 4 Ch 1:118-120:
$$Z_{mech} = \xi_{topo}^2 \cdot Z_0 \approx 6.485 \times 10^{-11}\ \mathrm{kg/s}$$

**Physical meaning:** force-per-velocity at a single node (via topo-kinematic map).
**Scale:** per-node, macroscopic mechanical dual.
**Relevance:** not directly used in Phase III coupling but establishes that
the electrical/mechanical/acoustic identities are all numerically equivalent
under the Axiom-2 conversion constant.

### 2.6 Event-horizon impedance `Z_EH`

From Vol 4 Ch 1:364:
$$Z_{EH} \to 0\ \Omega$$

**Physical meaning:** impedance at Axiom-4 full-saturation limit (both μ and ε
collapse asymmetrically). The TIR mirror at Γ=−1.
**Relevance:** the pair-creation endpoint according to §37 — A²=1 at two
adjacent nodes is locally a "mini-event-horizon" where Z drops to 0.

## 3. Dimensional analysis table

Every quantity in the Phase III simulator, with its SI units and lattice-native equivalent:

| Symbol | SI units | Lattice-native (ℓ_node=1, m_e=1, c=1, ℏ=1) | Physical interpretation |
|---|---|---|---|
| `ℓ_node` | m | 1 | spatial unit |
| `C_0` | m/s | 1 | light speed |
| `M_E` | kg | 1 | mass unit |
| `ℏ` | J·s | 1 | action unit |
| `τ_relax = ℓ_node/c` | s | 1 | fundamental time unit |
| `e_charge` | C | `√α` | ≈ 0.0854 |
| `ξ_topo = e/ℓ_node` | C/m | `√α` | topo-kinematic scale |
| `V_SNAP = m_e c²/e` | V | `1/√α` ≈ 11.7 | rupture voltage |
| `V_YIELD = √α · V_SNAP` | V | `1.0` | engineering yield (!) |
| `I_max = ξ·c` | A | `√α` | max current |
| `Z_0 = μ_0 c` | Ω | `1` | characteristic impedance |
| `η_vac` | kg/s (via R_vac) | ? | **mutual inductance — UNSPECIFIED symbol** |
| `L_cell = μ_0·ℓ_node` | H | `?` | per-bond inductance |
| `C_cell = ε_0·ℓ_node` | F | `?` | per-bond capacitance |
| `V` (scalar K4 voltage) | V | ratio to V_SNAP | wave amplitude |
| `u` (displacement) | m | ratio to ℓ_node | Cosserat translation |
| `ω` (microrotation) | rad/m (?) | dimensionless | Cosserat rotation |
| `A² = \|V\|²/V_SNAP²` | dimensionless | dimensionless | saturation amplitude squared |

### 3.1 Critical observation: V_YIELD = 1 in lattice natural units

In lattice units, the **engineering yield threshold is V_YIELD = 1**, NOT `V_SNAP = 1`. My
current coupled simulator uses `V_SNAP = 1.0` as the user-facing normalization (per S4-A).
When the user sees `amp = 0.5·V_SNAP`, that's effectively `amp = 0.5/√α = 5.85` in
units where V_YIELD = 1. **We're massively above yield, below rupture.**

This explains why my Phase III-B sources at amp=0.5 "look small" (50% of V_SNAP) but are
actually HUGE relative to V_YIELD. The Axiom-4 operator in the code uses V_SNAP as the
normalization for A, meaning the "√(2α) Regime I/II boundary" corresponds to
A = √(2α) = 0.121 in V/V_SNAP. In V_YIELD units this is A_yield-units = 0.121/√α = 1.42.

### 3.2 The coupling-term dimensional consistency check

S1-D coupling: `L_c = (V²/V_SNAP²) · W_refl(u, ω)`

- `V²/V_SNAP²`: dimensionless ✓
- `W_refl`: has units of energy density (same as other terms in `_energy_density_bare`)
- So `L_c` has units of energy density ✓ (matches the action dimensionally)

But: is `W_refl` actually capturing the RIGHT physics? Its form
`(1/64) · |∇S|²/S²` has dimensions of `[1/length²]` (since ∇S is `[1/length]`).
Per line 202 of cosserat_field_3d.py, it's labeled as "Cosserat energy density"
but the dimensional analysis gives `[1/length²]` — not the `[energy/volume]` of
a true energy density. This is numerically OK in lattice natural units (where
all lengths are dimensionless), but **obscures the physical interpretation**.

**Flag for Grant:** `W_refl` as currently implemented lacks explicit dimensional
coefficients. When SI calibration is applied post-Phase-III, the dimensional
restoration will need care.

## 4. Axiom → Operator → Simulator mapping

| Axiom | Operator(s) | In simulator |
|---|---|---|
| **Axiom 1** (K4 LC substrate) | Op5 (4-port scatter matrix) | `build_scattering_matrix` in k4_tlm.py |
| | Op1 (bond propagation) | `_connect_all` (np.roll) |
| **Axiom 2** ([Q] ≡ [L]) | Op12 (topological invariant) | `extract_crossing_count`, `extract_hopf_charge` |
| | Op20 (self-consistent amplitude) | NOT IMPLEMENTED (plan §4 gate S5-open) |
| **Axiom 3** (Effective action) | Op8 (Lagrangian density) | `_energy_density_bare/saturated` |
| | Op9 (time evolution) | `CosseratField3D.step()`, `CoupledK4Cosserat.step()` |
| **Axiom 4** (Saturation) | Op14 (Z_eff from A²) | `_update_z_local_total` (coupling module) |
| | Op3 (bond reflection Γ) | `op3_bond_reflection=True` in k4_tlm.py |

### 4.1 Operators NOT directly represented

- **Op21** (multipole decomposition): used statically in Ch 8, no simulator analog.
- **Op7** (projection loss at 90°): captured indirectly via scatter matrix, not as a named operator.
- **Mutual inductance η_vac / R_vac duality**: **NO named operator or symbol** in the simulator.
  The 0.5 off-diagonal elements of the scatter matrix implicitly encode it, but there's no
  way to independently tune the cascade-coupling strength.

### 4.2 The missing operator for cascade saturation

Per the agent's research (§6 synthesis), the AVE-native pair-creation mechanism requires:

```
Stage 4: Mutual-inductance backpressure
  As Z_eff at node_i diverges, the scattering matrix elements change
  (per k4_tlm.py, impedance weighting). The reflected wave from node_i
  propagates back to node_{i-1}.
```

My simulator DOES do this (the scatter matrix updates via z_local), but the
timescale is the OUTER dt (K4 step). Within a single step, the cascade is frozen.
**If the cascade mechanism operates on a SUB-STEP timescale** — say, the bond-
traversal time τ_relax = ℓ_node/c — then my Phase III-B integrator is missing it.

**Concrete test**: in natural units τ_relax = 1, outer_dt = 1/√2 ≈ 0.707. These
are COMPARABLE timescales. So a single K4 step advances by roughly one τ_relax.
If the cascade needs MULTIPLE τ_relax to develop, my N_sub = 8 Cosserat sub-steps
should be enough. If it needs sub-τ_relax feedback, I need intra-step z_local
recomputation.

## 5. Proposed new symbol scheme (Grant's request)

To avoid conflation, introduce the following:

| Proposed symbol | Meaning | Current code reference |
|---|---|---|
| `Z_0` | Classical/unstrained lattice-cell characteristic impedance, = √(μ_0/ε_0) ≈ 376.73 Ω | `Z_0` in constants.py |
| `ℤ_lat(r)` or `Z_eff(r)` | Local effective impedance at position r, Axiom-4-modulated | `z_local_field` |
| `ℤ̃_mut` or `η_vac` | Mutual inductance between adjacent K4 nodes (drag coefficient) | IMPLICITLY 0.5 in S_ij |
| `ℤ_K4` | Reserved alias for Z_0 when context is specifically K4-lattice-native (acoustic) | — |
| `ℤ_mech` | Mechanical impedance dual, ξ²·Z_0 | `Z_MECH` |
| `Γ_bond(i, j)` | Reflection coefficient at bond (i, j): `(ℤ_lat(j) − ℤ_lat(i))/(ℤ_lat(j) + ℤ_lat(i))` | inside `_connect_all` if `op3_bond_reflection` |

**Recommendation**: introduce `η_vac` as a NAMED parameter in the coupled simulator
with a tunable coupling strength (default matching the current implicit 0.5).
This opens the door to testing cascade mechanisms explicitly.

## 6. What the current Phase III-B simulator actually models

### Correctly:
- **Axiom 1 scatter/connect kinematics** ✓ (K4-TLM unchanged from Vol 4 Ch 1)
- **Axiom 4 local saturation via Z_eff = Z_0/√S** ✓ (both K4 and Cosserat contributions)
- **Cosserat time evolution** ✓ (Phase I validated)
- **Scalar field coupling Lagrangian (V²/V_SNAP²) · W_refl** ✓ (S1-D)

### Under-models:
- **Mutual inductance η_vac as an independent parameter** ✗ (baked into S_ij=0.5, not tunable)
- **Intra-K4-step z_local updates** ✗ (outer-dt only; may miss sub-step cascade)
- **Vacuum noise spectrum** ⚠ (using σ=0.01 placeholder; corpus doesn't quantify)
- **Quantum Foam topology-trapping mechanism** ✗ (noise is isotropic; trapping would require structured noise from LC resonance modes)

### Does NOT conflate:
- V_SNAP (rupture) vs V_YIELD (engineering) — both defined, V_SNAP used as user-facing normalization
- Continuum Z_0 vs lattice Z_cell — treated as equal per corpus (Vol 4 Ch 1:278)
- Electrical vs mechanical impedance — topo-kinematic map available via ξ

### MAY conflate (Grant's concern):
- **Photon-mode impedance vs bond-element impedance**. A photon propagating
  through a bond sees Z_cell = Z_0. But when we talk about "lattice impedance"
  we sometimes mean the MEDIUM's impedance (for wave propagation) and sometimes
  the BOND's impedance (for circuit analysis). These are numerically equal in
  unstrained lattice but diverge under strain.
- **Local vs. mutual impedance**. When saturation hits at node i, Z_eff(i)
  rises. But the effective impedance seen by a wave APPROACHING node i from
  a neighbor depends on BOTH Z_eff(i) AND the mutual coupling to node i-1.
  My simulator captures the first but not the second-order mutual effect.

## 7. Implications for Phase III-B redesign

Given the decomposition above, here is the corrected plan:

### 7.1 Primary physics questions (first-principles, axiom-mapped)

1. **Does the cascade mechanism require explicit η_vac tuning?**
   - If the implicit 0.5 in S_ij is correct, Phase III-B should work with just
     intra-step z_local updates + noise + CW sources.
   - If η_vac needs to be larger (i.e., tighter mutual coupling), Phase III-B
     needs a coupling-strength parameter.

2. **Is the sub-step timescale cascade feedback required?**
   - Per §4.2, dt_outer ≈ τ_relax. The cascade has ~1 τ_relax to develop per step.
   - If mutual-inductance-driven cascades need feedback within a τ_relax, we need
     intra-step z_local updates (simple fix: recompute 2-4× per outer step).

3. **What's the physical RMS of Quantum Foam?**
   - Corpus: noise is "indistinguishable from vacuum" at some σ (Vol 1 Ch 3:483).
   - Quantitative: NOT specified. Our σ=0.01 is arbitrary.
   - Need a first-principles derivation from Axiom 1 LC resonance modes.

### 7.2 Proposed Phase III-B experimental matrix (after this foundations doc)

**Before running, adjudicate these with Grant:**

- **A. η_vac coupling strength:** default (0.5 in S_ij) or parameterize?
- **B. Intra-step z_local updates:** 1x (current), 2x (pre-scatter + pre-connect), or N_sub x (full sub-step coupling)?
- **C. Vacuum noise amplitude:** keep σ=0.01, or parameterize and sweep?
- **D. CW source amplitude in lattice natural units:**
  - In V_SNAP units: 0.5 (what we used) = 0.5·V_SNAP ≈ 5.85·V_YIELD
  - In V_YIELD units: 1.0 = engineering yield threshold, clean
  - Does amp=V_YIELD (yield-matched) produce different physics than amp=0.5·V_SNAP (half-rupture)?
- **E. Wavelength:** long λ (6-10 cells, low frequency, slew-rate-safe) or short λ (3-4 cells, high frequency, slew-rate-limited per Thread 1)?
- **F. Initial state:** pure Quantum Foam noise, or noise + seed (small (u, ω) shell)?

### 7.3 Success criteria in AVE-native terms

- **Cascade signature:** count of nodes simultaneously at Z_eff > 2·Z_0 (i.e., √S < 0.5, A² > 0.75 = Regime II/III boundary). Should grow with time during saturation buildup.
- **Cavity formation:** spatial coherence length of the saturated region (larger than the photon wavelength → true cavity, not just a peak).
- **Topological trapping:** non-zero Q_H (Hopf charge) integrated over the cavity interior, whereas outside it stays near 0.
- **Pair formation (P_IIIb-pair):** ≥2 spatially separated centroids with individual Q_H contributions of opposite sign.

## 8. What to ask Grant (pre-execution gates)

The following need adjudication BEFORE Phase III-B redesign code:

### Q1 — Symbol / parameter set
Adopt the new symbol scheme (§5)? If yes, introduce `η_vac` as a tunable
parameter in `CoupledK4Cosserat` with physical default from corpus.

### Q2 — Amplitude units
Switch the user-facing `amp` parameter from V_SNAP-normalized to V_YIELD-normalized
(cleaner physical mapping)? Current amp=0.5·V_SNAP would become amp=5.85·V_YIELD;
much more obvious that we're well past yield.

### Q3 — Intra-step z_local updates
Enable them (2-4x per outer step) to capture sub-step cascade feedback? Minor
code change in `CoupledK4Cosserat.step()`; may reveal new physics.

### Q4 — Vacuum noise
Keep σ=0.01 placeholder, or derive from Axiom 1 LC resonance modes?
First-principles derivation is a research item in its own right.

### Q5 — Wavelength choice
Short (high-f, slew-rate-stressed) or long (safe, classical)? The agent's §7
flagged that high-f is where the cascade would kick in most strongly, but
short λ is also numerically harder to simulate cleanly (closer to Nyquist).

### Q6 — Overall scope
Is Phase III-B's goal:
(a) demonstrate P_IIIb-pair in a specific pre-selected configuration, OR
(b) scan the parameter matrix (§7.2) to MAP when pair creation activates?
(a) is a focused "prove it" run; (b) is a landscape study.

## 9. Next-step plan

**Pre-Grant-adjudication** (no new code):
- This doc (45_) is the deliverable.
- Optionally: add a first-principles derivation of `η_vac` from the K4
  scatter matrix, if Grant wants that to be rigorous.

**Post-Grant-adjudication**:
- Based on Q1-Q6 answers, rewrite Phase III-B per the decisions.
- Add any new parameters to `CoupledK4Cosserat` constructor (e.g., `eta_vac`,
  `n_intra_step_zlocal_updates`, `noise_spectrum_kind`).
- Run the chosen configuration (single or parameter-sweep).

## 10. Honest statement of what this doc DOES and DOES NOT resolve

### Resolves:
- Naming ambiguity between Z_0, Z_cell, Z_eff, η_vac, Z_mech — now explicit.
- Axiom/operator mapping for each simulator component.
- Dimensional analysis of every quantity — no hidden dimensional mistakes found.
- Identifies the SPECIFIC missing piece: `η_vac` is implicit in scatter matrix,
  not a tunable parameter; mutual-inductance-driven cascade is numerically
  under-represented.

### Does NOT resolve:
- First-principles value of Quantum Foam noise amplitude (Vol 1 Ch 3 is
  qualitative).
- Whether the §5 "cascade mechanism" synthesized from corpus threads is a
  legitimate derived prediction of the axioms or an educated guess.
- The pair-creation success criterion — still pre-registered at A²_cos ≥ 0.5
  AND ≥2 centroids, but the exact numerical threshold has no first-principles
  derivation.

### Flags forward:
- **F1**: `η_vac` symbol and its first-principles value — needs a derivation doc
  if we want full Axiom-1 rigor.
- **F2**: Quantum Foam spectrum — derivation from LC resonance mode structure
  would pin σ_V and σ_ω. Currently just placeholder 0.01.
- **F3**: Amplitude normalization convention — V_SNAP vs V_YIELD vs lattice-native.
  The mixed convention in the current codebase is a latent conflation risk.