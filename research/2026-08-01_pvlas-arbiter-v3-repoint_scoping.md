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

*(§2 lands next)*

## 3. GATE 2 — the letter check

*(§3 lands next)*

## 4. The three execution blockers

*(§4 lands next)*

## 5. Non-overlap + lane mechanics

*(§5 lands next)*
