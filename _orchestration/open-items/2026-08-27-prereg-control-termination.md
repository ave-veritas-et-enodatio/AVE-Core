---
id: prereg-control-termination
title: "Does the cold empty-vacuum CONTROL carry a Termination? The frozen prereg is silent, and two artifact arms depend on the answer"
status: OPEN
owner: grant
opened: 2026-08-27
source: research/2026-08-26_virtual-neutral-vs-saturation-wall_prereg_FROZEN.md
anchor: "The §3.1 negative control, the A5 artifact test, and the LOC-1 instrument receipt."
---

**A QUESTION, not an asserted defect.** Surfaced by the round-4 clearing audit of
PR #1023 and left deliberately unanswered by the round-5 repair lane, which
tabled both readings rather than picking one.

**Why this item lives on the prereg branch.** AMENDMENT 1's non-rescue receipt
cited *"`git diff --stat origin/main...HEAD` is one file"* as evidence that no
measurement exists on the branch to move a criterion toward, and AM2.2(b)
therefore declined to add a second file. `AMENDMENT 3` restates that receipt in
the form its content always had — **no driver, no solved state, no measured
number** — which this markdown file does not disturb. The question now travels
with the document it is about.

## The question

`AMENDMENT 1 §A1.1(i)` asserts that `CORE` is defined on the cold empty-vacuum
control. `CORE` is frozen in `§A1.2` as **the nodes owning a terminated slot**
(`port // net.degree`). So if the control carries no `Termination`, it has no
terminated slots, and `CORE` is undefined there.

**The frozen body does not say.** Read this session at
`origin/research/2026-08-26-virtual-neutral-prereg`:

- `:622` — the CONTROL row, verbatim: *"| **CONTROL** | `build_srs_net(L=6)` with
  $A_{\text{bond}} \equiv 0$ (cold, empty) | The §3.1 negative control, the A5
  artifact test, and the LOC-1 instrument receipt. |"* — the row states the
  carrier and the amplitude field. It states nothing about a termination.
- `:687-688` — verbatim: *"A **real** `Termination` with a non-empty port set and
  a non-zero drive, on every **physics** configuration. **`term=None` is FORBIDDEN
  on the physics path** (§7 NT-2)"*.
- `:874` — NT-2, verbatim: *"`term is not None` **and** `len(term.ports) > 0`,
  asserted at the call site | **`term=None` is FORBIDDEN on the physics path.**"*

Both requirement sites are scoped to the **physics path**. The control is not the
physics path. So the freeze neither requires nor forbids a termination there.

## Why it is load-bearing — two artifact arms turn on it

- **Arm A5** fires when the resolved null set `𝒩` **equals the cold control's null
  set**. If the control carries no drive it carries no field, so its null set is
  either empty or undefined — and the comparison A5 performs is then either
  vacuous or itself an A1 (`𝒩 = ∅`) condition. A5 is the arm that keeps a surface
  present in empty vacuum from being read as a confinement surface, so an arm that
  cannot evaluate is worse than one that fires.
- **`d_null`** is `AMENDMENT 1`'s frozen locus scalar, defined as a hop distance
  **to CORE**. On a control with no `CORE`, no `d_null` exists.

## The two readings, with the text each rests on

| reading | rests on | consequence |
|---|---|---|
| **The control DOES carry the §A1.2 Termination** | `:622`'s purpose clause names the control as the A5 comparator and the LOC-1 instrument receipt, both of which need a field; `§0:56`; `§4.4` arm A5 | A5 compares like with like; `CORE` and `d_null` are defined on the control as `§A1.1(i)` assumes |
| **The control does NOT** | `:687-688` and `:874` scope the requirement to *"every **physics** configuration"* / *"the physics path"*; `§5.9:708` enumerates the physics runs | `§A1.1(i)`'s clause is wrong as written; A5 needs restating in terms that do not require a control null set |

## Disposition

`AMENDMENT 1 §A1.1(i)`'s clause is marked **UNDETERMINED** on the prereg branch —
not withdrawn, not affirmed. It must be answered by a further **dated amendment**
(Rule-12 append, never an edit to the frozen body) **before a driver is written**,
because a driver would have to choose one reading silently.

## Method, and what this item does not establish

The three cites above were read this session from the branch blob, line by line.
This item does **not** claim the frozen body is silent everywhere on the control's
termination — it claims the CONTROL row and the two requirement sites do not
settle it, which is what was read. A search for other statements about the
control's drive was not run.

I did not determine which reading is correct. Both are consistent with the text
that was read, and choosing between them is a design decision about what the
negative control is *for*.

→ **grant**, or the lane that writes the driver, whichever comes first.
