---
id: merge-ours-corpus-sweep
title: The merge=ours corpus-wide correction sweep — ROUTED to Grant, and half-executed without his call
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-07-20
source: _orchestration/2026-07-20_pending-rulings-and-frontier-queue.md
anchor: "★**ROUTED, NOT FIXED HERE (Grant-gated, corpus-wide):**"
---

**The routing, verbatim from the source:** the withdrawn `merge=ours` silent-drop belief
*"pre-exists on `main` at **this file's own `:28` preamble note** and at
**`_orchestration/docket-entries/README.md`:19**. Those are not this lane's text and are **not**
touched here. A corpus-wide `merge=ours` correction sweep … needs a Grant call before anyone
edits process docs on the strength of it."*

**★ GATE BREACH, on record (2026-08-13, orchestrator).** PR #965 added a dated `★CORRECTION`
block to **one of the two named sites** (`docket-entries/README.md`) without the Grant call the
routing requires. The corpus is now **half-swept**: the queue's own `:28` preamble still asserts
the withdrawn mechanism. The edit's *content* is true and independently verified — `.gitattributes`
sets `*.md merge=ours`, `git config --get-regexp '^merge\.ours\.'` returns empty both local and
`--global`, and a scratch-repo reproduction produced a loud `CONFLICT (content)` with `<<<<<<<`
markers — and it is additive under Rule 12. This is a **discipline** finding, not a correctness
one. Recorded rather than quietly reverted, per flag-don't-fix.

**The decision owed:** authorize (or decline) the corpus-wide sweep, and rule on whether the
already-landed half stands, is reverted, or is completed.
