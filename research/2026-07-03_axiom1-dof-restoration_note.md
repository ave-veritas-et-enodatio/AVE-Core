# Axiom-1 DOF-sentence Restoration — z=4-diamond → z=3-chiral-srs

**Date:** 2026-07-03
**Arc:** `analysis/axiom1-dof-restoration`
**Grant ruling (2026-07-03, verbatim):** "we should re-write, but lets be detailed on
checking and apply the vocab skills and identify kb/manuscript updates."
**Nature:** RESTORATION of the axiom's physical claim, NOT a meaning change. Canon ruled
z=3 long before the z=4 clause entered (`vol1/claim-quality.md:141,:753-766`, `clm-9s9apq`
/ `clm-q39qct`; the Vol-1 datasheet ruling "K4 z=3, don't flip to 4"). This arc IS the
"future-arc work" the D1-RATIFICATION commit (776c8780) explicitly named when it left the
z=4 clause verbatim as a walk-back target.

---

## 1. PROVENANCE TRACE — when/how "z=4 diamond" entered the axiom body

`git log -S "z=4" / -S "diamond" / -S "4-fold" -- manuscript/common_equations/eq_axiom_1.tex`:

| Commit | Date | What it did to the connectivity clause |
|:--|:--|:--|
| (pre-`01cac6bb` baseline) | ≤2026-06-11 | `with 4-fold K4 nearest-neighbor connectivity at each node.` — the latent internal inconsistency (K4/srs is trivalent, yet "4-fold") already present, but no explicit "diamond" and no "production engine" scoping. |
| **`01cac6bb`** "Propagate D1 walk-back" | **2026-06-11** | **THE CONTAMINATION EVENT.** Changed to `with \textbf{4-fold (z=4 diamond) nearest-neighbor connectivity} at each node in the production engine.` — hardcoded z=4 diamond as the SUBSTRATE connectivity AND appended "in the production engine," binding the axiom's physical claim to engine-implementation status. Reflected the (then-current) 2026-06-12 D1 reading (z=4 diamond = production computational net). Same commit added the "D1 adjudication, 2026-06-12" block ("The production computational net is z=4 diamond"). |
| `63fea0ae` "LEAN eq_axiom blocks" | 2026-07-03 | Retired the `$\mathcal{M}_A$` glyph (INVARIANT-N1); **DELETED** the "Cold-lattice handedness on diamond… k_χ" sentence and the "production computational net is z=4 diamond" D1-block sentence from the file (these deletions ORPHANED two vocab-register cites to `eq_axiom_1.tex:35`/`:37` — see §4). Left the z=4 opening clause. |
| **`776c8780`** "D1 RATIFICATION" (PR #486) | 2026-07-03 | Ratified z=3 srs as production carrier; added the **"Consistency note (flag-don't-fix)"** on line 31 explicitly naming the z=4 clause a "NAMED walk-back target… left verbatim here… the walk-back that reconciles the two is future-arc work." **Did NOT rewrite the DOF sentence** (deliberate; that arc recorded the adjudication only). |

**STOP-condition check (was z=4 a Grant-adjudicated wording?): NO.**
- The z=4 clause was a *drive-by propagation* (`01cac6bb`) of the 2026-06-12 provisional D1
  default (framing B: diamond=engine, srs=instrument), which was itself **superseded twice**:
  first by a **Grant ratification dated 2026-06-25** (recorded at
  `unified-engine-design-doctrine.md:211`: *"Decision 1 (RATIFIED, Grant 2026-06-25): the
  production engine substrate is the chiral z=3 srs net"*), then by the **2026-07-03 D1
  RATIFICATION** (PR #486). The z=4 clause was already stale by 2026-06-25 and is now
  doubly-ratified against.
- The 776c8780 commit itself flagged the clause as a walk-back target and named "the walk-back
  that reconciles the two" as "future-arc work." This arc is that work. No silent supersession
  of a ratified sentence — the reverse: executing a deferred, doubly-ratified correction.

---

## 2. PRE-EDIT SWEEP — classified table (two-method: rg + BSD-grep + python-walk)

**Method cross-check.** rg (manuscript, connectivity-filtered) and a python os.walk (all scope
dirs, z=4-token AND connectivity-token co-occurrence, 74 lines) agree on the manuscript
category-(a) set; the python-walk's extra ~55 lines are all src/ + research/ derivation-USES of
z=4-as-K4-coordination-number (Bethe-lattice admittance sums, Maxwell rigidity counting, W-boson
loop, g-2), which are NOT substrate-connectivity axiom-restatements (see category (c′)).

### (a) MUST-CHANGE — states z=4/diamond as the SUBSTRATE's connectivity (the physical claim)

| # | file:line | current wording (connectivity clause) | edit scope |
|:--:|:--|:--|:--|
| a1 | `manuscript/common_equations/eq_axiom_1.tex:25` | "4-fold (z=4 diamond) nearest-neighbor connectivity … at each node in the production engine" | **THE PRIMARY REWRITE** (this arc) |
| a2 | `manuscript/ave-kb/common/axiom-register.md:145` | canonical-statement: "z=4 diamond nearest-neighbour connectivity in the production engine" | KB-leaf edit (this arc) |
| a3 | `manuscript/ave-kb/common/axiom-register.md:147` | provenance: "z=4 diamond production engine vs bare z=3 srs instrument … fixed the coordination-number reading" | KB-leaf edit (this arc — update to ratified reading) |
| a4 | `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:16` | "4-fold K4 nearest-neighbour connectivity" | KB-leaf edit (this arc) |
| a5 | `manuscript/backmatter/12_mathematical_closure.tex:77` | "4-fold K4 nearest-neighbor connectivity" | manuscript .tex edit (this arc) |
| a6 | `manuscript/vol_9_vacuum_datasheet/chapters/01_general_description.tex:18` | "4-fold K4 nearest-neighbour connectivity" | manuscript .tex edit (this arc) |

### (a-fig) MUST-CHANGE-BUT-DEFERRED — figure geometry depicting z=4 substrate connectivity

| # | file:line | current | why deferred |
|:--:|:--|:--|:--|
| af1 | `manuscript/vol_9_vacuum_datasheet/figures/node_anatomy.tex:16,:22` | TikZ: "4-fold K4 nearest-neighbour bond stubs (tetrahedral connectivity)" + 4 bond-stub `\foreach` at {35,145,215,325}° + caption "4-fold K4 connectivity" | **DEFERRED (logged, not truncated).** This is rendered figure GEOMETRY (4 struts at specific angles), not a one-word text edit; correcting to z=3/trivalent (3 struts, 120°) is a figure re-render coupled to the datasheet house-style program ("K4 z=3, 3 struts, don't flip to 4"). Belongs to the datasheet-figure arc, not this text-restoration arc. **1 file, 2 lines + geometry.** |

### (b) ALREADY-CORRECT — states z=3/srs (no edit)

| file:line | wording |
|:--|:--|
| `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:54` | "3-fold ($z=3$) K4 nearest-neighbour connectivity" + `% clm-q39qct ($z=3$ = K4/SRS connectivity choice)` — **the canonical Scheme-A source eq_axiom_1.tex:3 points to; already z=3** |
| `manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex:105` | "chiral SRS net (Axiom 1 substrate, coordination $z=3$)" |
| `manuscript/ave-kb/vol1/axioms-and-lattice/ch2-macroscopic-moduli/dielectric-snap-limit.md:32` | "chiral SRS net (Axiom 1 substrate, coordination $z=3$)" |
| `manuscript/ave-kb/vol1/claim-quality.md:141,:753-766` | "chiral SRS net (coordination $z=3$)"; `clm-9s9apq` z=3 justification (canon anchor) |
| `manuscript/ave-kb/common/vocabulary-register.md:439,446` | `def-4b1a2c` K4 production carrier = "chiral srs z=3 net" (ratified) |
| `manuscript/ave-kb/vol4/circuit-theory/…/unified-engine-design-doctrine.md:211-223` | "Decision 1 (RATIFIED, Grant 2026-06-25): … chiral z=3 srs" |
| `manuscript/vol_9_vacuum_datasheet/chapters/17_engine_requirements.tex:86` | "srs graph is the chiral degree-3 (10,3)-a net" |

### (c) ENGINE-SCOPED — correctly describes the diamond engine/instrument as implementation (LIST, don't edit — migration-policy territory)

| file:line | wording | note |
|:--|:--|:--|
| `manuscript/ave-kb/vol4/circuit-theory/…/unified-engine-design-doctrine.md:209,215-224,238-247` | "§E — Connectivity: chiral z=3 srs vs achiral z=4 diamond"; diamond "reserved for coarse-grained macroscopic regime"; the flag-don't-fix D1-tension block | correctly scopes diamond as instrument; owns its own flag-don't-fix; get carrier-tag language at next touch per migration policy |
| `manuscript/vol_9_vacuum_datasheet/chapters/18_experimental_prints.tex:37,:200` | "production substrate build_diamond_net — degree-4 achiral Fd-3m diamond … srs … acceptance instrument" | **STALE vs D1** (says diamond=production) but this is print-kit engine-scoped; migration-policy P0 carrier-tag territory, NOT this arc |
| `manuscript/ave-kb/vol9/ch18-experimental-prints/index.md:54,:117,:137` | "diamond production K4 (build_diamond_net)"; "diamond-primary / achiral-cold reading" | same — print-kit engine-scoped, migration P0 |
| `manuscript/ave-kb/vol9/ch3-pin-port-configuration/node-scattering-multiplicity.md:35` | "srs net is degree-3 and the diamond net is degree-4" | descriptive contrast; fine |
| `manuscript/ave-kb/common/numerical-provenance-manifest.md:36` | "coordination_z=4" (K4 admittance tree S11) | engine-numeric provenance of a diamond-run; migration territory |

### (c′) DERIVATION-USES of z=4-as-K4-coordination-number — DISTINCT PHYSICS QUESTION (do NOT edit here)

These use z=4 as the K4 coordination number INSIDE a derivation (Bethe-lattice admittance,
Maxwell rigidity counting, Kirkwood-Fröhlich, K=2G form, water z/3 isotropy factor). Whether
these should migrate to z=3 is a **physics re-derivation** (P1/P2 migration acceptance-gate
territory — the α/Lorentz-chain survival gate), NOT a documentation edit. Editing z=4→z=3 in a
Bethe-lattice admittance sum silently changes a numerical result. **flag-don't-fix.**

| file:line | use |
|:--|:--|
| `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:230,:257` | "z=4 is the K4 coordination number" (Higgs Dyson/Bethe-lattice fixed point) |
| `manuscript/vol_3_macroscopic/chapters/13_water_lc_lattice.tex:271` | "z/3 = 4/3 … tetrahedral coordination z=4 projected onto three channels" |
| `manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md:104`, `trampoline-analogy-primer.md:489`, `trampoline-framework.md:75` | "z=4 tetrahedral coordination" in Cosserat eigenmode / Maxwell-rigidity / K=2G form |
| `manuscript/ave-kb/vol3/gravity/…/trace-reversal-mechanism.md:25` | "K4 z=4 coordination fixes only the FORM K/G=f(ρ)" (K=2G form derivation) |
| `manuscript/ave-kb/claim-quality-closure-roadmap.md:107` | same K=2G FORM/VALUE row |
| `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md:184` | Kirkwood-Fröhlich "z=4 tetrahedral symmetry" |
| src/: `w_boson_loop`, `g_minus_2_lattice`, `transmission_line`, `cosserat.py`, `q_g47_*`, hexagonal_lattice, kit scripts | z=4 coordination in admittance/loop derivations + diamond-kit STL generators (engine code, migration territory) |

### (d) STALE-CITE — references to eq_axiom_1.tex line numbers/content that moved

| # | citing file:line | cites | problem | action |
|:--:|:--|:--|:--|:--|
| d1 | `vocabulary-register.md:466` (`def-7c3f9e` chirality, realization (a)) | `eq_axiom_1.tex:35` "Cold-lattice handedness on diamond … k_χ Cosserat order-parameter" | **content DELETED** from eq_axiom_1.tex by `63fea0ae` (LEAN). Line 35 is now a different sentence. | **FIX (this arc, per brief):** re-point to the surviving home (`src/ave/topological/cosserat_field_3d.py:115-124`, already co-cited) and drop the dead `eq_axiom_1.tex:35` cite (content no longer in the file). |
| d2 | `vocabulary-register.md:447` (`def-4b1a2c` K4, referent (b)) | `eq_axiom_1.tex:35` "The production computational net is z=4 diamond" | **content DELETED** by `63fea0ae` (+ SUPERSEDED by ratification). | **FIX (this arc):** re-point to the surviving in-axiom split (the ratified D1 block, line renumbered post-rewrite) or to `k4_tlm.py:97-119`. |
| d3 | `vocabulary-register.md:446` (`def-4b1a2c` K4, referent (a)) | `eq_axiom_1.tex:23-24` (identity) + `:18-21` (D1 adjudication) | line numbers shift after the rewrite; verify + re-pin | **FIX (this arc):** re-pin to the post-rewrite line of the identity sentence + provenance block. |
| d4 | `vocabulary-register.md:443` (`def-4b1a2c` canonical-home) | `eq_axiom_1.tex:18` | line shifts after rewrite | **FIX (this arc):** re-pin. |
| d5 | `unified-engine-design-doctrine.md:236` (Vol-4 leaf, flag-don't-fix block) | `eq_axiom_1.tex:37` "D1 adjudication, 2026-06-12 … z=4 diamond" verbatim | **content DELETED** by `63fea0ae`; the verbatim quote no longer exists at :37. | **FLAG-ONLY (NOT this arc's scope):** this is a Vol-4 circuit-theory leaf that owns its own flag-don't-fix record of the 2026-06-25-vs-.tex tension; its canon-propagation is the auditor-lane "propagate the 2026-06-25 ratification into eq_axiom_1.tex" item it itself names. Surfaced here for the auditor queue. |

---

## 3. THE NEW SENTENCE (verbatim) — see §THE-REWRITE below (filled at edit time)

## 4. Register / vocab findings (INVARIANT-S12)

- `def-4b1a2c` (K4): status **adjudicated**, production carrier = chiral srs z=3; `open-ambiguity-flag: YES`
  (3 referents) → the new sentence MUST carry the qualifying parenthetical the watch-list demands
  ("chiral Laves K4 = the degree-3 srs / Sunada-K4 net"). ✔ satisfied by the rewrite.
- `def-7c3f9e` (chirality): status **ambiguous**; production-vs-instrument split unadjudicated at the
  space-group level — the rewrite says the srs net is chiral (I4_1 32) as a STRUCTURAL name, consistent
  with the axiom naming, without asserting the achiral-diamond-realizes-chiral question (that stays open).
- No new term required minting. All load-bearing terms (K4, srs, Laves, Sunada, chirality, node,
  I4_1 32, coordination/z, Cosserat, micropolar) have register entries or are canonical.
