# The Parallel-Site Re-Verify Gate (standing discipline)

**Status:** ACTIVE — ratified 2026-06-14 (discipline-infra lane, posture-B consolidation). **Lane-agnostic.**
**Owner:** discipline / infrastructure lane. **Consumed by:** every lane that banks an aggregating artifact.

## Why this exists
The immune system of this work is **lane independence**, not a skill firing inside the lane about to err. Every real catch across the arc came from an *independent* second lane (producer/auditor split, adversarial fan-out, a sibling's fresh grep, or Grant).

The recurring, structural failure this gate closes is the **salience-gradient / parallel-site lapse**: a discipline that holds at the *salient* site silently lapses at the structurally-identical *dull* one. It is not carelessness — AVE's own **Rule-12 amendment convention manufactures the trap**: the original verdict is preserved and the demotion is *appended*, so a loud early headline and a quiet later demotion coexist in one file *by design*. Anyone who builds a summary from the headline re-makes the error.

**Canonical instance (the gate's reason for being):** `genesis-chord-falsification-ledger.md` built the `screened-winding-probe` entry from the source's top `## VERDICT` block "EXONERATED" headline (`research/2026-06-11_screened-winding-probe_result.md:16`) and missed the appended §8 "VERDICT DEMOTED" panel (`:131`). The fix (commit `532e27d5`) was made by the **same lane** that built the error (`bfa94beb`), self-merged with zero reviews — it happened to be clean, but nothing *independent* confirmed that until this gate's first run (2026-06-14, all 10 entries re-verified FAITHFUL; the one standing source-trap is `screened-winding-probe`, whose §0 headline is still un-retracted by Rule-12 design).

## When the gate fires (eligibility — ALL three)
1. The artifact **aggregates ≥3 structurally-parallel entries** (ledger rows, matrix entries, a multi-file PR with repeated-structure files, a synthesis resting on N sources, a foreword promotion resting on N anchors).
2. It was built by **summarizing** those entries/sources (so a headline could diverge from the body).
3. It is about to be **banked** (committed, merged, or built upon).

## Scope — check EVERY entry ("least-salient" made determinable)
**Default: the independent lane re-verifies ALL N entries.** This is what the validated genesis run did (10/10), and it's the only scope a *fresh* independent lane can actually execute — "which entries did the producer flag?" is invisible to an auditor who wasn't in the producer's head, so a subset drawn from "what was flagged" is un-determinable and would silently exempt the exact entry that was reasoned-about-but-wrong. Do **not** narrow to a "salient subset."

The producer may narrow the set ONLY by recording the exemption in a **durable artifact** (a commit message or doc line naming the entries already independently checked, and by whom) — never an in-chat claim. Absent that, check all N.

Within the full set, two kinds of entry are **highest-yield — verify hardest, never skip:**
- **Any entry whose SOURCE is Rule-12-amended:** the source carries an appended section *after* its original verdict matching
  `DEMOTED | PANEL ADJUDICATION | AMENDMENT | Rule 12 | SUPERSEDED | RETRACT | REVISED | walk-back | correction`
  (case-insensitive). **Keep this list byte-identical to the template's grep step (`parallel-site-gate.template.js`).** Every Rule-12-amended source is a latent salience trap.
- For a multi-file PR, the look-uniform / repeated-structure files (whose diff is parallel to another file's), not the one interesting file the producer focused on.

## The check (independent lane, read-past-the-headline)
For each least-salient entry, an **independent** lane — **NOT** the producer who built the artifact —:
1. Reads the entry's **current claim** in the artifact (verbatim + line).
2. Locates the entry's **source** and reads **past the headline**: greps the *whole* source for any trailing amendment/demotion section appearing **after** the original verdict (the patterns above).
3. Confirms the entry reflects the source's **latest appended adjudication**, not its headline.
4. Cites **file:line on both sides.** Verdict ∈ {`FAITHFUL`, `SALIENCE-TRAPPED`, `OTHER-MISMATCH`, `CANNOT-VERIFY`}, and flags whether the source still carries an un-retracted headline (a **standing trap** for future readers, even if this entry navigated it).

Independence is non-negotiable: a producer's self-recheck is the weak form the gate exists to replace.

## Banking-checklist lines (copy-paste into any PR / merge / synthesis ritual)
> ☐ **Parallel-site re-verify:** an INDEPENDENT lane re-checked the least-salient entries (every un-flagged entry; priority on Rule-12-amended sources) against each source's LATEST adjudication — not the headline. Verdicts recorded; any `SALIENCE-TRAPPED` / `OTHER-MISMATCH` resolved before banking; any `standing source trap` flagged to the documentation lane for a §0 supersession-pointer.

> ☐ **Counterfactual actually exercised (both directions):** the counterfactual behind the result was *named and run*, not just asserted. A **positive** has a should-fail control that *actually failed* + a stated counterfactual it beats + **no knob / plant / fit / headline in the loop**. A **negative** is one the effect *could* have produced in that regime/carrier, closed by **functional form**, not a bare null. (The salience-gradient defense is the first line above; this is the operating principle that keeps a banked claim from resting on an un-exercised counterfactual. Encoded here as a checklist line, not a new skill — existing skills don't auto-fire.)

## Running it (the reusable template — do not hand-roll the fan-out)
The independent pass is one command:
```
Workflow({
  scriptPath: "<AVE-Core>/_orchestration/parallel-site-gate.template.js",
  args: {
    artifact:       "<what is being banked>",            // human description
    artifact_path:  "<file to read each entry's current claim from>",
    repo:           "<repo path for git history>",        // optional
    entries: [ { label, locate_hint, source_ref, note }, ... ]  // the least-salient set
  }
})
```
It fans **one independent `ave-auditor` per entry** and returns
`{ submitted, verified, unchecked, gate_green, total, faithful, salience_trapped[], other_mismatch[], cannot_verify[], standing_source_traps[], full[] }`
— a sub-auditor that returns null becomes an explicit `CANNOT-VERIFY` row (never silently dropped), and **`gate_green` is true only when every entry came back `FAITHFUL`**. The no-entries early return adds an `error` field.
Validated on the 10-entry genesis ledger, 2026-06-14 (run `w8qa61lvh`).

## Lane-agnostic
This gate is **not** genesis-ledger-specific. It applies to **any** aggregating artifact about to be banked — the field-decomposition lane's outputs, the magic-angle audit landing, a canon walk-back touching N leaves, a sweep-audit table, a foreword promotion resting on N anchors. Same trigger, same template.

## The discipline lane is not exempt (recursive caveat)
This lane edits the discipline infrastructure itself — exactly where salience lapses bite hardest (the trigger-detect hook's hardcoded table drifted once; `ave-newly-created-skill-self-audit` once failed its own audit). So this lane's **own** multi-entry artifacts — the declutter proposal's per-skill keep/retire calls, a `trigger_patterns` backfill across N skills, a hook keyword table — are parallel-site artifacts and get the **same independent re-verify before they land**, priority on the dull entries (the skills nobody flagged).
