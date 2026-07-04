# QED-normalization correction — the birefringence matched-differential ratio (Rule-12)

**Date:** 2026-07-03 · **Lane:** implementer · **Branch:** `analysis/birefringence-letter`
**Class:** CORRECTION (Rule-12 — preserve body, add dated header). Triggered by a two-lane hostile-referee pass
on the standalone Letter (PR #498). The AVE leg is UNAFFECTED; only the QED co-prediction normalization — and
therefore the AVE/QED ratio — is corrected.

---

## 0. The finding (verbatim, then verified)

The referee flagged: the QED electric-field birefringence coefficient `(3/45)α²(E/E_crit)²` used throughout the
campaign is **understated by exactly `1/(2πα) ≈ 21.81`** relative to the repo's OWN PVLAS-anchored magnetic leg,
which recovers the textbook `A_e = 1.32×10⁻²⁴ T⁻²`.

**Independent re-derivation this session (did NOT trust the referee):**
1. The magnetic differential `3 A_e B²` at `B = B_crit` is `3 A_e B_crit² = α/(30π) = 1.454 α²` — confirmed
   BOTH numerically (`7.7427×10⁻⁵`) AND analytically (`3·(2α²/45)·(ℏ³/(μ₀m⁴c⁵))·(m²c²/(eℏ))² = (6α²/45)/(4πα) =
   α/(30π)`, using `α = e²μ₀c/(4πℏ)`). This anchors to `A_e = 1.32×10⁻²⁴ T⁻²`, the community/PVLAS value.
2. The leading Euler-Heisenberg birefringent invariant is `(E²−B²)²`, which is `E↔cB` symmetric. So a probe
   crossing a **static E** must see the SAME differential coefficient as one crossing a static B at `B=E/c`:
   `Δn_static-E = α/(30π)·(E/E_crit)²`. NOT `(3/45)α² = 0.0667 α²`.
3. Ratio of the two: `[α/(30π)] / [(1/15)α²] = 15/(30πα) = 1/(2πα) = 21.81`. **Confirmed. The referee is right.**
4. Root cause in the code: the module comment `src/ave/bench/birefringence.py:92-97` claims the `3/45` electric
   leg comes from "PVLAS/BMV magnetic ... translated to a static E via B→E/c, c·B_crit==E_crit." But that
   translation gives `1.454 α²`, NOT `3/45`. The module's own `A_EH_LITERATURE` dict (`:106`) contains the
   correct `~1.45` value and labels it "order-of-magnitude EH" — then the drivers use `3/45` anyway. The comment
   is internally contradictory; the `3/45` electric leg is the bug.

## 1. The static-vs-propagating factor of 2 (surfaced BEYOND the referee — flag-don't-fix)

The referee anchored to `15π/α² ≈ 8.85×10⁵` using the **static-E** duality coefficient `α/(30π)`. But there is a
second external arbiter the referee (physics lane) did not fold in and the journal lane raised separately: the
**BIREF@HIBEF LoI Eq.19** (WebFetch-verified this session):

    N'/N = δ² = (4α²/225)(I_L/I_S)²(z/λ_X)²,   I_S = Sauter-Schwinger = 4.7×10²⁹ W/cm²

reproduces `~10⁻¹²` at `I_L = 10²¹` W/cm² (focus-integrated). Matching this to `δ² = π²(z/λ_X)²Δn²` implies, for a
**propagating** plane-wave pump (E and B co-moving, BOTH invariants active), a differential `α/(15π)` —
a **factor 2 larger** than the static-E value. This is a real static-vs-propagating physics distinction, NOT an
error. Since the HIBEF pump IS a propagating optical wave, the geometry-matched (and conservative, larger-QED)
headline is the propagating value:

| QED normalization | Δn coeff of (E/E_crit)² | ratio δn_AVE/δn_QED |
|---|---|---|
| **propagating (LoI-matched) — HEADLINE** | `α/(15π) = 2.908 α²` | **`7.5π/α² ≈ 4.42×10⁵`** |
| static-E duality (PVLAS-magnetic-matched) | `α/(30π) = 1.454 α²` | `15π/α² ≈ 8.85×10⁵` |
| ~~pre-fix (3/45), WRONG~~ | ~~`0.0667 α²`~~ | ~~`7.5/α³ ≈ 1.93×10⁷`~~ |

The AVE numerator is `1/(2α)` (from `−½(E_crit/E_yield)² = −½·(1/α)`), unchanged.

## 2. The corrected numbers (drivers re-run this session)

- **Ratio (dn):** `4.42×10⁵` propagating (headline) / `8.85×10⁵` static. Was `1.93×10⁷`.
- **QED P_flip (single-pass z=10µm, demonstrated pump):** `2.76×10⁻¹⁴` (9835 eV), `2.19×10⁻¹⁴` (8766 eV),
  `4.75×10⁻¹⁴` (12914 eV). Was `1.45/1.15/2.50×10⁻¹⁷`.
- **AVE P_flip (UNCHANGED):** `5.39/4.28/9.28×10⁻³`.
- **AVE/QED flip ratio per row:** `~1.95×10¹¹` (was `3.72×10¹⁴`).
- **Separation:** AVE↔QED ~11 OOM in flip-prob (was the inflated ~14).

## 3. Falsifier survival (Rule-11 — stated explicitly, both referees agree)

The kill-logic is **UNCHANGED**:
- AVE flip-prob `5.39×10⁻³` sits `2.25×10⁷` (~7.4 OOM) above the Marx-Schulze `2.4×10⁻¹⁰` polarimeter floor.
- Corrected QED flip-prob `2.76×10⁻¹⁴` sits `~8.7×10³` (~3.9 OOM) BELOW that floor.
- A pump-on null at/below the corrected QED co-prediction still kills the AVE E-sector; an AVE-sized signal still
  falsifies QED at this observable. The discriminator was always the coefficient GAP, and the gap survives.

## 4. Code changes (this branch)

- `src/ave/bench/birefringence.py`: ADDED `delta_n_qed_electric_pvlas(E, geometry=)` (propagating `α/15π` /
  static `α/30π`) and `coefficient_ratio_differential_pvlas(geometry=)`. The old `delta_n_qed` and
  `coefficient_ratio_differential` are PRESERVED with dated SUPERSEDED docstrings (do-not-use-for-prediction).
- The three campaign drivers now call the corrected leg (propagating). JSON outputs regenerated; the exposure
  figure regenerated (QED line ~3 OOM higher, AVE line unchanged, CLEAN-FIELD verdict preserved).
- `make verify` GREEN; drivers ruff-clean.

## 5. Corpus files carrying the superseded ratio (Rule-12 banners added / to add)

Canonical (banner added this branch): `manuscript/ave-kb/vol4/claim-quality.md` (clm-pp3qwf),
`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`.
Pointer-banners added: the campaign research docs (flagA promotion/ratio-comparison, gap1 prereg/result, the
registered prediction doc, the facility survey, the forward-prediction register, the bankable-falsifier).
Also carrying it: `manuscript/vol_4_engineering/chapters/12_falsifiable_predictions.tex`,
`manuscript/ave-kb/vol2/claim-quality.md`, `k4-bloch-dispersion-quartic.md`. All point here.

**Downstream (surfaced to the auditor, NOT landed by implementer):** a full inline sweep replacing every
`7.5/α³` → `7.5π/α²` and `1.93×10⁷` → `4.42×10⁵` (and the single-arm `4.14×10⁶` → its corrected `π`-form) across
the corpus is the auditor's to land as a canonical-propagation pass. This note + the dated banners are the Rule-12
preservation; the inline burn-down is the follow-on.
