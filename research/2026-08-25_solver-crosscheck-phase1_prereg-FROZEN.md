# PHASE-1 PREREG — **FROZEN** — external-solver cross-check, pilot scale

**Date:** 2026-08-25 · **Branch:** `research/2026-08-25-solver-crosscheck-phase1` · **Base:** `origin/main` @ `766d5179`
**Lane:** external-solver cross-check (SCX), Phase 1 — implementer satellite
**Epic:** [`_orchestration/2026-08-23_external-solver-crosscheck-epic.md`](../_orchestration/2026-08-23_external-solver-crosscheck-epic.md) §4 Phase 1
**Brief:** [`_orchestration/2026-08-24_solver-crosscheck-phase1-brief.md`](../_orchestration/2026-08-24_solver-crosscheck-phase1-brief.md)
**GO gate:** [`_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md`](../_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md) (R56) — verified present on `origin/main` before this document was opened.
**Skeleton this fills:** [`research/2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md`](2026-08-24_solver-crosscheck-phase1-prereg-skeleton.md)

> # 🔒 FREEZE STATEMENT
>
> This document is the **frozen** Phase-1 prereg. It is committed **ALONE** and **PUSHED** before
> any exporter code, any emitted netlist, and any comparison number exists in the tree
> (freeze-by-push, per the skeleton's freeze protocol). **Rule 11 binds from the push:** no bin,
> tolerance, edge or label below may be edited, widened or re-labelled after any comparison
> content lands. A post-push change is a Rule-12 dated amendment carrying its own justification,
> never a silent edit.
>
> **Deviation from the skeleton's letter, declared:** the skeleton says the document is
> *"renamed"*. This lane **copied** rather than renamed, so the Phase-0 skeleton survives in place
> as the Phase-0 deliverable the epic §4 lists and as the target of the requirements doc's link.
> Nothing in the skeleton's structure is edited by this lane.
>
> **The skeleton's ★ GATE ASK, resolved by ratify-by-exception.** The skeleton asked the Phase-0
> GATE to ratify or correct its *structure-frozen / values-unfrozen* reading. R56 fired the gate
> and raised no exception on it, under the protocol R56 §3 names verbatim: *"under the
> ratify-by-exception protocol the walk framing declared"*. The reading therefore **stands**.
> Recorded here so it is a ratified reading, not an inherited one.

**Class:** **IMPLEMENTATION-VERIFICATION** (a sub-class of CONSISTENCY). **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, axiom or ruling; changes no solidity; propagates nothing.** **No result from this phase may be framed as emergence, as a chord, or as a falsification of AVE.** Two integrators agreeing on the same network validates that the engine solves its own equations. It says nothing about whether the axioms describe the vacuum.

**Sibling docs (cite-don't-duplicate):**
[`research/2026-08-24_solver-crosscheck-phase0_requirements.md`](2026-08-24_solver-crosscheck-phase0_requirements.md) (`SCX-REQ-*`, the single source of truth for every requirement ID) ·
[`research/2026-08-24_solver-crosscheck-phase0_tradestudy.md`](2026-08-24_solver-crosscheck-phase0_tradestudy.md) (T1–T6 option space).

---

## §0 — R56 RATIFIED SELECTIONS, QUOTED VERBATIM

The Phase-1 GO gate's ruling, [`2026-08-24-ruling-r56-scx-trades.md`](../_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md), transcribed verbatim from `origin/main`. **These are the selections this prereg builds to; nothing below may deviate from them.**

> **Grant, in chat, 2026-08-24, verbatim:** *"a+r2"*

> 1. **T2 = option (a): lossless transmission-line element per bond** — one
>    SPICE `T` element per srs bond, $(Z_0, \mathrm{TD})$, the $z=3$ vertex as
>    an ordinary shunt node (the $\Gamma = -1/3$ mismatch emerges from the
>    junction, unmodeled). Option (b) lumped-ladder is retained ONLY as the
>    trade study's internal convergence diagnostic; option (c) mutual-K stays
>    pre-rejected.
> 2. **The ω_C label: R2 is PINNED as a TAGGED ENGINEERING CONVENTION for the
>    exporter only** — $\mathrm{TD} = \texttt{ANALYTIC\_NETWORK\_FACTOR}/\omega_C$,
>    band top $\pi\sqrt3\,\omega_C$. **The corpus's physics-level R1-vs-R2
>    adjudication flag (`srs-band-structure.md:157`, "Flagged for adjudication")
>    stays OPEN** — this ruling selects the exporter's emitted label and
>    mandates the machine check that the emitted delay matches it (the Phase-1
>    brief's FL-1 test); it does NOT adjudicate the corpus flag.
> 3. **T1 (ngspice), T3 (engine adjacency export), T4 (`.AC` driving-point /
>    two-port), T6 (native/normalised emission + SI round-trip check): STAND as
>    the lane's selections** under the ratify-by-exception protocol the walk
>    framing declared — Grant ruled T2 explicitly and raised no exception on
>    the lane calls.
> 4. **NOT ruled here:** the `bond_lc` symbol rename (FL-1's naming half) — the
>    brief's machine-checked exporter test covers the hazard; the rename stays
>    an open lane proposal.

**★ The R2 pin is an ENGINEERING CONVENTION on the exporter's emitted label, not a physics adjudication.** R56 §2 says so in its own words and this prereg repeats it because it is the single most misreadable line in the lane: **the corpus's physics-level R1-vs-R2 flag at `srs-band-structure.md:157` remains OPEN.** Verified verbatim on this branch at that line:

> *"Only the scale LABEL changes under R1, not the k-space band SHAPE or the gap inventory. Flagged for adjudication."*

Nothing this lane runs, passes or fails may be read as closing that flag.

---

## §1 — Standard Vacuum Analysis header (sector declaration, re-declared per epic §7)

| axis | declaration |
|---|---|
| **MODE** | **Numerical-infrastructure verification.** No physics claim is minted, moved or retired by this phase. |
| **REGIME** | **Regime I — cold, sub-yield, lossless-reactive**, linear small-signal. Ax-4 saturation OFF ($A=0$, $S(A)=1$); Op14 not engaged. |
| **PHASE-STATE** | **Cold crystalline, quiescent** (Axiom-5 clause-Q operating point, $\varepsilon_{11}=0$). Saturated, ruptured and pre-bond states are OUT OF SCOPE; no result may be extrapolated across a phase boundary. |
| **CHANNEL** | **Scalar / translational ONLY.** One scalar node variable per node — the Op5 shunt-junction port set. **No Cosserat / T2 microrotation DOF is exported, driven or read** (`SCX-REQ-FENCE` F3). |
| **CARRIER** | **srs-z3** — the D1-ratified production carrier. The exporter asserts `net.carrier == "srs-z3"` before emitting a line, so exporting the z=4 diamond instrument fails loudly (`SCX-REQ-GRAPH.2`). |
| **CROSS-WIRING CHECK** | Performed. Nothing in this phase couples the scalar channel to charge (Cosserat winding), spin ($\mu$ sign-selector) or mass (A1 dilatation). The export carries connectivity plus two line parameters and nothing else. |
| **consistency-vs-emergence** | **IMPLEMENTATION-VERIFICATION.** Declared before any run. |

**Circuit statement, before any framework word.** A network of identical lossless delay lines is joined at 3-way shunt junctions. Two independent integrators are handed the *same* network with the *same* element values. **Question: do they report the same resonances?** Nothing about the vacuum is at issue — only whether our integrator integrates.

**Plane & projection.** Reference plane = the **node** (the shunt junction), where the engine's port variables and SPICE's node voltages are the same object. Every observable is reported as a **dimensionless ratio $\omega/\omega_C$** (equivalently the electrical angle $\theta=\omega\,\mathrm{TD}$), so the comparison is scale-free and T6's units choice cannot move a verdict.

**Coordinates (`phase-space-coordinate-check`).** The canonical claim lives in **frequency space** ($\omega/\omega_C$) and, for the supercell rung, in **reciprocal space** on the BCC reciprocal lattice. Measurement is in those coordinates: an `.AC` sweep returns frequencies, and they are compared against frequencies. The $\omega$-vs-$k$ discipline of `srs-band-structure.md:69-76` binds — **a frequency is never compared against a wavevector**, and no $\mathbf k$-label is compared at all (F2).

## §1.5 — `substrate-native-check` walk, re-run at IMPLEMENTATION time

The requirements §0.5 walk was Phase-0's, on the *requirements*. This one is on the **exporter**, which is new solver-adjacent code and re-triggers the skill. Walked **before the first line of exporter code was written.**

| checkpoint | walk result at implementation time |
|---|---|
| **CP1 — substrate dynamics** | Discrete **scatter + connect** wave propagation on a distributed LC transmission-line network (Op5 TLM). NOT Lagrangian minimisation, NOT gradient descent, NOT continuum-Helmholtz, NOT an energy basin. **Consequence for the exporter: the emitted primitive is a SPICE lossless `T` element, one per bond — the same mathematical object, no approximation.** The R56-ratified T2(a). |
| **CP2 — sector** | V-sector (scalar TLM) only; Cos-sector fenced out. Op14 off at $A=0$, so no sector coupling exists to leak. |
| **CP3 — AVE-native objective** | The TLM transmission eigenmode / network AC response — **explicitly NOT the lumped graph-Laplacian $\omega=\sqrt\lambda$**, the model the corpus REJECTED for failing the frozen $1/\sqrt3$ velocity gate. **This is the load-bearing exporter constraint and it is machine-enforced**: the exporter emits zero lumped `L`/`C` per node on any srs rung; a lumped tank appears only on L0, which is declared a solver-numerics smoke test and carries no srs topology. |
| **CP4 — coordinates** | Frequency space and reciprocal space, per §1 above. |
| **CP5 — local clock** | N/A by declaration: $A=0$ everywhere ⇒ $S(A)=1$ ⇒ $\omega_{local}=\omega_{global}$ uniformly. Recorded so its absence is a declared scope, not an omission. |
| **CP6 — reactance pair** | **Not triggered.** T4's selection here is frequency-domain `.AC`, not transient ringdown; there is no snapshot to mis-read. Had transient been selected, both the C-state and the L-state would have to be recorded across the window. Recorded so the non-trigger is a decision, not a gap. |
| **CP7 — sampling** | No PML anywhere (all networks are closed or explicitly port-terminated), so the PML-exclusion corollary is vacuously satisfied. **No top-K density extraction is used**; pole extraction is by reactance root-finding on the driving-point impedance, not by argpartition on a field array. |
| **CP8** | N/A — no emergence / hosting test. |
| **CP9** | Every observable is a **directly solved** network quantity on both sides: ngspice solves the MNA system; the engine side either diagonalises the engine's own one-step operator or evaluates the canonical arccos map on the engine's own adjacency. No algebraic heuristic on either leg. |
| **CP10** | No bulk force term anywhere. Terminations are rendered as **boundary conditions** ($\Gamma$ at a port), which is also the only way a netlist can express them. |

**Substrate-native verdict: the exporter emits `T` elements on the engine's own graph, and nothing else.** The SM/continuum default the walk exists to catch — reaching for a lumped `L`–`C` ladder because that is what a general-purpose netlist author reaches for first — is the T2(b) trap, and it is closed by ruling and by machine check.

---

## §2 — The frozen network ladder, the drive/observe pinning, and the extraction method

### §2.1 — Element values (all imported by symbol; the exporter has ZERO free parameters)

Per `SCX-REQ-ELEMENTS`, every value enters by import. **Nothing below is typed into the exporter.** The values in the "at HEAD" column are the fresh §7 reproduction-gate receipts on `766d5179`, recorded so this document's arithmetic is checkable — the exporter reads the symbols, not this table.

| quantity | canonical symbol | import path | value at HEAD `766d5179` |
|---|---|---|---|
| Line characteristic impedance | `Z_0` | `src/ave/core/constants.py` | $376.73031346177066\ \Omega$ |
| Node cutoff | `OMEGA_C` | `src/ave/core/constants.py` | $7.76344071105011\times10^{20}$ rad/s |
| Network projection | `ANALYTIC_NETWORK_FACTOR` | `src/ave/core/chiral_lattice_dynamics.py` | $0.5773502691896258$ |
| **Bond one-way delay (R2)** | **`ANALYTIC_NETWORK_FACTOR / OMEGA_C`** | derived from the two symbols above | $\mathbf{7.436783388682972\times10^{-22}}$ **s** |
| Cell tank inductance (L0 only) | `L_CELL` | `src/ave/core/constants.py` | $4.85262047439289\times10^{-19}$ H |
| Cell tank capacitance (L0 only) | `C_CELL` | `src/ave/core/constants.py` | $3.41912668394556\times10^{-24}$ F |
| Coordination | `net.degree` | `build_srs_net` | 3 |

**Derived reference frequencies (frozen):** $\omega_{link}=1/\mathrm{TD}=\sqrt3\,\omega_C$; band top $\theta=\pi \Rightarrow f_{top} = 1/(2\,\mathrm{TD}) = 6.723336876543721\times10^{20}$ Hz $=5.441398\ \omega_C$. Frequency-to-angle map, frozen: $\theta = 2\pi f\,\mathrm{TD}$, and $\omega/\omega_C = \theta/\texttt{ANALYTIC\_NETWORK\_FACTOR}$.

**TAGGED ENGINEERING CHOICES (every non-lattice-derived parameter, exhaustively).** Each is a solver-side numerical knob, none can move a verdict, and each is named so the "lattice-derived completeness" rule (epic §5.5) is satisfied by disclosure rather than by silence:

| # | choice | value | why it cannot move a verdict |
|---|---|---|---|
| EC-1 | Coarse `.AC` sweep point count | 20001 (LIN) | Only brackets roots; the reported frequency comes from the refinement, and TOL-GRID is COMPUTED and gated (§3.3). |
| EC-2 | Coarse sweep band | $f\in[10^{-3},\,1.0]\times f_{top}$ | Fixed by F1 (the comparison band IS $\omega\le\pi\,\omega_{link}$), not chosen for convenience. The lower edge excludes only the DC pole, which is separately accounted. |
| EC-3 | Root-refinement rounds | 3 | Convergence is MEASURED and reported per rung; the achieved bracket width is a receipt, not an assumption. |
| EC-4 | Residue probe offset $\delta$ | $10^{-6}$ (relative) | The multiplicity readout's separation ratio is COMPUTED and gated (§3.4). |
| EC-5 | Residue rank threshold | $10^{-2}$ (relative to $\sigma_{\max}$) | Sits $\ge2$ decades from BOTH populations by construction (§3.4); the achieved separation is reported. |
| EC-6 | ngspice `set numdgt=17` | 17 | Output precision only. Without it ngspice prints 7 digits and the instrument would be reporting its own formatter. |
| EC-7 | Emitted float format | Python `repr` (shortest round-tripping) | Guarantees the netlist's number re-reads to the identical double. Machine-checked (§5, CTRL-RT). |

**No other numerical parameter exists in the exporter or the driver.** If one appears during implementation it is a design defect under epic §5.4 and is reported as one, not tuned.

### §2.2 — The comparison ladder (fixed order; each rung gates the next)

| rung | object | engine / analytic side | solver side | legs | GATE (frozen) |
|---|---|---|---|---|---|
| **L0** | **P1-A** bare cell tank: one `L_CELL` ∥ one `C_CELL` | arithmetic identity from `constants.py`: $\omega_0=1/\sqrt{L_{CELL}C_{CELL}}=\omega_C$ | `.AC` driving-point pole | **2-way** (solver-vs-arithmetic) | pole within TOL-FREQ of $\omega_C$ |
| **L1** | **P1-B** one bond, open–open | closed form $\theta=\pi$ | `.AC` driving-point pole | **2-way** (see FL-3, §6.3) | pole within TOL-FREQ of $f_{top}$ |
| **L2** | **P1-C** $z=3$ vertex + 3 open stubs | closed form: $\theta=\pi/2$ (mult 2, **dark at the vertex**), $\theta=\pi$ (symmetric) | `.AC` driving-point poles at **two** drive nodes | **2-way** (see FL-3, §6.3) | every visible pole within TOL-FREQ; F6 accounting exact |
| **L3** | **P1-D** 4-site srs primitive cell, real periodic wrap ($K_4$ complete graph of 6 lossless lines) | **three-way**: arccos map on $\mathrm{eig}(A)$ **and** the ENGINE's own one-step TLM operator via `chiral_lattice.scalar_tlm_step` | `.AC`, all 4 drive nodes | **3-way** | TOL-FREQ + TOL-MULT + TOL-COUNT all exact |
| **L4** | **OBS-4** srs supercell, **$L=2$** (real periodic wrap; $N=64$ nodes, $B=96$ bonds) | **three-way**: arccos map on $\mathrm{eig}(A)$ of `build_srs_net(2)` **and** the ENGINE's `scalar_tlm_step` operator | `.AC`, all 64 drive nodes | **3-way** | TOL-FREQ + TOL-MULT + TOL-COUNT all exact |
| **AUX-B** | two-junction composite (§9, added under KEEP-BOTH; **SUPPLEMENTARY, NON-GATING**) | `ave.viz.ave_chart.two_junction_gamma` (ABCD transfer matrix) | `.AC` $\Gamma$ locus | 2-way, instrument-vs-instrument | TOL-GAMMA (§3.5); **cannot move the §4 bin** |

**$L=2$, frozen, with its reason.** $L=2$ is the smallest supercell that is a genuine 3D srs sample rather than a single primitive cell, and its full interior spectrum is already pinned by the Phase-0 receipts and re-derived fresh in §7. $L=3$ ($N=216$, $B=324$) is **NOT run**: it needs 216 drive-node `.AC` runs for the multiplicity readout and adds no structural content the $L=2$ mesh does not already carry. **This is a frozen scope decision, not a result-dependent one.**

**MESH fence, restated as a frozen expectation, so it cannot be discovered mid-run:** at $L=2$ the commensurate $\mathbf k$-mesh is coarse and **the highest interior mode sits at $\theta/\pi=0.7977$, i.e. $4.3406\,\omega_C$ — well below the true band top $5.4414\,\omega_C$.** *"The top is missing"* at $L=2$ is a **mesh artefact and is pre-registered as such.** The band top is reached at L1 (a single bond), where it is exact.

### §2.3 — Drive / observe pinning and the F6 dark-mode accounting (frozen BEFORE the run)

`SCX-REQ-FENCE` F6 requires the prereg to name the drive/observe points **and** the modes those choices make unobservable. *An unobservable mode is not a missing mode.*

| rung | drive | observe | modes PRE-DECLARED unobservable at that drive |
|---|---|---|---|
| L0 | current source into the tank node | that node | none |
| L1 | current source into node `n0` | `n0` | none in $0<\theta\le\pi$ |
| L2 | **two separate runs**: (i) the vertex `n0`; (ii) a stub end `n1` | the driven node | **(i) vertex drive: the $\theta=\pi/2$ differential pair is DARK** — those two modes have exactly zero voltage at the vertex, so a vertex-driven sweep returns only the symmetric $\theta=\pi$ family. **(ii) stub drive: nothing is dark.** The two runs together see every mode. |
| L3 | 4 separate runs, one current source per node | all 4 nodes each run | none (the full $Z(\omega)$ matrix is assembled) |
| L4 | 64 separate runs, one current source per node | all 64 nodes each run | none (the full $Z(\omega)$ matrix is assembled) |

**Driving with a current source does not perturb the network under test.** An ideal current source is an open circuit to the homogeneous problem, so the poles of the driving-point impedance are the natural frequencies of the *unmodified* network. Stated because it is the reason a driven measurement can report an undriven object's spectrum at all.

---

## §3 — Analytic expectations, frozen as FORMS **and** as VALUES

### §3.1 — The closed-form pole set of a node-driven lossless TL network (derived here, before the run)

**Why this derivation is in the prereg.** The T4-selected observable is a **node** driving-point `.AC` sweep. The Phase-0 fence F5 is a statement about the **port-space** spectrum of the discrete-time TLM one-step operator. Those are two different spaces, and the accounting rule for the measurement actually being taken has to be written down *before* the run or it becomes a mid-debug rationalisation. It is derived, not assumed:

For a network of identical lossless lines $(Z_0,\mathrm{TD})$ joined at shunt nodes, one line between nodes $u,v$ contributes to the node-admittance matrix $Y_{uu}\mathrel{+}=1/(jZ_0\tan\theta)$ and $Y_{uv}\mathrel{-}=1/(jZ_0\sin\theta)$, with $\theta=\omega\,\mathrm{TD}$. Summing over bonds, with $D$ the degree matrix and $A$ the adjacency,

$$Y(\theta)\;=\;\frac{1}{jZ_0\sin\theta}\Bigl(D\cos\theta-A\Bigr).$$

Natural frequencies are $\det Y=0$. For a $z$-regular graph, $D=zI$ and the condition is $\det(z\cos\theta\,I-A)=0$, i.e.

$$\boxed{\;\cos\theta=\mu_n/z \quad\Longleftrightarrow\quad \theta_n=\arccos(\mu_n/z),\qquad \omega_n=\omega_{link}\arccos(\mu_n/z)\;}$$

on the adjacency spectrum $\{\mu_n\}$ — **exactly the canonical arccos TL map** (`srs-band-structure.md` §2). Furthermore, near a root,

$$Z(\theta)\;=\;Y^{-1}\;\approx\;\frac{-jZ_0}{z\,(\theta-\theta_k)}\,P_k,\qquad P_k=\!\!\sum_{n:\ \mu_n=\mu_k}\!\! u_nu_n^{\!\top},$$

so **the residue matrix at each pole is a scalar times an orthogonal projector**: its rank is exactly the multiplicity of $\mu_k$ and its nonzero singular values are all equal. That is what makes the §3.4 multiplicity readout exact rather than heuristic.

### §3.2 — ⚑ F5-AC — a NEW accounting rule, added alongside F5 under KEEP-BOTH (F5 is not edited)

**F5 stands exactly as written in the requirements §6 and the skeleton §4.** It says a finite TLM network's natural-frequency set is not the arccos-map set: the graph's cycle space, $B-N+1$ modes, piles up at $\theta=0$ and at $\theta=\pi$ in the **one-step operator's port-space spectrum**. Verified fresh in §7: the $L=2$ supercell's TLM operator has $\theta=0$ at multiplicity 34 and $\theta=\pi$ at multiplicity 34, against a cycle space of $B-N+1=33$.

**F5-AC (this lane's addition, binding on the T4 measurement).** In the **node-space** driving-point impedance of the same network, the pole set is exactly the arccos set of §3.1 and **contains no cycle-space content**. The cycle-space modes are circulating line modes with zero voltage at every node, so they are structurally invisible to any node-driven, node-observed measurement. The two statements are consistent, and the dimension count closes: for $L=2$, port space $=2B=192$, and $192 = \underbrace{2\times62}_{\text{interior, }e^{\pm i\theta}\text{ pairs}}+\underbrace{2\times(1+33)}_{\theta=0\ \text{and}\ \theta=\pi\ \text{blocks}}$, against node space $N=64=62+1+1$.

**Consequence, frozen:** the L3/L4 comparison is against the **node-space** count — interior poles counted with multiplicity $=N-(\text{mult of }\mu=z)-(\text{mult of }\mu=-z)$ — and **an absence of the cycle-space block in the `.AC` result is a PASS, not a divergence.** Were F5 applied unmodified to the `.AC` measurement, a correct export would be scored as ~66 missing modes.

**This is surfaced, not absorbed.** F5-AC is a lane-derived accounting rule about the instrument, not a physics claim and not a correction to any corpus statement. It is flagged in §10 for auditor review, and it is the one place this prereg extends the skeleton's fence set rather than filling it in.

### §3.3 — Frozen tolerance axes

| axis | quantity | frozen value | how it is enforced |
|---|---|---|---|
| **TOL-GRID** | coarse sweep step ÷ smallest reference mode spacing at that rung | **$\le 1.0\times10^{-2}$** | **COMPUTED per rung and GATED.** Set BEFORE TOL-FREQ, per the skeleton's instrument-resolution clause. |
| **TOL-REFINE** | achieved relative bracket half-width at the end of root refinement | **$\le 1.0\times10^{-9}$** | COMPUTED per pole; a pole that does not converge routes to `INCONCLUSIVE`, never to a bin. |
| **TOL-FREQ** | $\bigl|\omega_{solver}/\omega_{ref}-1\bigr|$ per matched mode | **$\le 1.0\times10^{-7}$** | gating, PRIMARY |
| **TOL-MULT** | per-frequency multiplicity | **exact integer match** | gating |
| **TOL-COUNT** | total interior mode count, after the F5-AC accounting | **exact integer match** | gating |
| **TOL-LOSSLESS** | $\max_f\bigl|\mathrm{Re}\,Z/\mathrm{Im}\,Z\bigr|$ over every sampled point | **$\le 1.0\times10^{-9}$** | gating — the receipt that the emitted network really is lossless (Regime I). A nonzero real part means a resistive element leaked into the export. |

**TOL-FREQ's value, justified rather than asserted.** It sits **two decades above** the measured instrument floor (the L1 refinement reaches the analytic pole at relative error below $10^{-9}$; see EC-3's reported receipt) and **six decades below** the smallest structural error class the comparison exists to catch (an R1-for-R2 label swap is a $\sqrt3-1=7.3\times10^{-1}$ relative offset; a one-part-in-$10^4$ delay error is $10^{-4}$). Both directions are stated because *a tolerance the instrument cannot resolve always passes, and a tolerance the instrument cannot meet always fails.*

### §3.4 — The frozen extraction method (T4 = `.AC` driving-point)

1. **Emit** the netlist from the engine graph (§2.1 values, R2 delay).
2. **Coarse `.AC` LIN sweep**, EC-1/EC-2, one run per drive node; record $X(f)=\mathrm{Im}\,Z_{jj}(f)$ and $\mathrm{Re}\,Z_{jj}(f)$.
3. **Losslessness receipt**: TOL-LOSSLESS over every sampled point. Fail ⇒ the export is not lossless ⇒ `DIVERGE-ATTRIBUTED` to the exporter.
4. **Bracket**: a **pole** is a sign change of $X$ across which $|X|$ diverges (equivalently, a sign change of $1/X$ with $|X|$ large on both sides). A sign change with $|X|$ small on both sides is a **zero** of the driving-point impedance and is NOT a pole. Foster's reactance theorem guarantees poles and zeros alternate on a lossless network, so this classification is exhaustive.
5. **Refine**: $1/X$ is analytic and vanishes linearly at a pole, so refine by linear interpolation of $1/X$ across the bracket, EC-3 rounds, each round re-sampling a narrowed window by a fresh single-point `.AC`. Terminate at TOL-REFINE; report the achieved width.
6. **Multiplicity**: at $f_{probe}=f_{pole}(1+\delta)$, EC-4, assemble the full $N\times N$ matrix $Z(f_{probe})$ from the $N$ drive-node runs and take its SVD. By §3.1 the pole term dominates and its residue is a scaled orthogonal projector, so the multiplicity is $\#\{\sigma_i>\text{EC-5}\cdot\sigma_{\max}\}$. **The separation ratio $\sigma_{m}/\sigma_{m+1}$ is COMPUTED and REPORTED at every pole**; a separation below $10^{2}$ routes to `INCONCLUSIVE` rather than being read through.
7. **Compare** against the engine/analytic reference set on the SAME axis ($\omega/\omega_C$), interior band $0<\theta<\pi$ per F1 and F5-AC.

**The extraction reads no reference value.** Steps 2–6 do not consume any engine-side or canonical frequency; the reference set enters only at step 7. This is the ANTI-TAUTOLOGY control (§5) stated as an algorithm property.

### §3.5 — AUX-B tolerance

| axis | quantity | frozen value |
|---|---|---|
| **TOL-GAMMA** | $\max_\theta\bigl|\Gamma_{ngspice}(\theta)-\Gamma_{ave\_chart}(\theta)\bigr|$ over the frozen $\theta$ grid (complex modulus of the difference) | **$\le 1.0\times10^{-12}$** |
| **TOL-GAMMA-DC** | $\bigl|\Gamma(\theta{=}0)-(-3/5)\bigr|$ and $\bigl|\Gamma(\theta{=}\pi/2)-(-3/7)\bigr|$, ngspice side | **$\le 1.0\times10^{-12}$** each |

AUX-B $\theta$ grid, frozen: 361 points, $\theta\in[0,2\pi]$ inclusive, LIN in $\theta$ (hence LIN in $f$ through $\theta=2\pi f\,\mathrm{TD}$). **AUX-B is R1/R2-INVARIANT**: it is parameterised by the electrical angle $\theta$ directly, so the label convention cancels out of the comparison entirely. Recorded so AUX-B is not miscounted as a convention check.

### §3.6 — The frozen reference sets (values, re-derived fresh at GO under §7)

**L0 (P1-A):** $\omega_0/\omega_C = 1$ exactly; $f_0 = 1.2355899645644838\times10^{20}$ Hz.

**L1 (P1-B, one bond, open–open):** $D=\mathrm{diag}(1,1)$, $A$ the single-edge adjacency ($A_{01}=A_{10}=1$) ⇒ $\cos\theta=\pm1$ ⇒ **no interior pole**; the single resonance is the boundary root $\theta=\pi$, $f=6.723336876543721\times10^{20}$ Hz $=5.441398\,\omega_C$. **This is the half-wave / Bragg object and the CONVENTION CONTROL's measurement point.**

**L2 (P1-C, vertex + 3 open stubs):** $D=\mathrm{diag}(3,1,1,1)$, star adjacency. Solving $\det(D\cos\theta-A)=0$: the $v_0=0$ branch requires $\cos\theta=0$ ⇒ $\theta=\pi/2$ with a **2-dimensional** solution space ($\sum_i v_i=0$) — **the differential pair, exactly zero at the vertex**; the $v_0\ne0$ branch gives $\cos^2\theta=1$ ⇒ $\theta\in\{0,\pi\}$ — the symmetric family. Frozen: **vertex drive ⇒ interior pole count 0**; **stub drive ⇒ one interior pole at $\theta=\pi/2$, $f=3.3616684383\times10^{20}$ Hz $=2.720699\,\omega_C$, multiplicity 2**; both drives see $\theta=\pi$.

**L3 (P1-D, $K_4$ complete graph of 6 lines):** $\mu=\{3,-1,-1,-1\}$. Frozen: **one interior pole, $\theta=\arccos(-1/3)=1.9106332362490184$, $f=4.0889549701\times10^{20}$ Hz $=3.309314\,\omega_C$, multiplicity 3** — the canonical Γ-point optical multiplet $\sqrt3\arccos(-1/3)$. **Interior count $=3$.** Note $K_4$ is NOT bipartite ($\mu_{\min}=-1\ne-3$), so **there is no $\theta=\pi$ root at L3** — a frozen structural discriminator: a $\theta=\pi$ pole appearing at L3 is an exporter defect.

**L4 (srs supercell $L=2$; $N=64$, $B=96$):** frozen interior set, **10 distinct $\theta$, total multiplicity 62** ($=64-1-1$; the $\mu=+3$ uniform mode is the DC root and the $\mu=-3$ mode is the $\theta=\pi$ root, both boundary):

| # | $\theta$ | $\omega/\omega_C$ | multiplicity |
|---:|---|---|---:|
| 1 | 0.635563 | 1.100821 | 6 |
| 2 | 0.729728 | 1.263929 | 6 |
| 3 | 0.955317 | 1.654648 | 4 |
| 4 | 1.230959 | 2.132133 | 9 |
| 5 | 1.432283 | 2.480786 | 6 |
| 6 | 1.709310 | 2.960614 | 6 |
| 7 | 1.910633 | 3.309314 | 9 |
| 8 | 2.186276 | 3.786800 | 4 |
| 9 | 2.411865 | 4.177519 | 6 |
| 10 | 2.506030 | 4.340627 | 6 |
| | | **TOTAL** | **62** |

**All values above are re-derived fresh at run time from `constants.py` + `build_srs_net` (§7). The table is the frozen expectation, not the input to the comparison** — the comparison consumes the freshly computed reference, and any drift between this table and the fresh values is itself a finding banked under a dated note.

---

## §4 — VERDICT GRAMMAR: outcome bins (mutually exclusive, exhaustive)

| bin | criterion |
|---|---|
| **AGREE** | Every rung L0–L4 within its frozen tolerance (TOL-FREQ, TOL-MULT, TOL-COUNT, TOL-LOSSLESS all pass), **and** every §5 fence accounted for with no unexplained mode, **and** the POSITIVE CONTROL fired. |
| **DIVERGE-ATTRIBUTED** | At least one rung outside tolerance, **and** the §6 protocol localises it to exactly one of {exporter, solver numerics, engine} with a receipt. **A valid, bankable outcome — the engine-side arm is the single most valuable result the epic can produce.** |
| **DIVERGE-UNATTRIBUTED** | Outside tolerance and the §6 protocol runs to completion without localising. **Fires the epic §8 KILL: the instrument is unsound; bank the negative and stop.** |
| **INCONCLUSIVE** | The run did not produce a comparable number: solver non-convergence, a pole that failed TOL-REFINE, a multiplicity separation below $10^2$, a network that would not build, or a POSITIVE-CONTROL failure. **Mandatory bin — never folded into any other.** |

**Bin-integrity check (run now, before any value exists):** every falsifier in §5 routes to exactly one bin; no falsifier routes to two; `INCONCLUSIVE` is reachable independently of the physics (a solver crash reaches it with the network correct). ✅

**AUX-B is binned separately** (§9) and **cannot move the bin above**.

---

## §5 — Controls and falsifiers (**UNRUN ≠ PASSED**)

**POSITIVE CONTROL (mandatory before any agreement is bookable).** Re-emit the L3 netlist with **one** bond's `TD` multiplied by a frozen factor **1.05** and confirm the comparison **resolves the planted defect** and bins it `DIVERGE-ATTRIBUTED`. *A comparison that cannot detect a planted defect cannot certify an agreement.* The planted-defect run is emitted to its own netlist file and is never mistaken for the clean one (distinct filename, and the header records the mutation).

**NEGATIVE CONTROL.** L1 (the single bond) is a network with no srs content whatever. Confirm **no srs-specific structure appears** in it: its interior pole count is 0 and its only root is the wiring-theorem half-wave. Guards against the pipeline manufacturing structure.

**ANTI-TAUTOLOGY CONTROL (machine-enforced).** The exporter must not read any reference frequency, and the comparison harness must not feed reference values into the netlist. Enforced by a test asserting the exporter module imports **no** band-structure symbol and that no emitted netlist contains any reference frequency.

**CONVENTION CONTROL (the FL-1 hazard, converted to a measurement).** Emit and run **both** label conventions once at L1 and confirm the measured resonance ratio is **exactly $\sqrt3$** to within TOL-FREQ. The R1 netlist is emitted with `TD` $=\ell_{node}/c_0$ from `bond_lc()` — *the symbol an exporter author would wrongly reach for* — so the control measures the actual hazard, not a paraphrase of it.

**FL-1 MACHINE CHECK (mandated by the brief's FL-1 and by R56 §2).** A test asserts the exporter's emitted `TD`:
- **equals** `ANALYTIC_NETWORK_FACTOR / OMEGA_C` (R2, the declared convention) to bit-exactness, both symbols imported;
- **differs from** the R1 delay reachable through `bond_lc()` (`chiral_lattice.py`), with the ratio $\sqrt3$ to machine precision;
- **differs from** the *third* live convention FL-1(iii) names, $\sqrt3\,\ell_{node}/c_0$ (`r10_v8_ee_phase_a.py`), with the ratio 3.
- **fires in both directions**: a mutation fixture builds the R1 delay and asserts the R2 assertion WOULD fail on it, so the gate is provably able to fire rather than vacuously green.

**ROUND-TRIP CONTROL (CTRL-RT).** Every numeric emitted into a netlist is re-parsed from the emitted text and asserted bit-identical to the source double. Guards the one place a `%g` format could silently truncate a canonical constant.

**T6 SI/NATIVE PAIRED CONTROL (R56 §3 selection).** Every rung is emitted and run **twice** — once in SI, once in native/normalised units ($Z_0=1$, $\mathrm{TD}=1$) — and the two runs' **dimensionless** $\theta$ sets must agree within TOL-FREQ. This is T6(c)'s paired run, pre-positioned as the §6(b) solver-numerics check.

**Falsifier list (each routes to exactly one §4 bin):**

| # | falsifier | bin |
|---|---|---|
| FS-1 | Any rung outside TOL-FREQ, localised by §6 | DIVERGE-ATTRIBUTED |
| FS-2 | Any rung outside TOL-FREQ, not localised after §6 runs to completion | DIVERGE-UNATTRIBUTED (**epic KILL**) |
| FS-3 | Mode count or multiplicity mismatch after the F5-AC accounting | DIVERGE-ATTRIBUTED or -UNATTRIBUTED per §6 |
| FS-4 | Positive control fails to resolve the planted defect | INCONCLUSIVE (instrument not validated; **no agreement may be booked**) |
| FS-5 | Convention control does not return exactly $\sqrt3$ | DIVERGE-ATTRIBUTED to exporter |
| FS-6 | Solver non-convergence / TOL-REFINE failure / multiplicity separation $<10^2$ / network will not build | INCONCLUSIVE |
| FS-7 | TOL-LOSSLESS exceeded (a resistive element leaked into an srs export) | DIVERGE-ATTRIBUTED to exporter |
| FS-8 | SI and native runs disagree beyond TOL-FREQ | DIVERGE-ATTRIBUTED to solver numerics |
| FS-9 | FL-1 machine check fails, in either direction | DIVERGE-ATTRIBUTED to exporter (**and the run is not bookable**) |

**Observable robustness ladder.** PRIMARY (gating) = frequency agreement per matched mode (TOL-FREQ) and exact mode/multiplicity accounting (TOL-MULT, TOL-COUNT). SUPPLEMENTARY, never gating = peak amplitudes, $Q$ values, phase slopes — all of which depend on the sweep grid and the terminations, not on the physics under comparison.

---

## §6 — Divergence adjudication protocol (epic §5.3, fixed order) and the GO-time resolution of the named open items

### §6.1 — The three suspects, fixed order

1. **(a) EXPORTER.** Hand-audit the emitted netlist against the graph and `constants.py`. **The netlist is human-readable by design and carries every imported symbol in its header** (`SCX-REQ-ELEMENTS.2`), so this is mechanical. Cross-check node/bond counts against $8L^3$ / $12L^3$. Every emitted netlist is TRACKED for exactly this purpose.
2. **(b) SOLVER NUMERICS.** Integrator/tolerance sweep on the solver side; re-run at finer TOL-GRID; re-run under the other units scaling — **the T6 SI/native paired control (§5) is exactly this check, pre-positioned**. Second solver (Xyce) only if T1(b) is later ratified and installed; **it is not installed and is not procured by this lane**.
3. **(c) ENGINE.** What remains. L1/L2's analytic anchor localises (a)-vs-(c) before either is trusted at L3/L4 scale, subject to §6.3. **L0 sits below the anchor** as the solver-vs-arithmetic numerics smoke test, and **an L0 pass does not clear (b) globally** — L0 is a lumped tank, whereas L1–L4 export the bond as a TL element and add network scale, so step (b) still runs its own check at divergence time.

**No tuning to agreement.** The exporter has no free parameter by construction: topology from the engine, values from `constants.py`, EC-1…EC-7 all solver-side and all incapable of moving a verdict (§2.1). **If a knob appears that would let the export be tuned toward agreement, that knob is a design defect in the exporter and is reported as one** (epic §5.4).

### §6.2 — FL-1 — resolved for the exporter, OPEN for the corpus

R56 §2 pins **R2 as a TAGGED ENGINEERING CONVENTION for the exporter only**, mandates the machine check, and explicitly leaves the corpus's physics-level flag OPEN. This lane executes exactly that: the FL-1 machine check (§5) and the CONVENTION CONTROL (§5). **R56 §4 additionally rules that the `bond_lc` symbol rename is NOT ruled and stays an open lane proposal — this lane renames nothing, re-words nothing and re-derives neither site.**

### §6.3 — FL-3 — resolved as TWO-WAY at L1/L2; the epic's three-way anchor survives at L3/L4

`scatter_matrix(n)` raises `ValueError("n must be >= 2")` (`src/ave/core/chiral_lattice.py:99-100`), so the engine cannot build an open-terminated **1-port** node. The requirements name two ways out: **(a)** relax the guard — *"a small engine touch that needs its own justification and is NOT authorized here"* — or **(b)** run those objects two-way.

**FROZEN DECISION: (b).** R56 did not authorize an engine touch and this lane owns zero physics decisions, so **the engine is not modified.** Consequences, stated rather than hidden:

- **L1 and L2 are TWO-WAY** (analytic-vs-solver). The epic §4 Phase-1 wording — *"BOTH the engine and the solver are first checked against the closed-form value independently"* — is **not** satisfied at L1/L2, and **the epic's three-way localisation claim is correspondingly weakened at those rungs.**
- **L3 and L4 ARE genuinely THREE-WAY**, and this is the mitigation that makes the loss tolerable: every node in the $K_4$ complete graph and in the srs supercell has degree 3, so the engine's own `scatter_matrix(3)` and `chiral_lattice.scalar_tlm_step` run unmodified. The engine leg at L3/L4 is the **engine's shipped code path**, exercised by applying `scalar_tlm_step` to unit basis vectors to assemble its one-step operator — not a re-implementation of it.
- **Any P1-B/P1-C one-port formula used anywhere in this lane is disclosed as a formula, not an engine code path** (`ave-driver-script-honesty`): the closed form $S_{ij}=2/n-\delta_{ij}$ extends to $n=1$ giving $S=[+1]$, and the guard is therefore a guard, not a physics gap — but the engine does not execute it and this lane does not pretend otherwise.

### §6.4 — Q1 — UNANSWERED at freeze; F1 is stated as INSTRUMENT SCOPE ONLY

The requirements §8.1 asked Grant one plumber-physical question — *does a vacuum bond ring at its FULL-wave, or is the half-wave the top by construction?* — and it is **not answered as of this freeze.** R56 did not address it.

**Frozen consequence:** **F1 is stated in this prereg as an instrument-scope statement and nothing more.** The comparison band is $\omega\le\pi\,\omega_{link}$ because that is what the engine's discrete-time TLM can represent; **solver modes above the band top are EXPECTED, are NOT divergences, and this document takes NO position on whether they are physical.** No Phase-1 result may be read as bearing on Q1 in either direction. The question is re-routed to Grant, unchanged, in §10.

---

## §7 — Reproduction gate (epic §5.2) — RUN AT GO, BEFORE ANY EXPORT

**Every engine-side reference is re-derived on the current engine at comparison time.** The Phase-0 §7 receipts are **NOT** load-bearing. The gate below was run at GO on this branch's HEAD `766d5179` (Phase 0 ran on `ff0fde8b`), **before any exporter code existed**, and is re-run by the tracked driver at comparison time.

| receipt | Phase-0 banked (`ff0fde8b`) | fresh at GO (`766d5179`) | drift |
|---|---|---|---|
| `Z_0` | 376.73031346177066 | 376.73031346177066 | none |
| `OMEGA_C` | 7.76344071105011e+20 | 7.76344071105011e+20 | none |
| `ANALYTIC_NETWORK_FACTOR` | 0.5773502691896258 | 0.5773502691896258 | none |
| TD under R2 | 7.436783388682972e-22 s | 7.436783388682972e-22 s | none |
| TD under R1 | 1.2880886674083153e-21 s | 1.2880886674083153e-21 s | none |
| R1/R2 ratio | 1.732050807568877 | 1.732050807568877 | none |
| scalar band envelopes (48³) | [0,2.1321] [1.6547,3.3093] [2.1321,3.7867] [3.3093,5.4414] | identical to 4 dp | none |
| global band top | 5.4414 $\omega_C$ | 5.4414 $\omega_C$ ($\pi\sqrt3$) | none |
| Γ multiplet | {0, 3.3093 ×3} | {0, 3.3093 ×3} | none |
| H point | $\mu=\{-3,1,1,1\}$ | $\mu=\{-3,1,1,1\}$ | none |
| srs $L=3$ bipartite | 108/108, $\mu=\pm3$, $\lambda_{\max}=6$ | 108/108, $\mu_{\min}=-3.0000000000$, $\mu_{\max}=+3.0000000000$, $\lambda_{\max}=6.0000000000$ | none |
| $K_4$ complete TLM operator | 0(×4), 1.910633(×6), π(×2) | 0(×4), 1.910633(×6), π(×2) | none |
| P1-C TLM operator | 0(×1), π/2(×4), π(×1) | 0(×1), π/2(×4), π(×1) | none |
| P1-B TLM operator | 0(×1), π(×1) | 0(×1), π(×1) | none |
| srs $L=2$ TLM operator | θ=0 ×34, θ=π ×34, 10 interior | θ=0 ×34, θ=π ×34, 10 interior, mults [6,6,4,9,6,6,9,4,6,6] | none |
| $L=2$ highest interior | 0.7977 π = 4.3406 $\omega_C$ | 0.7977 π = 4.3406 $\omega_C$ | none |

**REPRODUCTION GATE: PASS on every scalar-channel number this lane consumes. ZERO drift between `ff0fde8b` and `766d5179`.**

**Demotion re-check at GO (skeleton §7).** Re-verified on this branch: `srs-band-structure.md` §1 (`:27-47`), §2 (`:49-76`), §5(c) (`:136-140`) and §6 (`:145-146`, `:153-157`) carry **no demotion marker**; `translation-circuit.md:189` and `:884-888` are **CLEAN**. The R2 adjudication flag at `:157` is re-verified present and still reading *"Flagged for adjudication"* — quoted verbatim in §0.

---

## §8 — Deliverables (fixed order)

1. **This frozen prereg** — committed ALONE and PUSHED before any exporter code, netlist or comparison number exists.
2. **The exporter** — `src/ave/solvers/scx_spice_export.py`, carrying the `SCX-REQ-ELEMENTS.2` canonical-source assertion, the `net.carrier == "srs-z3"` guard, and the symbol-echo netlist header.
3. **The machine-checked tests** — `src/tests/test_scx_spice_export.py`, including the FL-1 both-directions delay-convention gate (§5).
4. **The emitted netlists**, tracked under `research/netlists/2026-08-25-scx-phase1/` — the §6.1(a) hand-audit artifact.
5. **The comparison driver + its output record** — `src/scripts/vol_1_foundations/scx_phase1_crosscheck.py` and its JSON.
6. **`research/2026-08-25_solver-crosscheck-phase1_result.md`** — verdict in exactly one §4 bin, register re-declared, every fence's accounting shown.
7. **Phase-2 GO recommendation, or the epic-KILL record.**

**Reuse, not rebuild (Rule 14).** The ngspice subprocess hook already exists in-tree at `src/ave/bench/spice_runner.py` (`run_ngspice`, `read_wrdata`, `ngspice_available`). This lane **uses it** and writes no second runner. See §10 FL-5 — its existence is not cited anywhere in the Phase-0 planning pair, which is surfaced as a flag rather than silently absorbed.

---

## §9 — AUX-B: the ave-chart two-junction composite (ADDITION under KEEP-BOTH; SUPPLEMENTARY)

**Provenance of the ask.** The means-test register at [`research/2026-08-24_ave-chart-instrument_note.md`](2026-08-24_ave-chart-instrument_note.md) §7 names a **Class B — cross-solver** row, verbatim: *"the two-junction composite's Γ(ω) and the graded loci, measured in **ngspice** on the exported netlist and overlaid on fig 2/3 — same objects, two independent computational routes (transfer matrix vs MNA)"*, status *"PLANNED — rides the Phase-1 satellite."*

**It fits this lane's frozen scope and is therefore run**, as an explicitly-labelled ADDITION to the skeleton's L0–L4 ladder. Under the KEEP-BOTH pattern it is added **alongside**; **no skeleton rung is redefined, renamed or re-cut.**

**The object.** One lattice bond spanning two $z=3$ vertices, fed from a cold semi-infinite $Z_0$ bond: near vertex = shunt $Z_0/2$, line of electrical length $\theta$ at $Z_0$, far vertex = $Z_0/2$ load. Netlist primitives: one `T` element $(Z_0,\mathrm{TD})$ — **the same ratified T2(a) primitive** — plus two resistors.

**⚠ The two resistors are PORTS, not substrate elements — declared, because they sit against this document's Regime-I lossless-reactive header.** A $Z_0/2$ resistor is the SPICE rendering of a *reflectionless semi-infinite lossless bond pair*; no energy is dissipated in the substrate, it leaves through a matched port. **AUX-B is therefore the ONE rung in this prereg whose netlist is not resistor-free, and TOL-LOSSLESS does not apply to it.** The isolated/incoherent scoping of the composite is inherited verbatim from `two_junction_gamma`'s own docstring and is NOT relaxed here.

**What AUX-B does and does not establish.**
- **DOES:** cross-check the `ave_chart` ABCD transfer-matrix route against ngspice's MNA route on the same composite — implementation-verification of a **plotting instrument**.
- **DOES NOT:** bear on the engine, on the srs band structure, or on any physics. It is the register's **class B (machinery)**, explicitly not its class C.
- **Cannot move the §4 bin.** Its own pass/fail is reported separately under TOL-GAMMA (§3.5).

**Frozen AUX-B anchors** (both already canonical in the instrument note, so this is a reproduction not a new claim): $\Gamma(\theta{=}0)=-3/5$ and $\Gamma(\theta{=}\pi/2)=-3/7$.

---

## §10 — Routed flags (surfaced, NOT fixed by this lane)

| # | flag | route |
|---|---|---|
| **F5-AC** | This prereg adds a node-space accounting rule alongside F5 (§3.2), derived in closed form. F5 itself is untouched. It is a statement about the T4 instrument, not about the substrate — but it is a lane-authored extension of a pre-registered fence set and should be reviewed as one. | auditor lane (review at PR) |
| **FL-1** | Unchanged and still OPEN at corpus level per R56 §2. Three live in-tree bond-delay conventions, re-verified on this branch: `bond_lc()` ⇒ $1/\omega_C$ (R1); `ANALYTIC_NETWORK_FACTOR` ⇒ $1/(\sqrt3\,\omega_C)$ (R2, pinned here); `r10_v8_ee_phase_a.py:255` `bond_length_SI = np.sqrt(3.0) * L_NODE` ⇒ $\sqrt3/\omega_C$ (a third, $3\times$ the R2 delay). | auditor lane; the `bond_lc` rename stays an open lane proposal per R56 §4 |
| **FL-2** | Two stale line-cites inside `srs-band-structure.md`, re-verified still stale on this branch: `:145` cites `constants.py:294` for `OMEGA_C` (real site `:305`); `:117` cites `:770` for `V_LONG` (real site `:781`). Pure line-drift, content correct at both real sites. | auditor lane (cite-repair sweep) |
| **FL-3** | Resolved for Phase 1 as TWO-WAY at L1/L2 (§6.3). The `scatter_matrix` $n<2$ guard is untouched. | closed for this phase; the engine-touch option remains available to a future phase with its own justification |
| **Q1** | **Still unanswered and re-routed to Grant, unchanged.** Does a vacuum bond ring at its full-wave, or is the half-wave the top by construction? It decides whether F1 is framed as an instrument ceiling or as physics, and therefore what a Phase-2 result doc may say about modes above the band top. **This prereg takes no position** (§6.4). | **Grant** (plumber-physical) |
| **FL-5** | **NEW, lane-surfaced.** The Phase-0 planning pair (requirements + trade study) analyses the ngspice adoption as if the repo had no ngspice infrastructure — T1 states *"neither solver is currently a repo dependency"*, which is true of the dependency question, but neither doc cites the in-tree ngspice hook `src/ave/bench/spice_runner.py`, the `_orchestration/2026-07-03_spice-lane-charter.md` SPICE lane, or the five `src/scripts/vol_4_engineering/spice_ladder_rung*.py` drivers that already run ngspice. **No Phase-0 conclusion is thereby wrong** — T1's selection of ngspice is if anything strengthened — but the option analysis was written without its own prior art in view. **This lane reuses `spice_runner.py` rather than rebuilding it (§8) and does not edit the Phase-0 docs.** | auditor lane / orchestrator (Phase-0 doc currency) |

---

## §11 — Anti-rescue guard

Real odds that this returns `DIVERGE` on some rung are **substantial and expected** — F1, F5/F5-AC and F6 each describe a way a *correct* export produces a mode set that does not match a naive reference, and the whole point of writing them down first is that discovering one mid-run must not become a licence to re-cut a bin. **A `DIVERGE-ATTRIBUTED` verdict against the engine is the epic's most valuable outcome and must be reported as a finding, not debugged toward agreement** (Rule 11: honest closure; the wrong reaction is a rescue, the right reaction is a clean result with the mechanism named).

**Explicitly forbidden after this push:** widening a tolerance, re-labelling a bin, dropping a rung, re-cutting the interior band, adding an exporter knob, or converting an `INCONCLUSIVE` to an `AGREE` by re-running with different EC values. Any of these is a Rule-12 dated amendment with its own justification, or it does not happen.

---

## §12 — Skill-selection plan for Phase-1 execution (declared at freeze; retro-pass at phase close)

`ave-prereg` (this freeze-by-push event) · `substrate-native-check` (§1.5, walked before the exporter's first line) · `ave-canonical-source` (every exporter import) · `ave-driver-script-honesty` (exporter + comparison driver; the FL-3 disclosure in §6.3 is its output) · `ave-reproduction-gate` (§7) · `verify-before-cite` (every reference pointer re-verified on this branch at GO) · `phase-space-coordinate-check` (§1 coordinates: frequency-space claim, frequency-space measurement) · `consistency-vs-emergence` (register declared in §1, re-declared in the result doc) · `ave-independence-check` (what agreement does and does not establish — §9 and the result doc's scope paragraph) · stop-and-ask (2-attempt cap; a physics surprise is a stuck-point, not a judgment call).
