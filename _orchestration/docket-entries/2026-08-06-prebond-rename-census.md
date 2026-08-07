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

**Two methods, and they agree exactly.** Method A `git grep -in`; method B an independent
`grep -rin` over `*.md` / `*.tex` / `*.py` / `*.json`. Both return **52 lines across 31 files**,
symmetric difference **empty**. Reported because a single-method count in this repo has a
documented false-negative floor.

Surface forms found (why a `"pre-geodesic plasma"` fixed-string grep is NOT the right query):
`pre-geodesic plasma` in 15 punctuation variants, plus bare `pre-geodesic`, `pre-geodesic fluid`,
`pre-geodesic vacuum`, and `pre-geodesic (γ=−1, …)`.

## 2. The cost, by class

| class | files | lines | treatment |
|---|---|---|---|
| **live canon — renameable prose** | 8 | 21 | rename in place |
| **verbatim-quote surfaces** (a site that quotes another site's bytes, or is itself quoted) | 4 | 6 | bytes preserved, gloss attached |
| **figure code + rendered label** | 1 | 2 | rename in source; regeneration routed, NOT run here |
| **Q1 — frozen / preserved-historical** (`research/_archive/**`, dated preregs / results / notes / charters, merged docket records, the framing note that PROPOSED the rename) | 18 | 23 | untouched |

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

Sites reading **de-bonded**: `boundary-observables-m-q-j.md`:51 (BH-horizon row),
`trampoline-framework.md`:713 (BH row), `trampoline-analogy-primer.md`:267 (Regime IV) and `:543`
(Vol 3 Ch 21 framing). Every other live site reads **pre-bond**.

## 4. Fences carried into the execution

- **C6 (rescope-v2 correction):** *"The pre-bond rename census (follow-on brief item 7) must not
  touch D3-scoped sites"* — the secondary-EMT-scale *"amorphous network"* sense. Checked: the
  `pre-geodesic` surface and the D3 `amorphous` surface are **disjoint** at the census SHA, two
  methods — zero pre-existing lines carry both — so the fence costs nothing here and is recorded
  as satisfied rather than assumed. (At this branch's tip exactly one line carries both, and it is
  this PR's own Axiom-1 vocabulary rider, which quotes R7's fence and R8's leak classification and
  renames nothing.)
- **Lock-vocab fence (brief item 7 scope note):** the R17 lock vocabulary (phase-lock bond, lock
  range, free-running, the Adler carve) is register-**PROPOSED** and must NOT ride this pass into
  canon. Checked after execution: zero lock-vocab tokens introduced at any renamed site.
- **Line-count discipline:** every edit is in-place on its own line. No line is inserted or
  removed at any site, so no `path:NN` cite into any touched file moves.

## 5. What this census does NOT do

It adjudicates no physics, promotes no phase to a named thermodynamic object, and does not touch
the OPEN question of what the substance-level (de-bonded) constitutive law is — which R17's C7
disposition names as the program's deepest open object. It renames a word.
