> # ⚠ DRAFT — NOT FROZEN, NOT A PREREG OF RECORD
>
> **This is the pre-G2 skeleton, preserved in git so hours of characterised
> work survive a scratch wipe. It is NOT the prereg P2 will run under.**
>
> **What it is:** a firewalled author's draft (the author saw no results and
> none existed), declaring the observable set and discharging the epic's eight
> guards, with every decision-1/decision-3-dependent value left BLANK and
> marked `FROZEN-AT-G2`.
>
> **Known defects, from the 2026-08-25 firewall audit — repair these before
> any freeze:** (1) it presents G2 decision 4 as RULED using a phrasing that
> did not exist in the corpus at authoring time (the ruling is now recorded in
> R58, so this is repairable by re-citation); (2) observables (b) M/Q and (c) g
> carry **no declared extraction method** — exactly the two a later author
> could tune; (3) the g controls are **not genuinely can-fire** as written
> (the analytic fixture exercises the wrong code path); (4) a WALK-tagged
> premise (the elementarity reading) is load-bearing in the frozen
> adjudication table it is explicitly forbidden from supporting; (5) the "g
> carries no FROZEN-AT-G2 blank" exemption is unsound.
>
> **Blocked on:** S1 (no machinery maps a solution to M, Q or g — blocks the
> two RULED observables), the decision-1/carrier coupling, and the
> non-triviality + aliasing gates R58 §4 requires. See
> `_orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md`.

# PREREG SKELETON — P2: the autonomous-mode existence solve (static-existence epic, Stage 4)

**Status: SKELETON, pre-freeze.** Written by a prereg-author agent **FIREWALLED
from results**: no P2 run has been executed, no P2 number exists, and the author
will never see the run. This document becomes the FROZEN prereg when the four G2
decisions are ruled and every `FROZEN-AT-G2` blank in §5 is filled **verbatim from
the ruling**. Until then it is not a freeze and no run may execute against it.

**Authoring commit (every cite below verified at this SHA):** `766d5179`
(AVE-Core `main`, 2026-08-25).

**Consumes (all on `origin/main`):**
- the epic — [`_orchestration/2026-08-24_static-existence-epic.md`](../_orchestration/2026-08-24_static-existence-epic.md) (§1 carve, §5 guard set, §8 what-this-is-NOT)
- the build brief — [`_orchestration/2026-08-24_static-existence-build-brief.md`](../_orchestration/2026-08-24_static-existence-build-brief.md) (Stage 3 = G2, Stage 4 = P2)
- the G1 walk record — [`research/2026-08-24_g1-ac-steady-state-walk_RECORD.md`](2026-08-24_g1-ac-steady-state-walk_RECORD.md) (harmonic balance + SOURCE-IDLE; DISPROVE pre-frozen)
- the G2 walk record — [`research/2026-08-25_g2-boundary-and-gyromagnetic-walk_RECORD.md`](2026-08-25_g2-boundary-and-gyromagnetic-walk_RECORD.md)
- the decision set — [`_orchestration/open-items/2026-08-25-g2-freeze-decisions.md`](../_orchestration/open-items/2026-08-25-g2-freeze-decisions.md)
- the solver — `src/ave/solvers/harmonic_balance_srs.py` + [`research/2026-08-24_harmonic-balance-solver-validation_note.md`](2026-08-24_harmonic-balance-solver-validation_note.md)
- the measured response maps — [`research/2026-08-24_engine-gamma-meanstest_result.md`](2026-08-24_engine-gamma-meanstest_result.md) (scalar) and [`research/2026-08-24_transverse-gamma-meanstest_result.md`](2026-08-24_transverse-gamma-meanstest_result.md) (both transverse branches)

**G2 decision state at authoring (the firewall's other half — the author does not
know the values of two of the four):**

| # | decision | state | consequence for this document |
|---|---|---|---|
| 1 | scaffold form (source-terminated + common-mode projection vs injection-lock) | **IN FLIGHT** | every dependent value written `FROZEN-AT-G2` and left blank (§5) |
| 2 | observable set — projected M/Q on two imposition representatives | **RULED: "include"** (Grant, verbatim `A2: include`) | §4(b) is written as a binding observable |
| 3 | envelope normalization fork (3a ARM, 3b AGGREGATION, 3b′ port-count mapping) | **IN FLIGHT / HOLD** (gated on the collapse sub-task) | every dependent value written `FROZEN-AT-G2` and left blank (§5) |
| 4 | `g` as a frozen verdict observable | **RULED: "yes"**, with a unit-tested extractor | §4(c) is written as a binding observable with its controls |

**Cite-drift note (verify-before-cite, at this SHA).** The decision-4 text and the
G2 walk record cite canon's honest `g` line as `translation-circuit.md:637`. At
`766d5179` that line is **`translation-circuit.md:839`**, verbatim: *"**$g = 2$ is
POSITED, not derived**"*. The content is unchanged; the line number has drifted.
This document cites **:839** and records the drift rather than propagating a dead
line number.

---

## §0 — SECTOR / REGIME / MODE DECLARATION (house table)

| Axis | Declaration |
|---|---|
| **MODE** | **Autonomous-mode existence solve** by **harmonic balance**: posit a tone set, solve the phasor-domain Kirchhoff fixed point on the graded network with the varactor tone-mixing, and test **SOURCE-IDLE self-consistency**. No time axis, no time-stepping, no transients, no damping device. This is a *fixed-point existence* question, **not** reachability, **not** formation, **not** relaxation-from-a-precursor. |
| **SECTOR** | The `(2,3)` winding is **Cosserat / T2** (the charge carrier); the `S`-railing and mass bookkeeping are **A1-adjacent**. **A1 ⊥ T2 is a fence, not a coupling** (guard 5, §3.5). Which carrier actually runs — and therefore which sectors the run can *represent* — is `FROZEN-AT-G2` (**F7**), because it rides decision 1. **Honest capability statement at authoring:** the harmonic-balance solver is wired on the **scalar `srs-z3`** carrier only (validation note sector header: *"scalar channel on the srs-z3 carrier … T2/Cosserat NOT wired"*), while the Stage-1 transverse machinery (`src/ave/solvers/transverse_graded_scatter.py`) is a **time-domain** vector-TLM scatter with **no phasor/harmonic-balance path**. Any sector the frozen carrier cannot represent is **NOT-RUN and reported as NOT-RUN** — never as a null (§7 V6). |
| **ENGINE-DOF receipt** | Scalar/translational channel: `chiral_lattice.scalar_tlm_step` on `build_srs_net` (`research/2026-08-24_solver-crosscheck-phase0_requirements.md:25`); the phasor operator is that certified scatter+connect map itself (`harmonic_balance_srs.py` header, "THE PHASOR FIXED POINT"). Transverse channel: `transverse_graded_scatter.py` (Stage-1, time-domain). |
| **REGIME** | **Regime-2 nonlinear, self-consistent**: the `S`-field is an *unknown of the solve*, read from the DP-1 cycle-average envelope of the solution's own tone phasors — the tones couple only through the shared `S`-field. This is the first use of the solver's self-consistent path for a physics question; Stage-2 gates 1–2 imposed `A` externally and gate 3 never evaluated the envelope. |
| **PHASE-STATE** | **AC steady state — stationary, NOT DC.** *"Everything moves, nothing changes"* (G1 walk §1): the phasor description is a fixed point, the orbit closes identically every period, envelope and topological class are constants of the motion. **The relaxed state's own regime/phase-state — cold, sub-railed, or railed — is part of the RESULT, never an assumption** (guard 7, §3.7). |
| **CLASS** | **Existence test of a fixed point** under an imposed topological boundary condition. Mints no `clm-`, no `def-`, moves no solidity by itself; P3 propagation fires only behind G3 (adversarial verify, ≥3 lenses, repairs-need-reaudit to convergence). |

**`consistency-vs-emergence` tag (mandatory, epic §6).** A PROVE outcome is at most
**consistency with `clm-satnec`** — the model's own topological-route claim — and is
**never** an emergence result, a formation result, or an AVE-distinct chord. A
DISPROVE outcome demotes `clm-satnec` and leaves the dynamic route
(`resonant-lc-solitons.md:142`) carrying the existence question alone. Both branches
leave the energize-LOCK negative **untouched**.

## §1 — BINDING SCOPE (epic §8, restated as binding text)

This run asks **one** question: *does a source-idle, self-consistent AC steady state
carrying the imposed winding EXIST, and if so does its core rail?* Restating the
epic's own carve:

- **NOT a formation study.** The formation question is `CLOSED-NEGATIVE`
  (energize-LOCK / keystone-pump: the engine pumps `H` at `dt→0`, three escape
  hatches closed). Nothing here reopens it, explains it away, or bears on it in
  either direction.
- **NOT an emergence test.** Imposing the finished texture is legitimate **only**
  because the claim is *existence* (guard 1, §3.1). No result may be framed as the
  engine "hosting", "building", "growing", or "forming" anything.
- **NOT a chord claim.** Any PROVE outcome is **internal consistency of the model's
  own claims**; the AVE-vs-SM boundary is untouched by every branch. No
  AVE-distinct framing may leave this lane without `ave-discrimination-check`.

**FORBIDDEN conclusion-shapes in the result doc, regardless of what the run shows**
(this list is restated verbatim in the result doc's scope block):

1. "therefore the electron / a bound state can (or cannot) FORM";
2. "therefore the energize-LOCK negative is explained away / reopened / weakened";
3. "the engine HOSTS / GENERATES / BUILDS the electron" (any emergence verb);
4. any claim that the imposed winding was *derived*, *selected*, or *preferred* by
   the lattice — it is **imposed**, and the `(2,3)` SELECTION is canon-imported
   (`form-deriving-value-importing.md:221`, `clm-8c3yhs`);
5. any AVE-vs-SM distinctness claim, chord claim, or foreword-promotion proposal;
6. any cross-sector statement of the form "the defect saturates ⇒ the defect IS the
   mass" (guard 5, §3.5);
7. any claim about a sector the frozen carrier does not represent (§7 V6);
8. any statement that a **NOT-RUN** arm or an **out-of-regime** configuration
   returned a null (`ave-regime-phase-state-check`: a null where the effect cannot
   exist is an ARTIFACT, not a falsification).

## §2 — THE METHOD (G1 record §2, executed verbatim)

**The reformulation, and why.** The pre-G1 framing ("impose a static texture, relax
the lattice") was refuted at the G1 walk: *"relax"* is undefined on a lossless
reactive substrate, texture-clamping conflates the DC operating point with the AC
signal, and bleeding-under-hold created an unadjudicable ambiguity. The `(2,3)` is
an **AC object** — two resonances of the bond-pair tank, frequency-locked 3:2, in
steady state. "Static" in canon's named test therefore means **STATIONARY, not DC**.

**The five steps (G1 record §2, binding):**

1. **Posit the tone set** — the 2 and 3 lines on the bond-pair structure. Tones are
   dimensionless per-step phase advances `theta_m` in the canonical open interval
   `(0, pi)` (`ToneSet.__post_init__`, `harmonic_balance_srs.py:362-377`: on integer
   steps `theta` and `2*pi - theta` are the same physical line, and `0`/`pi` are
   self-conjugate and break the `|v|^2/2` cycle mean). **The frozen ratio is 3:2**;
   the numeric base is `FROZEN-AT-G2` (**F8**).
2. **Write phasor-domain Kirchhoff on the graded network**, including the varactor's
   tone-mixing: `e^{i theta_m} v_m = M(S) v_m + sources`, `M(S) = C · blockdiag(S_u)`,
   `S_ij = 2 Y_j / (sum_k Y_k) - delta_ij`, `Y = Y_0 / sqrt(S(A))`.
3. **Close the loop on the S-field.** `A_bond` is the **DP-1 cycle time-average
   envelope** of the solution's own tone phasors — *"NOT an instantaneous phase
   snapshot"* (`substrate-perspective-electron.md:62`). The cross-tone COMBINE rule
   is **derived** (distinct canonical tone lines average out); the **normalization**
   is the open fork frozen at **F3/F4/F5**.
4. **Solve the algebraic fixed point** (`solve_self_consistent`) — no time-stepping,
   no transients, no damping device. Ax3 is untouched **by construction**: the graded
   scatter conserves the `Y`-weighted energy exactly, and the only sink is a declared
   matched **termination** — a boundary condition (checkpoint-10 class), never a bulk
   loss term.
5. **Apply the existence criterion: SOURCE-IDLE self-consistency.** Solve the driven
   steady state, then check that the scaffold goes idle *at the solution*. The wall
   the solution maintains must be made of the solution's own amplitude — *"the mirror
   is made of the thing it confines"*. The scaffold is scaffolding; the test is
   whether it can be removed.

**The source-idle observables (all COMPUTED from the solved state,
`source_idle_report`, `harmonic_balance_srs.py:787-857`):** `source_amp`,
`exchange_amp`, `P_in`, `P_out`, `P_net`, and the autonomous defect
`r_auto = ||e^{i theta} v − M_full v|| / ||v||` taken with the **full, uncut** connect
map. Adjudication is by `idle_verdict(...)` against **caller-declared** thresholds
(**F10**) — reconcile-don't-declare: the function measures, the prereg declares, the
verdict is computed.

> **★ SCAFFOLD-ABSENT TRAP, called out before the run (the solver's own disclosure,
> `harmonic_balance_srs.py:800-812`).** When `term is None` the report returns
> **literal zeros** for `source_amp` / `exchange_amp` / `P_in` / `P_out` — structurally
> guaranteed, **not measured**. Two of the three idle criteria are then satisfied by
> construction and only `r_auto` carries content. **A P2 idle verdict obtained with
> `term is None` is a ONE-observable verdict and is VOID as an existence verdict**
> (§7 V4). The P2 solve must pass a **real `Termination`**.

**DISPROVE, PRE-FROZEN (G1 record §2 step 5, verbatim):** *"no source-idle solution
with a railed core exists."* The old bleeding-ambiguity cannot arise, because nothing
is held at the solution.

**The passive baselines this run is read against:** P1's measured transverse
response maps (both branches, `2026-08-24_transverse-gamma-meanstest_result.md`) and
the scalar Class-C locus (`2026-08-24_engine-gamma-meanstest_result.md`), which the
solver already reproduces to `max |ΔΓ| = 0.00129` at gate 2. Those are **response
maps of imposed gradings** — the *null* against which a self-consistent state must
show something a passive graded medium does not.

## §3 — THE EIGHT GUARDS, DISCHARGED BY NAME (epic §5; each with its receipt)

### §3.1 — GUARD 1: existence-not-emergence carve (`substrate-native-check` ckpt 8)

**The guard.** Checkpoint 8 says: on an emergence/hosting test, seed the **generative
precursor** and let the dynamics build the structure — do **not** plant the finished
composite and test persistence.

**The discharge.** This run **does** plant the finished texture, and that is legitimate
**only** because the claim is **existence, not emergence**. The three questions are
distinct (epic §1): *formation* (can the dynamics BUILD it? — **CLOSED-NEGATIVE**),
*response* (how does the medium REACT to an imposed grading? — **MEASURED**, the two
Class-C results), and *existence* (does a self-consistent stationary state EXIST under
the topological constraint? — **OPEN, this run**). A fixed-point existence question is
answered by exhibiting or failing to exhibit the fixed point; imposing the boundary
condition is the *statement of the question*, not a claimed mechanism.

**Receipt that the carve is load-bearing, not decorative:** the §1 forbidden-conclusion
list travels verbatim into the result doc, and the classification of any PROVE outcome
is fixed **in advance** as consistency-with-`clm-satnec`
(`saturation-rim-inversion.md`, claim 2, **OPEN mechanism candidate, NOT
Grant-ratified**), never emergence.

**What would VOID this guard:** any result-doc sentence using a hosting/forming verb
for the solved state; any framing in which the *imposition* is presented as an output.

### §3.2 — GUARD 2: challenge-canonical-negative CONFIG-GREP (owed, not waived)

**The guard, verbatim** (`saturation-rim-inversion.md:57`): *"no free-precursor
genesis, no `dt→0` pump ramp, impose-and-relax only"* — **grep the CONFIG, not the
conclusion.** The G1 record §5 restates the obligation and refuses the waiver: *"a
phasor-domain fixed-point solve is config-disjoint from all of them by construction —
but the grep is still owed, not waived."* The Class-C prereg's §3 is the template.

#### §3.2.1 — Closed negative A: energize-LOCK / keystone-pump (electron-genesis-from-free-precursor, LEANS-FALSIFIED, three escape hatches CLOSED)

Canonical statements of the closed path's CONFIG:
`research/2026-06-24_engine-phase-space-winding_prereg.md:12` — *"NO external drive.
This is the operational line between this test (winding-existence under lossless
evolution) and the barred self-formation (which PUMPED `H` at `dt→0`)."*;
`research/2026-06-23_engine-stage2-native-cage_prereg.md:51-56` — *"We do NOT claim
formation-from-free-precursor: that is the leaning-negative keystone-pump (the
convergence-engine coupling pumps H at dt→0)."*

| config key | CLOSED energize-LOCK path | THIS run (P2) |
|---|---|---|
| initial state | **FREE PRECURSOR** seeded to self-form | the **finished winding as a boundary condition**; nothing free, nothing seeded that could bind (and the imposition is the question, §3.1) |
| drive / pump | convergence-engine coupling; `H` **PUMPED**; pump ramp; behavior probed as `dt→0` | **a scaffold whose removability is the verdict.** The scaffold's drive is not a pump: it is required to go **idle at the solution** or the run reads DISPROVE. Delivered power `P_in` is a **computed receipt** with a declared threshold (**F10**), not an assumption |
| `dt→0` limit | **load-bearing** (the pump appears as `dt→0`) | **DOES NOT EXIST.** There is no time axis, no integrator, no `dt`, and no limit to take: the unknowns are phasors and the equations are algebraic (`harmonic_balance_srs.py` header, "No time axis") |
| time-domain trajectory | the whole content | **none** — nothing is stepped, nothing is held, nothing bleeds |
| medium↔field coupling | self-consistent **during a pumped evolution** | self-consistent **at a stationary fixed point**: `S` is a functional of the cycle-average ENVELOPE of a steady state; there is no ramp for it to ride |
| energy ledger | pumped (`H` grows) | lossless by construction (`S_u^2 = I` even when graded; `Y`-weighted energy conserved, tested to 1e-12); the **only** sink is a declared matched termination — a boundary condition, never a bulk loss term (ckpt 10) |
| claim scope | formation route | fixed-point existence; formation claims **FORBIDDEN** (§1) |

**Structural proof of non-reconstruction.** Genesis requires (**free precursor** ∧
**pump** ∧ **a time axis along which the pump acts**). This config has **none of the
three conjuncts** — the third is absent *by the nature of the phasor domain*, which is
the strongest form of disjointness available. The scaffold is the one surface on which
a reader could suspect a pump in disguise; it is closed by making scaffold-idleness the
verdict criterion itself, with computed power receipts.

#### §3.2.2 — Closed negative B: **#415** (real-space coupled static eigensolve BLED the winding; "bound eigenstate carrying both mass and winding DOES-NOT-EXIST")

Cited at `research/2026-07-01_electron-unifier-cocompress_prereg_FROZEN.md:22`;
restated in `saturation-rim-inversion.md` (the nearest *dynamical* charge-winding tests
read NEGATIVE at both loci — *"the real-space coupled eigensolve (**#415**) bled the
`(2,3)` off the bound mode"*).

| config key | #415 closed path | THIS run (P2) |
|---|---|---|
| operation | **eigensolve** of a coupled **static (DC)** operator | **harmonic-balance fixed point** at a posited AC tone set — an algebraic steady-state solve, not a spectral decomposition of a static operator |
| coordinates | **REAL-SPACE** field configuration carrying the winding | the winding is imposed as a **differential phase specification on boundary ports** — a phase-space/phasor object (guard 3, §3.3) |
| failure mode reconstructed? | the winding **bled off** the mode during the coupled solve | the winding is a **boundary condition held by the scaffold during the solve**, and the verdict is whether the *solution's own gradient* takes it over (source-idle). **A bleed here is not a repeat of #415's bleed — it is a DISPROVE reading, and it is pre-frozen as such** (§8) |
| what P2 may say about #415 | — | **nothing.** No result-doc sentence may present P2 as reopening, confirming, or explaining #415; the config differs in operation *and* coordinates |

**Non-reconstruction, stated exactly:** #415's negative is about a **static real-space
coupled eigensolve**. P2 is a **stationary phasor-domain fixed point** with the winding
entering as a boundary differential. The two share no operator, no coordinate system,
and no observable. The *shape* of a possible P2 failure (winding not sustained by the
solution) resembles #415's, which is exactly why it is **pre-frozen as DISPROVE** rather
than left available as a post-hoc "explained-away" reading.

#### §3.2.3 — Closed negative C: **#417** (phase-space winding read the LC CARRIER RATIO, not topology)

Cited at `research/2026-07-08_electron-lock-barrier_prereg.md:15`; banked from
`research/2026-06-24_engine-phase-space-winding_result.md:29` — the detuning sweep in
which *"(2,3)"* tracked `ω_b:ω_s` continuously, and the yield-front orbit read the
`(−5,−5) = (1,1)`-class, **not** `(2,3)`. Canon's reading:
*"a topological integer cannot slide."*

| config key | #417 closed path | THIS run (P2) |
|---|---|---|
| what produced the "winding" | a **measured** orbit ratio read off two coupled carriers — a continuously-slidable **carrier ratio** | the winding is **IMPOSED and FIXED** as the boundary condition; the run never reads a winding number back out as evidence of topology |
| the trap | a carrier-ratio readout was mistaken for a topological class | **structurally unavailable**: the tone ratio is a **posit** (`ToneSet`, a tuple of dimensionless numbers), so no P2 observable can be "the measured winding" |
| observable overlap | orbit-ratio readout | **none of #417's observables are constructible from this run's data**; §4's declared set contains no measured winding number |
| what P2 may say about #417 | — | **nothing.** In particular, a converged solution at the posited 3:2 tone ratio is **NOT** evidence that the lattice "selects" `(2,3)` (§1 forbidden shape 4) |

**★ The #417-shaped trap this run must not walk into, named in advance:** if a
source-idle solution is found at the posited ratio, the honest reading is *"a fixed
point exists at the imposed class"* — **not** *"the lattice produced the winding."* A
tone ratio that was put in cannot come out as a discovery. Should the solve be run at
additional ratios (not required by this prereg), a **family** of source-idle solutions
across ratios is the expected #417-consistent outcome and is **not** a defect.

#### §3.2.4 — Over-determination tell (the ½ / ¼ coincidence check)

No adjudication threshold in §8 is tuned to land on any closed negative's number, and
none of the privileged constants of the neighborhood (`α`, `√α`, `1/2`, `1/4`, `−1/3`,
`√15/4`, `1/√3`) appears as an adjudicator. `1/√3` appears only as an inherited
instrument **gate** (cold velocity factor, `ANALYTIC_NETWORK_FACTOR`), and `A = √α`
appears only as a **report-against** canonical operating point
(`resonant-lc-solitons.md:138`), never as a pass/fail. **Any P2 threshold that lands
within a factor of 2 of a canonical constant must be re-derived or re-declared before
the freeze** — a ½-or-¼ coincidence between a declared threshold and a canonical value
is the over-determination tell, not a receipt.

### §3.3 — GUARD 3: `phase-space-coordinate-check` (the transduction hazard)

**The guard.** The `(2,3)` is a **phase-space portrait** — the bond-pair tank's
Clifford-torus winding, `INVARIANT-N1`: *not* a real-space knot
(`electron-identification.md` §1 property 2, verbatim: *"The `(2,3)` 'trefoil' is the
phase-space winding pattern, NOT a real-space trefoil knot."*). A naive real-space
imposition is the exact conflation class the register's ambiguity flag and A46 police.
**The G1 walk exists because of this guard.**

**The declared coordinate map for P2 (stated before any run):**

1. The solver's unknowns `v[u, p]` **are** phasor coordinates — the incident-wave
   phasor at node `u`, port `p`. They are not real-space field samples that stand in
   for a phase; they are the phase-space variables themselves.
2. The **imposition** is a **differential phase specification across boundary ports**
   (a relative phase advance around a loop), not a real-space texture painted onto
   lattice sites. Its common-mode part is the tube phase `ϖ` and is forbidden (guard
   8, §3.8).
3. The **verdict observables** are declared per-coordinate-system in §4, and every one
   of them states which space it lives in. **The rung-crossing hazard in the geometry
   readout is called out and answered in §4(d)** — the winding's "center" is a
   phase-space object while the saturated shell is a real-space locus, and **canon
   provides no map carrying phase-space interior structure to real space** (only the
   edges project: `M` and `Q` — the ppt argument, G1 §3). §4(d) therefore declares
   only quantities that *are* defined in the space they are read in.
4. Any Γ-like readout reuses the Stage-2 declared map (multi-load de-embedded
   interface two-port in the single-Bloch-mode basis) with its reference-plane caveat:
   `|Γ|` is reference-plane invariant, `Re(Γ)` and `arg Γ` are **not**.

**Receipt:** validation note, "The coordinate map (phase-space-coordinate-check,
declared)".

### §3.4 — GUARD 4: structural-null stencil lens (the per-node-broadcast trap **and its transverse analog**)

**The guard.** A per-node-**uniform** grading **cancels identically** at the shunt
junction: in `S_ij = 2 Y_j / (sum_k Y_k) − delta_ij` a common factor in every `Y_j`
cancels, and the scatter reduces to `(2/n)J − I` **regardless of S**
(`src/ave/solvers/vacuum_varactor_scatter.py:54`, verbatim: *"A per-NODE-UNIFORM
admittance CANCELS at the shunt junction"*). **Any null obtained through a per-node
broadcast is an ARTIFACT, not a result.**

**The transverse analog, identified (Stage-1 receipts,
`src/ave/solvers/transverse_graded_scatter.py:31-47`):**

| trap | statement | the gate that catches it |
|---|---|---|
| **T1** (inherited) | per-node-uniform admittance collapses to bedrock exactly; a constant-`A` slab makes every **interior** node collapse and the response is **boundary-layer-only** | `gate_t1a_global_uniform` (collapse ≤ 1e-13) + `gate_t1b_boundary_set` (deviation set **==** the mixed-admittance node set, non-empty, max deviation ≥ 1e-3) |
| **T2** (component-space, the transverse-specific analog) | the bond has ONE impedance — loading is **component-scalar**. A **per-component** loading would smuggle un-owned **birefringent** structure into the state | `gate_so2_equivariance`: the graded step commutes with a global polarization rotation (≤ 1e-12), under **both** loading maps |
| **T3** (observable blindness) | because the graded scatter is `S_u ⊗ I_2` and commutes with global SO(2), **every polarization-angle observable is blind to the grading** — a polarization-angle null is structurally guaranteed, not measured | extraction reads port-amplitude sums on the launch component only; any polarization-angle observable is **inadmissible as evidence** |

**Discharge for P2, binding:**
- Grading is **per-directed-BOND**, never per-node-broadcast. This is asserted at
  build time and **checked**, not assumed.
- **The structural-null gate is two-sided and must CAN-FIRE in both directions:**
  (i) a deliberately per-node-uniform control must produce the exact bedrock collapse
  (the trap reproduced on purpose), and (ii) the P2 configuration must produce a
  **non-empty** deviation set at the mixed-admittance nodes. Failing (i) means the
  gate is not measuring the trap; failing (ii) means the P2 grading is invisible to
  the operator and **every P2 null is an artifact** (§7 V3).
- If the frozen carrier is transverse or two-component, **T2 and T3 bind as written**
  and no polarization-angle observable may carry evidentiary weight.

### §3.5 — GUARD 5: sector ownership, **A1 ⊥ T2**

**The guard.** The winding is **Cosserat / T2**; the mass and the `S`-railing
bookkeeping are **A1-adjacent**. The rim-inversion sector carve applies throughout, and
**no cross-wiring** of *"the defect saturates"* into *"the defect IS the mass"* is
permitted.

**The canon this run must not cross-wire (checked at authoring):**
- `def-vyvsn1` (SOLID): `V_yield` is the **transverse-T2 self-trap wall**; the
  longitudinal-A1 compliance bound is the **higher** `V_snap`. The A1 core operates
  **sub-saturated** at `A = √α ≈ 0.085`, `S ≈ 0.996` — **disk-interior**, not on the
  rim (`saturation-rim-inversion.md`; `resonant-lc-solitons.md:138`).
- Charge is the **STATIC imposed Link** (#416 two-natured ruling); mass is the
  **DYNAMICAL energy-bound A1** content. Two natures, one object, **two sectors**.
- **DP-3, Grant-ratified** (`trampoline-framework.md:255`): separate `S_μ`, `S_ε`
  kernels, **L2-sum WITHIN a grade, L∞ (first grade to `S→0`) ACROSS grades**. Under
  L∞-across-grades an A1 contribution **does not add into the T2 kernel at all**.

**Discharge, binding on the result doc:**
1. Every railing statement names **which grade / which sector** railed. "The core
   rails" without a sector label is an **inadmissible** sentence (§4(d) makes the
   per-grade profile a declared observable precisely so this is always answerable).
2. **"The longitudinal core saturates the transverse wall" is forbidden** — the
   G2 walk §8(c) records that the causation runs the other way and that DP-3's
   L∞-across-grades **forbids the proposed direction by construction**.
3. `g` (§4(c)) is explicitly a **cross-sector RATIO** — μ from the T2 winding, angular
   momentum from the Cosserat microrotation, mass in the denominator from A1. Reading
   `g` is not cross-wiring; asserting that one sector *causes* the other's saturation
   is. The distinction is stated in the result doc wherever `g` appears.

### §3.6 — GUARD 6: R40-B2a adjacency (cite, never load-bear silently)

The longitudinal-TLM-port reading on the reused n-port machinery is **DEMOTED**
(NEEDS-RE-DERIVATION, BIAS-DEBT). The stamp travels with this reuse. **What P2
load-bears:** the network/scatter algebra (`S_ij = 2Y_j/ΣY_k − δ_ij`, the certified
CONNECT permutation) and the `C_eff = C_0/S` bond-compliance reactance — nothing more.
**What P2 does NOT load-bear:** any longitudinal-port *interpretation* carried by the
demoted reading. Receipt: validation note, "R40-B2a carried"; dated note at the end of
the solver module.

### §3.7 — GUARD 7: regime / phase-state declaration (and the RESULT/ASSUMPTION line)

The house table is §0. The binding half of this guard: **the solved state's regime is
part of the RESULT, not of the assumption.** The prereg declares the *solve* to be
regime-2 self-consistent; it declares **nothing** about whether the solution is cold,
sub-railed, or railed — that is the verdict (§4(a)). Correspondingly:

- No threshold in §8 presumes railing;
- A **sub-railed** converged source-idle solution is a **fully valid, foreseen
  outcome** and is reported as such (it is the DISPROVE branch, §8);
- Per `ave-regime-phase-state-check`: **a null obtained where the effect cannot exist
  is an ARTIFACT, not a falsification.** Every null in the result doc must state the
  regime it was obtained in, and any null from a NOT-RUN or non-representable
  configuration is reported as NOT-RUN (§7 V6).

### §3.8 — GUARD 8: **ϖ-agnostic imposition** (harmonic balance posits TONES, not tube phases)

**The guard** (epic §5.8, from the frame-invariance walk): the tube phase is **NOT an
invariant of the `(2,3)` winding** — a uniform frame change preserves the ratio, and
only the **topological class** is the winding. Imposing a specific tube phase imposes
**MORE than the winding** and smuggles un-owned structure into the state.

**The discharge, stated explicitly as this prereg is required to state it:**

> **Harmonic balance posits TONES, not tube phases.** A `ToneSet` is a tuple of
> dimensionless per-step phase advances `theta_m` — *"nothing more"*
> (`harmonic_balance_srs.py:340-345`, the module's own guard-8 line). The posit is the
> **ratio 3:2**; the absolute tube phase `ϖ` is **not** an input, is **not** imposed,
> and appears **nowhere** in the frozen configuration.

**And the sharper half, from the G2 walk §1:** a **uniform** boundary specification is
**gauge** (`clm-relcnc`) — it projects nothing and the interior cannot detect it. The
scaffold does work only through the **differential**. **The common-mode part of a
source-terminated specification IS the tube phase `ϖ`**, which this guard forbids
imposing. Therefore:

- If decision 1 freezes **source-terminated**, the common mode must be **explicitly
  projected out**, and the projection is itself a **RECEIPT**: *if projecting out the
  common mode changes the solution, the scaffold was doing illegitimate work* (the
  tolerance is **F2**).
- If decision 1 freezes **injection-lock**, the guard is satisfied **by construction**
  (relative phase only) and the receipt is the cross-check in the other direction.
- Either way the run reports the **measured** common-mode sensitivity. **An unstated
  common mode is a guard-8 violation and VOIDS the run** (§7 V5).

## §4 — ★ THE DECLARED OBSERVABLE SET (every extraction method declared BEFORE any run)

**Binding rule for this section.** An observable is admissible **only** if this
document states, before the run: (i) **what** is computed, (ii) **from which
quantities of the solved state**, (iii) **in which coordinate system**, (iv) **against
what frozen criterion**, and (v) **what a null/failure of that observable means**. An
observable not fully declared here **may not be reported as evidence** — it may be
reported as an un-adjudicated observation, tagged, in an appendix.

**Declared set (six items):** (a) S-railing · (b) projected M/Q on two imposition
representatives · (c) `g` · (d) the geometry readout (per-grade real-space profiles +
defect-line locus + which-field-rails-where) · (e) the Pauli arm (a **second
configuration**) · (f) the source-idle receipt set (the existence criterion itself,
§2).

---

### §4(a) — **S-RAILING** — the named verdict

**What.** Whether the self-consistent solution's saturation field **rails** at a
localized core: `S → 0` (equivalently `A → A_yield`) on a bounded, connected locus,
with `S` recovering toward the cold value away from it.

**From what.** The converged `HBResult.S_bond` / `A_bond` fields — the DP-1
cycle-average envelope of the solution's own tone phasors, per bond
(`envelope_A_bond` → `bond_admittance`). **Not** an instantaneous snapshot
(`substrate-perspective-electron.md:62`).

**Coordinates.** `A_bond` is a **per-bond scalar on the real-space lattice**, computed
from phase-space (phasor) amplitudes. This is the one legitimate phase-space →
real-space projection in this document, because it is a **norm**, not interior
structure: `|v|` is frame-independent under the common-mode gauge and carries no tube
phase. Stated so no reader mistakes it for a transduction of the winding itself.

**Criterion.** `S_min ≤ S_rail` on a locus satisfying the frozen locality condition —
**`S_rail`, the locality condition (connectedness + bounded extent, in cells), and the
required cold-recovery margin are `FROZEN-AT-G2` (F9)**, because `A` — and hence `S`
— moves by the envelope normalization fork: the validation note's own closed-loop
receipt on the L=2 driven fixture reads `c-state → A_max 0.44007, S_min 0.89796` vs
`full-tank → A_max 0.61893, S_min 0.78544`. A railing threshold declared before that
fork is ruled would be a threshold declared in unknown units.

**Reported regardless of verdict.** The full `S`-profile, the location and extent of
`S_min`, and the cold-recovery profile — with the figure in white house style
(`ave.viz.style.apply`, Okabe-Ito, honest axes and units, legend outside the data, no
on-figure title).

**Null meaning.** A converged, source-idle, **sub-railed** solution is **not** a
failure of the run — it is the **DISPROVE** branch (§8), and it is reported with its
own `S_min` and profile, not as an absence.

---

### §4(b) — **PROJECTED M/Q ON TWO IMPOSITION REPRESENTATIVES** (decision 2, **RULED**)

**Grant, verbatim: `A2: include`.**

**Why this exists (G1 §3).** The electron is mapped to ~ppt **entirely through its
projections** (moment, charge, mass), and canon's boundary law says **only the edges
project** — the interior trace is invisible. Consequence adopted as test design:
**imposition routes are behaviorally equivalence-classed by their projections**, so
"which sector receives the imposition" has **no observable answer**. This observable
turns that *argument* into a **RECEIPT**.

**What.** The projected magnetic moment `M` and charge `Q` of the solved state, read on
**TWO different imposition representatives** of the same topological class.

**From what.** The solved state's boundary projections only — the edge quantities the
canon's boundary law permits. **Extraction is declared with the extractor** (§4(c)
shares the `M`/μ path and its unit tests). No interior quantity enters `M` or `Q`.

**Coordinates.** Boundary/edge projections — real-space integrals over the enclosing
surface of the phasor-domain solution's own currents/circulation. Declared explicitly
so the interior-structure prohibition (guard 3) is visibly respected.

**The two representatives** are `FROZEN-AT-G2` (**F7**) — they ride decision 1 (the
scaffold form determines what an "imposition representative" *is*). Binding
requirements on whatever is frozen: the two must (i) impose the **same topological
class**, (ii) differ in a way canon's equivalence argument says is unobservable, and
(iii) be **ϖ-agnostic** (guard 8) — neither may impose a tube phase.

**Frozen criteria (two, both binding):**
1. **EQUIVALENCE RECEIPT:** the two representatives' projected `(M, Q)` must agree
   within the frozen band (**F12**). Agreement = the equivalence class is a receipt.
   **Disagreement is a REAL and reportable finding** — it would mean the projections
   *do* see the imposition route, contradicting the G1 §3 equivalence argument. It is
   **not** a run failure; it is the argument failing, and the result doc says so.
2. **ppt CONSISTENCY CEILING:** any railed-core solution's projected moment must lie
   within the measured band, **or it is not describing an electron** (G1 §3 item 2).
   The band is **F12**. This is a **ceiling, not a fit**: nothing is tuned to reach it,
   and landing inside it is **consistency**, never a chord (`ave-discrimination-check`
   binds any distinctness framing).

---

### §4(c) — **`g`** (decision 4, **RULED: yes — a frozen verdict observable, with a unit-tested extractor**)

**What.** The gyromagnetic ratio of the solved state, computed as an **OUTPUT**:

> `g ≡ (μ / L_spin) · (2 m / q)` — the ratio of *how the state distributes its
> magnetic moment* to *how it distributes its angular momentum and mass*.

**From what (sector-explicit, guard 5):** `μ` from the **T2 winding** (the solved
circulation); `L_spin` from the **Cosserat microrotation** (Axiom 1: the
microrotational DOF *is* the substrate-native origin of intrinsic spin); `m` from the
**A1** content; `q` the imposed Link. **`g` is therefore a cross-sector RATIO —
reading it is not cross-wiring; asserting that one sector causes the other's
saturation is** (§3.5).

**Why it is the one criterion that cannot be argued into or out of by convention:**
`g` is a **pure dimensionless ratio**, hence **immune to every normalization fork on
the G2 list** by `clm-relcnc` (a ratio against a co-transforming reference cannot be
moved by the √2 envelope arm, the per-bond/per-node aggregation, the port-count
mapping, or the yield normalization). **`g` carries NO `FROZEN-AT-G2` blank** — and
that is exactly its value: while §4(a)'s threshold waits on decisions 1 and 3, §4(c)
is fully specified today.

**Canon status this observable moves (not a premise — the reason it is worth reading):**
canon books `g = 2` as **POSITED, not derived** — `translation-circuit.md:839`,
verbatim: *"**$g = 2$ is POSITED, not derived**"* (cite verified at `766d5179`; the
decision-set's `:637` has drifted).

#### The motivation, tagged **WALK** — the elementarity reading (NOT a premise)

> **[WALK — motivation only, un-swept, must not be used as a premise or a criterion.]**
> The attractive *"g=2 is the SU(2) double cover"* derivation is **RETRACTED with a
> decisive falsifier** (`electron-identification.md:92`, Rule-12 re-scope 2026-06-21,
> verbatim): *"the proton ($g_p \approx 5.586$) and neutron ($g_n \approx -3.826$) are
> also spin-½ and also carry the same $4\pi$ double-cover — yet $g \neq 2$. A ratio
> that equals 2 for every spin-½ particle cannot select $g = 2$ for the electron."*
> What the falsifier *teaches* is that **`g = 2` tracks ELEMENTARY, not spin-½**: it
> must come from what the electron has and the proton does not — the proton is
> **composite**, with charge and mass distributions that **differ**. That reading is
> the **motivation** for §4(c)'s SPLIT control below. It is **WALK-grade**, it has not
> passed the 6-question sweep gate, and **no verdict in §8 may rest on it**.

#### The extractor, and its **TWO mandatory controls** (both land as unit tests BEFORE the run)

The extractor is a **unit-tested** function (decision 4's own condition). It ships with
its tests **before** the P2 run, and the tests are **can-fire** tested in both
directions (a deliberately wrong input must fail them).

**CONTROL 1 — `g = 1` on identical distributions (the anti-Dirac-smuggling control).**

> The extractor **MUST return `g = 1`** for a configuration whose **charge and mass
> distributions are identical**.

That is the classical content of `g`: a body whose charge is distributed exactly as its
mass rotates with `μ/L = q/2m`, i.e. `g = 1`. **If the extractor returns `2` for that
fixture, Dirac's factor has been smuggled into the machinery** and every `g` the run
reports is an artifact of the extractor rather than a property of the solved state.
This control is an **analytic fixture with a closed-form answer** — it does not require
the P2 solve, it gates it. **Failing CONTROL 1 VOIDS every `g` reading** (§7 V7).

**CONTROL 2 — the SPLIT (the machinery-vs-physics discriminator).**

> The solve **must SPLIT**: **`g = 2` for a single-tank winding**, and **`g ≠ 2` for a
> multi-tank composite**.

**Stated as bluntly as it must be:**

> **A solve returning `2` for BOTH, or `2` for NEITHER, is a FAILED TEST OF THE
> MACHINERY — not a physics result.**
>
> - `2` for **both** ⇒ the extractor is insensitive to the distribution difference
>   that is the entire classical content of `g` (it is reporting a constant, and the
>   constant is the number canon *posits* — the worst possible failure mode, because
>   it looks like success).
> - `2` for **neither** ⇒ either the imposition, the extractor, or the solve is not
>   representing the winding's moment at all, and the run has no `g` content.
>
> In **both** cases the result doc reports **"machinery failure on the `g` axis"**,
> reports the numbers, and draws **no** physics conclusion in either direction. This is
> pre-frozen precisely so that a post-hoc reading cannot convert a machinery failure
> into a verdict.

**And the honest reading if the SPLIT does occur.** `g = 2` from the single-tank arm
and `g ≠ 2` from the composite arm is a **kill either way** and *how* it misses says
**which** thing failed — *"the identification, the imposition, or the machinery"*
(decision 4, reason iii). It is **consistency with canon's posited value plus a
derivation path**, and it must be graded by `consistency-vs-emergence` and
`ave-discrimination-check` before any word stronger than "computed, not posited"
attaches to it. **Deriving a posited number is not a chord** (§1 forbidden shape 5).

**Reported regardless:** `μ`, `L_spin`, `m`, `q`, their extraction receipts, `g` per
arm, both controls' outputs, and the can-fire receipts.

---

### §4(d) — ★ **THE GEOMETRY READOUT** (stated in the answerable form)

#### The rung-crossing, named first

The naive question — *"where in the lattice is the winding's center, and does the
saturated shell sit around it?"* — **is not answerable and must not be asked**:

- the winding's **"center" is a PHASE-SPACE object** (the defect of a phasor
  portrait), while
- the **saturated shell is a REAL-SPACE locus** (a set of bonds with `S → 0`), and
- **canon provides no map carrying phase-space interior structure to real space** —
  **only the edges project** (`M` and `Q`; the ppt argument, G1 §3, and the P0
  transduction pull's finding).

Asking for "the real-space position of the phase-space center" crosses a rung with no
bridge under it. **What follows is the answerable form**: quantities that are each
well-defined **in the space they are read in**.

#### (d1) — **Per-grade real-space profiles `S_μ(r)`, `S_ε(r)`**

**What.** The solved state's **separate per-grade** saturation profiles as functions of
real-space distance `r` from the **defect line** (defined in d2).

**Why per-grade and not a single `S`.** DP-3 (Grant-ratified,
`trampoline-framework.md:255`): the kernel acts on the **per-yield-normalized** strain
**in each grade**, with **separate `S_μ`, `S_ε` kernels** — **L2-sum within a grade,
L∞ (first grade to `S→0`) across grades**. A single lumped `S(r)` would erase exactly
the structure guard 5 requires the run to keep visible. **If the frozen carrier
(F7) represents only one grade, `S_μ(r)` / `S_ε(r)` collapse to that grade's profile
and the other is reported as NOT-REPRESENTED** — never as zero, never as "no railing
in that grade" (§7 V6).

**From what.** The converged per-bond envelope fields, binned by real-space distance
from the defect line; profiles reported with their binning and their per-bin counts.

#### (d2) — **Where the imposed phase texture's DEFECT LINE sits in the solved real-space field**

**What.** The real-space locus of the **imposition's own defect line** — the set of
bonds/ports where the *imposed* phase specification is singular (undefined phase). This
**is** well-defined without any phase-space→real-space transduction, because the
imposition map is *authored* on real-space ports: the defect line is a property of the
boundary condition the run itself writes down.

**Declared as:** the defect-line locus **as constructed by the imposition map** (an
input receipt, printed, not inferred), overlaid with **where the solved field's
per-grade profiles do what they do**. The observable is the **relationship between an
input locus and an output profile** — not a claim that the phase-space center "is" at
that place.

#### (d3) — **WHICH field rails, and WHERE** (stated explicitly, as the task requires)

**What.** For the solved state: **which grade** (`μ` / `ε` / the represented channel)
reaches its rail, **at which real-space locus**, and **at what distance** from the
defect line — reported as a labeled statement, never as an unlabeled "the core rails".
If **no** field rails, that is the reported answer (DISPROVE branch), with the per-grade
minima and their loci.

#### (d4) — **The TWO RIVAL EXPECTATIONS** (frozen before the run, so the run discriminates)

| | **RIVAL 1 — the standard-vortex resolution** | **RIVAL 2 — canon's `clm-satnec` proposal** |
|---|---|---|
| what happens to the amplitude at the core | **amplitude → 0**: the field vanishes at the phase singularity, the ordinary way a vortex resolves an undefined phase | **amplitude → yield**: `A → A_yield`, the response **rails** |
| what happens to the kernel | `S(A) → 1` (cold interior) | **`S → 0`** |
| what happens to the local clock | nothing — `c_eff → c` | **freezes**: `c_eff = c·√S → 0` — *"stable because it is static"* (`genesis-chord-falsification-ledger.md:145`, via `saturation-rim-inversion.md:39`) |
| topological consequence | the `A → 0` **unwinding channel is OPEN**; the interior confers **no protection** | amplitude freeze-out **removes** the unwinding channel; the winding is **maximally protected** on the rim |
| canon status | the generic-medium expectation | **`clm-satnec`, OPEN mechanism candidate, NOT Grant-ratified** — *"the lattice cannot smoothly carry a phase singularity, so the amplitude response rails … the saturated core is the lattice's RESOLUTION of the singularity"* |

**THE DISCRIMINATOR, frozen:** the **sign of `dA/dr` approaching the defect line**, and
the **value of `A` at the innermost admissible bin** relative to `0` and to
`A_yield`. Rival 1 predicts `A → 0` (monotone **decreasing** inward); Rival 2 predicts
`A → A_yield` (monotone **increasing** inward, `S → 0`). These are **opposite limits of
the same measured profile** — which is why (d1) is the observable and not a lumped
scalar.

**Foreseen third outcome, pre-recorded so it is not read as either rival:** a profile
that is **neither** monotone-in nor monotone-out — e.g. a ring/annulus extremum, or a
railing locus displaced from the defect line. That is a **real finding about the graded
medium**, is reported as the measured profile with **no** rival label attached, and
adjudicates the rival fork as **NEITHER** (§8).

**Non-adjudicators, stated in advance:** the *magnitude* of `S_min` versus any
canonical constant (`√α`, `0.996`, …) adjudicates **nothing** — it is a
report-against number only; and the *quantitative* profile shape is not compared to any
lumped cartoon.

---

### §4(e) — **THE PAULI ARM** (declared as a **SECOND CONFIGURATION**, not a second verdict)

**Framing correction carried in (do not re-litigate).** The "two defects" framing is
**RETIRED as ill-posed** — topological charge simply **adds**, so "two defects" is not a
distinct configuration from "one defect of charge 2". **The question is ONE
configuration's internal structure.**

**The question, stated in the answerable form:**

> Can **ONE self-consistent configuration** carry **two units of winding in the SAME
> grade**, versus **one unit in each of two grades**?

**Two configurations, run and reported as a pair:**

| arm | configuration | DP-3 frozen expectation |
|---|---|---|
| **SAME-GRADE** | two units of winding loaded into **one** grade | **CO-SATURATION**: L2-sum **within** a grade — the two units' normalized strains add in quadrature against **one** yield, so the shared kernel is driven harder than either alone |
| **DIFFERENT-GRADE** | one unit in each of **two** grades | **NO co-saturation**: L∞ **across** grades — the grades do **not** sum, so neither loads the other's kernel at all |

**Receipt for the expectation** (`trampoline-framework.md:255`, Grant-ratified DP-3,
verbatim): *"**separate $S_\mu, S_\varepsilon$ kernels** — L2-sum *within* a grade, L∞
(first grade to $S\to0$) *across* grades."*

**Extraction (declared).** For each arm: the per-grade profiles of §4(d1) plus the
**per-grade `S_min`** and the **loaded-grade identity**. The comparison is
**within-arm-across-grades** and **across-arms-at-matched-loading**; the co-saturation
statement is the **measured** difference in per-grade `S_min` between the two arms, not
an inference from the combine rule. The matched-loading definition is `FROZEN-AT-G2`
(**F13**), with the carrier's grade-representability (F7).

**★ WHAT THIS ARM TESTS — and, precisely, what it does not.** It tests **canon's own
OPEN item**, quoted verbatim (`form-deriving-value-importing.md:220`):

> *"the dynamical selection of the antisymmetric sector (**exclusion enforcement**)
> stays **OPEN**"*

— i.e. canon **derives the braid's sign** (`σ = −I`, FR two-loop braid, #315, at
PEER-ahead) and does **NOT** derive the **enforcement**. The Pauli arm is therefore
**not a competitor to the FR-braid treatment**; it probes the **open enforcement half**,
for which Op9 (`operators.md:49`, *"Γ_steric → −1 (Pauli-level overlap → impedance
divergence)"*) and Op4 (`operators.md:44`, the three-regime `Z(r)` with a **Pauli**
regime) already supply the repulsion side in canonical operator form.

**THE OBSTACLE, carried in so the result cannot overclaim** (G2 walk §8(d), the sharp
one): **Pauli is spin-dependent and state-based, not spatial.** Opposite-spin electrons
overlap *completely* in one orbital and are **allowed**; same-spin are not. **A
spin-blind capacity mechanism excludes both, so capacity alone CANNOT be Pauli.** The
candidate repair — DP-3's per-grade kernels making capacity spin-dependent **if spin
maps to grade** — carries its own counter-tension: **PR#260 ruled the μ-vs-ε fork
DEGENERATE on equilibrium observables** (a sign selector), which **cuts against** the
two spin states loading different grades. **That tension is un-walked. This arm does
not resolve it and may not claim to.**

**Frozen reading rules for this arm:**
1. A measured co-saturation split in the predicted direction is **consistency with
   DP-3's ratified combine rule** — it is **not** a derivation of Pauli exclusion, not
   an enforcement mechanism, and not a chord.
2. **No spin claim may be attached** to either arm's result. "Grade" is not "spin"
   until the #260-degeneracy walk rules it so.
3. **Absence of the predicted split is informative and is reported as such** — it
   would put pressure on the ratified combine rule at this operating point, which is a
   finding worth having (DP-3 itself records the cross-grade combine as an **open
   discriminator, degenerate to `O(α)` at the electron** — so a **non-α-suppressed**
   operating point is what would settle it; whether this run's operating point is
   α-suppressed is **itself a reported quantity**, not an assumption).
4. If the frozen carrier cannot represent two grades, **this arm is NOT-RUN** and is
   reported as NOT-RUN (§7 V6) — a structurally-guaranteed null here would be exactly
   the guard-4 artifact class.

---

### §4(f) — **THE SOURCE-IDLE RECEIPT SET** (the existence criterion, §2)

`source_amp`, `exchange_amp`, `P_in`, `P_out`, `P_net`, `r_auto` — per tone and
aggregated — plus the `idle_verdict` booleans against the declared thresholds (**F10**).
Reported in full for **every** solve, converged or not. Binding: a real `Termination`
must be present (§2's scaffold-absent trap; §7 V4), and the common-mode projection
receipt (§3.8, **F2**) is reported alongside.

## §5 — `FROZEN-AT-G2` PLACEHOLDERS (blank; **13** items)

**Rule.** Every blank below is filled **verbatim from the G2 ruling**, with the ruling
quoted and dated. **The prereg is not frozen, and no P2 run may execute, while any
blank remains** — except **F5**, which is *conditional* and is filled with
`MOOT (F4 = per-BOND)` if that is how F4 rules. **The author of this skeleton is
firewalled and does not know the values of decisions 1 and 3.**

**Provenance of the decision set (read before filling anything):** the G1 walk record
§4 lists **two** residual choices and the epic (`:112`) and build brief (`:69-71`) both
say **"two"** — those counts are **STALE**. The authoritative list is **four**:
`_orchestration/open-items/2026-08-25-g2-freeze-decisions.md`, with the envelope fork's
sub-structure in the validation note's "G2 FREEZE — the decision list this stage hands
up".

| # | placeholder | depends on | value |
|---|---|---|---|
| **F1** | **Scaffold form** — source-terminated boundary phasors with the common mode explicitly projected out, **vs** injection-lock; and which is the cross-check | **decision 1** | `FROZEN-AT-G2: ______` |
| **F2** | **Common-mode projection operator + its receipt tolerance** — the "if projecting out the common mode changes the solution, the scaffold was doing illegitimate work" threshold (guard 8) | decision 1 (F1) | `FROZEN-AT-G2: ______` |
| **F3** | **Envelope ARM** — DP-1 C-state vs DP-3 full-tank (**exactly √2 in A**; canon flags the full-tank normalization *"review-on-merge"*, `substrate-perspective-electron.md:87`) | **decision 3a** | `FROZEN-AT-G2: ______` |
| **F4** | **Envelope AGGREGATION** — per-BOND 2-port sum vs canon's per-NODE per-cell aggregate (`√(z/2) = 1.2247` on a uniform field; **content-dependent** in general) | **decision 3b** | `FROZEN-AT-G2: ______` |
| **F5** | **Port-count mapping**, *conditional on F4 taking the per-NODE arm* — canon writes the row on the K4 node's **4** ports (`substrate-perspective-electron.md:31`) while the srs carrier's node degree is **3** (sum the 3 incident ports / re-derive the χ²-of-N normalization for z=3 / reject the srs carrier for this row) | decision 3b′ | `FROZEN-AT-G2: ______`  *(or `MOOT` if F4 = per-BOND)* |
| **F6** | **Collapse-check outcome** — the cheap, un-run gating sub-task: are the √2 envelope fork and the storage-α vs response-α contour fork (`A²=α` vs `A²=2α`, *"near-colliding, Δ = 1.4×10⁻⁵"*, `cvr-reflection-smith.md:49-55`) **the same fork seen twice**? If they collapse, one ruling settles both | decision 3 (gating) | `FROZEN-AT-G2: ______` |
| **F7** | **Carrier + the TWO imposition representatives** — which engine channel runs (scalar `srs-z3` phasor path / a transverse phasor path that does not yet exist / other), and the two representatives of the imposed class for §4(b); **plus the grade-representability statement** that §4(d1) and §4(e) consume | decision 1 (F1) | `FROZEN-AT-G2: ______` |
| **F8** | **Tone-set numeric values** — the base `theta` in rad/step for the frozen **3:2** ratio, both tones inside the canonical open interval `(0, π)` and well-separated (the cross-term averaging horizon scales as `1/|θ₁−θ₂|`), placed in the carrier's linear band | F7 | `FROZEN-AT-G2: ______` |
| **F9** | **`S_rail` threshold + locality condition + cold-recovery margin** for §4(a) | F3/F4 (the envelope moves `A`, hence `S`) | `FROZEN-AT-G2: ______` |
| **F10** | **Source-idle thresholds** — `source_tol`, `exchange_tol`, `r_auto_tol` for `idle_verdict` | F1 (scaffold form sets what "idle" measures) | `FROZEN-AT-G2: ______` |
| **F11** | **Net size / geometry / fit margins / iteration budget** — `L`, enantiomorph, defect-line placement and wrap margins, evanescent fit margins, outer-loop `relax` and `outer_tol`, hard step/iteration caps | F7 | `FROZEN-AT-G2: ______` |
| **F12** | **M/Q projection normalization + the equivalence band + the ppt consistency-ceiling band** for §4(b) | F3/F4 (normalization), F7 (representatives) | `FROZEN-AT-G2: ______` |
| **F13** | **Pauli-arm configurations** — the SAME-GRADE and DIFFERENT-GRADE loadings and the matched-loading definition (or `NOT-RUN` with the representability reason, per §7 V6) | F7 | `FROZEN-AT-G2: ______` |

**Deliberately NOT frozen-at-G2 — stated so the freeze does not invent a blank:**
**`g` (§4(c)) and both of its controls carry no placeholder.** `g` is a pure
dimensionless ratio and is **immune to F3/F4/F5 by `clm-relcnc`**; `g = 1` on identical
distributions is an **analytic** control; the SPLIT is a **qualitative** criterion. This
is the observable that cannot be argued into or out of by convention — and it is fully
specified today.

## §6 — INSTRUMENT + SANITY GATES (run FIRST; the run is VOID if any fails)

Inherited from the Stage-2 validation and re-run **on the P2 configuration itself** —
a gate that passed on a different fixture is not a gate on this run.

- **IG-1 — cold linear limit:** the P2 net's cold velocity factor matches
  `ANALYTIC_NETWORK_FACTOR = 1/√3` within the frozen tolerance, and the fitted `k`
  sits on the analytic arccos band (`nearest_band_theta`). **Honest resolving power,
  carried in from the validation note:** this gate needs a systematic `k` error of
  **~0.50 %** at the top of the sweep and **~2.0 %** at the bottom before it fires —
  the `4.2e-9` headline is agreement on the run of record, **not** a `1e-9`
  discriminator. Quote it that way or not at all.
- **IG-2 — response-map re-anchor:** at the P2 tones, the single-tone graded limit
  reproduces the **measured** Class-C locus within the frozen band. Carried caveats:
  the comparison target is the **matched-filter** column (`gamma`), not the energy
  cross-check (`gammaE`) — the choice is load-bearing at `A = 0.3`; and the `0.010`
  absolute floor **swamps the low-`A` end** (a solver returning `Γ ≡ 0` would clear
  `A = 0.3`), so the load-bearing content is `max |ΔΓ|` and the **large-|Γ| end**.
- **IG-3 — source-idle machinery, can-fire in both directions:** a driven cold tank
  reads **not-idle** and an initialized lossless ring reads **idle** — with the
  **scaffold-absent asymmetry stated** (the ring's two zeros are structural; only
  `r_auto` carries content there, §2).
- **IG-4 — structural-null gate, two-sided (guard 4):** the per-node-uniform control
  reproduces the exact bedrock collapse **and** the P2 grading produces a non-empty
  deviation set at the mixed-admittance nodes.
- **IG-5 — losslessness / Ax3 receipt:** the `Y`-weighted energy ledger and the
  scatter's `S_u² = I` property hold to the frozen tolerance on the P2 configuration;
  **no damping device exists anywhere in the operator** (asserted **and** checked).
- **IG-6 — `g`-extractor controls (§4(c)):** CONTROL 1 (`g = 1` on identical
  distributions) passes on its analytic fixture, and both controls are **can-fire**
  tested (a deliberately wrong input fails them).
- **IG-7 — convergence receipts:** per-tone fixed-point residual `residual_rel`, the
  outer-loop `dA_inf` history, and `converged` flags — reported, with the frozen
  tolerances (**F11**).

**Any IG failure ⇒ the ENTIRE run is VOID** (§7 V1). No P2 observable may be
interpreted, in either direction.

## §7 — VOID CONDITIONS (the run is null and interprets NOTHING)

- **V1 — Instrument/sanity fail:** any IG-1…IG-7 failure (§6).
- **V2 — Non-convergence presented as a verdict:** a non-converged solve is **NOT** a
  DISPROVE. If the fixed point does not converge to the frozen tolerances, the run is
  **INCONCLUSIVE on existence** and says so; the DISPROVE branch requires a
  **converged** solve (§8).
- **V3 — Structural-null artifact (guard 4):** the P2 grading produces an **empty**
  deviation set at the mixed-admittance nodes (the grading is invisible to the
  operator), or any null is obtained through a per-node broadcast. Every null in the
  run is then an artifact.
- **V4 — Scaffold-absent idle verdict (§2):** an idle verdict computed with
  `term is None`. Two of three criteria are then satisfied **by construction** and the
  verdict is a one-observable verdict — **VOID as an existence verdict**.
- **V5 — Guard-8 violation:** a tube phase imposed, or the common-mode projection
  receipt (**F2**) not reported. An unstated common mode voids the run.
- **V6 — NOT-RUN reported as a null:** any statement that a sector, grade, or arm the
  frozen carrier cannot represent returned a null result. Non-representable ⇒
  **NOT-RUN**, reported as NOT-RUN, with the representability reason (F7).
- **V7 — `g`-extractor failure:** CONTROL 1 returns anything but `g = 1` on the
  identical-distribution fixture ⇒ **every `g` reading in the run is VOID**. (CONTROL
  2 failing is **not** a VOID — it is the declared **machinery-failure** verdict on the
  `g` axis, §4(c), and the rest of the run survives.)
- **V8 — Freeze breach:** the run executes against a document with an unfilled `F`
  blank (other than a `MOOT` F5), or the executed configuration differs from the frozen
  one without a dated **AMENDMENT** entry in the result doc.
- **Per-observable INVALID-EXTRACTION** voids **that observable only**; the run
  survives for the others, and the invalidation is reported with its receipt.

## §8 — ADJUDICATION RULES (a verdict follows MECHANICALLY)

Evaluated **in order**. Each step consumes only §4/§6 computed quantities and §5 frozen
values. **No verdict may be stated in language other than the rows below** until G3
adversarial verify (≥3 lenses) has run to convergence.

**Step 0 — Validity.** Any V1…V8 ⇒ **VOID**. Stop.

**Step 1 — Convergence.** Not converged to the F11 tolerances ⇒ **INCONCLUSIVE ON
EXISTENCE** (V2). Report residuals and history. Stop.

**Step 2 — Source-idle.** Compute `idle_verdict` against F10, with a real
`Termination` and the F2 common-mode receipt reported.

**Step 3 — Railing.** Compute `S_min` and the locality condition against F9, **per
grade** (§4(d1)).

**Step 4 — The existence verdict (the frozen table):**

| idle (step 2) | railed (step 3) | **VERDICT** |
|---|---|---|
| **idle** | **railed** | **EXISTS-RAILED** — a source-idle, self-consistent AC steady state with a railed core exists at the imposed class. This is the **PROVE** branch: **first direct evidence for the topological route `clm-satnec`**, at **consistency** grade, on the model's own claims. Not emergence, not formation, not a chord (§1). |
| **idle** | **sub-railed** | **EXISTS-UNRAILED** — a source-idle state exists but does **not** rail. The pre-frozen DISPROVE condition (*"no source-idle solution with a railed core"*) is **met**: the topological route is **disfavored**, `clm-satnec` demotes, and the **dynamic** route (`resonant-lc-solitons.md:142`) carries the existence question alone. |
| **not idle** | any | **NO-AUTONOMOUS-SOLUTION** — the scaffold cannot be removed; the state is scaffold-sustained, not self-clamped. **DISPROVE** on the pre-frozen criterion. The scaffold's residual `P_net` and `r_auto` are reported as the measure of *how far* from autonomous. |

**Step 5 — The equivalence receipt (§4(b)).** Representatives agree within F12 ⇒
**EQUIVALENCE-RECEIPTED**. Disagree ⇒ **EQUIVALENCE-REFUTED**, reported as a finding
about the G1 §3 argument, **not** as a run failure; the step-4 verdict stands but is
qualified as representative-dependent and names which representative produced it.

**Step 6 — ppt consistency ceiling (§4(b)).** A step-4 **EXISTS-RAILED** whose projected
moment falls **outside** the F12 band ⇒ the verdict stands as an existence statement
but is stamped **NOT-ELECTRON-CONSISTENT**; no electron identification may be attached
(G1 §3 item 2). Inside the band ⇒ **CEILING-CONSISTENT** — consistency, never a chord.

**Step 7 — the `g` axis (§4(c)), adjudicated INDEPENDENTLY of steps 4–6:**

| CONTROL 1 | SPLIT (CONTROL 2) | **`g` VERDICT** |
|---|---|---|
| fails | any | **VOID on the `g` axis** (V7) |
| passes | `g = 2` single-tank **and** `g ≠ 2` composite | **SPLIT-OBSERVED** — `g` computed, not posited, at consistency grade; *how* it lands is reported per arm |
| passes | `2` for **both**, or `2` for **neither** | **MACHINERY FAILURE ON THE `g` AXIS** — numbers reported, **no physics conclusion in either direction** |
| passes | any other pattern (e.g. `g ≠ 2` single-tank, `g = 2` composite) | **`g`-AXIS KILL** — reported with the miss pattern, which says whether the identification, the imposition, or the machinery failed; **which** it says is an **adjudication for G3**, not a claim this run may make |

**Step 8 — the geometry fork (§4(d4)):** `A → A_yield` / `S → 0` inward ⇒
**RIVAL-2 (`clm-satnec`-shaped)**. `A → 0` / `S → 1` inward ⇒ **RIVAL-1
(standard-vortex-shaped)**. Neither (non-monotone, annular, or displaced railing) ⇒
**NEITHER**, reported as the measured profile with no rival label. **This step is
labelled "-shaped" deliberately: a profile matching a rival's shape is consistency with
that reading, not a demonstration of its mechanism.**

**Step 9 — the Pauli arm (§4(e)), reported as a PAIR and never as a verdict on Pauli:**
**CO-SATURATION-SPLIT-OBSERVED** (same-grade co-saturates, different-grade does not) /
**NO-SPLIT** / **NOT-RUN** (F7 representability). All three are read under §4(e)'s
frozen reading rules — no spin claim, no exclusion-enforcement claim, and the
α-suppression status of the operating point reported alongside.

## §9 — ENGINEERING-CHOICE REGISTER (every non-lattice-derived parameter)

| # | parameter | status |
|---|---|---|
| E1 | net size / enantiomorph / geometry / wrap + fit margins | **F11** — engineering, recorded, not substrate-derived |
| E2 | tone base value (the **ratio 3:2** is the posit; the base is placement) | **F8** |
| E3 | outer-loop `relax`, `outer_tol`, iteration/step caps | **F11** |
| E4 | `S_rail`, locality condition, cold-recovery margin | **F9** — *must* be re-checked against §3.2.4's over-determination tell once F3/F4 rule |
| E5 | idle thresholds `source_tol` / `exchange_tol` / `r_auto_tol` | **F10** |
| E6 | common-mode projection tolerance | **F2** |
| E7 | M/Q equivalence band + ppt ceiling band | **F12** |
| E8 | IG-1/IG-2 tolerances (velocity %, band edge, `ΔΓ` floor + relative band) | inherited from the Stage-2 gates as **ENGINEERING-CHOICE**, re-declared at the freeze with the same rationale (instrument null floors + the two estimator classes' spread) |
| E9 | `A_cap` / `S_min` kernel floor conventions | inherited canonical kernel caps; **dormant only if the P2 grid stays inside them** — if the solved `A` exceeds the cap the caveat becomes live and must be reported, not clipped silently |
| E10 | binning for the §4(d1) radial profiles | declared at the freeze with per-bin counts reported |
| E11 | impedance map `z_b = √S(A_b)` | **NOT an engineering choice** — the shared canonical map (`cvr-reflection-smith.md` §2 via `ave_chart.py`); flagged here so nobody mistakes this run for an adjudication of the map's exponent (it is not) |

## §10 — REPORTING REQUIREMENTS (binding on the run agent) + THE FREEZE CHECKLIST

1. The **RESULT doc is this prereg's pair**; **this file is never edited after the
   freeze.** Every departure is a dated **AMENDMENT** entry in the result doc.
2. The result doc restates §1's forbidden-conclusion list **verbatim** in its scope
   block, and states the §0 house table for the run as executed.
3. Every §4 observable is reported **whether or not it supports a verdict**, with its
   extraction receipt, and every verdict is quoted from §8's tables **verbatim** —
   frozen-criterion-only language until G3.
4. Figures: white house style via `ave.viz.style.apply`, Okabe-Ito, honest axes **with
   units**, legend outside the data, no on-figure title.
5. Raw data, the driver, the receipts JSON, and a standalone **gating number-checker**
   land with the result (the Class-C / Stage-2 pattern); each gate **COMPUTES** its
   pass — **reconcile-don't-declare**: a gate consuming a self-declared field is a
   checklist, not a gate.
6. **Stop-and-ask:** a physics surprise is a **STUCK-POINT**, not a judgment call.
   Two-attempt cap, then a STUCK-POINT report to Grant — never an improvised
   re-framing mid-run.
7. **G3 gate:** adversarial verify (≥3 lenses — config compliance **re-grepped on the
   actual solver invocation**; physics/coordinates including the sector-ownership read
   on any railed solution; independent numerics rerun), then the
   **repairs-need-reaudit** loop to convergence. **A repaired result is not a verified
   result.** P3 propagation fires only behind G3, via its own reviewed PR.

**FREEZE CHECKLIST (all must be true before this document is renamed `_FROZEN` and any
run executes):**

- [ ] All four G2 decisions ruled, each ruling quoted **verbatim** and dated in §5.
- [ ] All 13 `FROZEN-AT-G2` blanks filled (F5 may read `MOOT`).
- [ ] The F6 collapse-check has been **run** (it is cheap and un-run at authoring), and
      its outcome recorded — including whether it collapses the contour fork.
- [ ] The `g` extractor **exists**, is **unit-tested**, and CONTROL 1 + the can-fire
      tests are **green** (IG-6) — before the P2 run, not after.
- [ ] The carrier (F7) is named, its **grade-representability** stated, and every
      non-representable arm marked **NOT-RUN** rather than left to produce a null.
- [ ] Author firewall intact: no P2 number appears anywhere in this document.
- [ ] Every threshold re-checked against §3.2.4's over-determination tell.

— END OF PREREG SKELETON (NOT YET FROZEN) —
