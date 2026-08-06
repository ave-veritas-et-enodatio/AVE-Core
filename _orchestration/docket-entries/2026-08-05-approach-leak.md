# Docket fragment — the approach-leak lane (2026-08-05, EXECUTION RECORD)

**Key:** `approach-leak` · **Branch:** `research/approach-leak` · **Base:** `origin/main` = `c4fdced0`
**Dispatch:** the last open number under the channel-scoped kernel-collapse ruling
([`2026-08-05-ruling-kernel-collapse-rescope.md`](2026-08-05-ruling-kernel-collapse-rescope.md):18
— *"the leak is one computable number"*).
**Artifacts:** [`research/2026-08-05_approach-leak_prereg-FROZEN.md`](../../research/2026-08-05_approach-leak_prereg-FROZEN.md)
(`bdb8b4a4`, pushed ALONE) · [`research/2026-08-05_approach-leak_result.md`](../../research/2026-08-05_approach-leak_result.md)
· `research/drivers/approach_leak.py` (`48076793`) · `research/drivers/approach_leak_results.json`
· `research/drivers/approach_leak_number_check.py` (gating via `make verify`).
**SVA pilot case 7** (v0.2 header, eleven rows).

---

## Outcome, one screen

**`LEAK-NOT-CERTIFIED`. NO BIN IS ADJUDICATED.** Nine of ten gates PASS; all six self-tests FIRE;
`G-NC-SLAST` FAILS on **this lane's own freeze error** — a `1e-40` tolerance sized against a
round-off error model when the limiting error is the predecessor's float64-seeded input precision.
The two values agree to 17 significant digits (`2.04408e-17` relative). **The tolerance was not
retuned**; the frozen global consequence was honoured.

**The physics is shipped in full as a NOT-ADJUDICATED DIAGNOSTIC**, and it has a clean structure:

- The whole question collapses onto ONE exponent, `p`, in `ω_m(r) = 2ω_C·S(r)^p`.
- **There is an exact knife-edge at `p = 2`**, derived at freeze and confirmed:
  `p < 2` ⇒ no intact cell open; `p > 2` ⇒ cells open; `p = 2` ⇒ **mass-independent**, decided by
  `Ω < 4θ` alone. `G-KNIFE` measures the mass-spread at `p = 2` at `7.77877e-62` across a `100×`
  mass lever; `FT-KNIFE` shows the mass-trend **reversing sign** across it.
- **`p` is not in canon.** Two-method absence receipt over `4418` tracked files, engines named
  (`git grep -P` PCRE-ASCII vs Python `re` Unicode, **no `\b` anywhere in the battery**):
  **zero hits for any `I_ω(A)` grading law**; the only substantive `G_c`-grading hit is the ENGINE
  line `cosserat_field_3d.py:767`, which canon has never ratified.
- On every member canon or the engine actually states — including **both** the dispatch's `p = 1/2`
  **and** the engine's coded `p = 1` — `N_open = 0` at all `6240` rows, with margins of `24.3`–`28.5`
  and `8.06`–`9.74` orders of magnitude in `S`. Cells open only at `p ≥ 2.5`, which requires an
  `I_ω ∝ S^{−3}` law that exists nowhere.
- **The leak bound and the verdict are the same inequality** (`ζ_max < 1`), derived at freeze and
  numerically confirmed to `2.77978e-59`. At the engine's own `p = 1`, `ζ_max = 7.64e-17` — a pure
  dimensionless ratio carrying **no absolute modulus**, because the same `G_c` sets both the drive
  strength and the gap.
- **Zero transported power is a theorem with a measured input:** `G-REAL` puts
  `min(ω_m² − ω²) = 1.13450335861760625511643046057e-38` in `ω_C²` units, strictly positive, so the
  transfer function is real and `⟨P⟩_period = 0` exactly. Reactive store on the Axiom-3 rim; no port
  crossed.

**Where the diagnostic points (a pointing, NOT an adjudication):** `GAP-CLOSED` co-firing with
`UNDERDETERMINED-CANON`. A successor with correctly-sized tolerances awards it.

---

## What is owed to the orchestrator

| # | item | owner |
|---|---|---|
| **1** | **A successor lane (`approach-leak v2`)** with `G-NC-SLAST` re-sized to the precision the predecessor SHIPPED its input at, or re-anchored on the predecessor's own rung value. Nothing else changes. | this lane's successor |
| **2** | **FLAG-IOMEGA — a NEW canon gap**, distinct from the five the last-bond lane enumerated: **no `I_ω(A)` grading law exists anywhere**, and the leak verdict turns over on it. Minted as a question, not filled with a default. | Grant / canon |
| **3** | **FLAG-EXP** — the dispatch's stated `gap ∝ √S_ε` disagrees with the engine's `G_c·S_eps_sq = G_c·S_ε²` (`gap ∝ S_ε`). Declared at freeze. The pointing survives both; the arithmetic does not. | orchestrator |
| **4** | **FLAG-MECH** — the last-bond lane's §2.3 *"band collapse, not a gap opening"* names the mechanism for the **normalized-L2** member only; on the **L∞** member the engine actually codes, the band top does not descend and the drive is **below a gap**, not above a top. Same conclusion, opposite mechanism. Predecessor file byte-untouched. | auditor |
| **5** | **FLAG-ROTTOP** — canon has **no micro-rotation band top**; the corpus's five near-hits are all the vector/Cosserat-**translational** bracket. Bracketed at three members here, none chosen, **moot on every below-knife member and reported as moot**. | auditor |
| **6** | **Three SVA v0.2 amendment proposals** (§8 of the result), **routed not drafted** — the auditor lands SVA amendments: (a) row 9's pre-freeze second-method check should extend to **negative-control** tolerances (this lane's failure landed exactly in that gap); (b) row 11 should name a **NO-ITERATION declaration** as a required positive fill; (c) row 4 should name **"declare the observable plane-invariant"** as an explicit option. | auditor |
| **7** | The standing **umbrella-glob proposal** for lane number-checks remains **PENDING**; this lane disclosed the two-shared-line union-conflict class rather than adopting it unilaterally. | orchestrator |

---

## Fences honoured

- **Nothing about the rotational channel AT or INSIDE `r_sat`.** The ruling's carve-out and its
  ROUTED penetrating-radiation frontier item are untouched; **MeV-scale rotational radiation is out
  of scope**, one cross-reference line only (result §6.2).
- No adjudication of the cross-grade aggregation fork, FORK-3(b), the `β` bracket, the `K(A)` fork,
  `FLAG-CAUSAL`, or any predecessor's bins.
- No promotion of the engine's coded `a = 2` to canon; no invention of an `I_ω(A)` law. The RHO-B
  `1/S³` grading is applied to the micro-inertia **by ANALOGY and labelled as one at every site**.
- No AVE-vs-competitor discriminator: the ECO free-reflectivity degeneracy applies unchanged.
- **`research/` + this docket fragment + the Makefile target only.** No KB, no manuscript, no
  `src/ave`. Engine byte-untouched and **never imported** (constants read by `ast` literal parse,
  gated by `G-CANON` against the canonical identities). Every predecessor artifact byte-untouched.
- Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; moves no solidity; edits no falsification ledger.
