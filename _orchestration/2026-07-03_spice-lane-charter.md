# SPICE-lane charter — deep-dive feasibility

**Date:** 2026-07-03
**Commissioned:** Grant, 2026-07-03. Planning arc — deliverable is this
charter + a feasibility note, NOT production code.
**Branch:** `analysis/spice-lane-charter` (off `origin/main`, HEAD `a0508e50`)
**Evidence note (file:line):** [`research/2026-07-03_spice-lane-feasibility_note.md`](../research/2026-07-03_spice-lane-feasibility_note.md)
**Pilot:** [`src/scripts/vol_4_engineering/spice_lane_pilot_poisson.py`](../src/scripts/vol_4_engineering/spice_lane_pilot_poisson.py)

## The vision being chartered (Grant's two-layer picture)

ONE lattice, two analyses. The SPICE `.OP`/`.AC`/`.TRAN` pattern is the
reference implementation of *"the Ax4 saturation/limits calculation (the
bias map, S(A) per node) sets the L/C values of the wave-carrying coupled
network."* The **SPICE lane** owns the network-equation truth + the Ax4
constitutive limits; the **spatial srs engine** owns geometry/topology
(windings). The division of labor is settled by commission; this charter
designs the SPICE half and its coupling to the engine half.

---

## 1. Inventory (verify-before-cite — full table in the feasibility note §1)

**The reframe:** the lane is NOT greenfield, and its "SPICE" has never run
in a SPICE engine. What exists:

- A **netlist compiler** (`spice_netlist_compiler.py`, 296 lines) that
  *emits* `.cir` files, single-sourced from `ave.core.constants` (:24) —
  but contains **no ngspice invocation anywhere**. Emit-only.
- A **canonical `.lib`** (`ave_vacuum_cell.lib`, 169 lines) with 5 valid
  ngspice-syntax behavioral subcircuits — **never parsed by ngspice** (only
  by tests that skip when ngspice is absent).
- Two **Python-native solvers** wearing the "SPICE" label:
  `spice_transient.py` (explicit-Euler, numpy/JAX) and `spice_cvr_loop.py`
  (L0/L1/L2 ODE ladder, self-reporting `"spice_executed": False` at :303).
- A **compiler demo** that "verifies" via numpy ABCD matrices, not ngspice.
- 5 **KB netlist leaves** (ch14-18) + the App-6 LaTeX manual + vol9
  device-circuit-models §1/§6, all describing netlist *forms*.

**Run-state:** `pytest` on the two SPICE test files → **14 passed, 5
skipped** (all 5 skips ngspice-gated). **No SPICE engine has ever validated
an AVE netlist.** The lane's actual computational content is Python; "SPICE"
is a branding pattern on it.

**clm- IDs riding on the leaves:** clm-vjv4zf, clm-c54kdd, clm-9sujp8,
clm-cbwd77, clm-kezk9z. All describe forms; none asserts a run result.

**Two flag-don't-fix inconsistencies found (do NOT resolve without Grant):**

- **FLAG-1 (value drift):** V_YIELD = 43651.85 (constants.py:464) vs
  43651.9 (`.lib` hardcoded default) vs **43653.7** (ch18 KB spec + App-6
  manual). App-6:167 falsely claims "No constants are hardcoded in the .lib."
- **FLAG-2 (varactor sign):** canonical `.lib:63` uses `C_eff = C0/S(V)`
  (diverges at yield); ch15+ch17 KB leaves use `C_eff = C0·S(V)`
  (collapses) — **reciprocal** laws, opposite plateau sign. App-6 worked
  numbers (1.155 at half-yield) confirm the `/S(V)` intent; the ch15/ch17
  leaves are the outliers.

These two flags **gate any live ngspice run** (§9): a run silently certifies
whichever inconsistent form the netlist carries.

---

## 2. Design answers (a)-(g)

Each answer: a **recommendation** + **open forks flagged for Grant**.

### (a) SCALAR VS VECTOR — the 6-DOF node → SPICE subcircuit

**The problem.** A SPICE node carries ONE scalar potential; the substrate
node has 3 translational + 3 rotational DOFs (the Cosserat micropolar
node). A naive `X1 A B AVE_VACUUM_CELL` collapses all six into one wire.

**What the corpus already commits to.** vol9 device-circuit-models
`per-dof-vacuum-node-circuit.md` (cited at §6.1) makes the reactive pair
`(L_i, C_i)` **diagonal in the three TRANSLATION DOF** (u→E, EM-translation
sector), and holds *per-DOF-translation ⊥ wave-channel-grade* (seam-7, "do
NOT collapse"). So the corpus's own answer is: the node is **not** one
2-terminal cell — it is (at least) a **per-axis replicated network**.

**RECOMMENDATION — tiered, honest:**

1. **Baseline (rungs 1-4):** treat each *wave channel / axis* as its own
   scalar sub-network. A translation axis = one `AVE_VACUUM_CELL` 2-terminal
   cell in its own node-numbering namespace (`Nx_*`, `Ny_*`, `Nz_*`). This
   is the honest SPICE-native mapping: **3 replicated scalar networks**, one
   per translation DOF, wired to the SAME topological graph but electrically
   independent until a coupling element is added.
2. **Rotational DOFs (the 3 Cosserat micro-rotations):** these are the
   CHARGE-"3" shear/winding sector (§6.1). They do **not** map to a
   translation-cell — they need the shear channel (`Z_shear = ρ c_shear`, a
   *mechanical* impedance, NOT `Z_0`). Represent them as a **separate
   3-network** in mechanical-impedance units, NOT wired galvanically to the
   translation networks (the A1⊥T2 fence, §6.1/master-equation.md:20).
3. **Inter-axis / inter-sector coupling:** only through a **behavioral
   coupling element** (B-source or mutual-K), never a shared node. The
   corpus's only sanctioned inter-grade coupling is the conserved
   `H_couple` (device-circuit-models §6.5): "NEVER a shared (V_inc,V_ref)
   phasor."

So the honest map is: **6-DOF node → 6 scalar sub-networks in 2 impedance
domains (3 translation @ Z_0, 3 rotation @ Z_shear), coupled only through
behavioral H_couple elements, never through shared nodes.**

**OPEN FORK (Grant): a-1.** Is the multi-terminal-cell route (one subckt
with 6 external pins carrying the 6 DOFs as 6 node-voltages) preferable to
6 replicated 2-terminal networks? Multi-terminal is more compact but
re-introduces the shared-node risk (SPICE has no notion of "orthogonal
sectors on the same node"). *Charter lean:* replicated networks — the
orthogonality fence is enforced by *construction* (separate namespaces),
not by discipline.

### (b) CHIRALITY — can a netlist carry I4_132 handedness?

**The problem.** Handedness (`def-7c3f9e`, the I4_132 lattice chirality) is
a geometric property of the srs net. A lumped netlist has no geometry.

**What CAN be carried.** A **non-reciprocal 2-port** — S ≠ Sᵀ — IS
representable in behavioral SPICE via B-sources (a circulator/gyrator
element). The corpus's canonical element for this is the **chiral
circulator** (`def-ch1crc`, `vocabulary-register.md:696`): the bipartite
A/B-sublattice NON-RECIPROCAL inter-tank coupling.

**What BREAKS.** Three hard limits, all corpus-confirmed:

1. **Magnitude is not derivable in a netlist.** `def-ch1crc` status:
   *"STATED — pending the chiral-crystal engine. The cubic-FDTD engine
   averages chirality out."* The netlist can carry the *form* (a
   circulator with S_12 ≠ S_21), but the *non-reciprocity magnitude* is
   IMPOSED (`cvr_model.py:243`). This is the FORM-deriving / VALUE-importing
   verdict again: a netlist chirality element is an **echo at magnitude**.
2. **2-port skew is RECIPROCAL** (the 2026-06-20 PARTIAL, §6.5): the only
   conservative coupling that EXISTS (skew-Hermitian circulator, PR #321)
   is reciprocal (forward == reverse) — it is the optical-activity
   **gyrator** (`def-0pt1ac`), NOT a one-way router. Genuine chiral
   non-reciprocity **needs the 3-port loop** (EM↔shear↔bulk, gauge phase
   3χθ_χ). A 2-terminal-per-edge netlist cannot express the 3-port loop
   without explicitly wiring the EM port as a third leg on every coupling.
3. **Naming trap:** do NOT call the netlist element a "gyrator" — the
   reciprocal `def-0pt1ac` gyrator and the non-reciprocal `def-ch1crc`
   circulator are DIFFERENT elements (`vocabulary-register.md:706`).

**RECOMMENDATION.** The netlist CAN carry a chiral circulator as a
behavioral non-reciprocal element (B-source pair implementing S_12 ≠ S_21),
and mutual-K coupled inductors CAN carry a sign-selected coupling. **But
tag every such element `magnitude-IMPOSED / echo` from birth** — the
netlist inherits, it does not derive, the chirality. The 3-port loop
(needed for genuine non-reciprocity) is a design *requirement* on the
coupling topology, not a free B-source.

**OPEN FORK (Grant): b-1.** Is a netlist chirality element worth building at
all, given the magnitude is imposed and the derivation is the chiral-crystal
engine's job (the geometry half)? *Charter lean:* build it only as a
consistency-fixture (does a 3-port skew loop conserve energy / route
correctly?), never as a derivation. Same posture as `spice_cvr_loop`'s
honest L2 latch: allowed as a fixture, never headlined as emergence.

### (c) TOPOLOGY LIMIT — what SPICE CANNOT do (state it plainly)

**Plainly: a lumped netlist cannot represent a knot.** The electron's
(2,3) phase-space winding / 0₁-unknot real-space body, the proton's 6³₂
Borromean topology, the writhe/Link integers, the confinement-surface
*shape* — none of these exist in a graph of L/C/R elements. A netlist has a
*topology* (which node connects to which) but no *geometry* (where nodes sit
in R³), and the AVE integers are geometric (linking numbers, writhe,
node-span). vol9 §6.2 is explicit: the confinement surface's *"shape is
FORCED by topology … DERIVED, never posited"* — and *"no solved
boundary-value problem produces the electron's surface from its 0₁-unknot
topology"* (§6.2 Status: OPEN). SPICE cannot supply that BVP.

**Where the handoff sits.** The SPICE lane consumes **integers and a graph
adjacency** produced upstream by the spatial srs engine:

```
  spatial srs engine  ──(graph adjacency + winding integers + S(A) bias map)──▶  SPICE lane
   (geometry/topology)                                                          (network eqns + Ax4 limits)
```

The SPICE lane receives: (1) the node/edge adjacency (which cells are
wired), (2) the per-node S(A) bias (the Ax4 saturation at each node from
the geometry solve), (3) any topological integer as a *boundary condition
or a coupling sign* (e.g. a writhe sign → a mutual-K sign, a linking number
→ a phase decree on a circulator). The SPICE lane NEVER computes a winding,
a writhe, or a confinement shape. **The handoff is: geometry/topology →
adjacency+bias+integer-BCs → network solve.** This is the make-or-break
seam of the whole two-layer picture and it is one-directional at rungs 1-4
(the two-way back-reaction is rung-6 / #86, see (e)).

### (d) SINGLE SOURCE OF TRUTH — engine ↔ netlist constitutive lockstep

**The problem, already realized.** The Ax4 kernel `S(x)=√(1-(x/x_max)²)`
appears in BOTH `ave.core.constants` / the Python engine AND the `.lib`
B-sources. **Drift has already happened** (feasibility note FLAG-1): V_YIELD
is 43651.85 / 43651.9 / 43653.7 across constants.py / `.lib` / KB-spec, and
App-6:167 falsely claims nothing is hardcoded.

**Two distinct drift surfaces:**

- **VALUE drift** — the *numbers* (V_YIELD, I_YMAX) baked as `.lib` subckt
  defaults and hardcoded in KB prose.
- **FORM drift** — the *kernel algebra* (which side of the fraction S(V)
  sits on — FLAG-2, the reciprocal-law inconsistency).

**RECOMMENDATION — generated `.lib`, CI-gated, both surfaces:**

1. **Generate the `.lib` from constants.py.** Add a
   `generate_vacuum_cell_lib()` to the compiler that emits the `.lib` with
   `V_YLD`/`I_YMAX` **substituted from `ave.core.constants`** (no subckt
   defaults, or defaults set to the live constant). The `.lib` becomes a
   build artifact, not a hand-edited file. This kills VALUE drift by
   construction (the ave-canonical-source rule).
2. **CI check for FORM drift.** A test that (i) parses the `.lib` B-source
   varactor expression and (ii) evaluates it at 3 sample V's against
   `saturation_factor()` from `scale_invariant.py`, asserting `C_eff/C0`
   matches to machine precision. This catches the FLAG-2 reciprocal-law
   inconsistency the moment it appears in a netlist. (The *existing*
   `TestSaturationKernelConsistency` in `test_spice_vacuum_cell.py` tests
   the Python `saturation_factor` against a *hand-typed* expected value — it
   does NOT parse the `.lib`, so it cannot catch `.lib` FORM drift. This is
   the gap.)
3. **Grep-gate the KB leaves + LaTeX** against hardcoded V_YIELD literals
   (a `verify-before-cite`-style CI grep): any `43653` or bare `V_yield=`
   literal in a `.md`/`.tex` that disagrees with constants.py fails CI.

**OPEN FORK (Grant): d-1.** Should the generated `.lib` be checked into the
repo (auditable, but a drift-able copy) or generated-at-test-time only
(no drift-able copy, but not human-readable in a diff)? *Charter lean:*
generate-at-test-time into a temp, plus a checked-in `.lib.template` with
`{{V_YLD}}` placeholders so diffs stay readable and the substituted artifact
is never hand-editable.

### (e) THE THREE ANALYSES — what each validates against in the engine

The `.OP` / `.AC` / `.TRAN` triple IS the two-layer picture's operational
spine. Mapping each to an engine cross-check:

| SPICE analysis | Substrate meaning | Validates against (engine) | Class |
|---|---|---|---|
| **`.OP`** | The **bias/statics solve** — DC operating point = the S(A) map per node. SPICE builds `G v = i` and solves for node potentials. | The srs engine's Poisson/Laplacian statics solve (the bias map). Pilot §3 shows MNA `.OP` == graph-Laplacian to 1e-15. | consistency (linear); manifestation (once S(A) nonlinearity in) |
| **`.AC`** | **Small-signal waves on the biased network** — linearize the Ax4 cell about its OP, sweep frequency, read the transfer function / dispersion. | The engine's ABCD-cascade eigenvalues / dispersion ω(k) (App-6 table:63) and the biased-chain speed shift (the S(A)→c_local map). | manifestation / consistency |
| **`.TRAN`** | The **full nonlinear co-evolution** — the biased network AND the bias evolve together. This is the **#86 back-reaction make-or-break** (memory: engine-architecture frontier). | The engine's two-way S(A)↔wave back-reaction (the DE-tracks-matter chord). **Long-game target, NOT rung-1.** | emergence (if it works) |

**The `.OP` ground-node point (design-question e, called out in the
commission).** SPICE *requires* a ground node — every netlist must have node
0. This is the **principled answer to the closed-graph neutrality
subtlety** that bit the Stage-1 build: a closed graph's Laplacian is
singular (nullspace = the constant vector = "float the whole thing"), so a
bare closed-graph statics solve has no unique solution. SPICE's mandatory
ground = pinning one node = deleting one row/col = making the reduced
Laplacian invertible. **The pilot demonstrates exactly this** (§3: ground
row/col deletion gives a unique solve agreeing with the pinned-Dirichlet
numpy path to 1e-15). So the SPICE `.OP` convention is not a nuisance — it
is the *correct* statics boundary condition the engine's closed-graph solve
was missing.

**What `.TRAN` needs from empirical-driver discipline (Rule 10).** The #86
back-reaction test is a time-domain LC test → it must record **both** the
C-state (V_inc / ω) AND the L-state (Φ_link / ω_dot) at every step over the
recording window (reactance-pair tracking). A single-phase snapshot cannot
distinguish a static bias from an oscillator caught at peak. This is a
hard requirement on the `.TRAN` rung when it is built, flagged now.

### (f) SCALE — where the lane is a CROSS-CHECK vs a SOLVER

**ngspice node-count reality.** ngspice uses sparse-LU (KLU) MNA; it handles
**~10³-10⁴ nodes** comfortably for `.OP`/`.AC`, and **~10²-10³ nodes** for a
long nonlinear `.TRAN` before wall-time dominates. A behavioral B-source per
edge (the Ax4 cell) is ~5-10× heavier than a plain R/L/C, so the practical
nonlinear-`.TRAN` ceiling is lower, ~a few hundred cells.

**An srs box of N³ cells.** Each cell edge → ~1 `AVE_VACUUM_CELL` subckt =
~4 internal nodes + 3 B-sources. An N³ box has ~3N³ edges (three
axis-directions). So:

| N (box side) | ~cells | ~netlist nodes | ngspice regime |
|---|---|---|---|
| 3 | 27 | ~few hundred | trivial — any analysis |
| 6 | 216 | ~few thousand | `.OP`/`.AC` fine; `.TRAN` slow |
| 10 | 1000 | ~15k nodes | `.OP`/`.AC` at the edge; nonlinear `.TRAN` chokes |
| ≥20 | ≥8000 | ≥120k nodes | **ngspice chokes** — this is the srs engine's job, not SPICE's |

**RECOMMENDATION — the lane is a CROSS-CHECK, not a bulk solver.** SPICE is
a **cell-level and chain-level** verification tool (single cell, 1D chain,
small 2D/3D patch ≤ N=6), where it *cross-checks* the srs engine's own
network solve on a small graph. For any production-scale lattice (N≥10,
electron-genesis boxes, cosmology) the srs engine's JAX/sparse solver is
the SOLVER; SPICE never competes with it. This matches App-6's own
positioning (:320 "SPICE is a verification tool, not a replacement"). **Do
not attempt to run a genesis-scale box through ngspice.**

**OPEN FORK (Grant): f-1.** For the mid-range (N=6-10) where ngspice `.OP`
is feasible but slow, is a cross-check worth the wall-time, or does the
cell + 1D-chain cross-check already pin down every constitutive bug (leaving
only graph-assembly bugs, which a numpy MNA cross-check like the pilot
catches for free)? *Charter lean:* cell + 1D-chain in ngspice; 2D/3D graph
assembly cross-checked by the pilot-style numpy MNA (no ngspice) — reserve
ngspice runs for the constitutive law, use numpy MNA for the topology
assembly.

### (g) STATICS CROSS-SOLVE — the minimal reusable harness (immediate consumer)

**The immediate consumer.** The Stage-1b rework needs an independent Poisson
cross-check: resistor network + current source + ground. **This already
exists as of this charter** — the pilot IS the minimal harness:
`spice_lane_pilot_poisson.py` exposes `build_random_resistor_graph`,
`solve_mna`, `solve_laplacian_pinned`, `emit_netlist`.

**Minimal reusable spec (what Stage-1b imports):**

```
solve_mna(L, ground, inject) -> v          # the SPICE .OP linear system, numpy
emit_netlist(edges, ground, inject) -> str # the ngspice-ready .cir (run when ngspice lands)
```

`L` is the weighted graph-Laplacian (conductance stamp) the srs engine
already has; `ground` is the pinned node (the neutrality fix); `inject` is
the current-source RHS. The harness returns node potentials AND emits the
matching `.cir`, so Stage-1b gets a numpy cross-check TODAY and a
second-engine (ngspice) cross-check the moment ngspice is installed — with
zero additional code.

**RECOMMENDATION.** Adopt the pilot as the Stage-1b statics cross-check
harness. It is 3 functions, pure numpy, no dependency, verified to 1e-15
against the independent Laplacian path. Promote it from
`scripts/vol_4_engineering/` into `src/ave/solvers/` (a
`poisson_cross_solve.py`) when Stage-1b consumes it, with a keeper test.

---

## 3. Pilot verdict

**PASS.** `spice_lane_pilot_poisson.py` on a 24-node/32-edge random resistor
graph with 1 mA injection: `max|v_MNA − v_Laplacian| = 7.55e-15 V`
(threshold 1e-10). The MNA linear system a SPICE `.OP` builds IS the
weighted graph-Laplacian the engine solves; the two agree to machine
precision. The ground-node row/col deletion is the principled neutrality
fix. Test-ladder rung 3 (known-Poisson vs numpy) demonstrated end-to-end.

**Caveat:** ngspice itself did NOT run (not installed). The pilot builds the
identical MNA matrix ngspice would build, in numpy, and emits the ngspice-
ready `.cir`. It does not exercise the Ax4 nonlinear kernel (that is rung 2,
blocked on the ngspice install).

---

## 4. Test ladder (validate-on-known, before the lane may verify anything)

Acceptance sequence. Each rung must pass before the next. Rungs 1-4 are the
lane's *self-qualification*; rung 5 is the first physics cross-check.

| Rung | Test | Validates | Needs ngspice? | Status |
|---|---|---|---|---|
| 1 | RC/LC analytic transients — τ=RC, f_res=1/(2π√LC) | the engine parses + integrates correctly | yes (or numpy MNA) | pending install |
| 2 | Single `AVE_VACUUM_CELL` Ax4 curve vs the kernel from constants.py — the varactor C(V) plateau | the `.lib` B-source == `saturation_factor()` (**catches FLAG-1 + FLAG-2**) | yes (B-source eval) | **blocked** — the sign/value flags must be adjudicated first |
| 3 | Known Poisson profile on a small graph vs numpy | `.OP` == graph-Laplacian; the neutrality/ground fix | **no** (numpy MNA) | **DONE** — pilot, 1e-15 |
| 4 | 1D LC-chain dispersion vs analytic ω(k) | `.AC` on a biased chain == engine dispersion | yes | pending install |
| 5 | Biased-chain small-signal speed shift vs the S(A) prediction | **first bias-couples-to-wave test** — the S(A)→c_local map | yes | pending install |

**Charter note on rung 5.** This class — a bias-coupled-to-wave effect — is
where the corpus's ONE bankable falsifier lives: E-route vacuum
birefringence (memory: birefringence FORK-1 resolved; the μ-grade is a
relativistic inductor keyed on circulation → static-B transparent →
E-route/HIBEF is the real test). Rung 5 is therefore not just a lane-QA
step; it is the smallest in-silico rehearsal of the falsifier. Build it with
that lineage explicit (do NOT headline it as the falsifier — it is a
consistency rehearsal of one).

---

## 5. Phased implementation plan (with cost estimates)

Costs are engineer-session estimates (S = short ≈ ½ session, M ≈ 1 session,
L ≈ 2-3 sessions). Every phase is gated; no phase proceeds on an
un-adjudicated premise (parallel-pressure-test discipline).

| Phase | Deliverable | Gate to enter | Cost |
|---|---|---|---|
| **P0 — Prereq** | `brew install ngspice`; wire `NGSPICE_AVAILABLE` into CI (the 5 skipped tests un-skip) | Grant approves the system-state change | S |
| **P0.5 — Flag adjudication** | Resolve FLAG-1 (value drift) + FLAG-2 (varactor sign) with Grant. Pick the canonical kernel side; regenerate/retag the outlier KB leaves (ch15/ch17) | Grant rules on the sign + value | S |
| **P1 — Single source of truth** | Generated `.lib` from constants.py (`.lib.template` + substitution); the FORM-drift CI check (parse `.lib`, eval vs `saturation_factor`); the KB-literal grep gate | P0.5 done (know the canonical form to lock) | M |
| **P2 — Rungs 1-2** | ngspice RC/LC transients + single-cell Ax4 curve vs kernel. Rung-2 is the payoff of P1 (the `.lib` now provably matches the engine) | P1 done, ngspice installed | M |
| **P3 — Statics cross-solve promotion** | Promote the pilot to `src/ave/solvers/poisson_cross_solve.py` + keeper test; Stage-1b consumes it | Stage-1b needs it (already feasible) | S |
| **P4 — Rungs 4-5** | 1D LC-chain `.AC` dispersion; biased-chain small-signal speed shift vs S(A) (the first bias→wave cross-check) | P2 done | M |
| **P5 — Scalar→vector honesty** | Per-axis replicated networks (design (a)); the 2 impedance domains; H_couple behavioral coupling — as a *fixture*, tagged form-derived/value-imported | P4 done + Grant rules on fork a-1 | L |
| **P6 — `.TRAN` back-reaction (#86)** | The two-way S(A)↔wave co-evolution with reactance-pair tracking. The make-or-break. Long-game. | P5 done + the engine-half back-reaction exists to cross-check against | L+ |

**Chirality (design (b))** is deliberately NOT its own phase — a netlist
chirality element is magnitude-imposed (echo) and the derivation is the
chiral-crystal engine's job. It enters (if at all) as a P5 fixture, tagged
echo, never headlined.

---

## 6. REASONABLE-PATH verdict

**YES — reasonable, cheap, and useful, with two named preconditions.**

**Why reasonable:**

- The dependency is tiny (ngspice: 2.6 MB brew bottle, open-source,
  CI-friendly — App-6's own canonical target).
- The core math already agrees: the pilot shows the SPICE `.OP` MNA system
  IS the engine's graph-Laplacian to 1e-15. There is no fundamental
  mismatch to reconcile at the linear-statics level.
- The lane fills a real gap: the srs engine's closed-graph statics solve was
  bitten by the neutrality/singular-Laplacian subtlety; SPICE's mandatory
  ground is the *correct* boundary condition, and the pilot harness delivers
  it to Stage-1b today (numpy) and via a second engine tomorrow (ngspice).
- The division of labor is clean and corpus-consistent: SPICE = network
  equations + Ax4 constitutive limits (cell/chain scale); srs engine =
  geometry/topology/windings (bulk scale). App-6 already positions SPICE as
  verification-not-replacement (:320).

**The two named preconditions (blockers, not doubts):**

1. **FLAG-2 (varactor sign) must be adjudicated first.** The canonical
   `.lib` and two KB leaves carry *reciprocal* constitutive laws (C_eff =
   C0/S vs C0·S) — opposite plateau signs. A live ngspice run would silently
   certify whichever the netlist carries. This is a load-bearing physics
   contradiction (which way does vacuum capacitance go at yield?), not a
   typo. Cheap to fix (App-6's worked numbers already imply `/S`), but must
   be a Grant ruling, not a silent implementer choice (flag-don't-fix).
2. **FLAG-1 (value drift) is the drift the lane exists to prevent, already
   present.** V_YIELD is three different numbers across constants/`.lib`/KB,
   and App-6 falsely claims nothing is hardcoded. P1 (generated `.lib` +
   CI) fixes it structurally, but it must be fixed *before* the lane is
   trusted as a cross-check, or the cross-check certifies drift.

**Where it is NOT a solver (the honest ceiling):** SPICE cannot represent
topology (no knot in a netlist — design (c)), cannot derive chirality
magnitude (imposed — design (b)), and chokes above ~10k nodes (design (f)).
It is a **cell/chain-scale cross-check**, full stop. The moment a claim
needs a winding, a writhe, a confinement shape, or a genesis-scale box, the
handoff to the srs engine (design (c)) is mandatory. Charter the lane at
that scope and it is a clean, cheap win. Overclaim it as a bulk solver or a
topology engine and it fails.

**One-line verdict:** *Promote the emit-only lane to a run-and-cross-check
lane at cell/chain scale — after the sign + value flags are Grant-adjudicated
and the `.lib` is generated from constants.py. Reasonable path; the pilot
already proves the linear-statics floor.*

---

## 7. Grant-gated forks (consolidated)

| ID | Fork | Charter lean |
|---|---|---|
| **FLAG-1** | V_YIELD value drift (43651.85 / 43651.9 / 43653.7) — which is canonical? | constants.py (43651.85); regenerate `.lib` + retag KB/LaTeX |
| **FLAG-2** | Varactor sign: C_eff = C0/S (diverge) vs C0·S (collapse) — reciprocal laws | `/S` (diverge) — App-6 worked numbers imply it; ch15/ch17 are outliers |
| **a-1** | 6-DOF node: 6 replicated 2-terminal networks vs one 6-pin multi-terminal cell | replicated (orthogonality by construction) |
| **b-1** | Build a netlist chirality element at all (magnitude imposed)? | only as an echo-tagged consistency fixture, never headlined |
| **d-1** | Generated `.lib`: checked-in artifact vs generate-at-test-time | `.lib.template` + substitute-at-test-time |
| **f-1** | Mid-range (N=6-10) ngspice `.OP` worth the wall-time? | no — cell+chain in ngspice, 2D/3D assembly via numpy MNA pilot |

---

## 8. Skills applied (retro-pass)

`substrate-native-check` (the 6-DOF→subcircuit map, design (a); sector
declaration before the SPICE word) · `verify-before-cite` (every inventory
row grepped; feasibility note file:line) · `consistency-vs-emergence` (the
three-analyses class column; rung-5 tagged consistency-rehearsal not
falsifier) · `flag-don't-fix` (FLAG-1/FLAG-2 surfaced with both paths +
verbatim, NOT resolved) · `ave-canonical-source` (design (d) single-source
mechanism) · `phase-space-coordinate-check` (design (c): the AVE integers
are phase-space/geometric, not lumped-netlist-representable).

## 9. Lane-discipline note

This charter does NOT: draft an Ax5 candidate (the flags are engine/KB
inconsistencies, not a missing axiom — A44); draft the auditor's manual
entry (surfaced, auditor lands); silently resolve FLAG-1/FLAG-2 (Grant
adjudicates the physics). The pilot is the one bounded run the commission
allowed. No system-state change was made (ngspice NOT installed).

