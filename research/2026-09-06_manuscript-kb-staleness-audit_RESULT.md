# RESULT — manuscript `.tex` vs KB staleness audit (2026-09-06)

**Branch:** `docs/2026-09-06-manuscript-kb-sync` · **Base:** `origin/main` @ `6b8b49a0`
**Class:** mechanical measurement. **Adjudicates nothing, edits no manuscript file.**
**Tool:** [`manuscript/ave-kb/tools/audit-tex-kb-staleness.py`](../manuscript/ave-kb/tools/audit-tex-kb-staleness.py) · raw scan: [`2026-09-06_tex-kb-staleness_scan.txt`](2026-09-06_tex-kb-staleness_scan.txt)

**Standing frame.** The KB is the truth source (standing G-ruling). A `.tex` is
STALE when it cites KB content that has since moved, been demoted, or been
rewritten. This audit measures that mechanically and hands over a candidate
list. **It does not decide whether any given site is wrong** — that needs
reading, and it is the next stage.

---

## §0 — HEADLINE

**Referential integrity is clean. The debt is entirely walk-back propagation lag.**

| Signal | Count | What it means |
|---|---|---|
| **S1** dead KB path in `.tex` | **0** | every `\kbleaf{}` path resolves |
| **S2** dead claim-id in `.tex` | **0** | every `clm-`/`def-`/`ilk-` id is in `claims.jsonl` |
| **S3a** build-band violation, **undisclosed** | **5** | printed prose leaning on a `do-not-build` claim with no banner nearby |
| S3c build-band cite, **disclosed** | 17 | banner or inline caveat present — honest |
| S3d build-band cite in a lookup-table row | 6 | provenance pointer, not an assertion |
| **S4a** time-lag, **material** | **190** | the cited leaf gained a walk-back / demotion / retraction **after** the `.tex` was last touched |
| S4b time-lag, cosmetic | 17 | leaf changed, but not in a way that reaches print |
| **S5** line-anchor drift | **49** | a `:NNN` anchor that is out of range, or whose leaf changed after the `.tex` |

`S3a + S3c + S3d = 28`, which matches an independent second-method recount of
`do-not-build` cites in non-comment `.tex` lines. **The `.tex` corpus scanned is
210 files** (212 minus 2 tool-test fixtures, which are deliberate negative cases).

> 🔴 **CORRECTED 2026-09-06 — the 190 is a CANDIDATE count with ~99% noise, not a
> defect count. An adjudication lane read all 79 vol9 S4a sites by hand and
> measured a TRUE-POSITIVE RATE OF 1.3%: one real propagation debt, 74 benign,
> three pre-existing dead anchors the signal did not and could not find.**
>
> **The cause is structural, and my earlier calibration in §4 answered the wrong
> question.** S4a asks *"did the cited leaf gain a grading marker anywhere since
> this `.tex` was touched"*. It has **no reach test** — nothing connects the marker
> to the sentence doing the citing. The large registry leaves legitimately carry
> dozens of demotions (`vocabulary-register.md` alone: **34** strong-marker added
> lines since 2026-08-01), so every one of the ~60 sites citing such a leaf trips
> the flag no matter what was demoted. §4 below weighed strong-vs-weak marker
> tokens and concluded "189 of 190 carry a strong marker" — **true, and
> irrelevant**: the markers are real, they just do not reach the citing assertion.
>
> **And the signal is blind to the class that actually matters.** Both true
> positives the lane found are **print asserting demoted content at a line carrying
> no cite at all** — invisible to any cite-keyed scan, including this one.
>
> **What the scan IS good for: a leaf index.** The 159 distinct sites factorize to
> **~22 distinct leaves**. Reading each leaf's demoted anchors once, then grepping
> print for those anchors, answers every site citing it at about a fifth of the
> cost of site-walking. That is the shape the remaining sweep should take.
>
> **What this correction does NOT touch, enumerated rather than summarized:** S1 = 0
> and S2 = 0 (referential integrity is clean, and those are exact checks, not
> heuristics); the five S3a build-band sites (claim-id lookups, not diff
> heuristics); S3c = 17 and S3d = 6, which reconcile with S3a to the independent
> 28-cite recount in §0; S4b = 17; and **S5 = 49 — untouched is not endorsed.**
> S5 was not re-measured by the vol9 lane at all, and §5 below already grades it
> *"mostly unverified-not-broken"*: only anchors past end-of-file are hard errors.
> **Method for this list:** read off the §0 signal table row by row, so every
> bucket printed there is accounted for above or is S4a itself.

## §1 — ~~THE ONE NUMBER THAT MATTERS: 190~~ → a candidate count, measured 1.3% true-positive

**189 of 190 material time-lag sites carry a STRONG marker** — the diff of the
cited leaf, since the citing `.tex` was last committed, ADDS at least one of
`RETRACTED / DEMOTED / WALK-BACK / SUPERSEDED / REFUTED / 🔴 / VACATED /
DEPRECATED / STRUCK`. Only one rests on weak tokens alone.

This is the same meta-finding the 2026-07-01 full-corpus audit reached by a
different route — *"the real, systematic debt is a MANUSCRIPT-OVERCLAIMS-vs-KB-
HONESTY LAG"* — now measured mechanically and **five weeks worse**.

**Leaves driving the most lag** (by citing-site count):

| leaf | sites |
|---|---|
| `vol3/cosmology/ch05-dark-sector/delta-strain-cosmic-tcc.md` | 18 |
| `common/vocabulary-register.md` | 17 |
| `common/form-deriving-value-importing.md` | 14 |
| `vol9/ch3-pin-port-configuration/device-circuit-models.md` | 12 |
| `vol1/claim-quality.md` | 9 |
| `common/translation-tables/translation-circuit.md` | 9 |
| `common/engine-capability-map.md` | 9 |

## §2 — THE FIVE UNDISCLOSED BUILD-BAND SITES

Printed prose citing a claim the KB grades `do-not-build`, with no demotion
banner within ±15 lines and not in a lookup-table row:

| site | claim | KB grade |
|---|---|---|
| `vol_9.../02_absolute_maximum_ratings.tex:35` | `clm-ezai5b` | do-not-build, solidity 0.4 |
| `vol_9.../02_absolute_maximum_ratings.tex:38` | `clm-uu6dl5` | do-not-build, solidity 0.4 |
| `vol_9.../16_cross_volume_reference.tex:189` | `clm-ezai5b` | do-not-build, solidity 0.4 |
| `vol_9.../16_cross_volume_reference.tex:197` | `clm-uu6dl5` | do-not-build, solidity 0.4 |
| `vol_9.../figures/g_star_comparison.tex:32` | `clm-uu6dl5` | do-not-build, solidity 0.4 |

`clm-uu6dl5` is *Effective Degrees of Freedom $g_* = 343/4 = 85.75$*. The figure
caption at `g_star_comparison.tex:32` renders it as a flat comparative fact
against the Standard Model's 106.75 with no grade qualifier. **These five are
CANDIDATES, not verdicts** — see §4.

## §3 — WHAT THE EPIC'S OWN STATE IS

> 🔴 **CORRECTED 2026-09-06, same day, before any lane consumed this.** The
> first version of this section said *"the waves did not execute"* and *"exactly
> one merge touched a volume `.tex`"*. **Both were false.** They came from four
> `git log` path globs — `manuscript/vol_0`, `vol_1`, `vol_2`, `vol_9` — that
> match **zero files**, because the real directories are
> `vol_0_engineering_compendium`, `vol_1_foundations`, `vol_2_subatomic`,
> `vol_9_vacuum_datasheet`. A zero result from a glob that matches nothing is
> not evidence. The corrected query (`-- 'manuscript/*.tex'`) returns **18
> merges**. This is the corpus's own named failure mode — a command that
> succeeded on the wrong state — and the standing rule it violates is: **verify
> any path filter matches a non-zero file set before trusting a zero result.**

**The epic EXECUTED.** Board §6 records all 12 epic PRs merged by Grant on
2026-08-03: #825 #826 #827 #831 #836 #839 #840 #842 #843 #844 #846 #847 #848
#850 #852 #853. Audit tags `audit/2026-08-03_mr-*` pin each lane tip.

What §6 records as NOT done, as of 2026-08-03:

- **STILL GATED — the ringdown wave (12 findings).** The cold-Q arc landed a
  **non-verdict**: #845 = `SOLVER-NOT-CERTIFIED`, all four frozen physics bins
  read *N/A*. #854 was the live retry. vol3 ch08 + ch15, `backmatter/07:{85,
  211,213}` and the ringdown mirror sites stayed unexecuted. **Disclosed cost,
  in print:** `backmatter/07` prints a withdrawal at `:145` while `:211/:213`
  still print the withdrawn claim.
- **OWED — 4 board corrections** (`backmatter/01_appendices.tex:{132,135,196}`
  re-tag; vol5 `07_solvent_damping.tex:41` mechanical→routed; the neon caption
  cite is `:53` not `:54`; `A_heavy_element_catalog.tex:20` dispatched as
  EXECUTE while `[REFUTED — dropped]`, reverted in #852).
- **OWED — addenda**, six site-classes with receipts in their PRs.
- **OPEN — 5 routed to core/Grant**, including the Petermann split
  (`C_2 = -0.32846` leaf vs `-0.328427` driver, ~158 ppm, load-bearing in g-2)
  and the cite-rot fix option (#850 — `verify-md-links` still strips `:NN`, so
  ~1,800 backticked bare cites remain wholly unchecked).

**What is therefore still unknown, and is the actual open question:** the
post-wave state of the 154 findings five weeks later. The board's dispositions
were 58 ruling-needed / 46 mechanical / 33 route-to-core / 12 gated-ringdown /
1 defer-to-live-lane. A re-validation lane against `6b8b49a0` is running.

**What the churn numbers do say** (these were computed correctly and stand):

```
KB commits since board base 19285c5d:   288   (190 KB files changed)
tex commits since board base:           187   (121 tex files changed)
```

Both sides moved substantially after the waves landed, which is what the 190
material-lag sites in §1 measure.

## §4 — CALIBRATION, AND WHY THE HEADLINE NUMBER MOVED THREE TIMES

The `S3` count went **53 → 28 → 12 → 5** across three calibration passes. Each
cut removed a real false-positive class, and each is recorded because the
uncalibrated number would have been reported as a defect count:

1. **53 → 28.** Dropped `status=proposed` and `status=ambiguous`. **All four
   `ilk-` nodes in the corpus are `proposed`** — it is the universal state for
   that node class, so citing one is not drift. `ambiguous` is a legitimate
   disambiguation-node status. `ilk-gravmb` alone accounted for 15 of the 53.
2. **28 → 12.** Dropped sites carrying a Rule-12 demotion banner nearby.
   `vol_3.../14_macroscopic_orbital_mechanics.tex:228` cites a solidity-0.2
   claim **under its own `🔴 DEMOTED 2026-07-19` banner** — honest, not stale.
3. **12 → 5.** Dropped two further classes found by hand-checking: sites whose
   caveat wording the first regex missed (`vol_5.../01_biophysics_intro.tex:118`
   reads *"a **coarse-correctness** result … not an atomic-precision
   validation"* and quotes the solidity inline), and cross-reference **table
   rows**, where a claim-id is a provenance pointer rather than an assertion.

**A tool bug was found and fixed mid-audit and is worth recording:** a
string-replace intended for the report's `order` list also rewrote two
`findings[...]` append keys into tuples, silently routing 17 findings into
buckets the report never printed. It surfaced only because the S3 sub-counts
stopped summing to the independent recount. **The sub-totals now reconcile
exactly (5+17+6 = 28), and that reconciliation is the tool's own check.**

## §5 — WHAT THIS AUDIT DOES NOT ESTABLISH

- **It does not say any of the 190 sites is wrong.** It says the cited leaf
  changed materially after the print did. Adjudicating each needs reading the
  leaf's diff against the printed sentence. That is the next stage and it is a
  judgment lane, not a script.
- **S5's 49 anchor-drift hits are mostly unverified-not-broken.** Only anchors
  past end-of-file are hard errors; the rest mean "the leaf changed after this
  `.tex`, so the `:NNN` may point at different bytes." Content-level anchor
  verification is what `verify-anchor-content.py` does and this tool does not
  duplicate it.
- **Method and blind spots.** The scan reads non-comment `.tex` lines only
  (`%`-comments are not printed). It finds cites in two forms — an `ave-kb/…​.md`
  path, and a bare `clm-`/`def-`/`ilk-`/`exp-`/`sup-` id. **A stale statement
  that cites nothing is invisible to it**, and that class is not measured here;
  the 2026-07-01 audit found such sites by reading, which is why the reading
  lane is not optional. Cross-repo cites, `figures/*.tex` that inherit context
  from their parent chapter, and `papers/` are in the scan but their conventions
  were not separately validated.
