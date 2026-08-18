---
id: repo-weight-policy
title: 162 MB in 8 tracked files >10 MB (~24% of pack) + 29 MB build outputs under src/ — LFS, prune, or accept?
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-17
source: _orchestration/2026-08-17_repo-cleanup-epic.md
anchor: "162 MB in 8 files >10 MB"
---

2026-08-17 census, HEAD `36ce03b9`, pack ≈ 684 MB:

- **8 tracked files exceed 10 MB (162 MB total):** `data/pantheon_plus/…STAT+SYS.cov`
  32 MB, two `assets/3d_models/*.stl` at ~30 MB each, plus five more. Empirical anchors
  and render assets — likely keep-but-relocate candidates (LFS or a fetch script), not
  deletions.
- **131 binary build outputs tracked under `src/`** (~29 MB): `.npz/.png/.gif/.pdf`
  across 8 output directories (e.g. `vol_6…/figures` 38 files, `vol_1…/_output` 33).
  These are driver-regenerable renders — the class the formatting epic's P2 already
  labels DELETE-CANDIDATE for regenerables.
- Untracked-but-local bloat noted for completeness (not repo weight): `data/planck_pr3/`
  2.1 GB, `.claude/worktrees/coldq-pole` 684 MB living inside the repo's `.claude/`.

**The decision:** (a) adopt git-LFS for >10 MB empirical/asset files, (b) prune tracked
regenerable outputs under `src/` (keep the drivers, drop their renders), (c) accept
current weight and close. (a)+(b) roughly halves clone weight; (b) alone is the cheap
half. Any prune lands only after the P2 regenerability rule is confirmed against each
directory — a render that is NOT regenerable is a GRANT-CALL per that batch's own scope
line.
