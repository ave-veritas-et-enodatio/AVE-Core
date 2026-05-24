# Cosmic-Axis Glossary Epic

**Status**: ACTIVE — implementor kickoff pending (Grant adjudicated 2026-05-19 EOD: scope C, before E1b-prime, path-stable yes, naming `cosmic-axes-and-frames-glossary.md`, fold in H_∞ hygiene items)
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-E1b adjudication research sweep (4 parallel `ave-corpus-grep` agents; full synthesis in chat log + reproducible from grep targets below)

## Why this exists

E1b-prime Pantheon+ adjudication surfaced that the AVE corpus carries **two physically distinct cosmological direction concepts** that are easy to conflate at the manuscript-readership level — and the corpus glossary (`common/translation-tables/translation-cosmology.md`) currently does NOT define either explicitly:

1. **K4 lattice rest frame** — the frame in which the chiral Laves K4 Cosserat substrate $\mathcal{M}_A$ sits at rest, identified empirically with the CMB rest frame per Q-G24 (`preferred-frame-and-emergent-lorentz.md:13,29`). The CMB dipole at $(l \approx 264°, b \approx 48°)$ is the Sun's velocity vector through this rest frame; it is NOT a fundamental cosmological axis.

2. **$\hat{\Omega}_{\text{freeze}}$** — the parent-BH spin axis preserved through K4 crystallization at lattice genesis; the global cosmic chirality direction from $I4_132$ space group lock-in (`omega-freeze-cosmic-grain-cascade.md:34-40`). This direction projects into the CMB axis-of-evil, Hubble bulk-flow, LSS spin, matter-asymmetry, E/B polarization decoupling, orbital-plane alignments, CODATA G $P_2(\cos\theta)$ profile, and CMB QNM ℓ-spectrum. Empirically pinned 2026-05-19 at $(l = 60.28°, b = 50.48°)$.

The plumber-physical adjudication of E1b-prime (Pantheon+ pipeline circularity) **depends on distinguishing these two concepts cleanly** — Pantheon+ subtracts solar motion at the CMB dipole direction (concept 1), not at $\hat{\Omega}_{\text{freeze}}$ (concept 2), so the test is structurally non-circular. Without explicit corpus definitions, this distinction has to be re-derived every time it's needed.

Beyond the dipole-vs-axis-of-evil distinction, **eight cosmic-axis observables share the same $\hat{\Omega}_{\text{freeze}}$ direction by the A-034 cosmic-scale instance**, and the corpus glossary doesn't have a unified definitional resting place for them either.

## Scope options for Grant adjudication

| Option | Scope | Effort | Files touched |
|---|---|---|---|
| **A** | Add 6-8 rows to `common/translation-tables/translation-cosmology.md` only | ~30 min | 1 file |
| **B** | Option A + new canonical leaf `common/cosmic-axes-and-frames-glossary.md` with full definitions of K4 rest frame / $\hat{\Omega}_{\text{freeze}}$ / parent-BH spin / cosmic lattice genesis / eight-observable cascade | ~1.5-2 hr | 2 files (translation table extension + new leaf) |
| **C** | Option B + propagate $(174°, -5°)$ → $(60.28°, 50.48°)$ walk-back across the 5+ canonical files where the stale placeholder still appears (already queued at `closure-roadmap.md:90` as a follow-up) | ~3-4 hr | 7+ files (B + universal-saturation-kernel-catalog.md, omega-freeze-cosmic-grain-cascade.md, divergence-test-substrate-map.md, vol_3_macroscopic/chapters/04_generative_cosmology.tex, backmatter/07_universal_saturation_kernel.tex, possibly A-034 prereg annotations) |

**Recommendation**: Option B. Captures the definitional load-bearing content without bundling the walk-back propagation (which is structurally independent and should run as its own session per `ave-walk-back` skill discipline). Option C bundles too much; cleaner to leave the walk-back propagation as its own queued item.

## Resolved decisions (Grant adjudication 2026-05-19 EOD)

| # | Decision | Resolution |
|---|---|---|
| G1 | Which scope option (A / B / C)? | **C** — full propagation + hygiene fold-in |
| G2 | Run before or after E1b-prime? | **BEFORE** — clean glossary anchors the Pantheon+ result doc |
| G3 | Path-stable annotation on the new leaf? | **YES** — `<!-- path-stable: referenced from vol3, vol6 as canonical cosmic-direction definitions -->` on line 3 |
| G4 | Naming convention for the new leaf | **`common/cosmic-axes-and-frames-glossary.md`** (sibling to `boundary-observables-m-q-j.md`) |
| G5 | Fold in the 2 H_∞ framing hygiene items surfaced during scoping? | **YES** — `lattice-genesis-hubble-tension.md:24` partial reversion + `predictions.yaml:142` framing inconsistency added as Phase 4 |

## What would be defined in scope B (new leaf content)

Outline of the leaf, with grep-confirmed citations for each entry:

### Section 1 — Rest frames
- **K4 lattice rest frame** — definition; identification with CMB rest frame per Q-G24; cite `preferred-frame-and-emergent-lorentz.md:13,29`
- **Sun's velocity through K4 rest frame** — $\sim 370$ km/s toward $(l \approx 264°, b \approx 48°)$; cite `flyby-anomaly-sagnac-operator.md:34`, `preferred-frame-and-emergent-lorentz.md:13`
- **Substrate equilibrium velocity floor** — $v_{\text{substrate}} = \alpha c / (2\pi) \approx 348.18$ km/s for LSR-class systems; cite `mond-hoop-stress.md:43-56`

### Section 2 — Cosmic direction axes
- **$\hat{\Omega}_{\text{freeze}}$ (cosmic chirality direction)** — definition; mechanism (Ax 1 + Ax 4 → parent-BH spin axis lock at K4 crystallization); cite `omega-freeze-cosmic-grain-cascade.md:34-40`, `trampoline-framework.md:91-119`
- **Parent-BH spin axis $\hat{J}_{\text{parent}}$** — identification with $\hat{\Omega}_{\text{freeze}}$ at genesis; cite `04_generative_cosmology.tex:405-413`, `universal-saturation-kernel-catalog.md:101`
- **CMB axis-of-evil** — Planck PR3 SMICA dispersion-maximizer; empirical pin at $(l = 60.28°, b = 50.48°)$; cite `2026-05-19_c5-cmb-axis-executable-observer-result.md:17,89`

### Section 3 — Eight projections of $\hat{\Omega}_{\text{freeze}}$
Reference table (do not duplicate — point to `omega-freeze-cosmic-grain-cascade.md:46-58`):
1. CMB axis-of-evil
2. Hubble bulk-flow direction
3. LSS galaxy-spin axis
4. Matter-asymmetry direction
5. E/B polarization decoupling axis
6. Orbital-plane alignment direction
7. CODATA G $P_2(\cos\theta)$ angular profile direction
8. CMB QNM ℓ-spectrum imprint direction

### Section 4 — Cosmic lattice genesis
- Definition: K4 phase transition at Ax 4 saturation ($A = 1$, $S(A) = 0$) inside parent-BH frame-dragging strain field
- What gets frozen: bond over-bracing $u_0^*$, chirality direction $\hat{\Omega}_{\text{freeze}}$, $\alpha$ + $G$ + $\mathcal{J}_{\text{cosmic}}$ via magic-angle operating point
- Cite `universal-saturation-kernel-catalog.md:99-101`, `omega-freeze-cosmic-grain-cascade.md:13-16`

### Section 5 — What is NOT $\hat{\Omega}_{\text{freeze}}$ (anti-confusion clarifications)
- CMB dipole direction $\neq$ $\hat{\Omega}_{\text{freeze}}$ — angular separation ~79°
- Sun's local kinematics $\neq$ cosmological initial condition
- Hubble flow magnitude is NOT predicted by AVE; only its direction
- Lattice rest frame velocity (370 km/s) and substrate equilibrium velocity ($\alpha c / 2\pi$) are DIFFERENT scoping (instantaneous solar vs LSR-class equilibrium floor)

## What would be added to `translation-cosmology.md` in scope A/B

Proposed new rows (under the existing 8 rows):

| **Cosmology** | **AVE Equivalent** | **Relationship** |
|---|---|---|
| CMB rest frame | K4 lattice $\mathcal{M}_A$ rest frame | Identification per Q-G24 (`preferred-frame-and-emergent-lorentz.md:29`). The substrate sits at rest in the CMB frame; vacuum crystallization at recombination defines this frame. |
| CMB dipole direction $(l \approx 264°, b \approx 48°)$ | Sun's velocity vector through $\mathcal{M}_A$ rest frame | $\sim 370$ km/s relative to lattice; NOT a fundamental cosmological axis. |
| CMB axis-of-evil ($\ell=2/\ell=3$ alignment) | $\hat{\Omega}_{\text{freeze}}$ projection (low-$\ell$ multipoles) | Empirical pin $(l = 60.28°, b = 50.48°)$ from Planck PR3 SMICA 2026-05-19; cosmic chirality direction inherited from parent-BH spin at K4 lattice genesis. |
| Hubble bulk-flow direction | $\hat{\Omega}_{\text{freeze}}$ projection (residual matter drift) | Whitford+2023 Pantheon+ at $(l \approx 323°, b \approx 26°)$, $\sigma \sim 30°$. Predicted to coincide with axis-of-evil; current separation 74.6° at 1.82σ — Outcome D. |
| LSS galaxy-spin axis | $\hat{\Omega}_{\text{freeze}}$ projection (galaxy chirality) | Longo 2011 + Shamir 2020 SDSS at $(l \approx 32°, b \approx 32°)$. Predicted to coincide with axis-of-evil; separation 27.9° marginally within 1σ. |
| Parent-BH spin axis $\hat{J}_{\text{parent}}$ | $\hat{\Omega}_{\text{freeze}}$ at K4 lattice genesis | Locked in by Ax 4 saturation + Ax 1 $I4_132$ chiral space group; specific direction empirically inferred (not derived from theory per A-031). |
| Big Bang (lattice genesis) | K4 phase transition at $A=1$ saturation inside parent-BH frame-dragging strain field | Crystallization front propagates at $c$; sweeps inherited volume = our observable universe. |
| Cosmic chirality bias | $\hat{\Omega}_{\text{freeze}}$ direction (handedness lock) | Right-handed by convention; mirror-image freeze-in gives left-handed universe with identical physics. |

## Skill discipline notes

When this work runs:

- **`ave-prereg`** — Skip (this is glossary work, not derivation work).
- **`verify-before-cite`** — Required. Every file:line citation in the new leaf must be re-grepped at execution time; some references may have shifted since 2026-05-19.
- **`ave-canonical-leaf-pull`** — Required for Section 3 (eight projections) — pull the canonical 8-observable table verbatim from `omega-freeze-cosmic-grain-cascade.md:46-58`; do not paraphrase.
- **`ave-handoff-canonical-locale`** — Already satisfied; this brief lives at `_orchestration/`.
- **Pure-AVE-corpus rule** — No external context anywhere in the leaf.
- **INVARIANT-N1** — Use $\mathcal{M}_A$ for the vacuum medium throughout.
- **INVARIANT-N2** — Common-area leaf, so use script $\ell_{\text{node}}$ if needed.
- **INVARIANT-S4 / S5** — Up-link on line 1 to `[↑ Common](../index.md)`; `<!-- leaf: verbatim -->` on line 2.
- **INVARIANT-S6** — If cross-volume reference target, add path-stable annotation per G3.

## Verification at session end

Implementor must verify:

1. Every file:line citation in the new leaf resolves correctly at HEAD.
2. The `translation-cosmology.md` table additions don't conflict with rows in `app-a-translation-matrix/translation-cosmology.md` (a sibling translation table in Vol 2 appendices — check for duplication).
3. New leaf is linked from `common/index.md` (the navigation index for the common KB area).
4. No external-context language in the new content.
5. `ave-auditor` verdict before push.

## Phase plan (LOCKED — implementor kickoff input)

**Branch**: `analysis/cosmic-axis-glossary` from `analysis/integration`
**Push**: yes (at end of Phase 5)
**Merge**: NO — orchestration session merges via `--no-ff` + audit-tag pattern after review

### Phase 0 — verification (10 min)

- Verify all file:line citations in this brief resolve at HEAD (`verify-before-cite`)
- Verify no overlap with `vol2/appendices/app-a-translation-matrix/translation-cosmology.md` (the sibling translation table)
- Re-grep `(174°, -5°)` occurrences to confirm the 5+ files in §3:
  - `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:88`
  - `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:26`
  - `manuscript/backmatter/07_universal_saturation_kernel.tex:221`
  - `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:467`
  - `manuscript/ave-kb/common/divergence-test-substrate-map.md:160` (citation gap note) + `:155` (load-bearing alignment claim)
  - `research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md:40,194,238,275,494`
- Create branch `analysis/cosmic-axis-glossary` from `analysis/integration`

### Phase 1 — Translation table extension (30 min)

- Append 8 new rows to `manuscript/ave-kb/common/translation-tables/translation-cosmology.md` per the table in §"What would be added to `translation-cosmology.md` in scope A/B" above
- Live-fire verify all citations (`verify-before-cite`)
- Commit: `kb(common): expand translation-cosmology with K4-rest-frame ↔ Ω_freeze direction definitions`

### Phase 2 — Glossary leaf creation (60-90 min)

- Create `manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md` per outline in §"What would be defined in scope B"
- Line 1: `[↑ Common](../index.md)` per INVARIANT-S4
- Line 2: `<!-- leaf: verbatim -->` per INVARIANT-S5
- Line 3: `<!-- path-stable: referenced from vol3, vol6 as canonical cosmic-direction definitions -->` per INVARIANT-S6
- Use $\mathcal{M}_A$ for vacuum medium per INVARIANT-N1; script $\ell_{node}$ per INVARIANT-N2 (common-area common-volume leaf so default to script)
- Apply `ave-canonical-leaf-pull` for Section 3 — pull 8-observable table verbatim from `omega-freeze-cosmic-grain-cascade.md:46-58`, do not paraphrase
- Link from `manuscript/ave-kb/common/index.md` navigation
- Commit: `kb(common): cosmic-axes-and-frames-glossary canonical leaf — K4 rest frame, Ω_freeze, parent-BH spin, lattice genesis`

### Phase 3 — (174°, -5°) → (60.28°, 50.48°) walk-back propagation (90-120 min)

Apply `ave-walk-back` skill discipline. Per-file action:

- `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:88` — replace `(l = 174°, b = -5°)` with `(l = 60.28°, b = 50.48°)`; annotate with empirical-pin reference: `(Planck PR3 SMICA, empirical pin 2026-05-19 per ../../../research/2026-05-19_c5-cmb-axis-executable-observer-result.md:17)`
- `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:26` — same replacement + same annotation
- `manuscript/backmatter/07_universal_saturation_kernel.tex:221` — same replacement with LaTeX-formatted annotation
- `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:467` — same replacement
- `manuscript/ave-kb/common/divergence-test-substrate-map.md` — at `:160`, mark the citation gap entry RESOLVED (replace gap-flagging language with empirical-pin reference); at `:155`, leave the load-bearing alignment claim wording intact (it's framework-level, not direction-specific)
- `research/_archive/L3_electron_soliton/2026-05-15_A-034_CMB_axis_alignment_empirical_prereg.md` — archival prereg; the 5 instances at `:40,194,238,275,494` get a single header annotation at top: `> **2026-05-19 retrospective annotation:** the literature axis (174°, -5°) referenced throughout this prereg was empirically pinned at (60.28°, 50.48°) per [`2026-05-19_c5-cmb-axis-executable-observer-result.md:17`](../../2026-05-19_c5-cmb-axis-executable-observer-result.md). Original prereg text preserved verbatim per archival discipline.`
- `manuscript/ave-kb/claim-quality-closure-roadmap.md:90` — mark the queued walk-back item RESOLVED with new doc link
- Commit per `ave-walk-back` batch pattern (one commit covers the full propagation): `kb(walk-back): propagate (174°,-5°) → (60.28°,50.48°) empirical pin across 7 files`

### Phase 4 — H_∞ framing hygiene fixes (30-45 min)

Surfaced during scoping as side-effect of post-912dd88 framing-walk-back audit:

- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md:24` — the table-cell "Method" column for AVE H_∞ currently shows `"First principles"`, inconsistent with the explanatory paragraph below and the parallel LaTeX `vol_3_macroscopic/chapters/04_generative_cosmology.tex` which both carry the post-912dd88 `"Geometric consistency"` framing. Fix the table cell to match (revert what appears to be an editing oversight).
- `manuscript/predictions.yaml:142` — entry P23 carries `"a priori prediction that Hubble tension is a regime artifact"` framing. Inconsistent with the post-912dd88 walk-back applied elsewhere. Reframe as `"geometric consistency identity that lands in the Planck-SH0ES tension band"` (matching the post-912dd88 framing at `mathematical-closure.md:141` and `04_generative_cosmology.tex` objectivebox).
- Verify cascade: grep for any OTHER `"First principles"` / `"a priori"` Hubble framing in corpus that may have been missed by the 912dd88 sweep
- Commit: `kb+predictions(hygiene): apply post-912dd88 H_∞ "geometric consistency" framing to remaining 2 stale-language instances`

### Phase 5 — Audit + push (15 min)

- Run `ave-auditor` review with prompt: `audit branch analysis/cosmic-axis-glossary against analysis/integration for: (a) all citations resolve, (b) pure-AVE-corpus rule, (c) INVARIANT-N1/N2/S4/S5/S6 compliance on the new leaf, (d) walk-back completeness across the 7 files in Phase 3, (e) H_∞ framing self-consistency post-Phase 4`
- Address any verdict findings
- Push branch `analysis/cosmic-axis-glossary` to origin
- Do NOT merge — orchestration session handles merge via `--no-ff` + audit-tag `audit/2026-05-NN_cosmic-axis-glossary`
- Return implementor summary to orchestration session: branches pushed, commits per phase, audit verdict, any walk-back-detected anomalies

## Cross-references

- E1b-prime briefing that surfaced this need: [`section-e-cascade.md`](section-e-cascade.md) Phase E1b-prime
- Canonical leaves referenced: `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`, `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`, `manuscript/ave-kb/common/divergence-test-substrate-map.md`
- Walk-back queue: `manuscript/ave-kb/claim-quality-closure-roadmap.md:90`
