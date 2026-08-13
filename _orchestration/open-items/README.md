# Open items — one file per open decision

**This directory is the machine-readable home for everything the program is waiting on.**
`generate_board.py` reads it, so anything landed here appears on `_orchestration/BOARD.md`
without anyone hand-updating a status list.

## Why one file per item

The same reason the docket moved to `docket-entries/` on 2026-07-21: **one lane, one file,
zero textual overlap.** A status list that every lane edits mid-file is a permanent collision
target. Separate files do not collide at all — there is nothing to resolve.

> **A hazard note that is NOT the reason.** The `merge=ours` "silent drop" story attached to
> the old queue was **withdrawn in-corpus on 2026-08-03**
> (`../2026-07-20_pending-rulings-and-frontier-queue.md:170-181`): `.gitattributes:9` does set
> `*.md merge=ours`, but the attribute is inert with no `merge.ours.driver` configured, and a
> first-party receipt shows real collisions surfacing as loud conflicts. Data loss was never
> the problem. **Machine-readability is** — and hand-maintained state going stale is.

## The schema

Every file is `<status-year>-<short-slug>.md` with this frontmatter. The generator validates
it and **fails loud** on a bad field rather than skipping the file — a silently-skipped open
item is exactly the failure this directory exists to prevent.

```yaml
---
id: sector-of-storage           # unique, kebab-case, stable (never renumber)
title: One line, plain English  # what appears on the board
status: OPEN-IN-WALK            # see the table below
owner: grant                    # grant | lane | unassigned
opened: 2026-07-26              # ISO date the item became open
source: path/to/file.md:30      # where the full record lives; the fragment is a POINTER
---
```

| `status` | meaning |
|---|---|
| `ROUTED-TO-GRANT` | needs Grant's word; nothing fires without it |
| `OPEN-IN-WALK` | Grant is actively walking it; not ruled |
| `OPEN` | open, no owner assigned yet |
| `REGISTERED` | recorded so the arc resumes correctly; not scoped, not dispatched |
| `QUEUED` | authorized in principle, waiting its turn |
| `PARKED` | deliberately held; needs an explicit word to unpark |

## The rules

1. **The fragment is a pointer, not the record.** Full evidence, receipts, and options stay
   where they already live. Duplicating them here creates a second thing to keep in sync,
   which is the disease.
2. **Closing an item = deleting its file**, in the same PR that lands the ruling. Git holds
   the history; the docket holds the ruling. A directory of closed items is a stale list
   wearing a fresh name.
3. **Never edit another lane's fragment.** Rule 12 corrections get a dated `-correction`
   suffix file that references the original.
4. **If it isn't here, it isn't on the board.** That is the forcing function: "the board
   should also show X" becomes a small file, not a hand-maintained paragraph.
