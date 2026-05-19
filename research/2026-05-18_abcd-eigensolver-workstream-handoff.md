# Workstream Handoff — ABCD-Matrix Eigensolver for Q-G47 Interpretation G Closure

**Date drafted**: 2026-05-18 night
**Status**: PENDING — next-session Priority #1
**Estimated scope**: ~2–4 hours (5 phases) — REVISED DOWN from initial ~4–8 hr estimate after corpus-grep surfaced existing `src/ave/solvers/transmission_line.py` (944 lines, canonical ABCD library already implemented)
**Author**: AVE implementer lane, 2026-05-18 session
**Workstream-precipitating finding**: [`research/2026-05-18_q-g47-interpretation-g-result.md`](research/2026-05-18_q-g47-interpretation-g-result.md) §5+§8
**Workstream prereq**: read precipitating-result doc first; this handoff assumes context.

## 0. TL;DR

Build an ABCD-matrix eigensolver that **directly computes the bound-state eigenmode** of a K4-TLM-bond TIR cavity at the canonical electron operating point, then extracts the Clifford-torus phase-space coordinates $(R, r)$ from the eigenvector. Compare to canonical Golden Torus targets $(\varphi/2, (\varphi-1)/2, 1/4)$. This SETTLES Interpretation G (K4-TLM A5 closure) DEFINITIVELY — bypasses all five methodology holes that 2026-05-18 session's FDTD post-hoc projection approach surfaced.

**Why this workstream is needed at all**: doc 78's K4-TLM evolve-and-measure (Mode III FAIL, persistence violated) + this session's MasterEquationFDTD evolve-and-project (Outcome A, no chirality mechanism) BOTH fail to verify Golden Torus realization. The failure is in the evolve-then-extract METHODOLOGY, not necessarily in the physics. ABCD eigensolve sidesteps evolution entirely.

**Canonical infrastructure already exists** ([`src/ave/solvers/transmission_line.py`](src/ave/solvers/transmission_line.py:45)): `abcd_segment`, `abcd_shunt`, `abcd_stub`, `abcd_cascade`, `s11_from_abcd` — the ABCD primitives are canonical AVE corpus, scale-invariant per the file's docstring "ABCD matrix for a TL segment → propagation; ABCD matrix for a shunt Y → junction coupling; S₁₁ from total ABCD → reflection (mismatch). The SAME three operators appear at all scales." Workstream composes them for the electron cavity.

## 1. Why this workstream exists — methodology gap

The 2026-05-18 Interpretation G test (this session) ran the geometry-verification observer on `MasterEquationFDTD` v14 canonical and found Outcome A (R/r = 13.29 vs target φ² = 2.618, 407% deviation). The `verify-before-cite` grep then surfaced that doc 78 (2026-04-27) had already run the K4-TLM-native equivalent on `VacuumEngine3D` (Mode III FAIL with persistence violation). Two engines, two different approaches, both fail to verify the canonical Golden Torus geometry of the electron bound state.

**Five methodology holes** that the FDTD-evolve-and-extract approach has:

| Hole | Source | Evidence |
|---|---|---|
| Post-hoc continuum→TLM projection ambiguity | `substrate-native-check` skill Q1 (this session) | The MasterEquationFDTD lacks native V_inc/V_ref state; the Riemann-invariant projection $V_{inc} = (V \pm \partial_r V)/2$ is an underdetermined post-hoc map for a continuum solution |
| Persistence decay problem | doc 78 §1.3 / §3.1 | K4-TLM bound state seeded AT Golden Torus DECAYED to 33% of initial amplitude within recording window — measurement captured decay phase, not stable attractor |
| Single-mode-Lissajous-degeneracy | Pre-run analysis (this session) | For any single-frequency oscillation $V(t) = A\cos(\omega t)$, the projection $(V \pm \partial_t V)/2$ produces straight-line trajectory in $(V_{inc}, V_{ref})$ plane — degenerate ellipse regardless of underlying topology |
| Substrate-engine mismatch | Grant intervention (this session, §6 of result doc) | MasterEquationFDTD is scalar EMT continuum — NO chiral coupling, NO Cosserat torque, NO K4 connectivity; the chirality mechanism for multi-mode (2,3) torus knot structure is ABSENT |
| Engine-attractor randomness | `run_v14_canonical` design | Sech seed at $A_{peak}=0.85$, $R=2.5$ evolves to whatever attractor the Master Equation supports; that attractor isn't necessarily the canonical electron bound state |

**ABCD eigensolver bypasses all 5**:

| Hole | ABCD eigensolver fix |
|---|---|
| Projection ambiguity | K4-TLM ABCD is NATIVE — eigenvector gives $(V, I)$ directly; $V_{inc}/V_{ref}$ decompose from definition $V_{inc/ref} = (V \pm Z_0 I)/2$ |
| Persistence decay | Eigenmodes are STATIONARY by construction — no time evolution, no decay |
| Single-mode degeneracy | Eigenvector has well-defined components for each mode of the cavity matrix; multi-mode structure is encoded in the matrix, not the time-series |
| Substrate-engine mismatch | ABCD inherits whatever chirality / coupling the K4 bond + cavity composition defines — controllable, not engine-fixed |
| Attractor randomness | Solves the algebraic eigenproblem for the canonical cavity geometry directly — no evolution, no seed dependence |

## 2. Goal statement (physical observable + canonical comparison)

**Goal**: Compute the dominant eigenmode of the round-trip ABCD matrix $M_{RT}$ for a closed (TIR-bounded) K4-TLM bond cavity arranged in the canonical electron Clifford-torus topology (Vol 1 Ch 8: trefoil knot at dielectric ropelength, $(p, q) = (2, 3)$). Extract the cavity's $(R, r)$ phase-space coordinates from the eigenvector and compare to:

- **R_GOLDEN_TORUS** = $\varphi/2$ ≈ 0.8090 (canonical, [`src/ave/core/constants.py:163`](src/ave/core/constants.py:163), added this session)
- **R_GOLDEN_TORUS_MINOR** = $(\varphi-1)/2$ ≈ 0.3090 (canonical, [`src/ave/core/constants.py:164`](src/ave/core/constants.py:164))
- **RR_GOLDEN_TORUS** = $1/4$ (algebraic identity from $\varphi^2 = \varphi + 1$; canonical, [`src/ave/core/constants.py:165`](src/ave/core/constants.py:165))
- **R/r target** = $\varphi^2 \approx 2.618$ (scale-invariant ratio)

**Adjudication criteria** (per `consistency-vs-emergence` skill classification — this is an INTRA-FRAMEWORK CONSISTENCY CHECK):

| Outcome | Criterion | Interpretation |
|---|---|---|
| **POSITIVE** | $(R, r)$ within 5% of Golden Torus targets AND $R/r$ within 2% of $\varphi^2$ | Theorem 3.1' precondition VERIFIED; 50% $\Lambda_{total}/\alpha_{cold}^{-1}$ gap reported in doc 131 is NOT geometric mismatch — must be UV running / loop corrections / other (re-test Interpretation F: $\alpha(\Lambda_{UV})$ running). Foreword line 106 can REMOVE Interpretation G flag. Theorem 3.1' leaf §49-63 needs precondition statement added but the BRIDGE itself holds. |
| **NEGATIVE** | $(R, r)$ deviates >10% from targets OR $R/r$ deviates >5% from $\varphi^2$ | Theorem 3.1' precondition GENUINELY UNFULFILLED by canonical electron cavity — the 4π³+π²+π = 137.036 derivation of Vol 1 Ch 8 has a deeper structural issue. Walk-back propagates to Vol 1 Ch 8 §3, foreword line 106, Theorem 3.1' leaf §49-63, BRANCH STATE weak-spot #2 (2b), L5 axiom_derivation_status A-001 / Q-G47 status row. |
| **AMBIGUOUS** | Eigensolve produces no eigenvalue with $|\lambda| = 1 \pm$ small (no sustained mode) | The K4-TLM bond cavity with canonical Clifford-torus geometry does NOT support a sustained mode at the operating point — even more severe issue than NEGATIVE. Requires re-examination of canonical electron-cavity geometry assumption itself. |

## 3. Substrate-physics foundation (pedantic — read before any code)

### 3.1 K4 lattice (Axiom 1)

Per `manuscript/ave-kb/vol1/axioms/ax1-chiral-laves-k4-cosserat-crystal.md` (canonical), the substrate is a **chiral Laves K4 Cosserat crystal**:

- **K4 connectivity**: 4 bonds per node, arranged in a chiral tetrahedral pattern (NOT symmetric tetrahedral — the chirality is structural, not approximate)
- **Bond LC tank**: each bond is a transmission-line LC tank with characteristic impedance $Z_0$ (canonical = 1 in natural units; SI value `Z_0 = sqrt(MU_0/EPSILON_0)` ≈ 376.73 Ω per [`src/ave/core/constants.py:81`](src/ave/core/constants.py:81))
- **Lattice pitch**: $\ell_{node} = \hbar / (m_e c)$ ≈ 3.86e-13 m per [`src/ave/core/constants.py:180`](src/ave/core/constants.py:180); natural-unit normalization sets $\ell_{node} = 1$

The chirality matters here because **asymmetric spring torques at the K4 node intrinsically couple radial breathing modes to angular precession modes** (Grant intervention, this session). This is the canonical mechanism for the (2,3) torus knot topology arising from a "simple breathing" bound state — the 2 = orbital winding, 3 = chiral spin precession, with frequencies in ratio 2:3.

### 3.2 Bond ABCD matrix (canonical, from `transmission_line.py:45-74`)

For a single transmission line segment with characteristic impedance $Z_c$ and complex propagation constant × length $\gamma \ell$:

$$\begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} \cosh(\gamma\ell) & Z_c \sinh(\gamma\ell) \\ \sinh(\gamma\ell)/Z_c & \cosh(\gamma\ell) \end{bmatrix}$$

For lossless LC ($\gamma = j\beta$, $\beta = \omega/c$): $A = D = \cos(\beta\ell)$, $B = jZ_c\sin(\beta\ell)$, $C = j\sin(\beta\ell)/Z_c$. For lossy (Op14 saturation modulates local $c_{eff} = c \cdot \sqrt{1-A^2}$): $\gamma$ acquires a real part proportional to the per-cycle reactive leak $1/Q = \alpha$ (Theorem 3.1' line 75 canonical: "per-cycle reactive leak fraction = $1/Q = \alpha$").

**Canonical file**: [`src/ave/solvers/transmission_line.py:45`](src/ave/solvers/transmission_line.py:45) — already implements this.

### 3.3 Cosserat torque coupling (Op14, Op17)

The K4 chirality enters the ABCD formalism via **Cosserat cross-port coupling**:

- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md` — Op14 cross-sector trading (V ↔ Cos coupling at the bond)
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md` — Op14 local clock modulation (relevant when bound state is at sub-saturation)
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md` — canonical reactive-power table that the matched-LC κ_entrain formula traces to

**Implementation hook**: at each K4 node, the 4-port ABCD composition needs to encode the chirality. Two possible approaches:

(a) **Phase-shift junction**: each port-pair through the K4 node carries an additional Cosserat-coupling phase $\phi_C$ (chirality direction-dependent: $+\phi_C$ for CW, $-\phi_C$ for CCW). The 4-port ABCD becomes a 4×4 scattering matrix with chirality-distinct off-diagonal terms.

(b) **Shunt admittance**: model the chiral torque coupling as a shunt admittance $Y_C$ at the K4 node, with imaginary part (capacitive/inductive) controlling the precession frequency. Use `abcd_shunt(Y_C)` from [`src/ave/solvers/transmission_line.py:76`](src/ave/solvers/transmission_line.py:76).

Approach (a) is more substrate-native but heavier to implement. Approach (b) is simpler and may suffice as a first cut. **Recommend (b) for Phase 2 first cut; escalate to (a) if (b) doesn't recover (2,3) topology**.

Canonical Cosserat coupling code: [`src/ave/topological/k4_cosserat_coupling.py`](src/ave/topological/k4_cosserat_coupling.py) — read this BEFORE Phase 2 to understand the existing Cosserat implementation; the ABCD wrapper should call into this, not re-derive.

### 3.4 TIR boundary at electron α-slew (Theorem 3.1')

Per [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:65-75`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:65) (verbatim verified this session via `verify-before-cite`):

> *"Vol 4 Ch 1:423-467 describes the saturation boundary as Total Internal Reflection: $Z_{\text{core}} \to 0$ drives $\Gamma = -1$ (perfect short), confining the LC oscillation. The effective radiation resistance per spinor cycle is $Z_0 / (4\pi)$... $Z_0$ is the vacuum's characteristic impedance through which any radiated energy would escape; $4\pi$ is the electron's spinor-cycle-phase requirement (SU(2) double-cover of SO(3))..."*

**Implementation**: the cavity boundary condition is $\Gamma = -1$ (perfect short circuit) → ABCD terminates as a load $Z_L = 0$. For ABCD round-trip composition: $M_{RT}$ closes back on itself, so the boundary condition becomes a **periodic boundary**: $\psi_{after} = \lambda \psi_{before}$ with $|\lambda| = 1$ for sustained modes.

### 3.5 The (2,3) trefoil topology of the canonical electron

Per [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) (and [`src/ave/core/constants.py:120-149`](src/ave/core/constants.py:120) canonical block):

> *"Trefoil at dielectric ropelength is pulled tight by vacuum tension; S₁₁ minimization (Universal Operator #6, $\lambda_{min}(S^\dagger S) \to 0$) enforces: $R - r = 1/2$ (self-avoidance), $R \cdot r = 1/4$ (holomorphic screening at $\pi^2$ surface optimum). Solving: $R = \varphi/2$, $r = (\varphi-1)/2$ (Golden Torus)."*

The (2,3) trefoil knot lives on the Clifford torus with these radii. The **round-trip path** for $M_{RT}$ composition: traverse $p = 2$ revolutions of the major circle (circumference $2\pi R$) × $q = 3$ revolutions of the minor circle (circumference $2\pi r$). Total path length $L_{RT} = 2 \cdot 2\pi R + 3 \cdot 2\pi r$ (this is the Φ_link-equivalent for the trefoil).

For Op21 multi-mode generalization (`theorem-3-1-q-factor.md:99` canonical): "each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle, giving $Q = \ell$ per mode." The ABCD eigenmode amplitudes give the $\ell$-per-mode counts directly.

### 3.6 Riemann invariants vs ABCD parameters — disambiguation

A potential source of confusion (caught in this session's substrate-native walk): the K4-TLM canonical $(V_{inc}, V_{ref})$ are NOT Riemann invariants of the underlying continuum PDE — they are **bookkeeping variables of the TLM scatter-connect ALGORITHM**, defined as:

$$V_{inc} = (V + Z_0 I)/2, \quad V_{ref} = (V - Z_0 I)/2$$

where $V$ is the node voltage and $I$ is the bond current. **The ABCD formalism keeps $(V, I)$ as state; the $(V_{inc}, V_{ref})$ are recovered from $(V, I)$ by definition at any point along the cavity**. This is the substrate-native extraction (no post-hoc projection from continuum gradients) that the FDTD approach lacked.

## 4. Mathematical formulation (full pedantic spec)

### 4.1 Cavity matrix construction

Let the canonical electron cavity be described by:
- $N$ ABCD segments along the (2,3) trefoil path
- $K$ K4-node junctions (4-port → 2-port reductions via chiral shunt approach (b) above)
- Periodic boundary: $\psi_{N+1} = \psi_1$ (closure of the trefoil)

Then:

$$M_{RT} = \prod_{i=N}^{1} M_i$$

where $M_i$ is either an `abcd_segment(Z_c, gamma_l)` (for a bond) or `abcd_shunt(Y_C)` (for a K4 junction with Cosserat coupling).

For the canonical Golden Torus at $R = \varphi/2$, $r = (\varphi-1)/2$ in $\ell_{node} = 1$ natural units:
- Major-circle bond count: depends on lattice realization of $2\pi R / \ell_{node} \approx 5.08$ → round to 5 bonds per major revolution
- Minor-circle bond count: $2\pi r / \ell_{node} \approx 1.94$ → round to 2 bonds per minor revolution
- Trefoil round-trip: $2 \cdot 5 + 3 \cdot 2 = 16$ bonds (one choice; alternative discretizations should be cross-validated)
- K4 junctions encountered: ~16 (one per bond traversal)

### 4.2 Eigenvalue interpretation

For the cavity matrix $M_{RT}$ (2×2 if 1-port-pair reduction; larger if higher-dimensional state vector):

$$M_{RT} \cdot \psi = \lambda \cdot \psi$$

Solve via `numpy.linalg.eig(M_RT)`. Interpret:

| $\lambda$ | Mode type |
|---|---|
| $\|\lambda\| = 1$ exactly (lossless) | Sustained mode — bound state at this frequency |
| $\|\lambda\| < 1$ slightly | Lossy sustained mode — leaks at rate $1/Q = 1 - \|\lambda\|$ |
| $\|\lambda\| > 1$ | Unstable mode — gain (unphysical for passive cavity) |
| $\|\lambda\| \ll 1$ | Strongly attenuated mode — not a bound state at this frequency |

For the canonical electron at TIR boundary, expect $\|\lambda\| \approx 1 - \alpha = 1 - 1/137$ ≈ 0.9927 per Theorem 3.1' line 75 ("$1/Q = \alpha$").

### 4.3 (R, r) extraction from eigenvector

The dominant eigenvector $\psi = (V, I)^T$ at the cavity reference point gives:

$$V_{inc} = (V + Z_0 I)/2, \quad V_{ref} = (V - Z_0 I)/2$$

Then $R = |V_{inc}|$, $r = |V_{ref}|$ (in $Z_0 = 1$ natural units). Compare to canonical targets.

**Normalization choice**: the eigenvector is defined up to a scalar. Choose normalization $|V|^2 + |Z_0 I|^2 = 1$ (energy conservation, total stored energy = 1 in natural units). Then $|V_{inc}|^2 + |V_{ref}|^2 = 1$ and $(R, r) = (|V_{inc}|, |V_{ref}|)$ are dimensionless fractions on the unit circle.

**Comparison to Golden Torus targets**: at $R = \varphi/2 \approx 0.809$ and $r = (\varphi-1)/2 \approx 0.309$, $R^2 + r^2 = (\varphi^2 + (\varphi-1)^2)/4 = (2\varphi^2 - 2\varphi + 1)/4 = (2(\varphi+1) - 2\varphi + 1)/4 = 3/4$. So under the energy-normalization $R^2 + r^2 = 1$, the targets should be rescaled by $\sqrt{4/3}$ → effective targets $R^* = \varphi/2 \cdot \sqrt{4/3} \approx 0.934$, $r^* = (\varphi-1)/2 \cdot \sqrt{4/3} \approx 0.357$. Verify this normalization choice before adjudication.

**Scale-invariant discriminator**: regardless of normalization, $R/r$ should equal $\varphi^2 \approx 2.618$ at Golden Torus. This is the load-bearing check.

## 5. Pedantic cross-reference inventory

### 5.1 Canonical AVE-Core leaves (corpus authority)

| Leaf | Purpose | Location |
|---|---|---|
| Theorem 3.1' Q-factor | Λ_i = Q_i bridge (THIS workstream's tested precondition) | [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) |
| Vol 1 Ch 8 α from Golden Torus | Canonical electron geometry derivation | [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) |
| Op14 cross-sector trading | V↔Cos coupling at bond | [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md) |
| Op14 local clock modulation | Sub-saturation $c_{eff}$ modulation | [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) |
| Orbital friction paradox + reactive-power table | Per-cycle reactive vs real leak (relevant for chirality phase factor) | [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) |
| Matched-LC κ_entrain | Coupling formula (relevant if reformulating ABCD as matched-LC system) | [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md`](manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md) |
| Universal operators index | Op7 / Op14 / Op17 / Op21 canonical | [`manuscript/ave-kb/common/operators.md`](manuscript/ave-kb/common/operators.md) |
| z₀-derivation | Characteristic impedance Z_0 canonical | [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) |

### 5.2 Engine code (AVE-Core/src/)

| File | Purpose for this workstream |
|---|---|
| [`src/ave/solvers/transmission_line.py`](src/ave/solvers/transmission_line.py) | **Primary infrastructure** — 944 lines, contains `abcd_segment`, `abcd_shunt`, `abcd_stub`, `abcd_cascade`, `s11_from_abcd`, JAX-backed equivalents, and nodal Y-matrix functions. Phase 1 of this workstream verifies coverage; Phase 2-4 composes for the cavity. |
| [`src/ave/core/k4_tlm.py`](src/ave/core/k4_tlm.py) | K4-TLM canonical scatter+connect engine. Reference for V_inc/V_ref state arrays (`V_inc[nx,ny,nz,4]`, `V_ref[nx,ny,nz,4]` at lines 196-197) and scatter coefficient implementation (`V_inc_A[k] = Γ * V_ref_A[k] + T * V_ref_B[k]` at line 399). |
| [`src/ave/topological/vacuum_engine.py`](src/ave/topological/vacuum_engine.py) | `VacuumEngine3D` (used by doc 78 prior cross-validation). Reference for how the K4 + Cosserat are coupled at engine level. |
| [`src/ave/topological/k4_cosserat_coupling.py`](src/ave/topological/k4_cosserat_coupling.py) | K4-Cosserat cross-coupling implementation. The ABCD chirality wrapper (approach (a) or (b) in §3.3) should call into this module, not re-derive Cosserat physics. |
| [`src/ave/topological/cosserat_field_3d.py`](src/ave/topological/cosserat_field_3d.py) | Cosserat ω/u field implementation. Phase 2 (K4 cell ABCD composition with chirality) references this for canonical Cosserat coupling form. |
| [`src/ave/topological/soliton_bond_solver.py`](src/ave/topological/soliton_bond_solver.py) | Existing bond solver — read to understand pattern conventions before writing the new ABCD eigensolver script. |
| [`src/ave/topological/borromean.py`](src/ave/topological/borromean.py), [`src/ave/topological/faddeev_skyrme.py`](src/ave/topological/faddeev_skyrme.py) | Topological-solver pattern references (for the proton; trefoil-electron ABCD should follow analogous patterns). |
| [`src/ave/solvers/radial_eigenvalue.py`](src/ave/solvers/radial_eigenvalue.py), [`src/ave/solvers/coupled_resonator.py`](src/ave/solvers/coupled_resonator.py) | Sibling eigensolvers — read for code conventions (input validation, output format) before writing the ABCD eigensolver. |

### 5.3 Canonical constants ([`src/ave/core/constants.py`](src/ave/core/constants.py))

| Constant | Line | Purpose |
|---|---|---|
| `C_0` | 78 | Speed of light (= 1 natural units) |
| `MU_0`, `EPSILON_0`, `Z_0` | 79-81 | Vacuum impedance (= 1 natural units) |
| `HBAR` | 82 | Action quantum (= 1 natural units) |
| `M_E` | 96 | Electron mass (sets ℓ_node) |
| `ALPHA` | 100 | Fine-structure constant (CODATA reference) |
| `ALPHA_COLD_INV`, `ALPHA_COLD` | 150-151 | $4\pi^3 + \pi^2 + \pi$ canonical |
| `PHI`, `R_GOLDEN_TORUS`, `R_GOLDEN_TORUS_MINOR`, `RR_GOLDEN_TORUS` | 162-165 | Golden Torus targets (added this session per `ave-canonical-source` skill) |
| `L_NODE` | 180 | Lattice pitch $\ell_{node}$ |
| `TAU_RELAX_SI`, `TAU_RELAX_NATIVE` | 275-276 | Thixotropic relaxation time (relevant for Op14 dynamics) |
| `R_I`, `R_II`, `R_III` | 348-350 | Phase boundaries (Axiom 4) |

**Discipline reminder** (per `ave-canonical-source` skill): ABCD solver imports MUST use `from ave.core.constants import ...` — no hardcoded numerical literals for any of the above. Cross-check verify block at top of solver per skill Step 4.

### 5.4 Prior FDTD-based attempts (this workstream's precipitating context)

| Doc | Engine | Approach | Outcome | Cross-reference |
|---|---|---|---|---|
| [`research/_archive/L3_electron_soliton/68_phase_quadrature_methodology.md`](research/_archive/L3_electron_soliton/68_phase_quadrature_methodology.md):62-71 | n/a | Canonical phase-space (V_inc, V_ref) framing | Sets the corpus-canonical R_phase/r_phase target | Background |
| [`research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md`](research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md) | `VacuumEngine3D` (K4-TLM native) | Seeded AT (2,3) Golden Torus ansatz, evolved 200 Compton periods | **Mode III FAIL** — R/r per-bond ∈ {2.16, 2.21, 5.47, 5.72}; persistence 33% (decay) | Methodology gap #2 (persistence) |
| [`research/_archive/L3_electron_soliton/130_q_g47_path_d_engine_cross_validation_first_pass.md`](research/_archive/L3_electron_soliton/130_q_g47_path_d_engine_cross_validation_first_pass.md):55-60 | `MasterEquationFDTD` (scalar EMT) | Smaller-scope cross-validation at N=24 | $A_{op}$ = 0.324 sub-saturation; breathing OK | Operating-point characterization |
| [`research/_archive/L3_electron_soliton/131_q_g47_path_d_full_two_engine_cross_validation_pass.md`](research/_archive/L3_electron_soliton/131_q_g47_path_d_full_two_engine_cross_validation_pass.md):50-66 | `MasterEquationFDTD` v14 | Full N=32, 5000-step canonical scope | $\Lambda_{total}$ = 102.78 (vs target 137.036; 50% gap) | The result THIS workstream is trying to explain |
| [`research/2026-05-18_q-g47-interpretation-g-prereg.md`](research/2026-05-18_q-g47-interpretation-g-prereg.md) | (this session) | Pre-registration for radial-projection geometry check | n/a — prereg only | Workstream antecedent |
| [`research/2026-05-18_q-g47-interpretation-g-result.md`](research/2026-05-18_q-g47-interpretation-g-result.md) | `MasterEquationFDTD` v14 | Radial Riemann-invariant + Lissajous PCA + FFT multi-mode | **Outcome A** — R/r = 13.29 vs target 2.618 (407% deviation) | THIS workstream's precipitating finding |

### 5.5 Operators (universal-operators canon)

The ABCD eigensolver invokes (implicitly or explicitly) these Universal Operators:

| Operator | Role in ABCD workstream | Canonical leaf |
|---|---|---|
| Op6 (S₁₁ minimization) | The Golden Torus geometry IS the S₁₁-minimum of the trefoil; the ABCD eigenmode is the bound state at this minimum | Vol 1 Ch 6, eq_universal_operators.tex |
| Op7 (90° crossing loss = $1/(2\pi^2)$) | Hopf crossing loss at K4 junctions; modulates the chiral shunt Y_C value | constants.py:231 (`N_Y_LOSS_90`) |
| Op14 (saturation + clock modulation) | At sub-saturation operating point, $c_{eff}$ shifts; ABCD's $\gamma\ell$ acquires a real part | Two canonical leaves (above) |
| Op17 (matched-LC coupling) | Per-cycle coupling efficiency $\epsilon_{det} = 4\pi/N^2$ at TIR boundary — referenced in ABCD adjudication if cavity Q-factor extraction is needed | `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md` |
| Op21 (multi-mode generalization) | Each mode with $\ell$ wavelengths releases $1/\ell$ per cycle → $Q = \ell$ per mode; ABCD eigenvalues' $|1 - \lambda|$ gives $1/Q$ per mode directly | `theorem-3-1-q-factor.md:99` + `src/scripts/vol_1_foundations/op21_multimode_derivation.py` |

### 5.6 External references (RF/microwave EE)

For canonical ABCD-matrix theory beyond what `transmission_line.py` covers:

- **D. M. Pozar, *Microwave Engineering*** (4th ed.), Ch 4 §4.4: ABCD matrices and cascade composition
- **R. E. Collin, *Foundations for Microwave Engineering*** (2nd ed.), Ch 5 §5.5: Two-port network parameters
- For closed-cavity periodic-boundary eigenvalue analysis: any photonic-crystal text (e.g., Joannopoulos, *Photonic Crystals*) §"Bloch modes" treats the same algebraic structure.

The eigenvalue interpretation ($|\lambda| = 1$ ↔ sustained mode) is standard photonic-crystal band-structure analysis applied to a closed loop instead of an extended lattice.

## 6. 5-phase implementation plan

### Phase 1 — Verify `transmission_line.py` coverage + extend if needed (~30 min)

**Goal**: confirm that `abcd_segment`, `abcd_shunt`, `abcd_cascade` cover what the K4 cavity needs.

**Steps**:
1. Read [`src/ave/solvers/transmission_line.py`](src/ave/solvers/transmission_line.py) lines 1-300 (NumPy backend; JAX backend optional for now)
2. Check if `abcd_shunt(Y)` admits complex Y (it should — already declared `complex` per line 76 signature) — needed for chirality phase encoding
3. Check if cascade composition supports the periodic-boundary closure needed for the round-trip matrix (likely needs a new small function `abcd_round_trip_eigenvalues(matrices)` that computes `np.linalg.eig(reduce(matmul, matrices))`)
4. **If extension needed**: add `abcd_round_trip_eigenvalues(matrices, normalization='energy')` to `transmission_line.py` with canonical docstring + verify-discipline-block. Test on simple LC resonator (1 segment, periodic BC → eigenvalues should be $\pm 1$ for half-wave resonance).

**Skill discipline**:
- `ave-canonical-source` → already-canonical infrastructure; just verify imports
- `ave-driver-script-honesty` → if new function added, must pass all 4 discriminators

**Exit criterion**: `transmission_line.py` either covers all needs OR has a new function `abcd_round_trip_eigenvalues` that's been tested on a simple known case.

### Phase 2 — K4 cell ABCD composition with chirality (~45 min)

**Goal**: build a `k4_cell_abcd(Z_c, gamma_l, phi_chiral)` function that returns the ABCD matrix for one K4 cell traversed in a specific direction, incorporating the chiral phase shift from asymmetric torque.

**Steps**:
1. Read [`src/ave/topological/k4_cosserat_coupling.py`](src/ave/topological/k4_cosserat_coupling.py) — understand existing chiral-coupling implementation
2. Choose chirality encoding (approach (a) phase-shift junction OR (b) chiral shunt admittance per §3.3) — recommend (b) first cut
3. For approach (b): `k4_cell_abcd(Z_c, gamma_l, Y_C_chiral)` = `abcd_cascade([abcd_segment(Z_c, gamma_l), abcd_shunt(Y_C_chiral), abcd_segment(Z_c, gamma_l)])` (two half-segments + shunt at junction)
4. The chiral admittance value: $Y_C = j \cdot \tan(\phi_C)$ where $\phi_C$ is the per-junction Cosserat phase shift. Derive $\phi_C$ from Op14 canonical (consult `op14-cross-sector-trading.md` + canonical Cosserat coupling formula in `k4_cosserat_coupling.py`).
5. Validate: compose 2 K4 cells with $\phi_C = 0$ (no chirality) → should match plain cascade of 2 segments. With $\phi_C \neq 0$ → reciprocity (AD - BC = 1) should hold for lossless case.

**Skill discipline**:
- `substrate-native-check` → checkpoint 1 (V-sector + Cos-sector cross-coupling), checkpoint 6 (reactance pair tracking through chiral junction)
- `ave-canonical-leaf-pull` → Q-factor canon + matched-LC canon (already enumerated in §5.5)

**Exit criterion**: `k4_cell_abcd` function with chirality encoding; validated on 2-cell reciprocity test.

### Phase 3 — Cavity round-trip composition for (2,3) trefoil (~30 min)

**Goal**: build $M_{RT}$ for the canonical electron cavity by composing K4 cells along the (2,3) trefoil path at Golden Torus radii.

**Steps**:
1. Discretize the (2,3) trefoil path on the K4 lattice: at $R = \varphi/2 \cdot \ell_{node}^{-1} \approx 0.81$ major radius and $r = (\varphi-1)/2 \cdot \ell_{node}^{-1} \approx 0.31$ minor radius (natural units), count the number of K4 cells encountered in one trefoil traversal. NOTE: $R, r < \ell_{node}$ means the trefoil is sub-lattice-resolution; ABCD bond-segment lengths $\gamma\ell$ should reflect this via $\beta\ell = (2\pi/\lambda) \cdot \ell$ where $\lambda$ is the wavelength on the trefoil path.
2. **Sub-lattice question** (NEW question this raises — surface to Grant): the Clifford-torus radii in natural units are LESS THAN $\ell_{node}$, so the trefoil is sub-lattice. How does ABCD discretization handle sub-lattice? Two options:
   - (i) Use ABCD in the continuum-limit sense (segment length $\gamma\ell$ as a free parameter, not tied to $\ell_{node}$ discretization)
   - (ii) Use K4-TLM scatter-connect rules at $\ell_{node}$ granularity but extract eigenmode at sub-lattice scale via Bloch-mode analysis
3. **Reasonable call** (autonomous mode): option (i) — treat the trefoil path as a 1D parametric curve with continuum ABCD; the K4 cells along the path are abstract junctions, not lattice-resolved. This matches how Pozar/Collin handle resonator analysis.
4. Build $M_{RT}$: 16 segments (per §4.1 estimation) × `k4_cell_abcd` calls along the trefoil; close with periodic BC (the round-trip IS the periodic closure).
5. Cross-check: at Golden Torus geometry, $M_{RT}$ should have dominant eigenvalue $|\lambda| = 1 - \alpha = 1 - 1/137 \approx 0.9927$ per Theorem 3.1' canonical "$1/Q = \alpha$".

**Skill discipline**:
- `phase-space-coordinate-check` → the eigenmode IS the (V_inc, V_ref) phase-space quantity; confirm this is what we're measuring
- `pre-test-physics-check` → surface the sub-lattice discretization question to Grant; make reasonable call per autonomous mode

**Exit criterion**: $M_{RT}$ matrix constructed for canonical Golden Torus parameters; dominant eigenvalue magnitude approximately $1 - \alpha$.

### Phase 4 — Eigensolve + (R, r) extraction (~30 min)

**Goal**: compute $(R_{meas}, r_{meas})$ from the dominant eigenvector and compare to canonical targets.

**Steps**:
1. `evals, evecs = np.linalg.eig(M_RT)`
2. Find dominant eigenvalue (largest $|\lambda|$); extract eigenvector $\psi = (V, I)^T$
3. Apply energy normalization: $|V|^2 + |Z_0 I|^2 = 1$
4. Compute $V_{inc} = (V + Z_0 I)/2$, $V_{ref} = (V - Z_0 I)/2$
5. $R_{meas} = |V_{inc}|$, $r_{meas} = |V_{ref}|$
6. Compare to canonical: `from ave.core.constants import R_GOLDEN_TORUS, R_GOLDEN_TORUS_MINOR, RR_GOLDEN_TORUS, PHI` — adjudicate POSITIVE / NEGATIVE / AMBIGUOUS per §2 criteria

**Skill discipline**:
- `ave-canonical-source` → canonical imports + verify-block at script startup
- `consistency-vs-emergence` → confirm this is INTRA-FRAMEWORK CONSISTENCY CHECK (not emergence); no CODATA inputs, no α-encoded inputs

**Exit criterion**: $(R_{meas}, r_{meas}, R\cdot r_{meas}, R/r_{meas})$ printed to stdout with canonical-target comparison + outcome classification.

### Phase 5 — Adjudication + walk-back propagation (~45 min)

**Goal**: based on Phase 4 outcome, execute walk-back per `ave-walk-back` skill across all affected leaves.

**Steps** (outcome-conditional):

**If POSITIVE**:
1. Update foreword line 106 to REMOVE Interpretation G flag; replace with "geometry verified at ABCD eigensolver"
2. Update BRANCH STATE weak-spot #2 (2b) to "RESOLVED — geometry verification PASS"
3. Update Theorem 3.1' leaf §49-63 to ADD §63b paragraph: "Precondition: this identification requires the bound state to be at Golden Torus geometry. ABCD eigensolver at [commit SHA] confirms this realization at 2026-05-18-... See `research/2026-05-18_abcd-...result.md`."
4. Mark Q-G47 K4-TLM A5 chain as RESOLVED in foreword α-derivation chains list (chain A5 status changes from "attempted Class 4 via Λ_total" to "verified via ABCD eigensolver geometry")
5. Initiate Interpretation F (UV running) workstream as next priority for the 50% Λ_total gap

**If NEGATIVE**:
1. Update foreword line 106 to STRONGEN Interpretation G flag: "geometry NOT verified by ABCD eigensolver; canonical electron Golden Torus is theoretical-only"
2. Update Theorem 3.1' leaf §49-63 to ADD §63b paragraph: "Precondition: this identification REQUIRES Golden Torus geometry. ABCD eigensolver at [commit SHA] found realization FAILS by [N]%. The bridge is UNVERIFIED for the canonical electron at v14 operating point."
3. Walk-back propagates to Vol 1 Ch 8 §3 (α derivation): explicitly note the geometry-realization gap
4. Walk-back propagates to L5 axiom-status A-001 / Q-G47 row: mark as STRUCTURALLY-OPEN, not just numerically-open
5. Promote the geometry-realization question to a Class-A peer-review priority

**If AMBIGUOUS** (no sustained eigenmode):
1. Re-examine canonical electron-cavity geometry assumption itself (Vol 1 Ch 8 trefoil-at-dielectric-ropelength)
2. Possible explanation: the (2,3) trefoil is the right topology for the K4 bonded electron AT lattice-resolution, NOT at sub-lattice continuum scale; the ABCD framework's continuum limit may not apply
3. Cascade follow-up: rebuild with K4-TLM-discrete scatter+connect at $\ell_{node}$ granularity (NOT continuum ABCD); this becomes a NEW workstream

**Skill discipline**:
- `ave-walk-back` → MANDATORY for any of the 3 outcome branches; the propagation checklist for matrix-row adjudications + leaf updates per skill body
- `ave-evidence-framing-discipline` → tighten all "verified" / "matches" / "within tolerance" language to actual numerical bounds; no overclaim

**Exit criterion**: walk-back commits land per `ave-walk-back` checklist; foreword + Theorem 3.1' leaf + BRANCH STATE + L5 status all consistent.

## 7. Skill-selection plan (per `feedback_skill_selection_planning.md` rule)

**Upfront formal Skill invocations** (write 60-sec plan BEFORE starting any phase):

| Skill | Phase | Trigger reason |
|---|---|---|
| `ave-prereg` | Phase 0 (start) | Corpus-grep across 10 repos for any prior ABCD-eigensolver work + verify `transmission_line.py` is the only canonical ABCD source |
| `ave-canonical-leaf-pull` | Phase 1 | Q-factor canon + matched-LC canon + Op14/Op17/Op21 canon enumeration before ABCD library extension |
| `substrate-native-check` | Phase 2 | NEW solver code with V↔Cos cross-coupling — full 7-checkpoint walk |
| `pre-test-physics-check` | Phase 3 | Sub-lattice discretization question — surface to Grant before locking in continuum-vs-discrete choice |
| `phase-space-coordinate-check` | Phase 4 | Eigenmode IS the phase-space measurement; confirm coordinate system matches corpus claim |
| `ave-canonical-source` | Phase 4 | Final solver imports + verify-block at startup |
| `ave-driver-script-honesty` | Phase 4 | New driver script; 4-discriminator check |
| `consistency-vs-emergence` | Phase 4 | Classify result (INTRA-FRAMEWORK CONSISTENCY CHECK, not emergence) |
| `verify-before-cite` | Phase 5 | Walk-back citations to Theorem 3.1', foreword line 106, BRANCH STATE, L5 status |
| `ave-walk-back` | Phase 5 | MANDATORY for outcome-conditional propagation |

**Implicitly applied** (logged):
- `ave-evidence-framing-discipline` throughout — tighten language at every print/docstring/commit-message moment
- `ave-newly-created-skill-self-audit` — N/A (no new skill being created)
- `ave-canonical-source` invoke-side audit (Discriminator 5 of `ave-driver-script-honesty`) — if invoking existing scripts during validation

**Delegated to sub-agents**:
- `ave-corpus-grep` agent in Phase 0 (corpus inventory; protect context window for substantive work)
- `ave-auditor` agent in Phase 5 (independent second-pass audit of the walk-back before commit)

## 8. Adjudication framework (concrete numerical bounds)

| Outcome | $R$ deviation | $r$ deviation | $R/r$ deviation | Multi-mode | Eigenvalue magnitude |
|---|---|---|---|---|---|
| **POSITIVE** | <5% from $\varphi/2$ | <5% from $(\varphi-1)/2$ | <2% from $\varphi^2$ | Yes (single dominant + harmonics) | $0.99 < \|\lambda\| < 1.0$ |
| **NEGATIVE** | >10% | >10% | >5% | (any) | (any with $\|\lambda\| > 0.9$) |
| **AMBIGUOUS** | (any) | (any) | (any) | (any) | No eigenvalue with $\|\lambda\| > 0.9$ |
| **POSITIVE-WITH-CAVEAT** | <10% | <10% | <5% | Single mode only (no harmonics) | $0.99 < \|\lambda\| < 1.0$ but only one eigenmode | Geometry realized but mode-count <3 — Op21 multi-mode generalization may not apply at this scope |

**Reasonable-call defaults for autonomous mode** (per prereg discipline):
- Bayesian prior post-Grant intervention + post-doc-78 reframing: NEGATIVE ~50%, POSITIVE ~30%, AMBIGUOUS ~15%, POSITIVE-WITH-CAVEAT ~5%
- This is more optimistic than the FDTD-result distribution because ABCD eigensolve bypasses the persistence problem

## 9. Walk-back propagation list (concrete files per outcome)

### POSITIVE outcome walk-back (per `ave-walk-back` skill):

1. [`manuscript/ave-kb/common/foreword.md`](manuscript/ave-kb/common/foreword.md) line 106 — remove Interp G flag; replace with verification citation
2. [`research/BRANCH_STATE_2026-05-18_analysis-divergence-test-substrate-map.md`](research/BRANCH_STATE_2026-05-18_analysis-divergence-test-substrate-map.md) §weak-spots #2 (2b) — mark RESOLVED
3. [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) §49-63 — add §63b precondition paragraph
4. [`research/_archive/L5/axiom_derivation_status.md`](research/_archive/L5/axiom_derivation_status.md) Q-G47 row — mark K4-TLM A5 chain VERIFIED
5. [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) §3 — cite ABCD eigensolver as verification
6. [`research/2026-05-18_k4-tlm-a5-alternative-interpretations.md`](research/2026-05-18_k4-tlm-a5-alternative-interpretations.md) §3.G — mark COMPLETED; promote Interp F as next priority

### NEGATIVE outcome walk-back:

1-3 (same files as POSITIVE, opposite framing)
4. [`research/_archive/L5/axiom_derivation_status.md`](research/_archive/L5/axiom_derivation_status.md) Q-G47 row — mark STRUCTURALLY-OPEN (stronger than NUMERICALLY-OPEN)
5. Vol 1 Ch 8 §3 — add explicit geometry-realization gap acknowledgment
6. Promote to peer-review priority #1 (replaces C1-BH-RING as top peer-review item)
7. Foreword "what could break the framework" section — add geometry-realization gap as Class-A concern

### AMBIGUOUS outcome walk-back:

All NEGATIVE actions PLUS:
8. Open a NEW research-doc thread: `research/2026-05-XX_continuum-vs-lattice-electron-cavity.md` — the framework needs to decide whether the canonical electron is sub-lattice continuum (where ABCD applies) or lattice-discrete (where K4-TLM scatter+connect applies). This question may displace several months of corpus work.

## 10. Cost-benefit framing

| Cost | Estimate |
|---|---|
| Phase 1-4 implementation | ~2-3 hours |
| Phase 5 walk-back | ~30-60 min (POSITIVE/NEGATIVE), up to ~2 hr (AMBIGUOUS with new workstream) |
| Corpus-grep + skill discipline overhead | ~30 min |
| **Total** | **3-4 hours typical, 5-6 hours AMBIGUOUS-case** |

| Benefit | Why |
|---|---|
| Settles Interpretation G DEFINITIVELY | Either outcome resolves the 50% $\Lambda_{total}$ gap framing — POSITIVE clears geometry, NEGATIVE narrows to genuine structural gap |
| Replaces 2 failed FDTD methodologies | Bypasses persistence problem (doc 78) + post-hoc projection (this session) + chirality absence (this session) |
| Direct path to Vol 1 Ch 8 verification | Either reinforces the canonical α derivation OR surfaces a load-bearing gap that's been hidden by methodology issues |
| Multi-session unblocks | Foreword promotion-precision pass, BRANCH STATE resolution, L5 status update all unblock |
| ABCD library extension | Phase 1 work generalizes — future Q-G47-class problems (e.g., proton cinquefoil, muon Cosserat-doubled) can reuse the eigensolver infrastructure |

| Risk | Mitigation |
|---|---|
| Sub-lattice question (§3 + Phase 3) may produce AMBIGUOUS outcome | Phase 5 has explicit handling; new workstream is scoped not surprise |
| Chirality encoding (approach (a) vs (b)) may not adequately capture K4 asymmetry | Validate against doc 78's K4-TLM result (R/r per-bond values 2.16-5.72 should match in the appropriate limit) |
| Phase 1 may find `transmission_line.py` covers eigenmode case → no extension needed | This is GOOD — drops scope to ~2 hr total |

## 11. Pre-flight checklist (for fresh agent picking this up)

Before starting Phase 1:

- [ ] Read [`research/2026-05-18_q-g47-interpretation-g-result.md`](research/2026-05-18_q-g47-interpretation-g-result.md) end-to-end (precipitating context)
- [ ] Read this handoff doc end-to-end
- [ ] Read [`research/2026-05-18_k4-tlm-a5-alternative-interpretations.md`](research/2026-05-18_k4-tlm-a5-alternative-interpretations.md) for the broader interpretation enumeration this fits into
- [ ] Read [`research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md`](research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md) for the prior K4-TLM cross-validation Mode III result + persistence-violation caveat
- [ ] Skim [`src/ave/solvers/transmission_line.py`](src/ave/solvers/transmission_line.py) lines 1-300 (NumPy ABCD library)
- [ ] Skim [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) lines 49-100
- [ ] Verify on branch `analysis/c8-baryon-ladder-pdg-anchor` OR check whether a new feature branch is appropriate
- [ ] Confirm working tree clean before starting
- [ ] Write 60-sec skill-selection plan upfront per §7 (per `feedback_skill_selection_planning.md` rule)

If all of the above is done, proceed with Phase 1.

## 12. Provenance + audit trail

**This handoff drafted in**: 2026-05-18 night session, after Interpretation G FDTD test landed with Outcome A; precipitated by Grant intervention "need an a b c d solver?" + doc-78-reframing finding from `verify-before-cite` grep.

**Skills fired in drafting this handoff** (per `feedback_skill_selection_planning.md`):
- `ave-prereg` corpus-grep already-completed (Phase 0 of this workstream is essentially the corpus-grep done at session start)
- `verify-before-cite` for all canonical-leaf citations (Theorem 3.1' §49-63 verified verbatim; doc 78/130/131 verified verbatim; transmission_line.py existence verified via `head -80` + function-inventory grep)

**Citations in this handoff verified via** explicit Bash commands documented in `_session_log/2026-05-18-interp-g-handoff.log` (will be added by next-session agent picking this up). Until then, the citations above can be re-verified via:

```bash
sed -n '49,75p' /Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
head -80 /Users/grantlindblom/AVE-staging/AVE-Core/src/ave/solvers/transmission_line.py
grep -nE "^(def |class )" /Users/grantlindblom/AVE-staging/AVE-Core/src/ave/solvers/transmission_line.py | head -30
```

**Pure-AVE-corpus rule compliance** (per memory entry): all content above is pure physics — no external-context references, all motivations cast in substrate-physics terms.
