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

**146 rows carry the rider in the landed corpus** (row-header tag ⚑ **BIAS-DEBT**, counted from the landed
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
confirm compliance (§7). Corpus text quoted in the notes is reproduced from the banked audit and is
**content-verified at HEAD (markup-reduced, not byte-identical)**; it is never reworded. *(This
sentence itself carried the falsified byte-exact claim until 2026-08-12 — §6 F13.)*

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
`path:NN` strings from the banked audit; a fence keeps them **byte-identical to the bank** (which is
not the same as byte-identical to HEAD — see F11), keeps `verify-md-links` off
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

**The false positives, by adjudicated class.** ⚑ **Two denominators live here and the first cut
labelled them with one number — corrected 2026-08-12 at review.** The **anchor census** (this §2.1
scan, run on the 185 *anchor* lines before any edit) returned **62 flags → 7 genuine + 55 FP**. The
**forward guard** (run on the 177 *stamped* lines after the first commit) returned **58 flags → 2
genuine + 56 FP**; its set is not the anchor census's, because routed and STUCK rows carry no stamp
while three stamped lines self-match on this batch's own EOF note. **The table below is the
GUARD-scoped set and sums to 56**, which is why it reconciles with the 56 keys in
`GUARD_ADJUDICATED_FP`; the anchor-census FP count is **55**. Both numbers are correct for their own
surface, and neither is a subset of the other.

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
- **Rider/scope tags, counted from the landed notes: 146 ⚑ BIAS-DEBT · 24 ⚑ PAST-WALL · 2 ⚑ R49.**
  ⚑ *Was 147 BIAS-DEBT until 2026-08-12: the generator had emitted one on the UNACTIONED STUCK row
  `vol4/claim-quality.md:252`, which is now stripped (§6 F12). The tag never applied to a demoted
  row that lost it — 146 is the count over rows this batch actually demoted, and it always was.*

---

## 4. Per-class disposition

| Class | Rows | Disposition | Where |
|---|---|---|---|
| NEEDS — stamped | **176** | same-line status stamp + dated EOF note carrying the four-clause header, the R48 discipline, the rider and, per row, the verbatim quote + verbatim banked rationale + the resolution pointer | 109 files across `manuscript/ave-kb/`, `manuscript/vol_*`, `manuscript/{backmatter,frontmatter,common_equations}`, `src/ave/` |
| NEEDS — R39 byte-fenced | **7** | **no in-body stamp**; note routed to the governing file's EOF ledger with a pointer and the declaration quoted | §2.1 table |
| NEEDS — STUCK-POINT | **2** | **unactioned and unstamped**; full STUCK-POINT report at §5 | `appendices-overview.md:95`, `vol4/claim-quality.md:252` |
| — of the 176, PAST-WALL-scoped | 24 | the demotion is **scoped**: clause G resolves the cold, sub-yield side; the saturated-interior phase is one `eq_axiom_5.tex` explicitly does **not** write (*"the $D(A)\to\infty$ wall behaviour is past-wall-adjacent and \textbf{not written here}"*, with the de-bonded and pre-freeze phase forms named-open at (c3)/(c4)). Neither discharged nor adjudicated | in-note tag |
| — of the 183 actioned rows, BIAS-DEBT-ridden | 146 | resolution = the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** | in-note tag |
| — of the 185, R49 4π-convention | 2 | `saturating-modulus-and-backreaction.md:59`, `vol4/claim-quality.md:369` — the elliptic bias law carries the declared 4π source convention; R31-style dated-correction class | in-note tag |

---

## 5. STUCK-POINTs — 2 rows, unactioned, routed to Grant

Both rows are left **unstamped**. Their reports were **rewritten 2026-08-12 at review** — the first
cut of this section was **authored by hand** rather than generated from the banked row, and it broke
in two different ways, one of them severely. Both corrections are stated in the open below.

> 🔴 **CORRECTION OF RECORD (2026-08-12, at review) — STUCK-1's quote was FABRICATED, and it was
> routed to Grant in that state.** The first cut printed, under the retired strong label
> ***"Quote (byte-exact-at-HEAD)"*** — rendered hyphenated here **on purpose**, so that a corpus
> grep for the live label form returns a hard **zero** and this rider cannot be mistaken for one
> more site carrying it (F11) — the string `thrust metric via acoustic steepening: ∂_t ρ + ∇·(ρ v) = 0 with c_eff =
> c_0√(1 + ρ̄/(1−ρ̄²))`. **That string is at no line of any corpus file.** Re-derived at HEAD: it
> occurs exactly once corpus-wide, in *this record*, i.e. only where I wrote it. It is neither the
> banked quote nor the text at `appendices-overview.md:95`.
>
> **How it happened, stated so the mechanism is fixable and not just apologised for.** The 185 rows'
> in-corpus notes take their quote from the banked `quote` field **programmatically** and are byte-
> exact by construction (§9's machine check: 185/185). The two STUCK-POINT reports were the only
> row-level prose I typed by hand, and for STUCK-1 I typed a *reconstruction* of the physics — a
> continuity equation plus a wave-speed law that "looked like" the row — and then labelled the
> reconstruction byte-exact. **The label was the defect, not the physics intuition:** paraphrase is
> legitimate when it is called paraphrase. A fabricated string under a byte-exact label routed to
> Grant would have had him adjudicating text that does not exist.
>
> **The rule this batch now states for itself and hands to 2b:** *no quote is authored by hand.*
> Every quote in a report is pulled from the banked `quote` field or read out of the file, and is
> machine-verified against HEAD before the report is written — the same standard the generated notes
> already met. §7 carries the verification receipt.

Both rows remain **genuinely stuck on the merits** — but for STUCK-2 the ambiguity is now *narrower*
than the first cut claimed, because the corpus already answers half of it (below).

### STUCK-1 — `manuscript/ave-kb/common/appendices-overview.md:95`

- **Row (banked):** family `dark-wake-reaction-mass`, `uncertain: true`, `site_verdict: VERIFIED`,
  re-verified at HEAD by both engines.
- **Quote — the BANKED field, machine-verified present at HEAD:**
  `Non-Linear FDTD Acoustic Steepening PDE: $c_{eff}^2(x, y, z) = c_0^2 \left(1 + \kappa \cdot \bar{\rho}(x, y, z) \right)$`
- **The line at HEAD, read out of the file (the banked quote is a substring of it modulo the leading
  bullet/bold markup):**
  `- **Non-Linear FDTD Acoustic Steepening PDE:** $c_{eff}^2(x, y, z) = c_0^2 \left(1 + \kappa \cdot \bar{\rho}(x, y, z) \right)$ (Derived structurally for topological thrust metrics)`
- **Banked rationale, verbatim:** *"Thrust-metric 'acoustic steepening' PDE: if c_eff is the T2/EM
  index modulated by density it survives as refraction; if it is the compression carrier it dies —
  sector declaration owed."*
- **What is ambiguous:** the row's own rationale makes the disposition conditional on **which sector
  `c_eff` names**. If `c_eff` is the T2/EM index, the row is not an A1 consumer at all and Axiom 5
  clause G is the wrong pointer; if it is the compression carrier, clause G is the pointer and the
  mechanism dies. **Re-checked against the corrected quote:** no landed artifact declares the sector
  for *this* form. `eq_axiom_5.tex`, the axiom register, the interlock register and R49 are all
  silent on it, and the leaf itself says only *"(Derived structurally for topological thrust
  metrics)"*. **The routing stands on the merits.**
- **★ THE SUBSTRATE WALK, added at review — my reading, not a ruling.** A nonlinear FDTD wave speed
  keyed on the **local density** $\bar\rho$ and exhibiting **acoustic steepening** is a **compression
  carrier by construction**: steepening is what a wave does when its own speed depends on the
  amplitude it is carrying, so the modulating field and the carried field are the *same* field —
  that is a density/dilatation wave, i.e. the A1 slot. An **EM-index** reading would not be written
  this way: it would carry a refractive index $n(\bar\rho)$ with $c_{EM} = c_0/n$, the modulating
  density would be a *separate* field the transverse wave merely propagates through, and it would
  **not steepen**. On that reading the row is an A1 consumer and clause G is the pointer. **Surfaced
  as a reading; Grant still rules** — the row stays unstamped until he does, because a plumber's
  reading of a formula's shape is not a sector declaration.
- **★ THE NEAR-MISS, and it is the tell that the fabrication was self-inflicted.** The formula the
  first cut invented — `c_0√(1 + ρ̄/(1−ρ̄²))` — **is** a real corpus object, just not this row's:
  `src/ave/core/cavitation_flow.py`:22 carries
  `c_bulk²(ρ̄) = c₀² (1 + ρ̄/(1 − ρ̄²))`, and that module's own header line `:2` reads
  `Cavitation-Core Bulk-Flow — the rarefaction-stiffness branch of the BULK sector`. So the object I
  drifted toward **has** an explicit sector declaration — *BULK* — and had I verified my own quote I
  would have found it. That does not resolve STUCK-1 (different object, different leaf, different
  form: $1 + \kappa\bar\rho$ vs $1 + \bar\rho/(1-\bar\rho^2)$), but it is corroborating context for
  the walk above, and it is exactly the check the fabricated label prevented me from running.
- **What is needed to proceed:** a sector declaration for `c_eff` in the FDTD thrust-metric PDE
  (T2/EM index vs A1 compression carrier), from Grant or from the owning propulsion lane.
- **Recommendation:** rule the sector; if A1, the row demotes under clause G with the BIAS-DEBT rider
  and can be stamped by 2b. If T2/EM, it is a **re-bin** (arguably not a NEEDS row at all), which is
  2b's call and not this batch's.

### STUCK-2 — `manuscript/ave-kb/vol4/claim-quality.md:252`

- **Row (banked):** family `dark-wake carrier`, `uncertain: true`, `site_verdict: VERIFIED`,
  re-verified at HEAD by both engines.
- **Quote — verified byte-present at `vol4/claim-quality.md`:252 (this one IS byte-identical; see the
  §7 quote receipt):** `Momentum conservation closed by the "Dark Wake" — equal-and-opposite
  longitudinal shear strain into the lattice, propagating at $c_0$`
- **Banked rationale, verbatim:** *"Uncertain carrier: if the wake is a compression/bulk radiated wave
  it is a bulk radiative port (dies); if it is Cosserat-shear-carried it is untouched. Wording is
  ambiguous ('longitudinal shear'); the dark-wake is separately banked WRONG-REGIME, but the
  momentum-closure mechanism as stated consumes a propagating longitudinal carrier — re-derivation
  owed."*
- **🔴 THE VOCABULARY HALF IS WITHDRAWN — the corpus already answers it, and this batch failed to
  look (corrected 2026-08-12 at review).** The first cut asked Grant to adjudicate *"longitudinal
  shear strain"* against the canonical sector vocabulary. **That adjudication exists, is Grant's, is
  canonical, and predates this batch by two months.** `manuscript/ave-kb/common/dark-back-reaction-taxonomy.md`:13,
  verbatim: `**Channel-subscript note (2026-06-10, Grant rename-queue adjudication R5 — paragraph above preserved unedited):** the "longitudinal-shear" signature here is the **SHEAR channel** (the Cosserat deviatoric $\tau_{zx}$, a shear stress with longitudinal propagation direction) — explicitly **NOT** the bulk-volumetric/dilatational **longitudinal-V** grade (the "3").`
  The same leaf's `:23` fixes the same object as the dark wake and gives it the same propagation
  statement this row makes — verbatim: `The **dark wake** is the **far-field radiated shear stress** $\tau^{\text{far}}_{zx}$ — the real-space longitudinal-shear trail behind a **moving** soliton. It propagates *outward* (backward) at substrate wave speed $c_0$`.
  Same phrase, same object, same propagate-at-$c_0$ claim. **Asking a question the corpus has already
  ruled is the failure mode `verify-before-cite` exists to prevent, and this batch committed it:**
  the phrase was treated as ambiguous *in the abstract* instead of being grepped against the
  registry that owns it.
- **What remains genuinely open, RE-POSED as a re-bin question.** With R5 applied, the carrier is the
  **SHEAR** channel, which the carve does **not** touch — so the row's demotion premise is in doubt.
  That makes the live question a **bin** question, not a vocabulary one: **(a)** does the separately
  banked **WRONG-REGIME** disposition already cover this register row, so that a NEEDS demotion would
  double-count it? and **(b)** is a **NEEDS → SURVIVES-AS-RESPONSE re-bin** the correct disposition,
  given R5 puts the carrier outside the carve?
- **Why it is still not actionable here:** **a re-bin is out of this batch's authority.** R40 batch
  2a executes the banked bins; it does not move them. Stamping the row would demote a claim whose
  carrier R5 says survives; re-binning it would be this lane deciding a bin. Both are refused.
- **Candidate readings considered:** (a) stamp under clause G — **rejected**, R5 puts the carrier in
  the shear channel; (b) re-bin to SURVIVES in place — **rejected**, out of authority; (c) leave
  unstamped, discharge the vocabulary half against R5, and route the re-bin — **taken**.
- **What is needed to proceed:** a ruling on (a) and (b) above.
- **Recommendation:** **batch 2b should re-bin this row NEEDS → SURVIVES-AS-RESPONSE** unless the
  WRONG-REGIME banking is judged to already dispose of it, in which case it needs no separate action
  at all. Either way the vocabulary question is closed by R5 and should not be re-asked.

---

## 6. Findings surfaced, not fixed

**F1 — the forward guard's `GUARD_ADJUDICATED_FP` registry does not scale, and the batch registered
into it anyway.** The registry keys on the full stripped line bytes. This batch's flagged lines have
a **median length of ~718 characters** (longest **12 910**) — that distribution is measured over the
**58 flagged lines**, not over the 56 registry keys — so 56 keys is ~65 kB of literal blob in a
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

**F6 — the derived `.index/` movement was UNDERSTATED, and one movement was CONTENT LOSS, not stamp
text. Corrected 2026-08-12 at review, and the loss is repaired.** The first cut reported *"exactly 3
records, and the movement is the stamp text"*. **Measured: 5 records across 3 files**, and the fifth
was not stamp text at all.

| file | records | what moved |
|---|---|---|
| `claims.jsonl` | 3 | `def-l0ngdu`, `def-ncsatw` (`adjudicated_meaning`) and `clm-m3z5ux` (`rationale`) each gained the stamp string, because the stamped line feeds that derived field — the batch-1 F4 class, additive and benign |
| `strengthen-by.jsonl` | 1 | the to-do `text` for the `common/claim-quality.md`:561 bullet gained the stamp string — additive, same class |
| `depends-on.jsonl` | **1** | 🔴 **CONTENT LOSS:** the `clm-m3z5ux → clm-crbl60` edge's **`context` field became `null`** |

**The lost content is precisely the disambiguation this arc turns on** — 206 characters reading
*"…for the √2 c = √(K/ρ) bulk-modulus (dilatational) compression speed; per 2026-06-08 c_L
reconciliation this √2 c is the bulk-modulus speed, NOT the longitudinal P-wave √(10/3) c…"*. A
demotion sweep about the bulk sector deleted the √2c-vs-√(10/3)c carve from the machine index. It
never showed up as a gate failure: `verify-kb-metadata` checks the index is *freshly regenerated*,
and a faithfully-regenerated index of a broken parse is still fresh.

**Root cause, located and generic.** `manuscript/ave-kb/vol1/claim-quality.md`:445 is a depends-on
annotation of the shape `- clm-… — <title> [<context>]`, and the extractor anchors the context to
**end of line**: `_DEPENDS_ON_BRACKET_RE = re.compile(r"\[([^\[\]]*)\]\s*$")`
(`manuscript/ave-kb/tools/kb_index_lib.py`:195). Appending the stamp after the closing `]` moves the
bracket off the line end and the parse silently yields `None`. Putting the stamp *inside* the bracket
is also wrong — the stamp itself contains `[` and `]`, and the pattern's `[^\[\]]*` forbids nesting.

**Repair applied:** the stamp is moved to sit **before** the trailing `[context]` group, so the line
still ends with `]`. **Receipt, re-taken after `make refresh-kb-metadata`:** `depends-on.jsonl` is now
**byte-identical to `origin/main` — 0 differing records**, and the `clm-m3z5ux → clm-crbl60`
`context` is restored **byte-identical** (206 chars, compared field-by-field, not eyeballed). The
`.index/` delta is now **4 records across 2 files**, all additive stamp text.

**Scope check — how many other lines could carry this defect: exactly ONE, and it is this one.** A
Python scan over all 175 stamped lines' *original* text finds **1** line matching the depends-on
annotation shape ending in `[...]`, and **1** line ending with `]` at all — the same line. So the
defect was fully contained, but only by luck of distribution. **This annotation shape is now in the
batch-2b protocol (§8): 2b will meet it again, and its stamp must go before the bracket.**

`make refresh-kb-metadata` still reports *"Rewrote solidity in 0 claim-quality.md file(s) (0 solidity
line(s), 0 depends-on annotation(s) changed)"* and *"Rewrote leaf-references footer in 0
claim-quality.md file(s)"*. **No solidity number moved anywhere in this batch**, no `status:` field of
any `def-` node moved, and the derived files are committed **regenerated**, never hand-edited.

> **⚑ ONE ITEM DID NOT REPRODUCE AS REVIEWED.** The review reported the `strengthen-by.jsonl` `text`
> as gaining a **TRUNCATED** stamp fragment (`… 🔴 **[DEMOTED 2026-08-11 — R40`). Measured at HEAD,
> that field is **224 characters and carries the stamp in full**, terminating in `file]**`. There is
> no truncation in the artifact; the ellipsis appears to be display-side. The **count** correction
> (3 → 5 records, 2 → 3 files) stands and is applied above; the truncation characterisation does not.

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

**F13 — 🔴 THE SAME FALSIFIED CLAIM SAT IN THE PREAMBLE, ONE LEVEL ABOVE THE ROW LABELS F11 JUST
FIXED. Re-worded 2026-08-12; the CLASS is now gated.** Every one of the 109 per-file notes OPENED
with *"Corpus text quoted below is byte-exact and is never reworded"* — five to eleven lines above the
row label F11 had just corrected. The branch introduced it: **0 files on `origin/main`, 109 at the
pre-fix tip.** F11's own scope line — *"all 185 ROWS"* — is true, and does not reach the preamble.

**This is the third instance of one defect at three levels**, and the pattern is the finding:
(1) one hand-typed quote in this record labelled byte-exact and in fact fabricated → fixed at the
instance; (2) all 185 generated row labels → fixed at the row level; (3) all 109 preambles → found by
a third reviewer. **Each fix was scoped to the instance that had been found, not to the class.**

**⚑ THE UNDER-COUNT THAT HID IT, recorded as a live method finding.** The preamble ships in **two
carriers**: 62 markdown-form (one line) and 47 comment-form, where the generator's wrapper splits the
sentence across lines with the `%`/`#` marker repeated (`… byte-exact and is` / `% never reworded.`).
**A whitespace-flattening grep that is blind to the comment marker returns 62 and reads clean** —
reproduced here, and hit independently by the verifying lane. 62 + 47 = 109. **2b generates
comment-form notes and will meet this again:** any completeness count over R40 notes must normalise
the comment marker *before* matching, or it silently under-reports by ~43%.

**Fix applied:** all **109** preambles (62 md + 47 comment-form) re-worded to match the row label —
*"reproduced from the banked audit and is content-verified at HEAD (markup-reduced, not
byte-identical); it is never reworded"*. Safe under either outcome of the routed convention question,
same reasoning as F11. Two-method zero-residual receipt in §7.

**Fix made permanent — the CLASS is now gated, which matters more than the wording:**
[`../research/drivers/r40_quote_claim_strength_number_check.py`](../research/drivers/r40_quote_claim_strength_number_check.py)
asserts, per note, that **no STRONG (byte-identity) claim appears in the preamble OR in any row
label**, and that **the preamble and the row labels agree in strength** — a note whose preamble says
byte-exact while its rows say content-verified FAILS. It covers **both carriers** by normalising the
comment marker before matching, and it pins the marker-blindness under-count as a live regression
probe. Can-it-fire on synthetic drift in *each* carrier; negative controls in *each* carrier; a
non-empty-scan assertion; a declared self-exclusion (checker modules carry both shapes as fixtures —
measured safe: 0 of the 109 notes live under `research/drivers/`); and a 4-probe mutation receipt.
The convention hook is deliberate: under a future ruling that regenerates quotes byte-exact,
`ALLOW_STRONG` flips in **one** place and the strength-agreement assertion still fires.

> ⚑ **A mutation probe in that new module was itself a false receipt for one run, and it is recorded
> rather than quietly repaired.** M1's first cut rebound a back-compat *alias* rather than the
> function `flatten()` actually calls, so it perturbed nothing while reporting a pass. **A mutation
> probe that cannot reach the code path it claims to disable is exactly the false receipt this module
> exists to prevent.** Re-pointed at the live path; the dead alias is removed.

**F12 — 🔴 THE GENERATOR REFILLED THE SLOT IT WAS SUPPOSED TO LEAVE EMPTY. Stripped 2026-08-12 at
review; the rule is now enforced in code.** Both STUCK rows' landed EOF notes carried the generator's
boilerplate `**Resolution.**` paragraph — *"The demoted carrier is the propagating A1 / bulk branch;
under Axiom 5 clause G that slot is the **bound response** …"* — i.e. **the corpus asserted the very
pointer §5 says the batch refuses to assert**, on the very rows routed to Grant *because* the pointer
is unsettled. `vol4/claim-quality.md:252` additionally carried a **⚑ BIAS-DEBT** tag, so the corpus
asserted an A1/bulk demotion resolution for a row whose carrier Grant's **R5** had already placed in
the **SHEAR** channel (§5 STUCK-2).

**This is substitution-not-retraction at row level:** a slot that should have been left empty was
refilled with boilerplate. The record said one thing and the corpus said another, and **the corpus is
what a reader meets** — the §5 report was never the artifact at risk.

**Root cause:** the note generator branched on disposition for the *header* line (`STAMP` /
`LEDGER` / `STUCK`) but emitted the resolution paragraph and the rider/scope tags **unconditionally**.
The STUCK branch never had a suppression path.

**Fix applied:** both entries stripped to header + quote + banked rationale + an explicit
*"Routed to Grant — no resolution is asserted here"* paragraph that states, in the corpus, that the
entry names no pointer, carries no rider and carries no tag, and points at §5 for the full report.
The `⚑ BIAS-DEBT` tag is removed from `:252` (rider count 147 → **146**, §3).

**Fix made permanent:** the rule is now a gate —
[`../research/drivers/r40_stuck_row_note_guard_number_check.py`](../research/drivers/r40_stuck_row_note_guard_number_check.py),
auto-discovered by `make verify`'s lane-checks sweep. It discriminates rather than greps: a stamped
or fence-routed row **may** assert its pointer (that is the job), a STUCK row **may not**. Proven on
a synthetic STUCK row carrying the boilerplate (fires), a synthetic **stamped** row carrying the same
boilerplate (silent — the control that stops this becoming a blanket ban), a cleaned STUCK row
(silent), plus a non-empty-scan assertion and a 4-probe mutation receipt.

**F11 — 🔴 THE QUOTE LABEL ON ALL 185 ROWS OVERCLAIMED, AND IT IS THE SAME DEFECT AS §5's, ONE LEVEL
DOWN. Re-labelled 2026-08-12 at review.** Every generated row entry printed its quote under
*"Quoted claim, byte-exact-at-HEAD"* (markdown) / *"QUOTE (byte-exact-at-HEAD)"* (comment forms) —
**186 occurrences across 110 files at the tip, 0 on `origin/main`.** Measured against the
**pre-stamp** cited line: of the 185 banked quotes, **95 are byte-exact substrings** of that line and
**90 are not byte-present at it** (1 present elsewhere in the file, 9 spanning adjacent lines, 13
markup-stripped, 14 markup+wrap, 9 ellipsis-elided, 44 other). Two concrete instances:
`appendices-overview.md:94` printed `Weak Mixing Angle (Acoustic Mode Ratio):` where the file carries
`**Weak Mixing Angle (Acoustic Mode Ratio):**`; `engine-capability-map.md:31` printed
`must carry and couple them` where the file carries `must carry *and couple* them`.

**Root cause, and it is mine, not the audit's.** §9's two verification engines are **reduction**
engines by their own description — *"reduced to `[a-z0-9]` only"*, *"reduced to alphanumeric word
tokens"*. They establish **content presence at the anchor**, which is a real and useful result and is
what §9 claims. They do **not** establish byte-identity, and I attached a byte-identity label to
their output. The fix-pass then certified the generated quotes *"byte-exact by construction"* — true,
but **byte-exact to the BANK**, while the label said **HEAD**. Those are different artifacts, and the
bank's quotes carry the audit's own markup-stripping and unmarked elisions.

**This is §5's fabricated-quote defect one level down**, and this record's own diagnosis of that
applies verbatim: *"THE LABEL WAS THE DEFECT, not the intuition"* / *"paraphrase is legitimate when
it is called paraphrase."* It is also a **regression against merged precedent**: batch 1's landed
note on `origin/main` at `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex`:258
uses the neutral `:11  QUOTE:` form and claims no exactness at all.

**Fix applied — the weak-but-true label (path (a)).** All 185 rows now read **"Quoted claim (content
verified at HEAD; markup-reduced from the banked audit)"** / **"QUOTE (content verified at HEAD;
markup-reduced from the banked audit)"**. That is exactly what the engines verified. **No quote text
changed**, no line count changed, and the 90 non-byte-exact quotes are neither hidden nor regenerated.

**The alternative was NOT taken, and why.** Path (b) — regenerate the 89–90 from file bytes and keep
the strong label — would have produced a *stronger* artifact, but it is a **convention** question
(which standard every future R40 batch prints under), that question is **routed to Grant** and is
being consolidated with an identical one riding #946, and this lane does not get to set a corpus-wide
convention inside a demotion sweep. **The weak-but-true label is correct under either ruling**; the
strong label is correct under only one, and was not correct here.

**F10 — `verify-new-cite-excerpts` re-classified 14 PRE-EXISTING cites as "added" because the R40
stamp modified their lines, and the fix costs 8 lines their pure stamp-only status.** The gate diffs
`base...HEAD` and treats every cite on a modified line as newly authored. Fourteen such cites, on
eight lines, are cites this batch did not write. Batch 1 met the same thing once
(`gw-propagation-lossless.md:48`) and resolved it by appending a verbatim excerpt after the stamp;
this batch follows that precedent at eight lines, with the excerpts taken **byte-exact from the cited
lines** and a same-line note saying why they are there. **The cost is stated, not hidden:** those
eight lines are no longer stamp-only (§7 METHOD 2 counts them in their own row), though each original
text survives as a strict prefix / cell-for-cell.
**One cite could not be given an honest excerpt and is surfaced instead of faked:**
`dual-reactance-storage-taxonomy.md:51 → ../vol1/claim-quality.md:1391` points at a **blank line**
(the pre-existing `blank line cite` advisory class). No excerpt of a blank line exists, so none was
invented; the gate is satisfied by the other, real excerpt on that line, and the dead cite is left
for whoever owns that leaf. Repairing a pre-existing blank-target cite is not a status-only batch's
work.

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
  **109 EOF-append hunks**, and **0 SHIFTING hunks**.

  > ⚑ **THE NORMALIZATION RULE, stated (it was used but unstated in the first cut, 2026-08-12).** A
  > *naive* classifier — *append iff the hunk starts strictly past the old EOF* — returns
  > **171 / 107 / 2** on this same diff, not 171 / 109 / 0. The two are not a disagreement about the
  > corpus; they are two labellings of the same hunks. Under `--unified=0`, a stamp on a file's
  > **last original line** and the EOF note appended right after it collapse into **one** hunk, which
  > therefore consumes an original line (`old-count > 0`) while still being an append. This batch
  > classifies a hunk as an EOF-append when it **reaches** the old EOF (`old_start + old_count − 1 ≥
  > old_EOF`), not when it starts past it. **Measured: 107 pure appends (`old-count = 0`) + 2 merged
  > appends = 109**, and the 2 are named — `saturating-modulus-and-backreaction.md` (`@@ -194,1`, old
  > EOF 194) and `05_electroweak_gauge_theory.tex` (`@@ -185,1`, old EOF 185). Both are files whose
  > final original line happens to be a stamped row. **The append-only property is independently
  > confirmed by METHOD 2** (every modified original line is stamp-only or stamp+excerpt; zero
  > original lines lost), so the claim does not rest on this labelling — but the labelling had to be
  > said out loud, because a reader re-running the naive rule gets a different pair of numbers and
  > has no way to tell which of us is wrong.

  Scope, stated so it cannot be over-read: the
  receipt covers the 109 corpus files and **excludes** the derived
  `manuscript/ave-kb/.index/`, `_orchestration/`, and `research/drivers/`. Those carry no `path:NN`
  line anchors into themselves from the corpus (`r40_preserved_span_number_check.py` has **0** inbound
  line-cites, measured), so the exclusion is a stated scope, not a silent one.
- **METHOD 2 — independent line-by-line comparison against `git show origin/main:<file>`** (engine:
  Python, no git plumbing beyond the blob read): **50 680 original lines checked**, **175 modified
  original lines**, **0 violations**, **0 truncations**, split honestly:
  - **167** are **stamp-only** — byte-identical to the original once the inserted stamp string is
    removed;
  - **8** additionally carry the **gate-required verbatim cite excerpts** appended after the stamp
    (§6 F10). Each original line's text remains a strict **prefix** (or, for the two markdown table
    rows, is preserved cell-for-cell with the addition inside the final cell), so every incoming cite
    still resolves to a **superset** of its original content.

⇒ **Every one of the 6221 incoming `path:NN` cites into these files still resolves to its original
content.** The 175 modified lines reconcile with the identity's 176 stamped rows on 175 distinct
lines (§3).

**★ QUOTE-VERIFICATION RECEIPT (added 2026-08-12 at review — the check whose absence let §5's
fabrication through).** Every quote in this record's hand-authored sections is now machine-checked
against the artifact it cites, not read back by eye:

| quote | check | result |
|---|---|---|
| STUCK-1's quote | is the **banked `quote` field** of the row, and is present at `appendices-overview.md:95` modulo the leading bullet/bold markup | **PASS** |
| STUCK-1's HEAD line | reproduced byte-exact from the file | **PASS** |
| STUCK-2's quote | byte-present at `vol4/claim-quality.md:252`; the banked `quote` is a substring of it | **PASS** |
| R5 `dark-back-reaction-taxonomy.md:13` | excerpt byte-present at the cited line | **PASS** |
| R5 `dark-back-reaction-taxonomy.md:23` | excerpt byte-present at the cited line | **PASS** |
| `cavitation_flow.py:2` and `:22` | excerpts byte-present at the cited lines | **PASS** |
| `kb_index_lib.py:195` | the `_DEPENDS_ON_BRACKET_RE` line byte-present at the cited line | **PASS** |
| the fabricated string | occurs **exactly once** in the record, **inside the correction rider**, and nowhere under a live byte-exact label | **PASS** |

The 185 in-corpus notes were already machine-verified on this axis by construction (§9) — this
receipt closes the gap that the two hand-typed reports fell into.

**★ PREAMBLE RE-WORD RECEIPT (F13), both carriers counted separately, two methods.** Engine 1 =
Python `os.walk` over raw bytes with the comment marker normalised before matching; engine 2 = shell
`grep -rIo`, marker-agnostic. They agree.

| measure | markdown-form | comment-form | total |
|---|---|---|---|
| preambles at the pre-fix tip | 62 | 47 | **109** |
| preambles on `origin/main` | 0 | 0 | **0** (the branch introduced it) |
| **re-worded this pass** | **62** | **47** | **109** |
| residual `Corpus text quoted below is byte-exact…` | 0 | 0 | **0** |
| new content-verified preamble | 62 | 47 | **109** |

**Zero-residual, two methods:** engine 1 returns **0** for the markdown form, **0** for the
marker-aware wrapped comment form, and **0** for the marker-agnostic substring
`quoted below is byte-exact`; engine 2 (`grep -rIo 'quoted below is byte-exact'`) returns **0**.
**The naive comment-marker-blind flattening grep returns 62** — reproduced deliberately, because that
is the number that reads clean while 47 violations stand (F13).

**Surviving `byte-exact` strings are enumerated, not swept.** They fall in three classes, all true or
all self-describing: (a) the 8 stamp-modified corpus lines' *"cite excerpts, byte-exact at the cited
lines"* — verified true when built, §6 F10; (b) this record's F11/F13 prose, which must NAME the
retired claim to correct it; (c) pre-existing corpus text this batch never touched (research docs,
earlier docket entries, batch 1's own notes). **Two claims in THIS record were in neither class and
were corrected with the 109:** §1.2's *"Corpus text quoted in the notes is byte-exact and is never
reworded"* — the same falsified sentence, one level up again — and §2's *"a fence keeps them
byte-exact"*, now *"byte-identical to the bank (which is not the same as byte-identical to HEAD)"*.

**Gates, on the landed commits:**

| Gate | Result |
|---|---|
| `make verify` | **PASS**, exit 0 |
| `research/drivers/r40_preserved_span_number_check.py` | **PASS** — pinned batch-1 scan 60/24/0 unchanged; live forward guard **175 added stamped lines scanned, 0 flagged**; regression fires on the known breach; both spec extensions live |
| `research/drivers/r40_quote_claim_strength_number_check.py` | **PASS** — 109 note-bearing files scanned, preamble seen in **62 markdown + 47 comment-form = 109 of 109**, **0 over-claims and 0 preamble/row disagreements**; can-it-fire in BOTH carriers; negative control in BOTH carriers; marker-blindness regression pinned; mutation receipt 4/4 |
| `research/drivers/r40_stuck_row_note_guard_number_check.py` | **PASS** — 2 STUCK row entries scanned, **0 assert a resolution or carry a tag**; can-it-fire fires on the synthetic bad row; negative control clean; mutation receipt 4/4 |
| …`--mutation-receipt` | **PASS** — 9/9 probes hold, including **M6d** (the FP registry is narrow: right key suppresses, wrong file or wrong bytes do not) |
| `make verify-new-cite-excerpts CITE_BASE=origin/main` | **PASS**, run against the LANDED commits (§6 F2) |
| `make test` | **PASS** |
| `python -m compileall` / `py_compile` on the 24 edited engine modules | clean |

**Vocabulary compliance, two methods — and the receipt is stated in the form the measurement actually
supports.** Surface: the WHOLLY-NEW lines this batch authored (the 109 EOF notes + this record; a
modified pre-existing line is excluded, because its retired-word content is the corpus's, not this
batch's), with fenced verbatim quotes and inline backtick spans stripped. Python `re.findall` and
shell `grep -o -E` over the same bytes agree exactly: *dress* **112**, *retardation* **112**, *halo*
**111**, *grade* (exact word) **113**.

> ⚑ **These figures were 111 / 112 / 111 / 112 in the first cut and are corrected to 112 / 112 /
> 111 / 113 (2026-08-12, at review).** The two deltas trace to **one string** — §7's own correction
> rider, which quotes the pre-existing corpus phrase *"the graded Coulomb dress"* in *italics*
> rather than backticks, so the stated stripping rule leaves it in-surface. **The receipt is
> self-referential on this axis:** every word this receipt writes about the retired vocabulary moves
> the count it reports, and the first cut measured before its own rider existed. The rider that says
> *"a receipt that has to be re-scoped to survive is a finding about the receipt"* was itself off by
> one on exactly that axis, which is the tidiest possible demonstration of the point. **The
> load-bearing invariant does not move and is re-confirmed: authored USES = 0.** The count of
> mentions is bookkeeping about this document; the zero is the claim about the corpus.

**Every one of those is a MENTION, not a USE.** Hand-classified: all but one sit inside the
*retirement paragraph itself* — the sentence in each note that names the retired words in order to
retire them, replicated across the 109 notes in its three carriers (markdown, `%` comment, `#`
comment). The single remainder,
`src/ave/core/s2_hcouple_gate.py`:797, sits inside a **verbatim banked rationale** quoted in that
file's note (*"genuine field-resolved spatial transport within a grade"*), which is corpus text and
is never reworded. **Authored uses of the retired nouns: 0.**

> ⚑ **A first cut of this receipt claimed a bare "0" and was wrong as written.** The words are
> present 111–112 times; the true claim is *zero authored USES*, not zero occurrences. The first
> measurement also mis-scoped the surface — it counted whole modified corpus lines as "authored",
> which attributed pre-existing text like *"the graded Coulomb dress"* to this batch. Both errors are
> corrected above rather than quietly re-run: **a receipt that has to be re-scoped to survive is a
> finding about the receipt.**

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
### ★ PROTOCOL ADDITIONS BATCH 2b MUST CARRY (learned the hard way here)

1. **Stamp placement vs the depends-on annotation shape.** A claim-quality line of the form
   `- <id> — <title> [<context>]` has its context anchored to **end of line**
   (`kb_index_lib.py`:195, verbatim: `_DEPENDS_ON_BRACKET_RE = re.compile(r"\[([^\[\]]*)\]\s*$")`).
   A stamp appended **after** the `]` silently nulls the `context` field in `depends-on.jsonl`, and
   no gate catches it (F6). A stamp **inside** the bracket is also wrong — the stamp contains `[`
   and `]` and the pattern forbids nesting. **The stamp goes BEFORE the trailing bracket.** 2a met
   this shape once in 175 lines; 2b's 105 SURVIVES rows land in the same registers and will meet it
   again.
2. **A STUCK row emits NO resolution clause, ever — and the rule is now CODE, not prose.**
   2a's generator emitted its boilerplate `**Resolution.**` paragraph for every row regardless of
   disposition, so both STUCK rows landed asserting the very pointer the batch refused to assert, and
   one carried a `BIAS-DEBT` rider over a carrier a prior Grant ruling had already placed in a
   different sector (§6 F12). Prose review caught it; no gate could, because no gate knew the rule.
   It does now: [`../research/drivers/r40_stuck_row_note_guard_number_check.py`](../research/drivers/r40_stuck_row_note_guard_number_check.py)
   is auto-discovered by `make verify`'s lane-checks sweep and enforces that a row entry marked
   `NOT STAMPED — STUCK-POINT` carries no resolution clause and no rider/scope tag, while a **stamped**
   or **fence-routed** row may carry both (a demoted row naming its pointer is the whole job). It
   ships a **can-it-fire** fixture (a synthetic STUCK row carrying the boilerplate — must flag), a
   **negative control** (the same boilerplate on a stamped row — must not flag), a cleaned-STUCK
   fixture, a **non-empty-scan assertion**, and a 4-probe mutation receipt including row-boundary
   integrity (a later row's resolution must not be charged to the stuck row).
3. **No quote is authored by hand.** Every quote in every report — including STUCK-POINT reports and
   any hand-written prose — is pulled from the banked `quote` field or read out of the file, and is
   **machine-verified against HEAD** before the report is written. 2a's generated notes met this by
   construction (185/185); its two hand-typed reports did not, and one of them fabricated a quote
   under a byte-exact label (§5).
4. **Grep the registry that owns a term before routing a vocabulary question to Grant.** 2a routed
   *"longitudinal shear strain"* for adjudication when Grant had already ruled it
   (`dark-back-reaction-taxonomy.md`:13, R5). A phrase that "reads ambiguous" is a prompt to search,
   not a prompt to escalate.
5. **After any `.index/`-touching pass, diff the derived index FIELD-BY-FIELD against the base**, not
   by record count. F6's content loss was a field going `null` inside an otherwise-present record;
   `verify-kb-metadata` passes on a faithfully-regenerated index of a broken parse.

### ★ QUEUE ITEMS FOR BATCH 2b (recorded at the 2026-08-12 delta verify; NOT fixed here)

1. **★ THE NEW STUCK-ROW GUARD HAS A COMMENT-FORM BLIND SPOT — must be closed BEFORE 2b runs.**
   `r40_stuck_row_note_guard_number_check.py`'s `violations_in()` searches the STUCK marker only in
   the row **HEADER**. Markdown notes carry the disposition in the header, but **comment-form
   (`.tex`/`.py`) notes carry it in the row BODY** (`STAMPED AT: NOWHERE -- STUCK-POINT …`; cf.
   `08_gravitational_waves.tex:501`). **Both of 2a's STUCK rows are markdown, so this PR is
   unaffected** — but **2b generates comment-form notes**, so this must close before 2b starts.

   > ⚑ **RE-PROBED HERE, AND THE BLIND SPOT IS WIDER THAN REPORTED — record the wider one.** The
   > delta verify reported it as header-vs-body: *"move the same wording to the header = 1"*.
   > Measured, that variant still returns **0**, because the defect is upstream of position — it is
   > **VOCABULARY**. `STUCK_MARK` is `NOT STAMPED\s*[—-]{1,2}\s*STUCK-POINT`, which matches the
   > **markdown** generator's wording (*"NOT STAMPED — STUCK-POINT, routed to Grant"*, `True`) and
   > **does not match the comment generator's wording at all** (*"STAMPED AT: NOWHERE -- STUCK-POINT
   > routed to Grant"*, `False`) — in the header **or** the body. So the 2b fix is **two** changes,
   > not one: extend the marker vocabulary to the `STAMPED AT: NOWHERE -- STUCK-POINT` form **and**
   > search header + body. Fixing only the position, as the report implies, would leave the guard
   > blind. *(Recorded, deliberately not fixed here per the delta-verify instruction: 2a's scope is
   > closed and a guard change wants its own fixture delta.)*
2. **★ THE DATE-PINNED `STAMP` IN `r40_preserved_span_number_check.py` IS A GATE-LANE ITEM, AND 2b
   DOES NOT START UNTIL IT LANDS.** It fails **OPEN and SILENTLY** — probed at 2026-08-12, 2026-09-01
   and 2027-01-05, every one scans **0** and flags **0**, i.e. a future-dated batch would get a clean
   report from a gate that never looked at it. **It is no longer a future risk: it already
   under-scans 19 live stamps today.** The measured-correct replacement pattern and the required
   minimum-scanned assertion are in the infra-PR list below.
3. **★ R52 HAS NOT PROPAGATED — queued for 2b.** R52 ruled that the *"ν-denominator 7 = a mode count"*
   derivation is **NOT LICENSED**, and five-plus sites still run it, unedited on `main`:
   `mode-counting-heat-capacity.md:14`, `g-star-derivation.md:18`, `alpha-s-derivation.md:21` and
   `:35`, `03_geometric_inevitability.tex:417` / `:475` / `:495`,
   `11_thermodynamics_and_entropy.tex:149`. Plus a cite drift at `03_pin_port_configuration.tex:45`
   (cites `trampoline-framework.md:200`; the sentence is at `:204`). **Out of 2a's scope** — 2a
   executes the banked NEEDS bin and adjudicates no other ruling — and recorded here so 2b inherits
   it with its sites named.

### ★ ROUTED TO A SEPARATE INFRA PR — REQUIRED BEFORE BATCH 2b

These three change **gate semantics** and are deliberately **not folded into this PR**; each needs
its own fixture delta and its own review. Recorded here so 2b cannot start without them.

1. **The date-pinned `STAMP` regex** (`research/drivers/r40_preserved_span_number_check.py`:119,
   verbatim: `STAMP = re.compile(r"DEMOTED 2026-08-11|TAG DEMOTED 2026-08-11")`). Any batch not
   dated `2026-08-11` is **invisible** to both the pinned scan and the live forward guard, which
   would then report a clean run over a batch it never examined.
   **⚑ MY PROPOSED FIX WAS MEASURED AND IS WRONG — do not use it.** F3 proposed
   `(?:TAG )?DEMOTED \d{4}-\d{2}-\d{2}`; measured, that makes the **pinned scan read 61/25** (not
   60/24) and **self-flags `04_continuum_electrodynamics.tex:288`** — the very site
   `SECTIONING_PROBE` pins as a live regression. **This is exactly what F3 said had to happen
   before the change lands** (*"whether it perturbs the pinned batch-1 fixture numbers must be
   measured before it lands, not assumed"*) — the discipline held, and the measurement killed my
   own suggestion. The pattern that measures clean is
   `(?:TAG )?DEMOTED \d{4}-\d{2}-\d{2}(?=[^\n]{0,12}(?:R4\d-B|per R4\d))`
   (pinned 60/24 ✓, live 175/0 ✓, future-dated breach 1/1 ✓). An R40-**only** lookahead must be
   avoided: it drops the 2 R42 stamps.
   **Also required in that PR:** a **minimum-scanned assertion**, so an empty forward scan can never
   read as clean (the F2 failure mode, made structural instead of documented).
2. **`untouched` / `unedited` added to the `PRESERVE` vocabulary** — a real declaration form the
   detector's vocabulary lacks. Live at `manuscript/vol_9_vacuum_datasheet/figures/moduli_relationship.tex`:25
   (adjudicated **not** a fence, but **invisible** to the gate, so the gate's silence there carries
   no information).
3. **The F1 registry re-key** — recommended `(file, stamp-token, sha1(stripped-line)[:12])`, with
   the human reading staying exactly where it is. **The hazard is already live, not hypothetical:**
   this batch's third commit re-wrapped 8 stamped lines *after* the second commit wrote the
   registry. None of the 8 happened to be registered — **luck, not design**. A re-key removes the
   coupling between a line's byte-length and the gate's memory.

- **★ NAMED OPEN DEBT — the guard registry's scaling defect is registered-into, not repaired** (F1;
  re-key routed above).
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
