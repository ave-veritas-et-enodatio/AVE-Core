# L3 → BLR KB Migration — Execution Brief

TRANSIENT session doc. Companions: `claim-map.yaml` (which leaves / claims) and
`framing-concordance.md` (how to phrase the framing sweeps). This brief holds the
*execution discipline* — how to run each unit so plans survive contact with the
data. Liftable for the next large-scale transformation (rest of the KB volumes;
then the Python-code migration).

## Plan against primary sources

A plan presented for approval is a commitment: "approve this and it runs to
completion." Do not present one until its load-bearing assumptions are verified
against the **primary artifact the work transforms** — the file, the `git diff`,
the claim entry, the KB-wide grep of what a change touches.

Derived / secondary sources — `claim-map.yaml` `status` and row prose,
`subtree-claims`, index files, git-log one-liners, conversation summaries, earlier
conclusions — guide exploration but are **never** the basis of a plan or an
approval request.

- **Trigger.** If you catch yourself reasoning about whether a status field /
  summary / index is stale-or-current — stop. Open the primary artifact; do not
  adjudicate staleness by inference.
- Verification precedes the approval gate; it never sits inside execution. Reads
  are cheap — an interrupted, re-planned, re-approved unit is not.
- Plan at the granularity actually verified — never a coarser batch granularity
  that assumes uniformity you have not checked.
- A genuine surprise while executing an approved plan is a *planning defect* —
  diagnose why planning missed it.

## Per-unit readiness gate

A unit (leaf port, claim retirement, …) is not "ready to plan" until, for that
unit, you have read:

1. the **source** — `git diff <ancestor>..l3/<branch> -- <path>` (the net delta);
2. the current **target** state — the BLR file as it stands now;
3. the **metadata both sides touch** — every `claim-quality.md` entry the leaf's
   frontmatter cites;
4. for any claim a change **retires or moves** — the KB-wide grep of that
   `clm-id` (frontmatter citers, Tier-2 markers, prose, cross-entry references).

Subagents do not inherit this brief — state the readiness gate inline in any
subagent prompt that scopes or plans work.
