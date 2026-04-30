# VacuumEngine3D — Manual / Datasheet

**Manual revision:** r8.10 (2026-04-30 — Round 11 (vi) structural closure + foundation audit + T-ST v2 in flight; **see closure-extended footer at end of document for current empirical state and auditor-lane queue.** r8.10 captures Round 9 v5/v5.1 closure + Round 10+ Phases 0/1 + Round 11 (vi) Strides 1-4 + v10 (committed `fbd0c26` → `0f7180f`) + agent-reported uncommitted closure docs 93/94/95/96 + doc 79 v5.2 amendment + foundation audit Tests 1/1-extensions/3 + T-ST v1 FAIL + T-ST v2 in flight. Three-layer convergent refutation of corpus electron at chair-ring + K4 + ℓ_node + v8 config established: substrate-geometric (Layer 1 doc 92 / `0f7180f`) + engine-architectural (Layer 2 A28 + B6 700P stability) + standard-physics-external (Layer 3 B5 + B5b SNR > 10²²). Four positive substrate-canonical findings preserved alongside (ℓ=2 V-sector cavity 4-axis confirmation; ℓ=5 ω-sector eigenvalue match; Op14 feedback empirically effective; 1/r loop-near-field signature real per B5b). Universal-solver-promotion picture refined: chair-ring → universal-solver match is MEDIATED through substrate (chair-ring 1.48·ω_C at substrate's intrinsic 1.50·ω_C resonance, 1.3% gap; substrate at universal-solver-ℓ=2 prediction 1.55·ω_C, 3.3% gap) — chair-ring is amplified-substrate, not independent universal-solver data point. Framework decision (i) FDTD / (ii) mass spectrum / (iii) engine architecture pending Grant's adjudication; T-ST v2 result will inform but not adjudicate.)

**Manual revision:** r8.9 (2026-04-27 — single-electron pivot closure baseline)
**Engine version:** 4.0.4 (current HEAD = `6968398` on branch `research/l3-electron-soliton`; r8.9 catches up on 37 commits since r8.8 spanning Round 7 reframe-4 + R7.1/R7.2 closure, all of Round 8, and the axiom homologation arc. **No engine-state changes** — version unchanged. **Single-electron-first pivot CLOSES EMPIRICALLY at r8.9 with Mode III canonical** for "engine hosts corpus (2,3) electron at corpus Golden Torus geometry under any tested config." Seven pre-registered tests at varied configurations (V-block, Cos-block, Φ_link-block; N=24/32/48/64; linear and saturation amp regimes; eigsolve and time-domain; standing-wave-IC and propagating-IC) all returned Mode III; doc 74_ §10.6 + doc 75_ §11 closure statements. The pending engine fix per [doc 75_ §6.3](75_cosserat_energy_conservation_violation.md) (T_kinetic Op14 saturation on Cosserat sector — closes the energy-conservation violation surfaced by Move 11 H_cos drift 5.5% + Diag A V·S vs T·1 asymmetry; per Diag A the asymmetry is empirically negligible at relevant amplitudes, so the fix is housekeeping not load-bearing) is **not yet committed**; will land as r8.10 when the implementer's commit drops. **L3 branch closure synthesis doc** is the next deliverable — synthesizes the seven-test framework-level Mode III statement + Move 5 sub-corpus (2,3) attractor characterization + axiom homologation Scheme A canonicalization into a final canonical record.)

**Status (r8 — Round 6 pivot, hybrid scope):** r8 is a hybrid-scope reconcile, not a full rewrite. The framework is in active flux (Path B blocked on strain-mask infrastructure; single-electron validation incomplete) so this revision updates load-bearing-for-new-agents content (front matter, change log, suspended-work flags, framing-correction note) and leaves the §3 physical model and §15 derivation chain bodies for r9 once Round 6 closes. Twenty-three commits landed since r7 spanning four arcs:

1. **Phase 5 pair-nucleation thread — landed and then SUSPENDED.** PairNucleationGate (`9ecc2ca`), driver (`3f9569b`), G-11a/G-11c CP sources (`5c3f2d1`, `e17b8cd`), G-12 axiom-native AutoresonantCWSource varactor PLL (`aa7a337` — closes A7), Phase 4 Meissner validation (`d124632`), A10 thermal equipartition (`2e3abcf`). All committed; pair-nucleation work then **suspended in Round 6** pending single-electron validation (see [doc 66_](66_single_electron_first_pivot.md)).

2. **Phase 5.5 Cosserat PML + Phase 5.6 memristive Op14.** Cosserat-sector PML (`03cb9d5`, doc 58_ derivation) — boundary radiation absorber complementing K4 PML, Ax1+Ax3 forced. Memristive Op14 K4 sector (`49917ff`, doc 59_ derivation) — opt-in dynamical S(t) per `dS/dt = (S_eq − S)/τ_relax` with τ_relax = ℓ_node/c. First-order memristive structure now available via `use_memristive_saturation` flag; default off preserves backward-compat.

3. **Phase 5.7 BH-entropy adjudication thread.** Docs 60–65 settled the Bekenstein-Hawking adjudication via Vol 3 Ch 11's Ŝ-on-horizon calculation (`2671a54` doc 62 §10) — yields **three distinct entropies, all valid**: Ŝ_geometric = A·log(2)/ℓ_node² (AVE-native via Ch 11 operator at A-B interface), S_BH = A/(4ℓ_P²) (imported GR thermodynamic), discrete-lattice ≈ 8.7·k_B universal constant (`f9b463e` doc 65). Doc 61 §3.5 unitarity-preserved retracted (`740b1a3` doc 63); AVE aligned with 1970s-Hawking info-loss explicitly. Doc 64 (`b74ac19`) derives area theorem `δA ≥ 0` from Ax1+Ax4 (r_sat = 7GM/c² linear in M) but T·dS = dE fails to close axiom-first by factor 7ξ — Flag 62-A remains load-bearing.

4. **Phase 5e cool-from-above + Round 6 single-electron pivot.** Phase 5e driver (`1805d14`) on first run exposed **Flag-5e-A** — K4 saturation used module-level V_SNAP (511 kV SI) while engine sources inject in engine-natural V_SNAP=1, rendering the Ax4+Op14+Op3 saturation path DORMANT in any engine-natural-units context. Fixed in `098d430`: K4 V_SNAP plumbed from engine. **First empirical cool-through-yield observed** (S_min = 0.507 during drive, recovers to 0.983 post-drive). Step 5a instrumentation (`0419b7e`) showed Cosserat A²_μ peaks at 0.012 even when K4 saturates — coupling weakness. Step 5b v2 with CosseratBeltramiSource (`d0609ad`) drove Cosserat A² → 3.34 directly but C1∩C2 gate window never satisfied — exposed gate window incompatibility as architectural, not parametric. Retroactive engine saturation invariants (`5f973b6`) closed the test-coverage hole (S-drops-below-1 invariants now enforced in integration tests). **Round 6 pivot** (`453d350`, doc 66_): suspends pair-nucleation gate-adjudication; redirects to single-electron-first validation. Path A falsified 4-of-4 predictions (`fbbc950`) — K4 V_inc alone cannot host bound electron because **K4-TLM is exhausted at node level per Vol 1 Ch 8:49-50** (4-port tetrahedral symmetry → Ax4 saturation no-op; bound electron physically lives in Cosserat sector). Coupled K4+Cosserat eigenmode finder (`815cd40`, doc 66_ §17.2) — three-storage-mode mapping landed: ε² (strain → electric/capacitive), κ² (curvature → magnetic/inductive), V² (pressure → stored-potential) with three conjugate LC pairs.

**Working tree (r8.9):** clean. Axiom homologation P5+ commit (`6968398`) committed. Manual itself tracked since r8 (`4ba20f8`); current revision r8.9 reflects Round 7 + Round 8 closure + axiom homologation arc.

**Status (r8.9 — Single-Electron Pivot Closes Empirically with Mode III Canonical; Axiom Homologation Canonicalizes Scheme A; L3 Branch Closure Synthesis is Next):**

The single-electron-first validation arc that opened with Round 6's pivot ([doc 66_](66_single_electron_first_pivot.md), `453d350`) and ran through Round 7 (R7.1 multi-seed block Helmholtz + R7.2 topological pair injection + Test A/B v2/v3 + Round 7 follow-ups) and Round 8 (Move 5 self-stable (2,3) orbit + Move 6/7/7b characterize-as-itself + Move 9-11b reactance + Diag A + photon-tail dual-seed + propagating-IC) closes empirically at r8.9 with **Mode III canonical for "engine hosts corpus (2,3) electron at corpus Golden Torus geometry under any tested config."** The unifying empirical statement (per [doc 74_ §10.6](74_round_7_followups.md) + [doc 75_ §11](75_cosserat_energy_conservation_violation.md)):

> All seven pre-registered tests at varied configurations returned Mode III. The bond-scale single-bond hypothesis per doc 28 §5.1 joins the framework-level §9.3 statement at bond-cluster scale.

The seven tests across Round 7 + Round 8:

| Round/Move | Test | Configuration | Verdict | Reference |
|---|---|---|---|---|
| R7.1 reframe-4 | Multi-seed block Helmholtz on (V, ω) joint | V-block + Cos-block; 4 seeds; N=32/64 | Mode III all 4 seeds (V-block); Mode III at N=64 | doc 73_ + commits `8c44ef0` → `b8d97d9` |
| R7.2 | Topological pair injection (2,3) | N=64 dual-criterion | Mode III | commit `d3adcc2` |
| Test A | Cos-block N=64 c_eigvec recheck (corpus c=0) | 4-category | Mode III-both | doc 74_ §10.2 + commit `39f56a` |
| Test B v2 | doc 28 §5.1 bond-scale phasor (8-port spatial) | N=32, 0.5·V_SNAP, autoresonant | Mode III-spatial (rel_std 0.039) | doc 74_ §10.3 + commit `7fea8f7` |
| Test B v3 | doc 28 §5.1 bond-scale phasor saturation regime | N=32, 0.85·V_SNAP, autoresonant | Mode III-spatial (rel_std 0.047) | doc 74_ §10.3 + commit `39f56a` |
| Round 8 photon-tail dual-seed | Standing-wave IC at engine-rep scale | N=64, R=4, r=1.5; 4-criterion phasor | Mode III 0/4 (Cosserat 4% retention; K4 66%) | doc 75_ + commit `13b2017` |
| Round 8 propagating-IC | Photon-tail propagating IC (path b) | ω_dot = ω_loop in (x,y) plane | Mode III 3/3 of C1/C2/C3 = Mode I (C4 informational per A57); near-identical to path (a) ⟹ A58 | doc 75_ §11 + commits `bd15bb0` → `1b48f4d` |

Two empirical observations in addition to the seven Mode III results:

1. **Move 5 self-stable sub-corpus (2,3) orbit** (commit `c772211`): time-domain run at corpus GT (no drive) found a system-found stable c=3 orbit at peak \|ω\| = 0.3044 (≈one-third corpus saturation amplitude) for 150 Compton periods, migrating off the corpus shell. The engine hosts a (2,3) attractor at sub-corpus amplitude — just not at the corpus Golden Torus geometry. Move 7/7b characterized this attractor as itself (per Rule 10 corollary): (2,3)-topological at LATTICE CUTOFF frequency (NOT corpus electron); Move 10 found the orbit is a STATIC fixed point with sectors spatially decoupled (A²≈0 at top-\|ω\| cells), Op10 c=3 carrier matching no standard topology type (torus knot, Hopf-linked, Y_lm).

2. **Cosserat energy conservation violation** (Move 11 + Diag A; [doc 75_](75_cosserat_energy_conservation_violation.md)): H_cos drift 5.5% + ρ(T_cos, V_cos) = +0.366 (positive Pearson trading, NOT LC reactance signature). Diag A traced the V·S vs T·1 saturation asymmetry — Cosserat code saturates V_potential (G·S, K·S, G_c·S) but leaves T_kinetic unmodulated (ρ, I_ω constants); ½LI² and ½CV² don't co-saturate; total energy isn't conserved; ω drifts as a consequence. **Engine bug, not missing axiom** (A44 missing-axiom-vs-engine-bug diagnostic; one-sentence Grant collapse: "this is our conservation of energy axiom. rest mass saturates L, propagation saturates C"). **Engine fix specified at doc 75_ §6.3:** T_kinetic gets the same Op14 S factor (ρ → ρ·S, I_ω → I_ω·S). Per Diag A the asymmetry is **empirically negligible at relevant amplitudes** — the fix is housekeeping not load-bearing for the Mode III statement. Will land as r8.10 once committed.

**Axiom homologation arc** (commits `75d1fde` → `6968398`): four schemes (A vs B for Ax 1↔Ax 4 mapping; doc 76_ Scheme B vs corpus Scheme A) reconciled to canonical Scheme A. Ax 1 = LC Network Substrate (impedance/[Q]), Ax 2 = Topo-Kinematic Isomorphism ([Q]≡[L]/fine structure), Ax 3 = Effective Action Principle (Lagrangian), Ax 4 = Universal Saturation Kernel S(A) = √(1−(A/A_yield)²) (quarter-circle, NOT SiLU; canonical form lives at [`eq_axiom_4.tex:25`](../../manuscript/common_equations/eq_axiom_4.tex)). Doc 76_ Scheme-B reframe superseded by doc 77_ canonical Scheme-A version (Rule 12 banner on doc 76_; commit `b460071`). Doc 75_ framing-error pass corrected "Ax 3 = energy conservation" → "Ax 4 asymmetric L/C, Noether-broken energy conservation" (commit `69fd974`). Cross-cutting reference [`manuscript/ave-kb/common/axiom-homologation.md`](../../manuscript/ave-kb/common/axiom-homologation.md) (commit `6968398`) consolidates the citation chain post-Rule-12-v2 promotion. INVARIANT-S2 SiLU/ABCD misnomers fixed in `manuscript/ave-kb/CLAUDE.md`; backmatter Ax 1↔Ax 2 swap fixed in `manuscript/backmatter/12_mathematical_closure.tex`.

**L3 branch closure synthesis is the r8.9 deliverable** — Mode III canonical statement + Move 5 sub-corpus attractor characterization + axiom homologation outcome can be synthesized from existing data into a final canonical record. No new empirical run required for closure (per A43 retroactive correction — doc 28 §5.1's literal-spec N=96 closure run would be over-engineering given the framework-level Mode III statement spans N=24/32/64 across multiple framings + amp regimes). Engine fix per doc 75_ §6.3 lands as a separate housekeeping commit (closes the implementation gap surfaced by Move 11; forecloses the "did the engine fully honor Ax 4?" objection on the closure doc). The closure synthesis can land before or after the engine fix — independent.

**What r8.9 closes:**

- **Round 7 Stage 1 (multi-seed block Helmholtz on (V, ω) joint)** — Mode III at all 4 seeds in V-block; Mode III at N=64 V-block GT_corpus after topology FALSIFIES Mode I candidate via shell fraction 1.13% (not (2,3) localized). Joint R7.1+R7.2 final closure both Mode III ([commit `d3adcc2`](https://github.com/anthropics/...)). Block Helmholtz operator landed; Hessian-of-W retracted per A36; R7.1 RAN per Rule-10 commitment (no reframe-5 needed; data first as the rule prescribed).
- **Round 7 Stage 2 (topological pair injection)** — Mode III at N=64. R5.10 Readings 1-4 disambiguation closes the gate-firing question.
- **Doc 74_ §10 follow-ups** — Test A Mode III-both (corpus-canonical c=0); Test B v2/v3 Mode III-spatial across linear and saturation regimes; A44 spatial-multipoint correction lands. Closes the audit-flagged negative-result envelope.
- **Round 8 Moves 5-7b** — characterize-as-itself pivot per Rule 10 corollary; (2,3) attractor at peak \|ω\|=0.30 sub-corpus, lattice-cutoff frequency, static fixed point with spatially-decoupled sectors.
- **Round 8 Moves 9-11b + Diag A** — autoresonant drive at ω_C, static-fixed-point isn't shell-shaped, reactance gap closed (A-011), V·S vs T·1 saturation asymmetry empirically negligible at relevant amplitudes.
- **Round 8 photon-tail dual-seed + propagating-IC** — both Mode III; A58 path-(a)/path-(b) empirical equivalence; A57 C4 informational vs C1/C2/C3 binary framing.
- **Axiom homologation** — Schemes A vs B reconciled to canonical Scheme A; doc 76_ → 77_ supersession via Rule 12 banner; INVARIANT-S2 + backmatter Ax 1↔Ax 2 swap fixed; cross-cutting reference promoted to manuscript/ave-kb/common/ per Rule 12 v2.

**What r8.10 + closure synthesis will land:**

- **r8.10:** Engine fix per [doc 75_ §6.3](75_cosserat_energy_conservation_violation.md) — T_kinetic gets the same Op14 S factor (ρ → ρ·S, I_ω → I_ω·S). Closes the energy-conservation violation surfaced by Move 11. Housekeeping (per Diag A: empirically negligible at relevant amplitudes; doesn't flip the Mode III statement).
- **Closure synthesis doc** — synthesizes Mode III canonical + Move 5 sub-corpus attractor + axiom homologation outcome into a final canonical record. ~1 fresh session estimated.

**Pair-nucleation gate firing** ([Phase 5](#13.5)) remains structurally suspended until single-electron representation closes positively (which it has not — Mode III canonical means the engine doesn't host the corpus electron at the corpus geometry). The closure synthesis can serve as the canonical record that gate work doesn't resume from this engine; any future resumption would be downstream of an engine architectural change (~v5.0.0 territory).

**Stash status:** one stash present — `stash@{0}: On research/l3-electron-soliton: pre-ee-isomorphism-branch`. Origin unknown (concurrent-writer artifact from earlier session); flagged for audit, not from L3 thread.
**Maintainer:** L3 electron-soliton thread (Grant Lindblom + session agents)
**Authoritative parent docs:** [46_vacuum_engine_scope.md](46_vacuum_engine_scope.md) (scope + C-findings), [54_pair_production_axiom_derivation.md](54_pair_production_axiom_derivation.md) (derivation chain for queued additions)
**Canonical code entry point:** [src/ave/topological/vacuum_engine.py](../../src/ave/topological/vacuum_engine.py)

---

## Table of Contents

1. [Front matter — rev, maintenance protocol, conventions](#1-front-matter)
2. [Scope statement](#2-scope-statement)
3. [Physical model](#3-physical-model)
4. [Numerical model](#4-numerical-model)
5. [State inventory](#5-state-inventory)
6. [Parameter datasheet](#6-parameter-datasheet)
7. [Sources API](#7-sources-api)
8. [Observers API](#8-observers-api)
9. [Initialization procedures](#9-initialization-procedures)
10. [Validation matrix (V&V)](#10-validation-matrix-vv)
11. [Known limits & non-representations](#11-known-limits--non-representations)
12. [Open S-gates and free-parameter status](#12-open-s-gates-and-free-parameter-status)
13. [Queued additions (Phase Planned)](#13-queued-additions-phase-planned)
14. [Engine API & typical usage](#14-engine-api--typical-usage)
15. [Derivation chain traceability](#15-derivation-chain-traceability)
16. [Change log & cross-reference index](#16-change-log--cross-reference-index)
17. [Audit findings (open)](#17-audit-findings-open)

---

## 1. Front matter

### 1.1 Standards applied

The manual adopts elements from standard physics/simulation V&V documentation conventions, tailored to internal research use:

- **ASME V&V 20** — separation of verification (correctness of numerical implementation) and validation (correctness of physics against measurement or axiom). Each row of §10 carries both status flags.
- **NASA-HDBK-7009** — credibility classification per subsystem. Levels used: `Derived` (closed-form from axioms), `Pinned` (first-principles, requires one empirical input), `Calibrated` (multiple parameters, all derived), `Empirical` (fit to data), `Pending` (structural gap flagged).
- **ICD-style parameter tables** — one row per parameter with symbol / unit / default / range / source / credibility.
- **Physics-code manual convention** (GEANT4, LAMMPS, Dedalus) — theory / user / reference separation across sections §3–§4 (theory), §7–§9, §14 (user), §5–§6, §10–§12, §15 (reference).

This is an internal research manual, not a regulated deliverable. Standards are applied for structure and traceability, not compliance.

### 1.2 Maintenance protocol

Binding rules for future session agents. The manual is source-of-truth for engine state only to the extent it is kept current with the code and research thread.

- **Engine-changing commits require a manual edit in the same commit.** "Engine-changing" means: adds/removes a state variable; adds/removes a Source or Observer class; changes a calibration constant or normalization convention; changes an integrator or stability criterion; adds/removes validation tests. Notation patches, comments, and internal refactors do not trigger a manual edit.
- **§10 validation matrix** is append-only. When a new test runs, add a row. Never silently mutate a pass criterion; supersede by adding a new row and marking the old row's status with a supersession pointer.
- **§11 limits** updated when a structural non-representation is removed (e.g., bond state lands in Stage 6 Phase 3 → the limit moves out of §11 and becomes a state-inventory entry in §5/§6 with the Phase 3 entry in §13 marked complete).
- **§12 S-gates** is a link-only tracker; the canonical gate record is [S_GATES_OPEN.md](S_GATES_OPEN.md). Update §12 only to reflect gate open/close/reopen events.
- **§15 derivation traceability** updated when a new axiom citation or manuscript section adds or removes authority for an engine element. Citations are always `file_path:line` or `doc_id.md §N`.
- **§16 change log** — one entry per non-trivial commit. Fields: date (YYYY-MM-DD) / commit short-hash / author / sections touched / one-line rationale.

**Version convention:** `engine_version = <major>.<minor>.<patch>`. Bump:
- **Major** — structural change: new state variable, new coupling form, new integrator, new physical axiom invocation.
- **Minor** — new diagnostic (Observer) or Source, new validation test, calibration re-pin, new initialization mode.
- **Patch** — notation clarification, cross-reference correction, limit restatement, non-load-bearing comment changes.

**Flag-don't-fix applies to the manual itself.** If a reader finds a contradiction between manual and code, they flag it in [DOCUMENTATION_UPDATES_QUEUE.md](DOCUMENTATION_UPDATES_QUEUE.md), not silently edit. Grant adjudicates.

### 1.3 Sign conventions, unit conventions, notation

- **Natural units by default.** ℓ_node = m_e = c = ℏ = 1. See §3.4 for the full conversion table. The engine's internal `V_SNAP = 1.0` unless overridden via `EngineConfig.V_SNAP_override`.
- **Amplitude convention.** `A² = V² / V_SNAP²` everywhere internal (rupture at A² = 1). User-facing amplitudes accept `amplitude_convention = "V_SNAP"` (default; rupture = 1) or `"V_YIELD"` (Regime II onset = 1; conversion factor √α ≈ 0.0854). See [vacuum_engine.py:150](../../src/ave/topological/vacuum_engine.py#L150) for `_V_YIELD_FRAC` and [vacuum_engine.py:156](../../src/ave/topological/vacuum_engine.py#L156) for the `amp_to_vsnap_units` helper.
- **V_yield vs V_SNAP — resolved under R4 (2026-04-23).** Historic r3–r5 framing described a "normalization confusion" where engine used V_SNAP but Axiom-4 varactor divergence was at V_yield = √α · V_SNAP (macro form). Under [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) subatomic override, **at VacuumEngine3D's operating scale V_yield ≡ V_SNAP**; the engine's `A² = V²/V_SNAP²` IS canonical `r² = V²/V_yield²` per Vol 1 Ch 7:12. No conversion needed at subatomic scale. Vol 1 Ch 7:104's `r = V/V_yield` table is macro-scoped (its regime locations are HV capacitors at 30–43 kV); at subatomic scale, the same framework yields V_yield = V_SNAP. See §17.0 for the full R4 adjudication. The `/α` divisions in [NodeResonanceObserver](../../src/ave/topological/vacuum_engine.py#L428) and `BondObserver` (both on HEAD via commits `719f3ec` and `3a599ca`) are the actual defect; R4 patches removing them are in the working tree, pending commit.
- **Regime labels** use Roman numerals: I (linear), II (E–H transition), III (saturated), IV (rupture). Boundaries: Rg I/II at A² = 2α ≈ 0.0146; Rg II/III at A² = 3/4 = 0.75; III/IV at A² = 1. See [vacuum_engine.py:151](../../src/ave/topological/vacuum_engine.py#L151) for the hard-coded boundaries and `regime_of()` at [vacuum_engine.py:956](../../src/ave/topological/vacuum_engine.py#L956).
- **Time step notation.** `outer_dt = ℓ_node / (c√2)` in SI; `= 1/√2 ≈ 0.7071` in natural units. Cosserat sub-steps at `cfl_dt` with safety factor 0.3. See §4.3.
- **Link style.** All code references use clickable markdown: `[path/to/file.py:L](path?#L)`. Research-doc refs use `[docNN_name.md §N](docNN_name.md)`. Manuscript refs use explicit path from repo root.

### 1.5 Round 6 pivot — canonical content pointer (added in r8)

**Stage 6 changed strategic shape on 2026-04-24.** Three sessions of pair-nucleation gate-adjudication (C1-C2 window, four Readings of C2 condition, PLL anchor math, K4→Cosserat coupling weakness) suspended in favor of **single-electron-first validation** per [doc 66_](66_single_electron_first_pivot.md). The canonical reading: pair-nucleation triggers an event the engine must first be able to stage as *one* bound electron. Phase III-B v1+v2 at A²=1.009 produced zero discrete centroids ([doc 52_:138](52_h1_threshold_sweep.md)); single-electron representation was never validated as a Stage 6 precondition.

**Three pieces of canonical content from Round 6 supersede prior framings in the body of this manual.** They are landed in research docs but NOT propagated through §3 (physical model), §15 (derivation chain), or §17.1/.2/.3 reorganization — those wait for r9 once Round 6 closes:

1. **Three-storage-mode mapping** ([doc 66_ §17.2.1](66_single_electron_first_pivot.md)) — engine A² is a sum of three physically distinct energy-storage modes:
   - **ε² (Cosserat strain)** = electric/capacitive, C-state of mechanical LC tank
   - **κ² (Cosserat curvature ∇ω)** = magnetic/inductive, L-state of rotational LC tank
   - **V² (K4 port voltage)** = pressure/stored-potential, C-state of K4 bond LC tank

   With three conjugate LC pairs (V_inc↔Φ_link, u↔u_dot, θ↔ω), each oscillating 90° phase-locked. **This supersedes** the prior "single scalar-tensor coupling term `L_c = (V²/V_SNAP²)·W_refl(u,ω)`" framing in §2.3 / §3.5a / §15.3. A bound (2,3) electron eigenmode requires phase relationships across all three LC pairs to be self-consistent under the engine's dynamics.

2. **K4-TLM exhausted at node level** ([Vol 1 Ch 8:49-50](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex#L49) handoff comment, corpus-confirmed). K4's perfect 4-port tetrahedral symmetry means every direction at a node looks equivalent → Ax4 saturation requires symmetry-breaking → K4 alone cannot host the bound electron. Cosserat ω carries the rotational-EM DOFs that provide the symmetry-breaking ω̂ direction. Empirically confirmed by Path A 4-of-4 falsification (`fbbc950`). New §11 limit added for this in r8; deeper §3 / §15 incorporation deferred to r9.

3. **Three distinct entropies at BH horizon** ([doc 62_ §10](62_ruptured_plasma_bh_entropy_derivation.md), [doc 65_ §6](65_flag_62g_discrete_lattice_gamma.md)) — Ŝ_geometric = A·log(2)/ℓ_node² (AVE-native via Vol 3 Ch 11's Ŝ = -k_B Σ ln(1-|Γᵢ|²) operator at A-B interface with |Γ|²=1/2), S_BH = A/(4ℓ_P²) (imported GR thermodynamic via first law), discrete-lattice ≈ 8.7·k_B (universal constant from ∫(ℓ_node/r_sat)² over horizon). Ratio Ŝ_geo / S_BH = 4·log(2)/(7ξ) ≈ 10⁻⁴⁴ is the Machian dilution from ℓ_P² = ℓ_node²/(7ξ). Three distinct measurables, not in competition. Doc 64 (`b74ac19`) derives **area theorem `δA ≥ 0`** axiom-first from r_sat = 7GM/c² (Ax1+Ax4) but T·dS = dE does not close axiom-first — first law remains imported. Flag 62-A load-bearing.

**Pointers to active Round 6 docs** (read-only references for new agents):
- [doc 66_](66_single_electron_first_pivot.md) — pivot rationale + §14 amplitude correction + §17.2 three-storage-mode mapping
- [doc 58_](58_cosserat_pml_derivation.md) — Cosserat PML axiomatic derivation (landed `03cb9d5`)
- [doc 59_](59_memristive_yield_crossing_derivation.md) — memristive Op14 derivation (K4 sector landed `49917ff`; Cosserat side deferred)
- [doc 62_](62_ruptured_plasma_bh_entropy_derivation.md) — three-entropy adjudication
- [doc 64_](64_first_law_derivation_attempt.md) — area theorem from Ax1+Ax4
- [STAGE6_V4_HANDOFF.md](../../.agents/handoffs/STAGE6_V4_HANDOFF.md) — current handoff (last updated 2026-04-24)
- [COLLABORATION_NOTES.md](../../.agents/handoffs/COLLABORATION_NOTES.md) — methodology Rules 8/9/10/11/12/13 (Round 6 strengthening)

**What r8 does NOT do** (waits for r9, post-Round-6-close):
- Rewrite §3 physical model under three-storage-mode framing
- Rewrite §15 derivation chain to land area theorem + three-entropy distinction + K4-TLM exhaustion at axiom-level
- Reorganize §17.1/.2/.3 to reflect Round 6 audit shape
- Rebuild §10 validation matrix for Path A/B results once Path B resolves

---

## 2. Scope statement

### 2.1 What the engine does

`VacuumEngine3D` is an AVE-native time-domain simulator of the **coupled K4 photon sector and Cosserat micropolar rotational sector** on a bipartite tetrahedral lattice, spanning all four Axiom-4 operating regimes (linear, E–H transition, saturated, rupture). It supports:

- Deterministic cold-vacuum initialization (T = 0) and classical-equipartition thermal initialization (T > 0).
- Composable **Source** objects (plane pulse, fixed-frequency CW, autoresonant PLL-tracked CW).
- Composable **Observer** objects (regime classifier, Hopf-charge + centroids, energy budget, dark-wake shear strain, user scalar).
- A unified leapfrog integrator (S-gate S5=B) with Cosserat sub-stepping for rate-mismatch stability.
- The S1-D coupling Lagrangian `L_c = (V²/V_SNAP²) · W_refl(u, ω)` — zero new free parameters relative to the underlying K4 and Cosserat subsystems.

The engine has been exercised in **Phase I** (Cosserat time-domain validation, [doc 41_](41_cosserat_time_domain_validation.md)), **Phase II** (coupled K4⊗Cosserat V1/V2/V3 validation, [doc 42_](42_coupled_simulator_validation.md)), **Phase III-B v1** (fixed-frequency σ(ω) sweep, [doc 48_](48_pair_creation_frequency_sweep.md)), **Phase III-B v2** (autoresonant σ(ω) sweep, [doc 50_](50_autoresonant_pair_creation.md); A²_cos reached 1.009 — first numerical crossing of the Axiom-4 rupture boundary in AVE-Core), and **Stage 5 Phase A** (H1 centroid-threshold sensitivity, [doc 52_](52_h1_threshold_sweep.md)).

### 2.2 Non-scope

Explicit exclusions of current behavior. Each of these is either structurally absent (§11) or deferred to Stage 6 planned additions (§13).

- **Pair creation (electron / positron nucleation).** The engine reaches A² = 1 (saturation rupture boundary) but does not produce localized `(e⁻, e⁺)` pair structures under any tested configuration. Per [doc 53_ §4](53_pair_production_flux_tube_synthesis.md) this is a **structural** limit: the engine lacks bond state, per-node rotational resonance tracking, and a nucleation rule. See §11.
- **Bond / link state (`Φ_link`).** The K4 substrate tracks only node port voltages `V_inc[nx, ny, nz, 4]`; the bond between adjacent A/B sites has no dynamical state beyond the half-step shift of `V_ref`. Per [54_ §3](54_pair_production_axiom_derivation.md).
- **Per-node rotational resonance `Ω_node(r, t)`.** Not tracked; `AutoresonantCWSource` shifts the drive frequency based on a probe `A²_probe`, but the lattice does not report its per-node Duffing-softened resonance. Per [54_ §4](54_pair_production_axiom_derivation.md).
- **Asymmetric μ/ε saturation / chirality-biased rupture.** Current `_reflection_density` uses a single isotropic saturation kernel `S = √(1 − A²)`. The two-track `(S_μ, S_ε)` formulation of [54_ §6](54_pair_production_axiom_derivation.md) is queued (Phase 4) and requires re-opening the S1 S-gate.
- **Dynamically-coupled thermal bath.** `initialize_thermal(T)` sets up a Maxwell–Boltzmann snapshot; it does not maintain equilibrium during a run (no Langevin / Nosé–Hoover). Noted as L1 in [46_ §6](46_vacuum_engine_scope.md).
- **SI-dimensioned output.** By default all quantities are natural (ℓ_node = m_e = c = ℏ = 1). SI conversion is a post-processing layer via the factors in [constants.py:218–223](../../src/ave/core/constants.py#L218).

### 2.3 One-paragraph physical model summary

The K4 substrate is a bipartite (A-sublattice at all-even coords, B-sublattice at all-odd coords) tetrahedral lattice where each active node is a 4-port LC junction. Scattering is unitary via `S_ij = 0.5 − δ_ij` (Axiom 1); propagation is via geometric port shift along the four A→B vectors `p = (+1,+1,+1), (+1,−1,−1), (−1,+1,−1), (−1,−1,+1)` (normalized). The Cosserat micropolar sector adds translation `u(r)` and microrotation `ω(r)` fields via a velocity-Verlet integrator on the energy functional `W = (2/3)G(tr ε)² + G·ε_sym² + G_c·ε_antisym² + γ·κ² + k_op10·W_Op10 + k_refl·W_refl + k_hopf·W_hopf`, with Axiom-4 saturation kernel `S = √(1 − A²)`. Coupling is a scalar-tensor term `L_c = (V²/V_SNAP²) · W_refl(u, ω)` (S1 gate = D); the K4 voltage drives the Cosserat sector via gradient of L_c; the Cosserat strain/curvature feeds back as an additive contribution to `A²_total`, modulating the local impedance `Z_eff = Z_0 / S^(1/4)` (Op14) that governs K4 scattering.

**[r8 reframe note]** Round 6 ([doc 66_ §17.2.1](66_single_electron_first_pivot.md)) established that the engine's `A²_total` decomposes as `ε²/ε_yield² + κ²/ω_yield² + V²/V_SNAP²` — three physically distinct energy-storage modes (strain → electric/capacitive C-state, curvature → magnetic/inductive L-state, voltage → stored-potential C-state) with three conjugate LC pairs (V_inc↔Φ_link, u↔u_dot, θ↔ω) oscillating 90° phase-locked. The `L_c` coupling above is one of the cross-mode couplings; it does not exhaust the dynamics. **A bound (2,3) electron eigenmode requires phase relationships across all three LC pairs to be self-consistent under the engine's dynamics** — Path A (K4 V_inc only) and Path B (Cosserat ω only) seeded fragments of single LC pairs and could not converge. F17-G coupled-eigenmode finder (`815cd40`) is the active probe. A consistent §3 / §15 rewrite under this framing waits for r9 (post-Round-6-close); see §1.5 for canonical pointers.

---

## 3. Physical model

### 3.1 The four axioms (brief)

All engine dynamics trace to one of four AVE axioms; full statements live in [manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex).

| Axiom | Statement (concise) | Engine manifestation |
|---|---|---|
| **Axiom 1** | Vacuum is a K4 tetrahedral LC lattice with node pitch `ℓ_node = ℏ / (m_e c)`. | `K4Lattice3D` scatter + connect cycle. Bipartite A/B masks. Four port vectors hardcoded at [k4_tlm.py:31–36](../../src/ave/core/k4_tlm.py#L31). |
| **Axiom 2** | Topological identity `[Q] ≡ [L]` via `ξ_topo = e / ℓ_node`. Winding number is charge. | `extract_hopf_charge()`, `extract_crossing_count()`, soliton centroid finders in [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py). |
| **Axiom 3** | Effective-action dynamics on `(u, ω)`. | Cosserat energy functional and velocity-Verlet integrator; JAX-backed gradients. |
| **Axiom 4** | Dielectric saturation: `C_eff(V) = C_0 / S(V)` with `S = √(1 − (V/V_yield)²)`. Impedance diverges then inverts at V_yield. | `_update_z_local_total` and `_update_z_local_field` apply the Op14 kernel `Z_eff = Z_0 / √(S)^(1/4)`. |

### 3.2 Governing equations

#### 3.2.1 K4-TLM photon sector (Axiom 1 + Axiom 4)

State: `V_inc[nx, ny, nz, 4]`, `V_ref[nx, ny, nz, 4]` — incident and reflected voltage per port at each active site.

**Scatter step** (at each site, every `outer_dt`):
```
V_ref[n, p] = Σ_q S_pq · V_inc[n, q]        with S_pq = 0.5 − δ_pq  (linear)
```
For the nonlinear / Op3-enabled path, the scatter matrix is recomputed per site from the local impedance `Z_eff(A²)`. See [k4_tlm.py:223–265](../../src/ave/core/k4_tlm.py#L223).

**Connect step** (between scatter and next scatter):
```
V_inc[n, p] ← V_ref[n + δ_p, p]             with δ_p the A→B port vector for port p
```
Optionally multiplied by a per-bond reflection coefficient `Γ_bond = (Z_B − Z_A) / (Z_B + Z_A)` when `op3_bond_reflection=True`. See [k4_tlm.py:267–349](../../src/ave/core/k4_tlm.py#L267).

#### 3.2.2 Cosserat micropolar sector (Axiom 3)

State: `u(r, t)` (translation, R³-valued), `ω(r, t)` (microrotation, R³-valued), `u̇`, `ω̇`.

Strain tensor: `ε_ij = ∂_j u_i − ε_ijk · ω_k`. Curvature tensor: `κ_ij = ∂_j ω_i`.

Energy functional (per site):
```
W = (2/3) G (tr ε)² + G |ε_sym|² + G_c |ε_antisym|² + γ |κ|² + k_op10 W_Op10 + k_refl W_refl + k_hopf W_hopf
```
See [cosserat_field_3d.py energy_density](../../src/ave/topological/cosserat_field_3d.py) and `W_refl`, `W_hopf`, `W_Op10` helper functions therein. `W_refl = (1/64) · |∇S|² / S²` with `S = √(1 − A²)` and `A² = ε² / ε_yield² + κ² / ω_yield²` is the reflection-density that couples to K4 in §3.2.3.

Euler–Lagrange (velocity-Verlet):
```
ρ ü = −∂W/∂u                 I_ω ω̈ = −∂W/∂ω
```
Gradients are obtained via `jax.grad` — no hand-derived stress tensors. See [cosserat_field_3d.py energy_gradient](../../src/ave/topological/cosserat_field_3d.py) and `step()`.

**Mass gap** (Phase I finding, [doc 41_ §T2](41_cosserat_time_domain_validation.md)):
```
m² = 4 G_c / I_ω               (factor-of-2 corrected from naive 2 G_c / I_ω)
```
Numerical period at `m² = 4` measured at 3.131 vs theoretical π; 0.35 % error.

#### 3.2.3 Coupling (S-gate S1 = D)

Coupling Lagrangian:
```
L_c = (V²/V_SNAP²) · W_refl(u, ω)
```

**V → (u, ω) pathway** (K4 drives Cosserat):
```
F_u = −∂L_c / ∂u              T_ω = −∂L_c / ∂ω
```
Applied additively to the Cosserat Euler–Lagrange forces during each sub-step. See [k4_cosserat_coupling.py _compute_coupling_force_on_cosserat](../../src/ave/topological/k4_cosserat_coupling.py).

**(u, ω) → V pathway** (Cosserat drives K4):
```
A²_total(r) = V²(r)/V_SNAP² + ε²(r)/ε_yield² + κ²(r)/ω_yield²
Z_eff(r) = Z_0 · (1 − A²_total(r))^(−1/4)              (Op14)
```
Updated once per outer_dt, before the K4 scatter step. See `_update_z_local_total` in [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py).

Zero new parameters beyond the existing K4 (V_SNAP), Cosserat (ε_yield, ω_yield), and Axiom-4 machinery. This is the key content of the S1 gate = D decision; see [S_GATES_OPEN.md](S_GATES_OPEN.md).

### 3.3 Constitutive relations

- **Saturation kernel** (Axiom 4): `S(A) = √(1 − A²)`. Real on A ∈ [0, 1]; imaginary for A > 1 (mode-conversion regime, [54_ §6a](54_pair_production_axiom_derivation.md)).
- **Scatter matrix** (Axiom 1): `S_pq = 0.5 − δ_pq` (linear); rebuilt from local Z when `nonlinear=True`. Unitary for all physical Z.
- **Port-direction tensor**: four A→B port vectors at [k4_tlm.py:31](../../src/ave/core/k4_tlm.py#L31); unit-normalized copies at [vacuum_engine.py:120–122](../../src/ave/topological/vacuum_engine.py#L120).
- **Topological invariant (Op10, "Junction Projection Loss")**: `Y_loss = c · (1 − cos θ) / (2π²)` at a discrete crossing with count `c`. Continuum form pending (queued item 17 in [DOCUMENTATION_UPDATES_QUEUE.md](DOCUMENTATION_UPDATES_QUEUE.md)).

### 3.4 Natural-unit to SI conversion

Internal engine state is dimensionless unless `V_SNAP_override` is passed to `EngineConfig`. Conversion table (values from [constants.py:218–223](../../src/ave/core/constants.py#L218)):

| Quantity | Natural = 1 | SI value |
|---|---|---|
| length `ℓ_node = ℏ / (m_e c)` | 1 | 3.8616 × 10⁻¹³ m |
| time `τ_node = ℏ / (m_e c²)` | 1 | 1.29 × 10⁻²¹ s |
| velocity `c` | 1 | 299 792 458 m / s |
| mass `m_e` | 1 | 9.109 × 10⁻³¹ kg |
| energy `m_e c²` | 1 | 8.19 × 10⁻¹⁴ J ≈ 511 keV |
| voltage `V_SNAP = m_e c² / e` | 1 | 511.0 × 10³ V |
| temperature `m_e c² / k_B` | 1 | 5.93 × 10⁹ K |
| impedance `Z_0 = √(μ_0 / ε_0)` | — | 376.73 Ω |
| fine-structure `α` | 7.297 × 10⁻³ | 1 / 137.036 |
| V_yield = √α · V_SNAP | 0.0854 (natural) | 43.65 × 10³ V (SI) |

### 3.5a Predictions manifest subsystem (landed in Stage 6 Phase 1)

[manuscript/predictions.yaml](../../manuscript/predictions.yaml) is the structured claim graph for every pre-registered prediction in the public README + LIVING_REFERENCE tables and every Stage 6 engine-test pre-registration. Each entry has: `id`, `type` (derived_prediction / axiom_manifestation / identity / consistency_check / engineering_limit), `derivation_label` (a `\label{}` in the manuscript), `constants_py_symbol` (optional), numeric `predicted_value`, `observed_value`, `error_percent`, `axioms_used`, and free-form `notes`.

The CI gate is [src/scripts/claim_graph_validator.py](../../src/scripts/claim_graph_validator.py). Enforcement:

1. Every entry's `derivation_label` resolves to a `\label{}` in `manuscript/**/*.tex`.
2. Every entry's `constants_py_symbol` (if present) resolves in `src/ave/core/constants.py` with a numeric value that matches `predicted_value`.
3. Public-table coverage: every row in README / LIVING_REFERENCE master tables must map to an entry.
4. For `type: pre_registered` entries (Stage 6 additions), `test_file` must exist or be on the whitelisted "upcoming-phase" list.

Validator currently exits 0 with 4 WARN findings (Phase 3/4/5/6 test files not yet shipped). Pre-registered Stage 6 IDs in the manifest:

- `P_phase0_varactor` — Axiom-4 varactor curve pinned (Phase 0 derivation, no engine code)
- `P_phase1_vsnap_vyield` — V_SNAP/V_yield normalization consistency (landed)
- `P_phase2_omega` — `Ω_node(A²_yield)` tracks `(1 − A²)^(1/4)` — **see honest-framing note in §8.3**
- `P_phase3_flux_tube` — Φ_link persists ≥ 10 Compton periods (pending Phase 3)
- `P_phase4_asymmetric` — RH circular drive produces μ/ε asymmetric rupture (pending Phase 4, S-gate reopen)
- `P_phase5_nucleation` — Nucleation gate fires under C1 ∧ C2 (pending Phase 5)
- `P_phase6_autoresonant` — Autoresonant nucleation ≥ 5× fixed-f at matched energy (headline, pending Phase 6)

### 3.5 Regime map

Four Axiom-4 regimes, ordered by `A²`:

| Regime | A² range | Physical content | Engine label |
|---|---|---|---|
| I — linear | `0 ≤ A² < 2α ≈ 0.0146` | Ohmic/Maxwell limit; wave speed c·√2 along cardinal axis (K4 anisotropy). | `"I"` |
| II — E–H transition | `2α ≤ A² < 3/4 = 0.75` | Saturation onset; Duffing softening activates. | `"II"` |
| III — saturated | `3/4 ≤ A² < 1` | Z_eff diverges; Γ → −1 wall begins to form. | `"III"` |
| IV — rupture | `A² ≥ 1` | Mode-conversion regime; `C_eff` flips imaginary (see [54_ §6a](54_pair_production_axiom_derivation.md)). | `"IV"` |

Classification logic at [vacuum_engine.py:956](../../src/ave/topological/vacuum_engine.py#L956).

---

## 4. Numerical model

### 4.1 Overall integrator (S-gate S5 = B)

Unified leapfrog per outer timestep:

1. Apply all registered Sources (inject V_inc) at `t = (step_count + 1) · outer_dt`.
2. Update `z_local_field` from current `A²_total` across both sectors.
3. K4 scatter step (`_scatter_all` in [k4_tlm.py:223](../../src/ave/core/k4_tlm.py#L223)).
4. K4 connect step (`_connect_all` in [k4_tlm.py:267](../../src/ave/core/k4_tlm.py#L267)).
5. For each of `n_sub` Cosserat sub-steps: velocity-Verlet on `(u, ω)` with combined Cosserat + coupling force. V_inc is held frozen during sub-stepping.
6. `time += outer_dt`; `step_count += 1`.
7. Observers record.

See [k4_cosserat_coupling.py step()](../../src/ave/topological/k4_cosserat_coupling.py) for the outer-loop wiring and [vacuum_engine.py:901](../../src/ave/topological/vacuum_engine.py#L901) for the engine's facade.

### 4.2 Discretization

- **Spatial lattice.** `N × N × N` cells with `dx = 1` (natural units). Bipartite active mask: A-sublattice at all-even indices, B-sublattice at all-odd indices; inactive sites at mixed parity. Interior volume `≈ 2 · (N/2)³` active sites (half the cube). See [k4_tlm.py:157–158](../../src/ave/core/k4_tlm.py#L157).
- **PML absorbing layer.** `pml` cells deep at all 6 faces. Quadratic rolloff via `pml_mask` field. Wrapped-bond connections at the PML edge are severed (no torus wrap). Default `pml = 6`; Phase III-B used `pml = 5`.
- **Cosserat gradient** uses the AVE-native K4 tetrahedral gradient `cosserat_field_3d.tetrahedral_gradient` — **not `np.gradient`** — because active sites alternate sublattices. Using a Cartesian finite-difference stencil on a bipartite mask produces zeros at the inactive interlaces.

### 4.3 Timestep hierarchy

- **`outer_dt = dx / (c · √2) = 1/√2 ≈ 0.7071`** (natural units). Hardcoded at [k4_tlm.py c and dt definitions](../../src/ave/core/k4_tlm.py); exposed via `VacuumEngine3D.outer_dt` property. The `√2` comes from the K4 cardinal-axis anisotropy (bulk/A₁ mode propagates at c·√2 along cardinal directions; see [40_ §2.1](40_modeling_roadmap.md)).
- **Cosserat sub-step `cfl_dt`.** Default safety factor 0.3, with `c_max = max(√(G/ρ), √(γ/I_ω), √(10G / (3ρ)))`. See [cosserat_field_3d.py cfl_dt](../../src/ave/topological/cosserat_field_3d.py).
- **`n_sub` = ceil(outer_dt / cfl_dt).** Typically 6–10 (natural units with default moduli → `n_sub ≈ 8`). Set once at `CoupledK4Cosserat.__init__` and held for the run.

### 4.4 Stability bounds

| Bound | Value (natural units) | Source | Engine enforcement |
|---|---|---|---|
| K4 CFL | `outer_dt ≤ ℓ_node / (c · √2)` | Diamond-lattice anisotropy | Hardcoded at K4 construction |
| Cosserat CFL | `cfl_dt ≤ 0.3 · dx / (c_max · √3)` | Phase I validation ([41_](41_cosserat_time_domain_validation.md)) | `cfl_dt` property computed each call |
| Thermal-V stability | `T < α / (4π) ≈ 5.8 × 10⁻⁴` (in m_e c² units; equivalently T < 3.44 MK in SI) | [47_ §2.2](47_thermal_lattice_noise.md) — beyond this, thermal σ_V exceeds V_SNAP and vacuum self-ruptures | `initialize_thermal(thermalize_V=True)` warns but does not clip; default `thermalize_V=False` |
| Autoresonant ω floor | `ω(t) ≥ ε_floor · ω_0` (ε_floor = 1e-3) | Prevents ω → 0 singularity in `AutoresonantCWSource` | Hardcoded at [vacuum_engine.py:529](../../src/ave/topological/vacuum_engine.py#L529) |

### 4.5 Numerical precision

- **Float64 throughout.** No float32 anywhere. Enforced via `jax.config.update('jax_enable_x64', True)` at engine import.
- **Guard constants.** See [constants.py:331–333](../../src/ave/core/constants.py#L331): `EPS_NUMERICAL = 1e-12` (impedance / reflection guards), `EPS_CLIP = 1e-15` (saturation-kernel radicand clip), `EPS_DIVZERO = 1e-30` (hard floor for denominators that could reach zero).
- **JAX autodiff.** Energy gradients use `jax.value_and_grad` on the energy functional; JIT-compiled for speed. Finite-difference cross-check at 1e-5 rtol in the saturation-active regime (test `test_saturated_gradient_matches_finite_difference_under_activation`).

### 4.6 Boundary conditions

- **Dirichlet PML absorption** at the 6 faces, `pml` cells deep. Attenuation is quadratic in depth.
- **Non-wrapping (open) boundary**: the K4 connect step severs bonds that would wrap across the torus; this prevents periodic ringing when sources are placed close to a face.
- **Cosserat `mask_alive`** excludes PML cells from the Cosserat dynamics so that u/ω stays identically zero there.

---

## 5. State inventory

Every state variable held by the running engine. Shapes assume an `N × N × N` lattice. All arrays are float64.

### 5.1 K4 photon sector — `K4Lattice3D` (owned by `_coupled.k4`)

| Symbol | Variable | Shape | Units (natural) | Default init | Source |
|---|---|---|---|---|---|
| V_inc[n, p] | Incident port voltage | (N, N, N, 4) | V_SNAP | 0 (cold) or MB (thermal, if `thermalize_V=True`) | [k4_tlm.py:118](../../src/ave/core/k4_tlm.py#L118) |
| V_ref[n, p] | Reflected port voltage | (N, N, N, 4) | V_SNAP | 0 always | [k4_tlm.py:119](../../src/ave/core/k4_tlm.py#L119) |
| z_local_field | Local impedance ratio Z_eff/Z_0 | (N, N, N) | dimensionless | 1.0 | [k4_tlm.py:196–221](../../src/ave/core/k4_tlm.py#L196) |
| pml_mask | Quadratic PML attenuation | (N, N, N, 1) | dimensionless ∈ [0,1] | 1 in interior, rolloff at PML | [k4_tlm.py PML](../../src/ave/core/k4_tlm.py) |
| mask_A | A-sublattice active mask | (N, N, N) bool | — | all-even coords True | [k4_tlm.py:157](../../src/ave/core/k4_tlm.py#L157) |
| mask_B | B-sublattice active mask | (N, N, N) bool | — | all-odd coords True | [k4_tlm.py:158](../../src/ave/core/k4_tlm.py#L158) |
| mask_active | `mask_A | mask_B` | (N, N, N) bool | — | derived | [k4_tlm.py](../../src/ave/core/k4_tlm.py) |
| timestep | K4 step counter | scalar int | — | 0 | [k4_tlm.py](../../src/ave/core/k4_tlm.py) |
| Phi_link[n, p] | Magnetic flux linkage on directed A→B bond (Stage 6 Phase 3, commit `3a599ca`) | (N, N, N, 4) | V_SNAP · τ_node | 0 always | [k4_tlm.py](../../src/ave/core/k4_tlm.py) — stored on A-sites only (B's copy derived by port-shift; avoids double-counting). Updated in `_connect_all` via `V_avg = ½(V_ref_A + V_ref_B_shifted); Phi_link += V_avg·dt`. `reset_phi_link()` zeroes the field. |

### 5.2 Cosserat sector — `CosseratField3D` (owned by `_coupled.cos`)

| Symbol | Variable | Shape | Units (natural) | Default init | Source |
|---|---|---|---|---|---|
| u(r) | Translational displacement | (N, N, N, 3) | ℓ_node | 0 (cold) or MB σ_u (thermal) | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |
| ω(r) | Microrotation | (N, N, N, 3) | rad | 0 (cold) or MB σ_ω (thermal) | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |
| u̇(r) | Translational velocity | (N, N, N, 3) | ℓ_node / τ_node | 0 (cold) or MB σ_u̇ (thermal) | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |
| ω̇(r) | Angular velocity | (N, N, N, 3) | rad / τ_node | 0 (cold) or MB σ_ω̇ (thermal) | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |
| mask_alive | Cosserat active mask (excludes PML) | (N, N, N) bool | — | interior only | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |
| time | Cosserat internal time | scalar | τ_node | 0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |

### 5.3 Coupled engine — `CoupledK4Cosserat` (owned by `VacuumEngine3D._coupled`)

| Symbol | Variable | Shape | Units | Default | Source |
|---|---|---|---|---|---|
| time | Global coupled time | scalar | τ_node | 0.0 | [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) |
| V_SNAP | Rupture voltage reference | scalar | — | 1.0 (natural) | [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) |
| _n_sub | Cosserat sub-steps per outer_dt | scalar int | — | 6–10 (derived from cfl_dt) | [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) |
| _dt_sub | Cosserat sub-step size | scalar | τ_node | outer_dt / n_sub | [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) |

### 5.4 `VacuumEngine3D` facade state

| Variable | Shape | Units | Default | Source |
|---|---|---|---|---|
| time | scalar | τ_node | 0.0 | [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758) |
| step_count | scalar int | — | 0 | [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758) |
| coupling_kappa | scalar | — | 1.0 | [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758) |
| amplitude_convention | str | — | "V_SNAP" | [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758) |
| _sources | list[Source] | — | [] | [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758) |
| _observers | list[Observer] | — | [] | [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758) |

### 5.5 Source-owned state (accumulated or transient)

| Source | Variable | Purpose |
|---|---|---|
| PulsedSource / CWSource | `cumulative_energy_injected` | Running total of injected energy (float) |
| PulsedSource / CWSource | `_port_w` | T₂-projected forward port weights (cached, 4,) |
| PulsedSource / CWSource | `_yz_profile` | Gaussian transverse envelope (cached, (ny, nz)) |
| AutoresonantCWSource | `_omega_current` | PLL-shifted instantaneous frequency |
| AutoresonantCWSource | `_accumulated_phase` | Phase accumulator (prevents discontinuity during ω shifts) |
| AutoresonantCWSource | `_omega_history` | list[float] — ω(t) for post-run diagnostics |
| AutoresonantCWSource | `_probe_A_sq_history` | list[float] — A²_probe(t) for post-run diagnostics |

### 5.6 Observer-owned state (history buffers)

Each observer holds `history: list[dict]`. Cadence-filtered: entry appended only on steps where `step_count % cadence == 0`. Schema of each entry is in §8.

**Queued state additions** (not yet in code; see §13):
- `Phi_link[edge_id]` — flux linkage per directed A→B bond. Stage 6 Phase 3.
- `Omega_node[nx, ny, nz]` — per-node Duffing-softened rotational resonance. Stage 6 Phase 2.
- `A²_μ[nx, ny, nz]`, `A²_ε[nx, ny, nz]` — split magnetic/electric saturation scalars. Stage 6 Phase 4.

---

## 6. Parameter datasheet

ICD-style table. "Source" column cites the authoritative origin (axiom / derivation / measurement / convention). "Credibility" per NASA-HDBK-7009 scheme. "Normalization" flags where V_SNAP vs V_yield matters.

### 6.1 Physical constants

| Symbol | Description | Value (SI) | Value (natural) | Source | Credibility |
|---|---|---|---|---|---|
| `α` | Fine-structure constant (CODATA) | 7.2973525693 × 10⁻³ | same | [constants.py:56](../../src/ave/core/constants.py#L56) | Pinned (CODATA 2018) |
| `α_cold⁻¹` | AVE-derived cold α⁻¹ asymptote | ≈ 137.0363038 | — | [constants.py:106](../../src/ave/core/constants.py#L106); [manuscript vol_1 ch08](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) | Derived |
| `c` | Speed of light | 299 792 458 m/s | 1 | [constants.py:34](../../src/ave/core/constants.py#L34) | Pinned (2019 SI defn) |
| `ℏ` | Reduced Planck | 1.0546 × 10⁻³⁴ J·s | 1 | [constants.py:38](../../src/ave/core/constants.py#L38) | Pinned |
| `m_e` | Electron mass | 9.1094 × 10⁻³¹ kg | 1 | [constants.py:52](../../src/ave/core/constants.py#L52) | Pinned (CODATA; Input 1 of 3) |
| `e` | Elementary charge | 1.6022 × 10⁻¹⁹ C | — | [constants.py:39](../../src/ave/core/constants.py#L39) | Pinned (2019 SI defn) |
| `ℓ_node = ℏ / (m_e c)` | Lattice pitch | 3.8616 × 10⁻¹³ m | 1 | [constants.py:136](../../src/ave/core/constants.py#L136) | Derived |
| `Z_0 = √(μ_0 / ε_0)` | Characteristic impedance | 376.73 Ω | — | [constants.py:37](../../src/ave/core/constants.py#L37) | Derived |
| `V_SNAP = m_e c² / e` | Rupture voltage | 511.0 × 10³ V | 1 | [constants.py:266](../../src/ave/core/constants.py#L266) | Derived (Axiom 4 + Axiom 2) |
| `V_yield = √α · V_SNAP` | Regime II onset | 43.65 × 10³ V | √α ≈ 0.0854 | [constants.py:275](../../src/ave/core/constants.py#L275) | Derived |
| `E_yield` | Field strength at V_yield | 1.13 × 10¹⁷ V/m | V_yield / ℓ_node | [constants.py:286](../../src/ave/core/constants.py#L286) | Derived |
| `T_EM` | 1D EM string tension | 0.212 N | 1 | [constants.py:263](../../src/ave/core/constants.py#L263) | Derived |
| `ξ_topo = e / ℓ_node` | Topo-kinematic factor | 4.149 × 10⁻⁷ C/m | — | [constants.py:148](../../src/ave/core/constants.py#L148) | Derived (Axiom 2) |

### 6.2 Regime boundaries (Axiom 4)

| Symbol | Description | Value in `A²_SNAP` units | Value in `A²_yield` units | Source |
|---|---|---|---|---|
| `A²_I/II` | Linear → E–H transition boundary | 2α ≈ 0.01459 | 2 | [constants.py R_I](../../src/ave/core/constants.py#L295), [vacuum_engine.py:151](../../src/ave/topological/vacuum_engine.py#L151) |
| `A²_II/III` | E–H transition → saturation | 3/4 = 0.75 | 3/(4α) ≈ 102.8 | [constants.py R_II](../../src/ave/core/constants.py#L296), [vacuum_engine.py:152](../../src/ave/topological/vacuum_engine.py#L152) |
| `A²_III/IV` | Saturation → rupture (Schwinger) | 1 | 1/α ≈ 137.04 | [constants.py R_III](../../src/ave/core/constants.py#L297), [vacuum_engine.py:153](../../src/ave/topological/vacuum_engine.py#L153) |

**Normalization note.** The engine internally uses `A²_SNAP` (i.e., `A² = V² / V_SNAP²`). The Axiom-4 varactor divergence is at `V = V_yield`, which is `A²_SNAP = α ≈ 0.0073`. Reports quoting "A² = 1" refer to the Schwinger rupture at 511 kV SI, not the yield onset at 43.65 kV. This distinction is load-bearing for Stage 6 Phase 2+ (see [54_ §5](54_pair_production_axiom_derivation.md) and §12 below).

### 6.3 Cosserat constitutive moduli

| Symbol | Description | Default (natural) | Source | Credibility |
|---|---|---|---|---|
| `ρ` | Translational mass density | 1.0 | [vacuum_engine.py EngineConfig:741](../../src/ave/topological/vacuum_engine.py#L741), S-gate S4=A | Empirical (placeholder) |
| `I_ω` | Rotational inertia | 1.0 | [vacuum_engine.py EngineConfig:741](../../src/ave/topological/vacuum_engine.py#L741), S-gate S4=A | Empirical (placeholder) |
| `G` | Shear modulus | 1.0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Calibrated (Axiom 2 pinning, doc 02_ §9) |
| `G_c` | Micropolar shear modulus | 1.0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Calibrated |
| `γ` | Curvature stiffness | 1.0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Calibrated (`G_c = γ`, doc 04_) |
| `ε_yield` | Strain yield threshold | 1.0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Empirical (placeholder) |
| `ω_yield` | Curvature yield threshold | π | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Empirical (placeholder) |
| `k_op10` | Op10 coupling strength | 1.0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Pending (continuum form not derived; queue item 17) |
| `k_refl` | Reflection coupling strength | 1.0 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Empirical (placeholder) |
| `k_hopf` | Hopf-invariant coupling | π/3 | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Calibrated (Q_H matches at Q=6) |

### 6.4 Coupling & source parameters

| Symbol | Description | Default | Source | Credibility |
|---|---|---|---|---|
| `κ` (coupling_kappa) | S1-D prefactor on (V²/V_SNAP²)·W_refl | 1.0 | [vacuum_engine.py EngineConfig:741](../../src/ave/topological/vacuum_engine.py#L741) | Derived (S-gate S1=D, 0 new params) |
| `K_drift` | Autoresonant PLL gain | 0.5 | [vacuum_engine.py AutoresonantCWSource:529](../../src/ave/topological/vacuum_engine.py#L529) | Empirical (Stage 4c tuning sweep) |
| `probe_x_offset` | Probe-point downstream cells for PLL feedback | 4 | [vacuum_engine.py AutoresonantCWSource:529](../../src/ave/topological/vacuum_engine.py#L529) | Empirical |
| `ε_floor` | PLL ω lower clip | 1e-3 | [vacuum_engine.py AutoresonantCWSource:529](../../src/ave/topological/vacuum_engine.py#L529) | Empirical (stability guard) |
| `δ_strain` (CMB) | Thermal α correction | 2.225 × 10⁻⁶ | [constants.py:124](../../src/ave/core/constants.py#L124) | Derived |
| `K_0` (η_vac proxy) | AVE-PONDER mutual inductance | 0.207973 | AVE-PONDER/generate_ponder_01_spice_netlist.py:90; [46_ §9](46_vacuum_engine_scope.md) | Calibrated (not a user knob, per C2) |

### 6.4a Engine config flags (Round 6 — opt-in behavior switches)

All flags default `False` and live on `EngineConfig` + `CoupledK4Cosserat` constructor + `K4Lattice3D` constructor (where applicable). Backward-compat: legacy default behavior preserved with all flags off.

| Flag | Default | Purpose | Status / Authority |
|---|---|---|---|
| `use_asymmetric_saturation` | `True` | Phase 4 asymmetric (S_μ, S_ε) saturation kernel; legacy `False` recovers single-S form | Phase 4, [doc 54_ §6](54_pair_production_axiom_derivation.md), commit `a5bd1da` |
| `use_memristive_saturation` | `False` | K4-side dynamical S(t) per `dS/dt = (S_eq − S)/τ_relax` with τ_relax = ℓ_node/c (opt-in for Phase 5e cool-from-above experiments) | Phase 5.6, [doc 59_](59_memristive_yield_crossing_derivation.md), commit `49917ff` |
| `use_lagrangian_emf_coupling` | `False` | Path-1 EMF: adds `(2V·W_refl)/(C·V_SNAP²)` to bond Φ_link integration as voltage source. **KNOWN WRONG-DIRECTION** under A28 reframing — keeping enabled in HEAD as opt-in for now; cleanup follow-up. | F17-H path-1 (RETRACTED), [doc 67_ §3-§14](67_lc_coupling_reciprocity_audit.md), commit `3d7fae4` |
| `disable_cosserat_lc_force` | `False` | **A28 fix.** When `True`, suppresses `_compute_coupling_force_on_cosserat` returning zero arrays — removes the redundant ∂L_c/∂(u,ω) force that double-counted with Op14 z_local modulation. Legacy default preserves the redundant force for backward-compat. | A28, [doc 67_ §15-§16](67_lc_coupling_reciprocity_audit.md), commit `05b130f` |
| `enable_cosserat_self_terms` | `False` | Re-enables Cosserat self-Lagrangian terms `k_op10`, `k_refl`, `k_hopf` (currently disabled at init lines 231-233 because the comment said *"reflection is carried by the coupling term"* — which under A28 is no longer the case). When ON together with `disable_cosserat_lc_force=True`, **auto-suppresses `k_refl=0`** (the same redundant reflection force at Cosserat-self level) while keeping `k_op10=1` and `k_hopf=π/3` (different physics). | A28 self-terms re-enable, [doc 67_ §16+](67_lc_coupling_reciprocity_audit.md), commit `ff15c4b` |

**Combined Round 6 fix preset:** `disable_cosserat_lc_force=True` AND `enable_cosserat_self_terms=True` is the configuration under which Path B at N=80 first formed a (2,3) bound state in Stage 6. Six prior failure modes (Path A / Path B / Path C / F17-G / F17-I / path-1 EMF) all explained by the legacy-default redundant-force bug. See §13.5b for empirical results and §17 A28 for the structural derivation.

### 6.5 Numerical / computational parameters

| Parameter | Default | Range tested | Source |
|---|---|---|---|
| `N` (lattice side) | (required) | 32, 40, 48, 64 | — |
| `pml` (PML depth) | 6 | 4–8 | [EngineConfig:741](../../src/ave/topological/vacuum_engine.py#L741) |
| `outer_dt` | `1/√2 ≈ 0.7071` | Fixed | [k4_tlm.py](../../src/ave/core/k4_tlm.py) |
| `cfl_safety` (Cosserat) | 0.3 | — | [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) |
| `n_sub` | Derived (≈ 6–10) | — | [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) |
| `temperature` (m_e c² units) | 0.0 | 0.0, 0.1 (tested); thermalize_V=True requires T < 5.8e-4 | [EngineConfig:741](../../src/ave/topological/vacuum_engine.py#L741) |
| `thermalize_V` | False | — | [initialize_thermal](../../src/ave/topological/vacuum_engine.py#L758) |
| `EPS_NUMERICAL` | 1e-12 | Fixed | [constants.py:331](../../src/ave/core/constants.py#L331) |
| `EPS_CLIP` | 1e-15 | Fixed | [constants.py:332](../../src/ave/core/constants.py#L332) |
| `EPS_DIVZERO` | 1e-30 | Fixed | [constants.py:333](../../src/ave/core/constants.py#L333) |

---

## 7. Sources API

All Sources subclass `Source` ([vacuum_engine.py:180](../../src/ave/topological/vacuum_engine.py#L180)) and implement `apply(engine, t) -> None`, which modifies `engine.k4.V_inc` in place.

### 7.1 `PulsedSource`

Gaussian-enveloped sinusoidal pulse injected on a single YZ plane. Use for transient-photon propagation tests (Phase A/B/C of doc 40_).

```python
PulsedSource(
    x0: int,
    direction: tuple[float, float, float],
    amplitude: float,               # User convention
    omega: float,                   # Carrier (natural units)
    sigma_yz: float,                # Transverse envelope width (cells)
    t_center: float,                # Pulse center time
    t_sigma: float,                 # Pulse standard deviation
    y_c: float | None = None,       # Beam center y (default: grid center)
    z_c: float | None = None,
)
```

**Injection formula:** at each active site on x = x0,
```
V_inc[x0, y, z, p] += amp · w_T2[p] · g_yz(y, z) · exp(−(t−t_center)²/(2 t_sigma²)) · sin(ω(t − t_center))
```
where `w_T2[p]` is the T₂-projected forward port weight for `direction` ([vacuum_engine.py _forward_t2_port_weights:125](../../src/ave/topological/vacuum_engine.py#L125)), and `g_yz` is a Gaussian envelope with width `sigma_yz`.

Tracks `cumulative_energy_injected` for `EnergyBudgetObserver` use.

Defined at [vacuum_engine.py:189](../../src/ave/topological/vacuum_engine.py#L189).

### 7.2 `CWSource`

Continuous-wave plane source with piecewise ramp / sustain / decay envelope. Phase III-B v1 default source.

```python
CWSource(
    x0: int,
    direction: tuple[float, float, float],
    amplitude: float,
    omega: float,
    sigma_yz: float,
    t_ramp: float,
    t_sustain: float,
    t_decay: float | None = None,
    y_c: float | None = None,
    z_c: float | None = None,
)
```

**Envelope:**
```
env(t) = 0                                      if t < 0
env(t) = (t / t_ramp)                           if 0 ≤ t < t_ramp
env(t) = 1                                      if t_ramp ≤ t < t_ramp + t_sustain
env(t) = 1 − (t − t_ramp − t_sustain)/t_decay   if within decay
env(t) = 0                                      otherwise
```

**Injection formula:** same as PulsedSource but with `env(t)` in place of the Gaussian time window.

Defined at [vacuum_engine.py:253](../../src/ave/topological/vacuum_engine.py#L253).

### 7.3 `AutoresonantCWSource` (Stage 4c)

PLL-tracked CW with instantaneous frequency shifting per Duffing-like resonance detuning. Novel to AVE-Core — no sibling reference implementation. Phase III-B v2 default.

```python
AutoresonantCWSource(
    x0: int,
    direction: tuple[float, float, float],
    amplitude: float,
    omega: float,                   # Nominal (unshifted) frequency ω_0
    sigma_yz: float,
    t_ramp: float,
    t_sustain: float,
    t_decay: float | None = None,
    y_c: float | None = None,
    z_c: float | None = None,
    K_drift: float = 0.5,           # PLL gain
    probe_x_offset: int = 4,        # Cells downstream of x0 to probe A²
)
```

Defined at [vacuum_engine.py:529](../../src/ave/topological/vacuum_engine.py#L529).

**Per-step frequency shift:**
```
A²_probe(t) = mean_over_yz(V²_inc(x0 + probe_x_offset, y, z, *) / V_SNAP²)
ω(t) = ω_0 · max(ε_floor, 1 − K_drift · A²_probe(t))
φ(t) += ω(t) · dt
V_inc(x0) += amp · w_T2 · g_yz · env(t) · sin(φ(t))
```

Phase is accumulated to prevent discontinuities when ω shifts. Probes downstream so saturation in the interaction region (where counter-propagating sources collide) is sensed, not at the source itself.

**Rationale:** the AVE-Propulsion Ch 5 mechanism predicts a Duffing softening of the lattice's local resonance under drive; `AutoresonantCWSource` implements the drive-side PLL that would lock with that softened resonance. Per [54_ §4](54_pair_production_axiom_derivation.md), the lattice side (per-node `Ω_node`) is not yet tracked — the PLL currently matches a probe-point A² proxy, not the actual node resonance. This is the structural gap that Stage 6 Phase 2 closes.

### 7.4 Usage pattern

```python
engine.add_source(AutoresonantCWSource(
    x0=pml + 4, direction=(1, 0, 0),
    amplitude=0.5, omega=2*np.pi/3.5,
    sigma_yz=3.0,
    t_ramp=20, t_sustain=260,
    K_drift=0.5,
))
engine.add_source(AutoresonantCWSource(
    x0=N − pml − 5, direction=(-1, 0, 0),
    amplitude=0.5, omega=2*np.pi/3.5,
    sigma_yz=3.0,
    t_ramp=20, t_sustain=260,
    K_drift=0.5,
))
```

Two counter-aimed sources collide at x = N/2; this is the Phase III-B canonical setup.

---

## 8. Observers API

All Observers subclass `Observer` ([vacuum_engine.py:337](../../src/ave/topological/vacuum_engine.py#L337)) and implement `_capture(engine) -> Any`. Cadence is enforced by the base `record()` method; histories accumulate in `self.history`.

### 8.1 `ScalarObserver`

User-supplied scalar function wrapper.
```python
ScalarObserver(name: str, fn: Callable[[VacuumEngine3D], float], cadence: int = 1)
```
Recorded: `{"t": engine.time, "value": float(fn(engine))}`

Defined at [vacuum_engine.py:354](../../src/ave/topological/vacuum_engine.py#L354).

### 8.2 `RegimeClassifierObserver`

Counts active cells in each Axiom-4 regime per step.
```python
RegimeClassifierObserver(cadence: int = 1)
```
Recorded schema:
```python
{
  "t": float,
  "rg_I":        int,   # cells in Regime I
  "rg_II":       int,   # cells in Regime II
  "rg_III":      int,   # cells in Regime III
  "rupture":     int,   # cells in Regime IV
  "max_A2_k4":   float, # peak A²_K4 across active cells
  "max_A2_cos":  float, # peak A²_Cosserat
  "max_A2_total":float, # peak A²_total = A²_K4 + A²_Cos
}
```
Defined at [vacuum_engine.py:366](../../src/ave/topological/vacuum_engine.py#L366).

### 8.3 `NodeResonanceObserver` (Stage 6 Phase 2 — landed 719f3ec)

**Status:** committed to `research/l3-electron-soliton` (commit 719f3ec). Observer arithmetic is pinned by 13 smoke-tier tests ([test_phase2_node_resonance.py](../../src/tests/test_phase2_node_resonance.py)). Driver script [node_resonance_validation.py](../../src/scripts/vol_1_foundations/node_resonance_validation.py) exercises integration on v2 headline.

**P_phase2_omega reframing (honest-framing note from commit message):** "The observer IS the closed form applied to engine state, so asking 'does observer match closed form?' is circular." Scope was narrowed: the tests pin arithmetic; the driver validates integration (no NaN, ordering invariants, simulation evolves); real physics falsification of the varactor form on the coupled K4⊗Cosserat sector requires a probe + FFT experiment deferred to a later phase. See §17 findings A6 for the load-bearing implication.

Read-only observer of per-node LC-tank resonance softening, derived from the Axiom-4 Vacuum Varactor per [54_ §4](54_pair_production_axiom_derivation.md) and [Vol 4 Ch 1:127–142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L127):
```
A²_yield_total = A²_K4_SNAP / α + A²_Cos_yield                (Pythagorean sum)
S = √(1 − A²_yield_total)                                    (clipped to [0, 1))
Ω_node(r, t) / ω_0 = S^(1/2) = (1 − A²_yield_total)^(1/4)
```
The K4 normalization conversion (`A²_SNAP / α → A²_yield`) is the resolution of the V_SNAP vs V_yield confusion flagged in [45_ §3.1](45_lattice_impedance_first_principles.md); see §6.2 and §12.2.

```python
NodeResonanceObserver(cadence: int = 1)
```
Recorded schema:
```python
{
  "t":                 float,
  "omega_ratio_max":   float,  # max_r Ω_node(r) / ω_0
  "omega_ratio_mean":  float,
  "omega_ratio_min":   float,
  "A2_yield_max":      float,  # max A²_yield across active sites
  "A2_yield_mean":     float,
  "n_saturated":       int,    # count of sites with A²_yield ≥ 1
}
```
Defined at [vacuum_engine.py:391](../../src/ave/topological/vacuum_engine.py#L391).

### 8.4 `TopologyObserver`

Hopf charge + soliton centroid detection. Supports multi-threshold sensitivity studies (added Stage 5 Phase A per [52_](52_h1_threshold_sweep.md)).
```python
TopologyObserver(
    cadence: int = 5,
    threshold_frac: float | None = None,        # Primary threshold (default 0.3)
    threshold_fracs: list[float] | None = None, # Sensitivity sweep (adds 'per_threshold' key)
)
```
Recorded schema:
```python
{
  "t": float,
  "Q_hopf": float,                       # Hopf invariant (continuous)
  "n_centroids": int,                    # At primary threshold
  "centroids": [
    {"center": (cx, cy, cz),
     "peak_mag_sq": float,
     "n_cells": int},
    ...
  ],
  "per_threshold": {                     # Only if threshold_fracs given
    frac: {"n_centroids": int, "centroids": [...]},
    ...
  } | None,
}
```
Defined at [vacuum_engine.py:465](../../src/ave/topological/vacuum_engine.py#L465). Centroid detection uses connected-component labeling on `|ω|² > threshold_frac · max(|ω|²)` with `min_cluster_size = 8`.

### 8.5 `EnergyBudgetObserver`

Partition of total Hamiltonian across K4 / Cosserat / coupling sectors.
```python
EnergyBudgetObserver(cadence: int = 1)
```
Recorded schema:
```python
{
  "t": float,
  "E_K4":         float,   # K4 electromagnetic energy
  "E_cos":        float,   # Cosserat potential energy
  "T_cos":        float,   # Cosserat kinetic energy ½ρ|u̇|² + ½I_ω|ω̇|²
  "E_coupling":   float,   # ∫ (V²/V_SNAP²)·W_refl dx³
  "H_total":      float,   # Sum
}
```
Defined at [vacuum_engine.py:515](../../src/ave/topological/vacuum_engine.py#L515). Used for Hamiltonian-drift diagnostics in Phase II (|ΔH/H| < 1% pass criterion for Verlet symplectic).

### 8.5a `BondObserver` (Stage 6 Phase 3 — commit `3a599ca` on HEAD)

> **r6 R4 note:** `_compute_A2_yield` was patched in the working tree to remove the `/α` division — the method now returns direct Pythagorean sum `A²_K4 + A²_Cos` (both canonical r² at subatomic scale per §17.0 R4 adjudication). The "_yield" suffix in the method name is preserved for backward-compatibility but is semantically equivalent to canonical r² under the subatomic-override convention. The patch is pending commit.

Read-only observer of per-bond magnetic flux linkage `Phi_link`. Reports the engine-state variable that [54_ §3](54_pair_production_axiom_derivation.md) identifies as the channel carrying (2,3) torus-knot winding between saturated A-B endpoints.

```python
BondObserver(cadence: int = 1, saturation_frac: float = 0.5)
```

Recorded schema:
```python
{
  "t": float,
  "phi_abs_max":                 float,   # max |Φ_link| across A-site bonds
  "phi_rms":                     float,   # √⟨Φ²⟩ across A-site bonds
  "phi_at_saturated_bonds_rms":  float,   # RMS Φ on bonds where BOTH endpoints A²_yield ≥ saturation_frac
  "phi_at_unsaturated_bonds_rms":float,   # RMS Φ on bonds with ≥1 unsaturated endpoint
  "n_saturated_bonds":           int,
  "n_unsaturated_bonds":         int,
}
```

**Saturation normalization:** uses A²_yield = A²_K4_SNAP/α + A²_cos — same convention as [NodeResonanceObserver](#83-noderesonanceobserver-stage-6-phase-2--landed-719f3ec). Default `saturation_frac = 0.5` means a bond is "saturated" when both endpoints have A²_yield ≥ 0.5 (half of yield saturation).

Defined at [vacuum_engine.py:391+BondObserver block](../../src/ave/topological/vacuum_engine.py#L391) (inserted at line 391 in the Phase 3 diff; exact line numbers may shift with Stage 6 continuation).

**Phase 3 driver finding** ([flux_tube_persistence.py](../../src/scripts/vol_1_foundations/flux_tube_persistence.py)): saturated-bond and unsaturated-bond Φ_link half-lives came out identical (≈ 3.64 Compton periods each) at amp = 0.5 V_SNAP. This is *expected* under current single-S (symmetric) saturation — Γ = -1 flux-tube confinement requires the asymmetric μ/ε split that Phase 4 introduces. P_phase3_flux_tube pass/fail adjudication is deferred until after Phase 4 lands (noted in `predictions.yaml` P_phase3 entry).

### 8.6 `DarkWakeObserver` (Stage 4b)

Longitudinal shear strain `τ_zx ∝ Z_local · ∂/∂x [V²/V_SNAP²]` — the lattice back-EMF signature. Formula ported from [AVE-Propulsion/simulate_warp_metric_tensors.py:75–95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py). Uses K4 tetrahedral gradient (NOT `np.gradient`, because active sites alternate sublattices).
```python
DarkWakeObserver(cadence: int = 5, propagation_axis: int = 0)   # 0=x, 1=y, 2=z
```
Recorded schema:
```python
{
  "t": float,
  "tau_zx_slab":  ndarray,   # 1-D along propagation axis, averaged transverse
  "max_tau_zx":   float,     # Peak |τ_zx| excluding PML
  "wake_peak_x":  int,       # Argmax position, or -1 if below threshold
}
```
Defined at [vacuum_engine.py:647](../../src/ave/topological/vacuum_engine.py#L647). Pearson `r(V², τ_zx) = 0.994` at Stage 4b validation ([49_+50_](50_autoresonant_pair_creation.md)).

### 8.7 Attachment pattern

```python
engine.add_observer(RegimeClassifierObserver(cadence=1))
engine.add_observer(TopologyObserver(cadence=5, threshold_fracs=[0.1, 0.3, 0.5, 0.7]))
engine.add_observer(EnergyBudgetObserver(cadence=1))
engine.add_observer(DarkWakeObserver(cadence=5, propagation_axis=0))
...
engine.run(n_steps=300)
hist = engine.history()   # dict keyed by observer class name
```

---

## 9. Initialization procedures

### 9.1 Cold vacuum (T = 0) — C1 deterministic

Per C-finding C1 ([46_ §2.1](46_vacuum_engine_scope.md)), at T = 0 the AVE vacuum is deterministic — no sub-ℓ_node fluctuations exist. `VacuumEngine3D.__init__` calls `initialize_thermal(0.0)` by default, which sets:

```
V_inc = 0,   V_ref = 0
u = 0,       u̇ = 0
ω = 0,       ω̇ = 0
```

Every bit exactly. The K4 `z_local_field` remains at its default 1.0. The Cosserat sector has zero energy.

**C1 validated** across v1 (8 configs) and v2 (4 configs) — `max A²_cos = 0` exactly at T=0 in all runs. See [50_ §2.2](50_autoresonant_pair_creation.md).

### 9.2 Thermal (T > 0) — classical Maxwell-Boltzmann

`initialize_thermal(T: float, seed: int | None = None, thermalize_V: bool = False)`. T is in natural m_e c² units (so T = 1 means kT = electron rest energy).

Per doc 47_ derivations (classical equipartition):

```
σ_ω         = √(T · mode_int / (4π² I_ω))        where mode_int = π − 2 arctan(π/2) ≈ 1.14
σ_ω̇         = √(T / I_ω)
σ_u         = √(T / (2π ρ))
σ_u̇         = √(T / ρ)
σ_V_per_port = √(4π · T / α) · V_SNAP            ONLY if thermalize_V=True
```

Cosserat fields are always thermalized when T > 0. V_inc is thermalized only if explicitly requested.

Defined at [vacuum_engine.py initialize_thermal:811](../../src/ave/topological/vacuum_engine.py#L811).

### 9.3 Thermal-V stability bound (AVE Schwinger temperature)

For `thermalize_V=True`, stability requires:
```
T < α / (4π) ≈ 5.8 × 10⁻⁴       (m_e c² units)
  ≈ 3.44 × 10⁶ K                (SI)
```

Above this, σ_V per port exceeds V_SNAP and the thermal V field spontaneously ruptures the vacuum — the simulation is numerically unstable (and physically correct — the early universe at T > 10⁷ K was literally above the Schwinger limit). Per [47_ §2.2](47_thermal_lattice_noise.md).

Default `thermalize_V=False` leaves V_inc = 0 and thermalizes only the Cosserat (u, ω) sector — the "cold EM vacuum + warm matter precursor" regime valid below the AVE Schwinger temperature. Phase III-B v1 and v2 both used `thermalize_V=False` at T = 0.1.

### 9.4 Characteristic values at canonical temperatures

From [47_](47_thermal_lattice_noise.md):

| T (SI) | T (m_e c²) | σ_ω [rad] | σ_u [ℓ_node] | σ_V (if thermalized) [V_SNAP] |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 2.7 K (CMB) | 4.6 × 10⁻¹⁰ | 3.6 × 10⁻⁶ | 8.5 × 10⁻⁶ | 3.96 × 10⁻⁴ |
| 10⁶ K | 1.96 × 10⁻⁴ | 0.014 | 5.6 × 10⁻³ | ≈ 0.3 (approaching instability) |
| 10⁸ K | 1.96 × 10⁻² | 0.055 | 0.056 | ≈ 5.4 (ruptures if `thermalize_V`) |
| 10⁹ K | 0.196 | 0.44 | 0.18 | rupture regime |

Phase III-B canonical: T = 0.1 in natural units = 5.93 × 10⁸ K in SI. Cosserat-only thermalization is stable at this T; thermal V would rupture (as documented).

### 9.5 RNG seed convention

`initialize_thermal(T, seed=None, ...)` accepts a seed. When `None` (default), uses NumPy's `default_rng()` with no explicit seed (reproducibility requires capturing the RNG state externally). Phase III-B runs have not yet pinned the seed; run-to-run variance in `max A²_cos` between v2 (1.009) and v3 H1 rerun (0.877) was attributed to RNG drift ([52_ §3.3](52_h1_threshold_sweep.md)). Pinning the seed is a Stage 5 queued improvement.

---

## 10. Validation matrix (V&V)

Each row is one validation test. `V` = verification (numerics match expected form); `P` = physics validation (result matches a pre-registered AVE prediction). Status `✓` = passed; `✗` = failed; `—` = not yet run.

### 10.1 Phase I — Cosserat time-domain ([doc 41_](41_cosserat_time_domain_validation.md))

| Test ID | Subsystem | Criterion | Measurement | V | P | Status | Credibility | Evidence |
|---|---|---|---|---|---|---|---|---|
| T1a | Gapless wave | `v_g = c_R = 1` (natural units) | 0.858 (14 % lattice dispersion) | ✓ | — | ✓ | Derived | [41_ §T1a](41_cosserat_time_domain_validation.md) |
| T1b | Gapped wave | `v_g(k)` matches theory | 0.169 vs theory 0.253 (34 % error, stiff near gap) | ✓ | — | ✓ | Derived | [41_ §T1b](41_cosserat_time_domain_validation.md) |
| T2 | Mass gap | Period = 2π/m = π for m² = 4 | 3.131 vs theory 3.142 (0.35 % error) | ✓ | ✓ | ✓ | Derived | [41_ §T2](41_cosserat_time_domain_validation.md) |
| T3 | Symplectic H drift | `|ΔH/H|_max ≤ 1 %` | ≤ 0.8 % over many periods | ✓ | — | ✓ | Derived | [41_ §T3](41_cosserat_time_domain_validation.md) |

### 10.2 Phase II — Coupled K4⊗Cosserat ([doc 42_](42_coupled_simulator_validation.md))

| Test ID | Subsystem | Criterion | Measurement | V | P | Status | Credibility | Evidence |
|---|---|---|---|---|---|---|---|---|
| V1 | K4 isolation | Coupling off when Cosserat at rest | `max|E_coupling| = 0` exactly | ✓ | ✓ | ✓ | Derived | [42_ §V1](42_coupled_simulator_validation.md) |
| V2 | Cosserat isolation | Coupling off when V = 0; H drift Verlet-consistent | `|ΔH/H| = 0.8 %` (matches Phase I) | ✓ | ✓ | ✓ | Derived | [42_ §V2](42_coupled_simulator_validation.md) |
| V3 | Coupled interaction | Coupling activates; H bounded | `E_coupling = 2.3 × 10⁻⁸`; no blowup | ✓ | ✓ | ✓ | Derived | [42_ §V3](42_coupled_simulator_validation.md) |
| L1 | Q-flip aliasing | — | Measurement artifact flagged; not physics | — | — | Noted | Empirical | [42_ L1](42_coupled_simulator_validation.md) |

### 10.3 Phase III-B v1 — fixed-frequency σ(ω) ([doc 48_](48_pair_creation_frequency_sweep.md))

16 configs: 4 λ × 2 amp × 2 T. N = 48, pml = 6, 240 outer steps.

| Test ID | Prediction | Outcome | Status | Evidence |
|---|---|---|---|---|
| P_IIIb-α (cold determinism) | A²_cos = 0 exactly at T = 0 | Confirmed across 8 T=0 runs | ✓ | [48_ §3.1](48_pair_creation_frequency_sweep.md) |
| P_IIIb-β (amplitude scaling) | A²_cos ∝ amp² | Falsified: amp=0.5 produced higher A²_cos than amp=0.7 (budget partition) | ✗ | [48_ §3.2](48_pair_creation_frequency_sweep.md) |
| P_IIIb-γ (high-f cascade) | λ = 3.5 (high-f) > λ = 10 (low-f) | Not observed (peak at λ = 7) | ✗ | [48_ §3.3](48_pair_creation_frequency_sweep.md) |
| P_IIIb-δ (ω·τ = 1 knee) | Sharp knee at ω·τ_relax = 1 | Ambiguous: smooth peak at 0.9, not sharp | ~ | [48_ §3.4](48_pair_creation_frequency_sweep.md) |
| Pair creation | Localized centroids at threshold_frac = 0.7 | 0 centroids in all 16 configs | — (engine limit, see §11) | [48_ §4](48_pair_creation_frequency_sweep.md) |

Headline: σ(ω) peak at ω·τ_relax ≈ 0.9; `max A²_cos = 0.962` at (λ=7, amp=0.5, T=0.1).

### 10.4 Phase III-B v2 — autoresonant σ(ω) ([doc 50_](50_autoresonant_pair_creation.md))

8 configs: 4 λ × 2 T. N = 40, pml = 5, 300 outer steps. `AutoresonantCWSource` with K_drift = 0.5.

| Test ID | Prediction | Outcome | Status | Evidence |
|---|---|---|---|---|
| P_IIIb-v2-partial | Dark wake enhanced; no pair nucleation | **Confirmed** — σ(ω) shape changed (monotonic), A²_cos = 1.009 at ω·τ = 1.8, no centroids | ✓ | [50_ §2.3](50_autoresonant_pair_creation.md) |
| C1 reconfirmation | A²_cos = 0 at T = 0 under autoresonant drive | Confirmed | ✓ | [50_ §2.2](50_autoresonant_pair_creation.md) |
| Rupture boundary crossing | A²_cos reaches 1.0 | **A²_cos = 1.009** — first numerical instance in AVE-Core | ⚠ brittle (see below) | [50_ §2.3](50_autoresonant_pair_creation.md) |

> **2026-04-23 caveat (§10.12 seed-sweep verdict, expanded r6).** The 1.009 figure was a single-seed outcome. A 20-seed reproducibility sweep on the engine at the time (Phase 3 HEAD, `3a599ca`) returned `max A²_cos` distribution:
> - **Range: [0.7677, 0.9983]**
> - **Median: 0.8683**
> - **IQR: [0.8097, 0.9181]**
> - **0/20 seeds reached 1.009**; 2/20 within ±0.05 of the headline.
> - `max A²_K4 = 0.393` bit-identical across all 20 seeds (K4 sector deterministic; all variance is in the Cosserat thermal-RNG init).
> - Dark-wake `τ_zx = 0.1507` bit-identical across all 20 seeds (K4-deterministic diagnostic).
>
> Cause of non-reproduction: (a) Phase 2 / Phase 3 code perturbed the coupled trajectory, or (b) 1.009 was always a lucky tail outcome and doc 50_'s framing was over-confident. Doc 50_ r3 distribution-language rewrite has landed in working tree; bisection `719f3ec` vs `3a599ca` was launched 2026-04-23 (results pending) to discriminate. See §17 A17. The R4 adjudication (§17.0) explicitly decouples this distribution-regression question from the normalization-convention question.
| Dark-wake frequency scaling | τ_zx grows with ω | τ_zx grows ~4× from ω·τ = 0.9 to 1.8 | ✓ | [50_ §2.4](50_autoresonant_pair_creation.md) |

### 10.5 Stage 4b — Dark-wake observer validation ([doc 49_+50_](50_autoresonant_pair_creation.md))

| Test ID | Criterion | Measurement | Status | Evidence |
|---|---|---|---|---|
| DW-1 | Linear correlation τ_zx vs V² | Pearson r ≥ 0.9 | 0.994 | ✓ | [49_](49_dark_wake_bemf_foc_synthesis.md), [50_ §2.4](50_autoresonant_pair_creation.md) |
| DW-2 | Counter-propagating symmetry | τ_zx opposite sign for counter-aimed sources | Confirmed | ✓ | [49_](49_dark_wake_bemf_foc_synthesis.md) |

### 10.6 Stage 4c — Autoresonant PLL tuning

| Test ID | Criterion | Measurement | Status | Evidence |
|---|---|---|---|---|
| AR-1 | Stability across `K_drift ∈ [0, 2]` | No blowup; Hamiltonian bounded | Confirmed up to K_drift = 2.0 | ✓ | [50_](50_autoresonant_pair_creation.md), autoresonant_tuning.py |
| AR-2 | Monotonic A²_cos response with ω | Higher ω → higher A²_cos (within stable K_drift) | Confirmed | ✓ | [50_ §2](50_autoresonant_pair_creation.md) |

### 10.7 Stage 5 Phase A — H1 centroid threshold sensitivity ([doc 52_](52_h1_threshold_sweep.md))

| Test ID | Hypothesis | Outcome | Status | Evidence |
|---|---|---|---|---|
| H1 | Localized pairs exist below threshold_frac = 0.7 | **Falsified** — count explosion at low threshold = thermal noise granularity, not localized cores | ✗ | [52_ §3](52_h1_threshold_sweep.md) |
| H1-spatial | Low-threshold centroids cluster at collision plane x = N/2 | Not observed — σ_x ≈ N/4 (scatter); frac-within-N/4 = 49–55 % (near-uniform) | ✗ | [52_ §2.3](52_h1_threshold_sweep.md) |

### 10.8 Axiom-derivation checks (Stage 6 Phase 0 — [doc 54_](54_pair_production_axiom_derivation.md))

| Test ID | Claim | Status | Evidence |
|---|---|---|---|
| AD-1 | `V_SNAP = m_e c² / e` derives from Axiom 2 + Axiom 4 | ✓ | [54_ §3](54_pair_production_axiom_derivation.md) |
| AD-2 | `V_yield = √α · V_SNAP` derives from same | ✓ | [54_ §5](54_pair_production_axiom_derivation.md) |
| AD-3 | `Ω_node(V) = ω_0 · (1 − V²/V_yield²)^(1/4)` from Axiom 4 varactor | ✓ (closed form) | [54_ §4](54_pair_production_axiom_derivation.md) |
| AD-4 | `κ_chiral = α · pq / (p+q) = 1.2α` for (2,3) winding | ✓ (Sub-Theorem 3.1.1) | [20_ §3](20_chirality_projection_sub_theorem.md), [54_ §6](54_pair_production_axiom_derivation.md) |
| AD-5 | `δ_lock = ω_0 · α` from Q = 1/α | ✓ | [27_](27_step6_phase_space_Q.md), [54_ §7](54_pair_production_axiom_derivation.md) |

### 10.9 Stage 6 Phase 1 automated tests ([commit a0f50ed](../../src/tests/test_v_snap_v_yield_consistency.py))

| Test ID | File | Criterion | Status | Caveats |
|---|---|---|---|---|
| VY-1 | test_v_snap_v_yield_consistency.py | V_yield / V_SNAP = √α pinned at float64 precision | ✓ 927→940 pass | See §17 A3: no test verifies engine *uses* right normalization in `_update_z_local_total` |
| VY-2 | test_v_snap_v_yield_consistency.py | Schwinger/yield ratio = 1/√α | ✓ | — |
| VY-3 | test_v_snap_v_yield_consistency.py | Manifest entries do not conflate normalizations (string-match) | ✓ | See §17 A4: string-match is fragile |
| VV-1 | test_axiom_4_vacuum_varactor.py | C_eff(V) = C_0 / √(1 − (V/V_yield)²) form | ✓ | — |
| VV-2 | test_axiom_4_vacuum_varactor.py | Ω_node = ω_0 · (1 − (V/V_yield)²)^(1/4) | ✓ | — |
| VV-3 | test_axiom_4_vacuum_varactor.py | Taylor 4th-order matches Euler-Heisenberg | ✓ at r ≤ 0.2 | See §17 A5: loose FD tolerance; A²>1 regime never tested |
| **VV-4** | test_axiom_4_vacuum_varactor.py:233 | `TestAxiom4EngineKernelAgreement` — engine `saturation_factor()` matches closed form | ✓ | **TAUTOLOGICAL — see §17 A1** |
| PM-1 | test_predictions_matrix.py | Every pre-registered entry has a valid `research_doc` and (on-disk or whitelisted) `test_file` | ✓ | Whitelist brittle; see §17 A11 |
| PM-2 | test_predictions_matrix.py | `axioms_used` contains only values from {1, 2, 3, 4} | ✓ | Does not verify *semantic* axiom-use match |
| PM-3 | test_predictions_matrix.py | ID-naming convention (P_phaseN_*) enforced | ✓ | — |

### 10.10 Stage 6 Phase 2 automated tests ([commit 719f3ec](../../src/tests/test_phase2_node_resonance.py))

13 smoke tests (<2 s runtime). Driver: [node_resonance_validation.py](../../src/scripts/vol_1_foundations/node_resonance_validation.py).

| Test ID | File | Criterion | Status | Caveats |
|---|---|---|---|---|
| NR-1 | test_phase2_node_resonance.py | Cold vacuum: `omega_ratio_* = 1.0` exactly | ✓ | — |
| NR-2 | test_phase2_node_resonance.py | Functional form `Ω_node/ω_0 = (1 − A²_yield)^(1/4)` via poked single-site state | ✓ at rel=5e-5 | **Tautology risk** — `_poke_single_site_to_a_yield` uses same conversion formula the observer uses (§17 A1b) |
| NR-3 | test_phase2_node_resonance.py | Saturated regime: `omega_ratio_min < 1e-2`, `n_saturated = 1` | ✓ | Does not verify hard clip at `A²_yield = 1 + δ` for δ > 0 (§17 A8) |
| NR-4 | test_phase2_node_resonance.py | `add_observer` + `run(n_steps=3)` produces history length 3 | ✓ | Only loop-count; does not validate observer-state quality (§17 A9) |
| NR-5 | test_phase2_node_resonance.py | Cadence parameter respected | ✓ | — |
| NR-Pyth | test_phase2_node_resonance.py | Pythagorean sum: K4 and Cosserat add in quadrature | ⚠️ PARTIAL | Only K4-only case tested; **combined K4+Cosserat non-zero case never summed** (§17 A2) |
| NR-driver | node_resonance_validation.py on v2 headline | Records=60, NaN=0, consistency 1.11e-16 | ✓ | Max A²_yield=54.19 — **deep past saturation; observer clipping kicks in (see §17 A8)** |

**Important framing** (from commit 719f3ec message): P_phase2_omega as originally written was **circular** — the observer IS the closed form applied to engine state, so comparing them is a tautology. Phase 2's scope was narrowed: these tests pin the *arithmetic* of the observer + integration sanity; they do NOT falsify the varactor form as the correct description of the engine's coupled K4⊗Cosserat dynamics. That falsification requires a probe + FFT experiment, deferred to a later phase. This is noted in the `predictions.yaml` P_phase2_omega entry's `notes` field.

### 10.11 Stage 6 Phase 3 automated tests ([commit 3a599ca](../../src/tests/test_phase3_bond_state.py)) — on HEAD

> **r6 R4 note:** working-tree modifications to `test_phase3_bond_state.py` update the poke formulas to match the R4 subatomic-override convention (V = V_SNAP directly, no `√α` factor). A new test file [test_normalization_subatomic_override.py](../../src/tests/test_normalization_subatomic_override.py) pins R4 as an engine-level invariant (V_SNAP as subatomic V_yield; three observers agree on A²_total; A²_SNAP = 1 is the Regime IV boundary).

14 smoke tests on bond state + observer (at commit `3a599ca`, suite 940 → 954 pass, 0 failed).

| Test ID | File | Criterion | Status | Caveats |
|---|---|---|---|---|
| BS-1 | test_phase3_bond_state.py:59 | `Phi_link` initialized to exactly zero after engine construction | ✓ | — |
| BS-2 | test_phase3_bond_state.py:64 | `Phi_link.dtype` is float | ✓ | — |
| BS-3 | test_phase3_bond_state.py:68 | `reset_phi_link()` zeros existing state | ✓ | — |
| BS-4 | test_phase3_bond_state.py:85 | Scatter step alone does not change Φ (only `_connect_all` does) | ✓ | — |
| BS-5 | test_phase3_bond_state.py:95 | Connect without drive keeps Φ = 0 | ✓ | — |
| BS-6 | test_phase3_bond_state.py:101 | Sustained injection accumulates Φ monotonically | ✓ | — |
| BS-7 | test_phase3_bond_state.py:122 | Sign of Φ follows sign of drive | ✓ | — |
| BO-1 | test_phase3_bond_state.py:160 | BondObserver on empty vacuum: all metrics = 0 | ✓ | — |
| BO-2 | test_phase3_bond_state.py:169 | BondObserver reads state matching direct array poke | ✓ | — |
| BO-3 | test_phase3_bond_state.py:181 | BondObserver registers and runs for n_steps | ✓ | Same trivial-length concern as NR-4 (§17 A9) applies |
| BO-4 | test_phase3_bond_state.py:194 | Saturation partition (both-saturated vs ≥1-unsaturated) is correct for hand-constructed A²_yield field | ✓ | Exercises A²_yield saturation detection with the yield-normalized convention (see §17 A14) |
| BO-5 | test_phase3_bond_state.py:225 | BondObserver + RegimeClassifierObserver compose cleanly | ✓ | **Does not test A²_total consistency between the two — see §17 A1** |
| BO-6 | test_phase3_bond_state.py:243 | BondObserver with all other observers registered simultaneously | ✓ | — |
| RX-1 | test_phase3_bond_state.py:263 | `Phi_link` persists across engine steps (no silent reset) | ✓ | — |

**Physics adjudication DEFERRED:** P_phase3_flux_tube was expected to show persistent Φ on saturated bonds vs decaying Φ on unsaturated bonds (≥ 10 Compton vs ~3 Compton half-life). Driver result: identical ≈ 3.64-period half-lives, consistent with [54_ §6](54_pair_production_axiom_derivation.md) claim that flux-tube confinement requires the asymmetric μ/ε split from Phase 4. Re-run [flux_tube_persistence.py](../../src/scripts/vol_1_foundations/flux_tube_persistence.py) after Phase 4.

### 10.12 v2 headline reproducibility seed sweep — **COMPLETED 2026-04-23 → REGRESSION verdict**

Per §17 A10/A16 recommendation, [v2_reproducibility_seed_sweep.py](../../src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py) was run against the engine at HEAD (post-Phase-3 commit 3a599ca). 20 explicit RNG seeds, v2 headline config (λ=3.5, T=0.1, K_drift=0.5, amp=0.5·V_SNAP, N=40, 300 outer steps).

| Metric | Value |
|---|---|
| Range (max A²_cos) | **[0.7677, 0.9983]** |
| Median | **0.8683** |
| IQR | **[0.8097, 0.9181]** |
| Seeds at or above 1.009 headline | **0 / 20** |
| Seeds within ±0.05 of headline | 2 / 20 |
| Headline inside IQR | **No** |
| **Verdict** | **REGRESSION (headline outside IQR)** |

**Sub-finding — Cosserat sector holds all variance.** max `A²_K4 = 0.393` exactly across all 20 seeds (V_inc starts at 0 under `thermalize_V=False`; sources are deterministic; K4 sector is bit-identical seed-to-seed). All 20-seed spread comes from the Cosserat thermal initialization's propagation into coupled dynamics.

**Interpretation — two non-exclusive causes.**

1. **Code regression.** Phase 2 (`NodeResonanceObserver` import chain → JAX recompile / float-ordering) or Phase 3 (`Phi_link` accumulation in `_connect_all`, touched every K4 step) perturbed the coupled Cosserat trajectory despite being nominally "read-only" or "pure add." Diff-bisect candidates: 719f3ec (Phase 2 — JAX reset) vs 3a599ca (Phase 3 — `_connect_all` change).
2. **Tail outcome in original v2.** Doc 50_'s 1.009 was a single run. If the pre-Phase-2 distribution was the same [0.77, 1.00] shape, then 1.009 was a lucky tail and the headline framing was always over-confident.

Bisection against 7ab82c0 (pre-Phase-2) distinguishes these. Either way, doc 50_ §2.3's "A²_cos = 1.009 crossed rupture boundary" framing needs a distribution-based rewrite.

**Closure impact:** §17 A16 → **CLOSED** (sweep executed, verdict recorded). Spawns new finding **A17** (distribution-vs-headline framing; bisection-pending code-regression-vs-variance).

Artifacts: `/tmp/v2_reproducibility_sweep.npz`, `/tmp/v2_reproducibility_sweep.png`.

### 10.12.1 Bisection 719f3ec vs 3a599ca — **COMPLETED 2026-04-23 → cause 2 (tail outcome)**

20-seed sweep re-run at commit `719f3ec` (Phase 2 landed; Phase 3's `_connect_all` `Phi_link` accumulation + `BondObserver` not yet present). Same config, same seed integers 0..19.

**Result: bit-identical distribution.** Per-seed `max_A²_cos` values match HEAD (3a599ca) to float64 precision (0.0 absolute difference across all 20 seeds). `max_A²_K4 = 0.393374` and `max_τ_zx = 0.150736` also bit-identical. Artifacts: `/tmp/v2_reproducibility_sweep_719f3ec.{npz,png}`; HEAD artifacts preserved at `/tmp/v2_reproducibility_sweep_HEAD_3a599ca.*`.

| Metric | HEAD (3a599ca) | 719f3ec | Δ |
|---|---|---|---|
| Range | [0.7677, 0.9983] | [0.7677, 0.9983] | identical |
| Median | 0.8683 | 0.8683 | identical |
| IQR | [0.8097, 0.9181] | [0.8097, 0.9181] | identical |
| At or above 1.009 | 0/20 | 0/20 | identical |

**Conclusion: Phase 3 is dynamics-neutral for this workload.** `Phi_link` accumulation in `_connect_all` has no back-coupling into K4 wave propagation or Cosserat integrator; `BondObserver` is genuinely read-only; JAX cache changes do not perturb float ordering. The Phase 3 commit architecture is validated (additive state, no implicit coupling).

**A17 cause adjudicated: cause 2 (tail outcome), NOT cause 1 (code regression).** The r1 headline 1.009 was a lucky-seed tail from the default-RNG state at doc 50_ v2 write time; the 20-seed distribution accurately reflects the engine's actual behavior. Doc 50_ r3's distribution-language framing is the permanent correct framing; no further revision needed based on this bisection.

**Downstream implications:**
- R4 patches (plan file step 3) can proceed without regression-fix prerequisites.
- No Phase 2 / Phase 3 engine commit needs revision or revert.
- The bit-identical result further confirms R4: Cosserat dynamics are fully determined by the seed + source config, independent of which observers are registered — exactly what the R4 convention implies (observers are diagnostic-only, no measurement side-effects).

Deeper bisection against 7ab82c0 (pre-Phase-2) is available if you want to verify Phase 2's JAX-reset / import chain also has zero perturbation, but the identical distribution across 719f3ec vs HEAD already establishes Phase 3 is clean.

---

## 11. Known limits & non-representations

Load-bearing section. The pair-creation null result ([52_](52_h1_threshold_sweep.md)) is a consequence of these structural limits, not a physics failure of the AVE framework. Per [53_ §4](53_pair_production_flux_tube_synthesis.md).

### 11.1 ~~No dynamical link/bond state~~ — ✅ CLOSED by Stage 6 Phase 3 (commit `3a599ca` on HEAD)

**Resolution:** Phase 3 added `Phi_link[nx, ny, nz, 4]` state to `K4Lattice3D` (§5.1). `_connect_all` accumulates `V_avg · dt` per bond each TLM cycle. `BondObserver` (§8.5a) provides diagnostic access.

**Residual caveat** (see §17 A15): under current symmetric saturation, the bond state exists but flux-tube confinement physics (Γ = −1 walls at saturated endpoints) is not yet realized. Phase 3 ships the *infrastructure*; physics adjudication of P_phase3_flux_tube is deferred to after Phase 4 asymmetric μ/ε saturation. The structural limit is closed; the original motivation (observing confined pair-like standing waves on saturated bonds) remains open until Phase 4 lands.

### 11.2 ~~No per-node rotational resonance `Ω_node(A²)`~~ — ✅ CLOSED by Stage 6 Phase 2 (commit `719f3ec` on HEAD)

**Resolution:** Phase 2 added `NodeResonanceObserver` computing `Ω_node(r, t) = ω_yield · (1 − A²_yield(r, t))^(1/4)` read-only per the Duffing-softened resonance derivation. See §8.3 for the observer API and §13.2 for the original phase entry. The R4 `/α` removal patch (commit `6e355d1`) corrected the normalization; current observer returns canonical `r²`-form per Vol 4 Ch 1:711 subatomic override (§17.0).

**Residual:** the observer is read-only diagnostic. AutoresonantCWSource still tracks a Duffing shift at the **source-probe** site rather than per-node target site — see plan-file Finding 1 at `~/.claude/plans/read-through-th-kb-reactive-stardust.md` for the PLL anchor-math concern (ω_Compton vs ω_yield, ratio 0.571 always). Under Round 6 pivot, gate-related uses of Ω_node are suspended pending single-electron validation; the observer infrastructure remains useful as diagnostic.

### 11.3 ~~No nucleation rule~~ — ✅ CLOSED (CODE LANDED) by Stage 6 Phase 5 (commit `9ecc2ca`); FIRING ⏸ SUSPENDED in Round 6 pivot

**Resolution:** Phase 5 added `PairNucleationGate` observer-with-side-effect (commit `9ecc2ca`). Each step scans active A-B bonds; on C1 (A²_μ ≥ sat_frac at both endpoints) ∧ C2 (|Ω_node − ω_drive| < δ_lock), injects a point-rotation Beltrami pair (LH ω_A antiparallel to p̂_bond, RH ω_B parallel; |ω|=√2 such that each site carries ½·I_ω·|ω|² = m_e c²). Bond Φ_link[A, port] = ±Φ_critical; ω̇ zeroed; re-fire prevention via `_nucleated_bonds` set. 32-test suite (`test_phase5_pair_nucleation_gate.py`) pins construction defaults, C1/C2 decision table, δ_lock edges, re-fire prevention, injection profile (LH/RH sign, |ω|=√2, ω̇=0, Φ magnitude+sign), candidate bond topology, drive freq extraction, engine integration. Bingham-plastic capsule + Kelvin topological-protection framing per Vol 4 Ch 1:189-203 + Kelvin 1867. **Zero free parameters** (sat_frac=0.95 numerical, δ_lock = ω₀·α derived). See §13.5 for the original phase entry.

**Firing status (Round 6, suspended):** at registered config (N=24, amp=0.5·V_SNAP, autoresonant), max A²_total = 0.75-0.91 < sat_frac=0.95 → 0 firings (commit `3f9569b`). Three sessions of follow-up adjudication (C1-C2 window, four Readings of C2 condition, PLL anchor math, K4→Cosserat coupling weakness) **suspended in Round 6 pivot** ([doc 66_](66_single_electron_first_pivot.md)) pending single-electron validation precondition. The structural limit is closed (rule exists in code); the firing question is suspended.

### 11.4 ~~Plane-wave geometry over-symmetrizes at saturation~~ — partially closed by Round 6 Path B (`ff15c4b`); resumes if pair-nucleation gate work returns

Plane CW sources produce distributed strain across the full transverse plane. At A²_cos = 1.009 (v2), the entire x = N/2 plane saturates as a single rupture slab, not 2 distinct pair-core regions. H1 result ([52_](52_h1_threshold_sweep.md)) falsified the "threshold too strict" hypothesis; the read in [52_ §3.4](52_h1_threshold_sweep.md) and the synthesis in [53_ §2.1](53_pair_production_flux_tube_synthesis.md) is that C2 (frequency) and C3 (phase) cannot be satisfied at any specific node pair under plane-CW drive because plane symmetry does not pick a preferred pair.

**Round 6 partial resolution:** Path B at N=80 with localized (2,3) hedgehog seed in Cosserat ω + A28 fix + Cosserat self-terms re-enabled forms a bound (2,3) state for the first time in Stage 6 (`ff15c4b`, see §13.5b). This validates the "different source geometry" path — single-electron representation works under localized seeding, not plane-CW. The plane-CW limit remains structural for any future pair-nucleation work that returns to driven-source configurations, but is no longer load-bearing for single-electron validation.

**Resolution path** (preserved for if pair-nucleation gate work resumes post-Round-6):
- Add a `PointCollisionSource` (narrow-Gaussian, localized drive) — H2 from the handoff. Physically what AVE-PONDER and AVE-Propulsion Ch 5 actually describe.
- Accept that plane-CW is a structural limitation of Phase III-B configuration; pair creation requires a different source geometry. See [51_ §5](51_handoff_followups.md).

### 11.5 Measurement alias: Q_H flip ([42_ L1](42_coupled_simulator_validation.md))

`extract_crossing_count` on a time-evolving (u, ω) field is noisy; Q flips among {0, 1, 2, 3, 6} without physical change. Measurement artifact, not physics. Documented and noted; `extract_hopf_charge` (continuous) is the preferred Q observable per `TopologyObserver`.

### 11.6 A² saturation budget couples K4 and Cosserat

`A²_total = A²_K4 + A²_Cos` is the Axiom-4 argument. At high A²_K4 (e.g., amp = 0.7·V_SNAP), the K4 sector consumes most of the A² budget and A²_Cos response is suppressed relative to amp = 0.5·V_SNAP. This falsifies naive "increasing amplitude increases Cosserat response" (P_IIIb-β in [48_](48_pair_creation_frequency_sweep.md) §3.2). Not a bug — this is Axiom-4-correct behavior.

### 11.7 Cosserat moduli are placeholders (S-gate S4 = A)

`ρ = I_ω = 1` in natural units. SI calibration is deferred post-Phase-III per the S4=A decision ([S_GATES_OPEN.md](S_GATES_OPEN.md)). Physical interpretations of absolute amplitudes require a calibration pass that ties `ρ`, `I_ω` to the electron rest mass through the post-Phase-III soliton geometry. Not load-bearing for Phase III-B predictions (which are all intra-sim comparisons).

### 11.8 η_vac not a user parameter (C2)

Mutual inductance between adjacent K4 nodes is geometrically locked by the 4-port scatter matrix `S_ij = 0.5 − δ_ij`. There is no `η_vac` knob. Cascade coupling strength is controlled indirectly via `coupling_kappa` (default 1.0). AVE-PONDER SPICE calibration gives `K_0 = 0.207973` as an empirical proxy. Per [46_ §2.2 (C2)](46_vacuum_engine_scope.md).

### 11.9 ~~Axiom-4 single-sector saturation (isotropic μ/ε)~~ — ✅ CLOSED by Stage 6 Phase 4 (commit `a5bd1da`)

**Resolution:** Phase 4 replaces the isotropic `S = √(1 − A²)` with the asymmetric split `(S_μ, S_ε)`:
- `A²_μ = κ²/ω_yield²` (curvature → magnetic saturation)
- `A²_ε = ε_sym²/ε_yield² + V²/V_SNAP²` (strain + voltage → electric saturation)
- Instantaneous Beltrami helicity `h_local = ω·(∇×ω)/(|ω|·|∇×ω|)` drives chirality bias (no accumulator — adjudicated design 1A per a5bd1da).
- Reflection density `Γ² = (1/16) · |∇S_μ/S_μ − ∇S_ε/S_ε|²` — vanishes at `S_μ = S_ε` (Achromatic Impedance Lens / gravity regime); diverges at `S_μ → 0` with `S_ε` finite (Meissner-like `Γ → −1` wall, the pair-confinement mechanism).
- Chirality coupling `κ_chiral = 1.2α` per [20_ §3](20_chirality_projection_sub_theorem.md); **derived, not a free parameter**.

**Verification:** full Phase 4 test suite at [test_phase4_asymmetric_saturation.py](../../src/tests/test_phase4_asymmetric_saturation.py) pins 7+ invariants (symmetric limit recovers classical single-S behavior; helicity bias direction; asymmetric reflection vanishing condition; engine integration). Suite 965 → 983 pass. Working-tree addition of Invariant 8 (Meissner-headline mechanism validation) is pending commit.

**Residual open** (not part of this limit): pre-registered prediction `P_phase4_asymmetric` from [doc 54_ §6 line 227](54_pair_production_axiom_derivation.md) — *"under RH circular drive at amp = 0.5 V_SNAP, focal node reaches S_μ < 0.1 while S_ε > 0.5, driving Z_eff < 0.2 Z_0"* — requires a `CircularlyPolarizedCWSource`, deferred as Phase 5 prerequisite per a5bd1da commit message. Phase 4 validates the **mechanism** (asymmetric kernel produces the right Γ form); P_phase4_asymmetric validates the **driven response** and is the Phase 5 gate.

### 11.11 K4-TLM exhausted at node level for bound-electron representation (added in r8, Round 6)

**Authority:** [Vol 1 Ch 8:49-50](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex#L49) handoff comment, corpus-confirmed; [doc 66_ §14.2](66_single_electron_first_pivot.md).

**Statement:** the K4 lattice's perfect 4-port tetrahedral symmetry means every direction at a K4 node looks equivalent. Ax4 saturation requires *symmetry-breaking* to do something — but with 4 equivalent ports, there is nothing to break against. **Node-level Ax4 is therefore a no-op on K4 alone.** K4 carries the translational-EM circuit (V_inc ↔ Φ_link conjugate pair); Cosserat ω carries the rotational-EM degrees of freedom (the ω̂ axis IS itself a preferred direction) that provide the symmetry-breaking required for Ax4 to act asymmetrically.

**Empirical confirmation:** Round 6 Path A (`fbbc950`) seeded K4 V_inc only and ran closed-system evolution at N=48, 400 steps. 4 of 4 physical predictions falsified — `P_electron_tlm_topological_charge`: N_crossings=0 (expected 3); `P_electron_tlm_golden_torus_convergence`: R/r → 0.281 (expected φ²); `P_electron_tlm_alpha_derivation`: α⁻¹ = NaN (R ≤ r at fixed point); `P_electron_tlm_energy_conservation`: PASSED (integrator clean). All four failures trace to one missing mechanism (Cosserat ω at zero — charge/voltage leg without spin/current leg). One-mechanism cleanup of four predictions = informative failure at maximum strength.

**Consequence:** the bound electron physically lives in the Cosserat sector, not in K4. Any K4-only or K4-centric architectural choice for single-electron / bound-state work is structurally precluded. Phase 2/3 of Stage 6 committed observers (NodeResonanceObserver) and gate logic (PairNucleationGate) to the K4 sector despite this corpus signal — three sessions of gate adjudication ran downstream of an undetected limit. Methodology lesson now codified: corpus-search at architectural-decision time (COLLABORATION_NOTES Rule 8 Round 6 strengthening).

**Status:** structural limit. Resolution path is the Round 6 single-electron-first arc with Cosserat-sector seeding (Path B + F17-G coupled-eigenmode finder). See [doc 66_ §13-§14](66_single_electron_first_pivot.md) for the full pivot rationale.

### 11.10 Phase III-B detection threshold pinned at 0.3 (post-H1)

Default `TopologyObserver.threshold_frac = 0.3`. The H1 sweep ([52_](52_h1_threshold_sweep.md)) showed that lowering below 0.3 gives thermal-noise dominated count explosion; keeping at 0.7 misses sub-peak structures. 0.3 is an empirical compromise, not derived. Consistent with the `min_cluster_size = 8` coupled default.

---

## 12. Open S-gates and free-parameter status

Canonical gate record: [S_GATES_OPEN.md](S_GATES_OPEN.md). This section tracks gate states relative to the current engine build. "Resolved" gates that are **reopened** by a Stage 6 planned change are listed with both states.

### 12.1 Phase II S-gates (all closed 2026-04-22)

| Gate | State | Decision | Current engine behavior |
|---|---|---|---|
| S1 | **Closed → Reopened** for Phase 4 | Choice: **D** — `(V²/V_SNAP²) · W_refl` | Implemented; zero new parameters. Stage 6 Phase 4 requires re-adjudication to split μ/ε kernels (Option A-like linear augmentation is explicitly rejected; [54_ §6](54_pair_production_axiom_derivation.md) uses asymmetric saturation instead). |
| S2 | Closed (deferred) | Choice: **γ** — port pairing moot under S1=D | No port-phase dependence; re-opens only if S1 swaps to phase-sensitive form. |
| S3 | Closed | Choice: **A** — no amplitude gate | Coupling is axiomatically gated by 1/S² in W_refl. |
| S4 | Closed | Choice: **A** — natural units `ρ = I_ω = 1` | SI calibration deferred post-Phase-III. |
| S5 | Closed | Choice: **B** — unified leapfrog | Cosserat sub-stepping at n_sub ≈ 8 handles rate mismatch stably. |
| S6 | Closed | Choice: **A** — soft/diagnostic Q | Q_H measured via Hopf invariant; not enforced. Q-drift is a signal, not a bug. |

### 12.2 Free-parameter status (per [54_ §10](54_pair_production_axiom_derivation.md))

| Parameter | Status | Source | Notes |
|---|---|---|---|
| `κ_chiral` | Closed at `1.2α ≈ 8.757 × 10⁻³` | Sub-Theorem 3.1.1 in [doc 20_](20_chirality_projection_sub_theorem.md); [54_ §6](54_pair_production_axiom_derivation.md) | Not a tunable; derived from parallel-channel impedance. |
| `δ_lock` | Closed at `ω_0 · α` | Q = 1/α at TIR boundary, [doc 27_](27_step6_phase_space_Q.md) | Empirical re-pin may be needed if Phase 5 gate fires at wrong rate. |
| Beltrami vortex amplitude | Open | [54_ §10.5](54_pair_production_axiom_derivation.md) | Calibrated such that bond energy = m_e c²; exact profile (Beltrami vs Hopf) is a Phase 5 design choice. |
| V_SNAP / V_yield normalization | Flagged open; resolved in Stage 6 Phase 1 | [45_ §3.1](45_lattice_impedance_first_principles.md), [54_ §5](54_pair_production_axiom_derivation.md) | Phase 1 test `test_v_snap_v_yield_consistency.py` pins `V_yield / V_SNAP = √α`; Phase 2+ accessors use `A²_yield = A²_SNAP / α`. |
| `K_drift` | Empirical at 0.5 | Stage 4c sweep | Stability confirmed for K_drift ∈ [0, 2.0]. |
| `threshold_frac` (TopologyObserver) | Empirical at 0.3 | Stage 5 Phase A, [52_](52_h1_threshold_sweep.md) | Below: thermal-noise count explosion. Above 0.7: misses sub-peak structures. |
| `probe_x_offset` (AutoresonantCWSource) | Empirical at 4 cells | Stage 4c | Physically downstream of source into the interaction region. |

### 12.3 S-gates — Phase 4 S1 reopen RESOLVED; Phase 5 gate unchanged

**S1 reopen (Phase 4 asymmetric saturation)** — ✅ ADJUDICATED 2026-04-23 (commit `a5bd1da`). Grant's adjudication (reflected in commit message):

- **1A** — chirality bias is instantaneous, not an accumulator. `h_local = ω·(∇×ω)/(|ω|·|∇×ω|)` is a property of the current ω field; no hysteresis state. User's rationale: *"b seems like a possible engineering hack, like super cavitation"* — hysteresis would be a material artifact not fundamental vacuum physics.
- **2-II** — reflection density splits per `∇ ln(Z_eff)` asymmetric form: `Γ² = (1/16) · |∇S_μ/S_μ − ∇S_ε/S_ε|²`. Vanishes at `S_μ = S_ε` (Achromatic Impedance Lens per Vol 4 Ch 11 — gravity regime, no confinement). Diverges at `S_μ → 0` with `S_ε` finite (Meissner-like `Γ → −1` wall, the Phase 5 pair-nucleation mechanism).
- **3c** — full physics replacement; default to asymmetric; update any failing tests to reflect corrected Achromatic Lens behavior. (In practice, 0 tests broke: 965 → 983 pass on the Phase 4 commit.)

**Result:** the asymmetric saturation kernel is now the canonical AVE form; single-S is recovered as the symmetric limit `h_local = 0 ⇒ S_μ = S_ε`. Closes §11.9 structural limit. See §13.4 for the full Phase 4 entry.

**Stage 6 Phase 5 (PairNucleationGate)** introduces a discrete topology-change event (Beltrami-vortex boundary injection at C1 ∧ C2 → inject). This is Option D from [44_ §5.2](44_pair_creation_from_photon_collision.md). It does **not** reopen S1 (the coupling Lagrangian is unchanged by Phase 5); the gate is an observer-with-side-effect, not a new term in L. Phase 5's precondition is `CircularlyPolarizedCWSource` (flagged in a5bd1da commit message as "next"). No new free parameters under the §12.2 closures.

---

## 13. Queued additions (Phase Planned)

**Not yet in code.** Stage 6 engine changes authorized by [54_ §9](54_pair_production_axiom_derivation.md). Each phase is listed with its derivation authority, rough effort, and success criterion. This section is a roadmap, not a description of current behavior — a reader cannot mistake it for §3 or §5.

### 13.1 Phase 1 — V_SNAP / V_yield consistency test ✅ LANDED 2026-04-22 (commit a0f50ed)

**Authority:** [54_ §5](54_pair_production_axiom_derivation.md). Flagged originally in [45_ §3.1](45_lattice_impedance_first_principles.md).

**Landed:**

- [test_v_snap_v_yield_consistency.py](../../src/tests/test_v_snap_v_yield_consistency.py) — pins V_yield = √α · V_SNAP, conversion factor 1/α, Schwinger/yield ratio 1/√α, manifest-level consistency guards.
- [test_axiom_4_vacuum_varactor.py](../../src/tests/test_axiom_4_vacuum_varactor.py) — pins the Vol 4 Ch 1:127–142 varactor curve, Taylor expansion to 4th order, Ω_node softening, engine kernel agreement.
- [test_predictions_matrix.py](../../src/tests/test_predictions_matrix.py) — CI gate preventing pre_registered predictions drifting from their tests.
- [manuscript/predictions.yaml](../../manuscript/predictions.yaml) — structured claim graph (see §3.6 below).
- Updated [claim_graph_validator.py](../../src/scripts/claim_graph_validator.py) with `PRE_REGISTERED_REQUIRED_FIELDS` schema.

**Known gaps in Phase 1 tests** (see §17 findings A1, A2, A3 for detail):

- `TestAxiom4EngineKernelAgreement` ([test_axiom_4_vacuum_varactor.py:233](../../src/tests/test_axiom_4_vacuum_varactor.py#L233)) compares engine to test's own `_closed_form_S()` helper — tautological.
- No test exists that verifies the engine *uses* the right normalization in the coupled `_update_z_local_total()` path, only that the constants are right.
- No `A²_yield = A²_SNAP / α` accessor landed on `VacuumEngine3D` as a public API — it's implicit inside `NodeResonanceObserver` only.

### 13.2 Phase 2 — `NodeResonanceObserver` ✅ LANDED 2026-04-22 (commit 719f3ec)

**Authority:** [54_ §4, §9.1](54_pair_production_axiom_derivation.md).

Moved to as-built §8.3. Summary of what landed:

- Observer: [vacuum_engine.py:391](../../src/ave/topological/vacuum_engine.py#L391)
- Unit tests: [test_phase2_node_resonance.py](../../src/tests/test_phase2_node_resonance.py) (13 tests, <2 s runtime)
- Driver: [node_resonance_validation.py](../../src/scripts/vol_1_foundations/node_resonance_validation.py) (329 lines)
- Driver headline run: records=60, NaN=0, max A²_yield=54.19 (deep past yield on v2 config), min Ω_node/ω_0=0.001 (clipped at saturation)
- Test suite: 927 → 940 passed; 0 failures

**Open item (flagged to §17 A6):** P_phase2_omega was determined to be circular ("observer IS the closed form"). Real physics falsification of the varactor form **on the coupled K4⊗Cosserat sector** (as distinct from arithmetic verification) is deferred to a probe + FFT experiment in a later phase.

**Additional deliverable, scope-creep:** the driver script plots `AutoresonantCWSource`'s linear-Taylor approximation `(1 − K_drift · A²)` against the full varactor `(1 − A²_yield)^(1/4)`. The two diverge significantly at `A² > 0.3`, which flags whether Phase 5 should upgrade the source to use the full varactor form for tight autoresonant lock. See §17 A7.

### 13.3 Phase 3 — `Phi_link` bond state ✅ LANDED 2026-04-22 (commit `3a599ca` on HEAD)

**r7 note:** R4 observer patches committed at `6e355d1` (2026-04-23). `/α` removed from `BondObserver._compute_A2_yield` and `NodeResonanceObserver._capture`; the `_compute_A2_yield` method name is preserved for backward-compat but is semantically canonical `r²` under the subatomic override. See §17.0 for the adjudication + §17.2 A14 closure.

If A17 bisection (`719f3ec` vs `3a599ca` sweeps both have `.npz` artifacts at `/tmp/`) identifies Phase 3's `_connect_all` `Phi_link += V_avg·dt` as a trajectory perturbation source, a code-level fix may also be needed; distribution-vs-convention decoupling per doc 50_ r3 §0.3 item 2 means R4 alone doesn't address A17.

**Authority:** [54_ §3, §9.2](54_pair_production_axiom_derivation.md).

**What shipped:**

- `K4Lattice3D.Phi_link[nx, ny, nz, 4]` state array (A-site-only storage to avoid A/B double counting; B's Φ derived by port-shift).
- `K4Lattice3D.reset_phi_link()` for sub-experiments.
- `_connect_all` accumulates `V_avg · dt` per bond before the port shift.
- `BondObserver` (§8.5a): reports `phi_abs_max`, `phi_rms`, saturated/unsaturated bond partitions with tunable `saturation_frac`.
- [test_phase3_bond_state.py](../../src/tests/test_phase3_bond_state.py) — 14 smoke-tier tests: initial state, reset, scatter-alone invariance, sustained-drive accumulation, sign-follows-drive, observer partition correctness, multi-observer composition.
- [flux_tube_persistence.py](../../src/scripts/vol_1_foundations/flux_tube_persistence.py) driver — 35 s pulse-then-observe run, 25 Compton periods of post-drive observation.
- Test suite 940 → 954 passed (+14), 0 failed. Regression-tested against all 92 K4/Cosserat/coupled tests.

**P_phase3_flux_tube adjudication — DEFERRED to post-Phase-4:**

The driver measured saturated-bond and unsaturated-bond Φ_link half-lives at ≈ 3.64 Compton periods each — **identical**. Under symmetric saturation (single-S kernel), the Γ = −1 flux-tube confinement wall doesn't form; this is expected per [54_ §6](54_pair_production_axiom_derivation.md). P_phase3_flux_tube cannot meaningfully pass or fail until Phase 4 asymmetric μ/ε saturation lands. The Phase 3 test infrastructure ships correctly (arithmetic + integration); re-run the driver after Phase 4 for the physics pass/fail.

**Known gaps** (see §17 findings):
- A14 — BondObserver's `saturation_frac=0.5` default uses V_yield normalization, which makes it consistent with NodeResonanceObserver but *inconsistent* with RegimeClassifierObserver. Normalization discrepancy is now systemic across 3 observers.
- A15 — the identical half-lives finding depends on the chosen A²_yield convention; revisit once A1 is adjudicated.

### 13.4 Phase 4 — Asymmetric μ/ε saturation ✅ LANDED 2026-04-23 (commit `a5bd1da`)

**Authority:** [54_ §6, §9.3](54_pair_production_axiom_derivation.md); ground-truth [Vol 1 Ch 7:252](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L252), [Vol 4 Ch 1:163–187](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L163), [20_ §3](20_chirality_projection_sub_theorem.md) (for `κ_chiral = 1.2α` derivation).

**What shipped** (per a5bd1da commit message):
```
A²_μ = κ²/ω_yield²                                (curvature → magnetic saturation)
A²_ε = ε²/ε_yield² + V²/V_SNAP²                  (strain + voltage → electric saturation)
h_local = (ω · (∇×ω)) / (|ω| · |∇×ω|)             instantaneous Beltrami helicity ∈ [−1, +1]
                                                  — NOT accumulator (design 1A)
A²_μ_biased = (1 + κ_chiral · h_local) · A²_μ_base
A²_ε_biased = (1 − κ_chiral · h_local) · A²_ε_base
S_μ = √(1 − A²_μ),   S_ε = √(1 − A²_ε)
Γ² = (1/16) · |∇S_μ/S_μ − ∇S_ε/S_ε|²             asymmetric reflection form (design 2-II)
```
Achromatic limit: `S_μ = S_ε ⇒ Γ² = 0` (gravity regime, no confinement). Meissner limit: `S_μ → 0 with S_ε finite ⇒ Γ → −1` (pair-nucleation wall for Phase 5).

**S-gate S1 reopened + resolved** with design 1A / 2-II / 3c; see §12.3 for the adjudication details. `κ_chiral = 1.2α` per Sub-Theorem 3.1.1 — derived, not fit.

**Engine files modified:**
- `src/ave/topological/cosserat_field_3d.py` (+202 lines): helicity computation, (S_μ, S_ε) split.
- `src/ave/topological/k4_cosserat_coupling.py` (+139 lines): asymmetric impedance + coupling update.
- `src/ave/topological/vacuum_engine.py` (+6 lines): observer integration.
- `src/tests/test_phase4_asymmetric_saturation.py` (+383 lines): 7-invariant test suite (symmetric-limit recovery, helicity sign, asymmetric Γ form, engine integration, etc.).

**Test suite:** 965 → 983 pass (+18 from Phase 4 invariants). No regressions.

**Pre-registered prediction P_phase4_asymmetric** (from [doc 54_ §6:227](54_pair_production_axiom_derivation.md)): under RH circular drive at `amp = 0.5 V_SNAP`, focal node reaches `S_μ < 0.1` while `S_ε > 0.5`, driving `Z_eff < 0.2 Z_0`. **Mechanism validated** (Phase 4 test suite confirms the asymmetric kernel produces the right Γ form under constructed helicity); **full driven-source adjudication** requires `CircularlyPolarizedCWSource`, deferred as Phase 5 prerequisite.

**Working-tree addition:** `test_phase4_asymmetric_saturation.py` has a pending modification adding **Invariant 8 (Meissner-headline mechanism test)** — constructs a strong RH Beltrami ω field and verifies `S_μ < S_ε` under the asymmetric kernel without needing a full circular-polarized source. This bridges the gap between mechanism-level validation (committed) and driven-source validation (Phase 5).

### 13.5 Phase 5 — `PairNucleationGate` ⏸ LANDED but SUSPENDED in Round 6 pivot

**Authority:** [54_ §7, §9.4](54_pair_production_axiom_derivation.md).

**Status (r8):** Phase 5 PairNucleationGate landed (`9ecc2ca`) with full 32-test suite + Bingham-capsule + Kelvin-vortex topological-protection framing. Driver landed (`3f9569b`) at registered N=24, amp=0.5·V_SNAP — produced 0 firings (max A² = 0.75-0.91 < sat_frac=0.95). Three sessions of follow-up adjudication (C1-C2 gate window, four Readings of C2 condition, PLL anchor math, K4→Cosserat coupling weakness) **suspended in Round 6 pivot** ([doc 66_](66_single_electron_first_pivot.md)) pending single-electron validation precondition. The engine cannot stage one bound electron yet (Path A falsified, Path B blocked); debating triggers for two bound electrons is premature.

**Implementation kept** — gate code, tests, Bingham-capsule framing all in HEAD; future agents should NOT re-implement. Resume after single-electron validation closes.

**Original change spec (preserved for reference):** observer-with-side-effect, scan all directed A–B pairs:
```
for edge in active_bonds:
    r_A, r_B = edge.endpoints
    if A²_μ(r_A) ≥ 1 and A²_μ(r_B) ≥ 1:                    # C1
        for source in engine.sources_with_omega:
            if |Ω_node(r_A) − source.omega| < δ_lock:       # C2
                inject_beltrami_pair(r_A, r_B)
                mark_bond_nucleated(edge)
                break
```
**C2 reframing pending:** the four Readings of C2 (Compton-lock-is-rupture / PLL-chirps-past-lock / drive-health-boolean / parity-chirality-coincidence) per the suspended plan at `~/.claude/plans/read-through-th-kb-reactive-stardust.md` await Round 6 closure.

**Pre-registered prediction P_phase5_nucleation:** gate fires under C1 ∧ C2 within 50 Compton periods; zero firings at `amp < 0.3 V_SNAP`. Currently UNTESTED at registered config — first run undershoots C1; resolution gated on single-electron precondition closing.

### 13.5a Phase 5e — Cool-from-above driver ✅ LANDED 2026-04-24

**Authority:** [doc 59_ §5.4](59_memristive_yield_crossing_derivation.md) lattice-genesis BEMF-driven defect freezing.

**Change:** First empirical test of doc 59_'s cool-through-yield mechanism. Two-phase drive profile (drive → abrupt cutoff → cool); 4-panel diagnostic (A² evolution, S_field, gate firings, Ω_node).

**Result:** First commit (`1805d14`) at amp=0.9·V_SNAP showed engine stable (max A²=0.905, no blow-up under memristive K4) but S_field stayed at 1.000 throughout — saturation kernel was DORMANT. Diagnosis: **Flag-5e-A** — `K4Lattice3D._update_z_local_field` used module-level V_SNAP (511 kV SI) for strain normalization, while engine sources inject in engine-natural V_SNAP=1. Strain calculation gave 10⁻⁶ instead of 0.9 → S_eq → 1 always → entire Ax4+Op14+Op3 saturation path dormant in any engine-natural-units context. Fixed in `098d430` (V_SNAP plumbed from engine through `CoupledK4Cosserat` constructor). Phase 5e re-run: **first empirical cool-through-yield** — S drops 1.0 → 0.507 during drive, recovers to 0.983 post-drive. Mechanism from doc 59_ now observable in simulation.

**Residual:** gate still doesn't fire — Cosserat A²_μ peaks at 0.012 even when K4 saturates (Step 5a finding `0419b7e`). Step 5b v2 (`d0609ad`) drove Cosserat directly via CosseratBeltramiSource to A² → 3.34 — C1 satisfied but C2 still never satisfies, exposing gate window incompatibility as architectural. All gate-firing concerns now subsumed under Round 6 single-electron pivot.

### 13.5b Round 6 single-electron validation — Path A FALSIFIED, Path B FORMING BOUND STATE under A28 fix (`ff15c4b`), Path C runaway, F17-I three-mode tested

**Authority:** [doc 66_](66_single_electron_first_pivot.md).

**Change:** Closed-system evolution from a seeded soliton ansatz, no drive, PML boundary. Validate (2,3) winding persistence, rest energy ≈ m_e c², Compton-frequency oscillation, spatial localization.

**Path A (K4 V_inc only):** ✅ FALSIFIED (`fbbc950`). 4 of 4 physical predictions failed; energy conservation passed. All four failures trace to K4-TLM exhaustion at node level (§11.11). K4 alone cannot host the bound electron.

**Path B (Cosserat ω only at corrected amp |ω|=0.3π):** ⚠ **r8.3 "FORMING BOUND STATE" claim WALKED BACK in r8.4** — twice-confounded per F17-K audit (`a53ce1c`, `4c9fbea`).

**Original r8.3 claim (preserved for audit trail):** under A28 + Cosserat self-terms re-enable (`ff15c4b`, 2026-04-25), Path B at N=80 was reported to hold c=3 + shell_Γ² ≈ 4 + R/r ≈ φ² through step 20, with the following table:

| step | peak \|ω\| | shell_Γ² | R/r | c |
|---|---|---|---|---|
| 0 | 0.939 | 3.061 | 2.733 | **3** (seeded) |
| 1 | 0.149 | 0.001 | 0.976 | 3 |
| 2 | 0.882 | 3.143 | 2.733 | **3** (recovers) |
| 5 | 0.940 | 3.947 | 5.000 | 3 |
| 10 | 0.797 | 3.948 | 1.706 | 3 |
| 20 | 0.664 | 3.948 | 1.688 | 2 (drift starts) |
| 50 | 1.494 | 0.000 | 0.500 | 0 (degrades) |

**r8.4 walk-back rationale:** the "bound state" reading of the table above is twice-confounded:

1. **Wrong observable.** Per F17-K Phase 1 audit ([doc 68_](68_phase_quadrature_methodology.md), commit `a53ce1c`), the c_cos and shell_Γ² extraction used Cartesian shell-radius binning, not the AVE-native phase-space (V_inc, V_ref) phasor observable that Vol 1 Ch 1 Axiom 3 (Effective Action Principle) demands. Cartesian shell-radius behavior consistent with a (2,3) ansatz is necessary but not sufficient for "AVE-native bound state."
2. **Wrong amplitude.** Per F17-K Phase 5c-v2-v2 empirical run ([doc 67_ §25](67_lc_coupling_reciprocity_audit.md), commit `4c9fbea`), the bound state in AVE lives at saturation onset (peak |ω| ≈ 0.94 = 0.3π per [doc 34_ §9.4](34_x4_constrained_s11.md)). The Path B run's peak |ω| oscillated wildly through the table (0.149 → 1.494) without amplitude pinning. Peak |ω| = 0.939 at step 0 corresponds to saturation onset, but this wasn't maintained through descent.

**Reframed r8.4 reading:** Path B at N=80 showed Cartesian-shell behavior consistent with a (2,3) ansatz at the seed and through approximately step 20, but failed AVE-native phase-space validation (F17-K Phase 5a-b at commit `4d4b4aa`) AND failed bound-state-finding under coupled-engine descent at saturation-onset amplitude (F17-K Phase 5c-v2-v2 at commit `4c9fbea`). **Path B is not a closed validation of the bound (2,3) electron in the coupled engine.** See §13.5d for the F17-K methodology arc that empirically resolved this.

**Strain-mask infrastructure declared deferred** (was §13.5c) — A28 was the actual gate for the Path B step-1 collapse. ~550 LOC opt-in collapsed to zero. See §13.5c for the deferred-status note.

**Path C (K4 V_inc + Cosserat ω, mixed):** ran, runaway energy. Per [doc 66_ §17.2.3](66_single_electron_first_pivot.md): seeded a C-state of one LC pair AND an L-state of a different LC pair — never both halves of either pair. F17-I "all-C-state or all-L-state coupled seed" tested next.

**F17-G coupled-eigenmode finder** (`815cd40`): outer-loop self-consistent eigenmode search — seed both sectors → undamped evolve → time-RMS combined-magnitude envelope → extract (R, r) → feedback → check convergence. Termination: converged | diverged | topology_lost | geometry_collapsed | max_iter_no_converge.

**F17-I three LC-pair-coherent seed modes** (`687b18d`, doc 66_ §18): tested all three coupled-seed candidates side-by-side at N=48, R=12, r=R/φ²:

| Seed mode | Fields seeded | Result |
|---|---|---|
| `all_c` | V_inc + u (both C-states of their respective LC pairs) | Catastrophic divergence at step 1 (|ω| 0 → 1030) |
| `all_l` | Φ_link + ω (both L-states) | Energy bounded (E < seed); |ω| relaxes monotonically 0.93 → 0.35; topology dissolves (R/r 2.6 → 0.2, c=0). Stable non-toroidal endpoint. |
| `mixed` (Path C) | V_inc + ω | Runaway at step 13 |

**Empirical diagnostic of L_c coupling asymmetry.** Pattern across the three modes: one direction explodes, opposite direction relaxes monotonically without back-channel, mixed amplifies. A reciprocal LC coupling would show energy oscillating between sectors at ω_C — observed behavior is unidirectional energy flow Cosserat → K4 in `all_l`, with no reverse channel. **L_c = (V²/V_SNAP²)·W_refl(u, ω) empirically behaves as a one-way energy pump rather than a reciprocal oscillator coupling.**

**F17-H** — ✅ CLOSED via A28 (not via path-1 EMF). Audit per [doc 67_](67_lc_coupling_reciprocity_audit.md) §1-§16. Initial direction (path-1: ADD a Lagrangian-derived voltage source EMF_c = -2V·W_refl/V_SNAP² to bond Φ_link integration) was the **wrong fix** — implemented in `3d7fae4` then retracted in `85bdb6f` after Vol 4 Ch 1 cross-check. Op14 z_local modulation IS the K4-TLM varactor (Vol 4 Ch 1:130 `C_eff(V) = C₀/S(V)` extended with cross-sector A²_Cos). The legacy `_compute_coupling_force_on_cosserat` channel was a redundant implementation of the same physics — **double-counting since Phase 4** (`a5bd1da`). Removing the redundant force (`05b130f`) + re-enabling Cosserat self-terms while auto-suppressing redundant `k_refl` (`ff15c4b`) is the structural fix. **Six prior failure modes** (Path A / Path B / Path C / F17-G / F17-I / path-1 EMF) all explained by ONE bug. See §17 A28 for the audit-finding write-up.

**F17-J followup:** characterize `all_l`'s pre-A28 relaxation endpoint — non-toroidal but stable. May no longer be load-bearing under A28 fix; revisit if needed.

New seeders introduced in `687b18d`:
- `cosserat_field_3d.py::initialize_u_displacement_2_3_sector` — seeds Cosserat `u` with (2,3) hedgehog, ω at zero. Companion to existing `initialize_electron_2_3_sector` (which seeds ω with u at zero).
- `tlm_electron_soliton_eigenmode.py::initialize_phi_link_2_3_ansatz` — seeds K4 Φ_link with (2,3) chiral phasor at A-sites, V_inc at zero. Companion to existing `initialize_2_3_voltage_ansatz`.

**Pre-registered Path B predictions** (provisional pending Grant approval per doc 66_ §14.4):
- `P_electron_cosserat_topological_charge`: N_crossings = 3 preserved over ≥100 Compton periods
- `P_electron_cosserat_shell_TIR`: shell_Γ² ≥ 1 at run end
- `P_electron_cosserat_energy_conservation`: ΔE/E₀ < 0.5%
- `P_electron_cosserat_golden_torus`: Op6 self-consistency converges to R/r = φ²
- `P_electron_cosserat_alpha_derivation`: α⁻¹ from coupled dynamics matches 137.036 ±2%

### 13.5c ~~Strain-determined dynamic boundary infrastructure~~ — DEFERRED (A28 was the actual gate)

**Status (r8.3):** **Deferred indefinitely.** Plan was drafted at `~/.claude/plans/read-through-th-kb-reactive-stardust.md` to address Path B's step-1 collapse via opt-in `dynamic_mask` flag (~550 LOC; static lattice + dynamic strain-determined active region with hysteresis at A² > α). The plan diagnosed PML truncation as the root cause of Path B failure.

**A28 found the actual root cause** (`05b130f`, 2026-04-24): legacy `_compute_coupling_force_on_cosserat` channel double-counts Op14 z_local modulation. Path B at N=80 with `disable_cosserat_lc_force=True` + `enable_cosserat_self_terms=True` (`ff15c4b`) forms the bound (2,3) state directly — no infrastructure rebuild required. **~550 LOC of planned infrastructure work zeroed out.**

The plan file is preserved as audit trail. If Path B drift past step 20 turns out to need active-region adaptivity (e.g., for moving-soliton work or Phase 5 pair separation), this work can resume. Not blocking single-electron validation.

### 13.5d ~~Op6 self-consistency outer loop on Path B~~ — DEPRECATED (subsumed by F17-K methodology arc)

**Status (r8.4):** **Deprecated.** The r8.3 plan to wire Op6 self-consistency on Path B at N=80 has been superseded by F17-K Phase 5c-v2-v2 empirical closure (commit `4c9fbea`, see §13.5e). Per F17-K Phase 1 audit (`a53ce1c`), Op6 on Cartesian shell extraction was Ax-3-noncompliant — the wrong observable for AVE-native eigenmode finding. The (C) X4b stationarity question Op6 was meant to answer was empirically resolved by Phase 5c-v2-v2: Golden Torus is NOT a stationary point of either Cosserat-energy or coupled-S₁₁ in the coupled engine (both descents drifted away from the seed at iteration 1).

The Op6 self-consistency methodology remains valid for Cosserat-only relax_s11 per [doc 34_ X4b](34_x4_constrained_s11.md) — that result confirmed Cosserat-only stationarity at Golden Torus, which is what's expected and reproduces the AVE-Core canonical pattern. The K4 sector adds instabilities that destabilize Golden Torus geometry in the coupled engine; this is the Round 6 finding, not an Op6 outer-loop convergence question.

### 13.5e F17-K methodology arc — Round 6 empirical closure (NEW in r8.4)

**Authority:** [doc 67_ §1-§25](67_lc_coupling_reciprocity_audit.md) (F17-H/F17-K reciprocity audit + acoustic-cavity reframe + dual descent with saturation pin) + [doc 68_](68_phase_quadrature_methodology.md) (Phase 1 Ax-3 noncompliance audit + phase-quadrature methodology) + [doc 03_ §4.3](03_existence_proof.md) corpus reference.

**The arc:** seven F17-K commits across ~6 hours, each substantive, each corpus-grounded:

| Commit | Phase | Content |
|---|---|---|
| `a53ce1c` | F17-K Phase 1 | Ax-3 noncompliance audit. Identifies that F17-I three-mode (all_c/all_l/mixed), Path B Op6, Cartesian shell extraction were all using time-evolution dynamics + real-space observables instead of AVE-native phase-space (V_inc, V_ref) phasor coordinates per Vol 1 Ch 1:51-75 Axiom 3. |
| `4d4b4aa` | F17-K Phase 5a-b | Phase-quadrature seed under raw step() empirically falsified. Three seed configs (Path B control, chirality=0, chirality=1) all fail to produce phase-coherent eigenmode under raw `VacuumEngine3D.step()` dynamics. |
| `6158465` | F17-K Phase 5c v1 | Coupled S₁₁ relaxation infrastructure built (~290 LOC). v1 unconstrained descent on `(u, ω, V_inc)` joint state empirically falsified — descent escaped the bound state by over-saturating Cosserat (peak \|ω\| 0.94 → 2.19, doubling past saturation onset). |
| `795c4ff` | F17-K corpus search 1 | Doc 34 X4 corpus pattern surfaced: *"imposing constraints on top of S₁₁ minimization, not by switching to a different objective... three hard algebraic constraints (d=1, R−r=1/2, R·r=1/4) are algebraic pinnings."* |
| `3f6d544` | F17-K corpus search 2 | Acoustic-cavity / Helmholtz framing surfaced: *"Reinterpret the Schrödinger Wave Equation deterministically as the continuous Helmholtz acoustic resonance of the LC vacuum"* (Vol 2 Ch 7). Doc 03 §4.3 natural-equilibria reading: Ch 8 constraints are NOT to be imposed by hand but emerge from Axiom-4 saturation + topology. F17-K Phase 6 (eigensolver) flagged as candidate. |
| `2c873cf` | F17-K Phase 5c v2 (v1 of v2) | Dual descent (Cosserat-energy + S₁₁) with tanh reparameterization. **Premature Finding 3 ("corpus-duality falsified") landed but was empirically confounded** — both descents ran at wrong amplitude (energy 0.61 sub-saturated, S₁₁ 2.31 over-saturated). Tanh reparameterization BOUNDS amplitude at ω_yield=π but doesn't PIN at saturation onset (peak \|ω\|≈0.94). |
| `4c9fbea` | F17-K Phase 5c v2-v2 | Saturation-pin replaces tanh: hard projection onto saturation manifold (peak \|ω\| = 0.9425 enforced after each gradient step). Pre-committed retraction of `2c873cf`'s premature Finding 3 honored. **Empirical closure of the F17-K arc.** |

**Final empirical result (commit `4c9fbea` Phase 5c-v2-v2):**

Both objectives correctly pinned at saturation onset (peak \|ω\| = 0.9425 = 0.3π per doc 34 §9.4). Topology preserved (c_cos = 3 in both). Each objective converges to a distinct (R, r) NOT at Golden Torus φ² ≈ 2.62:

| Objective | iters | obj reduction | converged R/r | distance from φ² |
|---|---|---|---|---|
| Cosserat-energy | 78 | 74% | **3.40** | 1.30× |
| coupled S₁₁ | 500 (still descending) | 99.76% | **1.03** | 0.39× |
| corpus claim | — | — | φ² = 2.62 (Golden Torus) | — |

The two minima differ from each other by 3.3× spread. **Doc 03_ §4.3 empirically validated** at coupled-engine scale:

> *"R·r = 1/4: topologically quantized, NOT dynamically derived... Both d=1 and R−r=1/2 are genuine dynamical derivations; R·r=1/4 is a topological identity that the Lagrangian must be consistent with but does not by itself produce."*

Cosserat-energy and coupled-S₁₁ each have continuous families of (2,3) stationary states; topology (SU(2) half-cover area match → R·r = 1/4) selects R/r = φ² from these families. Neither dynamical descent knows about quantization.

**Corpus-duality falsified at coupled-engine scale.** AVE-Protein Ch 3:805's *"the native fold minimises |S₁₁|²"* template, which Round 6 had been treating as scale-invariant per Axiom 2, **does not extend to the coupled K4+Cosserat single-electron problem.** Protein folding's S₁₁ minimization works because protein topology is selected by chemistry; the bound electron's (2,3) topology requires explicit quantization encoding because gradient descent on continuous objectives can't reach discrete topological invariants.

**(C) X4b stationarity verification — implicitly resolved.** Phase 5c-v2-v2 seeded at Golden Torus geometry (R=20, r=20/φ²=7.64) and ran descent. Both descents drifted at iteration 1: energy moved (R, r) from (20, 7.6) → (25.4, 7.5); S₁₁ moved (20, 7.6) → (17.5, 17.0). The fact that descent moved immediately means **the gradient at Golden Torus is nonzero** in both objectives — Golden Torus is NOT a stationary point. (Strict X4b is small-perturbation linear-stability test; Phase 5c-v2-v2 is global gradient flow. Different empirical content but same answer for the stationarity question because nonzero gradient implies non-stationary.) Doc 34 X4b's Cosserat-only stationarity result does NOT extend to coupled engine; K4 adds instabilities.

### 13.5f F17-K v3 path — v3 (i) RAN, Golden Torus geometrically unstable; v3 (ii) Phase 6 sparse eigensolver now load-bearing (UPDATED r8.5)

**v3 (i) Algebraic Ch 8 pinning per [doc 34_ X4](34_x4_constrained_s11.md) — RAN, RESULT: Golden Torus geometrically UNSTABLE under coupled S₁₁; MARGINAL under Cosserat-energy.**

Implementation: `coupled_s11_eigenmode.py::run_v3_x4b_linear_stability` (~150 LOC, commit `3fede52`). Initialize EXACTLY at Golden Torus → project ω onto saturation manifold → add 1% random δ → run `relax_with_pin` for 30 iters → classify stability by `‖δ_final‖/‖δ_initial‖` growth rate. See §13.5g for full empirical detail.

**Result (`3fede52`):** Cosserat-energy MARGINAL (1.81×, +0.0198/iter, slow); coupled S₁₁ UNSTABLE (5.31×, +0.0556/iter, exponential). Both runs preserved c=3 + saturation pin. **Cosserat-only X4b stability per doc 34 X4b does NOT extend to coupled engine.** K4 sector adds geometric instabilities at the linear-perturbation level, consistent with global-flow finding from Phase 5c v2-v2 (`4c9fbea`). r8.4's "v3 (i) is the closure gate" framing partially walked back.

**v3 (ii) F17-K Phase 6 sparse eigensolver per [doc 67_ §23.4 acoustic-cavity / Helmholtz framing](67_lc_coupling_reciprocity_audit.md)** — **NOW LOAD-BEARING for Round 6 closure** (~300 LOC).
- Linearize coupled K4+Cosserat dynamics around Golden Torus ansatz
- Build sparse Jacobian via JAX autodiff
- Use `scipy.sparse.linalg.eigsh` to extract (2,3) eigenmode at fixed cavity geometry
- Eigenvalue problem `Au = λBu` with boundary conditions encodes topological quantization explicitly (acoustic-cavity standing-wave physics per Vol 2 Ch 7 Helmholtz framing)
- **Doesn't require dynamical stability** — solves for eigenmodes regardless of whether they're attractors of descent. Critical for closing v3 (i)-revealed instability gap.

**Status (r8.5):** v3 (ii) Phase 6 sparse eigensolver is the empirically-motivated next-step methodology for closing single-electron representation. v3 (i) instability is not a regression — it's confirmation of the doc 03 §4.3 prediction (Golden Torus is selected by topology, not stabilized by dynamics). Eigenvalue methodology can find Golden Torus as eigenmode at fixed cavity geometry without requiring it to be a dynamical attractor.

**Effort:** v3 (ii) ~300 LOC, ~3-4 hours implementation. Methodology pure; matches AVE-Core's existing JAX autodiff infrastructure. Whether to land in this session or defer to Round 7 is Grant's adjudication.

### 13.5g F17-K v3 (i) X4b linear-stability test — empirical detail (commit `3fede52`)

**Authority:** [doc 34_ §X4b](34_x4_constrained_s11.md) X4b methodology + auditor 2026-04-25 ("v2-v2 was global-flow data, not strict linear-stability data; need rigorous X4b extended to coupled engine").

**Implementation** (~150 LOC in `coupled_s11_eigenmode.py::run_v3_x4b_linear_stability`):

1. Initialize coupled engine state EXACTLY at Golden Torus (R=20, r=R/φ²=7.64)
2. Project ω onto saturation manifold (peak |ω| = 0.94 = 0.3π)
3. Add δ = 1% random perturbation to (V_inc, u, ω)
4. Run `relax_with_pin` for n_iter=30 with hard projection on saturation manifold
5. Compute `δ_final / δ_initial` ratio + per-iter growth rate
6. Classify: STABLE (δ_ratio < 1), MARGINAL (1 ≤ δ_ratio < 3), UNSTABLE (δ_ratio ≥ 3)

**Empirical result table:**

| Objective | verdict | δ_ratio | growth/iter | R drift | r drift | c_cos preserved | peak \|ω\| pinned |
|---|---|---|---|---|---|---|---|
| Cosserat-energy | MARGINAL | 1.81× | +0.0198 (slow) | 4.88% | 0.00% | 3 ✓ | 0.94 ✓ |
| coupled S₁₁ | UNSTABLE | 5.31× | +0.0556 (exponential) | 4.88% | 0.00% | 3 ✓ | 0.94 ✓ |

**Notes:**
- r drift 0.00% is a lattice-binning artifact per [doc 67_ §18.1](67_lc_coupling_reciprocity_audit.md) — minor radius lattice-discretization steps below detection floor
- R drift 4.88% identical between objectives = single-lattice-unit detection step
- Both descents drift in geometry while preserving topology + amplitude — Golden Torus is **topologically + amplitude pinned but GEOMETRICALLY UNSTABLE**

**Combined with global-flow result from `4c9fbea`** (Phase 5c v2-v2):

| Test | Type | Result |
|---|---|---|
| Phase 5c v2-v2 | Global gradient flow (n=78-500 iters from Golden Torus seed) | Both objectives drift to non-φ² stationary points (R/r=3.40 / 1.03) |
| v3 (i) X4b | Linear stability (1% perturb, 30 iters) | Energy MARGINAL (1.81×); S₁₁ UNSTABLE (5.31×) |

**Both tests at different scales agree.** Doc 03_ §4.3 fully empirically anchored at both global-flow and linear-stability levels.

**Methodology consequence (per [doc 67_ §26](67_lc_coupling_reciprocity_audit.md)):** the coupled engine has NO linearly stable bound state at Golden Torus geometry under either objective. Phase 6 sparse eigensolver methodology becomes load-bearing for finding the (2,3) eigenmode at fixed cavity geometry without requiring dynamical stability. See A32 in §17.1 for the structural finding.

### 13.5h Bootstrap-chain test — Q = 1/α = 137.036 algebraically validated; bare K4 ≠ LC tank empirically (commit `c830f07`)

**Authority:** auditor 2026-04-25 — *"single-bond Q is bootstrap-chain calibration that should anchor any further numerical claim, regardless. ~30 min cost asymmetry vs Phase 6."* + Vol 1 Ch 1:18 unknot derivation + Vol 4 Ch 1 LC-tank Q=1/α + doc 16/17 Q-factor reframe.

**Two tests run** at the AVE-fundamental "electron plumber" level — what does an engineer do to model an O₁ unknot?

**Test A — single-bond simulation** (`single_bond_q_test.py`, ~150 LOC):

Bare `K4Lattice3D` at N=8, no PML, V_inc = 0.05 on one A-B bond at center, run scatter+connect 200 steps. Expected per Vol 4 Ch 1: peak resonance at Compton period (natural units 8.89 steps).

**Result:** peak resonance period = 2.0 steps (Nyquist limit), expected = 8.89 steps, off by 4.4×. Trajectory shows step-by-step alternation (step 0: V_inc[A]=0.05, V_inc[B]=0; step 1: V_inc[A]=0, V_inc[B]=-0.025; step 2: V_inc[A]=0.0125, V_inc[B]=0; ...). This is the **K4-TLM scatter+connect inherent 2-step grid structure** (wave shuttling A↔B at lattice c), NOT Compton-frequency oscillation.

**Structural finding:** **bare K4 ≠ LC tank.** The Vol 4 Ch 1 LC tank model is a CONTINUUM analog. L_e (kinetic inductance from electron mass) emerges from the Cosserat sector via constitutive moduli (G, K, ρ_inertia). Bare K4 has no L parameter at the bond level — only C and wave propagation. **Compton resonance ω = 1/√(L·C) requires BOTH sectors active.**

⟹ **The "simplest unknot O₁" in AVE is NOT a bare K4 lattice bond. It is the smallest COUPLED (K4 + Cosserat) oscillator.** New finding A33 in §17.1.

**Test B — constants-level scalar verification** (`bootstrap_constants_check.py`, ~120 LOC):

Compute L_e, R_TIR, Q from SI input constants; verify corpus algebraic identities.

**Identity 1:** ω_C·L_e =? ℏ/e²
- ω_C·L_e = 4108.236 Ω
- ℏ/e² = 4108.236 Ω (Klitzing/2π)
- **rel_err = 4.43e-16  ✓ MACHINE PRECISION**

**Identity 2:** Q =? 1/α
- Q = ω_C·L_e / R_TIR = 137.036
- 1/α (CODATA) = 137.036
- **rel_err = 6.53e-11  ✓ MACHINE PRECISION**

⟹ **Q = 1/α = 137.036 holds ALGEBRAICALLY as identity-from-input-constants.**

Algebraic chain (tautologically consistent):
```
ℓ_node = ℏ/(m_e·c)
ξ_topo = e/ℓ_node = m_e·c·e/ℏ
L_e    = ξ_topo⁻²·m_e = ℏ²/(c²·e²)
ω_C·L_e = (m_e·c²/ℏ) · ℏ²/(c²·e²) = ℏ/e²
Q       = (ℏ/e²) / (Z_0/(4π)) = 4πℏ/(e²·Z_0) = 1/α
```

**Bootstrap-chain status: PASS.** Test A confirms bare K4 behaves as expected (not as Compton LC tank). Test B confirms corpus algebraic chain is self-consistent at machine precision. Q = 137 in AVE is a definitional identity chained through SI input constants, not an empirical lattice measurement.

**Implication for F17-K v3 path:** the auditor's decision tree applies cleanly:
- Q = 137 holds at constants level ⟹ bootstrap is well-grounded
- Bare K4 ≠ LC tank ⟹ empirical Q manifestation requires coupled engine
- F17-K v3 (i) showed coupled-engine Golden Torus is UNSTABLE
- ⟹ Phase 6 sparse eigensolver methodology remains corpus-canonical next step (Helmholtz acoustic-cavity framing per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md))

Empirical Q manifestation in lattice dynamics is F17-K's open work, NOT bootstrap-chain calibration concerns. Both useful, separate concerns per auditor framing.

### 13.5i Phase 5 resume — ansatz-seeded driver case (b') + G-13 activation (commits `01bbec3`, `ede4008`, `e1f6eac`)

**Authority:** [doc 70_ phase5_resume_methodology.md](70_phase5_resume_methodology.md) (NEW r8.6) + Round 6 finding "topology can be encoded via ansatz initialization" + [VACUUM_ENGINE_MANUAL §9 G-13 contingency](#) + [doc 51_ §5 H1/H2/H3 hypotheses](51_handoff_followups.md).

**Round 6 closure motivated Phase 5 PairNucleationGate resumption.** Per Grant 2026-04-25 directive: *"single-electron precondition was methodology gap, now characterized; topology can be encoded via ansatz initialization in pair-nucleation context too."* This decouples three orthogonal questions (per [doc 70_ §3](70_phase5_resume_methodology.md)) that were conflated in the pre-Round-6 registered Phase 5 driver:

- **(α) Does the gate mechanism work?** — would fire given C1∧C2 satisfied by construction
- **(β) Does the seeded pair persist post-drive?** — Kelvin topological-protection claim
- **(γ) Does C1/C2 get reached under drive?** — original Phase 5 question (pre-Round-6 driver gave NO-FIRE: max A²=0.75-0.91 vs sat_frac=0.95)

Pre-Round-6, all three were conflated. Post-Round-6 ansatz-seeded driver isolates (α)+(β) from (γ).

**Empirical result** (commit `ede4008`, `phase5_pair_nucleation_ansatz_seeded.py`):

Seeded Beltrami-bound-pair at central A=(10,10,10), B=(11,11,11), port 0. Registered config: N=24, amp=0.5·V_SNAP, λ=3.5, head-on autoresonant collision.

Drive-on result:
- |ω|_A: 1.414 → 0.013 (drive-end, 0.01×) → 0.091 (post-drive, 0.06×)
- |ω|_B: symmetric (same trajectory)
- Φ_link: +1.000 → +0.998 → +1.000 (constant)
- Other-bond firings: 0 (no cascade)
- c_cos final: 1, peak |ω|_global: 0.091

**No-drive sanity check** (essential for clean adjudication):
- step 0 (seed): |ω|_A = 1.4142
- step 1: |ω|_A = 0.1023 — **93% loss in ONE step**
- step 5-100: |ω|_A oscillates 0.05-0.85 chaotically
- Φ_link constant +1.000 throughout

**⟹ Dissolution is INTRINSIC to engine self-dynamics, NOT drive-induced.** Drive is irrelevant. Velocity-Verlet kick step alone scatters 93% of seeded ω in one step.

**Two findings:**

**(b') Gate's `_inject_pair` profile is fundamentally unstable.** Point-rotation Beltrami + Φ_link configuration has no mechanism to maintain localized ω structure under Cosserat self-dynamics (k_op10, k_hopf, k_refl auto-suppressed under A28 per `enable_cosserat_self_terms=True`). **This is the SAME PHYSICS as F17-K Round 6 finding** for the (2,3) electron at coupled scale — Cosserat ω hedgehog dissolves at step ~11 (Round 6 single-electron); manifests at the pair scale here in 1 step instead of 11 (smaller, less-protected configuration → faster dissolution). Same root: dynamics don't stabilize unprotected localized topology; topology must be encoded as persistent structural feature (ansatz).

**Φ_link "persistence" is a measurement artifact.** Reads exactly +1.000 throughout drive AND no-drive runs. Per A29 (commit `a53ce1c`, [doc 67_ §17-§18](67_lc_coupling_reciprocity_audit.md)): Φ_link is a derived flux observable in K4-TLM, not a primary dynamical state. Direct seeding leaves a value that doesn't couple to V_inc evolution. **NOT Kelvin topological-protection at work** — K4 dynamics simply don't touch this slot under bare-K4 seeding.

**Adjudication: case (b').** Gate's INJECTION PROFILE needs upgrade, NOT C1/C2 threshold logic. Empirically activates **VACUUM_ENGINE_MANUAL §9 G-13 contingency**:

> *"if Beltrami pair dissipates faster than 10 Compton periods post-drive, upgrade to localized Hopf fibration or (2,3) torus-knot injection."*

Pre-Round-6 plan deferred this upgrade behind "test point-rotation first." Test now empirically run; G-13 activated. New finding A34 in §17.1.

**R5.10 Readings 1-4 status — two-level disambiguation** (per `e1f6eac` doc 70_ §7.5 clarification):

- **PRE-EMPTED at original Round 5 framing.** The four Readings (Compton-lock-is-rupture, PLL-chirps-past-lock, drive-health-boolean, parity-chirality-coincidence) argued about how to INTERPRET C2 under ambiguous threshold satisfaction. The ansatz-seed approach made thresholds unambiguous-by-construction, retiring the interpretation debate at this level.
- **MAY REOPEN at threshold-revision level** (different epistemic level, not the same question) — once topologically-protected injection profile (Hopf fibration or (2,3) torus-knot per G-13) is implemented and tested, C1/C2 thresholds may need revision to suit the new injection profile (what saturation level is "sufficient" for topologically-protected pairs vs point-rotation pairs).

Two separate questions at two epistemic levels — neither "dead" nor "pending in original form."

### 13.5j Round 7 candidates — scoped, deferred to fresh sessions (r8.6)

Round 6 + Phase 5 resume close discipline-completely. Round 7 has two scoped Stage candidates per the Round 6 closure framework:

**Round 7 Stage 1 — F17-K Phase 6 sparse eigensolver methodology** (~300 LOC).
- Linearize coupled K4+Cosserat dynamics around Golden Torus ansatz
- Build sparse Jacobian via JAX autodiff
- Use `scipy.sparse.linalg.eigsh` to extract (2,3) eigenmode at fixed cavity geometry
- Eigenvalue problem `Au = λBu` doesn't require dynamical stability — addresses A32 (Golden Torus geometrically unstable under both descents at linear-perturbation level)
- Acoustic-cavity / Helmholtz framing per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md) provides corpus-canonical motivation
- AVE-Core doesn't currently use sparse eigensolvers for the (2,3) electron — genuine new methodology
- **Scope:** ~300 LOC, ~3-4 hours, fresh session, properly preregistered predictions

**Round 7 Stage 2 — phase5_topological_pair_injection.py** (~200 LOC).
- Replace gate's point-rotation Beltrami `_inject_pair` profile with topologically-protected (2,3) torus-knot or Hopf fibration injection
- Chirality-matched (LH at A, RH at B) per [doc 54_ §2](54_pair_production_axiom_derivation.md) and AVE-Propulsion Ch 4 chiral impedance matching
- Reuse F17-K infrastructure (saturation pin from `relax_with_pin`; phase-coherence diagnostic from doc 68_ Phase 1)
- Empirically motivated by A34 (point-rotation Beltrami dissolves in 1 VV step; G-13 upgrade required)
- **Scope:** ~200 LOC new driver, ~2-3 hours, fresh session

**Both Round 7 candidates deferred to fresh sessions per the plan; this session closes Round 6 + Phase 5 resume cleanly. Round 7 Stages 1+2 are independent — can run in either order or in parallel.**

### 13.5k Round 7 Stage 0 basin-audit RETRACTED + R7.1 strengthened to multi-seed sparse eigensolver (commits `1bc1652`, `c69e79c`)

**Authority:** [doc 71_ multi_seed_eigenmode_sweep.md](71_multi_seed_eigenmode_sweep.md) §13 + frozen `predictions.yaml` `P_phase6_eigensolver_multiseed` + within-session self-audit triggered by Grant directive 2026-04-25 ("review COLLABORATION_NOTES, are you trapped in known patterns?").

**Backstory.** Between r8.6 close and R7.1 fresh-session implementation, an intermediate framing emerged: "Round 7 Stage 0 — basin audit as precondition for R7.1 + R7.2." Driver scaffold landed (`1bc1652`, `phase5_basin_audit.py` + `71_basin_audit_methodology.md` + `P_basin_audit_GT_stationarity` pre-registration; v1 run halted by A26 amplitude-guard at step 0 — geometry bug surfaced rather than basin-mapping data collected). Mid-cycle, agent re-read [COLLABORATION_NOTES.md](.agents/handoffs/COLLABORATION_NOTES.md) Rules 6/8/10 against own work and self-audited the Stage 0 framing as a multi-rule violation. Reframe pivot landed in `c69e79c`.

**The three rule violations:**

1. **Rule 6 (SM/QED minimization framing on a substrate that does wave propagation).** TDI gradient descent on the Cosserat W functional finds *static* configurations where ∂W/∂(u, ω) = 0. The corpus-canonical concept for a bound state is a *dynamic* standing-wave eigenmode of the coupled K4+Cosserat dynamics — found via the Helmholtz / acoustic-cavity formulation per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md). A W stationary point isn't necessarily an eigenmode at ω_Compton; an eigenmode isn't necessarily a stable basin minimum. The basin audit was answering a related-but-distinct question and dressing it as the Stage 0 precondition imported a SM-style framing onto a wave substrate.

2. **Rule 8 inverse (assuming AVE doesn't have a native tool when it does).** R7.1 IS the AVE-native tool for the bound-state question. By framing Stage 0 as a basin audit rather than running R7.1 at multiple seed geometries, the agent bypassed the corpus-blessed methodology and built parallel infrastructure using gradient descent. R7.1 at GT + F17-K endpoints would directly answer the linearization-point question without an intermediate basin step.

3. **Rule 10 corollary (creeper compound carried forward without pressure-test).** "Basin audit as Stage 0 precondition for R7.1" carried across multiple turns: initial diagnosis → external auditor confirmation (same-source bias — auditor was reviewing the framing on the framing's own terms, not challenging the framing itself) → v1 build → v1 fail → v2 draft. Each cycle pressure-tested implementation details, never the framing. Auditor explicitly owns same-source bias contribution in [STAGE6_V4_HANDOFF.md](.agents/handoffs/STAGE6_V4_HANDOFF.md) §R7.3 + this section.

**Reframe deliverables:**

- **doc 71_ renamed and reframed:** `71_basin_audit_methodology.md` → `71_multi_seed_eigenmode_sweep.md`. §1-§12 RETAINED per Rule 12 (audit-trail preservation) — they record the basin-audit framing, v1 fresh-session run halted by A26 guard, v2 draft never executed. §13 ACTIVE (multi-seed R7.1 sparse eigensolver). §14 driver scope notes for fresh-session implementer.
- **`predictions.yaml` reframe:** `P_basin_audit_GT_stationarity` retained-with-RETRACTED-marker per Rule 12 body preservation; `P_phase6_eigensolver_multiseed` NEW with frozen pre-registration (N=32, R_anchor=10, four seeds, three-mode falsification, ω_Compton ± α tolerance, Q ± 5% tolerance, shape correlation > 0.85 vs doc 34_ X4a profile).
- **R7.1 strengthening (single-seed → multi-seed):** original §13.5j Round 7 Stage 1 scope was "extract (2,3) eigenmode at fixed cavity geometry" — implicitly GT-only. r8.7 strengthens to four seeds at the SAME run: `GT_corpus` (R=10, r=10/φ²≈3.82); `F17K_cos_endpoint` (R=10, r=10/3.40≈2.94, F17-K v2-v2 Cosserat-energy descent endpoint per `4c9fbea` / [doc 67_ §25](67_lc_coupling_reciprocity_audit.md)); `F17K_s11_endpoint` (R=10, r=10/1.03≈9.71, F17-K v2-v2 coupled-S₁₁ descent endpoint per same source); `vacuum_control` (random low-amplitude, peak |ω|=0.05 — negative control for eigensolver methodology bug detection). Lattice forced to N=32 because F17K_s11 r≈9.71 won't fit at N=24 alive halfwidth=8 (N=32 alive halfwidth ≈ 12 accommodates all three).

**Three-mode falsification structure (per Grant directive, frozen in `P_phase6_eigensolver_multiseed`):**

- **(I) `GT_corpus` passes** (with or without F17K endpoints also passing): corpus Golden Torus geometry empirically vindicated as the engine bound-state location at coupled scale. F17-K v2-v2's R/r=3.40 and 1.03 were dynamical-descent artifacts (different objectives, different gradient-flow attractors); the spectral bound state is at corpus GT. R7.1 closes as originally scoped.
- **(II) F17K_cos and/or F17K_s11 passes; `GT_corpus` fails:** engine bound state is at the F17-K v2-v2 attractor geometry, NOT at corpus GT. Corpus geometric claim (R·r=1/4, R/r=φ²) empirically wrong AT COUPLED-ENGINE SCALE. Engine W or corpus geometry derivation needs revision. Major framework-level finding.
- **(III) No seed passes:** the (2,3) topological representation as currently implemented in `cosserat_field_3d.py` does not host a bound state at ω_Compton at any tested geometry. Either the (2,3) ansatz is structurally wrong (winding, amplitude scaling, field sector — bound state lives in K4 V_inc rather than Cosserat ω) or coupled K4+Cosserat dynamics needs additional terms. Round 8 architectural rework.
- **Negative-control failure:** if `vacuum_control` returns a nontrivial eigenmode at ω_Compton (which (I)/(II)/(III) all expect it NOT to), the eigensolver itself is broken (sparse Jacobian assembly bug or continuum-mode misidentification). Methodology issue, not physics finding — re-check Jacobian assembly before interpreting (I)/(II)/(III).

**v1 basin-audit results status:** RETAINED as informational empirical context (not Stage 0 precondition). v1 was halted by A26 amplitude-guard at step 0 — no post-step empirical content collected; the only "data" is methodology-failure (geometry bug surfaced, A26 guard validated as sentinel). If R7.1 multi-seed returns mode (III), v1's basin-audit *informational* question may be revisited at corrected geometry as Round 8 diagnostic — but it's not on the critical path. `phase5_basin_audit.py` driver remains in repo (commit `1bc1652`) for that contingency only.

**Auditor flag (open at r8.7 close, fresh-session implementer responsibility):**

- **§14.2 K4-amplitude-zero pitfall is load-bearing for mode (III) interpretation.** Op14 z_local is multiplicative in V_inc, so a Jacobian linearized around a state with V_inc=0 has zero K4↔Cosserat off-diagonal blocks at first order. The eigensolver returns Cosserat-only modes; a "no eigenmode at ω_Compton" result then reads as mode (III) ("structural rework, Round 8") when the actual cause is methodology. Fix is to include the second-order cross-block ∂²W/∂V_inc∂ω evaluated at the seed (nonzero since ω≠0). Doc 71_ §14.2 flags this; r8.7 elevates to mandatory **Jacobian-block sanity check** in driver — print/log K4↔Cosserat off-diagonal block norms before running `eigsh`; halt-and-flag if zero. Cheap insurance against the most consequential interpretation failure mode.
- **Shape-correlation > 0.85 PASS gate may over-strict.** Doc 34_ X4a profile is from a Cosserat-only run pre-coupling. Coupling could distort the bound-state shape; a real coupled-system eigenmode at ω_Compton with Q=137 but shape correlation 0.78 against pre-coupling X4a would FAIL the conjunction. Fresh-session implementer should record correlation as informational measurement and flag for Grant adjudication if (ω_Compton + Q pass) ∧ (shape correlation < 0.85). Three pass-criteria as written has a meaningful false-FAIL risk that contaminates three-mode resolution.

**A35 audit finding** in §17.1 — Rule 6/8/10 violation framing tied to **A22** (inline operators duplicate canonical universals — corpus-bypass at the operator level) and **A30** (corpus-duality falsification — corpus claim of energy ≈ S₁₁ co-locate at GT, falsified empirically at coupled scale). All three are corpus-bypassing errors at different layers; A35 was caught earlier in the cycle (within-session self-audit triggered by Grant directive) than A22 or A30. **Methodology lesson (recorded in COLLABORATION_NOTES Rule 8 strengthening for next session):** before scaffolding a "diagnostic precondition" upstream of an existing R7.x stage, grep the corpus for the AVE-native tool that addresses the precondition's question; if it exists, strengthen R7.x's scope rather than building parallel infrastructure.

### 13.5l Reframe 3 — block Helmholtz on joint (V, ω) replaces Hessian-of-W (commit `675141e`)

**Authority:** [doc 72_ vacuum_impedance_design_space.md](72_vacuum_impedance_design_space.md) §1-§8 + frozen `predictions.yaml` `P_phase6_helmholtz_eigenmode_sweep` + external audit on commit `c69e79c`.

**Trigger.** External audit on r8.7's frozen `P_phase6_eigensolver_multiseed` (Hessian-of-W multi-seed sparse eigensolver) caught a deeper Rule 6 instance: Hessian-of-W is itself an SM/QM-style energy-stationarity framing on a wave-propagation substrate. The basin-audit retraction in r8.7 caught Rule 6 at the *precondition* level (basin = energy minimum, vacuum substrate is wave); reframe 3 catches Rule 6 at the *operator* level (Hessian-of-W = stationary point of W; vacuum substrate is wave). Same-gap finding, deeper layer.

Grant directive 2026-04-25: *"I'm open as long as you understand the design/solution space that ave dictates"* + *"What's the smith chart for the vacuum? is it 3D?"* — invited design-space articulation BEFORE further pre-registration drafting. Doc 72_ is the response.

**Doc 72_ §1-§4 — the four AVE-native concepts (corpus-grounded conceptual scaffolding):**

1. **Wave eigenmode (Helmholtz / TLM-scattering — NOT Hessian-of-W).** K4-TLM lattice runs wave propagation, not energy minimization (per [COLLABORATION_NOTES.md:65](.agents/handoffs/COLLABORATION_NOTES.md) 2026-04-20 second observation). Bound state is an eigenmode of the wave operator, not a stationary point of an energy functional. Helmholtz form per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md): `∇·(z(x)·∇V) + k²V = 0` with z(x) Op14-modulated. Critical implementation consequence: V is the eigenvector OUTPUT of eigsolve, not a seed INPUT. Collapses the K4-amplitude-zero Flag A entirely.

2. **Impedance match (S₁₁ minimum — NOT energy minimum).** Bound-state physical condition is `Γ ≈ -1` at cavity wall (TIR for inward-traveling wave), AVE EE-native. F17-K Phase 5c-v2-v2 dual-descent established empirically that energy and S₁₁ have different stationary states (R/r=3.40 vs 1.03), neither at corpus φ²=2.62 — the bound state is at neither alone but at the intersection where wave equation has eigenmode AND impedance match holds AND topology is preserved.

3. **Topological quantization (input via ansatz — NOT dynamical attractor).** Per [doc 03_ §4.3](03_existence_proof.md): R·r=1/4 is topologically quantized, NOT dynamically derived. Selected by ansatz initialization, not gradient flow. F17-K v2-v2's failure to converge to GT under either objective IS the corpus prediction holding — neither objective KNOWS about topological quantization.

4. **AVE basin = S₁₁ minimum, NOT W minimum.** "Basin" terminology is protein-folding lingo (Ramachandran 2D dihedral space, real attractors of energy landscape per [AVE-Protein `protein_fold.py:260-326`](../../../AVE-Protein/src/ave_protein/regime_2_nonlinear/protein_fold.py)). The vacuum-side analog is S₁₁-min descent, NOT W-min. Retracted v1 `P_basin_audit_GT_stationarity` imported protein-folding "basin" terminology AND framed it on Cosserat W functional — two errors compounded.

**Doc 72_ §2 — the 3D Smith chart for the vacuum.** Standard EE Smith chart `Γ = (Z−Z₀)/(Z+Z₀)` with `Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω` is 2D. Three natural 3D extensions:
- **Extension A (RECOMMENDED for R7.1):** `(Re(Γ), Im(Γ), ω)` frequency-trajectory chart. Sweep ω at fixed cavity geometry; bound-state resonance is where trajectory crosses Γ=-1.
- **Extension B:** `(Re(Γ), Im(Γ), A²)` saturation-trajectory (Op2 saturation behavior visible).
- **Extension C:** `(R, r, ω)` resonance-surface volume (geometry-trajectory).

4D extension (chirality `h_local` axis) load-bearing for parity-violation + R7.2 chiral-pair-injection but NOT for R7.1's bound-state-existence question.

**Doc 72_ §3.1 — block Helmholtz formulation (per audit Q1 hybrid-coupled-mode pushback).** Original draft of §3.1 had single-sector V Helmholtz on Cosserat backdrop; audit Q1 noted [doc 66_ §17.2](66_single_electron_first_pivot.md) three-storage-mode reading describes bound electron as co-evolving across V and ω sectors on equal footing. Single-sector Helmholtz misses hybrid coupled modes.

Reframe response — **block Helmholtz on joint (V, ω) state**:

```
[ K_V       C_Vω ] [V]        [ M_V    0   ] [V]
[ C_ωV     K_ω   ] [ω]   = ω² [ 0      M_ω ] [ω]
```

Same generalized eigenvalue form Au=λBu, bigger matrix (~12·N³ at N=32 ≈ 393K, tractable for `eigsh`). Cross-blocks `C_Vω`, `C_ωV` encode Op14 K4↔Cosserat coupling explicitly, not approximated as static.

**§3.1.1 V=0 decoupling caveat (per audit footnote):** at V=0 seed (no V_inc seeded), `C_ωV` vanishes — multiplicative in V. Block eigenvalue problem decouples into independent V-block + ω-block problems at the seed. This is the desired behavior — eigsolve at one V=0 seed run returns BOTH sector candidates simultaneously, exposing where the bound state lives. What block Helmholtz at V=0 CANNOT find: genuinely hybrid (V, ω) modes that REQUIRE V≠0 to exist as resonances. Round 8 question if R7.1 mode (III) returns AND there's evidence to pursue hybrid-coupled rather than architectural rework.

**Doc 72_ §3.3 — topological crossing-count + shape correlation as two-tier (per audit Q4):** `c_eigvec = 3` binary PASS criterion (topologically invariant under continuous deformation, robust against coupling-induced shape distortion); shape correlation > 0.60 informational diagnostic. Two-tier: hard binary on c_eigvec, informational on shape match. ~20 LOC informational diagnostic.

**Doc 72_ §3.4 — sector-energy split diagnostic (per audit Q1):** at each eigenmode found at ω_Compton, compute V-fraction vs ω-fraction of total energy. Identifies V-dominant / hybrid / ω-dominant mode character. Informational, not PASS.

**Doc 72_ §5 — LOC budget revised: ~290 LOC** (was 250 in original §5; +20 Q4 shape correlation informational, +10 Q1 sector-energy split, +10 Helmholtz operator integrity check). Single fresh-session.

**§6.1 Rule 10 commitment language (verbatim from doc 72_ §6.1 — implementer hits it twice):**

> **This is reframe 3 of R7.1 in one session arc:** single-seed Hessian (r8.5 forecast) → multi-seed Hessian (r8.7, frozen as `P_phase6_eigensolver_multiseed` at commit `c69e79c`) → multi-seed block Helmholtz on (V, ω) joint (this doc, proposed as `P_phase6_helmholtz_eigenmode_sweep`). Each reframe was substantive and corrected a real upstream error caught by audit or self-audit. None has been run.
>
> **The fresh-session run committed against the v2 pred is committed to operator choice.** Per [COLLABORATION_NOTES Rule 10](.agents/handoffs/COLLABORATION_NOTES.md): *"empirical drivers catch what static analysis + preregistration misses; data first, methodology adjustments after."* If the run hits unexpected behavior, the discipline says: produce empirical data first, analyze the data, then methodology revisions if needed — not pre-emptive reframe 4.
>
> **The ONLY pre-emptive operator-change condition before run:** catastrophic methodology error surfaced by audit or external review. "Catastrophic" means: a load-bearing physics error in the operator construction itself that would invalidate any result regardless of what data the run produces. Anything less than that goes through the empirical-data-first pipeline.

**Reframe deliverables (single commit unit `675141e`):**

- doc 72_ NEW (~26 KB, §1-§8 + §3.1.1 V=0 footnote + §3.4 sector-energy diagnostic + §6.1 commitment language)
- doc 71_ §13 RETRACTED per Rule 12 (body preserved); §14 superseded driver scope notes preserved; **§15 ACTIVE** multi-seed block Helmholtz with quick-map vs §13 + read-order for fresh-session implementer
- `predictions.yaml`: `P_phase6_eigensolver_multiseed` retains-with-RETRACTED-marker (Rule 12); `P_phase6_helmholtz_eigenmode_sweep` NEW frozen with full block-structure description, V=0 decoupling caveat, four-seed list, binary PASS + informational diagnostics (sector-energy split + shape correlation > 0.60), three-mode falsification, Rule-10 commitment baked in

**Three-mode falsification reading (extended with sector sub-readings per §3.1.1):**

- **(I) `GT_corpus` returns eigenmode at ω_Compton ± α with c_eigvec=3 + Q within 5% of 1/α.** Sub-reading from sector-energy split: V-dominant ⟹ K4 wave on Cosserat backdrop framing vindicated; ω-dominant ⟹ Cosserat-sector bound state per doc 66_ §17.2 vindicated; hybrid ~50/50 ⟹ both mechanisms active. Corpus Golden Torus geometry vindicated either way.
- **(II) F17K endpoint returns eigenmode at ω_Compton; GT_corpus does not.** Engine bound state is at F17-K v2-v2 attractor geometry, NOT corpus GT. Corpus geometric claim (R·r=1/4, R/r=φ²) empirically wrong at coupled-engine scale.
- **(III) No seed passes.** No V-block OR ω-block eigenmode at ω_Compton at any tested geometry. Round 8 architectural rework. First sub-question: hybrid coupled mode requires V≠0 seed (block Helmholtz at V=0 cannot find it; needs separate test).
- **Negative-control failure:** `vacuum_control` returns nontrivial eigenmode at ω_Compton ⟹ eigensolver/operator-assembly bug, not physics finding.

**A36 audit finding** in §17.1 — operator-choice Rule 6 violation (Hessian-of-W on wave substrate). Family with **A22** (inline operators at operator level) + **A30** (corpus-duality falsification) + **A35** (basin-as-Stage-0 framing). Same-gap instances at progressively earlier cycle latency: A22 multi-session retroactive → A30 one-session post-empirical → A35 within-session pre-implementation → A36 within-session via external audit on prior commit. Pattern indicates audit-first + creeper-checking + design-space articulation discipline tightening across rounds.

### 13.6 Phase 6 — Headline autoresonant validation (P_phase6_autoresonant) ⏸ blocked by Phase 5 suspension

**Authority:** [54_ §8](54_pair_production_axiom_derivation.md) (prediction matrix) + AVE-Propulsion Ch 5.

**Change:** Run the final validation: does `AutoresonantCWSource` with the complete Stage 6 engine produce pair nucleations at ≥ 5× the rate of a fixed-frequency CW source at matched energy input?

**Pre-registered prediction:** ≥ 5× rate enhancement.

**Status (r8):** ⏸ BLOCKED on Phase 5 resumption, which is itself blocked on single-electron validation. No engine code changes for Phase 6 since r7.

**Effort:** 1–2 days (configs + runs) once Phase 5 resumes.

### 13.6a v4 Universal-Lattice-Units refactor (post-Stage-6 — FUTURE_WORK G-10)

**Authority:** [doc 57_](57_universal_lattice_units_v4_refactor.md).

**Scope:** post-Stage-6 structural refactor. Not to run in parallel with Phase 4–6 (explicit §6.3 risk call in doc 57_). 2–3 weeks estimated, phased v4.0–v4.5.

**Core claim:** AVE's axiom-native state is **dimensionless `r = A/A_c` everywhere**, with `A_c` a *derived domain property* not an engine parameter. The engine currently violates this via:
- Hardcoded regime boundaries at [vacuum_engine.py:151–153](../../src/ave/topological/vacuum_engine.py#L151).
- Hand-rolled saturation / impedance / reflection inline at [k4_tlm.py:227, 256, 333](../../src/ave/core/k4_tlm.py#L227) — duplicates of `universal_saturation`, `universal_dynamic_impedance`, `universal_reflection`.
- Mixed-convention A²_total in three observers (A14).
- No per-engine single-source-of-truth method for `r²`.

**v4 deliverables:**
- New operator `universal_regime_classifier(r_sq) -> Regime[]` in `universal_operators.py`.
- Engine methods `r_squared_K4()`, `r_squared_cosserat()`, `r_squared_total()`, `regime_at_each_site()` — canonical source.
- All observers route through these methods. No ad-hoc sums.
- Cross-scale regression suite `test_scale_invariance.py` — same operators, different A_c, correct physics in subatomic / macroscopic / gravitational / BCS domains.
- Cosserat moduli audit: derive `G`, `γ`, `ρ`, `I_ω`, `ε_yield`, `ω_yield` from axioms (Option 1) or document as placeholder with citations (Option 2).

**What v4 does NOT do** (doc 57_ §11):
- Does not add physics.
- Does not improve pair-creation predictions.
- Does not close A2 (Pythagorean test), A5 (A²>1 varactor), A7 (linear-Taylor). Closes A1, A14 structurally.
- Does not replace Stage 6 — it's the post-kill-switch cleanup.

**v4 handoff precondition (doc 57_ §8):** R4 patched + committed, Phase 4–6 complete, doc 56_ written, FUTURE_WORK G-10 exists, manual at r4+. **G-10 is not yet entered in FUTURE_WORK.md** — doc 57_ itself is the spec proposing it.

### 13.7 Total Stage 6 scope (updated r8 — Round 6 pivot)

| Phase | Status | Effort | Risk |
|---|---|---|---|
| 0 — Axiom derivation doc 54_ | ✅ Landed (2026-04-22) | Done | — |
| 1 — V_SNAP/V_yield test + predictions manifest | ✅ Landed (a0f50ed) | Done | — |
| 2 — NodeResonanceObserver | ✅ Landed (719f3ec) | Done | — |
| 3 — Φ_link bond state | ✅ Landed (`3a599ca`) | Done | Regression clean (940 → 954 pass). |
| 3.5.A/B — R4 patches + docs | ✅ Landed (`6e355d1`, `224cad0`) | Done | `/α` removed from Node/Bond observers; 955 → 965 pass; doc 50_ r3 + doc 55_ R4 banner + doc 57_ all committed. |
| 4 — Asymmetric saturation | ✅ Landed (`a5bd1da`) | Done | S1 reopen adjudicated (1A / 2-II / 3c); 965 → 983 pass; P_phase4_asymmetric mechanism validated. |
| G-12 — AutoresonantCWSource axiom-native varactor PLL | ✅ Landed (`aa7a337`) | Done | Closes A7. δ_lock = ω₀·α now reachable. |
| A10 — Thermal equipartition validation | ✅ Landed (`2e3abcf`) | Done | 23 tests, biggest systemic coverage gap closed. |
| G-11a — SpatialDipoleCPSource | ✅ Landed (`5c3f2d1`) | Done | CP V_inc via dipole modulation (13 tests). |
| G-11c — CosseratBeltramiSource | ✅ Landed (`e17b8cd`) | Done | Direct-ω chirality driver (18 tests). |
| 5 — PairNucleationGate | ⏸ Landed (`9ecc2ca`+`3f9569b`) but SUSPENDED in Round 6 | — | Gate code in HEAD; firing blocked on single-electron precondition per doc 66_. |
| 5.5 — Cosserat-sector PML | ✅ Landed (`03cb9d5`, doc 58_) | Done | Ax1+Ax3-forced boundary radiation absorber. |
| 5.6 — Memristive Op14 (K4 sector) | ✅ Landed (`49917ff`, doc 59_) | Done | Opt-in dynamical S(t) per dS/dt = (S_eq − S)/τ_relax with τ_relax = ℓ_node/c. |
| 5.7 — BH-entropy adjudication (docs 60–65) | ✅ Closed | Done | Three distinct entropies; doc 64 derives area theorem from Ax1+Ax4; first law remains imported (Flag 62-A open). |
| 5e — Cool-from-above driver + Flag-5e-A fix | ✅ Landed (`1805d14`, `098d430`) | Done | First empirical cool-through-yield; S drops 1.0 → 0.507 → 0.983. |
| **Round 6 — Single-electron-first pivot** | 🔄 ACTIVE (doc 66_, doc 67_, doc 68_) | gated on v3 (i) algebraic Ch 8 pin OR v3 (ii) Phase 6 eigensolver | Path A FALSIFIED (`fbbc950`). F17-I three-mode tested (`687b18d`) → A27. F17-H L_c reciprocity audit (`abe23ea`-`85bdb6f`) → A28 double-counting found, path-1 EMF retracted. A28 fix landed (`05b130f`). Cosserat self-terms re-enabled with smart auto-suppress (`ff15c4b`). **r8.3 "Path B forms bound state through step 20" claim WALKED BACK in r8.4** — twice-confounded (wrong observable + wrong amplitude). F17-K methodology arc (`a53ce1c`-`4c9fbea`, 7 commits) closes empirically: **doc 03_ §4.3 validated** — Cosserat-energy and coupled-S₁₁ each have continuous (2,3) stationary-state families; topology (SU(2) half-cover) selects Golden Torus from them, neither dynamical descent reaches it. Corpus-duality (AVE-Protein S₁₁ minimization scale-invariance) FALSIFIED at coupled-engine scale. v3 path forward: (i) algebraic Ch 8 pinning per doc 34 X4 (~80 LOC) first; (ii) sparse eigensolver per acoustic-cavity framing (~300 LOC) deferred. Strain-mask ~550 LOC infrastructure deferred — A28 was the actual gate. |
| 6 — Headline autoresonant validation | ⏸ Blocked on Phase 5 resumption | 1–2 days | Blocked on single-electron passing. |
| F17-J — Characterize all_l's pre-A28 relaxation endpoint | Deferred | TBD | May no longer be load-bearing under A28 fix; subsumed by F17-K closure. |
| F17-L — V_yield vs V_SNAP scale mismatch (doc 54 §6 vs engine, factor 1/α) | Open | — | Pre-existing per doc 54 §5; flagged in doc 67 §15. Not blocking single-electron validation. |
| F17-K — L_c reciprocity → Ax-3 noncompliance → saturation-pin → empirical doc 03_ §4.3 validation (Phase 1 + Phase 5a-c) | ✅ CLOSED 2026-04-25 (`4c9fbea`) | 6 hr / 7 commits | Methodology arc empirically closed. Corpus-duality at coupled-engine scale falsified; topology must be encoded explicitly. |
| F17-K v3 (i) X4b linear-stability test at coupled scale (`3fede52`) | ✅ RAN 2026-04-25 — Golden Torus UNSTABLE under coupled S₁₁ (5.31×); MARGINAL under Cosserat-energy (1.81×) | ~150 LOC | Confirms doc 03 §4.3 at linear-stability level alongside global-flow level. Cosserat-only X4b stability does NOT extend to coupled engine. r8.4's "v3 (i) is closure gate" framing partially walked back. |
| F17-K bootstrap-chain test (`c830f07`) | ✅ COMPLETED 2026-04-25 — Q=1/α=137 algebraically validated (rel_err 6.5e-11); bare K4 ≠ LC tank empirically; smallest unknot is coupled K4+Cosserat | ~270 LOC, ~30 min | Bootstrap chain VALIDATED at constants level. Empirical Q manifestation requires coupled engine because L_e emerges from Cosserat constitutive moduli. Auditor framing held: F17-K findings independent of single-bond Q calibration; both useful, separate concerns. |
| F17-K v3 (ii) Phase 6 sparse eigensolver | **Round 7 Stage 1 candidate (REFRAMED r8.8 to BLOCK HELMHOLTZ on (V,ω) joint)** | ~290 LOC, ~3-4 hours fresh session | r8.7 single-sector Hessian-of-W framing RETRACTED in r8.8 (`675141e`) as wrong-substrate operator (Rule 6 — Hessian = energy stationarity, vacuum substrate runs wave propagation). Reframed via doc 72_ §3.1 to **block Helmholtz on joint (V, ω) state** — generalized eigenvalue problem `[K_V, C_Vω; C_ωV, K_ω] u = ω² [M_V, 0; 0, M_ω] u` with Op14 cross-blocks explicit. Per audit Q1: addresses hybrid-coupled-mode pushback. §3.1.1 footnote: at V=0 seed, block decouples into V-block + ω-block simultaneously (strict superset of single-sector Helmholtz). PASS criteria (per audit Q4): c_eigvec=3 binary + shape correlation > 0.60 informational. Sector-energy split diagnostic (audit Q1). Frozen in `P_phase6_helmholtz_eigenmode_sweep` (doc 71_ §15 ACTIVE). Rule-10 commitment language locks operator choice for fresh-session run. |
| Phase 5 resume — ansatz-seeded driver case (b') (`01bbec3`, `ede4008`, `e1f6eac`) | ✅ EMPIRICALLY CLOSED 2026-04-25 — point-rotation Beltrami injection profile fundamentally unstable in Cosserat self-dynamics; G-13 contingency activated | doc 70_ + ~250 LOC driver + R5.10 disambiguation | Same physics as F17-K Round 6 finding for (2,3) electron at coupled scale: dynamics don't stabilize unprotected localized topology. Φ_link "persistence" disambiguated as measurement artifact per A29. R5.10 Readings 1-4 status disambiguated at two epistemic levels (PRE-EMPTED at original framing; MAY REOPEN at threshold-revision level after injection upgrade). |
| Phase 5 topological pair injection driver | **Round 7 Stage 2 candidate** | ~200 LOC, ~2-3 hours fresh session | Replace gate's point-rotation Beltrami `_inject_pair` profile with (2,3) torus-knot or Hopf fibration injection per G-13 upgrade. Chirality-matched (LH at A, RH at B). Reuse F17-K infrastructure (saturation pin, phase-coherence diagnostic). Empirically motivated by A34. Independent of Round 7 Stage 1 — can run in either order or parallel. P_phase5_topological_injection pre-registration still pending. |
| Round 7 Stage 0 — basin-audit-as-precondition (`1bc1652`) | ❌ RETRACTED 2026-04-25 (`c69e79c`) — Rule 6/8/10 violation per A35 | doc 71_ §1-§12 retained as audit trail; v1 driver retained as informational tooling | Mid-cycle self-audit caught the framing error before R7.1 implementation. Rule 6 (SM-style minimization on wave substrate); Rule 8 inverse (parallel infrastructure bypassing R7.1's corpus-canonical eigensolver); Rule 10 creeper compound (carried multi-turn without pressure-test). v1 run halted by A26 amplitude-guard at step 0 — only methodology-failure data collected. R7.1 strengthened to multi-seed instead. |
| Round 7 Stage 1 multi-seed Hessian-of-W (`c69e79c`) | ❌ RETRACTED 2026-04-25 (`675141e`) — Rule 6 violation per A36 | doc 71_ §13 retained per Rule 12 audit trail; `P_phase6_eigensolver_multiseed` retained-with-RETRACTED-marker | External audit on r8.7's frozen pre-reg caught deeper Rule 6 instance: Hessian-of-W is itself SM/QM-style energy-stationarity framing on a wave-propagation substrate. Same-gap finding as A35 at deeper layer (precondition → operator). Reframed via doc 72_ design-space articulation to block Helmholtz on (V, ω) joint state. |
| Doc 72_ design-space articulation (`675141e`) | ✅ LANDED 2026-04-25 | doc 72_ §1-§8 (~26KB) | Four AVE-native concepts (wave eigenmode / impedance match / topological quantization / S₁₁-min ≠ W-min) + 3D Smith chart Extension A primary + block Helmholtz §3.1 + V=0 decoupling footnote §3.1.1 + sector-energy split diagnostic §3.4 + Rule-10 commitment language §6.1. Conceptual scaffolding for R7.1 fresh-session implementer; closes depth-of-understanding gap that produced three pre-reg retractions in one session. |
| F17-K v3 (ii) R7.1 multi-seed block Helmholtz on (V, ω) joint | **Round 7 Stage 1 candidate (REFRAMED r8.8)** | ~290 LOC, ~3-4 hours fresh session | Frozen `P_phase6_helmholtz_eigenmode_sweep` (doc 71_ §15 ACTIVE). Generalized eigenvalue problem on joint state. Cross-blocks `C_Vω`, `C_ωV` encode Op14 coupling explicitly. V=0 seed decouples into V-block + ω-block simultaneously per §3.1.1 (strict superset of single-sector Helmholtz). Three-mode falsification + sector-energy split diagnostic (V/hybrid/ω). PASS criteria: c_eigvec=3 binary + shape correlation > 0.60 informational. Rule-10 commitment locks operator choice for fresh-session run. |
| **Round 6 + Phase 5 resume status** | ✅ CLOSED 2026-04-25 (`e1f6eac`) | — | All four phases discipline-complete. Methodology arc characterized empirically; topology-encoding-by-ansatz finding applied to gate-firing problem; case (b') adjudicated via injection-profile-upgrade route. Round 7 Stages 1+2 named, scoped, deferred to fresh sessions. |
| **Remaining critical-path total (r8.8)** | superseded by r8.9 closure | — | r8.8 critical-path framing (gated on R7.1 fresh-session run) closes empirically at r8.9 with Mode III canonical across the seven-test framework-level statement. See r8.9 rows below. |
| R7.1 reframe-4 multi-seed block Helmholtz on (V, ω) joint (`8c44ef0`-`b8d97d9`) | ✅ RAN 2026-04-26 — Mode III at all 4 seeds (V-block comprehensive; Cos-block bottom-100-coverage); Mode I CANDIDATE at N=64 V-block GT_corpus (gap 0.45%) FALSIFIED by topology check (shell fraction 1.13%, not (2,3) localized) — third headline flip | doc 73_ + doc 74_ §1-§9, ~290 LOC | Fresh-session run committed to operator choice per Rule 10 commitment in r8.8. Two implementation bugs caught + fixed mid-run per Rule 10. Mode I N=64 candidate falsified by dual-criterion topology check (A39 v2 frequency + topology). Joint R7.1 + R7.2 final closure both Mode III via `d3adcc2`: engine does NOT host (2,3) electron bound state in V or Cos sectors at corpus GT. |
| R7.2 topological pair injection (2,3) at N=64 dual-criterion | ✅ RAN 2026-04-26 — Mode III | doc 74_ + commit `1c89fa1` (pre-reg) + closure in `d3adcc2` | Independent of R7.1; both ran in parallel and joint closure landed in single commit. Closes Phase 5 gate-firing question downstream of single-electron pivot. |
| Doc 74_ §10 audit follow-up tests (Test A + Test B v2/v3) | ✅ RAN 2026-04-26 — all Mode III | commits `53c2ce9` → `7fea8f7` → `39f56a` | Test A (Cos-block N=64 c_eigvec recheck, 4-category corpus-canonical c=0 framing) Mode III-both. Test B v1 single-port temporal (R/r=19.0 Mode II) caught wrong-question by audit per A44 spatial-multipoint correction; Test B v2 (8-port spatial per doc 26_ §3, 0.5·V_SNAP) Mode III-spatial rel_std 0.039; Test B v3 (saturation regime 0.85·V_SNAP) Mode III-spatial rel_std 0.047. **Test B v2/v3 IS the corpus-canonical doc 28_ §5.1 single-bond phasor test** at N=32 — closed empirically. Doc 74_ §10.6 framework-level closure statement: "All seven tests Mode III." |
| Round 8 Move 5 — self-stable (2,3) orbit hunt at corpus GT (time-domain, no drive) | ✅ RAN 2026-04-26 (commit `c772211`) — Mode III-orbit per pre-reg, but self-stable sub-corpus (2,3) orbit found empirically | ~150 LOC, P_phase6_self_consistent_orbit_hunt | Engine hosts a (2,3) plateau at peak \|ω\|=0.3044 (≈one-third corpus saturation) for 150 Compton periods, MIGRATING off the corpus shell. Empirical handle for "characterize as itself" pivot per Rule 10 corollary. |
| Round 8 Move 6 — natural attractor (R, r) characterization | ✅ RAN 2026-04-26 (commit `880165b`) — Mode III-natural; meta-methodological pivot | P_phase6_natural_attractor_characterization | Move 5 attractor's relaxed (R, r) delocalized at search-grid boundary, spectrum non-physical. Pivots to characterize-as-itself per Rule 10 (Rule 9 v2 reframe pattern: "what is this thing?" before "is corpus thing here?"). |
| Round 8 Move 7+7b — Phase 1 attractor characterization | ✅ RAN 2026-04-26 (commits `39444d0`, `dd63116`, `48d7cc9`) — branch (b): (2,3)-topological at LATTICE CUTOFF, NOT corpus electron | P_phase1_attractor_characterization + v2_fft_fix | Move 7 FFT zero-V_inc / Nyquist-artifact bug caught + Move 7b fix (sample at top-5 \|V_inc\|² cells, not \|ω\|² centroid-displaced — Rule 10 sampling-discipline corollary A49 centroid-of-shell). Auditor's Q≈2/α speculation dissolves at actual frequency. |
| Round 8 §13 amendment + §14 two-layer dimensional reconciliation | ✅ LANDED 2026-04-26 (commits `51463c2`, `fe83133`) | doc 73_ §13-§14 | FFT-as-leakage misinterpretation corrected per Grant's dimensional-analysis check — attractor is STATIC fixed point, NOT lattice-cutoff oscillator; Move 9 (autoresonant drive at ω_C) becomes load-bearing. §14 lands two-layer reconciliation: spin-½ half-cover (B canonical: m_Cosserat = 2·m_e per SU(2)→SO(3) double-cover) + Op14 saturation as gravitational redshift (NEW). σ=4 Cos-block test predicts shell-localized (NOT core) Mode I. |
| Round 8 Move 9 — autoresonant drive at ω_C | ✅ RAN 2026-04-26 — load-bearing per §13 amendment | (covered in commit chain `c9e38c4` → `89ba147`) | Tests corpus's actual standing-wave claim that linearized eigsolve necessarily misses. |
| Round 8 Move 10 — static fixed point spatial topology | ✅ RAN 2026-04-26 (commit `89ba147`) — STATIC FIXED POINT isn't shell-shaped, sectors spatially decoupled (A²≈0 at top-\|ω\| cells), Op10 c=3 carrier matches NONE of standard topology types (torus knot / Hopf-linked / Y_lm) | P_phase1_attractor_winding_characterization + scipy sph_harm API compat fix | §14 framing partially superseded — sectors are decoupled at the static fixed point, not coupled as the §14.4 σ=4 Cos-block prediction expected. |
| Round 8 Move 11 — A-011 reactance gap closed | ✅ RAN 2026-04-26 (commit `e9fdf99` pre-reg, `37f5d9d` result, `89ba147` Move 11b w/ PML filter) | P_phase1_attractor_reactance_tracking | Closes A-011 reactance gap (Φ_link + ω_dot computed but never read). Result: H_cos drift 5.5% + ρ(T_cos, V_cos)=+0.366 (NOT LC reactance signature; positive Pearson trading instead of anti-correlation). PML cell exclusion bug caught + Move 11b re-run with `pml_thickness ≤ {i,j,k} ≤ N - pml_thickness - 1` filter (A50 PML-cell-exclusion sub-rule). |
| Round 8 Diag A — Cosserat wave-speed amplitude dependence | ✅ RAN 2026-04-26 (commits `36d6e0d`, `bfc58d8`, `391a3b5`) — Mode I per pre-reg: V·S vs T·1 asymmetry is REAL but EMPIRICALLY NEGLIGIBLE at relevant amplitudes | P_ax5_cosserat_wave_speed_amplitude_dependence | A=6 integrator-cliff is separate from V·S/T·1 asymmetry; Diag C source audit + Move 11b's already-measured Pearson matrix close the Move 11 H_cos drift question (Op14 trading, not missing physics). Doc 75_ §6.3 engine fix specified: T_kinetic gets the same Op14 S factor (ρ → ρ·S, I_ω → I_ω·S). |
| Round 8 photon-tail dual-seed (path a) | ✅ RAN 2026-04-26 (commits `fb2e4f1`, `13b2017`) — Mode III 0/4 — dual-seed standing-wave IC at engine-rep scale catastrophically dissolves Cosserat (4% retention) while K4 partially survives (66% retention) | P_phase6_photon_tail_dual_seed; N=64, R=4, r=1.5 | Sector asymmetry surfaced; path (b) propagating IC strongly motivated. |
| Round 8 photon-tail propagating-IC (path b) | ✅ RAN 2026-04-26 (commits `bd15bb0`, `1b48f4d`) — Mode III, near-identical to path (a); 3/3 of C1/C2/C3 = Mode I (C4 informational per A57); A58 empirical equivalence | P_phase6_photon_tail_propagating_ic; ω_dot = ω_loop in (x,y) plane | **Round 8 photon-tail branch closed** per pre-reg threshold. Doc 75_ §11 + A57 (C4 informational vs C1/C2/C3 binary framing) + A58 (path-(a)/path-(b) empirical equivalence). |
| Doc 75_ Cosserat energy conservation violation finding | ✅ RAN 2026-04-26-27 — Engine bug, not missing axiom (A44 collapse) | doc 75_ §1-§11 + §6.3 fix spec | Move 11 + Diag A traced the V·S vs T·1 saturation asymmetry — Cosserat code saturates V_potential (G·S, K·S, G_c·S) but leaves T_kinetic unmodulated (ρ, I_ω constants); ½LI² and ½CV² don't co-saturate; total energy isn't conserved; ω drifts as a consequence. **Engine bug, not missing axiom** (Grant collapse: "this is our conservation of energy axiom. rest mass saturates L, propagation saturates C"). Engine fix specified at §6.3: T_kinetic gets the same Op14 S factor (ρ → ρ·S, I_ω → I_ω·S). Per Diag A asymmetry is empirically negligible at relevant amplitudes — fix is housekeeping not load-bearing. |
| Axiom homologation arc (commits `75d1fde` → `6968398`) | ✅ LANDED 2026-04-27 — Schemes A vs B reconciled to canonical Scheme A | 5 implementer commits + auditor cross-cutting reference | Ax 1 = LC Network Substrate / Ax 2 = Topo-Kinematic / Ax 3 = Effective Action / Ax 4 = Universal Saturation S(A) = √(1−A²) (quarter-circle, NOT SiLU). Doc 76_ Scheme-B reframe superseded by doc 77_ canonical Scheme-A version. INVARIANT-S2 SiLU/ABCD misnomers fixed. Backmatter Ax 1↔Ax 2 swap fixed. Cross-cutting reference [`manuscript/ave-kb/common/axiom-homologation.md`](../../manuscript/ave-kb/common/axiom-homologation.md) consolidates citation chain (Rule 12 v2 promotion). Doc 75_ framing-error pass corrected "Ax 3 = energy conservation" → "Ax 4 asymmetric L/C, Noether-broken energy conservation" per `69fd974`. |
| **L3 branch closure synthesis (next deliverable)** | 🔄 PENDING — fresh session | ~1 fresh session | Synthesizes the seven-test framework-level Mode III statement + Move 5 sub-corpus (2,3) attractor characterization + axiom homologation Scheme A canonicalization into a final canonical record. No new empirical run required; existing data is sufficient per A43 retroactive correction. Engine fix per doc 75_ §6.3 lands as separate housekeeping commit; closure synthesis can land before or after — independent. |
| **Engine fix r8.10 (housekeeping)** | 🔄 PENDING — implementer commit | ~1 fresh session | Apply doc 75_ §6.3 T_kinetic Op14 saturation: `ρ → ρ·S`, `I_ω → I_ω·S`. Closes energy-conservation violation surfaced by Move 11. Per Diag A empirically negligible at relevant amplitudes — fix forecloses "did the engine fully honor Ax 4?" objection on closure doc but doesn't flip Mode III statement. r8.10 manual update will mark r8.9-pending engine fix as committed. |
| **Remaining critical-path total (r8.9)** | — | **L3 branch closes empirically** | Single-electron-first pivot CLOSES with Mode III canonical for "engine hosts corpus (2,3) electron at corpus Golden Torus geometry under any tested config." Seven pre-registered tests at varied configurations (V-block, Cos-block, Φ_link-block; N=24/32/48/64; linear and saturation amp regimes; eigsolve and time-domain; standing-wave-IC and propagating-IC) all returned Mode III. Deliverables remaining: (1) closure synthesis doc; (2) engine fix r8.10 (housekeeping). Phase 5 pair-nucleation work remains structurally suspended; any future resumption would be downstream of an engine architectural change (~v5.0.0 territory). |

---

## 14. Engine API & typical usage

### 14.1 Minimum driver

```python
import numpy as np
from ave.topological.vacuum_engine import (
    VacuumEngine3D,
    AutoresonantCWSource,
    RegimeClassifierObserver,
    TopologyObserver,
    EnergyBudgetObserver,
    DarkWakeObserver,
)

# 1. Build the engine
engine = VacuumEngine3D.from_args(
    N=40, pml=5,
    temperature=0.1,              # m_e c² units
    amplitude_convention="V_SNAP",
    coupling_kappa=1.0,
)

# 2. Attach counter-propagating autoresonant CW sources
for x0, direction in [(engine.config.pml + 4, (1, 0, 0)),
                       (engine.N - engine.config.pml - 5, (-1, 0, 0))]:
    engine.add_source(AutoresonantCWSource(
        x0=x0, direction=direction,
        amplitude=0.5, omega=2*np.pi/3.5,      # λ = 3.5 cells
        sigma_yz=3.0,
        t_ramp=20, t_sustain=260,
        K_drift=0.5,
    ))

# 3. Attach observers
engine.add_observer(RegimeClassifierObserver(cadence=1))
engine.add_observer(TopologyObserver(cadence=5, threshold_fracs=[0.1, 0.3, 0.5, 0.7]))
engine.add_observer(EnergyBudgetObserver(cadence=1))
engine.add_observer(DarkWakeObserver(cadence=5, propagation_axis=0))

# 4. Run
engine.run(n_steps=300)

# 5. Post-process
hist = engine.history()
max_A2_cos = max(r["max_A2_cos"] for r in hist["RegimeClassifierObserver"])
print(f"Max A²_cos = {max_A2_cos:.3f}")

snap = engine.snapshot()       # full state at last step
```

Reference driver: [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py).

### 14.2 Engine class API

`VacuumEngine3D` methods, all defined in [vacuum_engine.py:758](../../src/ave/topological/vacuum_engine.py#L758):

| Method | Signature | Purpose |
|---|---|---|
| `__init__(config)` | `config: EngineConfig` | Direct construction |
| `from_args(**kwargs)` | classmethod | Convenience: `VacuumEngine3D.from_args(N=48, temperature=0.1)` |
| `initialize_thermal(T, seed=None, thermalize_V=False)` | T in m_e c² units | Re-initialize thermal state; called automatically at construction |
| `add_source(source)` | `source: Source` | Register |
| `add_observer(observer)` | `observer: Observer` | Register |
| `step()` | — | Advance one outer_dt |
| `run(n_steps)` | int | Advance n_steps |
| `snapshot()` | → dict | Full state at current step (runs ad-hoc observers) |
| `history()` | → dict[str, list] | All observer buffers keyed by class name / ScalarObserver name |
| `amp_display(amp_vsnap)` | → float | Convert internal V_SNAP units back to user convention |
| `regime_of(A2)` | → str | Classify into "I"/"II"/"III"/"IV" |
| `.outer_dt` | property → float | K4 outer timestep |
| `.time`, `.step_count` | fields | Current state |
| `.k4`, `.cos`, `.config` | fields | Expose the underlying substrate objects for power users |

### 14.3 Snapshot schema

`engine.snapshot()` returns:
```python
{
  "t":          float,
  "step_count": int,
  "regime":     { ... RegimeClassifierObserver._capture output ... },
  "topology":   { ... TopologyObserver._capture output ... },
  "energy":     { ... EnergyBudgetObserver._capture output ... },
}
```
See §8 for each sub-schema.

### 14.4 Common pitfalls

- **Thermalize_V at high T.** `initialize_thermal(T=0.1, thermalize_V=True)` silently exceeds the Schwinger-temperature stability bound (§9.3) and the run will diverge. Default `thermalize_V=False` guards this.
- **Cosserat gradient with `np.gradient`.** On a bipartite mask, `np.gradient` produces zeros at the inactive interlaces. Always use `cosserat_field_3d.tetrahedral_gradient`. `DarkWakeObserver` does this internally.
- **PML vs active area confusion.** Place sources at `x0 ≥ pml + 1` (not at `x0 = 0`) so the injected wave has a non-PML starting region. Canonical: `x0 = pml + 4`.
- **Counter-propagating sources need opposite `direction`.** The T₂ port-weighting is direction-sensitive. If both sources have `direction=(1, 0, 0)`, both inject in the same direction regardless of `x0`.
- **RNG seed drift.** Between v2 (max A²_cos = 1.009) and v3 H1 rerun (0.877), different default-RNG states produced a run-to-run swing. For reproducible A² at T > 0, pass `seed` to `initialize_thermal`.
- **Cadence on `EnergyBudgetObserver`.** Default cadence = 1 means the JAX-backed `E_coupling` gradient is recomputed every step. On large N this is the main per-step cost. Use `cadence=5` or higher for long runs where Hamiltonian drift monitoring is diagnostic-only.

---

## 15. Derivation chain traceability

Each engine element traces to: an axiom citation (the "why"), a research-doc chain (the "how we got here"), and a manuscript section (the publication-grade statement). Organized by subsystem.

### 15.1 K4 substrate (Axiom 1)

| Element | Axiom cite | Research-doc chain | Manuscript |
|---|---|---|---|
| K4 lattice pitch ℓ_node | Axiom 1 | [constants.py:136](../../src/ave/core/constants.py#L136) | [vol_1 ch01:17](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L17) |
| Bipartite A/B sublattices | Axiom 1 | [22_ §2–§4](22_step1_k4_rotation_action.md) — K4 = A₄ rotation group | vol_1 ch01 |
| 4 port vectors `(±1,±1,±1)` | Axiom 1 (tetrahedral) | [k4_tlm.py:31–36](../../src/ave/core/k4_tlm.py#L31); [vacuum_engine.py:120](../../src/ave/topological/vacuum_engine.py#L120) | vol_1 ch01 |
| Scatter `S_ij = 0.5 − δ_ij` | Axiom 1 (unitary 4-port) | [46_ §2.2 (C2)](46_vacuum_engine_scope.md); [14_](14_theorem_3_1_mutual_inductance_from_axioms.md) | vol_4 ch01 |
| `outer_dt = ℓ_node / (c√2)` | K4 anisotropy | [40_ §2.1](40_modeling_roadmap.md) | [constants.py:497](../../src/ave/core/constants.py#L497) |
| **Subatomic V_yield override** (`V_yield ≡ V_SNAP` at VacuumEngine3D's operating scale, making `A² = V²/V_SNAP²` canonical `r²`) | Axiom 4 + scale-dependence | R4 adjudication (§17.0, doc 55_ R4 banner, working-tree doc 50_ r3) | [vol_4 ch01:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711) explicit override; [vol_1 ch07:104](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L104) macro table for contrast |

### 15.2 Cosserat sector (Axiom 3)

| Element | Axiom cite | Research-doc chain | Manuscript |
|---|---|---|---|
| `(u, ω)` fields | Axiom 3 (effective action) | [02_](02_lagrangian_derivation.md); [01_ §10](01_identity_adjudication.md) — C3 SU(2) canonization | vol_1 ch02 |
| Mass gap `m² = 4 G_c / I_ω` | Phase I derivation | [41_ §T2](41_cosserat_time_domain_validation.md) | F1 flag in [S_GATES_OPEN.md](S_GATES_OPEN.md) |
| Moduli pinning `G_c = γ`, `ℓ_Cos = ℓ_node` | Axiom 1 Nyquist match | [04_](04_moduli_pinning_check.md) | vol_1 ch02 |
| Op10 invariant `c = 3` for electron | Axiom 2 + knot theory | [07_](07_universal_operator_invariants.md); [25_](25_step4_23_winding_selection.md) | [vol_1 ch08](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) |
| Saturation kernel `S = √(1 − A²)` | Axiom 4 | [46_ C4](46_vacuum_engine_scope.md) | vol_4 ch01 Varactor eq |

### 15.3 Coupling (S1 = D)

| Element | Axiom cite | Research-doc chain | Manuscript |
|---|---|---|---|
| `L_c = (V²/V_SNAP²) · W_refl` | S-gate S1=D, reuse of Op3/Axiom 4 | [S_GATES_OPEN.md S1](S_GATES_OPEN.md); [44_](44_pair_creation_from_photon_collision.md) | vol_4 ch01 |
| Zero new parameters | S1=D discipline | [S_GATES_OPEN.md](S_GATES_OPEN.md) | — |

### 15.4 Sources

| Element | Axiom cite | Research-doc chain | Manuscript |
|---|---|---|---|
| T₂-projected port weights | K4 photon identification | [30_](30_photon_identification.md); [vacuum_engine.py:125](../../src/ave/topological/vacuum_engine.py#L125) | — |
| `AutoresonantCWSource` PLL | Axiom 4 Duffing + AVE-Propulsion Ch 5 | [49_](49_dark_wake_bemf_foc_synthesis.md) | [AVE-Propulsion/vol_propulsion/ch05](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex) |

### 15.5 Observers

| Element | Axiom cite | Research-doc chain | Manuscript |
|---|---|---|---|
| Regime boundaries A²={2α, 3/4, 1} | Axiom 4 (regime map) | [46_ C3](46_vacuum_engine_scope.md) | [vol_1 ch07](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) |
| Q_H Hopf invariant | Axiom 2 | [cosserat_field_3d.py extract_hopf_charge](../../src/ave/topological/cosserat_field_3d.py); [07_](07_universal_operator_invariants.md) | vol_1 ch08 |
| Centroid finder | Engineering | [cosserat_field_3d.py find_soliton_centroids](../../src/ave/topological/cosserat_field_3d.py) | — |
| `DarkWakeObserver` τ_zx | AVE-Propulsion dark-wake | [49_](49_dark_wake_bemf_foc_synthesis.md) | [AVE-Propulsion warp_metric_tensors.py:75–95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py) |
| Energy budget | Axiom 3 Hamiltonian | [42_](42_coupled_simulator_validation.md) | vol_4 ch01 |

### 15.6 Initialization (thermal state)

| Element | Axiom cite | Research-doc chain | Manuscript |
|---|---|---|---|
| C1 cold-vacuum determinism | Axiom 1 (no sub-ℓ_node reality) | [46_ C1](46_vacuum_engine_scope.md); [47_](47_thermal_lattice_noise.md) | [vol_1 ch01:79–95](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex); [vol_1 ch03:514](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex) |
| σ_V, σ_ω equipartition | Classical equipartition | [47_ §2](47_thermal_lattice_noise.md) | queued for [vol_1 ch03](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex) (doc queue item 20) |
| AVE Schwinger T = 3.44 MK | σ_V = V_SNAP at kT = α·m_e c²/(4π) | [47_ §2.2](47_thermal_lattice_noise.md) | queued for [vol_4 ch01](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) (doc queue item 17) |
| "Thermal lattice noise" terminology (C6) | [vol_1 ch03:514](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex) | [46_ C6](46_vacuum_engine_scope.md) | — |

### 15.7 Queued (Stage 6) additions

| Element | Axiom cite | Research-doc | Manuscript |
|---|---|---|---|
| `Phi_link = ∫ V_bond dt` | Axiom 2 ([Q]≡[L]), memristance | [54_ §3](54_pair_production_axiom_derivation.md) | [vol_4 ch01:223–227](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L223) |
| `Ω_node = ω_0 · (1 − V²/V_yield²)^(1/4)` | Axiom 4 varactor | [54_ §4](54_pair_production_axiom_derivation.md) | [vol_4 ch01:127–142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L127) |
| Asymmetric (S_μ, S_ε) | [vol_1 ch07:252](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L252) | [54_ §6](54_pair_production_axiom_derivation.md) | vol_1 ch07 |
| κ_chiral = α pq/(p+q) | Sub-Theorem 3.1.1 | [20_](20_chirality_projection_sub_theorem.md); [54_ §6](54_pair_production_axiom_derivation.md) | [AVE-HOPF/03_hopf_01_chiral_verification:72–82](../../../AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex) |
| Pair nucleation gate (C1 ∧ C2) | Axiom 4 + Axiom 2 | [53_ §4.3](53_pair_production_flux_tube_synthesis.md); [54_ §7](54_pair_production_axiom_derivation.md) | — (publication target) |

### 15.8 Pythagorean vacuum-strain theorem

Currently [AVE-APU/vol_1_axiomatic_components/ch05:26–37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex). Queued for promotion to AVE-Core vol_1 as INVARIANT-Phy1 per [.agents/handoffs/FUTURE_WORK.md G-7](../../.agents/handoffs/FUTURE_WORK.md). Load-bearing for Stage 6 Phase 4 (§13.4) because `A²_total = A²_μ + A²_ε` is the quadrature-sum form justified by this theorem.

---

## 16. Change log & cross-reference index

### 16.1 Change log

| Date | Commit | Author | Sections | Rationale |
|---|---|---|---|---|
| 2026-04-22 | — | session agent | new | Initial creation of r0. Captures engine state through Stage 4d + Stage 5 Phase A + Stage 6 Phase 0 doc. |
| 2026-04-22 | a0f50ed | Grant + agent | — | `research(L3 Stage 6 Phase 0+1): axiom-derived pair-production mechanism + test baseline` — 7 files, 1886 insertions. Adds `predictions.yaml`, `test_axiom_4_vacuum_varactor.py`, `test_v_snap_v_yield_consistency.py`, `test_predictions_matrix.py`, docs 53_ / 54_. |
| 2026-04-22 | 719f3ec | Grant + agent | — | `feat(L3 Stage 6 Phase 2): NodeResonanceObserver — Ω_node diagnostic` — 4 files, 648 insertions. Adds `NodeResonanceObserver`, `test_phase2_node_resonance.py`, `node_resonance_validation.py`. Honest-framing clarification in commit message about P_phase2_omega circularity. |
| 2026-04-22 | — | session agent | §1, §8.3, §10.9, §10.10, §13.1, §13.2, §13 queued additions table, new §3.5a, new §17 | **Manual r1.** Reflects Phase 1 + Phase 2 landed. Adds predictions-manifest subsystem §3.5a, Stage 6 test V&V rows §10.9 / §10.10, and §17 Audit findings from a critical review (A1–A13). |
| 2026-04-22 | 3a599ca | Grant + agent | — | `feat(L3 Stage 6 Phase 3): Φ_link bond flux state + BondObserver` — 5 files, 786 insertions. First structural engine-state change of Stage 6. Test suite 940 → 954 pass. |
| 2026-04-22 | (untracked) | Grant + agent | — | `src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py` — attempt at closing §17 A10 top-pick via seed sweep. In working tree. |
| 2026-04-22 | — | session agent | §1, §5.1, §8.5a, §10.11, §10.12, §11.1, §13.3, §13.7 table, §16, §17 status annotations + A14/A15/A16 | **Manual r2.** Phase 3 landed. Bumps engine to 3.0.0 (new state variable Phi_link is structural, per §1.2 rule). §17 augmented with per-finding status and 3 new findings surfaced by the Phase 3 commit. |
| 2026-04-23 | — | research-agent + session agent | §1, §10.4, §10.12, §17 A14 r3 note, §17 A17, §17.2 (A16 closed), §17.3 summary | **Manual r3.** v2 reproducibility sweep completed with REGRESSION verdict (0/20 seeds reach 1.009; range [0.77, 1.00]). A16 closed; A17 opened (distribution-vs-headline + cause-TBD). R4 change plan declares direction for A14 (remove /α from Node/Bond observers → match RegimeClassifier SNAP convention). doc 50_ §2.3 flagged for distribution-language rewrite. |
| 2026-04-23 | — (untracked) | research-agent (Phase 3.5.A) | — | Doc 55_ `55_cosserat_normalization_derivation.md` delivered — independent re-derivation from Vol 1 Ch 7 + manuscript KB, per Grant's "don't trust doc 54_ as authoritative" directive. **Reverses manual r3's A14 direction**: Cosserat's yield-normalization is canonical per Vol 1 Ch 7:104; K4's SNAP is the outlier. Chooses R3 (dual accessors, minimal-invasive), defers full K4→yield migration to FUTURE_WORK G-9. Surfaces A18 (OpN drift), A19 (Vol 1 Ch 7:115/:130 inconsistency), A20 (ε_yield calibration). |
| 2026-04-23 | — | session agent | §1, §17 A14 r4 correction, §17 A18/A19/A20/A21, §17.3 summary, §16 | **Manual r4.** Integrates doc 55_. Earlier R4 direction (remove /α) explicitly superseded by doc 55_'s R3 direction (dual accessors, K4 is the outlier). Plan-disconnect flagged. |
| 2026-04-23 | — (untracked) | research-agent | — | Doc 57_ `57_universal_lattice_units_v4_refactor.md` delivered — 479-line plan for post-Stage-6 structural refactor (FUTURE_WORK G-10, 2–3 weeks). Consolidates all saturation/impedance/reflection through canonical universal operators; proposes new `universal_regime_classifier`; adds cross-scale regression suite. Explicitly post-Stage-6, not in parallel with Phase 4–6. G-10 not yet in FUTURE_WORK.md. |
| 2026-04-23 | — | session agent | §1, §13.6a new, §16.3 doc index, §17 A22/A23 new + status annotations, §17.3 summary, §16 | **Manual r5.** Integrates doc 57_. Adds §13.6a summarizing the v4 post-Stage-6 refactor plan. Two new findings: **A22** (inline saturation/impedance duplicates universal operators — Rule-6-adjacent drift risk, doc 57_ §2.1); **A23** (apparent framing tension between doc 55_ "K4 is outlier" and doc 57_ "V_SNAP = Vol 4 Ch 1:711 subatomic override" — spot-check needed). Confirms **R4 observer patch still NOT landed** — code-level A14 remains uncorrected. |
| 2026-04-23 | — | session agent | §1 status, §17 A14 r6 note, §17 A17 bisection-launched note, §17.2 A23 closed, §17.3 summary (A14/A15/A17/A20/A23 updated), critical-path blockers rewritten | **Manual r6 (partial — initial R4 recognition).** A23 spot-check resolved in favor of **R4 per Vol 4 Ch 1:711 subatomic override** (direct manuscript read: "Subatomic-scale simulations should override with v_yield=V_SNAP"). VacuumEngine3D IS subatomic-scale; engine's V_SNAP-normalization IS canonical r². Doc 55_'s R3 "K4 is outlier" direction superseded (doc 55_ marked with SUPERSEDED banner). Plan file's R4 direction (remove `/α` from NodeResonance + BondObserver) authoritative. TKI-derivation of ε_yield closes at 1 exactly under R4 — not placeholder. Doc 50_ r3 rewrite lands with R4 framing. Bisection 719f3ec vs 3a599ca launched 2026-04-23 for A17. **R4 observer patch still NOT applied at the code level.** |
| 2026-04-23 | — | session agent (fresh audit, corrupted) | §1 front-matter + Phase-3-rollback narrative across §5.1, §8.5a, §10.11, §11.1, §13.3, §13.7, §16.2, §17 A15/A17 annotations | **⚠ CORRUPTED r6 pass.** A session-agent pass (attributed to me) introduced fabricated claims: "Phase 3 rolled back to stash@{0}", "HEAD detached at 719f3ec", "Engine version reverted 3.0.0 → 2.2.0", "R4 observer bug patch has NOT landed". **All false per ground-truth git state** — HEAD is `3a599ca` on branch `research/l3-electron-soliton`, Phase 3 is landed, BondObserver/Phi_link are in the engine, R4 patches are in the working tree. Flagged by the concurrent research agent ("VACUUM_ENGINE_MANUAL corrupted by concurrent writer … all objectively false per actual git state"). R4 adjudication content (§17.0, A14/A19/A20/A23 retractions) was independently manuscript-grounded and retained through repair. |
| 2026-04-23 | — | session agent (r6 repair pass) | §1 front-matter restored, §5.1 Phi_link un-stashed, §8.5a BondObserver un-stashed, §10.11 Phase 3 tests un-stashed, §11.1 bond-state limit restored to CLOSED, §13.3 + §13.7 Phase 3 restored to LANDED, §16.2 engine version history corrected (3.0.0 current, 3.0.1 pending R4 commit), §17 A15/A17 + critical-path blockers rewritten against ground truth, §8.5a note added about working-tree R4 patch, §10.11 note added about `test_normalization_subatomic_override.py`, stash-description corrected (`pre-ee-isomorphism-branch` only, 32 insertions; no "doc 50_ r3 + bisection" stash exists) | **r6 repair pass.** Undoes Phase-3-rollback corruption. Preserves all R4 content (§17.0, A14/A19/A20/A23 retractions in §17.2) — those were always correct; the corruption was localized to Phase-3-state claims. Adds explicit acknowledgment that R4 observer patches are in the working tree (not committed). |
| 2026-04-23 | 6e355d1 | Grant + agent | — | `fix(L3 Stage 6 Phase 3.5.B): R4 normalization — subatomic override` — commits the R4 observer patches previously in working tree. `/α` removed from NodeResonance + Bond; test_normalization_subatomic_override.py added as invariant test; poke formulas updated in Phase 2/3 tests. |
| 2026-04-23 | 224cad0 | Grant + agent | — | `docs(L3 Stage 6 Phase 3.5.A/B): R4 adjudication docs + bisection driver` — commits doc 50_ r1→r2→r3 rewrite, doc 55_ with SUPERSEDED banner, doc 57_ v4 refactor plan, and `v2_reproducibility_seed_sweep.py` bisection driver. |
| 2026-04-23 | a5bd1da | Grant + agent | — | `feat(L3 Stage 6 Phase 4): asymmetric μ/ε saturation — S1 gate reopen` — Phase 4 landed. S-gate S1 reopened + resolved with design 1A (instantaneous Beltrami helicity, no accumulator), 2-II (asymmetric ∇ln(Z_eff) reflection form), 3c (full replacement). 965 → 983 pass. Key files: `cosserat_field_3d.py` (+202), `k4_cosserat_coupling.py` (+139), `vacuum_engine.py` (+6), new `test_phase4_asymmetric_saturation.py` (+383, 7 invariants). |
| 2026-04-23 | — | session agent (r7 update) | §1 front-matter, §11.9 closed, §12.3 S1 gate resolved, §13.4 Phase 4 landed, §13.7 scope table, §16.1 + §16.2 engine version history updated (3.0.1/3.0.2/3.1.0), §17 R4 status updated to committed, A15 re-annotated for Phase 4 enablement, critical-path blockers simplified | **Manual r7.** Reflects three 2026-04-23 commits (6e355d1 R4 patches, 224cad0 R4 docs, a5bd1da Phase 4). Engine now at 3.1.0 on HEAD `a5bd1da`. All R4-era findings closed (§17.2). Phase 5 (`PairNucleationGate`) is the remaining Stage 6 blocker; its precondition is `CircularlyPolarizedCWSource` (flagged in a5bd1da as "next"). |
| 2026-04-23 | d124632 | Grant + agent | — | `test(L3 Stage 6 Phase 4): Meissner mechanism validation (E.1a)` — adds 3 tests pinning core doc 54_ §6 mechanism (RH Beltrami → S_μ ≈ 0.22 while S_ε ≈ 1.0 → ratio < 0.35; LH reverses). |
| 2026-04-23 | aa7a337 | Grant + agent | — | `fix(L3 Stage 6 G-12): AutoresonantCWSource axiom-native varactor PLL` — replaces linear-Taylor with Ax4-native `(1−A²)^(1/4)` per Vol 4 Ch 1:127-142. Closes A7. K_drift deprecated. δ_lock = ω₀·α now reachable for Phase 5. |
| 2026-04-23 | 2e3abcf | Grant + agent | — | `test(L3 Stage 6 A10): thermal equipartition validation — 23 tests` — closes A10 (highest-leverage non-adjudication item). Pins Maxwell-Boltzmann variances σ_V/σ_ω/σ_ω̇/σ_u/σ_u̇ from doc 47_ §2 + C1 cold-vacuum determinism + seed reproducibility + √T scaling + moduli scaling + active-mask respect. |
| 2026-04-23 | e17b8cd | Grant + agent | — | `feat(L3 Stage 6 G-11c): CosseratBeltramiSource — direct-ω chirality driver` — direct helical ω injection at source slab; bypasses K4-port CP ambiguity. 18 tests. |
| 2026-04-23 | 5c3f2d1 | Grant + agent | — | `feat(L3 Stage 6 G-11a): SpatialDipoleCPSource — CP V_inc via dipole modulation` — two 90°-phase-shifted Gaussian-windowed dipole patterns. 13 tests. |
| 2026-04-23 | 9ecc2ca | Grant + agent | — | `feat(L3 Stage 6 Phase 5): PairNucleationGate — Kelvin vortex pair in Bingham capsule` — observer-with-side-effect on C1 ∧ C2; injects point-rotation Beltrami pair with bond Φ_critical. 32-test suite. Bingham-capsule + Kelvin topological-protection framing per Vol 4 Ch 1:189-203. |
| 2026-04-23 | 3f9569b | Grant + agent | — | `research(L3 Stage 6 Phase 5): pair-nucleation driver — N=24 C1 undershoot` — first run at registered amp=0.5·V_SNAP. Max A² = 0.75-0.91 < sat_frac=0.95; 0 firings. Driver plumbing verified clean. Adjudication deferred. |
| 2026-04-23 | 8272583 | Grant + agent | — | `research(L3 Stage 6 Phase 5.5-5.6): Cosserat PML + memristive yield-crossing derivations + 4 predictions + animation driver` — derivation-first commit landing docs 58_ + 59_ + 4 new predictions in `predictions.yaml` (P_memristor_loop_area, P_yield_heal_topological_residue, P_cooling_rate_defect_density, P_chirality_horizon_coupling). |
| 2026-04-23 | 99b497a | Grant + agent | — | `research(L3 Stage 6 Phase 5.7): BH interior contradiction audit + novel cosmic-K4 proposal (FLAGGED, corpus-contradicting)` — docs 60_ + 61_. Surfaces corpus contradiction between info-loss stance (Vol 3 Ch 15/21/KB-ch04) and alternative interface-encoding framing. Flagged per Flag 60-A; corpus-revision-pending. |
| 2026-04-23 | 03cb9d5 | Grant + agent | — | `feat(L3 Stage 6 Phase 5.5): Cosserat-sector PML + P_phase5_* prediction renames` — implements doc 58_ derivation. Quadratic-rolloff mask on (u̇, ω̇) with same `pml_thickness` as K4 PML. Closes Ax1+Ax3 boundary-treatment-symmetry gap. |
| 2026-04-23 | 49917ff | Grant + agent | — | `feat(L3 Stage 6 Phase 5.6): Memristive Op14 (K4 sector) — opt-in dynamical S(t)` — implements doc 59_ §10.2. New `use_memristive_saturation` flag default off; when on, K4 carries dynamical S(t) per first-order relaxation ODE with τ_relax = ℓ_node/c. Cosserat side deferred. |
| 2026-04-23 | 2671a54 | Grant + agent | — | `research(L3 Stage 6 Phase 5.7): S_BH adjudication + Ŝ-on-horizon calculation — doc 61_ vindicated as AVE-native geometric entropy` — doc 62_. Applies Vol 3 Ch 11 Ŝ operator with |Γ|²=1/2 at A-B interface; recovers `Ŝ_geometric = A·log(2)/ℓ_node²` axiom-first without microstate counting. Three-entropy distinction (Ŝ_geo, S_BH, discrete) lands as canonical. |
| 2026-04-23 | fcd5d3e | Grant + agent | — | `docs(L3 Stage 6 Phase 5.7): Doc 61_ surgical reframe — 10⁴⁴ direction corrected, three-entropy distinction landed` — fixes direction error in doc 61_ original §5 (was 10⁴⁴, correct is 10⁻⁴⁴). Reframes §5.4 retention-of-original-body. |
| 2026-04-24 | 740b1a3 | Grant + agent | — | `docs(L3 Stage 6 Phase 5.7): Doc 63_ info-loss re-audit — AVE aligns with 1970s-Hawking, doc 61_ §3.5/§11 retracted` — doc 63_. Vol 3 Ch 11 Ŝ operator measures entropy GENERATION at scattering events, not information CAPACITY preservation. Doc 61 §3.5 unitarity-preserved retracted via §0 header (body preserved per audit-trail discipline). AVE info-loss stance consistent with corpus per Flag 63-B. |
| 2026-04-24 | b74ac19 | Grant + agent | — | `research(L3 Stage 6 Phase 5.7): Doc 64_ first-law derivation attempt — partial closure, Flag 62-A remains` — doc 64_. **Area theorem `δA ≥ 0` derived from Ax1+Ax4** (`r_sat = 7GM/c²` linear in M; `δA = 392π·G²M·δM/c⁴`). dE = dM·c² from Ax2. T·dS = dE FAILS to close axiom-first by factor 7ξ ≈ 10⁴⁴ with native Ŝ_geometric — first law remains imported. Flag 62-A load-bearing. r_sat = 3.5·r_Schwarzschild flagged as falsifiable prediction (Flag 64-A). |
| 2026-04-24 | f9b463e | Grant + agent | — | `research(L3 Stage 6 Phase 5.7): Doc 65_ Flag 62-G closure — discrete-lattice Γ gives ~8.7·k_B universal constant, not A-scaling` — doc 65_. Discrete-lattice corrections to corpus's Γ=0 give `Ŝ_discrete ≈ 4π·log(2) ≈ 8.7 k_B` (mass-independent, topological invariant). Closes Flag 62-G but soft — Flag 65-A acknowledges WKB vs dimensional estimate disagreement (30+ orders of magnitude). |
| 2026-04-24 | 1805d14 | Grant + agent | — | `research(L3 Stage 6 Phase 5e): Cool-from-above driver — first run exposes latent unit-system bug in K4 saturation` — Phase 5e driver lands; first run at amp=0.9·V_SNAP shows S_field stays at 1.000 (saturation dormant). **Flag-5e-A** discovered: K4 uses module-level V_SNAP (511 kV SI) while engine sources inject in engine-natural V_SNAP=1. Saturation path effectively dormant in any engine-natural-units context. |
| 2026-04-24 | 098d430 | Grant + agent | — | `fix(L3 Stage 6 Flag-5e-A): K4 saturation uses engine V_SNAP — cool-through-yield now observable` — adds `V_SNAP` kwarg to `K4Lattice3D` (default None → module-level for SI standalone use; passed-through from `CoupledK4Cosserat` for engine-context use). 1144 pass, 3 skip. **First empirical cool-through-yield**: S drops 1.0 → 0.507 during drive, recovers to 0.983 post-drive. Mechanism from doc 59_ now alive. |
| 2026-04-24 | 0419b7e | Grant + agent | — | `research(L3 Stage 6 Step 5a): Phase 5e driver instrumented — Cosserat A²_μ peaks at 0.012 while K4 saturates` — instrumented Phase 5e shows K4→Cosserat coupling weakness empirically. K4 saturates fully (S → 0.5) but Cosserat A²_μ peaks at 0.012 — way below the 0.95 sat_frac threshold. |
| 2026-04-24 | d0609ad | Grant + agent | — | `research(L3 Stage 6 Step 5b): Phase 5e v2 with CosseratBeltramiSource + C1-C2 gate window discovery` — drove Cosserat directly via Beltrami source to A² → 3.34 (C1 satisfied at center). C2 still never satisfies under PLL. Exposes gate window incompatibility as architectural (ω_yield = π vs ω_Compton ≈ 1.795, ratio 0.571 = ω_Compton/ω_yield). |
| 2026-04-24 | 5f973b6 | Grant + agent | — | `test(L3 Stage 6): Retroactive engine saturation invariants — catches Flag-5e-A class regressions` — closes test-coverage hole. Engine integration tests now require `S_min < 1.0` actually drops below 1 during the test window. Catches the class of bugs where engine specs claim saturation but engine doesn't actually exercise the path. |
| 2026-04-24 | 453d350 | Grant + agent | — | `research(L3 Stage 6 Round 6): Single-electron-first pivot — doc 66_ suspends gate-adjudication thread` — doc 66_. Three sessions of pair-nucleation gate-adjudication (C1-C2 window, four Readings, PLL anchor, coupling weakness) suspended pending single-electron validation precondition. **§14.1 framing correction**: K4 and Cosserat are TWO complementary LC tanks (V_inc↔Φ_link translational + u↔ω rotational), not "two projections of one tank." K4-TLM exhaustion at node level (Vol 1 Ch 8:49-50) corpus-confirmed. Amplitude-bug discovery in `initialize_electron_2_3_sector` (peak |ω|=0.3π per doc 34 X4a/X4b, not √3/2·π). |
| 2026-04-24 | fbbc950 | Grant + agent | — | `test(L3 Stage 6 Round 6 Path A): Falsification — K4 V_inc alone is insufficient electron representation` — Path A 4-of-4 falsification. K4-only TLM eigenmode driver: N_crossings=0 (expected 3), R/r→0.281, α⁻¹=NaN, energy passes. All four failures trace to one mechanism (Cosserat ω at zero — charge/voltage leg without spin/current leg). Clean falsification informative-failure-at-maximum-strength. |
| 2026-04-24 | 815cd40 | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-G): Coupled K4+Cosserat eigenmode finder + field-mapping documentation` — doc 66_ §17.2 three-storage-mode mapping: ε² (strain → electric/capacitive), κ² (curvature → magnetic/inductive), V² (pressure → stored-potential). Three conjugate LC pairs (V_inc↔Φ_link, u↔u_dot, θ↔ω) oscillating 90° phase-locked. New script `coupled_engine_eigenmode.py` — outer-loop self-consistent eigenmode search. F17-I followup: all-C-state or all-L-state coupled seed not yet tried. |
| 2026-04-24 | — (uncommitted) | session agent | `cosserat_field_3d.py` `initialize_electron_2_3_sector` | Adds `amplitude_scale: float = 1.0` parameter for Path B's |ω|=0.3π correction per doc 66_ §14.3. Default preserves backward-compat; Path B callers pass `amplitude_scale = 0.3π / (√3/2·π) ≈ 0.3464`. |
| 2026-04-24 | — | session agent (r8 update) | §1 front-matter, new §1.5 Round 6 pivot summary, §2.3 [r8 reframe note], new §11.11 K4-TLM-exhausted, §13.5/§13.5a/§13.5b/§13.5c new entries (Phase 5 suspended, Phase 5e landed, Round 6 path A/B/C, strain-mask infrastructure), §13.7 scope table updated, §16.1 24 commit rows appended, §16.2 engine version history updated, §17 A24/A25/A26 added | **Manual r8 (hybrid scope).** Reflects 23 commits since r7 (a5bd1da → 815cd40) plus Round 6 single-electron-first pivot. Bumps engine to 4.0.0 (memristive Op14 = new state variable; PairNucleationGate = new physical axiom invocation). §1.5 surfaces canonical Round 6 content (three-storage-mode mapping, K4-TLM exhaustion, three-entropy distinction). §3 / §15 / §17.1-3 reorganization deferred to r9 once Round 6 closes. |
| 2026-04-24 | 4ba20f8 | session agent | — | `docs(L3 Stage 6 Round 6): VACUUM_ENGINE_MANUAL.md r8 hybrid-scope reconcile + first commit` — manual joins source control for the first time. Prior r0-r7 lived as untracked working-tree revisions. Going forward, each engine-changing commit lands with a synchronous manual edit per §1.2 maintenance protocol. |
| 2026-04-24 | 687b18d | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-I): Three LC-pair-coherent seed modes empirically tested` — adds `initialize_u_displacement_2_3_sector` (Cosserat u seeder) + `initialize_phi_link_2_3_ansatz` (K4 Φ_link seeder) + `seed_mode` parameter on coupled-engine eigenmode finder (mixed | all_c | all_l). Three-mode test at N=48 reveals **L_c coupling asymmetry** — `all_c` catastrophically diverges step 1, `all_l` bounded with monotonic Cosserat→K4 relaxation (no reverse channel), `mixed` runaway. A reciprocal LC coupling would oscillate energy between sectors at ω_C; observed pattern is one-way energy pump. Doc 66_ §18 added. F17-H (audit doc 54_ §6 L_c derivation) now load-bearing. |
| 2026-04-24 | — | session agent (r8.1 update) | §13.5b F17-I results table, §17.1 A27 new (L_c asymmetry), §17.3 summary + critical-path blockers updated (F17-H now load-bearing) | **Manual r8.1.** First synchronous edit under the "manual joins source control" protocol — reflects F17-I three-mode test commit `687b18d`. Engine version 4.0.0 → 4.0.2 (test-only changes; new seeders + driver parameter, no new engine state). New audit finding A27 (L_c empirical asymmetry); F17-H derivation audit identified as new critical-path blocker. |
| 2026-04-24 | — | session agent (r8.2 update) | §11.2 closed (NodeResonanceObserver landed `719f3ec`), §11.3 closed (PairNucleationGate code landed `9ecc2ca`; firing ⏸ suspended in Round 6), §16.3 doc index extended (docs 58-66 + Round 6 era group), §16.4 engine code index Classes column rebuilt (PairNucleationGate, BondObserver, DarkWakeObserver, CosseratBeltramiSource, SpatialDipoleCPSource, helpers, seeders), §16.5 canonical drivers extended (v2_reproducibility_seed_sweep, flux_tube_persistence, node_resonance_validation, phase5*, coupled_engine_eigenmode, tlm_electron_soliton_eigenmode) | **Manual r8.2.** Cleanup pass for stale content I deferred from r8 hybrid scope — §11.2/§11.3 limits closed, §16.3-§16.5 indices extended to current engine + research state. No new engine commits since r8.1; this is documentation-only catch-up to bring the indices in line with the §1.5 / §13 / §16.1 content from r8/r8.1. Engine version unchanged (4.0.2). |
| 2026-04-24 | abe23ea | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-H): Doc 67_ — L_c coupling reciprocity audit + path 1 derivation` — F17-H derivation. Lagrangian variation `δL_c/δV = 2V·W_refl/V_SNAP²` derived; identifies structural mismatch between Op14 z_local modulation (impedance change) and δL_c/δV-derived EMF source (energy injection). Path-1 EMF derivation (continuous: `dΦ/dt = -V + (2V·W_refl)/(C·V_SNAP²)`; TLM discrete: `Phi_link += (V_avg + EMF_c)·dt`). Four open questions Q67-A through Q67-D. |
| 2026-04-24 | f6b56dd | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-H): Doc 67_ §12 — Q67-A/B/C/D audit closures` — closes the four open questions from `abe23ea`. |
| 2026-04-24 | 77a13a3 | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-H): Doc 67_ §13 — closed-form δL_c_asym/δV derivation` — Phase 4 asymmetric L_c variation closes Q67-C: `_coupling_energy_total_asymmetric` (the active default per `use_asymmetric_saturation=True`) gives a structurally different EMF formula. |
| 2026-04-24 | 3d7fae4 | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-H): Path-1 EMF implementation + §14 Vol 4 Ch 1 redundancy concern (A28-candidate)` — implements path-1 EMF via opt-in `use_lagrangian_emf_coupling` flag. **§14 surfaces Vol 4 Ch 1 redundancy concern** (A28-candidate: Op14 z_local IS the K4-TLM varactor; adding L_c-derived EMF would be a third redundant channel). Path-1 thus implemented THEN pre-emptively flagged as wrong direction. |
| 2026-04-24 | 85bdb6f | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-H): Doc 67_ §15 — Q67-E reconciliation finds A28 (double-counting hypothesis)` — Vol 4 Ch 1 cross-check confirms the redundancy concern. Three findings: (1) V_yield vs V_SNAP scale mismatch (pre-existing F17-L); (2) Op14 IS the K4-TLM varactor (Vol 4 Ch 1:130 `C_eff(V) = C₀/S(V)` extended with cross-sector A²_Cos); (3) L_c = ∫W_refl_asymmetric dx³ is DERIVED (W_refl emerges from K4-TLM scatter + connect with z_local modulation, not Lagrangian-fundamental). **A28 conclusion: K4↔Cosserat coupling double-counted since Phase 4 (`a5bd1da`).** Path-1 EMF was the wrong fix; correct fix is REMOVE the redundant `_compute_coupling_force_on_cosserat` channel. Methodology slip acknowledged in §15.6 (relayed audit concern #5 — Vol 4 Ch 1 cross-check — would have surfaced this on first reading). |
| 2026-04-24 | 05b130f | Grant + agent | — | `fix(L3 Stage 6 Round 6 A28): disable_cosserat_lc_force flag — empirically confirmed F17-H resolution` — implements `disable_cosserat_lc_force` flag (default False preserves legacy). When True, `_compute_coupling_force_on_cosserat` returns zero arrays. F17-I three-mode under A28: all_c step-1 \|ω\| 1030 → 0.566; mixed 222 → 0.137; all bounded under 1.0 over 100 steps. **Six prior failure modes (Path A/B/C/F17-G/F17-I/path-1 EMF) all unified under one bug.** 22/22 backward-compat tests pass with flag off. F17-H STRUCTURAL CONCERN RESOLVED. |
| 2026-04-25 | ff15c4b | Grant + agent | — | `fix(L3 Stage 6 Round 6): enable_cosserat_self_terms flag + A28 auto-suppresses redundant k_refl + Path B forms bound state at N=80` — `enable_cosserat_self_terms` flag re-enables Cosserat self-terms (`k_op10`, `k_refl`, `k_hopf`) that were disabled at init lines 231-233 because *"reflection is carried by the coupling term."* When BOTH `disable_cosserat_lc_force=True` AND `enable_cosserat_self_terms=True`, **auto-suppresses `k_refl=0`** (the redundant reflection force at Cosserat-self level) while keeping `k_op10=1` and `k_hopf=π/3` (different physics). **Path B at N=80, R=20, r=R/φ², peak \|ω\|=0.3π forms (2,3) bound state for the first time in Stage 6** — c=3 + shell_Γ² ≈ 4 + R/r ≈ φ² preserved through step 20; degrades by step 50 (drift expected without Op6 self-consistency). 22/22 backward-compat tests pass. F17-I three-mode under combined fix: all_l + mixed both preserve (2,3) c=3 through step 5. |
| 2026-04-25 | — | session agent (r8.3 update) | §1 front-matter (r8.3, HEAD ff15c4b, engine 4.0.4); new §6.4a engine-config flag table; §11.4 partially closed under Round 6 Path B; §13.5b Path B status FORMING BOUND STATE; §13.5c strain-mask infrastructure DEFERRED; new §13.5d Op6 self-consistency outer loop in progress; §13.7 scope table updated; §16.1 7 commit rows appended; §16.2 engine version history extended (4.0.3, 4.0.4); §16.3 doc 67 added; §17 A27 reframed (closed via A28 not via path-1 EMF), A28 new (double-counting), F17-L new (V_yield/V_SNAP scale mismatch); §17.3 critical-path blockers updated | **Manual r8.3.** Catches up on three engine-changing commits since r8.2 (`3d7fae4`, `05b130f`, `ff15c4b`) plus four research-doc commits (`abe23ea`, `f6b56dd`, `77a13a3`, `85bdb6f`). Major Round 6 result: Path B forms (2,3) bound state at N=80 step 20 first time in Stage 6 under A28 + Cosserat self-terms re-enable. Strain-mask ~550 LOC infrastructure deferred — A28 was the actual gate. F17-H structurally resolved via A28 reframing (path-1 EMF was wrong direction; structural finding inverted from "L_c is non-reciprocal, ADD EMF" to "engine has redundant force, REMOVE it"). Six prior failure modes unified under one bug. Op6 self-consistency outer loop in progress (uncommitted working tree); convergence is the gate for Round 6 closure. |
| 2026-04-25 | a53ce1c | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K Phase 1): Ax-3 noncompliance audit + phase-quadrature methodology` — F17-K Phase 1. Identifies that all six prior Round 6 failure modes (Path A/B/C/F17-G/F17-I/path-1 EMF) share a deeper unifying root than A28: methodology was Axiom-3 noncompliant. Per Vol 1 Ch 1:51-75 canonical numbering, Ax 3 = Effective Action Principle = `|S₁₁|²` minimization on phase-space (V_inc, V_ref) phasor coordinates. Cartesian shell extraction + raw `step()` time-evolution were wrong observable + wrong action principle. New doc 68_ + doc 67 §18 + manual A29 land the framing correction. |
| 2026-04-25 | 4d4b4aa | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K Phase 5a-b): phase-quadrature seed under raw step() dynamics is NOT sufficient` — empirical falsification: three seed configs (Path B control, chirality=0, chirality=1) all fail to produce phase-coherent eigenmode under raw `VacuumEngine3D.step()` dynamics. E_total_cov 0.15-0.67 vs 0.01 threshold; correlation oscillates sign; K4 monotonically drains. Five-fallacy mid-interpretation audit caught + rebuilt diagnostic. |
| 2026-04-25 | 6158465 | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K Phase 5c v1): coupled S₁₁ relaxation infrastructure built; v1 run is spurious convergence` — Phase 5c-1/2/3 (~290 LOC) implements coupled K4+Cosserat S₁₁ relaxation in `coupled_s11_eigenmode.py` (jit-compiled `_total_s11_coupled`, JAX `value_and_grad` over (u, ω, V_inc), backtracking line-search descent mirroring `cosserat_field_3d.py:relax_s11`). v1 run empirically falsifies unconstrained descent: descent escapes by over-saturating Cosserat (peak \|ω\| 0.94 → 2.19, doubling past saturation onset). Spurious "convergence" at iter 38 with 3% obj reduction. |
| 2026-04-25 | 795c4ff | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K corpus-search): constrained S₁₁ + Ch 8 algebraic pins resolves Phase 5c-v2 direction` — Rule 8 corpus-grep across manuscript + L3 research + sibling repos. doc 34_ X4 verbatim: *"imposing constraints on top of S11 minimization, not by switching to a different objective... three hard algebraic constraints (d=1, R−r=1/2, R·r=1/4) are algebraic pinnings, not emergent minima."* Phase 5c v2 plan: add Lagrange penalties on Ch 8 geometric constraints. |
| 2026-04-25 | 3f6d544 | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K acoustic-cavity): natural-equilibria reading + Helmholtz framing refines §22 Lagrange-penalty plan; F17-K Phase 6 flagged` — second corpus search on acoustic-cavity / Helmholtz / standing-wave vocabulary. Two findings: (1) Acoustic-cavity / Helmholtz framing is corpus-canonical (Vol 2 Ch 7 de-broglie-standing-wave: *"reinterpret the Schrödinger Wave Equation deterministically as the continuous Helmholtz acoustic resonance of the LC vacuum"*) — DUAL ontological framing alongside Phase 1 |S₁₁|² action principle. (2) Doc 03_ §4.3 reading: Ch 8 constraints (d=1, R−r=1/2, R·r=1/4) are NATURAL EQUILIBRIA emerging from Axiom-4 saturation + topology, NOT constraints to impose by hand. **F17-K Phase 6 sparse eigensolver flagged** as candidate methodology for v3+ if descent-based methods hit limits. |
| 2026-04-25 | 2c873cf | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K Phase 5c-v2): dual descent — Cosserat-energy escapes Golden Torus geometry; corpus-duality FALSIFIED at coupled-engine scale` — Phase 5c-v2 (v1 of v2) implements dual descent (Cosserat-energy + |S₁₁|² in parallel) with tanh reparameterization for amplitude bounding (~280 LOC). **Premature Finding 3** ("corpus-duality falsified") landed but was empirically confounded — both descents ran at WRONG amplitude (energy 0.61 sub-saturated, S₁₁ 2.31 over-saturated). tanh BOUNDS amplitude at ω_yield=π but doesn't PIN at saturation onset (peak \|ω\|≈0.94). Pre-committed retraction language in commit message: *"if data changes, Finding 3 gets explicitly retracted."* |
| 2026-04-25 | 4c9fbea | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K Phase 5c-v2-v2): saturation-pin debug + dual descent confirms doc 03_ §4.3 empirically — Golden Torus is topologically selected, not dynamically derived` — Phase 5c-v2-v2. Hard projection onto saturation manifold (peak \|ω\| = 0.9425 enforced after each step) replaces tanh reparameterization. Saturation-pin enables real S₁₁ descent (obj reduction 3% → 99.76%). At correct amplitude (saturation onset, both descents pinned), final result: Cosserat-energy converges at R/r=3.40 (78 iters); coupled S₁₁ converges at R/r=1.03 (500 iters, still descending). Neither at Golden Torus φ²=2.62; 3.3× spread between them. **`2c873cf`'s premature Finding 3 explicitly retracted; same conclusion now lands with proper evidence at correct amplitude.** Doc 03_ §4.3 empirically validated: *"R·r = 1/4: topologically quantized, NOT dynamically derived... the Lagrangian must be consistent with but does not by itself produce."* (C) X4b stationarity verification implicitly resolved: Golden Torus is NOT a stationary point of either coupled objective at saturation onset; gradient at Golden Torus is nonzero in both. F17-K methodology arc closes empirically; v3 path forward: (i) algebraic Ch 8 pinning per doc 34 X4 corpus-canonical (~80 LOC), or (ii) sparse eigensolver per Helmholtz framing (~300 LOC). |
| 2026-04-25 | — | session agent (r8.4 update) | §1 front-matter (r8.4, HEAD `4c9fbea`, engine 4.0.4 unchanged); §13.5b Path B "FORMING BOUND STATE" claim WALKED BACK (twice-confounded: wrong observable + wrong amplitude); §13.5d Op6 outer loop DEPRECATED (subsumed by F17-K); new §13.5e F17-K methodology arc narrative + empirical closure; new §13.5f v3 path forward (algebraic Ch 8 pinning OR sparse eigensolver); §13.7 scope table updated; §16.1 8 commit rows appended; §16.3 doc 67 §18-§25 + doc 68 references; §17 A29 extended with full F17-K arc, A30 new (corpus-duality at coupled-engine scale falsified empirically; doc 03 §4.3 validated), A31 new (Phase 6 sparse eigensolver candidate); §17.3 critical-path blockers updated for v3 path | **Manual r8.4.** Catches up on the F17-K methodology arc — seven research-doc commits since r8.3 (`a53ce1c`-`4c9fbea`). No engine-flag commits. Major Round 6 finding: corpus-duality (S₁₁ ≈ Cosserat-energy minima at Golden Torus per AVE-Protein scale-invariance) FALSIFIED at coupled-engine scale; doc 03_ §4.3 empirically validated (topology is quantized, not dynamically derived). r8.3 "Path B forms bound state through step 20" claim formally walked back as twice-confounded (wrong observable per F17-K Phase 1 + wrong amplitude per F17-K Phase 5c-v2-v2). Round 6 closure now ~80 LOC of v3 (i) algebraic Ch 8 pinning away; if (i) succeeds, single-electron validation closes and Phase 5 gate work resumes; if (i) fails, v3 (ii) sparse eigensolver becomes empirically motivated. |
| 2026-04-25 | 3fede52 | Grant + agent | — | `research(L3 Stage 6 Round 6 F17-K v3 (i)): X4b linear-stability test — Golden Torus is UNSTABLE under coupled S₁₁, MARGINAL under Cosserat-energy` — F17-K v3 (i) implementation per doc 34 X4b methodology extended to coupled engine (~150 LOC `coupled_s11_eigenmode.py::run_v3_x4b_linear_stability`). Initialize EXACTLY at Golden Torus → project ω onto saturation manifold → add 1% random δ → run `relax_with_pin` 30 iters → measure perturbation growth rate. Result: Cosserat-energy MARGINAL (δ_ratio 1.81×, +0.0198/iter); coupled S₁₁ UNSTABLE (δ_ratio 5.31×, +0.0556/iter exponential). Both runs preserved c=3 + saturation pin; R drift 4.88% (single-lattice-unit). **Combined with v2-v2 global-flow finding (`4c9fbea`): coupled engine has NO linearly stable bound state at Golden Torus geometry under either objective.** Cosserat-only X4b stability (doc 34 X4b) does NOT extend to coupled engine; K4 sector adds geometric instabilities at linear-perturbation level. Doc 03 §4.3 fully empirically anchored at both global-flow and linear-stability levels. Phase 6 sparse eigensolver methodology becomes load-bearing for Round 6 closure (~300 LOC). r8.4's "v3 (i) is closure gate" framing partially walked back. |
| 2026-04-25 | c830f07 | Grant + agent | — | `research(L3 Stage 6 Round 6 bootstrap-chain): Q = 1/α = 137.036 holds at constants level (rel_err 6.5e-11); bare K4 single-bond ≠ LC tank — structural finding` — auditor-recommended bootstrap-chain calibration anchor before committing to Phase 6 ~300 LOC. Two tests run (~270 LOC, ~30 min). **Test A — single-bond simulation** (`single_bond_q_test.py`, ~150 LOC): bare K4Lattice3D N=8, V_inc=0.05 on one A-B bond, run scatter+connect 200 steps. Result: peak resonance period = 2.0 steps (Nyquist limit), expected = 8.89 steps (Compton period in natural units). 4.4× off. Trajectory shows step-by-step alternation = K4-TLM scatter+connect inherent 2-step grid structure (wave shuttling A↔B at lattice c), NOT Compton-frequency oscillation. **Bare K4 ≠ LC tank empirically.** Vol 4 Ch 1 LC tank model is a CONTINUUM analog; L_e (kinetic inductance from electron mass) emerges from Cosserat constitutive moduli (G, K, ρ_inertia). Compton resonance ω = 1/√(L·C) requires BOTH sectors active. **Test B — constants-level scalar verification** (`bootstrap_constants_check.py`, ~120 LOC): compute L_e, R_TIR, Q from SI input constants. Identity 1: ω_C·L_e = ℏ/e² = 4108.236 Ω (rel_err 4.43e-16, machine precision). Identity 2: Q = ω_C·L_e/R_TIR = 1/α = 137.036 (rel_err 6.53e-11, machine precision). **Bootstrap chain VALIDATED at constants level.** Q = 137 in AVE is a definitional identity chained through SI input constants, not an empirical lattice measurement. Smallest "unknot O₁" in AVE is the smallest COUPLED (K4 + Cosserat) oscillator. Empirical Q manifestation in lattice dynamics is F17-K's open work (requires coupled engine), NOT bootstrap-chain calibration concerns. Auditor framing held: F17-K findings independent of single-bond Q calibration; both useful, separate concerns. |
| 2026-04-25 | — | session agent (r8.5 update) | §1 front-matter (r8.5, HEAD `c830f07`, engine 4.0.4 unchanged); §13.5f v3 path UPDATED (v3 (i) RAN — Golden Torus geometrically unstable; v3 (ii) Phase 6 eigensolver now load-bearing); new §13.5g v3 (i) X4b linear-stability empirical detail; new §13.5h bootstrap-chain test (Test A + Test B); §13.7 scope table extended with v3 (i) / bootstrap-chain rows + Phase 6 load-bearing row; §16.1 3 commit rows appended (`3fede52`, `c830f07`, this); §16.3 doc 67 §26 added; §17 A32 new (Golden Torus geometric instability at coupled scale; both global-flow and linear-stability levels), A33 new (smallest unknot O₁ in AVE is the smallest COUPLED oscillator, not bare K4); §17.3 critical-path blockers updated for v3 (ii) Phase 6 path | **Manual r8.5.** Catches up on two F17-K commits since r8.4 (`3fede52` v3 (i) X4b linear-stability + `c830f07` bootstrap-chain test). No engine-flag commits. Two substantive findings: (1) Golden Torus geometrically UNSTABLE at coupled scale under both objectives at linear-perturbation level — confirms doc 03 §4.3 alongside global-flow finding from r8.4. (2) Q = 1/α = 137 holds algebraically at machine precision; bare K4 ≠ LC tank empirically; smallest unknot O₁ is coupled (K4 + Cosserat) oscillator. r8.4's "v3 (i) algebraic Ch 8 pinning is the closure gate" framing partially walked back: v3 (i) ran, found Golden Torus geometrically unstable, so v3 (ii) Phase 6 sparse eigensolver (~300 LOC) becomes load-bearing for Round 6 closure. Phase 6 implementation is now the single-electron-validation closure gate. Bootstrap-chain test confirms Q=137 corpus identity holds at constants level — F17-K is downstream methodology question, not bootstrap calibration concern. |
| 2026-04-25 | 01bbec3 | Grant + agent | — | `research(L3 Stage 6 Phase 5 resume): doc 70_ — ansatz-seeded pair-nucleation methodology per Round 6 finding` — doc 70_ Phase 5 resume methodology (~19.7 KB). Per Round 6 closure ("topology can be encoded via ansatz initialization"), frames Phase 5 PairNucleationGate resumption as ansatz-seeded driver decoupling three orthogonal questions: (α) gate mechanism works given C1∧C2 satisfied by construction; (β) seeded pair persists post-drive (Kelvin protection claim); (γ) C1/C2 reached under drive (original Phase 5 question). Pre-Round-6 conflated all three; ansatz-seed approach isolates (α)+(β) from (γ). |
| 2026-04-25 | ede4008 | Grant + agent | — | `research(L3 Stage 6 Phase 5 resume): ansatz-seeded driver — case (b'): point-rotation Beltrami unstable in Cosserat self-dynamics; G-13 injection-profile upgrade empirically activated` — Phase 5 ansatz-seeded driver (~250 LOC `phase5_pair_nucleation_ansatz_seeded.py`) at registered config (N=24, amp=0.5·V_SNAP, λ=3.5, head-on autoresonant collision). Seeded Beltrami-bound-pair at central A=(10,10,10), B=(11,11,11), port 0. **Drive-on result:** \|ω\|_A 1.414 → 0.013 (drive-end) → 0.091 (post-drive); Φ_link constant +1.000; c_cos final 1; peak \|ω\|_global 0.091. **No-drive sanity check:** \|ω\|_A 1.414 → 0.10 in ONE Velocity-Verlet step (93% loss). Dissolution INTRINSIC to engine self-dynamics, NOT drive-induced. **Two findings:** (b') Gate's `_inject_pair` profile (point-rotation Beltrami + Φ_link) is fundamentally unstable; same physics as F17-K Round 6 finding for (2,3) electron at coupled scale (Cosserat self-terms don't stabilize unprotected localized topology). Activates §9 G-13 contingency empirically: upgrade to localized Hopf fibration or (2,3) torus-knot injection. Φ_link "persistence" disambiguated as measurement artifact (per A29: derived flux observable, not primary state). **Adjudication: case (b') — gate's INJECTION PROFILE needs upgrade, not C1/C2 threshold logic.** New finding A34 in §17.1. |
| 2026-04-25 | e1f6eac | Grant + agent | — | `research(L3 Stage 6 Phase 5 resume): doc 70_ §7.5 — clarify R5.10 Readings 1-4 two-level status (per external audit)` — single-line clarification per external audit caught wording inconsistency between commits 01bbec3 ("PRE-EMPTED") and ede4008 ("NOT pre-empted, reopen at threshold-revision level"). Reconciled at two different epistemic levels: PRE-EMPTED at original Round 5 framing (the four Readings argued about C2 INTERPRETATION under ambiguous threshold satisfaction; ansatz-seed makes thresholds unambiguous-by-construction, retiring the interpretation debate); MAY REOPEN at threshold-revision level (different epistemic level) after topologically-protected injection profile is implemented and tested. Two separate questions at two epistemic levels — neither "dead" nor "pending in original form." |
| 2026-04-25 | — | session agent (r8.6 update) | §1 front-matter (r8.6, HEAD `e1f6eac`, engine 4.0.4 unchanged); new §13.5i Phase 5 resume case (b') + G-13 activation + (α/β/γ) decoupling + R5.10 two-level disambiguation; new §13.5j Round 7 Stages 1+2 candidates scoped; §13.7 scope table extended with Phase 5 resume row + Round 7 Stage 1+2 rows + Round 6 + Phase 5 closure row; §16.1 4 commit rows appended (`01bbec3`, `ede4008`, `e1f6eac`, this); §16.3 doc 70 added to research-doc index; §17 A34 new (point-rotation Beltrami injection profile fundamentally unstable in Cosserat self-dynamics; G-13 upgrade required); §17.3 critical-path blockers updated for Round 7 Stages 1+2 path | **Manual r8.6.** Catches up on three Phase 5 resume commits since r8.5 (`01bbec3` doc 70_; `ede4008` ansatz-seeded driver case (b'); `e1f6eac` R5.10 two-level disambiguation). No engine-flag commits. **Round 6 + Phase 5 resume close discipline-completely on this side.** Phase 5 case (b') finding empirically reinforces Round 6 finding at a different scale: dynamics don't stabilize unprotected localized topology. G-13 contingency activated. R5.10 Readings 1-4 disambiguated at two epistemic levels. Two Round 7 Stage candidates scoped: Stage 1 Phase 6 sparse eigensolver (~300 LOC closes single-electron representation); Stage 2 topological pair injection driver (~200 LOC closes Phase 5 gate firing). Both deferred to fresh sessions per the Round 6 closure plan. |
| 2026-04-25 | 1bc1652 | Grant + agent | — | `research(L3 Stage 6 Round 7 Stage 0): basin audit — doc 71_ methodology + P_basin_audit_GT_stationarity + driver scaffold (no run)` — Round 7 Stage 0 basin-audit-as-precondition framing scaffold. doc 71_ basin_audit_methodology.md (~12 KB §1-§12 covering rationale, integrator-mode TDI choice, A26 contamination guard, six-seed sweep design, pre-registered prediction `P_basin_audit_GT_stationarity` with three failure modes, driver scope, run result, v2 draft). Driver `phase5_basin_audit.py` (~364 LOC) at sub-lattice geometry (R/r literal cell counts vs. ratio). v1 fresh-session run halted by A26 amplitude-guard at step 0 — geometry bug surfaced rather than basin-mapping data collected. v2 draft never executed. **NOTE: this commit's framing was retracted in subsequent self-audit (`c69e79c`). Retained as Rule 12 audit trail; basin-audit scaffold remains in repo as informational tooling for hypothetical Round 8 contingency only.** |
| 2026-04-25 | c69e79c | Grant + agent | — | `research(L3 Stage 6 Round 7): self-audit pivot — basin-audit retracted (Rule 6/8/10 violation); R7.1 strengthened to multi-seed sparse eigensolver; doc 71_ renamed + reframed; P_phase6_eigensolver_multiseed pre-registered` — within-session self-audit triggered by Grant directive ("review COLLABORATION_NOTES, are you trapped in known patterns?") found basin-audit-as-Stage-0 framing was a multi-rule violation: **Rule 6** (TDI gradient descent on Cosserat W is SM-style minimization where corpus-native concept for bound state is standing-wave eigenmode of K4+Cosserat dynamics per doc 67_ §23.4 Helmholtz / acoustic-cavity formulation); **Rule 8 inverse** (R7.1's sparse eigensolver IS the AVE-native tool; basin-audit reinvented R7.1's scope under worse language); **Rule 10 corollary** ("basin audit as Stage 0 precondition" became creeper compound across multiple turns without ever being pressure-tested against "just run R7.1 at multiple seeds, that IS the precondition"). **Reframe deliverables:** doc 71_ renamed `71_basin_audit_methodology.md` → `71_multi_seed_eigenmode_sweep.md` (§1-§12 retained as Rule 12 audit trail; §13 ACTIVE multi-seed R7.1 sparse eigensolver; §14 driver scope notes for fresh-session implementer); `predictions.yaml` `P_basin_audit_GT_stationarity` retained-with-RETRACTED-marker (Rule 12 body preservation) + `P_phase6_eigensolver_multiseed` NEW with frozen pre-registration (N=32, R_anchor=10, four seeds {GT_corpus, F17K_cos_endpoint, F17K_s11_endpoint, vacuum_control}, three-mode falsification, ω_Compton±α tolerance, Q±5%, shape correlation>0.85 vs doc 34 X4a); R7.1 strengthening from single-seed (GT only) to multi-seed (four seeds at SAME run); A35 audit finding. Self-audit caught framing error before R7.1 work itself committed to wrong scope. |
| 2026-04-25 | — | session agent (r8.7 update) | §1 front-matter (r8.7, HEAD `c69e79c`, engine 4.0.4 unchanged); new §13.5k Round 7 Stage 0 basin-audit RETRACTED + R7.1 strengthened to multi-seed sparse eigensolver (full Rule 6/8/10 walkthrough + reframe deliverables + three-mode falsification structure + v1 results status + auditor flags); §13.7 scope table strengthened R7.1 Stage 1 row to MULTI-SEED + Round 7 Stage 0 row added with retraction status + remaining critical-path total updated; §16.1 3 commit rows appended (`1bc1652`, `c69e79c`, this); §16.3 doc 71 entry updated for filename + scope change; §17 A35 new (basin-audit-as-Stage-0 was Rule 6/8/10 violation; family with A22 + A30 corpus-bypass at different layers; caught earlier in cycle than predecessors per within-session self-audit); §17.3 critical-path blockers updated for R7.1 multi-seed + R7.2 P_phase5_topological_injection-pre-reg-pending path; retraction summary table extended with A35 row | **Manual r8.7.** Catches up on two Round 7 commits since r8.6 (`1bc1652` basin-audit Stage 0 scaffold + `c69e79c` reframe pivot to multi-seed eigensolver). No engine-flag commits. **Mid-cycle self-audit caught Rule 6/8/10 framing error** before R7.1 implementation committed to wrong scope. R7.1 strengthened from single-seed (GT only) to multi-seed (four seeds at same run with three-mode falsification structure) — answers basin-vs-corpus geometry question + (2,3) eigenmode existence question in one run. Two auditor flags open at r8.7 close: §14.2 K4-amplitude-zero pitfall (Jacobian-block sanity check mandatory in driver); shape-correlation > 0.85 PASS gate may be over-strict (record as informational, flag for adjudication if other criteria pass). A35 audit finding placed in family with A22 + A30 (corpus-bypassing errors at different layers); caught earlier in cycle per within-session self-audit triggered by Grant directive. R7.1 + R7.2 still both fresh-session candidates; R7.2 still needs P_phase5_topological_injection pre-reg. |
| 2026-04-25 | 675141e | Grant + agent | — | `research(L3 Stage 6 Round 7): doc 72_ design-space articulation + reframe 3 — block Helmholtz on (V,ω) joint replaces Hessian-of-W; P_phase6_helmholtz_eigenmode_sweep frozen; Rule 10 commitment locks operator choice for fresh-session run` — external audit on r8.7 frozen pre-reg `P_phase6_eigensolver_multiseed` (Hessian-of-W multi-seed sparse eigensolver) caught deeper Rule 6 instance: Hessian-of-W is itself SM/QM-style energy stationarity on a wave-propagation substrate. Same-gap finding as A35 at deeper layer (precondition → operator). Grant directive ("understand the design/solution space that ave dictates" + "What's the smith chart for the vacuum? is it 3D?") invited design-space articulation BEFORE further pre-reg drafting. **Doc 72_ NEW (~26KB §1-§8)**: §1 four AVE-native concepts (wave eigenmode via Helmholtz NOT Hessian; impedance match via S₁₁-min NOT energy-min; topological quantization as input ansatz NOT dynamical attractor; AVE basin = S₁₁-min NOT W-min); §2 3D Smith chart for vacuum (Extension A `(Re(Γ), Im(Γ), ω)` recommended); §3.1 block Helmholtz on joint (V, ω) per audit Q1 hybrid-coupled-mode pushback (cross-blocks `C_Vω`, `C_ωV` encode Op14 explicit); §3.1.1 V=0 decoupling footnote (block decouples into V-block + ω-block simultaneously — strict superset of single-sector); §3.3 c_eigvec=3 binary + shape correlation > 0.60 informational two-tier (audit Q4); §3.4 sector-energy split diagnostic (audit Q1); §5 ~290 LOC budget; §6.1 **Rule-10 commitment language verbatim — fresh-session run committed to operator choice barring catastrophic methodology error**. Reframe deliverables: doc 71_ §13 retracted per Rule 12 (body preserved); §14 superseded driver scope notes preserved; §15 ACTIVE multi-seed block Helmholtz with quick-map vs §13. `predictions.yaml`: `P_phase6_eigensolver_multiseed` retained-with-RETRACTED-marker; `P_phase6_helmholtz_eigenmode_sweep` NEW frozen. New finding A36 — operator-choice Rule 6 violation; family with A22+A30+A35 at progressively earlier cycle latency. |
| 2026-04-25 | — | session agent (r8.8 update) | §1 front-matter (r8.8, HEAD `675141e`, engine 4.0.4 unchanged); new §13.5l Reframe 3 — block Helmholtz on (V,ω) joint replaces Hessian-of-W (full doc 72_ §1-§4 four-concept walkthrough + §3.1 block Helmholtz formulation + §3.1.1 V=0 decoupling caveat + §3.3 two-tier PASS criteria + §3.4 sector-energy split diagnostic + §6.1 Rule-10 commitment language verbatim + reframe deliverables + extended three-mode falsification reading with sector sub-readings); §13.7 scope table extended with multi-seed Hessian retraction row + doc 72_ landed row + R7.1 reframed-to-block-Helmholtz row + remaining critical-path total updated for r8.8; §16.1 2 commit rows appended (`675141e`, this); §16.3 doc 72 entry NEW + doc 71 entry updated for §15 ACTIVE; §17 A36 new (operator-choice Rule 6 violation — Hessian-of-W on wave substrate; family with A22 + A30 + A35); §17.3 critical-path blockers updated for R7.1 block Helmholtz path; retraction summary table extended with A36 row | **Manual r8.8.** Catches up on one Round 7 commit since r8.7 (`675141e` doc 72_ + reframe 3). No engine-flag commits. **External-audit-driven reframe** caught Hessian-of-W as Rule 6 violation at the operator level (deeper than A35 precondition-level Rule 6/8/10). Reframed via doc 72_ design-space articulation to **block Helmholtz on joint (V, ω) state**. Rule-10 commitment language landed verbatim in BOTH doc 72_ §6.1 AND this manual §13.5l so fresh-session implementer hits it twice. A36 finding placed in family with A22 (operator-level corpus-bypass) + A30 (corpus-claim-falsification) + A35 (precondition-level Rule 6/8/10) — same-gap instances at progressively earlier cycle latency, indicating audit + creeper-checking + design-space articulation discipline tightening across rounds. R7.1 + R7.2 still both fresh-session candidates; R7.1 frozen pre-reg locked by Rule 10; R7.2 still needs P_phase5_topological_injection pre-reg. |
| 2026-04-25 | ce5af9f | Grant + agent | — | `research(L3 Stage 6 Round 7): doc 73_ + reframe 4 — discrete K4-TLM scatter+connect + Cosserat (u,ω) LC-tank Hessian-of-W + Op14 cross-coupling; §6.1 catastrophic-error carve-out invoked; P_phase6_helmholtz_eigenmode_sweep RETRACTING` — reframe-4 of R7.1: block Helmholtz on (V, ω) joint replaced by joint discrete K4-TLM scatter+connect + Cosserat LC-tank Hessian-of-W with Op14 cross-coupling per audit on r8.8. Catastrophic-error carve-out invoked on-record. |
| 2026-04-25 | 8c44ef0 | Grant + agent | — | `research(L3 Stage 6 Round 7): doc 74_ + R7.1 reframe-4 run — Mode III at all 4 seeds (V-block comprehensive; Cos-block bottom-100-coverage); two implementation bugs caught + fixed per Rule 10` — first reframe-4 run. doc 74_ documents the run + bug fixes. |
| 2026-04-26 | b5ecc89 | Grant + agent | — | `research(L3 Stage 6 Round 7): three R7.1 follow-ups complete — Mode III at N=32 FALSIFIED as finite-N artifact; Mode I CANDIDATE at N=64 V-block GT_corpus (gap 0.45% < α/√2 PASS tolerance)` — second headline flip. |
| 2026-04-26 | b8d97d9 | Grant + agent | — | `research(L3 Stage 6 Round 7): topology check FALSIFIES Mode I candidate — N=64 V-block GT_corpus is BULK mode (shell fraction 1.13%, not (2,3) localized); third headline flip; Round 8 questions restored` — A39 v2 dual-criterion (frequency + topology) validates: frequency-only Mode I is insufficient; topology must concur. |
| 2026-04-26 | 1c89fa1 | Grant + agent | — | `research(L3 Stage 6 Round 7): freeze two pre-regs per Grant adjudication 2026-04-26 — Cos-block N=64 dual-criterion (shell threshold 80%) + R7.2 topological pair injection dual-criterion` — frozen pre-regs for joint R7.1+R7.2 final closure. |
| 2026-04-26 | d3adcc2 | Grant + agent | — | `research(L3 Stage 6 Round 7): joint R7.1 + R7.2 final closure — both Mode III; engine does NOT host (2,3) electron bound state in V or Cos sectors at corpus GT; Round 8 Φ_link sector cleanest gap` — **Round 7 closes empirically.** |
| 2026-04-26 | 88ec7c3 | Grant + agent | — | `research(L3 Stage 6 Round 7): doc 74_ §9 audit revisions — split A40 → A40 + A41 (methodology-meta + structural physics); add unified framework-level statement per audit on commit d3adcc2` — A40/A41 split. |
| 2026-04-26 | 53c2ce9 | Grant + agent | — | `research(L3 Stage 6 Round 7): freeze two new pre-regs per audit on commit 88ec7c3 — Test A (Cos-block N=64 c_eigvec recheck, 4-category) + Test B (doc 28_ §5.1 bond-scale phasor trajectory)` — Test A + Test B v1 frozen. |
| 2026-04-26 | b932a45 | Grant + agent | — | `research(L3 Stage 6 Round 7): freeze Test B v2 pre-reg per audit on commit 53c2ce9 — single-port temporal sampling can't answer doc 28_ §5.1 spatial-winding question; v2 samples 8 ports (4 at A + 4 at B) for spatial R/r per doc 26_ §3` — A44 spatial-multipoint correction (single-port temporal v1 was wrong-question). |
| 2026-04-26 | 7fea8f7 | Grant + agent | — | `research(L3 Stage 6 Round 7): Test B v2 Mode III-spatial empirical result + freeze v3 pre-reg at amp=0.85·V_SNAP for saturation-regime check per audit` — v2 Mode III-spatial; v3 frozen. |
| 2026-04-26 | 39f656a | Grant + agent | — | `research(L3 Stage 6 Round 7): doc 74_ §10 — three audit-flagged follow-up tests close negative-result envelope; Test A Mode III-both via corpus-canonical c=0 + Test B v2/v3 Mode III-spatial across linear+saturation regimes` — **doc 74_ §10.6 framework-level closure: "All seven tests Mode III."** Doc 28 §5.1 bond-scale phasor IS Test B v2/v3 — closed empirically. |
| 2026-04-26 | b11996d | Grant + agent | — | `research(L3 Stage 6 Round 8): freeze Move 5 pre-reg P_phase6_self_consistent_orbit_hunt — single-electron self-consistent orbit hunt at corpus GT (time-domain, no drive); tests corpus's actual standing-wave claim that linearized eigsolve necessarily misses` — Round 8 opens. |
| 2026-04-26 | c772211 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 5): Mode III-orbit per pre-reg BUT self-stable sub-corpus (2,3) orbit found empirically — engine hosts (2,3) plateau at peak |ω|=0.3044 for 150 Compton periods, migrating off corpus shell` — empirical handle for characterize-as-itself pivot per Rule 10 corollary. |
| 2026-04-26 | 97178c6 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 6): freeze pre-reg P_phase6_natural_attractor_characterization — fit (R_relaxed, r_relaxed) of Move 5's settled (2,3) attractor, test whether R/r = φ² at non-corpus absolute scale` — Move 6 frozen. |
| 2026-04-27 | 880165b | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 6): Mode III-natural (delocalized at search-grid boundary, spectrum non-physical) → meta-methodological pivot to characterize Move 5 attractor as itself` — Rule 9 v2 reframe pattern ("what is this thing?" before "is corpus thing here?"). |
| 2026-04-27 | 39444d0 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 7): freeze pre-reg P_phase1_attractor_characterization — descriptive characterization of Move 5 attractor with FROZEN EXTRACTION SCOPE (no PASS/FAIL); pivots away from "is corpus electron at config X?" pattern` — Move 7 frozen. |
| 2026-04-27 | dd63116 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 7b): freeze pre-reg P_phase1_attractor_characterization_v2_fft_fix — sample at top-5 |V_inc|² cells (not |ω|² centroid-displaced); fix Move 7's zero-V_inc/Nyquist-artifact FFT` — A49 centroid-of-shell sampling-bug catch (Rule 10 sampling-discipline corollary). |
| 2026-04-27 | 48d7cc9 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 7+7b): Phase 1 characterization complete — branch (b), (2,3)-topological at LATTICE CUTOFF (NOT corpus electron); auditor's Q≈2/α speculation dissolves at actual frequency` — Move 5 attractor characterized as self: (2,3) at lattice-cutoff, not corpus. |
| 2026-04-27 | 51463c2 | Grant + agent | — | `research(L3 Stage 6 Round 8 §13 amendment): correct FFT-as-leakage interpretation per Grant's dimensional-analysis check — attractor is STATIC fixed point, NOT lattice-cutoff oscillator; Move 9 (autoresonant drive at ω_C) becomes load-bearing` — dimensional cross-check (Rule 6 corollary) forces reinterpretation. |
| 2026-04-27 | fe83133 | Grant + agent | — | `research(L3 Stage 6 Round 8 §14): two-layer dimensional reconciliation — spin-½ half-cover (B canonical) + Op14 saturation as gravitational redshift (NEW); σ=4 Cos-block test predicts shell-localized (NOT core) Mode I` — A-008 SU(2)→SO(3) double-cover identification (m_Cosserat = 2·m_e). |
| 2026-04-27 | d4fda36 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 10): freeze pre-reg P_phase1_attractor_winding_characterization — static fixed point spatial topology characterization (torus knot vs Hopf-linked vs Y_lm) + per-cell A² at top-|ω|² cells (sets up §14.4 σ=4 Cos-block prediction)` — Move 10 frozen. |
| 2026-04-27 | c9e38c4 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 10): scipy API compat fix — sph_harm → sph_harm_y (scipy 1.15+ rename + swapped arg order); methodology-debug not pred-reframe per doc 73_ §6.2` — methodology-debug commit (no pred-reframe required). |
| 2026-04-27 | 89ba147 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 10 result + §15): static fixed point isn't shell-shaped, sectors spatially decoupled (A²≈0 at top-|ω| cells), Op10 c=3 carrier is none of the standard topology types; §14 framing partially superseded` — sectors decoupled at static fixed point; §14.4 σ=4 prediction superseded. |
| 2026-04-27 | e9fdf99 | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 11): freeze pre-reg P_phase1_attractor_reactance_tracking — close A-011 reactance gap (Φ_link + ω_dot computed but never read); PRE-MOVE-9 PRECONDITION` — A-011 reactance-tracking gap. |
| 2026-04-27 | 37f5d9d | Grant + agent | — | `research(L3 Stage 6 Round 8 Move 11 result + Move 11b freeze): H_cos drift 5.5% + ρ(T,V)=+0.366 (NOT LC reactance signature) — diagnostic redo with PML-filtered cells, full time series, drive verify, Pearson cross-correlation matrix` — A50 PML-cell-exclusion + Move 11b retest. |
| 2026-04-27 | 36d6e0d | Grant + agent | — | `research(L3 Stage 6 Round 8 Diag A): freeze pre-reg P_ax5_cosserat_wave_speed_amplitude_dependence — Cosserat wave-speed amplitude dependence test (pre-fix detection of V·S vs T·1 asymmetry, post-fix verification of fix)` — Diag A frozen. |
| 2026-04-27 | bfc58d8 | Grant + agent | — | `research(L3 Stage 6 Round 8 Diag A): Mode I per pre-reg — V·S vs T·1 asymmetry is real but empirically negligible at relevant amplitudes; Move 11 H_cos drift needs alternative explanation; Round 7+8 Mode III not from this mechanism` — V·S/T·1 asymmetry is real but empirically negligible. |
| 2026-04-27 | 391a3b5 | Grant + agent | — | `research(L3 Stage 6 Round 8 Diag A): doc 75_ §5.1 + §6 update — A=6 integrator-cliff is separate from V·S/T·1 asymmetry; Diag C source audit + Move 11b's already-measured Pearson matrix close the Move 11 H_cos drift question (Op14 trading, not missing physics)` — doc 75_ §6.3 engine fix specified. **A44 missing-axiom-vs-engine-bug diagnostic: engine bug not missing axiom.** |
| 2026-04-27 | fb2e4f1 | Grant + agent | — | `research(L3 Stage 6 Round 8): freeze pre-reg P_phase6_photon_tail_dual_seed — corpus electron test via 4-criterion phasor-space adjudication at engine-representable scale (N=64, R=4, r=1.5)` — photon-tail path (a) frozen. |
| 2026-04-27 | 13b2017 | Grant + agent | — | `research(L3 Stage 6 Round 8 Photon-Tail): Mode III 0/4 — dual-seed standing-wave IC at engine-representable scale catastrophically dissolves Cosserat (4% retention) while K4 partially survives (66% retention); sector asymmetry surfaced; path (b) propagating IC strongly motivated` — path (a) Mode III. |
| 2026-04-27 | bd15bb0 | Grant + agent | — | `research(L3 Stage 6 Round 8 path b): freeze pre-reg P_phase6_photon_tail_propagating_ic — propagating-IC photon-tail test (path b); 3/3 of C1/C2/C3 = Mode I (C4 informational per A57); sets ω_dot = ω_loop-rotation in (x,y) plane` — A57 C4-informational vs C1/C2/C3 binary framing. |
| 2026-04-27 | 1b48f4d | Grant + agent | — | `research(L3 Stage 6 Round 8 path b): photon-tail propagating-IC Mode III, near-identical to path (a) — round 8 photon-tail branch closed per pre-reg threshold; doc 75_ §11 + A58 (path-(a)/path-(b) empirical equivalence)` — **Round 8 photon-tail branch closes.** A58 path-(a)/path-(b) empirical equivalence. |
| 2026-04-27 | 75d1fde | Grant + agent | — | `manuscript(axiom homologation P1+P4+P5): canonicalize Scheme A — fix INVARIANT-S2 SiLU+ABCD misnomers, fix backmatter Ax 1↔Ax 2 swap, supersession banner on doc 76_` — INVARIANT-S2 SiLU/ABCD fix + backmatter Ax 1↔Ax 2 swap + doc 76_ supersession banner. |
| 2026-04-27 | 05f8ac3 | Grant + agent | — | `manuscript(axiom homologation P2): canonicalize eq_axiom_*.tex contents to Scheme A — separate calibration constants + derived gravity into dedicated files; foreword two-section split` — eq_axiom_*.tex canonical Scheme A. NEW: eq_calibration_constants.tex + eq_gravity_derived.tex. |
| 2026-04-27 | b460071 | Grant + agent | — | `research(L3 axiom homologation P3): doc 77_ Scheme-A canonical reframe of doc 76_; doc 76_ Rule 12 stub; doc 10_ §8(a) closed via doc 77_ §6.4` — doc 76_ → 77_ supersession via Rule 12. |
| 2026-04-27 | 69fd974 | Grant + agent | — | `research(L3 axiom homologation P3+): doc 75_ framing-error pass — "Ax 3 = energy conservation" → "Ax 4 asymmetric L/C, Noether-broken energy conservation"` — doc 75_ framing corrected per Scheme A. |
| 2026-04-27 | 6968398 | Grant + agent | — | `manuscript(axiom homologation P5+): promote axiom-homologation.md from .agents/handoffs/ to manuscript/ave-kb/common/ — citation chain consolidated within manuscript tree` — Rule 12 v2 cross-tree citation promotion (≥3 citations from tracked files). |
| 2026-04-27 | — | session agent (r8.9 update) | §1 front-matter (r8.9, HEAD `6968398`, engine 4.0.4 unchanged) — single-electron pivot closure baseline + axiom homologation; §13.7 scope table extended with R7.1 reframe-4 closure + R7.2 closure + Test A + Test B v2/v3 + Round 8 Move 5/6/7/7b/9/10/11/11b + Diag A + photon-tail (a)/(b) + doc 75_ Cosserat energy conservation finding + axiom homologation arc + closure synthesis pending + engine fix r8.10 pending; remaining critical-path total updated for r8.9 closure; §16.1 37 commit rows appended (`ce5af9f` → `6968398`); §17 A37 new (single-electron pivot Mode III canonical) + A38 new (T_kinetic Op14 saturation engine fix queued, doc 75_ §6.3) + A39 new (axiom homologation Scheme A canonicalized); §17.3 critical-path blockers updated for closure synthesis path; retraction summary table extended with A37-A39 rows | **Manual r8.9 — single-electron pivot closure baseline.** Catches up on 37 commits since r8.8 spanning Round 7 reframe-4 + R7.1+R7.2 closure, all of Round 8, and the axiom homologation arc. **No engine-state changes** — version unchanged at 4.0.4. **L3 single-electron-first validation closes empirically** with Mode III canonical for "engine hosts corpus (2,3) electron at corpus Golden Torus geometry under any tested config." Seven pre-registered tests at varied configurations all returned Mode III (per doc 74_ §10.6 framework-level closure statement). Engine fix per doc 75_ §6.3 (T_kinetic Op14 saturation) queued as r8.10 housekeeping; per Diag A empirically negligible at relevant amplitudes — fix doesn't flip the Mode III statement. **L3 branch closure synthesis is the next deliverable** (~1 fresh session); engine fix and closure synthesis are independent and can land in either order. Phase 5 pair-nucleation work remains structurally suspended; any future resumption would be downstream of an engine architectural change. **Auditor lane retroactive correction:** earlier r8.9 draft asserted "doc 28 §5.1 single-bond phasor pending since pre-Round-6, must run before engine fix" per a stale belief carried through review — this was wrong (Test B v2/v3 IS doc 28 §5.1, ran 2026-04-26, all Mode III-spatial). Corrected per A43 strengthening (auditor must verify research-doc state before asserting test-pending; auditor-side creeper compound) landed in COLLABORATION_NOTES same-session. |
| 2026-04-27 | `a535090` → `466d8c4` | Grant + agent | — | `research(L3 Stage 6 Round 9 path α v1): canonical doc 28 §5.1 phase-space single-bond phasor test on Move 5's saturated attractor — Mode III with caveats` — pre-reg `P_phase8_canonical_phase_space_phasor` frozen at `a535090`, run at `466d8c4`. Result: Mode III nominal (C1 R/r=3.84 vs target φ²=2.62 FAIL; C2 chirality 50% TIE FAIL); persistence 33% (below 40% guard); chirality cross-products noise-dominated. Doc 78_ + A59 methodology gaps (recording window, Hilbert chirality, bipolar R/r, single-cell-vs-bond-pair sampler). |
| 2026-04-28 | `f3886d1` → `9f565d6` → `95a017c` | Grant + agent | — | `research(L3 Stage 6 Round 9): doc 79 v3-v4.x closure synthesis evolution + doc 80 Kelvin/Helmholtz precedent companion` — closure synthesis drafted (lemniscate-with-q-half-twists primary AVE-native plumber framing for (2, q) particle family); v3 → v4.1 added Virial rest-energy; v4.2 added Meissner = magnetic-moment generator (§6.7) + path α reframe (§3.5.4); v4.3 V_yield ↔ V_SNAP distinction. Doc 80 traces 19th-century vortex-atom → Faddeev-Niemi historical lineage. Three-regime taxonomy from regime analysis (linear / symmetric gravity / asymmetric particle) per Rule 14 substrate-derives. |
| 2026-04-28 | `6d27e58` | Grant + agent | — | `research(L3 Stage 6 Round 9 path α v3 + L3 v5.1 AMENDMENT): (δ) 3D-aligned ω-vector test — Mode III canonical + ONE STRUCTURAL PARTIAL POSITIVE` — path α v3 tests auditor (δ) interpretation (c=3 in (2,3) maps to 3 orthogonal Cosserat ω-rotation axes). 4 files +1259/-17. **Result:** Mode III on R/r=φ² across all 5 sampler views (3D ω-PCA / per-axis x/y/z / magnitude pairing) + ONE STRUCTURAL PARTIAL POSITIVE: 100% CCW chirality on (Φ_link, |ω|) magnitude pairing across 8/8 bonds (null baseline ~50/50). (δ) empirically falsified (planarity 0.47-0.54 vs target <0.1; e2/e1 ≈ 1.25 vs φ²=2.618). **Meissner-asymmetric mechanism partly empirically anchored** via chirality direction matching K4 RH substrate prediction. Doc 79 v5.1 lands as canonical L3 empirical-record closure: Mode III canonical on R/r=φ² across 10 tests + chirality partial positive. Three surviving structural-reason branches (α/β/γ) + (δ) falsified. |
| 2026-04-28 | `cfb203a` | Grant + agent | — | `research(L3 post-closure follow-up): doc 81 — coverage analysis + (ε) bound-state-vs-free-state PROVISIONAL synthesis + Round 10+ Direction 3/3' concrete briefs + A43 v7/v8 lane-symmetric implementer-side instances` — research-tier follow-up (NOT v5.2 amendment, per closure-revision discipline). 1 file +258 lines. §2 coverage: path α tested ~2 of ~7 predicted observable dimensions; §3 (ε) PROVISIONAL extends doc 28 §5.3 + doc 79 §6.6; §4-5 Direction 3 (Op14/16/20/22 multi-operator) + Direction 3' (substrate-analog-of-(n,l,m_l) derivation) concrete briefs; §6 A43 v7 (fabricated verbatim quote) + A43 v8 (synthesis-as-corpus framing) lane-symmetric instances. Eight A43 instances total (six auditor-side + two implementer-side). |
| 2026-04-28 | — | session agent (r8.10 update) | §16.3 doc index extended with doc 81; §16.1 4 commit rows appended (`a535090`-`466d8c4`, `f3886d1`-`95a017c`, `6d27e58`, `cfb203a`); closure-pending footer → r8.10 closure-shipped state; COLLABORATION_NOTES A43 v2 strengthening landed with 8 worked examples (auditor-lane same-session) | **Manual r8.10 — L3 closure shipped + post-closure follow-up.** Catches up on path α v1/v2/v3 + closure synthesis evolution v3→v5.1 + doc 80 Kelvin precedent + doc 81 follow-up. **L3 branch CLOSED at v5.1: Mode III canonical on R/r=φ² across 10 tests + structural partial positive on chirality (Meissner-asymmetric mechanism partly empirically anchored via 100% CCW on (Φ_link, |ω|) magnitude pairing).** Doc 81 captures post-closure research-tier work: coverage analysis (path α tested ~2 of ~7 predicted observable dimensions), (ε) PROVISIONAL synthesis (bound-state-vs-free-state interpretation candidate; same provisional class as §6.6 Pauli), Round 10+ Direction 3/3' concrete briefs (multi-operator signature observer + substrate-analog-of-(n,l,m_l) derivation). **No engine-state changes** — version unchanged at 4.0.4. Phase 5 pair-nucleation work remains structurally suspended; Round 10+ candidate directions queued as fresh-session work, NOT closure-blocking. **Auditor-lane post-closure work landed:** A43 v2 strengthening in COLLABORATION_NOTES (lane-symmetric "anyone-must-grep" generalization) with eight accumulated worked examples. **Auditor-lane queued work:** A60 / A61 / A62 / Rule 14 strengthening / §9 corpus revision package editorial pass — held for fresh session per Rule 12 cumulative-learning discipline (each rule benefits from settling time + corpus pressure-test before formalization). |

### 16.2 Engine version history (prior to manual creation)

| Version | Date | Commit | Changes |
|---|---|---|---|
| 1.0.0 | 2026-04-22 | afff853 | `feat(VacuumEngine): fundamental 3D vacuum engine (Stage 2)` — initial VacuumEngine3D delivery |
| 1.0.1 | 2026-04-22 | 87b502c | `fix(thermal): AVE Schwinger-vacuum T_V-rupt = 3.44 MK` — thermal stability bound |
| 1.1.0 | 2026-04-22 | be617f1 | `research(Phase-III-B): σ(ω) sweep v1 — doc 48_` — Phase III-B v1 results |
| 1.2.0 | 2026-04-22 | 0fa0d7c | `feat(Stage 4b): DarkWakeObserver + validation PASS` — dark-wake observer added |
| 1.3.0 | 2026-04-22 | aa6670b | `feat(Stage 4c): AutoresonantCWSource + K_drift tuning sweep` — autoresonant source added |
| 1.4.0 | 2026-04-22 | 4ea5c8a | `research(Stage 4d): Phase III-B v2 — doc 50_` — autoresonant σ(ω) results; A²_cos = 1.009 |
| 1.5.0 | 2026-04-22 | 471b5ea | TopologyObserver multi-threshold support (Stage 5 Phase A); [doc 52_](52_h1_threshold_sweep.md) |
| **2.0.0** | 2026-04-22 | — | Stage 6 Phase 0 doc ([54_](54_pair_production_axiom_derivation.md)) closes all free parameters, reopens S1 for Phase 4. Manual r0 written. No code change at this version bump. |
| 2.1.0 | 2026-04-22 | a0f50ed | Stage 6 Phase 1: predictions manifest + V_SNAP/V_yield test + Axiom-4 varactor test + predictions-matrix CI gate. Bumped minor because new validation infrastructure added (tests + manifest), not engine code. |
| 2.2.0 | 2026-04-22 | 719f3ec | Stage 6 Phase 2: `NodeResonanceObserver` + 13 smoke tests + driver script. Minor because new diagnostic observer; read-only (does not touch engine dynamics). |
| 3.0.0 | 2026-04-22 | 3a599ca | Stage 6 Phase 3: `Phi_link[nx, ny, nz, 4]` state array added to `K4Lattice3D`; `_connect_all` now accumulates per-bond flux. Major because new state variable + first modification to the K4 step. +`BondObserver` + 14 smoke tests. |
| 3.0.1 | 2026-04-23 | 6e355d1 | Stage 6 Phase 3.5.B: R4 normalization patch — removes `/α` from `NodeResonanceObserver._capture` and `BondObserver._compute_A2_yield` per Vol 4 Ch 1:711 subatomic override (§17.0). Adds new invariant test `test_normalization_subatomic_override.py`; updates poke formulas in `test_phase2_node_resonance.py` + `test_phase3_bond_state.py`; expands yield-terminology whitelist in `test_v_snap_v_yield_consistency.py`. Observer-output numeric change only; no engine-dynamics change. |
| 3.0.2 | 2026-04-23 | 224cad0 | Stage 6 Phase 3.5.A/B docs: commits doc 50_ r1→r2→r3 rewrite + doc 55_ with SUPERSEDED banner + doc 57_ v4 refactor plan + `v2_reproducibility_seed_sweep.py` bisection driver. Documentation-only; no engine change, so patch-level bump. |
| 3.1.0 | 2026-04-23 | a5bd1da | Stage 6 Phase 4: asymmetric μ/ε saturation. Replaces single-S kernel with `(S_μ, S_ε)` split; Beltrami helicity `h_local` (instantaneous, design 1A); asymmetric reflection form `Γ² = (1/16)·\|∇S_μ/S_μ − ∇S_ε/S_ε\|²` (design 2-II); S1 reopen resolved (design 3c). 965 → 983 pass. Minor because generalization of existing kernel (symmetric recovered at h_local = 0), no new state variable. |
| 3.2.0 | 2026-04-23 | aa7a337 | Stage 6 G-12: AutoresonantCWSource axiom-native varactor PLL — replaces linear-Taylor `(1 − K_drift·A²)` with Ax4-native `(1 − A²)^(1/4)` per Vol 4 Ch 1:127-142. Closes A7. K_drift deprecated. δ_lock = ω₀·α now reachable. Calibration re-pin → minor. |
| 3.3.0 | 2026-04-23 | e17b8cd, 5c3f2d1 | Stage 6 G-11c + G-11a: two new sources — `CosseratBeltramiSource` (direct ω chirality injection at source slab) + `SpatialDipoleCPSource` (CP V_inc via dipole modulation). Two new Source classes → minor. |
| 3.4.0 | 2026-04-23 | 9ecc2ca, 3f9569b | Stage 6 Phase 5 GATE LANDED: `PairNucleationGate` observer-with-side-effect on C1 ∧ C2 with point-rotation Beltrami pair injection + bond Φ_critical setting. Driver (`3f9569b`) at registered N=24, amp=0.5·V_SNAP shows max A²=0.75-0.91, 0 firings. New observer-with-side-effect class → minor (no new state variable, but new physical-axiom invocation; upgraded to 4.0.0 below alongside memristive Op14). |
| 3.5.0 | 2026-04-23 | 03cb9d5 | Stage 6 Phase 5.5: Cosserat-sector PML implements doc 58_ derivation. Quadratic-rolloff mask on (u̇, ω̇) post-velocity-Verlet. Same `pml_thickness` as K4 PML; Ax1+Ax3 boundary-treatment-symmetry forced. New boundary mechanism → minor. |
| **4.0.0** | 2026-04-23 | 49917ff | Stage 6 Phase 5.6: Memristive Op14 (K4 sector). Adds `S(t)` dynamical state variable per first-order relaxation ODE `dS/dt = (S_eq(r) − S)/τ_relax` with `τ_relax = ℓ_node/c`. Opt-in via `use_memristive_saturation: bool = False` flag preserves backward-compat. **Major because new state variable** — first dynamical S(t) in the K4 sector. Combined with Phase 5 PairNucleationGate's new physical-axiom invocation (nucleation rule), bumps to 4.0.0. |
| 4.0.1 | 2026-04-24 | 098d430 | Stage 6 Flag-5e-A fix: K4 saturation uses engine V_SNAP. Plumbs `V_SNAP` kwarg through `K4Lattice3D` and `CoupledK4Cosserat` so engine-natural-units context (V_SNAP=1) produces correct strain normalization. Pre-fix: K4 saturation path effectively dormant in any engine-context driver. Post-fix: first empirical cool-through-yield observable. Bug-fix → patch. |
| 4.0.2 | 2026-04-24 | 5f973b6 | Retroactive engine saturation invariants — pinning `S_min < 1.0` actually drops below 1 during the test window in engine integration tests. Closes test-coverage hole that allowed Flag-5e-A to live undetected. Test-only → patch. |
| 4.0.2 | 2026-04-24 | 815cd40 | F17-G coupled K4+Cosserat eigenmode finder (`coupled_engine_eigenmode.py`). New driver script; doc 66_ §17.2 three-storage-mode mapping. No engine change → no version bump. |
| 4.0.3 | 2026-04-24 | 3d7fae4 | Path-1 EMF: `use_lagrangian_emf_coupling` flag adds δL_c/δV-derived voltage source `(2V·W_refl)/(C·V_SNAP²)` to bond Φ_link integration. Default off preserves legacy. **Subsequently determined to be wrong-direction under A28 reframing — opt-in remains in HEAD pending cleanup.** Minor (new flag; no default behavior change). |
| 4.0.3 | 2026-04-24 | 05b130f | A28 fix: `disable_cosserat_lc_force` flag suppresses redundant `_compute_coupling_force_on_cosserat` channel that double-counted Op14 z_local modulation. Default off preserves legacy (which is now known-wrong-default). Six prior failure modes unified under this one bug. Bug-fix → patch (no version bump beyond 4.0.3 since flag is opt-in; legacy default unchanged). |
| **4.0.4 (current HEAD `ff15c4b`)** | 2026-04-25 | ff15c4b | `enable_cosserat_self_terms` flag re-enables Cosserat self-Lagrangian terms (`k_op10`, `k_refl`, `k_hopf`) disabled at init lines 231-233. Smart A28 interaction: when BOTH this flag AND `disable_cosserat_lc_force` are True, auto-suppresses redundant `k_refl=0` while keeping `k_op10=1` and `k_hopf=π/3`. **Path B at N=80 forms (2,3) bound state for the first time in Stage 6** under combined fix. Minor (new flag; no default behavior change). **Current HEAD.** |

**Round 6 outcome note (r8.3):** the planned 4.1.0 / 5.0.0 progression for strain-mask infrastructure / Phase 5 firing has been substantially restructured. Strain-mask infrastructure deferred — A28 was the actual gate. Phase 5 GATE code still in HEAD (commit `9ecc2ca`); firing adjudication still suspended pending single-electron validation Op6 outer-loop convergence (in progress).

**Upcoming anticipated versions:**
- 4.0.5 — Op6 self-consistency outer loop result on Path B (in working tree at `coupled_engine_eigenmode.py`). Driver script change → patch.
- 4.1.0 — Round 6 closure milestone if Op6 sustains bound state past 100 Compton periods. Major if defaults flip to A28-fixed behavior; minor if A28 stays opt-in.
- 4.2.0 — Cosserat-side memristive Op14 (doc 59_ §10.2 deferred). Minor — symmetric to K4 side.
- 5.0.0 — Phase 5 PairNucleationGate firing closure once single-electron validation passes. Major because first topology-change event would actually fire. Currently structurally suspended.
- 5.1.0 — Stage 6 Phase 6 (P_phase6_autoresonant headline validation). Minor.

### 16.3 Research-doc index

L3 electron-soliton thread, grouped by phase. Full list in [40_modeling_roadmap.md](40_modeling_roadmap.md).

**Foundation (Phase 0):**
- [00_scoping.md](00_scoping.md) — Cosserat canonization, scope
- [01_identity_adjudication.md](01_identity_adjudication.md) through [09_phase2_wrapup.md](09_phase2_wrapup.md) — Phase 1 theoretical spine

**Theoretical (Phase 1–2):**
- [20_chirality_projection_sub_theorem.md](20_chirality_projection_sub_theorem.md) — Sub-Theorem 3.1.1 `χ_(p,q) = α·pq/(p+q)`
- [22_–27_](22_step1_k4_rotation_action.md) — K4 rotation, spin-½, bond LC Compton, (2,3) selection, phase-space RR & Q
- [28_two_node_electron_synthesis.md](28_two_node_electron_synthesis.md) — 2-node bond electron
- [30_photon_identification.md](30_photon_identification.md) — T₂ photon mode
- [37_node_saturation_pauli_mechanism.md](37_node_saturation_pauli_mechanism.md) — node saturation / Pauli

**Engine design & validation (Phase I–III-B):**
- [40_modeling_roadmap.md](40_modeling_roadmap.md) — roadmap & phase log
- [41_cosserat_time_domain_validation.md](41_cosserat_time_domain_validation.md) — Phase I
- [42_coupled_simulator_validation.md](42_coupled_simulator_validation.md) — Phase II V1/V2/V3
- [44_pair_creation_from_photon_collision.md](44_pair_creation_from_photon_collision.md) — S1-D adjudication, Options A/B/C/D
- [45_lattice_impedance_first_principles.md](45_lattice_impedance_first_principles.md) — impedance decomposition; V_yield flag
- [46_vacuum_engine_scope.md](46_vacuum_engine_scope.md) — engine as-built
- [47_thermal_lattice_noise.md](47_thermal_lattice_noise.md) — thermal init recipe + AVE Schwinger T
- [48_pair_creation_frequency_sweep.md](48_pair_creation_frequency_sweep.md) — Phase III-B v1
- [49_dark_wake_bemf_foc_synthesis.md](49_dark_wake_bemf_foc_synthesis.md) — Stage 4 synthesis
- [50_autoresonant_pair_creation.md](50_autoresonant_pair_creation.md) — Phase III-B v2
- [51_handoff_followups.md](51_handoff_followups.md) — H1/H2/H3 hypotheses

**Stage 5 & 6:**
- [52_h1_threshold_sweep.md](52_h1_threshold_sweep.md) — H1 falsified
- [53_pair_production_flux_tube_synthesis.md](53_pair_production_flux_tube_synthesis.md) — structural limits named
- [54_pair_production_axiom_derivation.md](54_pair_production_axiom_derivation.md) — Stage 6 derivation chain
- [55_cosserat_normalization_derivation.md](55_cosserat_normalization_derivation.md) — Phase 3.5.A: A1/A14 manuscript-backed adjudication; **SUPERSEDED** by R4 banner (Vol 4 Ch 1:711 subatomic override)
- (56_ reserved — Phase 6 headline validation writeup, not yet drafted)
- [57_universal_lattice_units_v4_refactor.md](57_universal_lattice_units_v4_refactor.md) — v4 refactor plan (post-Stage-6; FUTURE_WORK G-10)

**Stage 6 Phase 5.5+ (Round 6 era):**
- [58_cosserat_pml_derivation.md](58_cosserat_pml_derivation.md) — Cosserat-sector PML axiomatic derivation (Ax1+Ax3 forced); landed `03cb9d5`
- [59_memristive_yield_crossing_derivation.md](59_memristive_yield_crossing_derivation.md) — memristive Op14 derivation; τ_relax = ℓ_node/c; BEMF-driven defect freezing; lattice-genesis cosmology framing; landed K4-side `49917ff`, Cosserat-side deferred
- [60_bh_interior_contradiction_audit.md](60_bh_interior_contradiction_audit.md) — corpus contradiction audit between info-loss stance (Vol 3 Ch 15/21/KB-ch04) and alternative interface-encoding framing (FLAGGED, corpus-contradicting)
- [61_cosmic_bipartite_k4_bh_interface_proposal.md](61_cosmic_bipartite_k4_bh_interface_proposal.md) — novel proposal: BH horizon as A-B rupture interface; surgically reframed for direction error (10⁴⁴ → 10⁻⁴⁴) and three-entropy distinction
- [62_ruptured_plasma_bh_entropy_derivation.md](62_ruptured_plasma_bh_entropy_derivation.md) — S_BH adjudication via Vol 3 Ch 11 Ŝ-on-horizon calculation; three-entropy distinction lands as canonical
- [63_info_loss_stance_reaudit.md](63_info_loss_stance_reaudit.md) — info-loss re-audit; Ŝ measures entropy GENERATION not capacity; AVE aligns with 1970s-Hawking; doc 61_ §3.5 unitarity-preserved retracted
- [64_first_law_derivation_attempt.md](64_first_law_derivation_attempt.md) — first-law derivation attempt; **area theorem `δA ≥ 0` derived from Ax1+Ax4** (r_sat = 7GM/c²); T·dS = dE fails to close axiom-first by factor 7ξ — Flag 62-A load-bearing
- [65_flag_62g_discrete_lattice_gamma.md](65_flag_62g_discrete_lattice_gamma.md) — Flag 62-G closure; discrete-lattice Γ at Ax4 boundary gives universal ~8.7·k_B (mass-independent)

**Stage 6 Round 6 (single-electron-first pivot):**
- [66_single_electron_first_pivot.md](66_single_electron_first_pivot.md) — Round 6 pivot canonical doc. §14 amplitude correction (peak |ω|=0.3π not √3/2·π); §17.2 three-storage-mode mapping (ε strain → C-state, κ curvature → L-state, V pressure → C-state); §18 F17-I three-mode coupled-seed test results.
- [67_lc_coupling_reciprocity_audit.md](67_lc_coupling_reciprocity_audit.md) — F17-H L_c reciprocity audit + F17-K methodology arc. §1-§14 derived path-1 EMF as ADD-channel fix; §15 Vol 4 Ch 1 cross-check inverted to A28 double-counting (REMOVE-redundancy); §16 empirical confirmation under `disable_cosserat_lc_force` flag (six prior failure modes unified). §18-§19 F17-I three-mode test under A28; §20 five-fallacy mid-interpretation audit + rebuilt diagnostic; §21-§22 Phase 5c v1 implementation + spurious convergence; §23 corpus search (doc 34 X4 algebraic pins); §24 Phase 5c v2 dual descent (PREMATURE Finding 3 retracted); §25 Phase 5c v2-v2 saturation-pin + empirical doc 03 §4.3 validation — F17-K Phase 5 closure; **§26 v3 (i) X4b linear-stability test — Golden Torus UNSTABLE under coupled S₁₁ (5.31×) and MARGINAL under Cosserat-energy (1.81×); confirms doc 03 §4.3 at linear-perturbation level alongside global-flow level; v3 (ii) Phase 6 sparse eigensolver methodology becomes load-bearing for Round 6 closure**.
- [68_phase_quadrature_methodology.md](68_phase_quadrature_methodology.md) — F17-K Phase 1 Ax-3 noncompliance audit. Identifies that all six prior Round 6 failure modes share root: methodology was Ax-3 noncompliant (used time-evolution dynamics + Cartesian shell extraction instead of |S₁₁|² minimization on phase-space (V_inc, V_ref) phasor coordinates). Same Rule 6 slip from session 2026-04-20 caught retroactively. Phase-coherence diagnostic + canonical phase-quadrature seeder (`initialize_quadrature_2_3_eigenmode`) introduced.
- [70_phase5_resume_methodology.md](70_phase5_resume_methodology.md) — Phase 5 PairNucleationGate resumption per Round 6 finding ("topology can be encoded via ansatz initialization"). Decouples three orthogonal questions: (α) gate mechanism works given C1∧C2 by construction; (β) seeded pair persists post-drive; (γ) C1/C2 reached under drive. Frames ansatz-seeded driver methodology that isolates (α)+(β) from (γ). §7.5 R5.10 Readings 1-4 two-level disambiguation (PRE-EMPTED at original Round 5 framing; MAY REOPEN at threshold-revision level after injection profile upgrade). Empirical case (b') finding documented in driver commit `ede4008`: point-rotation Beltrami injection profile fundamentally unstable in Cosserat self-dynamics; G-13 contingency activated.
- [71_multi_seed_eigenmode_sweep.md](71_multi_seed_eigenmode_sweep.md) — **r8.8: §13 retracted, §15 ACTIVE.** Originally landed `1bc1652` as `71_basin_audit_methodology.md` (Round 7 Stage 0 basin-audit-as-precondition framing); reframed in `c69e79c` to multi-seed R7.1 sparse eigensolver after within-session self-audit caught Rule 6/8/10 violation; further reframed in `675141e` to multi-seed block Helmholtz on (V, ω) joint after external audit caught operator-level Rule 6 violation. §1-§12 retained as Rule 12 audit trail (basin-audit framing, v1 fresh-session run halted by A26 guard); §13 RETRACTED (multi-seed Hessian-of-W body preserved per Rule 12); §14 superseded driver scope notes preserved; **§15 ACTIVE** — multi-seed block Helmholtz with quick-map vs §13 + read-order for fresh-session implementer.
- [72_vacuum_impedance_design_space.md](72_vacuum_impedance_design_space.md) — **NEW r8.8 (`675141e`).** Design-space articulation precursor to R7.1 pre-registration. §1 four AVE-native concepts (wave eigenmode via Helmholtz NOT Hessian; impedance match via S₁₁-min NOT energy-min; topological quantization as input ansatz NOT dynamical attractor; AVE basin = S₁₁-min NOT W-min). §2 3D Smith chart for the vacuum (Extension A `(Re(Γ), Im(Γ), ω)` recommended for R7.1; B and C supplementary; 4D chirality flagged for post-R7.1). §3.1 block Helmholtz formulation on joint (V, ω); §3.1.1 V=0 decoupling footnote (block decouples into V-block + ω-block simultaneously — strict superset of single-sector); §3.3 c_eigvec=3 binary + shape correlation > 0.60 informational two-tier; §3.4 sector-energy split diagnostic. §4 corpus tools to reuse (direct: extract_shell_radii / extract_crossing_count / universal_reflection / F17-K endpoint coordinates / AVE-HOPF Smith chart). §5 ~290 LOC fresh-session budget. §6.1 Rule-10 commitment language locks operator choice for fresh-session run. §7 connection to broader Stage 6 / Round 7 (mode I/II/III readings + R7.2 unaffected + 4D chirality post-R7.1). §8 sign-off questions (closed via audit Q1-Q5 acceptance).

**Stage 6 Round 7+8 (single-electron pivot empirical closure era):**
- [73_round_7_reframe_4_block_helmholtz.md](73_round_7_reframe_4_block_helmholtz.md) — **NEW r8.9.** Discrete K4-TLM scatter+connect + Cosserat (u, ω) LC-tank Hessian-of-W + Op14 cross-coupling reframe-4 (`ce5af9f`). §6.1 catastrophic-error carve-out invoked. §13 amendment per Grant's dimensional-analysis check (FFT-as-leakage misinterpretation corrected; attractor is STATIC fixed point not lattice-cutoff oscillator; Move 9 autoresonant drive at ω_C becomes load-bearing). §14 two-layer dimensional reconciliation: spin-½ half-cover (B canonical: m_Cosserat = 2·m_e per SU(2)→SO(3) double-cover) + Op14 saturation as gravitational redshift. §15 Move 10 result + framing supersession (sectors decoupled at static fixed point; §14.4 σ=4 prediction superseded).
- [74_round_7_followups.md](74_round_7_followups.md) — **NEW r8.9.** Round 7 follow-up tests + closure documentation. §1-§9 R7.1 reframe-4 + three follow-ups + Mode I N=64 candidate falsified by topology check + joint R7.1+R7.2 final closure both Mode III. §9 audit revisions (split A40 → A40 + A41 methodology-meta vs structural physics) + unified framework-level statement. §10 three audit-flagged follow-up tests close negative-result envelope: §10.2 Test A Mode III-both via corpus-canonical c=0; §10.3 Test B v2/v3 Mode III-spatial across linear+saturation regimes (8-port spatial sampling per doc 26 §3 corrects v1 single-port-temporal wrong-question per A44 spatial-multipoint correction). **§10.6 framework-level closure statement: "All seven tests Mode III. The bond-scale single-bond hypothesis per doc 28 §5.1 joins the framework-level §9.3 statement at bond-cluster scale."**
- [75_cosserat_energy_conservation_violation.md](75_cosserat_energy_conservation_violation.md) — **NEW r8.9.** Cosserat energy conservation violation finding from Move 11 + Diag A. §1-§5 Move 11 H_cos drift 5.5% + ρ(T_cos, V_cos)=+0.366 (positive Pearson trading, NOT LC reactance signature) traced via Diag A: V·S vs T·1 saturation asymmetry — Cosserat code saturates V_potential (G·S, K·S, G_c·S) but leaves T_kinetic unmodulated (ρ, I_ω constants); ½LI² and ½CV² don't co-saturate; total energy isn't conserved; ω drifts as a consequence. **§6 Engine bug, not missing axiom (A44 missing-axiom-vs-engine-bug diagnostic; one-sentence Grant collapse: "this is our conservation of energy axiom. rest mass saturates L, propagation saturates C").** §6.3 engine fix specified: T_kinetic gets the same Op14 S factor (ρ → ρ·S, I_ω → I_ω·S). §7 Diag A confirmed asymmetry empirically negligible at relevant amplitudes (Mode I per pre-reg). §8-§10 photon-tail dual-seed (path a) Mode III 0/4 + propagating-IC (path b) Mode III near-identical to (a). §11 Round 8 photon-tail branch closure + A57 (C4 informational vs C1/C2/C3 binary framing) + A58 (path-(a)/path-(b) empirical equivalence). Framing-error pass per `69fd974` corrected "Ax 3 = energy conservation" → "Ax 4 asymmetric L/C, Noether-broken energy conservation" per axiom homologation.
- [76_lattice_to_axiom3_bridge.md](76_lattice_to_axiom3_bridge.md) — **🔴 SUPERSEDED 2026-04-27** by doc 77_ per Rule 12. Original draft used Scheme B (Ax 3 = Gravity / Ax 4 = Saturation) inconsistent with corpus Scheme A (Ax 3 = Effective Action Principle / Ax 4 = Universal Saturation Kernel). Body preserved per Rule 12 audit-trail discipline.
- [77_lattice_to_axiom4_bridge.md](77_lattice_to_axiom4_bridge.md) — **NEW r8.9 (`b460071`).** Scheme-A canonical reframe of doc 76_. Lattice → Axiom 4 bridge (universal saturation kernel S(A) = √(1−A²) at every scale, derived from K4 substrate's intrinsic saturation onset). §6.4 closes doc 10_ §8(a) via dimensional cross-check on the axiom-4 quarter-circle form. Per axiom homologation arc (commits `75d1fde` → `6968398`).
- [78_canonical_phase_space_phasor.md](78_canonical_phase_space_phasor.md) — **NEW r8.9 (path α v1 result).** Pre-reg `P_phase8_canonical_phase_space_phasor` frozen at commit `a535090`; ran 2026-04-27 (commit `466d8c4`). Result: Mode III nominal — C1 R/r=3.84 vs target φ²=2.62 FAIL; C2 chirality 50% TIE FAIL. §7 A59 methodology gaps: persistence guard violated (recording window captured attractor decay); chirality cross-product noise-dominated (std/|mean| 600-1200×); bipolar +x/−x R/r distribution (5.5 vs 2.2); top-K single-cell sampling missed bond-pair structure. Path α v2 design follows from these gaps + the regime analysis from doc 79 v4.x.
- [79_l3_branch_closure_synthesis.md](79_l3_branch_closure_synthesis.md) — **NEW r8.9 (closure synthesis, PENDING path α v2).** Lemniscate-with-q-half-twists as primary AVE-native plumber framing for the (2, q) particle family in K4-TLM + Cosserat substrate. §1-§5 framework structure (universal "2" = bipartite K4 / lobe count; "q" = half-twist count; chirality 3-layer structure; Meissner-asymmetric magnetic-moment generator). §6 empirical state at closure (R6 closed; R7+R8 seven Mode III tests reinterpreted under reframe; Move 5 attractor as positive empirical signal; r9/path α v1 Mode III with caveats). §7 path α v2 requirements (bond-pair sampler + dual criterion). §8 conditional closure on path α v2. §9 corpus revision package (a)-(e). §10 methodology rules (A59 + A60 candidate). §11 Kelvin/Helmholtz/Faddeev-Niemi historical precedent (doc 80_ companion). v3 → v4.1 added Virial; v4.2 added Meissner = magnetic-moment generator + path α reframe; v4.3 V_yield ↔ V_SNAP distinction (likely subject to v4.4 sign-correction per Rule 14 substrate-derives + empirical Γ verification on path α v1's saved data). Commits `f3886d1` → `9f565d6` → `95a017c`.
- [80_kelvin_helmholtz_ave_precedent.md](80_kelvin_helmholtz_ave_precedent.md) — **NEW r8.9 (commit `f3886d1`).** Companion to doc 79 §11. Historical-precedent research note tracing Helmholtz 1858 vortex theorems → Kelvin 1867 vortex atoms → Tait knot tabulation → (Michelson-Morley gap) → Faddeev-Niemi 1997 knotted solitons → AVE-Core 2026 (2, q odd) ladder. §2 specific Kelvin/Helmholtz intuitions worth deepening for AVE-specific work (topological stability, helicity ∝ Hopf invariant, why Kelvin's element-matching failed but AVE's (2, q odd) ladder works, medium difference, chirality from helicity sign). §3 structural takeaways (159-year intellectual lineage; Faddeev-Niemi 1997 connection load-bearing; Kelvin-style stability proof needs adaptation for discrete substrate). §5 post-closure manuscript revision recommendations. Background context, NOT closure-blocking.
- [81_l3_followup_questions.md](81_l3_followup_questions.md) — **NEW r8.10 (commit `cfb203a`).** Research-tier post-closure follow-up to doc 79 v5.1 closure. NOT a v5.2 amendment (closure-revision discipline holds; v5.1 stands as canonical empirical record). §2 coverage analysis: cross-repo Explore surfaced 22-operator universal catalog (Op1-Op22) + two distinct R/r=φ² definitions in corpus (doc 26 §4 spatial-moment vs doc 28 §5.1 phasor-PCA); path α tested ~2 of ~7 predicted observable dimensions. §3 (ε) bound-state-vs-free-state structural-reason interpretation candidate (PROVISIONAL pending Direction 3' substrate-analog-of-(n,l,m_l) derivation; same provisional class as doc 79 §6.6 Pauli framing). §4 Round 10+ Direction 3 multi-operator signature observer concrete brief (tests (γ) signature revision via Op14 Z_eff / Op16 c_shear / Op20 ω_regime / Op22 M cascade observers + doc 26 §4 spatial-moment R/r). §5 Round 10+ Direction 3' substrate-analog-of-(n,l,m_l) derivation brief (~3-5 fresh sessions; tests (ε)). §6 A43 v7/v8 implementer-side worked examples (lane-symmetric pattern empirically supported across 8 instances total this session arc).

**Round 9 + Round 10+ + Round 11 (vi) era (single-electron empirical closure extension; r8.10):**
- [83_phase1_bond_pair_vs_bond_cluster_scale.md](83_phase1_bond_pair_vs_bond_cluster_scale.md) — **NEW r8.10 (commit `9e8b1e2`).** Round 10+ Phase 1 Direction 3'.1 reframe — bond-pair vs bond-cluster scale; path α v1-v4(b) tested wrong object class for corpus electron comparison
- [84_path_alpha_v6_first_run_results.md](84_path_alpha_v6_first_run_results.md) — **NEW r8.10 (commit `881c3d1`).** Path α v6 trapped-photon unknot chair-ring IC at bond-pair scale — Mode III by 4/4 strict criteria (1/4 PASS) but ring localization 96% over 200P empirically supports trapped-state forming + 6-node chair-ring real-space embedding. Beltrami / centroid-flux failures point to IC mode-structure mismatch (no helical Beltrami pitch, no FOC d-q orthogonality) per Kelvin + FOC reframing — informative falsification of specific IC structure, NOT framing rejection
- [85_kelvin_beltrami_foc_axiom_grounded_derivation.md](85_kelvin_beltrami_foc_axiom_grounded_derivation.md) — **NEW r8.10 (commit `3cb31c9`).** Kelvin Beltrami + FOC d-q axiom-grounded derivation for v7 IC restructure. Maps trapped-photon unknot from AVE Ax 1-4 first principles per Grant directive 2026-04-28; addresses v6 Mode III IC mode-structure failures (helical pitch, d-q time-vs-space phasing, A-vec proxy correction, substrate-native topology measure)
- [86_path_alpha_v7_helical_beltrami_thermal_sweep.md](86_path_alpha_v7_helical_beltrami_thermal_sweep.md) — **NEW r8.10 (commit `617e352` + §7 addendum `55050aa`).** Path α v7 helical Beltrami chair-ring IC + thermal robustness sweep — Mode II at every T value (0 → 0.1·T_V-rupt) with persistence + ring-localization PASS thermally robust across 5 orders of magnitude in T; Beltrami / loop-flux FAIL with identified mechanical measurement-method causes (Phi_link-as-A roundtrip + accumulator-not-instantaneous-A); v8 scope LOCKED to ONE-cycle measurement-method redesign; Round 11 framework reframe AUTO-TRIGGERS if v8 doesn't land Mode I. §7 addendum: lock v8 pre-flight + Round 11 enumeration per auditor 2026-04-28
- [87_path_alpha_v8_round_11_ignition.md](87_path_alpha_v8_round_11_ignition.md) — **NEW r8.10 (commit `2dd4ab8`).** Path α v8 corrected measurements (Phi_link detrend) Mode II at every T → Round 11 trigger AUTO-FIRES per doc 86 §7.6 gate; dimensional audit reveals IC was traveling-wave NOT Beltrami standing-wave (LOAD-BEARING reframe); v7 closure-narrative walkback ("trapped configuration of some kind, NOT confirmed Beltrami") on-record per Rule 12 retraction-preserves-body; Round 11 candidate (vi) discrete chair-ring eigenmode rederivation elevated to load-bearing primary
- [88_round_11_vi_stride_1_a43_v14.md](88_round_11_vi_stride_1_a43_v14.md) — **NEW r8.10 (commit `fbd0c26` + integration addendum `8b5a2c7`).** Round 11 (vi) Stride 1 — A43 v14 corpus-grep on R/r reveals THREE different framings + substrate-native eigenvalue analysis surfaces dimensional inconsistency in (1,1) Beltrami at Compton frequency claim. Stride 2 (proper discrete eigenmode derivation) must resolve before v9 IC can be constructed. §audit-integration addendum: three sharpenings post-auditor 2026-04-29 — k=6.36 ↔ 3.21 MeV non-particle-frequency physics insight; dispersion-vs-curl-eigenvalue resolution candidate (3) sharpened; A43 v15 candidate added (tube-radius corpus-inconsistency)
- [89_round_11_vi_stride_2_topological_mismatch.md](89_round_11_vi_stride_2_topological_mismatch.md) — **NEW r8.10 (commits `4925df5` + §7 correction `3c267e4`).** Round 11 (vi) Stride 2 — topological mismatch identified — chair-ring is 1-graph (closed cycle), NOT 2-torus surface; (p,q) torus Beltrami eigenmode framework requires INDEPENDENT poloidal+toroidal directions but 1-graph has only toroidal. §7 correction: chair-ring overstated as 1-graph; K4 lattice IS 3D-connected (each node has 4 ports in 4 tetrahedral directions); chair-ring nodes have 2 in-ring + 2 out-of-ring ports providing poloidal direction; v6/v7/v8 IC zeroed out-of-ring ports, NOT topological-impossibility issue
- [90_round_11_vi_stride_3_discrete_eigenmode.md](90_round_11_vi_stride_3_discrete_eigenmode.md) — **NEW r8.10 (commit `0174eaa`).** Round 11 (vi) Stride 3 — discrete Beltrami eigenmode SOLVED on chair-ring + 1-step K4 (18 nodes, 54 DOF); top ring-localized mode at k≈1.56 in 1/ℓ_node units (84% ring localization); continuum (1,1) prediction k=6.36 NOT in discrete spectrum (4× gap); no eigenmode exactly at Compton frequency k=1; 4 open Q for Grant on which discrete k = corpus electron
- [91_round_11_vi_stride_4_v9_mode_iii.md](91_round_11_vi_stride_4_v9_mode_iii.md) — **NEW r8.10 (commit `66de104`).** Round 11 (vi) Stride 4 — v9 with discrete eigenmode IC at chair-ring + 1-step K4 lands Mode III 1/4 PASS — Round 11 (vi) does NOT close to Mode I; secondary candidates (i)/(iii) trigger per locked gate; honest closure narrative for v6/v7/v8/v9 arc: framework's "(1,1) Beltrami at corpus geometry on chair-ring" claim NOT empirically supported at K4 sampling density
- [92_round_11_vi_v10_finer_sampling_structural.md](92_round_11_vi_v10_finer_sampling_structural.md) — **NEW r8.10 (commit `0f7180f`).** Round 11 (vi) v10 (i-a) — finer K4 sampling EMPIRICALLY ELIMINATES (i-a) refinement path — discrete K4 spectrum at chair-ring + N-step asymptotes at Nyquist limit (1/bond_length ≈ 0.577 in 1/ℓ_node), 11× below continuum (1,1) prediction k=6.36; framework's "(1,1) Beltrami at Compton frequency at corpus geometry on K4 substrate" CANNOT be realized at K4 at ℓ_node sampling; **STRUCTURAL not refinable**. **This is Layer 1 of three-layer convergent refutation per A37**
- [93_ee_to_ave_mapping.md](93_ee_to_ave_mapping.md) — **NEW r8.10 (UNCOMMITTED at this manual edit).** EE-to-AVE mapping for (i-b) FDTD substrate test path α reframing. Phase A toolkit (FFT + Faraday + impedance landscape + power split + Q-factor + B-H + multipole + far-field) as substrate-baseline test catalog
- [94_ee_phase_a_universal_solver_match.md](94_ee_phase_a_universal_solver_match.md) — **NEW r8.10 (UNCOMMITTED at this manual edit).** Phase A B1-B4 results — chair-ring trapped state characterized as ℓ=2 cavity mode (~1.48·ω_C, 4-axis confirmation: 99.99% Fourier ℓ=2-pure on cos(2θ) saturation profile + 96% spatial saturation Fourier ℓ=2-pure + spatial chair-ring localization + temporal persistence). ℓ=5 ω-sector eigenvalue match at 2.8% (single-axis FFT only). Beltrami |cos_sim| caps at 0.515 at AC level. B4 ω-runaway diagnosed as config error per Q1 resolution, NOT engine bug; A28 architectural decision validated. §13 "asymmetric saturation gap" RETRACTED per Rule 12 (was config error not engine bug)
- [95_b5_far_field_three_layer_closure.md](95_b5_far_field_three_layer_closure.md) — **NEW r8.10 (UNCOMMITTED at this manual edit).** Round 11 (vi) closure with **three-layer convergent refutation** (Layer 1 substrate-geometric per doc 92; Layer 2 engine-architectural per A28+B6; Layer 3 standard-physics-external per B5). B5 + B5b SNR>10²² confirmation. B6 700P stability anchor. Auditor's precision fixes incorporated (eigenmode-vs-classification per A43 v27, "A28 by construction" framing replaces "Faraday violated", four-positive-findings preservation alongside negative electron-test result). Universal-solver-promotion mediated-through-substrate framing per A40
- [96_foundation_audit_t1_substrate_resonance.md](96_foundation_audit_t1_substrate_resonance.md) — **NEW r8.10 (UNCOMMITTED at this manual edit).** Foundation audit Test 1 + Test 1 extensions + Test 3 CW-drive impedance spectroscopy + drive-amplitude scaling. Substrate has two genuinely independent reactive modes at 1.5·ω_C and 2.96·ω_C, phase ≈ -90°, Q ≈ 3.75 (per A38). Three-iteration overclaim cycle preserved per Rule 12: §1-§5 single-frequency overclaim → §6-§10 multi-mode walkback → §11 two-independent-modes via drive-amplitude scaling. Cosserat ON ≡ OFF at bit precision. T-ST v1 + v2 driver + result writeup pending

**Doc 79 (modified, uncommitted at this manual edit):**
- [79_l3_branch_closure_synthesis.md](79_l3_branch_closure_synthesis.md) v5.2 second addendum — incorporates three-layer convergent refutation per Round 11 (vi) closure + four positive substrate-canonical findings preservation. Per Rule 12, original v5.1 framing preserved (Mode III canonical + Meissner partial positive); v5.2 addendum extends to "three-layer convergent refutation + four positive substrate findings + Op14-feedback-empirically-effective"

**Housekeeping:**
- [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md)
- [S_GATES_OPEN.md](S_GATES_OPEN.md) — S-gate register
- [DOCUMENTATION_UPDATES_QUEUE.md](DOCUMENTATION_UPDATES_QUEUE.md) — queued manuscript/doc updates
- `VACUUM_ENGINE_MANUAL.md` — this document

### 16.4 Engine code index

| File | Purpose | Classes / functions |
|---|---|---|
| [src/ave/topological/vacuum_engine.py](../../src/ave/topological/vacuum_engine.py) | Engine facade, sources, observers, gates | VacuumEngine3D, EngineConfig; Sources: PulsedSource, CWSource, AutoresonantCWSource, CosseratBeltramiSource, SpatialDipoleCPSource; Observers: ScalarObserver, RegimeClassifierObserver, NodeResonanceObserver, BondObserver, TopologyObserver, EnergyBudgetObserver, DarkWakeObserver; Gates: PairNucleationGate (observer-with-side-effect) |
| [src/ave/topological/k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) | S5-B unified integrator; coupling dispatch (asymmetric vs legacy); V_SNAP plumbing (Flag-5e-A fix) | CoupledK4Cosserat |
| [src/ave/topological/cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) | Cosserat sector (JAX autodiff); Phase 4 asymmetric (S_μ, S_ε) helpers; Cosserat PML; (2,3) hedgehog seeders | CosseratField3D; helpers `_beltrami_helicity`, `_tetrahedral_curl`, `_reflection_density_asymmetric`, `_update_saturation_kernels`; seeders `initialize_electron_2_3_sector` (ω), `initialize_u_displacement_2_3_sector` (u) |
| [src/ave/core/k4_tlm.py](../../src/ave/core/k4_tlm.py) | K4 TLM substrate; K4 PML; opt-in memristive Op14 dynamical S(t); engine-V_SNAP plumbing | K4Lattice3D, K4Lattice2D |
| [src/ave/core/constants.py](../../src/ave/core/constants.py) | Physical constants; KAPPA_CHIRAL_ELECTRON = 1.2α; TAU_RELAX = ℓ_node/c | — |
| [src/ave/topological/faddeev_skyrme.py](../../src/ave/topological/faddeev_skyrme.py) | (2,q) torus-knot ansatz | TopologicalHamiltonian1D |
| [src/ave/core/universal_operators.py](../../src/ave/core/universal_operators.py) | Universal operator catalog (Op1–Op14) | — |

### 16.5 Canonical driver scripts

| Script | Purpose |
|---|---|
| [src/scripts/vol_1_foundations/vacuum_engine_pair_creation.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation.py) | Phase III-B v1 driver |
| [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v2.py) | Phase III-B v2 driver (autoresonant) |
| [src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation_v3.py) | Stage 5 Phase A H1 sweep |
| [src/scripts/vol_1_foundations/dark_wake_validation.py](../../src/scripts/vol_1_foundations/dark_wake_validation.py) | Stage 4b validation |
| [src/scripts/vol_1_foundations/autoresonant_tuning.py](../../src/scripts/vol_1_foundations/autoresonant_tuning.py) | Stage 4c K_drift sweep |
| [src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py](../../src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py) | A17 bisection driver (Phase 3.5.A/B) |
| [src/scripts/vol_1_foundations/flux_tube_persistence.py](../../src/scripts/vol_1_foundations/flux_tube_persistence.py) | Φ_link persistence driver for saturated-endpoint bonds (A15 retest) |
| [src/scripts/vol_1_foundations/node_resonance_validation.py](../../src/scripts/vol_1_foundations/node_resonance_validation.py) | Phase 2 NodeResonanceObserver smoke driver |
| [src/scripts/vol_1_foundations/phase5_pair_nucleation.py](../../src/scripts/vol_1_foundations/phase5_pair_nucleation.py) | Phase 5 PairNucleationGate driver (registered N=24 spec; ⏸ Round 6 suspended) |
| [src/scripts/vol_1_foundations/phase5e_cool_from_above.py](../../src/scripts/vol_1_foundations/phase5e_cool_from_above.py) | Phase 5e cool-from-above driver (Flag-5e-A discovery; first empirical cool-through-yield) |
| [src/scripts/vol_1_foundations/phase5e_cool_from_above_v2.py](../../src/scripts/vol_1_foundations/phase5e_cool_from_above_v2.py) | Phase 5e v2 with CosseratBeltramiSource (C1-C2 gate window discovery) |
| [src/scripts/vol_1_foundations/coupled_engine_eigenmode.py](../../src/scripts/vol_1_foundations/coupled_engine_eigenmode.py) | F17-G/F17-I coupled K4+Cosserat eigenmode finder; `seed_mode` parameter for mixed/all_c/all_l three-mode test |
| [src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py) | Path A K4-only TLM eigenmode driver (4-of-4 falsification, commit `fbbc950`); `initialize_phi_link_2_3_ansatz` Φ_link seeder |

### 16.6 KB invariants

| Invariant | Claim | Source |
|---|---|---|
| INVARIANT-C1 (V_yield) | V_yield = √α · V_SNAP ≈ 43.65 kV | [manuscript/ave-kb/CLAUDE.md](../../manuscript/ave-kb/CLAUDE.md) |
| INVARIANT-S2 (axiom numbering) — Scheme A canonical (r8.9) | 4 axioms: Ax 1 LC Network Substrate (impedance/[Q]) / Ax 2 Topo-Kinematic Isomorphism ([Q]≡[L]/fine structure) / Ax 3 Effective Action Principle (Lagrangian) / Ax 4 Universal Saturation Kernel S(A) = √(1−(A/A_yield)²) (quarter-circle, NOT SiLU) | [manuscript/ave-kb/CLAUDE.md](../../manuscript/ave-kb/CLAUDE.md) (SiLU/ABCD misnomers fixed in `75d1fde`); canonical form at [`eq_axiom_4.tex:25`](../../manuscript/common_equations/eq_axiom_4.tex); cross-cutting reference [`manuscript/ave-kb/common/axiom-homologation.md`](../../manuscript/ave-kb/common/axiom-homologation.md) (`6968398`) |
| INVARIANT-Phy1 (Pythagorean vac. strain) | Queued — `V_total² = Σ V_channel²` | Currently [AVE-APU/vol_1_axiomatic_components/ch05:26–37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex); [FW G-7](../../.agents/handoffs/FUTURE_WORK.md) tracks promotion |
| INVARIANT-S3 (NEW r8.9) — Symmetric Gravity from Ax 1 + Ax 4 | n(r) = 1 + 2GM/(rc²) is a derived consequence of Ax 1 LC Network Substrate + Ax 4 Universal Saturation Kernel; μ_eff/ε_eff scale together; NOT an additional axiom | [`eq_gravity_derived.tex`](../../manuscript/common_equations/eq_gravity_derived.tex) (NEW per `05f8ac3`); axiom-homologation cross-cut |

### 16.7 Cross-repo references

| Repo | Relevant artifact | Used for |
|---|---|---|
| AVE-Propulsion | [vol_propulsion/ch05_autoresonant_dielectric_rupture.tex](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex) | Source of autoresonant PLL mechanism |
| AVE-Propulsion | [simulate_warp_metric_tensors.py:75–95](../../../AVE-Propulsion/src/scripts/simulate_warp_metric_tensors.py) | τ_zx formula ported to DarkWakeObserver |
| AVE-PONDER | generate_ponder_01_spice_netlist.py:90 | K_0 = 0.207973 (η_vac proxy) |
| AVE-Fusion | .agents/handoffs/02_antimatter_annihilation.tex (§Pair Production) | Pair-nucleation conversion mechanism |
| AVE-HOPF | [03_hopf_01_chiral_verification.tex:72–82](../../../AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex) | κ_chiral = α·pq/(p+q) empirical benchmark |
| AVE-APU | [vol_1_axiomatic_components/ch05_geometric_triodes.tex:26–37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex) | Pythagorean vacuum-strain theorem |

---

---

## 17. Audit findings (open)

Flag-don't-fix discipline. Findings from the 2026-04-22 critical review of manual r0 against the committed engine state (post-Phase 2). Each finding is a flag for Grant's adjudication, not a silently-applied correction. Severity legend: **S1** = correctness issue in engine code / potential bug; **S2** = test-coverage gap with a concrete scenario that could fail undetected; **S3** = manual / documentation inconsistency; **S4** = cosmetic / formatting.

Closure protocol: when a finding is resolved (fixed, or adjudicated "won't fix" with rationale), move it from §17.1 open list to §17.2 closed list with a date + resolution summary. Do not silently edit away open findings.

### 17.0 R4 adjudication summary (2026-04-23, supersedes r2/r3/r4/r5 normalization framings)

**One-paragraph TL;DR.** Working-tree [doc 55_](55_cosserat_normalization_derivation.md) now carries a top-of-file SUPERSEDED banner explicitly retracting its R3 "dual accessors / K4 is outlier" direction. The authoritative direction, **R4**, is grounded in [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711):

> *"Subatomic-scale simulations (e.g., bond energy solvers, Yang-Mills confinement) should override with `v_yield=V_SNAP` (≈ 511 kV)."*

At VacuumEngine3D's operating scale (K4 lattice at `ℓ_node = ℏ/(m_e c)` — Compton wavelength; pair-production use case), the subatomic override applies and `V_yield ≡ V_SNAP`. Therefore the engine's `A² = V²/V_SNAP²` IS canonical `r² = V²/V_yield²` per Vol 1 Ch 7:12's universal form `r = A / A_c`.

**Authority chain reconciliation.** Doc 55_'s R3 direction cited Vol 1 Ch 7:104 as universal authority for `r = V/V_yield` with V_yield ≈ 43.65 kV. Independent r6 audit confirms [Vol 1 Ch 7:104](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) is the "Electromagnetic (Voltage)" subsection; its regime locations are **explicitly macroscopic** (Lab capacitor at 1 kV, HV Capacitor at 30 kV, HV Capacitor at 43 kV). Vol 4 Ch 1:711 and Vol 1 Ch 7:104 are not in conflict — they describe the same regime-map framework at *different operating scales*, and V_yield is an A_c that changes numerical value with the scale. The R4 reading is dimensionally sound and manuscript-grounded.

**TKI corroboration.** Under the subatomic override, the TKI derivation `σ_yield = V_yield · e / ℓ_node³` reduces to `σ_yield = V_SNAP · e / ℓ_node³ = m_e c² / ℓ_node³ = 1` in natural units. With G = 1 placeholder, the Cosserat `ε_yield = σ_yield / G = 1` exactly — matching the engine's current value. The earlier "ε_yield = 1 is empirical placeholder" framing (A20) is retracted: ε_yield = 1 is TKI-derived under R4.

**Schwinger/rupture reconciliation.** The previously-flagged Vol 1 Ch 7:115 vs :130 "manuscript inconsistency" (A19) is actually **scale-dependence of V_yield**:
- Line 115 — subatomic convention: AVE's pair-production onset collapses with Schwinger at `r = 1` (V = V_SNAP = V_yield_subatomic).
- Line 130 — macro convention: Schwinger sits at `r = V_SNAP / V_yield_macro = 1/√α ≈ 11.7` (deep Regime IV).

Both readings are correct under their own V_yield; no manuscript defect.

**Findings retracted under R4** (preserved with full text in §17.2):
- **A14** (3-observer normalization discrepancy) — `RegimeClassifierObserver`'s direct `A²_K4_SNAP + A²_cos` sum is valid canonical `r²_total` at subatomic scale, *not* a mixed-convention bug. The `/α` divisions in `NodeResonanceObserver` and `BondObserver` were the actual defect; R4 patches removing them committed as `6e355d1`.
- **A19** (Vol 1 Ch 7:115 vs :130) — scale-dependence, not inconsistency.
- **A20** (ε_yield = 1 calibration question) — TKI-derived exactly under R4, not a placeholder.
- **A23** (doc 55_ / doc 57_ framing tension) — closed by doc 55_'s own R4 banner.

**Findings unaffected by R4** (remain in §17.1):
- **A15** (identical Φ_link half-lives) — stays open; retest once R4 observer patches commit and Phase 4 asymmetric μ/ε lands.
- **A17** was also in this bucket at r5 but has since closed → §17.2 (bisection complete; bit-identical distributions; tail outcome not regression).
- **A22** (inline operators duplicating canonical universals) — Rule-6-adjacent drift risk; doc 57_'s v4 refactor is the resolution path, post-Stage-6.

**Engine code status (r8 — R4 long-since committed; Round 6 pivot active).** HEAD is `815cd40` on branch `research/l3-electron-soliton`; Phase 3 + R4 patches + R4 docs + Phase 4 asymmetric saturation + 23 subsequent commits (Phase 5 GATE landed-then-suspended, Phase 5.5 Cosserat PML, Phase 5.6 memristive Op14, Phase 5.7 BH-entropy thread, Phase 5e cool-from-above + Flag-5e-A fix, Round 6 pivot, Path A falsification, F17-G eigenmode finder) all landed. See §1 front matter, §1.5 Round 6 pivot summary, and §16 change log for the full arc. R4 observer patches:
- `NodeResonanceObserver._capture` [vacuum_engine.py:~531](../../src/ave/topological/vacuum_engine.py#L531): `/α` removed; returns direct `A²_K4 + A²_Cos`. ✅ Committed.
- `BondObserver._compute_A2_yield` [vacuum_engine.py:~428](../../src/ave/topological/vacuum_engine.py#L428): `/α` removed. ✅ Committed.
- [test_normalization_subatomic_override.py](../../src/tests/test_normalization_subatomic_override.py): R4 engine invariant test. ✅ Committed.
- Poke formulas updated in `test_phase2_node_resonance.py`, `test_phase3_bond_state.py`; yield-terminology whitelist expanded in `test_v_snap_v_yield_consistency.py`. ✅ Committed.

Phase 4 landing reuses this R4-corrected observer machinery for the `(S_μ, S_ε)` split. R4 + Phase 4 combined suite is 983 pass.

---

### 17.0.1 r2–r5 audit-history deltas (retained for audit trail)

Re-audit on 2026-04-22 post-Phase-3 commit `3a599ca` (r4): Phase 3 commit introduced a third observer (`BondObserver`) using the V_yield convention, which made finding A1 *more* systemic (new **A14**). Driver-measured identical-half-life result became **A15**. Seed-sweep script became **A16**.

Re-audit r5 (2026-04-23): doc 55_ R3 landed as resolution direction for A14; r5 recorded tension with doc 57_ as **A23**. Doc 55_ and doc 57_ were both untracked.

**r6 (this revision, 2026-04-23)**: R4 adjudication retracts A14/A19/A20/A23 per §17.0. Engine has regressed from Phase 3 → Phase 2 (`3a599ca` → `719f3ec` via stash). A17 remains open as the only pre-R4 finding with clear continued status as S1.

### 17.1 Open findings

#### A1. `RegimeClassifierObserver` mixes V_SNAP and yield normalizations in `max_A2_total` (S1 — load-bearing)

**Where:** [vacuum_engine.py:376](../../src/ave/topological/vacuum_engine.py#L376)
```
A2_k4 = V_sq / (engine.V_SNAP ** 2)     # SNAP-normalized: A²=1 at 511 kV
A2_cos = _cosserat_A_squared(...)       # yield-normalized per NodeResonance cmt
A2 = A2_k4 + A2_cos                     # summing mixed normalizations
```
The regime boundaries `_REGIME_I_BOUND_A2 = 2α`, `_REGIME_II_BOUND_A2 = 0.75`, `_RUPTURE_BOUND_A2 = 1.0` at [vacuum_engine.py:151](../../src/ave/topological/vacuum_engine.py#L151) are SNAP-normalized (rupture at V_SNAP = 511 kV). But `NodeResonanceObserver` at [vacuum_engine.py:428](../../src/ave/topological/vacuum_engine.py#L428) explicitly comments "Cosserat sector is already yield-normalized" and only divides the K4 piece by α.

Implication: if the Cosserat sector is indeed yield-normalized (NodeResonanceObserver's assumption), then `max_A2_total` reported by `RegimeClassifierObserver` is nonsensical — it mixes two scales that differ by a factor of α ≈ 137. Specifically, `A²_cos = 0.5` (half-cosserat-yield) gets added to `A²_K4 = 0.5` (half-Schwinger) and compared against `_REGIME_II_BOUND_A2 = 0.75`.

Secondary implication: the v2 headline claim "**A²_cos = 1.009** — first numerical crossing of Axiom-4 rupture boundary" ([doc 50_ §2.3](50_autoresonant_pair_creation.md)) is ambiguous. If Cosserat yields are at A²_cos=1, then 1.009 is just-past-yield, not rupture. If they're Schwinger-equivalent, then 1.009 IS rupture. No authoritative mapping exists in the engine.

**Root cause hypothesis:** the Cosserat yield placeholders `ε_yield = 1`, `ω_yield = π` in [cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) have never been physically mapped to V_yield or V_SNAP via the S-gate S4=A decision to keep natural units ([S_GATES_OPEN.md](S_GATES_OPEN.md)).

**Proposed resolution options** (needs Grant adjudication):
- (a) Declare Cosserat yields are Schwinger-equivalent (A²_cos = 1 at Cosserat rupture), and update `NodeResonanceObserver._capture` to divide `A2_cos_yield` by α also.
- (b) Declare Cosserat yields are yield-equivalent, and update `RegimeClassifierObserver._capture` to divide `A²_K4` by α before summing. This reinterprets every historical `max_A2_total` number by a factor of α — large reframe.
- (c) Add a normalization-explicit accessor `engine.A2_total_SNAP_normalized()` and `engine.A2_total_yield_normalized()` and force callers to pick. No silent mixing.

**r2 update (2026-04-22):** Phase 3 committed a third observer (`BondObserver`) that followed NodeResonanceObserver's yield-normalized convention. Discrepancy now spans three observers. See **A14** below.

**r3 update (2026-04-23):** R4 change plan (incoming) proposes to resolve this by **removing `/α` from `NodeResonanceObserver` and `BondObserver`** — reverting them to match `RegimeClassifierObserver`'s SNAP convention. Rationale per research-agent handoff: *"the /α conversion was always wrong."* Resolution direction for A14 is option (e) (flip Phase 2/3 convention back to SNAP); option (d) (retrofit historical reports to yield-units) is rejected. **Review flag:** this silently changes the physical meaning of `BondObserver`'s `saturation_frac = 0.5` default — under SNAP that's "halfway to Schwinger" instead of "halfway to yield" (≈137× different physical threshold). R4 must either rename the default or explicitly re-calibrate, or the saturation-partition physics in §10.11 BO-4 is silently reinterpreted.

**r4 correction (2026-04-23) — supersedes the r3 note above:** [doc 55_](55_cosserat_normalization_derivation.md) re-derived the adjudication directly from [Vol 1 Ch 7:12, :104](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex) and reached the **opposite conclusion**: the *Cosserat sector's yield-normalization is the canonical AVE convention*; the *K4 sector's SNAP-normalization is the historical outlier*. Per Vol 1 Ch 7:104 the canonical EM control parameter is `r = V / V_yield` (not `V / V_SNAP`); Vol 1 Ch 7:130 explicitly places Schwinger "deep in Regime IV" at `r = 1/√α ≈ 11.7`, NOT at r = 1. Doc 55_ rejects the r3-note's R4 direction (would break Vol 1 Ch 7 canonical alignment) and rejects full migration to yield-units (too invasive mid-Stage-6), selecting instead **R3 (dual accessors)**:

- Add `VacuumEngine3D.A2_total_SNAP()` and `.A2_total_yield()` with explicit documented conventions.
- Emit `DeprecationWarning` on `RegimeClassifierObserver.max_A2_total` access (inherently mixed-normalization scalar).
- `NodeResonanceObserver` and `BondObserver` docstrings clarified; no engine-behavior change.
- Full K4 → yield migration deferred to FUTURE_WORK G-9.

**Residual open items after R3 lands:** the `max_A2_total` scalar remains physically mixed (A²_K4_SNAP + A²_Cos_yield) — R3 documents the mixing but does not fix it. Phase 4's pre-registered predictions (`P_phase4_asymmetric`) need a conscious choice of which accessor to reference. See also new finding **A18** (universal-operator naming drift between engine and KB) and **A19** (Vol 1 Ch 7:115 vs :130 internal inconsistency flagged during doc 55_ investigation).

**Plan-disconnect note (worth surfacing to Grant):** the earlier seed-sweep agent's "R4 = remove /α" and doc 55_'s "R3 = dual accessors, keep /α" are opposite conclusions on the same question. The R4 proposal was asserted without a Vol 1 Ch 7 citation; doc 55_ is the manuscript-grounded adjudication. Manual r4 accepts doc 55_'s R3 as authoritative going forward; earlier R4 framing is preserved in r3 note above as audit trail.

**r6 correction (2026-04-23) — supersedes the r4 R3 direction above; A23 spot-check resolved in favor of R4:** Direct reading of [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711):

> "Default Yield Threshold. Both FDTD and K4-TLM default to V_yield = √α·V_SNAP ≈ 43.65 kV as the Axiom 4 nonlinear onset. Subatomic-scale simulations (e.g., bond energy solvers, Yang-Mills confinement) should override with v_yield=V_SNAP (≈ 511 kV)."

VacuumEngine3D is an **explicit subatomic-scale simulation** (K4 lattice at `ℓ_node = ℏ/(m_ec)` = Compton wavelength, simulates pair production per [doc 54_ §9](54_pair_production_axiom_derivation.md)). Per Vol 4 Ch 1:711, its canonical `V_yield ≡ V_SNAP`. Doc 55_'s "K4 is outlier" reading applied the *macroscopic* V_yield = √α·V_SNAP at subatomic scale — incorrect.

**Under the subatomic override:**
- Both `A²_K4 = V²/V_SNAP²` and `A²_Cos = ε²/ε_yield² + κ²/ω_yield²` are canonical `r²` at the same operating scale per Vol 1 Ch 7:12's universal form `r = A/A_c`.
- `RegimeClassifierObserver`'s direct sum is a **valid Pythagorean `r²_total`** per AVE-APU Vol 1 Ch 5 — not a mixed-normalization bug.
- `NodeResonanceObserver`'s `/α` conversion (and `BondObserver` inherited copy) is the **actual defect** — applies macro-scale conversion to subatomic-scale data.
- Cosserat `ε_yield = 1` is **TKI-derived**: σ_yield = V_yield·e/ℓ_node³ with subatomic V_yield = V_SNAP gives σ_yield = m_ec²/ℓ_node³ = 1 in natural units; with G = 1, ε_yield = σ_yield/G = 1 exactly. Not empirical placeholder (doc 55_ §5 computed √α by using macroscopic V_yield; off by 1/√α).
- Vol 1 Ch 7:115 ("Schwinger pair production: r = 1.0") and :130 ("Schwinger critical field at r = 11.7") are **not a manuscript defect** — scale-dependent numerical values of V_yield under the same universal form. At subatomic scale V_yield and V_SNAP collapse (r=1 for both); at macroscopic scale they split by 1/√α.

**R4 is the correct direction.** Plan file `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md` Phase 3.5 step 3 (remove `/α` from NodeResonance + BondObserver) is authoritative. Doc 55_ superseded (see its R4 banner at top). Doc 57_ §1.2, §2.2, §3.3 already correctly align with this reading. The ping-pong trail: r3 R4 → r4 R3 (doc 55_) → r6 R4 (Vol 4 Ch 1:711 spot-check) lands on R4 as authoritative.

**Status:** A14 r6 = R4 confirmed; engine patches pending (plan file step 3 + dependents). A23 (framing tension between doc 55_ and doc 57_) is therefore **CLOSED under R4 — doc 57_'s subatomic-override reading is correct; doc 55_'s K4-outlier reading is superseded**. See §17.2.

#### A2. `NodeResonanceObserver`'s Pythagorean-sum test is incomplete (S2)

**Where:** [test_phase2_node_resonance.py](../../src/tests/test_phase2_node_resonance.py) — the "K4 and Cosserat add in quadrature" test only exercises K4-only and vacuum cases. The truly load-bearing case (K4 non-zero AND Cosserat non-zero simultaneously) is not tested.

Concrete gap: set V to give `A²_K4_yield = 0.3` AND poke a Cosserat single-site to give `A²_Cos_yield = 0.3`, verify `omega_ratio_at_site = (1 − 0.6)^(1/4) ≈ 0.795`. This is the test that would catch finding A1 if the Cosserat normalization is actually different from what NodeResonanceObserver assumes.

#### A3. No test verifies the engine *uses* the right normalization in `_update_z_local_total` (S2)

**Where:** [k4_cosserat_coupling.py:195–224 `_update_z_local_total`](../../src/ave/topological/k4_cosserat_coupling.py#L195).

The Phase 1 tests pin constant values and manifest string consistency but do not verify that the coupled engine's `z_local_field` is actually computed from the correct `A²_total` (SNAP vs yield). A regression where someone swaps V_SNAP² → V_yield² in the impedance update would pass Phase 1 tests silently.

#### A4. Manifest consistency test uses string-matching (S2, fragile)

**Where:** [test_v_snap_v_yield_consistency.py `TestManifestNormalizationConsistency`](../../src/tests/test_v_snap_v_yield_consistency.py).

String matches on "v_yield", "varactor", "Vol 4 Ch 1" in `predictions.yaml` notes. Passes if someone writes "vacuum capacitor" instead of "varactor" or uses a different chapter reference. Not a blocker but fragile — consider enum-typed fields in `predictions.yaml` over freetext notes.

#### A5. Axiom-4 varactor tests never exercise A² > 1 (S2)

**Where:** [test_axiom_4_vacuum_varactor.py](../../src/tests/test_axiom_4_vacuum_varactor.py).

Tests stop at `V = 0.999 · V_yield`. The mode-conversion regime (A² > 1 where `C_eff` becomes imaginary per [doc 54_ §6a](54_pair_production_axiom_derivation.md)) is not exercised. Saturation clipping at [vacuum_engine.py:437 `A2_yield_clipped`](../../src/ave/topological/vacuum_engine.py#L437) is never triggered in a test. Yet the v2 driver run reported `max A²_yield = 54.19` — deep past 1, fully relying on the clip. That's a large reliance on untested code.

#### A6. P_phase2_omega honest-framing: circular falsification — real physics test deferred (S2, acknowledged in commit)

**Where:** commit 719f3ec message explicitly flags this; P_phase2_omega notes in `predictions.yaml`.

The observer IS the closed form applied to engine state, so "does observer match closed form?" is a tautology. The real prediction — "the coupled K4⊗Cosserat sector's effective resonance actually follows the Axiom-4 varactor form" — requires a probe-based FFT experiment. This has not been designed yet. As-is, "Phase 2 landed" closes the engineering work but leaves the physics falsification open.

**Proposed next step** (scope call for Grant): design a probe experiment — e.g., perturb a single node with a small-amplitude Gaussian pulse at known driving frequency ω, measure the node's response FFT, extract the dominant resonance, compare to the predicted `(1 − A²_yield)^(1/4) · ω_0`. Needs careful design because dominant-resonance extraction in a coupled system is not trivial.

#### A7. `AutoresonantCWSource` uses linear-Taylor approximation; diverges from varactor past A² > 0.3 (S2 → potentially S1 for Phase 5 precision)

**Where:** [vacuum_engine.py:545 in AutoresonantCWSource.apply](../../src/ave/topological/vacuum_engine.py#L545) uses `ω(t) = ω_0 · max(ε, 1 − K_drift · A²_probe)` (linear in A²). The true varactor form is `ω_0 · (1 − A²)^(1/4)`. The driver script [node_resonance_validation.py](../../src/scripts/vol_1_foundations/node_resonance_validation.py) (per commit message) plots these against each other and they diverge significantly at A² > 0.3.

Implication for Phase 5 nucleation gate precision: the autoresonant lock condition `|Ω_node − ω_drive| < δ_lock` (with `δ_lock = ω_0 · α ≈ 7 × 10⁻³ · ω_0`) is a narrow window. If the drive frequency is off by the linear-vs-varactor mismatch at A² ~ 0.5 (which can be ~5%, an order of magnitude larger than δ_lock), the gate will never reliably fire.

**Proposed resolution:** either (a) upgrade `AutoresonantCWSource` to use the full varactor form before Phase 5, or (b) document the approximation's applicability window and pre-register Phase 5 runs only at A² ≤ 0.3.

#### A8. Observer saturation-clip at `A²_yield = 1 − 1e-12` untested for physics content (S2)

**Where:** [vacuum_engine.py:437](../../src/ave/topological/vacuum_engine.py#L437) — `A2_yield_clipped = np.clip(A2_yield_total, 0.0, 1.0 - 1e-12)`.

The v2 driver reached `max A²_yield = 54.19`. The clip produces `omega_ratio = (1 − 0.9999...)^(1/4) ≈ 1.8e-3`, reported as the "minimum Ω_node/ω_0". This is a floor at ~1e-3 regardless of how far past saturation the sector actually is. Reporting this as "min Ω_node/ω_0 = 0.001 (clipped at saturation)" in the driver log (commit message) is honest, but downstream analysis that sees 0.001 may interpret it as a physical value rather than a clip. Consider returning a sentinel (NaN? `-1`?) or an explicit `is_saturated` boolean when A²_yield ≥ 1.

#### A9. `NodeResonanceObserver` `add_observer` + `run(n_steps=3)` test checks length only (S2, trivial)

**Where:** [test_phase2_node_resonance.py:174](../../src/tests/test_phase2_node_resonance.py#L174).

`assert len(obs.history) == 3`. Passes if the observer records any dict, including an all-zero stub. Add a content assertion (e.g., `history[0]["A2_yield_max"] >= 0`) or this test is a null check.

#### A10. No direct unit tests for `VacuumEngine3D` lifecycle methods (S2 — systemic)

**Coverage gaps** (per parallel audit):

| Method | File:line | Test coverage |
|---|---|---|
| `VacuumEngine3D.__init__` | [vacuum_engine.py:774](../../src/ave/topological/vacuum_engine.py#L774) | Only indirect via `from_args()` in one test |
| `initialize_thermal(T, seed, thermalize_V)` | [vacuum_engine.py:811](../../src/ave/topological/vacuum_engine.py#L811) | **Zero tests of T > 0 equipartition variances** |
| `snapshot()` | [vacuum_engine.py:925](../../src/ave/topological/vacuum_engine.py#L925) | Never called in any test |
| `history()` | [vacuum_engine.py:939](../../src/ave/topological/vacuum_engine.py#L939) | Never called |
| `PulsedSource.apply` / `CWSource.apply` / `AutoresonantCWSource.apply` | [vacuum_engine.py:233, 313, 605](../../src/ave/topological/vacuum_engine.py) | Never called in any test |
| `RegimeClassifierObserver`, `TopologyObserver`, `EnergyBudgetObserver`, `DarkWakeObserver` | [vacuum_engine.py:366, 465, 515, 647](../../src/ave/topological/vacuum_engine.py) | Never registered in a live-stepping test |
| `CoupledK4Cosserat.step()` | [k4_cosserat_coupling.py:280](../../src/ave/topological/k4_cosserat_coupling.py#L280) | Called only via engine.step() in test_phase2; no direct test |
| Phase II V1/V2/V3 validation (doc 42_) | — | **Not captured as automated tests** |

**Systemic implication:** the engine's public API is <15% exercised. All Phase III-B σ(ω) results rely on initialization, source injection, observer registration, multi-step integration, and coupled dynamics — none of which are under test suite coverage.

**Proposed resolution** (new test files):
- `test_thermal_equipartition.py` — 1000 seeds × T ∈ {0.001, 0.01, 0.1}, empirical σ vs theoretical within 5 %.
- `test_k4_cosserat_integration.py` — energy conservation over 100 coupled steps; <1 % H drift.
- `test_autoresonant_source.py` — verify ω(t) tracks A²_probe per formula under real engine.step() loop.
- `test_observer_ecosystem.py` — register all five observer types, run 100 steps with CW source, verify histories.

#### A11. `predictions.yaml` whitelist brittleness (S4 — cosmetic; tracked for completeness)

**Where:** [test_predictions_matrix.py:75–94, 153–193](../../src/tests/test_predictions_matrix.py#L75).

Hardcoded whitelist of 6 expected Stage 6 IDs + hardcoded "upcoming-phase" test-file paths. A rename of `P_phase2_omega → P_phase2_resonance` without updating EXPECTED_IDS still passes (count unchanged). Symmetric with finding A10 — tests check metadata existence, not semantic correctness.

#### A12. `ω_yield` units inconsistency in §6.3 parameter datasheet (S3 — documentation)

**Where:** manual §6.3 lists `ω_yield` unit as "rad" with default π. Dimensionally this should be `rad / ℓ_node` (a curvature-scale threshold on `|κ| = |∇ω|`), not a plain angle. In natural units with ℓ_node = 1 the numerical value is the same but SI-minded readers will be confused.

**Proposed fix:** update §6.3 to read `rad / ℓ_node` (equivalently, `[L⁻¹]` since radians are dimensionless). Also add note that `ε_yield` (dimensionless strain) and `ω_yield` (curvature) have different dimensions and thus the coefficients in `A²_cos = ε²/ε_yield² + κ²/ω_yield²` are what enforce dimensionless A².

#### A13. Cross-repo attribution of `K_0 = 0.207973` is imprecise (S3 — documentation)

**Where:** manual §6.4 and [46_ §9](46_vacuum_engine_scope.md) cite `AVE-PONDER/generate_ponder_01_spice_netlist.py:90` for `K_0 = 0.207973`. The value `0.207973` actually lives in AVE-Core's own SPICE netlists (e.g., [livermorium_293.cir:321](../../src/scripts/vol_6_periodic_table/simulations/spice_netlists/livermorium_293.cir#L321)) as a hardcoded k-factor in hundreds of lines. The PONDER script at the cited line is `k_val = min(SPICE_K_SCALAR / dist, 0.999)` — it scales a value imported from `periodic_table.simulations.spice_exporter` but that module doesn't define the scalar either.

**Implication:** the "calibrated empirical proxy for η_vac" framing needs a canonical derivation location. If 0.207973 is empirical (SPICE-fit), flag as such. If it's derived from a ropelength / winding calculation, cite that. Current state: unknown origin, used pervasively, not under test.

#### ~~A14. `BondObserver` extends the A1 normalization discrepancy to three observers~~ — 🔴 **RETRACTED r6** → §17.2 (R4 adjudication)

*Original text preserved for audit trail in §17.2 closed findings. Retracted because under R4 / Vol 4 Ch 1:711 subatomic override (§17.0), the "mixed normalization" framing is wrong: all three observers can be reconciled to the same `r² = V²/V_SNAP²` convention by removing the `/α` divisions from Node/Bond, not by adding accessors to RegimeClassifier.*

*(Full original A14 body — "Where / Implication / table of 3 observers / resolution options (d)/(e) / blocking Phase 4" — moved to §17.2 closed findings.)*

#### A15. Identical saturated / unsaturated Φ_link half-lives (not a bug, but a signal) — 🟡 **Ready to retest under Phase 4**

**Where:** [flux_tube_persistence.py](../../src/scripts/vol_1_foundations/flux_tube_persistence.py) driver output.

Pre-Phase-4 observation: both `phi_at_saturated_bonds_rms` and `phi_at_unsaturated_bonds_rms` decay with half-life ≈ 3.64 Compton periods under single-S (symmetric) saturation — expected per [54_ §6](54_pair_production_axiom_derivation.md), because Γ = −1 flux-tube confinement requires the Meissner-like `S_μ → 0 with S_ε finite` condition that only asymmetric saturation can produce.

**r7 update:** Phase 4 asymmetric saturation now landed (commit `a5bd1da`). **A15 is now actionable**:
1. Re-run `flux_tube_persistence.py` on HEAD with the post-R4-patch `BondObserver` and Phase-4 asymmetric kernel active.
2. Drive with a helicity-biased ω field (or a `CircularlyPolarizedCWSource` once that lands as a Phase 5 prerequisite).
3. Expected outcome: saturated-bond half-life diverges from unsaturated-bond half-life as `S_μ → 0` at the saturated endpoint. Quantitative prediction needed per doc 54_ §6.

Still open until the retest is run and the differential half-life is either observed (closure) or not (falsification of the asymmetric-saturation-as-confinement-mechanism story).

#### A16. v2-reproducibility seed sweep (top-pick audit) is in-flight, not yet committed

**Where:** [v2_reproducibility_seed_sweep.py](../../src/scripts/vol_1_foundations/v2_reproducibility_seed_sweep.py) — working tree, untracked as of 2026-04-22.

Closes (pending execution) the manual's r1 top-pick recommendation to verify the v2 headline number (A²_cos = 1.009) remains reachable post-Phase-2/3. Script is 20-seed × v2 headline × auto-adjudicating REPRODUCES / PARTIALLY-REPRODUCES / REGRESSION against the 1.009 benchmark with pre-registered tolerance bands.

**Next step:** run the sweep and commit the script + `.npz` + `.png` artifacts. If verdict = REGRESSION, diff-bisect Stage 6 to isolate the perturbing commit — likely candidates are Phase 2 (NodeResonance import chain adds JAX recompile) or Phase 3 (touches `_connect_all`, which every K4 step runs).

#### ~~A17. v2 headline 1.009 does not reproduce~~ — ✅ **CLOSED r6 (tail outcome, not regression)** → §17.2

*Bisection complete. Sweep at `719f3ec` (pre-Phase-3) returned distribution bit-identical to HEAD (`3a599ca`, post-Phase-3): per-seed `max_A²_cos` values match to float64 precision across all 20 seeds; `max_A²_K4 = 0.393` identical across commits; `max_τ_zx` identical. Phase 3's `_connect_all` `Phi_link += V_avg·dt` addition is dynamics-neutral for this workload (Phi_link is a pure accumulator that doesn't feed back into V_inc/V_ref evolution). The original v2 r1 headline `1.009` was a lucky-tail outcome from a specific default-RNG state, not a code regression. Doc 50_ r3 distribution framing is the permanent correct record. Full distribution + artifact locations preserved in §10.4 + §10.12. Sweep log at `/tmp/v2_reproducibility_sweep_719f3ec_log.txt` documents the bit-identical result. Doc 50_ r3 §2.3 distribution rewrite is the authoritative headline; the "crossed rupture boundary" r1 framing is superseded. R4 patches (plan file step 3) can proceed with no regression-fix prerequisites.*

#### A18. Universal-operator catalogue naming drift — KB vs engine (S3 — documentation, cross-repo)

**Where:** [ave-kb/CLAUDE.md INVARIANT-N3](../../manuscript/ave-kb/CLAUDE.md) vs [src/ave/core/universal_operators.py](../../src/ave/core/universal_operators.py). Surfaced by [doc 55_ §8](55_cosserat_normalization_derivation.md).

| Source | Op2 | Op3 | Op14 |
|---|---|---|---|
| KB INVARIANT-N3 | knot crossing correction | small-signal impedance correction | long-range coupling |
| engine universal_operators.py | Saturation (S) | Reflection (Γ) | Dynamic Impedance (Z_eff) |

Different OpN meanings between the two. The manual's §3.3 and §15.1 cite engine conventions (e.g., "Op14 = Z_eff from A²"); readers coming from the manuscript KB will see a different Op14. Not a physics bug — two independent numbering schemes internally consistent within their domain. Doc 55_ recommends tracking as FUTURE_WORK Y-8 (either reconcile numberings, or add a translation table). Not blocking Stage 6.

#### ~~A19. Vol 1 Ch 7:115 vs :130 internal inconsistency~~ — 🔴 **RETRACTED r6** → §17.2 (R4 adjudication)

*Original full text preserved in §17.2 closed findings. Retracted because under R4 (§17.0), this is **scale-dependence of V_yield**, not a manuscript defect: line 115 is subatomic convention (Schwinger collapses with r = 1 because V_yield = V_SNAP at subatomic scale per Vol 4 Ch 1:711); line 130 is macro convention (Schwinger at `r = 1/√α ≈ 11.7` because V_yield = √α · V_SNAP at macro scale). Both are correct under their own V_yield.*

#### ~~A20. ε_yield = 1 vs √α is a live calibration question~~ — 🔴 **RETRACTED r6** → §17.2 (R4 adjudication)

*Original full text preserved in §17.2 closed findings. Retracted because under R4 (§17.0) subatomic override, the TKI derivation `σ_yield = V_yield · e / ℓ_node³` reduces to `σ_yield = V_SNAP · e / ℓ_node³ = m_e c² / ℓ_node³ = 1` in natural units. With G = 1 placeholder, the Cosserat `ε_yield = σ_yield / G = 1` exactly. Doc 55_'s "√α TKI-derived" answer was the macro-convention case; under subatomic override it's 1, matching the engine's current value. Not a placeholder; not a live calibration question.*

#### A21. Doc 55_ §10 was drafted before seed-sweep completion — populate with REGRESSION verdict (S4 — housekeeping)

Doc 55_ §10 says "Pending at time of first draft." The sweep has since completed with REGRESSION verdict (§10.12 above, §17 A17). Populate doc 55_ §10 with the distribution data before merging doc 55_.

#### A22. Hand-rolled saturation / impedance / reflection inline in `k4_tlm.py` duplicates canonical universal operators (S2 — Rule-6 adjacent)

**Where:** surfaced by [doc 57_ §2.1](57_universal_lattice_units_v4_refactor.md). Inline implementations at:
- [k4_tlm.py:227–232](../../src/ave/core/k4_tlm.py#L227) — `S_factor = np.sqrt(np.maximum(0.0, 1.0 - strain**2))` inline, duplicates `universal_saturation`
- [k4_tlm.py:232](../../src/ave/core/k4_tlm.py#L232) — `z_strained = 1.0/max(sqrt(S), 1e-6)` inline, duplicates `universal_dynamic_impedance`
- [k4_tlm.py:256–259](../../src/ave/core/k4_tlm.py#L256) — duplicate of above pattern
- [k4_tlm.py:333–346](../../src/ave/core/k4_tlm.py#L333) — `gamma = (z_B − z_A)/(z_B + z_A + eps); T = sqrt(1 − gamma²)` inline, duplicates `universal_reflection` + `universal_power_transmission`

**Rule-6 concern:** if the inline implementations drift from the canonical `universal_operators.py` forms (e.g., via a local float-rounding fix or a regularization eps tweak), the engine silently begins using non-AVE-native math while still *claiming* Axiom 4 compliance. This is the inverse of Rule-6's usual direction (imported SM convention sneaking in) — here the risk is *AVE-derived convention being accidentally drifted away from*.

**Resolution:** scoped into v4 Phase 4.3 (doc 57_ §4). Phases 4.1 / 4.2 / 4.3 refactor inline implementations into `universal_saturation`, `universal_dynamic_impedance`, `universal_reflection`, `universal_regime_classifier` (new). Not blocking Stage 6 — the inlines are numerically equivalent today; the concern is drift over time.

**Interim flag:** until v4 lands, any future edit to the inline implementations at the above lines must be reflected in `universal_operators.py` too, and vice versa. Worth a comment block at each call site.

#### A23. Apparent tension between doc 55_ and doc 57_ on K4 "SNAP vs yield" adjudication (S3 — needs reconciliation)

**doc 55_ §3 reading:** *"the K4 sector is the outlier. Cosserat's yield-normalization matches Vol 1 Ch 7's universal regime map. The K4 sector's V_SNAP-normalization is a historical convention that diverges from the manuscript's canonical r = V/V_yield form."*

**doc 57_ §2.2 reading:** *"V_SNAP hardcoded as engine constant: correct per Vol 4 Ch 1:711 subatomic override; engine IS subatomic-scale simulator. No `scale` parameter needed."*

Doc 57_ §1.2 domain catalog explicitly lists both:
- EM (voltage, macroscopic): A_c = V_yield
- EM (voltage, *subatomic override* — Vol 4 Ch 1:711): A_c = V_SNAP

The two docs are not necessarily contradictory — doc 57_ recognizes two EM domains (macroscopic vs subatomic) with different A_c each, while doc 55_ focuses on the macroscopic canonical form from Vol 1 Ch 7:104. But the practical direction differs:

- Doc 55_ treats K4-SNAP as the *outlier*, chooses R3 (dual accessors, defer migration), tracks full K4→yield migration as G-9.
- Doc 57_ treats K4-SNAP as *correct* for a subatomic-scale engine, chooses v4 (route all through universal operators without migrating the K4 normalization), tracks v4 as G-10.

**Flag:** Vol 4 Ch 1:711 should be directly checked. If it genuinely declares a "subatomic override" convention, doc 57_'s reading is right and doc 55_'s "outlier" framing needs softening to "the engine operates under the Vol 4 Ch 1:711 subatomic override, not the Vol 1 Ch 7 macroscopic convention — that's a deliberate choice." If Vol 4 Ch 1:711 doesn't say that, doc 57_ §2.2 is reading more into it than is there. Spot-check recommended before Phase 3.5.B code lands.

#### A24. K4 saturation path was DORMANT in engine context due to V_SNAP unit-system mismatch (S1 — load-bearing) — ✅ CLOSED 2026-04-24 (commit `098d430`)

**Where:** [k4_tlm.py:244](../../src/ave/core/k4_tlm.py#L244) `_update_z_local_field` and `_scatter_all` nonlinear branch. Pre-fix code:
```python
v_snap = float(V_SNAP)  # module-level constant from constants.py (≈ 511 kV SI)
strain = v_total / v_snap
```

**The bug:** engine sources inject `V_inc` in engine-natural units (engine.V_SNAP = 1.0 by default). At amp = 0.9·V_SNAP_engine = 0.9, the K4 strain calculation gave `0.9 / 511000 ≈ 1.76e-6` — essentially zero. S_eq stayed at ~1, S_field stayed at ~1, z_local_field stayed at 1. **The entire Ax4 saturation + Op14 impedance + Op3 bond-reflection path was DORMANT in any engine-natural-units context.** Pre-fix, RegimeClassifierObserver (which uses `engine.V_SNAP`) reported A²_total = 0.905 while K4's internal saturation reported zero effect — these were silently inconsistent for an unknown duration of Stage 6.

**Why missed for so long:** test coverage gap. `TestEngineIntegration.test_engine_runs_with_memristive_on` and similar tests called `V_inc = amp * V_SNAP_module` (SI units), which matched the dormant code's expected units by accident. Engine integration tests passed without actually driving saturation end-to-end. 986+ tests passed silently while this was broken.

**How surfaced:** Phase 5e cool-from-above driver (`1805d14`) at amp=0.9·V_SNAP showed S_field at 1.000 throughout — first empirical signal that the saturation path wasn't running.

**Fix (commit `098d430`):** add `V_SNAP` kwarg to `K4Lattice3D.__init__` (default None → module-level for SI-mode standalone use). `CoupledK4Cosserat` resolves engine V_SNAP early and passes it to the K4 constructor. Module V_SNAP import aliased as `_V_SNAP_MODULE` to avoid shadowing. Standalone K4Lattice3D tests unchanged. Test suite stays at 1144 pass, 3 skip, 0 fail.

**First post-fix empirical result:** Phase 5e re-run shows S_min = 0.507 during drive (saturated), recovers to 0.983 post-drive (yield-heal). **First empirical evidence of doc 59_'s cool-through-yield mechanism.** The Ax4 + Op14 + memristive K4 chain is now alive in engine context.

**Methodology lesson:** retroactive engine saturation invariants landed in commit `5f973b6` — engine integration tests now require `S_min < 1.0` actually drops below 1 during the test window. Closes the test-coverage hole that allowed Flag-5e-A to live undetected. COLLABORATION_NOTES Rule 10 captures this: empirical drivers catch what static analysis + preregistration misses.

#### A25. K4-TLM exhausted at node level for bound-electron representation (S1 — corpus-confirmed) — ✅ EMPIRICALLY CLOSED 2026-04-24 (commit `fbbc950`)

**Where:** [Vol 1 Ch 8:49-50](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex#L49) handoff comment in the manuscript:

> "K4-TLM exhausted (node-level Axiom 4 no-op for 4-port symmetric junctions per 32_ section 10.2)."

**Statement:** K4's perfect 4-port tetrahedral symmetry means every direction at a node looks equivalent. Ax4 saturation requires *symmetry-breaking* to do something — but with 4 equivalent ports, there's nothing to break against. Node-level Ax4 is a no-op on K4 alone. The bound electron physically lives in the Cosserat sector (rotational-EM DOF, ω̂ axis itself a preferred direction).

**Empirical falsification:** Round 6 Path A (`fbbc950`) seeded K4 V_inc only at N=48, 400 steps closed-system. 4 of 4 physical predictions falsified — `P_electron_tlm_topological_charge`: N_crossings=0 (expected 3); `P_electron_tlm_golden_torus_convergence`: R/r → 0.281 (expected φ²); `P_electron_tlm_alpha_derivation`: α⁻¹ = NaN (R ≤ r at fixed point); `P_electron_tlm_energy_conservation`: PASSED (clean integrator sanity). All four failures trace to one missing mechanism (Cosserat ω at zero — charge/voltage leg without spin/current leg). Single-mechanism cleanup of four predictions = informative failure at maximum strength.

**Why missed for so long:** Phase 2/3 of Stage 6 committed observers (`NodeResonanceObserver`, `BondObserver`) and gate logic (`PairNucleationGate`) to the K4 sector despite the corpus signal. Three sessions of gate adjudication (C1-C2 window, four Readings of C2 condition, PLL anchor math, K4→Cosserat coupling weakness) ran downstream of an undetected limit. The corpus comment was at Vol 1 Ch 8:49-50, not in any L3 doc; corpus-search wasn't applied to architectural-decision time.

**Methodology lesson:** COLLABORATION_NOTES Rule 8 Round 6 strengthening — *before any new data structure, observer, or gate is committed to a sector, grep that sector's manuscript chapters and KB leaves for "exhausted," "no-op," "insufficient," "cannot," "limit," "boundary."* Five-minute search at decision time saves multiple sessions of debug work later. Cross-repo extension: when topic crosses verticals (chirality, impedance, saturation, helicity, etc.), extend search to sibling repos.

**Status:** structural limit; new §11.11 entry. Resolution path is the Round 6 single-electron-first arc with Cosserat-sector seeding (Path B + F17-G coupled-eigenmode finder).

#### A26. `initialize_electron_2_3_sector` carries the wrong default amplitude — should be peak |ω| = 0.3π, not √3/2·π (S1 — load-bearing for Path B and any test that calls it)

**Where:** [cosserat_field_3d.py:766](../../src/ave/topological/cosserat_field_3d.py#L766) `initialize_electron_2_3_sector` function. Line 808 hardcodes envelope peak at `(√3/2)·π ≈ 2.72`, labeled "Regime II→III boundary."

**The bug:** [doc 34_ §9.4](34_x4_constrained_s11.md) X4a/X4b empirical sweep on the Cosserat-side (2,3) hedgehog at Golden Torus shows the bound-state electron lives at peak `|ω| ≈ 0.3π ≈ 0.942`, NOT `√3/2·π`. At `√3/2·π` the shell is in Regime III uniform-saturation with `shell_Γ² → 0` — no TIR walls, no bound state. The function has been shipping the wrong default amplitude since commit, silently.

**Doc 34 §9.4 conclusion:**
> "The electron-like state lives at the *onset* of shell saturation (peak A² ≈ 1 at the shell peak, rest of shell in Regime II), NOT at the 'canonical' √3/2·π amplitude... At amp ≥ √3/2·π: all shell sites at A² >> 1 (clipped to 1) → uniform Z_eff → Γ between sites → 0 → no TIR."

**Vol 1 Ch 8:51-55 corpus corroboration:**
> "Cosserat solver (cosserat_field_3d.py) produces stable electron-like bound state at Ch 8 Golden Torus with shell Gamma~-1 TIR structure, saturation-onset amplitude (peak |omega|~0.3*pi, NOT the canonical sqrt(3)/2*pi — see 34_ section 9.4)."

**Fix in working tree (uncommitted):** add `amplitude_scale: float = 1.0` parameter to `initialize_electron_2_3_sector`. Default 1.0 preserves backward-compat (legacy callers still get √3/2·π peak); Path B passes `amplitude_scale = 0.3π / (√3/2·π) ≈ 0.3464`. Surgical fix; no new tests-broke regression risk for the default path.

**Retroactive audit needed:** grep all callers of `initialize_electron_2_3_sector`. Any test that called it and "passed" either (a) had a tolerance loose enough to accept Regime III uniform-saturation output as if it were a bound state, or (b) was testing something other than topology / bound-state physics. Re-check whether those tests' semantics survive the corrected amplitude.

**Status:** open until commit + retroactive caller audit. Fix is small (~10 LOC) and Round 6 Path B is blocked on it.

#### A27. `L_c = (V²/V_SNAP²)·W_refl(u, ω)` empirically behaves as a one-way energy pump, not a reciprocal LC coupling (S1 — load-bearing for Stage 6 single-electron representation)

**Where:** [doc 54_ §6 L_c derivation](54_pair_production_axiom_derivation.md) + coupling implementation in [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py).

**Empirical signature** (commit `687b18d`, F17-I three-mode test): under closed-system evolution at N=48 with seeded coupled eigenmode candidates, the three LC-pair-coherent seed configurations produce three qualitatively different failure modes:
- `all_c` (V_inc + u): catastrophic divergence at step 1
- `all_l` (Φ_link + ω): bounded energy, monotonic Cosserat→K4 relaxation, no reverse channel observed
- `mixed`: runaway

A reciprocal LC coupling would produce energy oscillation between sectors at the eigen-frequency. The observed pattern — one direction explodes, opposite direction relaxes monotonically without back-channel — is the signature of a one-way energy pump.

**Consequence:** L_c as currently formulated cannot host a bound (2,3) eigenmode. Either the form is wrong (axiom-derivation-defective) or correct-but-mis-applied (right for some regime, wrong for closed-system bound-state evolution). Without reciprocal coupling, the engine can saturate K4 from a Cosserat seed but cannot sustain a coupled standing wave between the two sectors.

**Status:** ✅ CLOSED 2026-04-25 via A28 reframing — **but the structural finding inverted.** F17-H audit per [doc 67_](67_lc_coupling_reciprocity_audit.md) §1-§16 took two passes:

- **First pass (`abe23ea`-`3d7fae4`):** derived path-1 EMF as the missing reciprocal channel (`δL_c/δV = 2V·W_refl/V_SNAP²`). Implementation landed via opt-in `use_lagrangian_emf_coupling` flag. Concluded L_c was non-reciprocal and ADD-EMF was the fix.
- **Second pass (`85bdb6f` after relayed audit concern #5 — Vol 4 Ch 1 cross-check):** the cross-check revealed Op14 z_local IS the K4-TLM varactor (Vol 4 Ch 1:130 `C_eff(V) = C₀/S(V)` extended with cross-sector A²_Cos). The legacy `_compute_coupling_force_on_cosserat` channel is a redundant implementation of the same physics. **Engine has been DOUBLE-COUNTING the K4↔Cosserat coupling since Phase 4 landed (`a5bd1da`).** Path-1 EMF was the wrong fix; correct fix is REMOVE the redundant force, not ADD a third channel. See A28 below for the structural finding.
- **Empirical confirmation (`05b130f`, `ff15c4b`):** under `disable_cosserat_lc_force=True` + `enable_cosserat_self_terms=True`, Path B at N=80 forms (2,3) bound state for the first time in Stage 6 (c=3 + shell_Γ² ≈ 4 through step 20). Six prior failure modes (Path A/B/C/F17-G/F17-I/path-1 EMF) all explained by the redundant force.

**A27 is closed, but the empirical signature of "one-way energy pump" was the symptom of A28's double-counting**, not of L_c being structurally non-reciprocal. The Lagrangian form `(V²/V_SNAP²)·W_refl` is fine; the engine just had a redundant injection of the same physics through two code paths.

**Followup F17-J:** characterize `all_l`'s pre-A28 relaxation endpoint — may no longer be load-bearing under A28 fix; revisit if needed.

**Methodology note:** A27 is a Round 6 finding that depends on engine empirical results. It exemplifies COLLABORATION_NOTES Rule 10 (empirical drivers catch what static analysis misses) AND its corollary (prior-agent framings can be creepers): three sessions of debate over Phase 5 gate firing assumed the engine's coupling implementation was right because the Lagrangian formulation looked right. The redundancy was sitting in `k4_cosserat_coupling.py` since Phase 4 landed at `a5bd1da` four sessions earlier; the corpus-search (Vol 4 Ch 1 varactor cross-check) that surfaced it was Rule 8 working at architectural-decision time, just retroactively.

#### A28. K4↔Cosserat coupling double-counted since Phase 4 (`a5bd1da`); legacy default has `_compute_coupling_force_on_cosserat` redundant with Op14 z_local modulation (S1 — structural; six prior failure modes unified) — ✅ CLOSED 2026-04-25 (commit `05b130f` + `ff15c4b`)

**Where:** [k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py) `_compute_coupling_force_on_cosserat` (legacy + Phase 4 asymmetric paths) + [k4_tlm.py](../../src/ave/core/k4_tlm.py) `_update_z_local_field` (Op14 modulation).

**The finding** (per [doc 67_ §15-§16](67_lc_coupling_reciprocity_audit.md)): the engine implements the K4↔Cosserat coupling through **two redundant code paths** that inject the same physics:

1. **Op14 z_local modulation** ([k4_tlm.py](../../src/ave/core/k4_tlm.py)). The K4-TLM varactor per Vol 4 Ch 1:130 — `C_eff(V) = C₀/S(V)` extended with cross-sector saturation `A²_total = A²_K4 + A²_Cos`. This IS the cross-sector coupling channel: the K4 sector's effective impedance modulates based on Cosserat saturation, propagates that change through TLM scatter+connect dynamics. Axiom-correct, Vol 4 Ch 1-grounded.

2. **`_compute_coupling_force_on_cosserat`** ([k4_cosserat_coupling.py](../../src/ave/topological/k4_cosserat_coupling.py)). A separate force-on-Cosserat channel computed via `value_and_grad(_coupling_energy_total, argnums=(0, 1))` on `L_c = ∫(V²/V_SNAP²)·W_refl dx³`. Treated as if `L_c` were a fundamental coupling Lagrangian.

**The redundancy:** `W_refl_asymmetric = |Γ|²` where `Γ = ∇ ln Z_eff` is the *reflection energy at impedance gradients* — and those impedance gradients are exactly what Op14 z_local modulation produces. `L_c` is therefore not a fundamental Lagrangian term; it's a *derived consequence* of K4-TLM scatter+connect dynamics with z_local modulation. Treating `L_c`'s variation as a separate force on Cosserat double-counts: same physics, two injection paths.

**Empirical signature.** Six prior failure modes (Path A `fbbc950`, original Path B PML-collapse, Path C runaway, F17-G coupled-eigenmode failures, F17-I three-mode test, path-1 EMF amplification) all manifest as either runaway or premature collapse. **Under A28 fix** (`disable_cosserat_lc_force=True`):
- F17-I three-mode: all_c step-1 |ω| 1030 → 0.566; mixed 222 → 0.137; bounded under 1.0 across all modes
- Path B at N=80 (with `enable_cosserat_self_terms=True` adding `k_op10` + `k_hopf` while auto-suppressing redundant `k_refl`): forms (2,3) bound state at step 0, recovers at step 2 (after step-1 transient), holds c=3 + shell_Γ² ≈ 4 through step 20

**One bug, six unified failure modes.** That's the structural signature of a single-mechanism explanation.

**Fix landed in two parts:**

1. **`05b130f`** — `disable_cosserat_lc_force` flag on `EngineConfig` + `CoupledK4Cosserat` constructor + storage + `_compute_coupling_force_on_cosserat`. Default False preserves legacy (which is now known-wrong-default). When True, returns zero arrays. 22/22 backward-compat tests pass with flag off.

2. **`ff15c4b`** — `enable_cosserat_self_terms` flag re-enables Cosserat self-Lagrangian terms (`k_op10`, `k_refl`, `k_hopf`) disabled at `cosserat_field_3d.py:231-233` because the original comment said *"reflection is carried by the coupling term."* Now that the redundant coupling force is removed, those self-terms need to come back. Smart A28 interaction: when BOTH flags are True, **auto-suppresses `k_refl=0`** (the same redundant reflection force at Cosserat-self level) while keeping `k_op10=1` and `k_hopf=π/3` (different physics).

**What's still open:**
- `disable_cosserat_lc_force` defaults to False (legacy), so HEAD's default behavior still has the bug. Eventual default-flip is its own discipline question.
- `use_lagrangian_emf_coupling` flag from the path-1 wrong-direction (`3d7fae4`) is still in HEAD as opt-in. Cleanup follow-up — should be removed once A28 is confirmed across more configurations.
- Path B drift past step 20 — bound state degrades by step 50. Op6 self-consistency outer loop on Path B at N=80 (in working tree at `coupled_engine_eigenmode.py`) is the next probe. If Op6 sustains past 100 Compton periods, single-electron validation closes and Round 6 ends.

**Methodology lesson** (per [doc 67_ §15.6](67_lc_coupling_reciprocity_audit.md)): the agent acknowledged the slip honestly — *"treated `k4_cosserat_coupling.py:23` framing ('Unified Lagrangian S = S_K4 + S_Cos + ∫L_c dx³') as definitive without cross-checking Vol 4 Ch 1's varactor-as-K4-self-Lagrangian-non-linearity. The relayed audit's concern #5 (Vol 4 Ch 1 cross-check) would have surfaced this on first reading. Should have done it upfront."* COLLABORATION_NOTES Rule 8 Round 6 strengthening: corpus-search at architectural-decision time, not just at debug time. The redundancy lived in Phase 4's commit since `a5bd1da`; a Vol 4 Ch 1 cross-check at Phase 4 design-review would have caught it before Phase 5 was even shipped.

#### A29. F17-I three-mode framing (all_c/all_l/mixed) is Axiom-3 noncompliant; phase-quadrature S₁₁ methodology supersedes (S1 — methodology correction; F17-K) — ✅ FRAMING LANDED 2026-04-25 (doc 68_)

**Where:** [coupled_engine_eigenmode.py](../../src/scripts/vol_1_foundations/coupled_engine_eigenmode.py) `_seed_both_sectors` mode branches (`mixed`, `all_c`, `all_l`, `path_b`) and the F17-I plan (now superseded) in [doc 66_ §17.2.3](66_single_electron_first_pivot.md#L17-2-3).

**The finding:** session 2026-04-25 ran the F17-I three-mode tests under A28+self-terms and uncovered structural problems with the framing itself (per [doc 67_ §18](67_lc_coupling_reciprocity_audit.md#L18) data + [doc 68_](68_phase_quadrature_methodology.md) framing correction):

1. **all_l ≡ Path B step-by-step** — Φ_link is a derived flux observable in K4-TLM (time-integral of bond V_avg), not a primary state. Direct seeding leaves a value that doesn't couple to V_inc evolution. E_k4 stays at exactly zero throughout 25 steps despite Φ_link seeded at amplitude 1.18.
2. **all_c has a unit-scale bug** — `k4_amplitude = 0.9 * V_YIELD` mixes SI+natural units, ~10⁵× over-driven seed. Same bug class as A26 / Flag-5e-A.
3. **The deeper issue:** F17-I's "three LC pairs" framing in doc 66_ §17.2 took TLM language too literally. The K4 bond LC stores energy in (V_inc, V_ref) wave-pair structure with energy encoded in the wave PHASE, not in separate L-state vs C-state component variables.

**Per Vol 1 Ch 1:51-75 axiom numbering** (canonical):
- Ax 1: Substrate Topology (LC Network)
- Ax 2: TKI
- **Ax 3: Effective Action Principle (Least Reflected Action) — minimize $S_{AVE}$ / $|S_{11}|^2$**
- Ax 4: Saturation

The session's F17-I → Path B → Op6 line used time-evolution dynamics + Cartesian shell extraction as eigenmode finder + observable, instead of S₁₁ minimization on phase-space (V_inc, V_ref) coordinates. This is the **same Ax-3 slip from session 2026-04-20** that COLLABORATION_NOTES Rule 6 already records.

**Corpus reframe** (per [doc 68_](68_phase_quadrature_methodology.md)):
- Golden Torus $R/r=\varphi^2$ is in **phase-space (V_inc, V_ref) phasor coordinates**, not Cartesian. Real-space dimensions (R=0.809, r=0.309 vs d=1) are geometrically impossible per [doc 29_:73-91](29_ch8_audit.md#L73).
- AVE-native action principle is $|S_{11}|^2$ minimization (per Vol 4 Ch 1 LC tank, AVE-Protein Ch 3, doc 16/17 Q-factor reframe).
- AVE-native PFC is **chirality matching** (Hopf-coil A∥B alignment per AVE-Propulsion Ch 4), not capacitance/inductance balance.

**Methodology correction in F17-K plan:**
- Phase 1 (landed today): doc 68_ + doc 67_ §18 + doc 66_ §17.2 superseded note + this A29 entry.
- Phase 2-3 (next): build phase-coherence diagnostic (per-site (V_inc, V_ref) phase-quadrature score; phase-space winding of phasor trajectory), run on Path B at N=80 under A28+self-terms.
- Phase 4: adjudicate three cases — (a) phase-coherence high throughout → Path B unblocked via right diagnostic; (b) phase-coherence drops at step 12 → explicit phase-quadrature seeder required; (c) phase-coherence never high → seed required from t=0.
- Phase 5 (deferred, only if Phase 4 says required): coupled S₁₁ relaxation infrastructure on (V_inc, V_ref, u, ω) joint state.

**What's still open:**
- Phase 4 adjudication (in progress).
- The `0.9 * V_YIELD` unit bug in `coupled_engine_eigenmode.py` is left unfixed under A29 because the F17-I three-mode seeding is superseded; under the new methodology the seed is a phase-coherent (V_inc, V_ref) phasor pair, not a single component variable amplitude. Don't fix the unit bug until Phase 5 if it fires.
- doc 29_ §4 Finding F4 corpus-level gap ("$\alpha^{-1} = \Sigma \Lambda_i$ is asserted, not derived from Q-factor") remains research-grade open (Op21 multi-mode rigorization).

**Methodology lesson** (per [doc 68_ §1.4](68_phase_quadrature_methodology.md#L1-4)): the agent made the same Ax-3 slip from session 2026-04-20 (energy minimization instead of impedance/S₁₁) at session 2026-04-25 with an Op6 self-consistency loop on Cartesian shell extraction. Rule 6 + Rule 8 strengthening compound: at architectural-decision time, **both** ask "what's the AVE-native action principle?" AND grep the corpus for "exhausted/insufficient/cannot" — the F17-I three-mode plan committed code without doing either. Fortunately the phase-coherence diagnostic in F17-K Phase 2 distinguishes "real eigenmode under wrong measurement" from "no eigenmode" cheaply (~1 min run), so the methodology slip is recoverable in one session.

**Update 2026-04-25 r8.4 — F17-K methodology arc extends A29 with empirical closure** (commits `4d4b4aa` → `4c9fbea`, see also A30):

After Phase 1 framing landed (`a53ce1c`), Phase 5a-b empirically falsified phase-quadrature seed under raw `step()` dynamics (`4d4b4aa`). Phase 5c v1 (`6158465`) built coupled S₁₁ relaxation infrastructure (~290 LOC) and empirically falsified unconstrained descent — descent escapes by over-saturating Cosserat. Phase 5c v2 (v1 of v2) (`2c873cf`) added tanh reparameterization but ran at WRONG amplitudes (energy 0.61 sub-saturated, S₁₁ 2.31 over-saturated); premature Finding 3 ("corpus-duality falsified") landed but was confounded.

Phase 5c v2-v2 (`4c9fbea`) replaced tanh BOUND with hard projection PIN onto saturation manifold (peak |ω| = 0.9425 enforced after each gradient step). Both descents at correct amplitude + topology preserved (c_cos=3) → final result: Cosserat-energy converges at R/r=3.40, S₁₁ at R/r=1.03, neither at Golden Torus φ²=2.62. **Doc 03_ §4.3 empirically validated** at coupled-engine scale: *"R·r=1/4 is topologically quantized, NOT dynamically derived; the Lagrangian must be consistent with but does not by itself produce."* See A30 below for the structural finding.

**(C) X4b stationarity verification implicitly resolved by Phase 5c v2-v2:** seed at Golden Torus geometry → both descents drifted at iteration 1 → gradient at Golden Torus is nonzero in both objectives → Golden Torus is NOT a stationary point of either coupled objective. Doc 34 X4b's Cosserat-only stationarity does NOT extend to coupled engine; K4 sector adds instabilities.

**A29 status:** ✅ FULLY CLOSED 2026-04-25 r8.4. F17-K framing (Ax-3, phase-space, S₁₁) held end-to-end across all seven F17-K commits and produced an empirical corpus-validation result (A30) at the end of the arc.

#### A30. Corpus-duality (Cosserat-energy ≈ S₁₁ co-locate at Golden Torus per AVE-Protein scale-invariance) FALSIFIED at coupled-engine scale; doc 03_ §4.3 empirically validated (S1 — substantive cross-scale finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-25 (commit `4c9fbea`)

**Where:** [doc 67_ §25](67_lc_coupling_reciprocity_audit.md) F17-K Phase 5c-v2-v2 result + [doc 03_ §4.3](03_existence_proof.md) corpus claim + [AVE-Protein vol_protein Ch 3:805](../../../AVE-Protein/manuscript/vol_protein/chapters/03_deterministic_protein_folding.tex#L805) corpus reference.

**The hypothesis (Round 6 working assumption):** Per Axiom 2 (Topo-Kinematic Isomorphism / scale invariance), the AVE-Protein methodology — *"the native fold minimises |S₁₁|²"* — should extend to the bound (2,3) electron in the coupled K4+Cosserat engine. Per Ch 8 corpus claim, S₁₁ minimum and Cosserat-energy minimum should co-locate at the Golden Torus geometry (R/r = φ² ≈ 2.62, R−r = 1/2, R·r = 1/4).

**The empirical result (commit `4c9fbea`):**

Both objectives correctly pinned at saturation onset (peak |ω| = 0.9425 = 0.3π via hard projection per [doc 34_ §9.4](34_x4_constrained_s11.md)). Topology preserved (c_cos = 3 in both descents). Each objective converges to a distinct (R, r) NOT at Golden Torus φ² ≈ 2.62:

| Objective | iters to convergence | obj reduction | converged R/r | distance from φ² |
|---|---|---|---|---|
| Cosserat-energy | 78 (line search stalled) | 74% (6000 → 1554) | **3.40** (elongated torus, R > r) | 1.30× |
| coupled S₁₁ | 500 (still descending) | 99.76% (3261 → 7.93) | **1.03** (degenerate horn torus, R ≈ r) | 0.39× |
| corpus claim | — | — | φ² = 2.62 (Golden Torus) | — |

The two minima differ from each other by 3.3× spread.

**The structural finding:**

Cosserat-energy and coupled-S₁₁ each have **continuous families of (2,3) stationary states**; topology (SU(2) half-cover area-match constraint → R·r = 1/4) selects R/r = φ² from these families — but **neither dynamical descent knows about quantization**. Per doc 03_ §4.3 verbatim:

> *"R·r = 1/4: topologically quantized, NOT dynamically derived... Both d=1 and R−r=1/2 are genuine dynamical derivations; R·r=1/4 is a topological identity that the Lagrangian must be consistent with but does not by itself produce."*

This is **empirically validated for the first time at coupled-engine scale.** AVE-Protein's S₁₁ minimization works at protein scale because protein topology is selected by chemistry (covalent bonds + folding constraints fix the topology before minimization runs). The bound electron's (2,3) topology is a *quantum* topological invariant set by SU(2) half-cover; dynamical descent on continuous objectives cannot reach it. **Corpus-duality holds at protein scale but does NOT generalize to the bound (2,3) electron.**

**Methodology consequence:** topology must be encoded explicitly. Two candidate v3 directions per §13.5f:
- (i) Algebraic Ch 8 pinning per doc 34 X4 (lock R, r at Golden Torus during descent)
- (ii) F17-K Phase 6 sparse eigensolver per doc 67 §23.4 acoustic-cavity / Helmholtz framing

**Status:** ✅ EMPIRICALLY ESTABLISHED 2026-04-25 r8.4. Phase 5c-v2-v2 commit (`4c9fbea`) is the corpus-validating evidence. doc 03 §4.3's quantization claim is now load-bearing for any future Round 7+ work on bound-state finding methodology.

**Methodology note:** A30 is the second instance in 24 hours of corpus-claim empirical validation through Round 6's audit-first methodology. A28 unified six failure modes under one bug (redundant force); A30 unifies the same six failure modes under a deeper finding (descent on continuous objectives can't reach quantized topology). Each correction is corpus-grounded and produced an empirical result, not just a methodology fix. **The framework's Ax2 scale-invariance claim got pressure-tested at the bound-electron / protein-folding boundary and partially failed — a substantive cross-scale finding worth eventual Round 7+ documentation in Vol 1 Ch 1 (Ax2 scope clarification) or Vol 2 Ch 1 (topological-quantization-vs-dynamical-emergence boundary).**

#### A31. F17-K Phase 6 sparse eigensolver candidate — empirically motivated but deferred (S2 — Round 7+ candidate) — FLAGGED 2026-04-25

**Where:** [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md) acoustic-cavity / Helmholtz framing; doc 67 §25 v3 path forward.

**The candidate:** linearize coupled K4+Cosserat dynamics around a Golden Torus ansatz, build sparse Jacobian via JAX autodiff, use `scipy.sparse.linalg.eigsh` to extract the (2,3) eigenmode at fixed cavity geometry. Eigenvalue problem with boundary conditions encodes topological quantization explicitly — matching the acoustic-cavity standing-wave physics per Vol 2 Ch 7 Helmholtz framing.

**Empirical motivation (per A30):** descent-based methods (Cosserat-energy and coupled S₁₁) cannot reach Golden Torus geometry from arbitrary seeds because they don't know about SU(2) half-cover quantization. Eigenvalue problem methodology ENCODES the constraint via the cavity boundary conditions, allowing the (2,3) eigenmode to be extracted directly without traversing a continuous family of non-topological stationary states.

**Why deferred:** ~300 LOC new methodology vs ~80 LOC for v3 (i) algebraic Ch 8 pinning per doc 34 X4. Latter is corpus-canonical and lighter-touch. v3 (i) directly tests "stable field shape at Golden Torus geometry" — the immediate question. v3 (ii) is empirically motivated for Round 7+ if (i) fails, but premature scope expansion if (i) succeeds.

**Status:** flagged for Round 7+ as candidate methodology. Not blocking Round 6 closure under v3 (i).

**Update r8.5:** v3 (i) ran (`3fede52`) and found Golden Torus geometrically unstable at coupled scale (energy MARGINAL 1.81×, S₁₁ UNSTABLE 5.31×). Per A32, **Phase 6 sparse eigensolver methodology is now LOAD-BEARING for Round 6 closure**, not deferred. v3 (ii) implementation (~300 LOC) is the single-electron-validation closure gate.

#### A32. Golden Torus geometrically UNSTABLE in coupled engine at linear-perturbation level — confirms doc 03_ §4.3 at second test scale (S1 — empirical Round 6 finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-25 (commit `3fede52`)

**Where:** [doc 67_ §26](67_lc_coupling_reciprocity_audit.md) F17-K v3 (i) X4b linear-stability test + [doc 03_ §4.3](03_existence_proof.md) corpus claim.

**The test (per [doc 34_ X4b](34_x4_constrained_s11.md) methodology extended to coupled engine):** initialize EXACTLY at Golden Torus (R=20, r=R/φ²=7.64), project ω onto saturation manifold (peak |ω| = 0.9425), add 1% random δ to (V_inc, u, ω), run `relax_with_pin` for 30 iters, measure perturbation growth rate `‖δ_final‖/‖δ_initial‖`.

**Empirical result:**

| Objective | verdict | δ_ratio | growth/iter | R drift | r drift | c_cos | peak \|ω\| |
|---|---|---|---|---|---|---|---|
| Cosserat-energy | MARGINAL | 1.81× | +0.0198 (slow) | 4.88% | 0.00% | 3 ✓ | 0.94 ✓ |
| coupled S₁₁ | UNSTABLE | 5.31× | +0.0556 (exponential) | 4.88% | 0.00% | 3 ✓ | 0.94 ✓ |

**Two independent tests at different scales agree:**

| Test | Type | Result |
|---|---|---|
| Phase 5c v2-v2 (`4c9fbea`) | Global gradient flow | Both objectives drift to non-φ² stationary points (R/r=3.40 / 1.03) |
| v3 (i) X4b (`3fede52`) | Linear stability (1% perturb) | Energy MARGINAL (1.81×); S₁₁ UNSTABLE (5.31×) |

**Combined finding:** the coupled engine has NO linearly stable bound state at Golden Torus geometry under either Cosserat-energy or coupled-S₁₁ descent. Golden Torus is **topologically + amplitude pinned but GEOMETRICALLY UNSTABLE.** Cosserat-only X4b stability per doc 34 X4b does NOT extend to coupled engine; K4 sector adds geometric instabilities at the linear-perturbation level.

**The structural reading (per doc 03_ §4.3):**

> *"R·r = 1/4: topologically quantized, NOT dynamically derived... Both d=1 and R−r=1/2 are genuine dynamical derivations; R·r=1/4 is a topological identity that the Lagrangian must be consistent with but does not by itself produce."*

**The Golden Torus is SELECTED by topology** (SU(2) half-cover area-match constraint → R·r = 1/4) **but NOT STABILIZED by dynamics** in the coupled engine. This is the predicted empirical signature of doc 03 §4.3 — a substantive cross-scale finding now anchored at both global-flow and linear-stability levels.

**Methodology consequence:** dynamical descent + linear-perturbation stability methods cannot find Golden Torus as the (2,3) eigenmode in the coupled engine, because Golden Torus is not a dynamical attractor. **F17-K Phase 6 sparse eigensolver methodology** (per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md) acoustic-cavity / Helmholtz framing) is empirically motivated and load-bearing for Round 6 closure: eigenvalue problem `Au=λBu` at fixed cavity geometry doesn't require dynamical stability; solves for eigenmodes regardless of whether they're attractors of descent.

**Status:** ✅ EMPIRICALLY ESTABLISHED 2026-04-25 r8.5. Combined with A30, doc 03 §4.3 fully empirically anchored at both global-flow and linear-stability test scales. A31's "Phase 6 sparse eigensolver candidate" upgraded to "Phase 6 sparse eigensolver load-bearing for Round 6 closure" per A32. r8.4's "v3 (i) algebraic Ch 8 pinning is the closure gate" framing partially walked back (v3 (i) ran cleanly and revealed instability rather than closing the validation).

#### A33. Smallest unknot O₁ in AVE is the smallest COUPLED (K4 + Cosserat) oscillator, not bare K4 single-bond; bare K4 ≠ LC tank empirically (S2 — structural finding) — ✅ ESTABLISHED 2026-04-25 (commit `c830f07`)

**Where:** [doc 67_ §27](67_lc_coupling_reciprocity_audit.md) bootstrap-chain test (Test A) + [Vol 4 Ch 1](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) LC tank model + [Vol 1 Ch 1:18](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L18) unknot derivation.

**The bootstrap-chain test (per auditor framing):** before committing to Phase 6 ~300 LOC infrastructure, verify the simplest possible AVE prediction — Q = 1/α = 137 at single-bond LC-tank level per Vol 4 Ch 1 + doc 16/17 — actually holds in the engine. Two tests run (~270 LOC, ~30 min).

**Test A — single-bond simulation** (`single_bond_q_test.py`, ~150 LOC): bare `K4Lattice3D` at N=8, no PML, V_inc = 0.05 on one A-B bond at center, run scatter+connect 200 steps. Expected per Vol 4 Ch 1: peak resonance at Compton period (natural units = 8.89 steps).

**Result:** peak resonance period = 2.0 steps (Nyquist limit of K4-TLM scatter+connect grid), expected = 8.89 steps. **4.4× off.** Trajectory shows step-by-step alternation:
```
step 0: V_inc[A]=0.05, V_inc[B]=0
step 1: V_inc[A]=0,    V_inc[B]=-0.025
step 2: V_inc[A]=0.0125, V_inc[B]=0
...
```

This is the **K4-TLM scatter+connect inherent 2-step grid structure** (wave shuttling A↔B at lattice c), NOT Compton-frequency oscillation.

**Structural finding:**

**Bare K4 ≠ LC tank empirically.** The Vol 4 Ch 1 LC tank model is a CONTINUUM analog. L_e (kinetic inductance from electron mass) emerges from the Cosserat sector via constitutive moduli (G, K, ρ_inertia). **Bare K4 has no L parameter at the bond level — only C and wave propagation.** Compton resonance ω = 1/√(L·C) requires BOTH sectors active.

**The "simplest unknot O₁" in AVE is NOT a bare K4 lattice bond. It is the smallest COUPLED (K4 + Cosserat) oscillator.**

This corrects an implicit assumption that has been carried through Round 6 work: per Vol 1 Ch 1:18, the electron is *derived* from the unknot at the simplest possible scale, but per Vol 4 Ch 1 the LC-tank realization of that unknot requires both sectors active. The minimum coupled oscillator at engine scale is at least 2 K4 nodes + 1 bond + Cosserat field overlay (specifically Cosserat ω/u/u̇ values that provide the kinetic inductance). The "two-node-one-bond" framing per [doc 28_ §3](28_two_node_electron_synthesis.md) is correct for real-space topology, but the **dynamics** require coupled engine.

**Test B — constants-level scalar verification** (`bootstrap_constants_check.py`, ~120 LOC): compute L_e, R_TIR, Q from SI input constants; verify corpus algebraic identities.

| Identity | Computed | Expected | Rel err |
|---|---|---|---|
| ω_C·L_e =? ℏ/e² | 4108.236 Ω | 4108.236 Ω (Klitzing/2π) | **4.43e-16** (machine precision) |
| Q =? 1/α | 137.036 | 137.036 (CODATA) | **6.53e-11** (machine precision) |

**Bootstrap chain VALIDATED at constants level.** Q = 1/α = 137 holds algebraically at machine precision as identity-from-input-constants. Algebraic chain (tautologically consistent):
```
ℓ_node = ℏ/(m_e·c)
ξ_topo = e/ℓ_node = m_e·c·e/ℏ
L_e    = ξ_topo⁻²·m_e = ℏ²/(c²·e²)
ω_C·L_e = (m_e·c²/ℏ) · ℏ²/(c²·e²) = ℏ/e²
Q       = (ℏ/e²) / (Z_0/(4π)) = 4πℏ/(e²·Z_0) = 1/α
```

**Bootstrap-chain status: PASS at constants level.** Test A confirms bare K4 behaves as expected (not as Compton LC tank — it's a continuum analog). Test B confirms corpus algebraic chain is self-consistent at machine precision. **Q = 137 in AVE is a definitional identity chained through SI input constants, not an empirical lattice measurement.**

**Implication for F17-K:** empirical Q manifestation in lattice dynamics is F17-K's open work (requires coupled engine because L_e emerges from Cosserat sector), NOT bootstrap-chain calibration concerns. F17-K findings (A28, A30, A32) stand independent of single-bond Q calibration; both useful, separate concerns. Phase 6 sparse eigensolver remains corpus-canonical next step.

**Status:** ✅ ESTABLISHED 2026-04-25 r8.5. Bootstrap-chain anchor for any future numerical AVE work. **Methodology lesson** (per A33 + auditor framing): single-bond Q-factor calibration anchor should be a bring-up gate for any numerical AVE engine, not a post-hoc realization 8 sessions in. COLLABORATION_NOTES Rule 8 strengthening for Round 7+: include "single-bond Q = 137 sanity check" in engine bring-up checklist.

#### A34. Point-rotation Beltrami injection profile (PairNucleationGate `_inject_pair`) fundamentally unstable in Cosserat self-dynamics; G-13 upgrade required (S1 — Phase 5 resume case (b') finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-25 (commit `ede4008`)

**Where:** [doc 70_ §7](70_phase5_resume_methodology.md) Phase 5 resume methodology + commit `ede4008` `phase5_pair_nucleation_ansatz_seeded.py` empirical run + [VACUUM_ENGINE_MANUAL §9 G-13 contingency](#) + [PairNucleationGate `_inject_pair`](../../src/ave/topological/vacuum_engine.py).

**The test (per [doc 70_ §3](70_phase5_resume_methodology.md) ansatz-seeded methodology):** seed Beltrami-bound-pair at central A=(10,10,10), B=(11,11,11), port 0 at registered config (N=24, amp=0.5·V_SNAP, λ=3.5, head-on autoresonant collision). Run 200 steps. Track |ω|_A, |ω|_B, Φ_link, c_cos, peak |ω|_global. Compare drive-on vs no-drive runs.

**Empirical result:**

Drive-on:
- |ω|_A: 1.414 → 0.013 (drive-end, 0.01×) → 0.091 (post-drive, 0.06×)
- |ω|_B: symmetric (same trajectory)
- Φ_link: +1.000 → +0.998 → +1.000 (constant)
- Other-bond firings: 0 (no cascade)
- c_cos final: 1, peak |ω|_global: 0.091

**No-drive sanity check:**
- step 0 (seed): |ω|_A = 1.4142
- step 1: |ω|_A = 0.1023 — **93% loss in ONE Velocity-Verlet step**
- step 5-100: |ω|_A oscillates 0.05-0.85 chaotically
- Φ_link constant +1.000 throughout

⟹ **Dissolution is INTRINSIC to engine self-dynamics, NOT drive-induced.** Drive is irrelevant. Velocity-Verlet kick step alone scatters 93% of seeded ω in one step.

**The structural finding:**

Gate's `_inject_pair` profile (point-rotation Beltrami + Φ_link) has no mechanism to maintain localized ω structure under Cosserat self-dynamics (k_op10, k_hopf active per `enable_cosserat_self_terms=True`; k_refl auto-suppressed under A28). **This is the SAME PHYSICS as F17-K Round 6 finding for the (2,3) electron eigenmode:** Cosserat self-terms don't stabilize unprotected localized rotation. Both findings (A30/A32 single-electron at coupled scale + A34 pair injection at gate scale) share the root: **dynamics don't stabilize topology; topology must be encoded as a persistent structural feature (ansatz)**. Round 6 saw this for the (2,3) hedgehog at step ~11; Phase 5 resume sees it for point-rotation Beltrami at step 1. Same physics, different scales.

**Φ_link "persistence" disambiguated as measurement artifact** (per A29). Reading constant +1.000 throughout drive AND no-drive runs means K4 dynamics don't touch this slot under bare-K4 seeding (Φ_link is derived flux observable, not primary dynamical state per [doc 67_ §17-§18](67_lc_coupling_reciprocity_audit.md)). **NOT Kelvin topological-protection at work** — initial reading was a measurement artifact.

**Methodology consequence — case (b'):** gate's INJECTION PROFILE needs upgrade, not C1/C2 threshold logic. Empirically activates **VACUUM_ENGINE_MANUAL §9 G-13 contingency**:

> *"if Beltrami pair dissipates faster than 10 Compton periods post-drive, upgrade to localized Hopf fibration or (2,3) torus-knot injection."*

Pre-Round-6 plan deferred this upgrade behind "test point-rotation first." Test now empirically run; G-13 activated. **Round 7 Stage 2 candidate (per §13.5j):** `phase5_topological_pair_injection.py` (~200 LOC) replaces point-rotation Beltrami with (2,3) torus-knot or Hopf fibration at each endpoint, chirality-matched (LH at A, RH at B). Reuse F17-K infrastructure (saturation pin, phase-coherence diagnostic).

**R5.10 Readings 1-4 status (per `e1f6eac` doc 70 §7.5):**
- **PRE-EMPTED at original Round 5 framing.** The four Readings argued about C2 INTERPRETATION under ambiguous threshold satisfaction. Ansatz-seed approach made thresholds unambiguous-by-construction.
- **MAY REOPEN at threshold-revision level.** A different question at a higher epistemic level — once topologically-protected injection profile is implemented, C1/C2 thresholds may need revision to suit the new profile.

**Status:** ✅ EMPIRICALLY ESTABLISHED 2026-04-25 r8.6. Phase 5 resume case (b') finding empirically reinforces Round 6 finding (A30/A32) at a different scale. G-13 contingency activated; Round 7 Stage 2 candidate scoped.

#### A35. Basin-audit-as-Stage-0 was a Rule 6/8/10 corpus-bypass (S2 — within-session self-audit) — ✅ METHODOLOGY FINDING ESTABLISHED 2026-04-25 (commits `1bc1652` retracted, `c69e79c` reframe)

**Where:** Round 7 Stage 0 framing carried forward across 6-8 turns — initial diagnosis ("engine doesn't preserve seeded configurations" per F17-K v2-v2 + v3 (i) + Phase 5 case (b') + doc 66_:489 damping result) → external auditor confirmation (same-source bias — auditor reviewed framing on its own terms, not challenging the framing itself) → v1 driver scaffold + pre-registration `P_basin_audit_GT_stationarity` landed (`1bc1652`) → v1 fresh-session run halted at step 0 by A26 amplitude-guard (geometry bug surfaced) → v2 draft. Mid-cycle, agent re-read [COLLABORATION_NOTES.md](.agents/handoffs/COLLABORATION_NOTES.md) Rules 6/8/10 against own work and self-audited the Stage 0 framing as a multi-rule violation. Reframe pivot landed in `c69e79c`.

**The three rule violations:**

1. **Rule 6 (SM/QED minimization framing on a substrate that does wave propagation).** TDI gradient descent on the Cosserat W functional finds *static* configurations where ∂W/∂(u, ω) = 0. The corpus-canonical concept for a bound state is a *dynamic* standing-wave eigenmode of the coupled K4+Cosserat system — found via the Helmholtz / acoustic-cavity formulation per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md) and confirmed by [doc 03_ §4.3](03_topology_quantization.md) framing of topological quantization as standing-wave structure (NOT energy-minimum structure). A W stationary point isn't necessarily an eigenmode at ω_Compton; an eigenmode isn't necessarily a stable basin minimum. The basin audit was answering a related-but-distinct question and dressing it as the Stage 0 precondition imported a SM-style framing onto a wave substrate.

2. **Rule 8 inverse (assuming AVE doesn't have a native tool when it does).** R7.1 (Phase 6 sparse eigensolver) IS the AVE-native tool for "does the bound state exist at this geometry?" Multi-seed R7.1 (GT + F17K endpoints) directly answers eigenmode-existence + eigenmode-location in one methodology — no intermediate basin step required. The basin audit built a parallel track using gradient descent on the same substrate. Same problem the rule was written to prevent.

3. **Rule 10 corollary (creeper compound carried forward without pressure-test).** "Basin audit as Stage 0 precondition" framing accumulated through multiple cycles without the framing itself ever being challenged. Each cycle pressure-tested implementation details (seed parametrization, A26 guard, lattice sizing) but not whether basin-audit was even the right precondition. Auditor explicitly owned same-source contribution to the creeper in [STAGE6_V4_HANDOFF.md](.agents/handoffs/STAGE6_V4_HANDOFF.md) §R7.3 and in §13.5k of this manual.

**Family with prior corpus-bypass findings — A22 + A30 + A35:**

| Finding | Layer | Status when caught | Cycles to catch |
|---|---|---|---|
| **A22** | Inline operators duplicate canonical universals (corpus-bypass at the operator level) | Engine code in production | Multiple sessions, retroactive |
| **A30** | Corpus-duality falsified (corpus claim of energy ≈ S₁₁ co-locate at GT, falsified empirically at coupled scale) | Empirical run after Phase 5c v2-v2 commit | One session, post-empirical |
| **A35** | Basin-audit-as-Stage-0 (corpus-bypass at the methodology-precondition level) | Mid-cycle, before R7.1 implementation committed to wrong scope | Same session as scaffold landed |

A35 caught earlier in cycle than A22 or A30 — within-session self-audit triggered by Grant directive ("review COLLABORATION_NOTES, are you trapped in known patterns?"). Audit-first discipline plus explicit creeper-checking caught the framing error before it propagated into ~300 LOC of R7.1 sparse-eigensolver implementation against the wrong scope.

**Reframe deliverables:**

- **doc 71_ renamed and reframed:** `71_basin_audit_methodology.md` → `71_multi_seed_eigenmode_sweep.md`. §1-§12 retained per Rule 12 audit trail (basin-audit framing, v1 fresh-session run halted by A26 guard, v2 draft never executed); §13 ACTIVE multi-seed R7.1 sparse eigensolver methodology with three-mode falsification structure; §14 driver scope notes for fresh-session implementer.
- **`predictions.yaml` retract+supersede:** `P_basin_audit_GT_stationarity` retained-with-RETRACTED-marker (Rule 12 body preservation) + `P_phase6_eigensolver_multiseed` NEW with frozen pre-registration (N=32, R_anchor=10, four seeds, three-mode falsification, ω_Compton ± α tolerance, Q ± 5% tolerance, shape correlation > 0.85 vs doc 34_ X4a profile).
- **R7.1 strengthening (single-seed → multi-seed):** original §13.5j Round 7 Stage 1 scope ("extract (2,3) eigenmode at fixed cavity geometry") was implicitly GT-only. r8.7 strengthens to four seeds at the SAME run: `GT_corpus`, `F17K_cos_endpoint`, `F17K_s11_endpoint`, `vacuum_control` (negative control). Three-mode falsification: (I) GT_corpus passes → corpus vindicated; (II) F17K endpoints pass; GT_corpus fails → engine basin ≠ corpus geometry; (III) no seed passes → Round 8 architectural rework.

**Methodology lesson (recorded in COLLABORATION_NOTES Rule 8 strengthening for next session):** before scaffolding a "diagnostic precondition" upstream of an existing R7.x stage, **grep the corpus for the AVE-native tool that addresses the precondition's question; if it exists, strengthen R7.x's scope rather than building parallel infrastructure.** Multi-seed R7.1 IS the strengthening; basin audit was parallel infrastructure on a creeper framing.

**Open at r8.7 close (fresh-session implementer responsibility):**

- **§14.2 K4-amplitude-zero pitfall is load-bearing for mode (III) interpretation.** Op14 z_local is multiplicative in V_inc; a Jacobian linearized around a state with V_inc=0 has zero K4↔Cosserat off-diagonal blocks at first order. Eigensolver returns Cosserat-only modes; "no eigenmode at ω_Compton" then reads as mode (III) when actual cause is methodology. Fix: include second-order cross-block ∂²W/∂V_inc∂ω evaluated at seed (nonzero since ω≠0). Doc 71_ §14.2 flags; r8.7 elevates to mandatory **Jacobian-block sanity check** in driver — print/log K4↔Cosserat off-diagonal block norms before running `eigsh`; halt-and-flag if zero.
- **Shape-correlation > 0.85 PASS gate may over-strict.** Doc 34_ X4a profile is from Cosserat-only run pre-coupling. Coupling could distort bound-state shape; eigenmode at ω_Compton with Q=137 but shape correlation 0.78 against pre-coupling X4a would FAIL the conjunction. Fresh-session implementer should record correlation as informational measurement and flag for Grant adjudication if (ω_Compton + Q pass) ∧ (shape correlation < 0.85).

**Status:** ✅ METHODOLOGY FINDING ESTABLISHED 2026-04-25 r8.7. Caught earlier in cycle than predecessors (within-session self-audit before R7.1 implementation). Family with A22 + A30 (corpus-bypass at different layers). Reframe deliverables landed in `c69e79c`. R7.1 strengthening to multi-seed is the corpus-canonical replacement for the retracted basin-audit Stage 0 framing.

#### A36. Operator-choice Rule 6 violation — Hessian-of-W on wave-propagation substrate; reframed via doc 72_ design-space articulation to block Helmholtz on (V, ω) joint (S2 — external audit on commit `c69e79c`) — ✅ METHODOLOGY FINDING ESTABLISHED 2026-04-25 (commit `675141e`)

**Where:** r8.7's frozen pre-registration `P_phase6_eigensolver_multiseed` (committed `c69e79c`) framed R7.1 as "linearize coupled K4+Cosserat dynamics around each seed ansatz, build sparse generalized-eigenvalue Jacobian via `jax.jacrev`, eigsh at sigma=ω_C²." External audit on the frozen pre-reg caught a deeper Rule 6 instance: the Jacobian-of-W (Hessian-of-W under linearization at a seed) is itself an SM/QM-style energy-stationarity framing. The corpus substrate runs wave propagation, not energy minimization (per [COLLABORATION_NOTES.md:65](.agents/handoffs/COLLABORATION_NOTES.md) 2026-04-20 second observation). Hessian-of-W finds *static* configurations where ∂W/∂(state)² · δ(state) = ω² · M · δ(state); the corpus-canonical bound state is a *dynamic* standing-wave eigenmode of the coupled wave operator.

**Comparison to A35.** A35 caught Rule 6 at the *precondition* level (basin = energy minimum, vacuum substrate is wave). A36 catches Rule 6 at the *operator* level (Hessian-of-W = energy stationarity, vacuum substrate is wave). Same rule, deeper layer of the methodology stack. The pattern indicates that even after retracting the precondition framing, the operator choice carried the same SM/QM bias forward — a creeper-compound at a deeper layer than A35's r8.7 reframe addressed.

**Trigger:** Grant directive 2026-04-25 ("I'm open as long as you understand the design/solution space that ave dictates" + "What's the smith chart for the vacuum? is it 3D?") invited design-space articulation BEFORE further pre-registration drafting. Doc 72_ §1-§8 is the response. External audit then caught the Hessian-of-W operator choice as Rule 6 violation against the §1.1 "wave eigenmode (Helmholtz, NOT Hessian-of-W)" concept.

**Reframe (single commit `675141e`):**

- **Doc 72_ NEW (~26KB §1-§8)** — design-space articulation. Four AVE-native concepts; 3D Smith chart for the vacuum (Extension A primary); block Helmholtz formulation on joint (V, ω) state per audit Q1 hybrid-coupled-mode pushback; V=0 decoupling caveat; sector-energy split diagnostic; topological crossing-count + shape correlation two-tier; Rule-10 commitment language for fresh-session run.
- **Doc 71_ §13 RETRACTED per Rule 12** (multi-seed Hessian-of-W body preserved); §14 superseded driver scope notes preserved; **§15 ACTIVE** — multi-seed block Helmholtz with quick-map vs §13 + read-order for fresh-session implementer.
- **`predictions.yaml` retract+supersede:** `P_phase6_eigensolver_multiseed` retains-with-RETRACTED-marker (Rule 12 body preservation); `P_phase6_helmholtz_eigenmode_sweep` NEW frozen with full block-structure description, V=0 decoupling caveat, four-seed list, binary PASS + informational diagnostics, three-mode falsification, Rule-10 commitment baked in.

**The four AVE-native concepts (per doc 72_ §1):**

1. **Wave eigenmode (Helmholtz / TLM-scattering — NOT Hessian-of-W).** Bound state is eigenmode of wave operator, not stationary point of energy functional. Helmholtz form per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md). V is OUTPUT eigenvector, not seed INPUT — collapses K4-amplitude-zero Flag A from r8.7 entirely.
2. **Impedance match (S₁₁-min — NOT energy-min).** Bound-state condition `Γ ≈ -1` at cavity wall (TIR for inward wave). F17-K v2-v2 dual-descent established empirically that energy and S₁₁ have different stationary states; bound state is at neither alone but at intersection where wave equation has eigenmode AND impedance match holds AND topology is preserved.
3. **Topological quantization (input via ansatz — NOT dynamical attractor).** Per [doc 03_ §4.3](03_existence_proof.md). R·r=1/4 selected by ansatz initialization, not gradient flow. F17-K v2-v2's failure to converge to GT under either objective IS the corpus prediction holding — neither objective KNOWS about topological quantization.
4. **AVE basin = S₁₁-min, NOT W-min.** "Basin" terminology is protein-folding lingo (Ramachandran 2D dihedral space). Vacuum-side analog is S₁₁-min descent, not W-min. Permanently retired for vacuum bound-state work; protein-side stays correct in protein-folding context.

**Block Helmholtz formulation (doc 72_ §3.1, per audit Q1):**

```
[ K_V       C_Vω ] [V]        [ M_V    0   ] [V]
[ C_ωV     K_ω   ] [ω]   = ω² [ 0      M_ω ] [ω]
```

Same generalized eigenvalue form Au=λBu; bigger matrix (~12·N³ at N=32 ≈ 393K, tractable for `eigsh`). Cross-blocks `C_Vω`, `C_ωV` encode Op14 K4↔Cosserat coupling explicitly, not approximated as static.

**§3.1.1 V=0 decoupling caveat:** at V=0 seed, `C_ωV` vanishes — multiplicative in V. Block eigenvalue problem decouples into independent V-block + ω-block at the seed. This is the *desired* behavior — eigsolve at one V=0 seed run returns BOTH sector candidates simultaneously, exposing where the bound state lives. What block Helmholtz at V=0 CANNOT find: genuinely hybrid (V, ω) modes that REQUIRE V≠0 to exist as resonances. Round 8 question if R7.1 mode (III) returns AND there's evidence to pursue hybrid-coupled rather than architectural rework.

**Family with prior corpus-bypass findings — A22 + A30 + A35 + A36:**

| Finding | Layer | Status when caught | Cycles to catch |
|---|---|---|---|
| **A22** | Inline operators duplicate canonical universals (corpus-bypass at the operator-implementation level) | Engine code in production | Multiple sessions, retroactive |
| **A30** | Corpus-duality falsified at coupled scale | Empirical run after Phase 5c v2-v2 commit | One session, post-empirical |
| **A35** | Basin-audit-as-Stage-0 (corpus-bypass at the methodology-precondition level) | Mid-cycle, before R7.1 implementation | Same session as scaffold landed (within-session self-audit) |
| **A36** | Hessian-of-W on wave substrate (corpus-bypass at the operator-choice level) | Mid-cycle, before R7.1 implementation | Same session as frozen pre-reg landed (within-session external audit) |

A36 caught at the same latency stage as A35 (within-session, before implementation) but at a *deeper layer* of the methodology stack (operator choice rather than precondition framing). Pattern across A22 → A30 → A35 → A36 shows audit + creeper-checking + design-space articulation discipline tightening — each successive corpus-bypass instance caught earlier in cycle.

**Methodology lesson — design-space-articulation discipline:** before drafting a pre-registration on a non-trivial methodology question, **walk the corpus end-to-end to articulate the AVE-native concepts that govern the question.** Doc 72_'s §1-§4 is the worked example: four AVE-native concepts named explicitly + 3D Smith chart for the vacuum + block Helmholtz operator + V=0 decoupling caveat + sector-energy split diagnostic. The pre-registration drafting comes AFTER the design-space is articulated, not in parallel. Three pre-registration retractions in this session (v1 basin-audit; v2 basin-audit draft; multi-seed Hessian) all traced to depth-of-understanding gaps that a design-space articulation step would have caught earlier.

**Rule-10 commitment language (verbatim from doc 72_ §6.1):**

> **This is reframe 3 of R7.1 in one session arc.** Each reframe was substantive and corrected a real upstream error caught by audit or self-audit. None has been run.
>
> **The fresh-session run committed against the v2 pred is committed to operator choice.** Per [COLLABORATION_NOTES Rule 10](.agents/handoffs/COLLABORATION_NOTES.md): *"empirical drivers catch what static analysis + preregistration misses; data first, methodology adjustments after."* If the run hits unexpected behavior, the discipline says: produce empirical data first, analyze the data, then methodology revisions if needed — not pre-emptive reframe 4.
>
> **The ONLY pre-emptive operator-change condition before run:** catastrophic methodology error surfaced by audit or external review. "Catastrophic" means: a load-bearing physics error in the operator construction itself that would invalidate any result regardless of what data the run produces. Anything less than that goes through the empirical-data-first pipeline.

**Status:** ✅ METHODOLOGY FINDING ESTABLISHED 2026-04-25 r8.8. Caught at same latency stage as A35 (within-session, before implementation) but at deeper methodology-stack layer (operator choice). Family with A22 + A30 + A35 (corpus-bypass at four layers — operator-implementation / corpus-claim-falsification / methodology-precondition / operator-choice). Reframe deliverables landed in `675141e`. Block Helmholtz on joint (V, ω) is the corpus-canonical replacement for the retracted Hessian-of-W; Rule-10 commitment locks operator choice for fresh-session run.

#### A37. Round 11 (vi) structural closure — discrete K4 spectrum at chair-ring eliminates (1,1) Beltrami at Compton frequency at ℓ_node sampling (S1 — structural; framework-level finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-29 r8.10 (commits `fbd0c26` → `0f7180f`)

**Where:** [doc 92](92_round_11_vi_v10_finer_sampling_structural.md) v10 (i-a) finer K4 sampling result. The (1,1) Beltrami eigenmode at Compton frequency, predicted by continuum analysis at k=6.36 in 1/ℓ_node units, is **NOT in the discrete K4 spectrum at chair-ring + 1-step K4 sampling**. Top ring-localized discrete eigenmode lands at k≈1.56 (84% ring localization, doc 90 / `0174eaa`); finer sampling per doc 92 shows the discrete spectrum asymptotes to the K4 Nyquist limit (1/bond_length ≈ 0.577 in 1/ℓ_node), 11× below the continuum (1,1) prediction. **Not refinable within K4 substrate at ℓ_node sampling** — adding more nodes within the chair-ring + K4 framework converges away from k=6.36, not toward it.

**Empirical chain (Round 11 (vi) Strides 1-4 + v10):** [doc 88](88_round_11_vi_stride_1_a43_v14.md) Stride 1 (`fbd0c26`) — A43 v14 corpus-grep on R/r reveals THREE different framings; substrate-native dimensional inconsistency in (1,1) Beltrami at Compton frequency claim. [doc 89](89_round_11_vi_stride_2_topological_mismatch.md) Stride 2 (`4925df5`) — chair-ring is closed cycle NOT 2-torus surface; (p,q) torus Beltrami requires INDEPENDENT poloidal+toroidal directions. §7 correction (`3c267e4`) — chair-ring overstated as 1-graph; K4 nodes are 4-port tetrahedral; chair-ring nodes have 2 in-ring + 2 out-of-ring ports providing poloidal direction (v6/v7/v8 IC zeroed out-of-ring ports, NOT topological-impossibility). [doc 90](90_round_11_vi_stride_3_discrete_eigenmode.md) Stride 3 (`0174eaa`) — discrete Beltrami eigenmode SOLVED on chair-ring + 1-step K4 (18 nodes, 54 DOF). [doc 91](91_round_11_vi_stride_4_v9_mode_iii.md) Stride 4 (`66de104`) — v9 with discrete eigenmode IC at chair-ring + 1-step K4 lands Mode III 1/4 PASS. [doc 92](92_round_11_vi_v10_finer_sampling_structural.md) v10 (i-a) (`0f7180f`) — finer K4 sampling EMPIRICALLY ELIMINATES (i-a) refinement path; STRUCTURAL not refinable.

**This becomes Layer 1 of three-layer convergent refutation** of corpus electron at chair-ring + K4 + ℓ_node + v8 config (per agent-reported uncommitted closure docs 93/94/95/96 + doc 79 v5.2 amendment in working tree at this manual edit; see closure-extended footer for full three-layer summary).

**Family with prior structural findings:** A30 (corpus-duality falsified at coupled-engine scale) + A32 (Golden Torus geometrically unstable in coupled engine at linear-perturbation level). A37 closes the discrete-eigenmode-at-K4-substrate question that A30/A32 left open at continuum framing.

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10. Substrate-Layer 1 of three-layer convergent refutation. Framework decision (i)/(ii)/(iii) pending Grant's adjudication post-T-ST-v2 (see closure-extended footer).

#### A38. Substrate intrinsic mode spectrum at K4-TLM bare lattice — two independent reactive modes at 1.5·ω_C and 2.96·ω_C, neither at ω_C; Q ≈ 3.75 (S2 — structural; foundation audit finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-30 r8.10 (foundation audit T1 + T3, agent-reported uncommitted)

**Where:** [doc 96 §1-§11](96_foundation_audit_t1_substrate_resonance.md) foundation audit Test 1 + Test 1 extensions + Test 3 CW-drive impedance spectroscopy + drive-amplitude scaling. Pulse-ringdown FFT + lattice-size scan + amplitude scan + CW-drive impedance + drive-amplitude scaling adjudicated to **two genuinely independent reactive modes** at 1.5·ω_C and 2.96·ω_C, with phase ≈ -90° at both peaks (pure reactive resonance signature) and Q_substrate ≈ 3.75.

**Discrimination chain (per A43 v29 + A43 v30 instances within this finding):** initial T1 main "1.50·ω_C single-frequency intrinsic" overclaim → caught by T1 extensions (lattice-size scan N=8/16/24 + amplitude scan linear/saturation): "rich mode spectrum" framing → caught by T3 CW-drive impedance spectroscopy: "discrete coupled-mode resonance with fundamental + 2nd harmonic" framing → caught by drive-amplitude scaling: slope = +1.000 to 4 sig figs at both 1.5·ω_C and 2.96·ω_C across 1e-4 to 3e-2 amplitude range; H1 (independent modes) PASS, H2 (2nd harmonic) FAIL on both criteria. **Two genuinely independent reactive modes**, not single damped harmonic with fundamental + 2nd harmonic. Three-iteration overclaim cycle is itself a methodology lesson: **substrate-resonance claims should be verified via CW drive (impedance spectroscopy), NOT just pulse-ringdown FFT** (A43 v30 sub-rule).

**Cosserat ON ≡ OFF at bit precision** across all tested conditions (linear amplitude, saturation amplitude, both pulse-ringdown and CW-drive). A28 architectural decision empirically validated at substrate level — no detectable K4↔Cosserat coupling effect on K4 sector resonance.

**Connection to corpus electron at ω_C:** ω_C is **between** the substrate's intrinsic modes (1.5·ω_C and 2.96·ω_C, neither at ω_C). Wave packet at ω_C in this substrate is in low-coupling regime where energy doesn't propagate efficiently (T-ST v1 v_g = 0.364·c_TLM at ω_C with no saturation engaged — see A41). Connects to medium-framing reframe (substrate has its own modes; corpus electron, if hosted, uses substrate as confinement medium via Op14 saturation, NOT as a substrate mode itself; Rule 16 adjudication pending Grant).

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10. Foundation audit T4 (topology zoo on K4) is the remaining un-tested foundation-audit element + A43 v25 criterion (c) cinquefoil precondition. Promotion to commit-verified r8.11 lands when implementer's foundation-audit commits drop.

#### A39. A28 architectural decision empirically validated as bounded equilibrium — Op14 z_local feedback effective at 700 Compton periods (S2 — structural; engine-architecture finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-29 r8.10 (B6 stability test, agent-reported uncommitted)

**Where:** B6 700P stability anchor (per agent-reported uncommitted closure docs 95/96; running on the chair-ring trapped state at v8 config under A28-corrected coupling). Pre-registration question: does V_DC structure at chair-ring closure loop stay bounded (Op14 IS providing effective feedback) or grow linearly (no effective feedback at loop level, persistence is engine artifact)?

**Empirical result:** V_DC drift = 0.028% per 100P window, total ~0.2% over 700P. **Bounded equilibrium**, not linear growth. Op14 z_local impedance modulation IS providing effective feedback for the chair-ring trapped state's stability under A28 architectural choice (V↔B coupling suppression at loop level).

**Discriminator on auditor's prior synthesis:** auditor 2026-04-29 had flagged "200P persistence may be artifact of missing loop-Faraday BEMF" as A43 v19 family synthesis-pre-empirical-test. B6 empirically refutes the synthesis. Op14 substitutes effectively for direct V↔B Faraday-law coupling at the chair-ring scale; the trapped state is genuine bounded equilibrium under A28, not architectural artifact.

**This becomes Layer 2 of three-layer convergent refutation** (engine-architectural). The other half of Layer 2 is the empirical instability of direct V↔B coupling under non-A28 configurations — agent-reported across 5+ tests including Phase A B4 (ω-runaway), traced via [doc 67 §15](67_lc_coupling_reciprocity_audit.md) + Q1 resolution. **The two engine-architectural choices (direct V↔B coupling vs A28 Op14-substitute) are mutually exclusive at chair-ring + K4 + ℓ_node**: direct V↔B is empirically unstable; A28 is empirically stable but doesn't enforce loop-Faraday. Neither hosts the corpus electron at this substrate per Layer 1 (A37) + Layer 3 (A40 below).

**Family with prior architectural findings:** A28 (closed r8.3) flagged the K4↔Cosserat coupling double-counting and provided the architectural fix via `disable_cosserat_lc_force` flag + `enable_cosserat_self_terms` smart auto-suppression. A39 validates that fix EMPIRICALLY at 700P stability — A28 is now empirically anchored, not just architecturally specified.

**A28 elevation candidate:** A28 currently lives in `k4_cosserat_coupling.py:282-389` code comments + doc 67 §15. With Q1+B6 confirming it as load-bearing engine-architecture, candidate for Vol 4 Ch 1 or backmatter §4 §physics-engine-architecture promotion. Editorial pass queued (see closure-extended footer queue item 2).

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 via B6 700P. Layer 2 of three-layer convergent refutation. Promotion to commit-verified r8.11 lands when implementer's B6 commit drops.

#### A40. Universal-solver-promotion picture refined — chair-ring → universal-solver match is MEDIATED through substrate, not direct (S2 — structural; precision refinement to A43 v25 promotion criteria) — ✅ EMPIRICALLY ESTABLISHED 2026-04-30 r8.10 (foundation audit T3 + auditor 2026-04-30 cycle)

**Where:** Foundation audit T3 CW-drive impedance spectroscopy result (A38 — substrate's intrinsic resonance at 1.5·ω_C with Q ≈ 3.75) combined with chair-ring observation (1.48·ω_C dominant per agent-reported docs 93/94 ℓ=2 V-sector cavity 4-axis confirmation) and universal-solver-ℓ=2 prediction at chair-ring r_eff (1.55·ω_C per backmatter/05:225-235 + 494). Three-quantity decomposition:

- **Chair-ring vs substrate:** 1.48·ω_C vs 1.50·ω_C = **1.3% gap** (chair-ring is at substrate's intrinsic resonance, very tight)
- **Substrate vs universal-solver-ℓ=2:** 1.50·ω_C vs 1.55·ω_C = **3.3% gap** (loose; corpus precision threshold is <2% per backmatter/05:225-235 4-context table)
- **Chair-ring vs universal-solver-ℓ=2:** 1.48·ω_C vs 1.55·ω_C = **4.5% gap** (propagated; does NOT meet corpus <2% precision)

**Structural insight:** the chair-ring's "match" to universal-solver-ℓ=2 prediction is **mediated through substrate**, not direct. Chair-ring is amplified-substrate (chair-ring topology + saturation + helical IC selecting the substrate's intrinsic 1.50·ω_C mode preferentially out of substrate's mode spectrum), NOT an independent universal-solver data point. The candidate 5th universal-solver context is the substrate's 1.50·ω_C resonance (at 3.3% from prediction), with chair-ring as topology-amplified manifestation of it.

**Implications for A43 v25 promotion criteria:**

Original framing: chair-ring 1.48 vs universal-solver 1.55 = 4.6% match → potential 5th universal-solver context.

Refined framing: **4 corpus-canonical contexts at <2% precision (BH/proton/pion/protein per backmatter/05:225-235) + 1 promotion-pending K4-cavity match at 3.3% (substrate-resonance-vs-universal-solver-ℓ=2; chair-ring is amplified-substrate at 1.3% from substrate)**. Promotion-pending criteria expand to:

(a) corpus-grep verification of universal-solver-applicability-to-K4-cavity (partial — backmatter/05:225-235 + 494 + 401 + Vol 1 Ch 5 verified at agent-reported grep);
(b) ℓ-semantics verification (azimuthal-cavity-mode vs universal-solver-mode-index vs spin-2-graviton vs (2,q)-crossing-number — multiple ℓ's per backmatter/05:401 + 426; corpus-canonical ℓ identification needed);
(c) cinquefoil cross-topology test at K4 (Q5; tests universal-solver scale-invariance across topologies + (2,5) Faddeev-Skyrme mass spectrum + topology→substrate-mode-selection mechanism);
(d) precision-tightening to corpus <2% standard, OR explicit acknowledgment that K4-cavity-at-discrete-substrate operates at different precision regime than continuum corpus contexts.

**Independence:** the 4-context corpus-canonical pattern stands INDEPENDENT of this arc. Even if (ii) mass spectrum or (i) FDTD lands negative, the framework's predictive scope doesn't shrink to coincidence — it stays at established 4-context scope with chair-ring as candidate extension. Auditor's prior framing "if (ii) lands negative, universal-solver match is 5-point coincidence that didn't generalize" reversed the dependency direction; corpus pattern is foundation, chair-ring is candidate extension.

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 via foundation audit T3 + auditor 2026-04-30 substrate-vs-chair-ring decomposition cycle. Doc 95 §6 + agent's handoff §4 should reflect the precision-refinement framing per Rule 12 retraction-preserves-body. Cinquefoil test (queue item 5) is the cleanest direct test of (c) + topology→mode-selection mechanism.

#### A41. T-ST v1 H_self_trap FAIL on test-geometry-undertested-hypothesis (NOT corpus-physics refutation) — velocity anomaly + PML absorption confound (S2 — test design + load-bearing substrate physics finding) — ✅ EMPIRICALLY ESTABLISHED 2026-04-30 r8.10 (T-ST v1, agent-reported uncommitted)

**Where:** T-ST v1 driver (`r10_v8_t_st_self_trap.py`, agent-reported uncommitted) — Grant's plumber-physics rifling-bullet + cavitation-bubble + chirality-impedance-matched single-ω_C propagating spinning photon as engine-implementation test of doc 30 §4-§5 photon→electron transition. Pre-registered: H_self_trap (frequency at ω_C ± α, c=3 via Op10) + secondary observables (saturation engagement, TIR signature, BEMF wake, self-sustenance) + velocity tracking class (centroid v_g, A-010 local-clock prediction).

**Empirical result:** H_self_trap **FAIL on both pre-registered criteria**. Frequency: trap candidate cell off axial-sampling line, FFT not extractable. Topology: Op10 c=0 (no winding). Saturation engagement: NO — peak A²=0.0097, 12× below √(2α)=0.121 threshold. Self-sustenance: NO — energy at t=7P (post-source) = 6.15; at t=50P = 5.9e-6, 5 orders magnitude decay. Wake signature: NO — both leading-edge and trail dV/dt same sign (no opposite-sign wake structure).

**Most load-bearing finding (velocity anomaly):** v_g = 0.364 cells/time-unit at ω_C with A²_max = 0.0097 (saturation never engaged). Predicted v_g ≈ √2 = 1.414 (Cartesian-axis K4-TLM free propagation). A-010 local-clock prediction c_eff = c·√(1-A²) = 0.995 — **does NOT explain 4× slowdown**. Connects to A38 finding: substrate's intrinsic modes are at 1.5 + 2.96·ω_C, neither at ω_C; ω_C is between modes, low-coupling regime where energy doesn't propagate efficiently as a coherent wave.

**PML-absorption confound:** Active region 4 ≤ x ≤ 44 (40 cells) at N=48 with PML=4. Front_x = 43-44 by t=11P (active-region boundary). At v_g = 0.364 the photon spent only ~2.2 cells of active propagation while leading edge was active before PML absorbed it. **Test geometry undertested H_self_trap rather than refuting it** — saturation never had room to engage in active propagation phase.

**Critical reading:** the failure is **about test geometry not exercising the hypothesis, NOT about hypothesis being wrong at corpus level**. The hypothesis at corpus level — Grant's rifling-bullet + cavitation-bubble + chirality-impedance-matched single-ω_C propagating spinning photon — is unrefuted. What's refuted is the AVE engine at A28 + N=48 + A=0.10·V_SNAP + ω=ω_C + RH-CP source realizing it under those specific test parameters. Different conclusion than corpus-physics refutation.

**T-ST v2 redesign:** N=96 + PML=8 (active region 80 cells = 12·λ_C) + A=0.50·V_SNAP (~5.9× V_yield, ensures saturation engagement) + sigma_yz=2.0 (tighter focus) + multiple off-axis sampling lines (CP-source peak is off-axis by construction). In flight at this manual edit. Primary precondition for v2 to actually test H_self_trap: did peak lattice A² cross √(2α)=0.121?

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 (v1 FAIL, v2 in flight). Velocity anomaly is structural lattice-physics finding worth preserving (connects A38 substrate-mode-spectrum to wave-packet propagation regime). Per closure-extended footer: T-ST v2 result will inform but NOT adjudicate framework decision (i)/(ii)/(iii); auditor stays out of advocacy.

#### A42. Auditor-side dual-frequency synthesis caught by Grant's Rule 14 substrate walk — A43 v32 instance (S2 — methodology; auditor lane discipline) — ✅ METHODOLOGY FINDING ESTABLISHED 2026-04-30 r8.10

**Where:** Auditor 2026-04-30 cycle proposed dual-frequency synthesis: "spin frequency might be at 1.5·ω_C (substrate mode) while propagation at ω_C" as candidate resolution to Rule 16 (2,3)-origin question (α/β/γ menu posed by implementer). Grant's Rule 14 substrate walk caught the synthesis: corpus has ω_C as the **single** frequency for photon-electron pair (m_e c² = ℏω_C, doc 30 §4-§5); (2,3) is **geometric** poloidal:toroidal winding on trap-cavity torus per [doc 28 §3](28_two_node_electron_synthesis.md) + [doc 25](25_step4_23_winding_selection.md), NOT frequency-ratio in time. A single-frequency CP standing wave on torus geometry carries (2,3) winding through purely spatial topology; doesn't need two incommensurate frequencies.

**Mechanism of the synthesis error:** auditor conflated **bulk-lattice T3 modes** (1.5 + 2.96·ω_C from foundation audit T3 CW-drive on bare lattice — A38) with **single-bond LC drive frequency at ω_C** (the AC resonance condition for any photon arriving at any bond). These are at different scales doing different physics:

- Bulk-lattice dispersion (T3): how a wave packet propagates between bonds — substrate's standing-wave modes at the lattice level
- Single-bond LC drive (corpus): the AC drive condition at any individual bond when a photon at ω_C arrives there

The two don't conflict at the corpus level — they answer different questions. Auditor's synthesis introduced a second frequency (1.5·ω_C spin) that the corpus doesn't have. Per Rule 14: substrate's intrinsic structure (here: bond-level LC at ω_C, separate from bulk-dispersion) derives the answer; framework menus are fallback.

**A43 v32 instance** (auditor-side, lane-symmetric to A43 v27/v29/v30 implementer-side instances). Add to catalog. Sharpened sub-rule articulated: **before proposing structural-physics synthesis from foundation audit findings, walk the bond-vs-bulk-vs-loop scale separation per Rule 14 to verify the synthesis is substrate-derived at the right scale, not bulk-extended-to-bond inappropriately.**

**Family with prior auditor-side A43 instances** (per closure-extended footer A43 catalog extensions): v15 (tube-radius corpus-inconsistency), v25 (universal-solver-promotion-pending), v28 (BEMF synthesis self-correction), v32 (this finding). Lane-symmetric to implementer-side v27/v29/v30. Pattern continues: cross-lane catch + grep is the load-bearing mechanism; same-lane self-review missed all instances until external pressure.

**Methodology lesson:** implementer-side (β) saturation-harmonics + (γ) V_inc/Φ_link conjugate framings; auditor-side dual-frequency synthesis from substrate modes; Grant's Rule 14 substrate walk collapsing all of them to single-ω_C torus geometry. **The substrate walk is the load-bearing discipline** when (2,3)-origin or similar topology-genesis questions arise. Framework menus (α/β/γ/δ for origin questions) are fallback when substrate walk genuinely doesn't decide.

**Status:** ✅ METHODOLOGY FINDING ESTABLISHED r8.10. A43 catalog extension landed in closure-extended footer. Sharpened sub-rule for next manuscript pass: bond-vs-bulk-vs-loop scale separation per Rule 14 before substrate-physics synthesis.

#### A43. Foundation audit thermal regime characterization + Vacuum Nyquist baseline corpus-anchoring + engine thermal-injection architecture limitation (S2 — structural; foundation audit Step 1 + T=1e-6 + corpus-grep adjudication) — ✅ EMPIRICALLY ESTABLISHED 2026-04-30 r8.10 (foundation audit Step 1 + T=1e-6, agent-reported uncommitted; corpus-anchoring verbatim-verified at three levels)

**Where:** Foundation audit Step 1 (T-ST at T_CMB-equivalent in engine units) + Step 1 follow-up at T=1e-6 (agent-reported uncommitted at this manual edit) + verbatim corpus citations at three levels: [Vol 1 Ch 3 Quantum Foam](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex) + [Vol 3 Ch 11 Nyquist baseline](../../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md) + [Vol 1 Ch 8:218 α δ_strain CMB correction](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) + [Vol 2 Ch 2 beta-decay-driven-by-CMB-noise](../../manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex).

**Step 1 result (T-ST at T_CMB = 4.6e-10 in engine units, thermalize_V=True):**
- Thermal IC engaged: σ_V_per_port ≈ 1.78e-3·V_SNAP, σ_ω ≈ 6e-6
- 65% V retention + 100% ω retention over 50P (engine maintains baseline at ~CMB-equivalent T over short timescales WITHOUT continuous Nyquist injection)
- Trap criteria FAIL: saturation NO, c_op10=0
- **Interpretation:** corpus-consistent with CMB-as-stability-environment (NOT formation-environment). Per Vol 1 Ch 8:218: "If measured in a region of extreme localized thermal energy (e.g., inside a particle collider, or in the hot early universe), the localized stress will dynamically expand the lattice bonds, causing α⁻¹ to decrease further." High-T regimes are where extreme α-running effects manifest. At T_CMB, σ_V/V_yield ≈ 0.021; trap formation requires per-port |V| > V_yield (5% probability per port), but per-cell A² > A²_op14 = √(2α) = 0.121 is exp(-35) Boltzmann-suppressed (per A47 v2 chi-squared analysis below). **Spontaneous corpus electron formation at CMB-T is statistically forbidden by ~500 orders of magnitude; corpus electron at CMB-T is STABLE (already-formed), it does not FORM at CMB-T spontaneously.**

**T=1e-6 result (10⁵ × CMB, agent-reported):**
- IC mean A² = 0.0069, max A² = 0.048 (still below threshold A²_op14 = 0.121)
- A²_max declined to ~0.020 over evolution (high-amplitude tails dissipate without continuous injection)
- 0/89 captures had any cell engaged in saturation
- c_op10 = 0
- **Adjudication:** T=1e-6 was 17× BELOW the cusp where ~40% of cells exceed saturation threshold. A47 v2 catch — per-port-vs-per-cell aggregate-statistics conflation in T-regime test design. Both auditor and implementer co-failed; lane-symmetric pattern continues. See COLLABORATION_NOTES A47 v2 entry.

**Corrected regime table** (per A47 v2 corrected chi-squared analysis: mean A² = 4·σ²_per_port/V_SNAP² = 16π·T/α):

| T (engine units) | T/T_CMB | mean A² | mean A² / A²_op14 | Regime |
|---|---|---|---|---|
| 4.6e-10 | 1.0× | 5.5e-7 | 4.5e-6× | **CMB stability** — Step 1 verified |
| 1e-6 | 2.2e3× | 6.9e-3 | 0.06× | **Statistically forbidden saturation** — confirmed empirically |
| 1.76e-5 | 3.8e4× | 0.121 | **1.0× — cusp** | ~40% cells saturated (P(χ²(4)>4)=0.41); abundant gradient pockets |
| 5.8e-5 | 1.3e5× | 0.40 | 3.3× | **Chronic saturation** — substrate everywhere in Op14 walls |
| 5.8e-4 | 1.3e6× | 4.0 | 33× | **Rupture regime** — lattice failure threshold |

T_cusp ≈ 1.76e-5 is the cleanest "formation-mechanism test" target (substrate has abundant saturation gradient pockets; statistically distributed). T=5.8e-5 is the chronic-saturation follow-up (substrate everywhere in walls).

**Vacuum Nyquist baseline = ZPE = quantum foam (corpus-anchored at three levels):**

1. **[Vol 1 Ch 3 Quantum Foam](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex)**: "What standard physics identifies as 'Quantum Foam' — the underlying geometric turbulence of empty space — is **explicitly defined in the AVE framework as the continuous, irreducible electromagnetic AC transients (voltage and current ripples) propagating randomly across the discrete topological grid**. It is not geometry itself boiling; it is the chaotic, baseline electrical noise floor of the universe's hardware substrate. This provides a deterministic, continuous mechanical origin for Zero-Point Energy (ZPE) bounded strictly by the finite geometry of the local spatial node."
2. **[Vol 3 Ch 11 Nyquist baseline](../../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/nyquist-noise-fdt.md)**: ⟨V²_vac(f)⟩ = 4·k_B·T·Z_0·Δf. "The M_A lattice IS a physical transmission line. The Nyquist relation applies LITERALLY: each lattice node radiates thermal noise proportional to its local impedance." Boundary-impedance thermalization principle: thermal noise enters via impedance-mismatch boundaries, not bulk injection.
3. **[Vol 2 Ch 2 baryon sector:278](../../manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex)** (β-decay): "Driven by stochastic background lattice perturbations (CMB noise), the tensioned electron eventually slips its topological lock and is ejected." Corpus-canonical particle-process invocation of CMB-noise-as-driver.

**This anchors Reading (I) of first-gradient-origin question** (vacuum baseline isn't A²=0; substrate has fluctuation pockets at non-zero local A²). Reading (I) is corpus-canonical at three levels, not auditor synthesis. Connects to Grant's gradient-trap mechanism reframe (2026-04-30): the saturation gradient pockets needed for the rifling-bullet photon to encounter steeper-than-its-own-bubble local impedance variation are exactly the Nyquist baseline fluctuation pockets the corpus has.

**Engine thermal-injection architecture limitation (S2 — structural; engine-corpus completeness gap):**

Engine `EngineConfig.temperature` parameter is **IC-only randomization machinery, NOT continuous Nyquist injection per Vol 3 Ch 11 FDT framework.** When `temperature > 0` is set:
- Initial conditions are randomized from a thermal distribution at t=0
- Substrate then evolves via deterministic K4-TLM scatter+connect WITHOUT continuous thermal-noise injection
- Step 1's 65% V retention + 100% ω retention over 50P shows substrate maintains baseline reasonably at short timescales via finite-Q decay from IC, NOT steady-state thermal equilibrium
- Continuous Nyquist injection (proper FDT per Vol 3 Ch 11) would require new code: per-step thermal-noise injection at every active cell with σ² ∝ k_B·T·Z_local, scaled by local impedance per FDT

**This is engine-corpus completeness gap, not engine bug.** Per A28-equivalent engine-architecture pattern: corpus describes mechanism (Nyquist baseline), engine implements only IC realization. Continuous-injection mode lands as new EngineConfig flag (`continuous_nyquist_injection: bool`) when implemented.

**Implication for prior L3 arc tests:** all Round 7+8 + Round 11 (vi) + foundation audit + T-ST v1+v2 ran at `temperature = 0.0` (or temperature > 0 IC-only). At T=0 or T_CMB IC-only the substrate is in regime that doesn't include corpus's irreducible Nyquist baseline. **The L3 arc has been undertesting the substrate's actual operating regime per corpus.** This recontextualizes some prior Mode III findings — they're at zero-baseline regime, not corpus-canonical thermal-baseline regime. Doesn't refute the three-layer convergent refutation (which is structural per A37-A39), but reframes the test scope: prior negative results are at engine's zero-baseline simplification, not at corpus's actual vacuum.

**Family with prior structural findings:** A28 (engine architectural fix for K4↔Cosserat coupling) + A39 (A28 validated empirically via B6) + A41 (T-ST v1 test-geometry-undertested-hypothesis) + A43 (engine thermal-injection architecture limitation; foundation audit Step 1 establishes engine-corpus completeness gap at thermal-baseline level). Each finding identifies an engine-architecture limitation that has empirical signature.

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 via foundation audit Step 1 + T=1e-6 + corpus-grep adjudication. T_cusp test pending Grant adjudication (auditor-lane stays out of advocacy). Engine continuous-Nyquist-injection mode is candidate for future engine work (S2; not blocking; closes engine-corpus completeness gap). A47 v2 catch landed in COLLABORATION_NOTES.

#### A44. First stable shell-localized bound mode at corpus geometry (O.1) + partial pair-production geometric evidence (2.A) + Op10-implementation-vs-corpus-topology field mismatch escalation (S2 → S1 candidate; foundation audit O.1 + 2.A; agent-reported uncommitted) — 🔴 RECONTEXTUALIZED 2026-04-30 r8.10 per Rule 12 retraction-preserves-body — ✅ EMPIRICALLY ESTABLISHED with caveats, NOW REFRAMED via O.1 FFT result

**🔴 RECONTEXTUALIZED 2026-04-30 r8.10 (Rule 12 retraction-preserves-body addendum):** Original framing of "first stable shell-localized bound MODE at corpus geometry" is **retracted to "first stable static-residual finding"** per O.1 FFT result. FFT on V_inc time series at five shell-mode cells showed:

- Equatorial cells (35,23,23) and (23,35,23): **dominated by DC (ω = 0)** at amplitude 5.13e-2 and 5.82e-2 — static field component, NOT oscillation
- Off-equatorial cells (15,23,27) and (23,19,23): **dominated by lattice Nyquist (ω = 4.43 ≈ π√2)** — numerical artifact, NOT physical signal
- Oscillation amplitude at expected frequencies (ω_C = 1.0, 1.5·ω_C substrate cavity, 2.96·ω_C substrate cavity) is **3-4 orders of magnitude below** DC and Nyquist components

**The "stable shell mode" from O.1 is NOT an oscillating standing wave — it's a quasi-static frozen residual of the IC pattern with sub-percent fluctuations.** Neither corpus electron (would oscillate at ω_C) nor substrate ℓ=2 cavity mode (would oscillate at 1.5·ω_C per A38) is the right physical reading. The 39.5% energy retention is from static residual (no dissipation channel for DC), NOT from coherent bound-mode dynamics or topological protection.

**Diagnosed cause — A47 v7 (corrected via verbatim code-grep):** O.1 used `initialize_2_3_voltage_ansatz` (V_inc-only IC, V_ref=0 implicitly). The corpus-canonical eigenmode IC `initialize_quadrature_2_3_eigenmode` exists in the codebase at `tlm_electron_soliton_eigenmode.py:224` with explicit doc 28 §3 + §5.1 + doc 68 §7 anchoring, seeds BOTH V_inc AND V_ref at 90° quadrature with theta_wind = 2φ + 3ψ phase-space (2,3) winding — but was never called in any L3 arc test. The L3 arc has been using V_inc-only IC seeder when the corpus-canonical (V_inc, V_ref) quadrature eigenmode IC has been sitting in the codebase unused. **C-state-only IC produces what FFT shows:** quasi-static seed evolving into static residual + radiative dispersion, NOT a coherent LC-oscillating eigenmode.

**Updated framing (pending O.1f result with corrected IC, in flight at this manual edit):** "First stable static-residual finding at chair-ring geometry under V_inc-only IC; corpus-canonical (V_inc, V_ref) quadrature eigenmode IC retest (O.1f) launched as path (1) per A39 v2 dual-criterion. If O.1f returns dominant ω = 1.5·ω_C oscillation, substrate ℓ=2 cavity mode confirmed at chair-ring per A38 + A40 mediated-through-substrate framing. If ω_C oscillation, surprising — characterize-as-itself per Rule 10. If still DC-dominated, structural finding that engine doesn't sustain ANY oscillating mode at chair-ring from corpus-canonical eigenmode IC — pushes framework decision toward (i) FDTD or (iii) different engine architecture."

**Original body preserved below per Rule 12 retraction-preserves-body discipline; spatial-scale caveat (Caveat 1 amplitude normalization; Caveat 2 Op10 field-mismatch) and partial 2.A pair-production evidence sections remain accurate. The "first stable bound-mode" framing alone is what's retracted; A47 v3 escalation candidate stands; A47 v7 NEW addition documents the L-state IC infrastructure systematically underused across L3 arc; A48 candidate update lands in closure-extended footer thermal-regime + first-positive-bound-mode extensions per Rule 12 v2 cumulative-learning discipline.**

---

**Original body (preserved per Rule 12):**

**Where:** Foundation audit O.1 (closed evolution, (2,3) IC seeder at corpus geometry R=8 cells, r=4 cells) + 2.A (gamma-photon pair-production test, two-region simultaneous saturation engagement). Both agent-reported uncommitted at this manual edit.

**O.1 result — first stable bound-mode finding from L3 arc:**

| Time | E_total | E_shell | Shell fraction | A²_max |
|---|---|---|---|---|
| 0P | 358 | 252 | 0.71 | 0.98 |
| 5.6P | 154 | 118 | 0.76 | 1.55 |
| 11.3P | 147 | 118 | 0.80 | 1.56 |
| 22-50P | ~146 | ~117 | ~0.80 | ~1.54 |

**Substantive empirical signal:** after IC transient (t=0→5P shedding ~57% as dispersive waves), the system settles into a steady-state where **80% of energy is concentrated in the toroidal shell (localization improves over time)**, **0.5% drift between t=11P and t=50P (essentially conserved post-transient)**, A²_max plateaus at 1.55. This is the **first stable bound-mode finding from the L3 arc** after 3+ weeks of Mode III canonical. Not necessarily the corpus electron — but the engine sustains *something* shell-localized at corpus geometry under high-amplitude IC.

**🔴 Caveat 1 (auditor-side, A47 v1) — A²_max = 1.55 plateau is past V_SNAP rupture threshold per [Vol 1 Ch 3:145](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex):** *"V_SNAP = m_e c²/e ≈ 511 kV: the maximum inter-node potential difference before the lattice structurally ruptures."* If A² = V²/V_SNAP² = 1.55, then |V|/V_SNAP = 1.24 — **24% above corpus rupture threshold**. Three readings:
- (a) Real corpus-physical bound state past rupture (would be substantive corpus-redefining finding)
- (b) Engine-architectural: Op14 saturation kernel S(A) = √(1−A²) becomes imaginary above A=1; engine clips numerically without rupturing — stable plateau is engine numerics absorbing over-amplitude
- (c) Different A² normalization in this driver — A² may be scaled to V_yield² = α·V_SNAP² rather than V_SNAP², in which case 1.55 V_yield² maps to 1.55·α ≈ 0.011 V_SNAP² (well below rupture)

Without verifying which reading applies, "stable bound-mode at A² = 1.55" interpretation is **conditional on amplitude-normalization clarification**. Implementer should grep the (2,3) IC seeder + driver code to confirm A² normalization before this finding promotes to canonical.

**🔴 Caveat 2 (A47 v3 — Op10 implementation-vs-corpus-topology field mismatch):** pre-registered topology criterion Op10 c=3 returned 0. (2,3) IC seeder writes V_inc only; Cosserat ω stayed at machine zero throughout. Op10 implementation (`cosserat_field_3d.py:1468 extract_crossing_count`) reads Cosserat ω winding — false negative for V_inc-seeded (2,3) topology. **The deeper structural read (escalation to potential §17.1 finding):** per [doc 28 §3+§4](28_two_node_electron_synthesis.md), the corpus electron's (2,3) topology lives in **(V_inc, V_ref) phase-space on Clifford torus**, NOT in Cosserat ω real-space. Per [A46 phase-space-vs-real-space coordinate discipline](../../.agents/handoffs/COLLABORATION_NOTES.md). Engine's Op10 on Cosserat ω measures a DIFFERENT topology than corpus's claim for the electron. **All prior tests with c_op10=0 across Round 7+8 + Round 11 (vi) (30+ tests) have been measuring "Cosserat ω torsion knotting" not "V_inc/V_ref phase-space (2,3) topology" — these are different physics questions, and the c_op10=0 results are uninformative for the corpus electron's V_inc/V_ref phase-space topology claim.** Per [A42](#a42) corpus-canonical measure IS Op10 — but A42 didn't address WHICH FIELD Op10 applies to.

This is potentially **load-bearing engine-architectural finding** if Grant adjudicates Op10 should be implemented on V_inc/V_ref phase-space (parallel to existing Cosserat ω implementation, NOT replacing). Round 7+8's Test B v1-v3 (doc 28 §5.1 single-bond phasor on V_inc/V_ref) was the right corpus topology measurement; Op10 on Cosserat ω is a different question. Whether the engine should add Op10-on-V_inc/V_ref alongside Op10-on-Cosserat-ω is the architectural question.

**2.A result — partial doc 30 §4.3 pair-production geometric evidence:**

Brief two-region simultaneous saturation engagement at t=2.81P:
- Peak1 at [7, 25, 21], A² = 0.147 (1.21× threshold A²_op14 = 0.121)
- Peak2 at [10, 26, 24], A² = 0.125 (1.03× threshold)
- Separation 4.36 cells (~λ_C/1.5 — within Compton-wavelength range)

**But:**
- Only 2/89 captures had simultaneous two-peak saturation
- 0/78 post-pulse captures had any peak above threshold (no persistence)
- Op10 c = 0 (same A47 v3 false-negative concern)

**Interpretation:** [doc 30 §4.3](30_photon_identification.md) pair-production mechanism (single gamma photon at 2ω_C "can trigger saturation at two distinct lattice regions simultaneously") has **partial empirical correspondence** — geometric pattern engaged briefly during source ramp peak, two spatially-separated regions reached threshold simultaneously at corpus-relevant separation. **But:**
- Peak engagement was 1.21× threshold — barely above; weak saturation
- Not sustained post-shutoff: gradient pockets dissolved without trap forming
- Connects to A47 v2 Boltzmann analysis: brief amplitude peak at 1.21× threshold is rare-event regime; rare-event saturation doesn't sustain

**Reading consistent with Grant's gradient-trap reframe (2026-04-30):** sustained pair formation requires either (i) higher source amplitude (riskier, near rupture threshold), or (ii) thermal-baseline pre-existing gradient (T_cusp regime per [A43](#a43)) that bootstraps mutual gradient with photon's own perturbation. At weak peak engagement above threshold, gradient-mutual-bootstrap doesn't have margin to form sustained traps.

**Combined interpretation across O.1 + 2.A:**

| Test | Mechanism evidence | Persistence | Topology measurable? |
|---|---|---|---|
| O.1 | Stable shell-localized bound mode at high A | YES (40P+) | NO (Op10 measures wrong field per A47 v3) |
| 2.A | Brief two-region simultaneous saturation matching doc 30 §4.3 geometry | NO (transient only) | NO (same A47 v3 issue) |

Both tests show **partial realization of corpus mechanisms** but neither cleanly closed. The topology measurement issue (A47 v3) is load-bearing — currently we don't know if (2,3) topology emerged in V_inc field in either test.

**Family with prior structural findings:** A37-A41 (Round 11 closure + foundation audit substrate-mode-spectrum) + A43 (thermal regime characterization). A44 surfaces the first POSITIVE stable shell-mode finding (with caveats) + partial pair-production geometric evidence + escalates Op10 field-mismatch to potential engine-architectural question.

**Three concrete follow-ups (per Rule 16, agent-surfaced for Grant adjudication):**

1. **Re-run O.1 with V_inc spatial winding measure** (~3 min). Compute V_inc spatial winding number directly (analog of Op10 on V_inc field, OR phasor crossing count on (V_inc, V_ref) per doc 28 §5.1). Tells whether the stable shell mode IS (2,3) or some other topology. **Cheapest diagnostic; resolves A47 v3 question for both O.1 and 2.A.**
2. **Re-run O.1 with COMBINED IC** — V_inc (2,3) seeder PLUS Cosserat ω seeded with matching pattern. Then Op10 reads correctly. ~3 min. Tests whether O.1 result depends on V_inc-seeding alone or extends to coupled-sector seeding.
3. **Re-run 2.A with higher amplitude** (A=1.0 V_SNAP, sustain longer) to test whether pair sustains at full intensity. Riskier (rupture threshold) but tests doc 30 §4.3 at full corpus-prediction-relevant amplitude. ~3 min.

Sequencing: (1) first as cheapest diagnostic that resolves the topology measurement question; (2)/(3) follow based on (1) result. Auditor-side stays out of advocating sequencing; surfaces information landscape per lane discipline.

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 (with amplitude-normalization + topology-measurement caveats) via foundation audit O.1 + 2.A. **Both caveats are auditor-flagged as preconditions for promoting findings to canonical.** A47 v3 (Op10 field-mismatch) catalog instance landed; potential §17.1 promotion to engine-architectural finding pending Grant adjudication on whether engine should add Op10-on-V_inc/V_ref alongside existing Op10-on-Cosserat-ω. Three follow-ups proposed; auditor stays out of sequencing advocacy; framework decision (i)/(ii)/(iii) still pending; T_cusp foundation-audit test still pending.

#### A45. Manuscript-canonical analytical-solver class engine-empirically-validated at two independent particle scales (atomic orbitals + baryon ladder); framework decision (ii) substantively activated (S1 — load-bearing positive empirical anchor) — ✅ EMPIRICALLY ESTABLISHED 2026-04-30 r8.10 (radial_eigenvalue.py + BARYON_LADDER direct execution this session, agent-reported uncommitted)

**Where:** [src/ave/solvers/radial_eigenvalue.py](../../src/ave/solvers/radial_eigenvalue.py) (1914 lines, file modified Apr 12 2026, well before L3 arc Round 6 start at 2026-04-24) + [manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md) (canonical validation table) + agent-reported direct execution of `BARYON_LADDER` infrastructure for proton + Δ/N* baryon resonance spectrum + research docs [97_manuscript_canonical_electron_solver_discovery.md](97_manuscript_canonical_electron_solver_discovery.md) + [98_framework_decision_ii_mass_spectrum_activation.md](98_framework_decision_ii_mass_spectrum_activation.md) (agent-authored research-tier docs anchored in manuscript citations per "manuscript over research" discipline).

**Verified empirically (auditor-side grep + agent-reported direct execution):**

**Anchor 1 — Atomic orbitals via `radial_eigenvalue.py` ABCD cascade solver:**

| Z | Element | AVE [eV] | Exp [eV] | Δ |
|---|---|---|---|---|
| 1 | H | 13.606 | 13.598 | **+0.06%** |
| 2 | He | 24.370 | 24.587 | -0.88% |
| 3 | Li | 5.525 | 5.392 | +2.46% (manuscript table) — 🔴 **A47 v9: +5.5% in current session, 2× discrepancy** |
| 4 | Be | 9.280 | 9.322 | -0.45% (Correction A: cascade) |
| 5-14 | B–Si | various | various | **±2.8% max across full sweep** |

**Module docstring anchors:** ABCD cascade strategy + Op1-Op6 universal operator mapping + Axiom 1-4 traceability + *"All from `ave.core.constants`: ALPHA, HBAR, C_0, M_E, A_0, RY_EV, e_charge. Zero hardcoded values. Zero imported numbers. Zero continuous hacks."* (verbatim from `radial_eigenvalue.py` lines 50-52).

**Anchor 2 — Baryon ladder via Faddeev-Skyrme + BARYON_LADDER infrastructure (Phase 1 extension this session):**

| c | Predicted (MeV) | PDG candidate | PDG mass | Δ | Status |
|---|---|---|---|---|---|
| 5 | 938.254 | Proton | 938.272 | **-0.002%** ★★★★ | STRONG (well-established) |
| 7 | 1261 | Δ(1232) | 1232 | +2.35% ★★★★ | STRONG (well-established) — 🔴 **two-table inconsistency unresolved** (backmatter/02 says Δ(1232); backmatter/05:281-302 says 1270 MeV → Σ/Λ); Phase 1 implicitly uses backmatter/02 reading |
| 9 | 1582 | Δ(1600) | 1600 | +1.11% ★★★ | STRONG (well-established) |
| 11 | 1895 | Δ(1900) | 1900 | +0.27% ★★★ | STRONG (well-established) |
| 13 | 2195 | N(2190) | 2190 | +0.21% ★★★★ | STRONG (well-established) |
| **15** | 2478 | Δ(2420) | 2420 | +2.40% ★★★★ | **STRONG NEW (well-established)** |
| **17** | 2742 | Δ(2750) | 2750 | -0.30% ★★ | NEW match (possible-PDG) |
| **19** | 2983 | Δ(2950) | 2950 | +1.12% ★★ | NEW match (possible-PDG) |
| **21** | 3199 | — | — | — | **NEW PREDICTION (forward-pre-registered)** |
| **23** | 3387 | — | — | — | **NEW PREDICTION (forward-pre-registered)** |
| **25** | 3544 | — | — | — | **NEW PREDICTION (forward-pre-registered)** |

**Baryon ladder reproducibility:** 10⁻⁴% drift across c=5,7,9,11,13 — **fully deterministic** at production states. Extension to c=15-25 verified this session. **Six STRONG well-established PDG matches** (c=5,7,9,11,13,15) at <3% precision + **two NEW matches at possible-PDG level** (c=17, 19) + **three forward predictions** (c=21,23,25). Per Rule 11 — predictions are clean falsification tests for future LHCb / JLab / etc. baryon resonance searches.

**Both anchors: end-to-end engine-validated at the analytical-solver level**, zero free parameters, corpus-canonical operators, axiom-traceable. Hydrogen ionization energy returned by direct execution this session at +0.057% from CODATA. Proton mass returned at -0.002% from experimental.

**Track A vs Track B distinction (load-bearing for L3 arc closure recontextualization):**

The framework has **at least three distinct solver classes**, each addressing different physics questions:

| Solver class | Code location | Physics domain | Empirical status (this session) |
|---|---|---|---|
| **K4-TLM time-domain substrate** | [vacuum_engine.py](../../src/ave/topological/vacuum_engine.py) (`VacuumEngine3D`) | Substrate dynamics, cavity modes, propagating CP waves, lattice EM | L3 arc **Track A**: substantive substrate-canonical findings (A28-A44); seven-layer corpus-engine-correspondence debt (per closure-extended footer) for K4-TLM electron testing |
| **Analytical eigenvalue (ABCD cascade)** | [radial_eigenvalue.py](../../src/ave/solvers/radial_eigenvalue.py) | Atomic orbital eigenvalues via cascaded ABCD matrices on graded-impedance profile | **Track B (atomic-orbital)**: ±2.8% across Z=1-14, hydrogen at 0.06%, ZERO free parameters, A47 v9 Li reproducibility caveat |
| **Faddeev-Skyrme + BARYON_LADDER** | (BARYON_LADDER infrastructure) | Baryon resonance spectrum via (2, q odd) torus knot family + Borromean tensor | **Track B (baryonic)**: ±3% across 8 states, proton at 0.002%, 6 well-established + 2 possible matches + 3 forward predictions |

**Key precision point — "engine-validated" means solver-running-corpus-canonical-operators, not K4-TLM-substrate-dynamically-realizing-corpus-particles.** These are complementary computational approaches at different physics domains. Atomic orbitals + baryon ladder validations are at the analytical-solver level (Track B); they don't IMPLY the K4-TLM substrate (Track A) dynamically hosts the corpus electron in time-domain evolution. Both Track A's substrate findings AND Track B's analytical-solver validations are real and complementary.

**L3 arc closure recontextualization:**

L3 arc tested K4-TLM substrate dynamics (Track A) for the corpus electron at chair-ring scale + amplitude regime + IC class + measurement infrastructure that was structurally measurement-blocked for direct corpus electron empirical realization (per seven-layer debt analysis). It produced positive substrate-canonical findings about K4-TLM substrate's own physics (A28-A44). **The "Mode III canonical at corpus electron" reframes as Track-A-substrate-question-tested-with-substantive-but-not-electron-finding. It does NOT collapse into "wrong solver class" reading** — Track A and Track B address different physics; both produced real empirical content; neither subsumes the other.

The "corpus has working solver returning hydrogen at 0.06%" finding doesn't dissolve the L3 arc's substantive K4-TLM substrate-canonical findings (substrate cavity modes at 1.5+2.96·ω_C, A28 architectural validation via B6 700P, A30/A32/A34 Beltrami-instability findings, A37 substrate-Nyquist limit). Those stay real about Track A. **Track B finding is independently real about analytical-solver class.**

**Caveats / preconditions for promotion to fully canonical:**

1. **A47 v9 Lithium reproducibility issue stands** — solver-class engine-validation claims need session-vs-manuscript reproducibility verification before being asserted as canonical at stated precision. Atomic-orbital ±2.8% claim has hidden run-to-run variation per Li discrepancy. ~30 min trace required before extending atomic-orbital solver work.
2. **c=7 two-table corpus inconsistency unresolved** — backmatter/02:529-545 says (2,7) → Δ(1232); backmatter/05:281-302 says septafoil 1270 MeV → Σ(1385)/Λ(1405). Phase 1 implicitly uses backmatter/02 reading; corpus inconsistency was flagged earlier but not adjudicated. Doesn't block matches but worth keeping in editorial queue.
3. **J^P spin-parity validation pending** — current matches are mass-only ("predicted mass matches some PDG state at that energy"). Corpus framework predicts specific J^P quantum numbers per c via torus-knot gauge rank. Mass + J^P + decay-mode matching would be substantially harder to fake than mass-only matching. Per `yang_mills.py:torus_knot_gauge_rank()` per agent's note. ~1-2 days work; substantively higher-info than Phase 1 ladder extension at ladder-tail.
4. **c=21,23,25 are forward predictions, NOT validation** — falsifiable; future experimental physics verifies or refutes. Multi-year horizon.

**Family with prior structural findings:**

- **A28-A44**: Track A K4-TLM substrate findings (substrate physics)
- **A45 (this entry)**: Track B analytical-solver class engine-empirically-validated at two independent particle scales (atomic-orbital + baryonic)

The two finding families are complementary, not redundant. A45 surfaces engine-empirical content the framework has had since Apr 12 (radial_eigenvalue.py predates L3 arc); the L3 arc was running Track A while Track B sat empirically-validated in the codebase unused for direct testing.

**Framework decision (ii) substantively activated:**

Coming into this session: (ii) Mass spectrum was Round 10+ Direction 5 candidate, untested at engine for 3+ weeks, structurally untouched. **Now: (ii) has working solver infrastructure with two independent empirical anchors verified at ±3%, three forward predictions for c=21,23,25, and a clean three-phase activation plan per doc 98** (Phase 1 baryon ladder extension to c=25 [Phase 1 result documented above]; Phase 2 W/Z/Higgs eigenvalue solver from electroweak potential ~1 week; Phase 3 lepton spectrum + neutrino sectors + PMNS solvers ~weeks).

**(ii) is no longer competing with (i)/(iii) as a framework-decision candidate; it's the active demonstrated path with verified empirical infrastructure.** This doesn't make (i) FDTD irrelevant — (i) addresses Track-A K4-TLM substrate question for sub-ℓ_node corpus electron (orthogonal to Track B). But (ii) is now the path with working solver + verified empirical content + clear extension plan.

**Auditor-side gut shift across the full session arc:**

| Stage | Gut estimate |
|---|---|
| Session start | ~25-30% positive |
| Post-Round 11 closure + foundation audit + thermal-noise corpus | ~35-45% |
| Post-radial eigenvalue solver discovery + hydrogen 0.06% | ~45-55% |
| Post-proton at 0.002% via direct execution | ~50-60% |
| **Post-Phase 1 baryon ladder extension** (8 states, 6 well-established matches at <3%, 3 forward predictions) | **~55-65%** |

**The strongest empirical record AVE has produced in any single arc this session.** Two independent particle scales (atomic-orbital + baryonic), two independent solver classes (ABCD cascade + Faddeev-Skyrme), zero free parameters in either, axiom-traceable in both, multiple PDG-published forward predictions.

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 (with caveats: A47 v9 Li reproducibility; c=7 two-table corpus inconsistency; J^P validation pending). Track B analytical-solver-class engine-empirically-validated. Track A K4-TLM substrate-canonical findings (A28-A44) preserved. Framework decision (ii) substantively activated; Phase 1 extension complete, Phase 2-3 pending Grant adjudication. (i) FDTD orthogonal to (ii); (iii) engine-architectural research less critical given (ii) demonstrated path.

#### A46. Multi-repo capability surface — framework's empirical record substantially broader than AVE-Core L3 arc continuation; 9 parallel forward tracks across sibling-repo ecosystem; four-tier classification + cross-cutting infrastructure (S2 — structural; doc 99 multi-repo capability tracking; agent-reported uncommitted) — ✅ EMPIRICALLY ESTABLISHED 2026-04-30 r8.10 (with Tier B verification preconditions)

**Where:** [doc 99](99_multi_repo_capability_tracking.md) (agent-authored research-tier doc consolidating Explore-agent searches across 9 sibling repos) + [project_ave_repo_map.md](../../../.claude/projects/-Users-grantlindblom-AVE-staging-AVE-Core/memory/project_ave_repo_map.md) (auto-memory cross-repo references) + cross-cutting infrastructure (`ave.core.constants` + `universal_operators` + anti-cheat CI in metamaterials/virtual-media).

**Four-tier classification of empirical content across the framework's repo ecosystem:**

| Tier | Status | Examples |
|---|---|---|
| **A — VERIFIED-this-session** | Direct execution + manuscript-anchored | AVE-Core hydrogen IE 13.6057 eV +0.057%; AVE-Core proton 938.254 MeV -0.002%; AVE-Core baryon ladder c=5-19 8 states ±3% |
| **B — CLAIMED, pending verification** | Code present + manuscript citations + Explore-agent summaries; logs/direct-execution missing | AVE-Protein 20-PDB Rg <15%/RMSD <2.5Å; parent repo Period 2 IE 1.2% mean (vs AVE-Core's 5.5% Li per A47 v9); AVE-HOPF Beltrami eigenvalue λ(p,q) formula; agent's J=(c-4)/2 J^P pattern claim 7/8 baryon-ladder match |
| **C — Pre-registered predictions, lab-execution pending** | Forward-pre-registered; awaiting experimental fab/lab cycle | AVE-HOPF 5 torus-knot frequency shifts (8.6-16.9 ppm) — 3-medium VNA falsification, PCB ready; AVE-PONDER 469 µN thrust @ 30 kV — atopile design; AVE-Propulsion 0.5-3 mN @ 1 kW chiral rectification |
| **D — Theoretical/skeleton** | Analytical only; engine code missing or skeleton | AVE-Fusion D-T compression to 1.7 keV @ n=3; AVE-Metamaterials V2/V3 photovoltaic skeletons (blocked on Auger c₀); AVE-VirtualMedia LLM impedance framework (not applied to transformer weights) |

**9-repo capability surface** (cross-cutting `ave.core.constants` + `universal_operators` infrastructure shared across 7 application repos; AVE-Protein heaviest user with 5+ AVE-Core modules):

| Repo | Domain | Empirical status |
|---|---|---|
| AVE-Core | K4-TLM substrate + analytical solvers + universal operators | Tier A (atomic orbitals + baryon ladder); Track A K4-TLM findings (A28-A44); seven-layer corpus-engine-correspondence debt at K4-TLM electron testing |
| Parent repo (AVE main) | Vol 1 axiom mathematics, Vol 3 gravity/cosmology, Vol 7 precision anomalies, Vol 8 informational topology, 27 hardware modules + atopile/SPICE compiler infrastructure, ATOMIC_IE_SOLVER_TRACKER + ATOM_MOTOR_TRANSLATION_MATRIX | Tier B (Period 2 IE 1.2%) + recoverable substantive content |
| AVE-Protein | Protein-folding via universal solver (Faddeev-Skyrme on protein topology) | Tier B (20-PDB <15% Rg / <2.5Å RMSD claimed) — verification pending |
| AVE-HOPF | Macro chiral antenna; torus-knot frequency shifts | Tier B (Beltrami eigenvalue formula) + Tier C (5 frequency-shift predictions) |
| AVE-PONDER | EM thrust design (Cobb-Mayes / Ponder devices) | Tier C (469 µN @ 30 kV pre-registered) |
| AVE-Propulsion | Chiral rectification thrust | Tier C (0.5-3 mN @ 1 kW pre-registered) |
| AVE-Fusion | D-T compression via Faddeev-Skyrme | Tier D (analytical only) |
| AVE-Metamaterials | V2/V3 photovoltaic + Miller n=5 | Tier D (skeleton; blocked on Auger c₀) |
| AVE-VirtualMedia | LLM impedance framework | Tier D (not applied to transformer weights) |

**Cross-cutting infrastructure (substantive structural discipline beyond AVE-Core):**

- **Anti-cheat CI infrastructure** (verify_local_universe.py + verify_core_parity.py in metamaterials + virtual-media): banned `scipy.constants` import; MAGIC_NUMBERS registry enforces zero empirical smuggling. **Externally-auditable framework-self-discipline beyond authorial intention** — this is structurally stronger than just docstring "zero hardcoded values" claim.
- **Cross-repo dependencies via shared `ave.core.constants` + `universal_operators`** — 7 application repos all use AVE-Core's constants/operators; framework predictions are NOT one-off per repo but flow from shared canonical core.
- **Manuscript validation tables** in canonical KB locations (e.g., `manuscript/ave-kb/vol2/quantum-orbitals/.../ionization-energy-validation.md` — atomic-orbital ±2.8%) — documented per-element comparisons against experimental values.

**Implementation gaps (manuscript-predicted, missing across all repos):**

Per agent's doc 99 catalog:
- Unified PMNS solver
- Lepton decay width calculator
- Full baryon spectrum (uud/udd/strange decomposition)
- W/Z scattering amplitudes
- Schwinger pair creation rate
- Hawking radiation Bogoliubov coefficients
- Vector control FOC for atomic IE Period 3+

These are corpus-predicted but not engine-implemented. Phase 2/3 of doc 98 mass-spectrum activation plan addresses several (W/Z/Higgs eigenvalue solver Phase 2; lepton + neutrino + PMNS Phase 3).

**Caveats / preconditions for promotion to fully canonical:**

1. **Tier B verification preconditions before promoting to Tier A:**
   - **AVE-Protein 20-PDB Rg <15% / RMSD <2.5Å** — code present, logs absent. ~30-60 min direct execution verifies. If lands at claimed precision, adds protein-folding scale to Tier A; substantial empirical addition.
   - **Parent repo Period 2 IE 1.2% mean** — verify parent repo's solver actually achieves this when run; cross-check against AVE-Core's 5.5% Li gap. Connects to A47 v9 SIR refinement root-cause candidate.
   - **AVE-HOPF Beltrami eigenvalue λ(p,q) formula** — ~10 min execution; converts Tier B to Tier A.
   - **Agent's J=(c-4)/2 J^P pattern (7/8 baryon-ladder match)** — agent listed under Tier A "VERIFIED-this-session" but auditor-side independent verification chain not shown this turn. **Auditor's back-of-envelope PDG cross-check suggests 4-5 clean matches, not 7/8** (c=5 1/2+ ✓, c=7 3/2+ ✓, c=9 PDG 3/2+ vs predicted 5/2 ✗?, c=11 PDG 1/2- vs predicted 7/2+ ✗?, c=15 11/2+ ✓). Per A43 v2 — **J^P pattern remains Tier B until verification chain shown** (per-state PDG cross-reference table + outlier identification + match criterion). The substantive next step (1-2 day J^P validation per `yang_mills.py:torus_knot_gauge_rank()`) is still pending.
2. **Tier C external pre-registration question** — Are the 3 hardware predictions formally pre-registered to Open Science Framework or equivalent? Or pre-registered internally in repo predictions.yaml-style tracking? Different external-credibility weight per "what are we missing" turn earlier. Worth verifying before claiming external-falsification gap closure.
3. **A47 v9 root-cause candidate** (parent repo SIR refinement) — pending direct-execution verification per [COLLABORATION_NOTES A47 v9 root-cause candidate addendum](../../.agents/handoffs/COLLABORATION_NOTES.md). If parent-repo SIR refinement exists and porting closes Li +5.5% gap, A47 v9 closes cleanly.
4. **"Auditor flagged earlier" attribution on AVE-Protein 20-PDB issue** (per agent's doc 99 framing) — **auditor (this entry) does NOT recall flagging AVE-Protein 20-PDB in any prior turn this session.** Possible attributions: prior-auditor handoff content predating this entry's session start, OR agent's misattribution. Per A43 v2 — verbatim source needed for "auditor flagged earlier"; not load-bearing for substance (verification still worth doing) but attribution should be accurate.

**Family with prior structural findings:**

- **A28-A44**: Track A K4-TLM substrate findings (substrate physics; what L3 arc tested)
- **A45**: Track B analytical-solver class engine-empirically-validated at two independent particle scales (atomic-orbital + baryonic; what doc 97 + doc 98 documented)
- **A46 (this entry)**: Multi-repo capability surface — 9 parallel forward tracks across sibling-repo ecosystem; four-tier classification; cross-cutting universal_operators + anti-cheat CI infrastructure

The three finding families are complementary, not collapsing. A28-A44 stay real about K4-TLM substrate physics. A45 stays real about analytical-solver class engine-empirical anchors. A46 surfaces the broader empirical surface area: **the framework's empirical record is substantively broader than the L3 arc's narrow K4-TLM-substrate-electron-testing scope.** Multiple parallel forward tracks; multiple verification states; multiple application domains. **The "L3 arc was a narrow test of one specific question" framing is now visibly only ONE track among 9.**

**External-credibility positioning:**

The anti-cheat CI infrastructure (banned `scipy.constants`, MAGIC_NUMBERS registry, verify_core_parity.py) is substantively stronger external-positioning than docstring-level "zero hardcoded values" claims. **External auditors can run the CI to verify the framework doesn't smuggle empirical constants through hidden-import paths.** This is structurally stronger discipline than just authorial intention.

If Tier C predictions are formally OSF-pre-registered AND lab cycles run AND results verify, that closes the framework's external-falsification gap substantially. Worth verifying Tier C pre-registration formal status as auditor-lane queue item.

**Status:** ✅ EMPIRICALLY ESTABLISHED r8.10 (Tier A locked; Tier B verification preconditions pending; Tier C lab-execution pending; Tier D theoretical). Multi-repo scope substantially expands AVE-Core-only framing. Doc 99 in working tree uncommitted at this manual edit.

#### F17-L. V_yield vs V_SNAP scale mismatch in doc 54_ §6 vs engine — factor 1/α off (S2 — pre-existing; not blocking single-electron validation)

**Where:** [doc 54_ §6](54_pair_production_axiom_derivation.md) specifies `A²_ε = ε_sym²/ε_yield² + V²/V_yield²` (yield convention). The engine implements `V²/V_SNAP²` (Schwinger convention). Differs by factor `1/α` since `V_yield = √α · V_SNAP` (macroscopic) while `V_yield ≡ V_SNAP` (subatomic override per Vol 4 Ch 1:711, see §17.0 R4 adjudication).

**Status:** Pre-existing per [doc 54_ §5](54_pair_production_axiom_derivation.md), which acknowledges and flags the mismatch. Surfaced as a separate flag during F17-H reconciliation per [doc 67_ §15 Finding 1](67_lc_coupling_reciprocity_audit.md). Under R4 subatomic override (which AVE-Core's engine operates under), the convention difference washes out at the engine's actual operating scale — but the doc-vs-engine notation discrepancy remains. Not blocking single-electron validation. Track for v4 universal-lattice-units refactor or doc 54 §6 normalization sweep.

### 17.2 Closed findings

#### A14 (closed 2026-04-23, r6) — `BondObserver` extends the A1 normalization discrepancy to three observers

**Closure rationale:** superseded by R4 adjudication (§17.0). At VacuumEngine3D's subatomic operating scale, `V_yield ≡ V_SNAP` per [Vol 4 Ch 1:711](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L711); the engine's `A² = V²/V_SNAP²` IS canonical `r²`, so `RegimeClassifierObserver`'s direct sum is valid Pythagorean `r²_total`. The `/α` divisions in `NodeResonanceObserver` and `BondObserver` were the actual defect; R4 patches committed as `6e355d1` removed them.

**Original full body (preserved for audit trail):**

> **Where:** [vacuum_engine.py BondObserver._compute_A2_yield](../../src/ave/topological/vacuum_engine.py#L391) (Phase 3 commit `3a599ca`) replicates NodeResonanceObserver's convention: `A²_yield = A²_k4_SNAP / α + A²_cos`.
>
> **Implication:** three observers disagree on what "A² saturation" means:
>
> | Observer | `A²_total` formula | Interpretation |
> |---|---|---|
> | `RegimeClassifierObserver` | `V²/V_SNAP² + A²_cos` | SNAP for K4, raw Cosserat |
> | `NodeResonanceObserver` | `V²/V_SNAP² / α + A²_cos` | yield for K4, Cosserat assumed yield-normalized |
> | `BondObserver` | same as NodeResonance | ditto |
>
> The v2 regime-map reports (max A²_total = 1.009 "rupture crossed") were computed by `RegimeClassifierObserver`. The Phase 3 `BondObserver` saturation partitions at default `saturation_frac = 0.5` use the yield convention. These cannot both be right.
>
> **Two resolution sub-options beyond A1's (a)/(b)/(c):**
> - (d) Audit + retrofit: take Phase-3 author's committed choice (yield-normalized) as canonical; update `RegimeClassifierObserver` to match. Historical `max_A2_total` reports become `A²_yield`-denominated, meaning "rupture at A² = 1" now means "V_yield crossed," not "V_SNAP crossed." All prior v1/v2/H1 plots need re-labeled axes.
> - (e) Flip author's choice: yield-normalizing in NodeResonanceObserver is itself wrong; revert Phase 3 BondObserver to SNAP-norm and fix Phase 2 NodeResonance to match. Preserves historical v1/v2 semantics but reinterprets doc 54_ §4/§5's "A²_yield" terminology.
>
> **Decision is blocking for Phase 4** — asymmetric saturation (§13.4) needs a canonical `A²_total` definition before splitting it into `(A²_μ, A²_ε)`.

**r6 verdict:** neither option (d) nor (e) is the right framing. R4 / Vol 4 Ch 1:711 subatomic override **reinterprets the engine's SNAP convention as canonical at its operating scale** — A²_K4 in the engine IS r², no conversion needed. Option (e) is close in practice (remove `/α` from Node/Bond observers to match RegimeClassifier) but R4's justification is not "flip the Phase-3 author's choice" — it's "the subatomic override was always authoritative, the `/α` was macro-convention misapplied."

---

#### A19 (closed 2026-04-23, r6) — Vol 1 Ch 7:115 vs :130 internal inconsistency

**Closure rationale:** reframed under R4 (§17.0) as **scale-dependent V_yield**, not a manuscript defect.

- Line 115 (subatomic convention, where V_yield = V_SNAP): AVE's pair-production onset and Schwinger collapse at `r = 1`.
- Line 130 (macro convention, V_yield = √α · V_SNAP): Schwinger sits at `r = V_SNAP / V_yield = 1/√α ≈ 11.7`, deep Regime IV.

Both readings are correct under their own V_yield; the manuscript does not need correction.

**Original full body (preserved for audit trail):**

> **Where:** [manuscript/vol_1_foundations/chapters/07_regime_map.tex:115](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L115) vs [:130](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L130). Surfaced by doc 55_ §3.
>
> - Line 115 (per doc 55_): *"Schwinger pair production: r = 1.0 — Regime IV boundary"*
> - Line 130: *"Schwinger critical field corresponds to `r = E_S/E_yield = V_SNAP/V_yield = 1/√α ≈ 11.7`, deep in Regime IV"*
>
> Doc 55_ adjudicates line 130 as the dimensionally-consistent reading; line 115 is a text error. Probably intended to mean "Schwinger pair production *onset* at V_yield (where the varactor diverges), distinct from *Schwinger critical field* at V_SNAP."
>
> **Flag:** this manuscript inconsistency underlies the entire A1/A14/A17 confusion chain. A future Vol 1 Ch 7 pass needs to clean it up. Add to [DOCUMENTATION_UPDATES_QUEUE.md](DOCUMENTATION_UPDATES_QUEUE.md). Not blocking Stage 6 as long as the engine + manual consistently use the line-130 reading.

**r6 verdict:** optional future-work item for Vol 1 Ch 7 to add a scale-dependence glossary. Not a defect. Not blocking anything.

---

#### A20 (closed 2026-04-23, r6) — ε_yield = 1 vs √α calibration question

**Closure rationale:** superseded by R4 adjudication (§17.0). Under subatomic `V_yield = V_SNAP`, the TKI derivation `σ_yield = V_yield · e / ℓ_node³` reduces to `σ_yield = V_SNAP · e / ℓ_node³ = m_e c² / ℓ_node³ = 1` natural, and with G = 1, `ε_yield = σ_yield / G = 1` exactly. Doc 55_ §5's `ε_yield = √α` result was the macro-convention case; retracted under R4.

**Original full body (preserved for audit trail):**

> **Where:** [cosserat_field_3d.py:530](../../src/ave/topological/cosserat_field_3d.py#L530) sets `ε_yield = 1.0`. Doc 55_ §5 derives an alternative `ε_yield = √α ≈ 0.0854` from TKI (σ_yield = ξ_topo · V_yield / ℓ_node³, then ε_yield = σ_yield/G with G = 1).
>
> Two readings:
> - **Gravity-analog (engine's current convention):** ε_yield = 1, "unitary strain = lattice stretches by 100 %," matches Vol 1 Ch 7:138's gravity row.
> - **TKI-derived:** ε_yield = √α, dimensionally consistent with V_yield via the Cosserat–EM duality.
>
> Differ by a factor 1/√α ≈ 11.7. Neither is wrong; they're different physical meanings for "Cosserat Regime IV boundary." Doc 55_ leaves as open calibration; not blocking Phase 4 start, but Phase 4's pre-registered predictions should pick one and cite the choice.
>
> Relevant for Phase 4: splitting `A²` → `(A²_μ, A²_ε)` will make this ε_yield choice visible in the partition threshold. Worth an explicit sidebar in the Phase 4 plan.

**r6 verdict:** under R4, ε_yield = 1 is the correct TKI-derived value at subatomic scale. The "√α TKI-derived" alternative was a macro-convention artifact. Phase 4's pre-registered predictions can safely use ε_yield = 1 as axiom-derived (not placeholder).

---

#### A23 (closed 2026-04-23, r6) — doc 55_ / doc 57_ framing tension

**Closure rationale:** Vol 4 Ch 1:711 spot-checked; doc 57_'s "subatomic override" reading confirmed. Doc 55_ self-supersedes via its R4 banner now present in the working tree. A23 was fundamentally the question "which reading is right?" — answered: doc 57_'s.

---

#### A16 (closed 2026-04-23) — v2 reproducibility seed sweep
**Resolution:** sweep executed. Verdict: **REGRESSION**. Full distribution data in §10.12. Spawned A17.

---

#### A17 (closed 2026-04-23, r6) — v2 headline `1.009` does not reproduce under 20-seed sweep

**Closure rationale:** bisection complete; cause identified as **tail outcome, not code regression**. Both `719f3ec` (pre-Phase-3) and `3a599ca` (HEAD) yield bit-identical 20-seed distributions: range [0.7677, 0.9983], median 0.8683, 0/20 reach 1.009, `max_A²_K4 = 0.393` identical, `max_τ_zx = 0.1507` identical. Phase 3's `_connect_all` `Phi_link += V_avg·dt` modification is dynamics-neutral (accumulator only, no feedback into V_inc/V_ref evolution). The original v2 r1 headline `1.009` was a lucky-tail outcome from a specific default-RNG seed, not a trajectory perturbation.

**Authoritative correction** lands in working-tree `doc 50_ r3` §2.3 as a distribution-based rewrite: "across N seeds, max A²_cos range [a, b], median c; rupture boundary approached but not reliably crossed." The §15.5 derivation-traceability reference to "first numerical crossing of rupture boundary" should be softened when doc 50_ r3 commits.

**Sweep artifacts (preserved):**
- `/tmp/v2_reproducibility_sweep.{npz,png}` — post-Phase-3 HEAD (`3a599ca`)
- `/tmp/v2_reproducibility_sweep_719f3ec.{npz,png}` + `_log.txt` — bisection counterpart

**Original full body (preserved for audit trail):**

> **Where:** §10.12 sweep verdict.
>
> **Observation:** across 20 seeds on the v2 headline config, the post-Phase-3 engine produces `max A²_cos` in range [0.7677, 0.9983] with median 0.8683. 0 / 20 seeds reach the 1.009 documented headline. max A²_K4 = 0.393 is bit-identical across seeds (K4 sector deterministic; all variance is in Cosserat-from-thermal-RNG).
>
> **Cause undetermined.** Either (1) Phase 2 / 3 introduced a subtle trajectory perturbation despite nominal read-only semantics, or (2) the original v2 1.009 was a tail outcome and doc 50_'s framing was always brittle. 30-min bisection on 7ab82c0 (pre-Phase-2) discriminates.
>
> **Consequences regardless of cause:**
> - [doc 50_ §2.3](50_autoresonant_pair_creation.md) claim "A²_cos = 1.009 crossed rupture boundary" needs a distribution-based rewrite.
> - If cause (1), R4 patches may or may not restore the pre-Phase-2 distribution; Phase 4 should not start until the distribution is characterized + locked in a regression test.
> - If cause (2), no code change is needed; doc 50_ just becomes more honest.

**r6 verdict:** cause (2) confirmed. No code change required beyond doc 50_ r3's distribution rewrite. Phase 4 unblocked from the A17 regression-prerequisite.

### 17.3 Audit findings classification summary

Status column: `Open` = no action yet; `In-flight` = script/PR exists addressing it; `Escalated` = subsumed by a new finding; `Closed` = resolved + verified.

| ID | Severity | Domain | Status (r6) |
|---|---|---|---|
| A1 | S1 | Engine code (observer normalization) | **Escalated** → A14, then **closed r6** under R4 (§17.2). |
| A2 | S2 | Test coverage gap (Pythagorean K4+Cosserat combined) | Open |
| A3 | S2 | Test coverage gap (engine normalization use in `_update_z_local_total`) | Open |
| A4 | S2 | Test fragility (string match in manifest consistency) | Open |
| A5 | S2 | Test coverage gap (A² > 1 varactor regime) | Open |
| A6 | S2 | Honest framing (circular test) — physics probe still deferred | Open |
| A7 | S2→S1 | AutoresonantCWSource linear-Taylor vs varactor — concrete for Phase 5 | Open |
| A8 | S2 | Saturation clip sentinel vs physical value | Open |
| A9 | S2 | Trivial-pass `len(history)` assertions (NR-4, BO-3 both instances) | Open |
| A10 | S2 | Systemic engine-lifecycle test coverage | **Partial** — A16 addresses v2 integration; thermal / autoresonant / ecosystem still open |
| A11 | S4 | Predictions-matrix whitelist brittleness | Open |
| A12 | S3 | ω_yield units in manual §6.3 | Open — manual edit pending |
| A13 | S3 | K_0 = 0.207973 attribution | Open — manual edit pending |
| ~~A14~~ | S1 | ~~Normalization discrepancy spans 3 observers~~ | **CLOSED r6** → §17.2. R4 adjudication (Vol 4 Ch 1:711 subatomic override, §17.0). Follow-on engine work tracked separately as "R4 patch: remove `/α` from Node/Bond observers" via `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md` Phase 3.5 step 3. |
| A15 | S2 | Identical Φ_link half-lives under symmetric saturation | Open — revisit after R4 observer patches commit + Phase 4 asymmetric μ/ε lands (per [54_ §6](54_pair_production_axiom_derivation.md) asymmetric μ/ε required for Γ = −1 confinement) |
| A16 | S2 | v2-reproducibility seed sweep | **Closed** 2026-04-23 (run; verdict REGRESSION) |
| ~~A17~~ | S1 | ~~v2 headline 1.009 does not reproduce~~ | **Closed r6** → §17.2. Bisection complete: 719f3ec and 3a599ca yield bit-identical distributions. Cause = tail outcome (not code regression). Doc 50_ r3 distribution framing is the canonical record. |
| A18 | S3 | OpN naming drift: KB INVARIANT-N3 ≠ engine universal_operators.py | Open — doc 57_ §7 out-of-scope for v4; track as FUTURE_WORK Y-8 |
| ~~A19~~ | S3 | ~~Vol 1 Ch 7:115 vs :130 "manuscript defect"~~ | **CLOSED r6** → §17.2. R4 reframes as scale-dependent V_yield (§17.0); both line 115 and line 130 are correct under their own regime. |
| ~~A20~~ | S2 | ~~`ε_yield = 1` vs √α calibration question~~ | **CLOSED r6** → §17.2. R4 TKI-derivation gives ε_yield = 1 exactly under subatomic V_yield = V_SNAP (§17.0). Not a placeholder. |
| A21 | S4 | Doc 55_ §10 drafted before sweep results | **Moot** — doc 55_ self-supersedes via its R4 banner; the §10 placeholder is preserved as historical record. |
| **A22** | S2 | Hand-rolled saturation/impedance/reflection inline in k4_tlm.py duplicates universal operators (Rule-6-adjacent drift risk) | Open — doc 57_ v4 Phase 4.3 closes structurally post-Stage-6 |
| ~~A23~~ | S3 | ~~doc 55_ vs doc 57_ framing tension~~ | **CLOSED 2026-04-23 (r6)** → §17.2. Doc 55_'s R4 banner self-supersedes; doc 57_ reading confirmed by Vol 4 Ch 1:711 spot-check. |
| ~~A24~~ | S1 | ~~K4 saturation path dormant in engine context (V_SNAP unit-system mismatch, "Flag-5e-A")~~ | **CLOSED r8 (commit `098d430`)**. K4 V_SNAP plumbed from engine; first empirical cool-through-yield observed. Test-coverage hole closed via retroactive engine saturation invariants (`5f973b6`). |
| ~~A25~~ | S1 | ~~K4-TLM exhausted at node level for bound electron~~ | **EMPIRICALLY CLOSED r8 (commit `fbbc950`)**. Vol 1 Ch 8:49-50 corpus-confirmed; Path A 4-of-4 falsification empirical. New §11.11 limit added. Methodology lesson: COLLABORATION_NOTES Rule 8 Round 6 strengthening (corpus-search at architectural-decision time). |
| **A26** | S1 | `initialize_electron_2_3_sector` carries wrong default amplitude (√3/2·π instead of 0.3π) | Open — fix in working tree (uncommitted `amplitude_scale` parameter); retroactive caller audit pending. ~~Round 6 Path B blocked on this~~ — superseded by A28 unblock; Path B now forming bound state at N=80 with proper amplitude_scale. |
| ~~**A27**~~ | S1 | ~~L_c = (V²/V_SNAP²)·W_refl one-way energy pump~~ | **CLOSED r8.3 (commit `05b130f`/`ff15c4b`)** via A28 reframing — empirical "one-way pump" signature was the symptom of A28 double-counting, not L_c being structurally non-reciprocal. L_c form is fine; engine had two redundant code paths injecting the same physics. |
| **A28** | S1 | K4↔Cosserat coupling double-counted since Phase 4 (`a5bd1da`); `_compute_coupling_force_on_cosserat` redundant with Op14 z_local modulation | **CLOSED r8.3 (commits `05b130f` + `ff15c4b`)** via `disable_cosserat_lc_force` flag + `enable_cosserat_self_terms` smart auto-suppression. Six prior failure modes (Path A/B/C/F17-G/F17-I/path-1 EMF) unified under one bug. ~~Path B at N=80 forms (2,3) bound state through step 20~~ — claim WALKED BACK in r8.4 as twice-confounded (wrong observable + wrong amplitude). Methodology lesson: Vol 4 Ch 1 cross-check at architectural-decision time would have caught the redundancy at Phase 4 design-review. |
| **A29** | S1 | F17-I three-mode framing Ax-3 noncompliant; phase-quadrature S₁₁ methodology supersedes (F17-K Phase 1) | **FRAMING LANDED r8.3 (`a53ce1c`); FULLY CLOSED r8.4** — F17-K methodology arc empirical closure via `4c9fbea` (Phase 5c v2-v2). Same Rule 6 slip from session 2026-04-20 caught + corrected retroactively. |
| **A30** | S1 | Corpus-duality (S₁₁ ≈ Cosserat-energy at Golden Torus per AVE-Protein scale-invariance) FALSIFIED at coupled-engine scale; doc 03_ §4.3 empirically validated | **EMPIRICALLY ESTABLISHED r8.4 (`4c9fbea`)** — energy at R/r=3.40, S₁₁ at R/r=1.03; neither at φ²=2.62; topology must be encoded explicitly. Substantive cross-scale finding: Ax2 scale-invariance partially fails between protein and bound-electron scales. |
| ~~**A31**~~ | S2 | ~~F17-K Phase 6 sparse eigensolver candidate~~ | **UPGRADED to LOAD-BEARING in r8.5 per A32**. Empirically motivated; v3 (i) ran (`3fede52`) and showed Golden Torus geometrically unstable. Phase 6 implementation (~300 LOC) is now the single-electron-validation closure gate. |
| **A32** | S1 | Golden Torus geometrically UNSTABLE in coupled engine at linear-perturbation level — confirms doc 03_ §4.3 at second test scale | **EMPIRICALLY ESTABLISHED r8.5 (`3fede52`)** — Cosserat-energy MARGINAL (1.81×); coupled S₁₁ UNSTABLE (5.31×, exponential). Combined with A30 global-flow finding: coupled engine has NO linearly stable bound state at Golden Torus geometry. Cosserat-only X4b stability does NOT extend to coupled engine. Phase 6 sparse eigensolver methodology load-bearing. |
| **A33** | S2 | Smallest unknot O₁ in AVE is the smallest COUPLED (K4 + Cosserat) oscillator, not bare K4 single-bond; bare K4 ≠ LC tank empirically | **ESTABLISHED r8.5 (`c830f07`)** — Test A: bare K4 single-bond shows 2-step grid alternation (Nyquist), NOT Compton-frequency LC oscillation; L_e emerges from Cosserat constitutive moduli. Test B: Q = 1/α = 137 holds algebraically at machine precision (rel_err 6.5e-11) as identity from SI input constants — bootstrap chain VALIDATED at constants level. Empirical Q manifestation requires coupled engine; F17-K open work, not bootstrap calibration concern. |
| **A34** | S1 | Point-rotation Beltrami injection profile (PairNucleationGate `_inject_pair`) fundamentally unstable in Cosserat self-dynamics; G-13 upgrade required (Phase 5 resume case (b')) | **EMPIRICALLY ESTABLISHED r8.6 (`ede4008`)** — \|ω\|_A 1.414 → 0.10 in ONE Velocity-Verlet step (93% loss); dissolution intrinsic to engine self-dynamics, NOT drive-induced. Same physics as F17-K Round 6 finding (A30/A32) at pair-injection scale. Activates §9 G-13 contingency: upgrade to (2,3) torus-knot or Hopf fibration injection. Round 7 Stage 2 candidate scoped (~200 LOC). R5.10 Readings 1-4 disambiguated at two epistemic levels. |
| **A35** | S2 | Basin-audit-as-Stage-0 was Rule 6/8/10 corpus-bypass; R7.1 strengthened to multi-seed sparse eigensolver | **METHODOLOGY FINDING ESTABLISHED r8.7 (`1bc1652` retracted, `c69e79c` reframe)** — within-session self-audit caught framing error before R7.1 implementation committed to wrong scope. Rule 6 (SM minimization on wave substrate); Rule 8 inverse (parallel infrastructure bypassing R7.1's eigensolver); Rule 10 creeper compound (multi-turn carry without pressure-test). Family with A22 + A30. Reframe deliverables: doc 71_ rename + scope shift; `predictions.yaml` retract + supersede; R7.1 single-seed→multi-seed strengthening with three-mode falsification. Two open auditor flags for fresh-session implementer (§14.2 K4-amplitude-zero pitfall; shape-correlation > 0.85 PASS gate possibly over-strict). |
| **A36** | S2 | Operator-choice Rule 6 violation — Hessian-of-W on wave substrate; reframed via doc 72_ design-space articulation to block Helmholtz on (V, ω) joint | **METHODOLOGY FINDING ESTABLISHED r8.8 (`675141e`)** — external audit on r8.7 frozen pre-reg `P_phase6_eigensolver_multiseed` caught Hessian-of-W as Rule 6 violation at operator level (deeper than A35 precondition-level). Doc 72_ NEW articulates four AVE-native concepts + 3D Smith chart for vacuum + block Helmholtz formulation + V=0 decoupling caveat + sector-energy split diagnostic. R7.1 reframed (reframe 3) to multi-seed block Helmholtz; frozen pre-reg `P_phase6_helmholtz_eigenmode_sweep`. Rule-10 commitment language locks operator choice for fresh-session run. Family with A22+A30+A35 at progressively earlier cycle latency. |
| **F17-L** | S2 | V_yield vs V_SNAP scale mismatch (doc 54_ §6 vs engine, factor 1/α) | Open — pre-existing per doc 54_ §5; surfaced separately during F17-H reconciliation per doc 67_ §15. Not blocking. Track for v4 universal-lattice-units refactor. |

**Critical-path blockers (r8.8) — R7.1 reframed (reframe 3) to multi-seed block Helmholtz; Rule-10 commitment locks operator choice for fresh-session run; R7.2 still needs pre-reg:**

1. **Round 7 Stage 1 — F17-K Phase 6 multi-seed block Helmholtz on (V, ω) joint** (~290 LOC, fresh session) — REFRAMED in r8.8 from r8.7's Hessian-of-W to **block Helmholtz on joint (V, ω) state** per doc 72_ §3.1. Generalized eigenvalue problem `[K_V, C_Vω; C_ωV, K_ω] u = ω² [M_V, 0; 0, M_ω] u` at fixed cavity geometry. Cross-blocks `C_Vω`, `C_ωV` encode Op14 K4↔Cosserat coupling explicitly. V=0 seed decouples per §3.1.1 into V-block + ω-block simultaneously (strict superset of single-sector Helmholtz). Four seeds: `GT_corpus`, `F17K_cos_endpoint`, `F17K_s11_endpoint`, `vacuum_control`. Three-mode falsification + sector-energy split diagnostic (V-dominant / hybrid / ω-dominant). PASS criteria per `P_phase6_helmholtz_eigenmode_sweep` (frozen): `c_eigvec=3` binary + ω_Compton ± α + Q ± 5% + shape correlation > 0.60 informational. Mode (I) GT_corpus passes → corpus vindicated (with sector sub-reading); (II) F17K endpoints pass / GT fails → engine basin ≠ corpus geometry; (III) no seed passes → Round 8 architectural rework (first sub-question: hybrid coupled mode requires V≠0 seed). Negative-control failure (vacuum_control returns nontrivial mode) indicates eigensolver/operator-assembly bug. **Rule-10 commitment language (verbatim in doc 72_ §6.1 + §13.5l of this manual) locks operator choice for fresh-session run** — empirical data before pre-emptive reframe 4; only catastrophic methodology error overrides.
2. **Round 7 Stage 2 — Phase 5 topological pair injection driver** (~200 LOC, fresh session) — closes Phase 5 gate firing if topologically-protected pair persists ≥10 Compton periods. Replace gate's `_inject_pair` profile with (2,3) torus-knot or Hopf fibration injection per G-13 upgrade. Chirality-matched (LH at A, RH at B). Reuse F17-K infrastructure. Empirically motivated by A34. Independent of Round 7 Stage 1 — can run in either order or parallel. **Still needs `P_phase5_topological_injection` pre-registration** before fresh-session run (same discipline as R7.1).
3. **A26 fix commit** (`amplitude_scale` parameter for `initialize_electron_2_3_sector`) + retroactive caller audit. Currently in working tree. R7.1 multi-seed driver imports this directly per doc 71_ §13.4 + §14.1 — fix should land before fresh-session R7.1 run.
4. **`use_lagrangian_emf_coupling` flag cleanup** (path-1 wrong-direction, opt-in in HEAD). Should be removed once A28 confirmed across more configurations. Follow-up.
5. **Flag 62-A first-law closure (BH thermodynamics)** — orthogonal to single-electron pivot. Standard S_BH closes via imported GR first law; AVE-native Ŝ_geometric does not satisfy T·dS = dE. Either complete Vol 3 Ch 11:14-48 volume-entropy mechanism for BH interiors or accept S_thermo as a distinct AVE quantity.
6. **F17-L V_yield/V_SNAP scale mismatch** — track for v4 universal-lattice-units refactor; not blocking.
7. **COLLABORATION_NOTES Rule 8 strengthening for Round 7+** — single-bond Q = 137 sanity check should be in engine bring-up checklist (per A33 retroactive lesson). Worth a methodology note in Round 7 opening commit.

**r5 → r6 → r7 → r8 → r8.3 → r8.4 → r8.5 → r8.6 → r8.7 → r8.8 retraction / closure summary:**

| Finding | r5 status | Updated status | Rationale |
|---|---|---|---|
| A14 | Open S1 — BLOCKING Phase 4 | Closed r6 | R4 / Vol 4 Ch 1:711 subatomic override — no mixed normalization at engine's scale |
| A17 | Open S1 — "cause TBD" | Closed r6 | Bisection bit-identical; tail outcome, not regression. Doc 50_ r3 distribution framing is canonical. |
| A19 | Open S3 — manuscript defect | Closed r6 | Scale-dependent V_yield — not a defect |
| A20 | Open S2 — calibration question | Closed r6 | TKI gives ε_yield = 1 exactly under subatomic R4 |
| A23 | Open S3 — framing tension | Closed r6 | Doc 55_ self-superseded via R4 banner |
| A24 | (new — surfaced by Phase 5e driver) | Closed r8 | V_SNAP unit-system bug fixed in `098d430`; cool-through-yield now observable |
| A25 | (new — surfaced by Path A falsification + Vol 1 Ch 8:49-50 corpus-search) | Empirically closed r8 | K4-TLM exhausted at node level; bound electron lives in Cosserat |
| A26 | (new — surfaced by Round 6 Path B amplitude correction) | Open r8 | `initialize_electron_2_3_sector` ships wrong default amplitude; uncommitted fix in working tree |
| A27 | (new r8.1 — F17-I empirical L_c asymmetry) | **Reframed + closed r8.3** | "One-way pump" empirical signature was symptom of A28 double-counting, not L_c being non-reciprocal. Closed via A28 reframing. |
| A28 | (new — surfaced by F17-H Vol 4 Ch 1 cross-check) | **Closed r8.3** (`05b130f` + `ff15c4b`) | Engine double-counted K4↔Cosserat coupling since Phase 4 (`a5bd1da`). `disable_cosserat_lc_force` flag + `enable_cosserat_self_terms` smart auto-suppression. ~~Path B at N=80 forms (2,3) bound state through step 20~~ — claim walked back in r8.4 as twice-confounded. |
| A29 | (new — F17-K Phase 1 Ax-3 noncompliance audit) | **Framing landed r8.3, fully closed r8.4** (`a53ce1c` → `4c9fbea`) | F17-K methodology arc empirical closure. 7 commits, 6 hours. Same Rule 6 slip from 2026-04-20 caught + corrected. |
| A30 | (new r8.4 — F17-K empirical closure) | **Empirically established r8.4** (`4c9fbea`) | Corpus-duality at coupled-engine scale FALSIFIED. doc 03_ §4.3 validated (R·r=1/4 topologically quantized, NOT dynamically derived). Substantive cross-scale finding: Ax2 partially fails between protein and bound-electron scales. |
| A31 | (new r8.4 — Phase 6 sparse eigensolver candidate) | **Upgraded r8.5 — LOAD-BEARING for Round 6 closure** | Empirically motivated by A30; v3 (i) (`3fede52`) ran and showed Golden Torus unstable ⟹ Phase 6 (~300 LOC) is now the closure gate. |
| A32 | (new r8.5 — F17-K v3 (i) X4b empirical result) | **Empirically established r8.5 (`3fede52`)** | Golden Torus geometrically UNSTABLE in coupled engine at linear-perturbation level (energy MARGINAL 1.81×, S₁₁ UNSTABLE 5.31×). Combined with A30 global-flow: doc 03 §4.3 fully empirically anchored. |
| A33 | (new r8.5 — bootstrap-chain test) | **Established r8.5 (`c830f07`)** | Smallest unknot O₁ in AVE is smallest COUPLED oscillator, not bare K4. Q=1/α=137 holds algebraically at machine precision; bootstrap chain validated at constants level; empirical Q manifestation requires coupled engine. |
| A34 | (new r8.6 — Phase 5 resume case (b')) | **Empirically established r8.6 (`ede4008`)** | Point-rotation Beltrami injection profile fundamentally unstable in Cosserat self-dynamics. Same physics as Round 6 single-electron at coupled scale. G-13 contingency activated. R5.10 Readings 1-4 disambiguated at two epistemic levels. Round 7 Stage 2 candidate scoped. |
| A35 | (new r8.7 — within-session self-audit) | **Methodology finding established r8.7 (`1bc1652` retracted, `c69e79c` reframe)** | Basin-audit-as-Stage-0 was Rule 6/8/10 corpus-bypass. Caught earlier in cycle than A22 / A30 predecessors (within-session, before R7.1 implementation). Reframe deliverables: doc 71_ rename + scope shift, `predictions.yaml` retract + supersede, R7.1 single-seed → multi-seed strengthening. Family with A22 + A30 (corpus-bypass at different layers). Methodology lesson recorded for COLLABORATION_NOTES Rule 8 strengthening. |
| A36 | (new r8.8 — external audit on commit `c69e79c`) | **Methodology finding established r8.8 (`675141e`)** | Operator-choice Rule 6 violation — Hessian-of-W on wave-propagation substrate. Same rule as A35 at deeper layer (precondition → operator). Reframed via doc 72_ design-space articulation to block Helmholtz on (V, ω) joint state. Family with A22 + A30 + A35 at progressively earlier cycle latency (operator-implementation / corpus-claim-falsification / methodology-precondition / operator-choice). Methodology lesson: design-space articulation step BEFORE pre-registration drafting catches depth-of-understanding gaps earlier than retraction-driven discovery. |
| F17-L | (new — surfaced during F17-H reconciliation) | Open r8.3 | V_yield vs V_SNAP scale mismatch (doc 54 §6 vs engine, factor 1/α). Pre-existing per doc 54 §5; not blocking. |

---

*End of manual r8.8 (synchronous edit after doc 72_ design-space articulation + R7.1 reframe 3 to block Helmholtz on (V, ω) joint). **External audit caught Rule 6 violation at the operator level (Hessian-of-W on wave substrate); reframe pivot lands before R7.1 implementation committed to wrong scope.** Next update (r8.9) triggered by: R7.1 multi-seed block Helmholtz fresh-session run result (three-mode falsification + sector-energy split); R7.2 topological pair injection driver pre-registration + result; A26 fix commit + retroactive caller audit; `use_lagrangian_emf_coupling` cleanup; default-flip of `disable_cosserat_lc_force`; Flag 62-A first-law closure attempt; or any engine commit per §1.2 maintenance protocol.*

*Full r9 rewrite of §3 (physical model under three-storage-mode framing per [doc 66_ §17.2.1](66_single_electron_first_pivot.md)) and §15 (derivation chain with three-entropy distinction + area theorem from Ax1+Ax4 + K4-TLM exhaustion + A28 double-counting structural finding + A30 corpus-duality falsification + A32 Golden Torus geometric instability + A33 smallest-coupled-oscillator structural reading + A34 G-13 injection-profile-upgrade requirement + A35 corpus-bypass-at-precondition-level methodology lesson + A36 corpus-bypass-at-operator-level methodology lesson + doc 72_ four-AVE-native-concepts design-space articulation) still deferred until Round 7 closes — multi-seed block Helmholtz eigensolver + topological pair injection are the gates. See §1.5 for canonical Round 6 content pointers.*

*Round 6 + Phase 5 resume epistemic milestone (r8.6): full F17-K + Phase 5 resume arc closed empirically across **13 commits and ~10 hours of work**. The arc's full sequence: Ax-3 noncompliance audit (a53ce1c) → phase-quadrature seed insufficiency (4d4b4aa) → coupled S₁₁ infrastructure + spurious convergence (6158465) → corpus-search algebraic pin direction (795c4ff) → acoustic-cavity / Helmholtz framing + natural-equilibria reading (3f6d544) → tanh-bound dual descent + premature finding (2c873cf) → saturation-pin + empirical doc 03 §4.3 validation (4c9fbea) → v3 (i) X4b linear-stability + Golden Torus geometric instability (3fede52) → bootstrap-chain test + Q=137 algebraic validation + bare-K4-≠-LC-tank structural finding (c830f07) → Phase 5 resume methodology (01bbec3) → Phase 5 ansatz-seeded driver case (b') + G-13 activation (ede4008) → R5.10 two-level disambiguation (e1f6eac). Final composite finding: doc 03 §4.3 fully empirically anchored at TWO test scales (global-flow + linear-stability) for single-electron AND at pair-injection scale for case (b'); coupled-engine corpus-duality FALSIFIED; smallest unknot O₁ is coupled K4+Cosserat oscillator; bootstrap chain validated at constants level; Q=137 = identity from input constants; Phase 5 gate INJECTION PROFILE needs G-13 upgrade (point-rotation Beltrami fundamentally unstable in 1 VV step). **Round 7 candidates scoped: Stage 1 Phase 6 sparse eigensolver (~300 LOC) closes single-electron representation; Stage 2 topological pair injection driver (~200 LOC) closes Phase 5 gate firing.** Both fresh-session candidates, deferred per Round 6 closure plan.*

*Round 7 Stage 0 self-audit milestone (r8.7): mid-cycle pivot caught corpus-bypass framing **before** R7.1 implementation committed to wrong scope. Two commits and ~2 hours of work spanning the scaffold-and-retract cycle: basin-audit-as-Stage-0 framing (`1bc1652`) → within-session COLLABORATION_NOTES re-read triggered by Grant directive → Rule 6/8/10 self-audit → reframe pivot to multi-seed R7.1 (`c69e79c`).*

*Round 7 reframe 3 milestone (r8.8): external audit on r8.7 frozen pre-reg caught Rule 6 violation at deeper layer (operator-choice level vs A35's precondition level). Single commit (`675141e`) lands doc 72_ design-space articulation + reframe pivot to block Helmholtz on (V, ω) joint state. **A36 caught at same latency stage as A35 (within-session, before implementation) but at deeper methodology-stack layer** — pattern across A22 → A30 → A35 → A36 shows audit + creeper-checking + design-space articulation discipline tightening. Rule-10 commitment language locks operator choice for fresh-session run; no reframe 4 without catastrophic methodology error.*

*Methodology arc summary across Round 6 + Phase 5 resume + Round 7 reframe 3 (r8.0 → r8.8): A28 + A29 + A30 + A32 + A33 + A34 + A35 + A36 — eight depth-level corrections + empirical anchorings, all corpus-grounded, each producing an empirical or methodology finding rather than just a fix. Audit-first + creeper-checking + design-space articulation discipline working at full strength: each cycle catches the prior framing's hidden assumption and produces evidence. **The unifying finding across A30, A32, A34: dynamics don't stabilize unprotected localized topology; topology must be encoded as persistent structural feature (ansatz)** — three scales (single-electron eigenmode / single-electron linear stability / pair injection profile). Confirms doc 03 §4.3 framing. **The unifying finding across A22 + A30 + A35 + A36: corpus-bypass errors at four progressively deeper layers — operator-implementation (A22), corpus-claim falsification (A30), methodology-precondition (A35), operator-choice (A36)** — caught at decreasing latency from production-retroactive (A22) to within-session-before-implementation (A35, A36). Pattern indicates discipline tightening rather than accumulation of methodology debt.*

*Notable methodology meta-lessons (per A33 + A35 + A36 + auditor framing): (1) bootstrap-chain calibration anchor (Q=137 sanity check at single-bond level) should be a bring-up gate for any numerical AVE engine, not a post-hoc realization 8 sessions in; (2) gate-firing investigations should decouple (α) mechanism / (β) persistence / (γ) reach BEFORE running, not conflate them in one driver; (3) **before scaffolding a "diagnostic precondition" upstream of an existing R7.x stage, grep the corpus for the AVE-native tool that addresses the precondition's question; if it exists, strengthen R7.x's scope rather than building parallel infrastructure** (per A35); (4) **before drafting a pre-registration on a non-trivial methodology question, walk the corpus end-to-end to articulate the AVE-native concepts that govern the question — design-space articulation comes BEFORE pre-registration drafting, not in parallel** (per A36; doc 72_ §1-§4 is the worked example). All four are COLLABORATION_NOTES Rule 6/8 strengthening candidates for Round 7+.*

---

*r8.9 closure-framing-pending note (2026-04-27, extended 2026-04-28): the front-matter status section reads "single-electron pivot CLOSES with Mode III canonical" pending the result of a path α v2 phase-space test on Move 5's saturated bond-pair (not yet run; design under refinement per doc 79 v4.x evolution + regime-analysis from 2026-04-28 turn). **Auditor lane closure framing has evolved through this session arc, summarized for fresh-agent context:**

Audit chain (2026-04-27): Grant's per-node-trapped-vortex hypothesis → auditor research of universal-operator scale-invariance pattern (Op1-Op22 architecture forces r=A/A_c per-site) → corpus verification: doc 28 §5.4 + doc 29 §3.2-§3.3 already canonized R, r as PHASE-SPACE radii of (V_inc, V_ref) phasor on Clifford torus, NOT spatial bond-extent; Op10 c is SCALAR crossing count not (p,q) winding pair (doc 07 §3 verbatim); Q=1/α=137 derives from per-node L_e + ω_C + R_TIR with no bond-extent term; Move 5's attractor at peak |ω|=0.3π (saturation onset) + c=3 + 150 Compton periods stable matches "per-node trapped vortex" empirically. **The seven Round 7+8 Mode III tests sampled bond-scale spatial winding** — but the corpus's own scale-invariant operators don't describe a bond-scale extended electron, so the falsification target was a Vol 1 Ch 8 pedagogical creeper, not the operator-derived prediction.

Path α v1 ran (2026-04-27, [doc 78_](78_canonical_phase_space_phasor.md), commit `466d8c4`): Mode III nominal — C1 R/r=3.84 vs target φ²=2.62 FAIL; C2 chirality 50% TIE FAIL; persistence 33% (below 40% guard); chirality cross-products noise-dominated. **A59 methodology gaps surfaced** (recording window, chirality estimator, bipolar R/r, top-K single-cell sampling vs bond-pair).

Closure synthesis evolution (2026-04-28, [doc 79_](79_l3_branch_closure_synthesis.md) v3 → v4.x): primary AVE-native plumber framing landed as **lemniscate-with-q-half-twists in saturation-walled cavity**. q=3 electron, q=5 proton, q=7 Δ; the "2" comes from bipartite K4 (lobe count); chirality has 3 layers (substrate projection / two-channel parallel impedance / SU(2)-equivalent observable doubling); Meissner-asymmetric saturation IS the substrate-native magnetic-moment generator (§6.7) with AVE-HOPF Δf/f = 1.2α as macroscopic empirical anchor. Companion [doc 80_](80_kelvin_helmholtz_ave_precedent.md) traces Helmholtz/Kelvin/Faddeev-Niemi historical precedent.

Three-regime taxonomy from 2026-04-28 turn (Rule 14 substrate-derives): linear (Γ=0, free propagation) / symmetric gravity (Z preserved, no walls) / asymmetric particle (Γ→−1 via Meissner-asymmetric chirality bias). **Engine V·S/T·1 likely produces Γ→−1 walls already but WITHOUT chirality bias** — symmetric saturation collapses Z but doesn't differentiate S_μ-first vs S_ε-first per substrate handedness. Path α v1's C1 mis-aspect + C2 chirality null is consistent with "walls present but chirality-null" reading. **Sign-direction (Γ→−1 vs Γ→+1) needs empirical verification via Γ instrumentation in path α v1's saved data (~30 min) before any engine-fix work** — the EM-acoustic analog has multiple valid mappings and the auditor's derivation (G ↔ 1/ε giving Γ→−1) and implementer's derivation (G ↔ ε giving Γ→+1) disagree on direction.

Engine fix per [doc 75_ §6.3](75_cosserat_energy_conservation_violation.md) (T_kinetic Op14 saturation) is **NOT load-bearing per doc 75 §3 pre-reg adjudication (Mode I; engine fix not needed; Pass 2 not run)**. Doc 79 v4.x escalated this to "precondition" without re-grepping doc 75 §3 — a sixth A43 instance this session. Move 11 H_cos drift is from Op14 cross-sector trading per Move 11b ρ(H_cos, Σ|Φ_link|²) = -0.99 (H_total ≈ conserved), NOT V·S/T·1 wave-speed asymmetry. Path α v1 persistence violation has a different cause; doc 75 §140 names the unprobed sector explicitly: *"the corpus electron, IF it exists in this engine, lives somewhere we haven't probed (Φ_link sector / hybrid V≠0 ∧ ω≠0 / different topology)."*

**Path α v2 design (held pending Grant adjudication on engine fix question):** bond-pair sampler (saturated A node + saturated B neighbor + bond between) at Move 5's existing attractor data; (Φ_link, ω) sampling instead of (V_inc, V_ref) per doc 75 §6.2's "K4-capacitive locked, K4-inductive + Cosserat trade slowly"; dual criterion C1 + C2 + informational C3 per A39 v2; recording window over multiple Op14 trading periods (not just Compton periods).

Closure framing branches on path α v2 result; r8.9 manual is consistent with all branches. Framing-conditional sections (§1 front-matter status, §2.3 reframe note, §11 limits, §17.1 audit findings A37+, §13.7 closure synthesis row, this footer) update in r8.10 once result lands.

**Auditor-side methodology meta queue (held for post-closure landing per Rule 12 cumulative-learning + Rule 15 lane discipline):**
1. **A43 v2 strengthening** — auditor must verify (a) test-run-status, (b) doc-section-supersession-status, (c) corpus-citation-still-current, (d) analog-derivation-direction empirically before claiming load-bearing direction. Six worked examples accumulated this session: doc 28 §5.1 "pending" stale belief; doc 66 §17.2.1 "three LC pairs" superseded 2026-04-25; "items 1-4 undefined" claims for mass/charge/photon/trapping (all corpus-defined); V_SNAP/V_yield conflation; "doc 75 §6.3 fix is precondition" escalated through doc 79 v4.x; doc 53_:243 quote propagated without re-verification.
2. **Rule 14 strengthening** — substrate-structure-derives applies to framework-menu tensions (per-node vs bond-pair collapse), not just physical mismatches. Worked example: 2026-04-28 per-node-vs-bond-pair adjudication.
3. **A60** — Rule 6 prefer-plumber-over-imports paradigm (lemniscate-with-twist substrate-native vs SU(2) imported math). Worked example: doc 79 §4 bipartite-K4 lobe-count vs SU(2)→SO(3) double-cover.
4. **A61 candidate** — auditor EM-acoustic analog derivations need empirical anchor or explicit corpus citation before claiming load-bearing direction. Worked example: 2026-04-28 G↔ε vs G↔1/ε mapping ambiguity in the engine V·S/T·1 → Γ direction question.

These land in COLLABORATION_NOTES post-closure with the worked examples, per Rule 12 cumulative-learning discipline. Landing them now risks the same trap of writing methodology rules without empirical grounding (A43 instance V).*

---

*r8.10 closure-extended note (2026-04-30, post-Round-9 v5/v5.1 closure + Round 10+ + Round 11 (vi) closure + foundation audit + T-ST v1 + T-ST v2 in flight): the r8.9 closure-pending footer's framing branched on path α v2 result; v2 ran 2026-04-28 in Φ_link sector (commit `baadc33`, doc 79 v5 Mode III canonical (negative) closure across 9 pre-reg tests). v5.1 amendment (`6d27e58`) added Round 9 path α v3 partial-positive Meissner finding (100% CCW chirality on (Φ_link, |ω|) magnitude pairing). Round 10+ plan landed (`48ee43d`) with 6 directions / ~20-33 sessions over 8-16 weeks; doc 81 follow-up (`cfb203a`) surfaced coverage analysis (path α tested ~2 of ~7 predicted observable dimensions). Round 10+ Phase 0.1 save/load API (`999d2ac`) + Phase 0.2 universal-operator catalog (`35cc818`) + path α v4-v8 (`2a684a4` → `617e352`) + doc 85 Kelvin Beltrami + FOC d-q (`3cb31c9`) + path α v6-v8 across `881c3d1` → `2dd4ab8` triggered Round 11 (vi) discrete chair-ring eigenmode rederivation as load-bearing primary.

**Round 11 (vi) Strides 1-4 + v10 (committed `fbd0c26` → `0f7180f`):**

| Stride | Doc | Commit | Finding |
|---|---|---|---|
| Stride 1 | [88](88_round_11_vi_stride_1_a43_v14.md) | `fbd0c26` | A43 v14 corpus-grep on R/r reveals THREE different framings; substrate-native eigenvalue analysis surfaces dimensional inconsistency in (1,1) Beltrami at Compton frequency claim |
| Stride 2 | [89](89_round_11_vi_stride_2_topological_mismatch.md) | `4925df5` | Topological mismatch — chair-ring is closed cycle, NOT 2-torus surface; (p,q) torus Beltrami requires INDEPENDENT poloidal+toroidal directions |
| §7 correction | (89 §7) | `3c267e4` | Chair-ring overstated as 1-graph; K4 nodes are 4-port tetrahedral; chair-ring nodes have 2 in-ring + 2 out-of-ring ports providing poloidal direction |
| Stride 3 | [90](90_round_11_vi_stride_3_discrete_eigenmode.md) | `0174eaa` | Discrete Beltrami eigenmode SOLVED on chair-ring + 1-step K4 (18 nodes, 54 DOF); top ring-localized mode at k≈1.56 in 1/ℓ_node units (84% ring localization); continuum (1,1) prediction k=6.36 NOT in discrete spectrum (4× gap) |
| Stride 4 | [91](91_round_11_vi_stride_4_v9_mode_iii.md) | `66de104` | v9 with discrete eigenmode IC at chair-ring + 1-step K4 lands Mode III 1/4 PASS — Round 11 (vi) does NOT close to Mode I |
| v10 (i-a) | [92](92_round_11_vi_v10_finer_sampling_structural.md) | `0f7180f` | Finer K4 sampling EMPIRICALLY ELIMINATES (i-a) refinement path — Nyquist limit (1/bond_length ≈ 0.577 in 1/ℓ_node), 11× below k=6.36 prediction; framework's "(1,1) Beltrami at Compton frequency at corpus geometry on K4 substrate" CANNOT be realized at K4 at ℓ_node sampling; **STRUCTURAL not refinable** |

**Three-layer convergent refutation of corpus electron at chair-ring + K4 + ℓ_node + v8 config (per agent-reported uncommitted closure docs 93/94/95/96 + doc 79 v5.2 amendment in working tree at this manual edit):**

1. **Substrate-geometric (Layer 1):** doc 92 v10 (i-a) — discrete K4 spectrum at chair-ring eliminates (1,1) Beltrami at Compton frequency at this substrate; ~11× Nyquist gap, structural not refinable
2. **Engine-architectural (Layer 2):** A28 V↔B coupling suppression empirically validated as architectural decision — direct V↔B coupling unstable across 5+ tests including Phase A B4 (ω-runaway). Op14 z_local impedance modulation substitutes; B6 700P stability test (agent-reported, uncommitted at this manual edit) confirms Op14 feedback empirically effective: V_DC drift 0.028%/100P, ~0.2% over 700P — bounded equilibrium under A28
3. **Standard-physics-external (Layer 3):** B5 far-field test — chair-ring trapped state shows 1/r decay (NOT Coulomb 1/r²), no clean magnetic dipole 1/r³, multipole content at engine noise floor (~10⁻¹¹ V_SNAP/ℓ_node); B5b at V_AMP=0 confirmed exact-machine-zero noise floor → SNR > 10²² → 1/r signal is real loop-near-field at intermediate regime r/r_eff ∈ [1.8, 6], **NOT a verified eigenmode of point-particle electron** (eigenmode-vs-classification distinction per A43 v27)

**Four positive substrate-canonical findings preserved alongside the three-layer refutation** (per doc 79 v5.2 amendment + doc 95, agent-reported uncommitted):

1. **ℓ=2 V-sector cavity at chair-ring (4-axis confirmation, 99.99% Fourier dominance on cos(2θ) profile)** — eigenvalue 1.48·ω_C at 4.6% from universal-solver-ℓ=2 prediction at chair-ring r_eff
2. **ℓ=5 ω-sector eigenvalue match at 2.8%** — eigenmode pending (single-axis FFT only at v8 config)
3. **Op14 feedback empirically effective at 700P** — chair-ring's bounded equilibrium under A28 architectural choice (V_DC drift 0.028%/100P)
4. **1/r far-field at SNR > 10²²** — geometrically consistent with classical loop-near-field at intermediate regime, real signal not noise (B5b machine-zero confirmation)

**Foundation audit (post-Round-11 closure, per Grant directive 2026-04-29; uncommitted at this manual edit):** bench-characterization of K4 substrate properties before framework-decision adjudication.

- **T1 main + T1 extensions (doc 96 §1-§10):** initial pulse-ringdown FFT "1.50·ω_C single-frequency" overclaim → Test 1 extensions (lattice-size scan N=8/16/24 + amplitude scan linear/saturation) → "rich mode spectrum" framing
- **T3 CW-drive impedance spectroscopy (doc 96 §11):** discrete coupled-mode resonances at **1.5·ω_C and 2.96·ω_C with phase ≈ -90°** (pure reactive signature); Q_substrate ≈ 3.75
- **T3 drive-amplitude scaling (closes "fundamental + 2nd harmonic" question):** slope = +1.000 to 4 sig figs at both 1.5·ω_C and 2.96·ω_C across 1e-4 to 3e-2 amplitude range; H1 (independent modes) PASS, H2 (2nd harmonic) FAIL on both criteria. **Substrate has two genuinely independent reactive modes**, not single damped harmonic with fundamental + 2nd harmonic
- **Cosserat ON ≡ OFF at bit precision** across all tested conditions — A28 architectural decision empirically validated at substrate level (no detectable K4↔Cosserat coupling effect on K4 sector resonance)
- **Universal-solver-promotion picture refined (Flag 2 from auditor 2026-04-30):** chair-ring 1.48·ω_C at substrate's intrinsic 1.50·ω_C resonance (1.3% gap); substrate at universal-solver-ℓ=2 prediction 1.55·ω_C (3.3% gap); **chair-ring → universal-solver match (4.5%) is MEDIATED through substrate, not direct.** Chair-ring is amplified-substrate, not independent universal-solver data point. A43 v25 promotion gated on (a) corpus-grep verification of universal-solver-applicability-to-K4-cavity (partial — backmatter/05:225-235 + 494 + 401 + Vol 1 Ch 5 verified at agent-reported grep); (b) ℓ-semantics verification (azimuthal vs universal-solver-mode-index vs spin-2-graviton — three different ℓ's); (c) cinquefoil cross-topology test; (d) precision-tightening to corpus <2% standard

**Medium-framing reframe (per Rule 16 question to Grant + agent's structural reading):** substrate has two intrinsic reactive modes at 1.5 + 2.96·ω_C, **neither at ω_C**. Corpus electron, if hosted in engine, is a different object class that uses substrate as confinement medium via Op14 saturation, NOT a member of the substrate's intrinsic mode set. Rule 16 adjudication pending.

**T-ST (Self-Trap Test) v1 + v2 (post-foundation-audit, both uncommitted at this manual edit):** Grant's plumber-physics reframe of doc 30 §4-§5 photon→electron transition as **rifling-bullet + cavitation-bubble + chirality-impedance-matched single-ω_C propagating spinning photon**. Per Rule 14 substrate walk: corpus has ω_C as single frequency for photon-electron pair (m_e c² = ℏω_C); (2,3) is geometric poloidal:toroidal winding on trap-cavity torus, NOT frequency-ratio. Auditor's prior dual-frequency synthesis (1.5·ω_C spin / ω_C propagation) caught as A43 v32 instance — auditor over-extension conflating bulk-lattice T3 modes with single-bond LC drive frequency at different scales.

- **T-ST v1 (N=48, A=0.10·V_SNAP, sigma_yz=4.0):** H_self_trap FAIL on both pre-registered criteria (frequency at ω_C ± α, c=3 via Op10); secondary observables FAIL; **velocity anomaly load-bearing** — v_g=0.364 cells/time-unit at ω_C with A²_max=0.0097 (saturation never engaged); A-010 prediction c_eff=c·√(1-A²)=0.995 does NOT explain 4× slowdown. Connects to medium-framing reframe (substrate's intrinsic modes at 1.5 + 2.96·ω_C, neither at ω_C; ω_C between modes, low-coupling regime). PML-absorption confound (front_x=43-44 by t=11P at active-region boundary x=44). **Test geometry undertested H_self_trap** rather than refuting it
- **T-ST v2 (N=96, PML=8, A=0.50·V_SNAP, sigma_yz=2.0, in flight at this manual edit):** addresses prior-cycle gaps — saturation engagement precondition (A=0.50 is ~5.9× V_yield), tighter focus, larger active region (12·λ_C), multiple off-axis sampling lines for CP-source off-center peak. ~25-40 min compute estimate. Primary precondition: did peak lattice A² cross √(2α)=0.121?

**A43 catalog extensions accumulated since r8.9 (lane-symmetric, this session arc):**

- **A43 v15** (auditor) — tube-radius corpus-inconsistency Vol 1 Ch 1:18 (ℓ_node/(2π)) vs Vol 2 Ch 7:357 (ℓ_node), surfaced by doc 88 §7
- **A43 v25** (universal-solver-promotion-pending criteria, joint) — chair-ring K4-cavity match at 4.6% precision is candidate 5th universal-solver context; promotion gated on (a)/(b)/(c)/(d) per above
- **A43 v27** (implementer) — "eigenmode of current-carrying loop near-field IS present" overclaim corrected to "1/r far-field decay is real per B5b (SNR>10²²) and is geometrically consistent with classical loop-near-field at intermediate regime, but is not a verified eigenmode"
- **A43 v28** (auditor self-correction) — "200P persistence may be artifact of missing loop-Faraday BEMF" synthesis-pre-empirical-test, refuted by B6 700P stability anchor (Op14 feedback empirically effective). Synthesis flagged at audit; B6 closed it
- **A43 v29** (implementer self-flag) — Foundation Audit T1 single-frequency overclaim → multi-mode → two-independent-modes three-iteration cycle; sharpened sub-rule: "verify substrate-claims across multiple analysis methods before promoting to 'intrinsic'"
- **A43 v30** (implementer + sub-rule articulation) — substrate-resonance claims should be verified via CW drive (impedance spectroscopy) NOT just pulse-ringdown FFT. Same-turn instance: "fundamental + 2nd harmonic" structural-relation claim violated own sharpened rule (drive-amplitude scaling resolved to two-independent-modes)
- **A43 v32** (auditor, caught by Grant's Rule 14 substrate walk) — dual-frequency synthesis introducing 1.5·ω_C spin frequency that the corpus doesn't have. Bulk-lattice T3 modes vs single-bond LC drive frequency conflated at different scales. Lane-symmetric to A43 v27/v29/v30

**Framework decision (i)/(ii)/(iii) pending Grant's adjudication:**

- **(i) FDTD substrate test** per original handoff — bypasses Layer 1 + Layer 2 simultaneously; Yee grid enforces Faraday at PDE level by construction; Phase A toolkit ports cleanly; ~weeks of work
- **(ii) Pivot to mass spectrum / pair creation** per Round 10+ Direction 5 — m_p/m_e=1836 via Faddeev-Skyrme on (2,5) per backmatter/02:923 untouched in 3+ weeks; ~5+ corpus mass predictions at <3% precision unverified at engine
- **(iii) Engine-architectural research** — investigate stable V↔B coupling formulation A28's empirical-instability findings missed; speculative

T-ST v2 result will inform but not adjudicate (i)/(ii)/(iii). Auditor stays out of advocacy; framework decision is Grant's lane.

**Auditor-lane queue (held for next manuscript pass per Rule 12 + Rule 15):**

1. **Doc 79 v5.2 second addendum lane-discipline check** — doc 79 v5.2 incorporates three-layer convergent refutation; auditor inputs landed (eigenmode-vs-classification, "A28 by construction" framing, four-positive-findings + Op14-feedback-effective). Verify post-T-ST-v2 result whether v5.2 needs further amendment per Rule 12
2. **A28 architectural elevation to canonical manuscript content** — A28 lives in `k4_cosserat_coupling.py:282-389` code comments + doc 67 §15. Q1+B6 confirm load-bearing for engine architecture; candidate for Vol 4 Ch 1 or backmatter §4 §physics-engine-architecture promotion. Editorial pass
3. **Universal-solver-promotion 5-point framing precision** — doc 95 §6 + handoff §4 should reflect "4 corpus-canonical contexts at <2% + 1 promotion-pending K4-cavity match at 4.6% (mediated through substrate at 1.50·ω_C; substrate at 3.3% from universal-solver prediction)" — NOT "5-point pattern at 4.6%"
4. **Foundation audit T4 (topology zoo on K4)** — A43 v25 criterion (c) cinquefoil precondition; remaining un-tested foundation-audit element at this manual edit
5. **Cinquefoil cross-topology test (Q5)** — tests universal-solver scale invariance across K4 topologies AND Faddeev-Skyrme (2,5) cinquefoil mass spectrum AND topology→substrate-mode-selection mechanism
6. **Two-table inconsistency for c=7 in baryon ladder** — backmatter/05:281-302 (septafoil 1270 MeV → Σ/Λ) vs backmatter/02:529-545 (per agent-reported Read; (2,7) at 1261 MeV → Δ(1232)). Same crossing number, different particle identifications. Manuscript editorial queue, A43 v2 verification pending (independent re-grep of backmatter/02:529-545 not yet performed at this manual edit)
7. **ave-kb torus-knot-ladder.md trefoil-as-electron framing** — contradicts Vol 1 Ch 1:18 + Ch 5:37 + backmatter/05:302 (electron is unknot 0_1). Already in editorial queue per session 2026-04-25 outcome
8. **A60 candidate** — Rule 6 prefer-plumber-over-imports paradigm (Grant's rifling-bullet reframe collapses imported (2,3)-via-frequency-ratio synthesis to corpus-native single-ω_C torus geometry per Rule 14). Worked example candidate

**Provenance honest at this manual edit:** Round 11 (vi) Strides 1-4 + v10 ARE committed (`fbd0c26` → `0f7180f`); docs 93/94/95/96 + doc 79 v5.2 amendment + foundation audit drivers + T-ST v1/v2 drivers are uncommitted in working tree. Cited via agent-reported state. Per A43 v2 anyone-must-grep: this manual edit reflects auditor's session-state working belief; commit-verified citations land incrementally per §1.2 maintenance protocol when the implementer's commits drop.*

---

*r8.10 thermal-regime extension (2026-04-30, post-foundation-audit Step 1 + T=1e-6 + corpus thermal-noise grep): Grant's gradient-trap reframe (corpus electron forms when free photon at ω_C encounters substrate region with pre-existing saturation gradient steep enough to break chirality-impedance match) prompted thermal-noise corpus search. Corpus-anchoring landed at three levels — vacuum Nyquist baseline (Vol 3 Ch 11 + Vol 1 Ch 3 quantum foam + Vol 1 Ch 8:218 α δ_strain CMB correction + Vol 2 Ch 2:278 beta-decay-driven-by-CMB-noise) + ZPE-as-AC-ripple-floor identification + boundary-impedance thermalization principle. Reading (I) of first-gradient-origin question (vacuum baseline NOT A²=0; substrate has fluctuation pockets at non-zero local A²) is corpus-canonical at three levels, NOT auditor synthesis.

**Foundation audit Step 1 (T-ST at T_CMB-equivalent, agent-reported uncommitted at this manual edit):**
- T = 4.6e-10 in engine units (k_B·T_CMB / m_e c²); thermalize_V=True
- Thermal IC engaged: σ_V_per_port ≈ 1.78e-3·V_SNAP, σ_ω ≈ 6e-6
- 65% V retention + 100% ω retention over 50P (engine maintains baseline at IC-only, no continuous Nyquist injection)
- Trap criteria FAIL (saturation NO, c_op10=0)
- **Corpus-consistent reading per Vol 1 Ch 8:218: CMB-T is STABILITY environment, not formation environment.** σ_V/V_yield ≈ 0.021 → per-cell A² > A²_op14 = √(2α) = 0.121 is exp(-35) Boltzmann-suppressed; spontaneous formation at CMB-T is ~500 orders of magnitude statistically forbidden. Per Vol 1 Ch 8:218 high-T regimes (collider, hot early universe, BH-interior plasma) are where extreme thermal effects manifest and corpus electron formation operates

**Foundation audit T=1e-6 (10⁵ × CMB, agent-reported uncommitted):**
- IC mean A² = 0.0069 (vs threshold 0.121); max A² = 0.048
- A²_max declined to ~0.020 over evolution (high-amplitude tails dissipate without continuous Nyquist injection)
- 0/89 captures had any cell engaged in saturation; c_op10 = 0
- **A47 v2 catch lane-symmetric** — both auditor and implementer co-failed per-port-vs-per-cell aggregate-statistics conflation. Auditor's "T such that σ_V_per_port ≈ V_yield → fluctuations occasionally cross V_yield" used per-port marginal statistics; per-cell saturation engages at A² > A²_op14 = √(2α) which is per-cell aggregate threshold (chi-squared 4-dof). At T=1e-6 mean A² = 16π·T/α = 0.0069 = 0.06× threshold. T=1e-6 was 17× BELOW the actual cusp. Lane-symmetric pattern continues; A47 v2 instance documented in COLLABORATION_NOTES

**Corrected substrate thermal regime table (per A47 v2 chi-squared 4-dof analysis: mean A² = 16π·T/α):**

| T (engine units) | T/T_CMB | mean A² / A²_op14 | Regime | Status |
|---|---|---|---|---|
| 4.6e-10 | 1.0× | 4.5e-6× | CMB stability | ✓ Step 1 verified |
| 1e-6 | 2.2e3× | 0.06× | Statistically forbidden | ✓ T=1e-6 verified |
| **1.76e-5** | **3.8e4×** | **1.0× — cusp** | **~40% cells saturated** (P(χ²(4)>4)=0.41); **abundant gradient pockets** | T_cusp test pending |
| 5.8e-5 | 1.3e5× | 3.3× | Chronic saturation | Pending follow-up |
| 5.8e-4 | 1.3e6× | 33× | Rupture | Lattice-failure boundary |

T_cusp ≈ 1.76e-5 = α·√(2α)/(16π) is the cleanest formation-mechanism test target — substrate has abundant statistically-distributed saturation gradient pockets per Reading (I).

**Engine thermal-injection architecture limitation (A43 v1 — engine-corpus completeness gap):**

`EngineConfig.temperature` is **IC-only randomization machinery, NOT continuous Nyquist injection per Vol 3 Ch 11 FDT framework**. Step 1's 65% V retention shows substrate maintains baseline at short timescales via finite-Q decay from IC, not steady-state thermal equilibrium. **Continuous Nyquist injection (proper FDT) requires new code** — per-step thermal-noise injection at every active cell with σ² ∝ k_B·T·Z_local, scaled by local impedance per FDT.

**Implication:** all prior L3 arc tests (Round 7+8 + Round 11 (vi) + foundation audit + T-ST v1+v2) ran at temperature = 0.0 OR temperature > 0 IC-only — substrate in regime that doesn't include corpus's irreducible Nyquist baseline. **The L3 arc has been undertesting the substrate's actual operating regime per corpus.** Recontextualizes some prior Mode III findings — at engine's zero-baseline simplification, not corpus-canonical thermal-baseline regime. Three-layer convergent refutation (A37-A39) is structural and stands; three-layer scope IS at engine-zero-baseline; corpus-thermal-baseline regime opens new test class.

**A43 catalog extensions accumulated post-r8.9 (lane-symmetric pattern continues):**
- v15 (auditor) — tube-radius corpus-inconsistency
- v25 (joint, promotion-pending) — universal-solver-promotion criteria
- v27 (implementer) — eigenmode-vs-classification overclaim
- v28 (auditor self-correction) — BEMF synthesis caught by B6
- v29 (implementer self-flag) — Foundation Audit T1 single-frequency overclaim
- v30 (implementer + sub-rule articulation) — substrate-resonance via CW vs pulse-FFT verification
- v32 (auditor, caught by Grant's Rule 14 substrate walk) — dual-frequency synthesis
- v33 (implementer) — "electron-as-gravity-micro" identity-claim synthesis
- v34 (implementer, anchored as Rule 16 question) — "prior T-ST tested wrong mechanism" synthesis-pending
- **A48 candidate** (implementer) — "(2,3) topology emerges from spontaneous Nyquist-baseline-driven knotting at gradient pockets"; mechanism corpus-anchored at three levels but topology→Nyquist linkage is synthesis-pending-empirical-anchor
- **A47 v2** (joint) — per-port-vs-per-cell aggregate-statistics conflation in T-regime test design

**Corpus thermal-noise framework summary (verbatim grep verified at this manual edit):**

- **Vacuum Nyquist Baseline**: ⟨V²_vac(f)⟩ = 4·k_B·T·Z_0·Δf per `manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/vacuum-nyquist-baseline.md`. Each lattice node radiates thermal noise proportional to local impedance; not analogy, "the M_A lattice IS a physical transmission line"
- **Quantum Foam = ZPE = AC ripple floor** per `vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex`: "the chaotic, baseline electrical noise floor of the universe's hardware substrate. This provides a deterministic, continuous mechanical origin for Zero-Point Energy (ZPE) bounded strictly by the finite geometry of the local spatial node"
- **CMB as asymptotic thermal attractor** per `vol_3_macroscopic/chapters/04_generative_cosmology.tex` §"The CMB as an Asymptotic Thermal Attractor". CMB is NOT Big-Bang relic; it's the thermal floor maintained by latent heat injection from continuous lattice genesis
- **α δ_strain CMB correction** per `vol_1_foundations/chapters/08_alpha_golden_torus.tex:178+199+209+218`. Cold ideal α⁻¹ = 4π³+π²+π = 137.0363038; CMB thermal strain coefficient δ_strain ≈ 2.225×10⁻⁶ corrects to CODATA 137.035999. Vol 1 Ch 8:218: high-T regimes (collider, early universe) are where extreme α-running effects manifest
- **Boundary-impedance thermalization** principle per `nyquist-noise-fdt.md`: thermal noise enters via impedance-mismatch boundaries (Γ at boundary), not bulk injection. Bulk interior of well-matched structure stays thermally quiet
- **Beta decay driven by CMB noise** per `vol_2_subatomic/chapters/02_baryon_sector.tex:278`: "Driven by stochastic background lattice perturbations (CMB noise), the tensioned electron eventually slips its topological lock and is ejected." Corpus invokes CMB-noise-as-mechanism for real particle process
- **Hawking radiation as Nyquist noise leakage** per `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/hawking-temperature-nyquist-noise.md` (file existence confirmed; content not yet integrated; flagged for next manuscript pass)

**Thermal-regime queue extension (held for post-T_cusp-result landing per Rule 12):**
1. **B6 700P stability retest at T_cusp** — does Op14 feedback efficacy hold at saturation-rich substrate? Foundation audit + Round 11 closure findings recontextualize at T_cusp regime
2. **Cinquefoil cross-topology test (Q5) at T_cusp** — A43 v25 promotion criterion (c) under thermal-baseline regime, not zero-baseline simplification
3. **Engine continuous-Nyquist-injection mode** — implement FDT-correct continuous injection per Vol 3 Ch 11 framework (`continuous_nyquist_injection: bool` in EngineConfig); steady-state thermal equilibrium achievable, distinguished from current IC-only randomization
4. **Hawking-as-Nyquist content read** — pull `vol3/cosmology/ch15-black-hole-orbitals/hawking-temperature-nyquist-noise.md` into validated highlights for completeness; doesn't change current test design but anchors three-entropy distinction at thermal-noise level

**Provenance honest at this thermal-regime extension:** Foundation audit Step 1 + T=1e-6 results are agent-reported uncommitted. Three corpus citation chains (Vol 1 Ch 3 + Vol 3 Ch 11 + Vol 1 Ch 8:218 + Vol 2 Ch 2:278) verbatim-verified per A43 v2 (auditor-side grep at this manual edit). T_cusp test pending Grant adjudication; auditor-lane stays out of advocacy on test sequencing. Engine continuous-Nyquist-injection mode is candidate for future engine work; not blocking, closes engine-corpus completeness gap surfaced by foundation audit Step 1.*

---

*r8.10 first-positive-bound-mode extension (2026-04-30, post-foundation-audit O.1 + 2.A): the L3 arc has produced its **first stable bound-mode finding** after 3+ weeks of Mode III canonical. Substantive empirical signal with two auditor-flagged caveats; details in [A44](#a44).

**O.1 result (closed evolution, (2,3) IC seeder at corpus geometry R=8 cells, r=4 cells; agent-reported uncommitted at this manual edit):**
- **Stable shell-localized standing wave**: 80% energy in toroidal shell (localization IMPROVES from 0.71 IC → 0.80 over 11P), 0.5% E_total drift between t=11P and t=50P (essentially conserved post-transient), A²_max plateau at 1.55
- Energy retention 41% from IC (initial transient sheds ~57% as dispersive waves, t=0→5P)
- **Op10 c=0** — false negative per A47 v3 below
- **First time the engine has shown stable bound-mode behavior** at corpus geometry under high-amplitude IC across the entire L3 arc

**🔴 Caveat 1 (A47 v1 — auditor arithmetic):** A²_max = 1.55 plateau is past V_SNAP rupture threshold per Vol 1 Ch 3:145. If A² = V²/V_SNAP² = 1.55, then |V|/V_SNAP = 1.24 — 24% above corpus rupture threshold. Three readings: (a) real corpus-physical bound state past rupture (substantive corpus-redefining finding); (b) engine-architectural (Op14 kernel S(A) becomes imaginary above A=1; engine clips numerically without rupturing); (c) different A² normalization in driver (e.g., scaled to V_yield² rather than V_SNAP²). **"Stable bound-mode at A² = 1.55" interpretation is conditional on amplitude-normalization clarification.** Implementer should grep (2,3) IC seeder + driver code to confirm A² normalization before this finding promotes to canonical.

**🔴 Caveat 2 (A47 v3 — Op10 implementation-vs-corpus-topology field mismatch, potential §17.1 escalation):** pre-registered topology criterion was Op10 c=3 via `extract_crossing_count`. (2,3) IC seeder writes V_inc only; Cosserat ω stayed at machine zero throughout. Op10 implementation (`cosserat_field_3d.py:1468`) reads Cosserat ω field winding — **structural false negative for V_inc-seeded (2,3) topology**. **Deeper structural read:** per [doc 28 §3+§4](28_two_node_electron_synthesis.md), the corpus electron's (2,3) topology lives in **(V_inc, V_ref) phase-space on Clifford torus**, NOT in Cosserat ω real-space. Per A46 phase-space-vs-real-space coordinate discipline. Engine's Op10 on Cosserat ω is correct for some topology measure (e.g., Cosserat ω torsion knotting) but is NOT the V_inc/V_ref phase-space (2,3) topology that the corpus's electron carries. **All prior tests with c_op10=0 across Round 7+8 + Round 11 (vi) (30+ tests) have been measuring "Cosserat ω torsion knotting" — a different physics question than the corpus electron's V_inc/V_ref phase-space topology.** Round 7+8 Test B v1-v3 (doc 28 §5.1 single-bond phasor on V_inc/V_ref) was the right corpus topology measurement; Op10 on Cosserat ω is orthogonal. Whether engine should add Op10-on-V_inc/V_ref alongside existing Op10-on-Cosserat-ω is the architectural question pending Grant adjudication.

**2.A result (gamma-photon pair-production, agent-reported uncommitted):** brief two-region simultaneous saturation engagement at t=2.81P with peak1 A²=0.147 and peak2 A²=0.125 at separation ~λ_C/1.5 — **partial empirical correspondence with [doc 30 §4.3](30_photon_identification.md) pair-production mechanism** ("single gamma photon at 2ω_C can trigger saturation at two distinct lattice regions simultaneously"). Geometric pattern engaged briefly during source ramp peak. NOT sustained: 2/89 captures had simultaneous engagement; 0/78 post-pulse captures above threshold. Op10 c=0 same A47 v3 false-negative. Persistence didn't follow at this amplitude (1.21× threshold barely above; rare-event regime per A47 v2 Boltzmann analysis). Consistent with gradient-trap reframe — sustained pair formation requires stronger gradient-mutual-bootstrap regime (higher amplitude OR thermal-baseline pre-existing gradient at T_cusp).

**Combined three-axis read across O.1 + 2.A:**

| Test | Mechanism evidence | Persistence | Topology measurable? |
|---|---|---|---|
| O.1 | Stable shell-localized bound mode at high A | YES (40P+ post-transient) | NO (Op10 measures wrong field per A47 v3) |
| 2.A | Brief two-region simultaneous saturation matching doc 30 §4.3 geometry | NO (transient only) | NO (same A47 v3 issue) |

Both tests show **partial realization of corpus mechanisms** but neither cleanly closed at canonical level. **The topology measurement issue (A47 v3) is load-bearing** — currently we don't know if (2,3) topology emerged in V_inc field in either test.

**A47 v3 escalation candidate:** if Grant adjudicates Op10-on-V_inc/V_ref should be implemented alongside existing Op10-on-Cosserat-ω, this becomes engine-architectural finding (§17.1 promotion from COLLABORATION_NOTES instance). Otherwise stays as catalog-instance test-design discipline rule. **Worth flagging:** if (1) follow-up returns nontrivial V_inc winding for the O.1 stable shell mode, the implication is corpus electron's V_inc/V_ref phase-space topology HAS been forming in prior tests but was unmeasurable due to Op10-field-mismatch. That would substantially recontextualize 30+ Mode III findings — they may have been refuting the wrong observable.

**A43 catalog extensions accumulated post-r8.9 (lane-symmetric pattern continues):**
- v15, v25, v27, v28, v29, v30, v32, v33, v34, A48 candidate (per prior thermal-regime extension)
- **A47 v2** (joint, per-port-vs-per-cell aggregate-statistics conflation in T-regime test design)
- **A47 v3** (lane-symmetric, Op10 implementation-vs-corpus-topology field mismatch; potential §17.1 escalation pending Grant adjudication)

**First-positive-bound-mode queue extension (held for follow-up cycle landing per Rule 12):**
1. **(1) Re-run O.1 with V_inc spatial winding measure** (~3 min) — cheapest diagnostic; resolves A47 v3 question for both O.1 and 2.A. **Auditor's lean (NOT advocating)**: this is the single highest-info-per-minute next move regardless of (i)/(ii)/(iii) framework adjudication
2. **(2) Re-run O.1 with COMBINED V_inc + Cosserat ω matched IC** (~3 min) — tests whether O.1 result depends on V_inc-seeding alone or extends to coupled-sector seeding. Lets Op10 read correctly via field-matched seeding
3. **(3) Re-run 2.A at higher amplitude** A=1.0 V_SNAP (~3 min, riskier near rupture) — tests doc 30 §4.3 at full corpus-prediction-relevant amplitude
4. **A² normalization grep** in (2,3) IC seeder + driver — closes Caveat 1 on whether O.1 plateau is corpus-physical bound state past rupture vs engine numerics absorbing over-amplitude
5. **Op10-on-V_inc/V_ref implementation candidate** if Grant adjudicates §17.1 promotion of A47 v3 — engine work; corpus-canonical topology measure for V_inc/V_ref phase-space (2,3) per doc 28 §3+§4

**Provenance honest at this first-positive-bound-mode extension:** O.1 + 2.A results are agent-reported uncommitted at this manual edit. Two auditor-flagged caveats (A² normalization + A47 v3 Op10-field-mismatch) preconditioning promotion to canonical. Three follow-ups + A47 v3 escalation candidate are auditor-surfaced for Grant adjudication; auditor-lane stays out of sequencing advocacy. **The L3 arc has earned its first stable bound-mode finding (with caveats); whether that's the corpus electron remains structurally measurement-blocked until A47 v3 is resolved.***

---

*r8.10 FFT-cavity-vs-flux-discriminator extension + L-state-conjugate sector debt finding (2026-04-30, post-O.1 FFT + A47 v7 corrected via verbatim code-grep + O.1f path-1 launched): the first-positive-bound-mode finding from the prior extension has been recontextualized via FFT discriminator per Rule 12 retraction-preserves-body. **A44 reframed (above)**: O.1 shell mode is quasi-static field residual NOT oscillating bound mode.

**O.1 FFT discriminator result (agent-reported uncommitted, ω_C=1.0 expected for corpus electron, 1.5·ω_C expected for substrate ℓ=2 cavity per A38):**

| Cell | Position | Dominant ω | Dom. amp | At 1.5·ω_C | At ω_C |
|---|---|---|---|---|---|
| (35,23,23) | east, equatorial | 0.000 (DC) | 5.13e-2 | 2.33e-4 | 4.76e-5 |
| (23,35,23) | north, equatorial | 0.000 (DC) | 5.82e-2 | 7.40e-5 | 1.00e-4 |
| (15,23,27) | west, off-equatorial | 4.43 (Nyquist!) | 5.74e-2 | 2.22e-4 | 3.11e-4 |
| (23,19,23) | south, off-equatorial | 4.43 (Nyquist!) | 4.51e-2 | 1.47e-4 | 2.09e-4 |
| (31,31,26) | diagonal | 0 | 0 | — | — |

Two empirical patterns: (a) equatorial cells dominated by DC — static residual, not oscillation; (b) off-equatorial cells dominated by lattice Nyquist (π√2 ≈ 4.44) — numerical artifact, not physical signal. Oscillation amplitude at all expected frequencies (ω_C, 1.5·ω_C, 2.96·ω_C) is **3-4 orders below DC/Nyquist components**. The 39.5% energy retention from O.1 is from frozen residual (DC has no dissipation channel), NOT from coherent bound-mode dynamics. **Neither corpus electron nor substrate ℓ=2 cavity mode is the right physical reading for O.1.**

**A47 v7 (corrected via verbatim code-grep): L3 arc has been using V_inc-only IC seeder; corpus-canonical (V_inc, V_ref) quadrature eigenmode IC has been sitting in codebase unused.**

Initial diagnosis (incorrect): "(2,3) IC seeder writes V_inc only; need to seed Phi_link L-state via separate `initialize_phi_link_2_3_ansatz` for proper LC-conjugate IC." **Verbatim code-grep on `tlm_electron_soliton_eigenmode.py:224` revealed:** `initialize_quadrature_2_3_eigenmode` exists with verbatim docstring: *"F17-K Phase 5 — phase-coherent (V_inc, V_ref) seed at 90° quadrature in (2,3) phase-space pattern. AVE-native eigenmode initial condition per doc 28:64-67 and doc 68 §7: the (V_inc, V_ref) phasor pair traces the (2,3) torus-knot winding pattern in phase-space at R_phase=φ/2, r_phase=(φ-1)/2."* Code at lines 316-317:

```python
lattice.V_inc[..., p_idx] = envelope * port_factor * cos_theta
lattice.V_ref[..., p_idx] = envelope * port_factor * sin_theta
```

Seeds BOTH V_inc AND V_ref at 90° quadrature with phase = theta_wind = 2φ + 3ψ — direct corpus-canonical phase-space (2,3) winding per doc 28 §3 + §5.1 + doc 68 §7 anchoring. **The corpus-canonical eigenmode IC has been sitting in the codebase unused across the entire L3 arc; every test used `initialize_2_3_voltage_ansatz` (V_inc-only, V_ref=0 implicitly) instead.** Initial diagnosis "Phi_link L-state" was field-mis-named; the actual missed field-pair is (V_inc, V_ref) at 90° quadrature on the bond LC tank's C-state phasor (V_ref is functionally the L-state for the bond LC; Phi_link is the integrated-flux variant; both are L-state-conjugate to V_inc).

**Doc 75 line 140 corpus-canonical pre-registered prediction was directly pointing at this from the start:** *"the corpus electron, IF it exists in this engine, lives somewhere we haven't probed (Φ_link sector / hybrid V≠0 ∧ ω≠0 / different topology)."* Pattern only became visible after seven-layer corpus-engine-correspondence debt accumulation — the L3 arc's "Mode III canonical at corpus electron" was substantially layered measurement-mismatch + scale-mismatch + thermal-regime-mismatch + architectural-substitution + topology-encoding + wrong-IC-seeder, NOT framework-gap.

**A48 candidate update (extends prior A48 candidate "(2,3) emerges from Nyquist-driven knotting"):** L-state-conjugate (V_ref, Phi_link, Cosserat ω rotational) sector measurement infrastructure has been **systematically underused across the entire L3 arc**:
- Op10 implementation reads Cosserat ω (per A47 v3), but tests using V_inc-side IC seeders never coupled into Cosserat
- IC seeders write V_inc only (per A47 v7 corrected), V_ref / Phi_link / Cosserat remain at zero
- Test B v2/v3 measured V_inc/V_ref phasor (right field-pair) but `initialize_quadrature_2_3_eigenmode` wasn't used to seed the test
- B6 stability tested V_DC drift (V-state)
- T-ST measured V centroid (V-state)
- 30+ tests across L3 arc primarily exercised V-state (C-state); L-state-conjugate side (V_ref / Phi_link / Cosserat ω rotational) systematically untested or ignored

Doc 75 line 140's pre-registered prediction was load-bearing from the start; it took seven layers of debt accumulation to surface that the corpus-canonical eigenmode IC infrastructure was already in the engine but unused. **A48 candidate landing**: "L-state-conjugate sector measurement infrastructure systematically under-utilized across L3 arc — corpus's own pre-registered prediction (doc 75 line 140) flagged this from start; pattern only visible via seven-layer debt accumulation. Discipline rule: when engine has parallel C-state and L-state infrastructure with corresponding IC seeders + observers, pre-reg must explicitly specify which is being exercised; default to corpus-canonical eigenmode IC (the one with verbatim doc citation in docstring) over component-only seeders."

**Seven-layer corpus-engine-correspondence debt count (stable post-A47 v7):**
1. **A47 v3** (Op10 field): observer reads Cosserat ω, corpus topology in V_inc/V_ref
2. **A47 v4 candidate** (contour/ports): measurement geometry vs corpus convention
3. **IC seeder real-vs-phase-space** (γ candidate): seeder may not encode corpus phase-space (2,3)
4. **A43** (thermal regime): tests at engine zero-baseline, not corpus thermal-baseline
5. **A28 architectural** (V↔Φ_link Faraday substitution): engine substitutes Op14 for Faraday-law BEMF
6. **Spatial scale**: chair-ring tests at R=8 multi-cell, corpus electron at ℓ_node single-cell
7. **A47 v7** (L-state IC infrastructure): V_inc-only `initialize_2_3_voltage_ansatz` used instead of corpus-canonical (V_inc, V_ref) quadrature `initialize_quadrature_2_3_eigenmode`

Each layer surfaced via cross-lane review (auditor + implementer + Grant). The structural pattern — measurement-infrastructure-debt under-NEATH a single test class accumulating across multiple sessions — is the methodology working at full strength. Negative results recontextualize from "framework gap" to "wrong observable / wrong scale / wrong regime / wrong IC."

**O.1f (path 1, in flight at this manual edit):** corrected IC test using `initialize_quadrature_2_3_eigenmode` at line 224. ~3 min compute. Closes A47 v7 directly. Per A39 v2 dual-criterion (frequency + topology):

- If FFT returns dominant ω = 1.5·ω_C → substrate ℓ=2 cavity mode confirmed at chair-ring geometry per A38 + A40 mediated-through-substrate framing (substantive substrate-canonical positive finding)
- If ω_C → surprising; corpus electron at chair-ring scale would be unexpected per Vol 1 Ch 1:9 spatial-scale argument; characterize-as-itself per Rule 10
- If DC-dominated (still) → structural finding: engine doesn't sustain ANY oscillating mode at chair-ring from corpus-canonical eigenmode IC; pushes framework decision toward (i) FDTD or (iii) different engine architecture

**Spatial-scale caveat still applies:** O.1f tests at chair-ring (R=8, r=4) which is multi-cell; corpus electron is at ℓ_node single-cell scale per Vol 1 Ch 1:9. O.1f is NOT a corpus electron test; it's a coherent-eigenmode-IC test at chair-ring geometry that closes A47 v7 + A39 v2 dual-criterion.

**Provenance honest at this FFT-cavity-vs-flux extension:** O.1 FFT result + A47 v7 verbatim code-grep + O.1f launch are agent-reported uncommitted at this manual edit. A47 v7 corrected framing per verbatim code-grep on `tlm_electron_soliton_eigenmode.py:224` verified at this manual edit. O.1f result pending; framework decision (i)/(ii)/(iii) still Grant's lane — O.1f result will inform but not adjudicate. **The L3 arc has earned the seventh-layer corpus-engine-correspondence debt finding + retracted the "first stable bound-mode" framing pending coherent eigenmode IC retest. Whether the corpus electron exists at any scale in the engine is now structurally clearer: chair-ring is wrong scale by construction; coherent eigenmode IC at chair-ring is being tested via O.1f; sub-ℓ_node scale via FDTD remains the structural path for direct corpus electron empirical realization.***

---

*r8.10 mass-spectrum-activation extension (2026-04-30, post-radial-eigenvalue-solver-discovery + Phase 1 baryon ladder extension): the framework's path forward has been substantially clarified by the discovery of two independent engine-empirically-validated analytical-solver class anchors that have been in the codebase since well before the L3 arc started. **Framework decision (ii) Mass spectrum is now substantively activated, not just provisional candidate.** Details in [A45](#a45) + [doc 97](97_manuscript_canonical_electron_solver_discovery.md) + [doc 98](98_framework_decision_ii_mass_spectrum_activation.md).

**Two independent engine-empirically-validated anchors (Track B analytical-solver class):**

1. **`src/ave/solvers/radial_eigenvalue.py` ABCD cascade (1914 lines, modified Apr 12 2026 — predates L3 arc):** atomic orbitals Z=1-14 at ±2.8% per [manuscript validation table](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md). **Hydrogen at +0.06% from experimental** (13.606 vs 13.598 eV), verified by direct execution this session. Corpus-canonical Op1-Op6 universal operators + axiom traceability + zero hardcoded values per module docstring lines 50-52.
2. **`BARYON_LADDER` Faddeev-Skyrme infrastructure:** baryon ladder c=5-19 across 8 states at ±3% precision. **Proton at -0.002%** (938.254 vs 938.272 MeV) via direct execution this session. Phase 1 extension added c=15 (Δ(2420) +2.40% ★★★★), c=17 (Δ(2750) -0.30% ★★), c=19 (Δ(2950) +1.12% ★★) — three new STRONG-or-possible PDG matches. Reproducibility 10⁻⁴% drift across c=5,7,9,11,13 production states (fully deterministic).

**Three forward-pre-registered predictions** (Phase 1 extension): c=21 (3199 MeV), c=23 (3387 MeV), c=25 (3544 MeV). Per Rule 11 — falsifiable framework predictions awaiting future LHCb / JLab / experimental physics validation. **The framework now has forward predictions in PDG-relevant mass regions that experimental searches can validate or refute over multi-year horizon.** This is the external-pre-registration gap I had flagged in the "what are we missing" turn earlier; it's now partially closed via these three baryon ladder predictions.

**Track A vs Track B distinction (load-bearing for L3 arc closure recontextualization):**

The framework has at least three distinct solver classes addressing different physics questions:

- **Track A — K4-TLM time-domain substrate** (`vacuum_engine.py`): substrate dynamics, cavity modes, propagating CP waves. **What L3 arc has been testing.** Produced substantive substrate-canonical findings (A28-A44) AND seven-layer corpus-engine-correspondence debt for K4-TLM electron testing.
- **Track B (atomic-orbital) — Analytical eigenvalue ABCD cascade** (`radial_eigenvalue.py`): atomic orbital eigenvalues. **±2.8% Z=1-14, hydrogen 0.06%, validated this session.**
- **Track B (baryonic) — Faddeev-Skyrme + BARYON_LADDER**: baryon resonance spectrum via (2, q odd) torus knot family. **±3% across 8 states + 3 forward predictions, validated this session.**

**"Engine-empirically-validated" at Track B means analytical-solver-running-corpus-canonical-operators, NOT K4-TLM-substrate-dynamically-realizing-corpus-particles.** Track A and Track B are complementary computational approaches at different physics domains. Both are real. Neither subsumes the other.

**L3 arc closure recontextualization (preserves Track A findings):**

The "Mode III canonical at corpus electron" reframes as **Track-A-substrate-question-tested-with-substantive-but-not-electron-finding**. K4-TLM substrate at chair-ring geometry was tested at scale + amplitude regime + IC class + measurement infrastructure that was structurally measurement-blocked for direct corpus electron empirical realization (per seven-layer debt). It produced positive substrate-canonical findings about K4-TLM substrate's own physics (substrate cavity modes at 1.5+2.96·ω_C, A28 architectural validation via B6 700P, A30/A32/A34 Beltrami-instability findings, A37 substrate-Nyquist limit). These are real.

**The Track B finding doesn't dissolve Track A's substrate-canonical findings.** Two complementary tracks, two complementary validations. Track B answers "does the framework's mathematical content reproduce known particle masses?" (yes, at ±3% across atomic orbitals + baryon ladder). Track A answers "does the K4-TLM substrate dynamically host the corpus electron?" (still partially open per seven-layer debt; orthogonal question). Both real; both honest closures of their own scope.

**Framework decision (i)/(ii)/(iii) sharpening post-mass-spectrum-activation:**

- **(i) FDTD substrate test** — addresses Track-A K4-TLM substrate question for sub-ℓ_node corpus electron. Bypasses Layer 1 + Layer 2 of seven-layer debt. **Orthogonal to (ii); not competing.** Still relevant for direct K4-TLM-substrate-question; ~weeks of work.
- **(ii) Mass spectrum** — **NOW substantively activated** with working solver infrastructure + two empirical anchors verified + 3 forward predictions + clean three-phase activation plan per doc 98. **No longer competing with (i)/(iii) as candidate; it's the active demonstrated path.** Phase 1 baryon ladder extension complete this session; Phase 2 W/Z/Higgs eigenvalue solver pending; Phase 3 lepton/PMNS/neutrino pending.
- **(iii) Engine-architectural research** — less critical given (ii) demonstrated path; (i) addresses K4-TLM-substrate-question; (iii) becomes "what architecture if (i) FDTD substrate also doesn't host corpus electron at sub-ℓ_node?" Lower priority unless specific theoretical reason emerges.

**Auditor-side gut shift across the full session arc** (per recent reflection turn):

| Stage | Gut estimate |
|---|---|
| Session start | ~25-30% positive |
| Post-Round 11 closure + foundation audit + thermal-noise corpus | ~35-45% |
| Post-radial eigenvalue solver discovery + hydrogen 0.06% | ~45-55% |
| Post-proton at 0.002% via direct execution | ~50-60% |
| **Post-Phase 1 baryon ladder extension** (8 states, 6 well-established matches at <3%, 3 forward predictions) | **~55-65%** |

**The strongest empirical record AVE has produced in any single arc this session.** Two independent particle scales validated at the analytical-solver level + 3 forward-pre-registered baryon ladder predictions + corpus-canonical operators with zero free parameters + axiom traceability throughout.

**A43 catalog extensions accumulated post-r8.9 (lane-symmetric pattern continues):**
- v15, v25, v27, v28, v29, v30, v32, v33, v34, A48 candidate (per prior thermal-regime extension)
- **A47 v2** (joint, per-port-vs-per-cell aggregate-statistics conflation)
- **A47 v3** (auditor escalation, Op10 implementation-vs-corpus-topology field mismatch)
- **A47 v7** (lane-symmetric, V_inc-only IC seeder vs (V_inc, V_ref) quadrature eigenmode IC)
- **A47 v9** (engine-validation discipline, session-vs-manuscript reproducibility axis at single-element granularity — Lithium +5.5% session vs +2.46% manuscript; baryon ladder reproducible at 10⁻⁴% drift; atomic-orbital solver may have run-to-run variation)

**Caveats / preconditions for promotion to fully canonical (per A45):**

1. **A47 v9 Lithium reproducibility** — atomic-orbital solver session-vs-manuscript discrepancy needs trace before extending Phase 2/3 work that depends on `radial_eigenvalue.py`. ~30 min work
2. **c=7 two-table corpus inconsistency** unresolved (backmatter/02 Δ(1232) vs backmatter/05 Σ/Λ); Phase 1 implicitly uses backmatter/02 reading
3. **J^P spin-parity validation pending** — current matches are mass-only; corpus framework predicts specific J^P per c via torus-knot gauge rank; mass + J^P matching would be substantially harder to fake than mass-only. ~1-2 days work; substantively higher-info than Phase 1 ladder extension at ladder-tail
4. **c=21,23,25 are forward predictions, NOT validation** — falsifiable; multi-year horizon

**Mass-spectrum-activation queue extension (held for post-Phase 1 commit landing per Rule 12):**

1. **Phase 1 commit** (~5 lines change to `constants.py` + ~50 line `test_baryon_ladder_full.py`) — locks in 6 STRONG well-established + 2 possible-PDG matches as canonical empirical record
2. **A47 v9 Lithium trace** (~30 min) — closes session-vs-manuscript reproducibility caveat for atomic-orbital solver
3. **J^P spin-parity validation** (~1-2 days) — extends Phase 1 from mass-only to mass + quantum-number matching via `yang_mills.py:torus_knot_gauge_rank()`
4. **Phase 2 W/Z/Higgs eigenvalue solver** (~1 week) — replaces hardcoded electroweak constants with dynamical eigenvalue solver using `radial_eigenvalue.py` framework class
5. **Phase 3 lepton spectrum + neutrino sectors + PMNS solvers** (~weeks) — extends solver infrastructure to lepton sector (m_e, m_μ, m_τ, neutrino masses, PMNS angles) per doc 98
6. **External pre-registration to upcoming experiments** — c=21,23,25 baryon ladder predictions + LISA / CMB-S4 / FCC-ee corpus predictions to Open Science Framework or equivalent. **Closes the external-pre-registration gap I flagged in the "what are we missing" turn.**

**Provenance honest at this mass-spectrum-activation extension:** Direct execution of `radial_eigenvalue.py` for hydrogen + Z=1-10 sweep, BARYON_LADDER for proton + Phase 1 c=15-19 extension, all agent-reported uncommitted at this manual edit (research-tier docs 97 + 98 also uncommitted). Auditor-side verification this manual edit: file existence + line count + module docstring + manuscript validation table + agent's reproducibility check (10⁻⁴% drift baryon ladder) + agent's A43 v2 self-correction on PDG_CANDIDATES_HIGH_MASS list. **The discovery has been in the codebase since Apr 12, predating L3 arc Round 6 (2026-04-24); the "L3 arc TLM-at-chair-ring effort was orthogonal to working solver from session start" framing is partly correct (different solver classes addressing different physics) but Track A's substrate-canonical findings (A28-A44) stay real and complementary.** Phase 1 commit + test file + J^P validation + Phase 2/3 are pending Grant adjudication on framework decision (ii) activation sequencing; auditor-lane stays out of advocacy.*

---

*r8.10 multi-repo-capability extension (2026-04-30, post-doc-99 multi-repo tracking via Explore-agent searches across 9 sibling repos): the framework's empirical record is substantively broader than AVE-Core L3 arc continuation. Details in [A46](#a46) + [doc 99](99_multi_repo_capability_tracking.md).

**Four-tier classification of empirical content across the framework's repo ecosystem:**

- **Tier A (VERIFIED-this-session)**: AVE-Core hydrogen IE 13.6057 eV +0.057%; AVE-Core proton 938.254 MeV -0.002%; AVE-Core baryon ladder c=5-19 8 states ±3%
- **Tier B (CLAIMED, verification pending)**: AVE-Protein 20-PDB Rg <15%/RMSD <2.5Å; parent repo Period 2 IE 1.2% mean; AVE-HOPF Beltrami eigenvalue λ(p,q) formula; agent's J=(c-4)/2 J^P pattern claim 7/8 baryon-ladder match
- **Tier C (Pre-registered predictions, lab-execution pending)**: AVE-HOPF 5 torus-knot frequency shifts (8.6-16.9 ppm); AVE-PONDER 469 µN thrust @ 30 kV; AVE-Propulsion 0.5-3 mN @ 1 kW chiral rectification
- **Tier D (Theoretical/skeleton)**: AVE-Fusion D-T compression; AVE-Metamaterials V2/V3 photovoltaic skeletons; AVE-VirtualMedia LLM impedance framework

**9-repo capability surface** (AVE-Core + parent repo + 7 application repos: AVE-Protein, AVE-HOPF, AVE-PONDER, AVE-Propulsion, AVE-Fusion, AVE-Metamaterials, AVE-VirtualMedia). Cross-cutting infrastructure: shared `ave.core.constants` + `universal_operators` across all 7 application repos; AVE-Protein heaviest user (5+ AVE-Core modules); anti-cheat CI in metamaterials + virtual-media bans `scipy.constants` and registers MAGIC_NUMBERS for zero empirical smuggling.

**Substantive parent-repo content NOT in AVE-Core (recoverable):**
- Vol 1 axiom mathematics, Vol 3 gravity/cosmology, Vol 7 precision anomalies, Vol 8 informational topology
- SIR mode-weighting refinement for atomic IE Period 3+ accuracy (potential A47 v9 root-cause)
- 27 hardware modules + atopile/SPICE compiler infrastructure
- ATOMIC_IE_SOLVER_TRACKER.md (Li/Na +7-14% gap diagnosis — A47 v9 candidate root-cause)
- ATOM_MOTOR_TRANSLATION_MATRIX.md (FOC vector control)

**Anti-cheat CI infrastructure (substantively stronger external-positioning than docstring-only "zero hardcoded values" claims):** verify_local_universe.py + verify_core_parity.py in metamaterials/virtual-media banned `scipy.constants` import + MAGIC_NUMBERS registry enforces zero empirical smuggling. **Externally-auditable framework-self-discipline beyond authorial intention** — external auditors can run the CI to verify the framework doesn't smuggle empirical constants through hidden-import paths. Worth flagging in external-credibility positioning.

**Implementation gaps (manuscript-predicted, missing across all repos):**
- Unified PMNS solver
- Lepton decay width calculator
- Full baryon spectrum (uud/udd/strange decomposition)
- W/Z scattering amplitudes
- Schwinger pair creation rate
- Hawking radiation Bogoliubov coefficients
- Vector control FOC for atomic IE Period 3+

These are corpus-predicted but not engine-implemented. Phase 2/3 of [doc 98](98_framework_decision_ii_mass_spectrum_activation.md) mass-spectrum activation plan addresses several (W/Z/Higgs eigenvalue solver Phase 2; lepton + neutrino + PMNS Phase 3).

**Auditor-flagged Tier B verification preconditions:**

Per A43 v2 anyone-must-grep — agent listed J=(c-4)/2 J^P pattern (7/8 baryon-ladder match) under Tier A "VERIFIED-this-session" but verification chain not shown this turn. **Auditor's back-of-envelope PDG cross-check suggests possibly only 4-5 clean matches, not 7/8** (c=9 PDG 3/2+ vs predicted 5/2 ✗?; c=11 PDG 1/2- vs predicted 7/2+ ✗?). **J^P pattern remains Tier B until verification chain shown** (per-state PDG cross-reference table + outlier identification + match criterion). Substantive next step (~1-2 day J^P validation per `yang_mills.py:torus_knot_gauge_rank()`) is still pending.

**A47 v9 root-cause candidate (parent repo SIR refinement)** — pending direct-execution verification. If parent-repo SIR refinement ports to AVE-Core and resolves Li +5.5% → +1-2.5%, A47 v9 closes cleanly + atomic-orbital ±2.8% precision claim solidifies.

**"Auditor flagged earlier" attribution on AVE-Protein 20-PDB issue (per agent's doc 99 framing)** — auditor (this entry) does NOT recall flagging AVE-Protein 20-PDB this session. Possible attributions: prior-auditor handoff predating this entry's session start OR agent's misattribution. Per A43 v2 verbatim source needed; not load-bearing for substance (verification still worth doing) but attribution should be accurate.

**Tier C external pre-registration question** — **Are the 3 hardware predictions formally pre-registered to Open Science Framework or equivalent?** Or pre-registered internally in repo predictions.yaml-style tracking? Different external-credibility weight per "what are we missing" turn earlier. Internal repo-level pre-registration is good methodology hygiene but doesn't externally separate "derivation that happens to match data" from "derivation that predicts data we haven't seen." External OSF pre-registration with timestamp + experimental-collaboration buy-in is what provides that separation. Worth verifying Tier C pre-registration formal status as auditor-lane queue item.

**Implication for L3 arc closure framing:**

The "L3 arc was a narrow test of one specific question (corpus electron at K4-TLM substrate)" framing is now visibly only **ONE track among 9**:

- L3 arc = K4-TLM substrate test class (Track A in A45 framing) — produced substrate-canonical findings (A28-A44) AND seven-layer corpus-engine-correspondence debt for K4-TLM electron testing
- AVE-Core analytical-solver class (Track B in A45) — atomic orbitals + baryon ladder verified Tier A
- 7 sibling-repo application tracks (Track C in this A46 framing) — protein-folding, chiral antenna, EM thrust, propulsion, fusion, metamaterials, virtual-media — Tier B/C/D status varies

**Three complementary tracks, each at different verification states. The framework's empirical surface area is substantially broader than the L3 arc's narrow scope. Track A's K4-TLM substrate findings stay real; Track B's analytical-solver validations are now in place; Track C's sibling-repo capability surface has 7 application domains in various states of empirical realization.**

**Honest gut hold at 55-65%, with potential upward movement contingent on Tier B verification cycles:**

- If J^P pattern verifies at 7/8 (per yang_mills.py:torus_knot_gauge_rank()) — substantively stronger empirical anchor → 60-70%
- If AVE-Protein 20-PDB verifies at claimed precision (~30-60 min) — adds protein-folding scale to Tier A → 60-70%
- If Tier C predictions are formally OSF-pre-registered — closes external-credibility gap → 60-70%
- If parent repo's SIR refinement closes A47 v9 (Tier B → A) — Tier A precision claim solidifies → marginal upward
- If multiple verifications land — gut converges 65-75%

**Multi-repo-capability queue extension (held for verification cycles per Rule 12):**

1. **AVE-Protein 20-PDB direct execution** (~30-60 min) — converts Tier B to Tier A; substantive empirical addition if lands at claimed precision
2. **Parent repo SIR refinement port to AVE-Core** — closes A47 v9 if successful; closes ATOMIC_IE_SOLVER_TRACKER Period 3+ gap; recovers substantive parent-repo content
3. **J^P validation via yang_mills.py:torus_knot_gauge_rank()** (~1-2 days) — promotes J^P pattern from Tier B (auditor-flagged-pending) to Tier A or refines match count + identifies outliers
4. **AVE-HOPF Beltrami eigenvalue execution** (~10 min) — converts λ(p,q) formula from Tier B to Tier A
5. **Tier C OSF pre-registration verification** — confirms whether 3 hardware predictions are externally pre-registered or internal-only; substantively different external-credibility weight
6. **Vol 1 axiom mathematics + Vol 3 gravity/cosmology recovery from parent repo** — substantive content recovery; expands AVE-Core's documented empirical/mathematical surface area
7. **AVE-Metamaterials Miller n=5 universality** — extends mass-spectrum activation into materials physics; new domain extension

**Provenance honest at this multi-repo-capability extension:** doc 99 is agent-authored research-tier doc consolidating Explore-agent searches across 9 sibling repos. Tier A claims auditor-side verified (AVE-Core file existence + manuscript citations + agent reproducibility check). Tier B claims explicitly flagged as Explore-agent summaries pending direct verification. Tier C claims agent-reported as pre-registered in repos; external OSF pre-registration formal status not verified at this manual edit. Tier D claims agent-reported as theoretical/skeleton with implementation gaps. Auditor-side flag on J^P pattern's Tier A status (PDG cross-check suggests 4-5/8 not 7/8) + "auditor flagged earlier" attribution (auditor doesn't recall) noted in body. **The framework's empirical record is substantively broader than I had registered coming into this session; the L3 arc's narrow K4-TLM-substrate scope is one track among 9 parallel forward tracks; verification cycles on Tier B + external pre-registration confirmation on Tier C are the next decisive steps for converting claimed empirical surface area to verified.***
