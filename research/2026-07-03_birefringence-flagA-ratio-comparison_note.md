# FLAG-A — the two coexisting AVE/QED birefringence ratios: one-page comparison for Grant's leaf-promotion ruling

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12).** BOTH ratios compared here (`7.5/α³ ≈ 1.93×10⁷`
> differential, `4.14×10⁶` single-arm) use an understated QED denominator (too small by `1/(2πα) ≈ 21.8` —
> `(3/45)α²` and the `α³` single-arm form contradict the module's PVLAS-anchored magnetic leg at the `E↔cB`
> duality point). Corrected differential: `7.5π/α² ≈ 4.42×10⁵` (propagating). The observable-matching LOGIC of
> this note (differential ↔ polarimeter; single-arm ↔ interferometric probe) is unaffected — only the magnitudes
> change. See [`2026-07-03_birefringence-qed-normalization-correction.md`](2026-07-03_birefringence-qed-normalization-correction.md).

**Date:** 2026-07-03 · **Lane:** implementer · **Branch:** `analysis/birefringence-campaign-opening`
**Class:** ADJUDICATION MATERIAL — this note does NOT rule. It lays out the two ratios, which observable each pairs with, which one a real instrument reads, and where each appears in the corpus, for Grant's leaf-promotion decision (falsifier open-item #10 / R-1 residual).
**HEAD:** origin/main 93c7424d (both ratios live-verified this session).

---

## 0. The decision Grant owns

The falsifier doc's open-item #10 (`research/2026-06-21_birefringence-coefficient-bankable-falsifier.md:509-519`) flags that promoting the **par−perp differential** observable (−½A²) into the canonical claim `clm-pp3qwf` is **"an auditor/Grant call"**, tied to the R-1 residual (the differential is a NEW observable vs the leaf's historical scalar single-arm −¼A²). The leaf `vacuum-birefringence-e4.md` **already headlines the differential 1.93×10⁷** and keeps the single-arm 4.14×10⁶ as "traceability only." The open question is whether to **fully promote** the differential into the claim's canonical identity (retiring the single-arm to a footnote) OR **keep both** observable-matched (single-arm probe → 4.14×10⁶; differential ellipsometer → 1.93×10⁷). This note is the side-by-side for that call.

---

## 1. The two ratios (live-verified)

| | **Matched differential** | **Single-arm** |
|---|---|---|
| **Value** | `7.5/α³ = 1.9300×10⁷` | `1/(4·(7/45)·α³) = 4.1358×10⁶` |
| **AVE leg** | par−perp differential `δn_bir = n_∥ − n_⊥ = −½A²` | scalar single-arm (isotropic) `δn_iso = √S − 1 ≈ −¼A²` |
| **QED leg** | differenced Euler-Heisenberg `(3/45)α²(E/E_crit)²` (7/45 ∥ minus 4/45 ⊥) | parallel single-mode `(7/45)α²(E/E_crit)²` |
| **Closed form** | `(1/2)/((3/45)α²)·(E_crit/E_yield)² = (45/6)/α³` | `1/(4·(7/45)·α³)` |
| **α-structure** | α⁻³ (α⁻² tree-vs-loop × α⁻¹ E_yield import) — ECHO at value level | same α⁻³ — ECHO at value level |

Both ride the exact substrate identity `(E_crit/E_yield)² = 1/α` (verified live: 137.036). Both are field-independent. The **chord-vs-echo split is identical either way** (FORM = tree-O(1) saturation vs α²-loop = the chord; MAGNITUDE = α-echo). The physics verdict — AVE-distinct at all fields, ~6-7 OOM field-independent gap — does not depend on which ratio.

---

## 2. Which observable each pairs with — and which a real instrument reads

**This is the load-bearing distinction.**

- **A birefringence instrument (ellipsometer / X-ray dark-field polarimeter, PVLAS/BMV/HIBEF lineage) measures the par−perp DIFFERENTIAL** `n_∥ − n_⊥`. It rejects the isotropic common-mode shift (both eigenmodes see the same isotropic softening; the instrument reads only their difference). **→ a real birefringence instrument reads the 1.93×10⁷ ratio.** This is the GAP-1 campaign's observable (the HIBEF flip-prob is the differential; `research/2026-07-03_birefringence-gap1-hibef-feasibility_result.md`).

- **The single-arm 4.14×10⁶ pairs the AVE ISOTROPIC single-arm (−¼A²) against the QED PARALLEL single-mode (7/45).** Two framings coexist in the corpus for what this number IS:
  - **(a) "MISMATCHED / traceability-only"** (the leaf's + the survey's current framing, `vacuum-birefringence-e4.md:39,:71`): the AVE −¼ is the common-mode the polarimeter is BLIND to, and QED 7/45 is a single eigenmode — so pairing them compares quantities no single instrument reads together. Retained only for continuity with the historical headline.
  - **(b) "single-arm-retardance probe"** (FLAG-A #10's framing, `bankable-falsifier:517`): an instrument that measures an ABSOLUTE single-mode retardance (not a differential) — e.g. a single-pass phase measurement against a reference arm — would read the AVE single-arm against a QED single-mode, and 4.14×10⁶ is that ratio.

**The tension for Grant:** is 4.14×10⁶ (i) a mismatched artifact to footnote, or (ii) the legitimate ratio for a distinct (single-arm-retardance) instrument class that the campaign might also use? The number is the same; the physical status differs. A single-arm-retardance probe is not the HIBEF geometry, but it IS a real instrument class (interferometric single-pass phase).

---

## 3. Where each appears in the corpus (cite-chain, verified at HEAD)

**Matched differential (1.93×10⁷) — currently the headline:**
- Canonical leaf `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`: `:8` (title), `:22` (side-prediction), `:37` (boxed derivation), `:55` (falsifier statement), `:68` (R-1 reconciliation block).
- Claim body `vol4/claim-quality.md:427` (clm-pp3qwf `7.5/α³` ratio).
- Code `src/ave/bench/birefringence.py:328` `coefficient_ratio_differential()`; bench spec `adopters.py:138`.
- Register `research/2026-06-24_forward-prediction-register.md:153`.
- Falsifier doc `research/2026-06-21_birefringence-coefficient-bankable-falsifier.md:7-17` (R-1 resolution).

**Single-arm (4.14×10⁶) — currently traceability-only:**
- Leaf `vacuum-birefringence-e4.md:39,:71-72` (labeled MISMATCHED, traceability).
- Code `src/ave/bench/birefringence.py:309` `coefficient_ratio(a_eh=7/45)`.
- Falsifier doc body `:33-34,:42,:45` (the historical headline, now superseded per the doc's own :13 note) + `:517` (FLAG-A #10 single-arm-probe framing).
- Survey `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md:52-56` (carried as a band `[4×10⁵, 2×10⁷]`).

**The physical band (DERIVE-2, artifact-excluded):** single-arm ratios span `[4.14×10⁶ (7/45), 9.65×10⁶ (3/45)]`; the `a_EH≈1.45` PVLAS back-solve entry (→ 4.42×10⁵) is a `1/(2πα)` units artifact and must NOT anchor the low end (scout kill-lane flag; `birefringence.py:106` still ships it, LABELED do-not-use).

---

## 4. What is settled vs open (so the ruling is scoped)

**SETTLED (not part of the ruling):**
- The FORM is the chord, the MAGNITUDE is an α-echo — true at either ratio.
- A birefringence *ellipsometer/polarimeter* reads the differential (1.93×10⁷). The GAP-1 HIBEF campaign uses this. NOT in question.
- The `a_EH≈1.45` artifact is excluded. NOT in question.

**OPEN (the ruling):**
1. **Promote the differential fully into `clm-pp3qwf`'s canonical identity** (single-arm → footnote), OR **keep both observable-matched** (single-arm-retardance probe → 4.14×10⁶; differential ellipsometer → 1.93×10⁷)?
2. If keep-both: adopt framing **(a) mismatched-traceability** or **(b) single-arm-retardance-probe** for the 4.14×10⁶ number? (These carry different implications for whether a single-arm interferometric probe is a legitimate second campaign instrument.)

**Implementer recommendation (structure only, NOT a ruling):** the KEEP-BOTH discriminator pattern (a prior workspace lesson: when an audit finds a coexisting-ratio inconsistency, add the new axis alongside the legacy rather than redefine-in-place) argues for keep-both with framing (b) — it preserves the single-arm number for a real (interferometric single-arm) instrument class while headlining the differential for the HIBEF ellipsometer/polarimeter. But the leaf-promotion call is Grant's; this note lays out both cleanly.

---

**Provenance:** ratios live-verified (`coefficient_ratio_differential()=1.9300×10⁷`, `coefficient_ratio(7/45)=4.1358×10⁶`); all file:line cites confirmed at HEAD 93c7424d this session.
