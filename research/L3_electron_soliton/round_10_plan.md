# Round 10+ Research Plan — Six-Direction Comprehensive Sequencing

**Status:** planning doc, approved 2026-04-28 by Grant. Tracked in repo for auditor review + version control.

**Plan-mode source:** `~/.claude/plans/yes-bring-notes-up-binary-giraffe.md` (Claude-internal canonical location). This file is a copy committed into the repo so the auditor can review directly and future amendments are version-controlled via standard commit workflow.

**Document type:** research-tier planning doc, NOT an empirical-result doc. Distinct from numbered docs (78-81 = closure-arc results; 82-88 = Round 10+ result docs to land per this plan). Future planning docs follow same convention: `<arc>_plan.md` non-numbered prefix to avoid colliding with result-doc numbering.

**Amendment workflow:** if the plan needs revision (new findings during execution, scope changes, etc.), edit this file and commit; reference the prior commit hash for delta tracking. No closure-doc-style version-numbering required (this is planning, not empirical record).

---

## Context

The L3 electron-modeling branch closed Mode III canonical + one structural partial positive at [doc 79 v5.1](79_l3_branch_closure_synthesis.md) (commit `6d27e58`); post-closure follow-up landed at [doc 81](81_l3_followup_questions.md) (commit `cfb203a`). Round 10+ is the post-closure research arc that addresses the four surviving structural-reason interpretations + one provisional from doc 79 §7.6.3:

- **(α) Continuum-limit-only** — corpus electron is a continuum-limit object the engine at N=32 cannot host
- **(β) Topology revision** — (2,3) is wrong topology assignment for engine-representable scale
- **(γ) Substrate framing revision** — corpus electron's load-bearing observable isn't the doc 28 §5.1 phasor-trajectory PCA
- **(δ) 3D-axis mapping** — empirically falsified at v5.1 via path α v3
- **(ε) Bound-state-vs-free-state PROVISIONAL** — corpus's R/r=φ² applies to free-electron-specific configuration; Move 5's bounded setup constrains to bound-state-like attractor at different (n,l,m_l)

Path α tested ~2 of ~7 predicted observable dimensions (per [doc 81 §2.3](81_l3_followup_questions.md)); the multi-operator signature (Op14/16/20/22) + doc 26 §4 spatial-moment R/r definition + atomic-orbital ladder are the load-bearing untested pieces.

**Phase 1 exploration finding that revises prior scope:** doc 81 §3.4's "atomic-orbital ladder genuinely missing" was based on auditor cross-repo grep that scoped the wrong directory (`vol_2_microscopic/` doesn't exist; correct directory is `vol_2_subatomic/` plus KB at `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/`). Substantial atomic-orbital framework exists already: hydrogen E_n + a_0 (CODATA-exact), principal/angular/magnetic quantum numbers, MCL multi-electron solver (period 2 mean error 1.2%), K4-saturation Pauli, Op6 radial-node mechanism. Direction 3' scope is therefore "K4-coordinate-mapping integration of existing framework + pressure-tests," NOT "build atomic-orbital framework from scratch." Doc 81 §3.4 should eventually be amended (auditor-lane, not closure-doc work).

## Six directions and their structural-reason coverage

| # | Direction | Tests | Phase 1 finding |
|---|---|---|---|
| 1 | N=128+ lattice escalation | (α) continuum-limit | Memory ~6-8 GB at N=128; cost unprofiled; profile N=64/N=96 first |
| 2 | Topology variation ((p,q) sweep + Hopfion) | (β) topology revision | (2,3) hardcoded in seed funcs; ~300-500 LOC refactor to parametrize on (p,q); NO Hopf invariant code |
| 3 | Multi-operator signature observer | (γ) signature revision | Op14/16/20/22 NOT yet observers; observer pattern clear in `vacuum_engine.py:337-1500` (9 existing) |
| 3' | Substrate-(n,l,m_l) → K4 mapping | (ε) bound-state-vs-free-state | Substantially smaller scope than v5.1 implied; KB vol2 Ch.7 has CODATA-exact hydrogen + (n,l,m_l) framework |
| 4 | Engine fix per doc 75 §6.3 | Cleanliness | <1% effect at A≤2 (Diag A Mode I); E-070 cleanliness, NOT closure-blocking |
| 5 | Mass spectrum at higher q | Framework-level | (q=3,5,7) ladder named in corpus; mass-ratio derivation EXPLICITLY OPEN per doc 80 §2.3 |

## Sequencing plan: 4 phases over ~20-33 fresh sessions

```
Phase 0 (prerequisites, ~1-2 sessions)        — independent
   │
   ├─ Phase 1 (highest info-per-cost, ~8-13)  — parallelizable: Direction 3 ⊥ Direction 3'
   │     │
   │     ├─ Phase 2 (continuum limit, ~4-6)   — needs Phase 0.1 + Phase 1 baseline
   │     │
   │     └─ Phase 3 (topology + mass, ~6-10)  — Direction 2.1 unblocks Direction 5
   │
   └─ Phase 4 (cleanliness, ~1-2)             — independent, interleave anywhere
```

---

## Phase 0 — Infrastructure prerequisites (~1-2 fresh sessions)

Load-bearing for downstream phases; no empirical claims; pure tooling.

### 0.1 — Engine save/load API for Move 5 saved-state caching

**Why:** Phase 1 needs to rerun Move 5's saturated attractor with new observers ~5-8 times (one rerun per operator group). Each rerun currently re-simulates pre-evolve (10P) + selection (5P) windows from scratch (~15 min overhead per rerun). Cached state amortizes this: ~75-120 min saved across Phase 1. Per [Phase 1 Agent 1 finding](81_l3_followup_questions.md), no engine `save()/load()` infrastructure exists.

**Implementation scope:**
- Add `save(path)` / `load(path)` to [`src/ave/topological/vacuum_engine.py`](../../src/ave/topological/vacuum_engine.py) — pickle/npz of K4 + Cosserat full state (V_inc, V_ref, Phi_link, omega, omega_dot, u, u_dot, time index)
- New driver: [`src/scripts/vol_1_foundations/r10_save_move5_state.py`](../../src/scripts/vol_1_foundations/r10_save_move5_state.py) — runs path α v3 setup through end of selection window (15 P), saves engine state to `data/move5_attractor_15p.npz`
- Verification: load saved state, run 1 step, assert engine.time + omega_peak + V_inc snapshot match expected
- Cost: ~3-4 hr implementation + verification

### 0.2 — Universal-operator catalog source consolidation (light)

**Why:** Direction 3 needs canonical Op14/16/20/22 formulas + scale-invariance proofs; currently distributed across `manuscript/ave-kb/common/solver-toolchain.md` + `manuscript/ave-kb/common/axiom-homologation.md` + per-domain docs. Per [Phase 1 Agent 1](81_l3_followup_questions.md), no single catalog file yet.

**Implementation scope:**
- New file: [`manuscript/ave-kb/common/operators.md`](../../manuscript/ave-kb/common/operators.md) — single source-of-truth listing Op1-Op22 with: name, formula, scale-invariance argument, primary citation, implementation pointer (if observer exists)
- Cite [doc 81 §2.2](81_l3_followup_questions.md) as the synthesis basis; cross-link to existing distributed sources
- Keep concise (1 row per op + extended notes for Op14/16/20/22 only)
- Cost: ~2-3 hr (mostly extraction from existing distributed sources)

**Phase 0 verification:** Move 5 saved state loads cleanly; operators.md has all 22 entries with formula + citation.

---

## Phase 1 — Highest information-per-cost (~8-13 fresh sessions, parallelizable)

Direction 3 ⊥ Direction 3' run in parallel; each adjudicates a different structural-reason branch.

### Direction 3 — Multi-operator signature observer (tests (γ), ~5-8 fresh sessions)

Five new observers + joint adjudication on Move 5 saved state. Each observer is a separate pre-reg per A40 (dual-criterion + multi-N + multi-sector, pre-registered up-front).

**3.1 — Spatial-moment R_phase / r_phase observer (~1 session)**
- Implements doc 26 §4 lines 82-94 analytic definition: R_phase = ⟨A(s)⟩_s, r_phase = std(A(s)) along ℓ_node (NOT phasor-trajectory PCA — different observable per [doc 81 §2.1](81_l3_followup_questions.md))
- ℓ_node vs lattice-cell-spacing: at corpus scale, ℓ_node may be sub-cell. Implementation choice: integrate over multi-cell path along bond axis (treat ℓ_node as the bond span, not single cell)
- Pre-reg `P_phase10_spatial_moment_phasor`: Mode I if median R_phase/r_phase = φ² ± 5% across saturated bond-pairs
- Critical files: extend [`src/ave/topological/vacuum_engine.py`](../../src/ave/topological/vacuum_engine.py) Observer subclass; new driver [`src/scripts/vol_1_foundations/r10_spatial_moment_observer.py`](../../src/scripts/vol_1_foundations/r10_spatial_moment_observer.py)

**3.2 — Op14 Z_eff dynamic impedance trajectory observer (~1 session)**
- Z_eff(t) = Z₀/√S(A(t)) per cell; corpus Op14 K4↔Cosserat coupling
- Test vs corpus prediction of trading frequency ~0.020 rad/unit per Move 11b FFT (already empirically observed at ρ(H_cos, Σ|Φ_link|²) = -0.990)
- Pre-reg `P_phase10_op14_z_eff_trajectory`: Mode I if Z_eff modulation FFT peak matches corpus Op14 trading prediction at saturated bond-pairs
- Critical files: same observer pattern; new driver

**3.3 — Op16 c_shear wave-speed freeze observer (~1 session)**
- c_shear(t) = c_base·√S(A(t)) per cell; rest-mass mechanism per Vol 4 Ch 1
- Pre-reg `P_phase10_op16_c_shear_freeze`: Mode I if c_shear → 0 at saturation walls (Γ → -1 sites) within 5% of corpus prediction; Mode III if substrate is asymmetric (only S_ε or S_μ saturates) per §6.7 Meissner framing
- Critical files: same observer pattern; new driver

**3.4 — Op20 ω_regime regime-eigenvalue observer (~1 session)**
- ω_regime = ℓ·c_wave/r_eff at saturated bound state; topology rupture trigger at Regime III→IV transition
- Pre-reg `P_phase10_op20_omega_regime`: Mode I if ω_regime matches ω_C = m_e c²/ℏ ± 5%
- Critical files: same observer pattern; new driver

**3.5 — Op22 M avalanche cascade observer (~1 session)**
- M = 1/(1-S(V)) per cell; nonlinear yield amplification at saturation onset
- Pre-reg `P_phase10_op22_avalanche`: Mode I if M-factor profile at saturated walls matches corpus prediction; tests semiconductor-to-nucleosynthesis cascade mechanism
- Critical files: same observer pattern; new driver

**3.6 — Multi-operator joint adjudication (~1-2 sessions)**
- Run all 5 observers on cached Move 5 saved state (Phase 0.1)
- Joint adjudication: which subset of (3.1, 3.2, 3.3, 3.4, 3.5) passes Mode I? Identifies load-bearing operators for corpus electron signature
- Compare to v5.1 closure: if any subset passes Mode I, doc 79 §7.6.3 (γ) signature revision branch confirmed; closure interpretation reframes from "Mode III on doc 28 §5.1 spec" to "Mode III on phasor-trajectory observable, Mode I on multi-operator signature"
- New research doc: [`82_multi_operator_signature_result.md`](82_multi_operator_signature_result.md) per A48 frozen-extraction-scope (single coherent commit unit per pre-reg)

### Direction 3' — Substrate-(n,l,m_l) → K4 mapping (tests (ε), ~3-5 fresh sessions)

Significantly smaller scope than v5.1 / doc 81 implied per Phase 1 Agent 3 finding. KB vol2 Ch.7 already has substantial framework; gap is K4-coordinate mapping + multiorbital R/r prediction + pressure-tests.

**3'.1 — Pre-test for derivability (~3-4 hr, prerequisite for 3'.2-3'.5)**
- Question: can Op10 c=3 carrier preservation under [Move 10's "non-standard topology" finding](74_r7_k4tlm_lctank_run_result.md) be rewritten as l=2 angular-node-count signature?
- Examine Op10 catalog definition (per Phase 0.2 operators.md) + Move 10 empirical findings (`A²≈0 at top-|ω| cells, sectors spatially decoupled, c=3 carrier matches NONE of standard topology types`) + atomic-orbital (n, l, m_l) standard form per [`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md` lines 90-104](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)
- **If YES:** (ε) has lattice-resolvable instantiation; proceed to 3'.2
- **If NO:** (ε) requires continuum-scale framework; falsify or reframe (ε) as "AVE substrate has no discrete orbital ladder"
- Output: gate-decision documented in [`83_substrate_nlm_pretest.md`](83_substrate_nlm_pretest.md)

**3'.2 — Derive (n,l,m_l) → K4 bond-pair coordinate map (~1-2 sessions)**
- Candidate mappings (to be derived, not assumed):
  - n ↔ standing-wave radial node count (links to Op6 + spatial node structure per [`radial-eigenvalue-solver.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md))
  - l ↔ angular node count from Op10 c-invariant (Move 10's c=3 non-standard might be l=2 signature)
  - m_l ↔ Cosserat ω-axis orientation per [doc 79 §6.6 lines 442-445](79_l3_branch_closure_synthesis.md)
- Test internal consistency: do mappings satisfy n ≥ l+1, |m_l| ≤ l, n_r = n-l-1 (Op6 radial nodes)?
- Critical files: extend [`manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/) with new file `k4-nlm-coordinate-map.md`; reference from research doc

**3'.3 — Predict multiorbital R/r values per (n,l) (~1 session)**
- For each (n, l) configuration, predict bound-state R/r value from first principles using K4-coordinate map + Pauli K4-saturation
- Particular focus: 1s (n=1, l=0), 2s (n=2, l=0), 2p (n=2, l=1), 3s, 3p, 3d configurations
- Output: predicted R/r table for each (n, l) — substrate-native first-principles values, NOT phenomenological fits

**3'.4 — Compare predicted R/r to empirical Move 5 (~3-4 hr)**
- Move 5 + path α v1/v2/v3 empirical R/r ≈ 1.6-9.2 across views; bipolar +x / -x clusters
- Identify which (n, l) prediction matches empirical
- **Mode I (ε confirmed):** specific (n, l) prediction matches empirical R/r within 10%; Move 5 attractor identified as that bound state; doc 79 v5.1 closure interpretation reframes
- **Mode III (ε falsified):** no (n, l) prediction matches; (ε) interpretation falsified; restricts surviving structural reasons to (α)/(β)/(γ)

**3'.5 — He / Li pressure-test (~1 session, optional)**
- Extends KB vol2 Ch.7 MCL solver per [`helium-symmetric-cavity.md`](../../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md) (period 2 mean error 1.2% currently)
- Verify K4-coordinate map predicts He 1s² + Li 1s²2s¹ shell-filling correctly (canonicalizes [doc 79 §6.6 PROVISIONAL Pauli framing](79_l3_branch_closure_synthesis.md))
- Mode I: He IE prediction within 1% of CODATA (24.587 eV); Li 1s²2s¹ structure correctly populated
- Mode III: pressure-test fails; §6.6 PROVISIONAL Pauli framing requires revision

**Phase 1 critical files:**
- [`src/ave/topological/vacuum_engine.py`](../../src/ave/topological/vacuum_engine.py) — 5 new Observer subclasses
- `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/k4-nlm-coordinate-map.md` — new
- [`manuscript/predictions.yaml`](../../manuscript/predictions.yaml) — add P_phase10_* (5 pre-regs Direction 3)
- [`82_multi_operator_signature_result.md`](82_multi_operator_signature_result.md) — new
- [`83_substrate_nlm_pretest.md`](83_substrate_nlm_pretest.md) — new
- [`84_substrate_nlm_derivation.md`](84_substrate_nlm_derivation.md) — new

---

## Phase 2 — N=128 continuum-limit test (~4-6 fresh sessions)

Direction 1 — tests (α) continuum-limit-only branch. Depends on Phase 0.1 (cached state caching) for Phase 1 Direction 3 baseline reuse.

### 1.1 — Profile step() at N=64 + N=96 (~3-4 hr)

**Why:** N=128 cost unprofiled per Phase 1 Agent 1 finding (memory ~6-8 GB est., compute time TBD). Linear or super-linear scaling? Need empirical data to budget Phase 2.3.

**Implementation:**
- New driver: [`src/scripts/vol_1_foundations/r10_n_lattice_profiling.py`](../../src/scripts/vol_1_foundations/r10_n_lattice_profiling.py) — runs 100 steps each at N=32, N=64, N=96; logs wall-time per step + memory footprint
- Output: `r10_n_lattice_profiling_results.json` with scaling curve

**Mode I:** scaling sub-cubic at N=128 extrapolation → proceed to 1.2/1.3
**Mode III:** scaling super-cubic OR memory >16 GB → defer Direction 1, document as infrastructure-blocked

### 1.2 — Path α v1 spec rerun at N=64 (~1 session, ~2-3 hr)

**Why:** Cheap intermediate baseline; if N=64 already shows Mode I, no need for N=128.

**Implementation:**
- Reuse [`src/scripts/vol_1_foundations/r9_path_alpha_bond_pair_phasor.py`](../../src/scripts/vol_1_foundations/r9_path_alpha_bond_pair_phasor.py) pattern; change N_LATTICE = 64
- Pre-reg `P_phase10_path_alpha_n64`: Mode I if R/r=φ² ± 5% on phasor-trajectory PCA at N=64
- Single coherent A48 commit unit

### 1.3 — Path α v1 spec rerun at N=128 (~1-2 sessions, ~5-8 hr run)

**Why:** Direct test of (α) continuum-limit hypothesis. If N=32 Mode III + N=128 Mode I, (α) confirmed.

**Implementation:**
- Same pattern; N_LATTICE = 128, scale R = R_anchor × (128/32) = 40 (preserves corpus aspect ratio at finer resolution)
- Pre-reg `P_phase10_path_alpha_n128`: dual-criterion (R/r=φ²) + (chirality consensus)

### 1.4 — Multi-operator observer rerun at N=128 (~1 session)

**Why:** Cross-check Direction 3 result at higher resolution. If Direction 3 found Mode I on a specific operator at N=32, does it persist at N=128?

**Implementation:**
- Reuse Direction 3 observer infrastructure; rerun all 5 observers on N=128 saturated attractor
- Output: cross-resolution comparison table

### Phase 2 adjudication

**Mode I overall:** N=128 path α + multi-operator both yield φ² → (α) confirmed; corpus revision specifies framework predictions apply at finer-than-N=32 lattice; doc 79 v5.1 closure reframes
**Mode II:** N=128 path α improves toward φ² but doesn't match within 5% → continuum-limit partially confirmed, requires N=256+ extrapolation
**Mode III:** N=128 still Mode III → (α) falsified; restricts to (β)/(γ)/(ε)

---

## Phase 3 — Topology variation + mass spectrum (~6-10 fresh sessions)

Direction 2 + Direction 5 share (p,q) parametrization infrastructure. Direction 2.1 unblocks Direction 5.

### Direction 2 — Topology variation (~3-5 fresh sessions, tests (β))

**2.1 — Refactor seed functions to parametrize on (p,q) (~1-2 sessions, ~300-500 LOC)**

Per [Phase 1 Agent 2 finding](81_l3_followup_questions.md), (2,3) topology is HARDCODED in:
- [`src/ave/topological/cosserat_field_3d.py:777-843`](../../src/ave/topological/cosserat_field_3d.py) — `initialize_electron_2_3_sector` with `theta = 2.0*phi + 3.0*psi` at line 835
- [`src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py:33-122`](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py) — `initialize_2_3_voltage_ansatz` with same structure at line 107

**Refactor:**
- Generalize: `theta = p*phi + q*psi` with (p, q) as parameters
- Adjust chirality weighting (currently `inv_sqrt3 * tetrahedral_dot` for (2,3)) — derive (p,q)-generalized form
- Update envelope formula if confinement radius depends on (p,q)
- Rename: `initialize_electron_p_q_sector(p, q, R_target, r_target, ...)` and `initialize_p_q_voltage_ansatz(p, q, ...)`
- Backward compat: keep `initialize_electron_2_3_sector` as thin wrapper for `(p=2, q=3)` to avoid breaking existing path α drivers

**2.2 — (3,5) cinquefoil seed test (~1 session)**
- Pre-reg `P_phase10_topology_3_5`: setup identical to Move 5 except (p,q) = (3,5) seed
- Tests whether (3,5) hosts a stable saturated attractor at engine-representable scale
- Adjudication: same dual-criterion as path α v1 (R/r + chirality)

**2.3 — (2,5) and (2,7) seed tests (~1 session)**
- Pre-reg `P_phase10_topology_2_5` (proton-corpus q=5) + `P_phase10_topology_2_7` (tau-corpus q=7)
- Tests corpus's (2, q odd) ladder per [doc 80 line 19](80_kelvin_helmholtz_ave_precedent.md)

**2.4 — Hopfion seed test (~1 session, requires new infrastructure)**
- Hopfion is linked-rings, NOT torus knot — requires Hopf invariant detection code (not in repo per Phase 1 Agent 2)
- New file: [`src/ave/topological/hopfion_field.py`](../../src/ave/topological/hopfion_field.py) — Hopfion seed function + Hopf-invariant Q_H extraction
- Pre-reg `P_phase10_hopfion`: tests whether Hopfion is engine-stable at all (independent of φ² geometric prediction)

**2.5 — Topology-knot adjudication (~3-4 hr)**
- Joint adjudication across (2,3), (3,5), (2,5), (2,7), Hopfion runs
- Output: which (p,q) configurations are dynamically stable in K4-TLM substrate? Does ANY non-(2,3) config show Mode I R/r=φ² (suggesting (β) topology revision)?
- New research doc: [`85_topology_variation_result.md`](85_topology_variation_result.md)

### Direction 5 — Mass spectrum at higher q (~3-5 fresh sessions, framework-level research)

Per [doc 80 §2.3 line 52](80_kelvin_helmholtz_ave_precedent.md): "the (2, q odd) restriction is corpus-cited as 'stability rule' but the physical reason is open." This direction adjudicates the open question and derives mass ratios.

**5.1 — Faddeev-Skyrme c=7 scaling (~1 session)**
- Per [`src/ave/topological/faddeev_skyrme.py:18-26`](../../src/ave/topological/faddeev_skyrme.py), c=3 (electron) + c=5 (proton) defined; c=7 (tau) scaling unknown
- Extend `r_opt = κ_FS / c` formula to c=7; verify against existing (c=3, c=5) calibration
- Pre-reg `P_phase11_fs_c_7_scaling`: r_opt at c=7 satisfies internal-consistency constraints

**5.2 — Operator catalog at q=5 (proton, ~1 session)**
- Apply universal-operator catalog (Phase 0.2) at (p=2, q=5) parameter set
- Predict: m_p/m_e ratio from operator combinations at q=5 vs q=3 baseline
- Pre-reg `P_phase11_mass_ratio_proton`: predicted m_p/m_e within 5% of measured 1836.15

**5.3 — Operator catalog at q=7 (tau, ~1 session)**
- Same approach at (p=2, q=7); predict m_τ/m_e
- Pre-reg `P_phase11_mass_ratio_tau`: predicted m_τ/m_e within 5% of measured 3477.23

**5.4 — Joint mass-spectrum adjudication (~3-4 hr)**
- Output: which operators in the catalog set the q-dependent mass scaling? Is the "(2, q odd) restriction" derivable, or does it remain a postulated rule?
- New research doc: [`86_mass_spectrum_higher_q.md`](86_mass_spectrum_higher_q.md)

### Phase 3 critical files

- [`src/ave/topological/cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py) — refactor `initialize_electron_2_3_sector` → `initialize_electron_p_q_sector`
- [`src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py`](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py) — same refactor for voltage ansatz
- [`src/ave/topological/faddeev_skyrme.py`](../../src/ave/topological/faddeev_skyrme.py) — extend c=7 scaling
- [`src/ave/topological/hopfion_field.py`](../../src/ave/topological/hopfion_field.py) — new Hopfion seed + Q_H extraction
- [`manuscript/predictions.yaml`](../../manuscript/predictions.yaml) — P_phase10_topology_* + P_phase11_mass_*
- 2 new research docs (85, 86)

---

## Phase 4 — Engine fix cleanliness (~1-2 fresh sessions, low priority)

Direction 4 — apply [doc 75 §6.3](75_cosserat_energy_conservation_violation.md) T_kinetic saturation fix. Independent of all other phases; can interleave anywhere.

### 4.1 — T_kinetic saturation fix (~1 session)

Per Phase 1 Agent 1 finding, fix prescription clear:
- Modulate kinetic energy in [`src/ave/topological/cosserat_field_3d.py:1204-1209`](../../src/ave/topological/cosserat_field_3d.py): `T = ½·(ρ·S)·|u̇|² + ½·(I_ω·S)·|ω̇|²`
- Update `step()` integrator at `cosserat_field_3d.py:1228-1285` to use `ρ·S` and `I_ω·S` (currently constants)
- Note: integrator update is non-trivial; requires careful rewrite of velocity-Verlet step to preserve symplectic structure with state-dependent inertia

### 4.2 — Diag A high-amp scan rerun (~3-4 hr)

- Existing scan at `src/scripts/vol_1_foundations/r8_diag_a_supplementary_high_amp_results.json` shows asymmetry detectable at A≥4 only
- Rerun post-fix: verify asymmetry vanishes (Diag A passes Mode I across full A∈[0.1, 5] range)

### 4.3 — Path α v3 rerun for negligibility verification (~3-4 hr)

- Per [doc 75 line 140](75_cosserat_energy_conservation_violation.md): "the reason is NOT V·S, T·1 wave-speed drift" — verify v3's Mode III reproduces post-fix
- Pre-reg `P_phase10_engine_fix_negligibility`: path α v3 result identical (Mode III) within ±5% post-fix

### Phase 4 critical files

- [`src/ave/topological/cosserat_field_3d.py:1204-1285`](../../src/ave/topological/cosserat_field_3d.py) — T_kinetic + step() integrator update
- [`87_engine_fix_e070_result.md`](87_engine_fix_e070_result.md) — new

---

## Dependency / parallelization summary

| Phase | Depends on | Can parallelize with |
|---|---|---|
| 0.1 (engine save/load) | — | 0.2, 4.1 |
| 0.2 (operator catalog) | — | 0.1, 4.1 |
| 1 Direction 3 | 0.1, 0.2 | Direction 3' |
| 1 Direction 3' | 0.2 | Direction 3 |
| 2 (Direction 1) | 0.1, Phase 1 baseline | Phase 3 |
| 3 Direction 2 | — (or 0.1 for caching) | Phase 2 |
| 3 Direction 5 | 2.1 ((p,q) parametrization) | — |
| 4 (Direction 4) | — | Any phase |

**Parallelization opportunities:**
- Phase 0.1 ⊥ Phase 0.2 ⊥ Phase 4.1 (all independent infrastructure)
- Phase 1 Direction 3 ⊥ Direction 3' (different scopes, both leverage Move 5 cache)
- Phase 2 ⊥ Phase 3 (after Phase 1 lands)
- Phase 4 interleaves anywhere

**Critical path:** 0.1 + 0.2 → Phase 1 → Phase 2 → Phase 3 (Direction 5 specifically). Phase 4 is off critical path.

---

## Adjudication framework: which structural reason wins?

Round 10+ closure adjudication after all phases complete:

| Branch | Test direction | Mode I means | Mode III means |
|---|---|---|---|
| (α) Continuum-limit-only | Direction 1 (N=128) | Corpus electron at finer-than-N=32 | (α) falsified |
| (β) Topology revision | Direction 2 ((p,q) sweep) | Different (p,q) hosts corpus electron | (β) falsified |
| (γ) Signature revision | Direction 3 (multi-operator) | Some operator subset matches φ²/chirality | (γ) falsified |
| (ε) Bound-state-vs-free-state | Direction 3' (substrate-(n,l,m_l)) | Move 5 attractor identified as specific (n,l) | (ε) falsified |

**Possible Round 10+ outcomes:**
1. **One branch wins:** specific structural reason confirmed; framework canonicalizes that revision; closure shape becomes Mode I on that test
2. **Multiple branches partial:** some operators in Direction 3 match + some (n,l) in Direction 3' matches → composite reframe needed
3. **All branches Mode III:** corpus electron is genuinely not at engine-representable scale across all tested observables/topologies/configurations; framework requires deeper revision (could be additional structural reason (ζ) or framework-level reformulation)

---

## Out-of-scope (this Round 10+ plan deliberately excludes)

- Vol 1 Ch 8 manuscript revision per [doc 79 §9 corpus revision package](79_l3_branch_closure_synthesis.md) — auditor-lane editorial work
- Other AVE volumes (Vol 5 biology, Vol 6 periodic table, etc.) — separate research arcs
- Manuscript Vol 4 Ch 1 fine-structure derivation cross-check — couples to L3 but separate scope
- AVE-Protein, AVE-APU, AVE-Fusion sibling-repo work
- 47 public claims verification ledger across framework
- Auditor-lane post-closure bundle (manual r8.10 / A43 v2 / A60-62 / Rule 12 v2 / §9 corpus revision package) — auditor's own cadence

---

## Verification

**Per-phase verification:**

| Phase | Verification |
|---|---|
| 0.1 | Move 5 cached state loads; engine.step() produces identical next-state to fresh-run baseline |
| 0.2 | operators.md has all 22 entries with formula + scale-invariance + citation; cross-references resolve |
| 1 Direction 3 | 5 pre-regs (P_phase10_*) frozen; observers pass smoke tests; joint adjudication doc 82 lands with Mode-I/II/III conclusions per operator |
| 1 Direction 3' | 3'.1 derivability gate decided; if YES → 3'.2-3'.5 land with substrate-(n,l,m_l) map + multiorbital R/r prediction + Move 5 (n,l) match adjudication + He/Li pressure-test |
| 2 | N=128 path α + multi-operator results land; (α) Mode-I/II/III adjudication |
| 3 Direction 2 | (p,q) parametrization passes path α v1 (2,3) regression test (no behavior change at (p,q)=(2,3)); (3,5)/(2,5)/(2,7)/Hopfion runs land; (β) adjudication |
| 3 Direction 5 | mass-ratio predictions land for q=5, q=7 within 5% of measured |
| 4 | Diag A passes Mode I across A∈[0.1,5]; path α v3 reproduces Mode III (negligibility verified) |

**Round 10+ closure verification:**
- All phases land their pre-reg results in [`manuscript/predictions.yaml`](../../manuscript/predictions.yaml) + corresponding research docs (82-87)
- Final synthesis doc [`88_round_10_synthesis.md`](88_round_10_synthesis.md) — Mode-I/II/III adjudication across all four structural-reason branches; identifies which branch (if any) wins
- L3 v5.1 closure interpretation reframes if any branch wins Mode I; manuscript Vol 1 Ch 8 revision queued (auditor-lane) per outcome

---

## Estimated cost

| Phase | Sessions | Notes |
|---|---|---|
| Phase 0 | 1-2 | Infrastructure prereqs |
| Phase 1 Direction 3 | 5-8 | 5 observer subgroups + joint adjudication |
| Phase 1 Direction 3' | 3-5 | Pre-test + derivation + comparison + pressure-test |
| Phase 2 | 4-6 | Profile + N=64 + N=128 + multi-op rerun |
| Phase 3 Direction 2 | 3-5 | Refactor + 4 topology runs + adjudication |
| Phase 3 Direction 5 | 3-5 | c=7 + q=5,7 mass ratios + adjudication |
| Phase 4 | 1-2 | Cleanliness, interleavable |
| **Total** | **20-33** | Over ~8-16 weeks at current cadence |

Branches at Phase 1: if Direction 3 OR Direction 3' lands Mode I, several downstream directions may lose motivation (e.g., if (γ) signature revision confirmed, Direction 1 N=128 escalation becomes lower priority). Plan adapts based on Phase 1 results.
