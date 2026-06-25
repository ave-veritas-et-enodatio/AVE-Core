# Unified fully-dynamic AVE engine — P0 design note (regime-dispatch facade + single-grid bet)

**Branch:** `engine/p0-unified-dynamic` (off `origin/main` d7626508). BRANCH-ONLY.
**Scope (Grant-ratified):** P0 = scaffold the **regime-dispatch facade** + **validate-on-known**.
**Grid (Grant-ratified high-leverage bet):** SINGLE native K4. 6 DOF/node + the A1
dilatation scalar as a NODE-ATTACHED field on the SAME K4 graph.

This note is the skeleton-first first commit. The facade is built incrementally
after it (one core wired per commit), then the L0/L1 acceptance suite is run
THROUGH the facade and the closed-box energy gate is live-fired.

---

## 0. substrate-native-check walk (done BEFORE any facade code, Operating Principle 1)

The structural-null stencil lens (MEMORY: `feedback_structural_null_needs_stencil_lens`)
says: an operator adjudicating substrate physics MUST be native-K4, not
Cartesian-on-parity-mask, or it validates a disabled-flag discretization bug as
physics. Walked here for the single-grid 6-DOF rep:

* **K4 / stencil.** Every spatial operator the facade dispatches to is already
  native-K4:
  - L0/L1 medium: `chiral_lattice.LatticeNet` = the periodic **srs** net,
    degree **z=3** (do NOT flip 3→4), TLM scatter+connect (`scalar_tlm_step`,
    `vector_tlm_step`). The CONNECT map is a port permutation ⇒ orthogonal ⇒
    energy exactly conserved (`chiral_lattice_dynamics.connect_is_permutation`).
  - A1 cage + ω winding: `native_cage_imex.build_grad_div_periodic` assembles the
    sparse Grad/Div from `TETRA_OFFSETS = ((1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1))`
    — the 4 diamond-K4 tetrahedral diagonals. `L_D = Div·diag(D)·Grad` is the
    native divergence-form diamond Laplacian. The Cartesian 7-pt Laplacian is
    FORBIDDEN (HR1) and never assembled. The diamond A+B sublattice (parity mask
    `(i%2==j%2==k%2)`) is the ALIVE set — this is the genuine K4 diamond graph,
    not a Cartesian grid wearing a mask: the stencil is the tetrahedral
    gradient, the mask is the diamond's two-sublattice structure.
* **Cosserat / sector.** Two ORTHOGONAL grades, never a shared `(V_inc,V_ref)`
  phasor (`master-equation.md:20`; the genesis-24 double-count caution):
  - 3 translation `u` ↔ E/ε₀ (the A1 dilatation MASS-3 "scalar" lives here as
    the longitudinal projection; the 2 transverse are the photon),
  - 3 Cosserat micro-rotation `ω` ↔ B/μ₀ (the (2,3) winding = CHARGE/helicity).
  The A1 dilatation scalar is a NODE-ATTACHED field on the SAME K4 graph (the
  single-grid bet) — NOT a second grid.
* **Op14 / saturation.** The cage wall = a μ-load SHORT (Z_core→0, Γ→−1, settled
  PR#260). The saturation kernel is the α-clean `S(A)=(1−A²)^p` (p=½ primary).
  D = 1/S folded ONCE (single-1/S). For P0 (linear, S=1) the saturation is
  DORMANT — the facade carries it but does not exercise it.
* **phase-space vs real-space.** P0 validate-on-known observables are all
  real-space / spectral (energy drift, dispersion ω(k), network velocity, Q via
  ring-down / eigenframe, winding integer Link(∂Ω,F)). NO phase-space φ²/Clifford-
  torus claim is at issue at P0 (A46 satisfied: the corpus claims being
  reproduced are themselves real-space/spectral).

## 1. regime / phase-state declaration (ave-regime-phase-state-check)

* **MODE:** all-6-DOF carried (3 translation + 3 micro-rotation) + the A1
  node-field. P0 exercises the LINEAR free modes (transverse photon present;
  bulk/Cosserat presence is the P1 flip — see §6).
* **REGIME:** LINEAR, **S=1** (A≪1 ⇒ cold vacuum). The c_eff(V) saturation
  curve is carried keyed-to-channel but dormant.
* **PHASE-STATE:** cold vacuum / lossless reactive. Closed box (no PML, no
  damping) for the energy gate. A null where an effect cannot exist (e.g. the
  √S shear constitutive at S=1) is an ARTIFACT not a falsification — reported,
  not forced (inherits the L1-multiwave PARTIAL/FINDING discipline).
* **velocity-channel keying (carry BOTH, do NOT pin one exponent):**
  - c_EM PHASE = c₀/S (→∞ as A→1; the α-speed channel),
  - c_shear GROUP/mass = c₀·√S = c₀·(1−A²)^(1/4) (→0 as A→1; the matter clock).
  The c_shear def-lock is ALREADY landed (`test_l1_multiwave.py:67-70`) and is
  INHERITED, not re-flagged.

## 2. single-grid 6-DOF/node state representation

State on the single native K4 graph (N nodes, the srs/diamond node set):

| grade | symbol | DOF/node | EM map | corpus anchor |
|-------|--------|----------|--------|---------------|
| translation | `u` (3-vec) | 3 | E/ε₀ | Axiom-1 (3 translational) |
| ↳ transverse | `u_⊥` (2) | (2 of 3) | photon | EM-transverse, c_EM=c₀/S |
| ↳ longitudinal | `u_∥` (1) | (1 of 3) | A1 dilatation | the "3"/mass precursor |
| micro-rotation | `ω` (3-vec) | 3 | B/μ₀ | Cosserat (2,3) winding = charge |
| **A1 node-field** | `a_A1` (scalar) | +1 | bulk dilatation | **the single-grid bet** |

THE BET: the A1 bulk-dilatation scalar `a_A1` is carried as a **node-attached
field on the SAME K4 graph** as `ω` — NOT on a second Cartesian grid. The A1
cage operator (`native_cage_imex`, native TETRA_OFFSETS) and the ω
micro-rotation both live on the native diamond-K4 node set, so the A1 scalar
rides the same node set as a per-node attribute rather than needing an
inter-grid interpolation port.

### Single-grid VERDICT (P0): LOAD-BEARING HALF PROVEN; full unification deferred to P1 = the D1 decision

**Proven in P0 (the load-bearing half).** The A1 dilatation scalar node-field
AND the ω Cosserat micro-rotation **coexist on ONE diamond-K4 node set** with the
joint closed-box energy gate GREEN end-to-end (`coupled_cage_winding`, 60 coupled
steps, joint **|dH/H| = 1.18e-11**) and the (2,3) winding integer conserved on
the shared grid. That is the part the bet most needed: the A1 scalar does NOT
require a second grid relative to ω — it is a genuine per-node attribute on the
diamond-K4 graph the cage/winding sector uses.

**NOT proven in P0 (deferred to P1).** Two distinct native-K4-**family** carriers
still remain in the facade (see the `SingleGridState` docstring):
* the **srs z=3** net carries the FREE transverse photon modes (`chiral_lattice`,
  TLM port fields), and
* the **diamond z=4** N³ node array (TETRA_OFFSETS) carries the A1 node-field +
  the ω micro-rotation (`native_cage_imex` / `coupled_cage_winding`).

Both are native-K4-family, but they are NOT the same literal node list, and P0
does NOT collapse them onto one. Unifying these two carriers onto ONE node list
is the **P1** task, and that unification **IS the D1 connectivity decision**
(**chiral z=3 srs** for the free-mode carrier **vs achiral z=4 diamond** for the
A1/ω carrier). The two-grid bridge (Stage-3 reconciliation milestone,
`_spine.shared_grid_descriptor` "collapse_milestone") is therefore **NOT yet
dissolved** — its load-bearing half (A1↔ω on one node set) is dissolved; the
remaining srs↔diamond carrier reconciliation is the open P1/D1 work. This is the
`srs z=3 vs diamond z=4` node-set mismatch the §0 walk flagged as the wall that
must be reported precisely, NOT forced — and it is reported here, not forced.

## 3. regime-dispatch facade API

`ave.facade.unified_engine` — the MEDIUM-scaffold (validate-on-known), NOT a
self-formation search. The falsified bulk self-trap (S3 DISPERSE / #415 / #59)
is CLOSED-NEGATIVE; the self-formation slot is BARRED (the facade does not
re-run it).

```
class Regime(Enum):
    LINEAR_FREE      # S=1, all free modes (P0)
    SATURATED_CAGE   # A1 cage (native_cage_imex), Op14 active (P1+)
    COUPLED_WINDING  # A1↔ω coupled (coupled_cage_winding) (P1+)

class UnifiedEngine:
    def __init__(self, cfg): ...                  # dispatch on cfg.regime
    def free_modes(self) -> MediumHandle          # → chiral_lattice srs net
    def a1_cage(self) -> NativeCageIMEX            # → native_cage_imex (single-grid A1)
    def coupled(self) -> CoupledCageWinding        # → coupled_cage_winding
    def winding_reader(self) -> callable           # → charge_quantization.compute_Q_link
    def saturation_kernel(self, A)                 # → graded_vacuum_network (α-clean)
    def energy_gate(self) -> dict                  # closed-box |dH/H| (RUNG-0)
    def velocity_channels(self, A) -> dict         # BOTH c_EM, c_shear keyed to channel
```

The facade is a thin DISPATCH + WIRING layer. It REUSES the certified cores
verbatim (Rule-14 anti-rebuild) — it does NOT reimplement any stencil, stepper,
eigensolver, kernel, or winding reader.

## 4. reuse map (Rule-14 anti-rebuild — wire, do NOT reimplement)

| facade role | certified core (wired verbatim) | what it provides |
|-------------|----------------------------------|------------------|
| native K4 stencil + unitary stepper + A1↔ω port | `solvers.coupled_cage_winding` | Crank–Nicolson/Cayley unitary; separately-conserved ω; Hermitian A1↔ω H_couple |
| native sparse Grad/Div + IMEX A1 cage | `solvers.native_cage_imex` | `build_grad_div_periodic`/`assemble_L_D`; IMEX-implicit stiff 1/S; energy-consistent Newmark radiative port; `energy_conservation_gate` |
| L0 chiral medium + scatter-connect TLM | `core.chiral_lattice` + `chiral_lattice_vector` + `chiral_lattice_dynamics` | srs z=3 net; scalar/vector TLM; energy drift; dispersion/network velocity; isotropy |
| integer winding reader | `topological.charge_quantization` | `compute_Q_link` Link(∂Ω,F) ∈ ℤ; `seed_pq_winding` |
| α-clean (1−A²) kernel | `solvers.graded_vacuum_network` | `saturation_kernel`/`stiffness_profile`; lossless eigenframe Q=∞ |

EXCLUDED (do NOT carry): `master_equation_fdtd` (Cartesian-grid artifact),
`fdtd_3d` (μ-on-static-|B| bug).

## 5. honesty guards (carried in the facade)

* **α-clean throughout.** κ̃=6/5 (`_winding_host.winding_kappa_tilde`), the
  import-guard triad (ALPHA/Q_TANK/ELECTRON/RHO_BULK/V_SNAP/KAPPA_CHIRAL_ELECTRON
  absent). NOT the α-baked `cosserat_field_3d` readout path. The facade re-asserts
  the triad at construction.
* **MEDIUM-scaffold, NOT self-formation.** Self-formation slot BARRED.
* **c_shear def-lock INHERITED** (`test_l1_multiwave.py:67-70`), not re-flagged.
* **velocity channels keyed to channel** — BOTH c_EM (phase, c₀/S) and c_shear
  (group/mass, c₀·√S) carried; neither exponent pinned.

## 6. P0 acceptance gate (validate-on-known) + what P1 needs

* **RUNG-0:** energy/unitary-scatter, Z₀=√(μ₀/ε₀)=376.7Ω, isotropy.
* **RUNG-1:** L0 axiom-compliance + L1 free modes.
* Both reproduced GREEN **through the facade**; every existing green
  `engine_acceptance` row STAYS green; closed-box energy gate LIVE |dH/H|<1e-8
  in the lossless limit.
* **Single-grid verdict (load-bearing half only):** A1 node-field + ω coexist on
  ONE diamond-K4 node set (joint |dH/H|=1.18e-11, winding integer conserved).
  Full srs-z3↔diamond-z4 carrier unification is NOT done — deferred to P1 = the
  D1 decision (see §2 verdict). Do NOT headline this as "the two-grid bridge is
  dissolved" — only its load-bearing half is.
* **GATE-LIVENESS controls (through the facade):** the closed-box energy gate is
  proven to be a LIVE discriminator — driving the facade's energy-gate core
  (`a1_cage()`) with the rejected backward-Euler integrator TRIPS the gate
  (bleed=1.000 ≫ the 1e-8 gate, GX3-facade), and the radiative port is PASSIVE
  through the facade (Hmax/H0=1.000000, GX5-facade). Rule-14: GX3/GX5 logic
  reused verbatim from `test_stage2_native_cage_imex.py`.

**P1 next:** (1) the D1 connectivity decision — collapse the srs z=3 free-mode
carrier and the diamond z=4 A1/ω carrier onto ONE literal node list (chiral z=3
srs vs achiral z=4 diamond); (2) linear all-modes dynamic; flip the bulk/Cosserat
ABSENCE-findings (`test_l1_multiwave` T1.7/T1.8 MEDIUM-EXTENSION) to PRESENT by
routing the longitudinal `u_∥` + the ω micro-rotation field through the
single-grid A1 node-field + the `coupled_cage_winding` ω DOF — i.e. give the srs
medium the grades it currently lacks, on the unified K4 graph P1 establishes.
