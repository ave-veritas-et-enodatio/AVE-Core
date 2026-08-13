---
id: sibling-repo-uncommitted
title: Ten uncommitted files sitting in two sibling repos, unchanged for three months
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-05-20
source: _orchestration/index.md
anchor: "**AVE-Metamaterials SOLAR_PANEL_INITIATIVE WIP**"
---

Byte-for-byte the same working-tree state as the 2026-05-20 baseline. Commit, stash, or discard —
Grant's call, per cross-repo discipline (do NOT resolve these from an AVE-Core session).

- **AVE-Metamaterials** — `git status --porcelain` returns **exactly 8**, including
  `?? .agents/handoffs/SOLAR_PANEL_INITIATIVE.md` and `?? scripts/simulate_pv_lc_cavity.py`.
- **AVE-QED** — **exactly 2**: `M manuscript/vol_qed_replacement/chapters/09_anomalous_moment.tex`
  and `?? manuscript/vol_qed_replacement/main.pdf`.

*(The third repo in the original trio is clear: AVE-Protein's 51 uncommitted files no longer exist —
the work landed via `6ccd212` on 2026-05-22 and `git status` now shows 2 untracked housekeeping
entries. Verified and closed by the same sweep.)*

Verified 2026-08-13 by sweep.
