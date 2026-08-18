# AGENTS.md — pointer

This is **AVE-Core**: the AVE (Applied Vacuum Engineering) engine + manuscript + knowledge-base repo.

Agent orientation is not maintained here. Read, in this order:

1. **[`CLAUDE.md`](CLAUDE.md)** (repo root) — the canonical agent orientation: repo layout, branching + merge-authorization rules, pre-commit discipline, standing physics/epistemology rules. **Read this first.**
2. **[`manuscript/ave-kb/CLAUDE.md`](manuscript/ave-kb/CLAUDE.md)** — required before any knowledge-base work: the cross-cutting invariants (`INVARIANT-*`) every KB leaf must respect.
3. **[`src/ave/AGENTS.md`](src/ave/AGENTS.md)** — engine-scope guide: what an agent must know before modifying the numerical code (documentation canonicality, constants provenance).

> **Provenance note (2026-08-17).** This file previously held ~11 KB of *atopile* PCB-DSL
> template text (the `ato` declarative electronics language), carried in unmodified by the
> 2026-04-13 initial-release commit `de9d2293`. It described a toolchain this repo does not
> use and was never AVE content. Removed under Wave 1 of the 2026-08-17 repo-cleanup
> epic (PR #977). No AVE document cited it.
