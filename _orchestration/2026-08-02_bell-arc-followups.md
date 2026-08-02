# 2026-08-02 — Bell-provenance arc follow-ups (citation-hygiene queue)

**Provenance:** the 2026-08-02 quote-provenance arc — PR **#824** (merged
`605a6ca8`, tag `audit/2026-08-02_bell-quote-provenance`) retracted a
misattributed Bell quotation in `manuscript/ave-kb/common/the-abandoned-interior.md`;
PR **#828** (merged `ac165cf2`, tag `audit/2026-08-02_bib-stamp-reconciliation`)
reconciled that leaf's citation stamps with `manuscript/bibliography.bib`
reality and minted `michelson1887ether`. Both PRs surfaced follow-ups that were
flagged-not-fixed (per lane discipline); this brief is their durable home.
**Court: auditor lane; item F1's gate-creation decision is Grant-gated.**

## Open items

### F1 — no gate binds `\cite{}` keys to `bibliography.bib` (ROOT CAUSE — highest value)

`grep` of `manuscript/ave-kb/tools/` and `tools/` finds **zero readers** of
`bibliography.bib`. Consequence, demonstrated by this arc: `larmor1897dynamical`,
`larmor1900aether`, and `bell1976how` were minted in commit `60a04b96` yet the
consuming leaf's editorial stamps still said "not yet minted" — the drift ran
unnoticed until an external verification pass tripped over it, and the #828 fix
itself is unprotected against recurrence. Loud-on-drift is the corpus's own
INVARIANT-S11 rationale; citations are currently its blind spot.

**Proposed shape (~20-line script + Make target):** collect
`\\cite\{[^}]*\}` keys across `manuscript/**/*.tex` and `manuscript/ave-kb/**/*.md`,
require every key to resolve to an `@…{key,` entry in `bibliography.bib`;
optionally warn on never-cited entries. Wire into `make verify` alongside
`verify-kb-metadata` / `verify-md-links`.

**Gate-creation is HARD-GATED on Grant** (standing skills/infra discipline) —
this brief records the case; it does not build the gate.

### F2 — `historical-precedents.md:30` Michelson–Morley mention undated + uncited

The Root-2 line "the aether was refuted (Michelson–Morley)" carries no date and
no `\cite{}`, and MM is absent from that leaf's `:55` public-citation Fact
enumeration. `michelson1887ether` now exists (minted in #828) — the fix is a
one-line cite + adding MM to the `:55` enumeration, honoring the leaf's
Rule-12 body-preservation (the `:30` line sits in the preserved body; the cite
lands per the leaf's own dated-note pattern). Note the companion leaf's
read-with-care framing (`the-abandoned-interior.md` §"Michelson–Morley (1887),
read twice") when wording any touch.

### F3 — Abraham 1902/03 citation debt

`the-abandoned-interior.md` leans on "Abraham's rigid electron 1902" at `:24`,
`:56`, and the `:225` Fact enumeration with **no public anchor**; #828's
reconciled stamps now name the Abraham–Lorentz program as the sole remaining
editorial-stamp-only anchor (deliberate — page data was not verified to the
house bar). Candidate entry: Abraham, "Prinzipien der Dynamik des Elektrons,"
*Annalen der Physik* 315(1), 105–179 (1903) — **verify volume/pages against a
primary scan before minting** (secondary sources also cite a 1902 Göttinger
Nachrichten precursor; pick the anchor deliberately).

## Closed context (for the record)

- Bell misattribution: retracted at the leaf with two verbatim Bell anchors
  substituted (p. 77 "Lorentzian pedagogy"; pp. 67–68 thread-experiment) and
  the Einstein 1911 Varičak reply named as the correct primary (#824).
- Stamp/bib reconciliation: all four relativity-lineage anchors (FitzGerald,
  Lorentz, Larmor ×2, MM, Bell) now minted AND cited from the leaf; truth
  table in #828's body (#828).
