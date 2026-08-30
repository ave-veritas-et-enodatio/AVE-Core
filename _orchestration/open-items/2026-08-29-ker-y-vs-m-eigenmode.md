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

Two circuit objects (picture-lock P6 / signed walk §1 P6): (i) \(\ker Y\) / DC circulating current, zero terminal excitation; (ii) eigenvector of the scatter map \(M\) at \(|\lambda|=1\), frequency \(\theta\). Maxwell–Calladine was the unwritten weld that treated them as one “knot.” Do **not** mint that name. Q1-style counts stay in S5 if wanted later.

**Clause Q** is a lens on the DC arm (Q-point / reference-fixing; R43: never “ground”), not a verdict. Split the \(\omega\) glyph (microrotation field vs rate vs HB \(\theta\)) before any compute.

**Instrument fence (P5 SIGNED):** `harmonic_balance_srs.py` is stretch/A1-only. It is the wrong bench for either arm as a Cosserat object.

Full record: [`research/2026-08-29_picture-lock-spillover.md`](../../research/2026-08-29_picture-lock-spillover.md) S10.
