[↑ Parent](index.md)

# Pin-marker fixture — ERROR SOURCE (manuscript/ave-kb/, gates)

Line numbers here are NOT asserted by the tests; every case is keyed by its
cite text. `target.md` in this fixture tree is exactly 20 lines long. The SHAs
here are SYNTHETIC and this tree is not a git checkout: it exercises the
marker's GRAMMAR and BINDING with pin validation off. The object-store arm —
does the pin resolve at its own sha — is exercised against a throwaway repo the
test builds, in `test_pin_resolution_*`.

STAR — per-cite, not per-line: ledger row padding so this line has the shape of a real KB table row, which is the whole reason the line-scoped heuristic is imprecise; rows like this one routinely mix a single provenance pointer with several live derivation pointers, and a rule that keys on the row cannot tell them apart, so it switches checking off for the entire row; the marker below is attached to one cite and must therefore exempt exactly that one and leave its neighbour on the same row fully gated, which is the property this fixture exists to prove and the only thing R2 actually changes about the checker; pinned `target.md:900` pin:`aaaaaaa1` and live-and-dead `target.md:901` share this row. ledger row padding so this line has the shape of a real KB table row, which is the whole reason the line-scoped heuristic is imprecise; rows like this one routinely mix a single provenance pointer with several live derivation pointers, and a rule that keys on the row cannot tell them apart, so it switches checking off for the entire row; the marker below is attached to one cite and must therefore exempt exactly that one and leave its neighbour on the same row fully gated, which is the property this fixture exists to prove and the only thing R2 actually changes about the checker; 

HERITAGE arm — bare SHA `aaaaaaa1` on the row exempts `target.md:902` (grandfathered).
MALFORMED, not hex: `target.md:903` pin:`zzz`
MALFORMED, too short: `target.md:904` pin:`12`
MALFORMED, unbackticked: `target.md:909` pin:aaaaaaa1
MALFORMED, nothing to pin (no `:NN`): `target.md` pin:`aaaaaaa1`
MARKER on a line that still exists: `target.md:5` pin:`aaaaaaa1`
MARKER, link-ext form: [t](target.md):905 pin:`aaaaaaa1`
MARKER, link-in form: [t](target.md:906) pin:`aaaaaaa1`
MARKER on a path since renamed away: `gone-in-a-rename.md:7` pin:`aaaaaaa1`
ORPHAN, must FIRE — the marker missed the cite on its own row, so it binds to
nothing and the cite stays checked: `target.md:910` — as shipped pin:`aaaaaaa3`
DOC PROSE, must NOT fire — writing ABOUT the token, on a row carrying no
location cite at all, is documentation and not a mis-placed marker: pin:`aaaaaaa2`
CONTROL, unmarked and dead: `target.md:907`
CONTROL, unmarked and live: `target.md:5`

## Defect (1) — the marker must survive ordinary punctuation

Each of these is a live marker whose cite is dead at HEAD; every one must be
exempt, and none of them may report a malformed marker. If the token swallowed
trailing punctuation the way a glued `@<sha>` form does, these red-light
`make verify` on a legitimate pin.

- full stop: `target.md:920` pin:`aaaaaaa1`.
- comma: `target.md:921` pin:`aaaaaaa1`, and the sentence goes on
- semicolon: `target.md:922` pin:`aaaaaaa1`; and on
- close paren: (see `target.md:923` pin:`aaaaaaa1`)
- emphasis: *`target.md:924` pin:`aaaaaaa1`* and **`target.md:925` pin:`aaaaaaa1`**
- end of line, nothing after: `target.md:926` pin:`aaaaaaa1`

A table row, because the KB's rows are pipe-delimited:

| cite | note |
|---|---|
| `target.md:930` pin:`aaaaaaa1` | pinned inside a cell |
| `target.md:931` | unmarked neighbour in the same table |

> A blockquote, because walk-back records are written in them:
> per `target.md:940` pin:`aaaaaaa1` — *"the sentence that line carried then"*
