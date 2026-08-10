# R40 demotion sweep — scope verification (the mandated first step)

### ENTRY 2026-08-10-r40-sweep-scope-verification

**Class:** sweep infrastructure. Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`, moves no solidity,
adjudicates no channel, and **demotes nothing** — it verifies the worklist the demotions will run
against.
**Authority:** R40, [`2026-08-10-rulings-r40-r42.md`](docket-entries/2026-08-10-rulings-r40-r42.md),
Grant verbatim *"1. go / 2. agreed / 3. agreed"*.

**Execution SHA `6c291196`**, worktree verified clean (`git status --porcelain` = 0) before any edit.
Machine-readable output: [`research/drivers/r40_sweep_worklist_verified.json`](../research/drivers/r40_sweep_worklist_verified.json).

---

## 1. The split, re-derived — reconciles exactly

R40 names the worklist as #935's consumer table. Re-derived from the JSON's own `rows` array at the
execution SHA, not read off a headline:

```
349 rows = 59 DIES-WITH-THE-PHANTOM + 185 NEEDS-RE-DERIVATION + 105 SURVIVES-AS-RESPONSE
```

Three independent statements of the same split agree: the recomputed `Counter` over `rows`; the
JSON's own `bin_counts` field; and the result doc's `:113` — *"Totals: 349 consumer rows — 59
DIES-WITH-THE-PHANTOM · 185 NEEDS-RE-DERIVATION · 105 SURVIVES-AS-RESPONSE · 0
BOUND-RESPONSE-INCONSISTENT candidates survived adjudication."* **No drift in the split.** Per the
R35 standing standard the 59/185/105 was treated as a hypothesis to reconcile against, and it
reconciled.

`uncertain_count` = 52 (rows flagged uncertain by the panel and re-read by the lane orchestrator);
that is a provenance field, not a fourth bin, and it does not enter the identity.

## 2. Site verification at HEAD — and the probe finding that dominates it

Every row cites `path:line`. Verify-before-cite requires each to still resolve at HEAD, because the
table was measured at #935's base.

> ⚑ **METHOD FINDING, and it is the load-bearing one for anyone reusing this table.** A
> naive quote-probe reports **115 of 349** sites as ABSENT. That number is **almost entirely
> false**. Three probe generations, same corpus, same SHA:
>
> | probe | ABSENT | what it got wrong |
> |---|---|---|
> | v1 — first 60 chars of the quote, verbatim | **115** | the audit's quotes carry **unmarked elisions**, so a fixed window walks across a gap that is not in the source |
> | v2 — elision-split + Greek-letter mapping | **32** | quotes are **rendered prose** (`Γ_shear`, `√2`, `ρ×speed`) against **LaTeX/markdown source** (`$\Gamma_{\mathrm{shear}}$`, `$\sqrt2$`) |
> | v3 — hard reduction (strips `$ \ { } _`, LaTeX command names, Greek, arrows) | **11** | residual formatting cases only |
> | v3 + hand-read of all 11 | **5** | — |
>
> **A single-probe site check on this table has roughly a 20× false-drift rate.** Anyone who runs
> one probe and reports the result will "discover" a corpus-wide drift event that did not happen.
> The reduction that works is the one blind to markup on **both** sides.

**Verdict after hand-reading every residual:**

| verdict | rows | meaning |
|---|---|---|
| VERIFIED | **338** | quote found at the cited line or within ±3 |
| VERIFIED-BY-HAND | **6** | probe artifact; content confirmed present at/adjacent to the cited line by reading |
| **DRIFTED-NEEDS-REPIN** | **5** | the cited line does **not** hold the quoted content |

`338 + 6 + 5 = 349` ✓. **Zero FILE-MISSING, zero LINE-BEYOND-EOF** — no cited file or line has
disappeared.

### The 5 drifted rows — flagged, not guessed

Per the brief: *"flag any drifted site rather than guessing"*. None of these is re-pinned here;
re-pinning is a measurement, and it belongs to the batch that writes the note.

| row | bin | cited line now holds | the quote is |
|---|---|---|---|
| `manuscript/vol_9_vacuum_datasheet/chapters/03a_device_circuit_models.tex`:148 | NEEDS-RE-DERIVATION | *"The two-port read at the electron (native-engine render)."* | the `Γ=-1`-boundary-confined A1 dilatation cavity-mode sentence — not on this line |
| `manuscript/ave-kb/vol9/ch1-general-description/index.md`:22 | SURVIVES-AS-RESPONSE | the Axiom-4 kernel `S(A)=√(1−A²)` bullet | the `V_snap` max-ratings clause |
| `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex`:43 | SURVIVES-AS-RESPONSE | the Schwarzschild-radius EM-transverse sentence | the *"total-confinement Γ = −1 reflector lives in the shear and bulk channels"* sentence — same passage, different line |
| `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex`:169 | SURVIVES-AS-RESPONSE | *"The Event Horizon is classically defined as a coordinate singularity…"* | the *"Γ=−1 total-reflection wall is a separate, deeper boundary"* sentence — same passage, different line |
| `manuscript/vol_9_vacuum_datasheet/chapters/05_ac_electrical_characteristics.tex`:121 | SURVIVES-AS-RESPONSE | the operating-point/bias sentence | the `Γ = −1` wall on the A1 longitudinal dilatation sentence |

Three of the five are **same-passage off-by-a-few** — the FLAG-C anchor-drift class, not content loss.
Only two rows in the DIES/NEEDS classes are affected at all (`03a_device_circuit_models.tex`:148),
so the drift does **not** gate the high-severity batches.

## 3. Beyond-floor rows already on the record

The enumeration is **PATTERN-BOUNDED, not exhaustive** — the supplement says so in its own words:
*"The enumeration is hereby re-labeled PATTERN-BOUNDED, not exhaustive: no completeness claim
survives; the demotion sweep should treat the union+supplement as a floor."*

The supplement already carries **5 counter-sweep rows outside the 349** (1 DIES, 4
NEEDS-RE-DERIVATION). All five verify at HEAD (4 OK-EXACT, 1 OK-WINDOW). **They are additive to the
349 and must not be folded into it** — the sweep's identity therefore opens at **349 + 5 = 354
known rows**, before any straggler find.

The supplement also disposes of a pattern defect worth carrying forward: `F3_partition`'s
alternative `Aki` matched case-insensitively **as a substring** (t-**aki**-ng / m-**aki**-ng /
bre-**aki**-ng), inflating F3 with ~71 prose false positives. Direction of effect is **noise only** —
it raised apparent hit counts and hid no consumer — so it does not reopen the floor downward.

## 4. What this artifact hands the sweep

- The verified worklist as machine-readable JSON, each row carrying `bin`, `site`, `quote`, `family`,
  and a `site_verdict` of `VERIFIED` / `VERIFIED-BY-HAND` / `DRIFTED-NEEDS-REPIN`.
- The identity to reconcile the notes against: **349 table rows + 5 supplement rows**, with the
  five drifted sites named so a note is never written against a stale anchor.
- The probe lesson, so the site check is not re-derived wrongly by the next lane.

**Nothing is demoted in this artifact.** The R40 header form, the per-class note bodies, the R42
CHORD-tag disposition and the straggler sweep are the sweep's work, not this step's.
