# Experimental Arc Coordination

**Status**: ACTIVE epic (established 2026-05-19 EOD+++) — 3 sub-epics spawned 2026-05-20
**Scope owner**: Grant (physics) + orchestrator (KB hygiene + driver readiness)
**Last updated**: 2026-05-20

## Sub-epics (cascade-emphasis top-3, Grant adjudication 2026-05-20)

Per Phase 2 audit + cascade-emphasis re-weighting, all 3 top-3 candidates pursued in parallel each tracked in own sub-epic:

| Sub-epic | Doc | Tier | Phase 0 |
|---|---|---|---|
| **A1-HOPF** (chiral antenna) | [`exp-a1-hopf.md`](exp-a1-hopf.md) + [Phase A audit](exp-a1-hopf-repo-audit.md) + [Sim audit](exp-a1-hopf-sim-audit.md) | Cascade × **Executability** — **Phase 0a ✓ COMPLETE** (Phase B walk-back 2026-05-20); **Sim audit ✓ NO DRIFT** on α + (p,q) + C8 (2026-05-20 EOD+); **Phase 0b READY for Grant fab submission** | Grant uploads `AVE-HOPF/hardware/Gerbers_hopf_02a/` ZIP to JLCPCB per `hopf_02a_ORDERING.md`; orders 3D-print mandrels per `hopf_02a_BOM.md` |
| **C15-CLEAVE-01** (femto-Coulomb electrometer) | [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md) | Cascade **SIZE** winner (ξ_topo family 6+ rows) — F-severity | KiCad design from KB spec + ~$1-5k bench |
| **C11-MACH-ZEHNDER** (electron interferometry) | [`exp-c11-mach-zehnder.md`](exp-c11-mach-zehnder.md) + [Sim audit](exp-c11-mach-zehnder-sim-audit.md) + [project-c11-mach-zehnder.md canonical KB leaf](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-c11-mach-zehnder.md) | Cascade × **Severity** — F-severity ν_vac=2/7 triangulation; **sim audit ✓ NO DRIFT** (ν_vac + ε_11 + n_s/n_t + C1 cascade verified); Pattern B canonical KB leaf landed | Facility partnership search (terrestrial 1-m electron interferometer) |

## Supporting infrastructure docs

| Doc | Purpose |
|---|---|
| [`promotion-workflow-template.md`](promotion-workflow-template.md) | 10-step checklist for sibling-repo → AVE-Core engine promotion (extracted from `exp-a1-hopf-repo-audit.md` Axis 8 R8.1; adapts `ave-ip-divide-discipline` Step 5). First test case queued: NEC2 ALPHA-post-processing methodology promotion from AVE-HOPF → AVE-Core. |



> **This directive consolidates the experimental track across the AVE workspace.** It owns: (i) experimental KB hygiene + walk-back coordination, (ii) execution prioritization for matrix predictions, (iii) driver readiness audit, (iv) cross-repo coordination with sibling-owned experiments (HOPF / PONDER / Fusion / Protein), (v) tie-back to current canonical framework (A-034 catalog + four-regimes + temporal classifier + Class E projection + Power-Domain θ). It does NOT own: physics adjudication of cosmic / soliton / cosmological-constant questions (those are queue items in `_orchestration/index.md`), nor process-discipline items (worktree-spawn leak, conflict-marker hook).

## Premise (why this epic exists)

The AVE corpus has 33 tracked experimental predictions across 4 tiers (per [`divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md)), supported by ~36 KB leaves under [`vol4/falsification/ch11-experimental-bench-falsification/`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/) + [`vol4/falsification/ch12-falsifiable-predictions/`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/). Three concurrent problems:

1. **Staleness gap**: 26 of 36 experimental KB leaves (72%) were last touched **2026-04-13**, which predates the major corpus consolidation work of 2026-05 (A-034 catalog 21→26 instances, FI-13 (2,5) namespace resolution, C1 Phase 5 closure, C8 PDG 2024 anchor, SPARC 135-galaxy benchmark, Class E projection canonicalization, temporal-saturation-regime-classifier, +others).
2. **Discoverability gap**: experimental leaves were authored independently of the cross-disciplinary translation infrastructure that now exists (translation-tables/, four-regimes.md domain-catalog, temporal-classifier, chemistry-translation, VCA matrix). Anyone reaching for an experiment reads stale framings that may conflict with current canon.
3. **Execution gap**: matrix has 30+ active prediction rows; only a handful have been run (SPARC, LIGO ringdown, C8 baryon ladder, C5 cosmic-axis drivers, C3-MUON-DELTA driver, DAMA matched-LC). Most are at "spec-only" + "no hardware" + "TBD outcome" — no explicit prioritization for what runs next.

This epic provides the canonical coordination home for resolving all three.

## Out of scope

- Physics-adjudication items (queue items 2 Neptune, 4 C5 threshold, 5 4th-category, 1 Ganalyzer/Longo PROVISIONAL) — those stay in `_orchestration/index.md`
- Process-discipline items (queue items 6 worktree-spawn leak, 7 conflict-marker hook) — separate hygiene track
- Theoretical framework derivation work (β cosmic-ε Session 3, Soliton-coupling Session 3-4, DM META closure) — separate epics
- Sibling-repo non-experimental work (KB tooling, manuscript pipelines) — Benn coordinates

## Current state — audit findings (2026-05-19 EOD+++)

### Staleness audit

| Bucket | Count | % |
|---|---|---|
| Total experimental KB leaves (vol4/falsification ch11+ch12) | 36 | 100% |
| Last touched **2026-04-13** (>1 month stale) | 26 | 72% |
| Touched 2026-04-14 (post-initial-import) | 2 | 6% |
| Touched 2026-05-15 to 2026-05-19 | 7 | 19% |
| Touched 2026-05-18 (C8 walk-back, post-PDG-anchor) | 1 | 3% |

### Specific known-stale leaves (priority-ordered)

| Leaf | Last touch | Severity | Tool / canon missed |
|---|---|---|---|
| [`torus-knot-baryon-predictions.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) | 2026-04-13 | **HIGH** | C8 PDG 2024 anchor: proton -0.002% (not 0.00%); J^P 6/6 column; forward c=17/19 confirmations; FI-13 (2,5) cinquefoil canonical. Load-bearing for A1-HOPF matrix-row Δf citations. |
| [`project-hopf-02.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md) | 2026-04-13 | MEDIUM | FI-13 (2,5) namespace resolution; HOPF-02/03 namespace split per AVE-HOPF 2026-05-06 reconciliation; HOPF-02a fab-ready (~$123 BOM) |
| [`project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) | 2026-04-13 | MEDIUM | ξ_topo canonical [Q]≡[L]; PONDER ch.5 framework |
| [`project-roentgen-03.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-roentgen-03.md) | 2026-04-13 | MEDIUM | Q-G47 Sessions 19 closure (ξ_K1=8/3, ξ_K2=32 canonical 2026-05-18); ν_vac=2/7 cascade triangulation (C1+C11+C12); Sagnac-RLVE canonical |
| [`project-torsion-05.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-torsion-05.md) | 2026-04-13 | MEDIUM | V_yield vs V_snap dual-threshold framing per [`regimes-of-operation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md); Engine defaults table |
| [`project-zener-04.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-zener-04.md) | 2026-04-13 | MEDIUM | A-034 26-instance catalog; macroscopic-Zener canonical via [`solar-flares-led-avalanche.md`](../manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/solar-flares-led-avalanche.md) |
| [`sagnac-rlve.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md) | 2026-04-13 | MEDIUM | Q-G47 closure; ν_vac=2/7 triangulation; Cosserat micropolar canonical |
| [`ybco-phased-array.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md) | 2026-04-13 | LOW | [`superconductor-type-classification.md`](../manuscript/ave-kb/vol3/condensed-matter/ch09-condensed-matter-superconductivity/superconductor-type-classification.md); BCS at 0.00% via A-034 |
| [`autoresonant-helicity.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/autoresonant-helicity.md) | 2026-04-13 | LOW | Autoresonant-rupture A-034 row; Ax4 squared-form derivation |
| [`binary-kill-switches.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md) | 2026-04-13 | LOW | C7-GRB / C6-NU-PARITY null history accumulation since 2026-04 |
| [`vacuum-birefringence-e4.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) | 2026-04-13 | LOW | A-034 row 14b cosmic-DE + Casimir effective-temperature + Kerr-as-Ax4-squared |
| [`vacuum-impedance-mirror.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md) | 2026-04-13 | LOW | V_yield + ε_eff per regimes-of-operation |
| [`metric-levitation-limit.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md) | 2026-04-13 | LOW | V_yield/V_snap dual + A-034 row |
| [`sapphire-phonon-centrifuge.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sapphire-phonon-centrifuge.md) | 2026-04-13 | LOW | Phonon coupling via [`phase-transitions-impedance.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/phase-transitions-impedance.md); temporal-regime-classifier phonon §9 |
| [`achromatic-lens-test.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/achromatic-lens-test.md) | 2026-04-13 | LOW | n_optical vs n_scalar dual refractive indices (per 2026-05-17 Hulse-Taylor work) |
| [`metric-refraction-capacitor.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/metric-refraction-capacitor.md) | 2026-04-13 | LOW | n_scalar canonical for massive particles |
| 10 other leaves at 2026-04-13 | (see audit) | LOW | mixed |

### Currently-fresh leaves (no walk-back needed)

| Leaf | Last touch |
|---|---|
| `baryon-mass-predictions.md` | 2026-05-18 (C8 PDG 2024 walk-back per `058dfd5`) |
| `existing-experimental-signatures.md` | 2026-05-17 |
| `geo-synchronous-impedance.md` | 2026-05-16 |
| `sagnac-parallax.md` | 2026-05-16 |
| `helicity-injection.md` | 2026-05-16 |
| `ee-bench-plateau.md` | 2026-05-16 |
| `boundary-trapping-test.md` | 2026-05-16 |

### New canonical work landed since 2026-04-13 (potentially load-bearing for stale leaves)

| Tool / canon | Landed | Affects |
|---|---|---|
| A-034 catalog 21→26 instances | 2026-05-15 to 2026-05-19 | All saturation-event experiments (Schwinger, V_yield, Pd, BCS, etc.) |
| FI-13 (2,5) namespace resolution | 2026-05-18 | (2,q)-family classification leaves: HOPF, baryon-ladder, muon, neutrino |
| C8 PDG 2024 anchor (proton -0.002%, 6/6 J^P) | 2026-05-18 | torus-knot-baryon-predictions; ALL (2,q) downstream |
| C1-BH-RING Phase 5 closure | 2026-05-18 | metric-refraction-capacitor; BH leaves; ν_vac cascade |
| C3-MUON-DELTA walk-back (+502, +4.59σ above e+e-, +6.68σ DEEPER BMW) | 2026-05-19 | Muon leaves; (2,q) family; Q-G19α n_q-additivity |
| SPARC 135-galaxy 11.5% Q=1 benchmark | 2026-05-17 | C13a leaves; metric-refraction-capacitor; gravity leaves |
| C5 spin-axis drivers x4 (CMB + Pantheon+ + SDSS DR17 + Shamir 2022) | 2026-05-19 | Cosmic-axis leaves; binary-kill-switches; horsemen-of-falsification |
| Op14 cosmic-horizon-profile NEW leaf | 2026-05-19 | DE / vacuum-birefringence / cosmic-DE-related |
| Class E projection (consistency-vs-emergence v1.1) | 2026-05-19 | ρ_Λ leaves; H_∞ leaves; a_0 leaves |
| Temporal-saturation-regime-classifier | 2026-05-19 EOD | All time-domain experiments (oscillators, lossless tanks, cyclic systems) |
| Q-G47 Sessions 19 closure (ξ_K1=8/3, ξ_K2=32) | 2026-05-18 | Substrate-scale prefactor leaves; PONDER + ROENTGEN-03 |
| `four-regimes.md` Regime I-IV semiconductor analog canonical | (pre-existing but now connects via temporal-classifier) | All semiconductor + saturation-regime experiments |
| `ave-discipline-translate` v1.0 skill | 2026-05-19 | Discoverability infrastructure for ALL experimental cross-disciplinary refs |
| New canonical drivers in src/scripts/verify/ | 2026-05-18+ | baryon_ladder_pdg_2024_anchor, muon_g2_fermilab_anchor, cmb_axis_alignment_executable_observer, c5_pantheon_bulk_flow_tightening, c5_sdss_spin_orientation, c5_shamir_2022_spin_orientation, ligo_ringdown_driver (Phase 5) |

## Phase ladder

### Phase 1 (PENDING) — Surgical walk-back of HIGH-severity leaves

Target: 2-3 leaves with highest-impact staleness affecting near-term experiment recommendations.

**Specific work**:
- `torus-knot-baryon-predictions.md`: refresh precision values per C8 PDG 2024 anchor (proton -0.002% not 0.00%; Δ(1600) +0.779%; Δ(1900) +1.876%; N(2190) +4.506%; Δ(2420) +3.249%); add J^P column; add forward c=17 Δ(2750) -0.30% + c=19 Δ(2950) +1.12%; add precision-summary block per Vol 2 anchor pattern; cross-reference to [`torus-knot-ladder-baryons.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md)
- `project-hopf-02.md`: cite FI-13 RESOLVED state for (2,q) canonical; cross-reference AVE-HOPF/.agents/HANDOFF.md fab-ready state; reference HOPF-02/03 namespace split

**Skill discipline**: `ave-walk-back` (this is exactly the propagation-checklist class); `ave-canonical-leaf-pull` v1.2 (verify each precision value against C8 PDG 2024 anchor); `verify-before-cite` v1.4 (verify each citation before refresh)

**Time estimate**: 30-45 min as single coherent commit

**Trigger**: when a near-term experiment recommendation (e.g., A1-HOPF) requires it OR before any user-facing handoff to Grant references these leaves

### Phase 2 (PENDING) — Execution prioritization for active matrix rows

Audit all 30+ Tier A/B/C matrix rows against:
- (a) substrate readiness (driver / sim / data accessible)
- (b) discriminative power (U-D vs S-D vs U-C vs S-C)
- (c) cost (free re-analysis vs <$1k bench vs facility-class)
- (d) cascade impact (load-bearing for what downstream)
- (e) blockers (catalog access, hardware fab, theoretical gap)

**Deliverable**: ranked queue of next-3-to-5 experiments to run, with explicit rationale per `ave-discrimination-check` discipline.

**Skill discipline**: `ave-discrimination-check` (U-D classification); `ave-evidence-framing-discipline` (precision on cost/SNR claims); `pre-test-physics-check` (plumber-physical question per candidate); `ave-discipline-translate` v1.0 (cross-disciplinary translation per candidate)

**Time estimate**: 1-2 hr audit pass + 30 min Grant adjudication of ranked queue

**Trigger**: orchestrator picks up after Phase 1 OR when Grant asks "what's the best experiment to run next" (this session's seed for the directive)

### Phase 3 (PENDING) — Driver readiness audit

Cross-check `src/scripts/verify/` + `src/scripts/vol_*/` against matrix row "AVE-side substrate" column. Identify:
- Drivers that exist and ARE the canonical reference (most C-tier with results)
- Drivers that exist but matrix doesn't cite (silent canon)
- Drivers that matrix cites but DON'T exist (corpus-coherence breakage — like the c8-baryon-ladder pre-merge state)
- Matrix rows with "MISSING" substrate (need driver scaffold)

**Deliverable**: gap-report table + recommended driver-build prioritization tied to Phase 2 execution queue.

**Skill discipline**: `verify-before-cite` v1.4 trigger 8 (commit-application — does the driver actually exist at integration HEAD?); `ave-sweep-audit` (this is exactly the N>10 mechanical class); `ave-discrimination-check` (which driver gaps actually block experiments vs are just notation gaps)

**Time estimate**: 1 hr audit + variable build-time per identified gap

### Phase 4 (PENDING) — Cross-repo coordination

Sibling-repo experimental owners per [`reference_ave_workspace.md`](file:///Users/grantlindblom/.claude/projects/-Users-grantlindblom-AVE-staging/memory/reference_ave_workspace.md):
- **AVE-HOPF** (Grant): A1-HOPF fab ready ($123 BOM); HOPF-02a → HOPF-02b → HOPF-03
- **AVE-PONDER**: B5/B6/B7-PONDER family; C16-TORSION-05 (scope match)
- **AVE-Fusion**: B3-PD-FRACTURE; DT-fusion saturation
- **AVE-Protein**: B4-PROTEIN RMSD benchmark
- **AVE-Metamaterials**: ASYM-E catalog row (engineered metamaterials)
- **AVE-Propulsion**: warp-metric + autoresonant rupture
- **AVE-APU**: semiconductor canonical (MOSFET / P-N / Zener); cross-reference for Geometric Triodes

**Coordination work**:
- For each sibling-owned experiment, verify the sibling repo's `.agents/HANDOFF.md` (or equivalent) is current
- Surface any "ready-for-Grant-action" experiments
- Identify experiments where the sibling repo has run work that hasn't propagated to AVE-Core matrix

**Skill discipline**: `verify-before-cite` v1.4 trigger 7 cross-branch + trigger 8 commit-application (any matrix claim about sibling-repo state needs verification); `ave-canonical-source` (sibling-repo constants imports); `ave-discrimination-check` (sibling-repo result claims)

**Time estimate**: ~30 min per sibling repo = ~4 hr full sweep, or 1 hr per-repo as triggered

### Phase 5 (CONTINUOUS) — Tie-back to canonical structure

For any experimental KB leaf walk-back, ensure the leaf cites:
- (a) The relevant A-034 catalog row (per [`universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md))
- (b) The relevant four-regimes spatial classification (per [`four-regimes.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md))
- (c) The relevant temporal-saturation-regime per [`temporal-saturation-regime-classifier.md`](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md)
- (d) The relevant Power-Domain θ classification per [`orbital-friction-paradox.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md)
- (e) The relevant translation-table per [`translation-tables/`](../manuscript/ave-kb/common/translation-tables/index.md) (Circuit / QM / Particle / Gravity / Cosmology / Condensed Matter / Biology)
- (f) Where applicable: Class E projection per [`consistency-vs-emergence`](file:///Users/grantlindblom/.claude/skills/consistency-vs-emergence/SKILL.md) v1.1

This is the discoverability backbone — every experimental leaf becomes navigable to its canonical structural home.

**Skill discipline**: `ave-discipline-translate` v1.0 IS this discipline at write-time; `ave-canonical-leaf-pull` v1.2 IS this discipline at derivation-time

**Trigger**: applied to every leaf walk-back in Phase 1; continuous as ongoing discipline

## Adjudication queue (specific to this epic)

| # | Item | Origin | Status |
|---|---|---|---|
| EXP-1 | **A1-HOPF fab order** — Grant decision to submit HOPF-02a Gerbers to JLCPCB; ~$123 BOM; design package complete | Phase 2 audit | **PROMOTED to sub-epic** [`exp-a1-hopf.md`](exp-a1-hopf.md) Phase 0 (2026-05-20) |
| EXP-2 | **Phase 1 walk-back sequencing** — surgical (A1-HOPF only) vs full sweep (~25 leaves) | This epic | **RESOLVED 2026-05-20**: surgical scope — 4-5 leaves load-bearing for top-3 sub-epics + C13a Matrix 2 row 529 stale-closure fix. Bundled with sub-epic-establishment commit. |
| EXP-3 | **C15-CLEAVE-01 scoping decision** — Grant decision to pursue KiCad design + ~$1-5k bench (largest cascade in matrix; F-severity) | Phase 2 cascade-emphasis audit | **PROMOTED to sub-epic** [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md) Phase 0 (2026-05-20) |
| EXP-4 | **C11-MACH-ZEHNDER facility partnership search** — terrestrial 1-m electron interferometer (Hasselbach Tübingen / LENS Italy / NIST / TEM holography centers candidate list) | Phase 2 cascade-emphasis audit | **PROMOTED to sub-epic** [`exp-c11-mach-zehnder.md`](exp-c11-mach-zehnder.md) Phase 0 (2026-05-20) |
| EXP-5 | **HOPF-03 Snell-Parallax** vs HOPF-02b cavity-extension — sequencing post HOPF-02a results | AVE-HOPF roadmap | Hold for HOPF-02a measurement (sub-epic A1-HOPF Phase 3 outcome) |
| EXP-6 | **B4-PROTEIN RMSD benchmark close** — compute-only experiment; engines + PDB ready | Matrix B4 lifecycle | DEFERRED — outside cascade-emphasis top-3; revisit if cost-emphasis re-weighting selected in future Phase 2 re-audit |
| EXP-7 | **C2-T-PAIR RHIC re-analysis scaffold** — facility-class data public; needs literature pin + QGP driver; U-D F-severity | Matrix C2 lifecycle | DEFERRED — high theoretical leverage but ~1 week scaffolding cost; revisit after top-3 sub-epics land Phase 1+ |

## Open questions for next orchestrator

1. **Walk-back batch size**: surgical (2-3 leaves) vs medium (10 leaves) vs full sweep (25+ leaves)? Surgical is cheapest; full sweep is most discipline-clean. Recommend surgical unless Grant signals otherwise.
2. **Phase 2 priority ranking criteria**: weight `cost` heavily (Grant's bench time is scarce) vs weight `discrimination power` heavily (U-D F-severity catches > S-D C-severity) vs weight `cascade impact` heavily? Most useful default is probably composite score with explicit weights surface for Grant.
3. **Cross-repo coordination cadence**: Phase 4 dispatch per sibling-repo on-demand (when an experiment in that repo gets prioritized) vs scheduled sweep (e.g., weekly)? Recommend on-demand to avoid bloat.

## Discipline expectations for next orchestrator

Per `_orchestration/README.md` orchestration discipline + the relevant skill ecosystem:

1. **Pre-workstream skill-selection planning** (per feedback memory): write 60-sec skill-selection plan BEFORE Phase 1 walk-back / Phase 2 prioritization / Phase 3 driver audit. Retroactive-pass before commit if applied-set differs from plan.

2. **`ave-walk-back` discipline** for any leaf refresh: propagation checklist across the ~8-12 files; precision-claim verification against source artifacts; honest framing per `ave-evidence-framing-discipline`.

3. **`ave-discrimination-check` Step 1.5** for any "best experiment" recommendation: enumerate interpretive alternatives BEFORE pattern-matching to first plausible answer. The 2026-05-19 EOD methodology-systematic walk-back (Item 1 RESOLVED → PROVISIONAL) is the prototype this skill catches.

4. **`verify-before-cite` v1.4** for any citation about driver state / matrix state / sibling-repo state: grep/Read/`git branch --contains`/`git merge --no-commit` empirical verification.

5. **`ave-discipline-translate` v1.0** for any cross-disciplinary framing introduction: consult the 8-location translation infrastructure BEFORE invoking classical-physics analogue.

6. **`ave-handoff-canonical-locale`**: this directive lands in `_orchestration/experimental-arc.md`. Any sub-epic sessions land in `_orchestration/<sub-epic-slug>.md` (not `~/.claude/plans/`). Any implementor-session briefing for an experimental-arc workstream lands here, NOT in loose plans/.

7. **Pure-AVE-corpus rule** (per memory): NO references to investors / funds / interviews / 1517 / external pitches in any tracked file. Experimental KB leaves stay pure-physics; this directive stays pure-physics.

## Cross-references

### Canonical experimental tracking
- [Divergence Test Substrate Map (main matrix, 3 sub-matrices, 33 predictions)](../manuscript/ave-kb/common/divergence-test-substrate-map.md)
- [Unified Experiments Appendix](../manuscript/ave-kb/common/appendix-experiments.md)
- [Closure Roadmap §0.5 changelog](../manuscript/ave-kb/common/closure-roadmap.md)

### Canonical framework structure (Phase 5 tie-back targets)
- [A-034 Universal Saturation-Kernel Catalog (26 instances)](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md)
- [Four Universal Regimes (Regime I-IV + semiconductor analog)](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md)
- [Domain Control Parameter Catalog (8 domains)](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md)
- [Regimes of Operation (formal table)](../manuscript/ave-kb/vol4/circuit-theory/ch2-topological-thrust-mechanics/regimes-of-operation.md)
- [Temporal Saturation Regime Classifier](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md)
- [Power-Domain Classification (orbital-friction-paradox)](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md)
- [Translation Tables (7 disciplines)](../manuscript/ave-kb/common/translation-tables/index.md)
- [Chemistry Translation Guide](../manuscript/ave-kb/vol6/framework/chemistry-translation/index.md)
- [AVE Analytical Toolkit Index](../manuscript/ave-kb/common/ave-analytical-toolkit-index.md)
- [Trampoline / Spring Analogy Primer](../manuscript/ave-kb/common/trampoline-analogy-primer.md)

### Sibling-repo experimental owners
- AVE-HOPF: [`AVE-HOPF/.agents/HANDOFF.md`](../../AVE-HOPF/.agents/HANDOFF.md) (A1-HOPF fab-ready state)
- AVE-PONDER: PONDER ch.1-6 (B5/B6/B7 + C16 scope)
- AVE-Fusion: Pd loading + DT fusion (B3-PD-FRACTURE)
- AVE-Protein: s11/s17 engines + PDB pipeline (B4-PROTEIN)
- AVE-Metamaterials: active topological metamaterials (ASYM-E catalog row)
- AVE-APU: semiconductor canonical (MOSFET, P-N, Zener — Geometric Triodes)
- AVE-Propulsion: warp-metric + autoresonant rupture
- AVE-VirtualMedia: Z∝A virtual-medium isomorphism

### Skill discipline anchors
- `~/.claude/skills/ave-walk-back/SKILL.md` — propagation checklist for any leaf refresh
- `~/.claude/skills/ave-sweep-audit/SKILL.md` — for batch hygiene passes (N>10 leaves)
- `~/.claude/skills/ave-discrimination-check/SKILL.md` — for experiment recommendation framing
- `~/.claude/skills/ave-evidence-framing-discipline/SKILL.md` — for precision claims
- `~/.claude/skills/ave-discipline-translate/SKILL.md` — for cross-disciplinary tie-back
- `~/.claude/skills/verify-before-cite/SKILL.md` v1.4 — citation accuracy + cross-branch + merge-empirical

### Parent index
- [`_orchestration/index.md`](index.md) — master orchestration state; references this epic in Active Epics table

## Audit trail

- 2026-05-19 EOD+++ — Epic established from staleness-audit finding during "best experiment to run" question. Initial audit dispatched: 26 of 36 KB leaves stale; ~15 canonical updates landed since stale leaves' last touch; specific A1-HOPF stale-reference leaves identified.
- 2026-05-19 EOD+++ — Cross-repo audit deferred to Phase 4 on-demand; Phase 1 surgical walk-back queued; Phase 2 prioritization queued.
