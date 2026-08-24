# External-Solver Cross-Check — Phase-0 Trade Study (DECISIONS: OPEN)

**Date:** 2026-08-24 · **Lane:** external-solver cross-check, Phase 0 (implementer) · **Status:** DECISION RECORD, not a claim. Every trade ends **STATUS: OPEN**. **SELECTS NOTHING.** Cost is out of scope.

**Epic this executes:** [`_orchestration/2026-08-23_external-solver-crosscheck-epic.md`](../_orchestration/2026-08-23_external-solver-crosscheck-epic.md) §6. The epic's leanings are reproduced verbatim in each trade and are **leanings, not rulings**.

**Sibling docs.** Derived physics lives in [`research/2026-08-24_solver-crosscheck-phase0_requirements.md`](2026-08-24_solver-crosscheck-phase0_requirements.md) (the `SCX-REQ-*` datasheet) — **cite-don't-duplicate**: no derived number is restated here. The frozen Phase-1 prereg skeleton is [`research/2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md`](2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md).

> **★ Binding epistemic frame (`SCX-REQ-FRAME`; stated in full in the requirements datasheet §0, cited here by ID).** This epic is **IMPLEMENTATION-VERIFICATION**, a sub-class of CONSISTENCY. Two integrators agreeing on the same network validates that the engine solves its own equations correctly. **No trade below serves an AVE confirmation, and no phase of this epic can confirm or falsify AVE.**

> **★ Binding scope fence (`SCX-REQ-FENCE` F3, from [`srs-band-structure.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)).** **SCALAR / TRANSLATIONAL CHANNEL ONLY.** The scalar band top is closed-form and its leaf section carries no demotion marker. The vector/Cosserat channel's top is a live bracket whose upper arm is itself DEMOTED (R40 batches 1/2a) and gated on a PENDING-Grant ruling — **no stable reference number, therefore no test**. Every option in every trade below is scoped to the scalar channel; a vector-channel variant of any option is out of scope by construction, not merely un-preferred.

---

## Decision summary (all OPEN)

| # | decision | whose call | lane recommendation |
|:--|:--|:--|:--|
| **T1** | Solver | lane, ratified by Grant | **ngspice first**; Xyce deferred to the §5.3(b) second-solver arm, not procured now |
| **T2** | **Bond representation** | **★ GRANT (physics-adjacent)** | **lossless TL element per bond** (the epic's leaning, and the substrate walk agrees) — **but see T2.4: the choice silently carries an $\omega_C$-label consequence, which is why it is Grant's** |
| **T3** | Graph source | lane | **engine's own adjacency export** |
| **T4** | Observable extraction | lane | **`.AC` driving-point / two-port response**; transient ringdown NOT recommended without T6 native units |
| **T5** | Where results live | standing convention | `research/` prereg+result pair per phase — **no decision needed** |
| **T6** | *(lane-surfaced addition)* Units / scaling of the emitted netlist | lane | **native/normalised emission with an SI round-trip check** — and this becomes near-mandatory if T4 selects transient |

**T2 is the Phase-1 GO gate** (epic §4 Phase-0 GATE: *"Grant ratifies the trade-study decisions marked his"*).

---

## T1 — Solver

**Builds to REQ-IDs:** `SCX-REQ-ELEMENTS` (whatever solver is chosen must accept the canonical values without rescaling), `SCX-REQ-FENCE` F1 (the solver is continuous-time; the engine is not).

**Epic leaning (verbatim):** *"ngspice first (ubiquitous, scriptable); Xyce as the second-solver arm of §5.3b"*.

**Options:**

- **(a) ngspice.** Ubiquitous, scriptable, batch-mode with a `.control` block, free. **Locally present and probed this session: ngspice-46, `/opt/homebrew/bin/ngspice`, compiled with the KLU direct linear solver.**
- **(b) Xyce.** Sandia's parallel SPICE; the natural second integrator for the epic's §5.3(b) *"and where available a second solver"* clause. **Not installed on this box** (`which Xyce` / `which xyce` → not found). Procuring it is a build/install step this lane did not take and does not recommend taking at Phase 0.
- **(c) Both from the start.** Maximum independence, doubled setup and doubled netlist-dialect surface.

**Feasibility probed this session (T1/T6 de-risking; scratch only, not tracked code, not a Phase-1 result).** A single lossless bond exported as an ngspice `T` element — $Z_0=376.73031346177066$, $\mathrm{TD}=7.436783388682972\times10^{-22}$ s (the `SCX-REQ-LABEL` R2 delay) — open at both ends, driven by a unit AC current source, swept `.ac lin 40001 6.0e20 7.5e20`:

| probe | result |
|---|---|
| **SI-scale `.AC`** | resonance peak at $f=6.72334\times10^{20}$ Hz. Closed-form prediction $1/(2\,\mathrm{TD})=6.7233\times10^{20}$ Hz. **Agrees to within the sweep grid step** ($3.75\times10^{15}$ Hz, $5.6\times10^{-6}$ relative). No special options, no tolerance overrides, no convergence warnings. |
| **Native-scale `.AC`** (same network, $Z_0=1$, $\mathrm{TD}=1$) | resonance peak at $f=0.500000$ Hz vs predicted $0.5$ ✓ |
| **SI-scale `.TRAN`** | **did NOT complete within a 120 s budget and was terminated. Not diagnosed.** |
| **Native-scale `.TRAN`** | completed (40669 rows), ringing present ✓ |

**Physics-relevant differences:**

- **(a) is de-risked on the axis that mattered most.** The a-priori worry was that SI-scale element magnitudes ($10^{-21}$ s delays, $10^{20}$ Hz) would hit tolerance or dynamic-range pathology. On the `.AC` path they did not. **This is EVIDENCE BEARING ON the epic §8 PARK trigger** *"no solver represents the bond object without distortion"* **for the AC path** — a lossless `T` element with $(Z_0,\mathrm{TD})$ is exactly the substrate's bond object, and ngspice integrates it at canonical scale. **⚠ Status pinned (checker-audit SCX-09): the trigger is NOT retired, and this lane cannot retire it.** The probe behind this row is an **untracked, non-banked Phase-0 scratch run** of exactly the class §7 of the requirements doc disclaims, and **Phase 0 authorizes no implementation** — so the finding is *evidence from a non-banked probe*, not an accomplished retirement. Retiring the PARK trigger is a Phase-1 act, on a tracked driver, under the epic §5.2 reproduction gate. An earlier draft wrote "That removes the epic §8 PARK trigger", which asserted as done a thing Phase 0 is not permitted to do.
- **The transient path is NOT de-risked** and the failure is scale-correlated (native completed, SI did not). This couples T1 → T4 → T6 and is recorded in all three.
- **(b) buys real independence** — Xyce is an independently-developed code base, so a Xyce/ngspice agreement is a stronger receipt than either alone. But the epic's §5.3 protocol only reaches for a second solver *when suspect (b) — solver numerics — is live*, i.e. after a divergence is already observed. Procuring it before there is a divergence to attribute is pre-paying for a step that may never be needed.
- **(c)** doubles the netlist-dialect surface at Phase 1, which is exactly where the epic wants the exporter simple enough to hand-audit (§5.3(a)).

**Lane recommendation:** **(a) ngspice now, (b) Xyce deferred** — installed only if and when the §5.3 protocol reaches suspect (b). If the epic later wants a standing second-solver arm in CI, note that **neither solver is currently a repo dependency**, and adding one is a separate decision with its own CI/portability consequences (a contributor without ngspice cannot run the cross-check locally; the natural pattern is an opt-in marked test that skips when the binary is absent, mirroring the existing optional-dependency handling).

**STATUS: OPEN — decision pending (Grant ratification of the lane recommendation). SELECT NOTHING.**

---

## T2 — Bond representation ★ **GRANT'S CALL (physics-adjacent)**

**Builds to REQ-IDs:** `SCX-REQ-ELEMENTS` (which canonical pair the bond is built from), `SCX-REQ-LABEL` (**the load-bearing coupling — see T2.4**), `SCX-REQ-ANCHOR` (the pilot object is a bond), `SCX-REQ-FENCE` F1/F5.

**Epic leaning (verbatim):** *"**TL element** — the substrate model is TLM; SPICE's lossless line is the same object. Mutual-K (the archived code's choice) is pre-rejected: it is not the substrate's coupling"*.

**Scope fence carried into every option (F3, restated because it is Grant-facing):** scalar/translational channel only, per [`srs-band-structure.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md) §1–§2 — the sections that carry no demotion marker. The vector-channel analogue of any option below is out of scope; its band top is a bracket with a demoted upper arm and a PENDING-Grant fork.

### T2.1 — Options

- **(a) Lossless transmission-line element per bond** — one SPICE `T` element per srs bond, parameters $(Z_0,\mathrm{TD})$, with the $z=3$ vertex realised as an ordinary shunt node (which is exactly what the engine's `scatter_matrix` derives: $S_{ij}=2/n-\delta_{ij}$ is the shunt-junction KCL reduction, [`chiral_lattice.py:81-103`](../src/ave/core/chiral_lattice.py)).
- **(b) Lumped-LC ladder per bond** — each bond discretised into $M$ sections of series $L$ / shunt $C$.
- **(c) Mutual-inductance (`K`) coupling between per-node tanks** — the archived exporter's choice.

### T2.2 — Physics-relevant differences

- **(a) is the same mathematical object as the substrate model.** The substrate's scalar channel IS a distributed LC transmission-line network — the corpus states it as the load-bearing methods fact: *"the substrate-native srs vacuum is a **distributed LC transmission-line network** (the Op5 scatter+connect TLM …); its dispersion is the **coined-quantum-walk / transmission-line arccos map**"* ([`srs-band-structure.md:53-57`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)). A SPICE lossless line is that object with no approximation, and the $\Gamma=(2-z)/z=-1/3$ vertex mismatch ([`translation-circuit.md:189`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)) emerges from the shunt node for free rather than being modelled.
- **(b) reproduces the model the corpus REJECTED, in the $M\to$ small limit.** This is the substrate-native trap, and it is not a subtle one. The corpus adjudicated the lumped graph-Laplacian model $\omega=\sqrt\lambda$ against the distributed arccos map and the lumped model **FAILED the frozen $1/\sqrt3$ velocity gate** (it gives $1/\sqrt2$) and gives a band top of $\sqrt{12}=3.464\,\omega_C$ instead of $\pi\sqrt3=5.441\,\omega_C$ ([`srs-band-structure.md:59-67`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)). A one-section-per-bond LC ladder **is** the lumped model. It converges to (a) as $M\to\infty$, so (b) is not wrong in principle — but at any finite $M$ it introduces a discretisation error the engine does not have, which is a free parameter in the exporter, which epic §5.4 calls *"a design defect in the exporter"* by construction.
- **(c) is not the substrate's coupling.** The substrate's bond is a delay line carrying a travelling wave; a mutual-`K` between lumped tanks is an instantaneous reactive coupling with no propagation delay and therefore no band structure of the right form. It also reintroduces exactly the underived choices the dt-fusion ruling retired (`K = 0.5/d`, clamped 0.999 — [`docket-entries/2026-08-23-dt-fusion-ruling.md:23-26`](../_orchestration/docket-entries/2026-08-23-dt-fusion-ruling.md)). **Pre-rejected by the epic; recorded here for completeness, not offered.**

### T2.3 — `substrate-native-check` verdict on this trade

The walk (requirements §0.5) returns (a) unambiguously on CP1 and CP3: the substrate runs **wave propagation**, and the AVE-native objective is the **TLM transmission eigenmode**, not a lumped-network eigenvalue. Choosing (b) would be the classic SM/continuum-default leak in circuit clothing — reaching for the familiar lumped discretisation because it is the one a general-purpose netlist author reaches for first.

### T2.4 — ★ WHY THIS IS GRANT'S CALL AND NOT THE LANE'S

The choice is **not** convention-neutral. Per `SCX-REQ-LABEL` (requirements §3, the full derivation and the flag):

- **(a) takes $(Z_0,\mathrm{TD})$ directly** and lands on the **R2** convention, $\mathrm{TD}=\texttt{ANALYTIC\_NETWORK\_FACTOR}/\texttt{OMEGA\_C}$ — band top $\pi\sqrt3\,\omega_C$.
- **(b) most naturally reaches for `L_CELL`/`C_CELL` per section**, whose $\sqrt{LC}$ round trip is $1/\omega_C$ — i.e. it lands on the **R1** convention unless deliberately rescaled, band top $\pi\,\omega_C$.

So T2 silently selects an $\omega_C$ scale label, and the two labels differ by $\sqrt3$ on **every** frequency observable in the epic. The requirements doc pins R2 so an exporter cannot drift; but pinning a convention inside an implementation doc is not the same as ratifying it, and the corpus's own adjudication flag on R1-vs-R2 is still **open** (*"Flagged for adjudication"*, [`srs-band-structure.md:157`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md)).

**Additionally routed to Grant with this trade** (requirements §8.2 FL-1, flag-don't-fix): two live engine symbols currently encode the two different bond delays — `bond_lc()` ([`chiral_lattice.py:431-438`](../src/ave/core/chiral_lattice.py), R1) and `ANALYTIC_NETWORK_FACTOR` ([`chiral_lattice_dynamics.py:48`](../src/ave/core/chiral_lattice_dynamics.py), R2) — and acceptance test T0.2 ([`test_l0_medium.py:118-155`](../src/tests/engine_acceptance/test_l0_medium.py)) asserts the R1 form as a Class-A identity. No in-tree result is known to be wrong; the hazard is that the symbol *named* `bond_lc` is the one an exporter author reaches for.

**Lane recommendation:** **(a) lossless TL element**, matching the epic's leaning and the substrate walk. **(b) is retained only as a convergence diagnostic** — running the same graph as an $M$-section ladder and watching it approach (a) as $M$ grows would be a useful *internal* check that the TL element is behaving, but it is not the comparison. **(c) is pre-rejected.**

**STATUS: OPEN — ★ DECISION PENDING GRANT (physics-adjacent; this is the Phase-1 GO gate). SELECT NOTHING.**

---

## T3 — Graph source

**Builds to REQ-IDs:** `SCX-REQ-GRAPH` (the graph is the engine's own srs-z3 adjacency).

**Epic leaning (verbatim):** *"engine export (fixtures can silently drift from the engine's graph)"*.

**Options:**

- **(a) Engine's own adjacency export** — call `build_srs_net(L)` ([`chiral_lattice.py:206`](../src/ave/core/chiral_lattice.py)) and walk `net.neighbors` / `net.reverse_port`.
- **(b) Hand-built netlist fixtures** — author the srs connectivity directly in the exporter or as static `.cir` files.
- **(c) Hybrid** — engine export for the graph, static golden fixtures checked in as regression anchors.

**Physics-relevant differences:**

- **(a) is the only option that makes the result mean anything.** The epic's entire value proposition is *"the engine and an independent solver agree on the **same** network"*. If the netlist's topology is authored independently of the engine's, then agreement tests the author's transcription, and disagreement is unattributable between transcription and engine. (a) also inherits the engine's own carrier self-declaration (`net.carrier == "srs-z3"`), which the exporter can assert on before emitting — a cheap guard against silently exporting the z=4 diamond instrument (`SCX-REQ-GRAPH.2`).
- **(b)** would let the netlist drift from the engine across any future graph change, and the drift would be invisible: a stale fixture still produces a valid srs-looking netlist.
- **(c)** is (a) plus a regression net. The golden fixtures are then *outputs* of the export, not inputs to it, so the drift hazard of (b) does not apply — but a fixture that is regenerated on every graph change is not catching anything either, so its value depends on whether a graph change should be loud (it should).

**Lane recommendation:** **(a)**, with **(c)**'s golden-netlist regression as an optional Phase-2 addition once the export is stable. **Corollary requirement (already in `SCX-REQ-GRAPH.1`):** the exporter must assert `net.carrier == "srs-z3"` before emitting, so exporting the diamond instrument fails loudly rather than silently.

**STATUS: OPEN — decision pending. SELECT NOTHING.**

---

## T4 — Observable extraction

**Builds to REQ-IDs:** `SCX-REQ-OBS` (OBS-1…OBS-6), `SCX-REQ-FENCE` F1/F5/F6 (which modes are representable, which are cycle-space, which are dark at a driven port).

**Epic leaning (verbatim):** *"frozen per-phase in the prereg; Phase-2 leaning = two-port response"*.

**Options:**

- **(a) `.AC` driving-point impedance / $S_{11}$** at a named node.
- **(b) `.AC` two-port $S_{21}$** between two named ports.
- **(c) Transient ringdown** — pulse and FFT.

**Physics-relevant differences:**

- **(a)/(b) are frequency-domain and match the canonical claim's coordinates.** Every reference number in `SCX-REQ-OBS` is a frequency in units of $\omega_C$; extracting frequencies from a frequency-domain sweep needs no intermediate transform and no windowing choice. `phase-space-coordinate-check`: the corpus claim lives in $\omega$-space, so the measurement should too.
- **(c) needs the reactance pair.** If transient is selected, `substrate-native-check` CP6 binds: both the C-state and the L-state must be recorded across the window, because a snapshot at one phase is consistent with both a static configuration and an oscillator caught at peak. That is extra machinery for no extra information relative to (a)/(b) here.
- **(c) is the one option with a probed feasibility problem.** T1's probe: the SI-scale transient did not complete within a 120 s budget while the SI-scale `.AC` completed immediately, and the *same* transient completed in native units. **T4(c) therefore hard-couples to T6** — selecting transient without native/normalised emission is selecting a run that has already failed once at Phase 0.
- **F6 binds (a) specifically.** A driving-point sweep sees only modes with nonzero response at the driven node. Worked case in the requirements (§6 F6): P1-C's two differential modes have zero voltage at the vertex, so driving the vertex returns only the symmetric family. Whichever of (a)/(b) is chosen, the prereg must name the drive/observe nodes **and** the modes those choices make unobservable — *an unobservable mode is not a missing mode*.
- **F5 binds all three.** The finite network's natural-frequency set is not the arccos-map set: there is a cycle-space block of $B-N+1$ modes at $\omega=0$ **and** at the band top (33 each on the $L=2$ supercell, verified). Any set-comparison must count the interior spectrum with multiplicities halved and treat the edge blocks separately.

**Lane recommendation:** **(b) two-port `.AC` for Phase 2** (matching the epic's leaning), **(a) driving-point `.AC` for the Phase-1 pilot** (a single-port object needs no second port, and the driving-point impedance of P1-B/P1-C is closed-form). **(c) not recommended** unless T6 selects native units, and even then only as a cross-check of (a)/(b), never as the primary.

**STATUS: OPEN — decision pending; the per-phase selection freezes in each phase's prereg. SELECT NOTHING.**

---

## T5 — Where results live

**Builds to REQ-IDs:** none (documentation convention).

**Epic leaning (verbatim):** *"`research/` prereg+result pair per phase, per the standing grammar"* — **whose call: standing convention.**

There is no option space here; the standing repo grammar already fixes it (`research/YYYY-MM-DD_<slug>_prereg-FROZEN.md` + `research/YYYY-MM-DD_<slug>_result.md` per phase). Phase 0's own deliverables follow the bench-doc pattern instead (requirements + trade study + prereg skeleton), which is the same grammar's planning-tier form.

**STATUS: NO DECISION REQUIRED — standing convention applies.**

---

## T6 — Units / scaling of the emitted netlist *(lane-surfaced addition, not in the epic's §6 table)*

**Why this trade exists.** The epic's §6 table has no units row, and the SI magnitudes force one: the canonical bond is a $10^{-21}$-second delay line and the canonical cell tank is $10^{-19}$ H against $10^{-24}$ F. Epic §5.5 anticipates exactly this class of item — *"every element of the exported network derives from the canonical chain or carries an explicit **engineering-choice** tag (solver step ceilings, sweep ranges)"* — so this is a tagged engineering choice, not a physics decision. Added per the **KEEP-BOTH** pattern: a new axis alongside T1–T5, redefining none of them.

**Builds to REQ-IDs:** `SCX-REQ-ELEMENTS` (whatever scaling is used, values still enter by import and the round trip must be exact), `SCX-REQ-REPRO`.

**Options:**

- **(a) Emit in SI.** Netlist carries `Z0=376.73031346177066`, `TD=7.436783388682972e-22`. Hand-auditable against `constants.py` by eye — which directly serves the epic's §5.3(a) hand-audit, since the netlist *is* the audit artifact.
- **(b) Emit in native/normalised units** ($\ell_{node}=1$, $c_{link}=1$, $Z_0=1$), map results back on read. Every number is O(1); the mapping constants are printed in the netlist header.
- **(c) Emit in SI, with a native-unit run as a paired cross-check.** Both, with agreement between them as its own gate.

**Physics-relevant differences:**

- **The observables are dimensionless anyway.** Every reference in `SCX-REQ-OBS` is a ratio $\omega/\omega_C$, so the comparison is scale-free by construction and (a) vs (b) cannot change any verdict — only the numerical conditioning and the readability of the audit artifact.
- **(a) is better for the hand-audit, and is probed-viable on the AC path.** T1's probe put an SI-scale `T` element through `.AC` and got the closed-form resonance to within the grid step, with no tolerance overrides. So the a-priori conditioning worry is **de-risked** *for AC* — same register as the T1 row at §2 (checker-audit SCX-09): this is evidence from an **untracked, non-banked Phase-0 scratch probe**, not a retirement. Retiring anything is a Phase-1 act on a tracked driver under the epic §5.2 reproduction gate.
- **(b) is better for the transient path, and is probed-necessary there.** Same network, same probe: SI transient did not complete in 120 s; native transient completed. **Undiagnosed** — this lane observed it and did not chase it — but the correlation is clean enough to make (b) a prerequisite of T4(c) rather than a preference.
- **(b) costs the hand-audit some directness**: an auditor comparing the netlist to `constants.py` now has to apply the mapping, which is one more place a factor can hide. Mitigated by printing every canonical symbol and its native-unit image in the netlist header (already required by `SCX-REQ-ELEMENTS.2`).
- **(c) buys a free extra gate.** SI-run and native-run agreement on the dimensionless observables is a self-consistency check on the exporter's own scaling arithmetic, and it costs one extra solver invocation.

**Lane recommendation:** **(c)** — emit SI as the primary/auditable artifact, with a native-unit companion run whose dimensionless agreement is a pre-registered gate. If T4 selects transient, the native run becomes the primary and the SI run becomes the optional one.

**STATUS: OPEN — decision pending. SELECT NOTHING.**

---

## Coupling map (which trades are not independent)

| coupling | why |
|---|---|
| **T2 → `SCX-REQ-LABEL`** | (a) lands on R2, (b) lands on R1 unless deliberately rescaled — a $\sqrt3$ on every frequency observable. **The reason T2 is Grant's.** |
| **T4(c) → T6(b)** | Probed: SI transient did not complete, native transient did. Selecting transient without native units selects a run that already failed once. |
| **T1(b) → T5** | If Xyce is ever added, its netlist dialect differences become a second exporter target and the per-phase result docs must record which solver produced which number. |
| **T3 → `SCX-REQ-GRAPH.2`** | Engine export inherits `net.carrier`, so the diamond-instrument guard is free; a hand fixture would need the guard authored separately. |

---

## Named open items this trade study does NOT close

1. **FL-1** (requirements §8.2) — the `bond_lc()` / `ANALYTIC_NETWORK_FACTOR` bond-delay divergence. **Routed to the auditor lane; feeds T2.**
2. **FL-3** (requirements §8.2) — `scatter_matrix` raises for $n<2$, so the engine cannot build a 1-port-terminated network and the epic's *three-way* Phase-1 anchor is not currently constructible for P1-B/P1-C. **Phase-1 GO decision:** relax the guard (a small engine touch needing its own justification) **or** run those two objects as two-way analytic-vs-solver comparisons. Not decided here.
3. **Q1** (requirements §8.1) — the plumber-physical question: does a vacuum bond ring at its full-wave, or is the half-wave the top by construction? **Gates the F1 fence's framing** (instrument ceiling vs physics), and therefore gates what the Phase-2 prereg is allowed to say about modes above the band top.
4. **Whether either solver becomes a repo dependency** (T1) — CI/portability consequences, out of scope at Phase 0.

---

## Skill-selection retro-pass

`substrate-native-check` (T2.3 — the walk returns TL, and names the lumped-ladder option as the leak); `ave-canonical-source` (no value restated here; all cited to the requirements datasheet); `consistency-vs-emergence` (frame re-declared at the head); `verify-before-cite` (every epic leaning quoted verbatim and every code/KB cite re-verified this branch); `ave-driver-script-honesty` (the ngspice probes are labelled scratch, not-tracked, not-a-result, and the undiagnosed transient failure is reported as undiagnosed); stop-and-ask (T2 stopped at Grant; FL-1/FL-3/Q1 routed rather than resolved). **No drift from the epic §7 planned set.**
