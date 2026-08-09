# Spec correction — signed-Γ tag: call-site spelling (R31) + the census instrument (R33)

### ENTRY 2026-08-07-gamma-tag-spec-correction

**Class:** records / dated spec correction. Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`, moves no
solidity, adjudicates no channel, prefers no density branch.
**Authority:** R31 and R33, [`2026-08-07-rulings-r31-r33.md`](2026-08-07-rulings-r31-r33.md) —
Grant verbatim *"Ratify."* (R31) and *"Agree."* (R33).

**The frozen spec body is BYTE-UNTOUCHED.**
[`2026-08-07-gamma-tag-spec.md`](2026-08-07-gamma-tag-spec.md) stays exactly as merged (#918); this
is a dated correction beside it, not a rewrite. R31's own words: *"§3 froze the macro NAME; the
call-site spelling is corrected by a DATED SPEC-CORRECTION FRAGMENT (the frozen spec body
untouched)"*.

**MEASURED-AT-SHA.** Every number below is re-measured at `origin/main` = **`644a4546`**, in a
worktree at that commit verified clean (`git status --porcelain` = 0) before any edit, per the
spec's own §2 census-at-SHA rule. Counts taken at an earlier SHA are marked as such where they
appear.

---

## 1. R31 — the call-site spelling is `\gammaundeclared{}`

§3 froze the macro **name** and its definition. Both are unchanged and remain byte-exact in
`manuscript/structure/commands.tex`. What this fragment corrects is the **call-site spelling**: the
executing pass wrote `\gammaundeclared{}`, where §3's illustrative example shows the bare
`\gammaundeclared`.

**Why the bare form cannot be used.** TeX discards the space that follows a multi-letter control
word. At **136 of the 205** tag sites the next character is a space (132) or the end of line (4), so
the bare token would delete a printed space — violating §3 property 1, *"Renders as nothing. The tag
changes no printed character"*, which §3 itself calls load-bearing.

**The measurement** (`pdflatex`, one document, seven lines, `pdftotext` output verbatim):

| line | source | rendered |
|---|---|---|
| A | `$\Gamma = -1$ wall.` | `Γ = −1 wall.` — untagged baseline |
| B | `$\Gamma = -1$\gammaundeclared wall.` | `Γ = −1wall.` — **space gobbled** |
| C | `$\Gamma = -1$\gammaundeclared{} wall.` | `Γ = −1 wall.` — **identical to A** |
| D | `$\Gamma = -1$\gammaundeclared\ wall.` | `Γ = −1 wall.` — correct *here* |
| E | `(short $\Gamma = -1$) end.` | `(short Γ = −1) end.` — untagged baseline |
| F | `(short $\Gamma = -1$\gammaundeclared{}) end.` | `(short Γ = −1) end.` — **identical to E** |
| G | `(short $\Gamma = -1$\gammaundeclared\ ) end.` | `(short Γ = −1 ) end.` — **spurious space** |

**The two alternatives, measured and rejected.**

- **`\gammaundeclared\ `** (control-space) — rows D and G. It repairs the space-followed sites and
  **breaks the other 69**: at every punctuation-adjacent site it injects a space that was not there
  (`Γ = −1 )` instead of `Γ = −1)`). Trading a deletion at 136 sites for an insertion at 69 is not
  a repair. Next-character census of the 205 sites at `644a4546`: space 132, `)` 38, `,` 15, `;` 5,
  `:` 4, EOL 4, `-` 4, `}` 2, `.` 1.
- **`xspace`** — would decide per following character, but requires `\usepackage{xspace}` in the
  shared preamble for all eight volumes. A package dependency for a marker that must render nothing
  is a larger blast radius than the marker itself.

**The executed form keeps every frozen property.** Argument-free — `{}` is an empty group, not a
channel slot, so there is still nothing to guess into and the hand-set attribution R1 rejected is
still unreachable. Renders as nothing — rows C and F, and two whole-volume `pdftotext` diffs banked
in #923 (vol 1, 8632 lines; vol 9, 16878 lines; both empty). Machine-countable — see §2.

## 2. R31 — the §3 counting correction

§3 property 3 offers `git grep -c '\gammaundeclared'` as the population query. **`git grep -c`
counts LINES, not occurrences**, and 15 of the 205 markers share a line with another marker. At
`644a4546`, two methods (`git grep` and an independent Python `rglob` + `re` walk, agreeing exactly):

| query | scope | value | what it is |
|---|---|---|---|
| `git grep -c` | `manuscript` | **191** | LINES — 190 marker lines + 1 definition line |
| `git grep -c` | whole repo | 198 | + 5 spec-fragment lines + 2 in the R31–R33 ruling record |
| `git grep -o … \| wc -l` | `manuscript` | **206** | OCCURRENCES — 205 markers + 1 definition |
| `git grep -o … \| wc -l` | whole repo | **213** | 205 + 1 definition + 5 spec fragment + 2 ruling record |

**The population method the discharge workstream inherits is `git grep -o … | wc -l`**, scoped to
`manuscript` and netting out the one definition — **205**.

> ⚑ **Drift note, and why the re-measurement rule earns its keep.** The repo-wide occurrence figure
> was **211** when #923 measured it and is **213** here. Nothing in the manuscript moved: the R31–R33
> ruling record itself quotes the macro twice. A whole-repo count of this token is a count of the
> corpus's own discussion of the token, which is why the scoped `manuscript` figure is the one that
> means anything.

## 3. R33 — the census instrument, repaired

The ruling: *"The spec's §1 adjacency definition stands; the instrument diverges."* §1 is unchanged.
`src/scripts/signed_gamma_census.py` is changed.

**Three measured defects, each a divergence from §1's own words** (*"a location where **a signed
value is asserted for Γ**"*, and condition 4's rationale *"a Γ merely mentioned asserts nothing to
declare"*):

1. **NON-ADJACENT VALUE** — `classify_sign` called `_VALUE_RE.**search**` over the whole remainder
   of the line, so a Γ that asserts nothing inherited a later Γ's value. Worst case on the #923
   corpus: `vol_2_subatomic/chapters/01_topological_matter.tex`:167 read its "adjacent" value from
   **410 characters away**. **Repair:** the relation must be reachable across the BRIDGE only
   (a closing magnitude bar, `^2`, a subscript, and the gap characters `GAPS["adjacent-nested"]`
   already admits), and the whole reading is confined to the enclosing inline-math span.
2. **TRUNCATED VALUE** — the numeral was accepted with no check on what follows, so `= 1 - \alpha`,
   `= 1/3` and `= 1/9` all classified `+1`. **Repair:** a numeral continued by an arithmetic
   operator classifies `other` — visible in the census, never silently dropped, which is the
   module's existing stated philosophy for `= -1.0`.
3. **NOT THE LEFT OPERAND** — `T^2 = 1 - \Gamma^2 \to 1` gave Γ a limit belonging to `T^2`, on lines
   that go on to say *"at $\Gamma = 0$"*. **Repair:** the Γ (optionally inside magnitude bars) must
   be the relation's left operand.

**The comment test is repaired too, and here is the scope note.** `is_comment_line` tests only a
line's FIRST token, so `figures/electron_selfbiased_multiport.tex`:46 —
`\draw … (3.6,-1.6); % shorted stub / Gamma=-1 wall` — reported `rendered` with its Γ inside a
trailing comment. A new `is_comment_site(suffix, line, column)` makes `rendered` a property of the
OCCURRENCE. `is_comment_line` is **kept and unchanged**: it backs the `--comments` universe knob,
which selects whole lines, and that knob's meaning does not change.

**Detection is untouched.** Only classification changed, so the two-method self-check still compares
the same raw detection set — it re-runs green at `644a4546` (`agree, A = B = 2150 lines`). No
universe knob, no preset, and no ERE pattern moved.

**Why 2150 and not the spec's 2146 — the delta is fully accounted, and none of it is the repair.**
Detection-line sets diffed between `91a910f8` and `644a4546`: **+4 lines, 0 removed**, and the same
instrument reproduces `2146` on the `91a910f8` corpus.

- `manuscript/structure/commands.tex`:163 and :165 — the macro's OWN `%`-comment documentation,
  matched because `gamma_form=all` admits a bare ASCII `Gamma`. **The same self-referential drift
  class as §2's 211 → 213 note**: the corpus now discusses the token, so a corpus-wide scan for the
  token counts the discussion.
- `manuscript/ave-kb/common/translation-tables/translation-circuit.md`:991 and
  `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md`:283 — unrelated KB
  merges landed between the two SHAs. Nothing to do with this lane.

**The bridge is composed from the knob, not copied from it** (NOTE-3a). `_BRIDGE_RE` is built from
`SUBSCRIPT_NESTED` + `GAP_CHARS_NESTED` — the two named pieces `GAPS["adjacent-nested"]` is itself
now composed from — so widening or narrowing that knob moves the classifier's notion of "adjacent"
with it. A duplicated character class would let knob and classifier drift apart silently, which is
the defect class R33 exists to close one level up. The refactor is byte-neutral: the emitted
detection regex is **string-identical** before and after, asserted on the same universe.

## 4. R33 — the mutation receipt

`research/drivers/gamma_census_adjacency_number_check.py`, auto-discovered by
`make verify` through `verify-lane-number-checks` (the `research/drivers/*_number_check.py` glob);
its receipt is auto-run because the source declares the literal `--mutation-receipt`. It is also
runnable standalone.

**What each check consumes, scoped honestly.** IDENTITY and the planted families consume **no
declared number** — both sides are recomputed on the run, from the tree and from the classifier.
FINDINGS consumes **29 frozen `expected_post_fix` baselines**. That is a legitimate REGRESSION
BASELINE rather than a self-declared field — each was measured at the #923 execution SHA `2520e467`
and re-measured at `644a4546`, reproducing at both — but it is a baseline, and reading the whole
gate as baseline-free would be wrong.

**Plain run at `644a4546`:**

```
post-R33 actionable : 206 sites / 190 lines / 61 files
merged tags         : 205 markers / 190 lines
§4.4 do-not-touch   : 1 (12_cosmological_characteristics.tex:190, quoted ruled text)
identity            : 206 = 205 tagged + 1 site-selection exclusion
OK — identity reconciled, 29 finding line(s) re-checked, 6 planted case(s) correct.
```

**The reconciliation identity, stated plainly:**

```
post-R33 actionable  = 206
                     = 205 tagged  +  1 §4.4 site-selection exclusion
32 of the 33 #923 findings were INSTRUMENT ARTIFACTS and are gone.
 1 of the 33 was never a classification question at all.
```

> ⚑ **The 33rd finding is NOT eliminated, and must not be.** R33's target was *"the repaired
> classifier reproduces all 33 findings"*. Thirty-two do reproduce. The thirty-third —
> `vol_9_vacuum_datasheet/chapters/12_cosmological_characteristics.tex`:190, whose Γ sits inside a
> verbatim ``` ``…'' ``` quotation of a canonical KB leaf — is a **spec §4 item 4 SITE-SELECTION
> exclusion** (*"any line inside quoted ruled text"*), not a §1 classification property. §1 has four
> conditions — file class, rendered, channel, sign — and quotation is not one of them. Teaching the
> census to suppress it would be building the instrument to hit a pre-decided number, which is the
> checklist-wearing-a-gate defect this module's own docstring exists to prevent. It is therefore
> correctly **actionable** and correctly **untagged**, and the driver asserts exactly that.

**Planted cases — the forced-failure proof.** Nine synthetic lines; nothing in them reads the
corpus, so a corpus edit can never quietly turn one green. Seven assert a **sign**, two assert
**`rendered`** (the comment repair is not a sign property and needs its own control).

| case | asserts | expected | fix ON | fix FORCED OFF |
|---|---|---|---|---|
| FAR-VALUE (the only ±1 sits far away, past a math-mode exit) | sign | `none` | `none` ✓ | **`-1`** ← the defect |
| TRUNCATED (`\|\Gamma\|^2 = 1 - \alpha`) | sign | `other` | `other` ✓ | **`+1`** ← the defect |
| NOT-LEFT-OPERAND (`T^2 = 1 - \Gamma^2 \to 1` … `at $\Gamma = 0$`) | sign | `none` | `none` ✓ | **`+1`** ← the defect |
| **MATH-SPAN** (`($\Gamma$ = -1)` — value OUTSIDE the Γ's math span) | sign | `none` | `none` ✓ | **`-1`** ← the defect |
| **TRAILING-COMMENT** (`\draw …; % … ($\Gamma = -1$) wall`) | `rendered` | `False` | `False` ✓ | **`True`** ← the defect |
| ADJACENT (`$\Gamma = -1$` in its own span) | sign | `-1` | `-1` ✓ | `-1` |
| MAGNITUDE (`$\|\Gamma\| = 1$`) | sign | `+1` | `+1` ✓ | `+1` |
| CHAIN (`\Gamma = \frac{…}{…} = \frac{…}{…} = -1`) | sign | `-1` | `-1` ✓ | `-1` |
| RENDERED-CONTROL (no comment anywhere) | `rendered` | `True` | `True` ✓ | `True` |

The last four are deliberate **non-regression** cases: the repair must not eat assertions that were
always correct, and must not start suppressing typeset sites. It does neither.

**Two of these controls exist because attribution without a control is not evidence.**

- **MATH-SPAN** isolates the span confinement, and it is built so nothing else can mask it: the text
  before the Γ ends in an opener (left-operand passes), the value is a clean `-1` (the termination
  guard passes), and `$` is a BRIDGE character — so the anchored bridge would walk straight out of
  the math span and read `= -1` from text mode. Measured: with `math_segment` neutered and every
  other repair left on, the line reads `-1`; with it on, `none`. Without this case the span
  confinement would be a **conservative narrowing with no independent control** — corpus-wide it
  changes 18 classifications and **zero inside the actionable slice**, and FAR-VALUE is caught by
  the bridge either way.
- **TRAILING-COMMENT** isolates `is_comment_site`, which today is otherwise **behaviourally
  masked**: on the whole corpus it differs from `is_comment_line` at exactly **one** site
  (`figures/electron_selfbiased_multiport.tex`:46) and at that site the left-operand guard fires
  first. So the planted line puts an opener before the Γ and a clean adjacent value after it —
  leaving the comment repair as the only thing that can catch it.

**Attribution corrected in the driver's own registry** (same reason). `classify_sign`
short-circuits on the left-operand test before it reads a value, so a site can be caught by two
repairs at once and the #923 triage label is not always today's eliminating guard. Two rows are now
DUAL-labelled: `figures/electron_selfbiased_multiport.tex`:46 (TRAILING-COMMENT sets
`rendered=False` **and** NOT-THE-LEFT-OPERAND sets `sign=none`; both fire independently) and
`16_silicon.tex`:89 (triaged TRUNCATED-VALUE, eliminated by NOT-THE-LEFT-OPERAND; both fire).

**Receipt run (`--mutation-receipt`, `ADJACENCY_FIX` forced off, corpus untouched):**

```
FIRED   IDENTITY                   — the actionable set no longer reconciles against the tag population
FIRED   FINDINGS                   — the #923 finding lines come back as actionable
FIRED   PLANTED[FAR-VALUE]         — a value far down the line is read as adjacent again
FIRED   PLANTED[TRUNCATED]         — `= 1 - \alpha` is read as `+1` again
FIRED   PLANTED[NOT-LEFT-OPERAND]  — T^2's limit is attributed to Gamma again
FIRED   PLANTED[MATH-SPAN]         — the bridge walks out of the math span and reads a foreign value
FIRED   PLANTED[TRAILING-COMMENT]  — a Gamma inside a trailing comment counts as typeset again
perturbed run produced 34 failure(s)
RECEIPT OK — every declared control fired under the forced-off instrument.
```

All **seven** declared controls fire under the perturbation, so no check here is a tautology over an
unperturbed instrument, and every named repair has a control that isolates it.

**Where the second §4.4 site went.** The printed line reads `§4.4 do-not-touch : 1`, while #923
recorded **two** §4.4 do-not-touch classes. The other one —
`figures/electron_selfbiased_multiport.tex`:46, withheld as a `%`-comment line — has **migrated out
of §4.4 and into §1**: with `is_comment_site` in place its Γ is no longer `rendered`, so it fails a
§1 condition on its own and never reaches the site-selection stage. One do-not-touch class became a
classification. The quoted-ruled-text site is the only §4.4 exclusion left, and that is why the
count is 1.

## 5. What this correction does NOT do

It does not rewrite the frozen spec, does not re-open the §1 definition, does not retag or untag a
single print site, adjudicates no channel, prefers no density branch, and leaves the `Γ_shear` sign
exactly where canon has it — **unresolved**, at `manuscript/ave-kb/common/wall-taxonomy.md` §10.1.
It corrects a spelling, a counting method, and an instrument.
