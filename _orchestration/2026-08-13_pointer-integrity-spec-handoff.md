# HANDOFF — Pointer integrity: what problem are we actually solving, and does it warrant a gate?

**Class:** blind investigation lane. **Owner:** Grant launches. **Status:** not started.
**Posture:** you are asked to *derive a specification*, not to build a tool. Do not open a PR.

---

## §0 — Why you are blind, and what that means

An orchestrator has already formed a view on this. It is **deliberately withheld** until §6, which
is sealed. Read §1–§5, do the work, write your own answer, and only then open §6 to compare.

This matters because the orchestrator's last three attempts in this area produced: two tools with
self-referential defects that fired on their own source, and one gate that a cold audit found
**back-tests to zero on both incidents it was built for**. Its judgement here is not a reliable
prior, and anchoring on it is the specific failure this lane exists to avoid.

If §6 turns out to agree with you, say so plainly — convergence from an independent route is
evidence. If it disagrees, your reasoning wins unless it is factually wrong.

---

## §1 — The observed failures (verify these; do not take them on trust)

Four incidents, all 2026-08-13, all in AVE-Core. Each is checkable in git history.

1. **A 16-line freeze header** prepended to `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`
   broke **14 of 15** pointers created in the same commit (`_orchestration/open-items/*`).
   Detected mechanically, before anyone read them. See commit `a268d74f`.
2. **`manuscript/predictions.yaml` shrank 1110 → 138 lines** during a manifest split; 5 citations
   into it died. Detected by a checker, then repaired by hand — and the hand repair **missed 2 more**
   in `_orchestration/_archive/`.
3. **A stitched quote reached Grant as fact.** The orchestrator wrote *"the kinematic inventory 7
   stands on its own footing"* as a verbatim quote of a merged ruling. The source
   (`_orchestration/docket-entries/2026-08-12-ruling-r52-k2g-operating-point.md`, ~:113-115) reads
   *"That 7 is a different object from the per-cell kinematic inventory 7 (…), which stands on its
   own footing. **Do not merge the two sevens.**"* The elision removed the subject and inverted the
   meaning. A correction item was opened against a correct ruling on the strength of it.
4. **A withdrawn claim was cited as live.** `_orchestration/docket-entries/README.md` carried a
   `merge=ours` data-loss hazard that the corpus had **withdrawn 10 days earlier**
   (`_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md`, search
   `Merge note, CORRECTED 2026-08-03`). It was repeated into a plan as a live risk.

**Note the asymmetry in cost.** #1 cost approximately nothing. #3 and #4 cost real work and Grant's
attention. Ask yourself why, and whether the difference is structural. That question is the heart of
this brief.

---

## §2 — The existing tooling (read it before proposing anything)

All in `manuscript/ave-kb/tools/`:

- **`verify-md-links.py`** — repo-wide link + cited-id integrity. Reports ABSOLUTE state; the corpus
  carries ~3,100 pre-existing advisories. Console output TRUNCATES.
- **`verify-anchor-content.py`** — cited-line vs quoted-excerpt drift. **WARN-CLASS, always exit 0.**
  Read its docstring on *why*: it documents its false-positive classes and states that gating is
  *"a deliberate later promotion, not a default."*
- **`verify-anchor-content.py --new-cites BASE`** — a gating ratchet, wired in
  `.github/workflows/verify.yml`. Read `check_new_cites()` and establish **exactly** what it
  enforces. Be precise: there is a difference between requiring a thing to exist and requiring it to
  be correct, and which one this is determines most of your answer.
- `_orchestration/open-items/README.md` — the `anchor:` convention (pointers carry verbatim text,
  validated by `_orchestration/tools/generate_board.py`, which fails loud).

A tool named `verify-cite-stability.py` existed briefly and was **removed** — see the cold audit's
findings in PR #966's history. Do not resurrect it without independently re-deriving whether its
premise was sound.

---

## §3 — Measurements you should reproduce or refute

These come from a cold audit. Each is a claim; verify before relying on any of them.

| claim | why it matters |
|---|---|
| ~14,578 line-pins exist in tracked files | the legacy population |
| ~8,171 use bare/partial paths that never resolve from repo root | a root-only checker is blind to them |
| ~2,347 use `` `path`:NN `` (backtick OUTSIDE the colon) and ~932 use link form | the corpus's newer house styles |
| ~5,575 pins sit inside frozen/preserved text | Rule 12 forbids rewriting these, so they cannot be repointed |
| `constants.py` alone carries ~109 root-relative pins | one header insertion invalidates all of them |

If these are wrong, that is itself a finding — state the corrected numbers and your method.

---

## §4 — The questions to answer

1. **What is the harm, stated precisely?** Not "line numbers go stale." What bad outcome actually
   occurs, to whom, and at what cost? Use §1's four incidents as your evidence base and explain the
   cost asymmetry between them.
2. **What property of a pointer prevents that harm?** Derive it. Do not assume the answer is a
   checker.
3. **Given the existing tooling in §2, what is genuinely unguarded?** Be specific enough that
   someone could implement or reject it without further interpretation.
4. **Is a gate warranted for that gap, or is a convention sufficient?** The corpus's own position is
   at `verify-anchor-content.py` (warn-class, with stated reasoning). Argue with it or agree with it,
   but engage it.
5. **The 14,578 legacy pins** — convert, declare as permanent debt, or leave ambiguous? Say which and
   why. "Leave ambiguous" is currently the de-facto state and may be the worst of the three.
6. **What would a proposed check's coverage and false-positive surface be, measured?** A number, not
   an adjective. A tool that gates ~13% of the population while implying it covers all of it is worse
   than no tool.

---

## §5 — Deliverable and discipline

**Deliverable:** a written spec (or a reasoned "build nothing") answering §4. Name the files you
would change. No PR, no code.

- Every claim carries a receipt: file:line plus a quote, or a command plus its output.
- A "zero hits" result needs a structurally **different** second method, not a second regex. Box
  `grep` here is ugrep and has choked on complex patterns; `rg` and `git grep` are available.
- Truncated console output is **not** a diff basis. This repo has already shipped a false
  "0 new errors" that way.
- Consensus-bias check before flagging: actually broken, or merely unconventional?
- **STOP-AND-ASK PROTOCOL.** Stop and end your turn with a STUCK-POINT report if you hit: a fork this
  brief does not resolve · a corpus contradiction · an ontology question about what a thing IS · the
  same check failing twice (2-attempt cap). Report format: (1) the blocker, exact, file:line; (2)
  what you tried, ≤2 attempts; (3) the ONE question whose answer unblocks you, phrased concretely;
  (4) candidate readings, one line each, **un-endorsed**. A clean stuck-point report is a successful
  turn — it beats a plausible guess.

---

## §6 — SEALED: the orchestrator's candidate answer

> **Do not read until §4 is answered in your own words.** Then compare, and say plainly whether you
> agree, disagree, or think the framing is wrong.

<details>
<summary>Open after forming your own view</summary>

The orchestrator's position, offered as ONE candidate and explicitly not as the frozen criterion:

- The harm is a reader forming a **false belief** from a pointer, not the coordinate being stale.
  Incident #1 cost nothing because the pointer carried its own content, so breakage was detectable by
  string comparison at write time. #3 cost real work because the quote was fabricated-by-elision and
  nothing compared it to anything.
- Therefore the property that prevents harm is **pointer form** — a pointer must be verifiable by
  string comparison rather than by judgment — not drift surveillance.
- The dangerous failure is a pin landing on **wrong-but-plausible** content, not on a blank line or
  past EOF. The visible failure is the harmless one.
- `--new-cites` enforces that an added cite carries an adjacent excerpt. The orchestrator believes it
  does **not** verify that the excerpt MATCHES the cited source, and that this is the single genuine
  gap — the exact shape of incident #3.
- Candidate spec, one sentence: *a quote added next to a cite must appear verbatim in the file it
  cites.* Ratchet on new only; legacy stays warn-class; frozen text never gated.

Points of low confidence, flagged honestly: whether the gap is worth a gate at all versus convention;
whether the elision class (#3) is even mechanically detectable, since a *shortened* quote is
legitimate and an *inverted* one is not, and the difference may be semantic rather than textual.

</details>
