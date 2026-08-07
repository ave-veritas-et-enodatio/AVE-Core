# Spec — signed-Γ census treatment (i): the tag edit (R22)

### ENTRY 2026-08-07-gamma-tag-spec

**Class:** records / spec. Mints no `clm-`/`def-`, moves no solidity, adjudicates no channel, and
**executes no edit**. **Authority:** R22
(`_orchestration/docket-entries/2026-08-07-rulings-f3-f5-f1.md`:35–41), Grant verbatim *"let's route
back."* — the R1 treatment-(i) tag edit *"does not execute until a repo-resident spec exists"*.

**Why this file exists.** R1 routed execution to the doc lane as *"(their proposal)"*, and that
proposal rode a session-relayed report that never landed as a tracked artifact. PR #915 delivered
the census half and recorded the tag half as blocked on exactly this gap. This fragment closes it:
after it merges, the tag edit runs **against the frozen text below and nothing else**.

---

## 1. Definition — what "actionable" means

> **A location in the printed manuscript where a signed value is asserted for Γ without declaring
> which channel the Γ belongs to.**

Operationally, all four conditions:

| # | condition | why it is in the definition |
|---|---|---|
| 1 | file class is `print_tex` (`manuscript/**/*.tex`) | the printed manuscript is the surface where an undeclared sign is read as canon; KB leaves are handled by their own registers |
| 2 | the line is **rendered** — not a `%`-comment | a commented draft line asserts nothing |
| 3 | channel is **`unspecified`** — the Γ token carries no subscript | a Γ that already names its channel is declared, and needs no tag |
| 4 | sign is **`-1` or `+1`** — a value is asserted | a Γ merely *mentioned* asserts nothing to declare |

**What is deliberately excluded, and on whose authority.** Sites that already carry a channel
subscript are **not** actionable — they are declared. Sites with no asserted sign are **not**
actionable. And the ~2,332 unspecified-channel sites that assert no value are **not** to be
mass-subscripted: R1 rejects that as treatment (ii) because `wall-taxonomy.md` §10.1 records the
`Γ_shear` sign as **unresolved**, so assigning channels wholesale would hand-set an attribution
canon has not adjudicated.

## 2. The census, SHA-pinned

Measured **at `origin/main` = `91a910f8`**, in a worktree at that commit, with
`src/scripts/signed_gamma_census.py`. Universe declared knob-by-knob before the number:

```
roots=manuscript  exts=.tex,.md  gamma=all  relation=any  gap=adjacent-nested
signs=any  minus=unicode  glue=math  comments=include  magnitude_guard=True
```

Then the §1 filter (print_tex ∧ rendered ∧ unspecified ∧ sign ∈ {−1,+1}).

| quantity | value |
|---|---|
| **ACTIONABLE (the tag set)** | **238 sites / 63 files** |
| corpus total in the universe | 2887 sites / 2146 lines / 356 files |
| unspecified-channel (the judgment class, NOT actionable) | 2332 sites |
| **two-method self-check** | **AGREE** — method A `rglob`+`re`, method B subprocess `grep -rInE` on the byte-identical pattern; A = B = 2146 lines, symmetric difference empty |

**Unchanged from `d129e7ac`** (238/63 at both), which is a stability datum, not a coincidence: the
intervening merges touched drivers and records, not print Γ text.

> ⚑ **Census-at-SHA rule, self-imposed after a measured failure.** This census was run **at the
> SHA**, in a detached worktree — not against a working tree. PR #915's pre-bond census certified
> 52/31 under a "two methods agree" headline and was wrong: both methods read one tree, and that
> tree was the branch tip carrying the lane's own edit. Two scan ENGINES over one TREE cross-check
> the engines, not the tree. Any re-derivation of the number above must re-run at its SHA.

**Re-derivation, one line:**
`python3 src/scripts/signed_gamma_census.py --roots manuscript --ext .tex,.md --gamma-form all --relation any --signs any --gap adjacent-nested --comments include --sites --json out.json`
then filter `file_class == print_tex ∧ rendered ∧ channel == unspecified ∧ sign ∈ {-1,+1}`.

## 3. The tag — format

The tag **declares that a declaration is owed**. It does **not** assign a channel.

```latex
\gammaundeclared
```

A single argument-free macro placed immediately after the asserting expression:

```latex
... total reflection ($\Gamma = -1$\gammaundeclared) at the wall ...
```

**Definition** (to be added to `manuscript/common/` macros in the executing PR, not here):

```latex
% Marks a signed Gamma asserted without a declared channel. Renders nothing in
% the PDF; exists so the undeclared-channel population is machine-countable and
% can be discharged per wall-taxonomy Sec.10 item 3.
\newcommand{\gammaundeclared}{}
```

Four properties, each load-bearing:

1. **Renders as nothing.** The tag changes no printed character. It is a census marker, not
   reader-facing text, so no print claim gains or loses content.
2. **Argument-free.** A tag taking a channel argument would invite the hand-set attribution R1
   rejected. There is no slot to guess into.
3. **Machine-countable.** `git grep -c '\\gammaundeclared'` is the population; progress is
   measurable and the set can be re-derived at any SHA.
4. **Coinage verified.** `\gammaundeclared` has **0 prior corpus hits** at `91a910f8`, checked two
   methods (`git grep -F` and an independent `grep -r` over `*.tex`/`*.md`) per the
   grep-completeness rule.

## 4. Site-selection rule for the executing pass

1. **Re-derive first.** Re-run §2 at the execution SHA and pin it in the PR body. Do not carry the
   238/63 figure forward as truth — it is a measurement, and the convention it demonstrates is that
   measurements are re-taken.
2. **Tag exactly the §1 set.** One tag per asserting expression, immediately after it.
3. **Line-count-neutral.** Same-line insertion only. Print chapters are cite targets; an inserted
   line manufactures anchor drift (the FLAG-C class, and #915's own F6).
4. **Do not touch, and say so per class:** any site already carrying a channel subscript; any
   `%`-comment line; any frozen or preserved-historical block; any line inside quoted ruled text.
5. **Batch by file**, one commit per volume, with `make verify` green per commit.
6. **A site whose sentence becomes false or misleading under the tag is a FINDING**, surfaced in the
   PR body — not a fix, and not a channel guess.

## 5. What the tag does NOT license

It adjudicates no channel, prefers no density branch, and touches the `Γ_shear` sign nowhere — that
sign is **unresolved** in canon (`wall-taxonomy.md` §10.1) and its authority is a certified
instrument's branch-derived wall row (§10 item 3), never a doc-lane pass. Discharging a tag means
*supplying a declaration from that authority*, which is a separate future workstream. This spec
marks the debt; it does not pay it.
