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

> **Superseded 2026-08-18** by the combined-pass protocol above (Wave-2 ruling D7-A); body preserved (Rule 12) — every frozen requirement below still binds, only the one-full-universe-pass-per-row *scoping* is replaced.  <!-- rule12-freeze: base=0316211661e880e569debeac1c5c73fa0c1e4fb1 region=above offset=0 lines=76 bytes=6950 sha256=b143aabb5b0b032c13fd8b117a68b9a92447f31743947c95eb8d68ab08043ffc -->

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

Hits: *(empty until discharged)*

### F-C2 — K1 lock as live-threat candidate

| | |
|---|---|
| **KB deprecation** | C2 · `manuscript/ave-kb/common/physics-lineage-map.md:302` |
| **Corpse** | *"candidate = dynamical lock … graded HYPOTHESIS-class"* under a live-threat column |
| **Fence** | Same clause-not-page rule. LaTeX that names Poincaré cohesive stress as the *named hole* is not this corpse. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C3 — K5+K1 LOOP GAP doctrine as current routing aid

| | |
|---|---|
| **KB deprecation** | C3 · `manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md` (whole leaf) |
| **Corpse** | *WHEN TO USE: … scoping v11+ engine work*; advance ranks; platform ACTIVE; remanence rank-4; v11 ordered upgrades |
| **Fence** | Ranks as *historical traveler* may remain. This follow-up hunts ranks / v11+ / remanence offered as **current manufacture path**. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C4 — K1+K5 remanence as open route to mass

| | |
|---|---|
| **KB deprecation** | C4 · `manuscript/ave-kb/common/substrate-hysteresis-index.md:155,159` |
| **Corpse** | *"The LOOP GAP remains open until … remanence/coercivity/loop-area to mass"* + v11 charter / P11 |
| **Fence** | Anhysteretic-kernel *fact* (Level-1 has no loop area) is not the corpse. The corpse is remanence as the **live path that holds the electron**. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C5 — K1+K3+K5 manufacture = energize-lock + remanence

| | |
|---|---|
| **KB deprecation** | C5 · `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:123,127` |
| **Corpse** | *"Electron manufacture requires … energize-lock, and Level-2 remanence … v11 targets P11"* |
| **Fence** | Vol 9 datasheet circuit models that describe *walls / M,Q,J* without selling genesis-cook are not this corpse. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C6 — K1 remanence as OPEN R10 capability gap

| | |
|---|---|
| **KB deprecation** | C6 · `manuscript/ave-kb/common/engine-capability-map.md:32,67,82,112,127` |
| **Corpse** | Remanence / constitutive loop as the **open** retention mechanism the engine must still close |
| **Fence** | Do not banner "kernel is anhysteretic" as killed physics. Banner remanence-as-current-hold. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C7 — K2+K3 precursor → self-trap build order

| | |
|---|---|
| **KB deprecation** | C7 · `manuscript/ave-kb/common/engine-capability-map.md:109` |
| **Corpse** | *"seed photon precursor → self-trap"* as staged-growth construction path |
| **Fence** | Boundary \(\Gamma=-1\) self-trap (surviving localizer) is **not** this corpse. Hunt **bulk** self-trap / free-precursor seed offered as current. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C8 — K1+K2 capability-matrix YAML

| | |
|---|---|
| **KB deprecation** | C8 · `manuscript/ave-kb/common/figures/engine_capability_matrix.yaml:31,39` |
| **Corpse** | *"rest mass = self-trapped LONGITUDINAL-bulk wall"* + *"constitutive loop (remanence)"* with no banner channel |
| **Fence** | Same homonym as F-C7. LaTeX that copies this YAML prose as current capability is in scope. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C9 — K3 (2,3) self-assembly as remaining gate

| | |
|---|---|
| **KB deprecation** | C9 · `manuscript/ave-kb/common/historical-precedents.md:56` |
| **Corpse** | *"full `(2,3)` self-assembly … localized remaining gaps"* / graduation gated on self-assembling |
| **Fence** | Cosmic node-injection is held out. Static Link / tank (2,3) **stands**. Hunt self-assembly as a **live manufacture path**, not the winding as charge. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C10 — K5 common index still advertises the doctrine

| | |
|---|---|
| **KB deprecation** | C10 · `manuscript/ave-kb/common/index.md:63` |
| **Corpse** | Index blurb: ranked plumber order, three genesis lanes, v9–v15 directions, no superseded marker |
| **Fence** | A LaTeX TOC entry that merely *names* the LOOP GAP leaf is not live-wrong unless it offers ranks as current work. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

### F-C11 — K3 formation-route still "remains open" on the axiom leaf

| | |
|---|---|
| **KB deprecation** | Audit 1 · `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:33` |
| **Corpse** | *"the formation-route (genesis of a winding from a free precursor) remains open"* |
| **Fence** | Cosmic node-injection is held out. Charge = winding dictionary and the engine-derived interaction leg are **not** this row. |
| **Status** | PENDING-READ |

Hits: *(empty until discharged)*

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
