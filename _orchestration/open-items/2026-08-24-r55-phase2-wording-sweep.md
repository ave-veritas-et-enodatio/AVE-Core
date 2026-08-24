---
id: r55-phase2-wording-sweep
title: R55 Phase-2 — scripted long-tail wording sweep, "Axiom 5" → "the Substrate DC Bias source law"
status: OPEN
owner: lane
opened: 2026-08-24
source: _orchestration/docket-entries/2026-08-24-ruling-r55-axiom5-source-law.md
anchor: "the long-tail wording sweep"
---

R55 restructured the Substrate DC Bias axiom → source law and landed the Phase-1
authority sites (`eq_axiom_5.tex`, `CLAUDE.md` INVARIANT-S2, `axiom-register.md`,
`kb_index_lib.py` + tests, `eq_axiom_3.tex`). The long tail remains: **140 files**
under `manuscript/` + `src/` mentioned Axiom 5 at measurement (2026-08-24,
`git grep -il "axiom.\{0,1\}5" -- manuscript/ src/`).

Binding rewrite rule (R55 §4, verbatim): **"Axiom 5" → "the Substrate DC Bias
source law"**; **"five axioms" / "the axiom count is 5" → "the four axioms + the
source law."** Frozen trails (`research/`, `_orchestration/docket-entries/`) are
NOT rewritten, per Rule 12. Quoted-verbatim ratified text is never edited — sites
quoting the pre-R55 clause text byte-for-byte get a dated note only if
load-bearing, else they stand as historical quotes.

Execution shape (per the sweeps→scripts discipline): a script proposes the edits
site-by-site with context classes (grade-bearing statement / pure reference /
verbatim quote / frozen), a human-reviewable diff per class, and a receipt that
re-runs the measurement to zero grade-bearing residuals in live canon. One
reviewed PR. Until it lands, the alias note in INVARIANT-S2 + the register
carries the mapping and a pre-Phase-2 "Axiom 5" in live canon reads AS the
source law.

## HOMONYM-EXCLUDED class (added 2026-08-24, adversarial-review finding)

CLAUDE.md's own homonym guard (`manuscript/ave-kb/CLAUDE.md:379`, *"Homonym
guard — 'Axiom 5' is overloaded as of this landing"*) records that three live
engine files use the token `Axiom 5` for an UNRELATED coupled-resonator
normal-mode operator: `src/ave/solvers/coupled_resonator.py`,
`src/ave/condensed/silicon_crystal.py`, `src/ave/condensed/silicon_doping.py`.

These sites are **EXCLUDED from the rewrite rule** — applying it there would
mislabel an unrelated operator as the source law. The sweep script's context
classes MUST carry this exclusion explicitly. The operator's own rename (an
engine operator should never have carried an axiom's name; the guard asserted a
routing that was never minted) is a distinct sub-task of this sweep: propose
the rename in the same PR, separately reviewable, and retire the guard once
both the sweep and the rename land.
