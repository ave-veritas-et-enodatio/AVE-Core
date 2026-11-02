# Electron-identity — LaTeX + README follow-ups (end of epic)

**Status:** RUNNING TRACKER. Unblocked by Checkpoint 2 (2026-08-18). Not a live dispatch in this PR.
**Opened:** 2026-08-16
**Gated on:** lifted 2026-08-18. First F-row after Grant dispatches. Do not start reads in this PR.
**Epic:** `_orchestration/2026-08-14_electron-identity.md`

ELECTRON-IDENTITY-LATEX-README-FOLLOWUPS-ANCHOR: one full LaTeX+README read per KB deprecation, end of epic.

Grant 2026-08-16: Phase C stays KB-only. LaTeX volumes and READMEs are **end-of-epic follow-ups**. This file is the running list: **each KB deprecation is one follow-up**, and that follow-up's work is a **full read of every LaTeX document** (then the README set) for *that corpse only*. Grep may index; grep does not discharge a row.

---

## How this tracker runs

1. **Seed (this commit).** One row per Phase A ledger C-row (C1–C10). Status **QUEUED** — the KB banner has not landed.
2. **When Phase C banners a C-row (or a new KB live-wrong site).** Flip that follow-up to **PENDING-READ**. If Phase C adds a deprecation that is not already a row, **append a new F-row** (do not fold it into an existing corpse). This is what "running" means. **2026-08-16:** C1–C10 banners landed; F-C1…F-C10 → PENDING-READ. No new C-row beyond the seed.
3. **Discharge.** One implementor pass per F-row — **superseded 2026-08-18 (Wave-2 D7-A): one combined pass covers every open F-row at once**; method in *Discharge protocol — COMBINED PASS* below. Hits classified live-wrong / Q1 / fence-excluded. Live-wrong LaTeX/README sites get their own Type D banners in a **later** PR, not in Phase C.
4. **Do not start these reads in the Checkpoint 2 PR.** Gate lifted 2026-08-18. First F-row after Grant dispatches, unless Grant says otherwise.

**Not in this tracker:** engine code (`src/`), L3 archive bodies, research result docs (Q2), Poincaré cohesion, cosmic node-injection, Layer-8 / derive-\(\{m_e,\alpha,G\}\). Homonyms: \(\Gamma=-1\)/\(V_{\mathrm{yield}}\) *boundary* self-trap is the surviving localizer; cosmological lattice-genesis is the held-out K3 amend.

---

## Read universe (listing 2026-08-16, tree `7b2a5919`)

**LaTeX documents — 166 files.** Chapters, volume mains, frontmatter, backmatter, `common/`, `common_equations/`, `structure/`. Figure/circuit TikZ snippets are **out** (not documents).

```bash
git ls-files 'manuscript/**/*.tex' | rg -v '/figures/|/circuits/' | wc -l
# → 166  (tree 7b2a5919, 2026-08-16)
# by manuscript/ subtree (git ls-files | awk -F/ '{print $2}' | uniq -c):
#   ave-kb 2 · backmatter 11 · common 10 · common_equations 10 ·
#   frontmatter 3 · structure 2 · vol_0_engineering_compendium 6 ·
#   vol_1_foundations 12 · vol_2_subatomic 16 · vol_3_macroscopic 28 ·
#   vol_4_engineering 15 · vol_5_biology 7 · vol_6_periodic_table 21 ·
#   vol_9_vacuum_datasheet 23
```

**READMEs — 9 program-facing files.** `data/` and `research/_archive/` READMEs are out (Q2 / data kits).

```bash
git ls-files '*README.md' | rg -v '^data/|^research/_archive/'
```

`README.md` · `_orchestration/README.md` · `_orchestration/docket-entries/README.md` · `_orchestration/open-items/README.md` · `assets/3d_models/kit/README.md` · `manuscript/ave-kb/README.md` · `src/ave/viz/README.md` · `templates/lab-notebook/README.md` · `viz/README.md`

Re-run both listings at discharge time. If the count moved, update this section in the same PR as the first F-row that uses the new count.

**Combined pass 2026-11-01 — pass header.** Base `cbc668e7219ec8a8b13407da7a7a33ed622ad95b` (fetched once; no rebase; every path:line in the Hits below is at that SHA). Listing re-run at that SHA: **166 LaTeX + 11 READMEs = 177 documents**. Row set: **F-C1 … F-C11** (eleven rows, none added). Read receipt: `_orchestration/2026-11-01_electron-identity-read-receipt.tsv`. Corpus conflicts and `Seeds outside the row set`: `_orchestration/2026-11-01_electron-identity-combined-pass-conflicts.md`.

The README listing moved from 9 to 11 since tree `7b2a5919`. The two additions are `research/drivers/data/p2_scoping/README.md` and `src/tests/data/README.md`, both data-kit files the `^data/` filter misses only because of their path depth, so the "9 program-facing files" line above does not describe them. Both were read, because the listing is binding (protocol item 2); whether they stay in the universe is Grant's question, raised in the pass PR.

Class values in the receipt and Hits: live-wrong, Q1, Q2 and fence-excluded are protocol classes. `none`, `unsure` (printed here as *unsure — not picked*) and `reader-call` are DISPATCH-GLOSS. Every hit was re-classified at source by an independent checker, and every site a reader or checker called live-wrong or unsure went to three independent judges (corpse match, fence, currency). A site is recorded live-wrong only if the checker and at least two judges agree; a contested site stays *unsure — not picked*. No hit is left at `reader-call`.

---

## Discharge protocol — COMBINED PASS (ruled 2026-08-18, Wave-2 D7-A)

**Grant 2026-08-18 (D7-A).** F-row discharge is **one combined read pass** over the whole 175-document universe, producing a **per-row hit ledger for every open F-row at once** — not one full-universe pass per corpse. Nothing frozen on 2026-08-16 is relaxed: the reads are still **full-document** reads of the **whole listing**, never subsampled by "likely volumes"; **grep may index, grep never discharges a row**; each row keeps **its own fence**; and the **per-row hit ledger stays the discharge artifact**. What is shared is the *reading*, not the *ledger* — one traversal of the corpus, every row's corpse-filter applied to each document as it is read.

**Arithmetic.** Solo-pass rule as written: 11 F-rows × (166 LaTeX + 9 README) = **1,925** full-document reads. Combined pass: **175** full-document reads — one per document, with one classification per row recorded per document. Same evidence, the ~11× duplication removed.

### What one pass is

1. **Scope.** A pass covers **the F-row set open when the pass starts**. At ruling time that set is **F-C1 … F-C11** (eleven rows — F-C11 was appended 2026-08-17 and is in the set). The pass states its row set explicitly in its own header; a pass with an unstated row set discharges nothing.
2. **Universe.** The pass reads the full listing from **Read universe** above — re-run both `git ls-files` commands at pass start, and if a count moved, update that section in the pass's own PR. **A pass is valid only if its read log covers the full universe listing.** A pass whose log falls short of the listing discharges **no** row, however many hits it found.
3. **Reading.** Each document is read **in full, once**, and classified against **every** row in the pass's set inside that single read: for each row, is that corpse offered as *current*, named as dead (Q1), or fence-excluded (Poincaré / cosmic genesis / boundary self-trap / calibration inputs)? Fences stay **per row** — clearing one row's fence says nothing about another's.
4. **Deliverable.** One **Hits** ledger section per row in the set, appended under that row, with the **same fields as before**: path · verbatim fragment · why-current (live-wrong / Q1 / fence-excluded), plus the live-wrong / Q1 / fence-excluded counts.
5. **Zero-hit rows.** A row with **no hits in the pass** closes on the **pass's read receipt** — "read log covers the full 175-document listing; 0 hits for this corpse" — and flips to DONE. Silence out of a complete full-document read is evidence; silence out of a grep is not.
6. **Flip.** Each row in the pass's set flips to **DONE** when its ledger section lands. Do not banner in the read PR unless Grant says the read-and-banner may share a PR.

### Rows that arrive after a pass

A Phase-C banner (or later KB audit) that lands **after** a pass has started **appends its F-row and waits for the next combined pass**. It does **not** trigger a fresh solo full-universe read, and it is **not** back-fitted into a finished pass's ledger — that pass's reader was not carrying the new corpse-filter, so its read receipt cannot speak for the new row. One new row is a reason to schedule the next pass, not a reason to re-read the corpus alone.

`verify-before-cite` on every live-wrong fragment. `ave-walk-back` Q1/Q2 on the classification. Both unchanged.

---

## Discharge protocol (every F-row)

> **Superseded 2026-08-18** by the combined-pass protocol above (Wave-2 ruling D7-A); body preserved (Rule 12) — every frozen requirement below still binds, only the one-full-universe-pass-per-row *scoping* is replaced.

For **this corpse only** (the verbatim fragment + K# in the row):

1. List the 166 LaTeX documents (command above). That list is the work. Do not subsample by "likely volumes."
2. **Read each file in full.** A grep hit-list is an index, not a substitute. Record: path, whether the corpse is offered as *current*, Q1 (named as dead), or fence-excluded (Poincaré / cosmic genesis / boundary self-trap / calibration inputs).
3. Read each of the 9 READMEs the same way.
4. Append a **Hits** subsection under the F-row: live-wrong (to banner later) / Q1 / fence-excluded counts, with path + fragment for every live-wrong.
5. Flip the F-row to **DONE**. Do not banner in the read PR unless Grant says the read-and-banner may share a PR.

`verify-before-cite` on every live-wrong fragment. `ave-walk-back` Q1/Q2 on the classification.

---

## Follow-ups (one per KB deprecation)

Seeded from `_orchestration/2026-08-14_electron-identity-kill-list-ledger.md` §2. Status was **QUEUED** until the matching Phase C banner existed; **2026-08-16** all ten are **PENDING-READ**.

### F-C1 — K1 dynamical lock as AVE answer-candidate

| | |
|---|---|
| **KB deprecation** | C1 · `manuscript/ave-kb/common/the-abandoned-interior.md:65,:78` |
| **Corpse** | *"The AVE answer-candidate … the lock is the MOTION"* / three-part dynamic lock / snap channel UNRESOLVED |
| **Fence** | Banner the **lock clause only**. Poincaré Thread B on the same KB page is held out — do not treat LaTeX Poincaré-stress history as this corpse. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 2 · unsure — not picked 0.

- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:75` · `which is why the mass channel binds without the $S \to 0$ runaway firing.` · Printed current claim of why the mass channel binds. No lock, motion or remanence wording, and the T_2 cage is boundary form, so row text does not settle whether this is K1 binding.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:16` · `the Poincar\'e stress required to stabilize the charge` · Fence: LaTeX Poincare-stress history is not this corpse. The site lists it as a historical difficulty of the electromagnetic-mass program; no dynamical-lock clause appears in these documents.

### F-C2 — K1 lock as live-threat candidate

| | |
|---|---|
| **KB deprecation** | C2 · `manuscript/ave-kb/common/physics-lineage-map.md:302` |
| **Corpse** | *"candidate = dynamical lock … graded HYPOTHESIS-class"* under a live-threat column |
| **Fence** | Same clause-not-page rule. LaTeX that names Poincaré cohesive stress as the *named hole* is not this corpse. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 1 · unsure — not picked 0.

- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:16` · `the Poincar\'e stress required to stabilize the charge` · Fence: same clause-not-page rule; Poincare stress named as a hole is not this corpse. No lock candidate or live-threat column at the site.

### F-C3 — K5+K1 LOOP GAP doctrine as current routing aid

| | |
|---|---|
| **KB deprecation** | C3 · `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` (whole leaf) |
| **Corpse** | *WHEN TO USE: … scoping v11+ engine work*; advance ranks; platform ACTIVE; remanence rank-4; v11 ordered upgrades |
| **Fence** | Ranks as *historical traveler* may remain. This follow-up hunts ranks / v11+ / remanence offered as **current manufacture path**. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 0 · unsure — not picked 0.

### F-C4 — K1+K5 remanence as open route to mass

| | |
|---|---|
| **KB deprecation** | C4 · `manuscript/ave-kb/common/substrate-hysteresis-index.md:155,159` |
| **Corpse** | *"The LOOP GAP remains open until … remanence/coercivity/loop-area to mass"* + v11 charter / P11 |
| **Fence** | Anhysteretic-kernel *fact* (Level-1 has no loop area) is not the corpse. The corpse is remanence as the **live path that holds the electron**. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 7 · unsure — not picked 0.

- **fence-excluded** · `manuscript/backmatter/06_spice_verification_manual.tex:148` (also :81, :145, :182, :398) · `elastically---the hysteresis loop has zero enclosed area.` · Fence: the anhysteretic fact is not the corpse. Zero enclosed loop area at SPICE frequencies; the memristor is described with no claim that remanence holds the electron.
- **fence-excluded** · `manuscript/backmatter/appendix_c_derived_numerology.tex:36` · `Converting the localized Kinetic Yield Point into continuous structural strain dictates exactly how Non-Volatile Soliton Kinks (Chapter 8) are permanently packed.` · Permanent hold of a soliton reads like persistence at zero drive, but the hold is geometric packing in a Vol 4 logic element; neither remanence nor the electron is named.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_5.tex:167` *(comment, not printed)* · `genesis-written flux likewise persists with no drive, preserved by the derived` · Comment electret analogy: genesis-written flux persists with no drive, the row's zero-drive cue. It credits the conservation leg, not remanence, and frames no open route. Comment-only, so unsure.

### F-C5 — K1+K3+K5 manufacture = energize-lock + remanence

| | |
|---|---|
| **KB deprecation** | C5 · `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:123,127` |
| **Corpse** | *"Electron manufacture requires … energize-lock, and Level-2 remanence … v11 targets P11"* |
| **Fence** | Vol 9 datasheet circuit models that describe *walls / M,Q,J* without selling genesis-cook are not this corpse. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 0 · unsure — not picked 1.

- **unsure — not picked** · `manuscript/backmatter/appendix_c_derived_numerology.tex:41` · `When the geometry is driven to hold $\phi > \pi/3$, the internal node connections cross the Axiom 4 limit, physically generating the stable topological knot.` · Driving the lattice past the Axiom-4 limit to generate a stable knot resembles energize-then-lock genesis, but the section's object is a Vol 4 Chapter 8 logic kink; electron unnamed. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*

### F-C6 — K1 remanence as OPEN R10 capability gap

| | |
|---|---|
| **KB deprecation** | C6 · `manuscript/ave-kb/common/engine-capability-map.md:32,67,82,112,127` |
| **Corpse** | Remanence / constitutive loop as the **open** retention mechanism the engine must still close |
| **Fence** | Do not banner "kernel is anhysteretic" as killed physics. Banner remanence-as-current-hold. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 5 · unsure — not picked 1.

- **unsure — not picked** · `manuscript/common_equations/eq_axiom_5.tex:167` *(comment, not printed)* · `genesis-written flux likewise persists with no drive, preserved by the derived` · Same electret comment: a retention statement, credited to the conservation leg rather than a constitutive loop, with no engine gap named. Comment-only and not settled by the row text. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/06_spice_verification_manual.tex:148` (also :81, :145, :182, :398) · `elastically---the hysteresis loop has zero enclosed area.` · Fence: do not banner anhysteretic behaviour. 'Documented but not implemented' names an unbuilt SPICE term, not remanence as the open retention mechanism for the electron.

### F-C7 — K2+K3 precursor → self-trap build order

| | |
|---|---|
| **KB deprecation** | C7 · `manuscript/ave-kb/common/engine-capability-map.md:109` |
| **Corpse** | *"seed photon precursor → self-trap"* as staged-growth construction path |
| **Fence** | Boundary \(\Gamma=-1\) self-trap (surviving localizer) is **not** this corpse. Hunt **bulk** self-trap / free-precursor seed offered as current. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 1 · Q1 0 · Q2 0 · fence-excluded 11 · unsure — not picked 2.

- **live-wrong** · `manuscript/common_equations/eq_axiom_2.tex:33` · `the formation-route (genesis of a winding from a free precursor) remains open.` · Fence hunts free-precursor seed offered as current, and this frames free-precursor formation as open. No self-trap or staged build order appears, so the row text does not settle it. *[lens live-wrong 2, unsure 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_4.tex:42` · `Wave packet confined (mass)` · Printed table: c_eff to zero at saturation reads as wave packet confined, labelled mass, which is bulk self-confinement offered as current. No precursor or build order; footnote :47 leaves branch ontology open. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:10` · `proposed as the carrier of rest mass ($m_e c^2$ as trapped longitudinal compression energy)` · Reads as bulk trapping, but states no build order or trap mechanism. Line stamp says NEEDS RE-DERIVATION, not dead, so Q1 fails and the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/01_appendices.tex:80` · `$\Gamma \to -1$\gammaundeclared{} --- the short-circuit / TIR wall that \emph{confines} the electron, not a match.)}` · Boundary Gamma -> -1 TIR wall from dielectric saturation that confines the electron. F-C7 Fence: boundary Gamma=-1 self-trap is the surviving localizer, not bulk self-trap or free-precursor seed.
- **fence-excluded** · `manuscript/backmatter/05_universal_solver_toolchain.tex:599` · `The electron is an impedance mismatch ($\Gamma=-1$\gammaundeclared{}) that traps a longitudinal wave, bouncing at $E=V(r)$.` · Trap is stated as a Gamma=-1 impedance mismatch, the boundary self-trap the Fence keeps as surviving localizer. No precursor seed or staged build order appears.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:55` · `The confining $\Gamma = -1$\gammaundeclared{} wall is the transverse Cosserat ($T_2$) self-trap at $V_{yield}$` · Fence: boundary Gamma = -1 self-trap is the surviving localizer, not this corpse. This is the V_yield wall form, not bulk self-trap or free-precursor seed.
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:70` (also :17, :75) · `the \textbf{transverse Cosserat $T_2$ self-trap wall} --- the electron's confining $\Gamma = -1$\gammaundeclared{}` · Fence: boundary Gamma = -1 / V_yield self-trap is the surviving localizer, not this corpse. The header names the electron's confining wall in that form.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:95` (also :16, :87, :97) · `the boundary totally reflects substrate waves outside and totally traps them inside` · Fence: boundary Gamma=-1 self-trap is the surviving localizer, not this corpse. No bulk self-trap or precursor seed stated at these sites.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Fence clears boundary Gamma=-1 self-trap, but its hunt clause names free-precursor seed, and here propagating modes are what gets confined at that boundary. Row does not settle the combination.

### F-C8 — K1+K2 capability-matrix YAML

| | |
|---|---|
| **KB deprecation** | C8 · `manuscript/ave-kb/common/figures/engine_capability_matrix.yaml:31,39` |
| **Corpse** | *"rest mass = self-trapped LONGITUDINAL-bulk wall"* + *"constitutive loop (remanence)"* with no banner channel |
| **Fence** | Same homonym as F-C7. LaTeX that copies this YAML prose as current capability is in scope. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 11 · unsure — not picked 3.

- **unsure — not picked** · `manuscript/common_equations/eq_axiom_4.tex:42` · `Wave packet confined (mass)` · Mass as confinement at saturation resembles rest mass = self-trapped bulk. No longitudinal wall or copied YAML prose, and :55 puts the mass core sub-saturated. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:10` · `proposed as the carrier of rest mass ($m_e c^2$ as trapped longitudinal compression energy)` · Close to rest mass = self-trapped longitudinal-bulk wall, minus self and wall. Stamp reads DEMOTED, NEEDS RE-DERIVATION, not dead, so it is neither named dead nor plainly offered as current. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:230` *(comment, not printed)* · `longitudinal compression energy' consume the propagating reading; re-labeling to real-and-bound` · Unprinted R40 note quoting the line 10 clause as consuming the propagating reading. A demotion audit, not a kill, and line 10 says not dead. Comment-only site. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/01_appendices.tex:80` · `$\Gamma \to -1$\gammaundeclared{} --- the short-circuit / TIR wall that \emph{confines} the electron, not a match.)}` · F-C8 Fence names the same homonym. This is the boundary Gamma -> -1 wall; the site does not copy the YAML prose and says nothing of a LONGITUDINAL-bulk wall or remanence.
- **fence-excluded** · `manuscript/backmatter/05_universal_solver_toolchain.tex:599` · `The electron is an impedance mismatch ($\Gamma=-1$\gammaundeclared{}) that traps a longitudinal wave, bouncing at $E=V(r)$.` · The F-C7 homonym fence covers Gamma=-1, but the row also prints 'Acoustic Bulk Modulus Cavity' and a trapped longitudinal wave, echoing the YAML's longitudinal-bulk wall. Row text does not settle which reading holds.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:55` · `The confining $\Gamma = -1$\gammaundeclared{} wall is the transverse Cosserat ($T_2$) self-trap at $V_{yield}$` · F-C8 Fence is the same homonym as F-C7: this is the boundary Gamma = -1 V_yield wall, stated as transverse, not the longitudinal-bulk wall.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:55` · `trapped acoustic-compression energy; \texttt{def-vyvsn1}, PR\,\#260)` · Longitudinal A1 energy called trapped resembles the YAML mass clause, but the wall here is transverse, mass = A1 stands, and the stamp reads NEEDS RE-DERIVATION, not dead. Row text does not settle it.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:105` *(comment, not printed)* · `trapped acoustic-compression energy; \texttt{def-vyvsn1}, PR\,\#260)` · Comment re-quotes :55 in the R40 demotion note: acoustic label consumes the wave reading, mass = A1 survives, no signed kill named. Same open question as :55.
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:64` (also :16) · `\noindent\textbf{Dielectric Snap Voltage} (per Axiom 4; the \textbf{longitudinal A1 dilatation} saturation / rest-energy scale, $m_e c^2$;` · Calibration input, outside every row per the hit rules: V_snap is the m_e c^2 scale and mass = A1 stands. No self-trap or wall is claimed for the longitudinal sector.
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:70` (also :17, :75) · `the \textbf{transverse Cosserat $T_2$ self-trap wall} --- the electron's confining $\Gamma = -1$\gammaundeclared{}` · F-C8 Fence is the same homonym as F-C7: boundary Gamma = -1 wall at V_yield, stated as transverse, not a longitudinal-bulk wall.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Fence: same homonym as F-C7. Rest mass here comes from Gamma=-1 confinement, not a longitudinal-bulk wall, and no YAML capability prose is copied.

### F-C9 — K3 (2,3) self-assembly as remaining gate

| | |
|---|---|
| **KB deprecation** | C9 · `manuscript/ave-kb/common/historical-precedents.md:56` |
| **Corpse** | *"full `(2,3)` self-assembly … localized remaining gaps"* / graduation gated on self-assembling |
| **Fence** | Cosmic node-injection is held out. Static Link / tank (2,3) **stands**. Hunt self-assembly as a **live manufacture path**, not the winding as charge. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 1 · Q1 0 · Q2 0 · fence-excluded 9 · unsure — not picked 4.

- **live-wrong** · `manuscript/frontmatter/00_foreword.tex:16` · `Whether the electron self-assembles in this form is an open question examined in the volumes; here it is stated as a model, not a result.` · Frames electron self-assembly as an open question examined in the volumes. Not named dead, so the ambiguity default applies. Fence holds the static winding, not self-assembly as a live path. *[lens live-wrong 3]*
- **unsure — not picked** · `manuscript/backmatter/01_appendices.tex:311` · `In a fully emergent physical engine, mass states must generate dynamically from raw local topological configurations; relying upon static hard-coding prevents fluid lattice topology interactions.` · Engine spec says mass states must generate dynamically instead of being spawned; lines 313-319 then read mass off a knot. Row text does not settle whether this is self-assembly as a live path. Not picked. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:56` · `K4 lattice + soliton formation` · Soliton formation printed as a kernel event could read as particle self-assembly, but no (2,3) or manufacture path is named. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_2.tex:33` · `the formation-route (genesis of a winding from a free precursor) remains open.` · Winding genesis framed as open reads like the remaining self-assembly gate, as a path not as charge. No self-assembly wording or graduation gate at the site; same mechanism not certain. *[lens unsure 2, live-wrong 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Headed Particle Assembly and offered as settled with no banner, but this is field-driven confinement and the row's corpse is self-assembly as a remaining gate. Row text does not settle it. *[lens unsure 3]*
- **fence-excluded** · `manuscript/backmatter/02_full_derivation_chain.tex:827` (also :767) · `latent heat of node generation conceptually balances the holographic thermal` · Latent heat of cosmic node generation in the G/H_infinity argument; no electron or winding is formed. F-C9 Fence: cosmic node-injection is held out.
- **fence-excluded** · `manuscript/backmatter/03_geometric_inevitability.tex:554` (also :563) · `\textbf{Cosmic} K4 crystallization (TKI strain-snap mechanism` · Same cosmic lattice crystallization; the row's Fence holds out the cosmic item. No (2,3) winding or particle self-assembly is offered here.
- **fence-excluded** · `manuscript/backmatter/07_universal_saturation_kernel.tex:87` (also :216, :226, :230) · `K4 crystallization seed event` · Same cosmic lattice seed event; the row's Fence holds out the cosmic item. No (2,3) self-assembly is offered.
- **fence-excluded** · `manuscript/common/translation_cosmology.tex:27` · `Parent-BH strain on the pre-bond state (gloss \emph{pre-geodesic}; R9 rename 2026-08-06) triggers K4 crystallization seed event` · Cosmic lattice crystallization, not (2,3) self-assembly as a manufacture path. F-C9 Fence: cosmic node-injection is held out; tracker scope holds out cosmological lattice-genesis as the K3 amend.

### F-C10 — K5 common index still advertises the doctrine

| | |
|---|---|
| **KB deprecation** | C10 · `manuscript/ave-kb/common/index.md:63` |
| **Corpse** | Index blurb: ranked plumber order, three genesis lanes, v9–v15 directions, no superseded marker |
| **Fence** | A LaTeX TOC entry that merely *names* the LOOP GAP leaf is not live-wrong unless it offers ranks as current work. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 0 · unsure — not picked 0.

### F-C11 — K3 formation-route still "remains open" on the axiom leaf

| | |
|---|---|
| **KB deprecation** | Audit 1 · `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:33` |
| **Corpse** | *"the formation-route (genesis of a winding from a free precursor) remains open"* |
| **Fence** | Cosmic node-injection is held out. Charge = winding dictionary and the engine-derived interaction leg are **not** this row. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 6 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 3 · Q1 0 · Q2 0 · fence-excluded 18 · unsure — not picked 7.

- **live-wrong** · `manuscript/common_equations/eq_axiom_2.tex:33` · `the formation-route (genesis of a winding from a free precursor) remains open.` · Verbatim the corpse inside the printed Axiom 2 resultbox: free-precursor winding genesis framed as open, no banner at the site. The Fence clears the dictionary and interaction leg, not this clause. *[lens live-wrong 3]*
- **live-wrong** · `manuscript/frontmatter/00_foreword.tex:16` · `Whether the electron self-assembles in this form is an open question examined in the volumes; here it is stated as a model, not a result.` · Leaves formation open, matching remains open, but names no free precursor, so the row's parenthetical route is not explicit here. The plain self-assembly reading is carried under F-C9. *[lens live-wrong 2, unsure 1]*
- **live-wrong** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Propagating modes confined into the wound electron, generating rest mass, is genesis from a free precursor printed as standing physics with no banner. This row's fence holds only cosmic injection, charge dictionary and interaction leg. *[lens live-wrong 3]*
- **unsure — not picked** · `manuscript/backmatter/06_spice_verification_manual.tex:112` · `A1 mass core has completed)` · Exceeding V_snap is said to complete an A1 mass core, a drive-to-threshold formation reading in a numerical-guard note. No free precursor named; row text does not settle whether this is the corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:54` · `Dielectric breakdown $\to$ pair creation` · Saturation leading to pair creation is a formation event printed as canonical, not framed as open. No free precursor is named and K3's pair-production item is flagged, so the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:56` · `K4 lattice + soliton formation` · Catalog lists soliton formation as a saturation event at substrate scale, offered as canonical. No free precursor or 'remains open' wording; row text does not settle whether this is the formation-route corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:168` · `creation as the topological reorganization.` · Body note to the same catalog row: breakdown triggers pair creation as the reorganization, stated as standing. Formation event without a named free precursor; row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/appendix_c_derived_numerology.tex:41` · `When the geometry is driven to hold $\phi > \pi/3$, the internal node connections cross the Axiom 4 limit, physically generating the stable topological knot.` · Present-tense formation of a stable knot, not framed as open. No free precursor and no electron named; cosmic-injection fence does not apply. Row text does not settle whether this is the corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_5.tex:71` · `The genesis mechanism is a named-open entry of the genesis phase (phase map below) --- this clause neither supplies one nor licenses one.` · Prints the genesis mechanism as named-open but explicitly supplies none. It says neither free precursor nor cosmic node-injection, so row text does not settle corpse versus Fence. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_5.tex:98` · `\textbf{(c2)} the \textbf{genesis-phase} law that writes clause S's flux (the deposit is data, not a derivation).` · Genesis-phase law listed as a named-open hole for clause S flux. Flux rather than winding, and no free precursor named; row text does not settle corpse versus cosmic Fence. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/02_full_derivation_chain.tex:827` (also :767) · `latent heat of node generation conceptually balances the holographic thermal` · Cosmic node generation in the G/H_infinity argument, not a winding from a free precursor. F-C11 Fence: cosmic node-injection is held out.
- **fence-excluded** · `manuscript/backmatter/03_geometric_inevitability.tex:554` (also :563) · `\textbf{Cosmic} K4 crystallization (TKI strain-snap mechanism` · Cosmological lattice genesis, not electron minting. The row's Fence holds out cosmic node-injection and the tracker scope line holds out cosmological lattice-genesis.
- **fence-excluded** · `manuscript/backmatter/04_physics_engine_architecture.tex:164` · `utils/ 4 mods: winding extractor, genesis runner, genus, v8 instr.` · Printed inventory names a genesis runner as present tooling; 04:85 scopes the tree as inventory, not physics. Naming a tool may or may not offer genesis as current; row text does not settle it.
- **fence-excluded** · `manuscript/backmatter/07_universal_saturation_kernel.tex:87` (also :216, :226, :230) · `K4 crystallization seed event` · Cosmic K4 crystallization seed is lattice genesis with no electron minted; the row's Fence holds out the cosmic item and the tracker scope line names cosmological lattice-genesis as the held-out K3 amend.
- **fence-excluded** · `manuscript/common/translation_cosmology.tex:27` · `Parent-BH strain on the pre-bond state (gloss \emph{pre-geodesic}; R9 rename 2026-08-06) triggers K4 crystallization seed event` · A cosmic lattice seed event; it names no winding or free precursor. F-C11 Fence: cosmic node-injection is held out; tracker scope holds out cosmological lattice-genesis.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_2.tex:33` · `Axiom 2 thus carries both the charge \emph{dictionary} and a derived winding-pair \emph{interaction}` · Fence: charge = winding dictionary and the engine-derived interaction leg are not this row. Same line as the live-wrong clause; the finding scopes to that clause only.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:22` (also :16, :91) · `The \emph{interaction} between two such windings is engine-derived (2026-07-03)` · Fence: the charge = winding dictionary and the engine-derived interaction leg are not this row.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:35` (also :32, :41, :97) · `Lattice genesis (the framework's replacement for the Big Bang)` · Tracker homonym line: cosmological lattice-genesis is the held-out K3 amend. The site describes substrate crystallization, not electron formation from a precursor.

---

## New rows (append below; do not edit C1–C10 history)

Phase C (or a later KB audit) that banners a **new** live-wrong site adds `F-<id>` here, copies the verbatim fragment, states the fence, and starts at QUEUED.

---

## Census (update when a row flips)

| Status | F-rows | Listing |
|---|---:|---|
| QUEUED | 0 | — |
| PENDING-READ | 11 | F-C1 … F-C11 (KB banners landed 2026-08-16; F-C11 Audit 1 residue 2026-08-17; eleven `### F-C` headings) |
| DONE | 0 | — |

Census 2026-08-16 Phase C: **0 QUEUED / 10 PENDING-READ / 0 DONE**. Do not start these reads until Checkpoint 2.

Census 2026-08-18 Checkpoint 2: still **0 QUEUED / 11 PENDING-READ / 0 DONE**. Gate lifted. Do not start these reads in this PR.
