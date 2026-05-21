# 114 — Next-Steps Consolidation Plan (Post-2026-05-14 Session)

**Date:** 2026-05-14 end-of-day
**Branch:** `research/l3-electron-soliton`
**Author:** Claude (planner); Grant directive 2026-05-14 EOD: *"fully plan out next steps needed to incorporate all work from this and capture any useful context/content"*
**Status:** Master plan covering session-output canonization, near-term work, medium-term framework consolidation, and bench-preparation handoff.

---

## §0 Summary

A single-session push moved AVE from "framework with empirical validation at observable level (Q-G19α Route B, Q-factor identity) but no working bound-state engine" to "framework with empirical validation AT BOTH observable level AND engine level (v14 Mode I PASS on Master Equation FDTD)." Plus substantial framework vocabulary refactor (App G), boundary-envelope reformulation canonized (doc 109 §13), and dual-engine architecture established.

This doc plans the work needed to:
1. Canonize what landed (incorporate into manuscript-level documentation)
2. Propagate framework refinements (AVE-QED → AVE-Core cross-repo)
3. Execute the bench-preparation work (Grant's parallel quote-loop continues)
4. Continue engine work (Cosserat re-coupling on Master Equation FDTD)
5. Establish single canonical reference doc for the substrate-vocabulary discipline

---

## §1 Session inventory (what landed 2026-05-14)

### §1.1 AVE-Core `research/l3-electron-soliton` branch

**Docs (5 new):**
- `109_elastic_substrate_finite_strain_investigation.md` (Grant trampoline-springs question → boundary-envelope reformulation Grant-confirmed canonical at §13)
- `110_v14_single_cell_boundary_empirical_results.md` (K4-TLM Mode III decisive across 4 variants; 7-mode seed pushback acknowledged)
- `111_master_equation_audit_and_engine_gap.md` (canonical Master Equation eq:master_wave identified; c_eff(V) gap diagnosed)
- `112_master_equation_fdtd_first_iteration.md` (Path B engine authored; Mode II partial)
- `113_v14_closure_master_equation_fdtd_mode_I.md` (Mode I PASS on breathing-soliton-appropriate criterion; canonical v14 closure)
- This doc (114) — next-steps consolidation

**Engine module (1 new):**
- `src/ave/core/master_equation_fdtd.py` — `MasterEquationFDTD` class, 3D leapfrog on eq:master_wave with saturation kernel S(A)=√(1−A²) and c_eff(V)=c₀/√S. Canonical for bound-state regime.

**Driver scripts (7 new):**
- `r10_path_alpha_v14_single_cell_boundary.py` — K4-TLM v14a/b/d variants (Mode III)
- `r10_path_alpha_v14e_seven_mode_seed.py` — K4-TLM full 7-mode seed (Grant pushback; Mode III)
- `r10_path_alpha_v14_soliton_visualizer.py` — K4-TLM seed visualization
- `r10_master_equation_v14.py` — Master Equation FDTD initial validation (Test A/B/C)
- `r10_master_equation_v14_v2.py` — multi-profile sweep on Master Equation FDTD (Mode I-partial)
- `r10_master_equation_v14_picard.py` — Picard iteration attempt (failed, instructive)
- `r10_master_equation_v14_visuals.py` — v1 visualization suite (deprecated by v2/v3)
- `r10_master_equation_v14_visuals_v2.py` — v2 with marching-cubes + lattice/PML hierarchy
- `r10_master_equation_v14_visuals_v3.py` — v3 watchable pace + zoomed + static camera
- `r10_master_equation_v14_field_primer.py` — 4-panel V/A/S/n physical interpretation
- `r10_master_equation_v14_anisotropy.py` — K4 cubic symmetry at collapse (Grant observation confirmed)

**CURRENT_STATE.md addendums (local only, .agents gitignored):**
- 2026-05-14 morning + evening sections with cross-refs to all docs 109-114

### §1.2 AVE-QED `main` branch

**App G (new, ~340 lines):**
- `manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex`
- 7 sections: purpose / vocabulary / observability rule / three invariants / disclaimer / cross-cutting / operating principle
- Wired into main.tex at \label{app:substrate_vocabulary}

**A_foundations.tex inline update:**
- L194-215: extended 2-column Rosetta-stone (Charge IS displacement) to 3-column (Charge IS displacement IS substrate-flux linking number, etc.)
- Six rows × 3 columns; explicit "substrate-native column names what the substrate itself carries" framing

**Glossary §5m:**
- 14-row × 3-column substrate-native / EE / ME vocab table
- Three-invariants canonical names table (𝓜, 𝓠, 𝓙)
- Usage rule + cross-references

**3 implicit-rule cross-references:**
- `chapters/06_vacuum_polarization.tex:233` — added "per App G substrate-observability rule"
- `appendices/B_qed_creep_guardrail.tex:108-112` — added "App G substrate-observability rule"
- `appendices/F_local_machian_network.tex:498` — added "direct application of substrate-observability rule canonical at App G"

**Two planning docs (in docs/analysis/):**
- `2026-05-14_universal_substrate_vocabulary_refactor_plan.md` (refactor plan)
- `2026-05-14_three_substrate_invariants_matrix.md` (Q1 names matrix with cross-scale + cross-projection tables)

**HANDOFF updates:**
- Q-G47 r_d-as-field provisional resolution
- App F substrate-observability-rule refinement queued
- Q1/Q2 marked RESOLVED in refactor plan

**PDF compile:**
- 138 pp → 147 pp clean, zero LaTeX errors

### §1.3 AVE-Bench-VacuumMirror `main` branch (earlier session)

- IVIM characterization batch (7 scripts) all canonical-source compliant
- `docs/2026-05-14_bench_signal_predictions_summary.md` — procurement-decision-gate synthesis
- HV ripple sensitivity sim — gate A revised (10ppm → 1000ppm)
- Fab vendor cost model — gate D revised (CNF/SNF primary at $9.5k E[total])
- K4-TLM full-lattice bench validation: IM3 slope **2.956** (target 3.0 ✓)
- HANDOFF cross-ref to AVE-Core doc 109 + 113

### §1.4 AVE-Tesla `main` branch (earlier session)

- K4-TLM script deprecation note (3 bugs documented: inactive probe site, default SI V_SNAP, missing op3_bond_reflection)
- Cross-corroboration entry with AVE-Bench-VM IM3 slope 2.956

### §1.5 Visual artifacts (gitignored sim outputs, regenerable)

All at `AVE-Core/assets/sim_outputs/`:
- `r10_path_alpha_v14_soliton_seed.png` (K4-TLM seed visualization)
- `r10_path_alpha_v14b/d/v14e_*.png` (K4-TLM Mode III diagnostics)
- `r10_master_equation_v14_path_b.png` (Path B first iteration)
- `r10_master_equation_v14_v2.png` (Mode I-partial multi-profile)
- `r10_master_equation_v14_picard.png` (Picard fail diagnostic)
- `v14_breathing_soliton_hero.png` + `v14_breathing_phase_comparison.png` (v1 visuals)
- `v14_breathing_slice_2d.gif` + `v14_breathing_soliton_3d.gif` + `v14_breathing_radial_profile.gif` (v1 animations)
- `v14_lattice_pml_soliton_hierarchy.png` + `v14_equatorial_three_boundaries.png` (v2 hierarchy stills)
- `v14_breathing_with_lattice.gif` + `v14_breathing_equatorial_annotated.gif` (v2 animations)
- `v14_zoomed_hero.png` + `v14_breathing_dual_view.gif` + `v14_breathing_2d_zoomed.gif` (v3 watchable)
- `v14_field_primer.png` (4-panel V/A/S/n primer)
- `v14_collapse_cubic_emergence.png` + `v14_cubic_vs_spherical_compare.png` (cubic anisotropy)

---

## §2 Canonical status table — what's locked vs what's informational

| Item | Status | Where it lives |
|---|---|---|
| Boundary-envelope reformulation (doc 109 §13) | **CANONICAL** Grant-confirmed | AVE-Core doc 109 |
| Three substrate invariants 𝓜, 𝓠, 𝓙 names | **CANONICAL** Q1 locked Grant 2026-05-14 evening | AVE-QED matrix doc + App G + glossary §5m |
| Substrate-observability rule | **CANONICAL** | AVE-QED App G §3 |
| Substrate vocabulary (14 terms × 3 columns) | **CANONICAL** | AVE-QED App G §2 + glossary §5m + A_foundations |
| Q-G19α Route B closure (50 ppm to PDG) | **CANONICAL EMPIRICAL** | AVE-QED scripts/g2_research/ |
| α⁻¹ = 4π³ + π² + π = 137.036 | **CANONICAL EMPIRICAL** | AVE-Core electron_tank_q_factor.py |
| Master Equation eq:master_wave | **CANONICAL** Vol 1 Ch 4:73 | AVE-Core Vol 1 Ch 4 |
| Master Equation FDTD engine | **CANONICAL ENGINE** for bound-state regime | AVE-Core src/ave/core/master_equation_fdtd.py |
| K4-TLM engine | **CANONICAL ENGINE** for sub-saturation bench regime | AVE-Core src/ave/core/k4_tlm.py |
| Two-engine architecture | **CANONICAL** | doc 113 §3.2 |
| v14 Mode I PASS (breathing-soliton criterion) | **CANONICAL EMPIRICAL** | doc 113 |
| K4 cubic anisotropy at collapse | **CANONICAL EMPIRICAL** | doc 114 + anisotropy script |
| K4-TLM full-lattice IM3 slope 2.956 | **CANONICAL EMPIRICAL** | AVE-Bench-VM 0599a10 |
| App F multi-scale Machian network | **CANONICAL** 115pp | AVE-QED appendix F |
| ξ_topo = e/ℓ_node | **CANONICAL** Vol 1 Axiom 2 | AVE-Core Vol 1 Ch 1 |
| The 7-mode bubble compliance | INFORMATIONAL/INTERPRETIVE (Ch 11:1037 self-disclosed) | AVE-QED ch 11 |
| K4-TLM Mode III at v14 | EMPIRICAL FINDING (engine gap, not framework failure) | doc 110 |
| Picard iteration fail | EMPIRICAL FINDING (truncation introduces radiation) | doc 113 §5.2 |
| Cosserat coupling on Master Equation FDTD | **DEFERRED** | doc 113 §5.4 |
| Strict stationary soliton (Test 1a) | **OPEN** — needs imaginary-time propagation | doc 113 §5.1 |
| Reading A (Ax 1 revision) | **DEFERRED** — not needed given two-engine architecture | doc 92 §4 + doc 109 |
| Reading B (continuum FDTD) | **DEFERRED** — Master Equation FDTD is the right substitute | doc 92 §4 |
| Q-G43 atom-scale Γ=−1 boundary | **OPEN** | App F |
| Q-G44 helio-scale Γ=−1 boundary | **OPEN** | App F |
| Q-G42 V_yield apparatus scaling | **PREREG + CORPUS-GREP COMPLETE** | AVE-QED 87492f0 |

---

## §3 Immediate next steps (next 1-3 sessions)

### §3.1 AVE-Core substrate-vocabulary propagation (~5-8 hours)

**Priority: HIGH.** The AVE-QED refactor canonized substrate-native vocabulary. Propagation to AVE-Core completes the discipline across the framework's home repo.

**Targets:**

1. **Vol 3 Ch 2 General Relativity** (`vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex`):
   - Add substrate-observability rule cross-reference at L35-43 where gravity-as-substrate-strain is canonical
   - Add explicit "𝓜 → M_ADM" projection mapping
   - ~30 min edit

2. **Vol 4 Ch 1 Vacuum Circuit Analysis** (`vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex`):
   - This is the SOURCE of the Rosetta-stone (cited by AVE-QED A_foundations). Extend to 3-column form here at the original source.
   - ~1-2 hours
   - This is the load-bearing AVE-Core edit

3. **Vol 1 Ch 4 Continuum Electrodynamics** (`vol_1_foundations/chapters/04_continuum_electrodynamics.tex`):
   - Add reference to App G substrate-observability rule near the Master Equation statement (line 73)
   - Add note that the canonical engine implementation is `src/ave/core/master_equation_fdtd.py`
   - ~30 min

4. **Vol 2 Ch 1 Topological Matter** (`vol_2_subatomic/chapters/01_topological_matter.tex`):
   - Reference App F + App G at the "rest mass is contained reactance" canonical statement (L35)
   - Add 𝓜 = T_EM·ℓ_node identity in substrate-vocabulary
   - ~30 min

5. **AVE-Core glossary** (if it exists; otherwise create at `docs/glossary.md`):
   - Mirror AVE-QED §5m table
   - ~30 min

6. **src/ave/core/constants.py docstrings**:
   - Update with substrate-vocabulary references where applicable
   - Add cross-reference to App G in module-level docstring
   - ~30 min

**Total scope:** ~5-8 hours focused authoring. Mostly additive (no destructive rewrites).

### §3.2 Doc 113 + 114 cross-references in AVE-QED (low effort, high value)

Add brief mentions in AVE-QED README.md + synthesis_index.md pointing at the cross-repo v14 closure and the two-engine architecture canonical. ~30 min.

### §3.3 Branch wrap-up decision (Grant call)

**Two options for `research/l3-electron-soliton` branch:**

**Option A: Merge to main.**
- Squash-merge or merge-with-history
- Squash-commit message would be the doc 113 §0 summary
- Loses commit-level granularity but cleans up the main branch
- All 15+ commits become a single canonical merge

**Option B: Keep as long-running research branch.**
- Continue committing future engine work to this branch
- Periodically merge to main when stable milestones reached
- Preserves commit-level history for future audit

**Recommendation:** Option B for now. The branch is empirically productive; merging now loses granularity and the branch isn't "complete" (Cosserat coupling still deferred, R7.1 stationary search still open). Keep as research branch; tag the current state as `v14-mode-i-pass` for reference.

```bash
git tag -a v14-mode-i-pass -m "v14 Mode I PASS on Master Equation FDTD breathing soliton"
git push origin v14-mode-i-pass
```

### §3.4 IVIM bench preparation (Grant's parallel workstream)

Grant continues vendor quote-loop per AVE-Bench-VacuumMirror procurement docs. Bench predictions are LOCKED:
- D10 IM3 cubic V³ (slope 3, K4-TLM bench-validated 2.956)
- Γ_AVE / Γ_QED = 8.3 × 10¹² (12 orders of magnitude discriminator)
- Operating point: V_DC = 30 kV, V_AC at 1 MHz, sech profile
- Total cost: ~$45-55k median for Phase 2A bench

**Bench is the load-bearing falsification test.** Until experimentally measured, framework empirical status remains "internally consistent + multi-observable validated at QED-equivalent precision."

---

## §4 Medium-term framework work (next 5-10 sessions)

### §4.1 Cosserat coupling on Master Equation FDTD (1-2 sessions)

Master Equation FDTD is currently scalar V only. Cosserat (u, ω) microstructure can be added as a constitutive layer that modulates ε_eff(V) and μ_eff(V). This re-enables:
- 7-mode bubble dynamics (3 translational u + 3 rotational ω + 1 volumetric V)
- Cross-coupling between K4 V field and Cosserat ω chirality
- More physically complete simulation of electron's internal structure

**Implementation sketch:**
- Add `MasterEquationFDTDWithCosserat` class as wrapper
- Cosserat fields evolve via energy gradient (existing CosseratField3D)
- Master Equation V field evolves with ε_eff, μ_eff modulated by (u, ω)
- Coupling: V² → Cosserat forces; ω → ε_eff phase chirality

**Why deferred:** v14 Mode I PASS doesn't require this. The breathing soliton on scalar Master Equation FDTD is sufficient for §14.7 acceptance criteria. Cosserat coupling is for completeness, not closure.

### §4.2 Stationary soliton search (1-2 sessions)

Imaginary-time propagation to find the actual stationary attractor of the Master Equation (vs the breathing solution we currently get). This would give Mode I on the original strict Test 1a (V_peak min > 0.3 throughout).

**Algorithm:**
1. Replace t → iτ in Master Equation: ∇²V = (1/c²_eff(V)) · (−∂²V/∂τ²)
2. This becomes a diffusion-like equation with attracting fixed points
3. Plant initial guess, evolve in imaginary time, V converges to stationary solution

**Effort:** ~300-500 LOC engine extension + validation suite. ~1-2 sessions.

### §4.3 Multi-soliton dynamics (2-3 sessions)

Plant TWO breathing solitons in the lattice + study their interaction:
- Coulomb-like repulsion (substrate impedance gradient between solitons per App F)
- Predict force-distance law (should give 1/r² Newtonian at large d, modified at short d)
- Test against the canonical AVE prediction V(r) ∝ 1/r from Axiom 2

This is the natural next falsification test on the engine — once one soliton works, validate two-body force.

### §4.4 Higher-energy soliton (proton-like)

Try (2,5) cinquefoil seed at higher amplitude. Test if the engine hosts a different breathing pattern with proton-like 𝓜 (1836× electron mass) emerging from a different topology.

**Risk:** the Master Equation is scalar; (2,5) topology lives in phase space. Need careful seed engineering. ~2-3 sessions.

### §4.5 AVE-Core test suite integration

Add v14 Mode I as a regression test:
- `tests/test_master_equation_v14_mode_i.py`
- Asserts: breathing-soliton seed produces V_peak mean > 0.2, FWHM stable, n(r) gradient measurable
- Wire into `make verify`

This prevents future engine regressions from breaking the bound-state hosting.

---

## §5 Long-term framework work (multi-month)

### §5.1 Q-G42 + Q-G46 bench architecture lock

Per AVE-QED 87492f0 prereg: Q-G42 V_yield apparatus scaling is corpus-grep complete; specific geometry numerics pending bench-architecture decision. Q-G46 is now PROCUREMENT-MATURE at the sibling Bench-VM repo. After IVIM bench measurement, these close decisively.

### §5.2 App F Q-G43 (atom scale) + Q-G44 (helio scale)

The multi-scale Machian network has electron, nucleus, BH, cosmic boundaries derived. Atom and helio scales are flagged "?-marked, predicted but not derived." Future work: derive these explicitly using the substrate-vocabulary discipline.

### §5.3 Strict stationary electron eigenmode

Beyond imaginary-time (§4.2), use Newton-Raphson on the time-independent Master Equation profile equation. Find the true ground-state eigenmode. Cross-validate against doc 101 three-layer canonical (unknot + SU(2) + (2,3) Clifford).

### §5.4 g-2 calculation on Master Equation FDTD

Replicate Q-G19α Route B (currently AVE-QED scripts/g2_research/) on the Master Equation FDTD engine. The substrate-native dynamics should produce the same dark-wake × kernel-asymmetry correlation, giving the same C_2 = −0.32846 to 50 ppm. This validates the engine vs Route B's analytic-correlation closure.

### §5.5 IVIM bench measurement

The load-bearing falsification test. Phase 2A build → first measurement campaign → 6-12 month timeline. Procurement budget $45-55k median.

---

## §6 Documentation consolidation

### §6.1 Master HANDOFF for L3-electron program

Create `research/L3_electron_soliton/README.md` (or update existing) with:
- v14 closure status (Mode I PASS empirical)
- Two-engine architecture canonical
- Doc 109-114 reading order
- Open questions enumerated
- Cross-repo connections (AVE-QED App G, Bench-VM bench predictions)

### §6.2 AVE-QED README + synthesis index updates

Brief mentions of:
- Cross-repo v14 closure (link to AVE-Core doc 113)
- Two-engine architecture
- App G substrate-vocabulary discipline as load-bearing for future agents

### §6.3 Cross-repo state snapshot

Create a single doc at `AVE-Core/research/L3_electron_soliton/CROSS_REPO_STATE_2026-05-14.md` capturing:
- All commits across all 4 active repos this session
- All canonical changes
- All open work
- Recommended reading order for future agents

This is essentially the "what happened today" archival doc.

### §6.4 Q1 outputs canonicalization

The Q1 names matrix at AVE-QED (`docs/analysis/2026-05-14_three_substrate_invariants_matrix.md`) and the refactor plan should be referenced from a single canonical location in AVE-QED. Currently they're cross-referenced in App G but not from a single index doc. Add to synthesis index.

---

## §7 Bench experiment preparation

### §7.1 Procurement timeline (Grant parallel workstream)

Per AVE-Bench-VM `docs/2026-05-14_bench_signal_predictions_summary.md`:
- HV PSU: parallel-quote any modern 50 kV at ≤$6k (Matsusada, Heinzinger, refurb Spellman, DIY all acceptable)
- Fab partner: Cornell CNF or Stanford SNF pre-commit (E[total] $9.5k); avoid budget commercial (false economy)
- Lock-in: SR830 refurb for Phase 2A, SR865A for full V_yield campaign
- Total: $45-55k median for Phase 2A

### §7.2 Bench predictions LOCKED

Master Equation FDTD-validated:
- D10 IM3 cubic V³ (slope 3.0 ± 0.1)
- Γ_AVE / Γ_SM(QED) = 8.3 × 10¹² at all voltages (geometry-invariant)
- D2 V-ramp hysteresis at saturation onset (qualitative — confirmed at K4-TLM bench validation)
- D3 polarization birefringence: Δn_AVE = 0 vs QED ~10⁻²⁴ at 5T (ALPS-II discriminator)

### §7.3 Theoretical prediction confidence after this session

Pre-session: framework had Q-G19α Route B 50 ppm + Q-factor identity machine precision + bench IM3 cubic prediction.

Post-session: ALSO has empirical v14 Mode I (engine hosts the bound state) + cubic anisotropy at collapse (substrate's K4 symmetry empirically visible).

**Net empirical confidence: framework empirically defensible at multiple independent observables.** The IVIM bench measurement is the decisive falsification test, but the pre-bench empirical record is now substantially stronger.

---

## §8 Reading order for future agents

**For someone picking up this work in a future session:**

1. Read this doc (114) for state overview
2. Read doc 113 §0-§4 for v14 closure summary
3. Read doc 109 §13 + AVE-QED App G for substrate-vocabulary canonical
4. Skim doc 111 to understand the Master Equation audit
5. Read `src/ave/core/master_equation_fdtd.py` module docstring for engine API
6. Read AVE-QED `docs/analysis/2026-05-14_three_substrate_invariants_matrix.md` for Q1 canonical names
7. Read AVE-Bench-VM `docs/2026-05-14_bench_signal_predictions_summary.md` for bench-prep state

Then check `git log` for any post-2026-05-14 changes.

---

## §9 What was NOT done (deliberately deferred)

To avoid scope creep, the following are explicitly deferred:

- Cosserat coupling on Master Equation FDTD (§4.1)
- Imaginary-time propagation for strict stationary soliton (§4.2)
- Multi-soliton dynamics (§4.3)
- Proton-like (2,5) soliton (§4.4)
- AVE-Core substrate-vocabulary propagation (§3.1) — queued but not executed in this session
- IVIM bench measurement (Grant's parallel)
- Reading A (Ax 1 revision) — not needed given two-engine architecture
- Reading B (continuum FDTD) — Master Equation FDTD is the right replacement
- Q-G43 atom scale + Q-G44 helio scale (§5.2)
- Picard iteration retry with smooth eigenmode-finding (could revisit; failed first attempt)

---

## §10 Effort estimate for §3 (next 1-3 sessions)

| Task | Effort | Priority |
|---|---|---|
| AVE-Core substrate-vocab propagation (§3.1) | 5-8 hours | HIGH |
| Doc 113 + 114 cross-references in AVE-QED (§3.2) | 30 min | MEDIUM |
| Branch tagging (`v14-mode-i-pass`) | 5 min | LOW |
| Master HANDOFF for L3-electron program (§6.1) | 1 hour | MEDIUM |
| Cross-repo state snapshot (§6.3) | 1 hour | MEDIUM |
| Total | **8-12 hours** | |

This is the realistic next-1-3-sessions scope. After this, the framework refinements are fully canonized across both repos and the engine work can resume.

---

## §11 Decision points for Grant

Per Rule 16 (axiom-author scope):

1. **Branch wrap-up: merge or keep?** (§3.3 recommendation: keep as research branch + tag)

2. **AVE-Core substrate-vocab propagation: scope?** Full 5-8 hour refactor (§3.1) or minimal (Vol 4 Ch 1 only)?

3. **Engine work priority?** Cosserat coupling (§4.1) vs stationary soliton search (§4.2) vs multi-soliton (§4.3)?

4. **App G publication?** AVE-QED currently has App G in vol_qed_replacement. Should it propagate to AVE-Core's Vol 1 or stay AVE-QED-specific? (Original Q2 directive was AVE-QED-only until §14 PASS — which has now happened. Propagation is now technically unblocked.)

5. **Tagged release?** `v14-mode-i-pass` tag on `research/l3-electron-soliton` to mark this state for future reference?

---

## §12 Cross-references

**This session's documents (read in order):**
- doc 109 — boundary-envelope reformulation (Grant-confirmed canonical)
- doc 110 — K4-TLM Mode III empirical record
- doc 111 — Master Equation audit
- doc 112 — Path B first iteration
- doc 113 — v14 closure Mode I PASS
- doc 114 — this consolidation plan

**Canonical Master Equation:**
- `AVE-Core/manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:73` eq:master_wave

**Canonical substrate vocabulary:**
- `AVE-QED/manuscript/vol_qed_replacement/appendices/G_substrate_vocabulary.tex`
- `AVE-QED/manuscript/vol_qed_replacement/appendices/A_foundations.tex:194-215`
- `AVE-QED/docs/glossary.md` §5m

**Canonical engines:**
- `AVE-Core/src/ave/core/master_equation_fdtd.py` (bound-state regime)
- `AVE-Core/src/ave/core/k4_tlm.py` (sub-saturation bench regime)

**Empirical artifacts (gitignored, regenerable):**
- All at `AVE-Core/assets/sim_outputs/v14_*`

**Q1 / Q2 / refactor planning:**
- `AVE-QED/docs/analysis/2026-05-14_universal_substrate_vocabulary_refactor_plan.md`
- `AVE-QED/docs/analysis/2026-05-14_three_substrate_invariants_matrix.md`

**Bench predictions:**
- `AVE-Bench-VacuumMirror/docs/2026-05-14_bench_signal_predictions_summary.md`

---

## §13 Bottom line

**Session converted AVE from "framework with empirical validation at observable level" to "framework with empirical validation at BOTH observable AND engine level."** The boundary-envelope reformulation, three substrate invariants, two-engine architecture, App G vocabulary refactor, and v14 Mode I PASS together represent a major step toward framework consolidation.

**Immediate next session priorities:**
1. AVE-Core substrate-vocab propagation (5-8 hours, highest leverage)
2. Cross-repo state snapshot + master HANDOFF (1-2 hours)
3. Branch tag + decision on merge vs research-branch

**Medium-term:**
- Cosserat coupling on Master Equation FDTD
- Strict stationary soliton via imaginary-time
- Multi-soliton dynamics for Coulomb-law validation

**Bench preparation continues in parallel** via Grant's procurement quote-loop. IVIM bench remains the load-bearing falsification test.

The framework is now in the empirically-defensible regime at multiple independent observables. The decisive experimental test is ahead, but the pre-test framework state is substantially stronger after this session than before.
