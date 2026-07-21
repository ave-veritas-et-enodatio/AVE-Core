# RESULT — Kerr-table-correction re-adjudication: **MATCH-ARTIFACT** (walk-back)

**Lane:** kerr-table-canon-correction (upstream follow-on of PR #772)
**Date:** 2026-07-20
**Prereg (frozen, criteria set before run):** [`2026-07-20_kerr-table-correction_prereg-FROZEN.md`](2026-07-20_kerr-table-correction_prereg-FROZEN.md)
**Re-run (deterministic):** [`2026-07-20_kerr-table-correction_rerun.py`](2026-07-20_kerr-table-correction_rerun.py)
**Reference verification (this session, cross-checked):** qnm package + BCW-2006 fit; see prereg §0.

---

## Verdict against the frozen bins

> **MATCH-ARTIFACT** — `|D̄| = 9.53% ≥ 5%`.
> The banked "−0.45% mean ω_R, covers entire LIGO BBH catalog at GR-class precision,
> FULL PASS" agreement was two compensating errors: a **source-vs-detector-frame mass
> mismatch** (≈+9% frequency inflation) cancelling a genuine **≈−10% below-Kerr deficit**.
> The honest v2-vs-data state at the catalog spins is **≈−9.5%** (dimensionless,
> frame-independent) / **≈−11%** (detector-frame frequency) — **−9.53% under the banked
> v2 `x_sat(a*)` spin mapping; mapping-conditional.** This is a **flagship
> consistency-result walk-back** — flag prominently for Grant.
>
> **★ Mapping-conditional / fork-reopen (do not read as "AVE is −9.5% off"):** the
> −9.53% is conditional on the **retained v2** `x_sat(a*)` mapping, and that mapping's own
> 2026-05-18 selection over v1 rode the same corrupt table + frame mixing this lane corrects.
> On the same frozen C-1 dimensionless comparator, the **retired v1** mapping sits
> **+2.63% mean** vs corrected Kerr — *inside* the frozen `MATCH-SURVIVES |D̄| < 3%` band.
> See **§ FORK-REOPEN** below. The Grant foreword ruling should see BOTH numbers.

The frame-mixing model is **confirmed**: the re-run's BANK reconstruction
(v2 @ source-frame mass vs detector-frame obs) reproduces the leaf's exact banked
per-event numbers −2.00% / −1.22% / +1.87% (mean −0.45%). GR sanity: true Kerr at
**detector-frame** mass reproduces GW150914's observed 251 Hz to −0.99% (GR ringdown
consistency holds), while AVE-v2 at the same detector-frame mass gives 226 Hz (−10.1%).

## Corrected-vs-banked comparison table

| quantity | BANKED (leaf, 2026-05-18) | CORRECTED (this lane, 2026-07-20) |
|---|---|---|
| Kerr (2,2,0) ω_R·M at a*=0.90 | 0.53039 (in-repo table) | **0.67161** (qnm/BCW; in-repo was −21%) |
| Kerr (2,2,0) ω_R·M at a*=0.95 | 0.54652 | **0.74632** (in-repo was −27%) |
| AVE-v2 vs Kerr, dimensionless (mean, a*=0.64–0.74) | "+5.48%/+9.16% excess near-extremal" / "−0.45% vs LIGO" | **−9.53%** (AVE sits BELOW Kerr, growing with spin) |
| AVE-v2 vs obs, GW150914 detector-frame | −2.0% (frame-mixed) | **−10.1%** |
| AVE-v2 vs obs, mean 3 events (frame) | −0.45% | **−10.97%** (detector-frame) |
| Cold a*=0 eigenvalue (18/49 vs Kerr) | −1.7% | **−1.69%** (SURVIVES — genuine zero-free-parameter result) |
| decay-time τ "−0.47% mean, outperforms GR (−6.94%)" | banked | **frame- + ω_I-table-artifact-contaminated** — the τ chain rides the same source-frame masses AND the separately-corrupt ω_I table (high by +11%/+26% at a*=0.90/0.95); a full τ re-run is a flagged follow-on, but the −0.47% "match" does not survive the frame correction |

## Per-event frozen-bin outcome

| event | a* | C-1 dimensionless dev | C-2 detector-frame dev | bin |
|---|---|---|---|---|
| GW150914 | 0.67 | −9.19% | −10.09% (GR gate clean) | ARTIFACT |
| GW170104 | 0.64 | −8.59% | −16.29% (f_obs import-limited) | ARTIFACT |
| GW151226 | 0.74 | −10.83% | −6.54% (f_obs import-limited) | ARTIFACT |
| **mean** | | **−9.53%** | **−10.97%** | **MATCH-ARTIFACT** |

The C-1 dimensionless comparator is authoritative (frame- & mass-independent, depends
only on the well-measured spin). The C-2 per-event detector-frame numbers for
GW170104/GW151226 are import-limited (their KB-cited f_obs fail the GR sanity gate, i.e.
they are not clean l=m=2 QNM detector-frame frequencies) — flagged, does not change the bin.

## What survives / what walks back (Rule-11 both-preserved)

**SURVIVES (genuine, unchanged):**
- Cold Schwarzschild ℓ=2 eigenvalue `ω_R·M = 18/49 = 0.3673` vs Kerr `0.3737` (**−1.7%**),
  zero free parameters — the clean ν_vac=2/7 derivation. (ν_vac VALUE is GR-imported via
  K=2G per PR #261; FORM-derived — prereg provenance-rider.)
- The ORG-1-class multipole-ratio content (ν-free) is untouched by this lane.

**WALKS BACK (was flagship, now artifact):**
- The spinning-remnant "−0.45% ω_R / −0.47% τ / FULL PASS / covers entire LIGO BBH
  catalog at GR-class precision" match. Honest state: **the banked v2** `x_sat(a*)` mapping
  sits **≈−9.5% below Kerr** at catalog spins (a*=0.64–0.74), growing with spin (−12.6% at
  0.80, −20% at 0.95) — **mapping-conditional; see § FORK-REOPEN** (the retired v1 mapping is
  +2.63% mean, inside the frozen survives-band, and the v1→v2 fork's own adjudication is
  contaminated).
- The Phase-4 "v2 reproduces the GR Kerr curve at <3%" claim (it rode the corrupt table).
- The C1-BH-RING "FULL PASS" grade → the ν_vac=2/7 cascade is NOT empirically anchored at
  the C1 node by the spinning match (the cold eigenvalue's −1.7% is the only surviving
  C1 empirical content, and it is a single-point −1.7% consistency figure, not a "PASS").

**Note on sign vs the #772 ORG-2 finding:** #772's ORG-2 froze a "positive near-extremal
excess (AVE ABOVE Kerr)" prediction on the corrupt table; against corrected Kerr the sign
inverts (AVE BELOW Kerr). This lane's independent re-derivation confirms AVE-v2 is
monotonically below true Kerr at every spin — consistent with #772 findings 0/5.

## ★ FORK-REOPEN — the v1↔v2 spin-mapping fork (routed to GRANT; substrate-adjudicates-forks)

*Surfaced by the PR #774 adversarial review (finding 0, CONFIRMED MAJOR); computed by the
review and reproduced deterministically this lane.*

The 2026-05-18 Option-A adjudication that **retired the v1 spin mapping in favor of v2**
(`research/ligo-ringdown-driver-design.md` §8: *"Per Grant directive 2026-05-18 … selecting
Option A"*) was decided on the **same two errors this lane corrects**: the corrupt Kerr QNM
table AND source-vs-detector frame mixing. The load-bearing "v1 over-predicted spin correction
by ~13% mean" diagnosis (design doc §8.2 line 288: *"Mean AVE-v1-vs-LIGO: +12.98%"*) is the
**frame-mixed artifact** — v1 frequency at *source-frame* mass vs *detector-frame* `f_obs`,
reproducible only against the corrupt table — **not** a dimensionless comparison to true Kerr.

Against **corrected** Kerr on this lane's own frozen **C-1 dimensionless comparator**, the
retired v1 mapping (`x_sat,v1 = 7·r_ph⁺/3M`, entire cavity compliant; `ω_R·M = ℓ(1+ν_vac)/x_sat`)
sits at:

| a* | v1 vs corrected Kerr | v2 vs corrected Kerr |
|---|---|---|
| 0.64 (GW170104) | **+2.24%** | −8.59% |
| 0.67 (GW150914) | **+2.50%** | −9.19% |
| 0.74 (GW151226) | **+3.17%** | −10.83% |
| **catalog mean** | **+2.63%** | **−9.53%** |
| 0.95 (near-extremal) | +6.5% | −20.1% |

So on the **same frozen mean-`|D̄|` comparator the lane authored**, the **retired v1** mapping
lands **inside the frozen `MATCH-SURVIVES |D̄| < 3%` band** (prereg §3), while the **retained
v2** fails (MATCH-ARTIFACT). v1 outperforms v2 at every catalog spin and near-extremal. The
two-component (rigid K4 skeleton + compliant photon-orbit) physics that motivated Option A now
stands **empirically disfavored** vs the single-component v1.

**What this does NOT do — no silent v1 re-bank.** v1-vs-corrected-Kerr was **never** evaluated
under this prereg's frozen bins (the prereg froze the **v2** mapping only). The **+2.63% is
banked WITH PROVENANCE** (review-computed, reproduced this lane via `_rerun.py`'s v1 branch) as
a **fork-reopen datum**, not a validated match. The re-adjudication is **Grant's**, with a
**fresh frozen-first lane as the routed follow-on** — do not silently re-select v1.

**What this does to the foreword walk-back framing (R1d).** The flagship BANKED match is **void
either way** — neither +2.6% nor −9.5% is the banked sub-percent FULL PASS. But the honest
forward state is **"the AVE spin-mapping fork is REOPENED with v1 as the surviving candidate at
+2.6% mean vs true Kerr,"** *not* "AVE is −9.5% off." The Grant foreword ruling should see BOTH.

## Re-bank / propagation (landed in the following commits + flagged)

Fixed in this lane (implementer scope):
- `src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py` — both tables corrected + banner.
- `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md` — Rule-12 re-bank.
- `manuscript/ave-kb/common/divergence-test-substrate-map.md` — C1-BH-RING row re-grade.
- `research/ligo-ringdown-driver-design.md` §7–10 — corrected cites.

Flagged for Grant / auditor (Grant-ratified or manuscript-headline — flag-don't-fix):
- `manuscript/frontmatter/00_foreword.tex` "Second positive load-bearing empirical
  confirmation at scale" (LIGO ringdown) — the spinning match that promotion rests on is
  the artifact. **Walk-back candidate — flag prominently.** The ruling should see **BOTH**
  numbers (R1d / § FORK-REOPEN): the honest forward state is **"the spin-mapping fork is
  reopened with v1 as the surviving candidate at +2.6% mean vs corrected Kerr,"** not
  "AVE is −9.5% off." A fresh frozen-first v1-vs-corrected-Kerr lane is the routed follow-on.
- `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex` — already
  frames the spinning match as "post-hoc consistency check" but STILL reports the −0.45%/
  −0.47% numbers (the artifact numbers). Auditor lands the number correction.
- `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-c11-mach-zehnder.md` — C1 "FULL PASS" cascade reference.
- `manuscript/ave-kb/claim-quality-closure-roadmap.md` changelog (2026-05-18 C1 entries) — historical log; add dated correction entry.
- `manuscript/ave-kb/.index/claims.jsonl` / `common/claim-quality.md` clm-395gps — solidity
  0.55 rationale needs a frame-artifact rider (auditor/Grant lands the register grade).
- `manuscript/vol_9_vacuum_datasheet/chapters/{12,15,16}` + vol9 KB index C1 rows.
