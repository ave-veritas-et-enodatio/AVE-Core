# PHASE-1 RESULT — external-solver cross-check, pilot scale

**Date:** 2026-08-25 · **Branch:** `research/2026-08-25-solver-crosscheck-phase1` · **Base:** `origin/main` @ `766d5179`
Prereg-file: research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md
Prereg-commit: 737ba888
*(the prereg was frozen and **pushed before any exporter code, netlist or comparison number existed in the tree** — freeze-by-push)*
**GO gate:** [`_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md`](../_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md) (R56)
**Epic:** [`_orchestration/2026-08-23_external-solver-crosscheck-epic.md`](../_orchestration/2026-08-23_external-solver-crosscheck-epic.md) §4 Phase 1
**Artifacts:** driver [`src/scripts/vol_1_foundations/scx_phase1_crosscheck.py`](../src/scripts/vol_1_foundations/scx_phase1_crosscheck.py) · exporter [`src/ave/solvers/scx_spice_export.py`](../src/ave/solvers/scx_spice_export.py) · tests [`src/tests/test_scx_spice_export.py`](../src/tests/test_scx_spice_export.py) · record `research/drivers/scx_phase1_crosscheck_results.json` · netlists `research/netlists/2026-08-25-scx-phase1/`
**Solver:** ngspice-46 (KLU direct linear solver), `/opt/homebrew/bin/ngspice`

---

## §0 — VERDICT

> # `AGREE`
>
> ### — reachable **only under Rule-12 amendment A1**. Read the box below it before quoting it.
>
> Every gating rung **L0–L4** met its frozen tolerance **as amended by A1**. The marquee number: on the **srs $L=2$ supercell (64 nodes, 96 bonds)** ngspice and the engine agree on **all 10 distinct interior mode frequencies to $\le4.9\times10^{-10}$ relative**, with **all 10 multiplicities exactly matched** and the total interior mode count **62 vs 62 exact**.

### ⚠ THE BIN THAT MOVED — stated here, not only in §6

**Under the as-frozen EC-2 band this run does not bin `AGREE`.** The paired control this lane itself ran and shipped (`controls.amendment_a1_paired`) records `lossless_pass = false` on the **as-frozen** band at **L3** (`0.00012398271634903263`) and **L4** (`0.0005036554694722908`), against TOL-LOSSLESS `1.0e-9`. The prereg's falsifier **FS-7** routes a TOL-LOSSLESS exceedance to `DIVERGE-ATTRIBUTED` to exporter, and its `AGREE` criterion requires *"TOL-FREQ, TOL-MULT, TOL-COUNT, **TOL-LOSSLESS** all pass"*. So, in one sentence:

> **`AGREE` under amendment A1; under the as-frozen EC-2 band the run bins `DIVERGE-ATTRIBUTED` on the TOL-LOSSLESS axis at L3/L4.**

A1's closing list says it does not *"convert an `INCONCLUSIVE` into an `AGREE`"*. That is narrowly true and it steps around the bin that actually moved — **A1 is bin-moving**, and this box is the correction (landed at the PR clearing review; §7 routes it). What survives the correction, and is why the bin move is not a rescue: both bands were run, both are reported, the **interior** verdict is byte-for-byte identical under both on all three rungs (§6), FS-7's named mechanism (a resistive element in an srs export) is machine-checkably absent, and A1's replacement mechanism — a singular MNA solve at a band edge that coincides with $\theta=\pi$ — is measured rather than asserted. **None of that changes which bin the as-frozen criterion selects.** The reader who wants the un-amended answer gets `DIVERGE-ATTRIBUTED` at L3/L4, and the FAIL is on the auxiliary losslessness axis, not on any frequency, count or multiplicity.

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting any number above

**Class: IMPLEMENTATION-VERIFICATION** (a sub-class of CONSISTENCY), declared in the prereg §1 before the first run and re-declared here per epic §7.

- **It establishes:** the engine solves its own equations correctly at pilot scale. Two independently-developed integrators — our in-house TLM and Sandia-lineage industrial SPICE — handed the *same* network with the *same* canonical element values, report the *same* resonances.
- **It does NOT establish anything about the vacuum.** It is **not** an emergence result, **not** a chord, **not** a falsification of AVE, and **not** evidence that the axioms describe physical reality. It mints nothing: no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`, no KB leaf edited, no solidity moved, no register touched.
- **The band-top reproduction is an EXPORTER-INTEGRITY GATE, not independence** (F4, epic §4 Phase 2). $\pi\,\omega_{link}$ is a theorem of {3-regular, bipartite, identical lossless lines}; a solver reproducing it verifies the exporter built such a net. **The independence weight rests entirely on the L4 interior spectrum**, whose values the Phase-0 honeycomb contrast showed are NOT fixed by that premise set.
- **…and the GATED L4 comparison is closed-form-vs-numerics on ONE formulation, not two.** Prereg §3.1 derives the arccos map **from** $Y=(D\cos\theta-A)/(jZ_0\sin\theta)$ — *the same MNA formulation ngspice solves*. **The arccos leg is ngspice's own closed form.** So the marquee `4.852624968521013e-10` validates ngspice's KLU solve, Foster bracketing and secant refinement against the analytic roots of the matrix ngspice is factoring; it carries no engine content beyond the adjacency, and the adjacency reaches both legs through the exporter. The genuinely cross-formulation content — scatter+connect, `scatter_matrix(3)`, $\Gamma=-1/3$, no nodal admittance matrix assembled anywhere — is the **third leg**, which the frozen prereg does **not** gate. As first shipped, that leg was computed and discarded and the record held no L4 engine number at all; **§2.2 below now lands its receipt**, so the sentence *"two independently-developed integrators report the same resonances"* is backed by a number instead of by an unpersisted intermediate.
- **`AGREE` was not the expected outcome.** The prereg §11 recorded that the odds of a `DIVERGE` on some rung were *"substantial and expected"*. **On the PRIMARY observables — frequency, count, multiplicity — it did not happen, and that is the report.** On the auxiliary TOL-LOSSLESS axis it *did* happen under the as-frozen band, and A1 is what moved it (see the bin box above). Stating only the first half of that sentence is what the clearing review corrected.

**Sector declaration (re-declared).** MODE numerical-infrastructure · REGIME I cold, sub-yield, **lossless-reactive** ($A=0$, $S(A)=1$, Op14 not engaged) · PHASE-STATE cold crystalline quiescent ($\varepsilon_{11}=0$) · CHANNEL **scalar/translational ONLY** (no Cosserat/T2 microrotation DOF exported, driven or read) · CARRIER **srs-z3**. Cross-wiring check performed: nothing here couples the scalar channel to charge, spin or mass.

---

## §1 — Reproduction gate (epic §5.2) — RUN FIRST, BEFORE ANY EXPORT

Every engine-side reference was re-derived on the current engine at HEAD `766d5179` **before a single netlist line was emitted**. Phase 0 ran at `ff0fde8b`.

**Result: PASS on every scalar-channel number this lane consumes. ZERO drift.**

| receipt | Phase-0 banked (`ff0fde8b`) | fresh (`766d5179`) |
|---|---|---|
| `TD` under R2 | `7.436783388682972e-22` | `7.436783388682972e-22` |
| `TD` under R1 | `1.2880886674083153e-21` | `1.2880886674083153e-21` |
| R1/R2 ratio | `1.732050807568877` | `1.732050807568877` |
| band top | `5.4414` $\omega_C$ | `5.441398092702652` $\omega_C$ |
| Γ optical multiplet | `3.3093` $\omega_C$ | `3.3093138398130493` $\omega_C$ |
| srs $L=3$ adjacency | $\mu\in[-3,3]$, $\lambda_{\max}=6$ | `-2.9999999999999987` / `3.0000000000000013` / `6.0000000000000036` |
| srs $L=3$ bipartite | 108/108 | 2-colouring succeeded, **verified not assumed** |
| $K_4$ complete, engine TLM operator | 0(×4), 1.910633(×6), π(×2) | identical |
| srs $L=2$ cycle-space block | 34 at $\theta=0$ and $\theta=\pi$ | 34; cycle space $B-N+1=$ `33` |
| srs $L=2$ interior | 10 distinct, total 62 | 10 distinct, total 62 |

The engine leg is the engine's **shipped** code path: the one-step operator is assembled by applying `chiral_lattice.scalar_tlm_step` to unit port basis vectors, with `scatter_matrix(3)` unmodified. Orthogonality residual $\le1.8\times10^{-15}$ on every net.

**Two blocks were added to this gate at the PR clearing review, both REPORTED and neither GATING** (both are landed after the prereg froze its bins, so neither may become a criterion mid-lane, and neither feeds `reproduction_gate.pass`):

- `reproduction_gate.engine_leg_L4` — the L4 **engine-vs-arccos** receipt whose interior spectrum was previously computed and discarded. See **§2.2**.
- `reproduction_gate.prereg_s36_drift` — the prereg §3.6 frozen-table drift registry, executing the prereg's own drift rule. See **§7 / S36-DRIFT**.

---

## §2 — The ladder, rung by rung

All frequencies reported on the single frozen axis $\omega/\omega_C$ (equivalently $\theta=\omega\,\mathrm{TD}$), so no verdict can turn on a units choice.

| rung | object | legs | interior modes solver/ref | max rel dev | TOL-MULT | TOL-LOSSLESS |
|---|---|---|---|---|---|---|
| **L0** | bare `L_CELL`∥`C_CELL` tank | 2-way (solver-vs-**arithmetic**) | 1 / 1 | `2.220446049250313e-16` | **NOT ASSERTED** | `0.0` |
| **L1** | one bond, open–open | 2-way (FL-3) | 0 / 0 | `0.0` | vacuous | `1.395e-12` |
| **L2v** | $z{=}3$ vertex + 3 open stubs, **driven at the vertex** | 2-way (FL-3) | 0 / 0 | `0.0` | vacuous | `4.057e-12` |
| **L2s** | same object, **driven at a stub end** | 2-way (FL-3) | 1 / 1 | `0.0` | **PASS** 2 vs 2 | `5.292e-12` |
| **L3** | srs 4-site primitive cell, periodic wrap ($K_4$ complete, 6 lines) | **3-way** | 1 / 1 | `1.3033307766363578e-10` | **PASS** 3 vs 3 | `1.326e-11` |
| **L4** | **srs supercell $L=2$**, $N=64$, $B=96$ | **3-way** | **10 / 10** | `4.852624968521013e-10` | **PASS** 62 vs 62 | `9.831e-10` |

**Frozen tolerances (unchanged from the prereg):** TOL-FREQ `1.0e-7`, TOL-REFINE `1.0e-9`, TOL-GRID `1.0e-2`, TOL-LOSSLESS `1.0e-9`, TOL-MULT and TOL-COUNT exact.

### §2.1 — L4, the marquee comparison (the rung carrying the independence weight)

**Column label, corrected at the PR clearing review.** The deviation column below was headed *"rel dev, solver vs engine"*. That was wrong: at L3/L4 the driver's `Rung.reference` is `arccos_reference(...)`, so every number in it is **ngspice vs the arccos closed form**, not ngspice vs the engine's stepper. The engine leg is §2.2. Nothing in the table moved; only its header did.

| # | $\omega/\omega_C$ reference (**arccos**, node space) | rel dev, **solver vs arccos reference** | mult. solver | mult. ref |
|---:|---|---|---:|---:|
| 1 | `1.100826696` | `4.853e-10` | 6 | 6 |
| 2 | `1.263925376` | `3.110e-10` | 6 | 6 |
| 3 | `1.654656920` | `1.303e-10` | 4 | 4 |
| 4 | `2.132084252` | `2.768e-10` | 9 | 9 |
| 5 | `2.480786308` | `3.441e-10` | 6 | 6 |
| 6 | `2.960611785` | `4.834e-11` | 6 | 6 |
| 7 | `3.309313839` | `1.303e-10` | 9 | 9 |
| 8 | `3.786741172` | `2.128e-10` | 4 | 4 |
| 9 | `4.177472716` | `1.504e-10` | 6 | 6 |
| 10 | `4.340571398` | `4.062e-11` | 6 | 6 |
| | | | **62** | **62** |

TOL-GRID computed `1.750e-03` (frozen $\le10^{-2}$); refinement converged to `8.347e-11` (frozen $\le10^{-9}$); minimum residue-rank separation `3.693e+04` (floor $10^2$). The boundary root sits at `5.441398092702655` $\omega_C$ with $|\theta/\pi-1| =$ `4.440892098500626e-16`.

### §2.2 — THE ENGINE LEG AT L4 — the third-leg receipt that was missing

**This receipt was computed and discarded in the first shipped run** (`tlm_operator_spectrum(net2)` ran; only `n_dc`, `n_top`, `n_ports` and the orthogonality residual were persisted). It is now recomputed and persisted at `reproduction_gate.engine_leg_L4`.

The engine leg is the engine's **shipped** stepper — `chiral_lattice.scalar_tlm_step` applied to unit port basis vectors with `scatter_matrix(3)` unmodified, i.e. scatter+connect with $\Gamma=-1/3$ on the **port** space. It never assembles a nodal admittance matrix, which is exactly why it is the cross-formulation leg (§0 scope box).

| quantity | measured | note |
|---|---|---|
| orthogonality residual of the one-step operator | `8.018277400070575e-17` | the operator is orthogonal to machine precision, so its eigenphases are the physical $\theta$ |
| port-space $\theta$ blocks | `34` / `12` / `12` / `8` / `18` / `12` / `12` / `18` / `8` / `12` / `12` / `34` | 10 interior blocks between the two edge blocks |
| interior port-space multiplicity total | `124` | $=2\times$ `62` |
| port-space vs node-space multiplicity | **exactly $2\times$ on all 10 blocks** | eigenphases come in $\pm\theta$ pairs and $|\arg(\cdot)|$ folds them into one block |
| **max rel dev, ENGINE-TLM vs arccos interior set** | **`7.771561172376096e-16`** | against the frozen TOL-FREQ `1.0e-7` — eight decades inside |

**Compared on raw block means, not on the two sides' rounded dict keys.** The engine side keys its blocks at 6 dp and the arccos side at 9 dp; a key-to-key comparison measures the coarser rounding (`6.466711652830526e-07`) rather than the agreement. The record now carries both.

**Two honesty notes on this receipt.**

1. **It is REPORTED, NOT GATING.** It landed after the prereg froze its bins. Adding a gate to a frozen prereg mid-lane is the move the discipline forbids, so it is banked and reported and feeds no bin — including not feeding `reproduction_gate.pass`. Its tolerance is the already-frozen TOL-FREQ; no knob was minted for it.
2. **The PR clearing review independently ran this same leg and reported `0.0`; this lane measures `7.771561172376096e-16`.** Both are agreement at machine precision (≈3.5 ULP), and the difference is summation order in assembling the adjacency, not physics. The number recorded here is the one this lane's own code produces, per verify-before-cite; the discrepancy with the review's `0.0` is surfaced rather than reconciled by adopting the rounder number.

### §2.3 — THE SURVIVING TOL-LOSSLESS RECEIPT, AND WHY PHASE 2 MUST NOT INHERIT THE METRIC

The L4 receipt that A1 rescued is `9.830911760111372e-10` against TOL-LOSSLESS `1.0e-9` — it passes at **`98.30911760111371`% of the gate**. That is 1.7% of headroom on the marquee rung, and it is recorded here rather than left as an unremarked PASS.

**The metric is weak, and the weakness is structural, not a tuning matter.** $\max_f|\mathrm{Re}\,Z/\mathrm{Im}\,Z|$ over a fixed grid blows up wherever a sample lands near a **singularity of the driving-point impedance** — and A1's own corrected mechanism already says a lossless network has *two* kinds: **poles** ($|Z|\to\infty$) and **zeros** ($\mathrm{Im}\,Z\to0$ with $|Z|\to0$). At either, the computed real part is conditioning and roundoff, not resistance. A1 removed one *guaranteed exact* hit (the band edge); it did not close the class, and a different grid offset can push an identical, exactly-lossless netlist past `1.0e-9` on grid luck alone.

**Localization — external measurement, flagged as such.** This lane's record does **not** localize the `9.830911760111372e-10` (the per-node dict carries only `n_brackets` and `bracket_f`), which is itself part of the finding: the receipt as specified is not diagnosable from the artifact it writes. The PR clearing review, running its own ngspice sweep on the committed `L4_coarse_n0.cir`, measured the per-node residual maxima sitting near impedance **zeros**, at $|Z|\sim$ `1.346e-02` $\Omega$ with the largest per-node value `5.5638e-10` — *not* near poles. **Those numbers are the review's, not this lane's**, and are deliberately absent from the shipped record; they are quoted because they name the mechanism.

**Consequence, stated plainly: Phase 2 must RE-SPECIFY this receipt, not inherit it.** Candidate replacements (not adjudicated here): $|\mathrm{Re}\,Z|/|Z|$, or excluding samples within a stated distance of a computed root. **Do not read TOL-LOSSLESS as a robust losslessness gate.** What *does* hold robustly is the structural check `test_srs_rungs_emit_only_t_elements`: the srs rungs emit only `T` cards and the AC drive, zero `R` cards — a resistive leak is caught by construction, not by a grid lottery. **Whether $\max|\mathrm{Re}\,Z/\mathrm{Im}\,Z|$ is the receipt we want at all is routed to Grant in §7.**

---

## §3 — Every pre-registered fence, accounted for

The prereg §4/§5 named five ways a **correct** export could look like a divergence. Each is settled here with a measured number, not a narrative.

| fence | what it predicted | what was measured |
|---|---|---|
| **F1** — first-branch only | Solver carries the $n\pi/\mathrm{TD}$ ladder the discrete-time engine cannot; comparison restricted to $\omega\le\pi\,\omega_{link}$ | Enforced by the interior filter $0<\theta<\pi$. **No mode above the band top was compared.** F1 remains stated as **INSTRUMENT SCOPE ONLY** — Q1 is unanswered and nothing here bears on it. |
| **F2** — no Bloch phase | No $\mathbf k$-resolved dispersion; only the unlabelled supercell eigenfrequency SET | Confirmed: substitute (A) used, **no $\mathbf k$-label compared anywhere**. |
| **F5** — cycle-space block | $B-N+1$ extra modes at $\theta=0$ and $\theta=\pi$ in the TLM **port-space** operator | Confirmed on the engine leg: srs $L=2$ port space `192` = $2\times62$ interior + $2\times34$ edge; cycle space `33`. |
| **F5-AC** — this lane's addition | Those cycle-space modes are **DARK** to a node-driven measurement, so the `.AC` pole set is exactly the arccos set | **Confirmed: ngspice found exactly 10 distinct interior poles, total multiplicity 62 — not one cycle-space mode appeared.** Had F5 been applied unmodified to the `.AC` measurement, a correct export would have been scored as ~66 missing modes. |
| **F6** — dark modes at a driven port | The $\theta=\pi/2$ differential pair has zero voltage at the vertex, so a vertex drive cannot see it | **Confirmed exactly.** L2v (vertex drive): `0` interior poles. L2s (stub drive): `1` interior pole at `2.720699046` $\omega_C$, multiplicity `2`. **The mode is unobservable at the vertex and present at the stub — an unobservable mode is not a missing mode, and the prereg named which was which before the run.** |
| **MESH** | At $L=2$ the highest interior mode sits at `4.340571398` $\omega_C$, well below the true top `5.441398` — a mesh artefact, not a missing band | Confirmed to the digit. |

**F5-AC's derivation, restated because it is the one analytic step this lane contributed.** For a $z$-regular network of identical lossless lines joined at shunt nodes, $Y(\theta) = (D\cos\theta - A)/(jZ_0\sin\theta)$, so $\det Y = 0 \iff \cos\theta = \mu_n/z$ — the canonical arccos map, in **node** space. The residue at each root is $-jZ_0 P_k/(z(\theta-\theta_k))$ with $P_k$ the **orthogonal spectral projector**, which is what makes the multiplicity readout exact rather than heuristic. Cycle-space modes carry zero node voltage and are therefore structurally invisible to a node-driven measurement. **F5 itself is untouched** (KEEP-BOTH); F5-AC is added alongside it as the accounting rule for the T4 instrument.

---

## §4 — Controls (**UNRUN ≠ PASSED** — each ran, each is reported)

### POSITIVE CONTROL — the instrument can detect a planted defect
Frozen: `Re-emit the L3 netlist with **one** bond's `TD` multiplied by a frozen factor **1.05** and confirm the comparison **resolves the planted defect** and bins it `DIVERGE-ATTRIBUTED`.`

One bond of the L3 $K_4$ network had its `TD` multiplied by `1.05`. **DEFECT RESOLVED.** The triply-degenerate optical multiplet at `3.309313839` $\omega_C$ **split into four distinct poles** — `3.267607`, `3.268952`, `3.309314`, `5.35233` $\omega_C$ — against a reference of one pole at multiplicity 3. Interior count `4` vs reference `1`; TOL-MULT FAIL. Exactly the symmetry-lowering signature a broken bond should produce, and exactly the failure the comparison is supposed to catch. **Without this the `AGREE` above would not be bookable.** Artifact: `research/netlists/2026-08-25-scx-phase1/L3_planted_coarse_n0.cir` (its own header says `*** PLANTED DEFECT` and `THIS NETLIST IS DELIBERATELY WRONG`).

### CONVENTION CONTROL — the FL-1 $\sqrt3$ hazard, MEASURED not paraphrased
Frozen: `Emit and run **both** label conventions once at L1 and confirm the measured resonance ratio is **exactly $\sqrt3$** to within TOL-FREQ.`

R2 and R1 netlists both emitted and both run. **Measured ratio `1.7320508075688776` against $\sqrt3=$ `1.7320508075688772` — relative deviation `2.220e-16`.** The R1 netlist is built through `bond_lc()`, i.e. through *the symbol an exporter author would wrongly reach for*, so the control exercises the actual hazard.

### FL-1 MACHINE GATE — mandated by the brief and R56 §2
`src/tests/test_scx_spice_export.py::TestFL1DelayConvention`, **25 tests green**. It asserts the emitted `TD` is bit-identical to `ANALYTIC_NETWORK_FACTOR / OMEGA_C` and is neither of the other two live conventions (`bond_lc()` ⇒ $\sqrt3\times$; `r10_v8_ee_phase_a.py:255` `bond_length_SI = np.sqrt(3.0) * L_NODE` ⇒ $3\times$), **and it fires in both directions**: two mutation tests emit R1 and III and assert the R2 assertion rejects them, so the gate is provably able to fire rather than vacuously green. **The wrong-symbol reach is now caught by a test, not by vigilance.**

**A real defect this gate caught during authoring:** `ANALYTIC_NETWORK_FACTOR` is an `np.float64`, so the delay API was leaking numpy scalars whose `repr()` is `np.float64(...)` — an unparseable netlist token. Delays now coerce to plain `float`, asserted by test.

### T6 SI/NATIVE PAIRED CONTROL
Same networks emitted in SI and in native units ($Z_0=1$, $\mathrm{TD}=1$); dimensionless $\theta$ sets compared. **L1: max rel dev `0.0`. L3: max rel dev `0.0`.** T6(c)'s paired run, pre-positioned as the §6(b) solver-numerics check, is green.

### NEGATIVE CONTROL
The single bond (L1) carries no srs content. **`0` interior poles and `1` boundary root** — the bare wiring-theorem half-wave and nothing else. The pipeline is not manufacturing structure.

### ANTI-TAUTOLOGY CONTROL
AST-parsed: the exporter imports **no** band-structure symbol (`src/tests/test_scx_spice_export.py::test_exporter_imports_no_band_structure_symbol`), and no emitted netlist contains any reference frequency. **A comparison whose netlist knows the answer is a checklist, not a gate.**

### CTRL-RT round-trip
Every emitted number re-reads to the identical double (`repr`, never `%g`), asserted on `Z_0`, `OMEGA_C`, `ANALYTIC_NETWORK_FACTOR`, `L_CELL`, `C_CELL` and the emitted `TD`.

---

## §5 — AUX-B: cross-solver check of the `ave_chart` instrument (SUPPLEMENTARY, NON-GATING)

The means-test register at [`research/2026-08-24_ave-chart-instrument_note.md`](2026-08-24_ave-chart-instrument_note.md) §7 lists a **Class B — cross-solver** row, status *"PLANNED — rides the Phase-1 satellite."* It fit this lane's frozen scope, so it was run, pre-registered as an explicit **addition** to the L0–L4 ladder under KEEP-BOTH (no rung redefined).

The two-junction composite's $\Gamma(\theta)$ locus was computed two independent ways — `ave.viz.ave_chart.two_junction_gamma`'s ABCD transfer matrix, and ngspice's MNA on the exported netlist — over 361 points, $\theta\in[0,2\pi]$:

Frozen: `TOL-GAMMA` = `1.0e-12` on every row below.

| quantity | measured | frozen tolerance (TOL-GAMMA) |
|---|---|---|
| $\max_\theta\bigl|\Gamma_{ngspice}-\Gamma_{chart}\bigr|$ | `3.356589068483857e-16` | `1.0e-12` **PASS** |
| $\bigl|\Gamma(0)-(-3/5)\bigr|$ | `1.110e-16` | `1.0e-12` **PASS** |
| $\bigl|\Gamma(\pi/2)-(-3/7)\bigr|$ | `7.498e-18` | `1.0e-12` **PASS** |

**Scope, stated plainly.** AUX-B validates a **plotting instrument**, not the engine. It is the register's **class B (machinery)**, explicitly not its class C (the row that could produce a physics verdict). It **cannot and did not move the §0 bin**. The two $Z_0/2$ resistors in its netlist are **PORTS** — the SPICE rendering of reflectionless semi-infinite lossless bond pairs — not dissipative substrate elements, which is why TOL-LOSSLESS does not apply to that rung; the `two_junction_gamma` docstring's isolated/incoherent scoping is inherited unchanged. **The register's class-B row can now be marked RUN by the auditor lane; this lane does not edit that note.**

---

## §6 — 🔴 RULE-12 AMENDMENT A1, and why it is not a rescue

**One frozen instrument parameter was amended, in a dated Rule-12 amendment appended to the frozen prereg (its body untouched), BEFORE any comparison number was produced on any rung.** Full statement and receipts: `research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md` § AMENDMENT A1.

**The defect.** EC-2 froze the coarse band's upper edge at exactly $1.0\times f_{top}$, which is exactly the $\theta=\pi$ singularity of the node-admittance matrix $Y=(D\cos\theta-A)/(jZ_0\sin\theta)$. Two symptoms, one cause:

1. **The boundary root could not be BRACKETED inside the band** — a sign change needs samples on both sides — so detecting it depended on the floating-point sign of $\cot(\theta)$ at the final grid point. **It happened to work on L1, by accident.** An accident is not a receipt.
2. **TOL-LOSSLESS was then evaluated AT a singular MNA solve.** Measured on L4 under the as-frozen band: `1.240e-04` on L3 and `5.037e-04` on L4, at $f/f_{top}=$ `1.00000000` exactly, against $<10^{-9}$ at every other one of 20001 samples. **No lossless network can meet the frozen gate when a sample lands on the singularity to machine precision** — as frozen it was *"a tolerance the instrument cannot meet"*, the failure mode the prereg's own §3.3 instrument-resolution clause names.

> **🔴 NARROWED — the version of this sentence inside the frozen prereg's AMENDMENT A1 is an overstatement.** A1 says *"no lossless network **whatever** can meet the frozen gate when a sample lands on **a pole**"*. That is false as worded: the PR clearing review measured a sample **4.6e-6 relative from an interior pole** (drive node `n27`, $|Z|=7.7\times10^5\,\Omega$) returning `1.2157e-11` — *passing*. The claim holds only when the sample sits on the singularity **to machine precision**, which is what the frozen band's upper edge did ($\theta=\pi$ exactly, $\sin\theta$ underflowing to $1.22\times10^{-16}$) and is the only case A1's evidence supports. A1's own corrected-mechanism paragraph, two paragraphs later, already says *singularity* (pole **or** zero) and not *pole*; the overstated sentence contradicts it. **The frozen prereg is not edited** — a dated **NOTE N2** appended to it records the narrowing, per Rule-12 append-only. The narrowing does **not** disturb A1's rationale: the band edge was on the singularity to machine precision, which is the surviving form of the claim. `1.2157e-11` is the review's measurement, not this lane's, and is deliberately absent from the shipped record.

**The amendment.** Upper edge $\to 1.05\times f_{top}$. **The COMPARISON band is UNCHANGED** (interior $0<\theta<\pi$, exactly as §3.4 step 7 and F1 already froze); the extra samples are instrument and are never compared. **No tolerance value moved.**

**Why it is not a rescue, with receipts.** Both bands were RUN and both are REPORTED (`controls.amendment_a1_paired`):

| rung | $\max|\mathrm{Re}\,Z/\mathrm{Im}\,Z|$, as-frozen band | amended band | **interior verdict changed?** |
|---|---|---|---|
| L1 | `1.921e-10` PASS | `1.395e-12` PASS | **no** |
| L3 | `1.240e-04` FAIL | `1.326e-11` PASS | **no** |
| L4 | `5.037e-04` FAIL | `9.831e-10` PASS | **no** |

**The interior verdict is byte-for-byte identical under both bands on all three rungs.** The amendment moved an ill-conditioned auxiliary receipt and moved no comparison result. Falsifier FS-7 names its mechanism — *"a resistive element leaked into an srs export"* — and that mechanism is **machine-checkably absent**: `src/tests/test_scx_spice_export.py::test_srs_rungs_emit_only_t_elements` asserts the srs rungs emit only `T` cards and the AC drive, zero `R` cards.

**⚑ The amendment corrects itself, and that correction is on the record.** A single-drive-node probe taken while drafting A1 reported L3 at `4.448e-12` (PASS) and was used to argue that L3 — being non-bipartite, hence having no $\theta=\pi$ pole — was the clean control isolating the mechanism to bipartite rungs. **The full 4-drive-node run refutes that.** The corrected mechanism is more general: at $\theta=\pi$, $Y$ is singular for **every** rung — a **pole** where an eigenvalue $\mu=-z$ exists, a **zero** where it does not — so bipartiteness selects *which* singularity, not *whether there is one*. The drafting claim is preserved and marked in the prereg rather than quietly replaced.

---

## §7 — Flags surfaced (NOT fixed by this lane)

| # | flag | route |
|---|---|---|
| **F5-AC** | This lane added a node-space accounting rule alongside F5 (derivation in §3 above; F5 itself untouched, KEEP-BOTH). It is a statement about the T4 instrument, not about the substrate — but it is a lane-authored extension of a pre-registered fence set and should be reviewed as one. **It is load-bearing for the L4 verdict**: without it, a correct export scores as ~66 missing modes. | **auditor lane — review at PR** |
| **A1** | The Rule-12 amendment above, including its self-correction. | **auditor lane — review at PR** |
| **FL-1** | **Unchanged and still OPEN at corpus level**, per R56 §2. Three live in-tree bond-delay conventions, re-verified on this branch. The exporter's R2 pin is an **engineering convention on an emitted label**; the corpus's physics-level R1-vs-R2 flag at `srs-band-structure.md:157` — verified verbatim this branch: *"Only the scale LABEL changes under R1, not the k-space band SHAPE or the gap inventory. Flagged for adjudication."* — **stays open. Nothing in this result closes it.** The `bond_lc` rename stays an open lane proposal per R56 §4; this lane renamed nothing. | auditor lane |
| **FL-2** | Two stale line-cites inside `srs-band-structure.md`, **re-verified still stale on this branch**: `:145` cites `constants.py:294` for `OMEGA_C` (real site `:305`); `:117` cites `:770` for `V_LONG` (real site `:781`). Pure line-drift; content correct at both real sites. | auditor lane (cite-repair sweep) |
| **FL-3** | Resolved for Phase 1 as **TWO-WAY at L0/L1/L2**. `scatter_matrix` raises for $n<2$ and **no engine touch was authorized**, so the epic's three-way anchor is **not** satisfied at those rungs — stated, not hidden. **⚠ NARROWED at the PR clearing review.** The earlier wording — *"the three-way anchor DOES hold at L3/L4"* — was stronger than the record supported, on two counts. **(i)** The rung where the anchor goes unmet is **L0, the single cell the epic named by name**: epic:116 reads *"the **single cell's** resonance is analytically exact, so BOTH the engine and the solver are first checked against the closed-form value independently"*. Losing the anchor there is losing it at the rung it was written for, not at an incidental one. **(ii)** At L4 the engine leg was **computed and discarded**, so until §2.2 landed there was **no recorded engine number at L4** and the anchor was un-instantiated at the artifact level. What is true now: the engine leg runs unmodified at L3/L4 **and** L4 carries a persisted receipt (§2.2, `reproduction_gate.engine_leg_L4`, max rel dev `7.771561172376096e-16`), so the anchor is instantiated at L4 — REPORTED, not gating. **L0/L1/L2 remain two-way and the epic's named single-cell rung remains unmet.** | closed for this phase, **with the anchor unmet at L0** |
| **CLS-1** | **★ LATENT CODE DEFECT — was Phase-2 BLOCKING, NOW CLOSED.** `arccos_reference` classified interior-vs-boundary with an independent margin of 1e-9 stated in $\theta$. Near $\mu=\pm z$ the arccos map is **square-root singular** ($\mu=-z+\delta\Rightarrow\theta=\pi-\sqrt{2\delta/z}$), so a 1e-9 margin in $\theta$ demands $\lvert\mu+z\rvert\lesssim1.5\times10^{-18}$ — about three decades **below** double resolution at $\lvert\mu\rvert=3$. It could only ever be satisfied by `np.clip` firing. **Measured on this driver's OWN shipped value** `reproduction_gate.fresh.srs_L3_mu_min` $=$ `-2.9999999999999987`: the old margin classified the $\theta=\pi$ root as INTERIOR and minted a spurious mode — srs $L=3$ scored `215` interior modes and `20` distinct $\theta$ against the correct `214` / `19`, with the $\theta=\pi$ block counted `0` times instead of once. **This is the same floating-point-accident failure mode A1 was written to fix, sitting in the lane's own reference-side classifier.** **No Phase-1 number moves**: L3 is the $K_4$ cell ($\mu_{\min}=-1$) and L4 is srs $L=2$ (whose $\mu_{\min}$ clips), both verified unchanged — but Phase 2 runs at $L=3$ and above, and the recommendation below is GO on this code. **FIXED:** the margin is now `BOUNDARY_THETA_MARGIN` $=$ TOL-FREQ$\,\cdot\pi$, i.e. **the solver side's own interior filter**, so both sides of the comparison partition on one definition and no knob is minted. **Regression, fires in both directions:** `src/tests/test_scx_arccos_boundary_margin.py` drives the classifier with the old margin on that exact $\mu$ and **requires the wrong answer**, then requires the right one under the repair, and pins K$_4$/srs $L=2$ unchanged. | **closed by this repair** |
| **S36-DRIFT** | **Banked per the prereg's OWN rule.** The prereg's §3.6 L4 table closes with *"any drift between this table and the fresh values is itself a finding banked under a dated note"* — and none was banked, because those ten rows sat in no registry at all (`PHASE0_BANKED` never carried them, so the reproduction gate was blind to them, and the number-check only scans the **result** doc). Now registered as `PREREG_S36_L4_FROZEN` and reported at `reproduction_gate.prereg_s36_drift`. **The $\theta$ column reproduces to its printed precision on all ten rows** (max `6.466711652830526e-07`, inside 6-dp rounding everywhere). **The $\omega/\omega_C$ column does not**: max drift `2.2863871623979293e-05` $=$ `228.63871623979293`$\times$ TOL-FREQ, on 8 of 10 rows beyond their own print-rounding floor, and the single conversion factor those rows imply **varies row to row** (spread `4.8938282220856166e-05`), so that column was not produced from the frozen $\theta$ column by the frozen map $\omega/\omega_C=\theta/$`ANALYTIC_NETWORK_FACTOR`. **No verdict moves** — prereg §3.4 step 7 makes the comparison consume the **fresh** reference and it does; §2.1 above already carries the fresh values. **Dated NOTE N1 appended to the frozen prereg** (append-only; body untouched). REPORTED, not gating: the prereg makes drift a finding to bank, not a gate. | **banked** |
| **★ Q2** | **OPEN QUESTION FOR GRANT — routed, NOT answered here.** *Is $\max\lvert\mathrm{Re}\,Z/\mathrm{Im}\,Z\rvert$ over a swept grid the receipt you actually want for "the emitted network is lossless"?* The plumber-physical shape of the problem (§2.3): the ratio blows up wherever the grid lands near **either** singularity of the driving-point impedance — a **pole** ($\mathrm{Im}\,Z\to\infty$) or a **zero** ($\mathrm{Im}\,Z\to0$) — and at both the computed real part is roundoff on an ill-conditioned solve, not resistance. A perfectly lossless netlist can therefore fail the gate on grid luck, and the surviving L4 receipt passes at `98.30911760111371`% of it. **This result takes no position.** It decides what receipt Phase 2 specifies for losslessness; it does not bear on any Phase-1 frequency, count or multiplicity. | **Grant** (plumber-physical) |
| **Q1** | **Still unanswered; re-routed to Grant unchanged.** *Does a vacuum bond ring at its full-wave, or is the half-wave the top by construction?* **This result takes no position** and F1 is stated as instrument scope only. It decides what a Phase-2 result doc may say about modes above the band top. | **Grant** (plumber-physical) |
| **FL-5** | **Lane-surfaced.** The Phase-0 planning pair analyses the ngspice adoption without citing the in-tree ngspice infrastructure that already exists: the hook `src/ave/bench/spice_runner.py`, the `_orchestration/2026-07-03_spice-lane-charter.md` SPICE lane, and the five `src/scripts/vol_4_engineering/spice_ladder_rung*.py` drivers. **No Phase-0 conclusion is thereby wrong** — T1's ngspice selection is if anything strengthened — but the option analysis was written without its own prior art in view. **This lane reused `spice_runner.py` rather than rebuilding it (Rule 14) and edited no Phase-0 doc.** | auditor lane / orchestrator |
| **F5-prose** | Minor, no action proposed. F5's *prose* generalises the cycle-space block as *"$B-N+1$ … at $\theta=0$ **and** at $\theta=\pi$"*. That is exact on the bipartite srs $L=2$ supercell (34/34) and **not** on the non-bipartite $K_4$ complete graph, where the measured port-space blocks are **4 and 2**. F5's own data table already lists 4 and 2 correctly, so only the prose over-generalises. Recorded so a reader applying the prose rule is not surprised. | auditor lane (informational) |

---

## §8 — Phase-2 GO recommendation

**Recommend GO on Phase 2**, on the epic §4 gate *"agreement at the pilot scale, or an attributed-and-repaired divergence"* — agreement at pilot scale is met.

**What Phase 1 does and does not hand forward:**

- **Hands forward:** a hand-auditable exporter with zero free parameters and a machine-checked delay convention; an extraction method whose resolution is measured, not assumed; a validated instrument (the positive control fires); and the F5-AC accounting rule without which the Phase-2 dispersion comparison would mis-score a correct export.
- **Does NOT hand forward any physics.** Phase 2's structural band-top check remains an **exporter-integrity gate** (F4), not independence. **Phase 2's independence weight must rest on the quantitative interior comparison**, exactly as the epic §4 says.
- **Epic §8 PARK trigger.** The trigger *"no solver represents the bond object without distortion"* is now **retired on the AC path** — retired by a **tracked driver under the reproduction gate**, which is the Phase-1 act Phase 0 was explicitly not permitted to perform (the Phase-0 probe was untracked scratch and its docs pinned that limit). The **transient path remains un-de-risked and undiagnosed** and this lane did not touch it.
- **Blocking for Phase 2 — one item, raised and closed inside this PR.** **CLS-1** (§7) was a genuine Phase-2 blocker: the reference-side boundary classifier produced a *wrong reference mode count* at srs $L=3$ on the driver's own recorded $\mu_{\min}$, and Phase 2 runs at $L=3$ and above. It is **fixed, regressed in both directions, and verified to move no Phase-1 number**. Phase 2 is not gated on it any longer. **Q1 gates only what a Phase-2 doc may SAY about modes above the band top**, not whether Phase 2 may run.
- **Carried forward as a REQUIREMENT on Phase 2, not a blocker:** Phase 2 must **re-specify the losslessness receipt** rather than inherit $\max\lvert\mathrm{Re}\,Z/\mathrm{Im}\,Z\rvert$ over a fixed grid (§2.3 — the metric is a lottery on grid proximity to poles *and* zeros, and the surviving L4 receipt passes at `98.30911760111371`% of gate). **Q2** routes the shape of the replacement to Grant. Structural losslessness — zero `R` cards in an srs export — is independently machine-checked and is unaffected.
- **Also handed forward:** the L4 **engine-leg receipt** (§2.2) is now persisted, so Phase 2 inherits a three-way anchor that is instantiated at L4 in the artifact rather than only in the code path.
- **Phase 3 stays gated** on Phase 2 banked + a named consumer, per the epic. Nothing here changes that.

**Explicitly NOT recommended:** procuring Xyce. Epic §5.3 reaches for a second solver only when suspect (b) is live, and no divergence was observed. Pre-paying for a step that may never be needed is not warranted by this result.

---

## §9 — Skill-selection retro-pass

| skill | fired | where |
|---|---|---|
| `ave-prereg` | ✅ | freeze-by-push at `737ba888`, prereg committed ALONE before any code |
| `substrate-native-check` | ✅ | re-walked at implementation time (prereg §1.5, CP1–CP10) before the exporter's first line; CP3 is machine-enforced by `test_srs_rungs_emit_only_t_elements` |
| `ave-canonical-source` | ✅ | every element value an import; `assert_canonical_source()` runs before any emission |
| `ave-driver-script-honesty` | ✅ | FL-3 two-way disclosure; L3's driver-assembled `LatticeNet` disclosed; L0 labelled solver-vs-arithmetic in its own netlist header; UNRUN≠PASSED reporting fixes |
| `ave-reproduction-gate` | ✅ | §1, run before any export; zero drift |
| `verify-before-cite` | ✅ | every KB/code cite re-verified on this branch; FL-2 re-verified still stale |
| `phase-space-coordinate-check` | ✅ | frequency-space claim, frequency-space measurement; no $\mathbf k$-label compared (F2) |
| `consistency-vs-emergence` | ✅ | IMPLEMENTATION-VERIFICATION declared in the prereg and re-declared in §0 |
| `ave-independence-check` | ✅ | §0 scope box + F4 scoping + AUX-B's class-B fence |
| `ave-mechanism-claims-discipline` | ✅ | A1's mechanism claim was corrected when the full run refuted the drafting probe (§6) |
| stop-and-ask | ✅ (2 stuck-points, both resolved inside the cap) | the EC-2 band-edge defect and the TOL-LOSSLESS conditioning failure — diagnosed to a single root cause in two attempts and handled by dated amendment rather than by silent edit |

**Drift from the plan:** `ave-mechanism-claims-discipline` fired unplanned (the A1 self-correction). No planned skill went unfired.

### §9.1 — Retro-pass addendum: the PR clearing-review repair round (2026-08-25, post-run)

Seven defects were returned against this PR. **None overturned the AGREE** — the reviewer independently re-derived the L4 spectrum with its own parser, ngspice driver, bracketing and residue-rank SVD and matched to $\sim3\times10^{-15}$, and ran the missing engine leg. Every defect was in reporting, receipt structure, or one latent code path. Where they landed:

| # | defect | landed as |
|---|---|---|
| 1 | the headline was **bin-moving** and did not say so | §0 "THE BIN THAT MOVED" box, **plus** a machine gate in the number-check that fires if a frozen-band FAIL is ever headlined as `AGREE` without the qualifier, the other bin's name, and each failing rung's measured value |
| 2 | §2.1's marquee column mislabelled *solver vs engine*; `tlm2`'s interior spectrum computed and discarded | column relabelled **solver vs arccos reference**; new **§2.2** with the engine leg persisted at `reproduction_gate.engine_leg_L4` under the frozen TOL-FREQ |
| 3 | independence under-scoped — the arccos leg is ngspice's own closed form | new §0 scope-box bullet |
| 4 | **CLS-1**, the $\theta$-space boundary margin (Phase-2 blocking) | fixed to `BOUNDARY_THETA_MARGIN`; regression `src/tests/test_scx_arccos_boundary_margin.py` fires in both directions; §7 row; closed |
| 5 | TOL-LOSSLESS headroom + metric weakness | new **§2.3**; Phase-2 carried-forward requirement in §8 |
| 6 | frozen §3.6 drift unbanked, against the prereg's own rule | prereg **NOTE N1** (append-only) + `PREREG_S36_L4_FROZEN` registry + §7 row |
| 7 | two overstatements (A1's universal sentence; FL-3's *"anchor DOES hold"*) | narrowed in §6 and §7; prereg **NOTE N2** records the A1 narrowing without editing A1 |

**Skills fired in the repair round:** `verify-before-cite` (every number re-measured on this branch rather than copied from the review — which is how the review's `0.0` engine-leg deviation and this lane's `7.771561172376096e-16` came to be reported side by side), `ave-driver-script-honesty` (REPORTED-vs-GATING labelled on both new blocks), `self-referential-gate` (the new bin-disclosure gate and the CLS-1 registry were both probed in **both** directions, and two value arms were found passing vacuously and repaired before landing), `ave-reproduction-gate` (the repaired driver's reproduction gate re-run and diffed leaf-by-leaf against the record as shipped at `e79e9a8e`: **0 values moved, 0 dropped, 261 fields added** — a process figure about the repair diff, deliberately *not* registered as a record value, since it is a property of two commits rather than of the run), Rule-12 append-only (the frozen prereg's body and AMENDMENT A1 verified byte-identical to `737ba888` and to the pre-repair HEAD respectively).

**Discipline boundary observed:** no physics was re-run and no shipped number was moved. The engine-leg and drift receipts are pure engine-side recomputation; every ngspice-derived number in this doc is the one the original run measured.
