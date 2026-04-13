# Phase 4 Burn-Down List — Iteration 1

**Synthesized:** 2026-04-03  
**Sources:** `structure_review_iter1.md` (structure reviewer), `accuracy_review_iter1.md` (accuracy reviewer)  
**Total findings processed:** 12 (5 critical, 5 warnings, 4 notes) before retraction/consolidation  

---

## Retractions

### R-1: FINDING-005 scope correction (accuracy reviewer under-counts affected files)

The accuracy reviewer states "39 instances in vol3/cosmology." Direct inspection of the KB shows 31 instances in `vol3/cosmology/` and 8 additional instances in `vol4/future-geometries/ch13-future-geometries/` — 39 total across two volumes. The accuracy reviewer's vol3-only scope statement is incorrect. **Correct scope: vol3/cosmology/ (31 instances) + vol4/future-geometries/ch13-future-geometries/ (8 instances) = 39 files/instances across two volume trees.** Fix guidance in W-3 below reflects the corrected scope.

### R-2: WARNING-2 and WARNING-3 are partially resolved — partial retraction of WARNING-2 severity claim

The structure reviewer flags that `vol8/NOTES.md` and `vol8/appendix/index.md` appear only in a Contents bullet list, not in the Derivations and Detail table. Direct inspection of `vol8/index.md` shows the Derivations and Detail table contains exactly 4 domain rows (Foundations, Saturation and Pruning, Architecture Analysis, Activation Geometry). The Contents section bullet list includes Appendix and NOTES.md as supplemental entries. This is a genuine violation for the appendix (a child directory missing from the table — WARNING-3 confirmed). For NOTES.md, the structure reviewer's characterization is mostly accurate, but the severity is reduced: NOTES.md is already accessible via the Contents bullet, and its content is non-navigational metadata rather than derivation content. The WARNING-2 classification is retained but the fix guidance is adjusted to require a table row, not a `## Derivations and Detail` entry (see W-4).

---

## FINDING-001 Special Assessment: Chapter Summary / Exercises Sections

**Verdict: (b) — Intentional distillation scope decision, not a leaf fidelity gap. Finding retracted.**

**Evidence:**

1. **Vol1 and vol2 sources do not use `\begin{summarybox}` or `\begin{exercisebox}` environments.** They use plain `\section*{Chapter Summary}` followed by `\begin{itemize}` and `\section*{Exercises}` followed by `\begin{enumerate}`. Vol3 macroscopic and vol5–vol8 sources have zero instances of these environments (grep confirms 0 each). Only vol4 (38 instances in `begin{summarybox}/begin{exercisebox}`) and vol3 cosmology (30 instances in same) and vol7 (2 instances) contain the tcolorbox environments.

2. **The distiller explicitly documented this as an intentional decision.** Five vol3 chapter indexes carry: `NOTE: summarybox and exercisebox environments are not extracted as leaves.` This note appears in `vol3/cosmology/ch04-generative-cosmology/index.md`, `ch05-dark-sector/index.md`, `ch06-solar-system/index.md`, `ch14-orbital-mechanics/index.md`, and `ch15-black-hole-orbitals/index.md`. This is not an omission — the distiller actively flagged the decision at the chapter level.

3. **Vol7 is the single exception where summarybox/exercisebox were extracted.** `vol7/condensed-matter/ch4-phase-transitions/s03-melting-eigenmode.md` contains `**[Summarybox]**` and `**[Exercisebox]**` correctly rendered. This confirms that when the distiller chose to extract these environments, they rendered correctly.

4. **Vol4 source uses `\begin{summarybox}` in 19 chapters; the KB leaves do not contain them.** This is consistent with the same intentional scope decision applied across vol3 and vol4.

**Assessment:** The KB scope explicitly excludes summarybox/exercisebox section endings from most chapters as an intentional distillation decision. The accuracy reviewer's finding appears to have been made without checking the vol3 chapter index notes that document this decision. FINDING-001 is retracted.

**Structural note recorded as N-3 below:** The distiller's scope-exclusion notes (`NOTE: summarybox and exercisebox environments...`) appear in only 5 vol3 chapter indexes. Vol4 has 19 chapters with these environments and no corresponding notes in their indexes. For maintainability, vol4 chapter indexes should carry the same NOTE annotation where summarybox/exercisebox exist in source but were not extracted. This is a Note-level item.

---

## Critical Fixes

### C-1: Protein translation pointer leaves route agents to nonexistent path

**Files:**
- `ave-kb/vol2/appendices/app-a-translation-matrix/translation-protein.md`
- `ave-kb/vol2/appendices/app-a-translation-matrix/translation-protein-solver.md`
- `ave-kb/vol2/appendices/app-a-translation-matrix/index.md`

**Fix:**  
In `translation-protein.md`: change the canonical location claim from `` `ave-kb/common/` `` to `` `ave-kb/vol5/common/` `` and update the `→ Primary:` pointer to a working relative path: `../../../vol5/common/translation-protein.md`.  
In `translation-protein-solver.md`: same change — update canonical location to `` `ave-kb/vol5/common/` `` and `→ Primary:` pointer to `../../../vol5/common/translation-protein-solver.md`.  
In `index.md` Translation Tables table: change both "Canonical Location" column cells for the Protein Folding and Protein Solver rows from `` `ave-kb/common/` `` to `` `ave-kb/vol5/common/` ``.

**Evidence:** `ave-kb/common/` contains no protein files. The actual files `translation-protein.md` and `translation-protein-solver.md` exist at `ave-kb/vol5/common/`.

**Source:** CRITICAL-1 (structure reviewer) + FINDING-004 (accuracy reviewer) — converging finding. Accuracy reviewer provides the correct relative path format.

---

### C-2: vol4/index.md has no Key Results section

**Files:**
- `ave-kb/vol4/index.md`

**Fix:**  
Insert a `## Key Results` section between the volume description paragraph and the `## Domains` table. Populate it with one key result per domain drawn from the domain summaries already present in the Domains table. Minimum acceptable content:

| Result | Location |
|---|---|
| Topo-kinematic identity: $\xi_{topo} \equiv e/\ell_{node}$ bridges spatial mechanics and circuit theory | [Circuit Theory](circuit-theory/index.md) |
| HOPF-01 chiral antenna: $\Delta f/f = \alpha \cdot pq/(p+q)$, zero free parameters | [Hardware Programs](hardware-programs/index.md) |
| Dielectric yield limit: $V_{yield} = 43.65\,\text{kV}$ ($= \sqrt{\alpha} \cdot V_{node}$) | [Falsification](falsification/index.md) |
| K4-TLM Diamond lattice simulator: $S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$, unitary to machine epsilon | [Future Geometries](future-geometries/index.md) |

The distiller may refine the exact result statements, but the section must exist and contain at minimum one row per domain.

**Source:** CRITICAL-2 (structure reviewer).

---

### C-3: vol2/appendices/app-c-derivations/index.md missing leaf marker

**Files:**
- `ave-kb/vol2/appendices/app-c-derivations/index.md`

**Fix:**  
Replace line 2 (`<!-- Anomaly A10: App C has no \label in source; content exists as itemised lists but no labelled entry points -->`) with the leaf marker:
```
<!-- leaf: verbatim -->
```
The Anomaly A10 note may be retained on line 3 or later if it provides distiller context, but line 2 must be the machine-checkable leaf marker. The file is a terminal node with verbatim content and no children; it must carry the leaf marker per INVARIANT-S5.

**Source:** CRITICAL-3 (structure reviewer).

---

### C-4: vol8/ch1 opening section and Hardware/Software Isomorphism Inversion subsection absent from all leaves

**Files:**
- `ave-kb/vol8/foundations/ch1-llm-topology/` — no leaf covers the opening section

**Fix:**  
Create a new leaf `ave-kb/vol8/foundations/ch1-llm-topology/llm-topology-intro.md` containing:
- Line 1: `[↑ Ch.1 LLM Topology](index.md)`
- Line 2: `<!-- leaf: verbatim -->`
- Verbatim Markdown translation of:
  - `\section{Applied Vacuum Engineering in Language Models}` (opening paragraph, source lines 3–6 of `01_llm_topology.tex`)
  - `\subsection{The Hardware/Software Isomorphism Inversion}` (source lines 8–17), including the saturation operator equation $S(r) = \sqrt{1 - (A/A_c)^2}$ and the $Z \propto A$ vs $Z \propto 1/A$ inversion analysis

Then update `ave-kb/vol8/foundations/ch1-llm-topology/index.md`:
- Add a row to the Derivations and Detail table: `| [LLM Topology Introduction](llm-topology-intro.md) | Chapter opening; $Z \propto A$ vs $Z \propto 1/A$ inversion; saturation operator $S(r)$ |`
- Add the result `$Z \propto A$ (virtual) vs $Z \propto 1/A$ (biological): hardware/software isomorphism inversion` to the Key Results table, linking to `llm-topology-intro.md`
- Add a bullet to the Contents section

Note: The $Z \propto A$ inversion is already in the vol8/index.md Key Results pointing to `foundations/ch2-hw-sw-inversion/inversion-split.md`. The ch1 intro subsection covers the same concept at its first introduction — both the ch1 intro leaf and the ch2 leaf should exist. Do not remove the ch2 entry.

**Source:** FINDING-003 (accuracy reviewer). Also intersects INVARIANT-C4 in CLAUDE.md (Z-proportionality regimes). The vol8 NOTES.md explicitly documents the $Z \propto A$ inversion scope — this leaf's creation resolves that note's pending status.

---

### C-5: mond-hoop-stress.md missing "Dark Sector Comparison" table

**Files:**
- `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md`

**Fix:**  
Append the "Dark Sector Comparison: AVE vs. Observation" table to `mond-hoop-stress.md` before the closing `---`. The table must be a verbatim Markdown translation of source lines 240–254 of `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex`. Rendered form:

```markdown
### Dark Sector Comparison: AVE vs. Observation

| Observable | AVE Prediction | Observed | Error |
|---|---|---|---|
| $H_\infty$ | 69.32 km/s/Mpc | 69.8 (TRGB) | $-0.7\%$ |
| $a_0$ (MOND) | $1.07 \times 10^{-10}$ m/s$^2$ | $1.2 \times 10^{-10}$ | $-10.7\%$ |
| Dark Matter | Metric drag ($\eta_{eff} \neq 0$) | Rotation curves | Mechanism |
| Dark Energy | Lattice genesis latent heat | $\Lambda$CDM $\Omega_\Lambda$ | Mechanism |
```

The `\subsection*{Dark Sector Comparison}` heading in the source is unnumbered (`\subsection*`); render as `###` in Markdown. Preserve the exact four rows and three data columns as they appear in the source tabular environment.

**Source:** FINDING-002 (accuracy reviewer).

---

## Warning Fixes

### W-1: Three PATH-STABLE annotations missing source volume specifier

**Files:**
- `ave-kb/vol4/falsification/ch11-experimental-bench-falsification/achromatic-lens-test.md` line 3
- `ave-kb/vol4/falsification/ch11-experimental-bench-falsification/boundary-trapping-test.md` line 3
- `ave-kb/vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md` line 3

**Fix:**  
Replace the annotation on line 3 of each file:

| Current | Correct |
|---|---|
| `<!-- path-stable: referenced as sec:achromatic_lens -->` | `<!-- path-stable: referenced from vol3 as sec:achromatic_lens -->` |
| `<!-- path-stable: referenced as sec:boundary_trapping -->` | `<!-- path-stable: referenced from vol3 as sec:boundary_trapping -->` |
| `<!-- path-stable: referenced as sec:induced_vacuum_impedance_mirror -->` | `<!-- path-stable: referenced from vol3 as sec:induced_vacuum_impedance_mirror -->` |

The referencing volume is vol3 (confirmed by structure reviewer).

**Source:** WARNING-1 (structure reviewer).

---

### W-2: vol8/appendix subtree absent from Derivations and Detail table

**Files:**
- `ave-kb/vol8/index.md`

**Fix:**  
Add a row to the `## Derivations and Detail` table in `vol8/index.md`:

```markdown
| [Appendix](appendix/index.md) | Pointer to unified experiments appendix (`common/appendix-experiments.md`); Vol 8 contributes no experiments |
```

The current Contents bullet (`- [Appendix](appendix/index.md)`) is supplemental and does not substitute for a table row. Table-driven traversal is the canonical descent path per KB invariant.

**Source:** WARNING-3 (structure reviewer).

---

### W-3: `**[Result]**` must be `**[Resultbox]**` — 39 instances across vol3 and vol4

**Files (confirmed scope):**
- `ave-kb/vol3/cosmology/` — 31 instances across ~10 leaf files (subdirectories: `ch04-generative-cosmology/`, `ch05-dark-sector/`, and others in cosmology)
- `ave-kb/vol4/future-geometries/ch13-future-geometries/` — 8 instances across 4 leaf files (`k4-tlm-simulator.md`, `high-q-chiral-antenna.md`, `cem-methods-survey.md`, and others)

**Fix:**  
Global replace `**[Result]**` → `**[Resultbox]**` in all leaf files in both trees. The source LaTeX in both volumes uses `\begin{resultbox}`, which per INVARIANT-S1 must render as `**[Resultbox]**`. Do not change `**[Resultbox]**` occurrences that are already correct.

Shell-level fix: `find ave-kb/vol3/cosmology ave-kb/vol4/future-geometries -name "*.md" -exec sed -i '' 's/\*\*\[Result\]\*\*/\*\*[Resultbox]\*\*/g' {} +`

**Source:** FINDING-005 (accuracy reviewer) — scope corrected per R-1 retraction above.

---

### W-4: vol8/NOTES.md missing from Derivations and Detail table and uses undocumented marker

**Files:**
- `ave-kb/vol8/index.md`
- `ave-kb/vol8/NOTES.md` line 2

**Fix (two-part):**

Part 1 — `vol8/index.md`: Add a row to the `## Derivations and Detail` table:

```markdown
| [Vol 8 Notation Notes](NOTES.md) | Raw-form notation policy; $Z \propto A$ inversion scope; pending-result conventions |
```

Part 2 — `vol8/NOTES.md` line 2: Replace `<!-- notes: vol8-local -->` with `<!-- leaf: verbatim -->`. NOTES.md is a terminal document containing content (not an index), has no children, and must carry the INVARIANT-S5 leaf marker. The `<!-- notes: vol8-local -->` marker is not defined in CLAUDE.md and has no machine-checkable semantics. The vol8-local content type is adequately communicated by the document title and the table row description.

**Source:** WARNING-2 (structure reviewer).

---

### W-5: vol3 "See also" references use bare LaTeX labels without navigable paths

**Files (sample — exhaustive scan may find additional instances):**
- `ave-kb/vol3/condensed-matter/ch11-thermodynamics/transmon-decoherence.md`
- `ave-kb/vol3/condensed-matter/ch11-thermodynamics/baryon-asymmetry-derivation.md`
- `ave-kb/vol3/applied-physics/ch07-stellar-interiors/stellar-regime-classification.md`
- `ave-kb/vol3/condensed-matter/ch11-thermodynamics/index.md`

**Fix:**  
For each bare label `> ↗ See also: \`ch:quantum_computing\`` and similar:
- If the target document can be resolved to an existing KB path, replace the bare label with a functional relative hyperlink using the INVARIANT-F2 format.
- If the target cannot be resolved (document does not exist or chapter is not yet distilled), remove the `See also` line entirely. An unresolvable bare label is worse than no cross-reference — it consumes agent context without providing navigation.

Do not leave bare backtick labels in any `> ↗ See also:` annotation. Known labels and their status:
- `ch:quantum_computing` — Vol 4 Advanced Applications; check `vol4/advanced-applications/` for a quantum computing leaf before adding link
- `ch:regime_map` — likely `vol1/dynamics/ch7-regime-map/`; verify path exists
- `ch:fundamental_axioms` — likely `vol1/axioms-and-lattice/ch1-fundamental-axioms/index.md`; verify
- `ch:baryons` — likely `vol2/nuclear-field/` or `vol3/gravity/`; verify

Run a full scan for bare-label See-also annotations: `grep -rn "↗ See also.*\`ch:" ave-kb/` to find all instances before fixing.

**Source:** WARNING-4 (structure reviewer).

---

### W-6: vol1/ch1 index Key Results formula uses wrong delimiter

**Files:**
- `ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/index.md`

**Fix:**  
In the Key Results table, locate the Macroscopic Hardware Action formula entry and replace `\|...\|` (LaTeX double-pipe norm delimiter) with `|...|` (single-pipe absolute value). The source uses single-pipe. The exact replacement depends on the rendered formula — fix the specific `\|` occurrences in that table row only.

**Source:** FINDING-006 (accuracy reviewer).

---

### W-7: App A translation matrix index missing Key Results section

**Files:**
- `ave-kb/vol2/appendices/app-a-translation-matrix/index.md`

**Fix:**  
Insert a `## Key Results` section before `## Parameter Accounting`. Minimum acceptable content: one row summarizing what the translation matrix appendix concludes (e.g., that six domain translation tables establish the zero-parameter closure of the AVE framework). The Key Results section must exist at every subtopic index per structural invariant.

Example row:
```markdown
| Result | Statement |
|---|---|
| Parameter accounting closure | Six translation tables (circuit, QM, particle physics, gravity, cosmology, condensed matter, biology) + parameter accounting establish zero-parameter geometric closure from three calibration inputs |
```

**Source:** WARNING-5 (structure reviewer).

---

## Note Fixes (low priority)

### N-1: vol8/appendix/unified-experiments-ref.md uses non-standard leaf marker

**Files:**
- `ave-kb/vol8/appendix/unified-experiments-ref.md` line 2

**Fix:**  
Replace `<!-- leaf: cross-ref -->` with `<!-- leaf: verbatim -->`. All leaf documents use `<!-- leaf: verbatim -->` per INVARIANT-S5. The `cross-ref` variant is not defined in CLAUDE.md and breaks machine-checkable leaf detection.

**Source:** NOTE-1 (structure reviewer).

---

### N-2: common/ PATH-STABLE annotations use inconsistent format

**Files:**
- `ave-kb/common/appendix-experiments.md` line 3
- `ave-kb/common/full-derivation-chain.md` line 3
- `ave-kb/common/mathematical-closure.md` line 3
- `ave-kb/common/solver-toolchain.md` line 3
- `ave-kb/common/appendices-overview.md` line 3

**Fix:**  
These carry `<!-- path-stable: label app:X -->`. Normalize to the full format `<!-- path-stable: referenced from {vol} as app:X -->`, inserting the referencing volume for each. If the referencing volume cannot be determined without source inspection, leave current format as-is and defer to a future pass with source access. Do not invent volume attributions.

**Source:** NOTE-2 (structure reviewer).

---

### N-3: Vol4 chapter indexes missing distiller scope notes for summarybox/exercisebox exclusion

**Files:**  
All vol4 chapter indexes where source chapter contains `\begin{summarybox}` or `\begin{exercisebox}` but no KB leaf captures that content. Affected indexes include at minimum:
- `ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md`
- `ave-kb/vol4/falsification/ch11-experimental-bench-falsification/index.md`
- `ave-kb/vol4/future-geometries/ch13-future-geometries/index.md`
- And approximately 16 others matching the 19 vol4 source chapters with these environments.

**Fix:**  
Add a trailing note line to each affected chapter index (after the final `---`):
```
NOTE: summarybox and exercisebox environments in source are not extracted as leaves.
```
This matches the pattern already established in vol3 chapter indexes and makes the scope decision machine-discoverable consistently across volumes.

**Source:** Derived from FINDING-001 assessment above (not from either reviewer directly — synthesizer finding).

---

### N-4: CLAUDE.md PATH-STABLE placement rule is ambiguous for index documents

**Files:**
- `ave-kb/CLAUDE.md`

**Fix:**  
In INVARIANT-S5 or a new INVARIANT-S6, add a clarification distinguishing PATH-STABLE line placement:
- Leaf documents (line 1 = uplink, line 2 = `<!-- leaf: verbatim -->`): PATH-STABLE annotation goes on **line 3**
- Index documents (line 1 = uplink, line 2 = blank or `#` heading): PATH-STABLE annotation goes on **line 2**

This two-case rule is currently implied but not stated. The existing example at `vol2/quantum-orbitals/ch07-quantum-mechanics/index.md` uses line 2 correctly, but the ambiguity in CLAUDE.md means future distillers may place it on line 3 for indexes (which would create a blank line 2, inconsistent with other indexes).

**Source:** NOTE-3 (structure reviewer).

---

## Fix Wave Plan

All fixes are single-file or tightly-scoped multi-file operations. Groupings below maximize parallelism by ensuring no two concurrent agents touch the same file.

### Batch 1 (parallel — all independent, no shared files)

All critical and warning fixes that touch distinct files can be dispatched simultaneously:

- **C-1** — three files in `vol2/appendices/app-a-translation-matrix/` (single agent covers all three)
- **C-2** — `vol4/index.md` only
- **C-3** — `vol2/appendices/app-c-derivations/index.md` only
- **C-5** — `vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` only
- **W-1** — three files in `vol4/falsification/ch11-experimental-bench-falsification/` (single agent covers all three)
- **W-3** — multi-file replace across `vol3/cosmology/` and `vol4/future-geometries/ch13-future-geometries/` (single agent, global sed or per-file replace; no file overlap with other batch 1 tasks)
- **W-6** — `vol1/axioms-and-lattice/ch1-fundamental-axioms/index.md` only
- **W-7** — `vol2/appendices/app-a-translation-matrix/index.md` only (note: C-1 also touches this file's table — **assign to the same agent as C-1** to avoid conflict)

**Revised Batch 1 grouping:**
- Agent A: C-1 + W-7 (both touch `vol2/appendices/app-a-translation-matrix/` files)
- Agent B: C-2 (vol4/index.md)
- Agent C: C-3 (vol2/appendices/app-c-derivations/index.md)
- Agent D: C-5 (vol1 mond-hoop-stress.md)
- Agent E: W-1 (three vol4 falsification leaves)
- Agent F: W-3 (vol3/cosmology + vol4/future-geometries `**[Result]**` → `**[Resultbox]**`)
- Agent G: W-6 (vol1/ch1 index)

### Batch 2 (after Batch 1 — depends on new file from C-4 and table edits to vol8/index.md)

- **C-4** — create new file `vol8/foundations/ch1-llm-topology/llm-topology-intro.md` + edit `vol8/foundations/ch1-llm-topology/index.md` (single agent; no Batch 1 agent touches vol8 foundations ch1)
- **W-2** — `vol8/index.md` Derivations and Detail table addition
- **W-4** — `vol8/index.md` (table row) + `vol8/NOTES.md` (line 2 marker)

**Note:** W-2 and W-4 both touch `vol8/index.md` — assign to same agent in Batch 2.

- Agent H: C-4 (new leaf + ch1 index edit)
- Agent I: W-2 + W-4 (vol8/index.md two table additions + vol8/NOTES.md marker fix)

### Batch 3 (after Batch 1 — independent of Batch 2, can run in parallel with Batch 2)

- **W-5** — scan for bare-label See-also annotations across `vol3/`, then edit affected leaves. Requires a grep pass first. Single agent handles grep + edits.
- **N-1** — `vol8/appendix/unified-experiments-ref.md` line 2 (no vol8 conflict with Batch 2 since different file from NOTES.md and index.md)
- **N-2** — five `common/` files (no conflict with anything)
- **N-3** — ~19 vol4 chapter indexes (no conflict with Batch 1 vol4 agents since those touch falsification leaves and index.md only; verify no overlap with Agent B's vol4/index.md)

### Batch 4 (after all above — requires CLAUDE.md edit)

- **N-4** — `ave-kb/CLAUDE.md` edit. Deferred last because CLAUDE.md is loaded into every agent context; editing it mid-wave could create version skew if other agents are still running.
  - Agent J: N-4 (CLAUDE.md only)

---

## Summary Table

| ID | Priority | Files | Batch | Agent |
|---|---|---|---|---|
| C-1 | Critical | 3 files, vol2/appendices/app-a | 1 | A |
| C-2 | Critical | vol4/index.md | 1 | B |
| C-3 | Critical | vol2/app-c/index.md | 1 | C |
| C-4 | Critical | new file + vol8/ch1/index.md | 2 | H |
| C-5 | Critical | vol1/ch4/mond-hoop-stress.md | 1 | D |
| W-1 | Warning | 3 files, vol4/falsification | 1 | E |
| W-2 | Warning | vol8/index.md | 2 | I |
| W-3 | Warning | ~39 instances, vol3+vol4 | 1 | F |
| W-4 | Warning | vol8/index.md + NOTES.md | 2 | I |
| W-5 | Warning | vol3 See-also leaves (scan first) | 3 | — |
| W-6 | Warning | vol1/ch1/index.md | 1 | G |
| W-7 | Warning | vol2/app-a/index.md | 1 | A |
| N-1 | Note | vol8/appendix/unified-experiments-ref.md | 3 | — |
| N-2 | Note | 5 common/ files | 3 | — |
| N-3 | Note | ~19 vol4 chapter indexes | 3 | — |
| N-4 | Note | ave-kb/CLAUDE.md | 4 | J |
