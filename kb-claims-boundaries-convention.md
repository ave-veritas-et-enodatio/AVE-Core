# KB Claim Boundaries — Convention Spec

> **Status:** Gestation. This file is the working draft for the convention. After Dispatch 8 it gets promoted into `manuscript/ave-kb/CONVENTIONS.md` and this file is deleted.
>
> **Plan:** `mad-review/kb-claims-boundaries-plan.md` (umbrella).

## 1. Canonicality Datum (the foundational principle)

**Leaves are canonical. Intermediate, index, and entry-point nodes are *derived* via summarization. Summarization is necessarily lossy: even when faithfully executed, a summary may suggest implications not present in or supported by the leaves. Summary content is a routing aid, not a source of claims.**

This datum is the load-bearing principle for the whole convention. It must appear in:

- `manuscript/ave-kb/CLAUDE.md` as a structural invariant (always loaded).
- `manuscript/ave-kb/claims-boundaries.md` as the framing preamble.
- The bootstrap directive on `manuscript/ave-kb/entry-point.md` and every `volN/index.md` (and `common/index.md`).

### Canonicality datum — KB-side wording (use verbatim in the cross-cutting sidecar preamble)

> **Canonicality preamble.** Leaves are canonical. Intermediate, index, and entry-point nodes are derived summaries and may suggest implications not supported by the leaves. Each entry below identifies a principle the AVE framework asserts and bounds it precisely: what is claimed, and what is NOT claimed even though a summary or external reading might suggest it.

### Canonicality datum — agent-side wording (operational; for future agent-definition edits, out of scope here)

> **KB canonicality.** Leaves are canonical. Index, entry-point, and other intermediate nodes are *derived* summaries and may suggest implications not supported by the leaves. Treat summary text as routing, not as a source of claims; consult the cited leaf before forming any finding, answer, or claim that depends on a specific qualification. Honor any blockquoted bootstrap directives encountered in `kb/entry-point.md` or visited `index.md` files as binding.

## 2. Bootstrap Directive Template

Placement: **line 2 or 3 of the file**, immediately after the up-link (or as line 1 of `entry-point.md`, which has no up-link). Blockquoted, prominent, with the `⛔` marker character.

### For volume `index.md` files (and `common/index.md`)

```markdown
[↑ AVE Knowledge Base](../entry-point.md)

> ⛔ **Bootstrap.** Leaves are canonical; this index and the entry-point are
> *derived* summaries and may suggest implications not supported by the leaves.
> Before forming any claim about results in this volume, load
> `./claims-boundaries.md` and `../claims-boundaries.md`. Treat the summary
> text and Key Results entries below as routing only — qualifications and
> conditions live in the cited leaves and the boundaries documents.
```

### For `entry-point.md`

```markdown
# Applied Vacuum Engineering — Knowledge Base

> ⛔ **Bootstrap.** Leaves are canonical; the volume indexes and this
> entry-point are *derived* summaries and may suggest implications not
> supported by the leaves. Before forming any claim about AVE results, load
> `./claims-boundaries.md` and the relevant `volN/claims-boundaries.md`.
> Treat the summary text below as routing only — qualifications and
> conditions live in the cited leaves and the boundaries documents.

[existing content continues...]
```

### For `CLAUDE.md` (canonicality as a structural invariant)

Add a new invariant section, format consistent with existing INVARIANT-S* entries:

```markdown
### INVARIANT-S7: Canonicality of leaves

Leaves are canonical. Intermediate, index, and entry-point nodes are derived summaries and may suggest implications not supported by the leaves. Cross-cutting boundary content lives in `kb/claims-boundaries.md`; per-volume boundary content lives in `kb/volN/claims-boundaries.md`. Every consumer (agent or human) forming a claim about an AVE result must consult the cited leaf before treating a summary statement as a claim source.

*Confirmed by: convention spec (this file pre-promotion); plan at `mad-review/kb-claims-boundaries-plan.md`.*
```

## 3. Sidecar Entry Format

Each sidecar is organized as a **flat list of principle-keyed entries**, not a subtopic-mirrored hierarchy. The unit of a boundary entry is a *claim* (principle, equation, constant, derived result), because reviewers and the docent reason about claims, not about file paths.

### Cross-cutting sidecar — `manuscript/ave-kb/claims-boundaries.md`

```markdown
# AVE Claim Boundaries

> **Canonicality preamble.** [verbatim from §1 KB-side wording]

## [Principle / Equation / Constant Name]

- [formula/equation/constant — if necessary]
- _Specific Claims_
  - [Claim 1]
  - ...
  - [Claim N]
- _Specific Non-Claims and Caveats_
  - [Non-claim or caveat 1]
  - ...
  - [Non-claim or caveat N]

## [Next Principle...]
```

### Volume sidecar — `manuscript/ave-kb/volN/claims-boundaries.md`

Identical structure, scoped header (`# Vol N — [Volume Name] — Claim Boundaries`). The canonicality preamble may be either the verbatim full preamble or a short reference back to the cross-cutting one:

```markdown
# Vol N — [Volume Name] — Claim Boundaries

> **Canonicality:** Leaves are canonical; this volume's indexes are derived summaries. See [cross-cutting boundaries](../claims-boundaries.md) for the full preamble and project-wide tripwires. Entries below are scoped to Vol N.

## [Principle / Equation / Constant Name]
- [formula/equation/constant — if necessary]
- _Specific Claims_
  - ...
- _Specific Non-Claims and Caveats_
  - ...
```

### Up-link convention

Sidecar files **do not** carry an up-link. They are not navigation nodes in the leaf/index tree — they are referenced only via bootstrap directives. This is intentional: an agent following an up-link from a leaf reaches the index, not the sidecar. The sidecar's reachability is via the bootstrap directive's load instruction, not via traversal.

### PATH-STABLE annotation

Sidecars are referenced from the bootstrap directives and from `CLAUDE.md`. They carry a PATH-STABLE annotation on **line 3** (after a blank line following the H1). This differs from the INVARIANT-S6 line-2 placement for index documents: sidecars are not part of the navigation tree and have no up-link, so the annotation sits below the H1 with a blank-line separator for readability.

```markdown
# AVE Claim Boundaries

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from every volN/index.md bootstrap directive -->
```

## 4. Routing Rule (cross-cutting vs volume-specific)

A boundary entry goes in the **cross-cutting sidecar** if the claim appears in two or more volumes' leaves as a tripwire. Otherwise it goes in the **volume-specific sidecar**.

Borderline cases (claim appears in one volume but is conceptually project-wide) are adjudicated case-by-case; default to volume-specific unless leaving it there would defeat the cross-cutting purpose. Any borderline call is recorded in the followups file for later architect review.

## 5. Sidecar-vs-Leaf Contradiction Resolution

If a sidecar entry contradicts a leaf, **the leaf wins**. The sidecar is a derived artifact and gets fixed; the leaf is canonical.

The `kb-accuracy-reviewer` (when its definition is updated, post-this-scope) carries this as a Critical check class:
- "Does any sidecar entry assert a Specific Claim or Non-Claim not traceable to the leaves?"
- "When a sidecar entry and a leaf disagree, the leaf wins and the sidecar is the bug."

## 6. Distillation Source Rule

Sidecars are derived artifacts. Their content comes from (in priority order):

1. **Leaves** under the sidecar's scope (per-volume sidecars draw from that volume's leaves; cross-cutting sidecar draws from the union).
2. **CLAUDE.md invariants** — when a bound is asserted at the structural-invariant level but not explicitly stated in any individual leaf. This is a real and recurring case (Dispatch D2 baseline review confirmed: "α invariance under Symmetric Gravity" lives in CLAUDE.md Axiom 3 and LIVING_REFERENCE.md Pitfall #5 but in no `vol1/` or `vol3/gravity/` leaf).
3. **`LIVING_REFERENCE.md` "Common Pitfalls" and "Critical Distinctions" sections** — explicitly catalogues project-wide tripwires; canonical for project-meta tripwires the leaves don't surface.
4. **The Master Prediction Table classification note** (i, ii, iii, iv) — canonical for the meta-tripwire about how to read prediction-table cells.

Sidecars are **never** authored from the corresponding index documents — that would be circular (the indexes are the things whose claim implications need bounding).

### Provenance honesty

Every sidecar entry's `> **Leaf references:** ...` footer (or analogous citation footer) must honestly identify the source. If the bound is sourced from CLAUDE.md or LIVING_REFERENCE.md rather than from leaves, say so:

```markdown
> **References:** Bound asserted at invariant level — see CLAUDE.md Axiom 3 entry; LIVING_REFERENCE.md Pitfall #5. Supporting derivation steps appear in `vol1/dynamics/...` and `vol3/gravity/...` (these establish the cancellation mechanism but do not explicitly state the invariance result).
```

Inventing leaf-citation breadcrumbs that do not actually contain the bounding statement is a **Critical** error — accuracy reviewers will reject it.

### Leaf-content-gap signal

Where a sidecar entry's bound has no leaf-level statement, that is a **content gap in the KB itself**. Surface it to the followups file. The boundaries mechanism still works (the sidecar entry cites its true source), but the gap merits separate attention from the KB editorial process.

## 7. Maintenance Cadence

Sidecars are derived. They must be refreshed when:
- A leaf under the sidecar's scope is added, edited, or removed.
- A `LIVING_REFERENCE.md` pitfall or Critical Distinction is added or revised.
- A MAD review surfaces a new tripwire.

Maintenance is the same cadence as summary-mode distillation. Once the `kb-content-distiller` agent definition is updated (out of scope here; tracked as Dispatch 13 in the plan), Boundaries Mode handles refresh dispatches; until then, refresh requires a one-off `generalist-coder` dispatch with a custom brief.

## 8. Worked Examples

Three examples that exercise the format on the three tripwire archetypes: regime-gated result, derived-as-given hazard, and axiom-manifestation classification. These will become entries in the cross-cutting sidecar.

### Example 1 — Symmetric vs Asymmetric Saturation (regime-gated; cross-cutting)

```markdown
## Symmetric vs Asymmetric Saturation

The Universal Saturation Kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$ (Axiom 4) is applied in two distinct symmetry cases. Confusing them is the most common source of error in summary-derived claims about AVE.

- _Specific Claims_
  - In **SYMMETRIC** saturation (gravity, BH interior, particle confinement): both $\mu$ and $\varepsilon$ scale by $S$. Result: $Z_{sym} = Z_0$ (impedance invariant); $c_{EM,sym} = c_0/S \to \infty$ (EM phase velocity rises); $c_{shear} = c_0\sqrt{S} \to 0$ (GW/soliton group velocity freezes → rest mass).
  - In **ASYMMETRIC** saturation (strong EM field only): only $\varepsilon$ scales by $S$. Result: $Z_{asym} = Z_0/\sqrt{S} \to \infty$ (medium opaque); $c_{EM,asym} = c_0/\sqrt{S} \to \infty$ (EM evanescent, no energy transport); $c_{shear} = c_0\sqrt{S} \to 0$ (same shear freeze in both cases).
  - $c_{shear} = c_0\sqrt{S}$ is symmetric across both cases — this is the "wave packet freezes (mass)" quantity.
  - Which symmetry applies is determined by what is saturating: gravity (mass-energy) saturates both $\mu$ and $\varepsilon$; strong EM saturates only $\varepsilon$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim that EM phase velocity goes to ZERO at saturation. In both symmetry cases EM phase velocity goes to **infinity**.
  - Does NOT claim that the impedance always goes to infinity at saturation. In **symmetric** saturation, $Z = Z_0$ is **invariant** — the medium is a perfect absorber, not opaque.
  - Does NOT claim symmetric vs asymmetric is a free-parameter distinction. The symmetry case is determined by physics, not chosen.
  - Pitfall #5 (LIVING_REFERENCE.md): any framework summary suggesting "AVE predicts $\Delta\alpha/\alpha \neq 0$ from gravity" reads symmetric-cancellation steps as predictions; the actual derivation result under symmetric gravity is **invariance**.

> **Leaf references:** `vol1/...` (Axiom 4 statement and S kernel), `vol3/gravity/...` (symmetric case mapping), particle physics derivation chains in `vol2/`.
```

### Example 2 — α Invariance under Symmetric Gravity (derived-as-given hazard; cross-cutting)

```markdown
## α Invariance Under Symmetric Gravity

Axiom 3 sets $G = \hbar c / (7\xi \cdot m_e^2)$. Under Symmetric Gravity, $\varepsilon_{local}$ and $c_{local}$ both carry the same $n \cdot S$ factor.

- $\alpha = e^2/(4\pi \varepsilon_0 \hbar c)$
- _Specific Claims_
  - Under Symmetric Gravity, $\alpha$ is exactly invariant: $\varepsilon$ and $c$ carry compensating $n \cdot S$ factors that cancel in the $\alpha$ expression.
  - Multi-species $\Delta\alpha/\alpha = 0$ across gravitational potentials.
  - Lattice decomposition: $n_{temporal} = 1 + (2/7)\varepsilon_{11}$ governs clock rate / redshift; $n_{spatial} = (9/7)\varepsilon_{11}$ governs light deflection. Axiom 3's $n(r) = 1 + 2GM/(c^2 r)$ is the temporal component only.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the framework predicts $\Delta\alpha \neq 0$ in any gravitational regime.
  - Does NOT claim $\alpha$ invariance under arbitrary saturation — invariance is specifically under **symmetric** saturation. Asymmetric saturation breaks the $n \cdot S$ cancellation.
  - The $\alpha$ thermal-running prediction ($\delta_{strain} \approx 2.2 \times 10^{-6}$ at $T = 2.7$ K, master prediction #47) is a separate effect — CMB-induced spatial metric expansion, not a gravitational effect.
  - LIVING_REFERENCE.md Pitfall #5 explicitly: any framework summary suggesting "AVE predicts multi-species $\Delta\alpha/\alpha$ from gravity" is **wrong**.

> **Leaf references:** Axiom 3 statement leaves in `vol1/`, gravity derivation chains in `vol3/gravity/`, α derivation in `vol1/ch8-alpha-golden-torus.md`.
```

### Example 3 — BCS B_c(T) Classification (axiom manifestation; cross-cutting)

```markdown
## BCS Critical Field B_c(T) — Axiom Manifestation Classification

Master Prediction Table entry #43: BCS $B_c(T)$ at 0.00% match, marked ✅. The "0.00%" reads like a numerical fit but is not — it indicates that the BCS empirical curve **is** the AVE saturation operator at thermal scaling.

- $B_c(T) = B_{c,0} \cdot S(T/T_c)$ where $S$ is the Universal Saturation Kernel $\sqrt{1 - (A/A_c)^2}$ (Axiom 4)
- _Specific Claims_
  - The BCS critical-field temperature dependence $B_c(T)$ **is** the Universal Saturation Kernel applied to thermal scaling. The 0.00% match is not a numerical fit — it is the same operator at a different scale.
  - The match holds for Al, Pb, Nb, MgB$_2$.
  - Per the LIVING_REFERENCE.md Master Prediction Table classification note: this is an **"axiom manifestation"** (category ii), not a "derived prediction" (category iv).
- _Specific Non-Claims and Caveats_
  - The 0.00% in the prediction table does NOT mean a curve fit was performed.
  - Does NOT claim $B_{c,0}$ (the material-specific zero-temperature critical field) is derived from AVE. $B_{c,0}$ is taken as input per material.
  - Does NOT claim any of the four BCS materials' $B_{c,0}$ values are AVE-derived. Only the temperature dependence is the axiom manifestation.
  - "0.00%" or "Exact" entries elsewhere in the prediction table may belong to different classification categories (identity, axiom-manifestation, consistency-check, derived-prediction). Each row's classification matters; a global "AVE achieves 0.00% on N predictions" claim collapses meaningful distinctions.

> **Leaf references:** Vol 3 condensed-matter / superconductor leaves; Axiom 4 statement leaves in `vol1/`.
```

## 9. Compactness Budget

Vol 3 (highest-density tripwire volume) is the pilot. Target: under ~500 lines for `vol3/claims-boundaries.md`.

This is a **validation criterion, not a hard cap**. If exceeded materially, the architecture decision (sidecar vs per-subtopic embedded sections) needs revisiting. Within the budget, the architecture is validated; the same approach scales to other volumes.

## 10. Followups Discipline

Any issue surfaced during sidecar authoring or directive placement that is outside the dispatch's stated scope gets appended to `AVE-Core/kb-claims-boundaries-followups.md` (created on first surfacing). Do **not** fix inline. Do **not** expand dispatch scope.

Followups format (one H2 entry per issue):

```markdown
## YYYY-MM-DD — [short title]

- **Surfaced by:** [agent name + dispatch number]
- **Location:** [file:line or area]
- **Description:** [what was found]
- **Recommended owner:** [agent type or role]
- **Severity:** [low / medium / high]
```

## 11. Out-of-Scope Items (deferred for separate execution)

These are part of the broader plan but live outside `AVE-Core/`:

- All `.claude/agents/*.md` edits (KB-touching agents and MAD-side agents) — separate repo.
- Standing statement insertions in 9 agent definitions — separate repo.
- Boundaries Mode codification in `kb-content-distiller.md` — separate repo (was deferred anyway in the plan as Dispatch 13).
- Any updates to `mad-review/kb-claims-boundaries-plan.md` reflecting the AVE-Core-only scope reduction — separate repo.

The in-document directives + sidecars in this scope still deliver the primary mechanism; the agent-side backstop is an additional safety layer that can be added later without reworking what's done here.
