# Census — the pre-bond rename (R9), costed at `d129e7ac`

### ENTRY 2026-08-06-prebond-rename-census

**Class:** doc-lane vocabulary census. Mints no `clm-`/`def-`, moves no solidity, adjudicates
no fork. **Census-at-SHA:** every number below is measured at `origin/main` = `d129e7ac`, before
any edit in this PR.

**Authority:** R9 (`2026-08-06-rulings-go-prebond-hawking.md`:7–17) — GO, upgrading the
decision-batch R8 lean. Rename `"pre-geodesic plasma"` → **pre-bond state**, gloss *pre-geodesic*;
history split **de-bonded** (BH interior — bonded once, released) vs **pre-bond** (primordial
pre-freeze — never bonded). Fence, verbatim from R9: *"the rename is a VOCABULARY change only; no
site may gain or lose a physics claim in the same edit (any site whose sentence stops being true
under the new word is a finding to surface, not fix)"*.

---

## 1. The universe, stated before the count

Query: case-**insensitive** `pre-geodesic`, all tracked files, no extension filter. Stated because
a census is not a well-formed quantity until its universe is (the same discipline the signed-Γ
instrument enforces).

**The count is 51 lines across 30 files** at `d129e7ac`, re-derived 2026-08-06 (Tier-2 fix pass),
six ways: `git grep -in <SHA>`, a loose `git grep -inE "pre.?geodesic"`, the extension-filtered
`grep -rin` this record originally specified, an unfiltered `grep -rin`, `rg -in`, and a
`find | xargs grep -in` including binaries. All six return 51/30.

> **🔴 CORRECTION, 2026-08-06 — the first version of this section certified 52/31 under the
> headline *"Two methods, and they agree exactly … symmetric difference empty"*, and that was
> FALSE. The number is corrected above; the failure is recorded here rather than quietly
> overwritten, because it is a failure of the census-at-SHA discipline this very record exists to
> demonstrate.**
>
> **What went wrong, exactly.** Both methods were run against the **working tree** at the moment of
> writing — branch tip `813fd244` — not against the **pinned SHA**. That tree already carried
> `manuscript/ave-kb/common/axiom-register.md`:159, the Axiom-1 vocabulary rider **this PR itself
> authored** in commit `42ea6922`, which contains the phrase in a quotation. Re-measured to close
> the loop: `git grep -in "pre-geodesic" 813fd244` returns **52 lines / 31 files**; the same query
> at `d129e7ac` returns **51 / 30**; the delta is that one line in that one file. So 51 + 1 = 52
> and 30 + 1 = 31 — the over-count was this lane counting its own edit as pre-existing corpus.
>
> **Why two methods did not catch it.** They were not independent in the dimension that mattered.
> Two scan ENGINES over one TREE cross-check the engines, not the tree — and the tree was the
> wrong one. A two-method check defends against a scan-pattern false negative; it is blind to a
> shared corpus-state error, which is the false-positive twin of that failure mode. **Forward rule
> this record now carries: a census-at-SHA must be run at the SHA — `git grep <SHA>` or a detached
> worktree — never against a working tree that has moved past it.** The class-table splits below
> were rebuilt from the `d129e7ac` site list for the same reason.

Surface forms found (why a `"pre-geodesic plasma"` fixed-string grep is NOT the right query):
`pre-geodesic plasma` in 15 punctuation variants, plus bare `pre-geodesic`, `pre-geodesic fluid`,
`pre-geodesic vacuum`, and `pre-geodesic (γ=−1, …)`.

## 2. The cost, by class

Rebuilt from the `d129e7ac` site list (see the correction above). **Lines** are the primary unit
and sum to 51; **files** are counted distinctly per class and therefore do NOT sum to 30, because
two files (`trampoline-analogy-primer.md`, `14_phase_diagrams.tex`) carry both renameable prose and
a quote surface. Distinct files across all classes = 30.

| class | lines | files (distinct, class-local) | treatment |
|---|---|---|---|
| **live canon — renameable prose** | 19 | 7 | rename in place |
| **verbatim-quote surfaces** (a site that quotes another site's bytes, or is itself quoted) | 4 | 4 | quotation bytes preserved, gloss attached |
| **figure code + rendered label** | 2 | 1 | rename in source; regeneration routed, NOT run here |
| **Q1 — frozen / preserved-historical** (`research/_archive/**`, dated preregs / results / notes / charters, merged docket records, the framing note that PROPOSED the rename) | 26 | 20 | untouched |
| **TOTAL** | **51** | **30** | |

The four quote surfaces, named so the class is checkable rather than asserted:
`cosmic-axes-and-frames-glossary.md`:75, `trampoline-analogy-primer.md`:269,
`04_generative_cosmology.tex`:491, `14_phase_diagrams.tex`:48.

⚑ **Scope word on "bytes preserved", corrected 2026-08-06.** It means the **quotation's** bytes,
not the whole line. At three of those four the gloss is a pure append and the line's pre-existing
bytes survive intact; at `four-regimes.md`:31 — which is a **rename site**, listed under renameable
prose, not here — the live prose around the quotation WAS rewritten while the quotation
*"supercooled pre-geodesic plasma"* kept its bytes. Stating it as whole-surface byte preservation
was over-broad and is retracted.

Q1 is the majority of the surface, which is the expected shape: this vocabulary is fifteen months
old and most of its occurrences are in documents that record what was thought at their date.

## 3. The history split, per site — this is the part that is NOT mechanical

R9's split is not a find-and-replace: the same old phrase maps to **two different new words**
depending on which history the sentence is about.

| sentence is about | new word |
|---|---|
| the BH interior / Regime-IV local rupture endpoint (bonded once, released) | **de-bonded state** |
| the primordial pre-freeze parent medium (never bonded) | **pre-bond state** |
| the PHASE as such, history-neutral | **pre-bond state**, with the split named |

**Sites whose OPERATIVE renamed word is `de-bonded` — the full set, re-derived from the shipped
diff 2026-08-06 (Tier-2 fix pass), 7 line-cites across 5 files:**

| site | why de-bonded |
|---|---|
| `boundary-observables-m-q-j.md`:51 | BH-horizon row |
| `trampoline-framework.md`:713 | BH row |
| `trampoline-analogy-primer.md`:267 | Regime IV — reached from inside the crystal |
| `trampoline-analogy-primer.md`:543 | Vol 3 Ch 21 framing |
| `14_phase_diagrams.tex`:127 | BH interior, explicitly |
| `14_phase_diagrams.tex`:223 | BH-interior row of the regime table |
| `four-regimes.md`:31 | Regime-IV local rupture endpoint |

> **🔴 CORRECTION, 2026-08-06.** The first version of this section listed only the first four and
> then asserted *"Every other live site reads **pre-bond**"* — **false**, and the shipped edits are
> the evidence: `14_phase_diagrams.tex`:127/:223 and `four-regimes.md`:31 all read **de-bonded**.
> The universal is withdrawn and replaced by the enumerated set above. **No physics moves:** all
> three omitted sites are BH-interior / Regime-IV contexts, so `de-bonded` is the CORRECT word for
> them under R9's split — the defect was in the record of what the rename did, not in the rename.
> Every renameable-prose site not in this table reads **pre-bond**.

⚑ **Open, surfaced not fixed (Tier-2 corroborating observation).** The figure label at
`gen_true_phase_diagram.py`:98 now reads `MELT  (pre-bond state)` over a caption line whose first
referent is `BH interior` — and a BH interior is **de-bonded** under this same split. The label has
three referents (BH interior / parent medium / pre-K4 cosmos) spanning both histories, so no single
word is right for it. Naming it is a wording call on a rendered figure and is **routed with F4's
regeneration item**, not decided here.

## 4. Fences carried into the execution

- **C6 (rescope-v2 correction):** *"The pre-bond rename census (follow-on brief item 7) must not
  touch D3-scoped sites"* — the secondary-EMT-scale *"amorphous network"* sense. Checked: the
  `pre-geodesic` surface and the D3 `amorphous` surface are **disjoint** at the census SHA, two
  methods — zero pre-existing lines carry both — so the fence costs nothing here and is recorded
  as satisfied rather than assumed. **At this branch's tip THREE lines carry both**, re-derived
  2026-08-06 two methods (`git grep` + an independent Python line-scan over `git ls-files`), and
  all three are authored by this PR: `axiom-register.md`:151 (the Axiom-1 vocabulary rider),
  `cosmic-axes-and-frames-glossary.md`:75 (this PR's own currency gloss, which classes "plasma" as
  a leak of the retired-"amorphous" kind), and this record's own line above. **None is a D3
  `amorphous network` site**, so the C6 fence holds on the merits — checked independently: none of
  the five D3 sites (`substrate-native-terminology.md`:50, `appendix-derived-numerology.md`:50,
  `topological-packing-fraction.md`:16, `02_full_derivation_chain.tex`:357,
  `01_gravity_and_yield.tex`:23) appears in this PR's 41-file diff.
  🔴 **CORRECTION, 2026-08-06:** this parenthetical previously read *"exactly one line carries
  both"*. It was false the instant it landed — the same commit that wrote it also wrote the
  glossary gloss — and it was the one count in this block that skipped the second method the
  section header demands.
- **Lock-vocab fence (brief item 7 scope note):** the R17 lock vocabulary (phase-lock bond, lock
  range, free-running, the Adler carve) is register-**PROPOSED** and must NOT ride this pass into
  canon. Checked after execution: zero lock-vocab tokens introduced at any renamed site.
- **Line-count discipline:** every edit is in-place on its own line. No line is inserted or
  removed at any site, so no `path:NN` cite into any touched file moves.

## 5. What this census does NOT do

It adjudicates no physics, promotes no phase to a named thermodynamic object, and does not touch
the OPEN question of what the substance-level (de-bonded) constitutive law is — which R17's C7
disposition names as the program's deepest open object. It renames a word.
