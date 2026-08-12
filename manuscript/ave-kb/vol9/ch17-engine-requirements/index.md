[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: leaf-as-index
no-claim: "Vol-9 synthesis routing stub for the engine-requirements chapter; consolidates documented engine-failure lessons into a simulator spec. No new substrate-physics claim — every requirement cites its canonical derivation home and its violating-engine lesson."
-->

# Ch.17 Engine Requirements for Faithful Simulation

Chapter 17 of the Vol 9 datasheet reads the datasheet as a specification for the *simulator*, not only for the substrate. It states what a numerical engine must implement, per datasheet line, to simulate the vacuum cell (the Ch.3 DOF/mode table) faithfully. Each requirement is mapped to (a) the datasheet line it enforces and (b) the documented engine failure that taught it.

The chapter content is **Class B/C synthesis** per `consistency-vs-emergence` v1.3 — no new substrate-physics primitives. Each row consolidates an already-documented engine-failure lesson (A-027 two-engine architecture; the V_ref double-count; the genesis-24 EMF detonation; the graft-v2 source-symmetry lesson) into datasheet-format engine-requirement rows.

## Synthesis content

- **Per-sector wave-speed modulation in the propagation step.** $c_{eff}(V)$ per sector in propagation, not only $Z(V)$ at scatter (A-027; canonical `two-engine-architecture-a027.md`).
- **An independent state carrier per DOF-table row.** Read-only projections (`V_ref`) are observables, never state (the double-count; `master_fdtd_phasor_bridge.py:16-17`).
- **Saturation/confinement/reflection as BOUNDARY conditions** ($\Gamma$, Op17-bounded), never bulk forces (the crystal-engine/graft-v2 CP10 boundary-localized-vs-bulk contrast: a $c_{eff}$ trap $\to \Gamma$-wall via $g_{front}$ confines with **no** detonation, $\Gamma_{core}\to-0.24$; the genesis-24 detonation is the EMF-pump lesson of the next row, **not** bulk-force confinement; `substrate-native-check` CP10).
- **Cross-sector couplings as CONSERVED Hamiltonian pairs** (source + back-reaction from one $H_{couple}$; energize-lock, no non-conservative pump — the EMF `k4_cosserat_coupling.py:550` lesson). The conserved $H_{couple}$ is **NEVER a shared $(V_{inc}, V_{ref})$ phasor** ($V_{ref}$ is a read-only projection of the same scalar $V$, not an independent DOF — the $A1 \perp T2$ fence, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20; wiring the two-"3"s into one phasor is the genesis-24 / $w_{pol}=0$ double-count). The one live inter-grade candidate — the **graft-v3 shear$\leftrightarrow$bulk $\chi$-source** — is **DEMOTED B$\to$C / LOCK UNIMPLEMENTED** ([`ch3 index`](../ch3-pin-port-configuration/index.md):18 graft-v3 verdict; sign-selection demonstrated but topology-selection REFUTED, $\chi$ a source INPUT not carried from a photon, lock unimplemented): live-but-not-adjudicated, **NOT available**. Do NOT wire it as an adjudicated coupling. This is the coupling leg of the Fork-A isolation-vs-coupling discriminator ([`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md) §6.5). 🔴 **UPDATE (2026-06-20, Rule 12 — graft-v3 line preserved; "NOT available" revised):** the conserved-AND-transferring energize-LOCK graft-v3 could not deliver **is now realized by a skew-Hermitian circulator GENERATOR (PARTIAL)** — see the 🔴 2026-06-20 UPDATE at [`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):201 + PR #321. It conserves (no pump) AND transfers (100 %, on the winding), escaping the trilinear pump/inert dead-end; the residual is the 2-port skew is RECIPROCAL and genuine chiral non-reciprocity needs the 3-port loop with an IMPOSED magnitude (echo). The lock is **NOT** unimplemented — it is a PARTIAL with the non-reciprocity magnitude still open.
- **Source symmetry class must admit the target topology** (centrosymmetric source cannot select a chiral knot — graft-v2).
- **Conservation canaries on float64** (H-drift, $|\mathbf{L}|$ gates are the pump-vs-lock detectors); fixed $N$ across compared runs; alias-checked extractors with reliability gates **and representation-capability-validated at the sampling scale** (plant-$(2,3)$-at-de-novo-scale $\to$ read-$(2,3)$; minor radius $r \gtrsim 3$ cells — a TRUE $(2,3)$ reads back as $(2,2)$/garbage at $r\approx1.1$ cells, so de-novo $w_{pol}=0$ nulls are partly representation-limited per the extractor-poloidal-misread note); observers strictly read-only.
- **Regime-reachability**: the engine must reach the regime the test requires (bulk near-yield for rectification); sub-yield nulls are artifacts.
- **(Candidate — characterization-in-flight) Wall sharpness / leak must be shown NOT regularization-limited.** Sweep $S_{min}$ / $A_{cap}$ before attributing any wall-sharpness / leak number (e.g. $\Gamma_{min}\approx-0.85$ carried across graft-v2/v3) to a physical constant ($\alpha$ above all); a number that tracks a regularization knob is apparatus, not physics. In-flight characterization on `analysis/2026-06-10-apparatus-floors` ($S_{min}$/$A_{cap}$ wall attribution + $H_{bel}$ ledger floor + wall-sign audit); discipline `ave-apparatus-floor-attribution`. NOT yet an adjudicated requirement — promote on that branch's verdict.

## Acceptance-suite requirements (rows 11–15; 2026-06-16/17 ground-up arc)

Five requirement rows added from the ground-up engine-acceptance arc (the suite at `src/tests/engine_acceptance/`, wired into the claim-DAG by [`engine-acceptance-suite.md`](engine-acceptance-suite.md)). Each ← a documented engine-failure lesson from THIS arc, citing its canonical home:

- **(11) Chiral / optical-activity rotation must be unitary (copy-first, no NumPy view-aliasing); the losslessness gate must run rotation-ON.** In-place $2\times2$ rotation on NumPy views (`src/ave/core/chiral_lattice_vector.py:49-58`, pre-fix) makes the rotation non-orthogonal → ~O(1) energy drift (Axiom-3 leak); the $\kappa=0$ free-photon gates never hit it, but an energy gate WITH rotation ON (A1b / T1.5) does. Discipline `substrate-native-check`.
- **(12) The medium must carry the DOF the excitation needs.** The transverse-only carrier (2 DOF) cannot host mass (L3 longitudinal) or charge (L4 micro-rotation) — those need the full 6-DOF Cosserat node. A1a reports `carried_dof==2` vs `axiom_dof==6`; "No single engine carries more than one or two" (`common/engine-capability-map.md:19`). Discipline `ave-representation-capability-check`. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**
- **(13) The $S$-exponent must be single-sourced — RESOLVED (Grant F1 ruling).** The exponent defect is now **FIXED IN CODE**: `src/ave/core/master_equation_fdtd.py:184-188` (`n_em_index()`) returns $n_{EM}=S^{0.5}$ — the internally-consistent $c_{eff}^2=c_0^2/S$ form (`:148-151`) — with the in-code correction note at `:172-183` ("Legacy magnitude was $S^{1/4}$ … an exponent defect — half the physical power; corrected to ½ here"), mirrored in `src/ave/core/crystal_engine.py:431-432` ("The legacy magnitude was S^{1/4} … Corrected to ½ here"). Resolved by **Grant's F1 ruling** (`research/2026-07-07_electron-lock_design-note.md:316-319`: "the apparent √S-vs-$S^{1/4}$ ambiguity was an already-corrected code defect … resolved by Grant's F1 ruling"; canonical $S^{0.5}$ per `research/2026-06-30_electron-portmap-derivation_result.md:550`). A4 verifies the $c_{eff}^2=c_0^2/S$ form; the old `:165-169` line-anchors have drifted. Discipline `ave-canonical-source`.
- **(13a) The KB symbol $n_{eff}$ is OVERLOADED (√S EM vs 1/√S gravitational) — LIVE (KB-owner decision).** Distinct from the closed exponent defect above: the engine itself surfaces, and declines to silently reconcile, that $n_{eff}$ denotes $\sqrt{S}$ EM-transverse ($\delta n_{iso}=\sqrt{S}-1$ content at `vacuum-birefringence-e4.md:108-110`) but $1/\sqrt{S}$ gravitational (the $n_{eff}=c_0/c_{eff}=1/\sqrt{S}$ row at `substrate-perspective-electron.md:60`) — flagged in code at `master_equation_fdtd.py:178-180` + `crystal_engine.py:433-435`. ⚠ **The SOURCE comments at `master_equation_fdtd.py:178-179` carry STALE anchors** (`vacuum-birefringence-e4.md:12` / `substrate-perspective-electron.md:58`) — flag-only; the engine module stays untouched in this PR. **flag-don't-fix:** a KB-owner symbol decision; the code names the overload and picks no symbol. Discipline `ave-canonical-source`.
- **(14) Achromatic deflection ($\Gamma=0$) under a SYM bias must reproduce.** A co-scaled $\varepsilon\cdot\mu$ gradient keeps $Z=Z_0$ ($\Gamma\to0$) and bends light frequency-INDEPENDENTLY — the AVE-distinct gravitational-lensing mechanism (T2.2; `clm-k9up5c` "Achromatic Impedance Lens"). The deflection MAGNITUDE rides the input $A_0(x)$ — chord-vs-echo of the magnitude left OPEN, not headlined. Discipline `ave-discrimination-check`.
- **(15) The same operator code path must run at every scale; and a simulation is a derivation-support, never an experiment.** The SAME callable forces $\omega_R\cdot M=18/49$ at electron-mass AND BH-mass inputs (30+ OOM apart; `src/tests/engine_acceptance/test_operators.py`), $A_0$ varies, the operator does not (`common/operators.md:91` "scale-invariance is the framework's distinguishing claim"). Per INVARIANT-S10 every acceptance test registers as a `sup-` node (derivation branch), and per INVARIANT-S9 never as an `exp-` (a simulation is not an experiment). Discipline `ave-regime-phase-state-check`.

## RUNG-1 EXISTENCE requirements (rows 16–18; 2026-06-17 L3 posited-mass-cage arc)

Three requirement rows added from the RUNG-1 EXISTENCE arc (T3.3/T3.4 of `src/tests/engine_acceptance/test_l3_mass_cage.py`; sup- nodes hosted in [`engine-acceptance-suite.md`](engine-acceptance-suite.md); companion property×bucket sheet at [`electron-bound-resonator-coverage.md`](../../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md)):

- **(16) A bound mode must be excited by a density-peak / shell BREATHING kick, not a monopole/DC kick.** A monopole/DC kick on the posited Gaussian core does NOT ring — it slowly RELAXES, and the dominant FFT component is bin 1, whose $\omega\propto1/n_{steps}$ is a run-length artifact, not a physical mode (`test_l3_mass_cage.py:660-667`, T3.4a). With a radial-shell breathing kick ($\partial_t V$ on the wall antinode), $\omega_{cutoff}\approx2.87$ is run-length-STABLE (peak/mean≈456). Discipline: empirical-driver (Rule 10 density-peak sampling).
- **(17) A chord-vs-echo $Q$ read must REMOVE every $\alpha$-bake and measure $Q$ from cold dynamics.** Reading any display computed from the baked $Q_{TANK}=1/\alpha$ (`src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py:72`) returns 137 by construction (the instrument-echo-trap, `theorem-3-1-q-factor.md:21`). With both $\alpha$-bakes removed ($Q_{TANK}$ AND `gamma_em_sq` at `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py:364`), the cold cage's $Q_{ringdown}\approx30.8$ — NOT 137 — empirically confirming $Q=1/\alpha$ is an instance-baked VALUE-ECHO, not a cage-emergent chord (clean chord-vs-echo NEGATIVE; corroborates the value-scoped verdict at `theorem-3-1-q-factor.md:19`). Discipline: `consistency-vs-emergence`, `ave-canonical-source`.
- **(18) Top-$K$ field-density / $\Gamma$ extractions must exclude PML cells.** A top-$K$ $|\Gamma|$ read that includes PML cells returns the frozen-absorbing artifact, not interior physics. T3.3 reads $\Gamma_{bulk}$ on the PML-EXCLUDED interior, so $\Gamma_{min}(0.95)=-0.283$ (crosses the −0.25 OP2 gate), →0 in vacuum, floors above −1 (S_min clip) — a genuine interior wall (`test_l3_mass_cage.py:526`, T3.3). Discipline: empirical-driver (Rule 10 PML exclusion).

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex` (canonical Vol 9 chapter file)

---

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is byte-exact and is never reworded.

**Rows carried in this file.**

- **`:30`** — stamped at `:30`. *(family: engine DOF requirement)*
  Quoted claim, byte-exact at HEAD:
  ```text
  The transverse-only carrier (2 DOF) cannot host mass (L3 longitudinal) or charge (L4 micro-rotation) — those need the full 6-DOF Cosserat node.
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Requirement 12 states mass-hosting needs the engine to CARRY the longitudinal DOF; under the carve there is no independent bulk DOF — the requirement re-derives as constraint/projection machinery + A1 accounting, not an evolved DOF.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

