# FROZEN PREREG — Kerr QNM reference-table correction + v2 ringdown-match re-adjudication

**Lane:** kerr-table-canon-correction (upstream follow-on of PR #772 adversarial review)
**Date frozen:** 2026-07-20
**Branch:** `fix/kerr-qnm-table-correction`
**Status of THIS document:** frozen reference + convention + plan + bins. Contains **no** verdict.
The re-run + adjudication land in a *separate later commit* against the bins frozen here.

---

## 0. What is being corrected (verified two independent methods, this session)

The in-repo Kerr (2,2,0) reference table `BERTI_KERR_QNM_TABLE` at
`src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py:122` — docstring claims
"numerical Leaver-method continued-fraction solutions — high precision (~1e-5 absolute
error)" — is **wrong at spin**. It is correct only at `a*=0`. The PR #772 adversarial
review found this by two independent methods (from-scratch Leaver + `qnm` package +
Berti-Cardoso-Will fitting formula); receipts at findings 0/1/5 of the #772 digest.

**This lane independently re-verified** the corrected values THIS session by two methods:
1. **`qnm` package** (Stein 2019, high-precision Leaver continued-fraction; `s=-2,l=2,m=2,n=0`)
   — reproduces the exact Schwarzschild anchor `0.373672` and the #772 digest receipts to
   all digits (0.70→0.53260, 0.80→0.58602, 0.90→0.67161, 0.95→0.74632).
2. **Berti-Cardoso-Will 2006 fitting formula** `ω_R M = 1.5251 − 1.1568(1−a*)^0.1292`
   (Phys.Rev. D73 064030) — agrees with the `qnm` values to **<1.5% at every spin**
   (worst point is a*=0, where the fit is known to be ~1.4% low; the exact Schwarzschild
   anchor is used for that row instead).

> **Verify-before-cite note (honest):** an attempt at a *from-scratch* Leaver solver in
> this lane's scratchpad carried a coefficient-convention bug (failed the Schwarzschild
> anchor) and is **not** cited. The independent second method used here is the BCW
> analytic fit, which reproduces the `qnm` values and the #772 auditor's independent
> from-scratch Leaver receipts. Three-source provenance therefore = {`qnm` package
> [this session + #772], BCW-2006 fit [this session], #772 auditor from-scratch Leaver}.

### Corrected Kerr (2,2,0) reference values (M=1 geometric units)

`ω_R·M` = qnm high-precision Leaver; `ω_I·M` = qnm (damping magnitude, exp(−ω_I t)):

| a* | ω_R·M (correct) | ω_R·M (in-repo, WRONG) | in-repo error | ω_I·M (correct) | ω_I·M (in-repo, WRONG) |
|----|-----------------|------------------------|---------------|-----------------|------------------------|
| 0.00 | 0.37367 | 0.37368 | ✓ (anchor) | 0.08896 | 0.08896 | ✓ |
| 0.10 | 0.38702 | 0.38659 | −0.1% | 0.08871 | 0.08882 | |
| 0.20 | 0.40215 | 0.40005 | −0.5% | 0.08831 | 0.08847 | |
| 0.30 | 0.41953 | 0.41442 | −1.2% | 0.08773 | 0.08793 | |
| 0.40 | 0.43984 | 0.42965 | −2.3% | 0.08688 | 0.08712 | |
| 0.50 | 0.46412 | 0.44597 | −3.9% | 0.08564 | 0.08597 | |
| 0.60 | 0.49404 | 0.46378 | −6.1% | 0.08377 | 0.08434 | |
| 0.64 | 0.50819 | (interp) | | 0.08275 | | |
| 0.67 | 0.51986 | (interp) | | 0.08185 | | |
| 0.70 | 0.53260 | 0.48267 | **−9.4%** | 0.08079 | 0.08197 | |
| 0.74 | 0.55163 | (interp) | | 0.07909 | | |
| 0.80 | 0.58602 | 0.50465 | **−13.9%** | 0.07563 | 0.07831 | +3.5% |
| 0.90 | 0.67161 | 0.53039 | **−21.0%** | 0.06487 | 0.07198 | **+11.0%** |
| 0.95 | 0.74632 | 0.54652 | **−26.8%** | 0.05315 | 0.06721 | **+26.5%** |

**Two corrupt tables, one file.** The `ω_R` corruption is the #772 finding. This lane
additionally finds the **`ω_I` (damping) table is corrupt in the same pattern** (high by
+11%/+26% at a*=0.90/0.95), which the #772 digest did not separately verify — surfaced
here, corrected alongside.

**Extremal ZDM cross-check.** The l=m=2 mode is a zero-damped mode: analytically
`ω_R·M → m/2 = 1.0` and `ω_I·M → 0` as a*→1. Corrected table respects it (`qnm` at
a*=0.998 gives ω_R·M=0.9385, ω_I·M=0.0145). In-repo table grossly violates it (heads to
~0.55, damping stays high). This is an independent analytic proof the in-repo values are wrong.

---

## 1. Frame-handling convention (FROZEN — detector-frame throughout)

The banked comparison mixed frames: it compared AVE-v2 frequency computed from a
**source-frame** final mass against a **detector-frame** observed frequency. Because QNM
frequency scales as `f ∝ 1/M`, the source-frame mass (≈9% lower than detector-frame) inflates
the predicted `f` by ≈9%, which is why a genuine deficit could read as a sub-percent match.

**Frozen conventions for the re-run:**

- **(C-1) Primary comparator = the dimensionless eigenvalue ratio.** Compare
  `(ω_R·M)_AVE-v2(a*)` against `(ω_R·M)_Kerr(a*)` at each event's spin. This ratio is
  **frame-independent AND mass-independent** — it depends only on the (well-measured) final
  spin a*, and sidesteps every mass/redshift/f_obs import. This is the substrate-native
  comparator (dimensionless eigenvalue vs dimensionless eigenvalue).
- **(C-2) Detector-frame masses for any frequency comparison.** `M_det = M_source·(1+z)`.
  The observed LIGO ringdown frequency is the detector-frame (redshifted) quantity, so the
  predicted frequency MUST use `M_det`. Per-event z (import, GWTC-1): GW150914 z=0.09,
  GW170104 z=0.18, GW151226 z=0.09.
- **(C-3) GR sanity gate.** True Kerr at `M_det` must reproduce the observed detector-frame
  ringdown (textbook GR ringdown-consistency test). Where the imported `(M, a*, f_obs)`
  triple fails this gate, the f_obs import is flagged as low-quality and that event's
  frequency comparison is treated as import-limited (the dimensionless C-1 comparator still holds).

---

## 2. Frozen re-run plan

Deterministic, no-network re-run (script hard-codes the qnm-verified corrected table;
does not import `qnm` at run time). For each of the leaf's three canonical events
(GW150914 a*=0.67, GW170104 a*=0.64, GW151226 a*=0.74):

1. Compute `(ω_R·M)_AVE-v2(a*)` from the unchanged v2 formula
   `x_sat(a*) = 2 + 5·r_ph⁺(a*)/3M`, `ω_R·M = ℓ(1+ν_vac)/x_sat`.
2. Compute `(ω_R·M)_Kerr(a*)` from the CORRECTED table.
3. **C-1 comparator:** `dev_dimensionless = (ω_R·M)_AVE-v2 / (ω_R·M)_Kerr − 1`.
4. **C-2 comparator:** `f_AVE-v2(M_det)` vs `f_obs`; and the GR gate `f_Kerr(M_det)` vs `f_obs`.
5. Report alongside: the BANKED reconstruction `f_AVE-v2(M_source)` vs `f_obs` (must
   reproduce the leaf's −2.0%/−1.2%/+1.9%, mean −0.45%, to confirm the frame-mixing model).

Cold-eigenvalue (a*=0) is reported separately: it is the genuine zero-free-parameter
result `18/49 = 0.36735` vs Kerr `0.37367` (−1.69%) and is NOT under adjudication here.

---

## 3. FROZEN adjudication bins (criteria set BEFORE the run)

Adjudication is on the spinning-remnant match (the banked "−0.45% mean ω_R, covers entire
LIGO BBH catalog at GR-class precision, FULL PASS"). Threshold on the mean honest
deviation `D̄` (mean of the C-1 dimensionless deviations across the three events;
cross-checked by the C-2 detector-frame deviation for GW150914):

- **MATCH-SURVIVES** — `|D̄| < 3%`. The −0.45%-class agreement persists under the
  corrected table + detector-frame convention. Re-bank the match as still-good; note the
  reference-table + frame corrections as bookkeeping that did not change the conclusion.
- **MATCH-ARTIFACT** — `|D̄| ≥ 5%`. The banked sub-percent agreement was compensating
  errors (source-vs-detector frame factor × the below-Kerr deficit). The honest v2-vs-data
  state is `D̄`. **Rule-11 bankable walk-back**: original banked −0.45%/−0.47% text
  preserved verbatim under dated supersession; honest `D̄` banked alongside; the
  C1-BH-RING "FULL PASS / recovers GR / covers entire catalog" claims re-graded; the cold
  a*=0 eigenvalue (−1.7%) explicitly preserved as the surviving genuine result.
- **MIXED per-event** — some events `|dev| < 3%`, others `≥ 5%`. Re-bank per event.
- **UNDETERMINED** — the imports are too poor for any C-1/C-2 comparator to decide
  (e.g. GR sanity gate C-3 fails for ALL events AND the dimensionless C-1 comparator is
  itself inside its own reference uncertainty). Suspend the bin pending better imports.

**Rule-11 discipline (frozen):** a decisive negative here is the discipline working, not a
failure to be rescued. If MATCH-ARTIFACT fires, the branch closes with the walk-back
banked (both the original text and the corrected number preserved); no post-hoc rescue,
no adjudication-criteria drift.

**Provenance-rider (frozen, per #772 finding 2):** `ν_vac = 2/7` is a corpus INPUT whose
VALUE is GR-imported via K=2G (PR #261), FORM-derived only. Any re-banked ORG-2-adjacent
number floored by ν_vac (e.g. the 54/77 extremal floor, the 18/49 cold eigenvalue)
inherits that grade. This lane does not re-derive ν_vac.
