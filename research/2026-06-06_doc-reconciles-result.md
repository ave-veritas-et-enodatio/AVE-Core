# 2026-06-06 — Documentation reconciles (Findings 5, 6, 7)

Three mechanical doc-hygiene / relabel-not-retract reconciles from a contradiction
audit. **No new physics, no derivation. Constants/claims unchanged.** Branch
`analysis/2026-06-06-doc-reconciles` off `origin/main` (`c18cd480`). `verify-kb-metadata`
PASS + `verify-md-links` gating errors 0 after each finding.

Discipline applied: `verify-before-cite` (read each cited line before editing),
`ave-walk-back` (grep-exhaustive for #6/#7), KEEP-BOTH (relabel-not-retract for #6),
flag-don't-fix (surfaced contradictions out of scope rather than silently rewriting).

---

## Finding 6 — SU(2)-vs-K4 provenance drift (relabel-not-retract; KEEP-BOTH) — commit `953dc2b9`

The `4π` in `α⁻¹ = 4π³ + π² + π` and in the `Z₀/(4π)` radiation impedance is the
**bipartite K4 lobe-count** (2 sublattices × 2π phasor rotation per lobe = 4π
temporal-phase closure per observable Compton cycle); "SU(2)→SO(3) double-cover" /
"spinor cycle" is the **standard-physics translation reference**, NOT the substrate
mechanism. Canonical sides (DO NOT change, verified): `theorem-3-1-q-factor.md:78`,
`op21-multi-mode-mode-counting.md:131-132`, `ch8-alpha-golden-torus.md:121`,
`vol1/claim-quality.md:82`.

**Sites relabeled (9 files, 30 ins / 30 del — symmetric line-for-line relabel):**

| File | Lines | In audit list? |
|---|---|---|
| `vol3/cosmology/ch05-dark-sector/dama-matched-lc-coupling.md` | 14, 55, 78–83 (re-quoted theorem-3-1:75-79 verbatim), 96, 99, 179, 182, 232 | yes (78-83, 182) |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md` | 20, 40, 106, 107, 180, 191, 195, 205, 600 | yes (107, 180) |
| `vol3/cosmology/ch05-dark-sector/dm-mechanism-unification.md` | 74 | **ADDITIONAL** |
| `common/ave-analytical-toolkit-index.md` | 47, 60, 202 | **ADDITIONAL** |
| `vol3/claim-quality.md` | 993 (clm-5em8fx description) | **ADDITIONAL** |
| `vol4/claim-quality.md` | 1087, 1105 (clm-6t3p6x description + rationale) | **ADDITIONAL** |
| `vol3/cosmology/ch05-dark-sector/index.md` | 33 (nav summary) | **ADDITIONAL** |
| `vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md` | 56 (nav summary) | **ADDITIONAL** |
| `.index/claims.jsonl` | regenerated (clm-6t3p6x rationale) | — |

**ADDITIONAL drift sites beyond the audit's two named leaves:** `dm-mechanism-unification.md:74`,
`ave-analytical-toolkit-index.md:47/60/202`, `vol3/claim-quality.md:993`, `vol4/claim-quality.md:1087+1105`,
`vol3 ch05-dark-sector/index.md:33`, `vol4 ch1-vacuum-circuit-analysis/index.md:56`. Same drift
(SU(2)/spinor-cycle presented as the 4π mechanism); same relabel applied.

KEEP-BOTH preserved: anti-QED-import point (`parametric-coupling-kernel.md:107`
"NOT a solid-angle integration borrowed from QED"), the 4π-vs-2π teaching point (`:195`),
and the SU(2)/spinor breadcrumb retained everywhere as an explicit translation reference.
Values 4π, Z₀/(4π), ε_det=4π/N², the 0.6% DAMA match, δC/C₀=4.57% all preserved verbatim.

**Reviewed, deliberately NOT changed (not drift):**
- `finkelstein-misner-spin-half-derivation.md:95` — spin-½ canonical; explicitly disclaims
  attribution ("the Vol 4 theorem's 4π has its own derivation context… an implication, not an
  attribution claim of FM-on-unknot as the source").
- `op21-multi-mode-mode-counting.md:110` — "spinor-temporal $S^1_{4\pi}$" is a geometric
  circle-label in the canonical DO-NOT-CHANGE leaf, consistent with `:132`'s translation reference.
- `divergence-test-substrate-map.md:484,492` — dated historical audit-cycle log entries
  (changelog). Audit-trail continuity — not rewritten.
- All spin-½ / g=2 / J-boundary-winding SU(2) content across the KB (canonical; the corpus
  deliberately keeps SU(2)→SO(3) double-cover for spin-½).

---

## Finding 5 — BH-leaf stale title + strengthen-by closes (physics already decided) — commit `d6786d60`

BH confinement is a SHEAR-mode lattice phase transition (`G_shear→0`; under Symmetric
Gravity `Z=Z_0` everywhere, `Γ=0` — reflects shear waves *through the phase transition*,
not impedance mismatch), distinct from the electron's EM mismatch wall (`Γ=−1`, `Z→0`).
Canonical (DO NOT change, verified): `electron-bh-isomorphism.md:23-34`; governor
`vol3/claim-quality.md:101` (clm-ir8h78).

**Sites changed (5 files):**
- `black-holes-impedance-mismatch.md:8` — retitled "Black Holes and The Absolute Impedance
  Mismatch (Γ=−1)" → "Black Holes — Lattice Phase Transition, Not Impedance Mismatch"
  (title contradicted its own `:9` caveat + the body). De-staled the `:9` Tier-2 marker;
  added a `→ Primary` cross-ref to `electron-bh-isomorphism.md:23-34`.
- `ch04-generative-cosmology/index.md:37` — parent-index nav label synced to the new title.
- `vol3/claim-quality.md:129` — strengthen-by closed RESOLVED, pointed at the resolution locus.
- `vol1/claim-quality.md:734` — cross-leaf Z-tension strengthen-by closed RESOLVED.
- `.index/strengthen-by.jsonl` — regenerated (clm-ir8h78, clm-b9eura reverse-view text).

**verify-before-cite catch (audit off-by-one):** the audit cited `vol1/claim-quality.md:735`,
but the cross-leaf-Z-tension item is at **`:734`**. Line `:735` is a DIFFERENT item (Pauli
no-overlap derivation) — left verbatim-intact. Closed `:734`.

**FLAGGED, NOT fixed — additional BH-event-horizon-`Γ=−1` sites contradicting canonical
`Γ=0`** (out of Finding 5's decided-physics scope; the brief scoped grep-exhaustive to #6/#7,
not #5; these need physics adjudication, not a mechanical relabel):
- `common/universal-saturation-kernel-catalog.md:53` — "BH event horizon | SYM | … | R_S
  formation: Γ = −1". SYM rows should be Γ=0 per canonical; **but** row `:56` (ASYM-N ε-sector
  DE) legitimately uses Γ=−1, so this is a row-by-row physics call, not a blanket relabel.
- `vol4/falsification/ch11-experimental-bench/existing-signatures.md:34` +
  `vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md:46`
  — "At the event horizon, Γ=−1 (dielectric rupture) … hard reflective boundary". This Γ=−1
  framing **underpins the LIGO-echo falsification prediction** — load-bearing. The echo
  prediction may survive via canonical "perfect reflector for shear waves" (`electron-bh-isomorphism.md:34`),
  but the `Γ=−1` *mechanism* label conflicts with the canonical phase-transition mechanism.
  Recommend a follow-up adjudication pass.

---

## Finding 7 — `closure-roadmap.md` dead references — commit `a436e80f`

File renamed `common/closure-roadmap.md` → `claim-quality-closure-roadmap.md` (ave-kb root,
Benn 2026-05-24 `fcfc0d53`). Bare `closure-roadmap.md:NN` prose refs resolve to nothing.
Because this changelog churns line numbers every session, repointed to stable section +
unique entry-name anchors (the audit's "filename-only if content moved" option), not brittle
line numbers.

**Sites changed (2 corpus leaves):**
- `vol3/gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md:14` — two bare prose
  refs repointed: "closure-roadmap §0.5 line 74 C18-PROTOCOL-12-GEO-SYNC" → "claim-quality-closure-roadmap.md
  §0.5 C18-PROTOCOL-12-GEO-SYNC" (entry now at L79); "C7-GRB-DISPERSION per closure-roadmap.md:82"
  → "…per claim-quality-closure-roadmap.md §0.5" (content now at L109).
- `vol2/particle-physics/ch03-neutrino-sector/delta-cp-violation.md:42` — link target already
  resolved (fixed in the 2026-05-25 merge); updated stale display name "closure-roadmap" →
  "claim-quality-closure-roadmap.md" (FI-13 entry now at L145).

**verify-before-cite catch:** `trace-reversal-mechanism.md:22` (audit-mentioned) was already
fully correct — link, display name, AND the "§0 row 2" verbatim quote all match
`claim-quality-closure-roadmap.md` L32 (Tier-2 dashboard row). Left untouched.

**NOT changed (audit-trail continuity / out of corpus-leaf scope):** the roadmap's own dated
changelog self-references (`closure-roadmap.md:NN` inside historical §0.5 entries — preserved
per the file's "record of human intent" header); ~30 `research/` + `_orchestration/` historical
session docs; `.claude/hooks/SKILL_TRIGGER_DETECT.md:56` (the `ave-walk-back` trigger pattern
still matches via substring). `README.md`, `LIVING_REFERENCE.md`, `docs/glossary.md` already
use the correct name.

---

## Cross-repo deferrals (OUT OF SCOPE — separate AVE-Protein session)

AVE-Protein files reference the **dead** old path `../AVE-Core/manuscript/ave-kb/common/closure-roadmap.md`
(now at `…/claim-quality-closure-roadmap.md`). NOT edited per the brief. For a follow-up
AVE-Protein session, repoint:
- `AGENTS.md:19`
- `CLAUDE.md:87`
- `README.md:75` (+ `:88`)
- `manuscript/kb-protein/index.md:31`
- `manuscript/kb-protein/validation/20-protein-rmsd-table.md:157`
- `manuscript/kb-protein/glossary/protein-vocab-mapping.md:123, :156`

---

## Verifier status (final, branch tip)

- `make verify-kb-metadata` — **PASS** (721 files, 287 canonical entries, 327 index nodes).
- `make verify-md-links` — **gating errors: 0** (189 warn-only + 1 broken-inter are all
  pre-existing in files not touched here).
- `.index/` regenerated via `make refresh-kb-metadata`: `claims.jsonl` (Finding 6, clm-6t3p6x
  rationale) + `strengthen-by.jsonl` (Finding 5, clm-ir8h78/clm-b9eura). 0 solidity / 0 footer
  / 0 subtree-claims changes — all edits are prose-only with no derived-field impact.
