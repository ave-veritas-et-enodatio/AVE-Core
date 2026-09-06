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

## §1 — THE ONE NUMBER THAT MATTERS: 190

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

The 2026-08-02 manuscript-reconciliation board
(`_orchestration/2026-08-02_manuscript-reconciliation-board.md`, 154 classified
findings, Grant-ratified verbatim *"proceed"*) is based on `main` @ `19285c5d`.

**Since that base, exactly one merge touched a volume `.tex`** (`ff06fffd`,
oort-walkback-propagation). Meanwhile:

```
KB commits since board base:   288   (190 KB files changed)
tex commits since board base:  187   (121 tex files changed)
```

**The waves did not execute, and the board is now five weeks stale against both
sides.** Its 154 findings need re-validation against `6b8b49a0` before any of
them is dispatched; a finding whose cite has drifted is a vacated argument, not
a wrong one.

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
