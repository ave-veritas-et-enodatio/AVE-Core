# R55 — The Substrate DC Bias is restructured: axiom → SOURCE LAW. The framework is "four axioms + a source law." (2026-08-24)

### ENTRY 2026-08-24-ruling-r55-axiom5-source-law

**Grant, in chat, 2026-08-24 (the question):** *"is axiom 5 actually needed?"*

**Grant, in chat, 2026-08-24 (the lean, after the panel and the options walk):**
*"i think option C is the most honest and accurate correct?"*

**Grant, in chat, 2026-08-24 (the go):** *"draft the ratificatiom for c and lets
start implementing"*

**Class:** ruling — a container-grade restructure. The ratified CONTENT of
clauses S, G, and Q moves nowhere and loses nothing; what changes is the grade
of the container that holds them: **axiom → source law**. Supersedes **R44's
count clause** (*"the axiom count is 5"*) — R44's body is preserved per Rule 12
and remains the authoritative record of WHAT was ratified on 2026-08-10; this
entry re-grades the container it ratified. Recorded once, by the core
orchestrator session, with Grant's words verbatim — per the R44 convention.

---

## §1 — The question and how it was adjudicated

A7 of Grant's 2026-08-24 itemized list — *"is axiom 5 actually needed?"* — was
run as a four-lane adversarial necessity panel (independent lenses: eliminate-it,
defend-it, machine-receipts, comparator-frameworks). The panel ran inline in the
core orchestrator session; **this entry is the panel's record of finding.**
Convergent verdict: **PARTLY-ELIMINABLE** — the axiom-grade container
over-grades its content. Three options were walked with Grant:
(a) keep as-is, (b) re-grade the clauses in place under the axiom banner,
(c) restructure to "four axioms + a source law." Grant ruled (c).

## §2 — The findings (receipts, each independently checkable)

*(All §2 quotes are from the file as it stood at panel time, pre-restructure —
Phase 1 re-nouns the container in place; git carries the pre-edit text.)*

**2.1 The ratified text already grades its own clauses.** All three receipts are
verbatim from the canonical file, [`eq_axiom_5.tex`](../../manuscript/common_equations/eq_axiom_5.tex):

- **Clause S is DATA.** The file's own words: *"it is genesis-deposited
  boundary data on the crystalline phase, and it states that the flux is
  written, not how."* Boundary data is not an axiom of the material; it is
  what a particular history wrote onto the material.
- **Clause G is the one LAW-grade clause.** The κ-stiffened elliptic bias law
  $-\nabla\cdot[\kappa D(A)\nabla\varepsilon_{11}] = 4\pi T_{00}$ — a **source
  law** (Poisson-class comparator; elliptic, hence instantaneous by
  construction — the file itself names THE BIAS PROPAGATION THEOREM as
  *"this axiom's STANDING DEBT"*).
- **Clause Q is REFERENCE-FIXING.** The file's own words: *"the quiescent
  reference (Q-point) that makes the potentials defined and clause G's
  elliptic solve well-posed."* Grant's own ratifying words on 2026-08-10 were
  already reference-language: *"makes perfect sense, we need a ground
  reference."* A ground reference is a gauge choice, not a material primitive.

**2.2 The file's own discrimination check concedes the grade.** Verbatim:
*"the whole axiom can be read as 'boundary conditions', which every field
theory carries."* Option (c) makes the file's own concession the official
grade instead of a buried caveat.

**2.3 The flat-direction receipt.** The complex adds no dynamics: the file's
own forbids-block states *"it adds no kinetic or potential term on the flat
direction, so the pole-absence results survive it untouched."* What the
2026-08-10 ratification added was data (S) + one elliptic law (G) + a
reference (Q) — no new stiffness, no new wave, no new degree of freedom.

**2.4 The machine receipt (measured 2026-08-24, this repo state).** Inbound
`depends` edges by target in `manuscript/ave-kb/.index/depends-on.jsonl`:

| target | inbound depends edges |
|---|---|
| axiom-1 | 99 |
| axiom-2 | 38 |
| axiom-3 | 30 |
| axiom-4 | 101 |
| **axiom-5** | **0** |

Nothing in the claim graph depends on axiom-5. This receipt is strong, not
incidental: the index builder emits an `axiom` edge for every depends-on bullet
whose head names "Axiom N" (`kb_index_lib.py`, `_AXIOM_TOKEN_RE`), and the
build-time dangling guard (`_assert_framework_node_coverage`) fails loudly on
any reference to a missing node — so a zero count means zero derivations
declare the DC-bias complex as a premise. The founding four carry the entire
load-bearing surface. **Retiring the `axiom-5` framework node breaks zero
index consumers, verified at build time by the guard itself.**

*(Receipt correction, recorded for honesty: an earlier chat statement of this
receipt was re-measured before this entry landed. The numbers above are from
the live index at authoring; the claims.jsonl records themselves carry no
inbound-edge fields — the edges live in `depends-on.jsonl`.)*

## §3 — The ruling: four axioms + a source law

**The cut (AVE-native, the datasheet-vs-loading argument).** Axioms 1–4 are
the substrate's **DATASHEET** — what the material IS: its topology (Ax 1), its
charge dictionary (Ax 2), its lossless extremal dynamics (Ax 3), its
saturation kernel (Ax 4). The DC-bias complex is the **LOADING
specification** — what has been done TO the material: what a genesis history
deposited (S — data), how sources couple to the bound sector (G — the source
law), and where the reference sits (Q — the gauge/ground choice). A component
datasheet does not carry the application circuit's bias point. The file's own
EE-FIRST mapping already places clause G as a **BIAS NETWORK** — an
application circuit, not a component property.

**Ratified consequences:**

1. **Grade.** The container is a **SOURCE LAW**, not an axiom. Clause G is the
   law proper; clause S is its boundary data; clause Q is its reference
   fixing. All three travel together under one name, as ratified.
2. **Name.** R46's ratified name **"Substrate DC Bias" is RETAINED.** The
   canonical container noun is **"the Substrate DC Bias source law"** (short
   form in running prose: *"the source law"*). No renaming of the object, only
   re-grading of its container.
3. **Count.** The framework statement is **"the four axioms + the source
   law."** R44's *"the axiom count is 5"* is SUPERSEDED (count clause only;
   body preserved). *"The first new axiom ratified since the founding set"*
   becomes a historical statement — true of its date, superseded in grade.
4. **Content untouched.** Every equation, clause text, named-open hole
   (c1–c4), the internal falsifier $B = 7\mathcal{A}_g GM/c^2$ with ONE
   $\mathcal{A}_g$ across every consumer, the R45 phase structure, the R48
   UNVALUED-RATIFIED-CONSTANT status of $\mathcal{A}_g$, the R49(a)
   convention, and the R50 vocabulary all stand exactly as ratified. R43,
   R45–R50 are NOT superseded — they graded, named, and tooled the same
   object; the object persists.
5. **Derivation grade unchanged.** S/G/Q remain POSTULATED content (the
   file's derivation-grade note stands verbatim). This ruling does not claim
   the source law is derived; it claims the honest grade of postulated
   loading-data + one source law + one reference is not "axiom of the
   material."

## §4 — Consequence sweep (phased; Phase-1 authority sites land with this entry)

**Phase 1 (this PR):**

- [`eq_axiom_5.tex`](../../manuscript/common_equations/eq_axiom_5.tex) —
  container reframe (title, status block, container nouns); ratified clause
  text byte-preserved; R55 provenance block added, R49(a)-style (canonical
  file corrected in place, the dated block is the audit trail).
- `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 — the `- Axiom 5:` bullet
  re-headed as the source-law bullet (outside the axiom enumeration); the
  axiom parser reverts `[1-5]` → `[1-4]`
  (`kb_index_lib.py:180,183`, the R47 widening) so the `axiom-5` framework
  node RETIRES from `claims.jsonl`. §2.4's receipt + the dangling guard prove
  zero breakage.
- [`axiom-register.md`](../../manuscript/ave-kb/common/axiom-register.md) —
  counts return to 4; the register's own title ("the Four AVE Axioms")
  becomes correct again; the Substrate DC Bias section re-headed as the
  source-law entry with a dated R55 note, per the register's own line-shift
  discipline (appended notes, no in-place shifts above the cite surface).
- [`eq_axiom_3.tex`](../../manuscript/common_equations/eq_axiom_3.tex) —
  dated R55 fragment on the Gauss-function attribution (§5, rider 1).
- Index regen + board regen.

**Phase 2 (follow-on PR, scripted, per the sweeps→scripts discipline):** the
long-tail wording sweep. Live-canon reference surface measured 2026-08-24:
**140 files** under `manuscript/` + `src/` mention Axiom 5. Binding rewrite
rule: **"Axiom 5" → "the Substrate DC Bias source law"**; **"five axioms" /
"the axiom count is 5" → "the four axioms + the source law."** Frozen trails
(`research/`, `_orchestration/docket-entries/`) are NOT rewritten, per Rule 12
— they carry the historical grade honestly. Until Phase 2 lands, the alias
note in INVARIANT-S2 and the register carries the mapping, and a pre-Phase-2
"Axiom 5" in live canon reads AS the source law.

## §5 — Riders

1. **The eq_axiom_3 Gauss-function attribution (panel finding, repaired this
   PR).** `eq_axiom_3.tex` states the Gauss function
   $\nabla\cdot(\varepsilon_0\partial_t\mathbf{A})$ is *"pinned to its source
   value by the bound-sector constitutive law (Axiom 5 …); which clause of
   Axiom 5 pins it is deliberately left open."* The panel's answer: **no
   ratified clause writes that pin.** Clause S deposits the A1 dilatation flux
   $\oint_S \mathbf{u}\cdot\hat{\mathbf{n}}$ — a mechanical-sector object,
   DISTINCT from the EM Gauss function per the eq file's own non-circularity
   observation (the bias $\varepsilon_{11}$ vs $\nabla\mathbf{u}$ distinctness
   that the 57-order $\mathcal{A}_g$ miss evidences). The EM Gauss-function
   pin is **OWED on FORK-1, not held.** A dated fragment lands in
   `eq_axiom_3.tex` upgrading "deliberately left open which clause" to the
   honest "no clause yet — named-open, riding FORK-1."
2. **The $B(M)$ glyph collision** (open item
   `2026-08-24-axiom5-b-glyph.md`, PR #1003): rides the restructure **when
   Grant picks the replacement glyph**. This PR keeps $B(M)$ with the
   collision warning in place.
3. **R52-vs-pilot K-receipt reconciliation:** routed as its own open item
   (panel finding recorded there; adjudication separate — flag-don't-fix).

## §6 — What this ruling is NOT

- NOT a retraction of any clause, value, hole, or the falsifier.
- NOT a claim that the source law is derived (it remains postulated).
- NOT a demotion of the content's importance — every bias / bound-response /
  back-reaction consumer still routes through it. What changed is the honest
  answer to *"is this a structural primitive of the material?"* — no: it is
  the law + data + reference by which the material is **loaded**.
- NOT a license to delete "Axiom 5" from frozen records — Rule 12 stands.
