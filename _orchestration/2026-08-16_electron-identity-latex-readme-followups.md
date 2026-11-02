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

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 4 · unsure — not picked 13.

- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:200` · `A subatomic particle in this model is a stable, self-sustaining acoustic standing wave trapped inside a spherical $0 \ \Omega$ impedance boundary of its own geometric creation.` · Stated as the current model: motion sustaining its own boundary resembles the lock-is-the-motion clause. The word lock is absent and no Poincare framing is involved, so the corpse match is undecided. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:218` · `Maintaining this structural lock requires sustained threshold energy (the $43.65$ keV structural yield limit derived in Volume III, Chapter 1).` · Current definition of what holds the electron: a lock needing sustained energy. The line calls it geometric and structural, not motion or three-part, and no banner names it dead. Row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/05_universal_spatial_tension.tex:18` · `localized structural loops must store reactive energy to remain stable` · Stability is attributed to stored reactive energy, close to K1 reactive LC-binding. No lock, motion or candidate language; this generic statement does not settle it as the dynamical-lock corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:13` · `localised, self-sustaining topological soliton of confined electromagnetic waves` · Self-sustaining confined waves is the chapter's opening identity. It could be the dynamic lock in other words, but no lock mechanism is named, so the row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:40` · `feed into each other in a closed topological loop ($\nabla \times \mathbf{A} = k\mathbf{A}$), permanently trapping the energy` · E/B mutual feed permanently trapping energy reads as motion-holds-it (K1 reactive LC-binding), with no banner. The row's corpse wording (answer-candidate, three-part lock) does not appear, so live-wrong is not forced. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:152` · `drilled and held open by the $(2,3)$ Cosserat circulation, and closed by the surface tension of the void--vacuum boundary` · Circulation holding the cavity open resembles lock-as-motion, but the site is Class-C and :167 says it is not why the electron exists. Not the Poincare thread, so the fence does not decide it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:248` · `The localised inductive energy, previously trapped within the closed LC resonance of the Hopfion, unwinds.` · Energy trapped in a closed LC resonance, released when a boundary condition snaps, resembles the K1 lock and snap channel. The site is annihilation, not a claim about what holds the electron. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:259` · `The discrete sequential excitation of the substrate LC nodes guarantees charge containment` · Sequential node excitation guaranteeing containment is a motion-based hold in an unbannered caption. The row text does not say whether this is the dynamic lock. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:402` · `visualized as a "breathing mode" that maintains the particle's existence against vacuum decay` · Lossless energy cycling that maintains existence is lock-as-motion, but the subject is the He-4 nucleus, not the electron. The row text does not say whether it reaches nuclei. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:138` · `the resulting topologies phase-lock into their lower-energy states (Proton, Electron, and the transverse recoil acoustic wave/Neutrino)` · An electron state 'phase-locks' after the beta-decay arc. This may be the K1 lock or ordinary relaxation; no motion-as-lock or hold mechanism is stated, so the row text does not settle it. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:104` · `is the same LC phase-locking condition that defines the electron unknot` · An LC phase-locking condition is said to define the electron unknot, with no dead marker. The row does not settle whether this orbital standing-wave condition is the K1 lock. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/08_planck_and_string_theory.tex:79` · `\textit{All} stable fundamental structures are closed topological knots consisting of purely continuous LC standing waves.` · Stability is tied to knots made of LC standing waves, adjacent to K1 reactive LC-binding, but no lock or binding mechanism is stated. The row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:415` · `a closed trajectory where the electromagnetic standing wave constructively self-reinforces` · Phase-locked, self-reinforcing wave, ten lines after 'every stable particle is' a standing wave, reads near 'the lock is the MOTION'. But it is the BSD rational-point mapping, with no hold claim. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:75` · `which is why the mass channel binds without the $S \to 0$ runaway firing.` · Printed current claim of why the mass channel binds. No lock, motion or remanence wording, and the T_2 cage is boundary form, so row text does not settle whether this is K1 binding.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:16` · `the Poincar\'e stress required to stabilize the charge` · Fence: LaTeX Poincare-stress history is not this corpse. The site lists it as a historical difficulty of the electromagnetic-mass program; no dynamical-lock clause appears in these documents.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:103` · ```The ``rest mass is contained reactance'' framing here``` · Contained reactance stays a live framing. K1 lists reactive LC-binding and :36 moves rest mass off the inductive store, but the row text names only the dynamic lock.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:3841` · `two orthogonal principal strain axes jointly stabilize any topological defect against Derrick-type collapse` · Printed as present-tense stabiliser against collapse. Not the motion lock; strain wording sits near the Fence's Poincaré hold-out without naming it. Row text does not settle which.

### F-C2 — K1 lock as live-threat candidate

| | |
|---|---|
| **KB deprecation** | C2 · `manuscript/ave-kb/common/physics-lineage-map.md:302` |
| **Corpse** | *"candidate = dynamical lock … graded HYPOTHESIS-class"* under a live-threat column |
| **Fence** | Same clause-not-page rule. LaTeX that names Poincaré cohesive stress as the *named hole* is not this corpse. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 1 · unsure — not picked 1.

- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/05_universal_spatial_tension.tex:18` · `localized structural loops must store reactive energy to remain stable` · Same sentence as the F-C1 record. Reactive storage is the stability condition, but stated flat, with no live-threat column or HYPOTHESIS grade. Row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:16` · `the Poincar\'e stress required to stabilize the charge` · Fence: same clause-not-page rule; Poincare stress named as a hole is not this corpse. No lock candidate or live-threat column at the site.

### F-C3 — K5+K1 LOOP GAP doctrine as current routing aid

| | |
|---|---|
| **KB deprecation** | C3 · `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` (whole leaf) |
| **Corpse** | *WHEN TO USE: … scoping v11+ engine work*; advance ranks; platform ACTIVE; remanence rank-4; v11 ordered upgrades |
| **Fence** | Ranks as *historical traveler* may remain. This follow-up hunts ranks / v11+ / remanence offered as **current manufacture path**. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 1 · unsure — not picked 0.

- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:109` · `for any field; the v14` · A v14 electron seed is given in present tense under Engine implementation, with no superseded marker. It is a receipt, not a stated manufacture path, and the row hunts v11+ only as a current path.

### F-C4 — K1+K5 remanence as open route to mass

| | |
|---|---|
| **KB deprecation** | C4 · `manuscript/ave-kb/common/substrate-hysteresis-index.md:155,159` |
| **Corpse** | *"The LOOP GAP remains open until … remanence/coercivity/loop-area to mass"* + v11 charter / P11 |
| **Fence** | Anhysteretic-kernel *fact* (Level-1 has no loop area) is not the corpse. The corpse is remanence as the **live path that holds the electron**. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 9 · unsure — not picked 0.

- **fence-excluded** · `manuscript/backmatter/06_spice_verification_manual.tex:148` (also :81, :145, :182, :398) · `elastically---the hysteresis loop has zero enclosed area.` · Fence: the anhysteretic fact is not the corpse. Zero enclosed loop area at SPICE frequencies; the memristor is described with no claim that remanence holds the electron.
- **fence-excluded** · `manuscript/backmatter/appendix_c_derived_numerology.tex:36` · `Converting the localized Kinetic Yield Point into continuous structural strain dictates exactly how Non-Volatile Soliton Kinks (Chapter 8) are permanently packed.` · Permanent hold of a soliton reads like persistence at zero drive, but the hold is geometric packing in a Vol 4 logic element; neither remanence nor the electron is named.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_5.tex:167` *(comment, not printed)* · `genesis-written flux likewise persists with no drive, preserved by the derived` · Comment electret analogy: genesis-written flux persists with no drive, the row's zero-drive cue. It credits the conservation leg, not remanence, and frames no open route. Comment-only, so unsure.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/06_universal_operators.tex:117` · ```\textbf{reversible saturation knee}: sub-yield, AVE ``yield'' means``` · Fence: the anhysteretic-kernel fact is not the corpse. The sub-yield kernel is declared reversible, with no retention and no claim on what holds the electron.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/06_universal_operators.tex:121` · `\textbf{retained-set sense only} (the retention row as written); the` · Regime-IV 'retained-set' and 'retention row' are licensed as current usage. The site names no electron and no hold, so the row does not settle whether this is remanence as the live path.

### F-C5 — K1+K3+K5 manufacture = energize-lock + remanence

| | |
|---|---|
| **KB deprecation** | C5 · `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:123,127` |
| **Corpse** | *"Electron manufacture requires … energize-lock, and Level-2 remanence … v11 targets P11"* |
| **Fence** | Vol 9 datasheet circuit models that describe *walls / M,Q,J* without selling genesis-cook are not this corpse. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 0 · unsure — not picked 2.

- **unsure — not picked** · `manuscript/backmatter/appendix_c_derived_numerology.tex:41` · `When the geometry is driven to hold $\phi > \pi/3$, the internal node connections cross the Axiom 4 limit, physically generating the stable topological knot.` · Driving the lattice past the Axiom-4 limit to generate a stable knot resembles energize-then-lock genesis, but the section's object is a Vol 4 Chapter 8 logic kink; electron unnamed. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:259` · `establishing the physical derivation of confined point-particles via continuum wave-crashing.` · The caption sells a genesis route, so the Vol 9 datasheet fence does not clear it, but energize-lock, remanence and v11 are all absent. The row text does not settle it. *[lens unsure 2, fence-excluded 1]*

### F-C6 — K1 remanence as OPEN R10 capability gap

| | |
|---|---|
| **KB deprecation** | C6 · `manuscript/ave-kb/common/engine-capability-map.md:32,67,82,112,127` |
| **Corpse** | Remanence / constitutive loop as the **open** retention mechanism the engine must still close |
| **Fence** | Do not banner "kernel is anhysteretic" as killed physics. Banner remanence-as-current-hold. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 6 · unsure — not picked 2.

- **unsure — not picked** · `manuscript/common_equations/eq_axiom_5.tex:167` *(comment, not printed)* · `genesis-written flux likewise persists with no drive, preserved by the derived` · Same electret comment: a retention statement, credited to the conservation leg rather than a constitutive loop, with no engine gap named. Comment-only and not settled by the row text. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/06_universal_operators.tex:121` · `\textbf{retained-set sense only} (the retention row as written); the` · Retention is licensed past V_snap beside an 'open yield fork'. That fork is the friction sense, not a named engine retention gap; row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/06_spice_verification_manual.tex:148` (also :81, :145, :182, :398) · `elastically---the hysteresis loop has zero enclosed area.` · Fence: do not banner anhysteretic behaviour. 'Documented but not implemented' names an unbuilt SPICE term, not remanence as the open retention mechanism for the electron.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/06_universal_operators.tex:117` · ```\textbf{reversible saturation knee}: sub-yield, AVE ``yield'' means``` · Fence: do not banner 'kernel is anhysteretic' as killed physics. This states the reversible kernel only and names no open engine retention gap.

### F-C7 — K2+K3 precursor → self-trap build order

| | |
|---|---|
| **KB deprecation** | C7 · `manuscript/ave-kb/common/engine-capability-map.md:109` |
| **Corpse** | *"seed photon precursor → self-trap"* as staged-growth construction path |
| **Fence** | Boundary \(\Gamma=-1\) self-trap (surviving localizer) is **not** this corpse. Hunt **bulk** self-trap / free-precursor seed offered as current. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 2 · Q1 0 · Q2 0 · fence-excluded 39 · unsure — not picked 12.

- **live-wrong** · `manuscript/common_equations/eq_axiom_2.tex:33` · `the formation-route (genesis of a winding from a free precursor) remains open.` · Fence hunts free-precursor seed offered as current, and this frames free-precursor formation as open. No self-trap or staged build order appears, so the row text does not settle it. *[lens live-wrong 2, unsure 1]*
- **live-wrong** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:259` · `A spatial solver demonstrating how a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop when encountering extreme localised network impedance ($Z \to Z_{crit}$).` · A free EM wave winding into a stationary loop is a free-precursor seed offered as simulation-established, with no banner. The Fence clears only the boundary Gamma=-1 self-trap, not this construction path. *[lens live-wrong 3]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_4.tex:42` · `Wave packet confined (mass)` · Printed table: c_eff to zero at saturation reads as wave packet confined, labelled mass, which is bulk self-confinement offered as current. No precursor or build order; footnote :47 leaves branch ontology open. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:10` · `proposed as the carrier of rest mass ($m_e c^2$ as trapped longitudinal compression energy)` · Reads as bulk trapping, but states no build order or trap mechanism. Line stamp says NEEDS RE-DERIVATION, not dead, so Q1 fails and the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:105` · `$Z_{bulk} \to 0 \Rightarrow \Gamma_{bulk} = -1$ at the bulk cage` · Bulk-cage confinement is stamped DEMOTED but 'NEEDS RE-DERIVATION, not dead', so not Q1. 'Bulk' may mean the modulus channel, not an interior well; the Gamma=-1 form is fenced. Row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:558` *(comment, not printed)* · `the |Gamma|=1 wall survive; the confinement-of-a-dilatation-wave mechanism plus signed Gamma and` · Comment rationale for the line 105 demotion. Says the dilatation-wave mechanism consumes the phantom, under a NEEDS-RE-DERIVATION header. Comment only; not named dead under K2. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:208` · `$\Delta\phi = \alpha$; self-confinement` · The table gives the electron mechanism as bare self-confinement at yield, naming neither boundary nor bulk. The F-C7 Fence clears only the boundary self-trap, so it cannot decide this. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:125` · `The transient kinetic energy is forced to condense into trapped inertial tensor inductance ($L$).` · Free kinetic energy condenses into trapped mass past yield in the bulk, but the caption's subject is W/Z arcs, not the electron. Neither the boundary fence nor the free-precursor clause clearly decides it. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:43` · `The atomic orbital is the precise radius where this trapped bulk-modulus acoustic wave achieves a lossless resonant impedance match with itself` · A bulk-modulus wave is called trapped, but reflection is at the Coulomb turning point on orbital scale, not the electron's own localizer. The row does not settle this. No DEMOTED tag on this line. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:491` · `The cavity that traps the electron forms from the defect's own` · The wording reads as self-trap by the electron's own dispersion, but the context is the Z_eff Coulomb orbital with no free precursor. The row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:633` · `Compton wavelength; this is the confinement radius` · Soliton confinement set by Axiom 4 is offered as current (continues on line 634). The row does not say whether this is the fenced boundary localizer or bulk self-trap. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:1022` · `The electron defect has a saturated core ($S \to 0$:` · A saturated core, called a liquid cavity, is offered as current electron structure. The Fence protects the boundary form; a core could be either, and the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:3821` · `Each electron saturates the lattice out to its confinement` · Saturation sets a confinement radius, printed as current, inside the p_c derivation (see also :3819). Text does not say bulk localizer or the Fence's boundary self-trap, so the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:702` · `quantises arbitrary continuous topological orbits into integer-wound standing wave particles` · Chapter summary: reflection turns orbits into wound particles, resembling precursor-to-trap. 'Impedance reflection' leans toward the boundary Fence; no seed or bulk stated. Not settled. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/01_appendices.tex:80` · `$\Gamma \to -1$\gammaundeclared{} --- the short-circuit / TIR wall that \emph{confines} the electron, not a match.)}` · Boundary Gamma -> -1 TIR wall from dielectric saturation that confines the electron. F-C7 Fence: boundary Gamma=-1 self-trap is the surviving localizer, not bulk self-trap or free-precursor seed.
- **fence-excluded** · `manuscript/backmatter/05_universal_solver_toolchain.tex:599` · `The electron is an impedance mismatch ($\Gamma=-1$\gammaundeclared{}) that traps a longitudinal wave, bouncing at $E=V(r)$.` · Trap is stated as a Gamma=-1 impedance mismatch, the boundary self-trap the Fence keeps as surviving localizer. No precursor seed or staged build order appears.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:55` · `The confining $\Gamma = -1$\gammaundeclared{} wall is the transverse Cosserat ($T_2$) self-trap at $V_{yield}$` · Fence: boundary Gamma = -1 self-trap is the surviving localizer, not this corpse. This is the V_yield wall form, not bulk self-trap or free-precursor seed.
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:70` (also :17, :75) · `the \textbf{transverse Cosserat $T_2$ self-trap wall} --- the electron's confining $\Gamma = -1$\gammaundeclared{}` · Fence: boundary Gamma = -1 / V_yield self-trap is the surviving localizer, not this corpse. The header names the electron's confining wall in that form.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:95` (also :16, :87, :97) · `the boundary totally reflects substrate waves outside and totally traps them inside` · Fence: boundary Gamma=-1 self-trap is the surviving localizer, not this corpse. No bulk self-trap or precursor seed stated at these sites.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Fence clears boundary Gamma=-1 self-trap, but its hunt clause names free-precursor seed, and here propagating modes are what gets confined at that boundary. Row does not settle the combination.
- **fence-excluded** · `manuscript/vol_0_engineering_compendium/chapters/01_theoretical_stress_tests.tex:86` · `drives $Z_{core} = Z_0\sqrt{S} \to 0$ and $\Gamma \to -1$\gammaundeclared{} --- the short-circuit / TIR wall that \emph{confines} the electron, not a match.` · F-C7 Fence: boundary Gamma=-1 self-trap is the surviving localizer, not this corpse. The site confines at a wall; it offers no bulk self-trap or free-precursor seed.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:166` · `the threshold where non-linear saturation effects become dominant and the soliton begins to self-confine.` · V_yield homonym suggests the boundary fence, but the line prints a staged onset of self-confinement and never says boundary or bulk. Row text does not settle it.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:169` · `The kinetic yield governs mass assembly and confinement;` · Prints assembly at a yield threshold as a current process. No photon precursor is named and no boundary or bulk is stated, so neither fence nor corpse is settled.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:200` (also :171, :181, :199, :411, :428) · `trapped inside a spherical $0 \ \Omega$ impedance boundary of its own geometric creation.` · Fence clause: boundary Gamma = -1 self-trap is the surviving localizer. The site confines at the 0-ohm saturated boundary, with no bulk well and no free-precursor seed.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:103` (also :277, :429) · `The accelerating wave reflects off its own self-induced impedance boundary, trapping into a stabilised topological soliton (a Fermion)` · Fence: boundary Gamma=-1 self-trap is the surviving localizer. The trap here is the self-induced Gamma to -1 impedance boundary, not a bulk well or seeded staged growth.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/07_regime_map.tex:75` (also :295) · `from sub-threshold trapping a wave reflects inward at $\Gamma = -1$\gammaundeclared{} and forms a stable standing wave (matter)` · Fence: Gamma=-1 at V_yield is the boundary self-trap, the surviving localizer. No bulk well and no seeded precursor staging. Line 295 repeats the boundary form.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:167` (also :191) · `is held independently by the transverse-Cosserat ($T_2$) charge/spin $\Gamma = -1$\gammaundeclared{} self-trap wall at $V_{yield}$` · The T_2 Gamma=-1 wall at V_yield is the boundary self-trap that the F-C7 Fence names as the surviving localizer, not this corpse.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:41` · `It represents a permanent macroscopic \textbf{Impedance Mismatch} ($\Gamma = -1$\gammaundeclared{}) to the linear vacuum.` · Gamma = -1 is named as the electron's mismatch to the vacuum. The Fence holds the boundary form out. No seed, precursor or staged growth at this site.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/08_planck_and_string_theory.tex:25` · `bound by the high-impedance boundaries of the vacuum matrix` · Flux tubes held by high-impedance boundaries. F-C7 Fence: boundary self-trap is the surviving localizer, not the corpse; no bulk self-trap or precursor seed is offered.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/12_appendix_formal_proofs.tex:172` (also :173) · `At the knot boundary, $\Gamma = -1$\gammaundeclared{} (total` · Energy confined by total reflection at the knot boundary. F-C7 Fence: boundary Gamma=-1 self-trap is the surviving localizer, not the corpse.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:194` (also :199, :212, :563, :589, :663, :688) · `permanently trapping the dynamic wave energy inside the topological knot` · Knot-boundary Gamma = -1 mirror trapping energy. F-C7 Fence: boundary self-trap is the surviving localizer, not this corpse.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:339` · `In AVE, this maps to a \textbf{stable electromagnetic standing wave} trapped within the 3D vacuum lattice.` · Trap stated with no boundary and no mechanism. Row hunts bulk self-trap, Fence spares boundary. Site is a Hodge mapping, not a build order; row text does not settle it.

### F-C8 — K1+K2 capability-matrix YAML

| | |
|---|---|
| **KB deprecation** | C8 · `manuscript/ave-kb/common/figures/engine_capability_matrix.yaml:31,39` |
| **Corpse** | *"rest mass = self-trapped LONGITUDINAL-bulk wall"* + *"constitutive loop (remanence)"* with no banner channel |
| **Fence** | Same homonym as F-C7. LaTeX that copies this YAML prose as current capability is in scope. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 30 · unsure — not picked 8.

- **unsure — not picked** · `manuscript/common_equations/eq_axiom_4.tex:42` · `Wave packet confined (mass)` · Mass as confinement at saturation resembles rest mass = self-trapped bulk. No longitudinal wall or copied YAML prose, and :55 puts the mass core sub-saturated. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:10` · `proposed as the carrier of rest mass ($m_e c^2$ as trapped longitudinal compression energy)` · Close to rest mass = self-trapped longitudinal-bulk wall, minus self and wall. Stamp reads DEMOTED, NEEDS RE-DERIVATION, not dead, so it is neither named dead nor plainly offered as current. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:230` *(comment, not printed)* · `longitudinal compression energy' consume the propagating reading; re-labeling to real-and-bound` · Unprinted R40 note quoting the line 10 clause as consuming the propagating reading. A demotion audit, not a kill, and line 10 says not dead. Comment-only site. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:105` · `The invariant rest mass is the \textbf{$A_1$ longitudinal-dilatation} confinement` · Closest print to 'rest mass = LONGITUDINAL-bulk wall', under an R40 stamp saying 'not dead', so not Q1. mass = A1 stands per the signed table; the confinement mechanism is the open part. Not picked. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:558` *(comment, not printed)* · `the |Gamma|=1 wall survive; the confinement-of-a-dilatation-wave mechanism plus signed Gamma and` · Same comment: keeps mass=A1 accounting and the wall, puts the longitudinal confinement mechanism under re-derivation. Comment-only corpse, and the row does not settle it. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:36` · `\textbf{$A_1$ longitudinal dilatation depression} ($Z_{bulk} \to 0$)` · Rest mass as an A1 longitudinal depression at Z_bulk to 0 sits near the YAML's longitudinal-bulk wording, but mass = A1 stands per the fence table and no self-trapped wall is claimed. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:41` · `its motion displaces the lattice, generating longitudinal acoustic pressure waves governed by the vacuum's \textbf{Bulk Modulus}.` · Massive defect plus longitudinal bulk channel echoes the YAML wall prose, but concerns motion, not rest mass. The line's DEMOTED tag says needs re-derivation, not dead, so Q1 is not met. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/07_quantum_mechanics_and_orbitals.tex:383` · `The electron interacts with the vacuum's bulk modulus (acoustic impedance), not the shear modulus (electromagnetic impedance).` · Repeats the electron-on-bulk-modulus channel with no self-trap or rest-mass wording. The line's DEMOTED tag says needs re-derivation, not dead, so the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/01_appendices.tex:80` · `$\Gamma \to -1$\gammaundeclared{} --- the short-circuit / TIR wall that \emph{confines} the electron, not a match.)}` · F-C8 Fence names the same homonym. This is the boundary Gamma -> -1 wall; the site does not copy the YAML prose and says nothing of a LONGITUDINAL-bulk wall or remanence.
- **fence-excluded** · `manuscript/backmatter/05_universal_solver_toolchain.tex:599` · `The electron is an impedance mismatch ($\Gamma=-1$\gammaundeclared{}) that traps a longitudinal wave, bouncing at $E=V(r)$.` · The F-C7 homonym fence covers Gamma=-1, but the row also prints 'Acoustic Bulk Modulus Cavity' and a trapped longitudinal wave, echoing the YAML's longitudinal-bulk wall. Row text does not settle which reading holds.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:55` · `The confining $\Gamma = -1$\gammaundeclared{} wall is the transverse Cosserat ($T_2$) self-trap at $V_{yield}$` · F-C8 Fence is the same homonym as F-C7: this is the boundary Gamma = -1 V_yield wall, stated as transverse, not the longitudinal-bulk wall.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:55` · `trapped acoustic-compression energy; \texttt{def-vyvsn1}, PR\,\#260)` · Longitudinal A1 energy called trapped resembles the YAML mass clause, but the wall here is transverse, mass = A1 stands, and the stamp reads NEEDS RE-DERIVATION, not dead. Row text does not settle it.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_4.tex:105` *(comment, not printed)* · `trapped acoustic-compression energy; \texttt{def-vyvsn1}, PR\,\#260)` · Comment re-quotes :55 in the R40 demotion note: acoustic label consumes the wave reading, mass = A1 survives, no signed kill named. Same open question as :55.
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:64` (also :16) · `\noindent\textbf{Dielectric Snap Voltage} (per Axiom 4; the \textbf{longitudinal A1 dilatation} saturation / rest-energy scale, $m_e c^2$;` · Calibration input, outside every row per the hit rules: V_snap is the m_e c^2 scale and mass = A1 stands. No self-trap or wall is claimed for the longitudinal sector.
- **fence-excluded** · `manuscript/common_equations/eq_calibration_constants.tex:70` (also :17, :75) · `the \textbf{transverse Cosserat $T_2$ self-trap wall} --- the electron's confining $\Gamma = -1$\gammaundeclared{}` · F-C8 Fence is the same homonym as F-C7: boundary Gamma = -1 wall at V_yield, stated as transverse, not a longitudinal-bulk wall.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Fence: same homonym as F-C7. Rest mass here comes from Gamma=-1 confinement, not a longitudinal-bulk wall, and no YAML capability prose is copied.
- **fence-excluded** · `manuscript/vol_0_engineering_compendium/chapters/01_theoretical_stress_tests.tex:86` · `drives $Z_{core} = Z_0\sqrt{S} \to 0$ and $\Gamma \to -1$\gammaundeclared{} --- the short-circuit / TIR wall that \emph{confines} the electron, not a match.` · F-C8 Fence: same homonym as F-C7. A confining wall reached by Gamma to -1, with no longitudinal-bulk self-trap language, no remanence, and no copied YAML capability prose.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:171` (also :200) · `forms a standing wave = stable rest mass` · Echoes the YAML rest-mass form, but the wall here is the Gamma to -1 boundary. Fence: same homonym as F-C7, and no capability prose is copied.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:103` (also :277) · `The accelerating wave reflects off its own self-induced impedance boundary, trapping into a stabilised topological soliton (a Fermion)` · F-C8 fence is the F-C7 homonym: rest mass here ties to the Gamma to -1 boundary, not the LONGITUDINAL-bulk wall YAML prose. Line 105 carries that reading separately.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/07_regime_map.tex:295` (also :75) · `The standing wave that results is rest mass.` · F-C7 homonym fence: magnetic-branch Gamma to -1 boundary, not a longitudinal-bulk wall, and no capability-matrix prose copied.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:167` (also :191) · `is held independently by the transverse-Cosserat ($T_2$) charge/spin $\Gamma = -1$\gammaundeclared{} self-trap wall at $V_{yield}$` · This is the Gamma=-1 boundary homonym the F-C8 Fence inherits from F-C7: a transverse T_2 wall, not the YAML's longitudinal-bulk wall, and no remanence text.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/08_planck_and_string_theory.tex:25` · `bound by the high-impedance boundaries of the vacuum matrix` · F-C8 Fence: same homonym as F-C7. This is boundary confinement; the YAML prose on a self-trapped longitudinal-bulk wall is not copied here.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/12_appendix_formal_proofs.tex:172` (also :173) · `At the knot boundary, $\Gamma = -1$\gammaundeclared{} (total` · F-C8 Fence: same homonym as F-C7. This is boundary confinement, not the YAML self-trapped longitudinal-bulk wall copied as current capability.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:194` (also :199, :212, :563, :589, :663, :688) · `permanently trapping the dynamic wave energy inside the topological knot` · F-C8 Fence: same homonym as F-C7. Boundary mirror only; no YAML prose on a self-trapped longitudinal-bulk wall or constitutive loop is copied.

### F-C9 — K3 (2,3) self-assembly as remaining gate

| | |
|---|---|
| **KB deprecation** | C9 · `manuscript/ave-kb/common/historical-precedents.md:56` |
| **Corpse** | *"full `(2,3)` self-assembly … localized remaining gaps"* / graduation gated on self-assembling |
| **Fence** | Cosmic node-injection is held out. Static Link / tank (2,3) **stands**. Hunt self-assembly as a **live manufacture path**, not the winding as charge. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 1 · Q1 0 · Q2 0 · fence-excluded 11 · unsure — not picked 14.

- **live-wrong** · `manuscript/frontmatter/00_foreword.tex:16` · `Whether the electron self-assembles in this form is an open question examined in the volumes; here it is stated as a model, not a result.` · Frames electron self-assembly as an open question examined in the volumes. Not named dead, so the ambiguity default applies. Fence holds the static winding, not self-assembly as a live path. *[lens live-wrong 3]*
- **unsure — not picked** · `manuscript/backmatter/01_appendices.tex:311` · `In a fully emergent physical engine, mass states must generate dynamically from raw local topological configurations; relying upon static hard-coding prevents fluid lattice topology interactions.` · Engine spec says mass states must generate dynamically instead of being spawned; lines 313-319 then read mass off a knot. Row text does not settle whether this is self-assembly as a live path. Not picked. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:56` · `K4 lattice + soliton formation` · Soliton formation printed as a kernel event could read as particle self-assembly, but no (2,3) or manufacture path is named. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_2.tex:33` · `the formation-route (genesis of a winding from a free precursor) remains open.` · Winding genesis framed as open reads like the remaining self-assembly gate, as a path not as charge. No self-assembly wording or graduation gate at the site; same mechanism not certain. *[lens unsure 2, live-wrong 1]*
- **unsure — not picked** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Headed Particle Assembly and offered as settled with no banner, but this is field-driven confinement and the row's corpse is self-assembly as a remaining gate. Row text does not settle it. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_0_engineering_compendium/chapters/04_dcve.tex:99` · `In a fully emergent physical engine, mass states must generate dynamically from raw local topological configurations` · Could read as particles self-forming in the engine, but the section specifies a mass readout on a given knot and names neither (2,3) nor assembly. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:169` · `The kinetic yield governs mass assembly and confinement;` · Assembly offered as a current process, but no (2,3) winding and no remaining-gate framing appears. Whether this is self-assembly as a live manufacture path is not settled by the row. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:171` · `the saturating LC reaches $Z \to 0$, $\Gamma \to -1$\gammaundeclared{}, the wave reflects inward and forms a standing wave = stable rest mass (\emph{matter assembly} picture)` · Narrates a wave assembling matter as a standing picture. F-C9's fence covers static Link and cosmic injection, not this process. No (2,3) is named, so the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:198` · `\subsection{Internal Confinement and Matter Assembly}` · Printed heading over :200, which says the boundary is of the particle's own geometric creation. Reads as self-assembly, but with no (2,3) and no gate framing, so it is not settled. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:100` · `\textbf{Particle Assembly ($V \to 43.65\text{ kV}$):}` · Regime label offers particle assembly at V to V_yield as current. No (2,3) or gate language; row does not settle whether generic assembly is the self-assembly manufacture path. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:429` · `particle assembly from $\Gamma \to -1$\gammaundeclared{} reflections` · Summary repeats particle assembly as naturally produced by the Master Equation. No (2,3) or graduation gate named; row does not settle whether this is self-assembly as a live manufacture path. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/07_regime_map.tex:75` · ```as ``matter assembly begins.''``` · Quotes 'matter assembly begins' at V_yield as a live description of the transition. No (2,3) or gate language; the source chapter is outside this slice. Row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:259` · `winds into a stationary Spin-1 helical loop` · A wave winding itself into a stationary loop is self-assembly as a path, but the object is Spin-1 helical, not (2,3), and no remaining-gate framing appears. The row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:530` · `(topological defect formation, protein folding, crystallisation), the lattice finds ground states in physical time without algorithmic search` · Present-tense defect formation by relaxation resembles self-assembly, but names no (2,3), no electron, no manufacture path or gate. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:702` · `quantises arbitrary continuous topological orbits into integer-wound standing wave particles` · Orbits becoming wound particles under saturation could read as self-assembly, but the bullet summarises Hodge and BSD, names no (2,3) and no manufacture path. Not settled. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/02_full_derivation_chain.tex:827` (also :767) · `latent heat of node generation conceptually balances the holographic thermal` · Latent heat of cosmic node generation in the G/H_infinity argument; no electron or winding is formed. F-C9 Fence: cosmic node-injection is held out.
- **fence-excluded** · `manuscript/backmatter/03_geometric_inevitability.tex:554` (also :563) · `\textbf{Cosmic} K4 crystallization (TKI strain-snap mechanism` · Same cosmic lattice crystallization; the row's Fence holds out the cosmic item. No (2,3) winding or particle self-assembly is offered here.
- **fence-excluded** · `manuscript/backmatter/07_universal_saturation_kernel.tex:87` (also :216, :226, :230) · `K4 crystallization seed event` · Same cosmic lattice seed event; the row's Fence holds out the cosmic item. No (2,3) self-assembly is offered.
- **fence-excluded** · `manuscript/common/translation_cosmology.tex:27` · `Parent-BH strain on the pre-bond state (gloss \emph{pre-geodesic}; R9 rename 2026-08-06) triggers K4 crystallization seed event` · Cosmic lattice crystallization, not (2,3) self-assembly as a manufacture path. F-C9 Fence: cosmic node-injection is held out; tracker scope holds out cosmological lattice-genesis as the K3 amend.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex:28` · `Charge $= \mathrm{Link}(\partial\Omega, F) \in \mathbb{Z}$ stands as static topology.` · Fence: static Link / tank (2,3) stands. The scope note limits 'closes' to the static embedding, records the dynamical orbit NEGATIVE, and offers no self-assembly path.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:191` · `the self-formed $\Gamma=-1$\gammaundeclared{} TIR cage wall` · The self-formed wall sits on a seeded static (2,3) winding. The F-C9 Fence says static Link/tank (2,3) stands, and no live self-assembly path is offered.

### F-C10 — K5 common index still advertises the doctrine

| | |
|---|---|
| **KB deprecation** | C10 · `manuscript/ave-kb/common/index.md:63` |
| **Corpse** | Index blurb: ranked plumber order, three genesis lanes, v9–v15 directions, no superseded marker |
| **Fence** | A LaTeX TOC entry that merely *names* the LOOP GAP leaf is not live-wrong unless it offers ranks as current work. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 0 · Q1 0 · Q2 0 · fence-excluded 0 · unsure — not picked 0.

### F-C11 — K3 formation-route still "remains open" on the axiom leaf

| | |
|---|---|
| **KB deprecation** | Audit 1 · `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:33` |
| **Corpse** | *"the formation-route (genesis of a winding from a free precursor) remains open"* |
| **Fence** | Cosmic node-injection is held out. Charge = winding dictionary and the engine-derived interaction leg are **not** this row. |
| **Status** | PENDING-READ |

**Hits (combined pass 2026-11-01, base `cbc668e7`; in progress, 9 of 15 document groups recorded; this row is not discharged).** Sites: live-wrong 4 · Q1 0 · Q2 0 · fence-excluded 24 · unsure — not picked 22.

- **live-wrong** · `manuscript/common_equations/eq_axiom_2.tex:33` · `the formation-route (genesis of a winding from a free precursor) remains open.` · Verbatim the corpse inside the printed Axiom 2 resultbox: free-precursor winding genesis framed as open, no banner at the site. The Fence clears the dictionary and interaction leg, not this clause. *[lens live-wrong 3]*
- **live-wrong** · `manuscript/frontmatter/00_foreword.tex:16` · `Whether the electron self-assembles in this form is an open question examined in the volumes; here it is stated as a model, not a result.` · Leaves formation open, matching remains open, but names no free precursor, so the row's parenthetical route is not explicit here. The plain self-assembly reading is carried under F-C9. *[lens live-wrong 2, unsure 1]*
- **live-wrong** · `manuscript/frontmatter/00_foreword.tex:112` · `as $V \to 43.65$ kV the impedance drops to $Z \to 0$, forcing $\Gamma = -1$\gammaundeclared{} --- confinement of propagating modes into stable topological solitons` · Propagating modes confined into the wound electron, generating rest mass, is genesis from a free precursor printed as standing physics with no banner. This row's fence holds only cosmic injection, charge dictionary and interaction leg. *[lens live-wrong 3]*
- **live-wrong** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:259` · `establishing the physical derivation of confined point-particles via continuum wave-crashing.` · Free wave to confined particle is presented as an established derivation, offering the K3 formation route as current, beyond remains-open. This is not cosmic node-injection, so the Fence does not apply. *[lens live-wrong 3]*
- **unsure — not picked** · `manuscript/backmatter/06_spice_verification_manual.tex:112` · `A1 mass core has completed)` · Exceeding V_snap is said to complete an A1 mass core, a drive-to-threshold formation reading in a numerical-guard note. No free precursor named; row text does not settle whether this is the corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:54` · `Dielectric breakdown $\to$ pair creation` · Saturation leading to pair creation is a formation event printed as canonical, not framed as open. No free precursor is named and K3's pair-production item is flagged, so the row does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:56` · `K4 lattice + soliton formation` · Catalog lists soliton formation as a saturation event at substrate scale, offered as canonical. No free precursor or 'remains open' wording; row text does not settle whether this is the formation-route corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/07_universal_saturation_kernel.tex:168` · `creation as the topological reorganization.` · Body note to the same catalog row: breakdown triggers pair creation as the reorganization, stated as standing. Formation event without a named free precursor; row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/backmatter/appendix_c_derived_numerology.tex:41` · `When the geometry is driven to hold $\phi > \pi/3$, the internal node connections cross the Axiom 4 limit, physically generating the stable topological knot.` · Present-tense formation of a stable knot, not framed as open. No free precursor and no electron named; cosmic-injection fence does not apply. Row text does not settle whether this is the corpse. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_5.tex:71` · `The genesis mechanism is a named-open entry of the genesis phase (phase map below) --- this clause neither supplies one nor licenses one.` · Prints the genesis mechanism as named-open but explicitly supplies none. It says neither free precursor nor cosmic node-injection, so row text does not settle corpse versus Fence. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/common_equations/eq_axiom_5.tex:98` · `\textbf{(c2)} the \textbf{genesis-phase} law that writes clause S's flux (the deposit is data, not a derivation).` · Genesis-phase law listed as a named-open hole for clause S flux. Flux rather than winding, and no free precursor named; row text does not settle corpse versus cosmic Fence. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/00_intro.tex:49` · `as well as particle generation, are reframed as continuous mechanics arising naturally from this saturated medium.` · Chapter summary states particle generation as settled continuous mechanics. No route or precursor is named, so the row text does not settle whether this is the formation-route corpse. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:171` · `the saturating LC reaches $Z \to 0$, $\Gamma \to -1$\gammaundeclared{}, the wave reflects inward and forms a standing wave = stable rest mass (\emph{matter assembly} picture)` · F-C11's fence has no boundary clause. Formation of rest mass is told as current, but it starts from a trapped mode, not a free precursor. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:220` · `because these random spikes generally lack the sustained inductive tension required to close a stable unknot` · Implies a transient-to-unknot closure route with a stated requirement, offered as current. Subject is virtual particles, and a noise spike may not be a free precursor. Not settled. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:222` · `transient, localised phase twists generated by thermal node noise that fail to achieve stable resonant closure` · Same implied route as :220: closure is the success case these twists miss. It is not named dead and not said to be open, so the row does not settle it. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:283` · `This forward structural shockwave provides a continuous mechanical origin for discrete pair-production.` · A free travelling wave steepens until it snaps and yields pairs, offered as current. Pair production is not settled by the row, and no fence names it. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:315` · `When an entangled pair (e.g., $e^-e^+$) is synthesised from a single deformation of the substrate, two opposite-twist topological defects form.` · States a current formation event for a pair from a substrate deformation. Whether a deformation is a free precursor is not settled by the row, and the cosmic fence does not apply. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex:508` · `Virtual particles are failed topological knots that dissipate before achieving resonant stability.` · Chapter-summary restatement of the :220 route: resonant stability is the success case. Not named dead, and the free-precursor reading is unconfirmed, so it is not settled. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:103` · `The accelerating wave reflects off its own self-induced impedance boundary, trapping into a stabilised topological soliton (a Fermion)` · A wave 'trapping into' a fermion reads as genesis from a free wave, but the scope-line homonym keeps boundary self-trap as localizer. Row does not settle formation versus localization. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:429` · `particle assembly from $\Gamma \to -1$\gammaundeclared{} reflections` · Chapter summary prints particle assembly from Gamma to -1 reflections as a Master Equation product. Formation verb on the surviving boundary form; row does not settle whether this is free-precursor genesis. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/07_regime_map.tex:75` · `from sub-threshold trapping a wave reflects inward at $\Gamma = -1$\gammaundeclared{} and forms a stable standing wave (matter)` · 'Forms a stable standing wave (matter)' is a formation claim from a wave, stated flat, on the Gamma=-1/V_yield boundary. The scope-line homonym keeps that boundary as localizer; row does not settle genesis. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_1_foundations/chapters/07_regime_map.tex:295` · `The standing wave that results is rest mass.` · Gives a formation outcome at the Gamma to -1 boundary with no dead marker. Row does not settle formation versus localizer. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/09_computational_proof.tex:49` · `Topological Pair Production   & $H_{net}=0 \to e^+ + e^-$    & IV    & exact & 0 \\` · Pair genesis is printed as verified 'exact' with zero parameters; the precursor is unnamed. The K3 fence leaves two-node pair production vs 0_1 flag-don't-fix, so the row does not settle free-precursor genesis. *[lens unsure 3]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/10_open_problems.tex:10` · `preventing equal matter/antimatter unknot formation` · Cosmological unknot formation under lattice chirality. F-C11 Fence holds out cosmic genesis; no free-precursor manufacture path is offered, and the body uses imported electroweak baryogenesis. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:530` · `(topological defect formation, protein folding, crystallisation), the lattice finds ground states in physical time without algorithmic search` · Treats defect formation as something the lattice simply does, not as 'remains open'. No free precursor named; cosmic fence not engaged. Row text does not settle it. *[lens unsure 2, fence-excluded 1]*
- **unsure — not picked** · `manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex:702` · `quantises arbitrary continuous topological orbits into integer-wound standing wave particles` · Continuous orbit to integer-wound particle sits close to genesis of a winding, stated as fact not open. Bullet summarises Hodge and BSD; no free precursor named. Not settled. *[lens unsure 2, fence-excluded 1]*
- **fence-excluded** · `manuscript/backmatter/02_full_derivation_chain.tex:827` (also :767) · `latent heat of node generation conceptually balances the holographic thermal` · Cosmic node generation in the G/H_infinity argument, not a winding from a free precursor. F-C11 Fence: cosmic node-injection is held out.
- **fence-excluded** · `manuscript/backmatter/03_geometric_inevitability.tex:554` (also :563) · `\textbf{Cosmic} K4 crystallization (TKI strain-snap mechanism` · Cosmological lattice genesis, not electron minting. The row's Fence holds out cosmic node-injection and the tracker scope line holds out cosmological lattice-genesis.
- **fence-excluded** · `manuscript/backmatter/04_physics_engine_architecture.tex:164` · `utils/ 4 mods: winding extractor, genesis runner, genus, v8 instr.` · Printed inventory names a genesis runner as present tooling; 04:85 scopes the tree as inventory, not physics. Naming a tool may or may not offer genesis as current; row text does not settle it.
- **fence-excluded** · `manuscript/backmatter/07_universal_saturation_kernel.tex:87` (also :216, :226, :230) · `K4 crystallization seed event` · Cosmic K4 crystallization seed is lattice genesis with no electron minted; the row's Fence holds out the cosmic item and the tracker scope line names cosmological lattice-genesis as the held-out K3 amend.
- **fence-excluded** · `manuscript/common/translation_cosmology.tex:27` · `Parent-BH strain on the pre-bond state (gloss \emph{pre-geodesic}; R9 rename 2026-08-06) triggers K4 crystallization seed event` · A cosmic lattice seed event; it names no winding or free precursor. F-C11 Fence: cosmic node-injection is held out; tracker scope holds out cosmological lattice-genesis.
- **fence-excluded** · `manuscript/common_equations/eq_axiom_2.tex:33` · `Axiom 2 thus carries both the charge \emph{dictionary} and a derived winding-pair \emph{interaction}` · Fence: charge = winding dictionary and the engine-derived interaction leg are not this row. Same line as the live-wrong clause; the finding scopes to that clause only.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:22` (also :16, :91) · `The \emph{interaction} between two such windings is engine-derived (2026-07-03)` · Fence: the charge = winding dictionary and the engine-derived interaction leg are not this row.
- **fence-excluded** · `manuscript/frontmatter/00_foreword.tex:35` (also :32, :41, :97) · `Lattice genesis (the framework's replacement for the Big Bang)` · Tracker homonym line: cosmological lattice-genesis is the held-out K3 amend. The site describes substrate crystallization, not electron formation from a precursor.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:62` (also :56) · `The \emph{interaction} between two windings is also now engine-derived: two $(2,3)$ winding solitons repel when like-handed and attract when unlike-handed` · Fence clause: the charge = winding dictionary and engine-derived interaction leg are not this row. Axiom 2 prints no formation-route-remains-open sentence.
- **fence-excluded** · `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:233` (also :79, :242) · `at which the thermodynamic latent heat of node generation would balance the holographic thermal capacity of the expanding surface area` · Fence clause: cosmic node-injection is held out. This is the corpus node-heat G/H-infinity gloss and lattice genesis, not electron minting.
- **fence-excluded** · `manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:242` · `is engine-derived: two $(2,3)$ winding solitons repel when like-handed and attract when unlike-handed` · The engine-derived interaction between windings is the leg the F-C11 Fence names as not this row.

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
