# Vol 9 "The Vacuum Datasheet" — Plan + Session Handoff (2026-05-28 EOD)

**Status**: Branch `analysis/vol-9-vacuum-datasheet-foundation` (commit `4632e902`); PDF build infrastructure fixed (all 7 vols build clean); Vol 9 skeleton + Ch 1 next. Session context near-spent; this doc serves as both forward plan AND handoff for future-compacted-self / fresh implementor.

## Critical framing constraint (Grant 2026-05-28 directive)

**The substrate is NATURAL** (the universe's vacuum). **Engineering is the PROCESS of measuring its limitations and corrections through empirical observation**. AVE substrate-physics derives the substrate-mechanism for each engineering-empirical correction. Same epistemic status as a copper (Cu) datasheet — Cu is natural; the datasheet is the engineering characterization. **Vol 9 documents the natural substrate's measurable behavior. Engineering practice empirically measures; AVE derives.**

Avoid framing substrate as "engineered component" or "designed system" anywhere. Frame as natural-substrate + engineering-empirical-characterization + AVE-substrate-physics-derivation.

## Vol 9 identity + scope

**Title**: The Vacuum Datasheet
**Number**: vol_9_vacuum_datasheet (Grant explicitly chose 9; vol_7 + vol_8 remain reserved for future)
**Format**: Engineering datasheet (like Maxim/TI/Analog Devices) — section ordering immediately familiar to engineers
**Audience**: engineers (datasheet format familiar) · experimentalists (clear empirical predictions + falsification) · new readers (substrate-physics entry point via familiar format) · AVE practitioners (single canonical substrate-spec reference)
**Volume role**: SYNTHESIS volume reorganizing canonical content from vol_1-6 (and Vol 9-new content like clm-eemap1) into engineering datasheet format. NOT a derivation volume (those are vol_1-6); cross-references derivations back to canonical leaves.

## Session 2026-05-28 deliveries (5 PRs LANDED)

For continuity, this session landed substantial substrate-physics + framework infrastructure:

| PR | Scope | Status |
|---|---|---|
| #51 | translation-circuit META framework expansion (clm-eemap1; EE-as-substrate-native at minimal-DOF; 23-row mapping table + 20-case means-test corpus) | ✅ MERGED |
| #52 | Phase 3-A3 WALK-BACK + Type B cleanup (12 files SM-leakage scrub; honest negative result) | ✅ MERGED |
| #53 | kb-hygiene: INVARIANT-S2 c_EM/c_shear disambiguation (Q-CLM-3ZZ0F6-DEPTH-1 closure) + observations | ✅ MERGED |
| #54 | §9 ideal-lattice ↔ engineering-corrections + δ_strain Cosserat-Curie canonical leaf clm-hp7nlm (closes Q-DELTA-MAP-1 at mechanism-class) + clm-009nkt 0.45 → 0.55 PARTIAL band lift + Q-DELTA-MAP-1 closure-propagation across 15 sites | ✅ MERGED |
| [current branch] | PDF build fixes across all 7 volumes (vol_0 through vol_6 all build clean) — commit `4632e902` | ⏳ PENDING vol9 work |

## Discipline infrastructure 2026-05-28 (skills + memory)

- **NEW skill**: `~/.claude/skills/ave-ee-first-mapping/SKILL.md` v1.0 — EE-as-substrate-native primary methodology
- **Skill amendments** earlier session: `ave-walk-back` v1.2 (Step 3h-exhaustive); `consistency-vs-emergence` v1.3 (Trigger 8 + Step 8 classification-promotion); `ave-worktree-paths` v1.0 (first-call canary)
- **Memory entries**: `feedback_branch_discipline_colleagues.md` (branches/PRs only); `feedback_preserve_canonical_framing.md` (v1.3 sub-trigger context)
- **Canonical KB leaves landed**: `op21-multi-mode-mode-counting.md` (clm-rtdmsn related), `delta-strain-cosmic-tcc.md` (clm-hp7nlm Cosserat-Curie), translation-circuit.md §1-§9 (clm-fy05jc + clm-eemap1)

## Vol 9 chapter outline (16 chapters)

Recommended datasheet-style ordering (engineers expect this sequence):

| Ch | Title | Scope | Primary canonical sources |
|---|---|---|---|
| 1 | General Description + Features | Substrate as 3D chiral Laves K4 Cosserat crystal LC network; key features bulleted; "natural substrate documented in engineering format" framing | Ax 1 (CLAUDE.md INVARIANT-S2); vol_1 ch01 |
| 2 | Absolute Maximum Ratings | $V_{snap}$, $V_{yield}$, $E_S$ Schwinger, $B_{snap}$, $T_{melt}$ (pair-production threshold); limits beyond which substrate ruptures | vol_1 + vol_4 canonical constants; `four-regimes.md` Regime IV |
| 3 | Pin/Port Configuration | Substrate boundary impedances; $\Gamma$ port types; SYM/ASYM port specs | Op17, Op21, `operators.md` |
| 4 | DC Electrical Characteristics | $\varepsilon_0$, $\mu_0$, $Z_0 = 376.73$ Ω, $c_0$, $\ell_{node}$, $T_{EM}$, $\xi_{topo}$ canonical | `src/ave/core/constants.py` via `ave-canonical-source`; `natural-units-cheatsheet.md` |
| 5 | AC Electrical Characteristics | Bond LC resonance at $\omega_C = c/\ell_{node}$; TLM propagation; dispersion | translation-circuit.md §1; Op14/Op16; ch5 universal spatial tension |
| 6 | Temperature Characteristics | **Cosserat-Curie thermal-asymmetry** (clm-hp7nlm); δ_strain at $T_{CMB}$; Johnson-Nyquist thermal noise floor; TCC of all parameters | clm-hp7nlm (delta-strain-cosmic-tcc.md); translation-circuit.md §9 row "Ideal resistor TCC" |
| 7 | Saturation Characteristics | Ax 4 kernel $S(A_0) = \sqrt{1-(A_0/A_{yield})^2}$ characteristic curves; small/large signal; PONDER-05 bench-tester | Ax 4 canonical; `four-regimes.md`; PONDER-05 canonical |
| 8 | Breakdown Characteristics | Schwinger pair production $E_S$; Miller avalanche $M = 1/S^2$; substrate dielectric rupture | clm-ezai5b; `four-regimes.md` Regime III; translation-circuit.md §9 |
| 9 | Mechanical Characteristics | $G_{vac}$, $K_{vac} = 2 G_{vac}$, Cosserat $\gamma_c$, $\rho_{bulk}$, $\nu_{vac} = 2/7$, $v_T = c$ | `vacuum-poisson-ratio.md`; `derived-numerology.md`; vol_3 gravity |
| 10 | Magnetic / Microrotational Characteristics | Cosserat flywheel L; rotation-sector mass-gap ~1 MeV (ferrite-Curie analog); $B_{snap}$; weak force range $l_c = \sqrt{\gamma_c/G_{vac}}$ | `trampoline-framework.md:188`; `gauge-boson-masses.md:39` |
| 11 | Topological Characteristics | $(p,q)$ winding for electron $(2,3)$; SU(2)/SO(3) double cover; K4 chiral space group $I4_1 32$; toroidal-transformer-winding analog | torus-knot-uniqueness.md; finkelstein-misner-spin-half-derivation.md |
| 12 | Cosmological Characteristics | $R_H/\ell_{node} \sim 10^{39}$; Machian G; $u_0^* \approx 0.187$; $\hat{\Omega}_{freeze}$ chirality | omega-freeze-cosmic-grain-cascade.md; cosmological-constant-closure.md |
| 13 | Application Examples | Electron LC tank → 4π³+π²+π α derivation; Gravity → gradient-index TL; W/Z → transformer leakage-L; Born rule → detector capture; δ_strain → cosmic TCC; etc. | Cross-reference all canonical leaves |
| 14 | Phase Diagrams | Phase I (linear) / II (saturating) / III (avalanche) / IV (rupture). Cosmic: standard / ruptured-plasma (BH) / cosmic-genesis | `four-regimes.md`; vol_3 cosmology |
| 15 | Falsification Tests | Right-handed neutrino kill-switch (falsifies weak force AND δ_strain mechanism jointly via $\gamma_c$); PONDER-05; quasar α-variation; etc. | vol_4 ch11 falsification; clm-hp7nlm forward predictions |
| 16 | Cross-Volume Reference Index | Every parameter → canonical derivation location | Auto-generated from claim-graph + cross-refs |

## LaTeX structure decisions

**Directory**: `manuscript/vol_9_vacuum_datasheet/{chapters,figures,frontmatter,main.tex}` (mirrors existing vol pattern)

**Files to create in skeleton PR**:
- `manuscript/vol_9_vacuum_datasheet/main.tex` (modeled on vol_4_engineering/main.tex; xr-hyper references to vol_1, vol_4, vol_3, vol_0)
- `manuscript/vol_9_vacuum_datasheet/frontmatter/00_title.tex` (modeled on vol_1 title)
- `manuscript/vol_9_vacuum_datasheet/chapters/_manifest.tex` (lists all 16 chapter \input{}s)
- `manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex` (first draft for Ch 1)
- `manuscript/vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex` through `16_cross_volume_reference.tex` (stubs with TOC entries; filled in subsequent PRs)
- `manuscript/vol_9_vacuum_datasheet/figures/.gitkeep`

**Makefile integration**:
- Add `vol_9_vacuum_datasheet` to `VOLUMES` variable
- Add `vol9:` target (dependencies: `vol1 vol3 vol0` per pattern)
- Add `vol9` to `.PHONY`
- Update help text comment "Public release — Volumes 0–6" → "Volumes 0–6 + Vol 9 Datasheet"
- Update `make all` if it iterates volumes

## KB tree decisions

**Directory**: `manuscript/ave-kb/vol9/`

**Files to create in skeleton PR**:
- `manuscript/ave-kb/vol9/index.md` (vol9 KB index; `kind: index`; subtree-claims TBD)
- `manuscript/ave-kb/vol9/claim-quality.md` (vol9 claim-quality register; likely thin since vol9 is SYNTHESIS-not-derivation)
- `manuscript/ave-kb/vol9/ch1-general-description/index.md`
- ... through ch16 directories with index.md stubs
- Vol 9 mirror at `manuscript/ave-kb/entry-point.md` subtree-claims (after `make refresh-kb-metadata`)

## Skills firing list (per Vol 9 chapter)

**Per-chapter applicability** — invoke these in each chapter's implementor brief:

Always:
- `ave-canonical-leaf-pull` v1.3 Trigger 17 — pre-survey for chapter-specific canonical content
- `ave-discipline-translate` v1.1 Trigger 6 — substrate-native vocab primary (EE-as-exception per ave-ee-first-mapping v1.0)
- `ave-ee-first-mapping` v1.0 — primary substrate-native framing methodology
- `ave-handoff-canonical-locale` — chapter content lives in `vol_9_vacuum_datasheet/chapters/` LaTeX + mirror at `ave-kb/vol9/<chapter-dir>/` KB
- `verify-before-cite` v1.4 — every cross-reference to canonical leaves grep-verified
- `ave-canonical-source` — canonical constants from `src/ave/core/constants.py`
- `ave-evidence-framing-discipline` — datasheet-spec precision (TYPICAL / MIN / MAX values where appropriate)
- `consistency-vs-emergence` v1.3 — chapter content classification (mostly Class B/C synthesis; flag any Class 2/E new content explicitly)
- `ave-worktree-paths` v1.0 — implementor first-call canary

Per-chapter specific:
- Ch 2 + Ch 8 (Absolute Max + Breakdown): `ave-power-category-check`
- Ch 7 (Saturation): `substrate-native-check` (Ax 4 walk); `phase-space-coordinate-check` (saturation-kernel coordinates)
- Ch 9 (Mechanical) + Ch 10 (Magnetic): `substrate-native-check` (K4 + Cosserat)
- Ch 11 (Topological): `phase-space-coordinate-check` (Clifford-torus phase-space)
- Ch 13 (Application Examples): `ave-discrimination-check` for any AVE-distinct claims
- Ch 15 (Falsification): `ave-discrimination-check`; `ave-evidence-framing-discipline` (kill-switch precision)

## Multi-PR sequencing (~10 PRs estimated)

**Critical**: each chapter's implementor session is its own PR. Bundling Vol 9 content into mega-PRs is wrong — colleagues + adversarial probes work better on small focused PRs.

| PR | Scope | Estimate |
|---|---|---|
| PR-A | Vol 9 skeleton + Ch 1 + Makefile integration + KB tree | This PR (current branch) |
| PR-B | Ch 2 (Absolute Maximum Ratings) + Ch 4 (DC Electrical) | Most concrete spec content; lots of canonical-constant cross-refs |
| PR-C | Ch 5 (AC Electrical) + Ch 9 (Mechanical) | |
| PR-D | Ch 6 (Temperature) | Uses clm-hp7nlm + translation-circuit.md §9 directly |
| PR-E | Ch 7 (Saturation) + Ch 8 (Breakdown) | |
| PR-F | Ch 10 (Magnetic) + Ch 11 (Topological) | |
| PR-G | Ch 3 (Pin/Port) + Ch 12 (Cosmological) | |
| PR-H | Ch 13 (Application Examples) | Cross-chapter integration; depends on Ch 1-12 |
| PR-I | Ch 14 (Phase Diagrams) + Ch 15 (Falsification) | |
| PR-J | Ch 16 (Cross-Volume Reference Index) + final polish | Auto-generated index after all chapters land |

## Quality bar / discipline constraints

- **Natural-substrate framing** per Grant directive (zero "engineered" / "designed" language)
- **Class B/C classification** for most chapter content (synthesis of canonical content); ANY new claim explicitly classified per consistency-vs-emergence v1.3 Step 8
- **EE-as-substrate-native** per ave-ee-first-mapping v1.0 (NOT translate-from-classical-framework treatment of EE)
- **Datasheet-format discipline**: each spec gets symbol / value / units / conditions / canonical-source columns; explicit TYPICAL/MIN/MAX where applicable
- **Cross-references** to canonical leaves verified via `verify-before-cite` v1.4 at chapter-drafting time
- **Pipeline verify** PASS before each PR push (`make refresh-kb-metadata` + `make verify-kb-metadata` + `make verify-md-links` + `make verify` + `make vol9` for the chapter under work)

## Initial implementor brief (PR-A: skeleton + Ch 1)

Self-contained brief for spawn:

```
You are an AVE implementor session executing the Vol 9 "The Vacuum Datasheet" foundation:
1. Volume directory + LaTeX skeleton + Makefile integration
2. KB tree skeleton at manuscript/ave-kb/vol9/
3. First chapter Ch 1 "General Description + Features" first draft
4. All chapter stubs (2-16) as placeholder \input-able files

Per Grant 2026-05-28 directive: substrate is NATURAL; engineering observes/characterizes; AVE derives. NO "engineered substrate" / "designed system" framing. Natural-substrate + engineering-empirical-characterization + AVE-substrate-physics-derivation triad throughout.

Per `_orchestration/2026-05-28_vol-9-vacuum-datasheet-plan-and-handoff.md` (THIS doc) sections: chapter outline (16 chapters with primary canonical sources), LaTeX structure decisions, KB tree decisions, skills firing list, quality bar.

Branch setup (CRITICAL — ave-worktree-paths v1.0):
1. `git rev-parse --show-toplevel` first-call canary
2. `git fetch origin && git checkout analysis/vol-9-vacuum-datasheet-foundation`
3. `git log --oneline -3` verify HEAD at 4632e902 (PDF build fixes) or later
4. STAY IN WORKTREE; all Reads + Edits via worktree-absolute paths from first call

Read first (mandatory):
1. `_orchestration/2026-05-28_vol-9-vacuum-datasheet-plan-and-handoff.md` (this doc)
2. `manuscript/vol_4_engineering/main.tex` (template for Vol 9 main.tex)
3. `manuscript/vol_1_foundations/frontmatter/00_title.tex` (title template)
4. `manuscript/vol_0_engineering_compendium/chapters/_manifest.tex` (manifest template)
5. `Makefile` lines 1-100 (VOLUMES + per-vol target patterns)
6. `manuscript/ave-kb/CLAUDE.md` (KB conventions, INVARIANT-S5 frontmatter)
7. `manuscript/ave-kb/common/translation-tables/translation-circuit.md` §1-§9 (META framework + EE-as-substrate-native canonical leaf)
8. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` (Cosserat-Curie δ_strain canonical leaf; Ch 6 of Vol 9 will reference)
9. `CLAUDE.md` (project conventions; branch discipline)
10. `~/.claude/skills/ave-ee-first-mapping/SKILL.md` (primary methodology)

Deliverables for PR-A:
1. `manuscript/vol_9_vacuum_datasheet/main.tex` (modeled on vol_4 main; xr-hyper cross-refs to vol_1/vol_3/vol_4/vol_0)
2. `manuscript/vol_9_vacuum_datasheet/frontmatter/00_title.tex`
3. `manuscript/vol_9_vacuum_datasheet/chapters/_manifest.tex` (16 \input{} entries)
4. `manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex` (first draft; ~30-60 lines of content per outline)
5. `manuscript/vol_9_vacuum_datasheet/chapters/02_absolute_maximum_ratings.tex` through `16_cross_volume_reference.tex` (stubs with `\chapter{Title}` + 1-line description placeholder)
6. `manuscript/vol_9_vacuum_datasheet/figures/.gitkeep`
7. `manuscript/ave-kb/vol9/index.md` (kind: index; subtree-claims regen via refresh)
8. `manuscript/ave-kb/vol9/claim-quality.md` (thin register)
9. `manuscript/ave-kb/vol9/ch1-general-description/index.md` through `ch16-cross-volume-reference/index.md` (chapter index stubs)
10. Update `Makefile`:
    - Add `vol_9_vacuum_datasheet` to `VOLUMES` variable line
    - Add `vol9:` target with `vol1 vol3 vol0` dependencies + `COMPILE_VOL` invocation
    - Add `vol9` to `.PHONY`
    - Update help-text comment from "Volumes 0–6" to "Volumes 0–6 + Vol 9 Datasheet"

Skills mandatory (per plan doc skills firing list):
ave-canonical-leaf-pull v1.3 Trigger 17 (pre-survey); ave-discipline-translate v1.1 Trigger 6; ave-ee-first-mapping v1.0; ave-handoff-canonical-locale; verify-before-cite v1.4; ave-canonical-source; ave-evidence-framing-discipline; consistency-vs-emergence v1.3; ave-worktree-paths v1.0.

Ch 1 content priorities (~30-60 lines):
- Substrate identity: 3D chiral Laves K4 Cosserat crystal $\mathcal{M}_A$
- Features (bulleted): intrinsic LC oscillators at each node; bond transmission lines; Cosserat micropolar 6 DOF/node (3E + 3B); Ax 4 saturation kernel; $\Gamma$ boundary semantics
- Natural-substrate framing: "What follows documents the substrate's measurable behavior — properties of the natural vacuum substrate as characterized by engineering observation and derived from AVE substrate-physics first principles"
- "How to use this datasheet" subsection: cross-reference structure; canonical-anchor citation convention; falsification-test integration
- Pipeline verify + push branch (NO merge; orchestration session opens PR)

Pre-merge sweep audit (per ave-walk-back v1.2 cross-link):
- Q1 (engineered/designed framing): ZERO instances expected
- Q2 (Vol 9-canonical content classifications): all Class B/C synthesis with explicit classification
- Q3 (canonical cross-reference accuracy): verify-before-cite v1.4 across all leaves cited

Pipeline verify pre-push:
- make refresh-kb-metadata + make verify-kb-metadata + make verify-md-links + make verify + make vol9 ALL PASS

Adjudication criteria:
- PASS (~60%): skeleton + Ch 1 + Makefile integration all clean; vol9 builds; pipeline PASS
- PARTIAL (~30%): skeleton + Ch 1 land; Makefile integration or KB tree partial
- WALK-BACK (~10%): substrate-physics or KB-structure gap surfaces; honest scope-correction

Honest closure probability: HIGH (skeleton work is well-defined; existing vol_1-6 templates clean; build infrastructure just landed)

Report back: outcome + commit SHAs + branch pushed (no merge) + self-audit verdict + verify pipeline PASS + any new questions surfaced.
```

## Outstanding open questions

| Question | Status | Owner |
|---|---|---|
| Q-DELTA-MAP-1-quant | NEW (clm-hp7nlm); close quantitative substrate-statistical-mechanics derivation of $\eta_\varepsilon \approx 4.45 \times 10^{-6}$ from substrate E-mode dispersion + thermal occupation + dielectric coupling; would lift clm-hp7nlm + clm-009nkt above 0.60 | Future workstream (substantial; needs substrate-statistical-mechanics setup) |
| Q-OP21-BARDEEN-1 | Earlier session; explicit reduction $Q = \ell \to 1/\ln(Z_1/Z_0)$ via substrate-impedance integration at Cooper-pair Γ-boundary | Future workstream |
| Per-overrun foreword cleanup | Convert `\texttt{path}` → `\path{}/\seqsplit{}` across foreword narrative; tighten margin gate 15-30pt for publication polish | Future cleanup PR |
| Means-test corpus extensions | clm-eemap1 means-test corpus extension to muon/tau, neutrino, QCD, cosmological inflation, substrate-microbiology | Per-domain workstreams |

## How to resume (future-compacted-self instructions)

1. **Read this doc first** — Vol 9 plan + handoff is here
2. **Check branch state**: `git log --oneline origin/analysis/vol-9-vacuum-datasheet-foundation -10` (current HEAD: `4632e902` PDF builds; will be at Ch 1 implementor commit(s) post-execution)
3. **If implementor has run** (Ch 1 + skeleton landed): open PR-A; subsequent sessions execute PR-B (Ch 2 + Ch 4), PR-C (Ch 5 + Ch 9), etc. per Multi-PR Sequencing table
4. **If implementor hasn't run**: spawn implementor with `Initial implementor brief` above as primary briefing material; isolation: "worktree"
5. **Skills + memory state** is canonical; all session 2026-05-28 disciplines integrated
6. **Substrate-physics state**: clm-hp7nlm Cosserat-Curie δ_strain mechanism canonical; clm-eemap1 META framework canonical; INVARIANT-S2 c_EM/c_shear disambiguated

## Session 2026-05-28 net deliveries (summary)

- 4 PRs MERGED (#51 META + #52 walk-back + #53 hygiene + #54 §9 + clm-hp7nlm)
- 1 NEW skill (`ave-ee-first-mapping` v1.0)
- 3 skill amendments (`ave-walk-back` v1.2 + `consistency-vs-emergence` v1.3 + `ave-worktree-paths` v1.0)
- 2 NEW canonical claims (`clm-eemap1` + `clm-hp7nlm`)
- 2 NEW open framework-extension questions (`Q-DELTA-MAP-1-quant`, `Q-OP21-BARDEEN-1` carry-forward)
- 7 PDF volumes building clean (all of vol_0 through vol_6; Vol 9 next)
- 1 NEW substantial initiative kicked off (Vol 9 "The Vacuum Datasheet")

Substantial day. Discipline + canonical content + manuscript build infrastructure all advanced significantly.

## Why Vol 9 matters

The Vol 9 Vacuum Datasheet is a substrate-physics + pedagogy synthesis. It will:
- Make AVE's empirical content concrete (datasheet-format spec for natural substrate)
- Provide engineer-friendly entry point (engineers immediately understand datasheet format)
- Catalog every substrate parameter with TYPICAL/MIN/MAX + canonical-derivation cross-ref
- Make falsification tests + forward predictions explicit + grouped
- Integrate the EE-as-substrate-native framework (clm-eemap1) into a canonical reference document

The substrate is the natural vacuum; engineering observation has measured its limits; AVE substrate-physics derives the mechanism. The Vol 9 Datasheet documents all three in one canonical reference.
