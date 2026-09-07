# PR #1020 picture-lock

**Status: LANDED 2026-08-29** on `research/2026-08-26-overbraced-crystal-walk` (PR #1020). Working-pad copy remains gitignored at `.agents/handoffs/2026-08-29_PR1020_picture-lock.md`. This file is the tracked record.

**Rewrite landed 2026-08-29.** [`2026-08-26_overbraced-chiral-crystal-walk_RECORD.md`](2026-08-26_overbraced-chiral-crystal-walk_RECORD.md) now teaches this signed set. Pre-rewrite teaching body is at `9efcc8db`. Do not start #1021. Do not mint `def-` on this PR. Spillover that is **not** that rewrite lives in [`2026-08-29_picture-lock-spillover.md`](2026-08-29_picture-lock-spillover.md).

**Ship-time currency 2026-09-06 (merge of #1020).** H1 close and S9 characterization live on PR **#1034** (files disjoint from this PR; merge this first). P2's "Gated on H1" / "do not start a derivation" below is the 2026-08-29 snapshot. Vocab amend of `def-69f472` remains later. Do not mint on this merge.

**Round 4 — 2026-08-29.** Mapping + ordinary flags walked. Pads landed.

**Status-word correction 2026-09-06 (class-1 demotion; correction-PR against `main`, since #1020 is merged).** Grant ratified 2026-09-03 that *signed* means “passed adversarial pass plus physical/logical review with me.” No such receipt exists for any picture in this file — the recorded receipts are chat nods, one recorded **uncertainty** (P1), and for P5 no Grant assent at all. Every `Status: SIGNED` header below is therefore demoted **in place** to **Grant-agreed (chat), WALK-GRADE, UNAUDITED** (P5 to **WALK-GRADE, UNAUDITED**), each with its receipt stated. **No finding is withdrawn; only the grading word moved.** The kills (P4), the CLOSED verdicts (P6/P7), and every mapping-failure call stand exactly as recorded.

**Scope of that demotion — enumerated.** The token `SIGNED`/`signed` survives as a *positive* grade in **14 further occurrences across 13 lines**, all of them derived restatements of the same five pictures, left **byte-unchanged** so the Lens-3 mapping audit and the Round-3 table stay as recorded: `:5`, `:114`, `:115`, `:116`, `:118` (Lens-3 Verdict cells P0 / P1–P2 / P3 / P5), `:128`, `:158`, `:171`, `:184` (**two** tokens), `:185`, `:231`, `:233`, `:247`. **All 14 carry the demoted grade above.** Deliberately *not* touched, because they are denials or future-tense asks rather than claims of signature: `:88` (“not a signed identification”), `:145` (“unsigned picture”), `:183` (“stays unsigned”), `:196` (“sign the epistemology … **do not** sign …” — a recommendation), `:237` (“waits on Grant sign-off”), `:254` (“not missing signs”). **Method:** `grep -n -i 'sign'` over this file, cross-checked against a full read of all 250 pre-correction lines; two grep hits were false positives (`assign` `:205`, `signal` `:219`), and this correction block’s own `:11`/`:13` carry the token as the *object* of the correction, not as a grade. **Blind spot:** a restatement of a verdict phrased *without* the token `sign` (e.g. “locked”, “settled”, “agreed set”) is not caught by the grep leg and would only be caught by the read leg, which was run once, by one reader.

## Pictures (resume)

### P0 — What “over-braced” is for

**Grant (2026-08-29):** Does not know what the vacuum *is*. Characteristic impedance ⇒ it is most likely a material. Chiral Laves K4 Cosserat crystal is the working description, not known to be right. Intuition: if it is a true solid crystal it would be incredibly dense/stressed, as if in the interior of a black hole; our vacuum an impedance bubble compressed by a host universe at still higher strain. Over-bracing / stress is what lossless propagation of *projected strain* would need; that is what matter and waves in our reality would need.

**Circuit restatement (partially agreed):** Prestressed A1 **compliance** (varactor headroom, H6) so .AC can stay on the reactive arc. Uniform host-universe bias would be unread common-mode. **Not** DC voltage on the Kirchhoff \(L\)-struts (H1). BH-interior / impedance-bubble is **cosmology-scale intuition**, not ontology.

**Status: Grant-agreed (chat), WALK-GRADE, UNAUDITED — for #1020.** Over-brace is for lossless projected strain; that strain is AC readout, not a second field. **(2)** and **(3)** parked as spillover S11 (Grant 2026-08-29: they are not this PR). *Receipt:* the recorded Grant line above is a working-description/intuition statement and the circuit restatement is tagged **partially agreed** — no adversarial pass and no logical review with Grant is recorded.

**Def:** parked in spillover S5. Not minted here.

### P1 — Where the 3D phase-space knot lives

**Grant:** The strain projected from a 3D phase-space knot. Cannot picture whether 3D phase space *is* the vacuum’s physical reality, or the mapping between the physical vacuum and projected strain in our reality. **This turn:** update P1 to match P2.

**Grant-agreed (chat), WALK-GRADE, UNAUDITED (2026-08-29):** The vacuum’s *space* is the lattice (graph). Phase space is **not** that space and **not** a discardable plot. It is the **native state-coordinate chart of the tanks on that graph** \((V_{\mathrm{inc}},V_{\mathrm{ref}})\). The knot is a winding in those coordinates. Observed / “projected” strain is the AC readout (and the real-space envelope \(S(A(r))\)).

**Canon:** `def-kn0t01` (status **SOLID**); `def-69f472` (ambiguous only for the A46 size leak). **Not canon:** “lattice-is-the-space” — `[branch:#1033]` unmerged, **zero reviews**, not in this PR’s tree; chat-agreed only. The phrase also has no canon leg of its own: 0 hits for the literal token `lattice-is-the-space` anywhere in the tracked tree outside this line (`grep -rn` over the repo, `.git` excluded; a canon leg phrased without that token would not be caught by that pattern).

**Status: Grant-agreed (chat), WALK-GRADE, UNAUDITED.** *Receipt:* the recorded Grant line above states **uncertainty** — “Cannot picture whether 3D phase space *is* the vacuum’s physical reality, or the mapping between the physical vacuum and projected strain in our reality” — not a review.

### P2 — Is phase space an analytical tool?

**Grant:** Agreed the honest sentence. Track it for vocab/`def-`. Most important next theory step: characterize how to **model** that chart and how it is **coupled** to the vacuum and to matter/light/gravity (or how bulk properties emerge).

**Grant-agreed sentence (chat, WALK-GRADE, UNAUDITED):** Phase space is the native **state-coordinate chart of the lattice tanks**, distinct from the graph that is physical space. Smith is a **ratio chart** of that state, not the state itself.

**Vocab:** amend `def-69f472` (do not mint a second noun). A46 size-leak flag stays until that leak dies. Not minted this session. Fiber-bundle noun stays WALK.

**Theory next step:** spillover S9 — characterization / coupling / bulk emergence. Prior art already exists (ladder, `clm-acdc07`, Round-3 table, H1–H6). Do **not** start a derivation until a prereg. Gated on H1.

**Status: Grant-agreed (chat), WALK-GRADE, UNAUDITED** (sentence; *receipt:* “Agreed the honest sentence” above). Coupling program is spillover, not #1020.

### P3 — Which amplitude?

**Grant:** Amplitude makes sense. Two-knob + stretch-sector **agreed** (2026-08-29 later).

**Dead as stated:** this run as a source-free electron finder, as an isolated-amplitude selector, as a gravity SYM \(L{+}C\) experiment, or as a Chern/degeneracy selector. Not dead as an A1 phasor-KCL **instrument**.

**Rerun the same setup:** no. Unitary \(M\) + Ax 3 is structural; seed/family will not become selective.

**Modify then rerun:** only as a **new** experiment (S8 Cosserat-wired HB; or an A1-only \(\ker Y\)/\(M\) study that does not claim the knot). Not a #1020 patch.

**Status: Grant-agreed (chat), WALK-GRADE, UNAUDITED** (dead as stated; *receipt:* “Two-knob + stretch-sector **agreed** (2026-08-29 later)” above). Instrument kept; Cosserat/SYM jobs are spillover.

### P4 — Chern / Berry / degeneracy selector

**Grant:** Feels imported from SM/QED/GR model weights.

**Status: KILLED as a substrate picture** (Grant + VERIFY; Grant confirmed 2026-08-29 resume). Keep as EXTERNAL / leak example. S4 leakage CI is spillover, not this picture.

### P5 — Bracing = couple-stress / pin-jointed solver

**Grant:** Does not understand; dig in more.

**Plumber restatement (not a new hypothesis):** The HB code under discussion only wires the stretch / A1 scalar channel. Neighbor-to-neighbor *twist* (Cosserat \(\gamma_c\), inductive lacing of flywheels) is not in that solver. If the object is a held twist, a stretch-only model is the wrong bench.

**Status: WALK-GRADE, UNAUDITED** (bench fact / instrument limit). **No Grant receipt at all:** the recorded Grant line above is *“Does not understand; dig in more”*, and no assent is recorded after the plumber restatement; the receipt for the bench fact is the author-stated code check below. “Therefore no knot” stays **KILLED**. Cosserat-wired HB = S8 later effort.

**HB code:** `src/ave/solvers/harmonic_balance_srs.py` — phasor KCL \(e^{i\theta}v=M(S)v\) on srs z=3. Scalar / A1-adjacent only. T2 not wired (module `:147–149`). Instrument-grade; mints no physics.

### P6 — Loop current vs scatter-map eigenvector

**Grant:** What’s the follow-up? (P7: do not pick; analyze.)

**Follow-up (spillover S10), not a #1020 rewrite:**
1. **Drop the weld.** Maxwell–Calladine does not identify the knot. Do not mint. Retrieve later if a count is actually wanted (Q1 / S5).
2. **Keep both operators as analysis arms** — (i) \(\ker Y\) DC loop current; (ii) \(M\)-eigenmode at \(\theta\). Same as P7. Glyphs split before any compute (\(\omega\) field vs rate vs \(\theta\)).
3. **Do not run this HB code as either arm for the knot.** P5: no T2. An A1-only \(\ker Y\) or \(M\)-spectrum is a stretch-channel study, not the Cosserat object.
4. Self-stress `def-` stays in S5 until the analysis has a noun that is not the weld.
5. Cosserat-wired instruments for both arms = later, with prereg.

**Status: CLOSED for #1020.** Follow-up is spillover S10 (and board `ker-y-vs-m-eigenmode`). Not a signed identification of the knot.

### P7 — Clause Q if \(\omega=0\)

**Grant:** Does not want to pick. Wants to **analyze**.

**Restated Q2:** two-arm analysis of (i) vs (ii), not a fork Grant must close. Canon already supports both on the same sector; that is why analysis exists.

**Clause Q:** a **lens on the DC arm** (reference-fixing / Q-point, R43: never “ground”). Not a verdict. Do not reuse it as AC phase-normalization.

**Needed for #1020:** nothing to pick. Rewrite must not treat Q2 as settled, and must not reuse clause Q as AC phase-normalization.

**Needed for the analysis (S10, not this PR):** Cosserat-capable instruments, glyph split, prereg of both arms, clause Q as a DC-arm lens only.

**Status: CLOSED for #1020 as “do not pick.”** Analysis lives in S10.

---

## Lens 3 — mapping (hub, not spoke-to-spoke)

**Regime (walk never declared it; §6.8 already flagged):** vacuum teaching is sub-yield lossless-reactive. The object the walk wanted (saturated core) is **not** Regime I. Truss / Maxwell–Calladine language is clean only below the band edge; at the rail it leaks.

**Rule:** spokes map to the hub. Direct X↔Y without a hub cell is a mapping failure. EE is operational, not ontological. Cosserat/elastic is co-equal. Do **not** mint `translation-circuit.md` rows here (H1 still held).

| #1020 picture / join | Spoke (what the walk wrote) | Hub cell (what it must be) | Verdict |
|---|---|---|---|
| P0 over-brace for lossless projected strain | civil “over-braced / hyperstatic”; BH-host cosmology | A1 varactor **headroom** so .AC stays on the reactive arc; uniform bias = unread common-mode. (a) vs extra KVL loops = S11 | SIGNED hub use. Spoke names are gloss. BH-host = cosmology spoke, unsigned (S11) |
| P1/P2 knot in phase space | “3D phase space” / 3D Smith | Tank-state chart \((V_{\mathrm{inc}},V_{\mathrm{ref}})\); Smith = \(\Gamma\) **ratio** (T4), not the state | SIGNED. Direct “Smith = phase space” would be a failure; not signed |
| P3 HB amplitude | (none if kept as \(A\)) | Ax4 envelope; \(Y=Y_0/\sqrt{S(A)}\); Z **moves** — not SYM \(L{+}C\) | SIGNED. Gravity Op19 is a **different** hub slot |
| P4 Chern / Berry / degeneracy | TI / SM band topology | **No hub cell.** Integer selector was supposed to be winding \((2,3)\) / \(\Gamma=-1\) wall, which this code cannot see | **MAPPING FAILURE.** KILLED. Direct Chern↔knot |
| P5 pin-jointed / bracing = couple-stress | civil pin-joint; trampoline “over-bracing = \(\sigma^A\)” | A1 stretch vs T2 **mutual-\(L\)** (\(\gamma_c\)). Scalar HB = no flywheel transformer | SIGNED as **instrument limit**. Hub already in trampoline + `translation-circuit.md`:101. Walk’s “therefore no knot” is not a hub statement |
| P6 Maxwell–Calladine / self-stress = knot | structural rigidity \(\ker(R^T)\) | \(\ker Y\) (DC loop, no terminal source) **or** \(M\)-eigenmode — two hub objects | **MAPPING FAILURE** as a weld. Hub split is S10. Do not mint MC |
| P7 clause Q as AC phase-norm | (wrong job) | Q-point / clause Q = **DC** reference-fixing | Already split. Rewrite must keep DC |
| Kane–Lubensky | topological-mechanics | none in corpus (0 hits) | EXTERNAL. Do not mint. Do not use as hub |
| RF free-running oscillator as amplitude selector | RF / Hopf limit cycle | Ax3 **forbids** the loss+gain pair that pins RF amplitude | Spoke import of a selector the hub lacks. Motivates looking at structure; does **not** license MC |
| Spiderweb | metaphor | not a cell | Keep as Grant metaphor only |

**Identity-collapse probe (do not collapse):**
- S5 over-braced senses (trampoline \(\sigma^A\) vs P0 headroom vs MC count vs lever) — KEEP-ALL.
- \(\ker Y\) vs \(M\)-eigenmode — Grant: **analyze**, do not pick (S10).
- Kernel \(A\) vs \(\varepsilon_{11}\) / Op19 \(n\) — two knobs, signed split.
- Clause Q vs AC phase-normalization — already two jobs.

**Hub cells the rewrite may teach:** A1 varactor headroom; tank-state \((V_{\mathrm{inc}},V_{\mathrm{ref}})\); A1 vs T2 (no mutual-\(L\) in this solver); \(\ker Y\) and \(M\) as **two** operators.

**Hub cells the rewrite must not teach:** Chern as knot; MC as knot; pin-jointed ⇒ no knot; Smith as the vacuum; HB \(A\) as gravity \(L{+}C\).

**Not landed in any spoke.** Mapping audit only.

---

## Lens 4 — ordinary flags (Tier-1; no rewrite)

PR files: walk record, `_orchestration/open-items/2026-08-26-overbraced-crystal-audit.md`, regenerated `BOARD.md`. No frozen prereg. Mints no `clm-`. Sampled load-bearing cites on `origin/main` this turn (HB `:147–149`, `master-equation.md:20`, trampoline-primer `:155`, trampoline-framework `:190`/`:560`, `translation-circuit.md:101`, `port-register.md:50`, `srs_cage_winding.py:402`/`:480`, `alpha_crystal_mc_count.py:259–275`, rim-inversion charge sentence).

| Sev | Axis | Finding |
|---|---|---|
| **BLOCKER for rewrite** | Overclaim / unsigned picture | §9.1: *“Nothing above shows the physical picture of §2 is wrong.”* Instruments died; picture-lock killed Chern, MC-as-knot, “therefore no knot.” A rewrite that keeps that sentence teaches the unsigned spiderweb ontology as still live. Walk banner already says WALK-GRADE — not a merge-BLOCKER of the *current* record if it stays WALK. |
| **FLAG** | BOARD.md | Diff vs `main` sets **0 PRs open** from a **non-main** tree. This PR is an open PR. Do not treat that BOARD as program state; drop or regenerate on main in the rewrite. |
| **FLAG** | EXTERNAL-UNRETRIEVED | Maxwell–Calladine, Kane–Lubensky, Berry/Chern, RF oscillator used **load-bearing**, honestly tagged. Mapping already killed the joins. Rewrite must not keep them as teaching. |
| **FLAG** | Cite / provenance | VERIFY receipts attributed to `scratchpad/chk3.py` — **0 hits** in the tracked tree. `[MEASURED-VERIFY-PASS]` is not reproducible from the PR. |
| **FLAG** | Cite grade | `vocabulary-register.md:510` tagged **[CANON-VERIFIED]** for CHARGE = static Link. Quote is in the node; the node is **`def-portmp` PROPOSED/gated**, not SOLID. |
| **FLAG** | Rule 1 | Grant-facing mechanism lines with no claim-id: *“the knot is in the stress”*; §5 *“the bracing IS the couple-stress.”* Acceptable only while WALK; rewrite must drop or attach grade. |
| **NOTE** | Freeze | No prereg body in this PR. §9.2 kill list is walk-invented, not a frozen-criterion mutation. Rule 2 N/A. |
| **NOTE** | Derived-as-given | No kernel-magnitude-wearing-constitutive identification found. “Over-braced by 3” is already flagged in-walk as coordination-number, not MC. |
| **NOTE** | Cite sample | HB T2-unwired, trampoline `:155`, couple-stress row `:101`, winding reader as seed function, A1⊥T2 at master-equation `:20` — **match**. Trampoline-framework `:560` quote omits “AND geometric \(r_{\mathrm{secondary}}/d\)” — not fabricated. |
| **NOTE** | Rule 12 | EOF status note correctly withdraws §1’s F1 *argument* (unitary \(M\) ⇒ 192 solutions) and keeps the *conclusion* on F5/F6. Do not quote §1 without that note. |

**Recommended hold (until rewrite):** do not merge; do not start #1021; do not land BOARD.md as-is; rewrite exclusions = mapping table + §9.1 sentence + EXTERNAL names as teaching.

**Rewrite 2026-08-29:** those exclusions are now the signed walk. Lens-4 rewrite-BLOCKER (§9.1 keeping §2 live) is addressed. `BOARD.md` restored from `origin/main` (not regenerated on this branch).

---

## Vocab queue (round 2)

| Term | Action | Status |
|---|---|---|
| over-braced | Mint `def-` after Grant picks which collision sense is canonical | DRAFT below; not minted |
| self-stress | Mint `def-` | DRAFT; not minted |
| hyperstatic | Likely gloss of over-braced; 0 hits on main before the walk | OPEN: useful? |
| Kane–Lubensky | Why-imported; 0 corpus hits | Explain; do not mint |
| knot | Adjudicate vs `def-kn0t01` | OPEN |
| phase-space | Amend `def-69f472` with P2 signed sentence (not a second `def-`) | TRACKED; not minted this session |

Synonym check: use `theorem-thesaurus.md` for **theorems**; `vocabulary-register.md` for **nouns**. Vocab lens must ask “synonym of an existing `def-` / TH-row?” before “new def.”

---

## Plan-document deltas (do not edit the plan file until Grant says)

1. Per-PR **picture-lock artifact** (this file’s shape); land on the PR branch when agreed.
2. Vocab lens: **synonym vs new def** via theorem-thesaurus + vocabulary-register.
3. P4-class: **leak lexicon** (warn vs fail) as a future CI; skill HARD-GATED.
4. Mapping + ordinary flags walked 2026-08-29. Rewrite next. Do not start #1021.
5. P0 (2)(3) parked spillover S11 (not #1020). BH-host stays unsigned cosmology intuition.
6. P1 SIGNED; P2 sentence SIGNED → `def-69f472` amend + S9 coupling characterization (prereg before derive).
7. P5 SIGNED (instrument limit). P6/P7 CLOSED for #1020; analysis = S10.
8. **Spillover tracker** (not the per-PR picture-lock): [`2026-08-29_picture-lock-spillover.md`](2026-08-29_picture-lock-spillover.md) — Kirchhoff wording PR, leakage CI, synonym lens, mapping audit holds, S9/S10. Do not fold into #1020 rewrite.

---

## Round 3 — 2026-08-29 — AC/DC gravity as network equations

**Grant (this turn):** The AC/DC gravity mapping is compelling. Document it. Step back: strain of the lattice should be modeled via **network equations**. Map each concept from the last reply 1:1 to an EE circuit.

**Correction to the last reply:** it still spoke as if \(\varepsilon_{11}\) were a continuum field and matter/light were probes *of* that field. On the hub, **the graph voltages and currents *are* the strain**. Continuum \(\varepsilon_{11}\) is the long-wave name for that DC solution, not a second object.

**Status of this table:** Grant (2026-08-29) said the mapping **makes sense**. Adversarial audit: sign the **epistemology** (AC readout of a DC differential on a real medium); **do not** sign “same scalar Kirchhoff mesh” or “\(\varepsilon_{11}\) is \(V\) on the \(L\)-edges” until the holds in [`2026-08-29_picture-lock-spillover.md`](2026-08-29_picture-lock-spillover.md) are closed. This work **does not edit** `kirchhoff-network-method.md`.

### Network equations (the model, not a metaphor)

Pinned pairing: **impedance analogy** (`def-1mpanl`, Grant 2026-07-21): **stress \(\leftrightarrow\) voltage**, **velocity \(\leftrightarrow\) current**, **displacement \(\leftrightarrow\) charge** (`translation-circuit.md:17–26`).

On the graph (K4-graph column owns KCL/KVL, `lattice-model-register.md`):

1. **KCL (cut-set / node):** \(\displaystyle C_i(V_i)\,\frac{dV_i}{dt} = \sum_j I_{ji}\). Mechanical: net force / self-equilibration. Same statement as TH-5 (KCL = Fredholm solvability).
2. **KVL (cycle / loop):** \(\displaystyle V_i - V_j = L_{ij}\,\frac{dI_{ij}}{dt}\) on a lumped strut; around a closed walk the voltages close. Mechanical: compatibility — you cannot assign independent stretches to every bond.
3. **Bond as distributed TL** (`def-b0nd01`): Telegrapher
   \(\partial_s V = -L'\,\partial_t I\), \(\partial_s I = -C'\,\partial_t V\).
4. **Constitutive:** A1 varactor \(C(V)=C_0/S(V/V_{\mathrm{yield}})\); Cosserat \(\gamma_c\) = mutual \(M\) between flywheel inductors.
5. **.OP (DC):** \(\partial_t=0\). Capacitors hold DC voltage (opens at \(\omega=0\)). Inductors short (\(V_L=0\)). DC **voltages** live on the A1 tanks = Q-point / prestress. DC **currents** may still circulate in inductive cycles = \(\ker Y(\omega=0)\) (this is the circuit object P6 was reaching for, without Maxwell–Calladine).
6. **.AC:** linearize \(C,L,M\) at the local .OP; the AC voltages/currents *are* light, matter internals, clocks.

**Pairing collision (do not paper over):** [`kirchhoff-network-method.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md):17–19 writes strut current \(I\) as “inductive flux **or physical lattice strain**.” That is the **mobility** pairing (current \(\leftrightarrow\) force/strain). It contradicts `def-1mpanl`. Round 3 uses TKI. The kirchhoff leaf’s *update equations* (\(V=L\dot I\), \(C\dot V=\sum I\)) are the right network; its *word* “strain” on \(I\) is not.

### 1:1 — last reply → circuit

| Last-reply concept | Circuit object (1:1) | Equation / SPICE name | Canon row | Grade |
|---|---|---|---|---|
| DC strain \(\varepsilon_{11}\) / Q-point \(A\) | DC **voltage** on the A1 varactor (bias \(V_Q\)); DC **charge** \(Q=\int C\,dV\) = static **displacement**. Constitutive \(C(V)\) is the map. Continuum \(\varepsilon_{11}\) = long-wave dilatation of those \(\Delta Q\). | .OP node voltages | `def-q1escn`; `translation-circuit.md:112`; bond-lc §1.3 | **HELD** — this PR’s own spillover holds it: [`2026-08-29_picture-lock-spillover.md`](2026-08-29_picture-lock-spillover.md):69 H5, *“\(\varepsilon_{11}\) as A1 Q-point is #1033 WALK-GRADE, not TKI-forced (stress vs strain)”*. Competing identification on `[branch:#1033]` (unmerged, zero reviews). TKI split stress vs strain is the honest 1:1 |
| AC is the readout, not a second strain field | Small-signal \(v(t), i(t)\) on the same net after linearization | .AC / HB | `clm-acdc07` (i); `.OP/.AC` tool row ⚠ | canon measurement; tool row consolidation |
| Light | Traveling wave on T2/EM ports: \(V_{\mathrm{inc}},V_{\mathrm{ref}}\) on the bond TLs | Telegrapher + scatter \(M\) | photon-ee-mapping; I/Q row | canon |
| Matter (soliton) | Self-biased multi-port: DC \(V_Q\) + AC winding (transformer turns) behind a \(\Gamma=-1\) wall | .OP then .AC around it | `resonant-lc-solitons.md`; \(\Gamma=-1\) short | canon re-expression |
| Uniform DC, unread | **Common-mode bias**: same \(\Delta V\) on every varactor. Rulers/clocks are the same network, so they ride it. | CMRR of an ideal differential instrument | `translation-circuit.md:115`; WEP-CMRR row is a **different** register (coupling vs readout) | canon influence-class |
| Gravity as *medium state* | Spatially varying **.OP field** \(\{V_i\}\) (Gauss-slot: DC voltages set by sources, not a propagating mode) | elliptic / constraint, not Telegrapher | `clm-acdc07` table: gravity \(= S(A)\) operating-point field | organizing principle 0.55 |
| Local \(n\), clock, \(c_{\mathrm{shear}}\) | Linearized \(L',C',\omega_0\) **at that cell’s** \(V_Q\) | \(\tau=\sqrt{L'C'}\); tank \(\omega=1/\sqrt{LC}\) | Op19, Op14, Op16; SYM row | Op19 linear-in-\(\varepsilon_{11}\) is **imported** \(\nu_{\mathrm{vac}}\) |
| Observable interaction (force, ray bend, dress) | **Differential bias**: \(V_i\neq V_j\) along the graph. GRIN electrical length; dress = varactors walk \(C(V)\). | \(\nabla V\) on the graph; \(\Gamma=0\) if SYM | `translation-circuit.md:116`; envelope `:119` | canon |
| “Just the local DC gradient” | Force/bend = **difference** of adjacent \(V_Q\). Clock rate at one node is a **value**, seen only by comparing two .AC clocks. | common-mode rejected; differential survives | same | last-reply split stands |
| SYM (gravity-class) | \(L'\) and \(C'\) **co-scale**, \(Z=\sqrt{L/C}\) pinned, \(\Gamma_{\mathrm{EM}}=0\) | matched GRIN TL | `translation-circuit.md:117` | canon; bond-\(L,C\leftrightarrow\mu,\varepsilon\) **unlicensed** |
| ASYM (not gravity) | Only \(C'\) (\(\varepsilon\)) grades; \(Z\) moves | mismatch, \(\Gamma\neq 0\) | `translation-circuit.md:118` | canon vacuum-mirror channel |
| \(\mathbf{u}_0=-\mathcal{A}_g\nabla\varepsilon_{11}\) | Net force from a voltage gradient | **unvalued** (R48) | bond-lc §1.5 | no circuit number |
| Topology / charge | Integer winding / flux linkage (transformer turns), **not** a voltage | holonomy on the graph; DC linking | `clm-acdc07` (topology); TKI | second DC class |
| P0 over-brace / prestress | (a) DC \(V_Q\) so AC swing stays on the reactive arc (class-A bias); (b) extra branches ⇒ extra KVL loops. Uniform host-universe bias = unread common-mode. | .OP bias; extra loops | not a `def-` yet | SIGNED for #1020 as lossless projected strain; (a) vs (b) and BH-host are S11 |
| P6 circulating “self-stress” | DC loop current in inductor cycles at \(\omega=0\) | \(\ker Y(\omega=0)\), \(V_L=0\) | TH-5; not Maxwell–Calladine | CLOSED for #1020; analysis is S10 |
| Phase-space knot | AC state of the tanks: \((V_{\mathrm{inc}},V_{\mathrm{ref}})\) / \((2,3)\) phasors. **Not** a geometric threading of the graph. | state vector of .AC | `def-kn0t01` | P1/P2 SIGNED |

**WEP caution:** `translation-circuit.md:156` CMRR for equivalence is **coupling-level** (gravitational charge \(\equiv\) inertial mass). Uniform-bias unreadability is **readout-level**. Same English word, two registers (`def-` common-mode KEEP-ALL).

**Not landed in the spoke.** This table is the picture-lock record. `ave-ee-first-mapping` Step 6 (new row in `translation-circuit.md`) waits on Grant sign-off. Most cells already exist as rows; the new content is the **join**: strain = the Kirchhoff solution, gravity-as-interaction = differential .OP.

---

## Artifact inventory (chat → files)

Workshop is the chat. Archive is these tracked files on PR #1020.

| Artifact | Holds |
|---|---|
| this file | P0–P7 signs/kills; Lens 3 mapping; Lens 4 ordinary flags; Round-3 1:1 table; vocab queue |
| [`2026-08-29_picture-lock-spillover.md`](2026-08-29_picture-lock-spillover.md) | S1–S11, H1–H6, Kirchhoff names, P2 sentence, S9 coupling, S10 dual-arm |
| [`../_orchestration/open-items/2026-08-29-kirchhoff-pairing-labels.md`](../_orchestration/open-items/2026-08-29-kirchhoff-pairing-labels.md) | S1 |
| [`../_orchestration/open-items/2026-08-29-acdc-gravity-circuit-map.md`](../_orchestration/open-items/2026-08-29-acdc-gravity-circuit-map.md) | S2 |
| [`../_orchestration/open-items/2026-08-29-phase-space-tank-state.md`](../_orchestration/open-items/2026-08-29-phase-space-tank-state.md) | S9 |
| [`../_orchestration/open-items/2026-08-29-ker-y-vs-m-eigenmode.md`](../_orchestration/open-items/2026-08-29-ker-y-vs-m-eigenmode.md) | S10 |

**Known holes (not missing signs):** vocab “DRAFT below” for over-braced was never written (senses live in S5); Kane–Lubensky never explained in-pad (do not mint). Full back-and-forth wording lives in the session transcript, not duplicated here. `BOARD.md` on this branch is **not** program state (Lens 4 FLAG); restored from `origin/main` on the rewrite land, not regenerated.
