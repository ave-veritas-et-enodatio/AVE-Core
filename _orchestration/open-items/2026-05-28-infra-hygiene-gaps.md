---
id: infra-hygiene-gaps
title: Two infra gaps still open — no conflict-marker hook, and no structural worktree-leak fix
status: OPEN
owner: unassigned
opened: 2026-05-28
source: CLAUDE.md
anchor: "Structural fix for the same issue"
---

**1. Conflict-marker pre-commit hook — absent.** Verified by three independent methods, all
negative: (a) `.pre-commit-config.yaml` carries isort/black/flake8 only, no `check-merge-conflict`;
(b) `.git/hooks/pre-commit` is the dual-context `make verify` gate with no marker scan; (c) a
tree-wide search for a literal conflict-marker pattern across `src/`, `scripts/`,
`manuscript/ave-kb/tools/`, `Makefile` returns zero. `.github/workflows/verify.yml` runs only
`make verify` + `make test`. **~15 minutes of work** against a recorded commit-slip.

**2. Worktree-spawn branch-state leak — still a convention, not a structure.** `CLAUDE.md:107` calls
worktree isolation *"the structural fix"*, but `.claude/hooks/` holds only `precommit-verify.sh`,
`skill-trigger-detect.sh`, `validation-table-watchdog.sh` — **no pre-Write path guard.** The leak
recurred 3× during Vol-9 Wave-1 sessions *after* `ave-worktree-paths` v1.0 landed, which is what
"convention did not hold" looks like.

Verified 2026-08-13 by sweep at `origin/main` `7d361e96`.
