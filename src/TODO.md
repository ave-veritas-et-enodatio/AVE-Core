# AVE Engine — Outstanding Work

> **Dated note 2026-08-17 — two dangling pointers struck; file kept as a 2026-04-13
> snapshot.** Under "Completed" below, **`src/ave/ARCHITECTURE.md`** and
> **`src/scripts/ARCHITECTURE_REVIEW.md`** do **not** exist. Both were deleted in commit
> `5016cf26` (2026-04-13, *"chore: AVE-Core post-partitioning audit and IP scrub"*) — the
> same commit that last touched this file, so the pointers have dangled since they were
> written. What survives is the other half of each pair:
> **`src/scripts/ARCHITECTURE.md`** and **`src/ave/ARCHITECTURE_REVIEW.md`**, both present.
> The "Completed" lines are left unedited (they are a correct-as-of-2026-04-13 record).
> Flagged by the 2026-08-17 repo-cleanup census, Wave 1.

## Active
- Coding consistency pass (Black formatter, uniform annotations)
- Detailed human examination and evaluation of physics engine

## Completed
- Architecture characterization: `src/ave/ARCHITECTURE.md`, `src/scripts/ARCHITECTURE.md`
- Architecture review: `src/ave/ARCHITECTURE_REVIEW.md`, `src/scripts/ARCHITECTURE_REVIEW.md`
- IP partitioning: private volumes (7–9) moved to separate repos
- Generic TopologicalOptimizer extracted to `ave/solvers/topology_optimizer.py`
