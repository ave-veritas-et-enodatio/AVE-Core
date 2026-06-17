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
- **Cross-sector couplings as CONSERVED Hamiltonian pairs** (source + back-reaction from one $H_{couple}$; energize-lock, no non-conservative pump — the EMF `k4_cosserat_coupling.py:550` lesson).
- **Source symmetry class must admit the target topology** (centrosymmetric source cannot select a chiral knot — graft-v2).
- **Conservation canaries on float64** (H-drift, $|\mathbf{L}|$ gates are the pump-vs-lock detectors); fixed $N$ across compared runs; alias-checked extractors with reliability gates **and representation-capability-validated at the sampling scale** (plant-$(2,3)$-at-de-novo-scale $\to$ read-$(2,3)$; minor radius $r \gtrsim 3$ cells — a TRUE $(2,3)$ reads back as $(2,2)$/garbage at $r\approx1.1$ cells, so de-novo $w_{pol}=0$ nulls are partly representation-limited per the extractor-poloidal-misread note); observers strictly read-only.
- **Regime-reachability**: the engine must reach the regime the test requires (bulk near-yield for rectification); sub-yield nulls are artifacts.
- **(Candidate — characterization-in-flight) Wall sharpness / leak must be shown NOT regularization-limited.** Sweep $S_{min}$ / $A_{cap}$ before attributing any wall-sharpness / leak number (e.g. $\Gamma_{min}\approx-0.85$ carried across graft-v2/v3) to a physical constant ($\alpha$ above all); a number that tracks a regularization knob is apparatus, not physics. In-flight characterization on `analysis/2026-06-10-apparatus-floors` ($S_{min}$/$A_{cap}$ wall attribution + $H_{bel}$ ledger floor + wall-sign audit); discipline `ave-apparatus-floor-attribution`. NOT yet an adjudicated requirement — promote on that branch's verdict.

## Acceptance-suite requirements (rows 11–15; 2026-06-16/17 ground-up arc)

Five requirement rows added from the ground-up engine-acceptance arc (the suite at `src/tests/engine_acceptance/`, wired into the claim-DAG by [`engine-acceptance-suite.md`](engine-acceptance-suite.md)). Each ← a documented engine-failure lesson from THIS arc, citing its canonical home:

- **(11) Chiral / optical-activity rotation must be unitary (copy-first, no NumPy view-aliasing); the losslessness gate must run rotation-ON.** In-place $2\times2$ rotation on NumPy views (`src/ave/core/chiral_lattice_vector.py:49-58`, pre-fix) makes the rotation non-orthogonal → ~O(1) energy drift (Axiom-3 leak); the $\kappa=0$ free-photon gates never hit it, but an energy gate WITH rotation ON (A1b / T1.5) does. Discipline `substrate-native-check`.
- **(12) The medium must carry the DOF the excitation needs.** The transverse-only carrier (2 DOF) cannot host mass (L3 longitudinal) or charge (L4 micro-rotation) — those need the full 6-DOF Cosserat node. A1a reports `carried_dof==2` vs `axiom_dof==6`; "No single engine carries more than one or two" (`common/engine-capability-map.md:19`). Discipline `ave-representation-capability-check`.
- **(13) The $S$-exponent must be single-sourced.** `src/ave/core/master_equation_fdtd.py:169` returns $n=S^{0.25}$ (the `:165-168` block above it is the flag-don't-fix comment) while its own `c_eff_squared` (`:148-151`) implies $n=S^{0.5}$ — the two disagree. A4 verifies the internally-consistent $c_{eff}^2=c_0^2/S$ form and surfaces the exponent defect (flag-don't-fix); a physics-review item to adjudicate before any L3/L4 build that consumes $n$ or $c_{shear}$. Discipline `ave-canonical-source`.
- **(14) Achromatic deflection ($\Gamma=0$) under a SYM bias must reproduce.** A co-scaled $\varepsilon\cdot\mu$ gradient keeps $Z=Z_0$ ($\Gamma\to0$) and bends light frequency-INDEPENDENTLY — the AVE-distinct gravitational-lensing mechanism (T2.2; `clm-k9up5c` "Achromatic Impedance Lens"). The deflection MAGNITUDE rides the input $A_0(x)$ — chord-vs-echo of the magnitude left OPEN, not headlined. Discipline `ave-discrimination-check`.
- **(15) The same operator code path must run at every scale; and a simulation is a derivation-support, never an experiment.** The SAME callable forces $\omega_R\cdot M=18/49$ at electron-mass AND BH-mass inputs (30+ OOM apart; `src/tests/engine_acceptance/test_operators.py`), $A_0$ varies, the operator does not (`common/operators.md:91` "scale-invariance is the framework's distinguishing claim"). Per INVARIANT-S10 every acceptance test registers as a `sup-` node (derivation branch), and per INVARIANT-S9 never as an `exp-` (a simulation is not an experiment). Discipline `ave-regime-phase-state-check`.

## Manuscript counterpart

`manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex` (canonical Vol 9 chapter file)

---
