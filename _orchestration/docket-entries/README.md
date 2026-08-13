# Docket entry fragments (the news-fragments convention, adopted 2026-07-21)

**Why:** every lane used to append its `### ENTRY` block to the tail of `_orchestration/2026-07-10_rulings-docket.md`. The repo's union merge driver resolves those tail-appends locally, but **GitHub's server-side merge ignores `.gitattributes` merge drivers (including the built-in `union`)**, so any two open docket-touching PRs showed CONFLICTING the moment either merged — ~15 manual union-refresh cycles in the 2026-07-20/21 window alone. Grant [sic]: "why does this keep happening? seems like you could fix this routine issue easilh with a dofferent pr process."

**The convention (for every lane from 2026-07-21 on):**
- Write your docket entry as **one new file in this directory**: `YYYY-MM-DD-<lane-slug>.md`, containing your `### ENTRY <YYYY-MM-DD>-<lane-slug>` block (same content-keyed format as before).
- One lane, one file. Never edit another lane's fragment (Rule 12 corrections = a dated `-correction` suffix file referencing the original).
- The monolithic docket (`2026-07-10_rulings-docket.md`) is **frozen at its 2026-07-21 tail** — no new appends; it remains the historical record.
- `verify-docket-keys.py` scans BOTH the monolith and this directory for key uniqueness.
- **Generated-index rule** (the other conflict source): `manuscript/ave-kb/.index/*` is never text-merged — on any merge conflict, take either side and run `make refresh-kb-metadata` to regenerate from the merged sources.

Separate files per lane = zero textual overlap = no server-side conflicts **for the docket**. This convention retires the docket instance of the union-append conflict class, not the whole class.

**Remaining union-append targets (2026-07-21 audit, per `.gitattributes`):**
- `research/2026-07-16_f6-bath-meter_CHARTER.md` (`merge=union`) — same conflict class, last append 2026-07-19; unmigrated.
- `research/2026-07-17_regime-iv-dissipation-audit.md` (`merge=union`) — same conflict class, last append 2026-07-19; unmigrated.
- Both look to be winding-down append batteries; migrate to a per-lane fragment dir if either goes hot again.

> ★**CORRECTION 2026-08-13 — the hazard described in the next paragraph does not exist.**
> The `merge=ours` *silent-drop* mechanism was withdrawn in-corpus on 2026-08-03 at
> [`../2026-07-20_pending-rulings-and-frontier-queue.md`](../2026-07-20_pending-rulings-and-frontier-queue.md)`:170-181`:
> `.gitattributes:9` does set `*.md merge=ours`, but the attribute is **inert** with no
> `merge.ours.driver` configured (`git config --get-regexp '^merge\.ours\.'` returns empty,
> local and `--global`), so git falls back to the default 3-way text merge. A first-party
> receipt shows a real collision on a `.md` file surfacing as a **loud conflict**.
> The paragraph is preserved unrewritten per Rule 12 — **but do not cite it.** It misled a
> reader as recently as 2026-08-13. The queue it names is now frozen; open items live in
> [`../open-items/`](../open-items/), moved for machine-readability, not for safety.

**Distinct hazard, on record (needs its own treatment, not this convention):** `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md` falls under the blanket `*.md merge=ours` and is the highest-frequency shared-edit target (mid-file status-flips + tail appends). Under `merge=ours` a concurrent lane's discharge can be **silently dropped** (data loss, not a visible conflict). The fragment tool is the wrong shape for its status-flip pattern — routed as a separate follow-on.
