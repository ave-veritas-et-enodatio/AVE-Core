---
id: newcite-ratchet-split-brain
title: check_new_cites mixes committed line-sets with working-tree content — green receipts describing neither state
status: OPEN
owner: unassigned
opened: 2026-08-19
source: manuscript/ave-kb/tools/verify-anchor-content.py
anchor: "Uses `git diff --unified=0 <base>...HEAD`, i.e. the merge-base three-dot"
---

Found 2026-08-19 while root-causing a false-green local ratchet run on the Wave-2 PR-1
branch (recorded at PR #982's root-cause comment). `check_new_cites` derives its ADDED
line-set from commits (`git diff base...HEAD`) but reads file CONTENT from the working
tree (`path.read_text()`). Two false-green modes follow, both hit in one session:

1. **Pre-commit trivially green** — HEAD == base ⇒ empty diff ⇒ zero added lines ⇒ OK,
   regardless of what the working tree contains.
2. **Post-edit-pre-commit green** — the diff sees HEAD's (old) line as added, but the
   excerpt test reads the (fixed) disk file ⇒ OK for a commit that would fail in CI.

The only valid local receipt today is running the gate in a CLEAN checkout of the
committed tip. Candidate closures, un-endorsed: (a) read content from HEAD blobs
(`git show HEAD:<path>`) so both halves describe the same state; (b) refuse to run
with a dirty working tree (fail-loud, cheapest); (c) document the constraint in the
tool docstring + Makefile help and keep behavior. (a) is the correct fix; (b) is one
guard clause; (c) is a warning label on a split-brain gate.

Low urgency: CI is unaffected (clean checkouts by construction); the defect only
manufactures false LOCAL receipts — which is exactly how it survived unnoticed.
