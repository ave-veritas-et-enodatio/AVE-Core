# R40 demotion sweep — BATCH 2a (the 185 NEEDS-RE-DERIVATION rows)

### ENTRY 2026-08-12-r40-sweep-batch2a

**Class:** demotion execution. Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`, **moves no solidity
number**, adjudicates no channel, opens no fork. It changes the STATUS of already-written claims and
preserves every byte of their text (honesty-lag pattern, Rule 12).
**Authority:** R40, [`docket-entries/2026-08-10-rulings-r40-r42.md`](docket-entries/2026-08-10-rulings-r40-r42.md).
**Worklist consumed:** [`../research/drivers/r40_sweep_worklist_verified.json`](../research/drivers/r40_sweep_worklist_verified.json)
(banked by batch 0, PR #938); method record
[`2026-08-10_r40-sweep-scope-verification.md`](2026-08-10_r40-sweep-scope-verification.md); protocol
of record [`2026-08-11_r40-sweep-batch1.md`](2026-08-11_r40-sweep-batch1.md).

**Base:** cut from `origin/main` @ `a23a044b` (the #946 merge). `git status --porcelain` = 0 before
any edit. Batches 0 and 1 are merged (#938, #950).

**Scope, and nothing else:** the **185** rows binned `NEEDS-RE-DERIVATION`. The 105
`SURVIVES-AS-RESPONSE` re-scopes, the **4 beyond-floor supplement NEEDS rows**, and the two-method
straggler sweep are **BATCH 2b** and were not started.

---

## 1. What changed since batch 1 — the pointer is LANDED CORPUS, not a ruling record

Batch 1's notes pointed clause 4 at the R43/R44 ruling records, and its own §6 F10 routed the
improvement. Batch 2a takes it: **every note cites the landed artifact and cites a record only as
provenance.**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** / **G** / **Q**, canonical at
   [`../manuscript/common_equations/eq_axiom_5.tex`](../manuscript/common_equations/eq_axiom_5.tex):61,
   verbatim: `\medskip\noindent\textbf{G (bias coupling / bridge).} The operating-point \textbf{bias}
   $\varepsilon_{11}$ is the bound sector's potential, and the \textbf{bound response} $\mathbf{u}_0$
   is its gradient:`, with the register entry at
   [`../manuscript/ave-kb/common/axiom-register.md`](../manuscript/ave-kb/common/axiom-register.md):306,
   verbatim: `## Axiom 5 — Substrate DC Bias (deposit · grade · quiescence)`.

Under clause G the A1 / bulk slot is a **bound response** — mechanism gloss **back-reaction** — with
no independent propagating branch, no port, and zero longitudinal characteristic speed. A bulk *wave
speed*, a bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have no
referent, which is exactly what each NEEDS row owes a re-derivation against.

**R48 discipline, carried in every note.** $\mathcal{A}_g$ — the **bias-coupling area** that enters
clause G and nowhere else — is an `UNVALUED-RATIFIED-CONSTANT`
([`../manuscript/ave-kb/common/interlock-register.md`](../manuscript/ave-kb/common/interlock-register.md):370,
verbatim: `### 𝒜_g — the bias-coupling area *(R48: UNVALUED-RATIFIED-CONSTANT; the count STAYS 3)*`).
**No note writes $\mathcal{A}_g$ as valued, and no note implies the calibration count moved** — it is
`3` at `interlock-register.md`:12, verbatim: `expected-independent-count: 3`.

**R49 pointer, where a row's re-derivation runs through the elliptic bias law** (2 rows, §4): that law
carries the **declared 4π source convention**, canonical at
[`../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md):25,
verbatim: `> -\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)`
(`clm-rd9cjm`). Corrections of that class are **R31-style dated corrections**, not re-ratifications.

### 1.1 The honesty rider, cited from the axiom's own text

**THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt.** The rider is quoted from
`eq_axiom_5.tex`:86 — its own phase-structure paragraph, clause **(c1)** — verbatim:
`\textbf{(c1) THE BIAS PROPAGATION THEOREM --- this axiom's STANDING DEBT.} Clause G's elliptic law is the \emph{static abstraction of underived finite-speed bias dynamics}`,
and, on the same line,
`\textbf{The $(u,\pi)$ no-signalling theorem does NOT cover the bias read}`.

**147 of the 185 rows carry the rider** (row-header tag ⚑ **BIAS-DEBT**, counted from the landed
notes, not from the plan): their re-derivation turns on finite-speed bias dynamics, so their
resolution is *the ratified axiom WITH that debt standing* — never a closed replacement.

**Batch 1's mis-attribution is not repeated, and its known-stale upstream is not propagated.** The
rider is cited from `eq_axiom_5.tex`'s (c1), **not** from
[`2026-08-10_bias-propagation-brief.md`](2026-08-10_bias-propagation-brief.md), whose `:11` carries
the R50/R49(b) mis-attribution named as a standing open debt in batch 1 §8. That brief is referenced
nowhere in this batch's 109 notes.

### 1.2 Vocabulary — R50, and R49(b) for *retardation*

Canonical nouns authored in all 109 notes: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is the
mechanism gloss. *dress*, *grade*-as-canonical-noun and *halo*-for-the-physics (use the **near-field
store / added-mass**) are retired by **R50**; ***retardation* is retired by R49(b), not R50** — the
mis-attribution batch 1 had to correct across 42 notes. Two methods on this batch's authored prose
confirm compliance (§7). Corpus text quoted in the notes is byte-exact and is never reworded.

---

## 2. Method — line-count first, then zero line shift

**Line-count census BEFORE any edit (mandated).** A Python `os.walk` + `re` enumeration over **4196**
tracked text files finds **6221** inbound `path:NN` line-cites resolving into the **109** target
files — `constants.py` 988, `master-equation.md` 521, `cosserat_field_3d.py` 415,
`translation-circuit.md` 400, `vocabulary-register.md` 237, `crystal_engine.py` 170,
`resonant-lc-solitons.md` 170, `port-register.md` 136, … **Zero** target files have no inbound cite.
Inserting a note in body would have moved thousands of them.

So the batch is **append-only at the line level**:

- **Same-line status stamp** at each live-canon site — appended at end of line, or inserted before the
  row's final `|` (markdown tables), before the closing `\\` (LaTeX table cells), or as a trailing `%`
  comment (TikZ node lines). The claim text is preserved byte-for-byte inside the stamped line.
- **One dated note at EOF per file** — the four-clause header, the rider, and per row the verbatim
  quote + the verbatim banked rationale + the resolution pointer.
- **No line is inserted or deleted above EOF in any file.**

**Stamp string** (guard-visible by construction, see §6 F3): markdown
`🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this
file]**`; LaTeX the `\textbf{…}` form; Python the bare-bracket form.

**Note carrier, and a stated deviation from batch 1.** `.md` notes are markdown prose. **`.tex` and
`.py` notes are entirely `%` / `#` comment blocks** — batch 1 rendered its `.tex` header prose and put
only the per-line detail in comments. The deviation is deliberate: the verbatim quotes carry `_`,
`&`, `#`, `$` and raw LaTeX, and `make verify` does not compile LaTeX, so rendered prose would put a
build break where no gate could see it. The same-line stamp IS rendered in `.tex`, so a reader of the
claim still sees the status; the note is an audit ledger. **Stated, not slipped.**

**Verbatim quotes and rationales sit inside fenced blocks in `.md` notes.** They frequently contain
`path:NN` strings from the banked audit; a fence keeps them byte-exact, keeps `verify-md-links` off
literal link syntax, and keeps `verify-new-cite-excerpts` from re-classifying quoted corpus cites as
cites this batch authored. The batch's own artifact pointers are cited **by artifact + named clause,
without line numbers**, in the notes — line cites with verbatim excerpts live in *this* record, which
is the one file where they can be maintained.

**Display math and TikZ are never edited.** Three relocations, both lines recorded in every case:
`biquaternion-complex-coupled-network-equations.md`:166 → stamped at `:163` (the resultbox title;
the `$$` block is byte-untouched); `eq_universal_operators.tex`:10 → stamped at `:12` (mid-sentence
inside the `%` comment run `:8-12`, so the stamp goes at the run's end per the batch-1 protocol); and
the three TikZ node lines (`k4_irrep_decomposition.tex`:38/:72, `moduli_relationship.tex`:36) take a
trailing `%` comment stamp so the drawn figure is unchanged.

**Truth-break rule.** A stamp that would make the surrounding sentence false goes to the findings
unnoted. **Zero rows hit that rule.** One generated note line WAS factually wrong and was repaired
by hand rather than left (§6 F5).

## 2.1 The preserved-span census — 185 anchors, 62 flagged, every flag hand-read

The 185 anchors were scanned with the **landed** container-aware detector
([`../research/drivers/r40_preserved_span_number_check.py`](../research/drivers/r40_preserved_span_number_check.py),
`flags_for()`, both spec extensions live). **62 anchors flagged.** Every one was hand-read against its
own declaration.

**The adjudication rule this batch applied, stated so it can be argued with:** a fence requires a
declaration that **delimits a region** ("this box", "the tables above", "the bullets beneath", "all
notes above", "the line above") **and** the anchor must lie in that region. A bare "body preserved", a
"prior wording preserved *here* (inside this comment)", a "record X is preserved" naming an
`_orchestration/` artifact, and a physics sentence containing the word *preserved* are **not**
delimiting declarations. Where the named object plausibly INCLUDES the anchor, the row is routed to
the ledger rather than argued — routing costs only in-place visibility and never risks a breach.

**`KEEP-BOTH` was adjudicated PER SITE, never class-excluded** (batch 1 withdrew the class rule). All
12 `KEEP-BOTH` hits in this batch are **sense (ii)** both-objects-retained; the sense-(i) sites named
in batch 1 (`01_appendices.tex:57`, `vol4/claim-quality.md:487`, `08_gravitational_waves.tex:149`) are
not among this batch's anchors.

**Verdict: 7 genuine, 55 false positive.** The seven genuine fences take **no in-body stamp**; their
rows are routed to the governing file's EOF ledger with the span byte-untouched, per R39.

| # | site | the delimiting declaration |
|---|---|---|
| 1 | `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md:128` | `:133` — *"tables above PRESERVED unedited"*; `:128` is a row of those tables |
| 2 | `manuscript/ave-kb/vol2/claim-quality.md:1061` | `:1062` — *"claim PRESERVED, status honestly tagged"*; `:1061` IS that claim |
| 3 | `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:220` | inside the Rule-12 preserved Q1-REVERT warningbox `:188-242` — the SAME box batch 1 breached at `:208` and reversed |
| 4 | `manuscript/ave-kb/common/engine-capability-map.md:29` | `:21` / `:23` reframe banners, *"Rule 12 — body preserved"*; the DOF table is the governed body. **Conservative call** — the declaration is non-delimiting, so this is routing under doubt, not a proven fence |
| 5 | `manuscript/ave-kb/common/engine-capability-map.md:31` | as row 4 |
| 6 | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20` | `:40` — *"all notes above PRESERVED unedited"* (and `:36` *"bullets above PRESERVED unedited"*); `:20` is a note above both |
| 7 | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:26` | as row 6 |

**Rows 6 and 7 were caught LATE — by the forward guard, after the first commit — and the correction
is on the record rather than squashed away.** The first-cut adjudication used an ±8-line
upward-declaration probe; `master-equation.md`'s governing declaration sits **+20** and **+14** lines
below the anchors. Widening the probe to 45 lines surfaced them. Both stamps were **removed** and both
rows re-routed to the file's EOF ledger. **This is the third instance in this arc of a
distance-limited probe missing a real declaration** (batch 1's window detector missed one at +32);
the durable lesson is that *any* window on this corpus is wrong — only the container is right, and the
container must be read in the direction the declaration points.

**The 55 false positives, by adjudicated class** (rows sum to 55; every site and its reading is in
`GUARD_ADJUDICATED_FP` in the detector, and the same readings are the machine half of this table):

| class | n | reading |
|---|---|---|
| declaration HOLDS the prior wording **inside a `%`/`#` comment**; the stamped line is the live replacement | 13 | e.g. `09_mechanical_characteristics.tex:61` (decl `:63` quotes the superseded row verbatim inside the comment `:63-70`) |
| `KEEP-BOTH` matched in **sense (ii)** (both-objects-retained) | 12 | e.g. `03a_device_circuit_models.tex:79` (decl `:49`, *"Which operating point (KEEP-BOTH --- two distinct quantities)"*) |
| declaration preserves an **inline superseded quotation on its own line** | 10 | e.g. `port-register.md:87` (decl `:95` carries the superseded verdict text AT `:95`; `:87` is the live row) |
| declaration names a **different identified object** (a printed figure, a status line, a candidate, a table) | 10 | e.g. `device-circuit-models.md:201` (decl `:209` preserves *"the original status line above"* = `:207`) |
| **pure lexical match** — a physics sentence, or a ruling record preserved elsewhere | 8 | e.g. `eq_axiom_4.tex:55` (decl `:41` = *"Impedance preserved"*); `21_black_hole_interior_regime_iv.tex:200` (decl `:207` preserves an `_orchestration/` ruling record) |
| **self-match on this batch's own EOF note** | 3 | `04_dc_electrical_characteristics.tex:117`, `16_cross_volume_reference.tex:86`, `srs_cage_winding.py:313` — batch 1 named this class at `bulk_rarefaction_sector.py:129` |

---

## 3. The reconciliation identity

Stated as a sum and reconciled against the banked worklist:

```
  176   NEEDS rows  — stamped in place + dated EOF note   (on 175 distinct lines; one line
                      carries two rows: 15_black_hole_orbital_resonance.tex:31)
+   7   NEEDS rows  — R39 BYTE-FENCE ROUTED to the file's EOF ledger (no in-body stamp)
+   2   NEEDS rows  — STUCK-POINT: unactioned, unstamped, routed to Grant (§5)
+   0   NEEDS rows  — frozen-doc surface notes
= 185   NEEDS-RE-DERIVATION rows  ✓ reconciles with bin_counts_rederived["NEEDS-RE-DERIVATION"] = 185
```

Cross-checks:

- **frozen-doc surface notes = 0.** No NEEDS row lands in a dated `research/*_result.md`, a
  `prereg-FROZEN`, or a preserved-historical document — the 109 files are manuscript volumes, KB
  leaves/registers, and engine modules. Same as batch 1; nothing needed the surface-note-only path.
- **Blocked / truth-break rows = 0.**
- **Files carrying a dated EOF note = 109** — every file holding at least one NEEDS row, including
  all four files holding a byte-fence-routed or STUCK row (whose notes ARE the routed ledger entries).
- **Rider/scope tags, counted from the landed notes:** 147 ⚑ BIAS-DEBT · 24 ⚑ PAST-WALL · 2 ⚑ R49.

---

## 4. Per-class disposition

| Class | Rows | Disposition | Where |
|---|---|---|---|
| NEEDS — stamped | **176** | same-line status stamp + dated EOF note carrying the four-clause header, the R48 discipline, the rider and, per row, the verbatim quote + verbatim banked rationale + the resolution pointer | 109 files across `manuscript/ave-kb/`, `manuscript/vol_*`, `manuscript/{backmatter,frontmatter,common_equations}`, `src/ave/` |
| NEEDS — R39 byte-fenced | **7** | **no in-body stamp**; note routed to the governing file's EOF ledger with a pointer and the declaration quoted | §2.1 table |
| NEEDS — STUCK-POINT | **2** | **unactioned and unstamped**; full STUCK-POINT report at §5 | `appendices-overview.md:95`, `vol4/claim-quality.md:252` |
| — of the 176, PAST-WALL-scoped | 24 | the demotion is **scoped**: clause G resolves the cold, sub-yield side; the saturated-interior phase is one `eq_axiom_5.tex` explicitly does **not** write (*"the $D(A)\to\infty$ wall behaviour is past-wall-adjacent and \textbf{not written here}"*, with the de-bonded and pre-freeze phase forms named-open at (c3)/(c4)). Neither discharged nor adjudicated | in-note tag |
| — of the 185, BIAS-DEBT-ridden | 147 | resolution = the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** | in-note tag |
| — of the 185, R49 4π-convention | 2 | `saturating-modulus-and-backreaction.md:59`, `vol4/claim-quality.md:369` — the elliptic bias law carries the declared 4π source convention; R31-style dated-correction class | in-note tag |

---

## 5. STUCK-POINTs — 2 rows, unactioned, routed to Grant

Both are rows whose **resolution pointer is genuinely ambiguous**: the banked rationale poses a
sector fork that no landed artifact selects, so naming Axiom 5 as the resolution would *pick an arm*
and manufacture a false discharge. Two attempts were made on each (read the row's leaf in context;
read the banked rationale against clause G) and both stopped at the same fork.

### STUCK-1 — `manuscript/ave-kb/common/appendices-overview.md:95`

- **Row (banked):** family `dark-wake-reaction-mass`, `uncertain: true`, `site_verdict: VERIFIED`,
  re-verified at HEAD by both engines.
- **Quote (byte-exact at HEAD):** `thrust metric via acoustic steepening: ∂_t ρ + ∇·(ρ v) = 0 with
  c_eff = c_0√(1 + ρ̄/(1−ρ̄²))`
- **Banked rationale, verbatim:** *"Thrust-metric 'acoustic steepening' PDE: if c_eff is the T2/EM
  index modulated by density it survives as refraction; if it is the compression carrier it dies —
  sector declaration owed."*
- **What is ambiguous:** the row's own rationale makes the disposition conditional on **which sector
  `c_eff` names**. If `c_eff` is the T2/EM index, the row is not an A1 consumer at all and Axiom 5
  clause G is the wrong pointer; if it is the compression carrier, clause G is the pointer and the
  mechanism dies. Nothing in `eq_axiom_5.tex`, the axiom register, the interlock register or R49
  selects the arm.
- **Candidate readings considered:** (a) point at clause G and note the fork in the note — rejected:
  it reads as a discharge and the note's own resolution sentence would assert the compression arm;
  (b) point at *both* arms — rejected: a note that says "either the axiom resolves this or the row is
  out of scope" is not a resolution pointer; (c) leave unstamped and route — taken.
- **What is needed to proceed:** a sector declaration for `c_eff` in the thrust-metric PDE (T2/EM
  index vs A1 compression carrier), from Grant or from the owning propulsion lane.
- **Recommendation:** route to the lane that owns the thrust metric for a one-line sector
  declaration, then re-bin. If it is the T2/EM index the row is arguably not a NEEDS row at all.

### STUCK-2 — `manuscript/ave-kb/vol4/claim-quality.md:252`

- **Row (banked):** family `dark-wake carrier`, `uncertain: true`, `site_verdict: VERIFIED`,
  re-verified at HEAD by both engines.
- **Quote (byte-exact at HEAD):** `Momentum conservation closed by the "Dark Wake" — equal-and-opposite
  longitudinal shear strain into the lattice, propagating at $c_0$`
- **Banked rationale, verbatim:** *"Uncertain carrier: if the wake is a compression/bulk radiated wave
  it is a bulk radiative port (dies); if it is Cosserat-shear-carried it is untouched. Wording is
  ambiguous ('longitudinal shear'); the dark-wake is separately banked WRONG-REGIME, but the
  momentum-closure mechanism as stated consumes a propagating longitudinal carrier — re-derivation
  owed."*
- **What is ambiguous:** the corpus phrase **"longitudinal shear strain"** names two different
  objects depending on reading — an A1 dilatation (dies under clause G) or a Cosserat/T2 shear
  carrier (untouched). The row is *also* the register home of a claim separately banked
  **WRONG-REGIME**, so a status stamp here risks stacking two different demotions on one line.
- **Candidate readings considered:** (a) treat "longitudinal shear" as A1 and point at clause G —
  rejected: the phrase is self-contradictory in canonical vocabulary and picking A1 is a guess;
  (b) treat it as Cosserat-shear and mark the row surviving — rejected: that is a re-bin, which this
  batch has no authority to do; (c) leave unstamped and route — taken.
- **What is needed to proceed:** an adjudication of the phrase *"longitudinal shear strain"* against
  the canonical sector vocabulary (A1 dilatation vs Cosserat shear), and a ruling on whether the
  WRONG-REGIME banking already covers this register row.
- **Recommendation:** adjudicate the phrase first (it is a `def-`-shaped vocabulary question, not a
  physics fork); the row's disposition then falls out mechanically.

---

## 6. Findings surfaced, not fixed

**F1 — the forward guard's `GUARD_ADJUDICATED_FP` registry does not scale, and the batch registered
into it anyway.** The registry keys on the full stripped line bytes. This batch's flagged lines have
a **median length of ~718 characters** (longest **12 910**), so 56 keys is ~65 kB of literal blob in a
678-line gate module. It is machine-correct and hand-unauditable at once: a reviewer cannot check 56
multi-hundred-character keys, and any re-wrap of a stamped line silently re-flags. **The batch did
not re-key the registry** — that is a gate-design change and belongs to whoever owns the gate. The
reviewable half of the adjudication is §2.1's class table plus the per-entry reading comments.
**Recommendation:** re-key on `(file, stamp-token, short digest of the line)`, or on the anchor's
banked claim-quote, and keep the readings where they are.

**F2 — the guard was BLIND to this batch until the first commit landed, exactly as batch 1 warned.**
Run on the working tree, `origin/main..HEAD` is empty, the added-line map is empty, and the guard
reports *"0 added stamped line(s) scanned, 0 flagged"* — a trivial pass. Run against the landed
commit it scanned 177 and flagged 58. **A guard report from an uncommitted tree is not a guard
report.** This is the same trap batch 1 documented for `verify-new-cite-excerpts`; it now has a
second instance, in a second gate, which makes it a property of this repo's diff-based gates rather
than a quirk of one of them.

**F3 — the guard's `STAMP` regex hard-codes the batch-1 date, and this batch is only visible to it by
coincidence of dating.** `STAMP = re.compile(r"DEMOTED 2026-08-11|TAG DEMOTED 2026-08-11")`. Any
future batch whose stamp carries a different date is **invisible** to both the pinned scan and the
live forward guard, which would report a clean run over a batch it never examined. This batch's stamp
deliberately contains the literal token `DEMOTED 2026-08-11` (today's date) so the guard actually
gates it — but that is a property of the calendar, not of the design. **Surfaced, not fixed:**
generalising to `(?:TAG )?DEMOTED \d{4}-\d{2}-\d{2}` is a one-line change to a landed gate, and
whether it perturbs the pinned batch-1 fixture numbers must be measured before it lands, not
assumed. **Routed.**

**F4 — 2 of the 7 byte-fences were found only by the guard, after the first commit.** §2.1. The
in-batch probe was distance-limited (±8 lines) where the real declarations sat at +20 and +14. The
corrected census, the removed stamps and the re-routed rows are all in this record and in the
second commit; the first commit's message states 178/5/2 because that was true of its tree.

**F5 — one generated note line was factually wrong and was repaired by hand.** The `.tex`/`.py` note
generator described *every* stamp relocation as "anchor is display math". At
`manuscript/common_equations/eq_universal_operators.tex` the relocation reason was different — the
anchor `:10` sits mid-sentence inside the `%` comment run `:8-12` — so the note asserted something
false about the corpus. Repaired in place to state the real reason and the real stamped line
(`:12`). **A generated note is still an authored claim.**

**F6 — the derived `.index/` moved by exactly 3 records, and the movement is the stamp text.**
`make refresh-kb-metadata` reports *"Rewrote solidity in 0 claim-quality.md file(s) (0 solidity
line(s), 0 depends-on annotation(s) changed)"* and *"Rewrote leaf-references footer in 0
claim-quality.md file(s)"*. The 3 changed records are `def-l0ngdu` and `def-ncsatw`
(`adjudicated_meaning`) and `clm-m3z5ux` (`rationale`) — each because the stamped line feeds that
derived field. **No solidity number moved anywhere in this batch**, no `status:` field of any `def-`
node moved, and the derived file is committed **regenerated**, not hand-edited (batch-1 F4 class).

**F7 — the engine edits are documentation-only.** Every added line in `src/` is a `#` comment or
docstring prose; the only modified pre-existing lines are the 29 stamped ones. `py_compile` is clean
on all 24 edited modules. No code path, constant, default, flag or numeric changed. Any *live*
re-scope of the coded bulk sector belongs to the engine lane, and the notes say so.

**F8 — the two batch-1 mixed-bin lines behaved exactly as batch 1 predicted.**
`port-register.md:49` already carried batch 1's `🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]**`
stamp; this batch's stamp was appended after it, still inside the final `|`, and the batch-2a note
carries the NEEDS row's own quote and rationale. `vol9/ch9-mechanical-characteristics/index.md:11`
is not among the 185 (its co-resident NEEDS row is at another line in the same file). Batch 1's F7
disclosure is discharged for `port-register.md:49`.

**F9 — a link-generation defect was caught by the gate, not by review, and is worth carrying.** The
note template used the placeholders `PREFIX` / `KBPREFIX` / `RESPREFIX`; replacing `PREFIX` first
mangled `KBPREFIX` into `KB<prefix>`, producing **124 broken intra-repo links** across 62 files.
`verify-md-links` caught all 124 as gating errors. Repaired before the first commit. The lesson is
generic: **ordered substring replacement on overlapping placeholder names is a defect generator**;
the gate is what made it a 10-minute fix instead of a corpus rot.

---

## 7. Counts re-taken AFTER the edits, two methods, engines + tree-state named

**Tree state:** branch `docs/2026-08-12-r40-batch2a`, base `origin/main` @ `a23a044b`. The receipt
below is measured over the **109 corpus files** at the second commit (the tip that carries the two
un-stamps and the guard registry). *A receipt that describes a prior tree is not a receipt.*

- **METHOD 1 — `git diff --unified=0` hunk-shape analysis vs `origin/main`** (engine: `git` 2.x +
  Python `re`): over the 109 files, **171 in-place hunks** (old-count == new-count ⇒ no shift),
  **109 EOF-append hunks**, and **0 SHIFTING hunks**. Scope, stated so it cannot be over-read: the
  receipt covers the 109 corpus files and **excludes** the derived
  `manuscript/ave-kb/.index/`, `_orchestration/`, and `research/drivers/`. Those carry no `path:NN`
  line anchors into themselves from the corpus (`r40_preserved_span_number_check.py` has **0** inbound
  line-cites, measured), so the exclusion is a stated scope, not a silent one.
- **METHOD 2 — independent line-by-line comparison against `git show origin/main:<file>`** (engine:
  Python, no git plumbing beyond the blob read): **50 680 original lines checked**, **175 modified
  original lines**, **0 violations**, **0 truncations**. Every modified line is **stamp-only** — the
  original text is preserved byte-for-byte once the inserted stamp string is removed.

⇒ **Every one of the 6221 incoming `path:NN` cites into these files still resolves to its original
content.** The 175 modified lines reconcile with the identity's 176 stamped rows on 175 distinct
lines (§3).

**Gates, on the landed commits:**

| Gate | Result |
|---|---|
| `make verify` | **PASS**, exit 0 |
| `research/drivers/r40_preserved_span_number_check.py` | **PASS** — pinned batch-1 scan 60/24/0 unchanged; live forward guard **175 added stamped lines scanned, 0 flagged**; regression fires on the known breach; both spec extensions live |
| …`--mutation-receipt` | **PASS** — 9/9 probes hold, including **M6d** (the FP registry is narrow: right key suppresses, wrong file or wrong bytes do not) |
| `make verify-new-cite-excerpts CITE_BASE=origin/main` | **PASS**, run against the LANDED commits (§6 F2) |
| `make test` | **PASS** |
| `python -m compileall` / `py_compile` on the 24 edited engine modules | clean |

**Vocabulary compliance, two methods** over the prose this batch AUTHORED (the 109 EOF notes and this
record, excluding every verbatim corpus quote, which is byte-exact and never reworded): shell
`grep -c` and an independent Python `re.findall` over the same bytes both return **0** authored uses
of *dress*, *retardation*, *grade*-as-ε₁₁'s-noun, and *halo*-for-the-physics.

---

## 8. What batch 2a did NOT do, and its named open debts

- The **105 SURVIVES-AS-RESPONSE** re-scopes: untouched.
- The **4 beyond-floor supplement NEEDS rows** — `sm-translation-toolchain.md:28`,
  `schrodinger-from-circuit.md:28`, `gup-derivation.md:55`, `coupled_resonator.py:605` — **not
  actioned.** Batch 1 actioned its single supplement DIES row and reported it separately; this batch
  read its brief's *"the 185 rows binned NEEDS-RE-DERIVATION, and nothing else"* as excluding them.
  **★ NAMED OPEN DEBT, routed to the orchestrator:** they are beyond-floor rows of the same bin and
  should be swept with batch 2b unless the orchestrator wants them folded back here.
- The **two-method straggler sweep**: not run.
- **No re-binning.** Two rows the banked rationale itself flags as possibly mis-binned
  (`03a_device_circuit_models.tex:113` is batch-1 F3's DIES-vs-NEEDS candidate, and STUCK-1 may not
  be an A1 consumer at all) are **noted, not re-binned** — a demotion sweep has no authority to move
  a bin.
- **No live re-scope of engine behaviour**, no flag default changed, no channel enumeration rewritten.
- **No `status:` field of any `def-` node moved**, no solidity moved, no `clm-`/`sup-` minted or
  retired.
- **★ NAMED OPEN DEBT — the guard registry's scaling defect is registered-into, not repaired** (F1).
- **★ NAMED OPEN DEBT — the guard's date-hard-coded `STAMP` regex** (F3): the next batch dated other
  than `2026-08-11` is invisible to the gate unless it is generalised first.
- **★ INHERITED, STILL OPEN — batch 1's two named debts are untouched by this batch:** the #938
  supersession note owed on `2026-08-10_r40-sweep-scope-verification.md` (`:61` / `:79` still assert
  5 DRIFTED rows), and the R50/R49(b) mis-attribution at `2026-08-10_bias-propagation-brief.md:11`.
  This batch **does not propagate** either: its re-derivation ignores the stale DRIFTED bin (§9) and
  its rider cites `eq_axiom_5.tex` rather than the brief.
- **★ SURFACED — batch 1's F1 R42 referent-drift is unchanged and now has a second consumer.** The
  ruled label `engine-artifact-pending-constitutive-law` names a debt the ratified axiom closed;
  the genuinely outstanding debt is THE BIAS PROPAGATION THEOREM. This batch stamps
  `engine-acceptance-suite.md:177` (the T3.1 body, a NEEDS row) two lines below that tag without
  touching the label. Still Grant's adjudication.

---

## 9. The re-derivation of the 185, at HEAD, before any edit

Verify-before-cite: the bank was pinned at `6c291196` and two merges have landed since, so the set and
every site were re-derived rather than trusted.

**The split, recomputed — not read off a headline.** A `Counter` over the JSON's own `rows` array
returns `59 DIES / 185 NEEDS / 105 SURVIVES`, agreeing with the JSON's `bin_counts_rederived`.
**Shell cross-check** on raw bytes: `grep -o '"bin": "NEEDS-RE-DERIVATION"'` → **190**,
`DIES` → **60**, `SURVIVES` → **109**. The excess reconciles exactly: `190 = 185 table + 4 supplement
+ 1 re-pin block row`, `60 = 59 + 1 supplement`, `109 = 105 + 4 re-pin block rows`. **No drift in the
split.**

**Site verification, two independent engines** (the batch-0 method as strengthened by batch 1 §5 —
*a single probe on this table has a ~20× false-drift rate*):

- **ENGINE 1 — hard-reduction character scan.** Quote and target both reduced to `[a-z0-9]`; LaTeX
  command names blanked **length-preservingly** so the per-character line map stays aligned (the
  first cut used a length-*changing* substitution and reported drift of up to 45 lines — a
  self-inflicted false-drift event, caught and fixed before any verdict was recorded).
- **ENGINE 2 — token-containment sliding window.** Both sides reduced to alphanumeric tokens; every
  k-line window (k = 1…6) scored by `|quote ∩ window| / |quote|`. Order-insensitive, gap-tolerant,
  different failure modes.

| verdict | rows |
|---|---|
| exact at the cited line on BOTH engines | **164** |
| residual, hand-read → content present at the anchor | **21** |
| DRIFTED | **0** |

All 21 residuals are wrapped-line or rendered-vs-source artifacts (a quote spanning the anchor and
its continuation lines; rendered prose vs LaTeX-in-markdown source) — the classes batch 0 and batch 1
both named. **Shell cross-check:** every cited file exists and every cited line is in range
(`MISSING=0 OUT_OF_RANGE=0`). **185/185 verify at HEAD; zero anchors moved.** No batch-2a note is
written against a stale anchor.
