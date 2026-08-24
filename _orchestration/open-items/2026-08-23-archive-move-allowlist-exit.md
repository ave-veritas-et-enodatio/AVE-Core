---
id: archive-move-allowlist-exit
title: Archiving a script is a silent exit from the import-smoke known-broken allowlists, and the liveness guard mis-describes it
status: OPEN
owner: claude
opened: 2026-08-23
source: src/tests/test_scripts_import_smoke.py
anchor: "Allowlisted script-tree import(s) no longer generate a violation"
---

Minted from PR #996's blind-audit advisory (finding 2.7). The known-broken dicts' liveness
guards hard-fail on stale entries with the message "their bug was fixed upstream; remove the
now-stale ... entr(ies)". That description is correct for the repair path but WRONG for the
archive path: moving a broken script under `src/scripts/_archive/` removes it from the walk,
which fires the same guard with the same "fixed upstream" text — nothing was fixed; the file
left the surveyed tree. The #996 retirement handled this honestly (a dated note in the dict
records where the entries went), but the ROUTE remains: any future archive-move silently
discharges allowlist entries under a message that mis-attributes why.

Candidate dispositions (any lane may take this; no Grant ruling required):
(a) guard message amended to name both discharge paths (fixed upstream OR left the walk);
(b) additionally, the guard could require a dated tombstone comment in the dict when the
discharge path is an archive-move (pattern already set by #996's note).
