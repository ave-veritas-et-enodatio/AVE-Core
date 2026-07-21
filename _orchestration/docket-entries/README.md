# Docket entry fragments (the news-fragments convention, adopted 2026-07-21)

**Why:** every lane used to append its `### ENTRY` block to the tail of `_orchestration/2026-07-10_rulings-docket.md`. The repo's union merge driver resolves those tail-appends locally, but **GitHub's server-side merge ignores custom merge drivers**, so any two open docket-touching PRs showed CONFLICTING the moment either merged — ~15 manual union-refresh cycles in the 2026-07-20/21 window alone. Grant [sic]: "why does this keep happening? seems like you could fix this routine issue easilh with a dofferent pr process."

**The convention (for every lane from 2026-07-21 on):**
- Write your docket entry as **one new file in this directory**: `YYYY-MM-DD-<lane-slug>.md`, containing your `### ENTRY <YYYY-MM-DD>-<lane-slug>` block (same content-keyed format as before).
- One lane, one file. Never edit another lane's fragment (Rule 12 corrections = a dated `-correction` suffix file referencing the original).
- The monolithic docket (`2026-07-10_rulings-docket.md`) is **frozen at its 2026-07-21 tail** — no new appends; it remains the historical record.
- `verify-docket-keys.py` scans BOTH the monolith and this directory for key uniqueness.
- **Generated-index rule** (the other conflict source): `manuscript/ave-kb/.index/*` is never text-merged — on any merge conflict, take either side and run `make refresh-kb-metadata` to regenerate from the merged sources.

Separate files per lane = zero textual overlap = no server-side conflicts, ever.
