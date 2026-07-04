# FLAG-A leaf-promotion — RULING (Grant-ratified 2026-07-03: "the matched-differential")

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12).** The `7.5/α³ ≈ 1.93×10⁷` and `4.14×10⁶` ratios in
> this ruling use an understated QED denominator (too small by `1/(2πα) ≈ 21.8`). Corrected differential ratio:
> `7.5π/α² ≈ 4.42×10⁵` (propagating). The ruling's SUBSTANCE (promote the matched-differential; KEEP-BOTH the
> single-arm) is unaffected — only the numeric ratio values change. See
> [`2026-07-03_birefringence-qed-normalization-correction.md`](2026-07-03_birefringence-qed-normalization-correction.md).

**Date:** 2026-07-03 · **Lane:** implementer (landing a Grant ruling) · **Branch:** `analysis/birefringence-prediction-doc`
**Class:** ADJUDICATION RULING — records Grant's decision on falsifier open-item #10 / R-1 residual and the
edits that land it. Comparison material that fed the decision:
[`2026-07-03_birefringence-flagA-ratio-comparison_note.md`](2026-07-03_birefringence-flagA-ratio-comparison_note.md).

---

## 0. The decision (verbatim)

Grant ruled, verbatim: **"the matched-differential."**

Interpreted against the comparison note's two-option framing (which the note laid out for exactly this call):
> OPEN ruling #1: **Promote the differential fully into `clm-pp3qwf`'s canonical identity** (single-arm →
> footnote), OR **keep both observable-matched**.

The ruling **promotes the matched-differential** ($\delta n_{bir}=-\tfrac12 A^2$, ratio $7.5/\alpha^3\approx
1.93\times10^7$) into the **canonical falsifier identity** of `clm-pp3qwf` and the leaf. The single-arm is not
retired to a bare footnote — it is retained **KEEP-BOTH** with its scope stated (comparison-note framing (b),
the single-arm-retardance-probe class), per the workspace KEEP-BOTH discriminator pattern.

---

## 1. What was promoted (the canonical identity)

**Matched differential (the falsifier headline):**
- Observable: par$-$perp differential $\delta n_{bir}=n_\parallel-n_\perp\approx-\tfrac12 A^2$, $A=E/E_{yield}$.
  DERIVED (uniaxial probe tensor $\varepsilon_{ij}=\varepsilon\delta_{ij}+2\varepsilon'E_{0i}E_{0j}$ = exact
  differential of the scalar Ax-4 kernel; OQ-1).
- QED leg, differenced the same way: $\delta n_{QED}=(3/45)\,\alpha^2(E/E_{crit})^2$ (Euler-Heisenberg $7/45\parallel$,
  $4/45\perp$ differenced).
- Matched field-independent ratio $\delta n_{AVE}/\delta n_{QED}=(1/2)/((3/45)\alpha^2)\cdot(E_{crit}/E_{yield})^2
  =(45/6)/\alpha^3=7.5/\alpha^3\approx1.9300\times10^7$ (live-verified: `coefficient_ratio_differential()`).
- This is the observable a real birefringence instrument (polarimeter / ellipsometer / X-ray dark-field
  polarimeter, PVLAS/BMV/HIBEF lineage) reads: it rejects the isotropic common-mode and measures $n_\parallel-n_\perp$.
  It is the GAP-1 HIBEF campaign's observable.

## 2. What was retained KEEP-BOTH (the scoped secondary)

**Single-arm / isotropic (the secondary, scope-stated):**
- The isotropic common-mode index shift $\delta n_{iso}=\sqrt S-1\approx-\tfrac14 A^2$ is the quantity a
  birefringence polarimeter is BLIND to (both eigenmodes see it; the instrument reads only their difference).
- Paired against the QED parallel single-mode $7/45$ it gives $1/(4\cdot\tfrac{7}{45}\,\alpha^3)\approx
  4.1358\times10^6$ (live-verified: `coefficient_ratio(7/45)`).
- **Scope (the KEEP-BOTH statement):** this $4.14\times10^6$ is the ratio a distinct **single-arm-retardance
  probe** — an interferometric single-pass absolute-phase instrument (not a differential polarimeter) — would
  read. It is a real instrument class, so the number is preserved for it. It is NOT the polarimeter/ellipsometer
  falsifier headline. Explicit pairing: single-arm-retardance probe $\to4.14\times10^6$; differential
  ellipsometer/polarimeter $\to1.93\times10^7$.
- The `a_EH\approx1.45` PVLAS back-solve entry (→ $4.42\times10^5$) is a $1/(2\pi\alpha)$ units artifact and does
  NOT anchor the band (it remains LABELED do-not-use in `birefringence.py`).

## 3. Physics unaffected by which ratio (settled, not part of the ruling)

- The **chord-vs-echo split is identical either way:** the CHORD is that the vacuum saturates at all (tree-level
  O(1) birefringence-bearing structure the QED $\alpha^2$-loop vacuum lacks); the MAGNITUDE ($1.93\times10^7$ or
  $4.14\times10^6$) is an $\alpha$-echo at the value level (symmetric standard: QED's $a_{EH}\alpha^2$ is equally
  $\alpha$-rooted). Do not headline the magnitude as a chord.
- The physics verdict — AVE-distinct at all fields, field-independent $\sim6$-$7$ OOM gap — does not depend on
  which ratio.

## 4. Where the ruling was landed (edits in this commit)

- Claim body `manuscript/ave-kb/vol4/claim-quality.md`:
  - `clm-pp3qwf` banner: title changed from "Differential-observable correction (2026-06-21)" to
    "Differential-observable PROMOTION (Grant-ratified 2026-07-03)"; added the KEEP-BOTH scope + ruling-note link.
  - Body AVE identity line: promoted to lead with the differential $-\tfrac12 A^2$ / $7.5/\alpha^3$; single-arm
    demoted to the scoped KEEP-BOTH secondary.
  - Specific-Claims line: headline ratio changed from "$\delta n\sim10^6\times$ QED (single-arm)" to
    "$\delta n_{bir}\approx1.93\times10^7\times$ QED at the matched differential."
- Canonical leaf `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`:
  - FLAG-A banner updated from "adjudicated 2026-06-21" to "PROMOTED (Grant-ratified 2026-07-03)"; KEEP-BOTH scope
    stated; single-arm framed as scoped secondary not traceability-only; ruling-note link added.
  - (Title, side-prediction, boxed derivation, and falsifier statement already headlined the differential per the
    2026-06-21 correction — unchanged.)

## 5. Downstream propagation (surfaced to the auditor, NOT landed here)

Per lane discipline, corpus-wide propagation of the promotion (below) is the auditor's to land — I surface it:
- `research/2026-06-21_birefringence-coefficient-bankable-falsifier.md:509-522` (FLAG-A #10 open-item) can be
  marked RESOLVED-by-ruling (the differential is promoted; single-arm KEEP-BOTH scoped).
- `research/2026-06-24_forward-prediction-register.md:153` already carries $7.5/\alpha^3$ (consistent; no change).
- `src/ave/bench/adopters.py` OBSERVABLE row already DERIVED on the differential (consistent).
- The survey `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md:52-56` carries the single-arm
  band `[4e5, 2e7]` — the auditor may annotate it with the promotion (headline = differential $1.93\times10^7$).

**Provenance:** ratios live-verified this session (`coefficient_ratio_differential()=1.9300\times10^7`,
`coefficient_ratio(7/45)=4.1358\times10^6`; substrate identity $(E_{crit}/E_{yield})^2=137.036=1/\alpha$).
`make verify` GREEN.
