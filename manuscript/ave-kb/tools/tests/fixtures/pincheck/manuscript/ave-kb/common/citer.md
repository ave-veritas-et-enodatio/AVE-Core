[↑ Parent](index.md)

# Pin-marker fixture — ERROR SOURCE (manuscript/ave-kb/, gates)

Line numbers here are NOT asserted by the tests; every case is keyed by its
cite text. `target.md` in this fixture tree is exactly 20 lines long.

STAR — per-cite, not per-line: ledger row padding so this line has the shape of a real KB table row, which is the whole reason the line-scoped heuristic is imprecise; rows like this one routinely mix a single provenance pointer with several live derivation pointers, and a rule that keys on the row cannot tell them apart, so it switches checking off for the entire row; the marker below is attached to one cite and must therefore exempt exactly that one and leave its neighbour on the same row fully gated, which is the property this fixture exists to prove and the only thing R2 actually changes about the checker; pinned `target.md:900@aaaaaaa1` and live-and-dead `target.md:901` share this row. ledger row padding so this line has the shape of a real KB table row, which is the whole reason the line-scoped heuristic is imprecise; rows like this one routinely mix a single provenance pointer with several live derivation pointers, and a rule that keys on the row cannot tell them apart, so it switches checking off for the entire row; the marker below is attached to one cite and must therefore exempt exactly that one and leave its neighbour on the same row fully gated, which is the property this fixture exists to prove and the only thing R2 actually changes about the checker; 

HERITAGE arm — bare SHA `aaaaaaa1` on the row exempts `target.md:902` (grandfathered).
UNKNOWN pin sha — well-formed marker naming no commit: `target.md:5@ffffff09`
MALFORMED marker, too short: `target.md:903@12`
MALFORMED marker, not hex: `target.md:904@zzz`
MARKER on a line that still exists: `target.md:5@aaaaaaa1`
MARKER, link-ext form: [t](target.md):905@aaaaaaa1
MARKER, link-in form: [t](target.md:906@aaaaaaa1)
MARKER on a path since renamed away: `gone-in-a-rename.md:7@aaaaaaa1`
CONTROL, unmarked and dead: `target.md:907`
CONTROL, unmarked and live: `target.md:5`

