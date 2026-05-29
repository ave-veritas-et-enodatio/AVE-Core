# AVE-KB Improvements / Remaining Work

Running list of open work scoped specifically to the AVE-KB (canonical markdown tree at `AVE-Core/manuscript/ave-kb/`). Broader design questions about future agentic systems live elsewhere; items here are about making the existing KB better as it stands. Completed items are removed — git history holds them.

---

## Deferred

### D0. KB-vs-LaTeX divergence as a staleness signal
The KB markdown tree is canonical; the LaTeX manuscript (`manuscript/vol_*/`) is a derived publication artifact (effective 2026-05-07; documented in `kb-docent.md` "Canonical Source" + INVARIANT-S7). **Open:** decide whether to add a verifier step that flags KB-vs-LaTeX divergence as a *derivation-staleness* signal ("the LaTeX has not caught up to this leaf") rather than a KB error. No automated LaTeX-lag detection currently exists.

### D8. Strip redundant identification-system remnants
The now-deprecated `axiom-homologation.md` (`session/`) called for unifying the framework's identification systems; the unified `clm-`/`exp-`/`sup-` metadata spine fulfilled that. Its residual value is a pointer to *strip out truly redundant/unnecessary identification-system remains* still scattered in the corpus. (Mine the historical doc for specifics when picked up.)

### D11. Split vol4 — relocate the circuit-theory/operator core to vol1, keep applied engineering in vol4 (**coordinate with Grant**)
**Root cause of the vol3→vol4 forward-dependency edges** (the `depends-on` edges tagged `[vol3→vol4 exception, D11]` in vol3's `claim-quality.md`): vol4 is *internally mixed* in dependency-depth. Ch1 circuit theory + the universal operators (Op14 `clm-1eg13f`, etc.), Theorem 3.1′ (`clm-rtdmsn`), and the parametric-coupling kernel (`clm-6t3p6x`) are **near-foundational machinery** that vol1/vol2/vol3 build on — while ch8 (fusion), ch11–12 (falsification benches), ch15 (autoresonant), and the chiral-thrust work are genuine *applications* that correctly sit late. A vol3 macroscopic result depending on vol4 is the signature of that foundational machinery being mis-volumed.

**The fix (decided as the right move 2026-05-24, NOT yet scheduled):** relocate the foundational circuit-theory/operator content out of vol4 into **vol1** (foundations) / `common/`, leaving vol4 as purely applied engineering (chiral thrust stays in vol4). This makes every vol3→vol4 edge point backward, and is **solidity-neutral** (pure relocation = same node/edges, just refiled — the location-juggling invariant). It eliminates those forward-edge exceptions at the root and is the structurally-correct alternative to renumbering volumes (a wholesale vol3↔vol4 swap was considered and rejected: vol4 is mixed, not uniformly more foundational, so a swap would just relocate the forward edges while detonating every path / cross-ref / `path-stable` label / `.tex` citation).

**Why deferred:** big cross-volume change (claim/leaf re-homing + every reference update); **requires coordination with Grant** before execution.

**Execution notes for when picked up:**
- Relocation candidates: Op14 (`clm-1eg13f`), Theorem 3.1′ (`clm-rtdmsn`), parametric-coupling kernel (`clm-6t3p6x`), `clm-v6ti0v`, `clm-p2tp9i`. **Verify each target's *own* dependency feet are axioms/common/vol1 only before moving** — a target that itself rests on vol4-specific content cannot move to vol1 cleanly (would create a *new* forward edge) and must be split or held.
- Keep applied content in vol4: chiral thrust (`clm-7tynm2`) and the bench/device/fusion/autoresonant chapters.
- On landing, drop the vol3→vol4 forward-edge exceptions (tagged `[vol3→vol4 exception, D11]` in their `depends-on` rationales) — they become ordinary backward edges to the relocated claims.

<!-- Completed, removed per "completed items are removed — git history holds them":
     D13 (distill P47/P10/P41 → leaves + bridge) + D14 (flip bridge check warn→critical), 2026-05-27;
     D15 (pin encoding="utf-8" on all text I/O — tools tree D15.1/D15.2, then the full src/ sweep), 2026-05-27. -->

