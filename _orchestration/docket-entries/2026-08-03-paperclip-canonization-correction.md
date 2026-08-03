### ENTRY 2026-08-03-paperclip-canonization-correction (2026-08-03): correction to merged #832's fragment — the disclosed K2G prereg "off-by-one" DOES NOT EXIST; the frozen cite is correct

**Corrects:** [`2026-08-02-paperclip-canonization.md`](2026-08-02-paperclip-canonization.md)`:153` (merged **PR #832**, `2fcde4db`). Per [`README.md`](README.md)`:7` — *"Never edit another lane's fragment (Rule 12 corrections = a dated `-correction` suffix file referencing the original)"* — that fragment is **byte-untouched**; this file carries the correction. **Nothing in #832's physics or its paperclip canonization is affected**: the corrected item is a single out-of-scope *"surfaced, not fixed"* disclosure in its follow-on section.

#### The disclosure being corrected, verbatim

> *"…one lives in a `FROZEN` prereg: `research/2026-06-15_k2g-constitutive-provenance_prereg_FROZEN.md`:16 cites `…primer.md:26` for **"twist/microrotation ↔ couple-stress ↔ inductive/μ-sector"**, but the microrotation line is `:27` (`:26` is the E-field/translational-stretch bullet) — an **off-by-one that pre-dates this lane and is unaffected by it**. Surfaced, not fixed."*

#### The defect in the disclosure: a parenthetical mis-attached across a line wrap

**The prereg does not cite `primer.md:26` for microrotation.** It cites it for **stretch**, and the microrotation half carries its own, different cite. The sentence spans three source lines, and the cite sits at the *start* of `:16` while grammatically closing the clause that *ends* `:15` — which is what made it look attached to the clause that follows it. Verbatim, `research/2026-06-15_k2g-constitutive-provenance_prereg_FROZEN.md`:15-17:

```
15  **Corpus-anchored half (DOF-sector, qualitative):** stretch ↔ capacitive ↔ E-sector
16  (`electron-plumbing-primer.md:26`); twist/microrotation ↔ couple-stress ↔ inductive/μ-sector
17  (`translation-circuit.md:99-104`). Direction confirmed.
```

Two clauses, semicolon-separated, **each with its own trailing parenthetical cite**:

| clause | its cite | target content | verdict |
|---|---|---|---|
| *"stretch ↔ capacitive ↔ E-sector"* | `electron-plumbing-primer.md:26` | *"**E-field = translational stretch** (strain $\varepsilon$) — you *push/stretch* the fabric. This is the capacitive (C) sector."* | ✅ **exactly on point** |
| *"twist/microrotation ↔ couple-stress ↔ inductive/μ-sector"* | `translation-circuit.md:99-104` | `:100` *"**Microrotational B DOFs at node** \| **Inductive flywheel**"*; `:101` *"**Cosserat couple-stress $\gamma_c$** \| **Transformer mutual inductance gradient**"*; `:104` *"**Bond twisting (microrotational gradient)** \| Couple-stress / mutual-inductance gradient"* | ✅ **exactly on point** |

**Both cites are correct. There is no off-by-one, and there is nothing to fix in the frozen prereg.**

#### What IS true in the original disclosure

Its statement *about the primer* is accurate and is **not** corrected: `primer.md:27` **is** the microrotation bullet, and `:26` **is** the E-field/translational-stretch bullet. The error is solely the claim about **which clause the prereg attaches `:26` to**.

#### Temporal verification — both dates checked, because #832 itself moved the primer

The dispatch that surfaced this correctly flagged that merged **#832** added Step 3.5 to the primer, so line numbers might have shifted between the prereg's freeze date and today. **They did not** — #832's insertions land *below* the Step-1 bullet pair:

| primer line | at the freeze-date blob `bfa94beb` (2026-06-13, the primer's creating commit and the only one at or before the 2026-06-15 freeze) | at `origin/main` `583d43dd` (post-#832) |
|---|---|---|
| `:26` | *"**E-field = translational stretch** … capacitive (C) sector."* | **byte-identical** |
| `:27` | *"**B-field = microrotation** … inductive (L) sector."* | **byte-identical** |

So the cite `primer.md:26` was correct when the prereg froze **and is still correct today** — the correct target is `:26` under both readings of "correct target", and no re-pin is owed even in principle.

#### Disposition

- `research/2026-06-15_k2g-constitutive-provenance_prereg_FROZEN.md` — **BYTE-UNTOUCHED**, as a `FROZEN` prereg must be. It also needs no correction, which is the point of this entry.
- `manuscript/ave-kb/common/electron-plumbing-primer.md` — untouched.
- `_orchestration/docket-entries/2026-08-02-paperclip-canonization.md` — **byte-untouched** per README:7; this file is its dated correction.
- The K2G constitutive-provenance arc (prereg + [`result`](../../research/2026-06-15_k2g-constitutive-provenance_result.md)) is **unaffected**; no result, ruling or grade moves. **Zero ids minted.**
- **Durable lesson:** a cite-audit that reads a `file:line` claim without reading the *sentence* around it can mis-attach a trailing parenthetical to the following clause whenever the sentence wraps. The check that catches it is the one `verify-before-cite` already prescribes and that this pass ran: open the target, read what it says, and confirm it matches **the clause the cite actually closes** — not the nearest clause on the same line.
