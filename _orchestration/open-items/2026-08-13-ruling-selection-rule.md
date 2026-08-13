---
id: ruling-selection-rule
title: Docket ruling records should declare their number in one convention, not two
status: OPEN
owner: unassigned
opened: 2026-08-13
source: _orchestration/docket-entries/README.md
anchor: "Docket entry fragments (the news-fragments convention, adopted 2026-07-21)"
---

★ **REWRITTEN 2026-08-13 — the original framing was WRONG and is withdrawn.** It claimed
the selection rule was undecidable and that "from the text alone the two are not separable."
A cold audit grepped the corpus's own `## R<N> — ` heading convention and the answer fell out
immediately: **R1–R53, gapless, no duplicates, no file claiming a number another file claims.**
Nobody had looked. The board's derivation now takes the union of the filename and heading
conventions and reports the real debt.

**What actually remains.** Two conventions coexist, and one of them is invisible from the
filename:

| convention | example | visible in `ls`? |
|---|---|---|
| number in the filename | `2026-08-12-ruling-r52-k2g-operating-point.md` | yes |
| number only in a `## R<N> — ` heading | `2026-08-06-rulings-final-batch.md` (carries R11–R17) | **no** |

The union works, so nothing is broken. But a tool that must read every docket body to learn
which rulings exist is a tool that fails quietly the moment the heading style shifts — and the
filename-only derivation that shipped on 2026-08-13 under-reported the debt by ~1.8× for
exactly that reason.

**What would close this.** A single declared convention — number in the filename, or a
frontmatter field naming the rulings a file *records* as opposed to *cites*. Same shape as the
key uniqueness `verify-docket-keys.py` already enforces.

**Related:** `key-namespace-collision` — four distinct decisions all named `D1`. Both are
registry problems, not document-discipline problems.
