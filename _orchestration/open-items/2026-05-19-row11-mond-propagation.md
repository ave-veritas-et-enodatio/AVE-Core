---
id: row11-mond-propagation
title: A RESOLVED stamp asserts its own propagation, and the propagation never happened (Row 11 MOND)
status: OPEN
owner: unassigned
opened: 2026-05-19
source: manuscript/ave-kb/common/universal-saturation-kernel-catalog.md
anchor: "canonical leaf updated to SYM in this round"
---

**The cheapest fix on the board, and the most alarming shape.**

`universal-saturation-kernel-catalog.md:51` records the adjudication and then asserts its own
downstream propagation: *"adjudicated SYM … (catalog row wins over prior ASYM-N(μ) classification
at `saturated-lattice-mutual-inductance.md`; **canonical leaf updated to SYM in this round**)"* —
repeated at `:102`.

**The leaf was never updated.** `saturated-lattice-mutual-inductance.md:8` still reads *"the galactic
mutual-inductance saturation is the **MOND-ASYM-N row**"*, and its git log carries **no
classification commit at all** (last content touches `ccb0dec6` 2026-05-24 hygiene, `37bf84ca`
2026-05-23, `7312b11f` 2026-05-21).

So a reader following the catalog's own pointer lands on the opposite classification. This is not
"unverified whether resolved" — it is a **RESOLVED stamp that certifies work that does not exist**,
which is strictly worse than an open flag. Same class as the withdrawn claim left standing in a live
document.

Line refs in the index have also drifted: catalog `:38`→`:51`, leaf `:4`→`:8`.

Verified 2026-08-13 by sweep at `origin/main` `7d361e96`.
