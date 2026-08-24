# PHASE-1 PREREG **SKELETON** — external-solver cross-check, pilot scale

**Date:** 2026-08-24 · **Branch:** `research/2026-08-24-solver-crosscheck-phase0` · **Base:** `origin/main` @ `ff0fde8b`
**Epic:** [`_orchestration/2026-08-23_external-solver-crosscheck-epic.md`](../_orchestration/2026-08-23_external-solver-crosscheck-epic.md) §4 Phase 1.

> # ⚠ THIS IS A SKELETON, NOT A FROZEN PREREG.
>
> **Phase 0 is planning only and the epic authorizes no implementation.** This document fixes the
> **STRUCTURE** of the Phase-1 prereg — which bins exist, which axes they are cut on, which
> controls are mandatory, what the deliverable list is. **Every numerical tolerance, bin edge,
> sweep range and network size below is written as `⟨FROZEN-AT-PHASE-1-GO⟩`** and carries **no
> value**. Values are filled in and the document renamed to
> `research/2026-<MM>-<DD>_solver-crosscheck-phase1_prereg-FROZEN.md` **at Phase-1 GO, committed
> ALONE and PUSHED before any exporter code, netlist, or comparison number exists in the tree**
> (freeze-by-push). Rule 11 binds from that moment: no bin may be edited, widened, or re-labelled
> after any comparison content lands.
>
> **Filling in a value here does not freeze it.** The freeze event is the rename + solo commit +
> push at GO. Until then this file is a planning artifact and may be revised freely.
>
> **Blocked on:** T2 ratification (Grant), the epic's stated Phase-0 GATE. Also carries three named
> open items — FL-1, FL-3 and Q1 — listed in §9.
>
> **★ GATE ASK (checker-audit SCX-10), added so a reading is ratified rather than inherited:** the
> epic's Phase-0 deliverable is worded *"the frozen Phase-1 prereg skeleton"*, and this lane has
> read that as **structure-frozen / values-unfrozen** — the STRUCTURE (bins, axes, mandatory
> controls, deliverable list) is fixed by this document, while every tolerance and edge stays
> `⟨FROZEN-AT-PHASE-1-GO⟩` and the freeze event is the rename + solo commit + push at GO. That
> reading is what makes this file revisable today and it is **an interpretation this lane made, not
> one the epic states**. **The Phase-0 GATE is asked to ratify or correct it explicitly.** If the
> epic instead meant *fully frozen at Phase 0*, then this document is already past its freeze
> point, the paragraph above is wrong, and every subsequent edit to it is a Rule-11 violation —
> which is why the ambiguity is surfaced as a gate item rather than resolved by this lane.

**Class:** IMPLEMENTATION-VERIFICATION (a sub-class of CONSISTENCY). **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, axiom or ruling; changes no solidity; propagates nothing.** No result from this phase may be framed as emergence, chord, or a falsification of AVE.

**Sibling docs (cite-don't-duplicate — no derived number is restated here):**
[`research/2026-08-24_solver-crosscheck-phase0_requirements.md`](2026-08-24_solver-crosscheck-phase0_requirements.md) (`SCX-REQ-*`) ·
[`research/2026-08-24_solver-crosscheck-phase0_tradestudy.md`](2026-08-24_solver-crosscheck-phase0_tradestudy.md) (T1–T6, all OPEN).

---

## §0 — Standard Vacuum Analysis header

1. **SECTOR / OWNERSHIP.** Driven coordinate = the **scalar / translational** node variable (one scalar per node, the Op5 shunt-junction port set). **No Cosserat / T2 microrotation DOF is exported, driven, or read** — `SCX-REQ-FENCE` F3. Cross-wiring check performed: nothing in this phase couples the scalar channel to charge, spin, or mass; the export carries connectivity and two line parameters and nothing else.
2. **REGIME / PHASE-STATE.** MODE = numerical-infrastructure verification (no physics claim). REGIME = **Regime I, cold, sub-yield, lossless-reactive**, linear small-signal; Ax-4 saturation OFF ($A=0$), Op14 not engaged. PHASE-STATE = cold crystalline, Axiom-5 clause-Q quiescent ($\varepsilon_{11}=0$). **Saturated, ruptured and pre-bond states are OUT OF SCOPE** and no result may be extrapolated across a phase boundary.
3. **CIRCUIT STATEMENT (before any framework word).** A network of identical lossless delay lines is joined at 3-way shunt junctions. Two independent integrators are handed the *same* network with the *same* element values. **Question: do they report the same resonances?** Nothing about the vacuum is at issue — only whether our integrator integrates.
4. **PLANE & PROJECTION.** Reference plane = the **node** (the shunt junction), where the engine's port variables and SPICE's node voltages are the same object. Observables are reported as **dimensionless ratios $\omega/\omega_C$**, so the comparison is scale-free and T6's units choice cannot move a verdict.
5. **CONSISTENCY-VS-EMERGENCE.** IMPLEMENTATION-VERIFICATION. Agreement validates the engine's numerics against an independent integrator. **Disagreement is the more valuable outcome** and is attributed under §6.
6. **COORDINATES (`phase-space-coordinate-check`).** The canonical claim lives in **frequency space** ($\omega/\omega_C$) and, for OBS-4, in **reciprocal space** on the BCC reciprocal lattice. Measurement is in those coordinates. The $\omega$-vs-$k$ discipline of `srs-band-structure.md:69-76` binds: a frequency is never compared against a wavevector.

---

## §1 — The target, in one sentence

> Does ngspice (T1), fed the engine's own srs-z3 graph (T3) with canonical element values (`SCX-REQ-ELEMENTS`) under the R2 label convention (`SCX-REQ-LABEL`), reproduce the engine's certified scalar-channel resonances at pilot scale, within tolerances frozen before the first cross-run?

---

## §2 — VERDICT GRAMMAR (structure frozen here; edges frozen at GO)

### §2.1 — The comparison ladder (fixed order; each rung gates the next)

| rung | object | engine/analytic side | solver side | gate |
|---|---|---|---|---|
| **L0** | **P1-A** bare cell tank | arithmetic identity from `constants.py` (`SCX-REQ-ANCHOR.3` — solver-vs-arithmetic, **not** a two-integrator comparison) | `.AC` driving-point | `⟨FROZEN-AT-PHASE-1-GO⟩` |
| **L1** | **P1-B** one bond, open–open | closed form + TLM operator | `.AC` driving-point | `⟨FROZEN-AT-PHASE-1-GO⟩` |
| **L2** | **P1-C** vertex + 3 open stubs | closed form + TLM operator | `.AC` driving-point | `⟨FROZEN-AT-PHASE-1-GO⟩` |
| **L3** | **P1-D** 4-site primitive cell, real periodic wrap ($K_4$ complete graph of 6 lines) | arccos map on $\mathrm{eig}(A)$ + TLM operator | `.AC` | `⟨FROZEN-AT-PHASE-1-GO⟩` |
| **L4** | **OBS-4** supercell eigenfrequency SET, $L=\langle\text{FROZEN}\rangle$ | arccos map on $\mathrm{eig}(A)$ of `build_srs_net(L)` + cycle-space block (F5) | `.AC` sweep, peak extraction | `⟨FROZEN-AT-PHASE-1-GO⟩` |

**L1–L2 are the three-way anchor** (epic §4 Phase 1), **subject to FL-3**; **L0 is a solver-vs-arithmetic numerics smoke test and is not part of the anchor** (SCX-REQ-ANCHOR.2/.3). Epic §4 Phase 1, verbatim: *"BOTH the engine and the solver are first checked against the closed-form value independently"* — which L0 cannot satisfy, because its engine/analytic side is an arithmetic identity from `constants.py` rather than an independent integrator leg (§2.1 L0 row says so itself). **FL-3**: `scatter_matrix` raises for $n<2$, so the engine-side TLM leg of L1/L2 is not currently constructible without an engine touch. **If FL-3 is not resolved at GO, L1/L2 are declared TWO-WAY (analytic-vs-solver) in the frozen prereg and the epic's three-way localisation claim is correspondingly weakened — stated, not hidden.**

### §2.2 — Outcome bins (mutually exclusive, exhaustive; MANDATORY `INCONCLUSIVE`)

| bin | criterion (edges `⟨FROZEN-AT-PHASE-1-GO⟩`) |
|---|---|
| **AGREE** | Every rung L0–L4 within its frozen tolerance, **and** every fence in §4 accounted for (no unexplained modes). |
| **DIVERGE-ATTRIBUTED** | At least one rung outside tolerance, **and** the §6 protocol localises it to exactly one of {exporter, solver numerics, engine} with a receipt. **This is a valid, bankable outcome — the engine-side arm is the single most valuable result the epic can produce.** |
| **DIVERGE-UNATTRIBUTED** | Outside tolerance and the §6 protocol runs to completion without localising. **This fires the epic §8 KILL: the instrument is unsound; bank the negative and stop.** |
| **INCONCLUSIVE** | The run did not produce a comparable number (solver non-convergence, an unresolvable peak, a network that would not build). **Mandatory bin — never folded into any other.** |

**Bin-integrity check (run now, before any value exists):** every falsifier in §5 routes to exactly one bin above; no falsifier can fire into two bins; `INCONCLUSIVE` is reachable independently of the physics. ✅

### §2.3 — Tolerance AXES (the structure; values at GO)

Tolerances are specified on **dimensionless frequency ratios**, never on absolute frequencies:

| axis | quantity | tolerance form |
|---|---|---|
| **TOL-FREQ** | $\left|\omega_{solver}/\omega_{ref}-1\right|$ per matched mode | relative, `⟨FROZEN-AT-PHASE-1-GO⟩` |
| **TOL-GRID** | sweep resolution as a fraction of the smallest mode spacing at that rung — **must be finer than TOL-FREQ or the comparison cannot resolve its own tolerance** | ratio, `⟨FROZEN-AT-PHASE-1-GO⟩` |
| **TOL-MULT** | per-frequency multiplicity match (integer; exact or not at all) | exact match required |
| **TOL-COUNT** | total mode count within the compared band, after the F5 cycle-space accounting | exact match required |

> **Instrument-resolution clause (declared now).** TOL-GRID must be set **before** TOL-FREQ and must be strictly finer. The Phase-0 probe illustrates why: an SI `.AC` sweep of 40001 points over $[6.0,7.5]\times10^{20}$ Hz resolves $5.6\times10^{-6}$ relative, so a TOL-FREQ tighter than that would be measuring the grid, not the solver. **A tolerance the instrument cannot resolve is a tolerance that always passes.**

---

## §3 — Analytic expectations, frozen as FORMS (symbols, not values)

Stated as forms so that the frozen prereg's values are checkable against something written down first:

- **P1-A:** $\omega_0=1/\sqrt{L_{CELL}C_{CELL}}$.
- **P1-B (open–open):** $\omega_n=n\pi/\mathrm{TD}$; the engine carries $n=1$ only (F1).
- **P1-C (vertex + 3 open stubs):** symmetric family $\omega=n\pi/\mathrm{TD}$; differential family $\omega=(2n-1)\pi/(2\,\mathrm{TD})$, **two-fold degenerate**.
- **P1-D / L4:** $\omega=\omega_{link}\arccos(\mu/z)$ on the network adjacency spectrum, **plus** the F5 cycle-space block at $\omega\in\{0,\ \pi\,\omega_{link}\}$ of size $B-N+1$ each; interior arccos values appear at doubled multiplicity in the TLM operator's $e^{\pm i\theta}$ spectrum.
- **$\mathrm{TD}$:** `ANALYTIC_NETWORK_FACTOR / OMEGA_C` (R2, `SCX-REQ-LABEL`). **Under R1 every frequency above divides by $\sqrt3$** — the masquerade this prereg exists to pre-empt.

**All numerical values for the above are re-derived fresh at GO under `SCX-REQ-REPRO` / epic §5.2.** The Phase-0 receipts (requirements §7) are **NOT** load-bearing for Phase 1; drift between them and the fresh values is itself a finding to be banked under a dated note.

---

## §4 — Pre-registered fences: correct behaviour that will LOOK like divergence

**Declared before the first run so that none of them can be discovered mid-debug and rationalised.** Full statements in requirements §6.

| fence | what will be seen | why it is not a divergence |
|---|---|---|
| **F1** | Solver reports modes at $2\pi/\mathrm{TD}$, $3\pi/\mathrm{TD}$, … that the engine does not have | The engine's TLM is discrete-time with step $=\mathrm{TD}$; its representable band stops at $\pi\,\omega_{link}$. **Comparison band is $\omega\le\pi\,\omega_{link}$.** *(Framing of this fence — instrument ceiling vs physics — is gated on Q1, §9.)* |
| **F2** | No $\mathbf k$-resolved dispersion curve is produced | A netlist cannot impose a complex Bloch phase. Substitute (A), the unlabelled supercell eigenfrequency SET, is the observable; the $\mathbf k$-label is **not** compared. |
| **F5** | A large degenerate pile-up at DC and at the band top | The graph's cycle space, $B-N+1$ modes at each edge. **Compare the interior spectrum with multiplicities halved; count the edge blocks separately.** |
| **F6** | Modes present in the reference are absent from a driven sweep | Dark at the chosen drive node. **The prereg names the drive/observe nodes and the modes they make unobservable. An unobservable mode is not a missing mode.** |
| **MESH** | At small $L$ the supercell's top sits below $\pi\,\omega_{link}$ | The commensurate $\mathbf k$-mesh is coarse; the band top is not on the mesh. A mesh artefact, not a missing band. |

---

## §5 — Controls and falsifiers (frozen; **UNRUN ≠ PASSED**)

**POSITIVE CONTROL (mandatory before any agreement is bookable).** Inject a **known** defect into the netlist — e.g. perturb one bond's TD by a frozen factor — and confirm the comparison **resolves it** and bins it `DIVERGE-ATTRIBUTED`. A comparison that cannot detect a planted defect cannot certify an agreement. *(`CLV-REQ-VALIDATE` class, validate-on-known / anti-false-null.)*

**NEGATIVE CONTROL.** Run the identical pipeline on a network whose answer is trivially known and **not** srs — the single bond (L1) serves — and confirm no srs-specific structure appears. Guards against the pipeline manufacturing structure.

**ANTI-TAUTOLOGY CONTROL.** The exporter must not read any reference frequency, and the comparison harness must not feed reference values into the netlist. **Machine-enforced:** the exporter's imports are restricted to `constants.py` symbols + the graph; a grep gate asserts no band-structure symbol is importable from the exporter module. *(A comparison whose netlist knows the answer is a checklist, not a gate.)*

**CONVENTION CONTROL.** Emit and run **both** label conventions once at L1 and confirm the ratio is exactly $\sqrt3$. This converts the `SCX-REQ-LABEL` hazard from a silent failure mode into a measured, pre-registered quantity.

**Falsifier list (each routes to exactly one §2.2 bin):**

| # | falsifier | bin |
|---|---|---|
| FS-1 | Any rung outside TOL-FREQ, localised by §6 | DIVERGE-ATTRIBUTED |
| FS-2 | Any rung outside TOL-FREQ, not localised after §6 runs to completion | DIVERGE-UNATTRIBUTED (**epic KILL**) |
| FS-3 | Mode count or multiplicity mismatch after F5 accounting | DIVERGE-ATTRIBUTED or -UNATTRIBUTED per §6 |
| FS-4 | Positive control fails to resolve the planted defect | INCONCLUSIVE (instrument not validated; **no agreement may be booked**) |
| FS-5 | Convention control does not return exactly $\sqrt3$ | DIVERGE-ATTRIBUTED to exporter |
| FS-6 | Solver non-convergence / unresolvable peak / network will not build | INCONCLUSIVE |

**Observable robustness ladder.** PRIMARY (gating) = **frequency agreement per matched mode** (TOL-FREQ) and **exact mode/multiplicity accounting** (TOL-MULT, TOL-COUNT). SUPPLEMENTARY, never gating = peak amplitudes, $Q$ values, phase slopes — all of which depend on the numerically-imperfect terminations and the sweep grid, not on the physics under comparison.

---

## §6 — Divergence adjudication protocol (epic §5.3, fixed order)

1. **(a) EXPORTER.** Hand-audit the emitted netlist against the graph and `constants.py`. **The netlist is human-readable by design and carries every imported symbol in its header** (`SCX-REQ-ELEMENTS.2`), so this step is mechanical. Cross-check node/bond counts against $8L^3$ / $12L^3$.
2. **(b) SOLVER NUMERICS.** Integrator/tolerance sweep on the solver side; re-run at finer TOL-GRID; re-run under the other units scaling (T6(c)'s paired run is exactly this check pre-positioned). Second solver **only if** T1(b) has been ratified and installed.
3. **(c) ENGINE.** What remains. **The L1–L2 analytic anchor localises (a)-vs-(c) before either is trusted at L3/L4 scale** — subject to the FL-3 caveat in §2.1, and with **L0 sitting below the anchor** as the solver-vs-arithmetic numerics smoke test that clears suspect (b) first (`SCX-REQ-ANCHOR.2/.3`; consistency propagation of the §2.1 correction).

**No tuning to agreement.** The exporter has no free parameter by construction (topology from the engine, values from `constants.py`). **If a knob appears that would let the export be tuned toward agreement, that knob is a design defect in the exporter and is reported as one** (epic §5.4).

---

## §7 — Reproduction gate (epic §5.2)

Every engine-side reference number is **re-derived on the current engine at comparison time**. Banked numbers — including the Phase-0 receipts in requirements §7 — are **not** load-bearing. Drift between banked and fresh values is a finding, banked under a dated note, never silently overwritten.

**Demotion re-check at GO.** `srs-band-structure.md` §1/§2 carried no demotion marker as of 2026-08-24 (requirements §5.0). **Re-verify at GO** — a demotion landing between now and then would move a reference this prereg depends on.

---

## §8 — Deliverables (fixed order)

1. The frozen prereg (this document, renamed, values filled, committed alone and pushed).
2. The exporter (`src/ave/…` or `src/scripts/…` per the module-library convention), with the `SCX-REQ-ELEMENTS.2` canonical-source assertion and the anti-tautology grep gate.
3. The emitted netlists for L0–L4, tracked (they are the §6(a) hand-audit artifact).
4. The comparison driver + its output record.
5. `research/2026-<MM>-<DD>_solver-crosscheck-phase1_result.md` — verdict in one of the four §2.2 bins, with the register re-declared and every fence's accounting shown.
6. Phase-2 GO recommendation, or the epic-KILL record.

---

## §9 — Named open items blocking the freeze

| # | item | owner | effect if unresolved at GO |
|---|---|---|---|
| **T2** | Bond representation ratification | **Grant** | **Hard block.** The epic's Phase-0 GATE. Also silently selects the $\omega_C$ label (trade study T2.4). |
| **FL-1** | `bond_lc()` (R1) vs `ANALYTIC_NETWORK_FACTOR` (R2) encode different bond delays; acceptance test T0.2 asserts the R1 form | auditor lane | Not a hard block (this prereg pins R2 explicitly), but the CONVENTION CONTROL in §5 exists because of it and should be read as an open item, not a formality. |
| **FL-3** | `scatter_matrix` raises for $n<2$; engine cannot build a 1-port termination | Phase-1 GO decision | L1/L2 drop from three-way to two-way; **stated in the frozen prereg, not discovered at run time.** |
| **Q1** | Does a vacuum bond ring at its full-wave, or is the half-wave the top by construction? | **Grant** (plumber-physical) | Not a hard block, but it decides whether F1 is stated as an **instrument ceiling** or as **physics** — and therefore what the Phase-2 result doc is allowed to say about modes above the band top. |

---

## §10 — Anti-rescue guard

Real odds that this returns `DIVERGE` on some rung are **substantial and expected** — F1, F5 and F6 each describe a way a correct export produces a mode set that does not match a naive reference, and the whole point of writing them down first is that discovering one mid-run must not become a licence to re-cut a bin. **A `DIVERGE-ATTRIBUTED` verdict against the engine is the epic's most valuable outcome and must be reported as a finding, not debugged toward agreement** (Rule 11: honest closure; the wrong reaction is a rescue, the right reaction is a clean result with the mechanism named).

---

## Skill-selection plan for Phase-1 execution (declared now)

`ave-prereg` (the freeze-by-push event itself) · `substrate-native-check` (before the exporter's first line — the T2 walk is done, but the *exporter* is new solver-adjacent code and re-triggers) · `ave-canonical-source` (exporter imports) · `ave-driver-script-honesty` (exporter + comparison driver) · `ave-reproduction-gate` (§7) · `verify-before-cite` (every reference pointer re-verified at GO) · `phase-space-coordinate-check` (§0.6) · `consistency-vs-emergence` (register re-declared in the result doc) · `ave-independence-check` (what the agreement does and does not establish) · stop-and-ask (2-attempt cap). **Retro-pass at phase close if the applied set drifts.**
