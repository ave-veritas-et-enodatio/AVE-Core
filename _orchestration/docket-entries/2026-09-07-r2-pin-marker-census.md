### ENTRY 2026-09-07-r2-pin-marker-census

**Lane:** doc/tooling — the MIGRATION half of ruling **R2**
(`2026-08-06-rulings-decision-batch.md`, Grant verbatim *"1. agree / 2. agree /
3. agree / 4. agree / 5. agree"*; re-authorised 2026-09-07, *"build the pin
marker"*). The gate half — teaching `verify-md-links.py` the marker — is a
parallel lane's and is **not** touched here.

Base for every number below: `5a36cea5`, measured in a pristine `git worktree`
(the line-cite pass walks the filesystem, so untracked local files would
otherwise resolve paths a fresh clone cannot).

---

## 1. The token — READ FROM CANON, NOT COINED

```text
per `some-leaf.md:42` pin:`c4a546dc` — "the sentence that line carried then"
```

`` pin:`<7–40 lowercase hex>` ``, immediately to the RIGHT of the cite it pins,
binding **the nearest cite to its left and no other**. This is not this lane's
invention. It was written on **2026-08-06** by the doc lane R2 routed it to and
has been canon ever since, at `manuscript/ave-kb/CONVENTIONS.md`, section
*"Author-declared pin marker — the forward convention (2026-08-06)"*. That
section also records the coinage measurement — **0 prior corpus hits at
`d129e7ac`**, two methods (a fixed-string `git grep -F` for the four-character
opener, and an independent `grep -r` over `*.md` / `*.tex` / `*.py`).

> ⚠ **The first round of this lane coined a SECOND token, `path:NN@<sha>`, for
> the concept the corpus already named.** It asked whether its own candidates
> collided with each other and never asked whether one already existed; its
> coinage-grep probed `@pin:` and `{pin `, both of which miss the backticked
> `` pin:`sha` `` form. `ave-vocab-discipline`'s COINAGE rule answers this
> directly — an existing meaning is REUSED, not silently overloaded. The
> `@<sha>` spelling is retracted; nothing in the corpus ever carried it outside
> that round's own two pilot cites, both of which are re-keyed here.

**The re-key is not cosmetic.** `@<sha>` glued the SHA INSIDE the cite token, so
a migrated cite stopped matching the cite grammar altogether: the corpus census
fell 525 → 523 the moment two cites were marked. A marker-only gate would then
never see the cite it is supposed to be reading a marker for. `` pin:`sha` ``
sits outside the token, so a marked cite stays a well-formed cite — population
525 → 525, with `cites bound by a marker` 0 → 2. That is the shape a gate wants.

**No flag day.** The marker embeds a backticked SHA, so a marked cite is exempt
under the heritage rule AND the marker rule simultaneously. Migration and re-key
can land in either order.

### 1b. What R2's doc half actually needed

Nothing. It was discharged on 2026-08-06. What was never built is the CHECKER,
and that is the parallel gate lane's. This lane's remit is the MIGRATION half
only: census, classify, mark.

## 2. Census — the numbers R2 quoted are stale, and so is their shape

R2's "96" was KB-scoped at snapshot `d5a1b06b`. Re-measured at `5a36cea5`:

| scope | line-cites on a SHA-bearing line | distinct lines | lines >500 chars |
|---|---|---|---|
| corpus-wide | **525** | 271 | 182 |
| KB only | **156** | — | — |

Method: `pin_census_lib` imports `iter_line_cites`, `cite_target_uncheckable`
and `resolve_cite_candidates` **from `verify-md-links.py` itself**, so the
census measures the exact population the gate acts on rather than a lookalike
one. Cites with no `:NN` are excluded (the gate has no line to check).

Classification of those 525:

| class | n | what it is |
|---|---:|---|
| **LIVE** | **480** | resolves at HEAD; a normal cite that merely shares a row with somebody else's provenance SHA |
| **TRUE-PIN** | **5** | does not resolve at HEAD; corroborated at a SHA on its own row |
| **DEAD** | **0** | path resolves, line does not, nothing claims a pin |
| UNRESOLVED-PATH | 34 | path names nothing anywhere (house shorthand, sibling-repo files, line-wrapped names) — already advisory-reported |
| SKIPPED-SHAPE | 6 | glob / home-dir / ephemeral target — out of scope for both tools |

### 2b. Where the split between DEAD and UNRESOLVED-PATH was drawn, and why

Read literally, "resolves to nothing and no prose claims it is pinned" covers
the 34 UNRESOLVED-PATH rows too. They are split out because the gate splits
them: a cite whose PATH fails is advisory (`broken backtick path`), a cite
whose LINE fails is gating (`dead line cite`), and only the second changes
behaviour when the exemption is re-keyed. Under the single-bucket reading the
numbers are LIVE 480 / TRUE-PIN 5 / DEAD 34.

Those 34 are not 34 defects. **28 name a basename the repo has never had**, so
they cannot be renames — they are house shorthand (`vol_0/02_analytical_
summaries.tex` for the `vol_0_engineering_compendium/chapters/` file),
sibling-repo paths, skill files under `~/.claude`, and names truncated by
line-wrapping. Measured two structurally different ways, both **28 / 34**:

1. build the set of every basename ever named in a diff across all refs
   (`git log --all --format= --name-only`, 6,664 distinct paths) and test
   membership in Python;
2. ask git's own pathspec engine per basename
   (`git log --all --format=%H -1 -- '*/<base>' '<base>'`).

> ⛔ **CORRECTION (D5) — the first round reported 29, not 28.** Both methods
> here return 28, and they agree row by row. The residue is therefore **6**
> had-a-basename rows, not 5.

Of those 6: **four are manuscript shorthand** (`vol_0/chapters/03_computational_
graph.tex`, `vol_0/02_analytical_summaries.tex` ×2, `vol_2/06_electroweak_and_
higgs.tex` — each names a real file under `manuscript/vol_*/chapters/`, written
in board shorthand). The other two are the interesting ones.

**⛔ CORRECTION (D4) — the first round's "one real piece of rot" is
mis-attributed, and it is not rot.** It named:

> `_orchestration/2026-07_repo-conventions.md:184` cites
> `research/2026-06-22_birefringence-vca-bench-arc.md:75` … The citing sentence
> says *"At HEAD, … reads …"*, so it is a live claim about a path that resolves
> nowhere.

Line 184 carries **two** cites of that basename, and the `At HEAD` clause
belongs to the OTHER one:

- `` `_orchestration/2026-06-22_birefringence-vca-bench-arc.md:75` `` — this is
  what the sentence *"At HEAD, … reads …"* attaches to, and it **resolves**
  (census: LIVE);
- `` `research/2026-06-22_birefringence-vca-bench-arc.md:75` `` — appears only
  inside the closing parenthetical, which reads in full: *"(The brief cited this
  file as `research/…:75` — it is actually in `_orchestration/`, not `research/`;
  flagged in the ledger.)"*

So the unresolvable cite is a **deliberate quotation of a known-wrong path,
self-flagged in the same sentence**. Not rot at all. And attributing one cite's
clause to its row-mate is *precisely* the row-level mis-attribution R2 exists to
end — this docket committed it while arguing against it.

**The real rot in the residue is the sixth row**, and it is a better
advertisement for R2 than the retracted one:

> `_orchestration/parallel-site-gate.md:11` cites
> `research/2026-06-11_screened-winding-probe_result.md:16` inside a live claim
> (*"built the `screened-winding-probe` entry from the source's top `## VERDICT`
> block"*). That file was added on a branch (`33269545`) and **never landed on
> main** — 0 hits in `git ls-files` at HEAD. Line 16 exists at `836ee6de`. The
> two SHAs the row does carry, `532e27d5` and `bfa94beb`, **do not contain the
> file at all**, so the cite rides a row-level exemption that has nothing to do
> with it and cannot even be repaired by a path fix. Its correct repair is an
> explicit `` pin:`836ee6de` `` — i.e. exactly the marker R2 ruled — or deletion
> of the line cite.

That row is structurally the same shape as TRUE-PIN #1 below (a branch-only
file), and the only thing separating them is whether the enabling SHA happens to
sit on the row.

**99% of what the exemption hides is a live cite.** That is R2's false-negative
claim, measured.

## 3. The load-bearing consequence: re-keying the gate is FREE

Removing the SHA exemption today makes **zero** cites newly gate. Measured two
ways, and they agree:

1. the census: LIVE 480 / DEAD 0;
2. the gate's own `check_line_cites`, run over the whole corpus twice — once
   as shipped, once with `LineCite.pinned` forced False. **Re-run and
   confirmed on 2026-09-07:**

   | counter | exemption ON | exemption FORCED OFF |
   |---|---:|---:|
   | `skipped_historical_pin` | 480 | 0 |
   | `checked` | 13,644 | **14,124** (+480) |
   | `dead line cite` | **11** | **11** (+0) |
   | `blank line cite` | 1,112 | 1,144 (+32, advisory) |

   The 480 move from *skipped* to *checked* and **not one of them is dead**.
   The 11 dead cites are pre-existing and unrelated to the exemption.

So the marker migration is not a prerequisite for the re-key. It buys machine-
readability for four cites; the re-key buys ~480 cites of coverage. If only one
of the two halves of R2 ever lands, it should be the re-key.

### 3b. ✅ THE FLIP LANDED — 2026-09-12, post-integration numbers

Both halves are merged, the four marks are placed, and the exemption is **OFF**.
Measured on the integrated branch at `42dd7b40` through the real CLI (no forced
flags, so the constant is what decides the run):

| counter | exemption ON | exemption OFF |
|---|---:|---:|
| MARKER-EXEMPT | 8 | 8 |
| HERITAGE-EXEMPT | 485 | **0** |
| CHECKED | 13,644 | **14,129** (+485) |
| `dead line cite` | **11** | **11** (+0 — and the **same eleven**, diffed byte for byte) |
| GATING dead | **0** | **0** |
| `blank line cite` (advisory, never gating) | 1,112 | 1,144 (+32) |
| gating errors | 0 | 0 |
| exit code | **0** | **0** |

**ZERO cites newly gate**, so the flip ran. The dead-cite SETS were diffed, not
just their counts — the stricter test, and they are identical.

Numbers differ slightly from §3's 2026-09-07 measurement (485 vs 480, +32 vs
+30) for the reason §5's caveat (b) already names: the docket entries and tools
merged in this branch are themselves part of the corpus now, and they carry
cites. Nothing load-bearing moves.

**⚠ The flip was not the one line the switch's own comment promised.**
`main()` bound `heritage_exemption=not args.no_heritage_pin_exemption` — the CLI
flag, never `HERITAGE_PIN_EXEMPTION`. Setting the constant False alone would
have changed **nothing that `make verify` runs**: a switch nobody had exercised
through `main()` was decorative, and the terminal step could have been reported
as landed without altering one check. Now the constant is the default and the
flag an override, with a regression test that was verified to FAIL when the
original binding is put back.

**⚠ And LIVE still means the cited LINE EXISTS, not that its content still
matches.** The 485 cites of coverage this buys are line-existence coverage. A
45-cite read of the LIVE population on 2026-09-12 found **7 pointing at a line
that no longer says what the citing sentence says it says** — 15.6%, Wilson 95%
CI [7.7%, 28.8%], i.e. roughly 37–138 of the population — with a judgment-free
floor of **24 LIVE cites resolving to a line that is literally empty at HEAD**
and 33 to a line the gate's own `_CONTENTLESS_LINE_RE` calls contentless. Three
of the seven are **status inversions**, not line shifts: a docket calls a claim
"STILL ASSERTED LIVE" at a line that now reads CONTESTED; another flags a leaf
for stating LINEAR at a line that now states QUADRATIC under a RESOLVED note; a
result doc flags a leaf for "PR-pending" text that no longer exists in the file
at all. Re-running the gate with the exemption off over those seven produces
**five findings of no kind at all and two ADVISORY blanks** — so the flip
neither fixes the rot nor reveals it. `verify-anchor-content.py` is the advisory
home for content matching. **Do not read "LIVE 480 / DEAD 0" as "the corpus is
clean."**

## 4. Classifier precision — TRUE-PIN = **4 / 5** (byte-level, 2026-09-12)

> ⛔ **THIS SECTION'S ORIGINAL VERDICT WAS `2 / 5` AND IT WAS WRONG.** The
> correct count is **4 / 5**. The table below is the ORIGINAL, left standing
> because §4d needs it as the exhibit; **rows 3 and 4 are SUPERSEDED** and the
> corrected dispositions are in §4e. Read §4d before you use anything here.

The whole plan rests on the TRUE-PIN count, so all five were read again, by a
second reader who did not share the first reader's notes: resolve the cited line
at HEAD, resolve it at the SHA on its row, and compare what the line SAYS there
against what the citing sentence CLAIMS it says. Both passes landed on the same
two. **2 / 5** — *and that is the finding this section now exists to correct.*

| # | cite | at HEAD | at the row SHA | verdict |
|---|---|---|---|---|
| 1 | `_orchestration/2026-06-16_standing-decisions-audit-lane.md:123` → `stage15_layer_b_coupled_stability.py:58` | **no file of that name is tracked anywhere** (0 in `git ls-files`, 0 on disk) | `b2de04fc`: `src/scripts/vol_1_foundations/…` is 242 lines; **:58 = `OMEGA_BLOWUP_FACTOR = 1e3`**, the constant the sentence names | ✅ **TRUE PIN** — branch-only driver, no path repair possible even in principle; row prose says "branch-only" + "prereg `b2de04fc`" |
| 2 | `…/a1-hopf/exp-a1-hopf-repo-audit.md:417` → `_orchestration/exp-a1-hopf.md:50-57` | path gone (doc moved to `_orchestration/experimental/a1-hopf/`); the section now sits at **:63 and reads "✓ DONE 2026-05-20"** | `6621dae`: :50-57 = the *"Walk-back targets (Phase 1 of parent epic)"* table naming `torus-knot-baryon-predictions.md` + `project-hopf-02.md` | ✅ **TRUE PIN** — a path repair would be WRONG: the sentence records the STALE claim the audit found, which HEAD no longer carries. Row prose: *"audit verification at AVE-Core HEAD `6621dae`"* |
| 3 | `manuscript/ave-kb/claim-quality-closure-roadmap.md:87` → `closure-roadmap.md:80` | basename gone (renamed `claim-quality-closure-roadmap.md`, moved out of `common/`) | `4457d3e`: `manuscript/ave-kb/common/closure-roadmap.md` is 835 lines and **:80 is a `C5-CMB-AXIS` Planck-driver row** | ❌ **NOT A PIN** — the sentence claims *"E1b CMB-Hubble separation = 74.6° at 1.82σ … per `closure-roadmap.md:80`"*. Contradicted. The SHA is a branch-HEAD run stamp for a different driver |
| 4 | `manuscript/ave-kb/claim-quality-closure-roadmap.md:89` → `closure-roadmap.md:80` | same | `5f926ad`: same file, 837 lines, **:80 is a `C3-MUON-DELTA + Q-G19α` row** | ❌ **NOT A PIN** — the sentence claims *"E1b … CMB-LSS separation = 27.9° … per `closure-roadmap.md:80`"*. Contradicted. The SHA sits 5,400 characters away on a 6,112-character row |
| 5 | `research/2026-05-19_cosmic-epsilon-de-projection-mechanism.md:20` → `_orchestration/cosmic-epsilon-de-projection-scoping.md:9-17` | path gone (moved to `_orchestration/theoretical/`) | `20bb659`: :9-17 = the Q1/Q2/Q3 adjudications, exactly as the sentence says | ❌ **NOT A PIN** — the blob is **byte-identical** at `20bb659` and at HEAD; only the directory moved, and :9-17 at HEAD carries the same text. Pinning would freeze a cite whose live target is right there |

**The mechanism of all three misses, and it is not fixable by regex:** a cite
can EXIST at a SHA that sits on its row for an unrelated reason — a session
stamp, a branch-HEAD run stamp, a ruling id. Line-existence at the SHA is
*necessary* (see D2 below) but not *sufficient*; only reading the line decides.

> ⛔ **CORRECTION (D6, found on re-verification).** The first round described the
> three misses as *"Two of the three are cites broken by a rename … one resolves
> at its SHA to content that flatly contradicts."* The split is the other way
> round: **two contradict** (#3 C5-CMB-AXIS, #4 C3-MUON-DELTA) and **one is a
> clean rename** (#5). All three are also rename-broken, so "rename" does not
> discriminate; what discriminates is whether the SHA-resolved line says what
> the sentence says.

### 4d. ★ HOW 5 → 2 → 4 HAPPENED — R2's own thesis, demonstrated on R2's own verification

**This corpus writes table rows thousands of characters long.** The line under
dispute, `manuscript/ave-kb/common/closure-roadmap.md:80`, is **3,964 bytes**
(3,924 Unicode characters). Some KB rows reach 6,112.

Three readings of that one line, three different answers, one shared defect:

| pass | date | method | verdict |
|---|---|---|---|
| 1 | 2026-09-07 | the line-scoped SHA heuristic — is there a SHA *somewhere* on the row? | **5 / 5** |
| 2 | 2026-09-07 | two independent hand readers, `sed -n Np \| cut -c1-N` | **2 / 5** |
| 3 | 2026-09-12 | substring search across the WHOLE line, character offset quoted | **4 / 5** |

* Pass 1 saw a SHA on the row and concluded "pinned". That coarseness **is the
  defect R2 exists to end.**
* Pass 2 read the row's OPENING — *"a C5-CMB-AXIS Planck-driver row"* — and
  concluded "contradicted, NOT A PIN". The claim it was checking for sat
  **1,173 characters further along the same line.**
* The orchestrator then relayed the 2/5 verdict twice without opening the line.

**All three substituted a ROW-LEVEL read for a PER-CITE read.** Pass 2's two
readers AGREED — and agreed *precisely because* they made the same read of the
same head of the same line. Independent verification is not independent when
both verifiers truncate at the same offset.

The receipts, so this is checkable rather than asserted:

```text
#3  at 4457d3e, closure-roadmap.md:80 is 3,964 bytes
    "Outcome D (DATA INSUFFICIENT at 3σ)"   -> character offset 1,173
    "CMB-Hubble = 74.6° at 1.82σ"           -> character offset 1,213
    the citing sentence at claim-quality-closure-roadmap.md:87 claims exactly
    this, and the cite is CORRECT AS WRITTEN.

#4  at 5f926ad, the SAME content sits at :81, not :80.
    :81 is 3,964 bytes; "CMB-LSS = 27.9"    -> character offset 1,260
    :80 is 3,257 bytes and contains NONE of "27.9" / "CMB-LSS" /
        "DATA INSUFFICIENT"  (control, run to make the off-by-one decidable)
    -> the cite is off by EXACTLY ONE LINE. Repair, then mark.
```

**The operating rule that comes out of this.** When you resolve a cite, search
the **whole line** for the claimed content and **quote the matched region with
its character offset**. Never characterise a line by its opening.
`sed -n Np | cut -c1-N` is how this went wrong three times; it is not a
verification method on this corpus.

A live 45-cite re-audit of the LIVE population on 2026-09-12 measured the same
exposure from the other side: **8 of 45 sampled targets sit on a line over 1,000
characters**, the citing side is worse (**median citing line 1,051 chars, 23/45
over 1,000, 7/45 over 3,000**), and **five MATCH verdicts would have become
false DRIFT reports** under a head-of-row read — including
`port-register.md:87`, where the verbatim clause sits at offset 1,207 of 3,179
and the head reads as an unrelated table row. That is this same failure
reproduced on a different line, by a different reader, on the same day.

### 4e. The corrected dispositions, and what was done

| # | cite | corrected verdict | action taken 2026-09-12 |
|---|---|---|---|
| 1 | `_orchestration/2026-06-16_standing-decisions-audit-lane.md:123` → `stage15_layer_b_coupled_stability.py:58` | ✅ **TRUE PIN** (unchanged) | already marked at `b2de04fc`; left alone. Literal marker forms: §5 |
| 2 | `…/a1-hopf/exp-a1-hopf-repo-audit.md:417` → `_orchestration/exp-a1-hopf.md:50-57` | ✅ **TRUE PIN** (unchanged) | already marked at `6621dae`; left alone. Literal marker forms: §5 |
| 3 | `manuscript/ave-kb/claim-quality-closure-roadmap.md:87` → `closure-roadmap.md:80` | ✅ **TRUE PIN — and the cite is CORRECT AS WRITTEN.** §4's "contradicted" is withdrawn | MARKED at `4457d3e`; no other change. Literal marker forms: §5 |
| 4 | `manuscript/ave-kb/claim-quality-closure-roadmap.md:89` → `closure-roadmap.md:80` | ✅ **TRUE PIN, cite off by exactly one line.** §4's "contradicted" is withdrawn | REPAIRED `:80` → `:81`, then MARKED at `5f926ad`. Literal marker forms: §5 |
| 5 | `research/2026-05-19_cosmic-epsilon-de-projection-mechanism.md:20` → `_orchestration/cosmic-epsilon-de-projection-scoping.md:9-17` | ❌ **NOT A PIN** (unchanged) — blob byte-identical at `20bb659` and HEAD (`7fc4fc59`), only the directory moved | PATH REPAIR only, to `_orchestration/theoretical/…`; deliberately NOT marked |

**Four marks, one path repair, zero content corrections.** Every change is a
pointer. No numeric or physics claim was touched — that is Grant's, not a
lane's, and nothing here reached for it.

> ⚠ **And the document that defines the marker was minting false instances of
> it.** With the gate half merged, the checker flagged this docket's own two
> illustrative markers — the `some-leaf.md` token in §1 (a 4-space indented
> block, which the checker does not blank) and the `renamed-away.md` example in
> §4b — as `pin does not resolve at its own sha` and
> `orphan pin marker`. Warn-only, because `_orchestration/` is not an error
> source, and still exactly the standing trap: **a repair minting a fresh
> instance of the class it was fixing.** Both are now inside ``` fences.

Sample checks on the classes that are not being rewritten:

| class | hand-checked | classifier correct |
|---|---:|---|
| LIVE | **22** (seeded random sample of the 480; each cite's path resolved and its cited line read at HEAD) | **22 / 22** |
| UNRESOLVED-PATH | 34 — the whole population, structurally (§2b) | **34 / 34** unresolvable; 28 never-carried |
| DEAD | 0 in population | emptiness confirmed by the §3 second method |

The LIVE sample is worth one caveat, because it bounds what "LIVE" claims:
**LIVE means the cited LINE EXISTS, not that its content still matches.** Two of
the 22 resolve to a line that is empty or a bare `%` comment — and in one of
those the citing sentence is itself a `FLAG-CITE-SHIFT` note saying the symbol
has moved. Line existence is what the gate checks; content drift is a different
(advisory) pass.

→ **Do not bulk-migrate on this classifier.** `migrate-pin-markers.py`
therefore requires a hand-verified allow-list by default; `--allow-unverified`
exists but prints the measured precision first.

### 4b. D2 — the classifier would have marked genuinely dead cites

`classify` ordered

```python
elif resolving or prose:   klass = "TRUE-PIN"
```

**ahead of** the DEAD and UNRESOLVED-PATH branches, so **prose alone was
sufficient**. The auditor's fixture: a row reading

    | run at the time of `b649f9f2` | rot `target.md:99` |

where line 99 exists at **neither** HEAD nor `b649f9f2`, came out TRUE-PIN and
was rewritten. That is not a mis-classification, it is a laundering machine —
it converts undiscovered rot into a signed author declaration that the rot is
deliberate, and the marker is the one artefact in this system whose whole job is
to be believed.

**Repair.** Resolution at a SHA on the row is now the NECESSARY condition;
`prose_marker` is recorded, reported, and never sufficient. A DEAD or
UNRESOLVED-PATH row whose line claims a pin in prose is now the loudest thing
`pin-census.py` prints:

    ⚠ prose claims a pin but the cite resolves at NEITHER end : 1
        bad.md:3  target.md:99  [DEAD]

Both directions, on a synthetic two-commit repo, at the CLI:

| input | census | migrator |
|---|---|---|
| BAD — `target.md:99`, prose-pinned, out of range at HEAD **and** at the SHA | `TRUE-PIN 0 / DEAD 1`, ⚠ line fires | `cites marked: 0`, exit **0**, file byte-identical |
| GOOD — same row, `renamed-away.md:15`, resolves at the SHA | `TRUE-PIN 1 / DEAD 0`, no ⚠ | marked, exit **0**, line gains the marker — literal form in the fence below |

```text
pinned `renamed-away.md:15` pin:`2b653449`
```

The corpus count does not move: all 5 classifier TRUE-PINs already resolved at a
row SHA, so **TRUE-PIN stays 5 before and after the D2 repair**. The defect was
latent in the corpus and live in the tool.

### 4c. D3 — the homonym test encoded this lane's own scope

`test_marker_is_not_yet_a_homonym_in_this_repo` grepped the real repo and then
subtracted an allow-list of the directories this lane happened to be piloting
in (`_orchestration/`, `manuscript/ave-kb/tools/`). It therefore fails the first
time R2's actual purpose happens — a corpus-wide sweep, or an author
hand-writing a legitimate pin in a KB leaf. A test that breaks when the thing it
guards succeeds is not a guard.

Replaced with tests of the PROPERTY:

- the marker grammar, both directions, 11 cases — 7-hex floor and 40-hex ceiling
  accepted, 6-hex / 41-hex / uppercase / non-hex / missing-backticks /
  missing-colon rejected, and a bare backticked SHA explicitly NOT the marker
  (that is the heritage rule);
- CONVENTIONS' scope rule, directly: on a row carrying two cites and one marker,
  the cite to the marker's left is bound and the other is not;
- an author's hand-written marker in a KB leaf the migration has never touched
  is honoured — classified as already-marked and left byte-identical.

The thing the old test was actually asserting — *0 prior corpus hits* — is a
dated measurement, not an invariant. It lives in §1 and in CONVENTIONS.md, where
a measurement belongs.

## 5. The migration — done, and it is FOUR cites

Not a pilot. The census in §2 is corpus-wide and §4/§4e read its whole TRUE-PIN
population by hand, so there is nothing left to scale up to. **All four
hand-confirmed cites are marked; the one non-pin got a path repair.**

```text
_orchestration/2026-06-16_standing-decisions-audit-lane.md:123
  `stage15_layer_b_coupled_stability.py:58` pin:`b2de04fc`      (2026-09-07)

_orchestration/experimental/a1-hopf/exp-a1-hopf-repo-audit.md:417
  `_orchestration/exp-a1-hopf.md:50-57` pin:`6621dae`           (2026-09-07)

manuscript/ave-kb/claim-quality-closure-roadmap.md:87
  `closure-roadmap.md:80` pin:`4457d3e`                         (2026-09-12)

manuscript/ave-kb/claim-quality-closure-roadmap.md:89
  `closure-roadmap.md:81` pin:`5f926ad`   (:80 -> :81 repaired) (2026-09-12)
```

Corpus-wide, before → after (base `5a36cea5` → migration commit; measured with
this docket excluded, see the note below):

| corpus | before | after |
|---|---:|---:|
| line-cites on SHA-bearing lines | 525 | **525** |
| LIVE | 480 | 480 |
| TRUE-PIN | 5 | 5 |
| DEAD | 0 | 0 |
| UNRESOLVED-PATH | 34 | 34 |
| SKIPPED-SHAPE | 6 | 6 |
| `` pin:`sha` `` markers in prose | 0 | **2** |
| cites bound by a marker | 0 | **2** |

The population does **not** shrink, and that is the point of the token choice.
Under the retracted `@<sha>` spelling the same two cites took the count 525 →
523 and their TRUE-PIN count 5 → 3, because a marked cite stopped matching the
cite grammar. Here they stay classified, stay countable, and now carry a
declaration a checker can read.

Idempotent on the live corpus as well as in the fixtures: a second `--apply`
reports `already marked: 2`, rewrites 0 files and changes no bytes.

**The 480 LIVE are deliberately NOT swept.** They need no marker. They are
ordinary cites that merely share a row with somebody else's provenance SHA, and
they simply stop being exempted when the heritage switch flips (§3).

> **Two measurement caveats, both learned the hard way here.**
> (a) The line-cite pass walks the FILESYSTEM, so it counts untracked files. A
> `pytest` run leaves `.pytest_cache/README.md` in the repo root and the file
> count moves 2226 → 2227. Measure in a pristine worktree with no cache.
> (b) **This docket is itself part of the corpus.** Its §4 table quotes cites on
> SHA-bearing lines, so re-running the census at this branch's tip reads higher
> than the table above (539 / 484 / 12). The migration numbers are quoted with
> this file excluded; the difference is entirely this entry's own worked
> examples.

## 6. Refusals, by construction

`migrate-pin-markers.py` will not machine-edit a byte-frozen document. Any
candidate in a `*prereg-FROZEN*` file, a `research/**/*prereg*.md`, or a
`research/**/*[-_]result.md` is listed for a human and the run exits **2**, so
"refused" cannot be mistaken for "nothing to do". Proven both directions on
synthetic repos: exit 2 with the file byte-identical on the frozen path, exit 0
with the cite marked on byte-identical content at an ordinary path.

## 7. Open for Grant

> **Items 1 and 2 are DISCHARGED as of 2026-09-12** and are struck below rather
> than deleted. Items 3 and 5 remain open. Item 4 was actioned.

1. ~~**Re-key now.**~~ **DONE** — §3b. Exemption OFF, zero cites newly gate.
2. ~~**Three cites want a PATH REPAIR, not a marker.**~~ **CORRECTED and DONE** —
   §4d/§4e. It was ONE path repair (#5), not three; #3 and #4 were TRUE PINs
   that a head-of-row read mistook for contradictions, and #4 additionally
   needed a one-line pointer repair. All four marks are placed.
3. **STILL OPEN — prose-declared pins that still resolve, 28 of the ~480 LIVE.**
   An author wrote "as shipped at", the cite resolves anyway, so it is LIVE and
   the migrator leaves it. Under the now-live marker-only gate these are checked
   and pass. Confirm that is the wanted posture rather than marking them for
   intent.
4. **`CONVENTIONS.md` §"Author-declared pin marker" must not be marked
   superseded.** It is the token — and it was not: the 2026-09-12 edit is
   additive, retiring the *heritage heuristic* section while preserving its
   description verbatim as a blockquoted historical record. Its "Grandfathering"
   paragraph still quotes R2's KB-scoped **96 at `d5a1b06b`**; §2 here
   re-measures that as **525 corpus-wide / 156 KB-only at `5a36cea5`**. That
   stale figure is **still open** for whoever next touches the section.
5. **★ NEW, and the bigger number — CONTENT drift under a clean gate.** §3b:
   ~15.6% of LIVE cites (Wilson 95% CI [7.7%, 28.8%]) point at a line that no
   longer says what the citing sentence says it says, with a zero-judgment floor
   of 24 cites resolving to a literally empty line and 52 landing on a line
   whose banner now reads DEMOTED / RETRACTED / CONTESTED. Three sampled
   instances are live claims on main that their own targets contradict. The
   line-existence gate cannot see any of this and the flip does not change it.
   Decide whether `verify-anchor-content.py` gets a scoped content pass; the 24
   blank-line cites are a same-day, zero-judgment cleanup list.
