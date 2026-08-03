# LINK-FORM ANCHOR DRIFT — the newly-visible finding set (2026-08-03)

**Class: triage artifact. NOT an adjudication, NOT a repair.** This document REPORTS the
cite class that `manuscript/ave-kb/tools/verify-anchor-content.py` became able to see when
`CITE_RE` was taught the markdown-link anchor form on branch `tools/cite-re-link-form`.
**Nothing listed here is fixed by that branch, on purpose** — repair is per-owner triage on
the owning lane, and a tooling branch that also rewrote 208 anchors across 5 volumes would
be unreviewable. Follow-on named in `_orchestration/docket-entries/2026-08-02-paperclip-canonization.md`
(the "Named follow-on, NOT repaired here" section).

> **★ Self-suppression note.** Every `path:NN` cite in this document sits inside a fenced
> block. `verify-anchor-content.strip_fenced` blanks fenced blocks before scanning, so this
> artifact does **not** inject 208 new findings into the very advisory count it reports. If
> you unfence a block to work a row, expect the count to move.

---

## 1. The defect this closes

`CITE_RE` required the `:NN` to follow the file extension **immediately**. A KB-house-style
anchor renders with a closing paren in between — the `)` broke the match, so the entire
markdown-link anchor class was never scanned. Three stale KB-leaf anchors shipped in the
#832 arc underneath a **measured** advisory delta of `0`, because the tool never looked at
them.

Before (pre-fix, at `origin/main` `2fcde4db`):

```
CITE_RE = re.compile(
    r"(?P<path>(?:[\w.+-]+/)*[\w.+-]+\.(?:" + "|".join(TARGET_EXTS) + r")):(?P<line>\d+)(?!\d)"
)
```

After:

```
_PATH_RE = r"(?:[\w.+-]+/)*[\w.+-]+\.(?:" + "|".join(TARGET_EXTS) + r")"

CITE_RE = re.compile(
    r"(?:(?<=\]\()(?P<lpath>" + _PATH_RE + r")\)|(?P<path>" + _PATH_RE + r"))"
    r":(?P<line>\d+)(?!\d)"
)
```

**Why a lookbehind and not a bare `\)?`.** Both were measured on this corpus and are
**empirically identical here** — `\)?` and the `](…)`-anchored branch each add exactly
**857** cites, and a scan for "closing paren but no `](` opener" returns **0** sites. The
lookbehind was chosen anyway because it is structurally exact: it cannot match a future
prose parenthetical such as `(as noted in foo.md):12`, which the loose form would swallow.
The `](` is **asserted, not consumed**, so `m.start()` still lands on the path — the column
`associate_quote` ranks quote-proximity against — and the two branches stay comparable.

---

## 2. Both runs, verbatim, same tree

Same worktree, same tree (`origin/main` @ `2fcde4db`), same arguments
(`--top 5000`, the docket-receipt argument set). Only the tool file differs.

**BEFORE (pre-fix `CITE_RE`):**

```
[anchor-content] WARN-CLASS advisory — quoted-excerpt vs cited line drift
  cites scanned .............. 13249
  checked & anchored (OK) .... 364
  DRIFT — excerpt moved ...... 190  (stale :NN, excerpt found elsewhere)
  DRIFT — excerpt absent ..... 822  (not in target; see FP classes)
  not-checked (no quote) ..... 6349
  not-checked (trivial quote)  176
  unresolved target .......... 5348  (verify-md-links territory)
  → checked cites: 1376; drift: 1012 (73.5% of checked)
```

**AFTER (link-form-aware `CITE_RE`):**

```
[anchor-content] WARN-CLASS advisory — quoted-excerpt vs cited line drift
  cites scanned .............. 14106
  checked & anchored (OK) .... 432
  DRIFT — excerpt moved ...... 244  (stale :NN, excerpt found elsewhere)
  DRIFT — excerpt absent ..... 976  (not in target; see FP classes)
  not-checked (no quote) ..... 6930
  not-checked (trivial quote)  178
  unresolved target .......... 5346  (verify-md-links territory)
  → checked cites: 1652; drift: 1220 (73.8% of checked)
```

**Totals: 1012 → 1220 findings. `+208`.**

> ⚑ **Baseline-number correction (surfaced, not reconciled away).** The #832 docket receipts
> record the pre-change baseline as **`1006`** findings / `1368` checked cites. At
> `origin/main` `2fcde4db` the same command returns **`1012`** / `1376`. The `+6` is corpus
> drift between that lane's tip and this one, **not** a discrepancy in either measurement —
> both are re-runnable. This lane's delta is computed `1012 → 1220` at ONE tree, so the
> `1006`-vs-`1012` difference does not enter it.

**Category accounting (integrity check).** The per-bucket deltas sum to exactly the
link-form cite count:

```
cites          +857   (= the link-form class, measured independently)
  checked_ok    +68
  moved         +54
  absent       +154
  noquote      +581
  trivial       +2
  unresolved     -2
  ------------------
  sum          +857   ✓
```

The `-2` on `unresolved` is a real second-order effect, not noise: `associate_quote` skips
an adjacent line that carries a cite of its own (so a sibling's quote is never stolen), and
link-form cites now count as cites for that test. Two bare-form cites consequently lost a
mis-associated quote and moved out of the `unresolved` bucket. **Finding-set diff: `208`
new, `0` removed** — purely additive at the findings level.

**Attribution.** Re-scanning while recording which `CITE_RE` branch matched returns
**208 link-branch findings**, exactly equalling the report delta. Every new finding is
link-form; no bare-form finding changed.

---

## 3. What the 208 actually are — read this before working any row

The newly-visible class carries the **same false-positive contamination as the pre-existing
set**, and the tool is WARN-CLASS for exactly that reason (its own docstring names the FP
classes). Classifying the associated excerpt:

| excerpt class | count | moved | absent | is it anchor signal? |
|---|---|---|---|---|
| `ID-TOKEN` (`clm-`/`def-`/`exp-`/`sup-`/`ilk-` id in backticks) | 62 | 30 | 32 | **No.** An id string appears wherever the id appears. Pure noise. |
| `SHORT` (< 12 chars, e.g. `main`, `#782`, `g = 2`) | 56 | 13 | 43 | **Mostly no** — the documented generic-short-string FP class. |
| `IDENT` (a bare path / identifier, e.g. `TETRA_OFFSETS`, `k4_tlm.py`) | 37 | 10 | 27 | **Mostly no** — a path in backticks is a reference, not target content. |
| `PROSE` (a real excerpt) | 53 | 1 | 52 | **Sometimes.** This is where the signal lives. |
| **total** | **208** | **54** | **154** | |

**Zero out-of-range anchors.** Every one of the 208 cites a line that exists in its target
(checked against each target's real line count), so none is an unambiguous hard error.

**A second, independent pass was run** to get past the backtick-association FP: instead of
the checker's nearest-backtick-span heuristic, extract the `*"…"*` prose quote written
immediately after each link-form cite and check *that*. It returns **65** findings,
**13 of them KB-leaf→KB-leaf `moved`** — the high-confidence real-drift set. Those 13 (minus
one that the second pass itself mis-associated, see below) are the rows worth an owner's time.

> ⚑ **The second method has the same FP mode, demonstrated.** `double-slit-ee-mapping.md:60`
> reads (fenced):
> ```
> [ohmic-decoherence-born.md](ohmic-decoherence-born.md):40 (7-step chain opens), :55 ("No Born rule input anywhere in the chain"), 36–61
> ```
> The quote belongs to the bare `:55` fragment, **not** to the `:40` cite — and `:55` is
> **correct**. Reported here as a caught-and-discarded candidate rather than dropped
> silently: a multi-cite line defeats *any* nearest-quote heuristic, method-1 or method-2.

---

## 4. Hand-verified real drift (each re-grepped on this branch)

Seven rows verified by printing the cited line AND grepping the target for the excerpt.
**None is repaired here.** Listed with the owning area so triage can route.

```
★1  manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:79
      cites  common/translation-tables/translation-circuit.md:178
      quote  "the bond's incident/reflected voltage waves ARE the photon's own quadrature: ..."
      truth  that text is at :190      (:178 = the Operator-citation-provenance blockquote)
      also   the companion ":238" fragment on the same line resolves to :255
      ★ WHY THIS ONE IS FIRST: the citing line is labelled  **Anchors (verbatim, ✓-VERIFIED):**
        A self-certified anchor, stale, in the class the checker could not see.

★2  manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:92
      cites  common/translation-tables/translation-circuit.md:637
      quote  "$g = 2$ is POSITED, not derived"
      truth  that text is at :767      (:637 = the input-noise-voltage row)
      note   load-bearing epistemic caveat (g=2 imported, not axiom-derived); +130 lines of drift

★3  manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:96
      cites  common/translation-tables/translation-circuit.md:235
      quote  "the substrate does NOT independently select R·r=1/4"
      truth  that text is at :252      (:235 is a BLANK line)
      note   the Class-B / honest-α adjudication anchor (clm-0ktpcn)

★4  manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:88
      cites  common/translation-tables/translation-circuit.md:237–239
      quote  "The load-bearing disambiguation (gate (a)'s headline clarity)"
      truth  that text is at :254      (:237 is a BLANK line)

★5  manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md:105
      cites  common/translation-tables/translation-circuit.md:207
      quote  "GAP — not mapped"   (Autoresonance row)
      truth  that row is at :224

 6  ⚠ REPAIR-SAFETY ROW — LINE GRANULARITY IS NOT ENOUGH HERE.
    Two citing lines each carry THREE `master-equation.md):20` cites, and the three
    do NOT share a truth value. Repair per OCCURRENCE (column), never per line.

    manuscript/ave-kb/common/trampoline-framework.md:681        (one 2696-char line)
      col  799   "A1 dilatation-MASS"                     :20 CORRECT — leave alone
      col 1444   "TWO DISTINCT CLOCKS"                    stale → :38
      col 2264   no quoted excerpt; prose reads
                 "…the REFUTED flag at [`master-equation.md`](…):20."   stale → :36

    manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md:221   (one 2084-char
    line; same three banners, mirrored — the 2nd and 3rd swap order)
      col 1067   "TWO DISTINCT CLOCKS"                    stale → :38
      col 1304   "A1 dilatation-MASS"                     :20 CORRECT — leave alone
      col 2012   no quoted excerpt; prose reads
                 "…REFUTED flag at [`master-equation.md`](…):20."      stale → :36

    Columns are 0-based at the START OF THE PATH inside `](…)` — i.e. exactly what
    CITE_RE's match .start() reports — so each occurrence is re-locatable directly.

    Target truths, each re-grepped on this branch (master-equation.md, 117 lines):
      "A1 dilatation-MASS"    → :20 and nowhere else  (:20 = the TWO-"3"s block)
      "TWO DISTINCT CLOCKS"   → :38 and nowhere else  (:20 says TWO DISTINCT
                                *objects*, a different phrase in the same banner)
      the REFUTED banner      → :36   (":33 mentions "see the REFUTED-flag below"
                                but is a pointer, not the flag)

    ⚠ DO NOT blanket-repoint either line. Two of these six `:20` occurrences are
      CORRECT; a line-granular sed/repoint would break working anchors while fixing
      the stale ones. The `:36` target was UNNAMED in the first pass of this doc,
      which reported the pair as a single ":20 → TWO DISTINCT CLOCKS" row: it is in
      fact THREE distinct targets per line — :20 correct, :38 stale, :36 stale.

      checker note: all six occurrences associate the same backtick span
      `clm-533gvm` and report moved→:36. That is the right line for the two
      REFUTED-flag occurrences and the wrong line for the other four — right
      answer, wrong reason, the same failure shape as row 7 below.

 7  manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-transfer-function.md:41
      cites  theorem-3-1-q-factor.md:81
      quote  "only a fraction $1/Q=\alpha$ of the stored energy leaks per cycle"
      truth  that text is at :85       (off-by-4)
      note   the checker flagged this row via a MIS-ASSOCIATED backtick span
             (`pole_real/ω₀ = −0.00364868 = −α/2`), i.e. right answer, wrong reason.
             The drift is real; the checker's stated cause for it is not.
```

**Mechanism, not a coincidence — TWO insertion events, not one uniform shift.** Six anchors
in the rows above point into `common/translation-tables/translation-circuit.md`, and their
staleness is a **step function of depth in that file**, not a constant:

| row | anchor | content is now at | Δ |
|---|---|---|---|
| ★1 | `:178` | `:190` | **`+12`** |
| ★5 | `:207` | `:224` | `+17` |
| ★3 | `:235` | `:252` | `+17` |
| ★4 | `:237` | `:254` | `+17` |
| ★1's companion `:238` (a bare fragment on ★1's line — no path, so neither regex branch sees it) | `:238` | `:255` | `+17` |
| ★2 | `:637` | `:767` | `+130` |

Read as insertion **zones**: `+12` above old-`:178`; **a further `+5`** between old-`:178`
and old-`:207` (so everything from `:207` down is `+17`); and a further `+113` between
old-`:238` and old-`:637`. **★1 is `+12`, not `+17`, because its target sits ABOVE the
second insertion point.** The earlier wording here — "all stale by a uniform `+17` (`+12`
for ★1)" — was self-contradictory on precisely the sharpest row, and is corrected.

**The two-event reading is STRONGER evidence for the mechanism, not weaker.** One insertion
shifting one anchor set is a single bad merge. What the history actually shows is a hub that
kept absorbing insertions at *different depths* while its inbound anchors sat still:
`git log --follow` on the leaf puts the `+12` across **six** commits and the extra `+5`
across **four**, all between 2026-07-09 and 2026-07-28, with every one of these anchors
CORRECT when written and correct continuously from 2026-06-11 to 2026-07-09. Nineteen days
of continuous rot in a live hub, with nothing in the corpus flagging any of it, is a worse
failure mode than one event — and it is the mode a line-anchor checker exists to catch.

**How much of the 208 is this hub? `13` — measured, `6.2%`.** Not "a large share", and not
even the largest: `master-equation.md` takes **`26`**, `theorem-3-1-q-factor.md` `8`,
`physics-lineage-map.md` `7`. The hub does carry **`50` inbound link-form cites** across
`22` distinct anchor values (`:178` ×6, `:207` ×6, `:35` ×6, `:637` ×5, `:245` ×3, …), but
their disposition is `34` no-quote / `3` OK / `8` moved / `5` absent — so only `13` can
surface as findings at all. **The finding count measures CHECKABILITY, not staleness:** the
`34` no-quote cites into this leaf are unexamined, not verified-correct, and `3` is the
number affirmatively confirmed good.

**Not adjudicated here:** whether the correct repair is re-pointing each `:NN`, converting
these to anchor-slug links, or retiring line anchors into `path-stable` frontmatter for
high-churn hub leaves. That is an owner/Grant decision, not a tooling-lane one.

---

## 5. Full delta list — all 208 newly-visible findings

Format per row: citing `:line` · classifier verdict · excerpt class · cited target ·
where the excerpt actually is (moved rows only) · the resolved target path · the excerpt the
checker associated · **the actual content at the cited line**. Grouped by citing file.
Fenced (see the self-suppression note).

```
### _orchestration/2026-06-15_ceff-epsilon-monotonicity.md   [12 finding(s)]
    1. :64    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:21
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md
        excerpt  : C_eff = C_0/√(1−(V/V_yield)²)
        at-line  : <blank line>
    2. :64    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:32
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md
        excerpt  : C_eff = C_0/√(1−(V/V_yield)²)
        at-line  : \lim_{\Delta\phi \to \alpha} C_{eff}(\Delta\phi) = \lim_{\Delta\phi \to \alpha} \frac{C_{0}}{\sqrt{1-\left(\frac{\Delta\phi}{\alpha}\right)^{2}}} = \i
    3. :64    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md:27
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/dielectric-plateau-prediction.md
        excerpt  : Q=C0·V/√…
        at-line  : C_{diel}(E) = C_0 \cdot \sqrt{1 - \left(\frac{E}{E_{yield}}\right)^2} \;\to\; 0
    4. :64    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/ee-bench-plateau.md:18
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/ee-bench-plateau.md
        excerpt  : Q=C0·V/√…
        at-line  : As $E \to E_{yield}$: $\varepsilon_{eff} = \varepsilon_0 S \to 0$, and the **across-gap** capacitance an LCR meter reads **rolls off** with it — the l
    5. :64    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/simulation/ch18-universal-vacuum-cell/spice-subcircuit.md:26
        resolved : manuscript/ave-kb/vol4/simulation/ch18-universal-vacuum-cell/spice-subcircuit.md
        excerpt  : Q=C0·V/√…
        at-line  : > numpy MNA == graph-Laplacian (4.17e-10 V); rung-4 the 1D LC-chain band `ω(k)=2ω₀|sin(ka/2)|`
    6. :65    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/simulation/ch15-autoresonant-breakdown/index.md:17
        resolved : manuscript/ave-kb/vol4/simulation/ch15-autoresonant-breakdown/index.md
        excerpt  : Q = C_0√(…)·V
        at-line  : | Nonlinear detuning | $C_{eff}(V) = C_0\sqrt{1 - (V/V_{yield})^2}$; fixed-frequency drive falls out of phase as $C_{eff}$ drops | theory |
    7. :65    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/ee-bench-netlist.md:15
        resolved : manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/ee-bench-netlist.md
        excerpt  : C_eff = C_0·√(1−(V/V_yield)²)
        at-line  : C_{eff}(V) = C_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
    8. :65    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/index.md:19
        resolved : manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/index.md
        excerpt  : Q = C_0√(…)·V
        at-line  : | EE Bench capacitance rolloff | $C_{eff}(V) = C_0\sqrt{1 - (V/V_{yield})^2}$; anomaly window at $\sim 0.85 \times V_{yield}$ to $V_{yield}$; deviatio
    9. :65    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/simulation/index.md:24
        resolved : manuscript/ave-kb/vol4/simulation/index.md
        excerpt  : Q = C_0√(…)·V
        at-line  : | EE Bench yield plateau | Behavioral capacitor $Q = C_0\sqrt{1-(V/V_{yield})^2} \cdot V$ swept DC to $45\,\text{kV}$; $C_{eff}/C_0$ deviates $>10\%$ 
   10. :88    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:12
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md
        excerpt  : C_eff
        at-line  : By applying the Topo-Kinematic mapping to the electron's rest mass, its equivalent localized Inductance evaluates to $L_e \equiv \xi_{topo}^{-2} m_e$.
   11. :92    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:14
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md
        excerpt  : C_eff=C_0/S
        at-line  : > **Sector note (Q1 = (B), Grant-ratified 2026-06-15; `research/2026-06-15_ceff-epsilon-monotonicity_result.md`).** The diverging $C_0/S$ below is the
   12. :96    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md:89
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md
        excerpt  : C=ξ²/k
        at-line  : where $\kappa = x/F = 1/k$ is the mechanical compliance (inverse spring constant). Dielectric breakdown occurs when the lattice displacement exceeds i

### _orchestration/docket-entries/2026-07-22-saturation-rim-inversion-correction.md   [1 finding(s)]
   13. :3     [absent       ] [SHORT   ] -> 2026-07-21-saturation-rim-inversion.md:13
        resolved : _orchestration/docket-entries/2026-07-21-saturation-rim-inversion.md
        excerpt  : -correction
        at-line  : **Post-review repair (2026-07-21, PR #790 adversarial review):** the quantization-locus claim (`clm-riminv`) is carved **existence → PROTECTION** (the

### _orchestration/docket-entries/2026-08-02-rulings-d2-d3-d4-correction.md   [2 finding(s)]
   14. :3     [absent       ] [SHORT   ] -> 2026-08-01-rulings-d2-d3-d4.md:34
        resolved : _orchestration/docket-entries/2026-08-01-rulings-d2-d3-d4.md
        excerpt  : -correction
        at-line  : - **Banner (immediately after the table), four parts.** **(i) Spin scope, Ruling B1:** the BH-ringdown fire's flat `Q = ℓ` is the **cold `a* = 0` anch
   15. :13    [absent       ] [ID-TOKEN] -> ../../manuscript/ave-kb/common/physics-lineage-map.md:92
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : def-quant3
        at-line  : - **AVE position: CLASHES — integers = topology (winding).** Charge = Link ∈ ℤ is FORM-derived from Axiom 2 TKI (`vol2/particle-physics/ch01-topologic

### manuscript/ave-kb/common/ave-analytical-toolkit-index.md   [1 finding(s)]
   16. :181   [moved        ] [SHORT   ] -> boundary-observables-m-q-j.md:87  excerpt-actually-at [106]
        resolved : manuscript/ave-kb/common/boundary-observables-m-q-j.md
        excerpt  : b72045d4
        at-line  : For any localized region $\Omega$ in the substrate:

### manuscript/ave-kb/common/claim-quality.md   [1 finding(s)]
   17. :723   [moved        ] [IDENT   ] -> ./boundary-observables-m-q-j.md:91  excerpt-actually-at [104]
        resolved : manuscript/ave-kb/common/boundary-observables-m-q-j.md
        excerpt  : TETRA_OFFSETS
        at-line  : 3. **Compare against measured observables** (mass, charge, spin or angular momentum in the appropriate projection).

### manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md   [11 finding(s)]
   18. :13    [absent       ] [PROSE   ] -> ../../../src/ave/core/constants.py:770
        resolved : src/ave/core/constants.py
        excerpt  : V_TOROIDAL_HALO = 2
        at-line  : # the "(Effective Medium Theory)" attribution is doubly-superseded — K=2G is GR-IMPORTED
   19. :13    [absent       ] [PROSE   ] -> translation-tables/translation-circuit.md:35
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : x = I_scalar/(1 − V·p_c) + 1
        at-line  : The substrate IS an LC network. Axiom 1 (INVARIANT-S2) states verbatim: *"intrinsic LC oscillators at each node ... modeled in continuum as a Trace-Re
   20. :27    [absent       ] [SHORT   ] -> ../../../src/ave/core/constants.py:382
        resolved : src/ave/core/constants.py
        excerpt  : √α·V_snap
        at-line  : # --- Fundamental dimensionless constants (same in any unit system) ---
   21. :28    [absent       ] [SHORT   ] -> ../../../src/ave/core/constants.py:373
        resolved : src/ave/core/constants.py
        excerpt  : m_e c²/e
        at-line  : # Energy unit = M_0 · C_0² = m_e c² ≈ 511.0 keV
   22. :32    [absent       ] [SHORT   ] -> ../../../src/ave/core/constants.py:770
        resolved : src/ave/core/constants.py
        excerpt  : V_halo
        at-line  : # the "(Effective Medium Theory)" attribution is doubly-superseded — K=2G is GR-IMPORTED
   23. :221   [moved        ] [ID-TOKEN] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
   24. :221   [moved        ] [ID-TOKEN] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
   25. :221   [moved        ] [ID-TOKEN] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
   26. :221   [absent       ] [ID-TOKEN] -> ../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md:52
        resolved : manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md
        excerpt  : clm-533gvm
        at-line  : ### Field-Oriented Control (FOC) and the Secondary Density Wake
   27. :221   [absent       ] [ID-TOKEN] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md:11
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md
        excerpt  : clm-533gvm
        at-line  : **A-010 canonical.** Op14's dynamic impedance $Z_{\text{eff}}(r) = Z_0 / \sqrt{S(r)}$ doesn't just modulate impedance — it **modulates the local clock
   28. :247   [absent       ] [PROSE   ] -> ../../../src/ave/core/constants.py:770
        resolved : src/ave/core/constants.py
        excerpt  : V_TOROIDAL_HALO = 2.0
        at-line  : # the "(Effective Medium Theory)" attribution is doubly-superseded — K=2G is GR-IMPORTED

### manuscript/ave-kb/common/electron-plumbing-primer.md   [1 finding(s)]
   29. :84    [absent       ] [PROSE   ] -> ../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md:41
        resolved : manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md
        excerpt  : vol4/…/ch14-leaky-cavity-particle-decay/theory.md
        at-line  : In the AVE framework, an electron is the $0_1$ unknot in real space carrying a $(2,3)$ Clifford-torus winding pattern in phase space (see [Vol 1 Ch 8 

### manuscript/ave-kb/common/envelope-anatomy.md   [1 finding(s)]
   30. :40    [absent       ] [PROSE   ] -> ../../../src/ave/core/chiral_lattice_v10.py:29
        resolved : src/ave/core/chiral_lattice_v10.py
        excerpt  : A_YIELD_SQ = 2·α
        at-line  : # Yield surface: A_yield = sqrt(2α) ⇒ A²_yield = 2α (three-regime knee).

### manuscript/ave-kb/common/genesis-chord-falsification-ledger.md   [1 finding(s)]
   31. :55    [absent       ] [SHORT   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : k·R=3
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/common/physics-lineage-map.md   [5 finding(s)]
   32. :225   [absent       ] [PROSE   ] -> the-abandoned-interior.md:24
        resolved : manuscript/ave-kb/common/the-abandoned-interior.md
        excerpt  : manuscript/bibliography.bib:239-247
        at-line  : **Deletion 2 — THE INTERIOR (the ontology).** Kelvin's 1867 *On Vortex Atoms* sought the **constitution** of matter — atoms as knotted vortex tubes in
   33. :394   [absent       ] [IDENT   ] -> axiom-register.md:230
        resolved : manuscript/ave-kb/common/axiom-register.md
        excerpt  : vol3/condensed-matter/ch09-condensed-matter-superconductivity/
        at-line  : | **2** | $[Q]\equiv[L]/\xi_{topo}$ — charge = Burgers-vector dislocation ($\xi_{topo}\equiv e/\ell_{node}$) | HOW windings interact (coupling class);
   34. :394   [absent       ] [IDENT   ] -> interlock-register.md:249
        resolved : manuscript/ave-kb/common/interlock-register.md
        excerpt  : vol3/condensed-matter/ch09-condensed-matter-superconductivity/
        at-line  : - **failure_causation (criterion 4):** **CULPABLE-episode → SCRUBBED → INNOCENT-when-α-free.** The baked `Q_TANK = 1/α` in `cvr_model.py` was CULPABLE
   35. :394   [moved        ] [IDENT   ] -> translation-tables/translation-circuit.md:147  excerpt-actually-at [223, 669]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : vol3/condensed-matter/ch09-condensed-matter-superconductivity/
        at-line  : | **Double-slit: which-path detector / observer** | **resistive load $Z_{det}$** (Joule sink); $W_{extracted}\propto\lvert\partial_t\mathbf{A}\rvert^2
   36. :475   [absent       ] [PROSE   ] -> claim-quality.md:1318
        resolved : manuscript/ave-kb/common/claim-quality.md
        excerpt  : research/2026-07-08_p6-*
        at-line  : re-analysis of Planck PR3 SMICA CMB data for the cosmic-axis alignment, returning

### manuscript/ave-kb/common/port-register.md   [7 finding(s)]
   37. :28    [absent       ] [SHORT   ] -> substrate-native-terminology.md:47
        resolved : manuscript/ave-kb/common/substrate-native-terminology.md
        excerpt  : [canon]
        at-line  : | **thixotropic / liquefy / melt** | thixotropic sub-yield re-freeze is *reversible* softening ($S\downarrow$) — fine as such | **melt / liquefy** nam
   38. :37    [absent       ] [SHORT   ] -> ../vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md:10
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md
        excerpt  : [canon]
        at-line  : The three-impedance law (field-symbol registry §3.11; vocab-operator-unification audit §4a) assigns every reflection statement a **channel subscript**
   39. :43    [absent       ] [SHORT   ] -> ../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md:120
        resolved : manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md
        excerpt  : [canon]
        at-line  : | Claim | Sector | Mode | Modulus | Speed | Source operator / origin |
   40. :48    [absent       ] [SHORT   ] -> ../vol3/gravity/ch02-general-relativity/einstein-field-equation.md:62
        resolved : manuscript/ave-kb/vol3/gravity/ch02-general-relativity/einstein-field-equation.md
        excerpt  : [canon]
        at-line  : > 0$ (and $Z_{bulk} \to 0$) — an Op3 short giving $\Gamma_{shear} =
   41. :49    [absent       ] [SHORT   ] -> ../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md:13
        resolved : manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md
        excerpt  : [canon]
        at-line  : ## Key Results
   42. :50    [moved        ] [ID-TOKEN] -> ../vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md:59  excerpt-actually-at [5, 100, 124, 128, 130]
        resolved : manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md
        excerpt  : clm-kmliqx
        at-line  : $$\omega^2 = c^2 k^2 + \frac{4 G_c}{I_\omega}$$
   43. :50    [absent       ] [SHORT   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:24
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : [canon]
        at-line  : > **↗ Rotation-flavor tag (2026-07-03, KEEP-BOTH — §8 rotation un-conflation, `research/2026-07-03_em-readout-vsector-stage1_prereg.md` §8; additive, 

### manuscript/ave-kb/common/the-abandoned-interior.md   [5 finding(s)]
   44. :127   [moved        ] [SHORT   ] -> translation-tables/translation-circuit.md:637  excerpt-actually-at [767]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : g = 2
        at-line  : | Input noise voltage / current (1/f + thermal) | Substrate low-frequency-mode population (microrotational dispersion for 1/f) + Johnson-Nyquist subst
   45. :178   [absent       ] [SHORT   ] -> ../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:187
        resolved : manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md
        excerpt  : k = mₑv/ℏ
        at-line  : $$
   46. :183   [absent       ] [PROSE   ] -> ../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:153
        resolved : manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md
        excerpt  : ℓ_node = ℏ/mₑc
        at-line  : $$
   47. :183   [absent       ] [PROSE   ] -> ../vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:60
        resolved : manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md
        excerpt  : ℓ_node ≈ 386 fm
        at-line  : **AVE's lattice cutoff $\ell_{\text{node}}$** ($\approx 386$ fm vs Planck $\sim 10^{-35}$ m) eliminates 22 orders of magnitude of modes. The remaining
   48. :206   [absent       ] [PROSE   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md:22
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md
        excerpt  : gh pr view 166 → MERGED
        at-line  : | **Optical-scale anisotropy** | $\delta_{aniso} \sim (q\ell_{node})^4 \approx 2.2 \times 10^{-22}$ at $\lambda = 633$ nm; current cavity bounds $\sim

### manuscript/ave-kb/common/theorem-thesaurus.md   [39 finding(s)]
   49. :65    [absent       ] [SHORT   ] -> historical-precedents.md:10
        resolved : manuscript/ave-kb/common/historical-precedents.md
        excerpt  : def-
        at-line  : AVE re-ties **two threads from 19th-century physics, both shelved by ~1900** — Maxwell's quaternion / longitudinal electromagnetism, and Kelvin's vort
   50. :113   [moved        ] [SHORT   ] -> claim-quality.md:1345  excerpt-actually-at [1530, 1541]
        resolved : manuscript/ave-kb/common/claim-quality.md
        excerpt  : #782
        at-line  : - **Lock 3 — [NO-FLUX-STRUCTURAL] maximum principle (THEOREM class; ε > 0).** For the source-free variable-coefficient problem `L_w φ = 0`, `L_w = Bᵀ 
   51. :122   [absent       ] [SHORT   ] -> electron-plumbing-primer.md:159
        resolved : manuscript/ave-kb/common/electron-plumbing-primer.md
        excerpt  : t = Σ·n
        at-line  : The deep point: **nothing chooses the path.** Each electron only feels its local downhill; the field arranges itself (surface charges) so the *global*
   52. :134   [absent       ] [PROSE   ] -> physics-lineage-map.md:359
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : absolute_theorem_grade_ordering_holds_everywhere = True
        at-line  : **Capsule.** A General Electric engineer spent three decades on one move: any linear physical system — rotating machine, elastic solid, Maxwell field,
   53. :135   [absent       ] [PROSE   ] -> claim-quality.md:1541
        resolved : manuscript/ave-kb/common/claim-quality.md
        excerpt  : G_Voigt, G_Reuss, G_Hill
        at-line  : - **Does NOT re-open the #782 verdict.** BIN-4 is invariant across `β`; the banked bare-node `r_Z` values are **neither a floor nor a ceiling** of the
   54. :135   [absent       ] [PROSE   ] -> relative-offset-principle.md:57
        resolved : manuscript/ave-kb/common/relative-offset-principle.md
        excerpt  : G_Voigt, G_Reuss, G_Hill
        at-line  : - **Fork-ρ source + the `r_Z`-band consequence (flag).** The `#782` RVE bench ([`research/2026-07-21_rve-aggregation-bench_result.md`](../../../resear
   55. :144   [absent       ] [PROSE   ] -> ../vol4/future-geometries/ch13-future-geometries/cem-methods-survey.md:102
        resolved : manuscript/ave-kb/vol4/future-geometries/ch13-future-geometries/cem-methods-survey.md
        excerpt  : Gamma_cauchy = M_tt - M_tr M_rr^{-1} M_rt
        at-line  : <!-- claim-quality: clm-hd9bee (this paragraph identifies the "K4-graph TLM correction" — the K4-TLM Diamond Lattice unitary 4-port simulator with $\m
   56. :144   [absent       ] [PROSE   ] -> historical-precedents.md:10
        resolved : manuscript/ave-kb/common/historical-precedents.md
        excerpt  : Gamma_cauchy = M_tt - M_tr M_rr^{-1} M_rt
        at-line  : AVE re-ties **two threads from 19th-century physics, both shelved by ~1900** — Maxwell's quaternion / longitudinal electromagnetism, and Kelvin's vort
   57. :144   [absent       ] [PROSE   ] -> physics-lineage-map.md:357
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : Gamma_cauchy = M_tt - M_tr M_rr^{-1} M_rt
        at-line  : ### T8 — Gabriel Kron: network models of field equations (1930s–40s) · feeds F12
   58. :153   [absent       ] [PROSE   ] -> the-sourced-charge-no-go-cascade.md:94
        resolved : manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md
        excerpt  : b −= b.mean()
        at-line  : §R1): the Dirichlet energy `φᵀ L_w φ = Σ_edge ε_eff·(Δφ)²` vanishes iff every term
   59. :172   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/electron-identification.md:165
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md
        excerpt  : clm-p5cf3t
        at-line  : - [`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md` line 18](../../../vol4/circuit-theory/ch1-vacuu
   60. :172   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md:52
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md
        excerpt  : clm-p5cf3t
        at-line  : E_{\text{reactive}} = \frac{1}{2} L_{\text{tube}} I_{\max}^2 = \frac{1}{2} C_{\text{tube}} V_{\text{peak}}^2
   61. :174   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md:54
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md
        excerpt  : clm-p5cf3t
        at-line  : By the LC tank virial theorem (equipartition between magnetic and electric reactance: the peak-amplitude equality $\tfrac{1}{2}LI_{\max}^2 = \tfrac{1}
   62. :182   [absent       ] [PROSE   ] -> physics-lineage-map.md:359
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : static / DC / single-sign-susceptance
        at-line  : **Capsule.** A General Electric engineer spent three decades on one move: any linear physical system — rotating machine, elastic solid, Maxwell field,
   63. :183   [absent       ] [PROSE   ] -> engine-capability-map.md:356
        resolved : manuscript/ave-kb/common/engine-capability-map.md
        excerpt  : Z(omega) = j A (omega^2 - omega_zero^2) / [(omega^2 - omega_bond^2)(omega^2 - omega_anti^2)]
        at-line  : The F6 ε→T2 candidate has a **built, certified instrument** — the Foster/Caldeira–Leggett oscillator-comb bath meter (`src/ave/thermal/f6_bath_meter.p
   64. :218   [absent       ] [ID-TOKEN] -> physics-lineage-map.md:68
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : clm-mlwm3h
        at-line  : - **The branches:** (a) Kelvin 1867 vortex atoms — matter = knotted vortex tubes in the aether, species = knot type (Tait's tables = the birth of knot
   65. :220   [absent       ] [ID-TOKEN] -> physics-lineage-map.md:227
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : clm-mlwm3h
        at-line  : **Citations:** MacCullagh 1839/1848 (Trans. RIA 21); Cauchy 1839 (the "contractile"/"labile" aether, λ + 2μ = 0 — web-verified date + name via Whittak
   66. :227   [absent       ] [IDENT   ] -> ../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md:116
        resolved : manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md
        excerpt  : k2g-crystalline-provenance_prereg
        at-line  : | **$\sqrt{10/3}$** | 1.8257 | **P-wave (LONGITUDINAL)** speed ratio $c_P/c_S$ at the **VRH (Voigt-Reuss-Hill) average ONLY**: $(K+4G/3)/G=10/3$. A **
   67. :227   [absent       ] [IDENT   ] -> ../vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md:19
        resolved : manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md
        excerpt  : k2g-crystalline-provenance_prereg
        at-line  : **isotropic (Voigt–Reuss–Hill) average** scalar at $K = 2G$; the real srs/K4 lattice is
   68. :231   [moved        ] [SHORT   ] -> ../vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md:116  excerpt-actually-at [81, 147]
        resolved : manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md
        excerpt  : N_NU
        at-line  : | **$\sqrt{10/3}$** | 1.8257 | **P-wave (LONGITUDINAL)** speed ratio $c_P/c_S$ at the **VRH (Voigt-Reuss-Hill) average ONLY**: $(K+4G/3)/G=10/3$. A **
   69. :245   [absent       ] [ID-TOKEN] -> ../vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md:103
        resolved : manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md
        excerpt  : clm-91adfe
        at-line  : 2. **The electron's "bubble" $\neq$ the free photon, and $\neq$ a cavitation bubble.** The electron's core is its own $\Gamma=-1$ self-created $0\,\Om
   70. :245   [moved        ] [ID-TOKEN] -> ../vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md:25  excerpt-actually-at [6, 11]
        resolved : manuscript/ave-kb/vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md
        excerpt  : clm-91adfe
        at-line  : In the AVE framework, the constant density $\rho_0$ is replaced by the Axiom 4 saturated density:
   71. :274   [absent       ] [ID-TOKEN] -> ../vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:91
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md
        excerpt  : def-quant3
        at-line  : > the topological **$Q = \ell$ (cold flat-Q) is scoped to the a\*=0 anchor** — the $\Omega \to 0$ limit of
   72. :274   [absent       ] [ID-TOKEN] -> ../vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:91
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md
        excerpt  : def-quant3
        at-line  : > the topological **$Q = \ell$ (cold flat-Q) is scoped to the a\*=0 anchor** — the $\Omega \to 0$ limit of
   73. :274   [moved        ] [ID-TOKEN] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md:10  excerpt-actually-at [31]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md
        excerpt  : def-quant3
        at-line  : The substrate-foundational form of Op21 is the **mode-counting identity** $Q = \ell$ per Nyquist-cell-resolved confined mode at the substrate's $\Gamm
   74. :274   [absent       ] [ID-TOKEN] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:158
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : def-quant3
        at-line  : ## Q-glyph ownership (collapse-batch T10 — which "$Q$" a downstream cite means)
   75. :275   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md:54
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md
        excerpt  : def-quant3
        at-line  : | charge $-e$ (integer winding) | **B** (winding-sector L4) | clm-uatcql; def-3638f2 | FORM=chord (integer-ness from winding) / VALUE=DEFINITIONAL ($e
   76. :275   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/electron-identification.md:108
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md
        excerpt  : def-5d2b8a
        at-line  : - **FORM-derived (quantization / composition), VALUE imported or anchored:** charge $e$ — the **quantization / integer-ness** is FORM-derived (Ax2 TKI
   77. :275   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:96
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md
        excerpt  : def-5d2b8a
        at-line  : Three substrate-native inputs: the winding integer $n$ (the $(2,3)$: $w_{\text{tor}}=2$, $|\text{Link}|=1$);
   78. :275   [absent       ] [ID-TOKEN] -> ../vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md:96
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md
        excerpt  : def-3638f2
        at-line  : Three substrate-native inputs: the winding integer $n$ (the $(2,3)$: $w_{\text{tor}}=2$, $|\text{Link}|=1$);
   79. :275   [moved        ] [ID-TOKEN] -> vocabulary-register.md:272  excerpt-actually-at [261]
        resolved : manuscript/ave-kb/common/vocabulary-register.md
        excerpt  : def-quant3
        at-line  : - (2) **Winding integers** — the topologically-protected **graph** register (charge, the $(2,3)$, $\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$; def-
   80. :276   [absent       ] [PROSE   ] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:15
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : Q_TANK = 1/α
        at-line  : $$\boxed{\, \alpha^{-1} = Q_{\text{tank}} = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 124.025 + 9.870 + 3.142 
   81. :276   [absent       ] [PROSE   ] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:164
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : Q_TANK = 1/α
        at-line  : | **loaded / radiative $Q$** | $1/\alpha = 137.036$ | the vacuum↔EM coupling coefficient — an α-baked **ECHO** at the value level | this leaf `:15` / 
   82. :276   [absent       ] [PROSE   ] -> physics-lineage-map.md:390
        resolved : manuscript/ave-kb/common/physics-lineage-map.md
        excerpt  : Q_TANK = 1/α
        at-line  : | The BCS demotion (phenomenological constitutive law → "effective theory" once microscopics land) | STANDING | LIVE THREAT, honestly held: AVE is at 
   83. :289   [moved        ] [SHORT   ] -> claim-quality.md:1541  excerpt-actually-at [14, 56, 82, 126, 129]
        resolved : manuscript/ave-kb/common/claim-quality.md
        excerpt  : main
        at-line  : - **Does NOT re-open the #782 verdict.** BIN-4 is invariant across `β`; the banked bare-node `r_Z` values are **neither a floor nor a ceiling** of the
   84. :289   [moved        ] [SHORT   ] -> relative-offset-principle.md:57  excerpt-actually-at [25]
        resolved : manuscript/ave-kb/common/relative-offset-principle.md
        excerpt  : main
        at-line  : - **Fork-ρ source + the `r_Z`-band consequence (flag).** The `#782` RVE bench ([`research/2026-07-21_rve-aggregation-bench_result.md`](../../../resear
   85. :289   [moved        ] [SHORT   ] -> translation-tables/translation-circuit.md:334  excerpt-actually-at [41, 170, 236, 242, 264]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : main
        at-line  : | **F** | **The Hill (1963) / Huet (1990) / Hazanov–Huet (1994) two-sided apparent-modulus ordering** `C^SUBC ≤ C* ≤ C^KUBC` (prereg §1.3) | **The Dir
   86. :289   [moved        ] [SHORT   ] -> translation-tables/translation-circuit.md:334  excerpt-actually-at [41, 170, 236, 242, 264]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : main
        at-line  : | **F** | **The Hill (1963) / Huet (1990) / Hazanov–Huet (1994) two-sided apparent-modulus ordering** `C^SUBC ≤ C* ≤ C^KUBC` (prereg §1.3) | **The Dir
   87. :302   [absent       ] [IDENT   ] -> ../vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md:54
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/mass-closure-theorem.md
        excerpt  : common/translation-tables/
        at-line  : By the LC tank virial theorem (equipartition between magnetic and electric reactance: the peak-amplitude equality $\tfrac{1}{2}LI_{\max}^2 = \tfrac{1}

### manuscript/ave-kb/common/trampoline-framework.md   [6 finding(s)]
   88. :681   [moved        ] [ID-TOKEN] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
   89. :681   [moved        ] [ID-TOKEN] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
   90. :681   [moved        ] [ID-TOKEN] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
   91. :681   [absent       ] [ID-TOKEN] -> ../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:13
        resolved : manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md
        excerpt  : clm-533gvm
        at-line  : - Understand how orthogonal Field-Oriented Control (FOC) natively drives the emergence of the $p, d,$ and $f$ electron shells by eliminating macroscop
   92. :681   [absent       ] [ID-TOKEN] -> ../vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md:52
        resolved : manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-symmetric-cavity.md
        excerpt  : clm-533gvm
        at-line  : ### Field-Oriented Control (FOC) and the Secondary Density Wake
   93. :681   [absent       ] [ID-TOKEN] -> ../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md:28
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 MAGNETIC-BRANCH = SIGN-SELECTOR, NOT CAGE-MECHANISM (2026-06-18, Rule 12 / PR#260 B3-DEGENERATE — body below PRESERVED unedited; Grant-ratified)

### manuscript/ave-kb/common/translation-tables/translation-circuit.md   [9 finding(s)]
   94. :156   [absent       ] [PROSE   ] -> ../../vol4/claim-quality.md:1856
        resolved : manuscript/ave-kb/vol4/claim-quality.md
        excerpt  : …_prereg_FROZEN.md
        at-line  : - **UNIFORM-bias gauge-observability RIDER (CONSISTENCY re-expression of INVARIANT-S2).** The cell IS locally deficient under any held bias; readout i
   95. :191   [absent       ] [PROSE   ] -> ../operators.md:53
        resolved : manuscript/ave-kb/common/operators.md
        excerpt  : …alpha-quarter-hypothesis.md
        at-line  : | Op13 | D'Alembertian | $\Box^2$ (fully generalized wave equation operator) | 310 | CANONICAL by description — Vol 1 Ch 6 §1.12; uses local saturated
   96. :196   [absent       ] [PROSE   ] -> ../operators.md:45
        resolved : manuscript/ave-kb/common/operators.md
        excerpt  : vol_9…/05_ac_electrical_characteristics.tex
        at-line  : | Op5 | Multiport Y-to-S Conversion | $[S] = (I + [Y]/Y_0)^{-1}\cdot(I - [Y]/Y_0)$ | 225 | CANONICAL — explicit equation Vol 1 Ch 6 §1.5; applied at n
   97. :205   [moved        ] [ID-TOKEN] -> ../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md:106  excerpt-actually-at [5, 21]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md
        excerpt  : clm-vca7r1
        at-line  : > - **A1 longitudinal bond compliance:** $C_{eff}=C_0/S(V/V_{snap})$, DIVERGES at $V_{snap}$; small-signal tangent $C_{ss}=dQ/dV=C_0/S^3$ ([`device-ci
   98. :205   [moved        ] [ID-TOKEN] -> ../operators.md:42  excerpt-actually-at [144]
        resolved : manuscript/ave-kb/common/operators.md
        excerpt  : clm-invmtr
        at-line  : | Op2 | Universal Saturation Operator | $S(A, A_c) = \sqrt{1 - (A/A_c)^2}$ | 101 | CANONICAL — explicit equation Vol 1 Ch 6 §1.2. **A-034 EXPANDED CAT
   99. :223   [absent       ] [IDENT   ] -> ../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md:11
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-cross-sector-trading.md
        excerpt  : crystal_engine
        at-line  : A-012 canonical. Op14 saturation-driven impedance modulation transfers energy between substrate sectors via the bond LC tank's inductive side. **Empir
  100. :467   [absent       ] [PROSE   ] -> ../relative-offset-principle.md:57
        resolved : manuscript/ave-kb/common/relative-offset-principle.md
        excerpt  : E(rigid rotation) = 1.984e-3 > 0
        at-line  : - **Fork-ρ source + the `r_Z`-band consequence (flag).** The `#782` RVE bench ([`research/2026-07-21_rve-aggregation-bench_result.md`](../../../resear
  101. :467   [absent       ] [PROSE   ] -> ../the-sourced-charge-no-go-cascade.md:94
        resolved : manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md
        excerpt  : E(rigid rotation) = 1.984e-3 > 0
        at-line  : §R1): the Dirichlet energy `φᵀ L_w φ = Σ_edge ε_eff·(Δφ)²` vanishes iff every term
  102. :766   [absent       ] [IDENT   ] -> ../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md:107
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md
        excerpt  : ave-evidence-framing-discipline
        at-line  : >

### manuscript/ave-kb/common/vocabulary-register.md   [7 finding(s)]
  103. :421   [absent       ] [PROSE   ] -> trampoline-framework.md:685
        resolved : manuscript/ave-kb/common/trampoline-framework.md
        excerpt  : carrier × envelope
        at-line  : A boundary is a 2D surface, but practically it has a finite thickness — the **boundary envelope** is the 3D region where $A$ approaches the saturation
  104. :483   [absent       ] [IDENT   ] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md:36
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md
        excerpt  : BoundResonator
        at-line  : > **[Resultbox]** *The wall is not a perfect short — it leaks exactly $\alpha$ per cycle*
  105. :510   [absent       ] [PROSE   ] -> ../CLAUDE.md:73
        resolved : manuscript/ave-kb/CLAUDE.md
        excerpt  : status:proposed
        at-line  : - Axiom 4: **Universal Saturation Kernel** — $S(A) = \sqrt{1 - (A/A_{yield})^2}$ — universal quarter-arc kernel governing all 26 cross-scale saturatio
  106. :510   [absent       ] [PROSE   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : status:proposed
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  107. :518   [absent       ] [ID-TOKEN] -> ../CLAUDE.md:73
        resolved : manuscript/ave-kb/CLAUDE.md
        excerpt  : def-tk1xfm
        at-line  : - Axiom 4: **Universal Saturation Kernel** — $S(A) = \sqrt{1 - (A/A_{yield})^2}$ — universal quarter-arc kernel governing all 26 cross-scale saturatio
  108. :1039  [absent       ] [SHORT   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : [canon]
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  109. :1043  [absent       ] [SHORT   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : 5287ef32
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/common/window-blind-bounding-plane.md   [1 finding(s)]
  110. :16    [absent       ] [SHORT   ] -> ../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : no-claim:
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md   [3 finding(s)]
  111. :149   [absent       ] [ID-TOKEN] -> ../../../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md:28
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 MAGNETIC-BRANCH = SIGN-SELECTOR, NOT CAGE-MECHANISM (2026-06-18, Rule 12 / PR#260 B3-DEGENERATE — body below PRESERVED unedited; Grant-ratified)
  112. :149   [moved        ] [ID-TOKEN] -> ../../dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  113. :149   [moved        ] [ID-TOKEN] -> ../../dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/single-substrate-scale.md   [3 finding(s)]
  114. :24    [absent       ] [SHORT   ] -> ../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md:28
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md
        excerpt  : B_SNAP
        at-line  : At $v = 0$, the rest energy stored in the inductor's self-field is $E_0 = \tfrac{1}{2} L_0 I_{max}^2 = \tfrac{1}{2} (\xi_{topo}^{-2} m_0)(\xi_{topo} c
  115. :126   [moved        ] [ID-TOKEN] -> ../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md:28  excerpt-actually-at [5]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md
        excerpt  : clm-p5cf3t
        at-line  : At $v = 0$, the rest energy stored in the inductor's self-field is $E_0 = \tfrac{1}{2} L_0 I_{max}^2 = \tfrac{1}{2} (\xi_{topo}^{-2} m_0)(\xi_{topo} c
  116. :127   [absent       ] [PROSE   ] -> ../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md:15
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md
        excerpt  : m_e / ℓ_node
        at-line  : > L_{eff}(I) = \frac{L_0}{\sqrt{1 - \left(\dfrac{I}{I_{max}}\right)^{\!2}}}, \qquad I_{max} = \xi_{topo}\, c \approx 124.4 \text{ A}

### manuscript/ave-kb/vol1/claim-quality.md   [1 finding(s)]
  117. :1755  [moved        ] [IDENT   ] -> ../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md:92  excerpt-actually-at [118]
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md
        excerpt  : engine/p1b-modes-live
        at-line  : > \Sigma_b(\hat q\cdot\hat d_b)^4 = -\tfrac89\,(\hat q_x^4+\hat q_y^4+\hat q_z^4) + \tfrac43

### manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md   [2 finding(s)]
  118. :112   [absent       ] [SHORT   ] -> ohmic-decoherence-born.md:61
        resolved : manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md
        excerpt  : no-claim:
        at-line  : **Scope qualifier**: derivation applies to **AC signals or sign-symmetric signal ensembles** (the canonical Born-rule photodetection regime — oscillat
  119. :115   [moved        ] [SHORT   ] -> ../../../common/translation-tables/translation-circuit.md:207  excerpt-actually-at [224]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : 09722e2b
        at-line  : | Degenerate parametric amplifier (pump → signal/idler) | Op14 + $W_{refl}$ bridge (K4-$V^2$ → Cosserat-$\omega$) | ⚠ | the K4↔Cosserat coupling $W_{r

### manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/magnetic-saturation.md   [1 finding(s)]
  120. :34    [absent       ] [SHORT   ] -> ../../../vol3/cosmology/ch06-solar-system/kirkwood-gaps-cavity-modes.md:12
        resolved : manuscript/ave-kb/vol3/cosmology/ch06-solar-system/kirkwood-gaps-cavity-modes.md
        excerpt  : <0.3%
        at-line  : The asteroid belt gaps at mean-motion resonances with Jupiter are modelled as cavity modes in the gravitational impedance field: $a_{\text{gap}} = a_J

### manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md   [2 finding(s)]
  121. :36    [moved        ] [ID-TOKEN] -> ../../../common/claim-quality.md:773  excerpt-actually-at [795]
        resolved : manuscript/ave-kb/common/claim-quality.md
        excerpt  : clm-533gvm
        at-line  : - Does NOT claim a closed-form derivation of τ_relax in this leaf; the τ_relax window is taken from the Op14 vacuum-circuit work.
  122. :36    [moved        ] [ID-TOKEN] -> ../../../common/dark-wake-bemf-foc-synthesis.md:102  excerpt-actually-at [5, 86]
        resolved : manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md
        excerpt  : clm-533gvm
        at-line  : **This isomorphism suggests the same universal operator governs QNM decay, motor torque, and any co-rotating coupled oscillator.**

### manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md   [2 finding(s)]
  123. :79    [moved        ] [PROSE   ] -> ../../../common/translation-tables/translation-circuit.md:178  excerpt-actually-at [255]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : V_inc/V_ref ↔ Φ_link
        at-line  : > **Operator-citation provenance.** Every Op# below was grep-verified against [`operators.md`](../operators.md) §2 (the canonical 22-operator catalog)
  124. :96    [moved        ] [ID-TOKEN] -> ../../../common/translation-tables/translation-circuit.md:235  excerpt-actually-at [263, 750]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : clm-0ktpcn
        at-line  : <blank line>

### manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md   [2 finding(s)]
  125. :146   [moved        ] [ID-TOKEN] -> ../../dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  126. :146   [moved        ] [ID-TOKEN] -> ../../dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/chirality-and-antimatter.md   [6 finding(s)]
  127. :12    [absent       ] [ID-TOKEN] -> ../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : def-5d2b8a
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  128. :12    [absent       ] [ID-TOKEN] -> pair-production-axiom-derivation.md:27
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md
        excerpt  : def-5d2b8a
        at-line  : | Parity-conserving output | Two contra-rotating Beltrami vortices: $e^-$ (LH chirality) + $e^+$ (RH chirality); $m_e c^2$ each |
  129. :40    [moved        ] [ID-TOKEN] -> pair-production-axiom-derivation.md:27  excerpt-actually-at [5]
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md
        excerpt  : clm-ezai5b
        at-line  : | Parity-conserving output | Two contra-rotating Beltrami vortices: $e^-$ (LH chirality) + $e^+$ (RH chirality); $m_e c^2$ each |
  130. :41    [moved        ] [IDENT   ] -> pair-production-axiom-derivation.md:67  excerpt-actually-at [6, 136]
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md
        excerpt  : pair-production
        at-line  : The "rotational mode" at a node is the Cosserat microrotation $\omega$. Its per-node effective resonance $\Omega_{\text{node}}(A^2_{\text{local}})$ is
  131. :43    [moved        ] [ID-TOKEN] -> ../../../common/vocabulary-register.md:363  excerpt-actually-at [450, 451, 543, 703, 707]
        resolved : manuscript/ave-kb/common/vocabulary-register.md
        excerpt  : def-7c3f9e
        at-line  : - **canonical-home:** *(none — coinage; origin §43/§46/§47 epic adjudication)*
  132. :69    [absent       ] [ID-TOKEN] -> ../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : def-7c3f9e
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md   [5 finding(s)]
  133. :56    [absent       ] [PROSE   ] -> ../../../common/translation-tables/translation-circuit.md:637
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : finkelstein-misner:167
        at-line  : | Input noise voltage / current (1/f + thermal) | Substrate low-frequency-mode population (microrotational dispersion for 1/f) + Johnson-Nyquist subst
  134. :166   [moved        ] [IDENT   ] -> ../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:21  excerpt-actually-at [147]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : gamma_mag_sq_leak
        at-line  : > **Implementation note — two α-bakes and the EE-instrument echo-trap (2026-06-16; no-claim, factual description of `cvr_model.py`).** The $Q_{\text{t
  135. :174   [absent       ] [IDENT   ] -> ../../../common/boundary-observables-m-q-j.md:20
        resolved : manuscript/ave-kb/common/boundary-observables-m-q-j.md
        excerpt  : compute_Q_link
        at-line  : | $\mathcal{Q}$ | Boundary linking number | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ | **1D line/loop** | charge 
  136. :174   [absent       ] [IDENT   ] -> ../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : compute_Q_link
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  137. :174   [absent       ] [IDENT   ] -> torus-knot-uniqueness.md:23
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md
        excerpt  : compute_Q_link
        at-line  : | Hopf invariant (self-linking) | $Q_H = p \cdot q$ |

### manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/hollow-vortex-binding.md   [1 finding(s)]
  138. :46    [absent       ] [PROSE   ] -> ../../../../../research/2026-06-11_bubble-physics-completion.md:22
        resolved : research/2026-06-11_bubble-physics-completion.md
        excerpt  : RHO_CAV = -1/PHI
        at-line  : | cavitation floor ρ̄_cav | −1/φ ≈ −0.618034 | `src/ave/core/cavitation_flow.py:64` `RHO_CAV = −1/PHI` |

### manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md   [2 finding(s)]
  139. :14    [moved        ] [ID-TOKEN] -> ../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  140. :14    [moved        ] [ID-TOKEN] -> ../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20  excerpt-actually-at [36]
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : clm-533gvm
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md   [1 finding(s)]
  141. :157   [absent       ] [IDENT   ] -> ../../../common/dual-reactance-storage-taxonomy.md:221
        resolved : manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md
        excerpt  : docs/electron-proton-shape-walk
        at-line  : > **🔴 $X_L$ = the FLYWHEEL (spin/frequency-regulation) sector, NOT the rest-mass store (2026-06-20, Rule 12 — the "magnetic → $X_L$ → rest mass" gloss

### manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md   [1 finding(s)]
  142. :86    [absent       ] [IDENT   ] -> electron-bh-isomorphism.md:35
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md
        excerpt  : verify-before-cite
        at-line  : <blank line>

### manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md   [1 finding(s)]
  143. :27    [absent       ] [IDENT   ] -> ../../../common/the-abandoned-interior.md:183
        resolved : manuscript/ave-kb/common/the-abandoned-interior.md
        excerpt  : analysis/srs-chiral-micropolar
        at-line  : The Lorentzian construction buys **velocity only.** It says nothing about **structure**, and structure is where a lattice is most exposed. A discrete 

### manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md   [1 finding(s)]
  144. :26    [absent       ] [IDENT   ] -> ../ch03-macroscopic-relativity/refractive-index-of-gravity.md:14
        resolved : manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md
        excerpt  : consistency-vs-emergence
        at-line  : > $$

### manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/einstein-lensing-deflection.md   [2 finding(s)]
  145. :8     [absent       ] [IDENT   ] -> refractive-index-of-gravity.md:14
        resolved : manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md
        excerpt  : consistency-vs-emergence
        at-line  : > $$
  146. :14    [absent       ] [IDENT   ] -> refractive-index-of-gravity.md:14
        resolved : manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md
        excerpt  : consistency-vs-emergence
        at-line  : > $$

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-stability-eigenmode.md   [2 finding(s)]
  147. :19    [absent       ] [SHORT   ] -> ../../../common/translation-tables/translation-circuit.md:207
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : no-claim:
        at-line  : | Degenerate parametric amplifier (pump → signal/idler) | Op14 + $W_{refl}$ bridge (K4-$V^2$ → Cosserat-$\omega$) | ⚠ | the K4↔Cosserat coupling $W_{r
  148. :57    [moved        ] [IDENT   ] -> ../../../common/translation-tables/translation-circuit.md:207  excerpt-actually-at [224, 239]
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : crystal_engine
        at-line  : | Degenerate parametric amplifier (pump → signal/idler) | Op14 + $W_{refl}$ bridge (K4-$V^2$ → Cosserat-$\omega$) | ⚠ | the K4↔Cosserat coupling $W_{r

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-transfer-function.md   [1 finding(s)]
  149. :41    [absent       ] [PROSE   ] -> theorem-3-1-q-factor.md:81
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : pole_real/ω₀ = −0.00364868 = −α/2
        at-line  : - $Z_0$ is the vacuum's characteristic impedance through which any radiated energy would escape

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/graded-network-response.md   [3 finding(s)]
  150. :44    [moved        ] [SHORT   ] -> ../../claim-quality.md:391  excerpt-actually-at [112, 138, 259, 513, 541]
        resolved : manuscript/ave-kb/vol4/claim-quality.md
        excerpt  : main
        at-line  : <blank line>
  151. :289   [absent       ] [SHORT   ] -> ../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : src/ave
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  152. :341   [absent       ] [SHORT   ] -> ../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md:104
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md
        excerpt  : wejkhvnfb
        at-line  : $$\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1/2}{(2\alpha/15\pi)}\left(\frac{E_{crit}}{E_{yield}}\right)^2 = \frac{15\pi}{4\alpha^2} = \frac{3.75\

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/measurement-coupling-probe.md   [4 finding(s)]
  153. :13    [moved        ] [ID-TOKEN] -> ../../../common/vocabulary-register.md:569  excerpt-actually-at [716]
        resolved : manuscript/ave-kb/common/vocabulary-register.md
        excerpt  : def-gv1net
        at-line  : - **canonical-home:** *(no single home — Pitfall #5 / two-effective-speeds discipline at `manuscript/ave-kb/CLAUDE.md`; mode speeds at `vol1/dynamics/
  154. :60    [moved        ] [ID-TOKEN] -> ../../../common/vocabulary-register.md:324  excerpt-actually-at [435, 438, 441, 452, 510]
        resolved : manuscript/ave-kb/common/vocabulary-register.md
        excerpt  : def-tk1xfm
        at-line  : - **open-ambiguity-flag:** YES — the surface glyph ξ is overloaded by distinct objects:
  155. :273   [moved        ] [ID-TOKEN] -> ../../../common/vocabulary-register.md:324  excerpt-actually-at [435, 438, 441, 452, 510]
        resolved : manuscript/ave-kb/common/vocabulary-register.md
        excerpt  : def-tk1xfm
        at-line  : - **open-ambiguity-flag:** YES — the surface glyph ξ is overloaded by distinct objects:
  156. :325   [moved        ] [ID-TOKEN] -> ../../../common/vocabulary-register.md:569  excerpt-actually-at [716]
        resolved : manuscript/ave-kb/common/vocabulary-register.md
        excerpt  : def-gv1net
        at-line  : - **canonical-home:** *(no single home — Pitfall #5 / two-effective-speeds discipline at `manuscript/ave-kb/CLAUDE.md`; mode speeds at `vol1/dynamics/

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md   [3 finding(s)]
  157. :105   [absent       ] [ID-TOKEN] -> ../../../CLAUDE.md:73
        resolved : manuscript/ave-kb/CLAUDE.md
        excerpt  : def-vyvsn1
        at-line  : - Axiom 4: **Universal Saturation Kernel** — $S(A) = \sqrt{1 - (A/A_{yield})^2}$ — universal quarter-arc kernel governing all 26 cross-scale saturatio
  158. :105   [absent       ] [ID-TOKEN] -> ../../../CLAUDE.md:73
        resolved : manuscript/ave-kb/CLAUDE.md
        excerpt  : def-vyvsn1
        at-line  : - Axiom 4: **Universal Saturation Kernel** — $S(A) = \sqrt{1 - (A/A_{yield})^2}$ — universal quarter-arc kernel governing all 26 cross-scale saturatio
  159. :387   [absent       ] [ID-TOKEN] -> relativistic-inductor.md:15
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor.md
        excerpt  : def-vyvsn1
        at-line  : > L_{eff}(I) = \frac{L_0}{\sqrt{1 - \left(\dfrac{I}{I_{max}}\right)^{\!2}}}, \qquad I_{max} = \xi_{topo}\, c \approx 124.4 \text{ A}

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md   [1 finding(s)]
  160. :150   [absent       ] [IDENT   ] -> ../../../vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md:18
        resolved : manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/analog-ladder-filter.md
        excerpt  : ave-audit-of-audit
        at-line  : ```

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md   [1 finding(s)]
  161. :133   [absent       ] [SHORT   ] -> ../../../vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md:22
        resolved : manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md
        excerpt  : :14,38
        at-line  : | Bulk-longitudinal | $Z_{\mathrm{bulk}} = \rho_{\mathrm{bulk}}\,c_{\mathrm{bulk}}$ | $\sqrt{2}\,\rho_{\mathrm{bulk}}\,c_0$ | $\Gamma_{\mathrm{bulk}}\

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md   [1 finding(s)]
  162. :21    [absent       ] [PROSE   ] -> cvr-reflection-smith.md:32
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md
        excerpt  : gamma_em_sq()
        at-line  : On the Smith chart the locus runs straight along the real axis from the centre ($\Gamma=0$) to the left rim ($\Gamma=-1$): a pure resistance collapse 

### manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md   [1 finding(s)]
  163. :180   [moved        ] [SHORT   ] -> graded-network-response.md:109  excerpt-actually-at [120, 323, 342]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/graded-network-response.md
        excerpt  : wejkhvnfb
        at-line  : are derived; the **magnitude is imported** (per-dof:71), so this is a **FORM-level chord, not a

### manuscript/ave-kb/vol4/claim-quality.md   [4 finding(s)]
  164. :1142  [absent       ] [SHORT   ] -> ../vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md:95
        resolved : manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md
        excerpt  : 3–10 ms
        at-line  : |---|---|---|---|---|
  165. :1610  [absent       ] [IDENT   ] -> ./circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md:5
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-reflection-smith.md
        excerpt  : SubstrateExcitation
        at-line  : no-claim: "Consolidation / translation leaf (consistency-vs-emergence: CONSISTENCY, not emergence). The reflection-coefficient view of the electron wa
  166. :1614  [absent       ] [IDENT   ] -> ./circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:12
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md
        excerpt  : pole_real_over_w0
        at-line  : By applying the Topo-Kinematic mapping to the electron's rest mass, its equivalent localized Inductance evaluates to $L_e \equiv \xi_{topo}^{-2} m_e$.
  167. :1614  [absent       ] [IDENT   ] -> ./circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md:76
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/topological-kinematics.md
        excerpt  : pole_real_over_w0
        at-line  : > \quad \Longrightarrow \quad L = \xi_{topo}^{-2}\, m

### manuscript/ave-kb/vol6/appendix/geometric-inevitability/platonic-progression.md   [1 finding(s)]
  168. :14    [absent       ] [IDENT   ] -> ../../framework/mass-defect-summary.md:8
        resolved : manuscript/ave-kb/vol6/framework/mass-defect-summary.md
        excerpt  : consistency-vs-emergence
        at-line  : ## Macroscopic Mass Defect Summary

### manuscript/ave-kb/vol9/ch17-engine-requirements/engine-acceptance-suite.md   [1 finding(s)]
  169. :169   [absent       ] [PROSE   ] -> ../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : converter_on=False
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r

### manuscript/ave-kb/vol9/ch17-engine-requirements/index.md   [3 finding(s)]
  170. :19    [absent       ] [SHORT   ] -> ../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : ch3 index
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  171. :19    [absent       ] [SHORT   ] -> ../ch3-pin-port-configuration/device-circuit-models.md:201
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md
        excerpt  : ch3 index
        at-line  : **The Q slot stays EMPTY (strict anti-substitution).** The TARGET of the network is to derive the electron $Q$ from channel impedances + couplings (th
  172. :19    [absent       ] [SHORT   ] -> ../ch3-pin-port-configuration/index.md:18
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/index.md
        excerpt  : ch3 index
        at-line  : - **Sector-to-sector coupling matrix** over $\{\mathbf{E}(u), \mathbf{B}(\omega), V(A_1), A(\text{sat})\}$. Conservative $\mathbf{E}\leftrightarrow\ma

### manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md   [8 finding(s)]
  173. :60    [absent       ] [ID-TOKEN] -> ../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md:43
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/cvr-dc-operating-point.md
        excerpt  : def-tk1xfm
        at-line  : > — the **physical** exponent. The as-coded $S^{0.25}$ **understates** wall depth: downstream $\Gamma=(n-1)/(n+1)$
  174. :60    [absent       ] [PROSE   ] -> ../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:133
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md
        excerpt  : fig:vol9_electron_selfbiased_multiport
        at-line  : **Mixed impedance DOMAINS (units discipline).** Only $Z_{\mathrm{EM}}\equiv Z_0$ is an **electrical** impedance ($\Omega$, V/A); $Z_{\mathrm{shear}}$ 
  175. :159   [absent       ] [ID-TOKEN] -> ../../common/boundary-observables-m-q-j.md:43
        resolved : manuscript/ave-kb/common/boundary-observables-m-q-j.md
        excerpt  : sup-1ecv2m
        at-line  : The same three observables appear at every $\Gamma = -1$ saturation surface in the substrate hierarchy:
  176. :201   [absent       ] [ID-TOKEN] -> ../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:19
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : sup-wuy333
        at-line  : > **Value-scoped status (2026-06-14, keystone $\alpha$-verdict, auditor-gated).** This Key Result is the **Q-factor reframe** of $\alpha^{-1}$, not a 
  177. :201   [absent       ] [ID-TOKEN] -> ../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:21
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : sup-wuy333
        at-line  : > **Implementation note — two α-bakes and the EE-instrument echo-trap (2026-06-16; no-claim, factual description of `cvr_model.py`).** The $Q_{\text{t
  178. :205   [absent       ] [SHORT   ] -> ../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : ch17 index
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  179. :205   [absent       ] [SHORT   ] -> ../ch17-engine-requirements/index.md:19
        resolved : manuscript/ave-kb/vol9/ch17-engine-requirements/index.md
        excerpt  : ch17 index
        at-line  : - **Cross-sector couplings as CONSERVED Hamiltonian pairs** (source + back-reaction from one $H_{couple}$; energize-lock, no non-conservative pump — t
  180. :207   [moved        ] [SHORT   ] -> ../../../../src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py:243  excerpt-actually-at [432]
        resolved : src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py
        excerpt  : main
        at-line  : CLASS-INVARIANT FORM. ``Q`` is a REQUIRED keyword instance field (no electron

### manuscript/ave-kb/vol9/ch3-pin-port-configuration/index.md   [1 finding(s)]
  181. :18    [absent       ] [IDENT   ] -> device-circuit-models.md:201
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md
        excerpt  : _compute_emf_per_port
        at-line  : **The Q slot stays EMPTY (strict anti-substitution).** The TARGET of the network is to derive the electron $Q$ from channel impedances + couplings (th

### manuscript/ave-kb/vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md   [5 finding(s)]
  182. :21    [moved        ] [IDENT   ] -> device-circuit-models.md:52  excerpt-actually-at [20, 24, 31, 35, 113]
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md
        excerpt  : AVE_VACUUM_CELL
        at-line  : | Tank elements | $L_{\mathrm{cell}}=\mu_0\ell_{\mathrm{node}}$, $C_{\mathrm{cell}}=\varepsilon_0\ell_{\mathrm{node}}$ | `constants.py`; Ch.4 DC primi
  183. :21    [moved        ] [IDENT   ] -> device-circuit-models.md:127  excerpt-actually-at [20, 24, 31, 35, 113]
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md
        excerpt  : AVE_VACUUM_CELL
        at-line  : ↗ [`loop-gap-electron-resonator-closure-doctrine.md`](../../common/loop-gap-electron-resonator-closure-doctrine.md); `research/2026-06-12_loop-gap-ele
  184. :73    [absent       ] [SHORT   ] -> ../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md:41
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md
        excerpt  : ad26d357
        at-line  : > $\alpha/(15\pi)$ (carrier average) — is the same $\times4$-geometry $\times\tfrac12$-carrier chain; the
  185. :77    [moved        ] [IDENT   ] -> ../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md:92  excerpt-actually-at [113]
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md
        excerpt  : photon_birefringence
        at-line  : > \Sigma_b(\hat q\cdot\hat d_b)^4 = -\tfrac89\,(\hat q_x^4+\hat q_y^4+\hat q_z^4) + \tfrac43
  186. :101   [absent       ] [IDENT   ] -> ../../../../src/ave/core/k4_tlm.py:110
        resolved : src/ave/core/k4_tlm.py
        excerpt  : K4_BOND_DIRECTIONS
        at-line  : Type A joins B via:

### manuscript/ave-kb/vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md   [2 finding(s)]
  187. :46    [absent       ] [SHORT   ] -> ../../vol1/dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md:33
        resolved : manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md
        excerpt  : ad26d357
        at-line  : > **[Resultbox]** *Euler-Heisenberg $E^4$ Correction*
  188. :46    [absent       ] [SHORT   ] -> ../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md:41
        resolved : manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md
        excerpt  : ad26d357
        at-line  : > $\alpha/(15\pi)$ (carrier average) — is the same $\times4$-geometry $\times\tfrac12$-carrier chain; the

### manuscript/ave-kb/vol9/ch9-mechanical-characteristics/index.md   [1 finding(s)]
  189. :33    [absent       ] [SHORT   ] -> ../ch3-pin-port-configuration/device-circuit-models.md:143
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md
        excerpt  : NU_VAC
        at-line  : **Mixed impedance DOMAINS (units discipline — do NOT collapse to one unit).** The three channel values are NOT a single homogeneous set: only $Z_{\mat

### manuscript/ave-kb/vol9/claim-quality.md   [1 finding(s)]
  190. :511   [moved        ] [ID-TOKEN] -> ../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:19  excerpt-actually-at [5, 73]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md
        excerpt  : clm-rtdmsn
        at-line  : > **Value-scoped status (2026-06-14, keystone $\alpha$-verdict, auditor-gated).** This Key Result is the **Q-factor reframe** of $\alpha^{-1}$, not a 

### research/2026-05-18_abcd-eigensolver-workstream-handoff.md   [3 finding(s)]
  191. :245   [moved        ] [IDENT   ] -> research/_archive/L3_electron_soliton/68_phase_quadrature_methodology.md:62  excerpt-actually-at [13, 34]
        resolved : research/_archive/L3_electron_soliton/68_phase_quadrature_methodology.md
        excerpt  : VacuumEngine3D
        at-line  : ## 2. Phase-space Golden Torus framing (corpus citations)
  192. :247   [absent       ] [IDENT   ] -> research/_archive/L3_electron_soliton/130_q_g47_path_d_engine_cross_validation_first_pass.md:55
        resolved : research/_archive/L3_electron_soliton/130_q_g47_path_d_engine_cross_validation_first_pass.md
        excerpt  : MasterEquationFDTD
        at-line  : At the bound-state's operating amplitude A_op = V_peak_mean / V_yield = 0.324:
  193. :248   [absent       ] [IDENT   ] -> research/_archive/L3_electron_soliton/131_q_g47_path_d_full_two_engine_cross_validation_pass.md:50
        resolved : research/_archive/L3_electron_soliton/131_q_g47_path_d_full_two_engine_cross_validation_pass.md
        excerpt  : MasterEquationFDTD
        at-line  : | V_peak mean (late phase) | 0.2152 | settled breathing amplitude |

### research/2026-06-19_charge-quantization-gate_prereg.md   [3 finding(s)]
  194. :69    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/common/boundary-observables-m-q-j.md:20
        resolved : manuscript/ave-kb/common/boundary-observables-m-q-j.md
        excerpt  : 𝒬 = Link(∂Ω, F_substrate) ∈ ℤ
        at-line  : | $\mathcal{Q}$ | Boundary linking number | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ | **1D line/loop** | charge 
  195. :71    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md
        excerpt  : 𝒬 = H_bel = ∫ ω·(∇×ω)
        at-line  : > **🔴 TWO-"3"s DISAMBIGUATION (2026-06-10, Rule 12 — line above PRESERVED unedited; pre-adjudicated, Grant-ratified).** The phrase "the longitudinal r
  196. :85    [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:23
        resolved : manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md
        excerpt  : Q_H = p·q
        at-line  : | Hopf invariant (self-linking) | $Q_H = p \cdot q$ |

### research/2026-06-20_node-circulator-coupling.md   [1 finding(s)]
  197. :8     [absent       ] [IDENT   ] -> ../manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md:159
        resolved : manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md
        excerpt  : feat/node-2domain-nport
        at-line  : > **Status: OPEN.** The $\Gamma=-1$ TIR condition itself is canonical (clm-kezk9z; RUNG-1 T3.3 `sup-1ecv2m` — $\Gamma_{\mathrm{bulk}}$ crosses the OP2

### research/2026-06-24_forka-alpha-flip.md   [1 finding(s)]
  198. :6     [absent       ] [SHORT   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:138
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md
        excerpt  : R·r=¼
        at-line  : > - **The electron = a self-biased multi-port LC circuit at a self-set, self-stable Q-point.** Bias = the **saturation-state $A$** (the operating poin

### research/2026-06-30_electron-portmap-derivation_result.md   [1 finding(s)]
  199. :36    [moved        ] [SHORT   ] -> ../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md:136  excerpt-actually-at [54, 56]
        resolved : manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md
        excerpt  : Γ=−1
        at-line  : <blank line>

### research/2026-07-09_srs-band-survey_result.md   [1 finding(s)]
  200. :124   [absent       ] [PROSE   ] -> 2026-06-16_k4-zone-edge-nyquist-settle_result.json:25
        resolved : research/2026-06-16_k4-zone-edge-nyquist-settle_result.json
        excerpt  : band_top_omega = 1.9105 rad/step
        at-line  : "band_top_omega": 1.9105173215317497

### research/2026-07-26_d1-sector-and-inertia-route_scoping.md   [3 finding(s)]
  201. :39    [absent       ] [PROSE   ] -> ../manuscript/ave-kb/common/translation-tables/translation-circuit.md:306
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : git grep -n def-mstar1 origin/main
        at-line  : - **Effective mass $m^* = \hbar^2/(d^2E/dk^2)$ ↔ dispersion-read inertia** — a candidate derivation route for the D1 sector-crossed $c^2$ question, be
  202. :94    [moved        ] [ID-TOKEN] -> ../manuscript/ave-kb/common/relative-offset-principle.md:39  excerpt-actually-at [5, 11, 13, 17, 57]
        resolved : manuscript/ave-kb/common/relative-offset-principle.md
        excerpt  : clm-hu1jjw
        at-line  : **(C-kin) — kinematic participation (walk-ratified, UNCONDITIONAL).** Trapped-energy patterns **participate in any carrier's oscillatory material moti
  203. :115   [absent       ] [PROSE   ] -> ../manuscript/ave-kb/common/translation-tables/translation-circuit.md:156
        resolved : manuscript/ave-kb/common/translation-tables/translation-circuit.md
        excerpt  : WEP-CMRR ~1e-15
        at-line  : | **Equivalence principle** (gravitational charge $\equiv$ inertial mass) ⚠ regime-tag | **CMRR — COUPLING-level common-mode rejection.** **At the WEP

### research/2026-07-31_anisotropy-observable_scoping.md   [5 finding(s)]
  204. :259   [absent       ] [PROSE   ] -> 2026-07-04_parent-condition-match-forces-balance_result.md:24
        resolved : research/2026-07-04_parent-condition-match-forces-balance_result.md
        excerpt  : Γ_min = 1.5e-8
        at-line  : > ρ_bond = k_a/k_s lands on **ρ_bond = 1 (k_s = k_a) to machine precision** (ρ* = 0.99999999,
  205. :278   [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol4/claim-quality.md:733
        resolved : manuscript/ave-kb/vol4/claim-quality.md
        excerpt  : [requires-external-retrieval]
        at-line  : - Map the parity-odd $k$-linear term onto the explicit SME operator basis and show which Kostelecký coefficient it feeds, to sharpen the $\sim$11-OOM 
  206. :281   [absent       ] [PROSE   ] -> ../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md:22
        resolved : manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md
        excerpt  : [requires-external-retrieval]
        at-line  : | **Optical-scale anisotropy** | $\delta_{aniso} \sim (q\ell_{node})^4 \approx 2.2 \times 10^{-22}$ at $\lambda = 633$ nm; current cavity bounds $\sim
  207. :468   [absent       ] [ID-TOKEN] -> ../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md:15
        resolved : manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md
        excerpt  : clm-07kd5v
        at-line  : In the AVE framework, this is resolved because the geometric polarization of the LC network scales its dual reactive components symmetrically. The abs
  208. :1152  [absent       ] [PROSE   ] -> 2026-06-11_alpha-hand-of-god-framing.md:255
        resolved : research/2026-06-11_alpha-hand-of-god-framing.md
        excerpt  : [requires-external-retrieval]
        at-line  : | 2 | breathing-mode GW amplitude + polarization fraction from a melt event | the scalar/longitudinal ("breathing") GW amplitude a melt / crystallizat
```

---

## 6. What this branch changed, and what it deliberately did not

- **Changed:** `CITE_RE` (+ a `cite_path()` helper for the two branches), the Scope docstring
  (which previously said "optionally wrapped in backticks or a Markdown link" — ambiguous
  between the in-parens form the tool DID see and the after-parens form it did NOT), and a
  new regression test `manuscript/ave-kb/tools/tests/test_verify_anchor_content.py`.
- **Unchanged:** exit-code semantics. The tool returns `0` on every scan path, as before;
  `make verify` invokes it with a leading `-` (errors ignored) and no `--top`, and the
  standalone `make verify-anchor-content` target consumes the same always-0 contract.
  Confirmed by reading the Makefile, not assumed.
- **NOT changed:** any of the 208 anchors. Not one. Repair is per-owner triage.

> ⚑ **FLAGGED, not fixed — the checker scans its own test fixtures.**
> `verify-anchor-content.SKIP_DIRS` does **not** prune `tests/fixtures`, unlike its sibling
> `verify-md-links` (which carries an explicit `("tests", "fixtures")` skip pair). Harmless
> today — the existing fixtures produce `0` findings — but a latent trap: any on-disk
> stale-anchor fixture would be counted as corpus drift forever. This branch sidesteps it by
> building its fixture in a tmpdir (as the tool's own `--self-test` does) rather than by
> changing `SKIP_DIRS` mid-audit.
