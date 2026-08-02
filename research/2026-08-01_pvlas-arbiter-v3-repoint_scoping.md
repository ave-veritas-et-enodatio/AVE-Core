# PVLAS arbiter v3 re-point — GATED SCOPING (Grant ruling D7)

**Class:** scoping only. **Nothing re-pointed.** `src/` is byte-untouched on this branch;
`manuscript/` is byte-untouched; `papers/` is byte-untouched. This document is the
consumer-and-letter sweep that Grant ruling **D7** made the *gate* on the re-point, plus the
gate verdict and the three execution blockers the sweep surfaced.

**Grant ruling D7 (2026-08-01), verbatim `[sic]`:** *"D7: follow your rec"*

The rec D7 adopts is option **(i)** — *re-point the live bench arbiter to v3* — **GATED on a
consumer-and-letter sweep coming back clean.** The gate is the operative clause. This lane ran
the sweep. **The letter gate did not come back clean.** Per the gate's own stop condition the
re-point was **not executed**, and the surface is routed back to Grant.

---

## 0. Scope fence, stated first

| | |
|---|---|
| **Executed** | Gate 1 (three-method consumer sweep) + Gate 2 (letter check) |
| **NOT executed** | the re-point itself (D7's payload), any test re-pin, any docstring edit |
| **Files modified** | this doc + `_orchestration/docket-entries/2026-08-01-d7-repoint-pvlas.md` |
| **`src/ave/` bytes changed** | **0** |
| **`manuscript/` bytes changed** | **0** |
| **`papers/` bytes changed** | **0** |
| **ids minted** | **0** — no `clm-`/`def-`/`sup-` node, no solidity change, no KB status flip |
| **Physics adjudicated** | **none.** The v2-vs-v3 footing is *already* adjudicated (KB is truth-source); what is NOT adjudicated is surfaced in §4 |
| **Lane isolation** | throwaway worktree off `origin/main` @ `19285c5d`; branch `src/repoint-pvlas-v3` |

**Out of scope by dispatch:** `src/ave/qed/*` (a concurrent lane holds
`src/deprecate-superseded-birefringence-ratio`). Overlap verified zero — see §5.

---

## 1. Context verification (verify-before-cite — three brief cites corrected)

Every context claim in the dispatch was re-verified against the tree before any sweep ran.
**Three cites in the dispatch are off; all three are content-correct but path/line-wrong, and
none changes the physics.** Recorded because a `path:line` that does not resolve is exactly the
weak-anchor failure the discipline exists to catch.

| # | Dispatch said | Verified state | Verdict |
|---|---|---|---|
| C1 | KB leaf at `manuscript/ave-kb/vol4/**circuit-theory/ch1-vacuum-circuit-analysis**/vacuum-birefringence-e4.md` | the leaf is at `manuscript/ave-kb/vol4/**falsification/ch12-falsifiable-predictions**/vacuum-birefringence-e4.md`. The cited `circuit-theory/ch1-…` directory **does contain** `node-up-small-large-signal.md`, which the leaf cites at `:85` — plausibly the cross-cite that got transposed. | **path WRONG**, content right |
| C2 | *"the **boxed** re-frozen v3 … at `:104`"* | `:104` carries the v3 equation in a plain `$$…$$` (the OPTION-B body consolidation). The **`\boxed{}`** v3 is at **`:34`**, inside the 🔵 FOOTING RE-FREEZE note. Both read $15\pi/4\alpha^2=3.75\pi/\alpha^2\approx2.2\times10^5$. | **line off**, content right (two sites agree) |
| C3 | HEAD `e6de554b` | `origin/main` is **`19285c5d`**; `e6de554b` is 2 commits back (`19285c5d` merge #818 → `41d54303` → `e6de554b` merge #817). Worktree branched from `19285c5d`. | **stale by 2 commits** |
| — | `:106` states *"v3 is exactly half v2"* | **VERIFIED verbatim** at `:106`: *"v3 is exactly half v2, the $\langle\cos^2\rangle=\tfrac12$ carrier average removed."* | ✓ |
| — | `coefficient_ratio_differential_pvlas()` returns `4.424666e+05` | **VERIFIED live** — see §1.1. Function content-located at `src/ave/bench/birefringence.py`:**391-418**. | ✓ |

The KB's own **numbering disambiguation** is at `vacuum-birefringence-e4.md`:61 — *"labels are v1
$=7.5/\alpha^3$, v2 $=7.5\pi/\alpha^2$, v3 $=3.75\pi/\alpha^2$"* — so the dispatch's v2/v3 labels
are KB-correct. ⚠ **Beware a second, colliding numbering:** the Letter's `provenance.md` uses
"v1"/"v2" for *document* revisions, where the Letter's **v1** carries the value-level **v2**
($7.5\pi/\alpha^2$) and the Letter's **v2** carries the value-level **v3** ($3.75\pi/\alpha^2$).
Two version axes, opposite offsets. §3 uses value-level labels throughout and tags document
versions explicitly.

### 1.1 Numeric receipts — banked live on this branch

```
ALPHA                                      = 0.0072973525693
(E_CRIT/E_YIELD)^2 = 137.035999083696  ==  1/ALPHA = 137.035999083696   (identity holds)
7.5*pi/ALPHA**2        (v2)                = 4.4246658351e+05
15*pi/(4*ALPHA**2)     (v3, closed form)   = 2.2123329175e+05
3.75*pi/ALPHA**2       (v3, equivalent)    = 2.2123329175e+05
(0.5*(E_CRIT/E_YIELD)**2)/(2*ALPHA/(15*pi))(v3, ratio form) = 2.2123329175e+05
LIVE coefficient_ratio_differential_pvlas(geometry="propagating") = 4.4246658351e+05
LIVE coefficient_ratio_differential_pvlas(geometry="static")      = 8.8493316702e+05
```

**v2 / v3 = 2.000000 exactly** — the KB's `:106` *"exactly half"* is reproduced, and the three
independent routes to v3 (closed form, $3.75\pi$ form, ratio form through the substrate identity)
agree to 1e-12. The KB box's stated precision is $\approx2.2\times10^5$; all three routes match it.
So the arithmetic target of a D7 re-point is unambiguous: **`2.212333e+05`**, derivable from
`ave.core.constants.ALPHA` (or, equivalently, from `E_CRIT`/`E_YIELD` through the substrate
identity) with no magic number.

## 2. GATE 1 — consumer sweep, three methods

Per the D1 lane's precedent (`_orchestration/docket-entries/2026-08-01-d1-deprecate-ratio.md`,
"★(d) LIVE-CALLER SWEEP — clean negative, THREE methods agreeing"): `git grep` over the tracked
tree; an independent filesystem `grep -rn` (sees untracked files the index cannot); and an **AST
`Call`/`ImportFrom`/`Attribute` node scan** over every `.py` under the repo (1307 files parsed,
excluding `.git`, `.claude/worktrees`, `.venv`, `_archive`).

⚠ **A shell-glob false-negative was hit and corrected mid-sweep** (the standing
grep-completeness-false-negatives lesson): zsh expanded `--include=*.py` as a glob and aborted
method 1's first invocation with `no matches found`. Re-run with quoted pathspecs. Recorded
because a silent zero here would have been read as "no consumers".

### 2.1 GATE-1 VERDICT: **CLEAN.** Five call sites, three files, all record-only.

The AST scan is authoritative for callers and returns **exactly 5 `Call` nodes + 4 imports + 0
bare attribute references**; methods 1 and 2 return the same file set. **No call site is inside
`src/ave/`** — the arbiter has no internal consumer. **No call site feeds a `P_flip`, a bin edge,
a verdict function, or any adjudicated quantity**; every one of the five writes the value into a
JSON record and prints it as context. That is the substantive Gate-1 finding: *the re-point is
behaviourally inert for every downstream prediction*, which is exactly what the KB predicts
(`vacuum-birefringence-e4.md`:44, footing-invariance of the $P_{flip}$ headline).

| # | Site | Kind | Argument | What it does with the value | Class |
|---|---|---|---|---|---|
| 1 | `src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py`:382 | live caller | `geometry="propagating"` | `out["matched_differential_ratio_7.5pi_over_alpha2_propagating"]` + a print; **not** consumed by the `P_flip` chain below it | live, record-only |
| 2 | …`birefringence_gap1_hibef_feasibility.py`:385 | live caller | `geometry="static"` | `out["matched_differential_ratio_15pi_over_alpha2_static"]` | live, record-only |
| 3 | `src/scripts/vol_9_device/birefringence_hibef_scenario_predictions.py`:136 | live caller | `geometry="propagating"` | same key + print; the per-scenario table is computed independently | live, record-only |
| 4 | …`birefringence_hibef_scenario_predictions.py`:140 | live caller | `geometry="static"` | static key | live, record-only |
| 5 | `src/scripts/vol_9_device/birefringence_prior_art_exposure_scan.py`:359 | live caller | `geometry="propagating"` | same key + print; the CLEAN-FIELD gate is computed independently | live, record-only |
| — | `src/ave/bench/__init__.py`:81, :159 | re-export + `__all__` | — | public-API surface only | export |

### 2.2 Value consumers (the `4.42…e5` / `7.5π/α²` pattern set), classified

Pattern set swept: `4.42`, `4.424666`, `4.4e5`, `4.4247`, `442466`, `7.5\s*\*?\s*(np\.)?pi`,
`7.5π`. Raw-hit count across `src/ scripts/ research/ manuscript/ _orchestration/ papers/
claim-prereg-ots/` = **245**; below is the classified set after dropping unrelated float
substrings inside simulation-output JSON (e.g. a `4.42…` timestep in
`bemf_feedback_results.json`), which are numerically coincidental and physically unrelated.

| Site | Content | Class | Re-point impact |
|---|---|---|---|
| `src/ave/bench/birefringence.py`:402 | docstring *"= 7.5\*pi/alpha^2 ~ 4.42e5"* | **the arbiter itself** | rewritten by the re-point |
| `src/ave/bench/birefringence.py`:376-388 `coefficient_ratio_differential()` | already banner-stamped `==== SUPERSEDED (2026-07-03) ====`, returns v1 `1.93e7` | superseded sibling | none (untouched) |
| `src/tests/test_birefringence_v3_chain.py`:38,:41 | `assert isclose(chain["v2"], 7.5*pi/ALPHA**2)`; `assert isclose(chain["v2"], 4.4247e5)` | **test pin — on the CHAIN driver, not on the arbiter** | **NONE.** See §2.3 |
| `src/scripts/vol_4_engineering/birefringence_coefficient_discriminator.py`:158-176 | computes v1→v2→v3 and self-asserts the closed forms | independent v3 implementation | none |
| `src/scripts/vol_9_device/*.py` ×3, comment blocks at :378-381 / :133-135 / :356-358 | *"CORRECTED (2026-07-03) … 7.5 pi/alpha^2 ~ 4.42e5"* narration | live driver comments | would need per-site rewrite |
| `src/scripts/vol_9_device/*.py` ×3, JSON key literal `matched_differential_ratio_7.5pi_over_alpha2_propagating` | **the key NAMES the value** | live driver output schema | **BLOCKER-2, §4** |
| `src/scripts/vol_9_device/_output/birefringence_{gap1_hibef_feasibility,hibef_scenario_predictions,prior_art_exposure_scan}.json` | `442466.5835078048` under that key | committed driver output (letter-cited) | value moves on re-run |
| `src/scripts/vol_9_device/_output/vacuum_birefringence_{bench,facility_sweep}.json` | `442466.58353669324` under `"PVLAS A_e differential (~1.45)"` | **LOOK-ALIKE, NOT A CONSUMER** — see §2.4 | none |
| `src/ave/bench/adopters.py`:13,:86,:138,:152,:180-191,:203,:214,:219,:221 | the whole bench spec, incl. `frozen=True` `Prereg` at :181 and `verdict_fn=lambda r: r > 1e6` at :214 | **v1-footing, NOT a consumer of this function** — see §2.5 | none from this re-point |
| `manuscript/ave-kb/vol4/claim-quality.md`:455-466 | 🔴 header quoting *"Corrected matched-differential ratio: $7.5\pi/\alpha^2\approx4.42\times10^5$"* + naming this function as the harness | **manuscript site, v2-footing, un-re-frozen** | **out of scope** (auditor lane owns KB) |
| `research/2026-07-03_…qed-normalization-correction.md`, `research/2026-07-05_field-convention-carrier-average_note.md`:107,:109,:219, `research/2026-07-05_qed-leg-crossing-angle_note.md`:22,:98 | dated research records | dated record | never edit |
| `manuscript/vol_4_engineering/chapters/12_falsifiable_predictions.tex`:120 | LaTeX comment, already v3-aware | manuscript site | none |
| `_orchestration/experimental/2026-06-04_round2-adjudications.md`:15,:161 | 2026-06-04 adjudication | dated record | never edit |
| `claim-prereg-ots/claims_by_hash.md`:9 | **OTS-anchored** v1-document registration quoting `7.5*pi/alpha^2 ~ 4.42e5` | **frozen public artifact** | never edit — §3.2 |
| `papers/2026_birefringence_letter/*` | **GATE 2** | — | §3 |

### 2.3 The one test that pins `4.4247e5` does NOT pin the arbiter

`src/tests/test_birefringence_v3_chain.py`:41 asserts `chain["v2"] ≈ 4.4247e5` — but `chain` is
`scripts.vol_4_engineering.birefringence_coefficient_discriminator.differential_ratio_v3_chain()`,
a **separate** implementation that already emits **v3 as its headline** (`:39`, `:42`:
`assert isclose(chain["v3"], 3.75*pi/ALPHA**2)` and `≈ 2.2123e5`). That module's own docstring at
`:12` reads *"v3 = 3.75 pi/alpha^2 ~ 2.2e5 = 15 pi/(4 alpha^2) `<-- THE HEADLINE`"*.

**So the corpus already carries a live, tested v3 implementation in `src/`** — it is simply not
the function the bench arbiter exposes. Nothing in `src/tests/` pins
`coefficient_ratio_differential_pvlas` at all (verified: zero hits for the function name under
`src/tests/`). Consequence: **D7's execute-step (c) — "any test pinning 4.42e5 updated" — has no
work in it.** The `4.4247e5` pin is a *chain-provenance* assertion (v1→v2→v3 arithmetic), and
re-pointing the arbiter must **not** touch it; deleting it would destroy the record of the very
carrier-average step D7 is applying.

### 2.4 Look-alike disclosed: two JSONs carry `442466.58…` from a DIFFERENT function

`vacuum_birefringence_bench.json`:74 and `vacuum_birefringence_facility_sweep.json`:106 carry
`442466.58353669324` under the key `"PVLAS A_e differential (~1.45)"`. This is **not** a consumer:
`vacuum_birefringence_facility_sweep.py`:398 calls `coefficient_ratio(A_EH_LITERATURE["PVLAS A_e
differential (~1.45)"])` — i.e. the **single-arm** function with the PVLAS static-duality
$a_{EH}=\alpha/(30\pi\alpha^2)=1.4544$.

The numeric coincidence is exact and worth naming so a future sweep does not misclassify it:
$$\text{single-arm }\tfrac14 \text{ over static } \tfrac{\alpha}{30\pi} \;=\; \frac{30\pi}{4\alpha^2}=\frac{7.5\pi}{\alpha^2}
\qquad=\qquad \text{differential }\tfrac12 \text{ over propagating } \tfrac{\alpha}{15\pi}$$
Two *mismatched-observable* pairings landing on one number because the $\tfrac12/\tfrac14$ and
$15/30$ factors of two cancel. Different function, different footing, **numerically identical to
the last digit of the shared route**. A re-point of the arbiter leaves both JSONs unchanged.

### 2.5 `adopters.py` is v1-footing and is NOT reachable from this re-point

The D1 lane routed `adopters.py` as its FLAG-DON'T-FIX #2 and escalated that
`verdict_fn=lambda r: r > 1e6` (`:214`) flips under v3. **Independently re-verified here, and the
reachability is the load-bearing part:** `adopters.py`:40-44 imports exactly three names —
`delta_n_ave_differential`, `delta_n_qed`, `vacuum_magnetic_birefringence_constant` — so it
**imports neither `coefficient_ratio_differential` NOR `coefficient_ratio_differential_pvlas`**
(the `coefficient_ratio_differential()` text at `:203`/`:219` is a *provenance string*, not a
call), and the AST scan finds zero calls to either in that file. `ratio_at` (`:103-105`)
recomputes the v1 pairing inline: `abs(delta_n_ave_differential(E)) / delta_n_qed(E,
a_eh=_A_EH_DIFFERENTIAL)` with `_A_EH_DIFFERENTIAL = 3.0/45.0` (`:72`).

⇒ **A D7 re-point of the arbiter does not move `adopters.py`'s verdict at all.** The frozen
`Prereg` at `:181` and the `>1e6` verdict remain on the v1 footing either way. Disclosed here so
the PR body cannot be read as claiming the re-point fixes it: it does not, and the frozen block
must not be edited. That surface stays exactly where D1 left it — routed, open, untouched.

### 2.6 Mid-lane supplement folded in — `adopters.py` re-derived at head

A mid-task supplement routed the D1 lane's `adopters.py` findings with the instruction to
re-derive them before acting. Done. **Two of the three claims reproduce exactly; the third
(reachability) does not, and the divergence is the load-bearing part.**

**★ Claim (a) — "the verdict-flip is a STOP-and-route condition same as the letter": DOES NOT
HOLD for a re-point of *this* function, and the disproof is empirical, not an argument.**

Reproduced first, so the flip itself is on the record as REAL:

```
ratio_at(1e13) = ratio_at(1e14) = ratio_at(3e16) = 1.930035e+07  ->  verdict_fn True
KB v3                            = 2.212333e+05  ->  verdict_fn False
v1/v3 = 87.2398   ==   2/(pi*ALPHA) = 87.2398        (KB :102 factor reproduced to 6 s.f.)
```

**But the flip is unreachable from D7's payload.** `verdict_fn` is applied to
`SensitivitySpec.observable_of = ratio_at`, and `ratio_at` recomputes the v1 pairing inline from
`delta_n_ave_differential` / `delta_n_qed(a_eh=3/45)`. Monkeypatching the arbiter to return v3 and
re-running the full bench model:

```
BASELINE   verdict=BANKABLE_AS_DISCRIMINATOR | ratio_at(1e13)=1.930035e+07 | verdict_fn=True
PVLAS->v3  verdict=BANKABLE_AS_DISCRIMINATOR | ratio_at(1e13)=1.930035e+07 | verdict_fn=True
VERDICT MOVED?  False
```

The banked verdict *does* exist and *is* pinned — `src/tests/test_bench_adopters.py`:33,
`assert r.verdict is Verdict.BANKABLE_AS_DISCRIMINATOR` — and it is **invariant under the
re-point**. ⇒ **`adopters.py` is not a STOP condition for D7.** The v1→v3 verdict flip is real but
belongs to a *different, un-fired* change (re-pointing `ratio_at`'s QED leg), which D7 does not
authorize and this lane did not make.

**★ Claim (b) — "the 7 non-frozen adopters sites are in-scope consumers for execute step
(d)/(e)": PUSHED BACK, with evidence.** Step (d)/(e) scope "consumers of its value" — of
`coefficient_ratio_differential_pvlas`. The `adopters.py` sites carry the **v1** magnitude
$7.5/\alpha^3\approx1.93\times10^7$, which is the return of the *already-deprecated*
`coefficient_ratio_differential()` — a different quantity, one re-freeze further back. Editing
them under a D7 re-point would be **re-freezing v1→v3 in a file D7 never names, silently skipping
the v2 rung**, and would put this lane's hands on the same surface the D1 lane deliberately
routed rather than fixed. **Flagged, not taken.** They are a genuine open surface; they are a
*separate ruling's* surface.

**★ Claim (c) — the site inventory: reproduces in substance, diverges in count. My own
re-derivation, pattern set `7\.5|1\.93e7|:328|:320|1e6`, `Prereg` block content-located at
`:179–:201` (`frozen=True` at `:181`):**

| Line | Content | Frozen? |
|---|---|---|
| :13 | module docstring *"MATCHED par-perp DIFFERENTIAL ratio 7.5/alpha^3 ~ 1.93e7"* | no |
| :14 | *"= coefficient_ratio(7/45), **birefringence.py:320**"* — **a SECOND stale cite, distinct from :328** (`coefficient_ratio` is content-located at `:356`) | no |
| :18 | *"the 7.5-trace a94672de"* | no |
| :86-87 | `birefringence_bench_spec` docstring *"= 7.5 / alpha^3 ~ 1.93e7"* | no |
| :138-139 | ledger row *"7.5/alpha^3 ~ 1.93e7 is a symmetric alpha-ECHO"* | no |
| :152 | axis `name="par-perp coefficient ratio (7.5/alpha^3)"` | no |
| **:180** | `ref="…(+ 7.5-trace a94672de)"` | **YES — inside `Prereg(` at :179** |
| :185 | `"birefringence.py:328 coefficient_ratio_differential"` (content-located at `:375`) | **YES** |
| :191 | POSITIVE bin *"ratio ~1.93e7, field-independent"* | **YES** |
| :203 | `gating_axis="par-perp coefficient ratio (7.5/alpha^3)"` | no |
| :214 | `verdict_fn=lambda r: r > 1e6` | no |
| :219 | *"the 7.5/alpha^3 ratio is a quantitative claim"* | no |
| :221-222 | `analytic_provenance="…(birefringence.py:328)"` — the second `:328` | no |

**Divergences from the supplement, both surfaced not silently absorbed:** (1) the frozen count is
**3, not 2** — `:180` sits between `Prereg(` at `:179` and `frozen=True` at `:181`, so it is
inside the frozen block by construction and must be disclose-only along with `:185`/`:191`;
(2) there is a **third** stale cite, `birefringence.py:320` at `:14`, pointing at
`coefficient_ratio` (actually `:356`) — the supplement named only the two `:328` instances. Row
count depends entirely on the pattern set, so "eight" and "thirteen" are not in conflict; the
*frozen/non-frozen boundary* is the part that matters and it moves by one.

## 3. GATE 2 — the letter check

### 3.1 GATE-2 VERDICT: **FIRES.** The letter rides v2 — but in the *opposite direction* the gate anticipated.

The gate's stop condition is *"IF the letter rides v2 anywhere."* It does, at two live
`provenance.md` sites. **But the letter's body and its authoritative public registration are
already on v3, and it is the CODE that is behind.** The gate is protecting the right surface for
a reason nobody wrote down: re-pointing the arbiter would *silently change what a
submission-gated artifact's traceability row resolves to*, without touching that row.

| Surface | Footing | Class | Verdict |
|---|---|---|---|
| `main.tex`:81-82, :275, :291, :750, :756, :794, :1083, :1136 | **v3** $3.75\pi/\alpha^2\simeq2.2\times10^5$ | live headline | ✅ already v3 |
| `main.tex`:294, :759 | v2 $7.5\pi/\alpha^2$ | **intentional convention history** — `:759` reads *"(A prior draft quoted $7.5\pi/\alpha^2\simeq\num{4.4e5}$, which paired the instantaneous model kernel against the cycle-averaged one-loop coefficient — a mixed footing…)"*; `provenance.md`:322-323 records these two as deliberately RETAINED | ✅ correct as written |
| `claim-prereg-ots/claims_by_hash.md`:12 (`42c760c1`, V4), :15 (`9988dc39`, V5), :18 (`e3071e70`, V6) | **v3** | **OTS-anchored, current** — V6 verbatim: *"coefficient ratio 3.75\*pi/alpha^2 ~ 2.2e5 to the instantaneous Euler-Heisenberg coefficient"* | ✅ already v3 |
| `claim-prereg-ots/claims_by_hash.md`:9 (`f34e7559`, V1) | v2 | **OTS-anchored, superseded** — V4 explicitly *"Supersedes the 2026-07-04 registration (f34e755998a9)"* | ⛔ never edit (frozen public artifact) |
| `provenance.md`:89, :243, :307, :405 | v2 | dated `REVISION-2` banner + two *"ANCHORED v1 … preserved verbatim"* blocks + the §10 KB-seam narration | ⛔ never edit (Rule-12 preserved) |
| **`provenance.md`:121** | **v2** | **★ LIVE traceability row, §1 "Number-by-number map (paper claim -> source)"** | 🔴 **STALE — the trigger** |
| **`provenance.md`:168** | **v2** | **★ LIVE §4 discipline-tags line** | 🔴 **STALE** |
| `make paper` build | — | `latexmk -pdf` only (`Makefile`:269-272); no Python, no driver, no `ave` import | ✅ build does not consume the function |
| `figures/exposure_plane.{pdf,png}` | — | committed artifacts; generator `birefringence_prior_art_exposure_scan.py` **is** a call site (#5) but the ratio is record-only, not plotted (`vacuum-birefringence-e4.md`:160: *"This render does **NOT** restate the matched-differential COEFFICIENT ratio"*) | ✅ figure unaffected |

### 3.2 The two stale rows, verbatim

`papers/2026_birefringence_letter/provenance.md`:121 —

> `| Eq.(9), abstract, §III.B **(REV-2)** | Ratio `7.5pi/alpha^2 ~ 4.42e5` (propagating; `15pi/α²~8.85e5` static) | `ave.bench.coefficient_ratio_differential_pvlas(geometry="propagating")`; live `4.4247e5`. Was `7.5/α³~1.93e7`. |`

`papers/2026_birefringence_letter/provenance.md`:168 —

> `headline the `4.42e5` magnitude (REV-2; was `1.93e7`) as emergence; it ledgers`

**★ Row `:121` is already self-contradicting at head, independently of anything this lane does.**
It asserts the paper's **Eq.(9)** is $7.5\pi/\alpha^2\approx4.42\times10^5$. `main.tex`:750
(the equation body; `\label{eq:ratio}` on the following line, `:751`) reads:

> `  =\frac{15\pi}{4\alpha^2}=\frac{3.75\pi}{\alpha^2}\simeq\num{2.2e5}.`

Eq.(9) is v3. The traceability row says v2. Both files are at `origin/main` `19285c5d`; both were
last touched by the same commit `5109c961`. The row was never carried through the §9 Arm-2
re-freeze — `provenance.md`:319 records the re-freeze sweep as covering *"abstract, §II.B
honesty-item (iv), Eq.9 + surrounding text, §III conclusion, Table I caption"*, i.e. **`main.tex`
sites only**. The §1 map, a `provenance.md` site, was outside that sweep's scope and stayed at
REV-2. **This is a pre-existing corpus defect, surfaced not created.**

### 3.3 Why the gate is right to stop this lane

The re-point would make `:121`'s cited call return `2.212333e+05`. That **repairs** the
paper↔code link at Eq.(9) — the code would finally agree with the equation. But it
**simultaneously falsifies the row's own prose as written** (*"Ratio `7.5pi/alpha^2 ~ 4.42e5`
… live `4.4247e5`"`) and leaves `:168` quoting a magnitude no longer produced anywhere. So a
D7 re-point is **not** completable without editing
`papers/2026_birefringence_letter/provenance.md`.

Three reasons that edit is not this lane's to make:

1. **Scope.** The dispatch fences this lane to `src/ave/bench/` + consumers. `papers/` is not in it.
2. **Artifact class.** The Letter is submission-gated with a committed PDF and a live OTS chain;
   its provenance ledger is part of the artifact of record. Which rows are *history* and which are
   *live map* is a judgement the Letter's own revision protocol owns (`provenance.md`:307 — *"this
   v2 does NOT re-stamp"*), not an engine lane's.
3. **Flag-don't-fix.** Two merged corpus files disagree about what Eq.(9) is. Both paths and both
   verbatim strings are now on the record above. Neither was reframed to match the other.

**Consequence for D7 as written: the gate's stop condition is met, so the ruling's own
conditional withholds execution.** D7 said re-point *gated on the sweep coming back clean*; the
letter leg did not come back clean. Routing back, not proceeding, is executing D7 — not
declining it.

## 4. The three execution blockers

Gate 2 alone suffices to stop. Two further blockers surfaced during the sweep that would have
bitten *even if* the letter had come back clean, so both are routed with it. **BLOCKER-1 is the
one that changes what "re-point to v3" means.**

### ★ BLOCKER-1 — the function has no v3 branch, and adding one is a KEEP-BOTH design decision, not a scalar swap

D7's execute-step (a) reads *"compute `3.75*pi/ALPHA**2` or equivalent"*. That presumes the
arbiter's shape can carry v3. It cannot, as written. The function is
**denominator-parameterised**, not footing-parameterised
(`src/ave/bench/birefringence.py`:411-418):

```python
    ave_num = 0.5 * (E_CRIT / E_YIELD) ** 2  # = 1/(2 alpha)
    if geometry == "propagating":
        qed_coeff = ALPHA / (15.0 * np.pi)
    elif geometry == "static":
        qed_coeff = ALPHA / (30.0 * np.pi)
    else:
        raise ValueError(f"geometry must be 'propagating' or 'static', got {geometry!r}")
    return ave_num / qed_coeff
```

v3 requires the QED denominator $2\alpha/(15\pi)$ — the **instantaneous** one-loop coefficient.
**Neither existing branch is it**, and neither existing branch is *wrong*: per
`vacuum-birefringence-e4.md`:38-41 (the *"static-to-propagating decomposition"*) the chain is
$\alpha/(30\pi) \xrightarrow{\times4} 2\alpha/(15\pi) \xrightarrow{\times\frac12} \alpha/(15\pi)$
— static duality, head-on crossing geometry, carrier average. All three are legitimate QED
coefficients **in their own footing**; what v2 got wrong was the *pairing* (instantaneous AVE
numerator against a cycle-averaged QED denominator), not either coefficient.

⇒ The parameter is doing two jobs at once. `"propagating"` and `"static"` name **geometries**;
the v2→v3 step is a **temporal-footing** change orthogonal to geometry. Three admissible shapes,
none of which an implementer lane should pick unilaterally:

- **(A) Redefine `"propagating"` in place** to $2\alpha/(15\pi)$. Smallest diff; but it makes the
  keyword *lie* (the propagating one-loop headline in the literature **is** $\alpha/(15\pi)$), and
  it silently changes what every existing call site means. Fails the KEEP-BOTH pattern.
- **(B) Add a third keyword** (`"instantaneous"`) returning $15\pi/(4\alpha^2)$, make it the
  **default**, and leave `"propagating"`/`"static"` returning exactly what they return today with
  a mixed-footing warning in the docstring. Preserves both legacy axes; matches the standing
  KEEP-BOTH-discriminator practice (add an axis, don't redefine in place); costs a default flip
  that moves all five call sites' recorded value.
- **(C) Split the parameter in two** — `geometry ∈ {static, propagating}` × `footing ∈
  {instantaneous, cycle_averaged}` — which is the physically honest factorisation and makes the
  v2 mixed-footing state *unrepresentable*, but is the largest diff and changes the signature.

**Recommendation, stated as a recommendation and not a decision: (B).** It is the only one of the
three that leaves every existing call site's semantics intact while making v3 the thing the
arbiter returns by default, and it is the shape the corpus already uses when an audit finds an
inconsistency in a frozen axis. **Not taken here.** Note that (A) — the reading a fast pass at
D7's *"re-point"* wording most naturally supports — is the one shape that fails the corpus's own
pattern.

### BLOCKER-2 — three JSON keys NAME the value they carry

All three v9 drivers write the arbiter's return under the literal key
`matched_differential_ratio_7.5pi_over_alpha2_propagating`
(`birefringence_gap1_hibef_feasibility.py`:383, `birefringence_hibef_scenario_predictions.py`:138,
`birefringence_prior_art_exposure_scan.py`:361), plus
`matched_differential_ratio_15pi_over_alpha2_static` at `birefringence_gap1_hibef_feasibility.py`:384
and `birefringence_hibef_scenario_predictions.py`:139. A re-point without a
key rename produces a **self-contradicting record** — a key that says `7.5pi` over a value that is
`3.75pi`. A re-point *with* a key rename changes the **output schema** of three drivers whose
committed JSON is cited by the Letter's provenance ledger as the source of Table I
(`provenance.md`:102-106, *"Drivers (re-run this session, all reconcile):"*, which lists all three
by path).

Committed values that would move on re-run:

```
src/scripts/vol_9_device/_output/birefringence_gap1_hibef_feasibility.json      442466.5835078048
src/scripts/vol_9_device/_output/birefringence_hibef_scenario_predictions.json  442466.5835078048
src/scripts/vol_9_device/_output/birefringence_prior_art_exposure_scan.json     442466.5835078048
```

Neither the key rename nor the JSON regeneration is authorized by D7's execute list, and both
touch letter-cited artifacts — i.e. BLOCKER-2 folds into the same Gate-2 routing.

### BLOCKER-3 — the manuscript/KB side is still on v2 at a site D7 does not name

`manuscript/ave-kb/vol4/claim-quality.md`:455-466 carries a 🔴 header whose **corrected** value is
still v2 — verbatim: *"**Corrected matched-differential ratio: $\mathbf{7.5\pi/\alpha^2\approx4.42\times10^5}$**
(propagating/LoI-matched headline)"* — and names this exact function as the harness at `:464`.
The KB leaf that D7 treats as truth-source has been consolidated to v3 (`vacuum-birefringence-e4.md`
Option-B, `:51`); `claim-quality.md` has not. **Not edited** — KB is the auditor lane's, and
D7 fences this lane to `src/`. Surfaced so the re-point is not landed while the claim-quality
register still teaches v2 as *the correction*.

### 4.1 What a clean D7 execution would need, as a routing list

1. **Grant/orchestrator picks a shape** from BLOCKER-1 (A) / (B) / (C).
2. **A ruling on whether `papers/2026_birefringence_letter/provenance.md`:121 and :168 may be
   updated**, and by which lane. (The rows are stale *today*; the re-point makes them stale in a
   new way.)
3. **A ruling on the JSON key rename + driver-output regeneration** (BLOCKER-2), which is the same
   letter-artifact question in a different file.
4. **A routing for `claim-quality.md`:455-466** to the auditor lane (BLOCKER-3).
5. Only then: the `src/ave/bench/birefringence.py` edit, which is ~8 lines and the *easiest* part
   of D7 by a wide margin.

**Nothing in items 1-4 is an implementer call.** That asymmetry — a trivial code change fenced
behind four adjudications — is the honest summary of why this lane stopped.

## 5. Non-overlap + lane mechanics

### 5.1 Zero overlap with the three named concurrent branches — file sets diffed, not assumed

| Branch | File set vs `origin/main` | Overlap with this lane |
|---|---|---|
| `src/deprecate-superseded-birefringence-ratio` | `_orchestration/docket-entries/2026-08-01-d1-deprecate-ratio.md`, `src/ave/qed/__init__.py`, `src/ave/qed/birefringence.py`, `src/tests/test_grqed_stage2_qed_extension.py` | **none** |
| `docs/factor7-and-782-basis-notes` | `_orchestration/docket-entries/2026-08-01-factor7-and-782-basis.md`, `manuscript/ave-kb/vol1/…/domain-catalog.md`, `manuscript/ave-kb/vol3/…/stellar-regime-classification.md`, `manuscript/vol_1_foundations/chapters/07_regime_map.tex`, `manuscript/vol_3_macroscopic/chapters/07_stellar_interiors.tex`, `manuscript/vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex`, `research/2026-07-21_rve-aggregation-bench_result.md` | **none** |
| `docs/rulings-d2-d3-d4` | **no ref on `origin`** (`git rev-parse --verify origin/docs/rulings-d2-d3-d4` fails) — un-pushed or differently named | **cannot collide with an unpushed ref**; re-check at merge time |

This lane's file set is **two files**: `research/2026-08-01_pvlas-arbiter-v3-repoint_scoping.md`
and `_orchestration/docket-entries/2026-08-01-d7-repoint-pvlas.md`. The `src/ave/qed/*` fence in
the dispatch is honoured by construction — this lane touched no `.py` at all.

### 5.2 Lane mechanics

- Self-isolated throwaway worktree at `.claude/worktrees/repoint-pvlas-v3`, branched from
  **`origin/main` @ `19285c5d`** (the dispatch's `e6de554b` is 2 commits stale — §1 C3).
- Branch name `src/repoint-pvlas-v3` **retained as dispatched** even though the branch carries no
  `src/` change, so the orchestrator's tracking key does not move. Disclosed rather than
  unilaterally renamed.
- Skeleton-first, one section per commit (the incremental-write discipline).
- **Every `file:line` in this doc was re-read at ship time.** Six of this lane's own draft cites
  were wrong and were corrected before commit: the three dispatch cites in §1 (C1/C2/C3), the
  `claims_by_hash.md` V5/V6 line numbers (`:14`/`:16` → `:15`/`:18`), the KB decomposition-chain
  lines (`:46-50` → `:38-41`), and the provenance driver-list lines (`:98-101` → `:102-106`). Two
  further corrections came from re-deriving the supplement (§2.6): the `adopters.py` import list
  and the frozen-block boundary.
- A zsh glob false-negative was hit and disclosed (§2), per the standing
  grep-completeness lesson.

### 5.3 Discipline tags

- **consistency-vs-emergence:** *nothing newly asserted.* This lane derives no quantity and moves
  no claim. The v2/v3 numbers it prints are re-computations of already-adjudicated corpus values,
  banked as receipts (§1.1). Class of the underlying claim is unchanged: `clm-pp3qwf` remains
  CONSISTENCY-class with the magnitude an adjudicated $\alpha$-echo, the FORM the chord.
- **verify-before-cite:** fired; six corrections, itemised in §5.2.
- **flag-don't-fix:** three contradictions surfaced with both paths + verbatim strings, none
  resolved — `provenance.md`:121 vs `main.tex`:750 (§3.2); `claim-quality.md`:455-466 vs
  `vacuum-birefringence-e4.md` Option-B (§4 BLOCKER-3); the three JSON keys vs their own values
  (§4 BLOCKER-2).
- **honest closure (Rule 11):** no criterion was dropped to convert the gate's ❌ to ✅. The gate
  fired; the ruling's own conditional withheld execution; the branch is reported as gated, not as
  done.
- **KEEP-BOTH discriminator pattern:** invoked in BLOCKER-1 as the reason shape (A) is
  inadmissible and shape (B) is recommended — add an axis, don't redefine a frozen one in place.
- **substrate-native-check:** N/A — no solver, observer, eigsolver, or operator was scaffolded;
  the object is a closed-form ratio of two already-canonical coefficients.
- **phase-space-coordinate-check (A46):** N/A / PASS — the observable is a polarization-phase
  retardance ratio on both legs; no real-space-vs-phase-space mismatch is introduced or relied on.

### 5.4 Acceptance battery

| Check | Result |
|---|---|
| `make verify` | **exit 0** — *"[Verify] ALL PHYSICS PROTOCOLS PASSED."* |
| `verify-docket-keys` (standalone + inside `make verify`) | **85 entries / 83 unique / no new duplicate keys**; this lane's `### ENTRY 2026-08-01-d7-repoint-pvlas` header parses |
| pytest `test_ave_bench` + `test_bench_adopters` + `test_bench_model` + `test_birefringence_v3_chain` | **99 passed in 0.71s** (control — no `.py` modified) |
| pure-corpus grep, both new files | **zero hits** |
| `git diff --stat origin/main...HEAD -- src/ manuscript/ papers/` | **empty** |
| `ruff check src/ave/bench src/scripts/vol_9_device src/tests/test_birefringence_v3_chain.py` | **`Found 86 errors.` — PRE-EXISTING, see below** |

**★ Self-correction, verify-before-cite, on this lane's own output.** An earlier draft of the
battery asserted *"ruff check … All checks passed"*. **That was written before the command ran and
it is false.** The real result is `Found 86 errors.` Three honest findings follow, none of them a
regression:

1. **Pre-existing, proven by control.** The identical `Found 86 errors.` is produced from the
   **untouched main checkout at the same SHA `19285c5d`**, and this branch's
   `git diff --stat origin/main...HEAD -- src/` is empty. No `.py` byte changed on this branch.
2. **`ruff` is not a gate this repo enforces.** The Makefile has **no `lint:` target** and never
   invokes ruff; `make verify` does not call it. The dispatch's "ruff clean" acceptance line
   describes a gate that does not exist here — surfaced rather than quietly satisfied by scoping
   the invocation until it went green.
3. **Not fixed, deliberately.** Config is `select = ["E","F","W","I"]`, `line-length = 120`
   (`pyproject.toml`:37-42); `src/scripts/vol_9_device` carries a standing import-order/style
   backlog under it. Reformatting untouched driver bodies is unrequested scope and would put this
   lane's diff into `src/`, breaking its own fence.

### 5.5 Non-goals fenced

No re-point. No `src/` edit. No test re-pin. No JSON regeneration. No `papers/` edit. No KB or
manuscript edit. No frozen block touched. No id minted, no solidity moved, no claim-graph edge
added. No contradiction resolved. No shape picked for BLOCKER-1. No `src/ave/qed/*` file opened
for write. The v2-vs-v3 footing itself is **not** re-litigated here — KB is truth-source and the
factor 2 is adjudicated; only the *engine's* alignment to it is at issue, and that is what stays
open.
