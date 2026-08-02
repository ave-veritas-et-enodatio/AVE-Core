### ENTRY 2026-08-01-bench-staleness-propagation

**Lane:** implementer · **Branch:** `docs/bench-staleness-propagation` · **Class:** mechanical staleness-propagation, **zero new decisions** (six items, every one a propagation of an already-adjudicated correction).

**Provenance:** the 2026-08-01 bench-inventory audit (findings F2, F5, F6, F7, F8) + the 2026-08-01 HOPF theory-compilation finding (ITEM 6). Upstream adjudications propagated: the **2026-06-04 per-node adjudication**, the **2026-07-02 Cleave rescope**, the **2026-06-03 Sagnac retirement**, the **2026-07-06/07 roll-off ruling**, and the **2026-06-04 HOPF round-2 C3/C4 retirement**.

---

#### ITEM 1 (F5) — per-node adjudication propagated to 3 unbanner'd Ch.11 leaves

The 2026-06-04 per-node / apparatus-voltage adjudication reached `vacuum-impedance-mirror.md` and the PONDER-05 site family (11 KB files) but **never reached three Ch.11 leaves**, all of which carried zero `per-node`/`apparatus`/`conflation` hits and still taught apparatus-voltage-as-per-node as live physics.

Dated Rule-12 banners added (bodies preserved unedited), patterned on the mirror leaf's own 2026-06-04 RE-SCOPED box. Arithmetic verified against `src/ave/core/constants.py` on this branch (`L_NODE = 3.8616e-13` m, `V_YIELD = 43651.85` V, `R_I = √(2·ALPHA) = 0.1208`), with `A₀ = E_local·ℓ_node/V_YIELD`:

| Leaf | Conflated claim | Per-node `A₀` | vs the `R_I` knee |
|---|---|---|---|
| `project-zener-04.md` | "the moment the localized field crosses the 43.65 kV Impedance Rupture limit" (80 kV/1 mm) | `7.08e-10` | 8.23 OOM below |
| `project-torsion-05.md` | "Because \|−75 kV\| > 43.65 kV, the vacuum LC network instantly saturates" (75 kV/1 mm) | `6.63e-10` | 8.26 OOM below |
| `metric-levitation-limit.md` | "Because 59.1 kV > 43.65 kV, the spatial vacuum undergoes absolute impedance rupture" (59.1 kV/1 mm ref.) | `5.23e-10` | 8.36 OOM below |

Reaching `A₀ = 1` across even a 1 µm gap needs **~113 GV**. A null at these drives is an **artifact-of-regime**, not an Axiom-4 falsification. Also annotated the Matrix-2 lifecycle row for **C16-TORSION-05** (was "complete … TBD" as if a live build candidate → per-node-conflation-retired; outcome cell TBD → n/a-artifact-of-regime).

#### ITEM 2 (F7) — priority block re-derived, not patched

The map's "Priority order for action" ranked the **Sagnac-RLVE fab package #2** while the A2 entry and Matrix-2 row of the *same file* record it **RETIRED to corroborative-null (2026-06-03)**. Audit of the whole block found **four of five entries stale**: #3 LIGO ("the executable observer is the missing piece" — the driver ran, result RETRACTED 2026-07-20), #4 CMB ("execution deferred" — EXECUTED 2026-05-19, MARGINAL-D), #5 muon g-2 (driver built + re-framed 2026-05-19).

Per the audit's recommendation the block was **re-derived** from `_orchestration/2026-07-15_hardware-ratings-map.md` §2/§3, importing its charter rule verbatim and its own priority marks: **1.** F6 ε→T2 irreversible field channel (§3, "Priority 1", GATED) · **2.** R10 census Stage-2 (§2, "priority 4") · **3.** R11 CVR (§2, "priority 5, elevated" — the only real-machine probe) · **4.** R12 Cleave-01 (§2, "queued behind R11") · **5.** the remaining un-numbered BENCH-∅ rows in the map's row order. Rows of the divergence map with no ratings-table row (A1-HOPF, C1, C5, C3) are ranked separately with true current status; retired/regime-artifact rows are named so they cannot be re-promoted. The superseded block is preserved verbatim in a collapsed `<details>` marked do-NOT-action.

#### ITEM 3 (F2) — stale "Blocking" gate resolved on the cRIO prereg-draft

`research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md` §11 items 1-2 still read open, item 1 marked **"Blocking"** for §6 bin pinning. Both were resolved by the ratified roll-off ruling (Grant-ratified 2026-07-06/07, PRs #562/#558; KEEP-BOTH supersession at `.../ch12-falsifiable-predictions/ee-bench-plateau.md:20`):

- **item 1 (sign-of-slope)** → RESOLVED to the roll-off (Branch F sign): chord `C_diel = C₀S → 0`, tangent `C_ss = C₀(S − A²/S)` zero-crossing at `E/E_yield = 1/√2` (NDC snap-back), keyed on `V_yield`.
- **item 2 (is Branch R off-bench?)** → RESOLVED **YES**: Branch R's `C₀/S` divergence is the orthogonal **longitudinal-A1** bond compliance keyed on the higher `V_snap ≈ 511` kV, which an across-gap meter does not read. The R/F tension is **scope, not contradiction**.

Canonical successor named: `research/2026-07-13_cvr-requirements_DERIVED.md`. §11 items 3-4 untouched by the ruling and left explicitly open.

#### ITEM 4 (F8) — stale "chord" label on ratings-map R12

`_orchestration/2026-07-15_hardware-ratings-map.md` R12 called the Cleave-01 gap-independence axis a **"chord"**. Stale vs the 2026-07-02 rescope (`project-cleave-01.md:39-40`): *"COUPLING-STATUS — NULL-CONFIRMED-FINAL (2026-07-02, `clm-clvchn`). The derived-pump reading is closed; the bench is a corroborative-null discriminator."* Both the 2-band and the faithful N-band srs Chern return `C = 0` in both readings and both enantiomorphs — **AVE itself predicts the null**, so a positive REOPENS `clm-clvchn` and never confirms. The **AXIS is correct and stands** (gap-INDEPENDENCE, not the slope); only the chord/echo class label was corrected, with a dated note.

#### ITEM 5 (F6) — HOPF-02a fabbed-vs-not-fabbed disambiguated

Core sites asserted HOPF-02a is "fabbed" / "already-fabbed … measured on". `AVE-HOPF/.agents/HANDOFF.md` (source of truth, read-only — **AVE-HOPF was not edited**) records Phase 0a fab-artifact generation **complete** (Gerbers + drill + DRC at `hardware/Gerbers_hopf_02a/`) with the **Phase 0b physical fab order NOT placed**; the gate is Grant's ~$123 JLCPCB upload. **No HOPF-02a board and no HOPF-02a measurement exist.**

**Four** sites disambiguated to *"fab-artifacts exported (Gerbers); order not placed"* — the audit named three; a fourth carries the identical claim in the Matrix-1 predictions row and was corrected in the same pass. A one-line source-of-truth pointer to `AVE-HOPF/.agents/HANDOFF.md` was added under the §A1 Substrate bullet, and the Matrix-3 next-action re-ordered to **place-the-order-first**.

> ⚠ **Cite-shift caught in the same bullet:** `AVE-HOPF/.agents/HANDOFF.md:43` is now a blank line; the HOPF-01 confound content (varying `L_wire`, no enantiomer pair, single substrate) lives at **`:72`**. Corrected with the shift annotated.

#### ITEM 6 — the 2026-06-04 HOPF round-2 C3/C4 retirement propagated

The map still carried the **round-1** framing calling C3 medium-independence and C4 enantiomer sign-flip *"the AVE-distinct legs"*, including the flatly-false *"Classical EM **cannot** reproduce medium-independence … or enantiomer sign-flip."*

Round-2 (Grant-adjudicated 2026-06-04) retired **both** to consistency-class. The correct counterfactual is not a coupled-line model but a classical **reciprocal Pasteur (chiral/bianisotropic) medium** — *"from sugar water to a copper-helix PCB"*: its rotatory power `κ` is a geometric property of the handed inclusion, not of the host `ε` (⇒ medium-independent shift, C3), and mirroring sends `κ → −κ` (⇒ enantiomer sign-flip, C4). Round-2 verdict for both: **FORM-SHARED-RETIRE**.

Receipts (the local AVE-HOPF checkout sits on a branch predating the round-2 merge; content read from AVE-HOPF `main`):
- `AVE-HOPF/research/2026-06-04_hopf-round2-chiral-counterfactual-result.md:189-191` — the §5 per-survivor verdict table (C3 FORM-SHARED-RETIRE, C4 FORM-SHARED-RETIRE, chirality channel PARTIAL)
- same doc `:20-23` — the sugar-water mechanism
- `_orchestration/experimental/2026-06-04_round2-adjudications.md:40` — *"Decision (Grant AGREED 2026-06-04). (a) reciprocal-Pasteur at the linear bench → §6.2 C3/C4 'AVE-DISTINCT' labels **retire to consistency-class**; (b) **ADD** the 2-port S₂₁-vs-S₁₂ reciprocity sweep to HOPF-02a."*
- `README.md:295` — already current; used as the model wording

Nine sites corrected: map `:54` (full round-2 supersession box, round-1 paragraph preserved verbatim), `:57` (the SM counterfactual), `:58`, `:444` (this branch's own ITEM-2 priority bullet), `:496` (Matrix-1), `:582` (Matrix-2), `:622` (Matrix-3), `:793` (Operational implication), `:1104` (ranked-list bronze entry) + `open-source-hardware.md:21`. The surviving AVE-distinct leg is named everywhere: the **2-port S₂₁-vs-S₁₂ reciprocity sweep**, a **linear-null in the accessible regime** (the distinct regime is above-yield), needing **2-port hardware the 1-port SMA edge-launch HOPF-02a board does not provide**. `open-source-hardware.md`'s closing *"falsified … if the medium and sign legs are null"* is explicitly retired — a null there is now the **expected consistency-class outcome**.

---

#### Cite-shift sweep

Line-count deltas: `divergence-test-substrate-map.md` 1107→1150 (+43) · `project-zener-04.md` 20→49 · `project-torsion-05.md` 23→55 · `metric-levitation-limit.md` 42→79 · `crio-…prereg-draft.md` 394→422 · `open-source-hardware.md` 42→46 · `hardware-ratings-map.md` 99→99 (0).

Corpus-wide sweep over `*.md`/`*.tex`/`*.py` for both cite forms (`filename:NNN` and the bare `line NNN` / `lines NNN-MMM` form), classified by comparing origin/main content at the cited line against HEAD.

**REPAIRED (8 — target verified semantically correct on origin/main, shifted by this branch; all 8 re-verified to resolve after ITEM 6):** the map's own two `project-torsion-05.md` "lines 8-13" → "lines 44-53" cites; `common/physics-lineage-map.md:239` (zener `:18`→`:47`); `research/2026-07-10_collapse-target-registry.md:213-215` (the three leaves); `research/2026-07-13_cvr-requirements_DERIVED.md:20,:31` (prereg `:165-170`→`:193-198`, `:193`→`:221` — repaired first, since that datasheet is the canonical successor named in ITEM 3).

**NOT REPAIRED — DISCLOSED as pre-existing wrong-target cite-rot** (a +N bump would have preserved a cite that pointed at the wrong row *before* this branch; verified against the map's own `### ` section boundaries). These files are left **byte-identical to origin/main**, so this branch adds no new cite debt:

| Citing site | Cites | Labelled | Actually lands in |
|---|---|---|---|
| `vol_9…/gen_bankable_falsification_windows.py:12` | map `:143` | "(C1-BH-RING)" | §B7 PONDER-05 (B7 `:142`, C1 `:157`) |
| `vol_9…/gen_bankable_falsification_windows.py:17` | map `:245,247` | "(C12-G-STAR)" | §C10 Muon lifetime (C10 `:242`, C12 `:261`) |
| `vol1/…/preferred-frame-and-emergent-lorentz.md:235` | map `:399` | "C7-GRB-DISPERSION" | §D5 HTS/Meissner (D5 `:397`) |
| `claim-quality-closure-roadmap.md:85` | map `:514` | a C5-CMB-AXIS row | the C15-CLEAVE-01 matrix row |
| `claim-quality-closure-roadmap.md:100` | map `:497` | a C15-CLEAVE-01 row | the KIMS+MAJORANA κ line |
| `claim-quality-closure-roadmap.md:115` | map `:153,160,949` | a C5 row | `:153` blank · `:160` C1 discriminator · `:949` a mermaid comment |

**DISCLOSED, not rewritten (~60):** further shifted cites inside dated research result/prereg docs, `_orchestration/` boards and `_archive/`. Rewriting line numbers inside a dated record is revisionist — git is the trail.

**→ ROUTED FOLLOW-ON:** a dedicated **cite-rot lane** for the six wrong-target cites above. They are a *different* defect class from shift (the cite never pointed at its labelled row), and re-pointing them is a content decision this lane declined to make.

---

#### Battery

`make verify` **exit 0** at every commit · broken-inter-link count **unchanged at 42** (stash A/B comparison vs origin/main) · `make refresh-kb-metadata` **idempotent** (0 subtree-claims, 0 solidity, 0 leaf-references, 0 `.index/` files rewritten) · `verify-docket-keys` clean · pure-corpus observed · zero file overlap with the live branches `docs/rulings-d2-d3-d4`, `docs/factor7-and-782-basis-notes`, `src/deprecate-superseded-birefringence-ratio`, `src/repoint-pvlas-v3`.

> 🔴 **CORRECTION 2026-08-02 (Rule 12 — the original sentence is preserved verbatim immediately below; git is the trail).** The battery line above originally read: *"…, `src/deprecate-superseded-birefringence-ratio` (`src/repoint-pvlas-v3` does not exist locally or on origin)."* **That parenthetical was false.** `src/repoint-pvlas-v3` **does** exist on origin at **`a370eb93`** (8 commits ahead of `origin/main`), touching **2 files**: `_orchestration/docket-entries/2026-08-01-d7-repoint-pvlas.md` and `research/2026-08-01_pvlas-arbiter-v3-repoint_scoping.md`. The likely cause is a `git ls-remote` / branch-list check run before that branch was pushed, recorded as a permanent negative.
>
> **Re-verified result (the claim the battery line should have made): ZERO FILE OVERLAP.** `git diff --name-only origin/main...a370eb93` returns the two files above; `git diff --name-only origin/main...` for this branch returns thirteen files (`_orchestration/2026-07-15_hardware-ratings-map.md`, `_orchestration/docket-entries/2026-08-01-bench-staleness-propagation.md`, `manuscript/ave-kb/claim-quality-closure-roadmap.md`, `manuscript/ave-kb/common/divergence-test-substrate-map.md`, `manuscript/ave-kb/common/physics-lineage-map.md`, the four Ch.11 leaves `metric-levitation-limit.md` / `open-source-hardware.md` / `project-hopf-02.md` / `project-torsion-05.md` / `project-zener-04.md`, `research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md`, `research/2026-07-10_collapse-target-registry.md`, `research/2026-07-13_cvr-requirements_DERIVED.md`). The intersection is **empty**. The non-overlap conclusion stands; only the reason given for it was wrong.

#### Flagged, not fixed

1. **`project-hopf-02.md:102`** reads *"HOPF-02a DESIGN-COMPLETE; PHASE 0a artifact-generation pending"* — stale in the **opposite** direction from ITEM 5 (Phase 0a is complete; Phase 0b, the order, is the pending gate). A different defect than the adjudicated one; surfaced, not edited.
2. **`claim-quality-closure-roadmap.md:96`** still contains "already-fabbed HOPF-02a", but it is a **preserved 2026-06-03 walk-back record row** (audit trail), not a live status claim — left intact per audit-trail-in-git discipline.
3. **`_orchestration/index.md` §"Next-move priority ladder"** is a 2026-05-28-era ladder, independently stale from the ITEM-2 block. Out of scope; flagged.
4. **`main` drift:** the brief pinned `main` at `e6de554b` (PR #817); actual `origin/main` at branch time was **`19285c5d`** (PR #818). Worktree taken off `origin/main` per the brief's own instruction.
