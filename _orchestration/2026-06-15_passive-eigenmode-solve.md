# Passive winding-protected electron eigenmode — the structural keystone (ORCHESTRATION)

> **STATUS: PHASE 0 COMPLETE (corpus-grep prereg) → PHASE 1 GRANT GATE (ontology + flags).**
> Lane worktree `AVE-Core-eigenmode-wt`, branch `analysis/2026-06-15-passive-eigenmode-solve`
> off `main@40a2a2e7`. **main is PROTECTED — Grant merges; this lane does NOT merge.**
> Arc: corpus-grep prereg ✅ → **ontology+flags surface to Grant (GATE — HERE)** →
> Rule-11 freeze → auditor-gate → driver → result → adjudicate to Grant.
>
> **HEADLINE (the prereg payload):** the passive fixed-point solve is **NOT greenfield**.
> The energy/S11 stationary-point version is **FALSIFIED**; the *decoupled* wave-eigensolve
> returned **Mode III (no bound state)**; the **ONE untried residue** is the **fully-coupled
> hybrid (V≠0 ∧ ω≠0) wave-eigensolve** with the (2,3) winding **imposed as a topological BC**
> on the independent ω-carrier. The charter's "winding as topological BC" is exactly what
> **rescues** the question from the prior negatives (which all let the winding be *selected*).

---

## §0 — Derivation target (the charter, verbatim)

Does a self-consistent nonlinear **STANDING** eigenmode exist — find $\psi$ such that the
saturation $S[\psi]$ forms a $\Gamma=-1$ cavity whose **own eigenmode IS $\psi$** — with the
conserved $(2,3)$ winding as a **TOPOLOGICAL boundary condition**, in the **T2 / phase-space
channel**, **LOSSLESS/PASSIVE** (a fixed-point, NOT autoresonant gain-driven)?

Not "can a flowing photon dynamically lock into mass" (genesis, banked negative — §1) but
"does a passive, topology-protected standing fixed-point **exist + is it stable**." A
**boundary-value / self-consistency** problem, not an initial-value evolution.

---

## §1 — Why this is DIFFERENT from the banked *genesis* negative

**BANKED — `research/2026-06-14_t2-genesis-selflock_result.md` (PR #233):** the ACTIVE
autoresonant self-lock tested **NO-GENESIS at every $A_0$** on `crystal_engine`/near-yield;
anti-lock signature **$\omega_{local}$ RISING**. It **explicitly scopes its null** to "this
engine/regime/precursor; does NOT prove photon→mass impossible." That is an **initial-value**
null; it says nothing about whether the **passive fixed-point exists.**

| Axis | Genesis self-lock (banked) | THIS effort (passive eigenmode) |
|:---|:---|:---|
| Problem class | initial-value (seed→evolve→watch) | boundary-value / fixed-point |
| Energetics | active, gain loop | passive/lossless fixed-point |
| Question | does it *dynamically form*? | does the standing solution *exist + is it stable*? |
| Winding | (not the discriminator) | **imposed** as a topological BC on $\psi$ |
| Detector | PLV (DEFECTIVE) | self-consistency residual + stability eigenvalue |

---

## §2 — Prior-work inventory (corpus sweep `wte7dhv5v`, 8 angles, grep-confirmed)

**This is the load-bearing prereg finding. The passive solve has been worked in three forms;
two are closed-negative, one is the live-open residue.**

### 2a — What was DONE and FALSIFIED / NEGATIVE

1. **Energy / S11 gradient-flow stationary-point solve → DONE, FALSIFIED.** Live solvers
   exist: `cosserat_field_3d.py:1453` `relax_to_ground_state`, `:1317` `relax_s11`; coupled
   `src/scripts/vol_1_foundations/coupled_s11_eigenmode.py` (F17-K Phase 5, commits
   `6158465`→`2c873cf`→`4c9fbea`). Seeded **AT** Golden Torus geometry, **both objectives
   drift away at iteration 1** (energy →R/r=3.40, S11 →R/r=1.03; target φ²=2.62). Corpus
   verdict (`2026-05-18_abcd-handoff-prereg-outcome-corpus-state-retrofit.md:24,50`):
   **"Golden Torus is NOT a stationary point of either Cosserat-energy or coupled-S11
   gradient flow … GT is selected by topological-quantization ANSATZ, not by gradient flow
   on any objective the engine knows."** Plus the corpus's own **methodological** verdict
   (`VACUUM_ENGINE_MANUAL.md:1692`): energy stationary-point = **SM/QM-leakage, AVOID**;
   the correct passive object is a **wave eigenmode** (V = OUTPUT eigenvector, not a seed).
2. **Decoupled wave-eigensolve (the RIGHT object) → PARTIALLY RUN → Mode III.** Helmholtz
   form `div(z(x)∇V)+k²V=0`, `z(x)=`Op14 saturation profile (`72_vacuum_impedance_design_space.md:21`).
   R7.1 ran the **decoupled V=0 block + bottom-100 Cos-block at fixed cavity** → **Mode III,
   no electron bound state at ω_C** (`…retrofit.md:76-85`).
3. **ABCD-matrix direct eigensolver ("stationary by construction, no time evolution") →
   PROPOSED-then-RETIRED, no code written** (`2026-05-18_abcd-eigensolver-workstream-handoff.md:1-14`):
   retired because the gradient-flow falsification "applies equally to the proposed ABCD
   eigensolve."

> **Currency caveat (verify-before-cite):** the L3 stationary-point closure is spring-2026;
> the 2026-06 arcs (option-B, nyquist-binding) **carry the negatives forward as canon** (the
> binder-must-be-nucleated finding), so they are live — but the **hybrid-coupled variant is
> the one explicitly left open.**

### 2b — The ONE genuinely-untried residue (the real target)

**The fully-coupled HYBRID eigenmode: V≠0 AND ω≠0 simultaneously, where the Op14 saturation
cross-coupling is the load-bearing BINDING (not a perturbation).** Named explicitly and
**never run** (`72_vacuum_impedance_design_space.md:158` — "genuinely hybrid (V,ω)
eigenmodes that require V-nonzero AND omega-nonzero simultaneously … the decoupled-block
solve CANNOT find by construction … Round 8 question"; `…retrofit.md:76-85` item 2;
restated as the open Layer-8 "smallest stable soliton from K4+Axiom-4 with $m_e$ NOWHERE in
inputs" at `2026-06-11_nyquist-binding-route_CLOSED.md:54-58`).

### 2c — Two load-bearing CONSTRAINTS any passive solve MUST clear

- **The ω≡0 exact-fixed-point trap.** K4↔Cosserat coupling `W_refl` is **even in ω** → ω=0
  is an **exact fixed point**; a **pure-V seed can never break the ω=0 symmetry**
  (`option-B-discrete-emergence-result.md:181,210,356`; `2026-06-06_simulation-assumptions-audit.md:13`
  A1.1 — "the entire electron-genesis (III) verdict is a direct consequence of this one
  assumption"). **→ a passive relaxation seeded pure-V lands at the trivial ω=0 solution.**
  The fix: an explicit ω content / odd symmetry-breaker — **which the charter's imposed
  winding-BC supplies.**
- **The (2,3) winding is the BINDER and must be NUCLEATED/IMPOSED.** Impose it (Arm C) →
  binds at **91% retention**; withhold it (Arm A) → **disperses like noise (1.7% ≈ baseline)**
  (`option-B-discrete-emergence-result.md:348,358`). **→ the charter is right to impose the
  winding as a BC, not let it emerge.**

**Consequence for the ontology (the rescue):** every prior negative let the winding be
*selected/emergent* (gradient flow on an objective; or a pure-V seed hitting the ω=0 trap).
The charter **imposes** the (2,3) winding as a topological BC and asks only: *given that BC,
does the coupled (V,ω) wave-eigensolve have a **stable, lossless** bound eigenmode at ω_C?*
That is **well-posed and genuinely open** — and distinct from the falsified "is GT a
stationary point of an objective."

### 2d — Reusable infrastructure (and the gap)

- **Fixed-point half EXISTS:** `solvers/eigenvalue_root_finder.py:60` `find_eigenstate`
  (domain-agnostic Newton-Raphson on a λ_min(S†S)·G residual, "ZERO domain-specific
  physics" + JAX variant); `universal_operators.py:347` λ_min(S†S) primitive;
  `cosserat_field_3d.py:1453/1317` relax_*; self-consistent idioms at
  `radial_eigenvalue.py:1031` (brentq + screening loop) and `cosserat.py:133`
  (parameter-free Δ-iteration).
- **Stability half MUST BE BUILT:** there is **no** Jacobian-eigenvalue / growth-rate /
  sparse-eigsh linear-stability routine anywhere in `src/ave` (grep empty). The only
  "stability" is a perturb-then-re-verify **kick** (`electron_spec_suite.py:85`
  `spec_T4_stability_kick`) — empirical, not an eigenvalue. The gradient + Verlet stepper
  primitives to build a finite-difference Jacobian → eigvals layer DO exist.

### 2e — Winding carrier + coordinate discipline (the correct, hazard-free representation)

- **Winding lives on the INDEPENDENT Cosserat-ω carrier, NOT the breather phasor.** Reuse
  `src/ave/utils/fast_winding_extractor.py:165` `extract_2_3_omega_fast(omega, pi_omega,…)`
  (toroidal-2 from the ω-major circle, poloidal-3 from the ω-tank LC phase). Charge =
  **Beltrami helicity** `_beltrami_helicity` (`cosserat_field_3d.py:450`); winding→coupling
  `kappa_tilde_torus(p,q)=pq/(p+q)` → (2,3)→`1.2·α` (`cosserat_field_3d.py:98`).
- **Coordinate discipline (A46, load-bearing).** The (2,3) Clifford-torus winding is a
  **phase-space** object (`theory.md:16`, `ch8-alpha-golden-torus.md:29`). The phasor
  **SHAPE** (aspect R/r=φ²) is **necessary-not-sufficient**, NOT the winding pair
  (`2026-06-04_full-electron-transverse-selftrap-result.md:90,144`). Instrument in phasor
  coords (`V_inc=E+ZH`, `V_ref=E−ZH`) — but the **winding DOF is read off the ω-carrier**,
  per below.
- **HARD HAZARD verbatim** (`master-equation.md:20`; code basis `k4_tlm.py:346`,
  `master_fdtd_phasor_bridge.py:14-18`): "**never wire the winding into the breather's own
  phasor `(V_inc, V_ref)`** — `V_ref` is a read-only projection of the same scalar `V`, not
  an independent DOF; doing so self-inflicts the genesis-24/crystal `w_pol=0` double-count."

---

## §3 — Discriminator + classification

**Classification (`consistency-vs-emergence`):** an **EXISTENCE test** — does the substrate
support a **stable lossless** self-consistent passive standing mode, given the imposed (2,3)
BC? **Non-redundant over the dynamical Arm-C imposed-winding run** (which bound at 91%
*retention*, i.e. a *decaying* dynamical state): the passive solve adds **(i) lossless
existence** (a true standing eigenmode, not a slow leak) and **(ii) the linear-stability
eigenvalue** (stable fixed point vs metastable).

- **POSITIVE:** a stable, lossless, self-consistent hybrid (V,ω) standing mode exists at
  ω_C, (2,3) winding conserved on the ω-carrier, largest stability eigenvalue ≤ 0 (no gain
  required) → **the eigencavity STRUCTURE is real.**
- **NEGATIVE:** no self-consistent solution / disperses / a stable solution **requires gain**
  → **the structural eigenmode fails** (stronger than the genesis null — the standing
  mass-mode does not exist as a passive fixed-point even with the winding imposed).

---

## §4 — Method skeleton (for the driver brief; NOT yet dispatched, GATE-blocked)

The substrate-native passive solve = a **wave eigenmode** with V as OUTPUT (NOT gradient
descent on an energy/S11 objective — that route is falsified + SM-leakage, §2a):

1. **Impose** the (2,3) winding as a topological BC on the **independent Cosserat-ω carrier**
   (supplies the odd ω that clears the ω=0 trap; `extract_2_3_omega_fast` for read-out).
   Never wire it into `(V_inc,V_ref)`.
2. **Coupled self-consistency:** given the trial ω-winding + V profile, compute the Op14
   saturation $z(x)=S[\psi]$ → the $\Gamma=-1$ cavity rendered as a **boundary condition**
   ($\Gamma$, Op17-bounded), **NOT** a bulk energy/force term (`substrate-native-check` CP10
   — bulk term is singular at the wall and detonates; cf. the PUMP DETONATE arm).
3. **Solve the coupled (V,ω) wave-eigenproblem** in that cavity — both sectors nonzero, Op14
   cross-coupling load-bearing — for eigenmode φ + eigenfrequency.
4. **Self-consistency update** $\psi\leftarrow\phi$ (winding-preserving); iterate to fixed
   point. Convergence = residual→0 (reuse `find_eigenstate` / relax_* machinery, §2d).
5. **Stability (BUILD this):** finite-difference Jacobian of the map about the fixed point →
   eigenvalues; largest real part decides **stable lossless** vs **requires gain / unstable**.
6. **`ave-conserved-vs-pumped`:** the converged state must be a **passive fixed point** —
   a drive-sustained state is a NEGATIVE, not a positive.

**Detector reframe (replaces the defective PLV):** validation pair = **converge to the
known sech eigen-profile** (positive control; cage `SECH_ANCHOR` PR #222, `self.V`
self-focuses, F1/F3-PASS, persists bounded — `cage-stiffening-wall_result.md:12`,
`cage_stiffening_wall.py:109`) and **a generic Gaussian fails to converge / disperses**
(negative control, same result:13). This is profile-selectivity at the fixed-point level,
not a time-series coherence gate.

**Platform (per `ave-loop-gap-harness-discipline`):** the A1/longitudinal-bulk Γ=−1 cavity
is `crystal_engine.py`/`master_equation_fdtd.py`'s confirmed home; the ω-carrier needs
`CosseratField3D` (which hosts the relax_* fixed-point finders) + the coupled
`VacuumEngine3D`/`CoupledK4Cosserat`. **The hybrid-coupled solve spans both — exactly the
A1⊗T2 cross-coupling that is the open physics. This is Flag-A; platform is GATE-blocked.**

---

## §5 — Flags to Grant (flag-don't-fix; the Phase-1 GATE)

**Flag-A — A1-vs-T2 mass sector (UNRESOLVED, load-bearing for the solve's channel).**
Both sides live, neither retracted at HEAD:
- **SIDE A (T2-mass):** `cosserat-mass-gap.md:108` — "$A_1$ … is massless, $T_2$ … carries
  the mass-gap content"; `:106` $m_ec²$ inherits from the Cosserat (T2) mass-gap formula.
- **SIDE B (A1-mass):** `master-equation.md:20` — "$m_ec²$ = trapped acoustic compression =
  **A1 dilatation-MASS**"; T2 carries the **winding/charge**, NOT the mass.
- The **provenance-vs-state** reframe (`cosserat-mass-gap.md:110`, `photon-identification.md:17`)
  sides with B (A1 standing-V = the saturated-phase order parameter) but **does not retract
  SIDE A's body line**; `photon-identification.md` hosts THREE framings in one file (`:11`
  T2-photon, `:17` A1-dilatation, `:151` sector-agnostic standing wave). $m_ec²$ magnitude is
  **hypothesis-class** (`photon-identification.md:19`).
- **The question:** is $\psi$ an A1 object, a T2 object, or the **hybrid (V,ω)** object (the
  charter's "T2 channel" with the cavity reading A1/bulk)? The §2b residue says **hybrid** —
  which would make the contradiction a **false dichotomy** the solve could *resolve*: mass =
  the coupled standing energy, A1 amplitude ⊗ T2 winding, bound by Op14. **Does Grant accept
  framing the solve on the hybrid (V,ω) mode (so it bears on Flag-A), or hold the sector call
  fixed first?**

**Flag-B — the SCOPING call (the decisive one).** The corpus has already falsified the
gradient-flow stationary-point route and returned Mode-III on the decoupled wave-eigensolve;
its own diagnosis is "**GT is selected by topological ANSATZ, not by any eigen/objective
principle.**" Two readings:
- **(B1) Proceed, scoped to the untried hybrid-coupled wave-eigensolve** with the winding
  imposed as a BC (§2b/§4). Rationale: the imposed-BC framing is precisely what the prior
  negatives did NOT test, and it is the named-open Round-8/Layer-8 target.
- **(B2) The "topological ANSATZ, not eigen-principle" diagnosis is itself the answer** — i.e.
  a NEGATIVE here is already strongly expected, and the structural keystone may be "the
  winding is quantized/imposed, full stop; there is no further self-selecting eigen-principle
  to find." Under this reading the effort's value is a **clean confirmation** (the structure
  is imposed, not emergent), not a discovery.

  **My read (orchestration, not a decision):** B1 is worth running *because* the discriminator
  cuts both ways — a stable lossless hybrid eigenmode would be a real positive (structure is a
  genuine passive eigenstructure), and a clean negative would *upgrade* B2 from "expected" to
  "tested." But it is your physics call whether B1 is a new test or a re-skin of the closed
  stationary-point negative.

**Flag-C — detector reframe.** PLV LOCK is dropped for **self-consistency residual +
stability eigenvalue**, validated by the **sech-converges / Gaussian-disperses** control pair
(§4). Confirm this is the right instrument (the PLV defect, `t2_…_result.md` §0.5, is why).

**Flag-D — clock exponent (3-way contradicted; sets the cavity-mode frequency).** Matter
clock = `c_shear = c₀(1−A²)^{+1/4}` (CORRECT, `CLAUDE.md` INVARIANT-S2); `op14-local-clock-
modulation.md:17` `^{1/2}` STALE (off ×2); `04_superluminal_transit.tex:41` `c_EM` MISLABELED
(`2026-06-09_substrate-temporal-values-definition.md:48`). Resolution proposed (p=1/4) but
stale leaves remain in-corpus. The eigensolve's ω_C must use the **shear** exponent; flag so
it does not silently inherit a stale ½.

(Inline-prose surface per `feedback_inline_questions` — no multi-choice UI.)

---

## §6 — Skill-selection plan (60-sec, per `feedback_skill_selection_planning`)

| Skill | Where it fires | Why load-bearing |
|:---|:---|:---|
| `ave-prereg` | Phase 0 ✅ | corpus-grep inventory — **caught the non-greenfield finding** |
| `phase-space-coordinate-check` | prereg + driver | winding read in phasor/ω-carrier, not real-space (A46) |
| `substrate-native-check` (CP8/9/10) | driver brief | impose winding-BC (CP8 with the ω=0-trap caveat); Γ as BC not bulk (CP10); dynamical not algebraic (CP9) |
| `ave-conserved-vs-pumped` | driver + result | passive/lossless fixed-point; drive-sustained = NEGATIVE |
| `consistency-vs-emergence` | result | existence/emergence test, non-redundant over Arm-C |
| `pre-test-physics-check` (T7+T8) | **GATE (now)** | 2+ prior negatives on adjacent routes → surface reframe; ontology before dispatch |
| `ave-loop-gap-harness-discipline` | platform | hybrid spans crystal_engine ⊗ Cosserat; no new `*_vN` |
| `ave-driver-script-honesty` + `ave-apparatus-floor-attribution` | result | convergence/floor = physics or solver artifact |

---

## §7 — Arc + gates

| Phase | Gate | Owner | State |
|:---|:---|:---|:---|
| **0. Corpus-grep prereg** | sweep `wte7dhv5v` → inventory | THIS lane | ✅ DONE |
| **1. Ontology + flags** | **GRANT GATE** (Flags A–D; B = scoping) | Grant | **← HERE** |
| **2. Rule-11 freeze** | prereg frozen (discriminator + bins + falsifiers) | THIS lane | blocked on 1 |
| **3. Auditor-gate** | READ-ONLY `ave-auditor` verifies prereg vs corpus | auditor | — |
| **4. Driver** | ave-implementer, own worktree, §4 hybrid-coupled wave-eigensolve + controls + stability layer | implementer | — |
| **5. Result** | honest bin vs discriminator; flag-don't-fix | implementer | — |
| **6. Adjudicate** | result → Grant | Grant | — |

---

## §8 — Phase log

- **2026-06-15** — Lane founded. Read charter + `_orchestration/index.md` +
  `manuscript/ave-kb/CLAUDE.md` + `ave-loop-gap-harness-discipline`. Verified grounded-state
  anchors. Worktree off `main@40a2a2e7`. **Phase 0 corpus sweep `wte7dhv5v` (8
  ave-corpus-grep agents) COMPLETE** → inventory §2: passive solve is NOT greenfield
  (gradient-flow FALSIFIED, decoupled wave-eigensolve Mode-III, ABCD retired); ONE untried
  residue = hybrid-coupled (V,ω) wave-eigensolve with imposed (2,3) BC; two constraints
  (ω=0 trap, binder-must-be-nucleated) that the imposed-BC framing clears; infra exists for
  the fixed-point half, stability layer must be built. **NEXT: Phase-1 Grant gate — Flags
  A–D + the B scoping call. Driver dispatch is GATE-blocked.**
