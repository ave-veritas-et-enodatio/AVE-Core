# A1 Amplitude Trace — Frozen Verdict Bins (PREREG, frozen-by-push)

**Date:** 2026-07-20
**Branch:** `research/a1-amplitude-trace` (worktree off `origin/main` @ `64f1894d`)
**Lane:** implementer — A1 AMPLITUDE TRACE (short derivation lane, Grant-fired 2026-07-20:
verbatim [sic] "lets fire the short derivation task to teace A1")
**Status at freeze:** FROZEN. This document is pushed BEFORE the verdict is written, per the
freeze-by-push / prove-or-disprove discipline. The frozen bins + decision criteria + the
consequence-each-way statements below cannot be tuned to the completed trace's conclusion.

---

## §0 — The question (settles the physics under the #748 MOND adjudication)

At a node sitting in the **STATIC** gradient-index profile of a galaxy, what IS the amplitude
`A` that enters the Axiom-4 saturation kernel `S(A) = √(1 − A²)`?

**Two candidate identifications:**

- **(i) `A = g_N/a_0`** — field-over-yield-field, the #748-adjudicated canonical. Substituting into
  the quadratic kernel gives `S = √(1 − (g_N/a_0)²)` — the QUADRATIC form. Uniform with the corpus
  grammar everywhere else (`r = V/V_SNAP`, `A = E/E_yield` — every catalog row keys LINEARLY on
  field/critical-field). #748 canonicalized this from the leaf's own setup but **did NOT derive it**
  (`2026-07-20_mond-kernel-adjudication_result.md` R3, on branch `feat/mond-kernel-adjudication`).
- **(ii) `A ∝ √(g_N/a_0)`** — the strain-amplitude reading in the engine docstring narrative
  (`galactic_rotation.py:135` "orbital shear creates a strain proportional to √(g_N)").
  **Retirement equivalence:** `A = √(g_N/a_0)` into the canonical quadratic kernel `√(1 − A²)` gives
  `√(1 − g_N/a_0)` ≡ the RETIRED linear-in-ratio form. So (ii) winning **REOPENS** the #748
  form-level resolution.

**Regime/sector header (frozen):** A1 dilatation; static / DC operating point (fixed rotation rate =
fixed acceleration = DC bias point, Grant-walked 2026-07-20); sub-yield lossless-reactive (Regime I–II,
`g_N ≪ a_0` at SPARC `r_eval = 5·R_disk`); galactic scale. **This is a DC operating-point
identification, NOT a modal problem.**

SPARC measured (i) and (ii) DEGENERATE (#748) — only a constitutive derivation settles it.

---

## §1 — Frozen verdict bins + decision criteria

The trace TRACES which node-level state variable the kernel's `A` physically is, following (a) the
Axiom-4 kernel's own L2-norm definition of `A` (`common/axiom-register.md:188` — `A` is the normalized
amplitude of the dynamical LC-tank coordinate, `A² =` energy fraction), (b) the DC-operating-point
`A`-definition (`ave-kb/CLAUDE.md:75` — `A_0 = V_DC/V_yield = E_local/E_yield` = field/yield-field),
(c) the `a_0` provenance chain (`mond-hoop-stress.md` — `a_0 = c H_∞/(2π)`, a critical ACCELERATION),
and (d) the gradient-index gravity mapping (`einstein-field-equation.md`, `trampoline-analogy-primer.md`
Step 5.5). Each step is tagged `canon-read` / `derived` / `assumed`; where the chain hits an unforced
identification it is named and the trace **fails closed**.

**FROZEN BINS (exactly one is selected by the trace):**

- **`A=g_N-FORCED`** — the substrate forces `A = g_N/a_0` (linear-in-field into the quadratic kernel).
  *Selected iff:* the DC-operating-point `A`-definition (field/yield-field) + a corpus-native mapping of
  the gravitational field `g_N` onto the tank's field coordinate, with the yield being the critical
  acceleration `a_0`, is forced with no free alternative. #748 canonical CONFIRMED and upgraded
  leaf-asserted → substrate-derived.

- **`A∝√g_N-FORCED`** — the substrate forces `A = √(g_N/a_0)` (→ retired linear kernel). *Selected iff:*
  the tank's saturating coordinate is forced to be a quantity whose SQUARE (energy) is `∝ g_N` (e.g. the
  orbital-motion Lorentz strain `A = v/c`, `v² = g_N r`), AND that quantity normalizes cleanly to
  `√(g_N/a_0)` with the CANONICAL constant `a_0`. **This REOPENS #748** (Rule-11 consequence banked, not
  softened — the form-level resolution would have to be re-run).

- **`UNDETERMINED`** — an unforced choice controls it. *Selected iff:* the chain reaches an
  identification the corpus neither derives nor forces (e.g. field-vs-kinetic amplitude is a free
  posit), so neither (i) nor (ii) is substrate-forced. The trace then states the precise
  **additional axiom-level statement** that would force each branch.

**Anti-anchoring fence (frozen):** the #748 canonicalization AND the 26-row catalog uniformity prior
BOTH favor (i). The trace is run as if either could win. A finding of `A=g_N-FORCED` must rest on a
substrate-forcing chain, NOT on the prior; if the only support is "everything else does it that way,"
that is `UNDETERMINED`, not `A=g_N-FORCED`. Conversely (ii) is steel-manned to its strongest
substrate story before being set aside.

---

## §2 — Consequence-each-way (frozen pre-verdict)

**If `A=g_N-FORCED`:**
- #748 canonical form (`g_eff = g_N + √(g_N·a_0)·√(1 − (g_N/a_0)²)`) CONFIRMED; the amplitude
  identification upgrades **leaf-asserted → substrate-derived** (`clm-u86caq`).
- R3 docstring follow-on: `galactic_rotation.py:135` "strain proportional to √(g_N)" corrects TOWARD
  `A = g_N/a_0` — the trace supplies the DERIVATION #748 R3 said it lacked. (Docstring edit is a routed
  engine-hygiene follow-on, NOT landed by this research lane.)
- The √g_N object is relocated to its correct home (named by the trace), not deleted.

**If `A∝√g_N-FORCED`:**
- #748 form-level resolution REOPENS; the retired linear kernel `√(1 − g_N/a_0)` returns as
  substrate-forced. Surfaced to Grant + auditor; the SPARC-degeneracy verdict stands but the
  form-resolution tiebreak flips. Rule-11: banked as a clean reopening, not debugged toward a rescue.

**If `UNDETERMINED`:**
- #748's canonical form remains leaf-asserted (NOT substrate-derived); the R3 follow-on stays open;
  the precise missing axiom-level statement is surfaced to Grant as the walk item.

---

## §3 — Discipline

research/ deliverables only (this prereg + a result doc + a small symbolic/numeric check script); no
engine/KB/tex edits; pure-corpus; incremental commits; `make verify` green; dated docket continuation
entry; PR `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`. Flag-don't-fix on any contradiction found.
