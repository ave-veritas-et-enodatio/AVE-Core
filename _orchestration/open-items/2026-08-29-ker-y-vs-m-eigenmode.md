---
id: ker-y-vs-m-eigenmode
title: "Analyze ker Y (DC loop current) and M-eigenmodes as two arms — do not pick; drop Maxwell–Calladine as the knot identity"
status: OPEN
owner: grant
opened: 2026-08-29
source: research/2026-08-29_overbraced-crystal-picture-lock.md
anchor: "Follow-up is spillover S10 (and board `ker-y-vs-m-eigenmode`)"
---

**Grant (2026-08-29, #1020 P7):** does not want to pick self-stress vs ringing. Wants to **analyze**.

**Grant (later):** P6 closed as a **#1020 follow-up**. Analysis stays here, not in the PR rewrite.

Two circuit objects (picture-lock P6 / the **WALK-GRADE, UNAUDITED** walk §1 P6): (i) \(\ker Y\) / DC circulating current, zero terminal excitation; (ii) eigenvector of the scatter map \(M\) at \(|\lambda|=1\), frequency \(\theta\). Maxwell–Calladine was the unwritten weld that treated them as one “knot.” Do **not** mint that name. Q1-style counts stay in S5 if wanted later.

**Clause Q** is a lens on the DC arm (Q-point / reference-fixing; R43: never “ground”), not a verdict. Split the \(\omega\) glyph (microrotation field vs rate vs HB \(\theta\)) before any compute.

**Instrument fence (P5 — WALK-GRADE, UNAUDITED):** `harmonic_balance_srs.py` is stretch/A1-only. It is the wrong bench for either arm as a Cosserat object.

Full record: [`research/2026-08-29_picture-lock-spillover.md`](../../research/2026-08-29_picture-lock-spillover.md) S10.

**Status-word correction 2026-09-06 (class-1 demotion; completeness sweep).** Grant ratified
2026-09-03 that *signed* means **an adversarial pass AND a physical/logical review with him**;
chat agreement alone is chat-walk grade. P5 has **no Grant assent at all** — the recorded line
is *“Does not understand; dig in more”* — so its grade here follows the lock down to
**WALK-GRADE, UNAUDITED**. **The instrument fence itself is unchanged and still binding:**
`harmonic_balance_srs.py` is stretch/A1-only and is the wrong bench for either arm as a Cosserat
object; that is an author-checked code fact, not a graded picture. **Prior wording, preserved
verbatim per Rule 12:** `:15` read *“(picture-lock P6 / signed walk §1 P6)”*; `:19` read
*“**Instrument fence (P5 SIGNED):**”*.
